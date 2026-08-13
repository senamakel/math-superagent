# Pattern-finder findings: the 3e8 wider-width giant record (depth 300)

Extracted and verified this session. Inputs: `code/out/wider_width_b_clean.json`
(16,252,325 primes, sieve 3e8, first 300 rows, exact integers, step-law
verified 0 failures by the producing run); cross-checked against
`code/out/blocks_depth1000.json` (2e7 sieve) — **rows 1..161 identical
(0 mismatches)**, so both runs agree on the shared regime.

## 1. The 15 giants, correctly extracted (landing rows, 1-based)

Giant = regeneration event with jump j = b[r] − b[r−1] > 1000, transition
row r−1 → r:

```
pre-jump row (pair row) : 34   56   64   68   94   96  110  112  126  130  134  146  161  174  238
landing row             : 35   57   65   69   95   97  111  113  127  131  135  147  162  175  239
jump                    : 1314 1739 17326 8237 61088 11354 37746 129923 53470 190810 217657 360698 4323712 5237310 5596824
landing block           : 2179 5942 23265 31499 92620 103973 141706 271629 325090 515906 733564 1094273 5417975 10655286 16252084
```

- **14 of the 15 are genuine** (landing floorings ≥ 5,596,863). The one
  capped event is the last: row 238→239 lands at the finite right edge
  (flooring 1, intruder None; k* = 239), so its jump **≥ 5,596,824** is a
  lower bound and its gap arithmetic is excluded. (My earlier analysis
  including it produced a spurious max gap of 64 — an artifact; the correct
  live-regime max gap is **26**.)
- **The old depth-1000 "capped" giant i=161 is now RESOLVED**: at 3e8 its
  true jump is **4,323,712** with landing flooring 10,834,187 — completely
  genuine; the 2e7 "j ≥ 176,181" figure was a width underestimate.
- **The depth-1000 record max jump 360,698 (i=146) is superseded**: the
  wider run records genuine jumps 4,323,712 (i=161) and **5,237,310 (i=174)**;
  the largest *live* jump is 5,237,310 (i=174); only the row-238 jump is
  capped (≥ 5,596,824).

## 2. Inter-giant gaps — the "max gap 26" bound CORROBORATED

Genuine 14 pre-jump rows → 13 gaps: `22, 8, 4, 26, 2, 14, 2, 14, 4, 4, 12,
15, 13`; **max 26**, mean 10.54, median 12. The two new gaps (15, 13) sit
inside the existing range; the 15× width increase with blocks up to 4,900×
larger **did not grow the max gap**. Corroborates
`directive25-gap-trend-and-reconciliation` (status: checked, gap half
strengthened). Note directive25's "13th ratio 4.95 reverses the declining
ratio trend" is unchanged; the 14th ratio 1.967 keeps the geometric
description alive.

## 3. Parity regularity: giants fire at even pre-jump rows — 14/15

14 of 15 giant (2,4)-events have **even pre-jump row**; the sole exception
is **i=161** — which is genuine at 3e8 (jump 4,323,712), so this is a
numerical regularity with one real exception, **not** a width artifact
(that was my first hypothesis and is wrong).

Significance (exact hypergeometric, giant draw vs the event base rate):

| dataset | events (even frac) | giants even | hypergeom P |
| --- | --- | --- | --- |
| 2e7 rows 1..161 | 43 (0.698) | 12/13 | 0.034 |
| 3e8 rows 1..238 | 51 (0.725) | 14/15 | 0.030 |
| 3e8 minus capped 238 | 51 (0.725) | 13/14 | 0.043 |

The event set is itself even-row-biased (b^2-style); giants are additionally
even-biased beyond that base (p ≈ 0.03–0.04). vs a plain 1/2 null it is very
strong (p = 0.0009) but that is the wrong null. **Verdict: suggestive,
not established** — p ≈ 3% with one real counterexample and no mechanism.
Falsifier: a second odd-pre-jump-row giant (any giant at an odd pair row
other than 161). No mod-4 or mod-8 refinement exists (rows hit 0, 2 mod 4
roughly 1:2).

## 4. Landing-block growth: geometric vs linear — geometric wins, 14 points

Exact least-squares on the 14 genuine landings (row-238 capped excluded):

- geometric log b = a + m·x: slope m = 0.559902, **R² = 0.9607**,
  factor/event exp(m) = 1.7505
- linear b = a + m·x: slope 473,595.6, **R² = 0.4317**

Geometric description strengthened vs depth-1000 (R² 0.9607 vs 0.9439);
linear decisively worse. Consecutive ratios: 2.727, 3.915, 1.354, 2.940,
1.123, 1.363, 1.917, 1.197, 1.587, 1.422, 1.492, 4.951, 1.967 (mean 2.15).
**A description of 14 points, not a law** — directive25's reconciliation
caveat stands.

## 5. OEIS misses (record so nobody re-searches)

- `[2179, 5942, 23265, 31499, 92620, 103973, 141706, 271629, ...]` (giant
  landing blocks): **no entry**.
- `[2, 7, 13, 13, 24, 23, 22, 21, 24, 58, 97, 96, 97, ...]` (b-series with
  k = 1): **no entry** (consistent with the established
  `block_profile(k) = A000232(k) − 1` shift — the shifted series is the
  catalogued one, so this is not a new miss).

## Claims

```claim
id: wider-width-giant-record-3e8
statement: In the prime Gilbreath triangle from the sieve-3e8 run (16,252,325
  primes, depth 300), there are 14 genuine giant (2,4)-events (jump > 1000)
  with landing floorings >= 5,596,863 at pre-jump rows
  34,56,64,68,94,96,110,112,126,130,134,146,161,174 and one capped event at
  238 (flooring 1, jump >= 5,596,824). Rows 1..161 of the b-series match the
  depth-1000 (2e7) run exactly. The old depth-1000 capped i=161 is resolved:
  true jump 4,323,712, landing flooring 10,834,187. Record max genuine jump
  5,237,310 (i=174). Live-regime inter-giant max gap = 26 (gaps
  22,8,4,26,2,14,2,14,4,4,12,15,13), corroborating directive25's max-gap-26
  bound when width increased 15x and b increased 4,900x.
hypotheses: iterated absolute differences of primes below 3e8 to depth 300;
  giants = step-law (2,4)-events with jump > 1000; capped events excluded.
holds-here: yes
status: checked (exact integers; fits are descriptions, not theorems)
bearing: the recharge object of the run's narrowed target — giants keep
  arriving with max gap 26 across a 15x width increase.
anchor: code/out/pattern_finder_wider_giants.captured.txt,
  code/out/pattern_finder_giant_corrected.captured.txt
source: operator-computation
```

```claim
id: giant-parity-even-pre-jump-rows
statement: Among the 15 giant events of the wider-width run, 14 fire at even
  pre-jump rows (13/14 genuine, sole exception i=161 which is genuine at 3e8
  with jump 4,323,712). Exact hypergeometric P(>= observed even giants | event
  even base 37/51) = 0.030 (0.043 excluding the capped row-238); the event set
  is itself even-biased (even frac 0.725), so the giants' 0.933 even fraction
  is ~3% beyond base. No mod-4/mod-8 refinement; no mechanism; one real
  exception. CONJECTURE (numerical regularity), falsifier = any giant with a
  second odd pre-jump row.
hypotheses: same run as wider-width-giant-record-3e8.
holds-here: yes
status: checked numerically — suggestive, not established (p ~ 0.03, one
  real exception, no mechanism)
bearing: if a mechanism is found it would sit in the parity strata of the
  {0,2}-block dynamics; currently not load-bearing.
anchor: code/out/pattern_finder_giant_significance.captured.txt,
  code/out/pattern_finder_giant_parity2.captured.txt
source: operator-computation
```

```claim
id: giant-landing-geometric-fit-14
statement: Over the 14 genuine giant landings of the 3e8 run, exact LS fit:
  geometric log b = 8.4388 + 0.55990 x with R2 = 0.9607 (factor 1.7505/event)
  vs linear R2 = 0.4317. Geometric description holds on 14 points; ratios
  include 4.951 (13th) so it is a fit, not a law; directive25 reconciliation
  caveat stands.
hypotheses: as above.
holds-here: yes
status: numerical description only
anchor: code/out/pattern_finder_giant_corrected.captured.txt
source: operator-computation
```