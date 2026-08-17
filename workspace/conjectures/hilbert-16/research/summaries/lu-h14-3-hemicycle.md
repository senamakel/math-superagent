# Lu 2026 — Local uniform finite cyclicity of the H³₁₄ semihyperbolic hemicycle

Full text: [[lu-h14-3-hemicycle-html.full]] (arXiv:2607.13785, v2; preprint). See
also the abstract page [[lu-h14-3-semihyperbolic-hemicycle.full]].

## What the source establishes

**Theorem 1 (Local uniform finite cyclicity).** For the five-parameter
source-normalized quotient unfolding (1.3) of the quadratic field with
ẋ=−y+Bx²+μ₂y²+(μ₄+Bμ₅)x, ẏ=x+xy+μ₃y²+(1−2B)μ₅y, λ=(B,μ₂,μ₃,μ₄,μ₅):
there exist a fixed two-sided annular neighborhood U of the labelled graphic
Γ_{H¹⁴₃} on the Poincaré sphere, a neighborhood Λ ⊂ ℝ⁵ of 0, and a finite
constant B_{H¹⁴₃} such that N(λ;U) ≤ B_{H¹⁴₃} for every λ ∈ Λ — uniformly in all
five parameters, counting isolated limit cycles in the fixed collar.

**Status.** This is the case Roussarie–Rousseau 2015 explicitly left open ("the
one graphic through a triple point at infinity with no partial result", H³₁₄).
The graphic has: a noncompact source, two semihyperbolic horizontal endpoints,
and an upper-equatorial degeneration, all simultaneously.

**Method.** Finite atlas of stopped first hits before forming a full-lap return;
intersection argument representing each counted cycle by exactly one retained
itinerary; matched source estimate; direct Liénard–Dulac argument on the exact
mixed face; hyperbolic/central/strict-lips/middle/root-scale zero theorems;
finite specialization induction for coefficient/boundary/collapse/identity values.
**Computer-assisted** finite derivative and case enumerations (Parts II, III); the
physical exhaustiveness and theorem-applicability arguments are claimed as part of
the mathematical proof. Ancillary reproducibility certificates included
(verify_bautin_recurrence.py, verify_h14_center_bautin.py, etc.).

**Bound is existential** — no explicit or optimal cyclicity number.

## What it lets this run conclude

- The previously-open H³₁₄ row of the DRR inventory has a **claimed** closure:
  arXiv:2607.13785 (2026), preprint, unrefereed, computer-assisted in parts.
  This is a *claim* (status: asserted-by-source), NOT a verified closure. **The
  run's target should NOT be H³₁₄** unless the preprint survives scrutiny (it is
  80 pages, recent, 0 citations, with a reproducibility bundle — stress-testing
  its main theorem would itself be a real contribution, per GOAL.md: "stress-test
  the key step").
- **Finite algebraic core partially verified by this run** (hand re-derivation,
  exact arithmetic, in `research/notes/lu-finite-core-verified.md`): the four
  bridge identities, Darboux cofactors X(L)=(x+dy)L and X(F)=(2Bx+dy)F, the
  inverse-integrating-factor cofactor, and the degree-4 Bautin obstruction
  8L₄ = AC+CD+2DF−EF all hold. This certifies the *algebraic identities* the
  proof depends on, NOT the theorem (the human-proof remainder — analytic root
  uniqueness, Hadamard divisibility, domain completeness, zero theorems — is
  unverified and is exactly where a gap would live).
- The remaining solidly-open DRR rows per the strongest held sources: (I¹₆b),
  (H³₁₃), (DI₂b) — full finite cyclicity open (RR 2015 only closed their boundary
  sets) — plus whatever non-center triangles/other rows were never touched. The
  Lu preprint does not cover those.

```claim
id: drr-lu-claims-h14-3
statement: Lu (arXiv:2607.13785, 2026, preprint) claims local uniform finite
  cyclicity of the H^3_14 semihyperbolic hemicycle of quadratic fields: a fixed
  annular neighborhood and a finite uniform bound B over the full five-parameter
  unfolding. This is the graphic Roussarie-Rousseau 2015 left with no partial
  result. Bound existential; proof partly computer-assisted; not yet refereed.
  Its finite algebraic core (bridge identities, Darboux cofactors,
  degree-4 Bautin obstruction 8L4=AC+CD+2DF-EF) was re-derived by hand with
  exact arithmetic and verified by this run; the human-proof remainder and the
  degree-6 30-monomial equality are not yet independently checked.
hypotheses: n=2; five-parameter source-normalized unfolding; fixed collar U.
holds-here: claimed (preprint, 2026, 0 citations; finite core verified, theorem
  not).
status: asserted
bearing: H^3_14 is claimed closed as of 2026; the run's open-graphic attack
  should target (I^1_6b), (H^3_13), (DI_2b) instead, or stress-test Lu's proof.
anchor: research/sources/lu-h14-3-hemicycle-html.full.md
follows-from: drr-rr-boundary-only-for-3-graphics
```