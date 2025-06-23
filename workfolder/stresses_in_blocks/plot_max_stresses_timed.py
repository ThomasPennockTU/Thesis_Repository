# -*- coding: utf-8 -*-
from odbAccess import openOdb
from abaqusConstants import ELEMENT_NODAL
import numpy as np
import csv
import os

# --- Settings ---
odb_path = r'..\..\1.0-First delta flume\Job-amptest-1200.odb'
output_csv = 'max_principal_stress_per_block2.csv'
test = 0  # Set to 1 to run only the first frame, 0 for all

# --- Open ODB ---
if not os.path.exists(odb_path):
    raise IOError("ODB file not found: {}".format(odb_path))

odb = openOdb(odb_path)
step = odb.steps[odb.steps.keys()[-1]]  # Use the last step
frames = step.frames
all_instances = odb.rootAssembly.instances

# --- Filter block instances (names start with 'B-') ---
block_names = [name for name in all_instances.keys() if name.startswith('B-')]
block_names.sort()  # Optional: sort for consistent column order

# --- Prepare output table ---
header = ['Time'] + block_names
rows = []

# --- Limit number of frames if test mode is on ---
if test:
    frames = [frames[0]]

for frame_idx, frame in enumerate(frames):
    time = round(frame.frameValue, 2)
    print("Time step: {:.4f}".format(time))
    stress_field = frame.fieldOutputs['S']
    row = [time]

    for block_name in block_names:
        print("Processing block:", block_name)
        instance = all_instances[block_name]
        stress_subset = stress_field.getSubset(region=instance, position=ELEMENT_NODAL)

        max_princ = -1e20
        for val in stress_subset.values:
            s = val.data
            stress_tensor = np.array([
                [s[0], s[3], s[4]],
                [s[3], s[1], s[5]],
                [s[4], s[5], s[2]]
            ])
            principal_stresses = np.linalg.eigvalsh(stress_tensor)
            max_p = max(principal_stresses)
            if max_p > max_princ:
                max_princ = max_p

        row.append(max_princ if max_princ > -1e10 else '')

    rows.append(row)

odb.close()

# --- Write to CSV ---
with open(output_csv, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print("\n✅ Done. Max principal stress per block saved to '{}'".format(output_csv))