# Approach: dependency-graph-leaf-classification

```approach
idea: Every leaf of the odd dependency graph of a UPN is a prime power p^e for
  which p^e + 1 is a power of 2 (all its odd prime factors have been eliminated
  "upstream"). The equation p^e + 1 = 2^k with e ≤ 3 (cubefree) and p odd is a
  Catalan-type exponential Diophantine equation. Mihăilescu's theorem (Catalan's
  conjecture) classifies consecutive powers: 2^3 + 1 = 9 = 3^2 is the only
  non-trivial solution with both exponents > 1. Together with the Mersenne prime
  classification (e = 1: p = 2^k−1, p prime ⇒ p is Mersenne), the entire leaf
  set of any UPN dependency graph is rigidly constrained. Combined with the 2-adic
  budget identity (sum of v2 across all nodes = a+1) and the graph's branching
  rules (each non-leaf node p^e introduces new primes from p^e+1, whose combined
  2-adic weight must respect the budget), this forces a finite classification of
  possible dependency-graph shapes, and hence an absolute bound on a. This is NOT
  the closed higgs-depth-bound approach (which tried to bound the depth of the
  3-Higgs Pratt tree and was refuted because P_3 is infinite). The key difference:
  the dependency graph here is the ACTUAL graph of a UPN, not the ambient 3-Higgs
  Pratt tree. The nodes are the specific prime powers dividing n, and the edges
  are the specific divisibilities q | p^e+1 that the balance equation forces.
  This graph is finite for any given n, and its leaves satisfy the strong
  Catalan constraint. The infinitude of P_3 does not refute this: a UPN only uses
  finitely many 3-Higgs primes, and the question is whether the constraints at
  the leaves propagate upward to force a finite total.
mechanism: Let D be the directed graph whose vertices are the odd prime-power
  components p_i^{e_i} of a UPN n = 2^a·∏ p_i^{e_i}, with an edge from v to w
  if the prime of w divides v+1 (the "augmented" value p_i^{e_i}+1). Let L be
  the set of leaves (vertices with out-degree 0, after removing the even-part
  node 2^a, which has special status). For each leaf ℓ = p^e, all odd prime
  divisors of p^e+1 must have been accounted for by other vertices or are
  powers of 2. Since the graph is finite and no odd prime can be "unaccounted"
  (the balance is exact), every odd prime factor of p^e+1 either corresponds to
  an existing vertex or is ruled out by the budget constraints. This forces
  p^e+1 = 2^k·(product of primes already in the graph). For a leaf that is
  minimal (no incoming edges from below), p^e+1 must be a pure power of 2:
  p^e+1 = 2^k. By Mihăilescu (Catalan), the only solution with e > 1 and k > 1
  is 2^3+1 = 3^2. For e = 1, p = 2^k−1 must be a Mersenne prime. The known
  Mersenne primes give a finite set of possible leaf primes at this first layer.
  Inductively, each layer receives its "budget" of 2-adic valuations from the
  layer above, and the Catalan constraint limits the branching. Since the total
  2-adic budget is a+1 (from the budget identity), the tree height and width are
  bounded by a function of a. If a were unbounded, the tree could grow
  arbitrarily large, but the leaf constraints force the tree to be built from a
  limited alphabet of "atomic" prime components, giving an absolute bound on
  the tree size and hence on a.
status: proposed
first-step: (1) Derive the exact condition for a vertex p^e to be a leaf in the
  dependency graph: all odd prime factors q of p^e+1 must correspond to vertices
  in the graph, and the "excess" must be a power of 2. (2) Classify all
  solutions to p^e+1 = 2^k with p odd prime, 1 ≤ e ≤ 3, k ≥ 2 using
  Mihăilescu's theorem and elementary modular constraints (p^3+1 = (p+1)(p^2−p+1),
  both factors powers of 2 ⇒ very restrictive). (3) Verify the leaf
  classification against the five known UPNs: for n=6 (leaf 3: 3+1=4=2^2 ✓),
  n=90 (leaf 5: 5+1=6=2·3, so leaf set depends on graph direction), and the
  fifth example's leaves. Do not record the approach as checked until all five
  match.
```