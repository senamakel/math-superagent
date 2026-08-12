<!-- source: http://ajc.maths.uq.edu.au/pdf/79/ajc_v79_p100.pdf | converted from PDF -->

AUSTRALASIAN JOURNAL OF COMBINATORICS
Volume 79(1) (2021), Pages 100–105

Classes of cubic graphs containing cycles
of integer-power lengths

P. J. Couch B. D. Daniel W. Paul Wright

Lamar University, Department of Mathematics
Beaumont, Texas 77710
U.S.A.
pjcouch@lamar.edu dale.daniel@lamar.edu research@weierstrass.org

Abstract

Erd˝os and Gy´arf´as conjectured in 1995 that every graph with minimum
degree three has a cycle of length 2k for some integer k> 1. Y. Caro
has asked the related question of whether every such graph has a cycle
whose length is a non-trivial power of some natural number. There have
been numerous related questions and conjectures, including questions by
various authors. We address a special case of the question of Caro, as
well as others, by showing that every graph G of minimum degree 3, such
that the set of centers of induced claws of G is independent, contains a
cycle of length a
k for some integers a ≥ 2and k ≥ 2.

1 Introduction

Erd˝os and Gy´arf´as conjectured ([5], [8]) that every graph with minimum degree three
has a cycle of length 2k for some integer k> 1.
Debose, Erd˝os, and Hobbs [4] narrowed the question by asking if each claw-free
graph with minimum degree two, maximum degree three, and at most two vertices
of degree 2 contains a cycle of length 2k for some non-negative integer k.In [3],
Shauger and the second-named author proved the result for planar claw-free graphs.
In [11], the result is proved for cubic claw-free graphs of genus at most six. More
recently, Verstraete has related results concerning unavoidable cycle lengths ([12],
[14]), Heckman and Krakovski [7] have shown that each 3-connected 3-regular planar
graph contains some 2j cycle for 2 ≤ j ≤ 7, and Bensmail [1] showed that there
exist arbitrarily large cubic graphs all of whose 2-power cycles have length 4 only, or
8only.
Herein, we study a related result. West [15] relates that Caro suggests the weaker
question of whether every such graph has a cycle whose length is a non-trivial power
of some natural number. We address a special case of the question of Caro, as well

ISSN: 2202-3518 c⃝The author(s). Released under the CC BY-ND 4.0 International License

P.J. COUCH ET AL. / AUSTRALAS. J. COMBIN. 79 (1) (2021), 100–105 101

as others, by showing that every graph G of minimum degree 3, and such that the
set of centers of induced claws of G is independent, contains a cycle of length a
k for
some integers a ≥ 2and k ≥ 2.

2 Preliminaries

We use the terminology of Bondy and Murty [2]. All graphs are ﬁnite, simple, and
undirected. In particular, for a graph G,we let ν(G) denote the number of vertices
of G. A graph in which each vertex has degree 3 is said to be cubic (or 3-regular).
A triangle is an isomorphic copy of K3. A vertex v of G is said to be contained in
atriangleof G if and only if there exists a triangle T that is a subgraph of G and
v ∈ V (T ).
An isomorphic copy of K1,3 is said to be a claw. For graphs G and H, G is said
to be H-free if G has no induced subgraph isomorphic to H. Our emphasis is on
claw-freeand almost claw-freecubicgraphs. The reader is referred to the excellent
survey [6] of such graphs by Faudree, Flandrin and Ryj´aˇcek.

3Main Results

An important result in our Theorem 1 below is the following of Paz (Theorem 7.3
of [9]).

Lemma 1. If m is a positive integer then for every positive integer n such that
n> 14.4
| m√1.5−1|m thereis atleast onepositiveinteger a such that n< a
m < 3
2n.

We begin with a speciﬁc case of the more general results that follow, because the
ideas and techniques used throughout are exempliﬁed in the simpler case.

Theorem 1. Suppose that G is a graph containing a cycle D such that:

1. D is not of length 10;
2. each vertex of D is of degree 3 in G;
3. each vertex of D is contained in precisely one triangle of G;and
4. if D meets a triangle T in G then D contains at most one edge of T .

Then G has a cycle of length a
k for some positive integers a ≥ 2 and k ≥ 2.

Proof. The reader may verify that in the result of Paz above, n must be chosen
greater than or equal to 286 in order that m be greater than or equal to 2. The
following table (Figure 1) notes that there is at least one power a
k for some positive
integers a ≥ 2and k ≥ 2 such that 2n ≤ a
k ≤ 3n for each n =2, 3, 4,... , 286 with
the exception of n =5.
By contracting each triangle T of the cycle D in G to an associated unique vertex
of degree 3 in the corresponding graph G′, D gives rise to a cycle D′ in G′.If D′ has

P.J. COUCH ET AL. / AUSTRALAS. J. COMBIN. 79 (1) (2021), 100–105 102

n a
k in [2n, 3n]
2 4
3 − 4 9
5 none
6 − 8 16
9 − 13 27
14 − 16 32
17 − 28 49
29 − 81 81
82 − 112 225
113 − 121 243
122 − 171 343
172 − 256 512
257 − 286 625

Figure 1: Integer-powers in [2n, 3n].

length less than or equal ito 286 then the neighborhood of cycle D in G contains a
cycle of each length 2n,... , 3n and therefore a cycle of length a
k for some positive
integers a ≥ 2and k ≥ 2. Since D does not have length 10, D′ does not have
length 5.
We may therefore assume that cycle D in G has length ν(D)≥ 3
2 · 286 = 429. We
may suppress one-third (or more) of the vertices of D to single vertices to note that
the subgraph of G induced by the neighborhood N(D)of D gives rise to every cycle
length L in G such that 286 ≤ 2
3ν(D) ≤ L ≤ ν(D). By the result of Paz above, there
are integers a ≥ 2and k ≥ 2 such that n< a
k < 3
2n. With n = 2
3 ν(D) ≥ 286, we
have 2
3 ν(D) ≤ a
k ≤ ν(D).

Each vertex v of a cubic claw-free graph G is contained in exactly one triangle
of G. Straightforward calculation ensures that such a graph G′ must contain cycle
lengths other than n = 10. The following corollary then follows immediately.

Corollary 1. Suppose that G is a claw-free graph with δ ≥ 3. Then G has a cycle
of length a
k for some positive integers a ≥ 2 and k ≥ 2.

Corollary 2. Suppose that G is a claw-free graph with minimum degree δ ≥ 2,
maximum degree Δ=3,and thecollection V2(G)= {v ∈ V (G): d(v)= 2} has two
or fewer elements. Then G has a cycle of length a
k for some positive integer a ≥ 2
and some integer k ≥ 2.

Proof. Suppose that V2(G) consists of a single vertex v with neighborhood N(v)=
{a, b}.
Assume that v is contained in no triangle and let G′ denote (G − v) ∪{e = ab}.
Then G′ has a cycle E′ of length a
k for some positive integers a ≥ 2and k ≥ 2by
Corollary 1. It then follows that G has a cycle E of length 1 + a
k for some positive

P.J. COUCH ET AL. / AUSTRALAS. J. COMBIN. 79 (1) (2021), 100–105 103

integer a ≥ 2 and some integer k ≥ 2. We may assume that E contains vertex v.
If E contains only one edge of each triangle that it meets then its length is 2t +1,
where t is the number of triangles meeting E.Then G contains cycles of all lengths
from 2t +1 to 3t + 1, inclusive. With 2t + 1 playing the role of n in Lemma 1, there
is a cycle of length a
k where n =2t +1 <a
m ≤ 3t +1 < 3
2 (2t +1). As above,
smaller cases of t may be calculated computationally. We may therefore assume that
E contains two edges of some triangle that it meets. The length 1 + a
k of E may
then be reduced by one.
If v is contained in triangle T then two copies of G are joined by an edge whose
end vertices are the copies of v. The resulting graph is cubic and claw-free and we
then apply Corollary 1.
We therefore assume that V2(G)= {u, v}. As a ﬁrst case, assume that u and
v are adjacent. We may assume that neither u nor v is contained in a triangle.
Assume the other vertex adjacent to u is w. By replacing the path wuv by a single
edge wv and applying the case above, we conclude that G has a cycle F of length
1+ a
k for some positive integer a ≥ 2 and some integer k ≥ 2and such that F
contains vertex u and v.If F contains only one edge of each triangle that it meets
then its length is 2t +2, where t is the number of triangles meeting E.Then G
contains cycles of all lengths from 2t +2 to 3t + 2, inclusive. As above, there is a
cycle of length b
j where n =2t +2 <b
j ≤ 3t +2 < 3
2(2t + 2), with the smaller cases
completed computationally. We may therefore assume that F contains two edges of
some triangle that it meets. The length 1 + a
k of F may then be reduced by one.
As a next case, we assume V2(G)= {u, v},that u and v are not adjacent, and
that u is contained in triangle Tu and v is contained in triangle Tv. The proof of this
is almost identical to the preceding case. As a ﬁnal case, we assume V2(G)= {u, v},
that u and v are not adjacent, and that u is contained in triangle Tu and v is contained
in no triangle. The proof of this case is as in the case above that V2(G) consists of
a single vertex and that vertex is contained in no triangle.

Corollary 3. Suppose that G is a graph containing a cycle D such that:

1. the minimum degree of vertices in D is 2 and there are at most two vertices of
degree 2;
2. each vertex of D which is of degree 3 is contained in precisely one triangle of G;
3. if D meets a triangle T in G then D contains at most one edge of T ;and
4. the length of D is not 5 if V2(D)= {u} and the length of D is not 10 if
V2(D)= {u, v}.

Then G has a cycle of length a
k for some positive integers a ≥ 2 and k ≥ 2.

Theorem 2. Suppose that a graph G has minimum degree 3 and that the set of
centers of induced claws of G is independent. Then G contains a cycle of length a
k

for some integers a ≥ 2 and k ≥ 2.

P.J. COUCH ET AL. / AUSTRALAS. J. COMBIN. 79 (1) (2021), 100–105 104

The proof of this is very similar and is left to the reader; the only nuance is
dealing with the potential for triangles that share vertices, which can be tedious and
repetitive.
Ryj´aˇcek [10] has deﬁned a graph G as almost claw-free if the set of centers of
induced claws is independent and for every vertex x, the domination number of
G[N(x)] is at most two. It is straightforward to see that every claw-free graph is
almost claw-free. Let G be an almost claw-free cubic graph. Suppose that D is a
cycle in G such that the length ν(D)of D is greater than or equal to 6 and if D
meets a triangle T in G then D contains at most one edge of T . The condition
that the centers of induced claws are independent guarantees that such a cycle meets
1
3 ⌈ν(D)⌉ or more triangles in G,where ⌈x⌉ is the usual ceiling function.

Theorem 3. Suppose that G is an almost claw-free graph with minimum degree 3.
Then G has a cycle of length a
k for some integers a ≥ 2 and k ≥ 2.

Proof. We may assume that G is non-planar by [7]. As a result (e.g., [13]), G contains
acycle E with three pair-wise crossing chords. It is straightforward that such a cycle
must have length greater than or equal to 20. We may therefore assume that the
circumference of G is greater than or equal to 20. Let D be a cycle in G of length
20 or more such that if D meets a triangle T in G then D contains at most one
edge of T . As in Theorem 1, we contract each of 1
3⌈ν(D)⌉ triangles of D in G to
an associated unique vertex of degree 3 in the corresponding graph G′, yielding a
cycle D′ in G′.If ν(D′) ≥ 286 then the proof proceeds exactly as in Theorem 1. It
therefore suﬃces to note that there is at least one power a
k for some positive integers
a ≥ 2and k ≥ 2 such that n ≤ a
k ≤ 4
3 n for the smaller possible values of n = ν(D).
A table may be easily constructed as in Theorem 1 demonstrating that such an a
k

exists for all 20 ≤ n ≤ 286.

4 Remaining Questions

We close with some questions related to the results of this work. Some of these we
have not studied, but they are clearly related and are of interest; some are new, while
others are quite old.

1. If a graph G has minimum degree at least three, then does G contain a cycle
whose length is a power of two? [5]
2. If a graph G is claw-free and is of minimum degree three, then does G contain
a cycle whose length is a power of two? [3]
3. If a graph G has minimum degree three, then does G contain a cycle whose
length is a power (of two or more) of some integer greater than or equal to 2? [15]
4. As a special case of the previous questions, what if G is assumed to be Hamil-
tonian?
 P.J. COUCH ET AL. / AUSTRALAS. J. COMBIN. 79 (1) (2021), 100–105 105

References

[1] J. Bensmail, On q-power cycles in cubic graphs, Discuss. Math. Graph Theory 37 (1)
(2017), 211–220.

[2] J. A. Bondy and U. S. R. Murty, Graph Theory with Applications, American Elsevier,
New York, 1976.

[3] D. Daniel and S. Shauger, A result on the Erd˝os-Gy·arf·as conjecture in planar graphs,
Proc. Thirty-second Southeastern Int. Conf. on Combinatorics, Graph Theory and
Computing (Baton Rouge, LA, 2001), Congr. Numer. 153 (2001), 129–139.

[4] Y. Debose, P. Erd˝os and A. Hobbs, Graphs having no short even cycles, Proc. Twenty-
seventh Southeastern Int. Conf. on Combinatorics, Graph Theory and Computing (Ba-
ton Rouge, LA, 1996), Congr. Numer. 121 (1996), 243–253.

[5] P. Erd˝os, Some old and new problems in various branches of combinatorics, Discrete
Math. 165/166 (1997), 227–231.

[6] R. Faudree, E. Flandrin and Z. Ryj·aˇcek, Claw-free graphs—A survey, Discrete Math.
164 (1997), 87–147.

[7] C. Heckman and R. Krakovski, Erd˝os–Gy·arf·as conjecture for cubic planar graphs,
Electron.J.Combin. 20 (2) (2013), #P7.

[8] P. S. Nowbandegani, H. Esfandiari, M. H. S. Haghighi and K. Bibak, On the Erd˝os–
Gy·arf·as Conjecture in claw-free graphs, Discuss. Math. Graph Theory 34 (3) (2014),
635–640.

[9] G. A. Paz, On the interval [n, 2n]: primes, composites and perfect powers, Gen. Math.
Notes 15 (1) (2013), 1–15.

[10] Z. Ryj·aˇcek, Almost claw-free graphs, J. Graph Theory 18 (5) (1994), 469–477.

[11] S. Shauger, Claw-free, cubic graphs of low genus have a cycle whose length is a power
of two, Congr. Numer. 159 (2002), 119–126.

[12] B. Sudakov and J. Verstraete, Cycle lengths in sparse graphs, Combinatorica 28 (3)
(2008), 357–372.

[13] C. Thomassen, A reﬁnement of Kuratowski’s theorem, J. Combin. Theory Ser. B
37 (3) (1984), 245–253.

[14] J. Verstraete, Unavoidable cycle lengths in graphs, J. Graph Theory 49 (2) (2005),
151–167.

[15] D. West, Open Problems Page,
http://www.math.uiuc.edu/ west/openp/2powcyc.html.

(Received 1 Jan 2020; revised 4 Nov 2020)
