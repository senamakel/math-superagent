"""s-sharing distribution (closed form) of the non-matching pairs of
K(k)-minus-a-perfect-matching, plus the s-determinism check on the two controls.

For a non-matching pair p={a,b} (b != mate(a)) in a k-set with perfect matching:
  pairs sharing exactly 1 element (containing a xor b, != p, non-matching):
      containing a: (k-1) - 1[matching edge {a,mate(a)}] - 0  = k-2 pairs total
                   with {a,*} among which p itself is {a,b} => k-3  (and the
                   matching edge {a,mate(a)} already excluded => k-2-1=k-3)
      same for b: k-3
      s=1 per-pair total = 2(k-3)
  pairs sharing 2 elements: only p itself.
  pairs sharing 0: M - 1 - 2(k-3),  M = C(k,2) - k/2.
Over all M non-matching pairs, each unordered pair counted twice, so global
  unordered-pair counts: s=1 => M*2(k-3)/2 = M(k-3);  s=0 => M*(M-1-2(k-3))/2.
"""
import itertools
import numpy as np
from math import comb
from lib.srg import is_srg, rook, bvls_graph


def s_global(k):
    M = comb(k, 2) - k // 2
    s1 = M * (k - 3)
    s0 = M * (M - 1 - 2 * (k - 3)) // 2
    return M, {0: s0, 1: s1}


def s_determined(A, zero):
    A = np.asarray(A, dtype=np.int64)
    n = A.shape[0]
    k = int(A[zero].sum())
    N = [i for i in range(n) if A[zero, i] == 1]
    matching, remaining = [], set(N)
    while remaining:
        a = min(remaining)
        remaining.discard(a)
        b = [c for c in N if c != a and A[a, c] == 1]
        b = b[0]
        remaining.discard(b)
        matching.append(frozenset((a, b)))
    outer = [i for i in range(n) if i != zero and A[zero, i] == 0]
    pair = {u: frozenset(x for x in N if A[u, x] == 1) for u in outer}
    by_s = {0: set(), 1: set()}
    for u, w in itertools.combinations(outer, 2):
        s = len(pair[u] & pair[w])
        by_s[s].add(int(A[u, w]))
    return {s: (len(v), sorted(v)) for s, v in by_s.items()}, k


if __name__ == "__main__":
    print("Closed-form s-sharing of non-matching pairs of K(k)-minus-matching:")
    for k in (4, 14, 22, 112, 994):
        M, per = s_global(k)
        print(f"  k={k}: M={M} non-matching pairs; unordered pair-pairs by s: "
              f"s=0:{per[0]}, s=1:{per[1]}, total={per[0]+per[1]} "
              f"(= {M*(M-1)//2} check: {per[0]+per[1]==M*(M-1)//2})")
    print()
    for name, A, v, k, lam, mu in [("rook", rook(3), 9, 4, 1, 2),
                                   ("bvls", bvls_graph(), 243, 22, 1, 2)]:
        ok, _ = is_srg(A, v, k, lam, mu)
        assert ok
        for fixed in (0, 1, A.shape[0] // 2, A.shape[0] - 1):
            det, kk = s_determined(A, fixed)
            pure = all(len(vals) == 1 for _, vals in det.values())
            print(f"[{name}] root {fixed}: k={kk} s-determinism {det} -> "
                  f"{'PURE (outer adjacency is a function of s)' if pure else 'NOT s-determined (real freedom)'}")
