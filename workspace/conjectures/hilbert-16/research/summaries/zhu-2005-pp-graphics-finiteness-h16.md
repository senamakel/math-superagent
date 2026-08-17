# Zhu 2005, "From the pp-graphics to the finiteness part of Hilbert's 16th problem for quadratic systems"

Source: `research/sources/zhu-2005-pp-graphics-finiteness-h16.full.md` [[zhu-2005-pp-graphics-finiteness-h16.full]] — from YorkSpace bitstream 3526f30d.

## What the source establishes

The **primary survey of the pp-graphics route** (the frontier's top-cited row,
9 citations from this library's sources).

- **Theorem 1.1**: a pp-graphic with a triple nilpotent elliptic point (Epp),
  of any codimension, with 2 parabolic and 2 hyperbolic sectors has cyclicity
  **≤ n** whenever the regular transition map R (in normalizing coordinates)
  has non-vanishing nth derivative. This is the same order-bound principle as
  Roussarie–Rousseau 2008, stated here for general codimension.
- **Theorem 1.2**: **all 16 pp-graphics of quadratic systems have finite
  cyclicity** (including the hemicycle H¹₆ and related structures).
- Theorem 2.1: the normal form `ẋ = y + ax² + cxy − y²`, `ẏ = xy`-type for
  graphics (H1), (F1a), (H3), (I2a).
- Theorem 3.2 (analytic extension principle): brings a node to normal form
  analytically; the section is then analytic in the node plane. This analyticity
  is what makes transition maps non-flat — the step that would fail for C^∞.

## What it implies here

Primary source for the "**16 pp-graphics finite**" statement — claim
`drr-zhu-2005-pp-graphics-16`. The Theorem 1.1 hypothesis (non-vanishing nth
derivative of a regular transition map ⇒ cyclicity ≤ n) is a finite, Lean-carryable
claim: it reduces finite cyclicity of a nilpotent pp-graphic to an algebraically
checkable non-flatness condition.

Evidence class: sourced-held — read from the held full text. Hypotheses: n=2,
pp-graphics. Falsifier: a pp-graphic in the list of 16 with unbounded cyclicity.

Claim id `drr-zhu-2005-pp-graphics-16` (full statement in
`research/notes/claims.md`).
