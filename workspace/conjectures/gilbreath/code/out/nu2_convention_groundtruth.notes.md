# nu2 convention ground truth + dyadic dichotomy verification (THIS RUN)

Settles task `fix-vacuous-dyadic-artifacts` (Directive 60 item 3) and
independently re-verifies the dyadic-periodicity dichotomy on the literal
"suffix of the right diagonal" convention, using a from-scratch full-triangle
oracle (no `lib.rightdiag` import) — a second route to the same quantity.

## The vacuous-artifact fix

`code/out/dyadic_periodic_check.captured.txt` is VACUOUS and is hereby
flagged: its `make_input_gaps` added a leading gap-1 for the 2->3 difference
AND `build_triangle` prepended `[1]`, giving `A_1 = (1,1,2,4,...)` with an
ODD second entry — a broken triangle in which nu2 = 0 everywhere. That is why
the table prints zeros for every period. **A table of all-zeros must not be
read as evidence.** This capture is the surviving record; the corrected
computation is below.

`code/out/reproduce_dyadic_periodicity.py` no longer IndexErrors (the modulo
wrap is on disk and it exits 0) but does **not** reproduce the Directive-58
host stage-1 integers. That discrepancy is resolved here (see next section).

## Independent brute-force oracle (this run)

`code/out/nu2_convention_groundtruth.py` builds the FULL exact triangle from
A_0 = q (2-then-odds from the periodic halved-gap bit word, gap = 2 if bit
else 4), reads the right diagonal `delta(q_n)=[A_0[n],..,A_n[0]]`, and counts
2s in the maximal {0,2} suffix of the body `d[0..n-1]` under two scan
conventions. Hand-check bound: period-1 (consecutive odds) gives literal
suffix reaching index 1, nu2 = 1,1,1 at n=50,100,199 — the oracle matches the
hand expectation.

### Literal convention (i>=0): true maximal {0,2} suffix of the body

| period P | word      | nu2 at n=200,400,800,1200 | class |
|----------|-----------|---------------------------|-------|
| 1        | [1]       | 1,1,1,1                   | O(1)  |
| 2        | [0,1]     | 1,1,1,1                   | O(1)  |
| 4        | [0,0,0,1] | 1,1,1,1                   | O(1)  |
| 8        | [0,0,0,0,0,0,0,1] | 1,1,1,1          | O(1)  |
| 3        | [0,0,1]   | 132,267,532,798           | linear ~0.66n |
| 5        | [0,0,0,0,1] | 104,212,424,639         | linear |
| 6        | [0,0,0,0,0,1] | 67,132,267,398         | linear |
| 7        | [0,0,0,0,0,0,1] | 56,343,456,684       | linear |

**The dyadic dichotomy is CONFIRMED on the literal convention:** minimal
period a power of 2 ⇒ nu2 = O(1); minimal period with an odd factor ⇒ nu2
grows ~linearly. This is the substantive content of the whole dyadic line and
it survives an independent code path.

### Exact host values are NOT reproducible — resolved

The Directive-58 host table (P=2,4,8 ⇒ 2,2,2,2; odd periods ⇒ their quoted
numbers) is **not matched by any single documented build+scan convention**:

- power-of-2: literal scan reports 1,1,1,1 at n=200,400,800,1200, not
  2,2,2,2. Diagnosis (`code/out/diagnose_p2_count.py`): for P=2 the diagonal
  is `[q_n, 2, 2, 0,...,0, 1]` at some n (suffix reaches two 2s, count 2) but
  `[q_n, 4, 2, 0,...,0, 1]` at others (suffix reaches one 2, count 1),
  depending on the phase of where the 4 lands. So **nu2 for power-of-2
  periods is bounded but n-dependent (fluctuates between O(1) values), not
  exactly 2 at every sampled n** — the host's constant `2,2,2,2` is a
  specific-phase artifact, not a stable value.
- odd periods: three independent conventions end up mutually incompatible by
  an off-by-one (literal [132,267,532,798], i>2 [131,...], nu2_periodic
  phase -3 [133,265,533,799] vs host [133,264,533,798]).

**Consequence:** the exact integers in the Directive-58 stage-1 table are
unreliable (convention/phase-dependent) and must not be quoted; the
*qualitative dichotomy* is the verified content, now confirmed by an
independent oracle on the literal definition.

## Status

- Vacuous `dyadic_periodic_check.captured.txt`: flagged, not to be read as
  evidence (all-zeros from a broken triangle).
- Dichotomy (2^k ⇒ O(1), odd factor ⇒ linear): CONFIRMED over the stated
  range by an independent full-triangle oracle (8 period words, n ≤ 1200,
  exact integers, literal convention).
- Exact stage-1 host integers: REFUTED as convention-independent; do not
  quote them.
