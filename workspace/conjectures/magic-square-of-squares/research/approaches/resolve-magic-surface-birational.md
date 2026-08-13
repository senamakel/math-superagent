```approach
id: resolve-magic-surface-birational
idea: Resolve the 256 singular points of the magic square surface X ⊂ P⁸
  (Michaud-Rodgers 2019), intersect with the eight square-entry quadrics to
  obtain a smooth projective surface S̃ parametrising the full 3×3 MSS, and
  determine its birational type (Kodaira dimension κ).  Each possible κ
  carries a specific Diophantine tool never applied to this problem — and
  the correct tool is determined by a finite exact computation, not by
  guesswork.

  This approach is NOT the same as the parked `kodaira-dimension-general-type`
  candidate, which blithely assumes the affine parametrisation can be
  compactified in weighted projective space without knowing the singular
  locus.  Here the singularities are KNOWN: 256 of them, at isolated points
  of X, from Michaud-Rodgers' 2019 explicit computation of the magic variety
  (a surface, with no lines, 256 singular points over C).  The resolution of
  these singularities is well-defined (they are quotient singularities from
  the S₃ action on the parametrisation — the variety is the GIT quotient of
  the space of 3×3 matrices by the diagonal torus plus the permutation group
  of the magic square symmetries).  Once resolved, S̃ is smooth, and the
  eight square-entry conditions become eight divisors on S̃.  Computing the
  canonical class of S̃ via adjunction on the blow-up of P⁸ determines κ(S̃).

  Cases and their Diophantine consequences:
  - κ = −∞ (rational/ruled): S̃ is birational to P² or a P¹-bundle; the MSS
    problem has a rational parametrisation — existence would be proved by
    writing it down.
  - κ = 0 (K3, Enriques, abelian): S̃ has trivial canonical bundle; the
    Brauer-Manin obstruction on S̃ can be computed (S̃ is smooth, unlike the
    original affine V); this is the one case where integral BM or
    transcendental BM can actually be evaluated.
  - κ = 1 (properly elliptic): S̃ fibres over a curve with elliptic fibres;
    the MSS problem reduces to rational points on the base curve and ranks of
    the fibres — a descent problem of known type.
  - κ = 2 (general type): S̃ has ample canonical bundle; Bombieri-Lang
    (conditional but widely believed for surfaces) implies finiteness of
    rational points; combined with GFP height bounds, the finite set is
    effectively computable.

  The computation of κ(S̃) is a finite exact computation: resolve the 256
  singularities of X explicitly (they are toric or quotient singularities),
  blow up P⁸ along the singular locus, take the proper transform of X, and
  compute the canonical class on the resulting smooth surface.  This is
  heavier than a Gröbner basis but is algorithmic: the singularities are
  isolated and their local equations are known (from the S₃-action on the
  magic subspace).  The payoff is not one conditional result but FOUR — one
  for each possible κ — and determining WHICH κ holds is itself a structural
  result about the MSS that has been open for 30 years.
status: proposed
mechanism: The approach exploits a structural fact that every previous
  Diophantine attack on the MSS has ignored: the projective geometry of the
  bare magic variety X is KNOWN (Michaud-Rodgers 2019), and its
  singularities are a finite computable set.  All previous approaches
  (Brauer-Manin, Chabauty, Faltings, GFP uniformity) treat the MSS as a
  system of Diophantine equations without first understanding the geometry
  of the solution space.  Computing κ(S̃) fills that gap and then tells
  you which Diophantine tool to use — the opposite of the usual approach
  (pick a tool and hope the geometry fits).
first-step: |
  Three concrete moves, in order:

  1. **Get the explicit equations of X ⊂ P⁸ from Michaud-Rodgers.**
     Download or reconstruct the 7 homogeneous line-sum equations defining
     the magic variety in P⁸ (coordinates are the 9 entries x₀₀, …, x₂₂).
     This is a surface of degree 6 with 256 ordinary double points
     (conjectured; verify by checking that the singular locus is 0-dimensional
     of degree 256).  Write a sympy script that computes the singular locus
     explicitly — the Jacobian of the 7 equations drops rank at 256 points.
     Verify against Michaud-Rodgers' count.

  2. **Intersect with the 8 square-entry quadrics.**
     The full nine-square surface S (before resolution) is X ∩ V(Q₁,…,Q₈)
     where Qᵢⱼ = xᵢⱼ − sᵢⱼ² = 0 (the sᵢⱼ are auxiliary variables, eliminated
     by taking the radical of the ideal).  In practice: substitute the magic
     parametrisation (c, u, v) into the square conditions aᵢ = sᵢ² and
     eliminate sᵢ.  This gives a system of polynomial equations in c, u, v.
     The resulting affine surface V ⊂ A³ is the object whose smooth
     compactification S̃ we need.  Compute a Gröbner basis for V to determine
     its dimension (should be 2) and degree.

  3. **Compute a smooth compactification and its canonical class.**
     Extend V to a projective surface in weighted projective space (weights
     determined by the degrees of c, u, v in the parametrisation).
     Desingularise via blow-ups at the singular points.  Compute K_{S̃} via
     the adjunction formula K_{S̃} = (K_{ambient} + S̃)|_{S̃} after each blow-up.
     Determine κ(S̃) = −∞, 0, 1, or 2 by computing the Iitaka dimension of
     K_{S̃}: if K_{S̃} is not effective → κ = −∞; if mK_{S̃} ∼ 0 for some m →
     κ = 0; if K_{S̃}·H = 0 for ample H → κ ≤ 1; if K_{S̃}·H > 0 → κ = 2.

  Guard: steps 2 and 3 are heavy symbolic computations and may exceed what
  sympy can handle in one session.  The fallback is to compute the Kodaira
  dimension using the known structure of X (step 1) plus the fact that the
  square-entry conditions are eight quadrics on P⁸ — their intersection with
  the degree-6 surface X generically gives a finite set, so S is a curve or
  a finite set modulo the parametrisation.  If S is a curve, compute its
  genus; if genus 0, the MSS has a rational parametrisation; if genus 1, it's
  an elliptic curve; if genus ≥ 2, Faltings applies.  This is a strictly
  simpler computation and may already close the problem.
precedent:
  - Michaud-Rodgers, "The magic square variety" (Warwick talk, 2019):
    X ⊂ P⁸ is a surface with 256 singular points and no lines.  This is the
    ONLY source that establishes the projective geometry of X; all other MSS
    work treats it as a Diophantine system without studying the solution
    variety as an algebraic variety.  The run's claim
    `magic-variety-is-surface-no-lines` captures this.
  - Bremner II (2001): the K3 surface S for the six-square configuration III;
    NS(S,Q) of rank 12, S(Q) nonempty.  The nine-square surface S̃ is a
    subvariety of (a blow-up of) S — the three extra square conditions cut
    out a 0-dimensional subscheme on S, so S̃ is birational to S but with
    additional structure at the basepoints.
  - The GFP theorem (Garcia-Fritz-Pastén 2026, this run claims
    `bremner-conjecture-proved` and `gfp-2021-theorem-6-1-doubled-points-in-scope`):
    if κ = 2 (general type) and Bombieri-Lang holds, the set of rational
    points is finite; the GFP theorem then bounds the height of those
    finitely many points in terms of the rank of the Robertson curve, giving
    an effective search bound (conditional on BL + uniform rank bound).
  - The resolution of quotient singularities is algorithmic (toric methods
    for cyclic quotient singularities; GIT for reductive quotients).  The
    256 singularities of X come from the S₃-action on the parametrisation
    (permuting the magic square's rows and columns) — they are quotient
    singularities of type A_n or D_n, which are resolved by a well-known
    sequence of blow-ups.
  - NOT subsumed by any approach in APPROACHES.md.  The parked
    `kodaira-dimension-general-type` approach assumes the affine
    parametrisation can be compactified naively; this approach uses the
    KNOWN singular locus of X (Michaud-Rodgers) to guide the
    compactification, making it algorithmic rather than speculative.
    No other approach studies the solution variety as a projective variety
    with known singularities.
speculation: The birational type of S̃ is not known.  If κ = 2, the
  conditional finiteness result is the strongest partial result available
  for the MSS (it reduces the problem to a finite search).  If κ ≤ 1, the
  classification enables a specific Diophantine attack — e.g., if κ = 0 and
  S̃ is a K3, its Brauer group can be computed (smooth S̃ has a computable
  Br, unlike the singular affine V).  The risk is that the computation of
  κ(S̃) is too heavy for the available symbolic tools; the fallback (computing
  the genus of the curve S obtained by intersecting X with the eight quadrics)
  is a lighter computation with a similar payoff structure.
```