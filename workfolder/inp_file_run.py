from abaqus import mdb
from abaqusConstants import *
import os

# Name of the job (should match your .inp file name without extension)
job_name = "Job-test"

# Submit job
mdb.JobFromInputFile(name=job_name, inputFileName=job_name + ".inp")
mdb.jobs[job_name].submit()
mdb.jobs[job_name].waitForCompletion()

print("✅ Abaqus job completed successfully.")
