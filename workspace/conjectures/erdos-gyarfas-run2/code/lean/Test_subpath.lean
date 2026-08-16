import Mathlib.Combinatorics.SimpleGraph.Paths

open SimpleGraph

namespace ErdosGyarfas

variable {V : Type*} {G : SimpleGraph V} {u v : V} {p : G.Walk u v}

/-- The subpath of `p` from position `ia` to position `ib` (dart indices), when `ia ≤ ib`. -/
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

end ErdosGyarfas
