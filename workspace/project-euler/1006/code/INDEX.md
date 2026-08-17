# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `brute.py` | Naive/oracle solution to Project Euler 1006: collects distinct length-k factors of the infinite Fibonacci word, interprets them as decimal ints, sums squares (Psi(k)). Verified: Psi(3)=20302, Psi(10)%101001001=10699667, all counts k+1 for k=1..20, factor sets stable under word extension. Note: builds word to len >= 3k, because 2k is insufficient at k=15 (needs 35). |
