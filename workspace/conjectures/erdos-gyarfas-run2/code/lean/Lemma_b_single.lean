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

/-- Core positional identity: the vertex at position `n` of the subpath is the vertex
at position `ia + n` of `p`, for `n ≤ ib - ia`. -/
lemma subpathPos_getVert {ia ib n : ℕ} (hle : ia ≤ ib) (hn : n ≤ ib - ia) :
    (subpathPos p ia ib hle).getVert n = p.getVert (ia + n) := by
  dsimp [subpathPos]
  rw [Walk.getVert_copy]
  have hmin : n ⊓ (ib - ia) = n := Nat.min_eq_left hn
  rw [Walk.take_getVert, Walk.drop_getVert]
  congr
  omega

/-- Every vertex of the subpath between positions `ia ≤ ib` (with `ib ≤ p.length`) is
`p.getVert j` for some `ia ≤ j ≤ ib`. -/
lemma subpathPos_mem_is_getVert {ia ib : ℕ} (hle : ia ≤ ib) (hib : ib ≤ p.length)
    (hp : p.IsPath) {x : V} (hx : x ∈ (subpathPos p ia ib hle).support) :
    ∃ j : ℕ, ia ≤ j ∧ j ≤ ib ∧ p.getVert j = x := by
  rw [Walk.mem_support_iff_exists_getVert] at hx
  rcases hx with ⟨n, hn, hnl⟩
  have hnle : n ≤ ib - ia := by
    have : (subpathPos p ia ib hle).length ≤ ib - ia := by
      simpa [subpathPos_length hle hib]
    omega
  refine ⟨ia + n, by omega, ?_, ?_⟩
  · omega
  · have := subpathPos_getVert (p := p) hle hnle
    rw [← this] at hn
    exact hn.symm

#print axioms ErdosGyarfas.subpathPos_mem_is_getVert

/-- For a longest path `p : G.Walk u v` and a neighbour `w` of the start vertex `u` lying
at position `i` on the path (i.e. `w = p.getVert i`), there is a cycle at `u` of length
`i + 1`: go along the subpath `u → w`, then take the closing edge `w - u`. -/
theorem cycle_from_neighbor {i : ℕ} (hi : 1 ≤ i) (hi_le : i ≤ p.length)
    (hp : p.IsPath) (hw : G.Adj u (p.getVert i)) :
    ∃ (v : V) (c : G.Walk v v), c.IsCycle ∧ c.length = i + 1 := by
  let w := p.getVert i
  let sub : G.Walk u w := subpathPos p 0 i (Nat.zero_le i)
  -- cycle at u: subpath u→w followed by closing edge w-u
  let c : G.Walk u u := sub.concat hw.symm
  refine ⟨u, c, ?_, ?_⟩
  · -- c is a cycle because sub is a path whose support avoids u (beyond position 0) and
    -- hw.symm's edge isn't in sub
    dsimp [c]
    -- prepend edge w-u: c = cons (hw.symm... wait sub.concat hw.symm = sub ++ cons hw.symm nil
    -- it's easier to use concat_isPath + edges
    sorry
  · dsimp [c, w, sub]
    rw [Walk.length_concat, subpathPos_length (Nat.zero_le i) hi_le]
    simp

#print axioms ErdosGyarfas.cycle_from_neighbor
