import matplotlib
matplotlib.use('Agg')

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
print("Instance: {}".format(instance_name))
print("Minimum Z: {:.4f} m".format(min_z))
print("Maximum Z: {:.4f} m".format(max_z))
print("Total Height: {:.4f} m".format(height))

# --- Plot histogram of z-coordinates ---
plt.figure(figsize=(8, 5))
plt.hist(z_coords, bins=20, edgecolor='black')
plt.title('Z-Coordinate Distribution of Nodes in {}'.format(instance_name))
plt.xlabel('Z-Coordinate (m)')
plt.ylabel('Number of Nodes')
plt.grid(True)
plt.tight_layout()
plt.show()

# --- Close the ODB ---
odb.close()

plt.savefig("z_distribution.png")
