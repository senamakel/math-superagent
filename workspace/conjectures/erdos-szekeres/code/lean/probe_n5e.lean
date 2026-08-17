import Mathlib.Data.Fin.Basic
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

def gp5 : Prop :=
  ∀ a b c : Fin 8, a ≠ b → a ≠ c → b ≠ c → o3 (X5 a) (X5 b) (X5 c) ≠ 0

#synth Decidable (o3 (X5 0) (X5 1) (X5 2) ≠ 0)
#synth Decidable (∀ x : Fin 8, x ≠ 0)

-- try providing decidable instances
example : Decidable gp5 := by
  infer_instance
