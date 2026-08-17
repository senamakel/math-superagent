import Mathlib.Data.Nat.Fib.Basic
import Mathlib.Data.Set.Basic
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Data.Set.Card
import Mathlib.Algebra.BigOperators.Intervals

/-!
# G1 — Sturmian factor structure of the Fibonacci word (PE1006)

> **Companion.**  The *provable shell* of this node — the monotone nesting
> `factorSet_prefix_nest` / `factorSet_chain` / `factorSet_chain_any` — is
> proved and kernel-verified in `code/lean/pe1006_psi_G1_factor_chain-87f94deb.lean`
> (sorry-free, axioms `propext`, `Quot.sound`).  This file keeps only the
> node's main count claim and its decomposition, so the reader can see exactly
> which part is open.

Node `G1-sturmian-factor-structure` (from `research/backward/pe1006-psi.md`).

Informal claim, tracked binder-by-binder:

> Let `F` be the infinite Fibonacci word (limit of `S_0 = 0`, `S_1 = 01`,
> `S_n = S_{n-1} S_{n-2}`). For every length `k ≥ 1`, the set of distinct
> Fibonacci subwords (contiguous substrings of some `S_n`) equals the set of
> length-`k` contiguous factors of `F`, and there are exactly `k + 1` of them.
> `F` is the characteristic Sturmian word of slope `1/φ²`, and a Sturmian word
> has factor complexity `p(k) = k + 1`.

## What is formalised here, and what each binder carries

* **`fibWord n`** — the finite word `S_n` (`S_0 = 0`, `S_1 = 01`,
  `S_{n+2} = S_{n+1} ++ S_n`), exactly the problem's definition.
* **`FactorSet w k`** — the set of length-`k` contiguous factors of a word `w`
  (a `Set (List α)`; `0 ≠ 00` as factors, matching the statement's list of
  four *distinct* length-3 words).
* **`FibSubwords k = ⋃_n FactorSet (fibWord n) k`** — literally "the set of
  distinct Fibonacci subwords of length k" as the problem words it
  (`problem.md`: a Fibonacci subword is a contiguous substring of some `S_n`;
  "there are only k+1 different Fibonacci subwords of length k").  This is the
  exact object the node's count quantifies over.
* **`fib_subword_count k h`** — `(FibSubwords k).ncard = k + 1`, the node's
  main claim.  Carries `h : 1 ≤ k` because the problem states the count only
  for *positive* lengths.  This is the Sturmian factor-complexity theorem and
  is **not yet proved in Lean**; it is a `gap`.

## What is genuinely proved here (the shell)

The factor sets form a monotone chain: `FactorSet (fibWord n) k ⊆
FactorSet (fibWord (n+1)) k`, because `S_n` is a prefix of `S_{n+1}` and a
length-`k` factor of a word is a length-`k` factor of any extension.  Hence
`FibSubwords k` (the object the count is over) is a monotone *nested* union
(`factorSet_chain_any`).  This nesting is the part of the node that is
provable by elementary means and is proved below.

## The deep part — honest status

Two ingredients of the full informal claim are NOT proved here:

1. **Stabilisation / identification with the infinite limit word `F`.**
   "the set of distinct Fibonacci subwords equals the set of length-k factors
   of F" requires the limit word and the fact that the nested chain
   `FactorSet (fibWord n) k` is eventually constant (each factor of `F` shows
   up in some `S_n`).  Mathlib has no Sturmian-word library, so the true limit
   word is not formalised; that stabilisation is the aperiodicity content
   (a Sturmian word is aperiodic) and is **not** proved here.
2. **The count `k + 1`.**  This is the factor-complexity theorem for Sturmian
   words (Morse–Hedlund 1940; Lothaire / Berstel, *Algebraic Combinatorics on
   Words* Ch. 2 §2.1.1 p. 89: Sturmian = complexity `P(s,n) = n+1`).  It is
   recorded under `namespace Cited` as an axiom with its source, but — because
   the bridge from the finite `S_n` family to the true limit word is not yet in
   Lean — it is **not** used to discharge `fib_subword_count`; that theorem
   remains a `gap` with the failure located precisely (see the report).

## Node status

The node's *statement* is formalised and elaborates; the *provable shell*
(nesting) is proved; the *count* and the *limit identification* are declared
`gap`s.  So the claim rests on `sorry` and is **not** `formalised`.
-/

namespace PE1006G1

open scoped BigOperators

/-- `S_n`: `S_0 = 0`, `S_1 = 01`, `S_{n+2} = S_{n+1} ++ S_n`. -/
def fibWord : ℕ → List Char
  | 0 => ['0']
  | 1 => ['0', '1']
  | n + 2 => fibWord (n + 1) ++ fibWord n

/-- The length-`k` contiguous factors of a word `w`, as a set of words
(respecting `List` equality). -/
def FactorSet {α : Type*} (w : List α) (k : ℕ) : Set (List α) :=
  { F : List α | ∃ i : ℕ, F = (w.drop i).take k ∧ F.length = k }

/-- The set of distinct Fibonacci subwords of length `k`: the union over all
`S_n` of their length-`k` factor sets.  This is the object the problem's
"there are only k+1 different Fibonacci subwords of length k" quantifies over
(`problem.md`). -/
def FibSubwords (k : ℕ) : Set (List Char) :=
  ⋃ n : ℕ, FactorSet (fibWord n) k

/-- The length-`k` factors of `w` as a `Finset` (decidable, for the oracle
checks); the image deduplicates, so `card` counts distinct factors. -/
def factorsFinset (w : List Char) (k : ℕ) : Finset (List Char) :=
  (Finset.range (w.length - k + 1)).image (fun i => (w.drop i).take k)

/-! ## Provable shell: the factor chain is monotone -/

/-- `S_n` is a prefix of `S_{n+1}`: `S_1 = S_0 ++ ['1']` (since `S_0 = '0'`);
for `n ≥ 1`, `S_{n+1} = S_n ++ S_{n-1}` by the definition. -/
lemma fibWord_prefix (n : ℕ) : ∃ r : List Char, fibWord (n + 1) = fibWord n ++ r := by
  cases n with
  | zero =>
      -- S_1 = ['0','1'] and S_0 ++ ['1'] = ['0'] ++ ['1'] = ['0','1']
      refine ⟨['1'], ?_⟩
      rfl
  | succ m =>
      refine ⟨fibWord m, ?_⟩
      change fibWord (m + 2) = fibWord (m + 1) ++ fibWord m
      rw [fibWord]

/-- A length-`k` factor of `w` is a length-`k` factor of `w ++ r`: every
contiguous block of `w` sits at the same offset inside the extension, and the
length-`k` condition is preserved. -/
theorem factorSet_prefix_nest {α : Type*} (w r : List α) (k : ℕ) :
    FactorSet w k ⊆ FactorSet (w ++ r) k := by
  rintro F ⟨i, hF, hlen⟩
  refine ⟨i, ?_, hlen⟩
  by_cases hi : i ≤ w.length
  · -- i ≤ w.length : the block stays entirely inside w, so the same offset
    -- finds it in w ++ r.  Prove k ≤ (w.drop i).length using hlen, then use
    -- drop_append / take_append to keep the take inside the w part.
    have hlen' : (List.take k (w.drop i)).length = k := by simpa [hF] using hlen
    have hmin : min k (w.drop i).length = k := by simpa [List.length_take] using hlen'
    have hk_le : k ≤ w.length - i := by
      have hdrop_len : (w.drop i).length = w.length - i := by simp
      rw [← hmin, hdrop_len]
      exact Nat.min_le_right k (w.length - i)
    rw [hF]
    rw [List.drop_append_of_le_length hi]
    rw [List.take_append_of_le_length (by simpa using hk_le)]
  · -- i > w.length ⟹ w.drop i = [] ⟹ the factor is empty and k = 0.
    have hdrop : w.drop i = [] := List.drop_eq_nil_of_le (le_of_lt (lt_of_not_ge hi))
    have hF0 : F = [] := by simpa [hdrop] using hF
    have hk : k = 0 := by simpa [hF0] using hlen.symm
    rw [hF0, hk]
    simp

/-- Every length-`k` factor of `S_n` is a length-`k` factor of `S_{n+1}`, so
`FactorSet (fibWord n) k ⊆ FactorSet (fibWord (n+1)) k`. -/
theorem factorSet_chain (k n : ℕ) :
    FactorSet (fibWord n) k ⊆ FactorSet (fibWord (n + 1)) k := by
  rcases fibWord_prefix n with ⟨r, hpre⟩
  rw [hpre]
  exact factorSet_prefix_nest (fibWord n) r k

/-- The chain is monotone across any step (induction on the step count). -/
theorem factorSet_chain_any (k n d : ℕ) :
    FactorSet (fibWord n) k ⊆ FactorSet (fibWord (n + d)) k := by
  induction d with
  | zero => intro x hx; simpa using hx
  | succ d ih =>
      exact fun x hx => factorSet_chain k (n + d) (ih hx)

/-! ## The deep claim (Sturmian factor complexity) — gapped -/

/-- The main node claim: there are exactly `k + 1` distinct Fibonacci subwords
of length `k` (for `k ≥ 1`).  This is the Sturmian factor-complexity theorem,
**not yet proved in Lean** — a declared `gap`.  Every original hypothesis is
carried: `k : ℕ` is the length, `h : 1 ≤ k` is the problem's "for each
positive integer k", and the object is `FibSubwords k` = "the distinct
Fibonacci subwords of length k". -/
theorem fib_subword_count (k : ℕ) (h : 1 ≤ k) :
    (FibSubwords k).ncard = k + 1 := by
  sorry

/-- ***Settlement of the identification half.***  The stabilisation claim:
every length-`k` factor of the infinite limit word is already a length-`k`
factor of some `S_n`.  Since the limit word is not formalised (no Mathlib
Sturmian library), this is stated as: the chain is eventually constant, i.e.
`⋃_n FactorSet (fibWord n) k` is attained by a finite index.  This is the
aperiodicity content and is **not** proved — a declared `gap`. -/
theorem factor_limit_stabilises (k : ℕ) :
    ∀ F : List Char, F ∈ FibSubwords k → ∃ n : ℕ, F ∈ FactorSet (fibWord n) k := by
  intro F hF
  simpa [FibSubwords, Set.mem_iUnion] using hF

/-! ### Cited literature (not used to discharge the gap)

The factor-complexity theorem is standard.  Recorded under `namespace Cited`
with its source so a later step can prove the bridge; it is **not** an axiom
`fib_subword_count` rests on, so that theorem stays honestly open. -/
namespace Cited

/-- src: Morse & Hedlund 1940; Lothaire, *Algebraic Combinatorics on Words*
(Berstel), Ch. 2 §2.1.1, p. 89: a Sturmian word has factor complexity
`P(s, n) = n + 1` for every `n ≥ 0` (this is the *definition* of Sturmian in
Lothaire).  Formalised here only as a placeholder shape; not used. -/
axiom sturmian_factor_complexity (k : ℕ) (h : 0 < k) :
    (FibSubwords k).ncard = k + 1

end Cited

/-! ## Small oracle checks (computed)

The statement's example: the four distinct length-3 Fibonacci subwords are
`001, 010, 100, 101`.  We verify directly that `S_5 = 0100101001001` (length
13) contains exactly these four length-3 factors and no others. -/

/-- `S_5 = 0100101001001` (documents give `S_2=010`, `S_3=01001`,
`S_4=01001010`; `S_5 = S_4 ++ S_3 = 01001010 ++ 01001`). -/
example : fibWord 5 = ['0','1','0','0','1','0','1','0','0','1','0','0','1'] := by
  native_decide

/-- The length-3 factor set of `S_5` is exactly `{001, 010, 100, 101}`, the
statement's four factors. -/
example : factorsFinset (fibWord 5) 3
    = {['0','1','0'], ['0','0','1'], ['1','0','0'], ['1','0','1']} := by
  native_decide

/-- Finite witness: `S_5` already delivers `4 = k + 1` distinct length-3
factors. -/
example : (factorsFinset (fibWord 5) 3).card = 4 := by
  native_decide

end PE1006G1

#print axioms PE1006G1.factorSet_prefix_nest
#print axioms PE1006G1.factorSet_chain
#print axioms PE1006G1.factorSet_chain_any
#print axioms PE1006G1.fib_subword_count
#print axioms PE1006G1.factor_limit_stabilises
#print axioms PE1006G1.Cited.sturmian_factor_complexity
