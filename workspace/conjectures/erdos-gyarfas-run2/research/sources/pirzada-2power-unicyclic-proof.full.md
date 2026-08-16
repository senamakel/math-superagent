<!-- source: https://ejgta.org/index.php/ejgta/article/download/1312/pdf_224 | converted from PDF -->

www.ejgta.org

Electronic Journal of Graph Theory and Applications 10 (1) (2022), 337–344

On 2-power unicyclic cubic graphs

S. Pirzada
∗a, Mushtaq A. Shah
b, Edy Tri Baskoro
c

aDepartment of Mathematics, University of Kashmir, Srinagar, Kashmir, India
bDepartment of Mathematics, AAAM Degree College, Bemina, Srinagar, India
cCombinatorial Mathematics Research Group, Faculty of Mathematics and Natural Sciences, Institut Teknologi Bandung, Indonesia

pirzadasd@kashmiruniversity.ac.in, shahmushtaq81@gmail.com, ebaskoro@itb.ac.id

∗Corresponding author

Abstract

In a graph, a cycle whose length is a power of two (that is, 2
k) is called a 2-power cycle. In this
paper, we show that the existence of an infinite family of cubic graphs which contain only one
cycle whose length is a power of 2. Such graphs are called as 2-power unicyclic cubic graphs.
Further we observe that the only 2-power cycle in a cubic graph cannot be removed implying that
there does not exist a counter example for Erd˝os-Gy´arf´as conjecture.

Keywords: cycle, cubic graph, Erd˝os-Gy´arf´as conjecture, distance
Mathematics Subject Classification: 05C38
DOI: 10.5614/ejgta.2022.10.1.24

1. Introduction

In a graph G, a 2-power cycle is a cycle whose length is a power of 2. A graph which contains
a unique 2-power cycle is called a 2-power unicyclic graph. In 1995, Erd˝os and Gy´arf´as [4] put
forward a conjecture which states that every graph with minimum degree 3 contains a simple cycle
whose length is a power of two. If the conjecture is false, a counter example would take the form of
a graph with minimum degree three having no cycles whose length is a power of two. It is known
through computer searches of Gordon Royle and Klas Markstrom that any counterexample must
have at least 17 vertices, and any cubic counter example must have at least 30 vertices. Markstrom’s
searches found four graphs on 24 vertices in which the only power-of-two cycles have 16 vertices,
one of these four graphs is planar. However, the Erd˝os-Gy´arf´as conjecture is now known to be true

Received: 4 March 2021, Revised: 10 April 2022, Accepted: 16 April 2022.

337 www.ejgta.org

On 2-power unicyclic cubic graphs | S. Pirzada et al.

for the special case of 3-connected cubic planar graphs, see Heckman and Krakovski [6]. Weaker
results relating the degree of a graph to unavoidable sets of cycle lengths are known. Verstraete
[12] showed that there is a set S of lengths, with |S| = O(n0.99), such that every graph with average
degree ten or more contains a cycle with its length in S. Sudakov and Verstraete [11] proved that
every graph whose average degree is exponential in the iterated logarithm of n necessarily contains
a cycle whose length is a power of two. Daniel and Shauger [2] proved the conjecture to be true for
planar claw-free graphs and Shauger [10] showed the conjecture to be true for graphs that avoid
large induced stars and satisfy additional constraints on their degrees. In 2004, Klas Markstrom
[8] provided extremal graphs for some problems on cycles in graphs.
A graph is planar if it can be embedded in the plane without crossing edges. A plane graph is an
embedded planar graph. A graph G is 3-connected if it becomes disconnected by removing at least
3 vertices. A graph G is cubic if every vertex of G is of degree three. More on graphs and cycles
can be seen in [3, 7, 9].By computer searches, Markstrom [6] verified Erd˝os-Gy´arf´as conjecture
for cubic graphs of order at most 29, and found that the smallest cubic planar graph with no 4-
or 8-cycles has 24 vertices (see Figure 1). Note that this graph contains a 16-cycle. Shauger [8]
proved the conjecture for K1,m free graphs of minimum degree at least m + 1 or maximum degree
at least 2m − 1. Every 3-connected cubic planar graph contains a 2
m− cycle, for some 2 ≤ m ≤ 7,
see [6].
 Figure 1. cubic graph with 24 vertices with no 4- or 8-cycle.

Markstrom’s 24-vertex cubic planar graph with no 4 or 8 cycles, found in a computer search
for counter example to the Erd˝os-Gy´arf´as conjecture, has cycles with 16 vertices. A recent study
by Bensmail [1] showed that their exist arbitrarily large cubic graphs with no q-power cycle. Frank
[5] showed that every k-regular k-connected graph on n vertices has k-diameter at most n
2 and
this upper bound cannot be improved when n = 4k − 6 + I(2k − 4). In particular, the maximal
3-diameter of 3-regular graphs with 2n vertices is equal to n, that is, the maximal 3-diameter of
3-regular graphs with n vertices is equal to n
2 .
In a graph, the distance between the two vertices is the number of edges in a shortest path (also
called a graph geodesic) connecting them. This is also known as the geodesic distance. Notice
that there may be more than one shortest path between two vertices. If there is no path connecting
the two vertices, that is, if they belong to different connected components, then conventionally the
distance is defined as infinite.
 338 www.ejgta.org

On 2-power unicyclic cubic graphs | S. Pirzada et al.

2. On two power unicyclic cubic graphs

In a graph G, if the distance between the vertices u and v is d(u, v) = r, the number of vertices
between u and v is r + 1. If G is a cubic graph of order n and e is any edge of G, then G − e is the
graph in which n − 2 vertices are of degree 3 and 2 vertices are of degree 2, such a graph is called
an (n − 2)-cubic graph.
 Figure 2. Cubic graph with eight vertices.

Figure 3. 6-cubic graph, that is, graph with eight vertices with six vertices of degree 3 and two vertices of degree 2.

The graph G, shown in Figure 2, has eight vertices and contains cycles of length 4, 5, 6, 7 and
8. Now remove the edge e = uv from G, we get the graph K = G − e, as shown in Figure 3.
Clearly K is (n − 2)−cubic and has no cycles of lengths 2
2, 2
3. Further the distance between the
vertices u and v in K is dK(u, v) = 3 < 4.
We will show that the above example leads to the existence of a family of 2-power unicyclic
cubic graphs, that is, a family of cubic graphs which contain only the cycle of length 2
k (2
k < n)
but does not contain any cycle of length 2
t, t ̸= k. We show the existence of this graph G by
construction, the graph G constructed will have even number of vertices, say n = 2s, and further
in G there is always a bridge which partitions V (G) into two parts with each part having s vertices.
So if G contains a cycle of length 2
k, then 2
k < s, since the presence of bridge does not allow the
cycle to have edges from both the parts, that is, contains edges from one of the two parts.

339 www.ejgta.org

On 2-power unicyclic cubic graphs | S. Pirzada et al.

Theorem 2.1. There exists a family of 2-power unicyclic cubic graphs, that is a family of cubic
graphs with order say n = 2s, which contain a cycle of length 2
k (2
k < s) but does not contain
any cycle of length 2
t, t ̸= k.

Proof. We show the existence of such a family by construction. We start with the construction of
the smallest such graph.
Consider the graph G of order 8 as shown in Figure 2. We remove the edge e = uv to get the
graph K = G − e as shown in Figure 3. We note that dK(u) = 2 and dK(v) = 2 so that K is
(6)-cubic. Further dH(u, v) = 3 < 4. Take 5 copies of K and name them as H1, H2, J1, J2 and H.
Also we represent the vertices of degree 2 by u1, v1 ∈ H1; u2, v2 ∈ H2; x1, y1 ∈ J1; x2, y2 ∈ J2
and u, v ∈ H. Further, let P1 = H1 ∪ H2 and Q1 = J1 ∪ J2.
Now, let X1 be the graph consisting of P1, Q1, H, K3 (vertices labeled as w1, w2, w3) and
K1,3 + x (vertices labeled as z1, z2, z3, z4 with z1 as the pendant vertex) together with the edges
v1u2, y1x2, v2w1, y2w2, w3v, uz1, u1z3, x1z4. Clearly degree of each vertex of X1 is three except
the vertex z1 whose degree is two.
We now take two copies of X1, one named as X1 and another as X ′
1. Label the vertices of X ′
1
as u′
1, v′
1 and so on. Consider the graph G1 = X1 ∪ X ′
1 ∪ {z1z′
1}. Clearly the graph G1 is cubic.

v1 u2 v 2

H 1 H 2

x
1 y
1 x2 y
2
 w 1

w2
 w 3
 z 1
 z 2

z 3

u v

J1 J 2

Figure 4. Cubic graph G1 with 94 vertices, having no cycles of length 4, 8, 16 but has a cycle of length 32.

We observe that the edge z1z′
1 is a bridge in G1 (joining X1 and X ′
1). Also the number of
vertices in each of X1 and X ′
1 is 47. So the maximum length of the cycle in G1 has to be less
or equal to 47 and thus G1 can have only 2
2, 2
3, 2
4, 2
5 cycles of the form 2
k. But as we see that
G1 does not contain the cycles of the lengths 2
2, 2
3, 2
4. Evidently G1 contains the cycle of length
2
5. Note that G1 cannot have a cycle of length 2
6 = 64, because of the presence of bridge z1z′
1

340 www.ejgta.org

On 2-power unicyclic cubic graphs | S. Pirzada et al.

between X1 and X ′
1. Hence we have constructed a cubic graph G1 of order 84 in which there are
no cycles of lengths 2
2, 2
3, 2
4 but it contains a cycle of length of 2
5. See Figure 4.
The above construction can be extended to obtain a family of cubic graphs in the following
way. Let Pi contain ∑i
j=1 2
j copies of K and name these copies as H1, H2, H3 . . . . Let Pi =
H1 ∪ H2 ∪ H3 ∪ . . . . Similarly let Qi contain ∑i
j=1 2
j copies of K and name these copies as
J1, J2, J3 . . . . Let Qi = J1 ∪ J2 ∪ J3 ∪ . . . . Label the vertices of degree 2 in H1, H2, H3 . . . ,
J1, J2, J3 . . . respectively by u1, v1 ∈ H1 ; u2, v2 ∈ H2 ; u3, v3 ∈ H3 ; . . . ; x1, y1 ∈ J1 ;
x2, y2 ∈ J2 ; x3, y3 ∈ J3 . . . .
Let Xi be the graph containing Pi, Qi, H (a copy of K), K3 (vertices labeled as w1, w2, w3)
and K1,3 + x (vertices labeled as z1, z2, z3, z4 with z1 as the pendant vertex) together with the edges
v1u2, v2u3, . . . ; y1x2, y2x3, . . . ; w3v, uz1, u1z3, x1z4 ; the edge between the vertex w1 and the
second vertex of the last copy K ∈ Pi ; the edge between w2 and the second vertex of the last copy
K ∈ Qi. Clearly degree of each vertex of Xi is three except the vertex z1 whose degree is two.
Now, take two copies of Xi, represented as Xi and X ′
i.
Consider the graph Gi = Xi ∪ X ′
i ∪ {z1z′
1}, which is cubic. We observe that the edge z1z′
1
is a bridge in Gi (joining Xi and X ′
i). Also the number of vertices in each of Xi and X ′
i is
|Xi| = |Pi| + |Qi| + |H| + |K3| + |K1,3 + x| = 2|Pi| + 8 + 3 + 4 = 2(8 ∑i
j=1 2
j) + 15,
since each copy of K contains eight vertices. Thus the length of the largest cycle has to be less
or equal to 2(8 ∑i
j=1 2
i) + 15 = 24(2 + 22 + 23 + · · · + 2i−1 + 2i) + 15. Further, we note that
|Xi| = |Xi−1| + 2i+1. If |Gi| is the order of Gi, it can be easily seen that |Gi| = |Gi−1| + 25.
Evidently, Gi does not contain the cycles of lengths 2
2, 2
3, 2
4, . . . , 2
i+3 but contains the cycle
of length 2
i+4. Also Gi does not contain the cycles of length 2
t, t ≥ i + 5, since the length of the
largest cycle is less or equal to 2
4(2 + 22 + 23 + · · · + 2i−1 + 2i) + 15. Hence Gi contains only one
cycle whose length is a power of 2.

For instance, G2 is a cubic graph of order 222 having no cycles of lengths 2
2, 2
3, 2
4, 2
5 but it
contains a cycle of length 2
6, see Figure 5. This is because the graph has a bridge and each part has
111 vertices. The minimum length of the cycle is 33 and total vertices in each part is 111. Thus,
the only cycle whose length is of the form 2
k with 33 ≤ 2
k ≤ 111 is 64.
Similarly, G3 is a cubic graph of order 478 having no cycles of lengths 2
2, 2
3, 2
4, 2
5, 2
6 but
it contains a cycle of length 2
7. This is illustrated in Figure 6. This graph has a bridge, so each
part has 239 vertices and minimum length of a cycle is 65 and total vertices in each part is 239.
Therefore, the only cycle of the form 2
k with 65 ≤ 2
k ≤ 239 is 128.
From the above discussion and examples, we get a recurrence relation of these cubic graphs as
follows.
Let us assume that there exists a cubic graph G which contains a cycle of length 2
k only but
does not contain cycles of length 2
t, t ̸= k. In particular, G will have no cycles of length 2
t,
2 ≤ t ≤ k − 1. Thus the number of vertices in this graph is at least 2
k, that is, n ≥ 2
k, where n is
the total number of vertices in the graph. Since it has no cycle of length 2
k−1, this implies that an
edge was removed in the graph between vertices u and v (say) which has removed all the cycles of
length 2
t, 2 ≤ t ≤ k − 1. Thus d(u, v) = 2
k−1 − 1. As 2
k−1 < 2
k, implies that 2(2
k−1) = 2
k, or
2(2
k−1 − 1) < 2
k, or 2
k−1 − 1 < 2k
2 or 2
k−1 − 1 < n
2 , where n ≥ 2
k. Thus, d(u, v) < n
2 , which
negates the above observation that each cubic graph with degree greater or equal to 3 has one cycle

341 www.ejgta.org

On 2-power unicyclic cubic graphs | S. Pirzada et al.

Figure 5. Cubic graph G2 with 222 vertices, having no cycles of length 4,8,16,32 but has a cycle of length 64.

Table 1. Recurrence relation for the cubic graphs
Graph Cycles of the form 2
t removed Cycle of the form 2
k present.
G1 with |G1| = 94 2
2, 2
3, 2
4 2
4+1 = 2
5

G2 with |G2| = |G1| + 26 2
2, 2
3, 2
4, 2
5 2
4+2 = 2
6

G3 with |G3| = |G2| + 27 2
2, 2
3, 2
4, 2
5, 2
6 2
4+3 = 2
7

G4 with |G4| = |G3| + 28 2
2, 2
3, 2
4, 2
5, 2
6, 2
7 2
4+4 = 2
8

G5 with |G5| = |G4| + 29 2
2, 2
3, 2
4, 2
5, 2
6, 2
7, 2
8 2
4+5 = 2
9

G6 with |G6| = |G5| + 210 2
2, 2
3, 2
4, 2
5, 2
6, 2
7, 2
8, 2
9 2
4+5 = 2
10

Gi with |Gi| = |Gi−1| + 2i+4 2
2, 2
3, 2
4, 2
5, · · · , 2
i+2, 2
i+3 2
i+4

of length 2
k. Accordingly, there is no cubic graph in which we can develop a counter case with
no cycle of power 2
k. This way we conclude that every graph with minimum degree 3 contains a
cycle whose length is a power of two.
 342 www.ejgta.org

On 2-power unicyclic cubic graphs | S. Pirzada et al.

Figure 6. Cubic graph G3 with 478 vertices, having no cycles of length 4, 8, 16, 32, 64 but has a cycle of length 128.

3. Conclusion

The Erd˝os-Gy´arf´as conjecture is one of the important problems in graph theory. The problem
has been partially proved to be true. Daniel and Shauger proved the conjecture to be true for planar
claw-free graphs and Shauger showed the conjecture to be true for graphs that avoid large induced
stars and satisfy additional constraints on their degrees.
The main aim of this paper is to show that counter example for the conjecture is not possible.
For this, we first prove the existence of an infinite family of cubic graphs which contain only one
cycle whose length is a power of 2. We show the existence of a family of cubic graphs in which all
the cycles of the form 2
t, where 2 ≤ t ≤ k − 1, can be removed and does contain only a cycle of
order 2
k, 2
k < n. Such graphs are called as 2-power unicyclic cubic graphs. Further, we observe
that the only 2-power cycle in a cubic graph cannot be removed implying that there does not exist
a counter example for Erd˝os-Gy´arf´as conjecture.

343 www.ejgta.org

On 2-power unicyclic cubic graphs | S. Pirzada et al.

Acknowledgement

The authors are grateful to the anonymous referee for his useful comments. The research of S.
Pirzada is supported by SERB-DST under the research project number CRG/ 2020/000109.

References

[1] J. Bensmail, On q-power cycles in cubic graphs. Discussions Mathematics Graph Theory 37
(2017), 211–220.

[2] D. Dale and S.E. Shauger, A result on the Erd˝os-Gy´arf´as conjecture in planar graphs, Proc.
32nd Southeastern Int. Conf. Combinatorics, Graph Theory and Computing, 56 (2001), 129–
13.

[3] C. Dalfo, M.A. Fiol, and M. Mitjana, On middle cube graphs, Electron. J. Graph Theory
Appl. 3 (2) (2015), 133–145.

[4] P. Erd˝os, Some old and new problems in various branches of combinatorics, Discrete Math.
165 (1997), 227–231.

[5] D. Frank, On the k-diameter of k-regular k-connected graphs, Discrete Math. 133 (1994),
291–296.

[6] C. Heckman and R. Krakovski, Erd˝os-Gy´arf´as conjecture for cubic planar graphs, Electronic
J. Comb. 2 (2013) p7.

[7] B. Li, L. Xiong, and J. Yin, Least degree vertices in longest cycles of graphs II, Electron. J.
Graph Theory Appl. 7 (2) (2020) 277–299.

[8] K. Markstrum, Extremal graphs for some problems on cycles in Graphs, Congr. Numerantium
171 (2004) 179–192.

[9] S. Pirzada, An Introduction to Graph Theory, Universities Press, Orient BlackSwan, Hyder-
abad (2012).

[10] S.E. Shauger, Results on the Erd˝os-Gy´arf´as conjecture in K1,m-free graphs, Proc. 29th South-
eastern Int. Conf. Combinatorics, Graph Theory and Computing, (1998) 61-65.

[11] B. Sudakov and J. Verstraete, Cycle lengths in sparse graph, Combinatorica 28 (3) (2008)
357- 372.

[12] J. Verstraete, Unavoidable cycle lengths in graphs, J. Graph Theory 49 (2) (2005) 151-167.

344
