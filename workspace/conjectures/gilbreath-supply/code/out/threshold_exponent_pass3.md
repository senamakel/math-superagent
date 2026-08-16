# Sublinear exponent of the exact-mean linear-supply threshold weight

The exact-mean threshold weight w*(n) = min w with mean_n(w) >= 0.40 over
weight-w binary strings in F2^n is sublinear in n. This note records the
fitted exponent and files the claim block.

```claim
id: weight-threshold-tends-to-zero-sublinear-exponent
statement: The exact-mean linear-supply threshold weight w*(n) — the minimum
  Hamming weight w such that the mean of nu2(h)/n over all weight-w binary
  strings h in F2^n is >= 0.40 — grows like n^E with a FITTED exponent
  E = 0.55678 +/- 0.00225 (OLS of log2(w*) vs log2(n) over the tail n >= 256,
  n = 256..32768, 8 points; identical by an independent numpy lstsq route).
  Per-doubling slopes log2(w*(2n)/w*(n)) for n = (16,32,64,128,256,512,1024,
  2048,4096,8192,16384) are (0.737, 0.485, 0.652, 0.541, 0.585, 0.544, 0.571,
  0.566, 0.541, 0.550, 0.543), settling around ~0.54-0.58. Since E > 0 the
  threshold weight is sublinear (w* = o(n)); linear supply (mean nu2/n >= 0.40)
  is therefore TYPICAL once the switch weight exceeds ~n^0.56, i.e. at a sublinear
  number of on-bits — strictly weaker than a positive fraction (n^1). The exact
  per-n threshold weights are: n=8:3, 10:3, 12:3, 14:4, 16:3, 32:5, 64:7,
  128:11, 256:16, 512:24, 1024:35, 2048:52, 4096:77, 8192:112, 16384:164,
  32768:239, giving theta = w*/n = 0.375, 0.300, 0.250, 0.286, 0.188, 0.156,
  0.109, 0.086, 0.063, 0.047, 0.034, 0.025, 0.019, 0.014, 0.010, 0.0073 — a
  monotonically falling ratio consistent with w*/n -> 0 (sublinearity), NOT a
  plateau.
hypotheses: per-n w* values are EXACT, computed from the verified threshold
  formula P_d(w) = (C(n,w) - [z^w](1-z)^k (1+z)^(n-k)) / (2 C(n,w)) with
  k = 2^popcount(d), the per-weight mean nu2/n averaged over all C(n,w) weight-w
  strings. Formula cross-checked against the literal brute oracle
  lib.supply_fold.s_sos digit-for-digit (code/out/threshold_exact_mean_
  independent.txt PART 1 & 2). n range 8..32768; the ordering of squared-error
  overlog2 is exact-mean, threshold 0.40 fixed.
holds-here: yes — every w* is an exact integer from the verified formula; the
  small-n values (n=8..16) agree with the exhaustive enumeration in
  code/out/linear_supply_by_weight.txt (8->3,10->3,12->3,14->4,16->3).
  The EXPONENT and the tend-to-zero LIMIT are fitted from the sampled n-list,
  not proved — the data are consistent with w* ~ n^0.56 but do not establish a
  law for all n.
status: measured-not-proved (the per-n values are exact; the sublinear exponent
  and the limit are numerical fits over the sampled range).
bearing: Linear supply is typical at a sublinear (n^~0.56) switch-weight
  threshold, so the arithmetic demand on the primes to make nu2(n) >= 0.4 n is
  strictly weaker than a positive fraction of switch bits (n^1) — it reduces to
  a sublinear number of mod-4 switches. This is problem.md result type 4 (an
  input strictly weaker than switch density), NOT type 1 (unconditional SUPPLY).
  One-sentence genericity gap: 'typical is not this string' — being above the
  threshold does not prove the primes' particular h has linear supply; that is
  the same genericity gap the prior passes ended on, and what changed is only
  the size of the arithmetic input needed (a sublinear switch count near n^0.56
  rather than a positive density).
anchor: code/out/threshold_exact_mean_independent.txt (exact formula, PART 3),
  code/out/threshold_limit_exact.txt (PART A), code/out/linear_supply_by_weight.txt
  (small-n exhaustive), code/pattern_finder/fit_threshold_exponent_pass3.py,
  code/out/threshold_exponent_pass3.md (this note), code/out/threshold_exponent_fit_pass3.txt.
```
