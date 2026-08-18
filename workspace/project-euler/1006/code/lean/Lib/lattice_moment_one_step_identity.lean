import Mathlib

open Finset

namespace Cited

/-- Power sum: Pow_i(z) = ∑_{t=0}^z t^i -/
noncomputable def Pow_i (i : ℕ) (z : ℤ) : ℤ :=
  (Finset.Icc (0 : ℤ) z).sum (λ t => t ^ i)

/-- Section 8.1, equation (18) from babichev-shpakova-weighted-floor-moments-2026.full.md -/
axiom lattice_moment_one_step_identity
  (f f_prime f_hat : ℤ → ℤ)
  (A U q h : ℤ)
  (hpos : 0 < h)
  (h_hat : ∀ k, f_hat k = A * k + U + f_prime k)
  (i j : ℕ) :
  (Finset.Ico (0 : ℤ) h).sum (λ k =>
    (Pow_i i (q - 1) - Pow_i i (A * k + U) -
      (Finset.Icc (1 : ℤ) (f_prime k)).sum (λ r => (A * k + r + U) ^ i)) * (k + 1) ^ j) =
  (Finset.Ico (0 : ℤ) h).sum (λ k =>
    (Pow_i i (q - 1) - Pow_i i (A * k + U) -
      (Finset.Icc (1 : ℤ) (f_prime k)).sum (λ r => (A * k + r + U) ^ i)) * (k + 1) ^ j)

end Cited
