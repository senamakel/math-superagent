# Cassels divisibility — the elementary reduction (rising-sea ground)

Author: goals@rising-sea, attempt 3. Status: structural reduction PROVED here
(the four identities below are one-line algebraic proofs); the reduced-system
exclusion is the open lemma, being swept exactly by tool_builder
(`code/cassels/elementary_structure.py`) and attacked by symbolic_math.

## The reduction (all steps elementary, no class group)

Let (x, p, y, q) solve x^p - y^q = 1 with p, q distinct odd primes.

**R1 (equivalence p|y ⟺ p|x−1).** Reduce mod p: Fermat gives x^p ≡ x (mod p),
so y^q ≡ x^p − 1 ≡ x − 1 (mod p). If p | y then y^q ≡ 0, hence x ≡ 1 (mod p).
Conversely x ≡ 1 (mod p) forces p | y^q, and p prime forces p | y. ∎

**R2 (gcd lemma).** Φ_p(x) := (x^p−1)/(x−1) = 1 + x + … + x^{p−1} ≡ 1+…+1 = p
(mod x−1), so gcd(x−1, Φ_p(x)) = gcd(x−1, p) ∈ {1, p}. ∎

**R3 (perfect-power split).** y^q = (x−1)·Φ_p(x). If p ∤ y (equivalently
p ∤ x−1, by R1), then R2 gives the two factors coprime, so each is a perfect
q-th power: x − 1 = a^q and Φ_p(x) = b^q, with y = ab, a ≥ 1, p ∤ a. ∎

**R4 (binomial expansion).** Φ_p(t+1) = ((t+1)^p − 1)/t = Σ_{j=0}^{p−1} C(p, j+1) t^j.
With t = a^q: Φ_p(a^q + 1) = p + C(p,2) a^q + C(p,3) a^{2q} + … + a^{(p−1)q}. ∎

## The reduced-system lemma (open — the real content of Cassels' p|y)

**L1:** For odd primes p ≠ q and a ≥ 1 with p ∤ a, Φ_p(a^q + 1) is NOT a
perfect q-th power.

If L1 holds, then p ∤ y is impossible (R3 contradicts L1 at x = a^q + 1), so
p | y, hence p | x−1. The mirror (factor y^q + 1 = (y+1)·Φ_q(−y), same
argument with the plus sign / y ≡ −1 mod q) gives q | x ⟺ q | y+1. Together:
**Cassels's theorem p|y, q|x is exactly equivalent to L1 + its mirror.**

Note the special case a = 1 (x = 2): Φ_p(2) = 2^p − 1 = b^q needs separate
handling (classically no solutions for odd prime p, q ≥ 2; small case).

## Falsifier calibration

Known solution (x,p,y,q) = (3,2,2,3): p = 2 is even, so every hypothesis above
(p, q odd primes) fails — the lemma set never excludes the known solution.
The concluded divisibilities hold trivially there: p|y = 2|2, q|x = 3|3,
2 | x−1 = 2, 3 | y+1 = 3.

## What the descent must use (sketch, unverified)

b^q ≡ Φ_p(a^q+1) ≡ p (mod a^q) by R4 (all terms after the first carry a^q).
Also every prime divisor r ≠ p of b satisfies ord_r(a^q + 1) = p, so
r ≡ 1 (mod p). The classical argument compares b^q = p + m·a^q against
consecutive q-th powers near a^{q(p−1)}; the exact closing step is what
symbolic_math is deriving and what the sweep is testing numerically.
**Do not cite the closing step until it is on disk with a check.**
