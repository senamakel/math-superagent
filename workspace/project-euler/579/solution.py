#!/usr/bin/env python3
"""
solution.py - Final PE 579 solution: primary-Hurwitz-quaternion enumeration +
O(1) Faulhaber power-sum summation.

Theory (see memory.md and research/):
  Every lattice cube factors uniquely as (primitive frame) x (scale t).  A
  primitive frame is a triple of pairwise-orthogonal equal-norm integer vectors
  (u,v,w), |u|^2=|v|^2=|w|^2=ell^2, with gcd(all 9 coords)=1.

  Euler-Rodrigues: any such orthogonal equal-norm integer frame is produced by
  an integer quaternion alpha=(a,b,c,d):

      u = ( a^2+b^2-c^2-d^2 , 2(bc-ad) , 2(bd+ac) )
      v = ( 2(bc+ad)      , a^2-b^2+c^2-d^2 , 2(cd-ab) )
      w = ( 2(bd-ac)      , 2(cd+ab) , a^2-b^2-c^2+d^2 )

  with |u|^2=|v|^2=|w|^2=N^2 where N=a^2+b^2+c^2+d^2, so ell=N.

  The theorem (Kiss-Kutas / Goswick et al.) : a primitive frame arises from a
  PRIMARY primitive integer quaternion, i.e. gcd(a,b,c,d)=1 and either
    a even, b,c,d odd, a+b+c+d ≡ 1 (mod 4),   or   a odd, b,c,d even, a+b+c+d≡1
  (equivalently: a's parity differs from b,c,d and (a+b+c+d)%4==1).  Every
  primitive frame has ODD edge length ell, so N is odd.  Enumerating primary
  primitive quaternions with N<=n (4-ball of radius sqrt(n)) and taking each
  resulting frame's canonical key exactly once gives the full set.

  For a primitive frame (ell,A,B,C,D): A=sum|edge x|, B=sum|edge y|, C=sum|edge z|,
  D=sum of edge-gcds.  Scaling by t:
    box-fit corners  T(t)=(n+1-tA)(n+1-tB)(n+1-tC)
    lattice points   pts(t)=ell^3 t^3 + ell*D t^2 + D t + 1   (Ehrhart/Ionascu)
  Then use O(1) Faulhaber power sums (solution_power.compute_power) so the cost
  per frame does not grow with n.

Author's note on complexity:
  Number of quaternions in the radius-sqrt(n) 4-ball is O(n^2).  Each is mapped
  to a frame in O(1).  Frames with gcd=1 (primitive): O(n^2).  Dedup via a set
  keyed by canonical (sign/permutation-invariant) frame.  So enumeration is
  O(n^2) time and O(n^2) space (the frame set).  For n=5000: ~1.2e8 quaternions
  scanned, ~7.5e6 distinct frames.  No exponential growth, no search of the
  answer space -- this is a closed parametrization.

Usage:
  python3 solution.py                 # full: validate then run n=5000
  python3 solution.py --no5000        # validate only (keep light)
"""
import math
import sys
import time
from math import gcd

# Reuse the exact O(1) power-sum summation (bit-for-bit as validated).
from solution_power import compute_power, P
from frame_method import canonical_key, gcd3, enumerate_primitive_frames


def euler(a, b, c, d):
    """Euler-Rodrigues frame from integer quaternion (a,b,c,d)."""
    a2, b2, c2, d2 = a * a, b * b, c * c, d * d
    u = (a2 + b2 - c2 - d2, 2 * (b * c - a * d), 2 * (b * d + a * c))
    v = (2 * (b * c + a * d), a2 - b2 + c2 - d2, 2 * (c * d - a * b))
    w = (2 * (b * d - a * c), 2 * (c * d + a * b), a2 - b2 - c2 + d2)
    return u, v, w


def is_primary(a, b, c, d):
    """Primary Hurwitz: a's parity differs from b,c,d and (a+b+c+d)%4==1."""
    if ((a - b) & 1) == 0 or ((a - c) & 1) == 0 or ((a - d) & 1) == 0:
        return False
    return (a + b + c + d) % 4 == 1


def enumerate_primitive_frames_quat(n):
    """Canonical primitive-frame dict via primary primitive quaternions.

    Same return contract as frame_method.enumerate_primitive_frames:
    dict canon_key -> (ell, A, B, C, D).  Does NOT skip on A,B,C>n (that
    matches frame_method, which keeps such frames for exact key-set identity).
    """
    R = math.isqrt(n)          # N = a^2+b^2+c^2+d^2 <= n  =>  |each coord| <= sqrt(n)
    R2 = R * R
    frames = {}
    # scan a,b,c in [-R,R], d ranges over the remaining 4-ball slice
    for a in range(-R, R + 1):
        a2 = a * a
        for b in range(-R, R + 1):
            ab = a2 + b * b
            if ab > R2:
                continue
            for c in range(-R, R + 1):
                abc = ab + c * c
                if abc > R2:
                    continue
                rem = R2 - abc
                dr = math.isqrt(rem)          # d ranges [-dr, dr]
                for d in range(-dr, dr + 1):
                    Nv = abc + d * d
                    if Nv > n or Nv == 0:
                        continue
                    if (Nv & 1) == 0:
                        continue             # primitive frames have odd ell=N
                    if gcd(gcd(gcd(a, b), c), d) != 1:
                        continue             # primitive quaternion
                    if not is_primary(a, b, c, d):
                        continue
                    u, v, w = euler(a, b, c, d)
                    key = canonical_key(u, v, w)
                    if key in frames:
                        continue
                    # ---- identical (ell,A,B,C,D) computation as frame_method ----
                    ell = Nv
                    A = abs(u[0]) + abs(v[0]) + abs(w[0])
                    B = abs(u[1]) + abs(v[1]) + abs(w[1])
                    C = abs(u[2]) + abs(v[2]) + abs(w[2])
                    D = (gcd3(u[0], u[1], u[2])
                         + gcd3(v[0], v[1], v[2])
                         + gcd3(w[0], w[1], w[2]))
                    frames[key] = (ell, A, B, C, D)
    return frames


# ---------------------------------------------------------------------------
# Oracle + reference frame counts (from frame_method, for reporting)
# ---------------------------------------------------------------------------
ORACLE_C = {1: 1, 2: 9, 4: 100, 5: 229, 10: 4469, 50: 8154671}
ORACLE_S = {1: 8, 2: 91, 4: 1878, 5: 5832, 10: 387003, 50: 29948928129}


def main():
    do5000 = "--no5000" not in sys.argv
    lines = []
    emit = lambda s: (print(s), lines.append(s))

    emit("=" * 78)
    emit("PE579 final solution: primary-Hurwitz-quaternion enumeration +")
    emit("O(1) Faulhaber power-sum summation.")
    emit("=" * 78)

    # ---- Part 1: frame-set identity vs frame_method (exact key set) ----
    verify_ns = [1, 2, 4, 5, 10, 50]
    emit("\n[1] frame-set identity: quat-keys == frame_method-keys")
    emit(f"{'n':>4} {'#quat-frames':>14} {'#ref-frames':>13}  keys-equal?")
    all_ok = True
    for n in verify_ns:
        tq = time.time()
        qf = enumerate_primitive_frames_quat(n)
        tq = time.time() - tq
        tf = time.time()
        rf = enumerate_primitive_frames(n)
        tf = time.time() - tf
        eq = set(qf.keys()) == set(rf.keys())
        # also verify the (ell,A,B,C,D) tuples agree on the common keys
        agree = all(qf[k] == rf[k] for k in qf.keys() if k in rf) if eq else False
        ok = eq and agree
        all_ok &= ok
        emit(f"{n:>4} {len(qf):>14} {len(rf):>13}  {'YES' if ok else 'NO (see detail)'} "
             f"(quat {tq:.2f}s / ref {tf:.2f}s)")
    emit("frame-set identity for n=1,2,4,5,10,50: " + ("ALL YES" if all_ok else "SOME NO"))

    # n=100, 200 with the reference (frame_method) - feasible but heavier
    for n in [100, 200]:
        tq = time.time()
        qf = enumerate_primitive_frames_quat(n)
        tq = time.time() - tq
        tf = time.time()
        rf = enumerate_primitive_frames_lean(n)
        tf = time.time() - tf
        eq = set(qf.keys()) == set(rf.keys())
        agree = all(qf[k] == rf[k] for k in qf.keys() if k in rf) if eq else False
        ok = eq and agree
        all_ok &= ok
        emit(f"n={n:>3} {len(qf):>10} {len(rf):>13}  {'YES' if ok else 'NO (see detail)'} "
             f"(quat {tq:.2f}s / ref {tf:.2f}s)")
    emit("[1] FINAL frame-set identity: " + ("ALL YES" if all_ok else "SOME NO"))

    # ---- Part 2: C/S oracle match (via power-sum summation) ----
    emit("\n[2] C/S oracle match (power-sum summation over quat frames)")
    emit(f"{'n':>4} {'C':>14} {'S':>18}  C-ok? S-ok?")
    for n in [1, 2, 4, 5, 10, 50]:
        qf = enumerate_primitive_frames_quat(n)
        C, S = compute_power(n, qf)
        cok = (n in ORACLE_C and C == ORACLE_C[n])
        sok = (n in ORACLE_S and S == ORACLE_S[n])
        emit(f"{n:>4} {C:>14} {S:>18}  {('OK' if cok else 'BAD')} {('OK' if sok else 'BAD')}")

    if not do5000:
        emit("\nSkipping n=5000 (--no5000).")
        with open("/workspace/solution_output.txt", "w") as f:
            f.write("\n".join(lines) + "\n")
        print("\nWrote /workspace/solution_output.txt")
        return

    # ---- Part 3: n=5000 ----
    emit("\n[3] n=5000 full computation")
    n = 5000
    t0 = time.time()
    frames = enumerate_primitive_frames_quat(n)
    t_enum = time.time() - t0
    nf = len(frames)
    emit(f"n=5000: distinct primitive frames = {nf}  (enumeration {t_enum:.1f}s)")

    t1 = time.time()
    C, S = compute_power(n, frames)
    t_sum = time.time() - t1

    # ---- Part 4: bit-for-bit cross-check: power-sum vs direct t-loop ----
    from frame_method import compute as compute_direct
    t2 = time.time()
    C_d, S_d = compute_direct(n, frames)
    t_direct = time.time() - t2
    cross_ok = (C == C_d) and (S == S_d)

    emit(f"C(5000) = {C}")
    emit(f"S(5000) = {S}")
    emit(f"S(5000) mod 10^9 = {S % 10**9}")
    emit(f"direct-loop C = {C_d}  S = {S_d}")
    emit(f"bit-for-bit cross-check (power-sum == direct-loop): "
         + ("PASS (identical)" if cross_ok else "FAIL"))
    emit(f"wall time: total {time.time()-t0:.1f}s (enumeration {t_enum:.1f}s, "
         f"power-sum {t_sum:.3f}s, direct-loop {t_direct:.3f}s)")

    if not cross_ok:
        raise SystemExit("CROSS-CHECK FAILED: power-sum != direct-loop")
    if not all_ok:
        raise SystemExit("FRAME-SET/MATCH FAILED")

    with open("/workspace/solution_output.txt", "w") as f:
        f.write("\n".join(lines) + "\n")
    print("\nWrote /workspace/solution_output.txt")


if __name__ == "__main__":
    main()
