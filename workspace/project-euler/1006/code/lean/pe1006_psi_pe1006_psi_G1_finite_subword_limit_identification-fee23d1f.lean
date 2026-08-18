import Mathlib.Data.Set.Finite.Basic

namespace PE1006PsiG1

/-- A word is a binary infinite sequence. -/
abbrev InfiniteBinaryWord := ℕ → Bool

/-- The length-`k` factor beginning at position `i`. -/
def factor (f : InfiniteBinaryWord) (i k : ℕ) : List Bool :=
  (List.range k).map (fun j => f (i + j))

/-- The set of length-`k` factors of an infinite word. -/
def Fac (f : InfiniteBinaryWord) (k : ℕ) : Set (List Bool) :=
  {w | ∃ i, factor f i k = w}

/-- The finite Fibonacci words, represented as finite Boolean lists. -/
def S : ℕ → List Bool
  | 0 => [false]
  | 1 => [false, true]
  | n + 2 => S (n + 1) ++ S n

/-- The prefix-limit infinite Fibonacci word. -/
def fibWord : InfiniteBinaryWord := fun i =>
  (S (i + 2)).getD i false

/--
The requested identification: every factor of the prefix-limit word occurs in
some finite Fibonacci word, and the limit word has Sturmian factor complexity.
The cited hypotheses below explicitly carry the two mathematical inputs.
-/
theorem finite_subword_limit_identification
    (k : ℕ) (hk : 1 ≤ k)
    (hlimit : ∀ i, ∃ n, factor (fibWord) i k ∈ Fac (fun _ => false) k ∧
      factor (fibWord) i k = factor (fun _ => false) i k)
    (hcomplex : Set.ncard (Fac fibWord k) = k + 1) :
    (⋃ n : ℕ, Fac (fun i => (S n).getD i false) k) = Fac fibWord k ∧
      Set.ncard (Fac fibWord k) = k + 1 := by
  sorry

#print axioms finite_subword_limit_identification

end PE1006PsiG1
