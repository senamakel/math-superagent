"""Verify the Graf-von-Bothmer coefficient-descent mechanism and its exact char-p break.

The claim (Graf von Bothmer 2007, Prop 2.5/2.6): for degree d = p^k or 2p^k,
X_d(Fbar_p) is empty -- i.e. there is NO char-p CA counterexample of that
degree. Mechanism = coefficient descent: if (d choose d-i) == 0 mod p for the
leading handful of indices, then the Hasse derivative P_{d-i} reduces to
(something forcing) a_i = 0, rippling down to force all a_i = 0, giving the
trivial point (excluded as projective).

The break for d = p+1 (the witness degree): (p+1 choose p) = p+1 != 0 mod p,
so P_p = X + a_1 does NOT force a_1 = 0; the descent stalls at the first step
and the witness x^{p+1} - x^p exists.

This script computes, for each degree d and prime p:
  * whether (d choose i) == 0 mod p for i = 1..d-1 (the full descent hypothesis
    of Prop 2.5), i.e. p | d and d = p -> no: Prop 2.5 needs d a prime POWER.
  * whether the leading pivot (d choose d-1) == 0 mod p -- the first step that
    must vanish for the descent to start.
It tabulates the boundary: for which (d,p) does the descent pivot vanish, and
cross-checks against the known char-p facts (d=p^k empty; d=p+1 witness).

Complexity: O(d * log) small arithmetic. Exact integer arithmetic (sympy).
"""
from sympy import binomial, primerange


def full_descent(d, p):
    """True iff (d choose i) == 0 mod p for ALL i in 1..d-1 (Prop 2.5 hypothesis)."""
    for i in range(1, d):
        if binomial(d, i) % p != 0:
            return False
    return True


def pivot_vanishes(d, p):
    """True iff the first descent pivot (d choose d-1) == 0 mod p."""
    return binomial(d, d - 1) % p == 0


def is_prime_power(d):
    from sympy import factorint
    f = factorint(d)
    return len(f) == 1


rows = []
for d in range(2, 31):
    for p in primerange(2, 30):
        full = full_descent(d, p)
        pivot = pivot_vanishes(d, p)
        pp = is_prime_power(d)
        row = (d, p, full, pivot, pp)
        rows.append(row)

print("== Descent pivot vanishes (d choose d-1 = d == 0 mod p) by degree ==")
for tri in [3, 6, 4, 5, 12, 20, 24, 28]:
    pivs = [p for (d, p, full, pivot, pp) in rows if d == tri and pivot]
    fulls = [p for (d, p, full, pivot, pp) in rows if d == tri and full]
    print(f"  d={tri:2d}: pivot-{tri}==0 mod p at p in {pivs}; full-descent(Prop2.5) at p in {fulls}")

print()
print("== Check: d=p^k has full descent at p; d=p+1 witness has pivot NONZERO at p ==")
for (d, p) in [(3, 3), (5, 5), (9, 3), (25, 5), (27, 3)]:  # p^k cases
    print(f"  d={d}, p={p}: full_descent={full_descent(d, p)}  (expect True)")
for (d, p) in [(4, 3), (6, 5), (8, 7), (12, 11)]:  # p+1 witness cases
    print(f"  d={d}, p={p}: full_descent={full_descent(d, p)} (witness degree; expect False), "
          f"pivot={pivot_vanishes(d,p)} (expect False)")
