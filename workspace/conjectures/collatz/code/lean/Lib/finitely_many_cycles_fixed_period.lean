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

/-- Source: Crandall 1978, Math. Comp. 32, 1281-1292, Corollary 7.2; see also
    research/summaries/crandall-1978-on-the-3x1-problem-ams.md. -/
axiom finitely_many_cycles_fixed_period (k : ℕ) :
  Set.Finite {Ω : Finset ℕ | Ω.card = k ∧ IsCycle Ω}

end Cited

#print axioms Cited.finitely_many_cycles_fixed_period
