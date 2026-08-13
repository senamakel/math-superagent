```approach
id: baker-elliptic-logarithms-ap
idea: Apply Baker's method (linear forms in elliptic logarithms, David 1995 /
       Hirata-Kohno / Masser) to the specific AP-on-doubled-points equation
       on the Robertson curve E: y² = x(x²−c²).  For a fixed centre e² and
       anti-diagonal half-difference c, the MSS condition is that three
       points 2P₀, 2P₁, 2P₂ ∈ E(Q) have x-coordinates in AP.  Write
       P_i in terms of the Mordell–Weil generators of E(Q) with unknown
       integer coefficients n_i, m_i (for rank ≤ 2; larger rank is similar).
       The AP condition x(2P₀) + x(2P₂) = 2x(2P₁) translates via the
       Weierstrass ℘-function — specifically, applying the duplication
       formula ℘(2z) = (℘(z)²+c²)²/(4℘'(z)²) — into an equation in
       elliptic logarithms of the form L(n₀,…,m₂) = 0, where L is a
       nontrivial linear form in the elliptic logarithms of the generators
       with algebraic coefficients.  Baker's theorem for elliptic logarithms
       (David, "Minorations de formes linéaires de logarithmes elliptiques",
       Mém. SMF 1995) gives an explicit lower bound
         |L| > exp(−C · (log max|n_i|)^κ)
       for all nonzero integer vectors (n_i, m_i) where |L| ≠ 0.  If the
       AP-equation equals zero for some integer coefficient vector — i.e.,
       if an MSS exists — then L = 0, and Baker's bound yields an inequality
       forcing max|n_i| ≤ B for an explicitly computable B.  Since max|n_i|
       controls the height of the points and hence the size of c itself,
       this gives an explicit upper bound on c for any MSS.  If the bound on
       c falls below the known search bound (10²⁵, Morgenstern/Buell), then
       no MSS exists.  If the bound on c exceeds the search bound, the
       method still yields an EFFECTIVE threshold c_max with the theorem
       "any MSS has centre ≤ c_max" — a genuine partial result.  This is
       the standard Baker-machine for Diophantine equations on elliptic
       curves, applied to the specific MSS equation for the first time.

mechanism: The Robertson reduction (`robertson-elliptic-reduction`) puts the
  full MSS on the single curve E_c: y² = x(x²−c²).  The AP condition is
    x(2P₀) + x(2P₂) − 2x(2P₁) = 0,
  where each P_i ∈ E(Q) and x(2P) is the duplication-map x-coordinate.
  Writing P_i = Σ_j a_{ij} G_j + T_i (G_j MW generators, T_i torsion,
  a_{ij} ∈ Z), the duplication formula for the x-coordinate expresses
  x(2P) as a rational function of degree 4 in x(P):
    x(2P) = (x(P)² + c²)² / (4x(P)(x(P)² − c²)).
  The Weierstrass parametrisation x(P) = ℘(z), y(P) = ℘'(z)/2 gives
  x(2P) = ℘(2z).  The AP equation becomes
    ℘(2z₀) + ℘(2z₂) − 2℘(2z₁) = 0,
  with z_i = Σ_j a_{ij} ω_j + η_i (ω_j the elliptic logarithms of the
  generators, η_i a torsion point logarithm).  Using the addition formula
  for ℘, this is a rational expression in ℘(z_i), ℘'(z_i) — equivalently,
  a relation in the group law on E:
    [2]P₀ + [2]P₂ = 2[2]P₁   in some sense?
  Actually the AP condition on x-coordinates IS NOT the group law — it's
  a different algebraic condition on E³.  But it IS algebraic, so it
  defines a curve/surface in E³ and classical Baker theory applies to its
  rational points via the logarithmic embedding.

  The key step: embed E(Q) into the Mordell–Weil lattice via the elliptic
  logarithm map φ: E(Q) → C/Λ.  The AP condition becomes an equation
  F(φ(P₀), φ(P₁), φ(P₂)) = 0 where F is a meromorphic function on (C/Λ)³
  expressible via the Weierstrass ℘-function and its derivative.  Writing
  each φ(P_i) in terms of the basis ω_j and unknown integers, F becomes
  a linear combination of products of ℘ and ℘' evaluated at integer linear
  combinations of the periods.  A transcendence theorem (Baker–Masser for
  elliptic functions, or the David/Hirata-Kohno lower bounds for linear
  forms in elliptic logarithms with algebraic coefficients) gives:
    if F(n⃗) = 0 for some integer vector n⃗, then max|n_i| < B,
  where B is an explicitly computable constant depending on E_c, its
  MW generators, and the coefficients of F.  The height of x(2P) grows
  as ĥ(2P) = 4ĥ(P) ∼ max|n_i|², so a bound on max|n_i| is a bound on
  the height of the MSS entries, hence a bound on c and e².

  The computation is standard but heavy: (i) compute the MW basis of
  E_c by 2-descent/mwrank, (ii) get period lattice and elliptic logarithms
  to high precision, (iii) express F as a ℘-linear form, (iv) apply David's
  theorem with the explicit constants in terms of h_F(E_c), [K:Q], and the
  degree of F, (v) solve the resulting inequality for max|n_i|.  The
  dependency on c makes this a family problem — but the Baker constants
  depend polynomially on h_F(E_c), which grows as log c, so the resulting
  bound B(c) grows like C·(log c)^κ.  If B(c) < log c for large c, the
  inequality forces c to be bounded — and the explicit threshold is the
  result.

  Named mathematics: Baker's theorem for elliptic logarithms (Masser 1975,
  Bertrand 1995, David 1995), the explicit lower bounds of David (Mém. SMF
  1995) and Hirata-Kohno (1991), the Weierstrass-℘ duplication formula
  ℘(2z) = −2℘(z) + (¼)(℘''(z)/℘'(z))² [which simplifies to the known
  degree-4 rational function above], and the Néron-Tate height / elliptic
  logarithm relation ĥ(P) = (1/2)|φ(P)|² for CM curves.

first-step: |
  1. **Derive the explicit algebraic form of the AP equation.**
     On E: y² = x³−c²x, write the duplication formula:
       x(2P) = f(x) = (x²+c²)²/(4x(x²−c²)).
     For three points P₀, P₁, P₂ ∈ E(Q), the AP condition is:
       f(x₀) + f(x₂) = 2 f(x₁),
     where x_i = x(P_i).  Eliminating denominators gives a polynomial
     equation in x₀, x₁, x₂ of degree ≤ 12 in each variable.  This is
     the subvariety V_c ⊂ A³.

  2. **For a fixed test curve (e.g., Bremner's c=138600, rank 2), compute
     the MW basis and the elliptic logarithms.**  Using sage or PARI/GP:
     get the period lattice, the elliptic logarithm embedding, and express
     the three unknown points in the MW basis.  Convert the AP equation to
     an equation in the logarithmic parameters z_i ∈ C.  This step
     verifies that the equation is non-degenerate (not identically zero)
     on E³.

  3. **Apply David's lower bound.**  Use David (1995) Theorem 2.1 or the
     formulation in Bugeaud–Győry (1996) for elliptic equations.  The
     condition F(x₀, x₁, x₂) = 0 where F is the AP equation translates
     to G(φ(P₀), φ(P₁), φ(P₂)) = 0 where G is built from ℘.  If G is not
     identically zero on the subspace spanned by the MW generators, David's
     theorem gives |G| > exp(−C_G · (log H)^κ_G) for nonzero values, where
     H = max|n_i| for the integer coefficient vector.  Since the MSS
     forces G = 0, we must have H ≤ exp(C_G^{1/κ_G}) — an explicit bound.
     Compute this bound numerically for the test c, and report the maximum
     possible log c it would allow.

  4. **Report.**  If the Baker bound on log c is below the known search
     threshold (~60, corresponding to c ≈ 10²⁵), the approach yields a
     theorem: no MSS exists with centre in the searched range.  If the
     bound is above the search threshold, report the effective bound
     as a partial result and the obstacle (Baker constants too large).

status: proposed
precedent: |
  - Masser, D.W., "Elliptic Functions and Transcendence", Lecture Notes in
    Math. 437, Springer 1975 — the foundational Baker-type result for
    elliptic logarithms.
  - David, S., "Minorations de formes linéaires de logarithmes elliptiques",
    Mém. Soc. Math. France (N.S.) No. 62 (1995), iv+143 pp. — the explicit
    constants and the theorem statement needed.  Theorem 2.1 gives the
    lower bound for linear forms in elliptic logarithms with explicit
    dependence on the Faltings height.
  - Hirata-Kohno, N., "Formes linéaires de logarithmes de points algébriques
    sur les groupes algébriques", Invent. Math. 104 (1991) 401–433.
  - The duplication formula for the x-coordinate on E: y² = x³+ax+b
    (standard, in any elliptic-curve textbook; the explicit rational form
    is x([2]P) = (x⁴−2ax²−8bx+a²)/(4(x³+ax+b)) — for a=−c², b=0 this
    simplifies to (x²+c²)²/(4x(x²−c²))).
  - NOT the same as David–Philippon E³: DP07 gives a height bound on all
    points of a subvariety of E³ in terms of the subvariety's geometry
    (Faltings height of E, deg V, etc.).  Baker's method gives a lower
    bound for a specific Diophantine equation using linear forms in
    elliptic logarithms.  Both are "effective" but use different theorems
    and yield different constants.
  - No source in this library applies Baker's method to the MSS AP equation.

speculation: The key unknown is whether the function G (the AP condition
  expressed in elliptic logarithms) is non-degenerate on the MW lattice —
  i.e., whether G(n₁,…,n_r) ≡ 0 forces all n_i = 0.  If G is identically
  zero on the lattice, the equation holds for all integer vectors and the
  Baker lower bound never engages — the approach fails.  The first step
  checks this degeneracy on a test curve.  If non-degenerate, the effective
  bound B(c) may still be astronomically large (Baker constants are
  typically gigantic), so the result might be "effective bound exists but
  exceeds the search frontier" — still a partial result.  The approach
  also requires the MW basis for E_c, which is computable for any fixed c
  via 2-descent but not across the family without a general rank bound.
killed-by: _none yet_
```