import Mathlib

namespace PE1006CW3

def Summary (V : ℕ → ℕ) (s : Finset ℕ) : ℕ × ℕ × ℕ :=
  (s.card, ∑ r ∈ s, V r, ∑ r ∈ s, V r ^ 2)

def AddSummary (x y : ℕ × ℕ × ℕ) : ℕ × ℕ × ℕ :=
  (x.1 + y.1, x.2.1 + y.2.1, x.2.2 + y.2.2)

theorem summary_union_add
    (V : ℕ → ℕ) (a b c : ℕ)
    (hab : a ≤ b) (hbc : b ≤ c) :
    Summary V (Finset.Ico a c) =
      AddSummary (Summary V (Finset.Ico a b)) (Summary V (Finset.Ico b c)) := by
  unfold Summary AddSummary
  have hd : Disjoint (Finset.Ico a b) (Finset.Ico b c) := by
    rw [Finset.disjoint_left]
    intro x hxab hxbc
    simp only [Finset.mem_Ico] at hxab hxbc
    omega
  have hu : Finset.Ico a c = Finset.Ico a b ∪ Finset.Ico b c := by
    ext r
    simp only [Finset.mem_Ico, Finset.mem_union]
    omega
  rw [hu, Finset.card_union_of_disjoint hd, Finset.sum_union hd,
    Finset.sum_union hd]

theorem summary_add_assoc (x y z : ℕ × ℕ × ℕ) :
    AddSummary (AddSummary x y) z = AddSummary x (AddSummary y z) := by
  simp [AddSummary, Nat.add_assoc]

#print axioms summary_union_add
#print axioms summary_add_assoc

end PE1006CW3
