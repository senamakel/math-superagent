#!/usr/bin/env python3
"""Sparse-input amplification of the SUPPLY fold Phi_n.

Central hypothesis (GOAL.md): can the fold Phi do work the switch-density form
cannot see?  Concretely the rival gaps share one finite computation:

  * G-eq-sparse-fold-is-sublinear:   sparse h (few 1s) must fold to sublinear
                                     weight wt(Phi_n h) = o(n).
  * G-weak-input-strictness:         some sparse h has wt(Phi_n h) >= c*n.

The single structural question both decide is the *capacity curve*:

    Cap(n, k) = max { wt(Phi_n h) : wt(h) = k }        (exact, brute force)

over all k-sparse length-n binary strings.  Exactly computing Cap for small n is
the oracle for the two rivals.

wt(Phi_n h) = #{ d in [2, n-1] : T(n,d) = 1 },  T(n,d) = XOR_{o subseteq d} h[n-1-d+o]
(problem.md facts 1-2), computed here two ways:
  * lib.supply_fold.s_sos   (O(n log n) submask-product SOS transform), and
  * the direct literal submask oracle t_direct (O(n * 2^popcount)), checked
    equal on every row so the count is not a float and not a single path.
All arithmetic exact; no float enters a judgment.
"""

from itertools import combinations
from lib.supply_fold import s_sos, t_direct


def _fold_weight(n, h):
    """wt(Phi_n h) with the + and the brute oracle cross-checked per row."""
    S, ones = s_sos(n, h)
    ones_direct = sum(t_direct(n, d, h) for d in range(2, n))
    assert ones == ones_direct, (n, ones, ones_direct)
    return ones


def _weight(h):
    return sum(h)


def max_weight_k_sparse(n, k):
    """Cap(n,k) = max wt(Phi_n h) over the C(n,k) strings with exactly k ones.
    Brute force over all index-subsets (legitimate oracle, small n).
    Returns (cap, argmax_index_list).  cap = -1 if no such h."""
    best = -1
    best_arg = None
    for idx in combinations(range(n), k):
        h = [0] * n
        for i in idx:
            h[i] = 1
        w = _fold_weight(n, h)
        if w > best:
            best = w
            best_arg = list(idx)
    return best, best_arg


def capacity_curve(n):
    """Exact Cap(n,k) for k = 0..n, plus argmax positions and the maximum over
    k <= n/2 (the sparse half).  Exact, brute force over C(n,k) per k."""
    out = []
    for k in range(0, n + 1):
        cap, arg = max_weight_k_sparse(n, k)
        out.append((k, cap, arg))
    return out


def position_analysis(n):
    """Where does the best k=1 string sit, as a function of position j?
    wt(Phi_n e_j) for every single j.  Exact; shows the boundary-spike mechanism
    (j near n-1 gives ~n weight) vs the interior (j fixed gives O(j))."""
    return [(_fold_weight(n, [1 if i == j else 0 for i in range(n)]), j)
            for j in range(n)]


def fixed_sparse_family(n_lo, n_hi, positions):
    """For a FIXED set of 1-positions (the same indices for every n >= their
    max, i.e. a fixed prefix-sparse string), report wt(Phi_n h)/n as n grows.
    If the ratio decays to 0 the fixed-sparse family fails to give linear
    weight (the refuter's fixed-1 bound generalized); if a fixed family keeps
    a linear ratio, that IS a G-weak-input-strictness witness.
    positions is an int or a list of ints (the fixed 1-indices)."""
    rows = []
    for n in range(n_lo, n_hi + 1):
        idx = positions if isinstance(positions, list) else [positions]
        h = [0] * n
        bad = False
        for i in idx:
            if i >= n:
                continue           # window too short to reach this index
            h[i] = 1
        w = _fold_weight(n, h)
        rows.append((n, w, w / n))
    return rows
