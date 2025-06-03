# -*- coding: utf-8 -*-
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

from odbAccess import openOdb
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import math
import os

# --- Settings ---
jobname = 'spinup_test'
odb_path = "../1.2-9 Block Flume pull test fd/{}.odb".format(jobname)
instance_name = 'BLOCK-2-LIN-1-5-LIN-11-1'
node_label = 33
set_names = ['whole', 'sides']  # Compare these two
print(odb_path)

# Slope angle: 1 vertical to 3 horizontal
alpha = math.atan(1.0 / 3.0)

# Rotation matrix (global → slope-aligned)
R = np.array([
    [math.cos(alpha), -math.sin(alpha), 0],
    [math.sin(alpha),  math.cos(alpha), 0],
    [0,                0,               1]
])

# --- Open ODB ---
odb = openOdb(path=str(odb_path))
step_keys = odb.steps.keys()
if len(step_keys) < 1:
    raise ValueError("ODB must contain at least one step.")
step1 = odb.steps[step_keys[0]]

# Get instance
if instance_name not in odb.rootAssembly.instances:
    raise ValueError("Instance '{}' not found.".format(instance_name))
instance = odb.rootAssembly.instances[instance_name]

# CNORMF key
def get_cnormf_key(step):
    for key in step.frames[0].fieldOutputs.keys():
        if key.startswith('CNORMF'):
            return key
    raise ValueError("CNORMF not found in step.")

cnormf_key_1 = get_cnormf_key(step1)

# --- Storage for each set ---
data = {}

# --- Step processor ---
def process_step(step, cnormf_key, region, instance):
    time_vals = []
    disp_vals = []
    cnormf1 = []
    cnormf2 = []
    cnormf3 = []

    for frame in step.frames:
        time = frame.frameValue
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

    tvals, dvals, c1, c2, c3 = process_step(step1, cnormf_key_1, region, instance)

    data[name] = {
        'time': tvals,
        'disp': dvals,
        'c1': c1,
        'c2': c2,
        'c3': c3
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
    'c1': "CNORMF1 (along slope)",
    'c2': "CNORMF2 (normal to slope)",
    'c3': "CNORMF3 (vertical)"
}

# --- Plot on both axes ---
for comp, ax, xkey in [('disp', ax1, 'Displacement Normal to Slope (m)'), ('time', ax2, 'Time (s)')]:
    for cid in ['c1', 'c2', 'c3']:
        # Whole block = solid
        ax.plot(data['whole'][comp], data['whole'][cid], label="Whole - " + labels[cid],
                linewidth=2, color=colors[cid])
        ax.fill_between(data['whole'][comp], data['whole'][cid], color=colors[cid], alpha=0.2)

        # Sides = dashed
        ax.plot(data['sides'][comp], data['sides'][cid], label="Sides - " + labels[cid],
                linewidth=2, linestyle='--', color=colors[cid])
        ax.fill_between(data['sides'][comp], data['sides'][cid], color=colors[cid], alpha=0.1)

    ax.set_xlabel(xkey)
    ax.set_ylabel("CNORMF Components (N)")
    ax.grid(True)
    ax.legend()

# --- Titles and save ---
ax1.set_title("CNORMF vs. Displacement (Whole vs. Sides)")
ax2.set_title("CNORMF vs. Time (Whole vs. Sides)")

plt.suptitle("Comparison of CNORMF - Job '{}' | Instance '{}'".format(jobname, instance_name), fontsize=14)
plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("cnormf_compare_{}_node{}_{}.png".format(
    jobname, node_label, instance_name.replace('-', '_')))
