# Primes-vs-fair prefix variance at N=40000: excess persists, limit undetermined (directive 15, corrected per 19/20)

Executor: `code/averaged/fair_prefix_variance_40000.py`, 5 uniform-h Monte Carlo
trials at N=40000 (529s). Capture: `code/out/fair_prefix_variance_40000.txt`.

## The question and the answer (measured, not proved)

Directive 15: does `primes/fair` — the ratio of the primes' prefix empirical
variance `s2_N` of `nu2(n)/n` to the uniform-h fair-model Monte Carlo prefix
variance — tend to 1, to a constant above 1, or keep falling from 1.283@4000?

| N | primes/fair | p·4N/lnN | f·4N/lnN |
|---|---|---|---|
| 1000  | 1.492 | 1.443 | 0.967 |
| 4000  | 1.420 | 1.392 | 0.981 |
| 10000 | 1.380 | 1.361 | 0.986 |
| 20000 | 1.353 | 1.337 | 0.988 |
| 30000 | 1.339 | 1.324 | 0.989 |
| 40000 | 1.329 | 1.315 | 0.990 |

**Corrected verdict (directive 19/20): the excess PERSISTS over the measured
range, but the limit is UNDETERMINED.** primes/fair is strictly decreasing at
every checkpoint (1.492@1000 → 1.329@40000), monotone with decelerating
decrements (slope vs ln N = −0.044). It has NOT plateaued — a sequence still
falling at its final measured step has not plateaued — and the two limits mean
opposite things: if the ratio reaches 1 the primes are asymptotically
indistinguishable from uniform for this statistic; if it stops above 1 there is
a permanent structural excess. Two decades (1000..40000) do NOT separate those
hypotheses: the file's own log-linear fit (slope −0.044) reaches 1 near
N ≈ 7×10^7, far beyond the measured range. Independent 4-trial crossing run
gives 1.341@40000 — agreement with the value, not with any limit.

The fair side tracks the analytic decoupled log-null exactly (`f·4N/lnN =
0.990@40000`), which independently confirms the proved `log(N)/(4N)` null
(claim `fold-rank-n-minus-2-binomial-proved` is what makes `Var(nu2/n) =
(n-2)/(4n^2) ~ 1/(4n)` and hence `E[s2_N] ~ log(N)/(4N)`). So the primes carry a
real, stable excess — the sharpest measurement available of how far the fixed
prime string h sits from random for this statistic.

Data-path is clean: `hP[:8] = [1,1,1,0,1,0,1,0]` == canonical prime `h[:8]`,
guard passed (`nu2(53)=18, nu2(64)=27, nu2(4000)=1975, mu_4000~0.4977`),
`nu2[40000]=20081` (~0.5020, the primes value — not a control). Negative-control
behaviour is as required from the sibling capture.

## What this means for the open problem

The like-for-like Monte Carlo ratio gives primes/fair = 1.492@1000 → 1.329@40000:
monotone decreasing with decelerating decrements. The excess PERSISTS over the
measured range (the primes carry ~33% more prefix variance than the uniform
fair model at 40000, and the fair side independently tracks the proved
log(N)/(4N) null at f·4N/lnN = 0.990). **Caution (directive 19):** two decades
do NOT separate a limit of 1 from a limit of a constant above 1 — the falling
decrements are consistent with (a) an eventual constant ~1.3 or (b) slow decay
still toward 1. The claim below is therefore "excess persists over the measured
range with decelerating decrements", NOT "converges to a constant above 1".
The open problem prove s2_N → 0 (directive 14) stands; what is settled is that
the excess is real and stable over [1000,40000], not that its limit is decided.

```claim
id: fair-mc-primes-ratio-constant-133-40000
statement: The like-for-like ratio of the primes' prefix empirical variance of
  nu2(n)/n to the uniform-h fair-model Monte Carlo prefix variance is
  primes/fair = 1.492@1000 -> 1.420@4000 -> 1.380@10000 -> 1.353@20000 ->
  1.339@30000 -> 1.329@40000: monotone decreasing with decelerating decrements
  (slope vs ln N = -0.044), so the excess above the fair model PERSISTS over
  the measured range [1000,40000]. The fair side tracks the proved log(N)/(4N)
  null (f*4N/lnN = 0.990@40000); the primes sit at p*4N/lnN = 1.315. Two
  decades do NOT separate a limit of 1 from a limit of a constant above 1 —
  the limit is undetermined, but the ~33% excess is real and stable over the
  measured range.
hypotheses: floored oracle nu2(n)=wt(Phi_n h), d in [2,n-1] (s_sos==s_direct;
  guard nu2(53)=18, nu2(64)=27, nu2(4000)=1975, mu_4000~0.4977), exact
  Fractions, N=40000, 5 uniform-h trials; data-path check hP[:8]==canonical
  prime h[:8]; nu2[40000]=20081 = primes.
holds-here: yes — measured to N=40000 (capture code/out/fair_prefix_variance_40000.txt).
status: measured
bearing: the excess above the uniform prefix-variance null PERSISTS over the
  measured range [1000,40000] (~33% at 40000), with decelerating decrements;
  whether the limit is 1 or a constant above 1 is NOT decided by these two
  decades (directive 19). This is the sharpest single measurement of how far
  the fixed prime string sits from random for this statistic. The open problem
  prove s2_N -> 0 (directive 14) remains.
anchor: code/out/fair_prefix_variance_40000.txt ;
  code/averaged/fair_prefix_variance_40000.py
```
