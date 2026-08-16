import Mathlib.Data.Nat.GCD.Basic

example : Nat.Coprime 9 7 := by
  decide

example : Nat.Coprime 9 25 := by
  decide

example : Nat.Coprime (7*11) 13 := by
  decide

example : Nat.Coprime 9 (7*11*31*151*331) := by
  decide

example : Nat.Coprime (3^2) (7*11*31*151*331) := by
  decide
