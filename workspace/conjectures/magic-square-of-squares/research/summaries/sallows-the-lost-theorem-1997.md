# Sallows, "The Lost Theorem", Math. Intelligencer 19(4) 1997, 51–54 — [[sallows-the-lost-theorem-1997.full]]

Presents the LS1 near-miss and a structural reinterpretation of 3×3 magic squares.

## The lost theorem
> **Theorem.** To every parallelogram on the plane there corresponds a unique equivalence class of 8 complex 3×3 magic squares, and to every equivalence class of 8 complex 3×3 magic squares there corresponds a unique parallelogram on the plane (rotations/reflections disregarded).

Mechanics: the corner points, edge midpoints and centre of a parallelogram centred at M=c with half-side vectors a,b are P=c+a−b, Q=c+a+b, R=c−a+b, S=c−a−b, U=c+b, V=c−a, W=c−b. Entering P,Q,R,S,U,V,W,c in the Lucas positions reproduces the standard magic-square formula. The eight 3-term arithmetic progressions found in every 3×3 magic square correspond to the eight collinear triples along the four edges and four bisectors of the parallelogram.

## Implication for this problem
Integer/real magic squares correspond to **degenerate (zero-area) parallelograms** on the real line — this is why the correspondence went unnoticed for centuries. The nine entries c±a, c±b, c±(a±b), lying along a collapsed parallelogram, are exactly the parametrised grid. The four "through-centre" progressions are the bisectors; the four outer ones are the edges — a reminder that the through-centre four are not the whole story (the outer rows/cols are also APs) and any argument must respect all eight APs.

This source is **mildly relevant**: it re-frames the structure without changing the number-theoretic obstruction. It establishes the near-miss LS1 (the run's Sallows witness), but the existence question is untouched.

```claim
id: sallows-parallelogram
statement: 3×3 magic squares (complex entries) biject with parallelograms: entries at corners,
  edge-midpoints and centre; integer squares are the degenerate (collinear) case; the 8 APs in
  any 3×3 magic square are the 4 edges and 4 bisectors of the parallelogram.
hypotheses: 3×3 magic squares, complex entries
holds-here: yes (classical geometry of the parametrisation)
status: proved (in-source)
bearing: structural view only; does not touch the squareness obstruction. The four outer
  rows/cols are also APs — a complete analysis must handle all eight, not just the four
  through-centre ones.
anchor: research/sources/sallows-the-lost-theorem-1997.full.md
```
