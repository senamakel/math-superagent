# Ionascu — "Ehrhart polynomial for lattice squares, cubes and hypercubes" (Rev. Roumaine 64 (2019) 57–80)

Source: https://imar.ro/journals/Revue_Mathematique/pdfs/2019/1/6.pdf (full text in `research/ehrhart_cubes.md`).

**What it is.** Computes Ehrhart polynomials of lattice squares/cubes/hypercubes. The run
already uses its **Theorem 3.1** (cube polynomial); this source is the citation backing the
lattice-point-count formula and the 4D constructions (not directly used for S(5000)).

## The statement the run relies on — Theorem 3.1 (cubes in R^3)
For a lattice cube given by orthogonal matrix C_ℓ = (1/ℓ)·[rows a,b,c] with integer
a_i,b_i,c_i satisfying a·a=b·b=c·c=ℓ² and mutual orthogonality, and d_i = gcd(a_i,b_i,c_i)
(row i = edge vector), the **Ehrhart polynomial** (lattice points in the t-dilated closed
cube) is
  L(C_ℓ, t) = ℓ³ t³ + ℓ(d1+d2+d3) t² + (d1+d2+d3) t + 1,  t∈N,   (...= (ℓt+1)(ℓ²t²+(D−ℓ)t+1) with D=d1+d2+d3).
Interior count = (−1)³ L(C_ℓ, −t) = ℓ³t³ − ℓ(d1+d2+d3)t² + (d1+d2+d3)t − 1 (Ehrhart
reciprocity, stated in §1).

## Verification against the statement's cubes (hand-checked here; matches memory.md)
- Cube A (axis, side 3): u=(3,0,0),v=(0,3,0),w=(0,0,3), ℓ=3, d_i=3. L(1)=27+3·9+9+1=64 ✓
  (problem: 64 total); interior = 27−27+9−1=8 ✓; surface 56 ✓.
- Cube B: u=(1,2,2),v=(2,−2,1),w=(2,1,−2), ℓ=3, d_i=1. L(1)=27+3·3+3+1=40 ✓ (problem: 40);
  interior 27−9+3−1=20 ✓; surface 20 ✓.

## Supporting statements / context
- General Ehrhart: L(P,t) is a degree-d polynomial, leading coeff = volume, constant 1;
  reciprocity L(P°,t)=(−1)^d L(P,−t) (§1, citing Ehrhart/Beck–Robins).
- **Theorem 3.2** (4D cube): L(t)=ℓD4 t³ + (ζ12+ζ13+ζ23) t² + (D1+D2+D3) t + 1.
  Not needed for 3D S(5000).
- (3.1)/(2.2) analogue for lattice *squares*: E2(t)=D t² + (d+d′)t + 1, used only as
  cross-check of the coefficient logic.
- The cube formula matches the run's memory.md exactly: pts(t)=ℓ³t³+ℓ·D t²+D·t+1 with
  D=d1+d2+d3 = sum of the three edge-gcds of the primitive frame.

## Hypotheses & applicability
Requires integer edge vectors with common norm ℓ² (a lattice cube: always true). The formula
applies to the cube itself; for the frame→cube scaling, memory.md applies it to the
t-scaled cube with ℓ→t·ℓ and d_i→t·d_i, giving the pts(t) polynomial used in the Faulhaber
summation. **Checked** by the oracle cubes A and B here and in memory.md.

## What it does NOT settle
The Ehrhart polynomial gives the lattice-point count per cube; it does not count the cubes
(C(n)) or handle the translation/box-fit count (those come from the span formula in
memory.md/frame_method.py). So this source covers half the S(n) sum (points per cube); the
other half (how many translations fit) is the run's own span argument.

## Net value
Direct citation for the point-count formula already validated. No contradiction with
memory.md. Not the bottleneck.
