#!/usr/bin/env python3
"""anbtable.py — print the A_n/B_n divisibility table from ccsum_ab.json.

For every n present in code/out/ccsum_ab.json it prints:
    n, A_n, B_n, A_n//(n-1)!, B_n//(n-1)!, A_n%(n-1)!, B_n%(n-1)!
(integer div/mod by (n-1)! so divisibility patterns show), plus a TRUST
column so nobody mistakes the invalid conjugacy-class rows for the true
A_n/B_n.

TRUST STATUS (verified 18 Sep 2025, see code/out/INDEX.md and the ccsum.py
investigation): ccsum.py's rows agree with the independently verified
out/extend_f.json ONLY at n=2.  For every n=3..30 they differ and are not
even arithmetic in k.  Root cause (proved): the engine assumes the cyclic-
subgroup count S(lambda,k)=#{tau in <pi>: tau(k)<tau(0)} is constant on each
conjugacy class, but test_classconst.py shows it takes several values within
one class (e.g. n=4, type (1,3): S in {0,1,2}).  Hence the n>=2 ccsum rows
must NOT be used as A_n/B_n.  A trusted reference table (n=2..11) is built
from out/extend_f.json in the same run so valid values are always on the
same page.

The requested columns are still computed for every row of ccsum_ab.json so
the script does what was asked, but every non-trusted row is flagged.

Usage: python3 code/anbtable.py   (writes code/out/anbtable.txt)
"""
import json
import math
import os

HERE = os.path.dirname(os.path.abspath(__file__))


def fact(nn):
    return math.factorial(nn)


def trusted_extend_rows():
    """Return {n: [f(1),...,f(n-1)]} from the independently verified file."""
    with open(os.path.join(HERE, "out", "extend_f.json")) as fh:
        return {int(k): v for k, v in json.load(fh).items()}


def main():
    ab_path = os.path.join(HERE, "out", "ccsum_ab.json")
    with open(ab_path) as fh:
        ab = json.load(fh)

    ext = trusted_extend_rows()
    # A_n/B_n from the trusted extend rows: A=f(1), B=f(2)-f(1)
    trust_ab = {}
    for n, row in ext.items():
        A = row[0]
        B = row[1] - row[0] if len(row) >= 2 else 0
        trust_ab[n] = (A, B)

    lines = []
    lines.append("A_n/B_n divisibility table (n | A | B | A//(n-1)! | B//(n-1)! | "
                 "A%(n-1)! | B%(n-1)! | TRUST)")
    lines.append("-" * 100)
    for sn in sorted(ab, key=int):
        n = int(sn)
        A = ab[sn]["A"]
        B = ab[sn]["B"]
        f = fact(n - 1)
        # trust: n==2 is the only ccsum row verified against extend_f.json
        if n in trust_ab and (A, B) == trust_ab[n]:
            trust = "TRUSTED (== extend_f.json)"
        elif n in trust_ab:
            trust = f"UNTRUSTED (differs from extend_f.json; expected {trust_ab[n]})"
        else:
            trust = "UNTRUSTED (new n, ccsum engine invalid for n>=3)"
        lines.append(
            f"{n:3d} | {A:>26} | {B:>26} | {A//f:>30} | {B//f:>28} | "
            f"{A%f:>28} | {B%f:>26} | {trust}"
        )

    lines.append("")
    lines.append("=== TRUSTED reference A_n/B_n (from out/extend_f.json, n=2..11) ===")
    lines.append(f"{'n':>3} | {'A_n':>22} | {'B_n':>22} | {'A//(n-1)!':>22} | "
                 f"{'B//(n-1)!':>22} | {'A%(n-1)!':>22} | {'B%(n-1)!':>22}")
    lines.append("-" * 120)
    for n in sorted(trust_ab):
        A, B = trust_ab[n]
        f = fact(n - 1)
        lines.append(f"{n:>3} | {A:>22} | {B:>22} | {A//f:>22} | {B//f:>22} | "
                     f"{A%f:>22} | {B%f:>22}")

    out = "\n".join(lines)
    print(out)
    out_path = os.path.join(HERE, "out", "anbtable.txt")
    with open(out_path, "w") as fh:
        fh.write(out + "\n")
    print(f"\nwrote {out_path}")


if __name__ == "__main__":
    main()
