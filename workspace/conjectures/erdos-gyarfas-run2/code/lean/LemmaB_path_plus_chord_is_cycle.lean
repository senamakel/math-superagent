import Mathlib.Combinatorics.SimpleGraph.Paths
import Mathlib.Combinatorics.SimpleGraph.DeleteEdges

/-!
# Lemma B — one direction, proved: every a–b path in G − e closes with e to a cycle of G

This file proves the easy inclusion of the Lemma B identity
`C(G) = C(G − e) ∪ {|P| + 1 : P a simple a–b path in G − e}`, namely

> for `hab : G.Adj a b`, every simple path `P` from `a` to `b` in `G.deleteEdges {s(a,b)}`
> gives, by prepending the closing edge `b – a`, a cycle of `G` of length `|P| + 1`.

Proof: map the walk `P` from `G − e` up to `G` (a walk of a subgraph is a walk of the
supergraph, `Walk.mapLe`), prepend the edge `hab.symm : G.Adj b a`, and apply
`Walk.cons_isCycle_iff`: the result is a cycle iff `P` is a path and the closing edge
`s(b,a)` is not among the edges of `P`. The latter holds because every edge of a walk
of `G − e` satisfies `s(x,y) ∉ {s(a,b)}` (from `deleteEdges_adj`), and `s(b,a) = s(a,b)`
(`Sym2.eq_swap`).

The reverse inclusion (a cycle of G not using e is a cycle of G − e; a cycle of G using
e splits at a and b into a simple a–b path of G − e) is NOT proved here; it is stated
as `sorry` in `LemmaB_cycle_lengths_transfer.lean`. See VERIFICATION_REPORT.md.
-/

open SimpleGraph

namespace ErdosGyarfas

variable {V : Type*}

/-- The set of cycle lengths present in a graph. A value `n` is in `CycleLengths G`
iff `G` has a closed walk `c : G.Walk v v` with `c.IsCycle` and `c.length = n`. -/
def CycleLengths (G : SimpleGraph V) : Set ℕ :=
  { n | ∃ v : V, ∃ c : G.Walk v v, c.IsCycle ∧ c.length = n }

/--
**Lemma B, one direction (proved).** If `P` is a simple `a–b` path in `G − e` with
`e = s(a,b)`, then `G` has a cycle of length `|P| + 1`: the path `P` closed by the
edge `b – a`.
-/
theorem cycle_lengths_transfer_subset {G : SimpleGraph V} {a b : V}
    (hab : G.Adj a b)
    (P : (G.deleteEdges {s(a, b)}).Walk a b)
    (hP : P.IsPath) :
    CycleLengths G (P.length + 1) := by
  -- the closed walk at b: closing edge b – a, then the a–b path P mapped up to G
  let c : G.Walk b b := Walk.cons hab.symm (P.mapLe (deleteEdges_le {s(a, b)}))
  refine ⟨b, c, ?_, ?_⟩
  · -- c is a cycle: P is a path and the closing edge s(b,a) is not an edge of P
    rw [Walk.cons_isCycle_iff]
    constructor
    · exact hP.mapLe (deleteEdges_le {s(a, b)})
    · -- every edge of a walk of G − e avoids s(a,b); and s(b,a) = s(a,b)
      rw [Walk.edges_mapLe_eq_edges]
      intro hmem
      have hadj : (G.deleteEdges {s(a, b)}).Adj b a := Walk.adj_of_mem_edges P hmem
      have hb : s(b, a) ∉ ({s(a, b)} : Set (Sym2 V)) := (deleteEdges_adj.mp hadj).2
      exact hb (by simp [Sym2.eq_swap])
  · -- length: c = edge + P, so |c| = |P| + 1
    simp [c]

#print axioms ErdosGyarfas.cycle_lengths_transfer_subset

end ErdosGyarfas
