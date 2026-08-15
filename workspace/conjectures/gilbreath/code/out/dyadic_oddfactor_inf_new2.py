#!/usr/bin/env python3
"""
Directive 62/64 decisive measurement — INFIMUM of the true nu2(n)/n over
n in [100, 20000] for odd-factor minimal periods P = 3,5,7,9, in RANGED
form so we can see whether the infimum KEEPS DECAYING toward 0 at large n
(a late plateau) or is bounded away from 0.

nu2(n) = number of 2s in the maximal {0,2} suffix of the right diagonal
delta(q_n), using the canonical `cycle_and_nu2` convention from
lib/rightdiag: suffix always starts at index >= 2 (body indices 0,1 never
counted); scanning stops at the first body entry not in {0,2}, or at index 2.

This is the same quantity the run anchored to nu2 = 2048 at n = 3999 for the
primes, and the one that feeds Granville Lemma 5.4's budget nu2 >= c*n.

Sequence: q_1 = 2, q_2 = 3, then q_{n+1} = q_n + (2 if bit else 4), bits the
periodic word (h[0] governs the gap q_2 -> q_3).

TWO independent routes, both exact integers, both using the same scan:
  (A) INCREMENTAL right-diagonal recurrence (delta(q_n) built from
      delta(q_{n-1}) in one pass)  -- O(N^2) diffs, O(N) memory.
  (B) FULL-TRIANGLE brute force (literal A_{k+1}(i)=|A_k(i)-A_k(i+1)| rows,
      right diagonal extracted)    -- independent code path.
They must agree cell-for-cell on the sampled points.

For each period we report:
  - inf nu2(n)/n over [100,N], [1000,N], [5000,N], [10000,N] and argmin,
  - the running-infimum history (every n that sets a new low) = the plateaus,
  - whether any new low is set after n > N/3   (a LATE plateau / decay signal),
  - the decisive read: bounded below by positive c, or decaying toward 0.

This is numerical verification over the stated range only — every conclusion
is CONFIRMED/REFUTED over n in [100,N], not proved.
"""
import sys
import numpy as np
from multiprocessing import Pool

sys.path.insert(0, '/workspace/code')
from lib.rightdiag import cycle_and_nu2


def build_seq(word, n_terms):
    """q_1=2, q_2=3; gap q_m->q_{m+1} (m>=2) uses word[(m-2)%P]: 2 if bit else 4."""
    q = [2, 3]
    P = len(word)
    while len(q) < n_terms:
        j = len(q) - 2
        gap = 2 if word[j % P] else 4
        q.append(q[-1] + gap)
    return q[:n_terms]


def scan_nu2_cyc(diag):
    """Canonical cycle_and_nu2 on a built diagonal (list or numpy array):
    body = diag[:-1], maximal {0,2} suffix starting at index >= 2."""
    body = diag[:-1]
    i = len(body)
    while i > 2 and body[i - 1] in (0, 2):
        i -= 1
    tau = i
    return body[tau:].count(2)


def sweep_nu2(word, N, lo=100):
    """Incremental diagonal recurrence; return {n: nu2} for n in [lo,N]."""
    q = build_seq(word, N + 1)
    D = [q[0]]
    out = {}
    for n in range(1, N + 1):
        nd = [0] * (n + 1)
        nd[0] = q[n]
        for k in range(1, n + 1):
            v = nd[k - 1] - D[k - 1]
            nd[k] = v if v >= 0 else -v
        D = nd
        if n >= lo:
            out[n] = scan_nu2_cyc(D)
    return out


def brute_force_nu2(word, n):
    """Independent full-triangle build: literal rows, right diagonal, same scan."""
    q = build_seq(word, n + 1)
    row = list(q)
    diag = [row[n]]
    for k in range(1, n + 1):
        nxt = [abs(row[i] - row[i + 1]) for i in range(len(row) - 1)]
        row = nxt
        diag.append(row[n - k])
    return scan_nu2_cyc(diag)


def analyze(P, word, nu2_by_n, N, lo):
    infs = {}
    for floor in (lo, 1000, 5000, 10000, 15000):
        seg = [nu2_by_n[n] / n for n in range(floor, N + 1)]
        if not seg:
            continue
        r = min(seg)
        arg = next(n for n in range(floor, N + 1) if nu2_by_n[n] / n == r)
        infs[floor] = (r, arg, nu2_by_n[arg])
    # running infimum (plateau readout)
    run = float('inf')
    running_trace = []
    for n in range(lo, N + 1):
        r_ = nu2_by_n[n] / n
        if r_ < run:
            run = r_
            running_trace.append((n, r_, nu2_by_n[n]))
    # late-new-low signal: does a new global low appear past N//3 ?
    late_updates = [(n, r_, v) for (n, r_, v) in running_trace if n > N // 3]
    return infs, running_trace, late_updates


def _worker(args):
    P, word, N, lo = args
    return P, word, sweep_nu2(word, N, lo)


def main():
    N = 20000
    lo = 100
    words = {3: [0, 0, 1], 5: [0, 0, 0, 0, 1],
             7: [0] * 6 + [1], 9: [0] * 8 + [1]}
    PERIODS = [3, 5, 7, 9]

    print("=" * 76)
    print("INFIMUM OF TRUE nu2(n)/n, RANGED, over n in [%d,%d]" % (lo, N))
    print("canonical cycle_and_nu2 (suffix starts at index>=2); exact ints")
    print("=" * 76)

    with Pool(len(PERIODS)) as pool:
        tmp = pool.map(_worker, [(P, words[P], N, lo) for P in PERIODS])
        results = {P: nu2_by_n for (P, _word, nu2_by_n) in tmp}

    for P in PERIODS:
        nu2_by_n = results[P]
        infs, trace, late = analyze(P, words[P], nu2_by_n, N, lo)
        print()
        print("--- P=%d word=%s ---" % (P, ''.join(map(str, words[P]))))
        for floor in (lo, 1000, 5000, 10000, 15000):
            if floor in infs:
                r, arg, v = infs[floor]
                print("    inf over [%6d,%d] = %.6f  @ n=%d (nu2=%d)"
                      % (floor, N, r, arg, v))
        print("    running-infimum updates (new lows / plateaus):")
        for (nn, rr, vv) in trace:
            print("      n=%-6d ratio=%.6f nu2=%d" % (nn, rr, vv))
        print("    new low set after n>%d (late-plateau/decay signal): %s"
              % (N // 3, "YES " + str(late) if late else "NO"))

    # ---------- independent brute-force comparison ----------
    print()
    print("=" * 76)
    print("INDEPENDENT ROUTE B (full-triangle brute force) vs ROUTE A (incremental)")
    print("=" * 76)
    all_ok = True
    for P in PERIODS:
        w = words[P]
        for trial_n in (300, 511, 1000, 2047, 4093):
            bfs = brute_force_nu2(w, trial_n)
            inc = results[P].get(trial_n)
            ok = (bfs == inc)
            all_ok &= ok
            print("  P=%d n=%-6d brute=%d incremental=%d  %s"
                  % (P, trial_n, bfs, inc, "OK" if ok else "MISMATCH"))
    print("ROUTE COMPARISON:", "ALL AGREE" if all_ok else "FAILED")

    # also reconcile against the anchored prime value direction: we cannot
    # hit 3999 cheaply for every period, so note the convention anchor.
    print()
    print("=" * 76)
    print("DECISIVE READ (CONFIRMED/REFUTED over n in [%d,%d] only):" % (lo, N))
    for P in PERIODS:
        nu2_by_n = results[P]
        infs, trace, late = analyze(P, words[P], nu2_by_n, N, lo)
        inf10000 = infs.get(10000)
        if inf10000 and inf10000[0] > 1e-4:
            print("  P=%d: inf over [10000,%d] = %.6f (bounded away from 0; "
                  "no late-plateau decay in range -> positive c plausible "
                  "for THIS word)" % (P, N, inf10000[0]))
        else:
            print("  P=%d: inf over [10000,%d] decays toward 0 or is 0 "
                  "-> NO uniform positive c" % (P, N))
    print()
    print("NOTE: periodic test words only; the primes are aperiodic. This "
          "measures whether the odd-factor converse is supply-useful on the "
          "periodic family, not Gilbreath itself.")


if __name__ == "__main__":
    main()
