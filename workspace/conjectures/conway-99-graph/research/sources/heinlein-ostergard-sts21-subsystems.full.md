<!-- source: https://arxiv.org/pdf/2104.06825 | converted from PDF -->

arXiv:2104.06825v2  [math.CO]  24 Aug 2022
Steiner Triple Systems of Order 21 with
Subsystems

Daniel Heinlein
∗ and Patric R. J. Östergård
Department of Communications and Networking
Aalto University School of Electrical Engineering
P.O. Box 15400, 00076 Aalto, Finland
{daniel.heinlein,patric.ostergard}@aalto.fi

Abstract

The smallest open case for classifying Steiner triple systems is order
21. A Steiner triple system of order 21, an STS(21), can have subsys-
tems of orders 7 and 9, and it is known that there are 12,661,527,336
isomorphism classes of STS(21)s with sub-STS(9)s. Here, the clas-
siﬁcation of STS(21)s with subsystems is completed by settling the
case of STS(21)s with sub-STS(7)s. There are 116,635,963,205,551
isomorphism classes of such systems. An estimation of the number of
isomorphism classes of STS(21)s is given.

Keywords: classiﬁcation, Steiner triple system, subsystem
MSC: 05B07

1 Introduction

A Steiner triple system (STS) is a pair (V, B), where V is a set of points and
B is a set of 3-subsets of points, called blocks, such that every 2-subset of
points occurs in exactly one block. The size of the point set is the order of
the STS, and an STS of order v is denoted by STS(v). It is well known that
an STS(v) exists iﬀ v ≡ 1 or 3 (mod 6). (1)

For more information about Steiner triple systems, see [4, 5].

∗Supported by the Academy of Finland, Grant 331044.

1

An STS(v) is said to be isomorphic to another STS(v) if there exists a
bijection between the point sets that maps blocks onto blocks; such a bijection
is called an isomorphism. An isomorphism of a Steiner triple system onto
itself is an automorphism of the STS. The automorphisms of an STS form
a group under composition, the automorphism group of the Steiner triple
system.
Classiﬁcation of combinatorial designs is about ﬁnding a transversal of
the isomorphism classes [13]. The Steiner triple systems have been classi-
ﬁed up to order 19, and the numbers of isomorphism classes are 1, 1, 1, 2,
80, and 11,084,874,829 for orders 3, 7, 9, 13, 15, and 19, respectively. A
classiﬁcation of the STS(19)s was published in 2004 with a remark that the
algorithm used would require hundreds of thousands of CPU years to clas-
sify the STS(21)s [11]. As this seems to be currently out of reach, one will
have to focus on subclasses of STS(21)s. Indeed, STS(21)s of various types
have been considered in this context, including STS(21)s with a nontrivial
automorphism group [10] (with earlier work in [3, 9, 20, 21, 22, 30, 31], also
considering other properties), anti-Pasch STS(21)s [18], and resolutions of
STS(21)s—that is, Kirkman triple systems—with subsystems [17].
A necessary condition for an STS(v) to have a nontrivial (w > 3) and
proper (w < v) subsystem of order w, i.e., a sub-STS(w), is that v ≥ 2w + 1;
see [5, Lemma 6.1]. Classiﬁcation of Steiner triple systems with sub-STS(7)s
has been carried out for orders 15 and 19—see [23, Table 1.29] and [15],
respectively—and for those with sub-STS(9)s for order 19—see [29].
The only possible nontrivial proper subsystems of STS(21)s are STS(7)s
and STS(9)s. The STS(21)s with sub-STS(9)s are classiﬁed in [14]; there
are 12,661,527,336 isomorphism classes of such designs. For STS(21)s with
sub-STS(7)s, the special case of Wilson-type systems is handled in [15].
Wilson-type STS(21)s contain three sub-STS(7)s on disjoint point sets. In
the current paper the classiﬁcation problem for STS(21)s with subsystems is
settled by completing the case of sub-STS(7)s.

Theorem 1 There are 116,635,963,205,551 isomorphism classes of STS(21)s
containing at least one sub-STS(7).

The paper is organized as follows. An algorithm for classifying STS(21)s
with sub-STS(7)s is described in Section 2, and the results are listed in Sec-
tion 3. The number of isomorphism classes of STS(21)s with sub-STS(7)s is
used in Section 4 to get an estimation of the total number of isomorphism
classes of STS(21)s.
 2

2 Classiﬁcation

In this section, we present a classiﬁcation algorithm for STS(21)s contain-
ing sub-STS(7)s. To facilitate reading, we give necessary deﬁnitions in Sec-
tion 2.1. The general approach is outlined in Section 2.2, details about sub-
tasks are given in Section 2.4, and some computational issues are considered
in Section 2.5.

2.1 Deﬁnitions

A (vr, bk) conﬁguration is an incidence structure with v points and b blocks,
such that each block contains k points, each point occurs in r blocks, and
two diﬀerent blocks intersect in at most one point. If v = b and k = r,
these are simply called vk conﬁgurations. The deﬁnitions of isomorphism
and automorphism of conﬁgurations are analogous to those for Steiner triple
systems.
A 1-factor in a graph, also called a perfect matching, is a 1-regular span-
ning subgraph and a 1-factorization is a partition of the edges of the graph
into 1-factors. A 1-factorization of a graph G = (V, E) is isomorphic to a
1-factorization of a graph G′ = (V ′, E′) if there is a bijection from V to V ′

that maps the 1-factors of the 1-factorization of G onto the 1-factors of the
1-factorization of G′.

2.2 General Approach

On a general level, the current approach follows [14], in which all of Theo-
rem 2 except the last statement already appeared.

Theorem 2 ([14]) Let (V, B) be an STS(v) that has a sub-STS(w) (W, B′).
Then

1. B = B′ ∪ F ∪ D where F and D are the sets of blocks that intersect W
in 1 and 0 points, respectively,

2. F = ⋃
p∈W Bp where Bp is the set of blocks in F that contain p ∈ W ,

3. B′
p = {B \ {p} : B ∈ Bp} is a 1-factor of a graph G with vertices V \ W
and edges ⋃
p∈W B′
p,

4. {B′
p : p ∈ W } is a 1-factorization of G,

5. G is w-regular and its complement G is (v − 2w − 1)-regular, and

3

6. G can be decomposed into a set of edge-disjoint 3-cycles—D being one
possible set—which forms a

((v − w)(v−2w−1)/2, ((v − w)(v − 2w − 1)/6)3)

conﬁguration.

Using this theorem, any STS containing a sub-STS is decomposable into
B′∪F ∪D. For the task of classifying all STS(v)s containing some sub-STS(w),
one has now two starting points: either a classiﬁcation of the 1-factorizations
underlying F or a classiﬁcation of the conﬁgurations corresponding to D.
Then, in both cases, one needs to combine this with a classiﬁcation of B′ to
create an STS in all possible ways, taking symmetry into account.
The next sections illustrate the details for v = 21 and w = 7; the general
setting is also depicted in [14].

2.3 Application to STS(21) containing sub-STS(7)s

Let (V, B) be an STS(21) that has a sub-STS(7) (W, B′). Clearly W ⊆ V
and B′ ⊆ B. The blocks in B \ B′ intersect W in either 0 or 1 points, and
those two sets of blocks are denoted by D and F , respectively.
Fix a point p ∈ W and let Bp be the set of blocks in F that contain p.
Further let
 B′
p = {B \ {p} : B ∈ Bp}. (2)

As a pair of points with one point in W and the other in V \ W must
occur in exactly one block of F , the sets in B′
p partition V \ W . The sets in
B′
p have size 2, and we may view them as edges in a graph with vertex set
V \ W . The sets in B′
p form a 1-factor of that graph. With 7 possible values
of p, we have 7 disjoint 1-factors of a 7-regular graph of order 14.
To complete the Steiner triple system, given a 7-regular graph G of order
14, one may ﬁnd all 1-factorizations of G and in the complement G ﬁnd
all decompositions into 3-cycles (which is the graph analogy of ﬁnding sets
of triples that cover all unordered pairs) and combine these in all possible
ways. Doing this for all possible choices of G gives all ways of extending the
initial STS(7). Finally, isomorph rejection needs to be carried out during the
process of combining parts. Speciﬁc details about using this approach in the
current work—where the order D → F → B′ for constructing the blocks B
is actually used—are presented in Section 2.4. See also [14].
There are 21,609,301 isomorphism classes of 7-regular graphs of order
14 [26]; see also [28, Table 4.25]. Only a small number of graphs G have

4

the property that the complement G can be decomposed into 3-cycles as
described in the last statement in Theorem 2. Indeed, the required 143
conﬁgurations have already been classiﬁed.
There are 21,399 isomorphism classes of 143 conﬁgurations [2]. Checking
the isomorphism classes of graphs underlying the 143 conﬁgurations shows
that their number is 20,787. As this is about one thousandth of the number
of regular graphs, the 143 conﬁgurations are the appropriate building block
for our algorithm.

Example There is a unique isomorphism class of an STS(21) that contains
at least one sub-STS(7) and that admits an automorphism group of order
108, see Table 1. The following incidence matrix of such a design visualizes
the partitions of points and blocks in the general approach (note that the
ordering of rows and columns within each subset does not necessarily coincide
with the ordering given by the algorithm):

W
 1 1 1 . . . . 1 1 1 1 1 1 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1 . . 1 1 . . . . . . . . . 1 1 1 1 1 1 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
1 . . . . 1 1 . . . . . . . . . . . . . . 1 1 1 1 1 1 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. 1 . 1 . 1 . . . . . . . . . . . . . . . . . . . . . . 1 1 1 1 1 1 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . 1 . 1 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 1 1 1 1 1 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . .
. . 1 1 . . 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 1 1 1 1 1 1 . . . . . . . . . . . . . . . . . . . . .
. 1 . . 1 . 1 . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1 1 1 1 1 1 1 . . . . . . . . . . . . . .

V \ W
 . . . . . . . 1 . . . . . . 1 . . . . . . 1 . . . . . . 1 . . . . . . 1 . . . . . . 1 . . . . . . 1 . . . . . . 1 1 1 . . . . . . . . . . .
. . . . . . . . 1 . . . . . . 1 . . . . . 1 . . . . . . . 1 . . . . . . 1 . . . . . . 1 . . . . . . 1 . . . . . . . . 1 1 1 . . . . . . . .
. . . . . . . . . 1 . . . . . . 1 . . . . . 1 . . . . . . . 1 . . . . . . 1 . . . . . 1 . . . . . . . 1 . . . . 1 . . . . . 1 1 . . . . . .
. . . . . . . . . . 1 . . . . . 1 . . . . . . 1 . . . . . 1 . . . . . . . . 1 . . . . . 1 . . . . . . . 1 . . . . 1 . . . . . . 1 1 . . . .
. . . . . . . . 1 . . . . . 1 . . . . . . . . . 1 . . . . . . 1 . . . . . . . 1 . . . . . 1 . . . . . . . 1 . . . . . . . . 1 . 1 . 1 . . .
. . . . . . . . . . . 1 . . . . . 1 . . . . 1 . . . . . . . . . 1 . . . . . . . 1 . 1 . . . . . . . . . . . 1 . . . . 1 . . . . . 1 1 . . .
. . . . . . . . . . . . 1 . . . . . 1 . . . . . . 1 . . . . . . . 1 . . . . . . . 1 . . . . 1 . . . . . . . . 1 1 . . 1 . . . . 1 . . . . .
. . . . . . . 1 . . . . . . . 1 . . . . . . . . 1 . . . . . 1 . . . . . . . . . 1 . . . 1 . . . . . . . . . . 1 . . . . . . . . . . . 1 1 1
. . . . . . . . . . . . . 1 . . . . . 1 . . . . . 1 . . . . . . 1 . . . . 1 . . . . . . . 1 . . . . . . 1 . . . . . 1 . 1 . . . . . . 1 . .
. . . . . . . . . . . 1 . . . . . . . . 1 . . 1 . . . . . . . . . . 1 1 . . . . . . . . . . 1 . . . . . . 1 . . . . . . . 1 . 1 . . . 1 . .
. . . . . . . . . . 1 . . . . . . 1 . . . . . . . . 1 . . . . 1 . . . . . . . . . 1 . . . . . 1 . . 1 . . . . . . . 1 . . . . 1 . . . . 1 .
. . . . . . . . . . . . . 1 . . . . 1 . . . . . . . . 1 . . . . . . 1 . 1 . . . . . . . . . . . 1 . . . . . 1 . . 1 . . . . 1 . . . . . 1 .
. . . . . . . . . 1 . . . . . . . . . . 1 . . . . . 1 . . . . . . 1 . . . . . 1 . . . . . . . . 1 1 . . . . . . . . . . 1 . . . . 1 . . . 1
. . . . . . . . . . . . 1 . . . . . . 1 . . . . . . . 1 1 . . . . . . . . . 1 . . . . . . . . 1 . . . 1 . . . . . . . . . 1 . . . . 1 . . 1
B0 B1 B2 B3 B4 B5 B6
B′ F D

Let V = {0, 1, . . . , 20}. The design can be constructed by considering the
group of order 108 generated by

(0, 9, 19)(2, 10, 16)(3, 4, 20, 8, 7, 18)(5, 6, 15, 14, 11, 13) and
(0, 3, 4)(2, 5, 6)(7, 8, 9, 20, 18, 19)(10, 15, 13, 16, 11, 14)(12, 17)

and taking the 7 orbits under the action of this group with representatives

{0, 1, 2}, {0, 3, 6}, {0, 9, 19}, {0, 10, 17}, {1, 12, 17}, {2, 5, 6}, {2, 10, 16}.

2.4 Details of the Approach

We shall now give more speciﬁc details needed for implementing the gen-
eral approach. Some of the computational subproblems will be considered

5

separately in Section 2.5.

The point set When building up an STS(21) (V, B) containing a sub-STS(7),
we let V = {0, 1, . . . , 20} such that W = {14, 15, . . . , 20} is the point set of
the particularized sub-STS(7) (W, B′), called S′.

The 143 conﬁguration The distribution of the orders of the automor-
phism groups of the 21,399 143 conﬁgurations [2] is

120,3282916319491612718151271431632421281564481.

The unique 143 conﬁguration with automorphism group order 56448 consists
of two disjoint STS(7) and is the conﬁguration of Wilson-type systems. Ig-
noring that conﬁguration here, the groups to be considered have order at
most 128, so there is no need for advanced group algorithms.
After ﬁxing a conﬁguration (V \ W, D), where the point set is V \ W =
{0, . . . , 13}, we compute its automorphism group A, the underlying graph G,
and the complement G. Notice that the group A is trivial in most of the
cases.

The 1-factorization For a given graph G, we ﬁrst determine the set F
of 1-factors of G and then use the 1-factors in F to compute the set F ′

of all possible 1-factorizations of G. If the group A is nontrivial, isomorph
rejection is further carried out by accepting precisely those 1-factorizations
in F ′ that are lexicographically minimum under the action of A. For an
accepted 1-factorization, the subgroup of A consisting of the elements that
stabilize the 1-factorization is denoted by A
′.
A 1-factor of G corresponds to a set B′
p deﬁned in (2), and a 1-factorization
of G gives a set of blocks F = ∪
20
p=14Bp up to permutation of the points in
W = {14, 15, . . . , 20} (we pick an arbitrary one). The group A
′ acts on V \W .
Blocks of F also have points in W , so we extend the action of A
′ to get a
group A
′′ acting on V . The permutation of the points in W for an element in
A
′′ is uniquely deﬁned by how the original element in A
′ maps the 1-factors.

The sub-STS(7) There is a unique STS(7), the Fano plane, which has an
automorphism group of order 168. Hence there are are 7!/168 = 30 distinct
labelled STS(7)s on 7 given points.
An isomorphism from one STS(21) with a sub-STS(7) to another maps
the particularized sub-STS(7) to a sub-STS(7). Hence there are two general
situations: STS(21)s with exactly one sub-STS(7) and STS(21)s with more
than one sub-STS(7)s. In the latter case, there are further several possibilities

6

for how the point sets of two sub-STS(7)s may intersect. Such an intersection
must form a (possibly trivial) sub-STS, so possible intersection sizes are 0, 1,
and 3.
If the intersection size is 0, then there is necessarily a third sub-STS(7)
whose point set is disjoint from the point sets of the ﬁrst two sub-STS(7)s,
that is, we have a Wilson-type system and the 143 conﬁguration discussed
earlier. Wilson-type STS(21)s have exactly three sub-STS(7)s [15, Lemma 1].
As the mentioned 143 conﬁguration is not considered here, this case will not
occur in the search.
Isomorph rejection when extending blocks D ∪ F with blocks B′ is anal-
ogous to the situation when extending blocks D with blocks F , considered
earlier. Now, out of the 30 possibilities, those sub-STS(7)s that are lexico-
graphically minimum under the action of A
′′ are accepted. The subgroup
of A
′′ consisting of the elements that stabilize the accepted sub-STS(7) is
denoted by A
′′′.
The blocks B = D ∪ F ∪ B′ now form an STS(21) with a particularized
sub-STS(7), and if those are the objects to classify we would be done. But
in the classiﬁcation of STS(21)s with at least one sub-STS(7), there is still
one ﬁnal step.

The ﬁnal isomorph rejection If there is exactly one sub-STS(7) in the
constructed design (V, B), then we accept the STS(21); its automorphism
group is the group A
′′′ computed earlier. Otherwise, we proceed by ﬁnding
all sub-STS(7)s in V . (As we have seen, these will intersect W in exactly 1
or 3 points; some precomputations for ﬁnding them can be done based on
D and F .) We now determine whether the particularized sub-STS(7) is a
canonically minimum sub-STS(7), to be discussed in Section 2.5, and accept
it if that is the case. The automorphism group of an accepted STS(21) is
obtained as a by-product of the computations.

2.5 Computational Subproblems

We shall here discuss some of the main computational subproblems that are
encountered when implementing the presented approach and that are not
standard problems related to data structures and algorithms.

Automorphism groups and canonical forms Automorphism groups
and canonical forms are conveniently computed with nauty [24] after an
appropriate transformation of the combinatorial structure to a graph.

7

To order the sub-STS(7)s of an STS(21) one may use the standard graph
encoding of the incidence matrix of the design, add one vertex for each
sub-STS(7), and let the 7 vertices corresponding to the points of the sub-STS(7)
form the neighborhood of an added vertex. Then the canonical order of ver-
tices given by nauty imposes an order on the sub-STS(7)s. More precisely,
nauty determines an order of the orbits of vertices under the action of the
automorphism group of the graph. Therefore we get an induced ordering of
the orbits of sub-STS(7)s under the action of the automorphism group of the
STS(21).
For small group orders, the abstract type of the automorphism groups
of the classiﬁed designs can be identiﬁed based on the multiset of orders of
elements. The abstract type can further be computed using AllSmallGroups
and StructureDescription in GAP [8]. In the current work, seven groups
(of orders 27, 54, 108, 294, and 1008) had to be treated manually and sepa-
rately. The designs with nontrivial automorphisms are amongst those classi-
ﬁed in [10].

1-factors and 1-factorizations Although ﬁnding single perfect match-
ings in general graphs respective all perfect matchings in bipartite graphs
are standard computational problems [6, 7], we use a backtrack algorithm to
compute all 1-factors of general graphs. Given the set of 1-factors of a graph,
the problem of ﬁnding all 1-factorizations can be phrased in the framework
of exact cover [12], whereby the instances can be solved, for example, using
the libexact [16] software.

3 Results

The total number of isomorphism classes of STS(21)s containing at least
one sub-STS(7) is 116,635,963,205,551, which splits into 116,635,961,039,200
cases that are not of Wilson type and 2,166,351 cases that are of Wilson
type [15].
More detailed information can be found in Table 1 and Table 2. The
column headers in Table 1 are the order of the automorphism group (O),
the number of contained sub-STS(7)s (U), the number of unordered pairs of
sub-STS(7)s that intersect in 1 and 3 points (I1 and I3, respectively), the
abstract type of the automorphism group (A), and ﬁnally the number of
isomorphism classes of STS(21)s with these properties (#).
For completeness, Table 1b from [15] is included. For all Wilson-type
STS(21)s, we have U = 3, I1 = 0, and I3 = 0 by [15, Lemma 1]. In the
Appendix, some data for STS(21)s that do not contain sub-STS(7)s is given.

8

The notation for the abstract types of groups is as follows: Cn is the cyclic
group of order n, Sn is the symmetric group of order n!, An is the alternating
group of order n!/2, Dn is the dihedral group of order n, and PSL(v, q) is the
projective special linear group in Fv
q. For two groups G and H, G × H is the
direct product of G and H, G ⋊ H is a semidirect product of G and H, and
Gn is G × G × · · · × G (n times).
A central open problem for speciﬁc STS(21)s is whether systems exist that
are doubly resolvable. The current work gives nothing new with respect to
this problem, because Kirkman triple systems of order 21 with sub-STS(7)s
have already been classiﬁed and tested [17].
The whole classiﬁcation including the detection of the abstract group
types took about 1300 CPU days on the equivalent of one core of an Intel
Xeon E5-2665 @ 2.40GHz.

Veriﬁcation We perform two tests to validate results. Let S be a transver-
sal of the isomorphism classes of the STS(21)s with sub-STS(7)s that are not
of Wilson type—this is the outcome of the current classiﬁcation—and let C
be a transversal of the isomorphism classes of the 143 conﬁgurations exclud-
ing the conﬁguration leading to Wilson-type STS(21)s. Further, let s7(S) be
the number of sub-STS(7)s in the system S, and let f (C) be the number
of 1-factorizations with labelled 1-factors of the complement of the graph
underlying the conﬁguration C. During the computations, all this data was
collected.
In the ﬁrst test, we count in two diﬀerent ways all pairs of labelled
STS(21)s that are not of Wilson type and their contained sub-STS(7)s. By
the Orbit–Stabilizer Theorem, we have

∑

S∈S
 21!
| Aut(S)| · s7(S) = ∑

C∈C
 21!
| Aut(C)| 7!
168 · f (C).

Both sides of this equality yielded

5,988,986,139,804,614,556,727,954,636,800,000

in the ﬁnal computation. The fact [15] that Wilson-type STS(21)s have
exactly three sub-STS(7)s and will not appear in the search is essential for
the double counting to work.
In the second test, we extract the STS(21)s with sub-STS(7)s from the
STS(21)s with nontrivial automorphisms classiﬁed in [10] and compare the
numbers with those in Table 1a. Also this test was successful.

9

Table 1: Numbers of STS(21)s containing at least one sub-STS(7)

(a) non-Wilson type

O U I1 I3 A #

1 1 0 0 C1 116,051,875,827,936

1 2 1 0 C1 31,778,146,776

1 2 0 1 C1 550,238,290,596

1 3 1 2 C1 593,663,600

1 3 3 0 C1 60,352,088

1 3 0 3 C1 1,385,739,943

1 4 1 5 C1 6,391,040

1 4 2 4 C1 198,304

1 4 3 3 C1 1,607,028

1 4 0 6 C1 157,886

1 5 1 9 C1 576

1 5 2 8 C1 50,192

1 5 3 7 C1 30,024

1 5 4 6 C1 1,704

1 6 3 12 C1 1,790

1 6 4 11 C1 688

1 7 5 16 C1 124

2 1 0 0 C2 19,270,679

2 2 1 0 C2 84,080

2 2 0 1 C2 814,880

2 3 1 2 C2 18,912

2 3 3 0 C2 43,062

2 3 0 3 C2 132,334

2 4 1 5 C2 9,088

2 4 2 4 C2 64

2 4 3 3 C2 2,448

2 5 2 8 C2 224

2 5 3 7 C2 2,092

2 5 4 6 C2 16

2 6 3 12 C2 140

2 6 4 11 C2 32

2 7 5 16 C2 188

2 9 9 27 C2 2

3 1 0 0 C3 177,205

3 2 1 0 C3 3,152

3 2 0 1 C3 5,508
 O U I1 I3 A #

3 3 3 0 C3 655

3 3 0 3 C3 4,152

3 4 3 3 C3 132

3 4 0 6 C3 6

3 5 4 6 C3 16

3 6 3 12 C3 18

4 1 0 0 C2
2 6,268

4 1 0 0 C4 628

4 3 3 0 C2
2 260

4 3 0 3 C2
2 870

4 5 3 7 C2
2 136

4 7 5 16 C2
2 24

4 9 9 27 C2
2 3

6 1 0 0 C6 849

6 1 0 0 S3 192

6 3 3 0 C6 146

6 3 3 0 S3 39

6 3 0 3 C6 91

6 3 0 3 S3 31

6 4 3 3 S3 16

6 6 3 12 S3 4

6 9 9 27 S3 2

7 1 0 0 C7 27

8 1 0 0 C4 × C2 8

8 1 0 0 D8 164

9 3 3 0 C2
3 1

9 3 0 3 C2
3 3

12 3 3 0 D12 4

12 3 0 3 D12 10

12 9 9 27 D12 3

14 1 0 0 C14 14

16 1 0 0 C2 × D8 8

18 3 3 0 C3 × S3 11

18 3 0 3 C3 × S3 6

36 9 9 27 S2
3 1

108 9 9 27 (C2
3 ⋊ C6) ⋊ C2 1
 (b) Wilson type

O A #

1 C1 2,156,186

2 C2 8,914

3 C3 685

4 C2
2 253

4 C4 18

6 C6 94

6 S3 103

8 C3
2 22

8 D8 19

9 C2
3 3

12 A4 2

12 D12 4

16 C2 × D8 4

18 C2
3 ⋊ C2 2

18 C3 × S3 5

21 C7 ⋊ C3 2

24 C2 × A4 9

24 C2
2 × S3 1

24 S4 7

42 C2 × (C7 ⋊ C3) 1

42 C7 ⋊ C6 5

48 C2 × S4 2

72 (C3 × A4) ⋊ C2 1

72 A4 × S3 4

126 S3 × (C7 ⋊ C3) 1

144 S3 × S4 1

294 C2
7 ⋊ C6 1

882 (C7 ⋊ C3)2 ⋊ C2 1

1008 PSL(3, 2) × S3 1

10

Table 2: Aggregated numbers of STS(21)s containing at least one sub-STS(7)

O #

1 116,635,942,616,481
2 20,387,155
3 191,529
4 8,460
6 1,567
7 27
 O #

8 213
9 7
12 23
14 14
16 12
18 24
 O #

21 2
24 17
36 1
42 6
48 2
72 5
 O #

108 1
126 1
144 1
294 1
882 1
1008 1

4 Estimating the Number of STS(21)s

The classiﬁcation of the STS(21)s with sub-STS(7)s gives a lower bound on
the number of isomorphism classes of STS(21) but can also be used for an
estimation of that number. The authors are not aware of any published
estimations.
Quackenbush [27] conjectured that almost all Steiner triple systems have
no nontrivial subsystems. Later, however, Kwan [19] used a random model
to ﬁnd evidence for the number of sub-STS(7)s in an STS(v) to have expec-
tation Θ(1), referring to similar work in [25] on Latin squares. The models
used in [19] and [25] are random 3-uniform hypergraphs and random integer
matrices, respectively.
An STS(v) has v(v − 1)/6 blocks out of v(v − 1)(v − 2)/6 3-subsets of
a v-set, that is, a ratio of p := 1/(v − 2) of the 3-subsets are blocks. We
may now form a random 3-uniform hypergraph on v vertices by including
blocks with probability p (note that p := 1/v, which is used in [19], works
when studying asymptotics). We denote the number of labelled STS(w)s on
w points by N(w). We have seen earlier that N(7) = 30. The number of
labelled STS(w)s on v points, where v ≥ w, is M(v, w) := N(w)( v
w
)
. The
probability for a given STS(w) to occur in the random model is pw(w−1)/6.
The linearity of the expected value allows now to compute the expected
number of sub-STS(w)
 µ(v, w) := N(w)( v
w
)

(v − 2)w(w−1)/6

and, abbreviating µ(∞, w) = limv→∞ µ(v, w), we have µ(∞, 7) = 1/168 ≈
0.00595 and µ(∞, w) = 0 for w > 7.
Let S be the set of positive integers fulﬁlling (1). Analogously to the
conjecture in [25, p. 346], see also [19], we state the following.

11

Conjecture 1 The distribution of the number of sub-STS(w)s in an STS(v)
tends to the Poisson distribution with expected value 1/168 for w = 7 and
expected value 0 for w > 7 as v ∈ S tends to inﬁnity.

The proportion of STS(v) containing at least one sub-STS(7) is then
approximately α = 1 − e
−1/168 ≈ 0.00593 for large v. Consequently, an
estimation of the total number of STS(v) can be obtained by dividing the
number of STS(v) with at least one sub-STS(w) by α.
As almost all Steiner triple systems have no nontrivial automorphisms [1],
an estimation for the number of isomorphism classes of STS(v) can be ob-
tained by dividing the number of isomorphism classes of STS(v) with at least
one sub-STS(w) by α.
There are only two instances for which the quality of such an estimation
can be checked, and the case STS(15) with only 80 isomorphism classes is
not useful. For the 11,084,874,829 STS(19) out of which 86,701,547 have at
least one sub-STS(7) [15], we get a ratio of approximately 0.00782, which is
getting into the same order of magnitude as α.
For the number of isomorphism classes of STS(21)s, using the classiﬁca-
tion results of the current paper we calculate

116,635,963,205,551/α ≈ 1.965 · 1016,

which indicates that the number could be somewhat greater than 1016, per-
haps between 1 · 1016 and 2 · 1016.
In the estimation one might consider utilizing µ(21, 7) ≈ 0.00389 rather
than µ(∞, 7), but notice that µ(19, 7) ≈ 0.00368 underestimates the true
value by a factor greater than 2, and the situation here might be analogous to
that for sub-Latin squares considered in [25]. In that paper, it is conjectured
that the expected number of 3 × 3 sub-Latin squares of a randomly chosen
n × n Latin square tends to 1/18 as n tends to inﬁnity, and numerical data
show that the value given by the random model for a ﬁxed parameter, f (n) =

12(n
3
)3n
−9, underestimates the computed value for small parameters. For
example, for n = 10, the asymptotic value (≈ 0.0556) is closer to the exact
value (≈ 0.0536) than f (n) (≈ 0.0207).
It is not clear whether an STS with subsystems is more or less prone
to have resolutions. If the correlation is weak, then the fact that there are
12,520,021 isomorphism classes of Kirkman triple systems of order 21 with
sub-STS(7)s [17] could be used to calculate

12,520,021/α ≈ 2.111 · 109,

which would hint that there might be somewhat more than 1 billion isomor-
phism classes of Kirkman triple systems of order 21.

12

Table 3: Numbers of STS(21)s with no sub-STS(7)s

O A #

2 C2 40,201,112
3 C3 1,540,602
4 C 2
2 3,007
5 C5 1,772
6 C6 533
6 S3 279
7 C7 39
8 D8 9
9 C 2
3 95
9 C9 7
12 A4 44
12 C6 × C2 18
18 C 2
3 ⋊ C2 1
 O A #

18 C18 2
18 C3 × S3 1
18 C6 × C3 5
21 C21 1
21 C7 ⋊ C3 7
24 C3 × D8 1
24 S4 1
27 C 2
3 ⋊ C3 3
36 C3 × A4 4
42 C3 × D14 1
54 C 2
3 ⋊ C6 1
126 C3 × (C7 ⋊ C6) 1
504 C3 × PSL(3, 2) 1

Appendix

The program developed for determining the abstract type of an automor-
phism group can be applied also to those STS(21)s with nontrivial auto-
morphisms from [10] that do not contain sub-STS(7)s. Such information is
presented in Table 3 using the notation described in Section 3.

Acknowledgements

The authors are grateful to Petteri Kaski for providing the STS(21)s with
nontrivial automorphisms classiﬁed in [10].

References

[1] L. Babai, Almost all Steiner triple systems are asymmetric, Ann. Discrete
Math. 7 (1980), 37–39.

[2] A. Betten, G. Brinkmann, and T. Pisanski, Counting symmetric conﬁgura-
tions v3, Discrete Appl. Math. 99 (2000), 331–338.

[3] M. B. Cohen, C. J. Colbourn, L. A. Ives, and A. C. H. Ling, Kirkman triple
systems of order 21 with nontrivial automorphism group, Math. Comp. 71
(2002), 873–881.
 13

[4] C. J. Colbourn, Triple systems, in: C. J. Colbourn and J. H. Dinitz (Eds.),
Handbook of Combinatorial Designs, 2nd ed., Chapman & Hall/CRC, Boca
Raton, 2007, pp. 58–71.

[5] C. J. Colbourn and A. Rosa, Triple Systems, Clarendon Press, Oxford, 1999.

[6] J. Edmonds, Paths, trees, and ﬂowers, Canad. J. Math. 17 (1965), 449–467.

[7] K. Fukuda and T. Matsui, Finding all the perfect matchings in bipartite
graphs, Appl. Math. Lett. 7(1) (1994), 15–18.

[8] The GAP Group, GAP – Groups, Algorithms, and Programming, Version
4.11.0, https://www.gap-system.org (2020).

[9] S. N. Kapralov and S. Topalova, On the Steiner triple systems of order 21
with automorphisms of order 3, in: Proc. Third International Workshop
on Algebraic and Combinatorial Coding Theory (Voneshta Voda, Bulgaria,
22–28 June, 1992), pp. 105–108.

[10] P. Kaski, Isomorph-free exhaustive generation of designs with prescribed
groups of automorphisms, SIAM J. Discrete Math. 19 (2005), 664–690.

[11] P. Kaski and P. R. J. Östergård, The Steiner triple systems of order 19,
Math. Comp. 73 (2004), 2075–2092.

[12] P. Kaski and P. R. J. Östergård, One-factorizations of regular graphs of order
12, Electron. J. Combin. 12 (2005), #R2.

[13] P. Kaski and P. R. J. Östergård, Classiﬁcation Algorithms for Codes and
Designs, Springer, Berlin, 2006.

[14] P. Kaski, P. R. J. Östergård, and A. Popa, Enumeration of Steiner triple
systems with subsystems, Math. Comp. 84 (2015), 3051–3067.

[15] P. Kaski, P. R. J. Östergård, S. Topalova, and R. Zlatarski, Steiner triple
systems of order 19 and 21 with subsystems of order 7, Discrete Math. 308
(2008), 2732–2741.

[16] P. Kaski and O. Pottonen, libexact user’s guide, version 1.0, HIIT Technical
Reports 2008-1, Helsinki Institute for Information Technology HIIT, 2008.

[17] J. I. Kokkala and P. R. J. Östergård, Kirkman triple systems with subsys-
tems, Discrete Math. 343 (2020), 111960.

[18] J. I. Kokkala and P. R. J. Östergård, Sparse Steiner triple systems of order
21, J. Combin. Des. 29 (2021), 75–83.

[19] M. Kwan, Almost all Steiner triple systems have perfect matchings, Proc.
London Math. Soc. (3) 121 (2020), 1468–1495.

14

[20] C. W. H. Lam and Y. Miao, Cyclically resolvable cyclic Steiner triple systems
of order 21 and 39, Discrete Math. 219 (2000), 173–185.

[21] R. A. Mathon, K. T. Phelps, and A. Rosa, A class of Steiner triple systems of
order 21 and associated Kirkman systems, Math. Comp. 37 (1981), 209–222
and 64 (1995), 1355–1356.

[22] R. Mathon and A. Rosa, The 4-rotational Steiner and Kirkman triple sys-
tems of order 21, Ars Combin. 17A (1984), 241–250.

[23] R. Mathon and A. Rosa, 2-(v, k, λ) designs of small order, in: C. J. Col-
bourn and J. H. Dinitz (Eds.), Handbook of Combinatorial Designs, 2nd ed.,
Chapman & Hall/CRC, Boca Raton, 2007, pp. 25–58.

[24] B. D. McKay and A. Piperno, Practical graph isomorphism, II, J. Symbolic
Comput. 60 (2014), 94–112.

[25] B. D. McKay and I. M. Wanless, Most Latin squares have many subsquares,
J. Combin. Theory Ser. A 86 (1999), 322–347.

[26] M. Meringer, Fast generation of regular graphs and construction of cages, J.
Graph Theory 30 (1999), 137–146.

[27] R. W. Quackenbush, Algebraic speculations about Steiner systems, Ann.
Discrete Math. 7 (1980), 25–35.

[28] G. Royle, Graphs and multigraphs, in: C. J. Colbourn and J. H. Dinitz
(Eds.), Handbook of Combinatorial Designs, 2nd ed., Chapman & Hall/CRC,
Boca Raton, 2007, pp. 731–740.

[29] D. R. Stinson and E. Seah, 284457 Steiner triple systems of order 19 contain
a subsystem of order 9, Math. Comp. 46 (1986), 717–729.

[30] V. D. Tonchev, Steiner triple systems of order 21 with automorphisms of
order 7, Ars Combin. 23 (1987), 93–96; and 39 (1995), 3.

[31] S. Topalova, STS(21) with automorphisms of order 3 with 3 ﬁxed points and
7 ﬁxed blocks, Math. Balkanica (N.S.) 18 (2004), 215–221.

15
