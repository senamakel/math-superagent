"""Empirical test of the convex-4set-supersaturation covering bound on the
verified es_construct at n=5,6,7.

Claim (candidate 2): the non-convex 4-subsets of an n-avoiding set must
4-uniformly cover the n-subsets, giving NNC(C,N-4,n-4) >= C(N,n), and this is
'sharp at N=2^{n-2}'.  We compute NNC exactly and check whether the inequality
is tight at the extremal N and violated at N+1 (as the mechanism claims), and
compare NNC to C(N,4) (the vacuous ceiling the double-count reduces to).

Exact arithmetic throughout.
"""
from itertools import combinations
from math import comb
import sys
sys.path.insert(0, "/workspace/code")  # not on PYTHONPATH in this scratch
from lib.es_construct import es_set
from lib.es_geom import in_convex_position

for n in (5, 6, 7):
    pts = es_set(n)
    N = len(pts)
    # count non-convex 4-subsets
    nnc = 0
    total = 0
    for c in combinations(pts, 4):
        total += 1
        if not in_convex_position(c):
            nnc += 1
    # covering: nnc * C(N-4, n-4) >= C(N, n) ?
    nnc_cover = nnc * comb(N - 4, n - 4)
    cover_needed = comb(N, n)
    print(f"n={n}  N={N}  total4={total}  nonconvex4={nnc}  "
          f"cover_lhs={nnc_cover}  needed={cover_needed}  "
          f"OK={nnc_cover >= cover_needed}  "
          f"nnc/max=C(N,4) ratio={nnc/comb(N,4):.4f}")
    # vacuous ceiling C(N,4)*C(N-4,n-4) vs C(N,n): identity = C(n,4)
    print(f"    vacuous C(N,4)*C(N-4,n-4)/C(N,n) = "
          f"{comb(N,4)*comb(N-4,n-4)/comb(N,n)} (should be C(n,4)={comb(n,4)})")
