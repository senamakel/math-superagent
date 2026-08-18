# Decision: adopted compensator-pfaffian-mourtada-moussu-synthesis

Recorded 2026 (inventor, converge turn). Memory server was down, so this durable
finding is written here until `remember_memory` recovers.

## The combination the converge turn produced

Candidate 3 (pfaffian-chain-return-map) was grounded-but-incomplete: it needed a
single bounded-format Pfaffian chain for the open non-hyperbolic graphics, and
research found no construction. The converge turn's better outcome: **read the
chain off the normal form that the run already holds**.

- RSZ/RR Theorem 2.3 (held, `research/sources/rousseau-rousseau-2015-center-graphics-arxiv.full.md`
  §2.6.2, `rousseau-shan-zhu-2015-second-type-dulac-full.full.md` §2.6) gives the
  second-type Dulac map in closed form: compensator ω(x,α) = (x^{-α}−1)/α, powers
  x^{σ̄}, x^{1/l}, plus a property-J remainder C^{l−2} in generalized monomials.
- Mourtada–Moussu (Bull. SMF, DOI 10.24033/bsmf.2297): the Dulac map of a reduced
  analytic 1-form is 1-Pfaffian **iff** the form is analytically normalisable.

These two facts combined mean the Pfaffian chain is not a guess: it is the normal
form itself, and its format (chain order 6, degree 2 on the regularized chart
x = r/r₀ ∈ [ε,M]) is read off the compensator/power monomials, with parameters
(α, σ̄, 1/l) appearing only as coefficients — hence the format is uniform over the
parameter stratum. This is what candidate 3 was missing.

## Test 1 (smooth test) location

The step that fails for C^∞-but-not-analytic fields is exactly
`analytically normalisable ⇒ Pfaffian`. A non-normalisable passage is not
Pfaffian and hence not zero-bounded by Khovanskii. The method cannot overstep
smoothness, because its chain is the analytic normal form.

## Named falsifier

The one computation that settles live-vs-refuted: compose the four second-type
maps δᵢ (Shan thesis §4.2, eq. 4.2.1) with the regular transitions U, R₁ and the
central saddle-node transition R, and test whether the composed displacement
keeps a fixed finite chain or introduces a new parameter-dependent exponent per
passage. A new exponent per passage = format unbounded over the stratum =
refuted (narrows to Kaloshin's elementary restriction).

## Refinement forced by reading the full MM 1997 text

The verbatim MM 1997 paper (now held at
`research/sources/mourtada-moussu-dulac-pfaffiennes.pdf.full.md`) refines the
synthesis in a way the Numdam abstract-page digest missed:

- MM's theorem is `1-Pfaffian ⇔ analytically normalisable`, where **1-Pfaffian**
  is the STRONG notion: the graph of the *whole* Dulac map lies on one analytic
  curve with isolated singularity. The paper's own conclusion: the Khovanskii
  route "est assez limité" — reserved for generic/integrable cases.
- Therefore the **strong** claim ("the whole Dulac map is Pfaffian") is refuted
  for the open graphics. The adopted synthesis is the honest refinement: use the
  RSZ/RR Theorem 2.3 **normal-form decomposition** D = leading + φ_A, where only
  the leading part (powers + compensator) is Khovanskii-Pfaffian of fixed format,
  and φ_A is controlled by DIR derivation-division.
- The MM theorem is still the load-bearing analyticity locator: a
  smooth-but-not-analytic form is not analytically normalisable, hence its Dulac
  map is not 1-Pfaffian, so a purely smooth bound would fail at this exact step.
- Full statement filed as claim `mourtada-moussu-1997-dulac-pfaffian-iff-normalisable`
  (research/claims/mourtada-moussu-1997-dulac-pfaffian-iff-normalisable.md).

## Status of the verification

The sympy probe `code/pfaffian/verify_compensator_chain.py` was WRITTEN but NOT
RUN (no shell available during the decision turn). Its claim — each dfᵢ/dx
polynomial in the chain variables — is asserted, not yet
verified-computationally. The first-step hands it to tool_builder to execute and
capture.

## The three candidates' disposition

- resurgent-borel-bridge-equation: refuted (killed-by: no sourced parameter-uniform
  bridge rank / zero-multiplicity theorem; resurgence is for individual Dulac
  finiteness, not uniform H(2)).
- cohomological-divergence-coboundary: refuted (killed-by: no theorem identifying
  the full four-Dulac displacement with a finite relative-period vector; Abelian
  methods need Hamiltonian ovals; Livšic needs hyperbolic dynamics).
- pfaffian-chain-return-map: narrowed (survives: Kaloshin's elementary restriction
  E(k) ≤ 2^{25k²}; its open-graphic extension is carried by the adopted synthesis).
