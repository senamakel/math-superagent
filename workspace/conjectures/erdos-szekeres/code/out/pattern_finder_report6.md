# Pattern-finder work: exploitable structure in the investigation's data

This round's task: look for exploitable structure in data the run has already
produced, extract integer sequences, run the exact sequence tools, and report
only regularities that hold exactly over every term, labelling them as
conjectures.

## What I did

1. Mapped every prior pattern-finder report (rounds 1–5) and the established
   template findings in CONTEXT.md / durable memory.
2. Computed a genuinely NEW exact statistic the run had not tabulated: the full
   **convex-subset spectrum** of the verified es_construct(n) — the count of
   convex k-subsets for every k=3..n-1 — using the exact lib/es_geom oracle
   (integer/Fraction determinants, never floating point).
3. Ran `analyze_sequence`, `find_linear_recurrence`, and `oeis_lookup` on the
   new rows and on the established template sequences.

## New exact data (this round), all oracle-exact

`code/out/convex_spectrum.py` (EXIT 0) + `convex_spectrum_n8_k4.py` (EXIT 0):

| n | N | k=3 | k=4 | k=5 | k=6 |
|---|---|---|---|---|---|
| 5 | 8 | 56 | 38 | — | — |
| 6 | 16 | 560 | 1119 | 802 | — |
| 7 | 32 | 4960 | 23220 | 49884 | 39648 |
| 8 | 64 | 41664 | 422186 | — | — |

Sanity: the k=3 row equals C(N,3) exactly (all 3-subsets of a general-position
set are convex), which independently confirms the oracle on these inputs. The
k=n-1 entry reproduces the established distinct-(n-1)-convex-subset counts
(38, 802, 39648).

## Sequence-tool verdicts (exact; conjectures, not proofs of continuation)

- **k=4 row [38, 1119, 23220, 422186]** (4 terms): not a low-degree polynomial
  (3rd differences never constant); growth ratios 29.45 → 20.75 → 18.18,
  decaying; **OEIS: no entry** — a real miss, recorded so nobody re-searches.
- **Total convex subsets [4, 94, 2481, 117712]** (4 terms): not low-degree
  polynomial; **OEIS miss** (recorded).
- **k=3 row = C(N,3)**: catalogued binomial, proved identity (trivial).
- The established rows (re-confirmed this round as already-known): gsplit valid
  splits [6,4,2,0] is the trivial arithmetic decay 12−2n; realized pattern
  classes [3,6,10,15,21] = C(n-1,2) = A000217; full transversals
  [2,9,96,2500,162000,26471025] = A001142(n-2); distinct-(n-1)-convex
  [4,38,802,39648] is an OEIS miss already recorded.

## The one structural conjecture worth stating exactly

The convex-k-subset spectrum of es_construct(n) appears **unimodal with its peak
at k = n−2** (one below the maximum convex size):
- n=6: 560, **1119**, 802 — peak at k=4 = n−2.
- n=7: 4960, **23220**, **49884**, 39648 — peak at k=5 = n−2.

**CONJECTURE (2 computed spectra — weak evidence, label as such):** for
es_construct(n) the convex k-subset count is maximised at k = n−2. First
falsifier: an n with the peak at k = n−1, or k ≤ n−3. This would need n=8's
full spectrum (C(64,k) for k=5,6 — ~7.6M and ~75M subsets, feasible but beyond
this run's budget) to test the 3rd data point.

Also (conjecture, 2–4 points): the convex-4 fraction
(convex 4-subsets / C(N,4)) = 0.543, 0.615, 0.646, 0.664 increases monotonically
and is bounded away from 1, while the k=n−1 counts grow super-exponentially —
so the spectrum's mass concentrates near the top, consistent with the
goodness/template picture. These are 2–4 point observations, not derived facts.

## Honesty / scope

Every number above was produced by a program this round ran and read (EXIT 0,
exact arithmetic), and every structural statement over the supplied terms is
labelled a **conjecture**. The unimodality and fraction-growth observations are
**descriptive of the es_construct template only** — exact numbers for one
extremal construction, not bounds on ES(n). The one new durable fact is the
4-term k=4 row and the *negative* finding that it is not polynomial and not in
OEIS: nobody should re-search it. Nothing here is presented as progress toward
the conjecture itself, and no enumeration exceeded its declared small bound.

Durable record (memory server was down all round — per steering fallback this is
written to the workspace and indexed):
`code/out/convex_spectrum_finding.md`, `code/out/convex_spectrum.py`,
`code/out/convex_spectrum.captured.txt`, `code/out/convex_spectrum_n8_k4.py`,
`code/out/convex_spectrum_n8_k4.captured.txt`.
