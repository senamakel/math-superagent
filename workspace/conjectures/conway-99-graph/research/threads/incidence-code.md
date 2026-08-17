# Thread: incidence p-rank / SNF of the triangle geometry

```thread
id: thread-incidence-code
question: Is the incidence p-rank / SNF of the triangle geometry a live
  99-vs-243 separator, or a parameter-determined invariant that cannot separate
  them?
status: dead
rests-on: incidence-code-of-triangle-geometry (approach, grounded), c4, c5,
  code/out/incidence_p_rank.captured.txt,
  code/out/incidence_prank_determinism.captured.txt
blocked-by:
deaded-by: directive 23, Route 8. Gate ANSWERED in incidence_prank_determinism.captured.txt
  (the sharpest reasoning of the run): the 2-rank is NOT parameter-determined —
  the naive spectral-multiplicity rule is VIOLATED on doily and GQ(2,4),
  Assmus-Key leaves STS p-ranks varying with the system — so it COULD separate
  99 from 243. BUT it is UNPROVABLE this way: a 99 value could only be settled
  by an actual 99 system, i.e. the very graph whose existence is in question
  (circular). The subtlety: within-family variation (rook rank_2=5 vs BvLS 243)
  is NOT evidence against parameter-determinism, since such an invariant varies
  across parameter points anyway; only a same-parameter split counts, and the
  one test available (Shrikhande vs rook(4), both srg(16,6,2,2)) gives none
  (rank_2(A+I)=16=16, rank_2(N)=16=16). Do not re-open.
next:
```

```claim
id: incidence-2rank-not-parameter-determined-but-unprovable
statement: The incidence 2-rank of the triangle geometry's point-x-triangle
  matrix N is NOT determined by the parameters, but is UNPROVABLE as a 99-vs-243
  separator this way (code/out/incidence_prank_determinism.captured.txt, exact
  arithmetic via lib.srg). The naive spectral-multiplicity rule for rank_2(A+I)
  is VIOLATED on doily srg(15,6,1,3) (rule predicts 1, actual 5) and GQ(2,4)
  srg(27,10,1,5) (predicts 1, actual 7), and Assmus-Key leaves STS 2-ranks
  varying with the system, so rank_2(N) could in principle separate 99 from 243.
  BUT: within-family variation (rook rank_2(N)=5 defect 4 vs BvLS 243 full) is
  NOT evidence against parameter-determinism (a parameter-determined invariant
  varies across parameter points too); only a SAME-parameter split counts, and
  the one test available — Shrikhande vs rook(4), both srg(16,6,2,2), cospectral
  non-isomorphic — gives none (rank_2(A+I)=16=16, rank_2(N)=16=16). A 99 value
  could only be settled by an actual 99 system, i.e. the very graph whose
  existence is in question (circular). Line closed as unusable (directive 23,
  Route 8). Also records the premise correction: the full-rank 243 is rank_2(N)
  (243x891 incidence matrix), NOT rank_2(A+I) which is 133 for BvLS.
hypotheses: N = point x triangle incidence matrix, NN^T = (k/2)I + A; the
  Shrikhande/rook(4) pair is the only same-(16,6,2,2) cospectral non-isomorphic
  pair available.
holds-here: yes — the gate is computed at the exact parameters of every family
  member and the same-parameter control pair.
status: checked (exact integer arithmetic; capture
  code/out/incidence_prank_determinism.captured.txt).
bearing: the incidence p-rank line cannot settle 99 absent the graph itself; it
  is a genuine but unprovable-this-way invariant. Do not re-open.
anchor: code/out/incidence_prank_determinism.captured.txt,
  research/approaches/incidence-code-of-triangle-geometry.md
contradicts: none
answers: incidence-prank-parameter-determinism
```

## Why this is a phase-4 target

The incidence matrix N of the triangle geometry (99 points × 231 lines for the
putative Conway graph) is not the adjacency matrix: it records which triangles
exist. The two refuted code routes (`macwilliams-binary-code-arc`,
`higman-module-restriction`) were both functions of A's *spectrum* and died
parameter-determined. N is different in kind, and its p-ranks are the classical
invariants that distinguish non-isomorphic Steiner triple systems of the same
order (Assmus–Key). The binding identities are NN^T = 7I + A and
N^T N = 3I + C3; over F_3, 7 = 1 so NN^T = I + A, and every column has weight
3 = 0, putting the column space in the even-weight subspace 1^⊥ of dimension 98
— a constraint with no adjacency-matrix analogue.

## The gate the directive orders

The measured rank-deficiency sequence 4, 5, 6 sits over rook/doily/GQ(2,4),
which have *different* v, so it may simply track v and be parameter-determined.
BvLS (same μ=2, λ=1 family as 99) has full rank_2, so the rank is not a fixed
function of v alone — but that does not yet prove it separates two systems of
the *same* (v,k,1,2). Settle that before any 99 conclusion.

## Falsifiers

- A proof or computed pair of systems with identical (v,k,1,2) and different
  rank_2(N) makes the invariant genuinely live for 99.
- A proof that NN^T = 7I+A with column weight 3 forces rank_2(N) (and rank_3(N))
  from the parameters alone refutes the line, exactly like the two A-based
  routes it was meant to avoid.
