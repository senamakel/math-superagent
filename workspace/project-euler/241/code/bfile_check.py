#!/usr/bin/env python3
"""Independent verification route for PE241 from the OEIS A159907 b-file.

A159907 (hemiperfect numbers) = {n : 2*sigma(n)/n is an odd integer}, which is
exactly the PE241 qualifying set {n <= 10^18 : sigma(n)/n = k+1/2, k integer}.
This script reads the downloaded b-file, extracts every term <= 10^18 (terms
1..22; term 23 = 6219051710415667200 already exceeds 10^18), optionally
independently verifies each extracted term's abundancy is sigma(n)/n = k+1/2,
sums the terms in exact integer arithmetic, and cross-checks against the DFS
result log if present.

Exact integer arithmetic throughout. Output written to code/BFILE_CHECK.md.
"""

import math
import os
import sys
from pathlib import Path

LIMIT = 10**18
BFILE = Path(__file__).resolve().parent.parent / "research" / "sources" / "A159907_bterm.full.md"
RUN_LOG = Path(__file__).resolve().parent / "RUN_LOG.md"
OUT = Path(__file__).resolve().parent / "BFILE_CHECK.md"


def parse_bterm(text: str):
    """Return list of (index, value) int tuples for every 'i value' line."""
    terms = []
    for line in text.splitlines():
        line = line.strip()
        if not line or line.startswith(("#", "<!--", "*")):
            continue
        parts = line.split()
        if len(parts) != 2:
            continue
        try:
            idx, val = int(parts[0]), int(parts[1])
        except ValueError:
            continue
        terms.append((idx, val))
    return terms


def factor_odd_power_sum(n):
    """sigma(n), the sum of divisors of n. Simple trial division (all terms
    are <= 1e18 but have small factors; fine for a 22-term check)."""
    m, s, p = n, 1, 2
    while p * p <= m:
        if m % p == 0:
            pp, cnt = p, 0
            while m % p == 0:
                m //= p
                cnt += 1
                pp *= p
            # sigma(p^cnt) = (p^(cnt+1)-1)/(p-1)
            s *= (pp - 1) // (p - 1)
        p += 1 if p == 2 else 2
    if m > 1:
        s *= (m + 1)
    return s


def abundancy_half_integer(n):
    """Return the reduced value 2*sigma(n)/n; True if it is an odd integer."""
    s = factor_odd_power_sum(n)
    num = 2 * s
    d = math.gcd(num, n)
    num, den = num // d, n // d
    return den == 1 and num % 2 == 1, num, s


def main():
    text = BFILE.read_text(encoding="utf-8")
    terms = parse_bterm(text)
    if not terms:
        print("ERROR: no terms parsed from", BFILE)
        sys.exit(1)

    selected = []   # (idx, value)
    excluded = []   # (idx, value) terms beyond the limit
    for idx, val in terms:
        if val <= LIMIT:
            selected.append((idx, val))
        else:
            excluded.append((idx, val))

    # Independent verification: each selected term really is in A159907.
    verified = []
    for idx, val in selected:
        ok, num, s = abundancy_half_integer(val)
        verified.append((idx, val, ok, num))
        if not ok:
            print(f"WARNING: term {idx} = {val} does NOT verify as hemiperfect")

    total = sum(val for _, val in selected)

    lines = []
    lines.append("# BFILE_CHECK — independent PE241 route via OEIS A159907 b-file")
    lines.append("")
    lines.append(f"- Source: `{BFILE.name}`")
    lines.append(f"- Limit: n <= 10^18")
    lines.append("- A159907 = hemiperfect numbers = the PE241 qualifying set "
                 "(2*sigma(n)/n an odd integer).")
    lines.append("")
    lines.append("## Selected terms (n <= 10^18): first unexcluded content")
    lines.append("")
    lines.append("| index | n | verified 2*sigma(n)/n = odd int |")
    lines.append("| --- | --- | --- |")
    for idx, val, ok, num in verified:
        lines.append(f"| {idx} | {val} | {'yes' if ok else 'NO — ' + str(num)} |")
    lines.append(f"| **total** | **{total}** | |")
    lines.append("")
    lines.append(f"**Sum of all {len(selected)} A159907 terms <= 10^18 = {total}**")
    lines.append("")
    lines.append("## Terms just beyond the limit (excluded)")
    lines.append("")
    lines.append("| index | n |")
    lines.append("| --- | --- |")
    for idx, val in excluded:
        lines.append(f"| {idx} | {val} |")
    lines.append("")
    lines.append(f"First excluded term: index {excluded[0][0]} = {excluded[0][1]} "
                 f"(exceeds 10^18 by factor {excluded[0][1]/LIMIT:.6g}).")
    lines.append("")

    # Cross-check against the DFS result log, if present.
    if RUN_LOG.exists():
        log_text = RUN_LOG.read_text(encoding="utf-8")
        dfs_vals = set()
        for tok in log_text.split():
            try:
                v = int(tok)
            except ValueError:
                continue
            if 0 < v <= LIMIT:
                dfs_vals.add(v)
        bfile_vals = {val for _, val in selected}
        if dfs_vals:
            match = dfs_vals == bfile_vals
            lines.append("## Cross-check vs DFS RUN_LOG.md")
            lines.append("")
            lines.append(f"- DFS log values (parsed ints <= 10^18): {len(dfs_vals)}")
            lines.append(f"- b-file values: {len(bfile_vals)}")
            lines.append(f"- Sets match exactly: **{'YES' if match else 'NO'}'**")
            if not match:
                only_bfile = bfile_vals - dfs_vals
                only_dfs = dfs_vals - bfile_vals
                lines.append(f"- only in b-file: {sorted(only_bfile)}")
                lines.append(f"- only in DFS log: {sorted(only_dfs)}")
        else:
            lines.append("## Cross-check vs DFS RUN_LOG.md")
            lines.append("")
            lines.append("- RUN_LOG.md exists but no integer values <= 10^18 parsed; "
                         "cross-check inconclusive.")
        lines.append("")
    else:
        lines.append("## Cross-check vs DFS RUN_LOG.md")
        lines.append("")
        lines.append("- `code/RUN_LOG.md` does not exist; no DFS cross-check performed.")
        lines.append("")

    OUT.write_text("\n".join(lines), encoding="utf-8")

    print(f"Extracted {len(selected)} terms <= 10^18 (indices "
          f"{selected[0][0]}..{selected[-1][0]}); "
          f"{len(excluded)} terms beyond (first excluded index {excluded[0][0]}).")
    for idx, val, ok, _ in verified:
        print(f"  {idx:>3}  {val:>20}  verified={ok}")
    print()
    print(f"TOTAL (sum of all A159907 terms <= 10^18) = {total}")
    print()
    print("Wrote", OUT)


if __name__ == "__main__":
    main()
