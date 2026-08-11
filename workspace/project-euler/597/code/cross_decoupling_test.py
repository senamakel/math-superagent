#!/usr/bin/env python3
"""Decisive test of the research-library treap recursion claims for PE 597.

The library (CONTEXT.md / ROOT.md / L1.0 notes) claims:
  1. root r = argmin over range of W_i = v_i/(L-40i);
  2. the range parity obeys
        parity([a,b]) = parity([a,r-1]) * parity([r+1,b]) * (-1)^cross
     with cross = number of (i in left [a,r-1], j in right [r+1,b]) pairs
     whose relative order flips at the root;
  3. (implicitly) cross depends only on the root choice (decoupling), and
     cross = |left| * |right| is never stated but asked about.

Here we ask three concrete questions with the TRUE race dynamics (brute
oracle), using the true bump-chain flipped pairs as 'cross':

  Q1. Is cross (the number of left/right index pairs i<j with a bump chain
      i->...->j) ALWAYS equal to |left| * |right| ?  [claim in question]
  Q2. Does cross depend ONLY on which boat is the min-W root of the WHOLE
      range (i.e. is it constant across speed configurations sharing the
      same root)?  [decoupling claim]
  Q3. Does the parity recursion parity(left)*parity(right)*(-1)^cross with
      TRUE cross reproduce the oracle?  [this is a tautology/reorganization;
      reported to show that when cross is fed ground truth it trivially]
      matches, which is why the library's "recursion is validated" wording
      is about ground-truth cross, not about predicting cross from the root.

The decisive claims are Q1 and Q2: if either fails, the "sum-of-products over
the treap tree is the parity of the FINAL permutation with cross=|L|*|R|"
claim is false.
"""
import sys, os, random
from collections import defaultdict
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from brute import simulate_order, outcome_parity


def W(args, L, i):
    return args[i] / (L - 40.0 * i)


def min_w_root(args, L, a, b):
    best = a
    for r in range(a + 1, b + 1):
        if W(args, L, r) < W(args, L, best):
            best = r
    return best


def true_cross_and_parity(n, L, speeds):
    """Return (root, true_flipped_leftright_pairs_cross, parity)."""
    above = simulate_order(n, L, speeds)
    r = min_w_root(speeds, L, 0, n - 1)
    # truthful chain-pairs: (i,j) with i<j and j reachable from i via bumps
    cross = 0
    for i in range(r):
        for j in range(r + 1, n):
            if j in above[i]:
                cross += 1
    return r, cross, outcome_parity(n, L, speeds)


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 200000
    rng = random.Random(1234)
    configs = [(3, 160.0), (4, 160.0), (4, 400.0), (5, 400.0), (5, 1800.0)]
    for (n, L) in configs:
        q1_bad = 0      # cross != |left|*|right|
        q1_nontrivial = 0
        q2_seen = defaultdict(set)   # root -> set of cross values seen
        q2_bad = 0
        q3_bad = 0
        cross_hist = defaultdict(int)
        for _ in range(N):
            speeds = [rng.expovariate(1.0) for _ in range(n)]
            root, cross, par = true_cross_and_parity(n, L, speeds)
            left = root
            right = n - 1 - root
            if -1 < root < n - 1:
                q1_nontrivial += 1
                if cross != left * right:
                    q1_bad += 1
            cross_hist[cross] += 1
            q2_seen[root].add(cross)
            # recursion parity with true cross
            rec = 0
            # left/right range parities recursively (true oracle), x sign
            # left range [0,root-1], right [root+1,n-1]
            if left >= 2:
                pl = parity_of_range(root - 1, L, speeds)
            else:
                pl = 0
            if right >= 2:
                pr = parity_of_range(root + 1, L, speeds)
            else:
                pr = 0
            rec = (pl + pr + cross) % 2
            if rec != par:
                q3_bad += 1
        print(f"n={n} L={L}:")
        print(f"  Q1 cross==|L|*|R| fails in {q1_bad}/{q1_nontrivial} "
              f"non-leaf-root cases  (cross histogram: {dict(sorted(cross_hist.items()))})")
        multi = {k: v for k, v in q2_seen.items() if len(v) > 1}
        print(f"  Q2 cross depends on root alone (decoupling): FAIL for roots "
              f"{multi}  (roots with >1 cross value: {len(multi)})")
        print(f"  Q3 recursion with TRUE cross matches oracle: "
              f"{'yes' if q3_bad == 0 else str(q3_bad) + ' mismatches'} "
              f"(tautological; cross fed ground truth)")


def parity_of_range(b, L, speeds):
    """True oracle parity of the sub-race on boats 0..b (same geometry)."""
    from brute import outcome_parity
    return outcome_parity(b + 1, L, speeds[:b + 1])


if __name__ == '__main__':
    main()
