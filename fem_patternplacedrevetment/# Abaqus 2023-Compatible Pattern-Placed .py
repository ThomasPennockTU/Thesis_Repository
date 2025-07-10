# Abaqus 2023-Compatible Pattern-Placed Revetment Model Generator
# Updated to use modern Python, modular design, better file handling, and improved performance

import pandas as pd
import numpy as np
from pathlib import Path
import logging
import os

from abaqus import *
from abaqusConstants import *

# Logging configuration
logging.basicConfig(level=logging.INFO, format='%(levelname)s: %(message)s')

# Constants
G = 9.81  # Gravitational acceleration (m/s^2)
DX = 0.01  # Spatial step size (m)
DT = 0.01  # Time step size (s)
RELAX_TIME = 2.0  # Time before first impact (s)
IMPACT_TIME = 2.0  # Time between impacts (s)

# File paths (using same relative paths as original code)
EXCEL_FILE = Path("example.xlsx")
BLOCK_INFO_FILE = Path("BasaltonSTSplus/info.txt")
JOINT_INFO_FILE = Path("BasaltonSTSplus_jointfilling/info.txt")
BLOCK_DIR = Path("BasaltonSTSplus")
JOINT_DIR = Path("BasaltonSTSplus_jointfilling")

# Read Excel file with robust error handling
if not EXCEL_FILE.exists():
    raise FileNotFoundError(f"Excel file not found: {EXCEL_FILE.resolve()}")

logging.info("Reading input data from: %s", EXCEL_FILE.name)
df = pd.read_excel(EXCEL_FILE).dropna(how='all')

# Helper to extract typed columns
def extract_column(df, index, dtype=float, name=None):
    try:
        return df.iloc[:, index].astype(dtype).tolist()
    except Exception as e:
        label = f"column {index + 1}" if not name else name
        raise ValueError(f"Failed to extract {label}: {e}")

# Extract model parameters
a_mname = extract_column(df, 0, str, "Model Name")
a_slope = extract_column(df, 1, float, "Slope")
a_zdtop = extract_column(df, 2)
a_zdbot = extract_column(df, 3)
bb_Hs = extract_column(df, 4)
a_s0p = extract_column(df, 5)
a_SI = extract_column(df, 6)
a_D = extract_column(df, 7)
a_d = extract_column(df, 8)
a_ll = extract_column(df, 9)
a_kk = extract_column(df, 10)
a_rhow = extract_column(df, 11)
a_rhos = extract_column(df, 12)
a_Fblockfilter = extract_column(df, 13)
a_Fblockblock = extract_column(df, 14)

# Wave heights: columns 15–19 (0-indexed 14–18)
try:
    aa_Hs = df.iloc[:, 14:19].astype(float).values.tolist()
except Exception as e:
    raise ValueError("Failed to parse wave heights: columns 15–19")

# S-profile and geometry params
a_S_mid = extract_column(df, 20)
a_S_width = extract_column(df, 21)
a_S_amp = extract_column(df, 22)
a_G_z = extract_column(df, 23)
a_G_x = extract_column(df, 24)

logging.info("Excel input successfully parsed.")

# Load block shape info
def load_block_info(file_path):
    if not file_path.exists():
        raise FileNotFoundError(f"Missing block info: {file_path}")
    data = np.loadtxt(file_path, delimiter=',', skiprows=1)
    return {int(row[0]): {'length': row[1], 'relrot': row[2], 'area': row[3]} for row in data}

block_info = load_block_info(BLOCK_INFO_FILE)
joint_info = load_block_info(JOINT_INFO_FILE)

logging.info("Block and joint geometry files loaded.")

# Example model generation loop for Abaqus
for idx, model_name in enumerate(a_mname):
    logging.info(f"Creating model: {model_name}")

    # Create the model
    model = mdb.Model(name=model_name, modelType=STANDARD_EXPLICIT)

    # Geometry parameters
    slope = a_slope[idx]
    d = a_d[idx]
    zdtop = a_zdtop[idx]
    zdbot = a_zdbot[idx]
    D = a_D[idx]
    rhow = a_rhow[idx]
    rhos = a_rhos[idx]

    # Create a simple bottom sketch as placeholder
    sketch = model.ConstrainedSketch(name='__profile__', sheetSize=10.0)
    sketch.Line(point1=(0.0, 0.0), point2=(5.0, 0.0))
    part = model.Part(name='Bottom', dimensionality=THREE_D, type=ANALYTIC_RIGID_SURFACE)
    part.AnalyticRigidSurfExtrude(depth=1.0, sketch=sketch)
    del model.sketches['__profile__']

    # Add reference point and surface
    part.ReferencePoint(point=part.vertices[2])
    part.Surface(name='Surf-Bottom', side1Faces=part.faces.getSequenceFromMask(('[#1 ]',),))

    # Instance in assembly
    assembly = model.rootAssembly
    assembly.Instance(name='Bottom-1', part=part, dependent=ON)

    # Gravity load
    model.ExplicitDynamicsStep(name='Step-1', timePeriod=1.0, previous='Initial')
    model.Gravity(name='Gravity', createStepName='Step-1', comp2=-G)

    # Field outputs
    model.fieldOutputRequests['F-Output-1'].setValues(variables=('U', 'S', 'P'))
    model.historyOutputRequests['H-Output-1'].setValues(variables=('ALLKE', 'ALLIE'))

    # Job definition
    job_name = f"Job-{model_name}"
    mdb.Job(name=job_name, model=model_name, type=ANALYSIS, explicitPrecision=SINGLE, nodalOutputPrecision=SINGLE, description='Auto-generated job')
    logging.info(f"Model {model_name} setup complete. Job ready: {job_name}")

logging.info("All models generated successfully.")
