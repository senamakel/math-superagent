# Approach: Makhnev-analog forced global sub-design from the n3-positive seed

```approach
idea: Makhnev 1988 Thm 2 wins the n3=0 branch by showing the closure of a
  triangle forces a rigid sub-object — srg(33,12,1,6) — which then dies on
  eigenvalue-multiplicity integrality (g-numerator -136 not divisible by 7).
  The n3>=1 branch (the surviving case) has never been given the ANALOGOUS
  move: instead of a local radius ball (which G-n3-no-local-obstruction proves
  can always complete), close the seed GLOBALLY — force the global absorption
  of the seed's ~91 outside vertices through the mu=2 / degree-14 /
  lambda=1 interaction into a specific induced sub-design whose parameters are
  k=14-specific and whose eigen-multiplicity or design-rank is then shown
  non-integral by the same exact-arithmetic weapon that killed srg(33,12,1,6).
mechanism: The seed spans 6 points in 2 lines. Its 7 other cross-pairs are all
  non-adjacent, so each must have exactly 2 common neighbours in Gamma, and the
  two cross-collinear pairs each sit on a third line. Absorbing these forced
  witnesses back into N(0)-matching (c5: every neighbourhood is 7K2) and into
  the 84-vertex mu=2 outer structure forces a definite, parameter-determined
  partition of the remaining 93 points into a smaller incidence structure (lines
  constrained to reuse the 231-line budget). If that residual structure's graph
  has distinct eigenvalues that fail the integrality condition for its size —
  computed exactly, as the srg(33,12,1,6) computation was — it is infeasible.
  Unlike interlacing-84 (refuted: satisfied by construction because it is a
  necessary condition of any such graph), this forces a SPECIFIC sub-design
  whose existence is not automatic — the gate is that Makhnev's own n3=0
  closure produces a real infeasible srg(33,12,1,6), so the same closure
  machinery is a genuine filter, and applying it to the n3>=1 seed is the
  unexplored symmetric case.
status: refuted
killed-by: The n3>=1 seed is locally consistent at EVERY radius (radius-6
  fixpoint, 19 survivors, never stops extending — discharged lemma
  G-n3-no-local-obstruction). Makhnev's n3=0 closure is determinate precisely
  BECAUSE that branch has no free bits (n3=0 fixes all cross-triangle joins),
  forcing the single object srg(33,12,1,6) which then dies on integrality. The
  n3>=1 seed, by contrast, has genuinely free cross-pair choices at every shell
  (which is why it extends locally at every radius), so no determinate global
  sub-design is forced by the closure machinery — the inventor's own note
  concedes that if the absorption has free parameters the candidate collapses
  into n3-seed-fisher-replication, and it does. Re-fighting G-n3-no-local-
  obstruction in the name of a "global closure" that cannot be pinned down
  produces no k=14-specific object to test for integrality.
first-step: (1) Reproduce the Makhnev n3=0 closure in code as a template
  (code/out/check_makhnev_n3_counts.captured.txt already has the counts:
  |Gamma(A)|=39, 12 inner + 20 outer triangles, forced srg(33,12,1,6)).
  (2) Re-run the SAME closure routine seeded by the n3>=1 configuration (two
  lines joined by 2 cross-collinear pairs) instead of by a single triangle;
  enumerate the forced partition of the 99 points. (3) If a determinate sub-
  design emerges, check its parameter-integrality exactly (divisor-of-Delta /
  g-numerator test) at a=7; also verify the closure routine returns the true
  n3=0 answer on rook(3)/BvLS so the machinery itself is validated.
```

## Notes (inventor)

Most speculative of the three, and the one most exposed to the discharged
no-local-obstruction lemma: the seed completes locally at every radius, so the
forced object here MUST be a global absorption (spanning far more than a radius
ball), not a local subgraph — otherwise it re-fights G-n3-no-local-obstruction.
The hope is that global mu=2/degree-14 absorption, unlike local growth, does NOT
have arbitrary free bits, so a determinate sub-design can be forced. That is
exactly the open question; if the absorption turns out to have free parameters,
this candidate reduces to the Fisher-replication ledger (n3-seed-fisher-
replication) and should be folded into it.
