# Pattern-finder: the mod-4 switch-walk ballot — a one-sided prefix structure

## The finding

Define the **mod-4 switch bit** of the k-th prime gap:

    bit_k = 1  iff  p_{k+1} != p_k (mod 4)   (i.e. p_{k+1}-p_k ≡ 2 (mod 4))
          = 0  otherwise

Let `w(n)` = number of switches among the gaps `g_3..g_n` (so the window has
`n-2` gaps), and define the **switch walk excess**

    e(n) = 2·w(n) − (n−2)  =  (# gaps ≡ 2 mod 4 among g_3..g_n) − (# other gaps).

**Ballot (conjecture, verified-numerically):** `e(n) ≥ 0` for every `n` — in
every prefix at least half of the first `n−2` prime gaps are ≡ 2 (mod 4); the
walk never dips below 0.

Verified pointwise on **three independent routes**:

| route | range | dips |
|---|---|---|
| naive fresh-sieve recompute | n ≤ 1e6 | 0 |
| exact triangle-convention recompute (run's window) | n ≤ 30000 | 0 |
| streaming sieve (bytearray) | n ≤ 5e7 primes (sieve to 1e9) | 0 |

Global min e = 1 at n=3; min e over the last half at 5e7 = +2,639,365. The
drift is steady and positive: min e/n over n≥T converges to ≈ 0.110 across
T, reached at the largest n — the marginal switch density stabilises near
0.555, giving e(n) ≈ 0.11·n.

## Why this is genuinely new and exploitable

- It is strictly **stronger** than an asymptotic density statement: it is a
  **pointwise prefix guarantee** (ballot/majority), not merely "density ~0.56".
- It is a **genuinely one-sided** statement on the *switch walk* — unlike the
  ν₂ fluctuation `2ν₂−n`, which the run recorded as oscillating (dev negative
  on 55.3% of n; that "no one-sided claim" refers to ν₂, a *different*
  statistic that depends on the whole absolute-difference triangle). The switch
  walk e(n) depends only on prime gaps mod 4 and never dips.
- Chebyshev-bias restatement: with `u_k = +1` if `p_k ≡ 1 (mod 4)`, `−1` if
  `p_k ≡ 3 (mod 4)`, the ballot is exactly
  `Σ_{k=2..n} u_k·u_{k+1} ≤ 0` for every prefix — a **negative lag-1
  autocorrelation of the residue-sign sequence in every prefix**.

## Role in Route B (the run's primary route)

The entire supply side of Route B reduces to this ballot:

    leg(a) transfer (verified, exact over n to 30000):  ν₂(n) ≥ w(n)/2
                                     (0 violations n≥17; exact contact n=44, min 0.5)
    leg(b) ballot (verified to 5e7): w(n) ≥ (n−2)/2  ⇔  e(n) ≥ 0
    composed:  ν₂(n) ≥ (n−2)/4  >  n^0.525  for n ≥ 23
               (min ν₂/n^0.525 = 1.542 at n=23, over n to 30000)

So a proof of the ballot (or even its weaker "positive density" form) would
close Route B's supply side. The transfer leg(a) is the deterministic part; the
ballot leg(b) is the load-bearing open prime-distribution statement.

## Status and what would falsify it

- **Conjectural.** The literature (ABGS 2011 §9, lau-2024) establishes that no
  *unconditional* positive-density lower bound on the consecutive-prime mod-4
  switch count exists; the count's asymptotic is a two-point
  Hardy–Littlewood / Lemke-Oliver–Soundararajan-level statement. So even this
  pointwise ballot has no available proof.
- First falsifier: the first `n` with `e(n) < 0`. **None found over 5e7 steps**;
  the positive drift (~0.11n) makes a dip appear unlikely, but that is not a
  proof.
- The ballot is NOT true for generic biased strings: a random Bernoulli(0.6)
  bit string violates it in 75/150 of the run's trials (capture
  `order_balance_test.captured.txt` / `prefix_closure_bigram.captured.txt`).
  The prime switch bits are non-iid in exactly the way that preserves
  prefix-majority — there is real number-theoretic content, consistent with
  the Chebyshev-bias / residue-anticorrelation literature.

## Bound on the claim

The composed Route-B bound is verified only to n=30000 (dense ν₂ data stops
there, and computing ν₂ for a row needs the whole triangle prefix — O(n²)).
The ballot leg alone extends to n=5e7. A fully extended Route-B bound would
need leg(a) at larger n, which is the expensive part.

## Files

- `code/pattern_finder/switch_walk_extend.py` — naive fresh-sieve recompute.
- `code/pattern_finder/switch_majority_stream.py` — streaming sieve (5e7).
- `code/pattern_finder/switch_walk_linear.py` — e/n drift.
- `code/pattern_finder/verify_supply_chain_runwindow.py` — full chain (run window).
- captures in `code/out/switch_walk_extend_*.txt`, `switch_majority_stream_5e7.captured.txt`,
  `switch_walk_linear_1e7.captured.txt`, `verify_supply_chain_runwindow.captured.txt`.
