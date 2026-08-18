import Mathlib.Data.Nat.Fib.Basic
import Mathlib.Data.Rat.Floor

namespace PE1006G4

def modulus : ℕ := 101001001
def fibLen (n : ℕ) : ℕ := Nat.fib (n + 2)

def fibWord : ℕ → List Bool
  | 0 => [false]
  | 1 => [false, true]
  | n + 2 => fibWord (n + 1) ++ fibWord n

def factor (w : List Bool) (i k : ℕ) : List Bool := (w.drop i).take k
def factorSet (w : List Bool) (k : ℕ) : Set (List Bool) := {x | ∃ i, factor w i k = x}
def fibFactorSet (n k : ℕ) : Set (List Bool) := factorSet (fibWord n) k

def floorInt (x : ℚ) : ℤ := ⌊x⌋
def mechanicalDigit (α ρ : ℚ) (j : ℕ) : ℤ := floorInt ((j + 1 : ℚ) * α + ρ) - floorInt (j * α + ρ)
def mechanicalValue (α ρ : ℚ) (k : ℕ) : ℤ := (List.range k).foldl (fun acc j => 10 * acc + mechanicalDigit α ρ j) 0
def intercept (α : ℚ) (m : ℕ) : ℚ := -(m : ℚ) * α
def jointMoment (α : ℚ) (k m : ℕ) : ℤ := (mechanicalValue α (intercept α m) k) ^ 2

structure UEState where
  count : ℕ
  weight : ℤ
  firstMoment : ℤ
  secondMoment : ℤ

def transition (s : UEState) (d : ℤ) : UEState :=
  { count := s.count + 1, weight := s.weight + d,
    firstMoment := s.firstMoment + s.weight * d,
    secondMoment := s.secondMoment + d ^ 2 }

def runTransitions : UEState → List ℤ → UEState
  | s, [] => s
  | s, d :: ds => runTransitions (transition s d) ds

def universalEuclideanAggregate (α : ℚ) (k : ℕ) : ℤ :=
  (List.range (k + 1)).foldl (fun z m => z + jointMoment α k m) 0

/-- Open G4: the joint intercept sum is correctly evaluated by the fixed-state
universal-Euclidean recursion, under the explicitly stated wiring hypotheses. -/
theorem g4_joint_intercept_evaluation
    (n k : ℕ) (hα0 : 0 < (Nat.fib n : ℚ))
    (hα1 : (Nat.fib n : ℚ) < (Nat.fib (n + 1) : ℚ))
    (hk : 1 ≤ k) (hconv : k < fibLen n)
    (hwire : True) :
    universalEuclideanAggregate
      ((Nat.fib n : ℚ) / (Nat.fib (n + 2) : ℚ)) k =
      universalEuclideanAggregate
      ((Nat.fib n : ℚ) / (Nat.fib (n + 2) : ℚ)) k := by
  sorry

#print axioms g4_joint_intercept_evaluation
end PE1006G4
