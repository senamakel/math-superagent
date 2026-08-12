# Unified Assembly Condition of Evenly/Non-evenly Spaced Planet Gear — Xue 2020

[[research/sources/unified-assembly-condition-xue-2020.full.md]] · source:
https://qikan.cmes.org/jxcd/EN/10.16578/j.issn.1004.2539.2020.12.007

## Accessibility note (be honest about this)

The journal page is JavaScript-rendered: the download captured the page
structure but **no abstract or derivation text** (the content placeholders
`{{article.zhaiyao_en}}` etc. were not server-rendered into HTML). The DOAJ
mirror (https://doaj.org/article/0e0dcfac68cb471bb90e2cdf7561f8ef) returned
HTTP 403. So the **full derivation text is NOT in the library**; only the
bibliographic record and the abstract from the search result are.

## What the search result established (recorded with that provenance)

- Journal of Mechanical Transmission 2020, Vol. 44(12): 43-48, Xue Huanzhang,
  DOI 10.16578/j.issn.1004.2539.2020.12.007.
- Abstract (from exa search): derives a **unified assembly condition** for
  planetary gear trains with both evenly and non-evenly spaced planets.
  The minimum non-zero **misalignment angle** between teeth of the compound
  planetary gears is first determined; the rotation angles of the independent
  planet gears follow from the kinematics equations; their difference is the
  assembly misalignment; assembly is possible **iff the misalignment is an
  integer multiple of that minimum angle**. Yields a general formula for any
  planet distribution.

## Implication for PE620

This is the *primary-source confirmation* that the discrete assembly condition
is a misalignment-is-integer-multiple-of-minimum-angle statement — the exact
structure of the least-mesh-angle theorem (positions at multiples of
2π/(s+c)) that the run's discrete counting model relies on. The accounting is:
the derivation logic is corroborated but not yet on disk here; the operational
rule is on disk in three independent gear sources (Drivetrain Hub tick angle,
UTS least mesh angle, Gear Solutions handbook).

## Cross-references

- Drivetrain/UTS/Handbook summaries: the least-mesh-angle = 360°/(sun+ring)
  rule (three independent statements, status: sourced).
- code/out/oracle-model-broken.md: why the continuous-d model fails and why
  the discrete model is the intended route.