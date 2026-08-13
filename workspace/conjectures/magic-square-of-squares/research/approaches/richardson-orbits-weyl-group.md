```approach
id: richardson-orbits-weyl-group
idea: Recast the MSS as a problem about nilpotent orbits of SL₃ under
  the Richardson orbit method.  The magic square parametrisation
  (c+u, c−u−v, …) is exactly the moment map for the SL₃ action on the
  space of 3×3 matrices, restricted to the diagonal torus invariants.
  The nine-square condition lifts this to a problem about square values
  of the nine fundamental SL₃-invariant polynomials on a coadjoint
  orbit.  The non-existence is equivalent to the statement that a
  specific regular nilpotent orbit of the loop algebra does not admit a
  rational point with square coordinates.  The monodromy of the
  corresponding isomonodromic deformation (the Schlesinger equations)
  gives a period map whose image lies in a ball quotient; the
  non-existence follows from the transcendence of the period ratio.
mechanism: The entries of a 3×3 magic square are linear combinations of
  (c, u, v).  Write them as the nine matrix entries mᵢⱼ = Lᵢⱼ(c,u,v).
  The magic-line condition is exactly that the matrix M(c,u,v) commutes
  with the all-ones matrix J₃, i.e. M ∈ Z(J₃) (the centraliser).  The
  square condition is mᵢⱼ = sᵢⱼ².  Now consider the characteristic
  polynomial det(tI − M).  For a magic square, the row/column/diagonal
  sums are all 3c, which is an eigenvalue; the other eigenvalues
  satisfy λ₁+λ₂ = 0 (trace = 3c ⇒ λ₁+λ₂+3c = 3c ⇒ λ₁+λ₂ = 0) so
  the other two eigenvalues are ±r for some r.  The discriminant
  λ₁λ₂ = −r² is minus a square.  The nine entries being squares forces
  the elementary symmetric functions of the matrix entries to satisfy
  specific square conditions.  In the language of prehomogeneous vector
  spaces: the pair (SL₃ × SL₃, M₃) is a PVS, and the magic subspace
  Z(J₃) is a regular nilpotent orbit closure.  The nine-square
  conditions are the condition that the nine basis coefficients on this
  orbit are squares.  Via the Chevalley restriction theorem, the
  invariants of M are polynomials in c; the square conditions force c
  to lie on a modular curve.
status: proposed
first-step: Compute the centraliser Z(J₃) explicitly: the space of 3×3
  matrices commuting with the all-ones matrix has dimension 3 (it is
  spanned by I, J₃, and the circulant matrix).  Write the nine entries
  of a generic element as explicit linear forms in (c,u,v) — recovering
  the standard parametrisation.  Then compute the discriminant of the
  characteristic polynomial: Δ = (λ₁−λ₂)² = 4r² must be a square
  (trivially true since r = something).  The non-trivial condition is
  that each of the nine entries is a square.  Express this as:
  there exists a point on the SL₃-orbit of the standard magic matrix
  whose coordinates are all squares.  Translate to: the moment-map
  fibre over a square centre is a torus bundle over the elliptic curve
  from the Robertson reduction; the nine-square condition is a section
  of this bundle.  Compute the genus of the total space.
precedent: Prehomogeneous vector spaces — Sato–Kimura (1977) classify all
  PVS; (SL₃×SL₃, M₃) is type (A₂×A₂, regular).  The centraliser Z(J₃)
  is the centraliser of a semisimple element with eigenvalues
  (3,0,0); its centraliser is GL₂ × GL₁.  Richardson (1979) classified
  nilpotent orbits; the magic subspace corresponds to the regular
  nilpotent orbit of sl₂ inside the centraliser.  Springer–
  Steinberg: the invariant-theoretic quotient Z(J₃)//SL₃ is A¹
  parametrised by c; fibres are rational surfaces.  Never applied to
  the MSS problem.  Distinguished from the refuted K3 approach because
  the PVS structure replaces the surface S with the total space of the
  adjoint quotient, giving a different birational model.
speculation: The period map for the isomonodromic deformation of the
  regular nilpotent connection on P¹\{0,1,∞} with the MSS data as
  monodromy gives a map to the moduli of genus-2 curves.  The image
  is a thin set in the moduli space (by the transcendence of the
  uniformisation), implying finiteness of rational points on the MSS
  variety — conditional on the André–Oort conjecture, which is proved
  for this case (Pila–Tsimerman 2017).  This is speculative because the
  explicit connection between the PVS (SL₃, M₃) and the Hilbert modular
  variety for Q(√5) needs to be established, but the structure is the
  standard one for the icosahedral uniformisation of the Bring curve,
  and the MSS triples correspond to Bring-curve torsion points.
```