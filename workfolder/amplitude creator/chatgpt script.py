import numpy as np
import matplotlib.pyplot as plt
from scipy.linalg import solve
from scipy.interpolate import interp1d
import pandas as pd

# --- Setup ---
rho_w = 1025.0
g = 9.81
Tp = 5.59
tan_beta = 1.0 / 3.0
D = 0.30
b = 0.30
k = 0.19
k_prime = 0.05
Lambda = np.sqrt(D * b * k / k_prime)

dx = 0.01
L = 10.0
x = np.arange(0, L + dx, dx)
N = len(x)

x_start, y_start = 1.86, 6.05
block_width = 0.5
n_blocks = 22
angle_rad = np.arctan(tan_beta)
block_x_centers = np.linspace(2.0, 12.5, 22)

# --- Rayleigh wave generation for Hs = 1.0 ---
Hs = 1.0
sigma = Hs / np.sqrt(2)
exceed_probs = np.arange(5, 0, -1) / 1000.0
wave_heights = sigma * np.sqrt(-2 * np.log(exceed_probs))

# --- Store results ---
dfs = {}

for i, H_wave in enumerate(wave_heights):
    wave_name = f"Wave-{i+1}_in_1000"

    # Wave physics
    Tm_1_0 = Tp / 1.1
    L_m_1_0 = (g * Tm_1_0**2) / (2.0 * np.pi)
    xi_m_1_0 = tan_beta / np.sqrt(H_wave / L_m_1_0)
    denom = (xi_m_1_0 - 0.2)**2
    P_dimless = 8.0 - 1.6 * xi_m_1_0 - 2.0 / denom
    P_max = P_dimless * rho_w * g * H_wave

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

    b_vec = -wave_impact.copy()
    b_vec[0] = 0
    b_vec[-1] = 0

    A = np.zeros((N, N))
    coeff = Lambda**2 / dx**2
    for j in range(1, N - 1):
        A[j, j - 1] = coeff
        A[j, j]     = -2 * coeff - 1
        A[j, j + 1] = coeff
    A[0, 0] = 1.0
    A[-1, -1] = 1.0

    phi_F = solve(A, b_vec)
    residual_force = phi_F - wave_impact

    residual_head_from_x = interp1d(x, residual_force, bounds_error=False, fill_value=0)
    block_heads_residual = residual_head_from_x(block_x_centers)

    # Pulse
    tt = np.linspace(0, 4, 200)
    pulse_shape = np.zeros_like(tt)
    pulse_indices = (tt >= 2.0) & (tt <= 2.25)
    pulse_t = tt[pulse_indices] - 2.0
    pulse_shape[pulse_indices] = np.interp(pulse_t, [0, 0.05, 0.25], [0, 1, 0])
    residual_func = interp1d(tt, pulse_shape, kind='linear', fill_value=0, bounds_error=False)

    time_high_res = np.arange(0, 11.991, 0.01)
    data = []
    for t in time_high_res:
        t_mod = t % 4
        res_val = residual_func(t_mod)
        forces = np.round(block_heads_residual * res_val, 5)
        data.append([round(t, 3)] + list(forces))

    columns = ["TIME"] + [f"ROW{j+1}" for j in range(n_blocks)]
    df = pd.DataFrame(data, columns=columns)
    dfs[wave_name] = df

# --- Plot residual force at ROW11 for each wave ---
fig, axs = plt.subplots(5, 1, figsize=(10, 15), sharex=True)

for i, (wave_name, df) in enumerate(dfs.items()):
    axs[i].plot(df["TIME"], df["ROW11"], label=wave_name)
    axs[i].set_ylabel("Force [Pa]")
    axs[i].legend()
    axs[i].grid(True)

axs[-1].set_xlabel("Time [s]")
plt.suptitle("Residual Force on Block ROW11 per Wave")
plt.tight_layout(rect=[0, 0.03, 1, 0.97])
plt.show()
