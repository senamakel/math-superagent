import Mathlib.Data.Nat.Basic

namespace PE1006G4BlockState

abbrev Summary := Nat × Nat × Nat

def summary (w : List ℕ) : Summary :=
  (w.length, w.sum, (w.map (fun x => x * x)).sum)
def cross (u v : List ℕ) : ℕ :=
  (u.getLastD 0) * (v.headD 0)

/-- The k=2 summary `(count,sum,sumsq)` loses the boundary data needed by
rolling concatenation: equal summaries can have unequal cross terms. -/
theorem k2_summary_nonclosure :
    summary [0, 1] = summary [1, 0] ∧
    cross [0, 1] [1] ≠ cross [1, 0] [1] := by
  constructor
  · rfl
  · decide

#print axioms k2_summary_nonclosure
end PE1006G4BlockState
