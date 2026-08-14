# PE 351 — independent findings: the result is known, the argument is sound

Question asked of research: is the run's conclusion already published and by
whom; is the method the standard one; is the argument strong enough; and is
"1 attempt on 11 established claims" plausible for a result of this size?

Verdict, bluntly: **the run discovered nothing.** It independently re-derived,
correctly, the published solution to a 2011 Project Euler problem. The
identity, the Φ(10⁸) anchor, the final answer, and the method are all in the
open literature, and no source contradicts the conclusion. The derivation
gains citations; it gains no novelty.

## 1. The result is published — confirmed on four levels, by fresh searches this session

**The answer.** H(10⁸) = 11762187201804552 is the accepted answer to Project
Euler 351 (published by Colin Hughes, 17 Sep 2011). Fresh identical records:
- https://github.com/roosephu/project-euler/blob/master/answers.txt ("351: 11762187201804552")
- https://github.com/lucky-bai/projecteuler-solutions/blob/master/Solutions.md (also nayuki's mirror)
- https://github.com/JuliaLang/julia/blob/82f810d79640d2aac/test/euler.jl ("#351: 11762187201804552")
- https://projecteuler.weebly.com/ and https://oraclesqlpuzzle.ninja-web.net/csharp/csharp-euler-answers.html (same value)

**The closed form.** OEIS A216453, "Number of points hidden from the central
point by a closer point in a hexagonal orchard of order n"
(https://oeis.org/A216453): a(n) = 6·(C(n+1,2) − Σ_{i=1..n} φ(i)), corrected
by **Piyush Kumar and Robert Israel, Aug 26 2014**; equivalently 6·A063985(n)
(**Jon Maiga, Jan 12 2019**). Entry submitted by **V. Raman, Sep 07 2012**,
explicitly linked to PE 351. This is exactly the run's
H(n) = 3n² + 3n − 6·Φ(n). My own `oeis_lookup` on the run's 20 computed
terms returned exactly A216453 — the run's output *is* the catalogue
sequence.

**The Φ(10⁸) anchor.** OEIS A064018 = Φ(10ⁿ)
(https://oeis.org/A064018): a(8) = **3039635516365908** — exactly the run's
value. Terms 0..18 by Hiroaki Yamanouchi; term 19 by Lucas A. Brown,
*Computation of the Totient Summatory Function*, arXiv:2506.07386
(https://arxiv.org/abs/2506.07386). trizen's sublinear implementations print
the same a(10⁸):
https://github.com/trizen/perl-scripts/blob/master/Math/partial_sums_of_euler_totient_function_fast.pl
and https://github.com/trizen/sidef-scripts/blob/master/Math/partial_sums_of_euler_totient_function_recursive.sf.

**The method.** The standard solution. Each of the six congruent sectors of
the hexagon contains C(n+1,2) points; ring i of a sector carries i points of
which φ(i) are coprime (visible), so H(n) = 6·Σ(i−φ(i)) = 6·(n(n+1)/2 − Φ(n)):
- https://euler.stephan-brumme.com/351/ — the canonical public write-up
  (Brumme 2017), same formula, same totient-sieve approach; his segmented
  sieve uses ~30 MB vs the run's 400 MB int32 table — same algorithm class,
  better memory discipline.
- https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/351.py
  (adapted from igorvanloo) — same formula H(n) = 3n(n+1) − 6·Φ(n).
- https://github.com/stbrumme/euler/blob/master/euler-0351.cpp — same.

The "second route" (Möbius identity Φ(n) = ½Σ μ(d)⌊n/d⌋(1+⌊n/d⌋), floor
grouping, Gauss divisor-sum recursion) is the standard sublinear summatory-
totient algorithm (Dirichlet hyperbola / Dujiao sieve), documented in the
same sources (trizen; Brown 2025).

## 2. Is the argument strong enough? Yes — but note what "independent" actually meant

What the argument rests on, and its standing:

1. **Visibility criterion** (hidden ⟺ gcd(|a|,|b|) > 1 in axial
   coordinates): classical (Sylvester 1883; MathWorld VisiblePoint; Farey
   length |F_n| = 1 + Φ(n)), and checked against a literal no-number-theory
   enumeration for small n.
2. **Sector decomposition** → H(n) = 6·(C(n+1,2) − Φ(n)): verified against
   all three statement oracles (H(5)=30, H(10)=138, H(1000)=1177848).
3. **Φ(10⁸) = 3039635516365908**: three computed routes agree exactly — the
   φ sieve, the μ-inversion sum (with a recorded and fixed step-p² sieve bug),
   and the sieve-free floor-grouped A063985 recursion. The catalogue value
   (A064018 a(8)) is the decisive external agreement.

Honest caveat on verification strength: routes 1 and 2 are two
implementations of the same routine class (both O(N)-memory sieves, sharing
the prime list); the genuinely independent confirmations are route 3 (a
different derivation) and the published catalogue value. That is sufficient:
the final answer also equals the accepted answer on five published records.
Doubting the Φ value would mean contradicting A064018, two sieves, the
recursion, and every answer list at once.

**No source contradicts the run's conclusion.** Two near-misses found and
rejected: (a) one auto-generated search summary claimed the value was "not
consistent with the growth pattern" — wrong by a trivial magnitude check,
Φ(10⁸)/10¹⁶ ≈ 0.30396 ≈ 3/π² and H ≈ (3 − 18/π²)·10¹⁶ ≈ 1.176·10¹⁶; (b) a
recalled chunk with the typo "11762189901804552" — refuted by A064018, both
sieves, and every published list (the run's own CONTEXT.md records this
typo). Neither is a real contradiction.

Worked arithmetic, re-checked by hand here: 6·3039635516365908 =
18237813098195448; 3·10¹⁶ + 3·10⁸ = 30000000300000000; difference =
11762187201804552. ✓ Also 6·1960364533634092 = 11762187201804552.

## 3. Is "1 attempt on 11 established claims" plausible? Yes — it is the expected signature of verification, not discovery

One attempt is exactly what a competent execution of a *known* problem looks
like. The identity is the first move a competent solver writes for this
geometry (it is the starting point of Brumme 2017, Raman 2012,
Kumar–Israel 2014, igorvanloo); the φ sieve is a two-line standard; the
eleven claims (visibility criterion, sector count, totient summatory values,
Möbius and Gauss identities) are a normal stock of lemmas for that chain —
each of them individually published, several already in OEIS. A genuinely
*new* result of this size would be expected to take many attempts, precisely
because the correct path would not be pre-charted. Here the fast convergence
is the signature of solving a 2011 problem whose published solution the run
re-derived from scratch, with the arithmetic landing on the catalogue value.

## 4. What the run should cite, and what it should not claim

Citable sources (all independently re-found this session):
- OEIS A216453 (formula; Raman 2012; Kumar–Israel 2014; Maiga 2019)
- OEIS A064018 + Brown arXiv:2506.07386 (Φ(10⁸) and its sublinear computation)
- Brumme's write-up https://euler.stephan-brumme.com/351/ (same method)
- Classical visibility / Farey theory (Sylvester 1883; MathWorld VisiblePoint)

What it should not claim: novelty. The run's own CLAIMS.md and CONTEXT.md
already mark the identities as sourced/checked rather than new — good
provenance hygiene. The final report should state the value, name these
sources, and describe the result as a verified re-derivation of the published
answer.

Sources rejected as irrelevant (for the record, so nobody re-searches):
- "Orchards in elliptic curves over finite fields" (Padmanabhan–Shukla 2020) — a different "orchard" problem.
- Visible-lattice-point generalizations (Goins et al. 2018, Ramanujan J.; visible points along curves) — confirm the gcd criterion, contain no hexagonal-orchard formula.

## URL list

- https://projecteuler.net/problem=351 — canonical statement, published 2011
- https://oeis.org/A216453 — the closed form, linked to PE 351
- https://oeis.org/A064018 — Φ(10ⁿ); a(8) = 3039635516365908
- https://arxiv.org/abs/2506.07386 — Brown, Computation of the Totient Summatory Function (2025)
- https://euler.stephan-brumme.com/351/ — standard solution, same formula and method
- https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/351.py — same formula
- https://github.com/roosephu/project-euler/blob/master/answers.txt — "351: 11762187201804552"
- https://github.com/lucky-bai/projecteuler-solutions/blob/master/Solutions.md — "351. 11762187201804552"
- https://github.com/JuliaLang/julia/blob/82f810d79640d2aac/test/euler.jl — "#351: 11762187201804552"
- https://github.com/trizen/perl-scripts/blob/master/Math/partial_sums_of_euler_totient_function_fast.pl — a(10⁸) example
- https://mathworld.wolfram.com/VisiblePoint.html — gcd=1 visibility, density 6/π²