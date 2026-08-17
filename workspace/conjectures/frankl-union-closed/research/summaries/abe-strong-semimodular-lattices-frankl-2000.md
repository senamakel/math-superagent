# Abe, "Strong semimodular lattices and Frankl's conjecture" (Algebra Universalis 44:379–382, 2000)

- Source: https://doi.org/10.1007/s000120050195
- Downloaded 2026 (librarian cycle) — full text in research/sources/abe-strong-semimodular-lattices-frankl-2000.full.md
- **Access limitation**: Springer is paywalled. The `.full.md` file contains only the article's metadata, abstract, and abstract-level content, NOT the proof text. The DOI record and abstract are confirmed; the proof argument itself could not be obtained from this route.
  - A second route worth trying if the proof text is needed: SpringerLink sharing/reveal, or the 4-page paper may be in an OA repository; not attempted this cycle.

## What it establishes (abstract, primary source)

> "In this paper, we show that Frankl's conjecture holds for strong semimodular lattices. The result is the first step to deal with the case of *upper* semimodular lattices."

This is the primary-source anchor for the ROOT.md lattice-class row "strong semimodular lattices satisfy UC". Previously that row (and citations of Abe 2000 in the Bruhn–Schaudt survey, Joshi–Waphare 2019) referenced *secondary* sources only. Now the DOI record and abstract are on disk as the primary citation.

Key facts pinned:
- Author: Tetsuya Abe (Tokyo Institute of Technology).
- Received 2000-05-30, accepted 2000-08-14, published December 2000.
- Class settled: **strong semimodular lattices** satisfy Frankl's conjecture (in the Poonen lattice form: some join-irreducible x has |{y : y ≥ x}| ≤ |L|/2).
- The abstract frames it as "the first step to deal with the case of upper semimodular lattices" — i.e. upper semimodular lattices in general remain OPEN (matches ROOT.md).

## Evidence class

- Claim "strong semimodular lattices satisfy UC": **asserted-by-source** (the abstract states it; the proof text is paywalled and not independently verified here). This matches the evidence class used for the sibling Abe–Nakano (modular) and Reinhold (lower semimodular) claims, both of which are also abstract-only in this library.
- This is a case of the broader lattice-formulation line (Poonen 1992; Abe–Nakano 1998 modular; Reinhold 2000 lower semimodular; Czédli–Schmidt planar semimodular).

<!-- source: https://doi.org/10.1007/s000120050195 -->

```claim
id: abe-strong-semimodular-lattices
answers: lattice-settled-classes
statement: Every finite strong semimodular lattice L with |L| >= 2 satisfies
  Frankl's (union-closed sets) conjecture: some join-irreducible x has
  |{y in L : y >= x}| <= |L|/2.
hypotheses: L finite strong semimodular lattice, |L| >= 2.
holds-here: true
status: asserted
bearing: primary-source anchor for the "strong semimodular" row of ROOT.md's
  settled classes; the paper names upper semimodular lattices as the next open
  case (which the library records as open, cf. upper-semimodular-open). Proof
  text paywalled; abstract obtained from the DOI record.
anchor: Abe, Algebra Universalis 44 (2000) 379–382, doi:10.1007/s000120050195,
  abstract.
```