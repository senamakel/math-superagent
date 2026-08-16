# Index — code/pattern_finder

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `acf_and_switch.py` | _(undescribed)_ |
| `analyze_increments.py` | _(undescribed)_ |
| `ar1_meanrevert.py` | _(undescribed)_ |
| `attack_second_moment.py` | Exact SOS-fold extension of the per-index second-moment plateau E[S(n)^2]~(n-2) to N=131072; attacks the rare-spike falsifier and the uniform |
| `autocorr_boundary.py` | Two-state Markov chain (autocorr (1-2a)^k) sweep of fold second-moment ratio: maps where density-1 SUPPLY breaks. Boundary ~ |
| `bench_dyadic_sos.py` | _(undescribed)_ |
| `break_exponent_competing.py` | Competing-model fit of threshold weight w*(n): pure power vs power*log-power vs forced sqrt*(log n)^B. Shows B is not significant and sqrt-model fits worse, so E~0.555 sublinear survives. |
| `build_canonical_seq.py` | _(undescribed)_ |
| `check_data_consistency.py` | _(undescribed)_ |
| `check_exponent_identifiability.py` | Direct log-drift test: correlation of log2(log2 n) with the pure-power residual of exact threshold weights (+0.045) — no (log n)^B drift, confirms bounded log2-periodic residual and E~0.555. |
| `check_name.py` | _(undescribed)_ |
| `check_oracle_consistency.py` | _(undescribed)_ |
| `check_subseqs.py` | _(undescribed)_ |
| `check_subseqs2.py` | _(undescribed)_ |
| `closedform_nonseparable.py` | Quantifies that 5/9 is not separable from fitted 0.555 (identical residual sd, exponent gap 30x below periodic swing). |
| `closedform_scan.py` | Sweeps candidate closed-form exponents for the threshold weight; shows 5/9 and 0.555 indistinguishable. |
| `compare_convention.py` | _(undescribed)_ |
| `control_generic.py` | _(undescribed)_ |
| `debug_int.py` | _(undescribed)_ |
| `debug_n16.py` | _(undescribed)_ |
| `directive47_compare.py` | Side-by-side residual: at 0.5568 w/n^E is bounded periodic (spread 0.024), at 0.58496 it monotone-drifts 0.624->0.531 - data prefers 0.555 over log2(3)-1. |
| `discriminator_probe.py` | _(undescribed)_ |
| `drift_discriminator.py` | _(undescribed)_ |
| `dyadic_collapse_and_prime_stats.py` | _(undescribed)_ |
| `dyadic_identity_and_blocks.py` | _(undescribed)_ |
| `dyadic_selfsim.py` | _(undescribed)_ |
| `exact_threshold_8192.py` | _(undescribed)_ |
| `exact_threshold_clean.py` | _(undescribed)_ |
| `exact_threshold_large.py` | _(undescribed)_ |
| `exact_threshold_logspace.py` | _(undescribed)_ |
| `exact_weight_threshold.py` | _(undescribed)_ |
| `excess_decomposition.py` | Decomposes the second moment excess E[S^2]-(n-2) to probe whether cross-terms grow (reported: excess is small/O(1) mean, primes at uniform level). |
| `extend_dyadic_k25.py` | _(undescribed)_ |
| `extend_dyadic_sequence.py` | _(undescribed)_ |
| `extend_second_moment.py` | Exact SOS-fold per-index sampler of the second-moment plateau and sign bias to N=65536. Input: N (default 65536). Output: S, S/sqrt(n), S^2/(n-2), S/n at sampled n plus fraction S>0. |
| `extract_and_analyze.py` | _(undescribed)_ |
| `extract_core_seqs.py` | _(undescribed)_ |
| `extract_dyadic_nu2.py` | Extracts dyadic and extremal subsequences of nu2(n) from the canonical JSON (nu2_primes_xor_40000.json) and computes max/min of nu2/n over the range, with the suppressible sys.set_int_max_str_digits note for n=2^k beyond the JSON range. |
| `extract_fresh_sequences.py` | _(undescribed)_ |
| `final_reduction_check.py` | _(undescribed)_ |
| `fit_growth.py` | _(undescribed)_ |
| `fit_threshold_exponent_pass3.py` | OLS fit of the exact-mean linear-supply threshold weight: log2(w*) = a + E*log2(n) over the tail n>=256, with per-doubling slopes, standard error on E, and test against candidate closed forms 1/2 and log_4(3)=0.7925. Reports E=0.55678 +/- 0.00225 (fitted, not a closed form). Uses exact integer w* values from the verified P_d(w) formula; cross-checked with an independent numpy lstsq route. Output captured to code/out/threshold_exponent_fit_pass3.txt. |
| `gen_verified_nu2.py` | _(undescribed)_ |
| `incr_corr.py` | _(undescribed)_ |
| `increment_cancel_identity.py` | _(undescribed)_ |
| `indep_extract.py` | Guard-checked extraction of nu2(n), S(n), D(n), and dyadic subsequences from the canonical nu2_primes_xor_40000.json, with corrected indexing (d[i]=nu2(i), i==n) verified against guards nu2(53)=18,64=27,4000=1975,40000=20081. |
| `inspect_nu2_json.py` | _(undescribed)_ |
| `kstar_cum_independent.py` | Independent exhaustive 2^n brute of the cumulative (nested) C_1..C_K correlation-order budget K*(n), confirming K*(n)=floor(n/2) for n=2..18; the deliverable answer comes from it. |
| `kstar_witness_functional.py` | Reads off the separating functional behind the K* witness: for the n=8 pair h=00000010 vs h'=00000100 (identical C_1, S^2=0 vs 4) it enumerates the 18 symmetric-difference monomials M_d△M_d' whose product differs — exactly those with |
| `log_periodic_quantify.py` | Quantifies the log-periodic decomposition: w/n^0.5568 flat at each fixed phase across doublings, phase means differ by amplitude ~0.069 - confirms bounded period-1 oscillation, no trend. |
| `log_periodicity.py` | _(undescribed)_ |
| `log_periodicity_extend.py` | Extends exact threshold to non-power-of-two large n (phase 1.25/1.5) to test log-periodicity; produces the w* values at n up to 65536 used in the decisive log-periodic analysis. |
| `mean_profile.py` | _(undescribed)_ |
| `mechanism_E.py` | Continuous independent-bit approximation of the mean; solving mean=0.4 gives E->~0.53 slowly, showing the exact 0.555 is higher (correlation terms) but sublinearity is robust. |
| `nu2_oracle_def.py` | _(undescribed)_ |
| `oracle_exact.py` | _(undescribed)_ |
| `parseval_bracket.py` | _(undescribed)_ |
| `per_scale_second_moment.py` | _(undescribed)_ |
| `phase1_exponent.py` | Phase-1.0 (powers of 2) exponent fit that removes log-periodic bias: E=0.555+/-0.002, 27 sigma from 1/2, 14.8 from log2(3)-1. |
| `price_bounded_autocorr.py` | Prices GOAL-priority-2 "bounded autocorrelation of h": compares fold second-moment ratio E[S^2]/(n-2) for primes vs iid vs thue vs alternating at sampled n. Shows iid passes (0.8-1.1) like primes while thue/alt collapse => raw autocorr not discriminating. |
| `price_bounded_autocorr2.py` | Prefix-mean version of price_bounded_autocorr over [512,16384]: primes ~1.12, iid ~0.80, thue ~8400, alt ~8400. Confirms the negative pricing of the bounded-autocorrelation candidate. |
| `probe_exact_dS.py` | _(undescribed)_ |
| `record_lows_all_n.py` | _(undescribed)_ |
| `s0_var.py` | _(undescribed)_ |
| `s0_var_struct.py` | _(undescribed)_ |
| `scale_control.py` | _(undescribed)_ |
| `scale_decomp.py` | _(undescribed)_ |
| `scale_mean.py` | _(undescribed)_ |
| `scale_mean_control.py` | _(undescribed)_ |
| `scale_variance.py` | _(undescribed)_ |
| `second_moment_structure.py` | Measures the prime-h fold second moment E[S(n)^2]/(n-2) vs the exact iid-uniform prediction n-2, and Monte-Carlo-verifies the uniform second moment. |
| `telescoping_crux.py` | _(undescribed)_ |
| `three_exact_verifications.py` | _(undescribed)_ |
| `threshold_exact_extend.py` | Exact closed-form threshold computation (first version); superseded by the linear-scan version because the mean is non-monotone in w. |
| `threshold_hypotheses.py` | Directive-45 discriminator: tabulates w/sqrt(n), w/(sqrt(n)ln n), w/n^log4(3), per-doubling slopes, and OLS exponent for the threshold-weight sequence. Shows 1/2 is 25 sigma away. |
| `threshold_linearscan.py` | Authoritative exact threshold: linear scan over w since mean_n(w) is non-monotone (parity alternation). Reproduced all 16 known w* (n=8..32768) digit-for-digit - the independent check. |
| `threshold_models.py` | Model comparison for w*(n): pure power, sqrt*log^g, and log_4(3) families; shows the power E~0.557 with no log correction wins on residuals; leading sparse-term mechanism predicts 0.415 not 0.557. |
| `total_acf_crux.py` | _(undescribed)_ |
| `verify_far_threshold_indep.py` | Independent exact recomputation (different code path, per-popcount grouping) of the exact-mean linear-supply threshold weight w*(n) through n=131072; reproduces all known values digit-for-digit, second route for the tends-to-zero finding. |
| `verify_wstar_seq.py` | Independent third-route computation of the exact linear-supply threshold weight w*(n) = min w with mean nu2/n over weight-w strings >= 0.40, via direct hypergeometric odd-count grouped by popcount; cross-checks the formula against the literal brute fold s_sos and reproduces all published w* values plus the exact 27-point sequence. |
