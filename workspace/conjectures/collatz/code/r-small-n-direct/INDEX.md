# Index — code/r-small-n-direct

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `verify_small.py` | Exact memoized verifier that every 1 <= n <= 2^20 reaches 1 under the Collatz map. Naive direct simulation (visited set, step cap 10^6) with a dict memoising the reaches-1 verdict for every decided value so orbits are never recomputed; the map C and the naive oracle come from code/brute.py (imported as `brute`), so the definitions cannot drift apart. Cross-checks the memoized method against brute.orbit_reaches_one on n=1..1000 (AGREE), then sweeps n=1..2^20 and prints the verdict line. Bears on code/lean/Lib/collatz_conjecture.lean, Cited.collatz_conjecture — finite exact evidence for the n <= 2^20 instances only. Correctness established by: (a) reproducing brute.py's oracle semantics, (b) the n=1..1000 cross-check against the independent naive oracle, (c) exact integer arithmetic throughout, no floats in any verdict. |
