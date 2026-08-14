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
status: refuted
killed-by: the linear representation is a fourth evaluator/certificate, not a
classification. The zero set {n : a(n,d)=0} of a regular sequence is not
automatic in general, so this route still needs a search over the interval to
find the fixed points. The adopted block-transfer theorem supersedes it by
collapsing the search to a proven bijection plus a closed-form sum for s(d).
```

## Why it was not adopted

The regular-sequence formalism is correct and sourced (Allouche–Shallit; the
closure of k-regular sequences under prefix sums; kernel characterization). The
concrete first step — exhibit the 10-kernel and write A_0..A_9 — was feasible.
But the honest caveat in the original note is exactly why it lost: a(n,d)=0 is
a zero set of a regular sequence, not an automatic set, so the linear
representation certifies *evaluation* of a(n,d) but does not by itself classify
where it vanishes. It would have been a fourth independent evaluator (useful
for cross-verification), while the block-transfer approach gives a bijective
classification of the whole solution set and a closed form for s(d) — a
strictly stronger structural result for this problem.
