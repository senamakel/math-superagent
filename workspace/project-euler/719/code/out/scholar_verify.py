import sys

# Independent verification of T(10^12) from the catalogued roots (roots408.txt)
roots = []
with open('/workspace/code/out/roots408.txt') as f:
    for line in f:
        line = line.strip()
        if line:
            roots.append(int(line))

# S-numbers are n = m^2 with root m >= 2 (exclude sentinels 0 and 1)
valid = [m for m in roots if m >= 2]

total = sum(m*m for m in valid)
n_terms = len(valid)
last = max(valid)

print("roots with m>=2:", n_terms)
print("largest root:", last)
print("T(10^12) = sum of m^2 over catalogued roots =", total)

# Sanity: oracle T(10^4) = 41333 from the same list
t10k = sum(m*m for m in valid if m*m <= 10**4)
print("T(10^4) from list =", t10k)
