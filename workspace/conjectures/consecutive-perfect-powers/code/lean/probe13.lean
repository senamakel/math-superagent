import Mathlib

-- Attempt A: (a+1)^q - a^q >= 3 for a>=1, q>=2, via (a+1)^q >= a^q + 3 shown by binomial-lite
example (a q : ℕ) (ha : 1 ≤ a) (hq : 2 ≤ q) : 3 ≤ (a + 1) ^ q - a ^ q := by
  -- (a+1)^2 - a^2 = 2a+1 >= 3 ; show D_q >= D_2
  have h2 : (a + 1) ^ 2 - a ^ 2 ≥ 3 := by
    -- (a+1)^2 - a^2 = 2a+1
    have h : (a + 1) ^ 2 = a ^ 2 + 2 * a + 1 := by ring_nf
    omega
  -- D_q >= D_2: (a+1)^q - a^q >= (a+1)^2 - a^2
  have hD : (a + 1) ^ q - a ^ q ≥ (a + 1) ^ 2 - a ^ 2 := by
    sorry
  omega
