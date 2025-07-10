# -*- coding: utf-8 -*-
from docx import Document
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
import os
from matplotlib.lines import Line2D

# --------- Set STIX Font ---------
plt.rcParams["font.family"] = "STIX Two Text"
plt.rcParams["mathtext.fontset"] = "stix"

# Load the document
doc = Document("workfolder/doc_tables/data.docx")

# Get the first table
table = doc.tables[0]

# Extract the table into a list of lists
data = []
for row in table.rows:
    data.append([cell.text.strip() for cell in row.cells])

# Convert to DataFrame
df = pd.DataFrame(data[1:], columns=data[0])

# Clean up column names (strip spaces, replace symbols)
df.columns = [
    col.strip()
        .replace("", "Δ")
        .replace("", "ξ")
    for col in df.columns
]

# Check exact column names
print("Columns:", df.columns.tolist())

# Convert relevant columns to numeric
df["Hs/ΔD"] = pd.to_numeric(df["Hs/ΔD"], errors="coerce")

# Check if ξ column exists
xi_col_candidates = [col for col in df.columns if "ξ" in col]
if not xi_col_candidates:
    raise ValueError("Could not find a ξ column in the table. Check your table header names!")
xi_col_name = xi_col_candidates[0]
print(f"Using column: {xi_col_name}")

df[xi_col_name] = pd.to_numeric(df[xi_col_name], errors="coerce")

# Filter rows where Type == "CB" and Toplayer == "Rectangular blocks"
df_cb_rect = df[
    (df["Type"] == "CB") &
    (df["Toplayer"] == "Rectangular blocks")
].dropna(subset=["Hs/ΔD", xi_col_name, "Updated damage"])

# Define color mapping
damage_colors = {
    "0": "white",
    "a": "green",
    "b": "yellow",
    "c": "orange",
    "d": "red",
    "c1": "orange",
    "d1": "red",
}

# Split into circles and crosses
df_circles = df_cb_rect[~df_cb_rect["Updated damage"].isin(["c1", "d1"])]
df_crosses = df_cb_rect[df_cb_rect["Updated damage"].isin(["c1", "d1"])]

# --- Add your own data point ---
my_xi = 1.515       # <<-- Replace with your own ξₘ-10 value
my_damage = "d"

# Define densities
rho_s = 2300     # block density (kg/m³)
rho_w = 1000     # water density (kg/m³)

# Calculate Δ
Delta = (rho_s - rho_w) / rho_w

# Calculate Hs/(Δ·D)
Hs = 0.7
D = 0.15
my_Hs_Delta_D = Hs / (Delta * D)

# Plot
fig, ax = plt.subplots(figsize=(10, 6))

# Circles
ax.scatter(
    df_circles[xi_col_name],
    df_circles["Hs/ΔD"],
    c=df_circles["Updated damage"].map(damage_colors),
    edgecolor='black',
    s=80,
    marker='o'
)

# Crosses
ax.scatter(
    df_crosses[xi_col_name],
    df_crosses["Hs/ΔD"],
    c=df_crosses["Updated damage"].map(damage_colors),
    edgecolor='black',
    s=80,
    marker='+',
    linewidth=2
)

# Plot your own data point
ax.scatter(
    my_xi,
    my_Hs_Delta_D,
    color=damage_colors[my_damage],
    edgecolor='black',
    s=80,
    marker='s',
    linewidth=1.5
)

# Add label with arrow
ax.annotate(
    "Abaqus Simulation\nH07 C30/37",
    xy=(my_xi, my_Hs_Delta_D),
    xytext=(my_xi - 0.35, my_Hs_Delta_D + 1),
    ha='right',
    va='center',
    fontsize=14,        # increased from 12
    color='black',
    arrowprops=dict(
        arrowstyle='-',
        color='gray',
        lw=1.5
    )
)

# Labels and title
ax.set_xlim(0, df_cb_rect[xi_col_name].max() * 1.1)
ax.set_xlabel(r"$\xi_{m-10}$", fontsize=16)
ax.set_ylabel(r"$H_s/\Delta D$", fontsize=16)
# ax.set_title(r"$H_s/\Delta D$ vs $\xi_{m-10}$ for Type CB with Rectangular blocks", fontsize=18)

# Grid and styling
grid_color = 'gray'
ax.grid(True, linestyle='-', alpha=0.5, color=grid_color)

for spine in ax.spines.values():
    spine.set_color(grid_color)

ax.tick_params(axis='both', color=grid_color)
ax.tick_params(axis='x', labelcolor='black', rotation=45, labelsize=14)
ax.tick_params(axis='y', labelcolor='black', labelsize=14)

# Legend
legend_elements = [
    Patch(facecolor="white", edgecolor='black', label='Damage 0'),
    Patch(facecolor="green", edgecolor='black', label='Damage a'),
    Patch(facecolor="yellow", edgecolor='black', label='Damage b'),
    Patch(facecolor="orange", edgecolor='black', label='Damage c / c1'),
    Patch(facecolor="red", edgecolor='black', label='Damage d / d1'),
    Line2D([0], [0], color='red', marker='s', markersize=10,
           linestyle='None', markeredgecolor='black', label='Abaqus Simulation'),
]
ax.legend(handles=legend_elements, fontsize=14, loc='best')

plt.tight_layout()

output_dir = "workfolder/doc_tables"
os.makedirs(output_dir, exist_ok=True)

output_path = os.path.join(output_dir, "Hs_Delta_D_vs_xim10_CB_Rectangular.png")

fig.savefig(
    output_path,
    dpi=300,
    bbox_inches='tight'
)

print("Plot saved to:", output_path)

# Show figure
plt.show()

# Optional: print filtered dataframe
print(df_cb_rect)
