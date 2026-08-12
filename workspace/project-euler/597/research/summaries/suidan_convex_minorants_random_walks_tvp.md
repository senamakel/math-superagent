# Suidan, "Convex minorants of random walks and Brownian motion" (TVP 2001) — summary

- Source: Toufic M. Suidan, Teor. Veroyatnost. i Primenen. 46(3) 498–512 (2001) [Theory of Probability and its Applications 46(3)]. URL: https://www.mathnet.ru/php/archive.phtml?wshow=paper&jrnid=tvp&paperid=3898&option_lang=eng (full text: research/sources/suidan_convex_minorants_random_walks_tvp.full.md)
- Content: exact distributional results for the convex minorant of a random walk of length N with iid real-valued increments having a density: full characterization of the distribution of the r-th longest segment length, via a bijection with cycle lengths in random permutations; explicit joint density for the r longest segments in the Brownian case. Using permutation theory it (re)proves the Sparre Andersen formula: P(the GCM of a length-N random walk consists of m segments) = (1/(m! N^m)) d^m/dz^m (−ln(1−z))^m |_{z→0^+} = |s(N,m)|/N! = S1(N,m)/N!. Expected number of segments = sum_{j} 1/j = H_N; variance = sum_j (1/j − 1/j^2).
- Bearing on PE597: the no-finish bump-race cluster count distribution P(k clusters) = S1(N,k)/N! is exactly the GCM face-count; Suidan's formula is the closed-form expression behind that identity, and the long-segment results describe cluster-size structure. The finite finish line is not treated.
- Restriction: boundary-free walks; no parity.

```claim
id: cm-composition-distribution
statement: P(number of faces of the GCM of a length-N random walk = m) = S1(N,m)/N! (= 1/(m! N^m) d^m/dz^m (−ln(1−z))^m at z→0^+), and the segment-length composition equals the cycle-length composition of a uniform random permutation.
hypotheses: iid increments with continuous law; boundary-free walk on [0,N].
holds-here: holds for the pure no-finish torpids race; not for the finite-finish problem.
status: verified-against-source (Suidan 2001, mathnet mirror; corroborated by Goldie 2022, Alsmeyer et al. 2020, Abramson thesis; run verified face-length statistics in code/verify_cm_face_dist.py)
bearing: exact no-finish cluster statistics; not the finite-finish parity.
anchor: research/sources/suidan_convex_minorants_random_walks_tvp.full.md
```