import Mathlib.Data.ZMod.Basic
import Mathlib.Tactic

example : (2 : ZMod 2) = 0 := by
  exact CharP.cast_eq_zero (ZMod 2) 2

example (x : ZMod 2) : x + x = 0 := by
  have h : (2 : ZMod 2) = 0 := CharP.cast_eq_zero (ZMod 2) 2
  rw [← two_mul]
  rw [h]
  simp

-- generic char-2 ring: (x+y)+(x+y)=0
example (R : Type) [CommRing R] [CharP R 2] (x y : R) : (x + y) + (x + y) = 0 := by
  have h : (2 : R) = 0 := CharP.cast_eq_zero R 2
  rw [← two_mul]
  rw [h]
  simp

-- alternate: use @CharP.cast_eq_zero
