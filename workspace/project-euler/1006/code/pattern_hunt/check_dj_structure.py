"""PE1006: exact S1 within-run jump structure — d_j extraction.

Conjecture (read off the first ~12 runs):
  For each V-run j (start s_j = floor(j phi^2), end s_{j+1}-1):
     S1(k) = A_j            for k = s_j
     S1(k) = A_j + d_j*10^{s_j}  for k in [s_j+1, s_{j+1}-1]
  where d_j is a positive integer (1..~99), i.e. S1 jumps at s_j+1 by exactly
  d_j at the s_j-th decimal position, then is flat until the next run start.
  Equivalently:  S1(s_j+1) - S1(s_j) = d_j * 10^{s_j}.

Verification: exact integer arithmetic over all runs j = 1..1144 (the data
extends to KMAX=3000; runs 1145, 1146 are truncated by the boundary and are
reported separately).

Then: extract d_j mod M sequence and the raw d_j sequence for the sequence
tools (find_linear_recurrence / analyze_sequence / OEIS).
"""
KMAX = 3000
S1 = [0] * (KMAX + 1)
V = [0] * (KMAX + 1)
for line in open('code/out/s1_exact.txt'):
    k, v = line.split()
    S1[int(k)] = int(v)
for line in open('code/out/vR_exact.txt'):
    k, v = line.split()
    V[int(k)] = int(v)

runs = []
start, v0 = 1, V[1]
for k in range(2, KMAX + 1):
    if V[k] != v0:
        runs.append((start, k - 1, v0))
        start, v0 = k, V[k]
runs.append((start, KMAX, v0))

d_ok = True
d_firstbad = None
d_as_int = []          # raw d_j (integer)
d_mod = []             # d_j mod M
for j in range(1, len(runs)):
    a, b, v = runs[j]
    if b == a:         # truncation singleton (last run)
        continue
    diff = S1[a + 1] - S1[a]
    if diff <= 0 or diff % (10 ** a) != 0:
        d_ok = False
        d_firstbad = (j, a, diff)
        break
    dj = diff // (10 ** a)
    d_as_int.append(dj)
    d_mod.append(dj % 101001001)
    # flat on [a+2, b]
    for k in range(a + 2, b + 1):
        if S1[k] != S1[a + 1]:
            d_ok = False
            d_firstbad = ("flat", j, a, k)
            break
    if not d_ok:
        break

print(f"runs total: {len(runs)-1}, proper runs verified (excl. truncation):", end=" ")
print(len(d_as_int))
print(f"S1(s_j+1) - S1(s_j) == d_j * 10^{{s_j}} with integer d_j > 0, and S1 flat on [s_j+2, s_{{j+1}}-1]: {d_ok}")
if d_firstbad:
    print("first bad:", d_firstbad)

print()
print("first 60 d_j (raw):")
print(d_as_int[:60])

with open('code/out/dj_raw.txt', 'w') as fh:
    for i, d in enumerate(d_as_int, start=1):
        fh.write(f"{i} {d}\n")
with open('code/out/dj_mod.txt', 'w') as fh:
    for i, d in enumerate(d_mod, start=1):
        fh.write(f"{i} {d}\n")
print("wrote code/out/dj_raw.txt, code/out/dj_mod.txt")

# supplementary: distribution of d_j values
from collections import Counter
c = Counter(d_as_int)
print("d_j value distribution (top 15):", c.most_common(15))
print("max d_j:", max(d_as_int), " #distinct values:", len(c))