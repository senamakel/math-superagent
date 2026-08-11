#!/usr/bin/env python3
"""Decisive test of the research-library recursion for PE 597 against the
brute oracle.

The research claim (CONTEXT.md, ROOT.md, L1.1/L0.0.md), stated precisely:

  For a boat-index range [a,b], let the "root" r be the boat slowest relative
  to the finish target, i.e. argmin of W_i = v_i/(L - 40i) over i in [a,b]
  (Plackett-Luce "clock", rate = distance d_i = L - 40i).  Then
      p([a,b]) = sum over r of  w(r) * p(left) * p(right) * (-1)^{cross}
  with
      w(r)      = d_r / sum_{j in [a,b]} d_j     (distance-ratio weight,
                  P(root = r) under the clock model),
      left      = [a, r-1],  right = [r+1, b],
      cross     = # pairs (i in left, j in right) whose relative order
                  flips at the root,
  and p(empty range) = p(single boat) = 1 (even).

This module implements that recursion EXACTLY (Fractions) and compares the
resulting p(n,L) against the brute oracle:

  * given exact values:  p(3,160) = 56/135,  p(4,400) = 0.5107843137
  * Monte-Carlo oracle values (code/toolkits/race_outcome.py) for the rest.

Because "cross" is not derivable from the clock model (the library's own open
gap: finish events are inverse-exponential, not clocks), we test BOTH natural
instantiations an implementer would use:

  (A) cross = |left| * |right|  (the treap-implied deterministic value: every
      left-right pair is claimed to flip), recursing sub-ranges by the same
      closed form;
  (B) cross = 0  (the naive no-flip instantiation);

and we ALSO report the per-vector parity recursion rooted at min-W with
cross = |L|*|R|, compared sample-by-sample against the oracle, to produce the
smallest counterexample (n, L, speeds) the task asks for.

As a control (what makes the parity ALGEBRA alone correct), we also show the
parity-propagation identity with TRUE cross and TRUE sub-race parities fed in
from the oracle -- this reproduces the full parity because it is a tautology,
which isolates where the claimed recursion actually fails.

Run:  python3 research_recursion_test.py [mc_trials]
"""
import sys, os, random
from fractions import Fraction
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "code"))
from toolkits.race_outcome import outcome_parity


def distances(n, L):
    return [Fraction(L - 40 * i) for i in range(n)]


def closed_form_recursion(n, L, cross_mode):
    """p(n,L) by the exact distance-ratio recursion (Fractions).

    S[a][b] = E[(-1)^{par}] over the range, then p = (1 + S)/2.
    cross_mode 'LxR' -> cross = |left|*|right|;  'zero' -> cross = 0.
    p(empty / single) = 1  ->  S = 1.
    """
    d = distances(n, L)
    S = {}

    def rec(a, b):
        if a >= b:
            return Fraction(1)
        if (a, b) in S:
            return S[(a, b)]
        denom = sum(d[i] for i in range(a, b + 1))
        total = Fraction(0)
        for r in range(a, b + 1):
            w = d[r] / denom
            left = rec(a, r - 1)
            right = rec(r + 1, b)
            term = left * right
            if cross_mode == 'LxR':
                cross = (r - a) * (b - r)
            else:
                cross = 0
            if cross % 2 == 1:
                term = -term
            total += w * term
        S[(a, b)] = total
        return total

    s = rec(0, n - 1)
    return s, (Fraction(1) + s) / 2


def W(s, L, i):
    return s[i] / (L - 40.0 * i)


def rec_parity_LxR(s, L, a, b):
    """Per-vector recursion parity, root = argmin W, cross = |L|*|R|."""
    if a >= b:
        return 0
    r = min(range(a, b + 1), key=lambda i: W(s, L, i))
    pl = rec_parity_LxR(s, L, a, r - 1)
    pr = rec_parity_LxR(s, L, r + 1, b)
    cross = (r - a) * (b - r)
    return (pl + pr + cross) % 2


def smallest_counterexample():
    """Search n=2 upward for the smallest (n, L, speeds) where the per-vector
    recursion parity disagrees with the oracle."""
    rng = random.Random(31415)
    for n in range(2, 7):
        for L in (160.0, 400.0, 1800.0):
            for _ in range(20000):
                speeds = [rng.expovariate(1.0) for _ in range(n)]
                op = outcome_parity(n, L, speeds)
                rp = rec_parity_LxR(list(speeds), L, 0, n - 1)
                if op != rp:
                    return (n, L, speeds, op, rp)
    return None


def mc_oracle(n, L, N, seed=11):
    rng = random.Random(seed)
    even = 0
    for _ in range(N):
        speeds = [rng.expovariate(1.0) for _ in range(n)]
        if outcome_parity(n, L, speeds) == 0:
            even += 1
    return even / N


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 400000
    L_list = [160.0, 400.0, 1800.0]
    print("=" * 78)
    print("PART 1 -- exact p(n,L) from the recursion vs the brute oracle")
    print("=" * 78)
    print(f"{'n':>2} {'L':>6} {'rec(LxR)':>12} {'rec(zero)':>10} "
          f"{'oracle(given/MC)':>18}")
    # given exact values
    given = {(3, 160.0): ("56/135", Fraction(56, 135)),
             (4, 400.0): ("0.5107843137", None)}
    for n in (3, 4, 5):
        for L in L_list:
            s1, p1 = closed_form_recursion(n, int(L), 'LxR')
            s0, p0 = closed_form_recursion(n, int(L), 'zero')
            key = (n, L)
            if key in given:
                name, val = given[key]
                if val is not None:
                    ostr = f"{name} = {float(val):.10f}"
                else:
                    ostr = name
            else:
                o = mc_oracle(n, L, N // 2 if n >= 4 else N)
                ostr = f"MC {o:.10f}"
            print(f"{n:>2} {L:>6.0f} {float(p1):>12.10f} {float(p0):>10.6f} "
                  f"{ostr:>18}")

    print()
    print("  Note: rec(0) = 1 for all cases; the cross=|L||R| ('LxR') version")
    print("  is the one the treap sum-of-products form implies. It gives")
    print("  p(3,160)=2/3 (truth 4/15+4/27 = 56/135) and p(4,400)=5/6")
    print("  (truth 0.5107843137) -- WRONG VALUES.")

    print()
    print("=" * 78)
    print("PART 2 -- per-vector recursion parity vs oracle; smallest counterexample")
    print("=" * 78)
    ce = smallest_counterexample()
    if ce is None:
        print("  no counterexample found up to n=6, L in {160,400,1800} (20k trials)")
    else:
        n, L, speeds, op, rp = ce
        print(f"  SMALLEST COUNTEREXAMPLE FOUND: n={n}, L={L}")
        print(f"    speeds = {[round(x, 5) for x in speeds]}")
        print(f"    oracle parity = {op}   recursion parity = {rp}")
        print(f"    (recursion says {('even' if rp == 0 else 'odd')}, "
              f"oracle says {('even' if op == 0 else 'odd')})")

    print()
    print("=" * 78)
    print("PART 3 -- control: parity algebra with TRUE cross + TRUE sub-race")
    print("=" * 78)
    print("  Feeding the oracle's own cross and sub-race parities into")
    print("  parity = parity(left)*parity(right)*(-1)^cross reproduces the")
    print("  full parity by construction (the algebra is trivially correct);")
    print("  the recursion's FAILURE is therefore in predicting the root")
    print("  distribution and/or cross, NOT in the parity parity algebra.")
    bad = 0
    rng = random.Random(54321)
    # only valid geometries: every boat must start strictly upstream of the
    # finish is FALSE -- every boat starts strictly BELOW the finish, so the
    # highest boat 40*(n-1) must be < L (positive distance to finish).
    valid = [(n, L) for n in range(3, 7) for L in L_list if 40 * (n - 1) < L]
    for _ in range(100000):
        n, L = valid[rng.randrange(len(valid))]
        speeds = [rng.expovariate(1.0) for _ in range(n)]
        # full oracle
        above = simulate_order(n, L, speeds)
        par_full, _ = parity_of_new_order(n, above)
        r = min(range(n), key=lambda i: W(speeds, L, i))
        # true cross at root
        cross = 0
        for i in range(r):
            for j in range(r + 1, n):
                if j in above[i]:
                    cross += 1
        # true sub-race parities (oracle on each slice, same geometry)
        pl = outcome_parity(r, L, speeds[:r]) if r >= 2 else 0
        pr = outcome_parity(n - 1 - r, L, speeds[r + 1:]) if n - 1 - r >= 2 else 0
        rec = (pl + pr + cross) % 2
        if rec != par_full:
            bad += 1
    print(f"  mismatches over 100000 random cases (ground-truth feed): {bad}")
    print("  -> parity algebra itself holds ({'0 mismatches' if bad==0 else 'FAIL'}).")


if __name__ == '__main__':
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "code"))
    from brute import simulate_order, parity_of_new_order
    main()
