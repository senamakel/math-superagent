import Mathlib.Data.Nat.Fib.Basic
import Mathlib.Data.Set.Basic
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Data.Set.Card
import Mathlib.Algebra.BigOperators.Intervals

/-!
# Node `fibonacci-sturmian-complexity` — decomposition (PE1006)

> **Companion.**  The *provable shell* of this node — that the length-`k` factor
> sets of the Fibonacci words `S_n` form a monotone nested chain and each is
> contained in the set of Fibonacci subwords — is kernel-verified in
> `code/lean/pe1006_psi_G1_factor_chain-87f94deb.lean` (sorry-free, axioms
> `propext`, `Quot.sound`).  This file restates that shell briefly and then
> records the **decomposition** of the node's real content, the count.

Node `fibonacci-sturmian-complexity`
(from `research/summaries/claim-fibonacci-sturmian-complexity.md`).

> The infinite Fibonacci word f (limit of the morphism `0 -> 01`, `1 -> 0` — the
> `S_n` limit of PE1006) is a Sturmian word, and its factor complexity function
> counts exactly `P(f, k) = k + 1` distinct factors (subwords) of length `k`,
> for every integer `k ≥ 0`.

## What the run needs this node for

PE1006's `Psi(k)` is a sum over the **distinct** length-`k` Fibonacci subwords,
and the problem tells us there are exactly `k + 1` of them.  Downstream, `Psi`
is a sum of `k + 1 → 10^18 + 1` terms, so the **count** `(FibSubwords k).ncard =
k + 1` is the load-bearing fact.  It is what this node contributes.

## The decomposition

The count splits into two halves, each the genuine content of the Sturmian
factor-complexity theorem:

* **`subword_count_upper`** — `(FibSubwords k).ncard ≤ k + 1`: there are *at
  most* `k + 1` distinct length-`k` Fibonacci subwords.  This is the Sturmian
  (aperiodic) upper bound: minimal complexity for a binary aperiodic word is
  `n + 1` (Morse–Hedlund / Lothaire Ch. 2 §2.1.1 p. 89), together with the
  identification of `FibSubwords k` with the length-`k` factor set of the limit
  word.  **Open.**
* **`subword_count_lower`** — `k + 1 ≤ (FibSubwords k).ncard`: there are *at
  least* `k + 1` distinct length-`k` Fibonacci subwords.  This is the
  *existence* half — a constructive list of `k + 1` distinct factors (the
  translation/rotation windows of the characteristic word).  For each concrete
  `k` it is a decidable, machine-checked certificate; in general it is open.
* **`fib_subword_count`** — the combining step: `le_antisymm` of the two.

The two bounds are the deep content and are left as `gap`s; the combining step
is kernel-checked so the *shape* of the argument is verified even while its
leaves are open.  A `Cited` axiom records the literature result (the factor
complexity of the Fibonacci word), giving a `conditional` route, but it is
**not** used to discharge the gaps, which stay honest tasks.
-/

namespace PE1006SturmComplexity

open scoped BigOperators

set_option maxRecDepth 10000 in

/-- `S_n`: `S_0 = 0`, `S_1 = 01`, `S_{n+2} = S_{n+1} ++ S_n` — exactly the
problem's definition. -/
def fibWord : ℕ → List Char
  | 0 => ['0']
  | 1 => ['0', '1']
  | n + 2 => fibWord (n + 1) ++ fibWord n

/-- The length-`k` contiguous factors of a word `w`, as a set of words
(respecting `List` equality, so `0 ≠ 00`). -/
def FactorSet {α : Type*} (w : List α) (k : ℕ) : Set (List α) :=
  { F : List α | ∃ i : ℕ, F = (w.drop i).take k ∧ F.length = k }

/-- The set of distinct Fibonacci subwords of length `k`: the union over all
`S_n` of their length-`k` factor sets.  This is exactly the object the problem
sentence "there are only k+1 different Fibonacci subwords of length k"
quantifies over. -/
def FibSubwords (k : ℕ) : Set (List Char) :=
  ⋃ n : ℕ, FactorSet (fibWord n) k

/-! ## Provable shell (reproduced; counterpart file has these kernel-verified) -/

/-- `S_n` is a prefix of `S_{n+1}`. -/
lemma fibWord_prefix (n : ℕ) : ∃ r : List Char, fibWord (n + 1) = fibWord n ++ r := by
  cases n with
  | zero => refine ⟨['1'], ?_⟩; rfl
  | succ m => refine ⟨fibWord m, ?_⟩; change fibWord (m + 2) = fibWord (m + 1) ++ fibWord m; rw [fibWord]

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

/-- Every length-`k` factor of `S_n` is a length-`k` factor of `S_{n+1}`, so
`FactorSet (fibWord n) k ⊆ FactorSet (fibWord (n+1)) k`. -/
theorem factorSet_chain (k n : ℕ) :
    FactorSet (fibWord n) k ⊆ FactorSet (fibWord (n + 1)) k := by
  rcases fibWord_prefix n with ⟨r, hpre⟩
  rw [hpre]
  exact factorSet_prefix_nest (fibWord n) r k

/-- Every length-`k` factor of any `S_n` is a Fibonacci subword. -/
theorem factorSet_mem_subwords (n k : ℕ) {F : List Char} :
    F ∈ FactorSet (fibWord n) k → F ∈ FibSubwords k := by
  intro hF
  rw [FibSubwords, Set.mem_iUnion]
  exact ⟨n, hF⟩

/-- The length-`k` factors of `w` as a `Finset` (decidable; `card` counts
distinct factors).  Used only for the finite, machine-checked certificates. -/
def factorsFinset (w : List Char) (k : ℕ) : Finset (List Char) :=
  (Finset.range (w.length - k + 1)).image (fun i => (w.drop i).take k)

/-! ## The decomposition (the node's real content) -/

/-- ***Upper bound.***  There are at most `k + 1` distinct Fibonacci subwords of
length `k`.  This is the Sturmian (aperiodic) upper bound: a binary aperiodic
word has factor complexity `≥ n + 1`, with equality iff Sturmian, and for the
Fibonacci word `P(f, k) = k + 1` (Morse–Hedlund 1940; Lothaire / Berstel,
*Algebraic Combinatorics on Words* Ch. 2 §2.1.1 p. 89), together with the
identification of `FibSubwords k` with the length-`k` factor set of the limit
word.  This identification needs the actual limit word of the `S_n` chain,
which Mathlib does not formalise (no Sturmian library) — that stabilisation is
the aperiodicity content.  **Declared `gap`.**
-/
theorem subword_count_upper (k : ℕ) (h : 1 ≤ k) :
    (FibSubwords k).ncard ≤ k + 1 := by
  sorry

/-- ***Lower bound (existence / certificate).***  There are at least `k + 1`
distinct Fibonacci subwords of length `k`.  The natural proof exhibits `k + 1`
distinct factors explicitly — the translation windows of the characteristic
word of slope `1/φ²` (Perrin–Restivo: characteristic word; the run's mechanical
construction).  For each concrete `k` this is a decidable, machine-checked
certificate (see the `decide` examples below); in general it is **open** and is
the constructive half of the factor-complexity theorem.
-/
theorem subword_count_lower (k : ℕ) (h : 1 ≤ k) :
    k + 1 ≤ (FibSubwords k).ncard := by
  sorry

/-- ***The combining step.***  `fib_subword_count` follows from the two bounds
by `le_antisymm`.  This is the theorem downstream `Psi` rests on: the sum over
length-`k` Fibonacci subwords runs over exactly `k + 1` distinct terms.  The
statement is kernel-checked here; its two leaves (`subword_count_upper`,
`subword_count_lower`) are the open `gap`s. -/
theorem fib_subword_count (k : ℕ) (h : 1 ≤ k) :
    (FibSubwords k).ncard = k + 1 := by
  exact le_antisymm (subword_count_upper k h) (subword_count_lower k h)

/-! ### Cited literature (backup; not used to discharge the gaps)

The factor-complexity theorem is standard.  Recorded under `namespace Cited`
with its source so a *conditional* route exists (the kernel checks the
implication; the hypothesis is the literature).  It is deliberately **not**
used in `fib_subword_count`, which stays an honest open task with its leaves
located. -/
namespace Cited

/-- src: Morse & Hedlund 1940; Lothaire, *Algebraic Combinatorics on Words*
(Berstel), Ch. 2 §2.1.1 p. 89; Wikipedia "Fibonacci word": the infinite
Fibonacci word `F` (the `S_n` limit of PE1006) is Sturmian, so its factor
complexity is `P(F, k) = k + 1` for every `k ≥ 1` (and `P(F, 0) = 1`).  This is
the whole node as a black box, held as literature for a conditional route only. -/
axiom fibonacci_word_factor_complexity (k : ℕ) (h : 1 ≤ k) :
    (FibSubwords k).ncard = k + 1

end Cited

/-! ### Finite, kernel-checked certificates for the lower bound

For concrete `k` the *upper* half stays open, but the *lower* half (existence
of `k + 1` distinct factors) is fully decidable: build a long enough `S_n`, form
the finite factor `Finset`, and `decide` its cardinality is `k + 1`.  These are
`decide` (kernel-reduced), never `native_decide`, so they carry the brute-force
evidence into the kernel for the small cases. `S_5 = 0100101001001` (length 13)
is enough for `k = 3, 4, 5`. -/

example : (factorsFinset (fibWord 5) 3).card = 4 := by
  decide

example : (factorsFinset (fibWord 6) 4).card = 5 := by
  decide

example : (factorsFinset (fibWord 6) 5).card = 6 := by
  decide

/-- The finite factor set of `S_5` of length `3` is exactly the statement's
four factors `001, 010, 100, 101` (`Psi(3) = 20302` oracle). -/
example : factorsFinset (fibWord 5) 3
    = {['0','1','0'], ['0','0','1'], ['1','0','0'], ['1','0','1']} := by
  decide

end PE1006SturmComplexity

#print axioms PE1006SturmComplexity.factorSet_prefix_nest
#print axioms PE1006SturmComplexity.factorSet_chain
#print axioms PE1006SturmComplexity.factorSet_mem_subwords
#print axioms PE1006SturmComplexity.subword_count_upper
#print axioms PE1006SturmComplexity.subword_count_lower
#print axioms PE1006SturmComplexity.fib_subword_count
#print axioms PE1006SturmComplexity.Cited.fibonacci_word_factor_complexity

/-!
## Decomposition map (gaps)

Each open sub-lemma below is written as a fenced `gap` block so the statement
graph can schedule the next attempt on it.  The `next` line names the concrete
first move a future role can take today.

```gap
id: subword-count-upper
lemma: PE1006SturmComplexity.subword_count_upper
status: open — at most k+1 distinct length-k Fibonacci subwords (Sturmian upper bound)
next: prove the Morse–Hedlund minimal-complexity upper bound for the
  characteristic (mechanical) word of slope 1/phi^2, i.e. that its length-k
  factor set has at most n+1 elements; the mechanical-word digit rule is
  already in PE1006G2Shell (code/lean/pe1006_psi_G2_mech_shell-1f79c34f.lean),
  so reduce the general-FibSubwords count to the mechanical-word factor count
  and bound that by k+1 via the three-distance / rotation structure.
```

```gap
id: subword-count-lower
lemma: PE1006SturmComplexity.subword_count_lower
status: open — at least k+1 distinct length-k Fibonacci subwords (existence/certificate)
next: exhibit k+1 explicit distinct translation windows of the characteristic
  word (the run's mechanical construction already computes them for k=1..400),
  form them as a Finset of size k+1 (decidable), and prove each lies in
  FibSubwords k; generalise the finite decide-certificate to arbitrary k by
  induction on the Sivasankar–Rama window-position theorem.
```

```gap
id: subword-limit-identification
lemma: (bridge) FibSubwords k equals the length-k factor set of the true limit
  word F = lim_n S_n; a Sturmian word is aperiodic, so no single S_n need carry
  every factor — the union is necessary.
status: open — needs a formal limit word (no Mathlib Sturmian library)
next: formalise the limit word as the pointwise limit of the nested chain
  (S_n is a prefix of S_{n+1}), characterising length-k factors of F as those
  occurring in some S_n; the nesting shell in
  pe1006_psi_G1_factor_chain-87f94deb.lean already supplies the monotone chain.
```
-/
