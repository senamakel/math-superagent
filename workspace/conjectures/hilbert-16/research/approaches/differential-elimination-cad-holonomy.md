# differential-elimination-cad-holonomy

```approach
name: differential-elimination-cad-holonomy
idea: Encode the polynomial flow and a restricted observation/return construction by a differential ideal, eliminate jet variables to obtain an algebraic graph relation, then use CAD to count real intersections with the diagonal.
status: refuted
killed-by: As a general attack on the open DRR graphics, differential elimination of the polynomial vector-field jet tower does not imply an algebraic Poincare or holonomy graph; polynomial flows have transcendental return maps, and CAD applies only after an independently proved algebraic first-integral or time-of-flight relation. The viable algebraic-invariant subclass is a restricted future task, not this candidate's proposed general mechanism.
precedent: https://doi.org/10.1145/345542.345571 (Boulier et al., canonical representatives of regular differential ideals); https://doi.org/10.1016/j.tcs.2026.115925 (Simmons–Platzer, differential elimination and algebraic invariants); https://doi.org/10.1007/s12346-023-00746-7 (Gasull–Giacomini, invariant algebraic curves and restricted limit-cycle counts); claim:gasull-giacomini-invariant-curves-restricted-counts; claim:h16-drr-121-graphics
survives: Differential elimination and CAD are legitimate exact tools for restricted algebraic-invariant or algebraic-time-of-flight subclasses, where an algebraic relation for the observed graph is independently proved.
killed-by: The general proposed implication from a polynomial ODE jet tower to an algebraic Poincare/holonomy graph is false as a methodological premise: solutions and return maps of polynomial ODEs are generally transcendental, and no cited theorem supplies such an algebraic relation for the open DRR graphics.
```

## Literature assessment

The named theory is **Ritt–Kolchin differential algebra / differential elimination**, followed by **real algebraic geometry and cylindrical algebraic decomposition**. Differential elimination computes differential consequences and elimination ideals; it does not imply that a solution graph or Poincare map is algebraic. CAD gives a finite decomposition and exact sign/connectedness decisions for semialgebraic sets defined by polynomial equations and inequalities. Its hypotheses therefore hold only after the graph relation F(rho,R,lambda)=0 has been independently established as algebraic and the parameter/observation domain is semialgebraic.

The literature found applications of elimination to polynomial invariants and invariant algebraic curves, and Gasull–Giacomini obtain restricted limit-cycle consequences from invariant algebraic curves. No source found applies Ritt–Kolchin elimination to the nonlinear holonomy of an arbitrary planar polynomial field or to the unresolved DRR graphics. The proposed “jet tower implies algebraic return graph” is precisely the unsupported step. Slow-fast systems are a direct falsifier: their time-of-flight and return maps commonly contain logarithmic/exponential or other transcendental dependence despite polynomial vector fields.

What survives is a narrowed program: choose a family with a proved algebraic first integral, invariant algebraic curve, or algebraic time-of-flight; derive the elimination certificate; then use CAD to count diagonal intersections. This could buy an effective restricted bound and a Lean-friendly finite certificate (ideal membership, resultant, sign conditions). It cannot presently buy a general H(2) result.

Tests: smooth test is met only through algebraicity, but the general proposal does not establish it. Lower-bound test applies to any claimed unrestricted bound. Slow-fast test kills the unrestricted algebraicity premise, while a restricted family must state why slow-fast degeneration is excluded.

The Simmons–Platzer 2026 item is a method reference, not evidence of application to Hilbert 16; its date and relevance should be independently checked before publication-level reliance.
