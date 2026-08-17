# Bouchard, "An averaging result for union-closed families of sets" (arXiv:2509.12537, 2025)

<!-- source: https://arxiv.org/html/2509.12537 | full text: research/sources/bouchard-averaging-result-upto-n2-2509.full.md -->

## What it establishes

Let `A` be a separating union-closed family on base set `[n]`, with
`A_<x = {A ∈ A : |A| < x}`; let `B` be a smallest irredundant subfamily of
`A_<n/2` whose union equals the union of `A_<n/2`. Everything is about the
**average set size** `Avg(A) = (Σ|A|)/|A|`, because Avarge ≥ n/2 implies UC:
an element counting argument (each of the n elements, on average in Avg(A)
sets) forces some element in ≥ Avg(A) ≥ n/2 of the sets, so present in ≥ |A|/2.

- **Theorem 1.4**: if `A` is separating with height `h ≤ 3`, then
  `Avg(A) ≥ n/2`, so UC holds.
- **Theorem 2.1 + Cor 2.2**: if `A` is separating with height `h = 4 ≤ n` and
  `0 ≤ |B| ≤ 2`, then `Avg(A) ≥ n/2`; hence some element is in ≥ |A|/2 sets —
  **UC holds for this class**. Lemma 2.1.1 (Falgas-Ravry) `|A| ≥ n` is used.
- **Section 3 — the limit**: `h = 4` is the **largest** height for which this
  averaging approach yields the bound. Theorem 3.2: for any `n ≥ 11` and
  `k ∈ [5, n+1]` there is a separating union-closed `A` with height `k`,
  `|B| = 1`, and `Avg(A) < n/2`. So averaging based on a single-small-family
  irredundant `B` fundamentally cannot reach height ≥ 5.
- Section 4 considers the remaining `3 ≤ |B| ≤ 4` case for `h = 4`.

## Bearing for this run

- **New restricted class, provable by averaging**: separating UC families with
  height ≤ 4 (with the `|B| ≤ 2` nuance at 4). Add to ROOT's settled classes.
- **Sharpens the known limits of averaging**: this is the same obstruction the
  library records as `cms-averaged-frankl-wrong` (averaging has intrinsic
  limits). Here is an explicit, modern witness: averaging cannot prove UC past
  height 4, because explicit separating families with `h ≥ 5, |B|=1, Avg<n/2`
  exist. Any attempt to "fix UC by an Avg ≥ n/2 argument" must confront this.
- Not a new record constant; a structural/strict-class contribution.

## Falsifier

A separating union-closed family with `h = 4`, `0 ≤ |B| ≤ 2`, and
`Avg(A) < n/2` would refute Theorem 2.1. (None known; theorem is that none
exists.)

```claim
id: bouchard-averaging-height4
statement: For any separating union-closed family A with height h = 4 ≤ n and 0 ≤ |B| ≤ 2
  (B a smallest irredundant subfamily of A_<n/2 with b(B) = b(A_<n/2)), Avg(A) ≥ n/2
  (Theorem 2.1); hence some element of [n] is in ≥ |A|/2 member sets, so UC holds for this
  class (Corollary 2.2). Theorem 1.4: UC (via Avg ≥ n/2) holds for all separating union-closed
  families with h ≤ 3. Theorem 3.2: h = 4 is the LARGEST height reachable by this averaging
  argument — for every n ≥ 11 and k ∈ [5, n+1] an explicit separating union-closed A with
  height k, |B| = 1, Avg(A) < n/2 exists.
hypotheses: A separating finite union-closed family, universe [n], height h the max chain size;
  B an irredundant subfamily of A_<n/2 of minimum size with the same union; h = 4 ≤ n case
  additionally needs 0 ≤ |B| ≤ 2 and n ≥ 4.
holds-here: yes — this is a new settled restricted class (height ≤ 4 with the |B| ≤ 2 nuance),
  additive to ROOT's list; and an explicit modern witness that pure averaging cannot prove UC
  past height 4 (links to cms-averaged-frankl-wrong).
status: asserted (Bouchard arXiv:2509.12537, 2025, proofs in full text; not yet run through the
  oracle)
bearing: adds "separating UC families of height ≤ 4 (with |B| ≤ 2)" to the settled classes;
  tightens the known limits of the averaging method with explicit h ≥ 5 witnesses (Avg < n/2).
  Not a new constant; a structural/strict-class contribution for the minimal-counterexample and
  abundance-profile lines.
anchor: research/sources/bouchard-averaging-result-upto-n2-2509.full.md
follows-from: falgas-ravry-separating-degree (Lemma 2.1.1 |A| ≥ n), cms-averaged-frankl-wrong
answers: (open — averaging-route limits)
falsifies: a separating union-closed family with h = 4, 0 ≤ |B| ≤ 2 and Avg < n/2.
```
