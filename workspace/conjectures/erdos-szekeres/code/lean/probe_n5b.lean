import Mathlib.Data.Fin.Basic
import Mathlib.Tactic

abbrev Pt := ℤ × ℤ

def o3 (a b c : Pt) : ℤ := (b.1 - a.1) * (c.2 - a.2) - (b.2 - a.2) * (c.1 - a.1)

-- es_construct(5), translated to min origin, scaled to integers (lx=1e6, ly=1.2e8 then translate)
def X5 : Fin 8 → Pt
| ⟨0,_⟩ => (0, 324000000000)
| ⟨1,_⟩ => (1000000000, 204000000000)
| ⟨2,_⟩ => (1000000001, 204000000001)
| ⟨3,_⟩ => (1000000002, 204000000004)
| ⟨4,_⟩ => (2000000000, 96000000004)
| ⟨5,_⟩ => (2000000001, 96000000003)
| ⟨6,_⟩ => (2000000002, 96000000000)
| ⟨7,_⟩ => (3000000000, 0)

-- strictly-inside test: p is strictly inside triangle of (a0,a1,a2)
def strictInside (p a0 a1 a2 : Pt) : Bool :=
  let s := o3 a0 a1 a2
  (s > 0 && o3 a0 a1 p > 0 && o3 a1 a2 p > 0 && o3 a2 a0 p > 0) ||
  (s < 0 && o3 a0 a1 p < 0 && o3 a1 a2 p < 0 && o3 a2 a0 p < 0)

-- 4 points in convex position iff no one is strictly inside the triangle of the others
def convexQuad (a b c d : Pt) : Bool :=
  !(strictInside a b c d) && !(strictInside b a c d) && !(strictInside c a b d) && !(strictInside d a b c)

-- half {1,4,5,6} should NOT be convex (4-avoiding)
example : !(convexQuad (X5 1) (X5 4) (X5 5) (X5 6)) := by
  native_decide

#eval convexQuad (X5 1) (X5 4) (X5 5) (X5 6)
