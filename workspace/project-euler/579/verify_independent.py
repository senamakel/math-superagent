#!/usr/bin/env python3
"""
verify_independent.py - Independent verification of the PE 579 machinery.

This is a CHECK of the machinery, NOT a recomputation of the final answer
S(5000).  It performs four tasks, each by a route independent (where possible)
of the one that produced the value:

Task 1: Re-run the primary-quaternion parametrization logic
        (/workspace/research/verify_primary.py) and report whether it passes:
          (a) for every odd N in 1..30, the set of distinct frames produced by
              ALL primitive integer quaternions (gcd(a,b,c,d)=1, norm N odd)
              EQUALS the set produced by PRIMARY primitive integer quaternions
              only, and
          (b) N == frame edge length for every primary frame.

Task 2: Exhaustively prove (via frame_method's vector-pairing enumeration,
        the *independent* direct enumeration, not the quaternion route) that NO
        primitive frame with coordinate spans fully inside box n has even edge
        length, for all n up to n=80 and every edge length ell <= 80.
        (ell odd in every frame => C/S contributions are odd-edge only.)

Task 3: Independently recompute C(n) and S(n) using frame_method's primitive-
        frame enumeration + solution_power's O(1) power-sum summation
        (compute_power), and confirm the oracle values for
        n = 1,2,4,5,10,50.

Task 4: If /workspace/solution.py exists with a quaternion enumeration, compare
        its frame-key set against frame_method's for n up to 200 (set equality).
        (Currently solution.py does not exist, so this is reported as N/A.)

No floats.  Everything is exact integer arithmetic.
"""
import time

import frame_method
from frame_method import enumerate_primitive_frames_lean
from solution_power import compute_power

OUT = "/workspace/verify_independent_output.txt"


# --------------------------------------------------------------------------
# Task 1: primary-quaternion logic (verbatim logic of verify_primary.py)
# --------------------------------------------------------------------------
def euler(a, b, c, d):
    u = (a*a + b*b - c*c - d*d, 2*(b*c - a*d), 2*(b*d + a*c))
    v = (2*(b*c + a*d), a*a - b*b + c*c - d*d, 2*(c*d - a*b))
    w = (2*(b*d - a*c), 2*(c*d + a*b), a*a - b*b - c*c + d*d)
    return (u, v, w)


def norm2(v):
    return v[0]*v[0] + v[1]*v[1] + v[2]*v[2]


def sign_norm(vec):
    for x in vec:
        if x < 0:
            return tuple(-y for y in vec)
        if x > 0:
            return vec
    return vec


def canon_frame(fr):
    return tuple(sorted(sign_norm(v) for v in fr))


def is_primary(a, b, c, d):
    par_diff = ((a - b) % 2 == 1 and (a - c) % 2 == 1 and (a - d) % 2 == 1)
    return par_diff and ((a + b + c + d) % 4 == 1)


def task1():
    from collections import defaultdict
    from math import gcd
    Nmax = 30
    frames_all = defaultdict(set)
    frames_primary = defaultdict(set)
    for a in range(-Nmax, Nmax + 1):
        for b in range(-Nmax, Nmax + 1):
            for c in range(-Nmax, Nmax + 1):
                for d in range(-Nmax, Nmax + 1):
                    nn = a*a + b*b + c*c + d*d
                    if not (1 <= nn <= Nmax and nn % 2 == 1):
                        continue
                    if gcd(gcd(gcd(a, b), c), d) != 1:
                        continue
                    fr = canon_frame(euler(a, b, c, d))
                    frames_all[nn].add(fr)
                    if is_primary(a, b, c, d):
                        frames_primary[nn].add(fr)
    ok = True
    for N in sorted(frames_all):
        if frames_all[N] != frames_primary[N]:
            ok = False
            print(f"  MISMATCH N={N}: all={len(frames_all[N])} primary={len(frames_primary[N])}")
    # N == edge length
    from math import isqrt
    edgelen_ok = True
    for N in sorted(frames_primary):
        for fr in frames_primary[N]:
            el = isqrt(norm2(fr[0]))
            if el != N:
                edgelen_ok = False
    return ok, edgelen_ok


# --------------------------------------------------------------------------
# Task 2: no primitive frame has even edge length (n up to 80)
# --------------------------------------------------------------------------
def task2():
    n = 80
    t0 = time.time()
    frames = enumerate_primitive_frames_lean(n)
    wall = time.time() - t0
    ells = [v[0] for v in frames.values()]
    even = [e for e in ells if e % 2 == 0]
    return (len(frames), len(ells), len(even), wall)


# --------------------------------------------------------------------------
# Task 3: independent C/S recomputation with frame + power-sum
# --------------------------------------------------------------------------
ORACLE_C = {1: 1, 2: 9, 4: 100, 5: 229, 10: 4469, 50: 8154671}
ORACLE_S = {1: 8, 2: 91, 4: 1878, 5: 5832, 10: 387003, 50: 29948928129}


def task3():
    results = []
    allok = True
    for n in [1, 2, 4, 5, 10, 50]:
        t0 = time.time()
        frames = enumerate_primitive_frames_lean(n)
        C, S = compute_power(n, frames)
        wall = time.time() - t0
        cok = C == ORACLE_C[n]
        sok = S == ORACLE_S[n]
        if not (cok and sok):
            allok = False
        results.append((n, C, S, cok, sok, wall))
    return allok, results


# --------------------------------------------------------------------------
# Task 4: solution.py quaternion enumeration vs frame_method (if it exists)
# --------------------------------------------------------------------------
def task4():
    import os
    if not os.path.exists("/workspace/solution.py"):
        return None
    try:
        import solution
        if not hasattr(solution, "enumerate_frames") and \
           not hasattr(solution, "enumerate_quat_frames"):
            return "present-but-no-enumeration-function"
    except Exception as e:
        return ("import-error", str(e))
    # If a solution enumeration exists, compare frame-key sets for n up to 200.
    lines = []
    for n in [60, 120, 200]:
        fm = set(enumerate_primitive_frames_lean(n).keys())
        try:
            sol = set(solution.enumerate_quat_frames(n).keys())
        except AttributeError:
            sol = set(solution.enumerate_frames(n).keys())
        lines.append((n, fm, sol, fm == sol))
    return lines


def main():
    lines = []

    def emit(s):
        print(s)
        lines.append(s)

    emit("=" * 78)
    emit("Independent verification of PE 579 machinery (not the final answer)")
    emit("=" * 78)

    # ---- Task 1 ----
    emit("\n[Task 1] Primary-quaternion parametrization logic")
    t0 = time.time()
    all_ok, edgelen_ok = task1()
    emit(f"  (a) For every odd N in 1..30, frames(all primitive quats) == "
         f"frames(primary primitive quats): "
         + ("PASS" if all_ok else "FAIL"))
    emit(f"  (b) N == edge length for every primary frame: "
         + ("PASS" if edgelen_ok else "FAIL"))
    emit(f"  Task 1 wall: {time.time()-t0:.2f}s")
    emit("  => " + ("PASS" if (all_ok and edgelen_ok) else "FAIL"))

    # ---- Task 2 ----
    emit("\n[Task 2] No primitive frame has even edge length (exhaustive, n<=80)")
    cnt, nells, neven, wall = task2()
    emit(f"  primitive frames with coordinate spans in box n=80: {cnt}")
    emit(f"  of those, edge length even: {neven}, odd: {nells - neven}")
    emit(f"  -> NO primitive frame has even edge length up to n=80: "
         + ("CONFIRMED (0 even)" if neven == 0 else "REFUTED"))
    emit(f"  Task 2 wall: {wall:.2f}s (vector-pairing enumeration, n=80)")

    # ---- Task 3 ----
    emit("\n[Task 3] Independent C(n), S(n) via frame enumeration + power sums")
    ok3, results = task3()
    emit(f"  {'n':>4} {'C(n)':>12} {'S(n)':>16}  C-ok  S-ok")
    for (n, C, S, cok, sok, wall) in results:
        emit(f"  {n:>4} {C:>12} {S:>16}  {cok}    {sok}")
    emit(f"  Oracle C: {list(ORACLE_C.values())}")
    emit(f"  Oracle S: {list(ORACLE_S.values())}")
    emit(f"  => Task 3 " + ("PASS (all match oracle)" if ok3 else "FAIL"))

    # ---- Task 4 ----
    emit("\n[Task 4] solution.py quaternion enumeration vs frame_method (n up to 200)")
    res4 = task4()
    if res4 is None:
        emit("  /workspace/solution.py does not exist -> task N/A (no "
             "quaternion-enumeration implementation to compare yet).")
    elif isinstance(res4, tuple) and res4 and res4[0] == "import-error":
        emit(f"  solution.py exists but imported with error: {res4[1]}")
    elif res4 == "present-but-no-enumeration-function":
        emit("  solution.py exists but exposes no enumeration function.")
    else:
        for (n, fm, sol, eq) in res4:
            emit(f"  n={n}: frame_method keys={len(fm)} solution keys={len(sol)} "
                 f"set-equal={eq}")
        emit("  => Task 4 " + ("PASS (set-equal at all checked n)"
                               if all(l[3] for l in res4) else "FAIL"))

    emit("\n" + "=" * 78)
    emit("SUMMARY")
    emit(f"  Task 1 (primary quats == all primitive quats, odd N<=30; N==edgelen): "
         + ("PASS" if (all_ok and edgelen_ok) else "FAIL"))
    emit(f"  Task 2 (no even-edge primitive frame, n<=80): "
         + ("PASS" if neven == 0 else "FAIL"))
    emit(f"  Task 3 (C/S match oracle at n=1,2,4,5,10,50): "
         + ("PASS" if ok3 else "FAIL"))
    if res4 in (None, "present-but-no-enumeration-function"):
        emit("  Task 4 (solution.py quaternion vs frame_method): N/A (no solution.py)")
    elif isinstance(res4, tuple):
        emit(f"  Task 4: {'PASS' if all(l[3] for l in res4) else 'FAIL'}")
    emit("=" * 78)

    with open(OUT, "w") as f:
        f.write("\n".join(lines) + "\n")
    print(f"\nWrote {OUT}")


if __name__ == "__main__":
    main()
