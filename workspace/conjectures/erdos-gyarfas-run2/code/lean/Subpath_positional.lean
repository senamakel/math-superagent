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

/-- Every vertex of the subwalk between positions `ia ≤ ib` (with `ib ≤ p.length`) is
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
  · have := subpathPos_getVert p hle hnle
    -- x = (subpathPos p ia ib hle).getVert n = p.getVert (ia+n)
    rw [← this] at hn
    exact hn.symm
where
  subpathPos_getVert {p : G.Walk u v} {ia ib n : ℕ} (hle : ia ≤ ib) (hn : n ≤ ib - ia) :
      (subpathPos p ia ib hle).getVert n = p.getVert (ia + n) := by
    dsimp [subpathPos]
    rw [Walk.getVert_copy]
    have hmin : n ⊓ (ib - ia) = n := Nat.min_eq_left hn
    rw [Walk.take_getVert, Walk.drop_getVert]
    congr
    omega

#print axioms ErdosGyarfas.subpathPos_mem_is_getVert
