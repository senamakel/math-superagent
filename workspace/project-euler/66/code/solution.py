#!/usr/bin/env python3
"""Project Euler 66 - primary method: exact-integer continued-fraction convergents.

Problem restatement
-------------------
For every non-square D with 1 <= D <= 1000, let (x_D, y_D) be the minimal
(fundamental) positive integer solution of the Pell equation

        x^2 - D y^2 = 1.

Square D have no positive solution: x^2 - k^2 y^2 = 1 would force
(x - ky)(x + ky) = 1, hence y = 0.  Find the D <= 1000 whose minimal x_D is
largest.

Governing theory (why the method works)
---------------------------------------
1. Lagrange's theorem: for non-square D, the simple continued fraction of
   sqrt(D) is eventually periodic (in fact purely periodic after a_0):

        sqrt(D) = [a_0; a_1, ..., a_{L-1}, 2a_0],     a_0 = isqrt(D),

   with period length L >= 1.  All inner partial quotients a_k (1 <= k < L)
   satisfy 1 <= a_k <= a_0, and the first k >= 1 with a_k = 2 a_0 is k = L.

2. Fundamental solution is a convergent: with p_n/q_n the convergents
   (p_-2 = 0, p_-1 = 1, q_-2 = 1, q_-1 = 0, and
   p_n = a_n p_{n-1} + p_{n-2}, q_n = a_n q_{n-1} + q_{n-2}), the norm
   p_n^2 - D q_n^2 satisfies

        p_{L-1}^2 - D q_{L-1}^2 = (-1)^L,

   and the FIRST convergent whose norm equals +1 is exactly the fundamental
   solution of x^2 - D y^2 = 1: it occurs at index L-1 when L is even and at
   index 2L-1 when L is odd (odd L: the norm -1 unit at index L-1 is squared
   into a norm +1 unit at 2L-1, p_{2L-1} = p_{L-1}^2 + D q_{L-1}^2,
   q_{2L-1} = 2 p_{L-1} q_{L-1}).  By Dirichlet's unit structure all positive
   solutions are powers of this unit, so "first convergent with norm +1" is
   the minimal solution in x (and in y).

Algorithm (per non-square D): exact-integer CF iteration, no floats, no search
over x or y; termination guaranteed within two periods (index <= 2L - 1).

Complexity
----------
Per D: O(L) big-integer recurrence steps, L = O(sqrt D) (period length).
Total over all non-square D <= 1000: on the order of 10^4-10^5 exact integer
operations.  Space: O(1) big integers per D.  No exponential time or space;
the cost depends on the input D, not on the size of the answer.
"""

import math
import time


def _solve(D):
    """(x, y, n) = fundamental solution of x^2 - D y^2 = 1 and its
    convergent index n.  Returns None for square D.

    n is the index of the convergent p_n/q_n that carries the fundamental
    solution; it is tracked for the independent period-parity cross-check.
    """
    a0 = math.isqrt(D)
    if a0 * a0 == D:
        return None

    # CF state: at iteration k we hold a_{k-1} in a, and the convergent
    # p_{k-1}/q_{k-1} in p/q, with p_m1/q_m1 = p_{k-2}/q_{k-2} and
    # p_m2/q_m2 = p_{k-3}/q_{k-3}.
    m, d, a = 0, 1, a0                 # m_0 = 0, d_0 = 1, a_0
    p_m2, p_m1 = 0, 1                  # p_{-2}, p_{-1}
    q_m2, q_m1 = 1, 0                  # q_{-2}, q_{-1}
    p, q = a0, 1                       # convergent p_0/q_0 = a_0/1
    # Norm at index 0 is a0^2 - D < 0 for non-square D, so never 1:
    assert p * p - D * q * q != 1

    cap = 4 * a0 + 100                 # generous pure bug-check guard
    for n in range(1, cap + 1):        # iteration n = 1, 2, ...
        m2 = d * a - m                 # m_n from m_{n-1}, d_{n-1}, a_{n-1}
        assert (D - m2 * m2) % d == 0, f"D={D} n={n}: exactness violated"
        d2 = (D - m2 * m2) // d        # exact division, guaranteed by theory
        assert d2 > 0, f"D={D} n={n}: d2 <= 0"
        a2 = (a0 + m2) // d2           # a_n

        # convergent n:  p_n = a_n*p_{n-1} + p_{n-2},  q_n = a_n*q_{n-1} + q_{n-2}
        pk = a2 * p + p_m1
        qk = a2 * q + q_m1
        if pk * pk - D * qk * qk == 1:
            return (pk, qk, n)

        # shift: the current convergent becomes p_n = pk, so the stored
        # back-convergents become p_{n-1} (= old p) and p_{n-2} (= old p_m1).
        p_m1, p_m2 = p, p_m1
        p = pk
        q_m1, q_m2 = q, q_m1
        q = qk
        m, d, a = m2, d2, a2

    raise RuntimeError(
        f"pe66_cf({D}): cap of {cap} CF steps exceeded (bug check; "
        "termination at index <= 2L-1 is guaranteed by theory)"
    )


def pe66_cf(D):
    """Fundamental solution (x, y) of x^2 - D y^2 = 1, or None for square D.

    Primary method: exact-integer continued-fraction convergents.
    """
    r = _solve(D)
    return None if r is None else (r[0], r[1])


def cf_period_length(D):
    """Period length L of the continued fraction of sqrt(D), D non-square.

    Independent detection (used only as a cross-check): the first k >= 1 with
    a_k = 2*a_0 is k = L (classical; inner partial quotients are <= a_0).
    """
    a0 = math.isqrt(D)
    m, d, a = 0, 1, a0
    L = 0
    while True:
        m2 = d * a - m
        d2 = (D - m2 * m2) // d
        a2 = (a0 + m2) // d2
        L += 1
        if a2 == 2 * a0:
            return L
        m, d, a = m2, d2, a2


def main():
    t0 = time.perf_counter()

    # ------------------------------------------------------------------
    # 1. Test-oracle self-check (BEFORE the full run)
    # ------------------------------------------------------------------
    oracle = {
        2: (3, 2),
        3: (2, 1),
        5: (9, 4),
        6: (5, 2),
        7: (8, 3),
        13: (649, 180),
    }
    for D in sorted(oracle):
        ex, ey = oracle[D]
        x, y = pe66_cf(D)
        assert (x, y) == (ex, ey), (
            f"oracle mismatch D={D}: got ({x},{y}), expected ({ex},{ey})"
        )
        assert x * x - D * y * y == 1, f"oracle norm check failed D={D}"
        print(f"oracle PASS D={D}: (x, y) = ({x}, {y})")

    # small-range argmax over non-square D <= 7
    small = []
    for D in range(2, 8):
        r = pe66_cf(D)
        if r is not None:
            small.append((D, r))
    sD, (sx, sy) = max(small, key=lambda t: t[1][0])
    assert sD == 5 and sx == 9, f"small-range argmax mismatch: D={sD}, x={sx}"
    print("small-range argmax PASS, D=5, x=9")

    # ------------------------------------------------------------------
    # 2. Full run: every non-square D in 1..1000
    # ------------------------------------------------------------------
    rows = []            # (D, x, y) in increasing D
    best = None          # (x, y, D) with largest minimal x
    tie_Ds = []          # D's sharing the maximal minimal x (if any)
    count = 0
    for D in range(1, 1001):
        r = pe66_cf(D)
        if r is None:
            continue
        x, y = r
        assert x * x - D * y * y == 1, f"full-run norm check failed for D={D}"
        count += 1
        rows.append((D, x, y))
        if best is None or x > best[0]:
            best = (x, y, D)
            tie_Ds = [D]
        elif x == best[0]:
            tie_Ds.append(D)

    with open("results_cf.tsv", "w", encoding="ascii", newline="\n") as fh:
        fh.write("D\tx\ty\n")
        for D, x, y in rows:
            fh.write(f"{D}\t{x}\t{y}\n")

    bx, by, bD = best
    assert bx * bx - bD * by * by == 1
    digits = len(str(bx))

    # ------------------------------------------------------------------
    # 3. Independent cross-check: fundamental-solution index rule.
    # For every non-square D, the convergent index n at which the norm first
    # reaches +1 must equal L-1 (L even) or 2L-1 (L odd), with L the CF
    # period length detected independently.  This verifies, on every D, that
    # the returned pair is the fundamental (minimal-x) solution, not merely
    # a solution.
    # ------------------------------------------------------------------
    parity_ok = True
    for D in range(1, 1001):
        if _solve(D) is None:
            continue
        x, y, n = _solve(D)
        L = cf_period_length(D)
        expected = (L - 1) if (L % 2 == 0) else (2 * L - 1)
        if n != expected:
            parity_ok = False
            print(f"PERIOD-PARITY MISMATCH: D={D}, n={n}, L={L}, expected={expected}")
    if parity_ok:
        print(f"period-parity index rule PASS for all {count} non-square D")

    t1 = time.perf_counter()
    elapsed = t1 - t0

    # ------------------------------------------------------------------
    # 4. Report
    # ------------------------------------------------------------------
    if len(tie_Ds) > 1:
        print(f"TIE NOTE: maximal minimal x = {bx} occurs at D in {tie_Ds}")
    print(f"ANSWER D = {bD}  (minimal x = {bx}, minimal y = {by})")
    print(
        f"SUMMARY: {count} non-square D in 1..1000; winning x has {digits} "
        f"digits; wall-clock {elapsed:.3f} s"
    )


if __name__ == "__main__":
    main()