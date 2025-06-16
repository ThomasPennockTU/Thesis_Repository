# -*- coding: utf-8 -*-
from odbAccess import openOdb
from abaqusConstants import ELEMENT_NODAL
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
import os
import re

# --- Settings ---
odb_path = r'..\1.0-First delta flume\Job-amptest-1200.odb'

if not os.path.exists(odb_path):
    raise IOError("File not found: {}".format(odb_path))

# --- Open ODB ---
odb = openOdb(path=odb_path)
step_names = list(odb.steps.keys())
if len(step_names) == 0:
    raise ValueError("No steps found in ODB.")
step_name = step_names[-1]
step = odb.steps[step_name]

# --- Filter relevant block instances ---
all_instances = odb.rootAssembly.instances.keys()
block_instances = [name for name in all_instances if re.match(r'BLOCK-2-LIN-1-2-LIN-\d+-1$', name)]

# Sort block instances numerically on the column number
def get_block_number(name):
    match = re.search(r'LIN-(\d+)-1$', name)
    return int(match.group(1)) if match else 999

block_instances = sorted(block_instances, key=get_block_number)

# --- Extract max principal stress per block ---
max_principal_stresses = []

for inst_name in block_instances:
    instance = odb.rootAssembly.instances[inst_name]
    max_principal = -1e20

    for frame in step.frames:
        if 'S' not in frame.fieldOutputs:
            continue

        stress_field = frame.fieldOutputs['S']
        stress_subset = stress_field.getSubset(region=instance, position=ELEMENT_NODAL)

        for val in stress_subset.values:
            stress_tensor = val.data
            stress_matrix = np.array([
                [stress_tensor[0], stress_tensor[3], stress_tensor[4]],
                [stress_tensor[3], stress_tensor[1], stress_tensor[5]],
                [stress_tensor[4], stress_tensor[5], stress_tensor[2]]
            ])
            principal_stresses = np.linalg.eigvalsh(stress_matrix)
            max_princ = max(principal_stresses)
            if max_princ > max_principal:
                max_principal = max_princ

    max_principal_stresses.append(max_principal)

odb.close()

# --- Plot bar chart ---
plt.figure(figsize=(12, 6))
x_labels = ['B{}'.format(get_block_number(name)) for name in block_instances]
plt.bar(x_labels, max_principal_stresses)
plt.title("Max Principal Stress per Block\nStep: {}".format(step_name))
plt.xlabel("Block ID (Column)")
plt.ylabel("Max Principal Stress (Pa)")
plt.grid(axis='y')
plt.tight_layout()
plt.savefig("bar_max_principal_stress_all_blocks.png")
