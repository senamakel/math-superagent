# Keevash–Long, "A stability result for the cube edge isoperimetric inequality" (JCTA 2017)

Source URL: https://doi.org/10.1016/j.jcta.2017.11.005
Retrieved via `read_sources` (server-side); direct download blocked by the
network boundary (Elsevier host unreachable from the run).

Paper: Peter Keevash, Eoin Long, *A stability result for the cube edge
isoperimetric inequality*, Journal of Combinatorial Theory, Series A 155
(2017).

## What this source establishes

A quantitative **stability** version of the cube edge-isoperimetric inequality.
Informally: if a subset A of the discrete cube {0,1}^n has edge boundary nearly
minimal for its size, then A is structurally close to an extremal configuration
(a subcube, or a small perturbation of a subcube). The distance from A to the
nearest extremal set is bounded by a function that tends to zero as the excess
edge boundary over the minimum tends to zero. It gives a *quantitative* bound:
how much the edge boundary exceeds the minimum is translated into how far A is
from a subcube.

Technique: isoperimetric stability via compression/monotonicity —
edge boundary is nonincreasing under symmetric-shifting operations — combined
with stability analysis for the cube edge-isoperimetric inequality, building
on the prior edge-isoperimetric and influence/variance frameworks
(Falik–Samorodnitsky; Friedgut–Kalai; KKL). Discrete symmetrization / averaging
arguments convert small boundary excess into structural closeness to a subcube.

## Why it is here

This is a genuine *technique* source extending the classical cube
edge-isoperimetric theorem, and it is the natural companion to the
vertex-isoperimetric stability of Keevash–Long (arXiv:1807.09618) already in
the library. It refines what the edge-isoperimetric half of
`survey-cube-isoperimetric-profile` says, adding a structural/stability
statement: edge-near-minimal sets are close to subcubes.

Relevance to the problem: it concerns sets whose edge *boundary* is near
minimal. Near-minimal edge boundary means near-minimal *total* internal edges
(e(s) ≈ 1/2(|S|·n − |∂S|)), i.e. low *average* internal degree — not low max
degree. It therefore confirms the obstruction: structure theorems for
edge-near-minimal sets control an average quantity and say nothing about a
maximum D(S). The extremal shape it describes (subcube-like) is consistent with
the parity-class scaffold of the d=0 line, but the +1-vertex excess in this
problem is exactly the regime this stability does not govern.

## Claim block

```claim
id: keevash-long-edge-isoperimetric-stability
statement: If A ⊆ {0,1}^n has edge boundary within ε of the minimum for its
  size, then A is within a quantitative distance (→ 0 as ε → 0) of a subcube
  or small subcube perturbation. Near-minimal edge boundary forces structural
  closeness to a subcube.
hypotheses: A ⊆ Q_n, |∂_e(A)| near minimal for |A|; compression/symmetrisation
  arguments over the cube.
holds-here: yes as a statement about edge-near-minimal sets; but near-minimal
  edge boundary = low average internal degree, not low max degree D(S).
status: asserted-by-source (Keevash–Long 2017, read via read_sources; primary).
bearing: structural stability of edge-isoperimetric extremal sets;
  confirms that edge-profile structure controls only average quantities.
falsifies: an A with near-minimal edge boundary that is far from every subcube
  beyond the stated bound.
anchor: https://doi.org/10.1016/j.jcta.2017.11.005
```
