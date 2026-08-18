# Prohens & Torregrosa, "New lower bounds for the Hilbert numbers using reversible centers", Nonlinearity 32(1):331–355 (2019)

<!-- source: https://ddd.uab.cat/pub/artpub/2019/204392/newlowbou_a2019v32n1p331.pdf | converted from PDF; peer-reviewed postprint, UAB open repository. Full text at research/sources/prohens-torregrosa-lower-bounds-reversible-centers-2019.full.md -->

## What it establishes

Current best explicit lower bounds for the Hilbert number H(N), small degree N,
by simultaneous degenerate Hopf bifurcations from symmetric **Darboux
reversible centers** of very high simultaneous cyclicity. Systems have ≥3
centers (one on the reversibility line, two symmetric about it); limit cycles
in a **three-nest** configuration, total ≥ 2n+m.

**Theorem 1.** H(4) ≥ 28, H(5) ≥ 37, H(6) ≥ 53, H(7) ≥ 74, H(8) ≥ 96, H(9) ≥
120, H(10) ≥ 142, configurations ⟨8,12,8⟩, ⟨11,15,11⟩, ⟨16,21,16⟩, ⟨23,28,23⟩,
⟨30,36,30⟩, ⟨38,44,38⟩, ⟨45,52,45⟩ respectively.

**Corollary 2.** (a) H(13) ≥ 212, H(17) ≥ 384, H(21) ≥ 568, H(31) ≥ 1184,
H(35) ≥ 1536, H(39) ≥ 1920, H(43) ≥ 2272. (b) For each (N₀,K₀) ∈
{(4,28),(5,37),(6,53),(7,74),(8,96),(9,120),(10,142)}: H(N) ≥ K₀·N²/(N₀+1)²
(quadratic scaling).

Method: parallelised Lyapunov-quantity computation. The reversible cubic centre
is reduced to a rational first integral; Prop. 6 exhibits the quartic
Hamiltonian H(x,y) = (2x⁴−x²+y²−2x−2)⁵ used for the degree-4 construction.
Prop. 3 characterises the three-centre condition (α = det Jac at (xc,yc) > 0,
a₀₃ = 1, xc²+yc² ≠ 0).

## Hypotheses / holds here

Polynomial planar systems of degree N; reversible-center + simultaneous
degenerate Hopf bifurcation. Holds here: yes — these are global lower bounds in
degree N against which any claimed upper bound must be tested (problem.md test 2).

**Evidence class: sourced** (peer-reviewed Nonlinearity, full postprint held
from UAB DDD; the values are recorded here as the paper's, not re-derived by
this run).

## Bearing on the problem

- **H(4) ≥ 28 now rests on a held primary source** (previously only "reported"
  via surveys). Same for H(5)≥37, H(6)≥53, H(7)≥74, H(8)≥96, H(9)≥120,
  H(10)≥142 and the corollary values.
- The reversible-center + simultaneous-degenerate-Hopf machinery is exactly the
  Bautin-ideal / Lyapunov-quantity instrument route of GOAL step 4; Prop. 6's
  explicit object is a RATIONAL FIRST INTEGRAL
  H(x,y) = (2x⁴−x²+y²−2x−2)⁵ / (8x⁵−5x³+5xy²−10x²−5x−4)⁴ whose associated
  reversible differential system is quartic with centers at (0,0),(1,±2) — NOT a
  quartic polynomial Hamiltonian. Perturbing to fifth order yields 28 cycles in
  ⟨8,12,8⟩. This matters for Lean: it is a rational (quotient) first integral,
  so a "quartic Hamiltonian" polynomial statement would be mis-typed; the
  three-centre condition (α>0, a₀₃=1, xc²+yc²≠0) is the Lean-statable part.
- The quadratic-scaling Corollary 2(b) is a concrete, checkable statement about
  H(N) growth for N in 4..10, distinct from the asymptotic n²log n lower bound.