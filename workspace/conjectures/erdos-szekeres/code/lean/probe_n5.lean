import Mathlib.Data.Fin.Basic
import Mathlib.Tactic

-- orientation determinant of triple given as integer points in a concrete list
def X5 : Fin 8 → ℤ × ℤ
| ⟨0,_⟩ => (0, 324000000000)
| ⟨1,_⟩ => (1000000000, 204000000000)
| ⟨2,_⟩ => (1000000001, 204000000001)
| ⟨3,_⟩ => (1000000002, 204000000004)
| ⟨4,_⟩ => (2000000000, 96000000004)
| ⟨5,_⟩ => (2000000001, 96000000003)
| ⟨6,_⟩ => (2000000002, 96000000000)
| ⟨7,_⟩ => (3000000000, 0)

def or3 (P : Fin 8 → ℤ × ℤ) (a b c : Fin 8) : ℤ :=
  ((P b).1 - (P a).1) * ((P c).2 - (P a).2) - ((P b).2 - (P a).2) * ((P c).1 - (P a).1)

-- test: is point 0 strictly inside triangle (1,4,5)? expect False (should not be)
#eval or3 X5 1 4 5
#eval or3 X5 4 5 1
#eval or3 X5 5 1 4

example : (or3 X5 1 4 5 > 0) := by native_decide
