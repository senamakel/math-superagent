# Index — code/refute

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `closure_analogues.py` | Smallest-scale counterexample hunt for analogous least-failure closure assertions: shows least failure of a simple arithmetic predicate (prime, square, semiprime) does not imply translation closure or a positive-density failure set. The logical obstruction to gap G-structural-closure's inference. |
| `closure_oracle.py` | Exact small Goldbach exceptional-set oracle (all even n <= 200) that directly tests the proposed closure maps (translation by 2k, prime multiplication, density) from gap G-structural-closure, and reports vacuous when no exception exists. Oracle only, O(n^2) trial division. |
| `goldbach_closure.p` | TPTP encoding of the Goldbach conjecture fragment (even => 4 or sum of two primes) submitted to find_counterexample; returned undecided at reached sizes. A sanity fragment only — too weak to encode standard arithmetic faithfully, so undecided is weak evidence, not a proof. |
| `sanity.p` | First TPTP sanity sketch (redundant even-definition axiom) superseded by goldbach_closure.p; kept as the initial encoding attempt in the refutation trail. |
