# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `abgs_m4_check.py` | Same ABGS m=4 check as code/out/abgs_m4_check.py, placed under code/ as the canonical reproduction source. Counts (1,1)=16574,(1,3)=22521,(3,1)=22520,(3,3)=16715; switch=57.5%, switch/equal=1.35. Supports abgs-mod4-nonuniform-measured. |
| `analyze_nu2.py` | _(undescribed)_ |
| `avg_nu2.py` | Deliverable: empirical status of averaged SUPPLY. Re-grounds the linearisation (fold wt vs literal suffix, n=3..60), streams nu2 one n at a time via the SOS fold, and reports exact prime mean/variance of nu2(n)/n at checkpoints, plus all-ones and Thue-Morse negative controls. Verified against direct mean/variance (n=2..120, exact equality) and reproduces problem.md's 0.4933 at n=4000 (1976/4000=0.4940). |
| `brute.py` | Naive oracle for SUPPLY: nu2(n)=wt(Phi_n h) over F2 via explicit Pascal-mod-2 fold matrix (canonical depths d=2..n-1, Lucas submask test). Validated: matches literal matrix route B in verify_brute.py at all tested n; nu2(4000)=1975=0.4938 (measured 0.4933, ~2-cell convention slack); reproduces nu2/n ~in [0.42,0.52] for n=50..3999; negative control (all-ones h -> O(1)) holds. |
| `compute_nu2.py` | _(undescribed)_ |
| `convention_check.py` | _(undescribed)_ |
| `corr_probe.py` | _(undescribed)_ |
| `dip_analysis.py` | _(undescribed)_ |
| `direct_triangle.py` | Literal absolute-difference-triangle reading of the maximal {0,2} suffix. Demonstrates that this literal reading gives nu2=0 for all n>=2 (bottom right-diagonal cell is always 1), so it is NOT the operative definition; the operative one is the fold weight in brute.py. Established by comparing with brute.py on n=20..100. |
| `dyadic_probe.py` | _(undescribed)_ |
| `excess_study.py` | _(undescribed)_ |
| `excess_verify_increments.py` | _(undescribed)_ |
| `extract_excess.py` | _(undescribed)_ |
| `fair_model_exact.py` | Exact brute-force oracle check of the iid-fair-model claim for SUPPLY: for n=2..12 enumerates all 2^n binary strings h, computes nu2(n)=#{d: T(n,d)=1} via the literal submask-XOR (lib.supply_fold.t_direct), and confirms the empirical mean equals (n-2)/2 exactly and the distribution is symmetric about (n-2)/2. Verified by reproduction of the stated equality for every n (2..12); output code/out/fair_model_exact.txt. Also reveals the stronger fact that the distribution is 4*C(n-2,k)/2^n (cells T(n,d) are independent fair bits). |
| `floor_variant.py` | _(undescribed)_ |
| `measure_smax_sqrt.py` | _(undescribed)_ |
| `measure_smax_sqrt_40000.py` | _(undescribed)_ |
| `mod4_probe.py` | _(undescribed)_ |
| `nu2_fast.py` | Exact nu2(n)=#{d in [2,n-1]:T(n,d)=1} via 2-adic submask-XOR DP, O(n^2), cross-checked against brute-force submask enumeration (PASSED). The authoritative fast oracle the sequence analysis used. |
| `oracle_fold_verify.py` | Independent oracle: builds Phi_n explicitly from Pascal binomials mod 2 (no Lucas shortcut) and computes wt(Phi_n h). Validates brute.py's Lucas-submask shortcut: agrees up to +/-1 (floor-at-2 convention) for every n in 2..80. Exact arithmetic. |
| `pattern_S_analyze.py` | Extracts S(n) deviation sequence from endpoint-density data; sign/magnitude/sqrt-analysis and recurrence checks. |
| `pattern_S_clt.py` | _(undescribed)_ |
| `pattern_S_generic.py` | KEY: bounds |
| `pattern_autocorr.py` | Initial autocorrelation probe of nu2/n residual (superseded by pattern_autocorr2 and pattern_longlag). |
| `pattern_autocorr2.py` | Effective-sample test via sliding-window means of nu2/n residual; found positive autocorrelation inflator ~6-11x (later shown to be drift/generic, not primes-specific). |
| `pattern_autocorr_control.py` | _(undescribed)_ |
| `pattern_cell_density.py` | KEY: fold-cell density nu2/(n-2) ~ 1/2 for primes and random, collapses for Thue-Morse; the clean separator showing primes are generic-good. |
| `pattern_collapse_map.py` | Maps fold-collapse boundary across inputs (random, thue-morse, periodic, anti-dyadic, rare-defect, sparse); shows sparsity/proximity-to-kernel drives collapse. |
| `pattern_density1.py` | _(undescribed)_ |
| `pattern_detrend.py` | Detrending control: local running-mean removal collapses long-lag autocorrelation of nu2/n to ~0, proving persistence is secular-drift artifact. |
| `pattern_dump_nu2.py` | _(undescribed)_ |
| `pattern_gradient.py` | Gradient probe: collapse tracks 1-density of h (sparse<=0.15 collapses, >=0.2 good), not 2-automaticity per se. |
| `pattern_longlag.py` | Long-lag autocorrelation and correlation-time of nu2/n residual; reported tau~8 which detrending showed to be drift artifact. |
| `pattern_primes_largeN.py` | Confirms primes' |
| `pattern_primes_vs_random.py` | Detrended autocorrelation comparison primes vs random iid h at same N; showed short-lag persistence is fold-generic, not a prime fingerprint. |
| `pattern_residue.py` | _(undescribed)_ |
| `pattern_tail.py` | Density/lower-tail of nu2/n; shows tail density dies to 0 (only fixed violating n), and uniform |
| `pattern_var.py` | _(undescribed)_ |
| `pattern_var_exponent.py` | Measures variance-decay exponent of nu2/n over [N/2,N) (~N^-1, ideal rate) and self-similarity corr(nu2(2n)/2n,nu2(n)/n) ~0.21 primes. |
| `probe2.py` | _(undescribed)_ |
| `probe_excess_struct.py` | _(undescribed)_ |
| `probe_increments.py` | _(undescribed)_ |
| `probe_nu2.py` | _(undescribed)_ |
| `reconcile_nu2.py` | Reconciles the three fold-weight routes (direct submask, explicit Pascal matrix, SOS zeta) to a single floored-at-2 convention and asserts exact agreement. Uses brute.py and lib.supply_fold. Validated on n=20,50,100,200,400. |
| `refute_actual_fold.py` | _(undescribed)_ |
| `refute_random_pointwise.py` | _(undescribed)_ |
| `refute_random_pointwise_run.py` | _(undescribed)_ |
| `refute_runner.py` | _(undescribed)_ |
| `residue_probe.py` | _(undescribed)_ |
| `run_refute_scripts.py` | _(undescribed)_ |
| `s_growth.py` | _(undescribed)_ |
| `scholar_intersection_formula_verify.py` | Scholar's machine verification of the load-bearing down-set intersection formula (M_d ∩ M_{d'} = M_{d∧d'}, |
| `validate_brute.py` | Measures brute.py against the three worked examples in problem.md. Establishes: (b) nu2(4000)=0.4938 matches stated 0.4933 within 3 cells; (c) min nu2/w=0.597@105 does NOT reproduce stated 0.7049; (a) samplied nu2/n range has outliers. Also confirms brute vs floored-canonical differ by <=1 (floor-at-2). |
| `verify_brute.py` | _(undescribed)_ |
| `verify_candidate2_refutex.py` | Negative-control oracle for refuted approach walsh-subset-sum-fold-structure: enumerates balanced (weight floor(n/2)) strings for n=8,16 (exhaustive) and subsamples n=24, computing wt(Phi_n x) via lib.supply_fold.s_sos, to show the fold kernel contains maximally-weighted strings (wt=0) and near-kernel balanced strings can have tiny fold weight. FIRST EXECUTED now: min wt = 0 at n=8,16 (kernel even-alt generators 1010..), 2 at n=24 (non-kernel witness 111111111111000000000000). Establishes no Phi-alone structural bound over balanced inputs exists; confirms closed-door obstruction. Capture: code/out/verify_candidate2_refutex.captured.txt. |
| `verify_excess_identity_brute.py` | _(undescribed)_ |
