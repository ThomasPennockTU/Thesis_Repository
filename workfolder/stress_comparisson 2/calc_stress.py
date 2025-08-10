# -*- coding: utf-8 -*-
from odbAccess import openOdb
from abaqusConstants import ELEMENT_NODAL
import numpy as np
import csv
import os

# --- Job list ---
job_list = [
    # 'Job-H-0_5_2300_30',
    'Job-H-0_6_2300_30',
    'Job-H-0_7_2300_30',
    # 'Job-H-0_8_2300_30',
    # 'Job-H-0_9_2300_30',
    # 'Job-H-1_1_2300_30',
]

# --- Folder containing ODBs ---
odb_folder = r'..\..\1.0-First delta flume final matrix 2'

# --- Limit frames for testing (1 = limit, 0 = all) ---
test = 0

for job_name in job_list:
    odb_path = os.path.join(odb_folder, job_name + '.odb')
    output_csv = os.path.join(os.path.dirname(__file__), 'principal_stress_per_block_%s.csv' % job_name)

    if not os.path.exists(odb_path):
        print "ERROR: ODB file not found:", odb_path
        continue

    print "\n=== Processing job:", job_name, "===\n"

    # --- Open ODB ---
    odb = openOdb(odb_path)
    step = odb.steps[odb.steps.keys()[-1]]  # Use the last step
    frames = step.frames
    all_instances = odb.rootAssembly.instances

    # --- Filter block instances (names start with 'B-') ---
    block_names = [name for name in all_instances.keys() if name.startswith('B-')]
    block_names.sort()

    # --- Prepare header ---
    header = ['Time']
    for block_name in block_names:
        header.append('%s_max' % block_name)
        header.append('%s_min' % block_name)

    rows = []

    # --- Determine how many frames to process ---
    if test:
        n_frames = min(100, len(frames))
    else:
        n_frames = len(frames)

    print "ODB has {} frames. Processing {} frames...".format(len(frames), n_frames)

    # --- Loop over frames ---
    for frame_idx in range(n_frames):
        frame = frames[frame_idx]
        time = round(frame.frameValue, 2)
        print "Frame %3d | Time step %.4f s" % (frame_idx + 1, time)
        stress_field = frame.fieldOutputs['S']
        row = [time]

        for block_name in block_names:
            instance = all_instances[block_name]
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

            # Append max and min to the row
            row.append(max_princ if max_princ > -1e10 else '')
            row.append(min_princ if min_princ < 1e10 else '')

        rows.append(row)

    odb.close()

    # --- Write to CSV in script's directory ---
    with open(output_csv, 'wb') as f:
        writer = csv.writer(f)
        writer.writerow(header)
        writer.writerows(rows)

    print "✅ Done. Max and Min principal stresses saved to '%s'" % output_csv

    # --- Send Telegram message ---
    try:
        import urllib
        import urllib2

        BOT_TOKEN = "8000286711:AAFiFXs6qjXh2nL11xpwynRSc-lAhkElQr8"
        CHAT_ID = "6217477088"
        TEXT = u"The stress calculation is done!\nFile: `%s`" % output_csv

        url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage"
        data = urllib.urlencode({
            "chat_id": CHAT_ID,
            "text": TEXT.encode('utf-8'),
            "parse_mode": "Markdown"
        })
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)

        if response.getcode() == 200:
            print "Telegram message sent."
        else:
            print "Telegram failed with HTTP code %s" % str(response.getcode())

    except Exception as e:
        try:
            print u"Telegram message failed: {}".format(unicode(e)).encode('utf-8')
        except:
            print "Telegram message failed (could not print unicode error message)."
