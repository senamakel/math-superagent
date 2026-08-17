import Mathlib.Data.Fin.Basic
import Mathlib.Data.Finset.Card
import Mathlib.Tactic

abbrev Pt := ℤ × ℤ

def o3 (a b c : Pt) : ℤ := (b.1 - a.1) * (c.2 - a.2) - (b.2 - a.2) * (c.1 - a.1)

-- es_construct(5): 8 points, integer-scaled (lx=1e6, ly=1.2e8) then translated to origin.
def X5 : Fin 8 → Pt
| ⟨0,_⟩ => (0, 324000000000)
| ⟨1,_⟩ => (1000000000, 204000000000)
| ⟨2,_⟩ => (1000000001, 204000000001)
| ⟨3,_⟩ => (1000000002, 204000000004)
| ⟨4,_⟩ => (2000000000, 96000000004)
| ⟨5,_⟩ => (2000000001, 96000000003)
| ⟨6,_⟩ => (2000000002, 96000000000)
| ⟨7,_⟩ => (3000000000, 0)

-- general position: no three collinear
def gp5 : Prop :=
  ∀ a b c : Fin 8, a ≠ b → a ≠ c → b ≠ c → o3 (X5 a) (X5 b) (X5 c) ≠ 0

example : gp5 := by
  decide

-- strict-left side predicate on indices i: i strictly left of directed line a->b
def leftOf (a b : Fin 8) (i : Fin 8) : Bool := o3 (X5 a) (X5 b) (X5 i) > 0

-- strictly-inside test for 4-point convex position
def strictInside (p a0 a1 a2 : Pt) : Bool :=
  let s := o3 a0 a1 a2
  (s > 0 && o3 a0 a1 p > 0 && o3 a1 a2 p > 0 && o3 a2 a0 p > 0) ||
  (s < 0 && o3 a0 a1 p < 0 && o3 a1 a2 p < 0 && o3 a2 a0 p < 0)

def convexQuad (a b c d : Pt) : Bool :=
  !(strictInside a b c d) && !(strictInside b a c d) && !(strictInside c a b d) && !(strictInside d a b c)

-- The 4 valid n=5 split halves (from the verified computation):
-- {1,4,5,6},{0,2,3,7},{0,5,6,7},{1,2,3,4}
-- each is 4-avoiding (NOT convex position)
example : !(convexQuad (X5 1) (X5 4) (X5 5) (X5 6)) := by decide
example : !(convexQuad (X5 0) (X5 2) (X5 3) (X5 7)) := by decide
example : !(convexQuad (X5 0) (X5 5) (X5 6) (X5 7)) := by decide
example : !(convexQuad (X5 1) (X5 2) (X5 3) (X5 4)) := by decide
