# Index — code/kernel

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `dyadic_crosscheck_pre.py` | Convention lock: wt(Phi_n h) equals direct-triangle nu2 on 60 random (m,h), 0 mismatches, and 0 on the all-ones kernel input. |
| `dyadic_kernel_probe.py` | DPC-kernel-classification feasibility probe: exhaustive min of wt(Phi_n h)/m over balanced+anti-dyadic h in {0,1}^m, m=4..18. Verdict: DECAYS to 0 as 1/m (half-step strings give constant fold weight 1 while being 0.5m from every 2^k-periodic string). Refutes DPC-kernel-classification as stated. Verified by two independent programs. |
| `dyadic_kernel_verify.py` | 3-route independent check (matrix dot / direct triangle / halved-XOR-on-suffix) confirming the probe's minimizers have wt(Phi h)=1; all agree on all 7 minimizers. |
| `dyadic_kernel_verify_constraints.py` | Independent check that the probe's minimizers satisfy both survivor constraints (balanced + anti-dyadic); all 7 pass, so they are genuine counterexamples. |
