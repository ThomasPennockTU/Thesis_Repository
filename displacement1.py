from odbAccess import openOdb
import matplotlib
matplotlib.use('Agg')  # Ensures compatibility in non-GUI mode
import matplotlib.pyplot as plt

# --- Settings ---
odb_path = '1.2-9 Block Flume pull test fd/Job-3.odb'
instance_name = 'BLOCK-2-LIN-1-5-LIN-11-1'
node_label = 33
direction_index = 2  # Z-direction (U3)

# --- Open ODB ---
odb = openOdb(path=odb_path)
step = odb.steps.values()[0]
instance = odb.rootAssembly.instances[instance_name]

# --- Collect data ---
time_vals = []
disp_vals = []

for frame in step.frames:
    time = frame.frameValue
    field = frame.fieldOutputs['U']
    subset = field.getSubset(region=instance)

    for val in subset.values:
        if val.nodeLabel == node_label:
            displacement = val.data[direction_index]
            time_vals.append(time)
            disp_vals.append(displacement)
            break  # Stop once we find the node in this frame

odb.close()

# --- Plot ---
plt.figure(figsize=(8, 5))
plt.plot(time_vals, disp_vals, marker='o')
plt.title('Vertical Displacement of Node {} in {}'.format(node_label, instance_name))
plt.xlabel('Time (s)')
plt.ylabel('Displacement U3 (m)')
plt.grid(True)
plt.tight_layout()
plt.savefig("displacement_node{}_{}.png".format(node_label, instance_name.replace('-', '_')))
