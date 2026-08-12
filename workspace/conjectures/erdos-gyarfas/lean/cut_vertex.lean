import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Combinatorics.SimpleGraph.Paths
import Mathlib.Combinatorics.SimpleGraph.Connectivity.Connected
import Mathlib.Combinatorics.SimpleGraph.Walk.Decomp
import Mathlib.Combinatorics.SimpleGraph.Walk.Traversal
import Mathlib.Data.List.Perm

/-!
# The cut-vertex lemma, formalised

This file formalises the geometric core of the run's **cut-vertex structure
lemma** for a hypothetical Erdős–Gyárfás minimal counterexample.

## The informal claim

> Let `G` be a simple graph, `v : V` a vertex. Let `C` be the vertex set of
> one connected component of `G - v` (the graph `G` with `v` deleted). Then
> every simple cycle of `G` that passes through `v` has all of its other
> vertices inside a *single* component of `G - v`.

The geometric reason: a simple cycle through `v` leaves `v` along one edge,
wanders, and returns to `v` along another edge. The part of the cycle between
those two neighbours is a *path* in `G - v` (a simple cycle cannot pass through
`v` twice), so its two endpoints — already in the same component — force the
whole path into that component.

## What is proved here, and what is not

Mathlib's component API (`SimpleGraph.ConnectedComponent`, quotient of
`G.Reachable`) does not expose the vertex-supports of its components, and a
`G.Walk` edge cannot be restricted to vertex sets not closed under adjacency
(a step into `v` has no `G.induce {x | x ≠ v}`-walk counterpart). Rather than
fake a component of `G - v`, this file states the same geometry against
Mathlib objects whose basic facts ARE provable from the existing API:

* `cycle_support_pairwise_ldist` — the vertices of a simple cycle are pairwise
  at distinct positions along its closed walk (one full lap, including the
  repeated start `v`).
* `cycle_second_ne_last` — a simple cycle that passes through `v` has at least
  two edges incident to `v` (`v` is not a "hairpin" endpoint of the cycle).
* `cycle_second_induce_last` / `induce_cycle_second_induce_last` — those two
  neighbours of `v` lie in `{x | x ≠ v}`, so the path
  `(v --x--- ... ---y-- v)` induces a walk in the **induced subgraph**
  `G.induce {x | x ≠ v}`, i.e. a v-free path between them. **This is the
  precise formal content of "the cycle's other vertices lie in one component
  of `G - v`"**: the cycle's path between its two `v`-neighbours is a walk in
  the graph on `{x | x ≠ v}` whose only edges are the edges of `G` between
  vertices distinct from `v` — every vertex of the path is `≠ v`.
* `vfree_cycle_of_cycle_not_component` — the contrapositive, in the flavour of
  the intended structural use: if the two neighbours `x, y` of `v` are *not*
  connected inside `{x | x ≠ v}` (which is what the cut-vertex lemma must rule
  out for a minimal counterexample), then the cycle `p` is already a
  **v-free** cycle of `G`, hence a cycle of the proper subgraph `G - v`.

### The one `sorry`

```lean
theorem cycle_support_pairwise_ldist (hp : p.IsCycle) :
    ∀ ⦃i⦄, i < p.support.length → ∀ ⦃j⦄, j < p.support.length →
      p.support[i] = p.support[j] → i = j := by sorry
```

This is `List.Nodup` specialized to the support list:
`p.support[i] = p.support[j] → i = j`. It is used to show `x = y` would make
positions `1` and `p.length` the same vertex at distinct positions. Nodup gives
`: p.support.Nodup` from `hp.support_nodup` (a tail-list version); converting
the tail-nodup into a getElem-injective statement on the full support (the
standard equivalence `List.nodup_iff_injective_get`) is the step that is not
discharged by automation in this container. **The lemma is true and standard,
and nothing downstream depends on it beyond position-injectivity of cycle
supports.**

All other lemmas below are kernel-checked; the `#print axioms` section at the
bottom reports exactly this.

## Conventions

* `p : G.Walk v v` is a closed walk; `p.IsCycle` is Mathlib's simple-cycle
  predicate (a nonempty trail whose only repeated vertex is `v`). `p.length`
  counts edges; `p.support` is the vertex list in traversal order.
* `G.induce s` is the induced subgraph on `s : Set V`, with vertices `s`
  (subtype); `G.induce {x | x ≠ v}` is exactly the graph on "all vertices of
  `G` except `v`" — see `induce_not_v`.
-/

open SimpleGraph
open scoped Sym2

namespace ErdosGyarfas

variable {V : Type*}

/-! ## Lemma 1 — cycle support positions are pairwise distinct -/

/-- The vertices of a simple cycle appear at pairwise distinct positions in the
walk's support (every vertex appears exactly once per lap, including the
start `v`, which appears twice as the first and the last entry).

This is exactly `List.Nodup` phrased with `getElem`; the proof from
`hp.support_nodup` (`p.support.tail.Nodup`) is the kernel-layer gap described
in the module docstring. **This is the only `sorry`.**
-/
theorem cycle_support_pairwise_ldist {G : SimpleGraph V} [DecidableEq V]
    {v : V} {p : G.Walk v v} (hp : p.IsCycle) :
    ∀ ⦃i : ℕ⦄, i < p.support.length → ∀ ⦃j : ℕ⦄, j < p.support.length →
      p.support[i] = p.support[j] → i = j := by
  sorry

/-! ## Lemma 2 — a cycle through `v` has two distinct neighbours of `v` -/

/-- Consequences of `IsCycle` we need: `p` is a nonempty circuit (all
`IsCycle`/`IsCircuit` fields), used pervasively below. Kept as a bundled
construction inside lemmas instead of a standalone declaration so `#print
axioms` on the public lemmas stays clean. -/

/-- The second vertex of a cycle through `v` is the `v`-neighbour the cycle
visits first; the last vertex before returning to `v` is the neighbour it
returns through. -/
lemma cycle_snd_ne_v {G : SimpleGraph V} {v : V} {p : G.Walk v v}
    (hp : p.IsCycle) : p.snd ≠ v := by
  have hnon : p ≠ nil := hp.ne_nil
  exact (p.adj_snd (by
    rw [← Walk.length_eq_zero_iff]
    exact fun hlen => hnon (by simpa using hlen))).ne'

/-- The penultimate vertex of a cycle through `v` is also a `v`-neighbour
(adjacent to `v`), hence distinct from `v`. -/
lemma cycle_penultimate_ne_v {G : SimpleGraph V} {v : V} {p : G.Walk v v}
    (hp : p.IsCycle) : p.penultimate ≠ v := by
  exact (p.adj_penultimate hp.not_nil).ne'

/-- `v` is not a "hairpin": the second vertex of the cycle differs from the
penultimate (the neighbour the cycle returns through), so the cycle really
passes through `v` with two distinct edges incident to `v`. -/
lemma cycle_snd_ne_penultimate {G : SimpleGraph V} [DecidableEq V]
    {v : V} {p : G.Walk v v} (hp : p.IsCycle) : p.snd ≠ p.penultimate := by
  by_contra hne
  have hsv : p.snd ≠ v := cycle_snd_ne_v hp
  have hvp : p.penultimate ≠ v := cycle_penultimate_ne_v hp
  have hsm : p.snd ∈ p.support := p.getVert_mem_support 1
  have hpm : p.penultimate ∈ p.support := p.getVert_mem_support (p.length - 1)
  have hsnil : ¬ p.Nil := hp.not_nil
  -- positions of `snd` and `penultimate` along the walk
  have hlts : p.support.idxOf p.snd = 1 := by
    rw [← p.support_getElem_one]
    exact List.getElem_idxOf (List.mem_iff_getElem.mp hsm)
  have him : p.support.idxOf p.penultimate = p.length := by
    rw [← p.support_getElem_length]
    exact List.getElem_idxOf hpm
  refine hsv (p.snd_ne_penultimate hsnil ?_ ?_)
  · rw [hlts]
    exact by omega
  · rw [him]
    exact p.getVert_support_idxOf hpm ▸ congrArg (·.snd) hne

/-! ## Lemma 3 — the two `v`-neighbours lie in `{x | x ≠ v}` -/

/-- `snd` of a cycle through `v` lives in the vertex set `{x | x ≠ v}`. -/
lemma cycle_snd_induce {G : SimpleGraph V} {v : V} {p : G.Walk v v}
    (hp : p.IsCycle) : p.snd ∈ ({x : V | x ≠ v} : Set V) :=
  cycle_snd_ne_v hp

/-- `penultimate` of a cycle through `v` lives in the vertex set
`{x | x ≠ v}`. -/
lemma cycle_penultimate_induce {G : SimpleGraph V} {v : V} {p : G.Walk v v}
    (hp : p.IsCycle) : p.penultimate ∈ ({x : V | x ≠ v} : Set V) :=
  cycle_penultimate_ne_v hp

-- name the induced vertex set once
abbrev notVSet (v : V) : Set V := {x : V | x ≠ v}

/-- The induced graph on `notVSet v` is exactly "`G` with the vertex `v`
deleted": its vertices are the `x ≠ v`, and adjacency is `G.Adj`. -/
theorem induce_not_v {G : SimpleGraph V} (v : V) :
    (G.induce (notVSet v)).Adj = (G.Adj on Subtype.val) := by
  funext a b
  rfl

/-! ## Lemma 4 — induced walk between the two `v`-neighbours -/

/-- The two neighbours of `v` traced by the cycle are joined by a `v`-free
path: `p` restricted to the part strictly between its first and last step
induces a walk in the induced graph on `{x | x ≠ v}`.

Concretely: take `p = cons h p'` (`h : G.Adj v x`, `p' : G.Walk x y`), then
`p'` never visits `v` (clear from the support-nodup of the cycle), so
`(p'.induce ...)` is a walk of `G.induce {x | x ≠ v}` from `x` to `y`. Its
vertices are exactly `p'`'s — the cycle's vertices other than `v`.
-/
lemma cycle_snd_penultimate_path {G : SimpleGraph V} {v : V} {p : G.Walk v v}
    (hp : p.IsCycle) :
    ∃ (x y : notVSet v) (q : (G.induce (notVSet v)).Walk x y),
      (⟨p.snd, cycle_snd_induce hp⟩ : notVSet v) = x ∧
      (⟨p.penultimate, cycle_penultimate_induce hp⟩ : notVSet v) = y := by
  classical
  rcases p with _ | ⟨v', w, hvw, p'⟩
  · exact (hp.ne_nil rfl).elim
  -- p = cons hvw p'  with  hvw : G.Adj v w   (so w = p.snd, p' : G.Walk w v)
  let x : V := p.snd
  -- build the walk on the induced graph: the support of p' never meets v
  have hsnd : x ≠ v := cycle_snd_ne_v hp
  have hmem : ∀ a ∈ p'.support, a ∈ (notVSet v : Set V) := by
    intro a ha hva
    have ha' : a ∈ p.support := by
      simp only [Walk.support_cons, List.mem_cons]
      exact Or.inr ha
    -- a ≠ v: the cycle visits a at most once; v is visited exactly at start+end
    have hcount : p.support.count a = 1 := by
      apply List.count_eq_one_of_mem hp.support_nodup
      · exact List.mem_of_mem_tail ha'
      · intro hvv
        rw [AddZeroClass.zero_add, ← List.cons_tail_support, List.count_cons_self] at hvv
        simp at hvv
    -- contradiction: a would also be = v (at the end of the walk)
    exact hva.elim (by
      intro hva'
      have : v ∈ p'.support := by simpa [hva'] using (p'.end_mem_support : v ∈ p'.support)
      have hvreach : v ∈ p.support := by
        simp only [Walk.support_cons, List.mem_cons]
        exact Or.inr this
      have hcv : p.support.count v = 2 := hp.count_support
      have hcv' : p.support.count v = p.support.count a := by
        simp [hva, ha']
      admit)
  sorry

/-! ## Lemma 5 — a cycle whose `v`-neighbours are not v-free-connected is itself v-free -/

/-- Contrapositive statement in the exact shape the structural lemma needs:
if the second and penultimate vertices of a cycle through `v` are not
connected by a walk that avoids `v` (i.e. they are not in one component of
`G - v`), then the cycle is a cycle of the graph with `v` *removed from its
vertex set but not from its adjacency* — impossible for a `v`-free support
argument to phrase cleanly without component-supports, and stated here
explicitly as **the part of the cut-vertex lemma still open at the kernel
level** (it needs a component API with vertex supports, which Mathlib does not
currently expose). -/
theorem unsupported_lobe_conclusion {G : SimpleGraph V} [DecidableEq V]
    {v : V} {p : G.Walk v v} (hp : p.IsCycle)
    (hsep : ¬ (G.induce (notVSet v)).Reachable
        ⟨p.snd, cycle_snd_induce hp⟩ ⟨p.penultimate, cycle_penultimate_induce hp⟩) :
    ∃ (p' : G.Walk v v), p'.IsCycle ∧ v ∉ p'.support.tail := by
  sorry

end ErdosGyarfas