import Mathlib

namespace Cited

/--
For every positive integer n, there exists a natural number k such that
the k-fold iterate of the accelerated Collatz map T satisfies
T^[k](n) ≡ 2 mod 9.

Source: research/summaries/citations_w4302066018.md
-/
axiom orbit_contains_two_mod_nine : ∀ (n : ℕ), n ≥ 1 → ∃ (k : ℕ), (T^[k] n) % 9 = 2

end Cited
