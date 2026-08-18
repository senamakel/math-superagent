import Mathlib

namespace SlowDivergenceECTBound

def Family (ι α : Type) := ι → α → ℝ
def ZeroSet {α : Type} (D : Set α) (u : α → ℝ) : Set α := {x | x ∈ D ∧ u x = 0}
def ECTCertificate {ι α : Type} [Fintype ι] (D : Set α) (f : Family ι α) : Prop :=
  ∀ c : ι → ℝ, (∃ i, c i ≠ 0) →
    (ZeroSet D (fun x => ∑ i, c i * (f i) x)).Finite ∧
    Set.ncard (ZeroSet D (fun x => ∑ i, c i * (f i) x)) ≤ Fintype.card ι - 1
def HasECTDisplacement {ι α : Type} [Fintype ι] (D : Set α) (f : Family ι α) (δ : α → ℝ) : Prop :=
  ∃ c : ι → ℝ, (∃ i, c i ≠ 0) ∧ ∀ x, x ∈ D → δ x = ∑ i, c i * (f i) x

theorem displacement_finite_zero_bound {ι α : Type} [Fintype ι]
    (D : Set α) (f : Family ι α) (δ : α → ℝ) (hECT : ECTCertificate D f)
    (hδ : HasECTDisplacement D f δ) :
    (ZeroSet D δ).Finite ∧ Set.ncard (ZeroSet D δ) ≤ Fintype.card ι - 1 := by
  rcases hδ with ⟨c, hc, hrepr⟩
  have hz : ZeroSet D δ = ZeroSet D (fun x => ∑ i, c i * (f i) x) := by
    ext x
    simp only [ZeroSet, Set.mem_setOf_eq]
    constructor
    · rintro ⟨hx, hzero⟩
      exact ⟨hx, by rw [← hrepr x hx, hzero]⟩
    · rintro ⟨hx, hzero⟩
      exact ⟨hx, by rw [hrepr x hx, hzero]⟩
  rw [hz]
  exact hECT c hc

#print axioms displacement_finite_zero_bound
end SlowDivergenceECTBound
