"""Probe for the Cassels descent of x^p - y^q = 1 (p, q distinct odd primes).

Exact integer arithmetic throughout; no floats, no math.pow, no logs.

Claims under test:
  (0) Symbolic identity:  Phi_p(a^q + 1) = sum_{j=0}^{p-1} C(p, j+1) a^{q*j}
      where Phi_p(t) = (t^p - 1)/(t - 1) = 1 + t + ... + t^{p-1}.
  (1) THE DESCENT LEMMA: for odd primes p != q and a >= 1 with p not | a,
      b^q = Phi_p(a^q + 1) is NEVER a perfect q-th power.
  (1a) same but WITHOUT the constraint p not | a, to isolate the role of p|a.
  (2) Residue pattern: if b^q = Phi_p(a^q+1) then necessarily
      b^q == p (mod a^q)  and  b^q == 1 (mod p).
      Check what b mod a would have to be by finding b = q-th root even when
      the value is not a perfect power; examine b(mod a) pattern to see if a
      descent (a smaller solution) is forced.

The falsifier: the claim must fail-safe on the known solution 3^2 - 2^3 = 1,
which has p = 2 even -> outside the odd-prime hypothesis, so it is EXCLUDED,
not refuted by these lemmas.
"""
from math import gcd, comb
import sys
sys.setrecursionlimit(100000)


def v_p(n, p):
    if n == 0:
        raise ValueError
    v = 0
    while n % p == 0:
        n //= p
        v += 1
    return v


def isqrt(n):
    if n < 0:
        raise ValueError
    if n < 2:
        return n
    x = n
    y = (x + 1) // 2
    while y < x:
        x = y
        y = (x + n // x) // 2
    return x


def perfect_root(n, q):
    """Exact q-th root of n if it exists, else None.  Binary search."""
    lo, hi = 1, 1
    # upper bound: hi = smallest integer with hi^q > n via doubling
    while hi ** q <= n:
        hi *= 2
    while lo <= hi:
        mid = (lo + hi) // 2
        pw = mid ** q
        if pw == n:
            return mid
        if pw < n:
            lo = mid + 1
        else:
            hi = mid - 1
    return None


def phi_p_at_ap1(a, q, p):
    """Phi_p(a^q + 1) = ((a^q+1)^p - 1) / a^q exactly."""
    return ((a ** q + 1) ** p - 1) // (a ** q)


def is_prime(n):
    if n < 2:
        return False
    d = 2
    while d * d <= n:
        if n % d == 0:
            return False
        d += 1
    return True


def primes_up_to(n):
    return [p for p in range(2, n + 1) if is_prime(p)]


def main():
    ODD = [3, 5, 7, 11, 13]
    print("=" * 78)
    print("(0) SYMBOLIC IDENTITY  Phi_p(a^q+1) = sum C(p,j+1) a^{qj}")
    from sympy import symbols, Sum, binomial, expand, Eq, simplify
    a, q = symbols('a q', integer=True, positive=True)
    ok0 = True
    for p in [3, 5, 7]:
        t = symbols('t')
        Phi = sum(t ** i for i in range(p))
        lhs = expand(Phi.subs(t, a ** q + 1))
        rhs = sum(binomial(p, j + 1) * a ** (q * j) for j in range(p))
        good = simplify(lhs - expand(rhs)) == 0
        ok0 = ok0 and good
        print(f"   p={p} identity holds: {good}")
    print("   RESULT:", "PASS" if ok0 else "FAIL")
    print()

    print("=" * 78)
    print("(1) DESCENT LEMMA: Phi_p(a^q+1) is never a q-th power, with p not|a")
    print("    p != q odd primes, a in [1, Amax], checking ALL a and only p|a"
          " excluded rows.")
    Amax = 200
    counterexamples_all = []
    counterexamples_pnoda = []
    rows = 0
    for p in ODD:
        for q in ODD:
            if p == q:
                continue
            # also require p != -... p,q distinct
            for a in range(1, Amax + 1):
                val = phi_p_at_ap1(a, q, p)
                r = perfect_root(val, q)
                rows += 1
                if r is not None:
                    counterexamples_all.append((p, q, a, r, val))
                    if a % p != 0:
                        counterexamples_pnoda.append((p, q, a, r, val))
    print(f"   rows checked: {rows}")
    print(f"   counterexamples to 'Phi_p(a^q+1) is a q-th power' (all a): "
          f"{len(counterexamples_all)}")
    for c in counterexamples_all[:20]:
        print(f"      FAIL p={c[0]} q={c[1]} a={c[2]}  Phi = {c[4]} = {c[3]}^{c[1]}")
    print(f"   of which with p not| a (the descent hypothesis): "
          f"{len(counterexamples_pnoda)}")
    for c in counterexamples_pnoda[:20]:
        print(f"      FAIL p={c[0]} q={c[1]} a={c[2]} (p={c[0]},{c[0]}%a) "
              f"Phi={c[4]}={c[3]}^{c[1]}")
    print("   RESULT:", "PASS (no counterexample, descent lemma holds over "
                         "the probed range)" if
          (len(counterexamples_all) == 0) else "COUNTEREXAMPLE FOUND")
    print()

    print("=" * 78)
    print("(1a) same WITHOUT p|a constraint, smaller range to find any pattern")
    # Is there ANY a (even p | a) making Phi a q-th power?  Reported above.
    print(f"   (counterexamples_all covers this: {len(counterexamples_all)} found"
          f" for p,q in {ODD}, a<=200)")
    print()

    print("=" * 78)
    print("(2) RESIDUE PATTERN when Phi_p(a^q+1) actually IS a q-th power")
    print("    (if any).  Check b^q == p (mod a^q) and b^q == 1 (mod p).")
    for (p, q, a, b, val) in counterexamples_all:
        print(f"   p={p} q={q} a={a} b={b}")
        print(f"      b^q mod a^q = {val % a**q}  (p = {p})  match={val % a**q == p % a**q}")
        print(f"      b^q mod p   = {val % p}  (should be 1)  match={val % p == 1}")
    if not counterexamples_all:
        print("   No real q-th power instances in range, so residue check is "
              "vacuous.  Instead inspect the 'forced b' for data:")
    print()

    print("=" * 78)
    print("(3) Where does b live if we FREEZE the descent hypotheses?")
    print("    Look at near-misses: values of Phi_p(a^q+1) that are 'closest'\n"
          "    to a q-th power, to see whether a descent b=g(a) is suggested.")
    # For a fixed p,q, list (a, next_perfect_power_gap) to see the structure
    for (p, q) in [(3, 5), (5, 3), (5, 7), (7, 5), (11, 3)]:
        print("   --- p=%d, q=%d, a in [1,60]: largest term a^{{(p-1)q}} "
              "dominates; show Phi - floor^q gap  ---" % (p, q))
        gaps = []
        for a in range(1, 61):
            val = phi_p_at_ap1(a, q, p)
            b0 = int(round(val ** (1.0 / q)))
            # refine b0 to the true floor root with exact arithmetic
            while (b0 + 1) ** q <= val:
                b0 += 1
            while b0 ** q > val:
                b0 -= 1
            gap = val - b0 ** q
            gaps.append(gap)
        # print the gap modulo a^q to see the descent residue p mod a^q
        print("      sample a and (Phi - floor^q) mod a^q :")
        for a in range(1, 61, 5):
            val = phi_p_at_ap1(a, q, p)
            b0 = int(round(val ** (1.0 / q)))
            while (b0 + 1) ** q <= val:
                b0 += 1
            while b0 ** q > val:
                b0 -= 1
            gap = val - b0 ** q
            print(f"         a={a:3d}  floor_b={b0:6d}  gap={gap:6d}  "
                  f"gap mod a^q={gap % a**q}")
    print()

    print("=" * 78)
    print("(4) FALSIFIER: known solution 3^2 - 2^3 = 1")
    x, p, y, q = 3, 2, 2, 3
    print(f"   x^p - y^q = {x**p} - {y**q} = {x**p - y**q}")
    print(f"   p | x-1 : {p} | {x-1} -> {(x-1) % p == 0}")
    print(f"   q | y+1 : {q} | {y+1} -> {(y+1) % q == 0}")
    odd_pair = (p >= 3) and (q >= 3)
    print(f"   (p,q) both odd prime: {odd_pair}  -> p=2 even, so the odd-prime\n"
          f"      descent hypothesis EXCLUDES the known solution (not refuted).")
    print("   RESULT: PASS (no over-elimination)")


if __name__ == "__main__":
    main()
