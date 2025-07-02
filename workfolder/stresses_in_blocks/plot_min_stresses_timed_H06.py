# -*- coding: utf-8 -*-
from odbAccess import openOdb
from abaqusConstants import ELEMENT_NODAL
import numpy as np
import csv
import os

# --- Settings ---
odb_path = r'..\..\1.0-First delta flume final\Job-H-0_6.odb'
output_csv = 'min_principal_stress_per_block_H06.csv'
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
block_names.sort()  # Optional: sort for consistent column order

# --- Prepare output table ---
header = ['Time'] + block_names
rows = []

# --- Determine how many frames to process ---
if test:
    n_frames = min(100, len(frames))
else:
    n_frames = len(frames)

print("✅ ODB has {} frames. Processing {} frames...".format(len(frames), n_frames))

# --- Loop over frames ---
for frame_idx in range(n_frames):
    frame = frames[frame_idx]
    time = round(frame.frameValue, 2)
    print("→ Frame {:3d} | Time step {:.4f} s".format(frame_idx + 1, time))
    stress_field = frame.fieldOutputs['S']
    row = [time]

    for block_name in block_names:
        instance = all_instances[block_name]
        stress_subset = stress_field.getSubset(region=instance, position=ELEMENT_NODAL)

        min_princ = 1e20
        for val in stress_subset.values:
            s = val.data
            stress_tensor = np.array([
                [s[0], s[3], s[4]],
                [s[3], s[1], s[5]],
                [s[4], s[5], s[2]]
            ])
            principal_stresses = np.linalg.eigvalsh(stress_tensor)
            min_p = min(principal_stresses)
            if min_p < min_princ:
                min_princ = min_p

        row.append(min_princ if min_princ < 1e10 else '')

    rows.append(row)

odb.close()

# --- Write to CSV ---
with open(output_csv, 'w') as f:
    writer = csv.writer(f)
    writer.writerow(header)
    writer.writerows(rows)

print("\n✅ Done. Min principal stress per block saved to '{}'".format(output_csv))

# --- Send Telegram message ---
try:
    import urllib
    import urllib2

    BOT_TOKEN = "8000286711:AAFiFXs6qjXh2nL11xpwynRSc-lAhkElQr8"
    CHAT_ID = "6217477088"
    TEXT = u"\U0001F916 The stress calculation is *done*!\nFile: `{}`".format(output_csv)

    url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage"
    data = urllib.urlencode({
        "chat_id": CHAT_ID,
        "text": TEXT.encode('utf-8'),
        "parse_mode": "Markdown"
    })
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)

    if response.getcode() == 200:
        print("✅ Telegram message sent.")
    else:
        print("⚠️ Telegram failed with HTTP code {}".format(response.getcode()))

except Exception as e:
    try:
        print(u"Telegram message failed: {}".format(unicode(e))).encode('utf-8')
    except:
        print("Telegram message failed (could not print unicode error message).")
