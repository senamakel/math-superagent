<!-- source: https://arxiv.org/pdf/2012.09391 | converted from PDF -->

Improving the Delsarte bound

Gary R.W. Greavesa, Jack H. Koolen
b,c and Jongyook Parkd

aSchool of Physical and Mathematical Sciences,

Nanyang Technological University, 21 Nanyang Link, Singapore 637371, Singapore

bSchool of Mathematical Sciences,

University of Science and Technology of China, 96 Jinzhai Road, Hefei, Anhui, 230026, PR China

cCAS Wu Wen-Tsun Key Laboratory of Mathematics,

University of Science and Technology of China, 96 Jinzhai, Road, Hefei, Anhui, 230026, PR China

dDepartment of Mathematics, Kyungpook National University, Daegu, 41566, Republic of Korea

e-mail: gary@ntu.edu.sg, koolen@ustc.edu.cn, jongyook@knu.ac.kr

December 18, 2020

Abstract

In this paper, we study the order of a maximal clique in an amply regular graph with a ﬁxed
smallest eigenvalue by considering a vertex that is adjacent to some (but not all) vertices of the
maximal clique. As a consequence, we show that if a strongly regular graph contains a Delsarte
clique, then the parameter µ is either small or large. Furthermore, we obtain a cubic polynomial
that assures that a maximal clique in an amply regular graph is either small or large (under certain
assumptions). Combining this cubic polynomial with the claw-bound, we rule out an inﬁnite family
of feasible parameters (v, k, λ, µ) for strongly regular graphs. Lastly, we provide tables of parameters
(v, k, λ, µ) for nonexistent strongly regular graphs with smallest eigenvalue −4, −5, −6 or −7.

Key Words: Strongly regular graphs, Cliques, Smallest eigenvalues, Hoﬀman bound,
Delsarte bound, Claw-bound, Feasible parameters
2020 Mathematics Subject Classiﬁcation: 05E30

1 Introduction

The following bounds are well-known for the order of a clique in a graph, regular graph, and strongly
regular graph, respectively.

(i) For a graph Γ with v vertices, Cvetkovi´c proved that the order of a coclique in Γ is at most
min{v − n+, v − n−} [2, Theorem 3.5.1], where n+ and n− are the numbers of positive and negative
eigenvalues of Γ, respectively. We call this bound the Cvetkovi´c bound.

(ii) For a regular graph with valency k and smallest eigenvalue −m, Hoﬀman proved that the order of
a coclique in Γ is at most v m
k+m [2, Theorem 3.5.2]. We call this bound the Hoﬀman bound.

(iii) For a strongly regular graph with valency k and smallest eigenvalue −m, Delsarte proved that the
order of a clique in Γ is at most 1 + k
m [4, Section 3.3.2]. We call this bound the Delsarte bound
and a clique in Γ is called a Delsarte clique if its order is equal to 1 + k
m .

From the Hoﬀman bound and Cvetkovi´c bound, we can obtain an upper bound on the order of a clique
in a graph Γ by considering the complement of Γ. We note that if the graph Γ is a strongly regular graph,
then the bound obtained from the Hoﬀman bound is the same as the Delsarte bound [1, Proposition
1.3.2].
Our purpose is to study the order of a maximal clique in an amply regular graph with a ﬁxed smallest
eigenvalue by considering a vertex that is adjacent to some (but not all) vertices of the maximal clique. As

1arXiv:2012.09391v1  [math.CO]  17 Dec 2020
a consequence, we show that if a strongly regular graph contains a Delsarte clique, then the parameter µ
is either small or large. Our main tool, which we exhibit in Section 3 is a cubic polynomial corresponding
to an amply regular graph Γ that can be used to bound that size of a maximal clique in Γ. In Section 4, we
combine this cubic polynomial with the claw-bound to rule out an inﬁnite family of feasible parameters
(v, k, λ, µ) for strongly regular graphs. In the appendix, we provide tables of parameters (v, k, λ, µ) for
nonexistent strongly regular graphs with smallest eigenvalue −4, −5, −6 or −7.

2 Deﬁnitions and preliminaries

All the graphs considered in this paper are ﬁnite, undirected and simple. For basic deﬁnitions and
terminology, the reader is referred to [1]. Let Γ be a connected graph with vertex set V (Γ). The distance
d(x, y) between two vertices x, y ∈ V (Γ) is the length of a shortest path between x and y in Γ. The
maximum distance occuring in Γ is called the diameter of Γ. For each x ∈ V (Γ), denote by Γ(x) the set
of vertices in Γ that are adjacent to x. For a vertex x of Γ, the number |Γ(x)| is called the valency of x
in Γ. In particular, if k = |Γ(x)| holds for all x ∈ V (Γ), then Γ is regular with valency k .
A regular graph with v vertices and valency k is called edge-regular with parameters (v, k, λ) if any two
adjacent vertices have exactly λ common neighbors. An edge-regular graph with parameters (v, k, λ) is
called amply regular with parameters (v, k, λ, µ) if any two vertices at distance 2 have exactly µ common
neighbors. An amply regular graph with parameters (v, k, λ, µ) with diameter at most 2 is also called
strongly regular with parameters (v, k, λ, µ).

Theorem 2.1. (Cf. [3, Theorem 8.6.3]) Let m ⩾ 2 be an integer. Let Γ be a strongly regular graph with
parameters (v, k, λ, µ) and eigenvalues k > σ > τ . If τ = −m and σ > 1
2 m(m − 1)(µ + 1) − 1, then one
of the following holds:

(i) µ = m(m − 1) and Γ is a Latin square graph LSm(n),

(ii) µ = m
2 and Γ is a block graph of Steiner system 2-(mn + m − n, m, 1),

where σ = n − m.

We use the above theorem as follows. Let m ⩾ 2 be an integer and let Γ be a strongly regular graph
with parameters (v, k, λ, µ) and smallest eigenvalue −m. Assume that µ ̸= m(m−1) and µ ̸= m2, then by
Theorem 2.1, we have σ ⩽ 1
2 m(m−1)(µ+1)−1. Since λ−µ = σ−m and k−µ = σm ( [6, p. 219]), we have
λ = σ+µ−m ⩽ 1
2 (m
2−m+2)(µ−1)+m
2−2m and k = σm+µ ⩽ 1
2 m
2(m−1)(µ+1)−m+µ. Furthermore,
one can see that v = 1+k +k(k −λ−1)/µ. Neumaier [10, Theorem 3.1] showed that µ ⩽ m
3(2m−3) - we
refer to this bound as the µ-bound. The µ-bound shows that there are ﬁnitely many such strongly regular
graphs (for ﬁxed m). For a pair (λ, µ) satisfying λ = σ + µ − m ⩽ 1
2 (m
2 − m + 2)(µ − 1) + m
2 − 2m and
µ ⩽ m3(2m−3), if the multiplicities of the eigenvalues of Γ are integral and both the Krein condition [10,
Lemma 2.1] and the absolute bound [10, Lemma 2.2] are satisﬁed, then we call the parameters (v, k, λ, µ)
feasible for a strongly regular graph.
Let Γ be a connected graph. A clique in Γ is a set of pairwise adjacent vertices of Γ, and a coclique
in Γ is a set of pairwise non-adjacent vertices of Γ. The number of vertices in a clique or coclique is
called the order of the clique or coclique. A clique C in Γ is called maximal if there is no clique in Γ that
contains C and at least one other vertex of V (Γ)\C. A complete graph Kn is a graph whose vertex set
is a clique of order n. For a vertex x of Γ, if Γ(x) contains a coclique ¯C of order s, then the subgraph
induced on ¯C ∪ {x} is called the s-claw. The adjacency matrix A = A(Γ) of Γ is the matrix whose rows
and columns are indexed by vertices of Γ and the (x, y)-entry is 1 whenever x and y are adjacent and 0
otherwise. The eigenvalues of Γ are the eigenvalues of A.
The following well-known result is called the Interlacing Theorem, and it shows that for a graph Γ,
the eigenvalues of an induced subgraph of Γ interlace the eigenvalues of Γ.

Theorem 2.2. (Cf. [7]) Let m ⩽ n be two positive integers. Let A be an n × n matrix, that is similar
to a (real) symmetric matrix, and let B be a principal m × m submatrix of A. Then,

θn−m+i(A) ⩽ θi(B) ⩽ θi(A)

holds for i = 1, . . . , m, where A has eigenvalues θ1(A) ⩾ θ2(A) ⩾ . . . ⩾ θn(A) and B has eigenvalues
θ1(B) ⩾ θ2(B) ⩾ . . . ⩾ θm(B).
 2

Remark 1. A partition Π = {P1, P2, . . . , Pm} of the vertex set of a graph Γ is called equitable if there
exist non-negative integers qij (1 ⩽ i, j ⩽ m) such that each vertex in Pi has exactly qij neighbors in Pj.
Moreover, an eigenvalue of the quotient matrix Q = (qij) of the equitable partition Π = {P1, P2, . . . , Pm}
is also an eigenvalue of the graph Γ [2, Lemma 2.3.1]. Together with Theorem 2.2, this shows that
eigenvalues of the quotient matrix of an equitable partition of the vertex set of an induced subgraph of
the graph Γ interlace those of Γ.

3 Maximal-clique polynomial

In this section, we introduce a cubic polynomial (see Remark 2) that gives a new bound on the order of
a maximal clique in an amply regular graph. Indeed, this cubic polynomial says that a maximal clique
in an amply regular graph is either large or small (under certain assumptions).
For positive integers a and t, let us consider the graph with a + t + 1 vertices consisting of a complete
graph Ka+t together with a vertex x that is adjacent to precisely a vertices of Ka+t. We denote this graph
by H(a, t). Note that the vertex partition of Γ = H(a, t) with parts {x}, Γ(x) and their complement is
equitable with quotient matrix
 Q =
 


0 a 0
1 a − 1 t
0 a t − 1


 .

For a graph with smallest eigenvalue −m containing H(a, t) as an induced subgraph, the following
lemma gives a relationship between a, t and m.

Lemma 3.1. Let Γ be a graph with smallest eigenvalue −m that contains H(a, t) as an induced subgraph.
Then (a − m(m − 1))(t − (m − 1)
2) ⩽ (m(m − 1))2. (3.1)

Proof. Note that Remark 1 says that the smallest eigenvalue of Q is at least −m. Thus det(mI + Q) ⩾ 0,
from which (3.1) follows directly.

In the following lemma, we show that the parameter a in Lemma 3.1 is small when any two non-
adjacent vertices of Γ have few common neighbors.

Lemma 3.2. Let Γ be a graph with smallest eigenvalue −m such that any two non-adjacent vertices
have at most µ common neighbors. Suppose that Γ has a maximal clique C of order c ⩾ (m − 1)(4m − 1)
and a vertex y ̸∈ C with a neighbors in C. If µ < c+m−1+
√D
2 then a ⩽ c+m−1−
√D
2 , where D =
(c + m − 1)(c − (m − 1)(4m − 1)).

Proof. Note that Γ contains H(a, c − a) as an induced subgraph. Then (3.1) becomes

a
2 − a(c + m − 1) + m(m − 1)(c + m − 1) ⩾ 0

Since c ⩾ (m − 1)(4m − 1), we know that (c + m − 1)(c − (m − 1)(4m − 1)) ⩾ 0. Hence either

a ⩽ c + m − 1 − √
(c + m − 1)(c − (m − 1)(4m − 1))
2

or
 a ⩾ c + m − 1 + √(c + m − 1)(c − (m − 1)(4m − 1))
2
holds. But, since C is maximal, we must have a ⩽ µ.

We apply the proof of Lemma 3.2 to strongly regular graphs having a Delsarte clique to obtain the
following result.

Proposition 3.3. Let Γ be a strongly regular graph with parameters (v, k, λ, µ) having smallest eigenvalue
−m. Assume that k ⩾ m2(4m − 5) and that Γ contains a Delsarte clique. Then either

µ ⩽ k+m
2−
√(k+m2)(k−4m3+5m2)
2 or µ ⩾ k+m2+
√(k+m2)(k−4m3+5m2)
2 .

3

Proof. Let C be a Delsarte clique in Γ. Then C has order c = 1 + k
m . By [1, Proposition 1.3.2], every
vertex outside C has µ
m neighbors in C. Since k ⩾ m
2(4m − 5) = m(m − 1)(4m − 1) − m, we know that
c = 1 + k
m ⩾ (m − 1)(4m − 1). Then from the proof of Lemma 3.2, we know that either

µ
m ⩽ c+m−1−
√(c+m−1)(c−(m−1)(4m−1))
2 or µ
m ⩾ c+m−1+
√(c+m−1)(c−(m−1)(4m−1))
2 .

Replace c by 1 + k
m to obtain that either

µ ⩽ k+m2−√(k+m2)(k−4m3+5m2)
2 or µ ⩾ k+m2+
√(k+m2)(k−4m3+5m2)
2 .

This ﬁnishes the proof.

Next we provide a technical lemma for adjacency for cliques in edge-regular graphs.

Lemma 3.4. Let Γ be an edge-regular graph with parameters (v, k, λ) having a clique C of order c. For
a vertex x in C, if every vertex in Γ(x)\C has at most n neighbors in C\{x}, then

(c − 1)(λ − (c − 2))
(k − (c − 1)) ⩽ n.

Proof. Note that every vertex in Γ(x) has λ neighbors in Γ(x). Then every vertex in C\{x} has λ−(c−2)
neighbors in Γ(x)\C. Thus, there are (c − 1)(λ − (c − 2)) edges between C\{x} and Γ(x)\C. Since every
vertex in Γ(x)\C has at most n neighbors in C\{x}, we have (c − 1)(λ − (c − 2)) ⩽ n(k − (c − 1)), as
required.

As an immediate consequence of Lemma 3.4, we have the following corollary.

Corollary 3.5. Let Γ be an amply regular graph with parameters (v, k, λ, µ) having a clique C of order
c. Then (c − 1)(λ − (c − 2))
(k − (c − 1)) ⩽ µ − 1.

Proof. Let x be a vertex in C and let y be a vertex in Γ(x)\C. Note that there is a vertex z in C\{x}
such that z is not adjacent to y. Then, since d(y, z) = 2, the vertex y has at most µ − 1 neighbors in
Γ(x)\C. By Lemma 3.4, we obtain that µ − 1 is at least (c−1)(λ−(c−2))
(k−(c−1)) , as required.

We combine Lemma 3.2 and Lemma 3.4 to establish the following lemma.

Lemma 3.6. Let Γ be an amply regular graph with parameters (v, k, λ, µ) having smallest eigenvalue
−m. Suppose that Γ has a maximal clique of order c ⩾ (m − 1)(4m − 1) such that µ < c+m−1+
√D
2 , where
D = (c + m − 1)(c − (m − 1)(4m − 1)). Then

(c + m − 3)(k − c + 1) − 2(c − 1)(λ − c + 2) ⩾ (k − c + 1)√D. (3.2)

Proof. Let x be a vertex in C. For a vertex y in Γ(x)\C, we denote the number of neighbors of y in
C\{x} by ny. Let n = max{ny | y ∈ Γ(x)\C}. Then by Lemma 3.4, we have (c−1)(λ−(c−2))
(k−(c−1)) ⩽ n. Let
z be a vertex in Γ(x)\C having n neighbors in C\{x}, that is, the vertex z has n + 1 neighbors in C
including x. By Lemma 3.2, we have n + 1 ⩽ c+m−1−√D
2 . Thus, we obtain that

(c − 1)(λ − (c − 2))
(k − (c − 1)) + 1 ⩽ n + 1 ⩽ c + m − 1 − √D
2 ,

from which (3.2) follows directly.

Alternatively, Lemma 3.6 can be written as the following lemma.

Lemma 3.7. Let Γ be an amply regular graph with parameters (v, k, λ, µ) having smallest eigenvalue
−m such that µ > m(m − 1). Suppose that Γ has a maximal clique C of order c > µ
2

µ−m(m−1) − m + 1.
Then

((c + m − 3)(k − c + 1) − 2(c − 1)(λ − c + 2))
2 − (k − c + 1)
2(c + m − 1)(c − (m − 1)(4m − 1)) ⩾ 0. (3.3)

4

Proof. Let D = (c+m−1)(c−(m−1)(4m−1)). Since µ > m(m−1), the inequality c > µ2

µ−m(m−1) −m+1
implies that (µ − m(m − 1))c > µ
2 − (m − 1)(µ − m(m − 1)), which is equivalent to (2µ − c − m + 1)
2 < D.
Hence 2µ − c − m + 1 ⩽ |2µ − c − m + 1| < √D, that is, µ < c+m−1+
√D
2 . Since (µ − 2m(m − 1))2 ⩾ 0,

we have that µ
2 ⩾ 4m(m − 1)(µ − m(m − 1)). Then µ > m(m − 1) implies that µ2

µ−m(m−1) ⩾ 4m(m − 1),

and this shows that c > µ2

µ−m(m−1) − m + 1 ⩾ (m − 1)(4m − 1). Now we can apply Lemma 3.6, to obtain
the inequality (3.2), and this implies the inequality (3.3), as required.

Remark 2. We denote the polynomial on the left hand side of the inequality (3.3) by MΓ(c), and we
will call it the maximal-clique polynomial. Note that MΓ(c) is a cubic polynomial in the variable c and
that the leading coeﬃcient of MΓ(c) is positive.

4 The claw-bound and cliques

In this section, we recall the claw-bound which was found by several authors [8, Section 3]. From the
claw-bound, we will show that if an amply regular graph Γ with parameters (v, k, λ, µ) does not contain a
coclique of order ¯c in a local graph (a graph induced on the set of neighbors of a vertex), then Γ contains
a clique of order at least 2 + λ − (¯c − 2)(µ − 1).
The claw-bound is given below, and it follows from the principle of inclusion and exclusion ( [5, 9]).

Lemma 4.1. (Cf. [5, 9]) Let Γ be an amply regular graph with parameters (v, k, λ, µ). Let x be a vertex
of Γ and let ¯C be a coclique of order ¯c ⩾ 2 in Γ(x). Then
(¯c
2

)(µ − 1) ⩾ ¯c(λ + 1) − k

Remark 3. Lemma 4.1 says that if (¯c
2
)(µ − 1) < ¯c(λ + 1) − k, then the graph induced on Γ(x) contains
no coclique of order ¯c, i.e., the graph Γ does not contain a ¯c-claw.

From the claw-bound, we give a bound on the order of a clique in an amply regular graph when the
graph does not contain a ¯c-claw.

Lemma 4.2. Let Γ be an amply regular graph with parameters (v, k, λ, µ). If (¯c
2
)(µ − 1) < ¯c(λ + 1) − k
for some integer ¯c ⩾ 2, then Γ contains a clique of order at least 2 + λ − (¯c − 2)(µ − 1).

Proof. Let x be a vertex of Γ and let s be the maximum number such that the graph induced by
Γ(x) contains a coclique of order s. Note that, by Remark 3, we know that s ⩽ ¯c − 1. Assume that
{y1, y2, . . . , ys} is a coclique of order s in Γ(x). The vertex y1 has λ neighbors in Γ(x)\{y2, . . . , ys}
and that for each i ∈ {2, . . . , s}, the vertices y1 and yi have at most µ − 1 common neighbors in
Γ(x)\{y2, . . . , ys}. Hence, there are at least λ − (s − 1)(µ − 1) vertices in Γ(x) that are adjacent to y1 but
not adjacent to yi for all i ∈ {2, . . . , s}. If two such vertices were not adjacent, then those two vertices
together with y2, . . . , ys would induce a coclique of order s + 1, a contradiction. Thus, the graph induced
by Γ(x) contains a clique of order at least 1 + λ − (s − 1)(µ − 1) and hence, Γ contains a clique of order
at least 2 + λ − (s − 1)(µ − 1) ⩾ 2 + λ − (¯c − 2)(µ − 1).

As an application of the maximal clique polynomial, we prove that there cannot exist any strongly
regular graph having the feasible parameters (v, k, λ, µ) in the following theorem.

Theorem 4.3. Let m ⩾ 4 be an integer. Then, there are no strongly regular graphs with the following
parameters:

v = 1 + k + k(k − λ − 1)/µ,

k = (m + 1)(m(2 − µ) + 2λ)/2 + 1,

λ = (m−3)
5+15(m−3)
4+91(m−3)3+283(m−3)
2)
2 + 226(m − 3) + 148,

µ = (m − 3)3 + 10(m − 3)
2 + 33(m − 3) + 38.

5

Proof. Suppose that there exists a strongly regular graph Γ with such parameters (v, k, λ, µ) for some
integer m ⩾ 4. Set ¯c = m + 2. Then (¯c
2
)(µ − 1) < ¯c(λ + 1) − k, and, by Lemma 4.2, we know that Γ
contains a clique of order at least 2 + λ − m(µ − 1). Thus, the graph Γ contains a maximal clique C of
order c1 ⩾ 2 + λ − m(µ − 1). Note that the Delsarte bound implies that 2 + λ − m(µ − 1) ⩽ c1 ⩽ 1 + k
m .
Recall the maximal-clique polynomial MΓ(c). Since m ⩾ 4, we know that

c1 ⩾ 2 + λ − m(µ − 1) > µ
2

µ − m(m − 1) − m + 1.

Then Lemma 3.7 implies that MΓ(c1) ⩾ 0. Note that MΓ(0) > 0, MΓ(2 + λ − m(µ − 1)) < 0 and
MΓ(1 + k
m ) < 0. But this is not possible since MΓ(c) is a cubic polynomial with a positive leading
coeﬃcient (Remark 2). Therefore, there are no strongly regular graphs with such parameters (v, k, λ, µ)
for all integer m ⩾ 4.

5 Acknowledgements

Gary Greaves is partially supported by the Singapore Ministry of Education Academic Research Fund
(Tier 1); grant numbers: RG29/18 and RG21/20.
Jack H. Koolen is partially supported by the National Natural Science Foundation of China (No.12071454),
Anhui Initiative in Quantum Information Technologies (No. AHY150000) and by the project “Analysis
and Geometry on Bundles” of Ministry of Science and Technology of the People’s Republic of China.
Jongyook Park is partially supported by Basic Science Research Program through the National Re-
search Foundation of Korea funded by Ministry of Education (NRF-2017R1D1A1B03032016) and the
National Research Foundation of Korea (NRF) grant funded by the Korea government (MSIT) (NRF-
2020R1A2C1A01101838).

References

[1] A.E. Brouwer, A.M. Cohen and A. Neumaier, Distance-Regular Graphs, Springer-Verlag, Berlin,
1989.

[2] A.E. Brouwer and W.H. Haemers, Spectra of Graphs, Universitext, Springer, 2012.

[3] A.E. Brouwer and H. Van Maldeghem, Strongly regular graphs, preprint (downloaded on October
19, 2020), https://homepages.cwi.nl/~aeb/math/srg/rk3/srgw.pdf.

[4] P. Delsarte, An algebraic approach to the association schemes of coding theory. PhD thesis, Univer-
site Catholique de Louvain, 1973.

[5] A.L. Gavrilyuk, On the Koolen-Park inequality and Terwilliger graphs, Electron. J. Combin. 17
(2010) ♯R125.

[6] C. Godsil and G. Royle, Algebraic Graph Theory, Springer-Verlag, Berlin, 2001.

[7] W.H. Haemers, Interlacing eigenvalues and graphs, Linear Algebra Appl. 226/228 (1995), 593-616.

[8] J.H. Koolen, Q. Iqbal, J. Park and M.U. Rehman, There does not exist a distance-regular graph
with intersection array {80, 54, 12; 1, 6, 60}, Graphs Combin. 35 (2019) 1597–1608.

[9] J.H. Koolen and J. Park, Shilla distance-regular graphs, European J. Combin. 31 (2010) 2064–2073.

[10] A. Neumaier, Strongly regular graphs with smallest eigenvalue −m, Arch. Math. (Basel) 33 (1979)
392-–400.
 6

6 Appendix

In this appendix, we give tables of parameters (v, k, λ, µ) for nonexistent strongly regular graphs with
smallest eigenvalue −4, −5, −6 or −7. Note that all of those parameters (v, k, λ, µ) are feasible (see the
deﬁnition in Section 2). In the tables below, ‘forbidden range’ means that the graph does not contain a
maximal clique of order in the forbidden range (Lemma 3.7), ‘Delsarte bound’ means ⌊1 + k
m ⌋, where −m
is the smallest eigenvalue, and ‘guaranteed clique order’ means the graph contains a (maximal) clique of
order at least that guaranteed clique order (Lemma 4.2).

µ v k λ forbidden range Delsarte bound guaranteed clique order
58 23276 1330 372 [71, 340] 333 146
62 25025 1426 399 [74, 368] 357 157
80 27455 1696 480 [92, 450] 425 166
82 38875 2046 569 [94, 539] 512 247

Table 1: Parameters for nonexistent strongly regular graphs with smallest eigenvalue −4

µ v k λ forbidden range Delsarte bound guaranteed clique order
115 133570 4365 960 [136, 885] 874 278
122 230958 5917 1276 [142, 1202] 1184 673
150 235586 6625 1440 [170, 1367] 1326 697
152 317628 7747 1666 [172, 1593] 1550 913
168 328560 8283 1786 [187, 1714] 1657 953
170 259000 7395 1610 [189, 1538] 1480 767
172 309016 8127 1758 [191, 1686] 1626 905
205 225885 7580 1675 [224, 1605] 1517 453
214 404587 10374 2241 [233, 2170] 2075 1178
240 314116 9675 2122 [258, 2052] 1936 929
240 485815 12040 2595 [258, 2524] 2409 1402

Table 2: Parameters for nonexistent strongly regular graphs with smallest eigenvalue −5

7

µ v k λ forbidden range Delsarte bound guaranteed clique order
201 545832 11451 2070 [232, 1926] 1909 472
204 895665 14784 2628 [235, 2484] 2465 1412
206 1331968 18122 3186 [237, 3042] 3021 1958
210 997920 15834 2808 [241, 2664] 2640 1556
212 1371657 18656 3280 [242, 3137] 3110 2016
252 1352572 20196 3570 [282, 3428] 3367 2066
254 1756209 23108 4057 [284, 3915] 3852 2541
264 717574 15048 2722 [293, 2582] 2509 620
267 886222 16821 3020 [296, 2880] 2804 1160
270 1112320 18954 3378 [299, 3237] 3160 1766
273 1423818 21567 3816 [302, 3675] 3595 2186
276 1867591 24840 4364 [305, 4223] 4141 2716
280 1026875 18544 3318 [309, 3178] 3091 1646
315 855570 17949 3248 [344, 3110] 2992 738
324 1462209 23808 4232 [353, 4093] 3969 2296
327 1791882 26481 4680 [356, 4540] 4414 2726
330 2232000 29694 5218 [359, 5078] 4950 3246
380 1503625 26144 4668 [408, 4530] 4358 2396
390 2223180 32214 5688 [418, 5549] 5370 3356
438 1148448 24522 4446 [466, 4311] 4088 952
440 1212001 25250 4569 [468, 4433] 4209 1498
450 1605240 29394 5268 [478, 5132] 4900 2576
456 1920621 32370 5769 [484, 5632] 5396 3041
468 2835028 39852 7026 [496, 6888] 6643 4226
470 3039520 41354 7278 [498, 7140] 6893 4466
472 3263897 42946 7545 [500, 7407] 7158 4721

Table 3: Parameters for nonexistent strongly regular graphs with smallest eigenvalue −6

8

µ v k λ forbidden range Delsarte bound guaranteed clique order
322 1769600 25753 3948 [365, 3702] 3680 1061
329 4271421 40460 6055 [372, 5810] 5781 3761
338 6057152 48841 7260 [380, 7016] 6978 4903
364 2747626 34125 5180 [406, 4937] 4876 2278
369 5619713 49152 7331 [411, 7088] 7022 4757
372 5783316 50065 7464 [414, 7221] 7153 4869
382 2369800 32463 4958 [424, 4716] 4638 1531
392 5873750 51793 7728 [434, 7485] 7400 4993
394 7404736 58305 8660 [436, 8417] 8330 5911
417 7593750 60743 9028 [458, 8786] 8678 6118
467 2897225 39688 6063 [508, 5824] 5670 1871
474 4178176 48025 7260 [515, 7021] 6861 3951
483 7331625 64232 9583 [524, 9342] 9177 6211
486 9133968 71921 10684 [526, 10443] 10275 7291
522 3891200 48633 7388 [562, 7150] 6948 3222
522 7314000 66693 9968 [562, 9728] 9528 6323
532 4231150 51198 7763 [572, 7525] 7315 3517
539 7818591 70070 10465 [579, 10226] 10011 6701
595 3189151 46998 7217 [635, 6982] 6715 1279
630 3325728 49385 7588 [670, 7354] 7056 1300
630 10072881 85988 12817 [670, 12578] 12285 8416
634 11915776 93825 13940 [673, 13701] 13404 9511
665 12031999 96558 14357 [704, 14118] 13795 9711
689 5860526 68575 10380 [728, 10144] 9797 5566
714 3844176 56525 8680 [753, 8447] 8076 1552
735 5498361 68600 10423 [774, 10188] 9801 4553
742 6244525 73458 11123 [781, 10888] 10495 5197
746 6729536 76465 11556 [785, 11321] 10924 6343
762 9236916 90551 13582 [801, 13346] 12936 8257
763 9431401 91560 13727 [802, 13490] 13081 8395
770 4190144 61285 9408 [809, 9176] 8756 1720
777 12822369 107744 16051 [816, 15813] 15393 10621
780 13752261 111800 16633 [819, 16395] 15972 11182
816 12114648 107321 16024 [855, 15787] 15332 10321
833 4660685 67228 10311 [872, 10079] 9605 2825
841 5217895 71478 10925 [880, 10692] 10212 3367
849 5861241 76120 11595 [888, 11362] 10875 4813
882 9888000 100793 15148 [921, 14913] 14400 8983
888 10974960 106553 15976 [927, 15740] 15222 9769
889 11171083 107562 16121 [928, 15885] 15367 9907
900 5357638 74925 11468 [939, 11236] 10704 3379
903 14473410 123403 18396 [942, 18159] 17630 12084
918 5105376 73865 11332 [957, 11101] 10553 3081
924 6973876 86625 13160 [963, 12927] 12376 5778
980 13835098 125685 18788 [1018, 18552] 17956 11937
990 5550960 79985 12268 [1028, 12037] 11427 3369
1007 8792525 101548 15363 [1045, 15130] 14507 8323

Table 4: Parameters for nonexistent strongly regular graphs with smallest eigenvalue −7

9
