import Mathlib

-- Attempt B: (a+1)^q - a^q >= 3 via monotonicity of base and exponent bounds
-- Show (a+1)^q >= a^q + 3 by:  q >= 2 → (a+1)^q >= (a+1)^2; a^q <= ...
example (a q : ℕ) (ha : 1 ≤ a) (hq : 2 ≤ q) : 3 ≤ (a + 1) ^ q - a ^ q := by
  have h1 : 1 ≤ a + 1 := by omega
  have hge : (a + 1) ^ 2 ≤ (a + 1) ^ q := pow_le_pow_right₀ h1 hq
  have hbase : (a + 1) ^ 2 ≥ a ^ 2 + 3 := by
    have : (a + 1) ^ 2 = a ^ 2 + 2 * a + 1 := by ring_nf
    omega
  -- (a+1)^q >= a^2+3 and a^q >= a^2
  have hqa : a ^ 2 ≤ a ^ q := pow_le_pow_right₀ (by omega : 1 ≤ a) hq
  have hF : (a + 1) ^ q ≥ a ^ q + 3 := by
    -- (a+1)^q >= a^2 + 3; a^q <= (a+1)^q ; need (a+1)^q >= a^q + 3
    sorry
  omega
