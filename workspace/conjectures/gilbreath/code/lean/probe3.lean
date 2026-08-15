import Mathlib.Data.Nat.Dist
import Mathlib.Tactic

def countOnes : List Nat → Nat
  | [] => 0
  | e :: rest => (if e = 1 then 1 else 0) + countOnes rest

example (w c : Nat) : (w - 1) - c = w - (1 + c) := by omega

example (w c : Nat) : (w - 1) - c = w - (1 + c) := by
  rw [Nat.sub_sub]
  simp [Nat.add_assoc, Nat.add_comm, Nat.add_left_comm]

example (w : Nat) (hw : countOnes ([1]) + 1 < w) (c := countOnes ([] : List Nat)) : True := by
  trivial

-- the full sub-goal shape from run_high e=1 branch
example (w : Nat) (h : 1 + countOnes ([] : List Nat) + 1 < w) :
    (w - 1) - countOnes ([] : List Nat) = w - (1 + countOnes ([] : List Nat)) := by
  omega

-- run_high target directly on a small concrete pattern
example : runAbs_placeholder := by
  -- not real; just checking omega arithmetic for the goal
  let rest : List Nat := []
  let w : Nat := 5
  let c := countOnes rest
  have : (4) - c = 5 - (1 + c) := by omega
  trivial

-- check omega closes with an explicit rewrite of countOnes
example (rest : List Nat) (w : Nat)
    (hw : countOnes rest + 1 < w - 1) :
    (w - 1) - countOnes rest = w - (1 + countOnes rest) := by
  omega

-- test the specific failing shape: does omega need bounds on w?
example (w : Nat) (hw : countOnes ([] : List Nat) + 1 < w - 1) :
    (w - 1) - countOnes ([] : List Nat) = w - (1 + countOnes ([] : List Nat)) := by
  omega
