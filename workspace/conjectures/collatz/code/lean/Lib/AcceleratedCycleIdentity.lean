import Mathlib

namespace Collatz

/-- src: standard parity-vector expansion for the accelerated 3x+1 map;
    this file states the identity as a blueprint, not as a cited theorem. -/
def T (n : ℕ) : ℕ :=
  if Even n then n / 2 else (3 * n + 1) / 2

def Parity (n : ℕ) : Bool := decide (Odd n)

def AffineNumerator (bits : List Bool) : ℕ :=
  bits.foldl (fun acc b => if b then 3 * acc + 1 else acc) 0

/-- A finite parity word determines an affine numerator for iterates, subject
    to the divisibility hypotheses needed to identify the actual orbit. -/
theorem parity_word_affine_identity
    (n : ℕ) (bits : List Bool)
    (hpos : 0 < n)
    (hbits : ∀ i < bits.length, Parity ((T^[i]) n) = bits.get ⟨i, hbits⟩)
    : ∃ a : ℕ, (T^[bits.length]) n = a := by
  sorry

#print axioms parity_word_affine_identity

end Collatz
