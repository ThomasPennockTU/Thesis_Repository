# -*- coding: utf-8 -*-
from odbAccess import openOdb

# --- Settings ---
odb_path = '../1.2-9 Block Flume pull test fd/Job-3.odb'

# --- Open ODB ---
odb = openOdb(path=odb_path)

# --- Loop through steps and print field output keys for the first frame only ---
for step_name, step in odb.steps.items():
    print("\nStep: '{}'".format(step_name))
    if len(step.frames) == 0:
        print("  (No frames in this step)")
        continue

    first_frame = step.frames[0]
    field_keys = first_frame.fieldOutputs.keys()

    print("  Field outputs in first frame:")
    for key in sorted(field_keys):
        print("    - {}".format(key))

odb.close()
