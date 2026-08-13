```approach
id: freys-curve-four-q-isogenies
idea: Recast the MSS as a problem about Q-rational isogenies of degree 4
  between elliptic curves.  Each AP of squares through the centre —
  a²−d, a², a²+d all squares — is equivalent via the classical congruent-
  number transformation to the elliptic curve E_d: y² = x³ − d²x having a
  point in 2E_d(Q).  But this is ALSO equivalent to: the curve
  E_{a²}: y² = x(x²−a⁴) admits a Q-rational 4-isogeny whose kernel
  contains a specific point.  The four AP conditions together force a
  configuration of four 4-isogenies on the same curve with linked kernels.
  The modular curve X₀(4) parametrising 4-isogenies is rational (genus 0),
  so one can write explicit coordinates; the four linked conditions define
  a curve C on X₀(4)⁴ whose rational points are the MSS.  Compute the
  genus of C; if genus(C) ≥ 2, Faltings gives finiteness; if genus(C) = 1
  and rank < genus, Chabauty applies.  This is NOT the refuted
  Chabauty–Coleman approach — those were Bremner's explicit quartics
  (genus 1).  Here the object is the moduli curve of linked 4-isogenies,
  which lives at the level of the j-invariant 1728 family and may have
  higher genus.
mechanism: For a = e² (centre square), the curve E: y² = x(x²−a²) has
  CM by Z[i] (j=1728).  A point P ∈ E such that x(2P) is in AP with a
  corresponds to a 4-isogeny from E to some E′, because the doubling map
  [2]: E → E/⟨P⟩ factors through a cyclic 4-isogeny when P has order 4
  in the appropriate Selmer structure.  Concretely: the four differences
  u, v, u+v, u−v correspond to four points Pᵢ (i = 1..4) on E with
  x(2Pᵢ) = a² ± dᵢ forming an AP.  The linkage u+v−(u+v)=0 and u−v−(u−v)=0
  forces the sum of the corresponding kernels to satisfy a torsion
  condition on the product of four copies of X₀(4).  The resulting modular
  curve C (the fibre product of four X₀(4)'s with the additive linkage
  imposed) is a curve over Q whose rational points parametrise all MSS
  with centre a².  Computing its genus and Jacobian rank is the decisive
  step.  If C is genus 0, the MSS family is rationally parametrised
  (existence likely).  If genus 1, standard descent applies.  If genus ≥ 2,
  Faltings + an effective Chabauty computation settles it.
status: parked-behind-blocking-question
first-step: Express the condition "x(2P) = a² ± d" on E: y² = x(x²−a⁴) in
  terms of the 4-isogeny kernel.  The curve X₀(4) has explicit equation
  (e.g. via the classical modular function j₄(z) = j(4z)).  Write the
  coordinates of a point on X₀(4) corresponding to the isogeny with
  kernel ⟨P⟩.  Then write the additive linkage u+v = w, u−v = z as an
  algebraic condition on the four points (φ₁, φ₂, φ₃, φ₄) ∈ X₀(4)⁴.
  Compute the genus of the resulting curve symbolically.
precedent: Standard — X₀(N) for N = 4 is rational; the j-map from X₀(4) to
  X(1) is explicit (e.g., Fricke 1928, or modern references).  The
  connection between congruent numbers and 4-isogenies on
  y² = x³ − n²x is classical.  The new move is: instead of studying the
  single curve E_e with three doubled points, study the moduli space of
  four linked 4-isogenies, which encodes all four AP differences
  simultaneously and whose geometry (genus) determines the answer.
  NOT subsumed by Bremner II's K3: that K3 encodes the generic fibration
  E_λ over Q(λ); the modular curve here encodes the SPECIFIC choice of
  four kernel points linked by additive relations, which is data at a
  different level (moduli of isogenies, not NS of a surface).
speculation: The fibre product may have genus 0 and yield a parametric
  construction of an MSS (proving existence), or genus ≥ 2 ruling out any
  rational MSS.  The 4-isogeny formulation has not been applied to the
  MSS problem before in the literature.
```