# Derivatives of the Separation Function of Generalized Saddle Connections

**Authors:** (authors per Springer page; open access, Qual. Theory Dyn. Syst. 24, art. 227, 2025-10-03)
**Source URL:** https://link.springer.com/article/10.1007/s12346-025-01379-8
**Full text:** `research/sources/separation-function-generalized-saddle-connections-qtds-2025.full.md`
**Evidence class:** sourced-held (full open-access text downloaded 2026 librarian pass).

## What it establishes

The classical Melnikov formula studies the breaking of a saddle connection
between two *hyperbolic* saddles via a convergent improper integral (the
Melnikov integral / separation function). This paper generalises the *separation
function* to connections whose endpoints are **semi-hyperbolic** or even
**nilpotent** singularities — precisely where the classical improper integral
can **diverge**.

- **Theorem A** (main result): under convenient hypotheses there is a kind of
  *residue* that still gives the derivative of the separation function
  `∂_{μ_j} d(μ₀)`, even when the naive Melnikov integral is no longer
  convergent. Broadens the situations in which connection-breaking (and so
  limit-cycle bifurcation) can be detected.
- **Generalized saddle separatrix / saddle connection** (Definition 2.1): a
  geometric notion covering nodes, saddle-nodes, semi-hyperbolic and nilpotent
  endpoints, not just hyperbolic saddles. Lemma 2.3 + directional blow-up show
  arrival trajectories form generalized saddle separatrices as μ varies.
- **Examples:**
  - heteroclinic connection between two nodes;
  - **heteroclinic connection between semi-hyperbolic saddles at infinity**;
  - homoclinic connection in a non-elementary singularity at infinity;
  - a **quadratic perturbation of a center whose period annulus is unbounded
    and has a semi-hyperbolic hemicycle as outer boundary** ($\Gamma_{\mu_0}=\{x=1\}$
    with $D_0\in(-1,0)$, $F_0\in(0,1)$ in a quadratic versal unfolding (21); the
    separation function is written out explicitly on the transverse section).

## Why it matters to this run

This is **on the edge of the DRR program's machinery** and connects directly to
three living threads:

1. `drr-mv-hemicycle-cyclicity-2` and the `H³₁₄`/semi-hyperbolic hemicycle case
   (Lu 2026 preprint): hemicycles with semi-hyperbolic saddles at infinity are
   the exact setting where the classical (hyperbolic) Melnikov integral fails
   and both this residue formula and the stopped-first-hit / Dulac-map methods
   are needed. This paper provides an independent tool for the same objects.
2. `fake-saddle-transition-maps`: fake saddles (impassable grains) are the
   degenerate analogue; the same "the naive integral diverges but a residue
   carries the information" theme recurs.
3. The generalised *separation function* is the object the displacement-function
   reasoning in GOAL.md wants — a statement about how many zeros/breaks a family
   of connections can have.

## Status / caution

- Open-access, refereed (QTDS 2025). This library's DRR picture is **unchanged**
  by it — it does *not* close a DRR graphic or change the open/closed count —
  but it is a **methodological addition** relevant to the semihyperbolic/nilpotent
  saddle-connection machinery the open hemicycle graphics require.
- Not to be confused with a closure of any DRR graphic; it is a tool paper.
