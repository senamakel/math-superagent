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

/-- The start vertex `u` of a longest path is not on the subpath strictly beyond position 0,
as long as the subpath starts at a positive position. -/
lemma subpathPos_not_mem_start {i : ℕ} (hi : 1 ≤ i) (hi_le : i ≤ p.length)
    (hp : p.IsPath) : u ∉ (subpathPos p 0 i (Nat.zero_le i)).support := by
  intro hmem
  -- subpathPos p 0 i is the prefix of p up to position i
  let q := subpathPos p 0 i (Nat.zero_le i)
  -- every vertex on q is `p.getVert j` for some `0 ≤ j ≤ i`
  have hmem' : ∀ x, x ∈ q.support → x ≠ u := by
    intro x hx
    rw [Walk.mem_support_iff_exists_getVert] at hx
    rcases hx with ⟨j, hj, hjl⟩
    -- j = position of x along p; q.getVert j = p.getVert j
    have : x = p.getVert j := by
      -- q is the prefix so q.getVert j = p.getVert j
      dsimp [q, subpathPos]
      sorry
    -- if x = u = p.getVert 0 then j = 0, contradiction with i ≥ 1 ... handled below
    rw [this] at hj
    -- need: p.getVert j = u = p.getVert 0 implies j = 0 (injectivity), then j<i impossible
    sorry
  exact hmem' u hmem rfl

end ErdosGyarfas
