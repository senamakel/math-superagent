import Mathlib.Combinatorics.SimpleGraph.Cycle
import Mathlib.Data.Fintype.Basic

open SimpleGraph

-- Erdős–Gyárfás conjecture (finite simple graphs)
theorem erdos_gyarfas_conjecture {V : Type*} [Fintype V] [Nonempty V]
    (G : SimpleGraph V) (hdeg : ∀ v : V, 3 ≤ G.degree v) :
    ∃ v : V, ∃ w : G.Walk v v, w.IsCycle ∧ ∃ k : ℕ, w.length = 2 ^ k := by sorry

#print axioms erdos_gyarfas_conjecture
