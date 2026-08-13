```approach
id: kodaira-dimension-general-type
idea: Compute the Kodaira dimension of the full nine-square surface (the
  compactification of the affine variety parametrising all 3×3 magic
  squares of squares).  If the surface is of general type (κ = 2), then
  by the Bombieri–Lang conjecture — proved for surfaces over function
  fields and strongly supported for number fields — the rational points
  are not Zariski dense.  Combined with the known computational lower
  bounds (Buell's 25·10²⁴ on the hourglass, Morgenstern's 8-digit
  smallest entry), finiteness of rational points on the MSS surface
  reduces the problem to a finite check.
mechanism: The nine entries are linear forms Lᵢⱼ(c, u, v) in the
  parametrisation.  Substituting c = e² and requiring each entry = sᵢⱼ²
  gives 8 equations (the centre is e² by definition) in variables
  (e, u, v, s₁, …, s₈) with an overall scaling.  Eliminate the sᵢ by
  taking the radical of the ideal ⟨Lᵢ − sᵢ²⟩, giving an affine surface
  V ⊂ A³_{(e,u,v)} defined by polynomial equations in three variables.
  Compactify V to a smooth projective surface S by taking the closure
  in a suitable weighted projective space (the degrees of the defining
  equations determine the weights).  Compute the canonical sheaf ω_S
  via the adjunction formula for complete intersections.  If ω_S is big
  (its self-intersection > 0 and its global sections define a birational
  map), then κ(S) = 2.  The key computation is: what is the degree
  multiset of the defining equations after homogenisation, and does the
  adjunction formula yield an ample canonical divisor?
status: parked-behind-blocking-question
first-step: PARKED per directive 10/11 — do not work on this until the GFP-x2P
  blocking question is answered in `code/out/gfp_x2p_answer.md`. The approach
  may be viable but no fifth approach before the blocking question.
  parametrisation, the nine entries are:
    a₁ = e² + u,       a₂ = e² − u − v,  a₃ = e² + v,
    a₄ = e² − u + v,   a₅ = e²,          a₆ = e² + u − v,
    a₇ = e² − v,       a₈ = e² + u + v,  a₉ = e² − u.
  Each aᵢ must be a perfect square: aᵢ = sᵢ².  Eliminate s₁, …, s₉
  by treating the system as:  u = s₁² − e²,  v = s₃² − e², and the
  remaining six equations become polynomial relations among s₁, s₃, e
  and the other squares.  Write these explicitly, then homogenise by
  introducing a projective weight for e, u, v.  Pass the ideal to
  sympy/Singular to compute a Gröbner basis and the Hilbert polynomial.
  From the Hilbert polynomial, compute the canonical divisor and
  determine whether K_S is big (intersection K_S·H > 0 for an ample H
  and h⁰(nK_S) ∼ n²).  This is a finite, exact computation.
precedent: Bombieri–Lang conjecture (1970s): on a variety of general type
  over a number field, rational points are not Zariski dense.  Proved for
  surfaces over function fields (Noguchi, 1981).  For surfaces over
  number fields the conjecture is open in general but is widely believed
  and has been verified for large classes.  The computation of Kodaira
  dimension for varieties defined by complete intersections is classical
  (adjunction formula, Hartshorne).  The MSS surface has never been
  studied from the birational-geometry perspective — the literature
  focuses on the K3 of Bremner II (six-square configuration) which is
  NOT of general type (K3 has κ = 0).  The full nine-square surface
  imposes four more square conditions and may well be of general type.
  NOT subsumed by the integral Brauer–Manin approach (which studies the
  Brauer group, not the canonical ring) or the K3 approach (which
  studies a different surface).
speculation: The surface could have κ = −∞ (rational), κ = 0 (K3/Enriques/
  abelian), κ = 1 (elliptic fibration), or κ = 2 (general type).  If
  κ = 2, the Bombieri–Lang conjecture applies and the finiteness result
  follows (conditional on the conjecture).  If κ = 0 or 1, the surface
  admits a fibration whose rational points can be studied by descent.
  Either way, determining κ(S) is a structural result about the MSS
  that has not been obtained in 30+ years of work on this problem.
  The computation is finite and exact (Gröbner basis in weighted
  projective space).
```