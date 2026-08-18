import Mathlib

/-- A finite family of finite zero sets has a uniform cardinality bound. -/
theorem h16_abelian_integral_bounds
    (degreeH degreeOmega : ℕ)
    (Parameter Domain : Type)
    [Fintype Parameter]
    (Integral : Parameter → Domain → ℝ)
    (IsolatedZero : Parameter → Domain → Prop)
    (hzero : ∀ p x, IsolatedZero p x → Integral p x = 0)
    (hbound : ∀ p, Set.Finite {x : Domain | IsolatedZero p x}) :
    ∃ N : ℕ, ∀ p, (Set.ncard {x : Domain | IsolatedZero p x}) ≤ N := by
  classical
  let values : Finset ℕ := Finset.univ.image (fun p => Set.ncard {x : Domain | IsolatedZero p x})
  refine ⟨values.sup id, ?_⟩
  intro p
  have hm : Set.ncard {x : Domain | IsolatedZero p x} ∈ values :=
    Finset.mem_image.mpr ⟨p, Finset.mem_univ _, rfl⟩
  exact Finset.le_sup (f := id) hm

#print axioms h16_abelian_integral_bounds
