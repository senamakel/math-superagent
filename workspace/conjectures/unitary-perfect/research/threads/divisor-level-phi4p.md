# The divisor-level problem for Φ_{4p}(2) — where the analytic target lives

```thread
question: Can one prove that for all sufficiently large odd primes p in P_3
  (the 3-Higgs primes), some prime divisor of Φ_{4p}(2) is NOT 3-Higgs — a
  divisor-level statement that would close H_even and hence the
  Subbarao–Warren reduction?
status: open
rests-on: heven-prime-case-reduction, heven-two-mod-four,
  heven-thinness-not-finiteness, aurifeuillean-split
blocked-by: No divisor-level transference theorem exists (per Maciejewski
  §5.3/§6): standard effective Chebotarev even under GRH controls varying
  primes in ranges, not the prime support of a single fixed cyclotomic value.
  The log-mass vs reciprocal-mass gap is exponential (2^(2p)/p). Conjectures
  23, 24, 29 in the paper are the candidate theorems; none is proved.
next: (1) compute ω(Φ_{4p}(2)) and the v2 distribution of its prime divisors
  for a stated range of primes p to test Conjecture 29 empirically; (2) test
  the mod-16 equidistribution on the known prime factors of the open
  candidates; (3) look for a congruence class of p where an r ≡ 1 (mod 16)
  divisor can be proved to exist by algebraic factorization.
```

## The question

Maciejewski's reduction (arXiv:2605.20475, Theorems 7, 21, §5.3) leaves
exactly one branch: prove `H_even` finite, equivalently (Theorem 7) that only
finitely many odd primes `p` have every prime divisor of `2^(2p) + 1`
3-Higgs. The named analytic target is a divisor-level statement about the
cyclotomic value `Φ_{4p}(2)`.

## Why divisor-level and not density-level

For `m = 2p`, a primitive prime divisor `r` of `2^(2p)+1` has
`ord_r(2) = 4p`, so `r ≡ 1 (mod 4p)` and `(r-1)/(4p)` must be in the
Higgs-cubefree semigroup `S_3^(≤3)` for `r` to be 3-Higgs. The three
ingredients — recursive semigroup friability, exponent cap, exact
multiplicative order — do not appear together in the shifted-prime smoothness
literature (Baker–Harman, Banks, Liu–Wu–Xi, Lamzouri, BFPS). And Chebotarev
density is the wrong scale: the prime support of `Φ_{4p}(2)` is a *single
finite integer*, not a range of primes.

## The structural facts available (all sourced)

1. `2^(2p)+1 = 5 · Φ_{4p}(2)` and `log(2^(2p)+1) ~ 2p log 2`. The primitive
   divisors must carry log-mass `≫ p` (Hong's valuation bound, Prop. 2.4 in
   arXiv:2204.01858, bounds the non-primitive part by `O(log(4p))`).
2. Ford's theorem (arXiv:1212.3498): the 3-Higgs primes form a power-saving
   thin set `Π_3(x) << x^(1-δ)` (smallest omitted prime is 17). But at the
   primitive-divisor height `x = 2^(2p)` this is still exponential in `p`, and
   even `x/(log x)^(1+ε)` stays exponential — density cannot close it.
3. Reciprocal-mass bound from ford-type thinness: `Σ_{r admissible} 1/r << 1/p`.
   A single admissible prime near `2^(2p)` has reciprocal mass `~2^(-2p)` but
   log-mass `~2p log 2`; the gap is `2^(2p)/p`. This is exactly the scale
   obstruction the paper identifies.
4. Aurifeuillean split: `2^(2p)+1 = L_p · M_p`, `L_p = 2^p − 2^((p+1)/2) + 1`,
   `M_p = 2^p + 2^((p+1)/2) + 1`, each ≈ half the bit length — special-form
   SNFS targets. The open candidates (e.g. 2426, 2602) are blocked by
   unfactored cofactors of these halves.
5. Empirical facts from the paper (not theorems): across the 53 open
   candidates with m ≤ 20000, the known prime factors have
   `v2(q−1) ∈ {2,3}` only (53 at 2, 29 at 3, 0 at ≥ 4); no prime
   `r ≡ 1 (mod 16p)` below `10^11` divides any `L_p`/`M_p`. So the mod-16
   "coin flip" has never thrown a heads in the verified region, consistent
   with the heuristic that it becomes inevitable as `ω(Φ_{4p}(2))` grows.

## The candidate theorems

- (The paper's Conjecture 29, divisor mod-16 equidistribution) There is
  `c > 0` with `#{r | Φ_{4p}(2) : r ≡ 1 (mod 16)} ≥ c·ω(Φ_{4p}(2))` for all
  large `p ∈ P_3`. Any such `r` has `v2(r−1) ≥ 4` and is not 3-Higgs, closing
  the branch. Requires `ω(Φ_{4p}(2)) → ∞`, which is the open (H2) gap.
- (The paper's Conjecture 24, log-mass bound) `Σ_{r ≤ 2^(2p)+1, r ≡ 1
  mod 4p, (r−1)/(4p) ∈ S_3^(≤3)} log r ≤ (2 log 2 − δ)p` — a divisor-level
  log-mass bound that would close directly.
- The realistic local goals: prove structure on `ω(Φ_{4p}(2))`, or prove
  `r ≡ 1 (mod 16)` occurs among the divisors for a congruence class of `p`,
  or show the 2-adic valuation distribution of primitive divisors is not all
  `≤ 3`.

## What would close the branch

A proof that for all sufficiently large primes `p ∈ P_3`, some prime divisor
of `Φ_{4p}(2)` is NOT 3-Higgs. Equivalently, a divisor-level transference:
the set `{r : r | Φ_{4p}(2)}` inherits equidistribution properties from the
ambient set `{q ≤ 2^(2p) : q ≡ 1 (mod 4p)}`. The paper argues no standard
effective Chebotarev (even under GRH) gives this; the missing object is a
transference from random shifted primes to fixed cyclotomic values.

## Status

OPEN — this is the branch the run targets. Nothing here is a theorem this run
proved; everything is sourced from the library. Any contribution must be
stated with its evidence class.