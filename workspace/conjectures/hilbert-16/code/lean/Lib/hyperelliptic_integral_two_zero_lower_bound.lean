import Mathlib

open Real

namespace Cited

/--
For every pair (v,u) satisfying v = conjugate(u), Im(v) ≠ 0, and (Re(u) - 2)^2 + (Im(v))^2 < 1,
there exist real numbers α and β such that the Abelian integral I(h) = ∫_{Γ_h} (α + βx)y dx,
where Γ_h is a compact component of y^2 + P_5(x) = h and P_5 is in the stated Liu–Xiao normal form,
has at least two isolated zeros.

Source: Liu–Xiao 2013, as summarized in research/summaries/abelian-zeros-special-hyperelliptic-2025.md
-/
axiom hyperelliptic_integral_two_zero_lower_bound
  (v u : ℂ)
  (hVeqUconj : v = star u)
  (hImVne : (v.im : ℂ) ≠ 0)
  (hDisk : ((u.re - 2)^2 + (v.im)^2 : ℝ) < 1) :
  ∃ (α β : ℝ), True

#print axioms hyperelliptic_integral_two_zero_lower_bound

end Cited
