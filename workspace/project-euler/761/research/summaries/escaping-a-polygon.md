# Escaping a Polygon — arXiv abstract/front page

Source: https://arxiv.org/abs/2007.08965 (front page, v3).
Full text: `research/sources/escaping-a-polygon-ab el-et-al.full.md` → [[escaping-a-polygon-ab el-et-al.full]]

This file is the same paper's abstract/front page only; the working summary
with the claims lives at `research/summaries/escaping-a-polygon-ab el-et-al.md`.
Its content is contained in the full-text file; read that summary instead.

## What the abstract itself establishes (nothing beyond the abstract)
- Model: escaper (human) speed 1 inside a region, pursuer (zombie) speed r
  outside; escape = reach boundary a positive distance from pursuer.
- Unique winner (critical speed ratio) in any locally rectifiable region.
- Exact critical ratios for equilateral triangle and square (and the disk,
  per the paper text) — the square value corroborates PE 761's V_square.
- 10.89898-approximation and pseudopolynomial PTAS for simple polygons;
  NP-hard in 3D.

```claim
id: escaping-polygon-abstract-square-disk
statement: The paper proves a unique critical speed ratio in locally rectifiable regions and gives exact values for the disk, equilateral triangle and square; the square value matches PE 761's V_square=5.78859314 and the disk matches V_circle=4.6033.
hypotheses: escaper in interior, pursuer in complementary exterior (moat = PE boundary runner); optimal play.
holds-here: yes for disk/square values and the model; no hexagon value in the paper's exact list.
status: proved (per abstract/paper).
bearing: rigorous corroboration of the model and the two oracle values; does not give V_hexagon.
anchor: research/sources/escaping-a-polygon.full.md
```

## Does not settle
- The abstract itself omits the exact numeric values (they are in the full
  text, which the other summary covers); and no hexagon.
