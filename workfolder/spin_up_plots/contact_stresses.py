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
contact_node_set_name = 'whole'  # <-- Must match a node set defined on the contact surface
node_label = 33  # For output filename

# --- Open ODB ---
if not os.path.exists(odb_path):
    raise IOError("ODB not found: {}".format(odb_path))

odb = openOdb(odb_path)

# Check contact node set
if contact_node_set_name.upper() not in odb.rootAssembly.nodeSets:
    raise ValueError("Node set '{}' not found in ODB.".format(contact_node_set_name))

contact_nodes = odb.rootAssembly.nodeSets[contact_node_set_name.upper()]

# --- Data storage ---
time_vals = []
contact_pressures = []

# --- Process pressure per frame ---
def process_step(step, t_offset=0.0):
    for frame in step.frames:
        time = frame.frameValue + t_offset

        if 'CPRESS' not in frame.fieldOutputs:
            continue  # skip if no contact pressure available in this frame

        cpress_field = frame.fieldOutputs['CPRESS']
        subset = cpress_field.getSubset(region=contact_nodes, position=ELEMENT_NODAL)

        total_pressure = 0.0
        count = 0

        for val in subset.values:
            total_pressure += val.data
            count += 1

        avg_pressure = total_pressure / count if count > 0 else 0.0

        time_vals.append(time)
        contact_pressures.append(avg_pressure)

# --- Process all steps ---
cumulative_time = 0.0
for step_name in odb.steps.keys():
    step = odb.steps[step_name]
    process_step(step, t_offset=cumulative_time)
    if step.frames:
        cumulative_time += step.frames[-1].frameValue

odb.close()

# --- Plotting ---
fig, axs = plt.subplots(2, 1, figsize=(10, 8), sharex=False)

# -- Full time range --
axs[0].plot(time_vals, contact_pressures, label=u'Avg Contact Pressure', marker='o')
axs[0].set_title(u"Contact Pressure — Full Time Range")
axs[0].set_ylabel(u"Pressure (Pa)")
axs[0].grid(True)
axs[0].legend()

# -- Zoom 8–9 s --
axs[1].plot(time_vals, contact_pressures, label=u'Avg Contact Pressure', marker='o')
axs[1].set_xlim(8, 9)
axs[1].set_title(u"Contact Pressure — Zoom t = 8–9 s")
axs[1].set_xlabel(u"Time (s)")
axs[1].set_ylabel(u"Pressure (Pa)")
axs[1].grid(True)
axs[1].legend()

plt.tight_layout()
plt.savefig("contact_pressure_node{}_{}.png".format(
    node_label, contact_node_set_name.replace('-', '_')))
