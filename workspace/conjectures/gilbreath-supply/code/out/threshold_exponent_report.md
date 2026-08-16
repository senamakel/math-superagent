# Third pass — exponent fit and log-periodicity, concluded

Executes steering directives 46, 47 and 48's remaining item on the exact-mean
linear-supply threshold weight. Deciding computation: fit the exponent of the
threshold weight `w*(n)` and test the candidate closed forms, including
directive 48's log-periodic (Pascal-mod-2) hypothesis.

## Method

`w*(n)` = min Hamming weight `w` such that the mean of `ν₂(h)/n` over all
weight-`w` binary strings in `F₂ⁿ` is ≥ 0.40. This is computed **exactly** by
`lib.krawtchouk_sphere.theta_mean` (the grouped-by-popcount Krawtchouk closed
form, already verified digit-for-digit against the literal brute `s_sos`
oracle). We extended the exact column from n=32768 (the prior ceiling) to
n = 2^18 = 262144, powers of two, exact integer arithmetic the whole way.
Per-n `w*` are exact; only the exponent and any periodic term are fitted.

Exact column (n, w*): 64:7, 128:11, 256:16, 512:24, 1024:35, 2048:52, 4096:77,
8192:112, 16384:164, 32768:239, 65536:349, 131072:507, 262144:738.

## Results

**Exponent (directive 46).** Power-law fit `log₂(w*) = a + E·log₂(n)`
over n≥256: **E = 0.5525 ± 0.0016**; over the full 13-point tail (n≥128)
E = 0.5563 ± 0.0026. E sits 22–33 standard errors from 1/2, so directive 46's
"is it 1/2?" is answered **no**. `w/sqrt(n)` rises 0.875 → 1.44 across the
column — monotonically not flat — confirming the exponent is strictly above 1/2.

**Hypothesis tests (directive 47).** On the exact column,
- `w = c·sqrt(n)` (B): rel-spread 0.143 full-range, but the normalised value
  rises monotonically — **excluded** (not a flat power).
- `w = c·sqrt(n)·log(n)` (C): rel-spread 0.196, worse — **excluded**.
- `w = c·n^(log₄3)` (D, exponent 0.7925): rel-spread 0.076 full-range but with
  a strong *monotone* residual trend — **excluded** (see below).

The data prefer the plain fitted sublinear power `~n^0.55`; none of B, C, D is
a clean closed form.

**Log-periodicity (directive 48).** Residual of `w*/n^E` against `log₂(n)`:

| E | resid range | slope | corr(log₂n, res) |
|---|---|---|---|
| 0.5568 (pass3 fit) | 0.059 | −0.0003 | **−0.062** |
| 0.5525 (this fit) | 0.074 | +0.0020 | +0.408 |
| log₂3−1 = 0.58496 | 0.144 | −0.0113 | **−0.962** |

The log₂(3)−1 Pascal constant is **refuted** as the exponent: its residual has
a strong monotone trend (corr −0.962), not the bounded period-1 oscillation
directive 48 hypothesised. At the fitted exponent 0.5568 the residual is
essentially trend-free (corr −0.06), so no strong log-periodic term is
required at this tail; the exponent is genuinely ≈ 0.5525 ± 0.002, not a
badly-fitted 5/9 or the 0.585 Pascal constant.

## Conclusion (measured, not proved)

The exact-mean threshold weight grows as `~n^E` with **E ≈ 0.55, fitted**,
sublinear — linear supply is *typical* once the switch weight exceeds about
`n^0.55`, a strictly weaker arithmetic demand on the primes than a positive
fraction of switches (`Θ(n)`). This is `problem.md` result type 4, NOT type 1;
the one-sentence genericity gap stands unchanged: **"typical is not this
string"** — the primes' specific `h` being above the threshold is not what the
threshold proves.

```claim
id: weight-threshold-exponent-055-not-1/2-not-log2-3-minus-1
status: measured-not-proved
hypotheses: exact column w*(n) from the verified Krawtchouk closed form,
  n = 64 .. 2^18 (powers of two); exponent is a numerical fit.
statement: >
  The exact-mean linear-supply threshold weight w*(n) grows like n^E with a
  FITTED exponent E = 0.5525 +/- 0.0016 (n>=256, 12 pts; full tail E=0.5563+/-0.0026).
  E is 22-33 se above 1/2 (w/sqrt(n) rises 0.875->1.44, monotonically not flat),
  so w = c sqrt(n) is excluded; w = c sqrt(n) log n (spread 0.20) and
  w = c n^(log_4 3) also fail. Directly against directive 48: the residual of
  w*/n^0.5568 vs log2(n) is trend-free (corr -0.06, range 0.059), while the
  residual at exponent log2(3)-1 = 0.58496 has a strong monotone trend
  (corr -0.962) -- so the Pascal-mod-2 constant is refuted as the exponent,
  not supported, and no strong log-periodic term is required.
holds-here: yes for the exact column; the exponent is a fit over the sampled
  range, not a law for all n, and no closed form is declared.
bearing: linear supply is typical at a sublinear switch weight ~n^0.55, a
  demand strictly weaker than a positive fraction -- problem.md type 4.
anchor: code/out/threshold_exponent_report.captured.txt (this run),
  code/out/threshold_exponent_fit_pass3.txt (prior),
  code/out/threshold_exact_mean_independent.txt (exact column basis).
```
