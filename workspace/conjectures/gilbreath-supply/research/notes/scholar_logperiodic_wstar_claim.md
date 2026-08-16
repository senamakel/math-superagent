# Scholar — claim block for the confirmed log-periodic structure of the threshold weight w*(n)

Author: scholar. This run's own third-pass computation (pattern_finder,
directives 45/46/47) resolved the pass's single open computation — the structure
of the linear-supply weight threshold — and the result is recorded in prose
(`research/CONCLUSION-PASS3.md`, `code/out/pattern_finder_deliverable_logperiodic.md`)
but had **no claim block**, so it never reached the claims ledger. This note
files it. The underlying source theorem (HJT 2024 Thm 2.2) is already a claim,
`hjt-p2-log-periodic-representation-proved`; what is missing is the run's own
*measured* confirmation that w*(n) carries that form.

The `follows-from` edge to the HJT block is the reason this is a Corollary-style
entry rather than an orphan: HJT grounds the *form* in a theorem; the run's exact
computation supplies the *specific exponent and amplitude* for w*(n), and the
adversarial refuter's independent linear-scan reproduction supplies the check.

```claim
id: wstar-log-periodic-n055-confirmed-measured
statement: >
  The exact-mean linear-supply threshold weight w*(n) = min{w : E_{S_w}[nu2/n]
  >= 0.40 over all weight-w strings in F2^n} (mean half, exact no sampling)
  satisfies w*(n) = n^E · P(log2 n) with a FITTED exponent E ~ 0.555
  (phase-1.0 OLS E = 0.55499 ± 0.00202 over n=256..65536) and P a bounded,
  period-1-in-log2(n) log-periodic factor of amplitude ~ 0.07 (phase means:
  phase 1.00 ~ 0.7383, phase 1.25 ~ 0.807, phase 1.50 ~ 0.7893, flat at each
  fixed in-cell phase n/2^{floor(log2 n)} across 9 doublings). Hence the
  threshold ratio theta = w*/n -> 0: linear supply (nu2/n >= 0.40) is
  exact-mean-TYPICAL once the switch count exceeds about n^0.555 — a SUBLINEAR
  switch count, strictly weaker than a positive mod-4 switch density (Theta(n)).
  1/2 is rejected at >25 sigma (w^2/n rises 0.77->1.74 not flat; 27 sigma on the
  phase-1.0 fit); log2 3 - 1 = 0.58496 is rejected at >14 sigma (residual
  monotone-drifts 0.624->0.531, spread 0.093, vs bounded-periodic spread 0.024
  at 0.555). 5/9 = 0.5556 is NOT separable from the fitted 0.555 (identical
  residual sd 0.01466, log2-units, n=256..65536; exponent gap 30x below the
  periodic swing) so 5/9 is a plausible candidate but NOT an established closed
  form. Per-n w* and theta are exact for n=8..65536
  (3,3,3,4,3,5,7,11,16,24,35,52,77,112,164,239,349 across n=8..65536;
  theta = 0.375@8 .. 0.0053@2^16), independently reproduced digit-for-digit by a
  from-scratch linear scan (required because mean_n(w) is NON-MONOTONE in w by
  parity).
hypotheses: canonical floored fold d in [2,n-1]; exact mean over the weight-w
  sphere via the Krawtchouk parity formula P_d(w) = (C(n,w) - [z^w](1-z)^k
  (1+z)^{n-k})/(2 C(n,w)), k = 2^popcount(d) (claim threshold-mean-exact-
  parity-formula), validated against exhaustive s_sos on small (n,w); n in
  [8,65536].
holds-here: yes — this is this run's own exact computation on the canonical
  oracle, cross-checked by the independent linear scan and by the HJT structural
  theorem (hjt-p2-log-periodic-representation-proved) which it realizes.
status: measured-not-proved (the per-n w* values are EXACT; the exponent 0.555
  and the log-periodic amplitude ~0.07 are FITTED over n<=65536; the limit
  theta->0 is the data-supported inference over every measured n>=64, not a
  proof)
bearing: >
  This is the third pass's affirmative headline and the workspace's first
  affirmative weakening across three passes. It reduces the arithmetic demand
  the primes would need for linear supply from a positive mod-4 switch density
  (Theta(n)) to a sublinear switch count ~n^0.55 — problem.md result type 4,
  never type 1. It does NOT prove SUPPLY for the primes: 'typical is not this
  string' (threshold-typical-is-not-this-string), the genericity gap to the
  primes' own h, is unchanged. The passage from this to a proof needs the two
  open lemmas G-threshold-asymptotic-zero and G-threshold-concentration
  (threshold-limit-hinges-on-hypergeometric-mode-bound); the HJT block grounds
  the log-periodic FORM in a theorem but does not transfer the exponent to w*.
  WHO: nobody should re-derive the threshold column (exact) or re-run the
  log-periodic test; both are closed on disk.
follows-from: threshold-mean-exact-parity-formula, hjt-p2-log-periodic-representation-proved
contradicts: none — supersedes the pass-2 'plateau near 1/8' reading (conclusion
  of linear-supply-by-weight-class) which a 300-sample/coarse-grid artifact
  produced; recorded in CONCLUSION-PASS3.md / supply-class-characterisation
  thread.
answers: threshold-limit-open-lemma-comes-next — does NOT answer
  walsh-spectral-subset-b904 (that request is about the prime string, not the
  generic threshold).
anchor: code/out/threshold_weight_logperiodic_extended.txt (decisive capture);
  code/out/pattern_finder_deliverable_logperiodic.md;
  research/CONCLUSION-PASS3.md; code/pattern_finder/phase1_exponent.py,
  directive47_compare.py, threshold_linearscan.py, log_periodicity_extend.py;
  research/summaries/hwang_janson_tsai_periodic_minimum_binomial_modp.md
```

## What this means for the run

The claim closes the measured half of the third pass's owed computation in a
form the ledger can cite: the threshold weight is sublinear at ~n^0.555 with a
confirmed log-periodic factor, so the arithmetic demand is sublinear. It is a
*measured* result (exact per-n values, fitted exponent and amplitude), and it
does not move the goal-past-this-point: SUPPLY for the primes still needs an
unconditional second-moment/Walsh bound (request `walsh-spectral-subset-b904`,
superceded by CONCLUSION-PASS3's two open lemmas for the generic theorem), and
the finite-prefix transfer. Nothing here is a proof of SUPPLY and nothing is
prime-specific.

## Sources that do not help (so nobody re-reads them)

Confirmed against prior passes, no change: the seven `citations_w*` files
(lead-only), the four OEIS rows, `odlyzko_gilbreath` (bibliography), the
Granville–Martin duplicate mirror, the quarantined
`matomaki_radziwill_tao_averaged_chowla`, the two metadata stubs
(`ashikhmin_barg_litsyn`, `friedlander_macwilliams_krawtchouk`), the HAL page,
and `DELETED_wrong_arxiv*`/`DELETED_shiu*` overwrite notes.
