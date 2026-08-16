# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | Workspace instructions for the code folder. |
| `analyze_roots.py` | Structural analysis of the 408 S-roots <= 10^6: mod-9 residues, digit-count histograms, repunit/power-of-10 chains, small roots. Pattern-finder reconnaissance. |
| `brute.py` | Brute-force oracle for PE 719: scans every n<=N, tests perfect squares for a digit-partition into >=2 blocks summing to the root. Reproduces T(10^4)=41333 and all statement examples (81,6724,8281,9801). Independent recursion route (is_s_number_rec) cross-checked via assertion. |
| `candidates_dfs.py` | Candidate 01 — forward DFS over digit-block boundaries with overshoot pruning; distinct independent implementation of the PE 719 split-and-sum test, reproduces all four reference T values. |
| `candidates_digitdp.py` | Candidate 02 — memoized digit-DP over (position, remaining-sum); independent implementation of the PE 719 split-and-sum test, reproduces all four reference T values. |
| `candidates_mitm.py` | Candidate 03's independent PE719 solver: meet-in-the-middle over prefixes (prefix/suffix partition-sum sets + straddle block) to test S-number status of each root. The only candidate with a completed full-size 10^12 run log: T(10^12)=128088830547982 (count 406). |
| `check_mod9.py` | _(undescribed)_ |
| `consec_pair_families_precise.py` | Pinpoints which consecutive-pair families are uniform S-root pairs. Establishes (10^k-10, 10^k-9) holds for all k>=3 and (10^k-1, 10^k) for all k>=2; generalization (10^k-10^j, +1) uniform only for k>=j+2. Measures coverage (18/408 roots <= 10^6). |
| `consec_pair_family.py` | Tests the 'suspicious partial family' of consecutive S-root pairs over the whole A038206 catalogue; shows (10^k-10^j, +1) is partial in general (fails at k=j+1), motivating the precise uniform-family analysis in consec_pair_families_precise.py. |
| `extract_seqs.py` | Extracts the first 40 square values (A104113), decade counts, and cumulative sums from the A038206 b-file; output fed to the sequence tools. |
| `f1_proof_check2.py` | Proves F1 (10^k-1, 10^k) both S-roots for all k>=2 by exact decimal identities: (10^k-1)^2=(10^k-2)*10^k+1 split [10^k-2,0*(k-1),1]; 10^{2k} split [10^k,0*k]. Verified k=2..60. |
| `f2_fresh2.py` | Fresh independent verification F1 to k=34 and F2 to k=31, boolean digit DP, no falsifier. |
| `f2_mechanism.py` | Looks for the clean block-split witness for F2 members and probes how far 10^k-10^j generalises; shows single-root and consecutive-pair uniform families start at k>=j+2. |
| `f2_proof_check2.py` | Proves F2 (10^k-10, 10^k-9) both S-roots for all k>=3 by exact decimal identities: (10^k-10)^2=10^{2k}-20*10^k+100 split [10^k-20,0*(k-3),10,0]; (10^k-9)^2=10^{2k}-18*10^k+81 split [10^k-18,0*(k-2),8,1]. Verified k=3..80. |
| `f2_splits.py` | _(undescribed)_ |
| `f2_symbolic.py` | sympy expansion confirming (10^k-10)^2=10^{2k}-20*10^k+100 and (10^k-9)^2=10^{2k}-18*10^k+81, the algebra underlying the F2 proof. |
| `families_direct.py` | Direct exact digit-partition verification (independent of the b-file) that F1=(10^k-1,10^k) and F2=(10^k-10,10^k-9) are S-root pairs for every k to 25; the check that promotes F2 from 'partial family' to a confirmed uniform-family conjecture with no falsifier found. |
| `gen_pair_families.py` | Shows (10^k-10^j, +1) consecutive pair is uniform S-root only for j=1 (=F2); fails at k=j+2 for all j>=2. Completes the family classification. |
| `mod_filter_sweep.py` | Sweeps moduli q in [2,5000] over the 406 S-roots <= 10^6 to test for a modular filter stronger than the known mod-9 rule (m≡0 or 1 mod 9). Verified negative: every restricting modulus is mod-9-based; no independent modular invariant exists. |
| `mod_probe_new.py` | Shows no modulus beyond 9 gives a stronger necessary residue filter on S-roots; mod 27/99 residues are exact lifts of mod-9 {0,1}. |
| `mod_sweep_stability.py` | Split-half stability check over the 406 S-roots deciding the mod-filter sweep thread: small multiples of 9 reproduce exactly the mod-9-consistent residue count (2/9) in disjoint halves (mod-9 exhaustive there), while the reduced residue sets on large composite moduli (720,990,1620,1980,1998) do NOT reproduce across halves, proving they are finite-sample artifacts, not filters. Closes the question of whether any cheap modulus beats mod-9. |
| `pattern_families.py` | Test self-similar closed families (powers of 10, 9-repunits, 45/55 families) over all 3200 S-roots in the A038206 b-file. |
| `pattern_families2.py` | _(undescribed)_ |
| `pattern_finder_check.py` | Independent pattern-finder check: verifies the mod-9 rule on every S-root in the 408-term and 3200-term b-files (zero violations), confirming the pruning assumption used by the solver. |
| `pattern_mod9.py` | _(undescribed)_ |
| `pattern_roots.py` | _(undescribed)_ |
| `seq_decades.py` | Extracts per-decade root counts D_k and per-decade sums of squares I_k from the b-file; labels corrected in the pattern-finder turn (cumulative sum over roots <=10^k equals T(10^{2k})). |
| `seq_extract.py` | Extracts square values, decade counts, cumulative sums, and mod-9 split from the A038206 b-file; asserts coverage (406 roots in [2,10^6], term 409 = 1005291). |
| `single_families.py` | Single-root families 10^k-j uniform S-roots only for j=1 and j=9. |
| `solution.py` | Efficient solver for PE 719: scans roots m in [2,sqrt(N)] instead of n, O(sqrt(N)); digit-partition recursion; computes T(10^12). |
| `verify_bfile.py` | Independent verification of PE 719: sums squares of S-number roots (2<=m<=isqrt(N), excluding sentinel roots 0,1) read from the OEIS A038206 b-file. Confirms T(10^4)=41333 and gives T(10^12)=128088830547982, matching solution.py. |
