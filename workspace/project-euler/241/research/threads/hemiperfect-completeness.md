# Thread: completeness of the hemiperfect enumeration below 10^18

question: Is the forced-denominator DFS (or the tree-search family it implements) a *complete* enumeration of n ≤ 10^18 with σ(n)/n = k+1/2, so that the 22 sourced A159907 values are provably all of them?
status: grounded-closed — completeness is proved for the general aσ(n)=bn+c tree-search (Alekseyev 2026 Thm 3.3: prime-wheel pruning never skips a solution); the run's c=0 forced-denominator DFS is the specialized instance (the c=0 "extra optimization" Alekseyev names but does not develop). The 22-value set + sum 482316491800641154 is sourced from the A159907 and four class b-files (claim hemiperfect-22-below-1e18).
rests-on: alekseyev-tree-search-complete, flammenkamps-tree-search-method, hpn11-two-below-1e18, hpn13-first-term-1e44, a160678-reachability-13over2, hemiperfect-22-below-1e18
blocked-by: none in the library — the only practical gap is that the run's own DFS (code/hemiperfect_dfs.py) has not executed in this environment (no shell), so the completeness is backed by the literature + sourced listings, not by the run's own full run at 10^18.
next: when a shell is available, run code/hemiperfect_dfs.py at 10^18 and confirm it reproduces the 22 values and sum 482316491800641154; cross-check DFS vs brute at a reachable bound (10^6 / 3e7); then write solution.md + final code/solution.py.
