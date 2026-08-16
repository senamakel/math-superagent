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
| `build_canonical_seq.py` | _(undescribed)_ |
| `check_data_consistency.py` | _(undescribed)_ |
| `check_name.py` | _(undescribed)_ |
| `check_oracle_consistency.py` | _(undescribed)_ |
| `check_subseqs.py` | _(undescribed)_ |
| `check_subseqs2.py` | _(undescribed)_ |
| `compare_convention.py` | _(undescribed)_ |
| `control_generic.py` | _(undescribed)_ |
| `discriminator_probe.py` | _(undescribed)_ |
| `drift_discriminator.py` | _(undescribed)_ |
| `dyadic_collapse_and_prime_stats.py` | _(undescribed)_ |
| `dyadic_identity_and_blocks.py` | _(undescribed)_ |
| `dyadic_selfsim.py` | _(undescribed)_ |
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
| `gen_verified_nu2.py` | _(undescribed)_ |
| `incr_corr.py` | _(undescribed)_ |
| `increment_cancel_identity.py` | _(undescribed)_ |
| `indep_extract.py` | Guard-checked extraction of nu2(n), S(n), D(n), and dyadic subsequences from the canonical nu2_primes_xor_40000.json, with corrected indexing (d[i]=nu2(i), i==n) verified against guards nu2(53)=18,64=27,4000=1975,40000=20081. |
| `inspect_nu2_json.py` | _(undescribed)_ |
| `kstar_cum_independent.py` | Independent exhaustive 2^n brute of the cumulative (nested) C_1..C_K correlation-order budget K*(n), confirming K*(n)=floor(n/2) for n=2..18; the deliverable answer comes from it. |
| `kstar_witness_functional.py` | Reads off the separating functional behind the K* witness: for the n=8 pair h=00000010 vs h'=00000100 (identical C_1, S^2=0 vs 4) it enumerates the 18 symmetric-difference monomials M_d△M_d' whose product differs — exactly those with |
| `nu2_oracle_def.py` | _(undescribed)_ |
| `oracle_exact.py` | _(undescribed)_ |
| `parseval_bracket.py` | _(undescribed)_ |
| `per_scale_second_moment.py` | _(undescribed)_ |
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
| `total_acf_crux.py` | _(undescribed)_ |
