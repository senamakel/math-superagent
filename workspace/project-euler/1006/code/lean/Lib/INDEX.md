# Index — code/lean/Lib

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `Statement.lean` | Formal PE1006 statement: defines the Fibonacci word fibWord, digitVal, valueOf (decimal value ignoring leading zeros), slidingFactors (length-k contiguous factors), Psi (sum of squares of distinct factor values), PsiResidue (mod M=101001001), and states as unproved theorems the two oracle examples (Psi 3 = 20302, Psi 10 % M = 10699667), the k+1 factor count, the oracle-input lemmas (M prime, 10 invertible mod M), and the target pe1006 : ∃ A < M with PsiResidue 10^18 = A. Every theorem ends in := by sorry; elaborates cleanly (lean_check compiled: true). |
