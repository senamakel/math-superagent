# Convergence decision — quasianalytic displacement module (Rolin–Servi)

**Round:** inventor convergence, 2026-08-18. Candidates under decision:
`abel-bautin-ideal-finite-cyclicity`, `darboux-liouvillian-integrability-certificate`,
`parametric-ominimality-nonhyperbolic-graphics` — all three refuted by research
(verdicts written by research into the three files, with `killed-by` and `survives`).

**Decision:** ADOPTED the synthesis `quasianalytic-displacement-module-rolin-servi`
(`research/approaches/quasianalytic-displacement-module-rolin-servi.md`).
This note is the durable memory record (Cognee endpoint down at time of writing;
store via `remember_memory` when it recovers).

## The structural insight (why this and not a re-proposal)

The three refutations each named a *different container* for the four-second-type
Dulac-map sum of an open DRR graphic's displacement, and each failed at the
**same place**:

| Candidate | Container it wanted | The shared failure |
|---|---|---|
| Abel/Bautin | scalar Abel Bautin ideal | not closed under the four-map sum; Composition Conjecture false; Smale–Pugh open; graphics are a two-equation problem (RR 2015) |
| Darboux/Liouvillian | Liouvillian divergence integral | Liouvillian ⇏ finite zeros (`sin(1/x)`); DI₂a NOT closed (ADL 2009 partial only) |
| o-minimality | L_trans definability | L_trans o-minimality IS the open conjecture; proved case NRH_d only (KRS 2009) |

The shared failure decomposes into three properties no tried container had all of:
**closure under addition** (ECT fails this: `(1,x)+(−1,−x)=0`),
**stability under specialization** (ECT Wronskian rank collapses at `a=0`),
and a **zero theorem on every stratum including vanishing slow-divergence**.

The Rolin–Servi generalized quasianalytic algebra (PLMS 110 (2015) 773–825,
doi:10.1112/plms/pdv010; Servi AIF 65 (2015), doi:10.5802/aif.2933) is o-minimal
— hence closed under addition, composition, AND specialization, with the definable
zero property — and contains Dulac-type transition maps. It is proved-closed,
research-surfaced, and **never tested on an open graphic's full four-map
displacement**. Multisummability of the passages (Ilyashenko Centennial History
Thm 4.12; Écalle accelero-summation) is the input class and where analyticity
bites (Test 1: a C^∞ field has no multisummable Dulac expansion, hence no algebra
membership, hence no zero theorem — Dulac's error made precise).

## Named falsifiers (from the approach file)

- (a) The four second-type maps are not multisummable in the SAME algebra
  (non-gluing Stokes sectors) → narrows to individual-finiteness (Écalle–Ilyashenko).
- (b) Summed displacement has no finite-rank module structure → o-minimality gives
  non-constructive finiteness only, not a Lean-finishable bound.
- (c) Vanishing slow-divergence stratum gives identically-zero displacement →
  must stratify → that IS the DRR program → refuted as a uniform route.

## First executable step (tool_builder)

For I^1_6b, take the four second-type Dulac maps from the held RR 2015 /
Shan 2013 blow-up, verify each is multisummable (hence in a Rolin–Servi
quasianalytic algebra), then form their SUM and verify the sum stays in the
same algebra. Deliverable = membership certificate, not a zero count.
Capture to `code/out/quasianalytic_displacement_module.captured.txt`.

## Lineage pointers written into the closed files

- `abel-...`: survives-line now points to the synthesis as repairing the
  container failure (closure under addition).
- `darboux-...`: survives-line names the synthesis as supplying the missing
  non-oscillatory class (o-minimal ⇒ zero property).
- `parametric-ominimality-...`: survives-line names the Rolin–Servi sub-structure
  as the synthesis's foundation (strictly weaker than L_trans, testable).

## Cataloguing caveat (2026-08-18, this round)

The Cognee endpoint is down (health check timing out; `remember_memory` refused with
"write it to the workspace instead"). `research/` is catalogued through Cognee, and
the approaches ledger render derives from that cataloguing: as of this writing
`derived/APPROACHES.md` still holds 62 entries and does NOT display
`quasianalytic-displacement-module-rolin-servi`, although the file exists on disk
with a well-formed fenced `approach` block, `slug`, and `status: adopted` (verified
by `read_document`). The three refuted candidates likewise carry their `killed-by`
in their files whether or not the render shows them. When Cognee recovers: re-derive
the ledger (any `write_document` under `research/` triggers it) and store this note
via `remember_memory`.

## Collateral correction (from research, to be applied by summaries owner)

`research/summaries/huzak-cyclicity-degenerate-df2a.md` carries the WRONG DOI
`10.3934/cpaa.2018062` (actually Mallick–Shivami–Son–Sundar, p-Laplacian).
Correct: **`10.3934/cpaa.2018063`** (Huzak, CPAA 17 (2018) 1305–1316).
Already corrected in `research/approaches/darboux-liouvillian-integrability-certificate.md`
precedent list and flagged in the board post.
