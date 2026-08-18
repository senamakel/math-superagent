# Rousseau–Shan–Zhu 2015 — finite cyclicity of (I¹₁₂), (I¹₁₃) through a nilpotent saddle

Full text: [[drr-nilpotent-saddle-graphics-2015-arxiv.full]] (arXiv:1502.00689;
published as R. Rousseau, C. Shan, H. Zhu, "Finite cyclicity of some graphics through
a nilpotent point of saddle type inside quadratic vector fields", J. Differential
Equations 259 (2015) 7206–7228).

## What the source establishes (held full text, verbatim)

**Main result:** finite cyclicity of the two graphics **(I¹₁₂)** and **(I¹₁₃)** through
a triple nilpotent point of saddle type inside quadratic vector fields. These are DRR
program rows (program launched 1994 by Dumortier–Roussarie–Rousseau to show a uniform
upper bound for the number of limit cycles of planar quadratic fields).

**The 88 count (line 73–74, verbatim):** proving (I¹₁₂) and (I¹₁₃) "will bring the
number of graphics of the program for which finite cyclicity is proved **to 88**."
This is the authors' own running total — the anchor of the run's
`h16-drr-closed-rows-2015` claim.

**Machinery (the parts the run reuses):** normal form for the unfolding of a nilpotent
triple point of saddle type (§2.1); the blow-up of the family and limit periodic sets
in the blown-up family (§2.3–2.4); **Dulac maps of first type (Theorem 2.3) and near
hyperbolic/semi-hyperbolic points (Theorem 2.5, 2.7)** — the first/second-type Dulac
map definitions this run's I¹₆b four-second-type analysis uses; the generalized
derivation–division zero theorem; convex graphics through a nilpotent saddle of
multiplicity 3 (§3), with cyclicity bounds per limit periodic set.

## What it lets this run conclude

- The RSZ 2015 source confirms: (a) the 88 count is the authors' running total as of
  2015 (before Roussarie–Rousseau 2015 closed (I¹₁₄), making 89 by this run's
  arithmetic); (b) the Dulac-map framework (first/second type, semi-hyperbolic points)
  is the exact machinery the I¹₆b/H³₁₃/DI₂b boundary results and the I¹₆b
  four-second-type gap sit inside; (c) Theorem 2.5/2.7 (Dulac maps near hyperbolic and
  semi-hyperbolic points) is the expansion source the run's `g-transition` goal needs
  for the elementary/semi-hyperbolic vertices.
- It does NOT close (I¹₆b), (H³₁₃), (DI₂b) full graphics (RR 2015 boundary-only), nor
  any degenerate graphics.

```claim
id: h16-rsz2015-nilpotent-saddle-i12-i13-closed
statement: Rousseau–Shan–Zhu 2015 (arXiv:1502.00689, JDE 259:7206–7228) prove finite cyclicity of the two DRR graphics (I^1_12) and (I^1_13) through a triple nilpotent point of saddle type inside quadratic vector fields; their text states this "will bring the number of graphics of the program for which finite cyclicity is proved to 88". They develop the normal form of the nilpotent triple saddle unfolding, the family blow-up, first-type Dulac maps (Thm 2.3) and Dulac maps near hyperbolic/semi-hyperbolic points (Thm 2.5, 2.7), and the generalized derivation–division method.
hypotheses: quadratic vector fields; DRR 1994 program inventory; nilpotent triple point of saddle type at infinity.
holds-here: yes — closes rows (I^1_12),(I^1_13); the 88 count is the authors' own.
status: asserted
evidence: full text held at research/sources/drr-nilpotent-saddle-graphics-2015-arxiv.full.md; 88-count verbatim at lines 73-74; abstract states the two graphics.
falsifier: a primary source showing one of (I^1_12),(I^1_13) is not closed by this paper, or giving a different 2015 closed count.
sources: https://arxiv.org/abs/1502.00689
anchor: research/sources/drr-nilpotent-saddle-graphics-2015-arxiv.full.md
follows-from: h16-drr-closed-rows-2015
answers:
```
