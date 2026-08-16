# Summary — Prime polynomials in short intervals and in arithmetic progressions

Source: Efrat Bank, Lior Bary-Soroker, Lior Rosenzweig, "Prime polynomials in
short intervals and in arithmetic progressions", Duke Math. J. 164 (2015), no. 2,
277–295. arXiv:1302.0625 (correct arXiv; full text at
`bank_barysoroker_rosenzweig_1302.0625.full.md`).

> **CORRECTION RECORD — do not trust any other file under this name.**
> An earlier download named `bank_barysoroker_rosenzweig_prime_polynomials_full`
> first resolved to the WRONG paper — arXiv:1405.1829, a physics/optics preprint
> ("PT-symmetric coupler with a coupling defect") — because the arXiv ID was
> guessed. That wrong content is NOT this paper and must not be cited. The
> correct arXiv for this Duke paper is **1302.0625**, verified against the
> abstract (same three authors, same short-interval + AP results). Overwritten
> here. Lesson (matching `DELETED_wrong_arxiv.md`): never guess an arXiv ID;
> verify the fetched title against the intended paper and arXiv IDs via search
> or citation graph.

## What this establishes

Function-field (F_q[t]) analogues of two classical prime-number conjectures,
in the large-finite-field limit q → ∞.

- **Short intervals.** For fixed degree k, the number of prime (monic
  irreducible) polynomials in the short interval
  `I(f, ε) = {g ∈ F_q[t] : deg(f−g) ≤ ε·deg f}` satisfies
  `π_q(I(f, ε)) ~ #I(f, ε)/k` uniformly, subject to `ε ≥ ε₀(f,q)`, where
  `ε₀ = 1/k`, or `2/k` if `p | k(k−1)`, or `3/k` if `p=2` and `deg f' ≤ 1`.
  The estimate FAILS in the neglected (too-short-interval) cases — explicitly
  exhibited.
- **Arithmetic progressions.** For relatively prime polynomials `D, f ∈ F_q[t]`
  with `‖D‖ ≤ q^{k(1−δ₀)}`, the count `π_q(k; D, f)` of degree-k prime
  polynomials `≡ f (mod D)` satisfies `π_q(k; D, f) ~ π_q(k)/φ(D)` uniformly,
  with `δ₀ = 3/k`, or `4/k` if `p=2` and `(f/D)'` is constant. Also generalised
  to other factorization types.
- Error terms are of size `O(π_q(k) q^{−1/2}/φ(D))` when
  `1 ≤ deg D ≤ k−3` (or `k−4` in the exceptional case).

## Why it matters here

This is one of the four grounding sources of the **adopted** function-field
model approach (`function-field-fqt-model`). It supplies the *one-point /
value-domain* machinery: irreducibles equidistribute in residue classes mod D
and in short intervals, effectively and in the large-q limit.

**The transfer gap (load-bearing, not closed by this source):** every statement
here is one-point (single irreducibles at given degree/residue class) or
macroscopic short-interval. None controls the *degree-ordered lex-consecutive*
switch statistic that the fold's two-point object reads — two irreducibles
adjacent in the degree-then-lexicographic order with difference non-zero mod T².
The grounding note for `function-field-fqt-model` states this explicitly: the
"switch-density analogue is a provable Chebotarev statement" claim over
F_2[t] is NOT what the sources give; the lex-consecutive pair is plausibly as
delicate as over Z. So this source grounds the one-point input, not the
two-point object.

```claim
id: bbsr-function-field-short-interval-AP
statement: Over F_q[t] as q → ∞, degree-k prime polynomials are equidistributed in
  short intervals I(f,ε) (π_q(I(f,ε)) ~ #I(f,ε)/k) and in arithmetic progressions
  mod D up to ‖D‖ ≤ q^{k(1−δ₀)} (π_q(k;D,f) ~ π_q(k)/φ(D)), with explicit ranges
  and error O(π_q(k)q^{−1/2}/φ(D)); the short-interval estimate fails in explicit
  too-short ranges.
hypotheses: large-finite-field limit q → ∞, fixed degree k; uniformity over f, D;
  the stated ε₀ / δ₀ exceptional conditions.
holds-here: yes for the one-point / value-domain PNT-in-AP input the function-field
  model's arithmetic relies on; NO for the degree-ordered lex-consecutive two-point
  switch object (never controlled here).
status: proved (Bank–Bary-Soroker–Rosenzweig 2015, arXiv:1302.0625).
bearing: grounds the one-point side of the adopted function-field model; the
  consecutive-switch transfer is open and is the model's own step to price.
anchor: research/sources/bank_barysoroker_rosenzweig_1302.0625.full.md
```

## Keyword map
function field; prime polynomials; short intervals; arithmetic progressions;
Chebotarev; large finite field limit; irreducibles; PNT in AP.
