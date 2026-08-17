import Mathlib.Data.Finset.Card
import Mathlib.Data.Fin.Basic

abbrev Point := ℤ × ℤ

section spine
variable {m : ℕ}
variable (convexPos : Finset (Fin m) → Prop)
variable (isCup : Finset (Fin m) → Prop)

theorem t (convexPos : Finset (Fin m) → Prop) : True := by trivial
end spine
