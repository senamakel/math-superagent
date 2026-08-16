# Summary — The variance of the number of prime polynomials in short intervals and in residue classes

Source: Jonathan P. Keating & Zeév Rudnick, arXiv:1204.0708 (2012). Full text:
`keating_rudnick_prime_polynomials_short_intervals_residue_classes.full.md`.

## What this establishes

Function-field versions of two central variance conjectures: Goldston–Montgomery
(variance of primes in short intervals) and Hooley (variance of primes in
arithmetic progressions).

- **Variance of primes in short intervals (Thm 4.1).** Fix n, `0 < h < n`; as
  `q → ∞` the variance of the count of primes in a short interval matches the
  Goldston–Montgomery prediction, governed by a singular-series/equidistribution
  constant.
- **Variance in arithmetic progressions (Thm 5.1).** For `Q ∈ F_q[T]`, `deg Q ≥ 2`,
  the variance of primes in a residue class mod Q has the Hooley prediction.
- **Equidistribution engine.** The results hinge on Katz's equidistribution of
  Frobenii (Thms 4.2, 5.2): the unitarized Frobenii `Θ_χ` for families of
  characters mod `T^{m+1}` / primitive odd characters mod Q become equidistributed
  in the projective unitary / unitary group as `q → ∞`.

## Why it matters here

This is the foundational source of the adopted `function-field-fqt-model`: it
establishes that in the function-field world the *second-moment / singular-series*
equidistribution structure of primes — the object that over the integers is
behind the pair-correlation / LOS machinery — is a fully effective, computable
theorem (via Katz equidistribution). It is the clearest demonstration that the
*value-domain* arithmetic the integer switch problem cannot reach is available
over F_q.

**Transfer gap (load-bearing):** the object is the *variance* (second moment) of
one-point counts in short intervals or residue classes — a value-domain second
moment, not the two-point *lex-consecutive* switch statistic the fold reads. It
grounds the singular-series/equidistribution side, not the consecutive-pair
object.

```claim
id: keating-rudnick-function-field-variance
statement: Over F_q[T], as q → ∞, the variance of the count of prime polynomials in
  short intervals (Goldston–Montgomery) and in arithmetic progressions mod Q (Hooley)
  obeys the classical predictions, with the constants governed by Katz equidistribution
  of Frobenii in projective/unitary groups.
hypotheses: fixed n, 0<h<n, deg Q ≥ 2; large finite field q → ∞; Katz equidistribution.
holds-here: yes for the value-domain second-moment/singular-series input the
  function-field model's arithmetic rests on; NO for the degree-ordered
  lex-consecutive switch object (two-point, uncontrolled here).
status: proved (Keating–Rudnick 2012, arXiv:1204.0708).
bearing: grounds the singular-series/equidistribution side of the adopted
  function-field model; the consecutive-switch transfer is the model's own open step.
anchor: research/sources/keating_rudnick_prime_polynomials_short_intervals_residue_classes.full.md
```

## Keyword map
variance; short intervals; arithmetic progressions; function field; prime
polynomials; Goldston–Montgomery; Hooley; Katz equidistribution.
