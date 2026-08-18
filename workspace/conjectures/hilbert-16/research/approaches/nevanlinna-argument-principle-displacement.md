# Nevanlinna argument-principle displacement

```approach
slug: nevanlinna-argument-principle-displacement
status: refuted
idea: Complexify the displacement to a holomorphic germ on CP² and bound its zero count by Nevanlinna theory
mechanism: The field complexifies to a holomorphic foliation; the displacement along a transversal satisfies a first-order ODE with polynomial-in-displacement coefficients; Nevanlinna's logarithmic-derivative lemma converts a growth bound (uniform over the parameter box, from bounded coefficient degree) into a uniform zero bound via the argument principle.
killed-by: No theorem found that gives a parameter-uniform Nevanlinna characteristic/growth bound for complexified return germs of the relevant non-hyperbolic polycycles; the proposed first-order polynomial ODE for displacement is not established, and existing complex zero-counting results require hypotheses (constructible orbits, algebraic trajectory/hypersurface intersections, or special polycycles) absent here.
precedent: https://ar5iv.labs.arxiv.org/html/1510.00120 ; https://arxiv.org/abs/1106.0857 ; https://doi.org/10.1090/bull/2002-39-03 ; claims: h16-drr-121-graphics, h16-dulac-finiteness-theorem
```

## Literature assessment

The proposed reformulation would be called a **Nevanlinna/complex-analytic zero-counting approach to holonomy or displacement**, but I found no paper applying it to the open DRR graphics. The closest relevant complex result is Gavrilov's work on two-saddle cycles (arXiv:1106.0857), which proves finite cyclicity in that special analytic setting by complex-domain analysis and the argument principle, using detailed Dulac-map geometry. It is not a Nevanlinna theorem and does not cover arbitrary degenerate graphics.

Ilyashenko's finiteness literature establishes finiteness for individual polynomial fields and analyzes monodromy asymptotics, but its cited mechanism is accelerosummation/quasianalytic asymptotics, not a uniform Nevanlinna characteristic estimate for a parameter family. The complex zero-counting paper *Zero counting and invariant sets of differential equations* (arXiv:1510.00120) proves polynomial-in-degree intersection bounds under the strong hypothesis of **constructible orbits** of an algebraic complex vector field. A generic complexified polynomial foliation in CP², and especially a local return germ near a non-hyperbolic polycycle, is not shown to have constructible orbits in that sense.

**Hypotheses here:** polynomial coefficients do provide a complexified algebraic foliation. They do not provide (i) a holomorphic single-valued displacement on a uniform complex domain, (ii) a proved first-order ODE whose coefficients are polynomial in displacement, (iii) a uniform characteristic/growth estimate over the compactified parameter space, or (iv) constructibility of the relevant trajectories. Complexification also introduces separatrix, monodromy, and domain singularities rather than removing them.

**Application to this problem:** no located source applies Nevanlinna theory to the DRR finite-cyclicity program or to I₆b¹, H₁₃³, DI₂b, or H₁₄³. Gavrilov's two-saddle argument-principle result is genuine precedent for the broad complex-analytic philosophy, but its hypotheses and geometry are substantially narrower.

**What it would buy if the missing theorem existed:** a characteristic bound plus Jensen/argument-principle control could convert growth into a uniform zero bound and would explicitly use holomorphic/algebraic structure, passing the smooth test. At present the growth estimate is not a lemma available from bounded polynomial degree, so this candidate is refuted as a supported route, not as a logical impossibility.

## Three tests

1. Smooth test: potentially passes only after a genuine complex extension and growth estimate; complexification is not itself the estimate.
2. Uniformity: completely missing; pointwise Nevanlinna bounds would not imply a family-uniform bound.
3. Counterexample boundary: the open non-hyperbolic DRR graphics are outside the special two-saddle and constructible-orbit hypotheses found.
```