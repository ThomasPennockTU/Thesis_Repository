# -*- coding: utf-8 -*-
from odbAccess import openOdb
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math
import numpy as np

# --- Settings ---
odb_path = '../1.2-9 Block Flume pull test fd/Job-3.odb'
instance_name = 'BLOCK-2-LIN-1-5-LIN-11-1'
node_label = 33  # Reference node for displacement
node_set_name = 'Set-1'  # Defined in root assembly

# Define slope angle: 1 vertical to 3 horizontal
alpha = math.atan(1.0 / 3.0)  # ≈ 18.43 degrees

# Rotation around global Z-axis: global → slope-aligned local system
R = np.array([
    [math.cos(alpha), -math.sin(alpha), 0],
    [math.sin(alpha),  math.cos(alpha), 0],
    [0,                0,               1]
])

# --- Open ODB ---
odb = openOdb(path=odb_path)

# --- Get step ---
step_names = odb.steps.keys()
if len(step_names) < 2:
    raise ValueError("ODB does not contain a second step.")
second_step = odb.steps[step_names[1]]

# --- Get instance ---
if instance_name not in odb.rootAssembly.instances:
    raise ValueError("Instance '{}' not found in the ODB.".format(instance_name))
instance = odb.rootAssembly.instances[instance_name]

# --- Get node set from root assembly ---
try:
    node_set = odb.rootAssembly.nodeSets[node_set_name.upper()]
except KeyError:
    raise ValueError("Node set '{}' not found in rootAssembly.".format(node_set_name))

# --- Data storage ---
disp_vals = []
rf1p_vals = []  # Along slope
rf2p_vals = []  # Normal to slope
rf3p_vals = []  # Vertical
rf_total_normal = []  # Repeats RF2 for Figure A

# --- Loop over frames ---
for frame in second_step.frames:
    rf_field = frame.fieldOutputs['RF']
    rf_subset = rf_field.getSubset(region=node_set)

    sum_rf_local = np.zeros(3)

    for val in rf_subset.values:
        rf_global = np.array(val.data)
        rf_local = np.dot(R, rf_global)  # Transform to slope-aligned system
        sum_rf_local += rf_local

    rf1p_vals.append(sum_rf_local[0])  # Along slope
    rf2p_vals.append(sum_rf_local[1])  # Normal to slope
    rf3p_vals.append(sum_rf_local[2])  # Vertical
    rf_total_normal.append(sum_rf_local[1])  # For Figure A

    # Displacement of reference node
    disp_normal = None
    u_field = frame.fieldOutputs['U']
    u_subset = u_field.getSubset(region=instance)
    for val in u_subset.values:
        if val.nodeLabel == node_label:
            u_global = np.array(val.data)
            u_local = np.dot(R, u_global)
            disp_normal = u_local[1]  # Normal to slope
            break

    if disp_normal is not None:
        disp_vals.append(disp_normal)

odb.close()

# --- Plot A: RF normal to slope ---
plt.figure(figsize=(8, 5))
plt.plot(disp_vals, rf_total_normal, marker='o', label='RF normal to slope (RF2)')
plt.title('Figure A: Reaction Force Normal to 1:3 Slope\nNode {} in {}'.format(
    node_label, instance_name))
plt.xlabel('Displacement Normal to Slope (m)')
plt.ylabel('Total Reaction Force (N)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figure_a_rf_normal_tilted_node{}_{}.png".format(
    node_label, instance_name.replace('-', '_')))

# --- Plot B: slope-aligned RF components ---
plt.figure(figsize=(8, 5))
plt.plot(disp_vals, rf1p_vals, label="RF1 (along slope)", marker='o')
plt.plot(disp_vals, rf2p_vals, label="RF2 (normal to slope)", marker='s')
plt.plot(disp_vals, rf3p_vals, label="RF3 (vertical)", marker='^')
plt.title("Figure B: Slope-Aligned Reaction Force Components\nSet '{}' in {}".format(
    node_set_name, instance_name))
plt.xlabel("Displacement Normal to Slope (m)")
plt.ylabel("Reaction Force Components (N)")
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig("figure_b_rf_components_tilted_node{}_{}.png".format(
    node_label, instance_name.replace('-', '_')))
