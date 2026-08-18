# Korec 1994 — density estimate (DML-CZ record; full-text PDF unobtainable so far)

<!-- src: I. Korec, "A density estimate for the 3x+1 problem", Mathematica Slovaca 44(1) (1994) 85–89. DML-CZ record: http://hdl.handle.net/10338.dmlcz/133225 ; EuDML: eudml.org/doc/32414. -->

## Status of the full text

The DML-CZ landing page was retrieved (research/sources/korec-1994-density-estimate-3x1.full.md).
Its PDF (`https://dml.cz/bitstream/handle/10338.dmlcz/133225/MathSlov_44-1994-1_8.pdf`)
is malformed for the text extractor — both the live host and a Wayback copy
failed. EuDML's record is metadata-only with the same dml.cz PDF link. So the
**full text is not held**; the theorem statement below comes from the DML-CZ
abstract and the search excerpts, and is **asserted-by-source**, not read from
the primary.

## What the source establishes (asserted)

**Theorem 1 (Korec 1994).** For T the accelerated 3x+1 map, for every real
c > log_4(3) = 0.79248125…, the set
M_c = { y ∈ N : (∃n)(T^n(y) < y^c) } has asymptotic density 1.

That is: for any c > log 3 / log 4 ≈ 0.7925, almost all integers (natural
density) eventually reach a value below y^c. The paper cites Everett 1977 and
Terras 1976 as the baseline (density 1 for T^n(y) < y), and proves the
strengthened y^c version.

## Relation to this run's claims

This is the theorem behind claim `tao-korec-baseline` in
research/summaries/tao-almost-all-orbits.md (Korec: for any θ > log 3/log 4,
Col_min(N) ≤ N^θ for almost all N). Tao's theorem is the stronger logarithmic-
density result with Col_min(N) < f(N) for any f(N)→∞. Both are density
results — they do NOT touch the conjecture itself (see `tao-does-not-close`).

## Claim

```claim
id: korec-density-1
statement: For the accelerated 3x+1 map T and any real c > log_4(3) = 0.79248125..., the set M_c = { y ∈ N : (∃n)(T^n(y) < y^c) } has asymptotic density 1. (Korec, Math. Slovaca 44 (1994), Theorem 1.)
hypotheses: T the accelerated (Syracuse) map; c > log 3 / log 4
holds-here: yes — this is the Korec baseline behind tao-korec-baseline; a density result, not a conjecture proof
evidence: asserted-by-source (abstract + search excerpts; full-text PDF malformed/unobtainable, DML-CZ and EuDML both point to the same malformed scan)
status: asserted
falsifies: a counterexample showing the set M_c has density < 1 for some c > log_4(3)
```

## What would close the full-text gap

A working extraction of `MathSlov_44-1994-1_8.pdf` (OCR), or a rehosted text-
layer copy. Until then the claim is asserted, not read from the primary.
