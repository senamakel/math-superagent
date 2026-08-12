<!-- source: https://arxiv.org/pdf/math/9712213 | converted from PDF -->

arXiv:math/9712213v1  [math.CO]  2 Dec 1997
Deformations of Coxeter Hyperplane
Arrangements

Alexander Postnikov

apost@math.mit.edu
 Richard P. Stanley

rstan@math.mit.edu

Department of Mathematics
Massachusetts Institute of Technology
Cambridge, MA 02139

Version of 14 April 1997
(Not quite complete)

Abstract

We investigate several hyperplane arrangements that can be viewed as
deformations of Coxeter arrangements. In particular, we prove a conjecture
of Linial and Stanley that the number of regions of the arrangement

xi − xj = 1, 1 ≤ i < j ≤ n,

is equal to the number of alternating trees on n + 1 vertices. Remarkably,
these numbers have several additional combinatorial interpretations in terms
of binary trees, partially ordered sets, and tournaments. More generally, we
give formulae for the number of regions and the Poincar´e polynomial of certain
ﬁnite subarrangements of the aﬃne Coxeter arrangement of type An−1. These
formulae enable us to prove a “Riemann hypothesis” on the location of zeros
of the Poincar´e polynomial. We also consider some generic deformations of
Coxeter arrangements of type An−1.

1 Introduction

The Coxeter arrangement of type An−1 is the arrangement of hyperplanes given by

xi − xj = 0, 1 ≤ i < j ≤ n. (1.1)

This arrangement has n! regions. They correspond to n! diﬀerent ways of ordering
the sequence x1, . . . , xn.
In the paper we extend this simple, nevertheless important, result to the case
of a general class of arrangements which can be viewed as deformations of the
arrangement (1.1).
 1

One special case of such deformations is the arrangement given by

xi − xj = 1, 1 ≤ i < j ≤ n. (1.2)

We will call it the Linial arrangement. This arrangement was ﬁrst considered by
N. Linial and S. Ravid. They calculated its number of regions and the Poincar´e
polynomial for n ≤ 9. On the basis of this numerical data the second author of the
present paper made a conjecture that the number of regions of (1.2) is equal to the
number of alternating trees on n + 1 vertices (see [25]). A tree T on the vertices
1, 2, . . . , n + 1 is alternating if the vertices in any path in T alternate, i.e., form an
up-down or down-up sequence. Equivalently, every vertex is either less than all its
neighbors or greater than all its neighbors. These trees ﬁrst appeared in [10], and
in [20] a formula for the number of such trees on n + 1 vertices was proved. In this
paper we provide a proof of the conjecture on the number of regions of the Linial
arrangement.
In fact, we prove a more general result for truncated aﬃne arrangements, which
are certain ﬁnite subarrangements of the aﬃne hyperplane arrangement of type ̃An−1
(see Section 9). As a byproduct we get an amazing theorem on the location of zeros
of Poincar´e polynomials of these arrangements. This theorem says that in one case
all zeros are real, whereas in the other case all zeros have the same real part.
The paper is organized as follows. In Section 2 we give the basic notions of
hyperplane arrangement, number of regions, Poincar´e polynomial, and intersection
poset. In Section 3 we describe the arrangements we will be concerned with in
this paper—deformations of the arrangement (1.1). In Section 4 we review several
general theorems on hyperplane arrangements. Then in Section 5 we apply these
theorems to deformed Coxeter arrangements. In Section 6 we consider a “semi-
generic” deformation of the braid arrangement (the Coxeter arrangement of type
An−1) related to the theory of interval orders. In Section 7 we study the hyperplane
arrangements which are related, in a special case, to interval orders (cf. [25]) and
the Catalan numbers. We prove a theorem that establishes a relation between the
numbers of regions of such arrangements. In Section 8 we formulate the main result
on the Linial arrangement. We introduce several combinatorial objects whose num-
bers are equal to the number of regions of the Linial arrangement: alternating trees,
local binary search trees, sleek posets, semiacyclic tournaments. We also prove a
theorem on characterization of sleek posets in terms of forbidden subposets. At last,
in Section 9 we study truncated aﬃne arrangements. We prove a functional equa-
tion for the generating function for the numbers of regions of such arrangements,
deduce a formula for these numbers, and the theorem on the location of zeros of the
characteristic polynomial.

2 Arrangements of Hyperplanes

First, we give several basic notions related to arrangements of hyperplanes. For
more details, see [31, 16, 17].
A hyperplane arrangement is a discrete collection of aﬃne hyperplanes in a vector
space. We will be concerned here only with ﬁnite arrangements. Let A be a ﬁnite

2

hyperplane arrangement in a real ﬁnite-dimensional vector space V . It will be
convenient to assume that the vectors dual to hyperplanes in A span the vector
space V ∗. Denote by r(A) the number of regions of A, which are the connected
components of the space V − ⋃
H∈A H. We will also consider the number b(A) of
(relatively) bounded regions of A.
These numbers have a natural q-analogue. Let AC denote the complexiﬁed ar-
rangement A. In other words, AC is the collection of the hyperplanes H ⊗C, H ∈ A,
in the complex vector space V ⊗C. Let CA be the complement to hyperplanes of AC
in V ⊗ C. Then one can deﬁne the Poincar´e polynomial PoinA(q) of A as

PoinA(q) = ∑

k≥0 dim H
k(CA, C) qk,

the generating function for the Betti numbers of CA.
The following theorem, proved in the paper of Orlik and Solomon [16], shows that
the Poincar´e polynomial generalizes the number of regions r(A) and the number of
bounded regions b(A).

Theorem 2.1 We have r(A) = PoinA(1) and b(A) = PoinA(−1).

Orlik and Solomon gave a combinatorial description of the cohomology ring
H
∗(CA, C) (cf. Section 8.3) in terms of the intersection poset LA of the arrange-
ment A.
The intersection poset is deﬁned as follows: The elements of LA are nonempty
intersections of hyperplanes in A ordered by reverse inclusion. The poset LA has a
unique minimal element ˆ0 = V . This poset is always a meet-semilattice for which
every interval is a geometric lattice. It will be a (geometric) lattice if and only if
LA contains a unique maximal element, i.e., the intersection of all hyperplanes in
A is nonempty. In fact, LA is a geometric semilattice in the sense of Wachs and
Walker [28], and thus for instance is a shellable and hence Cohen-Macaulay poset.
The characteristic polynomial of A is deﬁned by

χA(q) = ∑

z∈LA µ(ˆ0, z) qdim z, (2.1)

where µ denotes the M¨obius function of LA (see [24, Section 3.7]).
Let d be the dimension of the vector space V . Note that it follows from the
properties of geometric lattices [24, Proposition 3.10.1] that the sign of µ(ˆ0, z) is
equal to (−1)d−dim z.
The following simple relation between the (topologically deﬁned) Poincar´e poly-
nomial and the (combinatorially deﬁned) characteristic polynomial was found in [16]:

χA(q) = qdPoinA(−q−1). (2.2)

Sometimes it will be more convenient for us to work with the characteristic polyno-
mial χA(q) rather than the Poincar´e polynomial.

3

✁✁
✁✁
✁✁
✁✁
✁✁

❆
❆
❆
❆
❆
❆
❆
❆
❆
❆
 r

Figure 1: The Coxeter hyperplane arrangement A2.

A combinatorial proof of Theorem 2.1 in terms of the characteristic polynomial
was earlier given by T. Zaslavsky in [31].
The number of regions, the number of (relatively) bounded regions, and, more
generally, the Poincar´e (or characteristic) polynomial are the most simple numer-
ical invariants of a hyperplane arrangement. In this paper we will calculate these
invariants for several hyperplane arrangements related to Coxeter arrangements.

3 Coxeter Arrangements and their Deformations

Let Vn−1 denote the subspace (hyperplane) in Rn of all vectors (x1, . . . , xn) such
that x1 + · · · + xn = 0. All hyperplane arrangements that we consider below lie in
Vn−1. The lower index n − 1 will always denote dimension of an arrangement.
The braid arrangement or Coxeter arrangement (of type An−1) is the arrangement
An−1 of hyperplanes in Vn−1 ⊂ Rn given by

xi − xj = 0, 1 ≤ i < j ≤ n. (3.1)

It is clear that A has r(An−1) = n! regions (called Weyl chambers) and b(An−1) =
0 bounded regions. Arnold [1] calculated the cohomology ring H ∗(CAn, C). In
particular, he proved that

PoinAn−1(q) = (1 + q)(1 + 2q) · · · (1 + (n − 1)q). (3.2)

In this paper we will study deformations of the arrangement (3.1), which are
hyperplane arrangements in Vn−1 ⊂ Rn of the following type:

xi − xj = a
(1)
ij , . . . , a
(mij )
ij , 1 ≤ i < j ≤ n. (3.3)

where mij are nonnegative integers and a
(k)
ij ∈ R.
One special case is the arrangement given by

xi − xj = aij, 1 ≤ i < j ≤ n. (3.4)

The following hyperplane arrangements of type (3.3) worth mentioning:

4

• The generic arrangement (see the end of Section 5) given by

xi − xj = aij, 1 ≤ i < j ≤ n,

where the aij’s are generic real numbers.

• The semigeneric arrangement Gn (see Section 6) given by

xi − xj = ai, 1 ≤ i ≤ n, 1 ≤ j ≤ n, i ̸= j,

where the ai’s are generic real numbers.

• The Linial arrangement Ln−1 (see [25] and Section 8) given by

xi − xj = 1, 1 ≤ i < j ≤ n. (3.5)

• The Shi arrangement Sn−1 (see [22, 23, 25] and Section 9.2) given by

xi − xj = 0, 1, 1 ≤ i < j ≤ n. (3.6)

• The extended Shi arrangement Sn−1, k (see Section 9.2) given by

xi − xj = −k, −k + 1, . . . , k + 1, 1 ≤ i < j ≤ n, (3.7)

where k ≥ 0 is ﬁxed.

• The Catalan arrangements (see Section 7) Cn−1(1) given by

xi − xj = −1, 1, 1 ≤ i < j ≤ n, (3.8)

and C0
n−1(1) given by

xi − xj = −1, 0, 1, 1 ≤ i < j ≤ n. (3.9)

• The truncated aﬃne arrangement Aab
n−1 (see Section 9) given by

xi − xj = −a + 1, −a + 2, . . . , b − 1, 1 ≤ i < j ≤ n, (3.10)

where a and b are ﬁxed integers such that a + b ≥ 2.

One can deﬁne analogous arrangements for any root system. Let V be a real
d-dimensional vector space, and let R be a root system in V ∗ with a chosen set of
positive roots R+ = {β1, β2, . . . , βN } (see, e.g., [7, Ch. VI]). The Coxeter arrange-
ment R of type R is the arrangement of hyperplanes in V given by

βi(x) = 0, 1 ≤ i ≤ N. (3.11)

Brieskorn [6] generalized Arnold’s formula (3.2). His formula for the Poincar´e
polynomial of (3.11) involves the exponents e1, . . . , ed of the corresponding Weyl
group W : PoinR(q) = (1 + e1q)(1 + e2q) · · · (1 + edq).
Consider the hyperplane arrangement given by

βi(x) = a
(1)
i , . . . , a
(mi)
i 1 ≤ i ≤ N, (3.12)

where x ∈ V , mi are some nonnegative integers, and a
(k)
i ∈ R. Many of the results
of this paper have a natural counterpart in the case of an arbitrary root system. We
will brieﬂy outline several related results and conjectures. In more detail they will
appear elsewhere.
 5

✁
✁✁
✁✁
✁✁
✁✁
✁
 ❆
❆
❆
❆
❆
❆
❆
❆
❆
❆

Figure 2: Seven regions of the Linial arrangement L2.

4 Whitney’s formula and the NBC theorem

In this section we review several essentially well-known results on hyperplane ar-
rangements that will be useful in the what follows.
Consider the arrangement A of hyperplanes in V ∼= Rd given by equations

hi(x) = ai, 1 ≤ i ≤ N, (4.1)

where x ∈ V , the hi ∈ V ∗ are linear functionals on V , and the ai are real numbers.
We call a subset I in {1, 2, . . . , N} central if the intersection of the hyperplanes
hi(x) = ai, i ∈ I, is nonempty. For a subset I = {i1, i2, . . . , il}, denote by rk(I) the
dimension (rank) of the linear span of the vectors hi1, . . . , hil.
The following statement is a generalization of a classical formula of Whitney [29].

Theorem 4.1 The Poincar´e and characteristic polynomials of the arrangement A
are equal to
 PoinA(q) = ∑

I (−1)|I|−rk(I) qrk(I), (4.2)

χA(q) = ∑

I (−1)|I| qd−rk(I), (4.3)

where I ranges over all central subsets in {1, 2, . . . , N}. In particular,

r(A) = ∑

I (−1)|I|−rk(I) (4.4)

b(A) = ∑

I (−1)|I|.

We also need the well-known cross-cut theorem (see, [24, Corollary 3.9.4]).

Theorem 4.2 Let L be a ﬁnite lattice with minimal element ˆ0 and maximal ele-
ment ˆ1, and let X be a subset of vertices in L such that (a) ˆ0 ̸∈ X, and (b) if y ∈ L
and y ̸= ˆ0, then x ≤ y for some x ∈ X (such elements are called atoms). Then

µL(ˆ0, ˆ1) = ∑

k (−1)k nk, (4.5)

6

where nk is the number of k-element subsets in X with join equal to ˆ1.

Now we can easily deduce Theorem 4.1.
Proof. Let z be any element in the intersection poset LA, and let L(z) be the
subposet of all elements x ∈ LA such that x ≤ z, i.e., the subspace x contains z. In
fact, L(z) is a geometric lattice. Let X be the set of all hyperplanes from A which
contain z. If we apply Theorem 4.2 to L = L(z) and sum (4.5) over all z ∈ LA, we
get the formula (4.3). Then, by (2.2), we get (4.2). □

A cycle is a minimal subset I such that rk(I) = |I| − 1. In other words, a subset
I = {i1, i2, . . . , il} is a cycle if there exists a nonzero vector (λ1, λ2, . . . , λl), unique
up to a nonzero factor, such that λ1hi1 + λ2hi2 + · · · + λlhil = 0. It is not diﬃcult to
see that a cycle I is central if, in addition, we have λ1ai1 + λ2ai2 + · · · + λlail = 0.
Thus, if a1 = · · · = aN = 0 then all cycles are central, and if the ai are generic then
there are no central cycles.
A subset I is called acyclic if |I| = rk(I), i.e., I contains no cycles. It is clear
that any acyclic subset is central.

Corollary 4.3 In the case when the ai are generic, the Poincar´e polynomial is given
by PoinA(q) = ∑

I qrk(I),

where the sum is over all acyclic subsets I of {1, 2, . . . , N}. In particular, the number
of regions r(A) is equal to the number of acyclic subsets.

Indeed, in this case a subset I is acyclic if and only if it is central.

Remark 4.4 The word “generic” in the corollary means that no k distinct hy-
perplanes in (4.1) intersect in an aﬃne subspace of codimension less than k. For
example, if A is deﬁned over Q then it is suﬃcient to require that the ai be linearly
independent over Q.

Let us ﬁx a linear order ρ on the set {1, 2, . . . , N}. We say that a subset I in
{1, 2, . . . , N} is a broken central circuit if there exists i ̸∈ I such that I ∪ {i} is a
central cycle and i is the minimal element of I ∪ {i} with respect to the order ρ.
The following, essentially well-known, theorem gives us the main tool for the
calculation of Poincar´e (or characteristic) polynomials. We will refer to it as the No
Broken Circuit (NBC) Theorem.

Theorem 4.5 We have PoinA(q) = ∑

I q|I|,

where the sum is over all acyclic subsets I of {1, 2, . . . , N} without broken central
circuits.
 7

Proof. We will deduce this theorem from Theorem 4.1 using the involution principle.
In order to do this we construct an involution ι : I → ι(I) on the set of all central
subsets I with a broken central circuit such that for any I we have rk(ι(I)) = rk(I)
and |ι · I| = |I| ± 1.
This involution is deﬁned as follows: Let I be a central subset with a broken
central circuit, and let s(I) be the set of all i ∈ 1, . . . , N such that i is the minimal
element of a broken central circuit J ⊂ I. Note that s(I) is nonempty. If the
minimal element s∗ of s(I) lies in I, then we deﬁne ι(I) = I \ {s∗}. Otherwise, we
deﬁne ι(I) = I ∪ {s∗}.
Note that s(I) = s(ι(I)), thus ι is indeed an involution. It is clear now that all
terms in (4.2) for I with a broken central circuit cancel each other and the remaining
terms yield the formula in Theorem 4.5. □

Remark 4.6 Note that by Theorem 4.5 the number of subsets I without broken
central circuits does not depend on the choice of the linear order ρ.

5 Deformations of Graphic Arrangements

In this section we show how to apply the results of the previous section to arrange-
ments of type (3.3) and to give an interpretation of these results in terms of (colored)
graphs.
With the hyperplane xi − xj = a
(k)
ij in (3.3) one can associate the edge (i, j)
that has the color k. We will denote this edge by (i, j)(k). Then a subset I of
hyperplanes corresponds to a colored graph G on the set of vertices {1, 2, . . . , n}.
According to the deﬁnitions in Section 4, a circuit (i1, i2)(k1), (i2, i3)(k2), . . . , (il, i1)(kl)

in G is central if a
(k1)
i1,i2 + a
(k2)
i2,i3 + · · · + a
(kl)
il,i1 = 0. Clearly, a graph G is acyclic if and
only if G is a forest.
Fix a linear order on the edges (i, j)(k), 1 ≤ i < j ≤ n, 1 ≤ k ≤ mij. We will
call a subset of edges C a broken A-circuit if C is obtained from a central circuit by
deleting the minimal element (here A stands for the collection {a
(k)
ij }). Note that
it should not be confused with the classical notion of a broken circuit of a graph,
which corresponds to the case when all a
(k)
ij are zero.
We summarize below several special cases of the NBC Theorem (Theorem 4.5).
Here |F | denotes the number of edges in a forest F .

Corollary 5.1 The Poincar´e polynomial of the arrangement (3.3) is equal to

PoinA(q) = ∑

F q|F |,

where the sum is over all colored forests F on the vertices 1, 2, . . . , n (an edge (i, j)
can have a color k, where1 ≤ k ≤ mij) without broken A-circuits. The number of
regions of arrangement (3.3) is equal to the number of such forests.

In the case of the arrangement (3.4) we have:

8

Corollary 5.2 The Poincar´e polynomial of the arrangement (3.4) is equal to

PoinA(q) = ∑

F q|F |,

where the sum is over all forests on the set of vertices {1, 2, . . . , n} without broken
A-circuits. The number of regions of the arrangement (3.4) is equal to the number
of such forests.

In the case when the a
(k)
ij are generic these results become especially simple.
For a forest F on vertices 1, 2, . . . , n we will write m
F := ∏
(i,j)∈F mij, where the
product is over all edges (i, j), i < j, in F . Let c(F ) denote the number of connected
components in F .

Corollary 5.3 Fix nonnegative integers mij, 1 ≤ i < j ≤ n. Let A be an arrange-
ment of type (3.3) where the a
(k)
ij are generic. Then

1. PoinA(q) = ∑

F m
F q|F |,

2. r(A) = ∑

F m
F ,

where the sums are over all forests F on the vertices 1, 2, . . . , n.

Corollary 5.4 The number of regions of the arrangement (3.4) with generic aij is
equal to the number of forests on n labelled vertices.

This corollary is “dual” to the following known result (see, e.g., [24, Exer-
cise 4.32(a)]).

Proposition 5.5 Let Pn be the permutohedron, i.e., the polyhedron with vertices
(σ1, . . . , σn) ∈ Rn, where σ1, . . . , σn ranges over all permutations of 1, . . . , n. Then
the number of integer points in Pn is equal to the number of forests on n vertices.

The connected components of the (n
2)
-dimensional space of all arrangements (3.4)
correspond to (coherent) zonotopal tilings of the permutohedron Pn, i.e., certain
subdivisions of Pn into parallelopipeds. The regions of a generic arrangement (3.4)
correspond to the vertices of the corresponding tiling, which are all integer points
in Pn.

6 A semigeneric deformation of the braid arrange-
ment.

Deﬁne the “semigeneric” deformation Gn of the braid arrangement (3.1) to be the
arrangement xi − xj = ai, 1 ≤ i ≤ n, 1 ≤ j ≤ n, i ̸= j,

9

where the ai’s are generic real numbers (e.g., linearly independent over Q). The
signiﬁcance of this arrangement to the theory of interval orders is discussed in [25,
§3]. In [25, Thm. 3.1 and Cor. 3.3] a generating function for the number r(Gn) of
regions and for the characteristic polynomial χGn(q) of Gn is stated without proof.
In this section we provide the proofs.

Theorem 6.1 Let

z = ∑

n≥0 r(Gn) x
n

n!

= 1 + x + 3 x
2

2! + 19 x
3

3! + 195 x
4

4! + 2831 x
5

5! + 53703 x
6

6! + · · · .

Deﬁne a power series

y = 1 + x + 5 x
2

2! + 46 x
3

3! + 631 x
4

4! + 11586 x
5

5! + · · ·

by the equation 1 = y(2 − e
xy).

Then z is the unique power series satisfying

z′

z = y2, z(0) = 1.

Proof. We use the formula (4.4) to compute R(Gn). Given a central set I
of hyperplanes xi − xj = ai in Gn, deﬁne a directed graph GI on the vertex set
1, 2, . . . , n as follows: let i → j be a directed edge of GI if and only if the hyperplane
xi − xj = ai belongs to I. (By slight abuse of notation, we are using I to denote
a set of hyperplanes, rather than the set of their indices.) Note that GI cannot
contain both the edges i → j and j → i, since the intersection of the corresponding
hyperplanes is empty. If k1, k2, . . . , kr are distinct elements of {1, 2, . . . , n}, then it
is easy to see that if r is even then there are exactly two ways to direct the edges
k1k2, k2k3, . . . , kr−1kr, krk1 so that the hyperplanes corresponding to these edges have
nonempty intersection, while if r is odd then there are no ways. It follows that
GI, ignoring the direction of edges, is bipartite (i.e., all circuits have even length).
Moreover, given an undirected bipartite graph on the vertices 1, 2, . . . , n with blocks
(maximal connected subgraphs that remain connected when any vertex is removed)
B1, . . . , Bs, there are exactly two ways to direct the edges of each block so that the
resulting directed graph G is the graph GI of a central set I of hyperplanes. In
addition, rk(I) = n − c(G), where c(G) is the number of connected components of
G. Letting e(G) be the number of edges and b(G) the number of blocks of G, it
follows from equation (4.3) that

χGn(q) = ∑

G (−1)e(G)2b(G)qc(G),

10

where G ranges over all bipartite graphs on the vertex set 1, 2, . . . , n. This formula
appears without proof in [25, Thm. 3.2]. In particular, putting q = −1 gives

r(Gn) = (−1)n ∑

G (−1)e(G)+c(G)2b(G). (6.1)

To evaluate the generating function z = ∑ r(Gn) xn
n! , we use the following strategy.

(a) Compute An := ∑

G(−1)e(G), where G ranges over all (undirected) bipartite
graphs on 1, 2, . . . , n.

(b) Use (a) and the exponential formula to compute Bn := ∑

G(−1)e(G), where
now G ranges over all connected bipartite graphs on 1, 2, . . . , n.

(c) Use (b) and the block-tree theorem to compute the sum Cn := ∑

G(−1)e(G),
where G ranges over all bipartite blocks on 1, 2, . . . , n.

(d) Use (c) and the block-tree theorem to compute the sum Dn := ∑

G(−1)e(G)2b(G),
where G ranges over all connected bipartite graphs on 1, 2, . . . , n.

(e) Use (d) and the exponential formula to compute the desired sum (6.1).

We now proceed to steps (a)–(e).

(a) Let bk(n) be the number of k-edge bipartite graphs on the vertex set 1, 2, . . . , n.
It is known (e.g., [26, Exercise 5.5]) that

∑

n≥0
 ∑

k≥0 bk(n)qk x
n

n! =
 [
∑

n≥0
 ( n∑

i=0 (1 + q)i(n−i)(n
i
 )) x
n

n!
 ]1/2 .

Put q = −1 to get
∑

n≥0 An x
n

n! =
 (
1 + ∑

n≥1 2 x
n

n!
 )1/2 = (2e
x − 1)1/2 .

(b) According to the exponential formula [12, p. 166], we have

∑

n≥1 Bn x
n

n! = log ∑

n≥0 An x
n

n!

= 1
2 log(2e
x − 1).

(c) Let B′
n denote the number of rooted connected bipartite graphs on 1, 2, . . . , n.
Since B′
n = nBn, we get
 ∑

n≥1 B′
n x
n

n! = x d
dx
 ∑

n≥1 Bn x
n

n!

= x
2 − e−x . (6.2)

11

Suppose now that B is a set of nonisomorphic blocks B and w is a weight function
on B, so w(B) denotes the weight of the block B. Let

T (x) = ∑

B∈B w(B) x
p(B)

p(B)!,

where p(B) denotes the number of vertices of B. Let

u(x) = ∑

G
 (∏

B w(B)
) x
p(G)

p(G)! ,

where G ranges over all connected graphs whose blocks are rooted and are isomorphic
(as unrooted graphs) to elements of B, and where B ranges over all blocks of G.
The block-tree theorem [13, (1.3.3)][26, Ch. 5 Exercises] asserts that

u = xe
T ′(u). (6.3)

If we take B to be the set of all nonisomorphic bipartite blocks, w(B) = (−1)e(B),
and u = x/(2 − e
−x), then it follows from (6.2) that

T (x) = ∑

n≥1 Cn x
n

n! . (6.4)

(d) Let D′
n be deﬁned like Dn, except that G ranges over all rooted connected
bipartite graphs on 1, 2, . . . , n, so D′
n = nDn. Let v(x) = ∑

n≥1 D′
n xn
n! . By the
block-tree theorem we have v = xe
2T ′(v),

where T (x) is given by (6.4). Substitute v⟨−1⟩ for x and use (6.3) to get

x = v⟨−1⟩(x)e
2T ′(x)

= v⟨−1⟩(x) ( x
u⟨−1⟩(x)
 )2 .

Substitute v(x) for x to obtain

x v(x) = u⟨−1⟩(v(x))2.

Take the square root of both sides and compose with u(x) = x/(2 − e
−x) on the left
to get √xv
2 − e−√xv = v. (6.5)

(e) Equation (6.1) and the exponential formula show that

z = exp
 (
− ∑

n≥1(−1)nDn x
n

n!
 )

= exp (− ∫ v(−x)
x
 ) , (6.6)

12

where ∫ denotes the formal integral, i.e., ∫ ∑ an xn
n! = ∑ an xn+1
(n+1)! . (The ﬁrst minus
sign in (6.6) corresponds to the factor (−1)c(G) in (6.1).)
Let v(−x) = −xy2. Equation (6.5) becomes (taking care to choose the right sign
of the square root) 1 = y(2 − e
xy),

while (6.6) shows that z′/z = −v(−x)/x = y2. This completes the proof. ✷
Note. The semigeneric arrangement Gn satisﬁes the hypotheses of [25, Thm.
1.2]. It follows that ∑

n≥0 χGn(q) x
n

n! = z(−x)−q,

as stated in [25, Cor. 3.3]. Here z is as deﬁned in Theorem 6.1.
An arrangement closely related to Gn is given by

G′
n : xi − xj = ai, 1 ≤ i < j ≤ n,

where the ai’s are generic. The analogue of equation (6.1) is

r(G′
n) = (−1)n ∑

G (−1)e(G)+c(G)2b(G),

where now G ranges over all bipartite graphs on the vertex set 1, 2, . . . , n for which
every block is alternating, i.e., every vertex is either less that all its neighbors or
greater than all its neighbors. We don’t see, however, how to use this formula to
obtain a generating function for r(G′
n) analogous to Theorem 6.1.

7 Catalan Arrangements and Semiorders

Let us ﬁx distinct real numbers a1, a2, . . . , am > 0, and let A = (a1, . . . , am). In this
section we consider the arrangement Cn−1 = Cn−1(A) of hyperplanes in the space
Vn−1 = {(x1, . . . , xn) ∈ Rn | x1 + · · · + xn = 0} given by

xi − xj = a1, a2, . . . , am, i ̸= j. (7.1)

We consider also the arrangement C0
n−1 = C0
n−1(A) obtained from Cn−1 by adjoining
the hyperplanes xi = xj, i.e., C0
n is given by

xi − xj = 0, a1, a2, . . . , am, i ̸= j. (7.2)

Let fA(t) = ∑

n≥0 r(Cn−1) t
n

n! ,

gA(t) = ∑

n≥0 r(C0
n−1) t
n

n!

be the exponential generating functions for the numbers of regions of the arrange-
ments Cn−1 and C0
n−1.
The main result of this section is the following:

13

Theorem 7.1 We have fA(t) = gA(1 − e
−t) or, equivalently,

r(C0
n−1) = ∑

k≥0 c(n, k) r(Ck−1),

where c(n, k) is the signless Stirling number of the ﬁrst kind, i.e., the number of
permutations of 1, 2, . . . , n with k cycles.

Let us have a closer look at two special cases of arrangements (7.1) and (7.2).
Consider the arrangement of hyperplanes in Vn−1 ⊂ Rn given by the equations

xi − xj = ±1, 1 ≤ i < j ≤ n. (7.3)

Consider also the arrangement given by

xi − xj = 0, ±1, 1 ≤ i < j ≤ n. (7.4)

It is not diﬃcult to check the following result directly from the deﬁnition.

Proposition 7.2 The number of regions of the arrangement (7.4) is equal to n! Cn,
where Cn is the Catalan number Cn = 1
n+1(
2n
n )
.

Theorem 7.1 then gives a formula for the number of regions of the arrangement (7.3).
Let R be a region of the arrangement (7.3), and let (x1, . . . , xn) ∈ R be any point
in the region R. Consider the poset P on the vertices 1, . . . , n such that i >P j if
and only if xi − xj > 1. Clearly, distinct regions correspond to distinct posets. The
posets that can be obtained in such a way are called semiorders. See [25] for more
results on the relation between hyperplane arrangements and interval orders (which
are a generalization of semiorders).
The symmetric group Sn naturally acts on the space Vn−1 by permuting the
coordinates xi. Thus it also permutes the regions of the arrangement (7.4). The
region x1 < x2 < · · · < xn is called the dominant chamber. Every Sn-orbit consists
of n! regions and has a unique representative in the dominant chamber. It is also
clear that the regions of (7.4) in the dominant chamber correspond to unlabelled
(i.e., nonisomorphic) semiorders on n vertices. Hence, Proposition 7.2 is equivalent
to a well-known result of Wine and Freund [30] that the number of nonisomorphic
semiorders on n vertices is equal to the Catalan number. In the special case of the
arrangements (7.3) and (7.4), i.e., A = (1), Theorem 7.1 gives a formula for the
number of labelled semiorders on n vertices which was ﬁrst proved by Chandon,
Lemaire, and Pouget [8].
The following theorem, due to Scott and Suppes [21], presents a simple charac-
terization of semiorders (cf. Theorem 8.4).

Theorem 7.3 A poset P is a semiorder if and only if it contains no induced sub-
poset of either of the two types shown on Figure 3.

Return now to the general case of the arrangements Cn−1 and C0
n−1 given by (7.1)
and (7.2). The symmetric group Sn acts on the regions of Cn−1 and C0
n−1. Let Rn−1
denotes the set of all regions of Cn−1.
 14

r

r
 r

r
 r

r

r
 r

Figure 3: Forbidden subposets for semiorders.

Lemma 7.4 The number of regions of C0
n−1 is equal to n! times the number of Sn-
orbits in Rn−1.

Indeed, the number of regions of C0
n−1 is n! times the number of those in the dominant
chamber. They, in turn, correspond to Sn-orbits in Rn−1. As was shown in [25], the
regions of Cn−1 can be viewed as (labelled) generalized interval orders. On the other
hand, the regions of C0
n−1 that lie in the dominant chamber correspond to unlabelled
generalized interval orders. The statement now is tautological, that the number of
unlabelled objects is the number of Sn-orbits.
Now we can apply the following well-known lemma of Burnside (actually ﬁrst
proved by Cauchy and Frobenius).

Lemma 7.5 Let G be a ﬁnite group which acts on a ﬁnite set M. Then the number
of G-orbits in M is equal to
 1
|G|
 ∑

g∈G Fix(g, M),

where Fix(g, M) is the number of elements in M ﬁxed by g ∈ G.

By Lemmas 7.4 and 7.5 we have

r(C0
n−1) = ∑

σ∈Sn Fix(σ, Cn−1),

where Fix(σ, Cn−1) is the number of regions of Cn−1 ﬁxed by the permutation σ.
Theorem 7.1 now follows easily from the following lemma.

Lemma 7.6 Let σ ∈ Sn be a permutation with k cycles. Then the number of
regions of Cn−1 ﬁxed by σ is equal to the total number of regions of Ck−1.

Indeed, by Lemma 7.6, we have

r(C0
n−1) = ∑

σ∈Sn Fix(σ, Cn−1) = ∑

k≥0 c(n, k) r(Ck−1),

which is precisely the claim of Theorem 7.1.

Proof of Lemma 7.6 We will construct a bijection between the regions of Cn−1
ﬁxed by σ and the regions of Ck−1.
 15

Let R be any region of Cn−1 ﬁxed by a permutation σ ∈ Sn, and let (x1, . . . , xn)
be any point in R. Then for any i, j ∈ {1, . . . , n} and any s = 1, . . . , m we have
xi − xj > as if and only if xσ(i) − xσ(j) > as.
Let σ = (c11 c12 · · · c1l1) (c21 c22 · · · c2l2) · · · (ck1 ck2 · · · cklk) be the cycle decom-
position of the permutationXi = (xci1, xci2, . . .) for i = 1, . . . , k. We will write
Xi − Xj > a if xi′ − xj′ > a for any xi′ ∈ Xi and xj′ ∈ Xj. The notation Xi − Xj < a
has an analogous meaning. We will show that for any two classes Xi and Xj and
for any s = 1, . . . , m we have either Xi − Xj > as or Xi − Xj < as.
Let xi∗ be the maximal element in Xi and let xj∗ be the maximal element in Xj.
Suppose that xi∗ − xj∗ > as. Since R is σ-invariant, for any integer p we have the
inequality xσp(i∗) − xσp(j∗) > as. Then, since xi∗ is the maximal element of Xi, we
have xi∗ − xσp(j∗) > as. Again, for any integer q, we have xσq(i∗) − xσp+q(j∗) > as,
which implies that Xi − Xj > as.
Analogously, suppose that xi∗ − xj∗ < as. Then for any integer p we have
xσp(i∗) − xσp(j∗) < as. Since xj∗ ≥ xσp(j∗), we have xσp(i∗) − xj∗ < as. Finally, for any
integer q we obtain xσp+q(i∗) − xσq(j∗) < as, which implies that Xi − Xj < as.
If we pick an element xi′ in each class Xi we get a point (x1′, x2′, . . . , xk′) in Rk.
This point lies in some region R′ of Ck−1. The construction above shows that the
region R′ does not depend on the choice of xi′ in Xi.
Thus we get a map φ : R → R′ from the regions of Cn−1 invariant under σ to
the regions of Ck−1. It is clear that φ is injective. To show that φ is surjective, let
(x1′, . . . , xk′) be any point in a region R′ of Ck. Pick the point (x1, x2, . . . , xn) ∈ Rn

such that xc11 = xc12 = · · · = x1′, xc21 = xc22 = · · · = x2′, . . . , xck1 = xck2 = · · · = xk′.
Then (x1, . . . , xn) is in some region R of Cn−1 (here we use the condition a1, . . . , am ̸=
0). According to our construction, we have φ(R) = R′. Thus φ is a bijection.
This completes the proof of Lemma 7.6 and therefore also of Theorem 7.1. □

8 The Linial Arrangement.

As before, Vn−1 = {(x1, . . . , xn) ∈ Rn | x1 + · · · + xn = 0}. Consider the arrange-
ment Ln−1 of hyperplanes in Vn−1 given by the equations

xi − xj = 1, 1 ≤ i < j ≤ n. (8.1)

Recall that r(Ln−1) denotes the number of regions of the arrangement Ln−1. This
arrangement was ﬁrst considered by Nati Linial and Shmulik Ravid. They calculated
the numbers r(Ln−1) and the Poincar´e polynomials PoinLn−1(q) for n ≤ 9.
In this section we give an explicit formula and several diﬀerent combinatorial
interpretations for the numbers r(Ln−1).

8.1 Alternating trees and local binary search trees

We call a tree T on the vertices 0, 1, 2, . . . , n alternating if the vertices in any path
i1, . . . , ik in T alternate, i.e., we have i1 < i2 > i3 < · · · ik or i1 > i2 < i3 > · · · ik.
In other words, there are no i < j < k such that both (i, j) and (j, k) are edges in T .

16

Equivalently, every vertex is either greater than all its neighbors of less than all its
neighbors. Alternating trees ﬁrst appear in [10] and were studied in [20], where they
were called intransitive trees (see also [25]).

r r r r r

r r r r r
 r 
 
 
  
 ❅
❅
❅
❅❅
 ❅
❅
❅
❅❅
  
 
 
  
 ❅
❅
❅
❅❅

01 23

4

5
 67
 8

910
 Figure 4: An alternating tree.

Let fn be the number of alternating trees on the vertices 0, 1, 2, . . . , n, and let

f (x) = ∑

n≥0 fn x
n

n!

be the exponential generating function for the sequence fn.
A plane binary tree B on the vertices 1, 2, . . . , n is called a local binary search
tree if for any vertex i in T the left child of i is less than i and the right child of i
is greater than i. These trees were ﬁrst considered by Ira Gessel [11]. Let gn denote
the number of local binary search trees on the vertices 1, 2, . . . , n. By convention,
g0 = 1.
 r r r r

r r r

r r

r

 
 
  
  
 
  
  
 
  
 ❅
❅
❅❅
 
 
  
 ❅
❅
❅❅
 ❅
❅
❅❅
 
 
  
 ❅
❅
❅❅

12
 3
 4

5
 6
 7

8 9
 10

Figure 5: A local binary search tree.

The following result was proved in [20] (see also [10, 25]).

Theorem 8.1 For n ≥ 1 we have

fn = gn = 2−n n∑

k=0
 (
n
k
)(k + 1)n−1

and f = f (x) satisﬁes the functional equation

f = e
x(1+f )/2.

17

The ﬁrst few numbers fn are given in the table below.

n 0 1 2 3 4 5 6 7 8 9 10

fn 1 1 2 7 36 246 2104 21652 260720 3598120 56010096

The main result on the Linial arrangement is the following:

Theorem 8.2 The number r(Ln−1) of regions of Ln−1 is equal to the number fn
of alternating trees on the vertices 0, 1, 2 . . . , n, and thus to the number gn of local
binary search trees on 1, 2, . . . , n.

This theorem was conjectured by the second author (thanks to the numerical
data provided by Linial and Ravid) and was proved by the ﬁrst author. A diﬀerent
proof was later given by C. Athanasiadis [3].
In Section 9 we will prove a more general result (see Theorems 9.1 and Corol-
lary 9.9).

8.2 Sleek posets and semiacyclic tournaments

Let R be a region of the arrangement Ln−1, and let (x1, . . . , xn) be any point in R.
Deﬁne P = P (R) to be the poset on the vertices 1, 2, . . . , n such that i <P j if and
only if xi − xj > 1 and i < j in the usual order on Z.
We will call a poset P on the vertices 1, 2, . . . , n sleek if P is the intersection of
a semiorder (see Section 7) with the chain 1 < 2 < · · · < n.
The following proposition immediately follows from the deﬁnitions.

Proposition 8.3 The map R ↦→ P (R) is a bijection between regions of Ln−1 and
sleek posets on 1, 2, . . . , n. Hence the number r(Ln−1) is equal to the number of sleek
posets on 1, 2, . . . , n.

There is a simple characterization of sleek posets in terms of forbidden induced
subposets (compare Theorem 7.3).

Theorem 8.4 A poset P on the vertices 1, 2, . . . , n is sleek if and only if it contains
no induced subposet of the four types shown on Figure 6, where a < b < c < d.

In the remaining part of this section we prove Theorem 8.4.
First, we give another description of regions in Ln−1 (or, equivalently, sleek
posets). A tournament on the vertices 1, 2, . . . , n is a directed graph T without
loops such that for every i ̸= j either (i, j) ∈ T or (j, i) ∈ T . For a region R of
Ln−1 construct a tournament T = T (R) on the vertices 1, 2, . . . , n as follows: let
(x1, . . . , xn) ∈ R. If xi − xj > 1 and i < j, then (i, j) ∈ T ; while if xi − xj < 1 and
i < j, then (j, i) ∈ T .
Let C be a directed cycle in the complete graph Kn on the vertices 1, 2, . . . , n.
We will write C = (c1, c2, . . . , cm) if C has the edges (c1, c2), (c2, c3), . . . , (cm, c1). By

18

r

r
 r

r
 r

r
 r

r
 r

r

r
 r
 r

r

r
 r

a

c
 b

d
 a

d
 b

c
 a

b

d
 c
 a

c

d
 b

Figure 6: Obstructions to sleekness.

r
 r

r

C0

a

c

b
 r

r
 r

r

C1

a b

c d
 r

r r

r

C2

a b

cd
 r
 r

r
 r

C3

a

b c

d
 r
 r

r
 r

C4

a

c b

d

❆
❆
❆
✁
✁✁

❆
❆❑

✁
✁✕ ❄ ❏
❏❏
❏
❏

✡
✡
✡
✡
✡
✻

❏
❏❏❏❫ ✻

✡
✡
✡✡✢
 ❏
❏
❏❏
❏

✡
✡
✡
✡
✡
✻

❏
❏
❏❏❫ ✻

✡
✡
✡✡✢ ✁✁
✁❆
❆❆
✁
✁
✁❆
❆
❆
✁
✁✕ ❆❆❯
 ✁✁☛

❆
❆❑
 ✁
✁✁❆❆
❆
✁
✁
✁❆
❆
❆
✁
✁✕ ❆❆❯
 ✁✁☛

❆
❆❑

Figure 7: Ascending cycles.

convention, c0 = cm. An ascent in C is a number 1 ≤ i ≤ m such that ci−1 < ci.
Analogously, a descent in C is a number 1 ≤ i ≤ m such that ci−1 > ci. Let asc(C)
denote the number of ascents and des(C) denote the number of descents in C. We
say that a cycle C is ascending if asc(C) ≥ des(C). For example, the following
cycles are ascending: C0 = (a, b, c), C1 = (a, c, b, d), C2 = (a, d, b, c), C3 = (a, b, d, c),
C4 = (a, c, d, b), where a < b < c < d. These cycles are shown on Figure 7.
We call a tournament T on 1, 2, . . . , n semiacyclic if it contains no ascending
cycles. In other words, T is semiacyclic if for any directed cycle C in T we have
asc(C) < des(C).

Proposition 8.5 A tournament T on 1, 2, . . . , n corresponds to a region R in Ln−1,
i.e., T = T (R), if and only if T is semiacyclic. Hence r(Ln−1) is the number of
semiacyclic tournaments on 1, 2, . . . , n.

This fact was independently found by Shmulik Ravid.
For any tournament T on 1, 2, . . . , n without cycles of type C0 we can construct
a poset P = P (T ) such that i <P j if and only if i < j and (i, j) ∈ T . Now the
four ascending cycles C1, C2, C3, C4 in Figure 7 correspond to the four posets on
Figure 6. Therefore, Theorem 8.4 is equivalent to the following result.

Theorem 8.6 A tournament T on the vertices 1, 2, . . . , n is semiacyclic if and only
if it contains no ascending cycles of the types C0, C1, C2, C3, and C4 shown in
Figure 7, where a < b < c < d.

Remark 8.7 This theorem is an analogue of a well-known fact that a tournament
T is acyclic if and only if it contains no cycles of length 3. For semiacyclicity we
have obstructions of lengths 3 and 4.
 19

Proof. Let T be a tournament on 1, 2, . . . , n. Suppose that T is not semiacyclic.
We will show that T contains a cycle of type C0, C1, C2, C3, or C4. Let C =
(c1, c2, . . . , cm) be an ascending cycle in T of minimal length. If m = 3, or 4 then C
is of type C0, C1, C2, C3, or C4. Suppose that m > 4.

Lemma 8.8 We have asc(C) = des(C).

Proof. Since C is ascending, we have asc(C) ≥ des(C). Suppose asc(C) > des(c). If
C has two adjacent ascents i and i+1 then (ci−1, ci+1) ∈ T (otherwise we have an as-
cending cycle (ci−1, ci, ci+1) of type C0 in T ). Then C ′ = (c1, c2, . . . , ci−1, ci+1, . . . , cm)
is an ascending cycle in T of length m − 1, which contradicts the fact that we chose
C to be minimal. So for every ascent i in C the index i + 1 is a descent. Hence
asc(C) ≤ des(C), and we get a contradiction. □

We say that ci and cj are on the same level in C if the number of ascents between
ci and cj is equal to the number of descents between ci and cj.

Lemma 8.9 We can ﬁnd i, j ∈ {1, 2, . . . , m} such that (a) i is an ascent and j is
a descent in C, (b) i ̸≡ j ± 1 (mod m), and (c) ci and cj−1 are on the same level
(see Figure 8).

Proof. We may assume that for any 1 ≤ s ≤ m the number of ascents in {1, 2, . . . , s}
is greater than or equal to the number of descents in {1, 2, . . . , s} (otherwise take
some cyclic permutation of (c1, c2, . . . , cm)). Consider two cases.
1. There exists 1 ≤ t ≤ m − 1 such that ct and cm are on the same level. In this
case, if the pair (i, j) = (1, t) does not satisfy conditions (a)–(c) then t = 2. On the
other hand, if the pair (i, j) = (t + 1, m) does not satisfy (a)–(c) then t = m − 2.
Hence, m = 4 and C is of type C1 or C2 shown in Figure 7.
2. There is no 1 ≤ t ≤ m − 1 such that ct and cm are on the same level. Then 2
is an ascent and m − 1 is a descent. If the pair (i, j) = (2, m − 2) does not satisfy
(a)–(c) then m = 4 and C is of type C3 or C4 shown on Figure 7. □

Now we can complete the proof of Theorem 8.6. Let i, j be two numbers satisfying
the conditions of Lemma 8.9. Then ci−1, ci, cj−1, cj are four distinct vertices such
that (a) ci−1 < ci, (b) cj−1 > cj, (c) ci and cj−1 are on the same level, and (d) ci−1
and cj are on the same level (see Figure 8). We may assume that i < j.
If (cj−1, ci−1) ∈ T then (ci−1, ci, . . . , cj−1) is an ascending cycle in T of length
less than m, which contradicts the requirement that C is an ascending cycle on T of
minimal length. So (ci−1, cj−1) ∈ T . If ci−1 < cj−1 then (cj−1, cj, . . . , cm, c1, . . . , ci−1)
is an ascending cycle in T of length less than m. Hence, ci−1 > cj−1.
Analogously, if (ci, cj) ∈ T then (cj, cj+1, . . . , cp, c1, . . . , ci) is an ascending cycle
in T of length less than m. So (cj, ci) ∈ T . If ci > cj then (ci, ci+1, . . . , cj) is an
ascending cycle in T of length less than m. So ci < cj.
Now we have ci−1 > cj−1 > cj > ci > ci−1, and we get an obvious contradiction.
We have shown that every minimal ascending cycle in T is of length 3 or 4 and
thus have proved Theorem 8.6. □

20

r

r
 r

r

✻ ❄
cj

cj−1

ci−1

ci
 Figure 8:

8.3 The Orlik-Solomon algebra

In [16] Orlik and Solomon gave the following combinatorial description of the coho-
mology ring of an arbitrary hyperplane arrangement. Consider a complex arrange-
ment A of aﬃne hyperplanes H1, H2, . . . , HN in the complex space V ∼= Cn given
by Hi : fi(x) = 0, i = 1, . . . , N,

where fi(x) are linear forms on V (with a constant term).
We say that hyperplanes Hi1, . . . , Hip are independent if the codimension of the
intersection Hi1 ∩ · · · ∩ Hip is equal to p. Otherwise, the hyperplanes are dependent.
Let e1, . . . , eN be formal variables associated with the hyperplanes H1, . . . , HN .
The Orlik-Solomon algebra OS(A) of the arrangement A is generated over the com-
plex numbers by e1, . . . , eN subject to the relations:

eiej = −ejei, 1 ≤ i < j ≤ N, (8.2)

ei1 · · · eip = 0, if Hi1 ∩ · · · ∩ Hip = ∅, (8.3)

p+1∑

j=1(−1)j ei1 · · · ̂eij · · · eip+1 = 0, (8.4)

whenever Hi1, . . . , Hip+1 are dependent. (Here ̂eij denotes that eij is missing.)
Let CA = V − ⋃
i Hi be the complement to the hyperplanes Hi of A, and let
H
∗
DR(CA, C) denote de Rham cohomology of CA.

Theorem 8.10 (Orlik, Solomon [16]) The map φ : OS(A) → H
∗
DR(CA, C) deﬁned
by φ : ei ↦→ [dfi/fi]

is an isomorphism.

Here [dfi/fi] is the cohomology class in H
∗
DR(CA, C) of the diﬀerential form dfi/fi.
We will apply Theorem 8.10 to the Linial arrangement. In this case hyperplanes
xi − xj = 1, i < j, correspond to edges (i, j) of the complete graph Kn.

21

Proposition 8.11 The Orlik-Solomon algebra OS(Ln−1) of the Linial arrangement
is generated by evw = e(v,w), 1 ≤ v < w ≤ n subject to relations (8.2), (8.3), and
also to the following relations:

eabebceac − eabebcecd + eabeacecd − ebceacecd = 0,

eacebcebd − eacebcead + eacebdead − ebcebdead = 0. (8.5)

where 1 ≤ a < b < c < d ≤ n (cf. Figure 7).

Proof. Let C = (c1, c2, . . . , cp) be a cycle in Kn. We say that C is balanced if
asc(C) = des(C). We may assume that in equation (8.4) i1, i2, . . . , ip are edges of
a balanced cycle C. We will prove (8.4) by induction on p. If p = 4 then C is of
type C1, C2, C3, or C4 (see Figure 7). Thus C produces one of the relations (8.5).
If p > 4, then we can ﬁnd r ̸= s such that both C ′ = (cr, cr+1, . . . , cs) and C ′′ =
(cs, cs+1, . . . , cr) are balanced. Equation (8.4) for C is the sum of the equations for
C ′ and C ′′. Thus the statement follows by induction. □

Remark 8.12 This proposition is an analogue to the well-known description of the
cohomology ring of the Coxeter arrangement (3.1), due to Arnold [1]. This cohomol-
ogy ring is generated by evw = e(v,w), 1 ≤ v < w ≤ n, subject to relations (8.2), (8.3)
and also the following “triangle” equation:

eabebc − eabeac + ebceac = 0,

where 1 ≤ a < b < c ≤ n.

9 Truncated aﬃne arrangements

In this section we study a general class of hyperplane arrangements which contains,
in particular, the Linial and Shi arrangements.
Let a and b be two integers such that a + b ≥ 2. Consider the hyperplane
arrangement Aab
n−1 in Vn−1 = {(x1, . . . , xn) ∈ Rn | x1 + · · · + xn = 0} given by

xi − xj = −a + 1, −a + 2, . . . , b − 1, 1 ≤ i < j ≤ n. (9.1)

We call Aab
n−1 truncated aﬃne arrangement because it is a ﬁnite subarrangement
of the aﬃne arrangement of type ̃An−1 given by xi − xj = k, k ∈ Z.
As we will see the arrangement Aab
n−1 has diﬀerent behavior in the balanced case
(a = b) and the unbalanced case (a ̸= b).

9.1 Functional equations

Let fn = f ab
n be the number of regions of the arrangement Aab
n−1, and let

f (x) = ∑

n≥0 fn x
n

n! (9.2)

be the exponential generating function for fn.

22

Theorem 9.1 Suppose a, b ≥ 0.

1. The generating function f = f (x) satisﬁes the following functional equation:

f b−a = e
x · f a−f b

1−f . (9.3)

2. If a = b ≥ 1, then f = f (x) satisﬁes the equation:

f = 1 + x f a, (9.4)

Note that the equation (9.4) can be formally obtained from (9.3) by l’Hˆopital’s
rule in the limit a → b.
In the case a = b the functional equation (9.4) allows us to calculate the num-
bers f aa
n explicitly. The following statement was proved by P. Headley [14].

Corollary 9.2 The number f aa
n is equal to an(an − 1) · · · (an − n + 2).

The functional equation (9.3) is especially simple in the case a = b − 1. We call
the arrangement Aa,a+1
n−1 the extended Shi arrangement. In this case we get:

Corollary 9.3 Let a ≥ 1. The number fn of regions of the hyperplane arrangement
in Rn given by xi − xj = −a + 1, −a + 2, . . . , a, i < j,

is equal to fn = (a n+1)n−1, and the exponential generating function f = ∑

n≥0 fn xn
n!
satisﬁes the functional equation f = e
x·f a.

In order to prove Theorem 9.1 we need several new deﬁnitions. A graded graph
is a graph G on a set V of vertices labelled by natural numbers together with a
function h : V → {0, 1, 2, . . .}, which is called a grading. For r ≥ 0 the vertices v
in G such that h(v) = r form the rth level of G. Let e = (u, v) be an edge in G,
u < v. We say that the type of the edge e is the integer t = h(v) − h(u) and that
a graded graph G is of type (a, b) if the types of all edges in G are in the interval
[−a + 1, b − 1] = {−a + 1, −a + 2, . . . , b − 1}.
Choose a linear order on the set of all triples (u, t, v), u, v ∈ V , t ∈ [−a + 1, b − 1].
Let C be a graded cycle of type (a, b). Every edge (u, v) in C corresponds to a triple
(u, t, v), where t is the type of the edge (u, v). Choose the edge e in C with the
minimal triple (u, t, v). We say that C \ {e} is a broken circuit of type (a, b).
Let (F, h) be a graded forest. We say that (F, h) is grounded or that h is a
grounded grading on the forest F if each connected component in F contains a
vertex on the 0th level.

Proposition 9.4 The number fn of regions of the arrangement (9.1) is equal to the
number of grounded graded forests of type (a, b) on the vertices 1, 2, . . . , n without
broken circuits of type (a, b).
 23

Proof. By Corollary 5.1, the number fn is equal to the number of colored forests
F on the vertices 1, 2, . . . , n without broken A-circuits. Every edge (u, v), u < v,
in F has a color which is an integer from the interval [−a + 1, b − 1]. Consider the
grounded grading h on F such that for every edge (u, v), u < v, in F of color t we
have that t = h(v) − h(u) is the type of (u, v). It is clear that such a grading is
uniquely deﬁned. Then (F, h) is a grounded graded forest of type (a, b). Clearly, this
gives a correspondence between colored and graded forests. Then broken A-circuits
correspond to broken graded circuits. The proposition easily follows. □

From now on we ﬁx the lexicographic order on triples (u, t, v), i.e., (u, t, v) <
(u′, t
′, v′) if and only if u < u′, or (u = u′ and t < t
′), or (u = u′ and t = t
′ and
v < v′). Note the order of u, t, and v. We will call a graded tree T solid if T is of
type (a, b) and T contains no broken circuits of type (a, b).
Let T be a solid tree on 1, 2, . . . , n such that vertex 1 is on the rth level. If we
delete the minimal vertex 1, then the tree T decomposes into connected components
T1, T2, . . . , Tm. Suppose that each component Ti is connected with 1 by an edge (1, vi)
where vi is on the ri-th level.

Lemma 9.5 Let T, T1, . . . , Tm, v1, . . . , vm, and r1, . . . , rm be as above. The tree T is
solid if and only if (a) all T1, T2, . . . , Tm are solid, (b) for all i the ri-th level is the
minimal nonempty level in Ti such that −a + 1 ≤ ri − r ≥ b − 1, and (c) the vertex
vi is the minimal vertex on its level in Ti.

Proof. First, we prove that if T is solid then the conditions (a)–(c) hold. Condi-
tion (a) is trivial, because if some Ti contains a broken circuit of type (a, b) then T
also contains this broken circuit. Assume that for some i there is a vertex v′
i on the
r′
i-th level in Ti such that r′
i < ri and r′
i − r ≥ −a + 1. Then the minimal chain
in T that connects vertex 1 with vertex v′
i is a broken circuit of type (a, b). Thus
condition (b) holds. Now suppose that for some i vertex vi is not the minimal vertex
v′′
i on its level. Then the minimal chain in T that connects vertex 1 with v′′
i is a
broken circuit of type (a, b). Therefore, condition (c) holds too.
Now assume that conditions (a)–(c) are true. We prove that T is solid. For
suppse not. Then T contains a broken circuit B = C \ {e} of type (a, b), where C
is a graded circuit and e is its minimal edge. If B does not pass through vertex 1
then B lies in Ti for some i, which contradicts condition (a). We can assume that
B passes through vertex 1. Since e is the minimal edge in C, e = (1, v) for some
vertex v′ on level r′ in T . Suppose v ∈ Ti. If v′ and vi are on diﬀerent levels in Ti
then, by (b), ri < r. Thus the minimal edge in C is (1, vi) and not (1, v′). If v′ and
vi are on the same level in Ti, then by (c) we have vi < v′. Again, the minimal edge
in C is (1, vi) and not (1, v′). Therefore, the tree T contains no broken circuit of
type (a, b), i.e., T is solid. □

Let si be the minimal nonempty level in Ti, and let li be the maximal nonempty
level in Ti. By Lemma 9.5, the vertex 1 can be on the rth level, r ∈ {si − b + 1, si −
b + 1, . . . , li + a − 1}, and for each such r there is exactly one way to connect 1 with
Ti.
 24

Let pnkr denote the number of solid trees (not necessarily grounded) on the
vertices 1, 2, . . . , n which are located on levels 0, 1, . . . , k such that vertex 1 is on the
rth level, 0 ≤ r ≤ k.
Let
 pkr(x) = ∑

n≥1 pnkr x
n

n! , pk(x) =
 k∑

r=0 pkr(x).

By the exponential formula (see [12, p. 166]) and Lemma 9.5, we have

p′
kr(x) = exp(bkr(x)), (9.5)

where bkr(x) = ∑

n≥1 bnkr xn
n! and bnkr is the number of solid trees T on n vertices
located on the levels 0, 1, . . . , k such that at least one of the levels r − a + 1, r −
a + 2, . . . , r + b − 1 is nonempty, 0 ≤ r ≤ k. The polynomial bkr(x) enumerates the
solid trees on levels 1, 2, . . . , k minus trees on levels 1, . . . , r − a and trees on levels
r + b, . . . , k. Thus we obtain

bkr(x) = pk(x) − pr−a(x) − pk−r−b(x).

By (9.5), we get
 p′
kr(x) = exp(pk(x) − pr−a(x) − pk−r−b(x)),

where p−1(x) = p−2(x) = · · · = 0, p0(x) = x, pk(0) = 0 for k ∈ Z. Hence

p′
k(x) =
 k∑

r=0 exp(pk(x) − pr−a(x) − pk−r−b(x)).

Equivalently,
p′
k(x) exp(−pk(x)) =
 k∑

r=0 exp(−pr−a(x)) exp(−pk−r−b(x)).

Let qk(x) = exp(−pk(x)). We have

q′
k(x) = −
 k∑

r=0 qr−a(x) qk−r−b(x), (9.6)

q−1 = q−2 = · · · = 1, q0 = e
−x, qk(0) = 1 for k ∈ Z.
The following lemma describes the relation between the polynomials qk(x) and
the number of regions of the arrangement Aab
n−1.

Lemma 9.6 The quotient qk−1(x)/qk(x) tends to ∑

n≥0 fn xn
n! as k → ∞.

Proof. Clearly, pk(x) − pk−1(x) is the exponential generating function for the num-
bers of grounded solid trees of height less than or equal to k. By the exponential
formula (see [12, p. 166]) qk−1(x)/qk(x) = exp (pk(x) − pk−1(x)) is the exponential

25

generating function for the numbers of grounded solid forests of height less than or
equal to k. The lemma obviously follows from Proposition 9.4. □

All previous formulae and constructions are valid for arbitrary a and b. Now we
will take advantage of the condition a, b ≥ 0. Let

q(x, y) = ∑

k≥0 qk(x)yk.

By (9.6), we obtain the following diﬀerential equation for q(x, y):

∂
∂x q(x, y) = − (ay + yaq(x, y)) · (by + ybq(x, y)) ,

q(0, y) = (1 − y)−1,

where ay := (1 − ya)/(1 − y).
This diﬀerential equation has the following solution:

q(x, y) = by exp(−x · by) − ay exp(−x · ay)
ya exp(−x · ay) − yb exp(−x · by) . (9.7)

Let us ﬁx some small x. Since Q(y) := q(x, y) is an analytic function of y,
then γ = γ(x) = limk→∞ qk−1/qk is the pole of Q(y) closest to 0 (γ is the radius of
convergence of Q(y) if x is a small positive number). By (9.7), γa exp(−x · aγ) −
γb exp(−x · bγ) = 0. Thus, by Lemma 9.6, f (x) = ∑

n≥0 fn xn
n! = γ(x) is the solution
of the functional equation
 f a e
−x · 1−f a

1−f = f b e
−x · 1−f b

1−f ,

which is equivalent to (9.3).
This completes the proof of Theorem 9.1. □

9.2 Formulae for the characteristic polynomial

Let A = Aab
n−1 be the truncated aﬃne arrangement given by (9.1). Consider the
characteristic polynomial χ
ab
n (q) of the arrangement Aab
n−1. Recall that χ
ab
n (q) =
qn−1PoinAab
n−1(−q−1).
Let χ
ab(x, q) be the exponential generating function

χ
ab(x, q) = 1 + ∑

n>0 χ
ab
n−1(q) x
n

n! .

According to [25, Theorem 1.2], we have

χ
ab(x, q) = f (−x)−q, (9.8)

where f (x) = χ
ab(−x, −1) is the exponential generating function (9.2) for numbers
of regions of Aab
n−1.
Let S be the shift operator S : f (q) ↦→ f (q − 1).

26

Theorem 9.7 Assume that 0 ≤ a < b. Then

χ
ab
n (q) = (b − a)−n(Sa + Sa+1 + · · · + Sb−1)n · qn−1.

Proof. The theorem can be deduced from Theorem 9.1 and (9.8) (using, e.g., the
Lagrange inversion formula). □

In the limit b → a, using l’Hospital’s rule, we obtain

χ
aa
n (q) = (
Sa log S
1 − S
 )n · qn−1.

In fact, there is an explicit formula for χ
aa(q). The following statement easily
follows from Corollary 9.2 and appears in [14, ??][9, proof of Prop. 3.1].

Theorem 9.8 We have

χ
aa
n (q) = (q + 1 − an)(q + 2 − an) · · · (q + n − 1 − an).

There are several equivalent ways to reformulate Theorem 9.7, as follows:

Corollary 9.9 Let r = b − a.

1. We have χ
ab
n (q) = r−n ∑ (q − φ(1) − · · · − φ(n))n−1 ,

where the sum is over all functions φ : {1, . . . , n} → {a, . . . , b − 1}.

2. We have

χ
ab
n (q) = r−n ∑

s, l≥0
(−1)l(q − s − an)n−1(n
l
 )(s + n − rl − 1
n − 1
 ).

3. We have

χ
ab
n (q) = r−n ∑ ( n
n1, . . . , nr
) (q − an1 − · · · − (b − 1)nr)n−1 ,

where the sum is over all nonnegative integers n1, n2, . . . , nr such that n1 +
n2 + · · · + nr = n.

Examples:

1. (a = 1 and b = 2) The Shi arrangement Sn−1 given by (3.6) is the arrange-
ment A12
n−1. By Corollary 9.9.1, we get the following formula of Headley [14,
??] (generalizing the formula r(Sn−1) = (n + 1)n−1 due to Shi [22, ??][23]):

χ
1 2
n (q) = (q − n)n−1.

27

2. (a ≥ 1 and b = a + 1) More generally, for the extended Shi arrangement
Sn−1, k given by (3.7), we have (cf. Corollary 9.3)

χ
a, a+1
n (q) = (q − an)n−1.

3. (a = 0 and b = 2) In this case we get the Linial arrangement Ln−1 = A02
n−1
(see Section 8). By Corollary 9.9.3, we have (cf. Theorem 8.2)

χ
0 2
n (q) = 2−n n∑

k=0
 (n
k
)
(q − k)n−1, (9.9)

4. (a ≥ 0 and b = a + 2) More generally, for the arrangement Aa, a+2
n−1 , we have

χ
a, a+2
n (q) = 2−n n∑

k=0
 (
n
k
)(q − an − k)n−1.

Formula (9.9) for the characteristic polynomial χ
0 2
n (q) was earlier obtained by
C. Athanasiadis [3, Theorem 5.2]. He used a diﬀerent approach based on a combi-
natorial interpretation of the value of χn(q) for suﬃciently large primes q.
[asymptotic behavior of χ
ab
n (q) — to be inserted]

9.3 Roots of the characteristic polynomial

Theorem 9.7 has one surprising application concerning the location of roots of the
characteristic polynomial χ
ab
n (q)
We start with the case a = b. One can reformulate Theorem 9.8 in the following
way:

Corollary 9.10 Let a ≥ 1. The roots of the polynomial χ
aa
n (q) are the numbers
an − 1, an − 2, . . . , an − n + 1 (each with multiplicity 1). In particular, the roots are
symmetric to each other with respect to the point (2a − 1)n/2.

Now assume that a ̸= b.

Theorem 9.11 Let a+b ≥ 2. All the roots of the characteristic polynomial χ
ab
n (q) of
the truncated aﬃne arrangement Aab
n−1, a ̸= b, have real part equal to (a + b − 1) n/2.
They are symmetric to each other with respect to the point (a + b − 1) n/2.

Thus in both cases the roots of the polynomial χ
ab
n (n) are symmetric to each
other with respect to the point (a + b − 1) n/2, but in the case a = b all roots are
real, whereas in the case a ̸= b the roots are on the same vertical line in the complex
plane C. Note that in the case a = b − 1 the polynomial χ
ab
n (q) has only one root
an = (a + b − 1)n/2 with multiplicity n − 1.
The following lemma is implicit in a paper of Auric [5] and also follows from
a problem posed by P´olya [18] and solved by Obreschkoﬀ [15] (repeated in [19,
Problem V.196.1, pp. 70 and 251]). For the sake of completeness we give a simple
proof.
 28

Lemma 9.12 Let P (q) ∈ C[q] have the property that every root has real part a.
Let z be a complex number satisfying |z| = 1. Then every root of the polynomial
R(q) = (S + z)P (q) = P (q − 1) + zP (q) has real part a + 1
2.

Proof. We may assume that P (q) is monic. Let

P (q) = ∏

j (q − a − bji), bj ∈ R.

If R(w) = 0, then |P (w)| = |P (w − 1)|. Suppose that w = a + 1
2 + c + di, where
c, d ∈ R and i = √−1. Thus
∣
∣
∣
∣
∣

∏

j
 (1
2 + c + (d − bj)i
)∣
∣
∣
∣
∣ =
 ∣
∣
∣
∣
∣

∏

j
 (
−1
2 + c + (d − bj)i
)∣
∣
∣
∣
∣ .

If c > 0 then ∣
∣ 1
2 + c + (d − bj)i
∣
∣ > ∣
∣− 1
2 + c + (d − bj)i
∣
∣. If c < 0 then we have strict
inequality in the opposite direction. Hence c = 0, so w has real part a + 1
2 . □

Proof of Theorem 9.11. All the roots of the polynomial qn−1 have real part
0. The operator T = (Sa + Sa+1 + · · · + Sb−1)n can be written as

T = San b−1−a∏

j=1 (S − zj)n,

where each zj is a complex number of absolute value one (in fact, a root of unity).
The proof now follows from Theorem 9.7 and Lemma 9.12. □

9.4 Other root systems.

The results of Subsections 9.1–9.3 extend, partly conjecturally, to all the other root
systems, as well as to the nonreduced root system BCn (the union of Bn and Cn,
which satisﬁes all the root system axioms except the axiom stating that if α and β
are roots satisfying α = cβ, then c = ±1). Henceforth in this section when we use
the term “root system,” we also include the case BCn.
Given a root system R in Rn and integers a and b satisfying a + b ≥ 2, we deﬁne
the truncated R-aﬃne arrangement Aab(R) to be the collection of hyperplanes

⟨α, x⟩ = −a + 1, −a + 2, . . . , b − 1,

where α ranges over all positive roots of R (with respect to some ﬁxed choice of sim-
ple roots). Here ⟨ , ⟩ denotes the usual scalar product on Rn, and x = (x1, . . . , xn).
As in the case R = An−1 we refer to the balanced case (a = b) and unbalanced case
(a ̸= b).
The characteristic polynomial for the balanced case was found by Edelman and
Reiner [9, proof of Prop. 3.1] for the root system An−1 (see Theorem 9.8), and
conjectured (Conjecture 3.3) by them for other root systems. This conjecture was

29

proved by Athanasiadis [2, Cor. 7.2.3 and Thm. 7.7.6] for types A, B, C, BC, and
D. For types A, B, C and D the result is also stated in [3, Thm. 5.5]. We will not
say anything more about the balanced case here.
For the unbalanced case, we have considerable evidence (discussed below) to
support the following conjecture.

Conjecture 9.13 Let R be an irreducible root system in Rn. Suppose that the
unbalanced truncated aﬃne arrangement A = Aab(R) has h(A) hyperplanes. Then
all the roots of the characteristic polynomial χA(q) have real part equal to h(A)/n.

Note. (a) If all the roots of χA(q) have the same real part, then this real part
must equal h(A)/n, since for any arrangement A in Rn the sum of the roots of χA(q)
is equal to h(A).
(b) Conjecture 9.13 implies the “functional equation”

χA(q) = (−1)nχA(−q + 2h(A)/n). (9.10)

Thus χA(q) is determined by around half of its coeﬃcients (or values).
(c) Let a + b ≥ 2 and R = An, Bn, Cn, or Dn. Athanasiadis [2, Thms. 7.2.1 and
7.2.4] has shown that except possibly when both a = 1 and R = Cn we have

χ
ab
R (q) = χ
0,b−a(q − ak), (9.11)

where k denotes the Coxeter number of R. Presumably this equation also holds for
the missing case a = 1 and R = Cn. For BCn there is a similar result of Athanasidis
[2, Thm. 7.2.4]. These results and conjectures reduce Conjecture 9.13 to the case
a = 0 when R is a classical root system. A similar reduction is likely to hold for the
exceptional root systems.
(d) Conjecture 9.13 is true for all the classical root systems (An, Bn, Cn, BCn, Dn).
This follows from explicit formulas found for χ
ab
R (q) by Athanasiadis [4] together with
Lemma 9.12. The result of Athanasiadis is the following.

Theorem 9.14 Up to a constant factor, we have the following characteristic poly-
nomials of the indicated arrangements. (If the formula has the form F (S)qn or
F (S)(q − 1)n, then the factor is 1/F (1).)

A0,2k+2(Bn) : (1 + S2 + · · · + S2k)2(1 + S2 + · · · + S4k+2)n−1(q − 1)n

A0,2k+2(Cn) : same as for A0,2k+2(Bn)

A0,2k+1(Bn) : (1 + S + · · · + S2k)2(1 + S2 + · · · + S4k)n−1qn

A0,2k+1(Cn) : same as for A0,2k+1(Bn)

A0,2k+2(Dn) : (1 + S2)(1 + S2 + · · · + S2k)4(1 + S2 + · · · + S4k+2)n−3(q − 1)n

A0,2k+1(Dn) : (1 + S + · · · + S2k)4(1 + S2 + · · · + S4k)n−3qn

A0,2k+2(BCn) : (1 + S2 + · · · + S2k)(1 + S2 + · · · + S4k+2)n(q − 1)n

A0,2k+1(BCn) : (1 + S + · · · + S2k)(1 + S2 + · · · + S4k)nqn.

30

We also checked Conjecture 9.13 for the arrangements A02(F4) and A02(E6) (as
well as the almost trivial case Aab(G2), a ̸= b). The characteristic polynomials are

A02(F4) : q4 − 24q3 + 258q2 − 1368q + 2917

A02(E6) : q6 − 36q5 + 630q4 − 6480q3 + 40185q2 − 140076q + 212002.

The formula for χ
02
F4(q) has the remarkable alternative form:

A02(F4) : 1
8((q − 1)4 + 3(q − 5)4 + 3(q − 7)4 + (q − 11)4) − 48.

Note that the numbers 1, 5, 7, 11 are the exponents of the root system F4. For E6
the analogous formula is given by

A02(E6) : 1
1008P (q) − 210,

where

P (q) = 61(q − 1)6 + 352(q − 4)6 + 91(q − 5)6 + 91(q − 7)6 + 352(q − 8)6 + 61(q − 11)6,

which is not as intriguing as the F4 case. It is not hard to see that the symmetry
of the coeﬃcient sequences (1, 3, 3, 1) and (61, 352, 91, 91, 352, 61) is a consequence
of equation (9.10) and the fact that if e1 < e2 < · · · < en are the exponents of an
irreducible root system R, then ei + en+1−i is independent of i.

References

[1] V. I. Arnold, The cohomology ring of colored braid group, Math. Notes 5 (1969),
138–140.

[2] C. A. Athanasiadis, Algebraic combinatorics of graph spectra, subspace ar-
rangements and Tutte polynomials, Ph.D. thesis, M.I.T., 1996.

[3] C. A. Athanasiadis, Characteristic polynomial of subspace arrangements and
ﬁnite ﬁelds, preprint dated February 13, 1996.

[4] C. A. Athanasiadis, Extended Linial hyperplane arrangements for root systems
and a conjecture of Postnikov and Stanley, preprint dated May 15, 1997.

[5] M. A. Auric, G´en´eralisation d’un th´eor`eme de Laguerre, C. R. Acad. Sci. Paris
137 (1903), 967–969.

[6] E. Brieskorn, Sur les groupes de tress. In: S´eminaire Bourbaki 1971/72, Lecture
Notes in Math. 317, Springer Verlag, 1973, pp. 21–44.

[7] N. Bourbaki, Groupes et Alg`ebres de Lie, 2`eme partie, Ch. IV–VI, Paris, Her-
mann, 1968.
 31

[8] J. L. Chandon, J. Lemaire, and J. Pouget, D´enombrement des quasi-ordres sur
un ensemble ﬁni, Math. Inform. Sci. Humaines, 62 (1978), 61–80, 83.

[9] P. Edelman and V. Reiner, Free arrangements adn rhombic tilings, Discrete
Comput. Geom. 15 (1996), 307–340.

[10] I. M. Gelfand, M. I. Graev and A. Postnikov, Combinatorics of hypergeometric
functions associated with positive roots, to appear in Arnold-Gelfand Mathe-
matical Seminars 1993-1995.

[11] I. Gessel, private communication.

[12] I. P. Goulden and D. M. Jackson, Combinatorial Enumeration, John Wiley &
Sons, 1983.

[13] F. Harary and E. M. Palmer, Graphical Enumeration, Academic Press, New
York/London, 1973.

[14] P. Headley, Reduced expressions in inﬁnite Coxeter groups, Ph.D. thesis, Uni-
versity of Michigan, 1994.

[15] N. Obreschkoﬀ, L¨osung der Aufgabe 35, Section 2, Jahresber. Deutsch. Math.-
Verein. 36 (1927), 43–45.

[16] P. Orlik and L. Solomon, Combinatorics and topology of complements of hy-
perplanes, Invent. Math. 56 (1980), 167–189.

[17] P. Orlik and H. Terao, Arrangements of Hyperplanes, Springer-Verlag, Berlin/
Heidelberg/New York, 1992.

[18] G. P´olya, Aufgabe 35, Section 2, Jahresber. Deutsch. Math.-Verein. 35 (1926),
48.

[19] G. P´olya and G. Szeg¨o, Problems and Theorems in Analysis, vol. II, Springer-
Verlag, Berlin/Heidelberg/New York, 1976.

[20] A. Postnikov, Intransitive trees, J. Combin. Theory Ser. A., to appear.

[21] D. Scott and P. Suppes, Foundational aspects of theories of measurement, J.
Symbolic Logic 23 (1958), 113–128.

[22] J.-Y. Shi, The Kazhdan-Lusztig cells in certain aﬃne Weyl groups, Lecture
Notes in Mathematics, no. 1179, Springer-Verlag, Berlin/Heidelberg/New York,
1986.

[23] J.-Y. Shi, Sign types corresponding to an aﬃne Weyl group, J. London Math.
Soc. 35 (1987), 56–74.

[24] R. Stanley, Enumerative Combinatorics, vol. 1, Wadsworth & Brooks-Cole,
Belmont, CA, 1986; reprinted by Cambridge University Press, Cambridge, 1997.

32

[25] R. Stanley, Hyperplane arrangements, interval orders, and trees, Proc. Nat.
Acad. Sci. U.S.A. 93 (1996), 2620–2625.

[26] R. Stanley, Enumerative Combinatorics, vol. 2, Cambridge University Press,
Cambridge, in preparation.

[27] W. T. Trotter, Combinatorics and Partially Ordered Sets, The Johns Hopkins
University Press, Baltimore and London, 1992.

[28] M. L. Wachs and J. W. Walker, On geometric semilattices, Order 2 (1986),
367–385.

[29] H. Whitney, A logical expansion in mathematics, Bull. Amer. Math. Soc. 38
(1932), 572–579

[30] R. L. Wine and J. E. Freund, On the enumeration of decision patterns involving
n means, Ann. Math. Statist. 28 (1957), 256–259.

[31] T. Zaslavsky, Facing up to arrangements: face-count formulas for partitions of
space by hyperplanes, Mem. Amer. Math. Soc., vol. 1, no. 154, 1975.

33
