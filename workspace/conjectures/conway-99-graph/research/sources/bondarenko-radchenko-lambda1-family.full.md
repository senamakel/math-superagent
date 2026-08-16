<!-- source: https://arxiv.org/pdf/1201.0383 | converted from PDF -->

arXiv:1201.0383v3  [math.CO]  3 Feb 2012On a family of strongly regular graphs with

λ = 1

Andriy V. Bondarenko, Danylo V. Radchenko

Abstract

In this paper, we give a complete description of strongly regu-

lar graphs with parameters ((n2 + 3n − 1)2, n2(n + 3), 1, n(n + 1)).

All possible such graphs are: the lattice graph L3,3 with parameters

(9, 4, 1, 2), the Brouwer-Haemers graph with parameters (81, 20, 1, 6),

and the Games graph with parameters (729, 112, 1, 20).

Keywords: strongly regular graph, automorphism group, Brouwer-Haemers

graph, Games graph

AMS subject classiﬁcation. 05C25, 05C50, 52C99, 41A55, 11D61

1 Introduction

A strongly regular graph Γ with parameters (v, k, λ, µ) is an undirected reg-

ular graph on v vertices of valency k such that each pair of adjacent vertices

has λ common neighbors, and each pair of nonadjacent vertices has µ com-

mon neighbors. The incidence matrix A of Γ has the following properties:

AJ = kJ,

and
 A
2 + (µ − λ)A + (µ − k)I = µJ,

1

where I is the identity matrix and J is the matrix with all entries equal to 1.

These conditions imply that

(1) (v − k − 1)µ = k(k − λ − 1).

Moreover, the matrix A has only 3 eigenvalues: k of multiplicity 1, one

positive eigenvalue

r = 1
2
 (λ − µ + √(λ − µ)2 + 4(k − µ)))

of multiplicity
 f = 1
2
 (
v − 1 − 2k + (v − 1)(λ − µ)
√(λ − µ)2 + 4(k − µ))
 )
 ,

and one negative eigenvalue

s = 1
2
 (λ − µ − √
(λ − µ)2 + 4(k − µ))
)

of multiplicity

(2) g = 1
2
 (
v − 1 + 2k + (v − 1)(λ − µ)
√(λ − µ)2 + 4(k − µ))
 )
 .

Clearly, both f and g are integers. This together with (1) gives a family

of suitable parameters (v, k, λ, µ) for strongly regular graphs. The list of

all suitable parameters and known existence results for v ≤ 1300 could be

found in [1] (except for the trivial case when Γ is a disjoint union of complete

graphs mKn or its complement). Strongly regular graphs often appear in

diﬀerent areas of group theory, geometry, and set theory. Many of strongly

regular graphs have a large automorphism group, which is the main tool

to construct them. For example, some strongly regular graphs could be

naturally obtained from a rank 3 permutation group, see [2]. On the other

hand, there are strongly regular graphs having trivial automorphism groups.

The smallest such graph has parameters (25,12,5,6), see [3].

2

Arguably, the most widely known strongly regular graphs are Moore

graphs, with λ = 0 and µ = 1. The list of all suitable parameters for

such graphs are: (5, 2, 0, 1), (10, 3, 0, 1), (50, 7, 0, 1), and (3250, 57, 0, 1). In

the ﬁrst 3 cases, the graph with mentioned parameters is unique and has

an edge transitive automorphism group. That is: the cycle graph C5, the

Petersen graph, and the Hoﬀman-Singleton graph. The question whether

exists a strongly regular graph in the last case is a well-known open prob-

lem posed by Hoﬀman and Singleton [4]. However, Higman proved that the

automorphism group of such a graph could not be even vertex transitive,

see, for example, [5]. Later, Higman’s approach was widely generalized and

applied for other graphs, see, e.g., [6] and [7]. The typical result is that, if

for a given parameter set (v, k, λ, µ) a strongly regular graph exists, then it

has a small automorphism group. Full description of parameters for which a

strongly regular graph exists is not likely to be ever done.

In this paper we will investigate strongly regular graphs with λ = 1 and

negative eigenspaces of dimension g = k. One can deduce directly from (1)

and (2) that such a graph is either K3 or belongs to the family

((n
2 + 3n − 1)2, n
2(n + 3), 1, n(n + 1)),

where n ∈ N is the positive eigenvalue.

This family includes the lattice graph L3,3 with parameters (9, 4, 1, 2), the

Brouwer-Haemers graph with parameters (81, 20, 1, 6), which is also known

to be unique [8], and the Games graph with parameters (729, 112, 1, 20), for

which the uniqueness question was open. We will show that these are the

only graphs in the family.

Theorem 1. Suppose that there exists a strongly regular graph with param-

eters ((n
2 + 3n − 1)2, n
2(n + 3), 1, n(n + 1)). Then n ∈ {1, 2, 4}.

The proof consists of two parts. First, in Section 3 we will show that each

graph in the family exhibits certain symmetries (in particular, its group of

3

automorphisms is vertex-transitive). Then, in Section 4 we will use diﬀerent

properties of these symmetries to prove that the set of vertices can be given

a vector space structure over the ﬁnite ﬁeld F3. In particular, the number of

vertices in the graph is a power of 3.

Finally, the resulting diophantine equation has the only three mentioned

solutions by virtue of [9, Theorem B]. This equation has appeared during

the studying of ternary linear codes with exactly two nonzero weights and

with the minimal weight of the dual code at least 4. It was actually shown

in [10] that each of such codes of dimension 2m implies a strongly regular

graph from the family with v = 32m vertices.

The following result completes description of the family.

Theorem 2. The strongly regular graph with parameters (729, 112, 1, 20) is

unique up to isomorphism.

We will prove Theorems 1 and 2 in Section 5.

In the next section we will explain the Euclidean representation of strongly

regular graphs, which is the main tool to prove that each graph in the family

has a vertex transitive automorphism group.

2 Euclidean representation

Let Γ = (V, E) be a strongly regular graph with negative eigenspace of

dimension g. Then there exists a set of vectors {xi : i ∈ V } ⊂ Rg satisfying

the following two conditions. First,

⟨xi, xj⟩ =
 



1, if i = j,

p, if i and j are adjacent,

q, else,

4

where p, q ∈ (−1, 1). Second condition is that the set {xi : i ∈ V } forms a

spherical 2-design, that is ∑

i∈V xi = 0,

and ∑

i,j∈V ⟨xi, xj⟩2 = |V |2

g .

The values of p and q are uniquely determined by these conditions. For more

information on relations between the Euclidean representation of strongly

regular graphs and spherical designs see [11]. To construct such vectors

consider columns {yi : i ∈ V } of the matrix A − f I and put xi := zi/∥zi∥,

where
 zi = yi − 1
|V |
 ∑

j∈V yj, i ∈ V.

It is easy to check that these vectors satisfy the above mentioned conditions.

The main tool we will use for description of strongly regular graphs is the

fact that each subset {xi : i ∈ U}, where U ⊂ V , has a positive deﬁnite Gram

matrix {(xi, xj)}i,j∈U of rank at most g. Similarly, we could get the Euclidean

representation of Γ in Rf . However, we will never use it in this paper. The

reason is that f is much larger than g for graphs from the considered family.

Thus, the Euclidian representation in Rg contains much more information.

3 Nontrivial automorphisms

Fix n ≥ 2. Let Γ = (V, E) be a strongly regular graph with parameters

((n
2 + 3n − 1)2, n
2(n + 3), 1, n(n + 1)). In this section, we will also ﬁx some

vertex v∞ of Γ. For any vertex v, let N(v) be the set of all neighbors of v,

and let N ′(v) be the set of non-neighbors of v, i.e. N ′(v) = V \ ({v} ∪ N(v)).

The subgraph induced on the set N(v∞) is isomorphic to mK2. Deﬁne the

permutation σ on the set {v∞} ∪ N(v∞) by switching all pairs of adjacent

5

vertices in N(v∞) and leaving v∞ ﬁxed. Our goal in this section is to prove

the following

Proposition 1. The permutation σ can be extended uniquely to an automor-

phism of Γ.

To prove Proposition 1 we need the next simple lemma.

Lemma 1. Suppose that m0, m1, . . . , mn−2 are nonnegative integers such that

(3)
 n−2∑

i=0
 (n − i + 1
2
 )
mi ≤ (n + 1
2
 )
.

Then the following inequality

n−2∑

i=0
 (
n − i
2
 )mi ≤ (
n
2
)
,

holds. The equality attains if and only if m0 = 1, and m1 = m2 = . . . =

mn−2 = 0.

Proof. Since, for each k < n,
(k
2
) < (k + 1
2
 ) (n
2)

(
n+1
2 ) ,

we obtain the statement of lemma by multiplying (3) by (n
2)
/(n+1
2 )
.

Proof of Proposition 1. For the Euclidean representation of the graph Γ in

Rg we have p = − n2+2n−1
n2(n+3) , and q = 1
n(n+3). Now computing the determinant

of the Gram matrix we get that vectors {xi : i ∈ N(v∞)} are linearly in-

dependent. Since |N(v∞)| = n
2(n + 3) = g, this then implies that the set

{xi : i ∈ N(v∞)} forms a basis in Rg.

For any vertex u ∈ N ′(v∞), we have |N(u) ∩ N(v∞)| = µ = n(n + 1).

Denote by A(u) the set N(u) ∩ N(v∞), and by B(u) the set of neighbors of

6

A(u) that are in N(v∞) (so that |B(u)| = |A(u)| = n(n + 1)). Then, for

α = n
n2−1, β = 1
n2−1 and γ = n
n−1, we have

(4) x = xu + α ∑

i∈A(u) xi + β ∑

i∈B(u) xi + γxv∞ = 0.

Indeed, it is easy to check that ⟨x, xi⟩ = 0 for i ∈ N(v∞), and since the set

{xi : i ∈ N(v∞)} forms a basis then x = 0. Applying equation (4) for each

pair u, w ∈ N ′(v∞) we obtain

(5)
 


⟨xu, xw⟩ = p ⇔ n|A(u) ∩ A(w)| + |A(u) ∩ B(w)| = n + 1,

⟨xu, xw⟩ = q ⇔ n|A(u) ∩ A(w)| + |A(u) ∩ B(w)| = n(n + 1).

Observe that for a pair of nonnegative integers (k, l) the equation nk +l =

n + 1 has only two solutions: (1, 1) and (0, n + 1). The equation nk + l =

n(n + 1) has n + 1 solutions: (n + 1, 0), (n, n), (n − 1, 2n), . . . , (0, n(n + 1)).

We see that |A(u) ∩ A(w)| ≤ n + 1, so in any case A(u) ̸= A(w). Thus, if

we extend σ to an automorphism of Γ, then A(σ(u)) = B(u), and therefore

σ(u) is deﬁned uniquely.

Now, we ﬁx u ∈ N ′(v∞). Clearly, there are exactly n(n + 1) vertices in

N ′(v∞)∩N(u) with |A(u)∩A(w)| = 1, and exactly n
2(n+3)−2n(n+1) such

vertices with |A(u) ∩ A(w)| = 0. Let mi, i = 0, 1, . . . , n + 1, be the number of

vertices w ∈ N ′(v∞) ∩ N ′(u) with |A(u) ∩ A(w)| = i. The numbers mi must

satisfy three equations

(6)
 




∑n+1
i=0 mi = |N ′(v∞) ∩ N ′(u)| = n
4 + 4n
3 + 2n
2 − 5n − 1,
∑n+1
i=0 imi = |A(u)|(n
2(n + 3) − 4) = n(n
2 − 1)(n + 2)2,
∑n+1
i=0 (i
2
)mi = n(n
2 − 1)(n + 2)(n
2 + n − 1)/2.

Here, the second equation is obtained by counting edges between A(u)

and N ′(v∞)∩N ′(u). We get the third equation by counting triples (v1, v2, v3),

where v1 and v2 are diﬀerent vertices in A(u), and v3 ∈ N ′(v∞) ∩ N ′(u) is

adjacent to both v1 and v2.
 7

Now, solving (6) in mn−1, mn and mn+1 we obtain

(7)
 



mn−1 = (
n+1
2 ) − ∑n−2
i=0 (
n−i+1
2 )mi,

mn+1 = n
2(n + 3) − 2n(n + 1) + (n
2) − ∑n−2
i=0 (n−i
2 )
mi.

The crucial part of the proof is the following inequality

(8) mn+1 ≤ n
2(n + 3) − 2n(n + 1)

to be proven later. Assuming (8) it is easy to conclude the proof of Propo-

sition 1. Indeed, combining (7) and (8) with the statement of Lemma 1 we

immediately obtain that m0 = 1, and m1 = m2 = . . . = mn−1 = 0. There-

fore, for each u ∈ N ′(v∞) there exists a unique vertex wu ∈ N ′(v∞) such that

A(u) = B(wu). Deﬁne σ by σ(u) = wu, u ∈ N ′(v∞). Then σ is a bijection,

because σ(σ(u)) = u. Finally, since for each pair u, w ∈ N ′(v∞)

|A(u) ∩ A(w)| = |B(u) ∩ B(w)| = |A(σ(u)) ∩ A(σ(w))|,

and
 |A(u) ∩ B(w)| = |B(u) ∩ A(w)| = |A(σ(u)) ∩ B(σ(w))|,

we see that σ is an automorphism by virtue of (5), proving Proposition 1.

Now, we are ready to prove (8).

Denote by C(u) the set {w ∈ N ′(v∞) ∩ N(u) : |A(u) ∩ A(w)| = 1}, and

by D(u) the set {w ∈ N ′(v∞) ∩ N ′(u) : |A(u) ∩ A(w)| = n + 1}. We have

|C(u)| = |B(u)| = n(n + 1), and also |D(u)| = mn+1. Thus, to prove (8) it

is suﬃcient to show that vectors {xi : i ∈ B(u) ∪ C(u) ∪ D(u)} are linearly

independent (recall that g = n
2(n + 3)).

First, note that there are no edges between B(u)∪C(u) and D(u), between

v∞ and C(u), and between u and B(u). Then, v∞ is connected to each vertex

in B(u), and u is connected to each vertex in C(u). Also, in the subgraph

induced on B(u) ∪ C(u) every vertex has a degree 1. Suppose that there is

a nontrivial linear relation

(9) ∑

i∈B(u) βixi + ∑

i∈C(u) γixi + ∑

i∈D(u) δixi = 0.

8

For i ∈ B(u), denote by φ(i) ∈ V its unique neighbor in C(u). Put

SB = ∑

i∈B(u) βi, SC = ∑

i∈C(u) γi, and SD = ∑

i∈D(u) δi. Now, taking inner

products of both sides in (9) with xv∞ and with xu, we get

(10)
 


pSB + qSC + qSD = 0,

qSB + pSC + qSD = 0.

Similarly, taking inner products of both sides in (9) with xi and with xφ(i)
for each i ∈ B(u), we obtain

(11)
 


(1 − q)βi + (p − q)γφ(i) + qSB + qSC + qSD = 0,

(p − q)βi + (1 − q)γφ(i) + qSB + qSC + qSD = 0.

Subtracting from the ﬁrst equation in (10) the second we get that SB = SC.

Similarly, (11) yields βi = γφ(i), i ∈ B(u). Now, summing up the ﬁrst

equation of (11) over all i ∈ B(u) we obtain

(1 + p + 2(n
2 + n − 1)q)SB + n(n + 1)qSD = 0.

Combining this equation with (10) we get SB = SC = SD = 0. Thus, (11)

together with inequality 1 + p − 2q > 0, n ≥ 2, implies that βi = γφ(i) = 0

for all i ∈ B(u). Therefore, we are left with the relation
∑

i∈D(u) δixi = 0,

where ∑

i∈D(u) δi = 0. Let δ+
i = max(δi, 0), and δ−
i = − min(δi, 0). Then we

have ∑

i∈D(u) δ+
i xi = ∑

i∈D(u) δ−
i xi.

Normalizing δi in such a way that ∑

i∈D(u) δ+
i = ∑

i∈D(u) δ−
i = 1 we obtain

the following bound

∥ ∑

i∈D(u) δ+
i xi∥2 = ⟨ ∑

i∈D(u) δ+
i xi, ∑

i∈D(u) δ−
i xi⟩ = ∑

i,j∈D(u) δ+
i δ−
j ⟨xi, xj⟩(12)
 = ∑

i,j∈D(u),i̸=j δ+
i δ−
j ⟨xi, xj⟩ ≤ q ∑

i,j∈D(u),i̸=j δ+
i δ−
j = q,

9

where we used the fact that δ+
i δ−
i = 0 for i ∈ D(u), and ⟨xi, xj⟩ ≤ q for i ̸= j.

We will now use (12) to show that the quadratic form of three variables

Q(a, b, c) = ∥a(xu + xv∞) + b ∑

i∈B(u)∪C(u) xi + c ∑

i∈D(u) δ+
i xi∥2

attains a negative value for some a, b, c ∈ R, thus contradicting our assump-

tion (9). Let (aij) be the symmetric 3 × 3 matrix associated to the quadratic

form Q. Its entries are:

a11 = ∥xu + xv∞∥2 = 2 + 2q,

a12 = (|B(u)|p + |C(u)|q) + (|B(u)|q + |C(u)|p) = 2n(n + 1)(p + q),

a13 = 2q ∑

i∈D(u) δ+
i = 2q,

a22 = |B(u) ∪ C(u)|(1 + p + 2(n
2 + n − 1)q) = 2n(n + 1)(1 + p + 2(n
2 + n − 1)q),

a23 = |B(u) ∪ C(u)| ∑

i∈D(u) δ+
i q = 2n(n + 1)q,

a33 = ∥ ∑

i∈D(u) δ+
i xi∥2 ≤ q.

We may assume that a33 = q, since Q(a, b, c) can only increase. The deter-

minant of the resulting matrix is

det(aij) = −8(n + 1)(n
4 + 6n
3 + 7n
2 − 6n + 1)
n3(n + 3)3 ,

which is negative for n ≥ 1. Thus, Q attains a negative value. Therefore

vectors {xi : i ∈ B(u) ∪ C(u) ∪ D(u)} are linearly independent, proving (8)

and hence Proposition 1.

For each v ∈ V , denote by σv the automorphism constructed for v∞ = v.

It follows from the deﬁnition that each σv is an involution. Moreover, for

each three vertices u, v, and w forming a triangle, σu(v) = w. Since Γ is a

connected graph this immediately implies that Aut(Γ) is vertex transitive.

10

4 Structure of automorphisms

We now proceed to study the global structure of strongly regular graphs with

parameters
 ((n
2 + 3n − 1)2, n
2(n + 3), 1, n(n + 1))

by using the automorphisms we have constructed in Proposition 1. In this

section, we will prove the following

Proposition 2. The set of vertices V can be given a vector space structure

over F3 such that σv(u) = −(u + v) for all u, v ∈ V , in particular, |V | = 3m

for some m ∈ N.

First, we establish some properties of σv.

Lemma 2. Involutions {σu : u ∈ V } satisfy the following:

(i) σu(v) = σv(u) for all u, v ∈ V ;

(ii) if g is any automorphism of Γ, then gσu = σg(u)g;

(iii) σuσvσu = σσu(v) for all u, v ∈ V ;

(iv) the automorphism σuσv has no ﬁxed points, and (σuσv)3 = e for all

u ̸= v ∈ V ;

(v) if u and v are adjacent, then for all x ∈ V the vertices x and σuσv(x)

are also adjacent.

Proof. If u and v are adjacent, then they have both vertices σu(v) and σv(u)

as common neighbors. Thus the condition λ = 1 implies that σu(v) = σv(u).

If u and v are nonadjacent, then σu(v) is a unique vertex w, such that w is

nonadjacent to both u and v, and N(u) ∩ N(v) ∩ N(w) = ∅. Hence, in this

case we also have σu(v) = σv(u). This proves (i).

11

From (i) we see that triples {u, v, w} with w = σu(v) are deﬁned sym-

metrically in u, v, w, that is the following identities

w = σu(v) = σv(u), v = σu(w) = σw(u), u = σw(v) = σv(w)

hold. Therefore, g must preserve the set of such triples. This means that

σg(u)(g(v)) = g(w) = g(σu(v)), which proves (ii).

Part (iii) follows from (ii) by letting g = σv.

From (iii) we have σuσvσu = σσu(v) = σσv (u) = σvσuσv, hence (σuσv)3 = e.

If σu(σv(x)) = x, then σu(x) = σv(x), and therefore σx(u) = σx(v), which

contradicts u ̸= v. This proves (iv).

Finally, since σx is a graph automorphism for each x ∈ V , then for an ad-

jacent pair of vertices u and v the vertices σx(u) and σx(v) are also adjacent.

Similarly, the vertices σu(σx(u)) = x and σu(σx(v)) = σuσv(x) are adjacent

as well. This proves (v).

In the sequel, we will use the notation u ◦ v for σu(v). It is convenient,

since for any automorphism g we have g(u ◦ v) = g(u) ◦ g(v). The crucial

part in the proof of Proposition 2 is the following lemma.

Lemma 3. For all u, v, w ∈ V , we have (σvσwσu)2 = e.

Proof. We may assume that u, v, w are diﬀerent vertices, as other cases are

covered by Lemma 2.

Denote g1 = σuσv, g2 = σu◦wσw◦(u◦v), and g3 = σwσu◦(v◦w). Since u ̸= v

then u ◦ w ̸= w ◦ (u ◦ v), and w ̸= u ◦ (v ◦ w). Hence, by Lemma 2 (iv),

the automorphisms g1, g2, and g3 are of order 3, and have no ﬁxed points.

Moreover, we claim that g1g2g3 = e. Indeed, we have

g1 = σuσv,

g2 = σu◦wσw◦(u◦v) = σw(σuσwσwσu)σvσuσw = σwσvσuσw,

g3 = σwσu◦(v◦w) = σwσuσwσvσwσu,

12

where we used σx◦y = σσx(y) = σxσyσx repeatedly. Therefore,

g1g2g3 = σuσvσwσv(σuσwσwσu)σwσvσwσu =

σuσvσwσvσwσvσwσu = σu(σvσw)3σu = σ2
u = e.

Let us ﬁrst suppose that u and v are adjacent. Then, by Lemma 2 (v),

the vertices u ◦ w and w ◦ (u ◦ v) are also adjacent. Similarly, w and u ◦ (v ◦ w)

are adjacent. Using again Lemma 2 (v), we see that {x, gi(x), g−1
i (x)} is a

triangle for any x ∈ V and i ∈ {1, 2, 3}. From g1g2g3 = e we ﬁnd that

g3(x) = g−1
2 (g−1
1 (x)), therefore g−1
1 (x) and g3(x) are adjacent. Hence x and

g−1
1 (x) are also adjacent, and have two common neighbors g1(x) and g3(x).

Since λ = 1 then g1(x) = g3(x). The choice of x was arbitrary, therefore

g1 = g3. Thus we obtain

g1 = g3 ⇔ σuσv = σwσuσwσvσwσu ⇔

σv(σuσw)2σvσwσu = e ⇔ (σvσwσu)2 = e,

as claimed.

Now, suppose that u and v are nonadjacent. Then there exists t ∈ V

adjacent to both u and v. By the previous case, we have

(σtσwσu)2 = e,

(σvσwσt)2 = e,

σtσvσuσt = σuσv,

where the last equation is another form of (σtσvσu)2 = e. Multiplying the

ﬁrst two equations together, we get

e = (σvσwσt)2(σtσwσu)2 =

σvσwσtσv(σwσtσtσw)σuσtσwσu =

σvσw(σtσvσuσt)σwσu =

σvσwσuσvσwσu = (σvσwσu)2.

Lemma 3 is proved.
 13

Proof of Proposition 2. Now we can introduce a vector space structure on

V . Take some vertex v0 ∈ V and deﬁne it to be the zero vector. Denote the

multiplication of a vector v ∈ V by scalars from F3 as follows

1v = v, 0v = v0, and (−1)v = σv0(v).

Finally, for each u, v ∈ V deﬁne vector addition by

u + v = σv0(u ◦ v).

We only need to check that these operations indeed deﬁne a vector space over

F3. First, let us show the associativity of the vector addition. For arbitrary

u, v, w ∈ V , we have

u + (v + w) = (u + v) + w ⇔ σv0(u ◦ (v + w)) = σv0((u + v) ◦ w) ⇔

u ◦ (v + w) = (u + v) ◦ w ⇔ σuσv0(v ◦ w) = σwσv0(v ◦ u) ⇔

σuσv0σw(v) = σwσv0σu(v) ⇔ (σuσv0σw)2(v) = v,

which is true by Lemma 3. The rest of axioms are easily deduced from

Lemma 2. Namely, for each u, v ∈ V we have

u + v = σv0(u ◦ v) = σv0(v ◦ u) = v + u,

v + v0 = σv0σv0(v) = v, (−1)((−1)v) = σv0σv0(v) = v,

v+v = σv0σv(v) = σv0v = (−1)v, v+(−1)v = σv0σvσv0(v) = σvσv0σv(v) = v0,

and

−(u + v) = σv0σv0(u ◦ v) = σu(v) = σv0(u) + σv0(v) = (−1)u + (−1)v.

Proposition 2 is proved.

As a corollary, we see that each strongly regular graph in the family must

have 3m vertices, m ∈ N. For example, there is no strongly regular graph

with parameters (289, 54, 1, 12).
 14

5 Proof of main results

Now we are ready to prove Theorem 1.

Proof of Theorem 1. By Propositions 1 and 2 it remains to show that the

diophantine equation n
2+3n−1 = 3m has only the following integer solutions

(n, m) with n > 0:
 (1, 1), (2, 2), (4, 3).

Substituting u = 2n + 3 we obtain an equivalent equation

u2 − 13 = 4 · 3m.

By [9, Theorem B], this equation can hold only for m = 1, 2 or 3.

With some more work we can prove that there exists a unique strongly regular

graph with parameters (729, 112, 1, 20), namely the Games graph.

Proof of Theorem 2. Let Γ = (V, E) be a strongly regular graph with param-

eters (729, 112, 1, 20). By Proposition 2 we may assume that V = F 6
3 , and

for any x ∈ V the map σx : t → −(t + x) is a graph automorphism. Since

σ0σx(t) = t + x, we have that all shifts t → x + t are also automorphisms.

Therefore x and y are adjacent if and only if 0 and x − y are adjacent. The

last implies that 0 and x are adjacent if and only if 0 and −x are adjacent.

Hence, we can form a set H ⊂ P G(5, F3) by saying [x] ∈ H if and only if 0

and x are adjacent ([x] is the equivalence class of x ∈ F 6
3 \ {0} in P G(5, F3)).

The set H consists of 56 points. Now, we claim that H is a cap, i.e., any

line in P G(5, F3) meets H in at most two points. Indeed, it is suﬃcient to

consider three collinear points [x], [y], [x + y] ∈ H. Then 0 is connected to x,

y, and x + y. Similarly, x + y is connected to x, y, and 0. This contradicts

the fact that λ = 1, as 0 and x + y are connected and have x and y as

common neighbors. This proves that H is a cap. It was shown by Hill [12]

that there exists a unique cap with 56 points in P G(5, F3), and therefore H

15

is isomorphic to it. Hence Γ is isomorphic to the Games graph, as can be

seen from the construction given in [13, p.114-115].

References

[1] A. E. Brouwer, Parameters of strongly regular graphs, tables published

electronically at http://www.win.tue.nl/∼aeb/graphs/srg/srgtab.html.

[2] R. Griess, Twelve sporadic groups, Springer Monographs in Mathemat-

ics, 1998.

[3] H. Cohn, N. Elkies, A. Kumar, and A. Sch¨urmann, Point conﬁgurations

that are asymmetric yet balanced, Proc. Amer. Math. Soc. 138 (2010)

2863-2872.

[4] A. J. Hoﬀman, R. R. Singleton, On Moore graphs with diameters 2 and

3, IBM J. Res. Dev. 4 (1960) 497504.

[5] P. Cameron, Permutation Groups, Cambridge University Press, 1999.

[6] M. Maˇcaj, J. ˇSir´aˇn, Search for properties of the missing Moore graph,

Linear Algebra and Its Applications, 432 (2010) 2381-2398.

[7] A. A. Makhnev, V. V. Nosov, On automorphisms of strongly regular

graphs with λ = 0 and µ = 3, St. Petersburg Math. J., 21 (2010) 779-

790.

[8] A.E. Brouwer, W.H. Haemers, Structure and uniqueness of the

(81,20,1,6) strongly regular graph, Discrete Math. 106/107 (1992) 77-

82.
 16

[9] A. Bremner, R. Calderbank, P. Hanlon, P. Morton, and J. Wolfskill,

Two-weight ternary codes and the equation y2 = 4.3a + 13, J. Number

Theory 16 (1983) 212-234.

[10] R. Calderbank , W. M. Kantor, The geometry of two-weight codes, Bul-

letin of the London Mathematical Society, 18 (1986) 97-122.

[11] P. Cameron, Strongly regular graphs, in Selected Topics in Algebraic

Graph Theory (eds. L.W. Beineke and R.J. Wilson), Cambridge Univ.

Press, 2004.

[12] R. Hill, Caps and codes, Discrete Math. 22 (1978) 111-137.

[13] A.E. Brouwer, J.H. van Lint, Strongly regular graphs and partial geome-

tries, Enumeration and Design - Proc. Silver Jubilee Conf. on Combi-

natorics, Waterloo, 1982, pp. 85-122.

Centre de Recerca Matem`atica, Campus de Bellaterra, 08193 Bellaterra (Barcelona), Spain
and

Department of Mathematical Analysis, National Taras Shevchenko University, str. Volodymyrska,
64, Kyiv, 01033, Ukraine

Email address: andriybond@gmail.com

Department of Mathematical Analysis, National Taras Shevchenko University, str. Volodymyrska,

64, Kyiv, 01033, Ukraine
Email address: danradchenko@gmail.com
 17
