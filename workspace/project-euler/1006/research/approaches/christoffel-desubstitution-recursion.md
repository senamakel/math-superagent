# Christoffel conjugacy + morphism desubstitution recursion

```approach
idea: Decompose the length-k factor set recursively by its largest-Fibonacci block. The run's
  first-occurrence data shows L(k) = [0..F_m−1] ∪ T(k), where F_m is the largest Fibonacci
  number ≤ k+1 and T(k) is a small tail (this pattern is visible at every k in
  code/out/positions.txt). The [0..F_m−1] block is the F_m-element conjugacy class of a single
  Christoffel word (the central/standard word of the rotation interval), whose conjugate-sum
  Σ_rot val(w_rot)² has a closed form in the word's gap structure. The tail T(k) is itself the
  factor set of a reduced length, obtained by desubstituting under the Fibonacci morphism
  σ: 0→01, 1→0. Together this gives Ψ(k) = (Christoffel orbit sum) + (morphism-transformed
  smaller Ψ), a recursion whose depth is O(log k).
mechanism: This is the standard combinatorics-on-words structure of Sturmian factors: the n+1
  length-n factors are the conjugacy classes of Christoffel words governed by the continued
  fraction of the slope, and the Fibonacci word's singular factorization (Fici,
  "Factorizations of the Fibonacci Infinite Word", in FRONTIER) supplies the recursive block
  structure. The run's findings "conjugate+singular iff k is Fibonacci" and the observed
  L(k) = [0..F_m−1] ∪ tail are exactly this decomposition, so this line is native to the
  object rather than imposed on it.
status: proposed
first-step: For k = 1..60, confirm L(k) = [0..F_m−1] ∪ T(k) with F_m the largest Fibonacci
  number ≤ k+1; for each tail factor F[p..p+k−1] (p ∈ T(k)) exhibit it as σ or a bounded
  composition of σ applied to a strictly shorter factor. Then write the recursion
  Ψ(k) = (orbit sum) + (transformed smaller Ψ), and check it reproduces the oracle Ψ(k) for
  every k = 1..150.
```
