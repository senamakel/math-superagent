#!/usr/bin/env python3
"""Emit bounded slices of the extracted sequences for the sequence tools."""
import sys
from pathlib import Path

def load(path):
    return [int(x) for x in Path(path).read_text().split() if x.strip()]

r = load('/workspace/code/out/seq_rn.txt')
g = load('/workspace/code/out/seq_gn.txt')
sp = load('/workspace/code/out/seq_sp.txt')
pvals = load('/workspace/code/out/seq_p_sorted.txt')

print(f"r: {len(r)} terms, g: {len(g)} terms, S(p): {len(sp)} terms")
print()
print("=== r[0:512] ===")
print(repr(r[:512]))
print()
print("=== r[512:999] ===")
print(repr(r[512:]))
print()
print("=== g[0:512] ===")
print(repr(g[:512]))
print()
print("=== S(p) all 18 ===")
print(repr(sp))
print()
print("=== p sorted all 18 ===")
print(repr(pvals))
