import Mathlib.Data.Nat.Choose.Lucas
import Mathlib

-- IsPrimePow helper for 2^k
example (k : ℕ) (hk : 1 ≤ k) : IsPrimePow (2 ^ k) := by
  refine IsPrimePow.pow ?hbase (by simp [hk])
  exact isPrimePow_two

-- minFac of 2^k is 2
example (k : ℕ) (hk : 1 ≤ k) : (2 ^ k).minFac = 2 := by
  rw [Nat.minFac_pow]
  · exact Nat.minFac_eq_two (by norm_num)
  · exact hk

-- gcd_dvd name
example {s : Finset ℕ} {a b : ℕ} (h : a ∈ s) : s.gcd id ∣ a := by
  exact Finset.gcd_dvd h
