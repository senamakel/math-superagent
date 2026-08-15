#!/usr/bin/env python3
"""PATTERN-FINDER: which odd periods P have per-residue-affine nu2(n), and what
are the affine constants c_r (mod-P increments)?

Model: q_1=2, q_2=3, gap = 2 if bit else 4, bits = tail-1 word [0]*(P-1)+[1].
nu2(n) = #2s in maximal {0,2} suffix of right diagonal delta(q_n)
(lib.rightdiag.cycle_and_nu2, body convention).

nu2 per-residue affine  <=>  nu2(n+P)-nu2(n) = c_r (exact constant) for each
residue r mod P.  Report the set of such P in a range, the constants c_r, the
implied min slope, and the divisor pattern (Mersenne numbers 2^k-1, primes,
etc).  Exact integers; O(N^2) diffs, O(N) memory per P.
"""
import sys
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import incremental_diagonals, cycle_and_nu2


def build_seq(word, n_terms):
    q = [2, 3]
    per = len(word)
    while len(q) < n_terms:
        bit = word[(len(q) - 2) % per]
        q.append(q[-1] + (2 if bit else 4))
    return q[:n_terms]


def nu2_seq(word, nmax):
    q = build_seq(word, nmax + 1)
    out = {}
    for k, dd in enumerate(incremental_diagonals(q)):
        if k >= 2:
            out[k] = cycle_and_nu2(dd)[1]
    return out


def per_residue_affine(vals, P, nmin, nmax):
    """Return (True, c_r) if each residue's P-step increment is exactly constant."""
    cs = []
    for r in range(P):
        diffs = {vals[n + P] - vals[n] for n in range(nmin, nmax - P + 1)
                 if n % P == r}
        if len(diffs) != 1:
            return False, []
        cs.append(diffs.pop())
    return True, cs


def main():
    N = 1200
    nmin = 300
    Ps = [3, 5, 7, 9, 11, 13, 15, 17, 21, 23, 25, 27, 31, 33, 35, 39, 45]
    print("Odd periods P up to 45 (tail-1 word): per-residue-affine nu2?")
    print(f"window n in [{nmin},{N}]; affine iff nu2(n+P)-nu2(n) = c_r exactly per residue")
    print("=" * 78)
    for P in Ps:
        word = [0] * (P - 1) + [1]
        vals = nu2_seq(word, N)
        affine, cs = per_residue_affine(vals, P, nmin, N)
        if affine:
            minc = min(cs)
            print(f"P={P:2d}: AFFINE  c_r={cs}  min {minc}  slope {minc}/{P} = {minc/P:.4f}")
        else:
            print(f"P={P:2d}: not affine")
    print()
    print("Look for: which P are affine?  Divisor/Mersenne pattern?")


if __name__ == "__main__":
    main()