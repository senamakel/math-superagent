#!/usr/bin/env python3
"""Probe: time exact factorization of L_p, M_p for a set of odd primes p.

Purpose: calibrate the feasible bound for the full extension table (how far
p can go while every 2^{2p}+1 fully factors within a 540s budget on 28 cores).

Math: 2^{2p}+1 = L_p * M_p,  L_p = 2^p - 2^((p+1)/2) + 1,
      M_p = 2^p + 2^((p+1)/2) + 1, coprime and odd, each ~ p*log10(2)
      digits.  This probe times sympy.factorint on each half for a sparse
      selection of p so the full run below can pick a feasible PMAX.
"""
import time
from sympy import factorint

PROBES = [61, 83, 97, 101, 127, 139, 151, 173, 197, 211, 251, 307, 331, 401]


def main():
    for p in PROBES:
        s = pow(2, (p + 1) // 2)
        L = 2 ** p - s + 1
        M = 2 ** p + s + 1
        t0 = time.time()
        fL = factorint(L)
        tL = time.time() - t0
        t0 = time.time()
        fM = factorint(M)
        tM = time.time() - t0
        digits = len(str(L))
        print("p=%d  L(%d digits)=%s  M(%d digits)=%s  tL=%.2fs tM=%.2fs"
              % (p, digits, {k: fL[k] for k in sorted(fL)},
                 digits, {k: fM[k] for k in sorted(fM)}, tL, tM), flush=True)


if __name__ == "__main__":
    main()
