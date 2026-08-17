# Rousseau–Zhu 2002 — pp-graphics through a nilpotent elliptic point

Full text: [[rousseau-zhu-pp-graphics-nilpotent-elliptic.full]] — preprint (Oct 2002,
York University), 2329 lines held.

## What the source establishes

**Theorem 1.1 (quoted, from DRR 1994):** There exists a uniform bound for the
number of limit cycles of a quadratic vector field **iff** all limit periodic sets
surrounding the origin inside the family (1.2)
{ẋ=λx−μy+a₁x²+a₂xy+a₃y², ẏ=μx+λy+b₁x²+b₂xy+b₃y²}
have finite cyclicity inside (1.2). The complete list of **121 graphics** was given
there — a primary-adjacent confirmation of the 121 count and the exact normal form
of the quadratic family the DRR program works in.

**Main result:** any **pp-graphic through a multiplicity-3 nilpotent singularity of
elliptic type not surrounding a center** has finite cyclicity. Such graphics may
have additional saddles and/or saddle-nodes. **Altogether 15 graphics of [4]
(DRR 1994) are shown finitely cyclic** in this paper — including a pp-graphic with
an elliptic nilpotent point plus a hyperbolic saddle with hyperbolicity ≠ 1
(appears in generic 3-parameter families; the "Kotova–Stanzo zoo").

**Context.** The paper applies Zhu–Rousseau [15] theorems/methods to all pp-graphics
through a nilpotent elliptic point in the DRR list, adapting to up to three
additional elementary singular points. Together with Roussarie–Rousseau 2008
(cyclicity 2 for nilpotent pp-type H¹₇, F¹₇ₐ, H³₁₁, I¹₆ₐ), this is part of the
~88-by-2015 count.

## What it lets this run conclude

- Primary confirmation of the DRR reduction statement and the 121 list count, in
  the exact family normal form (1.2) — stronger anchor for
  `drr-121-graphics-reduction` than the secondary surveys alone.
- 15 pp-graphics through nilpotent elliptic points are closed by Rousseau–Zhu
  2002; these are inside the 88-by-2015 tally.

```claim
id: drr-rousseau-zhu-15-pp-graphics
statement: Any pp-graphic through a multiplicity-3 nilpotent singularity of
  elliptic type not surrounding a center in the DRR 121 list has finite cyclicity
  inside quadratic systems; Rousseau-Zhu (2002) prove this for 15 graphics.
  The DRR reduction itself is stated as Theorem 1.1: H(2) finite iff all limit
  periodic sets surrounding the origin in family (1.2) are finitely cyclic.
hypotheses: n=2; pp-graphics through nilpotent elliptic point; not surrounding a
  center.
holds-here: yes
status: asserted
bearing: confirms 121 count and the reduction's normal form at primary-adjacent
  level; 15 named rows closed.
anchor: research/sources/rousseau-zhu-pp-graphics-nilpotent-elliptic.full.md
follows-from: drr-121-graphics-reduction
```