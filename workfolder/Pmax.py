import numpy as np

# Constants
rho_w = 1025.0       # kg/m^3
g = 9.81             # m/s^2
Hs = 1.95            # m (Hm0)
Tp = 5.59            # s (peak period)
tan_beta = 1.0 / 3.0 # slope 1:3

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
P_max_kPa = P_max / 1000.0

# Print results
print("Tm-1,0:       %.3f s" % Tm_1_0)
print("L_m-1,0:      %.3f m" % L_m_1_0)
print("xi_m-1,0:     %.3f"   % xi_m_1_0)
print("P* (dimless): %.3f"   % P_dimless)
print("P_max:        %.2f kPa" % P_max_kPa)
