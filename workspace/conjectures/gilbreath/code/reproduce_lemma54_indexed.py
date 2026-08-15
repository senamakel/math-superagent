#!/usr/bin/env python3
"""Reproduce the operator's established numbers via the indexed incremental
path (lib.rightdiag_idx) so the deliverable machinery is checked against the
recorded notes before the 1e5 run and the synthetic failing sisters.

Part A: nu2 sample n in {50,...,3999}, sieve 3e6 — must reproduce the recorded
table exactly (26,42,98,203,389,785,1604,2048; nu2/n in 0.420..0.520).
Part B: Lemma 5.4 iff/suff/discarded n=20..2499, sieve 2e6 — must reproduce
(2480 tested, all successful, 0 violations, 100% delta=0).
"""
from lib.gilbreath import primes_up_to
from lib.rightdiag_idx import diagonals_by_n, nu2_of, lemma54_transition


def part_A():
    P = primes_up_to(3_000_000)
    samples = [50, 100, 200, 400, 800, 1600, 3200, 3999]
    diags = {}
    for n, d in diagonals_by_n(P):
        if n in samples:
            diags[n] = d
        if n >= max(samples):
            break
    gaps = [P[i+1]-P[i] for i in range(len(P)-1)]
    print("== Part A: nu2 sample, sieve 3e6 (recorded/ours) ==")
    print("%-6s %-8s %-10s %-8s %-8s %s" % ("n","nu2","n^0.525","nu2/n","g*","hyp"))
    bad = 0
    for n in samples:
        d = diags[n]
        nu2 = nu2_of(d)
        g = max(gaps[1:n])
        ok = g <= 2*nu2 + 2
        if not ok: bad += 1
        print("%-6d %-8d %-10.2f %-8.4f %-8d %s" % (n, nu2, n**0.525, nu2/n, g, ok))
    print("hyp failed at", bad, "sampled n (recorded: 0)")
    print("nu2 series (recorded): 26 42 98 203 389 785 1604 2048")


def part_B():
    P = primes_up_to(2_000_000)
    M = 2500
    gaps = [P[i+1]-P[i] for i in range(len(P)-1)]
    gstar = 0
    gen = diagonals_by_n(P)
    dprev = next(gen)[1]          # delta(q_1)
    tested = 0; n_ok = 0; iff_viol = 0; suff_viol = 0; zero_rows = 0
    for n in range(2, M):
        dcur = next(gen)[1]
        gstar = max(gstar, gaps[n-1])   # g_n
        if n < 20:
            dprev = dcur
            continue
        r = lemma54_transition(dprev, dcur, gstar)
        cyc = dprev[r['tau']:-1]
        if any(x not in (0, 2) for x in cyc):
            dprev = dcur
            continue
        if r['tau'] >= len(dcur) - 1:
            dprev = dcur
            continue
        tested += 1
        if r['success']: n_ok += 1
        if not r['iff']: iff_viol += 1
        if r['hyp'] and not r['success']: suff_viol += 1
        if r['discarded_delta0']: zero_rows += 1
        dprev = dcur
    print()
    print("== Part B: Lemma 5.4 iff/suff/discarded, sieve 2e6 ==")
    print("tested n:", tested, "all successful:", n_ok == tested, "(", n_ok, ")")
    print("iff  v<=2nu2+2 <=> success : violations =", iff_viol)
    print("suff g*<=2nu2+2 => success : violations =", suff_viol)
    print("discarded delta=0 rows:", zero_rows, "(%.1f%%)" % (100.0*zero_rows/max(1,tested)))
    print("recorded: 2480, all successful True, iff 0, suff 0, zero 2480 (100%)")


if __name__ == "__main__":
    part_A()
    part_B()
