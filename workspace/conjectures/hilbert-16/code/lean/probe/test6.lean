import Mathlib

open MvPolynomial

variable (l : ℕ) (A : Matrix (Fin 2) (Fin (2*l)) ℤ)

-- The map φ : MvPolynomial (Fin (2*l)) ℂ → MvPolynomial (Fin (2 + l)) ℂ
-- We use eval₂ with:
-- f : ℂ →+* MvPolynomial (Fin (2 + l)) ℂ (the inclusion)
-- g : Fin (2*l) → MvPolynomial (Fin (2 + l)) ℂ (the images of variables)

-- For the target, we use Fin (2 + l) indexing:
-- 0 to l-1: y variables (Fin.castAdd l)
-- l: t₁ (Fin.last l)
-- l+1: t₂ (Fin.last (l+1))

-- For the source, we use Fin (2*l) indexing:
-- 0 to l-1: x_i (Fin.castAdd l)
-- l to 2l-1: x_{l+i} (Fin.natAdd l)

-- The map:
-- φ(x_i) = y_i * t₁^{c_{i,0}} * t₂^{c_{i,1}} for i < l
-- φ(x_{l+i}) = y_{l-i-1} * t₁^{c_{l-i-1,1}} * t₂^{c_{l-i-1,0}} for i < l

-- But wait, the source says:
-- φ(x_i) = y_i * t₁^{c_{i1}} * t₂^{c_{i2}} for i = 1,...,l
-- φ(x_{l+i}) = y_{l-i+1} * t₁^{c_{l-i+1,2}} * t₂^{c_{l-i+1,1}} for i = 1,...,l

-- In 0-indexed:
-- φ(x_i) = y_i * t₁^{c_{i,0}} * t₂^{c_{i,1}} for i = 0,...,l-1
-- φ(x_{l+i}) = y_{l-i} * t₁^{c_{l-i-1,1}} * t₂^{c_{l-i-1,0}} for i = 0,...,l-1

-- Wait, let me re-index. The source uses 1-indexed:
-- φ(x_{l+i}) = y_{l-i+1} * t₁^{c_{l-i+1,2}} * t₂^{c_{l-i+1,1}} for i = 1,...,l
-- In 0-indexed, let i' = i-1, so i' = 0,...,l-1:
-- φ(x_{l+i'+1}) = y_{l-i'} * t₁^{c_{l-i',2}} * t₂^{c_{l-i',1}}
-- So φ(x_{l+i'}) = y_{l-i'-1} * t₁^{c_{l-i'-1,1}} * t₂^{c_{l-i'-1,0}} for i' = 0,...,l-1

-- Hmm, this is still confusing. Let me just use the source directly.

-- Actually, I think the simplest approach is to define the map using a function
-- that takes a Fin (2*l) and returns the appropriate monomial.

def φ_map : Fin (2*l) → MvPolynomial (Fin (2 + l)) ℂ := by
  intro i
  -- We need to decide whether i is in the first half or second half
  -- i.val < l means i is in the first half
  by_cases h : (i : ℕ) < l
  · -- i is in the first half: φ(x_i) = y_i * t₁^{c_{i,0}} * t₂^{c_{i,1}}
    let i' : Fin l := ⟨i, h⟩
    exact X (Fin.castAdd l i') * 
      (X (Fin.last l)) ^ (A 0 i') * 
      (X (Fin.last (l+1))) ^ (A 1 i')
  · -- i is in the second half: φ(x_i) = y_{l-(i-l)-1} * t₁^{c_{l-(i-l)-1,1}} * t₂^{c_{l-(i-l)-1,0}}
    have h' : (i : ℕ) - l < l := by
      have : (i : ℕ) < 2*l := i.2
      omega
    let i' : Fin l := ⟨(i : ℕ) - l, h'⟩
    -- The y index is l - (i-l) - 1 = 2*l - i - 1
    -- But we need to embed this into Fin l
    -- Actually, the source says y_{l-i+1} for the second half
    -- In 0-indexed: y_{l-i-1} where i is the 0-indexed second half index
    -- Let me use a different approach: define the y index directly
    sorry
  -- This is getting too complex. Let me try a different approach.

-- Let me try using a simpler indexing scheme.
