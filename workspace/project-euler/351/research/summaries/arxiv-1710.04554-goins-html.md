# Goins–Harris–Kubik–Mbirika, "Lattice point visibility on generalized lines of sight" — full text

<!-- source: https://arxiv.org/html/1710.04554v1 -->

## What the full text establishes (beyond the abstract)

The paper (AMM 125(7):593–601, 2018; arXiv:1710.04554) defines b-visibility along
curves f(x) = a·x^b and proves the visible proportion is 1/ζ(b+1). Section 1
("Background") recapitulates the classical theory this run depends on:

- **Sylvester (1883)**: the proportion of lattice points (m,n) ∈ ℕ×ℕ visible from the
  origin is 1/ζ(2) = 6/π².
- A point (r,s) is visible from (0,0) iff gcd(r,s) = 1 (the primitive-point criterion).
- The b = 1 specialization is exactly the classical setting.

The paper also proves (Proposition, §2) that for every fixed b there are arbitrarily
large rectangular arrays of b-invisible points — for b = 1, arbitrarily large
gcd > 1 blocks, e.g. {(kn + i, kn + j)} for any k ≥ 2.

## Claim for the ledger

```claim
id: visible-density-zeta-goins
statement: The proportion of lattice points in Z^2 visible from the origin is
1/zeta(2) = 6/pi^2 (Sylvester 1883); a point (r,s) is visible from (0,0) iff
gcd(r,s) = 1. Goins-Harris-Kubik-Mbirika (AMM 125(7):593-601, 2018, arXiv:1710.04554)
recover this as the b=1 case of their b-visibility result 1/zeta(b+1).
hypotheses: integer lattice Z^2, origin excluded, straight-line visibility.
holds-here: yes — the hexagonal orchard's triangular lattice is a rank-2 lattice,
and the brute-force oracle (gcd test) confirms the criterion at n = 5, 10, 1000.
status: sourced (Goins et al. 2018, AMM; Sylvester 1883 via their §1; corroborated
by MathWorld VisiblePoint and this run's brute force).
bearing: fixes the governing lemma: a hexagonal-orchard point with axial coordinates
(a,b) is hidden iff gcd(|a|,|b|) > 1; the visible fraction 6/pi^2 is the magnitude
anchor for Phi(N) ~ (3/pi^2) N^2.
anchor: research/summaries/arxiv-1710.04554-goins-harris-kubik-mbirika-lattice-visibility.md
```
