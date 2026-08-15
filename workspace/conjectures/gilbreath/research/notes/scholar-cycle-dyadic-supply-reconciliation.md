# Scholar cycle — dyadic-supply frontier reconciled; no new source to digest

The research agent finished; the reference library is unchanged since the last
closure (12 cycles verified in `library-build-report.md`; REQUESTS.md still
CLOSED). Every held source already has a summary + claim block; the
`citations_*` files under `research/summaries/` are OpenAlex citation-graph
lookups, explicitly "filed, not read," and add no theorem. So the scholar work
this cycle is **not re-digestion** but reconciliation of the newest
<span></span>run-computed claims against durable memory, and locating the one
verification gap left open.

## The genuinely-new content (all run-computed, all already filed as claims)

1. **`dyadic-collapse-proved`** (status: proved): h eventually periodic with
   minimal period a power of two `2^k` ⟹ ν₂(q_n) = O_k(1), sharp bound
   `ν₂ ≤ 2^k − 1` (preperiod N₀: `≤ N₀ + 2^k`). Proof is Lucas (tail cell =
   subset-zeta fold = σ^d h) + Frobenius (`σ^{2^k} = I + S^{2^k} = 0` since
   `S^{2^k} = I`). This is the collapse half of the dyadic dichotomy, and the
   clean answer to *why* constant-gap (P=1) and alternating-2/4 (P=2) inputs
   supply ν₂ = O(1).
2. **`rule90-periodic-window-collapse-refuted`** (checked): the over-general
   "any period collapses" is FALSE — odd-factor periods grow (P=3 ⟹ ν₂ ~ c·n).
   Supersedes the asserted `rule90-periodic-window-collapse`.
3. **`thue-morse-sublinear-supply-witness`** (proved by derivation): Thue–Morse
   h is aperiodic yet ν₂ = O(log n) (ζ(h)[d] = 1 ⟺ d a power of two). So
   "aperiodic ⟹ linear supply" is FALSE; the controlling invariant is 2-adic
   rigidity, not (a)periodicity.
4. **`dyadic-oddfactor-infimum-bounded`** (checked): odd-factor converse NOT
   plateau-refuted to n=24000 (P=3..15: inf ν₂/n in [0.114, 0.647], residual
   O(1)), but stays CONJECTURED and decays as P grows — no uniform c, no
   transfer to the aperiodic primes.

All four fit the adopted approach `dyadic-linear-complexity-supply` (subset-zeta
involution ⟹ supply = positive density of ζ(h), i.e. 2-adic non-rigidity).
**None closes G-supply**: the primes' `ν₂ ≥ c·n` stays the named-open two-point
mod-4 switch hypothesis (`abgs-2011-s9-mod4-switch-limit-open`). The conditional
Route B deliverable is unchanged.

## Verification gap found (the one open item)

The Thue–Morse machine check `code/out/check_thue_subset_zeta.py` (N=512:
ζ(h)[d]=1 ⟺ d∈{1,2,4,…,512}, and the identity `Σ_{j⊆d} wt(j) =
wt(d)·2^{wt(d)−1}`) has **not been executed** this cycle. The claim is marked
`proved` (the derivation is elementary and hand-checked d≤7); running the check
would upgrade it to `checked`. Operator should run
`timeout 540 python3 code/out/check_thue_subset_zeta.py | tee code/out/check_thue_subset_zeta.captured.txt`
and confirm the nonzero zeta positions are exactly the powers of two ≤ 512.

## Numerical records stored (verified-numerically, CONJECTURAL)
- Independent end-to-end oracle reproduces A_1..A_3 exactly; descent iff 0
  violations (199 cols); ballot & transfer 0 violations (tiny-n {3,4,10,14,16}
  = degenerate empty-{0,2}-tail, recorded honestly). `indep_oracle.captured.txt`.
- Switch-bit two-point structure to 2e8 primes: lag-1 r=−0.0261, drift +0.0964,
  lag≥2 max |r|=0.0031 (<0.005 falsifier), ballot e≥0 every prefix
  (final e=19,272,272). `switch_autocorr_ext.captured.txt`.

## Sources that do not help (say why, so nobody re-reads)
The `citations_*` OpenAlex lookups (Chase, CHT, Odlyzko) — bibliographic only.
The pre-2026 corpus was already digested to claim level in prior cycles.

## What the run still lacks (unchanged)
A proof (or unconditional bound) of `ν₂(q_{n−1}) ≥ c·n`, c>0 — the single
named-open hypothesis of Route B, two-point mod-4, conditional at HL/LOS level.
The dyadic dichotomy sharpens *why* supply can fail but does not supply it.
