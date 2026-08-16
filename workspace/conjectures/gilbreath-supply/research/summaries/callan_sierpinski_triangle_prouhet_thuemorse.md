# Callan, *Sierpinski's Triangle and the Prouhet-Thue-Morse Word*

arXiv:math/0610932v3 [math.CO], Nov 2006. David Callan, U. Wisconsin-Madison.
Full text: `research/sources/callan_sierpinski_triangle_prouhet_thuemorse.full.md`

<!-- source: https://arxiv.org/pdf/math/0610932 -->

## What it establishes

A short, exact structural note on Pascal's triangle mod 2 as the infinite
lower-triangular (0,1)-matrix `S` (S[i][j] = C(i,j) mod 2, i ≥ j; the "Sierpinski
triangle" / Lucas parity pattern). The fold Φ_n of this problem is the square
submask-XOR matrix of exactly this family (rows d, the operand `d`-fold
`(1+σ)^d`, degree `2^popcount(d)`), so `S` is the subject's own matrix.

**Theorem 1.** `S⁻¹` is a `(−1, 0, 1)`-matrix with **the same zero pattern as S**,
and the nonzero entry in position (i,j) is `(−1)^{b(i−j)}`, where `b` is the
binary digit sum. Writing `i free of j` for "the binary expansion of i has 0s in
every position where j has 1s" (addition of i and j in base 2 has **no carries**),
`C(i,j)` is odd ⟺ `i−j free of j` (Kummer; also Graham–Knuth–Patashnik Ex. 5.36).
So the zero/±1 pattern of both `S` and `S⁻¹` is governed exactly by the
no-carry / submask condition.

**Theorem 2 / Cor 3 / Thm 4 (the "free of" matrix family).** Define
`S(x)[i][j] = x^{b(i−j)}` if `i−j free of j`, else 0. Then `S(x)S(y) = S(x+y)`,
`S(x)^q = S(qx)`, `S(x)^r = S(r)` for rational r, and `S(1) = S`, `S(−1) = S⁻¹`.
This is a clean algebraic packaging of the submask auto-correlation structure.
(The sign pattern `(−1)^{b(i−j)}` is exactly the Prouhet–Thue–Morse word along
each column.)

## Bearing on SUPPLY

This is the **inverse** of the fold family, and both the fold Φ and its inverse
share the identical zero pattern — zero at position (i,j) iff `i−j` is **not**
free of j (iff `C(i,j)` even). Two consequences for the open request
`walsh-spectral-subset-b904` (a lower bound on `wt(Φ_n h)` for h not
"complicated"):

1. **The fold's column reading is the no-carry / submask relation.** A 1 at input
   position `j` reaches output position `i` iff `i−j free of j`; the count of
   such (the hit-set `|H_j| = #{d ∈ [2,n−1] : j ∈ M_d}` already computed in
   CONCLUSION-PASS2 §5) is exactly the number of `i` with `i−j free of j`. The
   existing hit-set table (fraction of large |H_j| falls like 1/n, median stays
   tiny) is the empirical side of this no-carry relation. No new number here —
   confirms the existing §2 / §5 measurements from the algebra side.

2. **The inverse zero pattern being identical to the fold's** says the fold is
   far from rank-deficient in the "+/−1" sense: on the free-of support it is
   essentially a signed permutation/rescaling with known signs, so low weight of
   `Φ_n h` is not forced by any structural "averaging out" in `S` — the
   non-cancellation already used in `enminus2-linear-supply` is what this
   theorem formalises. Notably `S = S(1)` and `S(−1) = S⁻¹` means the fold on a
   uniform input sends it to a vector whose weight is governed by the same
   no-carry support — consistent with the proved exact Binomial(n−2,1/2) law.

3. **Sense for the Walsh/subset-sum route.** The no-carry condition is what the
   "read-cone / hit-set" functional of GOAL priority 1 is the arithmetic of, so
   this pins that functional's algebra as one the fold's own inverse carries. It
   does **not** itself prove `wt(Φ_n h) ≥ c n` for the primes; it is a structural
   fact, not a supply theorem.

## Status / honest labels

Structural fact, proved in source (short, self-contained combinatorial proof via
Kummer + the free-of matrix family; also a Kronecker-product observation by
Bacher, added in proof). Not a SUPPLY result. Not a numeric computation — no
claim blocks with numbers to add. Fits the existing fold-geometry tier; the
`downset-row-intersection-meet-formula` and `fold-distance-enumerator-On` claims
already capture the row-side, this adds the inverse column-side sign structure.

## Relations

- Same subject as (in-library): `hofer_pascal_matrices_mod2`,
  `bacher_beeblebrox_reduction`, `mestrovic_lucas_theorem_survey`,
  `szechtman_sums_binomial_modp`, `rampersad_wiebe_2regular`.
- Cites **Bacher–Chapman, *Symmetric Pascal matrices modulo p*** (European J.
  Combin. 25, 2004, 459–473; arXiv:math.NT/0212144) — added to FRONTIER.md by
  the download. This is a directly relevant primary for the mod-p Pascal-matrix
  family the fold is a member of, and is **not** in the library (Bacher's
  `bacher_beeblebrox_reduction` is a different Bacher paper). A candidate for
  the next fetch.
- Cites Bacher, *La suite de Thue-Morse et la catégorie Rec* (CRAS 342, 2006)
  — the k-regular/Rec category connection to Thue-Morse, matching the in-library
  Allouche–Shallit / k-regular tier.
