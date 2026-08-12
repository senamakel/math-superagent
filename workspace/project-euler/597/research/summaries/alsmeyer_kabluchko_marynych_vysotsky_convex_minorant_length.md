# Alsmeyer, Kabluchko, Marynych, Vysotsky, "How long is the convex minorant of a one-dimensional random walk?" — summary

- Source: Gerold Alsmeyer, Zakhar Kabluchko, Alexander Marynych, Vladislav Vysotsky, arXiv:2002.07687, Electron. J. Probab. 25 (2020), doi:10.1214/20-ejp497. URL: https://arxiv.org/pdf/2002.07687 (full text: research/sources/alsmeyer_kabluchko_marynych_vysotsky_convex_minorant_length.full.md)
- Content: distributional limit theorems for the length (number of faces) of the convex minorant of a one-dimensional random walk with iid increments, and its segment-length structure. Key tool: the Sparre Andersen representation of the convex minorant in terms of uniform random permutations — the segment composition of the GCM on [0,n] is built from the cycle structure of a uniform random permutation (segment lengths = cycle lengths, with auxiliary iid increments attached to each cycle). This validates the claim: the face-length partition equals in distribution the cycle-length partition of a uniform random permutation, distribution-free over the increment law.
- Bearing on PE597: primary contemporary source for the no-finish bump-race cluster-size structure; extends the exactness from cluster count to the full composition. No finite finish line, no parity statistic.

```claim
id: cm-composition-distribution
statement: GCM of a random walk: face-length composition = (in distribution) cycle-length composition of a uniform random permutation; the permutation representation (Sparre Andersen) underlies all exact segment-statistics results.
hypotheses: iid/exchangeable increments, continuous law; boundary-free walk on [0,n].
holds-here: holds for the pure no-finish torpids race; not for the finite-finish problem.
status: verified-against-source (arXiv:2002.07687; corroborated by Goldie 2022, Suidan 2001, Abramson thesis; run verified face-length statistics in code/verify_cm_face_dist.py)
bearing: exact no-finish cluster composition statistics.
anchor: research/sources/alsmeyer_kabluchko_marynych_vysotsky_convex_minorant_length.full.md
```