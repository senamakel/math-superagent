# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive oracle for Project Euler 1006. psi_brute(k) builds Fibonacci words S_N until the distinct length-k factor set stabilises at size k+1, then returns (count, Psi(k), tightest N). Exact integer arithmetic. Verified: reproduces worked example Psi(3)=20302 and Psi(10) mod 101001001 = 10699667. This is the oracle against which the fast method is checked. |
| `data.py` | Data generation for PE1006: (a) prints distinct length-k Fibonacci subwords with integer values for k=1..12, saving to out/factors_k12.txt; (b) computes Psi(k) exactly for k=1..150 by scanning S_n with |
| `dump_factors.py` | Exact brute-force dumper of the k+1 Fibonacci subwords of length k for k=1..40. For each k it builds a comfortably long Fibonacci word and collects the distinct length-k contiguous substrings, asserting the count is k+1; prints sorted factors, Psi(k)=sum of squares of int values, Psi(k) mod 101001001, the ones-count multiset, and per-position one-counts N(i;k). Saves the sorted factor sets to code/out/factors_k40.json. Verified: reproduces Psi(3)=20302 and Psi(10) mod 101001001 = 10699667, and count==k+1 held for all k=1..40. |
| `dump_structure.py` | Exact brute-force structural dump of Fibonacci-factor combinatorics for k=1..60: builds S_N with |
| `find_recurrence.py` | _(undescribed)_ |
| `test_recurrences.py` | _(undescribed)_ |
