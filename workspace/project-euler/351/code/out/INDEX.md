# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | Convention: code/out holds program output (sequences, logs, verification artifacts) where it was produced, separate from what a person wrote. |
| `check_library_values.py` | Library-value oracle: computes Phi(n) by a naive phi sieve and checks H(5)=30, H(10)=138, H(1000)=1177848 (statement oracles) plus Phi(10^k) k=0..8 against OEIS A064018, then prints the check anchor H(10^8) = 3·10^8·(10^8+1) − 6·Phi(10^8) = 11762187201804552 that solution.py must reproduce. Exact integer arithmetic; the final answer is anchored here. |
| `check_mod4_law.py` | Exact verification over the full 200000-term prefix of the derived mod-4 residue law: A063985(n) odd iff n mod 4 in {1,2}, H(n) mod 12 == 6 iff n mod 4 in {1,2}, Phi(n) even for n>=2, cototient parity with the c(1), c(2) boundary anomalies. First version's L4 failed and was corrected — a caught error, recorded. |
| `commands.log` | Verbatim log of the shell commands this run executed (free/nproc, python probes, etc.), for audit outside the run. |
| `diag_a064016_check.py` | Independent verification of the A063985 diagonal A(10^k), k=0..8, against OEIS A064016 by a fresh Chai Wah Wu recursion; confirms A(10^8)=1960364533634092 (anchor of H(10^8)). |
| `diag_pass2.py` | Timing diagnosis of pattern_pass2's stages over the 200000-term prefixes (which stage dominates). |
| `diag_subseq_scan.py` | Extracts and sanity-scans the uncatalogued subsequences A(3^k), A(k^2), A(2^k·3), A(2^k·5) from the stored 200000-term prefix, with growth-ratio check against 1/2-3/pi^2. |
| `dump_terms.py` | Prints exact terms from the sequence files as JSON arrays for the sequence tools (no transcription); usage: python3 code/out/dump_terms.py [nterms]. |
| `exact_rec_check.py` | Exact no-low-order-recurrence check: sympy rank/nullspace of the Toeplitz systems for orders 1..12 over a 300-term block, then any candidate recurrence tested against the entire 200000-term prefix (no constant-coefficient recurrence of order <= 12 fits H, Phi, or A063985). |
| `extract_subs.py` | Re-extracts A(2^k), A(3^k), A(k^2), A(10^k), A(2^k·3), A(2^k·5) from the stored prefix and cross-checks them against the recorded values in pe351-pattern-findings.md (integrity check, all passed). |
| `fix_mobius_verify.py` | Corrected Möbius-inversion verification of Phi(N): the old verify_mobius.py used mu[p*p::p]=0 (step p, zeroing squarefree numbers 6,10,14,15,...); this uses step p*p. Matches the totient sieve exactly at N=2,3,5,10,20,100,1000,1e5,1e8 — Phi(1e8)=3039635516365908 by both routes, closing the run's recorded MISMATCH. |
| `growth_checks.py` | Growth, oscillation and jump structure over the exact 200000-term prefixes: H(n)/n^2 -> 3(1-6/pi^2), A/n^2 -> (1/2-3/pi^2), totient-defect sign changes (756 over the prefix), largest per-term jumps. |
| `mod12_independent_check.py` | Independent verification of the mod-12 period-4 conjecture: fresh spf-sieve phi computation over n<=200000 (Route 1), elementary parity steps c(k)==k mod 2 for k>=3 (Route 2), and the full-size check H(10^8) mod 12 == 0 (Route 3). |
| `mod12_large_probes.py` | Break-attempt for the mod-12 period-4 law beyond the 2e5-term prefix: 79 exact probes of H(n) mod 12 up to n=10^8 via Chai Wah Wu's recursion (n = 10^k+r, random large n, and n=10^8). 0 violations — the proven parity law holds at every probe. |
| `pattern_check.py` | Pattern checks on the sequences produced by patterns.py: verifies oracle values H(5)=30, H(10)=138, H(1000)=1177848, the exact identities H=6·A063985 and A063985=n(n+1)/2-Phi, and prints first 40 terms of each sequence for the sequence tools. Exact integer arithmetic. |
| `pattern_pass2.py` | Second pattern pass, fully vectorized exact checks over the 200000-term prefixes: A(n) mod 2 period-4 law term-by-term (A(n) vs A(n+4) from n=2), exact search for longer periods of A mod 2 up to 400, and further exact structure checks. |
| `patterns.py` | Pattern extraction for PE 351: exact totient sieve (N up to 2e5) producing H, A063985, cototient, phi, Phi sequences; falsifies the spurious order-4 recurrence at n=9; verifies Chai Wah Wu A063985 recursion vs sieve at probes including 10^8; reports growth ratio. |
| `pe351-pattern-findings.md` | The pattern-finder's findings document: which exact identities/laws hold over the full stored range, which are conjectures, the spurious order-4 recurrence killed at n=9, subsequence results, and the OEIS status of every sequence examined. |
| `pe351_values.md` | Record of the exact computed values (Phi and H at 5, 10, 1000, 10^8), the verification routes, and the origin-not-hidden gotcha. Producer: solution.py and verify_mobius.py. |
| `seq_A063985.txt` | A063985(n) for n=1..200000, exact (OEIS A063985); producer patterns.py. |
| `seq_H.txt` | H(n) for n=1..200000, exact (OEIS A216453); producer patterns.py. |
| `seq_Phi.txt` | Phi(n)=sum phi(k) for n=1..200000, exact (OEIS A002088); producer patterns.py. |
| `seq_cototient.txt` | Cototient c(k)=k-phi(k) for k=1..200000, exact (OEIS A051953); A063985 is its prefix sum. |
| `seq_phi.txt` | phi(k) for k=1..200000, exact (OEIS A000010); producer patterns.py. |
| `structure_checks.py` | Exact checks over 200000-term prefixes: cototient c(k)=k-phi(k) equals 1 iff k is prime; A063985 first-differences equal the cototient; H=6*A063985 and H mod 12 in {0,6}; totient-error growth. Checks 1-4 verified (check 5's sympy block was superseded by exact_rec_check.py). |
| `target_scale_check.py` | Applies the exact mod-12/parity laws at the target scale: n=10^8 (n mod 4 == 0) forces H(10^8) mod 12 == 0, A even, Phi even; checks these on the recorded final values — all hold. |
| `verify_mod4_law_indep.py` | Independent verification of the mod-4 law from a different code path (naive gcd-based phi over n=2..5000), plus application at the target scale n=10^8 using the verified H and A values, plus bounded negative checks that the law does not lift to A mod 4 or H mod 24 (no exact period <= 1000 from n=2). |
