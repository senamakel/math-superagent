```approach
id: conic-parametrisation-pair-sum-surface
idea: The strongest unbroken numerical fact from the Φ-reduction program is
  the `both=0` finding: over complete pair-sum censuses to M=800 (2.5 × 10⁹
  pairs), no pair q1,q2 ∈ Φ has BOTH 1−(q1+q2) and 1+(q1+q2) as rational
  squares.  The condition "both 1−s and 1+s are rational squares" is
  equivalent to `s = 2t/(1+t²)` for some rational t (parametrisation of
  x²+y² = 2), i.e. s lies on the IMAGE of a GENUS-0 rational curve.
  The both=0 finding therefore states that the set S = Φ + Φ ∩ (0,1) is
  DISJOINT from the image of t ↦ 2t/(1+t²).  This is a single Diophantine
  equation in five variables:
    4m₁n₁(m₁²−n₁²)/(m₁²+n₁²)² + 4m₂n₂(m₂²−n₂²)/(m₂²+n₂²)² = 2t/(1+t²),
  with mᵢ,nᵢ,t ∈ Q, mᵢ > nᵢ ≥ 1, gcd(mᵢ,nᵢ)=1, t ∈ (0,1), and the sum < 1.
  Cross-multiplying gives a homogeneous polynomial equation of degree 8 in
  the 5 variables — a surface over Q.  PROVE this surface has no Q-points.
  This is a concrete variety: compare it to the K3 and the nine-square X,
  compute its geometry, and apply Faltings/Bombieri-Lang or a 2-descent on
  its Albanese if applicable.

  Named mathematics: parametrisation of the conic x²+y²=2 (Diophantus),
  the Φ-value-set as the image of the degree-4 map f: P¹ → P¹, and the
  surface V = f(P¹) + f(P¹) − g(P¹) = 0 where g(t) = 2t/(1+t²).

mechanism: The both=0 numerical evidence is so strong (0 hits in 2.5×10⁹ pairs,
  while each side alone has 718 and 150 hits) that the surface is almost
  certainly empty of Q-points.  The approach is to PROVE it empty by
  computing the geometry of the surface V: (x₁,x₂,t) in weighted projective
  space with equations
    q(m₁,n₁) + q(m₂,n₂) = s
    s = 2t/(1+t²)
  where q(m,n) = 4mn(m²−n²)/(m²+n²)² = sin(4 arctan(n/m)).

  The trigonometric form is critical: q(m,n) = sin(4α) where α = arctan(n/m).
  So the equation is sin(4α₁) + sin(4α₂) = sin(2β) where t = tan(β/2) =
  sin(β)/(1+cos(β)).  Using sin(4α) = 2 sin(2α) cos(2α) and
  sin(2α) = 2 tan(α)/(1+tan²(α)), the equation becomes a polynomial in
  r₁ = n₁/m₁, r₂ = n₂/m₂, and t.

  Key geometric reduction: the map m ↦ q(m,n) factors through
  X₁(N) → X(1) for some level N (it's the modular function for Γ(4) or
  similar — sin(4 arctan(z)) is the inverse of a Schwarz triangle function).
  The equation q(r₁) + q(r₂) = g(t) is a CURVE on the modular surface
  P¹ × P¹ × P¹.  This is a (2,2,2)-divisor in (P¹)³ — a surface of general
  type if sufficiently general, with only finitely many rational points
  by Faltings (curves) or Bombieri–Lang (surfaces).  Determine its type
  by intersection theory.

  Alternatively, a cleaner formulation: set uᵢ = (mᵢ/nᵢ + nᵢ/mᵢ)/2 =
  (mᵢ²+nᵢ²)/(2mᵢnᵢ).  Then q(mᵢ,nᵢ) = (uᵢ²−1)^(1/2) / uᵢ² (up to sign).
  More usefully: the rational representation q = X/Y with
    X = 4mn(m²−n²), Y = (m²+n²)²
  gives a point on the elliptic curve y² = x³ − x after scaling (the
  congruent-number curve for d=1).  Indeed, q(m,n) is the x-coordinate of
  the duplication of a point on E: y² = x³−x — this is the ℘(2z) function
  for the square torus.  So the equation q(r₁) + q(r₂) = g(t) becomes
  x₁ + x₂ = g(t) where x_i are x-coordinates of points in 2E(Q), with
  E: y² = x³ − x.  This is a THREE-POINT condition on E(Q): two doubled
  points whose x-coordinates sum to g(t).  Since g(t) parametrises
  x²+y²=2, this is an ADDITIVE condition on doubled x-coordinates.

  The critical insight: on E: y² = x³ − x, the set 2E(Q) is a subgroup,
  and the sum x₁ + x₂ = s has been studied — it relates to the addition
  law and to the fact that x₁ + x₂ + x₃ = (y₁−y₂)²/(x₁−x₂)² for points
  with P₁ + P₂ + P₃ = O.  For doubled points, the group structure is more
  rigid.  If BOTH x₁+x₂ = g(t) AND g(t) is of the special form
  s = 2t/(1+t²), then a point on the curve E_M,N appears.

  The surface V is thus the fibre product of:
    (P₁, P₂) ∈ E² with P_i = 2Q_i  (i.e., P_i ∈ 2E(Q))
    and x(P₁) + x(P₂) ∈ Im(g).
  Since g(t) = 2 − (g(t)²+…)?  Actually g(t)² + (2/(1+t²))² = 2? No.
  The correct identity: if s = 2t/(1+t²), then 1−s² = (1−t²)²/(1+t²)²,
  so (1−s, 1+s) = ((1−t)²/(1+t²), (1+t)²/(1+t²)).  Both are squares iff
  t ∈ Q, which is the whole point.

  This parametrisation reduces the surface V to a variety in E × E × P¹,
  fibre product over the conic.  Its Kodaira dimension can be computed
  by adjunction on E × E × P¹.  If κ(V) = 2 (general type), Bombieri-Lang
  (conditional) gives finiteness; if V is elliptic or K3, descent methods
  apply.

status: proposed
first-step: |
  1. **Write the explicit equation for V.**  Parametrise q(m,n) by points
     on E: y² = x³ − x.  The duplication map x([2]Q) = f(x(Q)) = (x⁴+2x²+1)/(4x(x²−1))
     for E: y² = x³−x (a=−1, b=0).  Then q(m,n) = x([2]Q) for some Q.
     The pair-sum condition is x([2]Q₁) + x([2]Q₂) = 2t/(1+t²).
     Eliminate t via t = (1−√(1−s²))/s if needed, or keep the conic equation
     s² + w² = 2 (where w = √(1−s²) + √(1+s²)? — no, the parametrisation
     directly gives s).  The surface is:
       { (Q₁, Q₂, t) ∈ E² × P¹ : x([2]Q₁) + x([2]Q₂) = 2t/(1+t²) }.
     This is a divisor of type (2,2,2) on E×E×P¹ (the duplication map is
     degree 4, and the equation is linear in the x-coordinates).

  2. **Compute genus/type of V.**  Project V to E×E (forgetting t): the
     fibre over (Q₁,Q₂) is the set of t such that 2t/(1+t²) = x₁+x₂.
     This is at most 2 points (solving t²·(x₁+x₂) − 2t + (x₁+x₂) = 0,
     discriminant 4 − 4(x₁+x₂)² = 4(1−(x₁+x₂)²)).  So the projection
     V → E×E is a DOUBLE COVER, branched where x₁+x₂ = ±1.
     Since E×E is an abelian surface (κ=0), the double cover V is
     determined by the branch divisor B: x₁+x₂ = ±1 on E².
     Compute the genus/κ of V from the branch data: the double cover of
     an abelian surface branched along a smooth divisor B has
       K_V = π*(K_{E²}) + (1/2)B = (1/2)B
     since K_{E²} = 0.  So κ(V) is determined by the Iitaka dimension of
     B.  If B is ample or big, V is of general type and has finitely many
     rational points (conditional on Bombieri-Lang, which is open for
     surfaces — so this gives a conditional result).

  3. **Determine the rational points on V.**  If κ(V) = 2, the conditional
     finiteness + the complete pair-sum census to M=800 (zero hits) is
     EVIDENCE that V(Q) = ∅ (a single computation that checked all points
     of height ≤ some bound).  If κ(V) ≤ 1, V has a rational or elliptic
     fibration, and existence reduces to base-curve points.

  4. **Check against the witnesses.**  The both=0 finding has ALREADY been
     checked: the M=800 census computed all pairs and found zero solutions —
     this IS the witness-check.  The surface V has no Q-points in the range
     covered by the census; the task is to prove it has none anywhere.

precedent:
  - claim `phi-pair-sides-both-square-zero-through-M800`: both=0 verified
    at complete censuses to M=800 (status: checked).
  - claim `phi-no-triple-m400`: no additive triple q1,q2,q1+q2 in Φ for
    m,n ≤ 400 (status: checked, but not a theorem).
  - The parametrisation of x²+y²=2: t ↦ (2t/(1+t²), (1−t²)/(1+t²)) is
    classical (Pythagorean triples, stereographic projection).
  - The duplication formula on E: y² = x³−x: x([2]Q) = (x⁴+2x²+1)/(4x(x²−1)).
  - claim `concordant-forms-iff-ell-torsion-order-2`: the single-AP
    condition transports to the concordant-forms curve E(-d,d).
  - The surface V has NOT been studied in the literature as a stand-alone
    Diophantine object; the both=0 census is this run's own result.

speculation: The decisive gap is whether V is of general type (κ=2) — if so,
  the conditional finiteness result is a genuine partial theorem, and the
  numerical census is supporting evidence for V(Q)=∅.  If κ(V) ≤ 1, the
  both=0 finding remains a numerical observation and the surface geometry
  does not close the problem.  The branch-locus computation (X₁+X₂ = ±1 on
  E², where X_i = x([2]Q_i)) is explicit and sympy-tractable — the branch
  divisor is a (4,4)-curve on E² (since X_i is a degree-4 function), and
  its genus can be computed by adjunction.  The double-cover formula
  K_V = (1/2)π*(B) is correct for a smooth double cover branched along B;
  if B has singularities, they must be resolved.  The approach also requires
  verifying that the parametrisation q(m,n) = x([2]Q) is SURJECTIVE onto
  2E(Q) (it is, by definition, since every doubled point has an x-coordinate
  of this form for SOME Q — the question is whether every q(m,n) arises
  from a Q-rational Q).  For m,n ∈ Q, Q = (x(Q), y(Q)) is rational exactly
  when x(Q) ∈ Q and x(Q)³−x(Q) is a rational square.  The condition that
  q(m,n) = (x(Q)⁴+2x(Q)²+1)/(4x(Q)(x(Q)²−1)) for some rational x(Q) is an
  alternative characterisation of Φ — potentially simpler than the m,n form.

  This is SPECULATIVE as a proof of emptiness, but it is a precise
  geometric formulation of the strongest numerical evidence this run has
  produced.  Even if it only yields a conditional finiteness result, that
  is a genuine partial theorem delivered from the both=0 data.

killed-by: _none yet_
```