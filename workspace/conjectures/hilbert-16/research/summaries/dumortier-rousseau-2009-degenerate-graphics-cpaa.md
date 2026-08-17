# Dumortier–Rousseau 2009, degenerate graphics (CPA 8:1133–1157)

Source: `research/sources/dumortier-rousseau-2009-degenerate-graphics-cpaa.full.md` [[dumortier-rousseau-2009-degenerate-graphics-cpaa.full]] — from `http://www.dms.umontreal.ca/~rousseac/Dumortier_Rousseau.pdf`.

## What the source establishes

The paper attacks finite cyclicity of the **degenerate** DRR graphics — the ones
with a **line of singular points** in the finite plane — which lie outside the
elementary/nilpotent closures. It gives exact **5-parameter** normal forms for
the 13 degenerate graphics (3 normal forms suffice):

- **finite-plane line** (DF1a, DF1b, DF2a, DF2b, DH1, DH2):
  `ẋ = y + bxy − y² + µ1 + µ2x + µ3x²`, `ẏ = xy + µ4`, with a weak focus/centre.
- **infinity line** (DI1a, DI1b, DI2a, DI2b, DH3, DH4):
  `ẋ = cx − y + 1 + (1+µ2)x² + µ1xy + µ0y²`, `ẏ = xy − µ3x²`.
- **DH5**: no analytic 5-parameter normal form exists — needs a 7-parameter
  unfolding; slow motion is `ẋ = µ0+µ1x+µ2x²` on the line and
  `ẋ = µ3+µ4v+µ5v²+µ6v³` on the equator. This is the key obstacle for DH5.

**Theorem 3.1** (the core cyclicity statement): DF1a (b₀ ∈ (0,2)) has at most
**3** limit cycles near the graphic (≤1 if E1 ≥ 0); DF2a (b₀ = 0) at most **5**
(≤1 if bE1 ≥ 0, ≤1 on the circle {D = E1 = 0}).

**The single open point**: `P* = (D, E0, E1, E2) = (0,0,0,1)`. At P* the family
**cannot be desingularized** — E0 = D = 0, E1 = 0 leaves several expected limit
cycles and no blow-up exists. This is a genuine analytic-algebraic obstruction,
not a gap in technique. Completed later by Huzak 2018 (DF2a fully closed).

## What it implies here

- Primary source that upgrades the DF1a/DF2a rows from "reported" (Shan 2013
  thesis) to **sourced-held** — claim `drr-df1a-df2a-cyclicity-sourced`.
- The P* obstruction is the concrete shape of the `problem.md` **smooth test**:
  where a family resists desingularization, an asymptotic-only argument cannot
  decide cyclicity. Any later attempt on degenerate graphics must either
  desingularize P* or argue it away.

Evidence class: sourced-held — read from the held full text. Hypotheses: n=2,
degenerate graphics with a line of singular points, x₀ in a compact subset of
(0,∞).

Claim id `drr-df1a-df2a-cyclicity-sourced` (full statement in
`research/notes/claims.md`).
