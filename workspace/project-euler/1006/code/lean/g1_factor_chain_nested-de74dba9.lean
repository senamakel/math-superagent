import Mathlib.Data.Set.Basic
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Data.Set.Card
import Mathlib.Algebra.BigOperators.Intervals

/-!
# Node `g1-factor-chain-nested` — monotone nesting of the Fibonacci factor sets

Statement (from `research/notes/g1-formalisation-status.md`):

  For S_n = S_0=0, S_1=01, S_{n+2}=S_{n+1}S_n, the length-k contiguous factor
  sets form a monotone nested chain: FactorSet(fibWord n, k) ⊆
  FactorSet(fibWord (n+1), k) for all n, k.  In particular FibSubwords k =
  ⋃_n FactorSet(fibWord n, k) is a monotone (increasing) union, so the object
  the count k+1 is asserted over is well-defined.

Hypotheses carried by binders:

* `fibWord n : ℕ → List Char` encodes S_n with no hypotheses — a `def`.
* `FactorSet w k` — the length-k contiguous factors of `w` — is a `def`.
* `FibSubwords k := ⋃ n, FactorSet (fibWord n) k` — the union — is a `def`.
* `factorSet_chain (k n : ℕ)` : FactorSet (fibWord n) k ⊆
  FactorSet (fibWord (n + 1)) k.  Both `k` and `n` are *data*, not
  hypotheses: the claim holds for all naturals, so no side condition
  (no k ≥ 1) is needed.  This matches the source, which states the nesting for
  all n, k.
* `factorSet_chain_any (k n d : ℕ)` : FactorSet (fibWord n) k ⊆
  FactorSet (fibWord (n + d)) k — the monotone union across an arbitrary step,
  which is exactly "FibSubwords k is an increasing union".
* `fibWord_prefix (n : ℕ)` : ∃ r, fibWord (n+1) = fibWord n ++ r — the
  structural fact (S_n is a prefix of S_{n+1}) the nesting rests on.

So every binder is data; there are no unproved side conditions, and the goal
(`factorSet_chain` / `factorSet_chain_any`) is established unconditionally.
-/

namespace PE1006G1

open scoped BigOperators

/-- `S_n`: `S_0 = 0`, `S_1 = 01`, `S_{n+2} = S_{n+1} ++ S_n`. -/
def fibWord : ℕ → List Char
  | 0 => ['0']
  | 1 => ['0', '1']
  | n + 2 => fibWord (n + 1) ++ fibWord n

/-- The length-`k` contiguous factors of a word `w`, as a set of words
(respecting `List` equality, so `0 ≠ 00`). -/
def FactorSet {α : Type*} (w : List α) (k : ℕ) : Set (List α) :=
  { F : List α | ∃ i : ℕ, F = (w.drop i).take k ∧ F.length = k }

/-- The set of distinct Fibonacci subwords of length k: the union over all S_n
of their length-k factor sets (the object the problem's "k+1 different
Fibonacci subwords of length k" quantifies over). -/
def FibSubwords (k : ℕ) : Set (List Char) :=
  ⋃ n : ℕ, FactorSet (fibWord n) k

/-- `S_n` is a prefix of `S_{n+1}`: for n = 0, S_1 = S_0 ++ ['1']; for n ≥ 1,
S_{n+1} = S_n ++ S_{n-1} by definition. -/
lemma fibWord_prefix (n : ℕ) : ∃ r : List Char, fibWord (n + 1) = fibWord n ++ r := by
  cases n with
  | zero => refine ⟨['1'], ?_⟩; rfl
  | succ m =>
      refine ⟨fibWord m, ?_⟩
      change fibWord (m + 2) = fibWord (m + 1) ++ fibWord m
      rw [fibWord]

/-- A length-`k` factor of `w` is a length-`k` factor of `w ++ r`. -/
theorem factorSet_prefix_nest {α : Type*} (w r : List α) (k : ℕ) :
    FactorSet w k ⊆ FactorSet (w ++ r) k := by
  rintro F ⟨i, hF, hlen⟩
  refine ⟨i, ?_, hlen⟩
  by_cases hi : i ≤ w.length
  · have hlen' : (List.take k (w.drop i)).length = k := by simpa [hF] using hlen
    have hmin : min k (w.drop i).length = k := by simpa [List.length_take] using hlen'
    have hk_le : k ≤ w.length - i := by
      have hdrop_len : (w.drop i).length = w.length - i := by simp
      rw [← hmin, hdrop_len]
      exact Nat.min_le_right k (w.length - i)
    rw [hF]
    rw [List.drop_append_of_le_length hi]
    rw [List.take_append_of_le_length (by simpa using hk_le)]
  · have hdrop : w.drop i = [] := List.drop_eq_nil_of_le (le_of_lt (lt_of_not_ge hi))
    have hF0 : F = [] := by simpa [hdrop] using hF
    have hk : k = 0 := by simpa [hF0] using hlen.symm
    rw [hF0, hk]
    simp

/-- Every length-`k` factor of `S_n` is a length-`k` factor of `S_{n+1}`. -/
theorem factorSet_chain (k n : ℕ) :
    FactorSet (fibWord n) k ⊆ FactorSet (fibWord (n + 1)) k := by
  rcases fibWord_prefix n with ⟨r, hpre⟩
  rw [hpre]
  exact factorSet_prefix_nest (fibWord n) r k

/-- The chain is monotone across any step: FactorSet (fibWord n) k ⊆
FactorSet (fibWord (n + d)) k.  Hence FibSubwords k is an increasing union. -/
theorem factorSet_chain_any (k n d : ℕ) :
    FactorSet (fibWord n) k ⊆ FactorSet (fibWord (n + d)) k := by
  induction d with
  | zero => intro x hx; simpa using hx
  | succ d ih =>
      exact fun x hx => factorSet_chain k (n + d) (ih hx)

end PE1006G1

#print axioms PE1006G1.factorSet_prefix_nest
#print axioms PE1006G1.factorSet_chain
#print axioms PE1006G1.factorSet_chain_any
