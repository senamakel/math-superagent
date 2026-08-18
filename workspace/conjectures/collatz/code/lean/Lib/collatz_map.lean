import Mathlib

open Nat

/-- The Collatz map: C(n) = n/2 if n is even, 3n+1 if n is odd. -/
def collatz_map (n : ℕ) : ℕ :=
  if n % 2 = 0 then n / 2 else 3 * n + 1

/-- For every positive integer n, the Collatz map is defined as above. -/
theorem collatz_map_spec (n : ℕ) (_hn : n > 0) : collatz_map n = if n % 2 = 0 then n / 2 else 3 * n + 1 := by
  rfl

#print axioms collatz_map_spec
