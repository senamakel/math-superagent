# Scholar digest report — round 2 (post-research-agent)

## State of the library

The reference library on disk is mature and fully digested. All 42 source files
under `research/sources/` have a matching claim-block digest under
`research/summaries/`. `research/ROOT.md` (GOAL criterion 1), `CLAIMS.md`,
`THREADS.md`, `APPROACHES.md`, `BLUEPRINT.md`, `ENTAILMENT.md` are populated.
No source is undigested; the run is at the gap-driven steady state.

## The one systemic problem found: durable memory is non-functional

`remember_memory` accepts stores (returns a note id) but `recall_memory`
returns `NoDataError` on every read — the 7th such failure across the run, and
`relate_memory`'s graph store is empty. So **nothing a prior pass (or this
pass) stores in Cognee is retrievable, and the on-disk library is the run's
only effective durable store.** The `Recalled` section of CONTEXT.md ("None")
is an artefact of this, not of an empty run history. Consequences:

- The scholar report from round 1 claims "13 notes stored to Cognee"; those
  notes may or may not have persisted, but they cannot be recalled. All durable
  knowledge is on disk, not in memory.
- The correct mitigation: keep the on-disk claim blocks as the source of
  truth, keep calling `remember_memory` on every durable finding (write side
  works, so if/when the read side recovers the history is there), and do NOT
  re-derive anything that a claim block already establishes.

## Load-bearing derived arithmetic, re-confirmed by hand

Two computed-by-construction numbers this run reports rest on arithmetic I
re-checked against the written record (the `.py` and `.out` files are on disk):

- **Pirzada orders** `|G_i| = 2^{i+6} − 34`: G1=2^7−34=94, G2=2^8−34=222,
  G3=2^9−34=478 — all three match the paper's own orders. The *printed*
  recurrence `|G_i|=|G_{i-1}|+2^{i+4}` gives 158/350, so it is a typo; the
  correct step is `+2^{i+5}` (94+128=222, 222+256=478). Consistent with
  `code/out/verify_pirzada_orders.py` and the summary.
- **2/3 degree-fraction** `|V3| ≥ 2|V≥4|+1 ⟹ >2/3 of vertices degree 3`: with
  |V|=|V3|+|V≥4|, the inequality gives |V≥4| ≤ (|V3|−1)/2, so
  |V| ≤ (3|V3|−1)/2, i.e. |V3| ≥ (2|V|+1)/3 > 2|V|/3. ✓ Sound deduction from
  Carr's proved Cor 0.1. Recorded `derived`, not Lean-checked — correct to
  keep it there.

Neither is flawed; both are genuine strengthening/near-counterexample results.

## Contradictions (already surfaced in CLAIMS.md — reconfirmed)

- **Gebendorfer 2026 full-proof abstract** ("δ≥3 forces a C4 or C8") is
  contradicted by Markström's four 24-vertex cubic no-C4-no-C8 graphs, Exoo's
  78/540-vertex no-{4,8,16}(,32) graphs, and Exoo's G420 (inside the settled
  3-connected cubic planar class). Full text unobtainable (410/404). Treat
  conjecture as open; do not cite the preprint.
- **Pirzada Conclusion** over-claims (circular: invokes the conjecture). Cite
  only the construction.
- **Pirzada printed recurrence** contradicts its own orders (typo).

## Sources that do not help (recorded so nobody re-reads)

- OEIS A280939 — no connection to the problem.
- Exoo image-only subpages (G24a/G24b/N46/N4610/N468/N4832) — image data;
  substantively the index page already held.
- Verstraëte 2016 survey body — paywalled, bibliography only.
- Cayley-graph classes — settled but high-symmetry, weak structural transfer.

## What the run still lacks (unchanged from round 1)

- Independent check of the 2/3 degree-fraction (derived, not Lean-formalised).
- The live SAT question: does a δ≥3, n≥32 graph with independent degree-≥4 set,
  all others degree 3, no C4/C8/C16 exist? UNSAT would be a genuine structural
  theorem. This is the concrete next step.
- The run's oracle has not independently reproduced Balaji's n≤31 bound
  (only n≤8 2-connected / n≤16 baselines are the run's own).
