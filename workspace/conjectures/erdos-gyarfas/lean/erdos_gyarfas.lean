import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Combinatorics.SimpleGraph.Paths
import c4_lemma

open SimpleGraph

/-!
# The Erdős–Gyárfás conjecture, stated in Lean

**Conjecture (Erdős and Gyárfás, 1995).** Every finite simple graph with
minimum degree at least 3 contains a cycle whose length is a power of two
(`2^k` for some `k ≥ 2`, i.e. `4, 8, 16, …`).

## What the formal statement says, and how it could diverge

* `G : SimpleGraph V` on a finite type `V` is a *simple* graph: an irreflexive
  symmetric adjacency relation `G.Adj : V → V → Prop`. This is Mathlib's
  `SimpleGraph`; there are no loops and no multiple edges, exactly the
  conjectured setting.
* `3 ≤ G.minDegree` is the minimum-degree hypothesis. `minDegree` is defined
  over `Fintype V`, and on a degenerate (empty) vertex type it returns `0`, so
  the hypothesis is simply false there and the implication is vacuous — the
  statement asserts nothing wrong about empty graphs.
* The conclusion `ErdosGyarfas.IsEGConclusion G` (imported from
  `c4_lemma.lean`) asks for a closed walk `p : G.Walk u u` with
  `p.IsCycle ∧ p.length = 2^k`. `Walk.length` counts **edges**, so `k = 2`
  means a genuine 4-cycle. `IsCycle` demands a nonempty trail whose only
  repeated vertex is the start — a simple cycle.

The statement is:

    ∃ k, ∃ u, ∃ p : G.Walk u u, p.IsCycle ∧ p.length = 2^k

which is exactly the conjecture's conclusion. This file is the formal statement
only; there is no proof, the theorem body is `by sorry`.
-/

namespace ErdosGyarfas

/-- **Erdős–Gyárfás conjecture.** Every finite simple graph with minimum
degree at least 3 contains a cycle whose length is a power of two.

Unproved — the body is `by sorry`. Formalising the statement is the deliverable;
there is no proof to formalise yet. -/
theorem erdos_gyarfas {V : Type*} [Fintype V] [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj] (h : 3 ≤ G.minDegree) :
    IsEGConclusion G := by
  sorry

end ErdosGyarfas
