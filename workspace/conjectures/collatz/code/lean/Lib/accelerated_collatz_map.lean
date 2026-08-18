import Mathlib

namespace Cited

/-- For every positive integer n, define T(n) = n / 2 if n is even and T(n) = (3 * n + 1) / 2 if n is odd. -/
def T (n : ℕ) : ℕ := if n % 2 = 0 then n / 2 else (3 * n + 1) / 2

axiom accelerated_collatz_map (n : ℕ) (hn : n > 0) : T n = (if n % 2 = 0 then n / 2 else (3 * n + 1) / 2)

end Cited
