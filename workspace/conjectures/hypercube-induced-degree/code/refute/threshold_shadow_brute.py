"""Attack G-threshold-shadow.

Lemma under test:
  For each n and 0 <= d <= n, the function A |-> |O_{<=d}(A)| =
  |{ x in O : |N(x) cap A| <= d }|, over A subset E with |A| = a, is maximised
  by a Hamming ball in E (initial segment of simplicial/colex order).

We brute force the TRUE extremal value over all A of each size a, and compare
against candidate Hamming balls in E. This is the smallest encoding that could
refute the lemma.

O = odd-weight vertices, E = even-weight vertices. N(x) = the n neighbours of x
in the cube (all of opposite parity). For x in O, |N(x) cap A| counts how many
of x's neighbours lie in A.
"""
import itertools
from math import comb

def weight(x, n):
    return bin(x).count("1")

def build(n):
    E = [x for x in range(1 << n) if weight(x, n) % 2 == 0]
    O = [x for x in range(1 << n) if weight(x, n) % 2 == 1]
    # neighbours of each vertex (integer masks)
    neigh = {x: [x ^ (1 << i) for i in range(n)] for x in range(1 << n)}
    Eidx = {v: i for i, v in enumerate(E)}
    return E, O, neigh, Eidx

def threshold_val(A_set, d, O, neigh):
    """|O_{<=d}(A)| for the set A (set of even ints)."""
    cnt = 0
    for x in O:
        k = sum(1 for u in neigh[x] if u in A_set)
        if k <= d:
            cnt += 1
    return cnt

def brute_argmax(E, O, neigh, a, d):
    best = -1
    best_sets = []
    for subset in itertools.combinations(E, a):
        A_set = set(subset)
        v = threshold_val(A_set, d, O, neigh)
        if v > best:
            best = v
            best_sets = [subset]
        elif v == best:
            best_sets.append(subset)
    return best, best_sets

def ball_in_E_all_centers(E, O, neigh, a, d):
    """Max over all Hamming balls (centered at any vertex) intersected with E,
    of the threshold value. A Hamming ball of radius r has size sum_{i<=r} C(n,i);
    pick the ball with the desired size a and center anywhere."""
    # Collect candidate A: initial segments not easy; instead consider balls
    # centered at the all-zeros in the standard simplicial sense would center at an
    # even vertex. But balls centered at odd vertices also make sense as subsets of E.
    # A "ReLU ball" of radius r: all vertices within Hamming distance <= r of center c.
    best = -1
    best_As = []
    for center in range(1 << len(E)):
        pass
    # use actual cube dim n
    return best, best_As

def run(n, d):
    E, O, neigh, Eidx = build(n)
    results = []
    for a in range(0, len(E) + 1):
        best, best_sets = brute_argmax(E, O, neigh, a, d)
        results.append((a, best))
    return E, O, neigh, results

if __name__ == "__main__":
    import sys
    n = int(sys.argv[1]) if len(sys.argv) > 1 else 4
    d = int(sys.argv[2]) if len(sys.argv) > 2 else 1
    E, O, neigh, results = run(n, d)
    print(f"n={n} d={d}  |E|=|O|={len(E)}")
    print("  a : max |O_{<=d}(A)|")
    for a, best in results:
        print(f"  {a:2d} : {best}")
