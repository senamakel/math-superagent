# Pattern-finder report: a linear supply bound for Route B (Granville ν₂)

The open content of the primary route (GOAL.md Gaps) is the **supply side**:
Granville's Theorem 5.5 reduces Gilbreath's conjecture to
`ν₂(q_n) > n^β, β > 0.525`. Everything I report here is **verified
numerically** — exact over the terms supplied — and is a **conjecture**,
not a proof. The two legs are stated separately, because they fail or survive
independently and their confidence differs.

## The two quantities

- `ν₂(n)` — count of `2`s in the maximal `{0,2}` suffix of the prime right
  diagonal through `q_n` (data: `code/out/nu2_dense.txt`, exact to n=30000;
  plus sampled ν₂ to n=100000 from `nu2_incremental_1e5.txt`).
- `w(n)` — Hamming weight of the mod-4 switch bits
  `[p_{j+1} ≢ p_j (mod 4)]` for `j ∈ {2..n-1}` — i.e. `gap ≡ 2 (mod 4)`
  (`w` computed this run from a fresh sieve, both ranges).

## The two exact facts

**Leg (a) — transfer, ν₂ ≥ w/2.** For every `n ∈ [17, 30000]`,
`ν₂(n) ≥ w(n)/2`, with exact bare contact at `n=44` (ν₂=w/2 there). Also at
the 13 sampled ν₂ points up to `n=100000` the ratio `ν₂/w` is `≥0.667`,
and `≥0.75` for `n ≥ 100` (only isolated dip below 0.8 is `n=1005` at 0.748,
neighbours ≥0.79). Exact over the supplied data; **a conjecture** beyond.
This is the deterministic transfer the board's `chebyshev-bias-granville-nu2-supply`
candidate is built on. It is not the hard part.

**Leg (b) — density, w ≥ c·n for positive c.** `min_{n≥31} w(n)/n = 0.5484`
(at `n=31`); over `n≥100` it is `≥0.5733`; the empirical marginal switch
density stabilises near 0.56–0.59 (e.g. `w(30000)/30000 = 0.5798`,
`w(100000)/100000 = 0.5736`). So `w(n) ≥ 0.5484·n` for all `n ≥ 31` — a
**positive-density** statement on the consecutive-prime mod-4 switch rate.
Exact over the range; **the genuinely open prime-distribution statement**.

## The composed linear bound

Composing the two legs:

> **`ν₂(n) ≥ 0.2742 · n` for all `n ≥ 31`**  (verified: 0 violations).

Since Granville's threshold is only `n^0.525`, and `0.2742·n > n^0.525` for
every `n ≥ 16` (crossover ≈ 15.2), this bound clears the theorem by a margin
`min_{n≥31} ν₂/n^0.525 = 1.621` (at n=32). So **a single positive-density
lower bound on the mod-4 switch rate `w` would close the supply side of Route
B** — `ν₂/n` need not even tend to any constant, only stay above `c·n` for
some `c>0`.

## What is conjecture vs. what is checked

- Leg (a) is a clean deterministic transfer — but only verified over 2..30000
  (tight at n=44) and at 1e5 samples; not proved for all n.
- Leg (b) is the load-bearing open claim: it needs the consecutive-prime
  mod-4 switch density to have a positive lower limit — a two-point
  Hardy–Littlewood / Lemke-Oliver / Lemke-Oliver–Soundararajan-level
  statement. Verified 0.5484 over 31..1e5; conjectured beyond.
- That w(n) ≥ c·n uncatalogued (OEIS lookup returns only unrelated entries:
  A283371, A116579).

## Recommendation

Do not attack raw ν₂ — it has no low-order structure (find_linear_recurrence
and analyze_sequence find nothing on its first 20 terms; OEIS miss recorded).
Attack **leg (b)**: a proved positive lower density for the consecutive-prime
mod-4 switch rate. That is named territory (Hardy–Littlewood / GRH in AP +
Lemke-Oliver bias), and it converts directly into the linear supply bound via
the exact transfer leg (a).

## Provenance / verification

- `code/out/pattern_finder_verify_nu2_transfer.py` — reproduces every claimed
  number (min ν₂/w, fluctuation, beta-check, margin) from nu2_dense.txt.
- `code/out/pattern_finder_compose_linear.py` — composes the legs; 0 violations.
- `code/out/pattern_finder_attack_transfer.py` — the n=1005 dip is isolated;
  min (ν₂ − w/2) = 0.000 at n=44 (bare contact, the weakest point).
- `code/out/pattern_finder_w_density.py` — w lower density to 3e4.
- `code/out/pattern_finder_scale100k.py`, `pattern_finder_sampled_legA.py` —
  both legs survive to n=1e5 (dense w; sampled ν₂).
All exact integer arithmetic.
