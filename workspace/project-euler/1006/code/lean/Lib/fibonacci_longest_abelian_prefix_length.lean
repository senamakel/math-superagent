import Mathlib

open Nat

-- Citation: Fici et al., arXiv:1209.6013, abstract
-- "Let F_n be the Fibonacci numbers and f the infinite Fibonacci word (as indexed in the source).
--  For every integer j > 1, the longest prefix of f that is an abelian repetition of period F_j
--  has length F_j*(F_{j+1} + F_{j-1} + 1) - 2 if j is even, and F_j*(F_{j+1} + F_{j-1}) - 2 if j is odd."

namespace Cited

/-- The Fibonacci numbers: F_0 = 0, F_1 = 1, F_{n+2} = F_{n+1} + F_n -/
def fib : ℕ → ℕ
  | 0 => 0
  | 1 => 1
  | n + 2 => fib (n + 1) + fib n

/-- The infinite Fibonacci word over {0,1}, as a function ℕ → ℕ. -/
def fibWord : ℕ → ℕ := sorry

/-- A finite word w is an abelian repetition of period p if w can be written as
    w = u_1 u_2 ... u_k where each u_i has length p and all u_i are permutations
    of each other (i.e., each letter appears the same number of times in each block). -/
def IsAbelianRepetition (w : List ℕ) (p : ℕ) : Prop := sorry

/-- The length of the longest prefix of the infinite Fibonacci word that is
    an abelian repetition of period F_j. -/
def longestAbelianPrefixLength (j : ℕ) : ℕ := sorry

/-- Fici, G.; Lepistö, A.; and Salmela, L. "Abelian repetitions in the Fibonacci word."
    arXiv:1209.6013, 2012. -/
axiom fibonacci_longest_abelian_prefix_length (j : ℕ) (hj : 1 < j) :
    longestAbelianPrefixLength j =
      if Even j then
        fib j * (fib (j + 1) + fib (j - 1) + 1) - 2
      else
        fib j * (fib (j + 1) + fib (j - 1)) - 2

end Cited
