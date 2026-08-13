# Block-length growth, regeneration events, and renewal structure — what the library's sources cover

**Question (precise).** Has anyone studied the GROWTH of the leading `{0,2}` block length `b_k` under iterated absolute differences — specifically (i) the size/rate of regeneration events (block length increases), (ii) the distribution of jump sizes at such events, (iii) any claim that `b_k` grows roughly geometrically at regeneration events, or (iv) a renewal-process treatment of `b_k`?

**Method.** Library search only (per instruction: no new downloads; every claim below is from already-held sources under `research/sources/` or `research/summaries/`, plus the run's own computed records in `code/out/`). Searched via `search_claims`, `search_documents`, and direct reads of the named summaries (Odlyzko 1993, Killgrove–Ralston 1959, Chase 2024, CHT 2026, Eppstein 2011 (both posts), Arias de Reyna blog, OEIS A036262/A000232/A213014/A358691, plus Blair Morgan 2026, Agama 2021, Debono, Tao blog, Houston 2012, Caldwell, Colonna 2026).

## Verdict

**No held source — primary or secondary — studies the growth rate of `b_k`, the size/distribution of regeneration jumps, geometric growth, or a renewal-process treatment of the block length.** The literature covers exactly two blocks:

1. **Consumption/protection** (how much a `{0,2}` block guarantees the leading 1): Odlyzko 1993, Killgrove–Ralston 1959, Chase 2024 Lemma 3.2, CHT 2026 Lemma 3.7/3.8. All linear, not growth.
2. **Obstructions to decay** (long zero-blocks / long shallow `{0,d}`-blocks): CHT 2026 Thm 1.6, restated in the Tao blog. Concerning what *blocks* regeneration, not its rate.

Everything about *growth* — the `(2,4)`-event being the sole increase mechanism, jump sizes at those events, the block-length minima increasing with depth, the measured ~×1.68 per-giant-event geometric factor, the "giants arrive infinitely often" restatement — is this run's own, recorded in its threads/approaches, **not in the published literature**.

## Source-by-source

### (i) Regeneration events / size and rate of block-length increases

- **Odlyzko 1993** — **not covered.** Text (per `research/summaries/odlyzko-1993-iterated-absolute-differences.md`): the block lemma is the *longest* statement — "If for some N we find a K such that d_K(1)=1 while d_K(n)=0 or 2 for all 1≤n≤N, then d_k(1)=1 for K≤k≤N+K−1." This is consumption/protection only; Odlyzko defines G(n) (least row from which 1000 consecutive entries are 0/2) and verifies to `π(10^13)`, but **never tracks or comments on block-length increases**. No regeneration-event notion appears.
- **Killgrove–Ralston 1959** — **not covered.** Same linear block lemma (`P_{i,0}..P_{i+M−1,0}=1`), and P(i) (their name for A000232, the block length) is tabulated for i=0..95 — the *values* of `b_k` are published, but **no growth-rate/jump/renewal analysis of the P(i) sequence**.
- **Chase 2024** — **not covered as growth.** Lemma 3.2 is consumption of the maximum via `{0,d}`-blocks ("after L iterations the largest number is ≤ d−1"), i.e. the *decay* half again. No block-length increase / jump-size statement.
- **CHT 2026 (Chase–Hunter–Tao)** — **not covered.** Thm 1.6 isolates the two obstructions to decay (long zero-blocks, long shallow `{0,d}`-blocks). Lemma 3.7(iii) is `{0,d}`-closure/persistence — about *values*, and about how decay can fail, never about growth of the `{0,2}` block length or regeneration events. The mod-2 linearization (Lemma 3.10) is parity of entries, not block-length dynamics.
- **Eppstein 2011 (anti-Gilbreath / practical)** — **not covered.** Constructs sequences whose *right edge* escapes and re-enters 1 infinitely often (the escape threshold `g_i > s_i`), and the practical-numbers post discusses the Rule-90 interior, not block-length growth of the leading `{0,2}` block. Relevant as the standing anti-growth witness in the general class, but it contains no growth-rate statement about `b_k`.
- **Arias de Reyna blog** — **not covered.** Restates the K–R block lemma, G(n), Odlyzko's table, an empirical pseudo-prime model (P(GC)≈0.499, P(eventual-1)≈0.9916), and Chase's Theorem 1. No `b_k` growth analysis.
- **Blair Morgan 2026 (Return of the Lemma)** — **the closest.** Uses a "frontier" (leftmost position `≥1` with `G_r[k] ∉ {0,2}`), effectively `b_k` shifted by one, and records observed frontier positions: row 1 → 3, row 2 → 8, row 10 → 59, row 30 → 870, row 100 → >90,000. These are growth *data points* (someone outside this run has observed that the frontier increases with row), but **no rate, no jump/renewal treatment, no geometric claim** — the paper's content is the `{0,2}`-basin reduction, a single corridor-elimination obstruction, and the open Frontier Hypothesis (frontier never reaches position 4).
- **OEIS A000232 / A036262 / A213014 / A036277 / A358691** — **catalogue values only.** A000232 = "one less than the position of the first number larger than 2 in the n-th row" = the run's `b_k+1`; Hasler's A036262 comment (first term >1 must be 2; propagation of a ≥4 jump; GC ⟺ A036277(n) > A213014(n)+2) is the *mechanism* of the second entry, at the block-value level, not a growth-rate statement. A213014's descending runs 6,5,4,3,2,1,0 are the run's own verified erosion progression (consumption). **No OEIS entry studies how fast the A000232 terms grow, or the regeneration jumps.**
- **Run's own** (the growth content, all computed here): step law & recharge identity (proved, `research/notes/step_law_proved.md`); the 60 `(2,4)`-events at depth 1000 with jump sizes (median 4.5; 35/60 ≤ 1; giants j>1000: 12 genuine + 1 capped, largest measured 360,698) (`code/out/bigjump_characterization.notes.md`, `research/notes/regeneration_data.md`); block minima `[13,24,96,97,175,2762,5939,31525,31533,31534,733574,1094263]`; and the Directive-24 geometric fit (~×1.68 per giant event, R²=0.944 log-fit vs linear 0.783, 12 genuine points, rows 1..161) (`research/threads/regeneration.md`, `code/out/directive24_geometric_growth.md`).

### (ii) Distribution of jump sizes at regeneration events

**Not covered by any held source.** Jump sizes (the run's `j_i = b_{i+1} − b_i` at `(2,4)`-events) do not appear anywhere in the held literature. The closest catalogued quantity is the A000232/A036277 sequence itself, whose term-by-term increases are exactly the jumps, but OEIS records the values with no distributional/growth analysis, and no paper ties back to them.

### (iii) Geometric growth claim for `b_k`

**No published claim.** The only geometric-growth statement is the run's own measured fit (`research/threads/regeneration.md`, Directive 24). The OEIS b-file for A000232 (274 terms) makes the eventual growth empirically visible (3,8,14,14,25,…,4208,5943,23266,…,5,417,976,10,655,287,23,163,291,64,955,386,98,091,217) — an unmistakable geometric-ish staircase — but **nobody in the catalogue or literature says so or analyzes it**. The run's restatement "giants arrive infinitely often ⟹ GC" (`research/threads/regeneration.md`, `research/approaches/subadditive-growth-ergodic-block-length.md`) is internal, not sourced.

### (iv) Renewal-process treatment of `b_k`

**Not covered as published work.** The run's own approaches model it: `renewal-process-edge-flip-hitting-time` (inter-event gap = drain_time(y₀→4) + stall_time at y=4 + 1; grounded in Northshield 2010 / Malyshev 2021 for the XOR edge machinery) and `subadditive-growth-ergodic-block-length` (recharge identity as a renewal-reward process; criterion r·J > 1). Both are **adopted/proposed run directions, not literature**. The renewal vocabulary is the run's, not a source's. Note the subadditive-growth approach is marked **adopted** and renewal-process-edge-flip **grounded** — these names describe the run's project, and grounding here means "the proof engine exists in the literature", not that anyone solved the renewal question.

## Bearing on the run

- The geometric-growth direction is **completely unclaimed in the literature** — it is original to this run (as a measured statement). Nothing in any held source contradicts it; no source supports it either.
- Open REQUESTS row (regeneration rate / `(2,4)`-event lower bound) remains genuinely open and is the right target: "no source in existence proves or refutes a `(2,4)`-event rate lower bound" (research/REQUESTS.md). The geometric-growth claim downgrades the required bound to "giants arrive infinitely often" but does not remove the need for a structural source of the giants.
- If a future run wants a literature anchor for the renewal treatment, the technical machinery (mod-2 Pascal sums governing the edge XOR) is a named technique (Northshield 2010, Malyshev 2021 — cited in `renewal-process-edge-flip-hitting-time` precedent), but **not** the block-length renewal process itself.

## Claim

```claim
id: block-growth-literature-not-covered
statement: No held source — Odlyzko 1993, Killgrove–Ralston 1959, Chase 2024, CHT 2026, Eppstein 2011, Arias de Reyna blog, Blair Morgan 2026, Agama 2021, Debono, Tao blog, Houston 2012, Caldwell, Colonna 2026, or OEIS A000232/A036262/A213014/A036277/A358691 — studies the growth rate of the leading {0,2} block length b_k, the size/distribution of regeneration jumps, geometric growth of b_k, or a renewal-process treatment of b_k. The literature covers only (a) linear consumption/protection (block lemma, constant 1) and (b) obstructions to decay (CHT Thm 1.6: long zero-blocks / long shallow {0,d}-blocks). The closest external growth observation is Blair Morgan 2026's frontier positions (row 10 → 59, row 30 → 870, row 100 → >90,000) with no rate analysis. The geometric-growth measurement (~×1.68 per giant event, R²=0.944 log-fit, depth 1000) and the "giants arrive infinitely often" restatement of GC are this run's own, not sourced.
hypotheses: the leading {0,2} block length b_k of the iterated absolute-difference triangle; regeneration events = rows where b increases (the run's (edge,intruder)=(2,4) events); the named held sources.
holds-here: yes — this is a negative finding about the library's coverage; it bounds what any future claim can cite.
status: checked (library search over the held corpus; all named summaries and full-texts read or searched, plus search_claims/search_documents sweeps)
bearing: the geometric-growth/renewal direction is unclaimed and original to this run; a future attempt to ground it in the literature will find no precedent (a genuinely open direction). It also means the run must NOT cite the literature for any growth-rate statement — it must prove its own.
anchor: research/notes/block-growth-literature.md (this note); source reads: research/sources/odlyzko-1993-iterated-differences-latex-source.full.md, killgrove-ralston-1959-*, chase-2024-*, chase-hunter-tao-2026-*, eppstein-anti-gilbreath/practical-*, arias-de-reyna-gilbreath-blog, blair-morgan-2026-return-of-the-lemma, oeis-A000232/A036262/A213014/A036277/A358691
```