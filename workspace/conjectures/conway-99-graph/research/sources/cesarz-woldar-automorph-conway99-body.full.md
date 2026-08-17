<!-- source: https://arxiv.org/html/2308.02978v1 | converted from HTML -->

On the automorphism group of a putative Conway 99-graph

arXiv is now an independent nonprofit! [Learn more][1] ×

[License: arXiv.org perpetual non-exclusive license][2]

arXiv:2308.02978v1 [math.CO] 06 Aug 2023

# On the automorphism group of a putative Conway 99-graph

\firstname Patrick \middlename G. \lastname Cesarz Address: Dept. of Mathematics and Statistics
University of Wyoming
Laramie
WY 82071 (USA) Email address: [pcesarz@uwyo.edu][3] and \firstname Andrew \middlename J. \lastname Woldar Address: Dept. of Mathematics and Statistics
Villanova University
Villanova
PA 19085 (USA) Email address: [andrew.woldar@villanova.edu][4]

###### Abstract.

Let Γ \Gamma be a Conway 99-graph, that is, a strongly regular graph with parameters ( 99, 14, 1, 2) (99,14,1,2). In Makhnev and Minakova (On automorphisms of strongly regular graphs with parameters λ = 1 \lambda=1, μ = 2 \mu=2, Discrete Math. Appl. 14 (2) (2004) 201-210), the authors prove that the automorphism group G G of Γ \Gamma must have order dividing 2 ⋅ 3 3 ⋅ 7 ⋅ 11 2\cdot 3^{3}\cdot 7\cdot 11. They further show that if | G | |G| is divisible by 2 2 then | G | |G| must divide 42 42. In the present paper, we refine these results by proving that divisibility by 7 7 implies G ≅ ℤ 7 G\cong\mathbb{Z}_{7}. As a consequence, divisibility by 2 2 implies | G | |G| divides 6 6, \ie G G is isomorphic to one of ℤ 2, ℤ 6, S 3 \mathbb{Z}_{2},\mathbb{Z}_{6},S_{3}.

###### Key words and phrases:

Conway 99 99 -graph, strongly regular graph, automorphism group, orbit partition, orbit valencies

###### 1991 Mathematics Subject Classification

05E18, 05C25, 58D19

## 1. Introduction

The question of existence of a strongly regular graph with parameters ( 99, 14, 1, 2) (99,14,1,2) is a longstanding open problem. Its possible existence was first suggested by Norman Biggs in 1969 [2]. According to the account given by Richard Guy in [7], John H. Conway worked on this problem as early as 1975. Later, Conway would offer a $1,000 prize to anyone who could solve it (see [4], where it is listed as problem 2 among five posed open problems). From that point on, the graph came to be known colloquially as a *Conway 99-graph*.

In [4] Conway gave an alternate formulation of the existence problem, which we here reproduce:

Is there a graph with 99 vertices in which every edge ( \ie pair of joined vertices) belongs to a unique triangle and every nonedge (pair of unjoined vertices) to a unique quadrilateral?

Famously, A.A. Makhnev and I.M. Minakova proved in [9] that a strongly regular graph with parameters ( v, k, 1, 2) (v,k,1,2) can only exist if k = u 2 + u + 2 k=u^{2}+u+2 where u ∈ { 1, 3, 4, 10, 31 } u\in\{1,3,4,10,31\}. Such graphs are known to exist for u ∈ { 1, 4 } u\in\{1,4\} but not much is known about the remaining cases. Should a Conway 99-graph exist, it would correspond to the case u = 3 u=3.

The survey paper [10] by Makhnev neatly establishes a context for our work. Let G G be the automorphism group of a putative Conway 99-graph. In [9, Theorem 2.7] it is stated that the order of G G must divide 2 ⋅ 3 3 ⋅ 7 ⋅ 11 2\cdot 3^{3}\cdot 7\cdot 11. In [10, Corollary 2.4] Makhnev asserts the following:

If G G contains an involution t t, then one of the following holds:

1. (1)

If | G | |G| is divided by 7 then | G | |G| divides 42, [O ⁡ ( G), t] = 1 [O(G),t]=1, and in the case | G | = 42 |G|=42 the subgroup O ⁡ ( G) O(G) is non-Abelian,

2. (2)

| G | |G| divides 6.

In the present paper, we strengthen these results as follows:

1. ( 1 ′ 1^{\prime})

If | G | |G| is divisible by 7, then G G is isomorphic to ℤ 7 \mathbb{Z}_{7}.

2. ( 2 ′ 2^{\prime})

If 2 divides | G | |G|, then | G | |G| divides 6.

Our proof of ( 1 ′ 1^{\prime}) is performed in three stages, the first of which is to prove 14 cannot divide the order of G G. At the second stage, we show that divisibility by 7 implies G G is isomorphic to ℤ 7 \mathbb{Z}_{7} or F ​ r ​ o ​ b ​ ( 21) Frob(21). Here F ​ r ​ o ​ b ​ ( 21) Frob(21) denotes the Frobenius group of order 21, \ie the index 2 subgroup of the holomorph ℤ 7 ⋊ Aut ⁡ ( ℤ 7) ≅ F ​ r ​ o ​ b ​ ( 42) \mathbb{Z}_{7}\rtimes{\rm Aut}(\mathbb{Z}_{7})\cong Frob(42). The third stage is devoted to eliminating F ​ r ​ o ​ b ​ ( 21) Frob(21) as a possibility, and here we find it necessary to enlist the aid of a computer. It is worthy of note that stage 3 requires garnering as much structural information as possible in order to make a computer search feasible.

Our notation and terminology are standard. We refer the reader to [1, 3, 6, 11] as excellent sources of background material.

Our paper is organized as follows. In Section 2 we establish terminology and notation to be used throughout the paper. Especially relevant to later sections is a labeling scheme we provide for the vertices of a putative Conway 99-graph Γ \Gamma under the assumption that 7 divides | G | |G|. This scheme allows us to embed the automorphism group G G of Γ \Gamma into the symmetric group of degree 14.

In Section 3 we prove there are no order 14 automorphisms of Γ \Gamma. In Section 4 we complete the proof of ( 2 ′ 2^{\prime}) and show that divisibility by 7 implies G ≅ ℤ 7 G\cong\mathbb{Z}_{7} or F ​ r ​ o ​ b ​ ( 21) Frob(21). Orbit valencies are determined in the case when G ≅ F ​ r ​ o ​ b ​ ( 21) G\cong Frob(21).

In Section 5 we derive a fairly comprehensive structural framework for Γ \Gamma based on the assumption that G ≅ F ​ r ​ o ​ b ​ ( 21) G\cong Frob(21). This framework is crucial in reducing run-time, thereby making a computer search feasible. Results of this search show that G ≅ ℤ 7 G\cong\mathbb{Z}_{7} if 7 7 divides | G | |G|. Details of our program are provided in Section 6.

## 2. Preliminaries

Throughout this paper, Γ \Gamma will denote a putative Conway 99-graph, \ie a strongly regular graph with parameters ( 99, 14, 1, 2) (99,14,1,2). We denote its automorphism group by G G. Although Γ \Gamma is not vertex transitive, one can always “hang” the graph from any vertex x ∈ V ⁡ ( Γ) x\in V(\Gamma) whereby vertices are grouped together in accordance with their distance from x x. This is a property of distance-regular graphs in general and strongly regular graphs in particular. In such case, we refer to x x as the “root vertex”.

As is customary, we denote by Γ 1 ​ ( x) \Gamma_{1}\,(x) and Γ 2 ​ ( x) \Gamma_{2}\,(x) the set of neighbors and non-neighbors of x x respectively, commonly referred to as the first and second subconstituents of Γ \Gamma. When x x is understood from context, we will abbreviate these sets by Γ 1 \Gamma_{1} and Γ 2 \Gamma_{2}. In Figure 1 we depict the distance distribution diagram for Γ \Gamma. Note that the diagram indicates that | Γ 1 | = 14 |\Gamma_{1}|=14 and | Γ 2 | = 84 |\Gamma_{2}|=84.

For the moment we assume x ∈ V ⁡ ( Γ) x\in V(\Gamma) is an arbitrary vertex, however in due course our choice of x x will carry special significance. We label the 14 neighbors of x x by i ​ X {iX}, 1 ≤ i ≤ 7 1\leq i\leq 7, X ∈ { L, R } X\in\{L,R\}, see Figure 2. Since λ = 1 \lambda=1, we may assume without loss of generality that { i ​ L, i ​ R } \{iL,iR\} is an edge for every 1 ≤ i ≤ 7 1\leq i\leq 7.

1 14 14 1 12 1 84 2 12 Figure 1. Distance distribution diagram of Γ \Gamma x x 4 ​ L {4L} 4 ​ R {4R} 3 ​ R {3R} 5 ​ L {5L} 3 ​ L {3L} 5 ​ R {5R} 2 ​ R {2R} 6 ​ L {6L} 2 ​ L {2L} 6 ​ R {6R} 1 ​ R {1R} 7 ​ L {7L} 1 ​ L {1L} 7 ​ R {7R} Figure 2. A labeling scheme for V ⁡ ( Γ 1) V(\Gamma_{1})

Observe that for any X, Y ∈ { L, R } X,Y\in\{L,R\}, the vertices i ​ X, j ​ Y ∈ V ⁡ ( Γ 1) {iX},{jY}\in V(\Gamma_{1}) are nonadjacent if and only if i ≠ j i\neq j. As μ = 2 \mu=2, each pair of nonadjacent vertices i ​ X, j ​ Y ∈ V ⁡ ( Γ 1) {iX},{jY}\in V(\Gamma_{1}) must have a unique common neighbor in V ⁡ ( Γ 2) V(\Gamma_{2}). We label this common neighbor i ​ j ​ X ​ Y ijXY. As there are ( 14 2) − 7 = 84 \binom{14}{2}-7=84 pairs of nonadjacent vertices in V ⁡ ( Γ 1) V(\Gamma_{1}), we see that each of the 84 vertices in V ⁡ ( Γ 2) V(\Gamma_{2}) receives a unique label, again due to μ = 2 \mu=2.

{lemm}

Suppose g ∈ G g\in G fixes the subgraph Γ 1 + x \Gamma_{1}+x pointwise. Then g g fixes Γ 2 \Gamma_{2} pointwise, i.e, g g is the identity automorphism.

###### Proof.

Evident from our labeling scheme and the fact that μ = 2 \mu=2. ∎

{lemm}

Suppose there exists s ∈ G s\in G with | s | = 7 |s|=7. Then s s fixes a unique vertex in V ⁡ ( Γ) V(\Gamma), hence the ⟨ s ⟩ \langle s\rangle -orbit structure on Γ \Gamma is [1, 7 14] [1,7^{14}].

###### Proof.

As | V ( Γ) | = 99 ≡ ( mod 7) |V(\Gamma)|=99\equiv 1\!\pmod{7} we deduce that s s must have at least one fixed vertex which we may choose to fulfill the role of root vertex x x of Γ \Gamma. This establishes that both Γ 1 \Gamma_{1} and Γ 2 \Gamma_{2} are s s -invariant. In particular, the orbit structure of ⟨ s ⟩ \langle s\rangle on Γ 1 \Gamma_{1} is [7 2] [7^{2}], [1 7, 7] [1^{7},7], or [1 14] [1^{14}]. As i ​ L iL is a fixed point of s s if and only if i ​ R iR is, the number of fixed points must be even, \ie the ⟨ s ⟩ \langle s\rangle -orbit structure is either [7 2] [7^{2}] or [1 14] [1^{14}]. However, Lemma 2 rules out [1 14] [1^{14}], leaving [7 2] [7^{2}] as the orbit structure on Γ 1 \Gamma_{1}. Now suppose a vertex i ​ j ​ X ​ Y ∈ V ⁡ ( Γ 2) ijXY\in V(\Gamma_{2}) is fixed by s s. Then x x and i ​ j ​ X ​ Y ijXY have i ​ X, j ​ Y, i ​ X s, j ​ Y s {iX},{jY},{iX}^{s},{jY}^{s} as common neighbors. As i ≠ j i\neq j and μ = 2 \mu=2, it follows that { i ​ X, j ​ Y } = { i ​ X s, j ​ Y s } \{{iX},{jY}\}=\{{iX}^{s},{jY}^{s}\}. Since s s has no fixed points on Γ 1 \Gamma_{1}, this implies i ​ X s = j ​ Y {iX}^{s}={jY} and j ​ Y s = i ​ X {jY}^{s}=iX. But then each of i ​ X iX and j ​ Y jY is fixed by s 2 s^{2}, a contradiction. The result follows. ∎

{rema}

Note that one consequence of our labeling scheme, together with the assumption in Lemma 2, is that the automorphism group Aut ⁡ ( Γ) {\rm Aut}(\Gamma) embeds in Sym ⁡ ( V ⁡ ( Γ 1)) ≅ S 14 {\rm Sym}(V(\Gamma_{1}))\cong S_{14}. However, among all order 7 7 elements in Sym ⁡ ( V ⁡ ( Γ 1)) {\rm Sym}(V(\Gamma_{1})), the only ones that are graph automorphisms of Γ 1 \Gamma_{1} are powers of ( 1 ​ L, 2 ​ L, …, 7 ​ L) ​ ( 1 ​ R, 2 ​ R, …, 7 ​ R) (1L,2L,\dots,7L)\,(1R,2R,\dots,7R). Henceforth we denote s L = ( 1 ​ L, 2 ​ L, …, 7 ​ L) s_{L}=(1L,2L,\dots,7L), s R = ( 1 ​ R, 2 ​ R, …, 7 ​ R) s_{R}=(1R,2R,\dots,7R) and s = s L ​ s R s=s_{L}s_{R}. The two ⟨ s ⟩ \langle s\rangle -orbits on Γ 1 \Gamma_{1} are now transparent. They are { 1 ​ L, 2 ​ L, …, 7 ​ L } \{1L,2L,\dots,7L\} and { 1 ​ R, 2 ​ R, …, 7 ​ R } \{1R,2R,\dots,7R\}.

{lemm}

Every vertex of Γ 2 \,\Gamma_{2} lies on five 3 3 -cycles wholly inside Γ 2 \Gamma_{2}. Thus there are 140 140 3 3 -cycles in Γ 2 \Gamma_{2}.

###### Proof.

Clearly, every vertex in Γ \Gamma lies on seven 3 3 -cycles. Given a vertex v ∈ V ⁡ ( Γ 2) v\in V(\Gamma_{2}) it has precisely two Γ 1 \Gamma_{1} -neighbors u u and w w. As λ = 1 \lambda=1, each of v ​ u vu and v ​ w vw must be an edge in a unique 3-cycle. Moreover, these two 3-cycles cannot coincide. Indeed, this would require that u u and w w be adjacent, whence u ​ w ​ x uwx would be a second 3-cycle on the edge u ​ w uw where x x is the root vertex. This proves the remaining five 3 3 -cycles on v v lie entirely inside Γ 2 \Gamma_{2}. But now we have that the total number of 3 3 -cycles in Γ 2 \Gamma_{2} is 84 ⋅ 5 3 = 140 \frac{84\cdot 5}{3}=140 as claimed. ∎

## 3. Nonexistence of an order 14 automorphism

Our goal in this section is to prove G G does not contain any element of order 14. This will be a crucial step in our argument that divisibility by 2 implies | G | |G| divides 6 6.

Lemmas 3 and 3 set the groundwork for the rest of this section.

{lemm}

Suppose G G contains a cyclic subgroup K K of order 14 14. Then K = ⟨ s ​ t ⟩ K=\langle st\rangle where s = ( 1 ​ L, 2 ​ L, …, 7 ​ L) ​ ( 1 ​ R, 2 ​ R, …, 7 ​ R) s=(1L,2L,\dots,7L)\,(1R,2R,\dots,7R) and t = ( 1 ​ L, 1 ​ R) ​ ( 2 ​ L, 2 ​ R) ​ … ​ ( 7 ​ L, 7 ​ R) t=(1L,1R)\,(2L,2R)\,\dots\,(7L,7R).

###### Proof.

Let C S ​ ( s) = ( ⟨ s L ⟩ × ⟨ s R ⟩) ⋊ ⟨ t ⟩ C_{S}(s)=(\langle s_{L}\rangle\times\langle s_{R}\rangle)\rtimes\langle t\rangle denote the centralizer of s s in S = Sym ⁡ ( V ⁡ ( Γ 1)) S={\rm Sym}(V(\Gamma_{1})). There are seven involutions in C S ​ ( s) C_{S}(s) which take the form

 | t s R i = ( 1 ​ L, ( 1 + i) ​ R) ​ ( 2 ​ L, ( 2 + i) ​ R) ​ … ​ ( 7 ​ L, i ​ R) t^{\,s_{R}^{\,i}}=(1L,(1+i)R)\,(2L,(2+i)R)\dots(7L,iR) |  |

for 0 ≤ i ≤ 6 0\leq i\leq 6, and in each case ⟨ s ​ t s R i ⟩ \langle st^{\,s_{R}^{i}}\rangle is a cyclic subgroup of C S ​ ( s) C_{S}(s) of order 14. However, since t s R i t^{\,s_{R}^{\,i}} maps 1 ​ L 1L to ( 1 + i) ​ R (1+i)R and 1 ​ R 1R to ( 1 − i) ​ L (1-i)L, adjacency is preserved only if i = 0 i=0. Thus t t is the unique involution in Aut ⁡ ( Γ 1) {\rm Aut}(\Gamma_{1}) whereby K = ⟨ s ​ t ⟩ K=\langle st\rangle is the unique cyclic subgroup of order 14 in Aut ⁡ ( Γ 1) {\rm Aut}(\Gamma_{1}). ∎

{lemm}

K = ⟨ s ​ t ⟩ K=\langle st\rangle fixes the root vertex x x of Γ \,\Gamma but has no other fixed points. Thus each of the remaining seven K K -orbits on Γ \,\Gamma has size 14 14.

###### Proof.

Recall from Lemma 2 that x x is the unique vertex fixed by s ∈ K s\in K. As t t commutes with s s we have that x t x^{t} is fixed by s s, whence x t = x x^{t}=x. Thus x x is the unique vertex fixed by K K.

We now consider K K -orbits on Γ − x \Gamma-x. Clearly, K K fuses the two ⟨ s ⟩ \langle s\rangle -orbits in Γ 1 \Gamma_{1} so we are left to consider the orbit structure of K K on Γ 2 \Gamma_{2}. Since every ⟨ s ⟩ \langle s\rangle -orbit on Γ 2 \Gamma_{2} has size 7, the only possible size of a K K -orbit on Γ 2 \Gamma_{2} is 7 or 14. However, t t cannot fix any vertex i ​ j ​ X ​ Y ∈ V ⁡ ( Γ 2) ijXY\in V(\Gamma_{2}) where X, Y ∈ { L, R } X,Y\in\{L,R\}. Indeed, this would imply i ​ j ​ X ​ Y = ( i ​ j ​ X ​ Y) t = i ​ j ​ X C ​ Y C ijXY=(ijXY)^{t}=ijX^{C}Y^{C} where { L, R } = { X, X C } = { Y, Y C } \{L,R\}=\{X,X^{C}\}=\{Y,Y^{C}\}. If X ≠ Y X\neq Y, then i = j i=j which violates λ = 1 \lambda=1. Otherwise X = Y X=Y, which implies i ​ j ​ X ​ X = ( i ​ j ​ X ​ X) t = i ​ j ​ X C ​ X C ijXX=(ijXX)^{t}=ijX^{C}X^{C}, a contradiction since X ≠ X C X\neq X^{C}. ∎

{rema}

It is easy to see that a set of orbit representatives in the action of K K on Γ 2 \Gamma_{2} is given by { 12 ​ L ​ L, 13 ​ L ​ L, 14 ​ L ​ L, 12 ​ L ​ R, 13 ​ L ​ R, 14 ​ L ​ R } \{12LL,\,13LL,\,14LL,\,12LR,\,13LR,\,14LR\}. Moreover, each numerical coordinate i i occurs exactly four times in each orbit. For example, in the orbit with representative 12 ​ L ​ L 12LL, the coordinate 3 3 occurs in each of 23 ​ L ​ L 23LL, 34 ​ L ​ L 34LL, 23 ​ R ​ R 23RR, 34 ​ R ​ R 34RR. However, these four vertices are distributed evenly into pairs in the sense that 23 ​ L ​ L 23LL, 34 ​ L ​ L 34LL are neighbors of 3 ​ L 3L while 23 ​ R ​ R 23RR, 34 ​ R ​ R 34RR are neighbors of 3 ​ R 3R.

Consider the equitable partition π \pi induced by the K K -orbits 𝒪 1, 𝒪 2, …, 𝒪 6 \mathcal{O}_{1},\mathcal{O}_{2},\dots,\mathcal{O}_{6} on Γ 2 \Gamma_{2}. As is customary, we shall refer to π \pi as an *orbit partition*. We denote by b i ​ j b_{ij} the number of 𝒪 j \mathcal{O}_{j} -neighbors of any fixed vertex in 𝒪 i \mathcal{O}_{i}. When i = j i=j we simply write b i b_{i} and refer to it as the *internal valency*of the orbit 𝒪 i \mathcal{O}_{i}. We shall also call the b i ​ j b_{ij}*orbit valencies*(or simply *valencies*) due to what occurs naturally in the quotient graph Γ 2 / π \Gamma_{2}/\pi. Pictorially, b i ​ j b_{ij} appears as a label of an arc from 𝒪 i \mathcal{O}_{i} to O j O_{j}, however in our case this arc is an edge ( \ie b i ​ j = b j ​ i b_{ij}=b_{ji} for all i, j i,j) since all orbits 𝒪 i \mathcal{O}_{i} have the same size.

b 3 b_{3} b 4 b_{4} b 5 b_{5} b 6 b_{6} b 1 b_{1} b 12 b_{12} b 14 b_{14} b 13 b_{13} b 15 b_{15} b 16 b_{16} b 2 b_{2} b 24 b_{24} b 23 b_{23} b 25 b_{25} b 26 b_{26} b 34 b_{34} b 56 b_{56} b 45 b_{45} b 36 b_{36} b 35 b_{35} b 46 b_{46} 𝒪 1 \mathcal{O}_{1} 𝒪 2 \mathcal{O}_{2} 𝒪 3 \mathcal{O}_{3} 𝒪 4 \mathcal{O}_{4} 𝒪 5 \mathcal{O}_{5} 𝒪 6 \mathcal{O}_{6}

Figure 3. A general K K -orbit partition on Γ 2 \Gamma_{2} where K = ⟨ s ​ t ⟩ ≅ ℤ 14 K=\langle st\rangle\cong\mathbb{Z}_{14}

At present we have that s ​ t st is an order 14 automorphism of the subgraph Γ 1 + x \Gamma_{1}+x. We wish to show s ​ t st cannot extend to an automorphism of Γ \Gamma. Our first step toward this objective is to count in two ways the cardinality of the set

 | S = { u ​ v ​ w: u ​ v ​ w is a 2-path with ​ w ∈ 𝒪 i }, S=\{uvw:\text{$uvw$ is a 2-path with }w\in\mathcal{O}_{i}\}, |  |

where u u is a fixed vertex in 𝒪 i \mathcal{O}_{i} (see Figure 3).

For each of the b i b_{i} neighbors of u u in 𝒪 i \mathcal{O}_{i} there is a unique 2 2 -path from u u to w w (since λ = 1 \lambda=1). Similarly, for each of the 13 − b i 13-b_{i} non-neighbors of u u in 𝒪 i \mathcal{O}_{i} there are two 2-paths from u u to w w (since μ = 2 \mu=2). Thus | S | = b i ⋅ 1 + ( 13 − b i) ⋅ 2 = 26 − b i |S|=b_{i}\cdot 1+(13-b_{i})\cdot 2=26-b_{i}.

On the other hand, we may condition our count on the location of the intermediate vertex v v. For v v in 𝒪 j \mathcal{O}_{j} there are b i ​ j ​ ( b i ​ j − 1) b_{ij}\,(b_{ij}-1) such 2-paths. (Here and hereafter, we shall identify b i ​ i b_{ii} with b i b_{i} for notational convenience.) In addition, u u has exactly two neighbors in Γ 1 \Gamma_{1} each of which has a unique neighbor w ∈ 𝒪 i ∖ { u } w\in\mathcal{O}_{i}\setminus\{u\} ( \cf Remark 3). This gives | S | = ∑ j = 1 6 b i ​ j ​ ( b i ​ j − 1) + 2 |S|=\sum_{j=1}^{6}b_{ij}\,(b_{ij}-1)+2. Equating these two expressions for | S | |S|, we obtain 26 − b i = ∑ j = 1 6 b i ​ j ​ ( b i ​ j − 1) + 2 26-b_{i}=\sum_{j=1}^{6}b_{ij}\,(b_{ij}-1)+2. But due to the fact that ∑ i = 1 6 b i ​ j = 12 \sum_{i=1}^{6}b_{ij}=12, this simplifies to

(1) |  | 36 − ( b i 2 + b i) = ∑ j = 2 6 b i ​ j 2 36-\big(b_{i}^{\,2}+b_{i}\big)=\sum_{j=2}^{6}b_{ij}^{\,2} |  |

We divide our analysis into cases based on an assumed value for b i b_{i}. Once a choice of b i b_{i} is made, we find all ways of expressing 36 − ( b i 2 + b i) 36-\big(b_{i}^{\,2}+b_{i}\big) as a sum of five squares while maintaining the valency requirement ∑ i = 1 6 b i ​ j = 12 \sum_{i=1}^{6}b_{ij}=12. Note that b i ≤ 5 b_{i}\leq 5 since otherwise the value of 36 − ( b i 2 + b i) 36-\big(b_{i}^{\,2}+b_{i}\big) would be negative.

All solution sets are provided in the lemma below. Verification of the list is straightforward, so is left to the reader. Note that each solution set is expressed as an ordered pair of the form

 | ( b i, { a 2, a 3, a 4, a 5, a 6 }). \big(b_{i},\big\{a_{2},a_{3},a_{4},a_{5},a_{6}\big\}\big). |  |

This is because unlike the internal valency b i b_{i} which remains fixed, the values a 2, a 3, …, a 6 a_{2},a_{3},\dots,a_{6} may be assigned to the valencies b i ​ j b_{ij}, j ≠ i j\neq i, in any specified manner. Thus, there are multiple solutions corresponding to each solution set achieved by suitably permuting the members of the multiset { a 2, a 3, a 4, a 5, a 6 } \big\{a_{2},a_{3},a_{4},a_{5},a_{6}\big\}. Below, we list these members in decreasing order.

{lemm}

For b i ∈ { 1, 3, 5 } b_{i}\in\{1,3,5\} there are no solutions to formula (1). For other values of b i \,b_{i} the solutions are listed as follows:

1. (a)

( 0, { 4, 3, 3, 1, 1 }) \big(0,\big\{4,3,3,1,1\big\}\big) and ( 0, { 3, 3, 3, 3, 0 }) \big(0,\big\{3,3,3,3,0\big\}\big) when b i = 0 b_{i}=0.

2. (b)

( 2, { 4, 3, 2, 1, 0 }) \big(2,\big\{4,3,2,1,0\big\}\big) when b i = 2 b_{i}=2,

3. (c)

( 4, { 3, 2, 1, 1, 1 }) \big(4,\big\{3,2,1,1,1\big\}\big) and ( 4, { 2, 2, 2, 2, 0 }) \big(4,\big\{2,2,2,2,0\big\}\big) when b i = 4 b_{i}=4.

For future reference, it is convenient to designate these solution sets by type, e.g.

 | I. ( 0, { 4, 3, 3, 1, 1 }), II. ( 0, { 3, 3, 3, 3, 0 }), III. ( 2, { 4, 3, 2, 1, 0 }) {\rm I}.\;\big(0,\big\{4,3,3,1,1\big\}\big),\;\;{\rm II}.\;\big(0,\big\{3,3,3,3,0\big\}\big),\;\;{\rm III}.\;\big(2,\big\{4,3,2,1,0\big\}\big) |  |

 | IV. ( 4, { 3, 2, 1, 1, 1 }), V. ( 4, { 2, 2, 2, 2, 0 }) {\rm IV}.\;\big(4,\big\{3,2,1,1,1\big\}\big),\;\;{\rm V}.\;\big(4,\big\{2,2,2,2,0\big\}\big) |  |

We also extend this terminology to orbits, saying an orbit is *of type*T \rm T if its set of valencies correspond to a solution set of type T {\rm T}, T ∈ { I, II, III, IV, V } {\rm T}\in\{{\rm I,II,III,IV,V}\}.

We next count in two ways the number of 2 2 -paths starting from a fixed vertex u u in 𝒪 i \mathcal{O}_{i} and ending at some vertex w w in 𝒪 j \mathcal{O}_{j}, j ≠ i j\neq i. Here u u has exactly b i ​ j b_{ij} neighbors in 𝒪 j \mathcal{O}_{j}, and as λ = 1 \lambda=1 there exists a unique 2 2 -path starting at u u and ending at w w for each neighbor w w of u u in 𝒪 j \mathcal{O}_{j}. Similarly, u u has 14 − b i ​ j 14-b_{ij} non-neighbors in 𝒪 j \mathcal{O}_{j}, and as μ = 2 \mu=2 there are exactly two 2 2 -paths starting at u u and ending at each non-neighbor w w of u u in 𝒪 j \mathcal{O}_{j}. Thus in total there are b i ​ j ⋅ 1 + ( 14 − b i ​ j) ⋅ 2 = 28 − b i ​ j b_{ij}\cdot 1+(14-b_{ij})\cdot 2=28-b_{ij} such 2 2 -paths from u u into 𝒪 j \mathcal{O}_{j} when j ≠ i j\neq i.

For the second count, we focus on the location of an intermediate vertex v v in each such 2-path. Here v v can occur in any of the six K K -orbits on Γ 2 \Gamma_{2} as well as in Γ 1 \Gamma_{1}. In the case of K K -orbits on Γ 2 \Gamma_{2}, there are b i ​ k b_{ik} choices for v v in 𝒪 k \mathcal{O}_{k}, and for each such v v there are b k ​ j b_{kj} choices for w w in 𝒪 j \mathcal{O}_{j}. This gives b i ​ k ​ b k ​ j b_{ik}b_{kj} 2-paths of desired type. In addition, there are two choices for v v in Γ 1 \Gamma_{1} each of which has two neighbors w w in 𝒪 j \mathcal{O}_{j}. This produces four more 2-paths. Thus, in total there are precisely ∑ k = 1 6 b i ​ k ​ b k ​ j + 4 \sum_{k=1}^{6}b_{ik}b_{kj}+4 paths of the type in question when j ≠ i j\neq i.

Equating these two counts yields 28 − b i ​ j = ∑ k = 1 6 b i ​ k ​ b k ​ j + 4 28-b_{ij}=\sum_{k=1}^{6}b_{ik}b_{kj}+4, or equivalently

(2) |  | 24 − b i ​ j = ∑ k = 1 6 b i ​ k ​ b k ​ j. 24-b_{ij}=\sum_{k=1}^{6}b_{ik}b_{kj}. |  |

{lemm}

In a K K -orbit partition of Γ 2 \,\Gamma_{2} ( \cf Figure 3) we have the following:

1. (a)

The number of orbits of type I is at most 2 2.

2. (b)

The number of orbits of type II is at most 1 1.

3. (c)

The number of orbits of type III is at most 4 4.

4. (d)

The number of orbits of type IV is at most 4 4.

5. (e)

The number of orbits of type V is at most 1 1.

###### Proof.

(a) Suppose there exist two orbits 𝒪 i \mathcal{O}_{i} and 𝒪 j \mathcal{O}_{j} of type I. Then since b i = b j = 0 b_{i}=b_{j}=0, formula (2) reduces to 24 − b i ​ j = ∑ k ≠ i, j b i ​ k ​ b k ​ j 24-b_{ij}=\sum_{k\neq i,j}b_{ik}b_{kj}. Note that this formula is satisfied only if b i ​ j = 4 b_{ij}=4, which results in the solution 20 = 3 2 + 3 2 + 1 2 + 1 2 20=3^{2}+3^{2}+1^{2}+1^{2}. As an orbit of type I admits only one edge of valency 4, there cannot be a third orbit of this type.
(b) Let 𝒪 i \mathcal{O}_{i} and 𝒪 j \mathcal{O}_{j} be two orbits of type II. Since b i = b j = 0 b_{i}=b_{j}=0, formula (2) again reduces to 24 − b i ​ j = ∑ k ≠ i, j b i ​ k ​ b k ​ j 24-b_{ij}=\sum_{k\neq i,j}b_{ik}b_{kj}. But regardless of how one chooses b i ​ j ∈ { 0, 3 } b_{ij}\in\{0,3\} and reorders the corresponding multiset, this formula is never satisfied. Thus there is at most one orbit of type II.
(c) Let 𝒪 i \mathcal{O}_{i} and 𝒪 j \mathcal{O}_{j} be two orbits of type III. Since b i = b j = 2 b_{i}=b_{j}=2, formula (2) becomes 24 − 5 ​ b i ​ j = ∑ k ≠ i, j b i ​ k ​ b k ​ j 24-5b_{ij}=\sum_{k\neq i,j}b_{ik}b_{kj}. In this case one has b i ​ j ∈ { 0, 1, 2, 3, 4 } b_{ij}\in\{0,1,2,3,4\}, however there are no solutions if b i ​ j ∈ { 1, 2 } b_{ij}\in\{1,2\}. In contrast, every remaining choice of b i ​ j b_{ij} works. Specifically, if b i ​ j = 0 b_{ij}=0 one gets 24 = 4 ⋅ 1 + 3 ⋅ 4 + 2 ⋅ 3 + 1 ⋅ 2 24=4\cdot 1+3\cdot 4+2\cdot 3+1\cdot 2 as a solution. For b i ​ j = 3 b_{ij}=3 one gets 9 = 4 ⋅ 0 + 2 ⋅ 4 + 1 ⋅ 1 + 0 ⋅ 2 9=4\cdot 0+2\cdot 4+1\cdot 1+0\cdot 2, while for b i ​ j = 4 b_{ij}=4 one gets 4 = 3 ⋅ 0 + 2 ⋅ 1 + 1 ⋅ 2 + 0 ⋅ 3 4=3\cdot 0+2\cdot 1+1\cdot 2+0\cdot 3. Having only three allowable valencies for edges between pairs of type III orbits, it is not possible to have a fifth orbit of this type.
(d) Given any two orbits 𝒪 i \mathcal{O}_{i} and 𝒪 j \mathcal{O}_{j} of type IV, we have that b i ​ j ∈ { 1, 2, 3 } b_{ij}\in\{1,2,3\}. As b 1 = b 2 = 4 b_{1}=b_{2}=4, formula (2) becomes 24 − 9 ​ b i ​ j = ∑ k ≠ i, j b i ​ k ​ b k ​ j 24-9b_{ij}=\sum_{k\neq i,j}b_{ik}b_{kj}. Clearly b i ​ j = 1 b_{ij}=1 leads to a solution, namely 15 = 1 2 + 1 2 + 2 2 + 3 2 15=1^{2}+1^{2}+2^{2}+3^{2}, but other choices of b i ​ j b_{ij} fail. Since a type IV orbit has only three edges of valency 1, there can be at most four orbits of this type.
(e) Suppose there are two orbits 𝒪 i \mathcal{O}_{i} and 𝒪 j \mathcal{O}_{j} of type V. Then since b i = b j = 4 b_{i}=b_{j}=4, formula (2) becomes 24 − 9 ​ b i ​ j = ∑ k ≠ i, j b i ​ k ​ b k ​ j 24-9b_{ij}=\sum_{k\neq i,j}b_{ik}b_{kj}. Here b i ​ j ∈ { 0, 2 } b_{ij}\in\{0,2\}, but it is immediate that neither choice leads to a solution. This proves there is at most one orbit of type V. ∎

In the above, we applied formula (2) to bound orbits of identical type in a K K -orbit partition of Γ 2 \Gamma_{2}. We now do the same for orbits of mixed type. Note that we do not strive to obtain sharp bounds at this stage. Our goal is simply to eliminate several possibilities in an expedient manner.

{lemm}

Let T i, T j ∈ { I, II, III, IV, V } \rm T_{i}\,,T_{j}\in\{I,II,III,IV,V\}. Then the ( T i, T j) \rm(T_{i}\,,T_{j}) -entry in Table 1 bounds from above the number of orbits of type T j \rm T_{j} that can coexist with a fixed orbit of type T i \rm T_{i} in a K K -orbit partition of Γ 2 \,\Gamma_{2}.

###### Proof.

Note that the diagonal entries in Table 1 were previously confirmed in Lemma 3. Moreover, one need not check any entry ( T i, T j) \rm(T_{i}\,,T_{j}) that is equal to the diagonal entry ( T j, T j) \rm(T_{j}\,,T_{j}) since the latter is the maximum allowable number of orbits of type T j \rm T_{j} in any K K -orbit partition of Γ 2 \Gamma_{2}.

 | I | II | III | IV | V |

I | 2 | 0 | 4 | 0 | 0 |

II | 0 | 1 | 4 | 4 | 1 |

III | 2 | 1 | 4 | 2 | 1 |

IV | 0 | 1 | 4 | 4 | 1 |

V | 0 | 1 | 4 | 4 | 1 |

Table 1. Bounds on the number of orbits of mixed type

Case 1. ( I, II) = ( II, I) = 0 \rm(I,\,II)=(II,\,I)=0: Clearly, the only option for the shared edge is b i ​ j = 3 b_{ij}=3. As b i = b j = 0 b_{i}=b_{j}=0, formula (2) reduces to 21 = ∑ k ≠ i, j b i ​ k ​ b k ​ j 21=\sum_{k\neq i,j}b_{ik}b_{kj} where b i ​ k ∈ { 4, 3, 1, 1 } b_{ik}\in\{4,3,1,1\} and b k ​ j ∈ { 3, 3, 3, 0 } b_{kj}\in\{3,3,3,0\}. It is easy to see that no permutation of multisets leads to a solution, \ie ( I, II) = 0 \rm(I,\,II)=0. (For ( II, I) = 0 \rm(II,\,I)=0, the only change to the above is b i ​ k ∈ { 3, 3, 3, 0 } b_{ik}\in\{3,3,3,0\} and b k ​ j ∈ { 4, 3, 1, 1 } b_{kj}\in\{4,3,1,1\}.)
Case 2. ( I, IV) = ( IV, I) = 0 \rm(I,\,IV)=(IV,\,I)=0: In this case b i = 0 b_{i}=0 and b j = 4 b_{j}=4, so formula (2) reduces to 21 − 5 ​ b i ​ j = ∑ k ≠ i, j b i ​ k ​ b k ​ j 21-5b_{ij}=\sum_{k\neq i,j}b_{ik}b_{kj}. Here there are two options for b i, j b_{i,j}. If b i, j = 1 b_{i,j}=1 then we get 16 = ∑ k ≠ i, j b i ​ k ​ b k ​ j 16=\sum_{k\neq i,j}b_{ik}b_{kj} where b i ​ k ∈ { 4, 3, 3, 1 } b_{ik}\in\{4,3,3,1\} and b k ​ j ∈ { 3, 2, 1, 1 } b_{kj}\in\{3,2,1,1\}, and no permutation of multisets leads to a solution. For the second option b i ​ j = 3 b_{ij}=3, we get 6 = ∑ k ≠ i, j b i ​ k ​ b k ​ j 6=\sum_{k\neq i,j}b_{ik}b_{kj} where b i ​ k ∈ { 4, 3, 1, 1 } b_{ik}\in\{4,3,1,1\} and b k ​ j ∈ { 2, 1, 1, 1 } b_{kj}\in\{2,1,1,1\}. Again no permutation of multisets gives a solution. Thus ( I, IV) = ( IV, I) = 0 \rm(I,\,IV)=(IV,I)=0.
Case 3. ( I, V) = ( V, I) = 0 \rm(I,\,V)=(V,\,I)=0: Here the multisets { 4, 3, 3, 1, 1 } \{4,3,3,1,1\} and { 2, 2, 2, 2, 0 } \{2,2,2,2,0\} are disjoint, so there is no possible choice of valency for the edge between two orbits of these respective types. The result follows at once.
Case 4. ( III, IV) = 2 \rm(III,\,IV)=2: In this case, b i = 2 b_{i}=2 and b j = 4 b_{j}=4 so formula (2) becomes 24 − 7 ​ b i ​ j = ∑ k ≠ i, j b i ​ k ​ b k ​ j 24-7b_{ij}=\sum_{k\neq i,j}b_{ik}b_{kj}. There are three choices for b i ​ j b_{ij}, namely b i ​ j ∈ { 3, 2, 1 } b_{ij}\in\{3,2,1\}. If b i ​ j = 3 b_{ij}=3 the formula reduces to 3 = ∑ k ≠ i, j b i ​ k ​ b k ​ j 3=\sum_{k\neq i,j}b_{ik}b_{kj} where b i ​ k ∈ { 4, 2, 1, 0 } b_{ik}\in\{4,2,1,0\} and b k ​ j ∈ { 2, 1, 1, 1 } b_{kj}\in\{2,1,1,1\}, and it is immediate that there is no solution. If b i ​ j = 2 b_{ij}=2 we obtain 10 = ∑ k ≠ i, j b i ​ k ​ b k ​ j 10=\sum_{k\neq i,j}b_{ik}b_{kj} where b i ​ k ∈ { 4, 3, 1, 0 } b_{ik}\in\{4,3,1,0\} and b k ​ j ∈ { 3, 1, 1, 1 } b_{kj}\in\{3,1,1,1\}. Here there is a unique solution, namely 10 = 4 ⋅ 1 + 3 ⋅ 1 + 1 ⋅ 3 + 0 ⋅ 1 10=4\cdot 1+3\cdot 1+1\cdot 3+0\cdot 1. Finally, if b i ​ j = 1 b_{ij}=1 we obtain 17 = ∑ k ≠ i, j b i ​ k ​ b k ​ j 17=\sum_{k\neq i,j}b_{ik}b_{kj} where b i ​ k ∈ { 4, 3, 2, 0 } b_{ik}\in\{4,3,2,0\} and b k ​ j ∈ { 3, 2, 1, 1 } b_{kj}\in\{3,2,1,1\}. In this case there are three solutions, namely 17 = 4 ⋅ 3 + 3 ⋅ 1 + 2 ⋅ 1 + 0 ⋅ 2 = 4 ⋅ 1 + 3 ⋅ 3 + 2 ⋅ 2 + 0 ⋅ 1 = 4 ⋅ 2 + 3 ⋅ 1 + 2 ⋅ 3 + 0 ⋅ 1 17=4\cdot 3+3\cdot 1+2\cdot 1+0\cdot 2=4\cdot 1+3\cdot 3+2\cdot 2+0\cdot 1=4\cdot 2+3\cdot 1+2\cdot 3+0\cdot 1. In any case, there are just two possibilities for the valency of an edge from a fixed type III orbit to an orbit of type IV. We conclude that ( III, IV) = 2 \rm(III,\,IV)=2.
As all cases in the lemma statement have been treated, the proof is complete. ∎

The reader will note that the relation in Lemma 3 is not generally symmetric.

Let us write [I a, II b, III c, IV d, V e] \rm[I^{a},II^{\,b},III^{\,c},IV^{\,d},V^{\,e}] to indicate a K K -orbit partition of Γ 2 \Gamma_{2} having a a orbits of type I, b b orbits of type II, and so on. (If an orbit of specific type does not occur in the partition, we simply omit that type from the above partition notation.)

{lemm}

There is no K K -orbit partition of the form [III c, IV 6 − c] \rm[III^{\,c},IV^{\,6-c}] for any c c.

###### Proof.

By Lemma 3, one has 2 ≤ c ≤ 4 2\leq c\leq 4. As a type III orbit has a single edge of valency 4 and a type IV orbit has none, there are c / 2 c/2 edges of valency 4 in the partition. This means c c must be even. However, c = 2 c=2 is prohibited. Indeed, by Lemma 3 the existence of a type III orbit requires that there be at most two type IV orbits, hence 6 − c ≤ 2 6-c\leq 2.

We come now to the only remaining case which is c = 4 c=4. As shown in the proof of Lemma 3, each pair of type III orbits must share an edge of valency 0, 3 or 4. But as there are four type III orbits, every such valency gets used. On the other hand, we showed in Lemma 3 that two orbits of type IV must share an edge of valency 1. This leaves a type IV orbit with an unusable edge of valency 3, again a contradiction. ∎

One conclusion of Lemma 3 is that a viable K K -orbit partition of Γ 2 \Gamma_{2} must contain an orbit of type I, II or V. By way of the next two lemmas, we are able to narrow this down considerably.

{lemm}

There is no K K -orbit partition that contains an orbit of type I.

###### Proof.

By Lemma 3, the only possible orbit partition containing a type I orbit is [I 2, III 4] \rm[I^{2},III^{4}]. However, we have seen that no pair of type III orbits can share an edge of valency 2 ( \cf proof of Lemma 3 (c)), while type I orbits have no edges of that valency. This implies orbits of type III have unusable edges of valency 2 from which the result follows. ∎

{lemm}

A K K -orbit partition of Γ 2 \,\Gamma_{2} must be of the form [II, IV 4, V] \rm[II,IV^{4},V].

###### Proof.

By Lemmas 3 and 3, a K K -orbit partition must contain at least one orbit of type II or V. Suppose there exists a type II orbit in the partition. Then by Lemma 3 there cannot be a second orbit of type II, nor can there be more than one orbit of type V. Thus the partition is of the form [II, III c, IV d, V e] \rm[II,III^{c},IV^{d},V^{e}] where c + d + e = 5 c+d+e=5 and 0 ≤ e ≤ 1 0\leq e\leq 1. Also, as in the proof of Lemma 3, c c must be even.

Suppose first that c = 2 c=2. Then by Lemma 3 we have d ≤ 2 d\leq 2, whence the partition must be of the form [II, III 2, IV 2, V] \rm[II,III^{2},IV^{2},V]. In the proof of Lemma 3 (d), we saw that an edge shared by an orbit of type III and one of type IV must have valency 1 or 2. As type III orbits have only one edge of each such valency and there are two type IV orbits, both edges must be shared with a type IV orbit. But type III orbits have only one edge of valency 2, hence these edges are now used up. This is a contradiction because type V orbits have four edges of valency 2.

For c = 4 c=4, the argument is similar. An edge shared by two type III orbits must have valency 0, 3 0,3 or 4. As there are four type III orbits in this case, every such edge is used between orbits of this type. In particular, the single edge of valency 3 is no longer available. But a type II orbit has four edges of valency 3, so we again reach a contradiction. This proves c = 0 c=0 when a type II orbit is in the partition.

It only remains to see what occurs if we first assume the partition contains a type V orbit. But in this case the four valency 2 edges of this orbit are shared by four other orbits, be they of type III or IV. This means there must be an orbit of type II in the partition, a case we have already treated. We conclude that [II, IV 4, V] \rm[II,IV^{4},V] is the only possible form of a K K -orbit partition of Γ 2 \Gamma_{2} as claimed. ∎

We depict the orbit partition of type [II, IV 4, V] \rm[II,IV^{4},V] in Figure 4. It too will be shown to not exist in due course.

4 4 0 4 4 1 1 1 3 2 4 1 1 3 2 1 0 3 2 3 2 IV IV IV IV II V

Figure 4. The lone surviving K K -orbit partition of Γ 2 \Gamma_{2} ( \cf Lemma 3)

{lemm}

Neither a type IV orbit nor a type V orbit can contain a 3 3 -cycle.

###### Proof.

First observe that type IV and type V orbits have internal valency 4. In any orbit of either type we may fix a vertex v v and denote its neighbors by v p, v r, v s, v t v^{p},v^{r},v^{s},v^{t} where p, r, s, t ∈ K p,r,s,t\in K. However v p − 1, v r − 1, v s − 1, v t − 1 v^{\,p^{-1}},v^{\,r^{-1}},v^{\,s^{-1}},v^{\,t^{-1}} must also be neighbors of v v. This means, with one exception, the automorphisms p, r, s, t p,r,s,t must come in pairs. The one exception is if two or four of p, r, s, t p,r,s,t are involutory. However, this cannot be the case since K K contains a unique involution. Therefore, without loss of generality we may assume r = p − 1 r=p^{-1} and t = s − 1 t=s^{-1}. Moreover, we know that | r |, | t | ∈ { 7, 14 } |r|,|t|\in\{7,14\}. Three broad cases can arise here, namely | r | = | t | = 7 |r|=|t|=7, | r | = | t | = 14 |r|=|t|=14 and | r | = 7, | t | = 14 |r|=7,\,|t|=14.

Case 1. | r | = | t | = 7 |r|=|t|=7: In this case the orbit is comprised of two connected components but that won’t affect our argument. Since K K contains a unique subgroup of order 7, we must have r = t m r=t^{\,m} for some integer m ∈ { 2, 3 } m\in\{2,3\}. However, both subcases violate λ = 1 \lambda=1 as depicted in Figure 5. Specifically, if r = t 2 r=t^{2} then the edge v t ​ v t 2 v^{t}v^{\,t^{\,2}} lies on two 3-cycles, while if r = t 3 r=t^{3} the edge v ​ v t 4 vv^{\,t^{\,4}} suffers the same fate. (Note that the subcases m = 4, 5 m=4,5 are identical to m = 3, 2 m=3,2 respectively.)

Case 2. | r | = | t | = 14 |r|=|t|=14: Here we have r = t m r=t^{\,m} where m ∈ { 3, 5 } m\in\{3,5\}. Both subcases violate μ = 2 \mu=2 as indicated in Figure 6. Specifically, If r = t 3 r=t^{\,3} then vertices v t 3 v^{\,t^{\,3}}, v t 5 v^{\,t^{\,5}} have v t 2, v t 4, v t 6 v^{\,t^{\,2}},v^{\,t^{\,4}},v^{\,t^{\,6}} as common neighbors while if r = t 5 r=t^{\,5} then vertices v v, v t 4 v^{\,t^{\,4}} have v t 5 v^{\,t^{\,5}}, v t 9 v^{\,t^{\,9}}, v t − 1 v^{\,t^{-1}} as common neighbors.

Case 3. | r | = 7, | t | = 14 |r|=7,|t|=14: Here there are three subcases to consider, namely r ∈ { t 2, t 4, t 6 } r\in\{t^{2},t^{4},t^{6}\} as indicated in Figure 7. The first and last of these subcases lead to violations. Specifically, r = t 2 r=t^{\,2} violates λ = 1 \lambda=1 since the edge v ​ v t vv^{\,t} lies on two 3-cycles with respective antipodal vertices v t 2 v^{\,t^{\,2}} and v t − 1 v^{\,t^{\,-1}}. In contrast, r = t 6 r=t^{\,6} violates μ = 2 \mu=2 since the vertices v t 4 v^{\,t^{\,4}} and v t 11 v^{\,t^{\,11}} have v t 3, v t 10, v t 12 v^{\,t^{\,3}},v^{\,t^{\,10}},v^{\,t^{\,12}} as common neighbors (as well as v t 5 v^{\,t^{\,5}}). Curiously, the case r = t 4 r=t^{\,4} does not lead to any λ \lambda or μ \mu violations, however it produces no 3-cycles either. This completes the proof of the lemma. ∎

r = t 2 r=t^{\,2} v v v t v^{\,t} v t 2 v^{\,t^{\,2}} v t 3 v^{\,t^{\,3}} r = t 3 r=t^{\,3} v v v t v^{\,t} v t 3 v^{\,t^{\,3}} v, t 4 v^{\,,t^{\,4}}

Figure 5. The case | r | = | t | = 7 |r|=|t|=7 of Lemma 3

v v r = t 3 r=t^{\,3} v t 6 \;\,v^{\,t^{\,6}} v t 5 \;\;\,v^{\,t^{\,5}} v t 4 \;\;\;v^{\,t^{\,4}} v t 3 \hskip 14.40004ptv^{\,t^{\,3}} v t 2 \hskip 14.40004pt\;v^{\,t^{\,2}} v v r = t 5 r=t^{\,5} v t − 1 \;\,v^{\,t^{\,-1}} v t 9 v^{\,t^{\,9}} v t 5 \;\,\;v^{\,t^{\,5}} v t 4 \;\,\;v^{\,t^{\,4}}

Figure 6. The case | r | = | t | = 14 |r|=|t|=14 of Lemma 3

v v r = t 2 r=t^{\,2} v t − 1 v^{\,t^{\,-1}} v t 2 v^{\,t^{\,2}} v t v^{\,t} v v r = t 6 r=t^{\,6} v t 12 \;\,v^{\,t^{\,12}} v t 11 \;\,v^{\,t^{\,11}} v t 10 \;\,v^{\,t^{\,10}} v t 4 \;\,\;v^{\,t^{\,4}} v t 3 \;\,\;v^{\,t^{\,3}}

v v r = t 4 r=t^{\,4} v t 4 v^{\,t^{\,4}}

Figure 7. The case | r | = 7, | t | = 14 |r|=7,|t|=14 of Lemma 3

###### Theorem 1.

G G does not contain any order 14 14 elements.

###### Proof 3.1.

By way of contradiction, suppose G G contains an element of order 14 14. By Lemma 3 we may assume this element is s ​ t st, and as usual we set K = ⟨ s ​ t ⟩ K=\langle st\rangle. Lemma 3 now asserts that a K K -orbit partition must be of the form [II, IV 4, V] \rm[II,IV^{4},V]. (See Figure 4.) We now show this cannot occur.

Let 𝒪 \mathcal{O} be one of the four type IV orbits in the partition. Clearly 𝒪 \mathcal{O} has 28 internal edges each of which must lie on a unique 3-cycle. By Lemma 3, the third vertex of each such 3-cycle must lie in an orbit other than 𝒪 \mathcal{O}. However, this vertex cannot lie in any other type IV orbit since every pair of type IV orbits are conjoined by an orbit edge of valency 1. Thus the 28 vertices used to complete the aforementioned 3-cycles must lie in the two remaining orbits of type II and V. Since there are a total of 28 vertices in these two orbits, we conclude that every one of these vertices gets used in this fashion. Of great importance to us is the fact that every vertex in the orbit of type V lies on a unique 3-cycle with an edge in 𝒪 \mathcal{O}.

The above argument applies equally well to each type IV orbit. This means that each vertex in the unique type V orbit 𝒪 ′ \,\mathcal{O}^{\prime} must lie on exactly four 3-cycles conceived in this manner. However, 𝒪 ′ \,\mathcal{O}^{\prime} has no internal 3-cycles and there are no edges between 𝒪 ′ \,\mathcal{O}^{\prime} and the type II orbit of the partition. Thus every vertex in 𝒪 ′ \,\mathcal{O}^{\prime} lies on a total of four 3-cycles in Γ 2 \Gamma_{2}, which contradicts the fact that every vertex of Γ 2 \Gamma_{2} is required to lie on five 3-cycles in Γ 2 \Gamma_{2} ( \cf Lemma 2). We conclude that G G cannot contain any element of order 14.

## 4. Consequences of divisibility by 7

###### Proposition 2.

| G | |G| is not divisible by 14 14.

###### Proof 4.1.

Suppose 14 divides | G | |G|. Then by [9] one has | G | ∈ { 14, 42 } |G|\in\{14,42\}. Recall from [10] that [O ⁡ ( G), t] = 1 [O(G),t]=1, where O ⁡ ( G) O(G) is the maximal odd order normal subgroup of G G and t ∈ G t\in G is an involution. This alone rules out D 14 D_{14}, D 42 D_{42}, D 14 × ℤ 3 D_{14}\times\mathbb{Z}_{3} and F ​ r ​ o ​ b ​ ( 42) Frob(42) as possible isomorphism types of G G. The only remaining possibilities are ℤ 14 \mathbb{Z}_{14}, ℤ 42 \mathbb{Z}_{42}, ℤ 7 × S 3 {\mathbb{Z}_{7}}\times S_{3} and F ​ r ​ o ​ b ​ ( 21) × ℤ 2 {Frob}(21)\times\mathbb{Z}_{2}. However, each of these groups has an element of order 14 so is ruled out by Theorem 1.

{lemm}

Suppose 7 7 divides | G | |G|, and let P 7 P_{7} be a Sylow 7 7 -subgroup of G G. Then P 7 P_{7} is normal in G G.

###### Proof 4.2.

By [9] and Proposition 2, | G | |G| must divide 3 3 ⋅ 7 ⋅ 11 3^{3}\cdot 7\cdot 11. By Sylow’s Theorem, the number n 7 n_{7} of Sylow 7 7 -subgroups must satisfy n 7 = [G: N G ( P 7)] n_{7}=[G\!:\!N_{G}(P_{7})] and n 7 ≡ ( mod 7) n_{7}\equiv 1\!\pmod{7}. It is straightforward to deduce that P 7 ​ ⊴ ​ G P_{7}\trianglelefteq G for all orders of G G except possibly 3 2 ⋅ 7 ⋅ 11 3^{2}\cdot 7\cdot 11 and 3 3 ⋅ 7 ⋅ 11 3^{3}\cdot 7\cdot 11. However, in these two cases one has P 11 ​ ⊴ ​ G P_{11}\trianglelefteq G where P 11 P_{11} is a Sylow 11-subgroup of G G. As P 7 P_{7} does not embed in Aut ⁡ ( P 11) ≅ ℤ 10 {\rm Aut}(P_{11})\cong\mathbb{Z}_{10} it follows that [P 7, P 11] = 1 [P_{7},P_{11}]=1. But then P 11 ≤ N G ​ ( P 7) P_{11}\leq N_{G}(P_{7}) whence n 7 = [G: N G ( P 7)] ∈ { 1, 9, 27 } n_{7}=[G\!:\!N_{G}(P_{7})]\in\{1,9,27\}. We now conclude from the congruence n 7 ≡ ( mod 7) n_{7}\equiv 1\!\pmod{7} that n 7 = 1 n_{7}=1, \ie P 7 ​ ⊴ ​ G P_{7}\trianglelefteq G as claimed.

###### Proposition 3.

Divisibility by 7 7 implies | G | |G| divides 21 21.

###### Proof 4.3.

By our labeling scheme in Section 2 and Remark 2, it is clear that P 7 = ⟨ s ⟩ P_{7}=\langle s\rangle where s = ( 1 ​ L, 2 ​ L, …, 7 ​ L) ​ ( 1 ​ R, 2 ​ R, …, 7 ​ R) s=(1L,2L,\dots,7L)\,(1R,2R,\dots,7R). Furthermore, as ⟨ s ⟩ ​ ⊴ ​ G \langle s\rangle\trianglelefteq G by Lemma 4, we have that G G embeds in the normalizer N S ​ ( ⟨ s ⟩) N_{S}(\langle s\rangle) where S = Sym ⁡ ( V ⁡ ( Γ 1)) ≅ S 14 S={\rm Sym}(V(\Gamma_{1}))\cong S_{14}. Thus the order of G G must simultaneously divide | N S ​ ( ⟨ s ⟩) | = 2 2 ⋅ 3 ⋅ 7 2 |N_{S}(\langle s\rangle)|=2^{2}\cdot 3\cdot 7^{2} and 3 3 ⋅ 7 ⋅ 11 3^{3}\cdot 7\cdot 11. Obviously this implies | G | |G| divides 21 21.

{coro}

1. (a)

If 2 \,2 divides | G | |G|, then | G | |G| divides 6 6.

2. (b)

If 7 7 divides | G | |G|, then G G is isomorphic to either ℤ 7 \,\mathbb{Z}_{7} or F ​ r ​ o ​ b ​ ( 21) \,Frob(21).

###### Proof 4.4.

As divisibility by 2 implies | G | |G| divides 42, part (a) follows directly from Proposition 2. To prove (b), observe by Proposition 3 that | G | ∈ { 7, 21 } |G|\in\{7,21\}. There are only two groups of order 21 up to isomorphism, namely ℤ 21 \mathbb{Z}_{21} and F ​ r ​ o ​ b ​ ( 21) Frob(21), thus we have only to rule out the former. But 3 does not divide the order of the centralizer C G ​ ( s) = ( ⟨ s L ⟩ × ⟨ s R ⟩) ⋊ ⟨ t ⟩ ≅ ( ℤ 7 × ℤ 7) ⋊ ℤ 2 C_{G}(s)=(\langle s_{L}\rangle\times\langle s_{R}\rangle)\rtimes\langle t\rangle\cong(\mathbb{Z}_{7}\times\mathbb{Z}_{7})\rtimes\mathbb{Z}_{2} where S = Sym ⁡ ( V ⁡ ( Γ 1)) S={\rm Sym}(V(\Gamma_{1})). Thus G G cannot contain any element of order 21, \ie G ≇ ℤ 21 G\not\cong\mathbb{Z}_{21}.

In what follows, we gather detailed information about a putative Conway 99-graph Γ \Gamma under the assumption that G ≅ F ​ r ​ o ​ b ​ ( 21) G\cong Frob(21). Throughout, we assume G = ⟨ s, r ⟩ G=\langle s,r\rangle with | r | = 3 |r|=3. Since r r normalizes ⟨ s ⟩ \langle s\rangle it is clear that r r fixes the root vertex x x, hence Γ 1 \Gamma_{1} and Γ 2 \Gamma_{2} are preserved under the action of G G. Still, we have yet to pin down the precise structure of r r. This is remedied below.

{lemm}

With notation as above, we may assume

 | r = ( 1 ​ L, 2 ​ L, 4 ​ L) ​ ( 3 ​ L, 6 ​ L, 5 ​ L) ​ ( 1 ​ R, 2 ​ R, 4 ​ R) ​ ( 3 ​ R, 6 ​ R, 5 ​ R). r=(1L,2L,4L)\,(3L,6L,5L)\,(1R,2R,4R)\,(3R,6R,5R). |  |

###### Proof 4.5.

It is immediate that r r is an element in the normalizer N S ​ ( ⟨ s ⟩) N_{S}(\langle s\rangle) in S = Sym ⁡ ( V ⁡ ( Γ 1)) S={\rm Sym}(V(\Gamma_{1})). Applying standard group theoretic arguments, one deduces that there are 98 elements of order 3 in N S ​ ( ⟨ s ⟩) N_{S}(\langle s\rangle) and these take the form

 | ( [( 1 ​ L, 2 ​ L, 4 ​ L) ​ ( 3 ​ L, 6 ​ L, 5 ​ L)] s L i ​ [( 1 ​ R, 2 ​ R, 4 ​ R) ​ ( 3 ​ R, 6 ​ R, 5 ​ R)] s R j) ± 1 \left(\big[(1L,2L,4L)\,(3L,6L,5L)\big]^{s_{L}^{\,i}}\,\big[(1R,2R,4R)\,(3R,6R,5R)\big]^{s_{R}^{\,j}}\right)^{\pm 1} |  |

where 0 ≤ i, j ≤ 6 0\leq i,j\leq 6. However, it is easily verified that such an element is an automorphism of Γ 1 \Gamma_{1} if and only if i = j i=j. Thus, the 14 elements of order 3 in G G are precisely

 | ( ( 1 ​ L, 2 ​ L, 4 ​ L) ​ ( 3 ​ L, 6 ​ L, 5 ​ L) ​ ( 1 ​ R, 2 ​ R, 4 ​ R) ​ ( 3 ​ R, 6 ​ R, 5 ​ R)) ± s i \big((1L,2L,4L)\,(3L,6L,5L)\,(1R,2R,4R)\,(3R,6R,5R)\big)^{\pm\,s^{\,i}} |  |

from which the result follows.

{lemm}

The G G -orbit structure on Γ \Gamma is [1, 7 2, 21 4] [1,7^{2},21^{4}].

###### Proof 4.6.

As 21 does not divide 14, the two ⟨ s ⟩ \langle s\rangle -orbits on Γ 1 \Gamma_{1} cannot fuse under the action of G G. Thus the G G -orbit structure on Γ 1 \Gamma_{1} is [7 2] [7^{2}].

Now let 𝒪 \mathcal{O} be an arbitrary G G -orbit on Γ 2 \Gamma_{2}. We claim G G acts regularly on 𝒪 \mathcal{O} from which the desired result will follow. To this end, suppose i ​ j ​ X ​ Y ∈ 𝒪 ijXY\in\mathcal{O} is fixed by some g ∈ G g\in G, where X, Y ∈ { L, R } X,Y\in\{L,R\}. It follows that | g | = 3 |g|=3, since s s has no fixed points in Γ 2 \Gamma_{2}. As λ = 1 \lambda=1, we have i ≠ j i\neq j. Thus since μ = 2 \mu=2, g g must either fix or interchange the two Γ 1 \Gamma_{1} -neighbors of i ​ j ​ X ​ Y ijXY, \ie { i ​ X g, j ​ Y g } = { i ​ X, j ​ Y } \{iX^{g},jY^{g}\}=\{iX,jY\}. But as G G has odd order, these vertices must be fixed by g g, that is, i ​ X g = i ​ X iX^{g}=iX and j ​ Y g = j ​ Y jY^{g}=jY. As g g preserves adjacency, we must also have ( i ​ X C) g = i ​ X C (iX^{C})^{g}=iX^{C} and ( j ​ Y C) g = j ​ Y C (jY^{C})^{g}=jY^{C} where { X, X C } = { Y, Y C } = { L, R } \{X,X^{C}\}=\{Y,Y^{C}\}=\{L,R\}. In every instance, we obtain i ​ L g = i ​ L iL^{g}=iL and j ​ L g = j ​ L jL^{g}=jL. By transitivity of ⟨ s ⟩ \langle s\rangle on the orbit containing i ​ L iL, we get i ​ L = j ​ L z iL=jL^{z} for some z ∈ ⟨ s ⟩ z\in\langle s\rangle. This gives j ​ L [z, g] = i ​ L g − 1 ​ z ​ g = i ​ L z ​ g = j ​ L g = j ​ L jL^{[z,g]}=iL^{g^{\,-1}zg}=iL^{zg}=jL^{g}=jL, \ie j ​ L jL is a fixed point of [z, g] ∈ ⟨ s ⟩ [z,g]\in\langle s\rangle. But this implies [z, g] = 1 [z,g]=1, a contradiction since G G is nonabelian. We conclude that the G G -orbit structure on Γ 2 \Gamma_{2} is [21 4] [21^{4}] as claimed.

{rema}

Now that we understand the orbit structure of G G on Γ 2 \Gamma_{2}, it is an easy matter to determine a corresponding set of orbit representatives, viz. { 12 ​ L ​ L, 12 ​ R ​ R, 12 ​ L ​ R, 12 ​ R ​ L } \{12LL,12RR,12LR,12RL\}. For brevity we shall denote these orbits as L ​ L, R ​ R, L ​ R, R ​ L LL,RR,LR,RL, respectively. We indicate the corresponding G G -orbit partition of Γ 2 \,\Gamma_{2} in Figure 8.

b 1 b_{1} L ​ L LL b 2 b_{2} R ​ R RR b 3 b_{3} L ​ R LR b 4 b_{4} R ​ L RL b 12 b_{12} b 13 b_{13} b 24 b_{24} b 34 b_{34} b 14 b_{14} b 23 b_{23} Figure 8. General form of an G G -orbit partition of Γ 2 \Gamma_{2}

For i ​ j ​ X ​ Y ∈ V ⁡ ( Γ 2) ijXY\in V(\Gamma_{2}), we refer to i ​ X iX and j ​ Y jY as its coordinates. In the result that follows, we demonstrate a manner in which the coordinates of the 12 Γ 2 \Gamma_{2} -neighbors of a fixed vertex in Γ 2 \Gamma_{2} are balanced.

{lemm}

Let i ​ j ​ X ​ Y ijXY be a fixed but arbitrary vertex in Γ 2 \Gamma_{2} and consider collectively the 24 24 coordinates appearing among its 12 12 Γ 2 \Gamma_{2} -neighbors. Then the following hold:

1. (1)

Each of i ​ L, i ​ R, j ​ L, j ​ R iL,iR,jL,jR appears exactly once.

2. (2)

Each of k ​ L, k ​ R kL,kR appears exactly twice for each k ≠ i, j k\neq i,j.

3. (3)

Each of L L and R R appears 12 12 times, \ie Γ 2 \Gamma_{2} -neighbors of a vertex in Γ 2 \Gamma_{2} are L / R L/R -balanced.

###### Proof 4.7.

As in Lemmas 3 and 4 we let { X, X C } = { Y, Y C } = { L, R } \{X,X^{C}\}=\{Y,Y^{C}\}=\{L,R\}. We must show that each of i ​ X, j ​ Y iX,jY and i ​ X C, j ​ Y C iX^{C},jY^{C} occur exactly once as coordinates of Γ 2 \Gamma_{2} -neighbors of i ​ X ​ j ​ Y iXjY. We treat the pair i ​ X, j ​ Y iX,jY first. Since λ = 1 \lambda=1 and i ​ j ​ X ​ Y ijXY is adjacent to i ​ X ∈ V ⁡ ( Γ 1) iX\in V(\Gamma_{1}), there is a unique vertex in Γ 2 \Gamma_{2} which is their common neighbor. Evidently this vertex is of the form i ​ ℓ ​ X ​ W i\ell XW for some W ∈ { L, R } W\in\{L,R\} with ℓ ​ W ≠ j ​ Y \ell W\neq jY. Thus i ​ X iX occurs exactly once as a coordinate of a Γ 2 \Gamma_{2} -neighbor of i ​ j ​ X ​ Y ijXY and by a symmetric argument the same result holds for j ​ Y jY.

We next treat the pair i ​ X C, j ​ Y C iX^{C},jY^{C}. Observe that since λ = 1 \lambda=1, we have that i ​ j ​ X ​ Y ijXY and i ​ X C iX^{C} are nonadjacent. Since μ = 2 \mu=2, the vertices i ​ j ​ X ​ Y ijXY and i ​ X C iX^{C} must have a unique common neighbor i ​ ℓ ​ X C ​ W ∈ V ⁡ ( Γ 2) i\ell X^{C}W\in V(\Gamma_{2}) with i ​ X iX being their second common neighbor. Thus i ​ X C iX^{C} occurs exactly once as a coordinate of a Γ 2 \Gamma_{2} -neighbor of i ​ j ​ X ​ Y ijXY with a similar result holding for j ​ Y C jY^{C}. As { i ​ X, i ​ X C } = { i ​ L, i ​ R } \{iX,iX^{C}\}=\{iL,iR\} and { j ​ Y, j ​ Y C } = { j ​ L, j ​ R } \{jY,jY^{C}\}=\{jL,jR\}, assertion (1) is proved.

Now let k ≠ i, j k\neq i,j and W ∈ { L, R } W\in\{L,R\}. Since μ = 2 \mu=2 and k ​ W kW is nonadjacent to i ​ j ​ X ​ Y ijXY, there are exactly two vertices in Γ 2 \Gamma_{2} that are common neighbors of k ​ W kW and i ​ j ​ X ​ Y ijXY. Obviously, k ​ W kW appears as a coordinate in each such neighbor, so twice in total. Thus assertion (2) is proved. Finally, observe that (3) follows directly from (1) and (2).

As a consequence of Lemma 4 (3), we have the following.

{lemm}

With notation as in Figure 8, b 1 = b 12 = b 2 b_{1}=b_{12}=b_{2}, b 13 = b 23 \,b_{13}=b_{23}\, and b 14 = b 24 \,b_{14}=b_{24}.

###### Proof 4.8.

We apply Lemma 4 (3) to vertices in L ​ L LL, R ​ R RR, L ​ R LR, R ​ L RL in that order. Prefatory to this, note that the coordinates of vertices in L ​ R LR and R ​ L RL have a natural L / R L/R -balance built into them. This means we may safely ignore edges that adjoin any vertex of Γ 2 \Gamma_{2} to vertices in either of these two orbits.

Let u u be a fixed vertex in L ​ L LL. As u u has valency b 1 b_{1} in L ​ L LL, it must have b 1 b_{1} neighbors in R ​ R RR in order to restore L / R L/R -balance. This proves b 12 = b 1 b_{12}=b_{1}. By a similar argument based on R ​ R RR, we have b 12 = b 2 b_{12}=b_{2}. Now let u u be a vertex in L ​ R LR. Clearly, every neighbor of u u in L ​ L LL must be reciprocated by a neighbor in R ​ R RR to maintain balance. This proves b 13 = b 23 b_{13}=b_{23}. Applying this argument to vertices in R ​ L RL now yields b 14 = b 24 b_{14}=b_{24}.

To further narrow down possible orbit valencies, we adopt the approach used in Section 3. That is to say, we analyze 2-paths between vertices from pairs of orbits. Let u u be a fixed vertex in the orbit L ​ L LL. We wish to count in two ways the cardinality of the following set:

 | S = { u ​ v ​ w: u ​ v ​ w is a 2-path with ​ w ∈ R ​ R }. S=\{uvw:\text{$uvw$ is a 2-path with }w\in RR\}. |  |

Observe that for each of the b 1 b_{1} neighbors of u u in R ​ R RR there is a unique 2-path in S S (since λ = 1 \lambda=1), while for each of the 21 − b 1 21-b_{1} non-neighbors of u u in R ​ R RR there are two such paths (since μ = 2 \mu=2). This gives | S | = b 1 ⋅ 1 + ( 21 − b 1) ⋅ 2 = 42 − b 1 |S|=b_{1}\cdot 1+(21-b_{1})\cdot 2=42-b_{1}.

We next condition our count on the location of the intermediate vertex v v. Here we rely heavily on Lemma 4.

If v v lies in L ​ L LL, there are b 1 b_{1} choices for v v followed by b 1 b_{1} independent choices for w w. This gives a total of b 1 2 b_{1}^{2} paths in S S assuming the intermediate vertex v v is in L ​ L LL. Note that for v v in R ​ R RR the count is identical, \ie there are b 1 2 b_{1}^{2} paths in S S assuming v v is in R ​ R RR.

Now suppose v v is in the orbit L ​ R LR. Since u u has b 13 b_{13} neighbors in L ​ R LR and each such vertex has b 13 b_{13} neighbors in R ​ R RR, the total number of paths in this case is b 13 2 b_{13}^{2}. By a similar argument the number of paths with v v in R ​ L RL is b 14 2 b_{14}^{2}. Finally, we observe that there is no 2-path with intermediate vertex v v in V ⁡ ( Γ 1) V(\Gamma_{1}). Indeed, this would require that v = i ​ L v=iL and v = j ​ R v=jR for some i, j i,j, which is absurd. Thus we obtain | S | = 2 ​ b 1 2 + b 13 2 + b 14 2 |S|=2b_{1}^{2}+b_{13}^{2}+b_{14}^{2}.

Equating the above two expressions for | S | |S| gives 42 − b 1 = 2 ​ b 1 2 + b 13 2 + b 14 2 42-b_{1}=2b_{1}^{2}+b_{13}^{2}+b_{14}^{2} or equivalently

(3) |  | 42 − b 1 − 2 ​ b 1 2 = b 13 2 + b 14 2. 42-b_{1}-2b_{1}^{2}=b_{13}^{2}+b_{14}^{2}. |  |

The only integral solution to (3) is b 1 = 2 b_{1}=2, b 13 = b 14 = 4 b_{13}=b_{14}=4 which, by virtue of Lemma 4, narrows down all possible orbit valencies to the ones indicated in Figure 9.

2 2 L ​ L LL 2 2 R ​ R RR b 3 b_{3} L ​ R LR b 3 b_{3} R ​ L RL 2 2 4 4 4 4 4 − b 3 4-b_{3} 4 4 4 4 Figure 9. Narrowing down the valencies of a G G -orbit partition of Γ 2 \Gamma_{2}

We are nearly at the point of determining the unique orbit structure of G ≅ F ​ r ​ o ​ b ​ ( 21) G\cong Frob(21) acting on the second subconstituent Γ 2 \Gamma_{2} of a putative Conway 99-graph Γ \Gamma. To complete the process, we count in two ways the number of 2-paths originating at a fixed vertex u u in L ​ R LR and ending at some vertex in R ​ L RL.

One one hand, there are 4 − b 3 4-b_{3} edges from u u to some vertex w w in R ​ L RL, and in each case there is a unique 2-path u ​ v ​ w uvw since λ = 1 \lambda=1. Similarly, for each of the 21 − ( 4 − b 3) = 17 + b 3 21-(4-b_{3})=17+b_{3} vertices in R ​ L RL nonadjacent to v v there are two distinct 2-paths of required form. This gives a total of ( 4 − b 3) ⋅ 1 + ( 17 + b 3) ⋅ 2 = 38 + b 3 (4-b_{3})\cdot 1+(17+b_{3})\cdot 2=38+b_{3} such 2-paths.

We next focus our count on the location of the intermediate vertex v v. If v v is in either of L ​ L LL or R ​ R RR, there are 4 ⋅ 4 = 16 4\cdot 4=16 such 2-paths, while if v v is in either of L ​ R LR or R ​ L RL there are ( 4 − b 3) ​ b 3 = 4 ​ b 3 − b 3 2 (4-b_{3})b_{3}=4b_{3}-b_{3}^{\,2} such 2-paths. Lastly, we consider v ∈ V ⁡ ( Γ 1) v\in V(\Gamma_{1}). Since u u is in L ​ R LR, it has coordinates i ​ j ​ L ​ R ijLR for some i ≠ j i\neq j whence its two Γ 1 \Gamma_{1} -neighbors are i ​ L iL and j ​ R jR. Note that the 12 neighbors of i ​ L iL in Γ 2 \Gamma_{2} are of the form i ​ k ​ L ​ L ikLL and i ​ k ​ L ​ R ikLR ( = k ​ i ​ R ​ L =kiRL) where k ≠ i k\neq i. Thus six neighbors of i ​ L iL lie in L ​ R ∪ R ​ L LR\cup RL. However, these six neighbors are divided evenly between L ​ R LR and R ​ L RL, since i ​ k ​ L ​ R ikLR is in L ​ R LR if and only if i ​ k ​ R ​ L ikRL is in R ​ L RL. Thus i ​ L iL has three neighbors in L ​ R LR and by a symmetric argument the same holds for j ​ R jR. This gives six more 2-paths starting at u u and terminating at some vertex in R ​ L RL. Thus the total number of such 2-paths is 2 ​ ( 16) + 2 ​ ( 4 ​ b 3 − b 3 2) + 6 = 38 + 8 ​ b 3 − 2 ​ b 3 2 2(16)+2(4b_{3}-b_{3}^{2})+6=38+8b_{3}-2b_{3}^{\,2} via this second count.

Equating the two counts yields 38 + b 3 = 38 + 8 ​ b 3 − 2 ​ b 3 2 38+b_{3}=38+8b_{3}-2b_{3}^{\,2} which simplifies to 2 ​ b 3 2 − 7 ​ b 3 = 0 2b_{3}^{\,2}-7b_{3}=0. Clearly, the only integral solution is b 3 = 0 b_{3}=0 which gives us the following.

###### Proposition 4.

The unique G G -orbit partition of Γ 2 \,\Gamma_{2} where G ≅ F ​ r ​ o ​ b ​ ( 21) G\cong Frob(21) is as indicated in Figure 10.

2 2 L ​ L LL 2 2 R ​ R RR 0 0 L ​ R LR 0 0 R ​ L RL 2 2 4 4 4 4 4 4 4 4 4 4 Figure 10. The unique G G -orbit partition of Γ 2 \Gamma_{2}

{rema}

Observe that each of L ​ R ∪ { x } LR\cup\{x\} and R ​ L ∪ { x } RL\cup\{x\} is a coclique of size 22. This is in fact the largest independence number allowable by the Hoffman Ratio Bound (aka Hoffman-Delsarte inequality), see [8]. Further note from Figure 10 that every vertex outside of L ​ R ∪ { x } LR\cup\{x\} ( \resp R ​ L ∪ { x } RL\cup\{x\}) has precisely four neighbors in L ​ R ∪ { x } LR\cup\{x\} ( \resp R ​ L ∪ { x } RL\cup\{x\}).

## 5. Narrowing the search space

To this point, we have established that if | G | |G| is divisible by 7, then either G ≅ ℤ 7 G\cong\mathbb{Z}_{7} or G ≅ F ​ r ​ o ​ b ​ ( 21) G\cong Frob(21). At present, we are unable to eliminate either of these two groups in a computer-free manner. In this section, we gather sufficient structural information about Γ \Gamma that will allow us to prove G ≇ F ​ r ​ o ​ b ​ ( 21) G\not\cong Frob(21) with the aid of a computer. We would of course welcome independent verification of this fact, and we’d be delighted if a computer-free proof could be furnished.

Let us call a 3-cycle u 1 ​ u 2 ​ u 3 u_{1}u_{2}u_{3}*of type ( X 1 ​ Y 1, X 2 ​ Y 2, X 3 ​ Y 3) (X_{1}Y_{1},X_{2}Y_{2},X_{3}Y_{3})*provided u i u_{i} is in the orbit X i ​ Y i X_{i}Y_{i} where X i, Y i ∈ { L, R } X_{i},Y_{i}\in\{L,R\} for 1 ≤ i ≤ 3 1\leq i\leq 3.

###### Proposition 5.

Each of L ​ L LL and R ​ R RR consists of seven vertex-disjoint 3 3 -cycles.

###### Proof 5.1.

By transitivity of G G on its orbits, each orbit of 3-cycles in Γ 2 \Gamma_{2} has size 21 with the exception being 3-cycles of type ( L ​ L, L ​ L, L ​ L) (LL,LL,LL) or ( R ​ R, R ​ R, R ​ R) (RR,RR,RR). Indeed, orbits of 3-cycles of these two types would have to be of size 7 since the 3-cycles remain internal to their respective orbits. As there are a total of 140 3-cycles in Γ 2 \Gamma_{2} ( \cf Lemma 2), their division into n 7 n_{7} orbits of size 7 and n 21 n_{21} orbits of size 21 must satisfy 7 ​ n 7 + 21 ​ n 21 = 140 7n_{7}+21n_{21}=140. Moreover, 0 ≤ n 7 ≤ 2 0\leq n_{7}\leq 2 since each of L ​ L LL and R ​ R RR has internal valency 2. Since the only integral solution to the above is n 7 = 2 n_{7}=2 and n 21 = 6 n_{21}=6, each of L ​ L LL and R ​ R RR must contain seven vertex-disjoint 3-cycle.

For all 𝒪, 𝒪 ′ ∈ { L ​ L, R ​ R, L ​ R, R ​ L } \mathcal{O},\mathcal{O}^{\prime}\in\{LL,RR,LR,RL\}, we define

 | E ⁡ ( 𝒪, 𝒪 ′) = { u ​ v ∣ u ∈ 𝒪, v ∈ 𝒪 ′, u and v are adjacent }. E(\mathcal{O},\mathcal{O}^{\prime})=\{uv\mid\mbox{$u\in\mathcal{O},v\in\mathcal{O}^{\prime}$, $u$ and $v$ are adjacent}\}. |  |

For brevity, we write E ⁡ ( 𝒪) E(\mathcal{O}) rather than the more cumbersome E ⁡ ( 𝒪, 𝒪) E(\mathcal{O},\mathcal{O}).

{coro}

The subgraph Δ \Delta of Γ 2 \Gamma_{2} induced on E ⁡ ( L ​ L, R ​ R) E(LL,RR) is a disjoint union of cycles.

###### Proof 5.2.

This follows at once since Δ \Delta is a bipartite graph of valency 2 ( \cf Figure 10).

We next consider the induced graph Γ 2 ​ [ℰ] \Gamma_{2}[\mathcal{E}] where

 | ℰ = { u w ∈ E ( Γ 2) ∣ u ​ v ​ w is a 3-cycle for some v ∈ V ⁡ ( Γ 1) }. \mathcal{E}=\{uw\in E(\Gamma_{2})\mid\mbox{$uvw$ is a 3-cycle for some $v\in V(\Gamma_{1})$}\}. |  |

###### Proposition 6.

1. (a)

Γ 2 ​ [ℰ] \Gamma_{2}[\mathcal{E}] is a 2-valent spanning subgraph of Γ 2 \,\Gamma_{2}.

2. (b)

Every edge in ℰ \mathcal{E} traverses two distinct orbits. Furthermore, ℰ ∩ E ⁡ ( L ​ L, R ​ R) = ∅ \mathcal{E}\cap E(LL,RR)=\emptyset and ℰ ∩ E ⁡ ( L ​ R, R ​ L) = ∅ \mathcal{E}\cap E(LR,RL)=\emptyset.

3. (c)

A cycle in Γ 2 ​ [ℰ] \Gamma_{2}[\mathcal{E}] must traverse orbits in the following repetitive order:

 | L ​ L, L ​ R, R ​ R, R ​ L, L ​ L, L ​ R, R ​ R, R ​ L, …, L ​ L, L ​ R, R ​ R, R ​ L, L ​ L. LL,LR,RR,RL,LL,LR,RR,RL,\dots,LL,LR,RR,RL,LL. |  |

###### Proof 5.3.

Recall that every vertex in Γ \Gamma lies on seven 3-cycles. As i ​ X ∈ V ⁡ ( Γ 1) iX\in V(\Gamma_{1}) lies on the 3-cycle with vertices x x, i ​ X iX, i ​ X C iX^{C} where { X, X C } = { L, R } \{X,X^{C}\}=\{L,R\}, each of the remaining six 3-cycles on i ​ X iX must have a unique edge in ℰ \mathcal{E}. Ranging over all 14 choices for the vertex i ​ X iX, we conclude that | ℰ | = 14 ⋅ 6 = 84 |\mathcal{E}|=14\cdot 6=84.

Let i ​ j ​ X ​ Y ijXY be an arbitrary vertex in Γ 2 \Gamma_{2}, and observe that i ​ j ​ X ​ Y ijXY has i ​ X iX and j ​ Y jY as its Γ 1 \Gamma_{1} -neighbors. This means the edge adjoining i ​ j ​ X ​ Y ijXY to i ​ X iX must lie in a unique 3-cycle with third vertex of the form i ​ ℓ ​ X ​ W i\ell XW for some W ∈ { L, R } W\in\{L,R\}. Likewise, the edge adjoining i ​ j ​ X ​ Y ijXY to j ​ Y jY must lie in a unique 3-cycle with third vertex of the form j ​ m ​ Y ​ U jmYU for some U ∈ { L, R } U\in\{L,R\}. But then by definition, the edges adjoining i ​ j ​ X ​ Y ijXY to i ​ ℓ ​ X ​ W i\ell XW and i ​ j ​ X ​ Y ijXY to j ​ m ​ Y ​ U jmYU must lie in ℰ \mathcal{E}. This proves Γ 2 ​ [ℰ] \Gamma_{2}[\mathcal{E}] is a spanning subgraph of Γ 2 \Gamma_{2} and moreover, all 84 vertices in Γ 2 ​ [ℰ] \Gamma_{2}[\mathcal{E}] must have valency at least 2. But the sum of all valencies in Γ 2 ​ [ℰ] \Gamma_{2}[\mathcal{E}] must equal 2 ​ | ℰ | = 168 2|\mathcal{E}|=168 from which we conclude that Γ 2 ​ [ℰ] \Gamma_{2}[\mathcal{E}] is 2 2 -valent. Thus (a) is proved.

To prove (b) we first observe that ℰ ∩ E ⁡ ( 𝒪) = ∅ \mathcal{E}\cap E(\mathcal{O})=\emptyset for every orbit 𝒪 ∈ { L ​ L, R ​ R, L ​ R, R ​ L } \mathcal{O}\in\{LL,RR,LR,RL\}. Indeed, this follows for 𝒪 ∈ { L ​ R, R ​ L } \mathcal{O}\in\{LR,RL\} because these orbits are cocliques. For 𝒪 ∈ { L ​ L, R ​ R } \mathcal{O}\in\{LL,RR\} the result follows from Proposition 5 which asserts that every edge in L ​ L LL or R ​ R RR already occurs as an edge of an internal 3-cycle. It follows that every edge in ℰ \mathcal{E} must traverse distinct orbits. The proof that ℰ ∩ E ⁡ ( L ​ L, R ​ R) = ∅ \mathcal{E}\cap E(LL,RR)=\emptyset is obvious since no two vertices of the form i ​ j ​ L ​ L ijLL and k ​ ℓ ​ R ​ R k\ell RR can have a common Γ 1 \Gamma_{1} -neighbor. To prove ℰ ∩ E ⁡ ( L ​ R, R ​ L) = ∅ \mathcal{E}\cap E(LR,RL)=\emptyset we focus on the five 3-cycles in Γ 2 \Gamma_{2} that occur at a fixed vertex u u of L ​ L LL. Note that u u has two neighbors in R ​ R RR and four neighbors in each of L ​ R LR and R ​ L RL. As we have already shown, two of its eight neighbors in L ​ R ∪ R ​ L LR\cup RL form edges in Γ 2 ​ ( ℰ) \Gamma_{2}(\mathcal{E}) so cannot lead to 3-cycles at u u. As u u lies on a unique internal 3-cycle, it is clear that the remaining eight edges incident to u u (two into R ​ R RR and six into L ​ R ∪ R ​ L LR\cup RL) must form edges of the four non-internal 3-cycles at u u.

However, the two edges into R ​ R RR cannot form a 3-cycle at u u because every edge in R ​ R RR already occurs in a 3-cycle internal to the orbit R ​ R RR. The only remaining possibility is that these four 3-cycles at u u are of the form ( L ​ L, R ​ R, L ​ R) (LL,RR,LR), ( L ​ L, R ​ R, R ​ L) (LL,RR,RL), and ( L ​ L, L ​ R, R ​ L) (LL,LR,RL) (twice). It is the latter case that holds significance for us. This is because by transitivity on L ​ L LL, we obtain 42 of the 84 edges that traverse the orbits L ​ R LR and R ​ L RL. Likewise, by replacing L ​ L LL with R ​ R RR in the above argument we obtain 42 additional such edges. Thus all 84 edges traversing L ​ R LR and R ​ L RL are accounted for as sharing a common neighbor in either L ​ L LL or R ​ R RR, which implies ℰ ∩ E ⁡ ( L ​ R, R ​ L) = ∅ \mathcal{E}\cap E(LR,RL)=\emptyset. This completes the proof of (b).

From above, proving (c) is tantamount to showing there are no 2-paths u ​ v ​ w uvw in Γ 2 ​ [ℰ] \Gamma_{2}[\mathcal{E}] with u, w ∈ 𝒪 u,w\in\mathcal{O} and v ∈ 𝒪 ′ v\in\mathcal{O}^{\prime}, where { 𝒪, 𝒪 ′ } \{\mathcal{O},\mathcal{O}^{\prime}\} is one of { L ​ L, L ​ R } \{LL,LR\}, { L ​ L, R ​ L } \{LL,RL\}, { R ​ R, L ​ R } \{RR,LR\}, { R ​ R, R ​ L } \{RR,RL\}. We illustrate this for { 𝒪, 𝒪 ′ } = { L ​ L, L ​ R } \{\mathcal{O},\mathcal{O}^{\prime}\}=\{LL,LR\} since the other cases yield to a symmetric argument.

Suppose first that 𝒪 = L ​ L \mathcal{O}=LL and 𝒪 ′ = L ​ R \mathcal{O}^{\prime}=LR, so u, w ∈ L ​ L u,w\in LL and v ∈ L ​ R v\in LR. By transitivity of G G on L ​ R LR, we may assume v = 12 ​ L ​ R v=12LR. The only possible Γ 2 ​ [ℰ] \Gamma_{2}[\mathcal{E}] -neighbors of v v are therefore u = 1 ​ j ​ L ​ L u=1jLL and w = 1 ​ k ​ L ​ L w=1kLL. But in this case u ​ v ​ w uvw is a 3-cycle, which violates λ = 1 \lambda=1 since each of u, v, w u,v,w is adjacent to 1 ​ L ∈ Γ 1 1L\in\Gamma_{1}. Next suppose 𝒪 = L ​ R \mathcal{O}=LR and 𝒪 ′ = L ​ L \mathcal{O}^{\prime}=LL so that u, w ∈ L ​ R u,w\in LR and v ∈ L ​ L v\in LL. By transitivity of G G on L ​ R LR, there exists g ∈ G g\in G such that w = u g w=u^{g}. But then w w is adjacent to v, v g ∈ L ​ L v,v^{g}\in LL, thereby reducing this case to the one previously treated. With this, the proof of the proposition is complete.

{rema}

We may now describe the eight orbits of 3 3 -cycles in Γ 2 \Gamma_{2} by type. Specifically, they are ( L ​ L, L ​ L, L ​ L) (LL,LL,LL) (one orbit of size 7 7), ( R ​ R, R ​ R, R ​ R) (RR,RR,RR) (one orbit of size 7 7), ( L ​ L, R ​ R, L ​ R) (LL,RR,LR) (one orbit of size 21 21), ( L ​ L, R ​ R, R ​ L) (LL,RR,RL) (one orbit of size 21 21), ( L ​ L, L ​ R, R ​ L) (LL,LR,RL) (two orbits of size 21 21 each), ( R ​ R, L ​ R, R ​ L) (RR,LR,RL) (two orbits of size 21 21 each).

{coro}

The graph Γ 2 ​ [ℰ] \Gamma_{2}[\mathcal{E}] is a disjoint union of 84 k \,\frac{84}{k} cycles of identical length k k for some k ∈ { 4, 12, 28 } k\in\{4,12,28\}.

###### Proof 5.4.

By Proposition 6 (a), Γ 2 ​ [ℰ] \Gamma_{2}[\mathcal{E}] is 2-valent and hence a union of cycles. Moreover, all such cycles must have the same size k k by transitivity of G G on orbits of vertices. By Proposition 6 (c), the edges in such cycles must traverse the orbits L ​ L, L ​ R, R ​ R, R ​ L LL,LR,RR,RL in repetition, which means k k is a multiple of 4. One possibility is that the second time the cycle enters the orbit L ​ L LL it terminates at the initial vertex. In this case there are 21 4 4 -cycles in the graph Γ 2 ​ [ℰ] \Gamma_{2}[\mathcal{E}]. Otherwise, the cycle fails to close after one iteration resulting in a 4-path u ​ v ​ w ​ z ​ u ′ uvwzu^{\prime} where u, u ′ ∈ L ​ L u,u^{\prime}\in LL. But then by transitivity of G G on the vertices of L ​ L LL, there exists an element g ∈ G g\in G for which u ′ = u g u^{\prime}=u^{g}. Obviously, | g | = 3 |g|=3 or 7 7. If | g | = 3 |g|=3 we get seven 12 12 -cycles, namely the seven images of the 12-cycle u ​ v ​ w ​ z ​ u g ​ v g ​ w g ​ z g ​ u g 2 ​ v g 2 ​ w g 2 ​ z g 2 ​ u uvwzu^{g}v^{g}w^{g}z^{g}u^{g^{2}}v^{g^{2}}w^{g^{2}}z^{g^{2}}u under the action of ⟨ s ⟩ \langle s\rangle. A similar result holds for | g | = 7 |g|=7 in which case we obtain three 28 28 -cycles. As these are the only possibilities, the proof is complete.

{rema}

It is currently unclear to us if a Conway 9 9 -graph Q ​ R ​ ( 9) QR(9) (aka Paley graph of order 9 9) exists inside a putative Conway 99 99 -graph Γ \Gamma. But if this be the case then Γ 2 ​ [ℰ] \Gamma_{2}[\mathcal{E}] would consist of 21 21 vertex-disjoint 4 4 -cycles ( \cf Corollary 5). Moreover, by the transitive action of G G on each of its two Γ 1 \Gamma_{1} -orbits, Γ \Gamma would contain 21 21 embedded copies of Q ​ R ​ ( 9) QR(9).

## 6. Divisibility by 7 7 implies G ≅ ℤ 7 G\cong\mathbb{Z}_{7}

Up to this point, we have shown that if | G | |G| is divisible by 7 then there are just two possibilities for the isomorphism type of G G, namely ℤ 7 \mathbb{Z}_{7} and F ​ r ​ o ​ b ​ ( 21) Frob(21). In Section 4 we determined the unique orbit partition of Γ \Gamma under the assumption that G ≅ F ​ r ​ o ​ b ​ ( 21) G\cong Frob(21), while in Section 5 we derived a fairly comprehensive structural framework for Γ \Gamma under this same assumption. The framework obtained is essential in reducing run-time, thereby making a computer search feasible. Below we give details of our computer-generated proof that G G is isomorphic to ℤ 7 \mathbb{Z}_{7} provided | G | |G| is divisible by 7.

The program was written and implemented in GAP Version 4.12.2 [5]. Specifically, we utilized the GRAPE package Version 4.9.0 [12]. As the computer code is prohibitively large we cannot reproduce it here, however it is available upon request.

Below we sketch the key steps of the program.
Step 1: Initialize the vertex set, then create edges common to all cases of the search, namely those incident to each vertex in Γ 1 \Gamma_{1}. These account for all edges from x x to its Γ 1 \Gamma_{1} -neighbors, all edges internal to Γ 1 \Gamma_{1}, and all edges that traverse Γ 1 \Gamma_{1} to Γ 2 \Gamma_{2}.
Step 2: Form the seven 3-cycles internal to L ​ L LL by applying the AddEdgeOrbit function to a chosen internal edge incident to 12 ​ L ​ L 12LL.
Step 3: Repeat step 2 to generate the seven 3-cycles in the orbit R ​ R RR.
Step 4: Choose six possible neighbors of 12 ​ L ​ L 12LL in the orbit L ​ R LR, followed by three possible choices for such neighbors in R ​ L RL. Then apply the AddEdgeOrbit function to obtain half of the edges of the induced graph Γ 2 ​ [ℰ] \Gamma_{2}[\mathcal{E}].
Step 5: Repeat step 4 at the vertex 12 ​ R ​ R 12RR, thus determining the entire graph Γ 2 ​ [ℰ] \Gamma_{2}[\mathcal{E}].
Step 6: Choose the eight remaining neighbors of 12 ​ L ​ L 12LL. (This consists of three neighbors in L ​ R LR, three in R ​ L RL and two in R ​ R RR.) Apply the AddEdgeOrbit function to determine all edges incident to v v for every vertex in v ∈ L ​ L v\in LL.
Step 7: Repeat step 6 for the six remaining neighbors of 12 ​ R ​ R 12RR. (This consists of three neighbors in L ​ R LR and three in R ​ L RL.) This determine all edges incident to v v for every vertex in v ∈ R ​ R v\in RR.
Step 8: Complete the graph by forming all edges traversing the orbits L ​ R LR and R ​ L RL. This is accomplished by choosing four possible neighbors of 12 ​ L ​ R 12LR and applying the AddEdgeOrbit function. The graph is now ready for testing.
Step 9: Compare [[0, 0, 14], [1, 1, 12], [2, 12, 0]] [[0,0,14],[1,1,12],[2,12,0]] to the output yielded by the GlobalParameters function.

The program ran through 2,916 2,916 iterations. Each iteration was comprised of multiple cases ranging between the hundreds and thousands. We were able to avoid cases ranging well into the millions by continually exploiting the DoubleCosetRepsAndSizes function. This function was used when it was theoretically evident that every element in the double coset H ​ g ​ K HgK would produce the same computational result as g g, so need not be tested. This occurred at steps 6, 7 6,7 and 8 8 where H H and K K were suitably chosen “coordinate” stabilizers in the symmetric groups S 10 S_{10}, S 6 S_{6} and S 4 S_{4}, respectively.

## References

- [1] N. L. Biggs, *Algebraic Graph Theory*, Cambridge University Press, Cambridge, 1974, 2nd edition 1993.
- [2] N. L. Biggs, *Finite Groups of Automorphisms: Course Given at the University of Southampton*, October-December 1969, London Mathematical Society Lecture Note Series, vol. 6, Cambridge University Press, London and New York, 1971.
- [3] A. E. Brouwer, A. M. Cohen, A. Neumaier, *Distance-Regular Graphs*, Springer Berlin, Heidelberg, 1989.
- [4] J. H. Conway, *Five $1,000 Problems*, On-Line Encyclopedia of Integer Sequences (OEIS) sequence #A248380, 2017.
- [5] The GAP Group, GAP – Groups, Algorithms, and Programming, Version 4.12.2, 2022. [https://www.gap-system.org][5].
- [6] Godsil C., Royle G.: Algebraic Graph Theory. Graduate Texts in Mathematics. Springer New York, NY (2001).
- [7] R. K. Guy, “Problems”, in L. M. Kelly (ed.) *Proceedings of a Conference held at Michigan State University*, East Lansing, Mich., June 17-19, 1974, pp. 233-244, Lecture Notes in Mathematics vol. 490, Springer-Verlag, Berlin and New York, 1975.
- [8] W. H. Haemers, *Hoffman’s ratio bound*, Linear Algebra Applic. 617 (15) (2021), 215-219.
- [9] A. A. Makhnev, I. M. Minakova, *On automorphisms of strongly regular graphs with parameters λ = 1 \lambda=1, μ = 2 \mu=2*, Discrete Math. Applic. 14 (2) (2004), 201-210.
- [10] A. A. Makhnev, *On automorphisms of distance-regular graphs*, J. Math. Sciences 166 (6) (2010), 733-742.
- [11] J. J. Rotman, *An Introduction to the Theory of Groups*, Graduate Texts in Mathematics, vol. 148, Springer, New York, NY, 1994.
- [12] L. H. Soicher, The GRAPE package for GAP, Version 4.9.0, 2022. [https://gap-packages.github.io/grape][6].


## Links

[1]: https://info.arxiv.org/about
[2]: https://info.arxiv.org/help/license/index.html#licenses-available
[3]: mailto:pcesarz@uwyo.edu
[4]: mailto:andrew.woldar@villanova.edu
[5]: https://www.gap-system.org
[6]: https://gap-packages.github.io/grape
