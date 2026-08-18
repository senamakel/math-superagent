# DF2a slow-divergence / ECT reconnaissance

## Method
The theory tested is the extended-complete-Chebyshev (ECT) criterion: a finite family is an ECT system on an interval when its initial Wronskians do not vanish there. Slow-divergence calculations reduce local passage contributions to polynomial/logarithmic channels; exact symbolic Wronskians are therefore a necessary local algebraic check, not a global cyclicity proof.

## Executed evidence
`code/df2a_slow_divergence_symbolic.py` first calls the canonical naive oracle `brute.verify_all`, reproducing all 7 worked examples in `problem.md` (including the two additional radial controls), then computes exact Wronskians for
`1, t, t^2, t^2 log(t)` on `t>0`.

Capture: `code/out/df2a_slow_divergence_symbolic.captured.txt`.

Exact output:
- W1 = 1
- W2 = 1
- W3 = 2
- W4 = 4/t

Thus this particular four-channel toy passes the ECT nonvanishing test on `t>0`, and in particular on `1 <= t <= 2`.

## Limitations / attack
This is not the published DF2a normal form. It contains no paper-specific transition maps, slow-divergence integral, unfolding parameters, global domain, or displacement-function zero argument. Consequently it establishes no DF2a finite-cyclicity result. The earlier formal-channel calculation with `t^2*L` treated `L` as algebraically independent and correctly produced W4=0; replacing it by the genuine `log(t)` gives 4/t. This boundary distinction is exactly why formal-log ECT conclusions cannot be transferred without the derivative rule `d log(t)/dt=1/t` and a specified domain.

The larger computation was intentionally only the new hypothesis test: *does a genuine logarithmic channel, rather than a formal independent symbol, restore nonvanishing of the fourth Wronskian?* It answered yes for this toy, not for DF2a.
