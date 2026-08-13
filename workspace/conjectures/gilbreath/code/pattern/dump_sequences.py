#!/usr/bin/env python3
"""Dump the sequence data from blocks_depth1000.json for the sequence tools."""
import json

with open('code/out/blocks_depth1000.json') as f:
    d = json.load(f)

b = d['b']
s = d['s']
print('D =', d['D'], ' min_b =', d['min_block'], ' max_b =', d['max_block'])
print('first_bad =', d['first_bad'])

# block length b(k)
print('\nb(1..1000) =', b)
# second entry s(k), and s/2 (binary)
print('\ns(1..1000) =', s)
print('\ns/2 (binary) =', [x // 2 for x in s])

# regeneration events: k where b(k+1) >= b(k), i.e. diff >= 0
diffs = [b[i + 1] - b[i] for i in range(len(b) - 1)]
reg = [(i + 1, diffs[i]) for i in range(len(diffs)) if diffs[i] >= 0]
print('\nregeneration events k (b(k+1)-b(k) >= 0):', reg)
print('number of regen events:', len(reg))
print('jump sizes at regeneration:', [r[1] for r in reg])
print('regen k values:', [r[0] for r in reg])

# erosion run lengths
runs = []
cur = 1 if diffs[0] == -1 else 0
for x in diffs:
    if x == -1:
        cur += 1
    else:
        if cur:
            runs.append(cur)
        cur = 0
if cur:
    runs.append(cur)
print('\nerosion run lengths (consecutive -1 diffs):', runs)
print('num erosion runs:', len(runs), ' max:', max(runs))

# state right before regeneration: b at regen point, and the dip below
print('\nb[k] just before regen events (i.e. b at end of erosion):', end=' ')
print([b[r[0] - 1] if r[0] >= 1 else None for r in reg])

# b values where erosion bottoms out: local minima of b
lmin = []
for i in range(1, len(b) - 1):
    if b[i] <= b[i - 1] and b[i] < b[i + 1]:
        lmin.append((i + 1, b[i]))
print('local minima of b (k, b) exclusive of first term:', lmin)
print('global min over k>=2:', min(b[1:]), 'at k =', b[1:].index(min(b[1:])) + 2)

# s run lengths
sruns = []
cur, clen = s[0], 1
for x in s[1:]:
    if x == cur:
        clen += 1
    else:
        sruns.append((cur, clen))
        cur, clen = x, 1
sruns.append((cur, clen))
print('\ns run length distribution by value:')
for v in (0, 2):
    lens = [t[1] for t in sruns if t[0] == v]
    print(f'  s={v}: runs={len(lens)}, min={min(lens)}, max={max(lens)}, '
          f'mean={sum(lens)/len(lens):.2f}')

# positions where s changes: regen events for s? every time s changes
print('\ns change positions (k+1 where s differs):', end=' ')
print([i + 2 for i in range(len(s) - 1) if s[i] != s[i + 1]])
print('num s changes:', sum(1 for i in range(len(s) - 1) if s[i] != s[i + 1]))