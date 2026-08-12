# Goldie, "Records, permutations and greatest convex minorants" — summary

- Source: Charles M. Goldie, Mathematical Proceedings of the Cambridge Philosophical Society (2022), records-permutations-and-greatest-convex-minorants. URL: https://www.cambridge.org/core/journals/mathematical-proceedings-of-the-cambridge-philosophical-society/article/abs/records-permutations-and-greatest-convex-minorants/DEE42D1FC4782ACA192BD360A1B1EE36 (full text: research/sources/goldie_records_permutations_convex_minorants.full.md)
- Content: translates theorems on random permutations into distribution-free results about record times and the greatest convex minorant (GCM) of a random walk, by modelling them on a common probability space. Identifies the Bernoulli random variables appearing in the standard representation of the number of sides of the GCM of a random walk: the indicators I_j are independent with P(I_j = 1) = 1/j (j-th observation being a new lower record of the walk's increments / new cycle in the permutation construction).
- Bearing on PE597: this is the primary source for the *no-finish* bump-race fact that the number of bump clusters (GCM faces) is distributed as the number of cycles of a uniform random permutation, with the independent-Bernoulli(1/j) representation. It fixes the statement `cm-composition-distribution` in the ledger and its hypotheses: iid/exchangeable increments, no subset-average ties, boundary-free walk on a fixed interval.
- Restriction: no absorbing finish line; no parity statistic of the finite-finish race.

```claim
id: cm-composition-distribution
statement: For a random walk S_j = sum_{i<=j} X_i with iid continuous increments, the greatest convex minorant on [0,n] has F_n faces with P(F_n = k) = S1(n,k)/n! (unsigned Stirling first kind), equivalently F_n = 1 + sum_{r=2}^n Ber(1/r) in distribution; the face-length composition of n equals in distribution the cycle-length composition of a uniform random permutation of [n], distribution-free over the increment law.
hypotheses: iid (or exchangeable) increments; no subset-average ties (continuous law); boundary-free walk on a fixed interval.
holds-here: hypotheses hold for the *pure no-finish* torpids race (speeds iid Exp(1), continuous); the finite finish line of PE597 is a boundary not covered by this theorem.
status: verified-against-source (Goldie 2022 identifies the Bernoulli(1/j) representation; Suidan 2001 TVP and Alsmeyer–Kabluchko–Marynych–Vysotsky arXiv:2002.07687 give the same face-count/segment-length results; run also verified face-length statistics numerically, code/verify_cm_face_dist.py)
bearing: exact cluster-composition statistics of the no-finish race; the requested finite-finish PARITY is a further statistic this theorem does not supply.
anchor: research/sources/goldie_records_permutations_convex_minorants.full.md
```