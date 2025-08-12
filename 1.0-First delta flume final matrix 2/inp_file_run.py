# -*- coding: utf-8 -*-
from abaqus import mdb
from abaqusConstants import *
import os
import urllib
import urllib2

def run_job(job_name):
    print "Starting job:", job_name
    inp_file = job_name + '.inp'

    if not os.path.exists(inp_file):
        raise Exception("Input file '" + inp_file + "' not found!")

    mdb.JobFromInputFile(
        name=job_name,
        inputFileName=inp_file,
        numCpus=8,
        numDomains=8
    )
    mdb.jobs[job_name].submit()
    mdb.jobs[job_name].waitForCompletion()

    print "Abaqus job '" + job_name + "' finished."
    send_telegram_message(job_name)

def send_telegram_message(job_name):
    try:
        BOT_TOKEN = "8000286711:AAFiFXs6qjXh2nL11xpwynRSc-lAhkElQr8"
        CHAT_ID = "6217477088"
        TEXT = u"\U0001F916 I'm done simulating *" + job_name + "*! Check on me in the results folder. \U0001F4C1"

        url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage"
        data = urllib.urlencode({
            "chat_id": CHAT_ID,
            "text": TEXT.encode('utf-8'),
            "parse_mode": "Markdown"
        })
        req = urllib2.Request(url, data)
        response = urllib2.urlopen(req)

        if response.getcode() == 200:
            print "Telegram message sent for", job_name
        else:
            print "Telegram failed with HTTP code", response.getcode()

    except Exception as e:
        try:
            print (u"Telegram message failed: {}".format(unicode(e))).encode('utf-8')
        except:
            print "Telegram message failed (could not print unicode error message)."

# -------------------
# Run both jobs
# -------------------

print "=== Script started ==="

job_list = [
    # 'Job-H-0_5_2300_30',
    # 'Job-H-0_6_2300_30',
    # 'Job-H-0_7_2300_30',
    # 'Job-H-0_8_2300_30',
    # 'Job-H-0_9_2300_30',
    # 'Job-H-1_0_2300_30',
    # 'Job-H-1_1_2300_30',
    # 'Job-H-0_6_1950_30',
    # 'Job-H-0_6_1950_02',
    # 'Job-H-0_7_1950_30',
    # 'Job-H-0_7_1950_02',
    # 'Job-H-0_7_2300_07',
    # 'Job-H-0_7_2300_03',
    # 'Job-H-0_7_2300_02',
    # 'Job-H-0_7_2100_30',
    # 'Job-H-0_7_2100_07',
    # 'Job-H-0_7_2000_30',
    # 'Job-H-0_7_2000_03',
    # 'Job-H-0_8_2300_30-100W',
    'Job-H-0_8_2300_30_DESC',    

]

total_jobs = len(job_list)

for i, job_name in enumerate(job_list):
    print "\n--- Running job {}/{}: {} ---".format(i + 1, total_jobs, job_name)
    run_job(job_name)
    print "--- Completed job {}/{}: {} ---".format(i + 1, total_jobs, job_name)

print "\n=== All {} jobs finished ===".format(total_jobs)
