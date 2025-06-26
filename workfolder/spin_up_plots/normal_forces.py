# -*- coding: utf-8 -*-
from odbAccess import openOdb
from abaqusConstants import ELEMENT_NODAL
import numpy as np
import matplotlib
matplotlib.use('Agg')  # No GUI backend
import matplotlib.pyplot as plt
import math
import os

# --- Settings ---
odb_path = '../../1.0-First delta flume/Job-amptest-1200.odb'
instance_name = 'B-20-5'
output_file = 'normal_force_along_slope_B_20_5_auto.txt'
plot_file = 'normal_force_along_slope_B_20_5_plot.png'

# Define slope direction (1 vertical to 3 horizontal)
alpha = math.atan(1.0 / 3.0)
slope_vector = np.array([math.cos(alpha), math.sin(alpha), 0])  # Unit vector along slope

# --- Open ODB ---
if not os.path.exists(odb_path):
    raise IOError("ODB not found: {}".format(odb_path))

odb = openOdb(odb_path)

# Check instance
if instance_name.upper() not in odb.rootAssembly.instances:
    print("Available instances:")
    for key in odb.rootAssembly.instances.keys():
        print(" •", key)
    raise ValueError("Instance '{}' not found in ODB.".format(instance_name))

instance = odb.rootAssembly.instances[instance_name.upper()]

# --- Data storage ---
time_vals = []
force_along_slope_vals = []

# --- Process frames ---
def process_step(step, t_offset=0.0):
    for frame in step.frames:
        time = frame.frameValue + t_offset

        if 'CFORCE' not in frame.fieldOutputs:
            continue

        force_field = frame.fieldOutputs['CFORCE']
        subset = force_field.getSubset(region=instance, position=ELEMENT_NODAL)

        total_force = np.zeros(3)

        for val in subset.values:
            force_vec = np.array(val.data)
            if not np.allclose(force_vec, [0, 0, 0]):
                total_force += force_vec

        force_along_slope = np.dot(total_force, slope_vector)

        time_vals.append(time)
        force_along_slope_vals.append(force_along_slope)

# --- Loop over all steps ---
cumulative_time = 0.0
for step_name in odb.steps.keys():
    step = odb.steps[step_name]
    process_step(step, t_offset=cumulative_time)
    if step.frames:
        cumulative_time += step.frames[-1].frameValue

odb.close()

# --- Save text output ---
with open(output_file, 'w') as f:
    f.write("Time (s), Force Along Slope (N)\n")
    for t, fval in zip(time_vals, force_along_slope_vals):
        f.write("{:.4f}, {:.6f}\n".format(t, fval))

# --- Plotting (Unicode-safe for Python 2.7) ---
plt.figure(figsize=(10, 6))
plt.plot(time_vals, force_along_slope_vals, label=u'Force along slope (N)', marker='o')
plt.title(u'Total Contact Force Along Slope - B-20-5')
plt.xlabel(u'Time (s)')
plt.ylabel(u'Force (N)')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.savefig(plot_file)

print("✅ Results saved:\n - Text: '{}'\n - Plot: '{}'".format(output_file, plot_file))
