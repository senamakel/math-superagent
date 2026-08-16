# Index — code/gfold

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `g_run_telescope_verify.py` | Verifies the G-run-telescope lemma (down-set run structure C1 and interval-fold telescoping identity C2) on the prime-residue h and random two-valued h, exact F2 arithmetic. THIS RUN added the directive-26 failing negative control: a three-valued boundary (h = q_j mod 3) that MUST break the telescoping identity (438 mismatches over 620067 pairs), settling that the two-valued hypothesis is load-bearing and the positive result is not true by construction. Capture: code/out/g_run_telescope_verify_negctrl_full.captured.txt. |
| `neg_control_probe.py` | Probe used to confirm the directive-26 negative-control design before editing the real script: 2-valued boundary control holds (0 mismatches) and 3-valued boundary MUST fail (27 mismatches / 7707 pairs at small scale). Established that a 3-valued boundary is a valid perturbation of the telescoping identity hypothesis. |
