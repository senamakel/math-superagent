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
- [ ] `code/solution.py` (derived, non-enumerative method) agrees with the
      oracle at every reachable size and produces the largest m at full size.
