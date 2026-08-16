# The n₃ dichotomy — what would prove nonexistence of srg(99,14,1,2)

This skeleton splits the goal on n₃ = the number of unordered pairs of *disjoint*
triangles joined by exactly 2 edges (no shared vertices, exactly 2 cross edges). The
split is exhaustive because n₃ is a non-negative integer, and it is the sharpest split
the run currently has: Makhnev 1988 Thm 2 already disposes of the n₃ = 0 case, and its
contrapositive is precisely that any surviving srg(99,14,1,2) must have n₃ ≥ 1. So the
whole open problem is now the single proposition that n₃ ≥ 1 is impossible.

```skeleton
goal: no srg(99,14,1,2) exists
implies: Let Γ be a putative srg(99,14,1,2) and n3(Γ) its count of disjoint-triangle pairs joined by exactly 2 edges. n3(Γ) ∈ ℤ≥0, so n3 = 0 or n3 ≥ 1. G-n3-zero (discharged) kills the first branch via Makhnev Thm 2 / forced srg(33,12,1,6) infeasibility; G-n3-positive kills the second. Both branches impossible ⇒ Γ cannot exist.
killed-by: 
rests-on: makhnev1988-condstar-theorems, makhnev99-shorter-proof-integrality, n3-99-forced-at-least-3
status: live
```

```gap
id: G-n3-zero
lemma: No srg(99,14,1,2) has n3 = 0, where n3 = 0 is Makhnev's condition (*) — no pair
  of disjoint triangles is joined by exactly 2 edges. Under (*), Makhnev's closure of a
  triangle forces a subobject Λ₀ = srg(33,12,1,6), which is parameter-infeasible.
status: discharged
discharged-by: makhnev1988-condstar-theorems (sourced, primary Russian full text) with the
  decisive infeasibility step re-derived as makhnev99-shorter-proof-integrality (checked:
  the g-numerator 2k+(v−1)(λ−μ) = −136 is not divisible by √Δ = 7, so srg(33,12,1,6) has
  no integral eigenvalue multiplicity). Admissibility gate passed on both controls in
  makhnev-condstar-gate-passed (rook(3) and bvls both have n3 = 0 and μ = 2 ≤ 3).
thread: research/threads/n3-forced.md
next: (none — discharged; do not restate as open)
```

```gap
id: G-n3-positive
lemma: No srg(99,14,1,2) has n3 ≥ 1. Equivalently: the n3 seed — two disjoint triangles
  T1 = {a,b,c}, T2 = {d,e,f} joined by exactly 2 edges (cross edges a–d, b–e; the other
  seven cross pairs non-adjacent) — admits no completion to a graph on 99 vertices that
  is locally 7K2 with λ = 1 and μ = 2. Since n3-99-forced-at-least-3 sharpens this to
  n3 ∈ {3, 6, 9, …}, it suffices to rule out any graph containing the seed.
status: open
next: grow the *exact* forced closure of the 6-vertex n3 seed by ADDING witness vertices —
  for each edge, its unique triangle third vertex (λ = 1); for each non-adjacent pair, its
  two common neighbours (μ = 2) — tracking that the total never exceeds 99 vertices, no
  vertex exceeds degree 14, and no point lies on more than 7 lines. This is the step the
  radius-1 result did NOT take: n3-seed-locally-consistent-radius1 uses the relaxed
  upper-bound criterion (deficits satisfiable by the other ~91 vertices) and is therefore
  NOT an obstruction. tool_builder enumerates one more shell completely (report the
  free-bit count after witnesses are added); an EMPTY shell is a GLOBAL nonexistence
  result (the forced closure over-constrains before reaching 99 vertices), whereas a
  non-empty growing shell reports the frontier (space, worker count, wall-clock). In
  parallel theorem_prover: formalise the Makhnev closure machinery with the n3 = 0
  hypothesis dropped, so the same forced-subobject argument can be aimed at the seed.
```

## Discipline this skeleton imposes

- **The split is exhaustive by arithmetic, not by a route.** n₃ is a count, hence an
  integer ≥ 0; the two branches cover it. G-n3-zero is discharged, so the skeleton is
  "one lemma from a proof" in exactly the sense the reducer exists to capture.
- **The controls cannot refute G-n3-positive.** rook(3) and bvls(243) both have n₃ = 0
  (claims `n3-zero-four-classical-lambda1-srgs`, `makhnev-condstar-gate-passed`), so they
  are not witnesses against an n₃ ≥ 1 argument. The only known λ = 1 SRGs with n₃ ≥ 1 are
  the μ ≥ 4 Bondarenko–Radchenko members (81,20,1,6) and (729,112,1,20) — μ ≠ 2, so they
  cannot gate the μ = 2 kill argument either. The honest control for G-n3-positive is the
  hand-built seed inside a locally-7K2 μ = 2 patch, which is weaker than a real graph.
- **A local obstruction is not enough.** The seed is locally consistent at radius 1
  (claim `n3-seed-locally-consistent-radius1`), so G-n3-positive must be closed by a
  *forced-count* obstruction (> 99 vertices, degree > 14, or > 7 lines through a point)
  or a counting identity, not by more radius shells of the relaxed criterion.
