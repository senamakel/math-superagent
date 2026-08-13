#!/usr/bin/env python3
"""Extract the sequence data from code/out/witnesses.json (block lengths and
second entries for k=1..40) and print it ready to feed the sequence tools.

Source: the run's own witness file -- the oracle rows the generator produced.
Also prints b(k+1)-b(k), which is the quantity that measures {0,2}-block
consumption (=-1, pure erosion) vs regeneration (>= 0).
"""
import json

with open('/workspace/code/out/witnesses.json') as f:
    w = json.load(f)

prof = w['block_profile_first_40']
k = [e['k'] for e in prof]
b = [e['block'] for e in prof]
s = [e['second'] for e in prof]
assert k == list(range(1, 41)), k

print('b(1..40) =', b)
print('s(1..40) =', s)
diffs = [b[i + 1] - b[i] for i in range(len(b) - 1)]
print('b(k+1)-b(k) =', diffs)
print('min b =', min(b), 'at k =', b.index(min(b)) + 1)
print('max b =', max(b), 'at k =', b.index(max(b)) + 1)
print('min block diff =', min(diffs), ' (must be >= -1 by {0,2} closure)')
print('s/2 =', [x // 2 for x in s])