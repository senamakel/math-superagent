import Mathlib.Combinatorics.SimpleGraph.Paths
import Mathlib.Combinatorics.SimpleGraph.DeleteEdges

/-!
# Lemma B — cycle-length transfer across a chord deletion

Informal claim (from `research/approaches/edge-deletion-2adic-transfer.md`):

> The set of cycle lengths of `G` equals the cycle lengths of `G − e` union
> `{|P| + 1 : P a simple a–b path in G − e}`, where `e = ab` is an edge of `G`.

This is the equality of sets of natural numbers:
`C(G) = C(G − e) ∪ {|P| + 1 : P a simple a–b path in G − e}`.

The bijection behind it: a cycle of `G` either avoids the edge `e` (hence is a
cycle of `G − e`), or it uses `e`, in which case it is exactly a simple `a–b`
path `P` in `G − e` (the rest of the cycle) closed with the edge `e` back, so
its length is `|P| + 1`.

We **state** this equality precisely and mark the proof `sorry`. The two
inclusions are elementary but each needs a nontrivial walk/length argument
(every cycle through `e` gives a well-defined simple `a–b` path in `G − e`,
and conversely every such path plus `e` is a cycle), which we leave for a
later pass.
-/

open SimpleGraph

namespace ErdosGyarfas

variable {V : Type*}

/-- The set of cycle lengths present in a graph. A value `n` is in `CycleLengths G`
iff `G` has a closed walk `c : G.Walk v v` with `c.IsCycle` and `c.length = n`. -/
def CycleLengths (G : SimpleGraph V) : Set ℕ :=
  { n | ∃ v : V, ∃ c : G.Walk v v, c.IsCycle ∧ c.length = n }

/--
**Lemma B (stated, proof deferred).** Deleting the single edge `e = ab` preserves all
cycle lengths not using `e`, and turns each remaining cycle through `e` into a simple
`a–b` path of `G − e` whose length it exceeds by one:

`C(G) = C(G − e) ∪ { |P| + 1 : P a simple a–b path in G − e }`.
-/
theorem cycle_lengths_transfer {G : SimpleGraph V} {a b : V} (hab : G.Adj a b) :
    CycleLengths G =
      CycleLengths (G.deleteEdges {s(a, b)}) ∪
        { n | ∃ P : (G.deleteEdges {s(a, b)}).Walk a b, P.IsPath ∧ n = P.length + 1 } := by
  sorry

end ErdosGyarfas

#print axioms ErdosGyarfas.cycle_lengths_transfer
