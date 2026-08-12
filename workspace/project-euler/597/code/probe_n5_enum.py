#!/usr/bin/env python3
"""Probe: how far does the exact cell enumeration get for n=5 (d=4), and how
many leaves/cells does it produce? No volume computation. Just timing/scaling
of enumerate_cells, which is the real bottleneck.thesis check."""
import sys, os, time, math
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "toolkits"))
from arr_enum import enumerate_cells

for L in (400, 1800):
    t0 = time.time()
    leaves, planes = enumerate_cells(5, L, verbose=True)
    dt = time.time() - t0
    print(f"L={L}: {len(planes)} planes, {len(leaves)} cells, {dt:.2f}s")
    sys.stdout.flush()
