# Lemke Oliver–Soundararajan, "The distribution of consecutive prime biases and sums of sawtooth random variables"

Source: https://doi.org/10.1017/s0305004118000592 (Math. Proc. Cambridge Phil. Soc. 168 (2020) 149–169; online 2018). **Full text now held** (complete, all equations) at [[research/sources/lemke_oliver_soundararajan_sawtooth.full.md]], obtained via arXiv:1709.06168 (ar5iv html). The older partial capture (abstract + front matter only) remains at [[research/sources/los_sawtooth_consecutive_prime_biases.full.md]] and is superseded for the body.

## What it establishes (from the sources obtainable)

Companion to the 2016 PNAS "Unexpected biases" paper. The 2016 paper conjectured,
via Hardy–Littlewood k-tuples, that consecutive-prime residue patterns (mod q)
occur with their expected fair-share density in the limit, with slowly-decaying
secondary terms creating the observed biases. This 2018 paper isolates and studies
that **secondary term**:

- The residual variation among patterns beyond the dominant term is governed by a
  quantity connected to the **Fourier transform of classical Dedekind sums** and to
  the **error term in the summatory function of Euler's φ(n)**.
- The main theorem concerns the distribution of the sawtooth-sum quantity C(k)
  (and related sums) over k and over moduli q: as q → ∞, a near-continuous,
  symmetric limiting distribution emerges; there are short-sum approximations
  giving **average (grand-average) behavior across q** and showing **equidistribution
  on average**.

## What it means for SUPPLY

This is the strongest available lever for GOAL priority 1 (the **averaged** form).
The parity barrier for consecutive-prime **pair** residues mod 4 (the switch-density
form) is pointwise, but LOS here show that when one **averages over moduli q** (or
over the relevant parameters) the bias structure becomes equidistributed and
trackable — "equidistribution on average across q". If an analogous **average over
the fold's submask parameters** can be made to give positive switch density on
average, that is exactly the density-1 route: `wt(Φ_n h) ≥ c·n` for almost all n.

**Caveat.** This is conjectural in the relevant (pair-frequency) aspect — the
fair-share conjecture rests on Hardy–Littlewood. The *average-across-q*
equidistribution the paper proves is over moduli q, not over the fold-time
parameter n of SUPPLY; transferring it to `wt(Φ_n h)` for the fixed string h is
again an open bridge, and one the paper does not make. Still, it is the correct
reference for "the averaged form is porous to the parity barrier" and is
tangentially the arithmetic heart of the density-1 target.

```claim
id: los-sawtooth-averaged-bias-equidistributed
statement: In the Lemke-Oliver-Soundararajan framework for consecutive-prime residue-pattern frequencies (mod q), the secondary bias term is controlled by Fourier transforms of Dedekind sums and the Euler-φ summatory error; averaging over moduli q yields equidistribution on average (grand-average asymptotic), while the pointwise fair-share conjecture rests on Hardy-Littlewood and is not proved.
hypotheses: Hardy-Littlewood k-tuple heuristics for the fair-share conjecture; the average-across-q results are proved.
holds-here: The pointwise consecutive-pair frequency (switch-density) statement remains open (parity barrier); the average-across-q/over-parameters statement suggests the averaged form is the porous route the GOAL prioritises. Transfer to wt(Φ_n h) for fixed h is not made.
status: sourced (Lemke Oliver–Soundararajan 2018/2020; full text held via arXiv:1709.06168 — all theorems and proof details verified; see the companion summary file lemke_oliver_soundararajan_sawtooth.md for the full development including c₂ = C(k) q + O(...) and Thms 1.1/1.2/4.1/4.2)
bearing: Supports GOAL priority 1 — the density-1/averaged form of SUPPLY via averaged switch density — and provides the Dedekind-sum/φ-error vocabulary for the secondary terms. Does not settle SUPPLY; the fixed-string folded-weight transfer remains open.
anchor: research/sources/los_sawtooth_consecutive_prime_biases.full.md (abstract/front matter)
```
