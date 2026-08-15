#!/usr/bin/env python3
"""Scholar attack on the contradiction between two on-disk claims:

  rule90-periodic-window-collapse : "if h is periodic with period p, then every
    {0,2}-tail cell is an XOR-fold of a bounded window of h ... hence the
    {0,2}-suffix length and nu2 are O_p(1)"

versus the run's own exact dyadic-periodicity data (P=3 gives nu2=2666 at
n=4000, P=5 gives 2132, P=7 gives 2284 -- clearly NOT O(1)).

We rebuild the right-diagonal fold formula directly from first principles to
find which statement is correct and for which periods. We use the canonical
cycle_and_nu2 convention (maximal {0,2} suffix of the diagonal before the
terminal entry).

Right diagonal: through q_n (1-indexed), delta_k(q_n) = A_k[n-k].
Halved fold law (rule90-interior-xor, proved): the halved {0,2}-tail cell at
depth k is
    delta_k(q_n)/2 = XOR_{m=0}^{k-1} [binom(k-1,m) mod 2] * h[n-k+m]
where h[j] = (gap_j/2) mod 2 over the fixed ancestor interval, gap_2..gap_{n-1}.
Window of length k spanning columns n-k .. n-1 of h, Pascal row (k-1) coeffs.

We verify this fold formula against a literal |a-b| triangle for small cases,
then measure nu2(n) for periodic h of periods p with both a power-of-2 word and
an odd-factor word, at growing n, to see empirically whether O(1) or linear.
"""
import sys
from math import comb
sys.path.insert(0, '/workspace/code')
from lib.rightdiag import cycle_and_nu2


def gap_bits_generic(gaps):
    """h[j] = (gaps[j]//2) mod 2 for the gap sequence gaps[0..] = gap_2,..."""
    return [((g // 2) % 2) for g in gaps]


def build_2thenodds(period_word, n_terms):
    """Build the first n_terms gaps (gap_2..), periodic in the bit pattern:
    the gaps themselves are 2 (bit 0) or 4 (bit 1), bit j = word[j % p].
    The sequence q: q_1=2, q_2=3, q_{k+1}=q_k+gap_k for k>=2.
    Returns (q_list) 0-indexed."""
    p = len(period_word)
    gaps = [2 if period_word[j % p] == 0 else 4 for j in range(n_terms)]
    q = [2, 3]
    for g in gaps:
        q.append(q[-1] + g)
    return q


def delta_diag(q):
    """Literal right diagonal via |a-b| recurrence. q 0-indexed (q[0]=q_1)."""
    D = [q[0]]
    diags = [list(D)]
    for n in range(1, len(q)):
        nd = [0] * (n + 1)
        nd[0] = q[n]
        for k in range(1, n + 1):
            nd[k] = abs(nd[k - 1] - D[k - 1])
        D = nd
        diags.append(list(D))
    return diags


def fold_formula_check():
    """Verify the halved fold formula against literal |a-b| triangle for
    random periodic bit words, small n. Returns True if all match."""
    import random
    random.seed(1)
    for trial in range(300):
        p = random.randint(1, 8)
        word = [random.randint(0, 1) for _ in range(p)]
        n_terms = random.randint(6, 30)
        q = build_2thenodds(word, n_terms)
        diags = delta_diag(q)
        # halved gaps
        gaps = [q[i+1]-q[i] for i in range(1, len(q)-1)]  # gap_2..  (idx1->2)
        # actual gaps: q[1]-q[0]=3-2=1 is gap_1, ignore; gap_2 = q[2]-q[1]
        gg = [q[i+1]-q[i] for i in range(1, len(q)-1)]
        h = gap_bits_generic(gg)
        # check fold formula for each diagonal n and depth k in tail region
        for n in range(2, len(q)):
            diag = diags[n]
            for k in range(2, n):  # tail-ish cells
                # window h[n-k .. n-1], need n-k >= index of gap_2 in h
                # h indexed by j = gap index; gap_j corresponds to q_j->q_{j+1}
                # Our h list[0] = gap_2 bit. The fold uses columns j in [n-k,n-1].
                # We need h index = j-2 (since gap_2 is j=2 -> h[0]).
                win_start = n - k
                win_end = n - 1
                if win_start - 2 < 0:
                    continue
                val = 0
                for m in range(k):
                    if comb(k-1, m) % 2 == 1:
                        col = win_start + m
                        bit = h[col - 2]
                        val ^= bit
                # halved diag cell value
                dv = diag[k]
                # in {0,2}: cell should be 2*val if val in {0,1} and diag even
                if dv % 2 == 0 and (dv // 2) != val:
                    return False, (trial, n, k, dv, val)
    return True, None


def nu2_for_period(word, n_vals):
    """Return list of nu2(n) using canonical cycle_and_nu2."""
    out = []
    for n in n_vals:
        q = build_2thenodds(word, n)  # n gaps => q has n+2 entries, q_n at index n+1
        diags = delta_diag(q)
        diag = diags[-1]  # delta(q_n) with q_n = q[n+1]? careful with indexing
        tau, nu2 = cycle_and_nu2(diag)
        out.append(nu2)
    return out


def main():
    print("=== Step 1: verify fold formula vs literal triangle ===")
    ok, info = fold_formula_check()
    print("fold formula matches literal |a-b| triangle: %r %s" % (ok, info))

    print()
    print("=== Step 2: nu2 growth for periodic words, canonical convention ===")
    n_vals = [100, 500, 1000, 3000, 6000]
    tests = [
        ("P=1 tail1", [1]),
        ("P=2 alt", [0, 1]),
        ("P=3 tail1", [0, 0, 1]),
        ("P=4 alt(word 01)*2", [0, 1, 0, 1]),
        ("P=5 tail1", [0, 0, 0, 0, 1]),
        ("P=5 alt", [0, 1, 0, 1, 0]),
        ("P=6 tail1(odd factor 3)", [0, 0, 0, 0, 0, 1]),
        ("P=6 alt(word 01 rep)", [0, 1, 0, 1, 0, 1]),
        ("P=7 tail1", [0, 0, 0, 0, 0, 0, 1]),
        ("P=8 alt", [0, 1, 0, 1, 0, 1, 0, 1]),
    ]
    for name, word in tests:
        try:
            vals = nu2_for_period(word, n_vals)
            print("%-22s %s" % (name, vals))
        except Exception as e:
            print("%-22s ERROR %s" % (name, e))


if __name__ == "__main__":
    main()
