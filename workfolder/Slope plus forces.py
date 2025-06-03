import numpy as np
import matplotlib.pyplot as plt
from scipy.special import erf
from matplotlib.animation import FuncAnimation
from matplotlib.widgets import Button, Slider
from scipy.interpolate import interp1d

# --- Dike Profile & Block Coordinates (unchanged) ---
x_base = [0, 6, 6.05, 16.55, 16.5, 24.9, 26.9]
y_base = [0, 2, 1.86, 5.36, 5.5, 8.3, 8.3]
x_start, y_start = 6.05, 1.86
block_width = 0.5
block_height = 0.15
n_blocks = 22
slope = 1 / 3
angle_rad = np.arctan(slope)
slope_angle = np.degrees(angle_rad)
x_step = block_width * np.cos(angle_rad)
y_step = block_width * np.sin(angle_rad)
block_x = [x_start + i * x_step for i in range(n_blocks)]
block_y = [y_start + i * y_step for i in range(n_blocks)]
block_x_centers = [block_x[j] + block_width / 2 for j in range(n_blocks)]
block_y_centers = [
    block_y[j] + np.sin(angle_rad) * (block_width / 2) + block_height / 2
    for j in range(n_blocks)
]

# --- Slope coordinate (xx) for plot 4 ---
xx = np.linspace(0, 12, 300)

# --- Blue curve: Trapezoid (wave impact) ---
wave_impact_x = np.piecewise(
    xx,
    [xx < 4, (xx >= 4) & (xx < 4.5), (xx >= 4.5) & (xx < 5.5), (xx >= 5.5) & (xx < 6), xx >= 6],
    [
        0,
        lambda x: (x - 4) * (9.54 / 0.5),           # Rise from 0 to 9.54
        9,54,
        lambda x: 9.54 - (x - 5.5) * (9.54 / 0.5),    # Fall from 9,54 to 0
        0
    ]
)
A = 10
x1 = 4.5
x2 = 5.5
sigma = 0.7
filter_response_x = A * (erf((xx - x1) / sigma) - erf((xx - x2) / sigma)) / 2
filter_response_x = -filter_response_x
residual_x = filter_response_x + wave_impact_x  # CHANGED TO SUM

# --- Convert xx to y_along_slope for interpolation over y ---
y_along_slope = y_start + slope * xx

# --- Interpolators for y coordinates ---
wave_head_from_y = interp1d(y_along_slope, wave_impact_x, bounds_error=False, fill_value=0)
filter_head_from_y = interp1d(y_along_slope, filter_response_x, bounds_error=False, fill_value=0)
residual_head_from_y = interp1d(y_along_slope, residual_x, bounds_error=False, fill_value=0)

block_heads_wave_impact = wave_head_from_y(block_y_centers)
block_heads_filter = filter_head_from_y(block_y_centers)
block_heads_residual = residual_head_from_y(block_y_centers)

# --- For subplot 5 (time-plot): New time vector and force definitions ---
tt = np.linspace(0, 4, 200)  # Extended time: 0 to 4 seconds

# Define the "pulse" between 2.0s and 2.25s
wave_impact_t = np.zeros_like(tt)
filter_response_t = np.zeros_like(tt)

pulse_indices = (tt >= 2.0) & (tt <= 2.25)
pulse_t = tt[pulse_indices] - 2.0  # Pulse time: 0 to 0.25s
# Original pulse profile (triangle): 0 → 10 at t=0.05, then 0 at t=0.25
wave_impact_t[pulse_indices] = np.interp(
    pulse_t, [0, 0.05, 0.25], [0, 10, 0]
)
filter_response_t[pulse_indices] = np.interp(
    pulse_t, [0, 0.05, 0.25], [0, 6, 0]
)
filter_response_t = -filter_response_t  # Negative filter response in time

residual_t = filter_response_t + wave_impact_t

# Normalize by the maximum force (which is still 10)
norm_factor = np.max(np.abs(wave_impact_t))
if norm_factor == 0:
    norm_factor = 1
wave_impact_t /= norm_factor
filter_response_t /= norm_factor
residual_t /= norm_factor

# --- Prepare interpolation functions from plot 5 for animation ---
t_anim = np.linspace(0, 4, 201)
wave_func = interp1d(tt, wave_impact_t, kind='linear', fill_value=0, bounds_error=False)
filter_func = interp1d(tt, filter_response_t, kind='linear', fill_value=0, bounds_error=False)
residual_func = interp1d(tt, residual_t, kind='linear', fill_value=0, bounds_error=False)

# --- Plot Setup: 2 rows, 3 columns (figure size increased) ---
fig, axes = plt.subplots(2, 3, figsize=(22, 8))

def plot_blocks(ax):
    ax.fill_between(x_base, y_base, 0, color='khaki', alpha=0.7)
    for i in range(n_blocks):
        rect = plt.Rectangle((block_x[i], block_y[i]), block_width, block_height,
                             angle=slope_angle, color='saddlebrown', ec='black', lw=1)
        ax.add_patch(rect)
    ax.set_xlim(-2, 30)
    ax.set_ylim(-2, 14)
    ax.set_aspect('equal')
    ax.axis('off')

# --- Animated Subplots 1–3 (top row) ---
for i in range(3):
    plot_blocks(axes[0, i])
titles = ["Wave Forcing", "Filter Response", "Residual"]
for i in range(3):
    axes[0, i].set_title(titles[i])

# --- Animated Arrows for Each Plot (as before, but with correct y) ---
arrow_objs = [[], [], []]
colors = ['royalblue', 'red', 'green']
block_heads = [block_heads_wave_impact, block_heads_filter, block_heads_residual]

for plot_idx in range(3):
    for _ in range(n_blocks):
        arr = axes[0, plot_idx].arrow(0, 0, 0, 0, head_width=0.1, head_length=0.1, 
                                      fc=colors[plot_idx], ec=colors[plot_idx])
        arrow_objs[plot_idx].append(arr)

# --- Plot 4: Hydraulic Head vs Slope Coordinate (was axes[1,1], now axes[1,0]) ---

axes[1, 0].plot(xx, wave_impact_x, color='royalblue', label='Wave Impact')
axes[1, 0].plot(xx, filter_response_x, color='orange', label='Filter Response (negative, sigma=0.7)')
axes[1, 0].plot(xx, residual_x, color='green', label='Residual (sum)')
axes[1, 0].axvline(5, color='k', linestyle='--', label='Location Time Diagram')
axes[1, 0].set_xlim(0, 12)
axes[1, 0].set_ylim(-10, 12)
axes[1, 0].set_xlabel('Coordinate on the Slope from Top Revetment [m]')
axes[1, 0].set_ylabel('Hydraulic Head [m]')
axes[1, 0].legend(fontsize=10)
axes[1, 0].grid(True, which='both', linestyle='--', alpha=0.7)
axes[1, 0].set_title("Hydraulic Head on Slope")

# --- Plot 5: Normalized Force-Time Graph (was axes[1,2], now axes[1,1]) ---
line_wave, = axes[1, 1].plot(tt, wave_impact_t, color='royalblue', lw=2, label='Wave Impact')
line_filter, = axes[1, 1].plot(tt, filter_response_t, color='orange', lw=2, label='Filter Response (negative)')
line_resid, = axes[1, 1].plot(tt, residual_t, color='green', lw=2, label='Residual (sum)')
axes[1, 1].plot([2.05, 2.05], [-1.2, 1.2], 'k--', label='Moment Space Diagram')
axes[1, 1].set_xlim(0, 4)
axes[1, 1].set_ylim(-1.2, 1.2)
axes[1, 1].set_xlabel('Time [s]')
axes[1, 1].set_ylabel('Normalized Force [-]')
axes[1, 1].grid(True, which='both', linestyle='--', alpha=0.7)
axes[1, 1].legend(fontsize=10)
axes[1, 1].set_title("Normalized Force vs Time")
dot_wave, = axes[1, 1].plot([0], [wave_impact_t[0]], 'o', color='royalblue', markersize=10)
dot_filter, = axes[1, 1].plot([0], [filter_response_t[0]], 'o', color='orange', markersize=10)
dot_resid, = axes[1, 1].plot([0], [residual_t[0]], 'o', color='green', markersize=10)

# --- Empty axes[1,2] for buttons and slider ---
axes[1, 2].axis('off')

# --- Buttons in axes[1,2]'s location (place high in the axes space) ---
btn_start = Button(plt.axes([0.78, 0.21, 0.08, 0.06]), 'Start')
btn_pause = Button(plt.axes([0.88, 0.21, 0.08, 0.06]), 'Pause')

# --- Slider directly beneath the buttons (same right column) ---
slider_ax = plt.axes([0.78, 0.13, 0.18, 0.04])
time_slider = Slider(slider_ax, 'Time', 0, len(tt) - 1, valinit=0, valstep=1)

# --- Animation Control ---
running = {'animate': False}
current_frame = {'frame': 0}

def update_arrows_and_dots(frame):
    t = tt[frame]
    scale = float(wave_func(t))
    filter_scale = float(filter_func(t))
    resid_scale = float(residual_func(t))
    scaled_heads = [
        block_heads_wave_impact * scale,
        block_heads_filter * scale,
        block_heads_residual * scale
    ]
    for i in range(3):
        for j, arr in enumerate(arrow_objs[i]):
            arrow_x = block_x[j] + block_width / 2
            arrow_y = block_y_centers[j]
            F = -scaled_heads[i][j]   # <--- FLIP DIRECTION
            arrow_dx = -np.sin(angle_rad) * F
            arrow_dy = np.cos(angle_rad) * F
            arr.remove()
            arr_new = axes[0, i].arrow(arrow_x, arrow_y, arrow_dx, arrow_dy,
                                       head_width=0.1, head_length=0.1, 
                                       fc=colors[i], ec=colors[i])
            arrow_objs[i][j] = arr_new
    # Update dots in the normalized force-time plot
    dot_wave.set_data([t], [scale])
    dot_filter.set_data([t], [filter_scale])
    dot_resid.set_data([t], [resid_scale])
    fig.canvas.draw_idle()

def animate(frame):
    if not running['animate']:
        frame = current_frame['frame']
    else:
        current_frame['frame'] = frame
    update_arrows_and_dots(frame)
    return sum(arrow_objs, []) + [dot_wave, dot_filter, dot_resid]

def start(event):
    running['animate'] = True

def pause(event):
    running['animate'] = False

def slider_update(val):
    running['animate'] = False
    current_frame['frame'] = int(time_slider.val)
    update_arrows_and_dots(current_frame['frame'])

btn_start.on_clicked(start)
btn_pause.on_clicked(pause)
time_slider.on_changed(slider_update)

# --- Run Animation ---
ani = FuncAnimation(fig, animate, frames=len(tt), interval=50, blit=False, repeat=True)
plt.tight_layout()
plt.show()
