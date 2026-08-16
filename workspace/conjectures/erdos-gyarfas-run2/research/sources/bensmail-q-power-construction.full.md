<!-- source: https://bibliotekanauki.pl/articles/31342133.pdf | converted from PDF -->

Discussiones Mathematicae
Graph Theory 37 (2017) 211–220
doi:10.7151/dmgt.1926

ON q-POWER CYCLES IN CUBIC GRAPHS

Julien Bensmail

Department of Applied Mathematics and Computer Science
Technical University of Denmark
DK-2800 Lyngby, Denmark

e-mail: julien.bensmail.phd@gmail.com

Abstract

In the context of a conjecture of Erd˝os and Gy´arf´as, we consider, for
any q ≥ 2, the existence of q-power cycles (i.e., with length a power of q) in
cubic graphs. We exhibit constructions showing that, for every q ≥ 3, there
exist arbitrarily large cubic graphs with no q-power cycles. Concerning the
remaining case q = 2 (which corresponds to the conjecture of Erd˝os and
Gy´arf´as), we show that there exist arbitrarily large cubic graphs whose all
2-power cycles have length 4 only, or 8 only.
Keywords: cubic graphs, q-power cycles, Erd˝os-Gy´arf´as conjecture.

2010 Mathematics Subject Classiﬁcation: 68R10, 05C38.

1. Introduction

Throughout this note, given some q ≥ 2, by a q-power cycle of some undirected
simple graph G, we refer to a cycle of G whose length is a power of q. Our work
is related to the following conjecture attributed to Erd˝os and Gy´arf´as (see [1]).

Conjecture 1 (Erd˝os and Gy´arf´as). Every graph with minimum degree at least
3 has a 2-power cycle.

Although Erd˝os and Gy´arf´as themselves suspected that Conjecture 1 should
admit counterexamples, the question is still open in general. Conjecture 1 being
seemingly complicated, only a few works have been dedicated to it. Markstr¨om,
through a computer search, proved that any cubic counterexample to Conjecture
1 should have at least 30 vertices [4]. He also exhibited small cubic graphs whose
all 2-power cycles have length 16. Conjecture 1 was nevertheless veriﬁed in some
situations, such as for planar claw-free graphs (by Daniel and Shauger [2]), and

212 J. Bensmail

for K1,m-free graphs with minimum degree at least m + 1 or maximum degree at
least 2m − 1 (by Shauger [6]). More recently, the conjecture was also veriﬁed for
3-connected planar cubic graphs by Heckman and Krakovski [3]. More details on
this subject may be found in [5].
Caro, as reported by West [7], raised, in the context of Conjecture 1, a more
general question about whether every graph with minimum degree at least 3 has
a cycle whose length is a non-trivial power of some natural number.

Conjecture 2 (Caro). For every graph G with minimum degree at least 3, there
is a natural number q ≥ 2 such that G has qp-cycles for some p > 1.

Conjecture 1, if true, would basically answer positively to Conjecture 2 (with
setting q = 2). We here consider a generalization of Conjecture 1, which is
obtained by ﬁxing q in Conjecture 2, and whose some particular cases will be
answered in this note.

Question 3. For any q ≥ 2, does every large enough graph with minimum degree
at least 3 have a q-power cycle?

Although quite natural in the context of Conjecture 1 (the case q = 2 of Question
3 is exactly Conjecture 1), we did not ﬁnd any progress on Question 3 in literature.
We here exhibit constructions yielding a negative answer to Question 3 for
every q ≥ 3. These constructions all provide graphs being cubic and planar. As
our construction tools and techniques do not apply for the case q = 2 of Question
3, this conﬁrms that this remaining case, Conjecture 1, is by far the hardest case.

2. Terminology and Constructions

Most of our constructions are based on the following scheme. We start from an
internally cubic tree, namely a tree whose all non-leaf nodes have degree exactly
3. Clearly an internally cubic tree may have arbitrarily large order. In order to
get a cubic graph with no q-power cycles for some given q, the main idea now is
to start from some internally cubic tree T , and make T cubic by attaching some
gadgets to its leaves. So that we control the lengths of the cycles we create in
this way, one way to proceed is to attach gadgets to the leaves of T in such a way
that all leaves of T remain articulation vertices in the obtained cubic graph G.
In doing so, the only cycles in G will be the cycles in the gadgets used to raise
the degrees — so we just need to ﬁnd such gadgets with no q-power cycles.
We will mainly use two kinds of degree-raising gadgets — see Figure 1 for
an illustration of the described operations. The ﬁrst kind of gadgets are called
edge-gadgets. The main property of an edge-gadget G is that it is a subcubic
graph with only two vertices t1 and t2, called the ends of G, being of degree less

On q-Power Cycles in Cubic Graphs 213

than 3. Furthermore, t1 and t2 must be of degree exactly 1 in G. Basically, an
edge-gadget G with ends t1 and t2 can be used to replace an edge is some graph
H: assuming uv is an edge of H, one may just delete uv, add a copy of G to H,
identify u and t1, and identify v and t2 in H. In doing so, note that the degrees
of u and v are not aﬀected by the operation. Edge-gadgets can also be used to
raise by 2 the degree of any vertex w of H. To that end, one may just add a loop
at w, and replace that loop by an edge-gadget, in the same fashion as described
above.
 G
t1 t2

u v
 v
 u1

u2

u3
 G

t1

t2

t3

Figure 1. Replacing an edge by an edge-gadget (left), and a degree-3 vertex by a vertex-
gadget (right).

The second kind of gadgets we will use are vertex-gadgets. A vertex-gadget
G is a subcubic graph with only three vertices t1, t2 and t3, or ends, being of
degree less than 3, with t1, t2 and t3 being of degree exactly 2 in G. This time,
a vertex-gadget G with ends t1, t2 and t3 can be used to replace a vertex v with
degree 3 in a graph H: assuming u1, u2 and u3 are the three neighbours of v in
H, one may just delete v from H, add a copy of G to H, and match the vertices
among {t1, t2, t3} with those among {u1, u2, u3}. Note that if H is cubic, then of
course the obtained graph remains cubic after the modiﬁcation.

3. Cubic Graphs with no q-Power Cycles for q ≥ 3

We now exhibit constructions yielding, for any ﬁxed q ≥ 3, arbitrarily large cubic
planar graphs with no q-power cycles. We start by considering the case q ≥ 6,
before considering every remaining case separately.

3.1. Case q ≥ 6

The main gadget we use in this section is the edge-gadget G depicted in Figure
2, whose two ends are t1 and t2, and whose number k ≥ 1 of internal columns is
parametrized. We note that, for every k, the diﬀerent cycle lengths of G, as well
as the path lengths from t1 to t2, are easily deduced.

214 J. Bensmail

t1 t2

k columns

Figure 2. The edge-gadget G used for the case q ≥ 6.

Observation 4. Assume k ≥ 1 is ﬁxed. All cycles of G have length among {3, 4,
. . . , 2k + 2}.

Observation 5. Assume k ≥ 1 is ﬁxed. All {t1, t2}-paths of G have length among
{k + 3, k + 4, . . . , 2k + 3}.

Figure 3. The gadget G
′ used for the case q ≥ 6.

We will also make use of the gadget G′ depicted in Figure 3, where we call
the white vertex of G′ its root. We note the following.

Observation 6. All cycles of G′ have length among {3, 4, 5, 6, 7}.

We are now ready to construct a graph H with no q-power cycles for any
ﬁxed q ≥ 6. Start from H being an internally cubic tree. Now consider every leaf
v of T , add a new copy of G′ to H, and identify v and the root of G′. Note that,
so far, all cycles of H are the cycles in the copies of G′. To ﬁnish the construction,
consider every gadget G′ we attached to H, and replace every of its edges by a
copy of G. Now each cycle of H is either a cycle of G or goes through some copies
of G following some cycle of G′.

Observation 7. All cycles of H have length among

{3, 4, . . . , 2k + 2} ∪ {3k + 9, 3k + 10, . . . , 14k + 21}.

On q-Power Cycles in Cubic Graphs 215

Proof. As said above, a cycle C of H uses either (1) edges from a single copy
of G, or (2) edges of several copies of G following some cycle of G′. In situation
(1), from Observation 4 we know that the length of C is among {3, 4, . . . , 2k + 2}.
Now, in situation (2), C goes through several G’s following some cycle in G′.
Since the cycles in G′ have length among {3, 4, 5, 6, 7} according to Observation
6, and all {t1, t2}-paths of G have length among {k+3, k+4, . . . , 2k+3} according
to Observation 5, the smallest possible length for C is 3(k + 3) = 3k + 9 while
the biggest possible length for C is 7(2k + 3) = 14k + 21.

Corollary 8. If q ∈ {2k + 4, 2k + 5}, then H has no q-power cycle.

Proof. According to Observation 7, all cycles of H have length among

L = {3, 4, . . . , 2k + 2} ∪ {3k + 9, 3k + 10, . . . , 14k + 21}.

We remark ﬁrst that q ̸∈ L, so H has no q-cycle. Now note that q2 ∈ {4k2 +
16k + 16, 4k2 + 20k + 25}, which is strictly greater than 14k + 21 as long as k ≥ 1.
So, as long as k ≥ 1, which is always veriﬁed, H has no qp-cycle for any p ≥ 2.
So H has no q-power cycle.

The conclusion is then the following.

Theorem 9. For every q ≥ 6, there exist arbitrarily large planar cubic graphs
having no q-power cycles.

Proof. Consider the construction of H above. The original internally cubic tree
can be taken arbitrarily large — so H has arbitrarily large order. To now make
sure that H has no q-power cycle, just perform the construction with choosing k
so that q ∈ {2k + 4, 2k + 5}, which is possible since q ≥ 6. The conclusion follows
from Corollary 8.

3.2. Case q = 5

The main gadget to be used in this section is the vertex-gadget G depicted in
Figure 4, whose ends are t1, t2 and t3. Its cycle and path lengths properties of
interest here are the following.

Observation 10. All cycles of G have length among {3, 4}.

Observation 11. For every two distinct ends ti and tj of G, all {ti, tj}-paths of
G have length among {6, 7, 8}.

Now consider the multigraph G′ depicted in Figure 5, whose white vertex is
the root of G′. Clearly, we have the following.

Observation 12. All cycles of G′ have length among {2, 5}.

216 J. Bensmail

t1
 t3t2
 Figure 4. The vertex-gadget G used for the case q = 5.

Figure 5. The gadget G
′ used for the case q = 5.

We now describe how to obtain a cubic graph H with no 5-power cycles.
Start from H being an internally cubic tree. For every leaf v of H, identify v
and the root vertex of a new copy of G′. Finally consider every vertex v of H
(hence of degree 3) belonging to some copy of G′, and replace v by a copy of H
(as described in Section 2). Due to the symmetric structure of G, note that we
do not have to care about how the replacement is done (i.e., how the vertices
are joined). Furthermore, the only cycles in H are cycles in some copies of G, or
cycles going through copies of G following some cycle in G′. In particular, every
such cycle cannot go twice through a single copy of G.

Observation 13. All cycles of H have length among

{3, 4} ∪ {14, 15, . . . , 18} ∪ {35, 36, . . . , 45}.

On q-Power Cycles in Cubic Graphs 217

Proof. Let C be a cycle of H. If C is completely included in one of the copies of
G, then C has length among {3, 4} according to Observation 10. Now, if C goes
through several copies of G, then, according to the arguments above, it goes only
through 2 or 5 copies of G according to Observation 12. Recall that, when going
through a copy of G, cycle C uses 6, 7 or 8 of its edges (Observation 11). In case
C goes through exactly two copies of G, the length of C is among {14, 15, . . . , 18}.
Now, if C goes through exactly ﬁve copies of G, then the length of C is among
{35, 36, . . . , 45}. This concludes the proof.

Observation 13 now gives our conclusion, since the original internally cubic
tree from which H is constructed can be arbitrarily large.

Theorem 14. There exist arbitrarily large planar cubic graphs having no 5-power
cycles.

3.3. Case q = 4

We herein need the edge-gadget G depicted in Figure 6, whose ends are t1 and
t2. Its properties of interest are the following.
 t1

t2

Figure 6. The edge-gadget G used for the case q = 4.

Observation 15. All cycles of G have length among {3} ∪ {5, 6, . . . , 14}.

Observation 16. All {t1, t2}-paths of G have length among {7, 8, . . . , 15}.

We now construct a cubic graph H with no 4-power cycles. Start from H
being an internally cubic tree. Now consider every leaf v of H, and add a loop
at v. Note that H is now cubic. Finally replace every such loop by a new copy
of G. It should be clear that H remains cubic, and that the only cycles of H are
located at its “leaves”. We make it more formal below.

218 J. Bensmail

Observation 17. All cycles of H have length among

{3} ∪ {5, 6, . . . , 15}.

Proof. Consider a cycle C in H. It should be clear that C cannot include two
vertices of H belonging to the original internally cubic tree from which H was
constructed (because of its 1-connectivity). So C is either completely included in
some copy of G, in which case C has length among {3} ∪ {5, 6, . . . , 14} (Obser-
vation 15), or is actually a path from t1 to t2 in G. In the latter, C has length
among {7, 8, . . . , 15} according to Observation 16. This concludes the proof.

Once again, since the original internally cubic tree (from which H is con-
structed) can be arbitrarily large, from Observation 17 we get the following.

Theorem 18. There exist arbitrarily large planar cubic graphs having no 4-power
cycles.

3.4. Case q = 3

We will here use the edge-gadget G with ends t1 and t2 depicted in Figure 7. Its
properties are the following.

t1 t2

Figure 7. The edge-gadget G used for the case q = 3.

Observation 19. All cycles of G have length among {4, 6, 8}.

Observation 20. All {t1, t2}-paths of G have length among {13, 14, . . . , 25}.

To obtain a cubic graph H with no 3-power cycles, just repeat the construc-
tion from Section 3.3 but with using the gadget G introduced in this section. We
then get the following.

Observation 21. All cycles of H have length among

{4, 6, 8} ∪ {13, 14, . . . , 25}.

Proof. The proof of Observation 17 can just be mimicked in the current context.
The statement then follows from Observations 19 and 20.

For the same reasons as in Section 3.3, we can now state the following.

Theorem 22. There exist arbitrarily large planar cubic graphs having no 3-power
cycles.

On q-Power Cycles in Cubic Graphs 219

4. Discussion

In this paper, we have considered a generalization of Conjecture 1, namely Ques-
tion 3, and obtained some results about it. We have exhibited several construc-
tions conﬁrming that Conjecture 1, not surprisingly, is the hardest particular case
of Question 3.
A few side results can be deduced from our results. Since the case q = 4 of
Question 3 is wrong, we get that, in the context of Conjecture 1, there exists a
family of arbitrarily large planar cubic graphs whose only 2-power cycles have
length an odd power of 2. Similar statements may of course be formulated for
any power of 2 greater than 4.

t1 t2
 t1

t2

Figure 8. The edge-gadgets mentioned in the discussion section.

We also note that our constructions can be easily modiﬁed to get arbitrarily
large planar cubic graphs whose 2-power cycles are all of the same length. To
obtain such graphs whose all 2-power cycles are 4-cycles, we can just apply the
construction in Section 3.3 but with using, as G, the ﬁrst (left) edge-gadget
depicted in Figure 8. Similarly, to obtain such graphs whose all 2-power cycles
are 8-cycles, we can just repeat the same construction but with using, as G, the
second (right) edge-gadget depicted in Figure 8. Towards Conjecture 1, it could
be interesting to investigate whether, for any larger power of 2, say 2k > 8, there
exist inﬁnite families of cubic graphs whose all 2-power cycles have length 2k.

220 J. Bensmail

Acknowledgements

The author would like to thank the anonymous referees for their positive and
constructive comments.
 References

[1] P. Erd˝os, Some old and new problems in various branches of combinatorics, Discrete
Math. 165/166 (1997) 227–231.
doi:10.1016/S0012-365X(96)00173-2

[2] D. Daniel and S.E. Shauger, A result on the Erd˝os-Gy´arf´as conjecture in planar
graphs, Congr. Numer. 153 (2001) 129–139.

[3] C.C. Heckman and R. Krakovski, Erd˝os-Gy´arf´as conjecture for cubic planar graphs,
Electron. J. Combin. 20 (2013) #P7.

[4] K. Markstr¨om, Extremal graphs for some problems on cycles in graphs, Congr. Nu-
mer. 171 (2004) 179–192.

[5] P.S. Nowbandegani, H. Esfandiari, M.H.S. Haghighi and K. Bibak, On the Erd˝os-
Gy´arf´as conjecture in claw-free graphs, Discuss. Math. Graph Theory 34 (2014)
635–640.
doi:10.7151/dmgt.1732

[6] S.E. Shauger, Results on the Erd˝os-Gy´arf´as conjecture in K1,m-free graphs, Congr.
Numer. 134 (1998) 61–65.

[7] D. West, Erd˝os-Gy´arf´as conjecture on 2-power cycle lengths, Open Problems—
Graph Theory and Combinatorics.
http://www.math.illinois.edu/∼dwest/openp/2powcyc.html

Received 3 October 2015
Revised 18 March 2016
Accepted 30 March 2016

Powered by TCPDF (www.tcpdf.org)
