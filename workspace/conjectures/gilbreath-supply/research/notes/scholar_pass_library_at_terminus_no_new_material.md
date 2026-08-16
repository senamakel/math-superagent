# Scholar pass — final library reconciliation: no undigested claim-bearing source

Author: scholar. Scope: "the research agent just finished and the reference
library has new material" — read `research/` against GOAL, the task ledger, and
the current beliefs, and record what the newest material establishes.

## Headline finding

**There is no new claim-bearing source to digest.** Every full text under
`research/sources/` has a matching, claim-bearing digest under
`research/summaries/`. Cross-checking the two listings this pass:

- 50 full texts ↔ 50 substantive digests (40 carry `^id:` claim blocks; the
  claim-bearing ones verified at 51 blocks across those 40 files).
- The summary files without `^id:` blocks are exactly the categories already
  flagged do-not-re-read: seven `citations_w*` lead-only citation-graph files,
  four OEIS rows, the `librarian_*` and `scholar_*` reports, the
  `mauduit_rivat_gelfond_hal_page` metadata stub, and the
  `ashikhmin_barg_litsyn` / `friedlander_macwilliams_krawtchouk` metadata stubs.
- `sources/DELETED_wrong_arxiv.md` is an **overwrite note**, not a source: it
  documents that two guessed arXiv IDs (Maynard `1405.2594`→`1405.2593`,
  BFTB `1303.3348`→`1311.7003`) first fetched the wrong papers and were
  corrected in place. The wrong content never entered the claim ledger.

So the "new material since the research agent finished" is **not a source**. It
is the run's own terminus deliverable, `research/CONCLUSION.md` (directive 33).
That is the only genuinely new, claim-bearing document, and it is the run's
answer, not something to digest.

## What CONCLUSION.md establishes (the newest material)

Re-read and confirmed against ROOT.md/CLAIMS.md this pass — it is already
filed with claim blocks (`goal-hypothesis-refuted-fold-adds-nothing-measurable`,
`sixth-door-no-nu2-statistic-prime-specific`, both present in the rendered
CLAIMS.md):

1. **Verdict: the single hypothesis is REFUTED** (measured-not-proved). Whether
   Phi does work the switch-density form cannot see is answered NO: matched iid
   strings at the measured prime switch density p≈0.585 reproduce the primes'
   dip counts and last-dip positions essentially exactly (c=0.45: primes 763 vs
   random 699–996; c=0.48: primes 5655 vs random 5595–6989). No measurable
   nu2 regularity is prime-specific.
2. **Sixth closed door added**: no nu2 statistic is prime-specific; the primes
   sit in the generic-balanced-good class.
3. **What survives**: exactly one unconditional arithmetic statement,
   `E[S(n)²]=O(n)` (equiv. submask-window Walsh/second-moment bound) on the
   *specific* prime gap-parity string h[j]=((q_{j+1}−q_j)/2) mod 2 —
   unreachable by any measurement.
4. Proved facts re-agreed: rank n−2 / nullity 2 / ker=span(even-alt,odd-alt),
   surjectivity, wt exactly Binomial(n−2,1/2) for uniform h, the g-run
   telescoping identity (438-mismatch 3-valued control), endpoint-sign
   correction, fold-distance-enumerator F_n(z)=O(n).

## What this means for the run's goal/tasks/beliefs

Consistent with and completing the durable belief. The open request
`walsh-spectral-subset-b904` is retired (task `walsh-subset-sum-lower-bound`
dropped at terminus) and superseded by CONCLUSION §5. No belief changes; the
terminus is confirmed as the honest endpoint. The three open items re-confirmed:

1. **Finite-prefix transfer** — ergodic Lucas-mixing randomization ⇒
   quantitative `wt(Φ_n h) ≥ c·n` for the one fixed prime string; in no source;
   thread `finite-prefix-transfer` open.
2. **`E[S(n)²]=O(n)` for the prime string** — the single surviving route to
   SUPPLY (density-1 via Chebyshev); an unconditional theorem this run's
   measurements cannot reach.
3. The Decrement-ratio `/ N=160000` discriminator task was dropped at terminus;
   no computation is needed to find a new route — CONCLUSION closes the fold
   hypothesis.

## Sources that do not help (so nobody re-reads them)

- The seven `citations_w*` files: lead-only citation-graph tables, not evidence.
- The four OEIS rows, `mauduit_rivat_gelfond_hal_page`, the two
  Krawtchouk/MacWilliams metadata stubs: no theorems beyond what the primary
  digests already hold.
- `DELETED_wrong_arxiv.md`: overwrite note, no content.

## Contradictions

None new, and none against recalled memory. The two CLAIMS.md "contradictions"
rows (`rw-not-the-submask-xor-fold` vs a misspelled non-existent
`rw-described-as-the-fold-itself`; `r-finite-verified` id mismatch) remain the
self-resolved bookkeeping artefacts prior passes recorded. Note that
`recall_memory` (Cognee) has failed 17+ times this run, so this pass relied on
the on-disk ladders, ROOT.md, CONCLUSION.md, and `search_claims` — all of which
are consistent.

## Durable finding stored

The terminus state, its refutation verdict, the single surviving open statement,
and the note that Cognee recall is unavailable and the on-disk record is
reliable, are stored with `remember_memory`.

## What the run still lacks (unchanged, from CONCLUSION §5 and ROOT gaps)

The finite-prefix transfer and the unconditional second-moment/submask-Walsh
bound on the prime string. Both are theorem gaps, not library gaps; neither any
download in FRONTIER.md answers them, and search is frozen at terminus.
