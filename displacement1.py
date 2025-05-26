from odbAccess import openOdb
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt

# --- Settings ---
odb_path = '1.2-9 Block Flume pull test fd/Job-3.odb'
instance_name = 'BLOCK-2-LIN-1-5-LIN-11-1'
node_label = 33
direction_index = 2  # Z-direction

# --- Open ODB ---
odb = openOdb(path=odb_path)

# --- Get second step ---
step_names = odb.steps.keys()
if len(step_names) < 2:
    raise ValueError("ODB does not contain a second step.")

second_step = odb.steps[step_names[1]]
instance = odb.rootAssembly.instances[instance_name]
print(step_names)

# --- Collect data ---
time_vals = []
disp_vals = []

for frame in second_step.frames:
    time = frame.frameValue
    field = frame.fieldOutputs['U']
    subset = field.getSubset(region=instance)

    for val in subset.values:
        if val.nodeLabel == node_label:
            displacement = val.data[direction_index]
            time_vals.append(time)
            disp_vals.append(displacement)
            break

odb.close()

# --- Plot ---
plt.figure(figsize=(8, 5))
plt.plot(time_vals, disp_vals, marker='o')
plt.title('Z-Displacement of Node {} in {}\n(Step: {})'.format(
    node_label, instance_name, step_names[1]))
plt.xlabel('Time (s)')
plt.ylabel('Displacement U3 (m)')
plt.grid(True)
plt.tight_layout()
plt.savefig("displacement_node{}_{}_step2.png".format(
    node_label, instance_name.replace('-', '_')))
