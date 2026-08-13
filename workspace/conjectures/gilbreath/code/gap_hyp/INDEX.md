# Index — code/gap_hyp

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `gap_hypothesis_separation.py` | Separation test: do three candidate gap hypotheses (bounded window mean, bounded freq of gaps>G, Cramer g_n=O(log^2 p_n)) distinguish the prime gap sequence from same-length i.i.d. {2,4,...,20}-uniform sequences? Sieves primes <200000 (17983 gaps), builds two fixed-seed random columns (second with first gap forced to 2), prints side-by-side stats (max/mean gap, sliding-window max means for W=100/1000/10000, freq of gaps>G for G=6/10/20/50, Cramer ratio), then the per-hypothesis verdict. Correctness: preamble asserts A1..A3 of problem.md via lib.gilbreath rows_generator (PASS/FAIL printed first); window sums are exact integer prefix-sum differences; numpy Mersenne-Twister fixed seed makes the random columns reproducible; Cramer's conjecture is only a conjecture and the sharp form tested (max gap <= log^2 p_max) is the folklore reading — the program states this. Result: verdict NONE separates — primes and {2..20} both satisfy all three; the random tail is strictly tamer (max gap 20 cap), so the difference goes the wrong way. Output: code/out/gap_hypothesis_separation.captured.txt |
