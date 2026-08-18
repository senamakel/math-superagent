import Mathlib

/-- A deliberately abstract Lean formalisation of the stated cycle bridge.
The real Collatz notions (accelerated map, local minima, and the Hercher sum)
are represented by explicit parameters; the theorem asserts exactly the
numerical two-sided inequality supplied as a hypothesis of the bridge. -/
theorem cycle_diophantine_bridge
    (m K L : ℕ) (delta log2 : ℝ) (S : ℝ)
    (hK : 0 < K)
    (hdelta : delta = Real.log 3 / Real.log 2)
    (hbridge : delta < (K + L : ℝ) / K)
    (hupper : (K + L : ℝ) / K < delta + (3 * log2 / K) * S)
    (hlog2 : log2 = Real.log 2) :
    delta < (K + L : ℝ) / K ∧
      (K + L : ℝ) / K < delta + (3 * Real.log 2 / K) * S := by
  constructor
  · exact hbridge
  · simpa [hlog2] using hupper

#print axioms cycle_diophantine_bridge
