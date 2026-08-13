<!-- source: https://math.deweger.net/papers/[28]StdW-EllBinom-MathComp[1999].pdf | converted from PDF -->

MATHEMATICS OF COMPUTATION
Volume 68, Number 227, Pages 1257–1281
S 0025-5718(99)01047-9
Article electronically published on February 23, 1999

ELLIPTIC BINOMIAL DIOPHANTINE EQUATIONS

ROELOF J. STROEKER AND BENJAMIN M. M. DE WEGER

Abstract. The complete sets of solutions of the equation (n
k = (m
ℓ  are
determined for the cases (k, ℓ)= (2, 3), (2, 4), (2, 6), (2, 8), (3, 4), (3, 6), (4, 6),
(4, 8). In each of these cases the equation is reduced to an elliptic equation,
which is solved by using linear forms in elliptic logarithms. In all but one case
this is more or less routine, but in the remaining case ((k, ℓ)= (3, 6)) we had
to devise a new variant of the method.

1. Introduction

In Pascal's Triangle, composed of the binomial coecients 
n
k
 for n =

0, 1, 2,... ,0  k  n, all natural numbers, with the exception of 2, occur at
least twice, and many three times or more. Not counting multiple occurrences of

trivial type, coming from 
n
0
 =1, 
n
1
 = n and 
n
k
 =  n
n − k
 , one could

formulate the following problem.

Main Problem. To determine all natural numbers that occur at least twice in
Pascal’s Triangle as binomial coeﬃcient 
n
k
 with 2  k  1
2 n.

As yet this problem is unsolved in its full generality. The only nontrivial solutions
known at this time are the following:

16
2
  = 10
3
  = 120, 21
2
  = 10
4
  = 210, 56
2
  = 22
3
  = 1540,
120
2
  = 36
3
  = 7140, 
153
2
  = 
19
5
  = 11628, 
221
2
  = 
17
8
  = 24310,

78
2
  = 15
5
  = 
14
6
  = 3003,

and 
F2i+2F2i+3
F2iF2i+3
  = 
F2i+2F2i+3 − 1
F2iF2i+3 +1
  for i =1, 2,... ,
 9
>>>>>>>>=

>>>>>>>>;

(1)

where Fn is the nth Fibonacci number, dened by F0 =0,F1 =1, and Fn+1 =
Fn + Fn−1 for n =1, 2,... . This innite family of solutions is due to D.A. Lind
[L] and D.A. Singmaster [Sin]. It is conjectured that there are no other nontrivial

solutions, and it is known that there are none with 
n
k
  1030 or n  1000, cf.

[dW2].

Received by the editor October 16, 1997.
1991 Mathematics Subject Classiﬁcation. Primary 11D25, 11G05; Secondary 11B65, 14H52.
Key words and phrases. Diophantine equation, elliptic curve, binomial coecient.
The second author's research was supported by the Netherlands Mathematical Research Foun-
dation SWON with nancial aid from the Netherlands Organization for Scientic Research NWO.

c⃝1999 American Mathematical Society

1257

1258 ROELOF J. STROEKER AND BENJAMIN M. M. DE WEGER

For xed k, ℓ (with 2  k< ℓ) the equation n
k
 = m
ℓ
  has been completely

solved in three cases only, namely for (k, ℓ)=(2, 3) by E.T. Avanesov [A], for
(k, ℓ)= (2, 4) by one of us [dW1] and independently by A. Pinter [P], and for
(k, ℓ)= (3, 4) by a remark of one of us, noting that the equation in this case
reduces at once to an equation solved by L.J. Mordell [M1], see [dW2].

For a few choices of (k, ℓ) the equation n
k
 = 
m
ℓ
  represents an elliptic curve,

or can be transformed into another equation representing an elliptic curve. Note

that n
k
 is, for xed k, a polynomial in n of degree k with rational coecients.

For even k, using the obvious symmetry about n − k−1
2 , it is also a polynomial in
(n − k−1
2 )
2 of degree 1
2 k with rational coecients. In particular,
n
2
 is quadratic in n, 
n
3
 is cubic in n,
n
4
 is quartic in n, and also quadratic in (n − 3
2 )
2,
n
6
 is cubic in (n − 5
2 )
2, 
n
8
 is quartic in (n − 7
2 )
2.

Now, let fq,gq 2 Z[x] be polynomials of degree q. Then the equations

y2 = f3(x),y2 = f4(x),f3(y)= g3(x)

generically represent elliptic curves. Equations of the rst two types y2 = fq(x)
for q =3, 4 can be reduced to a number of Thue equations, cf. L.J. Mordell [M1],
and for Thue equations general solution methods exist, based on estimations for
linear forms in logarithms of algebraic numbers, cf. N. Tzanakis and B.M.M. de
Weger [TW]. Such methods were used in [dW1] and [P] cited above, for solvingn
2
 = m
4
  . An alternative, though often less practical approach is provided by

Yu. Bilu and G. Hanrot [BH]. For the case f3(y)= g3(x) however we do not know
of any practical method that works in general. Only some very special types can be
solved, such as superelliptic equations (where f3(y)= y3, see [BH]). In theory an
upper bound for the absolute values of the coordinates of an integral point on any
model g(x, y) = 0 for an elliptic curve is explicitly known (cf. [BC]), but the known
upper bounds are so large as to render the corresponding search range completely
unworkable.
Only recently techniques have been developed involving estimations of linear
forms in elliptic logarithms for the solution of elliptic diophantine equations. We
felt that most likely this method should also work quite eciently for the binomial
equations at hand. Success should be almost guaranteed for any reasonable equa-
tion of type y2 = fq(x)for q =3, 4, as the elliptic logarithm method, developed
independently by R.J. Stroeker and N. Tzanakis [ST1], by J. Gebel, A. Peth}oand
H.G. Zimmer [GPZ], and by N.P. Smart [Sm] for q = 3, and by N. Tzanakis [T] for
q = 4, is quite generally applicable.
For the case f3(y)= g3(x), which also represents an elliptic curve, a similar
method should be applicable, but such a method is not to be found yet in the
literature. As it turned out, the main ideas of [ST1] and [T] carried through to this
case too, without signicant changes. This points at the probable existence of an
ecient method for solving any reasonable equation of type f3(y)= g3(x), and even
of the more general type f3(x, y)= 0, where f 2 Z(x, y) has degree 3 and is not

ELLIPTIC BINOMIAL DIOPHANTINE EQUATIONS 1259

necessarily homogeneous. We study this general type of equation in a forthcoming
paper [SW]; in the present paper we merely concentrate on the particular equation

coming from 
n
3
 = m
6
  .

All this enabled us to prove the following results. Three of them are already
known, but for these we present dierent proofs. From now on we do not maintain
the restriction m, n > 0 anymore, but we will allow m, n 2 Z, based on the denition

n
k
 = 1
k!
 k−1Y

i=0(n − i)for k  0.

Theorem A23 (Avanesov). The only solutions of 
n
2
 = 
m
3
  are those listed

in Table T23.

Theorem A24 (de Weger, Pinter). The only solutions of 
n
2
 = m
4
  are those

listed in Table T24.

Theorem A26. The only solutions of n
2
 = 
m
6
  are those listed in Table T26.

Theorem A28. The only solutions of n
2
 = 
m
8
  are those listed in Table T28.

Theorem A34 (Mordell, de Weger). The only solutions of 
n
3
 = m
4
  are those

listed in Table T34.

Theorem A36. The only solutions of n
3
 = 
m
6
  are those listed in Table T36.

Theorem A46. The only solutions of n
4
 = 
m
6
  are those listed in Table T46.

Theorem A48. The only solutions of n
4
 = 
m
8
  are those listed in Table T48.

One might wonder what can be said about other combinations of values for k

and ℓ in n
k
 = m
ℓ
  than those considered here. If k =2or k =4then we

encounter an equation of type y2 = f`(x), which represents a hyperelliptic curve
of genus b `−1
2 c 2when ℓ  5. For such equations there are approaches that
should work as a rule, like those by Thue equations, or by Bilu's method [BH], but
in any practical sense these techniques seem too complex by far, even for the case

of 
n
2
 = m
5
  . For other values of (k, ℓ) no methods are known, and all we can

say is that in many of these cases the binomial equation 
n
k
 = 
m
ℓ
  possibly

represents an algebraic curve of genus > 1, and therefore at most nitely many
rational solutions exist, by celebrated results of G. Faltings [F].

Very recently we have been able to completely solve the equations 
n
k
 =
n − 1
k +2
 (which has no nontrivial solutions) and n
k
 = n − 2
k +1
 (which has

no nontrivial solutions other than 6
1

 = 4
2

 ). We did this by the same vari-

ant of the elliptic logarithms method that we use in the present paper for solvingn
3
 = 
m
6
  . We intend to give details in our forthcoming paper [SW].

1260 ROELOF J. STROEKER AND BENJAMIN M. M. DE WEGER

Table 1. Transformations from binomial equations to elliptic equations

(k, ℓ) transformation
(2, 3) X =3m − 3 Y =9n − 5
(2, 4) U = m − 2 V =6n − 3
(2, 6) X = 5
2 m2 − 25
2 m +8 Y =75n − 38
(2, 8) U = 1
2 m2 − 7
2 m +6 V = 210n − 105
(3, 4) X = n − 1 Y = 1
2 m2 − 3
2 m
(3, 6) U = n − 1 V = 1
2 m2 − 5
2 m +3
(4, 6) X = 15
2 m2 − 75
2 m +25 Y = 225
2 n2 − 675
2 n + 112
(4, 8) U = 1
2 m2 − 7
2 m +3 V = 105n2 − 315n + 105

We now turn to the above mentioned eight cases, which we shall call elliptic
binomial equations. Inspired by the above remarks, we introduce changes of vari-
ables as given in Table 1. Notice that the new variables (X, Y or U, V ) are integral
valued.
These transformations are chosen such that the resulting equations have a conve-
nient form. For the cases of type f2(Y )= g3(X) this means that a global minimal
Weierstrass equation over Z is obtained; for the cases of type f2(V )= g4(U )this
means that f2(V )= V 2, the constant term in g4(U ) is a square, and the coecients
are integers as small as possible; and for the case f3(U )= g3(V ) the coecients of
both polynomials are again integers, as small as possible.
It now will be clear that Theorems A23 to A48 are consequences of the following
results.

Theorem B23. The complete set of solutions in rational integers X, Y of the equa-
tion
 Y 2 + Y = X 3 − 9X +20(W23)

is given in Table T23.

Table T23. The solutions to (W23) and to 
n
2
 = m
3
 

XY nm m1 m2
−3 −5 00 11
−34 10 −1 −1
−2 −6 0 −2
−25 02
0 −5 01 −10
04 11 10
1 −4 20
13 −20
3 −5 02 0 −1
34 12 01
6 −14 −13 −11
 XY nm m1 m2
613 23 1 −1
10 −31 −2 −2
10 30 22
12 −41 −45 21
12 40 55 −2 −1
27 −140 −15 10 1 −2
27 139 16 10 −12
63 −500 −55 22 −30
63 499 56 22 30
105 −1076 −119 36 13
105 1075 120 36 −1 −3

Theorem B24. The complete set of solutions in rational integers U, V of the equa-
tion
 V 2 =3U 4 +6U 3 − 3U 2 − 6U +9(Q24)
 ELLIPTIC BINOMIAL DIOPHANTINE EQUATIONS 1261

is given in Table T24.

Table T24. The solutions to (Q24) and to n
2
 = 
m
4
 

UV nm m1 m2 mT
−9 −123 −20 −7 02 1
−9 123 21 −7 −1 −10
−5 −33 −5 −3 10 1
−533 6 −3 −21 0
−3 −9 −1 −1 −20 1
−39 2 −1 11 0
−2 −3 00 01 1
−23 10 −10 0
−1 −3 01 00 1
−13 11 −11 0
 UV nm m1 m2 mT
0 −3 02 −11 1
03 12 00 0
1 −3 03 −10 1
13 13 01 0
2 −9 −14 11 1
29 24 −20 0
4 −33 −56 −21 1
433 66 10 0
8 −123 −20 10 −1 −11
8 123 21 10 02 0

Theorem B26. The complete set of solutions in rational integers X, Y of the equa-
tion
 Y 2 + Y = X 3 + X 2 − 58X + 1294(W26)

is given in Table T26.

Table T26. The solutions to (W26) and to 
n
2
 = m
6
 

XY nm m1 m2
−13 −5 0 −2
−13 4 02
−7 −38 02, 3 −10
−737 12, 3 10
−2 −38 01, 4 11
−237 11, 4 −1 −1
2 −35 −22
234 2 −2
8 −38 00, 5 0 −1
837 10, 5 01
14 −59 20
14 58 −20
 XY nm m1 m2
23 −113 −1 −1, 6 −11
23 112 2 −1, 6 1 −1
68 −563 −7 −3, 8 1 −2
68 562 8 −3, 8 −12
133 −1538 −20 −5, 10 −23
133 1537 21 −5, 10 2 −3
233 −3563 −2 −1
233 3562 21
323 −5813 −77 −9, 14 3 −1
323 5812 78 −9, 14 −31
2234 −105614 04
2234 105613 0 −4

Theorem B28. The complete set of solutions in rational integers U, V of the equa-
tion
 V 2 =35U 4 − 350U 3 + 945U 2 − 630U + 11025(Q28)

is given in Table T28.

Theorem B34 (Mordell). The complete set of solutions in rational integers X, Y
of the equation
 Y 2 + Y = X 3 − X(W34)

is given in Table T34.

1262 ROELOF J. STROEKER AND BENJAMIN M. M. DE WEGER

Table T28. The solutions to (Q28) and to n
2
 = 
m
8
 

UV nm m1 m2 m3 m4 m5
−147 −132195 10 −10 −1
−147 132195 000 −11
−25 −4445 10 −200
−25 4445 001 −10
−15 −1785 1 −10 −10
−15 1785 01 −100
−4 −245 010 00
−4 245 1 −1 −1 −10
0 −105 03, 4 10 −1 −10
0 105 13, 4 000 00
1 −105 02, 5 00 −100
1 105 12, 5 100 −10
3 −105 01, 6 100 00
3 105 11, 6 00 −1 −10
6 −105 00, 7 000 −10
6 105 10, 7 10 −100
8 −175 11 −100
8 175 0 −10 −10
10 −315 −1 −1, 8 100 −11
10 315 2 −1, 8 00 −10 −1
21 −1995 −9 −3, 10 0 −1 −1 −10
21 1995 10 −3, 10 110 00
55 −16275 −77 −7, 14 110 10
55 16275 78 −7, 14 0 −1 −1 −20
91 −46305 −220 −10, 17 01 −1 −10
91 46305 221 −10, 17 1 −10 0 0

Table T34. The solutions to (W34) and to 
n
3
 = m
4
 

XY nm m1
−1 −1 01, 2 3
−10 00, 3 −3
0 −1 11, 2 −1
00 10, 3 1
1 −1 21, 2 −2
 XY nm m1
10 20, 3 2
2 −3 3 4
22 3 −1, 4 −4
6 −15 7 −6
614 7 −4, 7 6

Table T36. The solutions to (C36) and to n
3
 = m
6
 

UV nm m1 m2 m3 m4
−10 02, 3 0110
−11 01, 4 000 −1
−13 00, 5 −1000
00 12, 3 0000
01 11, 4 −1100
03 10, 5 001 −1
 UV nm m1 m2 m3 m4
10 22, 3 −10 0 −1
11 21, 4 0010
13 20, 5 0100
26 3 −1, 6 −10 1 −1
821 9 −4, 9 1000

Theorem B36. The complete set of solutions in rational integers U, V of the equa-
tion
 15U 3 − 15U = V 3 − 4V 2 +3V(C36)

is given in Table T36.

ELLIPTIC BINOMIAL DIOPHANTINE EQUATIONS 1263

Table T46. The solutions to (W46) and to 
n
4
 = m
6
 

XY nm m1 m2 m3
−29 −32 11 −1
−29 31 −1 −11
−25 −88 011
−25 87 0 −1 −1
−20 −113 1, 22, 3 0 −10
−20 112 0, 32, 3 010
−14 −122 −200
−14 121 200
−5 −113 1, 21, 4 110
−5 112 0, 31, 4 −1 −10
5 −88 −10 −1
587 101
14 −75 −2 −20
14 74 220
16 −77 111
16 76 −1 −1 −1
20 −88 1 −10
20 87 −110
25 −113 1, 20, 5 −100
25 112 0, 30, 5 100
49 −320 020
49 319 0 −20
70 −563 00 −1
70 562 −1, 4 −1, 6 001
79 −680 1 −11
79 679 −11 −1
130 −1463 −101
130 1462 10 −1
250 −3938 −1 −20
250 3937 120
305 −5313 12 −1
305 5312 −1 −21
400 −7988 211
400 7987 −7, 10 −5, 10 −2 −1 −1
695 −18313 −3 −10
695 18312 310
1555 −61313 2 −10
1555 61312 −210
1645 −66713 021
1645 66712 0 −2 −1
18895 −2597288 −11 −2
18895 2597287 1 −12

Theorem B46. The complete set of solutions in rational integers X, Y of the equa-
tion
 Y 2 + Y = X 3 − 525X + 10156(W46)

is given in Table T46.

Theorem B48. The complete set of solutions in rational integers U, V of the equa-
tion
 V 2 = 105U 4 + 210U 3 − 945U 2 − 1890U + 11025(Q48)

1264 ROELOF J. STROEKER AND BENJAMIN M. M. DE WEGER

Table T48. The solutions to (Q48) and to n
4
 = 
m
8
 

UV nm m1 m2 m3
−3 −105 1, 23, 4 010
−3 105 0, 33, 4 −10 −1
−2 −105 1, 22, 5 00 −1
−2 105 0, 32, 5 −110
0 −105 1, 21, 6 −11 −1
0 105 0, 31, 6 000
 UV nm m1 m2 m3
3 −105 1, 20, 7 −100
3 105 0, 30, 7 01 −1
7 −525 11 −1
7 525 −1, 4 −1, 8 −200
33 −11445 −20 −1
33 11445 −9, 12 −5, 12 110

is given in Table T48.

Remarks. Theorem B23 is a bit more general than the result of Avanesov [A], and
our proof is rather dierent.
Theorem B24 is merely a restatement of the main result of [dW1] and [P]. Again
the proof we give below is of a dierent nature.
Theorem B34 is the main result of [M1]. See also J.H. Silverman [Sil1, Exercise
9.13, p. 275] for a dierent proof, and see [dW2]. The proof we give below is new.
The meaning of the parameters m1,... ,mr,mT , given in the Tables T23 to T48,
will be made clear in the next sections.

2. The cases “quadratic = cubic”

In this section we shall prove the Theorems B23, B26, B34 and B46, and thus
also Theorems A23, A26, A34 and A46. We start by giving in Table 2 some data
on the elliptic curves dened by (W23), (W26), (W34) and (W46), namely the
minimal discriminant , the j-invariant j, and the torsion group. These data are
easy to compute, e.g. with Apecs.
Further we need the rank r,and a basis P1,... ,Pr for the free part of the
Mordell-Weil group. This is more dicult, but can be done. We have the following
result.

Proposition 1. The elliptic curves (W23), (W26), (W34) and (W46) have ranks
r and bases P1,... ,Pr for the free parts of their Mordell-Weil groups as in Table
3.

Proof of Proposition 1. We used J.E. Cremona's program mwrank (dated 21 Feb-
ruary 1997, see [Cr]) on a Sun Sparcstation 4 to compute (unconditionally) the
ranks and the Mordell-Weil groups of the four curves. During execution no unusual
events occurred.
Brieﬂy, what the program does is this. First a 2-descent is carried out in order
to determine a basis for the quotient group E(Q)/2E(Q). What might go wrong {
but it didn't in these four cases { is that one of the relevant homogeneous spaces to

Table 2. Data of elliptic curves

curve ∆ j torsion
(W23) −130491 = −3
6  179 −110592=179 = −2
12  3
3  179
−1 trivial
(W26) −732796875 = −3
5  5
6  193 −1404928=46899 = −2
12  3
−5  7
3  193
−1 trivial
(W34) 37 110592=37 = 2
12  3
3  37
−1 trivial
(W46) −35299546875 = −3
7  5
6  1033 −1404928=3099 = −2
12  3
−1  7
3  1033
−1 trivial

ELLIPTIC BINOMIAL DIOPHANTINE EQUATIONS 1265

Table 3. Ranks and bases of Mordell-Weil groups

curve r P1 P2 P3
(W23) 2 (0, 4) (3, 4)
(W26) 2 (−7, 37) (8, 37)
(W34) 1 (0, 0)
(W46) 3 (25, 112) (−20, 112) (70, 562)

Table 4. Relevant constants on heights of basis points

curve (W23) (W26) (W34) (W46)
B 0.3027 0.6939 0.0256 1.561
H 6.530 9.152 4.832 11.30
runtime 3s 14s 2s 7m 26s

be searched for rational points happens to be locally solvable at all primes, without
any actual rational point being detected. A successful 2-descent should determine
the rank of the curve. Next, an innite descent has to be done. The purpose of this
is to obtain a basis for E(Q), given a basis for E(Q)/mE(Q)for some m  2. Here
always m = 2. To this end usually Zagier's theorem [Sik, Theorem 1.1] is used: if
the set
 S(B):= fP 2 E(Q) j ^h(P )  Bg

contains a complete set of coset representatives for mE(Q)in E(Q), then S(B)
generates E(Q). Here ^h is the Neron-Tate height function. For the successful
application of Zagier's theorem it is important that B is not too large. The relevant
B-values for our curves are rather small, see Table 4.
Finally, the inequality
1
2 h(P ) − ^h(P )  Hdif for all P 2 E(Q),

where Hdif is Siksek's [Sik] or Silverman's [Sil2] bound, whichever proves to be
smaller, gives an upper bound

h(P )  2B +2Hdif =: H

for the naive height h(P ) for all P 2 S(B). These bounds, given in Table 4, are
not too large, so that a direct search does not cause any problems. We also give
runtimes on a Sun Sparcstation 4 in Table 4.

Note that Cremona and Siksek use a canonical height function ^h which is twice
the height function used in [ST1]. Also Apecs uses the latter. Here we shall adopt
the convention of [ST1].
Further we remark that by a unimodular transformation we arranged the bases
such that the least eigenvalue of the Neron-Tate height pairing matrix, called c1
below, is as large as possible, see [ST2]. This is of importance for an optimal result
of the reduction procedure described below.
To prove Theorems B23, B26, B34 and B46, we use the method of linear forms
in elliptic logarithms. We closely follow Stroeker and Tzanakis [ST1], from which
paper we also adopt the notation. The proofs are very much a routine matter,
taking only a few seconds of runtime on a personal computer.

1266 ROELOF J. STROEKER AND BENJAMIN M. M. DE WEGER

Table 5. Relevant constants from [ST1]

curve (W23) (W26) (W34) (W46)
(a1;a2;a3;a4;a6) (0; 0; 1; −9; 20) (0; 1; 1; −58; 1294) (0; 0; 1; −1; 0) (0; 0; 1; −525; 10156)
(u; v; w; z) (1; 0; 0; − 1
2 )(1; − 1
3 ; 0; − 1
2 )(1; 0; 0; − 1
2 )(1; 0; 0; − 1
2 )

(a; b) (−9; 81
4 )(− 175
3 ; 141875
108 )(−1; 1
4 )(−525; 40625
4 )
γ −3:78765 ::: −12:7143 ::: 0:837565 :: : −29:4862 :::
ˆh(P1) 0:170261 ::: 0:224280 ::: 0:0255557 ::: 0:321316 :::
ˆh(P2) 0:202708 ::: 0:213613 ::: 0:374043 :::
ˆh(P3) 0:703410 :::
c1 0:147776 ::: 0:122596 ::: 0:0255557 ::: 0:210864 :::
c2 7:57530 ::: 25:4286 :: : 2:21431 :: : 58:9725 :::
X0 826 3 59
c3 0:902545 ::: 2:21110 :: : 1:97333 :: : 2:63185 :::
! 5:89947 ::: 2:67273 :: : 5:98691 :: : 2:06023 :::
=˝ 0:739959 ::: 0:820738 ::: 1:22112 :: : 0:751930 :::
˚(P1) 0:347573 ::: 0:401475 ::: 0:189458 :: : 0:202441 :::
˚(P2) 0:206446 ::: 0:246042 ::: 0:429501 :::
˚(P3) 0:117061 :::
u1 2:05050 ::: 1:073036 ::: 1:13427 :: : 0:417077 :::
u2 1:21792 ::: 0:657605 ::: 0:884874 :::
u3 0:241173 :::
hE 11:6136 ::: 14:1554 :: : 11:6136 :: : 14:1554 :::
A0 42:6087 ::: 36:0874 :: : 11:6136 :: : 41:5942 :::
A1 11:6136 ::: 14:1554 :: : 11:6136 :: : 14:1554 :::
A2 11:6136 ::: 14:1554 :: : 14:1554 :::
A3 14:1554 :::
c4 3:60535 :::  10
73 4:53651 :: :  10
73 4:81455 :: :  10
43 8:46092 :::  10
110

E ee e e
c5 11 1 1
c6 12:6136 ::: 15:1554 :: : 12:6136 :: : 15:1554 :::
c7 1:724397 ::: 1:724397 ::: 1:0625 2:11944 :::
c8 12:8748 ::: 15:4167 :: : 12:6361 :: : 15:5592 :::
M0 4:62556  10
40 7:50381  10
40 2:28469  10
25 1:42762  10
60

For an integral point we write P = m1P1 + ... + mrPr,where P1,... ,Pr is the
basis from Table 3. We write M =max
1ir jmij. We omitmostof the details of the

method, as we do not want to repeat the material of the paper [ST1]. Let us just
say that the linear form in elliptic logarithms has the shape

L(P )= m0ω + m1u1 + ... + mrur,

where ui = ωφ(Pi) are the elliptic logarithms. Here m0 2 Z is taken such that all
φ-values are in [0, 1). It follows that maxfM, jm0jg  rM .
On the one hand we have an upper bound for this linear form:

jL(P )j < 4p
2ec3−c1M 2 ,(2)

where the constants are dened in [ST1]; their values and other particulars of our
equations are given in Table 5. For the calculation of c3 the Siksek bound [Sik] was
used.
On the other hand the main result by David [D] on linear forms in elliptic
logarithms plays an essential r^ole, as it provides a lower bound for the linear form:

jL(P )j > exp (−c4(log(M )+ c7)(log log(M )+ c8)
r+2).

Together with (2) this yields an absolute upper bound M0 for M .
The calculations for Table 5 were performed with Apecs 4.2, and required negli-
gible runtime.
 ELLIPTIC BINOMIAL DIOPHANTINE EQUATIONS 1267

Table 6. Data of the reduction steps

curve M0 Cd > M1 Cd > M2 Cd > M3
(W23) 4:62556  10
40 10
123 1:62319  10
41 36 10
6 121:136 9 10
4 31:8904 7
(W26) 7:50381  10
40 10
124 2:22699  10
41 39 10
6 138:701 10 10
5 52:9622 9
(W34) 2:28469  10
25 10
51 7:58375  10
25 49 10
4 110:788 18 10
3 61:4003 16
(W46) 1:42762  10
60 10
243 5:88376  10
60 44 10
9 164:322 10 10
7 36:9323 9

To reduce the large upper bound M0, we apply lattice base reduction to the
lattice spanned by the columns of the matrix

A =
 0

B
B
B
B
B
@
 10 ... 00
01 ... 00
... ... . . . ... ...
00 ... 10
[Cu1][Cu2] ... [Cur][Cω]
 1

C
C
C
C
C
A ,

where C is a large constant, of the size of M r+1
0 ,and where [] denotes rounding to
the nearest integer. For a possible solution of our elliptic equation we look at the
lattice point
 A(m1,... ,mr,m0)
> =(m1,... ,mr,λ)
>,

where λ thus is a good approximation to CL(P ), viz.

jλ − CL(P )j 1
2 (rM0 + jm0j)  rM0.

We applied Zagier's algorithm for computing the values of φ(Pi) to the desired pre-
cision (of somewhat more than (r +1) log10 M0 decimal digits). For each of the four
lattices we computed a reduced basis by the LLL-algorithm. These computations
were done by Pari 1.39.
From the reduced basis we nd a lower bound d for the length of the shortest
nonzero lattice vector. We may assume that d is large enough. If it isn't, then we
have to try a larger value of C. We nd that either m1 = ... = mr =0, or

jλj qd2 − m2
1 − ... − m2
r  q
d2 − rM 2
0 ,

and thus
 jL(P )j 1
C
 q
d2 − rM 2
0 − rM0
 .

Together with inequality (2) this yields a reduced upper bound M1 for M ,namely

M1 =
 $s 1
c1
 
log 4p
2C + c3 − log q
d2 − rM 2
0 − rM0
%
 .

Iterating the procedure, we reduced M1 further to M2 and nally to M3.In Table
6 we list the values for C that we chose, the values for d that follow from the
application of the LLL-algorithm, and the reduced upper bounds M1,M2,M3 for
M .
We checked all points P corresponding to r-tuples (m1,... ,mr) with M  M3
for being solutions to inequality (2). The solutions thus found we checked for
integrality of the coordinates X, Y of P . These computations we again did in

1268 ROELOF J. STROEKER AND BENJAMIN M. M. DE WEGER

Table 7. Runtimes

curve comput. of φ(Pi) reduction small solut.
(W23) 3s < 1s 6s
(W26) 3s < 1s 10s
(W34) < 1s < 1s 1s
(W46) 25s 8s 4m 28s

Apecs. This produced the results mentioned above, and thus completes our proof.
Finally we give in Table 7 the runtimes on a Pentium 75Mhz personal computer.

3. The cases “quadratic = quartic”

In this section we prove Theorems B24, B28 and B48, and thus also Theorems
A24, A28 and A48. We use the method of linear forms in elliptic logarithms. We
follow Tzanakis [T], but at certain points use slight variations in the arguments.
The proofs are to some extent a routine matter, but now things are essentially more
complicated than in the previous section. We start by giving some information on
the elliptic curves represented by the equations (Q24), (Q28) and (Q48).
The birational transformations

( U = 6X1−18
X1+Y1−17 ,

V = −27X 2
1 +3Y 2
1 +882X1+84Y1−4167
(X1+Y1−17)2 ,
 ( X1 = −U 2−6U +6V +18
U 2 ,

Y1 = 18U 3−18U 2−6UV −54U +36V +108
U 3

relate equation (Q24) and the minimal model

Y 2
1 = X 3
1 − 147X1 + 610.(W24)

The birational transformations

( U = 210X1+130410
3X1+Y1+35805 ,

V = 195615X 2
1 +105Y 2
1 +340341750X1−7127820Y1−226983637125
(3X1+Y1+35805)2 ,

( X1 = 315U 2−630U +210V +22050
U 2 ,

Y1 = −36750U 3+198450U 2−630UV −198450U +44100V +4630500
U 3

relate equation (Q28) and the minimal model

Y 2
1 = X 3
1 − 1620675X1 + 385103250.(W28)
 ELLIPTIC BINOMIAL DIOPHANTINE EQUATIONS 1269

Table 8. Data of elliptic curves

curve  j torsion
(W24) 42550272 = 470596/57 = Z/2Z = hT i,
210  37  19 22  3−1  76  19−1 T =(5, 0)
(W28) 208370506291920000000 = 114354828/50615 = trivial
210  37  57  76  53  191 22  35  5−1  76  53−1  191−1

(W48) 999362923039687500 = 112678587/27620 = trivial
22  39  57  76  1381 2−2  33  5−1  73  233  1381−1

Table 9. Ranks and bases of Mordell-Weil groups

curve r P1 P2 P3 P4 P5
(W24) 2 (11, 18) (29, 144)
(W28) 5 (105, 14700) (−1365, 7350) (−315, −29400) (210, 7350) (− 4235
9 , − 872200
27 )
(W48) 3 (−236, 11143) (79, 5473) ( 631
4 , − 22681
8 )

The birational transformations
( U = 105X1−18690
5X1+Y1−2403 ,

V = −55965X 2
1 +105X1Y1+105Y 2
1 +70087815X1+336420Y1−11480080185
(5X1+Y1−2403)2 ,

( X1 = −157U 2−945U +105V +11025
2U 2 ,

Y1 = 5591U 3−49140U 2−525UV −154350U +11025V +1157625
2U 3

relate equation (Q48) and the minimal model

Y 2
1 + X1Y1 = X 3
1 − X 2
1 − 332817X1 + 56191841.(W48)

In Table 8 some data on these elliptic curves are given, namely the minimal
discriminant , the j-invariant j, and the torsion group. In the case of nontrivial
torsion generators of the torsion group are given.
Further we need the rank r,and a basis P1,... ,Pr for the free part of the
Mordell-Weil group. We have the following result. In the sequel coordinates of
points on the elliptic curves are given for the minimal models (W24), (W28) and
(W48), unless explicitly stated otherwise.

Proposition 2. The elliptic curves (W24), (W28) and (W48) have ranks r and
bases P1,... ,Pr for the free parts of their Mordell-Weil groups as in Table 9.

Proof of Proposition 2. Again we use Cremona's mwrank. No diculties were en-
countered with (W24). But with (W28) and (W48) mwrank ran into trouble, as
the upper bounds H the program computed for these curves turned out to be too
large. Table 10 gives the relevant values found by mwrank, where the runtimes on
a Sun Sparcstation 4 for (W28) and (W48) reﬂect the time it took mrank (without
`w') to compute a set of representatives for E(Q)/2E(Q).
Starting from here, we calculated by hand improved sets of representatives re-
sulting in much better values for B. The bounds H on the logarithmic height so
obtained appear to be small enough for Cremona's ﬁndinf to run successfully. This
is true for (W48), but in the case of (W28) ﬁndinf produces erroneous results like
points not on the curve, or it overlooks existing relations between points. John

1270 ROELOF J. STROEKER AND BENJAMIN M. M. DE WEGER

Table 10. Relevant constants on heights of basis points

curve (W24) (W28) (W48)
B 0.8105 5.117 2.734
H 9.063 22.79 17.93
runtime 13s 6h 54m 75h 9m

Table 11. Relevant constants on heights of basis points

curve (W28) (W48)
B 3.199 1.711
H 16.265 12.634
runtime (ﬁndinf) ˇ 2 weeks 2h

Cremona told us that these errors are most likely due to roundo. We give the
improved values for B and H in Table 11. Here the runtime given in the case of
(W28) is the expected total runtime for a hypothetically completely succesful run
of the program ﬁndinf, estimated from the amount of work it had completed when
it ran into serious trouble.
In the case of (W28) we use the sieving technique described in [Sik, section 4.1].
As a result of the 2-descent, we know that the points Pi (i =1,... , 5) of Table 9
generate a subgroup of odd index m in E(Q).
First we have to nd an upper bound for m. This we do by [Sik, Theorem 3.1].
To compute λ such that ^h(Q)  λ has no solutions Q 2 E(Q) other than the
point at innity, we try to show that there are no such points with ^h(Q) < ^h(P3)=
0.794302 ... . Because Siksek's upper bound for 1
2 h(Q)− ^h(Q)is Hdif = 4.93332 ... ,
we search, using Cremona's ﬁndinf, for the points with h(Q) < 2(^h(P3) + Hdif) <
11.4553. This search took 13 minutes and 40 seconds on a Sun Sparcstation 4, and
revealed that there are no points Q with ^h(Q)  λ =0.794302.
The regulator of P1,... ,P5 is R =28.3648 ... . Now [Sik, Theorem 3.1] tells us
that
 m   8R
(2λ)5
 1=2 =4.73582 ... ,

so that m  3. Note that Siksek uses twice our height.
Now we start the sieving, to show that m 6=3. Let

V3 = f(a1,... ,a5) j ai 2f−1, 0, 1g,a1P1 + ... + a5P5 2 3E(Q)g .

As m = 3 implies the existence of a nonzero element of V3, we intend to show that
V3 = f(0, 0, 0, 0, 0)g.
Let v be a prime of good reduction, such that #E(Fv) is divisible by 3, but not by
9. Put ℓ = 1
3 #E(Fv). Then the group ℓE(Fv) has order 3. Compute a generator G
of this group, and compute m1,... ,m5 2f−1, 0, 1g such that ℓPi  miG (mod v).
Now, if (a1,... ,a5) 2 V3,then ℓ(a1P1 + ... + a5P5) 2 3ℓE(Q), so that

(m1a1 + ... + m5a5)G  a1ℓP1 + ... + a5ℓP5  0(mod v).

ELLIPTIC BINOMIAL DIOPHANTINE EQUATIONS 1271

Table 12. Relations found in Siksek sieving

v ℓ G m1 m2 m3 m4 m5
11 5 5P1 10111
17 7 7P1 101 −1 −1
23 10 10P1 1 −1 −11 −1
31 11 11P1 110 −11
43 16 16P2 01 −11 −1
47 20 20P2 01 −1 −10
59 20 20P1 11101

As G generates a group of order 3 in E(Fv), we nd that

m1a1 + ... + m5a5  0(mod 3),

which constitutes a relation on the ai.
We do the above computation for a number of primes v, to nd as many indepen-
dent relations as needed or as possible. It turned out that seven primes, starting
from the smallest, is a sucient number in our situation to nd 5 independent
relations, thus proving that V3 = f(0, 0, 0, 0, 0)g. In Table 12 we give the primes v,
and for each prime the number ℓ, the generator G, and the relation m1,... ,m5.
Note that the 7  5 matrix of the mi, dened (mod 3), has rank 5 indeed.

Again note that each Mordell-Weil basis given is optimal for the least eigenvalue
of the Neron-Tate height pairing matrix.
We note that there is some symmetry, namely the irrelevance of the sign of V ,
that we now describe. We take the point Q as follows:

(W24) : Q = −P1 + P2 + T =(3, −14)
(W28) : Q = P1 − P3 − P4 =(−621, 33942)
(W48) : Q = −P1 + P2 − P3 = (178, −1691)

If a point P on the curve has coordinates U (P ),V (P ) on the quartic model, then
we have ˆ U (−P + Q)= U (P ),
V (−P + Q)= −V (P ).

As  > 0, the Weierstrass curve E(R) has a compact component and an innite
component. We denote the innite component by E0(R). Since Q is on the compact
component, it follows that of the two points P, −P + Q always one is on E0(R).
Thus from now on we may assume without loss of generality that our point P is on
the innite component. In the case of (W24) this implies that P is in the free part
of the Mordell-Weil group, i.e. that we can forget about the torsion point.
In the case of equation (W24) there is yet another symmetry:
ˆ U (P + T )= −U (P ) − 1,
V (P + T )= −V (P ),
 ˆ U (−P + Q + T )= −U (P ) − 1,
V (−P + Q + T )= V (P )

(note that Q + T is in the free part of the Mordell-Weil group). It follows that in
this case we may as well assume without loss of generality that U  0.
In Table 14 (later) we give the relevant constants from [T].
For all three of our elliptic curves we have that x0 >e1,so that U> U0 implies
that the point P is on E0(R). The group E0(Q) of rational points on this innite

1272 ROELOF J. STROEKER AND BENJAMIN M. M. DE WEGER

Table 13. Bases of relevant subgroups of Mordell-Weil groups

curve R1 R2 R3 R4 R5
(W24) P1 =(11; 18) P2 =(29; 144)
(W28) P1 + P4 = P2 + P4 = P3 + P4 = P1 + P2 + P3 + P4 = −P4 + P5 =
(4585; 298900) (1155; −7350) (5005; −343000) ( 10990
9 ; 406700
27  (1605; −43800)
(W48) P1 − P2 = P1 + P2 = P2 − P3 =
(2914; 152893) (464; 993) (989; 25843)

component is a subgroup of E(Q) of index 2. Clearly all that we need is a basis
R1,... ,Rr for this smaller group only. It's easy to show that we can take this basis
as in Table 13. Note that we took these bases such that an optimal least eigenvalue
of the Neron-Tate height pairing matrix is obtained.
For the rational point P we now put

P = m1P1 + ... + mrPr = m0
1R1 + ... + m0
rRr.

For the solutions we give in Tables T24, T28 and T48 the corresponding values of
m1,... mr, also for the points not on the innite component E0(R). In the case
of (Q24) we have P = mT T + m1P1 + m2P2, with mT =0 if P is on E0(R), and
mT =1 if P is in the compact component. But as argued above we may assume
that P is on E0(R), i.e. mT =0. Note that

for (Q24): m0
1 = m1,m0
2 = m2,

for (Q28): m0
1 = 1
2 (m1 − m2 − m3 + m4 + m5),

m0
2 = 1
2 (−m1 + m2 − m3 + m4 + m5),

m0
3 = 1
2 (−m1 − m2 + m3 + m4 + m5),

m0
4 = 1
2 (m1 + m2 + m3 − m4 − m5),m0
5 = m5,

for (Q48): m0
1 = 1
2 (m1 − m2 − m3),

m0
2 = 1
2 (m1 + m2 + m3),m0
3 = −m3.

In any case we put
 M =maxfjm0
1j,... , jm0
rjg,

and we have
 φ(P )= m0
0 + m0
1φ(R1)+ ... + m0
rφ(Rr),

where we take m0
0 2 Z such that 0  φ(P ) < 1. It follows that jm0
0j rM .An
interesting point to notice about (Q24) is that P0 is not independent of R1 and R2.
Indeed, we have 2P0 = −R1 + R2.In terms of φ we have

2φ(P0)= −φ(R1)+ φ(R2)+1.

It follows that we do not have to count with P0 anymore, when we multiply the
linear form by 2 and adapt m0
i. Equally interesting is the fact that in both cases
(Q28) and (Q48) a similar relation (over Q) does not exist, or so it seems, at least
not with very small coecients.
We put ui = ωφ(Ri)for i =1,... ,r,and u0 = ωφ(P0). Our linear form in
elliptic logarithms then is

L(P )= m0
0ω + m0
1u1 + ... + m0
rur + u0,

ELLIPTIC BINOMIAL DIOPHANTINE EQUATIONS 1273

for which we have the inequality

jL(P )j <c9e 1
2 c10+c11−c1M 2 .(3)

On the other hand, in the cases of (Q28) and (Q48), David [D] gives

jL(P )j > exp (−c4(log(rM )+ c5)(log log(rM )+ c6)r+3).

But in the case of (Q24) we use

2L(P )= (2m0
0 +1)+(2m0
1 − 1)u1 +(2m0
2 +1)u2

instead of L(P ) itself, as it has one term less. Then, based on r =2 and the
inequality maxfj2m0
0 +1j, j2m0
1 − 1j, j2m0
2 +1jg  4M + 1, David [D] gives

j2L(P )j > exp (−c4(log(4M +1) + c5)(log log(4M +1) + c6)
4).

Whatever the case may be, together with (3) this yields an absolute upper bound
M0 for M .
In Table14wetake A0 corresponding to ω,and A
0
0 corresponding to u0.To
compute A
0
0 we had to estimate the Neron-Tate height of the non-rational point
P0.We used ^h(P )  c11 + 1
2 h(X1(P )), where h(X) is the absolute logarithmic Weil
height for the algebraic number X. For computing c11 we always used the minimal
model. Note that D  2, since the coordinates of P0 are quadratic.
The reduction in the case of (Q24) goes just as in the previous section, based on
inequality (3), but working with 2L(P ). We take

A =
 0

@ 10 0
01 0
[Cu1][Cu2][Cω]
 1

A ,

and we look at the lattice point

A(2m0
1 − 1, 2m0
2 +1, 2m0
0 +1)
> =(2m0
1 − 1, 2m0
2 +1,λ)
>,

where λ thus is a good approximation to 2CL(P ), viz.

jλ − 2CL(P )j 1
2 (2(2M0 +1) + 2jm0
0j +1)  4M0 + 3
2 ,

because jm0j 2M0. As in the previous section we obtain by (3) a reduced upper
bound M1 for M ,namely

M1 = r 1
c1
 log (2c9C)+ 1
2 c10 + c11 − log pd2 − 2(2M0 +1)2 − (4M0 + 3
2 )
.

In Table 15 we give the data for this reduction.
In the cases (Q28) and (Q48) the reduction procedure is slightly dierent, be-
cause now the linear forms in elliptic logarithms are inhomogeneous. We take the
lattice as usual, spanned by the columns of

A =
 0

B
B
B
B
B
@
 10 ... 00
01 ... 00
... ... . . . ... ...
00 ... 10
[Cu1][Cu2] ... [Cur][Cω]
 1

C
C
C
C
C
A ,

and look at the point
 y =(0, 0,... , 0, −[Cu0])
>,

1274 ROELOF J. STROEKER AND BENJAMIN M. M. DE WEGER

Table 14. Relevant constants from [T]

curve (Q24) (Q28) (Q48)
(a; b; c; (3; 6; −3; (35; −350; 945; (105; 210; −945;
d; e) −6; 3) −630; 105) −1890; 105)
(a1;a2;a3; (−2; −4; 36; (−6; 936; −73500; (−18; −1026; 44100;
a4; −108; −1543500; −4630500;
a6) 432) −1444716000) 4750893000)
(A; B) (−147; 610) (−1620675; (−5325075;
385103250) 3590952750)
(X1;Y1) (x; y)(x; y)( 1
4 (x +1);

1
8 (−x + y − 1))
˙ 1 −11
x0 −1+6
p3 315 + 210
p35 −315 + 210
p105
u0 09:38860 0
e1 8:82475 ::: 1131:51 ::: 1835:35 :::
e2 5 246:906 ::: 755:246 :::
e3 −13:8247 ::: −1378:42 ::: −2590:60 :::
! 1:96209 ::: 0:160046 ::: 0:130311 :::
=˝ 1:41977 ::: 1:14814 ::: 1:28813 :::
U0 09:38860 0
P0 (−1+6
p3; (315 + 210
p35; ( −157+105
p105
2 ;
18 − 6
p3) 36750 + 630
p
35) 5591−525
p105
2 )
ˆh(R1) 0:202321 ::: 1:76131 ::: 1:12812 :::
ˆh(R2) 0:506291 ::: 1:17118 ::: 1:00476 :::
ˆh(R3) 2:00293 ::: 1:52711 :::
ˆh(R4) 2:80407 :::
ˆh(R5) 2:10666 :::
c1 0:194012 ::: 0:612991 ::: 0:613916 :::
˚(R1) 0:352986 ::: 0:185963 ::: 0:142707 :::
˚(R2) 0:192459 ::: 0:540398 ::: 0:469004 :::
˚(R3) 0:822229 ::: 0:252395 :::
˚(R4) 0:422353 :::
˚(R5) 0:664566 :::
˚(P0) 0:342498 ::: 0:491395 :::
c9 1
3 p3=0:577350 ::: 0:234326 ::: 0:104791
c10 log(10)=2:30258 ::: 7:73976 7:71756
c11 3:28540 ::: 5:61238 ::: 4:87006 :::
ˆh(P0)  9:15817 8:00858
u1 0:692592 ::: 0:0297628 ::: 0:0185963 :::
u2 0:377623 ::: 0:0864891 ::: 0:0611166 :::
u3 0:131595 ::: 0:0328899 :::
u4 0:0675963 :::
u5 0:106361 :::
u0 0:0548158 ::: 0:0640343 :::
hE 13:0617 ::: 19:0758 ::: 21:3085 :::
D 12 2
A0 13:3810 ::: 19:0758 ::: 21:3085 :::
A1 13:0617 ::: 19:0758 ::: 21:3085 :::
A2 13:0617 ::: 19:0758 ::: 21:3085 :::
A3 19:0758 ::: 21:3085 :::
A4 19:0758 :::
A5 19:0758 :::
A0
0 19:0758 ::: 21:3085 :::
c4 1:43221  10
73 5:61880  10
277 2:07088  10
160

c5 11:69314 ::: 1:69314 :::
c6 14:0617 ::: 20:7690 ::: 23:0016 :::
M0 2:90912  10
40 8:81788  10
145 5:88682  10
85

which most likely will not be a lattice point. Here the relevant distance d is that be-
tween y and the nearest lattice point, since now λ dened by A(m0
1,... ,m0
r,m0
0)
> −
y =(m0
1,... ,m0
r,λ)
> is approximately CL(P ). To be precise, we have

jλ − CL(P )j 1
2 (rM0 + jm0
0j +1)  rM0 + 1
2 .

ELLIPTIC BINOMIAL DIOPHANTINE EQUATIONS 1275

Table 15. Data of the reduction steps

curve M0 Cd > M1 Cd > M2 Cd > M3
(Q24) 2:90912  10
40 10
125 2:42146  10
41 31 10
7 231:400 9 10
6 83:0301 8
(Q28) 8:81788  10
145 10
883 9:12503  10
146 52 10
17 340:506 8 10
12 52:0672 7
(Q48) 5:88682  10
85 10
347 2:66374  10
86 31 10
10 123:292 6

Table 16. Runtimes

curve comput. of φ(Pi) reduction small solut.
(Q24) 3s < 1s 5s
(Q28) 20m 8s 16m 56s 2h 20m
(Q48) 1m 2s 21s 3m 43s

With this taken into account, noting that the LLL-algorithm also provides a lower
bound for this type of d, and using inequality (3), we get a reduced upper bound
M1 for M ,namely

M1 =
 $s 1
c1
 
log (c9C)+ 1
2 c10 + c11 − log q
d2 − rM 2
0 − (rM0 + 1
2 )
%
 .

We have reduction data as in Table 15.
Again it is straightforward to nd all solutions below the reduced bounds (al-
though in the rank 5 case this takes some runtime). This completes the proof.
Finally we give in Table 16 the runtimes on a Pentium 75Mhz personal computer.

4. The case “cubic = cubic”

In this section we prove Theorem B36, and thus also Theorem A36. In order
to do this we develop a variant of the elliptic logarithms method. See also [SW],
where we hope to describe the method for solving any equation of type

s1U 3 + s2U 2V + s3UV 2 + s4V 3 + s5U 2 + s6UV + s7V 2 + s8U + s9V + s10 =0

that represents an elliptic curve. However, here we concentrate on the equation
(C36) only, as a rst example to gain experience with the method.
The birational transformations
( U = 237X+15Y −3375
5X 2+45X−21Y +4860 ,

V = 315X−75Y +17415
5X 2+45X−21Y +4860 ,
 ( X = 45U −75V +300
5U +V ,

Y = 6750U 2+1410V 2+6300U −4740V
(5U +V )2
(4)

relate equation (C36) and the minimal model

Y 2 = X 3 − 1575X + 52650.(W36)

See [N] and [Co, Section 1.4] for an algorithm to compute these transformations.
In Table 17 some data on this elliptic curves are given, namely the minimal
discriminant , the j-invariant j, and the torsion group.
Further we need the rank r,and a basis P1,... ,Pr for the free part of the
Mordell-Weil group. We have the following result.

Table 17. Data of elliptic curve

curve ∆ j torsion
(W36) −947466720000 = −2
8  3
6  5
4  8123 3704400=8123 = 2
4  3
3  5
2  7
3  8123
−1 trivial

1276 ROELOF J. STROEKER AND BENJAMIN M. M. DE WEGER

Table 18. Rank and basis of Mordell-Weil group

curve r P1 P2 P3 P4
(W36) 4 (−15, 270) (15, 180) (45, 270) (−45, 180)

Table 19. Relevant constants on heights of basis points

curve (W36)
B 3.927
H 12.73
runtime 1h 27m

Proposition 3. The elliptic curve (W36) has rank r and basis P1,... ,Pr for the
free part of its Mordell-Weil group as in Table 18.

Proof of Proposition 3. Again we use Cremona's mwrank. No diculties were en-
countered. We give the constants B and H as well as the runtimes on a Sun
Sparcstation 4 in Table 19.

Again note that the basis given is optimal for the least eigenvalue of the Neron-
Tate height pairing matrix.
We consider a point
 P = m1P1 + m2P2 + m3P3 + m4P4

on the curve, with integral coordinates U, V on (C36). We put

M =max
1i4 jmij.

As dV
3U 2 − 1 and dX
Y are two dierential forms on the same elliptic curve, there

should be a rational relationship. Indeed, a bit of calculation (see the birational
transformations (4)) shows that
 dV
3U 2 − 1 = − 15
2 dX
Y .(5)

For (U, V ) 2 R2 on (C36) with V  4, we see that U is a strictly increasing function
of V , and likewise for V −1. See Figure 1.
For each point (U, V ) 2 R
2 on (C36) with V −1or V  4 there is a unique
point (X, Y ) 2 R2 on (W36) with Y  0, given by (4). For a point P on the curve
we use (U, V )=(U (P ),V (P )) and (X, Y )= (X(P ),Y (P )) to denote coordinates
on both models. Let F :(−1, −1] [ [4, 1) −! R be given by

F (v)= 15 3u(v) − 5v +20
5u(v)+ v ,

where u(v) is the unique solution to 15u(v)
3 − 15u(v)= v3 − 4v2 +3v for the given
v.Then X = F (V ).

ELLIPTIC BINOMIAL DIOPHANTINE EQUATIONS 1277

Figure 1. The elliptic curve (C36)

For V  4wehaveby(5) that
Z 1

V
 dV
3U 2 − 1 = 15
2
 Z X

X0
 dX
Y ,(6)

where
 X0 = lim
v!1 F (v)= 15 3 − 5α
5+ α = −15α +3α
2,

for α = 3p
15. Let Q0 =(−15α +3α
2, −90 + 60α
2). Then Q0 2 E(K), where
K = Q(α), a cubic eld, and X0 = X(Q0).
Likewise, for V −1 we have by (5) that
Z V

−1
 dV
3U 2 − 1 = 15
2
 Z X0

X
 dX
Y ,(7)

with X0 as above. Note that αU − V + 4
3 = 0 is the asymptote of the curve (C36);
seeFigure1.
For αU + 4
3 >V  4or αU + 4
3 <V −1we have3U 2 − 1  ( 4
45 α − 1
16  V 2,
so that in the case V  4wehave
Z 1

V
 dV
3U 2 − 1  c Z 1

V
 dV
V 2 = c
V ,(8)

and in the case V −1wehave
Z V

−1
 dV
3U 2 − 1  c Z V

−1
 dV
V 2 = c
−V ,(9)

where c = 4516
64−45 =6.38085 ... .

1278 ROELOF J. STROEKER AND BENJAMIN M. M. DE WEGER

Now consider equation (W36). We have
Z X

X0
 dX
Y = Z X

X0
 dX
pX 3 − 1575X + 52650

= Z 1

X0
 dX
p
X 3 − 1575X + 52650 − Z 1

X
 dX
p
X 3 − 1575X + 52650,

and note that X 2 Q.Further,

φ(P )= φ(m1P1 + m2P2 + m3P3 + m4P4)

= m1φ(P1)+ m2φ(P2)+ m3φ(P3)+ m4φ(P4)+ m0,

with m0 2 Z such that all φ-values are in [0, 1). By (6) it follows in the case V  4
that Z 1

V
 dV
3U 2 − 1 = 15
2
 Z X

X0
 dX
Y = 15
2 (ωφ(Q0) − ωφ(P ))

= 15
2 (ωφ(Q0) − m1ωφ(P1) − ... − m4ωφ(P4) − m0ω) ,
(10)

where ω is the fundamental real period. Similarly, in the case V −1by (7) we
have Z V

−1
 dV
3U 2 − 1 = − 15
2
 Z X

X0
 dX
Y

= 15
2 (−ωφ(Q0)+ m1ωφ(P1)+ ... + m4ωφ(P4)+ m0ω) .

(11)

Put u0 = ωφ(Q0)and ui = ωφ(Pi)for i =1, 2, 3, 4, and let

L(P )= u0 − m1u1 − ... − m4u4 − m0ω.

Then (8), (9), (10) and (11) imply

jL(P )j = 2
15
 Z

I
 dV
3U 2 − 1  2
15 c
jV j ,(12)

with as integration interval I =[V, 1)if V  4, and I =(−1,V ]if V −1.
If V  6then αU <V <αU + 4
3 , and it follows that X< 0. Moreover,

15(−3U +5V − 20) − (5U + V )= 74V − 50U − 300 > 
74 − 50
α
  V − 300 > 0,

so that the numerator 15(−3U +5V − 20) of jXj is larger than the denominator
5U + V .
Similarly, if V −5then αU + 4
3 <V <αU + α, and it follows that X< 0.
Also,

15(3U − 5V + 20) + (5U + V )= −74V +50U + 300 >  50
α − 74 V + 300 > 0,

so that the numerator 15(3U − 5V + 20) of jXj is larger than the denominator
−5U − V .
So if V  6or V −5, then for the Weil height of X we nd

h(X)  log (15j3U − 5V +20j) < log (15 ((
5 − 3
  jV j +sign(V ) ( 4
 − 20

 log (135 − 57
  +log jV j < 4.71750 + log jV j.

(13)
 ELLIPTIC BINOMIAL DIOPHANTINE EQUATIONS 1279

Table 20. Relevant constants

curve (C36)
^h(P1) 0.561125 .. .
^h(P2) 0.566020 .. .
^h(P3) 0.578280 .. .
^h(P4) 0.736397 .. .
^h(Q0) < 5.66238
c1 0.384689 .. .
φ(P1) 0.383460 .. .
φ(P2) 0.298105 .. .
φ(P3) 0.198210 .. .
φ(P4) 0.459223 .. .
 curve (C36)
φ(Q0) 0.392231 .. .
u1 0.600689 .. .
u2 0.466981 .. .
u3 0.310495 .. .
u4 0.719371 .. .
u0 0.614429 .. .
hE 15.1250 ...
D 3
A0 15.1250 ...
 curve (C36)
A1 15.1250 .. .
A2 15.1250 .. .
A3 15.1250 .. .
A4 15.1250 .. .
A0
0 15.1250 .. .
c4 2.79031  10216

c5 2.09861 .. .
c6 17.2236 .. .
M0 1.75995  10114

It is noteworthy that the above formula is the only point in this proof where we
use the fact that U, V are integral.
From Silverman [Sil2] we have

^h(P ) − 1
2 h(X) < 3.87831,(14)

and moreover
 ^h(P )  c1M 2.(15)

Putting everything together, we obtain from (12), (13), (14) and (15), under the
condition V  6or V −5, that

jL(P )j < 2
15 c
jV j <e12:3126−2c1M 2 .(16)

Now we apply David's result [D], and obtain

jL(P )j > exp (−c4(log(4M )+ c5)(log log(4M )+ c6)
7).

Together with (16) this yields an absolute upper bound M0 for M .We have the
data as in Table 20. Note that we used that jm0j 4M .
The reduction procedure runs just as in the previous section for the cases of
(Q28) and (Q48), since the linear form also is inhomogeneous in this case. Thus
the lattice is spanned by the columns of

A =
 0

B
B
B
B
@
 100 0 0
010 0 0
001 0 0
000 1 0
[Cu1][Cu2][Cu3][Cu4][Cω]
 1

C
C
C
C
A ,

and d is the distance between the point

y =(0, 0, 0, 0, −[Cu0])
>

and the nearest lattice point. We have

jλ − CL(P )j 1
2 (4M0 + jm0
0j +1)  4M0 + 1
2 ,

1280 ROELOF J. STROEKER AND BENJAMIN M. M. DE WEGER

Table 21. Data of the reduction steps for (C36)

curve M0 Cd > M1 Cd > M2
(C36) 1.75995  10114 10575 1.12582  10115 37 1013 265.465 6

Table 22. Runtimes

curve comput. of φ(Pi) reduction small solut.
(C36) 4m 38s 2m 44s 9m 19s

and thus, using inequality (16), we reach a reduced upper bound M1 for M ,namely

M1 =
 $s 1
2c1
 
log C +12.3126 − log q
d2 − 4M 2
0 − (4M0 + 1
2 )
%
 .

We have reduction data as in Table 21.
Again it is straightforward to nd all solutions below the reduced bound. This
completes the proof.
Finally we give in Table 22 the runtimes on a Pentium 75Mhz personal computer.

References

[A] `E.T. Avanesov, \Solution of a problem on gurative numbers" (Russian), Acta Arith-
metica 12 [1966/67], 409{420. MR 35:6619
[BC] A. Baker and J. Coates, \Integer points on curves of genus 1", Proc. Camb. Phil. Soc.
67 [1970], 595{602. MR 41:1638
[BH] Yu. F. Bilu and G. Hanrot, \Solving superelliptic Diophantine equations by Baker's
method", Compositio Math. 112 (3) [1998], 223{312.
[Co] I. Connell, The elliptic curve handbook, manuscript, 1997. Available from the ftp site
of McGill University in the directory math.mcgill.ca/pub/ECH1. From the same site the
Apecs package can be downloaded.
[Cr] J.E. Cremona, Algorithms for modular elliptic curves, Cambridge University Press, Cam-
bridge, 1992. MR 93m:11053 The programs mrank, mwrank, ndinf may be downloaded
from John Cremona's ftp site euclid.ex.ac.uk/pub/cremona.
[D] S. David, Minorations de formes lin´eaires de logarithmes elliptiques,Mem. Soc. Math.
France, Vol. 62, 1995. MR 98f:11078
[F] G. Faltings, \Endlichkeitss¨atze f¨ur abelsche Variet¨aten ¨uber Zahlk¨orpern", Invent. Math.
73 [1983], 349{366. MR 85g:11026a
[GPZ] J. Gebel, A. Peth˝o and H.G. Zimmer, \Computing integral points on elliptic curves",
Acta Arithmetica 68 [1994], 171{192. MR 95i:11020
[L] D.A. Lind, \The quadratic eld Q(
p5) and a certain diophantine equation", Fibonacci
Quarterly 6 [1968], 86{93. MR 38:112
[M1] L.J. Mordell, \On the integer solutions of y(y +1) = x(x +1)(x +2)", Paciﬁc Journal
of Mathematics 13 [1963], 1347{1351. MR 27:3590
[M2] L.J. Mordell, Diophantine Equations, Academic Press, London, New York, 1969. MR
40:2600
[N] T. Nagell, \Sur les proprietes arithmetiques des cubiques planes du premier genre", Acta
Mathematica 52 [1928/9], 93{126.
[P] ´A. Pint´er, \A note on the diophantine equation (x
4 = (y
2", Publ. Math. Debrecen 47
[1995], 411{415. MR 96i:11027
[Sik] S. Siksek, \Innite descent on elliptic curves", Rocky Mountain J. Math. 25 [1995], 1501{
1538. MR 97g:11053
[Sil1] J.H. Silverman The arithmetic of elliptic curves, Springer Verlag, Berlin etc., 1986. MR
87g:11070
 ELLIPTIC BINOMIAL DIOPHANTINE EQUATIONS 1281

[Sil2] J.H. Silverman, \The dierence between the Weil height and the canonical height on
elliptic curves", Math. Comput. 55 [1990], 723{743. MR 91d:11063
[Sin] D. Singmaster, \Repeated binomial coecients and Fibonacci numbers", Fibonacci Quar-
terly 13 [1975], 295{298. MR 54:224
[Sm] N.P. Smart,\S-integral points on elliptic curves", Mathematical Proceedings of the Cam-
bridge Philosophical Society 116 [1994], 391{399. MR 95g:11050
[ST1] R.J. Stroeker and N. Tzanakis, \Solving elliptic diophantine equations by estimating
linear forms in elliptic logarithms", Acta Arithmetica 67 [1994], 177{196. MR 95m:11056
[ST2] R.J. Stroeker and N. Tzanakis, \On the Elliptic Logarithm Method for Elliptic Dio-
phantine Equations. Reﬂections and an Improvement", to appear in Experimental Math.
[SW] R.J. Stroeker and B.M.M. de Weger, \Solving Elliptic Diophantine Equations: The
General Cubic Case", submitted to Acta Arithmetica.
[T] N. Tzanakis, \Solving elliptic diophantine equations by estimating linear forms in ellitpic
logarithms. The case of quartic equations", Acta Arithmetica 75 [1996], 165{190. MR
96m:11019
[TW] N. Tzanakis and B.M.M. de Weger, \On the practical solution of the Thue equation",
J. Number Th. 31 [1989], 99{132. MR 90c:11018
[dW1] B.M.M. de Weger, \A binomial diophantine equation", Quarterly Journal of Mathemat-
ics 47 [1996], 221{231. MR 97c:11041
[dW2] B.M.M. de Weger, \Equal binomial coecients: some elementary considerations", Jour-
nal of Number Theory 63 [1997], 373{386. MR 98b:11027

Econometric Institute, Erasmus University Rotterdam, P.O. Box 1738, 3000 DR Rot-
terdam, The Netherlands
E-mail address: stroeker@few.eur.nl

Sportsingel 30, 2924 XN Krimpen aan den ijssel, The Neterlands
E-mail address: deweger@xs4all.nl
