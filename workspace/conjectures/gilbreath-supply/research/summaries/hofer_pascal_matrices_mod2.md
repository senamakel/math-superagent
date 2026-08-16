# Hofer, "A note on matrices over ℤ with entries from binomial coefficients and Catalan numbers once pure and once modulo 2"

Source: https://arxiv.org/pdf/2502.01343 (2025). Full text at
[[research/sources/hofer_pascal_matrices_mod2.full.md]].

## What it establishes

The infinite Pascal matrix over ℤ and its mod-2 reduction carry a clean
structural algebra. Key items bearing on the fold Φ (Pascal-mod-2 / Rule 90):

- **Lemma 1 (Thue–Morse structure of the mod-2 relation).**
  `M1^T diag(((−1)^{t_i})·) M1 = M2`, where `t_i = s₂(i) mod 2` is the
  **Thue–Morse** sequence. This is a genuine structural link: the mod-2 Pascal
  matrix family is conjugate (through a Thue–Morse sign diagonal) to itself.
- **Corollary 1.** Every upper-left n×n submatrix of M2 has determinant
  `∏_{i<n} (−1)^{s₂(i)}` — the Thue–Morse signs are exactly the determinant
  sequence. Connects the fold's linear algebra to the closed door 4 (Thue–Morse
  gives sublinear ν₂).
- **Corollary 2.** The same signed-binomial-determinant pattern for shifted
  submatrices.
- **Theorem 2.** The Catalan/Hankel matrices H1, H2 (mod 2) have determinant ±1.

## Why it matters for SUPPLY

- Confirms from the linear-algebra side that the fold's mod-2 Pascal matrix is
  controlled by Thue–Morse sign structure — the very object that gives the
  sublinear counterexample in closed door 4. So any weight lower bound for
  `wt(Φ_n h)` must *rely on h's arithmetic correlation*, not on any generic
  property of Φ alone; Φ's own structure allows Thue–Morse-type degeneration.
- The `(0,2)`-sequence/Niederreiter-`(0,2)`-property language (Cor 3) is a
  possible quantitative handle: the mod-2 Pascal matrix qualifies as a low-
  discrepancy / (0,2)-sequence generator, which is the sort of equidistribution
  statement that historically underlies density-1 (GOAL priority 1) results.

**Caveat.** This note is structural (determinants, multiplications, discrepancy)
and does not state a weight lower bound for images of arbitrary input — the very
gap the run must fill. It sharpens the constraint that any such bound is input-
dependent (Thue–Morse degeneracy), consistent with the five closed doors.

```claim
id: hofer-mod2-pascal-thue-morse-structure
statement: The infinite Pascal matrix M1 over ℤ and its mod-2 reduction satisfy M1^T diag(((−1)^{s₂(i)})·) M1 = M2 (Lemma 1), and every upper-left n×n submatrix of M2 (= Pascal matrix mod 2) has determinant ∏_{i<n}(−1)^{s₂(i)} (Cor 1), where s₂(i) is the binary digit sum mod 2 (the Thue–Morse sequence).
hypotheses: M1 = Pascal matrix over ℤ; M2 its mod-2 reduction; s₂(i) = Thue–Morse signs.
holds-here: Yes — the mod-2 Pascal matrix M2 is exactly the linear-algebra of the fold Φ that SUPPLY is about.
status: sourced (Hofer 2025, Lemma 1, Cor 1)
bearing: Shows Φ's mod-2 structure is governed by Thue–Morse signs — the object whose images have sublinear ν₂ (closed door 4). Confirms any weight lower bound must be input-dependent (use h's arithmetic), not a property of Φ alone. Also opens the (0,2)-sequence / low-discrepancy quantitative angle for density-1 results.
anchor: research/sources/hofer_pascal_matrices_mod2.full.md; summary above
```
