# Refuter — final report: attack on "about n^0.57 switches suffice" (third-pass head)

## What I attacked

The pass's affirmative result, as the steering directive states it: "linear
supply is typical once the switch count exceeds about n^0.57", where the
threshold weight is `theta(n) = min{w : E_Sw[nu2]/n >= 0.40}` and the
per-doubling slope of `log2(w)` vs `log2(n)` is claimed to "settle near 0.57".

## The four answers, and which came back

**Refuted (as stated)** — the exponent is not 0.57 and not a clean closed form,
and the claim as stated collides with the run's own two-condition definition of
"typical". _Sublinearity survives; the primes-transfer is not touched._ This was
an arithmetic analysis against the exact on-disk integer column, NOT a TPTP
model search — the claim is asymptotic (`w ~ n^p`, `slope -> ?`), a limit over
all n that no finite first-order model can falsify, so `find_counterexample`
cannot express it. I state that encoding limitation explicitly rather than
encode something adjacent (per the refuter rules' honest-encoding requirement).

## Ground 1 — the exponent is a drift to 1/2, not a settled constant 0.57

Exact weights: `3,3,3,4,3,5,7,11,16,24,35,52,77` at `n=8..4096`. Per-doubling
slopes `log2(w_{L+1}/w_L)`:

```
0, 0.737, 0.485, 0.652, 0.541, 0.585, 0.544, 0.571, 0.566
```

last-3 mean = **0.5607**; last-7 mean = 0.5635. The run's OWN saturation theory
(`research/notes/scholar_threshold_exact_mean.md`) predicts
`log2 w = L/2 + 0.42 sqrt(L)`, i.e. slope `= 1/2 + 0.21/sqrt(L)` = **0.5606** at
L=12. The observed 0.5607 matches the theory to 0.000. So the honest closed form
is `w ~ n^{1/2 + 0.42/sqrt(log2 n)} = n^{1/2+o(1)}` — a sublinear square-root
with a subpolynomial correction, drifting to exponent 1/2. 0.57 is the
small-window constant fit, sitting on a declining curve.

Closed-form test (the directive's candidates): `log_4(3) = log(3)/log(4) =
0.7925` — **refuted**, the slope never leaves 0.54–0.57; `1/2` — fitted as the
limit (via the theory); 0.57 — a fitted constant with no theoretical basis and
no clean close form, which is what the directive told me to report if it was not
clean.

## Ground 2 — the exact command settles only the MEAN half of "typical"

"Typical" is **two conditions** (directive 38/39): mean `nu2/n >= 0.40` AND
fraction of weight-w strings with `nu2/n >= 0.40` is `>= 0.5`. The resolved
computation (`threshold_limit_exact.txt`) is the exact MEAN half only. PART B of
the SAME capture gives the sampled frac half and it is **marginal at the
crossing**:

- n=256: exact-mean crossing is w=16, but frac(13)=0.389, frac(19)=0.579, so
  frac(16) ≈ 0.49 — BELOW 0.5. The two-condition theta* is w=19, not 16.
- n=512: exact crossing w=24, but frac(26)=0.5285, so theta* = 26, not 24.

So the reported weights (and hence the 0.57 fit) rest on the weaker single
condition, and the true "typical" threshold sits above the exact-mean threshold.

## What survives

- Sublinearity: `w ~ n^{1/2+o(1)}` — the conclusion that a sublinear switch
  count suffices for typicality (on random weight-w strings) is intact.
- The exact mean itself; the monotone (eventually) decrease of `theta/n` to 0.

## What is refuted / overstated

- "0.57 is a settled exponent / clean closed form" — false; it drifts to 1/2.
- "linear supply is typical once switches exceed ~n^0.57" — at the exact-mean
  crossing the frac>=0.5 half is not yet satisfied at n=256; the true theta* is
  higher and the exponent is not 0.57.
- Reading this as a *weakening of the arithmetic demand on the primes*: the
  result is over random weight-w strings; the transfer to the fixed prime string
  is exactly the unproven non-adversariality, so it does not lower the demand
  from positive switch density to n^0.57 switches. `typical is not this string`.

## Bounds / limits of this refutation

The slope data reach L=12 (n=4096). At L=12 the constant-0.57 and drift-to-1/2
hypotheses differ by only ~0.01, below the ±0.05 scatter — so I cannot *prove*
the exponent tends to 1/2 either; settling it needs n ≳ 2^20 (not on disk).
What is established: 0.7925 is wrong (decisive), the data support 1/2 +
subpolynomial over constant 0.57 (both fit; only the former has the run's own
theory behind it). `measured-not-proved`.

## Deliverables

- `research/scratch/refuter_theta_exponent.md` — Ground 1 analysis + closed-form test.
- `research/scratch/refuter_theta_fraction.md` — Ground 2 (frac half at crossing).
- `research/scratch/refuter_slope_arithmetic.md` — verified slope arithmetic.
- `teams/posts/refuter_theta_exponent.json` — board post.
- Cognee memory recorded.
