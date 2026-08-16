# Summary — Montgomery–Soundararajan, "Beyond pair correlation"

Source: H. L. Montgomery & K. Soundararajan, *Beyond pair correlation*, in
*Paul Erdős and His Mathematics, I* (Budapest 1999), Bolyai Society Mathematical
Studies vol. 11, pp. 507–514. arXiv:math/0003234. Full text:
`[[montgomery_soundararajan_beyond_pair_correlation.full]]`.

## What this establishes

A primary study of the **full moment hierarchy** (pair and beyond) of the prime
counting function in short intervals, and the arithmetic of the associated
singular series. It is the higher-order (K>1) companion to the pair-correlation
framework this run's reopened territory lives in.

- **Pair correlation → first two moments (RH-conditional equivalence).**
  Goldston–Montgomery (under RH): the Pair Correlation Conjecture is equivalent
  to `∫₀ˣ (ψ(x+h)−ψ(x)−h)² dx ~ hX log(X/h)`. The Cramér model (primes iid with
  prob 1/log n) would instead give `~ hX log X`. These two differ by the factor
  `log(X/h)/log X`, so the second moment *separates* the pair-correlation
  structure from the Cramér model — a template for how a K=2 (beyond-pair)
  statistic can beat a K=1 (independent/pair) model.
- **Higher (beyond-pair) moments, heuristically.** Using a quantitative form of
  the prime k-tuple hypothesis, the authors heuristically determine the **higher
  moments** of `ψ(x+h)−ψ(x)−h`: `ψ(x+h)−ψ(x)` is approximately normal with mean
  `~h` and variance `~h log(X/h)` as `x` ranges in `[1,X]` for `X^ε ≤ h ≤ X^{1−ε}`.
  So the normal shape — and hence the whole moment sequence — is predicted from
  the singular-series arithmetic, not assumed.
- **Numerical confirmation and a correction of the main term.** At `X=10^10`,
  `h=10^5` the measured variance `9.07×10^5` is significantly *smaller* than
  **both** the Cramér `h log X = 23.02×10^5` and the (1)-predicted
  `h log(X/h) = 11.51×10^5`. The resolution is a refined singular-series estimate.
  **Theorem (this paper):** `Σ_{k=1}^{h}(h−k)S(k) = ½h² − ½h log h + A·h + O(h^{1/2+ε})`
  where `S(k) = Π_{p|k}(1+1/(p−1))·Π_{p∤k}(1−1/(p−1)²)` is the Hardy–Littlewood
  singular series (0 for odd k) and `A = (1−C₀−log 2)/2`. This gives the sharpened
  second moment `∫₀ˣ (ψ(x+h)−ψ(x)−h)² dx = hX log(X/h) + B·hX + smaller`, with
  `B = −C₀ − log 2 ≈ −2.41509`, matching the computed `9.098×10^5` against the
  observed `9.066×10^5` far better than either naive model.

## What it implies here

This is a **value-domain** statement: its objects are `ψ(x+h)−ψ(x)` — the count of
primes in a short *interval* `(x, x+h]` — indexed by the location `x`, not the
prime *index*. The fold's own input `h[j] = (p_{j+1}−p_j)/2 mod 2` is governed by
**consecutive-prime residue pairs at prime indices**. The bridge the reopened
pass needs — a K>1 statistic of the fold controlled by an input weaker than
pointwise mod-4 switch density — would have to live at prime *indices*; this
paper lives at prime *values* in short intervals. So it does **not** supply the
index-domain transfer, and it does **not** prove anything about consecutive-prime
residue frequencies.

What it *does* provide for this problem:

- The sharpest statement of the **pair-correlation/Cramér second-moment
  discrimination** and its higher-moment normal-law prediction, which is exactly
  the template for "a K=2 (beyond-pair) functional beats the K=1 independent
  model" that SUPPLY's density-1 averaged form is trying to instantiate at the
  fold.
- The **singular-series moment machinery** (`S(k)` and the refined
  `½h²−½h log h+Ah` estimate) that underlies the pair/frequency side of the
  consecutive-prime problem — the arithmetic layer *behind* the LOS/Wu
  heuristic, now pinned to the observed second moment.
- A caution consistent with the run's CONCLUSIONS: even in the value domain where
  the machinery works, the moment analysis is heuristic (prime k-tuple) except
  for the singular-series refinement, whose *error-term* estimate is blocked by
  the twin-prime conjerror-term `E(X;k)`.

## What it does NOT settle

- Nothing about the fold matrix Φ, wt(Φ_n h), or ν₂.
- No transfer from short-value-intervals to prime-index residue patterns; the
  index-versus-value obstruction that killed eight value-domain routes applies
  here verbatim.
- Conjectural (prime k-tuple) beyond-pair; only the singular-series theorem is
  proved.

```claim
id: msbeyond-second-moment-discriminates-plus-singular-series
statement: >
  (1) Under RH, the Pair Correlation Conjecture is equivalent to
  (1/X)∫₀ˣ(ψ(x+h)−ψ(x)−h)²dx ~ h log(X/h), while the Cramér model gives
  ~ h log X — a factor log(X/h)/log X apart, so the second moment separates the
  pair-correlation structure from the independent model. (2) Beyond-pair:
  heuristically (prime k-tuple) ψ(x+h)−ψ(x)−h is approximately normal with mean
  ~h and variance ~h log(X/h). (3) Proved theorem: Σ_{k≤h}(h−k)S(k) =
  ½h² − ½h log h + A·h + O(h^{1/2+ε}), A=(1−C₀−log2)/2, with S(k) the
  Hardy–Littlewood singular series and B=−C₀−log2≈−2.41509 sharpening the second
  moment to hX log(X/h) + B·hX, matching the measured 9.098e5 vs 9.066e5 at
  X=1e10, h=1e5.
hypotheses: RH for the equivalence direction (1); prime k-tuple for the normal-law
  (2); the singular-series theorem (3) is unconditional.
holds-here: NO for the SUPPLY transfer — the object is value-domain (primes in
  short intervals, indexed by location x), while the fold reads consecutive-prime
  residues at prime indices; the index-versus-value obstruction applies verbatim.
  BUT the second-moment-discriminates template (K=2 beats the independent model)
  and the singular-series machinery are the arithmetic layer behind the
  LOS/Wu consecutive-pair side.
status: sourced — theorem (3) proved in the paper; (1) RH-conditional equivalence;
  (2) conjectural.
bearing: >
  Supplies the strongest short-interval second-moment discrimination (pair
  correlation vs Cramér) and the refined singular-series main term. It is the
  value-domain analogue of the K>1 functional the reopened pass seeks at the
  fold, and a caution: even where the machinery works (short intervals) the
  beyond-pair part is heuristic and the twin-prime error blocks the remainder.
  It does not transfer to the prime-index residue object and closes no request.
anchor: montgomery_soundararajan_beyond_pair_correlation.full (Theorem; §2; Table 1)
```

## Keyword map
pair correlation conjecture; Cramér model; second moment of primes in short
intervals; singular series; prime k-tuple; higher moments; normal law;
beyond pair correlation.
