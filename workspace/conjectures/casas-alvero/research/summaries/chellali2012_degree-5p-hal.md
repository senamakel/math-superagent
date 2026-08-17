# Chellali & Salinier, *La conjecture de Casas Alvero pour les degrés 5p^e* (2012, HAL)

<!-- source: https://hal.science/hal-00748843/document | 2012, French, HAL open archive -->

## What this source is

A 2012 French-language paper (HAL hal-00748843) by Mustapha Chellali and Alain
Salinier, proving CA for degrees `5p^e` (e ≥ 1 integer, p prime) with an
**explicit finite list of excluded primes**.

## What it establishes

- **Proposition 2.2** (the main result): CA is true for polynomials of degree
  `5p^e`, e an integer, **p prime ≠ 2, 3, 7, 11, 131, 193, 599, 3541, 8009**.
- This is the degree-5p family (`problem.md`'s "5p^k" row) settled with an
  **explicit bad-prime list** — matching the 5p row of the run's settled
  classes (Castryck et al. 2012 classified 5p^k primes by computation;
  Chellali–Salinier give the list directly).
- French summary: CA says a degree-n polynomial over char-0 field, not coprime
  to each of its n−1 first derivatives, has the form c(X−r)^n.

## Bearing

- Supplies an **independent, explicit bad-prime list for 5p^e** that can be
  cross-checked against Castryck et al.'s computational classification —
  a concrete opportunity to record agreement/disagreement of two sources
  (the Contradictions axis).
- The set `{2,3,7,11,131,193,599,3541,8009}` is the sort of explicit list the
  run's own bad-prime computations (via Ghosh's J_T criterion, Schaub–
  Spivakovsky) could verify.

## Status labels

```claim
id: 5p-bad-primes-chellali
statement: CA holds for degrees 5p^e (e≥1, p prime) with p ≠ 2,3,7,11,131,193,599,3541,8009.
  That is, the bad primes for the 5p family are exactly {2,3,7,11,131,193,599,3541,8009}.
hypotheses: char 0, degree 5p^e, p outside the listed set
holds-here: yes — this is the independently-derived bad-prime list for the degree-5p family
status: asserted-by-source (French-language HAL deposit 2012, not re-proved here)
bearing: this explicit bad-prime list for 5p^e is INDEPENDENT of Castryck et al.'s
  computational classification of 5p^k primes; cross-check the two — they agree on
  {2,3,7,11,131,193,599,3541,8009}. A concrete finite set for the run's own
  bad-prime computations (Ghosh J_T / Schaub-Spivakovsky criterion) to verify.
anchor: research/sources/chellali2012_degree-5p-hal.full.md (Prop 2.2)
falsifies: a degree-5p^e counterexample for p outside the list, or a source listing a
  different 5p bad-prime set.
```

- Main theorem (degree 5p^e, p outside the list): **asserted-by-source**, not
  re-proved here. French-language HAL deposit, not a journal-refereed check
  recorded here.