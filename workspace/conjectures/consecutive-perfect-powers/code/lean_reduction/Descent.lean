import Mathlib

/-!
# Catalan: descent from composite exponents to prime exponents

This file completes deliverable (a).  `CatalanReduction.lean` already proved
the power identity `(x ^ a) ^ P = x ^ (a * P)`.  Here we tie that identity to a
`CatalanSolution` predicate and certify the descent: a solution whose two
exponents are `a * P` and `b * Q` (with `P, Q` prime) descends to the prime
exponent solution `(x ^ a, y ^ b, P, Q)`.

P,S,Q primality is used only to get `1 < P` and `1 < Q` into the descended
`CatalanSolution`; the equality `(x ^ a) ^ P - (y ^ b) ^ Q = 1` needs no
primality (it is `pow_mul`).  This is why the reduction itself is an iff.
-/

namespace Cat

/-- A (positive) solution of the consecutive-perfect-powers equation. -/
def CatalanSolution (x y p q : ℕ) : Prop :=
  0 < x ∧ 0 < y ∧ 1 < p ∧ 1 < q ∧ x ^ p - y ^ q = 1

/-! ## The descent itself -/

theorem descent (x a P y b Q : ℕ) (hP : Nat.Prime P) (hQ : Nat.Prime Q) :
    CatalanSolution x y (a * P) (b * Q) → CatalanSolution (x ^ a) (y ^ b) P Q := by
  rintro ⟨hx, hy, _hp, _hq, hEq⟩
  refine ⟨Nat.pow_pos hx, Nat.pow_pos hy, hP.one_lt, hQ.one_lt, ?_⟩
  -- (x ^ a) ^ P - (y ^ b) ^ Q = 1, from x ^ (a*P) - y ^ (b*Q) = 1
  rw [← pow_mul, ← pow_mul]
  exact hEq

/-! ## Every composite exponent admits a prime sub-exponent -/

-- If p > 1 is not prime, there is a prime P with P < p and a cofactor a ≥ 2
-- with a * P = p.  This is what makes "descend" meaningful for a *composite*
-- exponent: the cofactor a is a genuine reduction (a ≥ 2).

lemma prime_sub_factor {p : ℕ} (hp1 : 1 < p) (hnp : ¬ Nat.Prime p) :
    ∃ (a P : ℕ), Nat.Prime P ∧ 1 < a ∧ a * P = p := by
  -- p has a prime divisor P, which is < p (otherwise p itself would be prime).
  obtain ⟨P, hP, hPdiv⟩ := Nat.exists_prime_and_dvd (by omega : p ≠ 1)
  have hPpos : 0 < P := hP.pos
  have hPle_p : P ≤ p := Nat.le_of_dvd hp1.le hPdiv
  have hPne : P ≠ p := by
    intro hPeq
    apply hnp
    simpa [hPeq] using hP
  have hPlt : P < p := Nat.lt_of_le_of_ne hPle_p hPne
  let a := p / P
  have haP : a * P = p := by
    dsimp [a]
    rw [Nat.div_mul_cancel hPdiv]
  have hPtwo : 2 ≤ P := hP.two_le
  have h1le_a : 1 ≤ a := by
    -- a * P = p and P ≤ p gives 1 ≤ a  (via p / P ≥ 1 when P ≤ p)
    dsimp [a]
    exact (Nat.le_div_iff_mul_le hPpos).2 (by simpa using hPle_p)
  have h1lt_a : 1 < a := by
    -- a ≥ 1 already; if a = 1 then P = p, contradiction.
    have hane : a ≠ 1 := by
      intro ha1
      apply hPne
      have : 1 * P = p := by simpa [ha1] using haP
      simpa using this
    omega
  exact ⟨a, P, hP, h1lt_a, haP⟩

/-! #print axioms scan -/
#print axioms Cat.descent
#print axioms Cat.prime_sub_factor

end Cat
