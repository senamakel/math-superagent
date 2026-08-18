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
theorem specialises it to the one representation `δ` is given by: per `p ∈ K`,
rewrite the zero set through `reduction.representation p hp` and apply
`reduction.ect_property p hp (reduction.coefficient p) (reduction.nonzero p
hp)`, with the uniform bound `N := reduction.dimension - 1` pulled out of the
`∀ p`.  Closed; kernel-verified with axioms exactly
`[propext, Classical.choice, Quot.sound]`.
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
  refine ⟨reduction.dimension - 1, ?_⟩
  intro p hp
  have hz : {x : Section | δ p x = 0} =
      {x : Section | (∑ i, reduction.coefficient p i * reduction.basis i p x) = 0} := by
    ext x
    simp only [Set.mem_ofPred_eq]
    constructor
    · intro h
      rw [← reduction.representation p hp x, h]
    · intro h
      rw [reduction.representation p hp x, h]
  rw [hz]
  exact reduction.ect_property p hp (reduction.coefficient p) (reduction.nonzero p hp)

#print axioms full_graphic_zero_bound

/- gap
id: slow-divergence-ect-partial-specialisation
lemma: ∀ (K, δ, hK, endpoint_maps, analytic_uniform_remainder,
  reduction : ECTReduction K δ holding), ∃ N, ∀ p ∈ K, δ's zero set on the
  section is finite with ncard ≤ N
status: closed
next: none — closed by rewrite-through-representation + ect_property, uniform
  N = dimension - 1; verified 2026-08-18, axioms [propext, choice,
  Quot.sound].  The three binder hypotheses hK, hendpoint, hanalytic are
  intentionally unused by this specialisation step and remain in the
  statement (they carry the conditional content of the node, to be supplied
  by the endpoint-maps and analytic-remainder work).
-/

end SlowDivergenceECTPartial
