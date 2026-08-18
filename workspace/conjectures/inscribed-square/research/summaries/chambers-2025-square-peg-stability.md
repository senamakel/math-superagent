# On the Square Peg Problem (Chambers 2025)

**Source:** Gregory R. Chambers, Discrete & Computational Geometry 73 (2025), 1144–1153  
**URL:** https://doi.org/10.1007/s00454-025-00720-x  
**Full text:** `research/sources/chambers-2025-square-peg-stability.full.md`

## What it establishes

A **stability/perturbation result**: If a Jordan curve γ is C⁰-close to a C² Jordan curve β, then γ inscribes a square of positive side length.

**Precise statement:** Let κ > 0 be the maximum unsigned curvature of β, and suppose there exists a continuous function f from the image of β to the image of γ such that |f(β(s)) − γ(s)| < 1/(10κ) for all s ∈ S¹, and f∘β is homotopic to γ inside the image of γ. Then γ contains an inscribed square of positive sidelength.

**Method:** The proof works via the space M₂(γ) of inscribed squares (a 1-dimensional manifold), studying its boundary behavior under the isotopy from β to γ. Uses Schnirelman's odd-count theorem for C² curves as its starting point, then tracks how the odd number of squares persists under sufficiently small perturbations.

## Relevance to this run

This is a new (2025) result that extends the inscribed-square guarantee from C² curves to a C⁰-neighborhood of C² curves — a genuinely larger class. However, the neighborhood bound depends on curvature (1/(10κ)), so as the approximating C² curve becomes more oscillatory, the admissible neighborhood shrinks. The result does **not** cover general continuous curves far from any C² curve (e.g., nowhere-differentiable fractal curves). It does, however, provide a **quantitative stability radius** around smooth curves, which could be useful in approximation arguments when the approximand is known to be C⁰-close to a curve with bounded curvature.

**Key limitation:** The closeness condition involves a *homotopy* inside the image of γ, essentially requiring that the perturbed curve is ambient isotopic to a C² curve within a controlled tube. This is a strong condition not satisfied by arbitrary continuous curves.

## Claims

```claim
id: chambers2025-stability-near-C2
statement: If a Jordan curve γ is C⁰-close to a C² Jordan curve β — specifically, if κ > 0 is the maximum unsigned curvature of β and there is a continuous f from the image of β to the image of γ with |f(β(s)) − γ(s)| < 1/(10κ) for all s, and f∘β is homotopic to γ inside the image of γ — then γ contains an inscribed square of positive side length.
status: asserted-by-source
evidence: Chambers 2025, Discrete & Computational Geometry 73, 1144–1153, DOI 10.1007/s00454-025-00720-x
holds-here: yes — extends the inscribed-square guarantee to a C⁰-neighborhood of C² curves; the neighborhood radius depends on curvature, so it does not cover curves far from any C² curve
falsifies: a published counterexample of a Jordan curve C⁰-close to a C² curve within 1/(10κ) with no inscribed square
```
