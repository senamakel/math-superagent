---
id: p2-proof-sum-cubes
kind: proof
---
Prove this in Lean 4, with a complete proof and no `sorry`:

> For every natural number `n`, the sum of the first `n` cubes equals the square
> of the sum of the first `n` naturals:
> `(∑ i ∈ Finset.range n, i ^ 3) = (∑ i ∈ Finset.range n, i) ^ 2`.

State it as a `theorem sum_cubes_eq_sq_sum`. Finish with
`#print axioms sum_cubes_eq_sq_sum`.
