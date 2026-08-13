```approach
id: galois-descent-extension-field-anchor
idea: Use the explicit degree-4 extension-field 3×3 MSS (Bremner 1999, centre
  532, over Q(√3,√133)) as a POSITIVE structural datum to determine the exact
  Galois-cohomological obstruction that kills Q-points.  Every previous
  approach treats this as a negative warning ("don't prove too much"); this
  approach inverts it: the Q(√3,√133)-solution IS a point on the Robertson
  curve E_c (c = 532 = 2²·7·19), with explicit MW generators over the
  extension, and Gal(Q(√3,√133)/Q) ≅ V₄ acts on the MSS triple by permuting
  the square-root choices.  The obstruction to descending this triple to Q is
  a 1-cocycle in H¹(V₄, E_c[2]) — a finite, computable group.  Computing it
  exactly identifies the *obstruction class*, and the same class must vanish
  for ANY c that admits an MSS over Q.  This turns the problem into: classify
  all c for which this specific Galois-cocycle vanishes.  The cocycle is a
  function of c (via the 2-torsion of E_c and the field of definition of the
  MW generators), so the classification is a family computation over c — but
  with the extension-field solution as an anchor, the cocycle is pinned down
  explicitly rather than conjectured.

mechanism: Bremner's Q(√3,√133)-MSS (Acta Arith. 88, 1999, claim
  `bremner-deg4-centre-532`) has centre c = 532 = 2²·7·19, magic constant
  1596.  The Robertson curve is E: y² = x(x²−c²) = x(x²−283024) over
  K = Q(√3,√133).  The MSS gives three doubled points 2P₀, 2P₁, 2P₂ ∈ E(K)
  with x-coordinates in AP and all six of x(2P_i) ± c being squares in K.
  Gal(K/Q) ≅ V₄ acts on the MW group E(K) and on the torsion E[2] ≅ (Z/2)².
  The key observation: a Q-rational MSS would give three doubled points in
  E(Q), hence three preimages P_i ∈ E(Q̄) that are Galois-invariant up to
  translation by E[2].  The Galois action on the K-MSS gives an explicit
  element of H¹(Gal(K/Q), E[2]) — the obstruction to descending the triple
  from K to Q.  This cocycle is computable from the explicit coordinates in
  Bremner 1999.

  The approach has three stages:
  (1) **Compute the obstruction class for Bremner's c=532.**  Write the
      MW basis of E(K) (by 2-descent over K), identify the three AP
      x-coordinates, lift them to explicit P_i ∈ E(K) via the duplication
      formula, and compute the Galois action: for each σ ∈ Gal(K/Q), write
      σ(P_i) = P_i + T_{i,σ} where T_{i,σ} ∈ E[2].  The map σ ↦ T_{i,σ}
      is a 1-cocycle; its cohomology class [T] ∈ H¹(V₄, E[2]) is the
      obstruction.  This class is NONZERO because the MSS is not over Q.

  (2) **Derive the condition for vanishing.**  For a general c, the same
      construction produces a cocycle class depending on c.  Vanishing means
      the cocycle is a coboundary: T_σ = σ(P) − P for some P ∈ E(K).  This
      is a finite condition on the MW generators of E(K) modulo the
      Galois action — a *descent* condition in the sense of Galois
      cohomology on elliptic curves, which is classical (Silverman, VIII).

  (3) **Classify c for which the obstruction vanishes.**  The obstruction
      class varies in the finite group H¹(V₄, E[2]) ≅ (Z/2)² (since
      H¹(V₄, E[2]) is finite for any finite Galois module).  Only finitely
      many c can map to the zero class in H¹, because the cocycle depends
      algebraically on c through the MW generators' fields of definition.
      This reduces the MSS to checking finitely many c — a finiteness result
      stronger than the GFP/HMS conditional reduction, because it uses the
      specific Galois structure of Bremner's family rather than a general
      height bound.

  Named mathematics: Galois cohomology of elliptic curves (Silverman VIII),
  the Kummer sequence 0 → E[2] → E → E → 0 and its associated descent map
  E(Q)/2E(Q) ↪ H¹(G_Q, E[2]), the inflation-restriction sequence for the
  tower Q ⊂ Q(√3) ⊂ Q(√3,√133), and the explicit cocycle computation from
  Bremner 1999.

  Why this is different from everything refuted: it is not a modular sieve
  (uses Galois cohomology, not congruences), not a height bound (H¹ is finite
  regardless of rank), not a geometric classification (κ, BM), and not a
  Φ-additive argument (works on the curve directly).  It is a *descent*
  argument anchored to a concrete known solution, making it checkable rather
  than speculative.

status: proposed
first-step: |
  **Reconstruct Bremner's Q(√3,√133)-MSS and compute its Galois action on
  the Robertson curve.**

  1. **Exact grid reconstruction.**  From Bremner 1999 and claim
     `bremner-deg4-centre-532`, reconstruct the nine entries (squares) of
     the degree-4 MSS over Q(√3,√133) in exact sympy algebraic number
     arithmetic.  Verify magic (all 8 line sums equal) and squareness
     (each entry is a perfect square in K).  Extract c = 532, u, v.

  2. **Recover the three doubled points on E: y² = x(x²−c²).**
     For each of the four APs through the centre (differences u, v, u+v,
     u−v), identify which endpoints are squares in K.  The MSS requires
     all eight endpoints to be squares; the field K makes this possible.
     Map each AP to a point on E(K) via the standard congruent-number
     transform: if A², e², B² is an AP of squares with common difference d
     and centre e², then (X, Y) = (B² − A², B(B²−A²)) is on E_d (up to
     scaling).  With e = √c, the scaling aligns all four curves to the
     same E: y² = x(x²−c²).  Extract the three doubled points for the
     anti-diagonal AP (the one with difference d = u+v or u−v).

  3. **Galois action.**  Gal(K/Q) ≅ V₄ = {1, σ, τ, στ} where σ(√3) = −√3
     and τ(√133) = −√133.  For each generator, compute the image of the
     three doubled x-coordinates and their preimages P_i (via duplication
     inversion: solve x(2P) = X for P, which reduces to a quartic
     x⁴ − 4Xx³ + 2c²x² + 4c²Xx + c⁴ = 0, splitting as (x²−2Xx−c²)²−4X²(x²−c²)
     — factorable).  The Galois action on the P_i gives the cocycle
     T_{i,σ} ∈ E[2].

  4. **Determine the cocycle class.**  Compute whether the cocycle is
     trivial in H¹(V₄, E[2]).  It must be NONTRIVIAL (otherwise the MSS
     would descend to Q).  Report the exact class.

  This first step is a finite, exact computation over an algebraic number
  field of degree 4 — well within sympy's capabilities.

precedent:
  - Bremner, "On squares of squares", Acta Arith. 88 (1999) 289-297:
    the Q(√3,√133)-MSS.  Claim `bremner-deg4-centre-532`, status: checked.
  - claim `extension-field-mss-exist`: MSS exist over proper algebraic
    number fields.  This is the hinge — any proof over Q must use
    rationalness/integrality, which Galois cohomology captures.
  - Silverman, "The Arithmetic of Elliptic Curves", GTM 106, Chapter VIII:
    Galois cohomology, the Kummer sequence, descent via H¹(G_Q, E[m]).
  - The Robertson reduction: claim `robertson-elliptic-reduction` (proved).
    Three doubled points on E: y² = x(x²−c²) with x-coordinates in AP.
  - This run's refutation of `root-number-parity-four-curves`: the parity
    argument was too weak (only mod 2), but the Galois-cohomological
    approach is a proper descent, not a parity sieve.
  - NOT subsumed by any approach in APPROACHES.md.  The extension-field
    MSS has been treated as a warning sign; no approach has used it as a
    positive structural datum.

speculation: The decisive unknown is whether the cocycle for c=532 has a
  clean description in terms of c that extends to a family classification.
  If the cocycle class is simply the image of c under the Kummer map
  K*/(K*)² → H¹(Gal, E[2]) composed with a norm, then the vanishing
  condition is a quadratic-form condition on c — reducing the MSS to
  solving a ternary quadratic form over Z (a conic), which has finitely
  many or no solutions by standard theory.  If the cocycle depends on more
  than c (e.g., on the MW generators' heights), the classification may not
  be finite.  The first-step computation settles this.

killed-by: _none yet_
```