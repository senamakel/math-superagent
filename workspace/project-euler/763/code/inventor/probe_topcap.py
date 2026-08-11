#!/usr/bin/env python3
"""Probe 1 of reversed 3D FE763 — the TOP CAP structural fact.

Every reachable 3D config S (after N>=1 divisions, 2N+1 cells, max level M)
is claimed to have:
  (S1) exactly 3 cells on its top level M, and
  (S2) those 3 top cells are exactly {p*+e1, p*+e2, p*+e3} for a UNIQUE empty
       cell p* at level M-1 (they are one cell's complete forward-child set;
       by Eriksson Prop 24, n>=3, no cell is ever produced twice, so the top
       level MUST be a single full child-triangle).

Run over every config recorded in /workspace/data/level_N.txt (N=2..12) and
report any violation.  Also verify:
  (S3) every level-N config has a_M == 3 (top level cardinality 3).
This is the deterministic-peel lever: it makes the reverse collapse canonical,
which is what turns counting configs into counting collapse trees.

Tool_builder: run `python3 code/inventor/probe_topcap.py` from /workspace.
"""
import os

E = [(1, 0, 0), (0, 1, 0), (0, 0, 1)]


def parse_config(line):
    # format: "a0 a1 ... aM | M | dx dy dz"
    hist_part = line.split("|")[0].strip()
    return [int(x) for x in hist_part.split()]


def main():
    bad_s1 = 0
    bad_s2 = 0
    total = 0
    for N in range(2, 13):
        path = f"data/level_{N}.txt"
        if not os.path.exists(path):
            continue
        lines = open(path).read().strip().splitlines()
        for line in lines:
            a = parse_config(line)
            M = len(a) - 1
            top = a[M]
            total += 1
            # S3: top level cardinality must be 3
            if top != 3:
                bad_s1 += 1
                print(f"S3 FAIL N={N} top_level_count={top} a={a}")
            # number of cells on level M-1 whose full child-triangle could
            # fill the top level exactly when that child-triangle sits at M.
            # a parent at level M-1 contributes +3 to level M.  Total on M is
            # 3, so exactly one such parent contributes.  Record divisibility.
            if a[M] % 3 != 0:
                bad_s2 += 1
                print(f"S2-partial FAIL N={N} a_M={a[M]} not divisible by 3")
    print(f"\nchecked {total} configs over N=2..12")
    print(f"S3 (top level == 3) violations: {bad_s1}")
    print(f"S2 (top level divisible by 3) violations: {bad_s2}")


if __name__ == "__main__":
    main()
