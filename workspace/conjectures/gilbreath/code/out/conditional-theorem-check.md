# Conditional-theorem assembly check — Route B

Verifies the arithmetic assembly of the conditional theorem:

> **IF** `nu2(q_n) >= c*n` for some fixed `c > 0` (the two-point mod-4
> correlation lower bound, a named open problem) **THEN** Gilbreath's
> conjecture holds.

Every leg is labelled **exact computation** or **sourced**; the open content is
named at the end. Verifier: `code/gap_analysis/conditional_routeB_check.py`,
capture `code/out/conditional_routeB_check.captured.txt` (EXIT_CODE=0).
`c = 0.4` throughout as a concrete instance; the structure is monotone in `c`.

## The chain, leg by leg

### Leg (a) — demand side `nu2 > n^beta`, `beta > 0.525` suffices — SOURCED

Granville Theorem 5.5 reduces GC to `nu2(q_{n-1}) > n^beta` with
`beta > alpha`, and the demand `alpha = 0.525` is unconditional by
Baker–Harman–Pintz 2001. Not recomputed here; held as sourced
(claim `bhp-demand-corollary-g-star`,
`research/notes/lemma54-re-derived-proof.md`). The honest form is
`alpha = 0.525 + delta` (BHP's 0.525 sits on the prime `p_n ~ n log n`, so on
`n` it is `0.525 + o(1)`), and `li2023-not-bottleneck` records that the exact
`alpha in {0.52,0.525}` is immaterial once the supply is linear: any affine
supply `nu2 >= c*n` beats `n^beta` for every `beta < 1`.

### Leg (b) — `c*n > n^0.525` eventually — EXACT COMPUTATION

`(c*n)/n^0.525 = c * n^0.475` is strictly increasing in `n`, so a single
threshold check, made exact in rational arithmetic (`(c*n)^40 > n^21`):

```
smallest n with c*n > n^0.525  :  n_0 = 7
```

`0.4*n > n^0.525` holds for every `n >= 7` (and the ratio only grows). So a
linear supply overtakes the `n^0.525` demand at a completely modest threshold
and never falls behind.

### Leg (c) — nu2 data, exact over 30,000 stored terms

Data: `code/out/nu2_dense.txt` (n=1..30000, sieve 1e6). Exact integer
comparisons (`nu2^40 > n^21`).

```
min nu2(n)/n        over [4000,30000] = 0.47452   (at n=4278)
min nu2(n)/n^0.525  over [4000,30000] = 24.95441  (at n=4020)
nu2(n) <= n^0.525 failures:  full range [1,30000] = 13,  [4000,30000] = 0
nu2(30000)=15029  vs  n^0.525(30000)=224.12
```

The 13 failures of `nu2(n) > n^0.525` over the **full** range are all in the
start-up region `n <= 16` (values 0,0,0,0,2,2,2,2,2,2,3,3,3 against thresholds
1.0..4.29); from `n = 17` onward the inequality holds on every term to 30000,
and on `[4000,30000]` the margin `nu2/n^0.525` is `>= 24.95` — a factor of
~25 over the theorem's actual pointwise threshold. This reproduces the two
board figures (`pattern_finder_nu2_report.md` §3–4).

### Leg (d) — Lemma 5.4 converts budget into success — PART EXACT / PART SOURCED

The lemma that turns the `nu2` supply into actual success is Lemma 5.4,
**proved on the even domain** by this run
(`lemma54-re-derived-proof`, parity-preserving descent; the δ=0 case Granville
discards is a normal closure case). Its budget inequality, with Link A
(`v <= g*_n` by `|a-b| <= max(a,b)`), is `g*_n <= 2*nu2 + 2`, where
`g*_n = max(g_2..g_n)` is the record first gap.

- **Exact:** `2*nu2(n)+2 >= g*_n` over `n=2..30000` (sieve 3e6):
  checked 29999 columns, **1 violation**, at `n=4` (`-2`), all later hold.
  Tightest slack after start-up: `2*nu2(30000)+2 - g*_30000 = 30060 - 86`.
  (The `n=4` dip is the same start-up region as in Leg (c).)
- **Sourced:** the demand `g*_n = O(p_n^0.525) = O(n^{0.525+eps})` is BHP
  2001. Since `g*_n/p_n^0.525 -> 0` (indeed `g*_n = O(n^{0.525+eps})` with
  `g*_n/n -> 0`), a **linear** supply `nu2 >= c*n` gives
  `2*nu2+2 = 2c*n+2`, which exceeds `g*_n` for every sufficiently large `n`
  automatically — no tuning of `c` or `beta` needed.

## What this check establishes (and does not)

Established (exact): the arithmetic assembly closes — a linear supply bound
overtakes the `n^0.525` demand at `n >= 7` (Leg b), is witnessed on
`[4000,30000]` with min ratio `0.4745` and min `nu2/n^0.525 = 24.95`
(Leg c), and the Lemma-5.4 budget `2*nu2+2 >= g*_n` holds on every column
from `n >= 5` (Leg d).

NOT established: the supply bound `nu2(q_n) >= c*n` itself. That is a
**two-point** statement about consecutive-prime mod-4 switches, hence
conjectural (needs Hardy–Littlewood / Lemke-Oliver-level control); the
library's `g-supply-two-point-crux-settled` shows no unconditional positive-
linear lower bound is derivable from PNT-in-AP / GRH / Dirichlet alone. So the
whole conditional theorem hangs on a single, named, open two-point
correlation bound — which is exactly the declared deliverable shape of Route B.

## provenance

- Verifier: `code/gap_analysis/conditional_routeB_check.py`, EXIT_CODE=0.
- Capture: `code/out/conditional_routeB_check.captured.txt`.
- Data: `code/out/nu2_dense.txt` (exact, sieve 1e6, 30,000 terms).
- Fresh sieve for Leg (d): `lib.gilbreath.primes_up_to(3_000_000)` (oracle
  reproduces the five worked rows of `problem.md`).
- Sourced: BHP 2001 (alpha=0.525), Granville Theorem 5.5,
  Lemma 5.4 (= `lemma54-re-derived-proof`, this run), Link A
  (`v <= g*_n`), `li2023-not-bottleneck`.
