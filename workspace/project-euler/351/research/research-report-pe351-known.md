# Research report: is the PE 351 result new, and is the argument sound?

Question: the run believes it has solved Project Euler 351 (hexagonal orchard),
concluding H(10^8) = 11 762 187 201 804 552 via the identity
H(n) = 3n² + 3n − 6·Φ(n). Was asked: is the result already known, is the
method standard, does anything contradict the conclusion, and is
reaching it in 1 attempt on 11 established claims plausible?

## Verdict

**The result is already known, the method is the standard one, and nothing in
the sources contradicts the conclusion.** The run computed (and verified with
unusual thoroughness) a published answer to a 2011 Project Euler problem using
the textbook method. There is no new mathematics here — which is the finding,
and it is a useful one: the derivation can cite the sources below.

## 1. The closed form is published — OEIS A216453

- Sequence: *Number of points hidden from the central point by a closer point
  in a hexagonal orchard of order n* — https://oeis.org/A216453
- Author V. Raman, Sep 07 2012; the entry explicitly links Project Euler 351.
- **Formula (exactly what the run uses):**
  a(n) = 6·(C(n+1,2) − Σ_{i=1..n} φ(i)), corrected by **Piyush Kumar and
  Robert Israel, Aug 26 2014**; equivalently a(n) = 6·A063985(n)
  (Jon Maiga, Jan 12 2019).
- The run's `solution.md` credits exactly this "Kumar–Israel formula" and the
  OEIS lookup matched the run's own computed terms 0,6,12,24,30,54,60,84,….

## 2. The answer is the published PE 351 answer

H(10^8) = 11762187201804552 appears as the accepted answer in independent
published lists:

- https://github.com/roosephu/project-euler/blob/master/answers.txt  ("351: 11762187201804552")
- https://github.com/lucky-bai/projecteuler-solutions/blob/master/Solutions.md
- https://projecteuler.weebly.com/ (entry "Problem 351: Hexagonal orchards — 11762187201804552")
- https://github.com/JuliaLang/julia/blob/82f810d79640d2aac/test/euler.jl ("#351: 11762187201804552")
- https://oraclesqlpuzzle.ninja-web.net/csharp/csharp-euler-answers.html ("Problem351: 11762187201804552")

## 3. The Φ(10^8) anchor is published — OEIS A064018

- a(n) = Φ(10^n) = Σ_{k≤10^n} φ(k) — https://oeis.org/A064018
- a(8) = **3039635516365908** — exactly the value the run computed by two
  independent sieves. Terms 0..18 by Hiroaki Yamanouchi, extended to 10^19 by
  Lucas A. Brown, "Computation of the Totient Summatory Function",
  arXiv:2506.07386 (https://arxiv.org/abs/2506.07386), which the run already
  had in `research/sources/`.
- The asymptotic Φ(n) ~ 3n²/π² is on the A064018 entry.

## 4. The method is the standard one

The ring-wise derivation (each of the six wedges of ring i carries i points,
φ(i) of them coprime/visible, so 6(i−φ(i)) hidden), reducing the problem to
the summatory totient, is the standard solution:

- Stephan Brumme, https://euler.stephan-brumme.com/351/ — same formula
  H(n) = 6Σ(i−φ(i)) = 6(n(n+1)/2 − Σφ(i)), same segmented-sieve approach at
  n = 10^8 (30 MB memory — ahead of the run's 400 MB int32 sieve, but same
  class).
- igorvanloo / cirosantilli:
  https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/351.py
  — same formula, prints H(10^8) = 11762187201804552.
- IVL Project Euler solutions: https://www.ivl-projecteuler.com/overview-of-problems/25-difficulty/problem-351
  — the gcd(x,n)>1-per-layer count, summatory totient, and Möbius-sieve
  acceleration (per-layer count → Φ, then sublinear evaluation).

The run's "second route" (Möbius identity Φ(n) = ½Σ μ(d)⌊n/d⌋(1+⌊n/d⌋) with
floor grouping, Brown's Θ(n^{2/3}) algorithm, and Chai Wah Wu's A063985
recursion) is likewise the standard fast prefix-sums / Dirichlet-hyperbola
method (Dujiao sieve) — see trizen's partial-sums implementations, which list
S(10^8)=3039635516365908:
https://github.com/trizen/sidef-scripts/blob/master/Math/partial_sums_of_euler_totient_function_recursive.sf

## 5. The claim ledger this run used is itself honest about provenance

The run's own `research/CLAIMS.md` (re-derived from notes) lists the closed
form, the summatory-totient Möbius identity, Φ(10^k) values, and the
visibility criterion as *sourced* or *checked*, and — correctly — does not
claim any of them as new. The "load-bearing but unverified" rows are exactly
the classical identities (gcd=1 ⇔ visible, Farey length 1+Φ(n), Gauss divisor
sum, Möbius inversion); each is standard and each is cross-checked in the
run's verification programs. No contradiction with the run's final conclusion
was found anywhere.

## 6. Plausibility of 1 attempt / 11 established claims

Fully plausible, and in fact what a competent execution of a known problem
looks like. The run's methods were the correct prefabricated ones (the
identity is 22 years' worth of published solutions' starting point; the φ
sieve is a two-line standard; the two independent confirmations of Φ(10^8)
are the same routine re-implemented). One attempt is the expected number for a
textbook chain that converges; 11 established claims is a reasonable stock of
ready lemmas for that chain. This is the signature of *verification of a
known result*, not of discovery — a genuinely new result of this size would
typically require many attempts precisely because the correct path is not
pre-charted.

## 7. What contradicts the conclusion? Nothing — one red herring

One search summary (an auto-generated summary of the official problem page)
asserted the value was "not consistent with the known growth pattern." That is
wrong, trivially: Φ(10^8) ≈ 0.30396·10^16 and H ≈ (3 − 18/π²)·10^16 ≈
1.176·10^16, so a 17-digit result beginning 1176… is exactly the right
magnitude; and the value matches every published answer list. No source
contradicts the run's conclusion.

Independent sanity arithmetic (done in this report, no program needed):
- 6·(3 039 635 516 365 908) = 18 237 813 098 195 448
- 3·(10^8)² + 3·10^8 = 30 000 000 300 000 000
- difference = 11 762 187 201 804 552 ✓
- Small-n checks of the identity (each verified by brute force in the run):
  H(5)=30, H(10)=138, H(1000)=1177848 — the statement's own oracles; H(8)=84.

## Bottom line

The run did not discover anything; it reproduced, exactly and with three
mutually independent computations, the published solution to a 2011 problem.
That is a success of a different kind — verification — and the derivation
gains citations: OEIS A216453 (Kumar–Israel formula), OEIS A064018 / Brown
arXiv:2506.07386 (the Φ value and its sublinear methods), and the classical
λ: coprime-pairs/visible-point theory (Sylvester 1883; MathWorld
VisiblePoint). Report the answer as the known one, cite these, and do not
claim novelty.

## Sources consulted

- https://oeis.org/A216453 (closed form, Kumar–Israel 2014; linked to PE 351)
- https://oeis.org/A064018 (Φ(10^n); a(8)=3039635516365908; Brown 2025)
- https://arxiv.org/abs/2506.07386 (Brown, Computation of the Totient Summatory Function)
- https://euler.stephan-brumme.com/351/ (standard solution write-up)
- https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/351.py
- https://www.ivl-projecteuler.com/overview-of-problems/25-difficulty/problem-351
- https://github.com/roosephu/project-euler/blob/master/answers.txt etc. (answer lists)
- https://github.com/trizen/sidef-scripts/blob/master/Math/partial_sums_of_euler_totient_function_recursive.sf (Φ sublinear algorithms with S(10^8))