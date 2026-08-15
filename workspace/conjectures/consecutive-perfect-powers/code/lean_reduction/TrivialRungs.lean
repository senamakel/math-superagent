import Mathlib

/-!
# Catalan: the trivial rungs

Two elementary "rungs" of the Catalan ladder, kernel-checked:

**R-trivial-bases.**  No solution of `x ^ p - y ^ q = 1` with `0 < x, 0 < y`
and `1 < p, 1 < q` has `x = 1` or `y = 1`.

**R-p-eq-q.**  `x ^ p - y ^ p = 1` has no positive solution for any prime `p`
(hence in particular for every odd prime `p`, the form stated in the workspace's
`R-p-eq-q` claim).  The argument is the factorisation
`x ^ p - y ^ p = (x - y) * S` with `S = Σ x^i y^(p-1-i)`; the right-hand side
equals `1` and both factors are positive, so both are `1`, contradicting
`S ≥ p ≥ 2`.

Every lemma here is evaluated against the known solution `(3,2,2,3)`: both bases
are `≥ 2` (so neither trivial-base lemma eliminates it) and its exponents are
`2 ≠ 3` (so `R-p-eq-q` sits outside the symmetric prime case and claims nothing
about it).  None of these over-prove.
-/

namespace CatalanRungs

/-! ## R-trivial-bases -/

/-- If `x = 1` then `1 - y^q = 1`, forcing `y^q = 0`, contradicting `0 < y`. -/
theorem no_x_eq_one {x y p q : ℕ} (hx : 0 < x) (hy : 0 < y) (_hp : 1 < p)
    (_hq : 1 < q) (hEq : x ^ p - y ^ q = 1) : x ≠ 1 := by
  intro hx1
  have hEq' : 1 ^ p - y ^ q = 1 := by simpa [hx1] using hEq
  have hsub : 1 - y ^ q = 1 := by simpa using hEq'
  have hyq0 : y ^ q = 0 := by
    -- 1 - y^q = 1 in ℕ forces y^q = 0
    by_contra hnot
    have hyqpos : 0 < y ^ q := by omega
    have hle : 1 ≤ y ^ q := hyqpos
    have : 1 - y ^ q = 0 := Nat.sub_eq_zero_of_le hle
    omega
  have hypos : 0 < y ^ q := Nat.pow_pos hy
  omega

/-- If `y = 1` then `x^p - 1 = 1`, forcing `x^p = 2`, impossible for `0 < x,
    `1 < p`. -/
theorem no_y_eq_one {x y p q : ℕ} (hx : 0 < x) (_hy : 0 < y) (hp : 1 < p)
    (_hq : 1 < q) (hEq : x ^ p - y ^ q = 1) : y ≠ 1 := by
  intro hy1
  have hEq' : x ^ p - 1 ^ q = 1 := by simpa [hy1] using hEq
  have hsub : x ^ p - 1 = 1 := by simpa using hEq'
  have hxpow : x ^ p = 2 := by
    have hxple : 1 ≤ x ^ p := (Nat.pow_pos hx).le
    omega
  by_cases hxl : x ≤ 1
  · have hx1 : x = 1 := by omega
    subst x
    simp at hxpow
  · have hx2 : 2 ≤ x := by omega
    have hp2 : 2 ≤ p := by omega
    have h4le2 : 4 ≤ 2 ^ p := by
      simpa using (pow_le_pow_right₀ (by norm_num : (1 : ℕ) ≤ 2) hp2)
    have h2lex : 2 ^ p ≤ x ^ p := Nat.pow_le_pow_left hx2 p
    have h4lex : 4 ≤ x ^ p := le_trans h4le2 h2lex
    omega

/-! ## R-p-eq-q -/

/-- Each power-product term `x^i * y^(p-1-i)` in the geometric sum is at least `1`. -/
lemma one_le_term {x y : ℕ} (hx : 1 ≤ x) (hy : 1 ≤ y) (i n : ℕ) :
    1 ≤ x ^ i * y ^ (n - 1 - i) := by
  have hxp : 0 < x := by omega
  have hyp : 0 < y := by omega
  have h1 : 1 ≤ x ^ i := Nat.one_le_pow i x hxp
  have h2 : 1 ≤ y ^ (n - 1 - i) := Nat.one_le_pow (n - 1 - i) y hyp
  exact one_le_mul h1 h2

/-- The geometric sum has `p` terms each `≥ 1`, so it is `≥ p`. -/
lemma geom_sum_ge {x y p : ℕ} (hx : 1 ≤ x) (hy : 1 ≤ y) (hp2 : 2 ≤ p) :
    p ≤ ∑ i ∈ Finset.range p, x ^ i * y ^ (p - 1 - i) := by
  calc
    p ≤ ∑ _i ∈ Finset.range p, (1 : ℕ) := by simp
    _ ≤ ∑ i ∈ Finset.range p, x ^ i * y ^ (p - 1 - i) := by
      exact Finset.sum_le_sum (by intro i _hi; exact one_le_term hx hy i p)

/-- `x ^ p - y ^ p = 1` has no positive solution for any prime `p`. -/
theorem r_p_eq_q (x y p : ℕ) (hx : 0 < x) (hy : 0 < y) (hp : Nat.Prime p)
    (hEq : x ^ p - y ^ p = 1) : False := by
  have hpos : 0 < x ^ p - y ^ p := by rw [hEq]; norm_num
  have hyp_lt : y ^ p < x ^ p := (Nat.sub_pos_iff_lt).mp hpos
  have hyltx : y < x := (Nat.pow_lt_pow_iff_left (by omega : p ≠ 0)).mp hyp_lt
  -- factorisation in ℕ: S * (x - y) = x^p - y^p
  have hfac := geom_sum₂_mul_of_ge hyltx.le p
  let S : ℕ := ∑ i ∈ Finset.range p, x ^ i * y ^ (p - 1 - i)
  have h1 : S * (x - y) = 1 := by
    simpa [S] using hfac.trans hEq
  have dvdS : S ∣ 1 := by
    refine ⟨x - y, ?_⟩
    exact h1.symm
  have hS : S = 1 := (Nat.dvd_one).mp dvdS
  have hx1 : 1 ≤ x := by omega
  have hy1 : 1 ≤ y := by omega
  have hp2 : 2 ≤ p := hp.two_le
  have hSge : p ≤ S := by
    dsimp [S]
    exact geom_sum_ge hx1 hy1 hp2
  have hSge2 : 2 ≤ S := le_trans hp2 hSge
  omega

/-! #print axioms scan -/
#print axioms CatalanRungs.no_x_eq_one
#print axioms CatalanRungs.no_y_eq_one
#print axioms CatalanRungs.r_p_eq_q

end CatalanRungs
