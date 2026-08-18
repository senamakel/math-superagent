import Mathlib

namespace Cited

/-- For every positive integer n, there exists a natural number k such that the k-th
iterate of the accelerated Collatz function T, defined by T(n) = (3n + 1) / 2 when n is odd
and T(n) = n / 2 when n is even, equals 1.

Source: research/summaries/chamberland-update-survey.md, Introduction -/
axiom accelerated_collatz_conjecture : ∀ (n : ℕ), n ≥ 1 → ∃ (k : ℕ), Nat.iterate (fun (m : ℕ) =>
  if m % 2 = 0 then m / 2 else (3 * m + 1) / 2) k n = 1

end Cited

#print axioms Cited.accelerated_collatz_conjecture
