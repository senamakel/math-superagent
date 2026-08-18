import Mathlib

namespace Dukov2023

def CharacteristicNumbers (n : ℕ) := Fin n → ℝ
def binaryMonomial {n : ℕ} (lam : CharacteristicNumbers n) (I : Fin n → Fin 2) : ℝ :=
  ∏ i, lam i ^ (I i).val
def Lambda (n : ℕ) (lam : CharacteristicNumbers n) : ℝ :=
  ∏ I : (Fin n → Fin 2), if (∀ i, I i = 0) then 1 else binaryMonomial lam I - 1
def M (a b c : ℝ) : ℝ := 4 * (a * b * c - 1) - (a - 1) * (b - 1) * (c - 1)
def L4 (lam : CharacteristicNumbers 4) : ℝ :=
  Lambda 4 lam *
    (M (lam 0) (lam 1) (lam 2) * M (lam 0) (lam 1) (lam 3) *
      M (lam 0) (lam 2) (lam 3) * M (lam 1) (lam 2) (lam 3))
axiom Typical {n : ℕ} (lam : CharacteristicNumbers n) : Prop
axiom BornLimitCycle {n : ℕ} (lam : CharacteristicNumbers n) : Type
axiom multiplicity {n : ℕ} {lam : CharacteristicNumbers n} : BornLimitCycle lam → ℕ
namespace Cited
/-- src: Dukov, arXiv:2201.03652, Theorem 1 and corollary. -/
axiom multiplicity_bound {n : ℕ} {lam : CharacteristicNumbers n} :
  Typical lam → ∀ c : BornLimitCycle lam, multiplicity c ≤ n
end Cited

theorem dukov_multiplicity_hyperbolic_polycycles
    {n : ℕ} {lam : CharacteristicNumbers n}
    (hTypical : Typical lam) :
    ∀ c : BornLimitCycle lam, multiplicity c ≤ n := by
  exact Cited.multiplicity_bound hTypical

#print axioms dukov_multiplicity_hyperbolic_polycycles
#print axioms Cited.multiplicity_bound
end Dukov2023
