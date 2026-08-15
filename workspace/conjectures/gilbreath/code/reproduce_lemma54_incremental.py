#!/usr/bin/env python3
"""Reproduce the operator's established numbers via the incremental 1D
right-diagonal path (lib.rightdiag), so deliverable 1/2 machinery is checked
against known results before the 1e5 run and the synthetic failing sisters.

Part A: nu2 sample table (matches code/nu2_granville_check.py, sieve 3e6, n in
{50,100,200,400,800,1600,3200,3999}).
Part B: Lemma 5.4 iff/suff/discarded-delta=0 (matches code/lemma54_iff_check.py,
sieve 2e6, n=20..2499) — but here on a REAL failing run the iff is checked
against a genuine 'success' predicate that can be False.
"""
from lib.gilbreath import primes_up_to
from lib.rightdiag import incremental_diagonals, cycle_and_nu2


def part_A():
    P = primes_up_to(3_000_000)
    samples = [50, 100, 200, 400, 800, 1600, 3200, 3999]
    gen = incremental_diagonals(P)
    diags = {}
    for n in range(0, max(samples) + 1):
        d = next(gen)
        if n in samples:
            diags[n] = d
    gstar = 0
    gaps = [P[i+1]-P[i] for i in range(len(P)-1)]
    print("== Part A: nu2 sample (incremental path, sieve 3e6) ==")
    print("%-6s %-8s %-10s %-8s %-10s %-8s %s" % ("n","nu2","n^0.525","nu2/n","g*","2nu2+2","hyp"))
    bad = 0
    for n in samples:
        d = diags[n]
        tail = d[2:-1]
        i = len(tail)
        while i > 0 and tail[i-1] in (0, 2):
            i -= 1
        cyc = tail[i:]
        nu2 = cyc.count(2)
        g = max(gaps[1:n])        # g_2..g_n
        ok = g <= 2*nu2 + 2
        if not ok: bad += 1
        print("%-6d %-8d %-10.2f %-8.4f %-10d %-8d %s" % (n, nu2, n**0.525, nu2/n, g, 2*nu2+2, ok))
    print("hyp failed at", bad, "of sampled n")
    print("NOTES said nu2/n in 0.420..0.520, nu2=2048 at n=3999, g*=72, 2nu2+2=4098, all hold")
    return bad


def part_B():
    P = primes_up_to(2_000_000)
    M = 2500
    gen = incremental_diagonals(P)
    diags = {}
    for n in range(0, M + 1):
        d = next(gen)
        if n >= 19:
            diags[n] = d
    gaps = [P[i+1]-P[i] for i in range(len(P)-1)]
    gstar = 0
    tested = 0; n_ok = 0; iff_viol = 0; suff_viol = 0; zero_rows = 0
    for n in range(20, M):
        dprev = diags[n-1]
        dcur = diags[n]
        tau, nu2 = cycle_and_nu2(dprev)
        cyc = dprev[tau:-1]
        if any(x not in (0, 2) for x in cyc):
            continue
        if tau >= len(dcur) - 1:
            continue
        v = dcur[tau]
        success = (dcur[-1] == 1)
        tested += 1
        if success: n_ok += 1
        pred = (v <= 2*nu2 + 2)
        if pred != success: iff_viol += 1
        g = max(gaps[1:n+1])
        if g <= 2*nu2 + 2 and not success:
            suff_viol += 1
        if 0 in dcur[tau+1:-1]:
            zero_rows += 1
    print()
    print("== Part B: Lemma 5.4 iff/suff/discarded (incremental path, sieve 2e6) ==")
    print("tested n:", tested, "all successful:", n_ok == tested, "(", n_ok, ")")
    print("iff  v<=2nu2+2 <=> success : violations =", iff_viol)
    print("suff g*<=2nu2+2 => success : violations =", suff_viol)
    print("rows where discarded delta=0 occurs:", zero_rows, "(%.1f%%)" % (100.0*zero_rows/max(1,tested)))
    print("NOTES said: 2480 tested, all successful True, iff 0, suff 0, zero cases 2480 (100%)")
    return tested


if __name__ == "__main__":
    part_A()
    part_B()
