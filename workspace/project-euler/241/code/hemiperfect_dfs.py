"""Validate the denominator-cancellation DFS for hemiperfect numbers.

We seek all n <= LIMIT with sigma(n)/n = r/2 for odd integer r
(hemiperfect numbers, OEIS A159907).

Method (the standard technique):
  - sigma is multiplicative, so sigma(n)/n = prod sigma(p^a)/p^a.
  - Target T = r/2.  Track reduced residual Q(n) = T*n/sigma(n) = num/den.
    Final answer needs Q = 1.
  - Extending by p^e multiplies Q by p^e/sigma(p^e).
  - FORCING (denominator cancellation): if den > 1 and d is the smallest
    prime factor of den, then d can only be cleared from the denominator by
    introducing prime p = d (because numerator gains p from the p^e factor,
    and d | p^e  <=>  p = d).  Primes are added in nondecreasing order, so d
    must be the NEXT prime introduced.  This keeps the search tiny: large
    primes only ever enter when the denominator demands them.
  - Prunes: Q < 1 (adding prime powers only lowers Q below 1, so no
    completion), n*den > LIMIT (can't restore to integer below limit), and
    reusing an already-used prime.

Output: the set of hemiperfect n <= LIMIT (should match A159907's prefix).
"""
from math import gcd
from sympy import primerange, factorint

LIMIT = 10**18

def sigma_pe(p, e):
    return (p ** (e + 1) - 1) // (p - 1)

# primes we may ever need: since abundancy is bounded, small primes suffice,
# but to be safe use primes up to ~10^6 (larger ones only come in as forced
# factors of a small denominator, which we factor on the fly instead).
PRIMES = list(primerange(2, 2000000))

solutions = {}

def dfs(r, idx, n, num, den):
    """num/den = reduced (r/2)*n/sigma(n).  Add primes from PRIMES[idx] up."""
    g = gcd(num, den)
    num, den = num // g, den // g
    if num == 1 and den == 1:
        solutions.setdefault(r, set()).add(n)
        return
    # cannot overshoot: Q must stay >= 1 (further multiplications lower it)
    if num < den:
        return
    if n > LIMIT:
        return

    d = den  # smallest prime factor of den (den==1 handled above)
    if den > 1:
        d = min(factorint(den))  # forced next prime

    # try next primes in nondecreasing order, starting from either the forced
    # one or the current pointer, whichever is larger.
    for p in PRIMES[idx:]:
        if p < d and den > 1:
            # we are forced to introduce d before anything larger: skipping d
            # leaves it forever in the denominator (prime order nondecreasing).
            continue
        e = 1
        while True:
            pe = p ** e
            n2 = n * pe
            if n2 > LIMIT:
                break
            # new Q = (num/den) * (pe / sigma_pe(p,e))
            sp = sigma_pe(p, e)
            num2 = num * pe
            den2 = den * sp
            if num2 < den2:      # Q < 1 -> can never reach 1
                break
            if n2 * den2 // gcd(num2, den2) > LIMIT:
                break
            # advance idx to next prime (nondecreasing order)
            dfs(r, idx + 1, n2, num2, den2)
            e += 1
        if p >= d and den > 1:
            break  # forced prime d already handled this level

def main():
    # odd r such that r/2 can be an abundancy below the 10^18 max
    for r in range(3, 40, 2):
        # target T = r/2.  Start Q = T = r/2.
        dfs(r, 0, 1, r, 2)
    allsol = set()
    for r in sorted(solutions):
        sols = sorted(s for s in solutions[r] if s <= LIMIT)
        allsol.update(sols)
        print(f"r/2 = {r}/2 : {len(sols)} solutions, sum={sum(sols)}")
    print("\nAll hemiperfect <= 10^18:")
    print(sorted(allsol))
    print("count =", len(allsol), " sum =", sum(allsol))

if __name__ == "__main__":
    main()
