#!/usr/bin/env python3
"""
solution_power.py - O(1)-per-frame power-sum summation for PE 579.

Reuses the EXACT primitive-frame enumeration from frame_method.py (imported, so
it is bit-for-bit the same enumeration).  ONLY the summation differs: instead of
looping over t=1..tmax, we expand

    T(t)  = (X - A t)(X - B t)(X - C t)          (X = n+1)
          = p0 + p1 t + p2 t^2 + p3 t^3

    pts(t) = ell^3 t^3 + ell*D t^2 + D t + 1
           = q0 + q1 t + q2 t^2 + q3 t^3

    g(t)   = pts(t)*T(t) = c0 + c1 t + ... + c6 t^6   (degree 6)

and use exact integer Faulhaber power sums

    P_j(n) = sum_{t=1}^{n} t^j

so that

    C-contribution = sum_{j=1..3} pj * P_j(tmax)        (plus p0*tmax = p0*P_0)
    S-contribution = sum_{k=0..6} ck * P_k(tmax).

Cost per frame is O(1) (a constant number of integer multiplications), so it no
longer grows with n.  No floats anywhere.

Usage:  python3 solution_power.py
Writes evidence to /workspace/power_validate.txt and prints it.
"""
import time

from frame_method import (
    enumerate_primitive_frames,
    enumerate_primitive_frames_lean,
    compute,
)


# ---------------------------------------------------------------------------
# Faulhaber power sums, exact integer, k = 0..6
# ---------------------------------------------------------------------------
def P(k, n):
    """P(k, n) = sum_{t=1}^{n} t^k, exact integer, for k in 0..6.

    Closed forms (standard Faulhaber), each exactly divisible for all n:
      P0 = n
      P1 = n(n+1)/2
      P2 = n(n+1)(2n+1)/6
      P3 = [n(n+1)/2]^2
      P4 = n(n+1)(2n+1)(3n^2+3n-1)/30
      P5 = n^2(n+1)^2(2n^2+2n-1)/12
      P6 = n(n+1)(2n+1)(3n^4+6n^3-3n+1)/42
    """
    if k == 0:
        return n
    a = n * (n + 1)
    if k == 1:
        return a // 2
    b = a * (2 * n + 1)
    if k == 2:
        return b // 6
    if k == 3:
        return (a // 2) * (a // 2)
    if k == 4:
        return b * (3 * n * n + 3 * n - 1) // 30
    if k == 5:
        return (n * n) * (n + 1) ** 2 * (2 * n * n + 2 * n - 1) // 12
    # k == 6
    return a * (2 * n + 1) * (3 * n ** 4 + 6 * n ** 3 - 3 * n + 1) // 42


def faulhaber_polys():
    """Return the 7 closed forms as (coeffs, denominator) for audit/printing."""
    forms = {
        0: ("n", 1),
        1: ("n(n+1)/2", 2),
        2: ("n(n+1)(2n+1)/6", 6),
        3: ("[n(n+1)/2]^2", 4),
        4: ("n(n+1)(2n+1)(3n^2+3n-1)/30", 30),
        5: ("n^2(n+1)^2(2n^2+2n-1)/12", 12),
        6: ("n(n+1)(2n+1)(3n^4+6n^3-3n+1)/42", 42),
    }
    return forms


# ---------------------------------------------------------------------------
# O(1) power-sum summation (the ONLY change vs frame_method.compute)
# ---------------------------------------------------------------------------
def compute_power(n, frames):
    """Return (C(n), S(n)) using O(1)-per-frame power sums. Exact integers."""
    X = n + 1
    C = 0
    S = 0
    for (ell, A, B, Cc, D) in frames.values():
        tmax = n
        if A > 0:
            tmax = min(tmax, n // A)
        if B > 0:
            tmax = min(tmax, n // B)
        if Cc > 0:
            tmax = min(tmax, n // Cc)
        if tmax <= 0:
            continue

        # T(t) coefficients
        pa = A + B + Cc         # sum of spans
        pb = A * B + A * Cc + B * Cc
        pc = A * B * Cc
        p0 = X ** 3
        p1 = -X * X * pa
        p2 = X * pb
        p3 = -pc

        # pts(t) coefficients
        q0 = 1
        q1 = D
        q2 = ell * D
        q3 = ell ** 3

        # g(t) = pts(t)*T(t) coefficients (convolution, degree 6)
        c = [0] * 7
        for i in range(4):      # index of q
            qi = (q0, q1, q2, q3)[i]
            for j in range(4):  # index of p
                c[i + j] += qi * (p0, p1, p2, p3)[j]

        # C-contribution = sum_{t=1..tmax} T(t) = p0*P0 + p1*P1 + p2*P2 + p3*P3
        ccontrib = p0 * P(0, tmax) + p1 * P(1, tmax) \
            + p2 * P(2, tmax) + p3 * P(3, tmax)
        # S-contribution = sum_{k=0..6} ck * P(k, tmax)
        scontrib = sum(c[k] * P(k, tmax) for k in range(7))

        C += ccontrib
        S += scontrib
    return C, S


# ---------------------------------------------------------------------------
# Direct loop version (identical to frame_method.compute), for equivalence check
# ---------------------------------------------------------------------------
def compute_direct(n, frames):
    """Direct t-loop summation (same as frame_method.compute). For comparison."""
    return compute(n, frames)


# ---------------------------------------------------------------------------
# Oracle
# ---------------------------------------------------------------------------
ORACLE_C = {1: 1, 2: 9, 4: 100, 5: 229, 10: 4469, 50: 8154671}
ORACLE_S = {1: 8, 2: 91, 4: 1878, 5: 5832, 10: 387003, 50: 29948928129}


def main():
    lines = []
    def emit(s):
        print(s)
        lines.append(s)

    # Verify Faulhaber formulas against a literal loop for k=0..6, n up to 200
    faulher_ok = True
    for k in range(7):
        for n in range(0, 201):
            expect = sum(t ** k for t in range(1, n + 1))
            if P(k, n) != expect:
                faulher_ok = False
                emit(f"FAULHABER MISMATCH k={k} n={n}: P={P(k,n)} expect={expect}")
    emit("Faulhaber P(k,n) checked vs literal loop for k=0..6, n=0..200: "
         + ("OK" if faulher_ok else "FAIL"))
    emit("")

    # Closed forms for audit
    emit("Faulhaber closed forms used (k: formula):")
    for k, (frm, den) in faulhaber_polys().items():
        emit(f"  P{k}(n) = {frm}")
    emit("")

    verify_ns = [1, 2, 4, 5, 10, 50]
    emit(f"{'n':>4} {'C(power)':>14} {'S(power)':>16}  match oracle?")
    results = {}
    for n in verify_ns:
        frames = enumerate_primitive_frames(n)
        C, S = compute_power(n, frames)
        results[n] = (C, S)
        mc = "C OK" if C == ORACLE_C[n] else "C MISMATCH"
        ms = "S OK" if S == ORACLE_S[n] else "S MISMATCH"
        match = f"{mc} | {ms}"
        emit(f"{n:>4} {C:>14} {S:>16}  {match}")
    emit("")

    # n=50: power-sum vs direct-loop exact equality + wall time of power phase
    n = 50
    t0 = time.time()
    frames50 = enumerate_primitive_frames(n)
    t_frames = time.time() - t0

    t1 = time.time()
    C_p, S_p = compute_power(n, frames50)
    t_power = time.time() - t1

    t2 = time.time()
    C_d, S_d = compute_direct(n, frames50)
    t_direct = time.time() - t2

    equal = (C_p == C_d) and (S_p == S_d)
    emit(f"n=50 power-sum     : C={C_p} S={S_p}")
    emit(f"n=50 direct-loop    : C={C_d} S={S_d}")
    emit(f"power-sum == direct-loop exactly (both C and S): "
         + ("ASSERT OK (bit-for-bit identical)" if equal else "MISMATCH"))
    emit(f"n=50 O(1) summation wall time (compute phase only): {t_power:.4f}s")
    emit(f"n=50 frame enumeration wall time (excluded from sum timing): {t_frames:.4f}s")
    emit(f"n=50 frame count: {len(frames50)}")
    if not equal:
        raise SystemExit("MISMATCH between power-sum and direct loop at n=50")

    with open("/workspace/power_validate.txt", "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\nWrote /workspace/power_validate.txt")


if __name__ == "__main__":
    main()
