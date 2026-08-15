# Weakened ladder: the G-supply statement ν₂(q_n) ≥ c·n

This ladder decomposes the run's **primary open content** (Route B, Granville
ν₂), not the block-length axis. The other ladders
(`recharge-ladder.md` canonical, `gilbreath-regeneration-ladder.md`,
`regeneration-ladder.md`) all climb the regeneration-rate axis; the single
statement that now carries the whole of Route B is the supply-side density
bound

    ν₂(q_n) ≥ c·n for all n ≥ N,

where ν₂(q_n) is the number of 2s in the maximal `{0,2}` suffix of the right
diagonal `δ_k(q_n) = A_k[n−k]` (k = 0..n−1) of the prime Gilbreath triangle.
By Granville Lemma 5.4 — **proved on the even domain** by this run, claim
`lemma54-re-derived-proof` — plus Theorem 5.5 with the demand side
`g*_n < n^α`, α = 0.52 **unconditional** (Baker–Harman–Pintz 2001 sharpened
by Li 2023, claim `li2023-short-interval-052`), this settles Gilbreath's
conjecture. So a settled top rung here *is* a settled conjecture; the ladder
is the goal narrowed to the one unproved supply statement.

**The six difficulties**, each specific:

- `infinite-horizon` — the target quantifies over every n ≥ N; a finite
  measurement is a fact about those n only.
- `nu2-diagonal-indirection` — ν₂ is defined on a *diagonal of the nonlinear
  triangle*, not on the input; relating it to the prime gaps is itself content,
  and the naive route (A_k = |forward difference|) is refuted
  (`fwd-diff-identity-refuted`).
- `transfer-linear-bound` — the structural transfer (diagonal `{0,2}`-tail bits
  = an F2-linear, invertible image of the halved gap bits) is proposed but not
  proved; and invertibility alone does **not** control Hamming-weight
  distortion, so the density-preservation bound ν₂ ≥ w/c is a separate, real
  combinatorial claim.
- `gap-mod4-density` — the gap-mod-4 bit `h[j] = [gap_{j+1} ≡ 2 (mod 4)]` has
  no proved positive-density lower bound; the Lemke Oliver–Soundararajan
  two-point statistic (claim `los-2016-consecutive-pair-mod4-bias`) gives only
  a mean, and its bias term is conjectural.
- `fluctuation-one-sided` — even a correct mean n/2 does not give a one-sided
  lower bound: the mod-4 bias oscillates Littlewood-type, so ν₂ ≥ c·n must
  survive fluctuation, and no held theorem provides that.
- `demand-side-unconditional` — Theorem 5.5 also needs the record-gap bound
  g*_n < n^α. This one is **already switched off for the primes** (BHP/Li
  α = 0.52), so it appears only so the ladder's top rung states its own
  hypotheses exactly.

```ladder
goal: Prove ν₂(q_n) ≥ c·n for all n ≥ N for some absolute c > 0, N, where ν₂(q_n) is the number of 2s in the maximal {0,2} suffix of the right diagonal δ_k(q_n) = A_k[n−k] (k = 0..n−1) of the prime iterated-absolute-difference triangle. Combined with the proved Lemma 5.4 (even domain) and the unconditional demand bound g*_n < n^0.52 (BHP/Li), this settles Gilbreath's conjecture.
difficulties: infinite-horizon, nu2-diagonal-indirection, transfer-linear-bound, gap-mod4-density, fluctuation-one-sided, demand-side-unconditional
status: open
```

## Rungs, bottom to top

```rung
id: R-nu2-finite-measurement
statement: For the prime triangle below 3e6, ν₂(q_n)/n ∈ [0.42, 0.52] at n ∈ {50,100,200,400,800,1600,3200,3999}, ν₂ exceeds n^0.52 by a factor 26 at n=3999, and the Lemma 5.4 budget 2ν₂+2 ≥ g*_n holds at every sample (claim granville-nu2-density-measured).
off: infinite-horizon, nu2-diagonal-indirection, transfer-linear-bound, gap-mod4-density, fluctuation-one-sided, demand-side-unconditional
stance: settled
merge: Replace the eight finite samples with a per-n structural statement. First move: the ancestor-window lemma (R-ancestor-window-fixed-interval), which is pure index arithmetic and converts "ν₂ is a triangle-diagonal quantity" into "ν₂ is carried by the fixed gap-bit window [2, n−1]". This is the bottom, settleable today.
```

```rung
id: R-lemma54-demand-leg
statement: Granville Lemma 5.4, proved on the even domain: for ε ∈ {0,2}^L with ν₂ = #{k : ε_k = 2}, and the orbit δ₀ = v (even), δ_k = |δ_{k−1} − ε_k|, one has δ_L ∈ {0,2} ⟺ v ≤ 2ν₂+2, and {0,2} is absorbing. This is the demand→success leg the supply bound plugs into (claim lemma54-re-derived-proof).
off: nu2-diagonal-indirection, transfer-linear-bound, gap-mod4-density, fluctuation-one-sided, demand-side-unconditional
stance: settled
merge: This consumes ν₂ but does not produce it — it is the "if supplied, success follows" half, closed with a valid proof (the δ=0 case Granville discarded is handled as the 0→2 bounce). Next rung turns nu2-diagonal-indirection back on: prove where the {0,2}-tail cells come from in row 1.
```

```rung
id: R-ancestor-window-fixed-interval
statement: In the prime triangle, the halved bits of the maximal {0,2} suffix of diagonal n (cells (k, n−k), k = K..n−2) are each an F2-linear (Pascal-mod-2) combination of the halved row-1 gap bits h[j] = (A₁[j]/2) mod 2 = [gap_{j+1} ≡ 2 (mod 4)] over the fixed interval j ∈ [2, n−1] — independent of where the suffix starts K (the single cell k = n−2 already reaches column 2, and the union over k ∈ [K, n−2] of ancestor intervals [n−k, n−1] is exactly [2, n−1]).
off: gap-mod4-density, fluctuation-one-sided, demand-side-unconditional
stance: open
merge: One-session corollary of the already-established mod-4 Pascal linearization (claim mod4-linearization, CHT Lemma 3.10, rule90-interior-xor): within the even domain, halving turns |a−b| into XOR, so every halved diagonal cell is a Pascal-selected XOR of halved gap bits. Settle it by writing the index arithmetic for the ancestor-union. Then turn the invertibility half of transfer-linear-bound back on (R-halved-diagonal-invertible-image).
```

```rung
id: R-halved-diagonal-invertible-image
statement: The map from the halved gap-bit window h[2..n−1] to the halved bits of the {0,2}-tail of diagonal n is F2-linear with a unitriangular (hence invertible) matrix in reversed column order — the whole-diagonal generalisation of the proved block-edge map (claim edge-interior-invertibility-sharpened).
off: gap-mod4-density, fluctuation-one-sided, demand-side-unconditional
stance: open
merge: Invertibility alone is NOT enough for the next step: a unitriangular invertible map can send a dense window to a sparse image or vice versa. The next rung (R-nu2-weight-ratio) is the density-preservation claim ν₂ ≥ w/c for the *specific* Pascal-convolution matrix — this is where the transfer is expected to bite, and it is a concrete combinatorial claim a forward attempt can attack today.
```

```rung
id: R-nu2-weight-ratio
statement: For the transfer matrix of R-halved-diagonal-invertible-image, every nonzero halved gap-bit window h over [2, n−1] satisfies weight(M·h) ≥ weight(h)/c for a universal c. Measured: ν₂/w ∈ [0.689, 0.867] on all eight prime samples, so c = 2 (i.e. ν₂ ≥ w/2) is the plausible target and c ≤ 2 already holds empirically.
off: gap-mod4-density, fluctuation-one-sided, demand-side-unconditional
stance: open
merge: This closes the structural half: ν₂ ≥ w/c for a universal c. It is a pure F2-linear-algebra statement about the Pascal-convolution (Rule-90) matrix and is the first place the structural hope can die — invertible maps do not preserve Hamming weight. If it fails, that is a finding that Route B's transfer does not exist at this level and the indirection must be handled differently. On success, turn gap-mod4-density back on (R-gap-mod4-density).
```

```rung
id: R-gap-mod4-density
statement: For the primes, the halved-gap bit h[j] = [p_{j+2} − p_{j+1} ≡ 2 (mod 4)] has Hamming weight w(n) ≥ c′·n for all n ≥ N, for some absolute c′ > 0 (measured w/n ≈ 0.60; the Lemke Oliver–Soundararajan two-point statistic gives the mean n/2 but only as an oscillating estimate).
off: fluctuation-one-sided, demand-side-unconditional
stance: open
merge: The two-point main term n/2 is unconditional (PNT in arithmetic progressions / LOS eq 5.1), but a one-sided lower bound must survive the Littlewood-type oscillation of the mod-4 bias. That is the last difficulty, turned back on in the top rung (R-gsupply-full); it is the number-theoretic core and the place the whole ladder is expected to stall for good.
```

```rung
id: R-gsupply-full
statement: ν₂(q_n) ≥ c·n for all n ≥ N (combining R-nu2-weight-ratio's ν₂ ≥ w/c with R-gap-mod4-density's w ≥ c′·n). By Lemma 5.4 (proved, even domain) and Theorem 5.5 with the unconditional demand bound g*_n < n^0.52, this gives A_k(0) = 1 for every k ≥ 1 — Gilbreath's conjecture.
off: demand-side-unconditional
stance: open
merge: n/a — top of the ladder. The ladder is exhausted exactly when this rung settles; reaching it means the one-sided prime-gap-mod-4 frequency bound (fluctuation-one-sided) has been turned back on and survived, which no held theorem does.
```

## Summary

- **Settled floor:** R-nu2-finite-measurement (`granville-nu2-density-measured`,
  checked) and R-lemma54-demand-leg (`lemma54-re-derived-proof`, proved). These
  are the two halves of Route B that are already banked.
- **Attack next:** R-ancestor-window-fixed-interval — a one-session index-arithmetic
  corollary of the already-proved mod-4 Pascal linearization; settling it is the
  cheapest new result on this ladder and it is the bridge every higher rung stands on.
- **Expected first bite:** R-nu2-weight-ratio — the density-preservation of the
  F2-linear transfer is a real combinatorial claim, not implied by invertibility, and
  it has only been observed on eight prime samples, never tested adversarially.
- **Expected final bite (where the whole route stalls):** `fluctuation-one-sided` at
  R-gap-mod4-density — a one-sided bound on the density of prime gaps ≡ 2 (mod 4)
  must survive Littlewood-type bias oscillation, and no held theorem provides that.
