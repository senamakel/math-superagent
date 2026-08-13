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
status: refuted
killed-by: The PVS premise is correct — (SL3 × SL3, M3) with the two-sided
  action (A,B)·M = A·M·B⁻¹ IS a prehomogeneous vector space, relative
  invariant det, open orbit = invertible matrices (Sato–Shintani;
  Sato–Kimura, Nagoya Math. J. 65 (1977) 1–155). But the MSS conditions
  are NOT expressed by PVS relative invariants (the relative invariants are
  powers of det, whereas 'each of nine entries is a square' is a coordinate
  condition with no PVS reading), and the magic subspace — the centraliser
  of the all-ones matrix J₃ — is the centraliser of a SEMISIMPLE element
  (J₃ has eigenvalues 3,0,0), hence a reductive centraliser of dimension 3,
  NOT a Richardson/nilpotent orbit (Richardson orbits parametrise nilpotent
  conjugacy classes). The period-map → ball quotient → André–Oort → Bring
  curve → Q(√5) chain is ungrounded in any source and would, if valid,
  overprove (cannot separate Q from Q(√3,√133)/Q over which MSS provably
  exist, this run's extension-field-mss-exist). André–Oort for curves in
  Hilbert modular varieties is real (Yafaev; effective Binyamini–Masser)
  but unrelated to the MSS.
precedent:
  - "Sato–Kimura, A classification of irreducible prehomogeneous vector
    spaces and their relative invariants, Nagoya Math. J. 65 (1977) 1–155",
    url: https://www.cambridge.org/core/journals/nagoya-mathematical-journal/article/89C47A4810A6F02971D393FD1FE44653
  - "Binyamini–Masser, Effective André–Oort for non-compact curves in
    Hilbert modular varieties, arXiv:2101.06412 / CRAS 2021"
  - "Yafaev, The André–Oort conjecture for Hilbert modular surfaces"
  - "Claim: richardson-pvs-valid-but-mss-not-pvs-invariant (research/notes/
    literature-check-3-new-approaches.md)"
first-step: NONE. The orbit/nilpotent/Richardson identification of the magic
  subspace fails (semisimple centraliser), and the nine-square condition is
  not a PVS invariant, so the PVS machinery cannot express the MSS. The
  transcendence/André–Oort conclusion would overprove.
speculation: (as originally written) "the link between the SL₃-orbit
  structure and the Hilbert modular variety for Q(√5) needs establishment."
  It could not be established; it does not exist in the literature and the
  MSS does not map to a Q(√5) Hilbert modular variety through any
  established construction.
```
