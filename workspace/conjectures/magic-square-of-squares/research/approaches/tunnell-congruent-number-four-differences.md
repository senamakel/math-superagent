```approach
id: tunnell-congruent-number-four-differences
idea: Apply Tunnell's theorem (1983) on congruent numbers to the FOUR
       differences u, v, u+v, u−v simultaneously, using the fact that each
       must be a congruent number (since each corresponds to a three-term
       AP of squares through the centre e²).  Tunnell's criterion
       characterizes congruent numbers via representation counts of specific
       quadratic forms.  The four linked differences must simultaneously
       satisfy Tunnell's representation-count equalities, and the additive
       constraints u+v and u−v relate the quadratic-form representations
       of the individual differences.  Using the convolution structure of
       theta-series coefficients (the Shimura lift / Waldspurger formula)
       that governs these representation counts, the additive relations
       force a specific identity among modular forms of half-integral weight
       whose Fourier coefficients are the representation counts.  If the
       identity cannot hold for the required coefficient triples, the four
       differences cannot all be congruent numbers simultaneously — and
       hence no MSS.  This is distinct from the refuted
       Hecke-character-product-L approach (which was superseded by
       resolve-magic-surface-birational and targeted L-functions at s=1,
       not Tunnell coefficients) and from the refuted 2-Selmer approach
       (which was subsumed by Bremner II's K3 NS data).  Tunnell's theorem
       operates at the level of explicit quadratic-form representations,
       which carry additional number-theoretic constraints (class numbers,
       genus theory) that the Selmer-group approach does not capture.

mechanism: Tunnell (Annals of Math. 118, 1983, Theorem 1): if n is a
  squarefree congruent number, then the number of integer solutions to
    2x² + y² + 8z² = n   (for n odd)
  and
    2x² + y² + 32z² = n  (for n odd)
  satisfy A_n = 2C_n, where A_n counts solutions to the first form and C_n
  to the second (and similarly for even n with forms 4x²+y²+8z²=n/2 etc.).
  The converse — if A_n = 2C_n, then n is congruent — is conditional on
  BSD, but the forward direction is unconditional.  For the MSS, each
  difference d ∈ {u, v, u+v, u−v} is a congruent number (since e², e²±d
  are all squares — the AP condition).  After removing square factors from
  d, Tunnell's criterion gives four unconditional equalities among the
  representation counts of quadratic forms in 3 variables.

  The key structural fact: the four differences are NOT independent —
  they satisfy (u+v) + (u−v) = 2u and (u+v) − (u−v) = 2v.  Each
  difference, after stripping square factors, has its Tunnell
  representations tied to the theta series of the corresponding ternary
  quadratic form.  The additive relations among the differences correspond
  to convolution relations among the theta-series coefficients via the
  Shimura correspondence (the Waldspurger formula: the d-th Fourier
  coefficient of a weight-3/2 modular form is, up to a nonzero factor,
  the central L-value L(E_d, 1) of the quadratic twist).  Since Tunnell's
  representation counts are essentially the same as the d-th coefficient
  of specific weight-3/2 forms, the additive relations among d force
  congruences among these coefficients modulo squares and modulo the
  Tunnell multiplier (2 for odd squarefree, etc.).

  More concretely: write d_i = s_i² · n_i where n_i is squarefree.  The
  Tunnell condition for n_i is A_{n_i} = 2C_{n_i}.  The outstanding
  question is whether the additive relations u, v, u+v, u−v force the
  squarefree parts n_i into a configuration that violates Tunnell's
  criterion.  For example, if n_{u+v} = n_u + n_v (modulo square factors),
  the representation counts might satisfy an inequality that contradicts
  A = 2C simultaneously for all four.  This is a finite computation up to
  the known search bound, but the structural goal is a PROOF that the
  simultaneous Tunnell equalities are impossible for any four linked
  differences.

  The heavy machinery: the Shimura lift maps weight-3/2 modular forms
  (whose Fourier coefficients ARE Tunnell's representation counts) to
  weight-2 modular forms (which correspond to elliptic curves).  For the
  congruent-number curves E_d: y² = x³−d²x, the d-th Fourier coefficient
  of the weight-3/2 form is — up to nonzero factors — the central value
  L(E_d, 1).  The additive relations among d correspond to additive
  relations among twists, which are controlled by the action of the Hecke
  algebra on the space of half-integral-weight forms.  This is a modular-
  forms approach, not a geometric one, and it uses the specific CM-by-Z[i]
  structure of the congruent-number curves.

  Named mathematics: Tunnell's theorem (1983), the Shimura correspondence
  (1973), the Waldspurger formula (central L-values as squares of
  half-integral-weight Fourier coefficients), ternary quadratic forms and
  their representation counts (genus theory, Siegel mass formula), the
  Hecke algebra on spaces of modular forms of half-integral weight.

first-step: |
  1. **Reproduce Tunnell's criterion numerically for small differences.**
     For a range of small d (up to 10⁶), compute Tunnell's representation
     counts A_d, C_d, and verify the forward direction: if e², e²±d are
     all squares, then after stripping square factors from d, A_{n_d} = 2
     C_{n_d}.  Test on the known differences from Bremner's witness
     (d = 138600 = 2³·3·5²·7·11 → n = 2310, and d = 97104 = 2⁴·3·7·17²
     → n = 357, etc.).  Compute A_n, C_n explicitly and verify the
     Tunnell equality for each.

  2. **Study the additive relations among the Tunnell coefficients.**
     For a candidate MSS centre e², the four differences are u, v, u+v,
     u−v.  For the test case of Bremner's witness (where only TWO of the
     four differences are fully realized as congruent numbers, since only
     two APs are complete), compute the Tunnell coefficients of all four
     differences and observe which equality fails for the unrealized
     differences.  This establishes the "signature" of the 7-square
     near-miss in Tunnell terms.

  3. **Formulate the simultaneous-Tunnell constraint algebraically.**
     The condition that all four differences are congruent numbers is
     equivalent to four Tunnell equalities.  Write the differences as
     u = e²·(m₁/n₁)²·f(p₁,q₁), v = e²·(m₂/n₂)²·f(p₂,q₂), etc., using
     the Φ reduction.  Express the Tunnell representation counts in terms
     of the (p_i, q_i) parameters.  The additive relations u+v, u−v then
     impose equations on the Tunnell coefficients.  Determine whether
     these equations are solvable — a system of Diophantine equations in
     the (p_i, q_i) that may be tractable by classical methods.

  4. **Run against the witness.**  The Bremner witness must survive
     (only two Tunnell equalities hold).  Verify that the simultaneous
     constraint fails exactly as expected — the failure mode for the
     7-square witness must match the theoretical prediction.

status: proposed
precedent: |
  - J.B. Tunnell, "A classical Diophantine problem and modular forms of
    weight 3/2", Invent. Math. 72 (1983) 323–334 — the congruent-number
    criterion via quadratic-form representation counts.  Theorem 1:
    if n is squarefree and congruent, then A_n = 2C_n (unconditional).
  - G. Shimura, "On modular forms of half integral weight", Annals of
    Math. 97 (1973) 440–481 — the Shimura correspondence between
    weight-3/2 and weight-2 modular forms.
  - J.-L. Waldspurger, "Sur les coefficients de Fourier des formes
    modulaires de poids demi-entier", J. Math. Pures Appl. 60 (1981)
    375–484 — the formula relating central L-values to squares of
    half-integral-weight Fourier coefficients.
  - The congruent-number curves E_d: y² = x³−d²x are CM by Z[i].  Their
    L-functions at s=1 are Hecke L-values — this is the modular context
    in which Tunnell's theorem lives.
  - This run's `phi-universal-set` claim: d/e² ∈ Φ for every AP difference,
    and the Φ-reduction gives a parametrisation of the Tunnell-eligible d.
  - NOT the refuted Hecke-character-product-L approach: that approach
    worked at the level of L-functions and product identities among the
    four curves, and was refuted as superseded.  This approach works at
    the level of quadratic-form REPRESENTATION COUNTS (Tunnell's A_n, C_n),
    which carry finer arithmetic information: inequalities, class-number
    constraints, and the explicit ternary-form structure that L-functions
    do not.

speculation: The key unknown is whether the additive relations u, v, u+v, u−v
  impose a solvable constraint on Tunnell's A_n, C_n coefficients.  The
  Tunnell criterion is a necessary condition for congruent numbers — it
  does not by itself force a contradiction, since many n satisfy A_n = 2C_n
  without being congruent (BSD converse is open).  But the FOUR SIMULTANEOUS
  Tunnell equalities with the additive links might be restrictive enough to
  be impossible.  The risk is that the Tunnell coefficients of u, v, u+v, u−v
  are not linked by any known formula (the additive relation is at the level
  of d, while Tunnell coefficients are at the level of the squarefree part
  of d) — the approach fails if no structural link exists.  The first-step
  computation on Bremner's witness tests this: if the Tunnell coefficients
  of u+v are unrelated to those of u and v, the approach is refuted.
killed-by: _none yet_
```