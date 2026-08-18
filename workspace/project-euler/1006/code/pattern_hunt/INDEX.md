# Index — code/pattern_hunt

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `analyze_exact_new.py` | Exact finite recurrence survey for stored integer sequences; solves rational homogeneous recurrences and reports Berlekamp–Massey behavior modulo several moduli, without claiming global validity. |
| `analyze_existing_sequences.py` | Exact inspection of stored PE1006 sequences: count/c1/Lmin identities and small linear-recurrence attempts; reports first counterexamples without altering solution. |
| `audit_sequences_independent.py` | Fresh schema-aware exact audit of every compact integer sequence artifact under code/out; separates index/value columns, tests exact rational recurrences, named structural laws, and cross-sequence affine/difference/modular relations. |
| `boundary_subseqs.py` | Extracts Fibonacci-boundary subsequences (Psi at k=F_m-1, F_m, F_m+1) from recorded tables for OEIS/sequence tools; superseded by the established directive-1 autocorrelation route. |
| `check_R_runs.py` | Analyzes run structure of the right-special factors R_k (constant-V runs of length 2/3) and S1(k) noise; writes code/out/s1_res.txt and vR_res.txt. |
| `check_c1_weight.py` | Fresh brute verification of c1(k)=1+floor(k/phi^2), the two-weight distribution {floor,ceil(k/phi^2)}, and c0=(k+1)-c1 for k=1..100. |
| `check_corr_translation.py` | Tests translation-invariance of factor-set pair-correlation C(i,j); shows it holds only at k=F_n-1, refuting lag-sum reduction at general k. |
| `check_digit_excess.py` | Computes the digit-excess staircase C(k)=len(Psi(k))-(2k-1) exactly via the validated recurrence pipeline up to k=3000, finding the transition points (24,257,2569); confirms this is a decimal-length artifact, not a modular regularity, so a dead end. |
| `check_directive1.py` | Verify directive-1 pair-correlation/autocorrelation formula vs brute exact Psi at k=F_n-1 (n=2..7): brute==rot==corr==exact. |
| `check_directive1_big.py` | Extend directive-1 verification to n=2..12 (k up to 232): rotation set == brute factor set, autocorr formula == rotation Psi. |
| `check_dj_oeis.py` | Verifies the S1 jump coefficient d_j = (S1(s_j+1)-S1(s_j))/10^{s_j} equals OEIS A019587 (left budding) over all 1145 V-runs, exact arithmetic. |
| `check_dj_structure.py` | Extracts and verifies the exact S1 within-run jump structure S1(s_j+1)-S1(s_j)=d_j*10^{s_j}, flat on [s_j+1, s_{j+1}-1], for all V-runs k=1..3000; writes dj_raw.txt / dj_mod.txt. |
| `check_even_minus_structure.py` | _(undescribed)_ |
| `check_ext_recurrence.py` | Verifies the right-extension (Sturmian) recurrence Psi(k+1)=100Psi(k)+100V(R_k)^2+20S1(k)+J(k) exactly k=1..40 against the string oracle; writes code/out/ext_recurrence.txt. |
| `check_ext_recurrence_400.py` | Verifies the mod-M right-extension recurrence and J(k)=c1(k+1) for k=1..400, plus Toeplitz probe; writes code/out/extrecur_res.txt. |
| `check_f20_falsification.py` | _(undescribed)_ |
| `check_fib_boundary_deviation.py` | _(undescribed)_ |
| `check_leading_block_c1.py` | Pins exact range k=1..137 where leading block floor(Psi/10^(2k-2))==c1(k); first failure k=138. Falsification record. |
| `check_leading_counts.py` | Clean recomputation of lead-1/lead-0 factor counts (k=1..30). |
| `check_lmin.py` | Early probe: Lmin vs floor(phi^2 k) and A344953; superseded by verify_lmin_formula.py. |
| `check_mod100_boundary.py` | _(undescribed)_ |
| `check_mod100_indep.py` | Independent attack on the mod-100 identity Psi(k)=c1(k)=1+floor(k/phi^2) mod 100 via the validated recurrence pipeline; confirms it holds k=1..3000 and fails at mod 1000 from k=2 (falsification boundary). |
| `check_position_balance_attack.py` | _(undescribed)_ |
| `check_position_balance_new.py` | _(undescribed)_ |
| `check_psi_digitlen.py` | Tests decimal-length conjecture len(Psi(k))==2k-1; refuted at k=24. Falsification record only. |
| `check_psi_leading_digits.py` | Tests leading-digit conjecture floor(Psi/10^(2k-2))==c1(k); refuted at k=138. Falsification record only. |
| `check_run_density.py` | Checks V(R_k) run-gap densities (3s ~ 1/phi, 2s ~ 1/phi^2) signalling the Sturmian/Wythoff structure. |
| `check_run_sequence_exact.py` | _(undescribed)_ |
| `check_runsum_increment.py` | Verifies the within-run Psi recurrence increment is closed-form in (s_j, L_j, V_j, A_j, d_j) over all proper V-runs (exact), completing the S1 structure analysis. |
| `check_s1_inrun.py` | First probe of S1 within V-runs; refuted the naive 'S1(k+1)=10*S1(k)' and left-append conjectures — records the negative result. |
| `check_s1_leftappend.py` | Attacks the left-append conjecture for S1 within V-runs; refuted (holds only for first ~12 runs), kept as a recorded dead end. |
| `check_s1_runstructure.py` | Verifies S1 is constant on [s_j+1, s_{j+1}-1] of each V-run (exactly two S1 maximal runs per V-run) and reports the S1 structure; supports the d_j=A019587 finding. |
| `check_small_moduli.py` | Probes Psi(k) mod small moduli via the validated right-extension recurrence to hunt for exact low-modulus cross-check regularities beyond the mod-100 one; finds only mod 4/25/100 carry the c1(k)=1+floor(k/phi^2) structure, rest noise-flat. |
| `check_toeplitz_defect.py` | Scans the pair-correlation Toeplitz defect for k=1..400: verifies |
| `check_weight_dist.py` | Tabulates length-k Fibonacci subword counts by weight; confirms exactly two weights floor/ceil(k/phi^2). |
| `check_wythoff_balance_final.py` | _(undescribed)_ |
| `check_wythoff_deviation.py` | _(undescribed)_ |
| `check_wythoff_deviation2.py` | _(undescribed)_ |
| `check_wythoff_gaps.py` | Probe of the V-run gap structure; verifies starts match floor(j*phi^2) and gaps lie in {2,3} plus cross-checks c1(10^18) via integer sqrt. Superseded by check_wythoff_gaps2.py which is more robust. |
| `check_wythoff_gaps2.py` | Verifies V-run start positions equal floor(j*phi^2)=A001950 (upper Wythoff) exactly for j=1..1146 and that the run-gap sequence takes only values {2,3} (the infinite Fibonacci word rewritten {2,3}, OEIS A282162/A076662). |
| `current_sequence_tools.py` | Reads stored integer sequence artifacts and prints exact prefixes and difference diagnostics for the current structural survey. |
| `digit_probe.py` | Probes digit-excess at targeted larger k to see whether excess (digits(Psi)-(2k-1)) ever reaches +2; part of the digit-length dead end (refuted as a closed form). |
| `digit_step_wide.py` | Tests digit-excess step pattern over k=1..2000 to find first falsifier of the {0 for k<=23, 1 for k>=24} claim; part of the digit-length dead end. |
| `digit_structure.py` | _(undescribed)_ |
| `digit_thresholds.py` | Binary-searches the exact digit-excess transition points of C(k)=len(Psi(k))-(2k-1); part of the digit-length dead end. |
| `direct_sequence_hunt.py` | Direct exact finite analysis of supplied Psi, c1, Lmin, d_j, and Toeplitz-defect sequences; reports differences, bounded rational linear recurrences, known-formula falsifiers, and zero-defect indices. |
| `extend_boundary_subsequence.py` | _(undescribed)_ |
| `extend_requested_patterns.py` | Efficient exact extension of c1, Psi mod 100, strict-next-Fibonacci Lmin, and V/run-start floor(j phi^2) regularities; reports first falsifiers and boundary values. |
| `extend_sequence_checks.py` | Independent exact recheck of c1 floor law, least-prefix Fibonacci formula, and Toeplitz-defect zero locations from stored tables. |
| `extract_subseqs.py` | Extract subsequences Psi mod M at k=F_m-1/F_m/F_m+1; superseded. |
| `extract_vr_runs.py` | Extracts V(R_k) run starts, gaps and values to code/out/vr_rungaps.txt and vr_runvals.txt for OEIS/sequence analysis. |
| `factor_route_c1_lmin_fresh.py` | Fresh exact factor-window audit of c1(k)=1+floor(k(3-sqrt(5))/2) and strict-next-Fibonacci Lmin, through K=200000; avoids floating point. |
| `final_new_sequence_audit.py` | Final independent exact audit of every compact integer sequence artifact in code/out; tests exact low-order recurrences and recorded floor/Fibonacci/Wythoff laws, reporting first falsifiers. |
| `fresh_c1_lmin_check.py` | Fresh independent extension check: compares c1's Fibonacci-word prefix-count law with the exact irrational-slope floor formula through 10000, and checks Lmin against the strict-next-Fibonacci formula by plain substring scanning through 10000. |
| `fresh_sequence_tool_audit.py` | Fresh exact audit of c1, Lmin, Toeplitz defects, run starts/gaps, and Psi residues; reports exact terms, recurrence diagnostics, and first falsifiers. |
| `gen_sequences.py` | Generate PE1006 integer sequences (Psi exact 1..25, Psi mod M 1..400, Lmin 1..400); writes code/out/*.txt. |
| `independent_compact_audit.py` | Independent exact recurrence audit of compact integer sequence artifacts; confirms no genuinely new low-order recurrence candidate. |
| `independent_nonpsi_hunt.py` | Independent exact finite-range checks of leading-1 factor counts and first-occurrence prefix lengths; direct factor extraction through k=1000, used as evidence for conjectured c1 and Lmin formulas. |
| `independent_psi_patterns.py` | Independent exact/residue tests for affine, Fibonacci, decimal-shift, Fibonacci-boundary, and low-order linear recurrence hypotheses; reports first falsifiers from stored Psi terms. |
| `independent_tabular_survey.py` | Compact exact survey of psi, c1, lmin and run/gap tables; checks recurrences and deliberate counterexamples. Its output is diagnostic evidence for the tabulated claims. |
| `inspect_requested_sequences.py` | Exact survey of psi, c1, ext-recurrence, and V-run sequences; tests bounded recurrence conjectures, formulas, and local OEIS evidence without full-size Euler evaluation. |
| `inspect_run_schema.py` | _(undescribed)_ |
| `inspect_tabular.py` | _(undescribed)_ |
| `mech_words.py` | _(undescribed)_ |
| `pattern_verify_full.py` | Verifies the right-extension recurrence mod M=101001001 for k=1..199, J(k)=c1(k+1)=1+floor((k+1)/phi^2), and V(R_k) run lengths in {1,2,3} by brute factor enumeration. |
| `pattern_verify_runs.py` | Independently re-verifies the right-extension recurrence Psi(k+1)=100Psi(k)+100V(R_k)^2+20S1(k)+J(k) (k=1..24 exact) and computes V(R_k) run structure by fresh brute factor enumeration. |
| `probe_digitlen_bisect.py` | Bisects the C(k)=len(Psi(k))-(2k-1) transitions using the sliding-window exact route; superseded by check_digit_excess.py which uses the recurrence pipeline. |
| `probe_digitlen_bisect4.py` | Pins only the digit-length 3->4 transition of the excess staircase; part of the digit-length dead end. |
| `probe_digitlen_structure.py` | _(undescribed)_ |
| `probe_digitlen_transitions.py` | _(undescribed)_ |
| `probe_exact_psi_extended.py` | _(undescribed)_ |
| `probe_noise.py` | Statistical probe of residue sequence (autocorr, chi2, collisions): noise-flat. |
| `probe_weak_leading_digits.py` | _(undescribed)_ |
| `push_lmin_k6764.py` | Third standalone Lmin verifier k=1..6764. |
| `run_gap_check.py` | _(undescribed)_ |
| `run_sequence_tools_current.py` | Extracts the already-computed compact integer sequences from code/out for exact sequence-tool analysis. |
| `sequence_audit_requested.py` | Exact disk-based audit of the requested psi, c1, lmin, dj, and Toeplitz-defect sequences; fits rational homogeneous recurrences through order 12 and reports exact candidate formulas with first falsifiers. |
| `sequence_report.py` | Exact artifact survey of psi, c1, counts, Lmin, and recurrence candidates; computes first falsifiers without published-sequence lookup. |
| `sequence_tools_new_run.py` | Fresh exact and modular sequence survey over stored PE1006 sequences: SymPy simple-recurrence search, Berlekamp–Massey orders, and finite differences. It reports only supplied-term evidence, not proofs. |
| `survey_sequences.py` | Independent artifact survey: tests Psi mod-100/mod-1000, Lmin, factor counts, and run-gap conjectures on genuine recorded terms; reports first falsifiers. |
| `targeted_relations.py` | Independent exact checks of candidate relations: Psi residues versus c1 modulo 100/1000, c1 differences, dj recurrence temptations, and V-run gap structure. |
| `verify_R_runs_wythoff.py` | Verifies exactly (k=1..3000) that the right-special factors' constant-value runs start at the upper Wythoff numbers s_j=floor(j*phi^2), left zero-padding within runs, run lengths in {1,2,3}, S1-run containment, J(k)=1+floor((k+1)/phi^2), and the exact Psi recurrence; also detects Psi(k) digit-palindromes. Writes code/out/r_runs_wythoff.txt, s1_exact.txt, vR_exact.txt. |
| `verify_audit_conclusions.py` | Independent second-route exact verification of the positive stored formulas and first cross-sequence falsifiers found by audit_sequences_independent.py. |
| `verify_boundary_recursion.py` | _(undescribed)_ |
| `verify_boundary_recursion_q.py` | _(undescribed)_ |
| `verify_c1_formula.py` | Verifies c1(k)=1+floor(k/phi^2) three independent routes k=1..400; writes code/out/c1_terms.txt. |
| `verify_lmin_formula.py` | Check Lmin(k)=k+NextFib(k)-1 for k=1..2583. |
| `verify_lmin_formula_f20.py` | Primary Lmin verifier k=1..6764 via bit-mask; helper-driven from code/lib/fibword.py. |
| `verify_lmin_formula_indep.py` | Independent cross-check of Lmin formula on sampled k. |
| `verify_psi_mod100_c1.py` | Verifies Psi(k)==c1(k)=A189663 (mod 100) for k=1..3000 by validated exact pipeline; tests mod-1000 falsification boundary. Load-bearing new regularity. |
