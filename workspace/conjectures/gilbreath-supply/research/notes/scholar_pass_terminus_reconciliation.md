# Scholar pass — library reconciliation at the terminus

Author: scholar. Scope: read `research/` against GOAL, the task ledger, and the
current beliefs, after the research agent finished. Since the last reconciliation
(`scholar_pass_newest_library_reconciliation`, directive-30 tick) the run has
moved from "library mature, no undigested source" to **terminus** (directive 33):
`research/CONCLUSION.md` exists, closes the single hypothesis as REFUTED, and
opens no new line of work.

## Headline finding

**There is no undigested or new claim-bearing source in `research/`.**
Cross-checking the two listings (this pass): every full text under
`research/sources/` has a matching, claim-bearing digest under
`research/summaries/`, and every one of the 51 claim blocks (`grep '^id:'`
across the summaries, 40 files) is on disk with its statement, hypotheses,
holds-here, status, and anchor. The genuine "new material since the last
reconciliation" is not a source but the run's own terminus deliverable
(`CONCLUSION.md`) and the pattern-finder genericity work it anchors.

## What the newest research/ material establishes

**`research/CONCLUSION.md` — the run's answer is NO.** Establishes, each with a
fenced claim block already landed in `research/ROOT.md` and rendered into
`research/CLAIMS.md` (verified this pass: `goal-hypothesis-refuted-fold-adds-nothing-measurable`,
`sixth-door-no-nu2-statistic-prime-specific` both present):

- The single hypothesis (does the fold `Φ` do work the switch-density form
  cannot see) is **REFUTED**, measured-not-proved: matched iid strings at prime
  switch density `p≈0.585` reproduce the primes' dip counts and last-dip
  positions essentially exactly (c=0.45 last-dip ≤7000: primes 763 vs random
  699–996; c=0.48: primes 5655 vs random 5595–6989). No measurable `ν₂`
  regularity is prime-specific; the primes sit in the generic-balanced-good
  class.
- A **sixth closed door** is added: "no `ν₂` statistic is prime-specific."
- The survived-open statement is exactly `E[S(n)²]=O(n)` (equivalently a
  submask-window Walsh/second-moment bound) on the specific prime gap-parity
  string — the parity barrier, unreachable by measurement.

**The implications for this run's goal/tasks/beliefs:** consistent with and
completing the durable belief that the open request `walsh-spectral-subset-b904`
is the single surviving arithmetic statement, and that the run's priority-1/2
lines are measured-but-not-proved rather than sources. No belief changes; the
CONCLUSION confirms the state recalled from the ladders and requisition ledger.

## Confirmations of durable memory (no contradictions found)

- `recall_memory` is broken this run (Cognee 404 / "No data found", 16 recorded
  failures). This pass relied on on-disk ladders and search_claims instead.
  **No on-disk source contradicts a held claim.** The two stale "contradictions"
  rows in CLAIMS.md (`rw-not-the-submask-xor-fold` vs a misspelled non-existent
  `rw-described-as-the-fold-itself`; `r-finite-verified` id mismatch) remain
  self-resolved bookkeeping artefacts, as prior passes recorded.
- The `mauduit-rivat-*`, `shiu-string-theorem`, `takei-rule90-...`,
  `rw-*`, `mr-short-*`, `mrt-fourier-...`, `rowland-*`, `szechtman-lucas-...`,
  `lucas-submask-odd`, `gilbreath-verified-10^13` blocks are re-confirmed
  present **on disk in the summaries** (this pass) even where the derived
  `CLAIMS.md` renderer omits some of them — the derive gap is bookkeeping, not
  missing content.

## Sources that do not help (so nobody re-reads them)

- `allouche_shallit_kregular_II` / `allouche_shallit_kregular_sequences`:
  2-regular/2-kernel machinery, digested, relevant only as the automata
  background Rampersad–Wiebe sits on; not a weight bound.
- The five `citations_w*` files: citation-graph lookup tables, explicitly "not
  evidence"; their cited sources that bear are digested.
- `odlyzko_gilbreath`: bibliography index page, leads only.
- `granville_martin_prime_number_races` / `_prime_races`: two mirrors of one
  paper; single-residue race context, GRH-conditional, refuted approach.
- The four OEIS rows: base-4 / fractal ternary sequences; unrelated to the fold.
- `ashikhmin_barg_litsyn_polynomial_method`, `friedlander_macwilliams_krawtchouk`:
  metadata stubs; content already held by the MacWilliams/Krawtchouk tier.

## What the run still lacks (unchanged)

1. The **finite-prefix transfer** — ergodic Lucas-mixing randomization (Pivato–
   Yassawi Thm 7.1 at density-one times) ⇒ quantitative `wt(Φ_n h) ≥ c·n` for
   the one fixed prime string. In no source; both halves absent. Thread
   `finite-prefix-transfer` still open.
2. An **unconditional second-moment/submask-Walsh bound** `E[S(n)²]=O(n)` on the
   specific prime gap-parity string — request `walsh-spectral-subset-b904`,
   still open, the single surviving route to priority-2 (and, via Chebyshev, the
   density-1 priority-1 form).

## Durable memory stored this pass

1. The terminated run state: CONCLUSION.md closes the fold hypothesis as
   REFUTED (measured-not-proved); sixth closed door; only `E[S(n)²]=O(n)` on the
   prime string survives, unreachable by measurement (source: CONCLUSION.md).
2. `recall_memory` (Cognee) is unavailable this run; the on-disk ladders and
   `search_claims` are the reliable reference.

This pass adds no claim block because it establishes nothing new: it confirms
that the library is fully digested and the run is at its documented terminus.
