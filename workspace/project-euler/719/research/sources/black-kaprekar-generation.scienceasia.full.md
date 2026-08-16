<!-- source: https://www.scienceasia.org/2001.27.n2/v27_133_136.pdf | converted from PDF -->

ScienceAsia  27 (2001) :  133-136ESEARCH ARTICLER

INTRODUCTION

The n-Kaprekar numbers are named after DR
Kaprekar, who first introduced them in 1980.
1 They
are formally defined as follows: an n-Kaprekar
number k   1 (n = 1,2,  …) satisfies the pair of
equations
2:

k = q + r (1)
k2 = q x 10
n + r, (2)

where k, q, and r are positive integers, such that for
k > 1, we require q > 0 and 0 < r < 10
n.

By convention, zero is not considered to be an n-
Kaprekar number, whereas k = 1 (where q = 0, r = 1,
and n is arbitrary) is considered to be an n-Kaprekar.
In addition, numbers of the form 10m (where m   1
and requiring r = 0) are not considered to be n-
Kaprekar numbers.
2

Some justification for considering Kaprekar
numbers as objects worthy of interest can perhaps
be found from their inclusion in the Penguin
Dictionary of Curious and Interesting Numbers.3

Some examples of n-Kaprekar numbers are:

9
2 = 81 9 = 8+1
55
2 = 3025 55 = 30+25
95121
2 = 9048004641 95121 = 90480+4641.

Some Properties of the Kaprekar Numbers
and a Means of Generation

Colin G Black
Mechanical Engineering Program, Sirindhorn International Institute of Technology at
Thammasat University, Pathum Thani 12121,  Thailand.
Corresponding author, E-mail: bcg@siit.tu.ac.th
 Received  31 Jul 2000
Accepted  26 Jan 2001

ABSTRACT This note describes what is believed to be a novel and easily implemented method for
generating integer Kaprekar numbers. The starting point for the method is the observation made here,
that a necessary condition for an integer k to be a Kaprekar number is that k must be congruent to k2

modulo-9. Moreover, it is also shown here that a Kaprekar number k is either a member of the residue
class [0] or residue class [1] modulo-9. For an integer k congruent to k2 modulo-9, further steps are
then established to find any integer values: q, r and n, such that k = q + r, and k
2 = q x 10
n + r. The
method described here is implemented using the computer algebra software package: Mathcad. A list of
the entire integer Kaprekar numbers lying between 1 and 10
6 is generated. In addition, some results
relating to the properties of the Kaprekar numbers are also presented.

KEYWORDS: Kapreka numbers, modulo arithmetic, congruent.

In fact, 9, 55 and 95121 are 1-Kaprekar, 2-Kaprekar
and 5-Kaprekar numbers, respectively.

In this note, a new scheme for generating all the
n-Kaprekar numbers less than or equal to a specified
value is obtained.

APPLICATION OF MODULO-9 ARITHMETIC

The starting point for the approach presented
here is the observation that one condition for an
integer k to be an n-Kaprekar number, is that k must
be congruent to k
2 modulo-9. Moreover, if k is an n-
Kaprekar number, then it is a member of either the
residue class [0] or the residue class [1] modulo-9.

Theorem 1: k is n-Kaprekar ⇒ k
2 ≡ k (mod 10
n - 1).

Proof: For an n-Kaprekar integer k defined by
equations (1) and (2):

k
2 = q x 10
n + r
= q x (10
n-1+1) + r
= q x (10
n-1) + q + r ⇒
k
2 ≡ (q + r) (mod 10
n - 1) ⇒
k
2 ≡ k (mod 10
n - 1). (3)

Corollary: It immediately follows from the above that
k is n-Kaprekar ⇒ k2 ≡ k (mod 9).

134 ScienceAsia  27 (2001)

Remark: From the definition of the square of an n-
Kaprekar integer k given above, it is observed that
with the exception of k = 1 (for which q = 0, n is
arbitrary, and r = 1) that k
2 > 10n.

Theorem 2: For t ≡ k(mod 9), then t ∈ {[0] ,[1]} for n-
Kaprekar k.

Proof: For integers: k, s and t, we can write:

k = 9 x s + t, 0 ≤ t ≤ 8 (4)

where
 t ≡ k(mod 9), (5)

Hence:

k2 =92 x s
2 + 2 x 9 x s x t + t
2 ⇒
k2 ≡ t2 (mod 9) (6)

But it follows from (3) - (6) that if k is an n-Kaprekar
number, then:

t ≡ t2(mod 9), 0 ≤ t ≤ 8. (7)

But (7) is only true for t = 0 or t = 1. Hence the set of
residue classes modulo-9 when k is n-Kaprekar is
{[0],[1]}.

Theorem 3: q is even for all the n-Kaprekar numbers;
and r is odd for the odd n-Kaprekar numbers and even
for the even n-Kaprekar numbers.

Proof:
Case 1: n-Kaprekar k odd.

If k is odd and greater than 1, then from

k = q + r

either q could be odd and r even, or q could be even
and r odd.

If k is odd, it follows that k
2 is odd. But

k2 = q x 10n + r

implies because n ≥ 1, that q x 10
n  must be even.
Hence r must be odd, and q must be even.

In the case of k = 1, it is noted that r = 1 and
q = 0.
 Case 2: n-Kaprekar k even.

If k is even then it follows that either both q or r
could be even, or both q and r could be odd. But if k
is even, it follows that k
2 is even. Hence, by similar
reasoning to that given above for Case 1, both r and
q must be even.

METHOD FOR GENERATING N-KAPREKAR NUMBERS

For an integer k satisfying:

t ≡ k(mod 9)
t ≡ t
2(mod 9), (8)

where t ∈ {[0],[1]}, equations (1) and (2) can then
be used to solve for possible values of r in terms of k
and n, denoted here by r(n). Eliminating q gives:

r(n) = (k
2 - k x 10
n)/(1 - 10n)
for n = 1, … , nmax . (9)

Hence another condition for k to be an n-
Kaprekar number is that the fractional part of r(n)
in equation (9) must be exactly equal to zero; that
is, only integer values for r(n) are acceptable.

The exponent n in equation (9) ranges from 1 to
a maximum value: nmax. The value of nmax is given
by re-arranging equation (2). For r > 0 and q > 0,
and for the monotonically increasing logarithmic
function, we have:

10n =(k
2 - r)/q ⇒
n = log10[(k2 - r)/q] ⇒
n < log10[k
2] = 2 log10[k] ⇒
nmax= ceil(2 log10[k]) (10)

where ceil(x) is defined here to be the smallest
integer greater than or equal to the argument x.

IMPLEMENTATION OF THE METHOD

For a given integer k, (8) represents the first step
in establishing if k is an n-Kaprekar number.
Subsequent steps are represented by equations (9)
and (10), and finally, if necessary, by the defining
equations (1) and (2).

 This method is implemented here using the
computer algebra software package Mathcad.4 The
Mathcad code is shown later.  A list of all the n-

ScienceAsia  27 (2001) 135

Kaprekar Numbers lying between 1 and 106,
generated using the method described here, is shown
in the table below. The corresponding values for the
integers: q, r and n, as defined by equations (1) and
(2), are also included in the table.

Table 1. n-Kaprekar Numbers  1 ≤ k < 106.

kq r n k2

10 1 1 1
98 1 1 81
45 20 25 2 2025
55 30 25 2 3025
99 98 1 2 9801
297 88 209 3 88209
703 494 209 3 494209
999 998 1 3 998001
2223 494 1729 4 4941729
2728 744 1984 4 7441984
4879 238 4641 5 23804641
4950 2450 2500 4 24502500
5050 2550 2500 4 25502500
5292 28 5264 6 28005264
7272 5288 1984 4 52881984
7777 6048 1729 4 60481729
9999 9998 1 4 99980001
17344 3008 14336 5 300814336
22222 4938 17284 5 493817284
38962 1518 37444 6 1518037444
77778 60494 17284 5 6049417284
82656 68320 14336 5 6832014336
95121 90480 4641 5 9048004641
99999 99998 1 5 9999800001
142857 20408 122449 6 20408122449
148149 21948 126201 6 21948126201
181819 33058 148761 6 33058148761
187110 35010 152100 6 35010152100
208495 43470 165025 6 43470165025
318682 101558 217124 6 101558217124
329967 108878 221089 6 108878221089
351352 123448 227904 6 123448227904
356643 127194 229449 6 127194229449
390313 152344 237969 6 152344237969
461539 213018 248521 6 213018248521
466830 217930 248900 6 217930248900
499500 249500 250000 6 249500250000
500500 250500 250000 6 250500250000
533170 284270 248900 6 284270248900
538461 289940 248521 6 289940248521
609687 371718 237969 6 371718237969
627615 39390 588225 7 393900588225
643357 413908 229449 6 413908229449
648648 420744 227904 6 420744227904
670033 448944 221089 6 448944221089
681318 464194 217124 6 464194217124
791505 626480 165025 6 626480165025
812890 660790 152100 6 660790152100
818181 669420 148761 6 669420148761
851851 725650 126201 6 725650126201
857143 734694 122449 6 734694122449
961038 923594 37444 6 923594037444
994708 989444 5264 6 989444005264
999999 999998 1 6 999998000001
 Table 2. Residue Classes Modulo-9 for n-Kaprekar
Numbers k: 1 ≤ k < 106.

ik t ≡ k Prime
mod(9) Factorization of k

11 ∈[1] =1
29 ∈[0] =32

345 ∈[0] =32 x 5
455 ∈[1] =5 x 11
599 ∈[0] =32 x 11
6 297 ∈[0] =33 x 11
7 703 ∈[1] =19 x 37
8 999 ∈[0] =33 x 37
9 2223 ∈[0] =32 x 13 x 19
10 2728 ∈[1] =23 x 11 x 31
11 4879 ∈[1] =7 x 17 x 41
12 4950 ∈[0] =2 x 32 x 5
2 x 11
13 5050 ∈[1] =2 x 52 x 101
14 5292 ∈[0] =22 x 3
3 x 7
2

15 7272 ∈[0] =23 x 3
2 x 101
16 7777 ∈[1] =7 x 11 x 101
17 9999 ∈[0] =32 x 11 x 101
18 17344 ∈[1] =26 x 271
19 22222 ∈[1] =2 x 41 x 271
20 38962 ∈[1] =2 x 7 x 112 x 23
21 77778 ∈[0] =2 x 32 x 29 x 149
22 82656 ∈[0] =25 x 3
2 x 7 x 41
23 95121 ∈[0] =33 x 13 x 271
24 99999 ∈[0] =32 x 41 x 271
25 142857 ∈[0] =33 x 11 x 13 x 37
26 148149 ∈[0] =34 x 31 x 59
27 181819 ∈[1] =11 x 16529
28 187110 ∈[0] =2 x 35 x 5 x 7 x 11
29 208495 ∈[1] =5 x 72 x 23 x 37
30 318682 ∈[1] =2 x 7 x 13 x 17 x 103
31 329967 ∈[0] =33 x 11
2 x 101
32 351352 ∈[1] =23 x 37 x 1187
33 356643 ∈[0] =34 x 7 x 17 x 37
34 390313 ∈[1] =7 x 11 x 37 x 137
35 461539 ∈[1] =13
2 x 2731
36 466830 ∈[0] =2 x 33 x 5 x 7 x 13 x 19
37 499500 ∈[0] =22 x 3
3 x 5
3 x 37
38 500500 ∈[1] =22 x 5
3 x 7 x 11 x 13
39 533170 ∈[1] =2 x 5 x 11 x 37 x 131
40 538461 ∈[0] =33 x 7
2 x 11 x 37
41 609687 ∈[0] =35 x 13 x 193
42 627615 ∈[0] =33 x 5 x 4649
43 643357 ∈[1] =11
2 x 13 x 409
44 648648 ∈[0] =23 x 3
4 x 7 x 11 x 13
45 670033 ∈[1] =7 x 13 x 37 x 199
46 681318 ∈[0] =2 x 33 x 11 x 31 x 37
47 791505 ∈[0] =33 x 5 x 11 x 13 x 41
48 812890 ∈[1] =2 x 5 x 133 x 37
49 818181 ∈[0] =35 x 7 x 13 x 37
50 851851 ∈[1] =7 x 11 x 13 x 23 x 37
51 857143 ∈[1] =7 x 122449
52 961038 ∈[0] =2 x 33 x 13 x 37
2

53 994708 ∈[1] =22 x 11 x 13 x 37 x 47
54 999999 ∈[0] =33 x 7 x 11 x 13 x 37

136 ScienceAsia  27 (2001)

CASTING OUT NINES

The sequence of n-Kaprekar numbers is
composed of two types of integers corresponding to
one of the two residue classes: [0] or [1] modulo 9.
A familiar (and easily proven) rule for calculating
residue classes in modulo-9 arithmetic, often called
“casting out nines,” can be applied to the n-Kaprekar
numbers. For example:

55 (mod 9) ≡ (5+5) (mod 9) ≡ 1
95121 (mod 9)
≡ (9+5+1+2+1) (mod 9) ≡  0

For an n-Kaprekar number k, where:

k= ap ap-1… a2a1, (11)

meaning

k= a1 + a2 x 10
1 + a3 x 10
2 + … ap x 10
p-1

(12)

we have for k either

(a1 + a2 + … ap) (mod 9) ≡ 0 (13)
or (a1 + a2 + … ap) (mod 9) ≡ 1 (14)

A complete list of the residue classes modulo-9,
in sequence, corresponding to the 54 n-Kaprekar
numbers lying between 1 and 10
6 given in Table 1,
is shown below in Table 2. The prime factorizations
of the n-Kaprekar numbers are also given.

CONCLUSIONS

The n-Kaprekar numbers k are congruent to their
squares modulo-9. Moreover, the set of residue
classes modulo-9 is {[0],[1]}; hence the n-Kaprekar
sequence is shown to be composed of two distinct
types, categorized by these two residue classes. Also,
some definite statements can be made about the
evenness of q, and the oddness or evenness of r,
where k = q + r.
The n-Kaprekar numbers occurring within a
specified range can be generated easily, and relatively
quickly, using the approach developed here.
 for k    1..kupper

j←0
 r← .

10
n - 1

if {k2 = q.10n + r}.(k = q + r)


 

x

k(kupper)
 nupper←ceil(2.log(kupper))

mod9k←mod(k, 9)

if (mod9k=mod9k2)

flag←0
 q←k - r

for n    1.. nupper

if (0<r).{r<10n}.(floor(r) = r).(flag = 0)

k  10n - k2

j←j  + 1

xj,0←k

xj,1←q

xj,2←r

x
j,
3←n

x
j,4←q.10n + r

xj,5←k2

flag←1

mod9k2←mod{mod9k2, 9}

REFERENCES

1. Kaprekar D (1980) On Kaprekar Numbers. J of Recreational
Mathematics 13(2), 81-2.
2. Iannucci Douglas E (2000) The Kaprekar Numbers. J of Integer
Sequences  3, Article 00.1.2. (http://www.research.att.com/
~njas/sequences/JIS/VOL3/iann2a.html).
3. Wells David (Editor) (1997) The Penguin Dictionary of
Curious and Interesting Numbers. Penguin Books Ltd.,
Middlesex, England.
4. Mathcad Software. Website:  http://www/mathsoft.com/
mathcad.

MATHCAD CODE

The Mathcad implementation of the method
developed here is shown below:

The n-Kaprekar numbers lying between 1 and
106, as well as all the additional information shown
in Table 1, were generated using k(10
6).
