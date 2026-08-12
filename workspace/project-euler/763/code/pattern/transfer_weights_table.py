#!/usr/bin/env python3
"""Final read-only table: D(N) from data dumps, and every histogram containing
a 6-level with its multiplicity (the exceptional family)."""
import glob, collections

def hist_of_line(line):
    return line.split('|')[0].strip()

print("D(N) from data dumps (#config lines per level file):")
tot = 0
for path in sorted(glob.glob('data/level_*.txt'), key=lambda p: int(p.split('level_')[1].split('.')[0])):
    n = int(path.split('level_')[1].split('.')[0])
    c = sum(1 for _ in open(path))
    print(f"  N={n:2d}: D={c}")
    tot += c

print("\nAll histograms containing a 6-level (N, hist, mult):")
rows6 = []
for line in open('code/out/per_hist_mult_13_14.txt'):
    line = line.strip()
    if not line.startswith('N=') or 'mult=' not in line: continue
    n = int(line[2:line.index('hist=')].strip())
    h = line.index('hist='); mi = line.index('mult=')
    hstr = line[h+5:mi].strip(); mval = int(line[mi+5:])
    vals = [int(x) for x in hstr.split()]  # keep padding to show stored form
    if 6 in vals:
        rows6.append((n, ' '.join(map(str, vals)), mval))
for path in sorted(glob.glob('data/level_*.txt'), key=lambda p: int(p.split('level_')[1].split('.')[0])):
    n = int(path.split('level_')[1].split('.')[0])
    per = collections.Counter()
    for line in open(path):
        per[hist_of_line(line)] += 1
    for hist, m in per.items():
        vals = list(map(int, hist.split()))
        if 6 in vals:
            rows6.append((n, hist, m))
seen = set(); 
for n, h, m in sorted(set(rows6)):
    key = (n, h)
    if key in seen: continue
    seen.add(key)
    print(f"  N={n:2d}  {h}  mult={m}")
print("total distinct 6-containing histograms:", len(seen))