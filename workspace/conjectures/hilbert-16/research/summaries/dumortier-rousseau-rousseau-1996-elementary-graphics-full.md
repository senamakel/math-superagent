# Dumortier–El Morsalani–Rousseau 1996 — Hilbert's 16th problem for quadratic systems and cyclicity of elementary graphics (abstract-level)

Full text: [[dumortier-rousseau-rousseau-1996-elementary-graphics-full.full]]
(Nonlinearity 9(5), 1996, 1209, DOI 10.1088/0951-7715/9/5/008). **Body PDF is
paywalled at IOP; held is the publisher record with the full abstract.**

## What the source establishes (abstract level)

- **Several elementary graphics of quadratic systems have finite cyclicity** —
  those with non-identical return map listed in the preceding DRR 1994 paper
  (J. Diff. Eqns 110:86–133). This is the class-closure paper behind the
  elementary DRR rows.
- **Method = Khovanskii's method** (fewnomial / Bézout-for-Liouville zero
  bounds), plus normal forms for elementary singular points, plus unbroken
  connections.
- **Compensation principle**: two singular points "compensate" each other
  precisely when the graphic surrounds a center — the mechanism behind
  center-surrounding elementary graphics.
- **Originality point the abstract itself flags**: for certain graphics among
  quadratic systems some *regular* transition maps are not tangent to the
  identity — i.e. the "flat remainder" at a regular vertex can be non-trivial,
  which complicates the naive composition of Dulac maps. This is directly
  relevant to any displacement-function composition argument this run writes:
  the transition maps along the sides of a graphic are not always
  identity-to-first-order.

**Author-list correction (recorded)**: the fetched IOP record and OpenAlex list
the authors as **F. Dumortier, M. El Morsalani, C. Rousseau** (earlier library
reports attributed it to Dumortier–Roussarie–Rousseau). The library's claim
note records this correction.

## Explicitly NOT established

- The PDF is not held; the *closure rows* themselves are corroborated by the
  held DGR 2002 full text (`drr-dgr-2002-elementary-closures`, seven elementary
  rows with explicit cyclicity ≤ 2/3) and the DRR94 cyclicity-1/2 abstract
  (`drr-drr94-cyclicity-1-2-abstract`, 33 graphics ≤ 2).
- Fine content (which graphics, what bounds) is not readable from the abstract.

## Implication for this run

This is a background/method anchor for the elementary-graphics rows of the DRR
inventory; on its own it decides nothing new. The "regular transition maps not
tangent to identity" observation is worth carrying into the displacement
functions: a composition argument that assumes identity-to-first-order
regular transitions will be wrong for these graphics.

```claim
id: drr-demr-1996-elementary-graphics-abstract
status: asserted
statement: Dumortier, El Morsalani, Rousseau, "Hilbert's 16th problem for
  quadratic systems and cyclicity of elementary graphics", Nonlinearity 9(5)
  1996, DOI 10.1088/0951-7715/9/5/008 (abstract + record held; PDF paywalled):
  proves finite cyclicity of several elementary graphics of quadratic systems
  (non-identical return map) by the Khovanskii method, normal forms at
  elementary singular points, compensation between singular points when the
  graphic surrounds a center, and proves for certain graphics that some
  regular transition maps are NOT tangent to the identity. Author list
  correction recorded: Dumortier-El Morsalani-Rousseau (not
  Dumortier-Roussarie-Rousseau).
hypotheses: quadratic systems; elementary graphics; Khovanskii method.
evidence-class: sourced (abstract-level; publisher record; PDF not held). The
  closure rows themselves are corroborated by held DGR 2002 full text.
falsifier: any of the abstract's claims contradicted by a held primary text;
  or a finding that the authors differ from the record's listing; none known.
holds-here: yes -- background/method anchor for the elementary DRR rows and a
  warning that regular transition maps in these graphics can fail to be
  tangent to the identity (matters for displacement-function composition).
anchor: research/sources/dumortier-rousseau-rousseau-1996-elementary-graphics-full.full.md
follows-from: drr-1994-citation-anchor
```