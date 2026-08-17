import Mathlib.Combinatorics.SimpleGraph.StronglyRegular
import Mathlib.Data.Fintype.Card

/-!
# Conway's 99-graph problem — statement node

The open conjecture (`problem.md`): does there exist an undirected graph on 99
vertices in which every edge lies in a unique triangle and every non-adjacent
pair lies in a unique 4-cycle?

As the run's restatement uses everywhere, the two conditions force regularity
and the object is *exactly* a strongly regular graph with parameters
`(99, 14, 1, 2)`:

  * "every edge in a unique triangle" = `λ = 1` (adjacent pairs have exactly one
    common neighbour);
  * "every non-adjacent pair in a unique 4-cycle" = `μ = 2` (non-adjacent pairs
    have exactly two common neighbours);
  * `v = 99`, and the counting relation `k(k−2) = 2(v−k−1)` then forces `k = 14`.

Mathlib already has the object `SimpleGraph.IsSRGWith n k λ μ` (a structure
bundling the cardinality, regularity, and the two common-neighbour conditions),
so the conjecture is a single existential over an abstract finite vertex type.

The file carries **statements only**, ending in `:= by sorry`. It is not a
proof of existence: the problem is open and this run does not claim it. What the
`sorry` marks is precisely "this proposition is not yet established", which is
the honest reading of the node.
-/

namespace Conway99

/-- The Conway 99-graph problem, in the strong-regular restatement the run uses
everywhere: does there exist a strongly regular graph with parameters
`(99, 14, 1, 2)`?

This is the central proposition of the whole run.  It remains an OPEN conjecture
— no construction and no nonexistence proof is known — so the body is exactly
`sorry`, and the `sorry` is the statement of that openness, not a proof attempt.
-/
theorem conway_99_srg_exists :
    ∃ (V : Type) (_ : Fintype V) (G : SimpleGraph V) (_ : DecidableRel G.Adj),
      @SimpleGraph.IsSRGWith V _ G _ 99 14 1 2 := by
  sorry

/-- Conway's own phrasing, before the restatement: a simple graph on 99 vertices
in which every edge is in a unique triangle (the `λ = 1` condition) and every
non-adjacent pair has exactly two common neighbours (the `μ = 2` condition, i.e.
lies in a unique 4-cycle).

This is definitionally the same family of objects as `conway_99_srg_exists`
once regularity is forced; stated here so the node carries the original wording
of the problem alongside the SRG restatement.  (Regularity and `k = 14` are
forced by these two conditions together with `v = 99`, through the identity
`k(k−2) = 2(v−k−1)`.)
-/
def ConwayFamily (V : Type) [Fintype V] (G : SimpleGraph V) [DecidableRel G.Adj] : Prop :=
  Fintype.card V = 99 ∧
    (∀ v w : V, G.Adj v w → Fintype.card (G.commonNeighbors v w) = 1) ∧
    (∀ v w : V, v ≠ w → ¬ G.Adj v w → Fintype.card (G.commonNeighbors v w) = 2)

/-- The `v = 99`, `λ = 1`, `μ = 2` portion of the counting derivation: the number
of 2-paths out of a degree-`k` vertex is `k(k−1)`, of which one lands back on the
vertex (parameter `λ = 1` triangle) and the remaining `k(k−2)` land on the
`v−k−1` non-neighbours, each reached `μ = 2` times, giving
`k(k−2) = 2(v−k−1)`.

(Stated, not proved: `:= by sorry`.  This is the identity that turns `v = 99`
into `k = 14`; a proof would be the "derive rather than import" step the
problem calls for.)
-/
theorem counting_identity (v k : ℕ) (hpos : 0 < k) :
    k * (k - 1 - 1) = 2 * (v - k - 1) → v = 1 + k + k * (k - 2) / 2 := by
  sorry

/-- The concrete numerical output of the counting derivation: with `v = 99`, the
relation forces `k = 14`.  (Stated, not proved.)
-/
theorem v99_forces_k14 (k : ℕ) :
    k * (k - 1 - 1) = 2 * (99 - k - 1) → k = 14 := by
  sorry

#check Conway99.conway_99_srg_exists
#check Conway99.ConwayFamily
#check Conway99.counting_identity
#check Conway99.v99_forces_k14

#print axioms Conway99.conway_99_srg_exists
#print axioms Conway99.counting_identity
#print axioms Conway99.v99_forces_k14

end Conway99
