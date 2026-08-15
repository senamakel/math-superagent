# Moser spindle — 7-vertex unit-distance graph, χ = 4

**Primary local source (verified, not quoted):** `code/brute.py` + `code/out/brute_calibration.txt`.
**Historical attribution:** the spindle graph is due to **L. Moser and
W. Moser** (1961), *Solution to Problem 10*, Canadian Mathematical Bulletin
**4** (1961), 187–189 — so named because it is the standard `7`-vertex
unit-distance graph used as the Hadwiger–Nelson lower-bound gadget `χ ≥ 4`.
(The exact 1961 citation could not be fetched this run; see attribution note.)

## The graph

Vertices (indices as in `code/brute.py`):

```
0 = O        = (0, 0)
1 = a1       = (1, 0)
2 = a2       = (1/2, sqrt3/2)
3 = a3       = (3/2, sqrt3/2)
4 = b1       = (5/6, sqrt11/6)
5 = b2       = (5/12 - sqrt33/12, 5/12 + sqrt11/12)
6 = b3       = b1 + b2      (5/4 - sqrt33/12, 5/12 + sqrt11/4)
```

All coordinates are exact in the field `Q(sqrt3, sqrt11)` (4-dim Q-basis
`{1, sqrt3, sqrt11, sqrt33}`). The graph is two unit rhombi (each a pair of
unit equilateral triangles) sharing the origin, with the second rhombus rotated
by `φ` where `cos φ = 5/6`, `sin φ = sqrt11/6`, so the two far tips are at
distance exactly `1`.

## Machine-verified facts (independent of any literature claim)

From `code/out/brute_calibration.txt` (exact-arithmetic oracle):

- **7 points**, distinct.
- **11 unit-distance edges**, every one certified `|x − y|² = 1` exactly; and
  **no** non-edge lands at distance 1 (no spurious, no missed edge).
- **Chromatic number 4**: 4-colourable (witness colouring `[0,1,2,0,1,2,3]`),
  **not** 3-colourable (complete backtracking test), 2-colourable false.
- `CALIBRATION PASSED: 11 edges, chi=4, not 3-colourable`.

## Why this is the calibration target for the whole run

Per `GOAL.md` / `problem.md`, this `7`-vertex graph is the pair on which the
edge-certifier and the complete colouring test must both be validated before any
construction is trusted. It reproduces the known lower bound `χ(G) ≥ 4` for the
plane in exact arithmetic. Any claimed `5`-chromatic graph must be reverified by
code independent of the construction code — the floating-point trap is that a
spurious edge can only increase apparent chromatic number, and the exact
certifier here is what defeats it.

## Attribution and status note

- The **geometry and the χ=4 verification are local and exact** — these are the
  run's own computed results and do not depend on literature.
- The **historical attribution** to Moser & Moser (1961, Canadian Math. Bull.)
  is standard and consistent with the problem.md description ("two rhombi of unit
  side sharing a vertex, rotated so their far vertices are at distance 1") and
  with the frontier's arXiv 1805.12181 lead (Exoo–Radziszowski, who develop the
  technique of spindling beyond `4` colours). The 1961 paper's text itself could
  not be fetched this run (network + evidence-policy screening); it is a named
  gap.
