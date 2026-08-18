import Mathlib

def UniformlyBounded {α β : Type*} [LE β] (f : α → β) : Prop :=
  ∃ B : β, ∀ a, f a ≤ B

/-- Compactness plus an explicit finite-range hypothesis gives a uniform bound. -/
theorem compact_finite_range_uniform_bound
    {α : Type*} [TopologicalSpace α] [CompactSpace α]
    {f : α → ℕ}
    (hfinite : Set.Finite (Set.range f)) :
    UniformlyBounded f := by
  classical
  let s : Finset ℕ := hfinite.toFinset
  refine ⟨s.sup id, ?_⟩
  intro a
  exact Finset.le_sup (s := s) (f := id) (hfinite.mem_toFinset.mpr ⟨a, rfl⟩)

#print axioms compact_finite_range_uniform_bound
