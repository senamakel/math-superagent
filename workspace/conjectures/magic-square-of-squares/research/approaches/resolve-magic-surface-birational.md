```approach
id: resolve-magic-surface-birational
idea: Resolve the 256 singular points of the magic-square-of-squares variety
  X ⊂ P⁸ and determine the Kodaira dimension κ of the smooth model X̃.  The
  answer is a finite, exact, computable structural fact that has never been
  obtained — and whichever of the four values of κ holds, it points to a
  specific Diophantine tool, so the computation replaces the 30-year
  guessing game of "pick a tool and hope the geometry fits" with "read the
  geometry off and use the tool it dictates".

  Setup (correct reading of Michaud-Rodgers): coordinates x₀₀,…,x₂₂ on P⁸
  are the SQUARE ROOTS of the nine entries; the 8 line-sums of the entries
  xᵢⱼ² are equal, giving 7 independent homogeneous QUADRATIC equations.  The
  zero set X is a surface (Hilbert polynomial degree 2), with 256 singular
  points over C (each with three zero coordinates), and contains no lines.
  So X already parametrises ALL magic squares whose entries are squares —
  there are no extra square conditions to impose; the coordinate change
  absorbs them.  The MSS problem over Q is: does X(Q) contain a point with
  no zero coordinate whose nine values xᵢⱼ² are distinct positive integers?
  (Positivity/distinctness are Zariski-open conditions, so they do not
  affect the birational type.)

mechanism: Every previous Diophantine attack treated the MSS as a system of
  equations and fought its singularities implicitly.  Bremner II (2001)
  computed the Néron-Severi group of a six-square K3 S (κ=0, S(Q) nonempty);
  Brauer-Manin on S is dead for that reason.  My own integral-Brauer-Manin
  proposal was refuted because the nine-square affine V/Z is singular and
  non-proper — but research's refutation itself named the missing step:
  "Re-proposing requires first finding a smooth projective model of the MSS
  variety with a computable Br, which no source provides."  That smooth
  model is X̃, obtained by resolving the KNOWN 256 singular points of X.
  The resolution is algorithmic (the singularities come from the S₃ action
  on the parametrisation, so they are cyclic quotient singularities, type
  Aₙ/Dₙ, resolved by a standard sequence of blow-ups), not blind.

  Then κ(X̃) is decisive, because each case has a tool that has never been
  correctly applied to the MSS precisely because the smooth model was never
  built:

  - κ = 2 (general type): K_{X̃} ample.  Bombieri-Lang (conjectural for
    surfaces over Q, but the standard structural hypothesis) gives finiteness
    of X̃(Q); the Garcia-Fritz-Pastén height-uniform theorem (this run's
    `bremner-conjecture-proved`, applies verbatim to the MSS AP by
    `gfp-2021-theorem-6-1-doubled-points-in-scope`) then bounds the heights
    of those finitely many points, conditional on a rank bound on the
    Robertson curve — turning non-existence into a finite, in-principle
    checkable computation.
  - κ = 0 (K3/Enriques): X̃ has trivial canonical bundle and is SMOOTH, so
    Br(X̃)/Br(Q) is computable where Br of the singular affine V was not.
    This is exactly the obstruction my integral-Brauer-Manin proposal wanted
    but could not reach; the resolution is the missing step that unblocks it.
  - κ = 1 (properly elliptic): X̃ fibres over a curve with elliptic fibres;
    the MSS reduces to base-curve points plus fibre ranks — a descent problem
    of known type.
  - κ = −∞ (rational/ruled): X̃ ≅ P² or a P¹-bundle up to birational
    equivalence; the MSS would admit a rational parametrisation, and
    existence would be decided by writing it down.

  The result is a genuine partial result in ALL FOUR cases — not "the
  conjecture follows" but "here is the birational type of the solution
  space, and therefore the correct next tool" — which is exactly the stated
  deliverable for an open problem.
status: adopted
first-step: |
  Tool_builder can start today.  Three concrete, checkable moves:

  1. **Reconstruct X and verify the 256 singular points (exact, sympy).**
     Define P⁸ coordinates x₀₀,…,x₂₂; define the 8 line-sums
     L_r = Σⱼ xᵢⱼ² (3 rows), L_c (3 columns), L_d, L_a (2 diagonals); set
     the 7 independent differences L_i − L_0 = 0.  Compute the singular
     locus: the 7×9 Jacobian of these quadrics must drop rank.  Solve
     (or confirm by Gröbner/primary decomposition) that the singular locus
     is 0-dimensional with degree 256, and that each singular point has
     exactly three zero coordinates.  Michaud-Rodgers is a TALK (claim
     `magic-variety-is-surface-no-lines`, status: asserted) — this step
     turns it into a checked claim, and the 256-point count is the first
     concrete thing the whole approach rests on.

  2. **Identify the local singularity type at one singular point.**
     Linearise the 7 quadrics at a representative singular point (say the
     one with x₁₂=x₂₁=x₂₂=0 up to symmetry); the tangent cone is a rank-
     deficient system of quadrics in 3 variables.  Determine the quotient
     singularity type (cyclic Aₙ or dihedral Dₙ) from the S₃-stabiliser of
     the point.  This fixes the blow-up recipe for step 3.

  3. **Resolve and compute K_{X̃}.**
     Blow up P⁸ along the singular locus, take the proper transform X̃ of X,
     and compute the canonical class K_{X̃} = (K_{P⁸}(X̃))|_{X̃} by adjunction,
     tracking the exceptional divisors.  Compute the Iitaka dimension of
     K_{X̃}: not effective → κ=−∞; mK_{X̃} ∼ 0 for some m → κ=0;
     K_{X̃}·H = 0 for ample H → κ≤1 (check elliptic fibration); K_{X̃}·H > 0
     → κ=2.  Report κ(X̃) with the computation that produced it.

  Fallback if the full resolution is too heavy: the eight line-sum-of-squares
  quadrics on P⁸ already force X to be a surface, and its canonical class
  can be bounded by resolving only the singularities that are needed for
  the adjunction computation (isolated quotient singularities contribute
  only their discrepancy).  If even that is too heavy, a lighter first
  result is the degree and geometric genus of X̃, which already distinguishes
  κ=2 (p_g > 1 and growing plurigenera) from κ≤1.
precedent:
  - Michaud-Rodgers, "Magic Squares of Squares" (Warwick talk, 2019):
    X ⊂ P⁸ is a surface with 256 singular points over C (three zero
    coordinates each) and contains no lines.  Claim
    `magic-variety-is-surface-no-lines`, status asserted (talk-level) — this
    run must verify it, which is exactly first-step 1.
  - Bremner II, "On squares of squares II", Acta Arith. 99 (2001) 289-308:
    the six-square K3 S with NS(S,Q) of rank 12 and S(Q) nonempty (claim
    `k3-ns-rank-12-not-maximal`); κ(S)=0, so Brauer-Manin on S is vacuous.
    The nine-square X is a subvariety; X̃ is the object the K3 approach needed
    but never built.
  - Colliot-Thélène-Xu (Compositio 145 (2009)) / Browning-Matthiesen
    (Ann. ENS 50 (2017)): integral Brauer-Manin is computable only for
    smooth homogeneous spaces / normic hypersurfaces.  This run's refutation
    of `integral-brauer-manin-nine-square` explicitly names "a smooth
    projective model of the MSS variety with a computable Br" as the missing
    prerequisite — which is exactly X̃ in the κ=0 case.
  - Garcia-Fritz-Pastén (arXiv:2604.04850, 2026) + Dimitrov-Gao-Habegger
    (Ann. Math. 194 (2021)): uniform Mordell-Lang; height-uniform bounds on
    APs of x-coordinates (claims `bremner-conjecture-proved`,
    `gfp-2021-theorem-6-1-doubled-points-in-scope`).  Supplies the
    effectiveness needed to make the κ=2 (Bombieri-Lang) case a finite
    search rather than a bare finiteness statement.
  - Resolution of cyclic quotient singularities: toric/orbifold blow-ups,
    classical (type Aₙ/Dₙ surface singularities; Reid's chapters in the
    standard references).  Algorithmic.
  - NOT subsumed by any approach in APPROACHES.md.  It is the sharpening of
    the parked `kodaira-dimension-general-type` candidate — which naively
    homogenises the affine parametrisation without knowing the singular
    locus — using the KNOWN 256-point singular structure of X.  It is the
    smooth-model step that the refuted `integral-brauer-manin-nine-square`
    and `brauer-manin-k3-surface` approaches both lacked.  No source has
    computed κ(X̃) or resolved X.
speculation: The birational type κ(X̃) is unknown and is the thing being
  computed — that is the point.  The claim that the 256 singularities are
  cyclic quotient singularities from the S₃ action is a hypothesis to verify
  in first-step 2.  The Bombieri-Lang step in the κ=2 case is conditional
  (BL is open for surfaces over Q), and the GFP effectiveness step is
  conditional on a uniform rank bound; both conditionals are labelled as
  such and the computation of κ(X̃) itself is unconditional.  The risk is
  that steps 2-3 exceed sympy's capacity; the fallback (degree and geometric
  genus of X̃) is a lighter computation with the same κ=2-vs-κ≤1 dichotomy.
```