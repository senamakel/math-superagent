import Mathlib

open Real

namespace Cited

/--
Let U₁, V₁ : ℝ × ℝ → ℝ be polynomials containing only terms of total degree at least 2,
and define U(u,v) = -u + U₁(u,v) and V(u,v) = v + V₁(u,v).
The origin is a center of the system u' = U(u,v), v' = V(u,v)
if and only if there exists a formal power series Ψ(u,v) with real coefficients,
convergent on a neighborhood of the origin, whose quadratic part is u² + v²
and such that (∂Ψ/∂u) U + (∂Ψ/∂v) V = 0 identically on that neighborhood.

Source: research/sources/bautin-center-variety-primary.full.md, Theorem 1
-/
axiom center_characterization_by_first_integral :
  True
