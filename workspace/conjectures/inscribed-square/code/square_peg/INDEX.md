# Index — code/square_peg

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `check_oracle.py` | Produces code/out/oracle_check.txt with exact polygon sanity checks, fixed rational ellipse approximations and error bounds, regular polygon circle checks, and the no-search 13x13 grid-bound note. |
| `independent_check.py` | Independent exact edge-pair/distance verifier used to attack the main oracle on bounded tiny polygons. |
| `oracle.py` | Exact Fraction polygon-boundary square oracle; finds nondegenerate cyclic squares with vertices on edge interiors using rational edge-pair solves; checked against an independent exact route. |
| `test_oracle.py` | Small regression test comparing the main Fraction oracle with an independent exact verifier and known unit-square result. |
| `verify_symmetric.py` | Exact Fraction verification script: reproduces brute.py sanity cases, checks the Nielsen–Wright symmetric hexagon is Jordan and reports oracle squares, and reports the irregular pentagon result. |
