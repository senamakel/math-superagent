#!/usr/bin/env python3
"""code/brute.py — the naive oracle for the Erdos-Straus equation 4/n = 1/x+1/y+1/z.

Obviously correct, not fast. Exact rational arithmetic only: solves() uses
fractions.Fraction (or integer cross-multiplication) and never a float.

This is the ground truth every other program in this run is measured against.
It does three things:

  solves(n, x, y, z)   -- is 4/n = 1/x + 1/y + 1/z with x,y,z positive ints?
  naive_solve(n, cap)  -- blindly search ordered 0 < x <= y <= z <= cap for a
                          witness of n. Bounded; only for small n. This is the
                          oracle's answer to "does a solution exist in range".
  main()               -- reproduces every worked example in the statement.

Method note on naive_solve: WLOG take 0 < x <= y <= z (reorder to canonical
form and check the unordered set). With x <= y <= z we have 4/n = sum <= 3/x,
so x <= 3n/4, and the first term alone gives 1/x <= 4/n so x >= n/4. Then for
each x, 1/y + 1/z = 4/n - 1/x, and y ranges from x up to 2/(4/n - 1/x). The
search costs O((n/4)^2) per n in the worst case — polynomial, fine for the
tiny n used here, and it is capped so a slow case cannot run away.
"""

from __future__ import annotations

from fractions import Fraction
from itertools import count
import json
import math
import os


def solves(n: int, x: int, y: int, z: int) -> bool:
    """True iff 4/n == 1/x + 1/y + 1/z with n, x, y, z positive integers.

    Exact integer cross-multiplication: 4/n = 1/x+1/y+1/z  <=>
    4*x*y*z == n*(y*z + x*z + x*y). Both sides are exact ints; no floats.

    Raises ValueError if any argument is non-positive.
    """
    if min(n, x, y, z) <= 0:
        raise ValueError("solves requires positive integers")
    lhs = 4 * x * y * z
    rhs = n * (y * z + x * z + x * y)
    return lhs == rhs


def _canonical(a: int, b: int, c: int) -> tuple[int, int, int]:
    """Order a,b,c ascending, so an (x,y,z) check is order-independent."""
    return tuple(sorted((a, b, c)))  # type: ignore[return-value]


def naive_solve(n: int, cap: int = 2000) -> tuple[int, int, int] | None:
    """Naive ordered search for a positive solution with x <= y <= z <= cap.

    Returns the first found (as ascending triple) or None. Cap stops a slow
    case; for the tiny n the worked examples use, this returns in milliseconds.
    This is a brute-force oracle and is only ever pointed at small n.
    """
    lb_x = max(1, (n + 3) // 4)          # n/4 <= x  (since 1/x <= 4/n)
    for x in range(lb_x, min(cap, n + 1) + 1):
        # remainder r = 4/n - 1/x = (4x - n)/(n*x) must equal 1/y + 1/z.
        den_x = 4 * x - n
        if den_x <= 0:
            continue
        # 1/y + 1/z = den_x/(n*x).  With y <= z:  2/z <= rem <= 2/y  => ...
        # y must satisfy 1/rem <= y, i.e. y >= n*x/den_x, and y <= 2/rem.
        y_lo = max(x, (n * x + den_x - 1) // den_x)
        y_hi = min(cap, (2 * n * x) // den_x)
        for y in range(y_lo, y_hi + 1):
            # 1/z = rem - 1/y = (den_x*y - n*x) / (n*x*y)
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


def _frac_identity_compatible(n: int, x: int, y: int, z: int) -> bool:
    """Cross-check a claim using Fraction directly (independent route)."""
    return Fraction(4, n) == Fraction(1, x) + Fraction(1, y) + Fraction(1, z)


def check_worked_examples() -> None:
    """Run every worked example from the statement and report agreement."""
    results: list[tuple[str, bool, str]] = []

    # 1. Even case: n = 2m, 4/(2m) = 1/m + 1/(2m) + 1/(2m).
    even_ok = True
    for m in range(1, 50):
        n = 2 * m
        x, y, z = m, 2 * m, 2 * m
        if not (solves(n, x, y, z) and _frac_identity_compatible(n, x, y, z)):
            even_ok = False
            break
    results.append((
        "even identity  4/(2m)=1/m+1/(2m)+1/(2m)  for m=1..49",
        even_ok,
        "checked exact int + Fraction",
    ))

    # 2. n == 3 (mod 4). The brief's lead identity is WRONG (it solves 3/n).
    #    The corrected identity is:
    #      n=4k+3, x=(n+1)/4, y=n(n+1)/4+1, z=y(y-1)
    #    Checked exactly and symbolically below. Here we check it directly as
    #    a family for many n (no blind search cap involved).  Note: a naive
    #    search capped at 1e5 finds NO witness for n=683 (z=1.36e10), which
    #    is why sweep failures are cap artifacts, not missing solutions.
    mod4_ok = True
    bad_mod4 = []
    for kk in range(0, 2000):
        nn = 4 * kk + 3
        xx = (nn + 1) // 4
        yy = nn * (nn + 1) // 4 + 1
        zz = yy * (yy - 1)
        if not (xx > 0 and yy > 0 and zz > 0 and solves(nn, xx, yy, zz)):
            mod4_ok = False
            bad_mod4.append(nn)
            break
    results.append((
        "n==3 (mod 4): corrected family solves for n=3..7999",
        mod4_ok,
        f"bad={bad_mod4}",
    ))

    # 3. All witnesses in witnesses.json.
    wpath = os.path.join(os.path.dirname(__file__), "out", "witnesses.json")
    with open(wpath) as fh:
        data = json.load(fh)
    witness_ok = True
    bad: list[str] = []
    for cls, ws in data["witnesses"].items():
        for entry in ws:
            n = entry["n"]
            xyz = entry["xyz"]
            if not (solves(n, *xyz) and _frac_identity_compatible(n, *xyz)):
                witness_ok = False
                bad.append(f"{n}:{xyz}")
    results.append((
        "all witnesses.json entries solve",
        witness_ok,
        f"bad={bad} count={sum(len(v) for v in data['witnesses'].values())}",
    ))

    # 4. Value sanity: n=1 has no solution (4==max sum 3); n=2 via even case.
    results.append((
        "n=1 has no positive solution (max of 1/x+1/y+1/z is 3)",
        naive_solve(1, cap=200) is None,
        "naive_solve(1) -> None",
    ))

    # Print a table.
    print(f"{'worked example':<58} {'ok' if True else ''}")
    print("-" * 78)
    all_ok = True
    for label, ok, note in results:
        all_ok = all_ok and ok
        print(f"{'PASS' if ok else 'FAIL':<4} {label:<54} [{note}]")
    print("-" * 78)
    print(f"overall: {'ALL WORKED EXAMPLES MATCH' if all_ok else 'SOME FAILED'}")
    return all_ok


def symbolic_identity_check() -> None:
    """Symbolically verify the corrected n==3 (mod 4) covering identity, and
    show the brief's typed lead is FALSE (it solves 3/n, not 4/n)."""
    from sympy import simplify, symbols
    k = symbols("k")
    n = 4 * k + 3
    # Corrected family: x=(n+1)/4, y=n(n+1)/4+1, z=y(y-1)
    x = (n + 1) / 4
    y = n * (n + 1) / 4 + 1
    z = y * (y - 1)
    diff = 4 / n - (1 / x + 1 / y + 1 / z)
    s = simplify(diff)
    print("symbolic: 4/n-(1/x+1/y+1/z), x=(n+1)/4, y=n(n+1)/4+1, z=y(y-1), n=4k+3 ->",
          s)
    assert s == 0
    # Now show the brief's lead, as literally typed, fails:
    xb, yb, zb = n, (n + 1) / 2, n * (n + 1) / 2
    sb = simplify(4 / n - (1 / xb + 1 / yb + 1 / zb))
    print("brief's typed lead solves  4/n == RHS?  diff =", sb,
          " (nonzero => it is the 3/n, not 4/n, identity)")
    assert sb != 0


if __name__ == "__main__":
    ok = check_worked_examples()
    symbolic_identity_check()
    print("naive oracle (brute.py) done. exit-ok =", ok)
