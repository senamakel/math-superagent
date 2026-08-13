# Approach: Elimination ideal / Gröbner basis over Z

```approach
idea: Eliminate the nine square variables s_i from the system in
  Z[c,u,v,s_1,...,s_9] consisting of the 9 norm-to-square equations
  entry_i(c,u,v) - s_i^2 = 0 together with the 7 line-sum conditions
  (already encoded by the parametrisation (c,u,v)).  The elimination ideal
  J = I(V) ∩ Z[c,u,v] either contains 1 (no integer solutions), defines a
  surface, or defines curves.  A Gröbner/resultant computation over Z would
  then contradict the claimed non-existence, or reduce the problem to fewer
  variables.

status: refuted
precedent:
  - The parametrisation (c,u,v) and its completeness: problem.md; this run's
    oracle (code/out/oracle_output.txt, status checked) — the grid
    [c+u, c-u-v, c+v; c-u+v, c, c+u-v; c-v, c+u+v, c-u] is the most general
    3x3 magic square, so the 7 line-sum equations are already solved by the
    parametrisation and carry no further (c,u,v) content.
  - Bremner, "On squares of squares", Acta Arith. 88 (1999) 289-297: MSS exist
    over proper extension fields (over Q(sqrt3,sqrt133), degree 4), and the
    entries are integral there (c,u,v integral, s_i in O_K).  Source:
    research/sources/bremner-on-squares-of-squares-1999.full.md.
  - Michaud-Rodgers (Warwick 2019 talk/project): the magic-square variety X in
    P^8 is a surface with 256 singular points; adjoining the square conditions
    keeps it singular.  Source:
    research/sources/michaud-rodgers-warwick-talk-2019.full.md, and the run's
    claim magic-variety-is-surface-no-lines.  This is the exact algebraic
    geometry where a Gröbner elimination would be computed.

killed-by: The square conditions are VACUOUS, and this kills the ideal over Z too,
  not just over an algebraically closed field.  For every (c,u,v) in Qbar^3,
  each entry entry_i(c,u,v) is an affine linear form and always has a square
  root s_i = sqrt(entry_i) in Qbar.  So the projection (c,u,v,s) -> (c,u,v)
  is DOMINANT: its image is all of A^3, the Zariski closure of the projection
  is A^3, and the Qbar-elimination ideal J_Ȳ = I(V) ∩ Qbar[c,u,v] = (0).

  Base-changing to Qbar can only shrink J under the natural map
  (J_Z ⊗ Qbar) ⊆ J_Ȳ: any f ∈ J_Z ⊗ Qbar ⊂ Qbar[c,u,v] that came from
  J_Z = I(V)∩Z[c,u,v] also lies in J_Ȳ = (0).  Since Z[c,u,v] is a free
  (flat) Z-module, the map J_Z -> J_Z ⊗ Qbar is injective.  Therefore
  J_Z = (0).  The elimination ideal over Z is EXACTLY the zero ideal:

     * there are NO nonzero polynomial invariants in (c,u,v) alone that every
       integer MSS must satisfy (this kills the pre-existing proposed
       approach groebner-elimination-nine-square's branch (c)),
     * J does not contain 1 (kills branch (a), the would-be proof of
       non-existence).

  The proposed trichotomy "contains 1 / surface / curve" is false — none of
  the three holds: V(J) = A^3 (dimension 3, neither a surface nor a curve),
  and 1 ∉ J.  Concretely 1 ∉ J is forced independently by the extension-field
  hinge: a full nine-square MSS exists over O_K (K = Q(sqrt3,sqrt133),
  Bremner 1999), i.e. V has a point over the flat Z-algebra O_K with (c,u,v)
  integral and s_i in O_K; substituting that point into any ideal element that
  equalled 1 would give 1 = 0, so 1 ∉ J over Z as well as over Qbar.

  The whole difficulty of the problem is INTEGRAL / RATIONAL square roots
  (positivity, distinctness, integrality of each s_i), which no ideal over a
  closure, nor any Z-flat elimination, can see: the elimination ideal is (0)
  over Z and over Qbar alike.  The obstruction is arithmetic (rational square
  roots in an additive configuration), not algebraic variety structure — the
  same separation-failure (Q vs Qbar / vs O_K) that sinks every purely
  algebraic-geometric attack, e.g. integral-brauer-manin-nine-square.

first-step was executed conceptually (code/out/candidate_verdict_math.py):
  for several (c,u,v) all 9 entries are affine forms; the projection is
  dominant; dominance is immediate.  Computing a literal Gröbner basis of J
  over Z (Singular/Macaulay2/sympy domain=ZZ) would only re-return J=(0) and
  teach nothing; it is not worth the compute.  This refutes the pre-existing
  proposed approach groebner-elimination-nine-square: branch (a) "1 ∈ J" is
  forbidden by the extension-field MSS (over O_K), branch (c) "nonzero proper
  ideal with arithmetic generators" is forbidden by J_Z = (0) via faithful
  flatness, and stationing over Z instead of Qbar changes nothing because
  elimination over a flat base sees the same (Zariski) closure.  The only
  computing that survives the elimination is the 2-cover / elliptic structure
  of the doubled-point x-coordinates, which is the subject of
  mordell-weil-sieve-robertson and uniform-height-bound-elliptic-ap — not of
  the elimination ideal.
```

## Why this fails (reader's digest)

The proposal's trichotomy rests on a category error. Over an algebraically closed
field, "is a perfect square" is *not an algebraic condition* — `s² = e` is
solvable for `s` for any `e`. Eliminating the `s_i` therefore throws away the
entire problem, and — because `Z → Q̄` is flat, so elimination over Z sees the
same Zariski closure — there are no nonzero `(c,u,v)`-only polynomial
invariants at all, and `1 ∉ J`. The arithmetic of MSS lives in the difference
between having a *rational* square root and *any* square root; that difference is
invisible to elimination ideals whether over Z or over Q̄. This is the same
reason the run's `integral-brauer-manin-nine-square` was refuted: the variety is
singular/non-proper and the arithmetic square-root condition is not captured by
algebraic geometry over a closure.

## Sources considered and rejected

- Gröbner-basis papers on Sudoku/magic squares (e.g. Arnold, "Gröbner Basis
  Representations of Sudoku", Math. Mag. 2010) model *linear/algebraic*
  constraints, not the "is a square" condition; not applicable.
- M. Helms, magicSquareOfSquares drafts: derive the linear parametrisation
  `a²=2e²-i², b²=2e²-h², ...` by Gaussian elimination — that is the same
  (c,u,v) parametrisation in squared form, and it keeps three independent
  squares; it does not and cannot eliminate the square-root condition.  This
  confirms the parametrisation, then stops.
- Cain arXiv:1908.03236 uses elimination/parametrisation over finite fields and
  rings Z/nZ (finite-field enumeration), NOT an elimination ideal over Z; its
  reformulation (quartics over abelian extensions) is the run's
  cain-quartic-gaussian-reformulation and does not advance the rational case.
- The Montclair thesis (Hengeveld) uses Gröbner to generate MSS over F_p; again
  finite-field, where "square mod p" is a residue check, not the rational case.

None of these applies a Gröbner/elimination ideal over Z to the rational MSS and
none suggests it can work; the algebraic reason is the vacuity above.
