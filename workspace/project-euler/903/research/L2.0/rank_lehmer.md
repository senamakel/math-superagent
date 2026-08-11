# Fold: rank / Lehmer (factoradic) structure

Lexicographic rank is computed by Lehmer/factoradic digits; this is the rank machinery the problem's `sum rank(π^i)` rests on. The rank model is defined here; powers and the cyclic subgroup {π^i} are tackled from the homomesy angle, not solved.

- [[lehmer_factorial_norm]] (Zawiślak 2111.03951): Lehmer/factoradic digits give lexicographic rank; j-th digit uniform on {0..j}. L0 `lehmer_factorial_norm.full.md`.
- [[factorial_number_system_wiki]]: factoradic representation and rank; digits independent. Full text is the Wikipedia page (kept in L1 only).
- [[../../L1/homomesies_permutations]] (2206.13409): **homomesy** over orbits of a map on S_n — the phenomenon that would make an orbit-average of a statistic equal its global average. Lehmer-code rotation: every orbit has size lcm(1..n) (Thm 4.8), inversion-linked statistics homomesic (Thm 4.7). Routes the "average rank over {π^i}" question, but the map here is rotation, not permutation-power/cyclic subgroup, and rank itself is not homomesic there.

<!-- brief -->
Established: rank(π)=1+Σ a_j (n−1−j)! with Lehmer digits a_j; digits are independent and uniform on their ranges. Homomesy (2206.13409) is the framework for averaging a statistic over orbit/power actions but covers rotation, not the cyclic subgroup {π^i}, and not rank. Open: no source gives sum of rank over {π^i}.
