# -*- coding: utf-8 -*-
from odbAccess import openOdb
import math
import csv

# === CONFIGURATION ===
odb_path = r'D:\tpennock\GitHub\Thesis_Repository\1.0-First delta flume final matrix\Job-H-0_6-1950_2.odb'
output_csv = 'uplift_downdrift_lastframe_maxcorners_06-1950_2.csv'

# === OPEN ODB ===
odb = openOdb(path=odb_path)
assembly = odb.rootAssembly

# === DEFINE SLOPE ANGLE ===
alpha_rad = math.atan(1.0 / 3.0)
cos_alpha = math.cos(alpha_rad)
sin_alpha = math.sin(alpha_rad)

# === DEFINE HALF BLOCKS ===
half_block_names = set(['B-%d-1' % i for i in range(1, 22, 2)] +
                       ['B-%d-10' % i for i in range(1, 22, 2)])
print("Half block names for control:")
print(sorted(half_block_names))

# === MAP BLOCK TO CORNER NODES ===
corner_nodes = [1, 8, 169, 176]

block_node_map = {}
for inst_name, inst in assembly.instances.items():
    if inst_name.startswith('B-'):
        if inst_name in half_block_names:
            # Still use node 52 for half blocks (or replace if you want corners for those too)
            block_node_map[inst_name] = [52]
        else:
            block_node_map[inst_name] = corner_nodes

# Sort blocks for consistent column order
sorted_blocks = sorted(block_node_map.keys())

# === GET LAST STEP ONLY ===
all_steps = sorted(odb.steps.keys())
last_step_name = all_steps[-1]
step = odb.steps[last_step_name]
n_total_frames = len(step.frames)
print("Processing last step: %s (%d frames)" % (last_step_name, n_total_frames))

# === PROCESS LAST FRAME OF LAST STEP ===
frame = step.frames[-1]
time = frame.frameValue
uplift_values = []
sliding_values = []
disp_field = frame.fieldOutputs['U']

for block in sorted_blocks:
    node_labels = block_node_map[block]
    inst = assembly.instances[block]
    
    block_uplifts = []
    block_slidings = []
    
    for node_label in node_labels:
        try:
            node = inst.getNodeFromLabel(node_label)
            disp = disp_field.getSubset(region=node).values[0]
            u1 = disp.data[0]
            u2 = disp.data[1]
            
            # Compute uplift (normal displacement)
            rel_uplift = u2 * cos_alpha - u1 * sin_alpha
            
            # Compute downdrift (sliding along slope)
            sliding = u1 * cos_alpha + u2 * sin_alpha

            block_uplifts.append(abs(rel_uplift))
            block_slidings.append(abs(sliding))
            
        except Exception as e:
            print("Warning: Skipped block %s, node %d: %s" % (block, node_label, str(e)))
            continue

    if len(block_uplifts) > 0:
        max_uplift = max(block_uplifts)
        max_sliding = max(block_slidings)
    else:
        max_uplift = None
        max_sliding = None

    uplift_values.append(max_uplift)
    sliding_values.append(max_sliding)

# === EXPORT TO CSV (PYTHON 2.7 COMPATIBLE) ===
uplift_headers = ['uplift_' + b for b in sorted_blocks]
sliding_headers = ['sliding_' + b for b in sorted_blocks]
header_row = ['Step', 'Time'] + uplift_headers + sliding_headers

with open(output_csv, 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(header_row)
    writer.writerow(
        [last_step_name, time] + uplift_values + sliding_values
    )

odb.close()
print("Export complete to '%s'" % output_csv)
