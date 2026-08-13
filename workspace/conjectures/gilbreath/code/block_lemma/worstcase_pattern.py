#!/usr/bin/env python3
"""Identify precisely which block patterns achieve the minimum self-preservation
depth n+1 under an adversarial-even tail (and which achieve a larger one), so we
can state the structural claim exactly rather than hand-wave 'the constant block'."""
from itertools import product


def self_preservation(block):
    """Rows starting with 1 from row [1]+block+[4]+[4]*40; count."""
    row = [1] + list(block) + [4] + [4] * 40
    cur = list(row)
    run = 0
    while cur[0] == 1 and len(cur) > 1:
        run += 1
        cur = [abs(cur[i] - cur[i + 1]) for i in range(len(cur) - 1)]
    return run


for n in (1, 2, 3):
    depths = {}
    for bits in product((0, 2), repeat=n):
        d = self_preservation(list(bits))
        depths.setdefault(d, []).append(bits)
    mn = min(depths)
    print(f"n={n}: min self-preservation = {mn}")
    print(f"   patterns at min ({len(depths[mn])}): {[''.join(str(b//2) for b in p) for p in depths[mn]]}")
    others = {d: [''.join(str(b//2) for b in p) for p in pats]
              for d, pats in depths.items() if d != mn}
    print(f"   all maxima = {max(depths)}, counts = "
          f"{ {d: len(p) for d, p in depths.items()} }")
