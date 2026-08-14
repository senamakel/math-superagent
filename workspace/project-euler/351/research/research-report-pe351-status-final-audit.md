# PE 351 status — final audit (fifth; fresh web verification of the exact answer string)

Question: is the run's result (H(10⁸) = 11762187201804552 via
H(n) = 3n² + 3n − 6·Φ(n)) already known, published, and by whom; is the
method standard; does anything contradict; is "1 attempt on 11 established
claims" plausible?

This is the fifth audit of the same question. The earlier four
(`research-report-pe351-known.md`, `research-report-pe351-known-verification.md`,
`research-report-pe351-independent-audit.md`, `research-report-pe351-my-findings.md`,
`research-report-pe351-status-confirmed-research-specialist.md`) all reached
the same verdict. This audit adds what the previous ones relied on but this
session re-verified against the live web, plus one direct download of a raw
answer list.

## Verdict, stated bluntly

**The run did not discover anything new. It re-derived, correctly and with
multiple mutually independent computations, the published answer to a 2011
Project Euler problem, using the textbook method.** The answer, the closed
form, the Φ(10⁸) anchor, and the method are all in the open record. "1
attempt on 11 established claims" is not merely plausible — it is exactly the
signature of *verification of a known problem*, not of discovery. A genuinely
new result of this size would be expected to take many attempts because its
path would not be pre-charted; here the path is the first paragraph of
every published solution.

## 1. The answer string is published — verified by direct download this session

The exact string **11762187201804552** as problem 351's answer:

- Downloaded raw: https://raw.githubusercontent.com/roosephu/project-euler/master/answers.txt
  → "351: 11762187201804552" (filed at research/summaries/roosephu-answers.md;
  also shown as https://github.com/roosephu/project-euler/blob/master/answers.txt).
- https://github.com/nayuki/luckytoilet-project-euler-solutions/blob/master/Solutions.md
  (search hit: "351." immediately followed by 11762187201804552).
- https://github.com/JuliaLang/julia/blob/82f810d79640d2aac/test/euler.jl
  ("#351: 11762187201804552").
- https://github.com/yenniejun/project-euler-gpt-langs/blob/main/solutions.txt
  ("351. 11762187201804552").
- https://projecteuler.weebly.com/ ("Problem 351: Hexagonal orchards — 11762187201804552").

The canonical statement is Project Euler 351 (Colin Hughes, published
2011-09-17): https://projecteuler.net/problem=351 (also /minimal=351 on disk).

## 2. The closed form is published — OEIS A216453, and it is exactly the run's identity

- https://oeis.org/A216453 — "Number of points hidden from the central point
  by a closer point in a hexagonal orchard of order n"; author **V. Raman,
  Sep 07 2012**; explicitly linked to PE 351.
- **FORMULA: a(n) = 6·(C(n+1,2) − Σ_{i=1..n} φ(i))**, corrected by **Piyush
  Kumar and Robert Israel, Aug 26 2014**; equivalently a(n) = 6·A063985(n)
  (**Jon Maiga, Jan 12 2019**). This is the run's
  H(n) = 3n² + 3n − 6·Φ(n), since 6·C(n+1,2) = 3n(n+1).
- The entry's terms 0, 6, 12, 24, 30, 54, 60, 84, 102, 138, … match the run's
  computed terms and the statement's oracles H(5)=30, H(10)=138, H(1000)=1177848
  (a(5)=30, a(10)=138; 6·(1000·1001/2 − 304192) = 6·196308 = 1177848).

## 3. The Φ(10⁸) anchor is published — OEIS A064018 and Brown arXiv:2506.07386

- https://oeis.org/A064018 — a(n) = Φ(10ⁿ) = Σ_{k≤10ⁿ} φ(k); the b-file row
  **"8 3039635516365908"** is exactly the run's two-sieve value Φ(10⁸) =
  3,039,635,516,365,908. Terms 0..18 by Hiroaki Yamanouchi, term 19 by Lucas
  A. Brown; internal page re-read this session with the terms
  1, 32, 3044, 304192, 30397486, 3039650754, 303963552392, 30396356427242,
  3039635516365908.
- https://arxiv.org/abs/2506.07386 — Brown, "Computation of the Totient
  Summatory Function" (2025): the Θ(n^{2/3})-time / Θ(n^{1/3})-space
  Dirichlet-hyperbola algorithm and its catalogue values; the same value is a
  worked example in trizen's implementation:
  https://github.com/trizen/perl-scripts/blob/master/Math/partial_sums_of_euler_totient_function_fast.pl
  ("a(10^8) = 3039635516365908").

## 4. The method is the standard one

The six-sector derivation — in one sector of ring i the points are the
fractions x/i (1 ≤ x ≤ i); φ(i) of them are coprime/reduced/visible, so each
sector contributes i − φ(i) hidden on ring i, and
H(n) = 6·Σ_{i≤n}(i − φ(i)) = 6·(n(n+1)/2 − Φ(n)) — is the textbook solution,
found identically in:

- https://euler.stephan-brumme.com/351/ (Stephan Brumme, 2017; canonical
  public write-up; segmented totient sieve for n = 10⁸ — same algorithm class
  as the run's full int32 sieve, better memory discipline ~30 MB vs ~400 MB).
- https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/351.py
  (adapted from igorvanloo; identical formula and totient summatory).
- https://www.ivl-projecteuler.com/overview-of-problems/25-difficulty/problem-351
  (per-layer gcd count → Φ; Möbius sieve and sublinear totient summatory).

The run's verification routes (Möbius inversion
Φ(n) = ½Σ μ(d)⌊n/d⌋(1+⌊n/d⌋); Gauss divisor-sum floor recursion; Chai Wah
Wu's A063985 recursion) are the standard sublinear summatory-totient methods
(Dirichlet hyperbola / Dujiao sieve; Brown 2025; trizen). The governing
theory — a lattice point is visible from the origin iff gcd(coords) = 1 and
visible density 1/ζ(2) = 6/π² (Sylvester 1883) — is classical and confirmed
by the library's sources (Goins–Harris–Kubik–Mbirika,
https://doi.org/10.1080/00029890.2018.1465760; Adhikari–Granville; the
hidden-forests literature of Goodrich–Mbirika–Nielsen, arXiv:1805.03186 /
Involve 14:2 (2021) 283–310).

## 5. Arithmetic re-check (exact integers, done here)

- Φ(10⁸) = 3,039,635,516,365,908 (A064018 a(8)); 6·Φ = 18,237,813,098,195,448.
- 3·(10⁸)² + 3·10⁸ = 30,000,000,300,000,000.
- Difference = **11,762,187,201,804,552** ✓ — matches the raw answers.txt
  download byte-for-byte.
- Small n: Φ(8) = 22; 6·(C(9,2) − 22) = 6·14 = 84 = H(8), consistent with the
  run's check and OEIS a(8) = 84. Statement oracles H(5)=30, H(10)=138,
  H(1000)=1177848 all reproduced.

## 6. Contradictions found

None. Two search-summarizer noises rejected: (a) an auto-summary saying the
number "is not aligned with the known sample values" — category confusion (it
compared the 10⁸ answer against the n = 5, 10, 1000 sample values, which are
different inputs, not a consistency check); (b) earlier sessions' stale
transcription typo 11762189901804552, which the correct string in the raw
download supersedes. The JuliaLang and answer-list files corroborate the exact
string. The run's own claims ledger marks the identities as sourced/checked,
correctly — consistent with re-derivation.

## Bottom line

Answer correct, argument sound (three independent exact computations of
Φ(10⁸), one of them a different derivation; brute-force oracle agreement at
n ≤ 1000 including the statement's own examples), everything already known,
no contradictions. The derivation should cite: OEIS A216453 (closed form;
Raman 2012; Kumar–Israel 2014; Maiga 2019), OEIS A064018 + Brown
arXiv:2506.07386 (Φ(10⁸)), and Brumme's write-up + the answer lists (the
value). Report the value as the known answer; do not claim novelty.

## Sources consulted (all re-verified or freshly fetched this session)

- https://raw.githubusercontent.com/roosephu/project-euler/master/answers.txt (downloaded; exact string)
- https://oeis.org/A216453 and https://oeis.org/A216453/internal (formula, author, correction history)
- https://oeis.org/A064018 and https://oeis.org/A064018/internal (Φ(10⁸) = a(8))
- https://arxiv.org/abs/2506.07386 (Brown 2025)
- https://euler.stephan-brumme.com/351/ (standard method write-up)
- https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/351.py
- https://www.ivl-projecteuler.com/overview-of-problems/25-difficulty/problem-351
- https://github.com/nayuki/luckytoilet-project-euler-solutions/blob/master/Solutions.md
- https://github.com/JuliaLang/julia/blob/82f810d79640d2aac/test/euler.jl
- https://github.com/yenniejun/project-euler-gpt-langs/blob/main/solutions.txt
- https://projecteuler.net/problem=351 (canonical statement)
- https://github.com/trizen/perl-scripts/blob/master/Math/partial_sums_of_euler_totient_function_fast.pl