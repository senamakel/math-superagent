# Tasks

## Directive 5 (steer): Stop downloading. Deduplicate, check CHT hypotheses, test Rule 90 depth prediction.

### Immediate (in order)

- [ ] **1. Deduplicate the two doubled claims.** `cht-inverse-theorem` appeared twice in CLAIMS.md (once from `library-state.md`, once from `chase-hunter-tao-2026-full-html.md` summary) — the library-state copy has been renamed to `cht-inverse-theorem-library`. `valid-extension-nonlocal` appeared twice (once from `backward-extension-automaton.md`, once from `muney-2026-holes-valid-extension-html.md`) — the backward-extension copy has been renamed to `valid-extension-backward-nonlocal-refuted`. The summaries are the authority; CLAIMS.md is re-derived on each write. **CLAIMS.md has been regenerated** — verify the new names appear once each.

- [ ] **2. CHECK CHT Theorem 1.6 hypotheses against the real prime rows — the directive's main demand.** `cht-inverse-theorem` has `holds-here: unchecked` in both copies. This is the trap: a true theorem whose hypotheses fail here looks like progress.

  Take the actual prime-difference triangle to depth 1000 (sieve 2e7). CHT Theorem 1.6 needs:
  - `a_n ≤ 2^M` — what is M for the normalized gaps a_n = (p_{n+2}−p_{n+1})/2 − 1?
  - No 0-block of length L. What is the longest run of consecutive 0s among the a_n in the window?
  - No {0,d}-block (2^{M−m} < d ≤ 2^{M−m+1}) of length ≥ R_m − 3R_{m−1} at depth ≤ 2R_{m−1}, with R_m ≥ 4R_{m−1}, R_0 ≥ 100L·8^M.
  - Compute M, L, R_0 for the actual data. Is R_0 ≥ 100L·8^M satisfiable at any depth the run can reach?

  If R_0 is astronomically larger than 1000 rows, set `holds-here: no (R_0 = X ≫ 1000, theorem does not bite at reachable depths)` with the numbers. If the hypotheses are satisfiable, set `holds-here: yes` with the computed parameters. Either way, report the numbers — "unchecked" is unacceptable on a claim that drives the obstruction analysis.

  Source: `code/out/blocks_depth1000.json`, `research/sources/chase-hunter-tao-2026-full-html.full.md` (Theorem 1.6).

- [ ] **3. Test Rule 90 depth prediction against block-length minima.** Rule 90 interior XOR evolution (proved, `research/notes/rule90-interior.md`) gives: at depths d = 2^j, binom(2^j, m) ≡ 1 (mod 2) for all m, so halved entries are the XOR of a width-(2^j+1) window. If XOR = 1 for a stretch, the original row is all-2 — a regenerated block.

  Minima record: [13, 24, 96, 97, 175, 2762, 5939, 31525, 31533, 31534, 733574, 1094263] (these are block-length *values*, not row indices).

  Test: for each local minimum, compute the row index k, find the depth from the start of the current block regime (the row where the block was last at a minimum), and check whether that depth equals 2^j or 2^j ± 1. Also test whether block expansion events (b_{k+1} ≫ b_k) occur at depths near powers of 2.

  Write the program, parallelise over hypothesis variants (`code/lib/parallel.py`, 28 CPUs), report match/mismatch with exact k and depth values. A match is a structural regeneration mechanism (partial result). A clean mismatch with exact numbers is also a result — it tells us the XOR-window explanation is not the whole story.

- [ ] **4. Formalise the difference operator in Lean 4.** Define the operator, prove (odd, even, even, ...) shape preservation, reduce to {0,2} second-entry claim as a machine-checked lemma. Report `#print axioms` and every remaining `sorry`. This is independent of items 2–3 and can run in parallel.

### Background (established, do not redo)

- **Reduction:** A_k(1) ∈ {0,2} ⇔ conjecture. Proved and checked to depth 599.
- **Block lemma:** constant = 1 (n+1 rows per length-n block). Proved, verified exhaustively, checked against real rows. `research/notes/block_lemma.md`.
- **Rule 90 interior (PROVED, split from refuted absorption wrapper):** `research/notes/rule90-interior.md`. Within any {0,2} block, halved entries evolve under XOR = Rule 90 = Pascal mod 2. The d-step formula is exact, verified n ≤ 13. The absorption wrapper stays refuted in `research/approaches/rule90-absorbing-boundary.md`.
- **Regeneration criterion:** b_{k+1} ≥ b_k ⟺ (A_k[b_k]==2 AND A_k[b_k+1]==4). Established to depth 1000, zero failures, 60/60 events match. `code/out/check_regenerate_lemma.captured.txt`.
- **Minima record (depth 1000):** block lengths at local minima = [13, 24, 96, 97, 175, 2762, 5939, 31525, 31533, 31534, 733574, 1094263].
- **Oracle:** `witnesses.json` (depth 600) and `blocks_depth1000.json` (depth 1000).
- **Library state:** downloads halted per directive. 92 sources on disk, 3 checked (FRONTIER.md checked column stuck at 3). No more downloads until a specific gap is stated that a source could close.
- **Lean 4 and Mathlib:** not yet started. Blocking: none.

### Threads

Two live threads:
- `research/threads/rule90-regeneration.md` — test depth d=2^j prediction against block-length data (item 3 above).
- `research/threads/regeneration.md` — the honest open question: is there a k with block length 0? Local criterion established; recurrence mechanism still open.