#!/usr/bin/env python3
"""Verify the two links that complete Granville's Lemma 5.4 from the descent lemma.
One row live at a time (O(depth*width) time, O(width) memory for the row; the
per-column diagonals are O(#columns * #depth) and are kept for the whole range).

Semantics follow the accepted independent verifier code/verify_granville_nu2_independent.py
(which in turn follows Granville's own code in the arXiv FULL PDF):

  right diagonal of column n:  delta_k(q_n) = A_k[n-k],  k = 0..n
      (delta_0(q_n)=q_n at the top, delta_n(q_n)=A_n(0)=1 the left edge).
  0-2 cycle of column n-1: the maximal {0,2} suffix of the body delta(q_{n-1})[:-1]
      (the terminal left-edge entry 1 excluded), scanned down to index 2.
      tau = start index of that cycle; nu2 = #{2} inside it.
  v = delta_tau(q_n)  (entry of the NEXT diagonal at the same tau) is the value
      entering the 0-2 cycle in the descent lemma.
  g*_n = max(g_2, ..., g_n),  g_k = p_k - p_{k-1}.

  Link A              : v <= g*_n  (the entering value is bounded by the largest gap).
  Lemma 5.4 hypothesis: g*_n <= 2*nu2 + 2.
  Margin              : (2*nu2 + 2) / g*_n  (> 1 = the hypothesis has slack).

This program reports these three quantities over real primes below 2e6 for
genuinely eligible columns n = 20..1200. Exact integers only.
"""
from lib.gilbreath import primes_up_to

NC = 1200          # highest column checked
NMIN = 20          # lowest column checked


def main():
    primes = primes_up_to(2_000_000)
    W = len(primes) - 1

    # g*_n = max(g_2..g_n): prefix max over the gap row (Granville convention,
    # identical to nu2_granville_check / verify_granville_nu2_independent).
    gaps = [primes[i + 1] - primes[i] for i in range(len(primes) - 1)]
    gstar = [0] * (NC + 2)
    mx = 0
    for n in range(1, NC + 2):
        mx = max(mx, gaps[n - 1])
        gstar[n] = mx

    # Build the right diagonals one row at a time.
    # diag[n][k] = A_k[n-k] for k = 0..n (k=n is the left edge A_n(0)=1).
    diag = {n: [] for n in range(NMIN - 1, NC + 1)}
    row = primes
    for k in range(0, NC + 1):
        for j, val in enumerate(row):
            n = j + k
            if n in diag and k <= n:
                diag[n].append(val)
        if k < NC:
            row = [abs(row[i] - row[i + 1]) for i in range(len(row) - 1)]

    def cycle_start(d):
        # maximal {0,2} suffix of the body (excluding the left-edge terminal
        # entry), scanned down to index 2.
        body = d[:-1]
        i = len(body)
        while i > 2 and body[i - 1] in (0, 2):
            i -= 1
        return i

    viol_v_le_g = 0     # Link A: v <= g*_n
    viol_hyp = 0        # Lemma 5.4 hypothesis: g*_n <= 2*nu2+2
    checked = 0
    maxmargin = 0.0
    eligible_examples = []
    for n in range(NMIN, NC + 1):
        dprev = diag[n - 1]
        dcur = diag[n]
        tau = cycle_start(dprev)
        cyc = dprev[tau:-1]
        if any(x not in (0, 2) for x in cyc):
            # the maximal suffix should be all-{0,2} by construction
            continue
        nu2 = cyc.count(2)
        if tau >= len(dcur) - 1:
            continue
        v = dcur[tau]
        g = gstar[n]
        checked += 1
        if v > g:
            viol_v_le_g += 1
        if g > 2 * nu2 + 2:
            viol_hyp += 1
        margin = (2 * nu2 + 2) / g if g > 0 else 0.0
        if margin > maxmargin:
            maxmargin = margin
        if len(eligible_examples) < 5:
            eligible_examples.append((n, tau, len(cyc), nu2, v, g))

    print(f"primes below 2e6: W={W} gaps, columns n={NMIN}..{NC} checked: {checked}")
    print(f"Link A  v <= g*_n                 : violations = {viol_v_le_g}  (expect 0)")
    print(f"Lemma 5.4 hypothesis g*_n<=2nu2+2 : violations = {viol_hyp}  (expect 0)")
    print(f"max margin (2nu2+2)/g*_n          : {maxmargin:.3f}")
    if eligible_examples:
        print("sample eligible columns (n, tau, |cycle|, nu2, v, g*_n):")
        for e in eligible_examples:
            print("   ", e)
    print()
    print("Composition: g*_n <= 2nu2+2  ==>  v <= g*_n <= 2nu2+2  ==>  x_L in {0,2}")
    print("(descent lemma), so success transfers row to row.")
    ok = (viol_v_le_g == 0 and viol_hyp == 0 and checked > 0)
    print("RESULT:", "ALL CHECKS PASSED" if ok else "VIOLATIONS")
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
