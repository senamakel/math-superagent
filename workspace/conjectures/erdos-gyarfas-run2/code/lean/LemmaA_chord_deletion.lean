import Mathlib.Combinatorics.SimpleGraph.Paths
import Mathlib.Combinatorics.SimpleGraph.DeleteEdges
import Mathlib.Combinatorics.SimpleGraph.Finite
import Mathlib.Combinatorics.SimpleGraph.Connectivity.Connected

/-!
# Lemma A — chord deletion preserving 2-connectivity and min-degree ≥ 2

Informal claim (from `research/approaches/edge-deletion-2adic-transfer.md`):

> Every 2-connected finite simple graph `G` with minimum degree ≥ 3 has an edge
> `e = ab` such that `G − e` is 2-connected and `minDegree(G − e) ≥ 2`.

Here "2-connected" is vertex-2-connectivity (the notion Whitney's open-ear
theorem and the reverse-ear deletion use): `G` is connected and deleting any
single vertex leaves it connected. We formalise that as `IsTwoConnected`.

Why it is true (and why the proof is deferred): a graph is *minimally*
2-connected when deleting any edge destroys 2-connectivity. Dirac (1967) proved
that every minimally 2-connected graph has a vertex of degree 2, so if `δ(G) ≥ 3`
then `G` is *not* minimally 2-connected, i.e. some edge `e` has `G − e`
2-connected. The `minDegree(G − e) ≥ 2` part is then immediate: deleting `e`
lowers the degree of only `a` and `b`, from `≥ 3` to `≥ 2`.

We **state** the lemma precisely and mark the proof `sorry`: the existence of the
edge rests on Dirac's theorem, which is not in Mathlib and is the real content.
-/

open SimpleGraph

namespace ErdosGyarfas

variable {V : Type*}

/-- Vertex-2-connectivity: `G` is connected and remains connected after the removal
of any single vertex (i.e. on the induced subgraph of `V \ {v}`). -/
def IsTwoConnected (G : SimpleGraph V) : Prop :=
  G.Connected ∧ ∀ v : V, (G.induce ({v}ᶜ : Set V)).Connected

/--
**Lemma A (stated, proof deferred).** Every 2-connected finite simple graph with
minimum degree at least 3 has an edge `e = ab` whose deletion preserves both
2-connectivity and minimum degree at least 2.
-/
theorem chord_deletion_lemma (G : SimpleGraph V) [Fintype V] [DecidableEq V]
    [DecidableRel G.Adj] (h₂ : IsTwoConnected G) (hδ : 3 ≤ G.minDegree) :
    ∃ a b : V, G.Adj a b ∧
      IsTwoConnected (G.deleteEdges {s(a, b)}) ∧
      2 ≤ (G.deleteEdges {s(a, b)}).minDegree := by
  sorry

end ErdosGyarfas

#print axioms ErdosGyarfas.chord_deletion_lemma
