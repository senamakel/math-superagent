# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `_run.sh` | Placeholder runner stub (0 bytes). Superseded by `code/lib/capture.py` (Directive 23): the `> file` truncation pattern is fixed at the runner, never per script. Do not reintroduce a `> file` capture anywhere — use `python3 -m lib.capture --target … -- …` (see Capture rule above). |
| `_run_sws.sh` | _(undescribed)_ |
| `_run_sws3.sh` | _(undescribed)_ |
| `abgs_m4_check.py` | Reproduces the ABGS 2011 Section 7 m=4 consecutive-prime-pair counts (16574, 22521, 22520, 16715) and derives the switch/equal split (57.5%/42.5%, ratio ~1.36). Supports claim abgs-mod4-nonuniform-measured. RAN clean. |
| `anf_dictionary_check.captured.txt` | Captured stdout of anf_dictionary_check.py: ANF/Möbius dictionary verified exact — T(n,d) == ANF coefficient a_d for all n=3..40, all d, with all-ones (kernel) negative control showing ANF support size 1. Establishes nu2(n) = # nonzero ANF coeffs of reversed window among indices 2..n-1. |
| `anf_dictionary_check.py` | Checks the ANF/Möbius dictionary for approach anf-mobius-reed-muller: that T(n,d)=XOR over submasks of d of h[n-1-d+o] equals the ANF coefficient a_d of the reversed window, for n=3..40, with an all-ones negative control. RAN CLEAN: 0 mismatches over n=3..40, all-ones control PASS. Capture: code/out/anf_dictionary_check.captured.txt. |
| `anf_second_moment_check.captured.txt` | Captured stdout of anf_second_moment_check.py: exact Phi-alone second-moment identity E[S(n)^2]=(n-2)+sum_{d!=d'}(1-2p)^{ |
| `anf_second_moment_check.py` | Checker for the fold-second-moment-krawtchouk adopted line: verifies E[eps_d eps_d'] = (1-2p)^{ |
| `averaged_mean_capture.txt` | _(undescribed)_ |
| `averaged_push_capture.txt` | _(undescribed)_ |
| `avg_nu2_out.txt` | _(undescribed)_ |
| `avg_push_capture.txt` | Combined verbatim capture of Tasks A/B/C averaged-push results, written by the three task scripts. |
| `avg_supply_note.md` | Measurement note for averaged SUPPLY: prime mean of nu2(n)/n ~0.49 rising with variance halving (0.0127->0.00032), all-ones and Thue-Morse controls decaying to 0, and the honest report of the convention collision (literal suffix is 0 for all n; the fold is the operative object). Empirically supports G-mean-linear; not a proof. |
| `bacher_pascal_verify.py` | Verifies Bacher's mod-2 symmetric-Pascal determinant formulas (det P(2n)=(-1)^n, det P(2n+1)=(-1)^(n+ds)) all match. Fold Phi_n: rank computed = n-1 for n=2..20, NOT n-3 and NOT nullity=1-rank... rank is full row rank (n-1), nullity 1, so "rank=n-3" is FALSE as coded — the Phi_n construction here differs from Bacher's symmetric Pascal. One-line int() format fix applied and it ran clean. |
| `candidate2_basis_check.py` | Checks whether the fold's down-set (Möbius/zeta) basis equals the Walsh/Fourier basis that the U²-norm and Gowers inverse theorem concern — the crux of candidate gowers-u2-nilsequence-uniformity |
| `chebyshev_oracle_verified_N40000.txt` | Captured output of code/averaged/chebyshev_verify_oracle.py at N=40000 (canonical-oracle-only verification, directive 13), REWRITTEN this run by the fixed script. PRIMES: mu_N (Primes)=0.49965810, s2_N=0.000093360697; s2_N decay 0.00078328@4000→0.00009336@40000; min nu2/n over [X,40000] = 0.33962264 (X=50), 0.45995045 (X=1000), 0.48502304 (X=10000), 0.49011407 (X=30000); dip-sparsity counts full-range {n in [50,N]: nu2/n<c}: c=0.30→0, 0.35→1, 0.40→3, 0.42→10, 0.45→51, 0.48→354 — all [10000,N] and [30000,N] windows 0 for every c in 0.30..0.48. New data-path lines: first 8 bits of h fed to STAGE1 = 11101010 (len=40001) == canonical prime h 11101010; ARRAY-assert after STAGE1 PASSED (nu2[53]==18, nu2[64]==27, nu2[4000]==1975, mu_4000 from produced array = 0.497259 within 0.01 of 0.4977). Controls at N=4000 now correctly labelled: mu_N (ALL-ONES)=0.00000000 (vacuous), mu_N (THUE-MORSE)=0.06414572 (fails density-1, frac below 0.30 = 0.982536, M falling) — the pre-edit capture's hardcoded "mu_N (Primes)" labels inside the control blocks are GONE. Entry guard passed. All numbers measured, not proved. |
| `chebyshev_sanity.txt` | _(undescribed)_ |
| `chebyshev_second_moment_N40000.settles.md` | Human note stating what the N=40000 capture settles (written after this run re-executed the 0-byte script): primes show a measured density-1 tail signal at 40000 (last quarter all >= 0.49, min rising 0.3396@50 -> 0.4901@30000), exact variance s2_N decaying ~1/N (9.34e-5 @40000, std 0.0097), Chebyshev bound >=99% of n have nu2/n >= 0.40; negative controls all-ones (vacuous) and Thue-Morse (fails) both behave; fair-model ratio s2/(1/4N) ~13-15. Labels everything measurement-not-proof per GOAL rule. |
| `chebyshev_second_moment_N40000.txt` | Exact captured output of code/averaged/chebyshev_second_moment.py at N=40000 (JOB 1, tool_builder, nproc=28, wall 262s): prime M(N) rising to 0.499658 at N=40000, dip sparsity (zero n below 0.45 in the last half/tail), exact variance s2_N decaying 7.83e-4 (N=4000) to 9.34e-5 (N=40000), plus the fair-variance-ratio table: meas s2*4Np ~12.5..14.9 vs theo_decoupled (1/N)sum(n-2)/(4n^2) *4Np ~6.58..8.88, meas/theo ratio 1.90@4000 -> 1.68@40000. Entry guard passed (nu2(53)==18, nu2(64)==27, mu_4000 within 0.01 of 0.4977). All numbers measured, not proved. |
| `chebyshev_separation_note.md` | Claim block mean-bounded-not-density1: the explicit two-point separation (mean exactly c=0.49, P(a≥c)=0.325 every N) showing a bounded Cesàro mean does NOT force a density-1 set — answers directive 3(c). Anchors the variance-vanishing route (s2_N→0) that does. |
| `check_levelset_identity.py` | _(undescribed)_ |
| `commands.log` | _(undescribed)_ |
| `density_model_control.note.md` | _(undescribed)_ |
| `density_model_control.txt` | Exact captured output of code/averaged/density_model_control.py (JOB 2, tool_builder). Entry guard passed; scene_header + prime M(N) 0.4394..0.4973, Thue-Morse -> 0.0641, Bernoulli(p=0.5968)/Bernoulli(0.5) trials showing the prime mean sits at the fold's generic balanced value. All measured. |
| `dip_sparsity_monotonic_fixed.txt` | Exact captured output of code/averaged/dip_sparsity_monotonic.py (JOB 4, tool_builder, N=40000 nproc=28) after fixing the worker to use fold_nu2 from lib.nu2 and adding assert_supply_guard at top. PRIMES tail [0.9N,N] dip density 0 for every c in 0.40..0.49 (largest empty-tail c = 0.49), half-window 0 except c=0.49 (density 0.0005), full-window dips confined to small n; window min full=0.339623, half=0.487947, tail=0.490344. All-ones (vacuous) and Thue-Morse (must-fail, tail dens 1.0) controls behave. All measured, not proved. |
| `dip_sparsity_real.note.md` | _(undescribed)_ |
| `directive21_exact_ratios.captured.txt` | _(undescribed)_ |
| `dyadic_extension_capture.txt` | _(undescribed)_ |
| `dyadic_extension_k25.note.md` | Claim block for the k=25 dyadic extension (directive 36): nu2(2^k)/2^k stays at 1/2 through k=25, no door-4 collapse at powers of two; status measured, scoped to the 23 dyadic sample points n=2^k, 2^k±1. |
| `dyadic_extension_k25.txt` | _(undescribed)_ |
| `dyadic_extension_k25_capture.txt` | _(undescribed)_ |
| `dyadic_stratify_by_popcount.captured.txt` | _(undescribed)_ |
| `dyadic_stratum_recheck.captured.txt` | _(undescribed)_ |
| `dyadic_stratum_recheck.note.md` | _(undescribed)_ |
| `dyadic_tool_builder_report.md` | Final tool_builder report for the two dyadic tasks: Task B corrected character identity PASS (6868/6868, spurious-sign negative control fails on 449 pairs incl. d=3) and Task A popcount stratification of S(n) showing weight is spread across strata (no low-popcount-stratum dominance), concluding the dyadic-gap-character route's amenable-region premise fails on the measured inputs. Everything labeled measured, not proved. |
| `dyadic_verify_character_identity.captured.txt` | _(undescribed)_ |
| `excess_E2_2000.txt` | _(undescribed)_ |
| `excess_E2_30000.txt` | _(undescribed)_ |
| `excess_E2_8000.txt` | _(undescribed)_ |
| `excess_diff.txt` | _(undescribed)_ |
| `excess_identity_brute.captured.txt` | Captured output of code/verify_excess_identity_brute.py at N=1000: independently verifies the core SUPPLY identity 2·ν₂(n)−(n−2) = −S(n) by the literal brute submask-XOR route (t_direct), distinct from the SOS/path. Holds for EVERY n in [2,1000], 0 mismatches, ones==fold_nu2 for all. This is the second independent route (after SOS) to the identity that grounds the whole endpoint-parity equivalence S(n)=o(n) ⟺ ν₂(n)≈n/2. |
| `excess_seq.txt` | _(undescribed)_ |
| `fair_model_exact.txt` | _(undescribed)_ |
| `fair_prefix_variance_40000.runlog` | _(undescribed)_ |
| `fair_prefix_variance_40000.txt` | _(undescribed)_ |
| `fair_prefix_variance_N10000_6trials.txt` | _(undescribed)_ |
| `fair_prefix_variance_N40000_2trials.txt` | _(undescribed)_ |
| `fair_prefix_variance_N40000_5trials.txt` | _(undescribed)_ |
| `fair_var_run.log` | _(undescribed)_ |
| `fair_variance_at_40000.note.md` | Directive-18 note and claim block for fair_variance_at_40000.txt: the correct prefix-variance null is log(N)/(4N) (one-line derivation), Ratio B = s2_N·4N/log N = 1.3155 at N=40000 (~32% excess), the per-doubling decrement column showing the excess PERSISTS but the limit (1 vs constant above 1) is UNDETERMINED, and the c=None deep-tail dip result with all-ones/Thue-Morse controls breaking at c=0.40. Status measured. |
| `fair_variance_at_40000.txt` | _(undescribed)_ |
| `fair_variance_independent_verify.txt` | _(undescribed)_ |
| `floor_convention_note.md` | Records that the nu2/n pointwise dip below 0.42 at n=53 is robust across floor conventions (min 0.3396-0.3585), refuting R-finite-verified (claim of >=0.42 for 50<=n<=4000). |
| `fold_alln_theorems.captured.txt` | _(undescribed)_ |
| `fold_second_moment_capture.txt` | Capture of the fold-second-moment-krawtchouk first step: A_2=O(n) (exponent 0.455), F_n(1-2p)=O(n) at p=0.585 (condition C holds, F_n~n), exact identity checks pass (with the var(S)=F_n-E[S]^2 correction), Krawtchouk diagonalization exact, and all-ones/Thue-Morse/single-1 controls correctly fail the iid model. |
| `g_mean_linear_grounded.md` | _(undescribed)_ |
| `g_run_telescope_negctrl.settles.md` | Settlement note and corrected fenced claim g-run-telescope-verified per directive 26, with the negative-control result (3-valued boundary gives 438 mismatches) and the honest bearing (telescoping reorganises the fold but does not by itself bound wt). |
| `g_run_telescope_verify.captured.txt` | Atomic-captured output of code/gfold/g_run_telescope_verify.py (claims C1 down-set run structure and C2 telescoping identity of the SUPPLY fold), re-run THIS run via the Directive-23 atomic runner `python3 -m lib.capture --target … -- python3 code/gfold/g_run_telescope_verify.py`. Exit 0, elapsed 570.05s (reported by the runner, this run). All checks PASSED: C1 d=0..16384 (16385 values, brute submask enumeration); C2/prime telescoping brute 52275 (d,pos) pairs + prefix-XOR full 1654885 pairs; C2/random 30 trials brute 1568250 + prefix 49646550 pairs. Previously 0 bytes (a failed `> file` capture — see Capture rule above); now a genuine verified capture. Settles claim g-run-telescope-verified — the machine grounding of the adopted dyadic-gap-character-correlation reduction step and the verification contract for lib/submasks.py. Exact arithmetic; not a proof of SUPPLY. |
| `g_run_telescope_verify_negctrl_full.captured.txt` | _(undescribed)_ |
| `goals_attempt2_status.md` | Attempt-2 (goals) status: records the two operator deliverables — the DIRECTIVES.md call-site answer (formatter label defect, not a data-path error) and the Ratio B extension to N=80000 — with the honest undetermined-limit statement, updated records, and verification notes. |
| `goals_attempt_status.md` | _(undescribed)_ |
| `guard_failure_report.md` | RESOLVED. Records the hard guard failure found while preparing the four SUPPLY jobs: assert_supply_guard asserted nu2(4000)==1976 but the canonical oracle returns 1975 (d in [2,n-1] convention); four independent routes agree. The guard has been fixed to assert exactly the operator's spec (nu2(53)==18, nu2(64)==27, primes mu_4000 within 0.01 of 0.4977) and the erroneous hard n=4000==1976 constant removed. All four jobs (chebyshev_second_moment_N40000.txt, density_model_control.txt, kernel_component.txt, dip_sparsity_monotonic_fixed.txt) now pass and have been re-run. |
| `input_strictness_capture.txt` | _(undescribed)_ |
| `inventor_identity_check.py` | _(undescribed)_ |
| `kernel_component.txt` | Exact captured output of code/averaged/kernel_component.py (JOB 3, tool_builder). Verifies ker Phi_n = span(even-alt,odd-alt) (rank n-2, nullity 2) for n=8..128, wt(h)/n = 0.6250..0.6875, dmin/n = 0.125..0.376 (att. even-alt/all-ones). Mislabel fixed: 0.597 was an unrelated nu2/w figure; the sentence now cites the script's own wt(h)/n 0.6250..0.6875. |
| `kernel_component_capture.txt` | _(undescribed)_ |
| `kstar_budget_explicit.captured.txt` | _(undescribed)_ |
| `kstar_cum_floor18.captured.txt` | Independent exhaustive 2^n capture confirming the cumulative (nested) correlation-order budget K*(n)=floor(n/2) for n=2..18, extending the catalogued range to n=17,18; contradicts the imported ceil(n/2) budget table. |
| `kstar_exact.captured.txt` | _(undescribed)_ |
| `kstar_resolve.captured.txt` | _(undescribed)_ |
| `kstar_settle.captured.txt` | _(undescribed)_ |
| `kstar_structural_capture.txt` | _(undescribed)_ |
| `linear_supply_by_weight.txt` | _(undescribed)_ |
| `linear_supply_independent.txt` | _(undescribed)_ |
| `nu2_4000_reconcile.captured.txt` | _(undescribed)_ |
| `nu2_extended.txt` | _(undescribed)_ |
| `nu2_over_w_resolved.md` | Settles problem.md's UNVERIFIED ν₂/w row: min over n∈[100,2000] is 0.597 at n=105 (both gap conventions); the quoted 0.7049 is discredited. |
| `nu2_primes_xor_40000.json` | _(undescribed)_ |
| `nu2_terms.txt` | _(undescribed)_ |
| `oracle_validation_report.md` | _(undescribed)_ |
| `orderk_correlation_capture.txt` | _(undescribed)_ |
| `orderk_def_resolve.txt` | _(undescribed)_ |
| `orderk_oracle_check.txt` | _(undescribed)_ |
| `pattern_D_terms.txt` | _(undescribed)_ |
| `pattern_S_terms.txt` | _(undescribed)_ |
| `pattern_finder_INDEX.md` | _(undescribed)_ |
| `pattern_finder_deliverable.md` | Pattern-finder's core deliverable: the fold-excess fluctuation S(n)=(n−2)−2ν₂(n) is a non-random-walk (corr(S,S⁺¹)≈0, white increments, ACF1(D)→−1/2, higher lags vanish) giving var(S)=O(n), the density-1 SUPPLY input; discriminates good inputs from the random-walk collapse witnesses by corr(S,S⁺¹) not ACF1. Exact over n≤40000; infinite-n whiteness is an open conjecture. |
| `pattern_finder_deliverable_2.md` | Pattern-finder deliverable 2: exact and measured structure of the ν₂/S sequence from canonical nu2_primes_xor_40000.json — the white-noise law S=√n·Z reconciles corr(S,S_{n+1})=0 with AC1(dS)=-1/2, confirms OEIS miss/no-recurrence, measures the second-moment plateau E[S²]≤C·n (C≈15, no drift) and finite exceptional sets, and independently corroborates the per-scale g=0 (switch-density) dominance that blocks weaker-input refinements. Recommendation: the plateau is the density-1 input; the open step is the unconditional second-moment bound (A) for the prime string, which the data shows is fold-generic and not prime-specific. |
| `pattern_finder_deliverable_3_fold_genericity.md` | Pattern-finder consolidated deliverable: every measurable regularity of nu2 is fold-generic including the last 'prime-specific' signal (dip sparsity), which matched random strings reproduce. Records the exact facts (white-noise, second-moment plateau ~1, finite exceptional set), the OEIS miss on nu2(2^k), and the open barrier E[S^2]=O(n) for the specific prime string. |
| `pattern_finder_deliverable_5_mod4_switch_bias.md` | _(undescribed)_ |
| `pattern_finder_deliverable_6_kstar_budget.md` | _(undescribed)_ |
| `pattern_finder_independent_audit.md` | Independent pattern-finder audit of the SUPPLY ν₂ data from the canonical JSON (with corrected index i==n, all guards verified): reproduces the white-noise law, second-moment plateau, finite exceptional sets, and per-scale g=0 (switch-density) dominance, confirms OEIS miss / no-recurrence / no self-similarity, and concludes every ν₂ regularity is fold-generic — no prime-specific signal, bounding the GOAL hypothesis that Φ does work the switch-density form cannot see. |
| `pattern_fourth_moment_upgrade.md` | Pattern-finder deliverable 4: measured E[Z^4]≈2.95 / E[S^4]≈3n^2 plateau and pointwise max S^2/n≤14.55 — the exact quantitative input that upgrades density-1 SUPPLY to finite-every-exceptional-set (pointwise) SUPPLY. Fold-generic. |
| `pattern_normalized_white_noise.md` | Pattern-finder deliverable: the prime fold weight's normalized fluctuation Z(n)=S(n)/√n is measured white noise with E[Z²]=1 and subgaussian tail over n=3..40000, explaining the reconciliation of E[S²]≈n with corr(S(n),S(n+1))≈0, and showing ν₂/n→1/2 with rate 1/2√n — the second-moment/subgaussian content that upgrades density-1 SUPPLY (Chebyshev) to finiteness of exceptional sets. Measured conjecture, not a proof. |
| `pattern_nu2_exact.txt` | _(undescribed)_ |
| `pattern_nu2_terms.txt` | _(undescribed)_ |
| `pattern_nu2_verified.json` | _(undescribed)_ |
| `pattern_var_captured.txt` | First executed capture of pattern_var.py: per-N mean μ_N and variance σ²_N of ν₂(n)/n for the primes up to N=4000, with a 5-point cross-check of the two independent ν₂ routes (all diff=0). Shows the empirical variance decaying (tail-only 7.78e-04 at N=500 → 9.11e-05 at N=4000). |
| `pattern_var_note.md` | _(undescribed)_ |
| `prefix_variance_constant_check.note.md` | _(undescribed)_ |
| `prefix_variance_constant_check.txt` | _(undescribed)_ |
| `prefix_variance_null_40000.txt` | _(undescribed)_ |
| `push_pv_run.log` | _(undescribed)_ |
| `r_finite_verified_contradiction.md` | Records the contradiction between the settled rung R-finite-verified (ν₂/n≥0.42 for all 50≤n≤4000) and exact computation finding 10 counterexamples confined to [50,274]. Carries claim r-finite-verified-contradicted. |
| `ratio_b_d21_finding.md` | Directive-21 correction: Ratio B (s2_N·4N/lnN) per-doubling decrement-RATIO discriminator, exact vs simple-division sets, both extrapolations (limit ~1.13 vs 1) declared neither. Records that the exact last ratio dips below 0.9 (not monotone), contradicting the rounded-set lean toward limit 1. |
| `ratio_b_directive21_final.md` | _(undescribed)_ |
| `ratio_b_extension.txt` | Capture of the PRIMES-only Ratio B extension to N=80000 (exact s_sos oracle): Ratio B = 1.297@80000, per-doubling decrements 0.051/0.032/0.024/0.021/0.019. The discriminator is the decrement RATIO; exact r_3=0.899404441, r_4=0.877780046 — final falls → modest lean toward limit ABOVE 1 (thin evidence, directive 25; the operator's rounded 0.875/0.905 are not carried). The limit (1 vs constant >1) remains undetermined. Measured, not proved. |
| `ratio_b_extension_d21.txt` | Re-captured Ratio B measurement to N=80000 with the directive-21 decrement-RATIO discriminator: per-doubling decrement ratios and both extrapolations (geometric-tail limit ~1.13 vs divergent-tail limit 1.00), neither declared. Data table matches the prior N=80000 capture; guards PASS. |
| `readcone_survey_capture.txt` | _(undescribed)_ |
| `refute_single_boundary_sweep.txt` | The consolidated refutation capture. Confirms the single established refutation (windowed G-sup-implies-switch / R-switch-equivalence false): h=e_{n-1} has nu2=n-2 (nu2/n=1.000) at zero switch density for every n=4..12, with negative control h=e_0 giving nu2=1 (sublinear). Produced by code/refute/refute_single_boundary_sweep.py. |
| `refuter_derivative_ladder_check.md` | Refuter report: the adopted derivative-ladder backbone (L1),(L4),(L5) survives engine/hand verification — a strengthened verdict, not a kill. |
| `refuter_dip_sparsity_findings.md` | Independent refutation findings on the tool_builder's dip-sparsity/M-monotonicity claim: c=0.40 dips finite {53,71,105} (n=145 exactly 0.4 is a float Fraction artifact), c=0.48 dips dense (0.112), M(N) non-monotone with 31.8% violation density, plus three fenced claims. |
| `refuter_fixed_single_one_bound.md` | Refuter note: fixed single-1 fold weight is bounded by j+1 = O(1), so the G-weak-input-strictness witness cannot be a finite sparse spike — its support must grow with n. |
| `refuter_live_structural_claims.md` | _(undescribed)_ |
| `refuter_parseval_uniform_p.md` | _(undescribed)_ |
| `refuter_powers_two_negative.md` | _(undescribed)_ |
| `research_verify_relations.py` | Machine checker for the two hand-refuted fold relations (abel neighbour relation and the four substitution rules) against the brute submask-XOR oracle; written for tool_builder to confirm both counterexamples over the full small range. |
| `rw_verify.py` | Executable oracle checker for Rampersad-Wiebe run-length theorems (n<20 sweep) and the full-cube submask-XOR zeta-transform round-trip (50 trials). FIXED this run: Theorem 9 used S(L)=L; the paper's positive integers are indexed from 0 (S(0)=1, S(1)=2, S(n)=2S(n-1)-S(n-2) => S(L)=L+1), now corrected, with the old wrong reading kept as a negative control that must fail. Verified: Thm 5 matches all n, Thm 9 matches all n, negative control fails all n, zeta round-trips 50/50. Capture: code/out/rw_verify_thm9_fixed.captured.txt. |
| `rw_verify_out.md` | Hand-verified checks of Rampersad-Wiebe structural claims plus the submask-zeta involution result, honestly labeled (executable sweep unrun). |
| `rw_verify_thm9_fixed.captured.txt` | Captured stdout of the fixed rw_verify.py: Theorem 9 (positive-integers run-length transform, Rampersad-Wiebe) now matches for EVERY n=1..19 with S(L)=L+1; negative control (pre-fix S(L)=L) fails every n; Thm 5 Fibonacci control still matches all n; submask-XOR zeta round-trip passes 50/50. Settles task reconcile-verifier-anomalies' Thm-9 part: the sum_T parameterization was right, the sequence indexing was off by one (paper indexes positive integers from 0: S(0)=1, S(1)=2, S(n)=2S(n-1)-S(n-2)). |
| `seq_S_from2.txt` | _(undescribed)_ |
| `seq_nu2_from2.txt` | _(undescribed)_ |
| `smax_report.md` | _(undescribed)_ |
| `smax_trajectory.txt` | _(undescribed)_ |
| `smax_trajectory_N1000_W2000.txt` | _(undescribed)_ |
| `smax_trajectory_N30000_W2000.txt` | _(undescribed)_ |
| `smax_trajectory_N40000_W2000.txt` | _(undescribed)_ |
| `sparse_fold_capture.settles.md` | One-page settlements statement for the sparse-input amplification result: what was run, what it settles (sparsity never caps fold weight; boundary-spike mechanism; fixed sparse strings have liminf 0 so G-weak-input-strictness witness must be growing and avoid the read-boundary drop), evidence class (exact, two oracle routes agree), honest non-proof status. |
| `sparse_fold_capture.txt` | Consolidated exact capture for sparse-input amplification of the SUPPLY fold: capacity curve Cap(n,k) (n=8,10,12), single-1 boundary amplification, and fixed-infinite-sparse family growth (powers-of-2, squares) over n in [256,4096]. Settles that sparsity never caps fold weight (even k=1 reaches n-2) while every fixed sparse string has liminf ratio 0, refining the search shape for G-weak-input-strictness. |
| `sparse_image_curve.py` | _(undescribed)_ |
| `squared_excess_order_check.py` | Draft checker for the squared-excess approach's structural facts: even symmetric differences, run structure, no singleton (so no standalone switch-sign term), distance-2 pairs are two non-adjacent singletons. Unrun; hand-check done in the approach file. |
| `supply_endpoint_density.txt` | _(undescribed)_ |
| `supply_fold_rank.final.captured.txt` | _(undescribed)_ |
| `unrun_scripts_captured.txt` | Captured output of the three formerly-unrun scripts (rw_verify, abgs_m4_check, bacher_pascal_verify) with run-status header, covering ranges, and the negative controls. Created by running each with python3 from /workspace. |
| `verify_approach_premises.py` | _(undescribed)_ |
| `verify_candidate2_refutex.captured.txt` | First-executed capture of code/verify_candidate2_refutex.py: exhaustive over all balanced strings at n=8 (70) and n=16 (12870), min wt(Phi_n x)=0 (the even-alt kernel generators 1010..), plus a 200-subsample at n=24 giving min wt=2 on a NON-kernel balanced string 111111111111000000000000. Negative control confirming no Phi-alone structural bound over balanced inputs (refuted approach walsh-subset-sum-fold-structure). |
| `w_switch_terms.txt` | _(undescribed)_ |
