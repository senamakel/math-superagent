#!/usr/bin/env python3
"""Independent verification oracle for the both-odd-primes branch.

Scan every (x, p, y, q) with p, q odd primes, x^p, y^q <= N, that is a GENUINE
solution of x^p - y^q = 1 (exact integer identity), and evaluate the
reconstructed Cassels + double-Wieferich necessary conditions on it.  A
"survivor" is an odd-prime solution (p,q odd) that satisfies ALL of:

    q | x          (Cassels)
    p | y          (Cassels)
    q^(p-1) == 1 (mod p^2)      (Wieferich, base q squared against p^2)
    p^(q-1) == 1 (mod q^2)      (Wieferich, base p squared against q^2)

The known solution (3,2,2,3) has p = 2 (even), so it is EXCLUDED BY THE
ODD-PRIME HYPOTHESIS: it is a genuine solution but never a survivor (its
(p,q) is not an odd pair).  The conjecture asserts the survivor count is 0 for
every N; this program re-confirms that below the stated bound.

This is a bounded exact verification oracle, NOT a proof: a survivor below the
bound is a candidate the odd-prime descent would have to exclude, and we report
it explicitly for the record.

All arithmetic is exact integer arithmetic (Python arbitrary-precision ints;
pow(a,b,m) for modular exponentiation; repeated exact multiplication for the
power values).  No floats, no logs, no math.pow.
"""
import math
import sys
import time

from lib.cond import check_conditions, is_odd_prime


def perfect_power_reps(N):
    """value -> list[(base, exp)] for every base^exp == value <= N,
    base >= 2, exp >= 2.  Exact integer arithmetic only."""
    reps = {}
    x = 2
    while x * x <= N:
        v = x * x
        e = 2
        while v <= N:
            reps.setdefault(v, []).append((x, e))
            v *= x
            e += 1
        x += 1
    return reps


def solutions_with_exponents(N):
    """All (x, p, y, q) with x^p, y^q <= N and x^p - y^q == 1, x,y>0, p,q>1.
    Returns a list of tuples (x, p, y, q, u) where u = x^p.
    Exact integer arithmetic; the identity itself is verified."""
    powers = perfect_power_reps(N)
    result = []
    for u, reps_u in powers.items():
        if u - 1 in powers:
            for (x, p) in reps_u:
                for (y, q) in powers[u - 1]:
                    if x ** p - y ** q == 1:
                        result.append((x, p, y, q, u))
    return sorted(result)


def main():
    N = int(sys.argv[1]) if len(sys.argv) > 1 else 10 ** 7
    t0 = time.time()

    print("=" * 78)
    print("check_conditions_all  N =", N)
    print("Scan GENUINE odd-prime-exponent solutions x^p - y^q = 1 (p,q odd),")
    print("evaluate Cassels (q|x, p|y) + double-Wieferich conditions.")
    print("Survivor = candidate satisfying ALL conditions.")
    print("=" * 78)

    # --- Oracle: all genuine solutions of x^p - y^q = 1 with x^p,y^q <= N.
    sols = solutions_with_exponents(N)
    print("\n[1] Genuine solutions (x,p,y,q) of x^p - y^q = 1, x^p,y^q <= N:")
    for (x, p, y, q, u) in sols:
        tag = "ODD-PAIR" if (is_odd_prime(p) and is_odd_prime(q)) else "non-odd"
        print(f"    x={x} p={p} y={y} q={q}   x^p={u}   ({tag})")
    print(f"    -> {len(sols)} solution(s).")

    # --- Calibration: the direct evaluator at the known solution.
    print("\n[2] Calibration of check_conditions at known solution (3,2,2,3):")
    c = check_conditions(2, 3, x=3, y=2)
    print("    check_conditions(2,3,x=3,y=2) =", c)
    cells = ("is_odd_prime_pair", "vp_y", "vq_x", "wieferich_1", "wieferich_2")
    print("    known solution satisfies Cassels content (q|x True, p|y True)")
    print("    but is_odd_prime_pair =", c["is_odd_prime_pair"],
          "(p=2 even) -> EXCLUDED BY HYPOTHESIS, never a survivor.")

    # --- Survivors: odd-prime solutions satisfying all four conditions.
    survivors = []
    checked = 0
    for (x, p, y, q, u) in sols:
        if not (is_odd_prime(p) and is_odd_prime(q)):
            continue
        checked += 1
        cc = check_conditions(p, q, x=x, y=y)
        all_hold = all(cc[k] for k in
                       ("vq_x", "vp_y", "wieferich_1", "wieferich_2"))
        if all_hold:
            survivors.append((x, p, y, q, u, cc))

    # --- Report.
    print("\n[3] Survivor scan over odd-prime solutions:", checked, "odd-pair",
          "solution(s) evaluated")
    print("    Survivor = satisfies q|x AND p|y AND q^(p-1)==1 mod p^2 AND",
          "p^(q-1)==1 mod q^2.")
    if survivors:
        print("    *** SURVIVORS FOUND (odd-prime candidates the descent would")
        print("        have to exclude): ***")
        for (x, p, y, q, u, cc) in survivors:
            print(f"    x={x} p={p} y={y} q={q} x^p={u} conds={ {k: cc[k] for k in cells} }")
    else:
        print("    SURVIVOR COUNT = 0")

    dt = time.time() - t0
    print("\n" + "=" * 78)
    print("RESULT")
    print(f"  N reached          : {N}")
    print(f"  genuine solutions  : {len(sols)}  (must be exactly (3,2,2,3))")
    print(f"  odd-pair solutions : {checked}")
    print(f"  survivor count     : {len(survivors)}")
    print(f"  runtime            : {dt:.3f}s")
    print("  NOTE: any odd-prime (p,q) survivor of ALL conditions below the")
    print("        bound is a candidate the descent would have to exclude;")
    print("        zero here is consistent with classifier being only the known")
    print("        solution (3,2,2,3), excluded by the odd-prime hypothesis.")
    print("=" * 78)

    # Exit code: 0 if oracle is exactly the known solution and no survivor.
    ok = (sols == [(3, 2, 2, 3, 9)]) and (len(survivors) == 0)
    sys.exit(0 if ok else 1)


if __name__ == "__main__":
    main()
