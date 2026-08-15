import Mathlib.Data.Nat.Choose.Lucas
import Mathlib.Tactic.Ring
import Mathlib

-- Frobenius in ZMod 2: for any a, (1 + a)^(2^k) = 1 + a^(2^k)
example (k : ℕ) (a : ZMod 2) : (1 + a) ^ 2 ^ k = 1 + a ^ 2 ^ k := by
  -- via add_pow_char_pow with ExpChar CharP (ZMod 2) 2
  exact add_pow_char_pow (R := ZMod 2) (x := 1) (y := a) (p := 2) (n := k)

-- ZMod 2 has characteristic 2 (so add_pow_char applies)
example (k : ℕ) (a : ZMod 2) : (1 + a) ^ 2 ^ k = 1 + a ^ 2 ^ k := by
  have h := add_pow_char_pow (R := ZMod 2) (x := (1 : ZMod 2)) (y := a) (p := 2) (n := k)
  simpa using h

-- weaker / direct via binomial theorem showing intermediate terms vanish:
-- (1+a)^(2^k) = sum_j C(2^k, j) a^j; for 1<=j<=2^k-1 the coefficient is 0 in ZMod 2.
-- Let's instead just confirm the ring handles 2 = 0.
example : (2 : ZMod 2) = 0 := by norm_num
example (x : ZMod 2) : 2 * x = 0 := by norm_num

-- ring should close the char-2 squaring claim (needs 2=0 fact)
example (a b : ZMod 2) : (a + b) ^ 2 = a ^ 2 + b ^ 2 := by
  have h : 2 = (0 : ZMod 2) := by norm_num
  ring_nf
  -- ring doesn't auto-use h; do it manually
  -- (a+b)^2 = a^2 + 2ab + b^2 ; 2ab = 0
  rw [pow_two, mul_add, add_mul, add_mul]
  -- we get a*a + a*b + b*a + b*b
  ring_nf
  -- now need to kill a*b + b*a = 2ab = 0
  rw [show (2 : ZMod 2) = 0 by norm_num]
  -- this should leave a^2 + b^2? Actually ring_nf left (a*b + b*a + a^2 + b^2) etc.
  omega
