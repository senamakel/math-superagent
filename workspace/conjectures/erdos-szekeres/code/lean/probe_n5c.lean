import Mathlib.Data.Fin.Basic
import Mathlib.Data.Finset.Card
import Mathlib.Tactic

abbrev Pt := ℤ × ℤ

def o3 (a b c : Pt) : ℤ := (b.1 - a.1) * (c.2 - a.2) - (b.2 - a.2) * (c.1 - a.1)

-- es_construct(5), integer-scaled then translated to origin
def X5 : Fin 8 → Pt
| ⟨0,_⟩ => (0, 324000000000)
| ⟨1,_⟩ => (1000000000, 204000000000)
| ⟨2,_⟩ => (1000000001, 204000000001)
| ⟨3,_⟩ => (1000000002, 204000000004)
| ⟨4,_⟩ => (2000000000, 96000000004)
| ⟨5,_⟩ => (2000000001, 96000000003)
| ⟨6,_⟩ => (2000000002, 96000000000)
| ⟨7,_⟩ => (3000000000, 0)

-- strictly left side: index x is strict-left of directed line a->b
def leftOf (a b x : Fin 8) : Bool := (o3 (X5 a) (X5 b) (X5 x)) > 0

def sides5 : Finset (Finset (Fin 8)) :=
  (Finset.univ : Finset (Fin 8 × Fin 8)).biUnion (fun p =>
    let a := p.1; let b := p.2
    if a = b then ∅ else
    let s : Finset (Fin 8) := Finset.univ.filter (fun x => leftOf a b x)
    if 0 < s.card ∧ s.card < 8 then {s} else ∅)

#eval (sides5).card

example : sides5.card = 8 * (8 - 1) := by
  native_decide
