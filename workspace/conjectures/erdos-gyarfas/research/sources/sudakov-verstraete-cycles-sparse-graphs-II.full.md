<!-- source: https://arxiv.org/pdf/1010.5309 | converted from PDF -->

arXiv:1010.5309v1  [math.CO]  26 Oct 2010
Cycles in sparse graphs II

Benny Sudakov ∗ Jacques Verstra¨ete †

Abstract

The independence ratio of a graph G is deﬁned by

ι(G) := sup
X⊂V (G)
 |X|
α(X) ,

where α(X) is the independence number of the subgraph of G induced by X. The independence
ratio is a relaxation of the chromatic number χ(G) in the sense that χ(G) ≥ ι(G) for every graph G,
while for many natural classes of graphs these quantities are almost equal. In this paper, we address
two old conjectures of Erd˝os on cycles in graphs with large chromatic number and a conjecture of
Erd˝os and Hajnal on graphs with inﬁnite chromatic number.

1 Introduction

Let G be a graph and let α(X) be the size of a largest independent set in the subgraph of G induced
by X. The independence ratio of a graph G is deﬁned by

ι(G) := sup
X⊂V (G)
 |X|
α(X) .

The independence ratio of a graph G is a relaxation of the chromatic number χ(G), since χ(G) ≥ ι(G)
for all graphs G. For many interesting classes of graphs, including random and pseudorandom graphs,
the chromatic number and independence ratio are equal or almost equal. On the other hand, so-called
Kneser graphs are examples of graphs on n vertices with constant independent ratio and chromatic
number of order log n [15]. In this paper, we are motivated by three conjectures on cycles in graphs
with large chromatic number. We give partial evidence for the truth of each conjecture by considering
graphs with large independence ratio.

1.1 Erd˝os’ conjecture on many cycles

Erd˝os [5] conjectured that a triangle-free graph with chromatic number k contains cycles of at least
k2−o(1) diﬀerent lengths as k → ∞. The conjecture of Erd˝os remains open, and in fact no lower bound
better than linear in k is known for the longest cycle in a triangle-free graph with chromatic number
k. In general, Theorem 2 in [20] shows that a graph of chromatic number k and no cycle of length g
contains cycles of Ω(k⌈(g−1)/2⌉) diﬀerent lengths. In this paper, we prove the following theorem which
shows in a very strong sense that Erd˝os’ conjecture is true for graphs with large independence ratio:

∗Department of Mathematics, UCLA, Los Angeles, CA 90095. Email: bsudakov@math.ucla.edu. Research supported
in part by NSF CAREER award DMS-0812005 and by a USA-Israeli BSF grant.
†Department of Mathematics, University of California, La Jolla, CA, 92093. E-mail: jverstraete@ucsd.edu. Research
supported in part by NSF Grant DMS-0800704 and an Alfred P. Sloan Research Fellowship.

1

Theorem 1 Every triangle-free graph with independence ratio at least k ≥ 3 has cycles of Ω(k2 log k)
consecutive lengths.

We prove this theorem in Section 2.5, after some preliminary results in Sections 2.1 – 2.4. The
important result by Kim [13] establishing the order of magnitude of triangle-complete graph Ramsey
numbers r(3, t) = Θ(t2/ log t) shows that there are triangle-free graphs with independence ratio k and
with O(k2 log k) vertices, so the above result is best possible up to the value of the implicit constant.

1.2 Hereditary Properties

Theorem 1 is part of a more general theorem on hereditary properties – families of graphs closed under
taking induced subgraphs. To describe the general theorem, let P be a hereditary property and let
f : [1, ∞) → [1, ∞) be an increasing bijection. Then we say that P has speed at most f if for every
n ∈ N and every n-vertex graph G ∈ P , we have ι(G) ≤ f (n). Since the identity function f (x) = x
for x ∈ [1, ∞) serves as an upper bound for the speed of every hereditary property, the speed of each
hereditary property is well-deﬁned. We shall prove the following theorem:

Theorem 2 Let f : [1, ∞) → [1, ∞) be an increasing bijection. If P is a hereditary property with
speed at most f , then any graph G ∈ P with ι(G) > 18k + 4 has cycles of at least 1
2 f −1(k) consecutive
lengths.

This theorem is proved in Section 2.6. Theorem 2 applies in general to the property PH of H-free
graphs – this is the hereditary property of graphs which do not contain any copy of H. For example,
one can obtain an appropriate generalization of Theorem 1.

Theorem 3 Let G be a Ks+1-free graph and suppose ι(G) > 18k + 4. Then G contains cycles of at
least 1
2 (k/s)s/(s−1) consecutive lengths.

Clearly this theorem holds also for all H-free graphs where H has s+1 vertices. We prove Theorem 3 in
Section 2.7. One can improve the lower bound (k/s)s/(s−1) in the above theorem by a polylogarithmic
factor which, for s = 3, agrees with Theorem 1, but this involves only further computations and so
will be omitted.

1.3 Erd˝os’ conjecture on unavoidable cycles

Erd˝os [7] oﬀered one thousand dollars for a satisfactory resolution of the following problem: in a graph
of inﬁnite chromatic number, which cycle lengths should appear? For example, Erd˝os conjectured that
a graph of suﬃciently large chromatic number has a cycle of length a prime. We show that if an n-
vertex graph has independence ratio at least 3 exp(8 log∗n), then not only does it contain a cycle of
prime length, it contains cycles of lengths from many other sparse inﬁnite sequences of integers. Here
log∗n is the number of times the natural logarithm must be applied to n to get a number less than
one, and in what follows, we write logb n for the logarithm base b, and omit the base if the logarithm
is the natural logarithm. We prove the following theorem:

2

Theorem 4 Let σ be an inﬁnite increasing sequence of positive integers satisfying σ1 ≥ 3 and log σr ≤
σr−1 for all r ≥ 2. If G is an n-vertex graph and

ι(G) ≥ σ1 exp(8 log∗n),

then G contains a cycle of length in the sequence σ.

Theorem 4 is proved in Section 3. We claimed that an n-vertex graph G with ι(G) ≥ 3 exp(8 log∗n)
contains a cycle of length a prime. Let pr denote the rth prime number. Then Bertrand’s Postulate
gives pr+1 ≤ 2pr for all r ∈ N, and so log pr+1 ≤ log pr + 1 ≤ pr for all r ∈ N. Applying Theorem 4 to
this sequence, we see that a graph G with ι(G) > 3 exp(8 log∗n) contains a cycle of length a prime, as
claimed. Theorem 4 gives a similar upper bound for much sparser sequences, such as powers of three,
or 2 + 1, 22 + 1, 222 + 1, . . . and so on.

An important remark is that Theorem 4 distinguishes between the independence ratio and the chro-
matic number: generalizations of Mycielski’s well-known construction of triangle-free graphs of arbi-
trarily large chromatic number provide constructions for inﬁnitely many n of an n-vertex graph Gn of
chromatic number χ(Gn) = Ω((log n)/(log log n)) with no cycle of length in a prescribed sequence σ
satisfying log σr ≤ σr−1 for r ≥ 2. The conclusion of Theorem 4 therefore does not hold if we replace
ι(G) with χ(G) in the theorem. We present the details of this construction in Section 5.

1.4 Erd˝os-Hajnal conjecture

Let C(G) = {ℓ : Cℓ ⊂ G} denote the set of cycle lengths in a graph G. Erd˝os [7] proposed the study
of the quantity
 L(G) = ∑

t∈C(G)
 1
t

and conjectured that in a graph of inﬁnite chromatic number, L(G) diverges. This conjecture was
proved by Gy´arf´as, Komlos and Szemer´edi [12]. Speciﬁcally, they proved that if G is a ﬁnite graph of
minimum degree d, then there exists ǫ > 0 such that

L(G) ≥ ǫ log d.

This is best possible up to the value of the constant ǫ, since the complete bipartite graph has L(Kd,d) ≤
1
2 log d+1. It follows that L(G) diverges when G has inﬁnite chromatic number, since a graph of inﬁnite
chromatic number contains a graph of minimum degree at least d for each d ∈ N. The result above
therefore does not rely on the chromatic number as much as the existence of subgraphs of arbitrarily
large average degree. Erd˝os and Hajnal [7, 9] conjectured that in a graph with inﬁnite chromatic
number, the sum of reciprocals of odd cycle lengths diverges. If C◦(G) is the set of lengths of odd
cycles in G, their conjecture states that if G is a graph of inﬁnite chromatic number, then

L◦(G) := ∑

t∈C◦(G)
 1
t = ∞.

In this paper, we give some evidence for this conjecture by showing:

3

Theorem 5 For any graph G on n vertices,

L◦(G) ≥ 1
2 log ι(G) − 8 log∗n.

We prove Theorem 5 in Section 4. This theorem is best possible up to the O(log∗n) term, in the sense
that L◦(Kt) ≤ 1
2 log ι(Kt) + 1. It would be interesting as a ﬁrst step to the Erd˝os-Hajnal conjecture
to show that L◦(G) diverges when G is a graph with inﬁnite independence ratio.

2 Preliminary results

In this section, we present the results necessary for the proofs of Theorems 1–5. The following notation
will be used. If G is a graph, then ι(G) is its independence ratio and α(G) is its independence number.
For a set X ⊂ V (G), we denote by ∂GX the set of vertices of V (G)\X adjacent to at least one vertex
in X. We sometimes omit the subscript G when it is clear which graph is being referred to. We write
α(X) for the independence number of the subgraph of G induced by X. Fixing a vertex v ∈ V (G), it
is convenient to let Ni(v) denote the set of vertices at distance exactly i from v.

2.1 Expanding subgraphs

The starting point for proving Theorems 1 – 4 is to show that graphs with large independence ratio
have nice expansion properties. Precisely, we make the following deﬁnitions:

Deﬁnition. We say that a graph G is k-expanding on independent sets if every independent set I in
G has |∂GI| > k|I|. A graph G is weakly k-expanding on independent sets if for some v ∈ V (G), every
independent set I ⊂ V (G)\{v} has |∂GI| > k|I|.

We notice in particular that if a graph is weakly k-expanding on independent sets, then all but at
most one vertex in the graph has degree more than k.

Lemma 1 Let k ≥ 1. Then every n-vertex graph G with α(G) < n/(k + 1) has an induced subgraph
that is k-expanding on independent sets and a 2-connected subgraph that is weakly k-expanding on
independent sets.

Proof. First we show that G has a subgraph H that is k-expanding on independent sets. Let
G0 = G. If G0 has no subgraph H as above, then there is an independent set I0 ⊂ V (G0) such that
|∂I0| ≤ k|I0|. Let G1 = G − I0 − ∂I0. Then there is an independent set I1 ⊂ V (G1) with |∂I1| ≤ k|I1|.
Let G2 = G1 − I1 − ∂I1. Continuing in this way, we eventually remove independent sets I0, I1, . . . , Ir
and their neighborhoods ∂I0, ∂I1, . . . , ∂Ir and this exhausts all the vertices in the graph:

V (G0) =
 r⋃

j=0
(Ij ∪ ∂Ij).

However, the set I = ⋃r
j=0 Ij is an independent set of size at least n/(k + 1) in G = G0, which is a
contradiction. Therefore there exists H ⊂ G that is k-expanding on independent sets. This proves
the ﬁrst statement of the lemma.
 4

To prove the second statement, if H is 2-connected, then we are done. If H is not 2-connected, let F
be an endblock of H – this is a maximal 2-connected subgraph of H containing exactly one cut vertex
v of H. Then for any independent set I ⊂ V (F )\{v},

|∂F I| = |∂H I| > k|I|.

So F is weakly k-expanding on independent sets. This completes the proof.

Ajtai, Koml´os and Szemer´edi [1] showed that if G is an n-vertex triangle-free graph, then α(G) =
Ω(
√n log n). Their result was improved by Shearer [17], who showed that if G is an n-vertex triangle-
free graph of maximum degree d ≥ 2, then

α(G) ≥ n(d log d − d + 1)
(d − 1)2 .

A straightforward calculation gives the following result:

Lemma 2 For n ≥ e15, every n-vertex triangle-free graph G has

α(G) > ( n log n
2
 )1/2.

Proof. Let m = ( n log n
2 )1/2. If G is a triangle-free n-vertex graph of maximum degree d, then
α(G) ≥ n/(d + 1) and the lemma follows easily for d ≤ 1. Suppose d ≥ 2. Observing that the
neighborhood of any vertex of G is an independent set, we obtain from Shearer’s bound,

α(G) ≥ max{d, n(d log d − d + 1)
(d − 1)2
 }.

If d > m, then we easily recover the bound in the lemma . If 2 ≤ d ≤ m, the second expression is a
decreasing function of d and so it is minimized when d = m. In this case we get

α(G) ≥ n(m log m − m + 1)
(m − 1)2

> n(log m − 1)
m

≥ ( n log n
2
 )1/2 + (log log n − 2 − log 2)n1/2

(2 log n)1/2 .

Since n ≥ e15, log log n ≥ 2 + log 2, and so we have the required bound.

The second deﬁnition we require is that of expansion on arbitrary sets of vertices in a graph:

Deﬁnition. A graph G is k-expanding on sets of size at most T if |∂GX| > k|X| for every X ⊂ V (G)
of size at most T . A graph G is weakly k-expanding on sets of size at most T if for some v ∈ V (G),
every set X ̸= {v} of size at most T has |∂GX| > k|X|.

Lemma 3 If G is an n-vertex triangle-free graph with α(G) < n/(3k + 1) and k ≥ e15, then G
contains a 2-connected subgraph H that is weakly 2-expanding on sets of size at most k2 log k and
weakly 3k-expanding on independent sets.
 5

Proof. Pass to a 2-connected subgraph H ⊂ G which is weakly 3k-expanding on independent sets,
using Lemma 1. Then for some v ∈ V (H), every independent set I ⊂ V (H)\{v} has |∂H I| > 3k|I|.
Let X ⊂ V (H) satisfy |∂HX| ≤ 2|X| where X ̸= {v}. If u ∈ X\{v}, then

|∂HX| ≥ |∂H {u}| − |X| > 3k − |X|.

If |X| < e15, then since k ≥ e15 we obtain |∂H X| > 2|X|. If |X| ≥ e15, then H[X] is a triangle-free
graph with at least e15 vertices. Suppose |X\{v}| = x. By Lemma 2, there is an independent set
I ⊂ X\{v} such that
 |I| ≥ ( x log x
2
 )1/2 ≥ 3,

Consequently, |X| − |I| ≤ x − 2 and therefore

2|X| = 2x + 2 ≥ |∂H X|

≥ |∂H I| − |X| + |I|

> 3k|I| − x + 2

≥ 3k · ( x log x
2
 )1/2 − x + 2.

This implies 2x > k2 log x and therefore x > k2 log k. This completes the proof.

2.2 P´osa’s lemma and long cycles

A well-known result of P´osa [16] shows how to ﬁnd long paths in graphs which are 2-expanding on sets
of size at most T : in this case one obtains a path of length at least 3T . To describe P´osa’s Lemma and
the variant we use, we require some notation. If P = v1v2 . . . vm is a longest path in a graph G and
{v1, vi} is an edge of G, consider a path Q = vi−1 . . . v1vi . . . vm of the same length as P , obtained by
adding edge {v1, vi} and deleting edge {vi−1, vi} from P . We say that Q was obtained from P via an
elementary rotation, which keeps endpoint vm ﬁxed. The set of all vertices of P which are endpoints of
paths obtained by repeated elementary rotations from P with ﬁxed endpoint vm is denoted by S(P ).
The following variant of P´osa’s Lemma (see Lemma 2.7 in [3]) is our starting point:

Proposition 1 Let T ≥ 1, and let G be a graph that is 2-expanding on sets of size at most T . Then
for any longest path P ⊂ G there is a cycle C ⊂ H of length at least 3T containing S(P ) ∪ ∂S(P ).

We require a slight adjustment of this proposition to accommodate weak 2-expansion: recall that
G is weakly 2-expanding on sets of size at most T if for some v ∈ V (G) and every set X ⊂ V (G)
with X ̸= {v}, |∂GX| > 2|X|. The proof of the proposition below is almost identical to the proof of
Proposition 1 given in [3].

Proposition 2 Let T ≥ 1, and let G be a graph that is weakly 2-expanding on sets of size at most
T . Then there exists a longest path P ⊂ G and a cycle C ⊂ H of length at least 3T containing
S(P ) ∪ ∂S(P ).

Proof. By deﬁnition of weak expansion, for some v ∈ V (G) and every X ⊂ V (G) with X ̸= {v} we
have |∂GX| > 2|X|. Let P be a longest path in G and let v1 ̸= v be an endpoint of P and vm the

6

other endpoint. The crucial step in the proof of Proposition 1 is that ∂S(P ) ⊂ S(P )− ∪ S(P )+, where
S(P )− is the set of vertices preceding S(P ) on P and S(P )+ is the set of vertices succeeding S(P )
on P . Since |S(P )−| ≤ |S(P )| and |S(P )+| ≤ |S(P )|, we must have |∂S(P )| ≤ 2|S(P )|. Since G is
weakly 2-expanding on sets of size at most T , we must have S(P ) = {v} or |S(P )| > T . However
since v1 ̸= v, |∂G{v1}| > 2 which shows that |S(P )| > 1 and therefore S(P ) ̸= {v}. It follows that
|S(P )| > T . To construct a cycle containing S(P ) ∪ ∂S(P ), let y be the last vertex of ∂S(P ) on P .
The segment of P from v1 to y contains all vertices of S(P ) ∪ ∂S(P ), otherwise any vertex of S(P )
after y on P would be distinct from vm and then the vertex after it on P would be an element of
∂S(P ), contradicting that y is the last vertex of ∂S(P ) on P . If x ∈ S(P ) is a neighbor of y in G, and
Q is a path from x to vm obtained by elementary rotations from P , then Q contains the segment of
P from y to vm. Moreover, starting from x, Q traverses all vertices of S(P ) ∪ ∂S(P ) before reaching
y and then continues along segment of P from y to vm. So Q together with the edge {x, y} forms the
required cycle. Since |S(P ) ∪ ∂S(P )| ≥ 3T , this cycle has the required length.

Combining Lemma 3 with Proposition 2, we arrive at the following theorem, which shows that triangle-
free graph with large independence ratio contains a very long cycle.

Theorem 6 Let G be a triangle-free graph with ι(G) > 3k + 1 where k ≥ e15. Then G has a cycle of
length at least 3k2 log k.

Proof. By Lemma 3, there is a 2-connected graph H ⊂ G that is weakly 2-expanding on sets of size
at most k2 log k. By Proposition 2, there is a cycle C ⊂ H of length at least 3k2 log k in G, completing
the proof.

2.3 Long odd cycles with chords

A chord of a cycle is an edge which joins two non-consecutive vertices of the cycle. To prove Theorem
1, we need to extend Theorem 6 further to obtain a long odd cycle with a chord.

Proposition 3 Let k ≥ e15 and let G be an n-vertex triangle-free graph with α(G) < n/(3k + 1).
Then G contains a non-bipartite graph consisting of a cycle of length at least 1
2 k2 log k with at least
one chord.

Proof. By Lemma 3, G contains a 2-connected subgraph H that is weakly 2-expanding on sets of
size at most k2 log k and weakly 3k-expanding on independent sets. By Proposition 2, there is a cycle
C ⊂ H of length at least 3T := 3k2 log k containing S(P ) ∪ ∂H S(P ) for some longest path P with
|S(P )| ≥ T . The vertices of S(P ) are called special vertices, and since ∂HS(P ) ⊂ V (C), all their
neighbors are vertices of C. Since H is weakly 3k-expanding on independent sets, all but at most one
vertex of H has degree more than 3k ≥ e15. In particular, every special vertex has two neighbors on
C which are not adjacent to that special vertex on C. If V (C) induces a non-bipartite subgraph of H,
then we are done – take C together with an appropriate chord of C. Suppose V (C) induces a bipartite
subgraph of H. Since H is weakly 3k-expanding on independent sets, χ(H) ≥ ι(H) > 3k ≥ e15. In
particular, H − V (C) is certainly non-bipartite and contains an odd cycle D. By 2-connectivity of
H, there exist two vertex disjoint paths Q′
1 and Q′
2 from V (D) to V (C) whose internal vertices are in
H−V (C)−V (D). In particular, there exist w1, w2 ∈ V (C) such that there are both even and odd length

7

paths Q1 and Q2 respectively and V (Q1)∩V (C) = {w1, w2} = V (Q2)∩V (C). Indeed, let Qi consist of
Q′
1 ∪ Q′
2 together with a subpath of D of length congruent to |E(Q′
1)| + |E(Q′
2)| + i modulo two, for i ∈
{1, 2}. Let P1 and P2 denote the two w1w2-subpaths of C, and suppose P1 contains at least 1
2 T special
vertices. If P1 has a chord, then P1 ∪ Q1 or P1 ∪ Q2 is the required non-bipartite subgraph. If P1 has
no chord, then at least 1
2 T special vertices on P1 each have at least two neighbors in V (P2)\{w1, w2}.
Pick a special vertex w ∈ V (P1) and neighbors x1, x2 ∈ N (w) ∩ V (P2). We assume that the order
of appearance of vertices on C is w1, w, w2, x2, x1 clockwise. For a, b ∈ V (C), let C(a, b) denote the
internal vertices of the subpath of C from a to b in the clockwise order where a precedes b. Consider
the paths R1 = C − C(x1, w1) − C(w, w2) + {w, x1} and R2 = C − C(w2, x2) − C(w1, w) + {w, x2}.
The path R1 is shown by dotted lines and arrows in the ﬁgure below. Then R1 ∪ R2 = C and {w, x2}
is a chord of R1 and {w, x1} is a chord of R2. One of these paths has length at least 1
2 |V (C)| > T ,
and together with Q1 or Q2 forms the required non-bipartite subgraph.

w1
 w2

x1
 x2

w
 C
 D

2.4 Consecutive cycle lengths

The main ingredient for ﬁnding cycles of many consecutive lengths in graphs is the following proposi-
tion [21]:

Proposition 4 Let F be a non-bipartite graph comprising a cycle with a chord, and let (A, B) be a
non-trivial partition of V (F ). Then for each ℓ ≤ |V (F )| − 1, there exists a path in F of length ℓ with
one endpoint in A and the other endpoint in B.

We illustrate the argument which will be used repeatedly in the rest of the paper. Recall that Ni(v)
denotes the set of vertices at distance exactly i from a given vertex v in a graph.

Proposition 5 Let G be a graph and suppose that Ni(v) contains a non-bipartite graph F comprising
a cycle of length L together with a chord. Then G contains cycles of L consecutive lengths, the shortest
of which has length at most 2i + 1.
 8

Proof. Consider a breadth-ﬁrst search tree rooted at v, and let T be a minimal subtree whose set of
leaves is V (F ). Then T branches at its root, and we let A be the set of leaves of T in one branch,
and B the remaining set of leaves of T . Then A ∪ B = V (F ) and A, B partition V (F ). Now we use
Proposition 4: there exists a path in F of length ℓ whose ﬁrst vertex is in A and whose last vertex is in
B for all ℓ ≤ |V (F )|−1. If T has height h, then we obtain cycles of lengths 2h+1, 2h+2, . . . , 2h+L−1
in H, as required. Furthermore, since h ≤ i, the shortest cycle has length 2h + 1 ≤ 2i + 1.

2.5 Proof of Theorem 1

Theorem 1 states that a triangle-free graph G with ι(G) ≥ k ≥ 3 contains cycles of Ω(k2 log k)
consecutive lengths. It is enough to prove the following quantitative version of this statement: let G
be a triangle-free graph with ι(G) > 18k + 4 where k ≥ e15, then G contains cycles of at least k2 log k
consecutive lengths. Pass to a subgraph F of G such that α(F ) < |V (F )|/(18k + 4). By Lemma
1, F has a subgraph H that is 18k + 3-expanding on independent sets. In this subgraph, pick any
vertex v and consider Ni := Ni(v) for i ∈ N. If for some i ∈ N, ι(Ni) > 3(2k) + 1, then Proposition 3
shows that the subgraph induced by Ni(v) contains a non-bipartite graph consisting of an odd cycle of
length at least 1
2 (2k)2 log 2k > k2 log k with at least one chord. In this case, the theorem follows from
Proposition 5. Otherwise, we have ι(Ni) ≤ 6k + 1 for every i ∈ N. In that case, α(Ni) ≥ |Ni|/(6k + 1)
and Ni contains and independent set I of size at least |Ni|/(6k + 1). Since H is 18k + 3-expanding on
independent sets, we conclude |∂I| > 3|Ni|. In particular, since

∂I ⊂ Ni ∪ Ni−1 ∪ Ni+1,

for all i ∈ N we have |Ni+1| + |Ni−1| > 3|Ni| − |Ni| = 2|Ni|.

Then |N0| = 1 and, since H is 18k + 3-expanding on independent sets, every vertex of H has degree
more than 18k + 3, so |N1| > 18k + 3 > |N0|. We easily obtain |Ni+1| > |Ni| by induction for all i ∈ N,
which is clearly impossible since H is a ﬁnite graph so some Ni must be empty. This completes the
proof.

2.6 Hereditary Properties

In this subsection we prove Theorem 2. The proof of Theorem 2 is almost identical to the proof of
Theorem 1 given over the last three sections, so we merely indicate how to generalize each component
of that proof. Throughout this section, k ≥ 1 and f : [1, ∞) → [1, ∞) is an increasing bijection and P
is a hereditary property. For a general hereditary property, the following lemma generalizes Lemma 3.

Lemma 4 Let P denote any hereditary property with speed at most f and G ∈ P where |V (G)| = n
and let k ≥ 1. If α(G) < n/(6k + 1) then G has a 2-connected subgraph that is weakly 2-expanding on
sets of size at most f −1(k) and weakly 3k-expanding on independent sets.

Proof. We repeat the proof of Lemma 3. Pass to a 2-connected subgraph H ⊂ G which is weakly
6k-expanding on independent sets, using Lemma 1: for some v ∈ V (H) and every independent set
I ⊂ V (H)\{v} we have |∂H I| > 6k|I|. Let X ⊂ V (H) with X ̸= {v}, and suppose |∂H X| ≤ 2|X|. If
X = {x}, then x ̸= v and |∂H {x}| > 6k > 2|X| so we have |X| ≥ 2. Since P is a hereditary property

9

of speed at most f , there is an independent set I ⊂ X\{v} such that |I| ≥ (|X| − 1)/f (|X| − 1), since
the subgraph of H induced by X is in P . Consequently,

2|X| ≥ |∂H X| ≥ |∂HI| − |X| + |I| > 6k|I| − |X|

and so 2k|I| < |X|. So if |∂H X| ≤ 2|X|, then

2k(|X| − 1)/f (|X| − 1) ≤ 2k|I| < |X|

from which we get f (|X| − 1) > 2k(|X| − 1)/|X| ≥ k since |X| ≥ 2. It follows that |X| > f −1(k).

Using this lemma, we obtain the following straightforward generalization of Proposition 3 for hereditary
properties.

Proposition 6 Let P be a hereditary property with speed at most f and G ∈ Pn and let k ≥ 1. If
α(G) < n/(6k + 1), then G contains a non-bipartite graph consisting of a cycle of length at least
1
2 f −1(k) with at least one chord.

Proof of Theorem 2. Let G ∈ P have ι(G) > 18k + 4 where k ≥ 1. By Lemma 1, G has a subgraph
H that is 18k + 3-expanding on independent sets. In this subgraph, pick any vertex v and consider
Ni = Ni(v) for i ∈ N. If for some i ∈ N, ι(Ni) > 6k + 1, then Proposition 6 shows that the subgraph
induced by Ni(v) contains a non-bipartite graph F consisting of a cycle of length at least 1
2 f −1(k)
with at least one chord. In this case, the theorem follows from Proposition 5. Otherwise, we have
ι(Ni) ≤ 6k + 1 for every i ∈ N. In that case, α(Ni) ≥ |Ni|/(6k + 1). Since H is 18k + 3-expanding on
independent sets, we conclude |Ni−1∪Ni∪Ni+1| > 3|Ni|, which leads to the contradiction |Ni| > |Ni−1|
for all i ∈ N, as in Theorem 1.

2.7 The property of H-free graphs

To prove Theorem 3, we compute an upper bound for the speed of Ps+1, the family of Ks+1-free
graphs. Note that if a graph contains Ks+1, then it contains a copy of every graph H on s + 1 vertices,
and in this case PH ⊂ Ps+1. We bound the speed using a well-known upper bound on the Ramsey
number r(Ks+1, Kt+1):

Proposition 7 If a graph G has at least (s+t
s ) vertices, then it contains a clique of order s + 1 or an
independent set of order t + 1. In particular, Ps+1 has speed at most fs where fs(x) = min{x, sx1−1/s}
for x ∈ [1, ∞).

Proof. The ﬁrst statement is a well-known bound on Ramsey numbers r(Ks+1, Kt+1). Note that
(s+t
s ) ≤ (st)s for all s, t ≥ 1. It follows that for any m-vertex Ks+1-free graph H, there is an
independent set of size at least t + 1 in H whenever m ≥ (st)s. By deﬁnition, an n-vertex graph
Ks+1-free graph G has
 ι(G) = sup
X⊂V (G)
 |X|
α(X) ≤ sup
1≤(st)s≤n
 (st)s

t + 1 < sn1−1/s.

We also have ι(G) ≤ n. This completes the proof.

10

For each ﬁxed s, the function fs in the last proposition is a continuous increasing function on [1, ∞)
with fs(1) = 1, and therefore fs : [1, ∞) → [1, ∞) is an increasing bijection. Applying Theorem 2, if
G ∈ Ps+1 and ι(G) > 18k + 4, then G contains cycles of at least 1
2 f −1(k) consecutive lengths. Since

f −1(k) = max{k, (k/s)
s/(s−1)} ≥ (k/s)
s/(s−1)

we conclude that a graph G ∈ Ps+1 with ι(G) > 18k + 4 has cycles of at least 1
2 (k/s)s/(s−1) consecutive
lengths. This completes the proof of Theorem 3. □

Remark. By using better bounds on r(Ks+1, Kt+1), Theorem 3 can be improved by logarithmic
factors of k, as we achieved for triangles. However computing bounds on the speed of Ps+1 is then
more cumbersome, so for simplicity we avoid these calculations.

3 Proof of Theorem 4

We are given a sequence σr satisfying log σr ≤ σr−1, and we have to prove that any graph G with
ι(G) > σ1 exp(8 log∗ n) contains a cycle of length σr for some r. We begin with some notation. Let
τ denote any inﬁnite increasing subsequence of σ with τ1 = σ1 and let Pr denote the property of all
graphs containing no cycle of any length σj ≤ τr. Deﬁne

△r := max{σj − σj−1 : σj ≤ τr}.

We deﬁne τ0 = 1 = △1. To prove Theorem 4, we ﬁrst prove the following more general theorem:

Theorem 7 Let σ be an inﬁnite increasing sequence of positive integers with σ1 ≥ 3 and let τ be an
arbitrary subsequence of σ with τ1 = σ1 and △r deﬁned as above. Then any n-vertex graph G ∈ Pr
has
 ι(G) < 27
rσ1 exp( r∑

i=1
 2 log △i
τi−1 + 2 log n
τr
 )
.

Before proving this theorem, we show how to derive Theorem 4 from it:

Proof of Theorem 4. In Theorem 4, we are given a sequence σ with log σr ≤ σr−1 for r ≥ 2. Let
T (r) denote the rth element of the sequence

σ1 e
σ1 e
eσ1 · · ·

Since log σr ≤ σr−1, there is an element σ between T (r − 1) and T (r) for all r ≥ 2, which we deﬁne
to be τr. We now apply Theorem 4 with this sequence τ = (τr)r∈N and τ1 = σ1. Then choose the
smallest value of r such that τr > 2 log n. Since T (r) is at least a tower of es of height r, we note that
r ≤ log∗n. The key fact is that r∑

i=1
 2 log △i
τi−1 ≤ 2r

since log △r ≤ τr−1 for all r ≥ 2. In conclusion, from Theorem 7, we have

ι(G) < 27
rσ1 exp(2r + 1) < σ1 exp(8 log∗n)

11

and this completes the proof. □

Proof of Theorem 7. Theorem 7 is a consequence of the following claim:

Claim 1. Let r, m ∈ N and δr = 1/⌈τr/2⌉. Then every m-vertex graph G ∈ Pr has

α(G) ≥ 1
ar m1−δr .

where ar is deﬁned by
 a1 = 27σ1 and ar = 27ar−1△δr−1
r .

To see how Theorem 7 follows, take a graph G ∈ Pr with n vertices; then Claim 1 shows

ι(G) ≤ sup
X⊂V (G)
 |X|
α(X) ≤ sup
X⊂V (G)
 |X|
1
ar |X|1−δr = arnδr

since we can apply Claim 1 with m = |X| to the subgraph of G induced by each set X ⊂ V (G). The
linear recurrence ar = 27ar−1△δr−1
r gives

ar = 27
rσ1
 r∏

i=1 △δi−1
i ≤ (27)
rσ1 exp( r∑

i=1
 2 log △i
τi−1
 )

and therefore
 ι(G) ≤ arnδr ≤ 27
rσ1 exp( r∑

i=1
 2 log △r
τr−1 + 2 log n
τr
 )
.

We proceed to the proof of Claim 1.

Proof of Claim 1. The claim is true for P1 using early known bounds on cycle-complete Ramsey
numbers [8] (see also [21]): for σ ∈ {2ℓ + 1, 2ℓ + 2},

r(CL, Kt) < 27σ1t1+1/ℓ

from which we obtain the required lower bound. Suppose r > 1 and that Claim 1 has been proved
for every graph in Pr−1, but that the claim is false for Pr. We ﬁrst compute an upper bound for the
speed of Pr−1.

Claim 1.1. The property Pr−1 has speed at most f where

f (x) = min{x, ar−1xδr−1} for x ∈ [1, ∞).

Proof of Claim 1.1. Since Claim 1 holds for Pr−1, we have that every p-vertex graph F ∈ Pr−1 satisﬁes

α(F ) ≥ 1
ar−1 p1−δr−1

12

This implies
 ι(F ) = sup
X⊂V (G)
 |X|
α(X) ≤ ar−1pδr−1.

Therefore Pr−1 has speed at most f where

f (x) = min{x, ar−1xδr−1}

for x ≥ 1, as required. □

Since by assumption Claim 1 does not hold for Pr, for some m ∈ N there exists an m-vertex graph
G ∈ Pr such that
 α(G) < 1
ar m1−δr .

Using Lemma 1, pass to an induced subgraph H of G which is armδr -expanding on independent sets.
For the rest of the proof of Claim 1, we work in the subgraph H of G to derive a contradiction.

Claim 1.2. For any v ∈ V (H) and any positive integer j ≤ 1/δr,

α(Nj(v)) > 3|Nj(v)|
ar .

Proof of Claim 1.2. Fix j ≤ 1/δr and let Hj be the subgraph of H induced by Nj(v). For convenience,
let hj = |Nj(v)| = |V (Hj)|. If α(Hj) > hj/9, then the proof of Claim 1.2 is complete, since ar ≥
9σ1 ≥ 27 for all r ∈ N. We may therefore write α(Hj) = hj/(6k + 1) where k ≥ 1 is a real number. By
Proposition 6, if f is an upper bound for the speed of Pr−1, then Hj contains a non-bipartite graph
comprising a cycle of length at least 1
2 f −1(k) with a chord. It is important to note that Pr ⊂ Pr−1
and therefore Hj ∈ Pr−1. By Claim 1.1,

f −1(k) = max{k, (k/ar−1)
1/δr−1} ≥ (k/ar−1)
1/δr−1.

By Proposition 5, H contains cycles of at least 1
2 f −1(k) consecutive lengths, the shortest of which has
length at most 2j + 1 ≤ τr. By deﬁnition of △r, and since G ∈ Pr, we must have 1
2 f −1(k) ≤ △r.
Recall that r ≥ 2 and therefore δr−1 ≤ 1/2, ar−1 ≥ 81. Rearranging this inequality, and using
α(Hj) = hj/(6k + 1), we obtain
 α(Hj) > hj
9ar−1△δr−1
r .

By deﬁnition of ar, the denominator is ar/3, as required. □

Since H is armδr -expanding on independent sets, we have for any j ≤ 1/δr and any maximum inde-
pendent set I in Hj, |∂H Nj(v)| ≥ |∂H I| > 3mδr · hj.

Since ∂HNj(v) ⊂ Nj(v) ∪ Nj−1(v) ∪ Nj+1(v), we conclude that

hj+1 + hj−1 > (3mδr − 1)hj ≥ 2mδr hj.

We also have h0 = 1 and h1 > 2mδr , since H is armδr -expanding on independent sets. Now the
recurrence inequality hj + hj−1 > (2c)hj with h0 = 1 and h1 > 2c has hj > cj for all j. With c = mδr ,
we obtain hj > mjδr for all j ≤ 1/δr, and in particular we obtain the contradiction hj > m = |V (G)|
when j = 1/δr. This completes the proof of Claim 1, and hence Theorem 7. □

13

4 Proof of Theorem 5

We are given an n-vertex graph G with ι(G) ≥ t and we have to show

L◦(G) ≥ 1
2 log t − 8 log∗n.

This is clearly true if t ≤ exp(16 log∗n) so we assume t > exp(16 log∗n). We let s = t/ exp(8 log∗n),
and consider the disjoint intervals of odd numbers:

Si = [si, si+1) ∩ (2N + 1)

for i ≥ 0. If for some i we have Si ⊂ C(G), then

L◦(G) ≥ 1
2 log s ≥ 1
2 log t − 8 log∗n

and the proof is complete. Otherwise, for each i we pick σi ∈ Si\C(G). Then we have deﬁned a
sequence σ with σi ≤ sσi+1. Let τ be a subsequence of σ such that log τr ≤ τr−1 and such that τr is
contained in the interval Si for which σ1T (r) ≥ si+1 − 1 but σ1T (r) < si+2 − 1. Here T (r) is a tower
of es of height r. Note that τr is well deﬁned, since intervals Si cover all numbers. We also let τ1 = σ1.
Applying Theorem 7 with this sequence τ and choosing r such that τr > 2 log n, we have r ≤ log∗n
and ι(G) < 27
rσ1 exp(2r + 1) < σ1 exp(8 log∗n) < s exp(8 log∗n) < t.

This contradiction completes the proof. □

5 Constructions

In this section, we give constructions which show that the conclusion of Theorem 4 does not hold if
ι(G) is replaced with the chromatic number χ(G).

Construction. The existence of triangle-free graphs with arbitrarily large chromatic number was
explicitly established by the so-called Mycielski graphs. A survey is given in [19]. These constructions
were generalized (see page 213 in [19]) to give, for each k, r ∈ N where r is odd, a graph Gk,r with
chromatic number k and no odd cycle of length at most r and with |V (Gk,r)| = 23−k(r + 2)k−2. We
observe that |V (Gk,r)| ≤ rk − 1 for every r, k ≥ 3, so we let G′
k,r consist of Gk,r together with enough
isolated vertices so that |V (G′
k,r)| = rk − 1 := n. Note that n is even. Provided that log(n + 1) ≤ r,
the increasing sequence σ of odd integers in {3, 5, . . . , r} ∪ {n + 1, n + 3, . . . } satisﬁes the requirements
of Theorem 4 and yet Gk,r has no cycle of length in σ. For instance, if we take k = ⌊r/ log r⌋ and
k ≥ 3, then n + 1 = rk ≤ er so log(n + 1) ≤ r, and

χ(Gk,r) = k ≥ ⌊ log(n + 1)
log log(n + 1)
 ⌋ ≫ exp(8 log∗n) .

It follows that while χ(Gk,r) is substantially larger than the bound exp(8 log∗n) for the independence
ratio in Theorem 4, Gk,r has no cycles of length in the sequence σ.

14

6 Concluding remarks

• We remark that the chromatic number can be arbitrarily large relative to the independence ratio
of a graph. Consider the Kneser graph Kn:r whose vertex set is all subsets of {1, 2, . . . , n} of size
r, and whose edges consisting of pairs of disjoint subsets of {1, 2, . . . , n} of size r. By Lov´asz’s
Theorem [15], χ(Kn:r) = n − 2r + 2. By the Erd˝os-Ko-Rado Theorem [10], α(Kn:r) = (n−1
r−1) and
therefore ι(Kn:r) ≥ n/r. If n = sr where s > 2 then for any set X ⊂ Kn:r, we claim α(X) ≤ |X|/s. To
see this, given any collection of |X| subsets of {1, 2, . . . , sr} of size r, there exists an i ∈ {1, 2, . . . , sr}
such that i is contained in at least r|X|/sr = |X|/s of the sets of size r. The sets containing i therefore
form an independent set of size at least |X|/s in Kn:r. Consequently ι(Ksr:r) ≤ s and we conclude
ι(Ksr:r) = s. Writing |V (Ksr:r)| = N , we obtain N = (sr
r ) < (es)r and therefore

χ(Kn:r) > ι(G) − 2
log ι(G) + 1 log N.

A good example is the Kneser graph K3r,r with N = (3r
r ) vertices, which has independence ratio three
and chromatic number Θ(log N ).

• The Erd˝os-Hajnal conjecture [7, 9] remains open. A partial step would be to show that if G is a
graph with inﬁnite independence ratio, then L◦(G) is inﬁnite, whereas in this paper we showed L◦(G) >
1
2 log ι(G) − 8 log∗n when G is an n-vertex graph. Perhaps it is true that L◦(G) > 1
2 log χ(G) − O(1) for
any ﬁnite graph G, although this is an even stronger question than the Erd˝os-Hajnal [9] conjecture.

References

[1] M. Ajtai, J. Koml´os, E. Szemer´edi, A note on Ramsey numbers, Journal of Combin. Theory Ser.
A 29 (1980) no. 3, 354–360.

[2] N. Alon, J. Spencer, The Probabilistic Method, 2nd ed., J. Wiley (2000).

[3] S. Brandt, H. Broersma, R. Diestel and M. Kriesell, Global connectivity and expansion: long
cycles and factors in f -connected graphs, Combinatorica 26 (2006), 17–36.

[4] Y. Caro, Y. Li, C. Rousseau and Y. Zhang, Asymptotic bounds for some bipartite graph-complete
graph Ramsey numbers, Discrete Mathematics 220 (2000), 51-56.

[5] P. Erd˝os, Some of my favourite problems in various branches of combinatorics, Matematiche
(Catania) 47 (1992), 231–240.

[6] P. Erd˝os, Some of my favorite solved and unsolved problems in graph theory, Quaestiones Math.
16 (1993), 333–350.

[7] P. Erd˝os, Some old and new problems in various branches of combinatorics. Graphs and combi-
natorics (Marseille, 1995). Discrete Math. 165/166 (1997), 227–231.

[8] P. Erd˝os, R. Faudree, C. Rousseau and R. Schelp, On cycle-complete graph Ramsey numbers, J.
Graph Theory 2 (1978), 53-64.
 15

[9] P. Erd˝os, A. Hajnal, On chromatic number of graphs and set-systems. Acta Math. Acad. Sci.
Hungar 17 (1966) 61–99.

[10] P. Erd˝os, C. Ko, R. Rado, Intersection theorems for systems of ﬁnite sets, Quarterly Journal of
Mathematics, Oxford Series, series 2 (1961) no. 12, 313-?320.

[11] A. Gy´arf´as, Graphs with k odd cycle lengths, Discrete Mathematics 103 (1992), 41–48.

[12] A. Gy´arf´as, J. Koml´os and E. Szemer´edi, On the distribution of cycle lengths in graphs, J. Graph
Theory 8 (1984), 441–462.

[13] J. Kim, The Ramsey number R(3; t) has order of magnitude t2/ log t, Random Struc- tures and
Algorithms 7 (1995), 173-207.

[14] L. Lov´asz, Combinatorial Problems and Exercises, 2nd Ed., North-Holland, Amsterdam,
1993.

[15] L. Lov´asz, Kneser’s conjecture, chromatic number, and homotopy. J. Combin. Theory Ser. A 25
(1978), no. 3, 319–324.

[16] L. P´osa, Hamiltonian circuits in random graphs, Discrete Mathematics 14 (1976), 359–364.

[17] J. Shearer. A note on the independence number of triangle-free graphs. Discrete Mathematics 46,
no. 1 (1983), 83–87.

[18] B. Sudakov, A note on odd cycle-complete graph Ramsey numbers. Electron. J. Combin. 9 (2002),
no. 1, Note 1, 4 pp. (electronic).

[19] H. Sachs, M. Stiebitz, On constructive methods in the theory of colour-critical graphs. Discrete
Mathematics 74, 1-2 (1989), 201–226.

[20] B. Sudakov and J. Verstraete, Cycle lengths in sparse graphs, Combinatorica 28 (2008), 357–372.

[21] J. Verstraete, Arithmetic progressions of cycle lengths in graphs, Combinatorics, Probability and
Computing 9 (2000), 369–373.

[22] J. Verstraete, Unavoidable cycle lengths in graphs. Journal of Graph Theory 49 (2005), no. 2
151–167.
 16
