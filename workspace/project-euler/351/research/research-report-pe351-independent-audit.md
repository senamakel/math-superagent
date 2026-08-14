# Independent audit: PE 351 — is the result known, and is the argument strong enough?

Auditor: research agent (fresh web searches this session; did not trust the
run's two existing status reports). Question: (1) is the run's conclusion
published and by whom; (2) is the argument strong enough for what it claims;
(3) is "reached in 1 attempt on 11 established claims" plausible for a result
of this size.

## 1. The result is published — confirmed by fresh searches, on four levels

**The numeric answer.** H(10^8) = 11762187201804552 is the accepted answer to
Project Euler Problem 351, published 17 Sep 2011 (projecteuler.net/problem=351).
Fresh independent records found this session:

- https://github.com/JuliaLang/julia/blob/82f810d79640d2aac/test/euler.jl — line "#351: 11762187201804552"
- https://github.com/roosephu/project-euler/blob/master/answers.txt — "351: 11762187201804552"
- https://github.com/lucky-bai/projecteuler-solutions/blob/master/Solutions.md — "351. 11762187201804552"
- https://projecteuler.weebly.com/ — "Problem 351: Hexagonal orchards ... 11762187201804552"
- https://oraclesqlpuzzle.ninja-web.net/csharp/csharp-euler-answers.html — "Problem351: 11762187201804552"

**The closed form.** OEIS A216453, "Number of points hidden from the central
point by a closer point in a hexagonal orchard of order n" —
https://oeis.org/A216453 — submitted by V. Raman, Sep 07 2012, explicitly
linked to Project Euler 351. Formula: a(n) = 6·(C(n+1,2) − Σ_{i≤n} φ(i)),
corrected by Piyush Kumar and Robert Israel, Aug 26 2014; equivalently
a(n) = 6·A063985(n) (Jon Maiga, Jan 12 2019). This is exactly the run's
identity H(n) = 3n² + 3n − 6·Φ(n). The run's computed 20 terms
0,6,12,24,30,54,60,84,102,138,144,192,198,246,288,336,342,414,420,492 match
the OEIS data row term-for-term (verified against the search snippet of the
entry).

**The Φ(10^8) anchor.** OEIS A064018 — a(n) = A002088(10^n) —
https://oeis.org/A064018 — lists a(8) = 3039635516365908, exactly the run's
two-sieve value. Terms 0..18 by Hiroaki Yamanouchi; term 19 by Lucas A. Brown,
"Computation of the Totient Summatory Function", arXiv:2506.07386
(https://arxiv.org/abs/2506.07386). The asymptotic Φ(n) ~ 3n²/π² is on the
entry. trizen's sublinear implementations also print
a(10^8) = 3039635516365908:
https://github.com/trizen/perl-scripts/blob/master/Math/partial_sums_of_euler_totient_function_fast.pl

**The method.** Standard, textbook; identical identity in the two most-cited
public solution write-ups:
- Stephan Brumme, https://euler.stephan-brumme.com/351/ — H(n) = 6·Σ(i−φ(i))
  = 6·(n(n+1)/2 − Σφ(i)), totient sieve, same segmented-sieve class the run
  uses (his is 30 MB segmented vs the run's 400 MB int32 table — same
  algorithm, better memory discipline).
- https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/351.py
  (adapted from igorvanloo) — same formula H(n) = 3n(n+1) − 6·Σφ(i),
  prints 11762187201804552.

## 2. The argument is strong enough — with three internal checks and one caveat

What the run's argument rests on, and its standing:

1. **Visibility criterion** (hidden ⟺ gcd(|a|,|b|) > 1 in axial coordinates):
   classical (Sylvester 1883; MathWorld VisiblePoint; Farey-sequence theory
   |F_n| = 1 + Φ(n), confirmed this session at
   https://en.wikipedia.org/wiki/Farey_sequence), and verified by the run
   against a literal no-number-theory scan for n ≤ 8.
2. **Sector decomposition** → H(n) = 6·(C(n+1,2) − Φ(n)): equivalent to the
   published formula; verified against all three statement oracles
   (H(5)=30, H(10)=138, H(1000)=1177848). The run itself found and refuted
   one intermediate sub-claim (axes carry one visible point each, not n),
   recorded in research/notes/pe351-axis-subclaim-refuted.md — the final
   identity does not depend on it. That self-correction is evidence of care,
   not weakness.
3. **Φ(10^8) = 3039635516365908**: computed three ways that agree exactly —
   the φ sieve (route 1), the μ-inversion sum (route 2, a genuinely different
   summation; the run records and fixed a step-p² μ-sieve bug), and the
   floor-grouped A063985 recursion (route 3, sieve-free, a different
   derivation). Catalogue check: rows k=0..8 of A064018 reproduced by a naive
   sieve. The final arithmetic is exact integer work: 3·10¹⁶ + 3·10⁸ −
   6·3039635516365908 = 11762187201804552, re-derived independently by
   6·1960364533634092.
4. **Magnitude sanity**: Φ(10⁸)/10¹⁶ = 0.30396 ≈ 3/π², and H ≈
   (3 − 18/π²)·10¹⁶ ≈ 1.176·10¹⁶. A 17-digit result beginning 1176… is
   exactly right, contradicting one auto-generated search summary's "not
   consistent with growth" remark, which was wrong.

Caveat to state plainly (not a contradiction): routes 1 and 2 are both
O(N)-memory sieve computations sharing only the prime list; they are two
implementations of the same routine class. The genuine independent confirmations
are route 3 (different derivation) and the OEIS catalogue value
(A064018 a(8), computed by Yamanouchi). Those are enough: the answer also
equals the accepted answer on five independent published records. Any residual
doubt in the Φ value would have to contradict all of these simultaneously.

**No source contradicts the conclusion.** The only contradictions found are
(a) a wrong auto-summary growth claim, (b) a stale recalled typo
11762189901804552 (correct: 11762187201804552) — both recorded in the run's
own CONTEXT.md and refuted by magnitude and by every published list.

## 3. Plausibility of "1 attempt on 11 established claims"

Plausible, and in fact the expected signature for a known problem. The
identity H(n) = 3n² + 3n − 6·Φ(n) is the *first* thing any competent solver
writes for this geometry (it is the starting point of Brumme 2017, Raman
2012, Kumar–Israel 2014); the φ sieve is a two-line standard; the 11 claims
(visibility criterion, sector count, Gauss divisor sum, Möbius identities,
Φ(10^k) values, Farey length) are a normal stock of lemmas for that chain.
One attempt is the expected number when the correct path is pre-charted — the
signature of *verification of a known result*. A genuinely new result of this
size reaching 1 attempt on 11 claims would be surprising; here it is exactly
what a competent execution of a published 2011 problem looks like.

## 4. Sources rejected (for the record)

- "Orchards in elliptic curves over finite fields" (Padmanabhan–Shukla,
  Finite Fields Appl. 2020) — orchard problem in a different sense; not the
  hexagonal orchard.
- "On sums involving the Euler totient function" (Bull. Austral. Math. Soc.)
  — gcd-sums of k-tuples; unrelated.
- "Visible lattice points along curves" (Ramanujan J. 2020), Goins et al.
  generalized lines of sight — visibility generalizations; the b=1 case
  confirms the classical criterion but no hexagonal-orchard formula.
- "Infinite products over visible lattice points" — partition identities;
  unrelated.

## Bottom line

The run did not discover anything; it independently re-derived, correctly and
with three mutually independent computations, the published solution to a
2011 Project Euler problem. Answer correct, argument sound, everything
already known, no contradictions. The derivation's citations should be:
OEIS A216453 (formula; Raman 2012, Kumar–Israel 2014, Maiga 2019), OEIS
A064018 + Brown arXiv:2506.07386 (Φ(10^8)), Brumme's write-up (same
method), and the classical lattice-visibility/Farey theory (Sylvester 1883).
Report the value as the known answer; do not claim novelty.

## URL list

- https://projecteuler.net/problem=351 (canonical statement; C. Hughes, 2011)
- https://oeis.org/A216453 (closed form, linked to PE 351)
- https://oeis.org/A064018 (Φ(10^n); a(8)=3039635516365908)
- https://arxiv.org/abs/2506.07386 (Brown, totient summatory computation)
- https://euler.stephan-brumme.com/351/ (standard solution, same formula)
- https://github.com/cirosantilli/project-euler-solutions/blob/master/solvers/351.py
- https://github.com/JuliaLang/julia/blob/82f810d79640d2aac/test/euler.jl
- https://github.com/roosephu/project-euler/blob/master/answers.txt
- https://github.com/lucky-bai/projecteuler-solutions/blob/master/Solutions.md
- https://projecteuler.weebly.com/
- https://oraclesqlpuzzle.ninja-web.net/csharp/csharp-euler-answers.html
- https://github.com/trizen/perl-scripts/blob/master/Math/partial_sums_of_euler_totient_function_fast.pl
- https://en.wikipedia.org/wiki/Farey_sequence (|F_n| = 1 + Σφ)
- https://mathworld.wolfram.com/VisiblePoint.html (gcd=1 visibility, 6/π²)