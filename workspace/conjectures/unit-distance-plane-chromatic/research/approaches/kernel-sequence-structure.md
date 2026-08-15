# Kernel-sequence structure — pattern-recognition report

## What was examined

The run's richest integer data is the sharp-kernel census (`C_N` = graphs on N
vertices with min-degree>=4, K4-free, K2,3-free, neighbourhood-max-degree<=2),
the class any 5-chromatic unit-distance graph must belong to. Per-N counts from
`code/out/census_kernel_n11_run.captured.txt` and
`code/out/analyze_kernel_chrom.captured.txt`:

| n | kernel members | 4-chromatic | 3-colourable |
|---|----------------|-------------|--------------|
| 8 | 1 | 1 | 0 |
| 9 | 4 | 1 | 3 |
| 10 | 16 | 16 | 0 |
| 11 | 228 | 198 | 30 |

## Tool results

- `analyze_sequence([1,4,16,228])`: not a low-degree polynomial; differences
  [3,12,212],[9,200],[191]; leading ratios 4.00,4.00,14.25. No evidence of
  polynomial growth.
- `find_linear_recurrence([1,4,16,228], max_order=3)`: **no** constant-
  coefficient linear recurrence of order <=3 fits all four terms.
- `oeis_lookup([1,4,16,228])` and `oeis_lookup([1,1,16,198])`: **both miss** —
  neither sequence is catalogued. No closed form will be looked up.
- Same tools on the 4-chromatic subset [1,1,16,198]: no structure.

## The one visible (fragile) observation

The kernel counts begin 1, 4, 16 = 4^0, 4^1, 4^2 — a perfect geometric head —
and then jump to 228 at n=11 (ratio 14.25). The 4-chromatic subset head is
1,1,16 and already breaks by n=9. With only four terms and OEIS silent, there
is no defensible closed form; the 4^k head is coincidence-sized and would need
n=12 to start to mean anything.

## Verdict

**No exploitable sequence structure exists in the data this run produced.** The
census sequences are four terms long, not catalogued, not polynomial, and not
constant-coefficient-recurrent. The genuinely load-bearing pattern is not a
*number* sequence but a *structural* one: every kernel member through N=11 is
4-colourable (verified by two independent oracles, Cadical SAT and exhaustive
backtracking, 249/249 agree). That is the size-bound result already recorded.

## What would settle the question

Only the n=12 kernel count (and whether any member is non-4-colourable) would
decide whether a recurrence/closed form exists. That enumeration is
infeasible (the census infeasibility point was n=11; n=12 is ~100M+ graphs). So
there is no route in this run to turn the kernel-count head into a theorem, and
the sequence tools correctly refuse to manufacture one.

## Recommendation

Do not spend budget hunting structure in these four terms. The useful next
derivation is structural, not numerical: fix the actual 4-chromatic members
(e.g. the n=8 and n=9 kernels are unique, from `analyze_cores_small`) and ask
whether any forced-monochromatic pair exists under 4 colours, per the
`G-forced-pair-exists` crux — that is where a bound could move, not in the
counts.
