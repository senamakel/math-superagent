# Fishkin 2010 — OpenAlex record (abstract via inverted index)

**Source URL:** https://api.openalex.org/works/doi:10.1090/S0077-1554-2010-00181-1
**Held at:** `research/sources/fishkin-openalex.full.md`
**Claim:** `research/claims/fishkin-perturbed-center-quadratic-bound.md`

## What this record establishes

The OpenAlex bibliographic record for Fishkin 2010 (Trans. Moscow Math. Soc.
71, DOI 10.1090/s0077-1554-2010-00181-1) — the only obtainable source of the
paper's abstract (AMS, MathSciNet, Semantic Scholar, and zbMATH all lack one
for this paper; the AMS "full text" captures are generic landing pages).

The abstract, reconstructed from the `abstract_inverted_index` (see
`research/findings/fishkin-abstract-reconstruction-2026-08-18.md` for the
full word-position reconstruction):

> "We investigate the number of limit cycles of a planar quadratic vector field
> with perturbed center-like singular point. An upper bound is obtained on the
> number of δ-good such cycles (Theorem 1). Here δ is a parameter characterizing
> cycles: it shows how far those are from points and infinite points. The bound
> also includes another parameter, κ, giving an estimate of distance to the set
> consisting of fields with a line [of singular points]. Earlier, Ilyashenko
> [and] Llibre found ... which ... sufficiently far ... Theorem 1 ... that
> complement each other and yield new ... field, regardless of its distance to
> [a center-like] point (Theorem 2)."

So the record confirms: the theorem structure (Theorem 1 = δ-good cycles of a
quadratic field with a perturbed center-like singular point, with κ measuring
distance to fields with a line of singular points; Theorem 2 = uniform bound
dropping the center-distance assumption) and the complementarity with
Ilyashenko–Llibre 2010.

## What it does NOT establish

- The specific numerical constants (10⁷² / 10⁷⁷ / δ^{−33}) quoted in earlier
  run reports. The abstract contains no exponents. Those figures are UNVERIFIED.
- The full proof structure, the δ-tameness/σ-perturbed-center analysis, or the
  exact theorem statements with constants — all require the primary text.

## Record metadata

- OpenAlex W2147420023; also indexed in MAG (2147420023), Crossref.
- Author: A. Yu. Fishkin (Lomonosov Moscow State University).
- OpenAlex marks the AMS PDF as open-access bronze:
  https://www.ams.org/mosc/2010-71-00/S0077-1554-2010-00181-1/S0077-1554-2010-00181-1.pdf
- CiteSeerX copy exists (doi 10.1.1.309.2425) but was unreachable this cycle.

[[fishkin-openalex.full]]
