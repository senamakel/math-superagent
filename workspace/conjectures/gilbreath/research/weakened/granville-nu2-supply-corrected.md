# Weakened ladder: the G-supply statement, corrected to the ledger

This **supersedes** `research/weakened/granville-nu2-supply-ladder.md`, which
carried two rungs as `open` that the claim ledger has since refuted. The
correction is the whole point of this file: those two rungs are recorded here
as `failed`, with the exact counterexample, so the forward loop does not pay
for them a third time.

The axis is the run's **primary open content** (Route B, Granville ν₂). The
goal is the one unproved supply statement

    ν₂(q_n) ≥ c·n for all n ≥ N,

where ν₂(q_n) is the number of 2s in the maximal `{0,2}` suffix of the right
diagonal `δ_k(q_n) = A_k[n−k]` (k = 0..n−1) of the prime
iterated-absolute-difference triangle. By Granville Lemma 5.4 — proved on the
even domain here (claim `lemma54-re-derived-proof`; descent core
Lean-formalised, claims `descent-lemma-halved-formalised`,
`lemma54-composition-lean-formalised`) — plus Theorem 5.5 with the demand side
`g*_n < n^α`, α = 0.52 **unconditional** (Baker–Harman–Pintz 2001 sharpened
by Li 2023, claim `li2023-short-interval-052`), a settled top rung *is* a
settled conjecture.

**What changed.** In the superseded ladder the climb went
`ancestor-window → invertible-image → weight-ratio → gap-mod4-density`. The
middle two steps are dead:

- the diagonal transfer matrix is **not invertible** (kernel = the all-ones
  vector, i.e. the consecutive-odds input), and
- a universal Hamming-weight lower bound `wt(M·h) ≥ wt(h)/c` is **false**
  (that same all-ones vector maps to weight 0 while having weight n−2).

So the structural half of Route B resolves cleanly: everything combinatorial is
either settled or refuted, and the *only* surviving open content is the
prime-specific density of the mod-4 switch bit. That is the named-open
statement (ABGS 2011 §9, claim `abgs-2011-s9-mod4-switch-limit-open`), and the
run's deliverable is the conditional theorem at that hypothesis.

**The six difficulties.**

- `infinite-horizon` — the target quantifies over every n ≥ N; a finite
  measurement is a fact about those n only.
- `nu2-diagonal-indirection` — ν₂ lives on a diagonal of the nonlinear
  triangle, not on the input; the naive route `A_k = |forward difference|` is
  refuted (`fwd-diff-identity-refuted`).
- `transfer-linear-bound` — the diagonal `{0,2}`-tail bits are an F2-linear
  image of the halved gap bits, but linearity alone gives **no** Hamming-weight
  lower bound; this is exactly where the superseded ladder broke.
- `gap-mod4-density` — the gap-mod-4 bit `h[j] = [gap_{j+1} ≡ 2 (mod 4)]` has
  no proved positive-density lower bound.
- `fluctuation-one-sided` — even a correct mean n/2 does not give a one-sided
  bound: the mod-4 bias oscillates Littlewood-type.
- `demand-side-unconditional` — Theorem 5.5 needs the record-gap bound
  `g*_n < n^α`; already switched off for the primes (BHP/Li α = 0.52), kept
  only so the top rung states its hypotheses exactly.

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
merge: Replace the eight finite samples with a per-n structural statement. First move: the ancestor-window lemma (next rung), pure index arithmetic that converts "ν₂ is a triangle-diagonal quantity" into "ν₂ is carried by the fixed gap-bit window [2, n−1]".
```

```rung
id: R-lemma54-demand-leg
statement: Granville Lemma 5.4, proved on the even domain: for ε ∈ {0,2}^L with ν₂ = #{k : ε_k = 2}, and the orbit δ₀ = v (even), δ_k = |δ_{k−1} − ε_k|, one has δ_L ∈ {0,2} ⟺ v ≤ 2ν₂+2, and {0,2} is absorbing. This is the demand→success leg the supply bound plugs into (claim lemma54-re-derived-proof; descent core Lean-formalised).
off: nu2-diagonal-indirection, transfer-linear-bound, gap-mod4-density, fluctuation-one-sided, demand-side-unconditional
stance: settled
merge: This consumes ν₂ but does not produce it. Turn nu2-diagonal-indirection back on: prove where the {0,2}-tail cells come from in row 1 (the ancestor window, next rung).
```

```rung
id: R-ancestor-window-fixed-interval
statement: In the prime triangle, the halved bits of the maximal {0,2} suffix of diagonal n (cells (k, n−k), k = K..n−2) are each an F2-linear (Pascal-mod-2, XOR/Rule-90) combination of the halved row-1 gap bits h[j] = (A₁[j]/2) mod 2 = [gap_{j+1} ≡ 2 (mod 4)] over the fixed interval j ∈ [2, n−1] — independent of where the suffix starts K (the single cell k = n−2 already reaches column 2, and the union over k ∈ [K, n−2] of ancestor intervals [n−k, n−1] is exactly [2, n−1]).
off: gap-mod4-density, fluctuation-one-sided, demand-side-unconditional
stance: settled
merge: The Pascal-mod-2 linearization is proved (rule90-interior-xor) and the fixed-window union is index arithmetic (g-supply-transfer-measured, checked). Turn transfer-linear-bound's explicit form back on: write the matrix out (next rung) — the step from "linear image" to an explicit matrix is where the invertibility error lives.
```

```rung
id: R-transfer-matrix-form
statement: The F2 transfer matrix Φ_n, rows k = 2..n−2 (halved {0,2}-tail cells of the right diagonal), cols j = 2..n−1 (halved gap bits h), has entry Φ_n[k][j] = C(k−1, j−(n−k)) mod 2, shape (n−3)×(n−2), rank n−3, nullity 1, and kernel = span(111…1) for every n = 2..20 (claim transfer-matrix-kernel-allones).
off: gap-mod4-density, fluctuation-one-sided, demand-side-unconditional
stance: settled
merge: The matrix is linear but NOT invertible — it is surjective with a one-dimensional kernel. This kills the "invertibility ⟹ density preservation" hope before it is stated; the next rung records the death of the universal weight transfer that the superseded ladder tried to climb through.
```

```rung
id: R-universal-weight-ratio
statement: For the transfer matrix Φ_n, every nonzero halved gap-bit window h over [2, n−1] satisfies weight(Φ_n·h) ≥ weight(h)/c for a universal c > 0.
off: gap-mod4-density, fluctuation-one-sided, demand-side-unconditional
stance: failed
merge: REFUTED, do not re-attack. The consecutive-odds input (all gaps 2, so h = 111…1) is a successful triangle with ν₂ = 0 for every n ≥ 4, while weight(h) = n−2 and weight(Φ_n·h) = 0 — so the ratio is 0 for all n and no positive c exists (claim transfer-matrix-kernel-allones). Even the weaker ν₂ ≥ w/2 is not a universal F2 identity: the all-2 gap string of length 12 has w = 12, ν₂ = 1 (claim g-supply-transfer-universal-refuted). The density transfer is prime-specific, not a combinatorial weight inequality; the surviving rung is the prime-specific statement, next.
```

```rung
id: R-nu2-prime-transfer
statement: For the primes (not all successful prefixes), ν₂(q_n) ≥ w(n)/c for some universal c > 0, where w(n) = weight of h over [2, n−1]. Measured: ν₂/w ≥ 0.5152 over the dense scan n ∈ [50,3000] (minimum at n = 53), ≥ 0.689 on the sparse set {50..3999} — so c = 2 works on every measurement made so far (claims g-supply-transfer-measured, nu2w-minima-reconciled).
off: gap-mod4-density, fluctuation-one-sided, demand-side-unconditional
stance: open
merge: This is the prime-specific remnant of the dead universal rung: the transfer survives for the primes as a measured fact, not a theorem, and no unconditional proof exists (the consecutive-prime mod-4 correlation is named-open, claim abgs-2011-s9-mod4-switch-limit-open). Compose it with a lower bound on w(n) itself — turn gap-mod4-density back on (next rung). First move: state the conditional theorem "w(n) ≥ c′·n ⟹ ν₂ ≥ c·n" with the two-point mod-4 correlation bound as its hypothesis.
```

```rung
id: R-gap-mod4-density
statement: For the primes, the halved-gap bit h[j] = [p_{j+2} − p_{j+1} ≡ 2 (mod 4)] has Hamming weight w(n) ≥ c′·n for all n ≥ N, for some absolute c′ > 0. Measured w/n ≈ 0.60; the Lemke Oliver–Soundararajan two-point statistic gives the mean n/2 but only as an oscillating estimate (claims g-supply-transfer-measured, los-2016-consecutive-pair-mod4-bias).
off: fluctuation-one-sided, demand-side-unconditional
stance: open
merge: The mean n/2 is unconditional (PNT in arithmetic progressions), but a one-sided lower bound must survive the Littlewood-type oscillation of the mod-4 bias — and ABGS 2011 §9 records that whether the consecutive-pair frequency tends to ANY limit is open, so no unconditional linear lower bound on the switch count exists in the literature. This is the named-open core; turning it back on is the top rung.
```

```rung
id: R-gsupply-full
statement: ν₂(q_n) ≥ c·n for all n ≥ N (combining R-nu2-prime-transfer's ν₂ ≥ w/c with R-gap-mod4-density's w ≥ c′·n). By Lemma 5.4 (proved, even domain) and Theorem 5.5 with the unconditional demand bound g*_n < n^0.52, this gives A_k(0) = 1 for every k ≥ 1 — Gilbreath's conjecture.
off: demand-side-unconditional
stance: open
merge: n/a — top of the ladder. The ladder is exhausted exactly when this rung settles; reaching it means the one-sided prime-gap-mod-4 frequency bound (fluctuation-one-sided, named-open) has been turned back on and survived, which no held theorem does.
```

## Summary

- **Settled floor, four rungs deep.** `R-nu2-finite-measurement`
  (`granville-nu2-density-measured`, checked), `R-lemma54-demand-leg`
  (`lemma54-re-derived-proof`, proved), `R-ancestor-window-fixed-interval`
  (`rule90-interior-xor` proved + fixed-window index arithmetic checked),
  `R-transfer-matrix-form` (`transfer-matrix-kernel-allones`, checked).
- **One shortcut dead and now recorded as such.** `R-universal-weight-ratio`
  is refuted by the consecutive-odds kernel vector; the superseded ladder's
  `R-halved-diagonal-invertible-image` was false because the matrix has
  nullity 1, not full rank. The block-edge erosion map *is* unitriangular
  (`edge-interior-invertibility-sharpened`), but that map is not the diagonal
  transfer — conflating the two was the error.
- **Attack next.** The single open content is prime-specific and named-open:
  the one-sided lower bound on the mod-4 switch bit. The attackable form is
  the **conditional theorem** "two-point mod-4 correlation lower bound
  ⟹ ν₂ ≥ c·n ⟹ Gilbreath", which is exactly the deliverable GOAL.md already
  names.
- **Expected bite.** `gap-mod4-density` / `fluctuation-one-sided` — a
  one-sided density bound on primes with gap ≡ 2 (mod 4) must survive
  Littlewood-type oscillation, and no held theorem provides it (ABGS 2011 §9:
  even the existence of a limiting ratio is open).
