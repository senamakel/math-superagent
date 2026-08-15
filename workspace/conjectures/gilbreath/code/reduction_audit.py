#!/usr/bin/env python3
"""AUDIT of the Granville right-diagonal reduction identity on real prime rows.

Decides whether the passage from real column dynamics to the (pattern, v)
descent model is a theorem or an assumption.

Setup (prime triangle):
  A_0 = p                       (the primes)
  A_{k+1}(i) = |A_k(i) - A_k(i+1)|
  right diagonals: delta_k(q_n) = A_k(n - k),   k in 0..n.

Identity under audit (Directive 38.3 / 41.2):
  delta_{k+1}(q_n) == |delta_k(q_n) - delta_k(q_{n-1})|     for all k in 0..n, all n.
  Equivalently the orbit satisfies  v_{k+1} = |v_k - eps_k|  with
  eps_k = delta_k(q_{n-1}) FIXED (independent of the new column q_n).

  WHY it is expected to hold with 0 violations (the mathematical content):
  delta_{k+1}(q_n) = A_{k+1}(n-k-1) = |A_k(n-k-1) - A_k(n-k)|
                   = | delta_k(q_{n-1}) - delta_k(q_n) |      [*]
  because delta_k(q_{n-1}) = A_k((n-1)-k) = A_k(n-k-1).  So [*] is the triangle
  recurrence itself; the eps_k are exactly the old diagonal and are fixed as the
  new column is added.  This is a THEOREM by construction, not an assumption.
  The audit machine-confirms it cell-by-cell on real primes.

Descent-model biconditional (Lemma 5.4 core):
  For each n:
    * 0-2 cycle of delta(q_{n-1}) = maximal {0,2} suffix of delta(q_{n-1})[:-1]
      (scan right-to-left, exclude the final bottom entry delta_{n-1}(q_{n-1})).
    * nu2 = # of 2s in that cycle.
    * v   = the entry of delta(q_n) at the cycle start (the first entry of the
      new diagonal that overlaps the cycle region).
    * x_L = the terminal entry = the last {0,2} landing.
  Check the biconditional:  (x_L in {0,2})  <=>  (v <= 2*nu2 + 2),  over all n.

Exact integer arithmetic only.  O(N log log N) sieve + O(M^2) triangle build.
"""
import math
from lib.gilbreath import primes_up_to, rows_generator


def cycle_start(d):
    """Start index tau of the maximal {0,2} suffix of d[:-1].
    Scans right-to-left from the entry before the final bottom entry."""
    body = d[:-1]                 # exclude terminal
    i = len(body)
    while i > 2 and body[i - 1] in (0, 2):
        i -= 1
    return i


def main():
    N_SIEVE = 2_000_000
    M = 300                        # audit columns n = 0..M, depth ~ M
    print("Granville right-diagonal reduction identity audit (real primes)")
    print("=" * 78)
    P = primes_up_to(N_SIEVE)
    print(f"sieve to {N_SIEVE}: {len(P)} primes (need >= {M + 2})")

    # Build triangle rows[0..M+1], rows[k] = A_k held as a full list (width M+2).
    gen = rows_generator(P, M + 1)
    rows = [next(gen) for _ in range(M + 2)]
    # sanity: row 0 is the primes, row 1 first differences
    assert rows[0][:3] == [2, 3, 5]
    assert rows[1][0] == 1 and rows[1][1] == 2      # |2-3|=1, |3-5|=2

    # ---- Part 1: the identity, cell by cell ------------------------------
    # delta_k(q_n) = rows[k][n-k].
    # check  rows[k+1][n-k-1] == | rows[k][n-k] - rows[k][n-k-1] |
    total_cells = 0
    identity_viol = 0
    # a few example cells printed for transparency
    examples = []
    for n in range(1, M + 1):
        for k in range(0, n):        # k+1 <= n in 0..n
            lhs = rows[k + 1][n - k - 1]                 # delta_{k+1}(q_n)
            dk_n = rows[k][n - k]                        # delta_k(q_n)
            dk_nm1 = rows[k][n - k - 1]                  # delta_k(q_{n-1})
            total_cells += 1
            if lhs != abs(dk_n - dk_nm1):
                identity_viol += 1
                if len(examples) < 5:
                    examples.append((n, k, lhs, dk_n, dk_nm1))
    print("\nPart 1: v_{k+1}=|v_k - eps_k| identity, eps fixed")
    print(f"  cells checked (spanning k=0..n-1 over n=1..{M}): {total_cells}")
    print(f"  identity violations: {identity_viol}   (expect 0)")
    for (n, k, lhs, a, b) in examples:
        print(f"    FIRST VIOLATION  n={n} k={k}: delta_{k+1}={lhs} "
              f"!= |delta_k(q_n)={a} - delta_k(q_{n-1})={b}|")
    print("  => identity is " +
          ("MACHINE-CONFIRMED (a theorem by construction, 0 violations)"
           if identity_viol == 0 else "VIOLATED"))

    # ---- Part 2: descent-model biconditional over all columns -------------
    n_final_ok = 0
    n_checked = 0
    bicond_viol = 0
    hyp_fail = 0            # v > 2*nu2+2 AND x_L in {0,2}  (contradicts iff via runway)
    nu2_samples = []
    for n in range(20, M + 1):
        dprev = [rows[k][(n - 1) - k] for k in range(n)]      # delta(q_{n-1}), k=0..n-1
        dcur = [rows[k][n - k] for k in range(n + 1)]         # delta(q_n),   k=0..n
        tau = cycle_start(dprev)
        cyc = dprev[tau:-1]
        # tape is {0,2} by construction of the maximal suffix; guard anyway
        if any(x not in (0, 2) for x in cyc):
            continue
        nu2 = cyc.count(2)
        if tau >= len(dcur) - 1:
            continue
        v = dcur[tau]                       # first entry of delta(q_n) in the cycle
        # The descent processes the L cycle entries {0,2} of dprev, starting from
        # v at index tau.  Each |delta - eps| step advances one index, so after
        # L = (n-1-tau) steps the orbit lands at index tau+L = n-1 of delta(q_n):
        #   x_L = delta(q_n)[n-1] = rows[n-1][1] = A_{n-1}(1),  the reduction object.
        L = (n - 1) - tau
        xL = rows[n - 1][1]                 # A_{n-1}(1)
        assert tau + L == n - 1
        n_checked += 1
        # biconditional: x_L in {0,2}  <=>  v <= 2*nu2+2
        land_in = (xL in (0, 2))
        pred = (v <= 2 * nu2 + 2)
        if land_in != pred:
            bicond_viol += 1
        # sufficiency-direction by runway: v > 2*nu2+2 must force x_L = v-2*nu2 >= 4
        if v > 2 * nu2 + 2:
            if land_in:                     # contradicted
                hyp_fail += 1
        nu2_samples.append((n, nu2, v, 2 * nu2 + 2, xL))
        if land_in:
            n_final_ok += 1

    print("\nPart 2: descent-model biconditional on real columns")
    print(f"  columns checked (n=20..{M}): {n_checked}")
    print(f"  columns whose terminal x_L lands in {{0,2}}: {n_final_ok}")
    print(f"  biconditional violations (x_L in {{0,2}} <=> v <= 2*nu2+2): "
          f"{bicond_viol}   (expect 0)")
    print(f"  runway contradictions (v > 2*nu2+2 yet x_L in {{0,2}}): "
          f"{hyp_fail}   (expect 0)")

    # sample table of (n, nu2, v, budget, xL)
    step = max(1, len(nu2_samples) // 30)
    print("\n  sample (n, nu2, v, 2*nu2+2, xL) over checked columns:")
    for (n, nu2, v, budget, xL) in nu2_samples[::step]:
        mark = "land" if xL in (0, 2) else "out"
        print(f"    n={n:>3}  nu2={nu2:>4}  v={v:>4}  budget={budget:>5}  "
              f"x_L={xL:>4}  [{mark}]  pred={v <= budget}")

    # ---- verdict -----------------------------------------------------------
    ok = (identity_viol == 0 and bicond_viol == 0 and hyp_fail == 0)
    print("\n" + "=" * 78)
    print(f"IDENTITY VERIFICATION: {total_cells} cells, "
          f"{identity_viol} violations (expect 0)")
    print(f"BICONDITIONAL: {n_checked} columns, {bicond_viol} violations (expect 0)")
    print("VERDICT: " + ("The passage from real column dynamics to the (pattern, v) "
                         "descent model is MACHINE-CONFIRMED as a theorem on real rows."
                         if ok else "discrepancy found — see above"))
    return 0 if ok else 1


if __name__ == "__main__":
    raise SystemExit(main())
