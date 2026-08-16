# Summary — Prime Number Races

Source: Andrew Granville, Greg Martin, *Amer. Math. Monthly* 113 (2006) 1–33.
Full text: `research/sources/granville_martin_prime_races.full.md`
Source URL: https://personal.math.ubc.ca/~gerg/papers/downloads/PNR.pdf

## What this source establishes

The canonical survey of Chebyshev-type biases in the distribution of primes
among residue classes. The mod-4 race: primes 4n+3 vs 4n+1. Chebyshev (1853)
observed 4n+3 often leads; the PNT-AP says the two are asymptotically equal, so
the "bias" is a phenomenon of the *fluctuations*, not the limit.

Key content for this run:
- The limit distribution of `(π(x;q,a) − π(x;q,b))` does not converge pointwise;
  under GRH + linear independence (Rubinstein–Sarnak) the normalized difference
  has a limiting distribution, and one residue class prevails *on a set of x of
  positive logarithmic density*.
- So biases persist on sets of positive density, but "which class wins" is a 0/1
  race in the logarithmic-density sense, not a simple inequality.

## Why it matters for SUPPLY

The mod-4 consecutive-prime *pair* question that SUPPLY's reduction needs is an
analogue of a prime race but for pairs, and is strictly harder: ABGS leave open
even the single-class asymptotic equality, and LOS conjecture only under HL. The
Granville–Martin framework explains that the *single-residue* races are already
oscillatory with positive-density leads, so any argument that a specified
pair-frequency has a positive limit must contend with the same phenomenon one
level up. It is context for the parity barrier, not a tool that bypasses it.

## Evidence class

Survey; the Rubinstein–Sarnak results it reports are proved *conditional on GRH
and linear independence hypotheses*. The observed biases are numerical.

```claim
id: gm-chebyshev-bias-positive-density
statement: In prime number races mod q, under GRH + linear independence, each residue class
  leads on a set of x of positive logarithmic density; the race does not converge pointwise.
hypotheses: GRH and linear independence of Dirichlet L-functions.
holds-here: true as the structural context for why the mod-4 pair-frequency question is
  subtle; the unconditional statements are only numerical.
status: asserted-by-source (conditional theorems + numerical surveys).
bearing: the frequency question behind SUPPLY is a pair-race generalisation; the
  single-residue races already show positive-density oscillation. Reinforces that a
  density-1 linear bound for ν₂ would have to be proved through the fold, not read off any
  naive frequency bias.
anchor: Granville–Martin 2006, §§1–3, 6.
```
