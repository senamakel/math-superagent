import Mathlib.Data.Nat.Choose.Factorization
import Mathlib

-- Interior binomial of a power of two is even.
-- Uses: factorization_choose_prime_pow  gives  (choose (2^m) j).factorization 2 = m - j.factorization 2
--       factorization_le_of_le_pow       gives  j.factorization 2 ≤ m   (from j ≤ 2^m)
-- Then m - j.factorization 2 > 0  requires  j.factorization 2 < m, i.e.  ¬ 2^m ∣ j,
-- which follows from j < 2^m.
example (m j : ℕ) (hjp : 0 < j) (hjm : j < 2 ^ m) :
    0 < (Nat.choose (2 ^ m) j).factorization 2 := by
  have hprime : Nat.Prime 2 := Nat.prime_two
  have hkn : j ≤ 2 ^ m := le_of_lt hjm
  have hk0 : j ≠ 0 := ne_of_gt hjp
  have hfc := Nat.factorization_choose_prime_pow (p := 2) (n := m) (k := j) hprime hkn hk0
    -- (choose (2^m) j).factorization 2 = m - j.factorization 2
  have hfacm : j.factorization 2 ≤ m := Nat.factorization_le_of_le_pow hkn
  have hndvd : ¬ 2 ^ m ∣ j := by
    intro hd
    have hle := Nat.le_of_dvd hjp hd   -- 2^m ≤ j
    omega
  have hltm : j.factorization 2 < m := by
    have : ¬ m ≤ j.factorization 2 := by
      intro hmle
      have hdvd : 2 ^ m ∣ j := (hprime.pow_dvd_iff_le_factorization hk0).2 hmle
      exact hndvd hdvd
    omega
  rw [hfc]
  omega
