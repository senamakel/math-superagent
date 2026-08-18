import Mathlib

open Language

/- Cassaigne, Complexité des facteurs spéciaux dans les mots sturmiens, 1997, p. 68.
   "Soit u un mot sturmien sur un alphabet à deux lettres (un mot infini binaire
   apériodique équilibré : deux facteurs quelconques de longueur n ont des effectifs
   de la lettre 1 qui diffèrent d'au plus 1). Alors u possède exactement n+1 facteurs
   distincts de longueur n pour tout n ≥ 0."
-/

namespace Cited

/-- A Sturmian word over a two-letter alphabet has exactly n+1 distinct factors
of length n for every n ≥ 0. -/
axiom sturmian_complexity_n_plus_one {α : Type} [DecidableEq α] (u : ℕ → α)
    (h_balanced : ∀ n : ℕ, ∀ p q : ℕ,
      ((Finset.filter (λ a => a = u p)
        (Finset.image (λ i : ℕ => u (p + i)) (Finset.range n))).card : ℤ) ≤
      ((Finset.filter (λ a => a = u q)
        (Finset.image (λ i : ℕ => u (q + i)) (Finset.range n))).card : ℤ) + 1)
    (h_aperiodic : ∀ p q : ℕ, p ≠ q → u p ≠ u q) :
    ∀ n : ℕ, (Finset.image (λ i : ℕ => u i) (Finset.range n)).card = n + 1

end Cited
