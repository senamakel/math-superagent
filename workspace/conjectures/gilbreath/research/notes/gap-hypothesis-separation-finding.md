# Gap-hypothesis separation: decisive negative, and the corrective control

## The directive-14 separation check (done, EXIT_CODE=0)

`code/gap_hyp/gap_hypothesis_separation.py`, capture `code/out/gap_hypothesis_separation.captured.txt`.
Self-check PASS (A1, A2, A3 of problem.md reproduced before the comparison). n = 17983 gaps per column.

| metric | primes<200000 | iid {2..20} | iid {2..20} first=2 |
| --- | --- | --- | --- |
| max gap | **86** | 20 | 20 |
| mean gap | 11.1214 | 11.0189 | 11.0445 |
| max window mean, W=100 | 14.34 | 13.10 | 12.80 |
| max window mean, W=1000 | 12.37 | 11.574 | 11.408 |
| max window mean, W=10000 | 11.8382 | 11.0928 | 11.1304 |
| freq gap>6 | 0.5690 | 0.7021 | 0.7034 |
| freq gap>10 | 0.3969 | 0.5026 | 0.5025 |
| freq gap>20 | **0.1231** | 0.0000 | 0.0000 |
| freq gap>50 | 0.0034 | 0.0000 | 0.0000 |
| max gap / log^2(p_max) | 0.5772 | 0.1344 | 0.1344 |

**Verdict: none of the three candidate hypotheses separates.** For each of
(a) bounded mean gap per window, (b) bounded frequency of gaps > G, (c) Cramér
g_n = O(log^2 p_n), the prime column satisfies it AND the {2..20} columns ALSO
satisfy it — the {2..20} model's tail is strictly LIGHTER than the primes'
(its support caps at 20), and its window means are all smaller. Wherever the
columns genuinely differ, the difference goes the WRONG way for separation.

**Consequence (per the directive's own instruction): the sweep families
{2..20} / {2,4,6} / Geom(p=.25) are the WRONG negative controls.** Their
death is not explained by any gap-size statistic the primes beat them on.

## What the data does point at

- All 852/1154 sweep deaths happen at k ≤ 10 (89.7% at k ≤ 3) — a startup
  phenomenon, sensitive to the first ~20 gap positions.
- Prime gaps satisfy the PROVED Torelli bound g_n ≤ n (claim
  `torelli-prime-gap-bound`, RAIRO-ITA 40 (2006) 107–121). An i.i.d. {2..20}
  sequence violates g_n ≤ n with high probability in exactly the death window:
  P(g_2 ≤ 2) = 1/10, P(g_3 ≤ 3) = 2/10.

## Corrective control in flight

`code/gap_hyp/torelli_conditioned_control.py` (agent-run-78):

1. {2..20} iid, first gap 2, rejection-conditioned on g_n ≤ n — does the
   Torelli constraint alone rescue the family?
2. {2,4,6} first-gap-2, same condition.
3. iid WITH REPLACEMENT from the actual prime-gap multiset below 200000 —
   destroys order/autocorrelation, keeps the exact marginal. If this dies
   while the primes live, the discriminator is ORDER (the pairing of
   consecutive gaps), not the gap distribution.
4. same multiset control, conditioned on g_n ≤ n.

## Status

gap-size hypotheses: closed (no separation, wrong direction).
Order/autocorrelation hypothesis: under test.