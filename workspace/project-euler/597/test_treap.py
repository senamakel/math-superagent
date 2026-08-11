#!/usr/bin/env python3
"""Deterministic test of the Cartesian-tree ("min-heap treap") hypothesis for
PE 597 parity.

Hypothesis under test:
  a_i = L - 40*(i-1)  (1-indexed) = L - 40*i (0-indexed), distance to finish.
  w_i = v_i / a_i.
  Build the Cartesian tree over indices with in-order = index order and
  min-heap priority w_i (root = smallest w; left/right subtrees = adjacent
  index ranges).
  Conjecture: a bump chain i -> ... -> j (i behind, j ahead) exists iff i and j
  are an ancestor/descendant pair in the tree. Then
      parity = (# index pairs {i,j} that are ancestor/descendant, with i<j) mod 2.

We compare this tree parity against the true oracle outcome_parity on many
random Exp(1) speed vectors, and Monte-Carlo the tree-model implied probability
against the given p(3,160)=56/135 and p(4,400)=0.5107843137.

Run:  python3 test_treap.py [trials_per_case]
"""
import sys, os, random
sys.path.insert(0, os.path.join(os.path.dirname(os.path.abspath(__file__)), "code"))
from toolkits.race_outcome import outcome_parity


def build_treap(n, w):
    """Return treap structure: for each node i, its left/right children set and
    parent; then compute ancestor/descendant pairs among indices.
    In-order = index order; min-heap priority w[i] (unique w assumed)."""
    # recursively find min-priority index over each range
    left = {}
    right = {}
    parent = {i: None for i in range(n)}

    def build(lo, hi, par):
        """Build treap on indices [lo, hi); return root index."""
        if lo >= hi:
            return None
        # root = index with MINIMUM w in [lo,hi)
        r = min(range(lo, hi), key=lambda i: w[i])
        parent[r] = par
        lchild = build(lo, r, r)
        rchild = build(r + 1, hi, r)
        left[r] = lchild
        right[r] = rchild
        return r

    root = build(0, n, None)
    return left, right, parent, root


def ancestor_descendant_pairs(n, left, right, parent, root):
    """Count pairs (i,j), i<j, where one is ancestor of the other."""
    anc = [set() for _ in range(n)]
    # do a pre-order, passing ancestor chain
    stack = [(root, frozenset())]
    while stack:
        u, chain = stack.pop()
        anc[u] = chain
        if left[u] is not None:
            stack.append((left[u], chain | {u}))
        if right[u] is not None:
            stack.append((right[u], chain | {u}))
    count = 0
    for i in range(n):
        for j in range(i + 1, n):
            if (j in anc[i]) or (i in anc[j]):
                count += 1
    return count % 2


def tree_parity(n, L, speeds):
    a = [L - 40.0 * i for i in range(n)]
    w = [speeds[i] / a[i] for i in range(n)]
    left, right, parent, root = build_treap(n, w)
    return ancestor_descendant_pairs(n, left, right, parent, root)


def run_deterministic(max_n, L_list, trials, seed=12345):
    rng = random.Random(seed)
    mismatches = []
    total = 0
    for n in range(2, max_n + 1):
        for L in L_list:
            for _ in range(trials):
                speeds = [rng.expovariate(1.0) for _ in range(n)]
                op = outcome_parity(n, L, speeds)
                tp = tree_parity(n, L, speeds)
                total += 1
                if op != tp:
                    mismatches.append((n, L, speeds, op, tp))
                    if len(mismatches) >= 30:
                        break
            if len(mismatches) >= 30:
                break
        if len(mismatches) >= 30:
            break
    return mismatches, total


def mc_tree(n, L, trials, seed=7):
    rng = random.Random(seed)
    even = 0
    for _ in range(trials):
        speeds = [rng.expovariate(1.0) for _ in range(n)]
        even += tree_parity(n, L, speeds) == 0
    return even / trials


def main():
    trials = int(sys.argv[1]) if len(sys.argv) > 1 else 20000
    mismatches, total = run_deterministic(6, [160.0, 400.0, 1800.0], trials)
    print(f"Deterministic test over n=2..6, L in (160,400,1800): {total} trials, "
          f"{len(mismatches)} mismatches")
    for (n, L, speeds, op, tp) in mismatches[:10]:
        print(f"  MISMATCH n={n} L={L} oracle={op} tree={tp}")
        print(f"    speeds={[round(s,5) for s in speeds]}")

    if mismatches:
        print("\nHYPOTHESIS FAILS. First 10 failing cases shown above.")
    else:
        print("\nHYPOTHESIS PASSES (0 mismatches across all trials).")

    # Monte-Carlo implied probability of the tree model vs given values
    print("\nTree-model MC estimates:")
    print(f"  p(3,160)  = {mc_tree(3, 160.0, trials, seed=101):.6f}  (given 56/135 = {56/135:.6f})")
    print(f"  p(4,400)  = {mc_tree(4, 400.0, trials, seed=102):.6f}  (given 0.5107843137)")
    print(f"  p(13,1800)= {mc_tree(13, 1800.0, trials, seed=103):.6f}  (empirical tree-model estimate)")


if __name__ == '__main__':
    main()
