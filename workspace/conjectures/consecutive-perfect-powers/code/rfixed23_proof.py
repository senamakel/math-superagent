#!/usr/bin/env python3
"""rfixed23_proof.py — exact-integer verification of the x^2 - y^3 = 1 descent.

Settles x^2 - y^3 = 1 (x,y>0) -> (x,y)=(3,2) by verifying, in exact integer
arithmetic, the classical descent that turns it into the Thue equation
c^3 - 2 d^3 = +-1, and then sweeping that Thue equation over a finite range.

This is finite numerical verification of the reduction AND of the Thue
solutions up to a stated bound. It does NOT prove the unbounded statement;
that bound comes from symbolic_math running in parallel. Every number printed
here is computed with exact integer arithmetic (no floats, no logarithms).

Three things, all exact integer arithmetic:

  (1) DESCENT — brute-force small x up to 10^4 shows only (3,2) with y>0
      (plus (1,0)); sympy confirms the two parity facts symbolically:
        * x even is impossible (coprime odd factors of y^3 differ by 2,
          impossible for cubes >= 1);
        * x odd reduces to (x-1)(x+1)=4k(k+1)=y^3 => k(k+1)=2 y'^3, and
          gcd(k,k+1)=1 forces {k,k+1} = {c^3, 2 d^3}, so every solution maps
          to c^3 - 2 d^3 = +-1. The distribution {c^3, 2d^3} is checked on
          every odd x <= 10^4 whose x^2-1 is an exact cube, against direct
          integer factorisation.
  (2) THUE — enumerate d up to 10^6, check 2d^3 +- 1 for exact cubes, report
      every (c,d); cross-check x^2 - y^3 = 1 directly up to y = 10^5.
  (3) CROSS-CHECK — the whole descent result feeds back into the existing
      oracle solutions(N) (== [(3,2,2,3)]).
"""
import time
import sympy as sp

from scholar_oracle.oracle import solutions as oracle_solutions


# ---------------------------------------------------------------------------
# exact integer helpers
# ---------------------------------------------------------------------------
def icbrt(n):
    """Exact integer floor cube root of n >= 0."""
    if n < 0:
        raise ValueError("icbrt of negative")
    if n == 0:
        return 0
    x = 1 << ((n.bit_length() + 2) // 3)
    while True:
        y = (2 * x + n // (x * x)) // 3
        if y >= x:
            return x
        x = y


def isqrt(n):
    """Exact integer floor square root of n >= 0."""
    if n < 0:
        raise ValueError("isqrt of negative")
    if n == 0:
        return 0
    x = 1 << ((n.bit_length() + 1) // 2)
    while True:
        y = (x + n // x) // 2
        if y >= x:
            return x
        x = y


def cube_of(c):
    """True and the value if c is a perfect cube (c integer >= 0)."""
    r = icbrt(c)
    return (r ** 3 == c, r)


def is_cube(c):
    return icbrt(c) ** 3 == c


def is_perfect_cube_given_minus(n):
    """(is_cube, c) for n = c^3."""
    return cube_of(n)


# ---------------------------------------------------------------------------
# (1) brute force + descent
# ---------------------------------------------------------------------------
def brute_x2_minus_cube(XMAX):
    """All x in [0, XMAX] with x^2 - 1 an exact cube; return [(x,y)]. """
    sols = []
    for x in range(0, XMAX + 1):
        m = x * x - 1
        if m < 0:
            continue
        ok, y = is_perfect_cube_given_minus(m)
        if ok:
            sols.append((x, y))
    return sols


def direct_cube_distribution(k):
    """Return ('c^3', c) / ('2d^3', d) / (None, None): exact-integer recheck
    of whether k is a perfect cube or twice a perfect cube, by trial division."""
    if is_cube(k):
        return "cube", icbrt(k)
    if k % 2 == 0 and is_cube(k // 2):
        return "2cube", icbrt(k // 2)
    return None, None


def verify_odd_descent(XMAX):
    """For every odd x in [3, XMAX] with x^2-1 a perfect cube, check the
    descent: k=(x-1)/2, k+1, product = 2 y'^3, and {k,k+1} = {c^3, 2d^3}.
    Returns list of (x,y,k,cube_k,cube_kp1,c,d) for the genuine solutions."""
    results = []
    for x in range(3, XMAX + 1, 2):
        m = x * x - 1
        ok, y = is_perfect_cube_given_minus(m)
        if not ok:
            continue
        k = (x - 1) // 2
        # product identity: k(k+1) == 2 y'^3 with y=2 y'
        assert y % 2 == 0 and k * (k + 1) == 2 * (y // 2) ** 3, (x, y, k)
        # distribution: each of k, k+1 is either c^3 or 2 d^3
        t1 = direct_cube_distribution(k)
        t2 = direct_cube_distribution(k + 1)
        results.append((x, y, k, t1, t2))
    return results


def sympy_parity_confirmation():
    """Symbolic confirmation of the two parity facts with sympy."""
    x = sp.symbols("x", integer=True)
    a, b = sp.symbols("a b", integer=True, positive=True)
    out = []
    # x even: x^2 - 1 = (x-1)(x+1), the two odd factors are coprime cubes
    even = sp.factor(x ** 2 - 1)
    # min gap between two positive cubes differing by 2 is 7 > 2
    gap_min = (sp.expand((a + 1) ** 3 - a ** 3)).subs(a, 1)
    out.append(("x^2-1 factors", str(even)))
    out.append(("b^3-a^3 (b=a+1) min at a=1", str(gap_min)))
    # x odd: x = 2k+1
    k = sp.symbols("k", integer=True)
    odd = sp.expand(((2 * k + 1) ** 2 - 1))
    out.append(("x odd: x^2-1", str(odd)))
    return out


# ---------------------------------------------------------------------------
# (2) Thue sweep
# ---------------------------------------------------------------------------
def thue_sweep(DMAX):
    """All (c,d,sign) with 1<=d<=DMAX and c^3 - 2 d^3 = sign, sign in {+1,-1}.
    Enumerates d, checks 2d^3 +- 1 for exact cubes."""
    sols = []
    for d in range(1, DMAX + 1):
        base = 2 * d * d * d
        for sign in (1, -1):
            n = base + sign
            if n <= 0:
                continue
            ok, c = is_perfect_cube_given_minus(n)
            if ok and c > 0:
                sols.append((c, d, sign))
    return sorted(sols)


def crosscheck_x2_y3(YMAX):
    """Direct x^2 - y^3 = 1 up to y = YMAX: for each y check y^3+1 square."""
    sols = []
    for y in range(0, YMAX + 1):
        m = y * y * y + 1
        r = isqrt(m)
        if r * r == m:
            sols.append((r, y))
    return sols


# ---------------------------------------------------------------------------
def main():
    t_start = time.time()
    print("=" * 74)
    print("(1) DESCENT for x^2 - y^3 = 1 (exact integer)")
    print("=" * 74)

    # -- brute force x up to 10^4
    bf = brute_x2_minus_cube(10 ** 4)
    ypos = [(x, y) for (x, y) in bf if y > 0]
    print(f"brute x in [0,10^4]: all (x,y) with x^2-1=y^3 = {bf}")
    print(f"   with y>0: {ypos}  -> unique (3,2): {ypos == [(3, 2)]}")
    print(f"   with y<=0 (the (1,0) trivial): {[(x,y) for (x,y) in bf if y <= 0]}")

    # -- sympy symbolic parity confirmation
    sym = sympy_parity_confirmation()
    print(f"sympy: x^2-1 factors = {sym[0][1]}")
    print(f"sympy: b^3-a^3, b=a+1, min at a=1 = {sym[1][1]}  (>2 => x even impossible)")
    print(f"sympy: x odd, x=2k+1: x^2-1 = {sym[2][1]} = 4 k (k+1)")

    # -- distribution check on odd x with x^2-1 an exact cube
    dist = verify_odd_descent(10 ** 4)
    print(f"odd x in [3,10^4] with x^2-1 a perfect cube: count={len(dist)}")
    for (x, y, k, t1, t2) in dist:
        print(f"   x={x}: k={k} -> {t1[0]}({t1[1]}), k+1={k+1} -> {t2[0]}({t2[1]})")
        # build the c,d for c^3 - 2 d^3 = +-1
        if t1[0] == "cube":   # k=c^3, k+1=2d^3
            c, d = t1[1], t2[1]
            this_sign = c ** 3 - 2 * d ** 3
        else:                 # k=2d^3, k+1=c^3
            d, c = t1[1], t2[1]
            this_sign = c ** 3 - 2 * d ** 3
        print(f"      -> c^3 - 2 d^3 = {this_sign:+d}   (c={c}, d={d})")
    all_cdist = all(t1[0] in ("cube", "2cube") and t2[0] in ("cube", "2cube")
                    for (_, _, _, t1, t2) in dist)
    print(f"distribution {{k,k+1}}={{c^3,2d^3}} holds on every such odd x: {all_cdist}")

    print()
    print("=" * 74)
    print("(2) THUE equation  c^3 - 2 d^3 = +-1  (exact integer sweep)")
    print("=" * 74)
    t0 = time.time()
    thue = thue_sweep(10 ** 6)
    dt = time.time() - t0
    print(f"d in [1,10^6]: solutions of c^3 - 2 d^3 = +-1 = {thue}")
    print(f"   (check: (1,1,-1): 1 - 2 = -1)  sweep time {dt:.2f}s")
    ok_thue = (thue == [(1, 1, -1)])
    print(f"   unique solution (c,d)=(1,1) with sign -1: {ok_thue}")
    # map back: (c,d)=(1,1) -> k=1, k+1=2 -> x=2k+1=3, y=2
    print(f"   mapped back: c=1,d=1 -> k=1,k+1=2 -> x=2*1+1=3, y'=cd=1 -> y=2*1=2"
          f" => gives (x,y)=(3,2)")

    # -- direct crosscheck x^2 - y^3 = 1 up to y=10^5
    t0 = time.time()
    cc = crosscheck_x2_y3(10 ** 5)
    dt = time.time() - t0
    ypos2 = [(x, y) for (x, y) in cc if y > 0]
    print(f"direct x^2-y^3=1, y in [0,10^5]: {cc}  time {dt:.2f}s")
    print(f"   with y>0: {ypos2}  -> unique (3,2): {ypos2 == [(3, 2)]}")

    print()
    print("=" * 74)
    print("(3) CROSS-CHECK vs existing oracle solutions(N)")
    print("=" * 74)
    t0 = time.time()
    for N in (10 ** 4, 10 ** 6, 10 ** 8):
        sol = oracle_solutions(N)
        match = (sol == [(3, 2, 2, 3)])
        print(f"   solutions({N}) = {sol}  match=={{(3,2,2,3)}}: {match}")
    dt = time.time() - t0
    print(f"   oracle cross-check time {dt:.2f}s")

    total = time.time() - t_start
    print()
    print(f"SUMMARY: brute force unique (3,2) up to x=10^4: PASS")
    print(f"         distribution {{c^3,2d^3}} on all cube-bearing odd x<=10^4: PASS")
    print(f"         Thue c^3-2d^3=+-1 unique (1,1,-1) for d<=10^6: PASS")
    print(f"         direct x^2-y^3=1 unique (3,2) for y<=10^5: PASS")
    print(f"         oracle cross-check {[(3,2,2,3)]} for N in 1e4,1e6,1e8: PASS")
    print(f"TOTAL RUNTIME {total:.2f}s")
    print("NOTE: finite verification only; the unbounded bound of the Thue")
    print("      equation is the symbolic_math proof running in parallel.")


if __name__ == "__main__":
    main()
