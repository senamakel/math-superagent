import Mathlib

namespace Cited

/--
Avanesov 1967, Acta Arith. 12 409-420 (primary unreadable); attested via Kiss 1988 and GRKTU 2020,
summaries avanesov-figurate-numbers-1967.md and avanesov-and-laishram-attestation.md,
claim avanesov-1967-cx3-cy2-complete

The positive integer solutions (x, y) to binomial C(x,3) = C(y,2) are exactly
(3,2), (5,5), (10,16), (22,56), (36,120).
-/
axiom avanesov_triangular_tetrahedral_solutions :
  ∀ (x y : ℕ), 0 < x → 0 < y →
    ((Nat.choose x 3 = Nat.choose y 2) ↔
      (x = 3 ∧ y = 2) ∨ (x = 5 ∧ y = 5) ∨ (x = 10 ∧ y = 16) ∨ (x = 22 ∧ y = 56) ∨ (x = 36 ∧ y = 120)) :=
  sorry

end Cited
