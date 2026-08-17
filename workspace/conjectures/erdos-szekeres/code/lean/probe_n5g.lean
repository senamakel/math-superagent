import Mathlib.Data.Fin.Basic
import Mathlib.Data.Finset.Card
import Mathlib.Tactic

abbrev Pt := ℤ × ℤ
def o3 (a b c : Pt) : ℤ := (b.1 - a.1) * (c.2 - a.2) - (b.2 - a.2) * (c.1 - a.1)

def X5 : Fin 8 → Pt
| ⟨0,_⟩ => (0, 324000000000)
| ⟨1,_⟩ => (1000000000, 204000000000)
| ⟨2,_⟩ => (1000000001, 204000000001)
| ⟨3,_⟩ => (1000000002, 204000000004)
| ⟨4,_⟩ => (2000000000, 96000000004)
| ⟨5,_⟩ => (2000000001, 96000000003)
| ⟨6,_⟩ => (2000000002, 96000000000)
| ⟨7,_⟩ => (3000000000, 0)

def strictInside (p a0 a1 a2 : Pt) : Bool :=
  let s := o3 a0 a1 a2
  (s > 0 && o3 a0 a1 p > 0 && o3 a1 a2 p > 0 && o3 a2 a0 p > 0) ||
  (s < 0 && o3 a0 a1 p < 0 && o3 a1 a2 p < 0 && o3 a2 a0 p < 0)

def convexQuad (a b c d : Pt) : Bool :=
  !(strictInside a b c d) && !(strictInside b a c d) && !(strictInside c a b d) && !(strictInside d a b c)

-- A 4-point half (as a Finset of indices) is 4-avoiding iff its points are NOT in convex position.
def halfAvoids4 (S : Finset (Fin 8)) : Prop :=
  ¬ (∃ a b c d : Fin 8, a ∈ S ∧ b ∈ S ∧ c ∈ S ∧ d ∈ S ∧
       ({a,b,c,d} : Finset (Fin 8)).card = 4 ∧ convexQuad (X5 a) (X5 b) (X5 c) (X5 d))

-- Line-separability of a half S: S is exactly the strict-left side of some directed pair (a,b).
-- (Here a,b are the two boundary points of the separating line, both assigned strictly.)
def isStrictLeftSide (S : Finset (Fin 8)) : Prop :=
  ∃ a b : Fin 8, a ≠ b ∧ S = Finset.univ.filter (fun x : Fin 8 => o3 (X5 a) (X5 b) (X5 x) > 0)

-- The canonical n=5 half L = {1,4,5,6}; its complement R = {0,2,3,7}.
def L5 : Finset (Fin 8) := {2, 0, 3, 7}

example : L5.card = 4 := by native_decide

-- strict-left side witness (7,2): strict left set = {1,4,5,6}?  Wait L5={0,2,3,7}.
-- From the python print: strict-left realized by (7,2) gives {1,4,5,6}. So let's define that as a half.
def H7 : Finset (Fin 8) := {1, 4, 5, 6}

example : H7.card = 4 := by native_decide

-- is H7 a strict left side of (7,2)?
example : isStrictLeftSide H7 := by
  refine ⟨7, 2, ?_, ?_⟩
  · native_decide
  · native_decide

#print axioms isStrictLeftSide
