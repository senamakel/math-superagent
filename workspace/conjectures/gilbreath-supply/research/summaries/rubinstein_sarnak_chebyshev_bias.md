# Summary — Chebyshev's Bias

Source: Michael Rubinstein, Peter Sarnak, *Experimental Mathematics* 3(3)
(1994) 173–197.
Full text: `research/sources/rubinstein_sarnak_chebyshev_bias.full.md`
Source URL: https://www.math.uwaterloo.ca/~mrubinst/publications/Chebyshev.pdf

> Note on the full text: the PDF converts with corrupted glyphs (vector-font
> mathematics), so the saved full text is not legible in places. The substance
> of the main theorem is reported here as relayed by the Granville–Martin
> survey (`granville_martin_prime_number_races.md`, itself authoritative), and
> by the paper's own abstract. The bibliographic and abstract-level facts are
> reliable; any fine formula should be read from a legible copy before being
> quoted.

## What this source establishes

The foundational "prime race" paper. Chebyshev (1853) observed that primes ≡ 3
(mod 4) seem to predominate over primes ≡ 1 (mod 4). Rubinstein–Sarnak make this
precise, conditional on the Generalized Riemann Hypothesis (GRH) and the Grand
Simplicity Hypothesis (GSH — the zeros of Dirichlet L-functions are linearly
independent over ℚ):

- The normalised difference `(π(x;4,3) − π(x;4,1)) / (√x / log x)` has a
  limiting distribution.
- The set of x where 4n+3 leads has a **positive logarithmic density**, and for
  small moduli this density is essentially 1 (the bias is "there almost
  always").
- They characterise exactly which moduli/residue classes exhibit the bias.
- Generalisations to ideal classes in number fields and to prime geodesics.

The key structural fact: the lead is not a settled inequality (Littlewood showed
it switches infinitely often) but a positive-density phenomenon in the
logarithmic sense, and only provable conditionally.

## Why it matters for SUPPLY

This is the reference behind ABGS's positioning of the pair-frequency question
as a "prime race" situation. It establishes that *single-residue* biases persist
with positive density conditionally on GRH+GSH. The *pair* race that SUPPLY's
mod-4 switch density needs is one level higher and strictly harder: ABGS leave
even the single-pair-class limit open, and nothing unconditional is known. So
the Chebyshev-bias framework is the context for why any claimed positive limiting
frequency of the (1,3)/(3,1) pair class is at best conditional/conjectural —
reinforcing that SUPPLY must be pursued through the fold, not the raw frequency.

## Evidence class

Conditional theorem (GRH + GSH) + numerical investigation. Not an unconditional
statement about the primes.

```claim
id: rs-chebyshev-bias-positive-density
statement: Under GRH and GSH (linear independence of Dirichlet-L zeros), the normalised
  mod-4 race difference (π(x;4,3)−π(x;4,1))/(√x/log x) has a limiting distribution and the
  set of x where 4n+3 leads has positive logarithmic density (essentially 1 for small
  moduli).
hypotheses: GRH + GSH.
holds-here: conditional only; the unconditional fact is Littlewood's oscillation (lead
  switches infinitely often).
status: asserted-by-source (conditional theorem).
bearing: the single-residue race already requires GRH+GSH for a positive-density statement;
  the pair-race/frequency analogue needed for SUPPLY is harder and unconditionally unknown.
anchor: Rubinstein–Sarnak 1994 (main theorem), as relayed in Granville–Martin 2006 §3.
```

```claim
id: rs-pairrace-analogue-harder
statement: The consecutive-prime-pair residue-frequency question (whether e.g. (1,3)/(3,1)
  mod 4 occur asymptotically equally often, or with positive fixed frequency) is a
  strict generalisation of the single-residue prime race and is unconditionally unknown
  (ABGS §9).
hypotheses: —
holds-here: true; this is the reduction's dead end.
status: asserted-by-source (ABGS §9 open question; Rubinstein–Sarnak the single-class model).
bearing: the reason the run attacks the fold rather than the frequency.
anchor: ABGS 2011 §9; Rubinstein–Sarnak 1994.
```
