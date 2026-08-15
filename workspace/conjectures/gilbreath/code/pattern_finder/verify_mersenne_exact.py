#!/usr/bin/env python3
"""Independent exact verification of the Mersenne-period nu2 affine structure.

Tail-1 word of odd period P=2^k-1 drives a 2-then-odds sequence q_1=2, q_2=3,
gap = 2 if bit else 4.  nu2(n) = #2s in the maximal {0,2} suffix of the right
diagonal through q_n (body convention, index >= 2).

This recomputes nu2(n) for a window and checks:
  (1) per-residue affinity mod P: nu2(n+P)-nu2(n) = c_{n mod P} (constant)
  (2) sum_r c_r = 3^k - 3
  (3) the DENSITY interpretation: what is lim nu2(n)/n exactly?
      -- this is the subtle point: if per-residue slope c_r/P differs across
         residues, the global slope is NOT c_r/P.  We measure it directly.
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

def nu2_map(word, nmax):
    q = build_seq(word, nmax + 1)
    out = {}
    for k, dd in enumerate(incremental_diagonals(q)):
        if k >= 2:
            out[k] = cycle_and_nu2(dd)[1]
    return out

def check(k, windowsize=14):
    P = 2**k - 1
    N = P * (windowsize + 4) + 100
    nmin = P * 2 + 100
    vals = nu2_map([0]*(P-1)+[1], N)
    # per-residue increment
    cr = {}
    ok = True
    for r in range(P):
        diffs = {vals[n+P]-vals[n] for n in range(nmin, N-P) if n % P == r}
        if len(diffs) != 1:
            ok = False
            cr[r] = None
        else:
            cr[r] = diffs.pop()
    S = sum(c for c in cr.values() if c is not None)
    target = 3**k - 3
    # direct density over a large window
    import statistics
    nA = P*(windowsize) + 100
    nB = N - 20
    ratio = (vals[nB] - vals[nA]) / (nB - nA) if (nB-nA) else 0
    from fractions import Fraction
    fslope = Fraction(S, P*P)   # claimed density (sum cr)/P^2
    return dict(k=k, P=P, affine=ok, S=S, target=target,
                match=(S==target), cmin=min(cr.values()) if ok else None,
                direct_ratio=ratio, claimed_slope=fslope,
                frac=float(fslope))

def main():
    print("Mersenne P=2^k-1: verify per-residue affine nu2, sum c_r = 3^k-3, density")
    print("="*78)
    for k in range(2, 9):
        r = check(k)
        print("P=%4d (2^%d-1)  affine=%s  sum_c_r=%d  target 3^k-3=%d  match=%s"
              % (r['P'], k, r['affine'], r['S'], r['target'], r['match']))
        print("     min c_r=%s  direct ratio d(nu2)/dn over big window=%.6f"
              "  claimed slope (sum c_r)/P^2=%s (%.6f)"
              % (r['cmin'], r['direct_ratio'], r['claimed_slope'], r['frac']))

if __name__ == "__main__":
    main()
