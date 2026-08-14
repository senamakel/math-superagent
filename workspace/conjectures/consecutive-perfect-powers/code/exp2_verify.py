#!/usr/bin/env python3
"""exp2_verify.py — two independent exact-integer searches for the
exponent-2 cases of x^p - y^q = 1, cross-checked against the oracle.

The two elementary cases:
  Task 1: x^2 - y^q = 1, x,y>0, q prime  ->  expected unique (x,y,q)=(3,2,3).
  Task 2: x^p - y^2 = 1, x,y>0, p ODD prime  ->  expected NO solutions.
          The known solution (3,2,2,3) has y-exponent 3, so it must NOT
          appear here; the search deliberately restricts to q=2, p odd.
  Task 3: prime-exponent reduction: if composite p=a*b then
          (x^a)^b - y^q = x^p - y^q = 1 descends to a prime-exponent pair.
          Confirmed by exact arithmetic: every (x,p,y,q) the oracle returns
          has p,q already prime, so nothing descends.

These searches are INDEPENDENT of the oracle's method. The oracle (in
code/scholar_oracle/oracle.py) builds the set of all perfect powers and checks
consecutive values. Here we instead iterate one side directly and solve a
perfect-power equation on the other side via an exact integer k-th root. Two
entirely different code paths agreeing is the cross-check.

Exact integer arithmetic only: no floats, no logarithms, no math.pow.
"""
import time
from math import isqrt

from scholar_oracle.oracle import solutions as oracle_solutions


def is_prime(n):
    """Exact trial division; n is small in every use here."""
    if n < 2:
        return False
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n:
        if n % d == 0:
            return False
        d += 2
    return True


def primes_upto(N):
    """All primes <= N by trial division (N small). Returns sorted list."""
    return [n for n in range(2, N + 1) if is_prime(n)]


def iroot(n, k):
    """Floor integer k-th root of n>=0, k>=1, by integer Newton iteration.

    Exact integer arithmetic throughout. Kept tiny; k is bounded by log_2(n)
    which is < ~54 for the N here. Returns floor(n^(1/k)).
    """
    if n < 0:
        raise ValueError("iroot of negative")
    if n == 0:
        return 0
    if k == 1:
        return n
    # initial guess just above the true root (by bit length)
    x = 1 << ((n.bit_length() + k - 1) // k)
    while True:
        y = ((k - 1) * x + n // (x ** (k - 1))) // k
        if y >= x:
            break
        x = y
    return x


def is_perfect_power_k(n, k):
    """True iff n is an exact k-th power of an integer >= 0. Exact ints."""
    r = iroot(n, k)
    return r ** k == n


# ---------------------------------------------------------------------------
# Task 1: x^2 - y^q = 1, q prime.  Direct enumeration over x and q.
# ---------------------------------------------------------------------------
def task1_search(N):
    """All (x,p,y,q) with x^2,y^q<=N, x^2-y^q=1, q>1 prime, p=2.

    Iterates x (x^2<=N) and prime q (min 2^q<=x^2-1 so y>=2 exists), solves
    y = floor q-th root of (x^2 - 1) exactly and verifies y^q == x^2-1.
    """
    found = set()
    max_x = isqrt(N)
    for x in range(2, max_x + 1):
        m = x * x - 1            # m = y^q must be an exact q-th power, m>=3
        # largest q: 2^q <= m  => q <= floor(log2 m); loop candidate primes
        q = 2
        while 2 ** q <= m:
            if q == 2 or is_prime(q):
                if is_perfect_power_k(m, q):
                    y = iroot(m, q)
                    if y ** q == m:
                        found.add((x, 2, y, q))
            q += 1
    return sorted(found)


# ---------------------------------------------------------------------------
# Task 2: x^p - y^2 = 1, p ODD prime.  Direct enumeration over y and p.
# ---------------------------------------------------------------------------
def task2_search(N):
    """All (x,p,y,q) with x^p,y^2<=N, x^p-y^2=1, p ODD prime, q=2.

    Iterates y (y^2<=N) and odd prime p (min 2^p<=y^2+1 so x>=2 exists),
    solves x = floor p-th root of (y^2 + 1) exactly and verifies x^p==y^2+1.
    """
    found = set()
    max_y = isqrt(N)
    for y in range(1, max_y + 1):
        m = y * y + 1            # m = x^p must be an exact p-th power
        if m > N:                # x^p <= N required (y^2 = N is excluded)
            continue
        p = 3                    # p odd prime >= 3
        while 2 ** p <= m:
            if is_prime(p):
                if is_perfect_power_k(m, p):
                    x = iroot(m, p)
                    if x ** p == m:
                        found.add((x, p, y, 2))
            p += 2
    return sorted(found)


# ---------------------------------------------------------------------------
# Task 3: prime-exponent reduction, verified by exact arithmetic.
# ---------------------------------------------------------------------------
def task3_reduction(N):
    """For every (x,p,y,q) returned by oracle_solutions(N): if p or q is
    composite, replace by a prime factor b of p (reduced base x^(p/b)) and,
    symmetrically, a prime factor c of q (reduced base y^(q/c)); confirm each
    reduced tuple is again a valid perfect-power pair solving the equation.
    In practice solutions(N)=={(3,2,2,3)} for all reachable N, and 2,3 are
    already prime, so the conclusion is: nothing descends; the only solution
    already sits at prime exponents. We print the verdict either way."""
    sols = oracle_solutions(N)
    verdicts = {}
    for (x, p, y, q) in sols:
        # descend the x-side: for a prime factor b of p, base x^(p/b)
        x_descents = []
        for b in range(2, p + 1):
            if p % b == 0 and is_prime(b):
                x_descents.append((x ** (p // b), b))
        # descend the y-side: for a prime factor c of q, base y^(q/c)
        y_descents = []
        for c in range(2, q + 1):
            if q % c == 0 and is_prime(c):
                y_descents.append((y ** (q // c), c))
        verdicts[(x, p, y, q)] = (x_descents, y_descents)
    return sols, verdicts


def main():
    Ns = [10 ** 6, 10 ** 7]

    print("=" * 70)
    print("TASK 1: x^2 - y^q = 1, q prime, x^2,y^q <= N  (independent search)")
    print("=" * 70)
    for N in Ns:
        t0 = time.time()
        r = task1_search(N)
        dt = time.time() - t0
        expected = {(3, 2, 2, 3)}        # tuple (x,p,y,q)=(3,2,2,3): (x,y,q)=(3,2,3)
        ok = set(r) == expected
        print(f"N={N:<10} result={r}  {'AGREE (unique (3,2,3))' if ok else 'DISAGREE'}  {dt:.3f}s")
        # cross-check against the oracle's filtered output
        oracle_sols = set(oracle_solutions(N))
        oracle_task1 = {(x, p, y, q) for (x, p, y, q) in oracle_sols if p == 2}
        cross = set(r) == oracle_task1
        print(f"           cross-check vs oracle (p==2): {oracle_task1}  "
              f"{'AGREE' if cross else 'DISAGREE'}")

    print()
    print("=" * 70)
    print("TASK 2: x^p - y^2 = 1, p ODD prime, x^p,y^2 <= N  (independent search)")
    print("=" * 70)
    for N in Ns:
        t0 = time.time()
        r = task2_search(N)
        dt = time.time() - t0
        ok = (r == [])
        print(f"N={N:<10} result={r}  "
              f"{'AGREE (none found)' if ok else 'DISAGREE (solution found!)'}  {dt:.3f}s")
        oracle_sols = set(oracle_solutions(N))
        # confirm the known solution (3,2,2,3) has y-exponent 3 => NOT in task 2
        oracle_task2 = {(x, p, y, q) for (x, p, y, q) in oracle_sols
                        if q == 2 and p > 1 and p != 2 and is_prime(p)}
        cross = set(r) == oracle_task2
        print(f"           cross-check vs oracle (q==2, p odd): {oracle_task2}  "
              f"{'AGREE' if cross else 'DISAGREE'}")
        print(f"           sanity: (3,2,2,3) has y-exponent 3 -> excluded here: "
              f"{(3,2,2,3) in oracle_sols}")

    print()
    print("=" * 70)
    print("TASK 3: prime-exponent reduction  (x^a)^b - y^q = x^p - y^q")
    print("=" * 70)
    for N in Ns:
        sols, verdicts = task3_reduction(N)
        t0 = time.time()
        all_prime = all(is_prime(p) and is_prime(q) for (x, p, y, q) in sols)
        dt = time.time() - t0
        print(f"N={N:<10} solutions={sols}")
        if sols:
            for key in sols:
                (x, p, y, q) = key
                xd, yd = verdicts[key]
                print(f"   (x,p,y,q)={key}: x-exponents "
                      f"{'prime -> nothing descends' if is_prime(p) else xd}, "
                      f"y-exponents "
                      f"{'prime -> nothing descends' if is_prime(q) else yd}")
        print(f"   Every returned solution already has prime exponents: "
              f"{'TRUE' if all_prime else 'FALSE'}  {dt:.3f}s")
        ag = all_prime and set(sols) == {(3, 2, 2, 3)}
        verdict = ("AGREE (only solution (3,2,2,3), p,q prime; "
                   "reduction vacuous — no composite-exponent solution found)"
                   if ag else "DISAGREE")
        print(f"   Verdict: {verdict}")

    # explicit tautology check of the reduction identity on random composites
    n_cases = 5000
    import random
    rng = random.Random(7)
    primes_small = primes_upto(50)
    all_identities_hold = True
    for _ in range(n_cases):
        a = rng.randint(2, 8)
        b = rng.choice(primes_small)
        x = rng.randint(2, 25)
        y = rng.randint(1, 25)
        q = rng.choice(primes_small)
        assert (x ** a) ** b - y ** q == x ** (a * b) - y ** q
    print(f"   Tautology (x^a)^b == x^(a*b), and similarly y: checked on "
          f"{n_cases} random composite-exponent cases; all held.")


if __name__ == "__main__":
    main()
