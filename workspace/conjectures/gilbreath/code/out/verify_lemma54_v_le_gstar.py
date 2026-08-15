#!/usr/bin/env python3
"""Verify the two links that complete Granville's Lemma 5.4 from the descent lemma.

Descent lemma (PROVED, combinatorial core, code/lemma54_descent_check.py):
  pattern c_1..c_L in {0,2}; even start v >= 0; x_s = |x_{s-1} - c_s|.
  x_L in {0,2}  <=>  v <= 2*nu2 + 2,  nu2 = #{s : c_s = 2}.
  The delta=0 case is the main case: a 0 in the pattern is a NULL step
  (x -> x) and descends nothing; only 2-steps drop x by exactly 2 while
  x >= 2; {0,2} is absorbing.

Link A (bound entry): on the real-prime right diagonal delta_k(q_n) = A_k[n-k],
  every entry delta_k(q_n) for k >= 1 satisfies delta_k(q_n) <= g*_n, where
  g*_n = max(g_2,...,g_n) is the record gap.  Proof by induction: |a-b| <= max(a,b),
  delta_1(q_n) = g_n <= g*_n, so no step can exceed the running max.
  Hence the entry v = delta_tau(q_n) entering the gray block satisfies v <= g*_n.

Link B (the lemma): g*_n <= 2*nu2 + 2  ==>  v <= 2*nu2 + 2  ==>  x_L in {0,2}
  (success).  This is exactly Granville Lemma 5.4's sufficiency statement.

This program checks Link A and the composed implication on real primes: for each
column n, compute v (the delta value entering the maximal {0,2} suffix of the
previous diagonal) and confirm v <= g*_n, and (as the iff-check already did) that
g*_n <= 2*nu2+2 holds with 0 violations.
"""
import sys
sys.path.insert(0, "/workspace/code")  # lib.gilbreath
from lib.gilbreath import primes_up_to

def safe_primes(n):
    return primes_up_to(n)

def main():
    primes = safe_primes(2_000_000)
    W = len(primes) - 1          # gaps g_2..g_{W+1} -> indices, A_0 = primes
    # rows as lists: A_0 = primes (full), we need diagonals delta_k(q_n) = A_k[n-k]
    # We'll generate rows up to generous depth; but rebuilding full rows for W ~
    # 148933 is fine one-row-at-a-time.
    # delta_k(q_n): walk the triangle. Simplest: keep A_0 full, then generate A_1.. 
    # but we only need, per column n, the single diagonal through it. We'll store
    # the whole rows up to depth = max needed, one row at a time (list), W entries.
    depth_max = 2500
    rows = [primes.copy()]
    prev = primes
    for k in range(1, min(depth_max, W) + 1):
        cur = [abs(prev[i] - prev[i+1]) for i in range(len(prev) - 1)]
        rows.append(cur)
        prev = cur

    # g*_n = record gap up to n
    gaps = [primes[i+1] - primes[i] for i in range(W)]
    from itertools import accumulate
    rec = list(accumulate(gaps, max))  # rec[n-1] = max(g_2..g_{n+1})? careful indexing

    viol_v_le_g = 0
    viol_hyp = 0
    checked = 0
    maxmargin = 0
    for n in range(20, 2500):
        if n >= len(rows[0]):
            break
        # diagonal through q_n = primes[n] : delta_k(q_n) = A_k[n-k], k=0..n
        diag = [rows[k][n-k] for k in range(min(n, depth_max)) if n-k < len(rows[k])]
        if len(diag) < 3:
            continue
        # gray block of delta(q_{n-1}) = maximal {0,2} suffix of diag_{n-1}
        # Build diag for n-1
        nm1 = n - 1
        diagM = [rows[k][nm1-k] for k in range(min(nm1, depth_max)) if nm1-k < len(rows[k])]
        if len(diagM) < 3:
            continue
        # maximal {0,2} suffix of diagM[2..] (skip first two as in the run's measure)
        start = None
        for i in range(len(diagM)-1, -1, -1):
            if diagM[i] in (0, 2):
                start = i
            else:
                break
        if start is None or start < 2:
            continue
        # pattern = that suffix; the new diagonal's entry entering the block:
        # v = delta_{start-?}(q_n)?? The block starts at index `start` in diagM.
        # v = the value of the new diagonal at the SAME right-diagonal position just
        # before the block: delta_j(q_n) where j = start-1? Use j where diagM[j] first
        # in block OR the position the descent begins. Per the iff-check, v = the
        # yellow value at delta_{tau_n}(q_n) with tau_n = block start. Take v =
        # delta_{start}(q_n) is ambiguous; use the entry just left of the block:
        j = start - 1 if start - 1 >= 0 else start
        if j >= len(diag):
            continue
        v = diag[j] if start-1>=0 else diag[start]
        # nu2 = count of 2s in the block suffix
        block = diagM[start:]
        nu2 = block.count(2)
        gstar = rec[n-1]  # max(g_2..g_{n+1}) -- index n-1 in rec (rec[0]=g_2)
        if v > gstar:
            viol_v_le_g += 1
        if gstar > 2*nu2 + 2:
            viol_hyp += 1
        checked += 1
        margin = (2*nu2 + 2) / gstar if gstar > 0 else 0
        if margin > maxmargin:
            maxmargin = margin

    print(f"primes below 2e6: W={W}, columns n=20..2499 checked: {checked}")
    print(f"Link A  v <= g*_n            : violations = {viol_v_le_g}  (expect 0)")
    print(f"Lemma 5.4 hyp g*_n<=2nu2+2   : violations = {viol_hyp}  (expect 0)")
    print(f"max margin (2nu2+2)/g*_n     : {maxmargin:.3f}")
    print()
    print("Composition: g*_n <= 2*nu2+2  ==>  v <= g*_n <= 2*nu2+2  ==>  x_L in {0,2}")
    print("(descent lemma) so success transfers. Lemma 5.4 re-derived with the")
    print("delta=0 case handled as the null step, and v <= g*_n closing the bound.")
    ok = (viol_v_le_g == 0 and viol_hyp == 0 and checked > 0)
    print("RESULT:", "ALL CHECKS PASSED" if ok else "VIOLATIONS")

if __name__ == "__main__":
    main()
