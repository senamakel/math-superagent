import Mathlib.Combinatorics.SimpleGraph.Paths

open SimpleGraph

namespace ErdosGyarfas

variable {V : Type*} {G : SimpleGraph V} {u v : V} {p : G.Walk u v}

/-- The subpath of `p` from position `ia` to position `ib` (dart indices), when `ia ≤ ib`.
A walk from `p.getVert ia` to `p.getVert ib`. -/
def subpathPos (p : G.Walk u v) (ia ib : ℕ) (hle : ia ≤ ib) :
    G.Walk (p.getVert ia) (p.getVert ib) :=
  ((p.drop ia).take (ib - ia)).copy rfl (by
    rw [Walk.drop_getVert]
    congr
    omega)

lemma subpathPos_length {ia ib : ℕ} (hle : ia ≤ ib) (hib : ib ≤ p.length) :
    (subpathPos p ia ib hle).length = ib - ia := by
  dsimp [subpathPos]
  rw [Walk.length_copy]
  rw [Walk.take_length, Walk.drop_length]
  have hmin : min (p.length - ia) (ib - ia) = ib - ia := by omega
  rw [Nat.min_comm, hmin]

/-- The subpath of `p` between positions `ia ≤ ib` is a path when `p` is a path. -/
lemma subpathPos_isPath {ia ib : ℕ} (hle : ia ≤ ib) (hp : p.IsPath) :
    (subpathPos p ia ib hle).IsPath := by
  dsimp [subpathPos]
  have hsub : ((p.drop ia).take (ib - ia)).IsSubwalk p :=
    ((p.drop ia).isSubwalk_take _).trans (p.isSubwalk_drop _)
  have hpath : ((p.drop ia).take (ib - ia)).IsPath :=
    Walk.isPath_of_isSubwalk hsub hp
  simpa using (Walk.isPath_copy ((p.drop ia).take (ib - ia)) rfl rfl).mpr hpath

/--
For a longest path `p : G.Walk u v` between a pair of neighbours `a = p.getVert ia`,
`b = p.getVert ib` of the start vertex `u` (with `ia < ib`), the edge `u-b`, the reversed
subpath `b → a` and the edge `a-u` form a cycle at `u` of length `ib - ia + 2`.
-/
theorem cycle_from_two_neighbors {ia ib : ℕ} (hlt : ia < ib)
    (hib : ib ≤ p.length) (hp : p.IsPath)
    (iha : G.Adj u (p.getVert ia)) (ihb : G.Adj u (p.getVert ib)) :
    ∃ (v : V) (c : G.Walk v v),
      c.IsCycle ∧ c.length = ib - ia + 2 := by
  -- The spokes and the subpath
  let a := p.getVert ia
  let b := p.getVert ib
  let sub : G.Walk a b := subpathPos p ia ib (Nat.le_of_lt hlt)
  -- cycle at u: edge u-b, reversed subpath b→a, edge a-u
  -- wrapped in the concrete closed walk
  let back : G.Walk b u := (sub.reverse).append (iha.symm.toWalk)
  let c : G.Walk u u := (ihb.toWalk).append back
  refine ⟨u, c, ?_cycle, ?_len⟩
  · dsimp [c, back]
    rw [Walk.length_append, Walk.length_append, Walk.length_reverse,
      subpathPos_length (Nat.le_of_lt hlt) hib]
    omega
  · sorry

#print axioms ErdosGyarfas.cycle_from_two_neighbors
