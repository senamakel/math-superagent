# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `brute-oracle-output.txt` | _(undescribed)_ |
| `closed-form-verified.md` | Claim note marking G1-checked: the closed-form f_place_value(n,d) was computationally verified against the brute-force oracle (statement table 0..12, f(22,2)=6, every n in 0..20000, all 14 solutions in 0..300000, 199981 third, f=3 never). Upgrades G1 from asserted to checked in the ledger. |
| `commands.log` | _(undescribed)_ |
| `indep-total-check.py` | Third independent route to the PE156 grand total: re-aggregates the nine on-disk per-digit solution files (code/out/solutions-d{1..9}.txt) by plain integer addition — no digit-counting code — checking counts vs A130432 [84,14,36,48,5,72,49,344,9], strict increasing order, paper Table 3 maxima, s(1)=22786974071 (given), and the total == 21295121502550. Awaiting tool_builder execution. |
| `pattern_block_structure.out` | _(undescribed)_ |
| `pattern_residue_exact.out` | _(undescribed)_ |
| `solution-run.log` | _(undescribed)_ |
| `solution.captured.txt` | _(undescribed)_ |
| `solutions-d1.txt` | _(undescribed)_ |
| `solutions-d2.txt` | _(undescribed)_ |
| `solutions-d3.txt` | _(undescribed)_ |
| `solutions-d4.txt` | _(undescribed)_ |
| `solutions-d5.txt` | _(undescribed)_ |
| `solutions-d6.txt` | _(undescribed)_ |
| `solutions-d7.txt` | _(undescribed)_ |
| `solutions-d8.txt` | _(undescribed)_ |
| `solutions-d9.txt` | _(undescribed)_ |
| `verify-output-note.md` | Note beside the verify.py output with the claim block PE156-grand-total-verified: Sum_{d=1..9} s(d) = 21295121502550, with per-digit sums, the three-way evaluator agreement, the brute-force agreement bounds, the oracle points reproduced, and the sources (bound = Khovanova-Marton Prop 9.1; counts = OEIS A130432; d=1 last term 1111111110 sourced from the arXiv full text on disk). |
| `verify-output.txt` | _(undescribed)_ |
| `verify.captured.txt` | _(undescribed)_ |
