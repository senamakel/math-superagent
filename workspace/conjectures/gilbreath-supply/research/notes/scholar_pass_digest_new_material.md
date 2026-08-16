# Scholar pass — digest of new material since the last reconciliation

Author: scholar. The research agent has finished; the library is mature. What is
genuinely NEW in `research/` since the last scholar digest is not a batch of full
texts but: (1) the **pass-3 threshold computation** (GOAL.md's single owed
computation, resolved), with its four claim blocks, and (2) the **HJT 2024**
primary source grounding the log-periodic representation. Two Thue–Morse full
texts (Spiegelhofer, Müllner–Spiegelhofer) were added earlier and are already
digested; I re-confirmed their claim blocks reach the ledger.

## What the new material establishes (against SUPPLY, the goal, current beliefs)

**Pass-3 threshold result (measured-not-proved, the pass's affirmative).** The
question GOAL.md set — does the min weight ratio at which linear supply becomes
typical tend to 0 or plateau near 1/8 — is answered: **it tends to 0**. The
threshold *weight* is sublinear, `w*(n) ≈ n^0.555 · P(log₂ n)` with `P`
bounded, period-1-in-log₂(n), amplitude ~0.07. Per-n `w*` is exact (closed-form
Krawtchouk sphere mean, no sampling) for n = 8..262144; the exponent 0.555 and
the limit are fitted, not proved. Consequences and bounds:

- **What it does.** Reduces the arithmetic demand from positive mod-4 switch
  density (`Θ(n)` switch pairs) to a **sublinear switch count ~n^0.55** — the
  workspace's first affirmative weakening across three passes. It is result
  type 4 (input strictly weaker than switch density), **never** type 1
  (unconditional SUPPLY), never prime-specific.
- **Closed forms rejected.** `c√n` (E=1/2) at >25σ, `n^{log₂3−1}` (E=0.58496)
  at >14σ. `5/9` is *not separable* from the fitted 0.555 — do not adopt it.
- **What it does NOT prove.** The limit theta→0, the exponent 0.555, and the
  log-periodic amplitude are fitted over n ≤ 65536 — supporting data, not a
  theorem. This pass-2 "1/8 plateau" is refuted as a coarse-grid artifact.
- **Genericity gap unchanged:** *typical is not this string* — being above the
  threshold does not prove the primes' own h has linear supply. Nothing here is
  a proof of SUPPLY.

**The two open lemmas (the named gap measurement → theorem).** `G-threshold-
asymptotic-zero` (biased-cell sum → 0 for every fixed θ, so E[ν₂/n]→1/2 and
θ_mean(n)→0) and `G-threshold-concentration` (Var(ν₂)=o(n²), fraction criterion
holds in the limit). Both are PURE F2/hypergeometric — **no primes, no number
theory** — the most tractable open items in the workspace. Both rest on the
single self-provable hypergeometric mode bound
`|E[(-1)^X]| ≤ max_j P[X=j] = O(1/√(1+Var X))` (X ~ Hypergeometric(n,m,w)),
which the on-disk library does not state. The earlier refuted pointwise bound
`|E[(-1)^X]| ≤ (1−2θ)^m` must NOT be resurrected (n=6,m=3,w=2 counterexample).

**HJT 2024 (the new primary source).** Theorem 2.2 proves the log-periodic
representation `F_p(n) = n^ρ·P(log_p n)`, ρ = log_p((p+1)/2), for the count of
Pascal entries not divisible by p; p=2 is OEIS A006046 with ρ₂ = 0.58496
(claim `hjt-p2-log-periodic-representation-proved`, status proved). This
*grounds the FORM* hypothesis for w*(n) in a theorem but does **not** transfer
the exponent — the run's own tabulation decided w*'s exponent is ~0.555,
distinct from ρ₂. The analogy is structural, not a matching of constants.

## Independent verification this pass (not on the prior pass's word)

I re-derived the load-bearing exact-mean formula (claim
`sphere-mean-krawtchouk-exact` / `threshold-mean-exact-parity-formula`) at its
anchor n=4, w=1 by hand: formula gives P(d=2)=1/2, P(d=3)=1, total E=3/2, and
brute enumeration of the 4 weight-1 strings gives ν₂ = (1,2,1,2), mean 6/4 =
3/2. ✓ Matches exactly. I wrote `code/scholar/verify_sphere_mean_formula.py`
for the mechanical full sweep (n=3..12, all w) — coder's to run via lib.capture.

## Contradictions with recalled memory

None new at the level of two theorems that both hold. Two reconciliations:

1. **Pass-2/1/8 superseded (not a contradiction, a correction).** `threshold-
   weight-sublinear` `contradicts:` the pass-2 "plateau near 1/8" reading — that
   was a 300-sample/coarse-grid sampling artifact; the exact mean shows 0.109@64,
   0.086@128, not 0.125. The ledger already records this.
2. **Request closure is NOT granted.** G-threshold lemmas and the w* result do
   NOT close `walsh-spectral-subset-b904` — that request is about the *prime
   string* (its second-moment bound), not the generic weight threshold. It
   stays open, as does the finite-prefix transfer.

## Sources that do not help (so nobody re-reads them)

Confirmed unchanged from prior passes: the seven `citations_w*` files (lead-only
citation graphs), the four OEIS rows unrelated to the fold, `odlyzko_gilbreath`
(bibliography), the Granville–Martin duplicate mirror, `matomaki_radziwill_tao_
averaged_chowla` (quarantined wrong download), the two metadata stubs
(`ashikhmin_barg_litsyn`, `friedlander_macwilliams_krawtchouk`), the HAL page,
the `DELETED_*` overwrite notes. The `mauduit-rivat-*`, `green_tao_mobius_*`,
`matomaki_radziwill_*` analytic-NT tier is value-domain machinery whose
index-domain transfer is absent — refuted approaches, not evidence for SUPPLY.

## What the run still lacks (unchanged, precisely)

1. **`E[S(n)²]=O(n)` for the specific prime gap-parity string** — the single
   surviving route to density-1 SUPPLY (request `walsh-spectral-subset-b904`,
   still open). The pass-3 generic result does not touch it.
2. **The finite-prefix transfer** — ergodic Lucas-mixing randomization ⇒
   quantitative `wt(Φ_n h) ≥ c·n` for the one fixed string. Larger missing tool.
3. **Proof of the threshold limit** — the hypergeometric mode bound
   (G-threshold-parity-control), which is self-provable with no new source.
   THIS is the natural next attack for a theorem-prover/symbolic role.

## Durable findings stored

Pass-3 threshold result (tends to 0, sublinear exponent ~0.55, type 4 not 1);
HJT 2024 grounding the log-periodic form; the two Thue–Morse level-of-
distribution negative pricings. All source-backed, with hypotheses and bounds.
