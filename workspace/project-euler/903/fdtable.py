#!/usr/bin/env python3
"""FD table for PE 903 structure: F(d), phi(n!/d), and Q(n) = sum_d ... .

For n = 4, 5, 6 prints every divisor d of n! with phi(n!/d) and F(d) exactly,
verifies F(n!) = n!(n!+1)/2 (it must, since pi^n! = id for all pi), verifies
sum_d phi(n!/d)*F(d) against the known Q values (4808 / 597876 / 133103808),
cross-checks f_table against the literal per-i oracle, and writes
fdtable.json: list of {n, d, phi(n!/d), F(d)} plus per-n totals.
"""

import itertools
import json
from math import factorial

from toolkits.f_literal import f_by_gcd
from toolkits.f_table import f_table

KNOWN = {4: 4808, 5: 597876, 6: 133103808}   # known Q(n) values (statement + run)
RANK_EXAMPLE = ((2, 1, 3), 3)                # from the problem statement


def phi(x):
    r = x
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
            r -= r // p
        p += 1
    if x > 1:
        r -= r // x
    return r


def divisors(x):
    ds = [1]
    p = 2
    while p * p <= x:
        if x % p == 0:
            while x % p == 0:
                x //= p
                ds = ds + [d * p for d in ds]
        p += 1
    if x > 1:
        ds = ds + [d * x for d in ds]
    return sorted(set(ds))


def main():
    # reproduce the statement's rank example independently of the toolkits
    perms3 = list(itertools.permutations(range(1, 4)))
    assert perms3.index(RANK_EXAMPLE[0]) + 1 == RANK_EXAMPLE[1], "rank example"

    rows = []
    summary = []
    for n in (4, 5, 6):
        nf = factorial(n)
        F = f_table(n)                     # cycle-raising route
        Flit = f_by_gcd(n)                 # literal orbit route (oracle)
        assert F == Flit, f"f_table vs literal oracle disagree for n={n}"
        assert F[1] == nf * (nf + 1) // 2, "F(1) identity"
        assert F[nf] == nf * (nf + 1) // 2, "F(n!) identity (pi^n! = id)"

        Q = 0
        for d in divisors(nf):
            ph = phi(nf // d)
            Q += ph * F[d]
            rows.append({"n": n, "d": d, "phi(n!/d)": ph, "F(d)": F[d]})
        assert Q == KNOWN[n], f"Q({n}) mismatch: {Q}"

        print(f"=== n = {n}   (n! = {nf})   Q(n) = {Q}  "
              f"[oracle check {'OK' if Q == KNOWN[n] else 'FAILED'}]")
        for d in sorted(F):
            print(f"  d={d:4d}  phi({nf//d:3d})={phi(nf//d):5d}  "
                  f"F(d)={F[d]:10d}")
        summary.append({"n": n, "n!": nf, "Q(n)": Q, "ok": Q == KNOWN[n]})
        print()

    with open("fdtable.json", "w") as fh:
        json.dump({"rows": rows, "totals": summary}, fh, indent=2)
    print("wrote fdtable.json (%d rows)" % len(rows))
    print(json.dumps(summary))


if __name__ == "__main__":
    main()
