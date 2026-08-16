# Binary Steinhaus triangles — explicit bases for symmetry subspaces of Rule-90 Pascal-mod-2 objects

<!-- source: https://hal.science/hal-02313960v1/file/articleV1.pdf | converted from PDF -->
Full text at `research/sources/binary_steinhaus_triangles_rule90.full.md`.

## What it establishes

A *binary Steinhaus triangle* is a triangle of 0s and 1s following the same local
rule as Pascal's triangle mod 2 (equivalently, the iterated Rule-90 / Sierpinski
gasket: `a_{i,j} ≡ a_{i−1,j−1} + a_{i−1,j} (mod 2)`). This paper gives explicit
bases and dimensions for the linear subspaces of such triangles invariant under
the rotational (120°) and horizontal symmetries:

- **`dim RST(n) = ⌊n/3⌋ + δ_{1,(n mod 3)}`** (rotationally symmetric binary
  Steinhaus triangles; Cor 3.5), with an explicit basis in Thm 3.9 / Cor 3.11.
- **`dim HST(n) = ⌈n/2⌉`** (horizontally symmetric; Cor 4.6), explicit basis
  Prop 4.7.
- **Proposition 2.2.** A set G of n cells is a generating index set for the full
  triangle space `ST(n)` iff the mod-2 determinant of the binomial index matrix
  `M_G = ( C(i_k−1, j_k − l) )` is 1. That is the linear-algebra of the
  Rule-90 fold: the generating set of the whole space is detected by a mod-2
  binomial (Pascal) determinant — the same object as the fold matrix `Φ`.

## Bearing on SUPPLY

- The Rule-90/Pascal-mod-2 linear map (the fold `Φ`) is here given complete
  linear-algebraic structure: which index sets generate the full space, and
  what dimension the symmetric subspaces have. The operative `Φ_n`
  rank n−2, nullity 2, ker = span(even-alt, odd-alt) (corrected —
  fold-rank-is-n-2-nullity-2-alternating) is the rank statement of the same map.
- Confirms that the map `Φ` is *far from injective in weight terms*: there are
  large symmetry subspaces (dimension ~ n/2, ~n/3) that force low-weight /
  highly-structured images — physically the same phenomenon as closed door 4
  (anti-dyadic bounded-weight images). A weight lower bound on `wt(Φ_n h)`
  therefore cannot come from `Φ`'s linear structure alone; it must use `h`'s
  arithmetic correlation, exactly as the Hofer / Thue–Morse caveat concluded.
- The paper studies *triangles* generated from an initial row; the fold `Φ`
  reads a *window* of h along submask-XOR coordinates. The transfer of the
  bases/dimensions to the rectangular offset `Φ_n` is not stated and is
  unchecked — same caveat as Bacher.

```claim
id: steinhaus-binary-dimensions
statement: For binary Steinhaus triangles (Rule-90 / Pascal-mod-2), the rotationally symmetric subspace has dim ⌊n/3⌋+δ_{1,n mod 3} and the horizontally symmetric subspace has dim ⌈n/2⌉, each with an explicit basis of binomial-index cells; and a set G of n cells generates the full triangle space iff det(C(i_k−1,j_k−l)) ≡ 1 mod 2.
hypotheses: binary Steinhaus triangle of size n (Rule-90 / Pascal-mod-2 local rule); symmetry as stated.
holds-here: The linear map is exactly the fold Φ (Pascal-mod-2 / Rule-90). The symmetry-subspace dimensions confirm Φ has large invariant/core subspaces — consistent with, but a sharper quantification of, the low-weight-image phenomenon of problem.md closed door 4. Transfer from Steinhaus-triangle indexing to the rectangular offset Φ_n is unchecked.
status: asserted-by-source (published HAL paper, proofs in full text; not independently recomputed for Φ_n here)
bearing: Quantifies that Φ's own linear structure already contains O(n)-dimensional subspaces collapsing to structured/low-weight images, reinforcing that wt(Φ_n h) ≥ c·n must come from h's arithmetic, not from Φ's linear algebra alone.
anchor: research/sources/binary_steinhaus_triangles_rule90.full.md
```
