# Webb, "On 4/n = 1/x + 1/y + 1/z" (Proc. AMS 25 (1970) 578–584)

Source: https://www.ams.org/journals/proc/1970-025-03/S0002-9939-1970-0256984-9/S0002-9939-1970-0256984-9.pdf
(author's own copy from the AMS free archive; the DOI record is
10.1090/S0002-9939-1970-0256984-9).
Full text: `research/sources/stewart-webb-1970-exception-density.full.md`
(converted from PDF; OCR is imperfect — "4/w" for "4/n", etc. — but the theorem
statements and proof are readable).

## What it establishes (sourced, primary)

**Attribution correction**: the paper is by **William A. Webb alone** (the run's
older memory had "Stewart & Webb 1970"). Stewart is the co-author of the 1966
*Canadian J. Math.* lemma paper cited inside it; the 1970 *Proc. AMS* paper is
Webb's.

**Theorem 1 (main)**: if S(N) is the number of positive integers n ≤ N for
which `4/n = 1/x + 1/y + 1/z` is **not** solvable in positive integers, then

```
S(N) ≪ N/(log N)^{7/4}.
```

**Method (elementary + Selberg sieve)**: the two-unit-fraction lemma
(Lemma 1: `a/b = 1/x + 1/y` iff there are divisors d₁, d₂ of b with
`a | d₁+d₂`; generalized proof in Stewart–Webb 1966) is used to build
solvability conditions on n from prime residue classes mod 8 (Lemma 2: solvable
if some prime p ≡ 7 (mod 8) has n ≡ 0, −1, −2, −2⁻¹ (mod p); or p ≡ 3 (mod 8)
with n ≡ 0, −1 (mod p); or p ≡ 5 (mod 8) with n ≡ 0 (mod p)). Selberg's sieve
(Halberstam–Roth) over the sifting classes then gives the bound.

**Concluding remarks**: residue classes mod 16 improve the exponent to 2;
mod 2^k (arbitrary k) gives 9/4 − ε. The paper closes by noting these are far
from the conjecture S(N) = 0, or even S(N) ≪ N^{1−ε}.

## Relation to the library

- This is the **original** density result whose improved versions (Vaughan's
  exp(−c(log N)^{2/3}) 1970 bound; Elsholtz's k-unit-fraction generalisations)
  the run's other sources restate. It supersedes the run's memory that
  "Webb 1970: the proportion of counterexamples up to N tends to 0" — the
  precise statement is the 7/4 exponent above.
- Lemma 2's solvability conditions are residue-class identities of exactly the
  shape this run builds: `4/n = 1/rn + p/(2(t+1)n)` with `p = 8t+7`, etc. — the
  per-prime modular equations that Salez later systematised into the seven
  equations. The mod-8 conditions appearing here are a genuine subset of the
  classical Mordell-family mod-8 identity.

```claim
id: webb-1970-exception-density
statement: The number S(N) of n ≤ N for which 4/n = 1/x+1/y+1/z has no positive-integer solution satisfies S(N) ≪ N/(log N)^{7/4}, proved by elementary two-unit-fraction conditions plus Selberg's sieve over residue classes mod 8; refinements mod 16 and mod 2^k give exponents 2 and 9/4−ε.
hypotheses: n ≥ 2 integer; S(N) counts unsolvable n.
holds-here: true — the bound is context for how many open n can remain, not a construction; the residue-class solvability conditions inside it (mod 8 primes) are the classical identity shapes the six open classes avoid.
status: sourced (Webb 1970, Proc. AMS 25, 578–584, full text on disk; the attribution "Stewart & Webb 1970" in earlier memory is corrected to Webb alone).
bearing: fixes the "how many" scale for the exceptional set; the six-class mod-840 picture is the residue-level refinement of exactly this sieve.
anchor: research/sources/stewart-webb-1970-exception-density.full.md
```

## Consequence for this run

The paper's Lemma 2 conditions are the mod-8 precursor of the mod-840
classification: they show solvability is decided by which prime residue classes
divide factors of n, and the six open classes are precisely the primitive square
classes mod 840 that escape every such condition at the small moduli. Any new
family must add a solvability condition that none of 1,121,169,289,361,529
(mod 840) escapes — i.e. must introduce a modulus or divisor structure the
classical conditions never see.