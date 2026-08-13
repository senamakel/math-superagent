# Tasks

## Directive 11 (steer): Fix event-rate sweep, persist stats, rerun.

### Immediate (in order)

- [ ] **1. Rerun the event-rate sweep with the fixed code.** The format-string crash (`NoneType.__format__`) is patched, and stats are now persisted to `code/out/event_rate_stats.jsonl` before `report()` is called. Run:
  ```
  timeout 540 python3 code/event_rate/event_rate_sweep.py 2>&1 | tee code/out/event_rate_sweep.captured.txt; echo EXIT_CODE=$?
  ```
  On the mathematics: `rho_live` and `rho_rows` measured on rows 1..161 are statements about rows 1..161. To argue the {0,2} regime persists, say explicitly what makes the rate a lower bound for all k rather than an observed frequency. Consumption is not regeneration.

- [ ] **2. Deduplicate the two doubled claims.** `cht-inverse-theorem` appeared twice in CLAIMS.md — both copies now have `holds-here: no` with computed R_0 = 419,430,400 ≫ 1000. Verify once that CLAIMS.md reports it once. `valid-extension-nonlocal` appeared twice — verify the new names appear once each.

- [ ] **3. CHECK CHT Theorem 1.6 hypotheses — already done.** `cht-inverse-theorem` has `holds-here: no (R_0 = 419,430,400 ≫ 1000)` per `code/out/cht_hyp_check.captured.txt`. Verify the capture is in context and no re-run is needed.

- [ ] **4. Test Rule 90 depth prediction against block-length minima.** Rule 90 interior XOR evolution (proved, `research/notes/rule90-interior.md`) gives: at depths d = 2^j, binom(2^j, m) ≡ 1 (mod 2) for all m, so halved entries are the XOR of a width-(2^j+1) window. If XOR = 1 for a stretch, the original row is all-2 — a regenerated block.

  Thread `research/threads/rule90-regeneration.md` status: the relative-depth null check (`code/out/null_rule90_depth.captured.txt`) found mild tol=1 concentration (p=0.017) but no signal at tol=0 — thread tagged as needing a different angle on the depth prediction. Test block EXPANSION events (b_{k+1} ≫ b_k) and check whether those depths are near powers of 2 rather than block-length minima depths.

  If re-running: use `code/rule90_test/analyze_rule90_depth.py` against `code/out/blocks_depth1000.json`, parallelise over hypothesis variants (`code/lib/parallel.py`, 28 CPUs), report match/mismatch with exact k and depth values.

- [ ] **5. Formalise the difference operator in Lean 4.** Define the operator, prove (odd, even, even, ...) shape preservation, reduce to {0,2} second-entry claim as a machine-checked lemma. Report `#print axioms` and every remaining `sorry`. This is independent of items 2–4 and can run in parallel.

### Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved and checked to depth 599.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved, verified exhaustively, checked against real rows. `research/notes/block_lemma.md`.
- **Rule 90 interior (PROVED):** `research/notes/rule90-interior.md`. Within any {0,2} block, halved entries evolve under XOR = Rule 90 = Pascal mod 2. The d-step formula is exact, verified n ≤ 13.
- **Regeneration criterion:** b_{k+1} ≥ b_k ⟺ (A_k[b_k]==2 AND A_k[b_k+1]==4). Established to depth 1000, zero failures, 60/60 events match.
- **Minima record (depth 1000):** block lengths at local minima = [13, 24, 96, 97, 175, 2762, 5939, 31525, 31533, 31534, 733574, 1094263].
- **CHT Theorem 1.6 hypothesis check — DONE.** M = ceil(log2 89) = 7, L = 2, R_0 = 100·L·8^M = 419,430,400 ≫ 1000. Theorem does not bite at reachable depths. `holds-here: no`. Captured: `code/out/cht_hyp_check.captured.txt`.
- **Oracle:** `witnesses.json` (depth 600) and `blocks_depth1000.json` (depth 1000).
- **Library state:** 92 sources on disk. Gatti 2020 classified not-load-bearing. FRONTIER.md restored. Filter active. No more downloads until a specific gap is stated that a source could close.
- **Lean 4 and Mathlib:** not yet started. Blocking: none.
- **Event-rate sweep bug:** format-string crash on None rl/rr after 135s/26 workers — FIXED. Code now builds `rls`/`rrs` strings and persists `stats_list` to `code/out/event_rate_stats.jsonl` before calling `report()`. Rerun is item 1.

### Threads

Three live threads:
- `research/threads/regeneration.md` — the honest open question: is there a k with block length 0? Step law and recharge identity are exact; conjecture is now an event-rate inequality. Route A (combinatorial bound on max erosion between events) and Route B (analytic bound from prime gaps).
- `research/threads/rule90-regeneration.md` — test depth d=2^j prediction against block-length data (item 4 above). Null check done, tol=1 signal marginal, tol=0 dead. Expansion-event angle may differ.
- `research/threads/event_rate_lower_bound.md` — the event-rate sweep fix; rerun and report.