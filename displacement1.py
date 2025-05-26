from odbAccess import openOdb
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import math
import numpy as np

# --- Settings ---
odb_path = '1.2-9 Block Flume pull test fd/Job-3.odb'
instance_name = 'BLOCK-2-LIN-1-5-LIN-11-1'
node_label = 33

# Slope angle from horizontal in degrees
slope_angle_deg = 30.0
alpha = math.radians(slope_angle_deg)

# Rotation matrix: global -> local
# Rotation around Y-axis (assuming slope lies in X-Z plane)
R = np.array([
    [math.cos(alpha), 0, -math.sin(alpha)],
    [0,               1,  0],
    [math.sin(alpha), 0,  math.cos(alpha)]
])

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
disp_vals_along_slope = []

for frame in second_step.frames:
    time = frame.frameValue
    field = frame.fieldOutputs['U']
    subset = field.getSubset(region=instance)

    for val in subset.values:
        if val.nodeLabel == node_label:
            U_global = np.array(val.data)  # [Ux, Uy, Uz]
            U_local = np.dot(R, U_global)  # Transform to slope-aligned CS
            disp_along_slope = U_local[0]  # Local X' = along slope
            time_vals.append(time)
            disp_vals_along_slope.append(disp_along_slope)
            break

odb.close()

# --- Plot ---
plt.figure(figsize=(8, 5))
plt.plot(time_vals, disp_vals_along_slope, marker='o')
plt.title('Displacement Along Slope\nNode {} in {} (Step: {})'.format(
    node_label, instance_name, step_names[1]))
plt.xlabel('Time (s)')
plt.ylabel('Displacement Along Slope (m)')
plt.grid(True)
plt.tight_layout()
plt.savefig("displacement_along_slope_node{}_{}_step2.png".format(
    node_label, instance_name.replace('-', '_')))
