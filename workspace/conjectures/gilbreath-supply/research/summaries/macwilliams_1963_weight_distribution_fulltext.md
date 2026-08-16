# Summary — MacWilliams (1963), "A theorem on the distribution of weights in a systematic code"

Source: Jessie MacWilliams, *Bell System Technical Journal* 42 (1963) 79–94 (thesis, Harvard). Source URL: https://user.eng.umd.edu/~abarg/ECC/macwilliams1963.pdf. Full text: [[research/sources/macwilliams_1963_weight_distribution_fulltext.full]].

## What this establishes

The **original statement of the MacWilliams identity** — the linear equations relating the weight distribution of a linear code to that of its dual. For a systematic (linear) code `C ⊆ F^n`, `q` elements, dimension `k`, write `A_i` = # codewords of weight `i`, `B_i` the same for the dual `C^⊥` (dimension `m = n−k`). With `v = q−1`:

**Theorem 1.** `Σ_{i=0}^n A_i (1+v z)^{n−i}(1−z)^i = Σ_{i=0}^n B_i z^i`.

Equivalently the dual weight distribution is the Krawtchouk (MacWilliams) transform of `C`'s: `W(C^⊥;x,y) = (1/|C|)·W(C; y−x, y+x)`. The paper is the *source paper*: it proves the identity by elementary linear algebra (generating functions) and gives the necessary-condition corollary for a set of weights to be realisable as a code spectrum. The identity holds for equivalent codes and is multiplicative for decomposable (direct-sum) codes (Cor 1.1).

## Why it matters for SUPPLY — the Walsh connection

This is the origin of the exact tool the run's open request `walsh-spectral-subset-b904` sits on. The machinery: for a linear map / code `C`, the dual weight distribution is the **Walsh/Hadamard transform** of the code's weight distribution, and the Krawtchouk polynomials are exactly the orthogonal polynomials diagonalising that transform over the Boolean cube. For the fold `Φ` of SUPPLY, `wt(Φ_n h)` is an image-weight under an `F₂`-linear map — the same kind of quantity the MacWilliams identity trades between a code and its dual. The identity is the reason weight-distribution questions on `F₂^n` can be attacked spectrally (Krawtchouk eigenvalues), which is the direction the open request wants.

**Does not settle the request:** MacWilliams' identity is a transform *of* weight distributions (a statement about their functional relationship), not a lower bound on a single folded image `wt(Φ_n h)` from an input hypothesis. Its equality/structure identifies the Krawtchouk basis as the right coordinate system, but a bound on `wt(Φ_n h)` still needs an arithmetic input on `h`.

## What would falsify its bearing

If someone treated the MacWilliams identity as itself giving `wt(Φ_n h) ≥ c·n`: it does not — it relates weight *distributions* of a code and its dual, not the weight of one folded vector, and gives no input-dependent lower bound.

```claim
id: macwilliams-weight-distribution-theorem
statement: For a linear code C ⊆ F_q^n of dimension k with weight distribution A_i and its dual C^⊥ with B_i, the two are related by Σ_i A_i (1+v z)^{n−i}(1−z)^i = Σ_i B_i z^i (v=q−1), i.e. the dual's weight enumerator is the Krawtchouk-transform of C's; the identity determines B uniquely from A and is a linear system of equations.
hypotheses: C linear (systematic) code over F_q; dual = orthogonal complement; identity holds up to code equivalence, multiplicative for decomposable codes.
holds-here: Yes as machinery — the relevant space is F_2^n and the transform is the Walsh/Hadamard one (Krawtchouk eigenvalues), exactly the coordinate system of the submask-XOR fold Φ.
status: proved (MacWilliams 1963, elementary proof in full text; standard)
bearing: The canonical original statement of the Walsh/Krawtchouk duality on the Boolean cube. Fixes the transform-based (spectral) coordinate system for weight-of-image questions like wt(Φ_n h), the direction of request walsh-spectral-subset-b904. It is a distributional identity, not a per-vector lower bound, so it does not by itself close the request.
anchor: research/sources/macwilliams_1963_weight_distribution_fulltext.full.md, Theorem 1
```
