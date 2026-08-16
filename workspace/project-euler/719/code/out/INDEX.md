# Index — code/out

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `README.md` | _(undescribed)_ |
| `brute.txt` | _(undescribed)_ |
| `candidates_mitm.txt` | Candidate 03's verified full-size MITM run log: reproduces all 11 worked examples, T(10^4)=41333, T(10^6)=10804656, T(10^9)=6222187932, T(10^12)=128088830547982 (count 406). Confirms the final answer by an independent MITM route. |
| `commands.log` | _(undescribed)_ |
| `final.log` | _(undescribed)_ |
| `final_answer.md` | Records the checked final answer T(10^12)=128088830547982 and its two independent verification routes. |
| `live_rerun.captured.txt` | Live re-run in this container: solver at 10^4/10^6/10^9 matches recorded values, and the independent A038206 b-file route confirms T(10^12)=128088830547982 at full size. This is the executed verification for this attempt. |
| `oracle.md` | _(undescribed)_ |
| `pattern_report.md` | Pattern-recognition report on the A038206 S-root sequence: re-confirms the mod-9 rule (0 violations over 3200 roots), proves the infinite two-block Kaprekar family m_k=5·10^k·(10^{k+1}−1), and records that no linear recurrence or closed form governs the general sequence. |
| `roots408.txt` | _(undescribed)_ |
| `roots_seqs.txt` | _(undescribed)_ |
| `scholar_fresh_check.py` | Fresh independent verification of T(10^12): builds the S-root predicate from scratch (memoized suffix reachability), reproduces the worked examples, T(10^4)=41333, re-derives T(10^12) by scanning roots, and cross-checks the resulting root set against the catalogued roots408.txt. To be run by tool_builder. |
| `scholar_independent_check.py` | Scholar's independent third-route numeric check of T(10^12): sums m^2 over the catalogued A038206 roots in [2,10^6] and also re-derives the S-root predicate freshly to confirm every catalogued root really is an S-root. Not yet run in this container — the scholar role has no execution tool; left for tool_builder to run. |
| `scholar_verify.py` | Scholar-authored independent check stub: sums m^2 over the catalogued A038206 roots (m>=2) in roots408.txt to re-derive T(10^4)=41333 and T(10^12). A redundant third route to the already-confirmed answer; left for tool_builder to run if desired. NOT yet run in this container. |
| `seq_decades.txt` | Exact decade-level sequences (root counts, square-sums, cumulative) from the A038206 b-file to 10^9, tool results (no recurrence/polynomial/OEIS match), and the 19 consecutive-root pairs — pattern-finder output, all negative or marginal. |
