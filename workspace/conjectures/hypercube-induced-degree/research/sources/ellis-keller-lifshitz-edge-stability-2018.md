# Ellis–Keller–Lifshitz, "On the structure of subsets of the discrete cube with small edge boundary" (Discrete Analysis, 2018)

Source URL: https://doi.org/10.19086/da.3668
Retrieved via `read_sources` (server-side); direct download blocked by the
network boundary.

Paper: David Ellis, Nathan Keller, Noam Lifshitz, *On the structure of subsets
of the discrete cube with small edge boundary*, Discrete Analysis (2018). Preprint
form widely circulated (arXiv). Companion to their *On a biased edge isoperimetric
inequality for the discrete cube*, JCTA 163 (2019).

## What this source establishes

A sharp stability ("almost isoperimetric" / structure) theorem for the cube
**edge** isoperimetric inequality, best possible up to the absolute constant C:

> For any m-element subset F ⊆ {0,1}^n and any integer l, if the edge boundary
> of F has size at most g_n(m) + l (where g_n(m) is the minimum possible edge
> boundary for size m), then there exists an extremal family G (an initial
> segment of the lexicographic order, up to cube automorphism) with
> |F Δ G| ≤ C·l for an absolute constant C.

This is the sharp stability version of Harper's edge-isoperimetric theorem: a
set whose edge boundary is near the minimum is quantitatively close to an
extremal (lexicographic initial segment = subcube-like) set, with distance
bounded by the excess boundary.

**Technique:** purely combinatorial, avoiding Fourier analysis. Proof by
induction on n, centred on an intermediate structure theorem (their
Proposition 4.1) about how F intersects codimension-1 and codimension-2
subcubes. Uses shifting/compressions, analysis of influences, and a six-ingredient
inductive strategy. Notably they show it *does not suffice* to pass only to
codimension-1 subcubes; codimension-2 is needed, which they frame as a warning
against abandoning an inductive approach in the cube.

## Why it is here

This is the frontier's highest-cited (4× by the library's own sources) missing
primary source and a genuine *technique* treatment of the edge-isoperimetric
stability problem — the natural sharp companion to Keevash–Long's stability (in
library) and Ellis 2011 (in library). It pins down with a sharp constant the
relation "small edge-boundary excess ⇒ close to a subcube".

Relevance to the problem: it concerns sets whose edge *boundary* (= total
influence, an average/outer quantity) is near minimal. Small boundary excess
means low total internal edge count, i.e. low *average* internal degree — not
low *maximum* degree D(S). So it confirms the obstruction: the structural
theory of edge-near-minimal sets controls averages and total dependence, and
says nothing about the max internal degree of the +1-vertex excess at
|S| = 2^{n-1}+1. It also matters to the methods debate: its purely-combinatorial
inductive (compression + influence) proof is the *standard alternative* to the
spectral-interlacing route; knowing exactly what it can and cannot produce
(influence/total-boundary structure, not max degree) is what the approach
comparison (AGENTS rule 8) needs.

## Claim block

```claim
id: ellis-keller-lifshitz-edge-stability
statement: For any F ⊆ {0,1}^n with |F| = m and edge boundary at most
  g_n(m) + l (g_n(m) = min edge boundary for size m), there is an extremal G
  (lexicographic initial segment, up to cube automorphism) with |F Δ G| <= C·l
  for an absolute constant C. Sharp up to C.
hypotheses: F ⊆ Q_n, edge boundary = total influence; near-minimal boundary.
holds-here: yes as a statement about edge-near-minimal sets; near-minimal edge
  boundary = low average internal degree, not low max degree D(S).
status: asserted-by-source (Ellis–Keller–Lifshitz 2018, read via read_sources;
  primary).
bearing: sharp edge-isoperimetric stability; confirms that edge-boundary
  structure controls averages, not the max internal degree of the +1 excess;
  also flags that coordinate-induction here needs codimension-2, relevant to
  the induction method debate.
falsifies: an F with boundary excess l whose distance to every extremal set
  exceeds C·l, or a boundary-minimal F far from every initial segment.
anchor: https://doi.org/10.19086/da.3668
```
