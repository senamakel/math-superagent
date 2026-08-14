# Induced subgraphs of hypercubes (European J. Combinatorics, 2012)

Source URL: https://www.sciencedirect.com/science/article/pii/S0195669812001680
(Retrieved via `read_sources`; network boundary blocks direct PDF download.)

## What this source establishes

For the k-cube Q_k, a vertex of an induced subgraph Q_k[S] is **full** if its
internal degree equals k (the maximum possible). Define
φ_k(n) = max{ # full vertices in Q_k[S] : |S| = n }.

- Theorem 3.2: an exact recursive formula for φ_k(n). With the "higher
  categorical/radix" (HCR) decomposition n = Σ_{ℓ=0}^{i} C(k,ℓ) + m,
  φ_k(n) = Σ_{ℓ=0}^{i-1} C(k,ℓ) + m·(k−i−1)... (recursive in k, dyadic-layer
  structure). Extremal subgraphs achieve the bound.
- Theorem 4.1: min over pairs of induced subgraphs (H1,H2) covering all edges
  of Q_k of max(|V(H1)|, |V(H2)|) equals
  Σ_{ℓ=0}^{⌊k/2⌋} C(k,ℓ) + (k mod 2)·C(k−1, ⌊k/2⌋).

Method: Kruskal–Katona theorem applied to the shadow of the set system of S —
a vertex is full iff all k neighbours lie in S, a shadow condition.

## Why it is here

This is a technique source that counts vertices by *degree* on the hypercube via
Kruskal–Katona, i.e. a maximum-producing count rather than an average-boundary
bound — one of the few tools that could give a lower bound on D(S) directly. The
"full vertex" endpoints (degree k) are the opposite end of the spectrum from
problem.md's S of size 2^{n-1}+1, but the method is the relevant machinery.

## Claim block

```claim
id: induced-subgraphs-hypercube-full-vertices-kk
statement: The maximum number of full (internal-degree-k) vertices in an
  n-vertex induced subgraph of Q_k is exactly φ_k(n), given by a recursive
  Kruskal-Katona/shadow formula (Theorem 3.2), and the edge-cover min-max is
  the binomial-sum of Theorem 4.1.
hypotheses: S ⊆ V(Q_k), |S| = n.
holds-here: yes — genuine technique for counting vertices by internal degree on
  the cube; one of the few maximum-producing (as opposed to average-boundary)
  tools available.
status: asserted-by-source.
bearing: provides a k-side (large-degree) counting method; the Kruskal-Katona
  shadow machinery is a candidate route to a D(S) lower bound at the
  2^{n-1}+1 size, though problem.md's size is the low-degree end, not the
  full-vertex end.
anchor: induced-subgraphs-hypercubes-2012
```
