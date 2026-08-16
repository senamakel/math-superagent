# Moshkovitz & Shapira, "Ramsey Theory, Integer Partitions and a New Proof of the Erdős–Szekeres Theorem", arXiv:1206.4001 (2012, Adv. Math. 262 (2014) 1107–1129)

<!-- source: https://arxiv.org/pdf/1206.4001 | full text at research/sources/moshkovitz-shapira - Ramsey theory integer partitions new proof of ES - arxiv1206.4001.full.md -->

**Publication.** Guy Moshkovitz and Asaf Shapira, arXiv:1206.4001 [math.CO] (2012); published in
*Advances in Mathematics* 262 (2014) 1107–1129. (Baek's arXiv:2206.04260, already in the library,
cites this as the origin of the α-statistic / slope-labeling machinery used in the (α,β)-plane proof.)

## Why this source matters

This is the **primary source of the integer-partition machinery** that underlies the run's structural
route. It gives an *exact* characterization of the ordered-3-uniform-hypergraph Ramsey number
N3(q,n) in terms of counting high-dimensional integer partitions, and a new pigeonhole proof of the
Erdős–Szekeres cups-caps theorem. This is the theoretical backbone of the orientation-variable /
monotone-path SAT formulation the run's sources (Fox–Pach–Sudakov–Suk, Baek, Balko–Valtr,
Scheucher, Dumitru) all build on, and it is the precise source of the down-set→partition injectivity
used in Baek's α-statistic.

## Definitions and the key theorem

- **Monotone path (length = #edges).** In K^N_k (vertices ordered 1..N), edges
  {x1..xk}, {x2..xk+1}, …, {xn..x_{n+k-1}} form a monotone path of length n.
- **Nk(q,n)** = least N such that every q-coloring of the edges of K^N_k contains a monochromatic
  monotone path of length n.
- **Pd(n)** = number of n×⋯×n (d-dimensional) integer partitions with entries from {0,…,n}
  (a d-dimensional hypermatrix, decreasing in each line).
- **Theorem 1 (main):** For all q≥2, n≥2: **N3(q,n) = P_{q-1}(n) + 1.**
  Concrete values: P_1(n) = (2n choose n); P_2(n) = Π_{1≤i,j,k≤n} (i+j+k−1)/(i+j+k−2)
  (MacMahon). Hence N3(2,n) = (2n choose n) + 1, N3(3,n) = P_2(n)+1.
- **EST follows:** g(n+2,n+2) ≤ N3(2,n), and the cups-caps bound g(n,n) ≤ (2n-4 choose n-2)+1
  is the q=2 case; N3(2,a,b) = (a+b choose a)+1 (generalizes to the two-sided cups-caps).
- **Higher uniformity:** Theorem 3/4 give Nk(q,n) bounded by towers; e.g. Nk(2,n) =
  t_{k-1}((2−o(1))n) (Cor 2), resolving the Eliáš–Matoušek problem; for k=3: N3(q,n) = 2^{Θ(n^{q-1})}.

## The new pigeonhole proof of EPS (the exact structure the run can reuse)

The upper bound N3(q,n) ≤ P_{q-1}(n)+1 is proved by a **Seidenberg-style injectivity** argument:
- For each edge uv (u<v), record C(uv) = (1+n_1,…,1+n_q) ∈ [n]^q, where n_i is the length of the
  longest color-i monotone path ending at edge {u,v}.
- For each vertex v, D(v) = {x ∈ [n]^q : x ≼ C(uv) for some u<v} is a down-set in [n]^q.
- Down-sets in [n]^q ⟷ (q−1)-dimensional partitions (Observation 2.1), of which there are P_{q-1}(n).
- If u<v had D(u)=D(v), then C(uv) ∈ D(u) gives some t<u with C(uv) ≼ C(tu); but the longest
  color-c path ending at {t,u} (c = color of {t,u,v}) extends to a longer one ending at {u,v},
  contradiction. So D is injective on vertices; N ≤ P_{q-1}(n).

The lower bound N3(q,n) > P_{q-1}(n) identifies vertices with distinct d-dimensional partitions
ordered lexicographically and colors each edge {A≺B≺C} by the coordinate i where δ(B,C) exceeds
δ(A,B), or d+1 = q when no such i exists; a monochromatic path then forces a strictly increasing
coordinate (or partition entry), bounding its length.

## Direct bearing on this run

1. **Cups-caps from a pigeonhole, not a recursion.** The run's oracle / structural work can verify the
   ES cups-caps bound g(n,n)=(2n-4 choose n-2)+1 by this injective down-set map, giving an independent
   handling of the exact f(k,ℓ) value that the Morris–Soltan survey (in library) proves by recursion.
2. **The exact count is partitions, not binomials.** N3(2,n) = (2n choose n)+1 is P_1(n)+1; the
   (2n-4 choose n-2)+1 EST bound is a *combinatorial-pressure* consequence, not the tight count. The
   distinction matters for any argument that tries to push the cups-cap budget: the true extremal
   count for avoiding both is controlled by partition enumeration, not by the binomial alone.
3. **The injectivity map is the same mechanism as Baek's α-statistic** (which maps an a-cap,b-cup-free
   config into the grid simplex T_{a,b} of size (a+b-4 choose a-2)). This source is where that injectivity
   comes from and states it in its cleanest (down-set) form. A run trying to bound the size of a
   cap/cup-free near-extremal set can build its oracle on this exact injectivity.
4. **Caveat (abstract vs realizable), the run's standing warning.** N3 refers to *arbitrary*
   colorings of ordered 3-uniform hypergraphs; the lower-bound constructions realize as abstract
   colorings, and Balko–Valtr (in library) showed the corresponding *geometric* conjecture is NOT
   settled by abstract-colorings bounds. Use the injectivity as a structural constraint, but do not
   cite the abstract-coloring N3 results as geometric ones without the realizability/pseudolinearity
   argument.

## claim blocks (for CLAIMS.md)

```claim
id: ms-n3q-partition-count
statement: N3(q,n) = P_{q-1}(n)+1, where N3(q,n) is the least N such that every q-coloring of the ordered complete 3-uniform hypergraph on N vertices has a monochromatic monotone path of length n, and P_d(n) is the number of d-dimensional n×⋯×n integer partitions with entries in {0,…,n}. In particular N3(2,n) = (2n choose n)+1 and N3(3,n) = P_2(n)+1.
hypotheses: arbitrary colorings of order-colored 3-uniform hypergraphs (not restricted to realizable/pseudolinear colorings).
holds-here: true as a statement about the abstract ordered-hypergraph model; NOT directly a geometric statement — the geometry needs the realizability/pseudolinearity constraint on top (Balko–Valtr show the abstract generalization of the ES conjecture fails).
status: asserted-by-source (Theorem 1 of arXiv:1206.4001, proofs given; advanced, not independently re-derived here).
bearing: the exact structural source of the cups-caps budget: avoiding both an n-cap and n-cup is controlled by partition enumeration P_1(n) = (2n choose n), and the ES cups-caps bound (2n-4 choose n-2)+1 is a combinatorial-pressure consequence this run's oracle can verify via the down-set injectivity.
anchor: research/sources/moshkovitz-shapira - Ramsey theory integer partitions new proof of ES - arxiv1206.4001.full.md
```

```claim
id: ms-esz-downset-injectivity
statement: The Erdős–Szekeres cups-caps theorem g(n,n) ≤ (2n-4 choose n-2)+1 follows from a pigeonhole/injectivity proof: assign each edge uv the down-set D(v) of label-vectors ≼ C(uv); D is injective on vertices, and down-sets in [n]^q biject with (q−1)-dimensional partitions. This is a Seidenberg-style proof, distinct from the original recursion.
hypotheses: order-colorings of K^3_N; for the geometric cups-caps bound, the realizability of the coloring (points vs abstract triples).
holds-here: true; the injectivity is exactly the mechanism Baek's α-statistic uses, and this is the cleanest statement of it.
status: asserted-by-source (Section 2.1 proof of arXiv:1206.4001; the EST bound g(n,n)≤(2n-4 choose n-2)+1 itself is independently in the library via Morris–Soltan and the 1935 paper).
bearing: a structural fact the run's oracle can verify: for any set avoiding caps and cups of given sizes, the down-set map is injective with the partition count as the extremal size. Directly relevant to structural lemmas on hypothetical extremal sets.
anchor: research/sources/moshkovitz-shapira - Ramsey theory integer partitions new proof of ES - arxiv1206.4001.full.md
```
