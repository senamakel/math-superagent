# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `analyze_existing_sequences.py` | Parses existing Goldbach and Chen sequence artifacts and reports exact lengths, endpoint data, gcds, and congruence violations before sequence-tool analysis. |
| `analyze_oes_table.py` | _(undescribed)_ |
| `brute.py` | Naive oracle for the binary Goldbach statement: trial-division is_prime, exhaustive goldbach_partitions(n), satisfies_goldbach(n) predicate. Reproduces every worked example in problem.md (4=2+2; 2 excluded, not a counterexample; 1 not prime) and hand-counted partition numbers for even n in [4,50]. Cross-checked against sympy.isprime enumeration for all even n ≤ 198. Correctness basis: self-checks (every returned pair is prime, ordered, sums to n), hand counts, sympy route. To be used only at small n; the fast sieve method (separate agent) is checked against it. |
| `chen_sequence_extend.py` | _(undescribed)_ |
| `closedform_mod3.py` | Closed form of the D(x;p) mod-3 bias: exact identity C[(2,1)] = #(n<=N, n=2 mod 6, n-3 composite); verified exactly at N=50000. |
| `crosscheck_sp.py` | _(undescribed)_ |
| `emit_slices.py` | Emits bounded slices of the extracted sequences for the sequence tools (they accept <=512 terms). |
| `extend_sp.py` | First-appearance S(p) sequence to N=50000, with mod-3 breakdown; 41 terms. |
| `extend_sp_10m.py` | Vectorized S(p) computation to N=1e7, the strongest attack on conjecture (C); 112 minimal primes, residue table exact. |
| `extend_sp_fast.py` | S(p) to N=200000 via ordered pair enumeration; tests the mod-3 congruence theorem and the S(p) mod-6 conjecture; 61 terms. |
| `extend_sp_vec.py` | Vectorized (numpy) S(p) computation to N=2e6; attacks conjecture (C) p>7 ==> S(p) != 0 mod 6; 86 minimal primes. |
| `extract_sequences.py` | Extract integer sequences r(n), g(n), S(p) from Goldbach partition data up to N; writes code/out/seq_*.txt; the oracle route for the sequence analysis. |
| `gap_analysis.py` | _(undescribed)_ |
| `goldbach_oracle.py` | Small-bound naive Goldbach oracle plus sieve cross-check; reproduces 4=2+2 and checks naive versus fast for every even n through 1000, bearing on Goldbach.Statement. |
| `goldbach_oracle_small.py` | Naive exact Goldbach oracle; reproduces worked examples and checks all even inputs through 1000, serving as evidence for GoldbachConjecture. |
| `pattern_extend_check.py` | Exact audit of existing Goldbach-derived S(p), r(n), and g(n) sequences; tests modular regularities and reports first supplied counterexamples. Evidence for the provisional pattern-audit note, not a proof. |
| `rn_mod_structure.py` | Shows r(n)=A045917 has NO mod-6 residue structure (uniform across n mod 6), so the mod-3 structure is confined to minimal-prime S(p), not partition counts. |
| `sequence_audit.py` | Reads stored Goldbach count, minimal-prime, and first-appearance sequences and prints exact basic invariants and violations; evidence-only audit. |
| `sequence_audit_run.py` | _(undescribed)_ |
| `sequence_chunks.py` | Prints reproducible 512-term chunks from existing r(n) and g(n) outputs so exact sequence tools can inspect bounded segments without exceeding tool limits. |
| `test_oes_claims.py` | Tests OeS's empirical S_min/S_max bounds (0 violations over head primes) and the mod-3 D(x;p) frequency split against fresh head data. |
| `test_tail_oes.py` | Tests the mod-3 congruence (T) and the mod-6 avoidance conjectures (C),(C') on the OeS Top-50 tail data (S~1e18): 0 violations of (T), residue table exactly {(1,2):30,(2,4):20}. |
| `verify_mod3_structure.py` | Proves by exhaustive enumeration (0 violations) the mod-3 law: n=2 mod 6 & p(n)!=3 ==> p(n)=1 mod 3; n=4 mod 6 ==> p(n)=2 mod 3. Full-partition and minimal-prime versions. |
| `verify_thresholds.py` | _(undescribed)_ |
