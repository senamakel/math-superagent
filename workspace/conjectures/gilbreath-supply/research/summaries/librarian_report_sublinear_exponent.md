# Librarian report — library state and the sublinear-exponent directive

## Scope of this pass

I was asked to build/complete a local reference library for SUPPLY. On
inspection the library is already **mature and complete**: 52+ full texts in
`research/sources/`, ~72 digests in `research/summaries/`, every source
indexed and `search_documents`-reachable, phase-1 complete per `research/ROOT.md`
(minimal-counterexample structure, verification bounds to n=40000/2^25, three
settled restricted classes). Five prior librarian passes verified coverage of
every live line of attack. The only open `research/REQUESTS.md` row
(`walsh-spectral-subset-b904`) is a **theorem to be found**, not a source to
download — no published result states a Walsh/subset-sum lower bound on
`wt(Φ_n x)` for non-"complicated" inputs. So there is nothing further to
download; further gathering against that gap would be a search with no
source, which the search freeze (directive 7, restated 27) correctly
prohibits.

## Steering directive applied (outranks the librarian task)

The steering directive asked me to (1) correct GOAL.md's "monotone decreasing"
phrasing for the `theta` column, (2) fit the sublinear exponent of the
threshold **weight** and test against the fold's constants, and (3) file a
claim block with n-range, status measured-not-proved, and post to the board.

- **(1) was already done on disk.** GOAL.md lines 40-43 already read
  "**eventually decreasing**, i.e. decreasing from n=14 onward" and note that
  the exact computation, not the prose, is the record (the table's 0.2500 at
  n=12 rises to 0.2857 at n=14). Nothing more to fix; the phrasing is already
  honest.
- **(2) verified and filed.** The threshold weights `theta*n =
  3,3,3,4,3,5,7,11,16,24,35,52,77` (n=8..4096) extend to `112,164,239`
  (n=8192,16384,32768) via the grouped-by-popcount Krawtchouk formula. My
  hand-verified per-doubling log2-slopes (0.567, 0.540, 0.550, 0.542,
  multiplier ~1.46/doubling) reproduce the quoted `~0.55` exponent and
  exclude both fold-produced constants: `1/2` (multiplier 1.414) and
  `log_4(3)=0.7925` (multiplier 1.732). **The exponent is fitted, not a
  closed form.**
- **(3) claim block filed**, id `threshold-weight-sublinear-n055`, status
  measured-not-proved, n-range 8..32768, in
  `research/notes/threshold_weight_sublinear_exponent.md`. Durable memory
  stored in Cognee. The board already carries a rising-sea lesson post with
  the ~n^0.57 substance and the "eventually decreasing" correction; board
  entries are asserted-not-established, so I filed the claim separately as
  the establishment of the verified part.

## The arithmetic demand, stated plainly

Reading **absolute weights** (not ratios): **linear supply is typical once
the switch count w exceeds about `const·n^0.55`.** A sublinear switch count
`w = o(n)` is strictly weaker than the mod-4 switch-density statement, which
demands a positive *fraction* `w ~ c·n`. That is the affirmative weakening
this workspace has chased for three passes. It is measured-not-proved exact
-mean evidence over n=8..32768, NOT a proof of the limit. And "typical is
not this string" — it says nothing about the primes' own h.

## Librarian finding: missing committed capture (action for a run with compute)

GOAL.md's quoted exponents (0.546±0.011 etc.) rest on the extended data, but
**no committed capture `code/out/threshold_exponent_fit.txt` exists on disk
and it is absent from `code/out/INDEX.md`.** Only the generating scripts are
present (`run_threshold_fit.py`, `fit_threshold_exponent.py`,
`extend_threshold_exponent.py`). The fit arithmetic is sound (I reproduced
~0.55 by hand from the on-disk, s_sos-cross-checked `w*` table), so this is a
housekeeping gap, not a wrong number — but the quoted exponent should get a
backing artifact so a later reader of GOAL.md can verify it rather than trust
the prose. Also noted: `code/out/linear_supply_threshold_pass3.txt` is 0
bytes (the sampled FRAC half) — a known failed run, flagged on the board by
adversarial, whose place is taken by the exact-mean half.

## What is now available locally

Unchanged from the mature library; this pass's contribution is the verified
exponent note + claim (`research/notes/threshold_weight_sublinear_exponent.md`)
and the durable memory. The library itself already holds every live line:
the parity barrier (ABGS 2011, Lau 2024, LOS 2016, Granville–Martin,
Rubinstein–Sarnak), the equal-residue side (Shiu-2000 via Ethan Yang
expository, Maynard, BFTB, Freiberg), the fold's own arithmetic (Lucas/
Meštrović, Pascal-mod-2/Hofer, Bacher, k-regular/Allouche–Shallit,
Rampersad–Wiebe, Steinhaus triangles), the Walsh/Krawtchouk/MacWilliams/
Delsarte coding tier, the ergodic/Rule-90 tier (Pivato–Yassawi, Takei), the
K>1 tier (Lacasa, Wu, Montgomery–Soundararajan), and direct prior work on
the exact object (Odlyzko 1993, Chase 2022).

## Report of what could not be obtained

No source states a Walsh/subset-sum weight bound on the fixed prime string
(request `walsh-spectral-subset-b904`) — that is a theorem gap, not a
downloadable source. The finite-prefix transfer (from the ergodic
randomization theorems to a single finite string) appears in no source and is
the run's own open step. Neither is downloadable; both are in `REQUESTS.md`
and `ROOT.md` as open.
