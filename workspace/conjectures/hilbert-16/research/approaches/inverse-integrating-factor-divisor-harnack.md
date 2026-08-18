# Inverse integrating factor + Harnack oval bound

```approach
idea: Change the object carrying the cyclicity from the displacement function
     (a 1-D germ on a transversal) to the INVERSE INTEGRATING FACTOR V — the scalar
     function on the phase plane satisfying X(V) = V·div(X), whose zero set contains
     every limit cycle. For an analytic focus, cyclicity is the ORDER of the formal
     inverse integrating factor at the singularity, read off the Bautin ideal this
     run has already computed exactly; for a family with an explicitly verified
     polynomial/algebraic IIF, the number of limit cycles in a region is bounded by
     the number of ovals of the real algebraic curve {V = 0} lying in that region
     (Giacomini–Llibre–Viano), and that oval count is bounded by Harnack's theorem on
     the degree of V. The change of representation is the point: the displacement
     lives on a transversal and is a transcendental germ; the inverse integrating
     factor lives on the plane and, for a polynomial unfolding of a polynomial field,
     is a FORMAL POWER SERIES whose order and Newton polygon are algebraic invariants
     of the Bautin ideal — a finite, kernel-checkable object, not an asymptotic
     expansion. This is distinct from the Darboux-integrability proposal, which uses
     Darboux COFACTORS for nonexistence certificates (a first integral, not the
     inverse integrating factor; nonexistence, not counting).

mechanism: Why this problem's structure suits it. (1) The inverse integrating
     factor is the established instrument for BOTH existence and counting of limit
     cycles: Giacomini–Llibre–Viano prove limit cycles are contained in {V = 0};
     García–Llibre–Maza (JDE 2013) and Gasull–Giacomini give the order-of-V bound on
     focus cyclicity (vanishing multiplicity equals cyclicity in the nondegenerate
     focus case, lower bound in several degenerate/nilpotent cases under their
     monodromy, analyticity and non-flatness hypotheses). (2) It connects the two
     halves of H16 the workspace keeps deliberately separate: the oval count of
     {V = 0} is a Part-I (Harnack/Gudkov) question, and the order of V at a focus is
     a Part-II (Bautin-ideal) question. No closed approach makes this connection.
     (3) Test 1 (smooth) is met at the right place: V is defined by the FIRST-ORDER
     PDE X(V)=V·div(X), which has a FORMAL power-series solution for an analytic
     field but NOT for a generic C^∞ field (the formal solution need not converge
     nor be Borel-summable without analyticity); the Harnack bound on {V=0} requires
     V to be algebraic, which uses algebraicity of the coefficients. A smooth field
     has no algebraic V. (4) The finite core is already in hand: the run has
     computed the Bautin ideal ⟨L4,L6,L8⟩ exactly (code/out/membership.captured.txt)
     and the focal values through degree 14; the order of the formal inverse
     integrating factor at a focus is the index of the first nonzero focal value,
     which is an ideal-membership / sign-condition computation Lean can close (the
     cofactor-certificate pattern already in BautinRecurrence.lean).

     RESEARCH GROUNDING (narrowed). The sourced theorem is: if a C^1 planar field
     has an IIF V on U, every limit cycle contained in U lies in V^{-1}(0); for
     analytic foci the vanishing multiplicity of V along the blown-up reference
     cycle equals cyclicity in the nondegenerate case and gives a lower bound in the
     degenerate/nilpotent cases. Harnack gives an oval bound for a real irreducible
     algebraic curve of degree d (with singularity corrections), but ONLY after
     proving V is a polynomial/algebraic curve of known degree and that all relevant
     cycles lie on its ovals. The current H16 target has NO theorem producing one
     global polynomial IIF for the full quadratic unfolding or the open DRR
     graphics; a formal power-series IIF and Bautin ideal membership do NOT imply
     convergence, algebraicity, a degree bound, or global coverage. THEREFORE the
     unrestricted global Harnack cap is NOT claimed; what is adopted is the LOCAL
     IIF-order ⇒ cyclicity theorem, plus the global Harnack cap ONLY on a named
     family where a polynomial/algebraic IIF is explicitly verified.

status: adopted

first-step: (a) VALIDATE the local IIF-order theorem against the literature
     boundary before trusting it on anything new. For the quadratic focus family
     already computed by this run (u' = −v + a1u² + a2uv + a3v², v' = u + b1u² +
     b2uv + b3v²), compute the FORMAL INVERSE INTEGRATING FACTOR V = Σ v_k as a
     power series over Q[u,v] by solving X(V) = V·div(X) order by order (a linear
     recurrence for the homogeneous components v_k), and verify that the order of
     V at the origin — the first k with v_k ≠ 0 — equals the index of the first
     nonzero Lyapunov quantity, reproducing Bautin's M(2)=3 (V has order 4, since
     L1=L2=L3=0 and L4≠0 force v_4≠0). State the order-of-V ⇒ cyclicity claim in
     Lean as a theorem over the Bautin ideal (the ideal-membership certificates
     already exist in BautinRecurrence.lean).

     (b) THE GENUINELY NEW STEP, after validation: for ONE open center graphic
     whose unperturbed field is Darboux-integrable (so V_0 is explicit and
     rational/algebraic), compute the perturbed formal V to finite order and read
     the cyclicity off the Newton polygon of V — the finite algebraic core Lean can
     finish, with the Harnack oval bound as the global cap ONLY if V is proved
     polynomial/algebraic of known degree on the relevant domain. The run already
     holds Darboux cofactor identities for the Lu H^3_14 family (X(L)=(x+dy)L,
     X(F)=(2Bx+dy)F, kernel-checked) — a Darboux-integrable unperturbed field gives
     an explicit algebraic V_0, and the perturbation's formal V is computed by the
     same recurrence. Do NOT infer the global Harnack cap from the formal Bautin
     core alone; prove degree and domain first.

killed-by: (none — adopted). The original unrestricted claim that formal IIF order
     plus Harnack bounds H16.2 was refuted by research (no global polynomial-IIF
     existence or uniform degree bound for the open DRR families); the surviving
     restriction — local IIF vanishing multiplicity for analytic foci, global
     Harnack only on a verified polynomial/algebraic IIF — is what is adopted.

precedent:
- https://doi.org/10.1016/j.jde.2013.07.046 (García–Llibre–Maza, cyclicity of a simple focus via vanishing multiplicity of the IIF)
- https://doi.org/10.1007/s10884-011-9209-2 (García–Giacomini–Grau, generalized Hopf bifurcation via IIF)
- https://doi.org/10.1016/j.jde.2011.06.008 (Zhang, Harnack and algebraic limit cycles)
- https://doi.org/10.1007/s12346-023-00746-7 (Gasull–Giacomini, invariant algebraic curves and IIF)
- claim:drr-lu-claims-h14-3
- claim:lu-finite-core-partially-verified
- claim:bautin-chart-membership-l8-l10-l12
- claim:h16-drr-121-graphics
```
