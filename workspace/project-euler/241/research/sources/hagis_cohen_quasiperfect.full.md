<!-- source: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/773348EC71E156E2E460DCC03D55030D/S1446788700018401a.pdf/some-results-concerning-quasiperfect-numbers.pdf | converted from PDF -->

/. Austral. Math. Soc. (Series A) 33 (1982), 275-286

SOME RESULTS CONCERNING
QUASIPERFECT NUMBERS

PETER HAGIS, JR. and GRAEME L. COHEN

(Received June 3, 1981)

Communicated by A. J. van der Poorten

Abstract

New methods are introduced here to show that if n is a quasiperfect number and u(n) the number of
its distinct prime factors, then u(n) > 7 and n > 1035, and if further 3}« then u(n) > 9 and
n > 1O
40.

1980 Mathematics subject classification (Amer. Math. Soc): 10 A 20.

1. Introduction

A positive integer n is said to be quasiperfect (QP) if

(1) o(n) = 2n+l

where, as usual, o(n) is the sum of the positive divisors of n. Although, as yet, no
quasiperfect numbers have been found, several papers have been devoted to a
study of the properties which must be possessed by such numbers (//any exist).
In the sequel n will always denote a quasiperfect number and «(«) will denote the
number of distinct prime factors of n. The following facts have been previously
established:
(A) n — k
2 where k is odd;
(B) if m is a proper divisor of n then a(m) < 2m;
(C) if r | a(n) then r = 1 or 3 (mod8);

Copyright Australian Mathematical Society 1982

275

https://doi.org/10.1017/S1446788700018401 Published online by Cambridge University Press

276 Peter Hagis, Jr. and Graeme L. Cohen [2 ]

(E) if 3 \ n then w(«) > 8;
(F) n > 1020.
(A), (B) and (C) (implicitly) were proved by Cattaneo (1951), (D) is due to
Kishore (1978), and (E) and (F) were proved by Abbott and others (1973).
A result of Dickson (1913) implies that for each t there are only finitely many
QP numbers n with «(«) < t. As pointed out by Pomerance (1975), the method
of Dickson's proof shows this set is effectively computable.
In the present paper we improve (D), (E) and (F) by proving the following
theorems.

THEOREM 1. If n is a quasiperfect number and (15, n) = 1, then u(n) > 15 and
n > 10 "

THEOREM 2. // n is QP and3\n then w(«) > 9 and n > 10
40.

THEOREM 3. If n is QP then u(n) > 7.

THEOREM 4. / / n is QP then n > 10
35.

2. Feasible components

In what follows p and q, with or without subscripts, will always denote odd
primes. With (C) in mind, and recalling that o(n) is multiplicative, we shall say
that "p" is feasible" or " the exponent a is feasible for p " if 2 | a and if no prime
factor of o(p") is congruent to 5 or 7 modulo 8. More generally, I1J=1 pf
1 will be
said to be feasible if at is feasible for pi for 1 *£ / *s j . If p" || n then p" must be
feasible.
Using the CDC CYBER 174 at the Temple University Computing Center, a
search was made for feasible exponents of the odd primes less than 200. The
results appear in Table 1 in Section 8. In this table, /? = /?(/?) is the smallest
exponent whose feasibility for p was not tested. A lower bound V for p? is given
for each prime p in Table 1 and, in parentheses next to each feasible exponent a
of p, the prime factors less than 100 of o(p
a) are listed. For example, /J(89) = 16,
and if 89
a||n and 89" < 10
31 then a = 2, 8 or 10; also, 67 | a(89
10) so a ^ 10 if
67 | n. For p — 19,29,37,..., there is no feasible exponent less than /8( p).
It will be convenient to define /$ — P(p) for each odd prime/; as follows:

DEFINITION 1. If p < 200 then the value of /?(/?) is given in Table 1. If
200 <p < 10 3, then $ = 8; if 10
3 <p < 10 4, then 0 = 6; Up > 104, then 0 = 4.

https://doi.org/10.1017/S1446788700018401 Published online by Cambridge University Press

[3] Quasiperfect numbers 277

It follows that

(2) />-*-• < 10~20

for every odd prime/?.
We shall write 0, for/?(/>,).
A search was also made for all primes between 200 and 2000 for which p
2 is
feasible. List 1 consists of all such primes for which p = 2 (mod 3), and List 2
consists of all such primes for which p = 1 (mod 3). Further, List 3 contains all
primes such that p
A is feasible where 200 < p < 2000. In each list (given in
Section 8) all q such that q \ o(p") and 11 < q < 100 are enclosed in parentheses
next to p.

REMARK 1. We did not checkp" for feasibility if either/? > 2000 or if a > 6 and
200 < p < 2000. In what follows, if the feasibility of p
a is unknown to us we will
treat p" as if it were feasible whenever 2 | a and a < P(p) (see Definition 1). We
note, however, that if 3 | n and p = 1 (mod3) then we cannot have p
2\\n, since
(from (1)) n and o{p
a) are relatively prime whenever p
a\\n.

REMARK 2. Our lists considerably extend (and amend) lists in Abbott and
others (1973), Lemma 4A. The lists given there were constructed on the basis of
congruence arguments (for example, p
2ftn when /? = 2 or 4 (mod 7)). More
information than we require here is contained in our lists, but they should prove
useful to others working with quasiperfect numbers.

3. Two important lemmas

Our next objective is to prove two lemmas which will be very useful in the
remaining sections of this paper. For convenience we first introduce the notation
h(k) = a(k)/k, where k is a positive integer. h(k) is multiplicative, h(p'
x) —
\ima^xh(p
a) = p/(p- 1); and it is easy to see that 1 < h(p") < h(p
h) if
0 < a < b < oo, and h(p
a) < h(qb) if p > q and 0=£a<oo, l<fc<oo . (See
Section 1.3 in Pomerance (1974).)
From (1) and (F) we see that

(3) 2<h(n)<2+ 10- 20 = 2*,

from which it follows that

(4) II/7'(/>-l)
p\n p\n

https://doi.org/10.1017/S1446788700018401 Published online by Cambridge University Press

278 Peter Hagis, Jr. and Graeme L. Cohen (41

LEMMA 1. Suppose that n is QP and n =  I[sl=, p?>H'j=, qp = MN where (M, N)
= 1, s > 1, t > 1. Let B =  2*/h(M') where M' = II*=1 />,
c< with 2 < c, < a,, and
let D = h(M")/2 where M" = Usi=xp?; with at < d,•< oo. Suppose also that

qt<q2< ••• <qr Then:

(i)

(ii)

PROOF. Suppose that ^, < (^45 - 3 + l)/2(5 - 1). Then it is an algebraic
exercise to verify that (\/qx + 1/2) 2 >B - 3/4 so that 1 + ^rj"
1 + q{2 > B.
Using (3) and (A) we see that

2*>h(n) = h(M) • h(N)>h(M') • h(q
2x)

= 2*B- l(l + q? + q\ 2) ^ 2*B
lB = 2*.

This contradiction proves (i). Now assume that qx >  (1 — D1/')"
1. Then
qx/(qx - 1) < r>"
1/( so that

2 < *(n) = h(M) • A(7V) < h(M) 11 /  >

7= 1

< A(A/") • {q xf (qx - 1))' < h(M")(D-
l/')' = 2DD^ = 2.

This contradiction proves (ii).

LEMMA 2. Suppose n is QP, and write n = Np", where p \ N. Write also

t
(5) ^ = -^11 ^ where qj\M,

7= 1

{(6) F=h(M){[qJ(qJ-\), £=2^"' .

7= 1 7= 1
(7) R = 2/(2- F), and

L = R- 2FU/ (2 - F)(2 - F + FU),

where U is any upper bound for E. If F < 2, then

(8) L-p
l ^p<R.

Further, if q < p are the two largest prime factors ofn, then

(9) L' = L- (L- (q + 2)~
1)'
1 <p<R.

PROOF. According to Jerrard and Temperley (1973), Proposition 3,

2/ (2 - h(N)) -p

https://doi.org/10.1017/S1446788700018401 Published online by Cambridge University Press

[51 Quasiperfect numbers 279

and, as shown by Pomerance (1974), Section 1.5,

(10) F- FE<h(N)^F.

Therefore, when F < 2,

2/ (2 - F ) - 2 / (2 - h(N)) < 2 / (2 - F ) - 2 / (2 - F + F£ )

= 2FF / (2 - F)(2 - F + FE)

*£ 2FU/ (2 - F)(2 - F + FU),
since E <  U and x/(c + x) is monotonic increasing when c > 0, and (8) follows.
Then /> > L - (q + 2)~" and (9) also follows.

4. The proof of Theorem 1

If(«, 15)= 1 and«(n)< 14 then, since h(p
a) < h{p
x) = p/(p - 1),

59

p\n P~7

Hence, «(« ) s* 15; and n 3= (7 • 17 • 31 • 41 • 71 • 73 • 89 • 97 • 103 • 127 • 167 •
199 • 223 • 239 • 241)2 > 1057, since 13
6 > 234 > 2412. (See Table 1 and Lists 1,
2,3.)
 5. The proof of Theorem 2

We shall prove here only the second part of the theorem, since our method for
showing that «(« ) 3= 9 when 3 \ n is similar to that used in the proof of Theorem
3, and requires less computing. Full details of the proof are available from either
of the authors.
By Theorem 1, if (15, n) — 1 then n >  1057. Therefore, in the remainder of this
section we assume that 3 \ n and 5 | n. If n is divisible by 11, 19 or 29 then (see
Table 1) n > 56 • 11
16(7 • 17 • 31 • 41 • 71 • 73 • 89)2 > 1042. Therefore, we may
assume that (11 • 19 • 29, n) -\.UU\n then u(n) > 14  since Vtf=ip/(p - 1)
• (10/ll)(12/13)(18/19)(28/29)< 2; and if 13 | n then w(n)>l l since
II^L5jp/(/? — 1) - (10/11)(18/19)(28/29) < 2. It follows easily that n > 5 6 •
13
6(7 • 17 • 31 • 41 • 71 • 73 • 89 • 97 • 103)
2 > 1040.

6. The proof of Theorem 3

By (D) we need only prove that u(n) ¥=  6. We suppose, therefore, that
n = nf=] p"' where px < p 2 <  • • • < p 6. By Theorem 2, pt — 3 and since
(3/2)Uf=np/(p - 1) < 2 we see that 5 </>2 < 11. If p2 = 5  then, by Lemma 1

https://doi.org/10.1017/S1446788700018401 Published online by Cambridge University Press

280 Peter Hagis, Jr. and Graeme L. Cohen (61

with M' = 3456, we have/>3 > 17; and since O/2)(5/4)HlL59p/(p - 1) < 2 we
see that p3 < 53. If />2 = 7 then, since (3/2)(7/6) II *L29/>/(/> ~ 1) < 2, we see
that 11 «/?3 < 23. Ifp2 = 11 then 13 </>3 < 17 since

31

p=l9

A computer program utilizing double precision arithmetic was written which for
each feasible value of M — p°'p£
2p°
3 used Lemma 1 to find upper and lower
bounds for p4. For at < /J, (see Definition 1 and Table 1) we took c, = a, in M'
and dj = at in M", while for a, 3= /?, we took c, = /?, in M' and d{ = oo in M".
Thus, the infinite set of M's was investigated by examining the elements of a
finite set. For example, it was found that 127 </?4 < 761 for /?, = 3, p2 = 5,
/>3 = 17. The program then used Lemma 1 to find bounds onp5 for each feasible
value of M — p
a^P2
2P"
lPt'- (We included p\ and p\ as possible factors of M but
did not check for feasibility if pA > 200. See Remark 1. No p4 exceeded 761.)
Since « = II?=,/>,a' we can write (see (5)) n — p£
6N = p%*M\l'j=lqp where
/>, | M if a, < 0, and pi = q} for somej if a, > /?,. From (2), £ = TJ=, ^"^" ' < f •
10"
20 < 5 • 10 "
20 = U. The program calculated F (which was always less than 2),
as given by (6), for all possible values of M and <?,,... ,q, as determined by the
values of /?,, p2,... ,p5 previously found and the exponents implied by Definition
1 and Remark 1. (For example, if p5 > 10000 and p5 = 2 (mod 3) then either
p\ || M or p5 = qr) Also, R and L' (with q = p5), as defined in (7) and (9), were
calculated in order to determine/?6. For only 12 quintets (/>,, p2, p3, p4, p5) did
R and L' span a prime, thus yielding a (possible) value of p6. The (possible) prime
factors of a six component quasiperfect number are given in Table 2.

TABLE 2

Pi
3
3
3
3
3
3
3
3
3
3
3
3
 Pi
5
5
5
5
5
5
5
7
7
7
7
11
 Pi
17
17
17
19
19
23
43
11
11
11
13
13
 PA
257
337
571
151
197
59
59
37
47
71
41
23
 Ps
65537
1709
743
503
347
193
67
103
107
79
43
29
 Pe
4294427569
1783
983
541
401
521
113
191
137
89
107
31

https://doi.org/10.1017/S1446788700018401 Published online by Cambridge University Press

[7) Quasiperfect numbers 28 1

We now write n — II f= \ pf' = m Wj= t qp where /?, | m if a, < /?, and p t = qj for
somey if a, > /?,. For all possible values of m and q{,...,q, as determined by the
values of />, given in Table 2 and the exponents implied by Definition 1 and
Remark 1, h(m)I['j=lqJ/(qj — 1) was calculated and h(n) was then bounded
using (10). In every case either h(n) < 2 or h(n) > 2 + 10"
20. This contradiction
to (3) completes the proof of Theorem 3.

7. The proof of Theorem 4

Theorem 4 is proved by establishing the twenty facts below. Only eight of these
are proved here; the details of the remaining proofs are available from either of
the authors. Notice first that, by Theorem 2, if 3 \ n then n >  1040, so that we may
assume that 3 | «. We shall use:

LEMMA 3 . Suppose that n is QP and 3\n. Then there is an even number of
components q b of n with q = b = 1 (mod 3).

PROOF. From (1), and since 3 | n, a(n) =  1 (mod 3). Then there must b e an
even number of components q h of n with a(q h) =  2 (mod 3). If qb is such a
component, then q ¥=  3 and q z 2 (mod 3) since b is even, by (A). Thus q = 1
(mod3), so a(q b) =  b+\=2 (mod  3). Thus b =  1 (mod3). This proves the
lemma.

I. Ifp
a\\nandp
a >  II
16 then n >  1035.

PROOF. Since the six smallest possible components of n are 3
4 < 172 < 412 < 74

< 712 < 892 (see Table 1) it follows that n >  347411I6(17 • 41 • 71 • 89)2 > 1035.

II. IfS = {11, 19, 29, 37, 53, 59, 73, 97, 101, 113, 131, 137, 157, 163, 173, 181,

191, 197, 199} andp \ n where p E S, then n >  10 35 . If 43-47 \n then n > 10 35 .

PROOF. This follows immediately from I and an examination of Table 1.

III. Ifu(n)> \0thenn> 10
35.

PROOF. If «(«) > 10 then n > 3 45674(17 • 41 • 71 • 89 • 167 • 239 • 311)2 >
10
36.

We assume hereafter that/7 £ 5 if p \ n, that 43 • 471 n and that u(n) = 7, 8 or
9.

https://doi.org/10.1017/S1446788700018401 Published online by Cambridge University Press

282 Peter Hagis, Jr. and Graeme L. Cohen [8]

IV. If (n, 35)= 1 thenn> 1035.

PROOF. Assume that (n,35)=l . If 13 \n then, since «(« ) < 9, h(n) <
(3/2)(17/16)(23/22)(31/30)(41/40)(43/42)(61/60)(67/66)(71/70) < 2 which
contradicts (3). If 13 | n then w(«) = 9 since

(3/2)(13/12)(17/16)(23/22)(31/30)(41/40)(43/42)(61/60) < 2,

so n s* 34136(17 • 41 • 71 • 89 • 167 • 239 • 311)2 > 1036.

We may now assume that 5 | n or 7 | n. (Notice that 5 • 7 \ n since /J(34 5 6 7 4 ) >
2*. See Lemma 4B in Abbott and others (1973).)

M.If3
1%\nthenn> 1035.

From Table 1 we may now assume that 3
4 II n or 312 II n.
It will be convenient for what follows to now make the following definition.

DEFINITION 2. The positive integer s will be said to be satisfactory if s =  3"q
yn
2

where: (i) a = 4 or 12; (ii) q = 5 or 7; (iii) ju has no prime factor belonging to S or
{2,3,5,7};  (iv) p =  1 (mod3) implies that p
2fts; (v) «(s ) = 7, 8 or 9; (vi)
2<h(s)<2*.

We see immediately that if n is Q.P and n < 1035 then n is satisfactory.

VI. If5
l6\nthenn> 10
35.

PROOF. If 516 | n then, from Table 1, either 5l6||w or 522 | n. In the latter case
n s* 3
4522(17 • 41 • 71 • 89 • 167)
2 > 1035. Now suppose that 312||n. If 17 fn then
n >  3I2516(41 • 71 • 89 • 167 • 239)2 > 1036. If 17 | n then, by Lemma 1 with M'
= 312516172, p\n if 17 <p < 251. Therefore, n 3* 312516(17 • 311 • 353 • 383 •
449) 2> 1039. We can now assume that 3
4516 II n. Since a(3
4) = 121 and 409 | a(5
16)
we see from (1) that n = 60 (mod 121) and n = 204 (mod 409). Let n = 34516x2

and suppose that n < 1035. Then it is easy to verify that 53x
2 = 60 (mod 121) and
98.x
2 = 204 (mod 409). These congruences have four positive simultaneous solu-
tions less than m = 121 • 409, namely, x, = 7343, x2 =  22105, x3 — 27384, x4 =
42146. These were found using the Chinese Remainder Theorem. For i — 1,2,3,4
and 0 < k < [10 175/3 25 8w] = 1817560 the integers n(i, k) = 34516(x, + km)
2

were decomposed as necessary into their prime factors. No satisfactory values of
«(/, k) were found. We conclude that if 34516 II n then n > 1O
35.
We may now assume, using Table 1, that 5
6 II n if 5 | n.

https://doi.org/10.1017/S1446788700018401 Published online by Cambridge University Press

[91 Quasiperfect numbers 283

VII. If3
]256\\nthenn> 1035.

VIII. Ifl
n\rtthenn> 1035.

IX. Ifl
w\\nthenn> 1O
35.

X. If3
nl*\\nthenn> 1O
35.

We may now assume that either 3456||« or 3 47 4||«.

XI. If23
w\nthenn> 10
35.

PROOF. If 5 | n then by Lemma 1, with NT =  34562310, (17 • 41, n) =  1. There-
fore, n 3= 34562310(71 • 89 • 167 • 239)2 > 1036. If 7 4||« it is easy to verify, using
Lemma 3 and Table 1, that n > 1O
35 unless 43
4||«. If 17 \n then n^
34742310434(41 • 71 • 89)2 > 1036. If 171 n then by Lemma 1, with M' =
34741722310434, (41 • 71 • 89, n) = 1. In that case, n ^ 347423'°43
4(17 • 167 •
239)2 > 1037.

From this and Table 1 we may now assume that if 23 | n then 23
4||n.

XII. If I7
io\ n then n>  1O
35.

XIII. If 5 • \l\nthenn> 1035.

Henceforth we may assume that 17 \ n if 5 | n.

XIV. If5p\n, where p = 23, 31 or 43, then n >  1035.

PROOF. By XI, I and Table 1 we may assume that 3
456234||n or 3456316||« or
3456434||«. Let n = 3
45
tp
2ax
2 where p2a =  234, 31 6 or 43
4 and suppose that
n <  1035. From (1) we see that 86(/>
ax)2 = 60 (mod 121) and \5M\(p
ax)
2 =
9765 (mod 19531). The four common incongruent solutions of these congruences
are Xl = 264434(pa)~\ X2 =  341027(/?
a)-', X3 =  2022224(/7a)"
1) X4 =
2098817(p
a)-' where >>"' is the reciprocal of y modulo m =  121 • 19531. For
< = 1,2,3,4 let x: =  xt{pa) be the least positive residue of A", modulo m. Also, let
K = K(pa) =  [\O]T5/3
25
3p
am]. Then K(23
2) =  224844, K(3\
3) = 3992 and
AT(43
2) = 64328. For / = 1,2,3,4 and 0 < k < K the integers n(i,k,p
a) =
3*5
6p
2a(xi + km)2 =  3
45
6p
2afi
2 were decomposed as necessary into their prime
factors (unless p | ju). N o satisfactory value of n(i, k, p") was found.

https://doi.org/10.1017/S1446788700018401 Published online by Cambridge University Press

284 Peter Hagis, Jr. and Graeme L. Cohen [ 10]

XV. 7/5 -4\\nthenn> 10
35.

XVI. / / 5 | n then n >  1035.

XVII. 7/7 -231/1 thenn> 1O
35.

XVIII. 7/7 • 13/71 n, where p = 41 or 43, then n > 1035.

XIX. 7/7 • \lp | n, w/im>/> = 31 or 41, tfie« « > 1035.

XX.If7\nthenn> 1O
35.

PROOF. We may assume that 34741| n, and by XVII we may suppose that 23 {n.
Since /i(3
474136172) > 2* we see that 13 • 171«. Let n = 3
47
413
c17
rf7>
2 where
c = 0 or 6 and d = 0, 2 or 8. By Lemma 3, q
lb\\n where q > 17, q = 1 (mod3),
& > 1 and £ =?*= 3. If c = d  — 0, then, since

(3/2)(7/6)(31/30)(41/40)(43/42)(61/60)(67/66)(71/70) < 2,

w(/i) = 9 an d « ^ 3474434(41 • 71 • 89 • 167 • 239 • 311)2 > 1036. If 17 j n then
by XIX, we may assume that (31 • 41, n) =  1. Since

(3/2)(7/6)(17/16)(43/42)(61/60)(67/66)(71/70) < 2

we see that «(n) = 8 or 9. Since 3
474172(43 • 67 • 79)4(71 • 89)2 > 1036 we may
assume that at most two prime factors q > 17 of n have exponents greater than 2.
If <?V | n where q andp exceed 17 then n 3= 3
474172434616(71 • 89 • 167)
2 > 1037.
Otherwise,
 h(n) <  (121/81)(7/6)(17/16)(43/42)(67/66)
X (71/70)(89/88)(167/166)(239/238) < 2.

Now suppose that 13 | n. Then, by XVIII, we may assume that (41 • 43, n) — 1. If

/>6||H for p > 13 then n >  3474136316674712892 > 1035. Therefore, we may as-
sume (see I) that (31 • 47 • 61, n) — 1, and since

(121/81)(7/6)(13/12)(67/66)(71/70)(79/78)(83/82) < 2

it follows that w(/i) > 8. Then, n >  3474136674(71 • 89 • 167 • 239)2 > 1036.

Theorem 4 now follows from IV, XVI and XX.

https://doi.org/10.1017/S1446788700018401 Published online by Cambridge University Press

[Ill Quasiperfect numbers

8. Tables
 285

TABLE 1

Feasible exponents a for primes p < 200 if p" is a component of a quasiperfect
number. For each p, p" < V < p& where P need not be feasible. Prime factors
< 100 of a( p") are given in parentheses next to a. (See Section 2.)

p
3

7

13

19

29

37

43

53

61

71

79

89

101

107

113

131

139

151

163
173

181

193

199
 a

4(11),  12,28(59),
40(83)

2(3,19),  4,  10,
12, 16,  18

6

4, 12
6

2

4,6

2,8(73),  10(11,67)
 4

4(41)

6

2(3)
 P
52

28

40

16

22

30

24

30

30

12

18

16

30

12

10

16

12

12

12
16

16

16

10
 V

1024

1023

1044

1020

1032

1047

1039

10
51

1O
53

1022

1034

10
31

, 06O

1024

1020

1O
33

1025

1026

1026

1035

1036

1036

1022
 P
5

11

17

23

31

41

47

59

67

73

83

97

103

109

127

137

149

157

167
179

191

197
 a

6,  16,  22

16

2,8(19),  10

4, 10(11),  12

2(3),  6

2

6(43),  10

4

2(3)

4

2(3), 8(3),  10(89)

2(3),  4(11)

6

2(3),  4

6

2,8

4(11)"to
40

28

26

18

16

16

16

12

24

16

12

16

16

16

12

10

16

16

10
12

10

16
 V

1027

1029

10
31

1024

1023

1025

1026

10
21

1043

1029

1023

10
31

1032

1032

10"

10
21

1034

1035

1022

1027

1022

1036

LIST 1. Primes p such that p
2 is feasible where p = 2 (mod3) and 200 <p <
2000. Prime factors < 100 of a(p
2) are given in parentheses next top. 239(19),
311(19), 353(19), 383, 449(97), 479(43), 593, 617(97), 647, 743, 761, 839, 857,
881(19), 911, 1097, 1151(19), 1193, 1217, 1223(19), 1487, 1559, 1583, 1847,
1889(73).

https://doi.org/10.1017/S1446788700018401 Published online by Cambridge University Press

286 Peter Hagis, Jr. and Graeme L. Cohen [12]

LIST 2. Primes p such that p
2 is feasible where p = 1 (mod 3) and 200 < p <
2000. Prime factors (other than 3) < 100 of a(p
2) are given in parentheses next to
p. 223, 241, 271, 337(43), 409, 463(19), 577(19), 631, 673, 727, 937, 967(67), 1039,
1063, 1249(73), 1447, 1489(19), 1567, 1609, 1657, 1753, 1879, 1993.

LIST 3. Primes p such that p
A is feasible where 200 < p < 2000. Prime factors
< 100 of o(p
4) are given in parentheses next to p. 227, 239, 263, 359, 367(11),
379(11,41), 439, 443(11), 463, 479, 503, 523, 563, 587(11), 643(11), 647(11),
719(11), 727, 887, 919, 967, 983(11), 1063, 1103(11,41), 1123(41), 1187, 1223,
1259(11), 1327, 1439(11), 1487, 1499(11), 1579, 1627, 1663, 1699(11,41), 1759(41),
1787(11), 1847, 1879(11), 1979, 1987.

References

H. L. Abbott, C. E. Aull, Ezra Brown and D. Suryanarayana (1973), 'Quasiperfect numbers', Ada
Arith. 22, 439-447; (1976), 'Corrections to the paper "Quasiperfect numbers'", Ada Arith. 29,
427-428.
Paolo Cattaneo (1951), 'Sui numeri quasiperfetti', Boll. Un. Mat. Ital. (3) 6, 59-62.
L. Dickson (1913), 'Finiteness of the odd perfect and primitive abundant numbers with n distinct
prime factors', Amer. J. Math. 35, 413-422.
R. P. Jerrard and Nicholas Temperley (1973), 'Almost perfect numbers', Math. Mag. 46, 84-87.
Masao Kishore (1978), 'Odd integers N with five distinct prime factors for which 2 — 10~
12 <
o(N)/N < 2 + 10"'
2', Math. Comp. 32, 303-309.
C. Pomerance (1974), 'Odd perfect numbers are divisible by at least seven distinct primes', Ada Arith.
25, 265-300.
C. Pomerance (1975), 'The second largest prime factor of an odd perfect number'. Math. Comp. 29,
914-921.

Department of Mathematics
Temple University
Philadelphia, Pennsylvania 19122
U.S.A.
 School of Mathematical Sciences
The New South Wales Institute
of Technology
Broadway, New South Wales 2007
Australia

https://doi.org/10.1017/S1446788700018401 Published online by Cambridge University Press
