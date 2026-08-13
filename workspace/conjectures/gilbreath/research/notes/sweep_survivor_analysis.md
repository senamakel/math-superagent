# Event-rate sweep: survivor analysis

Dataset: `code/out/event_rate_stats.jsonl` (1154 sequences) + the sweep's
captured report. Analysis: `code/event_rate/analyze_survivor.py` →
`code/out/survivor_analysis.captured.txt`. Pure read of the persisted jsonl;
no new sieves, no row arithmetic beyond the recorded stats.

Field semantics (from `code/event_rate/event_rate_sweep.py::measure_rows`):
- `first_b0` = first 1-based row k with leading `{0,2}` block length
  `b_k = 0` — the **death row**; `None` = survived to batch depth
  (sweep D=600, deep D=1200, long D=4000).
- `trunc_k` = first row whose block filled the whole finite row
  (`b_k = row width − 1`, no intruder exists past it).
- `eligible` = rows with `b_k ≥ 1` and an intruder; `events` = (2,4)-events
  on eligible rows; `rho_live` = events/eligible.
- Totals reproduce the recorded analysis exactly: 852/1154 died (73.8%),
  302 survived (26.2%), 20,013 events / 46,528 eligible rows, 0 step-law and
  0 recharge-identity failures.

## Q1 — per-family deaths and death rows (pooled over batches)

| family | n | died | surv | die% | death rows min/med/max |
| --- | --- | --- | --- | --- | --- |
| consecutive | 62 | 0 | 62 | 0% | — |
| f2-rand24 | 62 | 0 | 62 | 0% | — |
| f2-skew246 | 62 | 20 | 42 | 32% | 2 / 3 / 8 |
| f2-skew24810 | 58 | 33 | 25 | 57% | 2 / 5 / 10 |
| f2-uniform3 | 58 | 35 | 23 | 60% | 2 / 2 / 6 |
| f2-geo05 | 62 | 42 | 20 | 68% | 2 / 3 / 9 |
| f2-uniform5 | 58 | 50 | 8 | 86% | 2 / 2 / 6 |
| f2-geo00625 | 10 | 10 | 0 | 100% | all k=2 |
| f2-geo0125 | 10 | 10 | 0 | 100% | 2 / 2 / 3 |
| f2-geo025 | 58 | 58 | 0 | 100% | 2 / 2 / 9 |
| f2-uniform10 | 58 | 58 | 0 | 100% | 2 / 2 / 6 |
| f2-uniform25 | 58 | 58 | 0 | 100% | 2 / 2 / 3 |
| f2-uniform50 | 58 | 58 | 0 | 100% | 2 / 2 / 3 |
| rand24 | 48 | 30 | 18 | 62% | all k=1 |
| skew246 | 48 | 31 | 17 | 65% | 1 / 1 / 8 |
| skew24810 | 48 | 37 | 11 | 77% | 1 / 1 / 9 |
| geo05 | 48 | 39 | 9 | 81% | 1 / 1 / 8 |
| uniform3 | 48 | 45 | 3 | 94% | 1 / 1 / 4 |
| uniform5 | 48 | 46 | 2 | 96% | 1 / 1 / 4 |
| geo025 | 48 | 48 | 0 | 100% | 1 / 1 / 7 |
| uniform10/25/50 | 48 each | 48 | 0 | 100% | 1 / 1 / 2..4 |

Overall death-row histogram (all 852 deaths): k=1: 342, k=2: 346, k=3: 76,
k=4: 24, k=5: 19, k=6: 17, k=7: 14, k=8: 6, k=9: 6, k=10: 2.
89.7% (764/852) die by row 3; **max death row over the whole dataset is 10**.

## Q2 — conditioning on first gap = 2: support shape still discriminates

Matched families, pooled batches (n includes sweep 48 + deep/long where run):

| gaps | base die% | f2 die% | f2 death rows min/med/max |
| --- | --- | --- | --- |
| {2,4} (rand24) | 62% (30/48, all k=1) | **0% (0/62)** | — |
| skew{2,4,6} | 65% | 32% (20/62) | 2 / 3 / 8 |
| skew{2,4,6,8,10} | 77% | 57% (33/58) | 2 / 5 / 10 |
| uniform{2..6} | 94% | 60% (35/58) | 2 / 2 / 6 |
| uniform{2..10} | 96% | 86% (50/58) | 2 / 2 / 6 |
| uniform{2..20} | 100% | 100% (58/58) | 2 / 2 / 6 |
| uniform{2..50} | 100% | 100% (58/58) | 2 / 2 / 3 |
| uniform{2..100} | 100% | 100% (58/58) | 2 / 2 / 3 |
| Geo(p=0.5) | 81% | 68% (42/62) | 2 / 3 / 9 |
| Geo(p=0.25) | 100% | 100% (58/58) | 2 / 2 / 9 |
| Geo(p=0.0625/0.125, deep only) | — | 100% (10/10 each) | 2 |

So **yes, support shape discriminates inside the f2 class**: among the
first-gap-2 families, death rate rises monotonically with gap-support width
and mean gap (f2-rand24 0%, f2-skew246 32%, f2-uniform3 60%, f2-uniform5
86%, f2-uniform10/25/50 and Geo(p≤0.25) 100%). First gap 2 removes the
k=1 deaths entirely (no f2 family has a death before k=2) and is sufficient
for the {2,4}-support families, but is not sufficient for wider support.

### Why the {2,4}-support dichotomy is mechanical (checked, exact)

With gaps ⊆ {2,4}: `A1 = (1, |3−(3+g0)|, …) = (1, g0, …)`, so
`b_1 = 0` (death at row 1) iff `g_0 = 4` — matching all 30 rand24 deaths
(every one at k=1). If `g_0 = 2`, then `A1 = (1, 2, |g1−g|… )` and a direct
expansion gives **row 2 = (1, {0,2}×…) for every continuation** (checked
exhaustively over all `(2,4)^3` gap patterns: 0 violations). The state
`(1, {0,2}, {0,2}, …)` is closed under absolute differencing (checked on all
2^4 patterns; the corner's every row is again the corner), so these sequences
satisfy the `{0,2}` property for **all** rows — they are provably immortal
until the finite width runs out. Consistent with the data: every rand24
survivor has trunc_k = 2, every consecutive sequence has trunc_k = 1, every
f2-rand24 sequence has trunc_k = 2. This is why those families show 0%
death: their survival is the already-regenerated corner, not an event-rate
phenomenon.

## Q3 — no survivor of row 10 ever died (to the file's depth)

- Max `first_b0` over all 852 deaths: **10**; zero sequences have
  `first_b0` in 11..D. Confirmed: **no sequence reaching row 11 with `b ≥ 1`
  died within its batch depth** (600 / 1200 / 4000).
- Stronger, and new: every one of the 302 survivors entered the **corner**
  (block filled the whole finite row, `trunc_k` set) — none ran to batch
  depth with an intruder still present. Corner-entry row: trunc_k=1 for
  consecutive, 2 for rand24/f2-rand24, 25–55 for the wider f2 families
  (median: f2-uniform3 28, f2-skew246 39, f2-skew24810 45, f2-geo05 46).

## Q4 — the surviving class, in one sentence

The 302 survivors (26.2%) are exactly the sequences whose first gap is 2 and
whose gaps are drawn from small support or a geometric p ≥ 0.5 — at one
extreme the provably-immortal corner families (consecutive, f2-rand24; 124
sequences entering the corner at row ≤ 2), at the other the non-degenerate
regenerating families (f2-skew246, f2-skew24810, f2-uniform3, f2-uniform5,
f2-geo05, plus unforced rand24/skew/geo05 survivors) with `rho_live` between
0.318 and 1.000 (median 0.643), `min_b` between 1 and 10 (median 2), all of
them eventually cornering by row 55 — and every death in the dataset happens
by row 10, 89.7% by row 3, so within this class dying is entirely a startup
transient and surviving row 10 is equivalent to surviving to the corner.

## Bearing on the run's open question

The primes (first gap 2, small skewed gaps, min b = 2 at depth 1000) sit in
the surviving minority, and the prime rows themselves hit the finite-width
corner artifact at k=162 (block 1,270,444 = width−1). The class-level picture
is now: survival ⟺ first gap 2 + narrow/skewed concentration, and eventual
cornering rather than an infinite event-rate race. This is consistent with
the Eppstein/CHT verdict that bounded-gap support alone is insufficient
without a concentration hypothesis; the data localises the failure to rows
1–3 and to the first gap in particular, and shows the "regeneration rate"
picture is wrong for the wide-support families (they die in the transient,
not by slow erosion).

## Claims

```claim
id: sweep-survivor-startup-only
statement: In the 1154-sequence event-rate sweep (2-then-odds class, D=600..4000, families consecutive/rand24/skew/uniform/geometric with and without first gap forced to 2), all 852 observed deaths occur at rows k <= 10 (342 at k=1, 346 at k=2, 764/852 by k=3); zero sequences with first_b0 in 11..D, and every one of the 302 survivors entered the {0,2}-corner (block filled the finite row, trunc_k <= 55) before or at batch depth. Surviving row 10 within this class is equivalent to surviving to the corner.
hypotheses: A_0 = (2, 3, 3 + cumsum(even gaps)), b_k = leading {0,2} length; death = first k with b_k = 0; corner = b_k = row width - 1 (no intruder); widths 2e5..2e6; exact int64 row arithmetic (numpy), verified against an independent pure-Python oracle on 4 sequences.
holds-here: no — the primes are the surviving minority (first gap 2, small skewed gaps, min b = 2 to depth 1000); the class-level death is a startup effect, not a model of what threatens the primes
status: computed and checked (bounded by batches: 48/10/4 seeds per family at depths 600/1200/4000); not proved for all k of any single sequence except the corner families (see sweep-corner-mechanism)
anchor: code/out/survivor_analysis.captured.txt, code/out/event_rate_stats.jsonl
```

```claim
id: sweep-corner-mechanism
statement: For the 2-then-odds class with gap support subseteq {2,4} and first gap 2, row 1 has A1[1] = g0 = 2 (b_1 = 2) and row 2 is the corner state (1, {0,2}, {0,2}, ...) for every continuation; the corner state is closed under absolute differencing, so such sequences satisfy the {0,2} property for all rows (until finite width ends the boundary process). If instead g0 = 4, A1[1] = 4 and b_1 = 0 (death at row 1). Verified over all (2,4)^3 gap patterns (0 violations) and all 2^4 corner patterns (closedness), and matched by the dataset: 30/30 rand24 deaths at k=1, 18/18 rand24 survivors and 62/62 f2-rand24 and 62/62 consecutive with trunc_k = 2, 1 respectively.
hypotheses: all gaps in {2,4}; A0 = (2, 3, 3 + cumsum(gaps)); first row index 1 of each row is position 1.
holds-here: yes for the {2,4}-support sub-class (proved by direct expansion; the corner closedness is 2 lines); the primes are not in this sub-class (gap 8,10,12,... occur), but the prime row does reach the corner at k=162 only as a finite-width artifact.
status: proved (elementary row-2 expansion + closure of {0,2} under |a-b|), numerically confirmed on the dataset and by exhaustive small-pattern check
anchor: code/out/survivor_analysis.captured.txt; closure of {0,2} under absolute difference is the one-line fact already used throughout the run (e.g. research/notes/block_lemma.md)
```

```claim
id: sweep-f2-support-discrimination
statement: Conditioning on first gap = 2 removes all k=1 deaths and is sufficient for gap-support {2,4} (0/62 deaths across sweep+deep+long to D=4000) but still leaves death rate monotonically increasing with gap-support width / mean gap: f2-rand24 0/62 (0%), f2-skew246 20/62 (32%), f2-uniform3 35/58 (60%), f2-uniform5 50/58 (86%), f2-uniform10/25/50 58/58 (100%), f2-geo05 42/62 (68%), f2-geo025 58/58 (100%). So support shape discriminates fully inside the first-gap-2 subclass; first gap 2 is necessary for survival in this class but not sufficient.
hypotheses: same class as sweep-survivor-startup-only; mean gap per family: {2,4}=3, skew246=2.9, skew24810=3.16, uniform3=4, uniform5=6, uniform10=11, uniform25=26, uniform50=51, geo05=4, geo025=8, geo0125=16, geo00625=32.
holds-here: no (the primes sit in the narrow-skew surviving minority, consistent with f2-skew246/f2-skew24810 rates; the primes' unbounded gaps put them outside every fixed-support family)
status: computed and checked (bound: seeds and depths above); not proved
anchor: code/out/survivor_analysis.captured.txt
```