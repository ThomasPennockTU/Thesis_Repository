# -*- coding: utf-8 -*-
# Python 2.7-compatible Abaqus script
from odbAccess import openOdb
import math
import csv
import os
import sys
import traceback

# =========================
# USER CONFIG
# =========================
# Folder where your ODBs live
base_dir = r'D:\tpennock\GitHub\Thesis_Repository\1.0-First delta flume final matrix 2'

job_list = [
    # 'Job-H-0_5_2300_30',
    # 'Job-H-0_6_2300_30',
    'Job-H-0_7_2300_30',
    # 'Job-H-0_8_2300_30',
    # 'Job-H-0_9_2300_30',
    # 'Job-H-1_0_2300_30'
    # 'Job-H-1_1_2300_30'
]

# Write a combined CSV with one row per (job, frame)?
write_combined_csv = True
combined_csv_name = 'all_jobs_uplift_downdrift_ALLSTEPS_ALLFRAMES.csv'

# =========================
# OUTPUT DIRECTORY = SCRIPT DIR
# =========================
try:
    SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
except:
    SCRIPT_DIR = os.getcwd()
output_dir = SCRIPT_DIR

# =========================
# GEOMETRY / SELECTION
# =========================
alpha_rad = math.atan(1.0 / 3.0)
cos_alpha = math.cos(alpha_rad)
sin_alpha = math.sin(alpha_rad)

# Half-blocks (odd rows, columns 1 and 10)
half_block_names = set(['B-%d-1' % i for i in range(1, 22, 2)] +
                       ['B-%d-10' % i for i in range(1, 22, 2)])

# Corner nodes for full blocks
corner_nodes = [1, 8, 169, 176]

# =========================
# HELPERS
# =========================
def resolve_odb_path(entry):
    """Return an absolute .odb path for a job_list entry (supports fuzzy match)."""
    # Absolute file given?
    if os.path.isabs(entry) and os.path.isfile(entry):
        return entry
    # If entry ends with .odb, try in base_dir
    if entry.lower().endswith('.odb'):
        p = os.path.join(base_dir, entry)
        if os.path.isfile(p):
            return p
    # Bare job name -> try exact .odb
    cand = os.path.join(base_dir, entry + '.odb')
    if os.path.isfile(cand):
        return cand
    # Fuzzy match: first .odb in base_dir that contains entry
    try:
        for fname in os.listdir(base_dir):
            if fname.lower().endswith('.odb') and entry.lower() in fname.lower():
                return os.path.join(base_dir, fname)
    except:
        pass
    return None

def per_job_output_csv_name(job_basename):
    return os.path.join(
        output_dir,
        '%s_uplift_downdrift_ALLSTEPS_ALLFRAMES.csv' % job_basename
    )

def build_block_node_map(assembly):
    """Map each block instance to the node labels to read."""
    block_node_map = {}
    for inst_name, inst in assembly.instances.items():
        if inst_name.startswith('B-'):
            if inst_name in half_block_names:
                block_node_map[inst_name] = [52]     # half blocks
            else:
                block_node_map[inst_name] = corner_nodes  # full blocks
    sorted_blocks = sorted(block_node_map.keys())
    return block_node_map, sorted_blocks

def extract_row_for_frame(assembly, disp_field, block_node_map, sorted_blocks,
                          cos_alpha, sin_alpha):
    """For one frame: return (uplift_values, sliding_values) lists."""
    uplift_values = []
    sliding_values = []
    for block in sorted_blocks:
        node_labels = block_node_map[block]
        inst = assembly.instances[block]

        block_uplifts = []
        block_slidings = []

        for node_label in node_labels:
            try:
                node = inst.getNodeFromLabel(node_label)
                sub = disp_field.getSubset(region=node)
                if not sub.values:
                    continue
                disp = sub.values[0]
                u1 = disp.data[0]
                u2 = disp.data[1]

                rel_uplift = u2 * cos_alpha - u1 * sin_alpha
                sliding = u1 * cos_alpha + u2 * sin_alpha

                block_uplifts.append(abs(rel_uplift))
                block_slidings.append(abs(sliding))
            except Exception as e:
                # Keep going
                # print("Warn %s node %d: %s" % (block, node_label, str(e)))
                continue

        if block_uplifts:
            uplift_values.append(max(block_uplifts))
            sliding_values.append(max(block_slidings))
        else:
            uplift_values.append(None)
            sliding_values.append(None)

    return uplift_values, sliding_values

def write_header_if_needed(writer, blocks):
    uplift_headers = ['uplift_' + b for b in blocks]
    sliding_headers = ['sliding_' + b for b in blocks]
    header = ['Job', 'Step', 'FrameIndex', 'Time'] + uplift_headers + sliding_headers
    writer.writerow(header)
    return header

def write_row(writer, job_name, step_name, frame_index, time_val, uplifts, slidings):
    row = [job_name, step_name, frame_index, time_val] + uplifts + slidings
    writer.writerow(row)

# =========================
# MAIN
# =========================
combined_file = None
combined_writer = None
combined_header_written = False
combined_header = None

try:
    if write_combined_csv:
        combined_csv_path = os.path.join(output_dir, combined_csv_name)
        combined_file = open(combined_csv_path, 'wb')
        combined_writer = csv.writer(combined_file)

    for entry in job_list:
        odb_path = resolve_odb_path(entry)
        if not odb_path or not os.path.isfile(odb_path):
            print("ERROR: ODB not found for job name: %s" % entry)
            continue

        job_basename = os.path.splitext(os.path.basename(odb_path))[0]
        per_job_csv = per_job_output_csv_name(job_basename)

        try:
            print("Processing: %s" % odb_path)
            odb = openOdb(path=odb_path)
            assembly = odb.rootAssembly
            block_node_map, sorted_blocks = build_block_node_map(assembly)

            # Prepare per-job CSV
            pf = open(per_job_csv, 'wb')
            pw = csv.writer(pf)
            per_header = write_header_if_needed(pw, sorted_blocks)

            # Steps in order
            step_names = sorted(odb.steps.keys())
            for step_name in step_names:
                step = odb.steps[step_name]
                n_frames = len(step.frames)
                for fi in range(n_frames):
                    frame = step.frames[fi]
                    time_val = frame.frameValue

                    # Some frames may not have 'U'
                    if 'U' not in frame.fieldOutputs.keys():
                        # Write row with blanks
                        uplifts = [None] * len(sorted_blocks)
                        slidings = [None] * len(sorted_blocks)
                        write_row(pw, job_basename, step_name, fi, time_val, uplifts, slidings)
                        if write_combined_csv:
                            if not combined_header_written:
                                combined_header = write_header_if_needed(combined_writer, sorted_blocks)
                                combined_header_written = True
                            write_row(combined_writer, job_basename, step_name, fi, time_val, uplifts, slidings)
                        continue

                    disp_field = frame.fieldOutputs['U']
                    uplifts, slidings = extract_row_for_frame(assembly, disp_field, block_node_map,
                                                              sorted_blocks, cos_alpha, sin_alpha)

                    # Per-job row
                    write_row(pw, job_basename, step_name, fi, time_val, uplifts, slidings)

                    # Combined row
                    if write_combined_csv:
                        if not combined_header_written:
                            combined_header = write_header_if_needed(combined_writer, sorted_blocks)
                            combined_header_written = True
                        write_row(combined_writer, job_basename, step_name, fi, time_val, uplifts, slidings)

            pf.close()
            odb.close()
            print("  Wrote: %s" % per_job_csv)

        except Exception as e:
            print("FAILED: %s" % odb_path)
            traceback.print_exc(file=sys.stdout)
            try:
                if not odb.isClosed():
                    odb.close()
            except:
                pass
            try:
                pf.close()
            except:
                pass
            continue

finally:
    if combined_file is not None:
        combined_file.close()
        if write_combined_csv:
            print("Combined CSV written to: %s" % combined_csv_path)

print("Done.")
