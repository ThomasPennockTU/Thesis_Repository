from PIL import Image
import os

# Load wave tile and dike (foreground)
wave_tile = Image.open('/Users/thomaspennock/Documents/TUDelft/Civiel2024-2025/ThesisPrep/Thesis_Repository/workfolder/wave_animation_test/wave2.png').convert('RGBA')
dike = Image.open('/Users/thomaspennock/Documents/TUDelft/Civiel2024-2025/ThesisPrep/Thesis_Repository/workfolder/wave_animation_test/background.png').convert('RGBA')

# Resize dike to 50% of original size
dike = dike.resize((dike.width // 2, dike.height // 2), resample=Image.Resampling.LANCZOS)
dike_width, dike_height = dike.size  # Update for placement

# Wave tile and animation parameters
num_tiles = 4
overlap_px = 10
tile_width, tile_height = wave_tile.size
effective_tile_width = tile_width - overlap_px

# Frame and wave strip dimensions
frame_width = tile_width * 2 - overlap_px
frame_height = tile_height
y_offset = frame_height // 2  # Lower wave by half a frame

# Build the full wave strip with overlapping tiles
total_width = effective_tile_width * (num_tiles - 1) + tile_width
full_wave = Image.new('RGBA', (total_width, frame_height + y_offset), (255, 255, 255, 0))
for i in range(num_tiles):
    x_pos = i * effective_tile_width
    full_wave.paste(wave_tile, (x_pos, y_offset), wave_tile)

# Animation settings
num_frames = 100
total_shift = tile_width
shift_per_frame = float(total_shift) / num_frames

# Generate animation frames
frames = []
for i in range(num_frames):
    shift = int(round(i * shift_per_frame))
    right = total_width - shift
    left = right - frame_width

    if left < 0:
        break

    # Create empty frame
    frame = Image.new('RGBA', (frame_width, frame_height), (255, 255, 255, 0))

    # Crop and paste the wave background
    wave_crop = full_wave.crop((left, 0, right, frame_height))
    frame.paste(wave_crop, (0, 0), wave_crop)

    # Paste the resized dike in front, aligned bottom-right
    dike_x = frame_width - dike_width
    dike_y = frame_height - dike_height
    frame.paste(dike, (dike_x, dike_y), dike)

    # Convert to RGB (or leave as RGBA if you want transparency)
    frames.append(frame.convert('RGB'))

print(f"Aantal gegenereerde frames: {len(frames)}")

# Save as animated GIF
if frames:
    frames[0].save(
        '/Users/thomaspennock/Documents/TUDelft/Civiel2024-2025/ThesisPrep/Thesis_Repository/workfolder/wave_animation_test/seamless_wave_loop.gif',
        save_all=True,
        append_images=frames[1:],
        duration=20,
        loop=0
    )
else:
    print("⚠️ Geen frames gegenereerd. Controleer of wave2.png en background.png correct zijn geladen.")
