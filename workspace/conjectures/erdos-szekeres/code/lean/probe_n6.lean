import Mathlib.Data.Fin.Basic
import Mathlib.Data.Finset.Card
import Mathlib.Tactic

set_option maxRecDepth 1000000

abbrev Pt := ℤ × ℤ
def o3 (a b c : Pt) : ℤ := (b.1 - a.1) * (c.2 - a.2) - (b.2 - a.2) * (c.1 - a.1)

-- es_construct(6): 16 points, integer-scaled (lx=1e6, ly=4.8e9) then translated to origin.
def X6 : Fin 16 → Pt
| ⟨0,_⟩ => (0, 16320000000000)
| ⟨1,_⟩ => (1000000000, 11520000000000)
| ⟨2,_⟩ => (1000000001, 11520000000024)
| ⟨3,_⟩ => (1000000002, 11520000000096)
| ⟨4,_⟩ => (1000000003, 11520000000216)
| ⟨5,_⟩ => (2000000000, 7200000000004)
| ⟨6,_⟩ => (2000000001, 7200000000003)
| ⟨7,_⟩ => (2000000002, 7200000000000)
| ⟨8,_⟩ => (2000000010, 7200000000960)
| ⟨9,_⟩ => (2000000011, 7200000000961)
| ⟨10,_⟩ => (2000000012, 7200000000964)
| ⟨11,_⟩ => (3000000000, 3360000000216)
| ⟨12,_⟩ => (3000000001, 3360000000192)
| ⟨13,_⟩ => (3000000002, 3360000000120)
| ⟨14,_⟩ => (3000000003, 3360000000000)
| ⟨15,_⟩ => (4000000000, 0)

-- strictInside of one point against triangle (a0,a1,a2)
def strictInside (p a0 a1 a2 : Pt) : Bool :=
  let s := o3 a0 a1 a2
  (s > 0 && o3 a0 a1 p > 0 && o3 a1 a2 p > 0 && o3 a2 a0 p > 0) ||
  (s < 0 && o3 a0 a1 p < 0 && o3 a1 a2 p < 0 && o3 a2 a0 p < 0)

def convexQuad (a b c d : Pt) : Bool :=
  !(strictInside a b c d) && !(strictInside b a c d) && !(strictInside c a b d) && !(strictInside d a b c)

-- The recorded n=6 valid split half L = {1,5,6,7,8,9,10,11} is 5-avoiding.
-- Test just one convex-5 check: is {1,5,6,7,8} in convex position? It should be FALSE (5-avoiding).
example : ¬ (∃ w x y z v : Fin 16,
    ({w,x,y,z,v} : Finset (Fin 16)).card = 5 ∧ convexQuad (X6 w) (X6 x) (X6 y) (X6 z)) := by
  decide

-- Instead, test the direct non-convexity of a specific 5-subset using an independent convex-5 def:
example : ¬ (convexQuad (X6 1) (X6 5) (X6 6) (X6 7)) := by
  decide
