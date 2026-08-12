# DLMF §26.13, Permutations: Cycle Notation (NIST Digital Library of Mathematical Functions) — summary

- Source: NIST DLMF, Chapter 26 (Combinatorial Analysis), §26.13 Permutations: Cycle Notation. URL: https://dlmf.nist.gov/26.13 (full text: research/sources/dlmf_stirling_cycle_numbers.full.md)
- Content: canonical reference for permutation cycle notation. Defines the Stirling cycle numbers [n k] (signless Stirling numbers of the first kind |s(n,k)|) as the count of permutations of {1,…,n} with exactly k cycles; states the count of permutations with a given cycle type, the recurrence, and the relation of sign to cycle parity (sign of a permutation = (−1)^{n−#cycles}, i.e. parity = n − #cycles mod 2; equivalently a k-cycle is even iff k is odd).
- Bearing on PE597: (a) backs the S1(n,k)/n! = P(#cycles = k) statement used in the no-finish cluster-count identity; (b) the cycle-parity relation is the exact statistic the run compared against in the refuted "convex-minorant cycle-parity model" (code/cycle_parity.py): p(n,∞)=P(Σ_clusters C(size,2) even) differs from true race parity. Statement tier for the permutation/cycle facts in `cm-composition-distribution`.
- Restriction: standard permutation enumeration; nothing about the race.

```claim
id: stirling-cycle-numbers-and-cycle-parity
statement: [n k] = |s(n,k)| counts permutations of [n] with exactly k cycles; the sign of a permutation equals (−1)^{n−k}; each k-cycle has sign (−1)^{k−1}.
hypotheses: none (definitional).
holds-here: holds; used in the run's exact cycle-parity computations (code/cycle_parity.py) and in the no-finish cluster-count identity.
status: verified-against-source (DLMF 26.13 in library)
bearing: exact permutation-parity facts underlying the cycle-parity model and its refutation.
anchor: research/sources/dlmf_stirling_cycle_numbers.full.md
```