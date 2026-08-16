# Approach: Hessian covariant / transvectant (refuted)

Proposed: homogenise F(x,y) = y^n f(x/y); the classical theorem (Cayley) that
the Hessian (F,F)_2 ≡ 0 ⟺ F is an n-th power, and the bet that the covariant
algebra forces (F,F)_2 = 0 from the derivative-sharing conditions.

```approach
idea: A homogeneous binary form F(x,y) of degree n is the n-th power of a
      linear form iff its Hessian (second transvectant (F,F)_2) vanishes
      identically (Cayley; Kung–Rota exposition). CA is the statement that
      F(x,y) = y^n f(x/y) sharing a root with each derivative forces F an
      n-th power; re-express each derivative-sharing condition as a
      transvectant identity and use the covariant algebra to force (F,F)_2 = 0.
mechanism: The i-th Hasse derivative of f is a contraction/polar of F with a
      linear form, i.e. a transvectant of F; the shared-root condition is the
      vanishing of a covariant at the root point [β_j : 1]. The new object is
      the covariant algebra of F (Hessian and higher self-transvectants with
      their Cayley–Sylvester syzygies). The bet: this covariant structure — not
      the apolar ideal (the reason catalecticant-apolarity died) — is what the
      derivative conditions control, and the "Hessian ≡ 0 ⟺ n-th power" syzygy
      ladder is climbable one shared root at a time.
      Char-p break: the Hessian ⟺ pure-power theorem holds in char 0 / char>n;
      its proof divides by factorials / integrates, so it fails when p | n, and
      for x^{p+1}−x^p the Hessian is not the controlling obstruction.
status: refuted
killed-by: Both the classical theorem and the char-p break are real and
      sourced. (1) The theorem: Abdesselam–Chipalkatti, "On Hilbert covariants",
      Canad. J. Math. 64(5):975-994 (2012), doi:10.4153/cjm-2012-046-1 (also
      arXiv:1010.2358): "the Hessian of F vanishes identically exactly when F
      is the perfect d-th power of a linear form" — this is their Hilbert
      covariant H_{1,d} in the r=1, µ=d case, and they prove its coefficients
      cut out the perfect-power (Hilbert) locus scheme-theoretically. So the
      pure-power direction of the proposal is a true, citable theorem.
      (2) But NO source applies binary-form covariant/transvectant theory to
      the CA derivative-sharing system. The load-bearing bridge — "the
      derivative-sharing conditions force (F,F)_2 = 0" — is this proposal's own
      unproved conjecture. The run already refuted the sibling
      catalecticant-apolarity line for exactly this reason: the apolar ideal of
      a generic binary form is generated in two degrees, so the n−1 derivative
      resultants are not a coordinated ladder of a single covariant sequence.
      Nothing in the covariant-algebra literature changes that: the covariant
      ring is finitely generated, but no theorem of classical invariant theory
      says the n−1 resultants R_i = Res(f, H_i f) control (F,F)_2. The char-p
      break is genuinely located (Hessian theorem fails at p | n; homogenized
      x^{p+1}−x^p over F_p has vanishing Hessian yet is not a pure power,
      consistent with a located factorial/integration failure), satisfying the
      admissibility test, but a located break does not supply the missing
      bridge.
first-step: superseded. The one sourced fact worth keeping — the Hilbert
      covariant H_{1,d} whose vanishing locus is scheme-theoretically the
      perfect-power locus (Abdesselam–Chipalkatti 2012, Scheme Theorem) — is
      already implied by the run's simplest model: pure power ⟺ (F,F)_2 = 0.
      Retaining the full covariant ring adds no inference, exactly as
      catalecticant-apolarity bought nothing.
precedent: abdesselam-chipalkatti-2012, (doi:10.4153/cjm-2012-046-1,,
      arXiv:1010.2358:,, Hessian, ≡, 0, ⟺, perfect, d-th, power,, Hilbert,
      covariant, H_{1,d}, scheme-theoretically);, cayley-kung-rota, (classical,
      exposition);, catalecticant-apolarity, (refuted, sibling,:, apolar, ideal,
      generated, in, two, degrees);, No, source, applies, covariant, /,
      transvectant, theory, to, the, CA, derivative-sharing, system.
```
