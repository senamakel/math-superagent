# Scholar cycle — verification pass and record reconciliation

What this scholar cycle contributed: the library is closed and every
load-bearing source was already digested to claim-block level, so the value
added this cycle is (a) hand-verification of an `asserted` load-bearing claim,
(b) reconciliation of a stale verification-bound figure in durable memory, and
(c) a recorded infrastructure defect in the memory graph.

## 1. Colonna deletion counterexample: `asserted` → `checked` by hand

The claim `colonna-deletion-left-edge-failure` — that deleting one prime
(5, 7, or 11) from the prime list gives a 2-then-odds sequence whose left edge
fails — was recorded as `asserted` (a record-page footnote). It is load-bearing:
it kills the plain bounded-gap general-class strategy at `g ≥ 4`, the concrete
companion to Eppstein's asymptotic anti-Gilbreath construction.

Verified by **exact hand arithmetic** on the nested absolute-difference
triangle (no program needed; the integers are tiny):

- **delete-11** `(2,3,5,11,13,17,19)`: gaps `(1,2,6,2,4,2)` (max 6).
  `A_1=(1,2,6,2,4,2)` — matches the source exactly. `A_2=(1,4,4,2,2)` —
  `A_2(1)=4 ∉ {0,2}`. `A_3(0)=|1−4|=3 ≠ 1` — **left edge fails at row 3**.
- **delete-5** `(2,3,7,11,13,17,19)`: gaps `(1,4,4,2,4,2)` (max **4**).
  `A_1=(1,4,4,2,4,2)` — `A_1(1)=4` escapes immediately at row 1. So gaps ≤ 4
  *and* left-edge-failing: sharpens the window to `g ≤ 3`.
- **delete-7** `(2,3,5,11,13,17,19,23)`: `A_2(1)=4`, `A_3(0)=3` — fails at row 3.

Mechanism (transparent from the arithmetic): a `{2,6}` adjacency at positions
1–2 of a row produces `|2−6|=4` at the next row's second entry, which then
kills the leading 1. This is why the `g≥4` bounded-gap carve-down fails.

Filed: `research/notes/colonna-deletion-verified.md` (claim block, status
`checked`); the older `asserted` block in library-state.md re-labelled
`colonna-deletion-left-edge-failure-archive` to remove the duplicate id from
CLAIMS.md.

**Bearing:** the surviving general-class hopes are `g ≤ 3` (whose only proved
case is the trivial consecutive-odds `g=2`) or a **non-gap** hypothesis (CHT's
2-separated non-concentration). No bounded-gap theorem with `g ≥ 4` can hold —
a result GOAL.md's "general class with gaps bounded by g" target must respect.

## 2. Verification-bound reconciliation: G=800 → G=811

Durable memory / CONTEXT.md carried "Colonna 1.5×10^15, G=800". ROOT.md carried
"G=811 at 1.2125×10^15". Resolved by reading the 2026-08 refresh of Colonna's
record page:

- Verified for **all primes < 1.5×10^15** (completed 2026-03-18; 57,600 G values).
- **Absolute records:** G(π(10^14))=693, G(π(2.8×10^14))=788, G(π(6.15×10^14))=800,
  G(π(10^15))=800, G(π(1.0025×10^15))=806, G(π(1.2075×10^15))=809,
  **G(π(1.2125×10^15))=811 (02/15/26) — current absolute record.**
- The relative (vicinity-only) records reaching G=1935 near 6×10^27 are
  exploratory 128-bit and **not** a verification bound.

So ROOT.md is correct and the "G=800" in CONTEXT.md/durable memory is the
outdated Jan-2026 figure. Stored the corrected record in durable memory.

## 3. Infrastructure: memory graph half is broken

`recall_memory` default (fused) returns a 404 (`NoDataError`, triplet embeddings
never built) on the graph half; `relate_memory` returns 409. Passage-only recall
(`strategy=passages`) and `remember_memory` work. This means no agent can
currently read the graph/connection half of Cognee — relationship lookups must
fall back to CLAIMS.md / ENTAILMENT.md. Recorded in durable memory so the run
works around it rather than re-failing the same calls. **Not a Gilbreath
finding**; if the memory store is rebuilt the triplet pipeline must be re-run.

## Sources re-confirmed as correctly digested (no action needed)

- **Gatti 2020** (Theorem-4 invalid, Lemma-4 interval-completeness refuted,
  valid-extension global formula): already fully digested with a located flaw;
  confirmed sound.
- **Lemke Oliver–Soundararajan 2016** (`los-2016-consecutive-pair-mod4-bias`):
  correctly marked `asserted` (the whole Main Conjecture is k-tuple/Hardy–
  Littlewood-level conjectural; only the one-point r=1 case is unconditional).
  This is the named-conditional hypothesis on which Route B's honest deliverable
  rests.
- **Blair Morgan 2026** (local-condition sufficiency, corridor obstruction):
  already digested; the elementary sufficiency proof is correct and matches the
  run's reduction.

## What the run still lacks

Not a digest gap — a genuine mathematical gap, already precisely stated:
**the supply-side linear bound ν₂ ≥ c·n** on the mod-4 switch bit (named open
via ABGS 2011 §9). No source supplies it unconditionally; Route B's deliverable
is the conditional theorem at the LOS/HL two-point level. The library is closed;
nothing new is fetchable.
