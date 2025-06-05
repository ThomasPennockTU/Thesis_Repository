import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
from scipy.linalg import solve
import pandas as pd
from scipy.interpolate import interp1d

# JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME 

job_name = "Job-test2"

# --- Physical and Wave Parameters ---

rho_w = 1025.0       # [kg/m^3] Density of seawater
g = 9.81             # [m/s^2] Gravitational acceleration
Hs = 1.95            # [m] Significant wave height (Hm0)
Tp = 5.59            # [s] Peak wave period
tan_beta = 1.0 / 3.0 # [-] Slope of the revetment (tan(beta) = 1/3 for 1:3 slope)

# --- Filter and Soil Properties ---

D = 0.30             # [m] Thickness of the top (impervious) layer
b = 0.30             # [m] Thickness of the filter layer beneath --reset=0.13
k = 0.19             # [m/s] Permeability of the filter layer
k_prime = 0.05       # [m/s] Permeability of the base layer below the filter

# --- Derived Parameter ---

Lambda = np.sqrt(D * b * k / k_prime)  # [m] Leakage length (controls pressure dissipation)

#----------------------------------------------------------------------------------------------------------------------------

# Step 1: Estimate mean period
Tm_1_0 = Tp / 1.1

# Step 2: Calculate wavelength
L_m_1_0 = (g * Tm_1_0**2) / (2.0 * np.pi)

# Step 3: Calculate Iribarren number
xi_m_1_0 = tan_beta / np.sqrt(Hs / L_m_1_0)

# Step 4: Evaluate the dimensionless pressure formula
denominator = (xi_m_1_0 - 0.2)**2
if denominator == 0:
    raise ValueError("Denominator in pressure equation is zero.")

P_dimless = 8.0 - 1.6 * xi_m_1_0 - 2.0 / denominator

# Step 5: Convert to dimensional pressure
P_max = P_dimless * rho_w * g * Hs  # in Pascals

# Convert to kPa
H_max = P_max / (9.81 * 1025.0)

# Print results
print("Tm-1,0:       %.3f s" % Tm_1_0)
print("L_m-1,0:      %.3f m" % L_m_1_0)
print("xi_m-1,0:     %.3f"   % xi_m_1_0)
print("P* (dimless): %.3f"   % P_dimless)
print("P_max:        %.2f Pa" % P_max)
print("H_max:        %.2f m" % H_max)

#----------------------------------------------------------------------------------------------------------------------------

# Discretization
dx = 0.01
L = 10.0
x = np.arange(0, L + dx, dx)
N = len(x)

# Build phi_T (trapezoidal loading)
wave_impact = np.piecewise(
    x,
    [x < 4, (x >= 4) & (x < 4.5), (x >= 4.5) & (x < 5.5), (x >= 5.5) & (x < 6), x >= 6],
    [
        0,
        lambda x: (x - 4) * (P_max / 0.5),
        P_max,
        lambda x: P_max - (x - 5.5) * (P_max / 0.5),
        0
    ]
)

# Source term vector: b = -phi_T
b_vec = -wave_impact.copy()
b_vec[0] = 0
b_vec[-1] = 0

# Construct coefficient matrix A
A = np.zeros((N, N))
coeff = Lambda**2 / dx**2

for i in range(1, N - 1):
    A[i, i - 1] = coeff
    A[i, i]     = -2 * coeff - 1
    A[i, i + 1] = coeff

# Apply boundary conditions
A[0, 0] = 1.0
A[-1, -1] = 1.0

# Solve
phi_F = solve(A, b_vec)

# residual force
residual_force = phi_F - wave_impact

#print max and min values
print("Max value of the residual force: %.2f Pa" % np.max(residual_force))
print("Min value of the residual force: %.2f Pa" % np.min(residual_force))

# Plot
plt.figure(figsize=(8, 5))
plt.plot(x, wave_impact, label=r'$\phi_T(x)$ (Trapezoid)', color='blue')
plt.plot(x, phi_F, label=r'$\phi_F(x)$ (Solved)', color='red')
plt.plot(x, residual_force, label=r'residual force', color='green')
plt.xlabel('x [m]')
plt.ylabel('Pressure')
plt.legend()
plt.grid(True)
plt.title('Filter Response $\phi_F(x)$ to Trapezoidal Loading $\phi_T(x)$')
plt.tight_layout()
plt.show()

#----------------------------------------------------------------------------------------------------------------------------

# --- 1. Define block geometry ---
x_start, y_start = 1.86, 6.05          # Starting position of first block
block_width = 0.5                      # Block width [m]
block_height = 0.15                    # Block height [m]
n_blocks = 22                          # Number of blocks
slope = 1 / 3                          # Revetment slope (1:3)

angle_rad = np.arctan(slope)          # Slope angle in radians
block_x = [x_start + i * block_width * np.cos(angle_rad) for i in range(n_blocks)]
block_y = [y_start + i * block_width * np.sin(angle_rad) for i in range(n_blocks)]
block_x_centers = [
    block_x[j] + np.cos(angle_rad) * (block_width / 2)
    for j in range(n_blocks)
]
#temporary attempt
block_x_centers = np.linspace(2.0, 12.5, 22)

# --- 2. Compute normalized residual profile from steady-state solution ---
residual_profile = phi_F - wave_impact

# Interpolate residual profile along x
residual_head_from_x = interp1d(x, residual_profile, bounds_error=False, fill_value=0)
block_heads_residual = residual_head_from_x(block_x_centers)

# --- 3. Time pulse definition ---
tt = np.linspace(0, 4, 200)
pulse_shape = np.zeros_like(tt)
pulse_indices = (tt >= 2.0) & (tt <= 2.25)
pulse_t = tt[pulse_indices] - 2.0
pulse_shape[pulse_indices] = np.interp(pulse_t, [0, 0.05, 0.25], [0, 1, 0])  # Normalized triangle

# Time interpolation function
residual_func = interp1d(tt, pulse_shape, kind='linear', fill_value=0, bounds_error=False)


# --- 4. Construct time-resolved force table ---
time_high_res = np.arange(0, 11.991, 0.01)
data = []
for t in time_high_res:
    t_mod = t % 4  # Pulse repeats every 4 seconds
    res_val = residual_func(t_mod)
    forces = np.round(block_heads_residual * res_val, 5)  # Convert to N, round to 5 decimals
    data.append([round(t, 3)] + list(forces))

# --- 5. Build DataFrame and export ---
columns = ["TIME"] + [f"ROW{i+1}" for i in range(n_blocks)]
df = pd.DataFrame(data, columns=columns)

# Export to CSV
df.to_csv("residual_forces_table.csv", index=False)

# Optional preview
df.head()

# --- 6. Print max and min of each column ---
print("MAXIMUM VALUES PER COLUMN:")
print(df.max(numeric_only=True))

print("\nMINIMUM VALUES PER COLUMN:")
print(df.min(numeric_only=True))

#----------------------------------------------------------------------------------------------------------------------------

inp_lines = []

for col in df.columns[1:]:  # Skip "TIME", use "ROW1" to "ROW22"
    inp_lines.append(f"*AMPLITUDE, NAME={col}\n")
    
    for t, val in zip(df["TIME"], df[col]):
        inp_lines.append(f"{t:.3f}, {val:.5f},\n")  # Format: time, force
    
    inp_lines.append("\n")  # Separate blocks

# Preview first few lines
print("".join(inp_lines[:30]))
with open("block_amplitudes.inp", "w") as f:
    f.writelines(inp_lines)

print("✅ File 'block_amplitudes.inp' created with amplitudes per block (ROW1 to ROW22)")

#----------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------

# 1. Read the original .inp file
with open("Job-1.inp", "r") as f:
    lines = f.readlines()

# 2. Replace job name line
for i, line in enumerate(lines):
    if line.strip().lower().startswith("** job name:"):
        lines[i] = f"** Job name: {job_name} Model name: Model-1\n"
        break

# 3. Find indices to insert amplitudes
start_index = None
materials_index = None

for i, line in enumerate(lines):
    if line.strip().lower() == "*end assembly":
        start_index = i
    elif line.strip().lower() == "** materials" and start_index is not None:
        materials_index = i
        break

if start_index is None or materials_index is None:
    raise RuntimeError("❌ Could not find '*End Assembly' and '** Materials' markers.")

# 4. Keep the line before '** Materials'
line_before_materials = lines[materials_index - 1]

# 5. Validate the TIME column
if not (df["TIME"].is_monotonic_increasing and df["TIME"].is_unique):
    raise ValueError("❌ TIME column must be strictly increasing and unique.")

# 6. Generate amplitude lines
amplitude_lines = []

for col in df.columns[1:]:  # Skip TIME
    amplitude_lines.append(f"*AMPLITUDE, NAME={col}\n")
    for i in range(0, len(df), 4):
        chunk = df.iloc[i:i+4]
        row_entries = []
        for t, val in zip(chunk["TIME"], chunk[col]):
            row_entries.append(f"{t:.3f}, {val:.5f}")
        amplitude_lines.append(", ".join(row_entries) + "\n")

# 7. Insert amplitudes into file structure
new_lines = lines[:start_index + 1] + amplitude_lines + [line_before_materials] + lines[materials_index:]

# 8. Export modified file
with open("Job-1-test.inp", "w") as f:
    f.writelines(new_lines)

print(f"✅ Amplitudes inserted and job name updated in '{job_name}.inp'")


#----------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------------------------------------------------------------------------------------

