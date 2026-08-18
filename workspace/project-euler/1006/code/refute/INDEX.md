# Index — code/refute

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `G2-slope-refutation.md` | Refutation of Open Lemma G2 as written: the stated slope a=F(n-1)/F(n) is wrong (produces non-Fibonacci words with the block 11 at k=3); correct slope is F(n-2)/F(n)=fib(n)/fib(n+2). By-hand counterexample checked against the problem's own length-3 factor set and corroborated by code/out/check_slope.captured.txt. |
| `_run_check.py` | _(undescribed)_ |
| `check_M_and_claim3.py` | _(undescribed)_ |
| `check_d9_claim1.py` | _(undescribed)_ |
| `check_directive_claims.py` | _(undescribed)_ |
| `d9-claim1-k3.p` | _(undescribed)_ |
| `g2-slope-correct-k3.p` | TPTP encoding of claim G2 with the CORRECTED slope a=F(n-2)/F(n)=2/5 at k=3; sanity model showing the corrected slope matches the true factor set. |
| `g2-slope-fn-1-k3.p` | TPTP encoding of claim G2 with the STATED slope a=F(n-1)/F(n)=3/5 at k=3; expected `refuted` (mechanical words {011,101,110} do not equal the true factors {001,010,100,101}). |
| `g2_slope_check.py` | Independent exact check (Fractions) of the G2 slope claim at k=3,4,5 comparing arc-midpoint mechanical words for the stated slope F(n-1)/F(n) vs corrected F(n-2)/F(n) against the true factor set from S_n. |
| `refuter-summary.md` | Refuter's summary of the run: refutes the checked claim `ueuclid-incontainer-fails-s1s2` (a 1-indexed vs 0-indexed quantity confusion — the module is sound on disk), and records the directive-9 Claim-1 spot-checks plus the note that the d9-claim1-k3.p counterexample is an encoding artifact. |
| `ueuclid-S1-index-refutation.md` | Refutation record of claim `ueuclid-incontainer-fails-s1s2`: shows the decisive (1,0,1,5,z=3) case under the module's 1-indexed convention gives S1=547/S2=2551 (correct), and the claim's 426/1578 are the 0-indexed ue0 quantity. |
