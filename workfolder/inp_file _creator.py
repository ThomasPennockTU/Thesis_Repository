import os
print(os.listdir())

# 1. Read the .inp file
with open("workfolder/Job-2.inp", "r") as f:
    lines = f.readlines()

# 2. Show first 10 lines for preview
print("First 10 lines of the .inp file:")
for line in lines[:]:
    print(line.strip())

# 3. Export to a new .inp file
with open("workfolder/Job-test.inp", "w") as f:
    f.writelines(lines)

print("\n✅ File successfully re-exported as 'output_file.inp'")