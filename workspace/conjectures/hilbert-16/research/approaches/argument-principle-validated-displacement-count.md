# argument-principle-validated-displacement-count

```approach
name: argument-principle-validated-displacement-count
idea: Complexify a transversal return map away from polycycle singularities and count zeros of the holomorphic displacement by winding number on compact boundaries, with parameter subdivision and Rouché certificates; retain the result as a delta-away restricted bound.
status: adopted
first-step: Define one explicit quadratic analytic family, rational transversal, compact complex rectangle K at distance δ>0 from every singularity and separatrix endpoint, and displacement d=R−id. Implement interval-complex arithmetic for d on ∂K and certify 0∉d(∂K) uniformly on a finite rational parameter subdivision; compute the winding number and cross-check it against a direct subdivision/Rouché count. State the restricted theorem in Lean as a cited/conditional argument-principle certificate, with the exact δ, parameter box, boundary margin, precision, and remaining gap (δ→0) recorded.
precedent: https://doi.org/10.48550/arxiv.1106.0857 (Gavrilov, On the number of limit cycles which appear by perturbation of two-saddle cycles); https://doi.org/10.1016/j.anihpc.2013.12.001 (Gavrilov–Iliev, perturbations of quadratic Hamiltonian two-saddle cycles); https://doi.org/10.1090/mosc/248 (Roussarie–Rousseau, finite cyclicity of center graphics); claim:h16-drr-121-graphics; claim:drr-rr-boundary-only-for-3-graphics
survives: A holomorphic displacement on a compact complex transversal domain whose boundary avoids singularities can be zero-counted by the argument principle; this gives a bound only for cycles represented in that domain and uniformly certified over a finite parameter subdivision.
killed-by: none for the restricted statement; the proposed removal of delta is not supported and would require uniform complex domains as the polycycle is approached.
```

## Literature assessment

The reformulation is **complex-analytic argument-principle zero counting of Poincare/holonomy maps**, not Nevanlinna theory. Gavrilov's two-saddle paper explicitly proves finite cyclicity for analytic finite-parameter deformations by evaluating zeros of the return map in complex domains and states that it avoids Dulac asymptotic expansions. Its hypotheses are analyticity, a specified two-saddle cycle, finite-parameter analytic deformation, and a constructed complex domain with controlled boundary. These do not hold automatically for the open non-hyperbolic DRR graphics, especially as the transversal approaches the graphic; they do hold by assumption on a compact domain at positive distance from all singularities, provided joint holomorphicity and a nonvanishing boundary displacement certificate are actually established.

Roussarie–Rousseau 2015 applies displacement-map and Dulac-map methods to quadratic center graphics, but its results do not supply the proposed general delta-uniform complex domain for the unresolved full graphics. Thus this is a real precedent for the restricted route, not a closure of H(2). It buys a certified bound for a fixed compact annular/transversal region and parameter box, with analyticity explicit at the holomorphic continuation and boundary nonvanishing steps. It does not buy a bound on cycles accumulating at the polycycle.

Tests: smooth test passes only because joint holomorphicity/analytic continuation is load-bearing; it fails for merely smooth fields. Lower-bound test is irrelevant to an upper bound restricted away from the graphic, but any claimed global numerical bound must be checked against H(2)>=4 and H(3)>=13. Slow-fast test is an obstruction to removing delta: singular limits can move return domains and singularities onto the boundary, invalidating a fixed complex contour.

Evidence is sourced from search summaries and existing held claims; the exact contour hypotheses in Gavrilov must be read from the full paper before a theorem is quoted verbatim.
