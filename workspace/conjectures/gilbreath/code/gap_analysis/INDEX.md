# Index — code/gap_analysis

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `lemma54_failing_sisters.py` | Non-vacuous failing-side validation of Granville Lemma 5.4 on synthetic 2-then-odd sequences (includes Poisson-gap families), cross-checking the descent budget biconditional and contrapositive. |
| `lemma54_verify.py` | Re-derives and machine-verifies Granville Lemma 5.4 (the demand→success leg of the Route B ν_2 reduction): case rules, even-domain potential theorem + brute force, budget tightness, real-prime validation. Output in code/out/lemma54_verify.captured.txt. |
| `nu2_vs_gap_parity.py` | Measures nu_2(q_n) against the Hamming weight w(n) of the row-1 halved-gap ancestor window over [2,n-1], showing G-supply reduces to a prime-gap-mod-4 density claim (nu2 >= w/2 holds on all samples). |
