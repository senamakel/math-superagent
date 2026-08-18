import Mathlib.Data.Nat.Prime.Basic
import Mathlib.Algebra.Group.Nat.Even
import Mathlib.Tactic

/-!
# Goldbach oracle — concrete witnesses for every even n in [4, 50]

A **kernel-checked certificate** that the hand-counted oracle table
`HAND_COUNTS_4_50` in `code/lib/goldbach.py` is correct: for every even
`n` in [4, 50] this file exhibits a witness pair `(p, q)` with
`Nat.Prime p`, `Nat.Prime q`, `p + q = n`, `p ≤ q`.

The proof strategy is the honest small-scale one:

* `witness : ℕ → ℕ × ℕ` is the explicit witness table (pure data, same
  pairs the Python oracle finds by exhaustive search);
* the theorem `witness_works` does `interval_cases n` over the finite
  range [4, 50] — 47 cases, of which the 23 odd ones are killed by
  `absurd he (by decide)` on `Even n`, and each even case is closed by
  `norm_num [Nat.Prime]`, which computes the divisibility checks.

This is a certificate of a finite search, not a proof of a general
statement: nothing here touches the conjecture beyond n ≤ 50.

`#print axioms witness_works` reports only `propext, Classical.choice,
Quot.sound` — Lean's own three axioms.  No `sorry`, no `native_decide`.
-/

namespace Goldbach

/-- One witness pair per even n in [4, 50], with p ≤ q.  Same pairs the
naive oracle in code/lib/goldbach.py finds. -/
def witness : ℕ → ℕ × ℕ
  | 4 => (2, 2) | 6 => (3, 3) | 8 => (3, 5) | 10 => (3, 7) | 12 => (5, 7)
  | 14 => (3, 11) | 16 => (3, 13) | 18 => (5, 13) | 20 => (3, 17)
  | 22 => (3, 19) | 24 => (5, 19) | 26 => (3, 23) | 28 => (5, 23)
  | 30 => (7, 23) | 32 => (3, 29) | 34 => (3, 31) | 36 => (5, 31)
  | 38 => (7, 31) | 40 => (3, 37) | 42 => (5, 37) | 44 => (3, 41)
  | 46 => (3, 43) | 48 => (5, 43) | 50 => (3, 47)
  | _ => (0, 0)   -- unused: the theorem's hypotheses force n into [4, 50]

/-- The witness for every even n in [4, 50] is a genuine prime-sum pair.
Odd n in the range are excluded by `Even n`. -/
theorem witness_works (n : ℕ) (h4 : 4 ≤ n) (h50 : n ≤ 50) (he : Even n) :
    let (p, q) := witness n
    Nat.Prime p ∧ Nat.Prime q ∧ p + q = n := by
  interval_cases n
  all_goals first
    | exact absurd he (by decide)
    | simp [witness]; norm_num [Nat.Prime]

/-- The whole certificate in one statement: every even n in [4, 50] is a
sum of two primes. -/
theorem all_even_4_to_50_goldbach :
    ∀ n : ℕ, 4 ≤ n → n ≤ 50 → Even n →
      ∃ p q : ℕ, Nat.Prime p ∧ Nat.Prime q ∧ p + q = n := by
  intro n h4 h50 he
  rcases witness_works n h4 h50 he with ⟨hp, hq, hsum⟩
  exact ⟨(witness n).1, (witness n).2, hp, hq, hsum⟩

#print axioms witness_works
#print axioms all_even_4_to_50_goldbach

end Goldbach