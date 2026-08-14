# Approach — 10-regular sequence linear representation (Allouche–Shallit)

```approach
idea: Treat a(n,d) = f(n,d) − n as a 10-regular sequence (Allouche–Shallit
"Automatic Sequences", Ch. 16) and build its finite linear representation;
evaluate and certify the fixed points by base-10 matrix-automaton products
instead of arithmetic digit peeling.
mechanism: c_d(n) := number of digit-d occurrences in the decimal writing of n
satisfies c_d(10n+r) = c_d(n) + [r=d] for r∈{0..9}, so its 10-kernel is
finitely generated over ℤ (by {c_d, 1}); hence c_d is 10-regular (unbounded,
so *regular* but not automatic).  By the closure of k-regular sequences under
prefix sums, f(n,d) = Σ_{m≤n} c_d(m) is 10-regular, and n↦n is regular, so
a(n,d) = f(n,d)−n is 10-regular.  A k-regular sequence has a finite k-kernel,
hence a linear representation a(n) = u^T·A_{w_1}···A_{w_k}·v over the base-10
digits w of n.  This is a fourth structurally independent evaluator — a matrix
product over the digit string — distinct from the three already on disk
(place-value peeling in code/lib/digits.py, MSD block sums, and memoized
digit-DP in code/verify.py), and the linear representation is a compact,
independently checkable certificate for the whole sequence.
status: proposed
first-step: symbolically compute the 10-kernel of a(·,1) for j=0..3
(a(10^j n + r, 1) for 0 ≤ r < 10^j), exhibit the finitely many kernel
elements and their ℤ-linear relations, and write the matrices A_0..A_9 of the
linear representation; then check a(11,1)=4, a(12,1)=5 via the matrix product.
```

## Which parts are established, which are speculation

- **Established (named theory).** k-regular sequences and the kernel
  characterization are Allouche–Shallit, *Automatic Sequences: Theory,
  Applications, Generalizations* (CUP 2003); closure of k-regular sequences
  under summatory (prefix sums) is a theorem there. The recurrence
  c_d(10n+r) = c_d(n) + [r=d] is immediate from the definition.
- **Established by this run.** a(n,d) is exactly f(n,d)−n with f as in the
  problem; the fixed points are finite and bounded by n ≤ d·10^10
  (Khovanova–Marton Prop 9.1, on disk).
- **Speculation.** That the matrix-product evaluator will be simpler to
  certify or faster than the three arithmetic evaluators already present; the
  exact dimension of the kernel (I expect it to be small — a handful of
  elements such as f(·,d), n, 1, and log-related terms) and the concrete
  matrices. The first step exists precisely to pin these down.

## Honest caveat

The *zero set* {n : a(n,d)=0} of a regular sequence need not be automatic in
general, so this route gives a fresh evaluation/certification engine, not by
itself a finiteness theorem — it still leans on the sourced Prop 9.1 bound for
completeness.
