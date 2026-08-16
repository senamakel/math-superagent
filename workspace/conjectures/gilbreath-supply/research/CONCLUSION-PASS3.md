# Third pass — conclusion (updated by pattern_finder: log-periodic decomposition confirmed)

The pass's head question, set in `GOAL.md`, is **answered**:

> Does the minimum weight ratio at which linear supply becomes typical tend to
> **0**, or plateau near **1/8**?

**It tends to 0.** The threshold weight is sublinear, and the arithmetic demand
reduces to a **sublinear switch count** — strictly weaker than pointwise mod-4
switch density. This is the workspace's first affirmative weakening across
three passes. It is **problem.md result type 4**, never type 1, and the
genericity caveat is unchanged: *typical is not this string*.

## UPDATE (pattern_finder, this run): the log-periodic decomposition is CONFIRMED

The prior write-up left the log-periodic correction "unconfirmed" and reported
only a fitted exponent `0.557 ± 0.002`. The pattern-finder then extended the
**exact** threshold computation (the mean half is a closed form, so per-n `w*`
is exact with no sampling) beyond `n=32768` to `n=65536`, and sampled the
non-power-of-two phases needed to test log-periodicity. Results, all exact per-n:

- **Not `c·√n`.** Phase-1.0 (powers of 2) OLS `E = 0.55499 ± 0.00202` over 9
  points (n=256..65536), `27σ` from `1/2`; and `w²/n` rises `0.77 → 1.74` (not
  flat). `1/2` is dead.
- **Not `c·n^{log₂3−1}`.** At `E=0.58496` the residual `w/n^E` **monotone-drifts**
  `0.624 → 0.531` (spread 0.093); at `E=0.555` it is bounded periodic (spread
  0.024). `log₂3 − 1 = 0.58496` is ruled out (14.8σ on the phase-1.0 fit).
- **Log-periodicity confirmed (the operator's directive-46 signature).**
  `w*(n)/n^0.555` is flat at each fixed in-cell phase `n/2^{⌊log₂n⌋}` across many
  doublings, with phase means differing by **amplitude ≈ 0.069**:
  - phase 1.00: `0.730–0.750` over 9 doublings (n=256..65536), mean 0.7383
  - phase 1.25: `~0.807` (n=5120..40960)
  - phase 1.50: `0.779–0.800` over 7 doublings (n=768..49152), mean 0.7893

  This is exactly the textbook Pascal-mod-2 counting-function form
  `n^E · G(log₂ n)` with `G` bounded and period-1 (OEIS A006046; the analogy is
  structural, not a matching of constants). So the honest description is:

  ```
  w*(n) = n^0.555 · P(log₂ n),  P bounded, period-1 in log₂ n, amplitude ≈ 0.07
  ```

  — the exponent `0.555` is genuine with a periodic correction, not a
  badly-fitted `5/9` or `4/7`.
- **Closed-form honesty (directive 47).** `5/9 = 0.55556` is *not* separated
  from the fitted `0.555` by the data: after removing the log-periodic trend,
  both give identical residual sd 0.01466 (log2 units) over n=256..65536, and the
  exponent gap between them (0.0044 log2 units) is ~30× smaller than the periodic
  swing. So `5/9` is a plausible candidate but not an established closed form;
  the established content is sublinear `E ≈ 0.555` with the log-periodic factor,
  with `1/2` and `log₂3−1` firmly ruled out.
- **Mechanism.** The continuous independent-bit approximation
  `P[XOR odd] ≈ (1−(1−2w/n)^k)/2` solves to `E → ~0.53` slowly; the exact
  exponent `0.555` is higher, so higher-order (correlation) terms matter, and
  the sublinearity `E < 1` is robust to the approximation.
- **Independence check.** A from-scratch linear scan over `w` (required because
  `mean_n(w)` is **non-monotone** by parity) reproduced all 16 known `w*`
  (n=8..32768) digit-for-digit.

## The column

`w*(n)` = least Hamming weight `w` with exact mean of `ν₂(h)/n` over weight-`w`
strings = `0.40`:

```
n      8   10  12  14  16  32   64   128  256  512  1024 2048 4096 8192 16384 32768 65536
w*     3    3   3   4   3   5    7   11   16   24   35   52   77  112  164   239   349
theta  0.375 0.30 0.25 0.286 0.188 0.156 0.109 0.086 0.0625 0.0469 0.0342 0.0254 0.0190 0.014 0.010 0.0073 0.0053
```

`theta = w*/n` falls monotonically **from n=14 onward** (it is not globally
monotone: 0.2500@12 rises to 0.2857@14). The 1/8 plateau at n=64,128 was a
coarse-grid sampling artifact (exact mean at n=64 is 0.1094, at 128 0.0859).

## What it reduces the arithmetic demand to

Linear supply is typical once the switch weight exceeds about `n^0.555`. Read
against the mod-4 statement (a *positive fraction*, i.e. `Θ(n)` switch pairs),
a sublinear switch count `~n^0.56` is strictly weaker.

## Honest bounds on the claim

- The per-n `w*` and `theta` are **exact** for each n in 8..65536 (closed-form
  mean, no sampling; independently reproduced by linear scan).
- The **limit** (tends to 0), the **exponent** (0.555) and the **log-periodic
  factor** (amplitude ~0.07) are **fitted** from the measured range n ≤ 65536 —
  supporting data, not a theorem. The range does not rule out an eventual
  plateau at a smaller positive constant, but decisively removes the concrete
  "plateaus at 1/8" hypothesis.
- The exponent is explicitly **not a closed form**; `1/2` is rejected at >25σ,
  `log₂3−1` at >14σ.
- One-sentence genericity gap: **typical is not this string** — being above the
  threshold does not prove the primes' particular `h` has linear supply.

## The two open lemmas (what a proof would need)

- **G-threshold-asymptotic-zero** — for every fixed θ ∈ (0,1/2), w = ⌊θn⌋, the
  biased-cell sum `(1/n)Σ_{d=2}^{n−1} K_w(2^popcount(d); n)/C(n,w) → 0`, so
  E[ν₂/n] → 1/2 at every fixed θ and θ_mean(n) → 0. Engine: hypergeometric mode
  bound `|E[(-1)^X]| ≤ max_j P[X=j] = O(1/√(1+Var X))`.
- **G-threshold-concentration** — Var(ν₂(n)) = o(n²) at every fixed θ, so
  ν₂/n → 1/2 in probability and the fraction criterion holds in the limit.

## Claim blocks (fenced — these reach research/CLAIMS.md)

The pass's results below were filed only in prose. Fenced claim blocks are what
the ledger reads, so they are recorded here. Status discipline is unchanged:
the per-n `w*` values are EXACT (closed-form mean, no sampling), the exponent,
the log-periodic amplitude, and the limit are FITTED/OPEN, and nothing here is
a proof of SUPPLY for the primes.

```claim
id: threshold-weight-sublinear
statement: >
  The exact-mean linear-supply threshold weight
  w*(n) = min{ w : E_{S_w}[nu2/n] >= 0.40 } over all weight-w strings in F2^n
  (the exact Krawtchouk sphere-mean, no sampling) grows sublinearly:
  w*(n) = n^E . P(log2 n) with a FITTED exponent E ~ 0.555 (phase-1.0 OLS
  E = 0.55499 +/- 0.00202 over n = 256..65536) and P a bounded, period-1-in-
  log2(n) log-periodic factor of amplitude ~ 0.07. Equivalently the threshold
  ratio theta = w*/n -> 0: linear supply (E[nu2/n] >= 0.40) is TYPICAL once
  the switch count exceeds about n^0.56 — a SUBLINEAR switch count, strictly
  weaker than a positive mod-4 switch density (Theta(n)). Per-n w* is exact
  over n = 8..262144
  (3,3,3,4,3,5,7,11,16,24,35,52,77,112,164,239,349,507,738 across
  n = 8..2^18; theta = 0.375@8 .. 0.0028@2^18), independently reproduced
  digit-for-digit by a from-scratch linear scan (required because mean_n(w) is
  NON-MONOTONE in w by parity).
hypotheses: canonical floored fold d in [2,n-1]; exact mean over the weight-w
  sphere via the Krawtchouk parity formula P_d(w) = (C(n,w) - [z^w](1-z)^k
  (1+z)^(n-k))/(2 C(n,w)), k = 2^popcount(d); n in [8,262144].
holds-here: yes for the fold's generic behaviour; NOT for the primes' own h
  (genericity gap 'typical is not this string', threshold-typical-is-not-this-string)
status: measured-not-proved (per-n w* EXACT; exponent 0.555 and log-periodic
  amplitude ~0.07 FITTED over n <= 65536; limit theta -> 0 supported at every
  measured n >= 64, not a proof)
bearing: >
  Third pass's affirmative headline and the workspace's first affirmative
  weakening across three passes. It prices the weakest arithmetic input for
  the generic statement: a sublinear switch count ~ n^0.56 suffices for linear
  supply to be typical — problem.md result type 4, never type 1. It does NOT
  prove SUPPLY for the primes (typical is not this string). Passage to a proof
  needs the two open lemmas G-threshold-asymptotic-zero and
  G-threshold-concentration. WHO: nobody re-derives the w* column (exact) or
  re-runs the log-periodic test — both closed on disk.
follows-from: threshold-mean-exact-parity-formula,
  hjt-p2-log-periodic-representation-proved
contradicts: none — supersedes the pass-2 'plateau near 1/8' reading (a
  300-sample/coarse-grid artifact)
anchor: research/CONCLUSION-PASS3.md; code/out/threshold_weight_logperiodic_extended.txt;
  code/pattern_finder/threshold_linearscan.py, log_periodicity_extend.py,
  phase1_exponent.py
```

```claim
id: threshold-closed-forms-rejected
statement: >
  Among candidate closed forms for the threshold exponent E of w*(n) ~ n^E . P(log2 n),
  the data (exact per-n, n = 8..262144; phase-1.0 OLS over n = 256..65536):
  (i) E = 1/2 (w = c.sqrt n) is REJECTED: on the phase-1.0 fit E = 0.55499 +/-
  0.00202 puts 1/2 about 27 sigma away, and w^2/n RISES 0.77 -> 1.74 over
  n = 256..65536 (NOT flat), so sqrt-growth is dead;
  (ii) E = log2(3) - 1 = 0.58496 is REJECTED at ~14.8 sigma (phase-1.0): the
  residual w/n^E monotone-drifts 0.624 -> 0.531 (spread 0.093) across doublings,
  vs a bounded-periodic residual of spread 0.024 at E = 0.555;
  (iii) E = 5/9 = 0.5556 is NOT separable from the fitted 0.555: after removing
  the log-periodic trend both give IDENTICAL residual sd 0.01466 (log2 units,
  n = 256..65536) and the exponent gap (0.0044 log2 units) is ~30x smaller than
  the periodic swing — so 5/9 is a plausible candidate but NOT an established
  closed form.
hypotheses: canonical floored fold; exact-mean w* over n = 8..262144; phase-1.0
  (powers-of-2) OLS fit of log2 w* vs log2 n over n in [256,65536]; log-periodic
  detrending via fixed in-cell phase n/2^{floor(log2 n)}.
holds-here: yes (these are the pass's own exact computations; the rejection
  sigmas are from the fitted log2-w* regression)
status: measured-not-proved (the w* values and residual sd are EXACT/FITTED over
  the measured range; the sigmas quantify the fit, not a theorem about the limit)
bearing: >
  Records what the data CANNOT support, so a later reader does not adopt 5/9
  (or 1/2, or log2 3 - 1) because it is tidy. The established content is
  sublinear E ~ 0.555 with the log-periodic factor; 5/9 is a candidate closed
  form the range cannot separate. WHO: nobody re-rejects these forms; the
  discrimination is closed on disk.
follows-from: threshold-weight-sublinear
anchor: code/out/threshold_weight_logperiodic_extended.txt;
  code/pattern_finder/phase1_exponent.py, directive47_compare.py
```

```claim
id: G-threshold-asymptotic-zero
statement: >
  (OPEN LEMMA — the gap from the measurement to a theorem.) For every fixed
  theta in (0,1/2) and w = floor(theta n), the biased-cell sum is sublinear:
  (1/n) sum_{d=2}^{n-1} K_w(2^popcount(d); n)/C(n,w) -> 0 as n -> oo.
  Consequently E[nu2(n)/n] -> 1/2 at every fixed theta > 0, so the mean-
  crossing threshold theta_mean(n) = min{w/n : M(n,w) >= 0.40} -> 0. Engine
  (to be proved): group depths by popcount; the hypergeometric parity-mode
  bound |E[(-1)^X]| <= max_j P[X=j] = O(1/sqrt(1 + Var X)) for
  X ~ Hypergeometric(n, m, w), summed over the C(floor(log2 n), k) cells of
  popcount k; worst group k ~ (log2 n)/2 contributes o(n).
hypotheses: X ~ Hypergeometric(n,m,w) (w ones among n, m = 2^popcount(d) read
  positions of a fold cell); floored fold d in [2,n-1]; fixed threshold c = 0.40.
holds-here: yes — PURE F2/hypergeometric, NO primes, NO number theory (checked
  file-backed in research/backward/supply-threshold-limit.md)
status: open (unproved) — the measured/verified content (w* exact, theta ->
  0 supported) is not a proof of the limit
bearing: >
  Closing it (with G-threshold-concentration) promotes the measured tends-to-0
  to a proof that the linear-supply typical threshold tends to 0 — the strongest
  affirmative statement the workspace can reach. Most tractable open item: a
  self-provable hypergeometric log-concavity/local-limit bound, no new source.
  Does NOT prove SUPPLY for the primes (typical is not this string).
follows-from: threshold-mean-exact-parity-formula, threshold-weight-sublinear
answers: threshold-limit-hinges-on-hypergeometric-mode-bound (closes the mode-bound
  gap if proved, but today OWNS it as the named open step)
anchor: research/backward/supply-threshold-limit.md; research/notes/threshold_limit_open_lemma.md
```

```claim
id: G-threshold-concentration
statement: >
  (OPEN LEMMA — the gap from the measurement to a theorem.) For every fixed
  theta in (0,1/2) and w = floor(theta n), Var(nu2(n)) = o(n^2). Hence
  nu2(n)/n -> 1/2 in probability, so the fraction criterion
  P[nu2/n >= 0.40] -> 1 holds in the limit and the combined 'typical'
  threshold (mean AND fraction) tends to 0. Engine (to be proved): the second
  moment over symmetric-difference sizes, using the downset-row-intersection
  measure |M_d \triangle M_{d'}| = 2^{pc(d)} + 2^{pc(d')} - 2^{pc(d ^ d') + 1}
  and the Krawtchouk evaluation of E[(-1)^{T(n,d)+T(n,d')}].
hypotheses: X ~ Hypergeometric as in G-threshold-asymptotic-zero; floored fold;
  fixed threshold c = 0.40.
holds-here: yes — PURE F2/hypergeometric, NO primes, NO number theory
status: open (unproved) — measured/verified content is not a proof of the limit
bearing: >
  Together with G-threshold-asymptotic-zero, converts the measured fraction
  criterion into a theorem (theta -> 0 for the combined threshold). Same
  hypergeometric mode-bound engine; closing it is the natural next attack.
  Does NOT prove SUPPLY for the primes.
follows-from: threshold-mean-exact-parity-formula, threshold-weight-sublinear,
  downset-row-intersection-meet-formula
anchor: research/backward/supply-threshold-limit.md; research/notes/threshold_limit_open_lemma.md
```

## Captures

- `code/out/threshold_weight_logperiodic_extended.txt` (the decisive capture, n≤65536)
- `code/out/linear_supply_threshold_pass3.txt`, `code/out/threshold_exact_mean_independent.txt`
- `code/out/threshold_limit_exact.txt`, `code/out/threshold_exponent_fit_pass3.txt`
- `code/pattern_finder/threshold_linearscan.py` (independent exact reproduction)
- `code/pattern_finder/log_periodicity_extend.py`, `log_periodic_quantify.py`,
  `phase1_exponent.py`, `directive47_compare.py`, `mechanism_E.py`

No further lines are opened after this write-up; the fenced claim blocks in this file are the pass's last addition (directive 49) — ids mirrored in research/ROOT.md, summary posted to the board.
