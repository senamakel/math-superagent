import Mathlib.Combinatorics.SimpleGraph.Paths

/-!
# Subpath positional lemmas — shared library

`subpathPos p ia ib hle` is the subwalk of `p` from position `ia` to position
`ib` (dart indices).  This file collects the positional identities used by the
longest-path lemmas:

* `subpathPos_length` — its length is `ib - ia`;
* `subpathPos_getVert` — its vertex at position `n` is `p.getVert (ia + n)`;
* `subpathPos_isPath` — a subpath of a path is a path;
* `subpathPos_mem_is_getVert` — every vertex on the subpath is `p.getVert j`
  for some `ia ≤ j ≤ ib`;
* `subpathPos_support` — the support of the prefix-subpath is exactly the
  prefix of `p.support`;
-/

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

lemma subpathPos_getVert {ia ib n : ℕ} (hle : ia ≤ ib) (hn : n ≤ ib - ia) :
    (subpathPos p ia ib hle).getVert n = p.getVert (ia + n) := by
  dsimp [subpathPos]
  rw [Walk.getVert_copy]
  have hmin : n ⊓ (ib - ia) = n := Nat.min_eq_left hn
  rw [Walk.take_getVert, Walk.drop_getVert]
  congr
  omega

/-- The subpath of `p` between positions `ia ≤ ib` is a path when `p` is a path. -/
lemma subpathPos_isPath {ia ib : ℕ} (hle : ia ≤ ib) (hp : p.IsPath) :
    (subpathPos p ia ib hle).IsPath := by
  dsimp [subpathPos]
  have hsub : ((p.drop ia).take (ib - ia)).IsSubwalk p :=
    ((p.drop ia).isSubwalk_take _).trans (p.isSubwalk_drop _)
  have hpath : ((p.drop ia).take (ib - ia)).IsPath :=
    Walk.isPath_of_isSubwalk hsub hp
  simpa using (Walk.isPath_copy ((p.drop ia).take (ib - ia)) rfl rfl).mpr hpath

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
    rw [this] at hn
    exact hn

/-- The support of the prefix subpath `subpathPos p 0 i` is the prefix of length
`i + 1` of `p.support`. -/
lemma subpathPos_support {i : ℕ} (hi : i ≤ p.length) :
    (subpathPos p 0 i (Nat.zero_le i)).support = p.support.take (i + 1) := by
  dsimp [subpathPos]
  rw [Walk.support_copy]
  have htake : ((p.drop 0).take i).support = p.support.take (i + 1) := by
    rw [Walk.support_take]
    simp
  exact htake

end ErdosGyarfas
