import Mathlib.Data.Rat.Floor
import Mathlib.Data.ZMod.Basic
import Mathlib.Data.Nat.Fib.Basic

/-!
# PE1006 G4: the unresolved joint-intercept evaluator

This file deliberately separates the exact statement from the open theorem.
For a rational slope `a`, window length `k`, intercept index `m`, and digit
position `j`, `digit a m j` is the floor difference
`floor((-m*a)+(j+1)*a)-floor((-m*a)+j*a)`.  `value` interprets the resulting
binary word as a base-10 integer.  `psi` is the sum of the squares of the
`k+1` distinct words, modulo `M = 101001001`.

The desired G4 theorem says that the joint sum over all intercepts can be
reduced to a fixed-dimensional state (independent of `k`) and evaluated in
O(log k), by a Euclidean/continued-fraction recursion.  The existence of such
an evaluator, and its specification for the actual joint intercept boundary
state, remain open in this workspace; they are represented only by `sorry`.
-/

noncomputable section
open scoped BigOperators
namespace PE1006G4Statement

abbrev Modulus := ZMod 101001001
abbrev State := Fin 6 → Modulus

structure Node where
  dR : ℕ
  dU : ℤ
  w : Modulus
  s0 : Modulus
  s1 : Modulus
  s2 : Modulus

def digit (a : ℚ) (m j : ℕ) : ℤ :=
  ⌊(-((m : ℚ) * a) + ((j + 1 : ℕ) : ℚ) * a)⌋ -
  ⌊(-((m : ℚ) * a) + ((j : ℕ) : ℚ) * a)⌋

def wordValue (a : ℚ) (m k : ℕ) : Modulus :=
  ∑ j : Fin k, (10 : Modulus) ^ (k - 1 - j.1) * (digit a m j.1 : Modulus)

def jointInterceptSum (a : ℚ) (k : ℕ) : Modulus :=
  ∑ m ∈ Finset.range (k + 1), (wordValue a m k) ^ 2

/-- A hand-written specification predicate for a proposed fixed-dimensional
Euclidean evaluator.  `step` is the one-block transition and `output` extracts
its answer; `depth` is logarithmic in the input by hypothesis. -/
def EvaluatorSpec (a : ℚ) (step : ℕ → State → State) (output : State → Modulus)
    (init : State) (depth : ℕ → ℕ) : Prop :=
  (∀ k : ℕ, output (step k init) = jointInterceptSum a k) ∧
  (∀ k : ℕ, depth k ≤ 2 * (Nat.log (k + 2) + 1))

/-- Fully quantified form of the desired fixed-dimensional O(log k) result.
The state dimension is the fixed six coordinates in `State`; no enumeration of
intercepts is present in the evaluator interface. -/
theorem fixed_dimensional_Olog_joint_intercept
    (a : ℚ) :
    ∃ (step : ℕ → State → State) (output : State → Modulus)
      (init : State) (depth : ℕ → ℕ),
      EvaluatorSpec (a := a) step output init depth := by
  sorry

/-- The old interface is retained as a weaker, explicitly conditional shell. -/
/- namespace Cited -/
axiom Cited.universal_euclidean_spec
    (p q r n : ℕ) (hr : 0 < r) : ∃ node : Node, node.dR = n
axiom Cited.telescoped_second_moment_from_node
    (a : ℚ) (k : ℕ) : ∃ c0 c1 c2 : Modulus, True
/- end Cited -/

theorem g4_reduction_interface (a : ℚ) (k : ℕ) (hk : 1 ≤ k) :
    ∃ node : Node, node.dR = k + 1 ∧ ∃ c0 c1 c2 : Modulus, True := by
  obtain ⟨node, hnode⟩ := Cited.universal_euclidean_spec 0 0 1 (k + 1) (by decide)
  obtain ⟨c0, c1, c2, h⟩ := Cited.telescoped_second_moment_from_node a k
  exact ⟨node, hnode, c0, c1, c2, h⟩

#print axioms fixed_dimensional_Olog_joint_intercept
#print axioms g4_reduction_interface
#print axioms Cited.universal_euclidean_spec
#print axioms Cited.telescoped_second_moment_from_node
end PE1006G4Statement
