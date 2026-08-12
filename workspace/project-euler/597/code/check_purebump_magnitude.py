#!/usr/bin/env python3
"""Two checks on the pure-bump (L->inf) limit:

(A) Does pure-bump parity depend ONLY on the speed ORDER, or on magnitudes too?
    The closed-form limits p3(inf)=7/18, p4(inf)=19/36 vs the order-count
    1/3, 13/24(=13/24... wait 13/24 even? p3 order-count = 2/6=1/3) disagree with
    large-L MC, which suggests parity depends on magnitudes even with no finish.
    Test: same strict ordering, two different magnitude vectors -> same parity?
    If not, order-count enumeration is invalid.

(B) Independent large-L MC of p(n,L) for n=3,4 against the exact limits
    7/18 and 19/36, using genuine Exp(1) speeds at L=10^9.

Pure-bump races here are run EXACTLY in rational arithmetic (no finish line),
so there is no approximation in the per-vector parity.
"""
import sys, os, random
from fractions import Fraction as F
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brute import outcome_parity


def pure_bump_parity(n, speeds):
    """Bump-only race (L=infinity) with rational exact speeds. Return parity."""
    state = [0]*n          # 0 rowing, 2 OUT (bumped)
    pos = [F(40)*j for j in range(n)]
    edges = [[] for _ in range(n)]
    while True:
        rowing = [j for j in range(n) if state[j] == 0]
        if not rowing:
            break
        best = None
        for j in rowing:
            k = None
            for kk in range(j+1, n):
                if state[kk] == 0:
                    k = kk; break
            if k is not None and speeds[j] > speeds[k]:
                ct = (pos[k]-pos[j])/(speeds[j]-speeds[k])
                if best is None or ct < best[0]:
                    best = (ct, j, k)
        if best is None:
            break
        _, j, k = best
        state[j] = 2
        pos[j] = pos[k]
        edges[j].append(k)
    above = [set() for _ in range(n)]
    for i in range(n):
        seen = {i}; stack = [i]
        while stack:
            u = stack.pop()
            for w in edges[u]:
                if w not in seen:
                    seen.add(w); stack.append(w)
        above[i] = seen - {i}
    # parity = number of chain pairs mod 2 = inversion count
    chain_pairs = sum(len(above[i]) for i in range(n))
    return chain_pairs % 2


def ordering_variants(n, order):
    """Two rational speed vectors with the SAME strict ordering `order`
    (speeds[order[0]] > speeds[order[1]] > ...) but very different magnitudes."""
    # variant 1: clumped (differences tiny)  -> near-ties
    vals1 = [n**2 - r for r in range(n)]          # decreasing, unit gaps
    v1 = [None]*n
    for r, boat in enumerate(order):
        v1[boat] = F(vals1[r])
    # variant 2: spread (huge gaps)          -> clear-cut
    vals2 = [10**(n - r) for r in range(n)]       # geometric spread
    v2 = [None]*n
    for r, boat in enumerate(order):
        v2[boat] = F(vals2[r])
    return v1, v2


def main():
    random.seed(11)
    # (A) magnitude dependence of pure-bump parity
    print("(A) pure-bump parity vs speed ORDER + magnitudes (no finish):")
    for n in (3, 4, 5):
        import itertools
        mismatch = 0
        total = 0
        example = None
        for order in itertools.permutations(range(n)):
            v1, v2 = ordering_variants(n, order)
            p1 = pure_bump_parity(n, v1)
            p2 = pure_bump_parity(n, v2)
            total += 1
            if p1 != p2:
                mismatch += 1
                if example is None:
                    example = (order, v1, p1, v2, p2)
        print(f"  n={n}: {mismatch}/{total} orderings change parity with magnitudes")

    # (B) exact limits agree with large-L MC
    print("\n(B) order-count even-probability vs true large-L limits:")
    for n, order_even_frac in ((3, F(2,6)), (4, F(13,24)), (5, F(67,120))):
        # order-equal weighting (pure_bump_limit's model)
        N = 2000000
        even = 0
        rng = random.Random(100+n)
        for _ in range(N):
            v = [rng.expovariate(1.0) for _ in range(n)]
            if outcome_parity(n, 10**9, v) == 0:
                even += 1
        mc = even/N
        se = (mc*(1-mc)/N) ** 0.5
        print(f"  n={n}: order-count model={float(order_even_frac):.6f}  "
              f"true MC(L=10^9)={mc:.6f} +/- {se:.6f}")


if __name__ == '__main__':
    main()
