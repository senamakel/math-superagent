import Mathlib.Data.Fin.Basic
import Mathlib.Data.Finset.Card
import Mathlib.Tactic
import Mathlib.Data.Nat.Basic

set_option maxRecDepth 1000000

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

-- A pair of halves (L, R) is a "valid split" iff
--   L and R partition the 8 points,
--   L is a strict-left open half-plane side of some directed pair,
--   each half has size 4, and neither half is in convex position (both 4-avoiding).
-- We state it via witnesses; kernel `decide` will check.

def convexQuad (a b c d : Pt) : Bool :=
  let sis := fun p a0 a1 a2 : Pt =>
    (o3 a0 a1 a2 > 0 && o3 a0 a1 p > 0 && o3 a1 a2 p > 0 && o3 a2 a0 p > 0) ||
    (o3 a0 a1 a2 < 0 && o3 a0 a1 p < 0 && o3 a1 a2 p < 0 && o3 a2 a0 p < 0)
  !(sis a b c d) && !(sis b a c d) && !(sis c a b d) && !(sis d a b c)

-- concrete valid split: L = {1,4,5,6}, R = {0,2,3,7}, L is strict-left of (7,2)
def L : Finset (Fin 8) := {1, 4, 5, 6}
def R : Finset (Fin 8) := {0, 2, 3, 7}

example : L = {1,4,5,6} := by
  decide

example : L.card = 4 := by
  decide

example : R.card = 4 := by
  decide

example : L ∩ R = ∅ := by
  decide

example : ¬ (convexQuad (X5 1) (X5 4) (X5 5) (X5 6)) := by
  decide

example : ¬ (convexQuad (X5 0) (X5 2) (X5 3) (X5 7)) := by
  decide

-- L is strict-left of directed pair (7,2), i.e. x ∈ L iff o3 X7 X2 x > 0
example : L = Finset.univ.filter (fun x : Fin 8 => o3 (X5 7) (X5 2) (X5 x) > 0) := by
  decide

#print axioms convexQuad
