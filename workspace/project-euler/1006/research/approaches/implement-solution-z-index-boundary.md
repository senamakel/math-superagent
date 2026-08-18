# Implement-solution continuation — decisive boundary result

The failed task and banked attempts were inspected first. The universal-Euclidean primitive itself is sound, but the proposed mech_psi→single-call reduction is not.

## Theory and complexity

The governing theory is the mechanical-word representation of the Fibonacci Sturmian word, with the telescoped decimal value expressed as a weighted sum of floors. `ueuclid` computes one fixed-intercept floor sequence in logarithmic Euclidean time. Formulation B, however, sums over `m=0..k`; after reindexing, each digit-floor has a different intercept. A single `ueuclid` node therefore cannot evaluate the outer square without a further joint-index identity. This is a structural obstruction, not a bound to increase. The attempted efficient evaluator is consequently not implemented.

## Executed smallest harness

`code/verify_z_index.py` was written and run. It compares `ue0` (the correct 0-indexed wrapper, weights `z^0,...`) with a literal 0-indexed loop at `k=1,2,3`, then checks `mech_psi` formulation A/B.

Output:

```
z = 90900901
k=1: all ue0 moments = True
k=1: mech A=B=1, values=[0, 1]
k=2: all ue0 moments = True
k=2: mech A=B=101, values=[0, 1, 10]
k=3: all ue0 moments = True
k=3: mech A=B=20302, values=[1, 10, 100, 101]
INDEXING HARNESS PASSED: k=1,2,3; ue0 weights z^0..z^k.
```

Thus the z^0 indexing is pinned and is not the remaining failure.

## Attack / counterexample

`code/refute/reduction_boundary_harness.py` was then written and run. It tests the tempting single-intercept second-moment reduction against the exact mechanical oracle:

```
k=1: mech_psi=1, single-intercept-S2=0, equal=False
k=2: mech_psi=101, single-intercept-S2=0, equal=False
k=3: mech_psi=20302, single-intercept-S2=100900000, equal=False
Conclusion: z^0 indexing is fixed by ue0, but the prior single-call
reduction is mathematically insufficient: formulation B has k+1 intercepts.
```

The smallest counterexample is k=1. Therefore no honest O(log) evaluator or target residue can be produced from the existing artifacts. Running larger bounds would settle nothing new: the failure is already structural at k=1. The required next step is a different joint-index theorem/monoid, not a larger computation. The corrected anchors and `10^18` are intentionally not reported.
