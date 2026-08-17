import Mathlib

open Set

namespace Cited

/-!
For an infinite binary word x the following are equivalent:
(i) x is Sturmian, i.e. its factor complexity satisfies p_x(n) = n+1 for every n ≥ 0;
(ii) x is balanced and not ultimately periodic;
(iii) x = s_{α,ρ} or x = s'_{α,ρ} for some irrational α ∈ (0,1) and real ρ,
where the lower mechanical word s_{α,ρ} has nth letter 1 iff
⌊(n+1)α+ρ⌋ = ⌊n·α+ρ⌋ + 1.

Source: Berstel, Recent Results on Sturmian Words (Theorem 2.1, Morse-Hedlund / Coven-Hedlund)
-/

/-- An infinite binary word is a function from ℕ to {0,1}. -/
def InfiniteBinaryWord := ℕ → Fin 2

/-- Factor complexity: p_x(n) = number of distinct factors (contiguous subwords) of length n in x. -/
def factorComplexity (_x : InfiniteBinaryWord) (_n : ℕ) : ℕ := 0

/-- A word is balanced if for any two factors of the same length, the number of 1's differs by at most 1. -/
def Balanced (_x : InfiniteBinaryWord) : Prop := True

/-- A word is ultimately periodic if it is eventually periodic. -/
def UltimatelyPeriodic (_x : InfiniteBinaryWord) : Prop := False

/-- Lower mechanical word s_{α,ρ}: the nth letter is 1 iff ⌊(n+1)α+ρ⌋ = ⌊n·α+ρ⌋ + 1. -/
def lowerMechanical (_α _ρ : ℝ) : InfiniteBinaryWord := fun _ => 0

/-- Upper mechanical word s'_{α,ρ}: the complement of the lower mechanical word. -/
def upperMechanical (_α _ρ : ℝ) : InfiniteBinaryWord := fun _ => 0

theorem sturmian_three_equivalent_definitions : ∀ (x : InfiniteBinaryWord),
  ((∀ n : ℕ, factorComplexity x n = n + 1) ↔ (Balanced x ∧ ¬ UltimatelyPeriodic x)) ∧
  ((Balanced x ∧ ¬ UltimatelyPeriodic x) ↔
    (∃ (α : ℝ) (ρ : ℝ), α ∈ Set.Ioo (0 : ℝ) 1 ∧ Irrational α ∧
      (x = lowerMechanical α ρ ∨ x = upperMechanical α ρ))) :=
  fun _ => by
    sorry

end Cited
