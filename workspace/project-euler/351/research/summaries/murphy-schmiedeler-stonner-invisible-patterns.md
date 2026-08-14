# Murphy, Schmiedeler & Stonner, "First Occurrence and Frequency of Invisible Lattice Point Patterns" (SIAM Undergrad Research Online)

Source: https://www.siam.org/media/i1thfsyh/s136404pdf.pdf — full text at
`research/sources/murphy-schmiedeler-stonner-invisible-patterns.full.md`
[[murphy-schmiedeler-stonner-invisible-patterns.full]]

## What this source establishes

Computational classification (491 CPU-days, 112 cores, domain 24M×24M, C
program, Saint Louis University HPC) of invisible rectangular blocks in Z²,
with proof of the structural facts behind the data:

- **Theorem 2.1** (cites Goins–Harris–Kubik–Mbirika Prop. 3): a lattice point
  (x,y) is visible from the origin iff gcd(x,y) = 1. This is the exact
  criterion this run's H(n) derivation uses.
- **Closest invisible n×m rectangles, 1 ≤ n,m ≤ 4** (Table 2.1, radial
  order): 1×1 at (2,2), 2×2 at (14,20), 3×3 at (1274,1308), **4×4 at
  (7247643, 10199370)** — confirming the location Eric Weisstein had posited
  on MathWorld's Visible Point page. Lexicographic-first locations in
  Table 4.1 (4×4 lex-first at (8853, 5583967323)).
- **Corollary 3.2**: no pattern containing a visible point of every parity
  type A,B,C,D (coordinate parities) occurs — a special case of
  Herzog–Stewart (1971): the only non-occurring patterns are complete residue
  classes of pairs modulo some prime.
- **Corollary 3.3**: every occurring n×m invisible rectangle has at least
  ⌊n/2⌋·⌊m/2⌋ invisible points (pigeonhole over parity types).
- **Empirical density**: proportion of invisible points in the searched
  domain is 0.392073 ≈ 1 − 6/π², visible 0.607927 ≈ 6/π² — matching the
  classical constant this run uses as its magnitude anchor.
- Proposition 4.2: given an x-column satisfying the necessary prime-divisor
  conditions, infinitely many y place an invisible rectangle there (CRT).

## Why it is in this library

Independent, peer-reviewed-style computational corroboration of (a) the
gcd=1 visibility criterion and (b) the 6/π² density anchor. It is the
"hidden-forest location" literature this run's visibility sources cite, and
its Theorem 2.1 fixes the criterion from a fourth independent source.

## What it does not settle

No bounded-region counting formula (nothing like H(n) = 6(C(n+1,2) − Φ(n)));
no totient connection. The empirical frequency tables (Section 5) are
catalogue-style data, not needed here. Not load-bearing for the exact answer.

## Claims

```claim
id: invisible-rectangle-classification
statement: A lattice point (x,y) is visible iff gcd(x,y)=1 (Murphy–Schmiedeler–Stonner Thm 2.1, citing Goins et al. Prop 3); closest invisible n×m rectangles for 1≤n,m≤4 classified (4×4 first at (7247643,10199370)); every occurring n×m rectangle has ≥ floor(n/2)·floor(m/2) invisible points (Cor 3.3); measured invisible proportion 0.392073 ≈ 1 − 6/pi^2.
hypotheses: Z^2, straight-line visibility from origin, first quadrant.
holds-here: yes — corroborates the gcd criterion and the 6/pi^2 density anchor this run's derivation and magnitude check use; no bounded-hexagon formula.
status: sourced (computational classification, SIAM URO; 491 CPU-days over 24M×24M)
bearing: independent corroboration of the governing lemma; not load-bearing for H(10^8).
anchor: research/summaries/murphy-schmiedeler-stonner-invisible-patterns.md
```
