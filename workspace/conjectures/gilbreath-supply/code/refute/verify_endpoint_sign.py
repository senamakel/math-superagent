#!/usr/bin/env python3
"""Verify the committed formula in G-endpoint-comparison-density against the
direct oracle.

Committed statement claims:
    (-1)^{T(n,d)} = (-1)^{#runs(d)} * prod_R chi(r_{a_R}) chi(r_{b_R})

The corrected identity (per the board's adversarial post) is:
    (-1)^{T(n,d)} = prod_R chi(r_{a_R}) chi(r_{b_R})
because [r_a != r_b] = 1  <=>  chi(r_a)chi(r_b) = -1, so (-1)^{[r_a!=r_b]} =
chi(r_a)chi(r_b), and XOR of the run indicators carries signs multiplicatively
with NO extra sign per run.

We check, for arbitrary h (any {0,1} string -> boundary r in {1,3}), whether
each candidate formula equals the direct oracle value.
"""
import sys, os, random

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", ".."))
from lib.submasks import boundary_from_h, downset_runs, fold_xor
from lib.supply_fold import t_direct


def chi(x):
    return -1 if x % 4 == 3 else 1


def corrected_formula(n, d, r):
    """prod_R chi(r_{a_R}) chi(r_{b_R}), a_R = n-1-d+u, b_R = n-1-d+v+1."""
    prod = 1
    for (u, v) in downset_runs(d):
        a = n - 1 - d + u
        b = n - 1 - d + v + 1
        prod *= chi(r[a]) * chi(r[b])
    return prod


def committed_formula(n, d, r):
    """(-1)^{#runs(d)} * prod_R chi(r_{a_R}) chi(r_{b_R})  (the committed form)."""
    runs = downset_runs(d)
    prod = 1
    for (u, v) in runs:
        a = n - 1 - d + u
        b = n - 1 - d + v + 1
        prod *= chi(r[a]) * chi(r[b])
    return (-1) ** len(runs) * prod


def main():
    random.seed(3)
    # test over arbitrary h strings so the identity is checked as a pure
    # Boolean statement, not on the primes in particular
    n = 10
    bad_corrected = 0
    bad_committed = 0
    checked = 0
    examples = []
    for trial in range(300):
        h = [random.randint(0, 1) for _ in range(n)]
        r = boundary_from_h(h)
        for d in range(2, n):
            T = t_direct(n, d, h)                    # oracle: 0 or 1
            rhs_direct = -1 if T else 1              # (-1)^{T}
            checked += 1
            c = corrected_formula(n, d, r)
            if c != rhs_direct:
                bad_corrected += 1
                if len(examples) < 3:
                    examples.append(("corrected", n, d, h, c, rhs_direct))
            m = committed_formula(n, d, r)
            if m != rhs_direct:
                bad_committed += 1
                if len(examples) < 3:
                    examples.append(("committed", n, d, h, m, rhs_direct))
    print(f"checked {checked} cells (n={n}, over random h, d=2..n-1)")
    print(f"  corrected formula (no sign): mismatches = {bad_corrected}")
    print(f"  committed formula (with (-1)^#runs): mismatches = {bad_committed}")
    for ex in examples[:3]:
        print("   example:", ex)

    # explicit hand-check on the primes' own r for the reported d=2,d=3
    from lib.primes import mod4_string
    big = mod4_string(20)   # r[j] = q_{j+1} mod 4
    r = [big[j] for j in range(20)]
    h = [1 if r[j + 1] != r[j] else 0 for j in range(len(r) - 1)]
    print("\nPrimes' own residues, n=10:")
    for d in [2, 3, 5, 6, 7]:
        T = t_direct(10, d, h)
        print(f"  d={d}: T={T} (-1)^T={-1 if T else 1} "
              f"corrected={corrected_formula(10, d, r)} "
              f"committed={committed_formula(10, d, r)}")


if __name__ == "__main__":
    main()
