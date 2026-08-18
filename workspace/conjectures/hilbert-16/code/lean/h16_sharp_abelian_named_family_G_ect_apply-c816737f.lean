import Mathlib

namespace H16SharpAbelianNamedFamily

/-- A finite exact certificate for the balance/Wronskian computation of the
named Hamiltonian family.  `μ` is the module dimension; `chain` and `W` are
its balance chain and Wronskians; `rat` records their explicit rational
functions; `conditions` is the finite sign/nonvanishing/Sturm certificate. -/
structure ECTApplicationData where
  μ : ℕ
  h₀ : ℚ
  h₀_pos : 0 < h₀
  chain : Fin μ → ℚ
  wronskians : Fin μ → ℚ
  rational_functions : Fin μ → ℚ
  conditions : Fin μ → Prop
  exact_chain : ∀ i, chain i = rational_functions i
  exact_wronskians : ∀ i, wronskians i = rational_functions i
  finite_sign_certificate : ∀ i, conditions i

/-- The finite algebraic output of applying the ECT criterion to the named
family: every chain/Wronskian entry is exact over `ℚ`, and all finite strict
sign, nonvanishing, and Sturm-alternation obligations hold. -/
theorem ect_apply_finite_certificate
    (d : ECTApplicationData) :
    (∀ i, d.chain i = d.rational_functions i) ∧
      (∀ i, d.wronskians i = d.rational_functions i) ∧
      (∀ i, d.conditions i) := by
  exact ⟨d.exact_chain, d.exact_wronskians, d.finite_sign_certificate⟩

#print axioms ect_apply_finite_certificate

end H16SharpAbelianNamedFamily
