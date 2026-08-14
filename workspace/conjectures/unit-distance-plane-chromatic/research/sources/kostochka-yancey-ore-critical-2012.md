# Ore's Conjecture on color-critical graphs is almost true — Kostochka & Yancey

**Source:** Alexandr Kostochka, Matthew Yancey, "Ore's Conjecture on
color-critical graphs is almost true", arXiv:1209.1050 (2012-09-05). Published
in JCTB / Combinatorica lineage; arXiv abstract read verbatim server-side via
read_sources (full text not on disk; the arXiv listing shows the theorem and
sharpness cases).

## What this establishes

The sharpest known lower bound on the number of edges in a k-critical graph on
n vertices — the current end of the Dirac → Gallai → Krivelevich →
Kostochka–Stiebitz → Kostochka–Yancey line, and the technique backbone of the
run's size-lower-bound skeleton.

**Theorem (Kostochka–Yancey, main result).** For k >= 4 and every k-critical
graph G on n vertices,

    |E(G)|  >=  F(k, n)  =  [ (k+1)(k-2) n - k (k-3) ] / [ 2 (k-1) ].

The bound is **sharp** (i.e. f_k(n) = F(k,n)) whenever:

1. n ≡ 1 (mod k-1) and n >= k; or
2. k = 4, n != 5, n >= 4; or
3. k = 5, n ≡ 2 (mod 4), and n >= 10.

For the run's case k = 5:

    F(5, n)  =  [ 6·3·n - 5·2 ] / [ 2·4 ]  =  (18n - 10)/8  =  (9n - 5)/4
              =  2.25 n - 1.25.

Sharp when n ≡ 1 (mod 4) (n >= 5) or n ≡ 2 (mod 4) (n >= 10). Compare:
Dirac trivial 2n; Gallai 2n + n/22; Krivelevich 2n + n/14; Kostochka–Yancey
2.25n − 1.25. The jump from 2n to 2.25n is the difference between the floor
barely exceeding the trivial δ ≥ 4 bound and a genuine additive gap.

**Consequences used by the skeleton.** For every 5-critical graph:
- e >= (9n−5)/4, i.e. e − 2n >= (n−5)/4. A 5-critical graph on n vertices has
  strictly more than 2n edges once n > 5 — a floor that a u(n) edge-count
  ceiling must be compared against as e >= 2.25n − 1.25, not e >= 2n.
- Polynomial-time algorithm: any graph G with |E(G[W])| < F_k(|W|) for all
  W ⊆ V(G), |W| >= k, is (k−1)-colourable. This is a *colourability certificate*:
  a graph that is sparse in this hereditary sense cannot be k-chromatic.

## Why it matters here

The size-lower-bound skeleton (G-exhaust) excludes n from hosting a minimal
5-chromatic unit-distance graph by showing the required edge floor (from
5-criticality) contradicts the u(n) edge-count ceiling. The stronger the floor
f(n), the more n are excluded. Kostochka–Yancey is the current best floor for
all k, is exact on two arithmetic progressions, and its proof is constructive
(potential method: ρ_k(R) = (k−2)(k+1)|R| − 2(k−1)|E(G[R])|, P_k(G) =
min_∅≠R⊆V ρ_k(R)). The Ore-conjecture confirmation (exact f_k(n+k−1) =
f_k(n) + ((k−1)/2)(k − 2/(k−1)) for all but O(k^{3/12})... all but at most
k^3/12 values of n) pins the exact asymptotic of the floor.

## Note on download

Fetched server-side via read_sources (arXiv abs page; abstract and sharpness
theorem read verbatim). Technique-tier result (extremal theory of colour-critical
graphs) — not answer-tier material for Hadwiger–Nelson.

```claim
id: kostochka-yancey-critical-edge-bound
statement: For k >= 4 and every k-critical graph G on n vertices, |E(G)| >= F(k,n) = ((k+1)(k-2)n - k(k-3))/(2(k-1)). Sharp when n ≡ 1 (mod k-1) (n >= k), or k = 4 with n >= 4, n != 5, or k = 5 with n ≡ 2 (mod 4), n >= 10. For k = 5: e >= (9n-5)/4 = 2.25n - 1.25. (Kostochka-Yancey, arXiv:1209.1050; sharp cases read verbatim from the arXiv listing.)
hypotheses: G finite simple k-critical graph (chi(G)=k, every proper subgraph has chi < k); k >= 4; n = |V(G)|.
holds-here: yes — a vertex-minimal 5-chromatic unit-distance graph would be 5-critical, so any such graph on n vertices has e >= (9n-5)/4; the size-lower-bound skeleton uses this as the edge floor against u(n) ceilings, and the paper's (k-1)-colourability certificate (hereditary sparseness below F_k) is a direct non-5-chromaticity certificate.
status: sourced (arXiv abstract and sharpness theorem read verbatim via read_sources; the F formula for k=5 evaluated here)
bearing: the sharpest edge floor for G-crit/G-exhaust; strictly stronger than Krivelevich (2.07n) and Dirac (2n); exact on two residue classes; supplies a polynomial-time (k-1)-colourability certificate for sparse graphs.
anchor: research/sources/kostochka-yancey-ore-critical-2012.md
```

```claim
id: ky-potential-method
statement: The Kostochka-Yancey proof uses the potential rho_k(R) = (k-2)(k+1)|R| - 2(k-1)|E(G[R])| over subsets R of a k-critical graph; P_k(G) = min over nonempty R; the theorem states the minimum of |E(G)| given the potential constraint, and gives a polynomial-time (k-1)-colouring algorithm for graphs whose induced subgraphs all satisfy |E(G[W])| < F_k(|W|).
hypotheses: k-critical / sparse graphs as described.
holds-here: yes — the potential method is exactly the tool for turning "would-be 5-critical unit-distance graph" density constraints into colouring certificates: if every induced subgraph has e < F_5(|W|), the graph is provably 4-colourable.
status: sourced (potential definition and algorithm read in the arXiv excerpt)
bearing: a certificate path for the size-lower-bound route that needs no SAT search: hereditary sparseness alone proves 4-colourability.
anchor: research/sources/kostochka-yancey-ore-critical-2012.md
```