# -*- coding: utf-8 -*-
from odbAccess import openOdb
from abaqusConstants import ELEMENT_NODAL
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import math
import os

# --- Settings ---
odb_path = '../../1.2-9 Block Flume pull test fd/3_spinup_test_spaced.odb'
instance_name = 'BLOCK-2-LIN-1-5-LIN-11-1'
node_label = 33  # For filename only

# Slope angle: 1 vertical to 3 horizontal
alpha = math.atan(1.0 / 3.0)

# Rotation matrix (global → local slope-aligned)
R = np.array([
    [math.cos(alpha), -math.sin(alpha), 0],
    [math.sin(alpha),  math.cos(alpha), 0],
    [0,                0,               1]
])

# --- Open ODB ---
if not os.path.exists(odb_path):
    raise IOError("ODB not found: {}".format(odb_path))

odb = openOdb(odb_path)
if instance_name not in odb.rootAssembly.instances:
    raise ValueError("Instance '{}' not found.".format(instance_name))

instance = odb.rootAssembly.instances[instance_name]

# --- Data storage ---
time_vals = []
s11_local = []
s22_local = []
s33_local = []
s11_global = []
s22_global = []
s33_global = []

# --- Process stress per frame ---
def process_step(step, t_offset=0.0):
    for frame in step.frames:
        time = frame.frameValue + t_offset
        stress_field = frame.fieldOutputs['S']
        subset = stress_field.getSubset(region=instance, position=ELEMENT_NODAL)

        sum_local = np.zeros(3)
        sum_global = np.zeros(3)
        count = 0

        for val in subset.values:
            s = val.data
            sigma = np.array([
                [s[0], s[3], s[5]],
                [s[3], s[1], s[4]],
                [s[5], s[4], s[2]]
            ])
            sigma_local = np.dot(R, np.dot(sigma, R.T))

            sum_local += np.array([sigma_local[0, 0], sigma_local[1, 1], sigma_local[2, 2]])
            sum_global += np.array([sigma[0, 0], sigma[1, 1], sigma[2, 2]])
            count += 1

        if count > 0:
            avg_local = sum_local / count
            avg_global = sum_global / count

            time_vals.append(time)
            s11_local.append(avg_local[0])
            s22_local.append(avg_local[1])
            s33_local.append(avg_local[2])
            s11_global.append(avg_global[0])
            s22_global.append(avg_global[1])
            s33_global.append(avg_global[2])

# --- Process all steps ---
cumulative_time = 0.0
for step_name in odb.steps.keys():
    step = odb.steps[step_name]
    process_step(step, t_offset=cumulative_time)
    if step.frames:
        cumulative_time += step.frames[-1].frameValue

odb.close()

# --- Plotting ---
fig, axs = plt.subplots(3, 1, figsize=(10, 12), sharex=False)

# -- Full time range, local slope --
axs[0].plot(time_vals, s11_local, label=u'$\sigma_{11}$ (along slope)', marker='o')
axs[0].plot(time_vals, s22_local, label=u'$\sigma_{22}$ (normal to slope)', marker='s')
axs[0].plot(time_vals, s33_local, label=u'$\sigma_{33}$ (vertical)', marker='^')
axs[0].set_title(u"Full Time Range: Local Slope-Aligned Stress")
axs[0].set_ylabel(u"Stress (Pa)")
axs[0].grid(True)
axs[0].legend()

# -- Zoomed local slope, t = 8–9 s --
axs[1].plot(time_vals, s11_local, label=u'$\sigma_{11}$ (along slope)', marker='o')
axs[1].plot(time_vals, s22_local, label=u'$\sigma_{22}$ (normal to slope)', marker='s')
axs[1].plot(time_vals, s33_local, label=u'$\sigma_{33}$ (vertical)', marker='^')
axs[1].set_xlim(8, 9)
axs[1].set_ylim(-5000, 5000)
axs[1].set_title(u"Zoom t = 8–9 s: Local Slope-Aligned Stress")
axs[1].set_ylabel(u"Stress (Pa)")
axs[1].grid(True)
axs[1].legend()

# -- Zoomed global slope, t = 8–9 s --
axs[2].plot(time_vals, s11_global, label=u'$\sigma_{11}$ (global X)', marker='o')
axs[2].plot(time_vals, s22_global, label=u'$\sigma_{22}$ (global Y)', marker='s')
axs[2].plot(time_vals, s33_global, label=u'$\sigma_{33}$ (global Z)', marker='^')
axs[2].set_xlim(8, 9)
axs[2].set_ylim(-5000, 5000)
axs[2].set_title(u"Zoom t = 8–9 s: Global (Unrotated) Stress")
axs[2].set_xlabel(u"Time (s)")
axs[2].set_ylabel(u"Stress (Pa)")
axs[2].grid(True)
axs[2].legend()

plt.tight_layout()
plt.savefig("stress_local_and_global_zoom_node{}_{}.png".format(
    node_label, instance_name.replace('-', '_')))
