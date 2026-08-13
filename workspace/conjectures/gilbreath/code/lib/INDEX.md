# Index — code/lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `gilbreath.py` | Exact iterated absolute-difference row generator for Gilbreath's conjecture. primes_up_to(n) sieves the primes; rows_generator(primes, depth) yields A_0..A_depth one row at a time (O(width) memory); block_profile(row) is the length of the leading {0,2} block ignoring the leading entry. Main asserts reproduction of the five worked rows in problem.md (A_1..A_5 first 12 each) exactly, then runs to depth 600 over the first 33860 primes (sieve to 400000, same width as code/out/witnesses.json) confirming the leading entry is always 1, the second entry is always in {0,2}, and every index>=1 entry of every row k>=1 is even. Captured output in code/out/oracle_depth600.captured.txt. Correctness established by matching witnesses.json and the problem.md table exactly (A_1=[1,2,2,4,2,4,2,4,6,2,6,4], A_2, A_3, A_4, A_5 all match; 33860 primes, depth 600, EXIT AGREE). Single-threaded. |
