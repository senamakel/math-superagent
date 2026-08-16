import Mathlib.Combinatorics.SimpleGraph.Finite
import Mathlib.Combinatorics.SimpleGraph.Paths

/-!
# The Erdős–Gyárfás conjecture — formal statement

> Every finite simple graph with minimum degree at least 3 contains a cycle
> whose length is a power of two (with exponent `k ≥ 2`, so length 4, 8, 16, …).

Formalisation conventions:

* `IsPowerOfTwoLen n` : there is `k ≥ 2` with `n = 2^k`.  The `k ≥ 2` clause
  matches the reference formalisation in `formal-conjectures` (Erdős Problem 64)
  and excludes the vacuous lengths 1 and 2.
* A "cycle" is a `SimpleGraph.Walk v v` satisfying `Walk.IsCycle`.
* `G.minDegree ≥ 3` is Mathlib's minimum-degree notation.

We do **not** prove this theorem (it is open); it is stated with `sorry`.
-/

open SimpleGraph

namespace ErdosGyarfas

/-- A natural is a power of two with exponent at least 2. -/
def IsPowerOfTwoLen (n : ℕ) : Prop :=
  ∃ k : ℕ, 2 ≤ k ∧ n = 2 ^ k

/-- A walk-based cycle. `c : G.Walk v v` and `c.IsCycle`. -/
def HasPowerOfTwoCycle (G : SimpleGraph V) : Prop :=
  ∃ v : V, ∃ c : G.Walk v v, c.IsCycle ∧ IsPowerOfTwoLen c.length

/--
**The Erdős–Gyárfás conjecture.** Every finite simple graph with minimum
degree at least 3 contains a cycle whose length is a power of two (k ≥ 2).

Stated, not proved — this is an open conjecture.
-/
theorem erdos_gyarfas_conjecture (G : SimpleGraph V) [Fintype V]
    [DecidableRel G.Adj] (hδ : 3 ≤ G.minDegree) :
    HasPowerOfTwoCycle G := by
  sorry

end ErdosGyarfas

#print axioms ErdosGyarfas.erdos_gyarfas_conjecture
