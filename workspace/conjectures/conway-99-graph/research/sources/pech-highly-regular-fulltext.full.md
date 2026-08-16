<!-- source: https://alco.centre-mersenne.org/item/ALCO_2021__4_5_843_0.pdf | converted from PDF -->

ALGEBRAIC
 COMBINATORICS

Christian Pech

On highly regular strongly regular graphs
Volume 4, issue 5 (2021), p. 843-878.

<http://alco.centre-mersenne.org/item/ALCO_2021__4_5_843_0>

© The journal and the authors, 2021.
Some rights reserved.

This article is licensed under the
CREATIVE COMMONS ATTRIBUTION 4.0 INTERNATIONAL LICENSE.
http://creativecommons.org/licenses/by/4.0/

Access to articles published by the journal Algebraic Combinatorics on
the website http://alco.centre-mersenne.org/ implies agreement with the
Terms of Use (http://alco.centre-mersenne.org/legal/).

Algebraic Combinatorics is member of the
Centre Mersenne for Open Scientiﬁc Publishing
www.centre-mersenne.org

Algebraic Combinatorics
Volume 4, issue 5 (2021), p. 843–878
https://doi.org/10.5802/alco.183

On highly regular strongly regular graphs

Christian Pech

Abstract In this paper we unify several existing regularity conditions for graphs, including
strong regularity, k-isoregularity, and the t-vertex condition. We develop an algebraic composi-
tion/decomposition theory of regularity conditions. Using our theoretical results we show that
a family of non rank 3 graphs known to satisfy the 7-vertex condition fulﬁlls an even stronger
condition, (3, 7)-regularity (the notion is deﬁned in the text). Derived from this family we obtain
a new inﬁnite family of non rank 3 strongly regular graphs satisfying the 6-vertex condition.
This strengthens and generalizes previous results by Reichard.

1. Introduction

Strongly regular graphs (srgs) are simple regular graphs with the property that the
number of common neighbors of a pair of distinct vertices depends only on whether
the two vertices are connected by an edge or not. Originally introduced by R. C. Bose
in [4], they are one of the central notions of modern algebraic graph theory. Small
examples include the pentagon, the Petersen graph, triangular graphs, the Clebsch
graph, . . . (A. E. Brouwer maintains a list of known small examples at [6]). Srgs arise,
e.g. as orbital graphs of permutation groups of rank three (such srgs are usually called
rank 3 graphs or 2-homogeneous graphs). Thanks to the classiﬁcation of ﬁnite simple
groups, all rank 3 graphs are known by now (cf. [2,32,39]). However, by no means, all
srgs arise in this way. Srgs exist in such an abundance that nowadays a complete clas-
siﬁcation up to isomorphism seems hopeless (cf. [17, 43, 58]). To single out the more
interesting specimen it is necessary to impose stronger regularity conditions. One pos-
sible such regularity condition is the so-called t-vertex condition that was introduced
by D. G. Higman in [25] (cf. also [24]). A graph is said to fulﬁll the t-vertex condition
if the number of subgraphs with at most t vertices of a given isomorphism type over
a ﬁxed pair of vertices depends only on whether or not the vertices are connected by
an edge or whether they are equal. Thus the t-vertex condition is, in fact, a class of
regularity conditions parameterized by t which generalizes the regularity conditions
of strongly regular graphs. In particular, the srgs are precisely the graphs that fulﬁll
the 3-vertex condition. Clearly, all rank 3 graphs satisfy the t-vertex condition for ar-
bitrary t. Of special interest are non-rank 3 graphs that satisfy the t-vertex condition
for some t > 3. The smallest examples for t = 4 have order 36 (cf. [35]). As non-rank
3 srgs with the t-vertex condition for t > 3 appear to be very rare, there has been

Manuscript received 19th December 2017, revised 28th February 2021, accepted 6th May 2021.

Keywords. Strongly regular graphs, invariants, k-isoregularity, t-vertex condition, partial quadran-
gles, generalized quadrangles, partial linear spaces.

ISSN: 2589-5486 http://algebraic-combinatorics.org/

Christian Pech

an ongoing research eﬀort to discover new examples and to understand their nature
(cf. [28, 29, 33, 35, 49, 51]).
Another class of regularity conditions strengthening strong regularity is k-isoregu-
larity. A graph is said to be k-isoregular if for every set S of at most k vertices the
number of common neighbors of the elements of S depends only on the isomorphism
type of the subgraph induced by S. The srgs are precisely the 2-isoregular graphs.
In the same way that the t-vertex condition is a combinatorial approximation of 2-
homogeneity, k-isoregularity is a combinatorial approximation of k-homogeneity. The
notion of k-isoregularity has its origins in works by J. M. J. Buczak, Ja. Ju. Gol’fand,
and M. Klin ([8, 22]).
For a comprehensive overview of the history and the literature related to the t-
vertex condition and k-isoregularity, we refer to Section 9 of Reichard’s [51].
Every 5-isoregular ﬁnite graph is homogeneous (cf. [10]), i.e. every isomorphism
between subgraphs extends to an automorphism. Similarly, it was conjectured by
M. Klin (cf. [16]) that there is a number t0 such that an srg is 2-homogeneous if and
only if it satisﬁes the t0-vertex condition. To prove or refute this conjecture, it is
necessary to have good methods for observing whether or not a given graph fulﬁlls
the t-vertex condition. Already in [24] Hestenes and Higman noticed that to verify the
4-vertex condition it is enough to test it just for two types of subgraphs. More results
on how to simplify the testing of the t-vertex condition were given by A. V. Ivanov
and S. Reichard [29, 49].
In this paper, we develop a theory of regularity conditions applicable, in principle,
to many categories of combinatorial objects. This leads us to new criteria for the t-
vertex condition and for (k, t)-regularity (a regularity condition that strengthens the
concept of k-isoregularity in the same way as the t-vertex condition strengthens the
concept of 2-isoregularity).
Using our techniques, we show that the point graphs of partial quadrangles (in the
sense of [9]) fulﬁll the 5-vertex condition (see Theorem 5.7). Moreover, we show that
if the point graph of a partial quadrangle is 3-isoregular, then it is (3, 7)-regular (see
Theorem 5.17). In particular, the point graphs of generalized quadrangles of order
(q, q2) are (3, 7)-regular (this strengthens a recent result by S. Reichard [51] stating
that the point graphs of GQ(q, q2) satisfy the 7-vertex condition). As a consequence we
obtain that the point graphs of partial quadrangles of order (s, t, µ) = (q −1, q2, q2 −q)
satisfy the 6-vertex condition (see Corollary 5.19).
The paper is structured into two main parts, a theoretical one (consisting of Sec-
tions 3 and 4) and a more applied one (consisting of Section 5).
Section 3 is the technical backbone of the paper. Here graph types and the re-
lated regularity conditions (like T-regularity and (m, n)-regularity) are deﬁned and
compared to classical regularity conditions (like k-isoregularity and the t-vertex con-
dition). The main result of this section is the type counting lemma (Lemma 3.28).
Roughly speaking it states that graphs that are regular for some graph types are also
regular for some other, bigger graph types. Its proof hinges on an elementary notion
from category theory, namely, the universal property of colimits, that provides a bi-
jection between compatible cocones of a diagram with the morphisms starting from a
given ﬁxed colimit of this diagram. In the rest of Section 3, the type counting lemma
is used to derive those criteria for (m, n)-regularity that are used in the applied sec-
ond part of the paper. Of particular interest for the reader may be Corollary 3.42, a
criterion for the (m, n)-regularity formulated purely in graph-theoretical language.
In Section 4 the results from Section 3 are used to improve known criteria for the
t-vertex condition.

Algebraic Combinatorics, Vol. 4 #5 (2021) 844

On highly regular strongly regular graphs

At some places of the paper we are faced with the problem of enumerating unlabeled
3- and 4-connected graphs of small orders (⩽ 8). While these tasks can certainly be
completed “by hand” using the known inductive methods for their construction from
literature (notably Tutte’s characterization of 3-connected graphs [56], and Slater’s
characterization of 4-connected graphs [53]), it is safer to trust in computers for such
calculations. We used the geng-utility from the package nauty and traces (cf. [42]) in
conjunction with GAP (cf. [18]) and GRAPE (cf. [54]) for the automatic enumeration
of small 3- and 4-connected graphs.
In this paper, problems from algebraic graph theory are treated using methods
from category theory. The results are then applied to graphs constructed out of ﬁ-
nite incidence geometries (notably partial quadrangles and generalized quadrangles).
While the paper is written in a mostly self-contained manner, it may be helpful to
have some standard literature from these ﬁelds at hand. A modern source for algebraic
graph theory is [21]. For notions from category theory, we refer to the classics [3, 40].
For incidence geometries we recommend [14] as a starting point (see also [47]). Finally,
for a recent survey on homogeneous structures, we refer to [41].

2. Preliminaries about the category of graphs

Let us start by ﬁxing some notations: A graph is a pair (V, E) where V is a ﬁnite set
of vertices and E ⊆ (V
2 ) is a set of undirected edges.(1) If Γ is a graph, then by V (Γ)
we denote the vertex set and by E(Γ) we denote the edge set of Γ. If M ⊆ V (Γ), then
by Γ(M ) we denote the subgraph of Γ induced by M . As usual, the order of a graph is
the number of its vertices and the valency of a vertex is the number of its neighbors.
A graph Γ for which E(Γ) = (V (Γ)
2 ) is called a complete graph. A complete graph of
order n is denoted by Kn. The complement of a graph Γ is (V (Γ), (V (Γ)
2 ) ∖ E(Γ)). It
is denoted by Γ.
The class of all graphs can be naturally equipped with a concept of homomor-
phisms: A graph homomorphism (or short: homomorphism) from a graph Γ1 to a graph
Γ2 is a function f : V (Γ1) → V (Γ2) with the property that for each {v, w} ∈ E(Γ1) we
have that {f (v), f (w)} ∈ E(Γ2). A one-to-one homomorphism f : Γ1 → Γ2 is called
an embedding if for all {v, w} ∈ (V (Γ1)
2 ) : {v, w} ∈ E(Γ1) ⇐⇒ {f (v), f (w)} ∈ E(Γ2).
Following the tradition of category theory (and somewhat conﬂicting with the
tradition of algebraic graph theory), whenever f : A → B, and g : B → C, then the
composition of f and g is a morphism from A to C that is denoted by g ◦ f . That is,
we use the convention that morphisms are applied to elements of their domain from
the left so that (f ◦ g)(x) = f (g(x)).
Next, we introduce the main construction principle of graphs relevant to this paper.
It has a combinatorial and a category-theoretic dimension. Let us start with the
category-theoretic one. In what follows we will use capital greek letters to denote
suitable (local) subgraphs of a considered global graph. As a rule, the global graph
itself is denoted by the letter Γ.

Definition 2.1. Let ∆, Θ1, Θ2 be graphs and let f1 : ∆ → Θ1, f2 : ∆ → Θ2 be
homomorphisms. A compatible cocone of (f1, f2) is a pair (g1, g2) where g1 : Θ1 → Θ,

(1)Here and below, for a set M and a non-negative integer k, by (M
k ) we denote the set of
k-element subsets of M .

Algebraic Combinatorics, Vol. 4 #5 (2021) 845

Christian Pech

g2 : Θ2 → Θ for some graph Θ, such that the following diagram commutes:

(1) Θ1 Θ

∆ Θ2

g1

f1 f2
 g2 .

The cocone (g1, g2) is called a limiting cocone of (f1, f2) if for any other compatible
cocone (h1, h2) of (f1, f2) where h1 : Θ1 → Γ, h2 : Θ2 → Γ there exists a unique
homomorphism k : Θ → Γ such that the following diagram commutes:

Γ

Θ1 Θ

∆ Θ2

g1

h1
 k

f1 f2
 g2
 h2 .

In that case the diagram (1) is called a pushout square.

For us, only the special case when (f1, f2) is a pair of embeddings is of interest.
In this case, for every limiting cocone (g1, g2) of (f1, f2) we have that g1 and g2 are
embeddings, too. A concrete construction of limiting cocones of pairs of embeddings
in the category of graphs goes as follows:

Construction. Let f1 : ∆ ↪→ Θ1, f2 : ∆ ↪→ Θ2 be embeddings. Let ̃Θ be the disjoint
union of Θ1 and Θ2. Let θ ⊆ V ( ̃Θ)
2 be the smallest equivalence relation that contains
{(f1(v), f2(v)) | v ∈ V (∆)}. Let Θ := ̃Θ/θ (vertices of Θ are equivalence classes of
θ and two classes are connected by an edge if some representatives of the classes are
connected by an edge in ̃Θ). Finally, let g1 : Θ1 ↪→ Θ and g2 : Θ2 ↪→ Θ be given by
g1 : v ↦→ [v]θ, g2 : w ↦→ [w]θ. Then (g1, g2) is a limiting cocone for (f1, f2).
Note that θ has equivalence classes of size ⩽ 2. One can imagine that Θ is ob-
tained by glueing Θ1 and Θ2 together at a copy of ∆, which is marked in Θ1 and
Θ2 through f1 and f2, respectively. This construction is also known under the name
graph amalgamation, ﬁbered sum or amalgamated free sum (cf. [40, 44]).

Example 2.2. Consider the following three graphs:

∆ : x y Θ1 :
 u1 u2

u3
 Θ2 :
 v1 v2

v3 v4
 .

Deﬁne f1 : ∆ ↪→ Θ1 and f2 : ∆ ↪→ Θ2 according to

f1 : x ↦→ u1, y ↦→ u2; f2 : x ↦→ v3, y ↦→ v4.

According to the construction of amalgamated free sums we have that V (Θ) =
(V (Θ1) ˙∪V (Θ2))/θ, where θ is the equivalence relation on V (Θ1) ˙∪V (Θ2) generated by

{(f1(x), f2(x)), (f1(y), f2(y))} = {(u1, v3), (u2, v4)},

Algebraic Combinatorics, Vol. 4 #5 (2021) 846

On highly regular strongly regular graphs

and where the operation ˙∪ denotes the disjoint union of sets. In other words,
V (Θ) = {{u1, v3}, {u2, v4}, {u3}, {v1}, {v2}}, and Θ is given by

Θ :
 {v1} {v2}

{u1, v3} {u2, v4}

{u3}
 .

3. Graph types and regularity conditions

The t-vertex condition arises from a local invariant of pairs of vertices of a graph. Let
Γ = (V, E) be a graph and let (x, y) ∈ V 2. We consider all induced subgraphs of Γ
that contain x and y and that have order ⩽ t. Two such subgraphs are said to be
of the same type if they are isomorphic by an isomorphism that ﬁxes x and y. The
possible types of subgraphs correspond to all isomorphism classes of graphs of order
⩽ t with a pair of distinguished vertices. To the pair (x, y) ∈ V 2 we may associate
a function ϕx,y from the types to the natural numbers that maps every type to the
number of induced subgraphs of Γ that contain x and y and that are of this type.
Graphs Γ where the function ϕx,y does not depend directly on the pair (x, y) but only
on whether x = y or {x, y} ∈ E or {x, y} ∈ (V
2 ) ∖ E, are said to fulﬁll the t-vertex
condition. In the following, we give an equivalent deﬁnition of the t-vertex condition
using the language of category theory.

3.1. Basic definitions.

Definition 3.1. A graph type T is a triple (∆, ι, Θ) where ∆ and Θ are graphs and
ι : ∆ ↪→ Θ is an embedding. The order of T is the pair (m, n) where m is the order of
∆ and n is the order of Θ. The graphs ∆ and Θ are called base graph and underlying
graph of T, respectively.

Example 3.2. Consider the following graphs:

∆ : a1 a2 Θ :
 b1 b2

b3 b4

ι : ∆ ↪→ Θ shall be given by ι : a1 ↦→ b1, a2 ↦→ b2. Then T = (∆, ι, Θ) is a graph type
of order (2, 4).

For given graph types T1 = (∆1, ι1, Θ1) and T2 = (∆2, ι2, Θ2) a morphism from
T1 to T2 is pair (f, g) of graph homomorphisms such that f : ∆1 → ∆2, g : Θ1 → Θ2
and such that the following diagram commutes.

∆2 Θ2

∆1 Θ1

ι2

ι1

f g

With this choice of morphisms graph types form a category. In particular, there is a
natural concept of isomorphism between graph types.

Algebraic Combinatorics, Vol. 4 #5 (2021) 847

Christian Pech

Remark 3.3. When we depict a graph type T = (∆, ι, Θ), we prefer a more compact
representation than in Example 3.2. We draw a picture of Θ. Then we mark ι(v) in
black, for all v ∈ V (∆). Clearly, this determines the graph type up to isomorphism.
For instance, the graph type from Example 3.2 is depicted as follows:

T : .

In case it is not implied otherwise by the context, we always assume that the base
graph ∆ is an induced subgraph of Θ and that the embedding ι is the identical
embedding.

A ﬁrst observation about the category of graph types is:

Lemma 3.4. Given natural numbers m and n such that m ⩽ n, there are just ﬁnitely
many isomorphism classes of graph types of order (m, n).

Proof. There are just ﬁnitely many (say, l) unlabeled graphs of order n. Moreover,
every graph of order n accounts for at most ( n
m
) graph types of order (m, n), up to
isomorphism. Hence, there are at most l · ( n
m
) isomorphism classes of graph types of
order (m, n). □

Definition 3.5. Let T = (∆, ι, Θ) be a graph type, let Γ be a graph, and let κ : ∆ ↪→ Γ
be an embedding. An embedding ˆκ : Θ ↪→ Γ is called an extension of κ along ι if the
following diagram commutes:
 Θ Γ

∆
 ˆκ

κ
ι .

The number of all extensions of κ along ι is denoted by #(Γ, T, κ). If ∆ embeds into
Γ and if for every pair of embeddings κ, κ
′ : ∆ ↪→ Γ we have #(Γ, T, κ) = #(Γ, T, κ
′),
then this number is denoted by #(Γ, T). In case that ∆ does not embed into Γ, we
deﬁne #(Γ, T) := 0. In both cases Γ is called T-regular.

Example 3.6. Let us consider the complement graph Γ1 of the Petersen graph:

Γ1 : 1
 6

2
 7

3

8
 4

9
 5

10
 .

Take the graph type from Example 3.2. Let us ﬁx an embedding κ : ∆ ↪→ Γ1, say,
κ : a1 ↦→ 1, a2 ↦→ 2. The joint neighbors of 1 and 2 in Γ1 are 4, 6, 7, and 8. These

Algebraic Combinatorics, Vol. 4 #5 (2021) 848

On highly regular strongly regular graphs

vertices induce a 4-cycle. Thus, there are exactly eight extensions of κ along ι, namely

ˆκ1 : b1 ↦→ 1, b2 ↦→ 2, b3 ↦→ 4, b4 ↦→ 6, ˆκ2 : b1 ↦→ 1, b2 ↦→ 2, b3 ↦→ 6, b4 ↦→ 4,

ˆκ3 : b1 ↦→ 1, b2 ↦→ 2, b3 ↦→ 4, b4 ↦→ 8, ˆκ4 : b1 ↦→ 1, b2 ↦→ 2, b3 ↦→ 8, b4 ↦→ 4,

ˆκ5 : b1 ↦→ 1, b2 ↦→ 2, b3 ↦→ 6, b4 ↦→ 7, ˆκ6 : b1 ↦→ 1, b2 ↦→ 2, b3 ↦→ 7, b4 ↦→ 6,

ˆκ7 : b1 ↦→ 1, b2 ↦→ 2, b3 ↦→ 7, b4 ↦→ 8, ˆκ8 : b1 ↦→ 1, b2 ↦→ 2, b3 ↦→ 8, b4 ↦→ 7.

In particular, we observe that #(Γ1, T, κ) = 8. Since the automorphism group of Γ1
is a rank 3 group, this number does not depend on the particular choice of κ. In other
words, Γ1 is T-regular with #(Γ1, T) = 8.
Let us now consider the Shrikhande graph Γ2:

Γ2 : 1 9

2
 10

3

11

4

12
 513
 6

14
 7

15
 8
 16

consider the embedding κ : ∆ ↪→ Γ2 given by κ : a1 ↦→ 1, a2 ↦→ 9. The joint neighbors
of 1 and 9 are 10 and 16, respectively. These two vertices are connected by an edge.
Hence there are exactly two extensions of κ along ι, namely

ˆκ1 : b1 ↦→ 1, b2 ↦→ 9, b3 ↦→ 10, b4 ↦→ 16, ˆκ2 : b1 ↦→ 1, b2 ↦→ 9, b3 ↦→ 16, b4 ↦→ 10.

Thus, we have that #(Γ2, T, κ) = 2. However, if we consider κ
′ : ∆ ↪→ Γ2 given by
κ
′ : a1 ↦→ 1, a2 ↦→ 5, then the two joint neighbors 3 and 7 of 1 and 5 are not connected
by an edge in Γ2. Consequently, there is no extension of κ
′ along ι in Γ2. In other
words, #(Γ2, T, κ
′) = 0. It follows that the Shrikhande graph is not T-regular.

Remarks 3.7.

• If T = (∆, ι, Θ) is a graph type of order (0, n), and if Γ is an arbitrary graph,
then Γ is T-regular. In this case #(Γ, T) is equal to the number of embeddings
of Θ into Γ.
• If T = (∆, ι, Θ) is a graph type of order (n, n), and if Γ is an arbitrary graph,
then Γ is T-regular. In this case #(Γ, T) ∈ {0, 1}. It is 1 if Γ has a subgraph
isomorphic to Θ and 0 otherwise.
• If T1 and T2 are isomorphic graph types, then every graph Γ that is T1-regular,
is also T2-regular. Moreover, in this case we have #(Γ, T1) = #(Γ, T2).
• A concept equivalent to T-regularity, but in the category of complete colored
graphs, was introduced and studied by S. Evdokimov and I. Ponomarenko
in [15] in relation with the t-vertex condition for association schemes.

Algebraic Combinatorics, Vol. 4 #5 (2021) 849

Christian Pech

A simple but important observation is:

Lemma 3.8. Let Γ be T-regular for T = (∆, ι, Θ). Then Γ is T-regular, where T :=
(∆, ι, Θ).

Proof. Clear. □

Definition 3.9. Let m ⩽ n be two natural numbers. We say that a graph Γ is

• (=m, =n)-regular if it is T-regular for all graph types T of order (m, n).
• (=m, n)-regular if it is (=m, =l)-regular for all m ⩽ l ⩽ n,
• (m, =n)-regular if it is (=k, =n)-regular for all k ⩽ m,
• (m, n)-regular if it is (=k, n)-regular for all k ⩽ m.

The concept of (m, n)-regularity is a combinatorial approximation of the notion of
m-homogeneity. Recall:

Definition 3.10. A graph Γ is called m-homogeneous if every isomorphism between
induced subgraphs of order at most m extends to an automorphism of Γ. It is called
homogeneous if every isomorphism between ﬁnite induced subgraphs extends to an
automorphism.

It is not hard to see that for every graph Γ of order n we have that m-homogeneity
is equivalent to (m, n)-regularity.

Lemma 3.11. A graph Γ satisﬁes the t-vertex condition if and only if it is (2, t)-regular.

Proof. Clear. □

3.2. Composition of graph types.

Definition 3.12. Let T1 = (∆1, ι1, Θ1) and T2 = (∆2, ι2, Θ2) be graph types, and let
e : ∆2 ↪→ Θ1.
Let Λ be a graph, λ1 : Θ1 ↪→ Λ, λ2 : Θ2 ↪→ Λ such that the following is a pushout
square (see Deﬁnition 2.1):
 Θ2 Λ

∆2 Θ1

λ2

ι2
 e
 λ1 .

Then the graph type (∆1, λ1 ◦ ι1, Λ) is called the free sum of T1 and T2 with respect
to e. It is denoted by T1 ⊕e T2.

Remark 3.13. The following picture illustrates the construction of a free sum of types:

T1 T2 T1 ⊕e T2
 .

In the picture on the left we see T1. In the picture in the middle we see T2, and how
∆2 is embedded by e into Θ1. In the picture on the right we see how Θ1 and Θ2 are
glued together along ∆2, to obtain Λ. Now, ∆1 still naturally embeds into Λ and we
obtain the free sum of the types with respect to e.

Algebraic Combinatorics, Vol. 4 #5 (2021) 850

On highly regular strongly regular graphs

Example 3.14. Let us consider the graph types T1 = (∆1, ι1, Θ1) and T2 =
(∆2, ι2, Θ2) given by the following pictures:

T1 :
 x y

z
 T2 :
 u v

w
 .

Let e : ∆2 ↪→ Θ1 be given by
 e : u ↦→ z, v ↦→ y.

To obtain the free sum of T1 and T2 with respect to e, we have to take the disjoint
union of Θ1 and Θ2, and to identify u with z and v with y. We end up with the graph
Λ in the following picture:
 Λ :
 {x} {y, v}

{z, u} {w}
 .

Finally, we have T1 ⊕e T2 = (∆1, ι, Λ), where ι : ∆1 ↪→ Λ is given by ι : x ↦→ {x}, y ↦→
{y, v}. If we forget about the labelling, then we obtain:

T1 ⊕e T2 : .

3.3. Decomposition of graph types.

Definition 3.15. Let T, T2 be graph types. We say that T is T2-reducible if T ∼=
T1 ⊕e T2 for some T1 ≇ T and for some e.

Remark 3.16. With the notions from above T = (∆, ι, Θ) is T2-reducible if and only
if the set V (Θ) can be decomposed as a disjoint union of subsets M1, M2, and M3,
such that
(1) im(ι) ⊆ M1 ∪ M3,
(2) M2 ̸= ∅
(3) there are no edges in Θ between vertices from M1 and vertices from M2,
(4) T
′
2 := (Θ(M3), ι
′, Θ(M2∪M3)) ∼= T2 (here ι′ denotes the identical embedding).

M2

M3

M1

In this case, we have T1 = (∆, ι, Θ(M1 ∪ M3)) and T ∼= T1 ⊕e T
′
2, where e is the
identical embedding of M3 into M1 ∪ M3.

Remark 3.17. In Example 3.14, T1 ⊕e T2 is T2-reducible. Beware that there are
some degenerate forms of reducibility that we need to take care of: Every graph type
T = (∆, ι, Θ) is T-reducible, since T ∼= T∆ ⊕1∆ T, where T∆ = (∆, 1∆, ∆) (here 1∆
denotes the identity on V (∆)). In general, whenever T ∼= T
′ ⊕e T for some T
′ and
some e, then T
′ ∼= T∆ and e is an isomorphism of ∆ to the base-graph of T
′.

Algebraic Combinatorics, Vol. 4 #5 (2021) 851

Christian Pech

Definition 3.18. A graph type T is called (m, n)-irreducible if whenever T ∼= T1 ⊕e T2
for a graph type T1 and a graph type T2, where T2 is of order (k, l) with k ⩽ m and
l ⩽ n, then we already have T ∼= T1 or T ∼= T2. Otherwise, we call T (m, n)-reducible.

Lemma 3.19. A graph type T is (m, n)-reducible if and only if it is T
′-reducible, for
some graph type T
′ of order (k, l), where k ⩽ m and l ⩽ n, such that T
′ ≇ T.

Proof. Clear. □

Example 3.20. Consider the following graph type of order (1, 4):

x y

u v .

It is (2, 4)-reducible, since

x y

u v ∼=
 x y
 ⊕e
 x′ y′

u v
 .

Moreover, the graph type
 x y

u v

of order (2, 4) is (2, 3)-reducible (and hence also (2, 4)-reducible), because

x y

u v ∼=
 x y

u
 ⊕e
 x′ y′

v
 .

In both examples, e : x′ ↦→ x, y′ ↦→ y.

In the following it is our goal to link the concept of (m, n)-reducibility to classical
graph-theoretical terms.

Definition 3.21. Let T = (∆, ι, Θ) be a graph type. Let S ⊆ V (Θ) be the image of ι.
Then we deﬁne the enveloping graph of T to be the graph with vertex set V (Θ) and
with edge set E(Θ) ∪ (S
2). The enveloping graph of T will be denoted by Env(T).

Example 3.22.
 T : Env(T) :

Recall that a graph Γ is called l-decomposable if there exists an l-element set of
vertices whose deletion makes the graph disconnected. Moreover, Γ is called (n + 1)-
connected if it is l-indecomposable, for all l ∈ {0, . . . , n}. Note that our deﬁnition of
(n + 1)-connectedness slightly deviates from the classical one (cf. e.g. [23, p. 45]). In
particular, the usual deﬁnition allows a graph of order n to be n − 1-connected, at
most. Of course, such highly connected graphs are exactly the complete graphs. For

Algebraic Combinatorics, Vol. 4 #5 (2021) 852

On highly regular strongly regular graphs

technical convenience, in this paper the complete graphs are k-connected for every
k ∈ N.

Lemma 3.23. A graph type T = (∆, ι, Θ) of order (m1, n + 1) is (m2, n)-irreducible if
and only if Env(T) is (m2 + 1)-connected.

Proof. “⇐:” Suppose that T = (∆, ι, Θ) is (m2, n)-reducible. That is, T is T
′-reducible
for some graph type T
′ of order (k, l), where k ⩽ m2 and l ⩽ n, such that T
′ ≇ T (see
Lemma 3.19). Let us ﬁx such a graph type T
′. Then, as described in Remark 3.16,
we may decompose V (Θ) into a disjoint union of subsets M1, M2, M3, such that
im(ι) ⊆ M1 ∪ M3, M2 ̸= ∅, there are no edges in Θ between vertices from M1
and M2, and such that T
′ ∼= T
′′ := (Θ(M3), ι
′′, Θ(M2 ∪ M3)), where ι′′ is the identical
embedding. Since |M1|+|M2|+|M3| = |V (Θ)| = n+1 and since |M2|+|M3| = l < n+1,
we conclude that M1 is non-empty.
Now we observe that in Env(T) there are still no edges between vertices from M1
and vertices from M2, since only edges between vertices in im(ι) ⊆ M1 ∪M3 are added
in the course of the construction of Env(T). Thus, removing the k vertices of M3 from
Env(T) makes the remainder disconnected. It follows that Env(T) is k-decomposable.
Consequently, Env(T) is not (m2 + 1)-connected.
“⇒:” Suppose that ˆΘ := Env(T) is not (m2 + 1)-connected. Then there exists some
k ⩽ m2 such that ˆΘ is k-decomposable. Thus, there exists pairwise disjoint subsets
M1, M2, M3 of V ( ˆΘ), such that M1 ∪ M2 ∪ M3 = V ( ˆΘ), M1, M2 ̸= ∅, |M3| = k,
and such that there are no edges in ˆΘ between vertices from M1 and vertices from
M2. Thus, if M ⊆ V (Θ) denotes the image of ι, then we have M ⊆ M1 ∪ M3 or
M ⊆ M2 ∪ M3. Without loss of generality assume that M ⊆ M1 ∪ M3. Then, with
T
′ = (Θ(M3), ι
′, Θ(M2 ∪ M3)) (where ι′ is the identical embedding), we obtain that T
is T
′-reducible (see Remark 3.16). By construction we have that T
′ is of order (k, l),
where l = |M2 ∪ M3| ⩽ n. Thus T
′ ≇ T. Consequently, T is (m2, n)-reducible (see
Lemma 3.19). □

Example 3.24. The only 3-connected graph of order 4 is the complete graph K4.
Thus, the only (2, 3)-irreducible graph types of order (2, 4) are:

.

3.4. The dominance quasiorder of graph types.

Definition 3.25. Let T1 = (∆1, ι1, Θ1), T2 = (∆2, ι2, Θ2) be graph types. Then we
deﬁne T1 ≼ T2 (T2 dominates T1) if there exists a morphism (f, g) : T2 → T1 such
that f : ∆2 → ∆1 is an isomorphism and such that g : Θ2 → Θ1 is surjective on
vertices. If, in addition, g is not an isomorphism, then we write T1 ≺ T2.

Lemma 3.26. The relation ≼ deﬁnes a quasiorder on graph types. For ﬁnite graph
types T1, T2 we have T1 ∼= T2 if and only if T1 ≼ T2 and T2 ≼ T1.

Proof. Clear. □

Example 3.27. In the picture below the order diagram of the domination quasiorder
of all graph types of order (2, t) for 2 ⩽ t ⩽ 4 with base graph ∆ isomorphic to K2
can be found (in this diagram, a graph type T2 dominates a graph type T1 iﬀ T2 can

Algebraic Combinatorics, Vol. 4 #5 (2021) 853

Christian Pech

be reached by an upwards-sloped path starting from T1).

Two typical examples of covering pairs in this diagram are given below together
with the morphisms mapping the dominating types to the dominated ones (indicated
by arrows ↦→). Each time, the two arrows between the black vertices determine the
isomorphism f between the base graphs and all four arrows together determine the
surjective homomorphism g between the underlying graphs of the types.

3.5. The type counting lemma. Now all preparations are made so that we can
come to the central auxiliary result of this paper from which all other results depend
crucially. It is the place where algebraic graph theory meets category theory. Its proof
critically depends on the universal property of amalgamated free sums.

Lemma 3.28 (Type counting lemma). Given a graph Γ and graph types T1 =
(∆1, ι1, Θ1) and T2 = (∆2, ι2, Θ2). Let e : ∆2 ↪→ Θ1 be an embedding. Then Γ is
T1 ⊕e T2-regular if

(1) Γ is T1-regular,
(2) Γ is T2-regular, and
(3) Γ is T-regular for every T ≺ T1 ⊕e T2.

Before coming to the proof of the type counting lemma, we need to prepare a few
tools:

Definition 3.29. Let Θ and Γ be graphs, and let h : Θ → Γ be a graph homomorphism.
By Θ/h we denote the graph whose vertex set is V (Θ)/ker h and whose edge set is

Algebraic Combinatorics, Vol. 4 #5 (2021) 854

On highly regular strongly regular graphs

given by

E(Θ/h) := {{M1, M2} | M1, M2 ∈ V (Θ)/h,

{h(m1), h(m2)} ∈ E(Γ), for some m1 ∈ M1, and m2 ∈ M2}.

Lemma 3.30. Let h : Θ → Γ be a graph homomorphism. Then the natural mapping
χh : V (Θ) → V (Θ/h) deﬁned by χh : v ↦→ [v]ker h is a surjective graph homomorphism
to Θ/h. Moreover, there is a unique graph embedding ˜h from Θ/h to Γ such that
h = ˜h ◦ χh.

Proof. Straightforward. □

Now we are ready to prove the type counting lemma. The reader is invited to study
Example 3.31 in parallel.

Proof of Lemma 3.28. Let us start by ﬁxing some notations. Suppose T1 ⊕e T2 =
(∆1, ι, Θ). Let λ1, λ2 be given such that the following is a pushout square:

Θ2 Θ

∆2 Θ1

λ2

ι2
 e
 λ1

and such that ι = λ1 ◦ ι1.
For every compatible cocone (µ1, µ2) of (e, ι2), let us denote by hµ1,µ2 : Θ → Υ the
unique homomorphism that makes the following diagram commutative:

Υ

Θ2 Θ

∆2 Θ1.

λ2

µ2
hµ1,µ2

ι2
 e
 λ1
 µ1

By Lemma 3.30 we have that every hµ1,µ2 decomposes uniquely into the natural
homomorphism χµ1,µ2 : Θ → Θ/hµ1,µ2 and an embedding ˜hµ1,µ2 : Θ/hµ1,µ2 ↪→ Υ.
Let us deﬁne Tµ1,µ2 := (∆1, χµ1,µ2 ◦ ι, Θ/hµ1,µ2). We claim that if µ1 and µ2 are
embeddings, then Tµ1,µ2 is a graph type, that is, χµ1,µ2 ◦ ι is an embedding. To see
this, observe that
˜hµ1,µ2 ◦ χµ1,µ2 ◦ ι = hµ1,µ2 ◦ ι = hµ1,µ2 ◦ λ1 ◦ ι1 = µ1 ◦ ι1.

Thus, since µ1 ◦ ι1 and ˜hµ1,µ2 are embeddings, it follows that so is χµ1,µ2 ◦ ι. Note that
T1 ⊕e T2 dominates Tµ1,µ2 , since (1∆1, χµ1,µ2 ) : T1 ⊕e T2 → Tµ1,µ2, and since χµ1,µ2
is surjective:
 ∆1 Θ/hµ1,µ2

∆1 Θ.

χµ1,µ2 ◦ι

1∆1
 ι
 χµ1 ,µ2

Let us collect the graph types obtained in this way in a set T :

T := {Tµ1,µ2 | (µ1, µ2) is a compatible cocone of (e, ι2), µ1, µ2 are embeddings}.

Note that in the deﬁnition of T the compatible cocones (µ1, µ2) of (e, ι2) are not
restricted to a ﬁxed codomain Υ. In particular they form a proper class. So we need
to show that T is well-deﬁned. Next we will prove the following claims:
(A) T is a ﬁnite set.

Algebraic Combinatorics, Vol. 4 #5 (2021) 855

Christian Pech

(B) Exactly one element of T , namely Tλ1,λ2 , is isomorphic to T1 ⊕e T2. In par-
ticular, all other elements of T are strictly dominated by T1 ⊕e T2.
About (A): Recall that for every compatible cocone (µ1, µ2) of (e, ι2) we have Tµ1,µ2 =
(∆1, χµ1,µ2 ◦ ι, Θ/hµ1,µ2). Let us analyze Θ/hµ1,µ2 . According to Deﬁnition 3.29 its
vertex set is V (Θ)/ ker hµ1,µ2. Thus, the number of possible quotients Θ/hµ1,µ2 is
bounded from above by Bn · 2(
n
2), where n = |V (Θ)| and where Bn denotes the n-th
Bell number. Since χµ1,µ2 ◦ ι : ∆1 → Θ/hµ1,µ2 is an embedding, it is in particular a
function. Thus, the cardinality of T can be estimated from above by Bn · 2(n
2) · nm,
where m = |V (∆1)|.
About (B): First we note that Tλ1,λ2 ∈ T , since λ1 and λ2 are embeddings and
since (λ1, λ2) is a limiting cocone for (e, ι2). Clearly, hλ1,λ2 = 1Θ. So ker hλ1,λ2 is the
equality relation and Θ/hλ1,λ2 is obtained from Θ by renaming each vertex v to the
singleton class {v} = [v]ker hλ1 ,λ2 . In particular, χλ1,λ2 : Θ → Θ/hλ1,λ2 is an isomor-
phism. Thus (1∆1, χλ1,λ2) : T1 ⊕e T2 → Tλ1,λ2 is an isomorphism, too. It remains to
show that Tλ1,λ2 is the only element of T that is isomorphic to T1 ⊕e T2: Suppose
that Tµ1,µ2 = (∆1, χµ1,µ2 ◦ ι, Θ/hµ1,µ2 ) is an element of T isomorphic to T1 ⊕e T2.
Then in particular, Θ/hµ1,µ2 is isomorphic to Θ. Since |V (Θ/hµ1,µ2 )| = |V (Θ)|, we
have that ker hµ1,µ2 is the equality relation. Thus V (Θ/hλ1,λ2) = V (Θ/hµ1,µ2), and
χλ1,λ2 and χµ1,µ2 coincide as functions. Moreover, since |E(Θ)| = |E(Θ/hµ1,µ2)|, we
obtain, that χµ1,µ2 is an isomorphism. Consequently, Tµ1,µ2 = Tλ1,λ2 , which proves
Claim (B).
At this point it is essential to notice that T only depends on T1, T2, and e, but not
on Γ. Let us ﬁx an embedding κ : ∆1 → Γ. Our goal is to determine #(Γ, T1 ⊕e T2, κ).
However, we are not able to do so directly. Instead we are going to prove the following
identity:

(2) #(Γ, T1) · #(Γ, T2) = ∑

T∈T #(Γ, T, κ).

Note now that by the assumption and by (B), we have that Γ is T-regular for all
graph types T ∈ T ∖ {Tλ1,λ2}. Thus, from (2) we obtain that

#(Γ, T1 ⊕e T2, κ) = #(Γ, Tλ1,λ2, κ) = #(Γ, T1) · #(Γ, T2) − ∑

T∈T ∖{Tλ1,λ2 }
#(Γ, T),

which obviously does not depend on κ. Thus, once we show identity (2), then we are
done. The rest of the proof is dedicated to the task of showing (2).
Let µ1 : Θ1 ↪→ Γ, µ2 : Θ2 ↪→ Γ. Then (µ1, µ2) is called a κ-compatible pair if
(a) µ1 extends κ along ι1 (i.e. κ = µ1 ◦ ι1),
(b) µ2 extends µ1 ◦ e along ι2 (i.e. µ1 ◦ e = µ2 ◦ ι2).
Clearly, every κ-compatible pair is a compatible cocone for (e, ι2). Thus, to every
κ-compatible pair (µ1, µ2) we can associate the graph type Tµ1,µ2 from T . Let us
deﬁne
 Pκ := {(µ1, µ2) | (µ1, µ2) is a κ-compatible pair},

Pκ,T := {(µ1, µ2) | (µ1, µ2) ∈ Pκ, Tµ1,µ2 = T}.

Then, by deﬁnition we have

(3) #(Γ, T1) · #(Γ, T2) = |Pκ| = ∑

T∈T |Pκ,T|.

In the following we are going to show:

(4) ∀T ∈ T : |Pκ,T| = #(Γ, T, κ).

Algebraic Combinatorics, Vol. 4 #5 (2021) 856

On highly regular strongly regular graphs

Let T ∈ T . Then there exists a compatible cocone (ν1, ν2) of (e, ι2), such that T =
Tν1,ν2 = (∆1, χν1,ν2 ◦ ι, Θ/hν1,ν2 ) and such that both, ν1 and ν2 are embeddings.
Let ˆκ : Θ/hν1,ν2 ↪→ Γ be an extension of κ along χν1,ν2 ◦ ι (i.e. κ = ˆκ ◦ χν1,ν2 ◦ ι).
Deﬁne µ
[ˆκ]
1 : Θ1 ↪→ Γ by µ
[ˆκ]
1 := ˆκ◦χν1,ν2 ◦λ1 and µ
[ˆκ]
2 : Θ2 ↪→ Γ by µ
[ˆκ]
2 := ˆκ◦χν1,ν2 ◦λ2.

Θ2 Θ Θ/hν1,ν2 Γ

∆2 Θ1 ∆1.

µ
[ˆκ]
2

λ2 χν1 ,ν2 ˆκ

e

ι2 µ
[ˆκ]
1
λ1 κ

ι1

We claim that (µ
[ˆκ]
1 , µ
[ˆκ]
2 ) is a κ-compatible pair. First we note that µ
[ˆκ]
1 is an embed-
ding, since ˜hν1,ν2 ◦ (χν1,ν2 ◦ λ1) = ν1 is an embedding and µ
[ˆκ]
2 is an embedding, since
˜hν1,ν2 ◦ (χν1,ν2 ◦ λ2) = ν2 is an embedding. Next we compute that

µ
[ˆκ]
1 ◦ ι1 = ˆκ ◦ χν1,ν2 ◦ λ1 ◦ ι1 = ˆκ ◦ χν1,ν2 ◦ ι = κ,

thus µ
[ˆκ]
1 extends κ along ι1, and

µ
[ˆκ]
1 ◦ e = ˆκ ◦ χν1,ν2 ◦ λ1 ◦ e = ˆκ ◦ χν1,ν2 ◦ λ2 ◦ ι2 = µ
[ˆκ]
2 ◦ ι2,

thus µ
[ˆκ]
2 extends µ
[ˆκ]
1 ◦ e along ι2 and the claim is proved.
The next step is to show that the assignment ˆκ ↦→ (µ
[ˆκ]
1 , µ
[ˆκ]
2 ) is a bijection:
“injectivity”: Let ˆκ1 and ˆκ2 be extensions of κ along χν1,ν2 ◦ ι and suppose that
(µ
[ˆκ1]
1 , µ
[ˆκ1]
2 ) = (µ
[ˆκ2]
1 , µ
[ˆκ2]
2 ). Note that ˆκ1 ◦ χν1,ν2 is the unique mediating morphism
from the limiting cocone (λ1, λ2) to (µ
[ˆκ1]
1 , µ
[ˆκ1]
2 ), and that ˆκ2 ◦ χν1,ν2 is the unique
mediating morphism from (λ1, λ2) to (µ
[ˆκ2]
1 , µ
[ˆκ2]
2 ). Since (µ
[ˆκ1]
1 , µ
[ˆκ1]
2 ) = (µ
[ˆκ2]
1 , µ
[ˆκ2]
2 ),
we have ˆκ1 ◦ χν1,ν2 = ˆκ2 ◦ χν1,ν2 . Since χν1,ν2 is surjective, we conclude ˆκ1 = ˆκ2.
“surjectivity”: Let (µ1, µ2) be any κ-compatible pair such that Tµ1,µ2 = T = Tν1,ν2 .
In particular, Θ/hµ1,µ2 = Θ/hν1,ν2, and thus also χµ1,µ2 = χν1,ν2 . We claim that
˜hµ1,µ2 is an extension of κ along χν1,ν2 ◦ ι. Indeed, we may compute

˜hµ1,µ2 ◦ χν1,ν2 ◦ ι = ˜hµ1,µ2 ◦ χµ1,µ2 ◦ ι = hµ1,µ2 ◦ ι = hµ1,µ2 ◦ λ1 ◦ ι1 = µ1 ◦ ι1 = κ.

It remains to show that ˜hµ1,µ2 is really a preimage of (µ1, µ2) under our correspon-
dence. For this we compute

˜hµ1,µ2 ◦ χν1,ν2 ◦ λ1 = ˜hµ1,µ2 ◦ χµ1,µ2 ◦ λ1 = hµ1,µ2 ◦ λ1 = µ1,

and
 ˜hµ1,µ2 ◦ χν1,ν2 ◦ λ2 = ˜hµ1,µ2 ◦ χµ1,µ2 ◦ λ2 = hµ1,µ2 ◦ λ2 = µ2.

This ﬁnishes the proof of (4). Now, identity (2) is a direct consequence of (3) and (4).
□

The type counting lemma is the technical backbone of all further results in this
paper. Alas, while the language of category theory used in the proof is convenient for
assuring correctness, it is not ideal to illustrate the combinatorial intuitions behind
the proof. To amend this situation, we elaborate on an extended example:

Example 3.31. Suppose, we are given a (2, 4)-regular graph Γ. In other words, Γ is
strongly regular and satisﬁes the 4-vertex condition. Let us illustrate the idea behind
the proof of the type counting lemma by analyzing the graph type T = (∆, ι, Θ)

Algebraic Combinatorics, Vol. 4 #5 (2021) 857

Christian Pech

given by the following picture (here ∆ = Θ({x, y}), and ι : ∆ ↪→ Θ is the identical
embedding):
 T :
 x y

u v
 w
 .

Our ﬁrst observation is that T is (2, 4)-reducible. In particular we have T ∼= T1 ⊕e T2,
where T1 = (∆, ι1, Θ1) and T2 = (∆2, ι2, Θ2) are given by:

T1 :
 x y

u T2 : u v
 w

y

and where e : ∆2 ↪→ Θ1 is the identical embedding. Since Γ is (2, 4)-regular, it is T1-
and T2-regular.
Let (µ1, µ2) be an arbitrary compatible cocone of (e, ι2), where µi : Θi ↪→ Υ (i ∈
{1, 2}), say
 µ1 : x ↦→ a, y ↦→ b, u ↦→ c,

µ2 : y ↦→ b, u ↦→ c, v ↦→ d, w ↦→ o, where a, b, c, d, o ∈ V (Υ).

Then the unique mediating morphism hµ1,µ2 is given by

hµ1,µ2 : x ↦→ a, y ↦→ b, u ↦→ c, v ↦→ d, w ↦→ o.

In the following we list all possibilities what the subgraph of Υ induced by {a, b, c, d, o}
might look like (depending on Υ and on (µ1, µ2)). This list is obtained by constructing
all graphs vertex labeled by {a, b, c, d, o} in such a way that every vertex has at least
one label (though, it may have more than one label) and such that every label is used
exactly once, subject to the condition that the above given functions µ1 and µ2 deﬁne
graph-embeddings. In our case this means that the vertices labeled by elements of
{a, b, c} induce K3 and those labeled by elements from {b, c, d, o} induce K4:

(1) :
 a b

c d
 o
 (2) :
 a b

c o
 d
 (3) :
 a, o
 c

d
 b

(4) :
 c
 o

a, d
 b
 (5) :
 a b

c d
 o
 (6) :
 a b
 c

d

o .

Algebraic Combinatorics, Vol. 4 #5 (2021) 858

On highly regular strongly regular graphs

Now we are ready to construct the set T mentioned in the proof of the type counting
Lemma. In cases (1) and (2) we obtain

T
(1) := Tµ1,µ2 :
 {x} {y}

{u} {v}
 {w}
 ˜hµ1,µ2 :
 



{x} ↦→ a,
{y} ↦→ b,
{u} ↦→ c,
{v} ↦→ d,
{w} ↦→ o.

In case (3) we obtain

T
(2) := Tµ1,µ2 :
 {x, w}
 {u}

{v}
 {y}
 ˜hµ1,µ2 :
 



{x, w} ↦→ a(= o),
{y} ↦→ b,
{u} ↦→ c,
{v} ↦→ d.

In case (4) we obtain

T
(3) := Tµ1,µ2 ∼= T
(2) :
 {u}
 {w}

{x, v}

{y}
 ˜hµ1,µ2 :
 




{x, v} ↦→ a(= d),
{y} ↦→ b,
{u} ↦→ c,
{w} ↦→ o.

In case (5) we obtain

T
(4) := Tµ1,µ2 ∼= T :
 {x} {y}

{u} {v}
 {w}
 ˜hµ1,µ2 :
 




{x} ↦→ a,
{y} ↦→ b,
{u} ↦→ c,
{v} ↦→ d,
{w} ↦→ o.

In case (6) we obtain

T
(5) := Tµ1,µ2 :
 {x} {y}

{u}

{v}

{w} ˜hµ1,µ2 :
 



{x} ↦→ a,
{y} ↦→ b,
{u} ↦→ c,
{v} ↦→ d,
{w} ↦→ o.

To sum up, we have
 T = {T
(1), T
(2), T
(3), T
(4), T
(5)}.

Algebraic Combinatorics, Vol. 4 #5 (2021) 859

Christian Pech

Let us ﬁx an embedding κ : ∆ ↪→ Γ. Then the set Pκ of all κ-compatible pairs is
given by

Pκ = {(µ1, µ2) | µ1 extends κ along ι1 and µ2 extends µ1 ◦ e along ι2}.

Thus, we have
 #(Γ, T1) · #(Γ, T2) = |Pκ| =
 5∑

i=1 #(Γ, T
(i), κ).

If we suppose that Γ is T
(1)-, T
(2)-, and T
(5)-regular, then, taking into account that
T
(2) ∼= T
(3), we obtain

#(Γ, T
(4), κ) = #(Γ, T1) · #(Γ, T2) − #(Γ, T
(1)) − 2 · #(Γ, T
(2)) − #(Γ, T
(5)).

Finally, observing that #(Γ, T, κ) = #(Γ, T
(4), κ). we arrive at

#(Γ, T, κ) = #(Γ, T1) · #(Γ, T2) − #(Γ, T
(1)) − 2 · #(Γ, T
(2)) − #(Γ, T
(5)).

As this does not depend on κ, we conclude that Γ is T-regular.

Remark 3.32. The formulation of the type counting Lemma is not as strong as it
could be. In particular, when analyzing the proof it becomes clear that the third
condition can be weakened. It is not necessary that Γ is T-regular for all graph types
T strictly dominated by T1 ⊕e T2. Instead it is suﬃcient to claim that Γ is T-regular
for all those graph types T for which there exists a morphism (f, g) : T1 ⊕e T2 ↠ T
such that

(1) f is an isomorphism,
(2) g is surjective and not an isomorphism,
(3) g ◦ λ1 and g ◦ λ2 are embeddings,

where (λ1, λ2) is a limiting cocone for (e, ι2).

Example 3.33. The type counting lemma is a qualitative statement about regularities.
It makes no claim about #(Γ, T1 ⊕e T2, κ), only that it is independent of κ. However,
when studying its proof, it becomes clear that there is also a quantitative dimension.
While it is not the topic of this paper, let us have a little look into this aspect, just
to get a taste. We consider the problem of counting subgraphs in strongly regular
graphs. In N. Kriger’s D.Phil thesis [38], following the spirit of the paper [24] by
M.D. Hestenes and D.G. Higman, formulae for counting four-vertex subgraphs in
strongly regular graphs are given and proved. Following Kriger’s notation, by F (Θ)
the number of induced subgraphs of Γ isomorphic to Θ is denoted. In general, if we
deﬁne TΘ := (∅, ι, Θ), then #(Γ, TΘ) is equal to the number of embeddings of Θ into
Γ. Thus we have F (Θ) = #(Γ, TΘ)/| Aut(Θ)|. Let Γ be a strongly regular graph with
parameters (v, k, λ, µ). That is, we know a priori that

#(Γ, ) = v, #(Γ, ) = k #(Γ, ) = λ #(Γ, ) = µ.

Algebraic Combinatorics, Vol. 4 #5 (2021) 860

On highly regular strongly regular graphs

In order to save some space, in the following, instead of #(Γ, T) we will write just
#(T).

#( ) = #( ) · #( ) − #( ) − #( ) = v − k − 1 =: ¯k

#( ) = #( ) · #( ) = vk

#( ) = #( ) · #( ) = v(v − k − 1) = v¯k

#( ) = #( ) · #( ) − #( ) = k − µ

#( ) = #( ) · #( ) − #( ) − #( ) = k − λ − 1

#( ) = #( ) · #( ) = vkλ

#( ) = #( ) · #( ) = v¯kµ

#( ) = #( ) · #( ) − #( ) = ¯k − k + λ + 1 =: ¯µ

#( ) = #( ) · #( ) = vk ¯µ

#( ) = #( ) · #( ) − #( ) − #( ) = ¯k − 1 − k + µ =: ¯λ

#( ) = #( ) · #( ) = v¯k¯λ

#( ) = #( ) · #( ) − #( ) − #( ) = vkλ(λ − 1) − #( )

#( ) = #( ) · #( ) − #( ) − #( ) = v¯kµ(µ − 1) − vkλ(λ − 1) + #( )

#( ) = #( ) · #( ) − #( ) = v¯kµλ − vkλ(λ − 1) + #( )

#( ) = #( ) · #( ) − #( ) = vk ¯µµ − v¯kµλ + vkλ(λ − 1) − #( )

#( ) = #( ) · #( ) − #( ) = vk ¯µk − 2vk ¯µµ + v¯kµλ − vkλ(λ − 1) + #( )

#( ) = #( ) · #( ) − #( ) − #( )

= v¯kµ(k − 2λ − 2) + vkλ(λ − 1) − #( )

#( ) = #( ) · #( ) − #( ) = vk ¯µλ − v¯kµλ + vkλ(λ − 1) − #( )

#( ) = #( ) · #( ) − #( ) = v¯k¯λµ − v¯kµ(k − 2λ − 2) − vkλ(λ − 1) + #( )

#( ) = #( ) · #( ) − #( )

= v¯k¯λ(k − 2µ) + v¯kµ(k − 2λ − 2) + vkλ(λ − 1) − #( )

#( ) = #( ) · #( ) − #( ) − #( )

= v¯k¯λ(¯λ − 1 − k + 2µ) − v¯kµ(k − 2λ − 2) − vkλ(λ − 1) + #( )

Note above how the counting of embeddings of 4-vertex graphs into Γ may be reduced
to counting #( ).

3.6. Criteria for (m, n)-regularity. The proofs of the following propositions
make use of a very basic induction principle for ﬁnite posets:

Lemma 3.34. Let (P, ⩽) be a ﬁnite partially ordered set and let B ⊆ P . If

(5) ∀p ∈ P : ({q ∈ P | q < p} ⊆ B ⇒ p ∈ B),

then we already have that B is equal to P .

Proof. Suppose that (5) holds for B, but that B ̸= P . Let x be a minimal element of
P ∖ B in (P, ⩽) (this exists because P is ﬁnite). Then for all y < x we have y ∈ B.
Thus, by (5), we also have x ∈ B, a contradiction. □

Algebraic Combinatorics, Vol. 4 #5 (2021) 861

Christian Pech

Proposition 3.35. Let Γ be an (m, m)-regular graph. Then, Γ is (m, n)-regular if and
only if it is (=m, n)-regular.

Proof. By deﬁnition, from (m, n)-regularity follows (=m, n)-regularity.
Suppose that Γ is (=m, n)-regular and (m, m)-regular. Let M be a transversal of
the isomorphism classes of graph types of order (k, l) for k ⩽ m and for l ⩽ n. Then,
by Lemma 3.4, (M, ≼) is a ﬁnite poset. Moreover, whenever T ∈ M and T
′ ≼ T, then
T
′ is isomorphic to an element of M.
Let T = (∆, ι, Θ) ∈ M be of order (k, l). Suppose that for all T
′ ≺ T the graph Γ is
T
′-regular. If l ⩽ m, then Γ is T-regular, by assumption. So suppose that m < l ⩽ n.
Let ˆ∆ be an induced subgraph of order m of Θ that contains the image of ι, and let ˆι
be the identical embedding of ˆ∆ into Θ. Then T1 := (∆, ι, ˆ∆) is a graph type of order
(k, m), and T2 := ( ˆ∆, ˆι, Θ) is a graph type of order (m, l). Moreover, T ∼= T1 ⊕ˆι T2. By
the assumptions, we have that Γ is T1- and T2-regular. Hence, by the type counting
lemma, we conclude that Γ is T-regular.
By the arguments above and by Lemma 3.34, Γ is T-regular for all graph types T
from M. In other words, Γ is (m, n)-regular. □

Note that a graph is (2, 2)-regular if and only if it is regular. Thus, the previous
proposition generalizes a classic result by A.V. Ivanov:

Theorem 3.36 (A.V. Ivanov [29, Proposition 2.1]). Let Γ be a regular graph. Then Γ
satisﬁes the t-vertex condition if and only if it is (=2, t)-regular.

Definition 3.37. A graph Γ = (V, E) is called k-isoregular if for every subset X ⊆ V
with |X| ⩽ k the number of vertices v /∈ X that are adjacent to all elements of X does
not depend on X but only on the isomorphism type of the subgraph of Γ induced by X.

Proposition 3.38. Let Γ be a graph and let k > 0 be a natural number. Then the
following are equivalent:

(1) Γ is k-isoregular,
(2) Γ is (=l, =l + 1)-regular for every 1 ⩽ l ⩽ k,
(3) Γ is (k, k + 1)-regular.

Proof. “(1)⇒(2):” Let l ∈ {1, . . . , k}, and let M be a transversal of the isomorphism
classes of graph types of order (l, m) where m ∈ {l, l + 1}. Without loss of generality
we may assume for every graph type T = (∆, ι, Θ) ∈ M that ι is the identical
embedding (i.e. ∆ is an induced subgraph of Θ). By Lemma 3.4, (M, ≼) is a ﬁnite
poset. Moreover, for every T ∈ M of order (l, m) and for every T
′ ≺ T we have that
the order of T
′ is (l, n) for some l ⩽ n ⩽ m; hence there exists a unique T
′′ ∈ M such
that T
′ ∼= T
′′.
In the following we show that Γ is T-regular, for all T ∈ M. Let T = (∆, ι, Θ)
be an element of M. Moreover, suppose that for all T
′ ≺ T from M the graph Γ is
T
′-regular. If the order of T is (l, l), then Γ is T-regular. So suppose that T has order
(l, l + 1). Let v be the unique vertex of Θ that is not in V (∆). If v has valency l in
Θ, then Γ is T-regular, because Γ is k-isoregular. So, suppose that the valency of v
in Θ is equal to m < l. Let ˆ∆ be the subgraph of ∆ induced by the neighbors of v,
let ˆΘ be the subgraph of Θ induced by the vertices of ˆ∆ together with v itself, and
let ˆι : ˆ∆ ↪→ ˆΘ be the identical embedding. Then T1 := (∆, 1∆, ∆) and T2 := ( ˆ∆, ˆι, ˆΘ)
are graph types. Moreover, T ∼= T1 ⊕e T2, where e denotes the identical embedding

Algebraic Combinatorics, Vol. 4 #5 (2021) 862

On highly regular strongly regular graphs

of ˆ∆ into ∆. v

ˆ∆
 ∆
 ∆ Θ V (Θ) = V (∆) ∪ {v}

ˆ∆ ˆΘ V ( ˆΘ) = V ( ˆ∆) ∪ {v}.

ι
=

ˆι
=

e = =

Then T1 is of order (l, l) thus, Γ is T1-regular. Moreover, T2 is of order (m, m + 1)
and the T2-regularity of Γ follows from the k-isoregularity of Γ. Now, from the type
counting lemma it follows that Γ is T-regular. Finally, from Lemma 3.34 it follows
that Γ is regular for all types from M. In particular, Γ is (=l, =l + 1)-regular.
“(2)⇒(3):” We show that Γ is (l, l + 1)-regular for all l ∈ {1, . . . , k}. We proceed
by induction on l. For the induction base we note that Γ is (1, 2)-regular if and
only if it is (=1, =1), and (=1, =2)-regular. The ﬁrst regularity condition is trivially
fulﬁlled and the (=1, =2)-regularity is given by assumption. Suppose, we know that
Γ is (l, l + 1)-regular and (=l + 1, =l + 2)-regular, for some 1 ⩽ l ⩽ k − 1. Then
from the (l, l + 1)-regularity follows immediately the (l + 1, l + 1)-regularity (indeed,
a graph is (l + 1, l + 1)-regular iﬀ it is (l, l + 1)-regular and (=l + 1, =l + 1)-regular;
however, trivially, every graph is (=l + 1, =l + 1)-regular). Moreover, we have that Γ is
(=l+1, l+2)-regular, because Γ is (=l+1, =l+1)-regular and Γ is (=l+1, =l+2)-regular.
Hence, from Proposition 3.35, it follows that Γ is (l + 1, l + 2)-regular.
“(3)⇒(1):” k-isoregularity of Γ follows immediately from the (k, k + 1)-regularity.
□

The following criterion by S. Reichard characterizes, when a k-isoregular graph
with the (t − 1)-vertex condition satisﬁes the t-vertex condition:

Theorem 3.39 ([49, Theorem 3]). Let Γ be a k-isoregular graph that satisﬁes the
(t − 1)-vertex condition for t > 3. Then, in order to verify the t-vertex condition, it
suﬃces to test the T-regularity for graph types T = (∆, ι, Θ) of order (2, t) with the
property that all vertices of Θ that are not in the image of ι have valency ⩾ k +1 in Θ.

Our next goal is to generalize this result:

Proposition 3.40. Let Γ be an (m, t)-regular graph. Let M be a set of graph types
and suppose that Γ is T-regular, for all T ∈ M. Then, in order to verify the (m, t+1)-
regularity of Γ it suﬃces to test the T-regularity for graph types of order (m, t + 1)
that are ̂T-irreducible for all ̂T ∈ M.

Proof. Let T be a transversal of the isomorphism classes of graph types of order
(m, t + 1). Then, by Lemma 3.4, (T , ≼) is a ﬁnite poset. Moreover, whenever T ∈ T
and T
′ ≼ T is a graph type of order (m, t+1), then T
′ is isomorphic to an element of T .
We will use the induction principle from Lemma 3.34 on (T , ≼): Let T = (∆, ι, Θ) ∈
T and suppose that Γ is T
′-regular for all T
′ ∈ T with T
′ ≺ T. Note that for every
graph type T
′′ ≺ T we either have that T
′′ is isomorphic to an element of T or it has
order (m, l) for some l < t + 1. In both cases we conclude that Γ is T
′′-regular.
If T is ̂T-irreducible for all ̂T ∈ M, then Γ is T-regular, by assumption. So suppose
that there exists a ̂T ∈ M, such that T is ̂T-reducible. Then T ∼= T1 ⊕e ̂T for some
graph type T1 ≇ T. But then the order of T1 is (m, l), for some l < t + 1. Hence,

Algebraic Combinatorics, Vol. 4 #5 (2021) 863

Christian Pech

by assumption Γ is T1-regular and ̂T-regular. By the type counting lemma we obtain
that Γ is T-regular.
Now, it remains to invoke Lemma 3.34, to obtain that Γ is regular for all types from
T . Consequently, Γ is (=m, =t+1)-regular. By assumption, Γ is (m, t)- and in particu-
lar (m, m)-regular. Hence, by Proposition 3.35, we have that Γ is (m, t+1)-regular. □

Proposition 3.41. Let Γ be a graph. Then Γ is (m, n + 1)-regular if and only if Γ
is (m, n)-regular and it is T-regular for every (m, n)-irreducible graph type T of order
(m, n + 1).

Proof. “⇒:” This is clear.
“⇐:” Let M be a transversal of the isomorphism classes of graph types of order
(k, l), where k ⩽ m and where l ⩽ n. By assumption, Γ is regular for all graph
types from M. By Proposition 3.40, in order to show that Γ is (m, n + 1)-regular it
suﬃces to show that Γ is T-regular, for all graph types T of order (m, n + 1) that are
̂T-irreducible, for all ̂T ∈ M.
By Lemma 3.19 we have that a graph type T of order (m, n + 1) is (m, n)-reducible
if and only if it is ̂T-reducible for some ̂T ∈ M. In particular, if T is (m, n)-irreducible,
then it is ̂T-irreducible for all ̂T ∈ M. This ﬁnishes the proof. □

Corollary 3.42. A graph Γ is (m, n + 1)-regular if and only if it is (m, n)-regular
and it is T-regular for all graph types T of order (m, n + 1) for which Env(T) is
(m + 1)-connected.

Proof. This follows immediatelyfrom Proposition 3.41 together with Lemma 3.23. □

Definition 3.43. Let Γ be a graph and let u ∈ V (Γ). Then with Γ1(u) we denote
the subgraph of Γ induced by the neighbors of u. Moreover, with Γ2(u) we denote the
subgraph of Γ induced by the non-neighbors of u (except u itself). Γ1(u) and Γ2(u) are
called the ﬁrst and the second subconstituent of Γ with respect to u, respectively.

The following proposition relates the regularities of a graph with the regularities of
its subconstituents. This is used later on to identify a new class of graphs satisfying
the 6-vertex condition:

Proposition 3.44. Let Γ be an (m, n)-regular graph where m ⩾ 1, and let u ∈ V (Γ).
Then Γ1(u) and Γ2(u) are both (m − 1, n − 1)-regular.

Proof. About Γ1(u): Let T = (∆, ι, Θ) be a graph type of order (r, s) where r ⩽ m − 1
and s ⩽ n − 1. Let ∆′ := ∆ + {x} and Θ′ := Θ + {y} be graphs obtained from ∆
and Θ by adjoining a single new vertex that is connected to vertices of ∆ and of Θ,
respectively. Let ι′ : ∆′ ↪→ Θ′ be deﬁned according to

ι′ : w ↦→
 {ι(w) w ∈ V (∆),
y w = x.

Then T
′ := (∆
′, ι
′, Θ′) is a graph type of order (r+1, s+1). As r+1 ⩽ m and s+1 ⩽ n,
we have that Γ is T
′-regular. Let κ : ∆ ↪→ Γ1(u). Deﬁne κ
′ : ∆′ ↪→ Γ according to

κ
′ : w ↦→
 {κ(w) w ∈ V (∆),
u w = x.

We claim that there is a bijection between set of extensions of κ along ι in Γ1(u) and
the set of extensions of κ
′ along ι′ in Γ:

Algebraic Combinatorics, Vol. 4 #5 (2021) 864

On highly regular strongly regular graphs

Let ˆκ be any extension of κ along ι in Γ1(u). We deﬁne ˆκ
′ : Θ′ ↪→ Γ according to

ˆκ
′ : w ↦→
 {ˆκ(w) w ∈ V (Θ),
u w = y.

Clearly, ˆκ
′ is an extension of κ
′ along ι′ in Γ.
Let on the other hand ˆκ
′ be any extension of κ
′ along ι′ in Γ. Then ˆκ := ˆκ
′↾V (Θ)
is an extension of κ along ι in Γ1(u). This establishes the desired bijection between
extensions of κ along ι in Γ1(u) and extensions of κ
′ along ι′ in Γ. In particular, we
have #(Γ1(u), T, κ) = #(Γ, T
′, κ
′) = #(Γ, T
′). Thus, Γ1(u) is T-regular. As T was
chosen arbitrarily, we conclude that Γ1(u) is (m − 1, n − 1)-regular.
About Γ2(u): From Lemma 3.8 it follows that Γ is (m, n)-regular. Clearly, we have
Γ1(u) = Γ2(u), as the neighbours of u in Γ are exactly the non-neighbors of u in
Γ, and the edges in Γ1(u) are exactly the non-edges in Γ2(u). From the ﬁrst part of
the proof it follows that Γ1(u) is (m − 1, n − 1)-regular. Again using Lemma 3.8 we
conclude that Γ2(u) is (m − 1, n − 1)-regular. □

Remark 3.45. The previous proposition generalizes a result from the folklore of alge-
braic graph theory to the case of (m, n)-regular graphs. Namely, if a graph is (k + 1)-
isoregular, then all its ﬁrst and second subconstituents are k-isoregular. This obser-
vation, together with spectral methods, stands at the center of Gol’fand’s lost proof
that 5-isoregular graphs are homogeneous (see [51, Section 9.2] for a historical account
and for further references).

4. Checking the t-vertex condition

Every graph satisﬁes the 1-vertex condition. A graph satisﬁes the 2-vertex condition if
and only if it is regular. A bit less obvious but rather straightforward is the observation
that a graph satisﬁes the 3-vertex condition if and only if it is strongly regular, i.e. it
is regular and the number of common neighbors of every edge is equal to a constant λ
and the number of common neighbors of every non-edge is equal to a constant µ (the
ﬁrst half of Example 3.33 contains the calculations necessary for a proof that strong
regularity implies the 3-vertex condition). A criterion for the 4-vertex condition is
given by:

Theorem 4.1 (M.D. Hestenes, D.G. Higman [24]). Let Γ be a strongly regular graph.
Then, in order to verify the 4-vertex condition it suﬃces to test the T-regularity for
the following two graph types of order (2, 4):
 .

In our terminology, this is a special case of Corollary 3.42 (m = 2 and n = 3, see
Example 3.24). More generally, we have:

Proposition 4.2. Let Γ be a graph that satisﬁes the t-vertex condition for t ⩾ 3.
Then, in order to verify the (t + 1)-vertex condition it suﬃces to test the T-regularity
for all those graph types T of order (2, t + 1) for which Env(T) is 3-connected.

Proof. This is a special case of Corollary 3.42 (m = 2, n = t). □

In [50, Theorem 4.9] S. Reichard proved that a graph satisfying the 4-vertex con-
dition satisﬁes the 5-vertex condition if and only if it is regular for a list of 16 graph
types. The following proposition reduces the number of graph types to be tested to 10:

Algebraic Combinatorics, Vol. 4 #5 (2021) 865

Christian Pech

Proposition 4.3. Given a graph Γ that fulﬁlls the 4-vertex condition. Then in order
to test whether Γ satisﬁes also the 5-vertex condition it suﬃces to count the graph
types in the table below.

Proof. According to Proposition 4.2, Γ satisﬁes the 5-vertex condition if and only if
it is T-regular for all T such that Env(T) is 3-connected. So we start by constructing
all 3-connected graphs of order 5. This gives us the following three graphs:

.

Next, for each graph Θ from this list we computed the orbits of Aut(Θ) in its action
on edges. Each orbit representative corresponds to a two-vertex subgraph ∆ ∼= K2,
producing a graph type (∆, ι, Θ) (as usual, ι is the identical embedding). This produces
the upper row of graph types. The lower row is obtained by removing the distinguished
edge in each case. Clearly, this produces a transversal of the isomorphism classes of
graph types T of order (2, 5) for which Env(T) is 3-connected. □

5. Point graphs of partial quadrangles

An incidence structure is a triple (P, L , I), where P is a set of points (denoted
by capital Latin letters P, Q, . . .), L is a set of lines (denoted by small Latin letters
l, s, t, . . .), and I ⊆ P × L is an incidence relation. The elements of I are called ﬂags
and the elements of (P × L ) ∖ I are called antiﬂags. A point P is called incident with
a line l if (P, l) is a ﬂag. Slightly abusing the notation we write in this case P ∈ l. Two
distinct ﬂags (P, p) and (Q, q) are called collinear if p = q, and concurrent if P = Q.
Two distinct points P and Q are called collinear if there exists a line l such that (P, l)
and (Q, l) are ﬂags. In this case we say that l goes through P and Q. Dually, we say
that two lines p and q are intersecting each other if there is a point P such that P ∈ p
and P ∈ q.
For every incidence structure, we may deﬁne its point graph. This is a simple graph
which has as vertices the points of the incidence structure such that between two
points there is an edge if and only if the points are collinear.
In the following we restrict our attention to so-called partial linear spaces of order
(s, t) (in the sense of [14, p. 3]):

Definition 5.1. Let s, t ∈ N ∖ {0}. A partial linear space of order (s, t) (short
PLS(s, t)) is an incidence structure (P, L , I) with the following properties:
PLS1. Every line is incident with the same number s + 1 of points.
PLS2. Every point is incident with the same number t + 1 of lines.
PLS3. Through any two distinct points goes at most one line.

If two lines p and q of a partial linear space intersect each other, then we denote
the unique point of intersection by p ∩ q.

Algebraic Combinatorics, Vol. 4 #5 (2021) 866

On highly regular strongly regular graphs

Remark 5.2. Note that in a partial linear space two lines are equal if and only if they
are incident with exactly the same points. Below we will implicitly identify a line in
a partial linear space with the set of points it is incident with. Moreover, a partial
linear space (P, L , I) will be denoted just like (P, L ).

We are interested in partial linear spaces because there are signiﬁcant classes of
them whose point graphs are strongly regular. Two such classes are deﬁned below.
The ﬁrst class of interest consists of the generalized quadrangles as introduced by
J. Tits in [55]:

Definition 5.3. A generalized quadrangle of order (s, t) (abbreviated to GQ(s, t)) is
a partial linear space of order (s, t) with the the following additional property:
GQ1. For every antiﬂag (P, q) there is a unique point Q such that P and Q are
collinear and such that Q ∈ q.

It is well-known that the point graph of a generalized quadrangle of order (s, t) is
strongly regular with parameters (v, k, λ, µ) where

v = (s + 1)(st + 1), k = s(t + 1), λ = s − 1, µ = t + 1.

Axiom GQ1 ensures that a generalized quadrangle does not contain triples of pairwise
collinear points that are not all three on one line. From this follows that every set of
points that induces a clique in the point graph is a subset of some line. In particular,
the generalized quadrangle can be reconstructed from its point graph up to isomor-
phism by taking as points the vertices of the point graph, as lines the maximal cliques
and as incidence relation the ∈-relation. Moreover, the point graph of a generalized
quadrangle cannot contain K4 − e as an induced subgraph because this would imply
the existence of two distinct maximal cliques that intersect in at least two points
which cannot happen because of axiom PLS3.
In [9] P. J. Cameron examined point graphs of generalized quadrangles and made
the above observations. These observations lead him to study strongly regular graphs
that do not contain K4 − e as an induced subgraph. It turns out that such graphs
always arise as point graph of certain partial linear spaces. The class of partial linear
spaces that have as a point graph an srg without K4 − e as an induced subgraph, are
called partial quadrangles. Below we give an axiomatization:

Definition 5.4. A partial quadrangle with parameters (s, t, µ) (short PQ(s, t, µ)) is
a partial linear space (P, L ) of order (s, t) with the following properties:
PQ1. If three points are pairwise collinear, then they are all three on one line.
PQ2. For every pair (P, Q) of non-collinear points there exist µ points X that are
collinear with both points P and Q.

The point graphs of partial quadrangles have an elegant characterization:

Theorem 5.5 (P. J. Cameron [9, Theorem 2]). Let Γ = (V, E) be a strongly regu-
lar graph with parameters (v, k, λ, µ). Then Γ is isomorphic to the point graph of a
partial quadrangle if and only if µ > 0 and it does not contain any induced subgraph
isomorphic to K4 − e.

Let us recall that starting from a strongly regular graph Γ with parameters
(v, k, λ, µ) that has no induced subgraph isomorphic to K4 − e, we can construct a
partial quadrangle by taking as points the vertices of Γ and as lines the maximal
cliques. The resulting partial quadrangle has parameters (λ + 1, k
λ+1 − 1, µ). On the
other hand, the parameters of the point graph of a PQ(s, t, ˜µ) are

v = s(t + 1)(˜µ + st)
˜µ + 1, k = s(t + 1), λ = s − 1, µ = ˜µ.

Algebraic Combinatorics, Vol. 4 #5 (2021) 867

Christian Pech

Remark 5.6. Every GQ(s, t) is at the same time a PQ(s, t, t+1). While there are many
known constructions for generalized quadrangles (cf. [47]), much fewer constructions
are known for proper partial quadrangles, i.e. for partial quadrangles that are not
generalized quadrangles. A ﬁrst source of proper partial quadrangles is given by the
triangle-free strongly regular graphs. They correspond to the PQ(1, t, µ). The known
triangle-free srgs are the pentagon (PQ(1, 1, 1)), the Petersen graph (PQ(1, 2, 1), the
Clebsch graph (PQ(1, 4, 2)), the Hoﬀman–Singleton graph (PQ(1, 6, 1)), the Gewirtz
graph (PQ(1, 9, 2)), the Mesner graph (PQ(1, 15, 4)), and the Higman–Sims graph
(PQ(1, 21, 6). Two more inﬁnite sources of proper partial quadrangles are related to
generalized quadrangles of order (q, q2). For the ﬁrst one we start with a GQ(q, q2)
and select a point P . Then we delete P , all lines through P , and all points that
are collinear with P in this generalized quadrangle. When this is done, we end up
with a PQ(q − 1, q2, q2 − q) (see [11, Theorem 7.9]). The second source is induced by
so-called hemisystems (in the sense of Segre [52, p. 161]). Whenever a hemisystem
exists in a GQ(q, q2), it gives rise to a PQ((q − 1)/2, q2, (q − 1)2/2). Such partial
quadrangles were constructed by Cossidente and Penttila (see [13]) for all odd prime
powers q. Meanwhile a number of other constructions of hemisystems in generalized
quadrangles were found. We refer to [57] for a relatively recent overview together with
further links to topics from algebraic graph theory. Also, the papers [1, 12, 14] may
be used as a starting point to get an overview of the known constructions of proper
partial quadrangles.

Now we are ready to formulate the ﬁrst result of this section:

Theorem 5.7. Let Γ be the point graph of a partial quadrangle. Then Γ is (2, 5)-
regular, i.e. it satisﬁes the 5-vertex condition.

Proof. At ﬁrst we note that by Theorem 4.1, in order to test the 4-vertex condition
for Γ it is enough to test it for
 T1 : ,

as Γ does not contain K4 − e as an induced subgraph. Clearly, we have

#(Γ, T1) = (s − 1)(s − 2).

Secondly we note that from all the graph types given in Proposition 4.3 only the
underlying graph of the ﬁrst one does not contain K4 − e as an induced subgraph.
Thus, in order to test the 5-vertex condition, we have only to consider

T2 :
 .

However, we easily compute

#(Γ, T2) = (s − 1)(s − 2)(s − 3). □

Let us have a look at a criterion for the 6-vertex condition for partial quadrangles:

Algebraic Combinatorics, Vol. 4 #5 (2021) 868

On highly regular strongly regular graphs

Proposition 5.8. Let Γ be the point graph of a partial quadrangle. Then in order to
test the 6-vertex condition for Γ it suﬃces to check it for the following 8 graph types:

.

Proof. The above given 8 graph types form a transversal of the isomorphism classes
of all those graph types T = (∆, ι, Θ) of order (2, 6) for which Env(T) is 3-connected
and for which Θ does not contain an induced subgraph isomorphic to K4 − e. Now
the claim follows from Theorem 5.7 together with Proposition 4.2. □

S. Reichard showed in [50] that among these 8 graph types there are 5 types T
such that the point graph of every generalized quadrangle is T-regular. Together with
this observation we obtain:

Proposition 5.9. The point graph of a generalized quadrangle satisﬁes the 6-vertex
condition if and only if it is regular for the following graph types:

.

Proof. Let Γ be the point graph of a GQ(s, t). By Proposition 5.8, in order to prove the
claim, we need to show that Γ is regular for the following graph types (to get a better
understanding, we depict the types not as graphs but as geometrical conﬁgurations):

T1 T2 T3 T4 T5.

However, it is not hard to see that:

#(Γ, T1) = t
2s(s − 1),

#(Γ, T2) = (t + 1)t(s − 1)(s − 2),

#(Γ, T3) = t
2s(s − 1),

#(Γ, T4) = (t + 1)t(s − 1),

#(Γ, T5) = (t + 1)t(t − 1)s. □

Recall, that in a partial linear space, three pairwise non-collinear points are called
a triad. Moreover, a center of a triad is a point collinear to all three points of the
triad.

Theorem 5.10 (P. J. Cameron [9, Theorem 2]). Let Π = (P, L ) be a partial quad-
rangle of order (s, t, µ). Then
(s(t − 1) + (µ − 1)(µ − 2)) ( (t + 1)ts2

µ − 1 − (t + 1)s + µ
) ⩾ µ(t − 1)
2s
2.

Algebraic Combinatorics, Vol. 4 #5 (2021) 869

Christian Pech

Moreover, equality holds if and only if every triad in Π has the same number c of
centers. In this case we have
 c = 1 + (µ − 1)(µ − 2)
s(t − 1) .

For the special case of generalized quadrangles this simpliﬁes to the following well-
known result:

Theorem 5.11 ([26, Theorem 3.2], [5, Corollary 3.1], [9, Corollary to Theorem 1]).
Let Π = (P, L ) be a generalized quadrangle of order (s, t). Then s
2 ⩾ t. Moreover,
equality holds if and only if every triad in Π has the same number (s + 1) of centers.

Remark 5.12. According to P.J. Cameron (cf. [9, Abstract]), the ﬁrst part of the
above theorem was proved by D.G. Higman in 1971. The fact that in generalized
quadrangles of order (s, s
2) every triad has exactly s + 1 centers (which, in turn, are
pairwise non-collinear) was proved by R.C. Bose and S.S. Shrikhande in 1971. In its
full generality the theorem was proved by P.J. Cameron in 1973.

Corollary 5.13 ([51, Corollary 3]). Let Γ be the point graph of a generalized quad-
rangle of order (q, q2). Then Γ is 3-isoregular.

Proposition 5.14. Let Π be a partial quadrangle of order (s, t, µ), such that every
triad in Π has the same number c of centers, and let Γ be its point graph. Then Γ
is 3-isoregular if and only if either Π is a generalized quadrangle and t = s
2, or Γ is
triangle-free (i.e. s = 1).

Proof. “⇒:” Suppose that Γ is 3-isoregular. Consider the following graph type T =
(∆, ι, Θ) of order (3, 4):
 x
 y
 z .

Then any embedding κ of ∆ into Γ determines a line l of Π (spanned by κ(x) and κ(y))
and a vertex p = κ(z) not on this line such that neither κ(x) nor κ(y) is collinear with
p. In any partial quadrangle there exists at most one vertex q on l that is collinear
with p (otherwise Π would contain a triangle of lines). So we have #(Γ, T) ∈ {0, 1}.
If #(Γ, T) = 0, then Γ is triangle-free and if #(Γ, T) = 1, then Π is a generalized
quadrangle. By Theorem 5.11, we obtain that t = s
2.
“⇐:” If Π is a generalized quadrangle of order (s, s
2), then Γ is 3-isoregular, by
Corollary 5.13. So suppose that Γ is triangle-free. Let u, v, w be three mutually distinct
vertices of Γ. If the subgraph of Γ induced by u, v, and w contains an edge, then none
of the edges has a common neighbor (otherwise Γ would contain triangles). So u, v,
w form a triad in Π. Hence, they have c common neighbors in Γ. Consequently, Γ is
3-isoregular. □

3-isoregular triangle-free graphs appear to be extremely rare. The following obser-
vation was made by R. Noda:

Proposition 5.15 (cf. [9, p. 70]). Let Γ be a non-degenerate triangle-free 3-isoregular
graph in which any three pairwise non-adjacent points are joint to exactly n vertices.
Then Γ is the point graph of a PQ(1, (n
2 + 2n − 1)(n + 1), n(n + 1)).

Remark 5.16. The ﬁrst two members of this series are the Clebsch graph (n = 1) and
the Higman–Sims graph (n = 2). For n = 3 the putative graph would have parameters

Algebraic Combinatorics, Vol. 4 #5 (2021) 870

On highly regular strongly regular graphs

(v, k, λ, µ) = (324, 57, 0, 12). It was shown by A. L. Gavrilyuk and A. A. Makhnev
in [20] that such a graph does not exist. For a very interesting account of the history
of the discovery of the Higman–Sims graph, we refer to [36].

Theorem 5.17. Let Γ be the point graph of a partial quadrangle and suppose that Γ
is 3-isoregular. Then Γ is (3, 7)-regular.

Proof. As Γ is 3-isoregular, it is (3, 4)-regular. By Corollary 3.42, in order to prove
(3, 5)-regularity of Γ it suﬃces to prove the T-regularity for all graph types T of order
(3, 5) for which Env(T) is 4-connected. Since Γ does not have K4 − e as an induced
subgraph, we can shorten this list by all T whose underlying graph contains K4 − e. A
computer search reveals that only the graph type Ta depicted below fulﬁlls all these
requirements:
 Ta Tb Tc
 .

However, it is easy to see that

#(Γ, Ta) =
 {(s − 2)(s − 3) s ⩾ 4,
0 otherwise.

Thus, Γ is (3, 5)-regular.
With the same reasoning as before and again using a computer, we obtain that Γ
is (3, 6)-regular if and only if it is Tb-regular. However, it is easy to see that

#(Γ, Tb) =
 {(s − 2)(s − 3)(s − 4) s ⩾ 5,
0 otherwise.

Thus, Γ is (3, 6)-regular.
Finally, once more using the same reasoning as above and using a computer, we ob-
tain that Γ is (3, 7)-regular if and only if it is Tc-regular. However, it is easy to see that

#(Γ, Tc) =
 {(s − 2)(s − 3)(s − 4)(s − 5) s ⩾ 6,
0 otherwise.

Thus, Γ is (3, 7)-regular. □

The previous theorem generalizes and strengthens a result by Reichard ([51, The-
orem 2]) that states that the point graphs of generalized quadrangles of order (q, q2)
satisfy the 7-vertex condition.

Corollary 5.18. Let Γ be the point graph of a partial quadrangle and suppose that
Γ is 3-isoregular. Then, for every u ∈ V (Γ), the second subconstituent Γ2(u) satisﬁes
the 6-vertex condition.

Proof. This follows from Proposition 3.44. □

Note that by Proposition 5.14, the previous corollary applies in particular to the
point graphs of generalized quadrangles of order (q, q2). This has the following con-
sequence:

Algebraic Combinatorics, Vol. 4 #5 (2021) 871

Christian Pech

Corollary 5.19. Let Γ be the point graph of a partial quadrangle of order (q −
1, q2, q2 − q). Then Γ satisﬁes the 6-vertex condition.

Proof. It was shown by A. A. Ivanov and S. V. Shpectorov in [27, Theorem A(i)] that
whenever a graph Γ is strongly regular with parameters (v, k, λ, µ) = (q4, (q2 + 1)(q −
1), q −2, q(q −1))) for some q ⩾ 2, such that in Γ every edge is contained in a complete
subgraph of order q, then Γ is of the shape ̂Γ2(u), where ̂Γ is the point graph of some
generalized quadrangle of order (q, q2), and where u is some vertex of ̂Γ.
Since the given graph Γ is the point graph of a PQ(q − 1, q2, q2 + q), the result
by Ivanov and Shpectorov applies to it. Let ̂Γ be the point graph of a GQ(q, q2) and
let u be a vertex of ̂Γ, such that Γ = ̂Γ2(u). By Proposition 5.14, ̂Γ is 3-isoregular.
Finally, by Proposition 3.44, we have that ̂Γ2(u) is (2, 6)-regular. In other words, Γ
satisﬁes the 6-vertex condition. □

Example 5.20. There exists an inﬁnite family of generalized quadrangles of order
(q, q2) whose point graphs are non rank 3 graphs (cf. [30, 31, 46]). By Theorem 5.17,
the point graph of any such generalized quadrangle is (3, 7)-regular. The second sub-
constituents of these graphs give rise to a hitherto unknown family of non-rank 3
graphs satisfying the 6-vertex condition.
The smallest actual example is the point graph Γ of a non-classical generalized
quadrangle of order (5, 25). Its parameters are given by

(v, k, λ, µ) = (756, 130, 4, 26).

Its automorphism group is intransitive of rank 11.
Γ has two non-isomorphic second subconstituents Γ′ and Γ′′. Both satisfy the 6-
vertex condition and both are in turn point graphs of partial quadrangles of order
(4, 25, 20). The automorphism group of Γ′ is intransitive of rank 52 and the automor-
phism group of Γ
′′ is transitive of rank 5.

Proposition 5.21. Let Γ be the point graph of a partial quadrangle, and suppose that
Γ is 3-isoregular. Then Γ satisﬁes the 8-vertex condition if and only if it is regular for
the following graph types of order (2, 8):
 .

Proof. By Theorem 5.17 we already know that Γ is (3, 7)-regular. Let M be a transver-
sal of all isomorphism classes of graph types of order (m, n), where m ⩽ 3 and n ⩽ 7.
To show that Γ satisﬁes the 8-vertex condition means to show that it is (2, 8)-regular.
By Proposition 3.40 it suﬃces to show that Γ is T-regular for all graph types of
order (2, 8) that are ̂T-irreducible, for all ̂T ∈ M. However, these are precisely the
(3, 7)-irreducible graphs types T of order (2, 8). In turn, by Lemma 3.23, these are the
graph types T of order (2, 8) for which Env(T) is 4-connected. By the computer we
may obtain a list of all such graph types. Since the point graph of a partial quadrangle
does not contain K4 − e as an induced subgraph, we may decrease the list of graph
types further to those whose underlying graph does not contain K4 − e. We end up
with the above depicted graph types and the four graph types given below (for better

Algebraic Combinatorics, Vol. 4 #5 (2021) 872

On highly regular strongly regular graphs

visibility they are depicted as geometric conﬁgurations rather than graphs):

T1 T2 T3 T4
 .

By Proposition 5.14, Γ is either the point graph of a generalized quadrangle of order
(q, q2) or it is triangle-free. Neither of the graph types T1, . . . , T4 is triangle-free. Thus,
if Γ is triangle-free then we are done. Suppose therefore that Γ is the point graph of
a generalized quadrangle Π = (P, L ) of order (s, t) = (q, q2). Then we compute:

#(Γ, T1) = (t + 1)t(s − 1)(s − 2)(s − 3),

#(Γ, T2) = (t + 1)t(s − 1)(s − 2),

#(Γ, T3) = t2s(s − 1)(s − 2),

#(Γ, T4) = t2s(s − 1)(s − 2). □

Let us at the end have a look on partial quadrangles Π in which every triad has the
same number c of centers, but where the point graph Γ is not necessarily 3-isoregular.

Lemma 5.22. Let Π be a partial quadrangle in which every triad has c centers, and let
Γ be the point graph of Π. Then Γ is regular for all graph types of order (3, 4), except
possibly the following:
 .

Proof. Let us ﬁrst of all list all graph types of order (3, 4) not mentioned above:
 .

Algebraic Combinatorics, Vol. 4 #5 (2021) 873

Christian Pech

Suppose that the parameters of Γ as a strongly regular graph are (v, k, λ, µ). Then
we count (using some of the previous calculations from Example 3.33):

#( ) = c,

#( ) = #( ) · #( ) − #( ) = µ − c,

#( ) = #( ) · #( ) − #( ) = (k − µ) − (µ − c) = k − 2µ + c,

#( ) = #( ) · #( ) − #( ) − #( ) = ¯λ − k + 2µ − c − 1,

#( ) = 0,

#( ) = #( ) · #( ) − #( ) − #( ) = µ − 1,

#( ) = #( ) · #( ) − #( ) = λ,

#( ) = #( ) · #( ) − #( ) − #( ) = k − 2λ − 2,

#( ) = #( ) · #( ) − #( ) = k − λ − µ,

#( ) = #( ) · #( ) − #( ) − #( ) = ¯µ − k + λ + µ − 1,

#( ) = λ − 1,

#( ) = 0,

#( ) = #( ) · #( ) − #( ) = k − λ − 1,

#( ) = #( ) · #( ) − #( ) = ¯µ − k + λ + 1. □

Proposition 5.23. Let Π be a partial quadrangle in which every triad has c centers,
and let Γ be the point graph of Π. Then Γ satisﬁes the 6-vertex condition if and only
if it is regular for the following graph types of order (2, 6):
 .

Proof. The four given graph types are exactly those from Proposition 5.8 that are irre-
ducible for any of the graph types of order (3, 4) depicted in the proof of Lemma 5.22.
All the other types are in fact ( )-reducible:

∼= ⊕e

∼= ⊕e

∼= ⊕e

∼= ⊕e .

Now the claim follows from Proposition 3.40. □

Algebraic Combinatorics, Vol. 4 #5 (2021) 874

On highly regular strongly regular graphs

6. Concluding remarks

The (m, n)-regularity introduced in Section 3 is a very strong condition. It is, in fact,
interesting only for m ⩽ 4, because any 5-isoregular graph is 5-homogeneous and, in
fact, homogeneous ([10, 19, 22]). At ﬁrst sight, this appears to limit the use of the
regularity conditions introduced in this paper. However, in principle, the deﬁnitions
and results from Section 3 apply to other categories of combinatorial objects. Finite
metric spaces (possibly with integer or with rational distances), directed graphs, or
semilinear spaces come to mind.
For the category of ﬁnite graphs, the most interesting are (m, n)-regular graphs
where m ∈ {2, 3, 4}. Here the goal is to ﬁnd (m, n)-regular graphs that are not m-
homogeneous and, if feasible, to classify such graphs completely, up to isomorphism.
As was noted above, every graph Γ is (0, n)-regular, because for every graph type
T = (∅, ι, Θ) the number #(Γ, T) is equal to the number of embeddings of Θ into
Γ. Nevertheless, counting subgraphs of a graph has been used as a global invariant
for distinguishing non-isomorphic graphs. For instance, in [34] subgraphs isomorphic
to K4 are counted in order to distinguish point-symmetric strongly regular graphs in
three inﬁnite families.
We would also like to mention K. Kováčiková’s dissertation thesis [37] about count-
ing subgraphs in strongly regular graphs, where she, among other things, counts the
induced subgraphs of order ⩽ 9 in a putative Moore graph of valency 57. Her meth-
ods involve the solution of huge linear systems of equations. It will be interesting to
compare her approach with the one given in this paper.
The (2, t)-regular graphs correspond exactly to the graphs that satisfy the t-vertex
condition. There is a longstanding conjecture by M. Klin [16], that there exists a
natural number t0 such that for each t ⩾ t0 all (2, t)-regular graphs are 2-homogeneous
(i.e. they are rank 3 graphs). The largest t for which the existence of a non-rank 3,
(2, t)-regular graph is settled is t = 7, due to Reichard [51, Theorem 2]. Thus in Klin’s
conjecture, we have t0 ⩾ 8.
We should mention that the motivation to study graphs with the t-vertex con-
dition comes not only from Klin’s conjecture. The driving motivation to introduce
the t-vertex condition was to distinguish the rank 3 graphs from other strongly reg-
ular graphs with the same parameters. In the times before the announcement of the
classiﬁcation of ﬁnite simple groups, there was the hope to uncover in this way new
sporadic ﬁnite simple groups. A typical example of the use of the t-vertex condition
as a distinguishing invariant is [45].
Up till now, (3, t)-regular graphs were known only for t = 4 (apart from the
3-homogeneous graphs). In this paper, the ﬁrst cases of non-3-homogeneous (3, 7)-
regular graphs are observed. Among the examples, there are graphs whose automor-
phism group is intransitive. Given Klin’s conjecture and because of the observation
that (3, t)-regular graphs appear to be much rarer than (2, t)-regular graphs, it seems
sensible to ask whether there exists a t1 such that all (3, t)-regular graphs with t ⩾ t1
are 3-homogeneous. This paper shows that if such a t1 exists, then t1 ⩾ 8. Note that
every (3, t)-regular graph is (2, t)-regular. Thus, if Klin’s conjecture turns out to be
true, then this question can be answered using the classiﬁcation of rank 3 graphs.
Recently, in [48] a classical family of strongly regular graphs originally constructed
by Brouwer, Ivanov, and Klin (see [7]) was analyzed for regularities. It was shown
there that these graphs are (3, 5)-regular but not 2-homogeneous.
There is only one known (4, 5)-regular graph that is not 4-homogeneous, the
McLaughlin graph on 275 vertices. A computer experiment showed that this graph is
not (4, 6)-regular. Is every (4, 6)-regular graph 4-homogeneous?

Algebraic Combinatorics, Vol. 4 #5 (2021) 875

Christian Pech

Acknowledgements. The present paper owes much to the numerous discussions with
Misha Klin and Sven Reichard that we had over the years on the topic of regularity
conditions of strongly regular graphs. My thanks go to Andy Woldar whose comments
helped to improve a preliminary version of the paper. Last but not least, the many
helpful remarks by the anonymous referees are gratefully acknowledged.

References

[1] John Bamberg, Frank De Clerck, and Nicola Durante, Intriguing sets in partial quadrangles, J.
Combin. Des. 19 (2011), no. 3, 217–245.
[2] Eiichi Bannai, Maximal subgroups of low rank of ﬁnite symmetric and alternating groups, J.
Fac. Sci. Univ. Tokyo Sect. IA Math. 18 (1971/72), 475–486.
[3] Francis Borceux, Handbook of categorical algebra (vol. 1), Encyclopedia of Mathematics and its
Applications, vol. 50, Cambridge University Press, Cambridge, 1994.
[4] Raj C. Bose, Strongly regular graphs, partial geometries and partially balanced designs, Paciﬁc
J. Math. 13 (1963), 389–419.
[5] Raj C. Bose and Sharadchandra S. Shrikhande, Geometric and pseudo-geometric graphs (q2 +
1, q + 1, 1), J. Geom. 2 (1972), 75–94.
[6] Andries E. Brouwer, Parameters of strongly regular graphs, https://www.win.tue.nl/~aeb/
graphs/srg/srgtab.html.
[7] Andries E. Brouwer, Andrei V. Ivanov, and Mikhail H. Klin, Some new strongly regular graphs,
Combinatorica 9 (1989), no. 4, 339–344.
[8] J. M. J. Buczak, Finite group theory, D.Phil. thesis, Oxford University, 1980.
[9] Peter J. Cameron, Partial quadrangles, Quart. J. Math. Oxford Ser. (2) 26 (1975), 61–73.
[10] , 6-transitive graphs, J. Combin. Theory Ser. B 28 (1980), no. 2, 168–179.
[11] Peter J. Cameron, Jean-Marie Goethals, and Johan J. Seidel, Strongly regular graphs having
strongly regular subconstituents, J. Algebra 55 (1978), no. 2, 257–280.
[12] Antonio Cossidente, Combinatorial structures in ﬁnite classical polar spaces, in Surveys in
combinatorics 2017, London Math. Soc. Lecture Note Ser., vol. 440, Cambridge Univ. Press,
Cambridge, 2017, pp. 204–237.
[13] Antonio Cossidente and Tim Penttila, Hemisystems on the Hermitian surface, J. London Math.
Soc. (2) 72 (2005), no. 3, 731–741.
[14] Frank De Clerck and Hendrik Van Maldeghem, Some classes of rank 2 geometries, in Handbook
of incidence geometry, North-Holland, Amsterdam, 1995, pp. 433–475.
[15] Sergei Evdokimov and Ilia Ponomarenko, Separability number and Schurity number of coherent
conﬁgurations, Electron. J. Combin. 7 (2000), Paper no. R31 (33 pages).
[16] Igor A. Faradžev, Mikhail H. Klin, and Mikhail E. Muzichuk, Cellular rings and groups of
automorphisms of graphs, in Investigations in algebraic theory of combinatorial objects, Math.
Appl. (Soviet Ser.), vol. 84, Kluwer Acad. Publ., Dordrecht, 1994, pp. 1–152.
[17] Dmitry G. Fon-Der-Flaass, New proliﬁc constructions of strongly regular graphs, Adv. Geom. 2
(2002), no. 3, 301–306.
[18] The GAP Group, GAP – Groups, Algorithms, and Programming, Version 4.11.1, 2021, https:
//www.gap-system.org.
[19] Anthony Gardiner, Homogeneous graphs, J. Combinatorial Theory Ser. B 20 (1976), no. 1,
94–102.
[20] Alexander L. Gavrilyuk and Alexander A. Makhnev, On Krein graphs without triangles, Dokl.
Math. 72 (2005), no. 1, 591–594.
[21] Chris Godsil and Gordon Royle, Algebraic graph theory, Graduate Texts in Mathematics, vol.
207, Springer-Verlag, New York, 2001.
[22] Jakov Ju. Gol’fand and Mikhail H. Klin, On k-homogeneous graphs, in Algorithmic studies in
combinatorics (Russian), Nauka, Moscow, 1978, pp. 76–85, 186 (errata insert).
[23] Frank Harary, Graph theory, Addison-Wesley Publishing Co., Reading, Mass.-Menlo Park,
Calif.-London, 1969.
[24] Marshall D. Hestenes and Donald G. Higman, Rank 3 groups and strongly regular graphs, in
Computers in algebra and number theory (Proc. SIAM-AMS Sympos. Appl. Math., New York,
1970), SIAM-AMS Proc., vol. IV, Amer. Math. Soc., Providence, R.I., 1971, pp. 141–159.
[25] Donald G. Higman, Partial geometries, generalized quadrangles and strongly regular graphs, Atti
del Convegno di Geometria Combinatoria e sue Applicazioni (Univ. Perugia, Perugia, 1970), Ist.
Mat., Univ. Perugia, Perugia, 1971, pp. 263–293.

Algebraic Combinatorics, Vol. 4 #5 (2021) 876

On highly regular strongly regular graphs

[26] , Invariant relations, coherent conﬁgurations and generalized polygons, Combinatorics
(Proc. Advanced Study Inst., Breukelen, 1974), Part 3: Combinatorial group theory, Math.
Centre Tracts, vol. 57, 1974, pp. 27–43.
[27] Alexander A. Ivanov and Sergey V. Shpectorov, A characterization of the association schemes
of Hermitian forms, J. Math. Soc. Japan 43 (1991), no. 1, 25–48.
[28] Andrei V. Ivanov, Non-rank-3 strongly regular graphs with the 5-vertex condition, Combinatorica
9 (1989), no. 3, 255–260.
[29] , Two families of strongly regular graphs with the 4-vertex condition, Discrete Math. 127
(1994), no. 1-3, 221–242, Graph theory and applications (Hakone, 1990).
[30] William M. Kantor, Generalized quadrangles associated with G2(q), J. Combin. Theory Ser. A
29 (1980), no. 2, 212–219.
[31] , Some generalized quadrangles with parameters q2, q, Math. Z. 192 (1986), no. 1, 45–50.
[32] William M. Kantor and Robert A. Liebler, The rank 3 permutation representations of the ﬁnite
classical groups, Trans. Amer. Math. Soc. 271 (1982), no. 1, 1–71.
[33] Petteri Kaski, Mahdad Khatirinejad, and Patric R. J. Östergård, Steiner triple systems satis-
fying the 4-vertex condition, Des. Codes Cryptogr. 62 (2012), no. 3, 323–330.
[34] Mikhail Klin, Nimrod Kriger, and Andrew Woldar, Classiﬁcation of highly symmetrical trans-
lation loops of order 2p, p prime, Beitr. Algebra Geom. 55 (2014), no. 1, 253–276.
[35] Mikhail Klin, Mariusz Meszka, Sven Reichard, and Alex Rosa, The smallest non-rank 3 strongly
regular graphs which satisfy the 4-vertex condition, Bayreuth. Math. Schr. (2005), no. 74, 145–
205.
[36] Mikhail H. Klin and Andrew J. Woldar, The strongly regular graph with parameters
(100, 22, 0, 6): hidden history and beyond, Acta Univ. M. Belii Ser. Math. 25 (2017), 5–62.
[37] Kristína Kováčiková, Induced subgraphs in strongly regular graphs, Dissertation Thesis, Come-
nius University in Bratislava, 2015.
[38] Nimrod Kriger, Investigation of strongly regular graphs of latin square type and related combi-
natorial objects, D.Phil. thesis, Ben-Gurion University of the Negev, Beer-Sheva, 2015.
[39] Martin W. Liebeck and Jan Saxl, The ﬁnite primitive permutation groups of rank three, Bull.
London Math. Soc. 18 (1986), no. 2, 165–172.
[40] Saunders Mac Lane, Categories for the working mathematician, second ed., Graduate Texts in
Mathematics, vol. 5, Springer-Verlag, New York, 1998.
[41] Dugald Macpherson, A survey of homogeneous structures, Discrete Math. 311 (2011), no. 15,
1599–1634.
[42] Brendan D. McKay and Adolfo Piperno, Practical graph isomorphism, II, J. Symbolic Comput.
60 (2014), 94–112.
[43] Mikhail Muzychuk, A generalization of Wallis-Fon-Der-Flaass construction of strongly regular
graphs, J. Algebraic Combin. 25 (2007), no. 2, 169–187.
[44] Jaroslav Nešetřil, Amalgamation of graphs and its applications, in Second International Con-
ference on Combinatorial Mathematics (New York, 1978), Ann. New York Acad. Sci., vol. 319,
New York Acad. Sci., New York, 1979, pp. 415–428.
[45] Dmitrii V. Pasechnik, Skew-symmetric association schemes with two classes and strongly regular
graphs of type L2n−1(4n−1), Acta Appl. Math. 29 (1992), no. 1-2, 129–138, Interactions between
algebra and combinatorics.
[46] Stanley E. Payne, Collineations of the generalized quadrangles associated with q-clans, in Com-
binatorics ’90 (Gaeta, 1990), Ann. Discrete Math., vol. 52, North-Holland, Amsterdam, 1992,
pp. 449–461.
[47] Stanley E. Payne and Joseph A. Thas, Finite generalized quadrangles, second ed., EMS Series
of Lectures in Mathematics, European Mathematical Society (EMS), Zürich, 2009.
[48] Christian Pech and Maja Pech, On a family of highly regular graphs by Brouwer, Ivanov, and
Klin, Discrete Math. 342 (2019), no. 5, 1361–1377.
[49] Sven Reichard, A criterion for the t-vertex condition of graphs, J. Combin. Theory Ser. A 90
(2000), no. 2, 304–314.
[50] , Computational and theoretical analysis of coherent conﬁgurations and related incidence
structures, Ph.D thesis, University of Delaware, 2003.
[51] , Strongly regular graphs with the 7-vertex condition, J. Algebraic Combin. 41 (2015),
no. 3, 817–842.
[52] Beniamino Segre, Forme e geometrie hermitiane, con particolare riguardo al caso ﬁnito, Ann.
Mat. Pura Appl. (4) 70 (1965), 1–201.
[53] Peter J. Slater, A classiﬁcation of 4-connected graphs, J. Combinatorial Theory Ser. B 17 (1974),
281–298.

Algebraic Combinatorics, Vol. 4 #5 (2021) 877

Christian Pech

[54] Leonard H. Soicher, GRAPE, GRaph Algorithms using PErmutation groups, Version 4.8.5,
2021, (Refereed GAP package), https://gap-packages.github.io/grape.
[55] Jacques Tits, Sur la trialité et certains groupes qui s’en déduisent, Inst. Hautes Études Sci.
Publ. Math. (1959), no. 2, 13–60.
[56] William T. Tutte, A theory of 3-connected graphs, Nederl. Akad. Wetensch. Proc. Ser. A 64 =
Indag. Math. 23 (1961), 441–455.
[57] Edwin R. van Dam, William J. Martin, and Mikhail Muzychuk, Uniformity in association
schemes and coherent conﬁgurations: cometric Q-antipodal schemes and linked systems, J. Com-
bin. Theory Ser. A 120 (2013), no. 7, 1401–1439.
[58] Walter D. Wallis, Construction of strongly regular graphs using aﬃne designs, Bull. Austral.
Math. Soc. 4 (1971), 41–49.

Christian Pech, Radebeul, Germany
E-mail : cpech@freenet.de
Url : https://www.researchgate.net/profile/Christian_Pech2

Algebraic Combinatorics, Vol. 4 #5 (2021) 878
