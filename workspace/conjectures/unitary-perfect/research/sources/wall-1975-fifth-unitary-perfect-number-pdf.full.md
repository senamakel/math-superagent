<!-- source: https://www.cambridge.org/core/services/aop-cambridge-core/content/view/B1919CB85AE1D97A7BAD3842B6E2AFB4/S000843950006598Xa.pdf/the-fifth-unitary-perfect-number.pdf | converted from PDF -->

Canad. Math. Bull. Vol. 18 (1), 1975

THE FIFTH UNITARY PERFECT NUMBER

BY
CHARLES R. WALL

1. Introduction. A  divisor d of a positive integer « is a unitary divisor if d and
njd are relatively prime. An integer is said to be unitary perfect if it equals the sum
of its proper unitary divisors. Subbarao and Warren [2] gave the first four
unitary perfect numbers: 6, 60, 90 and 87360. In 1969,1 reported [3] that

146 361 946 186 458 562 560 000

= 2
183 • 5
47 • 11 • 13 • 19 • 37 • 79 • 109 • 157 • 313

is also unitary perfect. The purpose of this paper is to show that this last number,
which for brevity we denote by W9 is indeed the next unitary perfect number
after 87360.
If d is a unitary divisor of n, we write d\\n; note that this notation is consistent
with the standard notation for exact division by prime powers. Let o*(ri) be the
sum of all unitary divisors of n :  <r*(n) = 2 *
d\\n
It is easy to show that a* is a multiplicative function, and in fact

cr*(pV-- 0 =  (l+P a )(l+^)"- ,

where p, q,... are distinct primes and the exponents are positive. We remark that
o*(ri) is odd only for n=l and n any power of 2.
Ifp and q are distinct primes, and/? | n but qjfn, then

(1) <**(pri)lpn <  o**(n)/n <  a*(qn)[qn.

Thus the value o*(ri)jn decreases as the primes dividing n are repeated, so if we wish
to maximize o*(ri)jn and at the same time minimize n, we must take n squarefree.
The requirement that N  be unitary perfect is clearly equivalent to o*(N)=2N.
Thus the search for unitary perfect numbers is the search for solutions to the Dio-
phantine equation

(2) 2 = £±1.Z±1.... ;
x y

with the restriction that x, y .. . are powers of distinct primes. If iVis unitary per-
fect and N=2
Ak with k odd, then as a consequence of (2), the number of distinct
prime divisors of A: is no more than A + l.

Received by the editors March 2, 1971 and, in revised form, October 24, 1973.
115

https://doi.org/10.4153/CMB-1975-021-9 Published online by Cambridge University Press

116  C. R. WALL  [April

For the remainder of this paper we assume that N is unitary perfect, that N< JV>
and that 2
A \\ N.

2. Elimination methods. Subbarao [1] has reported the impossibility of having
A be 0, 3, 4, 5, 7, 8, 9 or 10, and that

if ,4 = 1, then N=6 or 90;
if ,4=2, theniV=60;
if A=6, then N= 87360.

Thus we may restrict our attention here to ,4>11. Since o*(2
A)=l+2
A
9 we may
write 7V=2^(l+2^)<iwith d>\. Then N<> ^requires ^<38 , since J^<(3/2)1023.
The simplest way to eliminate a case is to show:

(3) N has enough known (or assumed) divisors to require that N > W.

Our basic procedure is to start with a given value for A; then o*(2
A)=\+2
A

provides us with some known divisors of N. We then sort the known (or assumed)
divisors into two categories: known (or assumed) unitary divisors, and other
known (or assumed) divisors. We let p be some prime, usually the largest, in the
latter category; then use of (3) allows us to obtain an upper bound on how many
times p can divide N. Once we have this bound we may consider cases in which
p
e || N; then a*(p
e)=l+p
e in general provides us with other known odd divisors
of N, and we repeat the procedure.
We write
 N = 2
A3
B5
cs,

with (s, 30)=1. If A^ll, B>3 and C>3 , then

2 = cr*(N)/N < (2049/2048)(28/27)(126/125)tf*(5)/5,

so that a*(s)js>l.9l. If s is the product of the primes from 7 through 59, inclusive,
then o*(s)js<l.90. Thus by the remarks following (1), s can be no smaller than
the product of the primes from 7 through 61, but this would imply

N > 2n3353s > 10
28.

Since 28/27> 126/125>1, the same lower bound for a*(s)ls also holds if B=C=0,
if B=0 and C>3 , or if B>3 and C=0 . However, each of these conditions implies
that iV>1024. Therefore:

(4) For A > 11 we have (N, 15) > 1, and if 33 | TV then either 5 || N or 521| N,
and if 531 N then either 3 || N or 321| N.

For brevity we let f(N)=sa*(N)/N.
If p
e || N then we have a contradiction if f(N) has more then e factors p in its
numerator. In the table in the next section we refer to this occurrence as "excesses."

https://doi.org/10.4153/CMB-1975-021-9 Published online by Cambridge University Press

1975]  FIFTH UNITARY PERFECT NUMBER  117

(5) The known unitary divisors of N determine other divisors of N because of
odd primes appearing in the numerator off(N). Let m be the largest known
odd unitary divisor of N, and let n be the largest known odd divisor of N
such that (n, m) = 1. Suppose 2
a || a*(m) and that n has b distinct prime
divisors. Let/ be defined by a+b+j=A+l, and let r be the product of the
first j primes not dividing 2mn. Then we have a contradiction if
f(2Am)f(n)f(r) < 2.

The remaining remarks in this section refer to the portion of the proof which
was done by computer [the steps could just as well be done by hand]. Let A be
fixed, let N=2
Ak with k odd, and let/? be the largest prime dividing a*(2
A)=l+2
A.
For 11<^<38 , p || (\+2A) by observation. If we assume/?* | N, then/?6-11 k,
so the unitary divisors of k must include enough odd prime powers to con-
tribute e—l factors p to the numerator off(N), and the product of these prime
powers is at least 2/?6-1—1. Therefore:

(6) We have a contradiction if p
e | N and 2Ape(2pe-1-l)>W. [Done by
computer.]
If/? || N, let q be the largest prime divisor of o**(/?)=/?+l. Then:

(7) We have a contradiction if 2
Apq > W. [Done by computer.]

3. Table of cases. The computer program immediately eliminates the cases
^4=28, A=29 and 31 <^4<38 by (7). The following table lists the remaining cases,
with the reason for eliminating the case if other than (3). Brackets are used in
conjunction with (4) to indicate for clarity the known powers of 3 and 5 which
divide N.
As a convenience, we use the following notation: if/?
6 is a prime power, we let
*/?
6 denote the product of/?6 and the largest odd unitary divisor of o*(p
e)=l+p
e.
For example, since <r*(59)=2
23 • 5, *59=3 -5-59 .

4. Special cases. In this section we take care of the cases left open in the pre-
vious section.

(8) If A = 11, the only possible case requires 2n683 || TV and 3
319 | N. However,
/(2 n683) = 3
319/2
9 =/(2 9). If there were an integer m with (2 • 683, m) = 1
and 2n683m unitary perfect, then 2
9m would be unitary perfect, which
cannot occur.

(9) We write N = 2
12241 • 11
47321 • 523 • 131 • m, where 3 • 7 • 17 | m. If 17 ||
m, then 3
37 • 17 | m; otherwise 3 • 7 • 17
21 m. Since N < W, m < 20189.
The only possible values for m are 3213, 6069, 16065 and 18207, but each
leaves an excess 11 in the denominator off(N).

(10) The case 2
12241 • 11
261 • 31 || N is impossible since

/(212241 • 11
261 • 31) = 17/16 =/(2 4 )

and A = 4 is impossible. The reasoning is similar to that in (8).

https://doi.org/10.4153/CMB-1975-021-9 Published online by Cambridge University Press

118

Table 1.
 Unitary Divisors

211

2 n683 3

2 n683 2

2n683246649
2U683246649 • 3 2

2n683246649-32311
2 n683
212

2 i2 2 4i 4
2122413

21224138263
21224P
21224122572

2122412257
2 1224P257-113 2

2 1224P257-113
2 1224P257-113-43 2

2122412257 • 113 • 43237
2 1224P257-113-43

2i2 24i 2257. H 3 . 43 . 19s
2 1224P257-113 -43-1 9
2 12241 2257-113-43-19
2 12 24P257-113-43-1 9
212241
2 12241-11 8

212241 -ll 7

212241 -ll 6

2 12241-11 5

212241 • 11613421

2 i2 2 4 i -H *
212241 -1147321
2 12241-ll 47321-523
 •172

•17

212241 • 1147321 -523-131
212241 • M35
212241 • ll 3

212241 -ll 2

212241 • 112613

212241 -112613523
212241 • 112613523 • 131

2i2 24i .1P61 2

212241 -1126121861
212241 -1126121861 -19
2 12241-1P6P1861 -19 -
212241 -1P6P1861-19 -
212241 -1126121861 -19 -
212241 -1P6 1
212241 -11261 -31 3

212241 -11261 -31 2

212241 • 11261 -3P481
212241 -1P6 1 -31
 17
I7.7 2
17 • 7253
 C. R. WALL

Other Divisors

3 • 6834

3319 • (1552692 or *155269)
3 • 5 • (466493 or *466492)
3353 [3253 k nown ]
5 4 -(31Po r *31P)

3319 see
17-241 5

17 • 1686701281
7-17-(I P or *lP)-8263 2

7-17-lP-(1033 2 o r *1033)
17 • 113 • (2575 or *2574 or *2573/241)
5 2 17-113-(132Po r *1321)
3-17-43-(113 5 o r *1134or *1133)
3 -5 - 17-43 • (12772or *1277)
3217 • 19 • (435 or *434 or *433)
325217 • 19 • 372

325217 . 192
3211 -17 - (19 5or *19 4or *193)
3211 -17-(18Po r *181)
3 2 5-l l • (17 4or *173)
325211 .(29 2 o r *29)
3 4 5-l l
(172 or *17)(1115 or *ll e , 9 < e < 14)
1726304673
3 • 17 • (162393P or *1623931)
13 • 17 • (61» or *61)(11172 or *1117)
3 • 17 • (1342P or *1342P)
3 • 17 • (22372 or *2237)
(172 or *17)(732P or *732P)
7 • (172 or *17)(5233 or *5232)
7 • (172 or *17) • 13P
3-7-1 7 see
3317 • 37
3217 • 37 • 52 (or A^ prime to 5)
17 • (6 P or *6P or *61 6 or *615/11 or
7 • (172 or *17) • 31 • 5232

7-17-3 1 -13 P

(172 or *17)(186P or *186P)
(73 o r * 7 2)(i 7 2 o r *i7)(i 9 3 o r *i 9 2 )
(52 or *5)(73 or *72)(173 or *172)
(33 or *32)(52 or *5)(74 or *73)
32 • (55 or *5
4)
34

(172 or *17)(3P or *3P for 4 < e < 1]
7217 • 19
17 • (4814 or *48P/241 or *48P)
 see (
 [Aprii

Elimination
if not (3)

(6)

(4)

excess 3's
(8) in next section
(6)

(5)

(9) in next section
(5)
(5)
*614)
 excess 11's

(4)
)
 excess 241's
10) in next section

https://doi.org/10.4153/CMB-1975-021-9 Published online by Cambridge University Press

1975]  FIFTH UNITARY PERFECT NUMBER  119

Table 1. contd.

Unitary Divisors  Other Divisors  Elimination
if not (3)

6832

683

213

213

2 i3 2 73 i 2

2132731
2132731 -
2132731 •
214

214

2 i4n 3 3

21411334219
2141132

21411321277

21411321277-29
214113
214113
214113
214113
214113
 29
4

293

2935219
29352

29
2

2924212

292421
292421 -211 2

292421 -211
292421-211 -53
292421 -211 -53-1 9
292421 -211-5 3
29
29 • 3253

29-3 2

29 • 5232

29 • 5219
52 29

214113
214113
214113
214113
214113
214113
214113
214113
214113
214113
214113
214113
214113
214113
215

2 i5 33 i 3

2153312

21533121889
21533121889 • 29
2 15331 21889-29-5 2

2 15331 21889-29-5 213-7
21533121889 • 29 • 5213
215331
215331 • 833

215331 • 832

215331 • 832532

215331 • 83253
215331 • 83253 • 52
 19-52
 3 • 2731
4

3 • 5092195973
3 • (3729181
2 or *3729181)
3 • (6836 or *6835 or *6834 or *6833)
3 • 5 • (466492 or *46649)
3319 see (11)
5-29-113 6

5-(29 2 o r *29)(*1135or *113
4)
3
25 • 19 • 29 • (42193 or *42192)
325219 • (292 or *29)(2112 or *211)
5229 • (12774 or *12773 or *12772)
(33 or *32)(53 or *52)(712 or *71)
• (294 or *293 or *292)
3353 [known]
3 • 5 • 19 • (2910 or *29e for 5 < e < 9)
3 • 5 • 19 • (3536412 or *353641)
3353 [3352 known]

3313 • (193 or *192)(2712 or 271 -17- 9
or 271 • 17
2)
3 • 5 • 19 • (4215 or *4214 or *421
3)
3 • 5 • 13 • 17 • 19 • (4012 or *401)
3-5-(19 2 o r *19)(2114or *2113)

3 • 5 • 19 • (534 or *533 or *53
2)
3
45 • (194 or *193 or *192)

3453 [345s known]

(13
2 or *13)(36 or *3 5 or *3
4)
3353 [3252 known]

5
419
 (6)

in next section
(6)

(4)

(4)
excess 5's

3313 • 192

3
211 • (3316 or *3315 or *331
4)
3
211 • 19 • 83 • (57492 or *5749)
3211 • (292 or *29)(18893 or *18892)
355 • 7 • 11 • (295 or *294 or *293 or *292)
3653 [3652 known]
3 6 7-l l • (133 or *132/5)

367311

32(112 or *11)(838 or *83e for 4 < e < 7)
347 • (ll 2 or *11)(22692 or *2269)
32(52 or *5)(112 or *11)(132 or *13)
(53
4 or *533)
325211 • 13 • (2812 or
3553 [3
55 known]
3 511-13 2
 excess 113's

(4)

(4)
excess 3's
(5)
excess 5's
excess 5's
(5)

(4)

excess 5's

'281)  (4)
(5)

https://doi.org/10.4153/CMB-1975-021-9 Published online by Cambridge University Press

120

Table 1 contd.
 C. R. WALL

Unitary Divisors  Other Divisors
 [April

Elimination
if not (3)

215331
215331
215331
215331
215331
215331
215331

2 1 6

216655372

21665537
217

217436912

21743691
218

2181094

2181093

2181092

2181092457
218109
218109 • 373

• 83253 • 5
•83
• 83 • 52

•83- 5
• 83 • 5 • 72

•83 5-7-1 3
•83-5- 7

218109
218109
218109
218109
218109
218109
218109
218109
218109
218109
218109
218109
218109
218109
218109
218109
218109
218109
218109
218109
218109
218109
218109
218109
218109
218109
218109
219

219174763

372
372137
372137 • 232

372137 • 23
37*137-23-3 211
372137 • 23 • 3 2

37-5H3 2

37 • 5 219 0d d

•37 • 52

37 • 52192

37 • 52192136

37 • 52192133

37
37
37
37
37
37
37
37
37
37
37
37
37
37
37
 •5 7
.57449

•5 6

.5 5

• 55521
•5 3

• 533219
•533211
.5332

•5 4

• 54313
• 5*313 • 157
• 54313 • 157 • 79
 3 611-13
3353 (or N prime to 5) [33 known]
337 - 11 -13
347311
 (5)
(4)
(5)
(5)
excess 5's
excess 7's
(5)
(6)

see (12) in next section
(6)

see (12) in next section
(6)

3*11 -13 2 (or TV prime to 13)
655373

2147549185
3211 • 331
3 • 436913

3 • 954451741
3211 -331
5 • 13 • 37 • 1095

5 • 13 • 37 •70579081
5211 • (132 or *13)(612 or *61)(1932 or *193)
5 • (133 or *132)(372 or *37)(4573 or *4572)
5 • (133 or *132)(372 or *37)(2292 or *229)
5211 • 13 • (378 or *377 or *376 or *375 or *374)
52(132 or *13)(192 or *19) • 31
•(43211 or43-ll 2 or43-ll 2 61 )
5311 • (132 or *13)(1374 or *1373 or *1372)
3 • 5(112 or *11)(235 or *234 or *233)
3-5 4 (ll 2 o r *ll)(53 2 o r *53)
3353 [3253 known]

5411213
 (4)
excess 3's
see (14) in next section
excess 5's
excess 5's
11 -13-(19 8 o r *19 6or *194)
11 • 181 • (137 or *135 or *134)

7-11-18 1 -(157 2or *157)
5333 (or N prime to 3) [53 known]
3 • 11 • 13 • 19 • (515 or *5« for 8 <, e ^ 14)
3-1 1 -13-19-29-449 2

33 [3357 known]
3-1 1 • 13219 • (6012 or *601)
3-1 1 • 13 • 19 • (5213 or *5212)
33 [3355 known]
33 [3253 known]
 excess 5's

(4)

(4)

(4)
(4)
excess 5's
excess 3's
(5) 7-1P13-19 2

3 • 11 • 13 • 19 • (3134 or *3133 or *3132)
3 • 11 -13 • 19- (157 3or *1572)
3-1 1 -13-19-79 2

3-11-13-1 9 see (15) in next section
3 • (1747634 or *1747633 or *1747632)
3 • 43691 see (13) in next section

https://doi.org/10.4153/CMB-1975-021-9 Published online by Cambridge University Press

1975]

Table 1. contd.
 FIFT H TO

Unitary Divisors

2
20

22061681
22061681 • 30841

2 2 1

2215419
2215419 • 271
2 215419-271-43 2

2215419 • 271 • 43
2215419 • 271 • 43 •
2215419 • 271 • 43 •
2215419 • 271 • 43 •
2215419 • 271 • 43 •
2215419 • 271 • 43 •

2215419 • 271 • 43 •
2215419 • 271 • 43 •
2215419 • 271 • 43 •
2215419 • 271 • 43 •
2
22

2222113
2222113-397
2222113 • 397 • 199
2 222113-397-199
2222113 • 397 • 199

2 2 3

2232796203
2232796203 • 5419

2 2 4

224673
224673 • 337
2
25

2254051
2254051 • 1013

2 2 6

2281613
2261613-269
2
27

22787211

230

2301321
 17 2

17229
17
17-
17-

17
17-
17-
17-
 ll 2

11

11
11
11
11

•151
 •36

•35

•3561
• 3561 • 31

•151-1 9
 OTARY PERFECT NUMBER

Other Divisors

17 • (616814 or *616813 or *616812)
17 • (308413 or *308412)
7 • 17 • (22032 or *2203)
32(432 o r *43)(54194 o r * 5419 3 o r *54i92)
325 • (432 or *43)(2714 or *2713 or *2712)
325 • 17 • (435 or *434 or *433)
3253(172 or *17)(372 or *37)
325 • (ll 2 or *11)(175 or *174 or *173)
3 25 2(ll 2or *ll)-29 2

3353 [known]
3 4 5-(ll 5 o r *ll 4 o r *113)
345 • (612 or *61)
5 • (313 or *3e for 9 < e ^ 12
or *38/17 or *37)
52(732 or *73)
5 • (613 or *612)
5-31 2

5
5 • (3972 or *397)(21134 or *21133 or *21132)
5 • 7 • (1512 or *151)(3974 or *3973 or *3972)
5 • 7 • (1512 or *151)(1993 or *1992)
537 • (1513 or *1512)
537 . (19 3 o r * 19 2 )
7 • (56 or *55 or *5
4)
3 • 27962032

3243 • 54192

325 • 43 • (2712 or *271)
97 • (2572 or *257)(6733 or *6732)
(972 or *97)(2572 or *257) • 3372

(972 or *97)(2572 or *257)(133 or *13
2)
3-11-25 1 • (40513 or *40512)
3-1 1 -251 -(1013 3or *10132)
3
211 • (133 or *132)(2512 or *251)
5 • 53 • 157 • (16133 or *16132)
5 • (532 or *53)(1572 or *157) • 2692

3452(532 or *53)(1572 or *157)
3 419-(87211 3or *872112)
3419 • (218032 or *21803)
5 213-41 -61 -(1321 3or *13212)
5 213-41 -61 • (6612 or *661)
 121

Elimination
if not (3)

(4)

(5)

(11) If 2
132731 • 683 || N, we have a contradiction as in (8), since /(2132731
• 683) =/(2 9).

(12) Note that /(21665537) =/(21743691) =/(2 15). If 2
1665537m < W or
2
1743691« < Wis unitary perfect with (m, 2 • 65537) = (n, 2 • 43691) =
1, then 215m or 215n is unitary perfect and smaller than W. But A = 15
has already been eliminated.

https://doi.org/10.4153/CMB-1975-021-9 Published online by Cambridge University Press

122  C. R. WALL

(13) Since/(219174763) = /(217), A ^ 17 implies A ^ 19 by reasoning similar
to that in (12).

(14) If N = 2
18109 • 37H37 • 23 • 3
25
411
213 • m < W with (m, 6) = 1, then
m < 133. Either ll 21| N and hence 61 | m, or 11 | m; either 13 || N and
hence 7 | m, or 13 | m. The only possible value for m is 77, but this re-
quires/(JV) < 2.

(15) We write N = 2
18109 • 37 • 5
4313 • 157 • 79 • 3 • 11 • 13 • 19 • m < W. Then
m < 7. Since 13 Jf m, 13 || iVand hence 7 | m. Thus only m = 7 is possible,
and hence N = W.

The author thanks the referee for his many suggestions.

REFERENCES

1. M. V. Subbarao, Are there an infinity of unitary perfect numbers?, Amer. Math. Monthly,
77 (1970), pp. 389-390.
2. M. V. Subbarao and L. J. Warren, Unitary perfect numbers, Canad. Math. Bull. 9 (1966),
pp.147-153.
3. C. R. Wall, A new unitary perfect number, Notices Amer. Math. Soc, 16 (1969), p. 825.

UNIVERSITY OF SOUTH CAROLINA

https://doi.org/10.4153/CMB-1975-021-9 Published online by Cambridge University Press
