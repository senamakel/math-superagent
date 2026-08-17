# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `PE1006_report_tasks_ABC.txt` | Consolidated printed report for Tasks A+B+C (modular structure of M=101001001; no small eventual period of r(k); factor-value and N(i;k) structure with circular-interval columns). Produced by code/pe1006/report_tasks.py; every number exact, sources: psi_data_1_150.txt and factors_k40.json + sympy order/factor. |
| `PE1006_tasks_ABC_note.md` | Markdown note establishing the three computed claims (M prime, ord_10/Pisano, no small period, circular-interval columns reconstruct Psi) with claim blocks; validated against the brute oracle. |
| `README.md` | _(undescribed)_ |
| `commands.log` | _(undescribed)_ |
| `computed-findings.md` | Claim blocks for this run's checked computations: the exact Psi(k+1) extension recurrence, the no-low-order-linear-recurrence negative result for Psi(1..150), the M=101001001 modular/Pisano/ord structure, the no-small-eventual-period result, and oracle agreement. These computed findings reach research/CLAIMS.md. |
| `dump_factors_k40.txt` | Captured stdout of code/dump_factors.py: full printed table for k=1..40 (counts, Psi(k), Psi(k) mod 101001001, ones-count multiset, per-position one-counts), plus the N(i;k) rows k=8..15. Includes count==k+1 confirmation. |
| `exact_state_1_120.json` | _(undescribed)_ |
| `extract_psi.py` | _(undescribed)_ |
| `extract_sequences.py` | _(undescribed)_ |
| `factors_k12.txt` | _(undescribed)_ |
| `factors_k40.json` | Data file: dict k (key as string "1".."40") -> sorted list of the k+1 distinct Fibonacci subwords of length k, produced by code/dump_factors.py. Source of the Psi(k), ones-counts, and per-position one-counts printed by that program. |
| `fib_state.py` | _(undescribed)_ |
| `mkseq.py` | _(undescribed)_ |
| `mod_A.txt` | TASK A: M=101001001 is prime; M-1=2^3*3*5^3*131*257; ord_10(M)=50500500=(M-1)/2; Pisano period pi(M)=101001000=M-1. All verified two ways. |
| `mod_B.txt` | TASK B: r(k)=Psi(k) mod M for k=1..150; no small (< =75) eventual period exists. |
| `mod_B_period.txt` | _(undescribed)_ |
| `mod_C.txt` | TASK C: factor table k=1..12 and N(i;k) k=1..40; candidate N=floor((k-i)a+c) falsified. |
| `mod_C_ones.txt` | Exact ones total T(k)=(k+1)*floor(ka)+r_k and r_k table. |
| `mod_C_struct.txt` | Verified: N(i;k) balanced in i; constant F_(m-2) at k=F_m-1; candidate falsified. |
| `mod_report.md` | Report of Tasks A/B/C with methodology and structural conclusions. |
| `n1_analysis.py` | _(undescribed)_ |
| `positions.txt` | _(undescribed)_ |
| `psi_brute_k1_30.txt` | _(undescribed)_ |
| `psi_data_1_150.txt` | _(undescribed)_ |
| `psi_seq.err` | _(undescribed)_ |
| `psi_seq.txt` | _(undescribed)_ |
| `psi_seq_1_150.txt` | _(undescribed)_ |
| `psi_state_1_200.txt` | _(undescribed)_ |
| `refute-stabilization-threshold.md` | _(undescribed)_ |
| `state_parse.py` | _(undescribed)_ |
| `state_sequences.py` | _(undescribed)_ |
| `state_vector_linear_recurrence.md` | Write-up of the (negative) state-vector linear-recurrence test: no constant-coefficient linear/affine recurrence (orders 1..6) fits the 5-dim, 6-dim, or vR^2-enriched state over M; individual components have no low-order linear recurrence (BM order = n/2). Includes re-verification of the extension formula on all 199 transitions and the structural reason (the verified recurrence needs vR^2, nonlinear in state). |
| `structure.json` | _(undescribed)_ |
| `structure_seqs.py` | _(undescribed)_ |
| `task_conjugate_structure.captured.txt` | Analysis note for claim PE1006-conjugate-singular-iff-fibonacci: raw verification (base/singular/base words, Fibonacci match) plus the table of base words and singular factors at each Fibonacci index, and why this is the rising-sea ground (Psi at F_m is a rotation-sum over one Christoffel word + one square; 10^18 is between F_86 and F_87). Companion to the raw stdout in task_conjugate_structure.raw.txt. |
| `task_conjugate_structure.raw.txt` | Raw captured stdout of code/pe1006/task_conjugate_structure.py: the conjugacy-class sizes for every k=1..60, proving the conjugate+singular decomposition holds exactly at Fibonacci indices. Companion to the analysis note task_conjugate_structure.captured.txt. |
| `verify_exact.py` | _(undescribed)_ |
| `verify_recurrence.py` | _(undescribed)_ |
| `vr_blocks.py` | _(undescribed)_ |
