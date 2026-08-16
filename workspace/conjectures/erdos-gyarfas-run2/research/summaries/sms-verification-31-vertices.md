# Balaji SMS 2026 — SAT verification to 32 vertices

Sources: Zenodo 20782738 (v2, "…up to 31 Vertices with SAT Modulo
Symmetries") and 20782739 (v1, "…up to 30 Vertices"). Both preprints, under
review. Landing-page/SMS description held; the PDF certificate is not in the
library.

## What it establishes (asserted by the preprint, not independently re-run here)

- **Method:** SAT Modulo Symmetries (SMS) — complete isomorph-free graph
  generation inside a CDCL solver — with the Glasgow subgraph solver as a
  complete forbidden-subgraph propagator on the classes {C4, C8, C16}.
- **v2 result:** every δ ≥ 3 graph on **≤ 31 vertices** contains a C4, C8, or
  C16. Hence any general counterexample has **≥ 32 vertices**.
- Each order ≤ 31 decided in ≤ ~2 hours on one CPU core; a conventional
  CEGAR baseline stalls near order 20.
- Corroboration claimed: exact ground-truth check vs nauty at n=10;
  reproduction of the n ≤ 16 baseline; agreement with an independent CEGAR
  solver for n ≤ 19; robustness across cardinality encodings and
  symmetry-breaking; reproducible pipeline; positive controls.
- The ≤ 31 range is precisely where 4, 8, 16 are the *only* admissible
  power-of-two cycle lengths (32 is the next power), so checking {4,8,16}
  settles the whole range.

## What it implies here

This is the run's verification bound: **any counterexample has ≥ 32
vertices**. This is a 2026 preprint under review, not journal-certified; the
run's oracle should reproduce a subset of it (e.g. n ≤ 19 via the CEGAR
agreement, or re-derive the n ≤ 16 baseline) before relying on the 32 bound as
an anchor. The bound does not depend on the conjecture's structure; it is
exact (a complete isomorph-free search) — so a counterexample, if one exists,
lives at n ≥ 32.

```claim
id: ce-verification-32
statement: Every graph with minimum degree ≥ 3 on at most 31 vertices contains a cycle of length 4, 8, or 16; hence any counterexample has at least 32 vertices.
hypotheses: finite simple, δ ≥ 3, n ≤ 31
holds-here: yes
status: asserted (preprint, not yet journal-certified; independently re-verified only up to ~19 here)
bearing: current verification bound; the oracle must reproduce a subset before trusting numbers past it
anchor: research/summaries/sms-verification-31-vertices.md
contradicts: none (strictly strengthens Royle/Markström 17 and 30)
```

```claim
id: ce-3232-only-lengths
statement: In the range n ≤ 31, the only admissible power-of-two cycle lengths are 4, 8, and 16 (the next power, 32, exceeds the vertex bound).
hypotheses: n ≤ 31
holds-here: yes
status: proved (trivial; a cycle of length 2^k needs 2^k vertices)
bearing: justifies checking only {4,8,16} in the verified range
anchor: research/summaries/sms-verification-31-vertices.md
```
