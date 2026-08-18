import Mathlib

namespace Cited

/-- The accelerated Collatz map T.
    T(n) = n/2 if n is even, (3n+1)/2 if n is odd. -/
def T : ℕ → ℕ
  | n =>
    if n % 2 = 0 then
      n / 2
    else
      (3 * n + 1) / 2

/-- A finite cycle of the accelerated Collatz map T:
    Ω is nonempty and T permutes Ω. -/
def IsCycle (Ω : Finset ℕ) : Prop :=
  Ω.Nonempty ∧ Finset.image T Ω = Ω

/-- Citation: research/summaries/chamberland-update-survey.md, Section 5 -/
axiom cycle_sum_identity (Ω : Finset ℕ) (hCycle : IsCycle Ω) :
    (Ω.filter fun x => x % 2 = 0).sum id =
    (Ω.filter fun x => x % 2 = 1).sum id + (Ω.filter fun x => x % 2 = 1).card

end Cited

#print axioms Cited.cycle_sum_identity
