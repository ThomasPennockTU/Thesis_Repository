import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
from scipy.linalg import solve
import pandas as pd
from scipy.interpolate import interp1d
import os

# JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME  JOBNAME 

job_name = 'Job-H-0_5-2300-30'
Hs = 0.5
density_value = 2300.0                # your new density
youngs_modulus_value = 7.5e9          # your new Young's modulus

# --- Constants ---
rho_w = 1025.0
g = 9.81
Tp = 5.59
tan_beta = 1.0 / 3.0
D = 0.15
b = 0.1
k = 0.3
k_prime = 0.015
Lambda = np.sqrt(D * b * k / k_prime)
print(Lambda)
SWL = 4.7
dx = 0.01
x = np.arange(0, 20.0 + dx, dx)
N = len(x)
H_wave_width = Hs

# --- Block parameters ---
block_length = 0.5
slope = tan_beta
block_dx = block_length * np.cos(np.arctan(slope))
block_start = 6.0
block_positions = [block_start + i * block_dx for i in range(22)]

# --- Generate wave heights (Rayleigh) ---

sigma = Hs / np.sqrt(2)
exceed_probs = np.arange(1, 6, 1) / 1000.0
wave_heights = sigma * np.sqrt(-2 * np.log(exceed_probs))

# --- Initialize storage ---
block_pressures_per_wave = {}
residual_profiles = {}  
wave_pressures = {}
filter_responses = {}

# Loop through each wave

for i, H_wave in enumerate(wave_heights):
    Tm_1_0 = Tp / 1.1
    L_m_1_0 = (g * Tm_1_0**2) / (2.0 * np.pi)
    xi = tan_beta / np.sqrt(H_wave / L_m_1_0)
    z_SWL = H_wave * (0.8 + 0.6 * np.tanh(xi - 2.1)) if xi < 3 else np.nan
    x_center = (SWL - z_SWL) / tan_beta

    w_base = (7 / 6) * H_wave
    w_top = (1 / 3) * H_wave
    x_left_base = x_center - w_base / 2
    x_right_base = x_center + w_base / 2
    x_left_top = x_center - w_top / 2
    x_right_top = x_center + w_top / 2

    # Calculate P_max
    denom = (xi - 0.2)**2
    P_dimless = 8.0 - 1.6 * xi - 2.0 / denom
    P_max = P_dimless * rho_w * g * H_wave

    # Build trapezoidal wave pressure
    p_vals = np.zeros_like(x)
    for j, xx in enumerate(x):
        if x_left_base <= xx < x_left_top:
            p_vals[j] = P_max * (xx - x_left_base) / (x_left_top - x_left_base)
        elif x_left_top <= xx <= x_right_top:
            p_vals[j] = P_max
        elif x_right_top < xx <= x_right_base:
            p_vals[j] = P_max * (x_right_base - xx) / (x_right_base - x_right_top)

    # Solve for filter response
    b_vec = -p_vals.copy()
    b_vec[0] = b_vec[-1] = 0
    A = np.zeros((N, N))
    coeff = Lambda**2 / dx**2
    for j in range(1, N - 1):
        A[j, j - 1] = coeff
        A[j, j] = -2 * coeff - 1
        A[j, j + 1] = coeff
    A[0, 0] = A[-1, -1] = 1.0
    phi_F = solve(A, b_vec)
    residual = phi_F - p_vals

    wave_name = f"Wave {i+1} in 1000, H={H_wave:.2f}"
    wave_pressures[wave_name] = p_vals
    filter_responses[wave_name] = phi_F
    residual_profiles[wave_name] = residual

    # Compute block pressures
    block_avg_pressures = []
    for x_start in block_positions:
        x_end = x_start + block_dx
        mask = (x >= x_start) & (x <= x_end)
        avg_pressure = np.mean(residual[mask])
        block_avg_pressures.append(avg_pressure)

    block_pressures_per_wave[f"Wave {i+1} in 1000, H={H_wave:.2f}"] = block_avg_pressures

# Plot histogram of block pressures for each wave
plt.figure(figsize=(10, 6))

colors = ["black", "tab:blue", "tab:red", "tab:green", "tab:purple"]
linestyles = ["-", "--", ":"]

for idx, wave_name in enumerate(wave_pressures.keys()):
    color = colors[idx % len(colors)]
    plt.plot(x, wave_pressures[wave_name],
             linestyle=linestyles[0],
             color=color,
             linewidth=1.2,
             label=f"{wave_name} - Wave Pressure")

    plt.plot(x, filter_responses[wave_name],
             linestyle=linestyles[1],
             color=color,
             linewidth=1.2,
             label=f"{wave_name} - Filter Response")

    plt.plot(x, residual_profiles[wave_name],
             linestyle=linestyles[2],
             color=color,
             linewidth=1.2,
             label=f"{wave_name} - Residual")

plt.xlabel("x [m]")
plt.ylabel("Pressure [Pa]")
plt.title("Wave Pressure, Filter Response, and Residuals")
plt.legend(ncol=2, fontsize=8)
plt.grid(True)
plt.tight_layout()
plt.show()

# Plot histogram of block pressures for each wave
fig, axs = plt.subplots(5, 1, figsize=(10, 14), sharex=True)

for i, (wave_name, pressures) in enumerate(block_pressures_per_wave.items()):
    axs[i].bar(np.arange(1, 23), pressures, color='skyblue', width=1, edgecolor='black')
    axs[i].set_ylabel("Avg Pressure [Pa]")
    axs[i].set_title(f"{wave_name}")
    axs[i].grid(True)

axs[-1].set_xlabel("Block Row Number")
plt.tight_layout()
plt.show()

print(block_pressures_per_wave)

# -----------------------------------------------------------------------------------------------------------------


# --- Time signal setup ---
total_waves = 5
pulse_duration = 0.25
pulse_interval = 2.0
dt = 0.01
time = np.arange(0, pulse_interval * total_waves, dt)

# Pulse shape (triangle from 0 to 0.25s)
pulse_t = np.array([0.0, 0.05, 0.25])
pulse_val = np.array([0.0, 1.0, 0.0])

# --- Construct time-dependent pressure table ---
n_blocks = 22
data = np.zeros((len(time), n_blocks))

for wave_index, (wave_name, pressures) in enumerate(block_pressures_per_wave.items()):
    t_start = wave_index * pulse_interval
    t_end = t_start + pulse_duration
    active_indices = (time >= t_start) & (time <= t_end)
    local_time = time[active_indices] - t_start
    pulse = np.interp(local_time, pulse_t, pulse_val)

    for i in range(n_blocks):
        data[active_indices, i] += pressures[i] * pulse

# --- Create DataFrame ---
columns = [f"ROW{i+1}" for i in range(n_blocks)]
df = pd.DataFrame(data, columns=columns)
df.insert(0, "TIME", time)
print(df)

#----------------------------------------------------------------------------------------------------------------------------


# -----------------------------------------
# Script logic
# -----------------------------------------

script_dir = os.path.dirname(os.path.abspath(__file__))

# Construct full path to the input file relative to the script location
inp_path = os.path.join(script_dir, f"Job-1.inp")

# Output will go to the working directory (current directory)
output_path = os.path.join(script_dir, f"{job_name}.inp")

# 1. Read the original .inp file
with open(inp_path, "r") as f:
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
        start_index = i + 2
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

# 7b. Replace density and Young's modulus
for i, line in enumerate(new_lines):
    if line.strip().lower() == "*density":
        # Replace the next line with the new density
        new_lines[i + 1] = f" {density_value},\n"
    elif line.strip().lower() == "*elastic":
        # Parse Poisson's ratio from existing line
        parts = new_lines[i + 1].strip().split(",")
        if len(parts) >= 2:
            poisson_ratio = parts[1].strip()
        else:
            raise ValueError("❌ Could not parse Poisson's ratio after *Elastic card.")

        new_lines[i + 1] = f" {youngs_modulus_value}, {poisson_ratio}\n"

# 8. Export modified file
with open(output_path, "w") as f:
    f.writelines(new_lines)

print(f"✅ Read from: {inp_path}")
print(f"✅ Written to: {output_path}")
print(f"✅ Amplitudes inserted and job name updated in '{job_name}.inp'")
print(f"✅ Density and Young's modulus updated.")

