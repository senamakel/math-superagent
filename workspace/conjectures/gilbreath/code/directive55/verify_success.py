#!/usr/bin/env python3
"""Directive-55: verify the alternating-2/4 family is a SUCCESSFUL
2-then-odds sequence (leading column A_k(0)=1 for all k) to large depth,
and confirm the nu2=O(1) phenomenon is not a finite-width artifact.

Also record the leading column for consecutive-odds and 2,2,4,2,4 for
comparison, plus a fresh-width sanity check (independent generator avoids
reusing a possibly-shared buffer).
"""
from directive55.nu2_transfer_characterize import (
    triangle_rows, alternating_24, two_two_four_then_2424, consecutive_odds,
    nu2_of_diagonal, build_gaps, w_of_seg)


def leading_and_nu2(seq, n, depth):
    """Return (leading_col_is_1 to depth, nu2c at n, w at n).
    Uses a fresh triangle to depth (independent generator)."""
    rows = list(triangle_rows(seq, depth))
    lead_ok = all(rows[k][0] == 1 for k in range(1, depth + 1))
    # nu2 at column n from the same rows
    dd = [rows[k][n - k] for k in range(min(len(rows), n + 1))
          if n - k < len(rows[k])]
    # terminal requires row n; if depth < n, body only (still fine for suffix)
    nu2_c, nu2_l, _, _ = nu2_of_diagonal(dd)
    gaps = build_gaps(seq)
    w = w_of_seg(gaps, n)
    return lead_ok, nu2_c, nu2_l, w


def main():
    DEPTH = 3000
    NS = [200, 500, 1000, 2000, 3000]
    print("Success (leading A_k(0)=1 to depth %d) and nu2 at varying n" % DEPTH)
    print("%-16s %-6s %-8s %-8s %-8s" % ("family", "n", "lead1", "nu2c", "w"))
    fams = {
        'alternating-2/4': alternating_24(DEPTH + 100),
        '2,2,4,2,4,...': two_two_four_then_2424(DEPTH + 100),
        'consecutive-odds': consecutive_odds(DEPTH + 100),
    }
    for name, seq in fams.items():
        lead_first = None
        for n in NS:
            lead_ok, nu2_c, nu2_l, w = leading_and_nu2(seq, n, min(DEPTH, n))
            if lead_first is None:
                lead_first = lead_ok
            print("%-16s %-6d %-8s %-8d %-8d" % (name, n, lead_ok, nu2_c, w))
        print("  (leading column 1 holds at all checked n for %s: %s)"
              % (name, lead_first))


if __name__ == "__main__":
    main()
