# Index — code/pattern_finder

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

**Status: DONE (directive 35).** This folder has only extensions and
re-verifications of settled results left — `extend_dyadic_k25.py`,
`extend_dyadic_sequence.py`, `extend_second_moment.py`,
`three_exact_verifications.py`, `final_reduction_check.py`. The dyadic-sequence
extension is not on the surviving open statement (research/CONCLUSION.md §5:
an unconditional second-moment / submask-window Walsh bound, which no
measurement reaches), and directive 34 closed the line. Do not start new
pattern-finder work and do not re-run the k=25 extension (see task
`kill-dyadic-k25-and-no-rerun`).

| File | Purpose |
| --- | --- |
| `acf_and_switch.py` | _(undescribed)_ |
| `analyze_increments.py` | _(undescribed)_ |
| `ar1_meanrevert.py` | _(undescribed)_ |
| `attack_second_moment.py` | Exact SOS-fold extension of the per-index second-moment plateau E[S(n)^2]~(n-2) to N=131072; attacks the rare-spike falsifier and the uniform |
| `autocorr_boundary.py` | Two-state Markov chain (autocorr (1-2a)^k) sweep of fold second-moment ratio: maps where density-1 SUPPLY breaks. Boundary ~ |
| `build_canonical_seq.py` | _(undescribed)_ |
| `compare_convention.py` | _(undescribed)_ |
| `control_generic.py` | _(undescribed)_ |
| `discriminator_probe.py` | _(undescribed)_ |
| `drift_discriminator.py` | _(undescribed)_ |
| `dyadic_selfsim.py` | _(undescribed)_ |
| `excess_decomposition.py` | Decomposes the second moment excess E[S^2]-(n-2) to probe whether cross-terms grow (reported: excess is small/O(1) mean, primes at uniform level). |
| `extend_second_moment.py` | Exact SOS-fold per-index sampler of the second-moment plateau and sign bias to N=65536. Input: N (default 65536). Output: S, S/sqrt(n), S^2/(n-2), S/n at sampled n plus fraction S>0. |
| `extract_and_analyze.py` | _(undescribed)_ |
| `extract_core_seqs.py` | _(undescribed)_ |
| `final_reduction_check.py` | _(undescribed)_ |
| `fit_growth.py` | _(undescribed)_ |
| `incr_corr.py` | _(undescribed)_ |
| `increment_cancel_identity.py` | _(undescribed)_ |
| `indep_extract.py` | Guard-checked extraction of nu2(n), S(n), D(n), and dyadic subsequences from the canonical nu2_primes_xor_40000.json, with corrected indexing (d[i]=nu2(i), i==n) verified against guards nu2(53)=18,64=27,4000=1975,40000=20081. |
| `nu2_oracle_def.py` | _(undescribed)_ |
| `oracle_exact.py` | _(undescribed)_ |
| `parseval_bracket.py` | _(undescribed)_ |
| `per_scale_second_moment.py` | _(undescribed)_ |
| `price_bounded_autocorr.py` | Prices GOAL-priority-2 "bounded autocorrelation of h": compares fold second-moment ratio E[S^2]/(n-2) for primes vs iid vs thue vs alternating at sampled n. Shows iid passes (0.8-1.1) like primes while thue/alt collapse => raw autocorr not discriminating. |
| `price_bounded_autocorr2.py` | Prefix-mean version of price_bounded_autocorr over [512,16384]: primes ~1.12, iid ~0.80, thue ~8400, alt ~8400. Confirms the negative pricing of the bounded-autocorrelation candidate. |
| `probe_exact_dS.py` | _(undescribed)_ |
| `s0_var.py` | _(undescribed)_ |
| `s0_var_struct.py` | _(undescribed)_ |
| `scale_control.py` | _(undescribed)_ |
| `scale_decomp.py` | _(undescribed)_ |
| `scale_mean.py` | _(undescribed)_ |
| `scale_mean_control.py` | _(undescribed)_ |
| `scale_variance.py` | _(undescribed)_ |
| `second_moment_structure.py` | Measures the prime-h fold second moment E[S(n)^2]/(n-2) vs the exact iid-uniform prediction n-2, and Monte-Carlo-verifies the uniform second moment. |
| `telescoping_crux.py` | _(undescribed)_ |
| `total_acf_crux.py` | _(undescribed)_ |
