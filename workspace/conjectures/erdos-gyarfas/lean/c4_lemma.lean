import Mathlib.Combinatorics.SimpleGraph.Basic
import Mathlib.Combinatorics.SimpleGraph.Paths

open SimpleGraph

/-!
# C4 lemma for Erdős–Gyárfás

This file carries two things:

1. a definition `IsEGConclusion` spelling out exactly what the Erdős–Gyárfás
   conclusion means for a graph `G`, and
2. a **kernel-checked** (no `sorryAx`) lemma that an existing 4-cycle already
   implies that conclusion.

The 4-cycle lemma is the small, sharp step the run's structural work relies on:
any part of an argument that produces a `C4` is already a full win, because
`4 = 2^2` is a power of two. It is intentionally kept minimal and
`sorry`-free.
-/

namespace ErdosGyarfas

variable {V : Type*}

/-- The Erdős–Gyárfás conclusion for a finite simple graph `G`:
there is a closed walk `p` at some vertex `u` which is a *simple cycle*
(`p.IsCycle`) and whose length is `2^k` for some `k : ℕ`.

Conventions (checked against Mathlib):
* `G.Walk u u` is a closed walk in the *simple* graph `G`, i.e. the undirected
  adjacency relation `G.Adj : V → V → Prop`, irreflexive and symmetric.
* `Walk.length` counts **edges**, so a cycle of length `4` is a 4-cycle
  (`4 = 2^2`), not a 5-walk.
* `Walk.IsCycle p` means `p.IsCircuit` (a nonempty trail returning to `u` whose
  only repeated vertex is `u`, appearing twice). This is the usual notion of a
  *simple* cycle.
-/
def IsEGConclusion (G : SimpleGraph V) : Prop :=
  ∃ (k : ℕ) (u : V) (p : G.Walk u u), p.IsCycle ∧ p.length = 2 ^ k

/-- If `G` contains a 4-cycle then it satisfies the Erdős–Gyárfás conclusion:
take `k = 2`, since `4 = 2^2`.  Kernel-checked, no `sorryAx`. -/
theorem c4_implies_conclusion [DecidableEq V]
    (G : SimpleGraph V) [DecidableRel G.Adj]
    (h : ∃ (u : V) (p : G.Walk u u), p.IsCycle ∧ p.length = 4) :
    IsEGConclusion G := by
  rcases h with ⟨u, p, hpcyc, hplen⟩
  refine ⟨2, u, p, hpcyc, ?_⟩
  rw [hplen]
  rfl

end ErdosGyarfas
