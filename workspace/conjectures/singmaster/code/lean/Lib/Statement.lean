import Mathlib.Data.Nat.Choose.Basic
import Mathlib.Data.Set.Card

/-!
# Singmaster's conjecture — Lean statement

`N(a)` counts how many times the integer `a` appears in Pascal's triangle.
We count **every** ordered pair `(n, k)` with `0 ≤ k ≤ n` and `C(n,k) = a`
— both mirrors `(n,k)` and `(n,n-k)` and the trivial pair `C(a,1)=C(a,a-1)`
are counted separately.  This is the "both-mirrors-plus-trivial-pair"
convention under which `N(3003) = 8`.

The conjecture: there is an absolute constant `B` with `N(a) ≤ B` for every
`a > 1`.
-/

/-- The set of occurrences of `a` in Pascal's triangle: pairs `(n,k)` with
  `0 ≤ k ≤ n` and `C(n,k) = a`.  Both mirror entries and the trivial pair are
  included, each as a distinct pair. -/
def occurrences (a : ℕ) : Set (ℕ × ℕ) :=
  { p | p.2 ≤ p.1 ∧ Nat.choose p.1 p.2 = a }

/-- `N(a)` = number of times `a` appears in Pascal's triangle, counting both
  mirrors and the trivial pair `C(a,1)=C(a,a-1)`.  (`Set.ncard` returns a
  natural: for `a > 1` the occurrence set is finite; were it infinite the
  value would be 0, but finiteness for `a > 1` is a theorem of this library,
  not asserted here.) -/
noncomputable def N (a : ℕ) : ℕ :=
  (occurrences a).ncard

/-- Singmaster's conjecture (1971): the number of times an integer appears in
  Pascal's triangle is bounded by an absolute constant independent of the
  integer.

  Concretely: there exists a natural `B` such that, for every `a > 1`,
  `N(a) ≤ B` — where `N(a)` counts both mirrors and the trivial pair
  `C(a,1) = C(a,a-1)`, so `N(3003) = 8`. -/
theorem singmaster_conjecture :
    ∃ B : ℕ, ∀ a : ℕ, 1 < a → N a ≤ B := by
  sorry

#check Nat.choose_one_right
#check Nat.choose_symm
#check Nat.choose_pos

#print axioms singmaster_conjecture
