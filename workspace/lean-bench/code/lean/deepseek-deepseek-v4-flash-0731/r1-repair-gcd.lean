import Mathlib.Data.Nat.Choose.Lucas
import Mathlib

-- IsPrimePow helper for 2^k
example (k : ℕ) (hk : 1 ≤ k) : IsPrimePow (2 ^ k) := by
  refine IsPrimePow.pow ?hbase ?_
  · use 2, 1
    norm_num
  · omega

-- minFac of 2^k is 2
example (k : ℕ) (hk : 1 ≤ k) : (2 ^ k).minFac = 2 := by
  rw [Nat.minFac_eq_two_iff]
  constructor
  · exact pow_ne_zero k (by norm_num : (2 : ℕ) ≠ 0)
  · use 2 ^ (k - 1)
    have hsub : k - 1 + 1 = k := Nat.sub_add_cancel hk
    calc
      2 ^ k = 2 ^ (k - 1 + 1) := by rw [hsub]
      _ = 2 ^ (k - 1) * 2 := by rw [pow_succ]
      _ = 2 ^ (k - 1) + 2 ^ (k - 1) := by ring

-- gcd_dvd name
example {s : Finset ℕ} {a : ℕ} {_b : ℕ} (h : a ∈ s) : s.gcd id ∣ a := by
  exact Finset.gcd_dvd h
