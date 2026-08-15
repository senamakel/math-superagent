# CB-dying-pair contains a located internal contradiction

## Status
Located defect in the **statement** of the open gap `CB-dying-pair`.
Not a refutation of Gilbreath, and not a refutation of the *mathematics* of
the counterexample-backward skeleton — it is a mislabelling of which row is
"dying" and which row has block length 1. The first step of the gap
(enumerate (e,y) with |e−y| ≥ 4) is unaffected.

## The claim as stated (research/BACKWARD.md, gap CB-dying-pair)

> At the first failure row K, the dying row K−1 satisfies b_{K-1} = 1,
> A_{K-1}(0) = 1, and A_{K-1}(1) ∈ {4,6,8,…}. Let e = A_{K-2}(1) be the edge
> and y = A_{K-2}(2) be the intruder at row K−2. Then A_{K-1}(1) = |e − y| …

## Why it is contradictory (two facts from the run's own definitions)

1. **`block_profile(row)` = number of leading entries at positions 1,2,…
   lying in {0,2}.** (code/lib/gilbreath.py) So
   `b(row) = 0 ⇔ row[1] ∉ {0,2}`, and
   `b(row) = 1 ⇔ row[1] ∈ {0,2} ∧ row[2] ∉ {0,2}`.

2. **Reduction (proved): A_K(0) = |1 − A_{K-1}(1)|.** (research/notes/reduction.md)
   K is the *first failure row*, so A_K(0) ≠ 1, hence
   `A_{K-1}(1) ∉ {0,2}`.

From (2), `A_{K-1}(1) ∈ {4,6,8,…}` — so `A_{K-1}(1) ∉ {0,2}` — and therefore
from (1) **b_{K-1} = 0, never 1**. The lemma asserts `b_{K-1} = 1`
*simultaneously* with `A_{K-1}(1) ∈ {4,6,8,…}`, which is impossible by
definition.

## The row that actually has b = 1

The lemma's own data (`e = A_{K-2}(1)`, `y = A_{K-2}(2)`, `A_{K-1}(1)=|e−y|`)
refer to **block length 1 at row K−2**, not K−1: if b_{K-2} = 1 then the block
is exactly position 1, so the edge (last block entry) is A_{K-2}(1) and the
intruder (first entry past the block) is A_{K-2}(2), and the next row's second
entry is |e−y|. The dying row is K−1, which has b_{K-1} = 0.

## Correct wording
- dying row K−1: b_{K-1} = 0, A_{K-1}(1) ∉ {0,2}.
- the (edge, intruder) pair lives at row **K−2** with b_{K-2} = 1.
- the constraint that produces failure: |e − y| = A_{K-1}(1) ∉ {0,2},
  i.e. (e,y) as the lemma already enumerates.

## How this was checked
Direct reasoning from the two cited definitional facts (block_profile in
code/lib/gilbreath.py; reduction in research/notes/reduction.md). The
find_counterexample tool returned `undecided` on every refutable encoding in
this environment (including a deliberately trivially-refutable toy), so no
machine refutation was obtainable — the contradiction is a one-line
definitional check, not a model search.

## Claim
```claim
id: cb-dying-pair-statement-contradiction
statement: In the open gap CB-dying-pair, "the dying row K-1 satisfies
  b_{K-1}=1 and A_{K-1}(1) in {4,6,8,...}" is internally inconsistent: the
  dying condition A_{K-1}(1) not in {0,2} (which is exactly what makes K the
  first failure row by |1-A_{K-1}(1)| != 1) forces b_{K-1}=0 by the
  definition of block_profile (b=0 iff row[1] not in {0,2}). The row with
  block length 1 is K-2 (where the lemma's own edge/intruder e,y live), not
  K-1.
hypotheses: none; purely the run's own definitions (block_profile counts
  leading {0,2} entries from position 1; reduction A_K(0)=|1-A_{K-1}(1)|).
holds-here: yes
status: checked (one-line definitional reasoning; model finder unavailable
  for refutation in this environment)
bearing: the first step of CB-dying-pair (enumerate (e,y) with |e-y| >= 4)
  is unaffected, but the framing "dying row has b=1" is a located error: the
  b=1 row is the row BEFORE the dying row. The counterexample-backward
  skeleton should track the edge/intruder at K-2 with b_{K-2}=1 and the dying
  row K-1 with b_{K-1}=0.
anchor: code/refute/cb_dying_pair*.p, code/refute/cb_dying_pair_statement.md
```
