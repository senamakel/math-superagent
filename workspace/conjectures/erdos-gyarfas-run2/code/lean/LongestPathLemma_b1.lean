import Mathlib.Combinatorics.SimpleGraph.Paths

/-!
# The longest-path lemma, part (b1)

For a longest path `p : G.Walk u v` (so every path has length `≤ p.length`),
every neighbour of the endpoint `u` lies on the path's support.

Proof: if a neighbour `w` of `u` were not on `p`, then prepending the edge
`w - u` to `p` would give a strictly longer path, contradicting maximality.
-/

open SimpleGraph

namespace ErdosGyarfas

variable {V : Type*} {G : SimpleGraph V} {u v w : V}

/-- Every neighbour of the start vertex of a longest path lies on the path. -/
theorem neighbor_of_longest_path_vertices_is_on_path {p : G.Walk u v}
    (hp : p.IsPath) (hmax : ∀ ⦃a b : V⦄ (q : G.Walk a b), q.IsPath → q.length ≤ p.length)
    (hw : G.Adj u w) : w ∈ p.support := by
  by_contra hnot
  -- `w - u - … - v` is a path one step longer than `p`.
  have hlong : (Walk.cons hw.symm p).IsPath := by
    rw [Walk.cons_isPath_iff]
    exact ⟨hp, hnot⟩
  have hlen := hmax (q := Walk.cons hw.symm p) hlong
  have : ¬ p.length + 1 ≤ p.length := by omega
  exact this hlen

end ErdosGyarfas

#print axioms ErdosGyarfas.neighbor_of_longest_path_vertices_is_on_path
