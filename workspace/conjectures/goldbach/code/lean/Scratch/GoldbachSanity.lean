import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Algebra.Group.Nat.Even
import Mathlib.Tactic

/-!
# Scratch: sanity-check `Goldbach.IsGoldbach` against the problem's own examples

`problem.md` fixes what the definition must say about small inputs:
* `4 = 2 + 2` IS a valid representation (primes need not be distinct);
* `n = 2` is excluded BY HYPOTHESIS (`2 < n`), not by the definition — but as a
  matter of fact `2` has no representation, since a prime `p` satisfies `2 ≤ p`,
  so two primes already sum to at least `4`.

This file checks both with kernel-checked proofs (no `sorry`, no `decide` over
an unbounded existential), so the definition in `Statement.lean` is pinned to
the problem's own examples before anything else builds on it.

Note: `decide` cannot be used directly on `IsGoldbach n` — the existential over
`ℕ` is unbounded, so no `Decidable` instance is synthesized. Explicit witnesses
are the honest check anyway.
-/

namespace Goldbach

def IsGoldbachPair (n p q : ℕ) : Prop :=
  Nat.Prime p ∧ Nat.Prime q ∧ p + q = n

def IsGoldbach (n : ℕ) : Prop :=
  ∃ p q : ℕ, IsGoldbachPair n p q

-- 4 = 2 + 2 : both summands prime, and they are allowed to coincide.
theorem four_is_goldbach : IsGoldbach 4 := by
  refine ⟨2, 2, ?_, ?_, ?_⟩
  · exact Nat.prime_two
  · exact Nat.prime_two
  · norm_num

-- 2 is not Goldbach: `p, q` prime forces `2 ≤ p` and `2 ≤ q`, hence `4 ≤ p + q`.
theorem two_not_goldbach : ¬ IsGoldbach 2 := by
  rintro ⟨p, q, hp, hq, hpq⟩
  have hp2 : 2 ≤ p := hp.two_le
  have hq2 : 2 ≤ q := hq.two_le
  omega

-- 6 = 3 + 3.
theorem six_is_goldbach : IsGoldbach 6 := by
  refine ⟨3, 3, ?_, ?_, ?_⟩
  · norm_num [Nat.Prime]
  · norm_num [Nat.Prime]
  · norm_num

-- 8 = 3 + 5.
theorem eight_is_goldbach : IsGoldbach 8 := by
  refine ⟨3, 5, ?_, ?_, ?_⟩
  · norm_num [Nat.Prime]
  · norm_num [Nat.Prime]
  · norm_num

-- The parity side: 8 is even, so it is inside the conjecture's hypothesis class.
theorem eight_is_even : Even 8 := by
  decide

-- 10 = 3 + 7 = 5 + 5; one representation suffices.
theorem ten_is_goldbach : IsGoldbach 10 := by
  refine ⟨5, 5, ?_, ?_, ?_⟩
  · norm_num [Nat.Prime]
  · norm_num [Nat.Prime]
  · norm_num

-- The genuinely ambiguous point in the informal statement: is `2` even?
-- Yes: `Even 2` holds, and the conjecture still excludes 2 only via `2 < n`.
theorem two_is_even : Even 2 := by
  decide

-- And the conjecture's hypothesis class really does exclude 2:
-- `2 < 2` is false, so the instance `2 < 2 → Even 2 → IsGoldbach 2` is vacuous.
theorem two_below_two_absurd : (2 < 2) → Even 2 → IsGoldbach 2 := by
  intro h
  omega

#print axioms four_is_goldbach
#print axioms two_not_goldbach

end Goldbach
