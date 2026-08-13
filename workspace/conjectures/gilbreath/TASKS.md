# Tasks

## Directive 36 (steer): empirical route at ceiling — pivot to theoretical

The 1e9 run doubled the width from 6e8 and row-248 is STILL capped (floor=0, genuine=False,
b_land = W−248−1 exactly). The geometric fit says b_land doubles every 14.16 rows while gaps
are 9 to 64 rows, so each giant costs 1.5× to 8× the width of the last. At 1e9 (1.37 GiB, 185s),
two more giants would need 1e10–1e11 — exceeds the 8 GiB cap. **Do not queue a 2e9 or 4e9
run.** The remaining work is theoretical: Granville's ν_2 lower bound (Directives 32, 33) and
CHT Theorem 1.6 (Directive 35). Both are in `research/sources/` as `*-FULLPDF.full.md` and
have not yet been read.

### Immediate (in order)

- [ ] **1. Parity correction (Directive 36).** The 1e9 capture's parity p-value counted all 16
  giants including row 247 (genuine=False). Recompute on the 15 genuine giants only: 1 odd
  (161) of 15. Under uniform parity: p = (C(15,1)+C(15,0))/2^15 = 16/32768 = 4.883e-04.
  Against the measured (2,4)-event base rate 0.600: p = 0.0052. Quote the base-rate figure,
  not the fair-coin one. Update `research/threads/regeneration.md` and any stale captures.

- [ ] **2. Record the 1e9 settlement.** The run's real findings, worth having:
  - max gap is still 64. The 239→248 gap of 9 is noise; 64 at 175→239 stands.
  - ratio bound gap_i/(j_i+1) holds everywhere, max 1.2644e-02, none above 0.1.
  - rows 1..247 reproduce 6e8, rows 1..161 reproduce 2e7 — oracle passed.
  - row-248 is STILL capped: b_land = 50,847,285 = W−248−1, floor=0, jump ≥ 27,684,003.
  Write `code/out/1e9_settlement.md` with these four findings and the ceiling rationale.

- [ ] **3. Read Granville 2026 — Lemma 5.4 and Theorem 5.5.**
  `research/sources/granville-2026-piercing-gilbreath-FULLPDF.full.md` (175 KB). Produce a
  summary: Lemma 5.4 statement verbatim (the ν_2 criterion), Theorem 5.5 statement, the
  demand side (α=0.525 unconditional from BHP), what the published proof of Lemma 5.4
  discards (the delta=0 case), and whether the reduction to ν_2 > n^β with β > 0.525 is
  valid. Anchor: `research/notes/granville-2026-summary.md`.

- [ ] **4. Read CHT 2026 — Theorem 1.6 and the column restriction.**
  `research/sources/chase-hunter-tao-2026-cramer-random-model-gilbreath-FULLPDF.full.md`
  (98 KB). Produce a summary: Theorem 1.6 statement verbatim, the column restriction
  j ≥ N′ (= ⌊N/2⌋), the hypotheses (i)–(iii), the R_m − 3R_{m−1} threshold, and the
  authors' own difficulty assessment on p. 8. Anchor:
  `research/notes/cht-2026-summary.md`.

- [ ] **5. Re-derive Granville Lemma 5.4 with the delta=0 case handled.**
  The operator's notes document the gap: `lemma54-discarded-case-is-universal` — the published
  proof discards a case occurring in 100% of columns. Re-derive from scratch, prove it, and
  Lemma 5.4 becomes `proved` here. Anchor: `research/notes/lemma54-re-derived.md`.

- [ ] **6. Reproduce ν_2 numbers in-container.**
  `code/nu2_granville_check.py` → `code/out/nu2_granville_check.captured.txt`. Verify
  ν_2/n ≈ 0.49–0.52 measured above threshold.

- [ ] **7. Three-route comparison in `research/threads/regeneration.md`.**
  With the empirical route at ceiling, the theoretical routes are now the only live ones.
  Route B (Granville ν_2) has weakest demand side: BHP unconditional, ν_2 measured above
  threshold, Lemma 5.4 to re-derive. Route C (CHT deterministic) needs Cramér (open,
  stronger than BHP); authors' own assessment: "look difficult to establish rigorously."
  Route A (ratio bound) is the empirical fallback — holds with enormous slack to 15 giants
  but cannot be extended computationally. State the run is on Route B as primary.

### Directive 35 items (continue, lower priority than the pivot)

- [ ] **8. Measure right-half {0,d} blocks (Directive 35 item 1).**
  CHT Theorem 1.6(iii) restricts the {0,d}-block obstruction to columns j ≥ N′. Scan the
  6e8 data for {0,d} blocks with d ≥ 2 in the right half. Produce:
  `code/out/cht_right_half_0d_scan.captured.txt`,
  `research/notes/cht-right-half-scan.md`.

### Directive 34 items (continue, lower priority)

- [ ] **9. Read Arias de Reyna.** Anchor: `research/notes/arias-de-reyna-summary.md`.
- [ ] **10. Read Muney 2026.** Anchor: `research/notes/muney-2026-summary.md`.
- [ ] **11. Read BCZ 2023 filtered-rays + quasi-periodicity.**
- [ ] **12. Re-judge `granville-2026-piercing-gilbreath-not-load-bearing`.**

### Directive 31 items (continue, lowest priority)

- [ ] **13. Clear the unrun `.py` pile in `code/out/`.**
- [ ] **14. Hygiene: remove bare .txt duplicates in `code/pattern_finder/`.**

### Do not do

- **Do not queue a 2e9 or 4e9 sieve run.** The empirical route is at ceiling (Directive 36).
  State what width giant 16 would need and stop buying giants with sieve.
- **Do not re-run the CHT hypothesis check.** `holds-here: no` is final (Directive 35).

## Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved, checked, Lean 4 IFF sorry-free.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved.
- **Rule 90 interior (PROVED).**
- **Step law + recharge identity — PROVED, universal.**
- **1e9 giant record:** 15 genuine giants, max gap 64, ratio bound holds everywhere.
- **Row-248 STILL capped at 1e9:** b_land = 50,847,285 = W−248−1, floor=0, jump ≥ 27,684,003.
  Empirical route at ceiling — geometric doubling means next giant needs 1e10–1e11.
- **Edge-map invertibility — PROVED.**
- **CHT Theorem 1.6 hypothesis check — DONE:** `holds-here: no`. Column restriction
  j ≥ N′ means leading block at j=1 does not violate (iii).
- **Rule 90 depth prediction — CLOSED** (null computed).
- **Oracle:** `witnesses.json`, `blocks_depth1000.json`, `giants_6e8.json`,
  `giants_1e9.json`.
- **Library:** downloads halted. FRONTIER.md restored.

### Threads

- `research/threads/regeneration.md` — LIVE, PIVOTED (Directive 36): empirical route at
  ceiling. Primary target = Route B (Granville ν_2). Lemma 5.4 re-derivation is the next
  theoretical step. Route A (ratio bound) is empirical fallback. Route C (CHT) calibrated
  by authors' own difficulty assessment.
- `research/threads/rule90-regeneration.md` — CLOSED (null computed).