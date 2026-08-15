import Mathlib

/-!
# Catalan: prime-exponent reduction and the known solution

Three small, airtight facts that every downstream argument about `x^p - y^q = 1`
assumes.

1. **The reduction identity.**  If `(x ^ a) ^ P - (y ^ b) ^ Q = 1` then with
   `p = a * P` and `q = b * Q` we have `x ^ p - y ^ q = 1` — i.e.
   `(x ^ a) ^ P = x ^ (a * P)` and `(y ^ b) ^ Q = y ^ (b * Q)`, which is just
   `pow_mul`.  P and Q being prime is stated in the task but is *not* needed
   for the identity; the general statement is an iff.

2. **The known solution.** `3 ^ 2 - 2 ^ 3 = 1`, as a direct arithmetic check.

3. **`3` and `2` are not nontrivial perfect powers**, so the known solution is
   "unchanged by the reduction": neither base can arise as a nontrivial `a ^ e`.
-/

namespace Catalin

/-! ## 1. The reduction identity -/

-- Over the natural numbers.  `Nat.pow_mul` rearranges the powers.
theorem reduction_iff (x a P y b Q : ℕ) :
    (x ^ a) ^ P - (y ^ b) ^ Q = 1 ↔ x ^ (a * P) - y ^ (b * Q) = 1 := by
  constructor
  · intro h
    rw [pow_mul, pow_mul]
    exact h
  · intro h
    rw [← pow_mul, ← pow_mul]
    exact h

-- The directed version exactly as the task states it, with P and Q prime.
-- Note that the primality hypotheses are unused: the power identity holds
-- for every natural exponent, so the reduction does not need `Nat.Prime`.
theorem prime_exponent_reduction (x a P y b Q : ℕ)
    (_hP : Nat.Prime P) (_hQ : Nat.Prime Q) :
    (x ^ a) ^ P - (y ^ b) ^ Q = 1 → x ^ (a * P) - y ^ (b * Q) = 1 := by
  intro h
  exact (reduction_iff x a P y b Q).mp h

-- The same identity over the integers (where there is no truncated subtraction).
theorem reduction_iff_int (x y : ℤ) (a b P Q : ℕ) :
    (x ^ a) ^ P - (y ^ b) ^ Q = 1 ↔ x ^ (a * P) - y ^ (b * Q) = 1 := by
  constructor
  · intro h
    rw [pow_mul, pow_mul]
    exact h
  · intro h
    rw [← pow_mul, ← pow_mul]
    exact h

/-! ## 2. The known solution -/

theorem known_solution_value : (3 : ℕ) ^ 2 - 2 ^ 3 = 1 := by
  norm_num

theorem known_solution :
    3 ^ 2 - 2 ^ 3 = 1 := by
  norm_num

/-! ## 3. `2` and `3` are not nontrivial perfect powers -/

-- Helper: a positive power with base and exponent at least 2 is at least 4.
lemma pow_four_le {a e : ℕ} (ha : 2 ≤ a) (he : 2 ≤ e) : 4 ≤ a ^ e := by
  have hba : 2 ^ e ≤ a ^ e := Nat.pow_le_pow_left ha e
  have heb : 2 ^ 2 ≤ 2 ^ e := by
    exact pow_le_pow_right₀ (by omega : 1 ≤ 2) he
  omega

lemma two_not_perfect_power : ¬ ∃ (a e : ℕ), 2 ≤ e ∧ a ^ e = 2 := by
  rintro ⟨a, e, he, h⟩
  by_cases ha : a ≤ 1
  · -- a ≤ 1, so a^e ≤ 1^e = 1 < 2
    have hle : a ^ e ≤ 1 := by
      have hbase := Nat.pow_le_pow_left ha e   -- a^e ≤ 1^e
      have hone : 1 ^ e = 1 := by simp
      omega
    omega
  · -- a ≥ 2
    have ha2 : 2 ≤ a := by omega
    have hge : 4 ≤ a ^ e := pow_four_le ha2 he
    omega

lemma three_not_perfect_power : ¬ ∃ (a e : ℕ), 2 ≤ e ∧ a ^ e = 3 := by
  rintro ⟨a, e, he, h⟩
  by_cases ha : a ≤ 1
  · have hle : a ^ e ≤ 1 := by
      have hbase := Nat.pow_le_pow_left ha e
      have hone : 1 ^ e = 1 := by simp
      omega
    omega
  · have ha2 : 2 ≤ a := by omega
    have hge : 4 ≤ a ^ e := pow_four_le ha2 he
    omega

end Catalin

/-! #print axioms scan (self-contained) -/
#print axioms Catalin.reduction_iff
#print axioms Catalin.prime_exponent_reduction
#print axioms Catalin.reduction_iff_int
#print axioms Catalin.known_solution
#print axioms Catalin.two_not_perfect_power
#print axioms Catalin.three_not_perfect_power
