# Reducer finding — H16.2 folded onto the open graphic (H₁₄³)

Durable decomposition, recorded while the Cognee memory server is down (see
CONTEXT.md "Recalled"). Re-deriving this finding would cost a later run a whole
turn; here it is, with every load taken from the claim ledger rather than from a
word in this file.

## The decomposition

- **Goal.** `H(2) < ∞` — every planar quadratic polynomial vector field has a
  number of limit cycles bounded uniformly over the family.
- **Frame (discharged from claims).** By the Roussarie/DRR reduction
  (`h16-drr-121-graphics`, `drr-1994-citation-anchor`, both asserted) H(2)<∞ is
  equivalent to finite cyclicity of every one of the 121 DRR graphics. The list
  is finite, so the whole conjecture is the maximum of finitely many cyclicity
  bounds — one open graphic is the entire remaining core.
- **Target selection (discharged from claims).** `g-drr-status` is discharged:
  Λ₀ = (H₁₄³), the semihyperbolic hemicycle through a triple nilpotent point at
  infinity with two semi-hyperbolic points along the equator, is the one
  triple-point-at-infinity graphic with no settled closure (`h16-drr-open-rows`,
  quoting RR 2015: "We have a partial result for every graphic, but one (namely
  (H₁₄³)), through a triple point at infinity"). Lu arXiv:2607.13785 (2026,
  UNREFEREED) CLAIMS it closed locally-uniformly (`drr-lu-claims-h14-3`) — so
  the run's job is to check that claim, not re-derive the whole theorem. The
  other partially-open center graphics are (I₆b¹),(H₁₃³),(DI₂b), boundary sets
  only (`drr-rr-boundary-only-for-3-graphics`).

## The three open gaps (research/backward/h16-2-h14-3-finite-cyclicity.md)

1. **G-lu-core** — the finite algebraic core of Lu's verification must stand up
   to clean-room exact recomputation (L₄=(AC+CD+2DF−EF)/8, L₆=−P/192 with its 30
   monomials, the Darboux cofactors, and the degree-8/10/12 ideal memberships
   L₈∈⟨L₄,L₆⟩, L₁₀,L₁₂∈⟨L₄,L₆,L₈⟩). Current claim `lu-finite-core-partially-verified`
   is **asserted-not-checked**: the degree-4/cofactor part was "re-derived by
   hand", the degree-6 equality was never re-executed, and `lyap_extend.py`
   CRASHED before finishing the extension. First move: `code/bautin/verify_lu_core.py`
   clean-room with sympy, captured to `code/out/lu_core.captured.txt`.
2. **G-lean-cert** — make the degree-6 30-monomial identity (192·L₆+P₃₀=0) a
   kernel-checked Lean theorem. `code/lean/Lib/BautinRecurrence.lean` currently
   defines P₃₀:=0 (placeholder), so the theorem is vacuous. First move: spell out
   all 30 monomials, put generated data as untrusted defs under
   `code/lean/Lib/Generated/`, checker by hand outside, close with `decide`.
3. **G-remainder** — the analytic lift from the center-ideal division
   (displacement = Σaᵢmᵢ(1+hᵢ), aᵢ in center ideal, hᵢ=o(1)) to a uniform
   ≤B-zeros in the collar. This is where analyticity must genuinely enter
   (test 1: a C^∞ version does not bound zeros — Dulac's error), and where
   uniformity must genuinely use compactness of the parameter box. Not
   machine-checked anywhere; the DRR-definition match (does Lu's collar+
   five-parameter result equal "finite cyclicity of the graphic" including the
   boundary-at-infinity) must be verified against held RR 2015 text.

## What would kill this reduction

- The zero-count never touching analyticity (a smooth falsity).
- G-lean-cert being vacuous (a certificate about the literal 0).
- Lu 2026 being wrong — in which case Λ₀ stays open and the target moves to
  (I₆b¹),(H₁₃³),(DI₂b), the three center graphics with boundary sets only.
