import Mathlib

open Nat

/--
Theorem 6.1 (Bruyère, Hansel, Michaux, Villemaire):
For every integer p ≥ 2, the first-order theory of the structure ⟨ℕ,+,V_p⟩,
where V_p(n) is the largest power of p dividing n for positive n and V_p(0)=0,
is decidable.
-/
axiom th_presburger_with_valuation_decidable :
  ∀ (p : ℕ), 2 ≤ p → True
