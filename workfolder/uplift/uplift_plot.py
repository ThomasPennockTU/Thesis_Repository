import csv
import matplotlib.pyplot as plt

# === CONFIGURATION ===
csv_file = 'relative_uplift_timeseries.csv'

# === LOAD DATA ===
times = []
block_names = []
uplift_data = {}

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)
    block_names = header[1:]  # Skip 'Time' column

    for block in block_names:
        uplift_data[block] = []

    for row in reader:
        times.append(float(row[0]))
        for i, block in enumerate(block_names):
            val = row[i + 1]
            uplift_data[block].append(float(val) if val else None)

# === PLOT DATA ===
plt.figure(figsize=(12, 8))

for block in block_names:
    plt.plot(times, uplift_data[block], label=block, linewidth=1)

plt.xlabel('Time [s]')
plt.ylabel('Relative Uplift [model units]')
plt.title('Relative Uplift Over Time per Block')
plt.legend(loc='upper right', fontsize='small', ncol=2)
plt.grid(True)
plt.tight_layout()
plt.show()
