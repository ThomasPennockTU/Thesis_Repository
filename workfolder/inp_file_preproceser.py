inp_lines = []

for col in df.columns[1:]:  # Skip "TIME", use "ROW1" to "ROW22"
    inp_lines.append(f"*AMPLITUDE, NAME={col}, TIME=TOTAL TIME\n")
    
    for t, val in zip(df["TIME"], df[col]):
        inp_lines.append(f"{t:.3f}, {val:.5f}\n")  # Format: time, force
    
    inp_lines.append("\n")  # Separate blocks

# Preview first few lines
print("".join(inp_lines[:30]))
