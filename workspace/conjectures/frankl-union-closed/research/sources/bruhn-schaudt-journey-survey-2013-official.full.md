<!-- source: https://www.uni-ulm.de/fileadmin/website_uni_ulm/mawi.inst.081/Henning/UCSurvey.pdf | converted from PDF -->

The journey of the union-closed sets conjecture

Henning Bruhn and Oliver Schaudt

Abstract

We survey the state of the union-closed sets conjecture.

1 Introduction

One of the ﬁrst mentions [6] of the union-closed sets conjecture calls it “a much-
travelled conjecture”. This is indeed so. Geographically it has spread from
Europe to at least North America, Asia, Oceania and Australia. Mathematically
it has ventured from its origins in extremal set theory to lattice and graph theory.
In this survey we strive to trace its journey.
The main attraction of the conjecture is certainly its simple formulation. A
family A of sets is union-closed if for every two member-sets A, B ∈ A also their
union A ∪ B is contained in A.

Union-closed sets conjecture. Any ﬁnite union-closed family of sets A ̸= {∅}
has an element that is contained in at least half of the member-sets.

An example of a union-closed family is given in Figure 1a, where we have
omitted commas and parentheses. There, one may count that the elements 1, 2, 3
appear each in only 12 of the 25 member-sets, which is less than half of the sets.
Each of the other elements 4, 5, 6 however is contained in 16 sets, more than
enough for the family to satisfy the conjecture. Power sets are other examples
of union-closed families, and there the conjecture is tight: every element appears
in exactly half of the member-sets.
Despite its apparent simplicity the union-closed sets conjecture remains wide
open. This is certainly not for lack of interest – there are about 50 articles

123456
12345 12346 12356 12456 13456 23456
1234 1235 1236 1456 2456 3456
123 145 246 356 456
45 46 56
4 5 6
∅

(a) Union-closed
 123456
12356 12346 12345
1236 1235 1234
456 236 135 124 123
56 46 45 23 13 12
6 5 4 3 2 1
∅

(b) Intersection-closed

Figure 1: A union-closed family and its complement

1

dedicated to the conjecture, as well as several websites [28, 69, 70]. Due to
this extensive research activity, we now know that the conjecture is satisﬁed for
various union-closed families A. For instance:

• if A has at most 12 elements or at most 50 member-sets;
• if the number n of member-sets is large compared to the number m of
elements, that is, when n ≥ 2
3 2
m;
• if n is small compared to m: when n ≤ 2m (where we need to assume that
A is separating, that is, for any two elements there exists a member-set
containing exactly one of them);
• if A contains one of a number of subconﬁgurations, such as a singleton-set;
• or if A has a particular structure, for instance, if A may be represented
by a lower semimodular lattice, or by a subcubic graph.

We will discuss all these results, and give proper attributions, in the course of
the article. All these partial results notwithstanding, we still seem to be far from
a proof of the conjecture, and this is even the case for the obvious relaxation in
which we settle for an element that appears in only, say, ≥ 1% of the member-
sets. The best result in this respect is an observation by Knill (slightly improved
by W´ojcik) that yields always an element of frequency at least n−1
log2 n .

In an article [7] of 1987, Peter Winkler
1 wrote “the ‘union-closed sets conjec-
ture’ is well known indeed, except for (1) its origin and (2) its answer!” While
the answer remains elusive, we can shed some light on its origins.
Most authors today attribute the conjecture to Peter Frankl, and following
Frankl [26] date it to 1979. The sole exception are Balla, Bollob´as and Eccles [9],
who call it a “folklore conjecture” that “was well known by the mid-1970s”. We
cannot resolve this conﬂict of attribution, nor do we have the intention to do so.
However, there is no doubt that Frankl did discover the conjecture (whether he
was not the ﬁrst is for others to decide) and that he played an instrumental role
in popularising it. Consequently, we will sometimes speak of Frankl’s conjecture.
In late 1979, Frankl [23] was working on traces of ﬁnite sets, a work that
culminated in his article [24] of 1983. Motivated by the observation that it could
be used to improve a number of bounds, Frankl formulated the conjecture when
travelling from Paris to Montreal. On his way, Frankl told the conjecture to
Ron Graham, who disseminated it widely. In about 1981, Dwight Duﬀus learnt
about it, which then led to its ﬁrst appearance in print: the proceedings of a
workshop held in 1984 in Banﬀ, edited by Rival [56], contain a short report of
Duﬀus on a “problem of P. Frankl”. The second mention is Stanley [64], which
simply cites Rival.
The next time the conjecture appeared in print, it had apparently travelled
with Franz Salzborn from Europe to Australia. An article of 1987 in the Aus-
tralian Mathematical Society Gazette [6] reports on the Annual Meeting of the
society during which Jamie Simpson publicised the conjecture. We may only

1Winkler informed us that the article was never intended to be published. Rather, this is
the case of an informal letter ending up in print without Winkler even knowing.

2

speculate that this is how the conjecture arrived in Papua New Guinea, where
Renaud and Sarvate went on to write the ﬁrst published research articles about
it [62, 63, 53] in 1989–1991. They were succeeded in 1992 by W´ojcik [71] in
Poland and, in the USA, by Poonen [50], who wrote his inﬂuential article when
he was an undergraduate. Many others followed in subsequent years.

In this survey, we aim to give a complete review of the literature on the
conjecture. While we tried to track down every article with a substantial con-
nection to the conjecture, we were not entirely successful as we could not obtain
an unpublished manuscript of Zagaglia Salvi [60] that, as W´ojcik [71] writes,
apparently contains reformulations of the conjecture.
The focus of this survey is on the methods employed to attack the conjecture.
Our treatment of the literature is therefore somewhat uneven. Whenever we can
identify a technique that, to our eyes, seems interesting and potentially powerful
we discuss it in greater detail.

2 Elementary facts and deﬁnitions

We quickly settle some notation and mention the most elementary facts. Let A
be a family of sets. We call the set U (A) := ⋃
A∈A A of all the elements that
appear in some member-set of A the universe of A. If A is union-closed then
taking the complements of all member-sets results in a family D = {U (A) \ A :
A ∈ A} that is intersection-closed : if C, D ∈ D then also C ∩ D ∈ D.
The union-closed sets conjecture has the following equivalent form for inter-
section-closed families.

Intersection-closed sets conjecture. Any ﬁnite intersection-closed family of
at least two sets has an element that is contained in at most half of the member-
sets.

Continuing with notation, we denote by

Ax := {A ∈ A : x ∈ A}.

the subfamily of member-sets containing any given element x ∈ U (A). The
cardinality |Ax| is the frequency of x in A. We also introduce notation for the
complement of Ax:
 Ax := A \ Ax = {A ∈ A : x /∈ A}.

We point out that, if A is union-closed, both Ax and Ax are union-closed as
well.
With this terminology, the union-closed sets conjecture states that in every
(ﬁnite) union-closed family A there is an x ∈ U (A) with |Ax| ≥ 1
2 |A|. We will
call such an element x abundant. When we consider an intersection-closed family
D, the intersection-closed sets conjecture asserts the existence of an element
y ∈ U (D) with |Dy| ≤ 1
2 |D|. Such a y is rare in D. (We realise that this leads

3

to the slightly bizarre situation that an element with frequency |Ax| = 1
2 |A| is
at the same time abundant and rare.)
As Poonen [50] observed, the union-closed sets conjecture becomes false if the
family is allowed to have inﬁnitely many member-sets. Indeed, the union-closed
family consisting of the sets {i, i + 1, i + 2, . . .} for every positive integer i has
inﬁnitely many member-sets but no element has inﬁnite frequency. As a conse-
quence, we will tacitly presuppose that every union-closed family considered in
this survey has only ﬁnitely many member-sets.
Additionally, we will always require the universe to be ﬁnite as well. This
is no restriction. If, for a union-closed family A, the universe has inﬁnite cardi-
nality there will be inﬁnitely many pairs of elements x and y in the universe of
A that cannot be separated by A, in the sense that x ∈ A if and only if y ∈ A
for all A ∈ A. In that case, we may simply delete y from all member-sets of
A. This results again in a union-closed family that satisﬁes the union-closed
sets conjecture if and only if A does. Consequently, it suﬃces to prove the con-
jecture for separating families A, those in which, for any two distinct elements
x, y ∈ U (A), there is an A ∈ A that contains exactly one of x, y. It is an easy
observation that the universe of any (ﬁnite) separating family is ﬁnite.
We remark furthermore that, if necessary, we may always assume a union-
closed family to include the empty set as a member. Adding ∅ will at most
increase the number of sets, while obviously the frequency of any element stays
the same. In the case of an intersection-closed family D, it is no restriction
to suppose that ∅, U (D) ∈ D. Indeed, adding U (D) to D makes satisfying the
intersection-closed sets conjecture only harder, while ∅ is always a member-set of
D unless there is an element x appearing in every set of D. In that case, deleting
x from every member results in an intersection-closed family that satisﬁes the
conjecture if and only if D does.
Given a family S of sets, the union-closure of S is the union-closed family A
deﬁned by A = { ⋃

S∈S ′ S : S ′ ⊆ S}
.

We may also say that A is generated by S.
Every union-closed family A has a unique subset B ⊆ A such that (a) A is
the union-closure of B and (b) B is inclusionwise minimal with this property.
Observe that B is simply the subfamily of non-empty sets B ∈ A with the
property that if B = X ∪ Y for some X, Y ∈ A, then X = B or Y = B. The
sets in B are the basis sets of A. Observe that A \ {B} is union-closed for B ∈ A
if and only if B is a basis set (or B = ∅).
Finally, for i, n ∈ N we use the notation [n] to denote {1, . . . , n} and [i, n]
for the set {i, i + 1, . . . , n}. We write 2
X for the power set of a set X. Any set
of cardinality k is a k-set. For a set X and an element x, we often write X + x
for X ∪ {x} and X − x for X \ {x}.
 4

3 The many faces of the conjecture

The union-closed sets conjecture has several equivalent reformulations that each
highlight a diﬀerent aspect. In this section we present three reformulations, one
in terms of lattices, one in the language of graphs and the last again in terms
of sets. That the same problem can be posed quite naturally in such diﬀerent
ﬁelds is a clear indication that Frankl’s question is a very basic and fundamental
one.
The reformulations also help us to gain conﬁdence in the veracity of the con-
jecture. Indeed, each oﬀers natural special cases such as semimodular lattices
or subcubic graphs that would appear quite artiﬁcial in the other formulations.
Proving the conjecture for such special cases then clearly adds evidence in sup-
port of the conjecture. Finally, each reformulation opens up new tools and
techniques to attack the conjecture.

3.1 The lattice formulation

Already in its earliest mention [56] it is recognised that the union-closed sets
conjecture, or rather its twin, the intersection-closed sets conjecture, has an
equivalent formulation in terms of lattices. In fact, any intersection-closed2

family together with inclusion forms a lattice.
We recall a minimum of lattice terminology. A ﬁnite lattice is a ﬁnite poset
(L, ≤) in which every pair a, b ∈ L of elements has a unique greatest lower bound,
denoted by a ∧ b (the meet), and a unique smallest upper bound, denoted by
a ∨ b (the join). All the lattices considered in this survey will be ﬁnite. The
unique minimal element is denoted by 0, the unique maximal element is 1. A
non-zero element a ∈ L is join-irreducible if a = b ∨ c implies a = b or a = c. We
write [a) := {x ∈ L : x ≥ a}. For more on lattices see, for instance, Gr¨atzer [29].

Let us ﬁrst see that an intersection-closed family A deﬁnes a lattice in a quite
direct way. This is illustrated in Figure 2, which shows the lattice corresponding
to the family of Figure 1b. As pointed out in the previous section, we may
assume that A contains its universe U (A). Then (A, ⊆) is a lattice. Indeed,
the unique greatest lower bound of any A, B ∈ A is A ∧ B = A ∩ B ∈ A, while
U (A) ∈ A guarantees that A and B always have a minimal upper bound. Such
a minimal upper bound is unique: If R and S are two upper bounds then also
R ∩ S ∈ A is an upper bound. Let us note that while A ∨ B always contains
A ∪ B, it is usually larger.
We now state the lattice formulation of Frankl’s conjecture:

Conjecture 1. Let L be a ﬁnite lattice with at least two elements. Then there
is a join-irreducible element a with |[a)| ≤ 1
2 |L|.

Let us see why Conjecture 1 is equivalent to the intersection-closed sets
conjecture. Let A be an intersection-closed family containing its universe and

2Or union-closed family, for that matter. However, it seems customary in the lattice context
to consider intersection-closed families.
 5

12356 12346 12345

1236

23

3

123456
 1235 1234

123124135
 13 12

12

236

45

4

4656

6 5

456
 Figure 2: The lattice of the set system in Figure 1. The join-irreducible elements
are precisely {1}, {2}, {3}, {4}, {5}, {6}.

consider the lattice (A, ⊆). Assume Conjecture 1 to hold, that is, there is a join-
irreducible J ∈ A with |[J)| ≤ 1
2 |A|. Suppose that every element of J appears
in some proper subset of J that is in A: ⋃
A⊂J A = J. Then, ⋁
A⊂J A ⊇⋃
A⊂J A = J, from which follows that ⋁
A⊂J A = J, which is impossible as J is
join-irreducible. Thus there is an x ∈ J that does not lie in any proper subset
of J.
Next, consider an A ∈ A containing x. Then J ∩A is a subset of J containing
x and therefore equal to J. In particular, J ⊆ A and thus A ∈ [J). Since
|[J)| ≤ 1
2 |A|, it follows that x appears in at most half of the member-sets of A.
For the other direction, consider a lattice L and associate to every x ∈ L
the set S(x) of join-irreducible elements z with z ≤ x. Then, for x, y ∈ L we
obtain that S(x ∧ y) = S(x) ∩ S(y), and thus the family A = {S(x) : x ∈ L} is
intersection-closed. Moreover, |A| = |L|.
Supposing that the intersection-closed sets conjecture holds, we obtain a
join-irreducible x ∈ L that is contained in at most half of the member-sets of
A. Then for any y ≥ x, it follows that x ∈ S(y) and thus |[x)| is bounded by
the number of member-sets of A containing x, which gives |[x)| ≤ 1
2 |L|.

Theorem 2. Conjecture 1 is equivalent to the union-closed sets conjecture.

In view of this equivalence we will say that a lattice satisﬁes Frankl’s con-
jecture if Conjecture 1 holds for it. To include the trivial case, we will extend
this to any lattice on less than two elements.
What are the advantages of the lattice formulation? In some sense, Frankl’s
conjecture is stripped down to its bare essential parts: the elements have van-
ished and all that counts is the inclusion relation between the sets. Moreover,

6

in comparison with the set formulation new special cases become natural – and
attackable. We will review them next.

3.2 Lattice results

The formulation of the lattice version resulted in a series of veriﬁed special cases
of Frankl’s conjecture. Already in Rival [56] it is mentioned, without proof, that
the conjecture holds for distributive and geometric lattices. This was explicitly
proved by Poonen [50], who also extended the latter case to complemented
lattices.
Abe and Nakano [3] showed the conjecture for modular lattices, a case that
includes distributive lattices. This, in turn, was generalised by Reinhold [52] to
lower semimodular lattices. We present the proof here, as it seems to be the
strongest result concerning lattice classes, and also because the proof is nice and
succinct.
Let x < y be two elements of a lattice. Then x is a lower cover of y if
x ≤ z ≤ y implies x = z or y = z for all elements z. A lattice L is lower
semimodular if a ∧ b is a lower cover of a ∈ L, whenever b ∈ L is a lower cover
of a ∨ b.

Theorem 3 (Reinhold [52]). Lower semimodular lattices satisfy Frankl’s con-
jecture.

Proof. Let L be a lower semimodular lattice with |L| ≥ 2. If the unique largest
element 1 ∈ L is join-irreducible then Frankl’s conjecture is trivially satisﬁed.
If not, we may pick a lower cover b ∈ L of 1, and a join-irreducible a ∈ L with
a ≰ b. Then 1 = a ∨ b.
We claim that the function [a) → L \ [a), x ↦→ x ∧ b is an injection, which
then ﬁnishes the proof. So, suppose that there are two distinct x, y ∈ [a) with
x ∧ b = y ∧ b. As either x ∧ y < x or x ∧ y < y, we may assume the former. This
implies x ∧ b = x ∧ y ∧ b ≤ x ∧ y < x. (1)

Now, as L is lower semimodular, and as b is a lower cover of 1 = x ∨ b, we obtain
that x ∧ b is a lower cover of x. Thus, x ∧ b = x ∧ y by (1) and therefore

a ≤ x ∧ y = x ∧ b ≤ b,

which contradicts our choice of a ≰ b.

Theorem 3 was also independently proved by Herrmann and Langsdorf [30]
and by Abe and Nakano [4]. In the latter article, the conjecture is also veriﬁed
for a superclass, lower quasi-semimodular lattices.
If there are lower semimodular lattices there are clearly upper semimodular
ones as well. However, this class seems to be much harder with respect to
Frankl’s conjecture. Already in Rival [56] it is mentioned, without proof, that
geometric lattices satisfy the conjecture. A proper proof was later given by
Poonen [50]. A lattice is geometric, and then upper semimodular, if it may be

7

represented as the lattice of ﬂats of a matroid. Abe [1] treats another subclass,
the so called strong upper semimodular lattices. Cz´edli and Schmidt [15] show
the conjecture for upper semimodular lattices L that are large, in the sense
that |L| > 5
8 2
m where m is the number of join-irreducible elements; they also
consider planar upper semimodular lattices.
Let us mention that it is an easy consequence of the lattice formulation that,
for any lattice L, Frankl’s conjecture holds for L or for its dual L
∗, or both.
(The dual lattice is obtained by reversing the order.) Duﬀus and Sands [18] and
Abe [2] derive stronger assertions for special classes of lattices.

We close this section with a wonderful application of Reinhold’s theorem
that was indicated to us by one of the anonymous referees. The application
concerns graph-generated intersection-closed families. Let G be a ﬁxed graph.
For every set X ⊆ V (G) we write EX for the set of edges of G that have both
their endvertices in X. Then {EX : X ⊆ V (G)} is intersection-closed.

Theorem 4 (Knill [38]). Given a graph G = (V, E) with at least one edge, the
intersection-closed family {EX : X ⊆ V } satisﬁes the intersection-closed sets
conjecture.

This result is also part of Knill’s PhD thesis [37]. The theorem was later
restated as a conjecture by El-Zahar [19], and, as a response to El-Zahar’s paper,
reproved by Llano, Montellano-Ballesteros, Rivera-Campo and Strausz [42].
As L = {EX : X ⊆ V (G)} is intersection-closed, it is a lattice with respect
to ⊆. We show that L is lower semimodular. Thus, Knill’s theorem becomes a
consequence of Theorem 3.
We call X ⊆ V (G) proper if EX ̸= EX ′ for any X ′ ⊊ X. Note that
L = {EX : X ⊆ V (G) and X is proper}, and so we may restrict our attention
to proper vertex sets. Let X, Y ⊆ V (G) be proper. First we note that

EX ∧ EY = EX ∩ EY = EX∩Y and EX ∨ EY = EX∪Y .

Next we observe that EX is a lower cover of EY if and only if

Y = X + y1 or EY = EX + y1y2 for some y1, y2 ∈ Y \ X.

Indeed, let EX be a lower cover of EY and consider an edge y1y2 ∈ EY \ EX .
Then, EX ⊊ EX∪{y1,y2} ⊆ EY and thus Y = X ∪ {y1, y2}. Now, if one of y1, y2,
y2 say, is contained in X we have Y = X + y1 and we are in the ﬁrst case. If
y1, y2 /∈ X then neither of y1, y2 may have a neighbour in X as otherwise EX
would be a proper subset of EX+y1 or of EX+y2 . The other direction is obvious.
So, assume that for proper A, B ⊆ V (G), the set EB is a lower cover of
EA ∨ EB. Then there are a1, a2 ∈ A \ B so that either A ∪ B = B + a1 or
EA∪B = EB + a1a2. If A ∪ B = B + a1 then A = (A ∩ B) + a1, and EA∩B is a
lower cover of EA. In the other case, when EA∪B = EB + a1a2 we get

EA = EA ∩ EA∪B = (EA ∩ EB) + a1a2 = EA∩B + a1a2,

8

and again EA∩B is a lower cover of EA. Thus, L is lower semimodular, and
Knill’s theorem is proved.

El-Zahar [19] observed that, when Knill’s theorem is generalised to hyper-
graphs, it becomes yet another reformulation of the union-closed sets conjecture.

3.3 The graph formulation

A more recent reformulation of the union-closed sets conjecture is stated in
terms of maximal stable sets of bipartite graphs. A stable set of a graph G is a
vertex subset so that no two of its vertices are adjacent. A stable set is called
maximal if no further vertex of G can be added without violating the stable
set condition. We refer to Diestel [16] for general terminology and notions on
graphs.
The graph formulation of the union-closed sets conjecture is as follows:

Conjecture 5. Any bipartite graph with at least one edge contains in each of
its bipartition classes a vertex that lies in at most half of the maximal stable
sets.

The conjecture was proposed by Bruhn, Charbit, Schaudt and Telle [11],
who also proved the equivalence to Frankl’s conjecture. In analogy to the
intersection-closed sets conjecture, let us call a vertex rare if it is contained
in at most half of the maximal stable sets. Note that for every edge uv of a
bipartite graph, always one of u and v is rare. Indeed, this follows directly from
the fact that no stable set may contain both u and v. Hence, in a hypothetical
counterexample to Conjecture 5, one bipartition class of the graph contains only
rare vertices, while no vertex in the other class is rare.
We sketch why Conjecture 5 and the intersection-closed sets conjecture are
equivalent.

Theorem 6. [11] Conjecture 5 holds if and only if the union-closed sets con-
jecture is true.

Proof. To prove equivalence to the intersection-closed sets conjecture, let us ﬁrst
consider a bipartite graph G with bipartition classes X, Y . By symmetry it is
enough to ﬁnd a rare vertex in X. Let A be the set of maximal stable sets of G.
It is straightforward to check that the traces of maximal stable sets in X, the
set {A ∩ X : A ∈ A}, is intersection-closed. Thus, if the intersection-closed sets
conjecture is true, there must be a rare element x of {A ∩ X : A ∈ A}, which
then is a rare vertex of G.
For the converse direction, let an intersection-closed family A be given. We
may assume that A contains its universe U . We deﬁne a bipartite graph G =
(V, E) on V = A ∪ U with edge set E = {Sx : S ∈ A, x ∈ U, x ∈ S}. That is,
G is the incidence graph of A. See Figure 3 for an illustration.
Then, if B denotes the set of maximal stable sets of G, it follows that A =
{B ∩ U : B ∈ B}. Thus, if x is a rare vertex of G in U , then x is a rare element
of A. This completes the proof.
 9

1 2 3 4 5 6

12346

123456
 12345
 12356
 12456
 13456
 23456
 1234
 1235
 1236
 1456
 2456
 3456
 123
 145
 246
 356
 456
 45
 46
 56
 4 5 6 e

Figure 3: The incidence graph of the intersection-closed family shown in Figure 1

As for the lattice fromulation, we will say that a bipartite graph satisﬁes
Frankl’s conjecture if the graph is not a counterexample to Conjecture 5, or if
it is edgeless.
Figure 3 shows the graph representation of intersection-closed family in Fig-
ure 1. We have to admit that it does not appear very appealing, as listing the
family seems much simpler. Nonetheless, the graph formulation allows for a
very compact representation of Frankl’s conjecture. This is exempliﬁed by the
graph in Figure 4 that encodes the same family as the graph in Figure 3. We
arrive at this graph by iteratively deleting any vertex v whose neighbourhood
is equal to the union of neighbourhoods of some other vertices. It is easy to
check that the resulting graph with v deleted satisﬁes the conjecture only if the
original graph does, see also [11].

123
1 2

3
 246

356

145
 4
4

5

5
 6
 6
 Figure 4: A more succinct representation

3.4 Graph results

The literature on graphs provides a rich selection of natural graph classes, even
bipartite ones, that may now serve as test cases for Frankl’s conjecture. So
far, the conjecture has been veriﬁed for chordal bipartite, subcubic, series-
parallel [11] and, in an approximate version, random bipartite graphs [12]. We
present some of these results here.
 10

A bipartite graph is said to be chordal bipartite if deleting vertices from the
graph can never result in a chordless cycle of length ≥ 6.

Theorem 7. [11] Chordal bipartite graphs satisfy Frankl’s Conjecture.

The proof rests on the local structure of chordal bipartite graphs. This is a
general strategy that we will discuss in more detail in Section 5. The main tool
here is the following lemma, where we denote by N 2(x) the neighbours of the
neighbours of a vertex x (including x).

Lemma 8. [11] Let x, y be two adjacent vertices of a bipartite graph with
N 2(x) ⊆ N (y). Then y is rare.

Proof. Let A denote the maximal stable sets of the chordal bipartite graph G,
and consider A ∈ Ay, that is, a maximal stable set containing y. Since y ∈ A,
no neighbour of y may be in A and hence N 2(x) ∩ A = ∅ as N 2(x) ⊆ N (y).
Therefore, no vertex in N (x) is adjacent with a vertex in A, which implies
N (x) ⊆ A.
We now construct an injective mapping Ay → Ax: given a set A ∈ Ay,
ﬁrst remove all members of N (x) from A and then ﬁll up the resulting set to a
maximal stable set with vertices from N 2(x). Finally, since x is adjacent to y,
we have Ax ⊆ Ay. Altogether, there is an injection Ay → Ay, which means
that y is rare.

To ﬁnish the proof of Theorem 7 it now suﬃces to observe that a type
of vertex known as a weakly simplicical vertex satisﬁes the conditions of the
lemma. That such a vertex always exists in each bipartition class is known from
the literature on chordal bipartite graphs. For details see [11].

Using results of Vaughan on 3-sets and Knill’s graph generated families (dis-
cussed in Sections 5 and 3.2 respectively), we obtain Frankl’s conjecture for
another natural graph class. Recall that a graph is subcubic if every vertex has
degree at most three.

Theorem 9. [11] Every subcubic bipartite graph satisﬁes Frankl’s conjecture.

The third class of graphs we treat are random bipartite graphs, where we can
only prove a slight weakening of Frankl’s conjecture. A random bipartite graph
is a graph on bipartition classes of cardinalities m and n, where any two vertices
from diﬀerent classes are independently joined by an edge with probability p.
For δ > 0, let us say that a bipartite graph satisﬁes Frankl’s conjecture up
to δ if each of its two bipartition classes has a vertex for which the number
of maximal stable sets containing it is at most 1
2 + δ times the total number
of maximal stable sets. We say that almost every random bipartite graph has
property P if for every ε > 0 there is an N such that, whenever m + n ≥ N , the
probability that a random bipartite graph on m + n vertices has P is at least
1 − ε.

Theorem 10. [12] Let p ∈ (0, 1) be a ﬁxed edge-probability. For every δ > 0,
almost every random bipartite graph satisﬁes Frankl’s conjecture up to δ.

The main tool in the proof is the averaging approach detailed in Section 6.

11

3.5 The Salzborn formulation

Returning to the sets point of view, let us present a surprising reformulation
of the conjecture that W´ojcik [72] attributes to Salzborn [61]. Recall that a
union-closed family A is separating if for any two elements of its universe there
is a member-set that contains exactly one of the two. It is easy to check that
A needs to have at least |U (A)| non-empty sets to separate all elements of its
universe. Thus, if ∅ ∈ A then A will have at least |U (A)| + 1 member-sets. It
turns out that the families with this minimum number of member-sets have a
surprisingly rich structure.
Let us call a union-closed family N normalised if it holds that ∅ ∈ N , N
is separating and |U (N )| = |N | − 1. The following conjecture may be found in
W´ojcik [72], or, with less details, in Salzborn [61].

Conjecture 11 (Salzborn [61]). Any normalised family N ̸= {∅} contains a
basis set B of size |B| ≥ 1
2 |N |.

Following W´ojcik [72], we outline why Salzborn’s conjecture implies the
union-closed sets conjecture. Consider a union-closed family A that we may
assume to contain ∅ as a member-set. We deﬁne

A⊈X := {A ∈ A : A ⊈ X} and A
∗ := {A⊈X : X ∈ A}.

It is easy to check that A
∗ is union-closed and separating. We note that X ⊆
Y if and only if A⊈X ⊇ A⊈Y for any X, Y ∈ A. This has several consequences.
Firstly, A⊈X ̸= A⊈Y if X ̸= Y , which implies that |A| = |A∗|. Secondly,
U (A
∗) = A⊈∅ = A \ {∅}. Finally, we remark that A
∗ has the dual lattice
structure of A.
To summarise, A
∗ is normalised and has the same number of members as A.
Next, we consider the basis sets of A
∗.

Every basis set of A
∗ is of the form Ax for some x ∈ U (A). (2)

Indeed, consider a basis set A⊈X of A
∗, and observe that A⊈X = ⋃
y∈U (A)\X Ay.
Pick a smallest set S ⊆ U (A) \ X so that still A⊈X = ⋃
y∈S Ay and consider a
bipartition S1 ∪ S2 = S. Since Ay = A⊈U (Ay), both ⋃
y∈S1 Ay and ⋃
y∈S2 Ay
are members of A
∗. Since A⊈X = ⋃
y∈S1 Ay ∪ ⋃
y∈S2 Ay, A⊈X is the union
of two member-sets of A
∗. As A⊈X is a basis set that implies that already
A⊈X = ⋃y∈Si Ay for i = 1 or i = 2, which by the minimality of S forces
S = Si. Therefore, S has to contain a unique element x, that is, A⊈X = Ax.

Assume now Conjecture 11 to hold. Then the normalised family A
∗ contains
a basis set B∗ with |B∗| ≥ 1
2 |A
∗| = 1
2 |A|.

As B∗ = Ax for some x ∈ U (A) by (2) we deduce that A satisﬁes the union-
closed sets conjecture. We therefore have proved one direction of:

12

Theorem 12 (Salzborn [61]). Conjecture 11 is equivalent to the union-closed
sets conjecture.

We omit the proof of the other direction, which may be found in W´ojcik [72].

Why do we ﬁnd the Salzborn reformulation surprising? At ﬁrst glance,
normalised families seem to be very restricted and in some sense this is true.
For instance, the statement of the union-closed sets conjecture is almost trivial
for them, see Theorem 23. From a lattice point of view, however, normalised
families turn out to be as general as union-closed families. We have already
remarked that A
∗ has the dual lattice structure of A, which directly implies
that every lattice type of a union-closed family is realisable as a normalised
family.
We know only one application of the Salzborn formulation: W´ojcik [72] uses
it to obtain a non-trivial lower bound on the maximum frequency of an element
in a union-closed family; see the next section.
The family A
∗ also appears in Johnson and Vaughan [34], although deﬁned
in a slightly diﬀerent way. In order to obtain a duality result, Johnson and
Vaughan associate to any union-closed family A the dual family A
∗ and then
observe that the union-closed sets conjecture is satisﬁed for at least one of A
and A
∗. We note that the analogous results in the lattice formulation and in
the graph formulation are almost trivial: for lattices this amounts to considering
the dual lattice, and for graphs it reduces to the observation that no stable set
may contain both endvertices of an edge.

The majority of the results on the union-closed sets conjecture are with
respect to the original set formulation. In the remainder of this article we stick
to this formulation as well. However, a good part of the discussed techniques
has a more or less direct analogue in the other formulations.

4 Obstacles to a proof

There are many results on special cases of the conjecture. Amazingly, if we
consider an arbitrary union-closed family, without any special structure or in-
formation on the number of elements, (almost) the best result we have seems
to be a simple observation due to Knill:

Theorem 13 (Knill [38]). Any union-closed family A on n member-sets has an
element of frequency at least n−1
log2(n) .

Proof. We may assume that ∅ ∈ A. Let us choose S ⊆ U (A) minimal such
that every non-empty set of A intersects S. Then for every x ∈ S there is a
A ∈ A with A ∩ S = {x}; otherwise S − x would still meet every non-empty
A ∈ A, which contradicts the minimality of S. As A is union-closed it follows
that {A ∩ S : A ∈ A} = 2S. Hence n ≥ 2
|S| and so |S| ≤ log2(n). As every of
the n − 1 non-empty member-sets of A intersects S, there is an element in S
that belongs to at least (n − 1)/ log2(n) many member-sets of A.

13

W´ojcik [72] improved the bound to 2.4n
log2 n for large n. His proof is not trivial,
but the result is still far from Frankl’s conjecture.

Here are two observations that could be interpreted as signs that the con-
jecture is, after all, perhaps not as hard as thought: normally the most frequent
element appears more often than needed, and there are several abundant ele-
ments. Indeed, the powerful averaging technique discussed in Section 6 builds
solely on these facts.
These observations are due to Poonen, who also found exceptions to them.
Power sets are an obvious example for families in which the maximum frequency
is exactly half the size of the family. Poonen conjectured that, among separating
families, these are the only ones.

Conjecture 14 (Poonen [50]). Let A be a separating union-closed family. Un-
less A is a power set, it contains an element that appears in strictly more than
half of the member-sets of A.

A similar conjecture was oﬀered by Renaud [53]. Moreover, Poonen de-
scribed families with a unique abundant element and again conjectured that
these are the only ones:

Conjecture 15 (Poonen [50]). Let A be a separating union-closed family on
universe U . If A contains a unique abundant element a then

A = {∅} ∪ {B + a : B ⊆ U − a}.

If these conjectures are to be believed, then there is a bit of a margin when
attacking the union-closed sets conjecture. So, why then has the conjecture
withstood more than twenty years of proof attempts?

The obvious ﬁrst approach is to try an induction, for instance on the number
of member-sets. If, given a union-closed family, we could delete one (or two)
basis sets so that the maximum frequency drops then, by induction, the original
family would satisfy the conjecture, too. Unfortunately, this is not always pos-
sible: in a power set of suﬃcient size, deleting one or two basis sets will never
reduce the maximum frequency.
So, naive induction will not succeed. Often, induction can only be made
to work if the hypothesis is strengthened, usually by exploiting some structural
insight. However, we feel that we are lacking in just that. We do not know what
the extremal families look like, those that have minimal maximum frequency
among all union-closed families of a given size. So far, there are not even any
good candidates. We will continue this discussion in Section 8.
A second reason why the conjecture has resisted so long lies in the weakness
of the techniques at our disposal. Let us brieﬂy review the main techniques used
to prove that a given family satisﬁes the conjecture: injections, local conﬁgura-
tions and averaging. In averaging we try to show that the average frequency
is large enough so that some element must be abundant. Averaging is very
powerful but has the drawback that there are families for which the average is

14

simply too low for the method to work. We discuss averaging and its limits
in Section 6. For the local conﬁgurations method one strives to identify small
families so that any large union-closed family containing the small one will au-
tomatically satisfy the conjecture. Unfortunately, given what we know at the
moment it seems doubtful that we will be able to show that any union-closed
family always contains such a local conﬁguration. We will have a closer look at
local conﬁgurations in the next section.
That leaves injections, the simplest of the three techniques. For an almost
trivial example, consider the case when a union-closed family A contains a
singleton, that is, there is an element x so that {x} ∈ A. Then

Ax → Ax, A ↦→ A + x

deﬁnes an injection, which clearly implies that 2|Ax| ≥ |Ax| + |Ax| = |A|.
Consequently, x is abundant. In fact, we have used this method already twice:
once for lower semimodular lattices and then for chordal bipartite graphs. The
main problem with the injection method is that we need to ﬁrst identify an
element that is likely to be abundant.
Sarvate and Renaud [62] were probably the ﬁrst to observe (in print) that
a singleton is always abundant. In a similar way, one of the two elements of
any 2-set is abundant. The pattern, however, breaks with 3-sets. Renaud and
Sarvate [63] describe a family with a unique smallest member-set of 3 elements,
none of which is abundant. Poonen [50] constructs a similar family, a generali-
sation of which we present here:
For each k ≥ 3 we deﬁne a union-closed family A
k with the property that
[k] is the unique smallest set, but no element of [k] is abundant. For this, we
use Poonen’s notation A ⊎ B for two set families A and B to denote the family

A ⊎ B := {S ∪ T : S ∈ A, T ∈ B}.

Now let
 A
k = {[k]} ∪
 k⋃

i=1
({∅, {i}, [k]} ⊎ Bi) ∪ (2[k] ⊎ [k + 1, 3k]),

where
 Bi = {[k + 1, 3k] \ {2i + 2}, [k + 1, 3k] \ {2i + 3}} for every i ∈ [k].

Note that the set [k] is the unique smallest set in A. In total, A
k contains
1+6k +2
k many sets, but every i ∈ [k] is contained in exactly 1+(2k +2)+2
k−1

sets of A. Therefore, no element of [k] is abundant.

Poonen’s family highlights one of the major obstacles on the way to a proof of
the union-closed sets conjecture: we do not know where to expect an abundant
element. However, there are special cases where this is known. We treat these
cases next.
 15

5 Local conﬁgurations

Sarvate and Renaud [62] observed that any singleton in a union-closed family
is abundant, and of the two elements of a 2-set at least one is abundant. This
motivates the search for good local conﬁgurations: a family L on few elements
so that any union-closed family A containing L has an abundant element among
the elements of L. Poonen [50] gives a complete characterisation of such families:

Theorem 16 (Poonen [50]). Let L be a union-closed family with universe [k].
The following statements are equivalent:

(i) Every union-closed family A containing L satisﬁes the union-closed sets
conjecture. In particular, A has an abundant element in [k].

(ii) There are reals c1, c2, . . . , ck ≥ 0 with ∑k
i=1 ci = 1 such that for every
union-closed family K ⊆ 2
[k] with K = L ⊎ K it holds that

k∑

i=1 ci|Ki| ≥ 1
2 |K|.

We stress that (ii) is indeed a local condition: for ﬁxed k there are only
ﬁnitely many such families K. As an application of his theorem, Poonen showed
that the union-closed family consisting of a 4-set together with any three distinct
3-subsets satisﬁes the conditions of his theorem. This was later generalised by
Vaughan [67] to three distinct 3-sets with a non-empty common intersection. As
mentioned in Section 3.4, Vaughan’s result is used to prove Frankl’s conjecture
for subcubic bipartite graphs.
A union-closed family L as in Theorem 16 is called Frankl-complete by
Vaughan [66], FC for short. Several FC-families are listed in [66], for exam-
ple a 5-set together with all its 4-subsets or a 6-set with all 5-subsets and eight
4-subsets. The list was later extended by Morris [46], who, in particular, com-
pletely characterised the FC-families on at most 5 elements.
To study FC-families in a more quantitative way, Morris [46] introduced the
function FC(k, m) deﬁned as the smallest r for which the set of every r of the
k-sets in [m] generates an FC-family. He showed that ⌊ m
2 ⌋ + 1 ≤ FC(3, m),
while Vaughan [67] gave an upper bound of FC(3, m) ≤ 2m
3 . A proof of Morris’
conjecture that FC(3, m) = ⌊ m
2 ⌋ + 1 was announced by Vaughan [65], but has
apparently never been published.
Mari´c, ˇZivkovi´c and Vuˇckovi´c [44] veriﬁed some known FC-families and found
a new one using the automatic proof assistant Isabelle/HOL. For this, they
formalised the condition of FC-families to enable a computer search. As a
result, we know now that all families containing four 3-subsets of a 7-set are
FC-families.

5.1 Small ﬁnite families

The union-closed sets conjecture has been veriﬁed for families on few member-
sets or few elements. The current best results use local conﬁgurations to reduce

16

the number of special cases substantially.
With respect to the size of the universe, the conjecture has to-date been
veriﬁed up to m = 12:

Theorem 17 (ˇZivkovi´c and Vuˇckovi´c [68]). The union-closed sets conjecture
holds for union-closed families on at most 12 elements.

The following result, that has not been improved upon in the last twenty
years, allows to leverage bounds on the universe size to bounds on the number
of member-sets:

Lemma 18 (Lo Faro [22]). Under the assumption that the union-closed sets
conjecture fails, let m denote the minimum cardinality of |U (A)| taken over all
counterexamples A to the union-closed sets conjecture. Then any counterexam-
ple has at least 4m − 1 member-sets.

The lemma was later rediscovered by Roberts and Simpson [58]. Together
with Theorem 17 we obtain:

Corollary 19. The union-closed sets conjecture holds for union-closed fami-
lies with at most 50 sets.

Various authors veriﬁed the conjecture for small values of n and m, where
as usual n is the number of member-sets and m the size of the universe. The
ﬁrst were Sarvate and Renaud [62] who treated a close variant that excludes the
empty set. In a ﬁrst paper they covered all cases up to n ≤ 11; in Sarvate and
Renaud [63] the case analysis was pushed up to n ≤ 19. Using his Theorem 16,
Poonen improved the bounds to m ≤ 7 and n ≤ 28. This was followed by Lo
Faro [22], who settled the union-closed sets conjecture for m ≤ 9 and n ≤ 36. For
this, he investigated several necessary conditions on a minimal counterexample,
among them Lemma 18 above. Roberts [57] shows the conjecture up to n ≤ 40.
Using the list of known FC-families, Morris [46] proved the union-closed sets
conjecture for families with m ≤ 9 and n ≤ 36, apparently unaware of the
older result by Lo Faro [22]. Nevertheless, there is merit in Morris’ proof as it
showcases how FC-families may be used to substantially reduce the number of
cases. This method is at the heart of all subsequent work in this direction.
In order to prove the conjecture for m ≤ 10, Markovi´c [45] imitated the
method of Theorem 16: he assigns non-negative weights to the elements of A
and extends this to the member-sets of A. He then observes that a total weight
of the member-sets of at least 1
2 n times the weight of the universe is suﬃcient
for the union-closed sets conjecture. As a by-product of this method, Markovi´c
discovered a number of new FC-families.
Boˇsnjak and Markovi´c [10] improve upon [45] by developing more general
local conﬁgurations that allow them to verify the conjecture up to m = 11. With
a very similar method and the use of a computer, ˇZivkovi´c and Vuˇckovi´c [68]
pushed this to m ≤ 12.
 17

6 Averaging

Obviously, a union-closed family A has an element of frequency ≥ 1
2 |A| if the
average frequency is at least 1
2 |A|. In other words, if

1
|U (A)| · ∑

u∈U (A) |Au| ≥ 1
2 |A|, (3)

then A satisﬁes the union-closed sets conjecture.
So far, not much is gained. Calculating ∑

u∈U (A) |Au| directly is clearly out
of question, as this would presuppose knowledge about the individual frequen-
cies |Au|. Fortunately, this is not necessary, as the sum of frequencies can be
determined indirectly with a simple double-counting argument:
∑

u∈U (A) |Au| = ∑

A∈A |A|. (4)

This identity is the heart of the averaging method. The total set size is usually
much easier to control, and in some cases may be estimated quite well.
Combining (3) and (4), a condition equivalent to (3) is that

1
|A| · ∑

A∈A |A| ≥ 1
2 |U (A)|.

That is, if the average set size of A is at least half the size of the universe then
A again satisﬁes the union-closed sets conjecture.
As discussed in Section 4, it is not obvious where to look for an abundant
element. The averaging method has the clear advantage that it simply sidesteps
this obstacle. In this section we describe how both (3) and (4) lead to some of
the strongest results on the union-closed sets conjecture.

6.1 Large families

In a clearly overlooked paper, Nishimura and Takahashi [47] prove for the ﬁrst
time that the union-closed sets conjecture always holds for large families. Their
proof uses the average set size argument: it is shown that the average set size
is greater than m
2 , which implies that there is an abundant element.

Theorem 20 (Nishimura and Takahashi [47]). Let A be a union-closed family of
more than 2
m − 1
2 √2m member-sets on a universe of size m. Then A satisﬁes
the union-closed sets conjecture.

Proof. Suppose there is a set S ⊆ U (A) with S /∈ A but |S| ≥ m
2 . Then for any
subset R ⊆ S with R ∈ A it holds that S \ R /∈ A. Thus, at least half of the
subsets of S are missing in A. This gives |A| ≤ 2
m − 1
2 · 2 m
2 , a contradiction.
Hence, every set S ⊆ U (A) of size at least m
2 is contained in A. This means
that the average set size is at least m
2 , ﬁnishing the proof.

18

Cz´edli [13] employed some involved lattice-theoretic arguments to push the
bound from 2
m − 1
2 √2m to 2m − √2m. A weaker result than Nishimura and
Takahashi’s was proved by Gao and Yu [27]. Recently, a serious improvement of
the above bound was given by Balla, Bollob´as and Eccles [9], which we present
in Section 6.4.

6.2 Bounds on the average

Averaging does not always work. It is easy to construct union closed families
with an average frequency and average set size that is too low to deduce the
union-closed sets conjecture. Reimer [51] gave a bound on the average set size
that is in some respect best possible.

Theorem 21 (Reimer [51]). Let A be a union-closed family on n sets. Then

1
n · ∑

A∈A |A| ≥ log2 n
2 . (5)

The result is too weak for Frankl’s conjecture as usually log2(n) < m. In
terms of the average frequency, Reimer’s bound reads as

1
m · ∑

u∈U (A) |Au| ≥ log2 n
m · n
2 . (6)

We discuss the beautiful proof of Theorem 21 in Section 6.4.
We now focus on separating union-closed families, where for every two ele-
ments there is a set containing exactly one of them. As explained in Section 2,
for the purpose of the union-closed sets conjecture it is not a restriction to
consider only separating families.

Theorem 22 (Falgas-Ravry [20]). Let A be a separating union-closed family on
m elements. Then 1
m · ∑

u∈U (A) |Au| ≥ m + 1
2 . (7)

He remarks that this bound is stronger than Reimer’s bound if m > √
n log2 n.
The proof of (7) is rather simple:

Proof. Assume that the elements 1, 2, . . . , m of U (A) are labelled in order of
increasing frequency. As A is separating, this ordering ensures that for any
1 ≤ i < j ≤ m there is a set Xij ∈ A such that i /∈ Xij and j ∈ Xij. For all
1 ≤ i ≤ m − 1 let Xi = ⋃m
j=i+1 Xij, and put X0 := U (A). Observe that (a) the
Xi are all distinct and that (b) [i + 1, m] ⊆ Xi. Thus, the statement follows
from ∑

u∈U (A) |Au| (a)
≥
 m−1∑

i=0 |Xi| (b)
≥
 m−1∑

i=0 (m − i) = m(m + 1)
2 .

19

Let us point out an easy consequence of the proof. As Nishimura and Taka-
hashi observed, the union-closed sets conjecture holds for families that are very
large with respect to their universe. Here we obtain the analogous result for
very small families:

Theorem 23. Any separating family on m elements with at most 2m member-
sets satisﬁes the union-closed sets conjecture.

Proof. Each of the m sets Xi as constructed above contains the most frequent
element xm.

We note that this is a weaker bound than the one obtained by Lo Faro
for a minimal counterexample (Lemma 18): n ≤ 4m − 1. However, Lo Faro’s
techniques do not extend easily to small families and there is a good reason
for this. If the factor in Theorem 23 can be improved to c > 2 then we may
deduce that there is always an element whose frequency is a constant fraction
of the number of member-sets. This natural weakening of the union-closed sets
conjecture is still very much open.

Theorem 24 (Hu [31]). Suppose there is a c > 2 so that any separating union-
closed family A
′ with |A
′| ≤ c|U (A
′)| satisﬁes the union-closed sets conjecture.
Then, for every union-closed family A, there is an element u of frequency

|Au| ≥ c − 2
2(c − 1) |A|.

The theorem is proved along the following lines: by cloning some element,
the universe U of A is enlarged to U ′. At the same time, we add sets of the form
U ′ − x in order to separate the clones from each other. The resulting family A
′

is then separating and will be made to have size |A′| ≤ c|U ′|. Now an element
of frequency ≥ 1
2 |A′| will still have high frequency in A.

Falgas-Ravry also gives a family of separating union-closed families which
shows that the combination of the bounds (5) and (7) is close to optimal, in
the sense that the sum of both bounds can serve as an upper bound on the
minimum possible weight of a separable union-closed family. For this, he calls
a pair (m, n) satisﬁable if there is a separating union-closed family with n sets
on a universe of m elements.

Theorem 25 (Falgas-Ravry [20] and Reimer [51]). Let (m, n) be a satisﬁable
pair of integers. Let A be a union-closed family on m elements and n sets of
minimal average frequency. Then

max ( n log2 n
2m , m + 1
2
 ) ≤ 1
m · ∑

u∈U (A) |Au| ≤ n log2 n
2m + m + 1
2 + n
m . (8)

To establish the upper bound in Theorem 25, Falgas-Ravry uses a construc-
tion not unlike that of Duﬀus and Sands [18] that we discuss below.

20

6.3 Limits of averaging

In the framework of the lattice formulation, Cz´edli, Mar´oti and Schmidt [14]
construct for every size m of the universe a family of ⌊ 2
3 2
m⌋ members, for which
averaging fails. We present here a lattice-free version of their family and a short
and elementary proof that the average is always too small.
On the set N<ω of ﬁnite subsets of the positive integers, let < be the order
deﬁned by ﬁrst sorting by increasing largest element and then by reverse colex
order. In other words, we set A < B if

• max A < max B; or

• max A = max B but max(A∆B) ∈ A

for ﬁnite A, B ⊆ N.
As an illustration, here is the initial segment of the order, where we write
124 for the set {1, 2, 4}:

∅ < 1 < 12 < 2 < 123 < 23 < 13 < 3 < 1234 < 234

< 134 < 34 < 124 < 24 < 14 < 4 < 12345 < ...

For any positive integer n, deﬁne the Hungarian family H(n) to be the inital
segment of length n of N<ω under <. It is easy to check that H(n) is union-closed
and that its universe is [⌈log2 n⌉].

Theorem 26 (Cz´edli, Mar´oti and Schmidt). For the Hungarian family on [m]
of size n = ⌊ 2
3 2
m⌋ 1
m · ∑

i∈[m] |H(n)
i | < |H(n)|
2 .

for any m > 1.

Proof. The key to the proof are the simple and well-known identities

⌊ 2
3 2m⌋ = 2m+1 − 1
3 = 2
m−1 + 2m−3 + . . . + 4 + 1 if m odd. (9)

⌊ 2
3 2m⌋ = 2m+1 − 2
3 = 2
m−1 + 2m−3 + . . . + 8 + 2 if m even. (10)

Put k = ⌊ m−1
2 ⌋. Denote by I0 the initial segment of N<ω of length 2m−1,
by I1 the set of the next 2
m−3 sets in the order, by I2 the following 2
m−5 sets
and so on until we reach Ik.
Clearly, |Ii| = 2m−(2i+1) and H(n) = I0 ∪ I1 ∪ . . . ∪ Ik. Moreover, we can
see that I0 = 2[m−1] and that for i ≥ 1, the set Ii is the set of all X ⊆ [m]
that contain all of m − 1, m − 3, . . . , m − (2i − 1) and of m, m − 2i, but none of
m − 2, m − 4, . . . , m − (2i − 2).
Thus, an element m−(2i−1) appears in half of the members of I0 ∪. . .∪Ii−1
and in all of the sets in Ii ∪ . . . ∪ Ik. Its frequency is therefore

|H(n)
m−(2i−1)| = 1
2 (|I0| + . . . + |Ii−1|) + |Ii| + . . . + |Ik|. (11)

21

An element m − 2i is contained in half of the sets of I0 ∪ . . . ∪ Ii−1, in all of
the sets in Ii but in none of Ii+1 ∪ . . . ∪ Ik. Its frequency is

|H(n)
m−2i| = 1
2 (|I0| + . . . + |Ii−1|) + |Ii|. (12)

Moreover, we observe that m lies in all of sets of H(n) but those in I0.
For the ﬁnal argument, we assume m to be even, that is m = 2k + 2. The
case of odd m is very similar. With (11) and (12), we obtain

m∑

j=1 |H(n)
j | = |H(n)
m | +
 k∑

i=1
 (|H(n)
m−(2i−1)| + |H(n)
m−2i|
) + |H(n)
1 |

= |H(n)| − |I0| +
 k∑

i=1
 (
|H(n)| + |Ii|
) + 1
2 |H(n)|

= (k + 1)|H(n)| − 2|I0| + 3
2 |H(n)|

= m
2 |H(n)| − 2
m + 3
2 · 2m+1 − 2
3 = m
2 |H(n)| − 1,

where we used (10) in the penultimate step.

So, the averaging method can never yield the union-closed sets conjecture
in its full generality. Might it perhaps be possible to at least obtain the natural
relaxation, in which we only ask for an element that appears in ≥ 1% of the
member-sets? As Duﬀus and Sands [18] observed, not even this more modest
aim may be attained just by averaging. We present here their construction.
Let V be a set of size 2t, and W = {w1, . . . , w2t} be a disjoint set of 2t

elements. Put
 A = 2
V ∪ {V ∪ {w1, . . . , wi} : i = 1 . . . , 2
t}.

Then A is a (separating) union-closed family of size |A| = 2
2t + 2t on a universe
U = V ∪ W of size 2t + 2t. Averaging yields

1
|U | · ∑

u∈U
 |Au|
|A| = 2t(22t−1 + 2t) + ∑2
t

i=1(2t − i + 1)
(2t + 2t)(22t + 2t)

= 2t(22t−1 + 2t) + 2t−1(2
t − 1)
(2t + 2t)(22t + 2t) → 0 as t → ∞,

as the largest summand in the numerator is t2
2t, while the largest one in the
denominator is 2
3t. This shows that an averaging argument cannot always
guarantee an element of frequency at least c|A| for any c > 0.

22

6.4 Up-compression

We now outline Reimer’s proof of Theorem 21 because it uses a common tech-
nique in extremal combinatorics: shifting or compression. We ﬁrst restate the
theorem.

Theorem 21 (Reimer [51]). Let A be a union-closed family on n sets. Then

1
n · ∑

A∈A |A| ≥ log2 n
2 .

Compression subjects the given initial object (the union-closed family), to
small incremental changes until a simpler object is reached (an up-set), while
maintaining the essential properties of the initial object. Variants of compression
have been used by Frankl in order to prove the Kruskal-Katona theorem [25] and
in the context of traces of ﬁnite sets [24]. The technique is also used by Alon [5]
and various others; see Kalai’s blog post [35] for an enlightening discussion.
Returning to Reimer’s proof we deﬁne the up-compression of a union-closed
family A. For this, consider an element i, and deﬁne

ui(A) =
 {A + i if A + i /∈ A
A otherwise,

for every A ∈ A. Then it turns out that the up-compressed family ui(A) :=
{ui(A) : A ∈ A} is still union-closed. Moreover, iteratively applying up-
compression for every element i in the universe of A results in an up-set: a
family U on universe U for which X ∈ U and X ⊆ Y ⊆ U implies Y ∈ U. We
may always assume A to have universe [m]. We then write u(A) for the iterated
up-compression um ◦ . . . ◦ u1(A).

Lemma 27 (Reimer [51]). Let A be a union-closed family on universe U . Then

(i) ui(A) is union-closed for any i ∈ U ; and

(ii) u(A) is an up-set.

What have we gained? The key to the averaging technique is to control the
total set size ∑
A∈A |A|. For an up-set the total set size can be given in a closed
form. Deﬁne the edge boundary of an up-set U on a universe U to be

EB(U) = {(A, A + i) : A /∈ U, i ∈ U and A + i ∈ U}.

Now

Lemma 28 (Reimer [51]). Let U be an up-set on m elements. Then

2 ∑

A∈U |A| = m|U| + |EB(U)|.

23

In order to ﬁnish Reimer’s proof we need to see that the second essential
part of the compression argument holds: that the object does not change too
much during compression. Here this means that the total set size has controlled
growth.

Lemma 29 (Reimer [51]). Let A be union-closed family. Then

(i) ∑

A∈A |u(A) − A| ≤ |EB(u(A))|; and

(ii) ∑

A∈A |u(A) − A| ≤ |A|(m − log2(|A|)).

Proof of Theorem 21. Applying the previous lemmas we obtain

2 ∑

A∈A |A| = 2 ∑

A∈A |u(A)| − 2 ∑

A∈A |u(A) − A|

≥ m|u(A)| + |EB(u(A))| − 2 ∑

A∈A |u(A) − A|

≥ m|A| + |EB(u(A))| − |EB(u(A))| − |A|(m − log2(|A|))

= |A| · log2(|A|).

Reﬁning Reimer’s approach, Balla, Bollob´as and Eccles improve substan-
tially on Nishimura and Takahashi’s observation that large union-closed families
never pose a counterexample to Frankl’s conjecture.

Theorem 30 (Balla, Bollob´as and Eccles [9]). Any union-closed family on m
elements with at least ⌈ 2
3 2
m⌉ member-sets satisﬁes the union-closed sets conjec-
ture.

In fact, Balla et al. prove that the average frequency of such a family A is
always at least |A|
2 . In view of Theorem 26 this is best possible.
The key idea of the proof of Theorem 30 is to exploit the Kruskal-Katona the-
orem in conjunction with up-compression. This allows to show that, among all
union-closed families on n member-sets, the Hungarian family H(n) has minimal
total set size. Since the total set size of H(n) is large, provided that n ≥ ⌈ 2
3 2
m⌉,
the double-counting argument (4) then yields an average frequency that is large
enough to imply the union-closed sets conjecture for the given family.

Up-compression, and in particular, the eﬀect of the order in which the ele-
ments i of the universe are chosen for the up-compression is further investigated
by Rodaro [59]. In a fairly involved article with a heavy algebraic ﬂavour he
arrives at an upper-bound on the number of basis sets of the union-closed fam-
ily. (Recall that a non-empty B ∈ A is a basis set if B = A ∪ A′ for A, A
′ ∈ A
implies A = B or A′ = B.) Rodaro’s bound, however, is weaker than a result
of Kleitman from 1976 on set families that are union-free. Cast in the language
of basis sets of a union-closed family the result becomes:

24

Theorem 31 (Kleitman [36]). Let A be a union-closed family on m elements.
Then the number of basis sets is at most
( m
⌊ m
2 ⌋
) + 2
m

m .

While it is not clear how sharp the bound is, a family with ( m
⌊ m
2 ⌋) basis sets

is easily found: simply take all subsets of 2
[m] of size at least ⌊ m
2 ⌋.

Up-compression is clearly a powerful concept. So, it seems enticing to apply
the method in a more direct way to attack Frankl’s conjecture: given a union-
closed family A, choose an element i in its universe and apply up-compression
with respect to i, and then reduce the problem to the hopefully simpler family
ui(A). Unfortunately, the up-compressed family ui(A) is much too simple with
respect to the union-closed sets conjecture: the family satisﬁes it for trivial
reasons. Indeed, the element i always appears in at least half of the member-
sets of ui(A).
Lo Faro [22] found a way to circumvent this. Call an element y dominated
by x if y ∈ A ∈ A implies x ∈ A—in other words, when Ay ⊆ Ax. Then we
may apply up-compression with respect to y selectively to the sets in Ax. That
is, we set
 u
′
y(A) :=
 {A + y if A ∈ Ax and A + y /∈ A
A otherwise.

The resulting family A
′ := u
′
y(A) is still union-closed. Moreover, the frequency
of y is bounded by the frequency of x, which has not changed. If A
′ satisﬁes
the union-closed sets conjecture then this is also the case for the original family
A. Thus, this restricted up-compression allows to force more structure without
augmenting the frequency. While Lo Faro manages to exploit this technique in
order to obtain a bound on a minimal counterexample it is not clear whether it
or a variant may be used to a more far-reaching eﬀect.
We note that up-compression is also used by Leck and Roberts [40] in the
context of the union-closed sets conjecture.

6.5 Generalised averages

We saw in the previous section that the Hungarian family H(n) has minimum
total set size among all union-closed families with n member-sets. Leck, Roberts
and Simpson [41] study a more general set-up, in which they allow the set
sizes to be weighted. For this, they consider non-negative weight functions
w : 2[m] → R≥0 that are constant on all sets of the same size. That is, there
are reals wi ≥ 0 so that w(X) = wi if |X| = i, for every X ⊆ [m]. Moreover,
the weights are non-decreasing with i, meaning w0 ≤ w1 ≤ . . . ≤ wm. The
weight of a non-empty union-closed family A is then deﬁned as ∑

A∈A w(A).
For example, if wi = i for all i ∈ [0, m], then w(A) is just the total set size.
For families generated by 2-sets, Leck et al. managed to determine the ex-
tremal families. These families turn out to be independent of the actual weight.

25

In contrast to above, where we used the reverse colex order we need here the
standard colex order: if X, Y ⊆ [m] are distinct then X < Y if and only if
max(X∆Y ) ∈ Y . Then, we deﬁne Uk to be the union-closure of the ﬁrst k
distinct 2-sets in the colex order. For any weight w, Leck et al. calculate the
weight of Uk to be a+2∑

i=2
 ((a + 1
i
 ) − (
a − b
i − 1
)) · wi,

where a and b are any integers such that 0 ≤ b ≤ a and k = (a
2) + b.

Theorem 32 (Leck, Roberts and Simpson [41]). For every k and every weight w,
the family Uk has minimum weight w(Uk) among all union-closed families gen-
erated by k distinct 2-sets.

A partial result of this had already been proved by Imrich, Sauer and
Woess [33], ﬁrst mentioned in their technical report [32], which showed that
any union-closed family A that is generated by basis sets of size 2, has an
average set size of at least 1
2 |U (A)|.

As we observed in Section 6.3, averaging does not always succeed, that is,
the arithmetic mean of the frequencies is sometimes too low to conclude that
the union-closed sets conjecture holds for a given family. For some families, such
as the Hungarian family discussed above, this is because there is one or perhaps
a few elements with very low frequency. Those elements might be so rare that,
on the whole, the average frequency drops below the Frankl threshold of half of
the member-sets.
One way to overcome this obstacle is to use a diﬀerent mean than the arith-
metic mean, one that de-emphasises the weight of extremely rare outliers. This
approach has been pursued by Duﬀus and Sands [18]. While they consider a
quasi-arithmetic mean for the lattice formulation, we present here the equivalent
form in the set formulation. In particular, Duﬀus and Sands pose the question
whether there is a c > 1 so that

1
|U |
 ∑

u∈U c|Au| ≥ c
 |A|
2 (13)

for all union-closed families A with universe U . Clearly, (13) would imply the
union-closed sets conjecture. As evidence, Duﬀus and Sands prove that the
lattice version of (13) holds for distributive lattices when c = 4.

While (13) seems quite enticing, a new idea is needed to make this, or some
other, generalised average work. Indeed, it is no longer obvious how the main
advantage of the averaging approach can be exploited, namely that the frequen-
cies are analysed indirectly via the set sizes. In the case of distributive lattices,
Duﬀus and Sands could investigate the individual frequencies |Au| to arrive at
their result. In general, this will not be possible. For, if it was, then there would
be no need to consider a quasiarithmetic mean (or of any other kind), as one
could immediately exhibit an abundant element.

26

6.6 Families of minimum density

Rather than averaging the frequencies over the whole universe, we may hope to
gain more by restricting the range of the average, for example to the elements
of the smallest member-set. This approach was developed by W´ojcik [71] and
followed up by Balla [8].
Deﬁne sk to be the largest real so that for any union-closed family A and
any k-set S in A it holds that
1
|S|
 ∑

u∈S |Au| ≥ sk|A|. (14)

The ﬁrst 10 values have been determined exactly by W´ojcik; we list here the
ﬁrst ﬁve: s1 = 1
2 , s2 = 1
2 , s3 = 4
9 , s4 = 2
5 and s5 = 9
25 . So, in particular, any
5-set in any union-closed family will always contain an element that appears in
at least a third of the member-sets.
Somewhat surprisingly, the value sk coincides with the so-called minimal
density of a family on k elements:

Theorem 33 (W´ojcik [71]). For every k ∈ N it holds that

sk = min
A 1
k|A| · ∑

u∈U (A) |Au|,

where the minimum ranges over all union-closed families A with |U (A)| = k.

We mention that we have reversed here deﬁnition and consequence, as W´ojcik
deﬁnes the sk as minimal densities but then proves the equivalence to (14).
W´ojcik conjectured and Balla proved that:

Theorem 34 (Balla [8]). For all k, sk ≥ log2 k
2k .

The main step in the proof is an application of Reimer’s theorem. As
W´ojcik [71] indicated, this lower bound is asymptotically optimal. To see this,
consider the family 2
[r] ∪ [k], where r = ⌈log2 k⌉, and observe that its density is
(1 + o(1)) log2 k
2k . Note, however, that this family is not separating.
Combining Theorems 33 and 34, Balla arrives at a lower bound on the
maximum frequency in terms of the size of the universe.

Corollary 35 (Balla [8]). In every union-closed family on m ≥ 16 elements and

n sets there is an element contained in at least √ log2 m
m · n
2 many member-sets.

7 Further results

Sarvate and Renaud [62] observed that if the union-closed sets conjecture holds
for union-closed families on n sets, n odd, then it holds for union-closed fam-
ilies with n + 1 sets. In particular, n0 is odd. Lo Faro [22] and later Roberts

27

and Simpson [58] proved n0 ≥ 4m0 − 1. As discussed earlier, this result turns
out to be very useful for families on few sets.
Another result in this direction is given by Norton and Sarvate [48]: any
counterexample with n0 sets contains at least three distinct elements of fre-
quency exactly n0−1
2 . Other necessary properties of counterexamples were given
by Lo Faro [21, 22] and Dohmen [17].

Peng, Sissokho and Zhao [49] study what they call the half-life of set families.
Given a set family B that is not necessarily union-closed, they consider the family⋃k B deﬁned as the family of unions of at most k sets of B. The half-life of B is
then the least k such that ⋃k B satisﬁes the assertion of the union-closed sets
conjecture.

8 Extremal frequency

Any induction proof of the union-closed sets conjecture will likely necessitate
a strengthened induction hypothesis coupled with structural insight on those
families with low maximum frequencies. Let us therefore look at the minimal
maximum element frequency a family on a given number of sets may have.
For a union-closed family A deﬁne φ(A) to be the maximum frequency of
an element of the universe, that is,

φ(A) = max
u∈U (A) |Au|.

Let φ(n) be the minimum over all φ(A), where A is a union-closed family of
n ≥ 2 member-sets. Clearly, this allows the trivial reformulation of the union-
closed sets conjecture as:

Conjecture 36. φ(n) ≥ n
2 for all integers n ≥ 2.

In this way, the union-closed sets conjecture becomes a problem about an
integer sequence. What can be said about this sequence φ(n)? For instance,
that it is a slowly growing sequence:

Lemma 37 (Renaud [53]). φ(n − 1) ≤ φ(n) ≤ φ(n − 1) + 1 for all n ≥ 2.

Renaud3 used the lemma to compute the ﬁrst 17 values of φ(n). We put
φ(1) = 1 so that the sequence starts from n = 1 on:

1, 1, 2, 2, 3, 4, 4, 4, 5, 6, 7, 7, 8, 8, 8, 8, 9, 10, ... (15)

Moreover, if the union-closed sets conjecture is true, then φ(n) = n
2 if n is a
power of two, and φ(n) > n
2 otherwise, provided Poonen’s conjecture (Conjec-
ture 14) is valid as well.
Now, there is a well-known slowly growing integer sequence that coincides
with φ(n) on the initial segment (15) and that, in addition, has a(n) = n
2 if

3We point out here that our sequence φ(n) equals Renaud’s [53] φ(n − 1).

28

and only if n is power of two. This is Conway’s challenge sequence, deﬁned by
a(1) = a(2) = 1 and the recurrence relation

a(n) = a(a(n − 1)) + a(n − a(n − 1)).

See, for instance, Kubo and Vakil [39] for background on the sequence.
As Mallows [43] proved that a(n) ≥ n
2 for all n ≥ 1, it seems tempting to
seek a deeper relation between φ(n) and a(n), and in some sense there is one.
Renaud and Fitina construct, for every n, a union-closed family whose maximum
element frequency is exactly equal to a(n). We discuss this construction next.
Let us deﬁne an order < on N(<ω), the set of ﬁnite subsets of N, by ﬁrst
sorting by largest element, then by decreasing cardinality and ﬁnally by colex
order. Thus, A < B if

• max A < max B; or
• max A = max B but |A| > |B|; or
• max A = max B and |A| = |B| but max(A∆B) ∈ B

Omitting parentheses and commas this yields

∅ < 1 < 12 < 2 < 123 < 13 < 23 < 3 < 1234 < 124

< 134 < 234 < 14 < 24 < 34 < 4 < 12345 < ...

as initial segment. It is easy to see that A ≤ C and B ≤ C implies A ∪ B ≤
C, which means that the ﬁrst n sets of this order form a union-closed family,
denoted by R(n).

Theorem 38 (Renaud and Fitina [55]). For every n ≥ 2, the most frequent
element of the Renaud-Fitina family R(n) has frequency a(n), that is,

φ(n) ≤ a(n).

So, is φ(n) always equal to a(n)? By Mallows’ result, that would clearly
prove the union-closed sets conjecture. Unfortunately, this is not the case. In a
subsequent paper, Renaud [54] described families B(n) whose element frequency
is sometimes strictly smaller than Conways’ challenge sequence. This happens
for the ﬁrst time at n = 23, where a(n) = 14. However, no element in the family

B(23) = 2[4] ∪ {12345, 1235, 1245, 1345, 2345, 125, 345}

on 23 member-sets appears more often than 13 times. We omit the precise
construction of B(n) but mention that it only diﬀers from R(n) in the last step,
when we delete sets of the same size of the power set 2
[m]. There the sets to
delete are chosen in a more balanced way, so that the frequency of the elements
1, . . . , m − 1 diﬀers by at most one.
Renaud determines the maximum frequency as follows. Let

n = 2
m −
 r−1∑

i=0
 (
m − 1
i
 ) − v,

29

where 0 ≤ r < m − 1 and 0 ≤ v < (m−1
r ). Then

φ(B(n)) = 2
m−1 −
 r−2∑

i=0
 (
m − 1
i
 ) − ⌊ rv
m − 1
 ⌋

Furthermore, he shows that always φ(B(n)) ≤ a(n). Are the families B(n) now
truly extremal, that is φ(n) = φ(B(n)) for all n? Again, this is not the case.
Renaud gives the example of the family

C = 2
[6] \ {6, 5, 16, 25, 36, 45, 136, 245},

in which the most frequent element appears in 30 member-sets. However, in
B(56) there is an element of frequency 31.

To conclude, we do not know much, in general, about the structure of an
extremal family, nor are there any convincing candidates. The only exception
are power sets P, for which holds φ(P) = φ(|P|), provided the union-closed sets
conjecture is true. Nevertheless, the examples in this section seem to indicate
that an extremal family would have relatively few elements compared to the
number of member-sets: let us call a family on n member-sets and a universe of
size m compact if 2m−1 < n ≤ 2m. For example, power sets, the Renaud-Fitina
families as well as the Hungarian families are compact.

Question 39. Is it true that for a union-closed family A it follows from φ(A) =
φ(|A|) that A is compact?

An aﬃrmative answer would be a major step towards the union-closed sets
conjecture. Indeed, Reimer’s bound (6) in conjunction with Theorem 17 gives:

Observation 40. Any compact union-closed family A contains an element that
is contained in at least 6
13 |A| member-sets.

While we have arrived at the end of this survey, the union-closed sets con-
jecture still has a bit of a journey ahead of it. We hope it will be an exciting
trip.

Acknowledgement

We are grateful for the extensive bibliography of Markovi´c [45] that was of great
help for our own literature research. We thank Bela Bollob´as, Dwight Duﬀus,
Peter Frankl, Tomasz  Luczak, Ian Roberts, Jamie Simpson, Peter Winkler and
David Yost for their input on the history of the conjecture and for help in
tracking down seemingly lost items of the literature. We thank Eric Balandraud
for inspiring discussions about the Hungarian family. Finally, we thank the
referee who pointed us to the result of Kleitman in Section 6.4, and observed
that Knill’s graph-generated families form lower semimodular lattices.

30

References

[1] T. Abe, Strong semimodular lattices and Frankl’s conjecture, Algebra univers. 44
(2000), 379–382.

[2] , Excess of a lattice, Graphs Comb. 18 (2002), 395–402.

[3] T. Abe and B. Nakano, Frankl’s conjecture is true for modular lattices, Graphs
Comb. 14 (1998), 305–311.

[4] , Lower semimodular types of lattices: Frankl’s conjecture holds for lower
quasi-semimodular lattices, Graphs Comb. 16 (2000), 1–16.

[5] N. Alon, On the density of sets of vectors, Disc. Math. 46 (1983), 199–202.

[6] A much-travelled conjecture, Austr. Math. Soc. Gaz. 14/3 (1987), 63.

[7] Union-closed sets conjecture, Austr. Math. Soc. Gaz. 14/4 (1987), 99.

[8] I. Balla, Minimum densities of union-closed families, arXiv:1106.0369v1
[math.CO], 2011.

[9] I. Balla, B. Bollobas, and T. Eccles, Union-closed families of sets, J. Combin.
Theory (Series A) 120 (2013), 531–544.

[10] I. Boˇsnjak and P. Markovi´c, The 11-element case of Frankl’s conjecture, Europ.
J. Combin. 15 (2008), R88.

[11] H. Bruhn, P. Charbit, O. Schaudt, and J.A. Telle, The graph formulation of the
union-closed sets conjecture, preprint, 2013.

[12] H. Bruhn and O. Schaudt, The union-closed sets conjecture almost holds for al-
most all random bipartite graphs, preprint, 2012.

[13] G. Cz´edli, On averaging Frankl’s conjecture for large union-closed sets, J. Combin.
Theory (Series A) 116 (2009), 724–729.

[14] G. Cz´edli, M. Mar´oti, and E.T. Schmidt, On the scope of averaging for Frankl’s
conjecture, Order 26 (2009), 31–48.

[15] G. Cz´edli and E.T. Schmidt, Frankl’s conjecture for large semimodular and planar
semimodular lattices, Acta Univ. Palacki. Olomuc., Fac. rer. nat., Mathematica
47 (2008), 47–53.

[16] R. Diestel, Graph theory (3rd edition), Springer-Verlag, 2005.

[17] K. Dohmen, A new perspective on the union-closed sets conjecture, Ars Combin.
58 (2001), 183–185.

[18] D. Duﬀus and B. Sands, An inequality for the sizes of prime ﬁlters of ﬁnite
distributive lattices, Disc. Math. 201 (1999), 89–99.

[19] M. El-Zahar, A graph-theoretic version of the union-closed sets conjecture,
J. Graph Theory 26 (1997), 155–163.

[20] V. Falgas-Ravry, Minimal weight in union-closed families, Electron. J. Combin.
18 (2011), #P95.

[21] G. Lo Faro, A note on the union-closed sets conjecture, J. Austral. Math. Soc. (Se-
ries A) 57 (1994), 230–236.

[22] , Union-closed sets conjecture: Improved bounds, J. Combin. Math. Com-
bin. Comput. 16 (1994), 97–102.
 31

[23] P. Frankl, personal communication.

[24] , On the trace of ﬁnite sets, J. Combin. Theory (Series A) 34 (1983),
41–45.

[25] , A new short proof for the Kruskal-Katona theorem, Disc. Math. 48
(1984), 327–329.

[26] , Handbook of combinatorics (vol. 2), MIT Press, Cambridge, MA, USA,
1995, pp. 1293–1329.

[27] W. Gao and H. Yu, Note on the union-closed sets conjecture, Ars Combin. 49
(1998), 280–288.

[28] Open Problem Garden, Frankl’s union-closed sets conjecture, http://
www.openproblemgarden.org/op/frankls_union_closed_sets_conjecture, ac-
cessed: 06/05/2013.

[29] G. Gr¨atzer, General lattice theory, Springer-Verlag, 2003.

[30] C. Herrmann and R. Langsdorf, Frankl’s conjecture for lower semimodular lattices,
unpublished preprint, 1999.

[31] Y. Hu, Master’s thesis, in preparation.

[32] W. Imrich, N. Sauer, and W. Woess, The average size of admissible sets in a
graph, Tech. report, Montanuniversit¨at Leoben, 1988.

[33] , The average size of nonsingular sets in a graph, Finite and Inﬁnite Com-
binatorics in Sets and Logic (N.W. Sauer et al., ed.), Kluwer Academic Publishers,
Dordrecht, Netherlands, 1993, pp. 199–205.

[34] R.T. Johnson and T.P. Vaughan, On union-closed families, I, J. Combin. Theory
(Series A) 85 (1999), 112–119.

[35] G. Kalai, Extremal Combinatorics IV: Shifting, http://gilkalai.
wordpress.com/2008/10/06/extremal-combinatorics-iv-shifting/, ac-
cessed: 01/05/2013.

[36] D.J. Kleitman, Extremal properties of collections of subsets containing no two sets
and their union, J. Combin. Theory (Series A) 20 (1976), 390–392.

[37] E. Knill, Generalized degrees and densities for families of sets, PhD thesis, Uni-
versity of Colorado, 1991.

[38] , Graph generated union-closed families of sets, arXiv:math/9409215v1
[math.CO], 1994.

[39] T. Kubo and R. Vakil, On Conway’s recursive sequence, Disc. Math. 152 (1996),
225–252.

[40] U. Leck and I.T. Roberts, Inequalities for cross-unions of collections of ﬁnite sets,
preprint, 2013.

[41] U. Leck, I.T. Roberts, and J. Simpson, Minimizing the weight of the union-closure
of families of two-sets, Australas. J. Combin. 52 (2012), 67–73.

[42] B. Llano, J.J. Montellano-Ballesteros, E. Rivera-Campo, and R. Strausz, On
conjectures of Frankl and El-Zahar, J. Graph Theory 57 (2008), 344–352.

[43] C.I. Mallows, Conway’s challenge sequence, Amer. Math. Monthly 98 (1991),
5–20.
 32

[44] F. Mari´c, M. ˇZivkovi´c, and B. Vuˇckovi´c, Formalizing Frankl’s conjecture: Fc-
families, Lecture Notes in Comput. Sci. 7362 (2012), 248–263.

[45] P. Markovi´c, An attempt at Frankl’s conjecture, Publications de l’Institut
Math´ematique. Nouvelle S´erie 81 (2007), 29–43.

[46] R. Morris, FC-families, and improved bounds for Frankl’s conjecture, Europ. J.
Combin. 27 (2006), 269–282.

[47] T. Nishimura and S. Takahashi, Around Frankl conjecture, Sci. Rep. Yokohama
Nat. Univ. Sect. I Math. Phys. Chem. 43 (1996), 15–23.

[48] R.M. Norton and D.G. Sarvate, A note on the union-closed sets conjecture, J. Aus-
tral. Math. Soc. (Series A) 55 (1993), 411–413.

[49] Y. Peng, P. Sissokho, and C. Zhao, An extremal problem for set families generated
with the union and symmetric diﬀerence operations, J. Combin. 3 (2012), 651–668.

[50] B. Poonen, Union-closed families, J. Combin. Theory (Series A) 59 (1992), 253–
268.

[51] D. Reimer, An average set size theorem, Comb., Probab. Comput. (2003), 89–93.

[52] J. Reinhold, Frankl’s conjecture is true for lower semimodular lattices, Graphs
Comb. 16 (2000), no. 1, 115–116.

[53] J.-C. Renaud, Is the union-closed sets conjecture the best possible?, J. Aus-
tral. Math. Soc. (Series A) 51 (1991), 276–283.

[54] J-C. Renaud, A second approximation to the boundary function on union-closed
collections, Ars Combin. 41 (1995), 177–188.

[55] J.-C. Renaud and L.F. Fitina, On union-closed sets and Conway’s sequence,
Bull. Austral. Math. Soc. 47 (1993), 321–332.

[56] I. Rival (ed.), Graphs and order, NATO ASI Series, vol. 147, Springer Netherlands,
1985.

[57] I. Roberts, The union-closed sets conjecture, Tech. Report 2/92, Curtin University
of Technology, 1992.

[58] I. Roberts and J. Simpson, A note on the union-closed sets conjecture, Australas.
J. Combin. 47 (2010), 265–267.

[59] E. Rodaro, Union-closed vs upward-closed families of ﬁnite sets,
arXiv:math/1208.5371v2 [math.CO], 2012.

[60] N. Zagaglia Salvi, An equivalent formulation of the union-closed sets conjecture,
manuscript.

[61] F. Salzborn, A note on the intersecting sets conjecture, manuscript, 1989.

[62] D.G. Sarvate and J.-C. Renaud, On the union-closed sets conjecture, Ars Combin.
27 (1989), 149–154.

[63] , Improved bounds for the union-closed sets conjecture, Ars Combin. 29
(1990), 181–185.

[64] R.P. Stanley, Enumerative combinatorics, vol. I, Wadsworth & Brooks/Cole,
1986.

[65] T.P. Vaughan, More on 3-sets in union-closed families: The end is in sight,
http://atlas-conferences.com/c/a/q/a/23.htm, accessed: 24/03/2013.

33

[66] , Families implying the Frankl conjecture, Europ. J. Combin. 23 (2002),
851–860.

[67] , Three-sets in a union-closed family, J. Combin. Math. Combin. Comput.
49 (2004), 73–84.

[68] M. ˇZivkovi´c and B. Vuˇckovi´c, The 12 element case of Frankl’s conjecture, preprint,
2012.

[69] D. West, Union-closed sets conjecture (1979), http://www.math.uiuc.edu/
~west/openp/unionclos.html, accessed: 06/05/2013.

[70] Wikipedia, Union-closed sets conjecture, http://en.wikipedia.org/wiki/
Union-closed_sets_conjecture, accessed: 06/05/2013.

[71] P. W´ojcik, Density of union-closed families, Disc. Math. 105 (1992), 259–267.

[72] , Union-closed families of sets, Disc. Math. 199 (1999), 173–182.

Version 25 Oct 2013

Henning Bruhn <henning.bruhn@uni-ulm.de>
Universit¨at Ulm, Germany

Oliver Schaudt <schaudto@uni-koeln.de>
Institut f¨ur Informatik
Universit¨at zu K¨oln
Weyertal 80
Germany
 34
