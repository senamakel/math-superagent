# Takei, "Limiting measures for addition modulo a prime number cellular automata"

Source: https://doi.org/10.15803/ijnc.7.2_124 (Int. J. Networking and Computing 7(2), 2017). Full text at [[research/sources/takei_limiting_measures_rule90.full.md]].

## What it establishes

Linear CA with two-site neighborhood on {0,…,p−1}^Z, Λω(x) = ω(x−1)+ω(x+1) mod p
(exactly Rule 90 for p=2, and its generalization to prime moduli). For
shift-invariant probability measures:

- **Odd p.** For any strong mixing, shift-invariant measure µ, the iterates
  `Λ^n µ` converge **if and only if** µ is the point mass δ₀ or the uniform
  product µ_{1/p}. Among strong mixing shift-invariant measures, the only
  Λ-invariant ones are δ₀ and µ_{1/p}.
- **p = 2 (Rule 90).** A characterization of when iterates starting from a
  convex combination of strong mixing measures converge (in Cesàro sense); gives
  all invariant measures within that class.

This is measure *rigidity* for the fold: non-degenerate (mixing) input is driven,
on average, to the uniform measure — the unique non-trivial invariant state.

## Why it matters for SUPPLY

Supports the same structural picture as Pivato–Yassawi Thm 7.1 from the measure
theoretic side: the fold Φ = 1+σ (Rule 90) **de-randomizes** strong-mixing input
toward uniform along Cesàro (density-one) averages. For SUPPLY this is the
plausibility that `wt(Φ_n h)` is ~ n/2 on a density-one set of n *provided* h's
empirical measure is mixing — the finite-prefix transfer being the open step.

**Caveat.** Again an infinite-measure / Cesàro-ergodic statement; does not by
itself give a bound on the single deterministic fold of the prime string h.
Complements (does not replace) the sharp Lucas-mixing characterization of
Pivato–Yassawi for p=2.

```claim
id: takei-rule90-mixing-limits-uniform
statement: For the fold Λ (addition mod p, two-site neighbourhood; Rule 90 when p=2), if µ is strong mixing and shift-invariant, the Cesàro means of Λ^n µ converge iff µ is the point mass δ₀ or the uniform product measure µ_{1/p}; for p=2 the class of invariant measures among convex combinations of strong mixing measures is characterized.
hypotheses: neighbourhood includes x−1 and x+1; µ shift-invariant; strong mixing; p prime.
holds-here: For p=2 the fold is exactly Rule 90 — the finite version of SUPPLY's Φ. The convergence-to-uniform statement is a measure/Cesàro fact; the finite fixed-string transfer is not supplied.
status: sourced (Takei 2017)
bearing: Confirms, from the measure-theoretic rigidity side, the de-randomization of mixing input by Rule 90 toward uniform — the picture behind a density-1 `wt(Φ_n h) ≥ c·n`. Reinforces that the only missing link is the finite-prefix transfer and that h must be mixing (Lucas/harmonic), not merely "complicated".
anchor: research/sources/takei_limiting_measures_rule90.full.md
```
