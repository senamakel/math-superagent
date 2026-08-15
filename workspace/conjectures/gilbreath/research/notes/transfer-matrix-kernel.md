# Transfer matrix kernel: why the universal covering bound fails

## Claim

```claim
id: transfer-matrix-kernel-allones
statement: The F2 transfer matrix Phi_n, rows k=2..n-2 (halved {0,2}-tail cells of the right diagonal), cols j=2..n-1 (halved-gap bits h), entry Phi_n[k][j] = C(k-1, j-(n-k)) mod 2, has rank n-3, nullity 1, and kernel = span(111..1) for every n=2..20, because row k's dot product with all-ones is the Pascal row sum 2^{k-1} = 0 mod 2. Hence wt(Phi_n h) = 0 for the all-ones bit string = the consecutive-odds input (q=(2,3,5,...), a SUCCESSFUL triangle with nu2=0, w=n-2), giving min_{h!=0} wt(Phi_n h)/wt(h) = 0 at every n. Therefore NO positive universal covering constant c exists: wt(Phi_n h) >= c*wt(h) is false for all c>0. This refutes the covering bound and confirms g-supply-transfer-refuted: the nu2 >= c*w transfer is prime-specific (case b), not a universal combinatorial identity. The real primes escape the kernel (min nu2/w = 0.5152 at n=53, never 0 over n<=3000, sieve 1e6). The 0.5152 dense-scan minimum and the sparse-set minimum 0.6885 at n=100 are the SAME nu2/w statistic under identical conventions (claim nu2w-minima-reconciled, code/out/reconcile_nu2w.notes.md), so the difference is sample density only, not a convention change.
hypotheses: any 2-then-odds prefix; tail = run's d[2:-1] convention; halved gap bit h[j] = (g_j/2) mod 2 over the fixed ancestor interval [2,n-1]; the Rule-90/Pascal window law (rule90-interior-xor, proved).
holds-here: yes
status: checked (exact F2 Gaussian elimination, all h enumerated to n=20; second route the Pascal-row-sum parity proof for the kernel)
anchor: code/refute/kernel_characterize.py, code/out/kernel_characterize.captured.txt, code/refute/universal_transfer_matrix_run.py, code/out/universal_transfer_matrix_RUN.captured.txt, code/out/reconcile_nu2w.captured.txt
bearing: closes the "prime-free provable half" of G-supply: the covering bound is refuted as a universal statement; any supply lower bound must be prime-specific.
```

## Context

- Setup: see the note body in code/out/kernel_characterize.notes.md.
- Cross-check: the kernel reason is also a proof (row sums of Pascal = 2^{k-1} = 0 mod 2), not only a computation; both agree.
- The consecutive-odds family q=(2,3,5,7,9,...) is SUCCESSFUL at every n (A_k(0)=1; cross-checked two independent code paths) while nu2=0, w=n-2 — the universal transfer fails inside the successful class.
