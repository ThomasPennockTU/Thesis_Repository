# -*- coding: utf-8 -*-
from odbAccess import openOdb
import math
import csv

# === CONFIGURATION ===
odb_path = r'D:\tpennock\GitHub\Thesis_Repository\1.0-First delta flume final\Job-H-1_0.odb'
output_csv = 'relative_uplift_timeseries_10.csv'

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

# === MAP BLOCK TO NODE LABEL ===
block_node_map = {}
for inst_name, inst in assembly.instances.items():
    if inst_name.startswith('B-'):
        node_label = 52 if inst_name in half_block_names else 100
        block_node_map[inst_name] = node_label

# Sort blocks for consistent column order
sorted_blocks = sorted(block_node_map.keys())

# === EXTRACT RELATIVE UPLIFT PER TIME FRAME FROM ALL STEPS ===
all_frame_data = []

for step_name, step in odb.steps.items():
    n_total_frames = len(step.frames)
    print("Processing step: %s (%d frames)" % (step_name, n_total_frames))
    
    for i in range(n_total_frames):
        frame = step.frames[i]
        time = frame.frameValue
        uplift_values = []
        disp_field = frame.fieldOutputs['U']

        for block in sorted_blocks:
            node_label = block_node_map[block]
            inst = assembly.instances[block]
            try:
                node = inst.getNodeFromLabel(node_label)
                disp = disp_field.getSubset(region=node).values[0]
                u1 = disp.data[0]
                u2 = disp.data[1]
                rel_uplift = u2 * cos_alpha - u1 * sin_alpha
            except Exception as e:
                print("Warning: Skipped block %s: %s" % (block, str(e)))
                rel_uplift = None
            uplift_values.append(rel_uplift)
        
        all_frame_data.append([step_name, time] + uplift_values)
        print("Processed frame %d / %d in step %s (Time = %.4f)" %
              (i + 1, n_total_frames, step_name, time))

# === EXPORT TO CSV (PYTHON 2.7 COMPATIBLE) ===
with open(output_csv, 'wb') as csvfile:
    writer = csv.writer(csvfile)
    writer.writerow(['Step', 'Time'] + sorted_blocks)
    writer.writerows(all_frame_data)

odb.close()
print("Export complete to '%s'" % output_csv)
