#!/usr/bin/env python3
"""Test all 228 unique kernel members of C_11 at k=4 with a complete SAT oracle.

Reads the unique edge lists collected from the 28 residue slices, runs the
calibrated complete k=4 colourability test (lib.satcolor) on each, and reports
whether any member is NOT 4-colourable (a candidate 5-chromatic unit-distance
graph). Independent second route (lib.coloring backtracking) cross-checks a
sample.
"""
import glob, sys
sys.path.insert(0, "/workspace/code")
from lib.satcolor import is_k_colorable, verify_witness
from lib.coloring import chromatic_colorable

members = []
for f in sorted(glob.glob("/workspace/code/out/kernel_slices/res*_of28.txt")):
    for line in open(f):
        line = line.strip()
        if line:
            # line is repr of sorted edge list like [(0,1),(1,2),...]
            members.append(eval(line))

n = 11
print(f"unique kernel members: {len(members)}")
failures = []
for idx, edges in enumerate(members):
    edges = [tuple(e) for e in edges]
    sat, witness = is_k_colorable(edges, 4, n)
    if not sat:
        failures.append((idx, edges))
        print(f"  NON-4-COLOURABLE member idx={idx} edges={edges}")
    else:
        verify_witness(edges, witness, 4)
print(f"all {len(members)} members 4-colourable: {len(failures)==0}")
print(f"failures: {len(failures)}")

# independent cross-check on all (if cheap) via backtracking lib
print("independent backtracking cross-check (lib.coloring):")
bt_fail = 0
for idx, edges in enumerate(members):
    edges = [tuple(e) for e in edges]
    ok, w = chromatic_colorable(n, edges, 4)
    if not ok:
        bt_fail += 1
        print(f"  BACKTRACKING NON-4COL idx={idx}")
print(f"backtracking all-4col universal: {bt_fail==0} ({bt_fail} fails)")
