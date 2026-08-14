# Raigorodskii — Borsuk's problem and the chromatic numbers of some metric spaces

**Source:** doi:10.1070/rm2001v056n01abeh000358
**Author:** A. M. Raigorodskii, Russian Mathematical Surveys 56 (2001)
Also related: A. M. Raigorodskii, "Coloring Distance Graphs and Graphs of
Diameters" (2012), doi:10.1007/978-1-4614-0110-0_23.
**Full text:** not on disk; read via read_sources.

## What this establishes (survey — the standard reference for the subject)

The colouring-of-the-plane problem is the widest-known instance of a family:
chromatic numbers of distance graphs in metric spaces, and Borsuk-type partition
problems. This survey consolidates the methods:

- **Lower-bound techniques:** constructing distance-based configurations
  (spindle-like structures) that force many colours; the spindle family is the
  standard construction engine for lower bounds, matching problem.md's
  "spindling" lead.
- **Upper-bound techniques:** tiling/combinatorial partition strategies; the
  7-colour hexagonal tiling of the plane is the canonical upper-bound
  construction; the survey discusses distance-realization constraints.
- **Density and independence:** how colour classes (independent sets) are
  constrained, feeding measurable-chromatic-number variants (which the problem
  statement explicitly says are NOT the target — a warning to record).
- Low-dimensional refinements, 3-space colourings (e.g. Coulson 1997, 18 colours
  omitting distance 1), and generalisations of the chromatic notion.

## Why it matters here

This fixes the vocabulary and the method landscape: spindle constructions,
tiling upper bounds, density of independent sets, and the measurable variant
boundary. The run's constructions should be measured against this taxonomy.

```claim
id: raigorodskii-method-landscape
statement: The standard method landscape for chi(R^2,1): lower bounds via spindle-like rigid configurations; upper bounds via tiling partitions (hexagonal 7-colouring); colour-class density bounds feeding measurable variants. The measurable-chromatic-number problem is a strictly larger lower bound and is NOT the plain problem.
hypotheses: Plain (non-measurable) chromatic number of the plane is the target; measurable variant demands extra structure on colour classes.
holds-here: true — fixes the boundary: the run attacks the plain problem; a result under a measurability hypothesis must be marked as the variant.
status: sourced (survey)
bearing: Positions the run's methods (spindles, tilings, density) in the standard landscape and marks the measurable-variant boundary.
anchor: research/sources/raigorodskii-chromatic-metric-spaces.md
```

## Note on download

Full text blocked at network layer. Content from read_sources survey summary.
Status: **sourced via read_sources; full text not on disk.**