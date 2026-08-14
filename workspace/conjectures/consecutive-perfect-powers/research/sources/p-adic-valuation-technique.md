# Technique: p-adic valuation (LTE) and the cyclotomic valuation identities behind the divisibility conditions

**Status:** Method/technique note written by the librarian. It records the *valuation techniques* the run uses; it does NOT record the published divisibility conditions for x^p - y^q = 1 (which the policy screens and the run must re-derive).

**Why this matters:** The problem's open gaps (BACKWARD.md G-Cassels, G-double-wieferich) reduce to the two valuation computations:
```
v_p(x^p - 1) = 1 + v_p(x - 1)     (LTE, p odd)
v_q(y^q + 1) = 1 + v_q(y + 1)
```
These force p | y and q | x once combined with the equation via the cyclotomic factorisation. The exact form of the double-Wieferich conditions must be **derived**, not copied from problem.md (whose hint "p^2 | y^{p-1} - 1" contradicts Cassels's p | y).

## The Lifting The Exponent (LTE) lemma

For an odd prime p, integers a, b with p | (a-b) and p ∤ ab:
```
v_p(a^n - b^n) = v_p(a - b) + v_p(n)
```
and for n odd,
```
v_p(a^n + b^n) = v_p(a + b) + v_p(n).
```
For p = 2 there are refined versions. This is the tool that computes v_p(x^p - 1) when p | (x-1): since x^p - 1 = (x-1)(1+x+...+x^{p-1}) and v_p(1+x+...+x^{p-1}) = 1 when p | (x-1), we get v_p(x^p-1) = v_p(x-1) + 1.

## The cyclotomic factorisation / ideal factorisation technique

In Z[zeta_p],
```
x^p - 1 = product_{i=1}^{p} (x - zeta_p^i)
```
The ideals (x - zeta_p^i) are pairwise coprime off the unique ramified prime (1 - zeta_p). Since the extension is totally ramified at p with (p) = (1-zeta_p)^{p-1}, all other primes are unramified, giving the "nearly coprime" structure. This is what lets the q-th-power equation y^q = x^p - 1 force each (x - zeta^i) to be a q-th power of an ideal, up to the ramified prime.

## The norm identity

N_{Q(zeta_p)/Q}(1 - zeta_p) = p (the product of (1-u) over primitive p-th roots is p — Lemma 5 in Nguyen's note). This is the exact value behind v_p computations at the ramified prime.

## What the run does with this (not what the answer is)

The run must re-derive, using these tools:
1. Cassels's divisibility: p | y and q | x for a solution with distinct odd primes p, q. (The known solution 3^2 - 2^3 = 1 has p = 2, so it is outside the odd-prime hypothesis — a lemma must state this explicitly.)
2. The double-Wieferich congruences, in their exact form, derived from the cyclotomic unit relation forced by p | y and q | x.
3. The exact form must be verified against the oracle check_conditions(p,q) calibrated so the known solution is excluded only by the odd-prime hypothesis.

The published final forms are NOT stored here; they are to be derived. This note only fixes the techniques.
