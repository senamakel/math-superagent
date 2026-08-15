import Mathlib

-- gcd of x-1 and x+1 is 1 when 2 | x
example (x : ℕ) (h2 : 2 ∣ x) : (x - 1).gcd (x + 1) = 1 := by
  -- since x even, gcd divides 2, and both are odd so gcd divides 1
  apply Nat.dvd_antisymm
  · -- 1 divides any gcd
    omega
  · -- gcd | 1 : gcd dvd x-1 and gcd dvd x+1; gcd odd, gcd even
    -- gcd divides (x+1) - (x-1) = 2, and gcd is odd
    sorry
