#!/usr/bin/env python3
"""Refuter: does the exact mean threshold weight really grow like ~n^0.57?

The claimed result (GOAL.md / steering directive): theta_mean(n) = min{w :
E_Sw[nu2]/n >= 0.40}, the absolute threshold WEIGHT, grows like n^0.57
(sublinear). If instead the fitted exponent drifts to 1/2, or toward 0.79
(log_4 3), or the absolute weight stops growing sublinearly, the claim "about
n^0.57 switches suffice" is a small-n artifact.

We compute theta_mean EXACTLY (Krawtchouk closed form, grouped by popcount --
no sampling, no enumeration) at n = powers of 2 and fit log2(w) vs log2(n)
between consecutive doublings. Pure arithmetic of the fold on weight-w strings
-- no primes, no number theory.
"""
from math import comb, log2, sqrt

from lib.krawtchouk_sphere import theta_mean


def main():
    print("theta_exponent: exact mean threshold weight vs n", flush=True)
    print("def = theta_mean(n) = min{w : E_Sw[nu2]/n >= 0.40} (exact Krawtchouk)")
    print("range = n = 16..131072 (powers of 2 and +1)", flush=True)
    ns = []
    for k in range(4, 18):
        ns.append(1 << k)
        ns.append((1 << k) + 1)
    rows = []
    for n in ns:
        w, mean = theta_mean(n)
        rows.append((n, w, mean))
        print("n=%7d  w=%5d  w/n=%.6f  mean=%.4f" % (n, w, w / n, mean), flush=True)
    print("")
    print("log2(w) and slope between consecutive doublings (n=2^k -> 2^(k+1)):")
    # collect per power of two
    prev = {}
    for n, w, _ in rows:
        k = int(round(log2(n))) if n & (n - 1) == 0 else None
        if k is None:
            continue
        if k - 1 in prev:
            w0, n0 = prev[k - 1]
            slope = (log2(w) - log2(w0)) / (log2(n) - log2(n0))
            print("  2^%d -> 2^%d : w %d -> %d  slope=%.4f  w/n=%.5f"
                  % (k - 1, k, w0, w, slope, w / n), flush=True)
        prev[k] = (w, n)


if __name__ == "__main__":
    main()
