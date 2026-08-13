# Killgrove & Ralston 1959 — On a conjecture concerning the primes

**Full text:** `research/sources/killgrove-ralston-1959-on-a-conjecture-concerning-the-primes.full.md`
**Source URL:** https://www.ams.org/journals/mcom/1959-13-066/S0025-5718-59-99262-2/S0025-5718-59-99262-2.pdf
**Published:** *Math. Comp.* (Math. Tables Aids Comp.) 13 (1959), 121–122. Received Oct. 7, 1958; ONR-sponsored. Authors at UCLA.

## Content

- **(A) The conjecture, attributed.** "The conjecture (Norman L. Gilbreath, private communication, July 1958) is then that `P_{i,0} = 1` for all `i > 0`" (the run's `A_k(0)`). Sequence `P_{0,j}` = j-th prime, `P_{0,0}=2`; iteration `P_{i,j} = |P_{i−1,j+1} − P_{i−1,j}|`. Their table reproduces the run's `A_1..A_6` exactly.
- **(B) Block lemma, exact words.** "if for some *i* and all *j*, `0 ≤ j ≤ M`, we have `P_{i,j} = 0` or 2 and `P_{i,0} = 1`, then all of the differences that derive from them will be bounded by 2, from which it follows that `P_{i,0}, P_{i+1,0}, ..., P_{i+M−1,0} = 1`." (Their indexing includes the leading 1 in the block so the count is off-by-one relative to Odlyzko; either way the protection is **one row per {0,2} entry**, coefficient 1.)
- **(C) P(i) and the verification.** `P(i)` = largest M with `P_{i,j} ≤ 2` for all `j ≤ M`; then `P_{k,0} = 1` for `i ≤ k < P(i) + i`. SWAC run on Lehmer's sieve of primes `< 792,722`; "the conjecture holds for all primes less than 792,722, which amounts to the first 63,419 primes" (Odlyzko's text states `< 792,731`, 63,419 — trivial discrepancy in the upper bound value). Full table of P(i) for i = 0..95, reaching `P(95) > 63,324`, `P(95)+95 > 63,419`. The P(i) values (3, 8, 14, 14, 25, 24, 23, 22, 25, 59, ...) are exactly OEIS A000232, which the run's block profile reproduces as P(i)−1.
- **(D) Context.** Also notes uncountably many sequences have the property (e.g. `{1, 0-or-2, ...}`); any such sequence has first differences bounded by `2^j`.

## Claims

```claim
id: killgrove-ralston-block-protection
statement: If row i starts 1 and has M entries after the leading 1 (their "0 ≤ j ≤ M" includes P_{i,0}) all 0 or 2, then the next M−1 rows start with 1 (their span P_{i,0}..P_{i+M−1,0}); protection is one row per {0,2} entry, coefficient 1.
hypotheses: triangle from primes via absolute differences; row is (1, 0/2, ...).
holds-here: yes — earliest published statement of the block lemma; agrees with Odlyzko 1993 up to indexing.
status: sourced (Killgrove–Ralston 1959, p. 121)
bearing: primary confirmation that the "≈ n/2" phrasing in problem.md is wrong; the true protection is linear with constant 1.
anchor: research/sources/killgrove-ralston-1959-on-a-conjecture-concerning-the-primes.full.md
```

```claim
id: killgrove-ralston-verification-1959
statement: Conjecture verified for all primes < 792,722 (first 63,419 primes) on SWAC using D. H. Lehmer's sieve; P(i) tabulated for i = 0..95, max P(i)+i > 63,419.
hypotheses: exact computation; finite initial segment.
holds-here: yes — the first machine verification; the run's block profile matches their P(i)−1.
status: sourced (Killgrove–Ralston 1959, p. 121–122; bound cross-checked against Odlyzko 1993's restatement)
bearing: the standard "verified to k < 63,419" citation; note Odlyzko's restatement says primes < 792,731 — the two sources differ in the last digits (792,722 vs 792,731); the first-63,419-primes count is unambiguous and consistent.
anchor: research/sources/killgrove-ralston-1959-on-a-conjecture-concerning-the-primes.full.md
```