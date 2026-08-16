#!/usr/bin/env python3
"""Increment structure of S(n) vs the prime string h and switch density.

D(n) = S(n+1) - S(n).  Established: mean(D)=0, std(D) large (sqrt scale).
Question: does D(n) correlate with any LOCAL feature of h (local switch
density, local 1-density, specific h[j] windows), or is it fold-structural?
We compute, for n in a window:
    D(n) = -2*(nu2(n+1)-nu2(n)) + 1     [since S=(n-2)-2 nu2]
and correlate with local features of h near its reading window.
"""
import numpy as np
import json
from lib.primes import h_string


def main():
    ny = json.load(open('code/out/nu2_primes_xor_40000.json'))
    N = 30000
    h = h_string(N + 1)
    # D(n) for n in [50, N]
    D = {}
    for n in range(50, N):
        # S(n) = (n-2) - 2*ny[n]
        d = ((n + 1 - 2) - 2 * ny[n + 1]) - ((n - 2) - 2 * ny[n])
        D[n] = d
    ds = np.array([D[n] for n in range(50, N)])
    print(f"D(n)=S(n+1)-S(n), n in [50,{N}): mean={ds.mean():.4f} "
          f"std={ds.std():.2f} min={ds.min()} max={ds.max()}")

    # correlate D(n) with nu2(n)/n and with local 1-density of h centred near n
    # First: D vs nu2(n)/n (does the increment depend on current fold weight?)
    vals_n = []
    for n in range(50, N):
        vals_n.append(ny[n] / n)
    print(f"corr(D(n), nu2(n)/n) = {np.corrcoef(np.array(vals_n), ds)[0,1]:+.4f}")

    # D(n) vs local 1-density h over a window of length L centred near n
    for L in [10, 50, 200]:
        loc = []
        cnt = 0
        for n in range(50, N):
            # h window [n-L, n+L]
            lo, hi = max(0, n - L), min(len(h) - 1, n + L)
            loc.append(sum(h[lo:hi + 1]) / (hi - lo + 1))
            cnt += 1
        c = np.corrcoef(np.array(loc), ds)[0, 1]
        print(f"corr(D(n), local-1-density window L={L}) = {c:+.4f}")

    # D(n) vs local SWITCH density of h
    for L in [10, 50, 200]:
        loc = []
        for n in range(50, N):
            lo, hi = max(0, n - L), min(len(h) - 1, n + L)
            sw = sum(1 for j in range(lo, hi) if h[j] != h[j + 1]) / (hi - lo)
            loc.append(sw)
        c = np.corrcoef(np.array(loc), ds)[0, 1]
        print(f"corr(D(n), local-switch window L={L}) = {c:+.4f}")


if __name__ == "__main__":
    main()
