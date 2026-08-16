<!-- source: https://arxiv.org/html/2608.02675v1 | converted from HTML -->

A 60-Vertex Lower Bound for Cubic BipartiteCounterexamples to the Erdős–Gyárfás Conjecture

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: CC BY 4.0][2]

arXiv:2608.02675v1 [math.CO] 02 Aug 2026

# A 60-Vertex Lower Bound for Cubic Bipartite
Counterexamples to the Erdős–Gyárfás Conjecture

Julius Tranquilli Email: [jtranqs@gmail.com][3]

2 August 2026
[DOI: 10.5281/zenodo.21695513][4]

###### Abstract

A certified exhaustive computation shows that every simple cubic bipartite graph on at most 58 58 vertices contains a cycle of length 4 4, 8 8, or 16 16. Consequently, any cubic bipartite counterexample to the Erdős–Gyárfás conjecture has at least 60 60 vertices, improving the established published lower bound of 30 30.

The proof begins with a Moore-bound observation: below 62 62 vertices, a cubic bipartite graph avoiding 4 4 - and 8 8 -cycles must contain a 6 6 -cycle. Viewing the graph as the Levi graph of a linear symmetric v 3 v_{3} -configuration turns this 6 6 -cycle into a Berge triangle. Up to symmetry, only two rooted extensions are possible. A complete restricted-growth search on at most 29 29 points closes both search trees. The computation is checked by two separately implemented searches using different C 16 C_{16} oracles and by a static witness certificate. Source code, certificates, and reproduction instructions are archived with the paper.

Keywords. Erdős–Gyárfás conjecture; cubic bipartite graphs; prescribed cycle lengths; exhaustive generation; symmetric configurations; computer-assisted proof.

2020 Mathematics Subject Classification. Primary 05C38; Secondary 05C30, 68V05.

## 1 Introduction

The Erdős–Gyárfás conjecture asks whether every finite simple graph of minimum degree at least three contains a simple cycle whose length is a power of two [5]. In a simple graph the first relevant lengths are 4, 8, 16, 32, … 4,8,16,32,\ldots. The conjecture remains open, although it is known for several restricted graph classes; examples include 3 3 -connected cubic planar graphs [6], P 10 P_{10} -free graphs [8], and, with computer assistance, P 13 P_{13} -free graphs [7]. Recent work also gives strong structural restrictions on a minimal counterexample [4].

Numerically, the result raises the established published lower bound applicable to the cubic-bipartite class from n ≥ 30 n\geq 30 to n ≥ 60 n\geq 60, and raises the newest public computational bound from n ≥ 32 n\geq 32 to n ≥ 60 n\geq 60.

This paper concerns the finite-order frontier inside the class of simple cubic bipartite graphs. Its main result is deliberately stated in a stronger form than a bare verification of the conjecture.

###### Theorem 1 (Finite cubic-bipartite frontier).

Every simple cubic bipartite graph G G with

 | | V ⁡ ( G) | ≤ 58 |V(G)|\leq 58 |  |

contains a simple cycle of length 4 4, 8 8, or 16 16.

###### Corollary 2.

Any simple cubic bipartite counterexample to the Erdős–Gyárfás conjecture has at least 60 60 vertices.

###### Proof.

Let L L and R R be the two bipartition classes of a counterexample G G. Cubicity gives

 | 3 ​ | L | = | E ⁡ ( G) | = 3 ​ | R |, 3|L|=|E(G)|=3|R|, |  |

so | L | = | R | |L|=|R| and | V ⁡ ( G) | |V(G)| is even. Theorem 1 excludes all possible orders through 58 58; the next possible order is 60 60. ∎

### 1.1 Comparison with previous bounds

Markström’s 2004 computation established the customary cubic lower bound n ≥ 30 n\geq 30 [9]. The accessible abstract of a 2011 bipartite computation also states 30 30, although later sources attribute 32 32 to that work [11, 12, 8]. Separately, a public 2026 SAT/SAT-Modulo-Symmetries computation excludes all minimum-degree-three graphs through order 31 31, giving the more broadly applicable bound n ≥ 32 n\geq 32 [1]. Table 1 records both comparisons.

Table 1: Comparison with the previously applicable finite-order bounds.

Comparison source | Previous | Present | Increase | Newly excluded cubic-bipartite orders |

Published cubic result (Markström, 2004) | n ≥ 30 n\geq 30 | n ≥ 60 n\geq 60 | 30 30 | 30, 32, …, 58 30,32,\ldots,58 (15 orders) |

Public minimum-degree-three computation (2026) | n ≥ 32 n\geq 32 | n ≥ 60 n\geq 60 | 28 28 | 32, 34, …, 58 32,34,\ldots,58 (14 orders) |

Theorem 1 also shows that one of the first three relevant power-of-two cycle lengths is forced; no 32 32 -cycle is needed.

### 1.2 Proof outline

The proof has two ingredients: a short structural reduction and a finite certified search. A cubic bipartite graph is first represented as the Levi graph of a symmetric 3 3 -uniform, 3 3 -regular set system. An edge-rooted Moore bound then forces a C 6 C_{6}, hence a Berge triangle. After normalizing that triangle, only two root orbits remain. A universal restricted-growth search with point cap 29 29 exhausts both orbits and recognizes a completed configuration as soon as all introduced points are cubic. The resulting certificate covers the entire range v ≤ 29 v\leq 29 at once.

## 2 Incidence configurations and cycle translations

Let G = ( X, Y, E) G=(X,Y;E) be a connected simple cubic bipartite graph. As in the proof of Corollary 2, write

 | | X | = | Y | =: v, | V ⁡ ( G) | = 2 ​ v. |X|=|Y|=:v,\qquad|V(G)|=2v. |  |

For each y ∈ Y y\in Y, let B y = N G ​ ( y) B_{y}=N_{G}(y) and regard ℬ = ( B y) y ∈ Y \mathcal{B}=(B_{y})_{y\in Y} as an indexed family of three-element blocks on the point set X X. Repeated triples are allowed at this stage: distinct vertices of Y Y remain distinct block indices even if they have the same neighborhood. The family has v v indexed blocks, and each point belongs to exactly three of them.

###### Proposition 3 (Incidence translation).

The neighborhood construction is a bijection, up to the natural relabelings, between connected simple cubic bipartite graphs with specified bipartition ( X, Y) (X,Y) and connected 3 3 -uniform, 3 3 -regular incidence structures ( X, ( B y) y ∈ Y) (X,(B_{y})_{y\in Y}) having v v points and v v indexed blocks.

###### Proof.

The preceding construction gives the incidence structure. Conversely, make one graph vertex for each point and one for each block index y y, and join x x to y y precisely when x ∈ B y x\in B_{y}. Uniformity gives degree three on the block side, regularity gives degree three on the point side, and the two kinds of objects form a bipartition. Each membership is a Boolean relation, so there is at most one edge between a given point and block index even when two indexed blocks are equal. The two notions of connectedness are the same because an incidence walk is exactly a graph walk in the constructed bipartite graph. ∎

###### Definition 4.

An indexed triple system is *linear*if blocks with distinct indices have at most one common point; equivalently, no unordered pair of points occurs in two indexed blocks.

###### Lemma 5 ( C 4 C_{4}).

The incidence graph contains a simple 4 4 -cycle if and only if two distinct blocks contain the same pair of points.

###### Proof.

A 4 4 -cycle in a bipartite incidence graph alternates as

 | x, B, x ′, B ′, x x,B,x^{\prime},B^{\prime},x |  |

with x ≠ x ′ x\neq x^{\prime} and B ≠ B ′ B\neq B^{\prime}. Thus x, x ′ ∈ B ∩ B ′ x,x^{\prime}\in B\cap B^{\prime}. Conversely, two blocks sharing distinct points x, x ′ x,x^{\prime} give exactly this 4 4 -cycle. ∎

By Lemma 5, it suffices after the first rejection test to work with linear triple systems. These are the symmetric combinatorial v 3 v_{3} -configurations of the configuration literature; their Levi graphs are exactly the cubic bipartite graphs of girth at least six [2, 3].

A Berge cycle of length k ≥ 3 k\geq 3 consists of distinct blocks B 0, …, B k − 1 B_{0},\ldots,B_{k-1} and distinct points p 0, …, p k − 1 p_{0},\ldots,p_{k-1} with p i ∈ B i ∩ B i + 1 p_{i}\in B_{i}\cap B_{i+1}, where indices are read modulo k k. Equivalently, it is a simple C 2 ​ k C_{2k} in the Levi graph; in particular, a C 6 C_{6} is a Berge triangle.

#### Worked example.

Take

 | B 1 = { a, b, c }, B 2 = { c, d, e }, B 3 = { e, f, a }. B_{1}=\{a,b,c\},\qquad B_{2}=\{c,d,e\},\qquad B_{3}=\{e,f,a\}. |  |

Their successive intersection points are c, e, a c,e,a. In the Levi graph these incidences form the alternating cycle shown in Figure 1.

a a B 1 B_{1} c c B 2 B_{2} e e B 3 B_{3} b b d d f f Figure 1: A Berge triangle and its Levi-graph C 6 C_{6}. The blue cycle is a − B 1 − c − B 2 − e − B 3 − a a-B_{1}-c-B_{2}-e-B_{3}-a; the gray edges show the third point of each block.

A familiar global example is the Fano plane: its seven points and seven lines form a symmetric 7 3 7_{3} -configuration, and its Levi graph is the cubic bipartite Heawood graph.

###### Lemma 6 ( C 8 C_{8}).

In a linear triple system, the incidence graph contains a simple 8 8 -cycle if and only if there are four distinct blocks B 0, B 1, B 2, B 3 B_{0},B_{1},B_{2},B_{3} and four distinct points p 0, p 1, p 2, p 3 p_{0},p_{1},p_{2},p_{3} such that

 | p i ∈ B i ∩ B i + 1 ( i ​ mod ​ 4). p_{i}\in B_{i}\cap B_{i+1}\qquad(i\ \mathrm{mod}\ 4). |  |

In other words, the blocks contain a Berge quadrilateral.

###### Proof.

A simple 8 8 -cycle alternates between four distinct point vertices and four distinct block vertices. Reading it cyclically gives the displayed incidences. Conversely, those incidences form the alternating closed walk

 | p 0, B 1, p 1, B 2, p 2, B 3, p 3, B 0, p 0. p_{0},B_{1},p_{1},B_{2},p_{2},B_{3},p_{3},B_{0},p_{0}. |  |

The stipulated distinctness makes this walk a simple 8 8 -cycle. Linearity ensures that a pair of consecutive blocks has at most one intersection point, so the test is unambiguous. ∎

###### Lemma 7 (Incremental C 16 C_{16} oracle).

Let H H be a partial incidence graph with no C 16 C_{16}, and add a new block vertex b b adjacent to the three points in B = { x, y, z } B=\{x,y,z\}. A new simple C 16 C_{16} is created if and only if H H contains a simple path of length 14 14 between two distinct members of B B.

x x y y b b z z old simple path in H H ( 14 14 edges) two new cycle edges Figure 2: The incremental C 16 C_{16} test. The old 14 14 -edge path and the two highlighted edges through the new block vertex b b form a 16 16 -cycle. The third incidence b ​ z bz is not used by this cycle.

###### Proof.

Any newly created C 16 C_{16} must use b b and exactly two of its incident edges. Deleting b b from that cycle leaves a simple 14 14 -edge path in H H. Conversely, adding b b and the two corresponding incidence edges closes any such path into a simple 16 16 -cycle, as in Figure 2. ∎

The statement allows one or two members of B B to be newly introduced points. Such a point has degree zero in H H, so it cannot be an endpoint of an old nontrivial path; the equivalence remains valid without a special case.

## 3 Triangle-rooted proof

### 3.1 Moore reduction and two normalized roots

###### Lemma 8 (Edge-rooted Moore reduction).

Every simple cubic bipartite graph on at most 58 58 vertices with no C 4 C_{4} and no C 8 C_{8} contains a C 6 C_{6}.

###### Proof.

Suppose instead that G G also has no C 6 C_{6}, and choose an edge u ​ v uv in one of its components. Since G G is simple and bipartite, that component has girth at least 10 10. Starting from u u, without using u ​ v uv, expose the nonbacktracking cubic tree through depth four; its level sizes are

 | 1, 2, 4, 8, 16. 1,2,4,8,16. |  |

Do the same from v v. A repeated vertex within one exposure gives a cycle of length at most 8 8. An intersection between the two exposures gives, together with u ​ v uv, a cycle of length at most 9 9, which is even by bipartiteness and hence has length at most 8 8. Thus all exposed vertices are distinct, so the component has at least

 | 2 ​ ( 1 + 2 + 4 + 8 + 16) = 62 2(1+2+4+8+16)=62 |  |

vertices, a contradiction. ∎

###### Lemma 9 (Triangle-root orbits).

Let ℋ \mathcal{H} be a linear 3 3 -uniform configuration containing a Berge triangle. After relabeling, its three triangle blocks are

 | { 0, 1, 3 }, { 1, 2, 4 }, { 0, 2, 5 }. \{0,1,3\},\qquad\{1,2,4\},\qquad\{0,2,5\}. |  |

Up to the stabilizer of this rooted triangle, the final block through point 0 0 is one of

 | { 0, 4, 6 }, { 0, 6, 7 }. \{0,4,6\},\qquad\{0,6,7\}. |  |

(a) rooted Berge triangle 0 0 T 1 T_{1} 1 1 T 2 T_{2} 2 2 T 3 T_{3} 3 3 4 4 5 5 red: already paired with 0 0 green: available old point (b) final block through 0 0 R R 0 0 4 4 6 6 { 0, 4, 6 } \{0,4,6\} R R 0 0 6 6 7 7 { 0, 6, 7 } \{0,6,7\} Figure 3: The forced triangle and its two normalized extensions. Here T 1 = { 0, 1, 3 } T_{1}=\{0,1,3\}, T 2 = { 1, 2, 4 } T_{2}=\{1,2,4\}, and T 3 = { 0, 2, 5 } T_{3}=\{0,2,5\}. Linearity excludes 1, 2, 3, 5 1,2,3,5 from the final block through 0 0, leaving either the old point 4 4 and one new point, or two new points.

###### Proof.

The three intersection points and the three remaining triangle points are distinct, so they may be labeled as in Figure 3. The two existing blocks through 0 0 pair it with 1, 2, 3, 5 1,2,3,5, which linearity excludes from its final block. The only available old point is 4 4. Thus the block contains either 4 4 and one new point or two new points. First-occurrence labeling gives 6 6, or 6, 7 6,7, and the rooted-triangle stabilizer makes all choices within each form equivalent. ∎

#### Restricted-growth extension.

After installing one of the two roots, the search labels points in order of first occurrence. At each state it chooses the least introduced point p p of degree below three and proposes its remaining blocks { p, q, r } \{p,q,r\} in lexicographic order. Eligible old labels exceed p p, have degree below three, and have not already been paired with p p; a proposal may instead use the next fresh label, or the next two fresh labels together. The search rejects a proposal that violates a degree or pair constraint or creates a Berge cycle of length 4 4 or 8 8, and otherwise inserts it and recurses. It records a completion as soon as every introduced point has degree three, whether or not the cap of 29 29 points has been reached.

###### Proposition 10 (Triangle-rooted coverage).

Every connected linear symmetric v 3 v_{3} -configuration with v ≤ 29 v\leq 29 that contains a Berge triangle and has no Berge cycles of lengths 4 4 or 8 8 occurs as a completed state in one of the two triangle-rooted cap- 29 29 restricted-growth trees.

###### Proof.

Choose a Berge triangle and apply Lemma 9. Install its three blocks and the appropriate fourth block through point 0 0. The preinstalled block { 1, 2, 4 } \{1,2,4\} is lexicographically first among the blocks with least point 1 1: any other such block cannot reuse a point already paired with 1 1. Begin the ordinary restricted-growth recursion at point 1 1, after this block.

Maintain the following invariant before processing a point p p: every target block with smaller least point has been inserted; the inserted target blocks through p p form a lexicographic initial segment; and introduced labels are consecutive and follow first occurrence. The normalized root establishes the invariant at p = 1 p=1.

Let B B be the first target block through p p not yet inserted. Every block containing p p and a smaller point was inserted when that smaller point was processed, so the other two points of B B have labels greater than p p. Previously unseen points receive the next one or two labels. Thus B B occurs among the generator’s proposals and is later than the preceding block through p p. It passes the degree and pair tests because the target is linear, and it passes the cycle tests because the target has no Berge cycles of lengths 4 4 or 8 8. Inserting B B preserves the invariant; when p p becomes cubic, the recursion advances to the least unfinished introduced point.

If the introduced points formed a proper subset closed under their incident blocks, the incidence graph would be disconnected. Hence connectedness ensures that every target point is eventually introduced. Since there are at most 29 29 points, no label outside the cap is needed. Once all introduced points are cubic, the tree recognizes the completed configuration immediately, even if fewer than 29 29 points were introduced. ∎

### 3.2 Certified finite search

One implementation uses simple-path DFS for its C 16 C_{16} oracle; a second joins complete lists of 7 7 -edge half-paths. Both use 29 29 as a point cap and test for a completion whenever all introduced points have degree three. Their cap- 29 29 totals are:

Table 2: Universal cap- 29 29 triangle-rooted search, split by root orbit.

orbit | states | attempted | structural | C 8 C_{8} | C 16 C_{16} | completions |

1 | 1,405 | 106,964 | 7,184 | 63,526 | 34,850 | 0 |

2 | 20,088 | 1,655,404 | 113,012 | 1,208,473 | 313,832 | 0 |

Total | 21,493 | 1,762,368 | 120,196 | 1,271,999 | 348,682 | 0 |

A static certificate contains one stream for each triangle-root orbit. The streaming checker reconstructs the appropriate root, every state, and every candidate. It recomputes structural rejections, validates positive C 8 C_{8} and C 16 C_{16} witnesses, recursively checks expansion records, and rejects any completed configuration. Crucially, completion is tested at the number of points actually introduced, rather than only at the cap. Thus each stream simultaneously covers every smaller side size represented by its root orbit.

###### Proposition 11 (Certified universal triangle search).

The two searches were implemented separately and use different C 16 C_{16} oracles; they agree on every counter and transcript hash for both cap- 29 29 roots. A third streaming checker accepts both certificate streams with zero completions. Consequently, no connected linear symmetric v 3 v_{3} -configuration with v ≤ 29 v\leq 29 that contains a Berge triangle avoids Berge cycles of lengths 4 4 and 8 8.

###### Proof.

The checker follows the deterministic candidate schedule: each rejection has a condition or positive cycle witness checked directly, while every expansion recursively consumes its child stream. An induction over this recursion shows that an accepted stream accounts for every proposal in its rooted search tree. Malformed, truncated, trailing, counter-tampered, or witness-tampered streams are rejected. Accepted streams therefore close both cap- 29 29 trees. Proposition 10 converts this tree exhaustion into the stated finite result. ∎

###### Computer-assisted proof of Theorem 1.

Suppose G G is a simple cubic bipartite graph on at most 58 58 vertices with no C 4, C 8, C_{4},C_{8}, or C 16 C_{16}, and choose a connected component H H. Every component of a cubic graph is cubic. Lemma 8 gives a C 6 C_{6} in H H. Proposition 3 translates H H into a connected symmetric v 3 v_{3} -configuration with v = | V ⁡ ( H) | / 2 ≤ 29 v=|V(H)|/2\leq 29. Lemma 5 makes it linear, and the C 6 C_{6} becomes a Berge triangle. The absent C 8 C_{8} and C 16 C_{16} become absent Berge cycles of lengths 4 4 and 8 8, contradicting Proposition 11. ∎

### 3.3 Six deepest kernels

The state-dumping checker reconstructs 337 337 surviving states with 19 19 blocks, the maximum depth attained by the triangle-rooted search. Every such state has already introduced all 29 29 points allowed by the cap. The retained mapping certificate supplies a point permutation and block permutation from every labeled state to one of six representatives.

Table 3: The six color-preserving classes among the deepest triangle-rooted states.

kernel | labelled occurrences | deficient points | compatible-pair graph |

K 1 K_{1} | 2 | 17 | 3 ​ K 1, 2 3K_{1,2} |

K 2 K_{2} | 20 | 18 | K 2 ⊔ 2 ​ K 1, 2 K_{2}\sqcup 2K_{1,2} |

K 3 K_{3} | 20 | 18 | K 2 ⊔ 2 ​ K 1, 2 K_{2}\sqcup 2K_{1,2} |

K 4 K_{4} | 75 | 18 | 2 ​ K 1, 2 2K_{1,2} |

K 5 K_{5} | 200 | 19 | K 1, 2 K_{1,2} |

K 6 K_{6} | 20 | 19 | K 1, 2 K_{1,2} |

Total | 337 |  |  |

In the table and in Figure 4, isolated deficient points are omitted from the displayed graph types.

For one of these states, call a point *deficient*when its degree is less than three. Form a graph on the deficient points by joining x x and y y precisely when they do not already share a block and the old incidence graph contains neither a simple 6 6 -edge path nor a simple 14 14 -edge path between them. Call such a pair compatible.

A new block { x, y, z } \{x,y,z\} can avoid C 4, C 8, C_{4},C_{8}, and C 16 C_{16} only if all three pairs are compatible: an old shared block gives a C 4 C_{4}, while an old path of length 6 6 or 14 14 is closed by the new block into a C 8 C_{8} or C 16 C_{16}, respectively. A legal new block therefore requires a triangle in the compatible-pair graph.

K 1: 3 ​ K 1, 2 K_{1}:\ 3K_{1,2} K 2: K 2 ⊔ 2 ​ K 1, 2 K_{2}:\ K_{2}\sqcup 2K_{1,2} K 3: K 2 ⊔ 2 ​ K 1, 2 K_{3}:\ K_{2}\sqcup 2K_{1,2} K 4: 2 ​ K 1, 2 K_{4}:\ 2K_{1,2} K 5: K 1, 2 K_{5}:\ K_{1,2} K 6: K 1, 2 K_{6}:\ K_{1,2} Figure 4: The compatibility graphs of the six terminal kernels, with isolated vertices omitted. Every displayed graph is a forest and therefore contains no triangle.

###### Proposition 12 (Six deepest kernels).

The 337 337 triangle-rooted states with 19 19 blocks form the six color-preserving isomorphism classes in Table 3. On their existing 29 29 -point sets, none admits a twentieth block without creating a C 4, C 8, C_{4},C_{8}, or C 16 C_{16} in its Levi graph.

###### Proof.

The mapping certificate is checked row by row against the 337 337 states reconstructed from the two witness streams. The independent Python checker verifies that every point map and block map is a permutation and preserves every incidence. It then recomputes simple paths of lengths 6 6 and 14 14 for every pair of deficient points in each representative. This gives the forests in Figure 4; restoring the omitted isolated vertices preserves triangle-freeness. Hence no representative admits another block within the 29 29 -point cap. ∎

The six forests explain the deepest terminal obstruction; branches terminating before 19 19 blocks remain covered directly by the two universal witness streams.

## 4 Additional checks

Agreement between the two triangle-rooted searches holds at the level of ordered decision-transcript hashes, not only aggregate counters. An earlier arbitrary-root enumeration, which does not assume a Berge triangle, also gives zero completions throughout v ≤ 29 v\leq 29. The repository contains the full outputs and verification tests for both computations.

For a generator-level comparison, the C 8 C_{8} and C 16 C_{16} filters were disabled and all completed connected linear symmetric v 3 v_{3} -configurations were generated for v = 7, …, 13 v=7,\ldots,13. After color-preserving canonical labeling and deduplication, the resulting graph6 sets agree exactly with nauty 2.9.3 genbg output generated with degree three and at most one common neighbor on the block side [10].

Table 4: Set-level generator comparison. The second column counts rooted and labelled restricted-growth leaves before deduplication; the third is the common number of color-preserving canonical graph6 records.

v v | Rooted/labelled leaves | Canonical configurations |

7 | 1 | 1 |

8 | 4 | 1 |

9 | 44 | 3 |

10 | 496 | 10 |

11 | 7,840 | 31 |

12 | 136,575 | 229 |

13 | 2,337,152 | 2,036 |

The common canonical counts in Table 4 also agree with the published census of Betten, Brinkmann, and Pisanski [2]. This independent overlap checks the restricted-growth generator through v = 13 v=13; completeness beyond that range follows from Proposition 10.

As positive controls, two independent cycle enumerators were applied to 128 128 symmetric 19 3 19_{3} -configurations known to avoid C 4 C_{4} and C 8 C_{8} while containing C 16 C_{16}; both classified every input correctly. The primary implementations and certificate checker still share the mathematical coverage argument in Proposition 10. The computation does not examine side size 30 30, and hence does not exclude an order- 60 60 counterexample.

## 5 Conclusion

The Moore reduction and incidence translation leave two triangle-rooted cap- 29 29 searches. The certified search rules out a completion in either orbit, and its 337 337 deepest states collapse to six terminal kernels with triangle-free compatibility graphs. Together, the structural reduction and certified enumeration prove that every simple cubic bipartite graph on at most 58 58 vertices contains a 4 4 -, 8 8 -, or 16 16 -cycle. The lower bound for any cubic bipartite counterexample is therefore 60 60.

## Artifact availability

The preprint is archived on Zenodo at [DOI: 10.5281/zenodo.21695513][4] as version v1.0.0. Source code, certificates, verification programs, logs, and reproduction instructions are available from the accompanying [GitHub repository][5], which also provides an immutable release, a complete SHA-256 manifest, and research-provenance documentation.

## AI disclosure

OpenAI ChatGPT materially assisted the initial research, including developing computational and structural approaches, portions of the incidence-based code and preliminary arguments, running and interpreting computations, and an initial literature audit. OpenAI Codex subsequently assisted with code and artifact auditing, reproducibility checks, additional verifiers and certificates, integration of the triangle-rooted method, and drafting and editing the manuscript and documentation. A custom closed-source coding and formalization harness built on a fork of Codex also assisted with later code, formalization, and verification work; it is not included in the public artifact or treated as independent evidence. Julius Tranquilli selected and directed the project and accepts responsibility for the final work; the retained code, logs, exact outputs, certificates, and mathematical arguments, rather than AI assertions, form the evidentiary basis, and a fuller activity-level account is included in the repository.

## References

- [1] Arjun Balaji. Erdős–Gyárfás Conjecture for Minimum-Degree-Three Graphs. Public GitHub repository, 2026. The bound n ≥ 32 n\geq 32 was recorded in commit 53502b0f on 3 July 2026; accessed 29 July 2026. [https://github.com/ArjunBalaji79/erdos-gyarfas-min-degree-3][6].
- [2] Anton Betten, Gunnar Brinkmann, and Tomaž Pisanski. Counting symmetric configurations v 3 v_{3}. *Discrete Applied Mathematics*, 99(1–3):331–338, 2000. [https://doi.org/10.1016/S0166-218X(99)00143-2][7].
- [3] Marko Boben. Irreducible ( v 3) (v_{3}) configurations and graphs. *Discrete Mathematics*, 307(3–5):331–344, 2007. [https://doi.org/10.1016/j.disc.2006.07.015][8].
- [4] Avery Carr. Every Minimal Counterexample to the Erdős–Gyárfás Conjecture Is Predominantly Cubic, 2026. arXiv:2605.22844. [https://arxiv.org/abs/2605.22844][9].
- [5] Paul Erdős. Some Old and New Problems in Various Branches of Combinatorics. *Discrete Mathematics*, 165–166:227–231, 1997.
- [6] Christopher Carl Heckman and Roi Krakovski. Erdős–Gyárfás Conjecture for Cubic Planar Graphs. *Electronic Journal of Combinatorics*, 20(2):P7, 2013.
- [7] Anand Shripad Hegde, R. B. Sandeep, and P. Shashank. Erdős–Gyárfás Conjecture on Graphs without Long Induced Paths, 2025. arXiv:2410.22842, version 2, 11 February 2025. [https://arxiv.org/abs/2410.22842][10].
- [8] Zhiquan Hu and Changlong Shen. The Erdős–Gyárfás Conjecture Holds for P 10 P_{10} -Free Graphs. *Discrete Mathematics*, 347(12):114175, 2024.
- [9] Klas Markström. Extremal Graphs for Some Problems on Cycles in Graphs. *Congressus Numerantium*, 171:179–192, 2004. Publication record: [https://urn.kb.se/resolve?urn=urn:nbn:se:umu:diva-19969][11].
- [10] Brendan D. McKay and Adolfo Piperno. Practical Graph Isomorphism, II. *Journal of Symbolic Computation*, 60:94–112, 2014. [https://doi.org/10.1016/j.jsc.2013.09.003][12].
- [11] Pouria Salehi Nowbandegani and Hossein Esfandiari. An Experimental Result on the Erdős–Gyárfás Conjecture in Bipartite Graphs. In *14th Workshop on Graph Theory: Colourings, Independence and Domination*, 2011. Accessible proceedings abstract states a lower bound of 30; later sources sometimes attribute 32. [http://www.cid.uz.zgora.pl/2011/files/AbstractsPdf/Salehi.pdf][13].
- [12] Pouria Salehi Nowbandegani, Hossein Esfandiari, Mohammad Hassan Shirdareh Haghighi, and Khodakhast Bibak. On the Erdős–Gyárfás Conjecture in Claw-Free Graphs. *Discussiones Mathematicae Graph Theory*, 34(3):635–640, 2014. A later source attributing the bipartite bound 32 to the 2011 work.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:jtranqs@gmail.com
[4]: https://doi.org/10.5281/zenodo.21695513
[5]: https://github.com/floor-licker/erdos-gyarfas-cubic-bipartite
[6]: https://github.com/ArjunBalaji79/erdos-gyarfas-min-degree-3
[7]: https://doi.org/10.1016/S0166-218X(99)00143-2
[8]: https://doi.org/10.1016/j.disc.2006.07.015
[9]: https://arxiv.org/pdf/2605.22844
[10]: https://arxiv.org/pdf/2410.22842
[11]: https://urn.kb.se/resolve?urn=urn:nbn:se:umu:diva-19969
[12]: https://doi.org/10.1016/j.jsc.2013.09.003
[13]: http://www.cid.uz.zgora.pl/2011/files/AbstractsPdf/Salehi.pdf
