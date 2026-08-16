# de Faria & Tresser, "On Sloane's persistence problem" — HELD IN FULL

Source: arXiv:1307.1188 (2013; Exp. Math. 23 (2014) 363–382). Full text:
`research/sources/de-faria-tresser-sloane-persistence-body.full.md`
(100 KB, ar5iv capture); abstract page in
`research/sources/de-faria-tresser-sloane-persistence.full.md`.

## The Erdős connection (the part that matters here)

The paper studies Sloane's multiplicative persistence `S_q` and its variants.
The key tie to this run's problem: in **base 3** the only nonzero values of the
Sloane map are **powers of 2** — i.e. investigating the orbit of 1 under
`x ↦ 2x` (the doubling map). So the persistence question in base 3 is governed
by exactly the same orbit that the Erdős conjecture concerns.

- **Conjecture 1a** (their own): there is `k_{3,2}` such that for `k ≥ k_{3,2}`
  the base-3 expansion of `2^k` has at least one digit **zero**. (This is the
  digit-0 analogue of Erdős's digit-2 conjecture; both are the same
  "conspiracy-free" expectation about the doubling orbit.)
- The paper explicitly notes (p. 141): *"Such a statement is reminiscent of a
  conjecture by Erdős to the effect that there is always a 2 among the digits
  in base 3 of 2^k for all k sufficiently large. This question has been
  recently addressed by Lagarias."*

## Proved results (POTENTIALLY USEFUL LEMMAS FOR THIS RUN)

- **Lemma 1 (2^n is never all-2s).** If `n > 3`, at least one digit of the
  base-3 expansion of `2^n` is not 2. Proof: if `2^n = 3^k − 1` (all 2s),
  that's a Catalan-type solution `3^k − 2^n = 1` with `n > 3`, impossible
  (elementary proof for the (2,3) prime case, [LeVeque p.85]). **This is a
  non-vacuous partial result in the digit-2 direction.**
- **Proposition 2 (stability-time bound).** For base 3, `ν_3(n) ≤ 2(1 + log_3 log_3 n)`
  for all `n ≥ 3` — a weak bound on how long the Sloane digit-product map takes
  to stabilize in base 3.
- **Lemma 3 (tail periodicity, re-derived elementarily).** `2` is a primitive
  root mod `3^k` for every `k ≥ 1`; the low-k ternary digits of `2^n` are
  periodic in `n` with minimum period `φ(3^k) = 2·3^(k-1)`. In one full period
  each *allowable* string of length `k` (not ending in 0) appears exactly once.
  This is exactly the modular-sieve structure problem.md describes, re-derived
  in a self-contained way.
- **Density result.** The set `A = { n : S_3(2^n) = 0 }` = `{ n : 2^n has a 0
  digit in base 3 }` has **asymptotic density 1**. (Among allowable strings of
  length k, those with at least one 0 have proportion → 1.)

```claim
id: DEFARIA-TRESSER-2N-NOT-ALL2S
statement: For every n > 3, the base-3 expansion of 2^n has at least one digit
  different from 2 (in particular it is never the all-2 string 3^k - 1 = 22...2_3).
hypotheses: n > 3 integer; 2^n written in base 3.
holds-here: yes -- a concrete partial result on the digit-2 side, proved by
  reduction to the Catalan-type equation 3^k - 2^n = 1 (elementary for the
  (2,3) prime case).
status: proved in the primary source.
bearing: rules out the extreme all-2 counterexample; does not by itself rule out
  digit configurations with some 0s and 1s but no 2 (the actual Erdős target).
anchor: research/sources/de-faria-tresser-sloane-persistence-body.full.md

claim
id: DEFARIA-TRESSER-TAIL-PERIODICITY
statement: 2 is a primitive root mod 3^k for all k >= 1, so the low-k ternary
  digits of 2^n are periodic in n with minimum period 2*3^(k-1); each allowable
  (not-0-ending) length-k string occurs exactly once per period.
hypotheses: k >= 1; the "allowable" strings are the 2*3^(k-1) length-k ternary
  strings not ending in 0.
holds-here: yes -- this is precisely the modular-sieve structure of problem.md
  (order of 2 mod 3^k = 2*3^(k-1), and the sweep through residue classes).
status: proved in the primary source.
bearing: elementary re-derivation of the sieve's period structure; the residue
  classes are swept uniformly (each allowable tail once per period).

claim
id: DEFARIA-TRESSER-DENSITY-1-DIGIT-ZERO
statement: The set { n : 2^n has at least one 0 digit in its base-3 expansion }
  has asymptotic density 1 among n.
hypotheses: asymptotic density in the natural-numbers sense.
holds-here: yes (recorded as a density statement, per the problem's rule that
  density of *all integers* with a digit property says nothing about the thin
  sequence 2^n -- but this is a density statement *within* the sequence 2^n
  indexed by n, so it does say most powers of 2 have a 0 digit).
status: proved in the primary source.
bearing: the "digit 0 in 2^n" version holds with density 1; this is the same
  orbit structure that underlies the Erdős digit-2 conjecture.
anchor: research/sources/de-faria-tresser-sloane-persistence-body.full.md
```

## Status

Primary source, held in full. Directly relevant: gives an elementary proof that
`2^n` is never all-`2`s base-3 (n>3), a clean re-derivation of the
`2·3^(k-1)` tail periodicity (the sieve's period), and the density-1 digit-zero
result for `2^n`. Its Conjecture 1a is the digit-0 analogue of Erdős's.
