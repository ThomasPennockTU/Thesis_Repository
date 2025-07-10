# -*- coding: utf-8 -*-
from abaqus import mdb
from abaqusConstants import *
import os
import urllib
import urllib2

# Safe print for Python 2.7
print "Script started."

# Job name (must match the .inp file name without the extension)
job_name = 'Job-H-0_6'
inp_file = job_name + '.inp'

# Check input file exists
if not os.path.exists(inp_file):
    raise Exception("Input file '" + inp_file + "' not found!")

# Submit Abaqus job
mdb.JobFromInputFile(
    name=job_name,
    inputFileName=inp_file,
    numCpus=8,
    numDomains=8
)
mdb.jobs[job_name].submit()
mdb.jobs[job_name].waitForCompletion()

print "Abaqus job '" + job_name + "' finished."

# Send Telegram message using urllib2 (Python 2.7)
try:
    BOT_TOKEN = "8000286711:AAFiFXs6qjXh2nL11xpwynRSc-lAhkElQr8"
    CHAT_ID = "6217477088"
    TEXT = u"\U0001F916 I'm done simulating *" + job_name + "*! Check on me in the results folder. \U0001F4C1"

    url = "https://api.telegram.org/bot" + BOT_TOKEN + "/sendMessage"
    data = urllib.urlencode({
        "chat_id": CHAT_ID,
        "text": TEXT.encode('utf-8'),  # Encode message for the HTTP request
        "parse_mode": "Markdown"
    })
    req = urllib2.Request(url, data)
    response = urllib2.urlopen(req)

    if response.getcode() == 200:
        print "Telegram message sent."
    else:
        print "Telegram failed with HTTP code", response.getcode()

except Exception as e:
    # Safe error print, avoid emojis in logs
    try:
        # attempt unicode-friendly print
        print (u"Telegram message failed: {}".format(unicode(e))).encode('utf-8')
    except:
        # fallback: ASCII-safe print
        print "Telegram message failed (could not print unicode error message)."
