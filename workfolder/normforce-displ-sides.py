# -*- coding: utf-8 -*-
from odbAccess import openOdb
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np

# --- Settings ---
odb_path = '../1.2-9 Block Flume pull test fd/Job-3.odb'
instance_name = 'BLOCK-2-LIN-1-5-LIN-11-1'
node_label = 176  # Target node
component_index = 2  # CNORMF3 is the third component (index 2)

# --- Open ODB ---
odb = openOdb(path=odb_path)

# --- Get instance ---
instance = odb.rootAssembly.instances[instance_name]

# --- Data storage ---
time_vals = []
cnormf3_vals = []

# --- Loop over all steps and frames ---
for step_name, step in odb.steps.items():
    for frame in step.frames:
        time = frame.frameValue

        if 'CNORMF' not in frame.fieldOutputs:
            continue

        cf_field = frame.fieldOutputs['CNORMF']
        cf_subset = cf_field.getSubset(region=instance)

        for val in cf_subset.values:
            if val.nodeLabel == node_label:
                cnormf3_vals.append(val.data[component_index])  # Z-component
                time_vals.append(time)
                break

odb.close()

# --- Output array format (time, CNORMF3) ---
cnormf3_array = np.column_stack((time_vals, cnormf3_vals))

# --- Print for inspection ---
print("Time (s) | CNORMF3 (N)")
for row in cnormf3_array:
    print("{:.5f} | {:.5f}".format(row[0], row[1]))

# --- Optional plot ---
plt.figure(figsize=(8, 5))
plt.plot(time_vals, cnormf3_vals, marker='o')
plt.title("CNORMF3 for Node {} over Time".format(node_label))
plt.xlabel("Time (s)")
plt.ylabel("CNORMF3 (N)")
plt.grid(True)
plt.tight_layout()
plt.savefig("cnormf3_node{}_vs_time.png".format(node_label))
