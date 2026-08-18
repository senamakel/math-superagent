import os

# Read problem.md
with open('/workspace/problem.md', 'r') as f:
    print("=== problem.md ===")
    print(f.read())

# List workspace
print("\n=== workspace listing ===")
for root, dirs, files in os.walk('/workspace'):
    level = root.replace('/workspace', '').count(os.sep)
    indent = ' ' * 2 * level
    print(f'{indent}{os.path.basename(root)}/')
    subindent = ' ' * 2 * (level + 1)
    for file in files:
        print(f'{subindent}{file}')
