# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive oracle for Project Euler 493. Pinpoints the definition by exhaustively enumerating every k-subset on small (c colours, m balls, k drawn) instances and averaging distinct colours (exact fractions), and cross-checks against the linearity-of-expectation formula E = c(1 - C((c-1)m,k)/C(cm,k)). The exhaustive average matched the formula on every small case tried, including C(20,10)=184756 subsets, then the formula gives E = 763700091/112000148 = 6.818741802 for the real problem (7,10,20). |
| `montecarlo.py` | Seeded Monte Carlo sanity check for PE493: draws 20 of 70 balls (colour = ball//10), averages distinct colours over 2,000,000 trials, computes the standard error, and compares against the exact linearity-of-expectation value 7*(1-C(60,20)/C(70,20)). Verified: exact value 6.8187418020; MC mean 6.8185885, SE 0.000283, difference -0.541 SE — within noise. |
| `solution.py` | _(undescribed)_ |
