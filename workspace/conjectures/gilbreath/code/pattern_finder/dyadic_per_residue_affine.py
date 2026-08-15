#!/usr/bin/env python3
"""PATTERN-FINDER: per-residue-affine structure of nu2(n) for odd-period
tail-1 words — is nu2(n+P) - nu2(n) CONSTANT for each residue class n mod P?

Model: q_1=2, q_2=3, gap = 2 if bit else 4, bits = [0]*(P-1)+[1] (tail-1 word).
nu2(n) = #2s in maximal {0,2} suffix of right diagonal delta(q_n)
(lib.rightdiag.cycle_and_nu2, body convention).

If for every residue r mod P the increment c_r = nu2(n+P)-nu2(n) is exactly
constant over a long window with c_r >= 1, then
    nu2(n)  >=  (min_r c_r / P) * n - O(1),
a positive linear lower bound — the odd-factor converse (conjectured) made
exact-per-residue.  Report (c_r)_r, min c_r, implied slope, and any residue
with c_r = 0 (that would kill the uniform positive bound).

Exact integer arithmetic; O(N^2) diffs and O(N) memory per P (N=1400).
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


def per_residue_increments(vals, P, nmin, nmax):
    """For each residue r mod P, the set of diffs nu2(n+P)-nu2(n), n in
    [nmin, nmax-P] with n ≡ r mod P."""
    res = {}
    for r in range(P):
        diffs = set()
        for n in range(nmin, nmax - P + 1):
            if n % P == r:
                diffs.add(vals[n + P] - vals[n])
        res[r] = diffs
    return res


def main():
    N = 1400
    nmin = 300
    print("Per-residue-affine structure of true nu2(n) on odd-period tail-1 words")
    print(f"window n in [{nmin}, {N}]; checks nu2(n+P)-nu2(n) per residue mod P")
    print("=" * 76)
    for P in [3, 5, 7, 9, 11, 13, 15]:
        word = [0] * (P - 1) + [1]
        vals = nu2_seq(word, N)
        res = per_residue_increments(vals, P, nmin, N)
        constant = all(len(s) == 1 for s in res.values())
        cs = [next(iter(s)) if len(s) == 1 else None for s in res.values()]
        if not constant:
            print(f"P={P:2d} tail-1 word: NOT per-residue affine — nonconstant residues:")
            for r in range(P):
                if len(res[r]) > 1:
                    print(f"    r={r}: diffs in {sorted(res[r])[:6]}")
            continue
        minc = min(cs)
        slope = minc / P
        mean_c = sum(cs) / P
        mean_slope = mean_c / P
        print(f"P={P:2d}: c_r = {cs}")
        print(f"     min c_r = {minc}  ->  nu2(n) >= ({minc}/{P}) n - O(1) = "
              f"{slope:.4f} n - O(1); mean slope {mean_slope:.4f}")
        print(f"     positive lower density: {'YES' if minc >= 1 else 'NO (c_r=0 exists)'}")
    print()
    print("Reading: per-residue affine with all c_r >= 1 proves a uniform positive")
    print("linear lower bound for nu2 on that word -> the odd-factor converse holds")
    print("on the measured words with the above constants (computed, not yet proved).")


if __name__ == "__main__":
    main()