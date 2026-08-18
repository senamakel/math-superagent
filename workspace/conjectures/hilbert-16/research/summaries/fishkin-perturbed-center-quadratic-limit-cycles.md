# Fishkin, "On the number of limit cycles of planar quadratic vector fields with a perturbed center"

**Source URL:** https://doi.org/10.1090/s0077-1554-2010-00181-1
**Held at:** `research/sources/fishkin-openalex.full.md` (OpenAlex record with abstract); the two AMS landing pages (`fishkin-perturbed-center-quadratic-limit-cycles.full.md`, `-ams.full.md`) contain NO mathematics.
**Published:** Trans. Moscow Math. Soc. 71 (2010)
**Claim:** `research/claims/fishkin-perturbed-center-quadratic-bound.md`
**Lean:** none — abstract-level only, no exact statement to formalize.

## What it establishes (abstract-level)

The OpenAlex abstract (the only abstract obtainable; AMS, MathSciNet, Semantic
Scholar all lack one for this paper) states verbatim in reconstructed order:

> "We investigate the number of limit cycles of a planar quadratic vector field
> with perturbed center-like singular point. An upper bound is obtained on the
> number of δ-good such cycles (Theorem 1). Here δ is a parameter characterizing
> cycles: it shows how far those are from points and infinite points. The bound
> also includes another parameter, κ, giving an estimate of distance to the set
> consisting of fields with a line [of singular points]. Earlier, Ilyashenko
> [and] Llibre found ... which ... sufficiently far ... Theorem 1 ... that
> complement each other and yield new ... field, regardless of its distance to
> [a center-like] point (Theorem 2)."

So the paper's theorem structure is confirmed:

- **Theorem 1**: an upper bound on the number of δ-good limit cycles of a
  quadratic field with a perturbed center-like singular point; the bound
  depends on δ and on κ (distance to fields with a line of singular points).
- **Theorem 2**: a bound that drops the center-distance assumption — a uniform
  bound on δ-good cycles of a quadratic field regardless of its distance to a
  center-like point, complementing Ilyashenko–Llibre 2010.

## What is NOT established

- The **specific numerical exponents** (10⁷², 10⁷⁷, δ^{−33}) quoted in earlier
  reports (research/REFERENCE-SET-REPORT-2026-08-18-restricted-h2.md,
  research/LIBRARY-STATUS-restricted-h2.md, and the previous form of the claim
  file) appear in **no held source**. They are UNVERIFIED until the primary
  text is obtained.
- The exact theorem statements, the proof structure, and the internal
  δ-tameness/σ-perturbed-center analysis are not verified from the primary
  text — the full text is not held (AMS PDF returned 429 rate-limit this cycle;
  vol 71 is in the free archive so a retry is legitimate).

## Why it matters to this run

- Complements the Ilyashenko–Llibre restricted bound by covering the
  **perturbed-center** case — the σ → 0 regime the latter excludes. Together
  they give the only known uniform bounds for δ-tame/δ-good cycles of
  quadratic fields.
- Same displacement-function / Poincaré-map / Growth-and-Zeros
  (Ilyashenko–Yakovenko counting) instrument family as the run's
  argument-principle approaches.
- The δ → 0 limit is where limit cycles accumulate on graphics — the divergence
  of these bounds is the quantitative shadow of the DRR-graphics obstruction.

## Caveats / data hygiene

- The earlier exponent figures (10⁷²/10⁷⁷/δ^{−33}) were quoted as
  "abstract-level" without any held source containing them. This summary
  corrects that: the structure is confirmed, the constants are not.
- Upgrade path: retry the AMS free-archive PDF (vol 71, >5 years old) when the
  server allows.

[[fishkin-openalex.full]]
