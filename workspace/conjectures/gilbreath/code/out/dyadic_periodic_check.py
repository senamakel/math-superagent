#!/usr/bin/env python3
"""
Scholar's small-oracle check of the LIVE dyadic-periodicity-collapse prediction
(thread research/threads/dyadic-periodicity-collapse.md, Directive 57).

Prediction under test: for a synthetic odd-number input sequence whose halved-gap
PARITY bits h_j = (g_j/2) mod 2 are eventually periodic with period P,
   nu2(q_n) = O_P(1)   exactly when P is a power of 2,
and nu2 grows when P has an odd factor.

nu2(q_n) = # of 2s in the maximal {0,2} suffix of the right diagonal through q_n.

Falsifier (stated in the thread): if a period-3 or period-5 family ALSO gives
nu2 = O(1), the dyadic story is wrong.

This is a bounded small oracle (rule 9): it does NOT push a bound, it checks the
qualitative shape of a structural claim on tiny instances.
"""
import sys

def build_triangle(gaps, depth):
    """gaps list: g_1.. ; row A_1 = (1, g_1, g_2, ...) where g_1 = 3-2 = 1.
    We construct A_0 = [2,3] + odds with the given even gaps appended.
    Actually simpler: build A_1 directly as the difference row, then iterate.
    A_1 = (1, g_1, g_2, ...)."""
    # A_1 row: leading 1, then gaps. gaps[0]=1 (2->3), gaps[1..] even.
    row = [1] + list(gaps)
    rows = [row]
    for _ in range(depth):
        row = [abs(row[i]-row[i+1]) for i in range(len(row)-1)]
        rows.append(row)
    return rows

def nu2_at_n(rows, n):
    """right diagonal through q_n: d[k] = A_k[n-k], k=0..n-1.
    nu2 = #2s in maximal {0,2} suffix of the diagonal."""
    d = []
    for k in range(n):
        r = rows[k]
        if n - k < len(r):
            d.append(r[n-k])
    # maximal suffix all in {0,2}
    # read from the bottom (k=n-1 end) upward
    # diagonal is d[0..]; the tip is d[len-1] (the very bottom cell, = q_n? )
    # We want maximal suffix from the tip. Let idx from the end.
    count2 = 0
    i = len(d)-1
    # extend while in {0,2}
    while i >= 0 and d[i] in (0,2):
        if d[i]==2:
            count2 += 1
        i -= 1
    return count2, i, d

def make_input_gaps(period_pattern, N):
    """Construct the even gap sequence (beyond the first gap=1) with halved
    parity = period_pattern (list of 0/1 repeated), plus a magnitude so the
    triangle is non-trivially {0,2}-regime."""
    gaps = [1]  # 2->3
    for i in range(N):
        h = period_pattern[i % len(period_pattern)]
        # gap even with (g/2) mod 2 == h ; use g = 2 or 4
        g = 2 if h==1 else 4
        gaps.append(g)
    return gaps

def run(period_pattern, nmin, nmax, depth):
    gaps = make_input_gaps(period_pattern, depth*3)
    rows = build_triangle(gaps, depth)
    out = {}
    for n in range(nmin, nmax+1):
        if n >= len(rows):
            break
        c2, stop_i, _d = nu2_at_n(rows, n)
        out[n] = c2
    return out

def describe(period_pattern, nmin=50, nmax=500):
    # depth must exceed nmax
    res = run(period_pattern, nmin, nmax, nmax+10)
    vals = [res[n] for n in res]
    # does nu2 stay O(1)? look at max over the last 2/3
    tail = vals[len(vals)//3:]
    return max(vals), max(tail), min(vals)

if __name__ == "__main__":
    periods = {
        1: [1],
        2: [1,0],
        3: [1,0,0],
        4: [1,0,0,0],
        5: [1,0,0,0,0],
        6: [1,0,0,0,0,0],
        7: [1,0,0,0,0,0,0],
        8: [1,0,0,0,0,0,0,0],
    }
    print("prediction: nu2 = O(1) iff period is a power of 2")
    print(f"{'P':>3} {'power2?':>7} {'nu2 all max':>11} {'nu2 tail max':>12} {'nu2 min':>7}")
    for P, pat in periods.items():
        mx_all, mx_tail, mn = describe(pat, nmin=50, nmax=500)
        print(f"{P:>3} {str(P & (P-1)==0):>7} {mx_all:>11} {mx_tail:>12} {mn:>7}")
