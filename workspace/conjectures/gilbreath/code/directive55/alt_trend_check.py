#!/usr/bin/env python3
"""Directive-55 follow-up: is the alternating-2/4 (and 2,2,4,2,4) transfer
ratio nu2/w genuinely decaying to 0, or settling at a positive value?

Load-bearing check: if a family satisfies H_b/H_d (both bit values present,
even with positive density on every prefix) yet nu2/w -> 0, then no listed
non-degeneracy hypothesis restores the transfer — it is prime-specific.

We trace nu2 (both conventions) and w at increasing n for the structured
families, to see the trend.
"""
from directive55.nu2_transfer_characterize import (
    triangle_rows, nu2_of_diagonal, build_gaps, w_of_seg,
    alternating_24, two_two_four_then_2424, all_gaps_4, consecutive_odds,
)


def trace(seq, ns, name):
    gaps = build_gaps(seq)
    maxn = max(ns)
    rows = list(triangle_rows(seq, maxn))
    print("\n[%s]" % name)
    print("%-7s %-7s %-7s %-8s %-10s %-10s" % (
        "n", "nu2c", "nu2l", "w", "nu2c/w", "nu2l/w"))
    for n in ns:
        dd = [rows[k][n - k] for k in range(n + 1) if n - k < len(rows[k])]
        nu2_c, nu2_l, _, _ = nu2_of_diagonal(dd)
        w = w_of_seg(gaps, n)
        cw = (nu2_c / w) if w else float('inf')
        lw = (nu2_l / w) if w else float('inf')
        print("%-7d %-7d %-7d %-8d %-10.5f %-10.5f" % (n, nu2_c, nu2_l, w, cw, lw))


if __name__ == "__main__":
    NS = [100, 200, 400, 800, 1200, 1600, 2000, 3000, 4000, 5000, 6000, 8000, 10000]
    trace(alternating_24(11000), NS, "alternating-2/4")
    trace(two_two_four_then_2424(11000), NS, "2,2,4,2,4,...")
    trace(all_gaps_4(11000), NS, "all-gaps-4")
    trace(consecutive_odds(11000), NS, "consecutive-odds")
