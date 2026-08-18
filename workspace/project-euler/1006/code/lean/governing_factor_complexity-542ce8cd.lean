import Mathlib.Data.Set.Basic
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Data.Set.Card
import Mathlib.Data.Nat.Basic
import Mathlib.Data.List.Basic
import Mathlib.Data.Fin.Basic
import Mathlib.Algebra.BigOperators.Intervals

/-!
# Node `governing-factor-complexity` (PE1006)

Informal claim (`research/notes/sourced-claims-governing-theory.md`):

> A **Sturmian word** has exactly k+1 distinct factors (contiguous substrings)
> of length k for every k >= 1 (Morse–Hedlund minimal complexity; Perrin–Restivo
> Theorem 1; and the *definition*: exactly n+1 factors of length n). Hence the
> infinite Fibonacci word has exactly k+1 distinct length-k substrings —
> precisely the problem's "interestingly, for each positive integer k, there are
> only k+1 different Fibonacci subwords of length k".

## What each binder carries

* **`k`** is the factor length, a natural number.
* **`h : 1 ≤ k`** is the statement's "for every k ≥ 1" — carried on the clause
  that needs positivity.
* **"Sturmian word"** is formalised as `IsSturmian s` : `factorComplexity s n =
  n + 1 ∀ n`.  This is the Morse–Hedlund / Lothaire *definition* of a Sturmian
  word (minimal factor complexity among aperiodic binary words), which is what
  the informal claim's parenthetical "and the definition" refers to.
* **"has exactly k+1 distinct factors of length k"** = `factorComplexity s k =
  k + 1`, where `factorComplexity` counts the distinct length-k contiguous
  factors of the infinite word.

## What is proved, what is cited

The **governing theorem** — a Sturmian word has exactly k+1 length-k factors —
is *definitional* and is proved sorry-free below (`governing_theorem`,
`governing_theorem_pos`): `IsSturmian` is defined to be exactly that property,
so the theorem unfolds to the definition.

The **"Hence the infinite Fibonacci word …"** clause needs the (deep) fact that
the infinite Fibonacci word `F` is Sturmian — i.e. that `F` is the mechanical
word of the irrational slope 1/φ² (Perrin–Restivo Theorem 1 + the Fibonacci
word's characteristic-slope identification, node `governing-sturmian`), and the
bridge `factorComplexity F k = (FibSubwords k).ncard` (the stabilisation of the
`S_n` factor chain: every factor of the limit already occurs in some finite
`S_n`).  Both are genuine open content of the run and are recorded here as
`Cited` axioms (literature) and as `gap`s with a `next` line each.  The count
`fib_subword_count` is therefore **conditional**: the kernel checks the
implication, and the hypothesis is the literature.
-/

namespace GoverningFactorComplexity

open scoped BigOperators

/-- An infinite binary word: a function from positions to {0,1}. -/
abbrev InfiniteBinaryWord := ℕ → Fin 2

/-- The length-`k` factor (`List α`) of the word `s` starting at position
`i`: the letters `s i, s(i+1), …, s(i+k-1)`.  Contiguous substrings of an
infinite word. -/
def Factor (s : ℕ → α) (i k : ℕ) : List α :=
  (List.range k).map (fun t => s (i + t))

/-- The set of all distinct length-`k` factors of the infinite word `s`
(respecting `List` equality, so `0 ≠ 00` as words). -/
def factorSet (s : ℕ → α) (k : ℕ) : Set (List α) :=
  { F : List α | ∃ i : ℕ, F = Factor s i k }

/-- The length of the factor `Factor s i k` is `k`. -/
lemma factor_length (s : ℕ → α) (i k : ℕ) : (Factor s i k).length = k := by
  rw [Factor, List.length_map, List.length_range]

/-- **Factor complexity**: `complexity s k` is the number of distinct length-`k`
factors of `s`.  For a binary word this is finite (there are only 2^k candidate
words), and `Set.ncard` is the cardinality of a set (defined even when the set
is infinite). -/
noncomputable def factorComplexity (s : InfiniteBinaryWord) (k : ℕ) : ℕ :=
  (factorSet s k).ncard

/-- **Sturmian** (Morse–Hedlund / Lothaire, Berstel *ACoW* Ch.2 §2.1.1):
an infinite binary word with minimal factor complexity, i.e.
`factorComplexity s n = n + 1` for every `n ≥ 0`.  This is the definition the
informal claim's parenthetical cites. -/
def IsSturmian (s : InfiniteBinaryWord) : Prop :=
  ∀ n : ℕ, factorComplexity s n = n + 1

/-! ## The governing theorem (proved: by definition) -/

/-- ***The node's first clause, formalised and proved.***  A Sturmian word has
exactly `k + 1` distinct factors of length `k`, for every `k ≥ 1`.  Because
`IsSturmian` is *defined* as `factorComplexity s n = n + 1` for all `n`, this
unfolds to the definition; `h : 1 ≤ k` is carried even though the definition
gives the equality for every `k`. -/
theorem governing_theorem_pos (s : InfiniteBinaryWord) (hs : IsSturmian s)
    (k : ℕ) (h : 1 ≤ k) : factorComplexity s k = k + 1 := by
  exact hs k

/-! ## The object the problem's count is over -/

/-- `S_n`: `S_0 = 0`, `S_1 = 01`, `S_{n+2} = S_{n+1} ++ S_n` — exactly the
problem's definition. -/
def fibWord : ℕ → List Char
  | 0 => ['0']
  | 1 => ['0', '1']
  | n + 2 => fibWord (n + 1) ++ fibWord n

/-- The length-`k` contiguous factors of a *finite* word `w`, as a set of words
(respecting `List` equality, so `0 ≠ 00`). -/
def wordFactorSet {α : Type*} (w : List α) (k : ℕ) : Set (List α) :=
  { F : List α | ∃ i : ℕ, F = (w.drop i).take k ∧ F.length = k }

/-- The set of distinct Fibonacci subwords of length `k`: the union over all
`S_n` of their length-`k` factor sets — literally the object of the problem's
"there are only k+1 different Fibonacci subwords of length k". -/
def FibSubwords (k : ℕ) : Set (List Char) :=
  ⋃ n : ℕ, wordFactorSet (fibWord n) k

/-! ## The "Hence the Fibonacci word …" clause — conditional (cited)

The count `(FibSubwords k).ncard = k + 1` follows from the governing theorem
**provided** the infinite Fibonacci word is Sturmian and provided the finite
`S_n`-union `FibSubwords k` equals the length-`k` factor set of that infinite
limit word.  Both are the run's deep content: the first is Perrin–Restivo
Theorem 1 (mechanical word of irrational slope 1/φ² ⇒ Sturmian, so k+1
factors), the second is the stabilisation of the nested `S_n` chain.  They are
recorded as `Cited` axioms — the kernel checks the implication, the hypotheses
are the literature — and the combining step `fib_subword_count` is kernel
checked below.
-/

namespace Cited

/-- The infinite Fibonacci word `F`: the pointwise limit of the `S_n` chain.
Declared as an **opaque constant** (not a reducing definition — in particular
it does *not* unfold to the all-zero word).  Its existence and well-definedness
(`S_n` is a prefix of `S_{n+1}`, so the pointwise limit exists) is part of the
gap `gond-stabilisation`; what is recorded here is that *this object* is the
one the problem's subwords come from. -/
axiom fibInf : InfiniteBinaryWord

/-- src: Perrin & Restivo, *On Sturmian words*, Thm 1 (a word is Sturmian iff
it is the mechanical word of an irrational slope) together with the fact that
the infinite Fibonacci word is the characteristic word of slope 1/φ²
(Perrin–Restivo Example 2; node `governing-sturmian`).  Hence the infinite
Fibonacci word is Sturmian. -/
axiom fibonacci_sturmian : IsSturmian Cited.fibInf

/-- src: stabilisation of the nested `S_n` factor chain (proved as a shell in
`code/lean/pe1006_psi_G1_factor_chain-87f94deb.lean`): every length-k factor of
the infinite limit word already occurs in some finite `S_n`, so the count over
`FibSubwords k` (the union) equals `factorComplexity F k` of the limit. -/
axiom factors_stabilise (k : ℕ) :
    (FibSubwords k).ncard = factorComplexity Cited.fibInf k

end Cited

/-- ***The count the problem asserts.***  The combining step: `fib_subword_count
k` follows from the governing theorem (`fibonacci_sturmian` = Sturmian, so k+1
factors) and the stabilisation bridge (`factors_stabilise`).  **Conditional**:
rests on the two `Cited` axioms. -/
theorem fib_subword_count (k : ℕ) (h : 1 ≤ k) :
    (FibSubwords k).ncard = k + 1 := by
  rw [Cited.factors_stabilise]
  exact Cited.fibonacci_sturmian k

#print axioms GoverningFactorComplexity.governing_theorem_pos
#print axioms GoverningFactorComplexity.fib_subword_count
#print axioms GoverningFactorComplexity.Cited.fibonacci_sturmian
#print axioms GoverningFactorComplexity.Cited.factors_stabilise

/-!
# Decomposition map (gaps)

The count `fib_subword_count` is conditional on two `Cited` axioms.  Each is
its own gap (the honest open content) so the statement graph can schedule them:

```gap
id: gond-fib-sturmian
lemma: (bridging) the infinite Fibonacci word F (limit of the S_n chain) is
  Sturmian — i.e. is the mechanical word of the irrational slope 1/phi^2
  (Perrin–Restivo Thm 1), so factorComplexity F k = k + 1.
status: open — literature result, not formalised (Mathlib has no Sturmian theory)
next: formalise F as the mechanical word digit(n) = floor((n+2)α)−floor((n+1)α)
  for the irrational α = 1/phi^2, then prove factor complexity k+1 via the
  three-distance / rotation structure; equivalently cite Perrin–Restivo Thm 1
  verbatim and prove the slope identification of node `governing-sturmian`.
```

```gap
id: gond-stabilisation
lemma: (bridging) (FibSubwords k).ncard = factorComplexity F k, i.e. the
  length-k factors of the infinite limit word are exactly the union over the
  finite S_n of their length-k factor sets (stabilisation of the nested chain;
  aperiodicity).
status: open — needs a formal limit word F (not in Mathlib) and that every
  factor of F occurs in some S_n.
next: build on the proved shell `factorSet_chain_any` in
  code/lean/pe1006_psi_G1_factor_chain-87f94deb.lean (S_n is a prefix of
  S_{n+1}, chain monotone) and formalise the pointwise limit F = ⋃_n prefixes.
```
-/

end GoverningFactorComplexity
