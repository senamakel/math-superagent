# Pattern pass 2026-08-19 — full on-disk sequence audit (pattern_finder)

Everything below is exact over the terms supplied; conjectures are labelled
with their falsifier terms. Programs and captures named for provenance.

## The two living conjectures, and their NEVER-COMPUTED falsifiers

Both conjectures were proposed by prior passes (pattern-pass-bautin-complement-
a052905.md, sequence-6param-bautin-audit.md) and both were left with falsifier
terms that **no run ever computed** — every attempt died at an intermediate
degree:

1. **5-param complement conjecture** `c(h) = (h^2+14h+8)/8` for even h >= 4
   (h=2 exceptional), equivalently `a_d = (C(h+4,4) - c(h))/2` for d >= 6.
   Verified exactly through d=16 (a_16 = 1505, from `.d16.tmp.txt`).
   **Falsifier: a_18 = 2392 (h=16).** Prior d18 runs reached only degrees
   14 (.d18_pattern_run.txt), 15 (.d18v2.tmp.txt), 16 (.d18_final2.tmp.txt)
   before being killed by the tool cap.

2. **6-param complement conjecture** `c6(h) = (h^2+22h+8)/8` (h=2 exceptional),
   i.e. `c6(h) = A052905(h/2) + h`. Verified exactly through d=12
   (a6_12 = 1481, from focal_6coeff_L12.txt recount).
   **Falsifiers: a6_14 = 3068 (h=12, c6=52); D6_14 = 37456183296000**
   (denominator identity D5 = D6). Prior L14 runs reached only degrees 11
   (.focal_6coeff_L14_run.txt) and 12 (.focal_6coeff_L14_pattern_run.txt)
   before the tool cap.

### Delegated this pass (tool_builder)

- **agent-run-4**: `python3 code/bautin/membership_d18.py 18` — no checkpoint
  support; previous attempts suggest ~2-4h wall (d16 took ~1947s, per-degree
  ratio ~2.1). Settles a_18 (falsifier) and L18 in <L4,L6,L8> (extends the
  Bautin-trick membership chain, the standing thesis).
- **agent-run-5**: `python3 code/bautin/focal_counts_6coeff.py --resume
  --max-degree 14 --deadline-min 240 --ckpt code/out/.focal_6coeff_state.json`
  — checkpoint has done_through=12, total_elapsed ~1594s; degrees 13-14 remain.
  Settles a6_14 and D6_14 (both falsifiers).

## Sequence-tool verdicts this pass (exact, computed terms only)

- `analyze_sequence` [4,30,97,236,485,890,1505]: not low-degree polynomial;
  `find_linear_recurrence` order<=4: none. OEIS: miss (recorded).
- `analyze_sequence` [10,16,23,31,40,50] (5-param complement tail):
  **constant second difference 1 — exactly quadratic**. Order-3 recurrence
  (3,-3,1) verified. OEIS: **A052905** = (n^2+7n+2)/2 at n=h/2.
- `analyze_sequence` [6,56,220,628,1481]: not polynomial; CCLR order<=3: none.
  OEIS: miss (recorded).
- `analyze_sequence` [14,22,31,41] (6-param complement tail):
  **constant second difference 1 — exactly quadratic**. (The order-2
  rational-coefficient fit (54/25,-59/50) from find_linear_recurrence is the
  documented false-positive trap on 4 terms; not reported as regularity.)
  OEIS lookup of the 6-param complement tail itself was NOT re-run (prior
  pass already recorded a miss for [9,14,22,31,41]).
- `oeis_lookup` [8,192,18432,1105920,22295347200,37456183296000]: miss
  (recorded — nobody searches the denominator sequence again).

## Refutations re-confirmed this pass (already on disk)

1. **Symmetry-pairing**: if a_d = (dim - c)/2 came from oddness under a
   signed-permutation involution, c(h) would equal |Fix_pi(h)| for one pi.
   Exact enumeration of all 312 signed involutions (5-param) / 76 permutation
   involutions (6-param): no match (complement_symmetry_probe.captured.txt,
   complement_symmetry_probe2.captured.txt).
2. **Rotation-operator-only denominator mechanism**: pure 2-power lcm from the
   operator vs observed odd factors 3,5,7 in D_d
   (research/findings/sequence-6param-bautin-audit.md).

## No other integer data awaiting analysis

All other captures reviewed (i6b toys, df2a slow-divergence, brute oracle,
membership runs): symbolic expressions or already-analyzed counts. Nothing
else on disk is an un-sequenced integer stream.

## What would falsify each claim (restated)

- A052905 identification for the 5-param complement: first term h=16 (a_18);
  predicted 2392. Settled by agent-run-4.
- 6-param c6 quadratic: a6_14 = 3068 and D6_14 = 37456183296000.
  Settled by agent-run-5.
