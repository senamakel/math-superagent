# Gallagher 1976 — "On the distribution of primes in short intervals"

**Full text:** `research/sources/gallagher-1976-primes-in-short-intervals.full.md` [[gallagher-1976-primes-in-short-intervals.full]]
**Source:** P. X. Gallagher, *Mathematika* 23 (1976) 4–9, doi 10.1112/S0025579300016442 (Columbia).

## What it establishes

**Theorem 1.** Let `P_k(h, N)` = number of integers `n < N` whose interval
`(n, n+h]` contains exactly `k` primes. Then, as `N→∞` with `h ~ λ·log N`,

```
P_k(h, N) / N  →  e^(−λ) · λ^k / k!    (Poisson with parameter λ),
```

**provided** the prime `r`-tuple conjecture (Hardy–Littlewood singular-series
asymptotic, formula (1)) holds uniformly for each `r` over distinct
`1 ≤ d_1,…,d_r ≤ h`. The proof goes through the moments of
`π(n+h) − π(n)` via the `r`-tuple formula, using that the singular series
`𝒮_d` averages to 1 over cubes (3).

**Theorem 2 (unconditional).** For positive constants `μ > λ`, the number of
`n < N` with `π(n + λ log N) − π(n) > μ` is `< N·e^{−cμ}` for an absolute
constant `c` — an **exponential upper bound on the tail**, obtained by
Selberg-sieve bounds (Klimov / Halberstam–Richert Thm 5.7) in place of the
unproved `r`-tuple conjecture.

## Hypotheses and whether they hold here

- Theorem 1 is **conditional** on the unproved Hardy–Littlewood prime
  `r`-tuple conjecture — it does not hold unconditionally for the primes.
- Theorem 2 is unconditional but a tail upper bound only; it controls large
  deviations of prime counts in short intervals, not the gap distribution
  feeding the Gilbreath triangle.

## Bearing on this run

This is the **primes-in-short-intervals / Poisson model** root that justifies
why the Cramér random model (Chase 2024, CHT 2026) treats normalized prime
gaps as roughly i.i.d. geometric/independent: under the `r`-tuple conjecture
the short-interval prime count is Poisson, which is the model those papers
instantiate. It is therefore a *justification-for-the-model* source, not a
result usable directly on the Gilbreath operator.

**Cited basis, not free background.** Odlyzko 1993 (held, LaTeX source §on
independence) cites Gallagher for exactly this: "There is a proof by Gallagher
that a form of the Poisson law for prime gaps follows from a quantitative form
of the Hardy–Littlewood prime k-tuple conjecture, and one can apply
Gallagher's arguments directly to conclude that the d_1(n)/2 reduced modulo 2
are independent for nearby values of n." CHT 2026 (held, §intro, ref [4]) use
"the Cramér model (or the calculation of Gallagher)" to predict the expected
value of the normalized-gap Gilbreath array grows like (c_j/2)·log n. So
Gallagher is the cited foundation of the independence/randomness assumption
the run's random-analogue sources rely on — worth recording as the link, even
though it contributes no Gilbreath-specific result.

- **Does not help compute or bound anything in the run's {0,2} machinery.**
  It says nothing about iterated absolute differences, block regeneration,
  or the leading-entry reduction.
- **Cannot certify a (2,4)-event rate bound:** the Poisson law is a mean/
  distribution statement conditional on an unproved conjecture, and even
  unconditionally it is a count bound, not a regeneration-rate bound.

## Claim

```claim
id: gallagher-1976-poisson-short-interval-model
statement: Under the (unproved) Hardy–Littlewood prime r-tuple conjecture, the
  number of primes in (n, n+h] for h ~ λ log N is Poisson(λ)-distributed in
  n < N (Theorem 1); unconditionally the count has an exponential upper bound
  on its upper tail (Theorem 2).
hypotheses: r-tuple conjecture uniform over cubes (Thm 1); none for the tail bound (Thm 2)
holds-here: unchecked (Thm 1 conditional on unproved conjecture; irrelevant to the iterated-difference operator)
status: proved
bearing: justifies the Cramér/Poisson random model used by Chase 2024 and CHT 2026;
  no direct use on the {0,2} block-regeneration machinery
anchor: research/sources/gallagher-1976-primes-in-short-intervals.full.md
```

## Why it was filed

Background source supporting the randomness assumption behind the random-analogue
literature already held. Not load-bearing for the run's combinatorial target; recorded so
nobody re-fetches it expecting a gap bound usable on the Gilbreath operator.
