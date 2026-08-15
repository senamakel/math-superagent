import Mathlib.Data.ZMod.Basic
import Mathlib.FieldTheory.Finite.Basic
import Mathlib.Data.Int.GCD
import Mathlib.Data.Int.ModEq
import Mathlib.Algebra.Ring.GeomSum

#check Int.cast_zmod_eq_zero_iff_dvd
#check ZMod.pow_card
#check sub_one_dvd_pow_sub_one
#check Finset.dvd_sum
#check Int.dvd_sub
#check Finset.sum_sub_distrib
#check Int.coe_nat_dvd
#check Nat.Prime.dvd_iff_eq
#check dvd_trans

namespace Cassels

theorem flt_dvd_iff {p : ℕ} (hP : Nat.Prime p) (x : ℤ) :
    (p : ℤ) ∣ (x - 1) ↔ (p : ℤ) ∣ (x ^ p - 1) := by
  haveI : Fact p.Prime := ⟨hP⟩
  rw [← Int.cast_zmod_eq_zero_iff_dvd (x - 1) p]
  rw [← Int.cast_zmod_eq_zero_iff_dvd (x ^ p - 1) p]
  push_cast
  rw [sub_eq_zero, pow_card]
  rfl

theorem phi_congruent_p {p : ℕ} (x : ℤ) (hx : 2 ≤ x) :
    x - 1 ∣ (∑ k in Finset.range p, x ^ k) - (p : ℤ) := by
  have hterm : ∀ k ∈ Finset.range p, (x - 1) ∣ x ^ k - 1 := by
    intro k hk
    exact sub_one_dvd_pow_sub_one x k
  have hsum : (x - 1) ∣ ∑ k in Finset.range p, (x ^ k - 1) := by
    exact Finset.dvd_sum hterm
  have hrewrite :
      (∑ k in Finset.range p, (x ^ k - 1)) = (∑ k in Finset.range p, x ^ k) - (p : ℤ) := by
    rw [Finset.sum_sub_distrib]
    rw [show (∑ k in Finset.range p, (1 : ℤ)) = (p : ℤ) by simp]
  rw [← hrewrite]
  exact hsum

theorem prime_of_dvd_both {p r : ℕ} (hP : Nat.Prime p) (hr : Nat.Prime r)
    {x : ℤ} (hx : 2 ≤ x)
    (h1 : (r : ℤ) ∣ x - 1) (h2 : (r : ℤ) ∣ ∑ k in Finset.range p, x ^ k) :
    r = p := by
  have hcong : x - 1 ∣ (∑ k in Finset.range p, x ^ k) - (p : ℤ) := phi_congruent_p x hx
  have h1' : (r : ℤ) ∣ (∑ k in Finset.range p, x ^ k) - (p : ℤ) := dvd_trans h1 hcong
  have hdvd : (r : ℤ) ∣ (p : ℤ) := by
    let phi : ℤ := ∑ k in Finset.range p, x ^ k
    have hsub : (r : ℤ) ∣ phi - (phi - (p : ℤ)) := Int.dvd_sub h2 h1'
    have hident : phi - (phi - (p : ℤ)) = (p : ℤ) := by ring
    rwa [hident] at hsub
  have hrpN : r ∣ p := Int.coe_nat_dvd.mp hrp  -- wrong, fix
  exact (hr.dvd_iff_eq hP).mp hrpN

end Cassels
