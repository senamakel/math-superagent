<!-- source: https://export.arxiv.org/pdf/math/0204222v1.pdf | converted from PDF -->

arXiv:math/0204222v1  [math.CO]  17 Apr 2002
On Arithmetic Progressions of Cycle Lengths in
Graphs

Jacques Verstra¨ete
Department of Pure Mathematics and Mathematical Statistics
Centre for Mathematical Sciences
Wilberforce Road, Cambridge CB3 OWB
England August 1999.
jbav@microsoft.com

Abstract
A recently posed question of H¨aggkvist and Scott’s asked whether
or not there exists a constant c such that if G is a graph of minimum
degree ck then G contains cycles of k consecutive even lengths. In
this paper we answer the question by proving that for k ≥ 2, a
bipartite graph of average degree at least 4k and girth g contains
cycles of (g/2 − 1)k consecutive even lengths. We also obtain a
short proof of the theorem of Bondy and Simonovits, that a graph
of order n and size at least 8(k − 1)n1+1/k has a cycle of length 2k.

Erd˝os and Burr [4] conjectured that for every odd number k, there is a
constant ck such that for every natural number m, every graph of average
degree at least ck contains a cycle of length m modulo k. Erd˝os and Burr [4]
settled their conjecture in the case m = 2 and Robertson (see [4]) settled the
case m = 0. The full conjecture was resolved by Bollob´as [1], who proved
the conjecture with ck = 2[(k + 1)k − 1]/k. In this paper, we show that
ck = 8k will do. Thomassen [11] later showed cycles of all even lengths
modulo k are obtained under the hypothesis that the average degree is at
least 4k(k + 1), without requiring k to be odd. Thomassen [10] also proved
that if G is a graph of minimum degree at least three and girth at least
2(k2 + 1)(3 · 2k2 +1 + (k2 + 1)2 − 1), then G contains cycles of all even lengths
modulo k.
 1

Bondy and Vince [3] proved that in a graph in which all but at most
two vertices have degree at least three, there exist two cycles whose lengths
diﬀer by at most two. This answered a conjecture of Erd˝os and was also
studied by H¨aggkvist and Scott [8]. Recently, H¨aggkvist and Scott [7],
considered extending this to considering arithmetic progressions of cycle
lengths in graphs. H¨aggkvist and Scott [7] proved that if G is a graph of
minimum degree at least 300k2 then G contains k + 1 consecutive even cycle
lengths. The same authors asked if a linear bound on the minimum degree
is possible. In this paper, we answer the question of H¨aggkvist and Scott in
the following theorem.

Theorem 1 Let k ≥ 2 be a natural number and G a bipartite graph of

average degree at least 4k and girth g. Then there exist cycles of (g/2 − 1)k

consecutive even lengths in G. Moreover, the shortest of these cycles has

length at most twice the radius of G.

This result generalises the above-mentioned result of Bollob´as and partly
generalises that of Thomassen, insofar as Thomassen’s result is valid for
graphs of minimum degree at least three, whereas the result above requires
average degree at least eight. The graph Kk,n−k shows that we require the
average degree to be at least about 2k to ensure the conclusion of Theorem
1.
 The following lemma lies at the heart of the proof of Theorem 1. It was
originally inspired by methods used by Gy´arf´as, Koml´os and Szemer´edi [6].
Whilst this paper was being written, the lemma was discovered to be implicit
in a lemma of Bondy and Simonovits [2]. Nevertheless, the proof is short
and is retained here for completeness.

Lemma 2 Let H be a graph comprising a cycle with a chord. Let (A, B)

be a non-trivial partition of V (H). Then H contains A–B paths of every

length less than |H|, unless H is bipartite with bipartition (A, B).

2

Proof. Label the vertices of the cycle 0, 1, . . . , n − 1 where n = |H|.
Suppose H does not contain A–B paths of every length less than n, and let
m be the smallest integer for which there is no A–B path of length m not
using the chord; m > 1 since (A, B) is a non-trivial partition of V (H). We
remark also that m ≤ n/2, or H would contain A–B paths of all lengths
less than n.

Now χ(j) = χ(j + m) for every j ∈ V (H), where χ is the characteristic
function of A (label arithmetic is modulo n). Let d = hcf(n, m). Then there
are integers p and q such that pm + qn = d; hence χ(j) = χ(j + d) for every
j. But then there is no A–B path of length d round the cycle; thus d = m
and m | n. In particular, A–B paths of every length less than m exist by
the deﬁnition of m, so A–B paths of every length other than multiples of m
exist by periodicity of χ.

We ﬁnd paths of the remaining lengths km, 1 ≤ k ≤ n/m − 1, using the
chord. Suppose ﬁrst that the chord joins two vertices within distance m on
the cycle, say 0 and r where 1 < r ≤ m. There exist A–B paths of length
m+r−1 round the cycle; thus χ(j) ̸= χ(j+m+r−1) for some j, −m < j ≤ 0.
But j + m + r − 1 ≥ r, so the path j, j + 1, . . . , 0, r, r + 1, . . . , j + km + r − 1
is an A–B path of length km provided j + km + r − 1 < n + j, which holds
for all the desired k ≤ n/m − 1.

So we may suppose the chord is 0r, where m < r < n − m. Let −m <
j < 0 and consider the paths j, j + 1, . . . , 0, r, r − 1, . . . , r − j − m + 1 and
m+j, m+j −1, . . . , 0, r, r+1, . . . , r−j −1, of length m. If either of them is an
A–B path we can extend it, by m vertices at a time, to A–B paths of lengths
km, k ≥ 1, until the number of unused vertices in the two arcs deﬁned by
the chord is less than m in each arc. At this point km + 1 ≥ n − 2(m − 1),
and as m | n, km = n − m as desired. Likewise, if either of the two paths
0, r, r − 1, . . . , r − m + 1 and 0, r, r + 1, r + m − 1 is an A–B path then H
contains paths of all lengths less than |H|.

Thus it follows, as χ(j) = χ(m + j), that for −m < j < 0 we have
χ(r − j − m + 1) = χ(r − j − 1) and that χ(r − m + 1) = χ(r + m − 1),
implying χ(r − j + 1) = χ(r − j − 1) and χ(r + m + 1) = χ(r + m − 1).

3

So χ(v + 2) = χ(v) for all r ≤ v < r + m, and so for all v ∈ V (H). Hence
m = 2.

We conclude, therefore, that |H| is even and the vertices of the cycle
are alternately in A and in B. It is immediately seen that, under these
circumstances, if the chord joins two vertices in the same class then H
contains A–B paths of all lengths less than |H|. Consequently, the chord
joins A to B, so H is bipartite, with bipartition (A, B).

Lemma 3 Let k ≥ 2 be a natural number and let G be a graph of average

degree at least 2k and girth g. Then G contains a cycle of length at least

(g − 2)k + 2, with at least one chord.

Proof. It is easily seen that a graph G of average degree at least 2k
contains a subgraph H of minimum degree at least k + 1. If P is a longest
path in H, then an endvertex v of P has all its neighbours on P . Some
neighbour u of v is at distance at least (g − 2)k + 1 from v on P . Hence
P + uv is a cycle of length at least (g − 2)k + 2. As k + 1 ≥ 3, this cycle has
at least one chord.

Proof of Theorem 1. We may assume that G is connected and let the
radius of G be rad(G). Choose a central vertex v0 ∈ V (G), and let Vi denote
the set of vertices a distance i from v0 in G. Then there exists l such that
Vl ∪ Vl+1 spans a graph G′ with at least k|Vl ∪ Vl+1| edges. By Lemma 3,
ﬁnd H ⊂ G′ comprising a cycle, of length at least (g − 2)k + 2, with a
chord. Let T ′ be a minimal subtree of T , restricted to ⋃
i≤l Vi, such that T ′

contains V (H) ∩ Vl. The minimality of T ′ ensures that it branches at its
root. Now let A be the set of vertices of H in one of these branches and let
B = V (H)\A. By Lemma 2, and as (A, B) is not the bipartition of H, there
are A–B paths of all lengths up to (g −2)k +1, all disjoint from T ′ −end(T ′).
Each A–B path of even length s, together with a subpath of T ′ between the
ends of such a path, gives rise to a cycle of length s + 2r, where r is the
distance from Vl to the root of T ′. Note that, as G is bipartite, all paths of

4

even length with one end in A have their other end in Vl. This gives cycles
C2r+2, C2r+4, .., C2r+(g−2)k, of (g/2 − 1)k consecutive even lengths, and since
v0 is a central vertex, 2r + 2 ≤ rad(G), as required.

We deﬁne the even girth of a graph G to be the length of a shortest even
cycle in G. Theorem 1 easily extends to general graphs, as is shown by the
following corollary.

Corollary 4 Let k ≥ 2 be a natural number, and let G be a graph of average

degree at least 8k and even girth g. Then there are cycles of (g/2 − 1)k

consecutive even lengths in G.

Proof. This follows from the observation that a graph of average degree
at least 8k has a spanning bipartite subgraph of average degree at least 4k,
and then applying Theorem 1 to this bipartite subgraph.

In the case of graphs of average degree at least 6k, we may also argue
as follows. Given a vertex v0, let Vl denote the vertices a distance l from
v0. Then either there exists l such that Vl ∪ Vl+1 spans a bipartite graph of
average degree at least 2k, or there exists l such that Vl spans a graph of
average degree at least 2k. In the former case, the method of Theorem 1 gives
cycles of all even lengths in an integer interval of form [2r+1, 2r+(g−2)k+1]
and the latter case gives (also following the proof of Theorem 1) cycles of
all odd lengths in an integer interval of form [2r + 1, 2r + (g − 2)k + 1]. So
we have the following theorem:

Theorem 5 Let k ≥ 2 be a natural number, and let G be a graph of average

degree at least 6k and girth g. Then, for some odd number r ≥ 3, there exist

cycles of all even lengths or all odd lengths in the interval [r, r + (g − 2)k].

The above result recalls the result of Bondy and Vince [3], that if G is
a graph with at most two vertices of degree at most two, then G contains
cycles of two consecutive lengths or two consecutive even lengths. This was

5

proved using a technique of Thomassen and Toft [12]. In comparison, note
that Theorem 5 requires average degree at least 6k where k ≥ 2. Therefore,
to ensure two cycles of consecutive lengths or consecutive even lengths, we
require average degree at least twelve, which is higher than what is required
in the context of Bondy and Vince’s results.

The following result is proved in the same was as Theorem 1:

Corollary 6 Let k ≥ 2 be a natural number, and suppose that G has chro-

matic number at least 2k + 2 and girth at least g. Then G contains cycles

of k(g − 2) consecutive lengths.

The idea is that some level of a breadth-ﬁrst search tree induces a graph
of chromatic number at least k + 1. Such a graph contains an odd cycle
of length at least k(g − 2) + 1 with a chord. We then apply the colouring
lemma to deduce that G contains cycles of k(g − 2) consecutive lengths.
In a sense, this generalizes a result of Gy´arf´as who showed that if G has
chromatic number at least 2k + 2, then G contains cycles of k distinct odd
lengths. These ideas may also be used to give a relatively short proof that
r(C2k+1, Kn) ≪ n1+1/(k+1). However, better results are easily obtain — for
example, it is possible to show that r(C2k+1, Kn) ≪ n1+1/(k+1)(log2 n)−1/k.

The cycles we have obtained are all very close together in the sense that
they share many vertices. H¨aggkvist and Scott [7] asked if it was possible,
under an appropriate bound on the size of the graph, to ﬁnd disjoint cycles
of k consecutive even lengths. This question also remains open, noting that
a bound of order at least k2 on the average degree would be required for
disjoint cycles of k consecutive even lengths. This is shown, for example, by
Kl,n−l where l < 2k + k(k − 1)/2 and n is suﬃciently large.

We remark that from Theorem 1 we may obtain a result on extremal
numbers for even cycles, that slightly improves the result obtained by Bondy
and Simonovits [2] (see Corollary 9). From their paper, it follows that a
graph of order n and size at least 90kn1+1/k contains a cycle of length 2k.

6

Two simple lemmas are required before proving our result. The ﬁrst lemma
is a special case of a lemma of Kostochka and Pyber [9].

Lemma 7 Let G be a graph of order n and size at least cn1+1/k, where

c ≥ 1. Then G contains a subgraph of average degree at least c and radius

at most k.

Proof. We may assume that G has minimum degree at least cn1/k. Let v0
be an arbitrary vertex in G and deﬁne Hi to be the subgraph of G induced by
vertices at distance at most i from v0. Deﬁne r = min{i : e(Hi) ≥ 1
2 c|Hi|}.
Clearly e(Hi) ≥ 1
2 cn1/k|Hi−1| for all i and so, by deﬁnition of r, |Hr−1| >
n1/k|Hr−2| which gives |Hr−1| > n(r−1)/k. Since |Hr−1| ≤ n, r − 1 < k and
so r ≤ k and Hr is the desired subgraph.

Lemma 8 Let G be a graph of order n with e(G) ≥ 2n1+1/k where k ≥ 2.

Then G has girth at most 2k + 1.

Proof. By Lemma 6, G has a subgraph H of radius at most k and average
degree at least two. So H contains a cycle and some cycle in H has length
at most 2k + 1.

In particular, if G is bipartite and k = 2 in Lemma 7, then G has a cycle
of length four. For comparison, a standard result states that a graph which
has at least n3/2/2 + n/4 edges contains a cycle of length four. We are able,
using Theorem 1, to show the existence of longer even cycles:

Theorem 9 Let G be a bipartite graph of order n and girth g, and of size

at least 4⌈2(k − 1)/(g − 2)⌉n1+1/k, where k ≥ 2 is an integer. Then G has

a cycle of length 2k.

Proof. By Lemma 7, either G contains a cycle of length 2k or g < 2k
and k ≥ 3. In the latter case, ⌈2(k − 1)/(g − 2)⌉ ≥ 2. Lemma 6 shows
that G contains a subgraph of average degree at least 4⌈2(k − 1)/(g − 2)⌉

7

and of radius at most k. By Theorem 1, there are cycles of at least k − 1
consecutive even lengths in H, the shortest length being at most 2k. So one
of these cycles must have length exactly 2k.

As a corollary to Theorem 8, we slightly improve the result of Bondy
and Simonovits [2]:

Corollary 10 Let G be a graph of order n and size at least 8(k − 1)n1+1/k,

where k ≥ 2. Then G contains a cycle of length 2k.

Acknowledgements

I would like to thank Andrew Thomason for his many helpful suggestions.

References

[1] Bollob´as, B., Cycles Modulo k, Bull. London Math. Soc. 9 (1977) 97–98.

[2] Bondy, J., Simonovits, M., Cycles of Even Length in Graphs, J. Com-
binatorial Theory B 16 (1974) 97–105.

[3] Bondy, J., Vince, A. Cycles in a graph whose lengths diﬀer by one or
two, J. Graph Theory 27 (1998) 11–15.

[4] Erd˝os, P., Some recent problems and results in graph theory, combi-
natorics, and number theory, Proc. Seventh S–E Conf. Combinatorics,
Graph Theory and Computing, Utilitas Math., Winnipeg, (1976) 3–14.

[5] Erd˝os, P., Some of my recent problems in Combinatorial Number The-
ory, Geometry and Combinatorics in: Graph Theory, Combinatorics
and Algorithms, Volume 1, Proc. Seventh Quadrennial International
Conference on the Theory and Applications of Graphs, Y. Alavi and A.
Schwenk eds., John Wiley and Sons (1995) 335–349.

[6] Gy´arf´as, A., Koml´os, J., Szemer´edi, E., On the distribution of cycle
lengths in graphs, J. Graph Theory 8 (1984) 441–466.

8

[7] H¨aggkvist, R., Scott, A., Arithmetic progressions of cycles, preprint.

[8] H¨aggkvist, R., Scott, A., Cycles of nearly equal length in cubic graphs,
preprint.

[9] Kostochka, A., Pyber, L., Small topological complete subgraphs of
dense graphs, Combinatorica 8(1) (1988) 83-86.

[10] Thomassen, C., Girth in Graphs, J. Combinatorial Theory B 35 (1983)
129–141.

[11] Thomassen, C., Paths, Circuits and Subdivisions in: Selected Topics
in Graph Theory 3, L. Beineke, R. Wilson eds., Academic Press (1988)
97–133.

[12] Thomassen, C., Toft, B., Non-separating induced cycles in graphs, J.
Combinatorial Theory B 31 (1981) 199–224.

9
