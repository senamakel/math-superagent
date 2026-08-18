# Index — code

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `AGENTS.md` | _(undescribed)_ |
| `brute.py` | Naive oracle for the Collatz conjecture. collatz_step(n) is one exact-integer map step; orbit_reaches_one(n, cap) simulates the orbit step by step with a visited set and returns True (reached 1), False (visited x != 1 twice: a non-trivial cycle, i.e. a counterexample), or None (cap exhausted — divergence undecidable in finite time). Bears on code/lean/Lib/collatz_conjecture.lean. Correctness: reproduces the worked example 1 -> 4 -> 2 -> 1, returns True for n = 1..10 and 27 (cap 1000), returns False on a synthetic 2-cycle 3->5->3 and None on a strictly increasing synthetic map — i.e. all three verdict paths were exercised. Intentionally naive: it is the oracle later fast methods are checked against. |
| `collatz_oracle.py` | Naive exact Collatz orbit oracle reproducing hand examples and checking a small finite range; exponential range use is explicitly prohibited beyond oracle_bound. |
