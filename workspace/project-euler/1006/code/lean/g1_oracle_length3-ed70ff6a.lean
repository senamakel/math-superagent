import Mathlib.Data.Set.Basic
import Mathlib.Data.Set.Finite.Basic
import Mathlib.Data.Set.Card
import Mathlib.Algebra.BigOperators.Intervals

/-!
# G1 — oracle: the length-3 Fibonacci subwords (PE1006)

Node `g1-oracle-length3` (from `research/notes/g1-formalisation-status.md`).

Informal claim, tracked binder-by-binder:

> The length-3 Fibonacci subwords are exactly 001, 010, 100, 101 — i.e. the
> length-3 factor set of S_5 = 0100101001001 has card 4 = 3+1 and equals
> {001, 010, 100, 101}.

Which binders each statement carries:

* **`fibWord n`** — the finite Fibonacci word `S_n` exactly as `problem.md`
  defines it: `S_0 = 0`, `S_1 = 01`, `S_{n+2} = S_{n+1} ++ S_n`.  The statement
  fixes `n = 5`.
* **`factorsFinset w k`** — the *distinct* length-`k` contiguous factors of a
  word `w`, as a `Finset` (image deduplicates, so `card` counts distinct
  factors).  The statement fixes `w = fibWord 5`, `k = 3`.
* **`oracle_length3_factors`** — `factorsFinset (fibWord 5) 3` equals the
  four-word set `{010, 001, 100, 101}`.  The two hypotheses of the claim
  (`S_5 = 0100101001001`, `k = 3`) are fixed numerically in the statement, not
  left as parameters: the node is only about this one oracle case, so there are
  no free binders to carry.
* **`oracle_length3_card`** — that factor set has cardinality `3 + 1`, the
  `k + 1 = 4` that the general count theorem quantifies with.

The proof is a kernel computation: `factorsFinset`, `fibWord`, and the four
literal words are all `def`s, so `decide` reduces the equality and the
cardinality to `rfl`.  No `native_decide` (the compiler-trusted reducer) is
used; every step is checked by the kernel's own evaluator, so the verdict is
`formalised`, not a compiler promise.
-/

namespace PE1006G1

/-- `S_n`: `S_0 = 0`, `S_1 = 01`, `S_{n+2} = S_{n+1} ++ S_n`. -/
def fibWord : ℕ → List Char
  | 0 => ['0']
  | 1 => ['0', '1']
  | n + 2 => fibWord (n + 1) ++ fibWord n

/-- The distinct length-`k` contiguous factors of `w`, as a `Finset`.
The image deduplicates, so `card` is the number of distinct length-`k`
subwords (`0 ≠ 00`, matching the problem's four distinct words). -/
def factorsFinset (w : List Char) (k : ℕ) : Finset (List Char) :=
  (Finset.range (w.length - k + 1)).image (fun i => (w.drop i).take k)

/-- The statement's own data: `S_5 = 0100101001001`
(`S_5 = S_4 ++ S_3 = 01001010 ++ 01001`). -/
lemma oracle_s5 : fibWord 5 = ['0','1','0','0','1','0','1','0','0','1','0','0','1'] := by
  decide

/-- The length-3 Fibonacci subwords are exactly 001, 010, 100, 101: the
length-3 factor set of `S_5` equals the four-word set
`{010, 001, 100, 101}`. -/
theorem oracle_length3_factors :
    factorsFinset (fibWord 5) 3
      = {['0','1','0'], ['0','0','1'], ['1','0','0'], ['1','0','1']} := by
  decide

/-- That factor set has cardinality `4 = 3 + 1`, the `k + 1` of the general
count theorem specialised to `k = 3`. -/
theorem oracle_length3_card : (factorsFinset (fibWord 5) 3).card = 3 + 1 := by
  decide

end PE1006G1

#print axioms PE1006G1.oracle_length3_factors
#print axioms PE1006G1.oracle_length3_card
