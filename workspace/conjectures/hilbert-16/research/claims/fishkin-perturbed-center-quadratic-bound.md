# Fishkin: uniform bound on δ-good limit cycles of quadratic vector fields (abstract-level only)

```claim
id: fishkin-perturbed-center-quadratic-bound
statement: A. Yu. Fishkin, "On the number of limit cycles of planar quadratic vector fields with a perturbed center", Trans. Moscow Math. Soc. 71 (2010), DOI 10.1090/s0077-1554-2010-00181-1, investigates the number of limit cycles of a planar quadratic vector field with a perturbed center-like singular point. An upper bound is obtained on the number of δ-good such cycles (Theorem 1), where δ characterizes how far those cycles are from singular points and infinite points; the bound also involves a parameter κ estimating the distance of the field to the set of quadratic fields with a line of singular points. A further result (Theorem 2) drops the center-distance assumption, complementing Ilyashenko–Llibre 2010, and together they yield a bound on the number of δ-good limit cycles of a quadratic field regardless of its distance to a center-like singular point.
hypotheses: planar quadratic polynomial vector fields, normalized as in Ilyashenko–Llibre 2010; δ-good limit cycles (encircling the origin, δ-away from the other singular points and infinity); κ-distant from singular quadratic fields (line of singular points). The exact theorem statements, including the precise numerical constants, are NOT verified from the primary text — the full text is not held.
holds-here: partially — the abstract confirms the paper exists, its theorem structure (perturbed-center case Theorem 1; uniform case Theorem 2 without center-distance assumption, complementing Ilyashenko–Llibre), and that it is a genuine restricted bound on H(2), result-category 2 in problem.md. It does NOT prove H(2) < ∞: the bound diverges as κ, δ → 0, the singular/degenerate regime where the DRR graphics live.
status: asserted-by-source (abstract level only)
evidence: The AMS journal landing pages (research/sources/fishkin-perturbed-center-quadratic-limit-cycles.full.md and -ams.full.md) contain NO mathematics — they are generic journal pages. The OpenAlex record (research/sources/fishkin-openalex.full.md) carries the abstract as an inverted index: it confirms "We investigate the number of limit cycles of a planar quadratic vector field with perturbed center-like singular point. An upper bound is obtained on the number of δ-good such cycles (Theorem 1)... κ ... distance to the set consisting of fields with a line [of singular points]... Ilyashenko [and] Llibre found ... complement each other and yield new ... field, regardless of its distance to [a center-like] point (Theorem 2)." The specific numerical exponents quoted in earlier reports (10⁷², 10⁷⁷, δ^{−33}) appear in NO held source and are UNVERIFIED.
falsifier: Any discrepancy between the quoted exponents (10⁷² / 10⁷⁷ / δ^{−33}) and the paper itself; a quadratic field in the stated class with more δ-good limit cycles than the bound; or a source showing the κ/δ hypotheses admit the divergence regime. The primary-text PDF (AMS free archive) must be obtained to verify the theorem statements.
sources: https://doi.org/10.1090/s0077-1554-2010-00181-1 ; https://api.openalex.org/works/doi:10.1090/S0077-1554-2010-00181-1 ; http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.309.2425
anchors: research/sources/fishkin-openalex.full.md (abstract inverted index: "We investigate the number of limit cycles of a planar quadratic vector field with perturbed center-like singular point. An upper bound is obtained on the number of δ-good such cycles (Theorem 1)...")
note: The earlier report rows (research/REFERENCE-SET-REPORT-2026-08-18-restricted-h2.md, research/LIBRARY-STATUS-restricted-h2.md, research/claims/fishkin-perturbed-center-quadratic-bound.md in its previous form) quoted the specific exponents 10⁷² / 10⁷⁷ / δ^{−33} as "abstract-level" without any held source containing them. This is a data-hygiene correction: the exponents are UNVERIFIED until the primary text is obtained. The theorem STRUCTURE (perturbed-center Theorem 1; uniform Theorem 2; complements Ilyashenko–Llibre) IS confirmed by the abstract. Upgrade path: retry the AMS free-archive PDF (vol 71 is >5 years old) when the server allows.
follows-from:
answers:
```

## Why this claim block exists

The previous file at this path had a YAML-bullet header and quoted specific numerical
exponents (10⁷², 10⁷⁷, δ^{−33}) as if abstract-level. Neither the bullet format nor
the exponents are supported: the two AMS "full text" captures are generic landing
pages with no mathematics, and the only abstract obtainable (OpenAlex) confirms the
theorem structure but not the constants. This block states exactly what is
established — the structure — and flags the constants as unverified.
