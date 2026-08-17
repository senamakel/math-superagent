# Pattern-finder report (round 3): adjudication of transversal-convexity + sequence record

Follow-up to `pattern_finder_report.md` / `pattern_finder_report2.md`. This round's
work was driven by the steering directive (13): adjudicate the transversal-convexity
finding against the literature, and do the housekeeping (close the two refuted
allowable-sequence tasks, stop the library round). Both are done; the substantive
deliverable is the mechanical confirmation of the adjudication.

## 1. Transversal-convexity: adjudicated (a) structural consequence, mechanically confirmed

The claim `es-construct-transversal-convexity` (every full transversal of the
verified es_construct X_n, one point per block, is convex — exact through n=9) was
already recorded as **structural consequence, verified**, NOT a discovery, and as an
instance of the positive-fraction ES phenomenon (`barany-valtr-positive-fraction`).
The directive asked me to decide (a) vs (b) and give the construction step that does
or does not imply it. Two exact experiments now confirm (a) mechanically:

**(E1) Margin analysis** (`transversal_adjudicate_margin.py`). On the construction's
convex arc (centers x-spacing 1000, strictly decreasing successive slopes, drop 0.1),
the arc's convexity corridor (slope-drop × spacing = 100) exceeds the largest cluster
diameter (~2.3e-5 at n=7, ~9.7e-5 at n=9) by **>8 orders of magnitude**. A
one-point-per-block transversal is a tiny perturbation of a strictly convex (n-1)-gon
in block order (Conjecture A), so convexity is forced by the margin.

**(E2) Placement-breaking control** (`transversal_breaking.py`, n=6, exact). Keep the
IDENTICAL blocks; replace the convex-arc centers with (i) scrambled y on the arc x's,
(ii) random y. Both destroy BOTH transversal-convexity (96/96 non-convex) and
n-avoidance (a convex 6-gon appears). The convex arc reproduces the original
transversal-convex / n-avoiding behavior.

So transversal-convexity is an artifact of the arc *placement*, not an intrinsic
property of the block decomposition — it does not characterize n-avoiding sets in
general. The one open question with value (does transversal-convexity of a block
decomposition force n-avoidance) is not settled by this control: the two properties
fail together off the arc, consistent with but not proving characterization.

These experiments are recorded in the claim note
(`code/out/transversal_convexity_claim.md`) and in durable memory.

## 2. Sequences the sequence tools establish exactly (over the given terms)

Run on the run's computed integers, with everything labelled as conjecture / structure:

| Sequence | Terms | Tool verdict | Status |
|---|---|---|---|
| gsplit valid splits (n=4..7) | 6,4,2,0 | constant diff −2 ⇒ degree-1 polynomial (arithmetic decay), period 1 mod 2 | trivial 12−2n, NOT catalogued; scoped to the template, matching n7-zero |
| distinct (n-1)-convex subsets | 4,38,802,39648 | no low-degree polynomial; growth ratios 9.5, 21.1, 49.4 ⇒ super-exponential; no linear recurrence; OEIS no match | no exploitable structure (already recorded as dead thread) |
| ES(n) conjecture | 3,5,9,17,33,65,129,257 | a(n)=3a(n-1)−2a(n-2), closed form 2^{n-2}+1 = A000051 | conjectured threshold (values proved only n≤6) |
| cups/caps threshold f(k,k) | 2,3,7,21,71,253,925,3433 | A323230, C(2k-4,k-2)+1 | proved (ES35) |
| full transversals (block-size product) | 2,9,96,2500,162000,26471025 | A001142(n-2) = prod C(n-2,i) | proved identity |
| whole-set cap / cup of X_n | cap 2, cup n−1 (n=4..11 exact) | cap constant 2; cup = n−1 | verified n=4..11 via validated es_geom oracle |

All exact arithmetic against the validated `lib/es_geom` oracle. None of the fits is a
proof of continuation; the ES(n)=2^{n-2}+1 recurrence is itself the conjecture being
attacked, so it must not be cited as support.

## 3. Housekeeping (per directive 13)

- `allseq-adjudicate` and `allowable-sequence-continue`: both already **dropped** in
  the tasks ledger with full adjudication reasons (reversal-depth=block-index is a
  structural impossibility; contiguous-block convexity false both directions). Nothing
  to re-run; the run must stop being told to redo refuted work.
- Library round stopped: I gathered nothing new (no source fetch, no search), per the
  directive to gather only against a stated gap in REQUESTS.md.

## 4. Recommendation

The transversal-convexity line is now correctly scoped as a property of the template.
The only part with potential value is the characterization question (does
transversal-convexity of a block decomposition force n-avoidance). My control shows
the two fail together off the arc, which is suggestive but not a proof; testing whether
some *non-arc* placement of the same blocks keeps transversal-convexity while admitting
a convex n-gon would be the next falsifier to hunt — but that belongs to the extremal-
structure thread, and only if it survives a cost check. No new catalogued sequence was
found; the distinct-(n-1)-convex-subset and gsplit counts carry no exploitable
regularity.
