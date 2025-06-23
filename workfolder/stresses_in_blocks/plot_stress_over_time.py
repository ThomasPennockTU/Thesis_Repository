# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
import pandas as pd

# --- Load CSV ---
csv_path = 'max_principal_stress_per_block.csv'
df = pd.read_csv(csv_path)

# --- Extract time and block columns ---
time = df['Time']
block_columns = df.columns.drop('Time')
print(df.head())
# --- Plot ---
plt.figure(figsize=(12, 6))

for block in block_columns:
    plt.plot(time, df[block], label=block)

plt.title("Max Principal Stress Over Time per Block")
plt.xlabel("Time (s)")
plt.ylabel("Max Principal Stress (Pa)")
plt.grid(True)
# plt.legend(loc='upper right', fontsize='small', ncol=2)
plt.tight_layout()
plt.savefig("stress_over_time_per_block.png")
print("✅ Plot saved: stress_over_time_per_block.png")

