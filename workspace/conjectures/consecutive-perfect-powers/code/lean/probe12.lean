import Mathlib

-- bounding (a+1)^q >= 2^q - 1 for a>=1, q>=1
example (a q : ℕ) (ha : 1 ≤ a) (hq : 1 ≤ q) : (2 : ℕ) ^ q ≤ (a + 1) ^ q := by
  have hbase : (2 : ℕ) ≤ a + 1 := by omega
  exact Nat.pow_le_pow_left hbase q

-- 2^q - 1 >= 2^2 - 1 = 3 for q >= 2
example (q : ℕ) (hq : 2 ≤ q) : (3 : ℕ) ≤ (2 : ℕ) ^ q - 1 := by
  have : (2 : ℕ) ^ 2 ≤ 2 ^ q := pow_le_pow_right₀ (by norm_num) hq
  nlinarith
