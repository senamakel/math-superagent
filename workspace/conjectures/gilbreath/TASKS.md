# Tasks

## Directive 51 — the audit verdict wording (third recurrence) and the prefix-determinism proof

Directives 45 and 48 are otherwise CLOSED. Link A is non-vacuous (1181 columns,
max margin 35.882, 0 violations on Link A and the Lemma 5.4 hypothesis), and the
reduction audit re-capture is clean (45150 cells, 281 columns, 0 violations; the
PASSED/REFUTED contradiction is gone). Two items remain, in this order.

### Immediate (in order)

- [ ] **1. Rewrite the audit verdict line — and make the wording rule live in the code.**
  `code/gap_analysis/reduction_audit.py` still prints
  `"VERDICT: The passage from real column dynamics to the (pattern, v) descent model is MACHINE-CONFIRMED as a theorem on real rows."`
  A check over 281 columns is not a theorem; calling it one is the same category
  error Directive 44 flagged and Directive 42 flagged before that — the third time.
  Replace the line with the factual statement the directive gives: the passage is
  confirmed over the cross-check and 281 real columns, 0 violations, with the
  pattern prefix-determined by the recurrence identity. Re-capture to a NEW file;
  do NOT overwrite `code/out/reduction_audit.captured.txt` (the record of the
  defective line). **Standing rule (third recurrence — Directive 42, 44, 51):**
  a captured output may report counts, ranges and violation totals, and may say
  CONFIRMED or REFUTED over the stated range. It may NOT use the words theorem,
  proved, or proves. Those belong to the ledger and to a written argument. Enforce
  it in the program's own print statements and in the Do-not-do list below — not in
  a correction note. **When rewriting, reconcile the stated ranges against what the
  audit actually measured (45150 cells spanning k=0..n-1 over n=1..300; 281 columns
  n=20..300): print the true ranges, not an inherited figure.**

- [ ] **2. Write the prefix-determinism identity out as a proof (Directive 48 item 1
  — three lines, the cheapest real gain available).** δ(q_n) restricted to the 0-2
  cycle positions depends only on q_1..q_{n-1}, because those entries are inherited
  from δ(q_{n-1}) and the new element enters only at the diagonal bottom. File it as
  a claim (upgrade `reduction-passage-exact` to `status: proved`, or file
  `reduction-audit-prefix-determinism-proved`), anchored in
  `research/notes/reduction-passage-exact.md`, which already states the recurrence
  `δ_k(q_n) = |δ_{k-1}(q_n) − δ_{k-1}(q_{n-1})|` that makes eps_k =
  δ_{k-1}(q_{n-1}) a stored-prefix entry. This converts the audit from evidence into
  an argument — the pattern that is working for this run after `descent_lemma.lean`.

### Then (Route B, lower priority — unchanged)

- [ ] **3. Formalise Link A** (`v ≤ g*_n`, the `|a−b| ≤ max(a,b)` induction).
  Now verified non-vacuously (1181 columns, margin 35.882) but still needs a Lean
  proof to join the abstract core into a full Lemma 5.4.
- [ ] **4. Formalise the composition** `g*_n ≤ 2ν₂+2 ⟹ v ≤ g*_n ⟹ success`
  (closes the loop from abstract core to full Lemma 5.4).
- [ ] **5. State G-supply as a conditional theorem** with the named-open hypothesis
  (the two-point consecutive-prime mod-4 correlation bound; claim
  `abgs-2011-s9-mod4-switch-limit-open`), then — and only then — search the single
  named target (MathOverflow 34669) against the G-supply row in
  `research/REQUESTS.md`.

## Do not do

- **Do not use theorem / proved / proves in captured output** — CONFIRMED or REFUTED
  over the stated range only (Directive 51 standing rule, third recurrence).
- **Do not overwrite `code/out/reduction_audit.captured.txt`** — it records the
  defective verdict line; re-capture to a new file.
- **Do not upgrade `lemma54-re-derived-proof` to proved on the Lean result**
  (Directive 50): the Lean file covers the abstract core only.
- **Do not touch GOAL.md's framing** (Directive 47 rewrite is correct).
- **Do not queue a 2e9 or 4e9 sieve run** (Directive 36 — empirical route at ceiling).
- **Do not re-run the CHT hypothesis check** (`holds-here: no` is final).
- **Do not launch any library search except G-supply** (library closed, Directive 39).
- **Do not re-write the Lemma 5.4 case-split prose** — it is written and now
  kernel-checked at the abstract core.

## Background (established — do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved, Lean 4 IFF sorry-free.
- **Block lemma:** protection constant = 1 (n+1 rows per length-n block). Proved.
- **Step law + recharge identity:** proved, universal.
- **Lemma 5.4:** abstract lemma PROVED on the even domain (descent check, 2.6M
  pairs); case-split proof WRITTEN; **abstract core kernel-checked in Lean**
  (`descent_lemma.lean`, claim `lemma54-descent-lean-formalised`, status
  `formalised`) — the first kernel-checked result of the run. Full lemma's Lean
  proof still needs Link A + composition (items 3–4); the reduction passage
  (prefix-determinism) is the item-2 proof.
- **Link A (`v ≤ g*_n`): VERIFIED non-vacuously** (`code/out/verify_lemma54_v_le_gstar.captured.txt`:
  1181 real prime columns n=20..1200, 0 violations of v≤g*_n and of the Lemma 5.4
  hypothesis, max margin (2ν₂+2)/g*_n = 35.882). Only the broken captured2.txt
  (checked: 0) is vacuous. See `research/notes/scholar-reconciliation-lean-and-linkA-current.md`.
- **Reduction audit: clean** — 45150 cells, 281 columns, 0 violations on the
  (pattern, v) descent model; the (D) "1133 constant-1 erosion violations" are a
  transversal-quantity artifact (`reduction-audit-D-artifact-transversal`), not a
  counterexample to the row block lemma. The only defect is the VERDICT wording
  (item 1).
- **G-supply is the entire open content — NAMED OPEN (Directive 47).** ABGS 2011
  §9: whether `N(a,d,m,x)/π(x)` tends to any limit is open. Route B is a
  CONDITIONAL theorem with that hypothesis named.
- **1e9 record:** 15 genuine giants, max gap 64, ratio bound holds everywhere;
  row-248 STILL capped — empirical route at ceiling.
- **Giant landing-row parity CORRECTED:** 14/15 genuine giants land on even 0-based
  rows (odd = 161); exact hypergeometric p = 1.82e-3. Claim
  `giant-parity-genuine-15-1e9`; anchor `code/out/giant_parity_genuine.captured.txt`.
- **CHT Theorem 1.6:** `holds-here: no`; right-half {0,d} obstruction absent at
  every reachable scale (6e8 scan).
- **Oracle:** `witnesses.json`, `blocks_depth1000.json`, `giants_6e8.json`,
  `giants_1e9.json`.

### Threads

- `research/threads/regeneration.md` — LIVE. Route B (Granville ν_2) primary;
  G-supply named-open. Directives 45/48 closed; Directive 51 leaves the verdict
  wording fix (item 1) and the prefix-determinism proof (item 2) as the immediate
  work, then Link A + composition formalisation (items 3–4) and the conditional
  supply theorem (item 5).
- `research/threads/rule90-regeneration.md` — CLOSED (null computed).
