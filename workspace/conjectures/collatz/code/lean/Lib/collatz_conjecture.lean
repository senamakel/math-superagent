import Mathlib

namespace Cited

/-- For every positive integer n, there exists a natural number k such that
the k-fold iterate of the Collatz map C satisfies C^[k](n) = 1.

Source: research/summaries/citations_w4302066018.md
-/
axiom collatz_conjecture : ∀ (n : ℕ), n ≥ 1 → ∃ (k : ℕ), Nat.iterate (fun (x : ℕ) =>
  if h : x % 2 = 0 then x / 2 else 3 * x + 1) k n = 1

end Cited
