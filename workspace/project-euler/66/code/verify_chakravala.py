#!/usr/bin/env python3
"""Phase 5 independent verification of results_cf.tsv via Bhaskara II's
Chakravala (cyclic) method.

Context
-------
solution.py computed, via the continued-fraction (CF) convergent method, the
minimal solution (x_D, y_D) of x^2 - D*y^2 = 1 for every non-square
D <= 1000 and wrote results_cf.tsv (header "D\\tx\\ty").  This script
re-derives every one of those rows by a SECOND, INDEPENDENT route -- the
Chakravala method, which uses NO continued fractions -- and requires exact
equality of the pairs.

Method and the result it rests on
---------------------------------
Chakravala maintains the invariant

        a^2 - D*b^2 = k                                   (1)

and at each step picks an admissible integer m (k | (a + b*m), taken in the
residue class m = -a*b^{-1} mod |k|) minimizing |m^2 - D|, then updates

        a' = |a*m + D*b| / |k|,
        b' = |a + b*m| / |k|,
        k' = (m^2 - D) / k.

Exactness rests on the composition (bhavana) identity

        (a*m + D*b)^2 - D*(a + b*m)^2 = (a^2 - D*b^2)*(m^2 - D) = k*(m^2 - D),

so dividing by k^2 preserves (1).  The two divisions in a', b' are exact
because k | (a + b*m) and gcd(b, |k|) = 1 (classically maintained by the
process) imply k | (a*m + D*b); then k | (m^2 - D) follows from gcd(b,k) = 1,
so the third division is exact as well.  The classical theorem (Bhaskara II,
12th century; modern reconstruction) says that with the minimal-|m^2 - D|
choice the process terminates with k = ±1 and delivers the fundamental
solution: k = 1 gives it directly, k = -1 is squared,
        (a^2 + D*b^2)^2 - D*(2*a*b)^2 = (a^2 - D*b^2)^2 = 1.
The fundamental (minimal-x) character of the result is the classical content
of the method; the oracle checks and the 969-row agreement with the CF route
validate it numerically here, and item 4 spot-checks minimality by brute
force on six small D.

Complexity
----------
Per D: at most 4*isqrt(D) + 50 = O(sqrt(D)) loop iterations (the guard);
each iteration is O(1) big-integer operations plus one modular inverse
(pow(b, -1, |k|) is O(log |k|) modular exponentiation).  Total for all 969
non-square D in 1..1000: on the order of 10^4 exact integer steps; space is
O(1) big integers per D.  No floats, no search over the answer space, no
exponential time or space.  The only brute force (allowed as a check) is
item 4's minimality spot-check on D in {2,3,5,6,7,13}.

Constraints honoured: exact integer arithmetic only (math.isqrt is the only
math facility used), Python standard library only.
"""

import math
import sys
import time


def chakravala(D):
    """Fundamental solution (x, y) of x^2 - D*y^2 = 1 via Chakravala.

    Returns None for square D.  Exact integer arithmetic only.
    """
    if math.isqrt(D) ** 2 == D:
        return None
    a, b, k = math.isqrt(D), 1, math.isqrt(D) ** 2 - D      # invariant a^2 - D*b^2 = k, k < 0
    guard = 0
    while k * k != 1:
        guard += 1
        if guard > 4 * math.isqrt(D) + 50:
            raise RuntimeError(f"chakravala({D}): no convergence within guard")
        bk = b % abs(k)
        inv = pow(bk, -1, abs(k))                           # modular inverse, needs gcd(b,|k|)=1 (theory)
        m0 = (-a * inv) % abs(k)                            # admissible class m = -a*b^{-1} (mod |k|)
        # Nonnegative candidates nearest the minimum of |m^2 - D| are m0 and m0 + |k|
        m = min((m0, m0 + abs(k)), key=lambda z: abs(z * z - D))
        assert (a + b * m) % k == 0 and (a * m + D * b) % k == 0
        a, b, k = abs((a * m + D * b) // k), abs((a + b * m) // k), (m * m - D) // k
    if k == 1:
        return (a, b)
    else:
        return (a * a + D * b * b, 2 * a * b)               # k == -1: square the unit (a + b*sqrt(D))^2


def read_cf_table(path):
    """Read results_cf.tsv into {D: (x, y)}; exact rows only."""
    with open(path, "r", encoding="ascii", newline="") as fh:
        lines = [ln.rstrip("\n") for ln in fh]
    lines = [ln for ln in lines if ln != ""]
    if not lines or lines[0] != "D\tx\ty":
        raise ValueError(f"bad header in {path} (got {lines[0] if lines else '(empty)'!r})")
    table = {}
    for ln in lines[1:]:
        parts = ln.split("\t")
        if len(parts) != 3:
            raise ValueError(f"malformed row in {path}: {ln!r}")
        D, x, y = (int(p) for p in parts)
        if D in table:
            raise ValueError(f"duplicate D={D} in {path}")
        table[D] = (x, y)
    return table


def main():
    t0 = time.perf_counter()
    failures = []   # human-readable problems; exit code = 1 unless empty

    # ------------------------------------------------------------------
    # 1. Oracle self-check BEFORE the full comparison
    # ------------------------------------------------------------------
    oracle = {2: (3, 2), 7: (8, 3), 13: (649, 180)}
    for D in sorted(oracle):
        ex, ey = oracle[D]
        got = chakravala(D)
        ok = (got == (ex, ey)) and (ex * ex - D * ey * ey == 1)
        if ok:
            print(f"oracle PASS D={D}: chakravala({D}) == ({ex}, {ey}), norm x^2 - {D}*y^2 == 1")
        else:
            print(f"oracle FAIL D={D}: chakravala({D}) == {got}, expected ({ex}, {ey})")
            failures.append(f"oracle mismatch at D={D}")

    # ------------------------------------------------------------------
    # 2. Read the CF table and check its integrity
    # ------------------------------------------------------------------
    cf = read_cf_table("results_cf.tsv")
    nonsquares = [D for D in range(1, 1001) if math.isqrt(D) ** 2 != D]

    if len(cf) != len(nonsquares):
        failures.append(f"table has {len(cf)} rows, expected {len(nonsquares)}")
    if set(cf) != set(nonsquares):
        missing = sorted(set(nonsquares) - set(cf))
        extra = sorted(set(cf) - set(nonsquares))
        failures.append(f"table D-set mismatch: missing {missing}, extra {extra}")

    cf_norm_bad = [D for D, (x, y) in cf.items() if x * x - D * y * y != 1]
    if cf_norm_bad:
        failures.append(f"CF rows failing x^2 - D*y^2 == 1: {cf_norm_bad}")

    # ------------------------------------------------------------------
    # 3. Full comparison: Chakravala vs CF, with norm re-asserts
    # ------------------------------------------------------------------
    mismatches = []
    chak = {}
    for D in nonsquares:
        xc, yc = chakravala(D)
        chak[D] = (xc, yc)
        if xc * xc - D * yc * yc != 1:
            failures.append(f"chakravala({D}) does not solve the Pell equation")
        xf, yf = cf[D]
        if (xc, yc) != (xf, yf):
            mismatches.append((D, (xc, yc), (xf, yf)))

    if mismatches:
        for D, (xc, yc), (xf, yf) in mismatches:
            print(f"MISMATCH D={D}: chakravala ({xc}, {yc}) != CF ({xf}, {yf})")
        failures.append(f"{len(mismatches)} mismatched row(s) vs results_cf.tsv")
        print(f"chakravala-CF agreement FAIL ({len(mismatches)} mismatch(es) of {len(nonsquares)} rows)")
    else:
        print("chakravala-CF agreement PASS for all 969 non-square D")

    # ------------------------------------------------------------------
    # 4. Winner over the chakravala results; confirm against the CF winner
    # ------------------------------------------------------------------
    bestD = max(nonsquares, key=lambda D: chak[D][0])
    bestx, besty = chak[bestD]
    print(f"WINNER D = {bestD}, minimal x = {bestx}, minimal y = {besty}")
    known = (
        661,
        16421658242965910275055840472270471049,
        638728478116949861246791167518480580,
    )
    winner_ok = (bestD, bestx, besty) == known and cf[bestD] == (bestx, besty)
    if winner_ok:
        print("winner confirmation PASS: chakravala and CF agree on D=661 with the stated minimal pair")
    else:
        failures.append("winner does not match the stated D=661 minimal pair")

    # ------------------------------------------------------------------
    # 5. Minimality spot-check by small-instance brute force
    #    (allowed ONLY as a check): no y' < y_found solves x^2 - D*y'^2 = 1
    # ------------------------------------------------------------------
    for D in (2, 3, 5, 6, 7, 13):
        xf, yf = chakravala(D)
        assert xf * xf - D * yf * yf == 1
        smaller_solution = None
        for y in range(1, yf):
            rhs = 1 + D * y * y
            if math.isqrt(rhs) ** 2 == rhs:
                smaller_solution = (math.isqrt(rhs), y)
                break
        if smaller_solution is None:
            print(f"minimality spot-check PASS D={D}: no solution with 1 <= y < {yf}")
        else:
            print(f"minimality spot-check FAIL D={D}: smaller solution {smaller_solution} < ({xf}, {yf})")
            failures.append(f"minimality spot-check failed at D={D}")

    # ------------------------------------------------------------------
    # 6. Report
    # ------------------------------------------------------------------
    elapsed = time.perf_counter() - t0
    print(f"verify_chakravala.py wall-clock {elapsed:.3f} s")
    if failures:
        print(f"FAILURES ({len(failures)}):")
        for f in failures:
            print(f"  - {f}")
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())