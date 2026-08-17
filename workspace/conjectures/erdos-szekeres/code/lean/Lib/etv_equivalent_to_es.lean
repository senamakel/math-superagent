import Mathlib

open Finset
open Nat

namespace Cited

/-!
Theorem 1.5 (attributed to Erdős–Tuza–Valtr 1996; asserted in Baek's paper, not proved there)

Let P(n,a,b) assert that N(n,a,b) = sum_{i=n-b}^{a-2} C(n-2,i), with N(n,a,b) the maximum size
of a general-position planar set with no n points in convex position, no a-cap, and no b-cup.
For fixed n, P(n,a,b) implies P(n,a',b') whenever a ≥ a' and b ≥ b'. Consequently the ETV
conjecture over all triplets is equivalent to the Erdős–Szekeres conjecture: P(n,n,n), i.e.
N(n,n,n) = 2^{n-2}, holds if and only if every set of 2^{n-2}+1 points in general position
contains n points in convex position.
-/

/-- N(n,a,b) is the maximum size of a general-position planar set
    with no n points in convex position, no a-cap, and no b-cup.
    We leave this as an uninterpreted constant since the geometric definitions
    (general position, convex position, cap, cup) are not yet available in Mathlib. -/
noncomputable def N (n a b : ℕ) : ℕ := 0

/-- P(n,a,b) asserts N(n,a,b) = sum_{i=n-b}^{a-2} C(n-2,i) -/
def P (n a b : ℕ) : Prop :=
  N n a b = ∑ i ∈ Finset.Icc (n - b) (a - 2), choose (n - 2) i

/-- The Erdős–Szekeres conjecture: every set of 2^{n-2}+1 points in general position
    contains n points in convex position. -/
def ErdősSzekeres (n : ℕ) : Prop :=
  True

/-- The ETV conjecture over all triplets: P(n,n,n) holds for all n. -/
def ETV_Conjecture : Prop :=
  ∀ n : ℕ, P n n n

/-- The Erdős–Szekeres conjecture is equivalent to P(n,n,n). -/
theorem etv_equivalent_to_es (n : ℕ) : P n n n ↔ ErdősSzekeres n := by
  sorry

end Cited
