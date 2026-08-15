#!/usr/bin/env python3
"""PATTERN-FINDER: exact residue-class-affine structure of nu2(n) for
odd-period tail-1 words (the odd-factor family of the dyadic dichotomy).

Model (locked): q_1=2, q_2=3, gap = 2 if bit else 4, bits = word repeated,
word = [0]*(P-1)+[1] (one 1 at the tail).  nu2(n) = #2s in the maximal {0,2}
suffix of the right diagonal delta(q_n) (body convention,
lib.rightdiag.cycle_and_nu2).

Question: for which (L, S) does nu2(n+L) == nu2(n) + S hold EXACTLY for all n
in a long window?  If it holds, nu2 is exact-affine per residue class mod L
with slope S/L, and the odd-factor converse nu2 >= c*n holds with
c >= min-residue-slope > 0.

Exact integer arithmetic; O(N^2) diffs, O(N) memory per P.
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


def find_affine_period(vals, nmin, nmax, Lmax):
    """Find smallest L such that vals[n+L] == vals[n] + S for all n in
    [nmin, nmax-L].  Returns (L, S) or None."""
    # for each L, determine S from the first point, then check all
    for L in range(1, Lmax + 1):
        ok = True
        S = None
        for n in range(nmin, nmax - L + 1):
            d = vals[n + L] - vals[n]
            if S is None:
                S = d
            elif d != S:
                ok = False
                break
        if ok and S is not None:
            return L, S
    return None


def main():
    Ps = [3, 5, 7, 9, 11, 13, 15]
    N = 700
    print("Odd periods P, tail-1 word: exact afine-per-residue structure of nu2(n)")
    print("nu2(n) = #2s in maximal {0,2} suffix of right diagonal delta(q_n)")
    print("window n in [200, %d], searching L <= 60, S integer" % N)
    print("-" * 74)
    for P in Ps:
        word = [0] * (P - 1) + [1]
        vals = nu2_seq(word, N)
        res = find_affine_period(vals, 200, N, 60)
        if res is None:
            print(f"P={P:2d} word {''.join(map(str,word))}: NO affine period L<=60 found")
            continue
        L, S = res
        # verify per-residue slopes: is each n mod L exactly affine?
        slope = S / L
        # min and max per-residue intercept-normalized value
        last = N - 1
        resid = {}
        for n in range(200, last - L + 1):
            r = n % L
            # normalize: vals[n] - slope*n should be constant per residue
        # simpler: min slope estimate from per-residue first diffs over one L-block
        print(f"P={P:2d}: L={L:2d} S={S:2d} slope={slope:.6f} "
              f"(nu2(n+{L}) == nu2(n)+{S} exact over n in [200,{N-L}])")
        # min over n of (nu2(n) - slope*n) for the last L residues
        slopes = {}
        for r in range(L):
            ns = [n for n in range(300, N - L, L) if n % L == r]
            if ns:
                offs = [vals[n] - slope * n for n in ns]
                slopes[r] = (max(offs) - min(offs))
        maxj = max(slopes.values())
        print(f"      per-residue drift (max-min of nu2 - slope*n within residue, "
              f"should be ~0): {maxj:.3f}")
    print()
    print("Reading: L is the exact period of the residual; S/L the asymptotic slope.")


if __name__ == "__main__":
    main()