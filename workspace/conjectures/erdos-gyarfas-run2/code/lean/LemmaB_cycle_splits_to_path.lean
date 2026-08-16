import Mathlib.Combinatorics.SimpleGraph.Paths
import Mathlib.Combinatorics.SimpleGraph.DeleteEdges
import Mathlib.Combinatorics.SimpleGraph.Walk.Decomp

/-!
# Lemma B, hard direction: a cycle of G through e = ab gives a simple a–b path in G − e

Informal claim: if `c : G.Walk v v` is a cycle of `G` that uses the edge
`e = s(a,b)` (i.e. `s(a,b) ∈ c.edges`), then the cycle, cut at the occurrence of
`e`, gives a simple path from `a` to `b` in `G.deleteEdges {s(a,b)}` whose length
is `|c| − 1`.

This is the missing inclusion of `cycle_lengths_transfer` in
`LemmaB_cycle_lengths_transfer.lean`. It is NOT yet proved here — the structure of
the proof is to rotate the cycle so that it starts with the edge `b – a`, observe
that the rotated cycle is `cons (b–a) P` with `P` a path from `a` to `b` whose
edges are exactly the edges of `c` minus `s(a,b)`, and then `transfer` `P` down to
`G.deleteEdges {s(a,b)}`.

We state the intermediate lemmas and mark the proof `sorry` — see VERIFICATION_REPORT.md.
-/

open SimpleGraph

namespace ErdosGyarfas

variable {V : Type*}

/-- The set of cycle lengths present in a graph. A value `n` is in `CycleLengths G`
iff `G` has a closed walk `c : G.Walk v v` with `c.IsCycle` and `c.length = n`. -/
def CycleLengths (G : SimpleGraph V) : Set ℕ :=
  { n | ∃ v : V, ∃ c : G.Walk v v, c.IsCycle ∧ c.length = n }

/-- **Lemma B, hard direction (stated, proof `sorry`).** A cycle of G using the edge
`e = s(a,b)` splits at that edge into a simple `a–b` path of `G − e` of length one less. -/
theorem cycle_using_edge_splits_to_path {G : SimpleGraph V} {a b v : V}
    (hab : G.Adj a b) (c : G.Walk v v) (hc : c.IsCycle)
    (huse : s(a, b) ∈ c.edges) :
    ∃ P : (G.deleteEdges {s(a, b)}).Walk a b,
      P.IsPath ∧ P.length = c.length - 1 := by
  sorry

/-- **Lemma B, other inclusion (stated, proof `sorry`).** Every cycle length of G is
either a cycle length of G − e or one more than the length of a simple a–b path of
G − e.  Equivalently `CycleLengths G ⊆ CycleLengths (G − e) ∪ {|P|+1 : P an a–b path}`. -/
theorem cycle_lengths_transfer_subset_cycle {G : SimpleGraph V} {a b : V}
    (hab : G.Adj a b) {n : ℕ} (hn : CycleLengths G n) :
    CycleLengths (G.deleteEdges {s(a, b)}) n ∨
      ∃ P : (G.deleteEdges {s(a, b)}).Walk a b, P.IsPath ∧ n = P.length + 1 := by
  sorry

#print axioms ErdosGyarfas.cycle_using_edge_splits_to_path
#print axioms ErdosGyarfas.cycle_lengths_transfer_subset_cycle

end ErdosGyarfas
