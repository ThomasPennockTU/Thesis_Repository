import csv
import matplotlib.pyplot as plt

# === CONFIGURATION ===
csv_file = 'relative_uplift_timeseries_06.csv'

# === LOAD DATA ===
times = []
block_names = []
uplift_data = {}

with open(csv_file, 'r') as f:
    reader = csv.reader(f)
    header = next(reader)

    # Header now has: ['Step', 'Time', 'B-1-1', ...]
    block_names = header[2:]   # skip Step and Time columns

    for block in block_names:
        uplift_data[block] = []

    for row in reader:
        # row[0] → Step name
        # row[1] → Time
        time_str = row[1]
        if time_str:
            times.append(float(time_str))
        else:
            times.append(None)

        for i, block in enumerate(block_names):
            val = row[i + 2]   # shift by 2 columns
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
