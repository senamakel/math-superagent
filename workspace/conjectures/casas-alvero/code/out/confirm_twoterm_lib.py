"""Independent confirmation of the two-term subset-sum law for F2 Hasse-CA.

Uses lib.casas_alvero.is_ca_hasse / is_pure_power (sympy, a different
implementation from the bit-parallel is_ca_f2 of extend_p2_multiplier /
parallel_p2_counts).  Verifies: x^a + x^n is a Hasse-CA counterexample over
F2 iff a is a proper nonempty subset-sum of the binary set-bits of n.
"""
import sys
from math import comb
from sympy import symbols, Poly, GF
from itertools import combinations
from lib.casas_alvero import is_ca_hasse, is_pure_power

x = symbols("x")


def subset_sums(n):
    B = [1 << i for i in range(n.bit_length()) if (n >> i) & 1]
    sums = set()
    for k in range(1, len(B)):
        for c in combinations(B, k):
            sums.add(sum(c))
    return sums


def main(ns):
    ok = True
    for n in ns:
        cand = subset_sums(n)
        for a in range(0, n + 1):
            f = Poly(x**n + x**a, x, domain=GF(2))
            is_ce = is_ca_hasse(f, 2) and not is_pure_power(f, 2)
            expect = (a in cand)
            if is_ce != expect:
                print(f"BREAK n={n} a={a}: subset-sum={a in cand} "
                      f"lib-counterexample={is_ce}")
                ok = False
        print(f"n={n}: all {n+1} a-values match the subset-sum law")
    print("INDEPENDENT CONFIRMATION:", "PASS (lib route)" if ok else "FAIL")


if __name__ == "__main__":
    main([int(s) for s in sys.argv[1:]] or [16, 18, 20, 24, 25, 30])
