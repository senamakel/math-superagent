# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `check_library_values.py` | Library-value oracle: computes Phi(n) by a naive phi sieve and checks H(5)=30, H(10)=138, H(1000)=1177848 (statement oracles) plus Phi(10^k) k=0..8 against OEIS A064018, then prints the check anchor H(10^8) = 3·10^8·(10^8+1) − 6·Phi(10^8) = 11762187201804552 that solution.py must reproduce. Exact integer arithmetic; the final answer is anchored here. |
| `commands.log` | _(undescribed)_ |
| `exact_rec_check.py` | _(undescribed)_ |
| `fix_mobius_verify.py` | Corrected Möbius-inversion verification of Phi(N): the old verify_mobius.py used mu[p*p::p]=0 (step p, zeroing squarefree numbers 6,10,14,15,...); this uses step p*p. Matches the totient sieve exactly at N=2,3,5,10,20,100,1000,1e5,1e8 — Phi(1e8)=3039635516365908 by both routes, closing the run's recorded MISMATCH. |
| `growth_checks.py` | _(undescribed)_ |
| `patterns.py` | Pattern extraction for PE 351: exact totient sieve (N up to 2e5) producing H, A063985, cototient, phi, Phi sequences; falsifies the spurious order-4 recurrence at n=9; verifies Chai Wah Wu A063985 recursion vs sieve at probes including 10^8; reports growth ratio. |
| `pe351_values.md` | Record of the exact computed values (Phi and H at 5, 10, 1000, 10^8), the verification routes, and the origin-not-hidden gotcha. Producer: solution.py and verify_mobius.py. |
| `seq_A063985.txt` | _(undescribed)_ |
| `seq_H.txt` | _(undescribed)_ |
| `seq_Phi.txt` | _(undescribed)_ |
| `seq_cototient.txt` | Cototient c(k)=k-phi(k) for k=1..200000, exact (OEIS A051953); A063985 is its prefix sum. |
| `seq_phi.txt` | _(undescribed)_ |
| `structure_checks.py` | Exact checks over 200000-term prefixes: cototient c(k)=k-phi(k) equals 1 iff k is prime; A063985 first-differences equal the cototient; H=6*A063985 and H mod 12 in {0,6}; totient-error growth. Checks 1-4 verified (check 5's sympy block was superseded by exact_rec_check.py). |
