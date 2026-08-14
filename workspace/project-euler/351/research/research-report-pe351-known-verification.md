# PE 351 — result-status verification report

Asked: is the run's solution known (published, and by whom), is the method
standard, does anything contradict the conclusion, and is "1 attempt on 11
established claims" plausible?

## Verdict, bluntly

**The run did not discover anything. It re-derived, independently and
correctly, the published solution to a 2011 Project Euler problem.** The
answer, the closed form, the Φ(10⁸) anchor, and the method are all in the
open literature. That is the finding: the derivation should cite the sources
below instead of presenting the result as new. The argument itself is sound —
verified here against three independent published records, with no
contradiction found.

## 1. The closed form is published: OEIS A216453

- **Sequence A216453**, "Number of points hidden from the central point by a
  closer point in a hexagonal orchard of order n",
  https://oeis.org/A216453 — submitted by **V. Raman, Sep 07 2012**, who
  linked the entry to Project Euler 351.
- **Formula (exactly what the run uses):**
  a(n) = 6·(C(n+1,2) − Σ_{i=1..n} φ(i)), corrected by **Piyush Kumar and
  Robert Israel, Aug 26 2014**; equivalently a(n) = 6·A063985(n),
  **Jon Maiga, Jan 12 2019**.
- The run's own `oeis_lookup` on its 20 computed terms
  0,6,12,24,30,54,60,84,102,138,144,192,198,246,288,336,342,414,420,492
  returned exactly A216453 — the run's output *is* the catalogue sequence,
  computed from scratch.

## 2. The answer is the published PE 351 answer

H(10⁸) = **11762187201804552** matched independently by fresh web searches
this session (not just the earlier report's list):

- https://github.com/lucky-bai/projecteuler-solutions/blob/master/Solutions.md
  (entry "351." followed by 11762187201804552)
- https://github.com/JuliaLang/julia/blob/82f810d79640d2aac/test/euler.jl
  ("#351: 11762187201804552")
- the run's own earlier search found the same value in:
  https://github.com/roosephu/project-euler/blob/master/answers.txt and
  https://projecteuler.weebly.com/

The canonical published source of the answer is Project Euler problem 351
itself (published 2011;
https://projecteuler.net/problem=351 and /minimal=351).

## 3. The Φ(10⁸) anchor is published: OEIS A064018

- a(n) = Φ(10^n) = Σ_{k≤10^n} φ(k), https://oeis.org/A064018.
- The b-file row **"8 3039635516365908"** (terms 0..18 by Hiroaki Yamanouchi,
  term 19 by Lucas A. Brown) is exactly the value the run computed by two
  independent sieves. I read the b-file directly this session
  (research/sources/oeis-A064018-... / b-file copy): rows 1..9 =
  1, 32, 3044, 304192, 30397486, 3039650754, 303963552392, 30396356427242,
  3039635516365908 — matching the run's list row-for-row.
- An independent third source reproduces the same value as an algorithm
  example output: trizen's partial-sums-of-φ scripts,
  https://github.com/trizen/perl-scripts/blob/master/Math/partial_sums_of_euler_totient_function_fast.pl
  ("a(10^8) = 3039635516365908").

## 4. The method is the standard one

The run's route — one sixth of the hexagon, points as fractions p/q with
gcd(p,q) > 1 hidden, φ(i) visible on ring i, hence
H(n) = 6·Σ(i−φ(i)) = 6·(n(n+1)/2 − Φ(n)) — is the textbook solution. I
downloaded and read the full treatment this session:

- **Stephan Brumme's solution write-up**,
  https://euler.stephan-brumme.com/351/ — states the same derivation
  fraction-by-fraction, the identical formula (4) 6·(n(n+1)/2 − Σφ(i)),
  the same totient-sieve approach for n = 10⁸ (his is a segmented sieve at
  30 MB vs the run's 400 MB int32 table — same algorithm class, better
  memory discipline), and gives the correct result. Brumme is the standard
  public reference solution for this problem.
- The run's "second route" (Möbius inversion
  Φ(n) = ½Σ μ(d)⌊n/d⌋(1+⌊n/d⌋), floor grouping, Gueuss-recursion) is the
  standard sublinear method (Dirichlet hyperbola / Dujiao sieve): trizen's
  scripts, https://oeis.org/A002088, and Lucas A. Brown's *Computation of
  the Totient Summatory Function*, https://arxiv.org/abs/2506.07386
  (already in the library), whose Table 1 contains Φ(10⁸) again.
- The governing theory — lattice point visible from the origin iff gcd of
  coordinates = 1, visible density 1/ζ(2) = 6/π² — is classical
  (Sylvester 1883; confirmed in this session's literature search by Goins et
  al., https://doi.org/10.1080/00029890.2018.1465760, and the surveys
  already in the library).

Nothing in any source contradicts the conclusion. Two red herrings found and
rejected:
- one auto-generated search summary said the value was "not consistent with
  the growth pattern" — wrong by a trivial magnitude check
  (Φ(10⁸)/10¹⁶ = 0.30396 ≈ 3/π², and H ≈ 1.176·10¹⁶ = 3(1−6/π²)·10¹⁶);
- a stale recalled chunk carries the typo "11762189901804552" — the correct
  value 11762187201804552 matches A064018 and every published answer list;
  the run's own CONTEXT.md already documents this as a transcription typo.

## 5. Plausibility of "1 attempt / 11 established claims"

Plausible, and indeed exactly what a competent execution of a *known*
problem looks like. One attempt is the expected number for a textbook chain
whose path is pre-charted: the identity is the starting point of two decades
of published solutions (Brumme 2017, Raman 2012, Kumar–Israel 2014), the φ
sieve is a two-line standard, and the two sieves agreeing on Φ(10⁸) is the
same routine re-implemented. Eleven established claims (closed form, 
coprime-iff-visible, μ-identities, Gauss divisor sum, Farey length, Φ(10^k)
values, Möbius recursion) is a reasonable stock for that chain. A genuinely
*new* result of this size would be expected to take many attempts precisely
because its correct path is not pre-charted; here the fast convergence is the
signature of verification, not discovery.

## Sources

- https://oeis.org/A216453 — closed form (Raman 2012; Kumar–Israel 2014; Maiga 2019)
- https://oeis.org/A064018 — Φ(10^n); a(8) = 3039635516365908 (Yamanouchi; Brown)
- https://arxiv.org/abs/2506.07386 — Brown, Computation of the Totient Summatory Function (2025)
- https://euler.stephan-brumme.com/351/ — standard solution write-up, same formula and method
- https://github.com/lucky-bai/projecteuler-solutions/blob/master/Solutions.md — answer list
- https://github.com/JuliaLang/julia/blob/82f810d79640d2aac/test/euler.jl — answer list (#351)
- https://github.com/trizen/perl-scripts/blob/master/Math/partial_sums_of_euler_totient_function_fast.pl — sublinear Φ with a(10^8) example
- https://doi.org/10.1080/00029890.2018.1465760 — Goins et al., lattice visibility theory
- https://projecteuler.net/problem=351 — canonical statement

## Bottom line

Answer correct, argument sound, everything already known. The derivation
gains citations: OEIS A216453 (formula), OEIS A064018 + Brown
arXiv:2506.07386 (Φ(10⁸) and its computation), Brumme's write-up (same
method, independent public record), and the Sylvester/Goins lattice-visibility
theory. Report the value as the known answer; do not claim novelty.