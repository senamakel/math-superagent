# The fold as a read-once branching program: algebraic decision-diagram bounds

```approach
idea: >
  Φ_n is computed by a read-once oblivious branching program of width
  O(popcount) (scan the depth bits, maintain the running XOR over the
  downset). The weight wt(Φ_n h) is then a statistic of a deterministic
  finite automaton reading the reflected prime residue string. The
  Nisan–Wigderson / algebraic branching program lower-bound machinery gives
  the exact communication-complexity of a function from its branching
  program structure; applied to Φ it yields a lower bound on wt(Φ_n h) for
  ANY input h of given statistical complexity, with the complexity
  hypothesis priced not as "h is complicated" but as the prime string being
  incompressible for read-once partitions. The closed doors are avoided
  because the hypothesis is about Φ's own read-once decomposition, not
  about h's weight/runs/aperiodicity.
mechanism: >
  Named machinery: read-once branching programs, Nisan's PRAM/communication
  lower bounds, and the algebraic (Nisan–Wigderson) determinantal
  complexity of the fold. The fold matrix Φ_n is exactly the class of
  matrices of the form M[x,y] = [y ⊆ x] (the submask/partition matrix),
  whose rank over F_2 is full (n-2, proved) but whose communication
  complexity over the {0,1} evaluation is governed by the log-rank and
  discrepancy of the partition. This is NOT the refuted
  f2-gram-disjointness-spectrum (Gram spectrum) and NOT the refuted
  gowers-u2-nilsequence (basis mismatch): it uses communication/discrepancy
  lower bounds for deterministic evaluation of a fixed string, a different
  engine from coding theory and from Walsh-uniformity.
status: proposed
first-step: >
  tool_builder, exact F_2 arithmetic. (1) Write Φ_n as a read-once branching
  program and verify its output equals the submask-XOR oracle for n <= 64.
  (2) Compute the deterministic communication complexity / partition
  discrepancy of Φ_n directly and compare to the Nisan lower bound. (3) For
  the prime h, price the statistical-complexity input needed: state the
  precise incompressibility hypothesis and test whether it is strictly
  weaker than positive switch density. FALSIFIER: if the branching program
  width or communication complexity is trivial (O(1) or Θ(log n)), the
  route gives no weight lower bound.
falsifies: >
  (a) the read-once decomposition is wrong against the oracle; (b) the
  communication complexity of Φ_n is Θ(n) (no discrepancy structure to
  exploit); (c) the incompressibility hypothesis on the prime string is
  equivalent to or stronger than positive mod-4 switch density.
```
