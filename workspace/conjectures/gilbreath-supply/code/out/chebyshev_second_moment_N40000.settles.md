# What the N=40000 second-moment capture settles

**Capture file** `code/out/chebyshev_second_moment_N40000.txt` is populated
and is this run's capture at the stated ceiling `N=40000`. An earlier version
of this note claimed the file "was found on disk at 0 bytes"; that is
**incorrect** (directive 14): the operator read the populated file before this
run. The `mu=0.064146` that was read beside the primes is the **Thue-Morse
negative-control** value at its own `N=4000` ceiling — the file's third
section, which must fail density-1 and does (dip density ~0.99). It is not
contamination of the primes table; the primes section is `mu_N=0.499658` at
`N=40000`. The discrepancy is recorded, not chased.

## Method
Streamed `n = 2..40000` one row at a time — never materialising an `O(n²)`
triangle. Each `nu2(n)` from `lib.supply_fold.s_sos` (verified
`O(n log n)` submask-product fold), cross-checked against the literal
submask-XOR oracle `s_direct` on `n=4..200` and spots 53,64,100. All arithmetic
exact (ints/Fractions); every printed float is a ratio. STAGE1 computed nu2 in
parallel (126s), STAGE2 reduced exact statistics single-threaded (18.5s), total
~149s.

## The operative object — PRIMES at N=40000
- Mean `mu_N = (1/N)Σ_{n≤N} ν₂(n)/n` rises to **0.499658** at N=40000
  (from 0.4394 at N=100), settling onto ~1/2, matching the fair-model
  `Binomial(n−2,1/2)` prediction (mean `(n−2)/2`).
- **Tail dip sparsity** — the measured density-1 statement:
  - over `[30000,40000]` (the last quarter): **every n has ν₂(n)/n ≥ 0.49**,
    min over the tail = `0.490114`; zero dips below 0.45, 0.48.
  - over the full range `[50,40000]`: only 1 n with `ν₂/n < 0.35`, 3 below
    0.40, 10 below 0.42, 51 below 0.45 — densities all < 0.0013.
  - `min of ν₂(n)/n over [30000,N] = 0.490` and **rising** with N
    (0.3396@50 → 0.4599@1000 → 0.4850@10000 → 0.4901@30000).
- **Exact variance** `s2_N = Var(ν₂/n over n≤N)`:
  `0.000783`@4000 → `0.0000934`@40000, decaying ~1/N, std `0.0097`@40000.
- **Chebyshev quantitative lower bound** (exact arithmetic, a *measurement*,
  not a proof): at N=40000, `mu=0.4997`, `s2=0.0000934`,
  - eps=0.10 → `#{n : ν₂/n < 0.40} ≤ 0.0093·N` (≥99% of n≤40000 have
    ν₂(n)/n ≥ 0.40);
  - eps=0.15 → `≤ 0.0041·N` (≥99.6% have ν₂(n)/n ≥ 0.35).
  The Chebyshev bound needs the variance-vanishing input `s2_N→0` to give
  density-1; here it is measured decaying ~1/N.

## Negative controls (both behave as required)
- **ALL-ONES** (kernel vector): M(N)=0, s2=0, 100% of n below every threshold —
  vacuous control, confirms the pipeline does not fake positive signal.
- **THUE-MORSE** (must FAIL density-1): M(1000)=0.108 falling, monotonicity
  violations density 0.828, ~99.3% of n below 0.30 — the closing-door witness
  that a complicated/dense input can still collapse. It fails here exactly as
  required, separating the primes from the structured witnesses.

## Fair-model ratio (DROPPED as a test — directive 14)
`s2_N / (1/(4N))` sits at ~12.5→14.9 across N=4000..40000, i.e. the empirical
prefix variance of `ν₂/n` does not equal the single-index fair-model variance
`1/(4n)` — the two are different objects (a per-`n` variance vs a prefix
statistic), so this ratio is not the decisive null test it was framed as.
Directive 14 drops the test. What *is* the operative statement is the measured
tail density-1 signal above, and the sharper pointwise tail-min signal below.

## Status
**Measured, not proved** (GOAL rule: a measurement is evidence, not progress).
What the capture establishes: at the 40000 ceiling the primes show a
*quantitatively strong density-1 tail signal* — the last quarter is entirely
≥ 0.49, and Chebyshev gives ≥99% of n≤40000 at ν₂/n ≥ 0.40. This is the
strongest averaged-form measurement on record for this run and is the natural
numeric anchor for the density-1 theorem (GOAL priority 1). The variance s2_N
is measured decaying ~1/N, the input Chebyshev needs; a *proof* that s2_N→0
for the primes is left open.

## The sharper pointwise statement (directive 14)
The tail min `min ν₂/n over [X,N]` is **rising with X**: 0.3396@50 →
0.4599@1000 → 0.4850@10000 → 0.4901@30000. That is stronger than density-1:
it is measured evidence for `ν₂(n)/n → 1/2` **pointwise**, with no exceptional
set at all in the computed tail. The sharpest open problem this reduces to is
therefore: **prove `s2_N → 0`** (variance vanishes; the weaker sufficient input
for SUPPLY, yielding the density-1/averaged form via Chebyshev), **or prove the
exceptional set is finite** (the stronger pointwise statement, essentially
SUPPLY at c = 1/2). The former does not imply the latter — bounded mean +
vanishing variance give density-1, not finiteness.

```claim
id: n40000-second-moment-density1-measured
statement: >
  For the prime gap-parity h and the floored fold oracle nu2(n)=#{d in [2,n-1]:
  T(n,d)=1}, computed at ceiling N=40000: mu_N = (1/N) sum_{n<=N} nu2(n)/n =
  0.499658 at N=40000; over [30000,40000] every n has nu2(n)/n >= 0.49 with
  min 0.490114 and zero dips below 0.45; over [50,40000] only 1 n below 0.35,
  3 below 0.40, 10 below 0.42, 51 below 0.45, all densities < 0.0013; the
  prefix variance s2_N decays 0.000783 at N=4000 to 0.0000934 at N=40000. The
  tail min of nu2/n over [X,N] is RISING with X: 0.3396@50, 0.4599@1000,
  0.4850@10000, 0.4901@30000.
hypotheses: >
  ceiling N=40000; oracle lib.supply_fold.s_sos (floored, d in [2,n-1]),
  cross-checked s_sos == s_direct on n=4..200 and spots 53,64,100; sequence is
  the primes (h[j] = ((q_{j+1}-q_j)/2) mod 2). Exact ints/Fractions; printed
  floats are ratios. Negative controls: all-ones (M=0, vacuous), Thue-Morse
  (fails density-1, ~99.3% of n below 0.30).
holds-here: yes
status: measured-not-proved
bearing: >
  Evidence for c = 1/2, not an argument for it. The rising tail min is evidence
  for POINTWISE nu2/n -> 1/2 with no exceptional set in the computed tail; the
  sharpest open problem is to prove s2_N -> 0 (weaker: density-1 form) or that
  the exceptional set is finite (stronger: pointwise).
anchor: code/out/chebyshev_second_moment_N40000.txt
```
