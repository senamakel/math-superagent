# Approach: Fisher-equality defect of the seeded partial STS (global line budget)

```approach
idea: The triangle geometry of a putative srg(99,14,1,2) is a partial Steiner
  triple system on 99 points with 231 lines of size 3 and 7 lines through every
  point — exactly 693 point-line incidences. For a (v=99, b, r=7, block size 3)
  partial design, Fisher's inequality gives b >= v (=99) and the exact triple
  count b = vr/3 = 231 is forced by the line-size and replication, so the design
  sits AT the Fisher bound. The n3 seed — two disjoint lines (triangles) whose
  point sets are joined by exactly two collinear cross-pairs — perturbs the
  design: each of the two cross-collinear pairs {a,d}, {b,e} must already lie on
  a line distinct from the two seed lines, so the seed installs extra lines and
  extra point-line incidences. The claim: forcing the seed and its mu=2/degree-14
  witnesses into the global 231-line / 693-incidence budget OVER-SUBSCRIBES it —
  the forced closure needs more distinct lines, or forces two of the 99 points
  to share a line through all their common structure (violating lambda=1), before
  all 99 points are placed. Over-subscription (>693 incidences or >231 distinct
  lines) is the exact global closing the run names as the ONLY surviving route
  for G-n3-positive. This is k=14-specific because the budget 693/231 is
  computed only once r=7 and k=14 are fixed.
mechanism: Fix the seed T1={a,b,c}, T2={d,e,f} with cross-collinear pairs a-d,
  b-e (two extra lines: {a,d,·} and {b,e,·}). In the partial STS, x-y adjacent
  iff collinear; mu=2 says every non-adjacent pair of points has exactly 2
  common neighbours, each common-neighbour pair being a forced line; lambda=1
  forbids two points on a shared line. Grow from the seed by the SOUND rules
  (add a new line only where an adjacent/interior pair is forced to gain a
  common neighbour; check adjacent<=1, non-adjacent<=2, degree<=14, 7-lines-per-
  point). Because the seed is locally consistent at every radius (discharged
  lemma G-n3-no-local-obstruction), the growth never dies locally — so the ONLY
  way it closes is the GLOBAL integer budget: distinct lines <= 231, incidences
  <= 693, points <= 99. Encode the seeded partial STS as an exact CP-SAT/IP
  feasibility problem on (points, lines, point-line incidences) with hard bounds
  (231, 693, 99) and the seed as a fixed partial assignment; UNSAT with the seed
  present + SAT with it absent is the k=14-specific contradiction.
status: proposed
first-step: (1) Confirm the exact Fisher values: b = vr/3 = 99*7/3 = 231,
  incidences = 693. (2) Build the partial-STS CP-SAT model (variables: 99 points
  x 7 line-slots; constraints: each line is a 3-subset, each pair on at most one
  line (lambda=1), each non-collinear pair has exactly 2 common neighbours
  (mu=2), degree 14, at most 231 distinct lines) with the n3 seed pinned in.
  (3) Solve with and without the seed; require the seed-free instance to be able
  to realize each control's geometry (rook, BvLS) to validate the encoder, and
  the seed-present instance at k=14 to be UNSAT before claiming the close.
```

## Notes (inventor)

This is the run's own named global route, formalised as a candidate: the
discharged no-local-obstruction lemma makes any *local* close impossible, so the
only live finish is the exact 231-line / 693-incidence / 99-point over-
subscription. It is NOT a re-proposal of a closed approach (this was named as
the next step, never executed) nor of order-6 counting (dead: n3-agnostic). The
hard part is the encoder's soundness — the sound rules that made the radius
growth terminate at a fixpoint must be mirrored in the CP-SAT constraints so a
UNSAT is real. Least speculative of the three because it follows the run's own
stated discipline, but it still must fail on nothing the family demands.
