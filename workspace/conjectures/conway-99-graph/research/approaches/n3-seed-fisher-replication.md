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
status: adopted
precedent: Fisher's inequality (b >= v) is standard design theory; the exact
  budget b=231, incidences=693, replication r=7, line size 3 is forced by
  k=14,lambda=1,mu=2 alone (problem.md derivation; c1). The n3>=1 case is the
  one surviving branch of the forced dichotomy (Makhnev Thm 2 wins n3=0 via
  srg(33,12,1,6) at a=7; the n3>=1 branch has no non-local obstruction and no
  published obstruction). No source was found that closes the n3>=1 branch;
  the run's own global over-subscription route was named as the live finish in
  CONTEXT.md/n3 findings and never executed.
first-step: (1) Confirm the exact Fisher values in code (b=99*7/3=231,
  incidences=693) and that both controls rook(3) (9 points, 6 lines, r=4) and
  bvls_graph() (243 points, 891 lines, r=22) saturate THEIR OWN budgets, so the
  encoder has a real notion of "saturates the budget". (2) Widen the existing
  n3 growth code (code/lib/localprop.py, sound rules that already terminate at a
  radius-6 fixpoint) into a full global line-budget model: track, per shell,
  the running count of distinct points used, distinct lines used, point-line
  incidences used, and per-point degree against the hard caps (99 points, 231
  lines, 693 incidences, degree 14, 7 lines per point). (3) Solve the seed-
  present instance at k=14 for global feasibility; require the seed-free instance
  to realize rook(3) and a structural slice of BvLS to validate the encoder
  BEFORE reading any UNSAT. (4) The live claim: seed-present + hard caps
  over-subscribes (forces >231 distinct lines or >693 incidences before all 99
  points are placed); if instead a feasible completion is found at k=14 with the
  seed, that is itself a strong positive structural result (a partial STS with
  the seed, 7 per point, mu=2) worth reporting. The gate: every consistency
  rule used must be the SOUND growth rule (adjacent<=1, non-adjacent<=2,
  degree<=14, 7-lines-per-point), never the buggy over-forcing saturation branch,
  so an UNSAT is real. This is k=14-specific because the budget 99/231/693/14 is
  only computed once lambda=1,mu=2,k=14 are fixed; it must fail on 9 and 243
  only in the sense that those members saturate their own budgets with n3=0 and
  do NOT carry the 2-edge-joined disjoint triangle seed (n3=0 finding), so the
  seed's oversubscription cannot refute them.
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
