import Mathlib.Data.Nat.Choose.Factorization
import Mathlib.Tactic

-- Probe: Function.iterate composition decomposition
#check Function.iterate_add
#check Function.iterate_zero
#check Function.iterate_succ
#check Function.iterate_succ'
#check Function.iterate_self
example (α : Type) (f : α → α) (a b : ℕ) : f^[a + b] = f^[b] ∘ f^[a] :=
  Function.iterate_add f a b
example (α : Type) (f : α → α) (a b : ℕ) (x : α) : f^[a + b] x = f^[b] (f^[a] x) := by
  rw [Function.iterate_add]

-- char 2: x + x = 0 in ZMod 2
example (x : ZMod 2) : x + x = 0 := by
  have h : (2 : ZMod 2) = 0 := by norm_num
  calc x + x = (2 : ZMod 2) * x := by ring
       _ = 0 := by simp [h]

-- (2^k : ZMod (2^k)) = 0
example (k : ℕ) : (2 ^ k : ZMod (2 ^ k)) = 0 := by
  exact ZMod.natCast_self (2 ^ k)

-- natCast_add hygiene in ZMod
example (P : ℕ) (a b : ℕ) (i : ZMod P) : i + (a : ZMod P) + (b : ZMod P) = i + ((a + b) : ZMod P) := by
  rw [← add_assoc]
  rw [← Nat.cast_add]
