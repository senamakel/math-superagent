# Abel, Akitaya, Demaine, Demaine, Hesterberg, Ku, Lynch — "Escaping a Polygon"

Source: arXiv:2007.08965, https://arxiv.org/html/2007.08965 . Full text:
`research/sources/escaping-a-polygon-ab el-et-al.full.md` → [[escaping-a-polygon-ab el-et-al.full]]
(Front-page/abstract copy at `research/sources/escaping-a-polygon.full.md` → [[escaping-a-polygon.full]].)

## What the source establishes (rigorous, peer-venue-adjacent arXiv v3, 65pp)

This is the formal game-theoretic model of the exact pursuit–*escape* game PE
761 instantiates. Escaper ("human") at max speed 1 in the interior; pursuer
("zombie") at max speed r on the *complementary* domain (exterior — the paper's
**moat model**; the PE runner-on-boundary is the same constraint to a boundary
line). Escape = reach a boundary point a positive distance from the pursuer.

- **Well-posedness (unique winner).** In any locally rectifiable region the
  game has a unique critical speed ratio r\*: above which the pursuer wins,
  below which the escaper wins, and AT which the pursuer wins (Theorem 5.15).
  This matches the PE statement's dichotomy (escape iff v < V).
- **Exact r\* for three shapes:** disk, equilateral triangle, and square. The
  square value is the same 5.7886… (matches PE oracle; corroborates the
  Math.SE/square value) and the disk value matches Ponder-This ~4.6033.
  Uses the "APLO" (axially-progressing laterally-opposing) escaper strategy =
  the staged "keep-opposite then dash" strategy, rigorously justified.
- **General simple polygons:** a formula r\* ≈ max over boundary pairs of
  d_z/d_h (zombie-geodesic distance over human-geodesic distance) giving a
  polynomial-time **10.89898-approximation**, and a pseudopolynomial PTAS.
- **Negative results:** NP-hard in 3D; PSPACE/NP-hardness to approximate for
  multiple players.

## Why it matters for this run

This is the rigorous confirmation that the mechanism is *sound*, not just a
puzzle heuristic: the boundary-time/geodesic comparison is provably the right
basis for the critical ratio, and the staged "opposite-then-dash" (APLO)
strategy is provably optimal for the symmetric shapes. It independently
corroborates the disk 4.6033 and square 5.7886 values.

**Caveat (the run's own note flags this):** the paper gives *exact* r\* only
for disk (circle), triangle and square — the regular **hexagon is not in the
paper's exact-shape list**, and the ~10.9-approximation is far too coarse to
give PE 761's 8-decimal answer. So this source supports the *model and the
mechanism* and the square/circle values, but provides **no hexagon value**;
the hexagon comes from the stewbasic/Math.SE formula (n=6), which this paper
does not independently cover.

```claim
id: escaping-polygon-wellposed-exact-square-disk
statement: The pursuit-escape game (escaper speed 1 inside, pursuer speed r constrained to the exterior/boundary) has a unique critical speed ratio r* in any locally rectifiable region; exact values are known for the disk (~4.6033), equilateral triangle and square (5.7886); general simple polygons admit a 10.89898-approximation and a pseudopolynomial PTAS.
hypotheses: escaper restricted to interior, pursuer to exterior (moat model = PE's runner-on-boundary); both play optimally, instant reaction; escape = reach boundary point a positive distance from pursuer.
holds-here: yes for the model and the disk/square values; the paper's exact list does NOT include the regular hexagon, so the PE 761 answer must come from elsewhere (stewbasic formula).
status: proved (arXiv paper, Theorem 5.15 well-posedness; exact square/disk derived).
bearing: confirms the boundary-time/geodesic mechanism and independently corroborates V_circle=4.6033 and V_square=5.7886; does NOT give V_hexagon.
anchor: research/sources/escaping-a-polygon-ab el-et-al.full.md
```

## What it does not settle
- No hexagon exact value (the target of PE 761).
- The ≈10.9-approximation is not usable for an 8-decimal answer.
