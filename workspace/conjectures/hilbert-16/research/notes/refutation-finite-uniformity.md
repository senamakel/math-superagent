# Refutation: pointwise finiteness is not uniformity

```claim
status: checked
statement: Pointwise finiteness of parameter-indexed objects does not imply one uniform finite bound.
counterexample: The TPTP problem `code/refute/finite_uniformity.p` was searched by `find_counterexample` and returned `SZS status: CounterSatisfiable`. Its axioms assert only that every parameter object is finite; its conjecture asserts a common cardinality bound. The returned finite model satisfies the axiom and falsifies the conjecture.
search-frame: First-order finite-model search of the abstract bridge, not a counterexample to Hilbert 16.2 or to the quadratic-family hypotheses.
falsifier: A valid uniformity result must use extra structure, e.g. compact/algebraic parameterization plus a genuine uniform zero-count theorem.
```

Hand check: finite sets of cardinalities 0,1,2,... are individually finite but have no common finite bound. Thus the naive compactness/pointwise-finiteness bridge in `G-uniform` is false when its structural hypotheses are omitted.
