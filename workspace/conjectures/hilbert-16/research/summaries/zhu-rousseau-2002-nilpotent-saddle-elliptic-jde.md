# Zhu–Rousseau 2002, "Finite cyclicity of graphics with a nilpotent singularity of saddle or elliptic type" (JDE 178:325–436)

Source: `research/sources/zhu-rousseau-2002-nilpotent-saddle-elliptic-jde.full.md` [[zhu-rousseau-2002-nilpotent-saddle-elliptic-jde.full]] — from YorkSpace bitstream fc2121d3.

## What the source establishes

The **primary machinery** behind the nilpotent-graphics closures (inside the
88-by-2015 tally).

- **Definition 1.1 (finite cyclicity)** — the formal definition this run's
  claims use: a limit periodic set C of X_{m0} has finite cyclicity in the
  family X_m if there exist N ∈ N and ε, δ > 0 such that any X_m with
  |m − m0| < δ has at most N limit cycles within Hausdorff distance ε of C;
  the minimum such N as ε, δ → 0 is `Cycl(C)`.
- **Object**: graphics through a nilpotent point of **saddle or elliptic type**
  of codimension 3 in C^∞ families; several results depend only on the
  nilpotent point having **multiplicity 3**, not the exact codimension.
- **Method**: blow-up of the family → all limit periodic sets; two types of
  **Dulac maps** in the blown-up family; a general method proving some regular
  transition maps have a **nonzero higher derivative**; finite cyclicity via
  Roussarie's generalized **derivation–division** method.
- Proposition 4.5: if the hyperbolicity ratio r₀ = 1, the Dulac map has a
  well-ordered asymptotic expansion (the property that fails in Dulac's
  original error, restored here for the r₀=1 resonance-lemma case).
- Theorem 4.10/4.14: the normal-form Dulac maps of the blown-up saddle with
  eigenvalues −1, 1, σ(a₀).

## What it implies here

Anchor for claim `drr-zhu-rousseau-2002-nilpotent-machinery`. The
derivation–division method is exactly the finite core GOAL.md wants carried in
Lean: cyclicity of a nilpotent graphic is bounded by the order of a transition
map, which is a statement about a function's Taylor coefficients — checkable
algebraically once the normal form is fixed. Definition 1.1 is the precise
notion that `holds-here: yes` claims about graphics must reference.

Evidence class: sourced-held — read from the held full text. Hypotheses: planar
C^∞ families; graphics through nilpotent saddle/elliptic point of codimension 3
(multiplicity 3 in some cases). Falsifier: a codimension-3 nilpotent graphic
with unbounded cyclicity.

Claim id `drr-zhu-rousseau-2002-nilpotent-machinery` (full statement in
`research/notes/claims.md`).