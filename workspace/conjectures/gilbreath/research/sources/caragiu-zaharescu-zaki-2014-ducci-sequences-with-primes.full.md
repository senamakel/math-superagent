<!-- source: https://www.fq.math.ca/Papers1/52-1/CaragiuZaharescuZaki.pdf | converted from PDF -->

ON DUCCI SEQUENCES WITH PRIMES

MIHAI CARAGIU, ALEXANDRU ZAHARESCU, AND MOHAMMAD ZAKI

Abstract. We introduce an analogue of the Ducci game that involves d-tuples of prime
numbers subjected to the iteration G sending such a d-tuple (p1, p2, . . . , pd) into (gpf(p1 +
p2), gpf(p2 + p3), . . . , gpf(pd + p1)), where for any x ≥ 1, gpf(x) represents the greatest prime
factor of the integer x. We show that the iteration of G always leads into a limit cycle C.
Moreover, if C has length greater than 1, then not only every vector in C has all components
in P0 := {2, 3, 5, 7}, but every element of P0 appears as a component of some vector in C. An
analysis of the lengths of the nontrivial cycles for small values of d is provided.

1. Introduction

An interesting elementary result going back to at least the 1930’s [15, 19] shows that iterating
the map φ(x1, x2, x3, x4) = (|x1 − x2|, |x2 − x3|, |x3 − x4|, |x4 − x1|) over the integers eventually
leads to the null vector. This generated extensive research and inspired numerous results on
the dynamics induced by the Ducci maps φ : Zd → Zd given by

φ(x0, x1, . . . , xd−1) = (|x0 − x1|, |x1 − x2|, . . . , |xd−1 − x0|).

For example, if d is a power of 2, iterating the above map always leads to the null vector. For
an arbitrary d, it is known that φ leads into limit cycles in which the vectors are essentially
binary (the components of each d-tuple in a cycle being either 0 or some constant c), so that
any investigation into the lengths of the limit cycles of φ [2, 8, 14, 17] would necessarily involve
its binary reduction φd : Fd
2 → Fd
2 given by

φ(u0, u1, . . . , ud−1) = (u0 + u1, u1 + u2, . . . , ud−1 + u0).

Many outstanding problems involve the number of iterations until the null vector is reached
[7, 18], the lengths of the Ducci cycles and the asymptotic growth of the number of cycles with
distinct lengths [8, 14], and generalized Ducci-type mappings incorporating various weights
[14]. Analogues of the integer/binary Ducci problem have been suggested and investigated
in various contexts such as real numbers [6, 16], matrices and multi-dimensional arrays [3],
abelian groups [4, 5], algebraic numbers [13], p-adic integers [9], etc.
In the present paper we will introduce a new analogue of the Ducci problem that involves
prime numbers and the greatest prime factor function. The reason for considering this analogue
lies in a series of intriguing recent results involving the “greatest prime factor sequences” [1, 12].
These are prime sequences {xn}n satisfying a recurrence relation of the form

xn = gpf(a1xn−1 + a2xn−2 + · · · + akxn−k + b), (1)

where ai > 0 and b ≥ 0 are integers, while gpf(x) represents the greatest prime factor of the
positive integer x (with the convention gpf(1) = 1). It was conjectured [1] that all prime
sequences satisfying a recurrence of the form (1) are ultimately periodic. Computational
evidence supports this ultimate periodicity conjecture and special cases have been proved,
such as the case of prime sequences satisfying xn = gpf(axn−1 + b) where a divides b [11, 12],
and the case of the “GPF-Fibonacci” sequences [1] satisfying xn = gpf(xn−1 + xn−2). All

32 VOLUME 52, NUMBER 1

ON DUCCI SEQUENCES WITH PRIMES

GPF-Fibonacci sequences eventually enter the unique limit cycle (3,5,2,7). However, a com-
puter search [1] revealed multiple limit cycles of lengths 100, 212, 28 and 6 for the “GPF-
Tribonacci” sequences, satisfying

xn = gpf(xn−1 + xn−2 + xn−3).

We considered this was enough to warrant a consideration of a “GPF-Ducci” analogue of
the classical Ducci game. The recursion is amazingly simple, to transform a ﬁnite sequence of
primes we simply take the greatest prime factor of the sums of nearest neighbors. For example,
the vector v0 = (5, 103, 7, 23) will be transformed into

v1 = (3, 11, 5, 7),

since 3 is the greatest prime factor of 5+103, 11 is the greatest prime factor of 103+7, 5 is the
greatest prime factor of 7+23, and ﬁnally 7 is the greatest prime factor of 23+5 (note that we
assume periodic boundary conditions for the vectors involved in the process). If we continue
the iteration we will get v2 = (7, 2, 3, 5), v3 = (3, 5, 2, 3), v4 = (2, 7, 5, 3), v5 = (3, 3, 2, 5),
v6 = (3, 5, 7, 2), v7 = (2, 3, 3, 5), v8 = (5, 3, 2, 7), v9 = (2, 5, 3, 3), while v10 = (7, 2, 3, 5) = v2
signals the entrance into a limit cycle of length 8, with the set of components of the vectors
in the limit cycle being precisely the set of the ﬁrst four primes, {2, 3, 5, 7}. In the present
paper we will prove that this is not accidental: indeed, for every vector size, the “GPF-Ducci”
iteration ultimately enters a limit cycle with all vector components in {2, 3, 5, 7}. Conversely,
every element of {2, 3, 5, 7} appears in one of the vectors in the limit cycle. This establishes
an interesting new analogue of the classical Ducci process. Moreover, a detailed cycle length
analysis for vector lengths 3 through 8 will be obtained through exhaustive computer search.

2. The GPF-Ducci Recursion

Let P be the set of all primes, and let d ≥ 2 be an integer. Our ‘GPF-Ducci’ map

G : P d → P d

will be deﬁned by

G(p1, p2, . . . , pd) = (gpf(p1 + p2), gpf(p2 + p3), . . . , gpf(pd + p1)) (2)

for every (p1, . . . , pd) ∈ Pd. Let P0 := {2, 3, 5, 7}. The main results that will be proved in the
present paper are summarized as follows:
• The iteration of G always leads into a limit cycle C.
• If C has length greater than 1, every vector in C has all components in P0.
• If C has length greater than 1, then every element of P0 is the component of some
vector appearing in C.
The iterations of the GPF-Ducci mapping (2) provide us with a new variation on the Ducci
theme, which gives an additional ‘arithmetic touch’ to the Ducci problem. The following
elementary result may be thought of as an analogue of the classical result of ultimate periodicity
of the Ducci game. It provides a quick argument that all GPF-Ducci iterations ultimately enter
a cycle, though without providing any details on the cycle structure.

Proposition 1. Every ‘GPF-Ducci’ iteration is ultimately periodic.

Proof. Let (p1, . . . , pd) be the initial prime d-tuple and let p be a prime such that p ≡ 1 (mod 3)
and such that p ≥ max(p1, . . . , pd). One can easily see that the set Kp := {r|r prime, r ≤ p}
is closed under the binary operation (r, s) ↦→ gpf (r + s). Thus, it follows that the components

FEBRUARY 2014 33

THE FIBONACCI QUARTERLY

of all d-tuples generated by the GPF-Ducci iteration starting from (p1, . . . , pd) are bounded
from above by p, which has ultimate periodicity as an immediate consequence, which proves
the proposition. □

For more algebraic properties of the greatest prime factor operation

(r, s) ↦→ gpf(r + s) (3)

deﬁned on the set of primes, with applications to sequences, we refer to [1] and [10]. Charac-
terizing the cycle structure of the GPF-Ducci iteration is an interesting problem. Note that
a cycle of length 1 must consist of a constant d-tuple (p, p, . . . , p). If d is even, for example,
every d-tuple of the form (p, q, p, q, . . . , p, q) has the property of being mapped into a cycle of
length 1 (however, it is possible to ﬁnd diﬀerent kinds of d-tuples with this property, as shown
by the (5, 17, 71, 61) 4-tuple). Computational evidence suggested to us a nice result that will
be proved in Theorem 1 below: namely, all limit cycles of the GPF-Ducci iteration of lengths
greater than 1 contain only vectors with components belonging to P0 – which is itself closed
under (3).
Since every sequence of ‘GPF-Ducci’ iterates is ultimately periodic, for every “seed” X =
(p1, . . . , pd) ∈ P d, there exist L = LX and n0 = nX such that for all n ≥ n0, Gn+L(X) =
Gn(X). Our main result might be thought of as a quaternary analogue of the classical result
on the binary character of the vectors in a limit cycle of the classical Ducci iteration.

Theorem 2. Let X ∈ P d with LX > 1. Then for all n ≥ nX the components of Gn(X) belong
to P0. Moreover, each element of P0 appears in Gn(X) for some n ≥ nX.

A complete computational veriﬁcation of Theorem 2 for small dimensions (d ≤ 8) is detailed
in the last section of the paper.

3. Proof of the Main Result

For any k with 1 ≤ k ≤ L = LX, let us denote

G
n0+k−1(X) := (pk,1, . . . , pk,d).

Let A be the L×d matrix in which the kth row is Gn0+k−1(X). Since L > 1, then (p1,1, . . . , p1,d)
is not a constant vector. The cycle C of the GPF-Ducci iteration thus consists of the rows of
the matrix A.

Proof of Theorem 2. The proof of our main result will be a direct consequence of the following
set of four lemmas.

Lemma 1. Let q be the largest entry in the matrix A. Then q is odd, and if the primes
a and b are consecutive entries in a row of A producing q = gpf(a + b) in the immediately
following row, one of the following holds true: (i) a = b = q, or (ii) q − 2 is a prime and either
(a, b) = (2, q − 2) or (a, b) = (q − 2, 2).

Proof. Indeed q is odd, since if q = 2 then LX = 1, in contradiction with the assumption of
Theorem 2. Assume that (i) is not true, that is either a ̸= q, or b ̸= q. If a ̸= q and b = q, then
gpf(a + b) ̸= q (otherwise q will divide a), which is a contradiction. Similarly we rule out the
possibility of b ̸= q and a = q. Also, the case in which both a and b are odd primes not equal
to q may be ruled out, since then gpf(a + b) ≤ a+b
2 < q. Therefore either a = 2, or b = 2. If
a = 2 then b must be an odd prime. If 2 + b is not a prime, then gpf(a + b) < 2 + b ≤ q, which
contradicts the assumption gpf(a + b) = q. Therefore 2 + b is a prime, in which case a = 2

34 VOLUME 52, NUMBER 1

ON DUCCI SEQUENCES WITH PRIMES

and b = q − 2 is a prime. A similar argument may be made in the case b = 2, in which case it
will follow that a = q − 2 is prime. Thus we proved that (ii) holds true. □

Lemma 2. Let p := q − 2. Then p must occur in A.

Proof. Indeed, from Lemma 1, if p does not appear in the matrix A then q appears in a row
exactly when there are consecutive occurrences of q in the previous row. Since q does appear
in A, and since the cycle matrix A is subjected to periodic boundary conditions, q must appear
in each row of A. If p is not an element of A, applying G to any row of A produces a strictly
smaller number of q’s in the next row. However, the cyclic structure of A makes this impossible
(the function “number of q’s in the nth row” would be periodic and strictly decreasing). □

Lemma 3. The largest entry q of the limit cycle matrix A satisﬁes q ≤ 7.

Proof. Assume on the contrary that q ≥ 11. Then p is odd and p − 2 = q − 4 is not a prime.
Let the primes a and b be two neighboring entries in a row of A such that in the next row they
will generate gpf(a + b) = p. We will show that both a and b must be equal to p by showing
that all other options will lead to gpf(a + b) ̸= p.
(i) Let a ̸= p and b = p. Then gpf(a+b) ̸= p (otherwise p will divide the prime a). Similarly,
gpf(a + b) ̸= p follows in the case a = p and b ̸= p.
(ii) Let a and b be both odd and not equal to p. If a < p and b < p, then a + b is even
and gpf(a + b) ≤ a+b
2 < p, so gpf(a + b) ̸= p. If a > p and b > p, then a = b = q, and so
gpf(a + b) ̸= p. If a < p and b > p, then b = q and a < p − 2 (since p − 2 is not a prime), in
which case gpf(a + b) ≤ a+b
2 < p−2+q
2 = p. The symmetric case b < p and a > p may be dealt
with in a similar way.
(iii) If a = b = 2, then gpf(a + b) = 2 ̸= p (p is odd).
(iv) Let a = 2 and b an odd prime. Since p − 2 is not a prime, b ̸= p − 2 and so p ̸= b + 2.
Thus, if 2 + b is a prime, gpf(a + b) = 2 + b ̸= p, while if 2 + b is not a prime, then gpf(a + b) ≤
2+b
3 ≤ 2+q
3 = 2+p+2
3 = 4+p
3 < p, and hence, gpf(a + b) ̸= p.
We conclude that if gpf(a + b) = p, then both a and b must equal p. That is, p appears in
a row exactly when there are consecutive occurrences of p in the previous row. Since p does
appear in A by Lemma 2, and due to the cyclic structure of A, it follows that p must appear
in each row of A. Since p − 2 does not appear in the matrix A, applying G to any row of A
produces a strictly smaller number of p’s in the next row. Thus, the number of occurrences of
p strictly decreases in the subsequent rows. As in the proof of Lemma 2, the cyclic structure
of A makes this impossible. Therefore, q ≤ 7 (so that every entry in the cycle matrix A is
either 2, 3, 5, or 7). This completes the proof Lemma 3. □

Note that Lemma 3 may be restated as follows: for all n ≥ nX we have Gn(X) ∈ P d
0 .

Lemma 4. Each one of the primes 2, 3, 5, and 7 is an entry of the matrix A.

Proof. First, we show that if 3 appears in some row of A, then 5 must appear in A. Indeed,
if 3 appears in a row of A, then that row has entries other than 3 (recall that L > 1). If there
is a 5 in the row, then we are done. If either 3 and 7, or 3 and 2 appear as nearest neighbors
in the row, then 5 will appear in the next row.
Next, we show that if 7 appears in some row of A, then 3 must appear in A. Indeed, if 7
appears in a row of A, since L > 1, then that row has entries other than 7. If there is a 3 in
this row, then we are done. If either 7 and 5, or 7 and 2 appear as nearest neighbors in this
row, then 3 will appear in the next row. Therefore, if 7 appears in some row of A, then 5 and
3 must appear in A.

FEBRUARY 2014 35

THE FIBONACCI QUARTERLY

We are now going to show that if 7, 5 and 3 appear in A, then 2 must appear too: for this it
will be enough to show that 3 and 5 appear as nearest neighbors in some row of A. Consider
a row of A containing a 3, and assume that 2 is not in this row (otherwise there is nothing to
prove). If 5 does not appear next to 3, then that row must contain one of the segments 3 3 7,
7 3 3, 7 3 7. From the ﬁrst two segments we get either 3 5 or 5 3 in the next row. From the
segment 7 3 7 we get 5 5 in the next row. Thus we either get 5 5 7 or 7 5 5 if there is no 3
next to 5 in A. But then in the subsequent row we do get 5 3 or 3 5. Therefore if 7 appears
in some row of A, then all three numbers 5, 3 and 2 must appear in A. The proof of Lemma
4 (and hence of Theorem 1) will be completed if we prove that 7 appears in A.
Suppose 7 does not appear in A. Then 2 and 5 can’t appear next to each other in a row,
since 7 will be immediately generated in the next row. If 2 and 5 appear in a row separated
by 3’s, then it is easy to see that a repeated application of G to the particular segment of the
form “2 3 3 . . . 3 5” or “5 3 3 . . . 3 2” ultimately produces a 7. Therefore we cannot have 2
and 5 in the same row. If a (necessarily non-constant) row consists of 3’s and 5’s, then 3 and
5 must appear next to each other somewhere in that row. Then, since 7 is not an entry of A,
a segment of the form 3 5 or 5 3 may only be produced, via G, from a segment of the form
3 3 2 or 2 3 3 in the previous row, which at its turn may only be a subsegment of either
one out of 3 3 2 2, 3 3 2 3, 2 2 3 3, or 3 2 3 3 in the same row. In the ﬁrst and third
case we get 2 and 5 after applying G once. In the second and fourth case we get 2 and 5 after
applying G twice. Hence, 3 and 5 can’t appear in the same row. Lastly, the possibility of a
non-constant row consisting of 2 and 3 only may be ruled out, since that would imply that the
previous row contains both 3 and 5 (only the segments 3 5 and 5 3 may generate a 2 via G).
To summarize, if 7 does not appear in A (i.e., each entry of A is either 2, 3 or 5) and if
L > 1, we proved that 2 and 5 cannot appear in the same row, and yet there is no row of
A consisting of 3 and 5 only, and no row of A consisting of 2 and 3 only. This contradiction
shows that if L > 1 then 7 must appear in A. This concludes the proof of Lemma 4, and
hence, together with the previous three Lemmas, of Theorem 2. □

4. Cycle Length Analysis: Computational Results

As a consequence of Theorem 2, in a computer-assisted search for the lengths of the non-
trivial cycles of the GPF-Ducci map G on Pd, we may restrict the search to the iterates of
the 4d initial vectors X ∈ P d
0 (with the understanding that other trivial cycles, or limit cycles
of length 1, may be obtained for other choices of X) In our analysis of the distribution of
the limit cycle lengths corresponding to the 4d values of X ∈ P d
0 we obtained the following
numerical results for 3 ≤ d ≤ 8.

• Out of 64 possible seeds X ∈ P 3
0 , G leads 4 times into a limit cycle of length 1 and 60
times into a limit cycle of length 12;
• Out of 256 possible seeds X ∈ P 4
0 , G leads 232 times into a limit cycle of length 1, 4
times into a limit cycle of length 2, 4 times into a limit cycle of length 4, and 16 times
into a limit cycle of length 8;
• Out of 1024 possible seeds X ∈ P 5
0 , G leads 4 times into a limit cycle of length 1, 70
times into a limit cycle of length 20, 120 times into a limit cycle of length 30, and 830
times into a limit cycle of length 40;
• Out of 4096 possible seeds X ∈ P 6
0 , G leads 1204 times into a limit cycle of length 1,
1428 times into a limit cycle of length 6, 1116 times into a limit cycle of length 12, 174
times into a limit cycle of length 27, and 174 times into a limit cycle of length 54;

36 VOLUME 52, NUMBER 1

ON DUCCI SEQUENCES WITH PRIMES

• Out of 16384 possible seeds X ∈ P 7
0 , G leads 4 times into a limit cycle of length 1,
196 times into a limit cycle of length 4, 196 times into a limit cycle of length 28, 3528
times into a limit cycle of length 126, and 12460 times into a limit cycle of length 168;
• Out of 65536 possible seeds X ∈ P 8
0 , G leads 19528 times into a limit cycle of length
1, 4 times into a limit cycle of length 2, 4 times into a limit cycle of length 4, 12496
times into a limit cycle of length 8, 14808 times into a limit cycle of length 16, 14816
times into a limit cycle of length 32, 240 times into a limit cycle of length 48, and 3640
times into a limit cycle of length 80.
The next computer-generated supporting data provides explicit examples of choices of the
initial vector X ∈ P d
0 producing a non-trivial cycle of a given length LX:
• For d = 3, LX = 12 for X = (2, 3, 5);
• For d = 4, LX = 2 for X = (2, 7, 3, 5), LX = 4 for X = (5, 3, 7, 2), and LX = 8 for
X = (7, 2, 3, 5);
• For d = 5, LX = 20 for X = (5, 3, 3, 7, 7), LX = 30 for X = (5, 7, 2, 5, 5), and LX = 40
for X = (7, 2, 5, 7, 7);
• For d = 6, LX = 6 for X = (2, 5, 3, 5, 3, 3), LX = 12 for X = (5, 2, 3, 5, 2, 2), LX = 27
for X = (5, 7, 3, 2, 7, 3), and LX = 54 for X = (3, 3, 7, 2, 5, 2);
• For d = 7, LX = 4 for X = (5, 7, 3, 3, 3, 7, 7), LX = 28 for X = (7, 7, 7, 5, 7, 5, 5),
LX = 126 for X = (3, 5, 7, 7, 7, 5, 7), and LX = 168 for X = (5, 3, 2, 2, 7, 3, 2);
• For d = 8, LX = 2 for X = (2, 7, 3, 5, 2, 7, 3, 5), LX = 4 for X = (2, 5, 3, 7, 2, 5, 3, 7),
LX = 8 for X = (3, 5, 2, 7, 7, 3, 7, 5), LX = 16 for X = (7, 5, 5, 5, 7, 3, 5, 3), LX = 32
for X = (5, 7, 7, 7, 3, 7, 2, 3), LX = 48 for X = (3, 7, 3, 7, 7, 3, 2, 5), and LX = 80 for
X = (7, 5, 5, 7, 5, 2, 3, 3).
As an interesting fact, the distribution of cycle lengths starting from seeds X ∈ P d
0 appears
to be tilted, for even values of d, towards smaller cycle lengths, and for odd values of d towards
the larger cycle lengths. The problem of cycle lengths for various values of d (analyzed in the
case of the classical Ducci game [8]) presents itself to be a promising combinatorial number
theory problem.
 5. Acknowledgment

We would like to thank the anonymous reviewer for the helpful and constructive comments.

References

[1] G. Back and M. Caragiu, The greatest prime factor and recurrent sequences, The Fibonacci Quarterly,
48.4 (2010), 358–362.
[2] F. Breuer, E. Lotter, and B. van der Merwe, Ducci-sequences and cyclotomic polynomials, Finite Fields
Appl., 13.2 (2007), 293–304.
[3] F. Breuer, Ducci sequences in higher dimensions, Integers: Electronic Journal of Combinatorial Number
Theory, 7 (2007), A24.
[4] F. Breuer, Ducci sequences over abelian groups, Communications in Algebra, 27.12 (1999), 5999–6013.
[5] F. Breuer, Ducci sequences and cyclotomic ﬁelds, Journal of Diﬀerence Equations and Applications, 16.7
(2010), 847–862.
[6] R. Brown and J. L. Merzel, Limiting behavior in Ducci sequences, Period. Math. Hungar., 47.1-2 (2003),
45–50.
[7] R. Brown and J. L. Merzel, The length of Ducci’s four-number game, Rocky Mountain J. Math., 37.1
(2007), 45–65.
[8] N. J. Calkin, J. G. Stevens, and D. M. Thomas, A characterization for the length of cycles of the N-number
game, The Fibonacci Quarterly, 43.1 (2005), 53–59.

FEBRUARY 2014 37

THE FIBONACCI QUARTERLY

[9] M. Caragiu and N. Baxter, A note on p-adic Ducci games, JP J. Algebra Number Theory Appl., 8.1
(2007), 115–120.
[10] M. Caragiu and G. Back, The greatest prime factor and related magmas, JP J. Algebra Number Theory
Appl., 15.2 (2007), 127–136.
[11] M. Caragiu and L. Scheckelhoﬀ, The greatest prime factor and related sequences, JP J. Algebra Number
Theory Appl., 6.2 (2006), 403–409.
[12] M. Caragiu, Recurrences based on the greatest prime factor function, JP J. Algebra Number Theory Appl.,
19.2 (2010), 155–163.
[13] M. Caragiu, A. Zaharescu and M. Zaki, On Ducci sequences with algebraic numbers, The Fibonacci
Quarterly, 49.1 (2011), 34–40.
[14] M. Chamberland and D. M. Thomas, The N-number Ducci game, J. Diﬀerence Equations and Applica-
tions, 10.3 (2004), 339–342.
[15] C. Ciamberlini and A. Marengoni, Su una interessante curiosita numerica, Periodiche di Matematiche,
Ser. 4, 17 (1937), 25–30.
[16] C. I. Cobeli, M. Crˆa¸smaru, and A. Zaharescu, A cellular automaton on a torus, Portugal. Math., 57.3
(2000), 311–323.
[17] A. Ehrlich, Periods in Ducci’s n-number game of diﬀerences, The Fibonacci Quarterly, 28.4 (1990),
302–305.
[18] W. A. Webb, The length of the four-number game, The Fibonacci Quarterly, 20.1 (1982), 33–35.
[19] F.-B. Wong, Ducci processses, The Fibonacci Quarterly, 20.2 (1982), 97–105.

MSC2010: 11B37, 11A41, 11B83

Department of Mathematics and Statistics, Ohio Northern University, Ada, Ohio 45810
E-mail address: m-caragiu.1@onu.edu

Institute of Mathematics of the Romanian Academy, PO Box 1-764, Bucharest 014700, Ro-
mania, and Department of Mathematics, University of Illinois at Urbana-Champaign, 1409 W.
Green Street, Urbana, IL, 61801
E-mail address: zaharesc@math.uiuc.edu

Department of Mathematics and Statistics, Ohio Northern University, Ada, Ohio 45810
E-mail address: m-zaki@onu.edu

38 VOLUME 52, NUMBER 1
