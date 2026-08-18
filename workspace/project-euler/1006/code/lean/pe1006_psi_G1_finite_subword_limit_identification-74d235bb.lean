import Mathlib.Data.List.Basic
import Mathlib.Data.Fintype.Card

namespace PE1006PsiG1

abbrev BinaryWord := List Bool

def fibWord : ℕ → BinaryWord
  | 0 => [false]
  | 1 => [false, true]
  | n + 2 => fibWord (n + 1) ++ fibWord n

def wordFactors (w : BinaryWord) (k : ℕ) : Set BinaryWord :=
  {u | ∃ i, i + k ≤ w.length ∧ u = (w.drop i).take k}

def finiteFactors (k : ℕ) : Set BinaryWord :=
  {u | ∃ n, u ∈ wordFactors (fibWord n) k}

def infiniteFibWord (i : ℕ) : Bool :=
  (fibWord (i + 6)).getD i false

def infiniteFactors (k : ℕ) : Set BinaryWord :=
  {u | ∃ i, u = (List.ofFn (fun j : Fin k => infiniteFibWord (i + j)))}

/-- gap
id: fib-prefix-limit
lemma: ∀ i : ℕ, ∀ k : ℕ, ∃ n : ℕ, k + i ≤ (fibWord n).length ∧ (fibWord n).getD (i + j) false = infiniteFibWord (i + j) for all j < k
status: open
next: Prove stabilization of the recursively generated Fibonacci words at every fixed prefix position, preferably by induction on i and k using fibWord length growth.
-/
lemma fib_prefix_limit :
    ∀ i k : ℕ, ∃ n : ℕ, k + i ≤ (fibWord n).length ∧
      ∀ j < k, (fibWord n).getD (i + j) false = infiniteFibWord (i + j) := by
  sorry

/-- gap
id: finite-infinite-factor-equivalence
lemma: finiteFactors k = infiniteFactors k
status: open
next: Use fib_prefix_limit for inclusion finiteFactors ⊆ infiniteFactors and the defining prefix property of the fixed point for the reverse inclusion.
-/
lemma finite_infinite_factor_equivalence (k : ℕ) :
    finiteFactors k = infiniteFactors k := by
  sorry

/-- gap
id: infinite-fibonacci-sturmian-complexity
lemma: ∀ k ≥ 1, (infiniteFactors k).Finite ∧ (infiniteFactors k).card = k + 1
status: open
next: Apply the Fibonacci word's characteristic Sturmian theorem and the Sturmian factor-complexity theorem; formalize or cite the exact hypotheses and bridge definitions.
-/
lemma infinite_fibonacci_sturmian_complexity :
    ∀ k : ℕ, 1 ≤ k → ∃ h : Fintype (infiniteFactors k), Fintype.card (infiniteFactors k) = k + 1 := by
  sorry

theorem finite_subword_limit_identification :
    ∀ k : ℕ, 1 ≤ k → finiteFactors k = infiniteFactors k ∧
      ∃ h : Fintype (infiniteFactors k), Fintype.card (infiniteFactors k) = k + 1 := by
  intro k hk
  constructor
  · exact finite_infinite_factor_equivalence k
  · exact infinite_fibonacci_sturmian_complexity k hk

#print axioms finite_subword_limit_identification

end PE1006PsiG1
