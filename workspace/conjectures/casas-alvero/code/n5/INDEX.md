# Index — code/n5

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `bench_n5_guards.py` | Second measurement script for the n=5 verifier: max |
| `bench_n5_primitives.py` | Design measurements for the n=5 verifier: (1) SNF on one real 195x120 matrix with a 480 s alarm — did not finish within cap (the measured infeasibility that forced the rank route); (2) is_ca_hasse(x^{p+1}-x^p, p) for p=2,3,7,11; (3) ordinary is_ca for p=8009 (cheap, all derivatives vanish); (4) max |
| `binomial_calibration.py` | Calibrates the Schaub-Spivakovsky SUFFICIENT binomial bad-prime criterion (arXiv:2307.05997 Cor 8: p |
| `feasibility_boundary.py` | Feasibility boundary of the Casas-Alvero minor criterion (Schaub-Spivakovsky arXiv:2411.13967 Thm 3.1) for n=3..8: computes d=(n^2-3n+4)/2, C=binom((n^2-n)/2, n-2), D=sum binom(d-i+n-2, n-2), tuples=n^(n-1) exactly (C, D cross-checked against lib.badprimes.lex_monomials), and states where each route (SNF, rank-mod-p) is feasible. Boundary: SNF feasible n<=4 (measured 19x15 0.002 s), rank-only n=5 (measured 106250 ranks/28 workers 384.1 s), rank also infeasible n>=6 (n=6: C=1365, D=2751, single rank ~185 core-s, full sweep ~2.2e5 core-h). Per-rank cost model O(D*C^2) extrapolated from the n=5 measurement; extrapolation beyond measured anchors is magnitude only, labelled as such. Exit 0; capture code/out/feasibility_boundary.captured.txt. Verified: independent recomputation of all parameter values by direct formulas matches. |
| `wall_time_runner.py` | Wall-time wrapper for the n=5 bad-prime verifier: runs code/badprimes_criterion/verify_badprimes_n5.py as a subprocess, prints its stdout followed by EXTERNAL WALL TIME in seconds, propagates exit status. Used because /usr/bin/time is not installed in the container. Established correct: used for the independent re-run (verify_badprimes_n5.py exit 0, 384.4 s external vs 384.1 s internal). |
