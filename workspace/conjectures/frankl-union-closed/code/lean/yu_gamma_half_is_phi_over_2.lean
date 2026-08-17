import Mathlib.Analysis.SpecialFunctions.Trigonometric.Basic
import Mathlib.NumberTheory.Real.GoldenRatio
import Mathlib.Analysis.Real.Sqrt
import Mathlib.Analysis.SpecialFunctions.Log.Basic

open Real

namespace YuGamma

/-- Binary entropy `h(x) = -x·log x - (1-x)·log(1-x)` on `[0,1]`, as a real
function. Mathlib's `Real.log 0 = 0` by convention, so extensions `h 0 = h 1 = 0`
coincide with the usual continuous convention. Only the symmetry `h(1-x) = h(x)`
is used by this claim's proofs. -/
noncomputable def h (x : ℝ) : ℝ := -(x * Real.log x + (1 - x) * Real.log (1 - x))

/-- The collapsed atom `a = (3 - √5)/2` of Yu's extremal at `t = 1/2`. At `t = 1/2`
the weight parameter satisfies `β = a`, so the coupling is
`P = (1-β)Q_{a,a} + βQ_{a,1}`. -/
noncomputable def a : ℝ := (3 - Real.sqrt 5) / 2

/-- The surviving marginal atom's weight `w₁ = 1 - β/2`, with `β = a` at `t = 1/2`:
the atom `p = a` carries weight `w₁`, the atom `p = 1` carries `β/2 = 1 - w₁`. -/
noncomputable def w1 : ℝ := 1 - a / 2

/-- Binary entropy symmetry `h(1-x) = h(x)`. This is what makes the numerator's
`h(2a - a²) = h(1 - a)` equal the denominator's `h(a)`. -/
theorem h_symm (x : ℝ) : h (1 - x) = h x := by
  unfold h
  have hx : 1 - (1 - x) = x := by ring
  rw [hx]
  ring

/-- `a² = 3a - 1`, i.e. `a` is a root of `X² - 3X + 1`; equivalently
`2a - a² = 1 - a`. -/
theorem a_sq : a ^ 2 = 3 * a - 1 := by
  unfold a
  have hsq : (Real.sqrt 5) ^ 2 = 5 := by
    rw [sq_sqrt (show (0 : ℝ) ≤ 5 by norm_num)]
  ring_nf
  nlinarith [hsq]

/-- `2a - a² = 1 - a`: the key collapse that turns `h(2a - a²)` into `h(1 - a)`. -/
theorem collapse_raw : 2 * a - a ^ 2 = 1 - a := by
  rw [a_sq]
  ring

/-- The α=0 collapsed coupling's ratio `g/Eh(p)`, stated multiplicatively:
the numerator `w₁²·h(2a - a²)` equals `w₁` times the denominator `w₁·h(a)`, so the
ratio collapses to `w₁ = 1 - a/2`. (Stated without division to avoid a
`h(a) ≠ 0` hypothesis.) -/
theorem value_ratio : w1 ^ 2 * h (2 * a - a ^ 2) = w1 * (w1 * h a) := by
  rw [collapse_raw, h_symm]
  ring

/-- `w₁ = 1 - a/2 = (1 + √5)/4`. -/
theorem w1_eq : w1 = (1 + Real.sqrt 5) / 4 := by
  unfold w1 a
  ring_nf

/-- `w₁ = φ/2`, where `φ = (1 + √5)/2` is the golden ratio. -/
theorem w1_eq_golden_half : w1 = Real.goldenRatio / 2 := by
  unfold w1 a Real.goldenRatio
  ring_nf

/-- `w₁ = cos(π/5) = cos(36°)`. Mathlib's trigonometric functions take radians;
`36° = π/5`. -/
theorem w1_eq_cos_pi_div_five : w1 = cos (Real.pi / 5) := by
  rw [Real.cos_pi_div_five]
  unfold w1 a
  ring_nf

/-- `h(1) = 0`: the entropy contribution of a coordinate at its maximal atom `1`
vanishes (this is how terms with any coordinate equal to `1` drop out of the
`E_{P^⊗2}` numerator). -/
theorem h_one : h 1 = 0 := by
  simp [h]

end YuGamma

#print axioms YuGamma.h_symm
#print axioms YuGamma.a_sq
#print axioms YuGamma.collapse_raw
#print axioms YuGamma.value_ratio
#print axioms YuGamma.w1_eq
#print axioms YuGamma.w1_eq_golden_half
#print axioms YuGamma.w1_eq_cos_pi_div_five
#print axioms YuGamma.h_one
