import numpy as np
import pandas as pd

# Significant wave heights to test
Hs_values = [0.5, 0.6, 0.7, 0.8]

# Number of waves simulated
N_waves = 1000

# Ranks of interest (1/1000, 2/1000, etc.)
ranks = [1, 2, 3, 4, 5]

# Prepare results
results = []

for Hs in Hs_values:
    # Rayleigh scale parameter
    b = Hs / np.sqrt(2)
    
    # Generate random wave heights
    wave_heights = np.random.rayleigh(scale=b, size=N_waves)
    
    # Sort descending
    wave_heights_sorted = np.sort(wave_heights)[::-1]
    
    # Get the highest waves
    extremes = [wave_heights_sorted[i-1] for i in ranks]
    
    results.append([Hs] + extremes)

# Create DataFrame
columns = ['Hs (m)'] + [f'{i}/1000 wave' for i in ranks]
df = pd.DataFrame(results, columns=columns)

print(df)

# Optionally save to CSV
df.to_csv('extreme_wave_heights.csv', index=False)