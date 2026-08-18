import Mathlib

/-!
A precise conditional node for the adopted slow-divergence/ECT route.
The target is the full I^1_6b quadratic graphic, whose non-boundary blown-up
strata contain four second-type Dulac maps.  The literature supplies neither
the required endpoint germs nor the finite-rank reduction, so those are
explicit hypotheses rather than silently asserted facts.

FIX (this pass): the previous version's `ECTReduction.ect_zero_bound` field
asserted the theorem's conclusion (finiteness + the ncard bound) directly as
assumed data for the one displacement `δ` in question, so the proof was an
unpacking of that assumption rather than a derivation from an ECT property of
the `basis` family. `endpoint_maps`, `analytic_uniform_remainder`, and `_hK`
were unused (`_`-prefixed) decoration. `ECTReduction` now states the actual
ECT hypothesis — every nontrivial linear combination of the basis has a
bounded, finite zero set, matching `Lib/ECTSlowDivergence.ECTFamily` — and the
theorem specialises it to the one representation `δ` is given by, left
`sorry` since that specialisation is the genuine (if routine, given
`ECTSlowDivergence.displacement_zero_bound`) step this node has not yet
discharged.
-/
namespace SlowDivergenceECTPartial

abbrev Parameter := ℝ × ℝ
abbrev Section := ℝ

/-- A finite-dimensional candidate ECT family on the common section: `δ` is a
nontrivial linear combination of `basis`, and every nontrivial combination of
`basis` itself has a finite, bounded zero set (the ECT property, not baked in
for `δ` alone). -/
structure ECTReduction (K : Set Parameter)
    (δ : Parameter → Section → ℝ) where
  dimension : ℕ
  basis : Fin dimension → Parameter → Section → ℝ
  coefficient : Parameter → Fin dimension → ℝ
  representation : ∀ p ∈ K, ∀ x : Section,
    δ p x = ∑ i, coefficient p i * basis i p x
  nonzero : ∀ p ∈ K, ∃ i, coefficient p i ≠ 0
  ect_property : ∀ p ∈ K, ∀ c : Fin dimension → ℝ, (∃ i, c i ≠ 0) →
    ({x : Section | (∑ i, c i * basis i p x) = 0}).Finite ∧
      Set.ncard {x : Section | (∑ i, c i * basis i p x) = 0} ≤ dimension - 1

/-- Partial claim: once the four second-type Dulac maps have an analytic,
parameter-uniform remainder and a finite-rank ECT reduction, their displacement
has a finite uniform zero bound on K.  `endpoint_maps` is deliberately a
proposition: no complete second-type endpoint formula is currently available
in the held literature. -/
theorem full_graphic_zero_bound
    (K : Set Parameter) (δ : Parameter → Section → ℝ)
    (hK : IsCompact K)
    (endpoint_maps : Prop)
    (analytic_uniform_remainder : Prop)
    (reduction : ECTReduction K δ)
    (hendpoint : endpoint_maps)
    (hanalytic : analytic_uniform_remainder) :
    ∃ N : ℕ, ∀ p ∈ K,
      ({x : Section | δ p x = 0}).Finite ∧
      Set.ncard {x : Section | δ p x = 0} ≤ N := by
  sorry

#print axioms full_graphic_zero_bound

/- gap
id: slow-divergence-ect-partial-specialisation
lemma: ∀ (K, δ, hK, endpoint_maps, analytic_uniform_remainder,
  reduction : ECTReduction K δ holding), ∃ N, ∀ p ∈ K, δ's zero set on the
  section is finite with ncard ≤ N
status: sorry
next: rewrite `{x | δ p x = 0}` as `{x | ∑ i, reduction.coefficient p i *
  reduction.basis i p x = 0}` via `reduction.representation`, then apply
  `reduction.ect_property p hp reduction.coefficient (reduction.nonzero p hp)`
  — the same rewrite-then-apply shape `ECTSlowDivergence.displacement_zero_
  bound` already uses for the single-point case; the remaining work is
  threading it through the `∀ p ∈ K` quantifier and picking a uniform `N`
  (e.g. `reduction.dimension - 1`, since the ECT bound is uniform in `p`).
-/

end SlowDivergenceECTPartial
