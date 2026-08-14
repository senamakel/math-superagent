# Measurable chromatic number of geometric graphs — Székely 1984; boundary sources

**Source:** doi:10.1007/bf02579223 (Székely, COMBINATORICA 4 (1984) 213–218)
**Related:** Bachoc–Nebe–de Oliveira–Vallentin, "Lower Bounds for Measurable
Chromatic Numbers", Geom. Funct. Anal. (2009), doi:10.1007/s00039-009-0013-7;
Székely–Wormald, "Bounds on the measurable chromatic number of R^n" (1989);
Payne, "Unit Distance Graphs with Ambiguous Chromatic Number" (2009).
**Full text:** not on disk; read via read_sources/abstracts.

## What this establishes

- **The measurable variant is genuinely different.** Székely (1984) exhibited a
  graph on the unit circle (edges at one fixed irrational-multiple-of-π arc
  length) that is 2-colourable in general but needs 3 colours when colour
  classes must be Lebesgue measurable. Under AC, χ and χ_m are not in general
  the same.
- Shelah–Soifer made the set-theoretic dependence explicit: the same graphs can
  have finite χ = χ_m in ZFC but uncountably large colouring requirements under
  weaker choice axioms.
- **The measurable-chromatic-number of R^n has strictly larger lower bounds**
  than the plain problem: Frankl–Wilson give χ_m(R^n) growing exponentially with
  dimension; Bachoc–Nebe–de Oliveira–Vallentin (2009) give new lower bounds for
  χ_m(R^10..R^24) via a theta-function/SDP→LP technique with Jacobi polynomials.
- For the plane, χ_m(R²) ≥ 5 (Falconer; Larman–Rogers line) — a *strictly
  stronger* lower bound than the plain χ ≥ 4 — so the measurable problem is
  NOT the problem in problem.md.

## Why it matters here

problem.md explicitly warns: "the measurable and the 'colour classes are nice
regions' variants have their own, larger, known lower bounds and are **not**
what is asked here. A statement proved under a measurability hypothesis is a
result about that variant and must be recorded as such." This source gives the
boundary its primary references: any colouring the run produces that uses
non-measurable sets is fine for the plain problem; any claim relying on
measurability belongs to χ_m and must not be attributed to χ.

```claim
id: measurable-variant-separate
statement: The measurable chromatic number chi_m differs from the plain chi for geometric graphs (Székely 1984) and has strictly larger lower bounds for R^n (Frankl–Wilson exponential; plane: chi_m(R^2) >= 5). A result proved under measurability of colour classes is a result about chi_m, not chi.
hypotheses: Colour classes required Lebesgue measurable; AC / choice context.
holds-here: true — fixes the boundary the problem statement draws: the run attacks the plain chi; measurable-variant results must be flagged as such.
status: sourced (Székely 1984; Bocher-Nebe-deOliveira-Vallentin; Payne; survey restatements)
bearing: Keeps the run honest about which problem it is solving; a measurable-variant lower bound is NOT a chi(R^2,1) lower bound.
anchor: research/sources/szekely-measurable-chromatic.md
```

## Note on download

Full text blocked at network layer. Content from read_sources/abstracts and the
surrounding literature (Payne 2009 restates Székely's example precisely).
Status: **sourced via read_sources; full text not on disk.**