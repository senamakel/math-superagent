import Mathlib.Data.Finset.Card
import Mathlib.Data.Fin.Basic

abbrev Point := ℤ × ℤ

section spine

variable {m : ℕ}

variable (convexPos : Finset (Fin m) → Prop)

variable (isCup : Finset (Fin m) → Prop)

variable (isCap : Finset (Fin m) → Prop)

variable (sameExtremes : Finset (Fin m) → Finset (Fin m) → Prop)

variable (hSharedTwo : ∀ C D : Finset (Fin m), sameExtremes C D → (C ∩ D).card = 2)

theorem union_card_shared_two {C D : Finset (Fin m)} {k n : ℕ}
    (h2k : 2 ≤ k) (hkn : k ≤ n)
    (hC : C.card = k) (hD : D.card = n + 2 - k) (hCD : (C ∩ D).card = 2) :
    (C ∪ D).card = n := by
  have hmain : (C ∪ D).card + (C ∩ D).card = C.card + D.card := by
    exact Finset.card_union_add_card_inter C D
  rw [hC, hD, hCD] at hmain
  omega

end spine
