<!-- source: https://cdm.ucalgary.ca/article/download/62323/54015 | converted from PDF -->

Volume 15, Number 1, Pages 22–41
ISSN 1715-0868

CONSTRUCTION OF STRONGLY REGULAR GRAPHS
HAVING AN AUTOMORPHISM GROUP OF COMPOSITE
ORDER

DEAN CRNKOVI ´C AND MARIJA MAKSIMOVI ´C

Abstract. In this paper we outline a method for constructing strongly
regular graphs from orbit matrices admitting an automorphism group
of composite order. In 2011, C. Lam and M. Behbahani introduced
the concept of orbit matrices of strongly regular graphs and developed
an algorithm for the construction of orbit matrices of strongly regu-
lar graphs with a presumed automorphism group of prime order, and
construction of corresponding strongly regular graphs. The method of
constructing strongly regular graphs developed and employed in this
paper is a generalization of that developed by C. Lam and M. Behba-
hani. Using this method we classify SRGs with parameters (49,18,7,6)
having an automorphism group of order six. Eleven of the SRGs with
parameters (49,18,7,6) constructed in that way are new. We obtain an
additional 385 new SRGs(49,18,7,6) by switching. Comparing the con-
structed graphs with previously known SRGs with these parameters,
we conclude that up to isomorphism there are at least 727 SRGs with
parameters (49,18,7,6). Further, we show that there are no SRGs with
parameters (99,14,1,2) having an automorphism group of order six or
nine, i.e. we rule out automorphism groups isomorphic to Z6, S3, Z9, or
E9.
 1. Introduction

One of the main problems in the theory of strongly regular graphs (SRGs)
is constructing and classifying SRGs with given parameters. A frequently
used method of constructing combinatorial structures is a construction of
combinatorial structures with a prescribed automorphism group. Orbit ma-
trices of block designs have been used for such a construction of combi-
natorial designs since 1980s. However, orbit matrices of strongly regular
graphs have not been introduced until 2011. Namely, Majid Behbahani and
Clement Lam introduced the concept of orbit matrices of strongly regular

Received by the editors February 18, 2018 and in revised form March 2, 2019.
2010 Mathematics Subject Classiﬁcation. 05E30, 20D45.
Key words and phrases. Strongly regular graph, automorphism group, orbit matrix.
This work has been fully supported by Croatian Science Foundation under the project
6732.
 c⃝2020 University of Calgary

22

SRGS HAVING AN AUTOMORPHISM GROUP OF COMPOSITE ORDER 23

graphs in [2]. They developed an algorithm for construction of orbit matri-
ces of strongly regular graphs with an automorphism group of prime order,
and construction of corresponding strongly regular graphs. In this way they
constructed strongly regular graphs with parameters (49,18,7,6) having an
automorphism of order ﬁve or seven.
In this paper we present a method of constructing strongly regular graphs
admitting an automorphism group of composite order from orbit matrices.
This method uses the notion of an orbit matrix of a strongly regular graph
introduced by Behbahani and Lam in [2]. Further, we give a classiﬁcation
of strongly regular graphs with parameters (49,18,7,6) having an automor-
phism group of order six. In that way we have constructed 55 SRGs with
parameters (49,18,7,6), and eleven of them are new. Using Godsil–McKay
switching and cycle-type switching we obtain additional 385 new SRGs with
parameters (49,18,7,6), thereby proving that up to isomorphism there are at
least 727 strongly regular graphs with parameters (49,18,7,6). Additionally,
we use the described method of the construction of SRGs admitting an au-
tomorphism group of composite order for an attempt to construct a strongly
regular graph with parameters (99,14,1,2) having an automorphism group
of order six or nine, which would prove the existence of a strongly regular
graph with these parameters.
The paper is organized as follows: after a brief description of the termi-
nology and some background results, in Section 3 we describe the concept
of orbit matrices, based on the work of Behbahani and Lam [2]. In Section
4 we explain the construction of strongly regular graphs from their orbit
matrices. In Section 5 we apply this method to construct strongly regular
graphs with parameters (49,18,7,6) having an automorphism group isomor-
phic to Z6 or S3, and in Section 6 we construct new SRGs with parameters
(49,18,7,6) by switching. In Section 7 we show that there are no strongly
regular graph with parameters (99,14,1,2) having an automorphism group
isomorphic to Z6, S3, Z9, or E9.

2. Background and terminology

We assume that the reader is familiar with basic notions from the theory
of ﬁnite groups. For basic deﬁnitions and properties of strongly regular
graphs we refer the reader to [4] or [14].
A graph is regular if all its vertices have the same valency; a simple regular
graph Γ = (V, E) is strongly regular with parameters (v, k, λ, µ) if it has |V| =
v vertices, valency k, and if any two adjacent vertices are together adjacent
to λ vertices, while any two nonadjacent vertices are together adjacent to
µ vertices. A strongly regular graph with parameters (v, k, λ, µ) is usually
denoted by SRG(v, k, λ, µ). An automorphism of a strongly regular graph Γ
is a permutation of vertices of Γ, such that every two vertices are adjacent
if and only if their images are adjacent.

24 DEAN CRNKOVI ´C AND MARIJA MAKSIMOVI ´C

An orthogonal array with parameters k and n is a k×n2 array with entries
from a set N of size n such that the n2 ordered pairs deﬁned by any two rows
of the matrix are all distinct. We denote the orthogonal array with these
parameters by OA(k, n). An OA(k, n) is equivalent to a set of k −2 mutually
orthogonal Latin squares (see [11]). Given an orthogonal array OA(n, k) we
can deﬁne a graph Γ as follows: The vertices of Γ are the n2 columns of the
orthogonal array (viewed as column vectors of length k), and two vertices
are adjacent if they have the same entries in one coordinate position. The
graph Γ is strongly regular with parameters (n2, (n − 1)k, n − 2 + (k − 1)(k −
2), k(k − 1)) (see [11]). Since the strongly regular graphs having at most
36 vertices are completely enumerated (see [5]), SRGs with 49 vertices are
the ﬁrst case of such graphs coming from orthogonal arrays that still have
to be classiﬁed. Enumeration of SRGs with parameters (49,18,7,6) having
an automorphism group of order six, i.e. the construction of 396 new SRGs
with these parameters in this paper is a step in that classiﬁcation.
Let Γ1 = (V, E1) and Γ2 = (V, E2) be strongly regular graphs and G ≤
Aut(Γ1) ∩ Aut(Γ2). An isomorphism α : Γ1 → Γ2 is called a G-isomorphism
if there exists an automorphism τ : G → G such that for each x, y ∈ V and
each g ∈ G the following holds:

(τ g).(αx) = αy ⇔ g.x = y.

Let d = (d1, d2, . . . , dv) be a vector of length v and S = {x1, x2, . . . , xv} a
set of v elements. Let ρ be a permutation on the set S. We say that ρ is a
d-permissible permutation if for every xi ∈ S it follows that

xj = ρ(xi) ⇒ di = dj.

3. Orbit matrices of strongly regular graphs

Orbit matrices of block designs have been frequently used for construction
of block designs, see e.g. [12] and [7]. In 2011 Behbahani and Lam introduced
the concept of orbit matrices of SRGs (see [2]).
Let Γ be a SRG(v, k, λ, µ) and A be its adjacency matrix. Suppose an
automorphism group G of Γ partitions the set of vertices V into b orbits
O1, . . . , Ob, with sizes n1, . . . , nb, respectively. The orbits divide A into
submatrices [Aij], where Aij is the adjacency matrix of vertices in Oi versus
those in Oj. We deﬁne matrices C = [cij] and R = [rij], 1 ≤ i, j ≤ t, such
that
 cij = column sum of Aij,
rij = row sum of Aij.

The matrix R is related to C by

(1) rijni = cijnj.

Since the adjacency matrix is symmetric, it follows that

(2) R = CT .

SRGS HAVING AN AUTOMORPHISM GROUP OF COMPOSITE ORDER 25

The matrix R is the row orbit matrix of the graph Γ with respect to G, and
the matrix C is the column orbit matrix of the graph Γ with respect to G.
Let us assume that a group G acts as an automorphism group of a
SRG(v, k, λ, µ). In order to enable a construction of SRGs with a presumed
automorphism group G, each matrix with the properties of an orbit matrix
will be called an orbit matrix for parameters (v, k, λ, µ) and a group G (see
[1]). Let W = A2. Using the same orbit partition of the vertices, W can
also be partitioned in W = [Wij], where i and j are the indices of the orbits.
Deﬁne a b × b matrix S = [sij] such that sij is the sum of all the entries in
Wij. Behbahani and Lam showed that S = CN R, and the orbit matrices
R = [rij] and RT = C = [cij] satisfy the condition

b∑

s=1 cisrsjns = δij(k − µ)nj + µninj + (λ − µ)cijnj.

Since R = CT , it follows that

(3)
 b∑

s=1
 ns
nj ciscjs = δij(k − µ) + µni + (λ − µ)cij

and b∑

s=1
 ns
nj rsirsj = δij(k − µ) + µni + (λ − µ)rji.

Therefore, we introduce the following deﬁnition of orbit matrices of SRGs.

Deﬁnition 3.1. A (b×b)-matrix R = [rij] with entries satisfying conditions:

b∑

j=1 rij =
 b∑

i=1
 ni
nj rij = k,(4)
 b∑

s=1
 ns
nj rsirsj = δij(k − µ) + µni + (λ − µ)rji(5)

where 0 ≤ rij ≤ nj, 0 ≤ rii ≤ ni − 1, and ∑b
i=1 ni = v, is called a row orbit
matrix for a strongly regular graph with parameters (v, k, λ, µ) and the orbit
lengths distribution (n1, . . . , nb).

Deﬁnition 3.2. A (b×b)-matrix C = [cij] with entries satisfying conditions:

b∑

i=1 cij =
 b∑

j=1
 nj
ni cij = k,(6)
 b∑

s=1
 ns
nj ciscjs = δij(k − µ) + µni + (λ − µ)cij,(7)

26 DEAN CRNKOVI ´C AND MARIJA MAKSIMOVI ´C

where 0 ≤ cij ≤ ni, 0 ≤ cii ≤ ni − 1, and ∑b
i=1 ni = v, is called a column
orbit matrix for a strongly regular graph with parameters (v, k, λ, µ) and the
orbit lengths distribution (n1, . . . , nb).

4. The method of construction

For the construction of SRGs with parameters (v, k, λ, µ) we ﬁrst check
whether these parameters are feasible. Then we select the group G and
assume that it acts as an automorphism group of an SRG(v, k, λ, µ). The
next step is to ﬁnd all the orbit lengths distributions (n1, n2, . . . , nb) for an
action of the group G and use them to costruct orbit matrices. Then we
construct strongly regular graphs from the obtained orbit matrices by using
a composition series of the group G to make a reﬁnement of the constructed
orbit matrices, as explained in Subsection 4.4. This approach have been
successfully used for construction of block designs (see e.g. [6, 7, 8]).
We prove the following theorem which we ﬁnd very useful while deter-
mining the possible orbit lengths distributions for an action of the presumed
automorphism group on a strongly regular graph.

Theorem 4.1. Let Γ be an SRG(v, k, λ, µ) with an automorphism group G
which acts on the set of vertices of Γ with b orbits, with f ﬁxed orbits and
b−f = v−f
w orbits of length w. Further, let ni be the number of ﬁxed vertices
incident with i ﬁxed vertices, and let mj be the number of orbits of length w
whose representatives are incident with j ﬁxed vertices. Then the following
equalities hold:
 f∑

i=0 ni = f, w
 f∑

j=0 mj = v − f(8)
 f∑

i=0 ni · i + w
 f∑

j=0 mj · j = f · k(9)
 f∑

i=0 ni · (i
2

) + w
 f∑

j=0 mj · (j
2

)
(10)
 = ∑f
i=0 ni · i
2 · λ + f · (f − 1) − ∑f
i=0 ni · i
2 · µ

Proof. The equalities (8) are obtained by counting ﬁxed and nonﬁxed ver-
tices. Let V be the set of vertices and F be the set of ﬁxed vertices. The
equality (9) is obtained by counting the elements of the set {(x, y) : x ∈
V, y ∈ F}. The equality (10) is obtained by counting the elements of the set
{({x, y}, z) : x, y ∈ F, z ∈ V, (x, z), (y, z) ∈ E}. □

Not every orbit matrix gives rise to strongly regular graphs while, on
the other hand, a single orbit matrix may produce several nonisomorphic

SRGS HAVING AN AUTOMORPHISM GROUP OF COMPOSITE ORDER 27

strongly regular graphs. For the elimination of orbit matrices that produce
G-isomorphic strongly regular graphs, we use the same method as for the
elimination of orbit matrices of G-isomorphic designs (see for example [7]).
We could use row or column orbit matrices, but since we construct matrices
row by row, it is more convenient for us to use column orbit matrices.

4.1. Orbit lengths distribution. Suppose an automorphism group G of Γ
partitions the set of vertices V into b orbits O1, . . . , Ob, with sizes n1, . . . , nb.
Obviously, ni is a divisor of |G|, i = 1, . . . , b, and

b∑

i=1 ni = v.

When determining the orbit lengths distribution we also use the following
result that can be found in [1].

Theorem 4.2. Let s < r < k be the eigenvalues of a SRG(v, k, λ, µ), then

φ ≤ max(λ, µ)
k − r v,

where φ is the number of ﬁxed points for an automorphism group G, where
|G| > 1 .

4.2. Prototypes for a row of a column orbit matrix. A prototype for
a row of a column orbit matrix C gives the information about the number of
occurrences of each integer as an entry of a particular row of C. Behbahani
and Lam [1, 2] introduced the concept of a prototype for a row of a column
orbit matrix C of a strongly regular graph with a presumed automorphism
group of prime order. We will generalize this concept, and describe a pro-
totype for a row of a column orbit matrix C of a strongly regular graph
under a presumed automorphism group of composite order. Prototypes will
be useful in the ﬁrst step of the construction of strongly regular graphs,
namely the construction of column orbit matrices.
Suppose an automorphism group G of a strongly regular graph Γ par-
titions the set of vertices V into b orbits O1, . . . , Ob, of sizes n1, . . . , nb.
With li, i = 1, . . . , ρ, we denote all divisors of |G| in ascending order (l1 =
1, . . . , lρ = |G|).

4.2.1. Prototypes for a ﬁxed row. Consider the rth row of a column orbit
matrix C. We say that it is a ﬁxed row of a matrix C if nr = 1, i.e. if it
corresponds to an orbit of length 1. The entries in this row are either 0 or
1. Let dli denote the number of orbits whose length are li, i = 1, . . . , ρ.
Let xe denote the number of occurrences of an element e ∈ {0, 1} at the
positions of the rth row which correspond to the orbits of length 1. It follows
that

(11) x0 + x1 = d1,

28 DEAN CRNKOVI ´C AND MARIJA MAKSIMOVI ´C

where d1 is the number of orbits of length 1. Since the diagonal elements of
the adjacency matrix of a strongly regular graphs are equal to 0, it follows
that x0 ≥ 1.
Let y(li)
e denote the number of occurrences of an element e ∈ {0, 1} at
the positions of the rth row which correspond to the orbits of length li
(i = 2, . . . , ρ). We have

(12) y(li)
0 + y(li)
1 = dli, i = 2, . . . , ρ.

Because the row sum of an adjacency matrix is equal to k, it follows that

(13) x1 +
 ρ∑

i=2 li · y(li)
1 = k.

The vector p1 = (x0, x1; y(l2)
0 , y(l2)
1 ; . . . ; y(lρ)
0 , y(lρ)
1 )

whose components are nonnegative integer solutions of the equalities (11),
(12), and (13) is called a prototype for a ﬁxed row. The length of a prototype
for a ﬁxed row is 2ρ.

4.2.2. Prototypes for a nonﬁxed row. Let us consider the rth row of a column
orbit matrix C, where nr ̸= 1. Let dli denote the number of orbits whose
length is li, i = 1, . . . , ρ.
If a ﬁxed vertex is adjacent to a vertex from an orbit Oi, 1 ≤ i ≤ b, then
it is adjacent to all vertices from the orbit Oi. Therefore, the entries at the
positions corresponding to ﬁxed columns are either 0 or nr. Let xe denote
the number of occurrences of an element e ∈ {0, nr} at those positions of
the rth row which correspond to the orbits of length 1. We have

(14) x0 + xnr = d1.

The entries at the positions corresponding to the orbits whose lengths are
greater than 1 are 0, 1, . . . , nr − 1 or nr. The entry at the position (r, r) is
0 ≤ cr,r ≤ nr − 1, since the diagonal elements of the adjacency matrix of
strongly regular graphs are 0.
Let y(li)
e denote the number of occurrences of an element e ∈ {0, . . . , nr}
of rth row at the positions which correspond to the orbits of length li (i =
2, . . . , ρ). From (1) and (2) we conclude that

(15) crini = cirnr,

where cir ∈ {0, . . . , ni}. If cri · ni
nr ̸∈ {0, . . . , ni}, then y(ni)
cri = 0. It follows
that

(16)
 nr∑

e=0 y(li)
e = dli, i = 2, . . . , ρ.

SRGS HAVING AN AUTOMORPHISM GROUP OF COMPOSITE ORDER 29

Since the row sum of an adjacency matrix is equal to k, we have that

(17) xnr +
 ρ∑

i=2
 nr∑

h=1 y(li)
h · h · nli
nr = k.

From equalities (3) and (15), we have sij = ∑b
k=1 cikcjknk, hence

srr =
 b∑

k=1 c
2
rknk,

It follows that

(18) n2
rxnr +
 ρ∑

i=2
 nr∑

h=1 y(li)
h · h2 · nli = srr,

where srr = (k − µ)nr + µn2
r + (λ − µ)crrnr and crr ∈ {0, . . . , nr − 1}.
The vector
 pnr = (x0, xnr ; yl2
0 , . . . , yl2
nr ; . . . ; ylρ
0 , . . . , ylρ
nr ),

whose components are nonnegative integer solutions of equalities (14), (16),
(17), and (18) is called a prototype for a row corresponding to the orbit of
length nr. The length of a prototype for a row which corresponds to the
orbit of length nr is 2+∑ρ
i=2(nr + 1).

4.3. Types. Suppose an automorphism group G of Γ partitions the set of
vertices V into b orbits O1, . . . , Ob, with sizes n1, . . . , nb, where ∑b
j=1 nj = v.
Let us deﬁne the vector κn = (κn1, . . . , κnb) such that κni = κnj if and only
if the representatives of the G-orbits Oi and Oj have conjugate stabilizers.
For every 1 ≤ r ≤ b it follows that

•
 b∑

j=1 c
2
rjnj = (k − µ)nr + µn2
r + (λ − µ)crrnr, crr = 0, . . . , nr − 1,

•
 b∑

j=1
 nj
nr crj = k,

• 0 ≤ cij ≤ ni, 0 ≤ cii ≤ ni − 1.

The nonnegative integer solution (crj)r is called an orbit structure of
the rth orbit. We say that two orbit structures (c′
ri)r and (c′′
ji)j are of
the same type if there exists a κn-permissible permutation α such that
c′
ri = c′′
j(αi), 1 ≤ i ≤ b.

Remark 4.3. Each type uniquely deﬁnes a prototype, while a prototype
does not uniquely determine a type. However, if all the representatives of the
orbits of the same length have conjugate stabilizers, then prototypes uniquely
determine types.

30 DEAN CRNKOVI ´C AND MARIJA MAKSIMOVI ´C

4.4. Reﬁnement. The idea of a reﬁnement of an orbit matrix is based on
the facts given in Theorems 4.4 and 4.5. A proof of Theorem 4.4 can be
found in [7].

Theorem 4.4. Let Ω be a ﬁnite nonempty set, G ≤ S(Ω) and H a normal
subgroup of G. Further, let x and y be elements of the same G-orbit. Then
|xH| = |yH|.

Theorem 4.5. Let Ω be a ﬁnite nonempty set, H ▹ G ≤ S(Ω), x ∈ Ω and
xG = ⊔h
i=1 xiH. Then a group G/H acts transitively on the set {xiH | i =
1, 2, . . . , h}.

Proof. H ▹ G yields (xH)g = (xg)H for all x ∈ Ω and g ∈ G. It holds that
(xiH)gH = (xig)H, i.e. a group G/H acts as a permutation group on the
set {xiH | i = 1, 2, . . . , h}. It remains to prove that G/H acts transitively
on {xiH | i = 1, 2, . . . , h}. Let xiH and xjH be two diﬀerent H-orbits
contained in G-orbit xG. There exists g ∈ G such that xj = xig, so we have
(xiH)gH = (xig)H = xjH. □

Hence, orbit matrices for an action of a group G can be reﬁned to the
corresponding orbit matrices for the action of the group H ▹ G. Every ﬁnite
group G has a composition series

{1} = H0 ⊴ H1 ⊴ · · · ⊴ Hn = G,

where composition factors Hi+1/Hi are simple, for 0 ≤ i ≤ n−1. If H ▹G ≤
Aut(Γ), then every G-orbit reﬁnes to one or more H-orbits of same lengths,
hence an orbit matrix for an action of the group G reﬁnes to orbit matrices
for the action of H.
The adjacency matrix of a strongly regular graph is also its orbit matrix
with respect to the trivial group. Hence, for {1} = H0 ⊴ H1 the reﬁnement
of orbit matrices for H1 produce the orbit matrices for H0, which are the
adjacency matrices of strongly regular graphs.

4.5. The algorithm of construction. The method of construction of
strongly regular graphs admitting an automorphism group G having a com-
position series {1} = H0 ⊴ H1 ⊴ · · · ⊴ Hn = G consists of the following n + 1
steps:
Step 1: Construction of the orbit matrices for the group G;
Step 2: Construction of the corresponding orbit matrices for the sub-
group Hn−1;
...
Step n: Construction of the corresponding orbit matrices for the sub-
group H1;
Step n+1: Construction of the corresponding orbit matrices for the
subgroup H0 = {1}, i.e. adjacency matrices of the strongly regular
graphs.

SRGS HAVING AN AUTOMORPHISM GROUP OF COMPOSITE ORDER 31

In each step of the construction, in order to construct orbit matrices, we
ﬁrst ﬁnd all prototypes and then all corresponding row types. Further, in
each step we eliminate mutually G-isomorphic orbit matrices so in the last
step of the construction we eliminate G-isomorphic strongly regular graphs.
This algorithm is especially eﬀective when the group G is solvable, i.e. when
the group G has a composition series

{1} = H0 ⊴ H1 ⊴ · · · ⊴ Hn = G,

where Hi+1/Hi is isomorphic to a cyclic group of a prime order pi, for
0 ≤ i ≤ n − 1.
In the sequel we show a construction of SRGs with parameters (49,18,7,6)
having an automorphism group of order six, and an attempt to construct
SRGs with parameters (99,14,1,2) with an automorphism group of order six
or nine. The complexity of the computations depends of the parameters of
the SRG, the presumed automorphism group and its presumed action. The
most demanding case was an attempt to construct a SRGs with parameters
(99,14,1,2) assuming an action of the group S3 acting with orbit distributions
(0,0,15,9) and (0,0,17,8). For each of these two cases it takes approximately
10 months on a quad-core CPU (3.2 GHz) with 8 threads. The construction
was conducted using our own programs written in GAP [9] and Mathematica
[15].

5. Classification of SRGs with parameters (49,18,7,6) having an
automorphism group of order six

According to [1, 2], all known SRGs with parameters (49,18,7,6) are ei-
ther constructed from OA(7, 3), or obtained by Pasechnik’s construction
[13], or constructed by Behbahani and Lam by using the SRG program
which is described in [1]. Further, strongly regular graphs with parameters
(49,18,7,6) that do not come from Latin squares are constructed in [3] by
applying Godsil-McKay switching and cycle-type switching. In this section
we describe the construction of some new strongly regular graphs with pa-
rameters (49,18,7,6), obtained by using the algorithm described in Section
4. We show that there are exactly 34 strongly regular graphs with parame-
ters (49,18,7,6) having a cyclic automorphism group of order six, 24 of them
nonisomorphic to the graphs described in [1, 2]. Further, we show that there
are exactly 36 strongly regular graphs with parameters (49,18,7,6) having a
nonabelian automorphism group of order six, 11 of them nonisomorphic to
the graphs described in [1, 2]. Fifteen of the constructed SRGs have auto-
morphism groups that contain both Z6 and S3. Comparing the constructed
SRGs with the SRGs constructed in [2] and [3], we establish that eleven
of the strongly regular graphs having an automorphism group of order six
constructed in this paper have not been previously known.
Let Γ be a strongly regular graph with parameters (49,18,7,6) and G ∼=
⟨α|α6 = 1⟩ ∼= Z6 ∼= Z2 × Z3 be the presumed automorphism group of
Γ. By di we denote the number of G-orbits of length i, i ∈ {1, 2, 3, 6}, so

32 DEAN CRNKOVI ´C AND MARIJA MAKSIMOVI ´C

d = (d1, d2, d3, d6) is the corresponding orbit lengths distribution. Using the
program Mathematica [15] we get all the possible orbit lengths distribution
that satisfy Theorem 4.2.
Using our own programs written in GAP [9] we construct all orbit matrices
for given orbit lengths distributions. In Table 1 we present the number of
mutually nonisomorphic orbit matrices for orbit lengths distribution that
give rise to orbit matrices for Z6. We reﬁne the constructed orbit matrices,
and obtain orbit matrices for the action of the subgroup Z3 ▹ Z6. In the
last step we obtain the adjacency matrices of strongly regular graphs with
parameters (49,18,7,6). The number of orbit matrices for Z3 (obtained by
the reﬁnement) and the number of the constructed SRGs with parameters
(49,18,7,6) are presented in Table 1.

Table 1. Number of orbit matrices and SRGs(49,18,7,6)
for the automorphism group Z6

distribution #OM-Z6 #OM-Z3 #SRGs distribution #OM-Z6 #OM-Z3 #SRGs

( 0, 2, 3, 6 ) 5 6 4 ( 3, 2, 0, 7 ) 2 3 0
( 0, 2, 5, 5 ) 2 2 0 ( 3, 2, 2, 6 ) 3 5 6
( 0, 2, 7, 4 ) 3 6 0 ( 3, 2, 4, 5 ) 3 6 0
( 1, 0, 0, 8 ) 4 10 2 ( 3, 2, 6, 4 ) 2 4 0
( 1, 0, 2, 7 ) 23 11 5 ( 4, 0, 3, 6 ) 4 9 0
( 1, 0, 4, 6 ) 37 66 16 ( 4, 0, 5, 5 ) 9 16 0
( 1, 0, 6, 5 ) 63 128 0 ( 5, 1, 0, 7 ) 1 1 0
( 1, 3, 0, 7 ) 3 2 1 ( 5, 1, 2, 6 ) 2 2 0
(1, 3, 2, 6 ) 2 1 0 ( 5, 1, 4, 5 ) 2 2 0
( 1, 3, 4, 5 ) 1 1 0 ( 5, 1, 6, 4 ) 1 1 0
( 1, 3, 6, 4 ) 1 1 0 ( 7, 0, 0, 7 ) 1 1 0
( 2, 1, 3, 6 ) 19 35 0 (7, 0, 2, 6 ) 1 1 0
( 2, 1, 5, 5 ) 19 31 0 ( 7, 0, 4, 5 ) 1 1 0
(2, 1, 7, 4 ) 7 7 0

Finally, we check isomorphisms of strongly regular graphs using GAP.
Thereby we prove Theorem 5.1. Orders and structures of the full auto-
morphism groups of these SRGs are also determined by using GAP. This
information is shown in Table 2. In Table 2 we also compare the constructed
graphs with the graphs constructed from OA(7, 3) and the ones described
in [2]. The group denoted by Frob21 is the Frobenius group of order 21,
isomorphic to the semidirect product Z7 : Z3.

Theorem 5.1. Up to isomorphism there exists exactly 34 strongly regular
graphs with parameters (49, 18, 7, 6) having a cyclic automorphism group of
order six.

Let G ∼= ⟨α, β|α3 = β2 = 1, αβ = α2⟩ ∼= S3 ∼= Z3 : Z2 be an automor-
phism group of a strongly regular graph Γ with parameters (49,18,7,6). As

SRGS HAVING AN AUTOMORPHISM GROUP OF COMPOSITE ORDER 33

Table 2. SRGs with parameters (49,18,7,6) having Z6 as
an automorphism group

i |Aut(Γi)| Aut(Γi) From OA(7, 3) From Behbahani-Lam [2]
1 6 Z6 Yes No
2 6 Z6 No No
3 6 Z6 No No
4 6 Z6 No No
5 6 Z6 No No
6 6 Z6 No No
7 6 Z6 No No
8 6 Z6 No No
9 6 Z6 No No
10 6 Z6 No No
11 6 Z6 No No
12 6 Z6 No No
13 6 Z6 No No
14 6 Z6 No No
15 6 Z6 No No
16 6 Z6 No No
17 12 D12 Yes No
18 12 D12 No No
19 12 Z6 × Z2 No No
20 12 Z6 × Z2 Yes No
21 18 Z3 × S3 No No
22 24 D24 Yes No
23 24 D24 No No
24 30 Z3 × D10 No Yes
25 48 D8 × S3 No No
26 72 A4 × S3 Yes No
27 72 A4 × S3 No No
28 72 A4 × S3 No No
29 72 A4 × S3 No No
30 126 S3 × Frob21 No Yes
31 144 S3 × S4 Yes No
32 144 S3 × S4 No No
33 1008 S3 × PSL(3, 2) Yes Yes
34 1764 (Frob21 × Frob21) : E4 Yes Yes

in the case of the cyclic group Z6, we take into consideration all possibili-
ties for orbit lengths distributions for the action of S3 on a SRG(49,18,7,6)
and construct corresponding orbit matrices. Then we reﬁne the constructed
orbit matrices for S3 to obtain orbit matrices for the subgroup Z3. In the
ﬁnal step of the construction we obtain adjacency matrices of the strongly
regular graphs with parameters (49,18,7,6) admitting a nonabelian auto-
morphism group of order six. We compare the constructed graphs with the
graphs constructed from OA(7, 3) and the graphs described in [2], and those

34 DEAN CRNKOVI ´C AND MARIJA MAKSIMOVI ´C

with an automorphism group isomorphic to Z6. The results are presented
in Theorems 5.2 and 5.3, and Tables 3, 4, and 5.

Theorem 5.2. Up to isomorphism there exists exactly 36 strongly regular
graphs with parameters (49, 18, 7, 6) having an automorphism group isomor-
phic to the symmetric group S3.

Theorem 5.3. Up to isomorphism there exists exactly 55 strongly regular
graphs with parameters (49, 18, 7, 6) having an automorphism group of order
six.

In Table 3 we give distribution that give rise to orbit matrices for S3,
and the number of the constructed orbit matrices. Further, the number of
orbit matrices for Z3 (obtained by the reﬁnement) and the number of the
constructed SRGs with parameters (49,18,7,6) are also presented in Table
3.
 Table 3. Number of orbit matrices and SRGs(49,18,7,6)
for the automorphism group S3

distribution #OM-S3 #OM-Z3 #SRGs distribution #OM-S3 #OM-Z3 #SRGs

(0,2,3,6) 5 6 0 (3,2,4,5) 3 6 5
(0,2,5,5) 2 2 0 (3,2,6,4) 2 4 0
(0,2,7,4) 3 6 4 (4,0,3,6) 4 9 4
(1,0,0,8) 4 10 1 (4,0,5,5) 9 16 0
(1,0,2,7) 23 11 0 (4,0,7,4) 11 11 0
(1,0,4,6) 37 66 0 (4,0,9,3) 11 7 1
(1,0,6,5) 63 128 20 (4,0,11,2) 22 22 0
(1,0,8,4) 127 117 2 (4,0,13,1) 74 73 0
(1,0,10,3) 133 39 0 (5,1,0,7) 1 1 0
(1,0,12,2) 191 170 0 (5,1,2,6) 2 2 3
(1,3,0,7) 3 2 0 (5,1,4,5) 2 2 0
(1,3,2,6) 2 1 0 (5,1,6,4) 1 1 0
(1,3,4,5) 1 1 0 (7,0,0,7) 1 1 4
(1,3,6,4) 1 1 3 (7,0,2,6) 1 1 0
(2,1,3,6) 19 35 0 (7,0,4,5) 1 1 0
(2,1,5,5) 19 31 11 (7,0,6,4) 2 2 0
(2,1,7,4) 7 7 0 (7,0,8,3) 3 3 0
(3,2,0,7) 2 3 0 (7,0,10,2) 2 2 0
(3,2,2,6) 3 5 0 (7,0,12,1) 3 3 0

Comparing the SRGs from Theorems 5.1, 5.2, and 5.3 (and the corre-
sponding Tables 1, 2, 3, 4, and 5) with the SRGs constructed in [2] and
[3], we found out that eleven of the strongly regular graphs having an auto-
morphism group of order six constructed in this paper are new; eight of the
SRGs having Z6 as the full automorhism group and the SRGs having the
full automorphism group isomorphic to D12, Z6 × Z2, or Z3 × S3.

SRGS HAVING AN AUTOMORPHISM GROUP OF COMPOSITE ORDER 35

Table 4. SRGs with parameters (49,18,7,6) having S3 as
an automorphism group

i |Aut(Γi)| Aut(Γi) From OA(7, 3) From Behbahani-Lam [2] From Z6
1 6 S3 Yes No No
2 6 S3 Yes No No
3 6 S3 Yes No No
4 6 S3 No No No
5 6 S3 No No No
6 6 S3 Yes No No
7 6 S3 Yes No No
8 6 S3 Yes No No
9 6 S3 Yes No No
10 6 S3 Yes No No
11 6 S3 Yes No No
12 6 S3 Yes No No
13 6 S3 Yes No No
14 6 S3 Yes No No
15 6 S3 No No No
16 6 S3 Yes No No
17 6 S3 Yes No No
18 6 S3 Yes No No
19 12 D12 Yes No [17]
20 12 D12 No No [18]
21 18 Z3 x S3 No No [21]
22 18 E9 : Z2 Yes No No
23 24 D24 No No [23]
24 24 D24 Yes No [22]
25 24 S4 Yes No No
26 24 S4 Yes No No
27 48 D8 × S3 No No [25]
28 72 A4 × S3 No No [27]
29 72 A4 × S3 No No [28]
30 72 A4 × S3 Yes No [26]
31 72 A4 × S3 No No [29]
32 126 S3 × F rob21 No Yes [30]
33 144 S3 × S4 Yes No [31]
34 144 S3 × S4 No No [32]
35 1008 S3 × P SL(3, 2) Yes Yes [33]
36 1764 (F rob21 × F rob21) : E4 Yes Yes [34]

In the next section we construct further SRGs with parameters (49,18,7,6)
by switching. In that way we obtain additional 385 new strongly regular
graphs with parameters (49,18,7,6).

6. SRGs(49,18,7,6) obtained by switching

Behbahani, Lam, and ¨Osterg˚ard constructed new SRGs with parameters
(49,18,7,6) by Godsil-McKay switching and cycle-type switching (see [3]).
In this section we apply switching to the new SRGs(49,18,7,6) described in
Section 5.

36 DEAN CRNKOVI ´C AND MARIJA MAKSIMOVI ´C

Table 5. SRGs with parameters (49,18,7,6) having an au-
tomorphism group of order six

|Aut(Γi)| #SRGs |Aut(Γi)| #SRGs
6 34 72 4
12 4 126 1
18 2 144 2
24 4 1008 1
30 1 1764 1
48 1

Let Γ = (V, E) be a graph and let V1 be a nonempty proper subset of V.
Further, let V2 := V \ V1. We construct a graph Γ′ = (V, E ′) in the following
way:

(1) if v1, v′
1 ∈ V1, then {v1, v′
1} ∈ E ′ if and only if {v1, v′
1} ∈ E,
(2) if v2, v′
2 ∈ V2, then {v2, v′
2} ∈ E ′ if and only if {v1, v′
1} ∈ E,
(3) if v1 ∈ V1, v2 ∈ V2, then {v1, v2} ∈ E ′ if and only if {v1, v2} /∈ E.

The graphs Γ and Γ′ are said to be switching-equivalent, and V1 is called
the switching-set. Let A be the adjacency matrix of a strongly regular graph
Γ with parameters (v, k, λ, µ). If A has eigenvalues k, r, and s, satisfying

v + 4rs + 2r + 2s = 0,

and Γ′ is regular, then Γ′ is again a SRG (possibly with diﬀerent parameters
than Γ). In [3] the authors use Godsil–McKay switching and cycle-type
switching to construct SRGs with parameters (49,18,7,6).

Deﬁnition 6.1. Let Γ = (V, E) be a graph and let π = (C1, C2, . . . , Ct, D)
be an ordered partition of V. Suppose that for all 1 ≤ i, j ≤ t and v ∈ D it
holds that

(1) any two vertices in Ci have the same number of neighbors in Cj,
(2) v has either 0, |Ci|/2, or |Ci| neighbors in Ci.

Then Godsil–McKay switching transforms Γ as follows: For each v ∈ D and
1 ≤ i ≤ t such that v has |Ci|/2 neighbors in Ci, add and delete edges such
that the neighborhood of v in Ci is complemented.

Godsil–McKay switching transforms a strongly regular graph to a strongly
regular graph (see [10]). Behbahani, Lam, and ¨Osterg˚ard [3] used the special
case of k = 1 and |C1| = 4, because they found out that this case was most
useful. From that reason we also use the case when k = 1 and |C1| = 4
to obtain new SRGs(49,18,7,6). Beside Godsil–McKay switching we use
cycle-type switching.

SRGS HAVING AN AUTOMORPHISM GROUP OF COMPOSITE ORDER 37

Deﬁnition 6.2. Let Γ = (V, E) be a graph and let π = (C1, C2, D) be an
ordered partition of V with |C1| = |C2| = S. Suppose that any v ∈ D fulﬁlls
(at least) one of the following conditions:
(1) v has equally many neighbors in C1 and C2,
(2) v has S neighbors in C1 ∪ C2.
Then cycle-type switching transforms Γ as follows: For each v ∈ D that is
adjacent to all vertices in C1 and to none in C2, or vice versa, add and
delete edges such that the neighborhood of v in C1 ∪ C2 is complemented.

As in [3], we used cycle-type switching with |C1| = |C2| = 3 to obtain new
SRGs with parameters (49,18,7,6). It is possible that the new graph obtained
from a strongly regular graph by cycle-type switching is not strongly regu-
lar, so this has to be checked whenever switching. Applying Godsil–McKay
switching and cycle-type switching to the SRGs having an automorphism
group of order six we obtain 385 new SRGs with parameters (49,18,7,6).
Thereby we proved Theorem 6.3. Information on orders of the full automor-
phism groups of the known SRGs with parameters (49,18,7,6) are given in
Table 6.
 Table 6. All known SRGs with parameters (49,18,7,6)

|Aut(Γi)| #SRGs |Aut(Γi)| #SRGs |Aut(Γi)| #SRGs
1 552 12 6 63 1
2 76 15 3 72 4
3 36 16 4 126 1
4 17 18 2 144 2
6 34 21 1 1008 1
8 8 24 4 1764 1
9 1 30 1
10 1 48 1

Theorem 6.3. Up to isomorphism there exists at least 727 strongly regular
graphs with parameters (49, 18, 7, 6).

The adjacency matrices of the constructed SRGs can be found at the link:
http://www.math.uniri.hr/~mmaksimovic/srg49.txt.

7. An automorphism group of order six or nine acting on a
SRG(99,14,1,2)

It is not known whether SRGs with parameters (99,14,1,2) exists (see
[5]). By applying the algorithm described in Section 4 we try to construct
an SRG(99,14,1,2) assuming an action of a group of order six or nine. We
used the following result from [1].

38 DEAN CRNKOVI ´C AND MARIJA MAKSIMOVI ´C

Theorem 7.1 (Behbahani–Lam). If there exists an SRG(99, 14, 1, 2), then
the only possible prime divisors of the size of its automorphism group are 2
and 3. Moreover, if that graph has an automorphism φ of order three, then
φ has no ﬁxed points.

7.1. Z6 acting on a SRG(99,14,1,2). Let Γ be a strongly regular graph
with parameters (99,14,1,2). Further, let us assume that the group G ∼=
⟨α|α6 = 1⟩ ∼= Z6 ∼= Z2 × Z3 acts as an automorphism group of Γ.
Let us denote by di the number of G-orbits of length i, i ∈ {1, 2, 3, 6},
so d = (d1, d2, d3, d6) is the orbit lengths distribution. Using the program
Mathematica we get all possible orbit lengths distributions that satisfy The-
orem 4.2. Using a program written in GAP we construct all orbit matrices
with the obtained orbit lengths distribution. In Table 7 we give the number
of constructed orbit matrices for each orbit lengths distribution.

Table 7. Number of nonisomorphic orbit matrices of SRGs
with parameters (99,14,1,2) for an automorphism group Z6.

distribution # OM
( 0, 0, 1, 16 ) 2
( 0, 0, 3, 15 ) 4
( 0, 0, 5, 14 ) 7

Then we try to reﬁne the obtained orbit matrices in order to construct
orbit matrices for the action of a subgroup Z3 ▹ Z6. Such orbit matrices for
Z3 do not exist, so there is no SRG(99,14,1,2) having an automorphism of
order six.

7.2. S3 acting on a SRG(99,14,1,2). Let Γ be a strongly regular graph
with parameters (99,14,1,2). Further, let us assume that the group G ∼=
⟨a, b | b3 = 1, a2 = 1, aba = b−1⟩ ∼= S3 ∼= Z2 : Z3 act as an automorphism
group of Γ. By di we denote the number of G-orbits of length i, i ∈
{1, 2, 3, 6}, and by d = (d1, d2, d3, d6) we denote the corresponding orbit
lengths distribution. Table 8 shows the number of constructed orbit matri-
ces for each orbit lengths distribution.
The orbit matrices for S3 cannot be reﬁned to orbit matrices for the
subgroup Z3 ▹ S3, so there is no SRG(99, 14, 1, 2) having an automorphism
group isomorphic to S3.
We summarize the results obtained in Sections 7.1 and 7.2 in the following
theorem.

Theorem 7.2. There is no SRG(99, 14, 1, 2) having an automorphism group
of order six.

SRGS HAVING AN AUTOMORPHISM GROUP OF COMPOSITE ORDER 39

Table 8. Number of nonisomorphic orbit matrices of SRGs
with parameters (99,14,1,2) for an automorphism group S3.

distribution # OM distribution # OM
( 0, 0, 1, 16 ) 2 ( 0, 0, 11, 11 ) 0
( 0, 0, 3, 15 ) 4 ( 0, 0, 13, 10 ) 0
( 0, 0, 5, 14 ) 7 ( 0, 0, 15, 9 ) 0
( 0, 0, 7, 13 ) 0 ( 0, 0, 17, 8 ) 0
( 0, 0, 9, 12 ) 0

7.3. E9 acting on a SRG(99,14,1,2). Let Γ be a strongly regular graph
with parameters (99,14,1,2). Further, let us assume that the group G ∼=
⟨a, b | a3 = b3 = 1, ab = a⟩ ∼= E9 ∼= Z3 × Z3 acts as an automorphism group
of Γ. By di we denote the number of G-orbits of length i, i ∈ {1, 3, 9}, and
by d = (d1, d3, d9) we denote the corresponding orbit lengths distribution.
By Theorem 7.1 we get that the only possible orbit lengths distribution
for E9 acting on a SRG(99,14,1,2) is (0,0,11). Up to isomorphism there is
only one orbit matrix for that orbit lengths distribution, namely the orbit
matrix
 O =
 


















 4 1 1 1 1 1 1 1 1 1 1
1 4 1 1 1 1 1 1 1 1 1
1 1 4 1 1 1 1 1 1 1 1
1 1 1 4 1 1 1 1 1 1 1
1 1 1 1 4 1 1 1 1 1 1
1 1 1 1 1 4 1 1 1 1 1
1 1 1 1 1 1 4 1 1 1 1
1 1 1 1 1 1 1 4 1 1 1
1 1 1 1 1 1 1 1 4 1 1
1 1 1 1 1 1 1 1 1 4 1
1 1 1 1 1 1 1 1 1 1 4
 


















 .

Table 9. Number of nonisomorphic orbit matrices of SRGs
with parameters (99,14,1,2) for an automorphism group of
order nine.
 distribution # OM
( 0, 0, 11) 1

In order to construct SRGs(99,14,1,2) having E9 as an automorphism
group, we need to reﬁne the orbit matrix O to obtain orbit matrices for the
action of a subgroup Z3 ▹ E9. Such orbit matrices for Z3 do not exist, so
there is no SRG(99,14,1,2) with an automorphism group isomorphic to E9.

40 DEAN CRNKOVI ´C AND MARIJA MAKSIMOVI ´C

7.4. Z9 acting on a SRG(99,14,1,2). Let Γ be a strongly regular graph
with parameters (99, 14, 1, 2), and let us assume that the group G ∼= ⟨α | α9 =
1⟩ ∼= Z9 acts as an automorphism group of Γ.
Let us denote by di the number of G-orbits of length i, i ∈ {1, 3, 9}, and
by d = (d1, d3, d9) the corresponding orbit lengths distribution. Theorem
7.1 yields that the only possible orbit lengths distribution for Z9 acting
on a SRG(99,14,1,2) is (0,0,11), hence O is the only orbit matrix for Z9
acting on a SRG(99,14,1,2). There is no SRG(99,14,1,2) for Z9 acting with
orbit matrix O, so there is no SRG(99,14,1,2) with an automorphism group
isomorphic to Z9.
Since the groups Z9 and E9 cannot act as automorphism groups of strongly
regular graphs with parameters (99,14,1,2), it follows that nine cannot be a
divisor of the order of an automorphism group of a SRG(99,14,1,2). The re-
sults from Theorem 7.1 and the results obtained in Section 7 are summarized
in the following theorem.

Theorem 7.3. If there exists a SRG(99, 14, 1, 2), then the order of its full
automorphism group is 2a3b, and b ∈ {0, 1}. If a SRG(99, 14, 1, 2) has an
automorphism φ of order three, then φ has no ﬁxed points. Further, there is
no SRG(99, 14, 1, 2) having an automorphism group of order six.

References

1. M. Behbahani, On strongly regular graphs, PhD thesis, Concordia University, 2009.
2. M. Behbahani, C. Lam, Strongly regular graphs with non-trivial automorphisms, Dis-
crete Math. 311 (2011), 132–144.
3. M. Behbahani, C. Lam and P. R. J. ¨Osterg˚ard, On triple systems and strongly regular
graphs, J. Combin. Theory Ser. A 119 (2012), 1414–1426.
4. T. Beth, D. Jungnickel and H. Lenz, Design Theory Vol. I, Cambridge University
Press, Cambridge, 1999.
5. A. E. Brouwer, Parameters of Strongly Regular Graphs, accessed on 1/10/2017, http:
//www.win.tue.nl/~aeb/graphs/srg/srgtab51-100.html.
6. D. Crnkovi´c and M. O. Pavˇcevi´c, Some new symmetric designs with parameters
(64,28,12), Discrete Math. 237 (2001), 109–118.
7. D. Crnkovi´c and S. Rukavina, Construction of block designs admitting an abelian
automorphism group, Metrika 62 (2005), 175–183.
8. D. Crnkovi´c, S. Rukavina and M. Schmidt, A classiﬁcation of all symmetric block
designs of order nine with an automorphism of order six, J. Combin. Des. 14 (2006),
301–312.
9. The GAP Group, GAP – Groups, Algorithms, and Programming, version 4.8.10, 2018,
https://www.gap-system.org.
10. C. D. Godsil and B. D. McKay, Constructing cospectral graphs, Aequationes Math.
25 (1982), 257–268.
11. C. Godsil and G. Royle, Algebraic Graph Theory, Springer–Verlag, New York, 2001.
12. Z. Janko, Coset enumeration in groups and constructions of symmetric designs, Com-
binatorics ’90 (Gaeta, 1990), 275–277, Ann. Discrete Math. 52, North–Holland, Am-
sterdam, 1992.
13. D. V. Pasechnik, Skew-symmetric association schemes with two classes and strongly
regular graphs of type L2n−1(4n − 1), Interactions between algebra and combinatorics,
Acta Appl. Math. 29 (1992), 129–138.

SRGS HAVING AN AUTOMORPHISM GROUP OF COMPOSITE ORDER 41

14. V. D. Tonchev, Combinatorial Conﬁgurations: Designs, Codes, Graphs, Pitman
Monographs and Surveys in Pure and Applied Mathematics 40, Wiley, New York,
1988.
15. Wolfram Research, Inc., Mathematica, version 11.2, Champaign, IL, 2017.

Department of Mathematics
University of Rijeka
Radmile Matejˇci´c 2, 51000 Rijeka, Croatia
E-mail address: deanc@math.uniri.hr

Department of Mathematics
University of Rijeka
Radmile Matejˇci´c 2, 51000 Rijeka, Croatia
E-mail address: mmaksimovic@math.uniri.hr
