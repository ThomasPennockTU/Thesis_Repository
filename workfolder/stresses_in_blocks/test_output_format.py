# -*- coding: utf-8 -*-
from odbAccess import openOdb
import os

# --- Settings ---
odb_path = r'..\..\1.0-First delta flume\Job-amptest-1200.odb'

# --- Open ODB ---
if not os.path.exists(odb_path):
    raise IOError("ODB file not found: {}".format(odb_path))

odb = openOdb(odb_path)
step = odb.steps[odb.steps.keys()[-1]]  # Use last step
frame = step.frames[0]  # First frame

# --- Get stress field output ---
if 'S' not in frame.fieldOutputs:
    raise KeyError("Stress tensor (S) not found in field outputs.")

stress_field = frame.fieldOutputs['S']
component_labels = stress_field.componentLabels
position = stress_field.locations[0].position

print("✅ Stress field 'S' found.")
print(" - Output position: {}".format(position))
print(" - Number of values: {}".format(len(stress_field.values)))
print(" - Components:", component_labels)

# --- Preview first 5 stress tensors ---
print("\n🧪 First 5 stress tensors:")
for i, val in enumerate(stress_field.values[:5]):
    print("  Value {} at element {} node {}:".format(i+1, val.elementLabel, val.nodeLabel if hasattr(val, 'nodeLabel') else '-'))
    print("   Data:", val.data)

odb.close()
