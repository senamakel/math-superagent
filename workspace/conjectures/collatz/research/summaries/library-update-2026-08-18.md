# Library update — 2026-08-18

This cycle searched widely before fetching. Existing canonical sources were checked rather than duplicated: Lagarias overview, Tao's published paper, Barina 2025, MathWorld, Encyclopedia of Mathematics, Hercher, Monks, and Ansari are already present. A fresh NSF-hosted copy of Tao's paper was added as `research/sources/tao-2022-almost-bounded-nsf.full.md` with digest `research/summaries/tao-2022-almost-bounded-nsf.md`.

## Verified source-backed claims

```claim
id: tao-theorem-1-3-library-update
statement: For every function f: positive integers -> reals with f(N)->+infinity, Col_min(N)<f(N) for logarithmic-density-one many positive integers N.
hypotheses: standard Collatz map; logarithmic density; f diverges to infinity.
holds-here: yes, exactly the classical map in this problem.
evidence: Tao, Forum of Mathematics Pi, published source; `research/sources/tao-2022-almost-bounded-nsf.full.md`, Theorem 1.3 and abstract.
status: asserted-by-source
falsifies: a primary published erratum changing Theorem 1.3 or a proof that the stated density conclusion is false.
```

```claim
id: barina-2p71-library-update
statement: Barina's 2025 project reports that all starting values below 2^71 reach the trivial cycle, using accelerated iteration, sieves, and distributed CPU/GPU computation.
hypotheses: finite bound n<2^71; computational implementation and completed run as reported by source.
holds-here: yes as a finite verified-by-source result, not as a universal theorem.
evidence: DOI 10.1007/s11227-025-07337-0; existing full source `research/sources/barina-2025-improved-verification-2p71.full.md` and summary.
status: verified-numerically
falsifies: reproducible counterexample below 2^71, or a source correction withdrawing the computation.
```

```claim
id: lagarias-counterexample-dichotomy-library-update
statement: Any failure of the Collatz conjecture must manifest as an unbounded orbit or a nontrivial positive-integer cycle; the literature treats these as the two principal obstructions.
hypotheses: deterministic map on positive integers; standard conjecture.
holds-here: yes as the structural reduction used in the cited overview, with the caveat that proving the dichotomy-to-convergence implication requires the usual orbit analysis.
evidence: Lagarias, The 3x+1 Problem: An Overview, `research/sources/lagarias-3x1-overview.full.md`, sections 6–7.
status: asserted-by-source
falsifies: a third type of nonconvergent positive orbit not covered by unboundedness or eventual periodicity, or a source correction.
```

## Search and fetch record

Searches covered verification algorithms, Tao's theorem, surveys, canonical encyclopedias, recursive sufficiency, and similar-source neighborhoods. OpenAlex citation-graph requests were rate-limited (HTTP 429) and were not used as evidence. Existing files were not downloaded again. The new NSF copy is locally available and source-traceable.
