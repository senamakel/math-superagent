```approach
idea: The threshold w*(n) is not a pure power law. √n is rejected at 27σ and n^{log₂3−1} at 14σ (with monotone residual drift); 5/9 is not separable from the fit (residual sd 0.01466 for both, exponent gap ~30× below the periodic swing). The correct form carries a bounded period-1 log-periodic factor.
mechanism: Fitting log w*(n) against log n on the exact per-n data separates the smooth exponent from the periodic residual; the residual amplitude (~0.07) dominates the candidate exponent gaps, so the log-periodic factor is a real feature of the threshold, not noise.
status: grounded
precedent: >
  The negative statistical content is the run's own exact per-n data (claims
  threshold-closed-forms-rejected, 27σ for √n, 14σ for n^{log₂3−1}; residual
  sd 0.01466 for both 5/9 and the fit — inseparable). The POSITIVE reading that
  the residual is a bounded period-1-in-log₂(n) oscillation rather than a trend
  is grounded in the theorem that Pascal-mod-2 counting functions carry exactly
  that form: Hwang–Janson–Tsai arXiv:2408.06817, Thm 2.2 (log-periodic
  representation, p=2 prototype OEIS A006046). Caveat as for
  threshold-weight-sublinear: HJT grounds the FORM, not the exponent. In-workspace:
  claim hjt-p2-log-periodic-representation-proved; notes
  log_periodic_pascal_mod2_engine.md. Falsifier: a tabulation of
  w*(n)/n^0.5568 vs log₂ n showing a monotone trend rather than a bounded
  oscillation would refute the log-periodic reading.
first-step: File the rejection statistics as a negative result (done — claim
  threshold-closed-forms-rejected), then test any remaining candidate exponents
  against the periodic detrended residual before proposing a further closed form.
```

