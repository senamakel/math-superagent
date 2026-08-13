```approach
id: torsion-coset-ap-forcing
idea: On the Robertson curve E: y² = x(x²−c²), the duplication map [2]: E → E
  has kernel E[2] = {O, (0,0), (c,0), (−c,0)} ≅ (Z/2)².  The MSS condition
  — three points Q₀,Q₁,Q₂ ∈ 2E(Q) with x-coordinates in AP — lifts to a
  condition on their PREIMAGES P_i (where [2]P_i = Q_i).  Each P_i is
  defined only up to a coset of E[2]: for each i, there are four choices of
  P_i differing by 2-torsion.  The AP condition x(Q₀) + x(Q₂) = 2x(Q₁) is
  an algebraic equation in the Q_i; substituting Q_i = [2]P_i gives an
  equation in the P_i that is invariant under independent translations
  P_i ↦ P_i + T_i (T_i ∈ E[2]).  The key claim is that the AP condition,
  expressed in terms of P_i, FORCES the three E[2]-cosets (P_i mod E[2])
  to satisfy a specific linear relation — and this relation may be
  INCOMPATIBLE with P_i ∈ E(Q) unless the Mordell–Weil rank is 0 (or 1).
  This is a FINITE question: E[2] has 4 elements, so there are 4³ = 64
  possible coset assignments; the AP condition selects a subset of these,
  and the existence of rational P_i in those cosets is a 2-descent problem
  whose image in Sel₂(E) × Sel₂(E) × Sel₂(E) is computable.

mechanism: The duplication formula for x-coordinates is:
    x([2]P) = f(x(P)) = (x(P)² + c²)² / (4 x(P) (x(P)² − c²)).
  For fixed x-coordinates x_i = x(P_i), the AP condition is:
    f(x₀) + f(x₂) = 2 f(x₁).
  Multiplying through by denominators gives a polynomial F(x₀,x₁,x₂) = 0
  of total degree 12 in each variable — symmetric under the action of the
  duplication formula's Galois group (which is D₄).

  Now the CRUCIAL structural observation: the duplication map satisfies
    x([2](P+T)) = x([2]P)   for any T ∈ E[2].
  This is because E[2] is exactly the kernel of [2], so [2](P+T) = [2]P
  and the x-coordinate is a function on E/{±1}, not on E.  So the AP
  condition on the Q_i = [2]P_i depends only on P_i modulo {±1} — but
  the RATIONALITY of P_i depends on P_i modulo E[2] (four cosets, not two).

  The 2-descent map: E(Q)/2E(Q) ↪ H¹(G_Q, E[2]) sends a point P to the
  cocycle σ ↦ σ(P̃) − P̃ where P̃ is any preimage of P under [2] (i.e.,
  any P̃ with [2]P̃ = P).  The image is the Selmer group Sel₂(E), which
  sits in the exact sequence:
    0 → E(Q)/2E(Q) → Sel₂(E) → Ш(E/Q)[2] → 0.

  For three points Q₀,Q₁,Q₂ ∈ 2E(Q), their classes [Q_i] ∈ E(Q)/2E(Q)
  are TRIVIAL (they are in 2E(Q)).  But their preimages P_i ARE the
  witnesses to this triviality: [2]P_i = Q_i means P_i ≡ 0 mod 2E(Q) for
  the purpose of the descent, but the coset of P_i modulo E[2] is what
  determines the specific P_i.

  Here is the torsion-coset forcing argument, laid out explicitly:
  (a) For each MSS, the three Q_i lie in 2E(Q), so there exist P_i ∈ E(Q)
      with [2]P_i = Q_i.
  (b) The AP condition F(x(P₀), x(P₁), x(P₂)) = 0, where F is the
      polynomial derived from f(x₀)+f(x₂)−2f(x₁).
  (c) Replace each x(P_i) by the Weierstrass ℘-function: x(P_i) = ℘(z_i)
      where z_i ∈ C/Λ is the elliptic logarithm of P_i.  The duplication
      formula is x([2]P) = ℘(2z) = f(℘(z)).
  (d) The AP equation ℘(2z₀) + ℘(2z₂) − 2℘(2z₁) = 0 is a known identity
      on the Weierstrass ℘-function.  Using the addition formula:
        ℘(2u) + ℘(2v) = (1/4)(℘'(u)²℘'(v)²)/(℘(u)−℘(v))² − ℘(u) − ℘(v)
      (with caveats), the AP condition simplifies when expressed directly
      in the P_i rather than the Q_i.
  (e) The SIMPLIFIED IDENTITY: On E: y² = x(x²−c²), the duplication
      x-coordinate satisfies:
        x(2P) = (x(P)² + c²)² / (4y(P)²).
      Using y(P)² = x(P)(x(P)²−c²), this becomes
        x(2P) = (x²+c²)² / (4x(x²−c²)).
      The AP condition x(2P₀) + x(2P₂) = 2x(2P₁) is thus:
        (x₀²+c²)²/(4x₀(x₀²−c²)) + (x₂²+c²)²/(4x₂(x₂²−c²)) = 2(x₁²+c²)²/(4x₁(x₁²−c²)).

  Now substitute x_i = ℘(z_i), y_i = ℘'(z_i)/2.  The duplication formula
  for ℘ gives ℘(2z) = −2℘(z) + (1/4)(℘''(z)/℘'(z))².  But on a curve
  with a = −c², b = 0, we have ℘''(z) = 6℘(z)² + 2a = 6℘(z)² − 2c².
  The AP equation ℘(2z₀) + ℘(2z₂) − 2℘(2z₁) = 0 becomes an equation in
  ℘(z_i) and ℘'(z_i).

  The point: write this equation in terms of the GROUP LAW on E itself.
  The equation ℘(2z₀) + ℘(2z₂) = 2℘(2z₁) is NOT a group-law identity
  — it's an x-coordinate condition.  But using the duplication and addition
  formulas, it can be rewritten as a condition linking the points P_i and
  their 2-torsion translates.

  Concretely: define the rational map
    Φ: E × E × E → A¹
    (P₀, P₁, P₂) ↦ x([2]P₀) + x([2]P₂) − 2x([2]P₁).
  This map factors through E³/(E[2]³) because [2] kills E[2].  The
  equation Φ = 0 defines a hypersurface in E³/(E[2]³).  Its rational
  points correspond to MSS configurations up to 2-torsion choices.

  The 64 cosets (E[2]³) act on this hypersurface.  The question: which
  cosets contain Q-points?  Each coset defines an ETALE ALGEBRA over Q
  (the field of definition of the preimages), and the condition that SOME
  coset yields all three P_i ∈ E(Q) is a condition on the image of
  (Q₀,Q₁,Q₂) under a specific 2-descent map to H¹(G_Q, E[2]³).

  This is DIFFERENT from the refuted 2-Selmer approach: it doesn't analyse
  four independent curves — it analyses the three doubled points on one
  curve, via the 64-coset action of E[2]³.

status: proposed
first-step: |
  1. **Compute the AP equation in terms of the group law.**  On
     E: y² = x(x²−c²), the duplication map and addition law are explicit
     rational functions.  Write the AP condition Φ(P₀,P₁,P₂) = 0 as a
     polynomial in the coordinates of P_i.  Since Φ factors through E³/E[2]³,
     the polynomial has degree 4 (the duplication map degree) in each
     variable and is symmetric under x_i ↦ x([−1]P_i) = x(P_i).

  2. **Identify which of the 64 E[2]-cosets can satisfy Φ = 0 over Q.**
     For each coset representative (T₀,T₁,T₂) ∈ E[2]³, substitute
     P_i = P_i' + T_i and ask whether the equation Φ(P₀'+T₀, P₁'+T₁, P₂'+T₂)
     can be identically zero (as a function of the P_i') — this would mean
     the coset algebraically contains the zero set.  More likely, Φ is
     GENERICALLY non-zero and its zero set is a proper subscheme of E³.
     For the cosets where Φ ≡ 0, the condition is vacuous (any P_i in that
     coset works) — this is the "special subvariety" case of Mordell–Lang.
     For the others, Φ = 0 is a nontrivial condition on the P_i'.

  3. **For a test c (Bremner's c=138600), compute the explicit P_i for the
     7-square witness and identify their cosets.**  The witness has exactly
     two of three doubled points in 2E(Q); compute their preimages P_i and
     determine which E[2]-cosets they live in.  Check whether the third
     point's failure to be in 2E(Q) corresponds to the required coset being
     empty over Q — a local obstruction that is visible in the 2-descent.

  4. **Derive the obstruction.**  If the AP condition forces the three P_i
     to lie in specific E[2]-cosets whose union is EMPTY over Q (i.e., no
     Q-point exists in those cosets by a 2-descent argument), then the MSS
     is impossible over Q.  This is a FINITE CHECK per c (64 cosets,
     2-descent computable by mwrank for any fixed c).  If the empty-coset
     condition holds for ALL c — i.e., the coset assignment forced by the
     AP equation is algebraically incompatible with rational points for ANY
     c — then we have a proof of non-existence.

  This first step is a symbolic algebra computation followed by an explicit
  2-descent for a test c.  It does not enumerate c; it checks whether the
  coset structure itself forces a contradiction.

precedent:
  - claim `robertson-elliptic-reduction`: MSS ⇔ three points in 2E(Q) with
    x-coordinates in AP on E: y² = x(x²−c²).  Status: proved.
  - Silverman, GTM 106: the Kummer sequence, 2-descent map, Selmer group.
    The map E(Q)/2E(Q) → H¹(G_Q, E[2]) is classical.
  - Bremner 1999: the duplication formula and 2E(Q) membership criterion.
  - This run's `robertson_reduction_check.txt`: for c=138600, exactly 2 of
    3 AP x-coordinates are in 2E(Q); the preimages are computed.
  - claim `gfp-2021-theorem-6-1-doubled-points-in-scope`: the GFP/HMS
    theorem applies to doubled points (not just to arbitrary E(Q) points).
  - NOT the same as the refuted `simultaneous-congruent-numbers-2selmer`
    (which studied four linked curves) — this is a SINGLE-CURVE 2-descent
    with 64 cosets of E[2]³, a different Galois module entirely.

speculation: The key unknown is whether Φ(P₀+T₀, P₁+T₁, P₂+T₂) is
  algebraically independent of the coset choice, or whether some cosets
  force Φ ≡ 0 (making the AP condition vacuous) while others force an
  impossible descent condition.  If every coset is algebraically equivalent
  (i.e., translating by 2-torsion merely permutes the zero set without
  changing its Q-point content), the coset approach adds nothing.
  But the duplication map [2] is a degree-4 cover with Galois group
  E[2] ⋊ {±1}, and the x-coordinate map kills {±1} but not E[2] — so
  translating by E[2] genuinely changes the equation Φ = 0 (because Φ
  involves x(2P) not x(P)).  Wait — x(2(P+T)) = x(2P) for T ∈ E[2],
  so the AP condition itself is E[2]-invariant.  The coset information
  enters ONLY through the rationality of the preimages P_i, not through
  the AP equation itself.  This means the approach reduces to: compute the
  2-descent map on the MSS triple and check whether the triviality of the
  Q_i in E(Q)/2E(Q) forces a contradiction in Sel₂(E).  This is a standard
  2-descent computation — the novelty is applying it to the specific triple
  rather than to a single point.

killed-by: _none yet_
```