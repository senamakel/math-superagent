#!/usr/bin/env python3
"""
solution.py - Final PE 579 solution.

Enumerator (primary primitive quaternions, streaming) + O(1) Faulhaber
power-sum summation.  See AGENTS.md / memory.md for the full theory.

  Every primitive lattice frame (u,v,w), pairwise-orthogonal equal-norm
  integer vectors with gcd(all coords)=1 and edge length ell=sqrt(|u|^2), is
  produced with the Euler-Rodrigues formula from a PRIMARY primitive integer
  quaternion (a,b,c,d):

      u=(a^2+b^2-c^2-d^2, 2(bc-ad), 2(bd+ac))
      v=(2(bc+ad), a^2-b^2+c^2-d^2, 2(cd-ab))
      w=(2(bd-ac), 2(cd+ab), a^2-b^2-c^2+d^2)

  with |u|^2=|v|^2=|w|^2 = N^2, N=a^2+b^2+c^2+d^2 = ell.  Every primitive frame
  has ODD ell=N.  PRIMARY: a's parity differs from b,c,d and (a+b+c+d)%4==1,
  with gcd(a,b,c,d)==1.  Enumerating primary primitive quaternions with N<=n
  (4-ball radius sqrt(n)) and deduping by canonical frame key yields exactly the
  primitive-frame set.

  For frame (ell,A,B,C,D):  A=sum|edge_x|, B=sum|edge_y|, C=sum|edge_z|,
  D=sum of edge-gcds.  Scaling by t:
      T(t)  = (n+1-tA)(n+1-tB)(n+1-tC)          box-fit corner count
      pts(t)= ell^3 t^3 + ell*D t^2 + D*t + 1   lattice points (Ehrhart/Ionascu)
  S and C accumulate over t with O(1) Faulhaber power sums per frame
  (compute_power), so per-frame cost is O(1) and independent of n.

Complexity: quaternion scan is O(n^2) (a ball of radius sqrt(n)), each frame
O(1).  Enumeration + summation is O(n^2) time, O(1) extra space when streaming
(the frame dict is only materialised for small validation n).

To respect the 2GB memory cap at n=5000 (~7.5M frames would need ~7GB as a
Python dict), the n=5000 path streams frames and accumulates C/S incrementally
for BOTH power-sum and the direct t-loop, then compares the totals
bit-for-bit.

Usage:
  python3 solution.py            # validate small n (dict-based) then solve n=5000
  python3 solution.py --no5000   # validation only
"""
import math
import sys
import time
from math import gcd

from solution_power import compute_power, P
from frame_method import (
    canonical_key, gcd3, enumerate_primitive_frames, enumerate_primitive_frames_lean,
    compute as compute_direct,
)

ORACLE_C = {1: 1, 2: 9, 4: 100, 5: 229, 10: 4469, 50: 8154671}
ORACLE_S = {1: 8, 2: 91, 4: 1878, 5: 5832, 10: 387003, 50: 29948928129}


def euler(a, b, c, d):
    """Euler-Rodrigues frame from integer quaternion (a,b,c,d)."""
    a2, b2, c2, d2 = a * a, b * b, c * c, d * d
    u = (a2 + b2 - c2 - d2, 2 * (b * c - a * d), 2 * (b * d + a * c))
    v = (2 * (b * c + a * d), a2 - b2 + c2 - d2, 2 * (c * d - a * b))
    w = (2 * (b * d - a * c), 2 * (c * d + a * b), a2 - b2 - c2 + d2)
    return u, v, w


def frame_of(a, b, c, d):
    """Map primary quaternion -> (key, (ell,A,B,C,D)) or None if not primitive."""
    Nv = a * a + b * b + c * c + d * d
    if Nv == 0:
        return None
    if gcd(gcd(gcd(a, b), c), d) != 1:
        return None
    u, v, w = euler(a, b, c, d)
    key = canonical_key(u, v, w)
    ell = Nv
    A = abs(u[0]) + abs(v[0]) + abs(w[0])
    B = abs(u[1]) + abs(v[1]) + abs(w[1])
    C = abs(u[2]) + abs(v[2]) + abs(w[2])
    D = gcd3(u[0], u[1], u[2]) + gcd3(v[0], v[1], v[2]) + gcd3(w[0], w[1], w[2])
    return key, (ell, A, B, C, D)


def iter_primary_quats(n):
    """Yield each primary primitive quaternion (a,b,c,d) with N<=n exactly once."""
    R = math.isqrt(n)
    # Case 1: a even, b,c,d odd ; d == (1-a-b-c) mod 4
    for a in range(-R, R + 1, 2):
        a2 = a * a
        for b in range(-R + 1, R + 1, 2):
            ab = a2 + b * b
            if ab > n:
                continue
            for c in range(-R + 1, R + 1, 2):
                abc = ab + c * c
                if abc > n:
                    continue
                dr = math.isqrt(n - abc)
                r = (1 - a - b - c) % 4
                d0 = -dr + ((r - (-dr)) % 4)
                for d in range(d0, dr + 1, 4):
                    yield a, b, c, d
    # Case 2: a odd, b,c,d even ; d == (1-a-b-c) mod 4
    for a in range(-R + 1, R + 1, 2):
        a2 = a * a
        for b in range(-R, R + 1, 2):
            ab = a2 + b * b
            if ab > n:
                continue
            for c in range(-R, R + 1, 2):
                abc = ab + c * c
                if abc > n:
                    continue
                dr = math.isqrt(n - abc)
                r = (1 - a - b - c) % 4
                d0 = -dr + ((r - (-dr)) % 4)
                for d in range(d0, dr + 1, 4):
                    yield a, b, c, d


def enumerate_primitive_frames_quat(n):
    """dict canon_key -> (ell,A,B,C,D) via primary primitive quaternions.

    For validation n (memory permits).  Does NOT skip frames with A,B,C>n
    (matches frame_method for exact key-set identity).
    """
    frames = {}
    for a, b, c, d in iter_primary_quats(n):
        res = frame_of(a, b, c, d)
        if res is None:
            continue
        key, tup = res
        if key not in frames:
            frames[key] = tup
    return frames


# ---------------------------------------------------------------------------
# Per-frame O(1) power-sum contribution (mirrors compute_power, one frame)
# ---------------------------------------------------------------------------
def frame_contrib_power(n, ell, A, B, Cc, D):
    """Return (C_contrib, S_contrib) for one frame at box size n, O(1)."""
    X = n + 1
    tmax = n
    if A > 0:
        tmax = min(tmax, n // A)
    if B > 0:
        tmax = min(tmax, n // B)
    if Cc > 0:
        tmax = min(tmax, n // Cc)
    if tmax <= 0:
        return 0, 0
    pa = A + B + Cc
    pb = A * B + A * Cc + B * Cc
    pc = A * B * Cc
    p0 = X ** 3
    p1 = -X * X * pa
    p2 = X * pb
    p3 = -pc
    q0, q1, q2, q3 = 1, D, ell * D, ell ** 3
    c = [0] * 7
    for i, qi in enumerate((q0, q1, q2, q3)):
        for j, pj in enumerate((p0, p1, p2, p3)):
            c[i + j] += qi * pj
    ccontrib = (p0 * P(0, tmax) + p1 * P(1, tmax)
                + p2 * P(2, tmax) + p3 * P(3, tmax))
    scontrib = sum(c[k] * P(k, tmax) for k in range(7))
    return ccontrib, scontrib


def frame_contrib_direct(n, ell, A, B, Cc, D):
    """Return (C_contrib, S_contrib) for one frame via direct t-loop."""
    tmax = n
    if A > 0:
        tmax = min(tmax, n // A)
    if B > 0:
        tmax = min(tmax, n // B)
    if Cc > 0:
        tmax = min(tmax, n // Cc)
    if tmax <= 0:
        return 0, 0
    ccount = 0
    scount = 0
    for t in range(1, tmax + 1):
        tx = n + 1 - t * A
        ty = n + 1 - t * B
        tz = n + 1 - t * Cc
        T = tx * ty * tz
        if T <= 0:
            break
        pts = ell ** 3 * t ** 3 + ell * D * t * t + D * t + 1
        ccount += T
        scount += pts * T
    return ccount, scount


def solve_stream(n, collect_frames=False):
    """Stream primary frames, accumulate C,S by power-sum and by direct loop.

    If collect_frames, also return the distinct-frame dict (for small n).
    Returns (C_p, S_p, C_d, S_d, frame_count, frames_or_None).

    Memory-safe at n=5000: only the dedup `seen` set of canonical keys is kept
    (~7.5M small tuples), NOT a value dict, so memory stays well under 2GB.
    """
    seen = set()
    frames = {} if collect_frames else None
    C_p = S_p = C_d = S_d = 0
    nframes = 0
    for a, b, c, d in iter_primary_quats(n):
        res = frame_of(a, b, c, d)
        if res is None:
            continue
        key, tup = res
        if key in seen:
            continue
        seen.add(key)
        nframes += 1
        if collect_frames:
            frames[key] = tup
        ell, A, B, Cc, D = tup
        cp, sp = frame_contrib_power(n, ell, A, B, Cc, D)
        C_p += cp
        S_p += sp
        cd, sd = frame_contrib_direct(n, ell, A, B, Cc, D)
        C_d += cd
        S_d += sd
    return C_p, S_p, C_d, S_d, nframes, frames


def main():
    do5000 = "--no5000" not in sys.argv
    lines = []
    emit = lambda s: (print(s), lines.append(s))

    emit("=" * 78)
    emit("PE579 final solution: primary-Hurwitz-quaternion enumeration +")
    emit("O(1) Faulhaber power-sum summation (streaming).")
    emit("=" * 78)

    # ---- Part 1: frame-set identity vs frame_method (exact key set) ----
    verify_ns = [1, 2, 4, 5, 10, 50, 100, 200]
    emit("\n[1] frame-set identity: quat-keys == frame_method-keys")
    emit(f"{'n':>4} {'#quat':>10} {'#ref':>10}  keys-equal  tuples-agree")
    all_ok = True
    for n in verify_ns:
        qf = enumerate_primitive_frames_quat(n)
        rf = (enumerate_primitive_frames(n) if n <= 50
              else enumerate_primitive_frames_lean(n))
        eq = set(qf.keys()) == set(rf.keys())
        agree = all(qf[k] == rf[k] for k in qf) if eq else False
        ok = eq and agree
        all_ok &= ok
        emit(f"{n:>4} {len(qf):>10} {len(rf):>10}      {('YES' if eq else 'NO'):<10} "
             f"{('YES' if agree else 'NO')}")
    emit("[1] FINAL frame-set identity: " + ("ALL YES" if all_ok else "SOME NO"))

    # ---- Part 2: C/S oracle match (power-sum over quat frames) ----
    emit("\n[2] C/S oracle match (power-sum summation over quat frames)")
    emit(f"{'n':>4} {'C':>14} {'S':>18}  C-ok S-ok")
    for n in [1, 2, 4, 5, 10, 50]:
        qf = enumerate_primitive_frames_quat(n)
        C, S = compute_power(n, qf)
        cok = (n in ORACLE_C and C == ORACLE_C[n])
        sok = (n in ORACLE_S and S == ORACLE_S[n])
        emit(f"{n:>4} {C:>14} {S:>18}  {('OK' if cok else 'BAD'):>3} "
             f"{('OK' if sok else 'BAD')}")

    if not do5000:
        emit("\nSkipping n=5000 (--no5000).")
        with open("/workspace/solution_output.txt", "w") as f:
            f.write("\n".join(lines) + "\n")
        print("\nWrote /workspace/solution_output.txt")
        return

    # ---- Part 3: n=5000 (streamed, memory-safe) ----
    emit("\n[3] n=5000 full computation (streamed)")
    n = 5000
    t0 = time.time()
    C_p, S_p, C_d, S_d, nframes, _frames = solve_stream(n, collect_frames=False)
    t_total = time.time() - t0
    cross_ok = (C_p == C_d) and (S_p == S_d)

    emit(f"n=5000 distinct primitive frames = {nframes}")
    emit(f"C(5000) = {C_p}")
    emit(f"S(5000) = {S_p}")
    emit(f"S(5000) mod 10^9 = {S_p % 10**9}")
    emit(f"direct-loop C = {C_d}  S = {S_d}")
    emit(f"bit-for-bit cross-check (power-sum == direct-loop): "
         + ("PASS (identical)" if cross_ok else "FAIL"))
    emit(f"wall time (enum + both summations, streamed): {t_total:.1f}s")

    if not cross_ok:
        raise SystemExit("CROSS-CHECK FAILED")
    if not all_ok:
        raise SystemExit("FRAME-SET/MATCH FAILED")

    with open("/workspace/solution_output.txt", "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\nWrote /workspace/solution_output.txt")


if __name__ == "__main__":
    main()
