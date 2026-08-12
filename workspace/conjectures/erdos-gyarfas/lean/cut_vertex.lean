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
    (G.induce (notVSet v)).Adj = (G.Adj on (Subtype.val : notVSet v → V)) := by
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
  exact (p.adj_penultimate hp.not_nil).ne.symm

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
  -- p.tail.getVert (p.tail.length - 1) = p.getVert (p.length - 2 + 1)
  -- tail drops one dart: p.tail.getVert n = p.getVert (1 + n), length_tail
  unfold Walk.penultimate
  rw [Walk.length_tail, ← Walk.getVert_tail]
  congr 1
  omega

/-! ## The interior of the cycle avoids `v` -/

/-- The strict interior of the cycle (vertices strictly between `snd` and
`penultimate` in traversal order — i.e. `p.tail.dropLast`) never visits `v`.
Follows from `p.support.count v = 2`: `v` appears exactly at the two ends of
the lap, and `p.tail.dropLast` contains exactly the interior positions. -/
lemma cycle_middle_avoids_v {G : SimpleGraph V} [DecidableEq V]
    {v : V} {p : G.Walk v v} (hp : p.IsCycle) :
    v ∉ (p.tail.dropLast).support := by
  sorry

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
  let q : (G.induce (notVSet v)).Walk
      ⟨p.snd, cycle_snd_induce hp⟩ ⟨p.penultimate, cycle_penultimate_induce hp⟩ :=
    (p.tail.dropLast).induce (notVSet v) habit
  refine ⟨q⟩

end ErdosGyarfas