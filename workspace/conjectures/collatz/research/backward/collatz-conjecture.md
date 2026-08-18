```skeleton
goal: For every positive integer n, iterating C(n)=n/2 when n is even and C(n)=3n+1 when n is odd eventually reaches 1 (equivalently, the accelerated map T has only the trivial cycle 1 -> 4 -> 2 -> 1 and no divergent positive orbit).
implies: By the counterexample dichotomy, any failure is either an unbounded orbit or entry into a non-trivial positive cycle. Thus it suffices to prove both universal exclusions: (D) every positive T-orbit is bounded (or reaches the trivial cycle), and (C) T has no non-trivial positive cycle. Together, determinism and the fact that a bounded orbit in the positive integers is eventually periodic imply every orbit enters a cycle; (C) identifies that cycle as the trivial one, hence the original orbit reaches 1.
status: sketched
rests-on: lagarias-counterexample-structure, lagarias-map-reduction
```

```gap
id: G-no-divergent-orbit
lemma: Every positive integer has a bounded accelerated Collatz orbit; more strongly, for every n there exists k with T^k(n) < n (or an equivalent global descent/termination statement sufficient to exclude an unbounded orbit).
status: open
next: theorem_prover: formalise the exact implication from a uniform descent predicate (for every n, exists k, T^k(n)<n) to eventual entry into the trivial cycle; then tool_builder can test candidate strengthened descent predicates on all n <= 2^20 against the existing exact oracle, explicitly treating the computation only as a counterexample search, not a proof.
```

```gap
id: G-no-nontrivial-cycle
lemma: The accelerated Collatz map T(n)=n/2 for even n and (3n+1)/2 for odd n has no positive-integer cycle other than the trivial cycle; equivalently, every hypothetical non-trivial cycle is impossible.
status: open
next: theorem_prover: formalise a hypothetical cycle by its K odd members, L even members, and parity/gap data, then prove a complete cycle-exclusion lemma from the Böhm–Sontacchi rational-cycle formula and an effective Diophantine estimate; begin by checking the existing formal bridge and separately state the missing bound on the cycle sum S, since the previous proposed x_min collision has the wrong inequality direction.
```

```gap
id: G-cycle-structural-termination
lemma: If every positive T-orbit is bounded and T has no non-trivial positive cycle, then every positive orbit reaches the trivial cycle and hence the original Collatz orbit reaches 1.
status: discharged
next: Already supplied by elementary finite-state reasoning: formalise in Lean that a bounded orbit in N is eventually periodic, and use the cycle exclusion hypothesis.
```
