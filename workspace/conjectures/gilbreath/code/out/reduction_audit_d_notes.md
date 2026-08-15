# reduction_audit (D) — the 1133 "constant-1 erosion" violations are an artifact

## Question

`code/gap_analysis/reduction_audit.py` section (D) reports 1133 violations of
`c_n >= c_{n-1} - 1`, where `c_n` = length of the maximal `{0,2}` suffix
("0-2 cycle") of the anti-diagonal `delta(q_n)`, excluding the bottom entry.
Is that a genuine phenomenon or a bug / convention error?

## Deciding evidence (code/gap_analysis/reduction_audit_d_investigate.py, EXIT_CODE=0)

1. **Exact reproduction.** Rebuilt diagonals with the audit's own sieve, the
   same incremental recurrence, and the same `zero_two_suffix_length`:
   `1133` violations over 9999 extensions. The number reproduces exactly.

2. **What the drop actually is — every one is a `4` stopper, all near the
   bottom.** In EVERY one of the 1133 violations, the first non-`{0,2}` entry
   going up the *new* diagonal is `4`. The bottom entry (`A_{n-1}(0)`) is `1`
   on every diagonal, and `A_{n-2}(1)` (the second entry of every row, the
   exact conjecture quantity) is in `{0,2}` for every `n ≥ 3` — including at
   every `n` where `c_n == 0`. So a "violation" is a diagonal whose cycle was
   *very long* and got cut by a `4` a few cells from the bottom; it is never
   a lost 1 or a lost second-entry `{0,2}`. Regeneration is undamaged.

3. **The two quantities measure different objects.** Consecutive cells of a
   ROW are difference-pairs, so `{0,2}` is closed along a row and the row law
   `b_{k+1} ≥ b_k − 1` (the proved block lemma / step law, constant 1) holds:
   0 violations over rows 0..10000. Consecutive cells of an ANTI-DIAGONAL are
   NOT difference-pairs — `c_n`'s cycle spans `c_n` cells in `c_n − 1`
   *different* rows (e.g. at n=31, 21 cells in 20 distinct rows). There is no
   `{0,2}` closure along the anti-diagonal, so the constant-1 erosion proven
   for rows does not transfer. The anti-diagonal `c_n` is transversal to a
   row's leading block.

## Verdict

**Artifact / convention mismatch, not a bug in the arithmetic and not a
genuine counterexample to the block lemma.** The audit's own comment is
correct: "the {0,2}-cycle length of an anti-diagonal is transversal to a
row's leading {0,2} block, which is the object the (proved) constant-1 block
lemma actually governs." The 1133 are real drops of the *diagonal suffix*, but
that suffix is a different, transversal quantity: it is NOT the leading {
{0,2}} block of any single row, its consecutive entries are not difference
pairs, and its drops correspond to a `4` entering within a few cells of the
bottom of a *long* cycle — which is exactly where a new (2,4)-regeneration
would build fresh {0,2} cells. The conjecture quantity (`A_k(1) ∈ {0,2}`) is
untouched on the whole range.

## claim

```claim
id: reduction-audit-D-artifact-transversal
statement: The 1133 reported violations of c_n >= c_{n-1} - 1 for the {0,2}-suffix
  length c_n of the anti-diagonal delta(q_n) (excluding the bottom entry) are an
  artifact, not a counterexample: they measure a transversal quantity. Every one
  of the 1133 drops is stopped by a value-4 entry within a few cells of the bottom
  of a long cycle; the bottom entry A_{n-1}(0) is 1 on every diagonal and the
  second entry A_{n-2}(1) (= delta(q_n)[n-2]) is in {0,2} for every n >= 3, so the
  conjecture quantity is untouched. Consecutive cells of an anti-diagonal are not
  difference-pairs (its cycle spans c_n cells in c_n - 1 distinct rows), whereas a
  row's consecutive cells ARE, so the {0,2} closure behind the proved row law
  b_{k+1} >= b_k - 1 (0 violations over rows 0..10000) does not transfer to the
  diagonal suffix.
hypotheses: primes < 2e5 (N=10001), exact integer arithmetic, same recurrence as
  reduction_audit.py.
holds-here: yes (this is the real-prime case under study)
status: checked
bearing: explains reduction_audit.py section (D); the diagonal-cycle law is NOT a
  valid reformulation of the block lemma and its "refutation" is a convention
  artifact. The proved row-direction block lemma b_{k+1} >= b_k - 1 stands.
anchor: code/out/reduction_audit_d_investigate.captured.txt
```

The row-coordinate b sequence `[0,2,7,13,13,24,...]` reproduced here matches
the depth-1000 record (`[2,7,13,13,24,...]` for k=1..) — `b_k =
A000232(k)-1`. Both the diagonal and the row computation were re-derived from
scratch in this file; the row computation additionally uses
`lib.gilbreath.rows_generator` / `block_profile`, an independent code path.
