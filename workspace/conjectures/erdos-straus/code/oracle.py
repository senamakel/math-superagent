#!/usr/bin/env python3
"""code/oracle.py — the Erdős–Straus verifier and identity checker.

This is the ground-truth oracle the whole run is measured against.  It holds
three things, in exact arithmetic only (no floats anywhere):

  solves(n, x, y, z)   -- integer cross-multiplication: is 4/n = 1/x+1/y+1/z
                           with n, x, y, z positive integers?
  is_identity(...)     -- sympy: does a proposed parametric family satisfy
                           4/n(k) - 1/x(k) - 1/y(k) - 1/z(k) == 0
                           exactly, as a rational function of k?
  main()               -- reproduces every worked example from problem.md:
                           even case, the n ≡ 3 (mod 4) identity (symbolically
                           and numerically), prime-reduction scaling, every
                           witness in witnesses.json, and a deliberately small
                           brute-force sweep over n in [2, 200].

Run:
    timeout 540 python3 code/oracle.py 2>&1 | tee code/out/oracle.captured.txt

The symmetry of solves is order-independent: checking an unordered
{x, y, z} set and an ordered triple give the same answer because the equation
is invariant under permuting the three unit fractions.
"""

from __future__ import annotations

from fractions import Fraction
import json
import os

from sympy import simplify, symbols


def solves(n: int, x: int, y: int, z: int) -> bool:
    """True iff 4/n == 1/x + 1/y + 1/z with n, x, y, z positive integers.

    Exact integer cross-multiplication:
        4/n = 1/x + 1/y + 1/z
      <=> 4*x*y*z = n*(y*z + x*z + x*y)
    Both sides are exact integers; never a float.

    Raises ValueError on any non-positive argument.
    """
    if min(n, x, y, z) <= 0:
        raise ValueError("solves requires positive integers")
    return 4 * x * y * z == n * (y * z + x * z + x * y)


def solves_fraction(n: int, x: int, y: int, z: int) -> bool:
    """Independent route through fractions.Fraction, for cross-checking."""
    return Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)


def is_identity(x_expr_k, y_expr_k, z_expr_k, n_of_k, k_symbol=None):
    """Symbolically verify a parametric family is an exact identity in k.

    Takes four sympy expressions (polynomials or rational functions) in the
    same symbolic variable `k` (default the sympy symbol 'k'):
        x(k), y(k), z(k)  -- candidate denominators
        n(k)              -- the n each triple is meant to solve
    Returns True iff  4/n(k) - 1/x(k) - 1/y(k) - 1/z(k)  simplifies to
    exactly zero as a rational function of k.

    This is the check that a "family" is really an identity and not just a
    family that happens to work for the first few k.  It settles infinitely
    many n at once.

    NOTE: does not itself check integrality or positivity of the denominators
    — those are separate conditions that must be stated and checked (the run
    does that numerically for the n ≡ 3 (mod 4) family below).
    """
    if k_symbol is None:
        k_symbol = symbols("k")
    diff = 4 / n_of_k - (1 / x_expr_k + 1 / y_expr_k + 1 / z_expr_k)
    return simplify(diff) == 0


def naive_solve(n: int, cap: int = 4000) -> tuple[int, int, int] | None:
    """Brute-force oracle: first positive solution with x <= y <= z <= cap.

    Returns the canonical ascending triple, or None if nothing in range.
    Bounded by `cap`; only ever pointed at small n.  This is the oracle's
    answer to "does a witness exist within range", kept deliberately small.

    Bound reasoning (used to shrink the loop, exact integer arithmetic):
    x <= y <= z  implies  4/n <= 3/x, so x <= 3n/4, and 1/x <= 4/n gives
    x >= n/4.  Then for fixed x, remainder r = 4/n - 1/x = (4x-n)/(nx), and
    y <= z gives y >= x, 1/rem <= y, y <= 2/rem — an O(n^2) loop total.
    """
    lb_x = max(1, (n + 3) // 4)
    for x in range(lb_x, min(cap, n + 1) + 1):
        den_x = 4 * x - n
        if den_x <= 0:
            continue
        y_lo = max(x, (n * x + den_x - 1) // den_x)
        y_hi = min(cap, (2 * n * x) // den_x)
        for y in range(y_lo, y_hi + 1):
            num = den_x * y - n * x
            if num <= 0:
                continue
            den = n * x * y
            if den % num != 0:
                continue
            z = den // num
            if z < y or z > cap:
                continue
            return (x, y, z)
    return None


# --------------------------------------------------------------------------
# Worked examples from problem.md
# --------------------------------------------------------------------------

def check_even_case() -> bool:
    """Even case: 4/(2m) = 1/m + 1/(2m) + 1/(2m) for m = 1..49."""
    for m in range(1, 50):
        n = 2 * m
        x, y, z = m, 2 * m, 2 * m
        if not (solves(n, x, y, z) and solves_fraction(n, x, y, z)):
            return False
    return True


def check_mod3_identity_symbolic() -> bool:
    """4/n = 1/n + 1/((n+1)/2) + 1/(n(n+1)/2) for n ≡ 3 (mod 4), as identity in k.

    Substitue n = 4k+3 so (n+1)/2 = 2k+2 and n(n+1)/2 are integers.  Verify
    the rational-function identity in k and that denominators are positive
    integers for k = 0..9.
    """
    k = symbols("k")
    n = 4 * k + 3
    x = n
    y = (n + 1) / 2
    z = n * (n + 1) / 2
    ident = is_identity(x, y, z, n, k_symbol=k)
    pos = all(
        solves(4 * kk + 3, 4 * kk + 3, (4 * kk + 3 + 1) // 2,
               (4 * kk + 3) * (4 * kk + 3 + 1) // 2)
        for kk in range(10)
    )
    return ident and pos


def check_mod3_identity_numeric() -> bool:
    """Independent numeric check: naive search finds a witness for every odd
    n == 3 (mod 4) below 2000 (not required to be the identity's triple)."""
    for n in range(3, 2000, 4):
        w = naive_solve(n, cap=4000)
        if w is None or not solves(n, *w):
            return False
    return True


def check_prime_reduction() -> bool:
    """Prime reduction: if 4/p solves, then scaling by m/p solves m (multiple of p).

    Demo: take p = 3.  4/3 = 1/1 + 1/3 + 1/3  (the mod-3 identity, n=3).
    Let base = (x, y, z) = (1, 3, 3).  For any m that is a multiple of p=3,
    claim  (x*m/3, y*m/3, z*m/3) solves m.  Demonstrates on m = 3, 6, 9, 30.
    Verifies both the concrete equality and that the general claim holds for
    a spread of multiples.
    """
    p = 3
    base = (1, 3, 3)
    if not solves(p, *base):
        return False
    for m in (3, 6, 9, 15, 30, 99, 300):
        if m % p != 0:
            return False
        scale = m // p
        scaled = tuple(v * scale for v in base)
        if not solves(m, *scaled):
            return False
    return True


def check_witnesses() -> tuple[bool, int]:
    """Every witness in code/out/witnesses.json must pass solves()."""
    wpath = os.path.join(os.path.dirname(__file__), "out", "witnesses.json")
    with open(wpath) as fh:
        data = json.load(fh)
    total = 0
    for cls, entries in data["witnesses"].items():
        for entry in entries:
            total += 1
            n = entry["n"]
            xyz = entry["xyz"]
            if not (solves(n, *xyz) and solves_fraction(n, *xyz)):
                return False, total
    return True, total


def brute_sweep(max_n: int = 200, cap: int = 4000) -> tuple[int, int, list[int]]:
    """Direct search x <= y <= z for every n in [2, max_n].

    Kept deliberately small (max_n <= 200 as required).  Returns
    (solved_count, total_count, unsolved_list).
    """
    solved = 0
    unsolved: list[int] = []
    for n in range(2, max_n + 1):
        w = naive_solve(n, cap=cap)
        if w is not None and solves(n, *w):
            solved += 1
        else:
            unsolved.append(n)
    return solved, max_n - 1, unsolved


def main() -> bool:
    checks: list[tuple[str, bool, str]] = []

    # 1. even case
    c = check_even_case()
    checks.append(("even identity 4/(2m)=1/m+1/(2m)+1/(2m), m=1..49", c,
                   "exact int + Fraction"))

    # 2. n == 3 (mod 4) identity, symbolic
    c = check_mod3_identity_symbolic()
    checks.append(("mod-3 identity symbolic (n=4k+3), integer+positive denom",
                   c, "sympy simplify == 0"))

    # 3. n == 3 (mod 4) identity, numeric
    c = check_mod3_identity_numeric()
    checks.append(("mod-3: naive witness for every n<2000, n==3 mod 4", c,
                   "direct search cap=4000"))

    # 4. prime reduction
    c = check_prime_reduction()
    checks.append(("prime reduction: scale p=3 solution to multiples", c,
                   "m=3,6,9,15,30,99,300"))

    # 5. witnesses
    c, total = check_witnesses()
    checks.append(("all witnesses.json entries solve", c, f"count={total}"))

    # 6. brute sweep
    solved, total, unsolved = brute_sweep(200, cap=4000)
    checks.append((
        f"brute sweep n in [2,200]: {solved}/{total} solved, "
        f"unsolved={unsolved}",
        solved == total,
        "x<=y<=z cap=4000, all solved (conjecture holds in range)",
    ))

    print(f"{'PASS/FAIL':<9} {'worked example / check':<52} [note]")
    print("-" * 88)
    all_ok = True
    for label, ok, note in checks:
        all_ok = all_ok and ok
        print(f"{'PASS' if ok else 'FAIL':<9} {label:<52} [{note}]")
    print("-" * 88)
    print(f"overall: {'ALL WORKED EXAMPLES MATCH' if all_ok else 'SOME FAILED'}")
    return all_ok


if __name__ == "__main__":
    import sys
    ok = main()
    sys.exit(0 if ok else 1)
