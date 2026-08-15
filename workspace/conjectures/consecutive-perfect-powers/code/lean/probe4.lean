import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Data.Nat.Factorization.Basic
import Mathlib.Algebra.GCDMonoid.Nat
import Mathlib.Algebra.Ring.Parity

/-- Coprime product is a power: each factor is the same power of some natural. -/
lemma coprime_mul_eq_pow_dvd {a b c k : ℕ} (hc : a.Coprime b) (h : a * b = c ^ k) :
    ∃ d, a = d ^ k := by
  have hg : IsUnit (GCDMonoid.gcd a b) := by
    rw [gcd_eq_nat_gcd, Nat.isUnit_iff, Nat.coprime_iff_gcd_eq_one.mp hc]
  exact exists_eq_pow_of_mul_eq_pow (α := ℕ) hg h
