<!-- source: http://elib.mi.sanu.ac.rs/files/journals/mv/282/mvn282p37-42.pdf | converted from PDF -->

MATEMATI ˇCKI VESNIK
MATEMATIQKI VESNIK 73, 1 (2021), 37–42
March 2021
 research paper
originalni nauqni rad

ON THE ERD ˝OS-GY ´ARF ´AS CONJECTURE FOR SOME CAYLEY
GRAPHS

Mohsen Ghasemi and Rezvan Varmazyar

Abstract. In 1995, Paul Erd˝os and Andr´as Gy´arf´as conjectured that for every graph X
of minimum degree at least 3, there exists a non-negative integer m such that X contains
a simple cycle of length 2
m. In this paper, we prove that the conjecture holds for Cayley
graphs of order 2p2 and 4p.
 1. Introduction

In this paper all graphs will be simple and ﬁnite and all groups will be ﬁnite. For a
graph X, we let V (X), E(X) and Aut(X) denote the vertex set, the edge set, the full
group of automorphisms of X, respectively.
A graph X is said to be vertex-transitive if Aut(X) acts transitively on V (X).
The minimum degree of X is the minimum degree of its vertices. Also, a k-cycle is a
cycle of length k.
Several questions on cycles in graphs have been posed by Erd˝os and his colleagues
(see, e.g. [1]). In particular, in 1995 Erd˝os and Gy´arf´as [3] asked: If G is a graph with
minimum degree at least three, does G have a cycle whose length is a power of 2?
This is known as the Erd˝os-Gy´arf´as conjecture. In fact, Erd˝os and Gy´arf´as [3] said
that “we are convinced now that this is false and no doubt there are graphs for every
r every vertex of which has degree ≥ r and which contain no cycle of length 2k, but
we never found a counterexample even for r = 3”.
Using the computer searches, Markstr¨om [6] veriﬁed the conjecture for cubic
graphs of order at most 29, and found that the smallest cubic planar graph with no
4- or 8-cycles has 24 vertices. Note that this graph contains a 16-cycle. Shauger [8]
proved the conjecture for K1,m–free graphs of minimum degree at least m + 1 or max-
imum degree at least 2m − 1. Daniel and Shauger [2] proved the conjecture for planar
claw-free graphs. Also, in [5] it is proved that the conjecture holds for 3-connected

2020 Mathematics Subject Classiﬁcation: 05C38, 20B25
Keywords and phrases: Erd˝os-Gy´arf´s conjecture; Cayley graphs; cycles of graphs.

37

38 On the Erd˝os-Gy´arf´as conjecture

cubic planar graphs (see also [7]). In [4] the authors proved that the conjecture holds
for Cayley graphs on some special groups.
In this paper we study the conjecture for some families of Cayley graphs. Let G
be a ﬁnite group and S a subset of G not containing the identity element 1. The
Cayley digraph X = Cay(G, S) on G with respect to S is deﬁned to have vertex set
V (X) = G and edge set E(X) = {(g, sg) | g ∈ G, s ∈ S}. If S91 = S, then Cay(G, S)
can be viewed as undirected graph, identifying an undirected edge {g, h} with two
directed edges (g, h) and (h, g). This graph is called the Cayley graph on G with
respect to S. It is well-known that Aut(X) contains the right regular representation
R(G) of G, the acting group of G by right multiplication, and X is connected if and
only if G = ⟨S⟩, that is, S generates G.
Let G be a ﬁnite group and let S and T be two subsets of G not containing the
identity 1 of G. If there is an α ∈ Aut(G) such that Sα = T , then S and T are said
to be equivalent, denoted by S ∼= T . It is easy to see that Cay(G, S) ∼= Cay(G, Sα).
Throughout this paper, we denote by Zn the cyclic group of order n and by Z
∗
n the
multiplicative group of Zn consisting of numbers coprime to n. Also, an element of
order 2 is called involution.
 2. Main results

Suppose that X = Cay(G, S) where |G| = 2p2. If G is an abelian group then by [4,
Theorem 1.3], G has a 4-cycle. Also, if G is non-abelian and p = 2 then G is isomorphic
to the dihedral group D8 or quaternion group Q8 and by [4] X contains a simple cycle
whose length is a power of two. Thus we may suppose that p > 2. From the elementary
group theory we know that up to isomorphism there are three non-abelian groups of
order 2p
2 deﬁned as:

G = G1(p) = ⟨a, b | a
p = b
2 = 1, bab
91 = a
91⟩;

G = G2(p) = ⟨a, b, c | ap = bp = c
2 = 1 = [a, b], c
91ac = a91, c
91bc = b91⟩;

G = G3(p) = ⟨a, b, c | ap = bp = c
2 = 1, [a, b] = [a, c] = 1, c
91bc = b
91⟩.

If G = G1(p) then by [4, Theorem 2.2] X has a cycle of length 4, 8 or 16. Thus
we may suppose that G ∼= G2(p) or G ∼= G3(p).

Theorem 2.1. Every connected Cayley graph X = Cay(G2(p), S) contains a cycle of
length 4 or 16.

Proof. It is easy to see that o(aibj) = p where 0 ≤ i, j ≤ p and i, j are not zero
simultaneously, and o(aibjc) = 2, where 0 ≤ i, j ≤ p − 1. Since X is connected it
follows that S contains an involution. Thus we may suppose that a
ib
jc ∈ S. Since
Aut(G2(p)) is transitive on the set of involutions in G2(p) we may suppose that c ∈ S.
Now we consider the following cases.
Case 1. S contains just involutions.

We may suppose that a
mb
nc belongs to S, where 0 ≤ m, n ≤ p−1 and m, n are not

M. Ghasemi, R. Varmazyar 39

zero simultaneously. Without loss of generality we may suppose that n ̸= 0. Since the
map a ↦→ a, b ↦→ b
n and c ↦→ a
mc is an automorphism of G2(p) one may suppose that
bc ∈ S. Since X is connected graph S must contain another element of order 2, say
a
kblc, where 0 ≤ k, l ≤ p − 1. If l = 0 then a
kc ∈ S. Since the map a ↦→ a
k, b ↦→ b and
c ↦→ c is an automorphism of G2(p) one may suppose that ac ∈ S. Thus {c, bc, ac} ⊆ S.
Now (ab
92, b
2c, b
91, abc, a91, a
2c, a
92b, a
2b91c, a
91b, ac, 1, c, a, a
91bc, ab
91, a
91b
2c, ab
92) is
a 16-cycle in X. Thus we may suppose that l ̸= 0. Again since the map a ↦→ a,
b ↦→ b
91 and c ↦→ akc is an automorphism of G2(p) one may suppose that b91c ∈ S.
Also, we know that c ∈ S. Thus {c, bc, b91c} ⊆ S. Now (1, c, b, cb, 1) is a 4-cycle in X.

Case 2. S contains an element of order p.

We may suppose that a
mbn ∈ S, where 0 ≤ m, n ≤ p − 1. First suppose that
m = 1 and n = 0. Then a ∈ S and so {c, a} ⊆ S. Now (1, c, ac, a
91, 1) is a 4-cycle
in X. Now suppose that m ̸= 1 and n ̸= 0. It is easy to see that the map a ↦→ a,
b ↦→ ambn and c ↦→ c is an automorphism of G2(p). Thus we may suppose that b ∈ S.
Thus {b, c} ⊆ S and so (1, c, bc, b
91, 1) is a 4-cycle in X.

Theorem 2.2. Every connected Cayley graph X = Cay(G3(p), S) contains a cycle of
length 4, 8 or 16.

Proof. It is easy to see that o(aibjc) = 2p, where 0 < i ≤ p − 1 and 0 ≤ j ≤ p − 1. We
have o(aibj) = p, where 0 ≤ i, j ≤ p − 1 and i, j are not zero simultaneously. Also,
o(b
ic) = 2, where 0 ≤ i ≤ p − 1. Since X is connected it follows that S does not
contain just involutions. Thus we may consider the following cases:
Case 1. S contains an involution and element of order p.

We may suppose that a
ib
j ∈ S. If i = 0 or j = 0 than a ∈ S or b ∈ S. Since
S = S91 it follows that {a, a
91} ⊆ S or {b, b
91} ⊆ S. Also, since Aut(G3(p)) is
transitive on the set of involutions in G3(p), one may assume that c ∈ S. Thus either
{a, a
91, c} ⊆ S or {b, c, b91} ⊆ S. For the ﬁrst case (1, a, ac, c, 1) is a 4-cycle in X and
for the second case (1, c, b91c, b, 1) is a 4-cycle in X. Thus we may suppose that i ̸= 0
and j ̸= 0. The map a ↦→ ai, b ↦→ bj and c ↦→ c is an automorphism of G3(p) and so
{ab, a
91b91, c} ⊆ S. Now (1, c, abc, ab
91, a
2, ca
2, cab, ab, 1) is a 8-cycle in X.

Case 2. S contains an involution and an element of order 2p.

We may suppose that a
ibjc ∈ S, where 0 < i ≤ p−1 and 0 ≤ j ≤ p−1. Since
Aut(G3(p)) is transitive on elements of order 2p, we may suppose that ac ∈ S. Also,
since S = S91 it implies that a
91c ∈ S. Suppose that bmc is an involution belongs to S.
If m = 0 then c ∈ S. Thus {ac, a
91c, c} ⊆ S and (1, c, a, ac, 1) is a 4-cycle in X. Thus
we may suppose that m ̸= 0. The map a ↦→ a, b ↦→ bm and c ↦→ c is an automorphism
of G3(p) and so we may suppose that bc ∈ S. Thus {ac, a
91c, bc} ⊆ S. First suppose
that p > 3. It is easy to see that (ab, b
91c, a
91b, a
92b91c, a
93b, a
93c, a
92, a
92bc, a
91b91,
a
91b
2c, b
92, ab
2c, ab
91, bc, 1, ac, ab) is a 16-cycle in X. Now suppose that p = 3. Now
(b, c, a2, a
2bc, b
2, b
2c, a
2b, ab
2c, b) is a 8-cycle in X.

Case 3. S contains an element of order p and 2p.

40 On the Erd˝os-Gy´arf´as conjecture

In this case we may suppose that a
ibjc ∈ S, where 0 < i ≤ p − 1 and 0 ≤ j ≤ p − 1.
First suppose that j = 0. Then a
ic ∈ S. Since S = S91 and the map a ↦→ a
i, b ↦→ b,
c ↦→ c is an automorphism of G3(p), it follows that {ac, a
91c} ⊆ S. Also, suppose that
a
mbn where 0 ≤ m, n ≤ p − 1, is an element of order p which belongs to S. If n = 0
then am ∈ S. Now the map a ↦→ a
m, b ↦→ b, c ↦→ c is an automorphism of G3(p) and
so we may suppose that a ∈ S. Thus {ac, a
91c, a} ⊆ S and (1, ac, c, a
91c, 1) is a 4-cycle
in X. If n ̸= 0 then the map a ↦→ a, b ↦→ bn, c ↦→ c is an automorphism of G3(p)
and so we may suppose that a
mb ∈ S. Therefore {ac, a
91c, a
mb, a
9mb
91} ⊆ S. Now it
is easy to see that (a
9m+2b
91, a
1−mbc, a
9mb91, 1, a
mb, a
m+1b91c, a
m+2b, a
2, a
9m+2b91)
is a 8-cycle in X. Now suppose that j ̸= 0. Since S = S91 and the map a ↦→ a
i,
b ↦→ b
j, c ↦→ c is an automorphism of G3(p), it follows that {abc, a
91bc} ⊆ S. Also,
suppose that a
mbn is an element of order p which belongs to S. If n = 0 then
{a, abc, a91bc} ⊆ S and (1, abc, bc, a
91bc, 1) is a 4-cycle in X. Also, if n ̸= 0 then the
map a ↦→ a, b ↦→ b
n, c ↦→ c is an automorphism of G3(p) and so we may suppose that
amb ∈ S. Again since the map a ↦→ a, b ↦→ b, c ↦→ b91c is an automorphism of G3(p) it
follows that {ac, a
91c} ⊆ S. Therefore {ac, a
91c, a
mb, a
9mb91} ⊆ S. Now it is easy to
see that (a
9m+2b91, a
1−mbc, a
9mb
91, 1, a
mb, a
m+1b91c, a
m+2b, a
2, a
9m+2b
91) is a 8-cycle
in X.

Case 4. S contains just elements of order 2p.

We may suppose that a
ibjc ∈ S, where 0 < i ≤ p−1 and 0 ≤ j ≤ p−1. Since
Aut(G3(p)) is transitive on elements of order 2p we may suppose that {ac, a
91c} ⊆ S.
Also, suppose that ambnc ∈ S, where 0 < m ≤ p−1 and 0 ≤ n ≤ p−1. Since X is con-
nected and S contains just elements of order 2p we may suppose that n ̸= 0. Now again
since the map a ↦→ a, b ↦→ bn, c ↦→ c is an automorphism of G3(p) we may suppose that
{ac, a
91c, a
mbc, a
9mbc} ⊆ S. If m = 1 then (1, abc, a2, ac, 1) is a 4-cycle in X. Thus we
may suppose that m > 1. Now (amb91c, a
m91b, a
2m91c, a
2m, a
mbc, 1, ac, am+1b, a
mb
91c)
is a 8-cycle in X.

Now we consider the Cayley graphs of order 4p. Suppose that X = Cay(H, S),
where |H| = 4p. If G is an abelian group then by [4, Theorem 1.3], G has a 4-cycle.
Also, if p = 2 then G is isomorphic to the dihedral group D8 or quaternion group
Q8 and by [4], X contains a simple cycle whose length is a power of two. Thus we
may suppose that p > 2. From the elementary group theory we know that up to
isomorphism there are three non-abelian groups of order 4p deﬁned as:

H = H1(p) = ⟨a, b | a
2p = b2 = 1, bab
91 = a
91⟩;

H = H2(p) = ⟨a, b | a
2p = 1, b
2 = a
p, b
91ab = a
91⟩;

H = H3(p) = ⟨a, b | a
p = b
4 = 1, b
91ab = a
r, r2 ≡ −1(p)⟩.

If H = H1(p) then by [4, Theorem 2.2] X has a cycle of length 4, 8 or 16. Thus we
may suppose that H ∼= H2(p) or H ∼= H3(p).

Theorem 2.3. Every connected Cayley graph X = Cay(H2(p), S) contains a 4-cycle.

Proof. Clearly H = H2(p) = {a
i, ba
i | 0 ≤ i ≤ 2p − 1}. Since H cannot be generated
by elements in ⟨a⟩, one may assume that ba
i ∈ S. Furthermore, a and ba
i (0 ≤ i ≤

M. Ghasemi, R. Varmazyar 41

2p − 1) have the same relations as a and b. This implies there is an automorphism of
H which maps a to a and ba
i to b. Thus one may assume that b, b
91 ∈ S. Now we
consider the following cases.
Case 1. a
m ∈ S, where m ̸= 0.

First suppose that (m, 2p) = 1. Now the map a ↦→ a
m, b ↦→ b is an automorphism
of H2(p) and so we may suppose that {a, a
91} ⊆ S. Now it is easy to see that
(1, a
91, ab, b, 1) is a 4-cycle in X. Now suppose that (m, 2p) ̸= 1. Since H = ⟨S⟩, it
follows that either a
i ∈ S where (i, 2p) = 1 or ba
j ∈ S where (j, 2m) = 1. For the
former case with the similar arguments as before {a, a
91} ⊆ S and (1, a
91, ab, b, 1) is
a 4-cycle in X. For the latter case the map a ↦→ aj, b ↦→ b is an automorphism of
H2(p) and so we may suppose that {b, b
91, ba, a91b
91} ⊆ S. Now (1, b, b2, a
91b, 1) is a
4-cycle in X.

Case 2. ba
m ∈ S.

First suppose that (m, 2p) = 1. In this case again the map a ↦→ a
m, b ↦→ b
is an automorphism of H2(p) and so we may suppose that {ba, a
91b91} ⊆ S. Now
(1, b, b2, a
91b, 1) is a 4-cycle in H2(p). Now suppose that (m, 2p) ̸= 1. If m = p then
{b, b
91, ba
m, a
9mb91} ⊆ S. Since H = ⟨S⟩ one may suppose that either a
i ∈ S where
(i, 2p) = 1 or ba
j ∈ S where (j, 2p) = 1. For the former case the map a ↦→ a
i, b ↦→ b is
an automorphism of H2(p) and so {b, b
91, a, a91} ⊆ S and (1, a
91, ab, b, 1) is a 4-cycle
in X. Also, for the latter case the map a ↦→ aj, b ↦→ b is an automorphism of H
and so {b, b
91, ba, a91b91} ⊆ S. Now (1, b, b2, a
91b, 1) is a 4-cycle in X. Therefore we
may suppose that m = 2. Since H = ⟨S⟩ we may suppose that either a
i ∈ S where
(i, 2p) = 1 or ba
j ∈ S where (j, 2p) = 1. Now with the similar arguments as before
we get a 4-cycle in X.

Theorem 2.4. Every connected Cayley graph X = Cay(H3(p), S) contains a 4-cycle.

Proof. Clearly H = H3(p) = {a
i, ba
i, b
2a
i, b
3a
i | 0 ≤ i ≤ p − 1}. Furthermore
o(ba
i) = o(b
3a
i) = 4 and o(b2a
i) = 2. Now we consider the following cases.
Case 1. a
i ∈ S, where i ̸= 0.

In this case the map a ↦→ a
i, b ↦→ b is an automorphism of H3(p) and so we may
suppose that {a, a
91} ⊆ S. Since G = ⟨S⟩, it follows that either ba
i ∈ S or b3a
i ∈ S.
In both cases the map a ↦→ a, b ↦→ btai (t ∈ {1, 3}) is an automorphism of H3(p).
Thus {b, b
91} ⊆ S and (1, b, b2, b
3, 1) is a 4-cycle in X.

Case 2. a
i /∈ S.

Since G = ⟨S⟩, one may assume that either ba
i ∈ S or b3a
i ∈ S. Also, the map
a ↦→ a, b ↦→ b
ta
i (t ∈ {1, 3}) is an automorphism of H3(p). Thus {b, b
91} ⊆ S and
(1, b, b2, b
3, 1) is a 4-cycle in X.

Acknowledgement. The authors are indebted to the referee for comments that
have improved this paper.

42 On the Erd˝os-Gy´arf´as conjecture

References

[1] J.A. Bondy, Extremal problems of Paul Erd˝os on circuits in graphs, in: Paul Erd˝os and his
Mathematics, II, Bolyai Soc. Math. Stud., 11, Janos Bolyai Math. Soc., Budapest (2002),
135–156.
[2] D. Daniel, S.E. Shauger, A result on the Erd˝os-Gyarfas conjecture in planer graphs, In: Pro-
ceedings of the Thirty-Second Southeastern International Conference on Combinatorics, Graph
Theory and Computing (Baton Rouge, LA, 2001), 153, 129–139.
[3] P. Erd˝os, Some old and new problems in various branches of combinatorics, Discrete Math.,
165/166 (1997), 227–231.
[4] M.H Ghaﬀari, Z. Mostaghim, Erd˝os-Gyarfas conjecture for some families of Cayley graphs,
Aequat. Math., 92 (2017), 1–6.
[5] C.C. Heckman, R. Krakovski, Erd˝os-Gyarfas conjecture for cubic planar graphs, Electron. J.
Comb., 20(2) (2013), 7–43.
[6] K. Markstr¨om, Extremal graphs for some problems on cycles in graphs, In: Proceedings of
the Thirty-Fifth Southeastern International Conference on Combinatorics, Graph Theory and
Computing, 171 (2004), 179–192.
[7] P.S. Nowbandegani, H. Esfandiari, M.H. Shirdareh Haghighi, B. Khodakhast, Note on the
Erd˝os-Gyarfas conjecture in claw-free graphs, Discuss. Math. Graph Theory., 34 (2014), 635–
640.
[8] S.E. Shauger, Results on the Erd˝os-Gyarfas conjecture in K1,m-free graphs, In: Proceedings
of the Twenty-Ninth Southeastern International Conference on Combinatorics, Graph Theory
and Computing(Boca Raton, FL, 1998), 134 (1998), 61–65.

(received 18.05.2019; in revised form 21.12.2019; available online 15.06.2020)

Department of Mathematics, Urmia University, Urmia 57135, Iran
E-mail: m.ghasemi@urmia.ac.ir
Department of Mathematics, Khoy Branch, Islamic Azad University, Khoy 58168-44799, Iran
E-mail: varmazyar@iaukhoy.ac.ir
