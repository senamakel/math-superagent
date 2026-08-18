import Mathlib

open Finset

variable {n : ℕ}

def R_le (r : Fin n → ℝ) (σ : Equiv.Perm (Fin n)) (i : Fin n) : ℝ :=
  ∏ j ∈ Finset.Iic i, r (σ j)

def R_lt (r : Fin n → ℝ) (σ : Equiv.Perm (Fin n)) (i : Fin n) : ℝ :=
  ∏ j ∈ Finset.Iio i, r (σ j)

noncomputable def Δ (r : Fin n → ℝ) : ℕ := by
  classical
    exact Finset.sup' (Finset.univ : Finset (Equiv.Perm (Fin n))) (Finset.univ_nonempty) λ σ =>
      ((Finset.univ : Finset (Fin n)).filter λ i =>
        (R_le r σ i - 1) * (R_lt r σ i - 1) < 0
      ).card

theorem hyperbolic_polycycle_delta_zero_iff_all_ratios_one (n : ℕ) (r : Fin n → ℝ) (hpos : ∀ i, 0 < r i) :
  Δ r = 0 ↔ ∀ i, r i = 1 := by
  constructor
  · intro hΔ i
    by_contra hne
    have hpos_i : 0 < r i := hpos i
    have hne' : r i ≠ 1 := hne
    have h_cases : r i < 1 ∨ 1 < r i := by
      by_cases h : r i < 1
      · exact Or.inl h
      · have h' : 1 ≤ r i := by linarith
        have hlt : 1 < r i := by
          by_contra hle
          have heq : r i = 1 := by linarith
          exact hne' heq
        exact Or.inr hlt
    sorry
  · intro h_all_one
    classical
      dsimp [Δ]
      apply le_antisymm
      · apply Finset.sup'_le
        intro σ hσ
        have h_card : ((Finset.univ : Finset (Fin n)).filter λ i =>
          (R_le r σ i - 1) * (R_lt r σ i - 1) < 0).card = 0 := by
          apply Finset.card_eq_zero.mpr
          apply Finset.filter_eq_empty_iff.mpr
          intro i hi
          have hR_le : R_le r σ i = 1 := by
            dsimp [R_le]
            apply Finset.prod_eq_one
            intro j hj
            rw [h_all_one (σ j)]
          have hR_lt : R_lt r σ i = 1 := by
            dsimp [R_lt]
            apply Finset.prod_eq_one
            intro j hj
            rw [h_all_one (σ j)]
          rw [hR_le, hR_lt]
          simp
        rw [h_card]
      · apply Nat.zero_le

#print axioms hyperbolic_polycycle_delta_zero_iff_all_ratios_one
