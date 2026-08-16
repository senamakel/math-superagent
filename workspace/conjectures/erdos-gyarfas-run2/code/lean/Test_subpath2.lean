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
  classical
  -- `(p.drop ia).take (ib - ia)` is a subwalk of `p`, hence a path.
  have hsub : ((p.drop ia).take (ib - ia)).IsSubwalk p :=
    ((p.drop ia).isSubwalk_take _).trans (p.isSubwalk_drop _)
  have hpath : ((p.drop ia).take (ib - ia)).IsPath :=
    Walk.isPath_of_isSubwalk hsub hp
  -- clean up the `copy` by showing IsPath is invariant under `copy`
  simpa using (Walk.isPath_copy ((p.drop ia).take (ib - ia)) rfl rfl).mpr hpath

end ErdosGyarfas
