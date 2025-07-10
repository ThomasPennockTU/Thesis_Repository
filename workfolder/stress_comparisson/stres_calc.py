# -*- coding: utf-8 -*-
from odbAccess import openOdb
from abaqusConstants import ELEMENT_NODAL
import numpy as np
import csv
import os

# --- Settings ---
odb_path = r'..\..\1.0-First delta flume final C30 10p\Job-H-0_5.odb'
output_csv = 'max_principal_stress_of_highest_vm_block_H05_C30_10p.csv'
test = 0  # Set to 1 to run only the first 100 frames, 0 for all frames

# --- Open ODB ---
if not os.path.exists(odb_path):
    raise IOError("ODB file not found: {}".format(odb_path))

odb = openOdb(odb_path)
step = odb.steps[odb.steps.keys()[-1]]  # Use the last step
frames = step.frames
all_instances = odb.rootAssembly.instances

# --- Filter block instances (names start with 'B-') ---
block_names = [name for name in all_instances.keys() if name.startswith('B-')]
block_names.sort()

# --- Prepare CSV header ---
header = [
    "Time",
    "Block_with_Max_VM",
    "Block_Max_VM_Stress",
    "Max_Principal_Stress_in_Block",
    "Min_Principal_Stress_in_Block"
]

rows = []
rows.append(header)

# --- Determine number of frames ---
if test:
    n_frames = min(100, len(frames))
else:
    n_frames = len(frames)

print "ODB has {} frames. Processing {} frames...".format(len(frames), n_frames)

# --- Loop over frames ---
for frame_idx in range(n_frames):
    frame = frames[frame_idx]
    time = round(frame.frameValue, 4)
    print "Frame %3d | Time %.4f s" % (frame_idx + 1, time)

    stress_field = frame.fieldOutputs['S']

    # --- Phase 1: scan all blocks for max von Mises ---
    block_max_vm = {}
    for block_name in block_names:
        instance = all_instances[block_name]
        stress_subset = stress_field.getSubset(region=instance, position=ELEMENT_NODAL)

        max_vm = -1e20
        for val in stress_subset.values:
            vm_stress = val.mises
            if vm_stress > max_vm:
                max_vm = vm_stress

        block_max_vm[block_name] = max_vm

    # Find block with global max von Mises stress
    block_with_max_vm = max(block_max_vm, key=block_max_vm.get)
    max_vm_stress = block_max_vm[block_with_max_vm]

    # --- Phase 2: compute principal stresses for that block only ---
    instance = all_instances[block_with_max_vm]
    stress_subset = stress_field.getSubset(region=instance, position=ELEMENT_NODAL)

    max_princ = -1e20
    min_princ = 1e20

    for val in stress_subset.values:
        s = val.data
        stress_tensor = np.array([
            [s[0], s[3], s[4]],
            [s[3], s[1], s[5]],
            [s[4], s[5], s[2]]
        ])
        principal_stresses = np.linalg.eigvalsh(stress_tensor)

        max_p = max(principal_stresses)
        min_p = min(principal_stresses)

        if max_p > max_princ:
            max_princ = max_p
        if min_p < min_princ:
            min_princ = min_p

    # Append to CSV
    rows.append([
        time,
        block_with_max_vm,
        max_vm_stress if max_vm_stress > -1e10 else '',
        max_princ if max_princ > -1e10 else '',
        min_princ if min_princ < 1e10 else ''
    ])

odb.close()

# --- Write CSV ---
with open(output_csv, 'wb') as f:
    writer = csv.writer(f)
    writer.writerows(rows)

print ""
print "Done. Results saved to '%s'" % output_csv
