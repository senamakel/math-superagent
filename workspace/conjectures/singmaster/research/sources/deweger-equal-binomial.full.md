<!-- source: https://math.deweger.net/papers/%5B20%5DdW-EqBinom-JNumTh%5B1997%5D.pdf | converted from PDF -->

File: 641J 210901 . By:DS . Date:02:04:97 . Time:13:23 LOP8M. V8.0. Page 01:01
Codes: 3368 Signs: 1456 . Length: 50 pic 3 pts, 212 mm

Journal of Number Theory  NT2109

journal of number theory 63, 373386 (1997)

Equal Binomial Coefficients: Some Elementary
Considerations

Benjamin M. M. de Weger*

Department of Mathematics, University of Leiden; and Econometric Institute,
Erasmus University Rotterdam, P.O. Box 1738, 3000 DR Rotterdam, The Netherlands

Received April 16, 1996; revised August 5, 1996

1. INTRODUCTION

In the Pascal Triangle, consisting of the binomial coefficients ( n
k) for
n=0, 1,2,. . . and 0˛k˛n, one encounters each natural number (with the
exception of 2) at least twice, and many numbers more than twice. There
are three well-known relations that account for this, namely

\n
k+=\ n
n&k+, \n
0+=1, \n
1+=n

for n=1, 2, ..., 0˛k˛n. Notice that the third relation above implies

\( n
k)
1 +=\n
k+ ,

so that there are infinitely many numbers occurring at least 4 times in the
Pascal Triangle.
Stripped of these trivialities, the more interesting problem becomes to
determine the natural numbers that occur at least twice as binomial coef-
ficients of the shape ( n
k) with 2˛k˛ 1
2 n, and this is yet unsolved in its
full generality. The only nontrivial solutions known at this time are the
following:

article no. NT972109
 373 0022-314X97 ˚25.00

Copyright  1997 by Academic Press
All rights of reproduction in any form reserved.

* This research was supported by the Netherlands Mathematical Research Foundation
SWON with financial aid from the Netherlands Organization for Scientific Research NWO.
E-mail: dewegerfew.eur.nl.

File: 641J 210902 . By:DS . Date:02:04:97 . Time:13:23 LOP8M. V8.0. Page 01:01
Codes: 2566 Signs: 1769 . Length: 45 pic 0 pts, 190 mm

\
16
2 +
=\
10
3 +
=120, \
21
2 +
=\
10
4 +
=210,

\
56
2 +
=\
22
3 +
=1540, \
120
2 +
=\
36
3 +
=7140,

\
153
2 +
=\
19
5 +
=11628, \
221
2 +
=\
17
8 +
=24310,

\
78
2 +
=\
15
5 +
=\
14
6 +
=3003,

and an infinite family:

\
F2i+2 F2i +3
F2i F2i+3 +
=\
F2i+2 F2i +3&1
F2i F2i +3+1 + for i=1, 2, ...,

where Fn is the n th Fibonacci number (defined by F0=0, F1=1, and
Fn +1=Fn+Fn &1 for n=1, 2, . . .). This infinite family is due to D. A. Lind
[L] and D. Singmaster [Sin2].
There are no other nontrivial solutions of ( n
k)=( m
l ) with ( n
k)˛1030 or
max[n, m]˛1000, as we could show without difficulties in a few hours on
a personal computer. Notice that D. Singmaster [Sin2] searched up to
248r 2.8_1014. We did this computer search as follows. To start with, all
solutions to ( n
k)=( m
l ) with max[k, l]˛4, are known, see below. Next, we
made a list of all ( n
k)˛1030 with 5˛k˛ 1
2 n, and sorted this list. Thus
numbers occurring twice in the list are easily found. Next, for each member
of the list we checked whether they were of the form ( m
l ) for l=2,3,4
(which was the most time-consuming step). All these computations were
done in exact (i.e. 30 digit) arithmetic. Finally, we made a list of all
( n
k)>1030 with max[n, m]˛1000 in 8 digit precision only, sorted this list,
and checked for pairs being close enough.
Let N(a) be the number of occurrences of a as a binomial coefficient.
Then N(1)=˜, N(2)=1, and clearly 2˛N(a)<˜ for all a˚3.
D. Singmaster [Sin1] proved that N(a)=O(log a), and conjectured that
N(a)=O(1). Later [Sin2] he even conjectured that N(a)˛10 for all a˚2.
H. L. Abbott, P. Erdo˘ s and D. Hanson [AEH] showed that the average
and normal order of N(a) is 2, and that N(a)=O(log alog log a). Maybe
even the following is (too good to be) true.

Conjecture A. The equation ( n
k)=( m
l ) has no nontrivial solutions but
those given above.

374 BENJAMIN M. M. DE WEGER

File: 641J 210903 . By:DS . Date:02:04:97 . Time:13:23 LOP8M. V8.0. Page 01:01
Codes: 2837 Signs: 2228 . Length: 45 pic 0 pts, 190 mm

This conjecture would imply N(a)˛8 for all a˚2, and N(a)˛6 for all
a˚2 with the exception of a=3003, where the upper bound N(a)=6 is
attained infinitely often.
In this note we will contribute a little bit to the knowledge on this
conjecture, and show that the special case ( n
3)=( m
4 ) has essentially been
settled over 30 years ago by L. J. Mordell, without anybody having realized
this (so it seems). The special cases ( n
2)=( m
3 ) and ( n
2)=( m
4 ) have been settled
before, but by much more complicated methods than we (and Mordell)
need. Further, we will also prove a partial result on rational solutions of
( n
3)=( m
4 ). We restrict ourselves entirely to elementary methods; i.e., the
deepest mathematics we require are only the first essentials of algebraic
number theory.
 2. INTEGRAL SOLUTIONS

In the context of diophantine equations, it's a bit more natural to study
the equation ( n
k)=( m
l ) for the extended definition of ( n
k) to all n, k # Z with
k˚0, as follows: \
n
k+
=n(n&1) }}} (n&k+1)
k! .

In this more general sense (and, by the way, also in the restricted sense),
for fixed k, l (with k<l) the equation ( n
k)=( m
l ) has been completely solved
in two cases only, namely the case (k, l)=(2, 3) by E . T. Avanesov [Av]
using Skolem's method, and the case (k, l )=(2, 4), after Richard K. Guy
had drawn attention to the problem in Section D3 of [G], by the present
author [dW] and independently by A kos Pinte r [Pi], both using the
GelfondBaker method.
It is the first purpose of this note to show that the case (k, l)=(3, 4) is
comparatively easy, as it is an almost trivial consequence of the result of
L. J. Mordell [M1], which itself has a more or less elementary proof. In
this paper, Mordell determines the products of 2 consecutive integers that
are equal to products of 3 consecutive integers. It is quite remarkable that
this connection between Mordell's well known result and our binomial
diophantine equation seems to have been unnoticed for over 30 years.
So here's our first main theorem, which might come as a disappointment
to the reader expecting nontrivialities.

Theorem1. The only solutions n, m # Z to ( n
3)=( m
4 ) are the following
trivial ones:

(n, m)# [0, 1, 2]_[0, 1, 2, 3],(n, m)=(3, 4), (3, &1), (7, 7), (7, &4).

375EQUAL BINOMIAL COEFFICIENTS

File: 641J 210904 . By:DS . Date:02:04:97 . Time:13:23 LOP8M. V8.0. Page 01:01
Codes: 2502 Signs: 1640 . Length: 45 pic 0 pts, 190 mm

Proof. Write out the equation ( n
3)=( m
4 )as

1
6 n(n&1)(n&2)= 1
24 m(m&1)(m&2)(m&3).

Suggested by symmetry we put

X=n&1, Y= 1
2 m(m&3),

and then we obtain the equation

Y 2+Y=X 3&X.

In other words, we are looking for products Y(Y+1) of two consecutive
integers being equal to products (X&1) X(X+1) of three consecutive
integers. Mordell's Theorem 2 below gives us all the solutions for (X, Y),
which are easily traced back to the trivial solutions for (n, m) given above.
This completes the proof. K

Theorem 2 (Mordell, 1963). The only solutions in X, Y # Z to the equation

Y 2+Y=X 3&X

are the following 10:

(X, Y)# [ &1,0,1]_[ &1, 0],(X, Y)=(2, 2), (2, &3), (6, 14), (6, &15).

Theorem 2 was proved in an elementary way by L. J. Mordell [M1]
in 1963 (see also Theorem 2 in Chapter 27 of his book [M2]). By
``elementary'' we mean that the deepest results that are used are the explicit
knowledge of a class group and generators of a unit group in a certain
cubic number field. For a different approach, that seems to be more
complicated, see Exercise 9.13 of J. H. Silverman's book [Sil]. We mention
that a third line of proof (using much more machinery, both theoretical
and computational) is made possible by the recent method of elliptic
logarithms, developed independently by R. J. Stroeker and N. Tzanakis
[ST], by J. Gebel, A. Petho˘ and H. G. Zimmer [GPZ], and by N. P. Smart
[Sm]. Below we will return to Mordell's proof.

3. RATIONAL SOLUTIONS

Note that we can even extend the definition of ( n
k) further, to n # Q (of
course we can just as well take n # R, or even n # C, but we do not want
to leave the area of number theory). When we want to study the equation

376 BENJAMIN M. M. DE WEGER

File: 641J 210905 . By:DS . Date:02:04:97 . Time:13:23 LOP8M. V8.0. Page 01:01
Codes: 3143 Signs: 2629 . Length: 45 pic 0 pts, 190 mm

( n
k)=( m
l ) for fixed k, l in this context, we enter the domain of arithmetic
algebraic geometry.
In the case (k, l)=(2, 3) the equation ( n
2)=( m
3 ) is a Weierstra? equation
of an elliptic curve. This curve has trivial torsion, and rank 2, and the
group of rational points is generated by (n, m)=(1, 0) and (n, m)=(1, 1).
Now, using the addition law on the elliptic curve, one can start producing
the infinitely many rational solutions. In other words, the set of solutions
n, m # Q of ( n
2)=( m
3 ) is infinite, but well understood.
In the case (k, l)=(2, 4) the equation ( n
2)=( m
4 ) also is an equation of an
elliptic curve. This curve has a torsion group of order 2, generated by
(n, m)=(0, 1), and the free part of the group of rational points is of
rank 2, and is generated by (n, m)=(0, 0) and (n, m)=(1, 1). Thus again
the set of solutions n, m # Q of ( n
2)=( m
4 ) is infinite, but well understood.
In the case (k, l)=(3, 4) things are different, because the algebraic curve
defined by the equation ( n
3)=( m
4 ) has genus 3, and thus, by Faltings's work
[F], has only finitely many rational points. It is notoriously difficult to
solve such problems of explicit determination of rational or integral
points on curves of genus >1. That we succeeded above in proving our
Theorem 1 on the integral points on our curve ( n
3)=( m
4 ), is due to the
remarkable fact that this curve is (in geometric language) a double cover
of an elliptic curve, namely the one given by Mordell's equation Y 2+Y=
X 3&X (this is just a reformulation of our proof of Theorem 1 above). The
rational points on this elliptic curve are again not too difficult to describe,
in fact, that's what Silverman uses in his Exercise 9.13 referred to above.
The curve has trivial torsion, rank 1, and the group of rational points is
generated by (X, Y )=(0, 0).
It is an interesting challenge to find out, e.g. on the basis of the facts
mentioned above, what can be said about the set of rational points on the
curve ( n
3)=( m
4 ). With Apecs we searched for solutions coming from the
rational points N } (0, 0) on the elliptic curve Y 2+Y=X 3&X, for |N|˛50
only (but note that the numerator and denominator of the second coor-
dinate of 50 } (0, 0) are already numbers of about 85 digits). So we feel safe
to formulate the following guess.

Conjecture B. The only solutions n, m # Q to ( n
3)=( m
4 ), besides the
integral ones given in Theorem 1 above, are

(n, m)=( 5
4 , 1
2), ( 5
4 , 5
2).

It is the second theme of this note to extend Mordell's elementary proof
of Theorem 2 [M1] to make a first step towards the solution of this
problem. Our extension concerns so-called S-integral solutions, i.e. rational

377EQUAL BINOMIAL COEFFICIENTS

File: 641J 210906 . By:DS . Date:02:04:97 . Time:13:23 LOP8M. V8.0. Page 01:01
Codes: 2190 Signs: 1369 . Length: 45 pic 0 pts, 190 mm

solutions of which the denominators have prime divisors from a fixed finite
set of primes only. We now restrict ourselves to the set consisting of the
prime 2. Thus we have the following result.

Theorem3. The only solutions n, m # Q of which the denominators are
powers of 2 to the equation ( n
3)=( m
4 ), are the ones given in Conjecture B
above.

Note that this result extends Theorem 1. Following the above proof of
Theorem 1, it is clear that Theorem 3 is a consequence of the following
result, which is an analogous extension to the S-integral case of Mordell's
Theorem 2.

Theorem4. The only solutions X, Y # Q of which the denominators are
powers of 2 to the equation Y 2+Y=X 3&X, besides the integral ones given
in Theorem 2 above, are

(X, Y)=\
1
4 , &5
8 +
, \
1
4 , &3
8 +
, \
161
16 , &2065
64 +
, \
161
16 , 2001
64 +
.

4. PROOF OF THEOREM 4

We will now prove Theorem 4, partly following, and partly extending
the line of argument in Mordell's original proof of Theorem 2 [M1]. Note
that our proof is completely elementary.

Proof of Theorem 4. We see at once that there is an integer k˚0, and
integers X1 , Y1 such that
 X= X1
22k , Y= Y1
23k .

Then the equation Y 2+Y=X 3&X leads to

Y 2
1+23kY1=X 3
1&24kX1 .

The idea is to complete the square in the left hand side of the equation,
and then factor both sides in the ring of integers of an appropriate number
field. For convenience we put

U=2X1 , V=2Y1+23k,

378 BENJAMIN M. M. DE WEGER

File: 641J 210907 . By:DS . Date:02:04:97 . Time:13:23 LOP8M. V8.0. Page 01:01
Codes: 2542 Signs: 1446 . Length: 45 pic 0 pts, 190 mm

and so obtain the equation

2V 2=U 3&24k +2U+26k +1,(1)

in which the left hand side has the obvious factorization 2_V_V over Z.
Let % be any root of the polynomial u3&4u+2. Then the right hand side
of equation (1) factors over the ring of integers OK of the cubic number
field K=Q(%)as

U 3&24k +2U+26k+1=(U&% 22k)(U 2+% 22kU+(&4+%2)24k).

The following facts of the field K are well known: the field discriminant
is 148=22 37, a Z-basis for the ring integers OK is [1, %, %2], the class
group is trivial, and the free part of the unit group of OK is generated by

=1=&1+%, =2=1&2%&%2.

Further we have the following factorizations into prime ideals:

(2)=(%)3,(&4+3%2)=(%)2 (1+%+%2),

and we have

N=1=N=2=1, N%=&2, N(1+%+%2)=37.

Note that Mordell [M1] uses &= 2
1 =2=2%&1 instead of =2 as second
fundamental unit, and 4%&3==1(1+%+%2) instead of 1+%+%2.
Let $ be the squarefree part of U&% 22k. If a prime element ? # OK
divides $, it divides 2 or V 2. In the latter case even ?2 divides 2V 2, and
because $ is squarefree, ? must divide the other factor of the right hand
side of (1), U 2+% 22kU+(&4+%2)24k, too. But then ? will divide any
linear combination of U&% 22k and U 2+% 22kU+(&4+%2)24k,in
particular it will divide

(U 2+% 22kU+(&4+%2)24k)&(U+% 22k +1)(U&% 22k)=(&4+3%2)24k.

In view of the above prime factorizations this leaves for ? only the
possibilities % and 1+%+%2, up to units.
Hence we can write
 U&% 22k=$_a square. (2)

where
 $=(&1)a = b
1 = c
2 %d (1+%+%2) e
 379EQUAL BINOMIAL COEFFICIENTS

File: 641J 210908 . By:DS . Date:02:04:97 . Time:13:23 LOP8M. V8.0. Page 01:01
Codes: 2709 Signs: 1512 . Length: 45 pic 0 pts, 190 mm

for some a, b, c, d, e # [0, 1], and the square is an algebraic integer, i.e. an
element of OK . For the norm of $ we have on the one hand

N$=(&1)a + d 2d37e,

and on the other hand, by (1), it differs by a rational integral square factor
from
 N(U&% 22k)=U 3&24k +2U+26k +1=2V 2.

It follows that a=d=1 and e=0. This leaves us four possibilities for $,
namely
 $ # [ &=1 %,&= 1 =2 %,&%,&=2 %].

At this point, to show that two of these four cases do not admit solutions,
we use an argument that we find somewhat more elegant and more general
than Mordell's arguments (on p. 1351 of [M1]). We study the three
embeddings _1 , _2 , _3 of K into R. They send % to _1(%)=&2.21. . .,
_2(%)=0.53.. ., and _3(%)=1.67.. .. Because

U 3&24k +2U+26k +1=(U&22k_1(%))(U&22k_2(%))(U&22k_3(%))=2V 2

has to be positive, we have two possibilities: either U>22k_3(%), or
22k_1(%)<U<22k_2(%). Because by (2) for each i # [1, 2, 3] the sign of
U&22k_i (%) has to be equal to the sign of _i ($), we study the signs of these
explicitly known numbers:

%=1 =2 &=1 % &=1 =2 % &% &=2 %

_1 && + & & + +
_2 +& & + & & +
_3 ++ & & + & +

This shows that in the case U>22k_3(%) it must be true that $=&=2 % (we
call this the first case), and in the case 22k_1(%)<U<22k_2(%) we must
have $=&% (we call this the second case).

The First Case

Let us first treat the case U>22k_3(%), thus $=&=2 %=&2+3%+2%2.
Making explicit the square in (2), for some A, B, C # Z we have

U&%22k=(&2+3%+2%2)(A+B%+C% 2)2.

Working out the brackets and comparing coefficients, we find the following
system of three quadratic equations:

380 BENJAMIN M. M. DE WEGER

File: 641J 210909 . By:DS . Date:02:04:97 . Time:13:23 LOP8M. V8.0. Page 01:01
Codes: 2690 Signs: 1793 . Length: 45 pic 0 pts, 190 mm

A2+3B2+9C 2+3AB+6AC+8BC=0, (3)

3A2+8B2+20C 2+12AB+16AC+36BC=&22k,(4)

&2A2&6B2&16C 2&8AB&12AC&24BC=U.

We may assume without loss of generality that A, B, C are coprime, and
that B˚0.
From now on our proof diverges from Mordell's proof. We feel that for
the situation we're in, with k not necessarily zero, our line of argument
works prettier, but this is to some extent a matter of taste.
We view equation (3) as a quadratic equation in the variable A. Its
discriminant should be a square, if rational solutions are to exist. Hence for
a D # Z we have

D2=(3B+6C) 2&4(3B2+8BC+9C 2)=B(4C&3B).

Here we are lucky, because the quadratic form in B, C in the right hand
side factors over Z. We let ; be a prime divisor of the squarefree part
of B. Then ; divides also the squarefree part of 4C&3B, and since ;
divides both B and 4C&3B, we find that ; divides 4C.If ; divides both
B and C then (3) implies that ; also divides A, and, in view of (4), we have
;=2. Using B˚0 our conclusion is that B is a square or twice a square.
In the case B=E 2 for an E # Z (that we can assume to be nonnegative),
also 4C&3B is a square, say F 2, and we have D=\EF. We now solve (3)
for A:
 A=& 3
2 B&3C\ 1
2 D,

and express everything in E, F. In this way we find

A= 1
4 (&15E 2\2EF&3F 2), B=E 2, C= 1
4 (3E 2+F 2).

Since F is defined up to sign we may take the \-sign to be a +-sign. We
insert the above expressions for A, B, C into equation (4), and obtain

1
16 (&25E 4+12E 3F+18E 2F 2&4EF 3&F 4)=&22k.

We are lucky again, since the binary form in the left hand side of this
equation factors over Z, and we thus find

(E&F)(25E 3+13E 2F&5EF 2&F 3)=2m,(5)

where m=2k+4. Had we not been this lucky, we would have arrived at
a so-called ThueMahler equation. Procedures for solving such equations
are known (see [TW2]), but are far from elementary.
 381EQUAL BINOMIAL COEFFICIENTS

File: 641J 210910 . By:DS . Date:02:04:97 . Time:13:23 LOP8M. V8.0. Page 01:01
Codes: 2753 Signs: 1960 . Length: 45 pic 0 pts, 190 mm

Before studying this equation, we first mention that the second case,
when B=2E 2, leads to the same expressions for A, B, C in terms of E, F
as above, multiplied by a factor 2. Hence we find the same quartic Eq. (5),
but this time with m=2k+2.
Returning to Eq. (5), let us write E=(&1) g 2hP and F=(&1) g 2hQ for
some nonnegative integers g, h, such that P, Q are coprime integers with
P>Q. Now we proceed to solve

(P&Q)(25P3+13P2Q&5PQ2&Q3)=2n,

with n=m&4h. Because P&Q divides 2n, there is an integer l˚0 such
that P&Q=2l. Substituting P=Q+2l into the above equation we find

32Q3+2l+53Q2+22l +311Q+23l25=2n & l.(6)

If l=0 then (6) immediately yields that n=0. So we have to solve

4Q3+12Q2+11Q+3=0,

which is easily seen to have only Q=&1 as integral solution. It leads to
P=0, using the fact that A, B, C are coprime, further to (E, F)=(0, \2)
with m=4, and to (A, B, C)=(&3, 0, 1) with k=0. Finally, this gives
(U, V)=(2, \1), and (X, Y)=(1, 0), (1, &1).
If l=1 then (6) becomes

32Q3+192Q2+352Q+200=2n&1.

The first terms 32Q3, 192Q2 and 352Q are all divisible by 32, whereas the
last term 200 is only divisible by 8, and not anymore by 16. Hence the
entire left hand side is divisible by 8 but not by 16, so n&1=3, and we
find the equation
 Q3+6Q2+11Q+6=0.

It has the solutions Q=&3, &2, &1 leading to P=&1, 0, 1. The case
(P, Q)=(&1, &3) leads to (E, F )=(1, 3) with m=4, and to (A, B, C)=
(&9, 1, 3) with k=0. Finally, this gives (U, V)=(12, \29), and (X, Y)=
(6, 14), (6, &15). The case (P, Q)=(0, &2) does not satisfy the requirements
of P, Q being coprime (and is seen to lead to the solutions found above at
l=0). The case (P, Q)=(1, &1) leads to (E, F)=(1, &1) with m=4, and
to (A, B, C)=(&5, 1, 1) with k=0. Finally, this gives (U, V)=(4, \5),
and (X, Y)=(2, 2), (2, &3).
It remains to treat the case l˚2. This time in (6) the last three terms
2l +53Q2,22l +311Q and 23l25 are divisible by 64, whereas the first term
32Q3 is only divisible by 32, but not by 64. It follows that n&l=5. Note

382 BENJAMIN M. M. DE WEGER

File: 641J 210911 . By:DS . Date:02:04:97 . Time:13:23 LOP8M. V8.0. Page 01:01
Codes: 2283 Signs: 1255 . Length: 45 pic 0 pts, 190 mm

that in Mordell's original work only k=0 is treated, in which case n˛4,
so that then the case l˚2 is trivial.
Putting, for convenience,

Z=Q+2l, W=2l&2,

we find the equation
 Z3&4ZW 2+2W 3=1. (7)

Equation (7) is a so-called Thue equation, that we conjecture to have only
the following solutions:

(Z, W)=(1, 2), (1, 0), (&1, &1), (&5, &3), (&31, 14).

This can probably be proved by the deep methods of the GelfondBaker
method, cf. [TW1]. But for us it would be like firing a cannon to kill a
mosquito, because all we need is those solutions of (7) for which W is a
power of 2. This can be done in an elementary way as follows.
First we show that if |W| ˚2 then |ZW| <2.61. Namely, let %1 , %2 , %3
be the three roots of t3&4t+2=0 (thus the %i are the _j (%) defined above,
but not necessarily in the same order). The equation (7) now factors as

(Z&%1W)(Z&%2W)(Z&%3W)=1,

and for a given solution Z, W we take indices such that

|Z&%1W|< |Z&%2W|< |Z&%3W|.

Either |Z&%1W|˚ 1
2|W| min|%i&%j | >0.567 |W|, and then

1= `

3

i =1 |Z&%iW|> |Z&%1W| 3˚(0.567 |W|) 3,

and then it follows that |W| ˛1, or |Z&%1W|< 1
2 |W| min|%i&%j |, and
then for k=2, 3 we find

|Z&%kW|˚ |W||%1&%k |&|Z&%1W|> 1
2 |W| min|%i&%j | >0.567 |W|,

and thus by |W|˚2
}
Z
W}
˛|%1 |+}
Z
W&%1}

=|%1 |+ 1
|Z&W%2 ||Z&W%3 ||W| <2.22+ 1
0.567 2 |W| 3<2.61.
 383EQUAL BINOMIAL COEFFICIENTS

File: 641J 210912 . By:DS . Date:02:04:97 . Time:13:23 LOP8M. V8.0. Page 01:01
Codes: 2477 Signs: 1452 . Length: 45 pic 0 pts, 190 mm

Next we show that when Z{1 and l is large, then so is |ZW|. Namely,
we look at (7) (mod 22l &2):

Z3=4ZW 2&2W 3+1=Z 22l&2&23l &5+1#1 (mod 22l&2),

provided that l˚3, and it follows that

22l &2 |(Z3&1)=(Z&1)(Z2+Z+1).

Since Z2+Z+1 is always odd, we have Z#1 (mod 22l&2), hence Z=1 or
|Z|˚22l&2&1. In the latter case we must have
}
Z
W}
˚22l&2&1
2l&2 =2l& 1
2l &2 .

Putting things together, on noting that 2l&12l &2<2.61 implies l=1,
we find for the case l˚2 only the possibilities |W|˛1 or Z=1 (note that
l=2 implies W=1). The solutions of (7) satisfying these conditions are
easy to determine: the only one is (Z, W)=(1, 2), with l=3. It leads to
(P, Q)=(1, &7), and to (E, F)=(1, &7) with m=8, further to (A, B, C)=
(&44, 1, 13) with k=2, to (U, V)=(322, \4066), and finally to (X, Y)=
(16116, &206564), (16116, 200164).

The Second Case

Now we treat the case 22k_1(%)<U<22k_2(%) where $=&%. Note that
in Mordell's original work only k=0 is treated, in which case we have at
once &2˛U˛1, which is trivial.
We proceed as in the first case above. So for some A, B, C # Z we have

U&% 22k=&%(A+B%+C%2) 2.

Working out the brackets and comparing coefficients, we find the following
system of three quadratic equations:

&C 2+AB+4BC=0, (8)

&A2&4B 2&16C 2&8AC+4BC=&22k,(9)

2B2+8C 2+4AC=U.

We may assume without loss of generality that A, B, C are coprime, and
that B˚0.
We are lucky once more, in that equation (8) now gives at once

(C&2B)2=B(A+4B),

so that again B is a square or twice a square.

384 BENJAMIN M. M. DE WEGER

File: 641J 210913 . By:DS . Date:02:04:97 . Time:13:23 LOP8M. V8.0. Page 01:01
Codes: 2968 Signs: 2135 . Length: 45 pic 0 pts, 190 mm

In the case B=E 2 (with an E that we can assume to be nonnegative) we
have A+4B=F 2, and we may take C=2E 2+EF. We substitute this into
(9), and thus obtain

12E 4+28E 3F+24E 2F 2+8EF 3+F 4=2m (10)

with m=2k. And again, in the case B=2E 2 we find the same equation
(10), but with m=2k&2.
This time the binary form in the left hand side of (10) does not factor
over Z, so now we seem to have run out of luck, and have to turn to non-
elementary methods such as [TW2]. But fortunately this is not so. To start
with, if m˚1 then F is even, say F=2F1 . Hence

2m &2=3E 4+14E 3F1+24E 2F 2
1+16EF 3
1+4F 4
1 ,

and we see that if m˚3 then also E is even. Since A, B and C are coprime
integers, we have only to search the solutions with m˛2.
Further, our luck is that (10) does not have any linear factors over R.
Using this, we observe that x4+8x3+24x2+28x+12 has as minimal
value 1 (at x=&1), and then by (10) we get

2m =E 4 \\F
E+
 4+8 \F
E+
 3+24\F
E+
 2+28 F
E+12+˚E 4.

But then we see E 4˛2m˛4, hence |E| ˛1. Now it is easily seen that in fact
there are only three solutions: (E, F)=(0, \1), (1, &1), (1, &2). The case
(E, F )=(0, \1) with m=0 leads to (A, B, C)=(1, 0, 0) with k=0, further
to (U, V)=(0, \1), and finally to (X, Y)=(0, 0), (0, &1). The case
(E, F )=(1, &1) with m=0 leads to (A, B, C)=(&3, 1, 1) with k=0,
further to (U, V)=(&2, \1), and finally to (X, Y)=(&1, 0), (&1, &1).
The case (E, F )=(1, &2) with m=2 leads to (A, B, C)=(0, 1, 0) with
k=1, further to (U, V)=(2, \2), and finally to (X, Y)=( 1
4 , &5
8 ), ( 1
4 , &3
8 ).
This completes the proof. K

REFERENCES

[AEH] H. L. Abbott, P. Erdo˘ s, and D. Hanson, On the number of times an integer occurs
as a binomial coefficient, Am. Math. Monthly 81 (1974), 256261.
[Av] E . T. Avanesov, Solution of a problem on figurative numbers [in Russian], Acta
Arith. 12 (196667), 409420.
[F] G. Faltings, Endlichkeitssa˘ tze fu˘ r abelsche Varieta˘ ten u˘ ber Zahlko˘ pern, Invent. Math.
73 (1983), 349366.
[G] R. K. Guy, ``Unsolved Problems in Number Theory,'' Second edition, Springer-
Verlag, New York, 1994.
[GPZ] J. Gebel, A. Petho˘ , and H. G. Zimmer, Computing integral points on elliptic curves,
Acta Arith. 68 (1994), 171192.
 385EQUAL BINOMIAL COEFFICIENTS

File: 641J 210914 . By:DS . Date:02:04:97 . Time:13:23 LOP8M. V8.0. Page 01:01
Codes: 2002 Signs: 1438 . Length: 45 pic 0 pts, 190 mm

[L] D. A. Lind, The quadratic field Q(- 5) and a certain diophantine equation, Fibonacci
Quart. 6 (1968), 8693.
[M1] L. J. Mordell, On the integer solutions of y( y+1)=x(x+1)(x+2), Pacific J. Math.
13 (1963), 13471351.
[M2] L. J. Mordell, ``Diophantine Equations,'' Academic Press, New York, 1969.
[Pi] A kos Pinte r, A note on the diophantine equation ( x
4)=( y
2), Publ. Math. Debrecen 47
(1995), 411415.
[Sil] J. H. Silverman, ``The arithmetic of Elliptic Curves,'' Springer-Verlag, Berlin, 1986.
[Sin1] D. Singmaster, How often does an integer occur as a binomial coefficient, Am. Math.
Monthly 78 (1971), 385386.
[Sin2] D. Singmaster, Repeated binomial coefficients and Fibonacci numbers, Fibonacci
Quart. 13 (1975), 295298.
[Sm] N. P. Smart, S-integral points on elliptic curves, Math. Proc. Cambridge Phil. Soc.
116 (1994), 391399.
[ST] R. J. Stroeker and N. Tzanakis, Solving elliptic diophantine equations by estimating
linear forms in elliptic logarithms, Acta Arith. 67 (1994), 177196.
[TW1] N. Tzanakis and B. M. M. de Weger, On the practical solution of the Thue equation,
J. Number Theory 31 (1989), 99132.
[TW2] N. Tzanakis and B. M. M. de Weger, How to explicitly solve a ThueMahler
equation, Compositio Math. 84 (1992), 223288.
[dW] B. M. M. de Weger, A binomial diophantine equation, Quart. J. Math. Oxford
Ser. 2 47 (1996), 221231.

386 BENJAMIN M. M. DE WEGER
