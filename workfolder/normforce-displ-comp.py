# -*- coding: utf-8 -*-
from odbAccess import openOdb
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import math

# --- Settings ---
odb_path = '../1.2-9 Block Flume pull test fd/Job-3.odb'
instance_name = 'BLOCK-2-LIN-1-5-LIN-11-1'
node_label = 33
set_names = ['whole', 'sides']  # Compare these two

# Slope angle: 1 vertical to 3 horizontal
alpha = math.atan(1.0 / 3.0)

# Rotation matrix (global → slope-aligned)
R = np.array([
    [math.cos(alpha), -math.sin(alpha), 0],
    [math.sin(alpha),  math.cos(alpha), 0],
    [0,                0,               1]
])

# --- Open ODB ---
odb = openOdb(path=odb_path)
step_keys = odb.steps.keys()
if len(step_keys) < 2:
    raise ValueError("ODB must contain at least two steps.")
step1 = odb.steps[step_keys[0]]
step2 = odb.steps[step_keys[1]]

# Get instance
if instance_name not in odb.rootAssembly.instances:
    raise ValueError("Instance '{}' not found.".format(instance_name))
instance = odb.rootAssembly.instances[instance_name]

# CNORMF keys
def get_cnormf_key(step):
    for key in step.frames[0].fieldOutputs.keys():
        if key.startswith('CNORMF'):
            return key
    raise ValueError("CNORMF not found in step.")

cnormf_key_1 = get_cnormf_key(step1)
cnormf_key_2 = get_cnormf_key(step2)

# --- Storage for each set ---
data = {}

# --- Step processor ---
def process_step(step, cnormf_key, region, instance, t_offset):
    time_vals = []
    disp_vals = []
    cnormf1 = []
    cnormf2 = []
    cnormf3 = []

    for frame in step.frames:
        time = frame.frameValue + t_offset
        field = frame.fieldOutputs[cnormf_key]
        subset = field.getSubset(region=region)

        sum_local = np.zeros(3)
        for val in subset.values:
            v_global = np.array(val.data)
            v_local = np.dot(R, v_global)
            sum_local += v_local

        cnormf1.append(sum_local[0])
        cnormf2.append(sum_local[1])
        cnormf3.append(sum_local[2])
        time_vals.append(time)

        # Displacement from reference node
        disp_normal = None
        u_field = frame.fieldOutputs['U']
        u_subset = u_field.getSubset(region=instance)
        for val in u_subset.values:
            if val.nodeLabel == node_label:
                u_local = np.dot(R, np.array(val.data))
                disp_normal = u_local[1]
                break
        if disp_normal is not None:
            disp_vals.append(disp_normal)

    return time_vals, disp_vals, cnormf1, cnormf2, cnormf3

# --- Loop over each node set name ---
for name in set_names:
    try:
        region = odb.rootAssembly.nodeSets[name.upper()]
    except KeyError:
        raise ValueError("Node set '{}' not found.".format(name))

    tvals1, dvals1, c1_1, c2_1, c3_1 = process_step(step1, cnormf_key_1, region, instance, 0.0)
    t_final_1 = step1.frames[-1].frameValue
    tvals2, dvals2, c1_2, c2_2, c3_2 = process_step(step2, cnormf_key_2, region, instance, t_final_1)

    data[name] = {
        'time': tvals1 + tvals2,
        'disp': dvals1 + dvals2,
        'c1': c1_1 + c1_2,
        'c2': c2_1 + c2_2,
        'c3': c3_1 + c3_2
    }

odb.close()

# --- Plot ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# --- Color setup ---
colors = {
    'c1': 'blue',
    'c2': 'green',
    'c3': 'orange'
}

labels = {
    'c1': u"CNORMF1 (along slope)",
    'c2': u"CNORMF2 (normal to slope)",
    'c3': u"CNORMF3 (vertical)"
}

# --- Plot on both axes ---
for comp, ax, xkey in [('disp', ax1, 'Displacement Normal to Slope (m)'), ('time', ax2, 'Time (s)')]:
    for cid in ['c1', 'c2', 'c3']:
        # Whole block = solid
        ax.plot(data['whole'][comp], data['whole'][cid], label=u"Whole – " + labels[cid],
                linewidth=2, color=colors[cid])
        ax.fill_between(data['whole'][comp], data['whole'][cid], color=colors[cid], alpha=0.2)

        # Sides = dashed
        ax.plot(data['sides'][comp], data['sides'][cid], label=u"Sides – " + labels[cid],
                linewidth=2, linestyle='--', color=colors[cid])
        ax.fill_between(data['sides'][comp], data['sides'][cid], color=colors[cid], alpha=0.1)

    ax.set_xlabel(u"{}".format(xkey))
    ax.set_ylabel(u"CNORMF Components (N)")
    ax.grid(True)
    ax.legend()

# --- Titles and save ---
ax1.set_title(u"CNORMF vs. Displacement (Whole vs. Sides)")
ax2.set_title(u"CNORMF vs. Time (Whole vs. Sides)")

plt.suptitle(u"Comparison of CNORMF (Whole vs. Sides) — Instance '{}'".format(instance_name), fontsize=14)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("cnormf_compare_whole_vs_sides_node{}_{}.png".format(
    node_label, instance_name.replace('-', '_')))
