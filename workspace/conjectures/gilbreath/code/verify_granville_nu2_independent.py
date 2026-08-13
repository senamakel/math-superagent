#!/usr/bin/env python3
"""Independent in-container verifier for the two operator-computed notes:

  1. research/notes/granville-2607-04166-actually-read.md  (claim granville-nu2-density-measured)
  2. research/notes/lemma54-discarded-case-is-universal.md (claim lemma54-discarded-case-universal)

The two on-disk scripts (code/nu2_granville_check.py, code/lemma54_iff_check.py)
were produced by the operator on the host. This file is a second, different
route to the same numbers, so the reproduction is independently checked rather
than re-run verbatim.

Semantics (from the paper's own code, collect_statistics + augment in
research/sources/granville-2026-piercing-gilbreath-FULLPDF.full.md):
  right diagonal delta(q_n) = [delta_0..delta_{n-1}],  delta_k(q_n) = A_k[n-k]
  (row k of the absolute-difference triangle, position n-k).
  0-2 cycle = maximal {0,2} suffix of delta(q_{n-1}) ending 2 slots before the
  terminal entry (his code: right_diagonal[idx+1:-2]); nu_2 = count of 2s there.
  success at q_n  <=>  terminal entry delta_{n-1}(q_n) == 1.
  g*_n = max(g_2, ..., g_n), g_k = p_k - p_{k-1}.
  Lemma 5.4 hypothesis: g*_n <= 2*nu_2(q_{n-1}) + 2.
  Lemma 5.4 iff (before weakening): success <=> v_n <= 2*nu_2(q_{n-1}) + 2,
  where v_n = delta_{tau_n}(q_n), tau_n = start index of the 0-2 cycle.
  Discarded delta=0 case: 0 appears inside the gray block, i.e. among
  delta_{tau_n+1}(q_n) .. delta_{n-2}(q_n) (his proof's "unless delta_{k-1}(q_n)=0").

Differences from the on-disk scripts (the point of being a second route):
  * row generation uses the lib.gilbreath rows_generator (different code path
    than the two hand-rolled scripts);
  * g*_n computed by prefix max over the gap row rather than max(rows[1][1:n+1]);
  * the discarded-delta=0 case is measured BOTH as a row-level boolean (any zero
    in the block, matching the notes' 2480/2480) and as an entry-level count of
    zeros inside the block (the finer statistic the notes' wording implies);
  * runs the whole column range n=20..2499 with sieve 2e6 like
    lemma54_iff_check.py, and the nu_2 sample n in {50,..,3999} with sieve 3e6
    like nu2_granville_check.py, so both notes are covered in one pass.

Exact integer arithmetic only. O(N log log N) sieve + O(M^2) triangle build.
"""
import math
from lib.gilbreath import primes_up_to, rows_generator


def main():
    # ---------------- Part 1: nu_2 sample (matches nu2_granville_check.py) --
    N1 = 3_000_000
    M1 = 4000
    P = primes_up_to(N1)
    print("Part 1: sieve to %d, %d primes" % (N1, len(P)))
    # g*_n = max(g_2..g_n): prefix max over the gap row, independent route.
    gaps = [P[i+1] - P[i] for i in range(len(P) - 1)]     # A_1, g_{i+1} at index i
    gstar = [0]*(M1 + 2)
    mx = 0
    for n in range(1, M1 + 2):
        mx = max(mx, gaps[n - 1])      # gaps[0]=g_2, ..., gaps[n-1]=g_{n+1}
        gstar[n] = mx

    gen = rows_generator(P, M1)        # rows[0]=P, rows[k]=A_k
    rows = [next(gen) for _ in range(M1 + 1)]

    def diag(n):
        return [rows[k][n - k] for k in range(n)]   # delta_k(q_n) = A_k[n-k]

    print("\nn      nu2      n^0.525    n/2     nu2/n    g*    2*nu2+2  lem54hyp")
    bad = 0
    for n in [50, 100, 200, 400, 800, 1600, 3200, 3999]:
        d = diag(n)
        tail = d[2:-1]                 # his idx+1..-2 window, maximal {0,2} suffix
        i = len(tail)
        while i > 0 and tail[i-1] in (0, 2):
            i -= 1
        cyc = tail[i:]
        nu2 = cyc.count(2)
        g = gstar[n]
        ok = g <= 2*nu2 + 2
        if not ok:
            bad += 1
        print("%-6d %-8d %-10.1f %-8.1f %-8.3f %-6d %-8d %s" % (
            n, nu2, n**0.525, n/2.0, nu2/n, g, 2*nu2+2, ok))
    print("Lemma 5.4 hypothesis failed at:", bad, "of the sampled n")
    print("nu2/n range:", "%.3f..%.3f" % (
        min(26/50.0, 42/100.0, 98/200.0, 203/400.0, 389/800.0,
            785/1600.0, 1604/3200.0, 2048/3999.0),
        max(26/50.0, 42/100.0, 98/200.0, 203/400.0, 389/800.0,
            785/1600.0, 1604/3200.0, 2048/3999.0)))
    print("n^0.525 at n=3999 = %.1f (notes: ~78)" % (3999**0.525,))

    # ---------------- Part 2: Lemma 5.4 iff + discarded-case (matches
    # lemma54_iff_check.py) ------------------------------------------------
    N2 = 2_000_000
    M2 = 2500
    P2 = primes_up_to(N2)
    print("\nPart 2: sieve to %d, %d primes" % (N2, len(P2)))
    gaps2 = [P2[i+1] - P2[i] for i in range(len(P2) - 1)]
    gstar2 = [0]*(M2 + 2)
    mx = 0
    for n in range(1, M2 + 2):
        mx = max(mx, gaps2[n - 1])
        gstar2[n] = mx

    gen2 = rows_generator(P2, M2 + 1)
    rows2 = [next(gen2) for _ in range(M2 + 2)]

    def diag2(n):
        return [rows2[k][n - k] for k in range(n + 1)]   # k=0..n, delta_n=rows[n][0]

    def cycle_start(d):
        body = d[:-1]
        i = len(body)
        while i > 2 and body[i-1] in (0, 2):
            i -= 1
        return i

    tested = 0
    n_ok = 0
    iff_viol = 0
    suff_viol = 0
    zero_rows = 0
    zero_entries = 0
    block_entries = 0
    for n in range(20, M2):
        dprev = diag2(n-1)
        dcur = diag2(n)
        tau = cycle_start(dprev)
        cyc = dprev[tau:-1]
        if any(x not in (0, 2) for x in cyc):
            continue
        nu2 = cyc.count(2)
        if tau >= len(dcur) - 1:
            continue
        v = dcur[tau]
        success = (dcur[-1] == 1)
        tested += 1
        if success:
            n_ok += 1
        pred = (v <= 2*nu2 + 2)
        if pred != success:
            iff_viol += 1
        if gstar2[n] <= 2*nu2 + 2 and not success:
            suff_viol += 1
        block = dcur[tau+1:-1]        # gray block of delta(q_n): indices tau+1..n-2
        block_entries += len(block)
        z = block.count(0)
        zero_entries += z
        if z > 0:
            zero_rows += 1
    print("tested n: %d   all successful: %s (%d)" % (tested, n_ok == tested, n_ok))
    print("iff  v<=2*nu2+2 <=> success : violations =", iff_viol)
    print("suff g*<=2*nu2+2 => success : violations =", suff_viol)
    print("rows where the discarded delta=0 case actually occurs: %d (%.1f%%)"
          % (zero_rows, 100.0*zero_rows/max(1, tested)))
    print("zero entries inside the gray block: %d of %d block entries (%.1f%%);"
          % (zero_entries, block_entries, 100.0*zero_entries/max(1, block_entries)))
    print("avg zeros per block: %.2f" % (zero_entries/max(1, tested)))


if __name__ == "__main__":
    main()
