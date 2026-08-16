# Hunde Eba — "Sieving for the Primes to Prove Their Infinitude" (Missouri J. Math. Sci.)

Source: https://doi.org/10.35834/mjms/1513306829 · full text: [[eba-inclusion-exclusion.full]]

## What it establishes

A short teaching article (Misssouri J. Math. Sci. 29(2):176–183, 2017). Uses a sieve built on the **inclusion–exclusion principle** to prove, by contradiction, the infinitude of primes — an alternative to Euclid's proof. The sieve expresses a property of the primes in terms of the prime-counting function.

## Consequences for this problem

Not needed. The run's inclusion–exclusion use (claim `inclusion-exclusion-sourceable`) is the standard finite-set |∪A_i| = Σ(-1)^{|J|+1}|∩A_i| formula applied to the divisors of 2^60−1 in the Möbius-inversion route — sourced to Wikipedia/Stanford inclusion–exclusion. Eba applies inclusion–exclusion to the sieve for a *proof of infinitude of primes*, entirely different application; it offers nothing new for computing Σ{n: s(n)=60}.

## Does not settle

Nothing relevant to the PE622 computation or to the exact inclusion–exclusion statement the run already holds.

## Status

Theorem: none usable here. The paper's contribution is a pedagogical proof technique, orthogonal to the run's goals.

## Verdict

**Does not help** — the inclusion–exclusion formula the run needs is already sourced and proved in `inclusion-exclusion-sourceable`; this source applies the principle in a direction PE622 does not use (a sieve proof of prime infinitude, not a divisor count/sum).
