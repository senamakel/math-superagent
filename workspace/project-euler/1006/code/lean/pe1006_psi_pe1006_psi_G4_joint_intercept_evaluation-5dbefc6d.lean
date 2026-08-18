import Mathlib

/--
A formal statement of the unresolved G4 node.  The abstract type `State` is the
fixed-dimensional state space; `sigma` constructs the state from the rational
convergent `a` and length `k`; `op` is its associative composition; `eval`
returns the required residue.  `admissible` expresses that `a = p/q` is a
Fibonacci convergent to α with denominator `q > k+2`.  `steps` is logarithmic
in `k`, expressed by a constant `C` and the bound `steps ≤ C * (Nat.log k + 1)`.
-/
def M : ℕ := 101001001

def V (a : ℚ) (m k : ℕ) : ℤ :=
  (Int.floor (a * (m + k + 1)) : ℤ) -
    10 ^ k * (Int.floor (a * m) : ℤ) +
    9 * ∑ j ∈ Finset.range k, (10 ^ (k - 1 - j) : ℤ) * (Int.floor (a * (m + j + 1)) : ℤ)

def Psi (a : ℚ) (k : ℕ) : ℤ := ∑ m ∈ Finset.range (k + 1), V a m k ^ 2

def Admissible (a : ℚ) (k : ℕ) : Prop := ∃ p q : ℕ, a = p / q ∧ k + 2 < q

def JointG4 : Prop :=
  ∃ (State : Type) (sigma : ℚ → ℕ → State) (op : State → State → State)
    (eval : State → ℕ) (steps : ℕ → ℕ) (C : ℕ),
    (∀ x y z : State, op (op x y) z = op x (op y z)) ∧
    (∀ a k : ℚ × ℕ, Admissible a.1 a.2 →
      eval (sigma a.1 a.2) = Int.emod (Psi a.1 a.2) (M : ℤ)) ∧
    (∀ k : ℕ, steps k ≤ C * (Nat.log k + 1)) ∧
    (∀ k : ℕ, ∀ a b : ℚ, Admissible a k → Admissible b k →
      eval (sigma a k) = eval (sigma b k))

/-- The requested G4 joint-intercept evaluation statement. -/
theorem pe1006_psi_G4_joint_intercept_evaluation : JointG4 := by
  sorry

#print axioms pe1006_psi_G4_joint_intercept_evaluation
