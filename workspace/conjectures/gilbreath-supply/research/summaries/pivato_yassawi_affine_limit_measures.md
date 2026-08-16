# Pivato–Yassawi, "Limit measures for affine cellular automata"

Source: https://arxiv.org/pdf/math/0108082. Full text at
[[research/sources/pivato_yassawi_affine_limit_measures.full.md]].

## What it establishes

**Setting.** LCA Φ on `A^{Z^D}` with A a finite abelian group (focus A = Z/p, p
prime). μ a shift-invariant probability measure.

**Concepts.** *Harmonic mixing*: Fourier coefficients along nontrivial characters
decay to 0, uniformly beyond a rank threshold. *Diffusion*: an expansiveness
property — the LCA spreads information so characters grow in rank under iteration.

**Main theorem.** For A = Z/p (p prime), **every nontrivial LCA on A^{Z^D} is
diffusive**. If μ is harmonically mixing (Bernoulli measures for D ≥ 1; N-step
Markov measures and many fully-supported Markov/product measures for D = 1), then
the iterates `Φ^N μ` weak-* converge to Haar measure **in density** (hence in
Cesàro average).

## Why it matters for SUPPLY

This is the earlier, ergodic-theoretic half of the randomization story for the
fold Φ = 1+σ. It establishes that *any* nontrivial LCA (in particular Rule 90 over
Z/2) de-randomizes harmonically-mixing input toward uniform. The connection the
run needs is: if the prime-gap-parity string's measure were harmonically mixing,
then `Φ^n h` would converge on average to a density-1/2 string — giving
`wt(Φ_n h) ≥ c·n`. But note the finite-prefix transfer (below) is the hard part.

**Caveat.** As with the companion paper, this is about measures on infinite
configurations and convergence in the weak-* / statistical sense; it does not
state anything about a single fixed deterministic `h` at a single finite fold
depth. It supplies vocabulary (harmonic mixing, diffusion) and the assurance that
the *only* obstruction to de-randomization is the input's mixing character.

Claim block: this read feeds the note
[[research/notes/pivato_lucas_mixing_equivalence.md]].
