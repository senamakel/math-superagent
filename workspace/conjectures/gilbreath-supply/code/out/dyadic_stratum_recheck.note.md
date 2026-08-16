# Dyadic-gap route: popcount/run-count re-check verdict

Re-examination of the SUPPLY dyadic-gap-character falsifier.
Capture: `code/out/dyadic_stratum_recheck.captured.txt`.

## Pipeline confirmed
`stratum_recheck.py` reproduced the earlier
`code/out/dyadic_stratify_by_popcount.captured.txt` exactly:
n=4000 per-popcount partials p=1:-3 … p=11:+3, S=48, |S|/n=0.0120, and the
0.740 figure (which is Σ|partial_p| over p≤5 / Σ_all = 74/100). Exact SOS via
`lib.supply_fold.s_terms_sos`, cross-checked internally (sum(terms)==S,
count(−1)==ones).

## Low-popcount group is balanced, not same-signed
- n=4000, popcount≤5: 1584 depths, +1=826, −1=758, net +68 (52/48).
- n=4000, popcount>5: 2414 depths, net −20. The halves *oppose*, so
  |S_low|/|S|=68/48=1.417 is an opposition artifact — unstable across n
  (n=400: 5/16=0.312; n=1000: S=−2, ratio 7.0).
- n=400 and n=1000: low group also ~52/48, not one-signed.

## Run-count split (the few-run strata the route actually reads)
- n=4000: few-run (runs≤4) is 7.4% of depths, net −4 (146 vs 150, balanced);
  largest classes runs=16:+54, runs=64:+45 are ~53/47 internally.
- n=400/1000: few-run group net −11 each, balanced.

## Verdict: route DEAD.
No stratum is one-signed; weight is spread; the few-run depths carry no net
signal. A pointwise dyadic-gap correlation bound inside those strata has no
clean one-sided input, so the arithmetic needed is as strong as the mean —
the route collapses toward switch density. Confirms the on-disk refutation.

## Correction to the earlier table's reading
The supporting figure "0.740 |S|-weight-share for p≤5" was a mis-leading
support: it measures where per-stratum |partial sums| concentrate, and those
partials come from internal cancellation, not one-sidedness. The low group's
own net is a small 52/48 residue. The earlier *conclusion* (DEAD) was right;
its weight-share *metric* was the shaky part, now superseded by the honest
+/−1 counts above.
