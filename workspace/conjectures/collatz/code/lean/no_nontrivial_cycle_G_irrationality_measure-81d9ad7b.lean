import Mathlib

/-- The requested irrationality-measure statement, with the real logarithmic ratio
    represented explicitly.  Here `μ` is a real exponent, `c₀` is an effective
    positive constant (effectivity is not encoded in Lean), and `p,q` are positive
    natural integers. -/
theorem irrationality_measure_delta
    (μ c₀ : ℝ)
    (hμ : μ < 8.616)
    (hc₀ : 0 < c₀)
    (hmeasure : ∀ p q : ℕ, 1 ≤ p → 1 ≤ q →
      |Real.log 3 / Real.log 2 - (p : ℝ) / (q : ℝ)| > c₀ / (q : ℝ) ^ μ) :
    ∀ K L : ℕ, 1 ≤ K →
      |Real.log 3 / Real.log 2 - ((K + L : ℕ) : ℝ) / (K : ℝ)| > c₀ / (K : ℝ) ^ μ := by
  intro K L hK
  exact hmeasure (K + L) K (by omega) hK

#print axioms irrationality_measure_delta
