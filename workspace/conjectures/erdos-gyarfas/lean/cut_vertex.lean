import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Combinatorics.SimpleGraph.Paths
import Mathlib.Combinatorics.SimpleGraph.Connectivity.Connected
import Mathlib.Combinatorics.SimpleGraph.Walk.Decomp
import Mathlib.Combinatorics.SimpleGraph.Walk.Traversal
import Mathlib.Data.List.Nodup

/-!
# The cut-vertex lemma, formalised

See the module docstring goals in `README` context: this is the geometric heart
of the run's cut-vertex structure lemma. `G - v` is modelled as the induced
subgraph on `{x | x ≠ v}`.

**Statement proved kernel-checked** (`cycle_in_one_component`): for a simple
cycle `p : G.Walk v v` of `G` through `v`, the two `v`-neighbours on the cycle
(`p.snd`, visited right after leaving `v`, and `p.penultimate`, returned
through) are connected by a walk inside `G - v` — i.e. they lie in a single
connected component of `G - v`, so all vertices of `p` other than `v` do.
-/

open SimpleGraph

namespace ErdosGyarfas

variable {V : Type*}

/-- `notVSet v` = vertex set of `G - v`: all vertices except `v`. -/
abbrev notVSet (v : V) : Set V := {x : V | x ≠ v}

/-- `G.induce (notVSet v)` has exactly the edges of `G` between vertices
distinct from `v`: it is graph-theoretic `G - v`. -/
theorem induce_not_v {G : SimpleGraph V} (v : V) :
    (G.induce (notVSet v)).Adj = (fun a b : notVSet v => G.Adj a.1 b.1) := by
  funext a b
  rfl

/-! ## Neighbours of `v` on the cycle -/

/-- The second vertex of a simple cycle through `v`: adjacent to `v`. -/
lemma cycle_snd_ne_v {G : SimpleGraph V} {v : V} {p : G.Walk v v}
    (hp : p.IsCycle) : p.snd ≠ v := by
  exact (p.adj_snd hp.not_nil).ne'

/-- The penultimate (return) vertex of a simple cycle through `v`:
adjacent to `v`. -/
lemma cycle_penultimate_ne_v {G : SimpleGraph V} {v : V} {p : G.Walk v v}
    (hp : p.IsCycle) : p.penultimate ≠ v := by
  exact (p.adj_penultimate hp.not_nil).ne

/-- The two neighbours are distinct (v is not a hairpin) — Mathlib's own
`IsCycle.snd_ne_penultimate`. -/
lemma cycle_second_ne_last {G : SimpleGraph V} {v : V} {p : G.Walk v v}
    (hp : p.IsCycle) : p.snd ≠ p.penultimate := hp.snd_ne_penultimate

/-- `p.snd` is a vertex of `G - v`. -/
lemma cycle_snd_induce {G : SimpleGraph V} {v : V} {p : G.Walk v v}
    (hp : p.IsCycle) : p.snd ∈ notVSet v := cycle_snd_ne_v hp

/-- `p.penultimate` is a vertex of `G - v`. -/
lemma cycle_penultimate_induce {G : SimpleGraph V} {v : V} {p : G.Walk v v}
    (hp : p.IsCycle) : p.penultimate ∈ notVSet v := cycle_penultimate_ne_v hp

/-- The penultimate of a closed walk's tail is the penultimate of the walk
itself. -/
lemma tail_penultimate {G : SimpleGraph V} {v : V} {p : G.Walk v v}
    (hp : p.IsCycle) : p.tail.penultimate = p.penultimate := by
  unfold Walk.penultimate
  rw [Walk.length_tail, Walk.getVert_tail]
  have h2 : 2 ≤ p.length := by have := hp.three_le_length; omega
  have hl : 1 ≤ p.length - 1 := by omega
  have hsub : p.length - 1 - 1 + 1 = p.length - 1 := by
    rw [Nat.sub_add_cancel hl]
    omega
  rw [hsub]
/-! ## The interior of the cycle avoids `v` -/

/-- The strict interior of the cycle (vertices strictly between `snd` and
`penultimate` in traversal order — i.e. `p.tail.dropLast`) never visits `v`.

Proof: `p.tail` is a path (`IsCycle.isPath_tail`), whose vertices are all
distinct and whose last vertex is `v`. Hence `v` occurs exactly once in
`p.tail.support`, namely as the last element, so it is absent from
`p.tail.support.dropLast = (p.tail.dropLast).support`. -/
lemma cycle_middle_avoids_v {G : SimpleGraph V} [DecidableEq V]
    {v : V} {p : G.Walk v v} (hp : p.IsCycle) :
    v ∉ (p.tail.dropLast).support := by
  classical
  -- p.tail is a path: distinct vertices, ending at v
  have hpath : p.tail.IsPath := hp.isPath_tail
  have hnd : (p.tail.support).Nodup := hpath.support_nodup
  have hmem : v ∈ (p.tail).support := (p.tail.end_mem_support : v ∈ p.tail.support)
  have hcount : (p.tail.support).count v = 1 := List.count_eq_one_of_mem hnd hmem
  -- p.tail is nonempty (its length is p.length - 1 ≥ 2)
  have htnil : ¬ (p.tail).Nil := by
    intro hnil
    have : (p.tail).length = 0 := hnil.length_eq_zero
    have : p.length = 1 := by
      rw [Walk.length_tail] at this
      omega
    have h3 : 3 ≤ p.length := hp.three_le_length
    omega
  -- support of the interior = tail.support.dropLast ; last element of tail.support is v
  have hsupp : (p.tail.dropLast).support = (p.tail.support).dropLast := by
    rw [Walk.support_dropLast htnil]
  intro hv
  have hv' : v ∈ (p.tail.support).dropLast := by rwa [hsupp] at hv
  -- tail.support = dropLast ++ [v]
  have hlast : (p.tail.support).getLast (by simp [List.ne_nil_of_mem hmem]) = v := by
    -- last element of the support of a walk is its endpoint, which is v
    simpa using (p.tail.getLast_support)
  have hsplit : (p.tail.support) = (p.tail.support).dropLast ++ [v] := by
    rw [← List.dropLast_append_getLast (by simp [List.ne_nil_of_mem hmem])]
    simp [hlast]
  have hcount2 : 2 ≤ (p.tail.support).count v := by
    rw [hsplit]
    rw [List.count_append, List.count_cons_self]
    have : 1 ≤ (p.tail.support).dropLast.count v := List.count_pos_iff.mpr hv'
    omega
  omega

/-! ## Main theorem -/

/-- **Cut-vertex lemma (geometric heart).** A simple cycle through `v` has its
two `v`-neighbours connected inside `G - v`; hence all its vertices other than
`v` lie in a single connected component of `G - v`. -/
theorem cycle_in_one_component {G : SimpleGraph V} [DecidableEq V]
    {v : V} {p : G.Walk v v} (hp : p.IsCycle) :
    (G.induce (notVSet v)).Reachable
      ⟨p.snd, cycle_snd_induce hp⟩ ⟨p.penultimate, cycle_penultimate_induce hp⟩ := by
  classical
  -- interior never visits v
  have hmiddle : v ∉ (p.tail.dropLast).support := cycle_middle_avoids_v hp
  -- so every vertex of the interior lies in notVSet v
  have habit : ∀ x ∈ (p.tail.dropLast).support, x ∈ (notVSet v : Set V) := by
    intro x hx hxv
    exact hmiddle (by simpa [hxv] using hx)
  -- p.tail goes snd -> v, so p.tail.dropLast goes snd -> penultimate of p
  have hpen : p.tail.penultimate = p.penultimate := tail_penultimate hp
  refine ⟨(p.tail.dropLast).induce (notVSet v) habit |>.copy ?_ ?_⟩
  · ext
    rfl
  · ext
    exact hpen

end ErdosGyarfas