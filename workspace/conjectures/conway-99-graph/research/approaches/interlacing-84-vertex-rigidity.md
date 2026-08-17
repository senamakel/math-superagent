# Approach: interlacing rigidity of the 84-vertex second subconstituent

```approach
idea: The only free part of a putative srg(99,14,1,2) is the induced subgraph H
  on the 84 distance-2 vertices of a fixed vertex 0. Cauchy interlacing applied
  to this 84x84 principal submatrix of the 99x99 adjacency matrix FORCES an
  exact count of eigenvalues of H equal to 3 and to -4. This spectral rigidity
  combines with 12-regularity (trace 0) and the mu=2 outer-pair adjacency rule
  (paired with the pair-labeling approach) into a heavily over-determined
  spectral+combinatorial object on 84 vertices -- an a=7/14-specific lever that
  the whole-graph eigenvalue routes (refuted on arrival because 9 and 243 pass
  them) never touch, because it lives in the induced-subgraph interlacing, not
  in the whole spectrum.
mechanism: Let G=srg(99,14,1,2) with spectrum alpha: 14^1, 3^54, -4^44 (1-indexed
  alpha_1=14, alpha_2..55=3, alpha_56..99=-4). Fix 0; N(0)=7K2 (c5); the 84
  distance-2 vertices form a principal 84x84 submatrix H (remove 0 and its 14
  neighbours: n-m = 15). Every outer vertex has degree 2 into N(0) (mu=2 and the
  degree count), so H is 12-regular on 84 vertices, hence trace(H)=0 and
  sum of eigenvalues = 0, with Perron eigenvalue 12. Cauchy interlacing,
  beta_i in [alpha_{i+15}, alpha_i], gives EXACTLY (hand-derived, exact):
    beta_1  : free band [3,14]         (the Perron eigenvalue = 12)
    beta_2..40 : forced = 3            (39 eigenvalues exactly equal to 3)
    beta_41..55: free band [-4,3]      (15 eigenvalues)
    beta_56..84: forced = -4           (29 eigenvalues exactly equal to -4)
  Trace: 12 + 39*3 + (sum of 15 in [-4,3]) + 29*(-4) = 0
       => the 15 banded eigenvalues must SUM to -13, each in [-4,3].
  So a putative Conway graph forces an 84-vertex 12-regular graph H whose
  spectrum is 12^1, 3^39, then 15 values in [-4,3] summing to -13, then -4^29.
  This is a rigid spectrum+degree object. Combined with the mu=2/lambda=1 rule
  on the pair-labeling of the 84 vertices (K14-minus-a-matching pairs), the
  graph H is determined far more tightly than a free 12-regular graph on 84
  vertices, and a nauty/sat check on that over-determined object is a bounded
  finite question (problem.md result class #4) rather than a 99-vertex search.
  The admissibility gate (must fail on both controls in a controlled way):
  the SAME interlacing framework applies to rook(3) (n=9, spectrum
  4^1,1^4,-2^4, outer m=4) and BvLS (n=243, spectrum 22^1,4^?, -5^?, outer
  m=220). The framework is universal; what differs is the numeric content -- at
  99 the forced triple/quadruple counts (39,+ banded sum -13, 29) live at
  a=7 (sqrt(4k-7)=7). The argument must state why the forced spectrum 12^1,
  3^39, [-4,3]^15 (sum -13), -4^29 on 84 vertices is realisable at neither 4
  nor 220 outer vertices for their controls, or fail.
first-step: (exact, hand-verified above, then machine-check) (1) Restate the
  forced interlacing counts in exact integer arithmetic and verify trace=0 with
  the banded sum -13. (2) Build the forced-spectrum+degree constraint as the
  SAT/CP-SAT target: find an 84x84 adjacency matrix of a 12-regular graph whose
  spectrum matches 12^1, 3^39, [-4,3]^15 (sum -13), -4^29 AND satisfies the
  mu=2 outer-pair rule. (3) Run the SAME encoder on the controls' outer
  subgraphs and require it to FIND the true C4 (rook) and the true 220-vertex
  outer graph (BvLS) before believing any empty result at 99; record that
  admissibility gate.
status: refuted
killed-by: automated necessary-interlacing condition, satisfied by the true outer
  subgraph by construction, hence no 99-vs-controls separating power on its own.
```

## Decision (inventor, converge round)

REFUTED as a standalone line of attack, but NOT because the arithmetic is wrong
(it is exact and hand-verified: 12 + 39·3 + Σ₁₅ + 29·(−4) = 0 ⟹ Σ₁₅ = −13). It
is refuted because the interlacing rigidity is a *necessary condition that any
true outer subgraph automatically satisfies* — if H came from an srg it would
interlace by construction, so the forced counts (39 threes, 29 minus-fours,
banded sum −13) are not themselves an obstruction at 99; they cannot separate
99 from the controls (rook/BvLS outer subgraphs satisfy their own interlacing
trivially). A necessary condition that holds on every candidate is a
specification for a search, not a proof.

It is therefore absorbed as a constraint inside the adopted
pair-labeling-84-vertex CP-SAT (12-regular ⇒ trace 0; the forced eigenvalue
counts and banded sum −13 tighten the SAT target), where it is useful, rather
than pursued as a standalone nonexistence route.

killed-by: automated necessary-interlacing condition, satisfied by the true
  outer subgraph by construction; no 99-vs-controls separating power on its own.
but the INTERLACING rigidity (exactly 39 threes, 29 minus-fours, banded sum -13
on the 84-vertex free part) is a FALSE statement-at-99 for the whole graph
(eigenvalue routes died because 9 and 243 pass the whole-graph spectrum) and
here it is a first genuinely induced-subgraph spectral statement with 84-vertex
content. Even if the search shows satisfiability (no contraction), that pins
the honest 84-vertex frontier the 99-vertex orbit-matrix route could not reach,
and the interlacing arithmetic is exact and checkable. The distinct object from
pair-labeling-84-vertex (combinatorial pair-rule) is that this one is purely
spectral rigidity; the two compose naturally.
