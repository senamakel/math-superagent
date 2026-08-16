#!/usr/bin/env python3
"""Verify the fold-cell structure for n=7 by the canonical oracle and print
the exact cells, so a TPTP encoding can be matched term-for-term against it.

NOT the final program — just a scratch check that the read-cone / cell layout
I use (T2..T6 for n=7) is right.
"""
import sys
sys.path.insert(0, "/workspace/code")
from lib.supply_fold import t_direct

n = 7
h = [0, 1, 0, 1, 0, 1, 0]   # arbitrary
for d in range(2, n):
    print("d=%d t_direct=%d" % (d, t_direct(n, d, h)))
