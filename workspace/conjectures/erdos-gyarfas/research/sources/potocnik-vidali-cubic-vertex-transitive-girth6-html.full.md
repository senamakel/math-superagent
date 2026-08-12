<!-- source: https://arxiv.org/html/2005.01635v4 | converted from HTML -->

Cubic vertex-transitive graphs of girth six

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2005.01635v4 [math.CO] 03 Jan 2025

# Cubic vertex-transitive graphs of girth six Thanks: Supported in part by the Slovenian Research Agency, projects J1-1691, P1-0285, and P1-0294

Primož Potočnik Address: Primož Potočnik,
Faculty of Mathematics and Physics, University of Ljubljana,
Jadranska 19, SI-1000 Ljubljana, Slovenia;
also affiliated with:
IMFM, Jadranska 19, SI-1000 Ljubljana, Slovenia. Email address: [primoz.potocnik@fmf.uni-lj.si][3] and Janoš Vidali Address: Janoš Vidali,
Faculty of Mathematics and Physics, University of Ljubljana,
Jadranska 19, SI-1000 Ljubljana, Slovenia.
also affiliated with:
IMFM, Jadranska 19, SI-1000 Ljubljana, Slovenia. Email address: [janos.vidali@fmf.uni-lj.si][4]

###### Abstract.

In this paper, a complete classification of finite simple cubic vertex-transitive graphs of girth 6 6 is obtained. It is proved that every such graph, with the exception of the Desargues graph on 20 20 vertices, is either a skeleton of a hexagonal tiling of the torus, the skeleton of the truncation of an arc-transitive triangulation of a closed hyperbolic surface, or the truncation of a 6 6 -regular graph with respect to an arc-transitive dihedral scheme. Cubic vertex-transitive graphs of girth larger than 6 6 are also discussed.

###### Key words and phrases:

cubic graph, vertex-transitive graph, girth-regular graph

###### 2000 Mathematics Subject Classification

20B25

## 1. Introduction

Cubic vertex-transitive graph are one of the oldest themes in algebraic graph theory, appearing already in the classical work of Foster [13, 14] and Tutte [33], and retaining the attention of the community until present times (see, for example, the works of Coxeter, Frucht and Powers [8], Djoković and Miller [9], Lorimer [23], Conder and Lorimer [6], Glover and Marušič [15], Potočnik, Spiga and Verret [27], Hua and Feng [16], Spiga [30], to name a few of the most influential papers).

The girth (the length of a shortest cycle) is an important invariant of a graph which appears in many well-known graph theoretical problems, results and formulas. In many cases, requiring the graph to have small girth severely restricts the structure of the graph.

Such a phenomenon can be observed when one focuses to a family of graphs of small valence possessing a high level of symmetry. For example, arc-transitive 4 4 -valent graphs of girth at most 4 4 were characterised in [29]. In the case of cubic graphs, even more work has been done. The structure of cubic arc-transitive graphs of girth at most 7 7 and 9 9 was studied in [12] and [7], respectively, and those of girth 6 6 were completely determined in [22]. By requiring more symmetry, some of these results can be pushed further; for example, in [24], cubic 4 4 -arc-transitive graphs of girth at most 13 13 were classified, while in [25], locally 3 3 -transitive graphs of girth 4 4 are considered. Recently, two papers appeared where the condition on arc-transitivity was relaxed (considerably!) to vertex-transitivity; namely as a byproduct of the results proved independently in [10] and [28], all cubic vertex-transitive graphs of girth 5 5 are known. There are several, sometimes surprising, applications of such classification results (see, for example, [5] for an application in the theory of abstract polytopes, [18] for an application regarding the distinguishing number, and [21] for a connection with the question of existence of odd automorphisms of graphs).

The purpose of this paper is to extend the above mentioned classification of cubic vertex-transitive graphs of girth at most 5 5 to a significantly more complex situation of vertex-transitive cubic graphs of girth 6 6. There are three generic sources of cubic vertex-transitive graphs of girth 6 6: hexagonal tessellations of the torus with three hexagons meeting at each vertex (that is, vertex-transitive maps on the torus of type { 6, 3 } \{6,3\} —note that all of them are vertex-transitive), truncations of arc-transitive triangulations of hyperbolic surfaces (that is, truncations of arc-transitive maps of type { 3, ℓ } \{3,\ell\} with ℓ ≥ 7 \ell\geq 7), and truncations of 6 6 -valent graphs admitting an arc-transitive group of automorphisms whose vertex-stabilisers act on the neighbourhoods either as a cyclic or as a dihedral group of degree 6 6 (these objects were dubbed arc-transitive dihedral schemes in [28]). More formal definitions of dihedral schemes and maps will be given in Sections 2.2 and 2.3, respectively.

The main result of this paper states that with the exception of a single graph, the famous Desargues graph on 20 20 vertices (that can also be defined as the generalised Petersen graph GP ⁡ ( 10, 3) \operatorname{GP}(10,3)), every cubic vertex-transitive graph of girth 6 6 arises in one of the above three ways. In Theorem 1, we refine this statement by classifying the cubic vertex-transitive graphs of girth 6 6 by their signature, which, roughly speaking, encodes the distribution of girth cycles throughout the graph.

Let us make this more precise. For an edge e e of a graph Γ \Gamma, let ϵ ⁡ ( e) \epsilon(e) denote the number of girth cycles containing the edge e e. Let v v be a vertex of Γ \Gamma and let { e 1, …, e k } \{e_{1},\ldots,e_{k}\} be the set of edges incident to v v ordered in such a way that ϵ ⁡ ( e 1) ≤ ϵ ⁡ ( e 2) ≤ … ≤ ϵ ⁡ ( e k) \epsilon(e_{1})\leq\epsilon(e_{2})\leq\ldots\leq\epsilon(e_{k}). Following [28], the k k -tuple ( ϵ ⁡ ( e 1), ϵ ⁡ ( e 2), …, ϵ ⁡ ( e k)) (\epsilon(e_{1}),\epsilon(e_{2}),\ldots,\epsilon(e_{k})) is then called the signature of v v. A graph Γ \Gamma is called girth-regular provided that all of its vertices have the same signature (and if in addition ϵ ⁡ ( e 1) = … = ϵ ⁡ ( e k) \epsilon(e_{1})=\ldots=\epsilon(e_{k}), the graph is called girth-edge-regular; see [19]). The signature of a vertex is then called the signature of the graph. Clearly, every vertex-transitive graph is also girth-regular.

We can now state the main result of the paper. The exceptional graphs Ψ n \Psi_{n}, Σ n \Sigma_{n} and Δ n \Delta_{n} appearing in the theorem below are defined in Section 2.4.

###### Theorem 1.

Let Γ \Gamma be a connected cubic graph. Then Γ \Gamma is vertex-transitive and has girth 6 6 if and only if Γ \Gamma is one of the following:

1. (a)

the skeleton of a map of type { 6, 3 } \{6,3\} on a torus, with signature

  - •

( 8, 8, 8) (8,8,8) for Ψ 7 \Psi_{7} (Heawood graph),

  - •

( 6, 6, 6) (6,6,6) for Ψ 8 \Psi_{8} (Möbius-Kantor graph),

  - •

( 4, 5, 5) (4,5,5) for Ψ 9 ≅ Δ 3 \Psi_{9}\cong\Delta_{3},

  - •

( 4, 4, 4) (4,4,4) for Σ 3 \Sigma_{3} (Pappus graph),

  - •

( 3, 4, 5) (3,4,5) for Ψ n \Psi_{n} with n ≥ 10 n\geq 10,

  - •

( 2, 3, 3) (2,3,3) for Δ n \Delta_{n} and Σ n \Sigma_{n} with n ≥ 4 n\geq 4, and

  - •

( 2, 2, 2) (2,2,2) otherwise;

2. (b)

the skeleton of the truncation of an arc-transitive map of type { 3, ℓ } \{3,\ell\} with ℓ ≥ 7 \ell\geq 7, with signature ( 1, 1, 2) (1,1,2);

3. (c)

the truncation of a 6 6 -regular graph Γ ^ \hat{\Gamma} with respect to an arc-transitive dihedral scheme, with signature ( 0, 1, 1) (0,1,1); or

4. (d)

the Desargues graph with signature ( 4, 4, 4) (4,4,4).

Note that all maps of type { 6, 3 } \{6,3\} on the torus are known and have been classified independently by several authors (see for example [3, 17, 20, 31, 32]) and two recent surveys of some of these classifications have appeared in [1, 4]. It is not difficult to see that every toroidal map of type { 6, 3 } \{6,3\} is vertex-transitive. In fact, as was shown in [2], all of them are Cayley graphs on generalised dihedral groups.

As a byproduct of Theorem 1, together with [28, Theorem 1.5], where cubic vertex-transitive graphs of girth 5 5 are classified, we obtain the following refinement of the classification of maps of type { 6, 3 } \{6,3\} (hexagonal tessellations) on the torus:

###### Corollary 2.

Let Γ \Gamma be the skeleton of a map of type { 6, 3 } \{6,3\} on the torus. If Γ \Gamma has no cycles of length less than 6 6, then either Γ \Gamma is one of the graphs Ψ n \Psi_{n} with n ≥ 7 n\geq 7, Σ n \Sigma_{n} with n ≥ 3 n\geq 3, Δ n \Delta_{n} with n ≥ 4 n\geq 4, or the only 6 6 -cycles of Γ \Gamma are the face cycles.

In Section 2, the necessary definitions and auxiliary results are stated. Section 3 is devoted to the proof of Theorem 1, while in Section 4, cubic vertex-transitive graphs of girth larger than 6 6 are discussed.

## 2. Definitions and notation

### 2.1. Graphs

Even though we are mainly interested in simple graphs, it will prove convenient to allow graphs to have loops and parallel edges. For this reason, define a graph as a triple ( V, E, ∂) (V,E,\partial), where V V and E E are the vertex-set and the edge-set of the graph, and ∂: E → { X: X ⊆ V, | X | ≤ 2 } \partial\colon E\to\{X:X\subseteq V,|X|\leq 2\} is a mapping that maps an edge to the set of its end-vertices. If | ∂ ( e) | = 1 |\partial(e)|=1, then e e is a loop. Two edges e e and e ′ e^{\prime} are parallel if ∂ ( e) = ∂ ( e ′) \partial(e)=\partial(e^{\prime}). Graphs with no loops and parallel edges are simple and can be thought of in the usual manner as a pair ( V, ∼) (V,\sim), where V V is the vertex-set and ∼ \sim is an irreflexive symmetric adjacency relation on V V.

The vertex-set and the edge-set of a graph Γ \Gamma are denoted by 𝒱 ⁡ ( Γ) \mathcal{V}(\Gamma) and ℰ ⁡ ( Γ) \mathcal{E}(\Gamma), respectively. Further, we let each edge consist of two mutually inverse arcs, each of the two arcs having one of the end-vertices as its tail. For an arc s s, we denote its inverse by s − 1 s^{-1}. The head of an arc s s is defined as the tail of s − 1 s^{-1}. The set of arcs of a graph Γ \Gamma is denoted by 𝒜 ⁡ ( Γ) \mathcal{A}(\Gamma), and the set of the arcs with their tail being a specific vertex u u by out Γ ⁡ ( u) \operatorname{out}_{\Gamma}(u). The valence of a vertex u u is defined as the cardinality of out Γ ⁡ ( u) \operatorname{out}_{\Gamma}(u).

An automorphism of a graph Γ:= ( V, E, ∂) \Gamma:=(V,E,\partial) is a permutation α \alpha of V ∪ E V\cup E preserving V V and E E and satisfying ∂ ( e α) = { u α, v α } \partial(e^{\alpha})=\{u^{\alpha},v^{\alpha}\} for every edge e ∈ E e\in E such that ∂ ( e) = { u, v } \partial(e)=\{u,v\}. As usual, we denote the group of all automorphisms of Γ \Gamma by Aut ⁡ ( Γ) \operatorname{Aut}(\Gamma).

If Γ \Gamma is a simple graph, then each automorphism of Γ \Gamma is uniquely determined by its action on 𝒱 ⁡ ( Γ) \mathcal{V}(\Gamma), so we may think of it as an adjacency-preserving permutation of 𝒱 ⁡ ( Γ) \mathcal{V}(\Gamma). Observe that every automorphism of Γ \Gamma induces a permutation of 𝒜 ⁡ ( Γ) \mathcal{A}(\Gamma). If G G is a subgroup of Γ \Gamma that acts transitively on vertices, edges or arcs of Γ \Gamma, then we say that Γ \Gamma is G G -vertex-transitive, G G -edge-transitive or G G -arc-transitive, respectively, with the prefix G G typically omitted if G = Aut ⁡ ( Γ) G=\operatorname{Aut}(\Gamma).

### 2.2. Dihedral schemes

Following [28], a dihedral scheme on a graph Γ \Gamma is an irreflexive symmetric relation ↔ \leftrightarrow on 𝒜 ⁡ ( Γ) \mathcal{A}(\Gamma) such that the simple graph ( 𝒜 ( Γ), ↔) (\mathcal{A}(\Gamma),\leftrightarrow) is a 2 2 -regular graph each of whose connected components is the set out Γ ⁡ ( u) \operatorname{out}_{\Gamma}(u) for some u ∈ 𝒱 ⁡ ( Γ) u\in\mathcal{V}(\Gamma). Intuitively, we may think of a dihedral scheme as an arrangement of arcs around each vertex into a non-oriented cycle. The group of all automorphisms of Γ \Gamma that preserve the relation ↔ \leftrightarrow will be denoted by Aut ( Γ, ↔) \operatorname{Aut}(\Gamma,\leftrightarrow) and the dihedral scheme ↔ \leftrightarrow is said to be arc-transitive if Aut ( Γ, ↔) \operatorname{Aut}(\Gamma,\leftrightarrow) acts transitively on 𝒜 ⁡ ( Γ) \mathcal{A}(\Gamma).

Given a dihedral scheme ↔ \leftrightarrow on a graph Γ \Gamma, we define the truncation of Γ \Gamma with respect to ↔ \leftrightarrow as the simple graph Tr ( Γ, ↔) \operatorname{Tr}(\Gamma,\leftrightarrow) whose vertex set is 𝒜 ⁡ ( Γ) \mathcal{A}(\Gamma), with two arcs s, t ∈ 𝒜 ⁡ ( Γ) s,t\in\mathcal{A}(\Gamma) adjacent in Tr ( G, ↔) \operatorname{Tr}(G,\leftrightarrow) if either t ↔ s t\leftrightarrow s or t t and s s are inverse to each other (see the example in Figure 1). Observe that Aut ( Γ, ↔) \operatorname{Aut}(\Gamma,\leftrightarrow) acts as a group of automorphisms of Tr ( Γ, ↔) \operatorname{Tr}(\Gamma,\leftrightarrow), implying that Tr ( Γ, ↔) \operatorname{Tr}(\Gamma,\leftrightarrow) is vertex-transitive whenever the dihedral scheme ↔ \leftrightarrow is arc-transitive.

(a) (b) (c)

Figure 1. (a) The octahedral graph, a 4 4 -regular graph. (b) The truncation of the octahedral graph with respect to the dihedral scheme obtained by considering the drawing (a) as a map (i.e., an octahedron). (c) The truncation of the octahedral graph with respect to a different dihedral scheme. Note that in both truncations, vertices of the graph in (a) have been replaced by 4 4 -cycles.

As was proved in [28, Lemma 3.5], arc-transitive dihedral schemes all arise in the following group theoretical setting. Let Γ \Gamma be a G G -arc-transitive graph (possibly with parallel edges) such that the permutation group G u out Γ ⁡ ( u) G_{u}^{\operatorname{out}_{\Gamma}(u)} induced by the action of the vertex-stabiliser G u G_{u} on out Γ ⁡ ( u) \operatorname{out}_{\Gamma}(u) is permutation isomorphic to the transitive action of 𝔻 d \mathbb{D}_{d}, ℤ d \mathbb{Z}_{d}, or (if d d is even) 𝔻 d 2 \mathbb{D}_{\frac{d}{2}} on d d vertices (here, the symbol 𝔻 d \mathbb{D}_{d} denotes the dihedral group of order 2 ​ d 2d acting naturally on d d points, while ℤ d \mathbb{Z}_{d} is the cyclic group acting transitively on d d points). Fix a vertex u u of Γ \Gamma and choose an adjacency relation ↔ u \leftrightarrow_{u} on out Γ ⁡ ( u) \operatorname{out}_{\Gamma}(u) preserved by G u out Γ ⁡ ( u) G_{u}^{\operatorname{out}_{\Gamma}(u)} in such a way that ( out Γ ( u), ↔ u) (\operatorname{out}_{\Gamma}(u),\leftrightarrow_{u}) is a cycle (note that the assumption on G u out Γ ⁡ ( u) G_{u}^{\operatorname{out}_{\Gamma}(u)} implies that such a relation exists). For every v ∈ 𝒱 ⁡ ( Γ) v\in\mathcal{V}(\Gamma), choose an element g v ∈ G g_{v}\in G such that v g v = u v^{g_{v}}=u, and let ↔ v \leftrightarrow_{v} be the relation on out Γ ⁡ ( v) {\operatorname{out}_{\Gamma}(v)} defined by s ↔ v t s\leftrightarrow_{v}t if and only if s g v ↔ u t g v s^{g_{v}}\leftrightarrow_{u}t^{g_{v}}. Then the union ↔ \leftrightarrow of all ↔ u \leftrightarrow_{u} for u ∈ V ⁡ ( Γ) u\in V(\Gamma) is a dihedral scheme invariant under G G.

We would like to point out that an equivalent definition of dihedral schemes and a generalization of the corresponding truncations was given recently in [10] (see also [11]). To obtain a truncation as defined above, the graph Υ \Upsilon in the definition of the generalised truncation in [10, Section 2] needs to be a cycle.

### 2.3. Maps

Topologically, a map is an embedding of a finite connected graph onto a closed surface in such a way that when the graph is removed from the surface, the connected components (called faces) of what remains are homeomorphic to open disks whose closures are closed disks.

There are several ways to describe a map combinatorially, one way being by specifying a set of walks in the graph that represent the boundaries of the faces of the map. More precisely, let Γ \Gamma be a connected graph and let 𝒯 \mathcal{T} be a set of closed walks in Γ \Gamma such that every edge of Γ \Gamma belongs to precisely two walks in 𝒯 \mathcal{T}. We will also require that every edge is traversed at most once by every walk in 𝒯 \mathcal{T}, even though in the literature often this is not required (the maps that satisfy our additional conditions are then sometimes called polyhedral). For two arcs s s and t t with a common tail, write s ↔ t s\leftrightarrow t if and only if the underlying edges of s s and t t are two consecutive edges on a walk in 𝒯 \mathcal{T}. If ↔ \leftrightarrow is a dihedral scheme, then ( Γ, 𝒯) (\Gamma,\mathcal{T}) is a map with skeleton Γ \Gamma and face walks 𝒯 \mathcal{T}. The topological map can then be reconstructed from such a pair ( Γ, 𝒯) (\Gamma,\mathcal{T}) by thinking of the graph as a 1 1 -dimensional CW complex and then gluing closed disks along its boundary homeomorphically to the closed curves in Γ \Gamma represented by elements of 𝒯 \mathcal{T}. The resulting topological space is then a closed surface, which can be either orientable or non-orientable.

An automorphism of a map ( Γ, 𝒯) (\Gamma,\mathcal{T}) is an automorphism of Γ \Gamma that preserves the set 𝒯 \mathcal{T}. Note that such an automorphism extends to a homeomorphism of the resulting surface preserving the embedded graph. The map is called vertex-, edge- or arc-transitive, provided that its automorphism group acts transitively on the vertices, edges or arcs of the underlying graph Γ \Gamma. If the graph Γ \Gamma is k k -regular and all the closed walks in 𝒯 \mathcal{T} have length ℓ \ell, then the map ( Γ, 𝒯) (\Gamma,\mathcal{T}) is said to be of type { ℓ, k } \{\ell,k\}.

There are two ways in which maps enter the classification of cubic vertex-transitive graphs of girth 6 6. The first is when the skeleton of a map is a cubic graph and the faces form the girth cycles, that is, when the map has type { 6, 3 } \{6,3\} and it contains no shorter cycles than the face walks (in this case, the face walks are cycles, so we may refer to them as face cycles). By computing the genus of the underlying surface using Euler’s formula, one sees that such a map resides either on the Klein bottle or on the torus. However, as was shown in [35], there are no vertex-transitive maps of type { 6, 3 } \{6,3\} and girth more than 4 4 on the Klein bottle. On the other hand, there are numerous toroidal vertex-transitive maps of type { 6, 3 } \{6,3\} and girth 6 6, and all of them are vertex-transitive. As mentioned in Section 1, toroidal maps of type { 6, 3 } \{6,3\} have been extensively studied from different angles and have been independently classified several times (see [4] or [1] for recent surveys).

The second way in which maps yield cubic vertex-transitive graphs of girth 6 6 is by taking (the skeleton of) the truncation of an arc-transitive map of type { 3, ℓ } \{3,\ell\} with ℓ ≥ 7 \ell\geq 7. Here, the truncation of a map ( Γ, 𝒯) (\Gamma,\mathcal{T}) has the usual meaning – note that its skeleton is the truncation of the underlying graph Γ \Gamma with respect to the dihedral scheme appearing in the definition of the map.

### 2.4. Three special families of toroidal graphs

In this section, we define the graphs Ψ n \Psi_{n}, Σ n \Sigma_{n} and Δ n \Delta_{n} appearing in Theorem 1. They are all skeletons of toroidal maps of type { 6, 3 } \{6,3\}, and unlike other toroidal maps of type { 6, 3 } \{6,3\}, they possess 6 6 -cycles other than the face cycles (and no shorter cycles). We will introduce them as Cayley graphs. Recall that a Cayley graph Cay ⁡ ( G, S) \operatorname{Cay}(G,S) on a group G G with the connection set S S, S ⊆ G ∖ { 1 G } S\subseteq G\setminus\{1_{G}\}, S = S − 1 S=S^{-1}, is a simple graph whose vertices are elements of G G, with g, h ∈ G g,h\in G adjacent whenever g ​ h − 1 ∈ S gh^{-1}\in S.

Since a Cayley graph Cay ⁡ ( G, S) \operatorname{Cay}(G,S) is vertex-transitive, it is also girth-regular. One can determine its girth g g by finding the length of the shortest nonempty sequence ( α 1, α 2, …, α g) (\alpha_{1},\alpha_{2},\dots,\alpha_{g}) with α i ∈ S \alpha_{i}\in S ( 1 ≤ i ≤ g 1\leq i\leq g) such that α i ​ α i + 1 ≠ 1 G \alpha_{i}\alpha_{i+1}\neq 1_{G} ( 1 ≤ i ≤ g − 1 1\leq i\leq g-1) and α 1 α 2 ⋯ α g = 1 G \alpha_{1}\alpha_{2}\cdots\alpha_{g}=1_{G}. The signature can then be determined by identifying all such sequences of length g g and counting how many times each element of the connection set appears as the first symbol in these sequences.

In what follows, let 𝔻 d \mathbb{D}_{d} denote the dihedral group of order 2 ​ d 2d acting naturally on d d points, and let ℤ d \mathbb{Z}_{d} be a cyclic group of order d d acting on d d points. For dihedral groups, we will use the presentation 𝔻 n = ⟨ ρ, τ | ρ n, τ 2, ( ρ τ) 2 ⟩ \mathbb{D}_{n}=\left\langle\rho,\tau\;\middle|\;\rho^{n},\tau^{2},(\rho\tau)^{2}\right\rangle – i.e., ρ \rho represents a unit rotation, while τ \tau represents a reflection of the points around some axis. For brevity, we denote ρ i = ρ i \rho_{i}=\rho^{i} and τ i = ρ i ​ τ \tau_{i}=\rho^{i}\tau, where indices are modulo n n. It is easy to see that for all integers i, j i,j, we have ρ i ​ ρ j = ρ i + j \rho_{i}\rho_{j}=\rho_{i+j}, ρ i ​ τ j = τ i + j \rho_{i}\tau_{j}=\tau_{i+j}, τ i ​ ρ j = τ i − j \tau_{i}\rho_{j}=\tau_{i-j} and τ i ​ τ j = ρ i − j \tau_{i}\tau_{j}=\rho_{i-j}. For the direct product 𝔻 n × ℤ 3 \mathbb{D}_{n}\times\mathbb{Z}_{3}, we abbreviate its member ( α i, u) (\alpha_{i},u) ( α ∈ { ρ, τ }) (\alpha\in\{\rho,\tau\}) as α i 0 \alpha_{i}^{0}, α i + \alpha_{i}^{+} or α i − \alpha_{i}^{-} if u = 0, 1, 2 u=0,1,2, respectively.

For a positive integer n n, we define the graph Δ n = Cay ⁡ ( 𝔻 3 ​ n, { τ 0, τ k, τ n }) \Delta_{n}=\operatorname{Cay}(\mathbb{D}_{3n},\{\tau_{0},\tau_{k},\tau_{n}\}) of order 6 ​ n 6n, where k = 3 / gcd ⁡ ( 3, n) k=3/\gcd(3,n). The graph Δ n \Delta_{n} is vertex-transitive with girth 6 6 for all n ≥ 3 n\geq 3, with signature ( 4, 5, 5) (4,5,5) if n = 3 n=3 and ( 2, 3, 3) (2,3,3) otherwise. For all n ≥ 1 n\geq 1, the graph Δ n \Delta_{n} admits an embedding onto a torus with 3 ​ n 3n hexagonal faces such that the consecutive arcs on each face correspond to the generators τ 0, τ k, τ n, τ 0, τ k, τ n \tau_{0},\tau_{k},\tau_{n},\tau_{0},\tau_{k},\tau_{n}. The graphs Δ 4 \Delta_{4} and Δ 5 \Delta_{5} are shown in Figure 19 (b) and Figure 20 (b).

For a positive integer n n, we next define the graph Σ n = Cay ( 𝔻 n × ℤ 3, { τ 1 0, τ 0 +, \Sigma_{n}=\operatorname{Cay}(\mathbb{D}_{n}\times\mathbb{Z}_{3},\{\tau_{1}^{0},\tau_{0}^{+}, τ 0 − }) \tau_{0}^{-}\}) of order 6 ​ n 6n. The graph Σ n \Sigma_{n} is vertex-transitive with girth 6 6 for all n ≥ 3 n\geq 3. The graph Σ 3 \Sigma_{3} is the Pappus graph with signature ( 4, 4, 4) (4,4,4), while for n ≥ 4 n\geq 4, Σ n \Sigma_{n} has signature ( 2, 3, 3) (2,3,3), For all n ≥ 1 n\geq 1, the graph Σ n \Sigma_{n} admits an embedding onto a torus with 3 ​ n 3n hexagonal faces such that the consecutive arcs on each face correspond to the generators τ 0 +, τ 0 +, τ 1 0, τ 0 −, τ 0 −, τ 1 0 \tau_{0}^{+},\tau_{0}^{+},\tau_{1}^{0},\tau_{0}^{-},\tau_{0}^{-},\tau_{1}^{0}. The graphs Σ 4 \Sigma_{4} and Σ 5 \Sigma_{5} are shown in Figure 19 (a) and Figure 20 (a). Note also that the graph Σ n \Sigma_{n} is isomorphic to the so-called split depleted wreath graph SDW ⁡ ( n, 3) \operatorname{SDW}(n,3) (cf. [34] and [26, Construction 11]) defined to have the vertex-set ℤ n × ℤ 3 × ℤ 2 \mathbb{Z}_{n}\times\mathbb{Z}_{3}\times\mathbb{Z}_{2} and edges of two types: { ( i, u, 0), ( i, u ± 1, 1) } \{(i,u,0),(i,u\pm 1,1)\} and { ( i, u, 1), ( i + 1, u, 0) } \{(i,u,1),(i+1,u,0)\}, for all i ∈ ℤ n i\in\mathbb{Z}_{n} and u ∈ ℤ 3 u\in\mathbb{Z}_{3}. An isomorphism between Σ n \Sigma_{n} and SDW ⁡ ( n, 3) \operatorname{SDW}(n,3) can be chosen so that it maps ( ρ i, u) ↦ ( i, u, 1) (\rho_{i},u)\mapsto(i,u,1) and ( τ i, u) ↦ ( i, u, 0) (\tau_{i},u)\mapsto(i,u,0) for every i ∈ ℤ n i\in\mathbb{Z}_{n} and u ∈ ℤ 3 u\in\mathbb{Z}_{3} (see Figure 2).

Figure 2. A section of Σ n ≅ SDW ⁡ ( n, 3) \Sigma_{n}\cong\operatorname{SDW}(n,3).

Finally, for a positive integer n n we define the graph Ψ n = Cay ⁡ ( 𝔻 n, { τ 0, τ 1, τ 3 }) \Psi_{n}=\operatorname{Cay}(\mathbb{D}_{n},\{\tau_{0},\tau_{1},\tau_{3}\}) of order 2 ​ n 2n. The graph Ψ n \Psi_{n} is vertex-transitive with girth 6 6 for all n ≥ 7 n\geq 7. The graphs Ψ 7 \Psi_{7} and Ψ 8 \Psi_{8} are the Heawood and Möbius-Kantor graphs with signatures ( 8, 8, 8) (8,8,8) and ( 6, 6, 6) (6,6,6), respectively. The graph Ψ 9 \Psi_{9} is isomorphic to Δ 3 \Delta_{3} with signature ( 4, 5, 5) (4,5,5). For n ≥ 10 n\geq 10, Ψ n \Psi_{n} has signature ( 3, 4, 5) (3,4,5). For all n ≥ 1 n\geq 1, the graph Ψ n \Psi_{n} admits an embedding onto a torus with n n hexagonal faces such that the consecutive arcs on each face correspond to the generators τ 0, τ 1, τ 3, τ 0, τ 1, τ 3 \tau_{0},\tau_{1},\tau_{3},\tau_{0},\tau_{1},\tau_{3}. The graph Ψ 10 \Psi_{10} is shown in Figure 3.

Figure 3. The graph Ψ 10 \Psi_{10} embedded on a torus. The double edges show one of the 6 6 -cycles which do not correspond to a face of the embedding.

Let us now determine the full groups of automorphisms of these graphs. We first give a lemma which will be useful in determining their automorphisms.

###### Lemma 3.

Let i, j, k, m i,j,k,m be distinct integers with 0 ≤ i, j, k < m 0\leq i,j,k<m, | j − k | ≠ m / 2 |j-k|\neq m/2 and gcd ⁡ ( i, j, k, m) = 1 \gcd(i,j,k,m)=1, and let Γ = Cay ⁡ ( 𝔻 m, { τ i, τ j, τ k }) \Gamma=\operatorname{Cay}(\mathbb{D}_{m},\{\tau_{i},\tau_{j},\tau_{k}\}). Define A h A_{h} ( h ∈ { i, j, k } h\in\{i,j,k\}) to be the set of arcs of Γ \Gamma corresponding to the generator τ h \tau_{h}. Suppose that φ \varphi is an automorphism of the graph Γ \Gamma that fixes the set A i A_{i}. Then either φ \varphi fixes the sets A j A_{j} and A k A_{k}, or swaps them.

###### Proof.

First, we note that the graph Γ \Gamma contains 6 6 -cycles such that its consecutive arcs correspond to the generators τ i, τ j, τ k, τ i, τ j, τ k \tau_{i},\tau_{j},\tau_{k},\tau_{i},\tau_{j},\tau_{k}. Let C C be such a cycle. As τ i ​ τ j ​ τ k ​ τ i ​ τ k ​ τ j = ρ 2 ​ j − 2 ​ k ≠ ρ 0 \tau_{i}\tau_{j}\tau_{k}\tau_{i}\tau_{k}\tau_{j}=\rho_{2j-2k}\neq\rho_{0}, the consecutive arcs of C φ C^{\varphi} must correspond to the same generators as those of C C – thus, all arcs of C C corresponding to τ j \tau_{j} (respectively τ k \tau_{k}) map to arcs of C φ C^{\varphi} all corresponding to τ j \tau_{j}, or all corresponding to τ k \tau_{k}. As each of these arcs also lies on another 6 6 -cycle C ′ C^{\prime} whose consecutive arcs correspond to the same generators as those of C C, it follows that φ \varphi acts in the same way on the arcs of C ′ C^{\prime}. Since the connection set generates the group 𝔻 m \mathbb{D}_{m}, the graph Γ \Gamma is connected, therefore this is true for all such 6 6 -cycles. We thus conclude that either φ \varphi fixes the sets A j A_{j} and A k A_{k}, or swaps them. ∎

We first deal with the graphs Δ n \Delta_{n} with n ≥ 3 n\geq 3. Recall that a Cayley graph Cay ⁡ ( G, S) \operatorname{Cay}(G,S) is called a graphical regular representation of the group G G if its full group of automorphisms is isomorphic to G G.

###### Proposition 4.

Let n ≥ 3 n\geq 3. The full group of automorphisms of the graph Δ n \Delta_{n} is isomorphic to the dihedral group 𝔻 3 ​ n \mathbb{D}_{3n} of order 6 ​ n 6n, i.e., Δ n \Delta_{n} is a graphical regular representation of 𝔻 3 ​ n \mathbb{D}_{3n}.

###### Proof.

As noted above, the graph Δ n = ( V, E, ∂) \Delta_{n}=(V,E,\partial) contains 6 6 -cycles such that their consecutive arcs correspond to the generators τ 0, τ k, τ n, τ 0, τ k, τ n \tau_{0},\tau_{k},\tau_{n},\tau_{0},\tau_{k},\tau_{n}, where k = 3 / gcd ⁡ ( 3, n) k=3/\gcd(3,n) – each arc lies on two such 6 6 -cycles. Furthermore, there are 6 6 -cycles in Δ n \Delta_{n} whose consecutive arcs correspond to the generators τ 0, τ n, τ 0, τ n, τ 0, τ n \tau_{0},\tau_{n},\tau_{0},\tau_{n},\tau_{0},\tau_{n}. Since gcd ⁡ ( 3 ​ n, n − k) = 1 \gcd(3n,n-k)=1, the arcs corresponding to τ k \tau_{k} and τ n \tau_{n} form a Hamiltonian cycle H H of Δ n \Delta_{n}. From the definition it follows that the group 𝔻 3 ​ n \mathbb{D}_{3n} acts regularly on the vertices of Δ n \Delta_{n} by right-multiplication, which induces the natural action of 𝔻 3 ​ n \mathbb{D}_{3n} on the edges of H H corresponding to τ k \tau_{k} (respectively τ n \tau_{n}). In particular, the automorphisms from 𝔻 3 ​ n \mathbb{D}_{3n} are precisely those which fix the sets A 0 A_{0}, A k A_{k} and A n A_{n} defined as in Lemma 3. We will show that Δ n \Delta_{n} does not admit any other automorphism.

If n ≥ 4 n\geq 4, there are no other 6 6 -cycles in Δ n \Delta_{n} other than the ones described above – the arcs corresponding to τ k \tau_{k} thus lie on two 6 6 -cycles, while the arcs corresponding to τ 0 \tau_{0} or τ n \tau_{n} lie on three 6 6 -cycles. Every automorphism of Δ n \Delta_{n} thus fixes the set A k A_{k}, and by Lemma 3, either fixes or swaps the sets A 0 A_{0} and A n A_{n}. If n n is not a multiple of 3 3, then k = 3 k=3 and the arcs corresponding to τ 0 \tau_{0} and τ k = τ 3 \tau_{k}=\tau_{3} form three 2 ​ n 2n -cycles. If, on the other hand, n n is a multiple of 3 3, then k = 1 k=1 and the arcs corresponding to τ 0 \tau_{0} and τ k = τ 1 \tau_{k}=\tau_{1} form another Hamiltonian cycle H ′ H^{\prime} of Δ n \Delta_{n}. Now, an edge e e with ∂ ( e) = { ρ i, τ i } \partial(e)=\{\rho_{i},\tau_{i}\} (i.e., corresponding to τ 0 \tau_{0}) along with the shortest path on H H between ρ i \rho_{i} and τ i \tau_{i} forms a cycle ρ i ​ τ i + n ​ ρ i + n − 1 ​ τ i + 2 ​ n − 1 ​ … ​ ρ i − n ​ τ i \rho_{i}\tau_{i+n}\rho_{i+n-1}\tau_{i+2n-1}\dots\rho_{i-n}\tau_{i} of length 2 ​ n + 2 2n+2 since ( n + 1) ⋅ n − n ⋅ 1 ≡ n 2 ≡ 0 ( mod 3 ​ n) (n+1)\cdot n-n\cdot 1\equiv n^{2}\equiv 0\pmod{3n}. However, an edge e ′ e^{\prime} with ∂ ( e ′) = { ρ i, τ i + n } \partial(e^{\prime})=\{\rho_{i},\tau_{i+n}\} (i.e., corresponding to τ n \tau_{n}) along with the shortest path on H ′ H^{\prime} between ρ i \rho_{i} and τ i + n \tau_{i+n} forms a 2 ​ n 2n -cycle ρ i ​ τ i + 1 ​ ρ i + 1 ​ τ i + 2 ​ … ​ ρ i + n − 1 ​ τ i + n \rho_{i}\tau_{i+1}\rho_{i+1}\tau_{i+2}\dots\rho_{i+n-1}\tau_{i+n}. Therefore, no automorphism of Δ n \Delta_{n} swaps the Hamiltonian cycles H H and H ′ H^{\prime}. In either case it then follows that no automorphism of Δ n \Delta_{n} swaps the sets A 0 A_{0} and A n A_{n}.

Consider now the case n = 3 n=3 – we then have k = 1 k=1. Besides the 6 6 -cycles described above, the graph Δ 3 \Delta_{3} also contains 6 6 -cycles whose consecutive arcs correspond to the generators τ 0, τ 1, τ 0, τ 1, τ 3, τ 1 \tau_{0},\tau_{1},\tau_{0},\tau_{1},\tau_{3},\tau_{1}. The arcs corresponding to τ n = τ 3 \tau_{n}=\tau_{3} thus lie on four 6 6 -cycles, while the arcs corresponding to τ 0 \tau_{0} or τ k = τ 1 \tau_{k}=\tau_{1} lie on five 6 6 -cycles. Every automorphism of Δ 3 \Delta_{3} thus fixes the set A 3 A_{3}, and by Lemma 3, either fixes or swaps the sets A 0 A_{0} and A 1 A_{1}. But since sequences of arcs corresponding to the generators τ 1, τ 0, τ 1, τ 0, τ 3, τ 0 \tau_{1},\tau_{0},\tau_{1},\tau_{0},\tau_{3},\tau_{0} do not form 6 6 -cycles, it follows that no automorphism of Δ 3 \Delta_{3} swaps the sets A 0 A_{0} and A 1 A_{1}. We thus conclude that for every n ≥ 3 n\geq 3, the full automorphism group of Δ n \Delta_{n} is isomorphic to the group 𝔻 3 ​ n \mathbb{D}_{3n}, so Δ n \Delta_{n} is its graphical regular representation. ∎

Let us now consider the graphs Σ n \Sigma_{n}. The full automorphism group of Σ 3 \Sigma_{3} has order 216 216. The following lemma deals with the case when n ≥ 4 n\geq 4.

###### Proposition 5.

Let n ≥ 4 n\geq 4. The full group of automorphisms of the graph Σ n \Sigma_{n} is isomorphic to the direct product 𝔻 n × 𝔻 3 \mathbb{D}_{n}\times\mathbb{D}_{3} of order 12 ​ n 12n.

###### Proof.

As noted above, the graph Σ n = ( V, E, ∂) \Sigma_{n}=(V,E,\partial) contains 6 6 -cycles such that their consecutive arcs correspond to the generators τ 0 +, τ 0 +, τ 1 0, τ 0 −, τ 0 −, τ 1 0 \tau_{0}^{+},\tau_{0}^{+},\tau_{1}^{0},\tau_{0}^{-},\tau_{0}^{-},\tau_{1}^{0} – each arc lies on two such 6 6 -cycles. Furthermore, there are 6 6 -cycles in Σ n \Sigma_{n} whose consecutive arcs all correspond to the generator τ 0 + \tau_{0}^{+} (or, equivalently, its inverse τ 0 − \tau_{0}^{-}). We denote the set of such 6 6 -cycles by C C. Since n ≥ 4 n\geq 4, there are no other 6 6 -cycles, so the arcs corresponding to τ 1 0 \tau_{1}^{0} lie on two 6 6 -cycles, while the arcs corresponding to τ 0 + \tau_{0}^{+} or τ 0 − \tau_{0}^{-} lie on three 6 6 -cycles. Every automorphism of Σ n \Sigma_{n} thus fixes the set C C, as well as the set E 1 0 E_{1}^{0} of edges corresponding to τ 1 0 \tau_{1}^{0}.

We may thus define a graph Λ = ( C, E 1 0, ∂ ′) \Lambda=(C,E_{1}^{0},\partial^{\prime}) with ∂ ′ ( e) = { c, c ′ } ⊂ C \partial^{\prime}(e)=\{c,c^{\prime}\}\subset C such that ∂ ( e) = { u, v } \partial(e)=\{u,v\} with u ∈ c u\in c, v ∈ c ′ v\in c^{\prime} (i.e., the endpoints of e e in Λ \Lambda are the cycles of C C containing the endpoints of e e in Σ n \Sigma_{n}). Furthermore, we define a dihedral scheme ↔ \leftrightarrow on Λ \Lambda by letting s ↔ t s\leftrightarrow t whenever the tails of s s and t t in Σ n \Sigma_{n} are adjacent. Note that the graph Λ \Lambda is a n n -cycle with tripled edges, and that Σ n \Sigma_{n} is isomorphic to Tr ( Λ, ↔) \operatorname{Tr}(\Lambda,\leftrightarrow).

We now claim that Aut ( Σ n) ≅ Aut ( Λ, ↔) ≅ 𝔻 n × 𝔻 3 \operatorname{Aut}(\Sigma_{n})\cong\operatorname{Aut}(\Lambda,\leftrightarrow)\cong\mathbb{D}_{n}\times\mathbb{D}_{3}. Indeed, the left factor in the direct product acts naturally on the vertices of Λ \Lambda and therefore on the cycles in C C, while the right factor acts naturally on the sets of parallel edges of Λ \Lambda (while preserving the dihedral scheme ↔ \leftrightarrow) and therefore the sets of edges of Σ n \Sigma_{n} connecting the same two cycles of C C; the two actions commute. This covers every automorphism of Σ n \Sigma_{n} which fixes the sets C C and E 0 1 E^{1}_{0}, and these automorphisms then form the full automorphism group of Σ n \Sigma_{n}. ∎

Finally, we consider the graphs Ψ n \Psi_{n}. The graphs Ψ 7 \Psi_{7} and Ψ 8 \Psi_{8} have full automorphism groups PGL ⁡ ( 2, 7) \operatorname{PGL}(2,7) of order 336 336 and GL ⁡ ( 2, 3) ⋊ ℤ 2 \operatorname{GL}(2,3)\rtimes\mathbb{Z}_{2} of order 96 96 (with the non-identity element of ℤ 2 \mathbb{Z}_{2} acting as a composition of the transposition and the inverse on GL ⁡ ( 2, 3) \operatorname{GL}(2,3)), respectively. The following lemma deals with the case when n ≥ 9 n\geq 9.

###### Proposition 6.

Let n ≥ 9 n\geq 9. The full group of automorphisms of the graph Ψ n \Psi_{n} is isomorphic to the dihedral group 𝔻 n \mathbb{D}_{n} of order 2 ​ n 2n, i.e., Ψ n \Psi_{n} is a graphical regular representation of 𝔻 n \mathbb{D}_{n}.

###### Proof.

Since Ψ 9 ≅ Δ 3 \Psi_{9}\cong\Delta_{3}, it follows from Proposition 4 that the full automorphism group of the graph Ψ 9 \Psi_{9} is isomorphic to 𝔻 9 \mathbb{D}_{9}. In the remainder of the proof we will thus assume n ≥ 10 n\geq 10.

Let G G be the full automorphism group of Ψ n \Psi_{n}. As noted above, the signature of the graph Ψ n \Psi_{n} with n ≥ 10 n\geq 10 is ( 3, 4, 5) (3,4,5) – since it consists of distinct integers, it follows that the stabilizer G u G_{u} of a vertex u u of Ψ n \Psi_{n} acts trivially on its neighbours, and by connectivity it follows that G u G_{u} is trivial. From the definition it follows that the group 𝔻 n \mathbb{D}_{n} acts regularly on the vertices of Ψ n \Psi_{n} by right-multiplication, so the full automorphism group G G is isomorphic to 𝔻 n \mathbb{D}_{n}. We can thus conclude that the graph Ψ n \Psi_{n} is a graphical regular representation of 𝔻 n \mathbb{D}_{n} for all n ≥ 9 n\geq 9. ∎

### 2.5. Auxiliary results

We will repeat some results from [28] that will be used in the following section.

###### Lemma 7.

( [28, Lemma 3.1]) If ( a, b, c) (a,b,c) is the signature of a cubic girth-regular graph Γ \Gamma of girth g g, then:

1. (1)

a + b + c a+b+c is even,

2. (2)

a + b ≥ c a+b\geq c, and

3. (3)

if a ≥ 1 a\geq 1 and c = a + b c=a+b, then g g is even. ∎

###### Lemma 8.

( [28, Lemma 3.2]) If the signature of a cubic girth-regular graph is ( 0, b, c) (0,b,c), then b = c = 1 b=c=1. ∎

###### Lemma 9.

( [28, Lemma 3.4]) Let Γ \Gamma be a cubic girth-regular graph of girth g g with signature ( a, b, c) (a,b,c). Let m = 2 ⌊ g / 2 ⌋ − 1 m=2^{\lfloor g/2\rfloor-1}. Then a ≥ c − m a\geq c-m and b ≤ a − c + 2 ​ m b\leq a-c+2m. ∎

###### Theorem 10.

( [28, Theorem 3.6]) If Γ \Gamma is a simple cubic girth-regular graph of girth g g with signature ( 0, 1, 1) (0,1,1), then Γ \Gamma is isomorphic to the truncation of a g g -regular graph Λ \Lambda (possibly with parallel edges) with respect to a dihedral scheme ↔ \leftrightarrow. Moreover, if Γ \Gamma is vertex-transitive, then the dihedral scheme ↔ \leftrightarrow is arc-transitive. ∎

###### Theorem 11.

( [28, Theorem 3.14]) Let Γ \Gamma be a simple connected cubic girth-regular graph of girth g g with n n vertices and signature ( 1, 1, 2) (1,1,2). Then g g is even and Γ \Gamma is the truncation of some map ℳ \mathcal{M} with face cycles of length g / 2 g/2. In particular, g / 2 g/2 divides n n. Moreover, if Γ \Gamma is vertex-transitive, then ℳ \mathcal{M} is an arc-transitive map of type { g / 2, ℓ } \{g/2,\ell\} for some ℓ > g \ell>g. ∎

###### Theorem 12.

( [28, Theorem 3.11]) Let Γ \Gamma be a connected simple cubic girth-regular graph of girth g g with n n vertices and signature ( 2, 2, 2) (2,2,2). Then g g divides 3 ​ n 3n and Γ \Gamma is the skeleton of a map of type { g, 3 } \{g,3\} embedded on a surface with Euler characteristic

 | χ = n ⁡ ( 3 g − 1 2). \chi=n\left(\frac{3}{g}-\frac{1}{2}\right). |  |

Moreover, every automorphism of Γ \Gamma extends to an automorphism of the map. In particular, if Γ \Gamma is vertex-transitive, so is the map. ∎

###### Theorem 13.

( [28, Theorems 1.2, 1.3, 1.4]) Let Γ \Gamma be a simple connected cubic girth-regular graph with signature ( a, b, c) (a,b,c). Then c ≤ 2 ⌊ g / 2 ⌋ c\leq 2^{\lfloor g/2\rfloor}, with equality implying that a = b = c a=b=c and Γ \Gamma is one of the following:

1. (a)

the complete graph K 4 K_{4} of girth g = 3 g=3,

2. (b)

the complete bipartite graph K 3, 3 K_{3,3} of girth g = 4 g=4,

3. (c)

the Petersen graph of girth g = 5 g=5,

4. (d)

the Heawood graph of girth g = 6 g=6,

5. (e)

the Tutte-Coxeter graph of girth g = 8 g=8, or

6. (f)

the Tutte 12 12 -cage of girth g = 12 g=12. ∎

## 3. Proof of Theorem 1

This section contains the proof of Theorem 1. For cubic vertex-transitive graphs of girth 6 6, Lemmas 7 and 9 and Theorems 10 and 13 imply that there are 27 27 possible signatures ( a, b, c) (a,b,c). In particular, c ≤ 8 c\leq 8 must hold. As we will see, only 9 9 of these signatures actually occur.

Let Γ \Gamma be a cubic vertex-transitive graph of girth 6 6. For an arc u ​ v uv of Γ \Gamma, let P ⁡ ( u ​ v) P(uv) be the partition of the set of vertices at distance 2 2 from u u that are not adjacent to v v into two sets according to their common neighbour with u u – i.e., P ⁡ ( u ​ v) P(uv) contains two sets with two vertices each. We also define T ⁡ ( u ​ v) T(uv) as the multiset of two multisets containing numbers which, for each vertex of P ⁡ ( u ​ v) P(uv), tell how many neighbours it has among the vertices of P ⁡ ( v ​ u) P(vu) (see Figure 4 (c) for an example). We refer to the ordered pair ( T ⁡ ( u ​ v), T ⁡ ( v ​ u)) (T(uv),T(vu)) as the type of the arc u ​ v uv. Clearly, ∑ ⋃ ⁡ T ⁡ ( u ​ v) = ∑ ⋃ ⁡ T ⁡ ( v ​ u) \sum\bigcup T(uv)=\sum\bigcup T(vu) equals the number of 6 6 -cycles the arc u ​ v uv lies on. Vertex-transitivity of Γ \Gamma implies that for every arc u ​ v uv with type ( R, S) (R,S), there is an arc u ​ w uw with inverse type ( S, R) (S,R). Since the valency of each vertex is odd, there must exist an arc with type ( R, R) (R,R) for some R R. Such an arc is said to have symmetric type. Thus, either all three arcs with tail u u have symmetric types, or one has symmetric type and the other two have mutually inverse asymmetric types.

Theorems 10, 11 and 13 already deal with signatures ( 0, 1, 1) (0,1,1), ( 1, 1, 2) (1,1,2) and ( a, b, 8) (a,b,8), respectively. We will now consider each remaining signature ( a, b, c) (a,b,c) in decreasing order of c c. In the following lemmas, we will start with vertices u 0, u 1, v 00, v 01, v 10, u_{0},u_{1},v_{00},v_{01},v_{10}, v 11, w 000, w 001, w 010, w 011, w 100, w 101, w 110, w 111 v_{11},w_{000},w_{001},w_{010},w_{011},w_{100},w_{101},w_{110},w_{111} and edges as shown in Figure 4 (a), and then add new vertices and edges to complete the graphs or arrive at a contradiction. Note that girth 6 6 implies that for each arc w h ​ i ​ j ​ w h ′ ​ i ′ ​ j ′ w_{hij}w_{h^{\prime}i^{\prime}j^{\prime}} ( h, h ′, i, i ′, j, j ′ ∈ { 0, 1 } h,h^{\prime},i,i^{\prime},j,j^{\prime}\in\{0,1\}), we must have h ≠ h ′ h\neq h^{\prime}, and for each 2 2 -path w h ​ i ​ j ​ w h ′ ​ i ′ ​ j ′ ​ w h ​ i ′′ ​ j ′′ w_{hij}w_{h^{\prime}i^{\prime}j^{\prime}}w_{hi^{\prime\prime}j^{\prime\prime}} ( h, h ′, i, i ′, i ′′, j, j ′, j ′′ ∈ { 0, 1 } h,h^{\prime},i,i^{\prime},i^{\prime\prime},j,j^{\prime},j^{\prime\prime}\in\{0,1\}), we must have i ≠ i ′′ i\neq i^{\prime\prime}. In particular, there is no 6 6 -cycle containing only vertices w h ​ i ​ j w_{hij} ( h, i, j ∈ { 0, 1 } h,i,j\in\{0,1\}).

(a) (b) (c)

Figure 4. Constructing a graph of girth 6 6. The general setting is shown in (a). (b) and (c) show the cases when the arc u 0 ​ u 1 u_{0}u_{1} lies on seven 6 6 -cycles, and six 6 6 -cycles with T ⁡ ( u 0 ​ u 1) = { { 2, 2 }, { 2, 0 } } T(u_{0}u_{1})=\{\{2,2\},\{2,0\}\}, respectively. A contradiction arises in both cases.

###### Lemma 14.

Let Γ \Gamma be a cubic graph of girth 6 6 and let G G be a group of automorphisms of Γ \Gamma acting transitively on its vertices. Let u 0 u_{0} be a vertex of Γ \Gamma. Then there is a neighbour u u of u 0 u_{0} such that there is an automorphism φ ∈ G \varphi\in G swapping u 0 u_{0} and u u. If u 1 u_{1} is such a neighbour, then, assuming the configuration of Figure 4 (a), we also have v i ​ j φ = v i ′ ​ j ′ v_{ij}^{\varphi}=v_{i^{\prime}j^{\prime}} and w h ​ i ​ j φ = w h ′ ​ i ′ ​ j ′ w_{hij}^{\varphi}=w_{h^{\prime}i^{\prime}j^{\prime}}, where h ≠ h ′ h\neq h^{\prime}, i ≠ i ′ i\neq i^{\prime}, j ≠ j ′ j\neq j^{\prime}.

###### Proof.

Suppose that Γ \Gamma has n n vertices. Then it must have 3 ​ n 3n arcs. Clearly, the set of arcs of Γ \Gamma is partitioned into at most three orbits under the action of G G. Suppose that there is an arc s 1 s_{1} with tail u 0 u_{0} such that s 1 s_{1} and s 1 − 1 s_{1}^{-1} (the inverse arc of s 1 s_{1}, see Section 2.1) lie in distinct orbits. By vertex-transitivity, there is an arc s 2 s_{2} with tail u 0 u_{0} such that s 2 s_{2} and s 2 − 1 s_{2}^{-1} lie in the same orbits as s 1 − 1 s_{1}^{-1} and s 1 s_{1}, respectively. Let u u be the head of the remaining arc s 3 s_{3} with tail u 0 u_{0}. Clearly, the arc s 3 s_{3} cannot lie in the same orbits as s 1 s_{1} or s 2 s_{2}, so it must lie in its own orbit which then also contains s 3 − 1 s_{3}^{-1}. Therefore, there is an automorphism φ \varphi swapping u 0 u_{0} and u u. If u 1 u_{1} is a vertex like u u, then, without loss of generality, φ \varphi acts on the vertices v i ​ j v_{ij} and w h ​ i ​ j w_{hij} from Figure 4 (a) as described. ∎

###### Lemma 15.

Let Γ \Gamma be a cubic girth-regular graph of girth 6 6 with signature ( a, b, c) (a,b,c). Then c ≠ 7 c\neq 7.

###### Proof.

Assuming the configuration of Figure 4 (a), suppose that the arc u 0 ​ u 1 u_{0}u_{1} lies on precisely seven 6 6 -cycles. Without loss of generality, we may assume that w 011 w_{011} and w 100 w_{100} only have one neighbour among w h ​ i ​ j w_{hij} ( h, i, j ∈ { 0, 1 }) (h,i,j\in\{0,1\}). Clearly, these vertices must induce a 7 7 -path, say w 011 ​ w 111 ​ w 001 ​ w 101 ​ w 010 ​ w 110 ​ w 000 ​ w 100 w_{011}w_{111}w_{001}w_{101}w_{010}w_{110}w_{000}w_{100}, see Figure 4 (b). The arc u 0 ​ v 00 u_{0}v_{00} thus lies on seven 6 6 -cycles, and the arc u 0 ​ v 01 u_{0}v_{01} lies on six 6 6 -cycles, so the signature of Γ \Gamma is ( 6, 7, 7) (6,7,7). This implies that the arc v 01 ​ w 010 v_{01}w_{010} should lie on seven 6 6 -cycles, however, it only lies on six 6 6 -cycles – contradiction. ∎

###### Lemma 16.

Let Γ \Gamma be a connected cubic vertex-transitive graph of girth 6 6 with signature ( a, b, c) (a,b,c), where c = 6 c=6. Then a = b = 6 a=b=6 and Γ \Gamma is the Möbius-Kantor graph, which is isomorphic to Ψ 8 \Psi_{8}.

###### Proof.

Assuming the configuration of Figure 4 (a), suppose that the arc u 0 ​ u 1 u_{0}u_{1} lies on precisely six 6 6 -cycles. First, assume that T ⁡ ( u 0 ​ u 1) = { { 2, 2 }, { 2, 0 } } T(u_{0}u_{1})=\{\{2,2\},\{2,0\}\}. Without loss of generality, we may assume that w 011 w_{011} has no neighbours among w h ​ i ​ j w_{hij} ( h, i, j ∈ { 0, 1 }) (h,i,j\in\{0,1\}). The remaining vertices must then induce a 6 6 -path, say w 111 ​ w 001 ​ w 101 w_{111}w_{001}w_{101} w 010 ​ w 110 ​ w 000 ​ w 100 w_{010}w_{110}w_{000}w_{100}, see Figure 4 (c). Thus, we have T ⁡ ( u 1 ​ u 0) = { { 2, 1 }, { 2, 1 } } T(u_{1}u_{0})=\{\{2,1\},\{2,1\}\}. The arc u 0 ​ v 00 u_{0}v_{00} has the same asymmetric type as u 0 ​ u 1 u_{0}u_{1}, contradiction.

Now, assume that T ⁡ ( u 0 ​ u 1) = { { 2, 2 }, { 1, 1 } } T(u_{0}u_{1})=\{\{2,2\},\{1,1\}\}. Without loss of generality we may assume w 000 ∼ w 100, w 110 w_{000}\sim w_{100},w_{110}, w 001 ∼ w 101, w 111 w_{001}\sim w_{101},w_{111} and w 011 ∼ w 100 w_{011}\sim w_{100}, see Figure 5 (a). The vertex w 010 w_{010} must then be adjacent to one of w 101 w_{101}, w 110 w_{110} and w 111 w_{111}, giving T ⁡ ( u 0 ​ v 00) = T ⁡ ( u 0 ​ u 1) T(u_{0}v_{00})=T(u_{0}u_{1}). The arc u 0 ​ v 01 u_{0}v_{01} then lies on precisely four girth cycles, so the types of the arcs u 0 ​ u 1 u_{0}u_{1} and u 0 ​ v 00 u_{0}v_{00} must then be both symmetric. However, in all three cases at least one of T ⁡ ( u 1 ​ u 0) T(u_{1}u_{0}) and T ⁡ ( v 00 ​ u 0) T(v_{00}u_{0}) equals { { 2, 1 }, { 2, 1 } } \{\{2,1\},\{2,1\}\}, making this case impossible.

(a) (b) (c)

Figure 5. Constructing a graph of girth 6 6 with c = 6 c=6. (a) The case T ⁡ ( u 0 ​ u 1) = { { 2, 2 }, { 1, 1 } } T(u_{0}u_{1})=\{\{2,2\},\{1,1\}\}, which leads to a contradiction. (b) The case T ⁡ ( u 0 ​ u 1) = { { 2, 1 }, { 2, 1 } } T(u_{0}u_{1})=\{\{2,1\},\{2,1\}\}. (c) The subcase of (b) with a = b = 5 a=b=5, which also leads to a contradiction.

The only remaining possibility is T ⁡ ( u 0 ​ u 1) = T ⁡ ( u 1 ​ u 0) = { { 2, 1 }, { 2, 1 } } T(u_{0}u_{1})=T(u_{1}u_{0})=\{\{2,1\},\{2,1\}\}. Without loss of generality, we may assume w 000 ∼ w 100 w_{000}\sim w_{100} and w 001 ∼ w 101, w 110 w_{001}\sim w_{101},w_{110}. Since w 111 w_{111} cannot have 2 2 neighbours among w 0 ​ i ​ j w_{0ij} ( i, j ∈ { 0, 1 } i,j\in\{0,1\}), we may further assume w 010 ∼ w 110 w_{010}\sim w_{110} and w 011 ∼ w 111 w_{011}\sim w_{111}, see Figure 5 (b). There is another arc w 01 ​ i ​ w 10 ​ j w_{01i}w_{10j} for some i, j ∈ { 0, 1 } i,j\in\{0,1\}. Note that ( i, j) = ( 0, 1) (i,j)=(0,1) is not possible as that would give a 4 4 -cycle.

The arcs u 0 ​ v 00 u_{0}v_{00} and u 0 ​ v 01 u_{0}v_{01} lie on at least five 6 6 -cycles. Suppose that u 0 ​ v 00 u_{0}v_{00} lies on precisely five 6 6 -cycles. Then u 0 ​ v 01 u_{0}v_{01} must also lie on precisely five 6 6 -cycles, and there is an automorphism of Γ \Gamma swapping u 0 u_{0} and u 1 u_{1} as in Lemma 14. Thus, we have w 011 ∼ w 100 w_{011}\sim w_{100}. Let x 0 x_{0} and x 1 x_{1} be the remaining neighbours of w 001 w_{001} and w 110 w_{110}, respectively (see Figure 5 (c)) – since u 0 ​ v 00 u_{0}v_{00} and u 0 ​ v 01 u_{0}v_{01} lie on precisely five 6 6 -cycles, they must be distinct vertices. The arcs u 0 ​ v 00 u_{0}v_{00} and u 0 ​ v 01 u_{0}v_{01} now both have asymmetric type ( { { 2, 1 }, { 1, 1 } }, { { 2, 1 }, { 2, 0 } }) (\{\{2,1\},\{1,1\}\},\{\{2,1\},\{2,0\}\}), contradiction.

Therefore, u 0 ​ v 00 u_{0}v_{00} lies on six 6 6 -cycles. Let x 0 x_{0} be the remaining neighbour of w 000 w_{000}. Then one of w 010 w_{010} and w 011 w_{011} is adjacent to x 0 x_{0}, while the other is adjacent to one of w 100 w_{100} and w 101 w_{101}. The arc u 0 ​ v 01 u_{0}v_{01} then also lies on 6 6 girth cycles, so the signature of Γ \Gamma is ( 6, 6, 6) (6,6,6). Since we haven’t made any other assumptions about the arc u 0 ​ u 1 u_{0}u_{1}, we may then assume without loss of generality that there is an automorphism of Γ \Gamma swapping u 0 u_{0} and u 1 u_{1} as in Lemma 14. We thus have w 010 ∼ x 0 w_{010}\sim x_{0}, w 011 ∼ w 100 w_{011}\sim w_{100}, and a vertex x 1 x_{1} such that w 101, w 111 ∼ x 1 w_{101},w_{111}\sim x_{1}. For the arc v 00 ​ w 001 v_{00}w_{001} to lie on 6 6 vertices, we must also have x 0 ∼ x 1 x_{0}\sim x_{1}, which completes the graph.

Figure 6 shows the labelling of vertices of Γ \Gamma with elements of 𝔻 8 \mathbb{D}_{8}, establishing that Γ \Gamma is isomorphic to Ψ 8 \Psi_{8}, and a drawing of Γ \Gamma as a generalized Petersen graph GP ⁡ ( 8, 3) \operatorname{GP}(8,3), showing that it is also isomorphic to the Möbius-Kantor graph. ∎

(a) (b)

Figure 6. The Möbius-Kantor graph of girth 6 6 and signature ( 6, 6, 6) (6,6,6), labelled as the Cayley graph Ψ 8 \Psi_{8}, (a) as the completion of Figure 5 (b), and (b) as a generalized Petersen graph GP ⁡ ( 8, 3) \operatorname{GP}(8,3).

###### Lemma 17.

Let Γ \Gamma be a connected cubic vertex-transitive graph of girth 6 6 with signature ( a, b, c) (a,b,c), where b = c = 5 b=c=5. Then a = 4 a=4 and Γ \Gamma is isomorphic to Ψ 9 \Psi_{9}.

###### Proof.

As a + b + c a+b+c is even, a a must also be even. Assuming the configuration of Figure 4 (a), suppose that the arc u 0 ​ u 1 u_{0}u_{1} lies on precisely a a 6 6 -cycles. As a ≠ b, c a\neq b,c, there exists an automorphism of Γ \Gamma swapping u 0 u_{0} and u 1 u_{1} as in Lemma 14. By Lemma 8, we must have a ≥ 2 a\geq 2.

Suppose a = 2 a=2. Without loss of generality, we may assume that the 2 2 -paths u 1 ​ u 0 ​ v 00 u_{1}u_{0}v_{00}, u 1 ​ u 0 ​ v 01 u_{1}u_{0}v_{01} and v 00 ​ u 0 ​ v 01 v_{00}u_{0}v_{01} lie on one, one and four 6 6 -cycles, respectively. By symmetry, we may assume, say, w 000 ∼ w 111 w_{000}\sim w_{111} and w 011 ∼ w 100 w_{011}\sim w_{100}, see Figure 7 (a). For v 00 ​ u 0 ​ v 01 v_{00}u_{0}v_{01} to lie on four 6 6 -cycles, the vertices w 00 ​ i w_{00i} and w 01 ​ j w_{01j} should have a common neighbour for all choices of i, j ∈ { 0, 1 } i,j\in\{0,1\}. This is, however, not attainable.

(a) (b)

Figure 7. Constructing a graph of girth 6 6 with b = c = 5 b=c=5. (a) The case a = 2 a=2, which cannot be completed. (b) The case a = 4 a=4, which can be completed to Ψ 9 \Psi_{9}.

Therefore, we have a = 4 a=4. We may thus assume that the 2 2 -paths u 1 ​ u 0 ​ v 00 u_{1}u_{0}v_{00}, u 1 ​ u 0 ​ v 01 u_{1}u_{0}v_{01} and v 00 ​ u 0 ​ v 01 v_{00}u_{0}v_{01} lie on two, two and three 6 6 -cycles, respectively. Three pairs of vertices w 0 ​ i ​ j w_{0ij} and w 0 ​ h ​ k w_{0hk} for some i, j, h, k ∈ { 0, 1 } i,j,h,k\in\{0,1\} with i ≠ h i\neq h then have a common neighbour – this covers six of the remaining arcs with tail among w 0 ​ i ​ j w_{0ij} ( i, j ∈ { 0, 1 } i,j\in\{0,1\}). As there are eight such remaining arcs, four of which have the head among w 1 ​ h ​ k w_{1hk} ( h, k ∈ { 0, 1 } h,k\in\{0,1\}), it follows that one or two of the common neighbours are vertices w 1 ​ h ​ k w_{1hk} for some h, k ∈ { 0, 1 } h,k\in\{0,1\}. Without loss of generality and by symmetry, we may then assume that there is a 3 3 -path w 000 ​ w 100 ​ w 011 ​ w 111 w_{000}w_{100}w_{011}w_{111}. Now, w 011 w_{011} cannot have a common neighbour with w 001 w_{001} (as the common neighbour should be w 111 w_{111}, and symmetry would imply that the 2 2 -path u 1 ​ u 0 ​ v 00 u_{1}u_{0}v_{00} lied on three 6 6 -cycles), so w 010 w_{010} has common neighbours with both w 000 w_{000} and w 001 w_{001}, none of which can be among w 1 ​ h ​ k w_{1hk} ( h, k ∈ { 0, 1 } h,k\in\{0,1\}). We may thus add new vertices x i ​ j x_{ij} ( i, j ∈ { 0, 1 } i,j\in\{0,1\}) with w i ​ i ​ i ∼ x i ​ i w_{iii}\sim x_{ii}, w i ​ i ​ j ∼ x i ​ j w_{iij}\sim x_{ij} and w i ​ j ​ i ∼ x i ​ i, x i ​ j w_{iji}\sim x_{ii},x_{ij} for both choices of { i, j } = { 0, 1 } \{i,j\}=\{0,1\}. We also have w 001 ∼ w 110 w_{001}\sim w_{110}, see Figure 7 (b).

The arc u 0 ​ u 1 u_{0}u_{1} has symmetric type with T ⁡ ( u 0 ​ u 1) = { { 2, 0 }, { 1, 1 } } T(u_{0}u_{1})=\{\{2,0\},\{1,1\}\}. Consider the arc v 00 ​ w 000 v_{00}w_{000}. We have P ⁡ ( v 00 ​ w 000) = { { u 1, v 01 }, { w 101, x 01 } } P(v_{00}w_{000})=\{\{u_{1},v_{01}\},\{w_{101},x_{01}\}\} and P ⁡ ( w 000 ​ v 00) = { { v 10, w 011 }, { w 010, y } } P(w_{000}v_{00})=\{\{v_{10},w_{011}\},\{w_{010},y\}\}, where y y is the remaining neighbour of x 00 x_{00}. The vertex v 01 v_{01} is adjacent to w 010 w_{010} and w 011 w_{011}, while u 1 u_{1} is adjacent to v 10 v_{10}, meaning that T ⁡ ( v 00 ​ w 000) ≠ T ⁡ ( u 0 ​ u 1) T(v_{00}w_{000})\neq T(u_{0}u_{1}). The arc v 00 ​ w 000 v_{00}w_{000} thus lies on five 6 6 -cycles. As u 0 ​ v 00 u_{0}v_{00} also lies on five 6 6 -cycles, v 00 ​ w 001 v_{00}w_{001} must lie on precisely four 6 6 -cycles. We have P ⁡ ( v 00 ​ w 001) = { { u 1, v 01 }, { w 100, x 00 } } P(v_{00}w_{001})=\{\{u_{1},v_{01}\},\{w_{100},x_{00}\}\} and P ⁡ ( w 001 ​ v 00) = { { v 11, x 10 }, { w 010, z } } P(w_{001}v_{00})=\{\{v_{11},x_{10}\},\{w_{010},z\}\}, where z z is the remaining neighbour of x 01 x_{01}. As w 100 w_{100} is not adjacent to any vertex of P ⁡ ( w 001 ​ v 00) P(w_{001}v_{00}) and x 00 ∼ w 010 x_{00}\sim w_{010}, we must also have x 00 ∼ x 10 x_{00}\sim x_{10}, and, by symmetry, x 01 ∼ x 11 x_{01}\sim x_{11}, thus completing the graph. Figure 8 (a) shows the labelling of vertices of Γ \Gamma with elements of 𝔻 9 \mathbb{D}_{9}, establishing that Γ \Gamma is isomorphic to Ψ 9 \Psi_{9}. ∎

(a) (b)

Figure 8. Constructing a graph of girth 6 6 with c = 5 c=5. (a) The graph Ψ 9 \Psi_{9} with signature ( 4, 5, 5) (4,5,5). (b) The case a = 2 a=2, b = 3 b=3, which cannot be completed.

###### Lemma 18.

Let Γ \Gamma be a connected cubic vertex-transitive graph of girth 6 6 with signature ( a, b, c) (a,b,c), where b < c = 5 b<c=5. Then a = 3 a=3, b = 4 b=4 and Γ \Gamma is isomorphic to Ψ n \Psi_{n} for some n ≥ 10 n\geq 10.

###### Proof.

As a + b + c a+b+c is even, a + b a+b must be odd. Assuming the configuration of Figure 4 (a), suppose that the arc u 0 ​ u 1 u_{0}u_{1} lies on precisely a a 6 6 -cycles. As a ≠ b, c a\neq b,c, there exists an automorphism φ \varphi of Γ \Gamma swapping u 0 u_{0} and u 1 u_{1} as in Lemma 14. By Lemma 8, we must have a ≥ 1 a\geq 1.

Suppose a = 1 a=1. By triangle inequality, we then have b = 4 b=4. Without loss of generality, we may assume that the 2 2 -paths u 1 ​ u 0 ​ v 00 u_{1}u_{0}v_{00}, u 1 ​ u 0 ​ v 01 u_{1}u_{0}v_{01} and v 00 ​ u 0 ​ v 01 v_{00}u_{0}v_{01} lie on zero, one and four 6 6 -cycles, respectively. Then, each remaining arc with tail among w 0 ​ i ​ j w_{0ij} ( i, j ∈ { 0, 1 } i,j\in\{0,1\}) must have a common neighbour with another such vertex as its head. However, the single edge completing a 6 6 -cycle on u 1 ​ u 0 ​ v 01 u_{1}u_{0}v_{01} does not reach such a common neighbour, contradiction.

Now suppose a = 2 a=2. We must then have b = 3 b=3. Without loss of generality, we may assume that the 2 2 -paths u 1 ​ u 0 ​ v 00 u_{1}u_{0}v_{00}, u 1 ​ u 0 ​ v 01 u_{1}u_{0}v_{01} and v 00 ​ u 0 ​ v 01 v_{00}u_{0}v_{01} lie on zero, two and three 6 6 -cycles, respectively. By symmetry, we then have w 010 ∼ w 101 w_{010}\sim w_{101} and w 011 ∼ w 100 w_{011}\sim w_{100}, see Figure 8 (b). For v 00 ​ u 0 ​ v 01 v_{00}u_{0}v_{01} to lie on three 6 6 -cycles, the vertices w 00 ​ i w_{00i} and w 01 ​ j w_{01j} should have a common neighbour for three choices of i, j ∈ { 0, 1 } i,j\in\{0,1\}. This is, however, not attainable.

The only remaining option is a = 3 a=3, b = 4 b=4. Without loss of generality, we may assume that the 2 2 -paths u 1 ​ u 0 ​ v 00 u_{1}u_{0}v_{00}, u 1 ​ u 0 ​ v 01 u_{1}u_{0}v_{01} and v 00 ​ u 0 ​ v 01 v_{00}u_{0}v_{01} lie on one, two and three 6 6 -cycles, respectively. Now, the vertices w 01 ​ h w_{01h} ( h ∈ { 0, 1 } h\in\{0,1\}) have two neighbours among w 1 ​ i ​ j w_{1ij} ( i, j ∈ { 0, 1 } i,j\in\{0,1\}), but at most one with i = 1 i=1. Without loss of generality we may then assume w 011 ∼ w 100 w_{011}\sim w_{100}, and also that w 000 w_{000} has a neighbour among w 1 ​ i ​ j w_{1ij} ( i, j ∈ { 0, 1 } i,j\in\{0,1\}). By symmetry, w 111 w_{111} then has a neighbour among w 0 ​ i ​ j w_{0ij} ( i, j ∈ { 0, 1 } i,j\in\{0,1\}). Since only one of v 10 v_{10} and v 11 v_{11} has a common neighbour with only one of w 000 w_{000} and w 001 w_{001}, and the arc u 0 ​ v 00 u_{0}v_{00} lies on four 6 6 -cycles, the latter must have symmetric type with T ⁡ ( u 0 ​ v 00) = { { 2, 1 }, { 1, 0 } } T(u_{0}v_{00})=\{\{2,1\},\{1,0\}\}.

In the remainder of this proof, we will gradually build an isomorphism between Γ \Gamma and Ψ n \Psi_{n} for some n ≥ 10 n\geq 10. We will thus assume that the graph Γ \Gamma has 2 ​ n 2n vertices which the automorphism maps to the elements of the group 𝔻 n \mathbb{D}_{n}. We start by relabelling the vertices u 0 u_{0}, u 1 u_{1}, v 00 v_{00}, v 01 v_{01}, v 10 v_{10}, v 11 v_{11}, w 000 w_{000}, w 001 w_{001}, w 010 w_{010}, w 011 w_{011}, w 100 w_{100}, w 101 w_{101}, w 110 w_{110} and w 111 w_{111} as ρ 0 \rho_{0}, τ 3 \tau_{3}, τ 0 \tau_{0}, τ 1 \tau_{1}, ρ 2 \rho_{2}, ρ 3 \rho_{3}, ρ − 1 \rho_{-1}, ρ − 3 \rho_{-3}, ρ − 2 \rho_{-2}, ρ 1 \rho_{1}, τ 2 \tau_{2}, τ 5 \tau_{5}, τ 6 \tau_{6} and τ 4 \tau_{4}, respectively. Note that each arc determined so far is of form ρ i ​ τ j \rho_{i}\tau_{j} or τ j ​ ρ i \tau_{j}\rho_{i}, where j − i ∈ { 0, 1, 3 } j-i\in\{0,1,3\}. Also, the automorphism φ \varphi acts as ρ i φ = τ 3 − i \rho_{i}^{\varphi}=\tau_{3-i} and τ i φ = ρ 3 − i \tau_{i}^{\varphi}=\rho_{3-i} on the vertices determined so far. These properties will continue to hold as we will be determining more arcs and vertices.

By the above argument, we may add vertices τ − 1 \tau_{-1}, τ − 3 \tau_{-3}, τ − 2 \tau_{-2}, ρ 5 \rho_{5}, ρ 6 \rho_{6} and ρ 4 \rho_{4} such that ρ − 1 ∼ τ − 1 \rho_{-1}\sim\tau_{-1}, τ − 2 ∼ ρ − 3 ∼ τ − 3 \tau_{-2}\sim\rho_{-3}\sim\tau_{-3}, ρ 5 ∼ τ 6 ∼ ρ 6 \rho_{5}\sim\tau_{6}\sim\rho_{6} and τ 4 ∼ ρ 4 \tau_{4}\sim\rho_{4}. Since none of τ i \tau_{i} ( i ∈ { − 1, − 2, − 3 } i\in\{-1,-2,-3\}) can have two neighbours among ρ j \rho_{j} ( j ∈ { − 2, 1, 2, 3 } j\in\{-2,1,2,3\}), it follows that the remaining neighbour of ρ − 1 \rho_{-1} is either τ 2 \tau_{2} or τ 5 \tau_{5}. However, ρ − 1 ∼ τ 5 \rho_{-1}\sim\tau_{5} implies ρ − 2 ∼ τ 4 \rho_{-2}\sim\tau_{4} by symmetry (see Figure 9 (a)), and the vertices ρ j \rho_{j} ( j ∈ { − 2, 1 } j\in\{-2,1\}) cannot have three neighbours among τ i \tau_{i} ( i ∈ { − 1, − 2, − 3, 5 } i\in\{-1,-2,-3,5\}), contradiction.

(a) (b)

Figure 9. Constructing a graph of girth 6 6 with signature ( 3, 4, 5) (3,4,5), with two choices of the remaining neighbour of ρ − 1 \rho_{-1}. In (a), it is assumed that ρ − 1 ∼ τ 5 \rho_{-1}\sim\tau_{5}, which leads to a contradiction. In (b), it is assumed that ρ − 1 ∼ τ 2 \rho_{-1}\sim\tau_{2}. The dashed, thick and double edges lie on three, four and five 6 6 -cycles, respectively.

Therefore, we have ρ − 1 ∼ τ 2 \rho_{-1}\sim\tau_{2}, and by symmetry also ρ 1 ∼ τ 4 \rho_{1}\sim\tau_{4}. Without loss of generality, we now have τ − 1 ∼ ρ − 2 ∼ τ − 2 \tau_{-1}\sim\rho_{-2}\sim\tau_{-2}, and by symmetry also ρ 4 ∼ τ 5 ∼ ρ 5 \rho_{4}\sim\tau_{5}\sim\rho_{5}, see Figure 9 (b). Examining the arcs ρ 0 ​ τ 3 \rho_{0}\tau_{3}, ρ 0 ​ τ 0 \rho_{0}\tau_{0} and ρ 0 ​ τ 1 \rho_{0}\tau_{1}, it follows that an arc s s lying on three, four or five 6 6 -cycles has T ⁡ ( s) T(s) equal to { { 2, 0 }, { 1, 0 } } \{\{2,0\},\{1,0\}\}, { { 2, 1 }, { 1, 0 } } \{\{2,1\},\{1,0\}\} and { { 2, 1 }, { 1, 1 } } \{\{2,1\},\{1,1\}\}, respectively. As τ 0 ​ ρ 0 \tau_{0}\rho_{0} lies on four 6 6 -cycles and both τ 1 \tau_{1} and τ 3 \tau_{3} have a common neighbour with τ 2 \tau_{2}, it follows that τ 0 ​ ρ − 1 \tau_{0}\rho_{-1} lies on five 6 6 -cycles. The edge τ 0 ​ ρ − 3 \tau_{0}\rho_{-3} then lies on three 6 6 -cycles; by symmetry, ρ 3 ​ τ 4 \rho_{3}\tau_{4} and ρ 3 ​ τ 6 \rho_{3}\tau_{6} must lie on five and three 6 6 -cycles, respectively. As τ 1 ​ ρ 0 \tau_{1}\rho_{0} lies on five 6 6 -cycles and both τ 0 \tau_{0} and τ 3 \tau_{3} have a common neighbour with τ 2 \tau_{2}, it follows that τ 1 ​ ρ 1 \tau_{1}\rho_{1} lies on four 6 6 -cycles. The edge τ 1 ​ ρ − 2 \tau_{1}\rho_{-2} then lies on three 6 6 -cycles; by symmetry, ρ 2 ​ τ 2 \rho_{2}\tau_{2} and ρ 2 ​ τ 5 \rho_{2}\tau_{5} must lie on four and three 6 6 -cycles, respectively. It follows that ρ − 1 ​ τ 2 \rho_{-1}\tau_{2} and ρ 1 ​ τ 4 \rho_{1}\tau_{4} lie on three 6 6 -cycles; furthermore, ρ 1 ​ τ 2 \rho_{1}\tau_{2} must lie on five 6 6 -cycles, while ρ − 1 ​ τ − 1 \rho_{-1}\tau_{-1} and τ 4 ​ ρ 4 \tau_{4}\rho_{4} lie on four 6 6 -cycles each. Continuing the examination, we obtain that the paths τ − 1 ​ ρ − 2 ​ τ − 2 ​ ρ − 3 ​ τ − 3 \tau_{-1}\rho_{-2}\tau_{-2}\rho_{-3}\tau_{-3} and ρ 4 ​ τ 5 ​ ρ 5 ​ τ 6 ​ ρ 6 \rho_{4}\tau_{5}\rho_{5}\tau_{6}\rho_{6} both consist of arcs alternatingly lying on five and four 6 6 -cycles each.

Now we have arrived at a point where we have determined 4 ​ t + 8 4t+8 vertices of the graph for some t ≥ 3 t\geq 3, of which τ − t \tau_{-t} and ρ 3 + t \rho_{3+t} are missing two arcs lying on three and five 6 6 -cycles, τ 1 − t \tau_{1-t}, τ 2 − t \tau_{2-t}, ρ 1 + t \rho_{1+t} and ρ 2 + t \rho_{2+t} are missing an arc lying on three 6 6 -cycles, and the vertices ρ i \rho_{i} and τ 3 + i \tau_{3+i} ( − t ≤ i ≤ t -t\leq i\leq t) have their neighbourhoods completely determined, and the arcs ρ i ​ τ j \rho_{i}\tau_{j} and τ j ​ ρ i \tau_{j}\rho_{i} determined so far lie on three, four or five 6 6 -cycles precisely when j − i j-i equals 3 3, 0 0 and 1 1, respectively.

For the arc τ 3 − t ​ ρ 2 − t \tau_{3-t}\rho_{2-t} to have the desired type { { 2, 1 }, { 1, 1 } } \{\{2,1\},\{1,1\}\}, the vertices τ − t \tau_{-t} and τ 2 − t \tau_{2-t} must have a common neighbour. By symmetry, the vertices ρ 3 + t \rho_{3+t} and ρ 1 + t \rho_{1+t} must also have a common neighbour. Of the vertices determined so far, only ρ 3 + t \rho_{3+t} is a candidate for the common neighbour of τ − t \tau_{-t} and τ 2 − t \tau_{2-t}. Suppose that this is the case – by symmetry, we must also have τ − t ∼ ρ 1 + t \tau_{-t}\sim\rho_{1+t}. As the arc τ − t ​ ρ 3 + t \tau_{-t}\rho_{3+t} must lie on five 6 6 -cycles and each of the vertices τ 3 − t \tau_{3-t}, τ 1 + t \tau_{1+t} and τ 2 + t \tau_{2+t} has a common neighbour with precisely one of τ 2 − t \tau_{2-t} and τ 3 + t \tau_{3+t}, it follows that τ 1 − t ∼ ρ 2 + t \tau_{1-t}\sim\rho_{2+t}, which completes the graph, see for example Figure 10 (a). If the indices are taken modulo n = 2 ​ t + 4 n=2t+4, it can be seen that the graph Γ \Gamma is isomorphic to Ψ n \Psi_{n}.

(a) (b)

Figure 10. Constructing a graph of girth 6 6 with signature ( 3, 4, 5) (3,4,5), with two choices of the common neighbour of τ − 1 \tau_{-1} and τ − 3 \tau_{-3}. In (a), it is assumed that the common neighbour is ρ 6 \rho_{6}, which then gives the graph Ψ 10 \Psi_{10}. In (b), it is assumed that the common neighbour is a new vertex ρ − 4 \rho_{-4}, which is adjacent to another new vertex τ − 4 \tau_{-4}, thus giving a situation similar to Figure 9 (b). The dashed, thick and double edges lie on three, four and five 6 6 -cycles, respectively.

Now assume the contrary, i.e., that the common neighbour of τ 2 − t \tau_{2-t} and τ − t \tau_{-t} is not ρ 3 + t \rho_{3+t}. Then it must be a new vertex, which we name ρ − 1 − t \rho_{-1-t}. By symmetry, the common neighbour of ρ 1 + t \rho_{1+t} and ρ 3 + t \rho_{3+t} must be another new vertex – call it τ 4 + t \tau_{4+t}. The arcs τ 2 − t ​ ρ − 1 − t \tau_{2-t}\rho_{-1-t} and ρ 1 + t ​ τ 4 + t \rho_{1+t}\tau_{4+t} must lie on three 6 6 -cycles each, and the arcs τ − t ​ ρ − 1 − t \tau_{-t}\rho_{-1-t} and ρ 3 + t ​ τ 4 + t \rho_{3+t}\tau_{4+t} must then lie on five 6 6 -cycles each. Therefore, the remaining arcs with ρ − 1 − t \rho_{-1-t} and τ 4 + t \tau_{4+t} as tails must lie on four 6 6 -cycles each. If the remaining neighbours of ρ − 1 − t \rho_{-1-t} and τ 4 + t \tau_{4+t} are new vertices τ − 1 − t \tau_{-1-t} and ρ 4 + t \rho_{4+t} (see for example Figure 10 (b)), then we are back at the previous case.

If, on the other hand, ρ − 1 − t \rho_{-1-t} and τ 4 + t \tau_{4+t} are adjacent to known vertices, we must have ρ − 1 − t ∼ τ 4 + t \rho_{-1-t}\sim\tau_{4+t}, since all other vertices missing an arc already lie on an arc lying on four 6 6 -cycles. As the arc τ 2 − t ​ ρ − 1 − t \tau_{2-t}\rho_{-1-t} lies on precisely three 6 6 -cycles and the vertex ρ 1 + t \rho_{1+t} is not adjacent to any of τ i − t \tau_{i-t} ( i ∈ { 1, 3, 4, 5 } i\in\{1,3,4,5\}), we must have ρ 3 + t ∼ τ 1 − t \rho_{3+t}\sim\tau_{1-t}, and by symmetry also τ − t ∼ ρ 2 + t \tau_{-t}\sim\rho_{2+t}, again completing the graph (see for example Figure 11 (a)). If the indices are taken modulo n = 2 ​ t + 5 n=2t+5, it can be seen that the graph Γ \Gamma is isomorphic to Ψ n \Psi_{n}. ∎

(a) (b)

Figure 11. (a) Completing Figure 10 (b) by identifying ρ − 4 = ρ 7 \rho_{-4}=\rho_{7} and τ − 4 = τ 7 \tau_{-4}=\tau_{7} to obtain Ψ 11 \Psi_{11}. The dashed, thick and double edges lie on three, four and five 6 6 -cycles, respectively. (b) Constructing a graph of girth 6 6 with signature ( 2, 4, 4) (2,4,4), which leads to a contradiction.

###### Lemma 19.

Let Γ \Gamma be a connected cubic vertex-transitive graph of girth 6 6 with signature ( a, b, c) (a,b,c), where c = 4 c=4. Then a = b = 4 a=b=4 and either Γ \Gamma is the Pappus graph, which is isomorphic to Σ 3 \Sigma_{3}, or Γ \Gamma is the Desargues graph.

###### Proof.

First assume that a < b = 4 a<b=4. By Lemma 8, we must then have a = 2 a=2. Assuming the configuration of Figure 4 (a), suppose that the arc u 0 ​ u 1 u_{0}u_{1} lies on precisely two 6 6 -cycles. As a ≠ b, c a\neq b,c, there exists an automorphism of Γ \Gamma swapping u 0 u_{0} and u 1 u_{1} as in Lemma 14. The 2 2 -path v 00 ​ u 0 ​ v 01 v_{00}u_{0}v_{01} then lies on three 6 6 -cycles, so the vertices w 00 ​ i w_{00i} and w 01 ​ j w_{01j} have a common neighbour for three choices of i, j ∈ { 0, 1 } i,j\in\{0,1\}. Symmetry implies that none of these common neighbours is a vertex w 1 ​ h ​ ℓ w_{1h\ell} ( h, ℓ ∈ { 0, 1 } h,\ell\in\{0,1\}). Instead we may assume without loss of generality that w 000 ∼ w 111 w_{000}\sim w_{111} and w 011 ∼ w 100 w_{011}\sim w_{100}. The vertices w 000 w_{000} and w 011 w_{011} cannot have a common neighbour, as that would imply that there are two common neighbours of w 001 w_{001} and w 010 w_{010}, giving us a quadrangle. By symmetry, w 100 w_{100} and w 111 w_{111} also have no common neighbour. Therefore, we have new vertices x 00 x_{00}, y 0 y_{0}, x 01 x_{01}, x 10 x_{10}, y 1 y_{1} and x 11 x_{11} such that w 000 ​ x 00 ​ w 010 ​ y 0 ​ w 001 ​ x 01 ​ w 011 w_{000}x_{00}w_{010}y_{0}w_{001}x_{01}w_{011} and w 111 ​ x 11 ​ w 101 ​ y 1 ​ w 110 ​ x 10 ​ w 100 w_{111}x_{11}w_{101}y_{1}w_{110}x_{10}w_{100} are 6 6 -paths in Γ \Gamma, see Figure 11 (b). However, the arcs u 0 ​ v 00 u_{0}v_{00} and u 0 ​ v 01 u_{0}v_{01} now both have the same asymmetric type ( { { 2, 1 }, { 1, 0 } }, { { 1, 1 }, { 1, 1 } }) (\{\{2,1\},\{1,0\}\},\{\{1,1\},\{1,1\}\}), contradiction.

Therefore, we have either b < 4 b<4 or a = b = 4 a=b=4. In either case, there exists an arc u 0 ​ u 1 u_{0}u_{1} lying on four 6 6 -cycles, where we again assume the configuration of Figure 4 (a), and an automorphism φ \varphi of Γ \Gamma swapping u 0 u_{0} and u 1 u_{1} as in Lemma 14. Clearly, u 0 ​ u 1 u_{0}u_{1} must have symmetric type. It cannot have type T ⁡ ( u 0 ​ u 1) = { { 2, 2 }, { 0, 0 } } T(u_{0}u_{1})=\{\{2,2\},\{0,0\}\} or T ⁡ ( u 0 ​ u 1) = { { 2, 0 }, { 2, 0 } } T(u_{0}u_{1})=\{\{2,0\},\{2,0\}\}, as this would imply the existence of a quadrangle. Suppose that T ⁡ ( u 0 ​ u 1) = { { 2, 1 }, { 1, 0 } } T(u_{0}u_{1})=\{\{2,1\},\{1,0\}\}. Without loss of generality, we may then assume w 000 ∼ w 100 w_{000}\sim w_{100}, w 011 ∼ w 111 w_{011}\sim w_{111} (see Figure 12 (a)), and w 010 ∼ w 10 ​ i w_{010}\sim w_{10i}, w 011 ∼ w 10 ​ j w_{011}\sim w_{10j} for some choice of { i, j } = { 0, 1 } \{i,j\}=\{0,1\}. Now, v 10 v_{10} has precisely one neighbour among the vertices of P ⁡ ( v 00 ​ u 0) P(v_{00}u_{0}), v 11 v_{11} has none, and w 010 w_{010} and w 011 w_{011} together have one or two. As the arc u 0 ​ v 01 u_{0}v_{01} lies on four 6 6 -cycles, it follows that u 0 ​ v 00 u_{0}v_{00} must then lie on precisely two 6 6 -cycles. This is however not possible by the previous argument.

(a) (b)

Figure 12. Constructing a graph of girth 6 6 with c = 4 c=4 with two choices for T ⁡ ( u 0 ​ u 1) T(u_{0}u_{1}). In (a), it is assumed that T ⁡ ( u 0 ​ u 1) = { { 2, 1 }, { 1, 0 } } T(u_{0}u_{1})=\{\{2,1\},\{1,0\}\}, while in (b), it is assumed that T ⁡ ( u 0 ​ u 1) = { { 2, 0 }, { 1, 1 } } T(u_{0}u_{1})=\{\{2,0\},\{1,1\}\}. Both assumptions lead to a contradiction.

Suppose now that T ⁡ ( u 0 ​ u 1) = { { 2, 0 }, { 1, 1 } } T(u_{0}u_{1})=\{\{2,0\},\{1,1\}\}. Without loss of generality we may now assume w 000 ∼ w 100 ∼ w 011 ∼ w 111 w_{000}\sim w_{100}\sim w_{011}\sim w_{111} and w 001 ∼ w 110 w_{001}\sim w_{110}, see Figure 12 (b). Now, v 10 v_{10}, v 11 v_{11} and w 011 w_{011} each have one neighbour among the vertices of P ⁡ ( v 00 ​ u 0) P(v_{00}u_{0}), and w 010 w_{010} can have at most one. As w 100 w_{100} is adjacent to both v 10 v_{10} and w 011 w_{011}, it follows that the arc u 0 ​ v 00 u_{0}v_{00} has asymmetric type with T ⁡ ( u 0 ​ v 00) = T ⁡ ( v 01 ​ u 0) = { { 1, 1 }, { 1, r } } T(u_{0}v_{00})=T(v_{01}u_{0})=\{\{1,1\},\{1,r\}\} for some r ∈ { 0, 1 } r\in\{0,1\}. However, w 100 w_{100} is adjacent to v 10 v_{10} and w 000 w_{000}, contradicting such a type for the arc v 01 ​ u 0 v_{01}u_{0}.

We must then conclude that T ⁡ ( u 0 ​ u 1) = { { 1, 1 }, { 1, 1 } } T(u_{0}u_{1})=\{\{1,1\},\{1,1\}\}. Without loss of generality, we may assume w 000 ∼ w 111 w_{000}\sim w_{111} and w 011 ∼ w 100 w_{011}\sim w_{100}. The remaining two 6 6 -cycles on u 0 ​ u 1 u_{0}u_{1} can now be completed in two ways. First assume w 001 ∼ w 110 w_{001}\sim w_{110} and w 010 ∼ w 101 w_{010}\sim w_{101}, see Figure 13 (a). As no vertex can be adjacent to three of the vertices w 0 ​ i ​ j w_{0ij} ( i, j ∈ { 0, 1 } i,j\in\{0,1\}), it follows that the arcs u 0 ​ v 00 u_{0}v_{00} and u 0 ​ v 01 u_{0}v_{01} have the same asymmetric type ( { { 2, 0 }, { x, y } }, { { 1, r }, { 1, s } }) (\{\{2,0\},\{x,y\}\},\{\{1,r\},\{1,s\}\}) for some r, s ∈ { 0, 1 } r,s\in\{0,1\}, contradiction.

(a) (b)

Figure 13. Constructing a graph of girth 6 6 with c = 4 c=4 and T ⁡ ( u 0 ​ u 1) = { { 1, 1 }, { 1, 1 } } T(u_{0}u_{1})=\{\{1,1\},\{1,1\}\}, with two possibilities for completing the 6 6 -cycles on u 0 ​ u 1 u_{0}u_{1}. In (a), w 001 ∼ w 110 w_{001}\sim w_{110} and w 010 ∼ w 101 w_{010}\sim w_{101} is assumed, which leads to a contradiction. In (b), w 001 ∼ w 101 w_{001}\sim w_{101} and w 010 ∼ w 110 w_{010}\sim w_{110} is assumed.

Therefore, we have w 001 ∼ w 101 w_{001}\sim w_{101} and w 010 ∼ w 110 w_{010}\sim w_{110}. Now we have T ⁡ ( u 0 ​ v 00) = T ⁡ ( u 0 ​ v 01) = { { 1, 1 }, { r, s } } T(u_{0}v_{00})=T(u_{0}v_{01})=\{\{1,1\},\{r,s\}\} and T ⁡ ( v 00 ​ u 0) = T ⁡ ( v 01 ​ u 0) = { { 1, r }, { 1, s } } T(v_{00}u_{0})=T(v_{01}u_{0})=\{\{1,r\},\{1,s\}\} for some r, s ∈ { 0, 1 } r,s\in\{0,1\}. The arcs u 0 ​ v 00 u_{0}v_{00} and u 0 ​ v 01 u_{0}v_{01} therefore have symmetric types, so we must have r = 1 r=1. Thus, the arcs u 0 ​ v 00 u_{0}v_{00} and u 0 ​ v 01 u_{0}v_{01}, and by symmetry also u 1 ​ v 10 u_{1}v_{10} and u 1 ​ v 11 u_{1}v_{11}, all lie on either three or four 6 6 -cycles, i.e., a = b ∈ { 3, 4 } a=b\in\{3,4\}. In particular, if a = b = 3 a=b=3, then the 2 2 -paths v 00 ​ u 0 ​ v 01 v_{00}u_{0}v_{01} and v 11 ​ u 1 ​ v 10 v_{11}u_{1}v_{10} lie on precisely one 6 6 -cycle each. Let x 00 x_{00} and x 01 x_{01} be the remaining negibours of w 000 w_{000} and w 001 w_{001}, respectively. Without loss of generality, we may then assume that x 00 x_{00} is adjacent to a vertex w 01 ​ i w_{01i} for some i ∈ { 0, 1 } i\in\{0,1\}. By symmetry, w 111 w_{111} must also have a common neighbour with a vertex w 10 ​ j w_{10j} for some j ∈ { 0, 1 } j\in\{0,1\}. Since neither x 00 x_{00} nor x 01 x_{01} can be adjacent with w 111 w_{111} (as that would give a triangle or a pentagon, respectively), the common neighbour must be a new vertex x 11 x_{11}, see Figure 13 (b).

Let us first assume w 010 ∼ x 00 w_{010}\sim x_{00}. By symmetry, we then also have w 101 ∼ x 11 w_{101}\sim x_{11}. Depending on whether the arc v 00 ​ w 001 v_{00}w_{001} lies on three or four 6 6 -cycles, x 01 x_{01} must have a common neighbour with one or both of v 01 v_{01} and x 00 x_{00}. If w 011 ∼ x 01 w_{011}\sim x_{01} were true, then the arcs u 0 ​ v 00 u_{0}v_{00} and u 0 ​ v 01 u_{0}v_{01} would lie on four 6 6 -cycles, and by vertex-transitivity, this would be true of all arcs of Γ \Gamma. It follows that x 00 x_{00} and x 01 x_{01} must have a common neighbour y 0 y_{0} regardless of this condition. If w 110 w_{110} were adjacent to x 01 x_{01}, then, by symmetry, x 11 x_{11} would have to be adjacent to y 0 y_{0}, giving us a pentagon. If, on the other hand, w 110 w_{110} were adjacent to y 0 y_{0}, then symmetry would imply x 01 ∼ x 11 x_{01}\sim x_{11}, and the neighbourhoods of all vertices determined so far would be determined, with the execption of the adjacent vertices w 011 w_{011} and w 100 w_{100}, which are missing an arc each. Removing these two vertices from the graph Γ \Gamma would yield a disconnected graph; since this is not true, say, for the vertex u 0 u_{0} and any of its neighbours, this contradicts vertex-transitivity of Γ \Gamma. Thus, the remaining neighbour of w 110 w_{110} must be a new vertex x 10 x_{10}, which, by symmetry, has a common neighbour y 1 y_{1} with x 11 x_{11}, see Figure 14 (a).

(a) (b)

Figure 14. (a) Constructing a graph of girth 6 6 with c = 4 c=4 and w 010 ∼ x 00 w_{010}\sim x_{00}, w 101 ∼ x 11 w_{101}\sim x_{11}. (b) Additionally assuming a = b = 3 a=b=3. The dashed and double edges should lie on three and four 6 6 -cycles, respectively, however, this cannot be attained for w 001 ​ x 01 w_{001}x_{01} and w 110 ​ x 10 w_{110}x_{10}.

Assume a = b = 3 a=b=3, and let z 0 z_{0} and z 1 z_{1} be the remaining neighbours of w 011 w_{011} and w 100 w_{100}, respectively. Then the vertex v 00 v_{00} has no common neighbours with w 100 w_{100} or z 0 z_{0}, so the arcs v 01 ​ w 011 v_{01}w_{011} and, by symmetry, also v 10 ​ w 100 v_{10}w_{100}, each lie on precisely three 6 6 -cycles. As w 110 w_{110} cannot have a common neighbour with w 100 w_{100} (or v 11 ​ u 1 ​ v 10 v_{11}u_{1}v_{10} would lie on two 6 6 -cycles), it must have a common neighbour with z 0 z_{0}, which must be the vertex x 10 x_{10}. Therefore, we have y 1 = z 0 y_{1}=z_{0}, and by symmetry also y 0 = z 1 y_{0}=z_{1}, see Figure 14 (b). The arcs v 01 ​ w 010 v_{01}w_{010} and v 10 ​ w 101 v_{10}w_{101} now lie on four 6 6 -cycles each. It follows that w 001 ​ w 101 w_{001}w_{101} and w 010 ​ w 110 w_{010}w_{110} should lie on three 6 6 -cycles each. As this is also true of v 00 ​ w 001 v_{00}w_{001} and v 11 ​ w 110 v_{11}w_{110}, the arcs w 001 ​ x 01 w_{001}x_{01} and w 110 ​ x 10 w_{110}x_{10} should lie on four 6 6 -cycles each, which, however, cannot be attained.

We thus have a = b = 4 a=b=4 and w 011 ∼ x 01 w_{011}\sim x_{01}, w 100 ∼ x 10 w_{100}\sim x_{10}. For the arc w 000 ​ w 111 w_{000}w_{111} to lie on four 6 6 -cycles, we must have y 0 ∼ y 1 y_{0}\sim y_{1}, which completes the graph. Figure 15 shows the graph Γ \Gamma and the Desargues configuration with points and lines labelled with the vertices of Γ \Gamma, showing that Γ \Gamma is indeed its incidence graph, i.e., it is isomorphic to the Desargues graph.

(a) (b)

Figure 15. (a) Completing Figure 14 (a) to obtain the Desargues graph. (b) The Desargues configuration with points and lines labelled with the vertex labels of (a).

Finally, we’re left with the case when w 011 ∼ x 00 w_{011}\sim x_{00}. By symmetry, we then also have w 100 ∼ x 11 w_{100}\sim x_{11}. As v 01 v_{01} would have no common neighbour with x 01 x_{01} if the arc v 00 ​ w 001 v_{00}w_{001} lay on precisely three 6 6 -cycles (or v 00 ​ u 0 ​ v 01 v_{00}u_{0}v_{01} would lie on two 6 6 -cycles), each of the vertices w 111 w_{111} and x 00 x_{00} must have a common neighbour with one of w 101 w_{101} and x 01 x_{01} regardless of this condition. As w 101 w_{101} and w 111 w_{111} have no common neighbour, we must have x 01 ∼ x 11 x_{01}\sim x_{11}, and the common neighbour of w 101 w_{101} and x 00 x_{00} must be a new vertex x 10 x_{10}. By symmetry, we then also have w 011 ∼ x 01 w_{011}\sim x_{01} and w 110 ∼ x 10 w_{110}\sim x_{10}, which completes the graph. Figure 16 shows the labelling of vertices of Γ \Gamma with elements of ℤ 3 × 𝔻 3 \mathbb{Z}_{3}\times\mathbb{D}_{3}, establishing that Γ \Gamma is isomorphic to Σ 3 \Sigma_{3}, and the Pappus configuration with points and lines labelled with the vertices of Γ \Gamma, showing that Γ \Gamma is indeed its incidence graph, i.e., it is isomorphic to the Pappus graph. ∎

(a) (b)

Figure 16. (a) Completing Figure 14 (a) to obtain the Pappus graph. (b) The Pappus configuration with points and lines labelled with the vertex labels of (a).

###### Lemma 20.

Let Γ \Gamma be a connected cubic vertex-transitive graph of girth 6 6 with signature ( a, b, c) (a,b,c), where c = 3 c=3. Then a = 2 a=2, b = 3 b=3 and Γ \Gamma is isomorphic to Δ n \Delta_{n} or Σ n \Sigma_{n} for some n ≥ 4 n\geq 4.

###### Proof.

Lemmas 7 and 8 imply that we have a ∈ { 1, 2 } a\in\{1,2\} and b = a + 1 b=a+1. It follows that each vertex is the middle point of three 2 2 -paths lying on precisely a − 1 a-1, one and two 6 6 -cycles.

First, let us prove that no 3 3 -path lies on two 6 6 -cycles. Suppose that the 3 3 -path u ​ v ​ w ​ x uvwx lies on two 6 6 -cycles. Then we must have vertices y, z, y ′, z ′ y,z,y^{\prime},z^{\prime} such that u ​ z ​ y ​ x ​ y ′ ​ z ′ uzyxy^{\prime}z^{\prime} is a 6 6 -cycle, see Figure 17 (a). Now, all arcs with tail u u lie on at least two 6 6 -cycles, so we have a = 2 a=2 and b = 3 b=3. In particular, each 2 2 -path lies on at least one 6 6 -cycle. But the 2 2 -paths u ​ v ​ w uvw, u ​ z ​ y uzy and u ​ z ′ ​ y ′ uz^{\prime}y^{\prime} lie on two 6 6 -cycles each, so all arcs with tail u u must lie on three 6 6 -cycles, contradiction.

(a) (b) (c) (d)

Figure 17. Constructing a graph of girth 6 6 with c = 3 c=3. (a) The case when a 3 3 -path lies on two 6 6 -cycles, which leads to a contradiction. (b) Determining the number of 6 6 -cycles the arcs with tail v v lie on. (c) Assuming that both u ​ v uv and w ​ x wx lie on a a 6 6 -cycles, which leads to a contradiction. (d) Assuming a = 1 a=1 and b = 2 b=2, again leading to a contradiction. The dashed, thick and double edges lie on a a, a + 1 a+1 and three 6 6 -cycles, respectively.

Let H = u ​ v ​ w ​ x ​ y ​ z H=uvwxyz be a 6 6 -cycle in Γ \Gamma. Suppose that the arc u ​ v uv lies on precisely a a 6 6 -cycles. The 2 2 -path u ​ v ​ w uvw must then lie on precisely one 6 6 -cycle, and there is a neighbour u ′ u^{\prime} of v v such that the 2 2 -path u ​ v ​ u ′ uvu^{\prime} lies on precisely a − 1 a-1 6 6 -cycles, see Figure 17 (b). The 2 2 -path u ′ ​ v ​ w u^{\prime}vw then lies on two 6 6 -cycles.

We will now show that the arc w ​ x wx lies on a + 1 a+1 6 6 -cycles. Suppose that this is not the case. The arc w ​ x wx thus lies on a a 6 6 -cycles. Similarly as before, the 2 2 -path v ​ w ​ x vwx also lies on precisely one 6 6 -cycle and there is a neighbour x ′ x^{\prime} of w w such that the 2 2 -paths x ​ w ​ x ′ xwx^{\prime} and v ​ w ​ x ′ vwx^{\prime} lie on precisely a − 1 a-1 and two 6 6 -cycles, respectively, see Figure 17 (c). As the 2 2 -paths u ​ v ​ w uvw and v ​ w ​ x vwx both lie on H H and neither of u ′ ​ v ​ w u^{\prime}vw and v ​ w ​ x ′ vwx^{\prime} lies on H H, it follows that the 3 3 -path u ′ ​ v ​ w ​ x ′ u^{\prime}vwx^{\prime} must lie on two 6 6 -cycles, contradiction.

Therefore, the edge w ​ x wx lies on a + 1 a+1 6 6 -cycles. Assume that a = 1 a=1. By a similar argument as before, the arcs z ​ u zu, y ​ z yz and x ​ y xy must then lie on three, two and three 6 6 -cycles, respectively. Let x ′ x^{\prime}, w ′ w^{\prime} and z ′ z^{\prime} be the remaining neighbours of w w, x x and y y, respectively, see Figure 17 (d). The 2 2 -path x ′ ​ w ​ x x^{\prime}wx cannot lie on any 6 6 -cycle, and the 2 2 -paths w ′ ​ x ​ y w^{\prime}xy and x ​ y ​ z ′ xyz^{\prime} must lie on one 6 6 -cycle each. By the previous argument, the latter two 2 2 -paths must lie on distinct 6 6 -cycles. Therefore, the 6 6 -cycle H ′ H^{\prime} containing the vertices z ′ z^{\prime}, y y, x x must also contain the vertex w w. However, neither v v nor x ′ x^{\prime} can be contained in H ′ H^{\prime} – contradiction.

It follows that a = 2 a=2 and b = 3 b=3, and each 6 6 -cycle contains at most 2 2 edges lying on precisely two 6 6 -cycles. Let m m be the number of edges lying on precisely two 6 6 -cycles. Then there are 2 ​ m 2m edges lying on three 6 6 -cycles, and the graph has 2 ​ m 2m vertices. As each vertex lies on four 6 6 -cycles, the graph Γ \Gamma has precisely 4 ​ m / 3 4m/3 6 6 -cycles. m m must then be divisible by 3 3 – in particular, the number of vertices is a multiple of 6 6. Vertex-transitivity implies that for each two arcs s, t s,t lying on precisely two 6 6 -cycles, there is an automorphism φ \varphi of Γ \Gamma such that s φ = t s^{\varphi}=t. Suppose that there is a 6 6 -cycle containing a single edge lying on precisely two 6 6 -cycles. If each such edge lies on two such 6 6 -cycles, then there are 2 ​ m > 4 ​ m / 3 2m>4m/3 such 6 6 -cycles, contradiction. Therefore, each such edge lies on one 6 6 -cycle containing 2 2 such edges, which gives m m and m / 2 m/2 6 6 -cycles with 1 1 and 2 2 such edges, respectively, again exceeding the total number of 6 6 -cycles.

It follows that there must be m m 6 6 -cycles containing 2 2 edges lying on two 6 6 -cycles each, and m / 3 m/3 6 6 -cycles containing no such edges. Let W 0 = v 0 ​ w 0 ​ x 0 ​ x 1 ​ w 1 ​ v 1 W_{0}=v_{0}w_{0}x_{0}x_{1}w_{1}v_{1} be a 6 6 -cycle such that the arcs v 0 ​ v 1 v_{0}v_{1} and x 0 ​ x 1 x_{0}x_{1} lie on two 6 6 -cycles each. Let u 0 u_{0}, y 0 y_{0}, u 1 u_{1}, w 2 w_{2} and y 1 y_{1} be the remaining neighbours of v 0 v_{0}, x 0 x_{0}, v 1 v_{1}, w 1 w_{1} and x 1 x_{1}, respectively. Since each of the 2 2 -paths w 0 ​ x 0 ​ x 1 w_{0}x_{0}x_{1}, w 1 ​ x 1 ​ x 0 w_{1}x_{1}x_{0}, y 0 ​ x 0 ​ x 1 y_{0}x_{0}x_{1}, y 1 ​ x 1 ​ x 0 y_{1}x_{1}x_{0} lies on precisely one 6 6 -cycle, and the first two lie on W 0 W_{0}, it follows that there must be a 6 6 -cycle containing the last two 2 2 -paths, say, Y 0 = x 0 ​ y 0 ​ z 0 ​ z 1 ​ y 1 ​ x 1 Y_{0}=x_{0}y_{0}z_{0}z_{1}y_{1}x_{1}. As the arc x 0 ​ x 1 x_{0}x_{1} already lies on two 6 6 -cycles, y 1 y_{1} cannot be adjacent to u 0 u_{0}, so its remaining neighbour must be a new vertex y 2 y_{2}. By the same argument, w 2 w_{2} is not adjacent to z 0 z_{0} and y 2 y_{2} is not adjacent to v 0 v_{0}. The 6 6 -cycle containing the 2 2 -path x 1 ​ w 1 ​ w 2 x_{1}w_{1}w_{2} is then X 1 = w 1 ​ x 1 ​ y 1 ​ y 2 ​ x 2 ​ w 2 X_{1}=w_{1}x_{1}y_{1}y_{2}x_{2}w_{2}, where x 2 x_{2} is a new vertex. The second 6 6 -cycle containing the 2 2 -path v 1 ​ w 1 ​ x 1 v_{1}w_{1}x_{1} must then also contain the vertices u 1 u_{1} and y 1 y_{1}, and by the same argument also the vertex z 1 z_{1}. Therefore, we have u 1 ∼ z 1 u_{1}\sim z_{1}, and by the same argument also u 0 ∼ z 0 u_{0}\sim z_{0}. By similar arguments, we may add new vertices u 2 u_{2}, v 2 v_{2} and z 2 z_{2} such that u 1 ∼ u 2 u_{1}\sim u_{2} and u 2 ​ v 2 ​ w 2 ​ x 2 ​ y 2 ​ z 2 u_{2}v_{2}w_{2}x_{2}y_{2}z_{2} is a 6 6 -cycle, see Figure 18 (a).

(a) (b)

Figure 18. Constructing a graph of girth 6 6 with signature ( 2, 3, 3) (2,3,3) embedded on a cylinder. In (a), the basic structure is shown. In (b), new vertices have been added to prevent arcs lying on more than three 6 6 -cycles. The dashed and double edges lie on two and three 6 6 -cycles, respectively.

Let α ∈ { u, w, y } \alpha\in\{u,w,y\} and β ∈ { v, x, z } \beta\in\{v,x,z\}. The arcs of form α 1 ​ α 2 \alpha_{1}\alpha_{2} and β 0 ​ β 1 \beta_{0}\beta_{1} all already lie on two 6 6 -cycles, so we cannot have edges of form α 0 ​ β 2 \alpha_{0}\beta_{2}. Therefore, we may add a new 6 6 -cycle u 3 ​ v 3 ​ w 3 ​ x 3 ​ y 3 ​ z 3 u_{3}v_{3}w_{3}x_{3}y_{3}z_{3} and arcs of form β 2 ​ β 3 \beta_{2}\beta_{3}, see Figure 18 (b). We have now arrived at a point where we have determined 12 ​ t 12t vertices of Γ \Gamma for some t ≥ 2 t\geq 2, and each of the vertices α 0 \alpha_{0} and α 2 ​ t − 1 \alpha_{2t-1} is missing an arc.

First assume α 0 ∼ α 2 ​ t − 1 \alpha_{0}\sim\alpha_{2t-1} for some α \alpha – without loss of generality, say, w 0 ∼ w 2 ​ t − 1 w_{0}\sim w_{2t-1}. Then each of u 0 u_{0} and y 0 y_{0} must be adjacent to one of u 2 ​ t − 1 u_{2t-1} and y 2 ​ t − 1 y_{2t-1}. If u 0 ∼ y 2 ​ t − 1 u_{0}\sim y_{2t-1} and y 0 ∼ u 2 ​ t − 1 y_{0}\sim u_{2t-1}, then an automorphism φ \varphi of Γ \Gamma with w 0 φ = u 0 w_{0}^{\varphi}=u_{0} has w i φ = u i w_{i}^{\varphi}=u_{i} for all i i ( 0 ≤ i ≤ 2 ​ t − 1 0\leq i\leq 2t-1). We must however also have w 2 ​ t − 1 φ = y 2 ​ t − 1 w_{2t-1}^{\varphi}=y_{2t-1}, contradiction. Therefore, we have u 0 ∼ u 2 ​ t − 1 u_{0}\sim u_{2t-1} and y 0 ∼ y 2 ​ t − 1 y_{0}\sim y_{2t-1}. Let n = 2 ​ t n=2t. Identifying the vertices u 2 ​ i u_{2i}, v 2 ​ i v_{2i}, w 2 ​ i w_{2i}, x 2 ​ i x_{2i}, y 2 ​ i y_{2i}, z 2 ​ i z_{2i}, u 2 ​ i + 1 u_{2i+1}, v 2 ​ i + 1 v_{2i+1}, w 2 ​ i + 1 w_{2i+1}, x 2 ​ i + 1 x_{2i+1}, y 2 ​ i + 1 y_{2i+1} and z 2 ​ i + 1 z_{2i+1} with τ 2 ​ i + \tau_{2i}^{+}, ρ 2 ​ i − \rho_{2i}^{-}, τ 2 ​ i 0 \tau_{2i}^{0}, ρ 2 ​ i + \rho_{2i}^{+}, τ 2 ​ i − \tau_{2i}^{-}, ρ 2 ​ i 0 \rho_{2i}^{0}, ρ 2 ​ i + 1 + \rho_{2i+1}^{+}, τ 2 ​ i + 1 − \tau_{2i+1}^{-}, ρ 2 ​ i + 1 0 \rho_{2i+1}^{0}, τ 2 ​ i + 1 + \tau_{2i+1}^{+}, ρ 2 ​ i + 1 − \rho_{2i+1}^{-} and τ 2 ​ i + 1 0 \tau_{2i+1}^{0} ( 0 ≤ i ≤ t − 1 0\leq i\leq t-1) establishes that the graph is isomorphic to Σ n \Sigma_{n}, see for example Figure 19 (a).

(a) (b)

Figure 19. Completing Figure 18 (b) to obtain the graphs Σ 4 \Sigma_{4} in (a) and Δ 4 \Delta_{4} in (b) embedded on a torus. The dashed and double edges lie on two and three 6 6 -cycles, respectively.

Now assume that α 0 ∼ α 2 ​ t − 1 ′ \alpha_{0}\sim\alpha^{\prime}_{2t-1} for some distinct α, α ′ ∈ { u, w, y } \alpha,\alpha^{\prime}\in\{u,w,y\}. Again, without loss of generality we may assume u 0 ∼ y 2 ​ t − 1 u_{0}\sim y_{2t-1}. Then each of w 0 w_{0} and y 0 y_{0} must be adjacent to one of u 2 ​ t − 1 u_{2t-1} and w 2 ​ t − 1 w_{2t-1}. By the above argument, w 0 ∼ w 2 ​ t − 1 w_{0}\sim w_{2t-1} is not possible, so we must have w 0 ∼ u 2 ​ t − 1 w_{0}\sim u_{2t-1} and y 0 ∼ w 2 ​ t − 1 y_{0}\sim w_{2t-1}. Let n = 2 ​ t n=2t and k = 3 / gcd ⁡ ( n, 3) k=3/\gcd(n,3). Identifying the vertices u 2 ​ i u_{2i}, v 2 ​ i v_{2i}, w 2 ​ i w_{2i}, x 2 ​ i x_{2i}, y 2 ​ i y_{2i}, z 2 ​ i z_{2i}, u 2 ​ i + 1 u_{2i+1}, v 2 ​ i + 1 v_{2i+1}, w 2 ​ i + 1 w_{2i+1}, x 2 ​ i + 1 x_{2i+1}, y 2 ​ i + 1 y_{2i+1} and z 2 ​ i + 1 z_{2i+1} ( 0 ≤ i ≤ t − 1 0\leq i\leq t-1) with τ ( 2 ​ k − n) ​ i \tau_{(2k\!-\!n)i}, ρ ( 2 ​ k − n) ​ i − n \rho_{(2k\!-\!n)i\!-\!n}, τ ( 2 ​ k − n) ​ i − n \tau_{(2k\!-\!n)i\!-\!n}, ρ ( 2 ​ k − n) ​ i + n \rho_{(2k\!-\!n)i\!+\!n}, τ ( 2 ​ k − n) ​ i + n \tau_{(2k\!-\!n)i\!+\!n}, ρ ( 2 ​ k − n) ​ i \rho_{(2k\!-\!n)i}, ρ ( 2 ​ k − n) ​ i + k − n \rho_{(2k\!-\!n)i\!+\!k\!-\!n}, τ ( 2 ​ k − n) ​ i + k − n \tau_{(2k\!-\!n)i\!+\!k\!-\!n}, ρ ( 2 ​ k − n) ​ i + k + n \rho_{(2k\!-\!n)i\!+\!k\!+\!n}, τ ( 2 ​ k − n) ​ i + k + n \tau_{(2k\!-\!n)i\!+\!k\!+\!n}, ρ ( 2 ​ k − n) ​ i + k \rho_{(2k\!-\!n)i\!+\!k} and τ ( 2 ​ k − n) ​ i + k − n \tau_{(2k\!-\!n)i\!+\!k\!-\!n} when n ≡ 2 ( mod 3) n\equiv 2\pmod{3}, and with τ ( 2 ​ k − n) ​ i + n \tau_{(2k\!-\!n)i\!+\!n}, ρ ( 2 ​ k − n) ​ i + n \rho_{(2k\!-\!n)i\!+\!n}, τ ( 2 ​ k − n) ​ i − n \tau_{(2k\!-\!n)i\!-\!n}, ρ ( 2 ​ k − n) ​ i − n \rho_{(2k\!-\!n)i\!-\!n}, τ ( 2 ​ k − n) ​ i \tau_{(2k\!-\!n)i}, ρ ( 2 ​ k − n) ​ i \rho_{(2k\!-\!n)i}, ρ ( 2 ​ k − n) ​ i + k \rho_{(2k\!-\!n)i\!+\!k}, τ ( 2 ​ k − n) ​ i + k + n \tau_{(2k\!-\!n)i\!+\!k\!+\!n}, ρ ( 2 ​ k − n) ​ i + k + n \rho_{(2k\!-\!n)i\!+\!k\!+\!n}, τ ( 2 ​ k − n) ​ i + k − n \tau_{(2k\!-\!n)i\!+\!k\!-\!n}, ρ ( 2 ​ k − n) ​ i + k − n \rho_{(2k\!-\!n)i\!+\!k\!-\!n} and τ ( 2 ​ k − n) ​ i + k \tau_{(2k\!-\!n)i\!+\!k} otherwise, establishes that the graph is isomorphic to Δ n \Delta_{n}, see for example Figure 19 (b).

If, on the other hand, none of α 2 ​ t − 1 \alpha_{2t-1} are adjacent to known vertices, we must have a new 6 6 -cycle u 2 ​ t ​ v 2 ​ t ​ w 2 ​ t ​ x 2 ​ t ​ y 2 ​ t ​ z 2 ​ t u_{2t}v_{2t}w_{2t}x_{2t}y_{2t}z_{2t} and α 2 ​ t − 1 ∼ α 2 ​ t \alpha_{2t-1}\sim\alpha_{2t} for all α ∈ { u, w, y } \alpha\in\{u,w,y\}. If none of α 0 \alpha_{0} is adjacent to known vertices either, then we must add another 6 6 -cycle in a similar fashion, which again gives us the previous case. Otherwise, first assume, say, w 0 ∼ z 2 ​ t w_{0}\sim z_{2t}. Then each of u 0 u_{0} and y 0 y_{0} must be adjacent to one of v 2 ​ t v_{2t} and x 2 ​ t x_{2t}. If u 0 ∼ v 2 ​ t u_{0}\sim v_{2t} and y 0 ∼ x 2 ​ t y_{0}\sim x_{2t}, then an automorphism φ \varphi of Γ \Gamma with w 0 φ = u 0 w_{0}^{\varphi}=u_{0} has w i φ = u i w_{i}^{\varphi}=u_{i} and then also z i φ = x i z_{i}^{\varphi}=x_{i} for all i i ( 0 ≤ i ≤ 2 ​ t 0\leq i\leq 2t). We must however also have z 2 ​ t φ = v 2 ​ t z_{2t}^{\varphi}=v_{2t}, contradiction. Therefore, we have u 0 ∼ x 2 ​ t u_{0}\sim x_{2t} and y 0 ∼ v 2 ​ t y_{0}\sim v_{2t}. Let n = 2 ​ t + 1 n=2t+1. Identifying the vertices u 2 ​ i u_{2i}, v 2 ​ i v_{2i}, w 2 ​ i w_{2i}, x 2 ​ i x_{2i}, y 2 ​ i y_{2i}, z 2 ​ i z_{2i} with τ 2 ​ i + \tau_{2i}^{+}, ρ 2 ​ i − \rho_{2i}^{-}, τ 2 ​ i 0 \tau_{2i}^{0}, ρ 2 ​ i + \rho_{2i}^{+}, τ 2 ​ i − \tau_{2i}^{-}, ρ 2 ​ i 0 \rho_{2i}^{0} ( 0 ≤ i ≤ t 0\leq i\leq t), and u 2 ​ i + 1 u_{2i+1}, v 2 ​ i + 1 v_{2i+1}, w 2 ​ i + 1 w_{2i+1}, x 2 ​ i + 1 x_{2i+1}, y 2 ​ i + 1 y_{2i+1}, z 2 ​ i + 1 z_{2i+1} with ρ 2 ​ i + 1 + \rho_{2i+1}^{+}, τ 2 ​ i + 1 − \tau_{2i+1}^{-}, ρ 2 ​ i + 1 0 \rho_{2i+1}^{0}, τ 2 ​ i + 1 + \tau_{2i+1}^{+}, ρ 2 ​ i + 1 − \rho_{2i+1}^{-}, τ 2 ​ i + 1 0 \tau_{2i+1}^{0} ( 0 ≤ i ≤ t − 1 0\leq i\leq t-1) establishes that the graph is isomorphic to Σ n \Sigma_{n}, see for example Figure 20 (a).

(a) (b)

Figure 20. Completing Figure 18 (b) to obtain the graphs Σ 5 \Sigma_{5} in (a) and Δ 5 \Delta_{5} in (b) embedded on a torus. The dashed and double edges lie on two and three 6 6 -cycles, respectively.

Finally, assume, say, y 0 ∼ x 2 ​ t y_{0}\sim x_{2t}. Then each of u 0 u_{0} and w 0 w_{0} must be adjacent to one of v 2 ​ t v_{2t} and z 2 ​ t z_{2t}. By the above argument, u 0 ∼ v 2 ​ t u_{0}\sim v_{2t} is not possible, so we must have u 0 ∼ z 2 ​ t u_{0}\sim z_{2t} and w 0 ∼ v 2 ​ t w_{0}\sim v_{2t}. Let n = 2 ​ t + 1 n=2t+1 and k = 3 / gcd ⁡ ( n, 3) k=3/\gcd(n,3). Identifying the vertices u 2 ​ i u_{2i}, v 2 ​ i v_{2i}, w 2 ​ i w_{2i}, x 2 ​ i x_{2i}, y 2 ​ i y_{2i}, z 2 ​ i z_{2i} ( 0 ≤ i ≤ t 0\leq i\leq t) and u 2 ​ i + 1 u_{2i+1}, v 2 ​ i + 1 v_{2i+1}, w 2 ​ i + 1 w_{2i+1}, x 2 ​ i + 1 x_{2i+1}, y 2 ​ i + 1 y_{2i+1}, z 2 ​ i + 1 z_{2i+1} ( 0 ≤ i ≤ t − 1 0\leq i\leq t-1) with τ ( 2 ​ k − n) ​ i + n \tau_{(2k\!-\!n)i\!+\!n}, ρ ( 2 ​ k − n) ​ i + n \rho_{(2k\!-\!n)i\!+\!n}, τ ( 2 ​ k − n) ​ i − n \tau_{(2k\!-\!n)i\!-\!n}, ρ ( 2 ​ k − n) ​ i − n \rho_{(2k\!-\!n)i\!-\!n}, τ ( 2 ​ k − n) ​ i \tau_{(2k\!-\!n)i}, ρ ( 2 ​ k − n) ​ i \rho_{(2k\!-\!n)i} and ρ ( 2 ​ k − n) ​ i + k \rho_{(2k\!-\!n)i\!+\!k}, τ ( 2 ​ k − n) ​ i + k + n \tau_{(2k\!-\!n)i\!+\!k\!+\!n}, ρ ( 2 ​ k − n) ​ i + k + n \rho_{(2k\!-\!n)i\!+\!k\!+\!n}, τ ( 2 ​ k − n) ​ i + k − n \tau_{(2k\!-\!n)i\!+\!k\!-\!n}, ρ ( 2 ​ k − n) ​ i + k − n \rho_{(2k\!-\!n)i\!+\!k\!-\!n}, τ ( 2 ​ k − n) ​ i + k \tau_{(2k\!-\!n)i\!+\!k} when n ≡ 2 ( mod 3) n\equiv 2\pmod{3}, and with τ ( 2 ​ k − n) ​ i \tau_{(2k\!-\!n)i}, ρ ( 2 ​ k − n) ​ i − n \rho_{(2k\!-\!n)i\!-\!n}, τ ( 2 ​ k − n) ​ i − n \tau_{(2k\!-\!n)i\!-\!n}, ρ ( 2 ​ k − n) ​ i + n \rho_{(2k\!-\!n)i\!+\!n}, τ ( 2 ​ k − n) ​ i + n \tau_{(2k\!-\!n)i\!+\!n}, ρ ( 2 ​ k − n) ​ i \rho_{(2k\!-\!n)i} and ρ ( 2 ​ k − n) ​ i + k − n \rho_{(2k\!-\!n)i\!+\!k\!-\!n}, τ ( 2 ​ k − n) ​ i + k − n \tau_{(2k\!-\!n)i\!+\!k\!-\!n}, ρ ( 2 ​ k − n) ​ i + k + n \rho_{(2k\!-\!n)i\!+\!k\!+\!n}, τ ( 2 ​ k − n) ​ i + k + n \tau_{(2k\!-\!n)i\!+\!k\!+\!n}, ρ ( 2 ​ k − n) ​ i + k \rho_{(2k\!-\!n)i\!+\!k}, τ ( 2 ​ k − n) ​ i + k − n \tau_{(2k\!-\!n)i\!+\!k\!-\!n} otherwise, establishes that the graph is isomorphic to Δ n \Delta_{n}, see for example Figure 20 (b). ∎

We can now wrap up our proof of Theorem 1. Let Γ \Gamma be a simple connected cubic vertex-transitive graph and let ( a, b, c) (a,b,c) be its signature. Theorem 13 and Lemmas 15 – 20 cover the cases when c ≥ 3 c\geq 3. Of the graphs appearing in these lemmas, only the Desargues graph does not admit an embedding onto a torus as a vertex-transitive map of type { 6, 3 } \{6,3\}.

We are left with the cases when c ≤ 2 c\leq 2. If ( a, b, c) = ( 2, 2, 2) (a,b,c)=(2,2,2), then, by Theorem 12, Γ \Gamma is the skeleton of a vertex-transitive map of type { 6, 3 } \{6,3\} embedded on a surface of Euler characteristic χ = 0 \chi=0, i.e., a torus or a Klein bottle. By Wilson [35], the skeleton of a vertex-transitive map of type { 6, 3 } \{6,3\} on a Klein bottle has girth at most 4 4, so Γ \Gamma must be the skeleton of a vertex-transitive map of type { 6, 3 } \{6,3\} on a torus. If ( a, b, c) = ( 1, 1, 2) (a,b,c)=(1,1,2), then, by Theorem 11, Γ \Gamma is the skeleton of the truncation of a connected map of type { 3, ℓ } \{3,\ell\} for some ℓ > 6 \ell>6. If ( a, b, c) = ( 0, 1, 1) (a,b,c)=(0,1,1), then, by Theorem 10, Γ \Gamma is the truncation of a 6 6 -regular graph Γ ^ \hat{\Gamma} with respect to an arc-transitive dihedral scheme. This finishes the proof of Theorem 1.

## 4. Larger girths

We wrap up this paper with a short discussion on the problem of extending the results proved here to graphs of larger girth. It is not surprising that the complexity of the situation grows with the girth and that several new infinite families arise, especially those with a small number of girth cycles, that is, those with signatures ( a, b, c) (a,b,c) where c c is relatively small. On the other hand, as computational evidence presented below suggests, further classification results could be obtained when one restricts to specific signatures with large values of c c and/or a, b a,b. We leave an in-depth analysis of these cases for future work and instead list the signatures of graphs of girths 7 7, 8 8 and 9 9 appearing in the census of connected cubic vertex-transitive graphs on at most 1280 1280 vertices by Potočnik, Spiga and Verret [26].

Tables 1, 2 and 3 show the number of connected cubic vertex-transitive graphs with at most 1280 1280 vertices for each signature ( a, b, c) (a,b,c) that appears, and also the number of symmetric graphs among those – clearly, the latter all have a = b = c a=b=c, so a dash is shown in the other rows in the tables. Note that substantially more signatures appear for girth 8 8 than for girths 7 7 and 9 9 – this is mainly due to part ( 3) in Lemma 7, which forbids signatures with c = a + b c=a+b in graphs of odd girths. By Theorem 12, the graphs with signatures ( 2, 2, 2) (2,2,2) are skeletons of maps – unlike with girths at most 6 6, there are cases of such maps on nonorientable surfaces.

signature vertex-transitive symmetric comments ( 0, 1, 1) (0,1,1) 76 76 − - truncations of 7 7 -regular graphs (Theorem 10) ( 2, 2, 2) (2,2,2) 8 8 8 8 skeletons of maps of type { 7, 3 } \{7,3\} (Theorem 12) ( 4, 4, 4) (4,4,4) 1 1 1 1 Coxeter graph ( 4, 4, 6) (4,4,6) 104 104 − - ( 4, 5, 5) (4,5,5) 3 3 − -

Table 1. Signatures of cubic vertex-transitive graphs of girth 7 7.

signature vertex-transitive symmetric comments ( 0, 1, 1) (0,1,1) 7262 7262 − - truncations of 8 8 -regular graphs (Theorem 10) ( 1, 1, 2) (1,1,2) 3107 3107 − - truncations of maps of type { 4, ℓ } \{4,\ell\} (Theorem 11) ( 1, 2, 3) (1,2,3) 153 153 − - ( 2, 2, 2) (2,2,2) 457 457 21 21 skeletons of maps of type { 8, 3 } \{8,3\} (Theorem 12) ( 2, 2, 4) (2,2,4) 1083 1083 − - ( 2, 3, 3) (2,3,3) 1033 1033 − - ( 3, 3, 4) (3,3,4) 51 51 − - ( 3, 4, 5) (3,4,5) 1 1 − - Cay ⁡ ( 𝔻 5 × 𝕊 3, { ( τ 0, ()), ( τ 1, ( 1 2)), ( τ 2, ( 1 3)) }) \operatorname{Cay}(\mathbb{D}_{5}\times\mathbb{S}_{3},\{(\tau_{0},()),(\tau_{1},(1\ 2)),(\tau_{2},(1\ 3))\}) ( 4, 4, 4) (4,4,4) 108 108 4 4 ( 4, 6, 6) (4,6,6) 62 62 − - ( 5, 5, 6) (5,5,6) 207 207 − - ( 6, 6, 6) (6,6,6) 1 1 0 0 Cay ⁡ ( GL ⁡ ( 2, 3), { ( 0 1 1 0), ( 1 2 2 0), ( 0 2 2 2) }) \operatorname{Cay}(\operatorname{GL}(2,3),\{{0\ 1\choose 1\ 0},{1\ 2\choose 2\ 0},{0\ 2\choose 2\ 2}\}) ( 8, 8, 8) (8,8,8) 3 3 2 2 ( 16, 16, 16) (16,16,16) 1 1 1 1 Tutte-Coxeter graph (Theorem 13)

Table 2. Signatures of cubic vertex-transitive graphs of girth 8 8.

signature vertex-transitive symmetric comments ( 0, 1, 1) (0,1,1) 51 51 − - truncations of 9 9 -regular graphs (Theorem 10) ( 2, 2, 2) (2,2,2) 156 156 12 12 skeletons of maps of type { 9, 3 } \{9,3\} (Theorem 12) ( 2, 3, 3) (2,3,3) 3 3 − - ( 4, 4, 4) (4,4,4) 2 2 2 2 ( 6, 6, 6) (6,6,6) 5 5 3 3 ( 8, 8, 8) (8,8,8) 2 2 1 1 Biggs-Smith graph (symmetric case)

Table 3. Signatures of cubic vertex-transitive graphs of girth 9 9.

## References

- [1] B. Alspach. Honeycomb toroidal graphs, 2020. [arXiv:2007.05133][5].
- [2] B. Alspach and M. Dean. Honeycomb toroidal graphs are Cayley graphs. Inform. Process. Lett., 109(13):705–708, 2009. [doi:10.1016/j.ipl.2009.03.009][6].
- [3] A. Altshuler. Construction and enumeration of regular maps on the torus. Discrete Math., 4:201–217, 1973. [doi:10.1016/S0012-365X(73)80002-0][7].
- [4] V. Andova, P. Dimovski, M. Knor, and R. Škrekovski. On three constructions of nanotori. Mathematics, 8(11):2036, 2020. [doi:10.3390/math8112036][8].
- [5] L. W. Berman, I. Kovács, and G. I. Williams. On the flag graphs of regular abstract polytopes: Hamiltonicity and Cayley index. Discrete Math., 343:111599, 2020. [doi:10.1016/j.disc.2019.111599][9].
- [6] M. Conder and P. Lorimer. Automorphism groups of symmetric graphs of valency 3 3. J. Combin. Theory Ser. B, 47(1):60–72, 1989. [doi:10.1016/0095-8956(89)90065-8][10].
- [7] M. Conder and R. Nedela. Symmetric cubic graphs of small girth. J. Combin. Theory Ser. B, 97(5):757–768, 2007. [doi:10.1016/j.jctb.2007.01.001][11].
- [8] H. S. M. Coxeter, R. Frucht, and D. L. Powers. Zero-symmetric graphs. Academic Press, Inc. [Harcourt Brace Jovanovich, Publishers], New York-London, 1981.
- [9] D. Ž. Djoković and G. L. Miller. Regular groups of automorphisms of cubic graphs. J. Combin. Theory Ser. B, 29(2):195–230, 1980. [doi:10.1016/0095-8956(80)90081-7][12].
- [10] E. Eiben, R. Jajcay, and P. Šparl. Symmetry properties of generalized graph truncations. J. Combin. Theory Ser. B, 137:291–315, 2019. [doi:10.1016/j.jctb.2019.01.002][13].
- [11] G. Exoo and R. Jajcay. Recursive constructions of small regular graphs of given degree and girth. Discrete Math., 312(17):2612–1619, 2012. [doi:10.1016/j.disc.2011.10.021][14].
- [12] Y.-Q. Feng and R. Nedela. Symmetric cubic graphs of girth at most 7 7. Acta Univ. M. Belii Ser. Math., (13):33–55, 2006. [http://actamath.savbb.sk/pdf/acta1303.pdf][15].
- [13] R. M. Foster. Geometrical circuits of electrical networks. Trans. Amer. Inst. Elec. Engin., 51:309–317, 1932.
- [14] R. M. Foster and I. Z. Bouwer. The Foster Census. Charles Babbage Research Center, Winnipeg, 1988.
- [15] H. Glover and D. Marušič. Hamiltonicity of cubic Cayley graphs. J. Eur. Math. Soc., 9(4):775–787, 2007. [doi:10.4171/jems/96][16].
- [16] X.-H. Hua and Y.-Q. Feng. Cubic graphs admitting transitive non-abelian characteristically simple groups. Proc. Edinb. Math. Soc, 54(1):113–123, 2011. [doi:10.1017/S0013091509000625][17].
- [17] I. Hubard, A. Orbanić, D. Pellicer, and A. Ivić Weiss. Symmetries of equivelar 4 4 -toroids. Discrete Comput. Geom., 48(4):1110–1136, 2012. [doi:10.1007/s00454-012-9444-2][18].
- [18] S. Hüning, W. Imrich, J. Kloas, H. Schreiber, and T. W. Tucker. Distinguishing graphs of maximum valence 3. Electron. J. Combin., 26(4):4.36, 2019. [doi:10.37236/7281][19].
- [19] R. Jajcay, G. Kiss, and Š. Miklavič. Edge-girth-regular graphs. European J. Combin., 72:70–82, 2018. [doi:10.1016/j.ejc.2018.04.006][20].
- [20] W. Kurth. Enumeration of Platonic maps on the torus. Discrete Math., 61(1):71–83, 1986. [doi:10.1016/0012-365X(86)90029-4][21].
- [21] K. Kutnar and D. Marušič. Odd extensions of transitive groups via symmetric graphs—the cubic case. J. Combin. Theory Ser. B, 136:170–192, 2019. [doi:10.1016/j.jctb.2018.10.003][22].
- [22] K. Kutnar and D. Marušič. A complete classification of cubic symmetric graphs of girth 6. J. Combin. Theory Ser. B, 99(1):162–184, 2009. [doi:10.1016/j.jctb.2008.06.001][23].
- [23] P. Lorimer. Vertex-transitive graphs of valency 3 3. European J. Combin., 4(1):37–44, 1984. [doi:10.1016/S0195-6698(83)80007-9][24].
- [24] M. Morton. Classification of 4 4 - and 5 5 -arc-transitive cubic graphs of small girth. J. Austral. Math. Soc. Ser. A, 50(1):138–149, 1991.
- [25] M. A. Perles, H. Martini, and Y. S. Kupitz. Locally 3-transitive graphs of girth 4. J. Graph Theory, 84(4):512–520, 2017. [doi:10.1002/jgt.22038][25].
- [26] P. Potočnik, P. Spiga, and G. Verret. Cubic vertex-transitive graphs on up to 1280 1280 vertices. J. Symbolic Comput., 50:465–477, 2013. [doi:10.1016/j.jsc.2012.09.002][26].
- [27] P. Potočnik, P. Spiga, and G. Verret. Bounding the order of the vertex-stabiliser in 3-valent vertex-transitive and 4-valent arc-transitive graphs. J. Combin. Theory Ser. B, 111:148–180, 2015. [doi:10.1016/j.jctb.2014.10.002][27].
- [28] P. Potočnik and J. Vidali. Girth-regular graphs. Ars Math. Contemp., 17(2):349–368, 2019. [doi:10.26493/1855-3974.1684.b0d][28].
- [29] P. Potočnik and S. Wilson. Tetravalent edge-transitive graphs of girth at most 4 4. J. Combin. Theory Ser. B, 97(2):217–236, 2007. [doi:10.1016/j.jctb.2006.03.007][29].
- [30] P. Spiga. Semiregular elements in cubic vertex-transitive graphs and the restricted Burnside problem. Math. Proc. Cambridge Philos. Soc., 157(1):45–61, 2014. [doi:10.1017/S0305004114000188][30].
- [31] I. Stojmenović. Honeycomb networks: Topological properties and communication algorithms. IEEE Trans. Parallel Distrib. Systems, 8(10):1036–1042, 1997. [doi:10.1109/71.629486][31].
- [32] C. Thomassen. Tilings of the torus and the Klein bottle and vertex-transitive graphs on a fixed surface. Trans. Amer. Math. Soc., 323(2):605–635, 1991. [doi:10.2307/2001547][32].
- [33] W. T. Tutte. A family of cubical graphs. Proc. Cambridge Philos. Soc., 43:459–474, 1947. [doi:10.1017/s0305004100023720][33].
- [34] S. Wilson. Families of regular graphs in regular maps. J. Combin. Theory Ser. B, 85(2):269–289, 2002. [doi:10.1006/jctb.2001.2103][34].
- [35] S. Wilson. Uniform maps on the Klein bottle. J. Geom. Graph., 10(2):161–171, 2006.


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:primoz.potocnik@fmf.uni-lj.si
[4]: mailto:janos.vidali@fmf.uni-lj.si
[5]: http://arxiv.org/abs/2007.05133
[6]: http://dx.doi.org/10.1016/j.ipl.2009.03.009
[7]: http://dx.doi.org/10.1016/S0012-365X(73)80002-0
[8]: http://dx.doi.org/10.3390/math8112036
[9]: http://dx.doi.org/10.1016/j.disc.2019.111599
[10]: http://dx.doi.org/10.1016/0095-8956(89)90065-8
[11]: http://dx.doi.org/10.1016/j.jctb.2007.01.001
[12]: http://dx.doi.org/10.1016/0095-8956(80)90081-7
[13]: http://dx.doi.org/10.1016/j.jctb.2019.01.002
[14]: http://dx.doi.org/10.1016/j.disc.2011.10.021
[15]: http://actamath.savbb.sk/pdf/acta1303.pdf
[16]: http://dx.doi.org/10.4171/jems/96
[17]: http://dx.doi.org/10.1017/S0013091509000625
[18]: http://dx.doi.org/10.1007/s00454-012-9444-2
[19]: http://dx.doi.org/10.37236/7281
[20]: http://dx.doi.org/10.1016/j.ejc.2018.04.006
[21]: http://dx.doi.org/10.1016/0012-365X(86)90029-4
[22]: http://dx.doi.org/10.1016/j.jctb.2018.10.003
[23]: http://dx.doi.org/10.1016/j.jctb.2008.06.001
[24]: http://dx.doi.org/10.1016/S0195-6698(83)80007-9
[25]: http://dx.doi.org/10.1002/jgt.22038
[26]: http://dx.doi.org/10.1016/j.jsc.2012.09.002
[27]: http://dx.doi.org/10.1016/j.jctb.2014.10.002
[28]: http://dx.doi.org/10.26493/1855-3974.1684.b0d
[29]: http://dx.doi.org/10.1016/j.jctb.2006.03.007
[30]: http://dx.doi.org/10.1017/S0305004114000188
[31]: http://dx.doi.org/10.1109/71.629486
[32]: http://dx.doi.org/10.2307/2001547
[33]: http://dx.doi.org/10.1017/s0305004100023720
[34]: http://dx.doi.org/10.1006/jctb.2001.2103
