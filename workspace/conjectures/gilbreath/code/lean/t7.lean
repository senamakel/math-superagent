import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

#check Even
#check Even.elim
example (e : ℕ) (he : Even e) : True := by
  rcases he with ⟨m, hm⟩
  -- what is the witness form?
  trace_state
  trivial
