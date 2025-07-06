from docx import Document
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from matplotlib.patches import Patch
from matplotlib.lines import Line2D
from matplotlib.legend_handler import HandlerTuple

# --------- Set STIX Font ---------
plt.rcParams["font.family"] = "STIX Two Text"
plt.rcParams["mathtext.fontset"] = "stix"

# Load the document
doc = Document("data.docx")

# Get the first table
table = doc.tables[0]

# Extract the table into a list of lists
data = []
for row in table.rows:
    data.append([cell.text.strip() for cell in row.cells])

# Convert to DataFrame
df = pd.DataFrame(data[1:], columns=data[0])

# Clean up column names (strip spaces, replace weird characters)
df.columns = [col.strip().replace("", "Δ") for col in df.columns]

# Check exact column names
print("Columns:", df.columns.tolist())

# Filter rows where Type == "CB" and Toplayer == "Rectangular blocks"
df_cb_rect = df[
    (df["Type"] == "CB") &
    (df["Toplayer"] == "Rectangular blocks")
]

# Convert relevant columns to numeric
df_cb_rect["Hs/ΔD"] = pd.to_numeric(df_cb_rect["Hs/ΔD"], errors="coerce")
df_cb_rect["N"] = pd.to_numeric(df_cb_rect["N"], errors="coerce")

# Drop rows with missing numeric data
df_cb_rect = df_cb_rect.dropna(subset=["Hs/ΔD", "N", "Updated damage"])

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
my_N = 1000
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
    df_circles["N"],
    df_circles["Hs/ΔD"],
    c=df_circles["Updated damage"].map(damage_colors),
    edgecolor='black',
    s=80,
    marker='o'
)

# Crosses
ax.scatter(
    df_crosses["N"],
    df_crosses["Hs/ΔD"],
    c=df_crosses["Updated damage"].map(damage_colors),
    edgecolor='black',
    s=80,
    marker='+',
    linewidth=2
)

# Plot your own data point
ax.scatter(
    my_N,
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
    xy=(my_N, my_Hs_Delta_D),
    xytext=(my_N - 200, my_Hs_Delta_D),
    ha='right',
    va='center',
    fontsize=12,
    color='black',
    arrowprops=dict(
        arrowstyle='-',
        color='gray',
        lw=1.5
    )
)

# Labels and title
ax.set_xlim(0, 2000)
ax.set_xlabel(r"N", fontsize=14)
ax.set_ylabel(r"$H_s/\Delta D$", fontsize=14)
ax.set_title(r"$H_s/\Delta D$ vs N for Type CB with Rectangular blocks", fontsize=16)

# Match grid, spines, and tick lines
grid_color = 'gray'
ax.grid(True, linestyle='-', alpha=0.5, color=grid_color)

# Spines same color as grid
for spine in ax.spines.values():
    spine.set_color(grid_color)

# Set tick lines gray
ax.tick_params(axis='both', color=grid_color)

# Set tick label text color back to black
ax.tick_params(axis='x', labelcolor='black')
ax.tick_params(axis='y', labelcolor='black')

# Ticks formatting
ax.tick_params(axis='x', labelrotation=45, labelsize=12)
ax.tick_params(axis='y', labelsize=12)

plt.tight_layout()

# Save figure
fig.savefig(
    "Hs_Delta_D_vs_N_CB_Rectangular.png",
    dpi=300,
    bbox_inches='tight'
)

# Show figure
plt.show()

# Optional: print filtered dataframe
print(df_cb_rect)
