# Scholar pass — re-reading the 2024–25 additions against the goal

This pass re-read the freshly-added library against GOAL.md, TASKS, and the
durable beliefs. Three findings stand out, each verified against the primary
full text on disk, not taken from the digest.

## 1. The whole real-k entropy-inequality line is now settled (Ho)

Verified against `research/sources/ho-generalized-boppana-lean-2026.html.full.md`
(theorem, proof, and Lean-4 claim all read in the body):

- **Ho, arXiv:2601.19327** proves `α_k·h(x^k) ≥ x^(k−1)·h(x)` for **all real
  k>1**, α_k the unique positive root of `x(1+x)^(k−1)=1`, equality iff
  `x∈{0, 1/(1+α_k), 1}`. Boppana's inequality is the k=2 case. Lean-4 formalsed
  (github.com/boonsuan/entropy-inequality).
- This closes the line Yuster opened (k=3,4), Yuster–Yashfe extended (5..20),
  and Wakhare reduced to a real-rootedness conjecture. **The one-variable
  entropy inequality that drives the iid barrier is now a theorem at every
  order.** It does NOT by itself move the k=2, c=1 UC constant — that is the
  gap (entropy methods are structurally capped below 1/2).
- **Bearing:** the `attack-coupling-half` task's k-union-closed generalisation
  now rests on proved ground at every k; the barrier
  `(3−√5)/2 = α₂/(1+α₂)` is exactly the k=2 member. What remains open is UC at
  k=2, c=1.
- Caveat kept: the author discloses GPT assistance in some proof steps; the
  Lean 4 formalisation is the independent mechanical check, satisfying the
  workspace rule that numerics/heuristics are not proof.

## 2. Record value reconciled — no hidden post-Liu record

Verified against `research/sources/wakhare-iterated-entropy-derivatives-2025.html.full.md`:

- The "≈0.38237 current best constant" in the 2025 J. Approximation Theory
  survey IS Jingbo Liu's conditionally-iid bound, cited there as
  [Liu24] = IEEE CISS 2024 pp.1-6. So 0.38237 / 0.38271 is **one** conditional
  bound, not a new published record.
- The peer-reviewed record remains **Yu ≈0.38234 (Entropy 2023)**; `(3−√5)/2`
  is the separately-peer-reviewed iid barrier (AHS, EJC 2024). No source in the
  library exceeds ≈0.38271 **unconditionally**.
- This closes request `exact-current-published-c8b8` (already claimed
  `published-status-current`, `published-record-c`).

## 3. Minimal-counterexample bound upgraded to |F| ≥ 51 (Hu)

Verified against `research/sources/hu-union-closed-2017.full.md` line 83, which
states the result verbatim: with Bošnjak–Marković's m≥12 improved to
Živković–Vučković's m≥13, Theorem 1 (`|A| ≥ 4m−1` for a separating minimal
counterexample) implies **a minimal counterexample has ≥ 51 sets**. Claims
`verified-m-small` and `hu-theorem1-4m-minus-1` carry this; the older |F|≥47
(using m≥12) is superseded. This also confirms |F|≤50 is a verified range.

## New sources digested this pass (verified faithful)

Each of these has a full digest in `research/summaries/` whose statements I
cross-checked against the run's durable knowledge:

- **Das–Wu (2412.03862)**: proves Nagel's conjecture exactly — kth-most-frequent
  element in ≥|F|/(2^(k−1)+1) sets, equality iff near-k-cube. Confirmatory;
  also restates the 2025 record at ≈0.3823455 unconditional.
- **Lozin–Zamaraev (JCTA 202, 2024)**: Horn-function formulation; UC settled
  for **submodular** functions and **double Horn** functions (dependency
  property). **New settled restricted classes** — genuinely a fresh formulation
  beyond lattice/graph.
- **Colbert (2412.18740)**: new settled class — union-closed families of
  **dimension ≤ 2** have an abundant element (finite and infinite); pins the
  precise finite/infinite divide for negative control #3.
- **Bhasin (2409.17050)**: simply-rooted families have acyclic cubical set;
  Euler identity Σ(−1)^k|C_k(F)|=1. Constraint, not a proof — the topological
  angle now has its primary source.
- **Nived (2409.02221)**: new bipartite graph class (decomposition common-side
  stable 2-layered) satisfies the graph form. Extends settled graph classes.
- **Phan (2412.18622)**: reformulation (UC ⟺ existence of the subfamily G in
  the log/count inequality); exact equivalence, not a bound.
- **Carvalho–Machiavelo (2408.11213)**: supratopology reformulation; reduction
  to separating/independent/normalized; descendants of power sets form a new
  settled class.
- **Moghaddas Mehr (2501.02637)**: isomorphisms of pure UC families are
  ground-element-induced; purity (no redundant element) is free for UC since a
  redundant element has density 1 — justifies assuming a counterexample is pure.
- **Lu–Raz (2405.10639)**: Reimer's conditions alone do NOT force abundance —
  sharpens negative control #2 (union-closure must be used).
- **Wakhare (2312.14743, JAT 2025)**: real-k entropy inequality programme
  (real-rootedness reduction), now confirmed by Ho's all-k proof. Attribution of
  "0.38237" = Liu CISS.

## Sources that do not help (and why)

- **OEIS A1xxxxx catalogue files** (A102897, A000012, etc.): counting sequences
  of union-closed/semilattice families. A recurrence for the *count* of
  union-closed families says nothing about whether an abundant element exists —
  GOAL marks this out of scope (dropped by operator directive). They are
  catalogued lookups, not derivations; do not re-read.
- **Citation-graph files** (`citations_w1993810789.md`, w2059461644,
  w2138776194, w2265864037): each explicitly says "filed by a citation-graph
  lookup, not read... none is evidence." They are leads, not claims; nothing to
  extract. Do not read again.
- **`eccles-stability-probe.md` + `eccles-stability-probe.full.md`**: a
  misdirected download (condensed-matter rheology paper, not Eccles). Marked
  THROWAWAY; the correct Eccles body is arXiv:1311.2298
  (`-2015-html.full.md`). Do not use the probe.
- **`bouchard-lattice-2025.trial.md`**: duplicate of the canonical
  2025 lattice digest; fine.

## Durable findings stored

Stored with `remember_memory` (all source-backed, hypotheses checked):
(1) Ho all-k inequality; (2) Wakhare 0.38237=Liu CISS reconciliation;
(3) Hu |F|≥51; (4) Lu–Raz Reimer's-conditions-negative; (5) Lozin–Zamaraev
Horn/submodular/double-Horn classes; (6) Moghaddas purity-is-free; (7) Bhasin
acyclicity; (8) Nived graph class; (9) Colbert dimension-≤2 class; (10)
Das–Wu Nagel; (11) Phan reformulation; (12) Carvalho–Machiavelo reductions.

## Contradictions / flags

- **No genuine source-vs-source contradiction found** among the new 2024–25
  additions. The Morris Conjecture 3 vs Pulaj-2017 contradiction (already in
  the ledger) is unaffected.
- The `|F| ≥ 47` older number in some files is superseded by `≥ 51`; claims
  `verified-m-small` and `hu-theorem1-4m-minus-1` already carry the corrected
  value.
- Nothing new contradicts recalled durable memory; the record value, barrier
  interpretation, and verified ranges all hold and are re-confirmed.

## What the run still lacks

- A **primary-source reproduction of Yu's ≈0.38234** optimisation end-to-end
  (the library now holds the full Yu/Cambie/Liu bodies, so this is feasible;
  the extended reproducible LP/entropy computation is the natural next step for
  the `attack-coupling-half` task).
- The **global-sup-over-α claim** (`yugamma`) is proved only at α=0 (φ/2) and
  as an upper bound; numerical-only elsewhere — not a theorem, still open.
- Novelty of φ/2 = Γ̂(1/2) unchecked against Yu/Cambie (a source check).

None of the new sources changes these gaps; several tighten the ground under
them.

## Addendum — library digestion completion pass

Reran the coverage check: every substantive source in `research/summaries/`
now carries a fenced claim block. Three blocks added this pass to previously
claim-less sources (all re-derived straight into `derived/CLAIMS.md`):

- **`markovic-bozin-equivalence`** — Božin 2004's Frankl-equivalence via a
  probability MEASURE ON SETS (not per-element weights): UC holds iff for every
  IC family A and every p:A→[0,1] with per-element coverage ≥1−f_A(a),
  E[log|π_X(A)|]/log|A| ≥ 1/2. Distinct from, and more general than, Poonen's
  weights; exact equivalence, no constant/class. The (⇒) tensor-power
  construction is the least-verified link (asserted-by-source, handout only).
- **`nagel-kth-frequency-question`** — Nagel's Question 2.1, now resolved by
  Das–Wu (kth-most-frequent ≥ |F|/(2^{k−1}+1), equality near-k-cubes).
- **`nagel-interior-operator-equivalences`** — the interior-operator/
  congruence-recast theorems in Nagel §3.1, adjacent to bouchard-ucx-ladder.

Also re-confirmed current status: the `file-coupling-inf-and-bb-feasibility-claims`
task was already complete (claims `coupling-true-inf-crossing-4d` and
`coupling-interval-bb-infeasible-10s` both verified in the store via
`search_claims`, not by grepping the capped CLAIMS.md rendering). No
grep-of-rendering false-alarm this time: the missing blocks were verified via
`search_claims` before adding.
