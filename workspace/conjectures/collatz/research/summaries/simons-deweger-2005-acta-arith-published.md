# Simons–de Weger 2005 — published version (Acta Arith. 117(1) 51–70)

<!-- src: J. Simons, B. de Weger, "Theoretical and computational bounds for m-cycles of the 3n+1-problem", Acta Arithmetica 117(1) (2005) 51–70, DOI 10.4064/aa117-1-3. Full text: research/sources/simons-deweger-2005-acta-arith-published.full.md (via Wayback Machine of the IMPAN free CC-BY PDF). -->

## What the source establishes

For T(n) = (3n+1)/2 if n is odd, T(n) = n/2 if n is even (the accelerated
3n+1 map), an **m-cycle** is a periodic orbit whose elements form m
increasing odd-run / decreasing even-run subsequences; it has K odd and L
even elements, and minimal element x_min. A cycle other than {1,2} is
nontrivial. Let δ = log 3 / log 2 and Λ = (K+L) log 2 − K log 3.

**Theorem 3 (Main Theorem).**
(a) (Brox) For every m there are only finitely many m-cycles.
(b) For 1 ≤ m ≤ 68 there are no nontrivial m-cycles.
(c) For 69 ≤ m ≤ 72 the only possible nontrivial m-cycles satisfy
x_min > 3.3889×10^17, with explicit (m, K, L, x_min) tables (e.g. the
m = 69 row: K = 5,750,934,602,875,680, L = 3,364,081,086,781,987,
x_min < 6.4877×10^17).

The proof: an upper bound for Λ exponential in K (Lemma 4/7), a
subexponential lower bound from transcendence theory (Lemma 12:
Λ > e^{−13.3(0.46057 + log K)}), so K, L, x_min < something exponential in m
(Lemmas 7, 13); a lower bound K > q_n from continued fractions of δ (Lemma
10) using the verification bound X0; combining these excludes m ≤ 68 and
leaves the 69–72 candidates above, to be ruled out as X0 grows. Corollary 2:
K > 2.2564×10^8 for any nontrivial m-cycle (Crandall's lemma).

**Key numbers:** Lemma 15 no cycles 2 ≤ m ≤ 57; Lemma 17 no cycles
2 ≤ m ≤ 63; Lemma 18 no cycles 64 ≤ m ≤ 68. For 58 ≤ m ≤ 515,619 a possible
cycle satisfies K < K2(m) (Lemma 16).

## Version nuance — 2005 published vs v1.44 preprint

The published paper proves non-existence only for **m ≤ 68** (with 69–72
candidates). The frequently-cited **m ≤ 75** figure is from the 2010 preprint
v1.44 (deweger.net), which uses Oliveira e Silva's later verification to
exclude 69–75. Attribution must distinguish the two. This held published
version also records Lemma 12's Λ lower bound with the constant 13.3 — the
effective irrationality-measure constant this run's Diophantine arm uses
(compare `zudilin-mu-8616`).

## Claims

```claim
id: sdw-2005-main-theorem
answers: official-published-simons-8841
statement: For the accelerated 3n+1 map T, (a) for every m there are finitely many m-cycles (Brox); (b) there are no nontrivial m-cycles for 1 ≤ m ≤ 68; (c) for 69 ≤ m ≤ 72 the only possible nontrivial m-cycles satisfy x_min > 3.3889×10^17, with explicit (K, L, x_min) tables. (Simons–de Weger, Acta Arith. 117 (2005), Theorem 3.)
hypotheses: m = number of local minima in a cycle of the accelerated map; nontrivial means not {1,2}
holds-here: true — the published 2005 baseline; Hercher's m ≥ 92 (hercher-m92) supersedes it
evidence: proved in source (full text held)
status: proved
falsifies: a published nontrivial m-cycle with m ≤ 68, or an error in the computation
```

```claim
id: sdw-2005-lambda-bounds
statement: For a nontrivial m-cycle with K odd and L even elements, 0 < Λ < (m/x_min)·something and Λ > e^{−13.3(0.46057 + log K)}; combining with continued-fraction lower bounds K > q_n of δ = log 3/log 2 gives the m ≤ 68 exclusion and exponential-in-m upper bounds on K, L, x_min. (Simons–de Weger 2005, Lemmas 4, 7, 10, 12, 13.)
hypotheses: nontrivial m-cycle, verification bound X0 with q_n + q_{n+1} ≤ (log 2) X0 / m
holds-here: true — this is the structural core of the m-cycle exclusion method
evidence: proved in source (full text held)
status: proved
falsifies: an error in the stated Λ bounds or the continued-fraction computation
```

## Cross-check with the v1.44 preprint

The held preprint (research/sources/simons-deweger-m-cycles-preprint-v1.44-deweger.net.full.md) is the 2010 improved version: Lemma 18(a) excludes 69 ≤ m ≤ 75 and 18(b) gives the (K, L) candidates for m ∈ {76, 77} with X0-dependent thresholds (5.39×2^60 in 2011 … 36.8×2^60 in 2040). The published 2005 text says "we prove that there exist no nontrivial m-cycles for m ≤ 68. For 69 ≤ m ≤ 72 we give possible solutions, which will be excluded when exterior computations à la [Ro] lead to new values for X0." Consistent: v1.44 is the update. The 1 ≤ m ≤ 68 exclusion is common to both.
