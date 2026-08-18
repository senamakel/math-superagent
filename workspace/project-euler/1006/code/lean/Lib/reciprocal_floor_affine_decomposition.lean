import Mathlib

open Nat

namespace Cited

/-
Source: research/sources/babichev-shpakova-weighted-floor-moments-2026.full.md,
Section 5.2, equations (11) and (13)

Let a and b be positive integers with 0 < b < a, let β be an integer with 0 ≤ β < a,
and define f(t) = floor((b*t + β)/a). Put u = a - β - 1.
For every integer k with 0 ≤ k < h, where h is the appropriate reciprocal-query range,
floor((a*k + u)/b) = A*k + U + f'(k), where A = floor(a/b), U = floor(u/b),
b' = a - A*b, β' = u - U*b, and f'(k) = floor((b'*k + β')/b).
-/
axiom reciprocal_floor_affine_decomposition
  (a b β : ℕ)
  (ha_pos : 0 < a)
  (hb_pos : 0 < b)
  (hb_lt_a : b < a)
  (hβ_lt_a : β < a)
  (h : ℕ)
  : ∀ k, k < h →
    let u := a - β - 1
    let A := a / b
    let U := u / b
    let b' := a - A * b
    let β' := u - U * b
    (a * k + u) / b = A * k + U + (b' * k + β') / b

end Cited
