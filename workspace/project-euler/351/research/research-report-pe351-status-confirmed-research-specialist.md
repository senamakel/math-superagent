# PE 351 status audit — research-specialist confirmation (fresh web checks)

Question: is the run's result (H(10⁸) = 11762187201804552 via
H(n) = 3n² + 3n − 6·Φ(n)) already known; is the method standard; does
anything contradict; is 1 attempt / 11 established claims plausible?

This is the fourth audit of the same question (the others:
`research-report-pe351-known.md`, `research-report-pe351-known-verification.md`,
`research-report-pe351-independent-audit.md`, `research-report-pe351-my-findings.md`).
All four, including this one with fresh web searches, reach the same verdict.
This note records what the fresh searches independently confirmed, so the
question is closed and nobody needs to search it again.

## Fresh confirmations this session (each via live search, not memory)

1. **The answer is the published PE 351 answer.** The exact string
   11762187201804552 appears as problem 351's accepted answer in at least
   five independent published records:
   - https://github.com/roosephu/project-euler/blob/master/answers.txt ("351: 11762187201804552")
   - https://github.com/lucky-bai/projecteuler-solutions/blob/master/Solutions.md ("351. 11762187201804552")
   - https://github.com/JuliaLang/julia/blob/82f810d79640d2aac/test/euler.jl ("#351: 11762187201804552")
   - https://projecteuler.weebly.com/ and https://oraclesqlpuzzle.ninja-web.net/csharp/csharp-euler-answers.html
   - https://gist.github.com/33e4a8beb47a08b6bbce ("351. 11762187201804552")
   The canonical statement is Project Euler 351 (Colin Hughes, published
   2011-09-17), https://projecteuler.net/problem=351.

2. **The closed form is published.** OEIS A216453, "Number of points hidden
   from the central point by a closer point in a hexagonal orchard of order
   n", https://oeis.org/A216453 — submitted by V. Raman, Sep 07 2012,
   explicitly linked to PE 351. Formula:
   a(n) = 6·(C(n+1,2) − Σ_{i=1..n} φ(i)) — corrected by Piyush Kumar and
   Robert Israel, Aug 26 2014; equivalently a(n) = 6·A063985(n) (Jon Maiga,
   Jan 12 2019). This is exactly the run's identity
   H(n) = 3n² + 3n − 6·Φ(n). OEIS data row (offset 1): 0, 6, 12, 24, 30,
   54, 60, 84, ... matches the run's computed terms and the statement's
   oracles H(5)=30, H(10)=138 (a(5)=30, a(10)=138), and H(1000)=1177848.

3. **The Φ(10⁸) anchor is published.** OEIS A064018 =
   A002088(10ⁿ) = Σ_{k≤10ⁿ} φ(k), https://oeis.org/A064018 — a(8) =
   **3039635516365908**, exactly the run's two-sieve value. Terms 0..18 by
   Hiroaki Yamanouchi, term 19 by Lucas A. Brown, *Computation of the
   Totient Summatory Function*, arXiv:2506.07386 (2025). Also reproduced in
   trizen's sublinear implementations
   (https://github.com/trizen/perl-scripts/blob/master/Math/partial_sums_of_euler_totient_function_fast.pl
   and the `.sf` recursive versions), each listing a(10⁸) = 3039635516365908.
   Asymptotic Φ(n) ~ (3/π²)n² is on the entry and on Wikipedia's Totient
   summatory function page.

4. **The method is the standard one.** The six-sector derivation — ring i of
   one sector carries i points, φ(i) of them coprime/visible, so
   H(n) = 6·Σ_{i≤n}(i − φ(i)) = 6·(n(n+1)/2 − Φ(n)) — is the textbook
   solution, found in:
   - https://euler.stephan-brumme.com/351/ (Stephan Brumme, 2017; canonical
     public write-up; segmented totient sieve — same algorithm class as the
     run's full int32 sieve, better memory: ~30 MB vs ~400 MB),
   - https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/351.py
     (adapted from igorvanloo; identical formula H(n) = 3n(n+1) − 6·Φ(n)),
   - https://www.ivl-projecteuler.com/overview-of-problems/25-difficulty/problem-351
     (per-layer gcd count → totient summatory, Möbius-sieve acceleration).
   The run's "second/third routes" (Möbius inversion
   Φ(n) = ½Σ μ(d)⌊n/d⌋(1+⌊n/d⌋); Gauss divisor-sum floor-grouped recursion
   of A063985) are the standard sublinear summatory-totient algorithms
   (Dirichlet hyperbola / Dujiao sieve; Brown 2025; trizen).

## Independent arithmetic re-check (exact integers, done here)

- Φ(10⁸) = 3039635516365908 (A064018 a(8)); 6·Φ = 18,237,813,098,195,448.
- 3·(10⁸)² + 3·10⁸ = 30,000,000,300,000,000.
- Difference = **11,762,187,201,804,552** ✓ (matches every published list
  and the run's three computed routes).
- Small-n sanity: Φ(8) = 22 (φ(1..8) = 1,1,2,2,4,2,6,4);
  6·(C(9,2) − 22) = 6·14 = 84 = H(8) = A216453 a(8) ✓. The statement's own
  oracles H(5)=30, H(10)=138, H(1000)=1177848 are reproduced by the
  identity (and by the run's brute force).

## Contradictions found

None. Two things that looked like contradictions and are not:
(a) an auto-generated search summary claiming H(10⁸) is "not consistent with
the growth pattern" — false by a magnitude check (Φ/10¹⁶ ≈ 0.30396 ≈ 3/π²;
H ≈ 1.176·10¹⁶ ≈ (3 − 18/π²)·10¹⁶); (b) a stale recalled chunk with the
transcription typo 11762189901804552 — the correct value 11762187201804552
matches A064018 and every published record. Both are already documented in
CONTEXT.md.
A caution generated by search summarizers ("PE 351 is Antenna on a Sphere",
"answer 704630/55") is hallucinated noise from an auto-summarizer that does
not know the problem — contradicts nothing in the run and nothing in any
primary source.

## Plausibility of 1 attempt on 11 established claims

Plausible and expected — as the signature of *verification of a known
problem*, not of discovery. The identity is the first move a competent
solver writes for this geometry (it is the starting point of Brumme 2017,
Raman 2012, Kumar–Israel 2014, igorvanloo); the φ sieve is a two-line
standard; the eleven claims are a normal stock of published lemmas for that
chain. A genuinely new result of this size would be expected to take many
attempts precisely because its path would not be pre-charted. The fast
convergence is exactly what solving a 2011 problem whose solution is
published in four independent places looks like. The run's own CLAIMS.md
correctly marks the identities as sourced/checked — provenance hygiene
consistent with re-derivation.

## Bottom line (unchanged by this fourth audit)

**The run did not discover anything new.** It independently re-derived,
correctly and with several mutually consistent computations, the published
answer to a 2011 Project Euler problem, using the textbook method and a
catalogued Φ(10⁸). Answer correct (11762187201804552), argument sound,
everything already known, no contradictions. The derivation should cite:
OEIS A216453 (closed form; Raman 2012, Kumar–Israel 2014, Maiga 2019),
OEIS A064018 + Brown arXiv:2506.07386 (Φ(10⁸)), and Brumme's write-up
(same method). Report the value as the known answer; do not claim novelty.