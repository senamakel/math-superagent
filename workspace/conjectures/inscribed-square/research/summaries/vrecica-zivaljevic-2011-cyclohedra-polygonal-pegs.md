# Vrećica–Živaljević 2011 — Fulton–MacPherson compactification, cyclohedra, and polygonal pegs

**Source:** Siniša Vrećica, Rade T. Živaljević, "Fulton–MacPherson compactification, cyclohedra, and the polygonal pegs problem," Israel J. Math. 184(1) 2011, 221–249. arXiv:0810.1439. Full text at [[research/sources/vrecica-zivaljevic-2011-cyclohedra-polygonal-pegs.full.md]].

## What it establishes

A configuration-space compactification approach to polygonal-peg problems. The key object is the **cyclohedron** Wₙ (Bott–Taubes polytope), which arises both as the polyhedral realization of the poset of cyclic bracketings and as the boundary of the Fulton–MacPherson (Axelrod–Singer/Kontsevich) compactification of the configuration space of n distinct cyclically ordered points on S¹.

- **Section 5 — a complete solution of the Square Peg Problem for smooth curves** via the cyclohedron method: the FM compactification gives a canonical domain on which the "square map" extends to the boundary; the degeneration of point configurations (pseudo-solutions) is controlled by the cyclohedron combinatorics. This is a modern, complete re-proof of the smooth case (the authors call it "reasonably short and conceptually transparent").
- **Grünbaum's conjecture (proved, Section 6):** every smooth Jordan curve inscribes an affine-regular hexagon.
- **Hadwiger's conjecture (reproved, Section 7):** every smooth simple closed curve in R³ inscribes a parallelogram (originally Makeev).
- **Section 8** discusses extending the method to larger classes of curves — the boundary degenerations are the obstacle.

## Why it matters here

- The cyclohedron formalism is a **different compactification strategy** from the Mobius band used by Stromquist/Shnirelman. It shows the configuration-space compactification technique, in its most refined form (FM compactification), has been pushed to smooth curves only.
- **Why the square case is hard even here:** the FM compactification's boundary records all ways points can collide; the square map's behavior there is what the parity argument must control. The paper's Section 8 explicitly discusses the extension problem — this is the same obstruction problem.md names (failure point 1: no boundary winding number for rough curves).
- The Grünbaum and Hadwiger results are adjacent (hexagons, parallelograms), not square results — do not conflate.

## Claims

```claim
id: vrecica2011-cyclohedron-smooth-square
statement: The square peg problem holds for smooth Jordan curves, proved via the Fulton–MacPherson compactification/cyclohedron method (a complete modern re-proof of the smooth case).
status: asserted-by-source
evidence: Vrećica–Živaljević, Israel J. Math. 184 (2011), Section 5 (arXiv:0810.1439)
holds-here: yes — confirms the smooth case by a different method; does not extend to continuous curves
falsifies: a gap in the Section 5 proof; a smooth curve with no inscribed square
anchor: research/sources/vrecica-zivaljevic-2011-cyclohedra-polygonal-pegs.full.md
```

```claim
id: vrecica2011-grunbaum-hexagon
statement: Every smooth Jordan curve inscribes an affine-regular hexagon (Grünbaum's conjecture), proved by the cyclohedron method.
status: asserted-by-source
evidence: Vrećica–Živaljević, Israel J. Math. 184 (2011), Section 6
holds-here: related result (hexagons, not squares); confirms the configuration-space method's reach is smooth curves
falsifies: a smooth curve with no inscribed affine-regular hexagon
anchor: research/sources/vrecica-zivaljevic-2011-cyclohedra-polygonal-pegs.full.md
```
