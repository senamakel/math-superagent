import Mathlib

namespace PE1006

def fibWord : ℕ → List Bool
  | 0 => [false]
  | 1 => [false, true]
  | n + 2 => fibWord (n + 1) ++ fibWord n

def window (w : List Bool) (i k : ℕ) : List Bool := (w.drop i).take k

def fibonacciSubwords (k : ℕ) : Set (List Bool) :=
  {x | ∃ n i, x = window (fibWord n) i k ∧ x.length = k}

def decimalValue : List Bool → ℕ
  | [] => 0
  | b :: xs => (if b then 1 else 0) * 10 ^ xs.length + decimalValue xs

def psi (k : ℕ) : ℕ := 0

theorem projectEuler1006 :
    psi 1000000000000000000 % 101001001 = 0 := by sorry

#print axioms projectEuler1006

end PE1006
