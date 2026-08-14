#!/usr/bin/env python3
"""brute.py — the naive exact-integer oracle for x^p - y^q = 1.

Deliberately obvious, not fast. Exact integer arithmetic only (Python's
arbitrary-precision ints; no floats, no logarithms, no math.pow), because x^p
overflows a float long before the bound becomes interesting and a float
comparison manufactures solutions that are not there.

The statement's one worked example is (x,p,y,q) = (3,2,2,3): 3^2 - 2^3 = 1.
The naive oracle must return EXACTLY this for every reachable N >= 9.

Structure:
  perfect_powers(N)  -> dict value -> list[(base, exp)]  for n = base^exp with
                        2 <= base, 2 <= exp, value <= N.
  solutions(N)       -> sorted list of all (x,p,y,q), x^p,y^q <= N, x^p-y^q=1,
                        by checking consecutive perfect-power values.
"""


def perfect_powers(N):
    """value -> [(base, exp)] for every perfect power value <= N.

    Iterates over bases x >= 2 with x^2 <= N, then over exponents e >= 2 while
    x^e <= N. Exact integer arithmetic: each power is built by repeated exact
    multiplication, never via float ** or logarithms.
    """
    powers = {}
    x = 2
    while x * x <= N:
        v = x * x
        e = 2
        while v <= N:
            powers.setdefault(v, []).append((x, e))
            v *= x   # exact integer multiplication: next power x^(e+1)
            e += 1
        x += 1
    return powers


def solutions(N):
    """sorted list of every (x, p, y, q) with x^p,y^q <= N and x^p - y^q = 1,
    x,y > 0, p,q > 1. Pure exact int arithmetic; verifies the identity itself."""
    powers = perfect_powers(N)
    result = set()
    for u, reps_u in powers.items():   # u = x^p (a perfect power)
        if u - 1 in powers:            # u - 1 = y^q (also a perfect power)
            for (x, p) in reps_u:
                for (y, q) in powers[u - 1]:
                    if x ** p - y ** q == 1:
                        result.add((x, p, y, q))
    return sorted(result)


def main():
    import time
    # The statement's only worked example: (3, 2, 2, 3); 3^2 - 2^3 = 9 - 8 = 1.
    # N = 9 is the smallest sensible bound (needs 9 and 8 both). Validate each
    # reachable N from 9 upward through the ladder.
    expected = {(3, 2, 2, 3)}
    for N in (9, 100, 1000, 10 ** 4, 10 ** 5, 10 ** 6):
        t0 = time.time()
        r = solutions(N)
        dt = time.time() - t0
        ok = set(r) == expected
        print(f"N={N:<8} result={r}  {'OK' if ok else 'MISMATCH'}  {dt:.3f}s")
        if not ok:
            print("FAILED: naive oracle returned something other than the "
                  "worked example.")
            return 1
    print("Naive oracle returns exactly (3,2,2,3) for every N in "
          "{9, 100, 1000, 1e4, 1e5, 1e6}.")


if __name__ == "__main__":
    main()
