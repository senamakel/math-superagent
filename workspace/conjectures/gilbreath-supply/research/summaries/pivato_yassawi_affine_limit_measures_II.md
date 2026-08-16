# Pivato–Yassawi, "Limit measures for affine cellular automata II"

Source: https://arxiv.org/pdf/math/0108083. Full text at
[[research/sources/pivato_yassawi_affine_limit_measures_II.full.md]].

## What it establishes

Companion to the affine-limit-measures paper. Strengthens the de-randomization
picture for linear CA over finite abelian groups A:

- **Theorem 2.** For p prime and A = Z/p, **every nontrivial LCA on A^{Z^D} is
  diffusive** (D ≥ 1).
- **Theorem 3.** If A is a finite abelian group, F an LCA, and µ a **harmonically
  mixing** measure, then **if F is diffusive, there is a Cesàro-density-one
  J ⊂ N with `wk*-lim_{J∋j→∞} F^j µ = Haar`**.
- **Proposition 14.** Fully supported Markov random fields on A^{Z^D} are
  harmonically mixing, for any abelian A.
- **Theorem 6.** For A = Z/n, F is diffusive if, for each prime divisor p of n,
  at least two coefficients of F are relatively prime to p.

## What it means for SUPPLY

Chain the three: for the fold F = 1+σ over Z/2 (Rule 90):
- F is nontrivial ⇒ diffusive (Thm 2);
- if the input measure µ is harmonically mixing (e.g. a fully-supported Markov /
  MRF — Prop 14), then F^j µ → Haar along a density-one set J (Thm 3).

So Rule 90 de-randomizes any harmonically-mixing input toward uniform in the
Cesàro/density-1 sense. Combined with Pivato–Yassawi Thm 7.1 (Lucas mixing is
equivalent to randomization for this exact automaton), the picture is complete on
the *measure* side: the only thing that stops
`wt(Φ_n h) ~ n/2` on a density-one set of n is whether the empirical law of the
prime-gap-parity string h is mixing (Lucas / harmonic). That is the arithmetic
input, and the finite-prefix transfer to the deterministic string is the open
step. This paper supplies the mixing notion (harmonic mixing) that the run should
target when trying to establish h is mixing.

```claim
id: harmonic-mixing-randomized-by-rule90
statement: For p prime and A=Z/p, every nontrivial LCA F on A^{Z^D} is diffusive (Thm 2); if µ is harmonically mixing then F^j µ weak-*-converges to Haar along a Cesàro-density-one J (Thm 3). Fully supported Markov random fields are harmonically mixing (Prop 14).
hypotheses: A finite abelian, M=Z^D, F a nontrivial LCA, µ harmonically mixing.
holds-here: For F=1+σ over Z/2 this is exactly the fold; harmonically-mixing or fully-supported-Markov input is de-randomized toward uniform at density-one times. Finite fixed-string transfer not supplied.
status: sourced (Pivato–Yassawi, math/0108083, Thms 2,3; Prop 14)
bearing: Gives the concrete arithmetic target for GOAL priority 1 (density-1 `wt ≥ c·n`): show the empirical measure of the prime-gap-parity string h is harmonically mixing (e.g. via Markov/autocorrelation decay), then transfer. Names "harmonic mixing" as the input to check.
anchor: research/sources/pivato_yassawi_affine_limit_measures_II.full.md
```
