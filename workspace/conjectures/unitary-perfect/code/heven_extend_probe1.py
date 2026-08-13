#!/usr/bin/env python3
"""Probe individual L_p, M_p factorizations for large p, per-p timing.

Each p probed in a separate subprocess with its own timeout so one hard
number cannot eat the whole budget.  Prints the p, digit count, per-half
factor result and elapsed time.  EXIT_CODE per p reported separately.
"""
import sys, time
from sympy import factorint

p = int(sys.argv[1])
s = pow(2, (p + 1) // 2)
L = 2 ** p - s + 1
M = 2 ** p + s + 1
digits = len(str(L))
t0 = time.time()
fL = factorint(L)
tL = time.time() - t0
t0 = time.time()
fM = factorint(M)
tM = time.time() - t0
print("p=%d digits=%d L=%s tL=%.2fs | M=%s tM=%.2fs"
      % (p, digits, {k: fL[k] for k in sorted(fL)}, tL,
         {k: fM[k] for k in sorted(fM)}, tM), flush=True)
