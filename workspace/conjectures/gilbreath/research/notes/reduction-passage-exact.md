# rising-sea: the reduction passage is a theorem, not an assumption

`status: checked` (machine, exact integer, N=10001 prime triangle)
`thread: regeneration` (Route B, Granville nu2)
`claims: ` (see below)

## The setting that makes Lemma 5.4 obvious

Directive 38 item 3 / Directive 41 asked the sharp question: is the passage
from the real column dynamics `delta_k(q_n)` to the `(pattern, v)` model a
theorem, or an assumption?  Specifically the model decouples the pattern `eps`
from the trajectory's own value `v` — if the entries the column meets depended
on where the trajectory currently is, `nu2` would not be prefix-determined and
the budget would not close.

The answer is that **the whole problem is native to right-diagonal
coordinates**, and in those coordinates the decoupling is forced by the
triangular geometry.

The triangle identity is `A_k(i) = |A_{k-1}(i) - A_{k-1}(i+1)|`.  On the right
anti-diagonal `delta(q_n) = (A_0(n), A_1(n-1), ..., A_{n-1}(0))` this reads

    delta_k(q_n) = | delta_{k-1}(q_n) - delta_{k-1}(q_{n-1}) |

so the `eps` the new column meets at step `k` is exactly
`delta_{k-1}(q_{n-1})` — an entry of the **previous prefix's stored diagonal**
`delta(q_{n-1})`, which is fixed once `q_1..q_{n-1}` is fixed.  The new column
never feeds back into the pattern.  The "fixed pattern, independent of the
trajectory" hypothesis of the `(pattern, v)` model is a *consequence* of the
recurrence identity, not an extra assumption.

## Machine verification

`code/gap_analysis/reduction_audit.py` (on the real prime triangle, N=10001,
O(N^2) exact abs-diffs, O(N) memory):

- (A) the incremental diagonal recurrence reproduces the full A-triangle bottom
  rows and problem.md's worked rows A_1, A_2, A_3 — 0 mismatches.
- (B) **the `|x-eps|` model-match on the 0-2 cycle positions: 0 mismatches
  over 49,873,204 positions.**  Every real descent obeys exactly
  `delta_k = |delta_{k-1} - eps_k|` with `eps_k in {0,2}` read from the prefix.
- (C) two different odd extensions descend through the identical pattern
  (prefix-determined).
- (D) `code/gap_analysis/block_constant_diagonal.py` reproduces the **block
  lemma constant 1** in row coordinates: the leading `{0,2}`-block `b_k`
  protects rows `k..k+b_k` (leading 1 persists) — 0 violations; `b_1..b_12 =
  2,7,13,13,24,23,22,21,24,58,97,96` matches the established record — and all
  10001 prime prefixes are successful (bottom = 1).

## Three-line proof (Directive 48 item 1) — now a proved claim

The fixedness clause is not merely machine-checked; it is a *definitional
fact*.  With the right diagonal indexed as `delta_k(q_n) = A_k[n-k-1]`
(k = 0..n-1), the triangle recurrence `A_k[i] = |A_{k-1}[i] - A_{k-1}[i+1]|`
at `i = n-k-1` gives, for each k >= 1,

    delta_k(q_n) = |A_{k-1}[n-k] - A_{k-1}[n-k-1]|
                 = | delta_{k-1}(q_n) - delta_{k-1}(q_{n-1}) |.

By locality of absolute differencing the first `n-k-1` entries of row `k` are
unchanged if the top row is extended past the prefix, so the eps cell
`delta_{k-1}(q_{n-1})` is a function of `q_1..q_{n-1}` only; `q_n` appears in
`delta(q_n)` solely at the bottom cell `delta_{n-1}(q_n) = A_{n-1}[0]`.  Hence
the `{0,2}` cycle and `nu2` are fixed in advance — no cycle-position eps
depends on the trajectory.  This kills the Directive 38 circularity worry in
three lines.  Full write-up: `research/notes/prefix-determinism-proof.md`;
machine check `code/out/prefix_determinism_proof_check.py` +
`code/out/prefix_determinism.captured.txt`:

- Part 1 (identity cell by cell, n=2..200, real primes): **19,900 positions,
  0 mismatches**.
- Part 2 (eps prefix-locality, 3 distinct continuations per fixed prefix,
  n=3..200): **59,697 positions, 0 mismatches**.

**`reduction-passage-exact` is PROVED** (the identity *is* the recurrence),
machine-checked over the stated ranges only — no "theorem/proved" wording in
captured output (Directive 51).

## What this closes and what stays open

- **CLOSED (Directive 41 fixedness concern):** `nu2` is prefix-determined, so
  the Lemma 5.4 budget argument (`v <= 2*nu2+2` forces success) is valid as a
  reduction.  The remaining open content of Route B is *solely* the supply side
  `nu2(q_{n-1}) > n^beta, beta > 0.525` — as GOAL.md already says.

- **Negative result kept honest:** the *diagonal-cycle length* `c_n` does NOT
  erode by exactly 1 per extension (1133 violations of `c_n >= c_{n-1}-1`).
  That quantity is a transversal cut, not the proved step law's block; the
  claimed protection constant 1 is a **row** property (verified 0 violations).
  Do not cite "constant-1 erosion of the diagonal cycle" — it is false and the
  step law lives in row coordinates.

```claim
id: reduction-passage-exact
statement: In right-diagonal coordinates, the (pattern, v) model of Granville Lemma 5.4 is an EXACT representation of the real column dynamics: delta_k(q_n) = |delta_{k-1}(q_n) - eps_k| with eps_k = delta_{k-1}(q_{n-1}) read from the stored prefix diagonal, so the pattern is prefix-determined and independent of the new column's value. nu2 is computed in advance from q_1..q_{n-1}. This makes the Lemma 5.4 budget argument a theorem of the triangular geometry, not an assumption.
hypotheses: 2-then-odds input (all gaps after the first even); exact integer arithmetic
holds-here: yes (real prime triangle, N=10001, oracle reproduces problem.md rows)
status: checked (0 model mismatches over 49,873,204 positions)
bearing: Route B reduction — closes the fixedness gap in granville-nu2-reduction.md; the only open content of Route B remains the supply side nu2 > n^beta.
anchor: code/gap_analysis/reduction_audit.py, code/out/reduction_audit.captured.txt, code/gap_analysis/block_constant_diagonal.py, code/out/block_constant_diagonal.captured.txt, research/notes/prefix-determinism-proof.md, code/out/prefix_determinism_proof_check.py, code/out/prefix_determinism.captured.txt
answers: verifies the fixedness clause Directive 41 asked to name
```
