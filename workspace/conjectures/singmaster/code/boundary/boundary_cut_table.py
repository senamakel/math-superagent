#!/usr/bin/env python3
"""Tabulate, for the Fibonacci family j=1..6 and the witness set, each
nontrivial occurrence's column k against the MRSTT boundary cut, exactly.

MRSTT (Theorem 1.3, Remark 1.5): with eps in (0,1), an occurrence (n,k) of
C(n,k)=a with 2<=k<=n/2 is BOUNDARY (MRSTT-OPEN) iff

    k < exp((log n)^(2/3+eps))

and INTERIOR iff exp((log n)^(2/3+eps)) <= k <= n/2.  Here we take eps=1/2
(the gap task's stated value), so cut_n = exp((log n)^(7/6)); log = natural.

Counting convention (same as the whole run): N(a) counts both mirrors
(C(n,k), C(n,n-k)) plus the trivial pair C(a,1)=C(a,a-1).

No search is performed: the occurrences are KNOWN, and each candidate rep
(n,k) is verified in exact integer arithmetic to satisfy C(n,k) == a before
it is tabulated.  This is why the run is cheap and cannot hang (the previous
code/boundary_cut.py hung: it binary-searched n up to a for the 28+-digit
family members).

The Fibonacci family (Lind/Singmaster, infinite N(a)>=6 family):
    n_j = F_{2j+2}*F_{2j+3} - 1,   m_j = F_{2j}*F_{2j+3} - 1,
    C(n_j+1, m_j+1) = C(n_j, m_j+2) = a_j
with two nontrivial left-half reps (n_j+1, m_j+1) and (n_j, m_j+2).
"""
import json
import math
import sys

sys.set_int_max_str_digits(0)  # allow str() of the astronomically large a_j

EPS = 0.5
EXP = 2.0 / 3.0 + EPS  # = 7/6


def cut(n):
    """Natural-log based MRSTT boundary cut for row n with eps=1/2."""
    return math.exp(math.log(n) ** EXP)


def is_boundary(n, k):
    """True iff (n,k) lies in the MRSTT-open boundary (k < cut)."""
    return k < cut(n)


def fib(n):
    a, b = 1, 1
    for _ in range(n - 1):
        a, b = b, a + b
    return a


def fib_members():
    F = [0, 1]
    for _ in range(2, 20):
        F.append(F[-1] + F[-2])
    members = []
    for j in range(1, 7):
        n = F[2 * j + 2] * F[2 * j + 3] - 1
        m = F[2 * j] * F[2 * j + 3] - 1
        a = math.comb(n + 1, m + 1)
        # two nontrivial left-half reps; verify both equal the same a
        assert math.comb(n, m + 2) == a, (j, "identity failed")
        members.append((j, a, [(n + 1, m + 1), (n, m + 2)]))
    return members


def main():
    rows = []

    # Witness set from witnesses.json (nontrivial canonical reps).
    with open("code/out/witnesses.json") as f:
        data = json.load(f)
    for a_str, rec in data["witnesses"].items():
        a = int(a_str)
        for (n, k) in rec["nontrivial"]:
            assert math.comb(n, k) == a, (a, n, k)
            rows.append((("witness", a), n, k))

    # Fibonacci family.
    for (j, a, reps) in fib_members():
        for (n, k) in reps:
            assert math.comb(n, k) == a, (j, n, k)
            rows.append((("fib", j, a), n, k))

    print("MRSTT boundary-cut tabulation, eps=1/2, cut_n=exp(log(n)^(7/6))")
    print("Convention: N(a) counts both mirrors + trivial pair.")
    print("category  a            rep (n,k)      cut_n        k      class")
    print("-" * 72)
    counts = {}
    for (cat, *rest), n, k in sorted(rows, key=lambda r: r[0]):
        c = cut(n)
        cls = "BOUNDARY" if is_boundary(n, k) else "interior"
        counts[cls] = counts.get(cls, 0) + 1
        if cat == "witness":
            label = "witness %d" % rest[0]
        else:
            label = "fib j=%d a=%d" % (rest[0], rest[1])
        print("%-13s %9d  (%7d,%2d)  %12.4f  %5d  %s"
              % (label, rest[-1] if cat == "witness" else rest[1],
                 n, k, c, k, cls))

    print("-" * 72)
    print("Totals over all 19 known nontrivial occurrences:")
    for cls in ("BOUNDARY", "interior"):
        print("   %-9s %d" % (cls, counts.get(cls, 0)))
    b = counts.get("BOUNDARY", 0) + counts.get("interior", 0)
    print("   total = %d" % b)
    print("DONE")


if __name__ == "__main__":
    main()
