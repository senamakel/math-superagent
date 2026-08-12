# Stanley, "An Introduction to Hyperplane Arrangements" (IAS/PCMI 2004) — summary

<!-- source: https://static.ias.edu/pcmi/2004/program/Stanleynotes.pdf | Richard P. Stanley, lecture notes, Park City Mathematics Institute July 12–19 2004; published in Geometric Combinatorics, IAS/Park City Math. Series 13 (2007) 389–496 -->

Full text at `research/sources/hyperplane_arrangements_stanley_ias_pcmi.full.md` (155k chars).

## What the source establishes

The standard graduate introduction to hyperplane arrangements. For a finite
set A of affine hyperplanes in V ≅ K^n:

- **Intersection poset L(A):** nonempty intersections of hyperplanes, ordered
  by reverse inclusion, with rank(A) = codimension of the minimal intersection
  = dimension spanned by the normals; L(A) is graded of rank rank(A), a
  meet-semilattice, and a lattice iff A is central (Prop 2.3).
- **Characteristic polynomial** χ_A(t) = Σ_{x∈L(A)} μ(0̂,x) t^{dim x}, with μ
  the Möbius function of L(A) (Definition 1.2/1.3).
- **Whitney's theorem** (2.4): χ_A(t) = Σ_{B⊆A, B: linearly independent}
  (−1)^{|B|} t^{n−|B|}.
- **Zaslavsky's theorem** (Theorem 2.5, the fundamental region-count result):
  for a real arrangement A in R^n,
  r(A) = (−1)^n χ_A(−1),   b(A) = (−1)^{rank(A)} χ_A(1),
  where r(A) = number of regions (connected components of R^n \ ∪A) and b(A) =
  number of relatively bounded regions.
- Corollary 2.1: r(A) and b(A) depend only on the intersection poset L(A).
- Examples: braid arrangement B_n has χ = t(t−1)⋯(t−n+1), hence r = n! (Weyl
  chambers); graphical arrangements recover chromatic polynomials.

## Bearing on PE597

The run's parity-region argument says the race outcome is constant on the open
cells of an arrangement of O(n²) linear hyperplanes in the normalized-speed
simplex (v_a=v_b and cross-multiplied event-time equalities). Zaslavsky's
theorem is the canonical statement that the number of such cells is governed by
the characteristic polynomial of the arrangement's intersection poset — the
named result behind "the arrangement has polynomially many faces in principle."
The run's own counts (n=3: 32 cells; n=4: 1202; n=5: ~13,750) show the
practical cost of naive cell enumeration still explodes; the theorem bounds the
geometry, not the enumeration algorithm. It does not give a closed recursion
for p(n,L).

## Sources / history

- Zaslavsky, *Facing up to arrangements: face-count formulas for partitions of
  space by hyperplanes*, Mem. Amer. Math. Soc. 1(154):vii+102, 1975.
- Crapo–Rota, Orlik–Solomon (Orlik–Solomon algebra, 1980) as further reading.

## Consistency with the run's record

Consistent with `research/torpids_exact_combinatorics_report.md` §3: the
"polynomial in principle" ceiling on arrangement faces is exactly Zaslavsky's
r(A) = |χ_A(−1)|; the report's caveat that the enumeration constant explodes in
practice is the run's own verified computation, not contradicted by this
source.