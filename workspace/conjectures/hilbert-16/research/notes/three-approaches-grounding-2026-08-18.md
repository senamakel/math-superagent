# Literature grounding pass — three proposed approaches (2026-08-18)

## 1. Inverse integrating factor + Harnack

**Verdict: narrowed, not grounded in its unrestricted form.**

The named theory is the inverse-integrating-factor (IIF) method. For a planar field `X=(P,Q)`, an IIF satisfies `X(V)=V div(X)`. The sourced theorem is: if `V` is a C1 IIF on `U`, every limit cycle contained in `U` lies in `{V=0}` (Giacomini–Llibre–Viano, as stated in Zhang 2011). For analytic focus problems, García–Llibre–Maza (2013) and García–Giacomini–Grau (2011) relate the vanishing multiplicity of an IIF in generalized polar coordinates to focus cyclicity: equality in the nondegenerate case and a lower bound in the degenerate/nilpotent cases, subject to analyticity, monodromy, and non-flatness hypotheses.

Harnack's theorem bounds the number of ovals of a real irreducible algebraic curve of degree `d` (with singularity corrections; Zhang 2011). It applies only if `V` is proved to be a polynomial/algebraic function of known degree and the cycles lie on the relevant ovals. A formal/local IIF obtained from the Bautin recurrence does not imply convergence, algebraicity, degree control, or global coverage. No source found supplies a global polynomial IIF for the open DRR graphics or the full quadratic unfolding. Thus the local IIF/Bautin restriction survives, but the proposed global Harnack cap is not a route to H16.2.

Sources: https://doi.org/10.1016/j.jde.2013.07.046; https://doi.org/10.1007/s10884-011-9209-2; https://doi.org/10.1016/j.jde.2011.06.008; https://doi.org/10.1007/s12346-023-00746-7. Claims: `drr-lu-claims-h14-3`, `lu-finite-core-partially-verified`.

## 2. Degenerate Hamiltonian irregular Picard–Fuchs + Borel–Laplace

**Verdict: refuted as stated; tangential restriction survives.**

The relevant established theory is the Petrov-module/Brieskorn-lattice and Picard–Fuchs theory. Novikov–Yakovenko construct finite-dimensional meromorphic/Pfaffian Picard–Fuchs systems for Abelian integrals of polynomial Hamiltonians; the bounded Brieskorn-lattice work treats semiquasihomogeneous (including degenerate) Hamiltonians and gives effective coefficient bounds. Gavrilov establishes finite Petrov modules in suitable semiquasihomogeneous settings. These results support effective zero bounds for Abelian integrals under their explicit domain and coefficient hypotheses.

They do **not** establish the proposed stronger claims: that the relevant Borel transforms are rational, that the open DRR Hamiltonians have the asserted irregular system with rational Borel data, or that the nonlinear four-Dulac displacement equals a finite collection of such solutions. The target is a nonlinear return-map composition, not merely a first variation/Melnikov Abelian integral. Existing library claims explicitly say GMV/Abelian criteria do not cover the full I6b four-Dulac graphic.

Sources: https://ar5iv.labs.arxiv.org/html/math/0110126; https://ar5iv.labs.arxiv.org/html/math/0201114; https://www.sciencedirect.com/science/article/pii/S0007449799800049; https://doi.org/10.1006/jdeq.2000.3967. Claims: `h16-bny-abelian-bound`, `h16-bd-abelian-linear-in-m`, `gmv-ect-does-not-cover-i6b-four-dulac`, `i6b-four-second-type-full-graphic-not-covered`.

## 3. Artin–Mazur zeta / finite-type return map

**Verdict: refuted as stated.**

The Artin–Mazur zeta function is `ζ_f(z)=exp(Σ N_n z^n/n)`, where `N_n` counts isolated fixed points of `f^n`, assuming each is finite. The Artin–Mazur theorem, as summarized by Smale, gives for a dense set of diffeomorphisms of a compact manifold an exponential bound on `N_n`, hence positive radius of convergence. It does not say that the zeta function is rational. Rationality is established in special global settings such as Axiom-A/no-cycle systems, shifts of finite type, and toral endomorphisms, using symbolic or homological structure.

No theorem found applies rational zeta or finite-type dynamics to a one-dimensional analytic Poincare/Dulac germ at a nonhyperbolic polycycle. The proposed assertion that rationality is equivalent to finite type in this generality is not an Artin–Mazur theorem; nor does numerator degree generally bound `N_1`. Finite determinacy of an analytic germ does not imply finite-type dynamics, and no closure-under-composition theorem for second-type Dulac maps was found. A zeta method could be useful only after independently constructing a compact hyperbolic/basic-set model, which excludes the target nonhyperbolic DRR regime.

Sources: https://doi.org/10.48550/arxiv.2405.10560; https://doi.org/10.1090/s0002-9904-1967-11798-1; https://doi.org/10.1007/s00605-009-0118-y; https://www.cambridge.org/core/journals/ergodic-theory-and-dynamical-systems/article/open-index-pairs-the-fixed-point-index-and-rationality-of-zeta-functions/05352D0184B248E2B401ED2F875C026A. Claims: `h16-drr-121-graphics`, `h16-dulac-finiteness-theorem`.

The approach files were updated with these verdicts and `killed-by`/restriction details. The workspace index refresh was blocked because research is Cognee-catalogued; no index was created.
