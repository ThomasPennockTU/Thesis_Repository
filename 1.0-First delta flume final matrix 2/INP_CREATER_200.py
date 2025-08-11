# -*- coding: utf-8 -*-
import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve
import pandas as pd
import os

# -------------------------------------------------
# User parameters
# -------------------------------------------------
Hs = 0.8
density_value = 2300
youngs_modulus_value = 30e9
num_waves = 100  # Number of top waves to process

# Format values into the job name (include wave count)
Hs_str = str(Hs).replace('.', '_')
E_str = int(youngs_modulus_value / 1e9)
job_name = "Job-H-{}_{}_{:02d}-{}W".format(Hs_str, int(density_value), E_str, num_waves)

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
SWL = 4.7
dx = 0.01
x = np.arange(0, 20.0 + dx, dx)
N = len(x)

# --- Block parameters ---
block_length = 0.5
slope = tan_beta
block_dx = block_length * np.cos(np.arctan(slope))
block_start = 6.0
block_positions = [block_start + i * block_dx for i in range(22)]

# -------------------------------------------------
# Generate top N wave heights (Rayleigh)
# -------------------------------------------------
n = 1000
p_values = [(k + 1) / float(n + 1) for k in range(num_waves)]
wave_heights = [Hs * np.sqrt(0.5 * np.log(1.0 / p)) for p in p_values]
wave_heights = sorted([round(h, 3) for h in wave_heights])  # ascending order

# --- Check plot for wave heights ---
plt.figure(figsize=(8, 5))
plt.plot(range(1, num_waves + 1), wave_heights, marker='o', markersize=4, linestyle='-')
plt.xlabel("Wave index (ascending)")
plt.ylabel("Wave height [m]")
plt.title("Top {} Wave Heights from Rayleigh Distribution".format(num_waves))
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------------------------
# Storage dictionaries/lists
# -------------------------------------------------
block_pressures_per_wave = {}
residual_profiles = {}
wave_pressures = {}
filter_responses = {}
# For reporting max residual per wave (rank, H, max_residual)
wave_max_residual_rows = []

# -------------------------------------------------
# Loop over waves
# -------------------------------------------------
for i, H_wave in enumerate(wave_heights):
    Tm_1_0 = Tp / 1.1
    L_m_1_0 = (g * Tm_1_0**2) / (2.0 * np.pi)
    xi = tan_beta / np.sqrt(H_wave / L_m_1_0)
    z_SWL = H_wave * (0.8 + 0.6 * np.tanh(xi - 2.1)) if xi < 3 else np.nan
    x_center = (SWL - z_SWL) / tan_beta

    w_base = (7.0 / 6.0) * H_wave
    w_top = (1.0 / 3.0) * H_wave
    x_left_base = x_center - w_base / 2.0
    x_right_base = x_center + w_base / 2.0
    x_left_top = x_center - w_top / 2.0
    x_right_top = x_center + w_top / 2.0

    denom = (xi - 0.2)**2
    P_dimless = 8.0 - 1.6 * xi - 2.0 / denom
    P_max = P_dimless * rho_w * g * H_wave

    p_vals = np.zeros_like(x)
    for j, xx in enumerate(x):
        if x_left_base <= xx < x_left_top:
            p_vals[j] = P_max * (xx - x_left_base) / (x_left_top - x_left_base)
        elif x_left_top <= xx <= x_right_top:
            p_vals[j] = P_max
        elif x_right_top < xx <= x_right_base:
            p_vals[j] = P_max * (x_right_base - xx) / (x_right_base - x_right_top)

    # Solve filter equation
    b_vec = -p_vals.copy()
    b_vec[0] = 0.0
    b_vec[-1] = 0.0
    A = np.zeros((N, N))
    coeff = Lambda**2 / dx**2
    for j in range(1, N - 1):
        A[j, j - 1] = coeff
        A[j, j] = -2.0 * coeff - 1.0
        A[j, j + 1] = coeff
    A[0, 0] = 1.0
    A[-1, -1] = 1.0
    phi_F = solve(A, b_vec)
    residual = phi_F - p_vals

    wave_name = "Wave {} in {}, H={:.2f}".format(i + 1, n, H_wave)
    wave_pressures[wave_name] = p_vals
    filter_responses[wave_name] = phi_F
    residual_profiles[wave_name] = residual

    # === Record max residual for this wave ===
    max_residual = float(np.max(residual))  # Pa
    wave_max_residual_rows.append([i + 1, float(H_wave), max_residual])

    # Compute average residual pressure per block
    block_avg_pressures = []
    for x_start in block_positions:
        x_end = x_start + block_dx
        mask = (x >= x_start) & (x <= x_end)
        avg_pressure = float(np.mean(residual[mask])) if np.any(mask) else 0.0
        block_avg_pressures.append(avg_pressure)

    block_pressures_per_wave[wave_name] = block_avg_pressures

# -------------------------------------------------
# Pretty print: rank, wave height, max residual per wave
# -------------------------------------------------
df_wave_report = pd.DataFrame(wave_max_residual_rows,
                              columns=["Rank", "WaveHeight_m", "MaxResidual_Pa"])

# Sort by Rank just to be explicit (already in order)
df_wave_report.sort_values("Rank", inplace=True)

print("\n=== Wave Rank / Height / Max Residual (Pa) ===")
# Nicely formatted printout
with pd.option_context('display.max_rows', None,
                       'display.max_columns', None,
                       'display.width', 120,
                       'display.float_format', lambda v: '{:,.3f}'.format(v) if isinstance(v, float) else str(v)):
    print(df_wave_report.to_string(index=False))

# Also save to CSV for record
df_wave_report.to_csv("wave_max_residual_report.csv", index=False)

# -------------------------------------------------
# Plot pressures for first few waves (optional)
# -------------------------------------------------
plt.figure(figsize=(10, 6))
colors = ["black", "tab:blue", "tab:red", "tab:green", "tab:purple"]
linestyles = ["-", "--", ":"]
for idx, wave_name in enumerate(list(wave_pressures.keys())[:5]):  # first 5 for clarity
    color = colors[idx % len(colors)]
    plt.plot(x, wave_pressures[wave_name], linestyle=linestyles[0], color=color, linewidth=1.2, label="{} - Wave Pressure".format(wave_name))
    plt.plot(x, filter_responses[wave_name], linestyle=linestyles[1], color=color, linewidth=1.2, label="{} - Filter Response".format(wave_name))
    plt.plot(x, residual_profiles[wave_name], linestyle=linestyles[2], color=color, linewidth=1.2, label="{} - Residual".format(wave_name))
plt.xlabel("x [m]")
plt.ylabel("Pressure [Pa]")
plt.title("Wave Pressure, Filter Response, and Residuals (First 5 Waves)")
plt.legend(ncol=2, fontsize=8)
plt.grid(True)
plt.tight_layout()
plt.show()

# -------------------------------------------------
# Time signal setup
# -------------------------------------------------
pulse_duration = 0.25
pulse_interval = 2.0
dt = 0.01
time = np.arange(0, pulse_interval * num_waves, dt)

# Triangle pulse
pulse_t = np.array([0.0, 0.05, 0.25])
pulse_val = np.array([0.0, 1.0, 0.0])

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

# DataFrame with amplitudes
columns = ["ROW{}".format(i + 1) for i in range(n_blocks)]
df = pd.DataFrame(data, columns=columns)
df.insert(0, "TIME", time)
print("\nAmplitude table preview:")
print(df.head())

# -------------------------------------------------
# Abaqus .inp file modification
# -------------------------------------------------
script_dir = os.path.dirname(os.path.abspath(__file__))
inp_path = os.path.join(script_dir, "Job-200.inp")
output_path = os.path.join(script_dir, "{}.inp".format(job_name))

with open(inp_path, "r") as f:
    lines = f.readlines()

for i, line in enumerate(lines):
    if line.strip().lower().startswith("** job name:"):
        lines[i] = "** Job name: {} Model name: Model-1\n".format(job_name)
        break

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

line_before_materials = lines[materials_index - 1]

if not (df["TIME"].is_monotonic_increasing and df["TIME"].is_unique):
    raise ValueError("❌ TIME column must be strictly increasing and unique.")

amplitude_lines = []
for col in df.columns[1:]:
    amplitude_lines.append("*AMPLITUDE, NAME={}\n".format(col))
    for i in range(0, len(df), 4):
        chunk = df.iloc[i:i+4]
        row_entries = ["{:.3f}, {:.5f}".format(t, val) for t, val in zip(chunk["TIME"], chunk[col])]
        amplitude_lines.append(", ".join(row_entries) + "\n")

new_lines = lines[:start_index + 1] + amplitude_lines + [line_before_materials] + lines[materials_index:]

for i, line in enumerate(new_lines):
    if line.strip().lower() == "*density":
        new_lines[i + 1] = " {},\n".format(density_value)
    elif line.strip().lower() == "*elastic":
        parts = new_lines[i + 1].strip().split(",")
        if len(parts) >= 2:
            poisson_ratio = parts[1].strip()
        else:
            raise ValueError("❌ Could not parse Poisson's ratio after *Elastic card.")
        new_lines[i + 1] = " {}, {}\n".format(youngs_modulus_value, poisson_ratio)

with open(output_path, "w") as f:
    f.writelines(new_lines)

print("\n✅ Read from: {}".format(inp_path))
print("✅ Written to: {}".format(output_path))
print("✅ Amplitudes inserted and job name updated in '{}'".format(job_name))
print("✅ Density and Young's modulus updated.")
print("✅ Wave max-residual report saved to 'wave_max_residual_report.csv'")
