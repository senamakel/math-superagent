# Li, "The number of primes in short intervals and numerical calculations for Harman's sieve" (arXiv:2308.04458)

<!-- source: https://arxiv.org/abs/2308.04458 | full text: research/sources/li-2023-primes-in-short-intervals-harman-sieve.full.md -->

Runbo Li, arXiv:2308.04458 [math.NT] (Aug 2023; v8). 44 pages.

## What it establishes

The key short-interval prime theorem, sharpened below the Baker–Harman–Pintz
exponent:

> **Theorem 1:** For all sufficiently large x, the interval [x − x^θ, x] contains
> at least one prime for every θ ≥ 0.52. Equivalently the maximal prime gap
> satisfies G(x) ≤ x^0.52 ultimately with a short interval [x, x + x^0.52].

This answers Harman–Pintz's argument and **improves Baker–Harman–Pintz 2001
(α = 0.525) to α = 0.52**. Theorem 2 gives nontrivial upper and lower bounds for
the number of primes in [x − x^θ, x] for 0.52 ≤ θ ≤ 0.525.

## Why it matters for this run (Route B, Granville ν_2 reduction)

Granville's Theorem 5.5 reduces Gilbreath's conjecture to a lower bound
ν_2 > n^β with β > α, where α is the exponent of an unconditional
"interval [x, x + x^α] contains a prime" theorem (the demand side). The run's
recorded α = 0.525 comes from BHP 2001. **This paper reduces α to 0.52, i.e. the
demand side is strictly weaker than recorded — β > 0.52 would suffice, and the
measured ν_2/n ∈ [0.42, 0.52] is even closer to n/2 than to n^0.525.**

The techniques (Harman's sieve, explicit integral estimates, the long-omitted
calculation steps for how the 0.525 barrier is pushed toward 0.52) are the
referee route for re-deriving the demand side with a tighter exponent.

## Status

- Claim-worthy: `li2023-short-interval-052` — the interval [x, x + x^0.52]
  contains a prime for all large x, unconditional.
- **Falsifier:** a source or computation showing the exponent 0.52 cannot be
  reached or is wrong.
- Not peer-reviewed at arXiv v8 as downloaded; chains use it as the sharpened
  demand side, and BHP 2001 (whose primary text failed to download on 4
  routes: malformed Maryland PDF, Wiley paywall, malformed Wayback, CiteSeerX
  connection error) remains the canonical citation.
