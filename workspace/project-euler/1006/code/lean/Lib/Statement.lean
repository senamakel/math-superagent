import Mathlib.Data.List.TakeDrop
import Mathlib.Data.Finset.Basic
import Mathlib.Data.Nat.Prime.Defs
import Mathlib.Data.Nat.GCD.Basic
import Mathlib.Data.Nat.ModEq
import Mathlib.Algebra.BigOperators.Intervals

/-!
# Project Euler 1006 — formal statement

We render the problem as a Lean specification and check that it elaborates.
Nothing is proved; every `theorem` here ends in `:= by sorry`.

Problem (from https://projecteuler.net/minimal=1006, saved at `problem.md`):

  * `S_0 = 0`, `S_1 = 01`, and `S_n = S_{n-1} S_{n-2}` (concatenation) for
    `n ≥ 2`.  Documents: `S_2 = 010`, `S_3 = 01001`, `S_4 = 01001010`.
  * A *Fibonacci subword* of length `k` is a length-`k` contiguous substring of
    some `S_n` (a factor of the infinite limit word).
  * There are exactly `k+1` distinct Fibonacci subwords of length `k`.
  * Reading each as a decimal number *ignoring leading zeros*, `Ψ(k)` is the
    sum of the squares of those `k+1` numbers.  Oracle values:
    `Ψ(3) = 20302` (factors `001,010,100,101` → 1²+10²+100²+101²), and
    `Ψ(10) ≡ 10699667 (mod 101001001)`.
  * Find `Ψ(10^18) mod 101001001`.

A word is a `List Char` (digits 0 and 1).  The limit word is obtained by
running the `S_n` recurrence until its length exceeds `k` (any
`S_n` with `length > k` contains every length-`k` factor of the infinite word).

## Reading of "ignore leading zeros"

`valueOf` folds `acc ↦ 10·acc + digit`.  A leading `0` contributes nothing
(`10·acc + 0 = 10·acc`), so leading zeros are ignored automatically, exactly as
`int('001') == 1` in the oracle.  This is the one place a re-reading could
differ: we interpret each factor as the *integer* it denotes, so two factors
that differ only in leading zeros are **not** "the same decimal number" unless
they are equal as words.  That matches the statement (which lists `001,010,100,101`
as four distinct subwords and sums `1²+10²+100²+101²`).
-/

namespace PE1006

/-- The `S_n` Fibonacci word: `S_0 = 0`, `S_1 = 01`, `S_n = S_{n-1} S_{n-2}`. -/
def fibWord : ℕ → List Char
  | 0 => ['0']
  | 1 => ['0', '1']
  | n + 2 => fibWord (n + 1) ++ fibWord n

/-- Digit value of one character (0 or 1). -/
def digitVal (c : Char) : ℕ := if c = '0' then 0 else 1

/-- Decimal value of a word, ignoring leading zeros (fold from the left). -/
def valueOf : List Char → ℕ :=
  List.foldl (fun acc c => acc * 10 + digitVal c) 0

/-- All length-`k` contiguous substrings (factors) of a word `w`. -/
def slidingFactors [DecidableEq α] (w : List α) (k : ℕ) : Finset (List α) :=
  (Finset.range (w.length - k + 1)).image fun i => (w.drop i).take k

/-- `Ψ(k)`: sum of the squares of the decimal values of the distinct length-`k`
Fibonacci subwords.  Index `fibWord (k + 2)` has length the (k+2)-nd Fibonacci
number, which exceeds `k`, so it samples every length-`k` factor of the limit. -/
noncomputable def Psi (k : ℕ) : ℕ :=
  ((slidingFactors (fibWord (k + 2)) k).image valueOf).sum fun n => n * n

/-- `Ψ(k)` reduced modulo the stated modulus. -/
noncomputable def PsiResidue (k : ℕ) : ℕ := Psi k % 101001001

/-- The problem's modulus. -/
def M : ℕ := 101001001

theorem modulus_prime : Nat.Prime M := by
  sorry

/-- `10` is invertible mod `M` (only invertibility, not primeness, is needed
by the floor-sum method's `x = 10⁻¹`). -/
theorem ten_invertible : Nat.Coprime 10 M := by
  sorry

/-- The two worked examples from the statement, as a checkable oracle lemma. -/
theorem oracle_examples :
    Psi 3 = 20302 ∧
    Psi 10 % M = 10699667 := by
  sorry

/-- The structural fact the statement asserts: there are exactly `k+1` distinct
length-`k` Fibonacci subwords (the Fibonacci word is Sturmian). -/
theorem fib_word_factor_count (k : ℕ) :
    (slidingFactors (fibWord (k + 2)) k).card = k + 1 := by
  sorry

/-- The problem's answer, read as a congruence plus a size bound on the witness.

Let `T = Ψ(10^18)`.  The answer `A` is the least residue of `T` modulo
`101001001`, i.e. the unique `A < 101001001` with `T ≡ A (mod 101001001)`.
This is a *specification* of the answer; the concrete value of `A` is what the
run computes.  (The statement is intentionally given existentially because the
specific numeric residue is not known to the formalisation yet.)
-/
theorem pe1006 :
    ∃ A : ℕ, A < M ∧ PsiResidue 1000000000000000000 = A := by
  sorry

end PE1006

#print axioms PE1006.pe1006
#print axioms PE1006.oracle_examples
#print axioms PE1006.fib_word_factor_count
