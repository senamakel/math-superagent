```approach
id: integral-brauer-manin-nine-square
idea: Apply Colliot-Thélène–Xu integral Brauer-Manin obstruction to the full
  nine-square affine variety V/Z, not the six-square K3 of Bremner II.
  Every previous approach works at the level of rational points (K3,
  elliptic curves, Φ); the integral BM obstruction is a refinement that
  uses denominators — precisely what separates Q from extension fields
  where MSS exist.  An integral point surviving a Brauer class over Q can
  fail over Z because the denominator structure differs from Q(√3,√133).
mechanism: The nine entries are squares ⇔ each entry is a norm N_{Q(i)/Q}(·).
  The 7 line-sum equations + 8 norm equations define an affine variety V
  over Z of dimension 2 (18 variables − 16 equations).  The integral
  Brauer-Manin set V(A_Q)_Z^Br is the subset of integral adelic points
  orthogonal to Br(V) under the Brauer pairing.  If V(A_Q)_Z ≠ ∅ but
  V(A_Q)_Z^Br = ∅, then V(Z) = ∅ — the integer MSS problem is solved.
  The computation uses the exact sequence
    0 → Br(V)/Br(Q) → H^1(Q, Pic(V_Qbar)) → …
  for the affine variety V.  Since V is a system of norm equations, its
  Picard group and Brauer group should be tractable via the machinery of
  Harpaz–Skorobogatov (integral Brauer-Manin for affine varieties) and
  the explicit norm-torus description.  Crucially, this obstruction
  CAN separate Z from Z[√3,√133]: an integral adelic point that survives
  over the ring of integers of Q(√3,√133) can fail over Z.
status: proposed
first-step: Express the nine-square variety V as an explicit affine scheme
  over Z: variables (x_ij)_{1≤i,j≤3} and (s_ij) with equations
  x_ij = s_ij² and the 7 magic-sum equations.  Eliminate the s_ij to
  get V as a subvariety of A⁹_Z defined by "each x_ij is a square"
  (encoded as norm conditions).  Compute the generic fibre V_Q and its
  Picard group Pic(V_Qbar) using the norm-torus description.  Start a
  research search for "integral Brauer-Manin norm equations" to find
  the relevant Harpaz/Wittenberg papers.
precedent: Colliot-Thélène–Xu (Compositio 2009) — integral Brauer-Manin
  obstruction; Harpaz–Skorobogatov (Duke 2016) — Brauer group of affine
  varieties; Wittenberg (2010 thesis) — integral points on varieties
  defined by norm equations.  Never applied to the MSS problem.
  Distinguished from the refuted Brauer-Manin-K3 approach because (a) V
  is the full 9-square variety, not the 6-square K3; (b) the integral
  obstruction is stronger than the rational one; (c) the affine Picard
  group carries the integrality data that the K3's NS does not.
speculation: The Picard group of V_Qbar may be computable from the norm-torus
  fibration V → T (where T is the torus of magic-square entries).
  If Br(V)/Br(Q) contains an element whose evaluation is constant and
  nonzero on all integral adelic points (while vanishing on the extension
  fields where MSS exist), the proof is complete.  This is speculative
  because computing the Brauer group of an affine variety defined by
  8 norm equations and 7 linear equations has not been done in the
  literature, but the machinery exists.
```