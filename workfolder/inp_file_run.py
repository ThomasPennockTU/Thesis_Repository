# -*- coding: utf-8 -*-
from abaqus import mdb
from abaqusConstants import *

# Job name and input file (without .inp extension)
job_name = 'Job-amptest'

# Submit and wait for job
mdb.JobFromInputFile(name=job_name, inputFileName=job_name + ".inp")
mdb.jobs[job_name].submit()
mdb.jobs[job_name].waitForCompletion()

print("✅ Abaqus job '{}' finished.".format(job_name))

# Send Telegram message using urllib (compatible with Python 2.7)
import urllib
import urllib2

BOT_TOKEN = "8000286711:AAFiFXs6qjXh2nL11xpwynRSc-lAhkElQr8"
CHAT_ID = "6217477088"
TEXT = u"\U0001F916 I'm done simulating *{}*! Check on me in the results folder. \U0001F4C1".format(job_name)

url = "https://api.telegram.org/bot{}/sendMessage".format(BOT_TOKEN)
data = urllib.urlencode({
    "chat_id": CHAT_ID,
    "text": TEXT.encode("utf-8"),
    "parse_mode": "Markdown"
})

try:
    request = urllib2.Request(url, data)
    response = urllib2.urlopen(request)
    print("📲 Telegram message sent to your phone.")
except Exception as e:
    print("❌ Telegram message failed:", str(e))
