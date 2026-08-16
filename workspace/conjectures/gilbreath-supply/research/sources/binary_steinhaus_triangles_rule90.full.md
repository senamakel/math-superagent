<!-- source: https://hal.science/hal-02313960v1/file/articleV1.pdf | converted from PDF -->

HAL Id: hal-02313960

https://hal.science/hal-02313960v1

Preprint submitted on 11 Oct 2019 (v1), last revised 30 Oct 2021 (v2)

HAL is a multi-disciplinary open access archive
for the deposit and dissemination of scientific re-
search documents, whether they are published or not.
The documents may come from teaching and research
institutions in France or abroad, or from public or pri-
vate research centers.
 L’archive ouverte pluridisciplinaire HAL, est des-
tinée au dépôt et à la diffusion de documents scien-
tifiques de niveau recherche, publiés ou non, émanant
des établissements d’enseignement et de recherche
français ou étrangers, des laboratoires publics ou
privés.

HAL Authorization

Symmetric binary Steinhaus triangles and parity-regular
Steinhaus graphs

Jonathan Chappelon

To cite this version:

Jonathan Chappelon. Symmetric binary Steinhaus triangles and parity-regular Steinhaus graphs. 2019. ⟨hal-
02313960v1⟩

Symmetric binary Steinhaus triangles and
parity-regular Steinhaus graphs

Jonathan CHAPPELON
∗

IMAG, Université de Montpellier, CNRS, Montpellier, France

October 11, 2019

Abstract

A binary Steinhaus triangle is a triangle of zeroes and ones that points down
and with the same local rule than the Pascal triangle modulo 2. A binary Steinhaus
triangle is said to be rotationally symmetric, horizontally symmetric or dihedrally
symmetric if it is invariant under the 120 degrees rotation, the horizontal reﬂec-
tion or both, respectively. The ﬁrst part of this paper is devoted to the study of
linear subspaces of rotationally symmetric, horizontally symmetric and dihedrally
symmetric binary Steinhaus triangles. We obtain simple explicit bases for each of
them by using elementary properties of the binomial coeﬃcients. A Steinhaus graph
is a simple graph with an adjacency matrix whose upper-triangular part is a binary
Steinhaus triangle. A Steinhaus graph is said to be even or odd if all its vertex
degrees are even or odd, respectively. One of the main results of this paper is the
existence of an isomorphism between the linear subspace of even Steinhaus graphs
and a certain linear subspace of dihedrally symmetric binary Steinhaus triangles.
This permits us to give, in the second part of this paper, an explicit basis for even
Steinhaus graphs and for the vector space of parity-regular Steinhaus graphs, that
is the linear subspace of Steinhaus graphs that are even or odd. Finally, in the last
part of this paper, we consider the generalized Pascal triangles, that are triangles of
zeroes and ones, that point up now, and always with the same local rule than the
Pascal triangle modulo 2. New simple bases for each linear subspace of symmetric
generalized Pascal triangles are deduced from the results of the ﬁrst part.

MSC2010: 05B30, 05A15, 05A10, 11A99, 11B75, 11B50, 11B65, 11B85, 05C50, 05C30.

Keywords: Steinhaus triangles, symmetric triangles, symmetric sequences, rotational
symmetry, dihedral symmetry, binomial coeﬃcients, Steinhaus graphs, parity-regular
graphs, even graphs, generalized Pascal triangles.

∗E-mail address: jonathan.chappelon@umontpellier.fr

1

Contents

1 Introduction 2

2 Preliminary results 6
2.1 Generating index sets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.2 Derived and antiderived sequences . . . . . . . . . . . . . . . . . . . . . . . 9

3 Rotationally symmetric Steinhaus triangles 10
3.1 Characterizations of RST (n) . . . . . . . . . . . . . . . . . . . . . . . . . 10
3.2 Generating index sets of RST (n) . . . . . . . . . . . . . . . . . . . . . . . 11
3.3 Bases of RST (n) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13

4 Horizontally symmetric Steinhaus triangles 18
4.1 Characterizations of HST (n) . . . . . . . . . . . . . . . . . . . . . . . . . 18
4.2 Generating index set of HST (n) . . . . . . . . . . . . . . . . . . . . . . . . 21
4.3 Bases of HST (n) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

5 Dihedrally symmetric Steinhaus triangles 24
5.1 Characterizations of DST (n) . . . . . . . . . . . . . . . . . . . . . . . . . 24
5.2 Generating index sets of DST (n) . . . . . . . . . . . . . . . . . . . . . . . 26
5.3 Basis of DST (n) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 28

6 Parity-regular Steinhaus graphs 32

7 Symmetric generalized Pascal triangles 41

8 Generalizations and open problems 47
8.1 Symmetric binary tetrahedra . . . . . . . . . . . . . . . . . . . . . . . . . . 47
8.2 Symmetric triangles in Z/mZ . . . . . . . . . . . . . . . . . . . . . . . . . 49

References 50

1 Introduction

A binary Steinhaus triangle (or Steinhaus triangle for short) of size n is a triangle
(ai,j)1⩽i⩽j⩽n of 0’s and 1’s verifying the same local rule than the Pascal triangle mod-
ulo 2, that is,
 ai,j ≡ ai−1,j−1 + ai−1,j (mod 2), (LR)

for all integers i, j such that 2 ⩽ i ⩽ j ⩽ n. Note that (0) and (1) are the Steinhaus
triangles of size 1 and ∅ is the Steinhaus triangle of size 0. An example of Steinhaus
triangle of size 7 is depicted in Figure 1.
It is clear that a Steinhaus triangle (ai,j)1⩽i⩽j⩽n is completely determined by its ﬁrst
row (a1,j)1⩽j⩽n. Indeed, by induction on i and using (LR), we obtain that

ai,j ≡
 i−1∑

k=0
 (i − 1
k
 )
a1,j−k (mod 2), (1)

2

0 0 1 0 1 0 0
0 1 1 1 1 0
1 0 0 0 1
1 0 0 1
1 0 1
1 1
0

Figure 1: A Steinhaus triangle of size 7

for all integers i, j such that 1 ⩽ i ⩽ j ⩽ n, where the binomial coeﬃcient (a
b) is the
coeﬃcient of the monomial X b in the expansion of (1 + X)
a, for all non-negative integers
a and b such that b ⩽ a. In the sequel, the Steinhaus triangle whose ﬁrst row is the
sequence S is denoted by ∇S. The Steinhaus triangle in Figure 1 is then ∇(0010100).
Since the set ST (n) of binary Steinhaus triangles of size n is closed under addition
modulo 2, it follows that ST (n) is a vector space over Z/2Z. Moreover, since a Steinhaus
triangle is uniquely determined by its ﬁrst row, the dimension of ST (n) is n, for all
non-negative integers n.
This kind of binary triangles has been introduced by Hugo Steinhaus in his problem
book [26, 27], where he posed, as an unsolved problem, the following

Question. Does there exist, for every non-negative integer n such that n ≡ 0 or 3 mod 4,
a Steinhaus triangle of size n containing as many 0’s as 1’s?

The Steinhaus triangle ∇(0010100) depicted in Figure 1 solves this problem for n = 7,
since it contains 14 zeroes and 14 ones. Note that, since a triangle of size n contains (
n+1
2 )

elements, the condition n ≡ 0 or 3 mod 4 is a necessary and suﬃcient condition for having
a triangle of size n with an even number of terms. The Steinhaus problem was solved for
the ﬁrst time by Heiko Harborth in 1972 [23]. Since then, many solutions of this problem
have appeared in the litterature [21, 22, 20, 13]. Generalizations of this problem in Z/mZ,
for all m ⩾ 2, can be found in [24, 9, 11, 14] and in higher dimensions in [12].
The local rule (LR) can also be written as

ai−1,j−1 ≡ ai−1,j + ai,j (mod 2) or ai,j ≡ ai−1,j + ai−1,j−1 (mod 2),

for all integers i, j such that 2 ⩽ i ⩽ j ⩽ n. This is the reason why the 120 degrees
rotation and the horizontal reﬂection of a Steinhaus triangle are also Steinhaus triangles,
of the same size. We denote by r and h the corresponding automorphisms of ST (n), that
are, r : ST (n) −→ ST (n)
(ai,j)1⩽i⩽j⩽n ↦−→ (aj−i+1,n−i+1)1⩽i⩽j⩽n
and h : ST (n) −→ ST (n)
(ai,j)1⩽i⩽j⩽n ↦−→ (ai,n−j+i)1⩽i⩽j⩽n
for all non-negative integers n. These automorphisms verify the following identities

r3 = h
2 = hrhr = idST (n),

where idST (n) is the identity map on ST (n). Therefore, the subgroup ⟨r, h⟩ generated by
r and h, of the automorphism group of ST (n), is isomorphic to the dihedral group D3.

3

This induces a faithful representation of D3 on ST (n), for all non-negative integers n. In
the sequel, the automorphism subgroup ⟨r, h⟩ is simply denoted by D3. For instance, for
S = (11001) and for all g ∈ D3, the Steinhaus triangles g (∇S) are depicted in Figure 2.

1 1 0 0 1
0 1 0 1
1 1 1
0 0
0
 1 1 1 0 0
0 0 1 0
0 1 1
1 0
1
 0 0 1 0 1
0 1 1 1
1 0 0
1 0
1
 1 0 0 1 1
1 0 1 0
1 1 1
0 0
0
 1 0 1 0 0
1 1 1 0
0 0 1
0 1
1
 0 0 1 1 1
0 1 0 0
1 1 0
0 1
1

∇S r (∇S) r2 (∇S) h (∇S) rh (∇S) r2h (∇S)

Figure 2: Action of D3 on ∇(11001)

For any subgroup G of D3 and any non-negative integer n, we consider the linear
subspace of invariant triangles of ST (n) under G, that is,

ST (n)
G = {∇ ∈ ST (n) | ∀g ∈ G, g (∇) = ∇} .

It is well known that there are exactly 6 subgroups of D3, that are {idST (n)}, ⟨h⟩, ⟨rh⟩,
⟨r2h⟩, ⟨r⟩ and D3. Obviously, we have ST (n)
G = ST (n) for the trivial subgroup G ={idST (n)}. Moreover, by the linear maps

ST (n)⟨h⟩ −→ ST (n)
⟨rh⟩

∇ ↦−→ r2 (∇)

and ST (n)
⟨h⟩ −→ ST (n)⟨r2h⟩

∇ ↦−→ r (∇)

it is clear that the three linear subspaces ST (n)
⟨h⟩, ST (n)
⟨rh⟩ and ST (n)⟨r2h⟩ are iso-
morphic to each other. Therefore, for all non-negative integers n, we only consider the
linear subspaces ST (n)⟨h⟩, ST (n)
⟨r⟩ and ST (n)
D3, that will be denoted by HST (n),
RST (n) and DST (n), respectively, in the sequel of this paper. Obviously, these vector
spaces simply correspond to ker (h − idST (n)), ker (
r − idST (n)) and ker (r − idST (n)) ∩
ker (
h − idST (n))
, respectively.
A Steinhaus triangle ∇ of HST (n), RST (n) or DST (n) is said to be horizon-
tally symmetric, rotationally symmetric or dihedrally symmetric, respectively, and veriﬁes
h (∇) = ∇, r (∇) = ∇ or r (∇) = h (∇) = ∇, respectively. Examples of such symmetric
Steinhaus triangles appear in Figure 3.

1 1 0 0 1 1
0 1 0 1 0
1 1 1 1
0 0 0
0 0
0
 1 0 0 1 1 1
1 0 1 0 0
1 1 1 0
0 0 1
0 1
1
 0 1 1 1 1 0
1 0 0 0 1
1 0 0 1
1 0 1
1 1
0

Figure 3: Triangles of HST (6), RST (6) and DST (6).

In [3], it was proved that

• dim HST (n) = ⌈ n
2 ⌉
,
 4

• dim RST (n) = ⌊ n
3 ⌋ + δ1,(n mod 3),

• dim DST (n) = ⌊ n+3
6 ⌋ + δ1,(n mod 6),

for all non-negative integers n, where δi,(n mod j) is equal to 1, if n ≡ i mod j, and 0
otherwise. Bases of HST (n), RST (n) and DST (n), for all non-negative integers n, are
obtained in [7]. In this paper, we give new bases, for each of these three linear subspaces,
which are simpler than those mentioned. They are obtained by considering elementary
properties of generalized binomial coeﬃcients.
A Steinhaus graph of order n ⩾ 1 is a simple graph whose adjacency matrix has an
upper-triangular part which is a binary Steinhaus triangle of size n − 1. For any sequence
S = (a1, a2, . . . , an−1) of 0’s and 1’s of length n − 1, its associated Steinhaus graph G (S)
is the simple graph of order n whose adjacency matrix M (S) = (ai,j)1⩽i,j⩽n veriﬁes

i) ai,j = aj,i, for all i, j ∈ {1, . . . , n}, (symmetry)

ii) ai,i = 0, for all i ∈ {1, . . . , n}, (diagonal of zeroes)

iii) a1,j = aj−1, for all j ∈ {2, . . . , n − 1}, (sequence S)

iv) ai,j = ai−1,j−1 + ai−1,j, for all integers i, j such that 2 ⩽ i < j ⩽ n, (local rule of ∇S)

where {x, . . . , y} denotes the set of integers {i ∈ Z | x ⩽ i ⩽ y}, for any integers x and
y. For example, for S = (0010100), the Steinhaus graph G (S) and its adjacency matrix
M (S) are depicted in Figure 4.
 1

2
3
4

5
 6 7 8
 0 0
0 0

0
 1

1
 0

0
 1

1
 0

0
 0

0
 0 0
0 1

1
 1

1
 1

1
 1

1
 0

0
 0 1
1 0

0
 0

0
 0

0
 1

1
 0 1
1 0

0
 0

0
 1

1
 0 1
1 0

0
 1

1
 0 1
1 1

1 0 0
0 0

G (0010100) M (0010100)

Figure 4: The Steinhaus graph G (0010100) and its adjacency matrix M (0010100)

The set of Steinhaus graphs of order n is denoted by SG(n), for all positive integers n.
It is clear that there is a natural correspondence between SG(n) and ST (n−1). Therefore,
for all positive integers n, the set SG(n) is a vector space over Z/2Z of dimension n − 1.
The family of Steinhaus graphs has been introduced in [24]. In [15], it was proved
that any simple graph of order n is isomorphic to an induced subgraph of a Steinhaus
graph of order (
n
2) + 1. A general problem on Steinhaus graphs is to characterize those, or
their associated binary sequences, having a given graph property such as connectedness,
planarity, bipartition, regularity, etc. It is easy to see that a Steinhaus graph is either
connected or totally disconnected (the edgeless graph). The bipartite Steinhaus graphs
are characterized in [17, 18, 8] and the planar ones in [19]. In [16, 2], it was conjectured
that there is only one regular Steinhaus graph of odd degree, the complete graph K2 =

5

G (1), and that the regular Steinhaus graphs of even degrees are the edgeless graphs
Kn = G (00 · · · 0) of orders n, for all positive integers n, and the non-trivial graphs
G (110110 · · · 110) of orders n = 3m + 1, for all positive integers m. This conjecture was
veriﬁed up to 117 vertices in [1] and up to 1500 vertices in [10] for the odd case.
A Steinhaus graph is said to be even (resp. odd) if every vertex has even degree (resp.
odd degree). Examples of even and odd Steinhaus graphs are given in Figure 5. For all
positive integers n, the sets of even Steinhaus graphs and of odd Steinhaus graphs of order
n are denoted by ESG(n) and OSG(n), respectively. In [16], it was proved that ESG(n)
is a linear subspace of SG(n) of dimension ⌊ n−1
3 ⌋, for all positive integers n, and OSG(n)
is an aﬃne subspace of direction ESG(n), for all even numbers n. Obviously, since the
number of vertices of odd degrees is always even, OSG(n) = ∅ when n is odd. According
to the terminology used in [1], a parity-regular Steinhaus graph is a Steinhaus graph that
is even or odd. For all positive integers n, the set of parity-regular Steinhaus graphs of
order n is denoted by PRSG(n), that is, PRSG(n) = ESG(n) ∪ OSG(n). As shown in
[1], the set PRSG(n) is a linear subspace of SG(n) of dimension ⌈ n
3 ⌉ − δ1,(n mod 2), for all
positive integers n. Bases of PRSG(n) have been computed, for n ⩽ 30, in [1]. In this
paper, we determine bases of ESG(n) and PRSG(n), for all positive integers n. This is
achieved by showing that the vector space ESG(n) is isomorphic to a particular linear
subspace of DST (2n − 1), for all positive integers n.

1

2

3

4

5
 6
 7
 8
 0 1
1 0

0
 0

0
 1

1
 0

0
 0

0
 0

0
 0 1
1 0

0
 1

1
 1

1
 0

0
 0

0
 0 1
1 1

1
 0

0
 1

1
 0

0
 0 0
0 1

1
 1

1
 1

1
 0 1
1 0

0
 0

0
 0 1
1 0

0 0 1
1 0
 1

2

3

4

5
 6
 7
 8
 0 1
1 0

0
 0

0
 1

1
 0

0
 0

0
 1

1
 0 1
1 0

0
 1

1
 1

1
 0

0
 1

1
 0 1
1 1

1
 0

0
 1

1
 1

1
 0 0
0 1

1
 1

1
 0

0
 0 1
1 0

0
 1

1
 0 1
1 1

1 0 0
0 0

G (1001000) M (1001000) G (1001001) M (1001001)

Figure 5: Even and odd Steinhaus graphs

This paper is organized as follows. In Section 2, some basic properties on generating
index sets of Steinhaus triangles and on derived and antiderived binary sequences are
introduced. After that, for all non-negative integers n, the linear subspaces RST (n),
HST (n) and DST (n) are studied in detail, with the determination of generating index
sets and bases for each of them: for RST (n) in Section 3, for HST (n) in Section 4 and for
DST (n) in Section 5. For any positive integer n, a certain correspondence between the
vector spaces ESG(n) and DST (2n−1) is established and bases of ESG(n) and PRSG(n)
are given in Section 6. In Section 7, we deal with symmetric generalized Pascal triangles,
that are binary triangles which point up and always with the same local rule. Finally,
open problems on generalizations of symmetric binary triangles are proposed in Section 8.

2 Preliminary results

We introduce, in this section, the notions of generating index sets of Steinhaus triangles
and of derived and antiderived binary sequences.

6

2.1 Generating index sets

Let n be a positive integer. We denote by ∇(n) the index set of Steinhaus triangles of
size n, that is, ∇(n) = {(i, j) ∈ N2 ∣
∣ 1 ⩽ i ⩽ j ⩽ n} .

A subset G of ∇(n) is said to be a generating index set of ST (n) if the knowledge of the
values ai,j, for all (i, j) ∈ G, uniquely determines the whole Steinhaus triangle (ai,j)1⩽i⩽j⩽n,
i.e., if the linear map πG : ST (n) −→ {0, 1}G

(ai,j)1⩽i⩽j⩽n ↦−→ (ai,j)(i,j)∈G

is an isomorphism. Since dim ST (n) = n, we deduce that the cardinality of a generating
index set of ST (n) is always n. From (1), it is clear that the set of top row indices of a
Steinhaus triangle of size n, that is,

G1 = {(1, 1), (1, 2), . . . , (1, n)} ,

is a generating index set of ST (n). Note that πG1 −1(S) = ∇S, for all S ∈ {0, 1}G1. It
follows that the set G is a generating index set of ST (n) if and only if the linear map
πG ◦ πG1 −1 : {0, 1}G1 → {0, 1}G is an isomorphism. For instance, the 16 generating index
sets of ST (3) (4 up to the action of the dihedral group D3) are depicted in Figure 6, where
a disk is either black if its position is in the generating index set or white otherwise.

1 1 1

0 0

0
 1 0 0

1 0

1
 0 0 1

0 1

1

{(1 ; 1) ; (1 ; 2) ; (1 ; 3) } {(1 ; 1) ; (2 ; 2) ; (3 ; 3) } {(1 ; 3) ; (2 ; 3) ; (3 ; 3) }

0 0 0

0 0

0
 0 0 0

0 0

0
 0 0 0

0 0

0
 0 0 0

0 0

0
 0 0 0

0 0

0
 0 0 0

0 0

0

{(1 ; 1) ; (1 ; 2) ; (2 ; 3) } {(1 ; 2) ; (2 ; 2) ; (3 ; 3) } {(1 ; 3) ; (2 ; 2) ; (2 ; 3) } {(1 ; 2) ; (1 ; 3) ; (2 ; 2) } {(1 ; 1) ; (2 ; 2) ; (2 ; 3) } {(1 ; 2) ; (2 ; 3) ; (3 ; 3) }

0 0 0

0 0

0
 0 0 0

0 0

0
 0 0 0

0 0

0
 0 0 0

0 0

0
 0 0 0

0 0

0
 0 0 0

0 0

0

{(1 ; 1) ; (1 ; 2) ; (3 ; 3) } {(1 ; 3) ; (2 ; 2) ; (3 ; 3) } {(1 ; 1) ; (1 ; 3) ; (2 ; 3) } {(1 ; 2) ; (1 ; 3) ; (3 ; 3) } {(1 ; 1) ; (1 ; 3) ; (2 ; 2) } {(1 ; 1) ; (2 ; 3) ; (3 ; 3) }

0 0 0

0 0

0

{(1 ; 2) ; (2 ; 2) ; (2 ; 3) }
 Figure 6: Generating index sets of ST (3)

Since the sets of right side indices,

Gr = {(1, n), (2, n), . . . , (n, n)} ,

7

and left side indices, Gl = {(1, 1), (2, 2), . . . , (n, n)} ,

of a Steinhaus triangle ∇ of size n can be seen as the sets of top row indices of the Steinhaus
triangles r (∇) and r2 (∇), respectively, it follows that Gr and Gl are generating index
sets of ST (n) too. Therefore, each element of a Steinhaus triangle can be expressed in
function of the terms of its ﬁrst row, of its right side or of its left side.
For any non-negative integers a and b such that b ⩽ a, the binomial coeﬃcient (a
b)

is the coeﬃcient of the monomial X b in the polynomial expansion of the binomial power
(1+X)
a. It corresponds to the number of ways to choose b elements in a set of a elements.
Here, we extend this notation by supposing that (a
b) = 0, for all integers b such that b < 0
or b > a. For this generalization, the Pascal identity
(a
b
) = (a − 1
b − 1
) + (
a − 1
b
 )

holds, for all positive integers a and all integers b.

Lemma 2.1. Let (ai,j)1⩽i⩽j⩽n be a binary Steinhaus triangle of size n. Then, we have

ai,j ≡
 n∑

k=1
 (i − 1
j − k
)
a1,k ≡
 n∑

k=1
 (
n − j
k − i
)
ak,n ≡
 n∑

k=1
 (j − i
k − i

)
ak,k (mod 2),

for all integers i, j such that 1 ⩽ i ⩽ j ⩽ n.

Proof. As for (1), by induction on i and using the local rule (LR).

Proposition 2.2. Let G = {(i1, j1), (i2, j2), . . . , (in, jn)} be a subset of ∇(n) whose car-
dinality is |G| = n. Then, the set G is a generating index set of ST (n) if and only if
det(MG) ≡ 1 mod 2, where
 MG = ((
ik − 1
jk − l
))
1⩽k,l⩽n .

Proof. From Lemma 2.1, we know that

aik,jk ≡
 n∑

l=1
 (
ik − 1
jk − l
)a1,l (mod 2),

for all k ∈ {1, . . . , n}. It follows that

πG ◦ πG1 −1(S) ≡ S.MGt (mod 2),

for all S ∈ {0, 1}
G1. Finally, the linear map πG ◦ πG1 −1 is an isomorphism if and only if
det(MG) ≡ 1 mod 2.

The notion of generating index sets and the result of Proposition 2.2 appear in a more
general context in [5, 6], where it is also proved that the set of generating index sets of
ST (n) deﬁne a matroid called the Pascal matroid modulo 2. Note that a generating index
set is simply called a generating set in [5, 6].
The deﬁnition of generating index sets can be extended to any linear subspace V of
ST (n). A subset G of ∇(n) is said to be a generating index set of V if the linear map

πG : V −→ {0, 1}
G

(ai,j)1⩽i⩽j⩽n ↦−→ (ai,j)(i,j)∈G
is an isomorphism. Note that |G| = dim V, for any generating index set G of V. In this
paper, we consider generating index sets of the linear subspaces RST (n), HST (n) and
DST (n), for all non-negative integers n.
 8

2.2 Derived and antiderived sequences

Let S = (aj)1⩽j⩽n be a sequence of 0’s and 1’s of length n.
The derived sequence ∂S of S is the sequence

∂S = (aj + aj+1 mod 2)1⩽j⩽n−1 (2)

of length n − 1, when n ⩾ 2, and the empty sequence, when n ⩽ 1. The iterated derived
sequences ∂iS of S are recursively deﬁned by ∂iS = ∂(∂i−1S), for all i ⩾ 1, with ∂0S = S.
The Steinhaus triangle ∇S can then be seen as the collection (∂iS)0⩽i⩽n−1, where, for
every i ∈ {1, . . . , n}, the ith row of ∇S corresponds to the derived sequence ∂i−1S.
The set of binary sequences of length n can be seen as a vector space over Z/2Z of
dimension n. Indeed, for two binary sequences S1 = (aj)1⩽j⩽n and S2 = (bj)1⩽j⩽n of
the same length n ⩾ 1, their sum is the sequence S1 + S2 = (aj + bj)1⩽j⩽n of length n.
Therefore, it is clear that the derivation map ∂ is linear, i.e., ∂(S1 + S2) = ∂S1 + ∂S2 for
all binary sequences S1 and S2 of same length.
For any i ∈ {1, . . . , n+1} and any x ∈ {0, 1}, the antiderived sequence of S = (aj)1⩽j⩽n
whose ith term is x is the sequence ∫
i,x S = (bj)1⩽j⩽n+1 of length n + 1 deﬁned by

bj =
 



 x +
 i−1∑

k=j ak (mod 2) for j ∈ {1, . . . , i − 1},

x for j = i,

x +
 j−1∑

k=i ak (mod 2) for j ∈ {i + 1, . . . , n + 1}.

In a more concise way, we have

bj = x +
 i−1∑

k=1 ak +
 j−1∑

k=1 ak (mod 2), (3)

for all j ∈ {1, . . . , n + 1}. Further, it is straightforward to obtain a fundamental theorem
of calculus.
For any non-negative integer n, the constant sequence of length n equal to x is denoted
by (x)n. For n = 1, the sequence (x)1 is simply denoted (x).

Proposition 2.3. Let S = (aj)1⩽j⩽n be a binary sequence of length n. For any i ∈
{1, . . . , n + 1} and any x ∈ {0, 1}, we have that

i) ∂ (∫
i,x S) = S,

ii) ∫
i,x (∂S) = S + (ai + x mod 2)n.

Proof. For i), let ∫

i,x = (bj)1⩽j⩽n+1 and ∂ (∫

i,x S) = (cj)1⩽j⩽n. By deﬁnition, from (2)
and (3), we obtain that

cj ≡ bj + bj+1 ≡
 (

x +
 i−1∑

k=1 ak +
 j−1∑

k=1 ak
)
 +
 (
x +
 i−1∑

k=1 ak +
 j∑

k=1 ak
)
 ≡ aj (mod 2),

for all j ∈ {1, . . . , n}. Therefore ∂ (∫
i,x S) = S.

9

Now, for ii), let ∂S = (bj)1⩽j⩽n−1 and ∫
i,x (∂S) = (cj)1⩽j⩽n. By deﬁnition, from (2)
and (3), we obtain that

cj ≡ x +
 i−1∑

k=1 bk +
 j−1∑

k=1 bk ≡ x +
 i−1∑

k=1(ak + ak+1) +
 j−1∑

k=1(ak + ak+1)

≡ x + (a1 + ai) + (a1 + aj) ≡ aj + (ai + x) (mod 2),

for all j ∈ {1, . . . , n}. Therefore ∫

i,x (∂S) = S + (ai + x mod 2)n.

A similar result has been obtained for inﬁnite binary sequences in [25]. It follows that
every binary sequence S of length n admits only two diﬀerent antiderived sequences, that
are, the sequences ∫

i,0 S and ∫
i,1 S for some i ∈ {1, . . . , n + 1}. Moreover, it is easy to
see that ∫
i,0 S + ∫
i,1 S = (1)n. For example, the sequence S = (0100) admits the two
antiderived sequences (00111) and (11000).

3 Rotationally symmetric Steinhaus triangles

In this section, after characterizing rotationally symmetric Steinhaus triangles, we deter-
mine, for all non-negative integers n, generating index sets and bases of RST (n).

3.1 Characterizations of RST (n)

First, by deﬁnition of the automorphism r, we have

r ((ai,j)1⩽i⩽j⩽n) = (aj−i+1,n−i+1)1⩽i⩽j⩽n = ∇(aj,n)1⩽j⩽n,

for any Steinhaus triangle (ai,j)1⩽i⩽j⩽n = ∇(a1,j)1⩽j⩽n. Therefore, a Steinhaus triangle
(ai,j)1⩽i⩽j⩽n is rotationally symmetric if and only if its ﬁrst row (a1,j)1⩽j⩽n and its right
side (aj,n)1⩽j⩽n correspond.

Proposition 3.1. The Steinhaus triangle (ai,j)1⩽i⩽j⩽n is rotationally symmetric if and
only if (a1,j)1⩽j⩽n = (aj,n)1⩽j⩽n.

For two binary sequences S1 = (a1, a2, . . . , an1) and S2 = (b1, b2, . . . , bn2) of length n1
and n2, respectively, we denote by S1 · S2 the concatenated sequence of length n1 + n2
deﬁned by S1 · S2 = (a1, a2, . . . , an1, b1, b2, . . . , bn2).
Let H be the linear map that assigns, to each Steinhaus triangle of order n ⩾ 3, its
subtriangle of order n − 3 obtained by removing its ﬁrst row and its left and right sides,
that is, H : ST (n) −→ ST (n − 3)
(ai,j)1⩽i⩽j⩽n ↦−→ (a1+i,2+j)1⩽i⩽j⩽n−3

Note that the linear map H is surjective. Indeed, for any ∇S′ ∈ ST (n − 3), it is easy
to verify that ∇S′ = H (∇S) if and only if S is one of the eight sequences of the form
S = (x1) · ∫

i,x S′ · (x2), where x1, x2 ∈ {0, 1} and ∫

i,x S′ is one of the two antiderived
sequences of S′. Examples of a Steinhaus triangle ∇S and its subtriangle H (∇S) are
depicted in Figure 7.
 10

1 0 1 1 1 1 0
1 1 0 0 0 1
0 1 0 0 1
1 1 0 1
0 1 1
1 0
1

1 0 0 0
1 0 0
1 0
1

Figure 7: H (∇(1011110)) = ∇(1000)

For any binary sequence S = (aj)1⩽j⩽n, we denote by σ(S) its sum σ(S) = ∑n
j=1 aj,
i.e., the number of ones in S, and by σ2(S) its sum modulo 2.
For any positive integer n ⩾ 3, by deﬁnition of RST (n) and H, it is clear that
H (RST (n)) ⊂ RST (n − 3). The precise relationship between a rotationally symmetric
Steinhaus triangle ∇S and its subtriangle H (∇S) is given in the following

Proposition 3.2. Let S be a ﬁnite binary sequence of length n ⩾ 3. The Steinhaus trian-
gle ∇S is rotationally symmetric if and only if H (∇S) = ∇S′ is rotationally symmetric
and S = (σ2 (S′)) · ∫
i,x S′ · (σ2 (S′)), for some i ∈ {1, . . . , n − 2} and some x ∈ {0, 1}.

Proposition 3.2 appears in [4] in a more general context. For the convenience of the
reader, a proof is given here.

Proof. Let ∇S = (ai,j)1⩽i⩽j⩽n ∈ ST (n) such that ∇S′ = H(∇S) = (a1+i,2+j)1⩽i⩽j⩽n−3 ∈
RST (n − 3). Since ∇S′ is rotationally symmetric, its top row (a2,j)3⩽j⩽n−1, its right side
(ai,n−1)2⩽i⩽n−2 and the reverse of its left side (an−i,n−i+1)2⩽i⩽n−2 correspond by Propo-
sition 3.1. Moreover, since (a1,j)2⩽j⩽n−1, (ai,n)2⩽i⩽n−1 and (an−i+1,n−i+1)2⩽i⩽n−1 are an-
tiderived sequences of the sequences (a2,j)3⩽j⩽n−1, (ai,n−1)2⩽i⩽n−2 and (an−i,n−i+1)2⩽i⩽n−2,
respectively, we deduce that they correspond if and only if there exist i1, i2 ∈ {2, . . . , n−1}
such that a1,i1 = ai1,n and a1,i2 = an−i2+1,n−i2+1. Since a1,1 ≡ a1,2 + a2,2 mod 2 and
a1,n ≡ a1,n−1 + a2,n mod 2, it follows from Proposition 3.1 again that the Steinhaus trian-
gle ∇S is rotationally symmetric if and only if a1,1 = a1,n ≡ a1,2 + a1,n−1 mod 2. Finally,
using the local rule (LR), we have that

σ (S′) =
 n−1∑

j=3 a2,j ≡
 n−1∑

j=3 a1,j−1 + a1,j ≡ a1,2 + a1,n−1 (mod 2).

This completes the proof.

3.2 Generating index sets of RST (n)

We are now ready to determine generating index sets of the linear subspace of rotationally
symmetric Steinhaus triangles, for every non-negative integer n.

Theorem 3.3. Let n be a non-negative integer. The set

GR = {
(i, ji) ∣
∣
∣ i ∈ {
1, . . . , ⌊n
3
 ⌋ + δ1,(n mod 3)}} ,

where ji ∈ {2i, . . . , n − i} for all i ∈ {
1, . . . , ⌊ n
3 ⌋} and j n+2
3 = 2n+1
3 when n ≡ 1 mod 3, is
a generating index set of RST (n).
 11

Proof. By induction on n.
For n = 0 and n = 2, it is clear that ∅ and ∇(00) are the only rotationally symmetric
Steinhaus triangles of sizes 0 and 2. Therefore, the empty set ∅ is a generating index set
of RST (0) and RST (2). For n = 1, the Steinhaus triangles ∇(0) and ∇(1) are both
rotationally symmetric and thus the set {(1, 1)} is a generating index set of RST (1).
Suppose now that the result is true for the sets of rotationally symmetric Steinhaus
triangles of size strictly lesser than n ⩾ 3. Let m = ⌊ n
3 ⌋ + δ1,(n mod 3). We consider the
subset H (GR) ⊂ ∇(n − 3) deﬁned by

H (GR) = {(i − 1, ji − 2) | i ∈ {2, . . . , m}}

and the linear maps f1 and f2 deﬁned by

f1 : RST (n) −→ {0, 1} × RST (n − 3)
∇S = (ai,j)1⩽i⩽j⩽n ↦−→ (a1,j1, H (∇S))

and f2 : {0, 1} × RST (n − 3) −→ {0, 1}
m

(x, ∇S′) ↦−→ (x) · πH(GR) (∇S′)

Then, for any (ai,j)1⩽i⩽j⩽n ∈ RST (n), we have

f2f1 ((ai,j)1⩽i⩽j⩽n) = f2 (a1,j1, (a1+i,2+j)1⩽i⩽j⩽n−3)
= (a1,j1) · πH(GR) ((a1+i,2+j)1⩽i⩽j⩽n−3)
= (a1,j1) · (ai,ji)2⩽i⩽m
= (ai,ji)1⩽i⩽m = πGR ((ai,j)1⩽i⩽j⩽n) .

Therefore f2f1 = πGR. From Proposition 3.2, we know that f1 is an isomorphism whose
inverse is deﬁned by f1−1 (x, ∇S′) = ∇
((σ2(S′)) · ∫

j1−1,x S′ · (σ2(S′))
), for all (x, ∇S′) ∈
{0, 1} × RST (n − 3). Moreover, since we have

1 ⩽ i − 1 ⩽ n − 3
3 and 2(i − 1) ⩽ ji − 2 ⩽ (n − 3) − (i − 1),

for all i ∈ {2, . . . , ⌊ n
3 ⌋}, and

m − 1 = (n − 3) + 2
3 and jm − 2 = 2(n − 3) + 1
3 ,

when n ≡ 1 mod 3, the set H (GR) is a generating index set of RST (n − 3) by induction
hypothesis. Therefore πH(GR) and thus f2 are isomorphisms. Finally, since the linear map
πGR = f2f1 is an isomorphism, the set GR is a generating index set of RST (n).

Corollary 3.4. Let n be a non-negative integer. The set

GR := {(
i, n − ⌊ n
3
 ⌋) ∣
∣
∣ i ∈ {
1, . . . , ⌊n
3
 ⌋ + δ1,(n mod 3)}}

is a generating index set of RST (n).

Proof. From Theorem 3.3, since 2i ⩽ n − ⌊ n
3 ⌋ ⩽ n − i for all i ∈ {1, . . . , ⌊ n
3 ⌋} and
n − ⌊ n
3 ⌋ = 2n+1
3 when n ≡ 1 mod 3.

Since the dimension of RST (n) corresponds to the cardinality of a generating index
set GR, it is straightforward to obtain the following

Corollary 3.5. dim RST (n) = ⌊ n
3 ⌋ + δ1,(n mod 3), for all non-negative integers n.

12

3.3 Bases of RST (n)

In the end of this section, using the generating index sets GR introduced before, we
determine bases of the linear subspace of rotationally symmetric Steinhaus triangles.
First, we consider the linear map ρ : ST (n) −→ RST (n) deﬁned by ρ = r2+r+idST (n),
for all non-negative integers n. Obviously, this map is surjective since ρ(∇) = ∇, for all
∇ ∈ RST (n). Moreover, as detailed below, all the terms of ρ (∇) can be expressed in
function of these of ∇.

Proposition 3.6. For all (ai,j)1⩽i⩽j⩽n ∈ ST (n), we have

ρ ((ai,j)1⩽i⩽j⩽n) = (ai,j + aj−i+1,n−i+1 + an−j+1,n+i−j mod 2)1⩽i⩽j⩽n .

Proof. First, by deﬁnition of r, we know that

r ((ai,j)1⩽i⩽j⩽n) = (aj−i+1,n−i+1)1⩽i⩽j⩽n ,

for all (ai,j)1⩽i⩽j⩽n ∈ ST (n). Thus, we obtain

r2 ((ai,j)1⩽i⩽j⩽n) = r ((aj−i+1,n−i+1)1⩽i⩽j⩽n) = (an−j+1,n+i−j)1⩽i⩽j⩽n ,

for all (ai,j)1⩽i⩽j⩽n ∈ ST (n). The result follows.

For any non-negative integer n, let Un be the Steinhaus triangle of size n deﬁned by

Un = ρ (∇(1)n) .

It is clear that U0 = ∅, U1 = ∇(1), U2 = ∇(00) and Un = ∇(011 · · · 110) for n ⩾ 3, since

Un = ρ (∇(1)n) = ∇(1 · · · 1) + ∇(10 · · · 0) + ∇(0 · · · 01) = ∇((1 · · · 1) + (10 · · · 0) + (0 · · · 01)),

for all positive integers n. The Steinhaus triangles Un are depicted in Figure 8, for the
ﬁrst few values of n. Moreover, an explicit formula for the terms of Un is given in the
following

1 0 0
0
 0 1 0
1 1
0
 0 1 1 0
1 0 1
1 1
0
 0 1 1 1 0
1 0 0 1
1 0 1
1 1
0
 0 1 1 1 1 0
1 0 0 0 1
1 0 0 1
1 0 1
1 1
0

Figure 8: Un for n ∈ {1, . . . , 6}

Proposition 3.7. For any non-negative integer n, we have

Un = (δi,1 + δi,j + δj,n mod 2)1⩽i⩽j⩽n .

13

Proof. First, if we denote ∇(1)n = (ai,j)1⩽i⩽j⩽n and Un = ρ (∇(1)n) = (bi,j)1⩽i⩽j⩽n, we
know from Proposition 3.6 that

bi,j ≡ ai,j + aj−i+1,n−i+1 + an−j+1,n+i−j (mod 2),

for all integers i and j such that 1 ⩽ i ⩽ j ⩽ n. Moreover, it is clear that ∂i(1)n = (0)n−i,
for all i ∈ {1, . . . , n − 1}. Therefore, ∇(1)n = (δi,1)1⩽i⩽j⩽n. This leads to

bi,j ≡ δi,1 + δj−i+1,1 + δn−j+1,1 (mod 2),

for all integers i and j such that 1 ⩽ i ⩽ j ⩽ n. Finally, since δj−i+1,1 = δi,j and
δn−j+1,1 = δj,n, the result follows.

Corollary 3.8. H (Un) = ∇(0)n−3, for all positive integers n ⩾ 3.

Proof. Let Un = (ai,j)1⩽i⩽j⩽n. By deﬁnition of H and Proposition 3.7, we obtain that

H (Un) = (ai+1,j+2)1⩽i⩽j⩽n−3 = (δi+1,1 + δi+1,j+2 + δj+2,n mod 2)1⩽i⩽j⩽n−3 = ∇(0)n−3.

For any non-negative integer k such that 3k ⩽ n, we consider the iterated operator

Hk = HH · · · H︸ ︷︷ ︸
k times : ST (n) −→ ST (n − 3k)
(ai,j)1⩽i⩽j⩽n ↦−→ (ak+i,2k+j)1⩽i⩽j⩽n−3k

Using the operators H
k and the generating index set GR, we obtain a family of bases of
RST (n), for all non-negative integers n.

Theorem 3.9. Let n and m be non-negative integers such that m = ⌊ n
3 ⌋ + δ1,(n mod 3).
For every k ∈ {0, . . . , m − 1}, let ∇k ∈ RST (n) such that H
k (∇k) = Un−3k. Then, the
set {∇0, . . . , ∇m−1} is a basis of RST (n).

The proof is based on the following

Lemma 3.10. Let ∇ = (ai,j)1⩽i⩽j⩽n ∈ ST (n) such that Hk (∇) = Un−3k, for some
k ∈ {0, . . . , ⌊ n
3 ⌋ − 1
}. Then,

ai,n−⌊ n
3 ⌋ = { 1 for i = k + 1,
0 for i ∈ {k + 2, . . . , ⌊ n
3 ⌋} .

Moreover, when n ≡ 1 mod 3, if H⌊ n
3 ⌋ (∇) = U1 = (1), then a⌊ n
3 ⌋+1,n−⌊ n
3 ⌋ = 1.

Proof of Lemma 3.10. Let k ∈ {0, . . . , ⌊ n
3 ⌋ − 1
}. By deﬁnition of H
k and Proposition 3.7,
we deduce that

(ak+i,2k+j)1⩽i⩽j⩽n−3k = H
k (∇) = Un−3k = (δi,1 + δi,j + δj,n−3k mod 2)1⩽i⩽j⩽n−3k . (4)

Since k ⩽ ⌊ n
3 ⌋ − 1, we have

2k + 1 ⩽ 2 ⌊n
3
 ⌋ − 1 < n − ⌊n
3
 ⌋ < n − k.

14

It follows from (4) that

ai,n−⌊ n
3 ⌋ = ak+(i−k),2k+(n−⌊ n
3 ⌋−2k) ≡ δi−k,1 +δi−k,n−⌊ n
3 ⌋−2k +δn−⌊ n
3 ⌋−2k,n−3k (mod 2), (5)

for all integers i such that 1 ⩽ i − k ⩽ n − ⌊ n
3 ⌋ − 2k, i.e., k + 1 ⩽ i ⩽ n − ⌊ n
3 ⌋ − k. Since
k ⩽ ⌊ n
3 ⌋ − 1, we obtain that
 δn−⌊ n
3 ⌋−2k,n−3k = δk,⌊ n
3 ⌋ = 0. (6)

Moreover, this leads to
 n − ⌊n
3
 ⌋ − k ⩾ n − 2 ⌊n
3
 ⌋ + 1 ⩾ ⌊n
3
 ⌋ + 1

and δi−k,n−⌊ n
3 ⌋−2k = δi,n−⌊ n
3 ⌋−k = 0, (7)

for all integers i ⩽ ⌊ n
3 ⌋. Therefore, for all i ∈ {
k + 1, . . . , ⌊ n
3 ⌋}, we obtain from (5), (6)
and (7) that ai,n−⌊ n
3 ⌋ = δi−k,1 = δi,k+1.

This completes the proof when k ∈ {0, . . . , ⌊ n
3 ⌋ − 1
}.
Finally, when n ≡ 1 mod 3, it is clear that

(1) = U1 = H n−1
3 (∇) = (a n+2
3 , 2n+1
3
 ) = (a⌊ n
3 ⌋+1,n−⌊ n
3 ⌋
) .

This completes the proof.

Proof of Theorem 3.9. We consider the set

GR := {(
i, n − ⌊n
3
 ⌋) ∣
∣
∣ i ∈ {1, 2, . . . , m}} .

For any k ∈ {0, . . . , m − 1}, since H
k (∇k) = Un−3k, it follows from Lemma 3.10 that

πGR(∇k) = (∗, . . . , ∗
︸ ︷︷ ︸
k , 1, 0, . . . , 0
︸ ︷︷ ︸
m−k−1 ).

Therefore, the set {πGR(∇k) | k ∈ {0, . . . , m − 1}} is a basis of {0, 1}GR. Finally, since
GR is a generating index set of RST (n) by Corollary 3.4, we conclude that the set
{∇k | k ∈ {0, . . . , m − 1}} is a basis of RST (n).

Since Un−3k = ρ ((1)n−3k) by deﬁnition, for all non-negative integers n and k such that
3k ⩽ n, this leads to the following

Corollary 3.11. Let n and m be non-negative integers such that m = ⌊ n
3 ⌋ + δ1,(n mod 3).
For every k ∈ {0, . . . , m − 1}, let Sk be a binary sequence of length n such that ∂kSk =
(1)n−k. Then, the set {ρ (∇S0) , . . . , ρ (∇Sm−1)} is a basis of RST (n).

Proof. Let k ∈ {0, . . . , m − 1}. First, by deﬁnition of the linear map ρ, we know that
ρ (∇Sk) ∈ RST (n). Moreover, since ∂kSk = (1)n−k, it follows that

Hk (ρ (∇Sk)) = ρ (
Hk (∇Sk)
) = ρ (∇(1)n−3k) = Un−3k.

Therefore, from Theorem 3.9, the set {ρ (∇Sk) | k ∈ {0, . . . , m − 1}} is a basis of RST (n).

15

Binomial coeﬃcients (
a
b) have been deﬁned before for any non-negative integer a and
any integer b. Now, we extend this deﬁnition for negative integers a. For any integers a
and b, let (a
b) denote the integers recursively deﬁned by

• (
a
0) = 1, for all a ∈ Z,

• (
0
b) = 0, for all b ∈ N
∗,

• (
a
b) = (a−1
b−1) + (
a−1
b )
, for all a, b ∈ Z.

When a is non-negative, it corresponds with the previous deﬁnition. Moreover, for any
negative integer a, the following equality holds
(a
b
) = { 0 for b < 0,
(−1)
b(
b−a−1
b ) for b ⩾ 0.

In this paper, we mainly consider the inﬁnite Pascal matrix modulo 2, that is, the doubly
indexed sequence ((a
b)

2)

(a,b)∈Z2, where (a
b)

2 is the value of (a
b) mod 2. The ﬁrst few values

of this doubly inﬁnite sequence are shown in Figure 9, where the terms (a
0)

2 are in blue,
for all integers a, and the terms (0
b)

2 are in red, for all positive integers b.
For any integers k and l, let S
(n)
k,l be the subsequence of length n of the kth column of
the inﬁnite Pascal matrix modulo 2 deﬁned by

S
(n)
k,l = ((l + j − 1
k
 )

2
)
1⩽j⩽n = (( l
k
)

2, (l + 1
k
 )

2, . . . . . . , (
l + n − 1
k
 )

2
) .

For instance, the sequence S(7)
5,2 = ((j+1
5 )

2)
1⩽j⩽7 = (0001010) appears in yellow in Fig-
ure 9. Since we retrieve the local rule (LR) in the inﬁnite Pascal matrix modulo 2, it is
straightforward to obtain the following

Proposition 3.12. Let k and l be two integers and let n be a positive integer. Then,

∂iS(n)
k,l = S
(n−i)
k−i,l = ((l + j − 1
k − i
 )

2
)
1⩽j⩽n−i ,

for all i ∈ {0, . . . , n − 1} and

∇S(n)
k,l = (( l + j − i
k + 1 − i

)

2
)

1⩽i⩽j⩽n .

For instance, the Steinhaus triangle ∇S(7)
10,−10 = ∇(0000110) appears in green in Figure 9.
We are now ready for giving explicit bases of RST (n), for every non-negative integer
n, using Corollary 3.11 with binary sequences S(n)
k,l .

Theorem 3.13. Let n and m be non-negative integers such that m = ⌊ n
3 ⌋+δ1,(n mod 3). For

any integers l0, . . . , lm−1, the set {
ρ (∇S
(n)
0,l0) , . . . , ρ (∇S(n)
m−1,lm−1)} is a basis of RST (n).
Moreover, we have

ρ (∇S
(n)
k,lk
) = ((lk + j − i
k + 1 − i
) + (
lk + n − j
k + i − j
 ) + (lk + i − 1
k + j − n
) mod 2
)
1⩽i⩽j⩽n , (8)

for all k ∈ {0, . . . , m − 1}.
 16

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 0 0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0
1 0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0
1 1 0 0 0 0 0 0 1 1 0 0 0 0 0 0 0 0 0 0
1 0 1 0 0 0 0 0 1 0 1 0 0 0 0 0 0 0 0 0
1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0
1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0
1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 0 0 0 0
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0
1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0
1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1

1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0
1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 0 0 0 0
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 0 0 0 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 0 0 0
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0 0
1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1 0
1 1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1 1
1 0 0 0 1 0 0 0 0 0 0 0 0 0 0 0 1 0 0 0
1 1 0 0 1 1 0 0 0 0 0 0 0 0 0 0 1 1 0 0
1 0 1 0 1 0 1 0 0 0 0 0 0 0 0 0 1 0 1 0
1 1 1 1 1 1 1 1 0 0 0 0 0 0 0 0 1 1 1 1
1 0 0 0 0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0
1 1 0 0 0 0 0 0 1 1 0 0 0 0 0 0 1 1 0 0
1 0 1 0 0 0 0 0 1 0 1 0 0 0 0 0 1 0 1 0
1 1 1 1 0 0 0 0 1 1 1 1 0 0 0 0 1 1 1 1
1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0 1 0 0 0
1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0
1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 0
1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1

· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·
· · · · · ·

...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...
 ...

...

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0

1111111111111111111111111111111111111111
 0001010
 0000110

000101

00111

0100

110

01
1

Figure 9: The inﬁnite Pascal matrix modulo 2 with ((a
0)

2)

a∈Z in blue, ((0
b)

2)
b>0 in red,

S
(7)
5,2 in yellow and ∇S
(7)
10,−10 in green
 17

Proof. By Proposition 3.12, we know that ∂kS
(n)
k,lk = S
(n−k)
0,lk = ((lk+j−1
0 )

2)

1⩽j⩽n−k = (1)n−k,
for all k ∈ {0, . . . , m − 1}. It follows from Corollary 3.11 that the set
{ρ (∇S(n)
k,lk
) ∣
∣
∣ k ∈ {0, . . . , m − 1}}

is a basis of RST (n). Moreover, the formula of ρ (∇S
(n)
k,lk
) given in (8) directly comes
from Proposition 3.12 and Proposition 3.6.

Remark. For any integer l0, we have ρ (
∇S
(n)
0,l0) = ρ (∇(1)n) = Un.

For instance, for n = 10 and l0 = l1 = l2 = l3 = 0, we obtain

k S
(10)
k,0 ρ (∇S(10)
k,0 )

0 (1111111111) ∇0 = ∇(0111111110)
1 (0101010101) ∇1 = ∇(1001010111)
2 (0011001100) ∇2 = ∇(0001001000)
3 (0001000100) ∇3 = ∇(0010001100)

All the rotationally symmetric Steinhaus triangles of size 10 are depicted in Figure 10,
where the elements of the basis {∇0, ∇1, ∇2, ∇3} are in red and, for every ∇ ∈ RST (10),
the coordinate vector (x0, x1, x2, x3) of ∇ = x0∇0 + x1∇1 + x2∇2 + x3∇3 is given.

4 Horizontally symmetric Steinhaus triangles

In this section, we characterize the horizontally symmetric Steinhaus triangles and we
give a generating index set of HST (n). This permits us to obtain bases of HST (n), for
all non-negative integers n.

4.1 Characterizations of HST (n)

A binary sequence S = (aj)1⩽j⩽n is said to be symmetric if an−j+1 = aj, for all j ∈
{1, . . . , n}. For instance, the sequence (010010010) is symmetric. As shown in the follow-
ing result, the symmetry is preserved under the derivation process.

Proposition 4.1. The binary sequence S is symmetric if and only if ∂S is symmetric
and σ2(∂S) = 0.

Proof. Let S = (aj)1⩽j⩽n and ∂S = (bj)1⩽j⩽n−1. Then, by deﬁnition of ∂S, we have

bi + b(n−1)−i+1 = bi + bn−i
≡ (ai + ai+1) + (an−i + an−i+1) (mod 2)
= (ai + an−i+1) + (ai+1 + an−(i+1)+1),
 (9)

for all i ∈ {1, . . . , n − 1}. Moreover, the sum σ(∂S) satisﬁes

σ(∂S) =
 n−1∑

i=1 bi ≡
 n−1∑

i=1 (ai + ai+1) ≡ a1 + an (mod 2). (10)

First, if S is symmetric, we deduce from (9) that ∂S is also symmetric and from (10) that
σ(∂S) is even. Conversely, if we suppose that ∂S is symmetric of even sum σ (∂S), we
know from (10) that a1 = an. Using this equality and (9), we can prove, by induction on
i, that ai = an−i+1, for all i ∈ {1, . . . , n}. This completes the proof.

18

0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0
0 0 0 0
0 0 0
0 0
0
 0 1 1 1 1 1 1 1 1 0
1 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1
1 0 0 0 0 0 1
1 0 0 0 0 1
1 0 0 0 1
1 0 0 1
1 0 1
1 1
0
 1 0 0 1 0 1 0 1 1 1
1 0 1 1 1 1 1 0 0
1 1 0 0 0 0 1 0
0 1 0 0 0 1 1
1 1 0 0 1 0
0 1 0 1 1
1 1 1 0
0 0 1
0 1
1
 1 1 1 0 1 0 1 0 0 1
0 0 1 1 1 1 1 0 1
0 1 0 0 0 0 1 1
1 1 0 0 0 1 0
0 1 0 0 1 1
1 1 0 1 0
0 1 1 1
1 0 0
1 0
1

(0 ; 0 ; 0 ; 0) (1 ; 0 ; 0 ; 0) (0 ; 1 ; 0 ; 0) (1 ; 1 ; 0 ; 0)

0 0 0 1 0 0 1 0 0 0
0 0 1 1 0 1 1 0 0
0 1 0 1 1 0 1 0
1 1 1 0 1 1 1
0 0 1 1 0 0
0 1 0 1 0
1 1 1 1
0 0 0
0 0
0
 0 1 1 0 1 1 0 1 1 0
1 0 1 1 0 1 1 0 1
1 1 0 1 1 0 1 1
0 1 1 0 1 1 0
1 0 1 1 0 1
1 1 0 1 1
0 1 1 0
1 0 1
1 1
0
 1 0 0 0 0 1 1 1 1 1
1 0 0 0 1 0 0 0 0
1 0 0 1 1 0 0 0
1 0 1 0 1 0 0
1 1 1 1 1 0
0 0 0 0 1
0 0 0 1
0 0 1
0 1
1
 1 1 1 1 1 0 0 0 0 1
0 0 0 0 1 0 0 0 1
0 0 0 1 1 0 0 1
0 0 1 0 1 0 1
0 1 1 1 1 1
1 0 0 0 0
1 0 0 0
1 0 0
1 0
1

(0 ; 0 ; 1 ; 0) (1 ; 0 ; 1 ; 0) (0 ; 1 ; 1 ; 0) (1 ; 1 ; 1 ; 0)

0 0 1 0 0 0 1 1 0 0
0 1 1 0 0 1 0 1 0
1 0 1 0 1 1 1 1
1 1 1 1 0 0 0
0 0 0 1 0 0
0 0 1 1 0
0 1 0 1
1 1 1
0 0
0
 0 1 0 1 1 1 0 0 1 0
1 1 1 0 0 1 0 1 1
0 0 1 0 1 1 1 0
0 1 1 1 0 0 1
1 0 0 1 0 1
1 0 1 1 1
1 1 0 0
0 1 0
1 1
0
 1 0 1 1 0 1 1 0 1 1
1 1 0 1 1 0 1 1 0
0 1 1 0 1 1 0 1
1 0 1 1 0 1 1
1 1 0 1 1 0
0 1 1 0 1
1 0 1 1
1 1 0
0 1
1
 1 1 0 0 1 0 0 1 0 1
0 1 0 1 1 0 1 1 1
1 1 1 0 1 1 0 0
0 0 1 1 0 1 0
0 1 0 1 1 1
1 1 1 0 0
0 0 1 0
0 1 1
1 0
1

(0 ; 0 ; 0 ; 1) (1 ; 0 ; 0 ; 1) (0 ; 1 ; 0 ; 1) (1 ; 1 ; 0 ; 1)

0 0 1 1 0 0 0 1 0 0
0 1 0 1 0 0 1 1 0
1 1 1 1 0 1 0 1
0 0 0 1 1 1 1
0 0 1 0 0 0
0 1 1 0 0
1 0 1 0
1 1 1
0 0
0
 0 1 0 0 1 1 1 0 1 0
1 1 0 1 0 0 1 1 1
0 1 1 1 0 1 0 0
1 0 0 1 1 1 0
1 0 1 0 0 1
1 1 1 0 1
0 0 1 1
0 1 0
1 1
0
 1 0 1 0 0 1 0 0 1 1
1 1 1 0 1 1 0 1 0
0 0 1 1 0 1 1 1
0 1 0 1 1 0 0
1 1 1 0 1 0
0 0 1 1 1
0 1 0 0
1 1 0
0 1
1
 1 1 0 1 1 0 1 1 0 1
0 1 1 0 1 1 0 1 1
1 0 1 1 0 1 1 0
1 1 0 1 1 0 1
0 1 1 0 1 1
1 0 1 1 0
1 1 0 1
0 1 1
1 0
1

(0 ; 0 ; 1 ; 1) (1 ; 0 ; 1 ; 1) (0 ; 1 ; 1 ; 1) (1 ; 1 ; 1 ; 1)

Figure 10: The 16 triangles of RST (10) where the 4 red triangles form a basis

19

Remark. It is natural to ask if there exists a similar result for the case where ∂S is
symmetric and σ(∂S) is odd. It is known that the binary sequence S = (aj)1⩽j⩽n is
antisymmetric, i.e., an−j+1 ≡ aj + 1 mod 2 for all i ∈ {1, . . . , n}, if and only if ∂S is
symmetric and σ2 (∂S) = 1. Note that antisymmetric binary sequences only exist for odd
lengths.

It follows that the horizontal symmetry of a Steinhaus triangle is only related to the
symmetry of its ﬁrst row.

Proposition 4.2. The Steinhaus triangle ∇S is horizontally symmetric if and only if the
sequence S is symmetric.

Proof. First, it is clear that if ∇S is horizontally symmetric, then S is a symmetric
sequence. Conversely, if we suppose that S is symmetric, we know from Proposition 4.1
that the iterated derived sequences ∂iS are symmetric, for all i ∈ {0, . . . , n−1}. Therefore,
the Steinhaus triangle ∇S is horizontally symmetric.

Now, we show that the horizontal symmetry of a Steinhaus triangle only depends on
the values of middle terms of its rows of odd lengths.

Proposition 4.3. The Steinhaus triangle (ai,j)1⩽i⩽j⩽n, of size n, is horizontally symmet-
ric if and only if an−2i,n−i = 0, for all i ∈ {0, . . . , ⌊ n
2 ⌋ − 1
}.

The proof is based on the following lemma which is straightforward from the deﬁnition
of a symmetric sequence.

Lemma 4.4. Let S = (a1, a2, . . . , an) be a symmetric binary sequence of length n. Then,

σ2(S) = { 0 if n is even,
a n+1
2 if n is odd.

Proof of Proposition 4.3. First, suppose that the Steinhaus triangle ∇S = (ai,j)1⩽i⩽j⩽n
of size n is horizontally symmetric. Then, since the iterated derived sequences ∂iS =
(ai+1,j)i+1⩽j⩽n are symmetric, for all i ∈ {0, . . . , n−1}, we know from Proposition 4.1 that
σ2 (∂iS) = 0, for all i ∈ {1, . . . , n − 1}. Moreover, for any i ∈ {1, 2, . . . , n}, the sequence
∂n−iS is of length i. It follows from Lemma 4.4 that an−2i,n−i = σ2 (∂n−(2i+1)S) = 0, for
all i ∈ {0, . . . , ⌊ n
2 ⌋ − 1
}
.
Conversely, suppose that an−2i,n−i = 0, for all i ∈ {0, . . . , ⌊ n
2 ⌋ − 1
}. We proceed by
induction on n. For n = 1, the result is clear since any Steinhaus triangle of size n = 1 is
horizontally symmetric. Suppose that the result is true for any Steinhaus triangle of size
strictly lesser than n. We consider the subtriangle ∇∂S = (ai+1,j+1)1⩽i⩽j⩽n−1 of size n − 1.
Since the identities a1+(n−1)−2i,1+(n−1)−i = 0 hold, for all i ∈ {0, . . . , ⌊ n−1
2 ⌋ − 1
}, it follows
that ∇∂S is horizontally symmetric by induction hypothesis. Therefore, the sequence ∂iS
is symmetric, for all i ∈ {1, . . . , n − 1}. If n is odd, then ∂S is symmetric and σ2 (∂S) = 0
by Lemma 4.4. Otherwise, if n is even, then ∂S is symmetric and σ2 (∂S) = a2, n
2 +1 = 0
by Lemma 4.4 again. It follows from Proposition 4.1 that S symmetric. Therefore, in any
case, the Steinhaus triangle ∇S is horizontally symmetric by Proposition 4.2.

20

4.2 Generating index set of HST (n)

Proposition 4.5. Let n be a non-negative integer. The set

GH := {(1, j) ∣
∣
∣ j ∈ {
1, . . . , ⌈n
2
 ⌉}}

is a generating index set of HST (n).

Proof. From Proposition 4.2, we deduce that HST (n) is isomorphic to the vector space
of symmetric binary sequences of length n. Obviously, a symmetric sequence of length n
is entirely determined by its ⌈ n
2 ⌉ ﬁrst terms.

Since the dimension of HST (n) corresponds to the cardinality of the generating index
set GH, it is straightforward to obtain the following

Corollary 4.6. dim HST (n) = ⌈ n
2 ⌉
, for all non-negative integers n.

4.3 Bases of HST (n)

Let n be a positive integer. For any positive integer k ∈ {1, . . . , n}, we denote by E(n)
k
the binary sequence of length n consisting only of zeroes, except at position k. In other
words, we have
 E
(n)
k = (( 0
j − k
)

2
)
1⩽j⩽n ,

for all k ∈ {1, . . . , n}. Since we retrieve the local rule (LR) of the inﬁnite Pascal matrix
modulo 2, we obtain that
 ∇E(n)
k = ((i − 1
j − k
)

2
)

1⩽i⩽j⩽n ,

for all integers k ∈ {1, . . . , n}.

Proposition 4.7. Let n be a positive integer. Then, the set {∇1, . . . , ∇⌈ n
2 ⌉
} is a basis of
HST (n), where

∇k = ∇(E(n)
k + E(n)
n−k+1) = ((i − 1
j − k
) + ( i − 1
j − n + k − 1

) mod 2
)
1⩽i⩽j⩽n ,

for all k ∈ {1, . . . , ⌊ n
2 ⌋}, and

∇n+1
2 = ∇E(n)
n+1
2 = (( i − 1
j − n+1
2
 )

2
)
1⩽i⩽j⩽n ,

when n is odd.

Proof. First, by deﬁnition, it is clear that ∇k ∈ HST (n), for all k ∈ {1, . . . , ⌈ n
2 ⌉}. Now,
we consider the set GH := {(1, j) ∣
∣ j ∈ {1, . . . , ⌈ n
2 ⌉}}. Since

πGH (∇k) = E
(⌈ n
2 ⌉)
k ,

for all k ∈ {1, . . . , ⌈ n
2 ⌉}, it follows that the set {πGH (∇1) , . . . , πGH (∇⌈ n
2 ⌉
)} is a basis

of {0, 1}GH . Moreover, since GH is a generating index set of HST (n) by Proposition 4.5,
we conclude that the set {
∇1, . . . , ∇⌈ n
2 ⌉
} is a basis of HST (n).

21

In the end of this section, we show that the generating index set GH also permits us
to obtain a basis from the sequences S
(n)
k,l = ((l+j−1
k )

2)

1⩽j⩽n introduced in Section 3.

Lemma 4.8. Let k and n be two positive integers of same parity. Then, the n-length
sequence S(n)
k,l is symmetric for l = k−n
2 . Moreover, the k + 2 middle terms of S
(n)
k, k−n
2 are

of the form (∗ · · · ∗ 1 00 · · · 00︸ ︷︷ ︸
k 1 ∗ · · · ∗).

Proof. Suppose that k and n are of same parity, i.e., l = k−n
2 is an integer. Let S
(n)
k,l =
(aj)1⩽j⩽n with aj = (
l+j−1
k )

2, for all j ∈ {1, . . . , n}. Since (
a
b)

2 = (b−a−1
b )

2, for any integers
a and b such that b ⩾ 0, it follows that

an−j+1 = ( k−n
2 + (n − j + 1) − 1
k
 )

2 = (k − ( k−n
2 + n − j) − 1
k
 )

2 = ( k−n
2 + j − 1
k
 )

2 = aj,

for all j ∈ {1, . . . , n}. Therefore, the sequence S
(n)
k,l is symmetric for l = k−n
2 . Moreover,

the k + 2 middle terms of S
(n)
k,l are (j
k)

2, for j ∈ {−1, . . . , k}, where (−1
k )

2 = (
k
k)

2 = 1 and
(j
k)

2 = 0, for all j ∈ {0, . . . , k − 1}, since k ⩾ 1. This completes the proof.

Theorem 4.9. Let n be a non-negative integer. The set {
∇1, . . . , ∇⌈ n
2 ⌉
} is a basis of
HST (n), where
 ∇k = ∇S
(n)
n−2k,−k = (( −k + j − i
n − 2k + 1 − i

)

2
)

1⩽i⩽j⩽n ,

for all k ∈ {1, . . . , ⌊ n
2 ⌋}, and ∇n+1
2 = ∇(1)n, when n is odd.

Proof. First, we know from Lemma 4.8 that the sequence S
(n)
n−2k,−k is symmetric, for
all k ∈ {1, . . . , ⌊ n
2 ⌋}. Obviously, when n is odd, the constant sequence (1)n is also
symmetric. Therefore ∇k ∈ HST (n), for all k ∈ {1, . . . , ⌈ n
2 ⌉}, by Proposition 4.2. Now,
we consider the set GH := {(1, j) ∣
∣ j ∈ {1, . . . , ⌈ n
2 ⌉}}. By Lemma 4.8 again, we know
that the n − 2k + 2 middle terms of S
(n)
n−2k,−k are of the form (∗ · · · ∗︸ ︷︷ ︸
k−1 1 00 · · · 00︸ ︷︷ ︸
n−2k 1 ∗ · · · ∗︸ ︷︷ ︸
k−1 )

and thus πGH (∇k) = (∗, · · · , ∗
︸ ︷︷ ︸
k−1 , 1, 0, · · · , 0
︸ ︷︷ ︸
⌈ n
2 ⌉−k
 ),

for all k ∈ {1, . . . , ⌊ n
2 ⌋}. Moreover, πGH (
∇n+1
2
 ) = πGH (∇(1)n) = (1, 1, . . . , 1), when n

is odd. Therefore, the set {πGH (∇k) ∣
∣ k ∈ {1, . . . , ⌈ n
2 ⌉}} is a basis of {0, 1}GH . Finally,
since GH is a generating index set of HST (n) by Proposition 4.5, we conclude that the
set {
∇1, . . . , ∇⌈ n
2 ⌉
} is a basis of HST (n).

Remark. When n is even, we have ∇n
2 = ∇S
(n)
0,− n
2 = ∇(1)n. Therefore, ∇⌈ n
2 ⌉ = ∇(1)n, for
all integers n.
For instance, for n = 7, we obtain

∇1 = ∇S
(7)
5,−1 = ∇(1000001), ∇2 = ∇S
(7)
3,−2 = ∇(0100010),
∇3 = ∇S
(7)
1,−3 = ∇(1010101), ∇4 = ∇(1111111).

All the horizontally symmetric Steinhaus triangles of size 7 are depicted in Figure 11,
where the elements of the basis {∇1, ∇2, ∇3, ∇4} are in red and, for every ∇ ∈ HST (7),
the coordinate vector (x1, x2, x3, x4) of ∇ = x1∇1 + x2∇2 + x3∇3 + x4∇4 is given.

22

0 0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0
0 0 0 0
0 0 0
0 0
0
 1 0 0 0 0 0 1
1 0 0 0 0 1
1 0 0 0 1
1 0 0 1
1 0 1
1 1
0
 0 1 0 0 0 1 0
1 1 0 0 1 1
0 1 0 1 0
1 1 1 1
0 0 0
0 0
0
 1 1 0 0 0 1 1
0 1 0 0 1 0
1 1 0 1 1
0 1 1 0
1 0 1
1 1
0

(0 ; 0 ; 0 ; 0) (1 ; 0 ; 0 ; 0) (0 ; 1 ; 0 ; 0) (1 ; 1 ; 0 ; 0)

1 0 1 0 1 0 1
1 1 1 1 1 1
0 0 0 0 0
0 0 0 0
0 0 0
0 0
0
 0 0 1 0 1 0 0
0 1 1 1 1 0
1 0 0 0 1
1 0 0 1
1 0 1
1 1
0
 1 1 1 0 1 1 1
0 0 1 1 0 0
0 1 0 1 0
1 1 1 1
0 0 0
0 0
0
 0 1 1 0 1 1 0
1 0 1 1 0 1
1 1 0 1 1
0 1 1 0
1 0 1
1 1
0

(0 ; 0 ; 1 ; 0) (1 ; 0 ; 1 ; 0) (0 ; 1 ; 1 ; 0) (1 ; 1 ; 1 ; 0)

1 1 1 1 1 1 1
0 0 0 0 0 0
0 0 0 0 0
0 0 0 0
0 0 0
0 0
0
 0 1 1 1 1 1 0
1 0 0 0 0 1
1 0 0 0 1
1 0 0 1
1 0 1
1 1
0
 1 0 1 1 1 0 1
1 1 0 0 1 1
0 1 0 1 0
1 1 1 1
0 0 0
0 0
0
 0 0 1 1 1 0 0
0 1 0 0 1 0
1 1 0 1 1
0 1 1 0
1 0 1
1 1
0

(0 ; 0 ; 0 ; 1) (1 ; 0 ; 0 ; 1) (0 ; 1 ; 0 ; 1) (1 ; 1 ; 0 ; 1)

0 1 0 1 0 1 0
1 1 1 1 1 1
0 0 0 0 0
0 0 0 0
0 0 0
0 0
0
 1 1 0 1 0 1 1
0 1 1 1 1 0
1 0 0 0 1
1 0 0 1
1 0 1
1 1
0
 0 0 0 1 0 0 0
0 0 1 1 0 0
0 1 0 1 0
1 1 1 1
0 0 0
0 0
0
 1 0 0 1 0 0 1
1 0 1 1 0 1
1 1 0 1 1
0 1 1 0
1 0 1
1 1
0

(0 ; 0 ; 1 ; 1) (1 ; 0 ; 1 ; 1) (0 ; 1 ; 1 ; 1) (1 ; 1 ; 1 ; 1)

Figure 11: The 16 triangles of HST (7) where the 4 red triangles form a basis

23

5 Dihedrally symmetric Steinhaus triangles

In this section, after characterizing dihedrally symmetric Steinhaus triangles, we deter-
mine, for all non-negative integers n, generating index sets and a basis of DST (n).

5.1 Characterizations of DST (n)

We begin by showing that the dihedral symmetry of a Steinhaus triangle is only related
to the symmetry of its ﬁrst row and of its right and left sides.

Proposition 5.1. The Steinhaus triangle ∇ is dihedrally symmetric if and only if two of
the three Steinhaus triangles ∇, r (∇) and r2 (∇) are horizontally symmetric.

Proof. Directly comes from the fact that the automorphisms h and hr are generators of
D3. First, if ∇ is dihedrally symmetric, then ∇ = r (∇) = r2 (∇). Since a dihedrally
symmetric triangle is also horizontally symmetric, the result follows.
Suppose now that the Steinhaus triangles ∇ and r (∇) are horizontally symmetric. It
follows that h (∇) = ∇ and hr (∇) = r (∇). Combining these identities with the relations
r3 = h
2 = hrhr = idST (n), we obtain that

∇ = r2 (r (∇)) = r2 (hr (∇))
= r2h (r (∇)) = hr (r (∇)) = hr2 (∇) = rh (∇) = r (h (∇)) = r (∇) .

We conclude that the Steinhaus triangle ∇ is dihedrally symmetric since it is horizontally
symmetric and rotationally symmetric. If the two horizontally symmetric Steinhaus trian-
gles are r2 (∇) and ∇, or r (∇) and r2 (∇), we can show by the same way that the triangles
r2 (∇) or r (∇) are dihedrally symmetric, since r (r2 (∇)) = ∇ and r (r (∇)) = r2 (∇), re-
spectively. In any case, we obtain that the Steinhaus triangle ∇ = r (∇) = r2 (∇) is
dihedrally symmetric.

Corollary 5.2. The Steinhaus triangle ∇S = (ai,j)1⩽i⩽j⩽n is dihedrally symmetric if and
only if two of the three sequences, its ﬁrst row (a1,j)1⩽j⩽n, its right side (aj,n)1⩽j⩽n or its
left side (aj,j)1⩽j⩽n, are symmetric.

Proof. Directly comes from Proposition 5.1, since, by Proposition 4.2, we know that the
Steinhaus triangles ∇S, r (∇S) and r2 (∇S) are horizontally symmetric if and only if the
sequences (a1,j)1⩽j⩽n, (aj,n)1⩽j⩽n and (aj,j)1⩽j⩽n are symmetric, respectively.

Proposition 5.1 also permits us to show that the dihedral symmetry of a Steinhaus
triangle only depends on the values of middle terms of its rows, its columns or its diagonals
of odd lengths.

Corollary 5.3. The Steinhaus triangle ∇S = (ai,j)1⩽i⩽j⩽n is dihedrally symmetric if and
only if two of the three sets {an−2i,n−i∣
∣i ∈ {0, . . . , ⌊ n
2 ⌋ − 1
}}, {ai,2i−1∣
∣i ∈ {1, . . . , ⌊ n
2 ⌋}}

and {ai,n−i+1∣
∣i ∈ {1, . . . , ⌊ n
2 ⌋}} are sets of zeroes.

Proof. From Proposition 4.3, we know that the Steinhaus triangles ∇S, r (∇S) and
r2 (∇S) are horizontally symmetric if and only if an−2i,n−i = 0 for all i ∈ {0, . . . , ⌊ n
2 ⌋ − 1
},
ai,2i−1 = 0 for all i ∈ {1, . . . , ⌊ n
2 ⌋} and ai,n−i+1 = 0 for all i ∈ {1, . . . , ⌊ n
2 ⌋}, respectively.
Finally, by Proposition 5.1, the Steinhaus triangle ∇S is dihedrally symmetric if and only
if two of the three Steinhaus triangles ∇S, r (∇S) and r2 (∇S) are horizontally symmetric.
This completes the proof.
 24

For any positive integer n ⩾ 3, by deﬁnition of DST (n) and H, it is clear that
H (DST (n)) ⊂ DST (n − 3). The precise relationship between a dihedrally symmetric
Steinhaus triangle ∇S and its subtriangle H (∇S) is given in the following

Proposition 5.4. Let S be a binary sequence of length n ⩾ 3. The Steinhaus triangle ∇S
is dihedrally symmetric if and only if H (∇S) = ∇S′ is dihedrally symmetric, σ2 (S′) = 0
and S = (0) · ∫

i,x S′ · (0), for some i ∈ {1, . . . , n − 2} and some x ∈ {0, 1}.

Proposition 5.4 appears in [4] in a more general context. For the convenience of the
reader, a proof is given here.

Proof. Let ∇S = (ai,j)1⩽i⩽j⩽n ∈ ST (n) such that ∇S′ = H(∇S) = (a1+i,2+j)1⩽i⩽j⩽n−3 ∈
DST (n − 3). From Proposition 3.2, Proposition 4.2 and Proposition 4.1, we deduce that
the Steinhaus triangle ∇S is dihedrally symmetric if and only if a1,1 = a1,n = σ2(S′), ∂S
is symmetric and σ2 (∂S) = 0. Since ∇S′ ∈ DST (n − 3), the sequence S′ is symmetric.
Therefore the sequence ∂S is symmetric if and only if a2,1 = a2,n. Moreover, it is clear
that σ (∂S) ≡ σ (S′) + a2,1 + a2,n mod 2. We claim that a1,1 = a1,n = σ2(S′), ∂S is
symmetric and σ2 (∂S) = 0 if and only if a1,1 = a1,n = σ2(S′) = 0. First, suppose
that a1,1 = a1,n = σ2(S′), ∂S is symmetric and σ2 (∂S) = 0. Since ∂S is symmetric, it
follows that a2,1 = a2,n and thus σ2 (S′) = σ2 (∂S) = 0. Conversely, suppose that a1,1 =
a1,n = σ2(S′) = 0. Since S′ is symmetric and σ2 (S′) = 0, we know from Proposition 4.1
that its antiderived sequence ∫
i,x S′ is symmetric too. Moreover, we have a1,1 = a1,n. It
follows that the sequence S is symmetric and, by Proposition 4.1 again, we obtain that
the sequence ∂S is symmetric and σ2 (∂S) = 0. This completes the proof.

For any non-negative integer n, the set of dihedrally symmetric Steinhaus triangles
∇S of size n with σ(S) even is denoted by DST 0(n). It is clear that DST 0(n) is a linear
subspace of DST (n). Moreover, the vector space DST (n) can be expressed in function
of its linear subspace DST 0(n).

Proposition 5.5. Let n be a non-negative integer. Then, we have

DST (n) = { DST 0(n) for n even,
DST 0(n) ⊔ (DST 0(n) + Un) for n odd,

where ⊔ is the disjoint union of two sets.

Proof. For any symmetric sequence S = (aj)1⩽j⩽n of length n, we know from Lemma 4.4
that σ2(S) = 0 when n is even and σ2(S) = a n+1
2 when n is odd. It follows that DST (n) =
DST 0(n), for n even. If n is odd, then we consider Un = ρ ((1)n). It is clear that
Un ∈ DST (n) and is generated from a sequence of odd sum, for all odd numbers n.
Since ∇S ∈ DST (n) with σ2(S) = 1 if and only if ∇S + Un ∈ DST 0(n), it follows that
DST (n) = DST 0(n) ⊔ (DST 0(n) + Un), when n is odd.

Using Lemma 4.4, it is straightforward to obtain from Propositon 5.4 the following

Corollary 5.6. Let S be a binary sequence of length n ⩾ 3. For n even, the Steinhaus
triangle ∇S is in DST 0(n) if and only if H(∇S) = ∇S′ is in DST 0(n − 3) and S =
(0) · ∫
i,x S′ · (0), for some i ∈ {1, . . . , n − 2} and some x ∈ {0, 1}. For n odd, the
Steinhaus triangle ∇S is in DST 0(n) if and only if H(∇S) = ∇S′ is in DST 0(n − 3) and
S = (0) · ∫
 n−1
2 ,0 S′ · (0).
 25

5.2 Generating index sets of DST (n)

We begin this subsection by giving, from Corollary 5.6, generating index sets of DST 0(n),
for all non-negative integers n.

Theorem 5.7. Let n and m be non-negative integers such that m = ⌊ n
6 ⌋ + δ4,(n mod 6).
For every integer i ∈ {1, . . . , ⌊ n
3 ⌋}, let ji ∈ {2i, . . . , n − i}. Then, the set

GD0 = {(2i + 1, j2i+1) | i ∈ {0, . . . , m − 1}} ,

when n is even, or GD0 = {(2i, j2i) | i ∈ {1, . . . , m}} ,

when n is odd, is a generating index set of DST 0(n).

Proof. By induction on n.
For n ∈ {0, 1, 2}, it is clear that ∇(0)n is the only element of DST 0(n). Therefore the
empty set ∅ is a generating set of DST 0(n), for these values of n.
Suppose now that the result is true for any size strictly lesser than n ⩾ 3. Let
m = ⌊ n
6 ⌋ + δ4,(n mod 6). We distinguish two cases following the parity of n.
Case 1. Suppose ﬁrst that n is odd. We consider the subset H (GD0) ⊂ ∇(n − 3) deﬁned
by H (GD0) = {(2i − 1, j2i − 2) | i ∈ {1, . . . , m}}

and the linear maps f1 and f2 deﬁned by

f1 : DST 0(n) −→ DST 0(n − 3)
∇S ↦−→ H (∇S)

and f2 : DST 0(n − 3) −→ {0, 1}m

∇S′ ↦−→ πH(GD0) (∇S′)

Then, for any (ai,j)1⩽i⩽j⩽n ∈ DST 0(n), we have

f2f1 ((ai,j)1⩽i⩽j⩽n) = f2 ((a1+i,2+j)1⩽i⩽j⩽n−3)
= πH(GD0) ((a1+i,2+j)1⩽i⩽j⩽n−3)

= (a2i,j2i)1⩽i⩽m = πGD0 ((ai,j)1⩽i⩽j⩽n) .

Therefore f2f1 = πGD0 . From Corollary 5.6, we know that f1 is an isomorphism whose

inverse is deﬁned by f1−1 (∇S′) = ∇((0) · ∫
 n−1
2 ,0 S′ · (0)
), for all ∇S′ ∈ DST 0(n − 3).
Moreover, since we have
 2(2i − 1) ⩽ j2i − 2 ⩽ (n − 3) − (2i − 1),

for all i ∈ {1, . . . , m}, and m = ⌊ n
6 ⌋ = ⌊ n−3
6 ⌋+δ4,(n−3 mod 6) when n is odd, the set H (GD0)
is a generating index set of DST 0(n − 3) by induction hypothesis. Therefore, f2 is an
isomorphism. Finally, since the linear map πGD0 = f2f1 is an isomorphism, the set GD0
is a generating index set of DST 0(n) in this case.

26

Case 2. Suppose now that n is even. We consider the subset H (GD0) ⊂ ∇(n − 3) deﬁned
by H (GD0) := {(2i, j2i+1 − 2) | i ∈ {1, . . . , m − 1}}

and the linear maps f1 and f2 deﬁned by

f1 : DST 0(n) −→ {0, 1} × DST 0(n − 3)
∇S = (ai,j)1⩽i⩽j⩽n ↦−→ (a1,j1, H (∇S))

and f2 : {0, 1} × DST 0(n − 3) −→ {0, 1}m

(x, ∇S′) ↦−→ (x) · πH(GD0) (∇S′)

Then, for any (ai,j)1⩽i⩽j⩽n ∈ DST 0(n), we have

f2f1 ((ai,j)1⩽i⩽j⩽n) = f2 (a1,j1, (a1+i,2+j)1⩽i⩽j⩽n−3)
= (a1,j1) · πH(GD0) ((a1+i,2+j)1⩽i⩽j⩽n−3)

= (a1,j1) · (
a2i+1,j2i+1)

1⩽i⩽m−1
= (
a2i+1,j2i+1)

0⩽i⩽m−1 = πGD0 ((ai,j)1⩽i⩽j⩽n) .

Therefore f2f1 = πGD0 . From Corollary 5.6, we know that f1 is an isomorphism whose

inverse is deﬁned by f1−1 (x, ∇S′) = ∇
((0) · ∫
j1−1,x S′ · (0)
), for all (x, ∇S′) ∈ {0, 1} ×
DST 0(n − 3). Moreover, since we have

4i ⩽ j2i+1 − 2 ⩽ (n − 3) − 2i,

for all i ∈ {1, . . . , m − 1}, and m − 1 = ⌊ n
6 ⌋ + δ4,(n mod 6) − 1 = ⌊ n−3
6 ⌋ when n is even, the
set H (GD0) is a generating index set of DST 0(n − 3) by induction hypothesis. Therefore
πH(GD0) and thus f2 are isomorphisms. Finally, since the linear map πGD0 = f2f1 is an
isomorphism, the set GD0 is a generating index set of DST 0(n) in this case.
This completes the proof.

Since the dimension of DST 0(n) corresponds to the cardinality of the generating index
set GD0, it is easy to obtain the following

Corollary 5.8. dim DST 0(n) = ⌊ n
6 ⌋ + δ4,(n mod 6), for all non-negative integers n.

Using Proposition 5.5 and Theorem 5.7, we are now ready to give a generating index
set of DST (n), for all non-negative integers n.

Theorem 5.9. Let n and m be non-negative integers such that m = ⌊ n+3
6 ⌋ + δ1,(n mod 6).
For every integer i ∈ {1, . . . , ⌊ n
3 ⌋}, let ji ∈ {2i, . . . , n − i}. Then, the set

GD = {(2i + 1, j2i+1) | i ∈ {0, . . . , m − 1}} ,

when n is even, or
 GD = {(1, j1)} ∪ {(2i, j2i) | i ∈ {1, . . . , m − 1}} ,

when n is odd, is a generating index set of DST (n).

27

Proof. First, suppose that n is even. We know, from Proposition 5.5, that DST (n) =
DST 0(n). Moreover, since m = ⌊ n+3
6 ⌋ = ⌊ n
6 ⌋ + δ4,(n mod 6) when n is even, it follows from
Theorem 5.7 that
 GD = GD0 = {(2i + 1, j2i+1) | i ∈ {0, . . . , m − 1}}

is a generating index set of DST (n) in this case.
Suppose now that n is odd. From Proposition 5.5, we know that DST (n) = DST 0(n)⊔
(DST 0(n) + Un). Therefore {(1, j1)} ∪ GD0 is a generating set of DST (n), where GD0 is
a generating index set of DST 0(n). Moreover, since m − 1 = ⌊ n+3
6 ⌋ + δ1,(n mod 6) − 1 = ⌊ n
6 ⌋

when n is odd, it follows from Theorem 5.7 that

GD = {(1, j1)} ∪ GD0 = {(1, j1)} ∪ {(2i, j2i) | i ∈ {1, . . . , m − 1}}

is a generating index set of DST (n) in this case. This completes the proof.

Corollary 5.10. Let n and m be non-negative integers such that m = ⌊ n+3
6 ⌋ + δ1,(n mod 6).
The set GD = {(
2i + 1, n − ⌊n
3
 ⌋) ∣
∣
∣ i ∈ {0, . . . , m − 1}
} ,

when n is even, or

GD = {(
1, n − ⌊n
3
 ⌋)} ∪ {(
2i, n − ⌊n
3
 ⌋) ∣
∣
∣ i ∈ {1, . . . , m − 1}} ,

when n is odd, is a generating index set of DST (n).

Proof. From Theorem 5.9, since 2i ⩽ n − ⌊ n
3 ⌋ ⩽ n − i, for all i ∈ {1, . . . , ⌊ n
3 ⌋}.

Since the dimension of DST (n) corresponds to the cardinality of the generating index
set GD, it is straightforward to obtain the following

Corollary 5.11. dim DST (n) = ⌊ n+3
6 ⌋ + δ1,(n mod 6), for all non-negative integers n.

5.3 Basis of DST (n)

First, using the operators H
k and the generating index sets GD introduced before, we
obtain a family of bases of DST (n), for all non-negative integers n.

Theorem 5.12. Let n and m be non-negative integers such that m = ⌊ n+3
6 ⌋ + δ1,(n mod 6).
For every k ∈ {
0, . . . , ⌊ n
3 ⌋ − 1
}, let ∇k ∈ DST (n) such that Hk (∇k) = Un−3k. Then, the
set {∇2k | k ∈ {0, . . . , m − 1}} ,

when n is even, or {∇0} ∪ {∇2k+1 | k ∈ {0, . . . , m − 2}} ,

when n is odd, is a basis of DST (n).

Remark. ∇0 = Un in the previous result.
 28

Proof. Suppose ﬁrst that n is even. We consider the set

GD = {(
2i + 1, n − ⌊n
3
 ⌋) ∣
∣
∣ i ∈ {0, . . . , m − 1}
} .

Let k ∈ {0, . . . , m − 1}. For ∇2k = (ai,j)1⩽i⩽j⩽n, since H
2k (∇2k) = Un−6k, it follows from
Lemma 3.10 that
 ai,n−⌊ n
3 ⌋ = { 1 for i = 2k + 1,
0 for i ∈ {
2k + 2, . . . , ⌊ n
3 ⌋} .

Moreover, it is clear that 2m − 1 ⩽ ⌊ n
3 ⌋ and thus

πGD (∇2k) = (∗, . . . , ∗
︸ ︷︷ ︸
k , 1, 0, . . . , 0
︸ ︷︷ ︸
m−k−1 ).

Therefore the set {πGD (∇2k) | k ∈ {0, . . . , m − 1}} is a basis of {0, 1}GD. Finally, since
GD is a generating index set of DST (n) by Corollary 5.10, we conclude that

{∇2k | k ∈ {0, . . . , m − 1}}

is a basis of DST (n) in this case.
Suppose now that n is odd. The proof is similar to the even case by considering the
generating index set

GD = {(
1, n − ⌊n
3
 ⌋)} ∪ {(
2i, n − ⌊ n
3
 ⌋) ∣
∣
∣ i ∈ {1, . . . , m − 1}} ,

from Corollary 5.10 and since

{πGD (∇0)} ∪ {πGD (∇2k+1) | k ∈ {0, . . . , m − 2}}

is a basis of {0, 1}GD using Lemma 3.10. This implies that the set

{∇0} ∪ {∇2k+1 | k ∈ {0, . . . , m − 2}}

is a basis of DST (n) in this case. This completes the proof.

Now, we consider the restriction of the linear map ρ on the linear subspace HST (n),
i.e., the linear map ρ HST (n) : HST (n) −→ DST (n) deﬁned by ρ = r2 + r + idn, for
all non-negative integers n. Obviously, this map is surjective since ρ(∇) = ∇, for all
∇ ∈ DST (n). Since Un−3k = ρ ((1)n−3k) by deﬁnition, for all non-negative integers n and
k such that 3k ⩽ n, this leads to the following

Corollary 5.13. Let n and m be non-negative integers such that m = ⌊ n+3
6 ⌋ + δ1,(n mod 6).
For every k ∈ {0, . . . , ⌊ n
3 ⌋ − 1
}, let Sk be a symmetric binary sequence of length n such
that ∂kSk = (1)n−k. Then, the set

{ρ (∇S2k) | k ∈ {0, . . . , m − 1}} ,

when n is even, or
 {ρ (∇S0)} ∪ {ρ (∇S2k+1) | k ∈ {0, . . . , m − 2}} ,

when n is odd, is a basis of DST (n).
 29

Remark. ρ (∇S0) = ρ (∇(1)n) = Un in the previous result.

Proof. Let k ∈ {0, . . . , ⌊ n
3 ⌋ − 1
}
. First, since Sk is symmetric, we know from Proposi-
tion 4.2 that ∇Sk ∈ HST (n) and thus ρ (∇Sk) ∈ DST (n), by deﬁnition of ρ. Moreover,
since ∂kSk = (1)n−k, it follows that

H
k (ρ (∇Sk)) = ρ (
H
k (∇Sk)
) = ρ (∇(1)n−3k) = Un−3k.

Therefore, the result directly comes from Theorem 5.12 by considering the dihedrally
symmetric Steinhaus triangles ∇k = ρ (∇Sk).

We end this section by giving an explicit basis of DST (n) in terms of the n-length
binary sequences
 S
(n)
k,l = ((l + j − 1
k
 )

2
)

1⩽j⩽n ,

for all integers k and l.

Theorem 5.14. Let n and m be non-negative integers such that m = ⌊ n+3
6 ⌋ + δ1,(n mod 6).
For every k ∈ {0, . . . , ⌊ n
3 ⌋ − 1
} of same parity than n, let

∇k = ρ (∇S(n)
k, k−n
2
 ) = (( k−n
2 + j − i
k + 1 − i
 ) + ( k+n
2 − j
k + i − j
) + ( k−n
2 + i − 1
k + j − n
 ) mod 2
)
1⩽i⩽j⩽n .

Then, the set {∇2k | k ∈ {0, . . . , m − 1}} ,

when n is even, or {Un} ∪ {∇2k+1 | k ∈ {0, . . . , m − 2}} ,

when n is odd, is a basis of DST (n).

Proof. Let k ∈ {0, . . . , ⌊ n
3 ⌋ − 1
} of same parity of n. First, we know from Lemma 4.8
that the sequence S(n)
k, k−n
2 is symmetric. Moreover, by Proposition 3.12, we have

∂k (S
(n)
k, k−n
2
 ) = S
(n−k)
0, k−n
2 = (1)n−k.

We conclude the proof by using Corollary 5.13 with the sequences Sk = S
(n)
k, k−n
2 , for all

k ∈ {0, . . . , ⌊ n
3 ⌋ − 1
} of same parity of n, and S0 = (1)n, when n is odd.

Corollary 5.15. Let n and m be non-negative integers such that m = ⌊ n
6 ⌋ + δ4,(n mod 6).
For every k ∈ {0, . . . , ⌊ n
3 ⌋ − 1
} of same parity than n, let

∇k = ρ (∇S(n)
k, k−n
2
 ) = (( k−n
2 + j − i
k + 1 − i
 ) + ( k+n
2 − j
k + i − j
) + ( k−n
2 + i − 1
k + j − n
 ) mod 2
)
1⩽i⩽j⩽n .

Then, the set {∇2k | k ∈ {0, . . . , m − 1}} ,

when n is even, or {∇2k+1 | k ∈ {0, . . . , m − 1}} ,

when n is odd, is a basis of DST 0(n).
 30

Proof. From Theorem 5.14, since we have that DST (n) = DST 0(n), when n is even, and
DST (n) = DST 0(n) ⊔ (DST 0(n) + Un), when n is odd, by Proposition 5.5.

For instance, for n = 22, we obtain

k S
(22)
2k,k−11 ρ (∇S(22)
2k,k−11)

0 (1111111111111111111111) ∇0 = ∇(0111111111111111111110)
1 (1100110011001100110011) ∇2 = ∇(0110110011001100110110)
2 (1000011110000111100001) ∇4 = ∇(0111111110000111111110)
3 (0000001100000011000000) ∇6 = ∇(0000000100000010000000)

All the dihedrally symmetric Steinhaus triangles of size 22 are depicted in Figure 12,
where the elements of the basis {∇0, ∇2, ∇4, ∇6} are in red and, for every ∇ ∈ DST (22),
the coordinate vector (x0, x2, x4, x6) of ∇ = x0∇0 + x2∇2 + x4∇4 + x6∇6 is given.

0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0
0 0 0 0
0 0 0
0 0
0
 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1
1 0 0 0 0 0 1
1 0 0 0 0 1
1 0 0 0 1
1 0 0 1
1 0 1
1 1
0
 0 1 1 0 1 1 0 0 1 1 0 0 1 1 0 0 1 1 0 1 1 0
1 0 1 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 1 0 1
1 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 1
0 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 0
1 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 1
1 1 1 0 0 0 0 0 0 0 0 0 0 0 1 1 1
0 0 1 0 0 0 0 0 0 0 0 0 0 1 0 0
0 1 1 0 0 0 0 0 0 0 0 0 1 1 0
1 0 1 0 0 0 0 0 0 0 0 1 0 1
1 1 1 0 0 0 0 0 0 0 1 1 1
0 0 1 0 0 0 0 0 0 1 0 0
0 1 1 0 0 0 0 0 1 1 0
1 0 1 0 0 0 0 1 0 1
1 1 1 0 0 0 1 1 1
0 0 1 0 0 1 0 0
0 1 1 0 1 1 0
1 0 1 1 0 1
1 1 0 1 1
0 1 1 0
1 0 1
1 1
0
 0 0 0 1 0 0 1 1 0 0 1 1 0 0 1 1 0 0 1 0 0 0
0 0 1 1 0 1 0 1 0 1 0 1 0 1 0 1 0 1 1 0 0
0 1 0 1 1 1 1 1 1 1 1 1 1 1 1 1 1 0 1 0
1 1 1 0 0 0 0 0 0 0 0 0 0 0 0 0 1 1 1
0 0 1 0 0 0 0 0 0 0 0 0 0 0 0 1 0 0
0 1 1 0 0 0 0 0 0 0 0 0 0 0 1 1 0
1 0 1 0 0 0 0 0 0 0 0 0 0 1 0 1
1 1 1 0 0 0 0 0 0 0 0 0 1 1 1
0 0 1 0 0 0 0 0 0 0 0 1 0 0
0 1 1 0 0 0 0 0 0 0 1 1 0
1 0 1 0 0 0 0 0 0 1 0 1
1 1 1 0 0 0 0 0 1 1 1
0 0 1 0 0 0 0 1 0 0
0 1 1 0 0 0 1 1 0
1 0 1 0 0 1 0 1
1 1 1 0 1 1 1
0 0 1 1 0 0
0 1 0 1 0
1 1 1 1
0 0 0
0 0
0

(0 , 0, 0, 0) (1 , 0, 0, 0) (0 , 1, 0, 0) (1 , 1, 0, 0)

0 1 1 1 1 1 1 1 1 0 0 0 0 1 1 1 1 1 1 1 1 0
1 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 0 1
1 0 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 0 1
1 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 1
1 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 1
1 0 0 1 1 0 0 0 0 0 0 1 1 0 0 1
1 0 1 0 1 0 0 0 0 0 1 0 1 0 1
1 1 1 1 1 0 0 0 0 1 1 1 1 1
0 0 0 0 1 0 0 0 1 0 0 0 0
0 0 0 1 1 0 0 1 1 0 0 0
0 0 1 0 1 0 1 0 1 0 0
0 1 1 1 1 1 1 1 1 0
1 0 0 0 0 0 0 0 1
1 0 0 0 0 0 0 1
1 0 0 0 0 0 1
1 0 0 0 0 1
1 0 0 0 1
1 0 0 1
1 0 1
1 1
0
 0 0 0 0 0 0 0 0 0 1 1 1 1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0 0 0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 1 0 0 1 1 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 1 0 1 0 1 0 0 0 0 0 0
0 0 0 0 0 1 1 1 1 1 1 1 1 0 0 0 0 0
0 0 0 0 1 0 0 0 0 0 0 0 1 0 0 0 0
0 0 0 1 1 0 0 0 0 0 0 1 1 0 0 0
0 0 1 0 1 0 0 0 0 0 1 0 1 0 0
0 1 1 1 1 0 0 0 0 1 1 1 1 0
1 0 0 0 1 0 0 0 1 0 0 0 1
1 0 0 1 1 0 0 1 1 0 0 1
1 0 1 0 1 0 1 0 1 0 1
1 1 1 1 1 1 1 1 1 1
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0
0 0 0 0
0 0 0
0 0
0
 0 0 0 1 0 0 1 1 0 1 0 0 1 0 1 1 0 0 1 0 0 0
0 0 1 1 0 1 0 1 1 1 0 1 1 1 0 1 0 1 1 0 0
0 1 0 1 1 1 1 0 0 1 1 0 0 1 1 1 1 0 1 0
1 1 1 0 0 0 1 0 1 0 1 0 1 0 0 0 1 1 1
0 0 1 0 0 1 1 1 1 1 1 1 1 0 0 1 0 0
0 1 1 0 1 0 0 0 0 0 0 0 1 0 1 1 0
1 0 1 1 1 0 0 0 0 0 0 1 1 1 0 1
1 1 0 0 1 0 0 0 0 0 1 0 0 1 1
0 1 0 1 1 0 0 0 0 1 1 0 1 0
1 1 1 0 1 0 0 0 1 0 1 1 1
0 0 1 1 1 0 0 1 1 1 0 0
0 1 0 0 1 0 1 0 0 1 0
1 1 0 1 1 1 1 0 1 1
0 1 1 0 0 0 1 1 0
1 0 1 0 0 1 0 1
1 1 1 0 1 1 1
0 0 1 1 0 0
0 1 0 1 0
1 1 1 1
0 0 0
0 0
0
 0 1 1 0 1 1 0 0 1 0 1 1 0 1 0 0 1 1 0 1 1 0
1 0 1 1 0 1 0 1 1 1 0 1 1 1 0 1 0 1 1 0 1
1 1 0 1 1 1 1 0 0 1 1 0 0 1 1 1 1 0 1 1
0 1 1 0 0 0 1 0 1 0 1 0 1 0 0 0 1 1 0
1 0 1 0 0 1 1 1 1 1 1 1 1 0 0 1 0 1
1 1 1 0 1 0 0 0 0 0 0 0 1 0 1 1 1
0 0 1 1 1 0 0 0 0 0 0 1 1 1 0 0
0 1 0 0 1 0 0 0 0 0 1 0 0 1 0
1 1 0 1 1 0 0 0 0 1 1 0 1 1
0 1 1 0 1 0 0 0 1 0 1 1 0
1 0 1 1 1 0 0 1 1 1 0 1
1 1 0 0 1 0 1 0 0 1 1
0 1 0 1 1 1 1 0 1 0
1 1 1 0 0 0 1 1 1
0 0 1 0 0 1 0 0
0 1 1 0 1 1 0
1 0 1 1 0 1
1 1 0 1 1
0 1 1 0
1 0 1
1 1
0

(0 , 0, 1, 0) (1 , 0, 1, 0) (0 , 1, 1, 0) (1 , 1, 1, 0)

0 0 0 0 0 0 0 1 0 0 0 0 0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 0 0 0 0 0 1 1 0 0 0 0 0 0
0 0 0 0 0 1 0 1 0 0 0 0 1 0 1 0 0 0 0 0
0 0 0 0 1 1 1 1 0 0 0 1 1 1 1 0 0 0 0
0 0 0 1 0 0 0 1 0 0 1 0 0 0 1 0 0 0
0 0 1 1 0 0 1 1 0 1 1 0 0 1 1 0 0
0 1 0 1 0 1 0 1 1 0 1 0 1 0 1 0
1 1 1 1 1 1 1 0 1 1 1 1 1 1 1
0 0 0 0 0 0 1 1 0 0 0 0 0 0
0 0 0 0 0 1 0 1 0 0 0 0 0
0 0 0 0 1 1 1 1 0 0 0 0
0 0 0 1 0 0 0 1 0 0 0
0 0 1 1 0 0 1 1 0 0
0 1 0 1 0 1 0 1 0
1 1 1 1 1 1 1 1
0 0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0
0 0 0 0
0 0 0
0 0
0
 0 1 1 1 1 1 1 0 1 1 1 1 1 1 0 1 1 1 1 1 1 0
1 0 0 0 0 0 1 1 0 0 0 0 0 1 1 0 0 0 0 0 1
1 0 0 0 0 1 0 1 0 0 0 0 1 0 1 0 0 0 0 1
1 0 0 0 1 1 1 1 0 0 0 1 1 1 1 0 0 0 1
1 0 0 1 0 0 0 1 0 0 1 0 0 0 1 0 0 1
1 0 1 1 0 0 1 1 0 1 1 0 0 1 1 0 1
1 1 0 1 0 1 0 1 1 0 1 0 1 0 1 1
0 1 1 1 1 1 1 0 1 1 1 1 1 1 0
1 0 0 0 0 0 1 1 0 0 0 0 0 1
1 0 0 0 0 1 0 1 0 0 0 0 1
1 0 0 0 1 1 1 1 0 0 0 1
1 0 0 1 0 0 0 1 0 0 1
1 0 1 1 0 0 1 1 0 1
1 1 0 1 0 1 0 1 1
0 1 1 1 1 1 1 0
1 0 0 0 0 0 1
1 0 0 0 0 1
1 0 0 0 1
1 0 0 1
1 0 1
1 1
0
 0 1 1 0 1 1 0 1 1 1 0 0 1 1 1 0 1 1 0 1 1 0
1 0 1 1 0 1 1 0 0 1 0 1 0 0 1 1 0 1 1 0 1
1 1 0 1 1 0 1 0 1 1 1 1 0 1 0 1 1 0 1 1
0 1 1 0 1 1 1 1 0 0 0 1 1 1 1 0 1 1 0
1 0 1 1 0 0 0 1 0 0 1 0 0 0 1 1 0 1
1 1 0 1 0 0 1 1 0 1 1 0 0 1 0 1 1
0 1 1 1 0 1 0 1 1 0 1 0 1 1 1 0
1 0 0 1 1 1 1 0 1 1 1 1 0 0 1
1 0 1 0 0 0 1 1 0 0 0 1 0 1
1 1 1 0 0 1 0 1 0 0 1 1 1
0 0 1 0 1 1 1 1 0 1 0 0
0 1 1 1 0 0 0 1 1 1 0
1 0 0 1 0 0 1 0 0 1
1 0 1 1 0 1 1 0 1
1 1 0 1 1 0 1 1
0 1 1 0 1 1 0
1 0 1 1 0 1
1 1 0 1 1
0 1 1 0
1 0 1
1 1
0
 0 0 0 1 0 0 1 0 0 0 1 1 0 0 0 1 0 0 1 0 0 0
0 0 1 1 0 1 1 0 0 1 0 1 0 0 1 1 0 1 1 0 0
0 1 0 1 1 0 1 0 1 1 1 1 0 1 0 1 1 0 1 0
1 1 1 0 1 1 1 1 0 0 0 1 1 1 1 0 1 1 1
0 0 1 1 0 0 0 1 0 0 1 0 0 0 1 1 0 0
0 1 0 1 0 0 1 1 0 1 1 0 0 1 0 1 0
1 1 1 1 0 1 0 1 1 0 1 0 1 1 1 1
0 0 0 1 1 1 1 0 1 1 1 1 0 0 0
0 0 1 0 0 0 1 1 0 0 0 1 0 0
0 1 1 0 0 1 0 1 0 0 1 1 0
1 0 1 0 1 1 1 1 0 1 0 1
1 1 1 1 0 0 0 1 1 1 1
0 0 0 1 0 0 1 0 0 0
0 0 1 1 0 1 1 0 0
0 1 0 1 1 0 1 0
1 1 1 0 1 1 1
0 0 1 1 0 0
0 1 0 1 0
1 1 1 1
0 0 0
0 0
0

(0 , 0, 0, 1) (1 , 0, 0, 1) (0 , 1, 0, 1) (1 , 1, 0, 1)

0 1 1 1 1 1 1 0 1 0 0 0 0 1 0 1 1 1 1 1 1 0
1 0 0 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 0 0 1
1 0 0 0 0 1 0 0 1 0 0 1 0 0 1 0 0 0 0 1
1 0 0 0 1 1 0 1 1 0 1 1 0 1 1 0 0 0 1
1 0 0 1 0 1 1 0 1 1 0 1 1 0 1 0 0 1
1 0 1 1 1 0 1 1 0 1 1 0 1 1 1 0 1
1 1 0 0 1 1 0 1 1 0 1 1 0 0 1 1
0 1 0 1 0 1 1 0 1 1 0 1 0 1 0
1 1 1 1 1 0 1 1 0 1 1 1 1 1
0 0 0 0 1 1 0 1 1 0 0 0 0
0 0 0 1 0 1 1 0 1 0 0 0
0 0 1 1 1 0 1 1 1 0 0
0 1 0 0 1 1 0 0 1 0
1 1 0 1 0 1 0 1 1
0 1 1 1 1 1 1 0
1 0 0 0 0 0 1
1 0 0 0 0 1
1 0 0 0 1
1 0 0 1
1 0 1
1 1
0
 0 0 0 0 0 0 0 1 0 1 1 1 1 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 1 1 1 0 0 0 1 1 1 0 0 0 0 0 0
0 0 0 0 0 1 0 0 1 0 0 1 0 0 1 0 0 0 0 0
0 0 0 0 1 1 0 1 1 0 1 1 0 1 1 0 0 0 0
0 0 0 1 0 1 1 0 1 1 0 1 1 0 1 0 0 0
0 0 1 1 1 0 1 1 0 1 1 0 1 1 1 0 0
0 1 0 0 1 1 0 1 1 0 1 1 0 0 1 0
1 1 0 1 0 1 1 0 1 1 0 1 0 1 1
0 1 1 1 1 0 1 1 0 1 1 1 1 0
1 0 0 0 1 1 0 1 1 0 0 0 1
1 0 0 1 0 1 1 0 1 0 0 1
1 0 1 1 1 0 1 1 1 0 1
1 1 0 0 1 1 0 0 1 1
0 1 0 1 0 1 0 1 0
1 1 1 1 1 1 1 1
0 0 0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0
0 0 0 0
0 0 0
0 0
0
 0 0 0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 1 0 0 0
0 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 0
0 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 0
1 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 1
0 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 0
0 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 0
1 1 1 0 1 1 0 1 1 0 1 1 0 1 1 1
0 0 1 1 0 1 1 0 1 1 0 1 1 0 0
0 1 0 1 1 0 1 1 0 1 1 0 1 0
1 1 1 0 1 1 0 1 1 0 1 1 1
0 0 1 1 0 1 1 0 1 1 0 0
0 1 0 1 1 0 1 1 0 1 0
1 1 1 0 1 1 0 1 1 1
0 0 1 1 0 1 1 0 0
0 1 0 1 1 0 1 0
1 1 1 0 1 1 1
0 0 1 1 0 0
0 1 0 1 0
1 1 1 1
0 0 0
0 0
0
 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0
1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1
1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1
0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0
1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1
1 1 0 1 1 0 1 1 0 1 1 0 1 1 0 1 1
0 1 1 0 1 1 0 1 1 0 1 1 0 1 1 0
1 0 1 1 0 1 1 0 1 1 0 1 1 0 1
1 1 0 1 1 0 1 1 0 1 1 0 1 1
0 1 1 0 1 1 0 1 1 0 1 1 0
1 0 1 1 0 1 1 0 1 1 0 1
1 1 0 1 1 0 1 1 0 1 1
0 1 1 0 1 1 0 1 1 0
1 0 1 1 0 1 1 0 1
1 1 0 1 1 0 1 1
0 1 1 0 1 1 0
1 0 1 1 0 1
1 1 0 1 1
0 1 1 0
1 0 1
1 1
0

(0 , 0, 1, 1) (1 , 0, 1, 1) (0 , 1, 1, 1) (1 , 1, 1, 1)

Figure 12: The 16 triangles of DST (22) where the 4 red triangles form a basis

31

6 Parity-regular Steinhaus graphs

For any binary sequence S = (aj)1⩽j⩽n of length n, we denote by ir(S) the interlacing
of the sequence S and its reversed sequence, that is, the sequence ir(S) = (bj)1⩽j⩽2n of
length 2n deﬁned by b2j−1 = aj and b2j = an−j+1,

for all j ∈ {1, . . . , n}. For instance, for S = (101000), we have ir(S) = (100010010001).
For any positive integer n, we consider the linear map

θ : SG(n) −→ ST (2n − 1)
G (S) ↦−→ ∇∫

n,0 ir(S)

Note that the Steinhaus triangle ∇S ∈ ST (n − 1) is then a subtriangle of θ(G (S)) ∈
ST (2n − 1). Indeed, for the sequence S = (aj)1⩽j⩽n−1 and the Steinhaus triangle
θ(G (S)) = ∇∫

n,0 ir(S) = (ai,j)1⩽i⩽j⩽2n−1, the Steinhaus triangle ∇S is simply the subtri-
angle (a2i,2j)1⩽i⩽j⩽n−1, since a2,2j = aj, for all j ∈ {1, . . . , n − 1}, by deﬁnition of θ, and,
using the local rule (LR), we have

a2i,2j ≡ a2i−1,2j−1 +a2i−1,2j ≡ a2i−2,2j−2 +2a2i−2,2j−1 +a2i−2,2j ≡ a2i−2,2j−2 +a2i−2,2j (mod 2),

for all integers i and j such that 2 ⩽ i ⩽ j ⩽ n − 1. For instance, for the sequence S =
(101000), the Steinhaus triangle θ(G (S)) is depicted in Figure 13, where the subtriangle
∇S appears in red.
 0 1 1 1 1 0 0 0 1 1 1 1 0
1 0 0 0 1 0 0 1 0 0 0 1
1 0 0 1 1 0 1 1 0 0 1
1 0 1 0 1 1 0 1 0 1
1 1 1 1 0 1 1 1 1
0 0 0 1 1 0 0 0
0 0 1 0 1 0 0
0 1 1 1 1 0
1 0 0 0 1
1 0 0 1
1 0 1
1 1
0

1 0 1 0 0 0

1 1 1 0 0

0 0 1 0

0 1 1

1 0

1

Figure 13: The Steinhaus triangle θ(G (101000)) where ∇(101000) appears in red

By deﬁnition of the linear map ir, we know that the sequence ir(S) is symmetric and
σ2 (ir(S)) = 0. It follows from Proposition 4.1 that the sequence ∫
n,0 ir(S) is symmetric
too. Therefore, using Proposition 4.2, we have

θ(G (S)) = ∇
∫
n,0 ir(S) ∈ HST (2n − 1),

for all G (S) ∈ SG(n). Moreover, using Lemma 4.4 and since the middle term of the
sequence ∫

n,0 ir(S) is 0 by deﬁnition, we obtain that

σ2 (∫
n,0 ir(S)
) = 0,

32

for any sequence S of length n − 1.
The main result of this section is to show that the restriction of θ to the linear sub-
space of even Steinhaus graphs ESG(n) induces an isomorphism between ESG(n) and
DST 0(2n − 1), for all positive integers n.

Theorem 6.1. Let S be a binary sequence of length n − 1 ⩾ 0. Then, the Steinhaus graph
G (S) is even if and only if the Steinhaus triangle θ (G (S)) is dihedrally symmetric.

The proof is based on the following

Lemma 6.2. Let S be a binary sequence of length n − 1 ⩾ 0. Let vi denote the ith vertex
of the Steinhaus graph G (S), for all i ∈ {1, . . . , n}, and let θ (G (S)) = (bi,j)1⩽i⩽j⩽2n−1 ∈
HST (2n − 1). Then, deg(v1) ≡ b1,1 (mod 2)

and, for any i ∈ {2, . . . , n}, if the (2i − 2)-th column C2i−2 = (bj,2i−2)1⩽j⩽2i−2 of θ (G (S))
is symmetric, then deg(vi) ≡ bi,2i−1 (mod 2).

Proof of Lemma 6.2. We consider the adjacency matrix M (S) = (ai,j)1⩽i,j⩽n of the Stein-
haus graph G (S). We already know that the upper-triangular part of M (S), i.e., the
Steinhaus triangle ∇S = (ai,j)1⩽i<j⩽n, corresponds to the subtriangle (b2i,2j)1⩽i⩽j⩽n−1
of θ (G (S)). In other words, we have ai,j = b2i,2j−2, for all integers i and j such that
1 ⩽ i < j ⩽ n. Then,
 deg(v1) =
 n∑

j=2 a1,j =
 n∑

j=2 b2,2j−2 =
 n−1∑

j=1 b2,2j, (11)

deg(vi) =
 i−1∑

j=1 aj,i +
 n∑

j=i+1 ai,j =
 i−1∑

j=1 b2j,2i−2 +
 n∑

j=i+1 b2i,2j−2 =
 i−1∑

j=1 b2j,2i−2 +
 n−1∑

j=i b2i,2j, (12)

for all i ∈ {2, . . . , n − 1}, and

deg(vn) =
 n−1∑

j=1 aj,n =
 n−1∑

j=1 b2j,2n−2. (13)

We claim that n−1∑

j=i b2i,2j =
 n+i−1∑

j=2i b2i,j, (14)

for all i ∈ {1, . . . , n − 1}. Since θ (G (S)) is horizontally symmetric, we know that its ith
row Ri = (bi,j)i⩽j⩽2n−1 is symmetric, for all i ∈ {1, . . . , 2n − 1}. Let i ∈ {1, . . . , n − 1}.
Since the sequence R2i is symmetric of even length 2(n − i) with b2i,j = b2i,2n−1+2i−j, for
all j ∈ {2i, . . . , 2n − 1}, we obtain the following identities by dividing in half σ(R2i) in
two diﬀerent ways

σ(R2i) =
 2n−1∑

j=2i b2i,j =
 n−1∑

j=i b2i,2j +
 n−1∑

j=i b2i,2j+1 =
 n−1∑

j=i b2i,2j +
 n−1∑

j=i b2i,2n−1+2i−(2j+1) = 2
 n−1∑

j=i b2i,2j,

33

and

σ(R2i) =
 2n−1∑

j=2i b2i,j =
 n+i−1∑

j=2i b2i,j +
 2n−1∑

j=n+i b2i,j =
 n+i−1∑

j=2i b2i,j +
 2n−1∑

j=n+i b2i,2n−1+2i−j = 2
 n+i−1∑

j=2i b2i,j.

Combining these two identities, the claim (14) is proved.
Using (14) and the local rule, we deduce from (11) that

deg(v1) =
 n−1∑

j=1 b2,2j =
 n∑

j=2 b2,j ≡
 n∑

j=2 (b1,j−1+b1,j) =
 n−1∑

j=1 b1,j +
 n∑

j=2 b1,j ≡ b1,1+b1,n (mod 2).

(15)
Now, let i ∈ {2, . . . , n} and suppose that the column C2i−2 of even size 2i−2 is symmetric.
Then, as for (14), using a double counting of σ(C2i−2), we obtain the following identity

i−1∑

j=1 b2j,2i−2 =
 2i−2∑

j=i bj,2i−2. (16)

Using (14), (16) and the local rule, we deduce from (12) that

deg(vi) =
 i−1∑

j=1 b2j,2i−2 +
 n−1∑

j=i b2i,2j =
 2i−2∑

j=i bj,2i−2 +
 n+i−1∑

j=2i b2i,j

≡
 2i−2∑

j=i (bj,2i−1 + bj+1,2i−1) +
 n+i−1∑

j=2i (b2i−1,j−1 + b2i−1,j)

=
 2i−2∑

j=i bj,2i−1 +
 2i−1∑

j=i+1 bj,2i−1 +
 n+i−2∑

j=2i−1 b2i−1,j +
 n+i−1∑

j=2i b2i−1,j

≡ bi,2i−1 + b2i−1,2i−1 + b2i−1,2i−1 + b2i−1,n+i−1 ≡ bi,2i−1 + b2i−1,n+i−1 (mod 2),
(17)
if i ∈ {2, . . . , n − 1}, and from (13) that

deg(vn) =
 n−1∑

j=1 b2j,2n−2 =
 2n−2∑

j=n bj,2n−2 ≡
 2n−2∑

j=n (bj,2n−1 + bj+1,2n−1)

=
 2n−2∑

j=n bj,2n−1 +
 2n−1∑

j=n+1 bj,2n−1 ≡ bn,2n−1 + b2n−1,2n−1 (mod 2).
 (18)

Since θ (G (S)) is horizontally symmetric, we know that b2n−1−2i,2n−1−i = 0, for all
i ∈ {0, . . . , n − 2}, by Proposition 4.3. Moreover, by deﬁnition of θ(G (S)) = ∇∫

n,0 ir(S),
we have that b1,n = 0. Therefore, we have

b2i+1,n+i = 0, for all i ∈ {0, . . . , n − 1}. (19)

Finally, by combining (15), (17) and (18) with (19), the result of Lemma 6.2 is proved.

34

Proof of Theorem 6.1. First, suppose that θ (G (S)) is dihedrally symmetric. Then, the
Steinhaus triangle r (θ (G (S))) = θ (G (S)) is horizontally symmetric and the column Ci
of θ (G (S)) is symmetric, for all i ∈ {1, . . . , 2n − 1}. It follows from Lemma 6.2 that

deg(vi) ≡ bi,2i−1 (mod 2),

for all i ∈ {1, . . . , n}. Since θ (G (S)) is dihedrally symmetric, we know from Corollary 5.3
that bi,2i−1 = 0, for all i ∈ {1, . . . , n − 1}. Moreover, since θ (G (S)) ∈ DST 0(2n − 1), we
have bn,2n−1 = b1,n = 0. Therefore, for every i ∈ {1, . . . , n}, the vertex vi is of even degree
and the Steinhaus graph G (S) is even.
Conversely, suppose that the Steinhaus graph G (S) is even. We prove, by induction
on i, that all the columns Ci of θ (G (S)) are symmetric. From Lemma 6.2, we know
that b1,1 ≡ deg(v1) mod 2. Since deg(v1) is even, it follows that b1,1 = 0. Moreover, since
b2,2 ≡ b1,1 + b1,2 ≡ b1,2 mod 2, we have that b1,2 = b2,2. Therefore, the columns C1 and C2
are symmetric. Suppose now that the columns C1, C2, . . . , C2i are symmetric, for some
i ∈ {1, . . . , n − 1}. First, since C2i is symmetric of even length, we know from Lemma 4.4
that σ2 (C2i) = 0. Therefore, since ∂C2i+1 = C2i, it follows from Proposition 4.1 that C2i+1
is symmetric. Moreover, since C2i is symmetric and the vertex vi+1 is of even degree, we
obtain by Lemma 6.2 that
 bi+1,2i+1 ≡ deg(vi+1) ≡ 0 (mod 2).

Since bi+1,2i+1 = 0, we obtain from Lemma 4.4 that σ2 (C2i+1) = 0. Therefore, when
i < n − 1, since ∂C2i+2 = C2i+1, using Proposition 4.1 again, we have that C2i+2 is
symmetric. This concludes the proof that all the columns Ci of θ (G (S)) are symmetric.
Obviously, it follows that the Steinhaus triangle r (θ (G (S))) is horizontally symmetric.
Finally, since the triangles θ (G (S)) and r (θ (G (S))) are horizontally symmetric, we know
from Proposition 5.1 that θ (G (S)) is dihedrally symmetric.

Corollary 6.3. For any positive integer n, the restriction

θ|ESG(n) : ESG(n) −→ DST 0(2n − 1)

is an isomorphism.

Proof. Let n be a positive integer. We consider the linear map

ψ : DST 0(2n − 1) −→ ESG(n)

(ai,j)1⩽i⩽j⩽2n−1 ↦−→ G (
(a2,2j)1⩽j⩽n−1)

We know from Theorem 6.1 that the linear maps θ|ESG(n) and ψ are well deﬁned. Moreover,
it is easy to verify that ψ ◦ θ|ESG(n) = idESG(n) and θ|ESG(n) ◦ ψ = idDST 0(2n−1). This
completes the proof.

This new result permits us to obtain the following two corollaries that were ﬁrst proved
in [16].

Corollary 6.4. dim ESG(n) = ⌊ n−1
3 ⌋
, for all positive integers n.

Proof. Since the vector space ESG(n) is isomorphic to DST 0(2n − 1) by Corollary 6.3,
we deduce from Corollary 5.8 that

dim ESG(n) = dim DST 0(2n − 1) = ⌊ 2n − 1
6
 ⌋ + δ4,(2n−1 mod 6) = ⌊ 2n − 1
6
 ⌋ = ⌊ n − 1
3
 ⌋ ,

for all positive integers n.
 35

Corollary 6.5. The Steinhaus matrix M (S) associated to an even Steinhaus graph G (S)
is doubly symmetric, i.e., all the diagonals of M (S) are symmetric.

Remark. This was a key result in the ﬁrst proof of the formula dim ESG(n) = ⌊ n−1
3 ⌋ in
[16]. Another simple proof of this result can also be found in [10].

Proof. Let S be a binary sequence of length n − 1 whose associated Steinhaus graph
G (S) is even. In other words, we want to prove that the Steinhaus triangle r2 (∇S) is
horizontally symmetric. Let θ (G (S)) = (bi,j)1⩽i⩽j⩽2n−1. Since θ (G (S)) ∈ DST 0(2n − 1)
by Theorem 6.1, it follows that r2 (θ (G (S))) is horizontally symmetric. Therefore, the
diagonal Di = (bj,i+j)1⩽j⩽2n−1−i is symmetric, for all i ∈ {0, . . . , 2n − 2}. It follows that

bj,i+j = b2n−i−j,2n−j, (20)

for all j ∈ {1, . . . , 2n − 1 − i} and for all i ∈ {0, . . . , 2n − 2}. Let ∇S = (ai,j)1⩽i⩽j⩽n−1.
As already seen, it corresponds to the subtriangle ∇S = (b2i,2j)1⩽i⩽j⩽n−1 of θ (G (S)).
Therefore, we have ai,j = b2i,2j, for all integers i and j such that 1 ⩽ i ⩽ j ⩽ n − 1. Let
i ∈ {0, . . . , n − 2}. From (20), we obtain that

aj,i+j = b2j,2i+2j = b2n−2i−2j,2n−2j = b2(n−i−j),2(n−j) = an−i−j,n−j,

for all j ∈ {1, . . . , n−1−i}. We conclude that the diagonal (aj,i+j)1⩽j⩽n−1−i is symmetric,
for all i ∈ {0, . . . , n−2}, and the Steinhaus triangle r2 (∇S) is horizontally symmetric.

Using Theorem 6.1 and the results of Section 5, we are now ready for giving a basis
of ESG(n), for all positive integers n.

Theorem 6.6. Let n be a positive integer. The set
{
ψρ (∇S(2n−1)
2k+1,k−n+1) ∣
∣
∣
∣ k ∈ {
0, . . . , ⌊ n − 1
3
 ⌋ − 1
}}

is a basis of ESG(n), where ψρ (∇S(2n−1)
2k+1,k−n+1) = G (Sk) with

Sk = ((
k − n + 2j − 1
2k
 ) + ( k + n − 2j
2k − 2j + 3
) + ( k − n + 2
2k − 2n + 2j + 2
) mod 2
)

1⩽j⩽n−1 ,

for all k ∈ {0, . . . , ⌊ n−1
3 ⌋ − 1
}.

Proof. Let n be a positive integer. From Corollary 5.15, we know that
{
ρ (∇S
(2n−1)
2k+1,k−n+1) ∣
∣
∣
∣ k ∈ {
0, . . . , ⌊ n − 1
3
 ⌋ − 1
}}

is a basis of DST 0(2n − 1), where ρ (∇S
(2n−1)
2k+1,k−n+1) is the triangle

((k − n + 1 + j − i
2k + 2 − i
 ) + ( k + n − j
2k + 1 + i − j
) + ( k − n + i
2k + 2 + j − 2n

) mod 2
)

1⩽i⩽j⩽2n−1 ,

for all k ∈ {0, . . . , ⌊ n−1
3 ⌋ − 1
}. It follows, by Corollary 6.3, that
{
ψρ (∇S
(2n−1)
2k,k−n+1) ∣
∣
∣
∣ k ∈ {
0, . . . , ⌊ n − 1
3
 ⌋ − 1
}}

36

is a basis of ESG(n). Since ψ ((ai,j)) = G ((a2,2j)1⩽j⩽n−1), we conclude that

ψρ (∇S(2n−1)
2k+1,k−n+1) = G (Sk) ,

with

Sk = ((
k − n + 2j − 1
2k
 ) + ( k + n − 2j
2k − 2j + 3
) + ( k − n + 2
2k − 2n + 2j + 2
) mod 2
)

1⩽j⩽n−1 ,

for all k ∈ {0, 1, . . . , ⌊ n−1
3 ⌋ − 1
}.

For instance, for n = 12, we obtain

k S
(23)
2k+1,k−11 ρ (∇S
(23)
2k+1,k−11) ψ (ρ (∇S
(23)
2k+1,k−11))

0 (10101010101010101010101) ∇(01101010101010101010110) G1 = G (11111111110)
1 (01000100010001000100010) ∇(00010100010001000101000) G2 = G (01101010110)
2 (10000010100000101000001) ∇(01111110100000101111110) G3 = G (10011001000)

All the even Steinhaus graphs of order 12 are depicted in Figure 14, where the elements
of the basis {G1, G2, G3} are in red and, for every G ∈ ESG(12), the coordinate vector
(x1, x2, x3) of G = x1G1 + x2G2 + x3G3 is given.
We end this section by giving a basis of the linear subspace PRSG(n) of parity-regular
Steinhaus graphs, for all positive integers n. By deﬁnition, we know that PRSG(n) =
ESG(n) ⊔ OSG(n), where OSG(n) is the set of odd Steinhaus graphs of order n, for all
positive integers n. As already remarked, it is clear that OSG(n) = ∅, when n is odd.
For n even, we obtain the following

Proposition 6.7. For any positive integer n,

OSG(2n) = ESG(2n) + G ((0)2n−2 · (1)) .

The proof is based on the following lemma, where the linear map ι is deﬁned by

ι : SG(2n) −→ SG(2n)
G (S) ↦−→ G (S + (0)2n−2 · (1))

for all positive integers n.

Lemma 6.8. For any positive integer n, the Steinhaus graph G (S) of order 2n is even
if and only if ι (G (S)) is odd.

Proof of Lemma 6.8. We consider the respective adjacency matrices M (S) = (ai,j)1⩽i,j⩽2n
of G (S) and M (S + (0)2n−2 · (1)) = (bi,j)1⩽i,j⩽2n of ι (G (S)). Then ,it is easy to see that
{ bi,j = ai,j for all 1 ⩽ i < j ⩽ 2n − 1,
bi,2n ≡ ai,2n + 1 (mod 2) for all 1 ⩽ i ⩽ 2n − 1,

since the sequence S + (0)2n−2 · (1) only diﬀers by the last term from the sequence S. It
follows that

degG(S) (v1) =
 2n∑

j=2 a1,j ≡
 2n∑

j=2 b1,n + 1 = degι(G(S)) (v1) + 1 (mod 2),

37

1

2

3
4
5

6

7
 8
 9 10 11
 12
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 0 0
0 0

0
 0

0
 0

0
 0

0
 0 0
0 0

0
 0

0
 0

0
 0 0
0 0

0
 0

0
 0 0
0 0

0 0 0
0 0
 1

2

3
4
5

6

7
 8
 9 10 11
 12
 0 1
1 1

1
 1

1
 1

1
 1

1
 1

1
 1

1
 1

1
 1

1
 1

1
 0

0
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 1

1
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 1

1
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 1

1
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 1

1
 0 0
0 0

0
 0

0
 0

0
 0

0
 1

1
 0 0
0 0

0
 0

0
 0

0
 1

1
 0 0
0 0

0
 0

0
 1

1
 0 0
0 0

0
 1

1
 0 0
0 1

1 0 1
1 0

(0 ; 0 ; 0) (1 ; 0 ; 0)

1

2

3
4
5

6

7
 8
 9 10 11
 12
 0 0
0 1

1
 1

1
 0

0
 1

1
 0

0
 1

1
 0

0
 1

1
 1

1
 0

0
 0 1
1 0

0
 1

1
 1

1
 1

1
 1

1
 1

1
 1

1
 0

0
 1

1
 0 1
1 1

1
 0

0
 0

0
 0

0
 0

0
 0

0
 1

1
 1

1
 0 0
0 1

1
 0

0
 0

0
 0

0
 0

0
 1

1
 0

0
 0 1
1 1

1
 0

0
 0

0
 0

0
 1

1
 1

1
 0 0
0 1

1
 0

0
 0

0
 1

1
 0

0
 0 1
1 1

1
 0

0
 1

1
 1

1
 0 0
0 1

1
 1

1
 0

0
 0 1
1 0

0
 1

1
 0 1
1 1

1 0 0
0 0
 1

2

3
4
5

6

7
 8
 9 10 11
 12
 0 1
1 0

0
 0

0
 1

1
 0

0
 1

1
 0

0
 1

1
 0

0
 0

0
 0

0
 0 1
1 0

0
 1

1
 1

1
 1

1
 1

1
 1

1
 1

1
 0

0
 0

0
 0 1
1 1

1
 0

0
 0

0
 0

0
 0

0
 0

0
 1

1
 0

0
 0 0
0 1

1
 0

0
 0

0
 0

0
 0

0
 1

1
 1

1
 0 1
1 1

1
 0

0
 0

0
 0

0
 1

1
 0

0
 0 0
0 1

1
 0

0
 0

0
 1

1
 1

1
 0 1
1 1

1
 0

0
 1

1
 0

0
 0 0
0 1

1
 1

1
 1

1
 0 1
1 0

0
 0

0
 0 1
1 0

0 0 1
1 0

(0 ; 1 ; 0) (1 ; 1 ; 0)

1

2

3
4
5

6

7
 8
 9 10 11
 12
 0 1
1 0

0
 0

0
 1

1
 1

1
 0

0
 0

0
 1

1
 0

0
 0

0
 0

0
 0 1
1 0

0
 1

1
 0

0
 1

1
 0

0
 1

1
 1

1
 0

0
 0

0
 0 1
1 1

1
 1

1
 1

1
 1

1
 1

1
 0

0
 1

1
 0

0
 0 0
0 0

0
 0

0
 0

0
 0

0
 1

1
 1

1
 1

1
 0 0
0 0

0
 0

0
 0

0
 1

1
 0

0
 0

0
 0 0
0 0

0
 0

0
 1

1
 1

1
 0

0
 0 0
0 0

0
 1

1
 0

0
 1

1
 0 0
0 1

1
 1

1
 1

1
 0 1
1 0

0
 0

0
 0 1
1 0

0 0 1
1 0
 1

2

3
4
5

6

7
 8
 9 10 11
 12
 0 0
0 1

1
 1

1
 0

0
 0

0
 1

1
 1

1
 0

0
 1

1
 1

1
 0

0
 0 1
1 0

0
 1

1
 0

0
 1

1
 0

0
 1

1
 1

1
 0

0
 1

1
 0 1
1 1

1
 1

1
 1

1
 1

1
 1

1
 0

0
 1

1
 1

1
 0 0
0 0

0
 0

0
 0

0
 0

0
 1

1
 1

1
 0

0
 0 0
0 0

0
 0

0
 0

0
 1

1
 0

0
 1

1
 0 0
0 0

0
 0

0
 1

1
 1

1
 1

1
 0 0
0 0

0
 1

1
 0

0
 0

0
 0 0
0 1

1
 1

1
 0

0
 0 1
1 0

0
 1

1
 0 1
1 1

1 0 0
0 0

(0 ; 0 ; 1) (1 ; 0 ; 1)

1

2

3
4
5

6

7
 8
 9 10 11
 12
 0 1
1 1

1
 1

1
 1

1
 0

0
 0

0
 1

1
 1

1
 1

1
 1

1
 0

0
 0 0
0 0

0
 0

0
 1

1
 0

0
 1

1
 0

0
 0

0
 0

0
 1

1
 0 0
0 0

0
 1

1
 1

1
 1

1
 1

1
 0

0
 0

0
 1

1
 0 0
0 1

1
 0

0
 0

0
 0

0
 1

1
 0

0
 1

1
 0 1
1 1

1
 0

0
 0

0
 1

1
 1

1
 1

1
 0 0
0 1

1
 0

0
 1

1
 0

0
 0

0
 0 1
1 1

1
 1

1
 1

1
 0

0
 0 0
0 0

0
 0

0
 1

1
 0 0
0 0

0
 1

1
 0 0
0 1

1 0 1
1 0
 1

2

3
4
5

6

7
 8
 9 10 11
 12
 0 0
0 0

0
 0

0
 0

0
 1

1
 1

1
 0

0
 0

0
 0

0
 0

0
 0

0
 0 0
0 0

0
 0

0
 1

1
 0

0
 1

1
 0

0
 0

0
 0

0
 0

0
 0 0
0 0

0
 1

1
 1

1
 1

1
 1

1
 0

0
 0

0
 0

0
 0 0
0 1

1
 0

0
 0

0
 0

0
 1

1
 0

0
 0

0
 0 1
1 1

1
 0

0
 0

0
 1

1
 1

1
 0

0
 0 0
0 1

1
 0

0
 1

1
 0

0
 1

1
 0 1
1 1

1
 1

1
 1

1
 1

1
 0 0
0 0

0
 0

0
 0

0
 0 0
0 0

0
 0

0
 0 0
0 0

0 0 0
0 0

(0 ; 1 ; 1) (1 ; 1 ; 1)

Figure 14: The 8 graphs of ESG(12) where the 3 red graphs form a basis

38

degG(S) (vi) =
 i−1∑

j=1 aj,i +
 2n∑

j=i+1 ai,j ≡
 i−1∑

j=1 bj,i +
 2n∑

j=i+1 bi,j + 1 = degι(G(S)) (vi) + 1 (mod 2),

for all i ∈ {2, . . . , 2n − 1}, and

degG(S) (v2n) =
 2n−1∑

i=1 ai,2n ≡
 2n−1∑

i=1 bi,2n + 2n − 1 ≡ degι(G(S)) (v2n) + 1 (mod 2),

where degG(S) (vi) and degι(G(S)) (vi) are the degrees of the ith vertex of the Steinhaus
graphs G (S) and ι (G (S)), respectively, for all i ∈ {1, . . . , 2n}. Since degG(S) (vi) ≡
degι(G(S)) (vi) + 1 mod 2, for all i ∈ {1, . . . , 2n}, the result follows.

Proof of Proposition 6.7. From Lemma 6.8, it is clear that ι induces an involution on
PRSG(2n) with OSG(2n) = ι (ESG(2n)) = ESG(2n) + G ((0)2n−2 · (1)), for all positive
integers n.

It immediately follows that, for any positive integer n, we have

PRSG(2n − 1) = ESG(2n − 1) (21)

and PRSG(2n) = ESG(2n) ⊔ (ESG(2n) + G ((0)2n−2 · (1))) . (22)

Therefore, we retrieve the following

Proposition 6.9. dim PRSG(n) = ⌊ n−1
3 ⌋ + δ0,(n mod 2), for all positive integers n.

Combining the identities (21) and (22) with Theorem 6.6, we obtain the following

Theorem 6.10. Let n be a positive integer. The set
{
ψρ (∇S(2n−1)
2k+1,k−n+1) ∣
∣
∣
∣ k ∈ {
0, . . . , ⌊ n − 1
3
 ⌋ − 1
}} ,

when n is odd, or the set

{G ((0)n−2 · (1))} ∪ {
ψρ (∇S
(2n−1)
2k+1,k−n+1) ∣
∣
∣
∣ k ∈ {0, . . . , ⌊ n − 1
3
 ⌋ − 1
}} ,

when n is even, is a basis of PRSG(n), where ψρ (∇S
(2n−1)
2k+1,k−n+1) = G (Sk) with

Sk = ((
k − n + 2j − 1
2k
 ) + ( k + n − 2j
2k − 2j + 3
) + ( k − n + 2
2k − 2n + 2j + 2
) mod 2
)

1⩽j⩽n−1 ,

for all k ∈ {0, . . . , ⌊ n−1
3 ⌋ − 1
}.

For instance, for n = 12, we obtain

G0 = G (00000000001) , G1 = G (11111111110) , G2 = G (01101010110) , G3 = G (10011001000) .

All the parity-regular Steinhaus graphs of order 12 are depicted in Figure 14 for even
graphs and in Figure 15 for odd ones, where the elements of the basis {G0, G1, G2, G3}
are in red and, for every G ∈ PRSG(12), the coordinate vector (x0, x1, x2, x3) of G =
x0G0 + x1G1 + x2G2 + x3G3 is given ((x1, x2, x3) when x0 = 0 in Figure 14).

39

1

2

3
4
5

6

7
 8
 9 10 11
 12
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 1

1
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 1

1
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 1

1
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 1

1
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 1

1
 0 0
0 0

0
 0

0
 0

0
 0

0
 1

1
 0 0
0 0

0
 0

0
 0

0
 1

1
 0 0
0 0

0
 0

0
 1

1
 0 0
0 0

0
 1

1
 0 0
0 1

1 0 1
1 0
 1

2

3
4
5

6

7
 8
 9 10 11
 12
 0 1
1 1

1
 1

1
 1

1
 1

1
 1

1
 1

1
 1

1
 1

1
 1

1
 1

1
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 0

0
 0 0
0 0

0
 0

0
 0

0
 0

0
 0

0
 0 0
0 0

0
 0

0
 0

0
 0

0
 0 0
0 0

0
 0

0
 0

0
 0 0
0 0

0
 0

0
 0 0
0 0

0 0 0
0 0

(1 ; 0 ; 0 ; 0) (1 ; 1 ; 0 ; 0)

1

2

3
4
5

6

7
 8
 9 10 11
 12
 0 0
0 1

1
 1

1
 0

0
 1

1
 0

0
 1

1
 0

0
 1

1
 1

1
 1

1
 0 1
1 0

0
 1

1
 1

1
 1

1
 1

1
 1

1
 1

1
 0

0
 0

0
 0 1
1 1

1
 0

0
 0

0
 0

0
 0

0
 0

0
 1

1
 0

0
 0 0
0 1

1
 0

0
 0

0
 0

0
 0

0
 1

1
 1

1
 0 1
1 1

1
 0

0
 0

0
 0

0
 1

1
 0

0
 0 0
0 1

1
 0

0
 0

0
 1

1
 1

1
 0 1
1 1

1
 0

0
 1

1
 0

0
 0 0
0 1

1
 1

1
 1

1
 0 1
1 0

0
 0

0
 0 1
1 0

0 0 1
1 0
 1

2

3
4
5

6

7
 8
 9 10 11
 12
 0 1
1 0

0
 0

0
 1

1
 0

0
 1

1
 0

0
 1

1
 0

0
 0

0
 1

1
 0 1
1 0

0
 1

1
 1

1
 1

1
 1

1
 1

1
 1

1
 0

0
 1

1
 0 1
1 1

1
 0

0
 0

0
 0

0
 0

0
 0

0
 1

1
 1

1
 0 0
0 1

1
 0

0
 0

0
 0

0
 0

0
 1

1
 0

0
 0 1
1 1

1
 0

0
 0

0
 0

0
 1

1
 1

1
 0 0
0 1

1
 0

0
 0

0
 1

1
 0

0
 0 1
1 1

1
 0

0
 1

1
 1

1
 0 0
0 1

1
 1

1
 0

0
 0 1
1 0

0
 1

1
 0 1
1 1

1 0 0
0 0

(1 ; 0 ; 1 ; 0) (1 ; 1 ; 1 ; 0)

1

2

3
4
5

6

7
 8
 9 10 11
 12
 0 1
1 0

0
 0

0
 1

1
 1

1
 0

0
 0

0
 1

1
 0

0
 0

0
 1

1
 0 1
1 0

0
 1

1
 0

0
 1

1
 0

0
 1

1
 1

1
 0

0
 1

1
 0 1
1 1

1
 1

1
 1

1
 1

1
 1

1
 0

0
 1

1
 1

1
 0 0
0 0

0
 0

0
 0

0
 0

0
 1

1
 1

1
 0

0
 0 0
0 0

0
 0

0
 0

0
 1

1
 0

0
 1

1
 0 0
0 0

0
 0

0
 1

1
 1

1
 1

1
 0 0
0 0

0
 1

1
 0

0
 0

0
 0 0
0 1

1
 1

1
 0

0
 0 1
1 0

0
 1

1
 0 1
1 1

1 0 0
0 0
 1

2

3
4
5

6

7
 8
 9 10 11
 12
 0 0
0 1

1
 1

1
 0

0
 0

0
 1

1
 1

1
 0

0
 1

1
 1

1
 1

1
 0 1
1 0

0
 1

1
 0

0
 1

1
 0

0
 1

1
 1

1
 0

0
 0

0
 0 1
1 1

1
 1

1
 1

1
 1

1
 1

1
 0

0
 1

1
 0

0
 0 0
0 0

0
 0

0
 0

0
 0

0
 1

1
 1

1
 1

1
 0 0
0 0

0
 0

0
 0

0
 1

1
 0

0
 0

0
 0 0
0 0

0
 0

0
 1

1
 1

1
 0

0
 0 0
0 0

0
 1

1
 0

0
 1

1
 0 0
0 1

1
 1

1
 1

1
 0 1
1 0

0
 0

0
 0 1
1 0

0 0 1
1 0

(1 ; 0 ; 0 ; 1) (1 ; 1 ; 0 ; 1)

1

2

3
4
5

6

7
 8
 9 10 11
 12
 0 1
1 1

1
 1

1
 1

1
 0

0
 0

0
 1

1
 1

1
 1

1
 1

1
 1

1
 0 0
0 0

0
 0

0
 1

1
 0

0
 1

1
 0

0
 0

0
 0

0
 0

0
 0 0
0 0

0
 1

1
 1

1
 1

1
 1

1
 0

0
 0

0
 0

0
 0 0
0 1

1
 0

0
 0

0
 0

0
 1

1
 0

0
 0

0
 0 1
1 1

1
 0

0
 0

0
 1

1
 1

1
 0

0
 0 0
0 1

1
 0

0
 1

1
 0

0
 1

1
 0 1
1 1

1
 1

1
 1

1
 1

1
 0 0
0 0

0
 0

0
 0

0
 0 0
0 0

0
 0

0
 0 0
0 0

0 0 0
0 0
 1

2

3
4
5

6

7
 8
 9 10 11
 12
 0 0
0 0

0
 0

0
 0

0
 1

1
 1

1
 0

0
 0

0
 0

0
 0

0
 1

1
 0 0
0 0

0
 0

0
 1

1
 0

0
 1

1
 0

0
 0

0
 0

0
 1

1
 0 0
0 0

0
 1

1
 1

1
 1

1
 1

1
 0

0
 0

0
 1

1
 0 0
0 1

1
 0

0
 0

0
 0

0
 1

1
 0

0
 1

1
 0 1
1 1

1
 0

0
 0

0
 1

1
 1

1
 1

1
 0 0
0 1

1
 0

0
 1

1
 0

0
 0

0
 0 1
1 1

1
 1

1
 1

1
 0

0
 0 0
0 0

0
 0

0
 1

1
 0 0
0 0

0
 1

1
 0 0
0 1

1 0 1
1 0

(1 ; 0 ; 1 ; 1) (1 ; 1 ; 1 ; 1)

Figure 15: The 8 graphs of OSG(12)

40

7 Symmetric generalized Pascal triangles

Another kind of binary triangles with a similar deﬁnition than Steinhaus triangles can be
considered. A generalized Pascal triangle of size n is a triangle ∆ = (ai,j)1⩽j⩽i⩽n of 0’s
and 1’s verifying the local rule (LR), i.e., ai,j = ai−1,j−1 + ai−1,j mod 2, for all integers
i, j such that 2 ⩽ j < i ⩽ n. A generalized Pascal triangle (ai,j)1⩽j⩽i⩽n is completely
determined by its left side L = (ai,1)1⩽i⩽n and its right side R = (ai,i)1⩽i⩽n. Therefore, we
denote by ∆ (L, R) the generalized Pascal triangle generated from the sequences L and
R. The set of binary generalized Pascal triangles of size n is denoted by PT (n). Since
the set of generalized Pascal triangles is closed under addition modulo 2, it follows that
PT (n) is a vector space over Z/2Z. An example of generalized Pascal triangle of size 5
is depicted in Figure 16.
 1
1 1
1 0 0
0 1 0 0
0 1 1 0 1

Figure 16: The generalized Pascal triangle ∆ ((11100), (11001))

Since a generalized Pascal triangle is uniquely determined by its left and right sides,
which have the same ﬁrst term, the dimension of PT (n) is 2n − 1, for all positive integers
n. Moreover, there exists a natural isomorphism between PT (n) and ST (2n − 1), for all
positive integers n. Indeed, as depicted in Figure 17, a generalized Pascal triangle of size
n can be seen as a subtriangle of a Steinhaus triangle of size 2n − 1.

1 1 0 0 1 0 1 0 0
0 1 0 1 1 1 1 0
1 1 1 0 0 0 1
0 0 1 0 0 1
0 1 1 0 1
1 0 1 1
1 1 0
0 1
1

1
1 1
1 0 0
0 1 0 0
0 1 1 0 1

Figure 17: γ (∇(110010100)) = ∆ ((11100), (11001))

For any positive integer n, let γ be the linear map deﬁned by

γ : ST (2n − 1) −→ PT (n)
(ai,j)1⩽i⩽j⩽2n−1 ↦−→ (ai,n−1+j)1⩽j⩽i⩽n

The linear map γ is well deﬁned since the generalized Pascal triangles and the Steinhaus
triangles share the same local rule (LR).

Proposition 7.1. The linear map γ : ST (2n − 1) −→ PT (n) is an isomorphism.

Proof. Let ∇ = (ai,j)1⩽i⩽j⩽2n−1 ∈ ST (2n − 1) and ∆ = γ (∇) = (ai,n−1+j)1⩽j⩽i⩽n. The
linear map γ is an isomorphism since the set GLR of indices of the left and right sides of

41

∆ = (ai,n−1+j)1⩽j⩽i⩽n, i.e.,

GLR = {(i, n) | i ∈ {1, . . . , n}} ∪ {(i, n − 1 + i) | i ∈ {2, . . . , n}}

is a generating index set of ST (2n − 1). First, all the terms of the ﬁrst row (a1,j)1⩽j⩽2n−1
of ∇ can be expressed in function of the elements of the left side (ai,n)1⩽i⩽n and of the
right side (ai,n−1+i)1⩽i⩽n of ∆. Indeed, for every j ∈ {1, . . . , n}, we know from Lemma 2.1
that
 a1,j ≡
 n−j∑

k=0
 (n − j
k
 )
ak+1,n (mod 2)

and
 a1,2n−j ≡
 n−j∑

k=0
 (
n − j
k
 )ak+1,n+k (mod 2).

Since G1 = {(1, j) | j ∈ {1, . . . , 2n − 1}} is a generating index set of ST (2n − 1), we
conclude that GLR is a generating index set of ST (2n − 1) too. Therefore, the linear map
γ is an isomorphism.

As for Steinhaus triangles, the action of the dihedral group D3 = ⟨r′, h
′⟩ on PT (n)
can be considered, where the automorphisms r′ and h
′ of PT (n) are deﬁned by

r′ : PT (n) −→ PT (n)
(ai,j)1⩽j⩽i⩽n ↦−→ (an+j−i,n+1−i)1⩽j⩽i⩽n

and h
′ : PT (n) −→ PT (n)
(ai,j)1⩽j⩽i⩽n ↦−→ (ai,1−j+i)1⩽j⩽i⩽n

For instance, for L = (11100) and R = (11001) and for all g ∈ D3, the generalized Pascal
triangles g (∆ (L, R)) are depicted in Figure 18.

1
1 1
1 0 0
0 1 0 0
0 1 1 0 1
 1
0 0
0 0 1
1 0 1 1
1 1 1 0 0
 0
1 0
1 1 1
0 0 0 1
1 0 0 1 1
 1
1 1
0 0 1
0 0 1 0
1 0 1 1 0
 0
0 1
1 1 1
1 0 0 0
1 1 0 0 1
 1
0 0
1 0 0
1 1 0 1
0 0 1 1 1

 ( L; R ) r′ ( ( L; R )) r′ 2 ( ( L; R )) h
′ ( ( L; R )) r′ h
′ ( ( L; R )) r′ 2h
′ ( ( L; R ))

Figure 18: Action of D3 on ∆ ((11100), (11001))

Proposition 7.2. For any positive integer n, we have

γr = r′γ and γh = h
′γ.

Proof. First, we have

γ (r ((ai,j)1⩽i⩽j⩽2n−1)) = γ ((aj−i+1,2n−i)1⩽i⩽j⩽2n−1) = (an+j−i,2n−i)1⩽j⩽i⩽n

and r′ (γ ((ai,j)1⩽i⩽j⩽2n−1)) = r′ ((ai,n−1+j)1⩽j⩽i⩽n) = (an+j−i,2n−i)1⩽j⩽i⩽n ,

42

for all (ai,j)1⩽i⩽j⩽2n−1 ∈ ST (2n − 1). Moreover,

γ (h ((ai,j)1⩽i⩽j⩽2n−1)) = γ ((ai,2n−1−j+i)1⩽i⩽j⩽2n−1) = (ai,n+i−j)1⩽j⩽i⩽n

and h
′ (γ ((ai,j)1⩽i⩽j⩽2n−1)) = h
′ ((ai,n−1+j)1⩽j⩽i⩽n) = (ai,n+i−j)1⩽j⩽i⩽n ,

for all (ai,j)1⩽i⩽j⩽2n−1 ∈ ST (2n − 1). This completes the proof.

A generalized Pascal triangle ∆ of size n is said to be

• rotationally symmetric if r′(∆) = ∆,

• horizontally symmetric if h
′(∆) = ∆,

• dihedrally symmetric if r′(∆) = h
′(∆) = ∆.

The sets of horizontally symmetric, rotationally symmetric and dihedrally symmetric
generalized Pascal triangles of size n are denoted by HPT (n), RPT (n) and DPT (n),
respectively, for all non-negative integers n. In other words, the sets HPT (n), RPT (n)
and DPT (n) are simply the linear subspaces ker (h
′ − idPT (n)), ker (
r′ − idPT (n)) and
ker (h
′ − idPT (n)) ∩ ker (r′ − idPT (n))
, respectively, where idPT (n) is the identity map on
PT (n), for all non-negative integers n. Examples of such triangles appear in Figure 19.

1
0 0
1 0 1
1 1 1 1
0 0 0 0 0
 1
0 1
0 1 0
1 1 1 0
1 0 0 1 1
 1
1 1
0 0 0
1 0 0 1
1 1 0 1 1

Figure 19: Triangles of HPT (5), RPT (5) and DPT (5).

It is now easy to see that a symmetric generalized Pascal triangles of size n corresponds
to a symmetric Steinhaus triangle of size 2n − 1, for all positive integers n.

Proposition 7.3. For any positive integer n, a steinhaus triangle ∇, of size 2n − 1,
is horizontally, rotationally, or dihedrally symmetric if and only if the generalized Pascal
triangle γ (∇), of size n, is horizontally, rotationally, or dihedrally symmetric, respectively.

Proof. From Propositions 7.1 and 7.2.

Corollary 7.4. The linear map γ induces isomorphisms of HST (2n − 1) upon HPT (n),
RST (2n−1) upon RPT (n) and DST (2n−1) upon DPT (n), respectively, for all positive
integers n.

Proof. From Proposition 7.3.

Using the isomorphism γ and the results of the previous sections, we obtain the di-
mension and a basis for each linear subspace of symmetric generalized Pascal triangles of
size n, for all positive integers n.

Proposition 7.5. For any positive integer n, we have

43

• dim HPT (n) = n,

• dim RPT (n) = 2 ⌊ n−1
3 ⌋ + 1,

• dim DPT (n) = ⌈ n
3 ⌉
.

Proof. Let n be a positive integer. From Corollary 7.4 and Corollary 4.6, we obtain that

dim HPT (n) = dim HST (2n − 1) = ⌈ 2n − 1
2
 ⌉ = n.

Moreover, from Corollary 7.4 and Corollary 3.5, we have

dim RPT (n) = dim RST (2n − 1) = ⌊ 2n − 1
3
 ⌋ + δ1,(2n−1 mod 3)

= ⌊ 2n − 1
3
 ⌋ + δ1,(n mod 3) = 2 ⌊ n − 1
3
 ⌋ + 1.

Finally, from Corollary 7.4 and Corollary 5.11, we obtain

dim DPT (n) = dim DST (2n − 1) = ⌊ 2n + 2
6
 ⌋ + δ1,(2n−1 mod 6)

= ⌊ n + 1
3
 ⌋ + δ1,(n mod 3) = ⌈ n
3
 ⌉ .

This completes the proof.

Theorem 7.6. Let n and m be positive integers such that m = 2 ⌊ n−1
3 ⌋ + 1. For any
integers l0, . . . , lm−1, the set
{
γρ (∇S
(2n−1)
k,lk
 ) ∣
∣
∣ k ∈ {0, . . . , m − 1}}

is a basis of RPT (n), where

γρ (∇S
(2 n−1)
k,lk
 ) = ((lk + j − i + n − 1
k + 1 − i
 ) + ( lk + n − j
k + i − j − n + 1
) + (lk + i − 1
k + j − n
) mod 2
)

1 ⩽j⩽i⩽n ,

for all k ∈ {0, . . . , m − 1}.

Proof. From Theorem 3.13 and Corollary 7.4.

Theorem 7.7. Let n be a positive integer. The set
{
γ (
S(2n−1)
2(n−k)−1,−k) ∣
∣
∣ k ∈ {1, . . . , n − 1}
} ∪ {γ (∇(1)2n−1)}

is a basis of HPT (n), where

γ (∇S(2n−1)
2(n−k)−1,−k) = ((−k + j − i + n − 1
2(n − k) − i
 )

2
)
1⩽j⩽i⩽n ,

for all k ∈ {1, . . . , ⌊ n
2 ⌋}, and γ (∇(1)2n−1) = ∆ ((1) · (0)n−1, (1) · (0)n−1).

44

Proof. From Theorem 4.9 and Corollary 7.4.

Theorem 7.8. Let n and m be positive integers such that m = ⌈ n
3 ⌉
. Then, the set

{γ (U2n−1)} ∪ {
γρ (S
(2n−1)
2k+1,k−n+1) ∣
∣
∣ k ∈ {0, . . . , m − 2}
}

is a basis of DST (n), where γ (U2n−1) = ∆ ((1) · (0)n−2 · (1), (1) · (0)n−2 · (1)) and

γρ (S
(2 n−1)
2k+1 ,k−n+1 ) = (( k + j − i
2k − i + 2
) + ( k − j + 1
i − j + 2k − n + 2
) + ( k − n + i
2k + j − n + 1
) mod 2
)
1 ⩽j⩽i⩽n ,

for all k ∈ {0, . . . , m − 2}.

Proof. From Theorem 5.14 and Corollary 7.4.

We end this section by giving bases obtained from Theorem 7.6 for RPT (6), from
Theorem 7.7 for HPT (4) and from Theorem 7.8 for DPT (11).
For n = 7 and k0 = k1 = k2 = k3 = k4 = 0, we obtain the following basis
{
γρ (∇S(13)
k,0 ) ∣
∣
∣ k ∈ {0, 1, 2, 3, 4}}

of RPT (7), where

k S(13)
k,0 ρ (∇S
(13)
k,0 ) γρ (∇S
(13)
k,0 )

0 (1111111111111) ∇(0111111111110) ∆0 = ∆ ((1000001), (1000001))
1 (0101010101010) ∇(0001010101000) ∆1 = ∆ ((0100010), (0100010))
2 (0011001100110) ∇(0101001100010) ∆2 = ∆ ((1110101), (1010111))
3 (0001000100010) ∇(0100000101010) ∆3 = ∆ ((0000010), (0100000))
4 (0000111100001) ∇(1111011110001) ∆4 = ∆ ((1011001), (1001101))

All the rotationnaly symmetric generalized Pascal triangles of size 7 are depicted in Fig-
ure 20, where the elements of the basis {∆0, ∆1, ∆2, ∆3, ∆4} are in red and, for every ∆ ∈
RPT (7), the coordinate vector (x0, x1, x2, x3, x4) of ∆ = x0∆0+x1∆1+x2∆2+x3∆3+x4∆4
is given.
For n = 4, we obtain the following basis
{
γ (S
(7)
7−2k,−k) ∣
∣
∣ k ∈ {1, 2, 3}
} ∪ {γ (∇(1)7)}

of HPT (4), where
 k S
(7)
7−2k,−k γρ (∇S
(7)
7−2k,−k)

1 (1000001) ∆1 = ∆ ((0001), (0001))
2 (0100010) ∆2 = ∆ ((0011), (0011))
3 (1010101) ∆3 = ∆ ((0100), (0100))

and ∆4 = γ (∇(1)7) = ∆ ((1000), (1000)). All the horizontally symmetric generalized
Pascal triangles of size 4 are depicted in Figure 21, where the elements of the ba-
sis {∆1, ∆2, ∆3, ∆4} are in red and, for every T ∈ HPT (4), the coordinate vector
(x1, x2, x3, x4) of ∆ = x1∆1 + x2∆2 + x3∆3 + x4∆4 is given.

45

0
0 0
0 0 0
0 0 0 0
0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0 0
 1
0 0
0 0 0
0 0 0 0
0 0 0 0 0
0 0 0 0 0 0
1 0 0 0 0 0 1
 0
1 1
0 0 0
0 0 0 0
0 0 0 0 0
1 0 0 0 0 1
0 1 0 0 0 1 0
 1
1 1
0 0 0
0 0 0 0
0 0 0 0 0
1 0 0 0 0 1
1 1 0 0 0 1 1
 1
1 0
1 1 1
0 0 0 0
1 0 0 0 1
0 1 0 0 1 1
1 1 1 0 1 0 1

(0 ; 0 ; 0 ; 0 ; 0) (1 ; 0 ; 0 ; 0 ; 0) (0 ; 1 ; 0 ; 0 ; 0) (1 ; 1 ; 0 ; 0 ; 0) (0 ; 0 ; 1 ; 0 ; 0)

0
1 0
1 1 1
0 0 0 0
1 0 0 0 1
0 1 0 0 1 1
0 1 1 0 1 0 0
 1
0 1
1 1 1
0 0 0 0
1 0 0 0 1
1 1 0 0 1 0
1 0 1 0 1 1 1
 0
0 1
1 1 1
0 0 0 0
1 0 0 0 1
1 1 0 0 1 0
0 0 1 0 1 1 0
 0
0 1
0 1 0
0 1 1 0
0 1 0 1 0
1 1 1 1 1 0
0 0 0 0 0 1 0
 1
0 1
0 1 0
0 1 1 0
0 1 0 1 0
1 1 1 1 1 0
1 0 0 0 0 1 1

(1 ; 0 ; 1 ; 0 ; 0) (0 ; 1 ; 1 ; 0 ; 0) (1 ; 1 ; 1 ; 0 ; 0) (0 ; 0 ; 0 ; 1 ; 0) (1 ; 0 ; 0 ; 1 ; 0)

0
1 0
0 1 0
0 1 1 0
0 1 0 1 0
0 1 1 1 1 1
0 1 0 0 0 0 0
 1
1 0
0 1 0
0 1 1 0
0 1 0 1 0
0 1 1 1 1 1
1 1 0 0 0 0 1
 1
1 1
1 0 1
0 1 1 0
1 1 0 1 1
1 0 1 1 0 1
1 1 1 0 1 1 1
 0
1 1
1 0 1
0 1 1 0
1 1 0 1 1
1 0 1 1 0 1
0 1 1 0 1 1 0
 1
0 0
1 0 1
0 1 1 0
1 1 0 1 1
0 0 1 1 0 0
1 0 1 0 1 0 1

(0 ; 1 ; 0 ; 1 ; 0) (1 ; 1 ; 0 ; 1 ; 0) (0 ; 0 ; 1 ; 1 ; 0) (1 ; 0 ; 1 ; 1 ; 0) (0 ; 1 ; 1 ; 1 ; 0)

0
0 0
1 0 1
0 1 1 0
1 1 0 1 1
0 0 1 1 0 0
0 0 1 0 1 0 0
 1
0 0
1 0 0
1 1 0 1
0 0 1 1 1
0 0 1 0 0 0
1 0 1 1 0 0 1
 0
0 0
1 0 0
1 1 0 1
0 0 1 1 1
0 0 1 0 0 0
0 0 1 1 0 0 0
 1
1 1
1 0 0
1 1 0 1
0 0 1 1 1
1 0 1 0 0 1
1 1 1 1 0 1 1
 0
1 1
1 0 0
1 1 0 1
0 0 1 1 1
1 0 1 0 0 1
0 1 1 1 0 1 0

(1 ; 1 ; 1 ; 1 ; 0) (0 ; 0 ; 0 ; 0 ; 1) (1 ; 0 ; 0 ; 0 ; 1) (0 ; 1 ; 0 ; 0 ; 1) (1 ; 1 ; 0 ; 0 ; 1)

0
1 0
0 1 1
1 1 0 1
1 0 1 1 0
0 1 1 0 1 1
0 1 0 1 1 0 0
 1
1 0
0 1 1
1 1 0 1
1 0 1 1 0
0 1 1 0 1 1
1 1 0 1 1 0 1
 0
0 1
0 1 1
1 1 0 1
1 0 1 1 0
1 1 1 0 1 0
0 0 0 1 1 1 0
 1
0 1
0 1 1
1 1 0 1
1 0 1 1 0
1 1 1 0 1 0
1 0 0 1 1 1 1
 1
0 1
1 1 0
1 0 1 1
0 1 1 0 1
1 1 0 1 1 0
1 0 1 1 0 1 1

(0 ; 0 ; 1 ; 0 ; 1) (1 ; 0 ; 1 ; 0 ; 1) (0 ; 1 ; 1 ; 0 ; 1) (1 ; 1 ; 1 ; 0 ; 1) (0 ; 0 ; 0 ; 1 ; 1)

0
0 1
1 1 0
1 0 1 1
0 1 1 0 1
1 1 0 1 1 0
0 0 1 1 0 1 0
 1
1 0
1 1 0
1 0 1 1
0 1 1 0 1
0 1 0 1 1 1
1 1 1 1 0 0 1
 0
1 0
1 1 0
1 0 1 1
0 1 1 0 1
0 1 0 1 1 1
0 1 1 1 0 0 0
 0
1 1
0 0 1
1 0 1 1
1 1 1 0 0
1 0 0 1 0 1
0 1 0 1 1 1 0
 1
1 1
0 0 1
1 0 1 1
1 1 1 0 0
1 0 0 1 0 1
1 1 0 1 1 1 1

(1 ; 0 ; 0 ; 1 ; 1) (0 ; 1 ; 0 ; 1 ; 1) (1 ; 1 ; 0 ; 1 ; 1) (0 ; 0 ; 1 ; 1 ; 1) (1 ; 0 ; 1 ; 1 ; 1)

0
0 0
0 0 1
1 0 1 1
1 1 1 0 0
0 0 0 1 0 0
0 0 0 1 1 0 0
 1
0 0
0 0 1
1 0 1 1
1 1 1 0 0
0 0 0 1 0 0
1 0 0 1 1 0 1

(0 ; 1 ; 1 ; 1 ; 1) (1 ; 1 ; 1 ; 1 ; 1)

Figure 20: The 32 triangles of RPT (7) where the 5 red triangles form a basis

46

0
0 0
0 0 0
0 0 0 0
 0
0 0
0 0 0
1 0 0 1
 0
0 0
1 0 1
1 1 1 1
 0
0 0
1 0 1
0 1 1 0
 0
1 1
0 0 0
0 0 0 0
 0
1 1
0 0 0
1 0 0 1

(0 ; 0 ; 0 ; 0) (1 ; 0 ; 0 ; 0) (0 ; 1 ; 0 ; 0) (1 ; 1 ; 0 ; 0) (0 ; 0 ; 1 ; 0) (1 ; 0 ; 1 ; 0)

0
1 1
1 0 1
1 1 1 1
 0
1 1
1 0 1
0 1 1 0
 1
0 0
0 0 0
0 0 0 0
 1
0 0
0 0 0
1 0 0 1
 1
0 0
1 0 1
1 1 1 1
 1
0 0
1 0 1
0 1 1 0

(0 ; 1 ; 1 ; 0) (1 ; 1 ; 1 ; 0) (0 ; 0 ; 0 ; 1) (1 ; 0 ; 0 ; 1) (0 ; 1 ; 0 ; 1) (1 ; 1 ; 0 ; 1)

1
1 1
0 0 0
0 0 0 0
 1
1 1
0 0 0
1 0 0 1
 1
1 1
1 0 1
1 1 1 1
 1
1 1
1 0 1
0 1 1 0

(0 ; 0 ; 1 ; 1) (1 ; 0 ; 1 ; 1) (0 ; 1 ; 1 ; 1) (1 ; 1 ; 1 ; 1)

Figure 21: The 16 triangles of HPT (4) where the 4 red triangles form a basis

For n = 11, we obtain the following basis

{γ (U21)} ∪ {
γρ (∇S
(21)
2k+1,k−10) ∣
∣
∣ k ∈ {0, 1, 2}}

of DPT (11), where ∆0 = γ (U21) = ∆ ((10000000001), (10000000001)) and

k S
(21)
2k+1 ,k−10 ρ (∇S
(21)
2k+1 ,k−10 ) γρ (∇S
(21)
2k+1 ,k−10 )

0 (010101010101010101010) ∇(000101010101010101000) ∆1 = ∆ ((01000000010), (01000000010))
1 (100010001000100010001) ∇(011110001000100011110) ∆2 = ∆ ((00110001100), (00110001100))
2 (000001010000010100000) ∇(000000010000010000000) ∆3 = ∆ ((00010001000), (00010001000))

All the dihedrally symmetric generalized Pascal triangles of size 11 are depicted in
Figure 22, where the elements of the basis {∆0, ∆1, ∆2, ∆3} are in red and, for every
∆ ∈ DPT (11), the coordinate vector (x0, x1, x2, x3) of ∆ = x0∆0 + x1∆1 + x2∆2 + x3∆3
is given.

8 Generalizations and open problems

In this section, we propose to extend the study of symmetric binary Steinhaus triangles in
two directions: in higher dimension with the binary Steinhaus tetrahedra and for triangles
of numbers in Z/mZ with a local rule for which the set of triangles is closed under the
action of the dihedral group D3.

8.1 Symmetric binary tetrahedra

A binary Steinhaus tetrahedron of size n is a tetrahedron (ai,j,k)1⩽i⩽j⩽k⩽n of 0’s and 1’s
verifying the local rule

ai,j,k ≡ ai−1,j−1,k−1 + ai−1,j−1,k + ai−1,j,k (mod 2), (LR2)

47

0
0 0
0 0 0
0 0 0 0
0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0 0
 1
0 0
0 0 0
0 0 0 0
0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0 0 1
 0
1 1
0 0 0
0 0 0 0
0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0 1
0 1 0 0 0 0 0 0 0 1 0
 1
1 1
0 0 0
0 0 0 0
0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0 0
0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0 1
1 1 0 0 0 0 0 0 0 1 1

(0 ; 0 ; 0 ; 0) (1 ; 0 ; 0 ; 0) (0 ; 1 ; 0 ; 0) (1 ; 1 ; 0 ; 0)

0
0 0
1 0 1
1 1 1 1
0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0 0
1 0 0 0 0 0 0 1
1 1 0 0 0 0 0 1 1
0 0 1 0 0 0 0 1 0 0
0 0 1 1 0 0 0 1 1 0 0
 1
0 0
1 0 1
1 1 1 1
0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0 0
1 0 0 0 0 0 0 1
1 1 0 0 0 0 0 1 1
0 0 1 0 0 0 0 1 0 0
1 0 1 1 0 0 0 1 1 0 1
 0
1 1
1 0 1
1 1 1 1
0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0 0
1 0 0 0 0 0 0 1
1 1 0 0 0 0 0 1 1
1 0 1 0 0 0 0 1 0 1
0 1 1 1 0 0 0 1 1 1 0
 1
1 1
1 0 1
1 1 1 1
0 0 0 0 0
0 0 0 0 0 0
0 0 0 0 0 0 0
1 0 0 0 0 0 0 1
1 1 0 0 0 0 0 1 1
1 0 1 0 0 0 0 1 0 1
1 1 1 1 0 0 0 1 1 1 1

(0 ; 0 ; 1 ; 0) (1 ; 0 ; 1 ; 0) (0 ; 1 ; 1 ; 0) (1 ; 1 ; 1 ; 0)

0
0 0
0 0 0
1 0 0 1
0 1 0 1 0
0 1 1 1 1 0
0 1 0 0 0 1 0
1 1 1 0 0 1 1 1
0 0 0 1 0 1 0 0 0
0 0 0 1 1 1 1 0 0 0
0 0 0 1 0 0 0 1 0 0 0
 1
0 0
0 0 0
1 0 0 1
0 1 0 1 0
0 1 1 1 1 0
0 1 0 0 0 1 0
1 1 1 0 0 1 1 1
0 0 0 1 0 1 0 0 0
0 0 0 1 1 1 1 0 0 0
1 0 0 1 0 0 0 1 0 0 1
 0
1 1
0 0 0
1 0 0 1
0 1 0 1 0
0 1 1 1 1 0
0 1 0 0 0 1 0
1 1 1 0 0 1 1 1
0 0 0 1 0 1 0 0 0
1 0 0 1 1 1 1 0 0 1
0 1 0 1 0 0 0 1 0 1 0
 1
1 1
0 0 0
1 0 0 1
0 1 0 1 0
0 1 1 1 1 0
0 1 0 0 0 1 0
1 1 1 0 0 1 1 1
0 0 0 1 0 1 0 0 0
1 0 0 1 1 1 1 0 0 1
1 1 0 1 0 0 0 1 0 1 1

(0 ; 0 ; 0 ; 1) (1 ; 0 ; 0 ; 1) (0 ; 1 ; 0 ; 1) (1 ; 1 ; 0 ; 1)

0
0 0
1 0 1
0 1 1 0
0 1 0 1 0
0 1 1 1 1 0
0 1 0 0 0 1 0
0 1 1 0 0 1 1 0
1 1 0 1 0 1 0 1 1
0 0 1 1 1 1 1 1 0 0
0 0 1 0 0 0 0 0 1 0 0
 1
0 0
1 0 1
0 1 1 0
0 1 0 1 0
0 1 1 1 1 0
0 1 0 0 0 1 0
0 1 1 0 0 1 1 0
1 1 0 1 0 1 0 1 1
0 0 1 1 1 1 1 1 0 0
1 0 1 0 0 0 0 0 1 0 1
 0
1 1
1 0 1
0 1 1 0
0 1 0 1 0
0 1 1 1 1 0
0 1 0 0 0 1 0
0 1 1 0 0 1 1 0
1 1 0 1 0 1 0 1 1
1 0 1 1 1 1 1 1 0 1
0 1 1 0 0 0 0 0 1 1 0
 1
1 1
1 0 1
0 1 1 0
0 1 0 1 0
0 1 1 1 1 0
0 1 0 0 0 1 0
0 1 1 0 0 1 1 0
1 1 0 1 0 1 0 1 1
1 0 1 1 1 1 1 1 0 1
1 1 1 0 0 0 0 0 1 1 1

(0 ; 0 ; 1 ; 1) (1 ; 0 ; 1 ; 1) (0 ; 1 ; 1 ; 1) (1 ; 1 ; 1 ; 1)

Figure 22: The 16 triangles of DPT (11) where the 4 red triangles form a basis

48

for all integers i, j, k such that 2 ⩽ i ⩽ j ⩽ k ⩽ n. The set of Steinhaus tetrahedra of
size n is denoted by ST 4(n). Since a Steinhaus tetrahedron (ai,j,k)1⩽i⩽j⩽k⩽n is uniquely
determined by its ﬁrst row (a1,j,k)1⩽j⩽k⩽n, it follows that ST 4(n) is a vector space over
Z/2Z of dimension (n+1
2 )
. An example of Steinhaus tetrahedron of size 5 is depicted in
Figure 23.
 1 1 0 1 0
1 1 1 1
1 0 0
0 0
1
 0 0 0 0
1 0 0
1 0
1
 1 0 0
0 0
0 1 0
0 1

Figure 23: A Steinhaus tetrahedron of size 5

The symmetry group of a regular tetrahedron is constituted by the identity, 11 ro-
tations (8 rotations by ± 2π
3 around an axis passing through a vertex and the middle of
the opposite side and 3 rotations by π
2 around an axis passing through the middle of two
opposite edges), 6 reﬂections and 6 rotoﬂections. This symmetry group is isomorphic to
S4 and the subset of rotations is a subgroup of order 12 isomorphic to A4.
From the local rule (LR2), for any Steinhaus tetrahedron T and for all g ∈ S4, it is
easy to see that g(T ) is also a Steinhaus tetrahedron, of the same size.

Problem 8.1. For any subgroup G of S4 and any non-negative integer n, we consider the
linear subspace of Steinhaus tetrahedra of size n deﬁned by

ST 4(n)
G = {T ∈ ST 4(n) | ∀g ∈ G, g (T ) = T } .

The problem is then to characterize ST 4(n)
G, to determine its dimension and a basis, for
all integers n and all subgroups G of S4.

8.2 Symmetric triangles in Z/mZ

Triangles similar to binary Steinhaus triangles can be considered for other kinds of num-
bers. In [4], the authors study triangles deﬁned from quasigroups. A quasigroup (G, ⋆)
is a ﬁnite set G with a binary operation ⋆ such that, for all a, b ∈ G, there exist unique
x, y ∈ G for which a ⋆ x = b and y ⋆ a = b. A ∇⋆-conﬁguration of size n is a triangle
(ai,j)1⩽i⩽j⩽n of elements in (G, ⋆) verifying the local rule

ai,j = ai−1,j−1 ⋆ ai−1,j,

for all integers i, j such that 2 ⩽ i ⩽ j ⩽ n. For (G, ⋆) = (Z/2Z, +), a ∇⋆-conﬁguration
is simply a binary Steinhaus triangle.
A quasigroup (G, ⋆) is said to be semisymmetric if y ⋆ (x ⋆ y) = x, for all x, y ∈ G. It
is easy to see that, for a semisymmetric quasigroup (G, ⋆), the set of ∇⋆-conﬁgurations is
closed under the 120 degrees rotation. Moreover, if (G, ⋆) is a commutative quasigroup,
the set of ∇⋆-conﬁgurations is also closed under the horizontal reﬂection.
A ∇⋆-conﬁguration is said to be rotationally symmetric if it is invariant under rotation
and is said to be dihedrally symmetric if it is invariant under rotation and horizontal
reﬂection (under the action of D3).
 49

The rotationally symmetric ∇⋆-conﬁgurations, for semisymmetric quasigroups, and
the dihedrally symmetric ∇⋆-conﬁgurations, for commutative semisymmetric quasigroups,
have been studied in [4]. Similar results than Propositions 3.2 and 5.4 are established and
the cardinality of sets of rotationnaly and dihedrally ∇⋆-conﬁgurations are given.

Theorem 8.2 (Theorem 3.4 in [4]). Let (G, ⋆) be a semisymmetric quasigroup. The
number conf R(n) of rotationally symmetric ∇⋆-conﬁgurations of size n is given by

conf R(n) =
 



 |G|
k if n = 3k,
|G|
k+1 if n = 3k + 1,
|Fix(⋆)||G|
k if n = 3k + 2,

where Fix(⋆) = {x ∈ G | x ⋆ x = x}.

Theorem 8.3 (Theorem 3.16 in [4]). Let (G, ⋆) be a commutative semisymmetric quasi-
group. The number conf D(n) of dihedrally symmetric ∇⋆-conﬁgurations of size n is given
by
 conf D(n) =
 



 |G|
k if n = 6k,
|G|
k+1 if n = 6k + 1,
|Fix(⋆)||G|
k if n = 6k + 2,
|G|
k+1 if n = 6k + 3,
|G|
k+1 if n = 6k + 4,
|Fix(⋆)||G|
k+1 if n = 6k + 5,

where Fix(⋆) = {x ∈ G | x ⋆ x = x}.

Suppose now that G = Z/mZ, with m ⩾ 2, and let ⋆ be the binary operation deﬁned by
x⋆y = −(x+y), for all x, y ∈ Z/mZ. Then, the quasigroup (Z/mZ, ⋆) is commutative and
semisymmetric. We are interested in the study of the sets of rotationally symmetric ∇⋆-
conﬁgurations and of dihedrally symmetric ∇⋆-conﬁgurations of size n in (Z/mZ, ⋆), that
we denote by RSC(Z/mZ,⋆)(n) and DSC(Z/mZ,⋆)(n), respectively. Examples of rotationally
and dihedrally symmetric ∇⋆-conﬁgurations of Z/6Z are depicted in Figure 24.

0 1 1 1 5 3 5 0
5 4 4 0 4 4 1
3 4 2 2 4 1
5 0 2 0 1
1 4 4 5
1 4 3
1 5
0
 0 3 5 3 3 5 3 0
3 4 4 0 4 4 3
5 4 2 2 4 5
3 0 2 0 3
3 4 4 3
5 4 5
3 3
0

Figure 24: Triangles in RSC(Z/6Z,⋆)(8) and DSC(Z/6Z,⋆)(8)

It is clear that RSC(Z/mZ,⋆)(n) and DSC(Z/mZ,⋆)(n) are submodule of the free Z/mZ-
module of ∇⋆-conﬁgurations.

Problem 8.4. Let m be a positive integer. For any positive integer n and each submodule
RSC(Z/mZ,⋆)(n) and DSC(Z/mZ,⋆)(n), determine its length and a generating set.

50

References

[1] Maxime Augier and Shalom Eliahou. Parity-regular Steinhaus graphs. Math. Comp.,
77(263):1831–1839, 2008.

[2] Craig Bailey and Wayne Dymacek. Regular Steinhaus graphs. Congr. Numer., 66:45–
47, 1988. Nineteenth Southeastern Conference on Combinatorics, Graph Theory, and
Computing (Baton Rouge, LA, 1988).

[3] André Barbé. Symmetric patterns in the cellular automaton that generates Pascal’s
triangle modulo 2. Discrete Appl. Math., 105(1-3):1–38, 2000.

[4] André Barbé and Fritz von Haeseler. Cellular automata, quasigroups and symmetries.
Aequationes Math., 62(3):211–248, 2001.

[5] André Barbé and Fritz von Haeseler. The Pascal matroid as a home for generating
sets of cellular automata conﬁgurations deﬁned by quasigroups. Theoret. Comput.
Sci., 325(2):171–214, 2004.

[6] André Barbé and Fritz von Haeseler. Frame cellular automata: conﬁgurations, gen-
erating sets and related matroids. Discrete Math., 309(6):1222–1254, 2009.

[7] Josep M. Brunat and Montserrat Maureso. Symmetries in Steinhaus triangles and
in generalized Pascal triangles. Integers, 11:A1, 2011.

[8] Gerard J. Chang, Bhaskar DasGupta, Wayne M. Dymàček, Martin Fürer, Matthew
Koerlin, Yueh-Shin Lee, and Tom Whaley. Characterizations of bipartite Steinhaus
graphs. Discrete Math., 199(1-3):11–25, 1999.

[9] Jonathan Chappelon. On a problem of Molluzzo concerning Steinhaus triangles in
ﬁnite cyclic groups. Integers, 8(1):A37, 2008.

[10] Jonathan Chappelon. Regular Steinhaus graphs of odd degree. Discrete Math.,
309(13):4545–4554, 2009.

[11] Jonathan Chappelon. A universal sequence of integers generating balanced Steinhaus
ﬁgures modulo an odd number. J. Combin. Theory Ser. A, 118(1):291–315, 2011.

[12] Jonathan Chappelon. Balanced simplices. Adv. in Appl. Math., 62:74–117, 2015.

[13] Jonathan Chappelon. Periodic balanced binary triangles. Discrete Math. Theor.
Comput. Sci., 19(3):#13, 2017.

[14] Jonathan Chappelon and Shalom Eliahou. On the problem of Molluzzo for the
modulus 4. Integers, 12:A18, 2012.

[15] Franz A. Delahan. Induced embeddings in Steinhaus graphs. J. Graph Theory,
29(1):1–9, 1998.

[16] Wayne M. Dymacek. Steinhaus graphs. In Proceedings of the Tenth Southeastern
Conference on Combinatorics, Graph Theory and Computing (Florida Atlantic Univ.,
Boca Raton, Fla., 1979), Congress. Numer., XXIII–XXIV, pages 399–412. Utilitas
Math., Winnipeg, Man., 1979.
 51

[17] Wayne M. Dymacek. Bipartite Steinhaus graphs. Discrete Math., 59(1-2):9–20, 1986.

[18] Wayne M. Dymacek and Tom Whaley. Generating strings for bipartite Steinhaus
graphs. Discrete Math., 141(1-3):95–107, 1995.

[19] Wayne M. Dymàček, Jean-Guy Speton, and Tom Whaley. Planar Steinhaus graphs.
In Proceedings of the Thirty-ﬁrst Southeastern International Conference on Combi-
natorics, Graph Theory and Computing (Boca Raton, FL, 2000), volume 144, pages
193–206, 2000.

[20] S. Eliahou, J. M. Marín, and M. P. Revuelta. Zero-sum balanced binary sequences.
Integers, 7(2):A11, 2007.

[21] Shalom Eliahou and Delphine Hachez. On a problem of Steinhaus concerning binary
sequences. Experiment. Math., 13(2):215–229, 2004.

[22] Shalom Eliahou and Delphine Hachez. On symmetric and antisymmetric balanced
binary sequences. Integers, 5(1):A6, 2005.

[23] Heiko Harborth. Solution of Steinhaus’s problem with plus and minus signs. J.
Combinatorial Theory Ser. A, 12:253–259, 1972.

[24] John C. Molluzzo. Steinhaus graphs. In Theory and applications of graphs (Proc. In-
ternat. Conf., Western Mich. Univ., Kalamazoo, Mich., 1976), volume 642 of Lecture
Notes in Math., pages 394–402. Springer, Berlin, 1978.

[25] Melvyn B. Nathanson. Derivatives of binary sequences. SIAM J. Appl. Math., 21:407–
412, 1971.

[26] Hugo Steinhaus. Sto zadań. Państwowe Wydawnictwo Naukowe, Warsaw, 1958.

[27] Hugo Steinhaus. One hundred problems in elementary mathematics. Basic Books,
Inc., Publishers, New York, 1964. With a foreword by Martin Gardner.

52
