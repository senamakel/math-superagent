# Summary — Tao, An uncertainty principle for cyclic groups of prime order

Source: Terence Tao, "An uncertainty principle for cyclic groups of prime order", *Math. Res. Lett.* 12 (2005) 121–127. arXiv:math/0308286 (6th version, 22 Jul 2004).
Source URL: https://arxiv.org/abs/math/0308286 (and https://arxiv.org/html/math/0308286v6). Full text locally at `research/sources/tao_uncertainty_cyclic_prime_html.full.md`.

## What this source establishes

**Theorem 1.1.** Let `p` be prime. If `f : Z/pZ → C` is non-zero, then

`|supp f| + |supp f̂| ≥ p+1`,

and this is **absolutely sharp**: conversely, for any non-empty subsets `A, B ⊆ Z/pZ` with `|A|+|B| ≥ p+1`, there exists `f` with `supp f = A` and `supp f̂ = B`. (Independently discovered by András Biró and Roy Meshulam.)

The engine is **Lemma 1.3 / Chebotarëv's theorem**: every minor of the prime-order Fourier (exponential) matrix `(e^{2πi x_j ξ_k/p})` is non-zero. Proof via a cyclotomic-integer lemma (Lemma 1.2) and a Vandermonde/differentiation argument.

Consequences:
- A sparse polynomial `Σ_{j=0}^k c_j z^{n_j}` with `k+1` non-zero coefficients, restricted to the `p`-th roots of unity, has at most `k` zeroes.
- A short proof of **Cauchy–Davenport**: `|A+B| ≥ min(|A|+|B|−1, p)`.

The paper closes by noting Meshulam's iteration giving, for `(Z/p)^n`,
`p^j |supp f| + p^{n−j−1} |supp f̂| ≥ p^n + p^{n−1}` for all `0 ≤ j ≤ n−1` — the convex-hull sharpening in the multivariate case, whose equality points are exactly subgroup indicators.

## Why it matters for SUPPLY — the F₂-cube additive bound

This is the primary reference for the *additive* (sum-of-supports) uncertainty principle on elementary groups. For SUPPLY the relevant group is `(Z/2)^n` (the Boolean cube), the Walsh–Hadamard basis. Tao's theorem is stated for prime-order cyclic `Z/pZ`, but the cited Meshulam iteration `p^j |supp f| + p^{n−j−1}|supp f̂| ≥ p^n + p^{n−1}` applies to `(Z/p)^n` — and with `p = 2` this is exactly the **multivariate Boolean-cube additive uncertainty principle**:

`2^j |supp f| + 2^{n−j−1} |supp f̂| ≥ 2^n + 2^{n−1}`  for each `0 ≤ j ≤ n−1`,

whose equality cases (per the same theory; see the Matusiak–Özaydın–Przebinda summary) are subgroup/affine-subspace indicators. This is the additive companion to the product bound and is the sharpest known Walsh-side trade-off in the exact coordinate system (Walsh basis over `F₂`) where the submask-XOR fold `Φ` lives.

The relevance to `wt(Φ_n h) ≥ c·n` is directional: these are support-in-Walsh-basis statements, not image-weight statements. The equality cases again are exactly the structured low-weight inputs (subspace indicators — e.g. a subgroup's indicator, of which the all-ones kernel vector and dyadic pathologies are instances) that the five closed doors forbid building on. So the source fixes the sharp Walsh-side bounds and their extremal (subspace) structure, but does not by itself lower-bound `wt(Φ_n h)` from an arithmetic input on `h`; that remains the open gap `walsh-spectral-subset-b904`.

## Evidence class

Proved theorem (published, with full proof; additive, absolutely sharp). Chebotarëv's theorem (all Fourier minors non-zero) is the load-bearing structural fact.

```claim
id: tao-additive-uncertainty-prime-cyclic
statement: For non-zero f : Z/pZ → C with p prime, |supp f| + |supp f̂| ≥ p+1, absolutely sharp; conversely any A,B with |A|+|B| ≥ p+1 are realisable as supports. Via Meshulam's iteration, for (Z/p)^n: p^j|supp f| + p^{n−j−1}|supp f̂| ≥ p^n + p^{n−1} for each 0 ≤ j ≤ n−1 (p=2 giving the Boolean-cube additive bound).
hypotheses: G = Z/pZ prime order, or (Z/p)^n; f non-zero complex; f̂ the (normalized) Fourier transform.
holds-here: For SUPPLY the relevant case is (Z/2)^n (Boolean cube, Walsh–Hadamard basis): the source's Meshulam iteration with p=2 is the multivariate additive uncertainty principle in the coordinate system of the submask-XOR fold Φ. Chebotarëv/minor-nonzero structure is the engine.
status: proved (Tao 2005 Thm 1.1 + cited Meshulam iteration; Chebotarëv Lemma 1.3)
bearing: The sharpest Walsh-side additive bound on the Boolean cube and its extremal subspace-indicator structure. Directional for request walsh-spectral-subset-b904: fixes the Walsh trade-off and its (subspace) equality cases, but does not by itself give wt(Φ_n h) ≥ c·n — the equality cases are exactly the low-weight structured inputs the closed doors forbid, so an input hypothesis on h is still required.
anchor: research/sources/tao_uncertainty_cyclic_prime_html.full.md (Thm 1.1, Lemma 1.3, Meshulam remark)
```

## What would falsify its bearing

If someone tried to use `|supp f| + |supp f̂| ≥ p+1` directly as a bound on `wt(Φ_n h)`: it would fail, because (a) `wt(Φ_n h)` is a co-domain image weight, not a Walsh-basis support size; and (b) the extremals are subspace indicators — e.g. a codimension-1 subgroup, whose indicator is a plus/minus structured object with small Walsh support — and Φ has low-weight images on exactly such structured inputs (the five closed doors). So the additive principle sharpens *what the Walsh side can constrain* but cannot itself yield the linear image-weight lower bound without an arithmetic input on `h`.
