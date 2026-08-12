"""Corrected denominator-cancellation DFS for hemiperfect numbers (PE 241).

Applies to all n <= LIMIT with sigma(n)/n = r/2 for odd r.

Residual: Q(n) = (r/2)*n/sigma(n) = u/v (reduced).  Solution iff Q = 1.
Extending by prime power p^e multiplies Q by p^e/sigma(p^e), a factor < 1.

Forcing: if v > 1 and d is the smallest prime factor of v, then the ONLY
prime we may introduce next is d (its numerator contribution p^e is the only
place a factor of d can enter, and primes are added in nondecreasing order).
The exponent of the forced prime d must be exactly a = v_p(v):
  - e < a leaves d in the denominator forever (d added once; sigma(p^e) is
    coprime to p), so Q can never reach 1;
  - e > a leaves surplus d in the numerator that no later sigma factor can
    cancel (all coprime to d), again blocking Q = 1;
  - e == a cancels the denominator power exactly.
Skipped primes (p < d) are permanently excluded, and the recursion continues
from index i+1, so a prime is never reused.

Prunes: u < v (Q<1), n > LIMIT, and n*(reduced denominator) > LIMIT.
"""
import sys
from math import gcd
from sympy import primerange, factorint

LIMIT = int(sys.argv[1]) if len(sys.argv) > 1 else 10**18

def sigma_pe(p, e):
    return (p ** (e + 1) - 1) // (p - 1)

# small primes to draw from; large primes enter only as forced factors of a
# small denominator, which we factor on the fly rather than iterating to.
PRIMES = list(primerange(2, 2_000_000))

solutions = {}


def dfs(r, idx, n, u, v):
    g = gcd(u, v)
    u, v = u // g, v // g
    if u == 1 and v == 1:
        solutions.setdefault(r, set()).add(n)
        return
    if u < v or n > LIMIT:
        return

    d = None
    if v > 1:
        d = min(factorint(v))          # forced next prime
        a = 0
        w = v
        while w % d == 0:
            w //= d
            a += 1                     # d^a || v; exponent must equal a

    for i in range(idx, len(PRIMES)):
        p = PRIMES[i]
        if d is not None and p < d:
            continue                   # may not skip the forced prime d
        if d is not None and p > d:
            break                      # only d may be introduced at this level
        # here (if d is not None) p == d
        estart = 1 if d is None else a
        e = estart
        while True:
            pe = p ** e
            n2 = n * pe
            if n2 > LIMIT:
                break
            sp = sigma_pe(p, e)
            u2 = u * pe
            v2 = v * sp
            if u2 < v2:                # Q < 1 -> can never return to 1
                break
            den_red = v2 // gcd(u2, v2)
            if n2 * den_red > LIMIT:
                break
            dfs(r, i + 1, n2, u2, v2)  # continue past prime p (no reuse)
            e += 1
        if d is not None:
            break                      # forced prime handled at this level


def main():
    # odd r reachable below 10^18: A088912 gives a(1..6)=
    # 2,24,4320,8910720,1.7e16,1.7e44 ; so below 10^18 only r in 3..11 qualifies.
    # Harmlessly iterate a little beyond to confirm those unreachable paths die.
    for r in range(3, 40, 2):
        dfs(r, 0, 1, r, 2)             # Q = r/2

    allsol = set()
    for r in sorted(solutions):
        sols = sorted(s for s in solutions[r] if s <= LIMIT)
        allsol.update(sols)
        print(f"r/2 = {r}/2 : {len(sols)} solutions, sum={sum(sols)}")
    print("\nAll hemiperfect <= %d:" % LIMIT)
    print(sorted(allsol))
    print("count =", len(allsol), " sum =", sum(allsol))


if __name__ == "__main__":
    main()
