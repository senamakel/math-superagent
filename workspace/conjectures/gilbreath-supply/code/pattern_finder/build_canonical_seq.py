#!/usr/bin/env python3
"""Rebuild the canonical nu2 sequence and derived S(n) with the CANONICAL
oracle (lib.nu2.fold_nu2 = s_sos, floored d in [2,n-1]).

NOTE: code/out/nu2_terms.txt disagrees with the canonical oracle at 53 (19 vs
18) and 64 (28 vs 27) — that file is NOT the canonical fold sequence and must
not be fed to the sequence tools. This script regenerates everything from
fold_nu2 + prime_h.

S(n) = (n-2) - 2*nu2(n) = sum_{d=2}^{n-1} (-1)^{T(n,d)}  (signed fold deviation)
"""
import sys, time
from fractions import Fraction
from lib.nu2 import fold_nu2
from lib.nu2_guard import prime_h, assert_supply_guard


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 4000
    assert_supply_guard(N)   # canonical guard: 53==18, 64==27, nu2(4000)==1975
    h = prime_h(N + 1)
    t0 = time.time()
    nu2 = {}
    for n in range(2, N + 1):
        nu2[n] = fold_nu2(n, h)
    print(f"fold_nu2 for n=2..{N} in {time.time()-t0:.1f}s")

    # spot checks
    for n, e in [(53, 18), (64, 27), (4000, 1975), (1000, 499)]:
        print(f"  nu2({n}) = {nu2.get(n)}  expect {e}")

    S = {n: (n - 2) - 2 * nu2[n] for n in nu2}

    with open('/tmp/nu2_canonical.txt', 'w') as f:
        for n in range(2, N + 1):
            f.write(f"{n} {nu2[n]}\n")
    with open('/tmp/S_canonical.txt', 'w') as f:
        for n in range(2, N + 1):
            f.write(f"{n} {S[n]}\n")

    # ---- structural stats ----
    print("\nnu2/n at checkpoints:  n  nu2/n  S")
    for n in [100, 500, 1000, 2000, 3000, 4000]:
        if n <= N:
            print(f"  {n}: {nu2[n]:4d}/{n} = {nu2[n]/n:.4f}   S={S[n]}")
    print("\nmax |S(n)|/sqrt(n) over [50,N]:")
    best = max(((abs(S[n]) / (n ** 0.5)), n) for n in range(50, N + 1))
    best2 = max(((abs(S[n]) / n), n) for n in range(50, N + 1))
    print(f"  max|S|/sqrt n = {best[0]:.3f} at n={best[1]}")
    print(f"  max|S|/n      = {best2[0]:.4f} at n={best2[1]}")
    # excess S as fraction of n stays bounded?
    print("\nCesaro mean of nu2/n and variance:")
    S1 = sum(Fraction(nu2[n], n) for n in range(2, N + 1))
    mu = S1 / N
    ex2 = sum(Fraction(nu2[n], n) ** 2 for n in range(2, N + 1)) / N
    print(f"  N={N}: mu={float(mu):.6f}  s2={float(ex2-mu*mu):.9f}")


if __name__ == "__main__":
    main()
