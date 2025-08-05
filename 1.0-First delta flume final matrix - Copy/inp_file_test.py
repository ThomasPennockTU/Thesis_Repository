# -*- coding: utf-8 -*-
from abaqus import mdb
from abaqusConstants import *

print("🔥 Script has started")


job_name = 'Job-test'
inp_file = job_name + ".inp"

print("📂 Submitting:", inp_file)

# mdb.JobFromInputFile(name=job_name, inputFileName=inp_file)
# mdb.jobs[job_name].submit()
# mdb.jobs[job_name].waitForCompletion()

print("✅ Done simulating:", job_name)