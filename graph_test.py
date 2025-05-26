from odbAccess import openOdb
import matplotlib.pyplot as plt

# --- Open the ODB file ---
odb = openOdb(path='1.2-9 Block Flume pull test/Job-1.odb')  # Replace with your .odb filename

# --- Access the instance (note: instance names are uppercase in ODB) ---
instance_name = 'BLOCK-2-LIN-1-5-LIN-11-1'  # Use exact name, uppercase
instance = odb.rootAssembly.instances[instance_name]

# --- Extract Z-coordinates (height) of all nodes in the instance ---
z_coords = [node.coordinates[2] for node in instance.nodes]

# --- Compute height range ---
min_z = min(z_coords)
max_z = max(z_coords)
height = max_z - min_z

# --- Print height information ---
print(f"Instance: {instance_name}")
print(f"Minimum Z: {min_z:.4f} m")
print(f"Maximum Z: {max_z:.4f} m")
print(f"Total Height: {height:.4f} m")

# --- Plot histogram of z-coordinates ---
plt.figure(figsize=(8, 5))
plt.hist(z_coords, bins=20, edgecolor='black')
plt.title(f'Z-Coordinate Distribution of Nodes in {instance_name}')
plt.xlabel('Z-Coordinate (m)')
plt.ylabel('Number of Nodes')
plt.grid(True)
plt.tight_layout()
plt.show()

# --- Close the ODB ----
odb.close()
