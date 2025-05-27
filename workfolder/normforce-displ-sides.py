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
node_set_name = 'sides'

# Define slope angle: 1 vertical to 3 horizontal
alpha = math.atan(1.0 / 3.0)

# Rotation matrix (global → slope-aligned)
R = np.array([
    [math.cos(alpha), -math.sin(alpha), 0],
    [math.sin(alpha),  math.cos(alpha), 0],
    [0,                0,               1]
])

# --- Open ODB ---
odb = openOdb(path=odb_path)

# Get both steps
step_keys = odb.steps.keys()
if len(step_keys) < 2:
    raise ValueError("ODB must contain at least two steps.")
step1 = odb.steps[step_keys[0]]
step2 = odb.steps[step_keys[1]]

# Get instance
if instance_name not in odb.rootAssembly.instances:
    raise ValueError("Instance '{}' not found.".format(instance_name))
instance = odb.rootAssembly.instances[instance_name]

# Get node set
try:
    node_set = odb.rootAssembly.nodeSets[node_set_name.upper()]
except KeyError:
    raise ValueError("Node set '{}' not found.".format(node_set_name))

# --- Find CNORMF key ---
def get_cnormf_key(step):
    for key in step.frames[0].fieldOutputs.keys():
        if key.startswith('CNORMF'):
            return key
    raise ValueError("CNORMF field not found in step.")

cnormf_key_1 = get_cnormf_key(step1)
cnormf_key_2 = get_cnormf_key(step2)

# --- Data storage ---
time_vals = []
disp_vals = []
cnormf1p_vals = []
cnormf2p_vals = []
cnormf3p_vals = []

# --- Function to process a step ---
def process_step(step, cnormf_key, t_offset=0.0):
    for frame in step.frames:
        time = frame.frameValue + t_offset
        field = frame.fieldOutputs[cnormf_key]
        subset = field.getSubset(region=node_set)

        sum_cnormf_local = np.zeros(3)

        for val in subset.values:
            cnormf_global = np.array(val.data)
            cnormf_local = np.dot(R, cnormf_global)
            sum_cnormf_local += cnormf_local

        cnormf1p_vals.append(sum_cnormf_local[0])
        cnormf2p_vals.append(sum_cnormf_local[1])
        cnormf3p_vals.append(sum_cnormf_local[2])
        time_vals.append(time)

        # Reference node displacement
        disp_normal = None
        u_field = frame.fieldOutputs['U']
        u_subset = u_field.getSubset(region=instance)
        for val in u_subset.values:
            if val.nodeLabel == node_label:
                u_global = np.array(val.data)
                u_local = np.dot(R, u_global)
                disp_normal = u_local[1]
                break

        if disp_normal is not None:
            disp_vals.append(disp_normal)

# --- Run both steps ---
process_step(step1, cnormf_key_1)
final_time_step1 = step1.frames[-1].frameValue
process_step(step2, cnormf_key_2, t_offset=final_time_step1)

odb.close()

# --- Create single figure with two subplots ---
fig, (ax1, ax2) = plt.subplots(1, 2, figsize=(14, 5))

# Left plot: CNORMF vs Displacement
ax1.plot(disp_vals, cnormf1p_vals, label=u"CNORMF1 (along slope)", marker='o')
ax1.plot(disp_vals, cnormf2p_vals, label=u"CNORMF2 (normal to slope)", marker='s')
ax1.plot(disp_vals, cnormf3p_vals, label=u"CNORMF3 (vertical)", marker='^')
ax1.set_title(u"CNORMF Components vs. Displacement")
ax1.set_xlabel(u"Displacement Normal to Slope (m)")
ax1.set_ylabel(u"CNORMF Components (N)")
ax1.grid(True)
ax1.legend()

# Right plot: CNORMF vs Time
ax2.plot(time_vals, cnormf1p_vals, label=u"CNORMF1 (along slope)", marker='o')
ax2.plot(time_vals, cnormf2p_vals, label=u"CNORMF2 (normal to slope)", marker='s')
ax2.plot(time_vals, cnormf3p_vals, label=u"CNORMF3 (vertical)", marker='^')
ax2.set_title(u"CNORMF Components vs. Time")
ax2.set_xlabel(u"Time (s)")
ax2.set_ylabel(u"CNORMF Components (N)")
ax2.grid(True)
ax2.legend()

plt.suptitle(u"Slope-Aligned CNORMF Components — Set '{}' in {}".format(
    node_set_name, instance_name), fontsize=14)

plt.tight_layout(rect=[0, 0, 1, 0.95])
plt.savefig("cnormf_slope_components_dual_node{}_{}_sides.png".format(
    node_label, instance_name.replace('-', '_')))
