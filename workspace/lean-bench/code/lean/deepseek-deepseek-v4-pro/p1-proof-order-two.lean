import Mathlib.Algebra.Parity
import Mathlib.NumberTheory.Euler

theorem odd_dvd_two_pow_totient_sub_one (n : ℕ) (hn : n ≥ 1) (hodd : Odd n) : n ∣ 2 ^ (Nat.totient n) - 1 := by
  have hcop : Nat.Coprime n 2 := Nat.coprime_two_of_odd hodd
  have hmod : 2 ^ (Nat.totient n) ≡ 1 [MOD n] := Nat.ModEq.pow_totient (a := 2) hcop
  have hle : 1 ≤ 2 ^ (Nat.totient n) := by
    have hpos : 0 < 2 ^ (Nat.totient n) := pow_pos (by norm_num : 0 < 2) (Nat.totient n)
    exact Nat.one_le_of_lt hpos
  exact hmod.dvd hle

#print axioms odd_dvd_two_pow_totient_sub_one
