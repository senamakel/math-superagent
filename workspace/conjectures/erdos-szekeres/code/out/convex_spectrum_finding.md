# Pattern-finder round: convex-subset spectrum of es_construct

## New exact data (this round): full convex-subset spectrum

For the **verified** es_construct(n) (N = 2^{n-2} points, largest convex subset
= n-1, no convex n-gon), exact convex k-subset counts, exact `lib/es_geom`
oracle (integer/Fraction determinants), `code/out/convex_spectrum.py` EXIT 0
and `code/out/convex_spectrum_n8_k4.py` EXIT 0:

| n | N | k=3 | k=4 | k=5 | k=6 |
|---|---|---|---|---|---|
| 5 | 8 | 56 | 38 | — | — |
| 6 | 16 | 560 | 1119 | 802 | — |
| 7 | 32 | 4960 | 23220 | 49884 | 39648 |
| 8 | 64 | 41664 | 422186 | — | — |

Sanity: k=3 row = C(N,3) exactly (56, 560, 4960, 41664) — all 3-subsets of a
general-position set are convex, confirming the oracle. The k=n-1 entry matches
the established distinct-(n-1)-convex-subset counts (38, 802, 39648).

## Sequence-tool verdicts (exact over supplied terms; conjectures only)

- **k=4 row [38, 1119, 23220, 422186]**: not a low-degree polynomial (3rd diffs
  not constant); growth ratios 29.45/20.75/18.18; **OEIS hit: none** (a miss —
  recorded so nobody re-searches). The ratio is decaying toward ~1, so it is
  substantially below the fully-convex ceiling C(N,4).
- **k=3 row = C(N,3)**: catalogued binomial, proved identity (trivial).
- Totals (k>=3): [94, 2481, 117712] — no low-degree polynomial, ratios
  26.4/47.4, no OEIS (need 4 terms; not computed).

## Structural observations (conjectures)

1. **Unimodality.** The spectrum rises then falls, peaking at:
   n=6: 560, **1119**, 802 (peak k=4 = n-2)
   n=7: 4960, **23220**, **49884**, 39648 (peak k=5 = n-2)
   So the peak is at **k = n-2** (one below the maximum convex size), in both
   computed spectra. CONJECTURE (2 points, weak): the convex k-subset count of
   es_construct(n) is unimodal with peak at largest convex size minus 1 = n-2.
2. **k=4 convex fraction** (convex 4-subsets / C(N,4)): n5 0.543, n6 0.615,
   n7 0.646, n8 0.664 — monotonically increasing, bounded away from 1.
3. The k=4 row near 0.66·C(N,4) while k=n-1 counts grow super-exponentially
   (38, 802, 39648 ≈ ratios 21, 49) shows the mass concentrates near the top of
   the spectrum — most convex subsets are almost-maximal. Consistent with the
   goodness/template picture.

## Bearing and honesty

These are **descriptive of the es_construct template only** — exact numbers for
one extremal construction, not bounds on ES(n). The unimodality and fraction
growth are 2–4 point observations labelled conjecture, not derived facts. The
new 4-term k=4 row is a genuine OEIS miss (recorded). It does not yield a closed
form for convex-4 counts of the extremal template.

Files: code/out/convex_spectrum.py, code/out/convex_spectrum.captured.txt,
code/out/convex_spectrum_n8_k4.py, code/out/convex_spectrum_n8_k4.captured.txt.
