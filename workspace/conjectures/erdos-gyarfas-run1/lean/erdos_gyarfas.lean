import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Combinatorics.SimpleGraph.Walk.Basic
import Mathlib.Combinatorics.SimpleGraph.Finite
import Mathlib.Combinatorics.SimpleGraph.Paths

/-!
# The Erdős–Gyárfás conjecture — formal statement

**Informal claim.** Every finite simple graph with minimum degree at least 3
contains a cycle whose length is a power of two.

The formulated statement below asserts the existence of `k ≥ 2` and a closed
walk `p : G.Walk v v` at some vertex `v` which is a cycle (`p.IsCycle`) and
whose length (`p.length`, counting edges) is exactly `2 ^ k`.

## Conventions, checked

* `G.degree v` is the number of neighbours of `v`; `G.minDegree` is the
  minimum over all vertices, defined as `0` on the empty vertex type. The
  hypothesis `3 ≤ G.minDegree` therefore rules the empty graph out (there
  `minDegree = 0`), so `∃ v` below is inhabited — this is why the leading
  `∃ (v : V)` is well-formed rather than vacuous on an empty type.
* `G.Walk v v` is a walk from `v` to itself. `p.IsCycle` is the Mathlib
  predicate (`IsCycle` in `SimpleGraph.Walk` / `Paths.lean`): `p` is a
  nontrivial trail whose support has no repeated vertex except its start/end.
  In particular `p.IsCycle` already rules out the length-0 and length-1 walks
  (a loop), so any witness is a genuine cycle of length at least 3.
* `p.length` counts *edges* (`length_nil = 0`, `length_cons = p.length + 1`),
  matching the graph-theoretic convention that a 4-cycle has length 4.
* `2 ^ k` is ℕ-valued PowerNat exponentiation, `2 ≤ k` forces the length to
  be a power of two with exponent at least 2 (i.e. length a multiple of 4).

The only divergence from the informal claim worth flagging: the informal
conjecture usually states "a power of two" without the `2 ≤ k` clause. Since a
power of two `2^k` with `k ≥ 2` is still a power of two, this statement is
*stronger* (asks for the exponent to be at least 2). This matches the run's
memorised formulation of the problem and the task prompt, which both request
`k ≥ 2`.
-/
theorem erdos_gyarfas {V : Type*} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj] (hmin : 3 ≤ G.minDegree) :
    ∃ (k : ℕ) (v : V) (p : G.Walk v v),
      p.IsCycle ∧ p.length = 2 ^ k ∧ 2 ≤ k := by
  sorry

#print axioms erdos_gyarfas
