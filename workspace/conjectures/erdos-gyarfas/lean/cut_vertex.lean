import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Combinatorics.SimpleGraph.Paths
import Mathlib.Combinatorics.SimpleGraph.Connectivity.Connected
import Mathlib.Combinatorics.SimpleGraph.Walk.Decomp
import Mathlib.Combinatorics.SimpleGraph.Walk.Traversal
import Mathlib.Data.List.Nodup

/-!
# The cut-vertex lemma, formalised

This file formalises the geometric core of the run's **cut-vertex structure
lemma** for a hypothetical Erdős–Gyárfás minimal counterexample.

## The informal claim

> Let `G` be a simple graph and `v : V` a vertex. Every simple cycle of `G`
> that passes through `v` has all of its other vertices inside a *single*
> connected component of `G - v` (the graph `G` with `v` deleted).

The geometric reason: a simple cycle through `v` leaves `v` along one edge,
wanders, and returns to `v` along *another* edge (a simple cycle cannot use
`v` as a hairpin). The part of the cycle strictly between those two
neighbours is a path that never meets `v`, so it is a walk in `G` on the
vertex set `{x | x ≠ v}` — i.e. a path inside the graph `G - v`. Its two
endpoints, being on that path, lie in a single connected component of `G - v`.

## The faithful formalisation

`G - v` is the graph on the vertex set `{x | x ≠ v}` with adjacency inherited
from `G`, which is exactly Mathlib's `G.induce {x | x ≠ v}` (see
`induce_not_v`). "Two vertices lie in a single connected component of `G - v`"
is `(G.induce {x | x ≠ v}).Reachable a b`.

The theorem proven **kernel-checked, no `sorry`** is:

```lean
cycle_in_one_component :
    (G.induce (notVSet v)).Reachable
      ⟨p.snd, cycle_snd_induce hp⟩ ⟨p.penultimate, cycle_penultimate_induce hp⟩
```

That is: for a simple cycle `p` through `v`, its two `v`-neighbours (the
vertex the cycle visits right after leaving `v`, `p.snd`, and the vertex it
returns through, `p.penultimate`) are connected by a walk in `G - v` — so the
whole cycle's vertices other than `v` lie in one component of `G - v`. This is
exactly the geometric content of the cut-vertex lemma.

## Why this is the right statement (and not a different one)

* `p.snd ≠ p.penultimate` (`cycle_second_ne_last`): `v` is not a hairpin, so
  the cycle passes through `v` with two distinct incident edges. This is
  Mathlib's own `IsCycle.snd_ne_penultimate`.
* `cycle_snd_ne_v` / `cycle_penultimate_ne_v`: the two neighbours are not `v`
  itself, so they are genuine vertices of `G - v` (each follows from
  `adj_snd`/`adj_penultimate` plus irreflexivity of `G.Adj`).
* The walk connecting them is the cycle's own interior segment,
  `p.tail.dropLast`, lifted into `G.induce (notVSet v)` via `Walk.induce`.
  This lift is legal because **every vertex of the interior is `≠ v`** — that
  is `cycle_middle_avoids_v`, proven from the fact that `p.tail` is a path
  ending at `v`, so `v` occurs exactly once in `p.tail.support`, namely as its
  last element, and hence not in `p.tail.support.dropLast`.
* `tail_penultimate` connects the penultimate of the interior segment to the
  penultimate of the whole cycle (they differ only in the accumulated `cons`).

## Convention notes

* `p : G.Walk v v` closed; `p.IsCycle` = simple cycle (nonempty trail, only
  repeated vertex is the start `v`). `p.length` counts edges; `p.support` is
  the vertex list in traversal order; `p.snd = p.support[1]`;
  `p.penultimate = p.support[p.length - 1]`.
* A cycle reaching `v` twice means `p.support` contains `v` at positions `0`
  and `p.length`; the distinctness that drives the hairpin argument lives in
  `p.support.dropLast` (which is `Nodup`), *not* in `p.support` itself. This
  is why the API is expressed via `p.tail` and `dropLast`.
-/

open SimpleGraph

namespace ErdosGyarfas

variable {V : Type*}

/-- `notVSet v` is the vertex set of `G - v`: all vertices except `v`. -/
abbrev notVSet (v : V) : Set V := {x : V | x ≠ v}

/-- `G.induce (notVSet v)` has exactly the edges of `G` between vertices
distinct from `v`, i.e. it *is* the graph-theoretic `G - v`. -/
theorem induce_not_v {G : SimpleGraph V} (v : V) :
    (G.induce (notVSet v)).Adj = (fun a b : notVSet v => G.Adj a.1 b.1) := by
  funext a b
  rfl

/-! ## Neighbours of `v` on the cycle -/

/-- The second vertex of a simple cycle through `v` is not `v` itself. -/
lemma cycle_snd_ne_v {G : SimpleGraph V} {v : V} {p : G.Walk v v}
    (hp : p.IsCycle) : p.snd ≠ v := by
  exact (p.adj_snd hp.not_nil).ne'

/-- The penultimate (return) vertex of a simple cycle through `v` is not `v`
itself. -/
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
  rw [Nat.sub_add_cancel hl]

/-! ## The interior of the cycle avoids `v` -/

/-- The strict interior of the cycle (vertices strictly between `snd` and
`penultimate` in traversal order — i.e. `p.tail.dropLast`) never visits `v`.

Proof: `p.tail` is a path (`IsCycle.isPath_tail`), so its vertices are all
distinct; its last vertex is `v` (it ends where the cycle returns to `v`).
Hence `v` occurs exactly once in `p.tail.support`, namely as the last element,
so it is absent from `p.tail.support.dropLast = (p.tail.dropLast).support`. -/
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
    have hlen0 : (p.tail).length = 0 := hnil.length_eq_zero
    rw [Walk.length_tail] at hlen0
    have h3 : 3 ≤ p.length := hp.three_le_length
    omega
  -- support of the interior = tail.support.dropLast
  have hsupp : (p.tail.dropLast).support = (p.tail.support).dropLast := by
    rw [Walk.support_dropLast htnil]
  intro hv
  have hv' : v ∈ (p.tail.support).dropLast := by rwa [hsupp] at hv
  -- tail.support = dropLast ++ [v]  (v is the last element of the support)
  have hne : (p.tail.support) ≠ [] := List.ne_nil_of_mem hmem
  have hlast' : (p.tail.support).getLast hne = v := by
    exact p.tail.getLast_support
  have hsplit : (p.tail.support).dropLast ++ [v] = (p.tail.support) := by
    have hg : (p.tail.support).dropLast ++ [(p.tail.support).getLast hne] = (p.tail.support) :=
      List.dropLast_append_getLast hne
    simp [hlast']
  have hcount2 : 2 ≤ (p.tail.support).count v := by
    rw [← hsplit]
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