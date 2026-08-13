# Tasks

## Directive 10 (steer): Frontier restoration — DONE. Gatti classified. Filter active.

### Immediate (in order)

- [x] **1. Restore FRONTIER.md from recovered 42 rows.** `research/FRONTIER.md` rewritten from `research/notes/frontier-recovered-2026-08-13.md` (commit db36fc23). 42 rows, plus 418 not-shown singletons. Filter header active — share/bookmark URLs dropped before write.

- [x] **2. Add share/bookmark filter to FRONTIER.md.** Patterns `intent/tweet`, `sharer.php`, `shareArticle`, `/submit?url=`, `BibtexHandler`, `/import/?url=`, `follow/publon`, `/follow/` are dropped. Header reports drops. One bad page cannot replace the frontier again.

- [x] **3. Record collapse-as-failure-signal.** `research/notes/frontier-collapse-alarm.md`: a >30% drop in candidate count on rewrite means the output is garbage — one wrapper page with navigation chrome.

- [x] **4. Classify Gatti 2020 as not-load-bearing.** Same class as granville-2026-piercing-gilbreath-not-load-bearing. Theorem 4 proof located invalid (assumes conclusion), Lemma 4 refuted by Muney 2026, valid-extension machinery already extracted. The download destroyed the frontier; the filter prevents recurrence. 21,041-byte full text has no lemma testable against blocks_depth1000.json. Claim `gatti-2020-not-load-bearing` in `research/notes/library-state.md`.

- [ ] **5. Deduplicate the two doubled claims.** `cht-inverse-theorem` appeared twice in CLAIMS.md — both copies now have `holds-here: no` with computed R_0 = 419,430,400 ≫ 1000. Verify once that CLAIMS.md reports it once. `valid-extension-nonlocal` appeared twice — verify the new names appear once each.

- [ ] **6. CHECK CHT Theorem 1.6 hypotheses against the real prime rows.** `cht-inverse-theorem` has `holds-here: no (R_0 = 419,430,400 ≫ 1000)` per `code/out/cht_hyp_check.captured.txt`. This is already done — verify the capture is in context and no re-run is needed.

- [ ] **7. Test Rule 90 depth prediction against block-length minima.** Rule 90 interior XOR evolution (proved, `research/notes/rule90-interior.md`) gives: at depths d = 2^j, binom(2^j, m) ≡ 1 (mod 2) for all m, so halved entries are the XOR of a width-(2^j+1) window. If XOR = 1 for a stretch, the original row is all-2 — a regenerated block.

  Thread `research/threads/rule90-regeneration.md` status: the relative-depth null check (`code/out/null_rule90_depth.captured.txt`) found mild tol=1 concentration (p=0.017) but no signal at tol=0 — thread tagged as needing a different angle on the depth prediction. The directive may be asking for a fresh test: look at block EXPANSION events (b_{k+1} ≫ b_k) and check whether those depths are near powers of 2 rather than block-length minima depths.

  If re-running: use `code/rule90_test/analyze_rule90_depth.py` against `code/out/blocks_depth1000.json`, parallelise over hypothesis variants (`code/lib/parallel.py`, 28 CPUs), report match/mismatch with exact k and depth values.

- [ ] **8. Formalise the difference operator in Lean 4.** Define the operator, prove (odd, even, even, ...) shape preservation, reduce to {0,2} second-entry claim as a machine-checked lemma. Report `#print axioms` and every remaining `sorry`. This is independent of items 5–7 and can run in parallel.

### Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved and checked to depth 599.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved, verified exhaustively, checked against real rows. `research/notes/block_lemma.md`.
- **Rule 90 interior (PROVED):** `research/notes/rule90-interior.md`. Within any {0,2} block, halved entries evolve under XOR = Rule 90 = Pascal mod 2. The d-step formula is exact, verified n ≤ 13.
- **Regeneration criterion:** b_{k+1} ≥ b_k ⟺ (A_k[b_k]==2 AND A_k[b_k+1]==4). Established to depth 1000, zero failures, 60/60 events match.
- **Minima record (depth 1000):** block lengths at local minima = [13, 24, 96, 97, 175, 2762, 5939, 31525, 31533, 31534, 733574, 1094263].
- **CHT Theorem 1.6 hypothesis check — DONE.** M = ceil(log2 89) = 7, L = 2, R_0 = 100·L·8^M = 419,430,400 ≫ 1000. Theorem does not bite at reachable depths. `holds-here: no`. Captured: `code/out/cht_hyp_check.captured.txt`.
- **Oracle:** `witnesses.json` (depth 600) and `blocks_depth1000.json` (depth 1000).
- **Library state:** 92 sources on disk. Gatti 2020 classified not-load-bearing (same class as granville-2026). FRONTIER.md restored. Filter active. No more downloads until a specific gap is stated that a source could close.
- **Lean 4 and Mathlib:** not yet started. Blocking: none.

### Threads

Two live threads:
- `research/threads/rule90-regeneration.md` — test depth d=2^j prediction against block-length data (item 7 above). Null check done, tol=1 signal marginal, tol=0 dead. Expansion-event angle may differ.
- `research/threads/regeneration.md` — the honest open question: is there a k with block length 0? Local criterion established; recurrence mechanism still open.