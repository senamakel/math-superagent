# Scholar pass — terminus verification: the "new material" is the run's own verdict, and the library is fully digested

Author: scholar. Scope: "the research agent just finished and the reference
library has new material" — read `research/` against GOAL (can the fold `Φ` do
work the switch-density form cannot see), against the task ledger, and current
beliefs, and record what the newest material establishes.

## The genuinely new material is not an external source

Cross-checked the on-disk state independently this pass (not on prior passes'
word): **50 full texts under `research/sources/` have 50 matching claim-bearing
digests under `research/summaries/`; `grep '^id:'` finds 51 claim blocks in 40
summary files.** No undigested claim-bearing source. Seven `citations_w*`
files are citation-graph lookup tables whose own headers say "a lead, not
evidence"; four OEIS rows, the two metadata stubs (`ashikhmin_barg_litsyn`,
`friedlander_macwilliams_krawtchouk`), the HAL page, and
`matomaki_radziwill_tao_averaged_chowla` (wrong-download quarantine) carry no
theorems. `DELETED_wrong_arxiv.md` is an overwrite note, not a source.

The genuinely new claim-bearing document since the run's last fully-verified
state is the run's own terminus deliverable, **`research/CONCLUSION.md`**
(directive 33/34). It is the *answer*, not a library item to digest.

## What CONCLUSION.md establishes (already filed, re-verified here)

1. **Refutation of the single hypothesis** (measured-not-proved): matched iid
   strings at the measured prime switch density `p ≈ 0.585` reproduce the
   primes' dip counts and last-dip positions essentially exactly (c=0.45
   last-dip ≤7000: primes 763 vs random 699–996; c=0.48: 5655 vs
   5595–6989). No measurable `ν₂` regularity is prime-specific; the primes sit
   in the generic-balanced-good class. Claim `goal-hypothesis-refuted-fold-adds-nothing-measurable`
   — **present in the rendered CLAIMS.md** (verified) and CONCLUSION.md.
2. **Sixth closed door**: no `ν₂` statistic is prime-specific. The atomic
   witness (deliverable 5): the LOS mod-4 switch preference is real and
   persistent (`corr(h_j,h_{j+1}) = −0.0555@40000 → −0.0416@256000`,
   `|corr|·√N` 3.4→21.1) yet **fold-inert**: `E[S(n)²]/(n−2) = 1.004` for the
   primes = the O(1) level of iid at the same p and of a same-(p,ac1) Markov.
   Claim `sixth-door-no-nu2-statistic-prime-specific` — **in CONCLUSION.md but
   NOT in the rendered CLAIMS.md** (grep finds no row).
3. **Single surviving open statement**: `E[S(n)²]=O(n)` on the specific prime
   gap-parity string (equiv. a submask-window Walsh/second-moment bound),
   unreachable by measurement and unproven. This is the terminal form of
   request `walsh-spectral-subset-b904`, which stays open.

## What this means for the goal/tasks/beliefs

The verdict confirms and completes the durable belief. No belief changes; the
terminus is the honest endpoint, and the closure is consistent with the proved
content (rank n−2, surjectivity, exact `Binomial(n−2,1/2)` for uniform h, the
g-run telescoping identity with its 438-mismatch control, the endpoint-sign
correction, `fold-distance-enumerator-On`). The three open items re-confirmed:
finite-prefix transfer; `walsh-spectral-subset-b904`; `s2_N → 0` (Ratio B
1.3155@40000, measured but unproved).

## Wiring state (verified by own grep, not prior passes' word)

- Closure claim `goal-hypothesis-refuted...` **is** in rendered CLAIMS.md.
- `sixth-door-no-nu2-statistic-prime-specific` is only in CONCLUSION.md; **not**
  in rendered CLAIMS.md — so the derive/renderer still misses it.
- **Neither terminus claim is mirrored in `research/ROOT.md`** (grep finds
  neither id); ROOT.md still reads as if the run were live (directive-30 head,
  averaged push "the only line in flight"). ROOT.md is not derived — it should
  have been hand-mirrored and was not.
- **The board has no terminus post**: the two work-products
  `teams/board_post_fold_genericity.md` and `teams/board_post_mod4_switch_bias.md`
  exist but were never posted to `teams/BOARD.md`/`board.jsonl` (grep of both
  finds no witness numbers 699/5655/763 or either terminus claim id). The other
  schools cannot see the closure on the board.
- The endpoint-parity spurious prefactor **was already corrected**:
  `research/backward/supply-from-endpoint-parity.md` line 113 now reads
  "corrected: no (−1)^{#runs(d)} prefactor" with the refuter citation — not a
  live defect.
- **`research/WEAKENED.md` still lists `R-random-pointwise` as open** with its
  Lucas-merit caveat — stale, since the rung is provably closed
  (surjectivity onto F₂^{n−2} ⇒ uniform image ⇒ `Binomial(n−2,1/2)` ⇒
  Chernoff). Re-attacking it wastes an attempt; attack should start at
  `R-submask-sufficiency`.

## Contradictions

- **Against recalled memory:** none. `recall_memory` (Cognee) still returns 404
  this run (environment fault, ~20 recorded failures against successful writes);
  the on-disk ladders, `search_claims`, and stored notes are the reliable
  reference. No source contradicts another beyond the two known self-resolved
  stale-id artefacts (`rw-not-the-submask-xor-fold` vs a misspelled
  `rw-described-as-the-fold-itself`; `r-finite-verified` id mismatch).
- The live "contradiction" is bookkeeping: WEAKENED.md and ROOT.md describe a
  mid-flight run while CONCLUSION.md records the terminus. That is a stale-
  context defect, not a factual dispute between two theorems.

## Sources that do not help (so nobody re-reads them)

All seven `citations_w*` (leads); the four OEIS rows; `odlyzko_gilbreath`
(bibliography); the Granville–Martin duplicate mirror; the quarantined
`matomaki_radziwill_tao_averaged_chowla`; the two metadata stubs and the HAL
page. Nothing new is claim-bearing beyond CONCLUSION.md.

## Durable findings stored

The terminus verdict, the sixth door, the single surviving open statement, the
wiring gaps (sixth-door claim and both terminus claims absent from ROOT.md;
sixth-door absent from rendered CLAIMS.md; no board post; WEAKENED.md stale on
R-random-pointwise), and the note that Cognee recall is unavailable and on-disk
state is reliable.

## What the run still lacks (unchanged, from CONCLUSION §5 and ROOT gaps)

The finite-prefix transfer; the unconditional second-moment/submask-Walsh bound
`E[S(n)²]=O(n)` on the prime string (request `walsh-spectral-subset-b904`); and
`proof` of `s2_N → 0`. All three are theorem gaps, not library gaps.

```claim
id: terminus-wiring-sixth-door-absent-live-recorded-not-executed
statement: >
  Independent grep audit of the terminus wiring: the external reference library
  is fully digested (50 full texts have 50 matching claim-bearing digests; 51
  claim blocks on disk; the derive gap means a dozen newer blocks are absent
  from the rendered CLAIMS.md but reachable via search_claims). The genuinely
  new claim-bearing matter is the run's own research/CONCLUSION.md — the single
  GOAL hypothesis (does Phi do work the switch-density form cannot see) is
  REFUTED (measured-not-proved: matched iid at p~0.585 reproduce dip counts and
  last-dip positions, c=0.45 last-dip<=7000 primes 763 vs random 699-996,
  c=0.48 5655 vs 5595-6989); sixth closed door (no nu2 statistic is
  prime-specific; the LOS mod-4 switch preference is fold-inert, E[S^2]/(n-2)=1.004);
  single surviving open statement E[S(n)^2]=O(n) on the prime gap-parity string
  (request walsh-spectral-subset-b904, unreachable by measurement). WIRING
  DEFECTS verified: closure claim goal-hypothesis-refuted-fold-adds-nothing-
  measurable IS in rendered CLAIMS.md, but sixth-door-no-nu2-statistic-prime-
  specific is NOT in rendered CLAIMS.md and NEITHER terminus claim is mirrored
  in research/ROOT.md (grep finds neither id); the board has NO terminus post
  (the two board_post_*.md files exist but were never posted to teams/BOARD.md
  or board.jsonl); research/WEAKENED.md still lists R-random-pointwise as open
  though it is provably closed by surjectivity=>Binomial(n-2,1/2)=>Chernoff.
  The endpoint-parity spurious (-1)^{#runs(d)} prefactor WAS already corrected
  (line 113 of supply-from-endpoint-parity.md).
hypotheses: the files as they sit on disk this pass, checked by grep.
holds-here: yes
status: checked (own grep audit this pass)
bearing: >
  Nobody should re-fetch library material expecting a way past the parity
  barrier — the library is mature and the terminus verdict is recorded. The
  actionable items are bookkeeping: mirror the two terminus claims into
  ROOT.md, post the terminus to the board, and stop treating R-random-pointwise
  as open (attack R-submask-sufficiency). CONTEXT.md/ROOT.md/WEAKENED.md describe
  a mid-flight run and should be updated to the terminus.
anchor: research/notes/scholar_pass_terminus_verification_new.md;
  research/CONCLUSION.md; research/ROOT.md (grep: no mirror);
  teams/BOARD.md + board.jsonl (grep: no post);
  code/out/pattern_finder_deliverable_5_mod4_switch_bias.md
contradicts: none
answers: does not answer walsh-spectral-subset-b904 — the gap is open and
  recorded so nobody re-fetches expecting closure.
```
