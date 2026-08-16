# Chebyshev second-moment capture at N=40000 — primes

The N=40000 second-moment work is the strongest averaged-form artifact this run
has produced. Re-run under directive 13/14 discipline: ONE canonical oracle
(`lib.nu2.fold_nu2` = `lib.supply_fold.s_sos`, the floored submask fold
d ∈ [2,n−1]), mandatory entry guard `assert_supply_guard(40000)`
(ν₂(53)==18, ν₂(64)==27, primes μ_4000 within 0.01 of 0.4977; the absolute
count at n=4000 is convention-sensitive — the floored `d∈[2,n−1]` value is
1975, confirmed by three routes s_sos/s_direct/from-scratch, the 1976 in older
captures being the `d∈[0,n−2]` bookkeeping),
and a first-three-lines capture header naming sequence / oracle / n-range so a
control cannot be mistaken for the subject.

```claim
id: n40000-second-moment-density1-measured
statement: For the prime gap-parity string h (h[j]=[q_{j+2}!=q_{j+1} mod 4]) and
  the floored submask fold nu2(n)=#{d in [2,n-1]: T(n,d)=1}=wt(Phi_n h),
  measured at ceiling N=40000: mu_N = (1/N) sum_{n<=N} nu2(n)/n = 0.499658;
  over [30000,40000] EVERY n has nu2(n)/n >= 0.49 with min 0.490114 and ZERO
  dips below 0.45; over [50,40000] only 1 n below 0.35, 3 below 0.40, 10 below
  0.42, 51 below 0.45, all densities under 0.0013; s2_N = variance of nu2(n)/n
  over n<=N decays 0.000783@4000 to 0.0000934@40000. Stronger (pointwise, no
  exceptional set in the tail): min of nu2(n)/n over [X,40000] RISES with X:
  0.3396@50, 0.4599@1000, 0.4850@10000, 0.4901@30000.
hypotheses: exact ceiling N=40000; oracle lib.nu2.fold_nu2 = lib.supply_fold.s_sos
  (cross-checked s_sos==s_direct on n=4..200 and spots 53,64,100); floored
  convention d in [2,n-1]; exact Fractions; negative controls all-ones (M=0,
  vacuous) and Thue-Morse (FALLS to ~0.064, ~99.3% of n below 0.30) both behave
  as required, showing the pipeline discriminates.
holds-here: yes, measured over n=2..40000 (primes only for the operative claim).
status: checked
bearing: evidence for c = 1/2, NOT an argument for it. The rising pointwise min
  is evidence nu2(n)/n -> 1/2 pointwise with no exceptional set in the tail.
  The open problem in its sharpest form: prove s2_N -> 0, equivalently that the
  exceptional set {n : nu2(n)/n < c} is finite for every c<1/2. The WEAKER
  sufficient input for SUPPLY is density-1 (s2_N -> 0 + Chebyshev gives
  density-1 nu2(n)/n >= c'); the pointwise-finite-exceptional-set statement is
  stronger than needed.
anchor: code/out/chebyshev_oracle_verified_N40000.txt
```

## Discrepancy record (directive 14's last item)

The operator asked me to record, not chase, which of two accounts of the prior
capture was true. `code/out/chebyshev_second_moment_N40000.settles.md` claims
the capture file "was found on disk at 0 bytes." But the operator reports the
file they read before this run carried a populated table with `mu=0.064146`
(the Thue-Morse value) beside the primes. The two accounts cannot both be
right: a 0-byte file holds no `mu=0.064146` line. The `chebyshev_second_moment_N40000.txt`
in this workspace now IS a populated full capture (primes 0.499658, plus
separately-labelled all-ones and Thue-Morse controls) — so whichever state the
prior file was found in, the current on-disk capture is the correct GATED re-run
produced under directive 13, and the `.settles.md` "0 bytes" claim is unreliable
narrative (it described the state before the earlier corrected re-run, and
cannot be reconciled with the operator's reading of a populated Thue-Morse
table). The key operational fact is that the DISCREDITED capture (Thue-Morse
masquerading as primes, header N=40000 vs table N=4000) must not be cited; the
correct primes capture is the one this claim block and the verified output file
record.
