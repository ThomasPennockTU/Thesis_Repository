import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import linregress
import os
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib.units import mm
from reportlab.lib import utils

# ------------------------
# Your CSV filename
# ------------------------

file_name = "workfolder/Material strength tests/Thomas-1_20250624-006.csv"


# ------------------------
# Geometry settings
# ------------------------

geometry = {
    "width_mm": 101.60,
    "depth_mm": 100.63,
    "L0_mm": 102.16
}

# ------------------------
# Process CSV and plot
# ------------------------

# Load data
df = pd.read_csv(
    file_name,
    sep=';',
    header=0,
    skiprows=[0,2],
    engine='python'
)
df.columns = df.columns.str.strip()

df['Time'] = pd.to_numeric(df['Time'], errors='coerce')
df['F'] = pd.to_numeric(df['F'], errors='coerce')
df['AVG'] = pd.to_numeric(df['AVG'], errors='coerce')

df = df.dropna(subset=['Time', 'F', 'AVG'])

A = (geometry['width_mm'] * geometry['depth_mm']) / 1e6
L0 = geometry['L0_mm'] / 1000

# Reference undeformed state
i_ref = df['L1'].idxmin()
df['S_rel'] = (df['S'] - df.loc[i_ref, 'S']) / 1000
df['F_N'] = df['F'] * 1000
df['strain'] = df['S_rel'] / L0
df['stress'] = df['F_N'] / A

linear_range = df[(df['strain'] >= 0.003) & (df['strain'] <= 0.008)].copy()

if len(linear_range) >= 2:
    slope, intercept, r_value, p_value, std_err = linregress(
        linear_range['strain'],
        linear_range['stress']
    )
    E = slope
    R2 = r_value ** 2
else:
    E = None
    R2 = None

if not df['stress'].empty:
    stress_max = df['stress'].max()
    strain_max = df.loc[df['stress'].idxmax(), 'strain']
else:
    stress_max = None
    strain_max = None

# ------------------------
# Plotting
# ------------------------

fig, axs = plt.subplots(5, 1, figsize=(8.27, 11.69))  # A4 portrait

# Plot 1
axs[0].plot(df['Time'], df['stress'], color='lightgray', label='Stress (full)')
if not linear_range.empty:
    axs[0].plot(linear_range['Time'], linear_range['stress'], color='darkred', label='Fitted Region')
axs[0].set_title("Stress over Time")
axs[0].set_xlabel("Time [s]")
axs[0].set_ylabel("Stress [Pa]")
axs[0].legend()
axs[0].grid()

# Plot 2
axs[1].plot(df['Time'], df['strain'], color='lightgray', label='Strain (full)')
if not linear_range.empty:
    axs[1].plot(linear_range['Time'], linear_range['strain'], color='green', label='Fitted Region')
axs[1].set_title("Strain over Time")
axs[1].set_xlabel("Time [s]")
axs[1].set_ylabel("Strain [-]")
axs[1].legend()
axs[1].grid()

# Plot 3
axs[2].plot(df['strain'], df['stress'], color='lightgray', label='Full Curve')
if E is not None:
    strain_fit = np.linspace(0, strain_max, 200)
    stress_fit = intercept + slope * strain_fit
    axs[2].plot(strain_fit, stress_fit, color='black', linestyle='--',
                label=f'Linear Fit (E ≈ {E/1e9:.2f} GPa)')
if not linear_range.empty:
    axs[2].scatter(linear_range['strain'], linear_range['stress'],
                   color='red', s=10, label='Fitted Region')
if stress_max is not None:
    axs[2].scatter(strain_max, stress_max, color='blue', s=40, zorder=5, label='Max Stress')
    axs[2].annotate(f"{stress_max/1e6:.2f} MPa",
                    xy=(strain_max, stress_max),
                    xytext=(strain_max + 0.002, stress_max),
                    arrowprops=dict(arrowstyle='->'))
axs[2].set_title("Stress–Strain Curve")
axs[2].set_xlabel("Strain [-]")
axs[2].set_ylabel("Stress [Pa]")
axs[2].legend()
axs[2].grid()

# Plot 4
axs[3].plot(df['Time'], df['D1'], label='D1', color='blue')
axs[3].plot(df['Time'], df['D3'], label='D3', color='orange')
axs[3].plot(df['Time'], df['D2'], label='D2', color='green')
axs[3].plot(df['Time'], df['D4'], label='D4', color='red')
axs[3].set_title('Time vs Displacement D1..D4')
axs[3].set_ylabel('Displacement [mm]')
axs[3].legend()
axs[3].grid()

# Plot 5
axs[4].plot(df['Time'], df['L1'], label='L1', color='blue')
axs[4].plot(df['Time'], df['L2'], label='L2', color='orange')
axs[4].plot(df['Time'], df['L3'], label='L3', color='green')
axs[4].plot(df['Time'], df['L4'], label='L4', color='red')
axs[4].plot(df['Time'], df['S'], label='S', color='grey')
axs[4].set_title('Time vs L1..L4 and S')
axs[4].set_ylabel('Displacement [mm]')
axs[4].legend()
axs[4].grid()

plt.tight_layout()

plot_filename = "test_plot.png"
plt.savefig(plot_filename, dpi=300)
plt.close(fig)

# ------------------------
# Create PDF report
# ------------------------

pdf_filename = "test_report.pdf"
c = canvas.Canvas(pdf_filename, pagesize=A4)
page_width, page_height = A4

# Title
c.setFont("Helvetica-Bold", 16)
c.drawString(30, page_height - 40, f"Mechanical Test Report")

# File name
c.setFont("Helvetica", 12)
c.drawString(30, page_height - 70, f"File: {file_name}")

# Summary text
y = page_height - 100
if E is not None:
    c.drawString(30, y, f"Estimated Young's Modulus (E): {E/1e9:.2f} GPa")
else:
    c.drawString(30, y, f"E: N/A")
y -= 20

if R2 is not None:
    c.drawString(30, y, f"R² of linear fit: {R2:.4f}")
else:
    c.drawString(30, y, f"R²: N/A")
y -= 20

if stress_max is not None:
    c.drawString(30, y, f"Maximum Stress: {stress_max/1e6:.2f} MPa")
else:
    c.drawString(30, y, f"Max Stress: N/A")

# Insert image
if os.path.exists(plot_filename):
    img = utils.ImageReader(plot_filename)
    iw, ih = img.getSize()
    scale = min((page_width - 60) / iw, (page_height - 200) / ih)
    iw_scaled = iw * scale
    ih_scaled = ih * scale
    c.drawImage(plot_filename, 30, y - ih_scaled - 30, width=iw_scaled, height=ih_scaled)

# Save PDF
c.showPage()
c.save()

print("PDF report generated successfully:", pdf_filename)
