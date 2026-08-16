# Thread: incidence p-rank / SNF of the triangle geometry

```thread
id: thread-incidence-code
question: Is the incidence p-rank / SNF of the triangle geometry a live
  99-vs-243 separator, or a parameter-determined invariant that cannot separate
  them?
status: open
rests-on: incidence-code-of-triangle-geometry (approach, grounded), c4, c5,
  code/out/incidence_p_rank.captured.txt,
  code/out/incidence_identity_check.captured.txt
blocked-by:
next: FIRST settle parameter-determinism (directive 18). Measured: rook rank_2=5
  /rank_3=5, doily 10/10, GQ(2,4) 21/21 (rank deficiency 4,5,6); BvLS rank_2=243
  (full), rank_3=231. If the deficiency sequence is forced by (v,k,lambda,mu)
  alone, it cannot separate 99 from 243 and the line dies exactly like
  macwilliams-binary-code-arc / higman-module-restriction. Assmus-Key says the
  p-rank of an STS genuinely varies with the system, and N is bound by
  NN^T=7I+A (mod p, 7=1 over F_3) with every column of weight 3, so it may be
  live — but this must be SHOWN (two systems with the same (v,k,1,2) but
  different rank_2(N), or a proof the rank is not spectrum-determined) before
  betting on it. Run every step against rook(3) and bvls_graph() through
  code/lib.srg.
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
