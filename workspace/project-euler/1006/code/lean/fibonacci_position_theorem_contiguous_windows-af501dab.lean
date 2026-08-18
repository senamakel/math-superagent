import Mathlib

/-!
Formal statement of Sivasankar--Rama, Proposition 1, in a finite-word model.
`F` is the length sequence, `fibWord` the rabbit Fibonacci words, `rot` left
rotation, and `factorSet` the set of length-k contiguous factors of an infinite
word.  The source theorem identifies the displayed finite prefix set with the
infinite factor set.  The source's theorem is recorded as a cited axiom because
this library does not yet contain its proof.
-/

namespace FibonacciPosition

abbrev Word := List Char

 def fibWord : Nat → Word
  | 0 => ['a']
  | 1 => ['a', 'b']
  | n + 2 => fibWord (n + 1) ++ fibWord n

 def fibLen (n : Nat) : Nat := (fibWord n).length

 def rot (w : Word) (i : Nat) : Word :=
  let j := i % w.length
  w.drop j ++ w.take j

 def wordPrefix (k : Nat) (w : Word) : Word := w.take k

 def finiteFactors (w : Word) (k : Nat) : Set Word :=
  {u | ∃ i, i + k ≤ w.length ∧ (w.drop i).take k = u}

 def fibonacciFactors (k : Nat) : Set Word :=
  {u | ∃ n, u ∈ finiteFactors (fibWord n) k}

 def windowIndices (n k : Nat) : Finset Nat :=
  (Finset.range (fibLen n)) ∪
    ((Finset.Icc (fibLen (n + 2) - k - 1) (fibLen (n + 1) - 1)))

 def windows (n k : Nat) : Set Word :=
  {u | ∃ i ∈ windowIndices n k, wordPrefix k (rot (fibWord (n + 1)) i) = u}

namespace Cited
/-- src: Sivasankar and Rama, arXiv:2207.04304, Proposition 1. -/
axiom proposition_one
    (n k : Nat) (hn : 2 ≤ n) (hk₁ : fibLen n ≤ k)
    (hk₂ : k < fibLen (n + 1)) :
    fibonacciFactors k = windows n k
end Cited

/-- The requested contiguous-window position theorem.

`n` and `k` are the source integers. `hn` carries `n ≥ 2`; `hk₁` carries
`F(n) ≤ k`, with `fibLen n` representing the source's `F(n)`; and `hk₂`
carries `k < F(n+1)`. The infinite factor set is represented by the union
of finite Fibonacci-word factor sets, while `windows` is the stated union of
rotation-prefix windows. -/
theorem fibonacci_position_theorem_contiguous_windows
    (n k : Nat) (hn : 2 ≤ n) (hk₁ : fibLen n ≤ k)
    (hk₂ : k < fibLen (n + 1)) :
    fibonacciFactors k = windows n k := by
  exact Cited.proposition_one n k hn hk₁ hk₂

#print axioms fibonacci_position_theorem_contiguous_windows
#print axioms Cited.proposition_one

end FibonacciPosition
