# Prefix-determinism identity — proof (Directive 48 item 1)

**Status: proved.** Filed as the load-bearing step that removes the
circularity worry of Directive 38: the `{0,2}` cycle pattern (and hence `ν₂`)
used by the Lemma 5.4 descent is fixed before the new element `q_n` is ever
seen. Machine evidence: `code/out/prefix_determinism.captured.txt`.

## Statement

Let `A_0 = (q_1, q_2, …)` be a real (or any exact-integer) top row, and define
the iterated absolute-difference rows

```
A_{k+1}(i) = |A_k(i) − A_k(i+1)|,        i ≥ 0.
```

For a prefix length `n`, the **right diagonal** is the last entry of each row
restricted to that prefix:

```
δ_k(q_n) = A_k[n − k − 1],        k = 0, …, n−1.
```

**Claim.** For every `n ≥ 2` and every `k = 1, …, n−1`,

```
δ_k(q_n) = |δ_{k−1}(q_n) − δ_{k−1}(q_{n−1})|.          (⋆)
```

The quantity `ε_k := δ_{k−1}(q_{n−1})` on the right is read **wholly from the
stored prefix diagonal** `δ(q_{n−1})` — that is, from `A_0, …, A_{n−1}` built
from `q_1, …, q_{n−1}` alone — so no entry of the descent pattern depends on
`q_n`. The new element `q_n` enters only the bottom cell `δ_{n−1}(q_n) =
A_{n−1}[0] = |q_{n−1} − q_n|`.

## Proof (three lines)

By the definition of the right diagonal and the row recurrence, for `0 ≤ k−1 ≤
n−2`,

```
δ_{k−1}(q_n)   = A_{k−1}[n−k−1],        (last entry of row k−1 over prefix n)
δ_{k−1}(q_{n−1}) = A_{k−1}[n−k−2].      (last entry of row k−1 over prefix n−1)
```

Then `δ_k(q_n)` is the last entry of row `k` over prefix `n`:

```
δ_k(q_n) = A_k[n−k−1]
         = |A_{k−1}[n−k−1] − A_{k−1}[n−k−2]|      (row-recurrence, i = n−k−1)
         = |δ_{k−1}(q_n) − δ_{k−1}(q_{n−1})|.       ∎
```

Because absolute differencing is local (each new row entry is a function of two
adjacent entries of the previous row), the first `n−k−1` entries of row `k`
computed from the full top row are identical to those computed from any top
row with the same prefix of length `n`. Hence the eps cells
`δ_{k−1}(q_{n−1})` are genuinely **prefix functions**: they are determined by
`q_1, …, q_{n−1}` and are invariant under how the top row is continued past
`n−1`.

## Why this is exactly the descent-model eps

In the Lemma 5.4 descent model the orbit is

```
v_0 = v,     v_{k+1} = |v_k − ε_k|,     ε_k ∈ {0, 2},
```

with the `ε_k` running over the `{0,2}` cycle read from `δ(q_{n−1})`. Identity
(⋆) is precisely that recurrence in right-diagonal coordinates: the `ε_k` are
the prefix cells `δ_{k−1}(q_{n−1})`, and `ν₂ = #{k : ε_k = 2}` is a count over
that prefix diagonal. Since (⋆) makes every `ε_k` independent of `q_n`, the
whole descent pattern — the sequence of eps values, the `{0,2}` cycle, and
`ν₂` — is **prefix-determined**. The earlier concern (Directive 38) that `ν₂`
might be circularly coupled to the trajectory entering the new column is
killed: `q_n` appears in `δ(q_n)` only at the diagonal bottom, and no
cycle-position eps is read there.

## Machine verification

Program: `code/out/prefix_determinism_proof_check.py`, exact integers, oracle
`lib.gilbreath.rows_generator`.

- **Part 1** — (⋆) cell by cell on the real primes, prefix lengths `n =
  2..200`: **19,900 positions, 0 mismatches.**
- **Part 2** — prefix-locality: for each `n = 3..200`, fix the prefix
  `q_1..q_{n−1}` and append *three distinct* primes `q_n`; the descent eps
  cell `δ_{k−1}(q_{n−1})` is rebuilt from the continuation triangle and must
  equal the stored prefix diagonal in every case: **59,697 eps positions, 0
  mismatches.** Also confirmed each `{0,2}` cycle region of `δ(q_{n−1})` is
  `{0,2}`-valued (594 checks, 0 violations).

Both parts report zero violations; the verdict line uses CONFIRMED over the
stated range only (Directive 51 — no "theorem"/"proved" wording in captured
output).

## Scope

This identity is a **definitional fact**: it *is* the triangle recurrence
restated in right-diagonal coordinates. It proves prefix-determinism only. It
does **not** by itself prove the descent outcome (`x_L ∈ {0,2}`) — that is the
separate, Lean-formalised core (claim `lemma54-descent-lean-formalised`), and
the bridge from this identity to the Lemma 5.4 conclusion is the composition
Link A `/` `g*_n ≤ 2ν₂+2 ⟹ success`.
