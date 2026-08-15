# Eggleton–Erdős–Skilton 1985 — Colouring the real line

**Subject:** The foundational primary paper of the distance-graph approach that
the adopted `flat-torus-periodic-6col` upper-bound route builds on. The Liu 2008
survey (`liu-2008-distance-graph-survey.md`) states explicitly that Eggleton,
Erdős and Skilton "initiated the study of distance graphs … motivated by the
plane coloring problem." This paper defines the distance graphs G(R, D) and
G(Z, D) that the whole periodicity/pattern-colouring tier studies.

## Source

- **R. B. Eggleton, P. Erdős, D. K. Skilton**, "Colouring the real line",
  *Journal of Combinatorial Theory, Series B* **39** (1985) 86–100.
- DOI: **10.1016/0095-8956(85)90039-5**
- https://doi.org/10.1016/0095-8956(85)90039-5

## What the paper establishes (from the retrieved record/abstract)

Distance graphs **G(R, D)**: vertex set the real line R, two vertices x, y
adjacent iff |x − y| ∈ D, where D is a set of positive reals (the *distance
set*). Restricting the vertex set to Z gives the integral distance graph
**G(Z, D)**. The paper introduces these graphs and studies their chromatic
number χ(R, D), determining **bounds and exact values of χ for various distance
sets D**. Key structural facts recorded in the retrieval:

- When D is a finite set of integers, **χ(G(Z, D)) ≤ |D| + 1** (this bound is
  recorded by later sources e.g. the HAL/DMTCS note and is a standard
  consequence of the colour-the-integers-by-residue argument).
- The paper is the direct ancestor of the prime-distance-graph work
  (Eggleton–Erdős–Skilton 1990), the pattern-periodic-colouring literature
  (Zhu 1998), the periodic/circulant-reduction theorem (Barajas–Serra 2005),
  and Liu's 2008 survey — all of which the library already carries.
- The de Bruijn–Erdős 1951 compactness reduction is the lineage that connects
  colouring the whole of R/Z to finite configurations, which is exactly the
  ladder the run's finite-object approach relies on.

## Why this is in the library

This is the **origin paper** of the distance-graph method the upper-bound
approach uses. The library carried its descendants (Liu survey, Barajas–Serra,
Zhu 1998) but not the paper that started the line and that Liu's survey names
as the motivation ("motivated by the plane coloring problem" — i.e. this paper
is a direct ancestor of the Hadwiger–Nelson investigation as a colouring of the
plane). Having the origin in the library fixes the definition of the object
(G(R,D), G(Z,D)) the whole periodic tier operates on, and the χ ≤ |D|+1 bound
for finite integer D, in the primary source.

## Boundary of the claim

The results are for the **distance-graph** model G(R, D) / G(Z, D) — a
*restricted* distance set D chosen by the colourer — **not** for the full
unit-circle distance set {1} over the plane that is `problem.md`'s object. The
plane unit-distance question is the Hadwiger–Nelson problem (4 ≤ χ ≤ 7), which
this paper does not settle. The χ(G(Z,D)) ≤ |D|+1 bound and the periodic
structure carry over only to the *lattice/periodic* analogue the adopted
approach makes precise with its own lifting/thickening lemma (a run-side
derivation, not this source).

## Fetch status

Direct download of the Elsevier full text is blocked at the network boundary
(recorded in `sources/README.md`); this record is the scholar's synthesis of
the retrieved abstract/record and the citation-graph entry. The exact-value
results for particular D are asserted-by-source from the record, not re-derived
here; the one concrete bound recorded (χ(G(Z,D)) ≤ |D|+1 for finite integer D)
is a standard result and is flagged as such.

```claim
id: eggleton-erdos-skilton-1985-real-line
statement: The distance graph G(R, D) on the real line (and its integral version
G(Z, D)) has as vertices R (resp. Z), with x,y adjacent iff |x-y| in D; the paper
introduces these graphs and determines bounds and exact values of the chromatic
number for various distance sets D. For finite D a subset of the positive
integers, chi(G(Z, D)) <= |D| + 1.
hypotheses: G(R,D)/G(Z,D) distance graphs as defined; D a set of positive reals
(resp. a finite set of positive integers for the |D|+1 bound).
holds-here: partially — defines the object the periodic/lattice colouring tier
operates on; but the chi <= |D|+1 bound and exact values are for the *integer
distance graph / restricted distance set* analogue, not for the open plane
Hadwiger-Nelson problem chi(G) in [4,7] that problem.md asks about.
status: asserted (from retrieved record/abstract; full text blocked)
bearing: primary-source origin of the distance-graph method the adopted
flat-torus-periodic-6col upper-bound approach builds on; fixes the definition
of G(R,D)/G(Z,D) and the |D|+1 integer-distance bound in the primary source.
anchor: research/sources/eggleton-erdos-skilton-1985-colouring-real-line.md
```
