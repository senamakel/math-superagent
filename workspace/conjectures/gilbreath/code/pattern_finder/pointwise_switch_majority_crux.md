# The Route B crux as a clean ballot: pointwise mod-4 switch majority

Pattern-finder consolidation. Read the on-disk captures, pulled the sequences,
ran the sequence tools, and independently re-computed the load-bearing one.

## What the whole open supply side compresses to

Route B's entire surviving open content is the **G-supply** statement
`ν₂(q_n) ≥ c·n` (measured nu2/n ≈ 0.5). The run has established that this
reduces (two legs, both checked on the primes) to a *single clean pointwise
statement*:

    e(n) := 2·w(n) − (n−2) = 2·R(n) − n ≥ 0   for every n

where, with 1-indexed primes `p_1=2, p_2=3, ...`:

- `gap_k = p_{k+1} − p_k`
- switch bit `h_k = (gap_k//2) % 2 == 1  ⟺ gap_k ≡ 2 (mod 4)`, for k ≥ 2
- `w(n) = Σ_{k=3}^{n} h_k`   (Hamming weight of switches over gaps 3..n)
- `R(n)` = number of maximal equal-residue runs among primes `p_3..p_{n+1}`
- identity `e(n) = 2·R(n) − n` (both checked exact, incl. `e = −Σ u_ku_{k+1}`)

`e(n) ≥ 0` ⇔ `R(n) ≥ n/2` ⇔ **mean equal-residue run length ≤ 2 in every
prefix** — i.e. the consecutive-prime mod-4 sequence is a ballot path that
never lets the non-switch pairs crowd out the switches. This is literally the
"prime ballot": the ±1 walk `e(n)` (up on a switch, down on a non-switch) stays
non-negative.

## Sequence tools results

- **Block profile** (rows 1..40): growing via roughly-doubling bursts
  (2,7,13,13,24,...,739,873,...,2770,2769). `analyze_sequence`: no low-degree
  polynomial; `find_linear_recurrence` (order ≤8): **none**.
- **nu2 first 100**: no polynomial, no low-order linear recurrence.
- **`e(n)` first 512**: a ±1 ballot path (steps exactly in {−1,1}); no constant
  coefficient recurrence (it is a data-dependent walk, as expected).
- **Giant gaps** (14 terms, max 64): no polynomial/recurrence of note (too few
  terms; not a structural target).

So the structural regularity of the run is not in any single low-order
recurrence — it is the **pointwise non-negativity of the mod-4 ballot `e(n)`**,
which the sequence tools describe as "residue periodicity/growth" but which is
really a one-sided walk bound.

## Independent re-verification (this cycle)

`code/pattern_finder/pf_ballot_recheck_mine.py`, sieve 3e8 (16,252,325 primes):

    window N = 16,252,323
    e(n) >= 0 for n in [2, 16252323]: YES
    min e = 0 at {4, 6, 8};  first e<0: NONE
    suffix minima:  n=100:24, 1e3:235, 1e4:1722, 1e5:14718, 1e6:125145
    identity e(n) = 2R(n) - n over k in [2,200000]: OK
    mean residue-run length 1.806 < 2, longest run 19, 54% runs length 1

This matches the run's own stream captures (5e7, 1e8, 2.23e9 / `switch_walk_extend_1e8`:
min e over n≥1000000 = 125147 at n=1000062; to 1e8 the pointwise bound holds).

## The chain that makes this THE crux

- leg (b): `e(n) ≥ 0` ⟹ `w(n) ≥ (n−2)/2`.
- leg (a): `nu2(n) ≥ w(n)/2` — holds on the primes (measured min ratio 0.5152,
  dense scan). **Not proved**, and the universal (any-2-then-odds) form is
  REFUTED (`g-supply-transfer-universal-refuted`, kernel = span(11..1)).
- composed: `nu2(n) ≥ (n−2)/4`, which exceeds `n^0.525` for all n ≥ 23
  (and `n^0.6` for n ≥ 37). So the whole supply side collapses to:

> **Conjecture (the one open step of Route B):** `e(n) ≥ 0` for all n — the
> mod-4 consecutive-prime switch walk stays non-negative.

Falsifier: the first `n` with `e(n) < 0`. None exists to n = 16,252,323.

## Status

- **Verified-numerically** (this cycle and earlier stream captures, exact
  integer arithmetic, depth to 1.6e7): `e(n) ≥ 0`.
- **NOT a proof.** It is a two-point consecutive-prime mod-4 statement; ABGS
  2011 §9 shows the two-point mod-4 asymptotics are OPEN, so no unconditional
  linear bound exists in the literature. The honest frame stays a CONDITIONAL
  theorem at Hardy–Littlewood / Lemke Oliver–Soundararajan level: if the
  mod-4 switch walk stays non-negative (which the primes do to 1.6e7), then
  G-supply, hence the Gilbreath second-entry claim, holds.
- Recorded in Cognee (`remember_memory`): "entire supply side = pointwise mod-4
  switch majority".

## Files
- `code/pattern_finder/pf_ballot_recheck_mine.py` (this cycle, independent)
- `code/out/pf_ballot_recheck_mine.captured.txt`
- existing stream captures: `switch_majority_stream_{5e7,1e8,2e8}.captured.txt`,
  `switch_walk_extend_1e8.captured.txt`, `mod4_ballot_autocorr.captured.txt`
