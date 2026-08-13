# Mond & Portier, "Ternary Egyptian fractions with prime denominator"

Source: A. Mond, J. Portier, Res. Number Theory 8 (2022) #41. https://doi.org/10.1007/s40993-022-00339-4 (open access, CC-BY)
Full text: `research/sources/ternary-egyptian-prime-denominator.full.md`

## What it is

A counting paper about m/p (m fixed-index, p prime) as a sum of three unit
fractions — i.e. the general "ternary Egyptian fraction with prime
denominator" problem whose m = 4 case is the Erdős–Straus conjecture.

## The result

For A_3(p) = #{ m ∈ ℕ : m/p = 1/m₁ + 1/m₂ + 1/m₃ } over primes p ≤ x:
- Luca–Pappalardi 2019: x(log x)³ ≪ Σ A_3(p) ≪ x(log x)⁵.
- **Theorem 1.2 (this paper): Σ_{p≤x} A_3(p) ≪ x(log x)³(log log x)²**, closing
  the upper/lower gap up to a polyloglog factor. Proof follows Elsholtz–Tao's
  divisor-counting method, with a Burgess-bound refinement of their
  Proposition 1.4 (here Prop 3.4: Σ_{a≤A,b≤B} τ(kab²+1) ≪ AB log(A+B) for
  k ≤ A^p, p < 5/3).

## The claim that matters for this run — Lemma 2.1 (Mordell's classification)

If m/p = 1/m₁+1/m₂+1/m₃ with gcd(m,p)=1, then either m ∈ {1,2,3} or there
exist positive integers a,b,c,u with gcd(a,b)=1, c | a+b, and either

- **Type I**:  m = (p + (a+b)/c) / (abu)  ⟺  p = 4abu − (a+b)/c  (m=4),
- **Type II**: m = (1 + p(a+b)/c) / (abu)  ⟺  p = (4abu − 1) c/(a+b)  (m=4).

Source is Mordell's *Diophantine Equations* (1969), per Lemma 2.1's citation.

## Why it is in this library

It is an independent, primary restatement of the **two-family Type I/II
parametrisation** for the prime case of 4/p = 1/x+1/y+1/z that the problem's
phase-2 instruction says to "establish, verify against a known solution, and
build on." For m = 4:

- Type I: p = 4abu − (a+b)/c, gcd(a,b)=1, c | a+b.
- Type II: p = (4abu − 1)·c/(a+b), gcd(a,b)=1, c | a+b.

These match the Bloom–Elsholtz survey's two congruence families
(claim `bell-esc-equivalence-congruence-classes`) and Elsholtz–Tao Prop 2.1/2.5
(p = 4abcd − f with f | 4a²d + 1, etc.). It is a *second* source for that
completeness, so the parametrisation is no longer resting on one paper's word.

## Verification status

Sourced (full text read). The specialisation to m = 4 above is an algebra
substitution (p = ma bu − ... with m = 4), not yet re-checked by the run's
oracle; treat the m = 4 forms as asserted-until-verified against
`code/out/witnesses.json`.
