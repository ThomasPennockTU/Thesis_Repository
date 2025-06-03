import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
from scipy.linalg import solve

# Constants
D = 0.30  # m
b = 0.13  # m
k = 0.19  # m/s
k_prime = 0.05  # m/s
Lambda = np.sqrt(D * b * k / k_prime)  # Leakage length, constant

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
        lambda x: (x - 4) * (9.54 / 0.5),
        9.54,
        lambda x: 9.54 - (x - 5.5) * (9.54 / 0.5),
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

# Plot
plt.figure(figsize=(10, 5))
plt.plot(x, wave_impact, label=r'$\phi_T(x)$ (Trapezoid)', color='blue')
plt.plot(x, phi_F, label=r'$\phi_F(x)$ (Solved)', color='red')
plt.xlabel('x [m]')
plt.ylabel('Pressure')
plt.legend()
plt.grid(True)
plt.title('Filter Response $\phi_F(x)$ to Trapezoidal Loading $\phi_T(x)$')
plt.tight_layout()
plt.show()
# The code above solves the problem of a filter response to a trapezoidal loading using finite difference methods.