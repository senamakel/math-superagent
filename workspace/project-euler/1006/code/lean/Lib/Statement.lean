import Mathlib

open Set
open List

/-!
Formalisation of Project Euler problem 1006.

Fibonacci subwords, their decimal values, and the sum-of-squares function Ψ(k).

Reference: https://projecteuler.net/minimal=1006

Definitions follow the problem statement exactly:
- S_n are defined by S₀ = "0", S₁ = "01", S_{n+2} = S_{n+1} ++ S_n.
- A Fibonacci subword of length k is a contiguous substring of length k
  occurring in at least one S_n.
- For a binary string x = x₀x₁…x_{k-1}, val(x) = Σ_{j=0}^{k-1} xⱼ·10^{k-1-j},
  i.e., the binary string is read as a decimal number (leading zeros permitted).
- Ψ(k) = Σ_{x∈F_k} val(x)² where F_k is the set of distinct length-k
  Fibonacci subwords.

Known anchors from the problem:
  F₃ = {001, 010, 100, 101}  ⇒  Ψ(3) = 1² + 10² + 100² + 101² = 20302.
  Ψ(10) ≡ 10699667 (mod 101001001).

The answer sought is Ψ(10¹⁸) mod 101001001.
-/
namespace PE1006

/-- The modulus given in the problem statement. -/
def M : ℕ := 101001001

/--
Fibonacci word S_n, as a list of bits.
`false` represents the digit 0 and `true` represents the digit 1.
-/
def fibWord : ℕ → List Bool
  | 0   => [false]
  | 1   => [false, true]
  | n+2 => fibWord (n+1) ++ fibWord n

/--
Length-k contiguous windows of a word w, i.e. all contiguous substrings
whose length is exactly k.
-/
def windows (w : List Bool) (k : ℕ) : Set (List Bool) :=
  { x | ∃ i : ℕ, x = (w.drop i).take k ∧ x.length = k }

/--
F_k : the set of binary strings of length k that occur as a contiguous
substring in some S_n.
-/
def fibSubwords (k : ℕ) : Set (List Bool) :=
  ⋃ n : ℕ, windows (fibWord n) k

/--
Interpret a binary string as a decimal number.
Given x₀x₁…x_{k-1}, val(x) = Σⱼ xⱼ·10^{k-1-j}.

Leading zeros are therefore allowed and contribute nothing to the value.
-/
def decVal : List Bool → ℕ
  | []     => 0
  | b :: bs => (if b then 1 else 0) * 10 ^ bs.length + decVal bs

/--
Ψ(k) = Σ_{x∈F_k} val(x)².

The set F_k is finite (it has exactly k+1 elements, by the Sturmian
complexity of the Fibonacci infinite word), so we sum using Finset.
The definition is noncomputable because proving finiteness requires
the Sturmian theory.
-/
noncomputable def psi (k : ℕ) : ℕ := by
  classical
  exact if h : (fibSubwords k).Finite then
    (h.toFinset).sum (λ x => (decVal x) ^ 2)
  else 0

/--
Placeholder for the unknown answer.
Once computed, replace `answer` with the value satisfying the congruence.
-/
opaque answer : ℕ

/--
Statement of Project Euler problem 1006.

The theorem asserts that Ψ(10¹⁸) and `answer` are congruent modulo M.
The proof (by `sorry`) is the computational challenge; the theorem is
stated here as the target.
-/
theorem projectEuler1006 : psi (10^18) % M = answer % M := by
  sorry

#print axioms projectEuler1006

end PE1006
