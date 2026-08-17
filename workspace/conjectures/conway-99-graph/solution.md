# Solution report — Conway's 99-graph problem (`srg(99, 14, 1, 2)`)

This is the consolidated deliverable of this run. All results below carry an
**evidence class** (proved / verified-computationally / conjectured /
asserted-by-source) and an anchor (a capture file with a runnable program).

---

## 0. The headline, first and plainly

**Neither existence nor nonexistence of `srg(99, 14, 1, 2)` is established by
this run or by the literature.** The problem is open. Nothing here claims the
graph or its absence. What this run produced is a set of *bounded, exact,
negative-checked structural results*: a short independent re-derivation of a
forced `n₃ ≥ 1`, **ten** closed attack routes with the obstruction that closed
each, a family classification, a documented and retracted false positive, and a
clean negative answer to the "how far does the local seed extend" question.

---

## 0.5 The n₃ dichotomy — the whole problem is one lemma, now at the front

**Evidence class: reasoned (the split is exhaustive by arithmetic; the two
discharges are sourced/checked as cited).**

The sharpest frame this run has produced (directive 39) collapses the attack on
`G-n3-positive` into **a single open lemma**, everything below being either the
discharged halves of it or closed routes that no longer need to be re-walked.
A full account is in `research/backward/n3-dichotomy.md`. The split is
exhaustive purely by arithmetic — n₃ is an integer, so n₃ = 0 or n₃ ≥ 1:

- **`G-n3-zero` — discharged.** Under n₃ = 0 (Makhnev's condition (*)), the
  forced closure of a triangle yields `Λ₀ = srg(33,12,1,6)`, which is
  parameter-infeasible by eigenvalue-multiplicity integrality (g numerator
  `2k+(v−1)(λ−μ) = −136`, not divisible by √Δ = 7). Sourced (Makhnev 1988 Thm 2,
  primary Russian text) plus re-derived here (`check_srg33_12_1_6.captured.txt`,
  `check_makhnev_n3_counts.captured.txt`; lean `n3_99_forced_at_least_3.lean`
  no sorries). Contrapositive: **any surviving graph has n₃ ≥ 1** (§1).
- **`G-n3-no-local-obstruction` — discharged.** The n₃ seed extends to a stable
  radius-6 fixpoint with no local obstruction at any radius — 19 survivors, max
  12 vertices, free bits 0, stop kind `fixpoint` (`n3_grow_radius.captured.txt`).
  So the local route is a dead end and the live move is **global**.
- **`G-n3-positive` — OPEN.** No srg(99,14,1,2) has n₃ ≥ 1. Its only remaining
  route is a **global** forced-count obstruction: over-subscription of the 693
  point-line incidences, the 231 lines, or the 99-point / 7-lines-per-point
  budget — or a global counting identity of order ≥ 7 that pins n₃ into an empty
  range. The exact line/point-replication ledger (route 7, and now with the
  rook(3)/bvls control pass the directive 39 orders) is the live instrument for
  the over-subscription half.

Everything that follows — the eleven closed routes of §2, the family facts, the
documented false positive, the local-radius answer — is therefore scaffolding:
either a discharged branch of the dichotomy or a direction that cannot
re-attack `G-n3-positive` and should not be re-opened.

## 1. What IS established: `n₃ ≥ 1` for any putative graph (re-derived)

**Evidence class: verified-computationally (integrality step), asserted-by-source
(lemma chain).**

`n₃` = number of pairs of triangles joined by exactly **two** edges.

**Claim:** any putative `srg(99, 14, 1, 2)` must contain a pair of disjoint
triangles joined by exactly two edges, i.e. **`n₃ ≥ 1`**.

**The shorter route used by this run** (shorter than Makhnev's own Thm 1 path):

1. The triangle geometry of a `(99,14,1,2)` graph is a partial Steiner triple
   system on 99 points with 231 blocks (lines), replication 7, 7 lines through
   each point.
2. Fix a vertex A. The forced-subgraph chain (Lemmas 6–9 of Makhnev 1988,
   **asserted-by-source**, reconstructed exactly in
   `code/out/check_makhnev_n3_counts.captured.txt`) forces, under the
   hypothesis `n₃ = 0`, the existence of an induced subgraph
   `Λ₀ = srg(33, 12, 1, 6)`:
   - `|Γ(A)| = 39`; 39 − 3 = 36 points in 12 inner triangles (each 3 points),
     plus 60 outside points forming 20 outer triangles, so
     1 + 12 + 20 = 33 triangle-vertices partition all 99 points, and these 33
     form a `srg(33, 12, 1, 6)`.
3. **`srg(33, 12, 1, 6)` is parameter-infeasible by eigenvalue-multiplicity
   integrality alone** (this run's self-contained step,
   `code/out/check_srg33_12_1_6.captured.txt`, exact integer/Fraction
   arithmetic, no floats, no use of Makhnev Thm 1):
   - eigenvalues r, s satisfy the parameter equation
     `x² − (λ−μ)x − (k−μ) = x² + 5x − 6 = 0` (since λ−μ = 1−6 = −5):
     discriminant Δ = (λ−μ)² + 4(k−μ) = 25 + 24 = 49, √Δ = 7, roots
     r = (−5+7)/2 = 1, s = (−5−7)/2 = −6; the multiplicity
     `g = ( (v−1) − (2k − (v−1))/√Δ ) / 2` — the capture reduces to: the
     numerator `2k + (v−1)(λ−μ) = 24 + 32·(−5) = −136` is **not divisible by**
     `√Δ = 7`, so g is non-integral.
4. **Contrapositive:** an `n₃ = 0` hypothetical graph would force this
   infeasible subgraph. Therefore no `(99,14,1,2)` can have `n₃ = 0`, i.e.
   `n₃ ≥ 1`.

This is a **constraint**, not a nonexistence proof: killing the `n₃ ≥ 1` case
is the open remainder (and the local seed for exactly that case — two disjoint
triangles joined by two edges — is the seed whose growth is analysed in §6).

Makhnev's own route rejects `Λ₀` via Thm 1 (μ = 6 > 3 and not the
`(27,10,1,5)` exception); this run rejects it by multiplicity integrality
directly, which is a strictly simpler self-contained argument.

**Anchor:** `code/out/check_srg33_12_1_6.captured.txt`,
`code/out/check_makhnev_n3_counts.captured.txt`,
`research/notes/makhnev-99-shorter-proof.md`.

### Sharpened: `1 ≤ n₃ ≤ 4158`

Combining the §1 lower bound with the **n3 cap** (the tightest non-negative
upper bound the 62 Reimbayev order-6 formulas put on `n₃`), any putative
`srg(99,14,1,2)` satisfies

```
1 ≤ n₃ ≤ 4158
```

over all five feasible members the cap is `cap = n·k·(k−2)/4 =
k(k−2)(k²+2)/8` (degree 8 in `u`; for k≥6 the binding formula is
`n1 = (1/12)nk(k−2) − n₃/3`), evaluated at `(99,14)` to `4158`.

- **Upper side (`n₃ ≤ 4158`): checked here** — exact symbolic (sympy) and
  brute-force over all 62 formulas, all four k≥6 members
  (`code/out/n3_cap_closed_form.py` → `code/out/n3_cap_closed_form.captured.txt`,
  cross-check `code/out/n3_cap_crosscheck.py`). Sharp: 4158 admissible, 4159
  not.
- **Lower side (`n₃ ≥ 1`): sourced + re-derived** (Makhnev 1988 Thm 2 chain,
  this section). Combined with the residue `n₃ ≡ 0 (mod 3)`, the effective
  sharp lower values are `3, 6, …, 4158`.

This supersedes any earlier statement that the `n₃` interval at k=14 was
`[0,4158]`: the lower endpoint is **1**, not 0, once the Makhnev conditional
(`n₃ = 0 ⇒ nonexistence`) is imported. It remains a **constraint**, not a
nonexistence proof — the interior case `n₃ ≥ 1` is open.

---

## 2. The eleven closed routes, each with the obstruction that closed it

1. **Vertex-derived design reduction does not recurse (refuted on BvLS).**
   The reduction from a vertex to the outer partial Steiner triple system
   (`G`-reduce: `code/out/g_reduce_control.captured.txt`) holds at radius (a)
   and (b) on both controls — triangles split as `k/2` through v, cross lines,
   and outer lines — but step (c), that the outer design's collinearity graph
   is again `λ=1, μ=2`, **fails on BvLS**: on the `(243,22,1,2)` outer system
   the collinearity graph has λ=1 but μ ∈ {0:330, 1:11880, 2:9900}. The
   reduction does not recurse, so it cannot be iterated to a contradiction.

2. **Hexagon (C6) count cannot distinguish 99.** The identity
   `n₁₂ = (1/12) n k (k−2)(2k²−21k+53) + n₃` is an exact identity, but both
   existing controls attain it with `n₃ = 0`
   (`code/out/hexagon_identity_verified.captured.txt`). So `n₃ = 0` is
   family-realizable and the C6 count alone cannot separate 99 from the
   existing members. The line survives only redirected through `n₃` (§1).

3. **Order-6 counting does not force `n₃ ≥ 1`.** All 62 Reimbayev order-6
   counts are of the form `(n,k)-term ± c·n₃` with `c ∈ {0,1/3,2/3,4/3,1,2,4,5,6,8,10,14}`,
   the residue class forced is `n₃ ≡ 0 (mod 3)`, and the order-6-counting-alone
   admissible interval at k=14 is `[0, 4158]` — every family member admits
   `n₃ = 0` as a non-negative
   integer for all 62 counts
   (`code/out/n3_order6_feasibility.captured.txt`). Integrality alone does not
   force `n₃ ≥ 1`; a k=14-specific geometric argument is required. (This is the
   *order-6-counting-alone* interval `[0,4158]`; once the Makhnev conditional
   `n₃ = 0 ⇒ nonexistence` is imported the effective interval is
   `[1, 4158]` — see §1's sharpened statement.)

4. **Triangle-graph non-strong-regularity is shared by 99 and 243.** The
   triangle graph (vertices = the 231 triangles) is **not** strongly regular:
   on BvLS, adjacent triangle-pairs have common-neighbour values taking 1
   distinct value (1), non-adjacent triangle-pairs 3 distinct values
   (`code/out/check_triangle_graph.captured.txt`). Since 243 exists with this
   property, any argument using "the triangle graph is not an SRG" as an
   obstruction to 99 is refuted on arrival for 99 too.

5. **No local obstruction to the join-2 seed at radius 1 — and none at any
   radius (strengthened in §6).** The two-disjoint-triangles-joined-by-two-edges
   configuration is locally consistent; the earlier "CONTRADICTION" was a
   soundness bug in the run's own engine (see §5). The obstruction, if any, is
   not local.

6. **The coclique-design route cannot rule anything out: the forced super-simple 2-(22,4,2) design EXISTS (settled constructively).** A tight 22-coclique `C` in a putative `srg(99,14,1,2)` forces the outside neighbourhoods `{N(b)∩C}` to be a 2-(22,4,2) design (b=77, r=14, k=4), and the lift additionally forbids any two blocks meeting in 3 points — a *super-simple* 2-(22,4,2) design (claim `super-simple-22242-gap`). Q2 — does such a design exist — is now settled **YES, constructively**: CP-SAT OPTIMAL in 167.35s (7315 booleans, 156131 branches), an explicit 77-block certificate in `code/out/coclique_lift_clean_design.txt`, independently verified — all point degrees 14, all 231 pairs covered exactly twice, max triple overlap 1 (`code/out/coclique_lift_cpsat.captured.txt`). **The design condition a 22-coclique would impose is satisfiable, so it cannot rule out the existence of such a coclique**: the route is closed as non-obstructive, not as a refutation of the graph — it bears on neither existence nor nonexistence. (Tool note: CP-SAT decided in 167s what MILP/HiGHS timed out on at 482s and what 4000 random draws could never have shown either way.)

7. **Global incidence counting: no forcing floor over-subscribes the fixed budget (closed).** The n₃ seed, grown to its stable local fixpoint, pins a *forced* ledger of lines and incidences inside the fixed global budget of the partial STS (99 points, 231 lines, 693 incidences, 7 lines/point). For **all 19 radius-6 survivors** (`code/out/n3_global_ledger.captured.txt`) the forced line/incidence floor is **exactly absorbable**: residual 223–227 lines and 669–681 incidences, no parity break (no odd `|I(v)|`), no vertex over 7, no negative deficit, min 4 / max 8 forced lines `L_in`, min 12 / max 24 forced incidences. The capture's own conclusion: **if an obstruction exists at this seed it is genuinely global/structural — a later-radius or cross-patch conflict — NOT a counting floor.** This kills the last cheap route: the counting-floor obstruction is absent.

8. **Incidence p-rank: closed as unusable, and this is the sharpest reasoning of the run.** The mod-2 (and mod-3) rank of the point×triangle incidence matrix `N` (`NNᵀ = (k/2)I + A`, `NᵀN = 3I + C₃`) is **NOT parameter-determined**: no spectral-multiplicity formula predicts the 2-rank (the naive even-eigenvalue rule fails on the doily `(15,6,1,3)` and GQ(2,4) `(27,10,1,5)` — rule predicts rank₂ 1, actual 5 and 7), so it *could* separate 99 from 243. But it is **unprovable this way**: a 99 value could only be settled by an actual 99 system, i.e. **the very graph whose existence is in question — circular**. Record the subtlety too: rank₂(N) varying across (9,4) and (243,22) is **NOT** evidence against parameter-determination, since such an invariant varies across parameter points anyway; **only a same-parameter split counts**, and the one available test — Shrikhande vs rook(4), both `srg(16,6,2,2)`, cospectral — gives **no** separation (rank₂(A+I) = 16 = 16, rank₂(N) = 16 = 16). `code/out/incidence_prank_determinism.captured.txt`. Closed as unusable (circular), not as contradicted.

9. **Two-graph descendant: closed by arithmetic.** The regular-two-graph descendant condition is `k = 2μ` (with companion `n = 2(2k−λ−μ)`). At 99: `k = 14` vs `2μ = 4` **fails**; companion `n = 50 ≠ 99`. Equally at 243: `k = 22` vs `2μ = 4` fails, companion `n = 82 ≠ 243`. Only rook(3) is a descendant (`k = 4 = 2μ`, Paley two-graph on 10 points). The loose claim "BvLS descends from a 244-point two-graph" is about a *co-edge-regular*, **non-regular** two-graph whose descendants do include srg(243,22,1,2) — but the k=2μ criterion is exactly the *regular*-two-graph one, and there both BvLS and 99 fail. `code/out/verify_twograph_gate.captured.txt`. Non-obstructive for the usual reason: the reformulation is inert for 99 exactly as for 243.

10. **The 6-vertex n₃-type gate is redundant, not wrong (closed, directives 26/27).** The 6-vertex-condition embedding count `E` for the n₃ template (two disjoint triangles joined by exactly two edges) tracks `n₃`: `E > 0 ⇔ n₃ > 0`. It therefore adds **no** 99 filter beyond the already-held Makhnev `n₃ ≥ 1` condition (§1). The count's zero at rook(3) and BvLS is **meaningful, not vacuous**: a hand-verified 7-vertex positive control `H` (`T₁={0,1,2}`, `T₂={3,4,5}`, cross edges `0-3`,`1-4`, vertex 6 isolated) contains exactly one join-2 pair, and the lib counter `count_induced_embeddings` returns the hand-checked nonzero counts `1, 1, 0`, total **4** over all ordered adjacent pairs (`code/out/n3_vc_loop_closure_recheck.captured.txt`, POSITIVE-CONTROL PASS). The one bad gate — a hypothesised `E = 16·n₃` — was caught and correctly retracted: over 37 random graphs the ratio `E/n₃` ranged **0.0 to 8.44**, not constant, so the identity test failed and `code/out/n3_vc_gate.captured.txt` is headed **SUPERSEDED / FLAWED IDENTITY TEST, Not evidence**. Verdict: the gate tracks n₃, n₃ ≥ 1 is already held, so the route closes as **redundant, not wrong** — this is the run's second self-retraction on record (the first is §4's localprop saturation bug).

11. **The whole orbit-matrix programme — order-3 AND order-2 — closed by computational infeasibility, NOT by mathematics (directive 37).** The plain unbroken order-3 (m=33) CP-SAT orbit matrix of a putative `srg(99,14,1,2)` does not terminate within any practical budget. The heartbeat gives **two points**: 15 variables fixed at 694 s, 33 fixed at 1889 s — 18 variables in 1195 s, about one per **66 s**; at that rate fixing all **41,745** variables would take roughly **32 days, and that is presolve alone**, before any search of the space an INFEASIBLE verdict would have to exhaust (`code/out/orbit_z3_enc_g99_plain_detached.captured.txt`, lines 300–375; note `research/notes/orbit-order3-infeasibility-boundary.md`). An **order-2** automorphism has **more** orbits than the order-3 case (≈(99+f)/2 for f fixed points), so its model is strictly larger and strictly worse — the order-2 case is not worth the same attempt at this rate either. **The obstruction is computational infeasibility, not a mathematical obstruction**: **no order-3 or order-2 exclusion is established**, the published Aut reduction to {Z₂, Z₃} (Crnković–Maksimović, Behbahani–Lam, Cesarz–Woldar) stands untouched, and the graph's automorphism group **remains open**. What this route *did* establish is the stated boundary (model size 41,745 vars / 57,165 constraints at m=33; presolve rate ~1 var/66 s) — that is the measurement a next pass can act on. Closed as boundary-recorded, not as a verdict; the Z2/Z3 automorphism question is out of reach of this CP-SAT encoding on this budget.

Each candidate was required to be run against the rook's graph `(9,4,1,2)` and
the Berlekamp–van Lint–Seidel graph `(243,22,1,2)` through `code/lib/srg.py`,
and to name the step that breaks on them. Routes 1–4 all survive on both
controls (a nonexistence argument using only parameters, counts, adjacency
algebra, integrality, interlacing, Krein or absolute bound **cannot** conclude
anything about 99 because it holds verbatim for 9 and 243). Route 5 is
different: it is cleared *local* and is answered directly for every radius in
§6. Route 6 is different again: it is a design-condition check, and the
construction settles it affirmatively, so it is non-obstructive. Routes 7 and 9
are arithmetic/structural closures (global counting floor; regular-two-graph
descendant) that each hold identically at 243, so they are refuted on arrival
as 99 arguments. Route 8 (incidence p-rank) is closed as **unusable — circular**:
it is not a spectrum function and could in principle separate 99, but a 99
value could only be measured on an actual 99 system, the very graph whose
existence is in question.

---

## 3. Family facts

- **Five-member classification (sourced, with integrality checked):** the
  feasible members of the `srg(v,k,1,2)` family are exactly
  `(v,k) ∈ {(9,4), (99,14), (243,22), (6273,112), (494019,994)}`.
- **Integrality iff `2u+1 | 63` (checked).** With `k = u²+u+2`,
  `v = 1 + k²/2`, `a = √(4k−7) = 2u+1` an odd integer, eigenvalue-multiplicity
  integrality holds iff `a | 63`, i.e. `a ∈ {3,7,9,21,63}`, `u ∈ {1,3,4,10,31}`.
  Mechanism: `a | k(4−k)/2`, and with `k=(a²+7)/4`, `a` odd, this reduces mod a
  to `a | 7·9 = 63`. **This names why `srg(33,8,1,2)` fails (a=5 ∤ 63) and why
  the same mechanism cannot touch 99 (a=7 | 63).** 99 is the `a=7` member.
  (`code/out/divisor63-characterization.md`, claim `divisor63-multiplicity-integrality`.)
- **Coclique (independence) bound closed form (checked):**
  `α = v·(−s)/(k−s) = (u·k+2)/2 = (u³+u²+2u+2)/2`, with eigenvalues r=u, s=−(u+1).
  Values at the five feasible u: `{3, 22, 45, 561, 15408}` — strictly increasing
  and **pairwise distinct**, so the 99 bound `α = 22` is parameter-specific.
  This is the single cleanest candidate number for a Wilbrink–Brouwer-style
  coclique-design contradiction at 99 (analogue of the `2-(15,5,4)`
  15-coclique argument at `(57,14,1,4)`), and the distinctness of the family
  bounds means such an argument is **not** refuted on arrival by 9 (bound 3)
  or 243 (bound 45).
  (`code/out/coclique-bound-closed-form.md`, claim `coclique-bound-closed-form`.)

---

## 4. A false positive, in full — recorded, not hidden

**The bug.** The shared arc-consistency engine `code/lib/localprop.py` had a
soundness bug in its **saturation branch**: when a pair was saturated (its
required common neighbours already fixed), it forced *every* candidate common
neighbour off on **both** sides — `a−v = 0 AND b−v = 0` — where the sound
conclusion is only the 2-SAT / at-least-one-off clause `NOT(a−v AND b−v)` (at
least one edge off, not both).

**The false verdict it produced.** For the n₃ seed (two disjoint triangles
`{a,b,c}`, `{d,e,f}` joined by cross edges `a−d`, `b−e`), the λ-witness pair
`(a,b)` (witness c) forced the candidate vertex `6` off both sides, flipping the
already-fixed `a−6=1` λ-witness of edge `(a,d)` — producing a spurious
`CONTRADICTION` with a clean-looking log. This was reported as a structural
obstruction before it was audited.

**The retraction.** The capture that carried it,
`code/out/n3_local_propagation.captured.txt`, is **annotated SUPERSEDED** at the
top, naming the bug and the sound result. The consumers audit
(`code/out/localprop_consumers_audit.md`) confirmed the bug was historical, not
active: `code/lib/localprop.py` now implements the sound `NOT(a-v AND b-v)`
semantics, and `code/out/independent_soundness_check.py` (engine vs. from-scratch
complete enumeration) reports `ENGINE == ENUMERATION on all forced values: True`
and **2 satisfying assignments** for the seed. No file downstream of
`localprop.py` carries a contaminated verdict.

**Why this is in the deliverable.** A self-caught false positive is the most
valuable single event of the run — it is exactly the class of error that
"proves" nonexistence of a graph that actually exists. It is recorded here so
no later pass re-cites the SUPERSEDED capture as a theorem.

---

## 5. The sound local result for the seed (radius-1, and every radius)

**Evidence class: verified-computationally (complete exact enumeration).**

The only criterion arc-consistency may soundly conclude on a bounded patch is
the **upper-bound** one: an *adjacent* pair has ≤ 1 common neighbour, a
*non-adjacent* pair ≤ 2, and any remaining *deficits* are satisfiable by the
other **91** vertices outside the patch. Only **excesses** are contradictions.

Under exactly that criterion, the join-2 seed admits **2 satisfying assignments**
over the 9 free interior edges of the 8-vertex forced closure (complete
enumeration of 512 assignments, exact): **the seed extends locally; there is NO
local obstruction at radius 1.**

A separate capture (`code/out/n3_seed_consistency.captured.txt`) reports 0
completions satisfying the constraints *exactly within the patch*. **That is NOT
an obstruction** and must not be cited as one: the required common neighbours of
a boundary pair may legitimately sit among the other 91 vertices. The sound
result (2 satisfying assignments under the upper-bound criterion) is the one
that carries.

**Anchor:** `code/out/n3_seed_consistency_ub.captured.txt`,
`research/notes/n3-seed-locally-consistent-radius1.md`,
claim `n3-seed-locally-consistent-radius1`.

---

## 6. At what radius does the seed stop extending? — Answer: at no radius

**Evidence class: verified-computationally (complete exact enumeration per
radius, stable fixpoint reached).**

The operator's stated next question — at what radius, if any, does the seed
stop extending — is answered by `code/out/n3_grow_radius.py` →
`code/out/n3_grow_radius.captured.txt`.

**Method (sound).** The patch is an exact `+1/0/-1` partial adjacency matrix
over materialised vertices. Only one rule grows it: **(3)** every adjacent pair
with 0 interior common neighbours forces a fresh distinct external λ-witness
vertex adjacent to both. Rules (1) λ-excess (adjacent pair ≥ 2 common
neighbours), (2) μ-excess (non-adjacent pair ≥ 3), (4) locally-7K2, (5)
degree ≤ 14 are **checks**; only excesses are contradictions. Deficits are never
materialised (the ~91 outside vertices absorb them). No use of the unsound
saturation branch.

**Result table (exact survivors):**

| Radius | Vertices reached | Max free interior bits | Survivors (exact) |
|---|---|---|---|
| 0 | 6 | 0 | 1 |
| 1 | 8 | 9 | **2** (self-check: must reproduce 2 ✓) |
| 2 | 8–9 | 6 | 5 |
| 3 | 8–11 | 15 | 11 |
| 4 | 8–11 | 8 | 19 |
| 5 | 8–12 | 9 | 19 |
| 6 | 8–12 | 0 | 19 |

**Boundary reached: a stable fixpoint at radius 6.** No survivor materialises a
new witness and none dies, with 0 free interior bits. Since rule-(3) λ-witness
growth is the only thing that grows the patch, a fixpoint here means **the seed
extends locally to every radius** — no zero-survivor radius, no excess, no
bit-cap hit (max free bits was 15, far below the 2²⁰ enumeration ceiling at
which a solver would become necessary). Wall clock: 0.9 s.

**Interpretation — the infeasibility boundary.** The answer to "at what radius
does the seed stop extending" is **it does not**: there is **no local radius
obstruction at all**. The constraint that would kill the n₃ ≥ 1 case is
entirely *global* — it lives in how the ~91 outside vertices interlock to
absorb the μ=2 and degree deficits, not in any local excess. This is a real
negative result for the approach: it says the obstruction (if any) is not
detectable by any finite local ball, so a proof must be global or must use more
than the five sound local rules. It also says the standing temptation to
re-encode the local ball in a solver would have converged on nothing — the
local question is provably exhausted.

**Caveat:** this is a LOCAL statement; it neither proves nor disproves global
existence of `srg(99,14,1,2)`.

**Anchor:** `code/out/n3_grow_radius.py`, `code/out/n3_grow_radius.captured.txt`.

---

## 7. The frontier — what a next pass should attack, and what it should not repeat

**What it should attack.**
1. The **global closure** of the n₃ ≥ 1 seed: take the radius-6 fixpoint
   structures (19 survivor sub-structures on 8–12 vertices) and attempt to
   close them into 99 vertices, i.e. decide whether the outside 87–91 vertices
   can be joined to satisfy μ=2 and degree-14 for every boundary pair. This is
   the only place the obstruction, if it exists, can live. **The global
   counting floor is ruled out** (route 7), so what remains is the
   **cross-patch / global structural** question — stated plainly, this is
   **harder than everything closed so far**: no local obstruction at any radius,
   no counting floor, and the residual 223–227 lines / 669–681 incidences are
   arithmetically absorbable for all 19 survivors. The obstruction, if any,
   lives in the interaction between patches or in a structural (not counting)
   property of the full 99-point assignment.
2. ~~A **coclique-design contradiction at 99**~~ — **closed (directive 20)**: the
   forced super-simple 2-(22,4,2) design **exists** (§2 route 6), so the design
   condition cannot rule out a 22-coclique. Not a live attack line.
3. **The a=7 specificity:** any nonexistence argument must be specific to
   `a = √(4k−7) = 7` (Rø0 the integrality that 9 and 243 both survive). A proof
   that works only at a=7 and breaks at a=3, 9 is the shape an admissible
   argument must take.

**What it should NOT repeat.**
- The eigenvalue-only, counts-only, integrality, Krein, absolute-bound,
  interlacing, two-weight-code (Delsarte) and SNF/critical-group routes: all
  parameter-determined, all surviving unchanged on 9 and 243, all already
  closed (CLOSED in §2 and in `research/APPROACHES.md`). Also not to repeat:
  the **global incidence counting floor** (route 7 — ruled out for all 19
  survivors), the **incidence p-rank** (route 8 — circular, unmeasurable
  without the very graph), and the **regular two-graph descendant** (route 9 —
  fails by k=2μ arithmetic at both 99 and 243).
- **The orbit-matrix programme (route 11) — NOT to repeat in CP-SAT.** Closed
  by computational infeasibility: the order-3 (m=33) search fixes ~1 variable
  per 66 s (presolve alone ≈ 32 days for all 41,745 variables), and the order-2
  case (≈(99+f)/2 orbits) is strictly larger and strictly worse. This bound
  applies **only** to this CP-SAT encoding at this presolve rate; a different
  encoder, a different solver, or a structural argument on the orbit matrix
  that avoids the 41,745-variable search is still open. What route 11 does **not**
  establish: no order-3 or order-2 automorphism exclusion, so the Aut reduction
  to {Z₂, Z₃} and the open automorphism-group question stand untouched.
- Re-running the local-radius growth: it is exhausted (fixed point).
- Re-encoding the local ball in SAT/CP-SAT, and (per the operator) the
  radius-2 CP-SAT setup generally — it burned two specialists for zero
  artifacts and the local question is now answered by complete enumeration
  anyway.
- Reproducing Makhnev's Thm-1 route for `n₃ ≥ 1`: the shorter integrality
  re-derivation (§1) already lands the same conclusion.

---

## 8. Completion status

- **Not established:** existence or nonexistence of `srg(99,14,1,2)`. Stated
  first and plainly (§0).
- **Established (verified-computationally / sourced):** `n₃ ≥ 1` (§1); **eleven**
  closed routes with obstructions (§2); five-member family, `2u+1 | 63`
  integrality, `α = 22` coclique bound (§3); the retracted false positive (§4);
  no local obstruction at any radius, stable fixpoint at radius 6 (§5–§6); no
  global counting floor (route 7), incidence p-rank unmeasurable/circular
  (route 8), two-graph reformulation inert (route 9); verified constraint
  `3 ≤ n₃ ≤ 4158`.
- **The run does not claim the problem.**
