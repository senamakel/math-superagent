# Balko & Valtr, "A SAT attack on the Erdős–Szekeres conjecture" (ENDM 2015)

<!-- source: https://eurocomb2015.w.uib.no/files/2015/08/endm1938.pdf | full text at research/sources/balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md -->

**Publication.** M. Balko and P. Valtr, *Electronic Notes in Discrete Mathematics* 49 (2015) 425–431 (EuroComb 2015). DOI 10.1016/j.endm.2015.06.060. Journal version: *European J. Combin.* 66 (2017) 13–23, DOI 10.1016/j.ejc.2017.06.010. **This is the open full text that closes request `balko-valtr-attack-baa4`.**

## Why this source matters (the single most important caution in the library)

Balko–Valtr **refute the Peters–Szekeres strengthened conjecture** — the claim that the ES conjecture holds over ALL red-blue colorings of the ordered complete 3-uniform hypergraph K^3_N, not just the colorings that arise from actual point sets. Their non-geometric counterexamples are exactly the **unrealizable abstract structures** the run's problem description warns about: they exist in abstract order-type / hypergraph space but not as planar point sets.

**The counterexamples are all NON-pseudolinear** (Section 5). A coloring is *pseudolinear* if every 4-tuple induces a realizable coloring of K^3_4 — i.e. one consistent with planar geometry. Since every real geometric coloring is pseudolinear, and all counterexamples are not, **these results do NOT touch the Erdős–Szekeres conjecture itself.** This is a verified, source-backed instance of "an upper-bound proof over all abstract order types is stronger than the conjecture and is FALSE." Any candidate proof in this run that works over all red-blue 3-uniform colorings (or all abstract chirotopes) must be checked against the Balko–Valtr witness before being believed.

## The framework (the vocabulary this run needs)

- Red/blue coloring of K^3_N: color triple {i,j,k} (ordered by x-coordinate) red if it's a 3-cap (clockwise), blue if 3-cup (counterclockwise). A coloring obtained from an actual point set is *realizable*.
- A **monotone k-path** in a coloring is a chain of edges {v1,v2,v3},{v2,v3,v4},…,{v_{k-2},v_{k-1},v_k}. Red paths ↔ k-caps, blue paths ↔ k-cups.
- A **(convex) k-gon** in a coloring: a red and a blue monotone path, vertex-disjoint except common end-vertices. Convex k-gons in the point set ↔ k-gons in the realizable coloring. There are 2^{k-2} non-isomorphic k-gons.
- cES(k): max N with a coloring of K^3_N and no k-gon. Geometry gives 2^{k-2} ≤ ES(k) ≤ cES(k).
- bN(a,u,k): max N with a coloring with no red a-path, no blue u-path, no k-gon.

## Results (asserted-by-source, peer-reviewed)

- **Theorem 2.1**: cES(7) > 32 and cES(8) > 64. **Refutes the Peters–Szekeres conjecture.** Uses Glucose SAT solver.
- bN(4,7,7) = 17; bN(5,6,7) ≥ 26, bN(5,7,7) ≥ 27, bN(6,6,7) ≥ 31, bN(6,7,7) ≥ 32, bN(7,7,7) ≥ 33; bN(4,8,8) ≥ 23 (counterexample to PS conjecture for k=8). For k>8 formulas too large.
- **Proposition 3.2**: N(4,k,k) ≤ C(k,2) − 1 (improves best upper bound by one for a=4).
- Over **pseudolinear colorings** (the geometric case) they VERIFY Conjecture 3.1 — the Erdős et al. equivalent of the ES conjecture — in the cases a=4,u=k=7 (N=16) and a=4,u=k=8 (N=22). All pseudolinear results matched the conjecture. So the geometry still behaves as conjectured even where the abstract hypergraph does not.
- The ES conjecture itself remains OPEN after this work (stated explicitly).

## Direct bearing on this run

1. **Do not try to prove the ES upper bound over abstract colorings/chirotopes** — it is false (cES(7)>32). The 4-tuple / pseudolinearity constraint is essential and must be part of any SAT or order-type encoding.
2. The SAT encoding uses **triple-orientation variables** (red/blue = clockwise/counterclockwise), exactly the formulation GOAL.md and PROBLEM.md point at, and which Scheucher and Dumitru also use (both in the library).
3. It confirms the Peters–Szekeres n=6 proof (also in library) as the last geometric case settled.

## claim block (for CLAIMS.md)
> This source **answers request `balko-valtr-attack-baa4`** — the open-access ENDM 2015 full text of the Balko–Valtr SAT attack, its triple-orientation encoding, and its refutation of the Peters–Szekeres strengthened conjecture — and **answers request `open-access-full-1e6e`** (open full text, eurocomb2015.w.uib.no, obviates the paywalled EJC 2017 version).

```claim
id: balko-valtr-refutes-PS
answers: balko-valtr-attack-baa4
answers: open-access-full-1e6e
statement: The Peters–Szekeres strengthened conjecture is FALSE: cES(7) > 32 and cES(8) > 64, i.e. there exist red-blue colorings of K^3_{33} (resp. K^3_65) with no 7-gon (resp. no 8-gon). The greedy bN values: bN(4,7,7)=17, bN(7,7,7)≥33, bN(4,8,8)≥23.
hypotheses: colorings of ordered complete 3-uniform hypergraphs, NOT restricted to pseudolinear/realizable colorings.
holds-here: FALSE for this problem's purpose as an abstraction — all the counterexamples are NON-pseudolinear, so they do NOT realize as planar point sets and do NOT bear on the geometric ES conjecture. It is a true theorem about a weaker abstraction.
status: asserted-by-source (peer-reviewed ENDM 2015 / EJC 2017; full text in library).
bearing: a crucial RULED-OUT direction. Any upper-bound argument over all abstract order types / all red-blue 3-uniform colorings is trying to prove something false; the pseudolinearity (4-tuple realizability) constraint is essential. Do not re-derive an abstract-chirotope upper bound.
anchor: research/sources/balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md
```

```claim
id: balko-valtr-pseudolinear-verifies
statement: Over pseudolinear colorings (every 4-tuple realizable), Conjecture 3.1 — the Erdős–Tuza–Valtr reformulation equivalent to the ES conjecture — is verified for a=4,u=k=7 with N(4,7,7)=16 and a=4,u=k=8 with N(4,8,8)=22; all pseudolinear SAT results matched the conjecture.
hypotheses: pseudolinear colorings of K^3_N, i.e. colorings consistent with planar geometry on every 4-subset.
holds-here: true — this is the geometric case, in exact agreement with the ES conjecture's predictions.
status: asserted-by-source (computed numerically by the authors, not independently re-derived here).
bearing: evidence that the geometry itself still follows the conjecture even where the abstract hypergraph fails; supports the split/decomposable partial results (Baek–Balko) and the structural route.
anchor: research/sources/balko-valtr-A-SAT-attack-on-ES-ENDM2015.full.md
```
