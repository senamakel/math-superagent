import Mathlib.Combinatorics.SimpleGraph.Paths

/-!
# Lemma b, single neighbour: a cycle of length `i + 1` from a neighbour at position `i`

For a path `p : G.Walk u v` and a neighbour `w = p.getVert i` of the start
vertex `u` lying at position `i ≥ 2` on the path, the subpath `u → w` plus the
closing edge `w — u` is a cycle at `u` of length `i + 1`.

The hypothesis is `2 ≤ i` (not `1 ≤ i` as in the original `Lemma_b_single.lean`):
for `i = 1` the subpath is the single edge `u — p.getVert 1` and closing it
gives the degenerate walk `u — w — u`, which repeats `u` and is not a cycle.
The original statement with `1 ≤ i` is **false** (take a path of length ≥ 1 and
the neighbour at position 1).

The subpath machinery (`subpathPos` and its positional lemmas) is inlined here
so the file is self-contained; it is the same content as `Subpath.lean`.
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

/-- The subpath of `p` between positions `ia ≤ ib` is a path when `p` is a path. -/
lemma subpathPos_isPath {ia ib : ℕ} (hle : ia ≤ ib) (hp : p.IsPath) :
    (subpathPos p ia ib hle).IsPath := by
  dsimp [subpathPos]
  have hsub : ((p.drop ia).take (ib - ia)).IsSubwalk p :=
    ((p.drop ia).isSubwalk_take _).trans (p.isSubwalk_drop _)
  have hpath : ((p.drop ia).take (ib - ia)).IsPath :=
    Walk.isPath_of_isSubwalk hsub hp
  simpa using (Walk.isPath_copy ((p.drop ia).take (ib - ia)) rfl rfl).mpr hpath

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

/-- For a longest path `p : G.Walk u v` and a neighbour `w` of the start vertex `u` lying
at position `i` on the path (i.e. `w = p.getVert i`), with `2 ≤ i`, there is a cycle at
`u` of length `i + 1`: go along the subpath `u → w`, then take the closing edge `w - u`. -/
theorem cycle_from_neighbor {i : ℕ} (hi : 2 ≤ i) (hi_le : i ≤ p.length)
    (hp : p.IsPath) (hw : G.Adj u (p.getVert i)) :
    ∃ (v : V) (c : G.Walk v v), c.IsCycle ∧ c.length = i + 1 := by
  -- the subpath u → p.getVert i, coerced to start at u
  let sub : G.Walk u (p.getVert i) :=
    (subpathPos p 0 i (Nat.zero_le i)).copy p.getVert_zero rfl
  -- cycle at u: subpath u→w followed by closing edge w-u
  let c : G.Walk u u := sub.concat hw.symm
  refine ⟨u, c, ?_, ?_⟩
  · dsimp [c]
    rw [Walk.concat_eq_append]
    refine Walk.IsPath.isCycle_append (p := sub) (q := (hw.symm.toWalk : G.Walk (p.getVert i) u)) ?_ ?_ ?_ ?_
    · -- sub.IsPath
      dsimp [sub]
      rw [Walk.isPath_copy]
      exact subpathPos_isPath (Nat.zero_le i) hp
    · simpa using (hw.symm).isPath_toWalk
    · -- sub.support.tail Disjoint (hw.symm.toWalk).support.tail = [u]
      have hu_not : u ∉ sub.support.tail := by
        dsimp [sub]
        rw [Walk.support_copy]
        have hsub_supp : (subpathPos p 0 i (Nat.zero_le i)).support = p.support.take (i + 1) :=
          subpathPos_support hi_le
        rw [hsub_supp]
        have hu_not_p : u ∉ p.support.tail := by
          rw [Walk.isPath_def] at hp
          exact List.Nodup.notMem (by simpa [List.cons_eq_cons] using hp)
        rw [← Walk.cons_tail_support p]
        rw [List.take_cons (by omega : 0 < i + 1)]
        simp only [List.tail_cons]
        exact fun h => hu_not_p (List.mem_of_mem_take h)
      have hq_tail : (hw.symm.toWalk : G.Walk (p.getVert i) u).support.tail = [u] := by
        rw [Adj.support_toWalk]
        simp
      rw [hq_tail]
      rw [List.disjoint_comm]
      simp [List.disjoint_left, hu_not]
    · left
      have hlen : sub.length = i := by
        dsimp [sub]
        rw [Walk.length_copy]
        simpa [subpathPos_length (Nat.zero_le i) hi_le]
      omega
  · dsimp [c, sub]
    rw [Walk.length_concat, Walk.length_copy]
    simp [subpathPos_length (Nat.zero_le i) hi_le]

#print axioms ErdosGyarfas.cycle_from_neighbor

end ErdosGyarfas
