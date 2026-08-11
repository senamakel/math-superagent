# Index — research

What each file in this folder is for. Keep it current: describe a file when you create it, and refresh this index after adding, renaming, or deleting files.

| File | Purpose |
| --- | --- |
| `factorial_number_system_wiki.md` | Summary (excerpt) of the Wikipedia factorial number system article; establishes that factoradic digits give the lexicographic rank (Lehmer code) of a permutation. Companion full text: research/factorial_number_system_wiki.full.md |
| `leanos_mth_roots_of_permutations.md` | Summary (excerpt) of Leanos, Moreno, Rivera-Martinez arXiv:1005.1531 on exact counts of m-th roots of permutations by cycle structure. Noted as NOT directly usable for Q(n) (root counts do not feed the intra-subgroup rank sum). Companion full text: research/leanos_mth_roots_of_permutations.full.md |
| `report_cited_facts.md` | Cited mathematical facts with URLs behind the run: (1) Lehmer/factorial rank, (2) k-th root counts by cycle structure (Wilf, Pavlov, Leanos et al), (3) sum-of-ranks identity = n!(n!+1)/2, (4) order/exponent of S_n and power-map bijectivity. Includes the finding that no closed form is known for the rank-sum over a cyclic subgroup (the part that must be attacked for n=10^6) |
| `report_rank_powers.md` | Earlier summary: cited facts (Lehmer/factorial-rank identity, ord = lcm of cycle lengths, sum of ranks = n!(n!+1)/2) plus the derived reduction Q(n) = sum over cyclic H of phi(size H)*(n!/size H)*sum over tau in H of rank(tau); notes the core intra-subgroup rank-sum is unresolved |
| `verify_facts.py` | Brute-force oracle for the rank/powers problem: Lehmer rank0/r1, apply_power, order, Q(n) literal, plus checks sum of ranks = n!(n!+1)/2 and rank(2,1,3)=3, Q(2)=5, Q(3)=88. Written but NOT run in its original environment; its n=2,3 checks were reproduced by hand (see report_cited_facts.md). Use to validate solution.py once a code executor exists |
