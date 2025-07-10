# -*- coding: utf-8 -*-
from abaqus import mdb
from abaqusConstants import *

# Job name and input file (without .inp extension)
job_name = "Job-2"

# Submit and wait for job
mdb.JobFromInputFile(name=job_name, inputFileName=job_name + ".inp")
mdb.jobs[job_name].submit()
mdb.jobs[job_name].waitForCompletion()

print(f"✅ Abaqus job '{job_name}' finished.")

# Send Telegram message
import requests

BOT_TOKEN = "8000286711:AAFiFXs6qjXh2nL11xpwynRSc-lAhkElQr8"
CHAT_ID = "6217477088"
TEXT = f"🤖 I'm done simulating *{job_name}*! Check on me in the results folder. 📁"

url = f"https://api.telegram.org/bot{BOT_TOKEN}/sendMessage"
data = {
    "chat_id": CHAT_ID,
    "text": TEXT,
    "parse_mode": "Markdown"  # allows bold/italic/etc.
}

response = requests.post(url, data=data)

if response.status_code == 200:
    print("📲 Telegram message sent to your phone.")
else:
    print("❌ Telegram message failed:", response.text)
