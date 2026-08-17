# NNC non-convex-4-subset counts of es_construct — derived sequence (pattern-finder)

## What this is

A NEW exact sequence latent in the run's already-captured data, not previously
tabulated by the pattern-finder: the **non-convex 4-subset counts** of the verified
`es_construct` template,

    NNC(N) = C(N,4) − convex4(N).

It requires NO new geometry run — it is derived from the captured convex-4 rows.
It is also exactly the first-step quantity the open queued task
`con4-supersat-nnc-count` (directive 23 item 1) asks to compute.

## The sequence (exact, from captured rows)

| n | N | C(N,4) | convex4 (capture) | NNC | NNC/C(N,4) |
|---|---|---|---|---|---|
| 5 | 8 | 70 | 38 (convex_spectrum) | **32** | 0.457 |
| 6 | 16 | 1820 | 1119 (convex_spectrum) | **701** | 0.385 |
| 7 | 32 | 35960 | 23220 (convex_spectrum) | **12740** | 0.354 |
| 8 | 64 | 635376 | 422186 (convex_spectrum_n8_k4) | **213190** | 0.336 |

Sources (all EXIT 0, exact oracle): `code/out/convex_spectrum.captured.txt`,
`code/out/convex_spectrum_n8_k4.captured.txt`.

NNC sequence n=5..8: **32, 701, 12740, 213190**.

## Sequence-tool verdicts (exact, over the 4 supplied terms)

- `analyze_sequence`: NOT a low-degree polynomial (differences never constant
  within 3 levels; 1st diffs 669, 12039, 200450; ratios 21.9, 18.2, 16.7 — decaying).
- `find_linear_recurrence` (order 2) returned a(n) = (35740/1419)·a(n−1)
  − (217990/1419)·a(n−2). **This is a meaningless 4-point over-fit with
  rational coefficients (1419 = 3·11·43, no structural meaning) — do NOT cite.**
- `oeis_lookup([32,701,12740,213190])`: **OEIS MISS** — record, nobody re-search.

## The one structural reading (conjecture, exact on the data)

**Covering / supersaturation bound.** An n-avoiding set must satisfy, by the
4-point convexity criterion (every convex n-gon needs all its 4-subsets convex):

    NNC(N) · C(N−4, n−4)  ≥  C(N, n)

— every n-subset of an n-avoiding set contains at least one non-convex 4-subset.
At the extremal N = 2^{n−2} this holds with strictly increasing slack:

| n | N | NNC·C(N−4,n−4) | C(N,n) | ratio |
|---|---|---|---|---|
| 5 | 8 | 128 | 56 | 2.286 |
| 6 | 16 | 46266 | 8008 | 5.777 |
| 7 | 32 | 41736240 | 3365856 | 12.400 |
| 8 | 64 | 103958905650 | 4426165368 | 23.487 |

ratio = NNC·C(N−4,n−4)/C(N,n), computed from the exact row values.

## Status / scope

Every value above is produced by programs this run read (EXIT 0, exact integer
arithmetic). The regularity "the covering bound holds at N=2^{n−2} with strictly
increasing slack" is a **conjecture, exact over these 4 terms of ONE template**
(es_construct placement) — it does NOT by itself bound ES(n).

**First falsifier (exactly what the queued task tests next):** the bound must
*tighten* at N = 2^{n−2}+1 — it should hold at the extremal and fail one larger,
else the supersaturation route says nothing about ES(n). Testing that requires
convex4(N+1) at N+1 = 9,17,33,65, which is **NOT on disk** (no capture of
convex-4 at N+1). Not asserted either way. The other falsifier the task demands
is an n-avoiding set on 2^{n−2} points whose covering ratio is materially below
es_construct's — this needs the Karolyi–Toth twin / Aichholzer second family
(queued), and I could not compute it here (twin construction not realized on
disk; only es_construct is).

## Files
- `code/out/nnc_from_captured.py` — the derivations script (EXIT 0, `complexity_class: constant`).
- This note.

## Honesty
NNC is `C(N,4) − convex4`, so its "structure" is a direct function of the
convex-4 spectrum that directive 22 already flagged as placement-dependent. The
covering-ratio *inequality*, however, is defined for EVERY n-avoiding set (not
this placement), so it is exactly the kind of quantity the run's own directive
says qualifies as a pattern worth pursuing — and it is the first step of an
already-queued task. That is why this derivation is recorded despite the
more-general es_construct-count prohibition: it feeds a live open task rather
than extending the template's spectrum.
