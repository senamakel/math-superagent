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
    over proper extension fields (over Q(sqrt3,sqrt133), degree 4).  Source:
    research/sources/bremner-on-squares-of-squares-1999.full.md.
  - Michaud-Rodgers (Warwick 2019 talk/project): the magic-square variety X in
    P^8 is a surface with 256 singular points; adjoining the square conditions
    keeps it singular.  Source:
    research/sources/michaud-rodgers-warwick-talk-2019.full.md, and the run's
    claim magic-variety-is-surface-no-lines.  This is the exact algebraic
    geometry where a Gröbner elimination would be computed.

killed-by: The square conditions are VACUOUS over an algebraically closed (or
  fraction) field.  For every (c,u,v) in Qbar^3, each entry entry_i(c,u,v) is
  an affine linear form and always has a square root s_i = sqrt(entry_i) in
  Qbar.  Hence the rational map (c,u,v,s_i) -> (c,u,v) is dominant, the image
  of V is all of A^3, and the elimination ideal
  J = I(V) ∩ Qbar[c,u,v] = (0).  V(J) = A^3: the proposed trichotomy
  "contains 1 / surface / curve" is false — none of the three holds.

  The two concrete consequences:
  1. J cannot contain 1: if it did, no solution would exist over Qbar, but a
     full nine-square MSS provably exists over Q(sqrt3,sqrt133) (Bremner
     1999), giving a Qbar-point and hence a prime containing J, so J is not
     the unit ideal.  (Even over Z this forces the Z-linear combination that
     would equal 1 to involve the s_i's square relations in a way no
     (c,u,v)-only ideal can express.)
  2. J is neither a surface nor a curve: V(J) = A^3, dimension 3.

  The whole difficulty of the problem is INTEGRAL / RATIONAL square roots
  (positivity, distinctness, integrality of each s_i), which no ideal over an
  algebraically closed field can see.  An elimination ideal over Z[c,u,v]
  captures exactly the Zariski closure over Qbar — i.e. nothing — and cannot
  distinguish Q from Qbar, which is precisely the separation this run's
  extension-field-mss-exist hinge says any valid argument must perform.
  Over an algebraically closed field the system is locally solvable at every
  prime power (the run's claim phi-padic-no-obstruction + locally-solvable
  fact); the obstruction is arithmetic (rational square roots in an additive
  configuration), not algebraic variety structure.

first-step was executed conceptually (code/out/candidate_verdict_math.py):
  for several (c,u,v) all 9 entries are affine forms with Qbar square roots;
  dominance is immediate.  Computing a literal Gröbner basis of J over Z
  would only re-return J=(0) and teach nothing; it is not worth the compute.
```

## Why this fails (reader's digest)

The proposal's trichotomy rests on a category error. Over an algebraically closed
field, "is a perfect square" is *not an algebraic condition* — `s² = e` is
solvable for `s` for any `e`. So eliminating the `s_i` over Z (whose geometric
content is the same as over Q̄) throws away the entire problem. The arithmetic of
MSS lives in the difference between having a *rational* square root and *any*
square root; that difference is invisible to elimination ideals. This is the same
reason the run's `integral-brauer-manin-nine-square` was refuted: the variety is
singular/non-proper and the arithmetic square-root condition is not captured by
algebraic geometry over the closure.

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
