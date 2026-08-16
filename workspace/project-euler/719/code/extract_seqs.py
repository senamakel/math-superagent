#!/usr/bin/env python3
"""Extract integer sequences from the A038206 b-file for pattern analysis."""
import re

B_FILE = "research/sources/oeis_a038206_b.full.md"

def load_roots(path):
    roots = []
    with open(path) as f:
        for line in f:
            m = re.match(r"\s*(\d+)\s+(\d+)\s*$", line)
            if m:
                roots.append(int(m.group(2)))
    return roots

roots = load_roots(B_FILE)
roots369 = [r for r in roots if r <= 100]  # the small roots
print("num roots:", len(roots))
print("small roots (<=100):", roots369)
print("first 40 roots:", roots[:40])
print("root values for S-numbers <= 10^4:", [r for r in roots if r*r <= 10**4])
