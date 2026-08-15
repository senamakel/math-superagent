#!/usr/bin/env python3
"""
Investigate reduction_audit.py section (D): the 1133 reported violations of
the "constant-1 erosion law"  c_n >= c_{n-1} - 1  in DIAGONAL coordinates,
where c_n = length of the maximal {0,2} suffix ("0-2 cycle") of the
anti-diagonal delta(q_n), excluding its bottom entry.

Question: is this a genuine phenomenon or a bug / convention error?
Deciding test, three parts:

  (i)  build diagonals EXACTLY as the audit does (same primes, same
       incremental recurrence, same zero_two_suffix_length), and report the
       FIRST few violating n with c_{n-1}, c_n, and the full {0,2}-cycle
       (suffix) of delta(q_{n-1}) and delta(q_n) so the drop can be inspected
       by hand;

  (ii) the value that BROKE the cycle: the first non-{0,2} entry going up the
       new diagonal from the bottom.  Is it a 4+ even (a large value entering
       near the bottom, i.e. a regeneration concern) or something innocuous?
       The bottom entry itself (leading column 0 of its row, == A_{n-1}(0)) is
       recorded separately: it is 1 iff the leading-entry conjecture holds.

 (iii) independent recomputation in ROW coordinates from lib.gilbreath: build
       the full A-triangle, count the leading {0,2} block b_k = block_profile
       (= A000232(k)-1) of each row, and check whether the PROVED row law
       b_k >= b_{k-1} - 1 holds with 0 violations over the same range.

The structural point tested: an anti-diagonal's consecutive cells are NOT
difference-pairs (cell (r,j) and (r-1,j+1) both live on diagonal n but are not
|a-b| of each other), whereas a row's consecutive cells ARE.  So the {0,2}
closure that makes the row law true does not transfer to the diagonal suffix.
We verify that directly by comparing the two laws over the same range.
"""
import sys
from collections import Counter
from lib.gilbreath import primes_up_to, rows_generator, block_profile


def build_diagonals(ps, N):
    """Incremental right diagonals, EXACTLY as reduction_audit.py builds them.
    delta(q_n) has length n; delta_0(q_n)=q_n, delta_k(q_n)=|delta_{k-1}(q_n)
    - delta_{k-1}(q_{n-1})|.  Keeps all diagonals (needed to print cycles)."""
    prev = None
    diags = [None]  # 1-indexed
    for n in range(1, N + 1):
        qn = ps[n - 1]
        cur = [0] * n
        cur[0] = qn
        if prev is not None:
            for k in range(1, n):
                cur[k] = abs(cur[k - 1] - prev[k - 1])
        diags.append(cur)
        prev = cur
    return diags


def zero_two_suffix_length(vec, exclude_last=False):
    """Audit's exact definition: length of maximal suffix of vec all in {0,2}.
    If exclude_last: skip the trailing (bottom) entry first."""
    end = len(vec)
    if exclude_last:
        end -= 1
    i = end - 1
    while i >= 0 and vec[i] in (0, 2):
        i -= 1
    return end - 1 - i


def cycle_of(vec, exclude_last=True):
    """The {0,2}-suffix of vec as an actual list (the audit's '0-2 cycle')."""
    end = len(vec)
    if exclude_last:
        end -= 1
    i = end - 1
    while i >= 0 and vec[i] in (0, 2):
        i -= 1
    return vec[i + 1:end]


def main():
    N = 10001
    LIM = 200000
    ps = primes_up_to(LIM)[:N]
    N = len(ps)
    print(f"primes used: {N} (largest {ps[-1]})")

    # ---------------- (i) build diagonals exactly as the audit ----------------
    diags = build_diagonals(ps, N)
    c = [0] * (N + 1)
    for n in range(2, N + 1):
        c[n] = zero_two_suffix_length(diags[n], exclude_last=True)

    # reconstruct the audit's numeric result
    dist = Counter()
    viol = []
    for n in range(3, N + 1):
        d = c[n] - c[n - 1]
        dist[d] += 1
        if d < -1:
            viol.append(n)
    print(f"(i) diagonal law c_n >= c_{{n-1}} - 1: violations = {len(viol)} "
          f"over {N - 2} extensions   [{dist[-1]} erode-by-1, {dist[0]} stay, "
          f"grow={sum(v for d, v in dist.items() if d > 0)}]")

    print("\n(i) FIRST 10 VIOLATIONS, with full 0-2 cycles:")
    shown = 0
    for n in viol[:10]:
        cp, cn = c[n - 1], c[n]
        dp = diags[n - 1]
        dc = diags[n]
        cyc_p = cycle_of(dp, True)
        cyc_c = cycle_of(dc, True)
        # positions of the cycles within each diagonal
        lo_p = (n - 1 - 1) - cp          # cycle of prev occupies indices lo_p..n-3
        # first non-{0,2} entry up the NEW diagonal (just above its cycle)
        stopper_idx = (n - 1 - 1) - cn    # index in cur of first non-{0,2} up
        stopper_val = dc[stopper_idx] if stopper_idx >= 0 else None
        bottom = dc[-1]                   # A_{n-1}(0), leading entry of row n-1
        print(f"\n  n={n}: c_{n - 1}={cp} c_{n}={cn}  d={cn - cp}")
        print(f"    bottom entry (=A_{n - 1}(0)) = {bottom}")
        print(f"    first non-{{0,2}} up new diag at idx {stopper_idx} = {stopper_val}"
              f"  (>=4? {stopper_val is not None and stopper_val >= 4})")
        print(f"    delta(q_{n - 1}) 0-2 cycle [{cp} cells]: {cyc_p}")
        print(f"    delta(q_{n})   0-2 cycle [{cn} cells]: {cyc_c}")
        shown += 1

    # break the cycle stopper values over ALL violations
    stop_counter = Counter()
    regen_ok = True   # every diagonal's bottom entry 1?
    for n in range(2, N + 1):
        if diags[n][-1] != 1:
            regen_ok = False
    for n in viol:
        cn = c[n]
        stopper_idx = (n - 2) - cn
        if stopper_idx >= 0:
            stop_counter[diags[n][stopper_idx]] += 1
        else:
            stop_counter['<none>'] += 1
    print(f"\n(i) ALL-violations stopper-value distribution "
          f"(first non-{{0,2}} above the new cycle): {dict(stop_counter)}")
    n4 = sum(v for k, v in stop_counter.items()
             if isinstance(k, int) and k >= 4)
    print(f"    stoppers that are 4+ even: {n4} of {len(viol)}; "
          f"bottom entry 1 on every diagonal: {regen_ok}")

    # how big are the drops?
    drops = Counter(c[n] - c[n - 1] for n in viol)
    print(f"    drop magnitudes among violations: {dict(sorted(drops.items()))}")
    # cycles are spread over multiple rows (columns 1..c in distinct rows)
    if viol:
        n0 = viol[0]
        cn0 = c[n0]
        rows_touched = list(range(n0 - 2, n0 - 1 - cn0, -1))
        print(f"    e.g. n={n0}: its {cn0} cycle cells live in {len(rows_touched)} "
              f"DIFFERENT rows {rows_touched} (columns 1..{cn0}) -- not one row's block")

    # ---------------- (iii) independent ROW-coordinate recomputation ----------
    depth = N - 1
    gen = rows_generator(ps, depth)
    b = []
    for row in gen:
        b.append(block_profile(row))
    # b[k] for row A_k, k=0..N-1
    row_viol = 0
    first_row_viol = None
    for k in range(1, len(b)):
        if b[k] < b[k - 1] - 1:
            row_viol += 1
            if first_row_viol is None:
                first_row_viol = k
    print(f"\n(iii) ROW-coordinate law b_k >= b_{{k-1}} - 1 over rows 0..{len(b) - 1}: "
          f"violations = {row_viol}")
    print(f"      b[0..12] = {b[:13]}")
    print(f"      (block_profile = A000232(k)-1, the leading {{0,2}} block length)")

    # exact conjecture quantity in diagonal coords: delta(q_n)[n-2] = A_{n-2}(1)
    # (second entry of row A_{n-2}), which must be in {0,2} for k = n-2 >= 1,
    # i.e. n >= 3.  n=2's cell is A_0(1)=3 (the base row of primes -- not a
    # conjecture target), so it is excluded here.
    second_bad = [n for n in range(3, N + 1) if diags[n][n - 2] not in (0, 2)]
    c_zero_ok = all(diags[n][n - 2] in (0, 2)
                    for n in range(3, N + 1) if c[n] == 0)
    print(f"\n(extra) second entry A_{{n-2}}(1)=delta(q_n)[n-2] in {{0,2}} "
          f"for all n=3..{N} (conjecture form): "
          f"{'YES' if not second_bad else 'NO -- ' + str(second_bad[:10])}")
    print(f"(extra) min c_n = {min(c[2:])}; at every n>=3 with c_n==0 "
          f"A_{{n-2}}(1) in {{0,2}} still holds: {c_zero_ok}")

    # same range: anti-diagonals n=3..N-1 correspond to rows up to A_{N-1}
    # (delta(q_n) bottom = A_{n-1}(0)); row law over all rows is the strongest form.
    print(f"\nsummary: diagonal-law violations {len(viol)} vs row-law violations "
          f"{row_viol} over the same prime range -> "
          f"{'row law is the proved one, diagonal c_n is transversal (artifact)' if row_viol == 0 else 'both fail'}")


if __name__ == "__main__":
    main()
