# Librarian audit — state after pass-3 close

**Cycle:** library audit after CONCLUSION-PASS3.md closed the pass's head
question (threshold weight tends to 0, sublinear ~n^0.557, workspace's first
affirmative weakening — problem.md type 4, not type 1).

## Verdict: NOTHING FURTHER (no new source this cycle)

The library is complete and topically mature for every live line; the search
freeze (directives 7/27/30) is recorded as still in force in the most recent
librarian reports (fourth pass, `summaries/librarian_report_fourth_pass.md`);
and the pass itself closed with "no new line is opened after this write-up."
No stated gap justifies a fetch — the one open request is a theorem to be
proven, not a paper to be obtained.

## What the audit confirmed

- **~78 files in `research/sources/`** (72 full texts, each with its source URL
  on line 1; three `DELETED_*` markers record genuinely unobtainable primaries,
  and `matomaki_radziwill_tao_fourier_uniformity_averaged` is the in-place
  pointer for the wrong first download). **~94 digests in `research/summaries/`**
  feed `research/CLAIMS.md`.
- **Top FRONTIER.md rows are all held.** The cited-by-3 rows (Hoi 2025 annotated
  bibliography, Prime Number Races / Granville–Martin) and the equal-residue /
  Maynard–Tao side (Maynard, BFTB "Consecutive primes in tuples",
  Freiberg, Shiu expository, Lau) are all on disk and digested. No ranking
  target is missing.
- **Fifth (counting from the fresh read this cycle) full pass over the frontier
  and the requests.** `REQUESTS.md` has exactly one open request,
  `walsh-spectral-subset-b904` — a Walsh/subset-sum lower bound on
  `wt(Φ_n x)` for submask-support inputs not "complicated" in any of the five
  refuted senses. It is a theorem to be found, not a source; nothing to
  download for it.
- **Search freeze governs.** Directive 7 gates any fetch behind naming an
  unworked FRONTIER candidate read and why none answers; directive 30's release
  condition (Ratio B decrement discrminator at N=160000, or an
  unaffordable-runtime note) is not met. ROOT.md records both. The one
  genuinely-new frontier candidate the citation pass surfaced — Maass,
  Martínez, Pivato, Yassawi 2006, *Attractiveness of the Haar measure for
  linear cellular automata on Markov subgroups* (IMS LNMS, doi
  10.1214/lnms/1196285812), the direct follow-up to Pivato–Yassawi's
  asymptotic-randomization-by-Phi theory — sits under the **dead** thread
  `finite-prefix-transfer` and is not worth a freeze violation.

## Why this is not a refill pass

Third-pass question (weight-threshold ratio → 0 vs plateau at 1/8) is
**answered** (CONCLUSION-PASS3.md): tends to 0, sublinear. Every piece of
theory that would explain the ratio is present (MacWilliams/Krawtchouk/
Delsarte, O'Donnell concentration, Yoshida fractal Pascal-weight, the
downset-meet geometry). The remaining open work is in-house computation and
the open pure-F2/hypergeometric lemmas (G-threshold-asymptotic-zero,
G-threshold-concentration) — self-provable, not missing sources.

## What the next cycle should do before anyone new is fetched

Name which unworked FRONTIER candidate it has read and why it does not answer
(directive 7), or satisfy the directive-30 release condition, or state a new
gap in REQUESTS.md with a falsifies column. Otherwise the freeze holds and the
library stands complete for the live line.

## Tooling note

`recall_memory`/`relate_memory` return 404 (Cognee: "No data found"); the
Cognee store is currently unavailable this cycle. Durable findings that would
normally go there are kept in this note and in the derived CLAIMS/ROOT files
instead. Do not treat a Cognee miss as evidence that a subject is unrecorded —
check `research/CLAIMS.md` and the per-note claim blocks.
