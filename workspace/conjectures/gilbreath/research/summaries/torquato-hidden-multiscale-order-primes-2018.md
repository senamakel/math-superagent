# Torquato–Zhang–De Courcy-Ireland, "Hidden multiscale order in the primes" (2018)

**Full text:** `research/sources/torquato-zhang-decourcy-ireland-hidden-multiscale-order-primes.full.md`
**Source URL:** https://arxiv.org/pdf/1804.06279 (arXiv:1804.06279v2 [math.NT], 16 Jun 2018)
**Published:** arXiv preprint; companion numerical study Zhang–Martelli–Torquato, "Structure factor of the primes", J. Phys. A 51 (2018) 115001.

## What it establishes

- **Setting:** primes in the interval `M ≤ p ≤ M+L` where **`L/M → β > 0`** — the "dyadic / long-interval" regime where the density `1/log M` is essentially constant. This is *not* the short-interval (`L ~ log M`) regime where Gallagher's Poisson result applies, and it is not about consecutive prime gaps at all.
- **Proposition 1 (conditional on Hardy–Littlewood prime-pairs):** the density-scaled structure factor of the primes `S(k)/(2πρ)` converges to a sum of dense Bragg (Dirac-delta) peaks at rational `k/π = m/n` for odd, square-free `n`: `Σ_n ♭ Σ_m^x φ(n)^{-2} δ(k − mπ/n)`.
- **Proposition 2:** primes in this regime are hyperuniform of **class II** (number variance `σ²(R) ~ log R`, structure factor effectively linear in `k` as `k→0`), like the Riemann zeta zeros but with dense Bragg peaks rather than a continuous structure factor.
- **Proposition 3:** the scalar order metric `τ` (deviation from uncorrelated) scales `τ/ρ² ~ cL`, growing with system size — the primes are "effectively limit-periodic."
- The limit-periodic form of the structure factor is an **equivalent formulation of the Hardy–Littlewood prime-pairs conjecture** (`m=2` fixed-separation case `r=2,4,6,…`) — the authors explicitly say they have **no proof** of it.

## What it does NOT establish (bearing for this run)

- It is a **two-particle / pair-correlation result on long intervals**, entirely conditional on Hardy–Littlewood. It gives **no unconditional statement** and says **nothing about consecutive primes or gaps modulo 4**.
- It contains **no lower bound on the frequency of consecutive-prime residue switches** — the atomic object Granville's ν₂ / this run's G-supply needs. In particular it does not touch whether `N(a,d,m,x)/π(x)` (ABGS 2011 §9) has any limit, nor the two-point mod-4 correlation bound.
- So it is **not** a supply-side witness for Route B. It should not be cited as one.

## Claim

```claim
id: torquato-2018-primes-hidden-multiscale-order-long-intervals
statement: Conditionally on the Hardy–Littlewood prime-pairs conjecture, the primes in a dyadic/long interval M≤p≤M+L with L/M→β>0 are "effectively limit-periodic": density-scaled structure factor S(k)/(2πρ) → Σ_{n odd squarefree} Σ_{m⊥n} φ(n)^{-2} δ(k−mπ/n), hyperuniform of class II (σ²(R)~log R), and τ/ρ²~cL. This is an equivalent restatement of HL on fixed-separation pairs (m=2), not a proof of it.
hypotheses: primes; long-interval regime L/M→β>0; conditional on Hardy–Littlewood prime-pairs conjecture.
holds-here: no — this is pair correlation in LONG intervals, entirely HL-conditional; it neither needs nor supplies any fact about consecutive primes, gaps mod 4, or the ν₂ supply side of Route B.
status: asserted (conditional on HL; the conditional derivation is the paper's own)
bearing: a frontier-twice-cited source that does NOT bear on this run's open question. Prevents over-citation: it is a long-interval structure-factor result, not a consecutive-prime mod-4 frequency result.
anchor: research/sources/torquato-zhang-decourcy-ireland-hidden-multiscale-order-primes.full.md
answers: does-torquato-bear-on-mod4-supply
```
