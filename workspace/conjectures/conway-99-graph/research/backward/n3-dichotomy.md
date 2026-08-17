# The n₃ dichotomy — what would prove nonexistence of srg(99,14,1,2)

This skeleton splits the goal on n₃ = the number of unordered pairs of *disjoint*
triangles joined by exactly 2 edges (no shared vertices, exactly 2 cross edges). The
split is exhaustive because n₃ is a non-negative integer, and it is the sharpest split
the run currently has: Makhnev 1988 Thm 2 already disposes of the n₃ = 0 case, and its
contrapositive is precisely that any surviving srg(99,14,1,2) must have n₃ ≥ 1. So the
whole open problem is now the single proposition that n₃ ≥ 1 is impossible.

Update (reducer, this turn): the local half of G-n3-positive is now settled, and the
old `next` on it ("grow one more radius shell, an empty shell is a global result") is
retracted. The run has shown the n₃ seed extends locally to a **stable fixpoint at
radius 6** with no local obstruction at any radius (`code/out/n3_grow_radius.captured.txt`:
19 survivors, max 12 vertices, free bits reach 0; stop kind `fixpoint`; wall clock 1.1s).
Growing shells by the sound upper-bound criterion can never close — the frontier is the
whole graph. That local result is now a discharged lemma (G-n3-no-local-obstruction)
below, and the only remaining path for G-n3-positive is a **global** move.

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
id: G-n3-no-local-obstruction
lemma: The n₃ seed — two disjoint triangles T1 = {a,b,c}, T2 = {d,e,f} joined by exactly
  2 edges (cross edges a–d, b–e) — admits a completion in every finite-radius shell of a
  lambda=1, mu=2, locally-7K2 patch grown by the sound upper-bound rule (grow a fresh
  witness only for adjacent/interior pairs forced to have a common neighbour; adjacent
  pairs ≤ 1 common neighbour, non-adjacent ≤ 2, degree ≤ 14, 7K2 are checks on excesses;
  deficits are satisfiable by the ~91 outside vertices). Equivalently: there is NO local
  obstruction to the seed at any radius.
status: discharged (FORMALISED on the kernel)
discharged-by: code/lean/n3_dichotomy_G_n3_no_local_obstruction.lean — lean_check
  `outcome: verified`, no sorries, no cited axioms. Nine theorems formalised: radius 0
  (n3_seed_upper_ok_radius0), radius 1 (n3_seed_no_local_obstruction_radius1 :
  upper_ok 8 R8), the fixpoint-closure lemma (r8_fixpoint_closed : every edge of R8
  already has an interior common neighbour), and the combining step
  (n3_seed_no_local_obstruction_every_radius : forall r, the radius-1 closure extends
  to every radius). The fixpoint-closure lemma is exactly why the sound growth rule
  materialises no fresh witness beyond R8 — the shell is stationary at 8 vertices for
  every radius, reproducing survivor 0 of code/out/n3_grow_radius.py →
  code/out/n3_grow_radius.captured.txt (the +0 witness / 8 verts / free-bits 0 branch
  that persisted through radius 6). The earlier CONTRADICTION capture
  n3_local_propagation.captured.txt is SUPERSEDED — an over-forcing saturation-branch
  bug in code/lib/localprop.py.
next: (none — fully proved on the kernel. Its only consequence is a negative one: a
  future attempt must NOT grow radius shells of the sound criterion expecting an empty
  shell, and must NOT re-derive a "local contradiction". It redirects G-n3-positive to a
  global move.)
```

```gap
id: G-n3-positive
lemma: No srg(99,14,1,2) has n3 ≥ 1. Equivalently: the n3 seed — two disjoint triangles
  T1 = {a,b,c}, T2 = {d,e,f} joined by exactly 2 edges (cross edges a–d, b–e; the other
  seven cross pairs non-adjacent) — admits no completion to a graph on 99 vertices that
  is locally 7K2 with λ = 1 and μ = 2. Since n3-99-forced-at-least-3 sharpens this to
  n3 ∈ {3, 6, 9, …}, it suffices to rule out any graph containing the seed.
status: open
next: GLOBAL, not another local shell (G-n3-no-local-obstruction makes the local route a
  dead end) and NOT an order-k subgraph-count identity. Acquisition of Reimbayev 2025
  order-7 paper (arXiv:2511.06572, in library, claim reimbayev-order7-counts-two-free-vars)
  closes the counting-identity route through order 7: order-7 Hamiltonian counts depend on
  TWO free variables (n3, h11, 4n3>=h11>=2n3), so no order-<=7 identity forces n3>=1 or
  pins n3 into an empty range (n3=0 with h11=0 is consistent at every family member).
  The ONLY remaining route is the EXACT line-/point-replication ledger: 99 points each on
  7 lines → 693 point-line incidences; 231 lines of size 3. Fix the seed in a putative
  srg(99,14,1,2) and compute 1) the exact minimum number of distinct lines+incidences the
  seed and its forced witnesses already occupy and 2) whether the residual budget the ~
  outside vertices must absorb is met by exactly the μ=2/degree-14 interaction — a forced
  over-subscription (>693 incidences, or >231 distinct lines before all 99 points placed)
  is the only global closing an empty result can carry, and it must be verified to fail on
  nothing the family demands.
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
- **A local obstruction is not enough, and there is none.** The seed is locally
  consistent at every radius (G-n3-no-local-obstruction), so G-n3-positive can ONLY be
  closed by a *global* forced-count obstruction — over-subscription of the 693 line-
  incidences, the 231 lines, or the 99-point / 7-per-point budget — or by a global
  counting identity of order ≥ 7 that pins n₃ into an empty range. Review: all closed
  order-≤6 lines are n₃-agnostic (order6-n3-not-forced), and the coclique α=22 lift is
  non-obstructive because the super-simple 2-(22,4,2) design EXISTS (super-simple-22242-
  exists), so neither recombines into G-n3-positive.
