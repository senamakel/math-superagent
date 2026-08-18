import Mathlib

namespace Cited

/--
From: research/summaries/buzzi-novaes-note-recent-attempt-2024.md, abstract

The claimed formula for the Hilbert number is H(n) = 2(n - 1)(4(n - 1) - 2) for every natural number n.
-/
def H (n : ℕ) : ℕ := 2 * (n - 1) * (4 * (n - 1) - 2)

axiom claimed_hilbert_number_formula (n : ℕ) : H n = 2 * (n - 1) * (4 * (n - 1) - 2)

#print axioms claimed_hilbert_number_formula

end Cited
