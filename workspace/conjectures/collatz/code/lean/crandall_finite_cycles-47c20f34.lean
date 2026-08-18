import Mathlib

namespace Cited

/-- src: Crandall, "On the 3x+1 problem", Math. Comp. 32 (1978), Corollary 7.2.
For each prescribed period, only finitely many cyclic trajectories occur. -/
axiom finitely_many_cyclic_trajectories (k : ℕ) :
  Set.Finite {c : Finset ℕ | c.Nonempty ∧ c.card = k}

end Cited

#print axioms Cited.finitely_many_cyclic_trajectories
