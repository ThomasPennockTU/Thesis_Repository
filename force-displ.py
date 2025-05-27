# -*- coding: utf-8 -*-
from odbAccess import openOdb
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math
import numpy as np

# --- Settings ---
odb_path = '1.2-9 Block Flume pull test fd/Job-3.odb'
instance_name = 'BLOCK-2-LIN-1-5-LIN-11-1'
node_label = 33  # Reference node for displacement

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

# --- Get second step ---
step_names = odb.steps.keys()
if len(step_names) < 2:
    raise ValueError("ODB does not contain a second step.")
second_step = odb.steps[step_names[1]]
instance = odb.rootAssembly.instances[instance_name]

# --- Data storage ---
disp_vals = []
force_vals = []

# --- Loop over frames ---
for frame in second_step.frames:
    # --- Total contact force over all nodes (slope-normal) ---
    total_force_normal = 0.0
    cf_field = frame.fieldOutputs['CF']
    cf_subset = cf_field.getSubset(region=instance)
    for val in cf_subset.values:
        cf_global = np.array(val.data)
        cf_local = np.dot(R, cf_global)
        total_force_normal += cf_local[1]  # Normal to slope

    # --- Displacement of reference node (node_label) ---
    disp_normal = None
    u_field = frame.fieldOutputs['U']
    u_subset = u_field.getSubset(region=instance)
    for val in u_subset.values:
        if val.nodeLabel == node_label:
            u_global = np.array(val.data)
            u_local = np.dot(R, u_global)
            disp_normal = u_local[1]  # Normal to slope
            break

    # Store if both values were found
    if disp_normal is not None:
        disp_vals.append(disp_normal)
        force_vals.append(total_force_normal)

odb.close()

# --- Plot ---
plt.figure(figsize=(8, 5))
plt.plot(disp_vals, force_vals, marker='o')
plt.title(u'Total Contact Force vs. Displacement (Normal to 1:3 Slope)\nNode {} in {}'.format(
    node_label, instance_name))
plt.xlabel(u'Displacement Normal to Slope (m)')
plt.ylabel(u'Total Contact Force Normal to Slope (N)')
plt.grid(True)
plt.tight_layout()
plt.savefig("total_force_displacement_normal_node{}_{}.png".format(
    node_label, instance_name.replace('-', '_')))
