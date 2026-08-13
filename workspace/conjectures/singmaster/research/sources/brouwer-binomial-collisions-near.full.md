<!-- source: https://aeb.win.tue.nl/preprints/binomcoll.pdf | converted from PDF -->

Binomial collisions and near collisions

Aart Blokhuis, Andries Brouwer, Benne de Weger
Eindhoven University of Technology
a.blokhuis@tue.nl, aeb@cwi.nl, b.m.m.d.weger@tue.nl

July 21, 2017

Abstract

We describe eﬃcient algorithms to search for cases in which binomial
coeﬃcients are equal or almost equal, give a conjecturally complete list
of all cases where two binomial coeﬃcients diﬀer by 1, and give some
identities for binomial coeﬃcients that seem to be new.

1 Introduction

Let us call a quadruple (n, k, m, l) with 2 ≤ k ≤ 1
2 n and 2 ≤ l ≤ 1
2 m a (binomial)
collision when k < l and (n
k) = (m
l ), and a near collision when (m
l )−(n
k) = d > 0
with (m
l ) ≥ d3. The exponent 3 is somewhat arbitrary. Maybe 5 is a more
natural exponent, see the end of this paper.
Collisions have been studied by many authors. Some references will be given
below. In this note we report on computer searches for collisions and near
collisions, and give seven inﬁnite families of near collisions.

2 Collisions

We list the known collisions. There are the double collision
(78
2
 ) = (15
5
 ) = (14
6
 ) = 3003,

six further sporadic examples given in the table below:

n k m l (m
l ) = (n
k)

16 2 10 3 120
21 2 10 4 210
56 2 22 3 1540
120 2 36 3 7140
153 2 19 5 11628
221 2 17 8 24310

and a miraculous inﬁnite family given by
(F2i+2F2i+3
F2iF2i+3
 ) = (
F2i+2F2i+3 − 1
F2iF2i+3 + 1
 ) for i = 1, 2, . . . ,

1

where Fi is the ith Fibonacci number (deﬁned by F0 = 0, F1 = 1, Fi+1 =
Fi + Fi−1 for i ≥ 1). The inﬁnite family is due to Lind [9], and was rediscovered
by several others such as Singmaster [15] and Tovey [18]. Examples are
(
15
5
 ) = (14
6
 ), (104
39
 ) = (103
40
 )
, (714
272
) = (
713
273
), (
4895
1869
) = (
4894
1870
)
.

Twenty years ago one of us conjectured

Conjecture 2.1 ([20]) There are no other collisions than those given above.

The current status is as follows.

Theorem 2.2 There are no unknown collisions in the following cases:

• (k, l) = (2, 3), (2, 4), (2, 5), (2, 6), (2, 8), (3, 4), (3, 6), (4, 6), (4, 8),

• (m, l) = (n − 1, k + 1), (n − 1, k + 2), (n − 2, k + 1),

• n ≤ 106,

• (n
k) ≤ 1060.

Proof. The ﬁrst two parts can be found in the literature.
The case (k, l) = (2, 3) was settled in [2]. The case (k, l) = (2, 4) was
settled in [12], and also in [19]. The case (k, l) = (2, 5) was settled in [5].
The cases (k, l) = (2, 6), (2, 8), (3, 6), (4, 6), (4, 8) were settled in [16]. The case
(k, l) = (3, 4) was settled in Mordell [11] (actually, he solved an equivalent
equation and seems not to have noted the relation to binomial coeﬃcients).
The case (m, l) = (n − 1, k + 1) was settled in [18] (and yields the inﬁnite
family). The cases (m, l) = (n − 1, k + 2), (n − 2, k + 1) were settled in [17].
The last two parts are the results of computer searches we report on in this
paper. Some details are given below. 2

Earlier computer searches handled n ≤ 10
3 and (n
k) ≤ 10
30 ([20]). In the
literature one also ﬁnds ﬁniteness results ([7], [4]), and results on the number of
times an integer may occur as binomial coeﬃcient ([14], [1], [8]).

2.1 Settling n ≤ 10
6

In order to ﬁnd all collisions with n ≤ N for some ﬁxed N , generate a list of
all values (n
k) with 2 ≤ k ≤ n/2 and n ≤ N . Sort it, and compare successive
elements to ﬁnd duplicates.
Now the list has length about 1
4 N 2, and probably does not ﬁt into memory.
One approach is to split the list into parts, e.g. into the sublists consisting of
all binomial coeﬃcients between 10
e−1 and 10
e, for all relevant e. We tried this
in Mathematica and did N = 34000 in 23h30m on a 2.6 GHz Intel i7.
A diﬀerent approach is to have a table and a priority queue, both of size N .
Both contain the same elements. Initially both contain the numbers (n+2
2 ) for
n < N . The priority queue is kept sorted. At each step the top two elements are
compared for equality. Afterwards the top element is discarded. When (n+k
k ) is
discarded, the new value (n+k+1
k+1 ) is added, unless k ≥ n. The new value needed

2

is computed from the old one via (n+k+1
k+1 ) = (n+k
k ) + (n+k
k+1). Note that the value
(n+k
k+1) is present in the table at index n − 1 at the moment it is needed.
Computation time for the algorithms as described is cubic in N if the precise
value of the binomial coeﬃcients is computed, since not only the length of the list
grows, but also the size of the numbers. Bounded precision suﬃces to ensure that
(almost) collisions are unlikely, and reduces the time needed to O(N 2 log N ).
Almost collisions still occur (for example, (102091
12877 ) = 1.256839391954534·10
16800,
(200954
9642 ) = 1.256839391954529 · 1016800). We used interval arithmetic to distin-
guish almost equal numbers, and full exact multiple length arithmetic in the
few cases where the interval arithmetic did not suﬃce. We tried this in C, with
a custom data type (since the usual data types do not handle large exponents,
or are too slow), and did N = 10
6 in 56h14m on an old 2 GHz PC.

2.2 Settling (
n
k) ≤ 10
60

In order to ﬁnd all collisions with (n
k) ≤ M we handle each relevant pair (k, l)
separately. Let lmax be the largest l such that (2l
l ) ≤ M . As we saw, the pairs
(k, l) with k < l ≤ 4 have been done already, so it suﬃces to handle 5 ≤ l ≤ lmax,
and for each l the values of k with 2 ≤ k ≤ l − 1, with k ≥ 3 if l = 5.
Given a pair (k, l), let mmax be the largest m with (m
l ) ≤ M . Make a list
of all m with 2l ≤ m ≤ mmax, and discard the m for which (m
l ) cannot be of
the form (n
k). What is left are possible collisions, and in practice only actual
collisions are left.
The discarding is done via a sieving process. The function f (n) = (n
k)

is a polynomial of degree k in the variable n, with rational coeﬃcients. The
denominators of the coeﬃcients have only prime factors ≤ k. For any prime
p > k the function f induces a polynomial map from Fp to itself. Let A(k, p) be
the size of the image. Experience shows that A(k, p) ≈ (1−e−1)p when k is odd,
and A(k, p) ≈ (1 − e
−1/2)p when k is even. See below for more remarks on this
function A(k, p). Since 1 − e−1 = 0.63... and 1 − e−1/2 = 0.39..., a signiﬁcant
fraction of all residues mod p cannot be of the form (n
k). Now pick p > l > k,
and look at (a
l) for 0 ≤ a ≤ p − 1. Whenever (a
l) is not in the mod p image of
f , discard all (m
l ) with m ≡ a (mod p) from the list.
Repeating this sieve action for all primes less than 500 (stopping earlier when
the list has become empty) we found all collisions up to M = 10
60. The largest
prime needed was p = 401. This took about 375 CPU hours total on a few old
2 GHz machines. For large l the upper bound mmax is small, and sieving is very
quick. (In fact for l ≥ 10 we sieved up to 10100.) The main part of the work are
the pairs (k, l) = (3, 5), (4, 5), where the list has length roughly M 1/5.

On A(k, p)

There is a lot of literature on the size of the image of a polynomial on Fp. For
k = 3 and k = 4 the value of A(k, p) was found by Daublebsky v. Sterneck [6].
One has A(3, p) = (2p ± 1)/3 when p ≡ ±1 (mod 6), and A(4, p) = (3p + 4 +
χ(−1) + 2χ(5) − 2χ(10))/8 for p > 5, where χ is the quadratic character. Birch
& Swinnerton-Dyer [3] showed that ‘general’ polynomials of degree k on Fp have
an image of size akp + O(√p) where ak = ∑k
i=1(−1)
i−1 1
i! . We conjecture in our
situation that the value Ak = limp→∞ A(k,p)
p exists, and equals Ak = ak for odd

3

k, and Ak = ∑k/2
i=1(−1)i−1 1
2ii! for even k. This is true for k ≤ 5. Note that for
even k there is the symmetry f (x) = f (k + 1 − x) explaining the smaller image
size.

3 Near collisions

3.1 Diﬀerence 1

We know about the following examples with d = 1:

n k m l (m
l ) = (n
k) + 1
6 3 7 2 21
7 3 9 2 36
11 2 8 3 56
10 5 23 2 253
12 4 32 2 496
16 3 34 2 561
60 2 23 3 1771
27 3 77 2 2926
29 3 86 2 3655
34 3 21 4 5985
22 5 230 2 26335
260 3 2407 2 2895621
93 4 2417 2 2919736
62 5 3598 2 6471003
28 11 6554 2 21474181
665 3 9879 2 48792381
135 5 26333 2 346700278
139 5 28358 2 402073903
19630 3 1587767 2 1260501229261
160403633 2 425779 3 12864662659597529

The above table is complete for the cases (k, l), (l.k) = (2, 3), (2, 4), (2, 6),
(3, 4), (4, 6) (as one sees by ﬁnding all integral points on the corresponding
elliptic curves), and for (n
k) ≤ 10
30. We conjecture the following

Conjecture 3.1 There are no other near collisions with diﬀerence 1 than those
given above.

and, more generally,

Conjecture 3.2 Given a ﬁxed diﬀerence d, the number of near collisions with
diﬀerence d is ﬁnite.

The latter conjecture can be backed by standard heuristic arguments. The
inﬁnite family of collisions seems like a miracle.
The cases mentioned above correspond to (double covers of) elliptic curves
in cubic Weierstrass form or in quartic form, and can be solved completely using
e.g. Sage [13] or Magma [10]. See [16], Table 1, for the transformations from
the binomial equations to the elliptic equations.

4

3.2 Inﬁnite families

When d is not ﬁxed, there are a few inﬁnite families.
(
12x2 − 12x + 3
3
 ) + (x
2
) = (24x3 − 36x2 + 15x − 1
2
 ) (1)
(
12x2 − 12x + 5
3
 ) + (x
2
) = (24x3 − 36x2 + 21x − 4
2
 ) (2)
(
60x2 − 60x + 15
5
 ) + (
x
2
) = (a
2
) (3)

where a = 3600x5 − 9000x4 + 8700x3 − 4050x2 + 905x − 77,
(
60x2 − 60x + 19
5
 ) + (
x
2
) = (a
2
) (4)

where a = 3600x5 − 9000x4 + 9300x3 − 4950x2 + 1355x − 152,
(
240x2 − 240x + 62
5
 ) + (3x − 1
2
 ) = (a
2
) (5)

where a = 115200x5 − 288000x4 + 288000x3 − 144000x2 + 35995x − 3597,
(
11340x2 + 11340x + 2835
9
 ) + (y
2
) = (a
2
) (6)

where y = 22680x3 + 34020x2 + 17001x + 2831 and a = 4134207084840000x9 +
18603931881780000x8 + 37201301530092000x7 + 43386206573682000x6+
32522432635935900x5 + 16249739546454750x4 + 5411800833695550x3+
1158443736409575x2 + 144626588131776x + 8023467184451,
(
11340x2 + 11340x + 2843
9
 ) + (y
2
) = (a
2
) (7)

where y = 22680x3 + 34020x2 + 17019x + 2840 and a = 4134207084840000x9 +
18603931881780000x8 + 37214425997028000x7 + 43432142207958000x6+
32591336087349900x5 + 16307159089299750x4 + 5440510606648950x3+
1167056670132675x2 + 146062077851076x + 8126002273751.

How does one ﬁnd such identities? In order to get (b
3) + (x
2) = (a
2), where
x is small, one needs 1
3 b(b − 1)(b − 2) = (a − x)(a + x − 1), a product of two
nearly equal numbers. If b = 3e2, then 1
3 b(b − 1)(b − 2) = (e(b − 2))(e(b − 1))
and we can take a − x = e(b − 2), a + x − 1 = e(b − 1) and ﬁnd e = 2x − 1,
b = 3(2x − 1)2, the ﬁrst family. The other families arise in a similar way.
Are there many such identities? Let us say that the quality of an identity(n(x)
k ) + d(x) = (m(x)
l ) is the degree of x in (n(x)
k ) and (m(x)
l ) divided by that in
d(x). Then our identities (1)-(7) have qualities 3, 3, 5, 5, 5, 3, 3. These are the
only identities of quality at least 3 that we know of. Maybe there are no others.
Maybe there is a number α, supposedly ≤ 3, such that there are only ﬁnitely
many identities of quality at least α.
It follows from the existence of the identities (1)-(7) that there are inﬁnitely
many near collisions, even with (m
l ) ≥ d5. Maybe there is a number β, certainly
β > 5, such that there are only ﬁnitely many near collisions with (m
l ) ≥ d
β.

5

References

[1] H.L. Abbott, P. Erd˝os & D. Hanson, On the number of times an integer
occurs as a binomial coeﬃcient, Am. Math. Monthly 81 (1974) 256–261.

[2] `E.T. Avanesov, Solution of a problem on ﬁgurate numbers (Russian), Acta
Arith. 12 (1966) 409–420.

[3] B.J. Birch & H.P.F. Swinnerton-Dyer, Note on a problem of Chowla, Acta
Arith. 5 (1959) 417–423.

[4] B. Brindza, On a special superelliptic equation, Publ. Math. Debrecen 39
(1991) 159–162.

[5] Y. Bugeaud, M. Mignotte, S. Siksek, M. Stoll & S. Tengely, Integral points
on hyperelliptic curves, Algebra and Number Theory 2 (2008) 859–885.

[6] R. Daublebsky v. Sterneck, ¨Uber die Anzahl inkongruenter Werte, die eine
ganze Funktion dritten Grades annimmt, Sitzungsberichte der kaiserlichen
Akademie der Wissenschaften, Wien, Bd. CXVI, Heft V, Abteilung IIa
(1907) 895–904.

[7] G. Faltings, Endlichkeitss¨atze f¨ur abelsche Variet¨aten ¨uber Zahlk¨orpern, In-
vent. Math. 73 (1983) 349–366.

[8] D. Kane, New bounds on the number of representations of T as a binomial
coeﬃcient, Integers 4 (2004) #A07.

[9] D.A. Lind, The quadratic ﬁeld Q (√5
) and a certain diophantine equation,
Fibonacci Quart. 6 (1968) 86–93.

[10] Wieb Bosma, John Cannon & Catherine Playoust, The Magma algebra
system. I. The user language, J. Symbolic Comput. 24 (1997) 235–265.

[11] L.J. Mordell, On the integer solutions of y(y + 1) = x(x + 1)(x + 2), Paciﬁc
J. Math. 13 (1963) 1347–1351.

[12] ´A. Pint´er, A note on the diophantine equation (x
4) = (y
2), Publ. Math.
Debrecen 47 (1995) 411–415.

[13] SageMath, the Sage Mathematics Software System (Version 7.5.1), The
Sage Developers, 2017, http://www.sagemath.org.

[14] D. Singmaster, How often does an integer occur as a binomial coeﬃcient,
Am. Math. Monthly 78 (1971) 385–386.

[15] D. Singmaster, Repeated binomial coeﬃcients and Fibonacci numbers, Fi-
bonacci Quart. 13 (1975) 295–298.

[16] R.J. Stroeker & B.M.M. de Weger, Elliptic binomial Diophantine equations,
Math. Comp. 68 No. 227 (1999) 1257–1281.

[17] R.J. Stroeker & B.M.M. de Weger, Solving elliptic Diophantine equations:
the general cubic case, Acta Arith. 87 (1999) 339–365.

6

[18] C.A. Tovey, Multiple occurrences of binomial coeﬃcients, Fibonacci Quart.
23 (1985) 356–358.

[19] B.M.M. de Weger, A binomial diophantine equation, Quart. J. Math. Ox-
ford Ser. 2 47 (1996]), 221–231.

[20] B.M.M. de Weger, Equal Binomial Coeﬃcients: Some Elementary Consid-
erations, J. Number Th. 63 (1997) 373–386.

7
