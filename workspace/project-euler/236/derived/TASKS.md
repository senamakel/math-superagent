# Tasks

- [x] Write/confirm the naive oracle. `code/brute.py` re-ran this cycle (base
      product Christmas Cake, 2,477,056 (s,t) pairs): reproduces BOTH statement
      worked examples — count 35 and smallest 1476/1475 — exactly. Also reports
      largest 123/59, pending independent confirmation.
- [ ] Research pass: download governing theory into `research/sources/` —
      rational solutions to linear systems with integrality constraints,
      Farey/Stern-Brocot mediant structure for bounding rational ratios, and
      standard treatments of simultaneous linear Diophantine equations. File
      each as a claim block.
- [x] `code/solution.py` (derived, non-enumerative method) executed at full
      size: all asserts pass (count 35, smallest 1476/1475, largest 123/59)
      and the literal six-equality Fraction witness check on the largest
      passes. Agrees with brute.py and verify_oracle.py.
