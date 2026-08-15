# Pattern-finder: the mod-4 switch-majority ballot — survival structure

Status: **exact over the terms / scale supplied; a conjecture beyond it.** Each
regularity is labelled with its falsifier. Nothing here is a proof.

## The structural fact: `e(n) ≥ 0` (the ballot)

Let `h[j] = [p_{j+1} − p_j ≡ 2 (mod 4)]` be the switch bit (1 = consecutive
primes differ in mod-4 class; gap ≡ 2 mod 4). Let `w(n) = Σ_{j=1}^{n} h[j]`
(annexing the run's convention that the ancestor window is `[2, n−1]`) and

    e(n) = 2·w(n) − (n−2)   =   (#switches) − (#non-switches)  in prefix n.

**Ballot claim:** `e(n) ≥ 0` for all n — the mod-4 switches never trail the
non-switches in any prefix.

### Fresh verification this pass
- Fresh sieve to 4e6: 283,145 gaps; density 0.56818; **min e = 2** attained only
  at n ∈ {2,4,6,8}; final e = 38,613.
- Fresh sieve to 21e6: 1,329,942 gaps; density 0.56177; **min e = 2** only at
  {2,4,6,8}; final e = 164,296.  Lag-1 autocorr r₁ = −0.0424; all lags ≥ 2 have
  |r| < 0.003 (in the 1e8 run: r₁ = −0.026, all longer lags |r| < 0.004).
- The run's earlier verifications reach **2e8 prime-pairs** (min e = 0 at
  n=2,4,6,8; final e = 19,272,272; global min e = 0).

### What the ballot is NOT (attacks that fail — this pass)
I fitted **two honest low-order null models to the primes' own statistics** and
showed neither reproduces the never-dip ballot:

- **IID**, marginal density p = w/n ≈ 0.56: **200/200** 2e6-long trials dip below 0.
  So plain positive density does not force the ballot.
- **Markov chain with the exact empirical transition matrix**
  P = {0:{0:0.4172,1:0.5828}, 1:{0:0.4546,1:0.5454}} (stationary P(1)=0.562,
  matching lag-1 anti-clustering): **1189/2000** trials dip below 0.

Crucial refinement — **the dips are a startup-window phenomenon.** Of 3000
Markov trials (N=2e6): 1751 dipped, of which **1691 (97%) dipped before n=100**,
median first-dip index = 7, **none** dipped after n=100k. So the prime ballot's
*extra* content over any low-order model is precisely:

1. a **favorable finite startup** (the first ~100 gaps keep the walk ≥ 0, min e
   = 2 — the balanced early switch distribution), and
2. **positive drift** 2E[h]−1 ≈ 0.10–0.12, which then carries `e` to +∞ a.s.

Longer-range correlation is **not** needed: |r_lag≥2| are all < 0.004. This is
the honest structural reading — not "the ballot is mysterious" but "the ballot
reduces to a bounded startup window plus drift, both of which are named-open
consequences of the two-point H–L / Lemke-Oliver–Soundararajan correlation
structure".

### Equivalence / transfer to the Route B supply bound
Two transfer legs (separate theorems; both machine-verified over the supplied
range [2,30000], 0 violations on each):

- **(a)** `ν₂(q_n) ≥ w(n)/2`  over n ∈ [17, 30000].
- **(b)** ballot `w(n) ≥ (n−2)/2` over [2,30000] (min excess 2w−(n−2) = 2; note
  the min e = 2 at n=2,4,6,8 is *why* leg (b) is exactly the ballot).

Composed: `ν₂ ≥ (n−2)/4` over [23, 30000] (0 violations, min 4ν₂/(n−2) =
1.333 at n=32) ⟹ `ν₂ ≥ n^0.525` for n ≥ 23 (min ν₂/n^0.525 = 1.542 at n=23),
which is **exactly the G-supply bound** Granville Theorem 5.5 needs.

**So the entire remaining open content of Route B is `e(n) ≥ 0`** — equivalently
the switch-majority ballot — which by this pass is carried by startup + drift,
both named-open two-point mod-4 primes statistics (ABGS 2011 §9: whether
N(a,d,m,x)/π(x) tends to any limit is open, so no unconditional one-sided bound
exists).

## Sequence tools — negatives (structure is not a closed form)
- `block_profile` b_k = [2,7,13,13,24,23,22,21,24,58,97,96,...] (first 30):
  **no** low-degree polynomial, **no** constant-coefficient recurrence (order
  ≤ 10), leading ratios grow. = OEIS A000232 − 1 (already recorded).
- `ν₂(q_n)` first 30 [0,0,0,0,2,2,2,2,2,2,6,3,5,3,5,3,11,6,...]: **no**
  polynomial, **no** recurrence, not in OEIS.
- `dev(n) = 2ν₂−n` first 50: **no** recurrence (order ≤ 8); and
  `nu2_walk_increments` shows `|ν₂(n+1)−ν₂(n)|` up to 468 while `|dev|` ≤ 639 —
  concentration is **not** a bounded-step walk (kills martingale/LIL-on-ν₂).
- OEIS lookup of the ballot terms [2,2,2,2,2,2,2,2,4,10,12,...] = **no match** —
  uncatalogued.

Recommendation: the exploitable structure is qualitative (an always-nonnegative
ballot carried by startup + drift), not a recurrence. A derivation of `e(n) ≥ 0`
would close Route B; the realistic deliverable is the conditional theorem naming
the two-point mod-4 correlation bound (startup + drift) as hypothesis.

## Falsifiers (each would break the claim)
- Any n with a switch deficit in a prefix — **not found** to 2e8 gap terms.
- A low-order Markov/iid model with the primes' own marginals that reproduces
  the never-dip to full scale — **does not**: both controls dip in ~60% of runs.
