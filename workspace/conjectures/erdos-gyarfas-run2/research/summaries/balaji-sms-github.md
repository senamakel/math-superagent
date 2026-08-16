# Balaji 2026 — SAT-Modulo-Symmetries verification (GitHub)

Source: GitHub repository `ArjunBalaji79/erdos-gyarfas-min-degree-3` (and the
Zenodo preprints 20782739 / 20782738 by A. Balaji, "…minimum-degree-3 graphs up
to 30 / 31 vertices"). Landing/source-code page held at
`research/sources/balaji-sms-github.full.md`; the preprints are also summarised
in `sms-verification-30-vertices.md` and `sms-verification-31-vertices.md`.

## What it establishes (asserted by the repo/preprints, not re-run here)

- First SAT-based verification of the Erdős–Gyárfás conjecture.
- Method: **SAT Modulo Symmetries (SMS)** — complete isomorph-free graph
  generation inside a CDCL solver — with the **Glasgow subgraph solver** as a
  complete forbidden-subgraph propagator on the classes {C4, C8, C16}.
- Result: every δ ≥ 3 graph on **≤ 31 vertices** contains a C4, C8, or C16.
  Hence any general minimum-degree-3 counterexample has **≥ 32 vertices**
  (frontier 17→32, and the cubic frontier 30→32 since cubic ⊂ δ≥3).
- Cross-checks: exact nauty ground-truth at n=10; reproduction of the n≤16
  baseline; agreement with an independent **CEGAR-SAT** solver (PySAT/CaDiCaL +
  power-of-two cycle detector) for n≤19; robustness across two cardinality
  encodings and a second symmetry-breaking method; positive controls; ~2
  CPU-hours per order.

## Caveats

- 2026 preprint, under review at *Experimental Mathematics*, not
  journal-certified.
- The general 32-vertex bound rests on the SMS search and has **no formal proof
  certificate**. By contrast, the separate cubic-bipartite result
  (arXiv:2608.02675, held) is certified by two independent oracles + a static
  witness, so the bipartite class has the stronger guarantee.
- The run's oracle should reproduce a subset (n≤16 baseline or n≤19 CEGAR
  agreement) before relying on the 32-vertex bound.

```claim
id: balaji-sms-32
statement: Every minimum-degree-3 graph on at most 31 vertices contains a C4, C8, or C16; any general counterexample has at least 32 vertices.
hypotheses: finite simple, delta >= 3, n <= 31
holds-here: yes
status: asserted (preprint, SMS search, no formal certificate)
bearing: current general verification bound; oracle must reproduce a subset first
anchor: research/sources/balaji-sms-github.full.md
```
