import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Algebra.GCDMonoid.Nat
import Mathlib.Algebra.GCDMonoid.Basic
import Mathlib.Algebra.Ring.Parity

#check Int.instSubsingleton -- ?
#check (inferInstance : Subsingleton ℕˣ)
#check exists_eq_pow_of_mul_eq_pow (α := ℕ)
#check Nat.Coprime.coprime_dvd_left
#check Nat.odd_iff
#check even_iff_exists_two_mul
#check Nat.coprime_self_add_right
#check Nat.prime_two
#check Nat.Prime.dvd_of_dvd_pow

example {a b c k : ℕ} (hc : a.Coprime b) (h : a * b = c ^ k) : ∃ d, a = d ^ k := by
  have hg : IsUnit (a.gcd b) := by
    rw [Nat.isUnit_iff, Nat.coprime_iff_gcd_eq_one.mp hc]
  exact exists_eq_pow_of_mul_eq_pow (α := ℕ) hg h
