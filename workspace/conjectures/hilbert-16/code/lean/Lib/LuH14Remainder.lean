/-
Precise analytic remainder target for Lu's H^3_14 displacement function.
The statement isolates the unformalised analytic step: after extracting the
finite Bautin polynomial part, the displacement has a uniformly controlled
remainder on a fixed collar.  No claim about the numerical value of the bound
is made here.
-/
import Mathlib.Analysis.SpecialFunctions.Pow.Real
import Mathlib.Topology.MetricSpace.Bounded

namespace LuH14

abbrev Plane := ℝ × ℝ

/-- A displacement function on a parameter box and radial collar. -/
def Displacement (D : Plane → ℝ) (p : ℝ × ℝ) (r : ℝ) : ℝ := D (p.1, p.2 + r)

/--
Analytic remainder lemma being attacked.  `R` is the remainder after the
finite Bautin truncation `Σ i < m, c i p r^i`.  The hypotheses explicitly say:
* the parameter set `K` is compact;
* `D` and every coefficient `c i` are continuous;
* the remainder identity holds on the collar;
* the remainder is uniformly bounded by `C r^m`.
This is a statement, not a proof of Lu's theorem: the key analytic estimate is
left as `sorry`.
-/
theorem analytic_remainder_bound
    (K : Set (ℝ × ℝ)) (D : (ℝ × ℝ) → ℝ)
    (c : ℕ → (ℝ × ℝ) → ℝ) (R : ℕ → (ℝ × ℝ) → ℝ → ℝ)
    (m : ℕ) (r₀ C : ℝ)
    (hK : IsCompact K)
    (hr₀ : 0 < r₀)
    (hD : Continuous D)
    (hc : ∀ i : ℕ, Continuous (c i))
    (hidentity : ∀ p ∈ K, ∀ r : ℝ, 0 ≤ r → r ≤ r₀ →
      D p = (∑ i ∈ Finset.range m, c i p * r ^ i) + R m p r)
    : ∃ C' : ℝ, 0 ≤ C' ∧ ∀ p ∈ K, ∀ r : ℝ, 0 ≤ r → r ≤ r₀ →
        |R m p r| ≤ C' * r ^ m := by
  sorry

#print axioms analytic_remainder_bound

end LuH14
