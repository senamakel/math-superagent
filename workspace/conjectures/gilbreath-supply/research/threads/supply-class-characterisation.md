# Which h have linear supply — the weight threshold where it becomes typical

Directive 38 names this as the productive next step of the second pass: the
fold's supply class, characterised by Hamming weight. One extreme point is
pinned (h = e_{n-2}: switch density 0, linear supply via the odd-depth
mechanism). The question is where the class's bulk begins.

**HEAD QUESTION RESOLVED (third pass, on disk).** The threshold ratio does
NOT plateau near 1/8. The exact-mean half (Krawtchouk closed form, no
sampling) falls monotonically from n=14 onward; extended independently to
n=32768 (0.007294, capture `code/out/threshold_exact_mean_independent.txt`,
both cross-checks PASS). The pass-2 `0.125,0.125` at n=64,128 was a
300-sample + coarse-grid artifact. Read in ABSOLUTE weight, the threshold
weight w(n) grows SUBLINEARLY — "linear supply is typical once the switch
count exceeds about w(n)", strictly weaker than positive mod-4 switch density.

**The log-periodic test is CLOSED (directive 45/46/47, on disk, claim `wstar-log-periodic-n055-confirmed-measured`).** Extended to n=65536 (exact per-n), the threshold weight has the CONFIRMED log-periodic form `w*(n) = n^0.555 · P(log2 n)` with P a bounded period-1-in-log2 factor of amplitude ~0.07 (phase-1.0 OLS E = 0.55499±0.00202; phase means 0.7383/0.807/0.7893, flat at each fixed in-cell phase across 9 doublings). 1/2 rejected >25σ, log2 3 − 1 = 0.58496 rejected >14σ, 5/9 not separable from 0.555 (do not declare it). Per-n w* exact, independently reproduced by a linear scan (mean_n(w) is non-monotone in w). The pass-3 write-up CONCLUSION-PASS3.md and the deliverable file record it; the claim block is filed at research/notes/scholar_logperiodic_wstar_claim.md. The two tasks that closed the pass — (a) log-periodic-oscillation-test-d47 and (b) write-pass3-conclusion-d47 — are DONE; do not re-run the test or re-derive the threshold column.

**The exponent is settled as FITTED, not a closed form (directive 47).**
Directive 45's fitted `n^0.55` was too high, and directive 46's 1/2 reading was
wrong. The fit over n≥256 gives E = 0.55678 with se = 0.00225 — 1/2 is more
than twenty-five standard errors away. The per-doubling slopes
0.5406,0.5850,0.5443,0.5712,0.5663,0.5406,0.5502,0.5433 oscillate about 0.556,
not drift. Record the exponent as 0.557 ± 0.002, no closed form. The
oscillation's candidate explanation is log-periodicity: Pascal-mod-2 counting
functions classically carry a leading term n^E times a bounded function
periodic in log2(n), and alternating high-low slopes across consecutive
doublings are that signature. Test it directly: tabulate w*(n)/n^0.5568
against log2(n) and report a period-1 oscillation and its amplitude if present
(task `log-periodic-oscillation-test-d47`) — a described phenomenon, exponent
genuinely 0.557 with a periodic correction rather than a badly-fitted 5/9 or
4/7. **Directive 48 sharpens that test into a two-horse race, because the
local slopes carry the natural Pascal constant inside their own range:** the
n=256→512 doubling gave 0.5850 = log₂3 − 1 to four decimals. A straight
log-log fit over a ~7-doubling window is *biased* when a log-periodic
correction is present — the oscillation pulls the fitted slope off the true
exponent — so 0.5568±0.0023 may be "exponent plus window artifact", not the
exponent. The canonical Pascal-mod-2 counting function A006046
(`a(2k)=3a(k)`, `a(2^n)=3^n`) carries exponent log₂3 = 1.58496 exactly, so
the natural candidate for the threshold exponent is log₂3 − 1 = 0.58496, which
sits inside the measured local-slope span. The deciding computation now
tabulates **both** `w*(n)/n^0.5568` and `w*(n)/n^0.58496` against log₂(n) side
by side, with residual ranges, and reports which residual is the bounded
periodic one with no trend. The falsifier for the analogy is unchanged — a
monotone trend rather than a bounded oscillation. Do not declare log₂3−1
because it is prettier: it has to beat 0.5568 on the residual, and if neither
residual is flat the fitted 0.557 stands.
The pass conclusion (task `write-pass3-conclusion-d47`) then writes up
theta→0, threshold weight sublinear at n^0.557, demand strictly weaker than
switch density, claim block n=8..32768 measured-not-proved, open lemmas
G-threshold-asymptotic-zero and G-threshold-concentration, genericity caveat
"typical is not this string".

**Caveats.** (1) The exact-mean half is rigorous (`threshold-mean-exact-parity-formula`),
the fraction half is sampled (S=4000-8000, measured n<=4096). (2) "tends to 0" is
the data-supported inference over every measured n>=64; the limit is not a proof.
(3) Genericity gap unchanged: "typical is not this string" — being above the
threshold does not prove the primes' h has linear supply. The gain is the SIZE
of the arithmetic input demanded: sublinear switch count, not full switch density.

```thread
id: supply-class-characterisation
question: Which binary strings h have linear supply nu2(h)/n bounded below by
  c > 0 for all large n? With one extreme point known (per-window h = e_{n-2}:
  switch density 1/n -> 0, nu2(n) = ceil((n-2)/2) ~ n/2), what is the minimum
  weight w at which linear supply becomes typical rather than exceptional among
  weight-w strings? If linear supply is generic even at very low weight, the
  arithmetic input the primes need is correspondingly weak — and naming how
  weak is the deliverable this pass exists to produce.
status: live (head question SETTLED as measured-not-proved on disk; the
  pass-2 'plateau near 1/8' and CONCLUSION-PASS2.md §2 'not settled' framing
  is SUPERSEDED by the third-pass exact capture — see next line)
rests-on: enminus2-linear-supply-switch-density-not-necessary,
  fixed-single-1-fold-weight-bounded-by-j,
  single-boundary-one-refutes-switch-equivalence-as-stated,
  threshold-mean-exact-parity-formula,
  threshold-weight-sublinear-n055-measured
blocked-by:
next: The exact-mean threshold theta_mean(n)/n is a PROVED (exact, exhaustive-
  verified) value per n and falls strictly with n (0.019@4096, extended to
  0.0028@2^18); the limit tends-to-0 is the data-supported inference over every
  measured n >= 64, not a proof. Three tasks close the residual:
  (1) R-threshold-n512/extension and a HIGH-SAMPLE re-run of the fraction at
  n=64,128 (raise 300 -> >=1000) to confirm the 0.125 readings were a
  sampling artifact and bank the crossing (tool_builder);
  (2) R-threshold-limit: prove theta_mean(n)/n -> 0 by the popcount-group
  argument (G-threshold-asymptotic-zero: sum over popcount-k cells of the
  cell-parity is o(n) for fixed theta; the one open lemma is the log-concavity
  bound G-threshold-parity-control) and the concentration o(n^2) (G-threshold-
  concentration), which together are a pure F2/hypergeometric theorem NO primes;
  (3) threshold-sublinear-demand-claim-block: post the claim that the demand is
  sublinear switch count (strictly weaker than switch density), one-sentence gap
  'typical is not this string'.
  The absolute-threshold-weight exponent is SETTLED as FITTED (directive 47):
  E = 0.557 ± 0.002 (0.55678 ± 0.00225 over n>=256), 1/2 ruled out by >25 se;
  per-doubling slopes oscillate about 0.556, no drift, no closed form attached.
  Two tasks close the pass: (a) log-periodic-oscillation-test-d47 — tabulate
  BOTH w*(n)/n^0.5568 AND w*(n)/n^0.58496 against log2(n) side by side
  (directive 48: log2(3)-1 = 0.58496 is the natural candidate, since A006046's
  exact a(2k)=3a(k) carries exponent log2(3) and the n=256->512 local slope
  0.5850 equals it to 4 decimals; a straight fit over ~7 doublings is biased
  low by a log-periodic correction, so 0.5568 may be a window artifact) and
  report which residual is bounded-periodic with no trend; if neither is flat,
  keep 0.557 as fitted — log2(3)-1 must beat 0.5568 on the residual, not by
  prettiness; (b)
  write-pass3-conclusion-d47 — the pass conclusion (theta->0, threshold weight
  sublinear at n^0.557 or n^(log2(3)-1) as the residual decides, demand
  strictly weaker than switch density, claim block
  n=8..32768 measured-not-proved, open lemmas G-threshold-asymptotic-zero and
  G-threshold-concentration, genericity caveat 'typical is not this string').
```
