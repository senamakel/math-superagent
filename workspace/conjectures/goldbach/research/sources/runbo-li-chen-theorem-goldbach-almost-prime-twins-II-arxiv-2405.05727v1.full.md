<!-- source: https://arxiv.org/pdf/2405.05727v1 | converted from PDF -->

arXiv:2405.05727v1  [math.NT]  9 May 2024
ON CHEN’S THEOREM, GOLDBACH’S CONJECTURE AND ALMOST
PRIME TWINS

RUNBO LI

Abstract. Let N denotes a suﬃciently large even integer, we deﬁne D1,2(N ) as the same
as those in previous articles about Chen’s theorem. In this paper, we show that D1,2(N ) ⩾
1.253 C(N )N
(log N )2 , improving previous record of Wu about 40%. We also get similar results on
twin prime problem and additive representations of integers. An important step in the proof
is the application of a theorem of Lichtman.

Contents

1. Introduction 1
2. Weighted Sieve Method 3
3. Proof of Theorem 1.1 5
4. Proof of Theorem 1.3 11
References 17

1. Introduction

Let N denotes a suﬃciently large even integer, p denotes a prime number, and let P2
denotes an integer with at most two prime factors counted with multiplicity. We deﬁne

D1,2(N) := |{p : p ⩽ N, N − p = P2}| . (1)

In 1973 Chen [5] established his remarkable Chen’s theorem:

D1,2(N) ⩾ 0.67 C(N)N
(log N)2 , (2)

where
 C(N) := ∏

p|N
p>2
 p − 1
p − 2
 ∏

p>2
 (
1 − 1
(p − 1)2
 ) . (3)

Chen’s constant 0.67 was improved successively to

0.689, 0.7544, 0.81, 0.8285, 0.836, 0.867, 0.899

by Halberstam and Richert [11] [10], Chen [7] [6], Cai and Lu [4], Wu [19], Cai [2] and Wu
[20] respectively. Chen [8] announced a better constant 0.9, but this work has not been
published.
In this paper, we obtain the following sharper result.

2020 Mathematics Subject Classiﬁcation. 11N35, 11N36, 11P32.
Key words and phrases. Chen’s theorem, Sieve, Mean value theorem.
1

Theorem 1.1.
 D1,2(N) ⩾ 1.253 C(N)N
(log N)2 .

One important signiﬁcance of our Theorem 1.1 is to make us truly achieve and exceed the
constant 0.9 claimed by Chen [8]. Our constant 1.253 gives a 40% reﬁnement of Wu’s prior
record 0.899. This is the greatest reﬁnement on the problem since Chen [5] from 1973.
Furthermore, for two relatively prime square-free positive integers a, b, let M denotes a
suﬃciently large integer that is relatively prime to both a and b, a, b < M ε and let M be
even if a and b are both odd. Let Ra,b(M) denote the number of primes p such that ap and
M − ap are both square-free, b | (M − ap), and M −ap
b = P2. In 1976, Ross [[17], Chapter 3]
established that
 Ra,b(M) ⩾ 0.608 C(abM)M
ab(log M)2 , (4)

where
 C(abM) := ∏

p|abM
p>2
 p − 1
p − 2
 ∏

p>2
 (
1 − 1
(p − 1)2
 ) , (5)

and the constant 0.608 was improved successively to 0.68 and 0.8671 by Li [12] and Li [13]
respectively. By using the same sieve process and methods in [13], we have the following
sharper.

Theorem 1.2.
 Ra,b(M) ⩾ 1.253 C(abM)M
ab(log M)2 .

Let x denotes a suﬃciently large integer and deﬁne

π1,2(x) := |{p : p ⩽ x, p + 2 = P2}| . (6)

In 1973 Chen [5] showed simultaneously that

π1,2(x) ⩾ 0.335 C2x
(log x)2 , (7)

where
 C2 := 2 ∏

p>2
 (
1 − 1
(p − 1)2
 ) , (8)

and the constant 0.608 was improved successively to

0.3445, 0.3772, 0.405, 0.71, 1.015, 1.05, 1.0974, 1.104, 1.123, 1.13

by Halberstam [10], Chen [7] [6], Fouvry and Grupp [9], Liu [16], Wu [18], Cai [1], Wu [19],
Cai [2] and Cai [3] respectively.
In this paper, we get the following sharper.

Theorem 1.3.
 π1,2(x) ⩾ 1.205 C2x
(log x)2 .

2

2. Weighted Sieve Method

Let A and B denote a ﬁnite set of positive integers, P denotes an inﬁnite set of primes
and z ⩾ 2. Put A = {N − p : p ⩽ N} , B = {p + 2 : p ⩽ x} ,

P = {p : (p, 2) = 1}, P(q) = {p : p ∈ P, (p, q) = 1},

P (z) = ∏

p∈P
p<z
 p, Ad = {a : a ∈ A, a ≡ 0(modd)}, S(A; P, z) = ∑

a∈A
(a,P (z))=1
 1.

Lemma 2.1. ([[20], Lemma 2.2]). We have

4D1,2(N) ⩾ 3S (A; P(N), N 1
13.27 ) + S (
A; P(N), N 1
8.24 )

− ∑

N 1
13.27 ⩽p<N 1
3
(p,N )=1
 S (Ap; P(N), N 1
13.27 )

− ∑

N 1
13.27 ⩽p<N 1
2 − 3
13.27
(p,N )=1
 S (
Ap; P(N), N 1
13.27 )

+ ∑

N 1
13.27 ⩽p2<p1<N 1
8.24
(p1p2,N )=1
 S (Ap1p2; P(N), N 1
13.27 )

+ ∑

N 1
13.27 ⩽p2<N 1
8.24 ⩽p1<N 1
2 − 3
13.27
(p1p2,N )=1
 S (
Ap1p2; P(N), N 1
13.27 )

− 2 ∑

N 1
2 − 3
13.27 ⩽p1<p2<( N
p1 ) 1
2

(p1p2,N )=1
 S (Ap1p2; P(Np1), p2)

− ∑

N 1
13.27 ⩽p1<N 1
3 ⩽p2<( N
p1 ) 1
2

(p1p2,N )=1
 S (Ap1p2; P(Np1), p2)

− ∑

N 1
8.24 ⩽p1<N 1
2 − 3
13.27 ⩽p2<( N
p1 ) 1
2

(p1p2,N )=1
 S
 (
Ap1p2; P(Np1), ( N
p1p2
 ) 1
2 )

− ∑

N 1
13.27 ⩽p1<p2<p3<p4<N 1
8.24
(p1p2p3p4,N )=1
 S (Ap1p2p3p4; P(N), p2)

− ∑

N 1
13.27 ⩽p1<p2<p3<N 1
8.24 ⩽p4<N 1
2 − 2
13.27 p−1
3
(p1p2p3p4,N )=1
 S (Ap1p2p3p4; P(N), p2)

3

+ O (N 12.27
13.27 )

= 3S1 + S2 − S3 − S4 + S5 + S6 − 2S7 − S8 − S9 − S10 − S11 + O (
N 12.27
13.27 ) .

Lemma 2.2. ([[3], Lemma 3.2]). We have

4π1,2(x) ⩾ 3S (
B; P, x 1
12 ) + S (
B; P, x 1
7.2 )

+ ∑

x 1
12 ⩽p2<p1<x 1
7.2 S (
Bp1p2; P, x 1
12 )

+ ∑

x 1
12 ⩽p2<x 1
7.2 ⩽p1<min(x 2
7 ,x 17
42 p−1
2 )
 S (Bp1p2; P, x 1
12 )

− 2 ∑

x 1
12 ⩽p<x 25
107 S (
Bp; P, x 1
12 ) − 2 ∑

x 25
107 ⩽p<x 2
7 −ε S (
Bp; P, x 1
12 )

− ∑

x 2
7 −ε⩽p<x 2
7 S (Bp; P, x 1
12 ) − ∑

x 2
7 −ε⩽p<x 29
100 S (
Bp; P, x 1
12 )

− ∑

x 29
100 ⩽p<x 1
3 −ε S (
Bp; P, x 1
12 ) − ∑

x 1
3 −ε⩽p<x 1
3 S (
Bp; P, x 1
12 )

− ∑

x 1
12 ⩽p1<x 1
3 ⩽p2<( x
p1 ) 1
2 S (Bp1p2; P(p1), p2)

− ∑

x 1
7.2 ⩽p1<x 2
7 ⩽p2<( x
p1 ) 1
2 S
 (
Bp1p2; P(p1), ( x
p1p2
 ) 1
2 )

− 2 ∑

x 2
7 ⩽p1<p2<( x
p1 ) 1
2 S (Bp1p2; P(p1), p2)

− ∑

x 1
12 ⩽p1<p2<p3<p4<x 1
7.2 S (Bp1p2p3p4; P(p1), p2)

− ∑

x 1
12 ⩽p1<p2<p3<x 5
42 <x 1
7.2 <p4<x 2
7 S (Bp1p2p3p4; P(p1), p2)

− ∑

x 1
12 ⩽p1<p2<x 5
42 ⩽p3<x 1
7.2 ⩽p4<x 17
42 p−1
3
 S (Bp1p2p3p4; P(p1), p2)

− ∑

x 1
12 ⩽p1<x 5
42 ⩽p2<p3<x 1
7.2 ⩽p4<x 17
42 p−1
3
 S (Bp1p2p3p4; P(p1), p2)

− ∑

x 5
42 ⩽p1<p2<p3<x 1
7.2 ⩽p4<x 17
42 p−1
3
 S (Bp1p2p3p4; P(p1), p2)

4

+ O (
x 11
12 )

= 3S′
1 + S′
2 + S′
3 + S′
4 − 2S′
5 − 2S′
6 − S′
7 − S′
8 − S′
9 − S′
10

− S′
11 − S′
12 − 2S′
13 − S′
14 − S′
15 − S′
16 − S′
17 − S′
18 + O (x 11
12 ) .

3. Proof of Theorem 1.1

In this section, sets A and P are deﬁned respectively. Let γ denotes the Euler’s constant,
F (s) and f (s) are determined by the following diﬀerential-diﬀerence equation
{
F (s) = 2eγ
s , f (s) = 0, 0 < s ⩽ 2,
(sF (s))′ = f (s − 1), (sf (s))′ = F (s − 1), s ⩾ 2,

and ω(u) denotes the Buchstab function determined by the following diﬀerential-diﬀerence
equation {
ω(u) = 1
u , 1 ⩽ u ⩽ 2,
(uω(u))′ = ω(u − 1), u ⩾ 2.

We ﬁrst consider S1 and S2. By Buchstab’s identity, we have

S1 = S (
A; P(N), N 1
13.27 ) = S (A; P(N), N 1
500 ) − ∑

N 1
500 ⩽p<N 1
13.27
(p,N )=1
 S (Ap; P(N), N 1
500 )

+ ∑

N 1
500 ⩽p2<p1<N 1
13.27
(p1p2,N )=1
 S (Ap1p2; P(N), N 1
500 )

− ∑

N 1
500 ⩽p3<p2<p1<N 1
13.27
(p1p2p3,N )=1
 S (Ap1p2p3; P(N), p3) (9)

and
 S2 = S (A; P(N), N 1
8.24 ) = S (A; P(N), N 1
500 ) − ∑

N 1
500 ⩽p<N 1
8.24
(p,N )=1
 S (
Ap; P(N), N 1
500 )

+ ∑

N 1
500 ⩽p2<p1<N 1
8.24
(p1p2,N )=1
 S (
Ap1p2; P(N), N 1
500 )

− ∑

N 1
500 ⩽p3<p2<p1<N 1
8.24
(p1p2p3,N )=1
 S (Ap1p2p3; P(N), p3) . (10)

By Iwaniec’s linear sieve method and arguments in [14] and [15] we have

S1 ⩾ (1 + o(1)) 2
eγ
 (
500f (500ϑ 1
500
 ) − 500 ∫ 1
13.27

1
500
 F (500(ϑ1(t, 1
500 , 1
500 ) − t))
t dt

5

+ 500 ∫ 1
13.27

1
500
 ∫ t1

1
500
 f (500(ϑ1(t1, t2, 1
500 ) − t1 − t2))
t1t2 dt2dt1

− ∫ 1
13.27

1
500
 ∫ t1

1
500
 ∫ t2

1
500
 F ( (ϑ1(t1,t2,t3)−t1−t2−t3)
t3
 )

t1t2t
2
3 dt3dt2dt1


 C(N)N
(log N)2 (11)

and
 S2 ⩾ (1 + o(1)) 2
eγ
 (
500f (
500ϑ 1
500
 ) − 500 ∫ 1
8.24

1
500
 F (500(ϑ1(t, 1
500, 1
500 ) − t))
t dt

+ 500 ∫ 1
8.24

1
500
 ∫ t1

1
500
 f (500(ϑ1(t1, t2, 1
500 ) − t1 − t2))
t1t2 dt2dt1

− ∫ 1
8.24

1
500
 ∫ t1

1
500
 ∫ t2

1
500
 F ( (ϑ1(t1,t2,t3)−t1−t2−t3)
t3
 )

t1t2t
2
3 dt3dt2dt1


 C(N)N
(log N)2 , (12)

where ϑ 1
500 = 19101
32000 and ϑ1(t1, t2, t3) is deﬁned as the same as in [15]. By numerical calcula-
tions we get that
 S1 ⩾ 14.901125 C(N)N
(log N)2 (13)

and
 S2 ⩾ 9.228483 C(N)N
(log N)2 . (14)

For S3, we split it into three parts and use diﬀerent distribution levels in each part.

S3 = ∑

N 1
13.27 ⩽p<N 1
3
(p,N )=1
 S (Ap; P(N), N 1
13.27 )

= ∑

N 1
13.27 ⩽p<N 25
128
(p,N )=1
 S (Ap; P(N), N 1
13.27 )

+ ∑

N 25
128 ⩽p<N 25
96
(p,N )=1
 S (
Ap; P(N), N 1
13.27 )

+ ∑

N 25
96 ⩽p<N 1
3
(p,N )=1
 S (
Ap; P(N), N 1
13.27 )

= S31 + S32 + S33. (15)

By Buchstab’s identity, we have

S31 = ∑

N 1
13.27 ⩽p<N 25
128
(p,N )=1
 S (
Ap; P(N), N 1
13.27 )

6

= ∑

N 1
13.27 ⩽p<N 25
128
(p,N )=1
 S (
Ap; P(N), N 1
500 )

− ∑

N 1
500 ⩽p2<N 1
13.27 ⩽p1<N 25
128
(p1p2,N )=1
 S (Ap1p2; P(N), N 1
500 )

+ ∑

N 1
500 ⩽p3<p2<N 1
13.27 ⩽p1<N 25
128
(p1p2p3,N )=1
 S (Ap1p2p3; P(N), p3) (16)

and
 S32 = ∑

N 25
128 ⩽p<N 25
96
(p,N )=1
 S (Ap; P(N), N 1
13.27 )

= ∑

N 25
128 ⩽p<N 25
96
(p,N )=1
 S (Ap; P(N), N 1
500 )

− ∑

N 1
500 ⩽p2<N 1
13.27 <N 25
128 ⩽p1<N 25
96
(p1p2,N )=1
 S (Ap1p2; P(N), p2) . (17)

By Iwaniec’s linear sieve method and arguments in [14] and [15] we have

S3 ⩽ (1 + o(1)) 2
eγ
 (
500 ∫ 25
128

1
13.27
 F (500(ϑ1(t, 1
500 , 1
500) − t))
t dt

− 500 ∫ 25
128

1
13.27
 ∫ 1
13.27

1
500
 f (500(ϑ1(t1, t2, 1
500 ) − t1 − t2))
t1t2 dt2dt1

+ ∫ 25
128

1
13.27
 ∫ 1
13.27

1
500
 ∫ t2

1
500
 F ( (ϑ1(t1,t2,t3)−t1−t2−t3)
t3
 )

t1t2t
2
3 dt3dt2dt1

+ 500 ∫ 25
96

25
128
 F (500(ϑ1(t) − t))
t dt

− ∫ 25
96

25
128
 ∫ 1
13.27

1
500
 f ( (ϑ1(t1)−t1−t2)
t2
 )

t1t
2
2 dt2dt1

+ 13.27 ∫ 1
3

25
96
 F (13.27( 1
2 − t))
t dt

) C(N)N
(log N)2

⩽ 23.466645 C(N)N
(log N)2 , (18)

7

where ϑ1(t) is deﬁned as the same as in [15]. Similarly, for S4–S6 we have

S4 ⩽ (1 + o(1)) 2
eγ
 (
500 ∫ 25
128

1
13.27
 F (500(ϑ1(t, 1
500 , 1
500) − t))
t dt

− 500 ∫ 25
128

1
13.27
 ∫ 1
13.27

1
500
 f (500(ϑ1(t1, t2, 1
500 ) − t1 − t2))
t1t2 dt2dt1

+ ∫ 25
128

1
13.27
 ∫ 1
13.27

1
500
 ∫ t2

1
500
 F ( (ϑ1(t1,t2,t3)−t1−t2−t3)
t3
 )

t1t2t
2
3 dt3dt2dt1

+ 500 ∫ 25
96

25
128
 F (500(ϑ1(t) − t))
t dt

− ∫ 25
96

25
128
 ∫ 1
13.27

1
500
 f ( (ϑ1(t1)−t1−t2)
t2
 )

t1t
2
2 dt2dt1

+ 13.27 ∫ 1
2 − 3
13.27

25
96
 F (13.27( 1
2 − t))
t dt

) C(N)N
(log N)2

⩽ 19.457442 C(N)N
(log N)2 , (19)

S5 = ∑

N 1
13.27 ⩽p2<p1<N 1
8.24
(p1p2,N )=1
 S (Ap1p2; P(N), N 1
13.27 )

= ∑

N 1
13.27 ⩽p2<p1<N 1
8.24
(p1p2,N )=1
 S (Ap1p2; P(N), N 1
500 )

− ∑

N 1
500 ⩽p3<N 1
13.27 ⩽p2<p1<N 1
8.24
(p1p2p3,N )=1
 S (Ap1p2p3; P(N), p3) (20)

⩾ (1 + o(1)) 2
eγ
 (
500 ∫ 1
8.24

1
13.27
 ∫ t1

1
13.27
 f (500(ϑ1(t1, t2, 1
500 ) − t1 − t2))
t1t2 dt2dt1

− ∫ 1
8.24

1
13.27
 ∫ t1

1
13.27
 ∫ 1
13.27

1
500
 F ( (ϑ1(t1,t2,t3)−t1−t2−t3)
t3
 )

t1t2t
2
3 dt3dt2dt1


 C(N)N
(log N)2

⩾ 1.690037 C(N)N
(log N)2 , (21)

S6 = ∑

N 1
13.27 ⩽p2<N 1
8.24 ⩽p1<N 1
2 − 3
13.27
(p1p2,N )=1
 S (
Ap1p2; P(N), N 1
13.27 )

8

= ∑

N 1
13.27 ⩽p2<N 1
8.24 ⩽p1<N 25
128
(p1p2,N )=1
 S (Ap1p2; P(N), N 1
13.27 )

+ ∑

N 1
13.27 ⩽p2<N 1
8.24 <N 25
128 ⩽p1<N 25
96
(p1p2,N )=1
 S (Ap1p2; P(N), N 1
13.27 )

+ ∑

N 1
13.27 ⩽p2<N 1
8.24 <N 25
96 ⩽p1<N 1
2 − 3
13.27
(p1p2,N )=1
 S (
Ap1p2; P(N), N 1
13.27 )

= ∑

N 1
13.27 ⩽p2<N 1
8.24 ⩽p1<N 25
128
(p1p2,N )=1
 S (Ap1p2; P(N), N 1
500 )

− ∑

N 1
500 ⩽p3<N 1
13.27 ⩽p2<N 1
8.24 ⩽p1<N 25
128
(p1p2p3,N )=1
 S (Ap1p2p3; P(N), p3)

+ ∑

N 1
13.27 ⩽p2<N 1
8.24 <N 25
128 ⩽p1<N 25
96
(p1p2,N )=1
 S (Ap1p2; P(N), N 1
13.27 )

+ ∑

N 1
13.27 ⩽p2<N 1
8.24 <N 25
96 ⩽p1<N 1
2 − 3
13.27
(p1p2,N )=1
 S (
Ap1p2; P(N), N 1
13.27 ) (22)

⩾ (1 + o(1)) 2
eγ
 (
500 ∫ 25
128

1
8.24
 ∫ 1
8.24

1
13.27
 f (500(ϑ1(t1, t2, 1
500 ) − t1 − t2))
t1t2 dt2dt1

− ∫ 25
128

1
8.24
 ∫ 1
8.24

1
13.27
 ∫ 1
13.27

1
500
 F ( (ϑ1(t1,t2,t3)−t1−t2−t3)
t3
 )

t1t2t
2
3 dt3dt2dt1

+ 13.27 ∫ 25
96

25
128
 ∫ 1
8.24

1
13.27
 f (13.27(ϑ1(t1) − t1 − t2))
t1t2 dt2dt1

+ 13.27 ∫ 1
2 − 3
13.27

25
96
 ∫ 1
8.24

1
13.27
 f (13.27( 1
2 − t1 − t2))
t1t2 dt2dt1
) C(N)N
(log N)2

⩾ 4.817602 C(N)N
(log N)2 . (23)

For other terms, by the arguments in [20], we have

S7 ⩽ (1 + o(1))
 (

8 ∫ 2654
727

2
 log(t − 1)
t dt

) C(N)N
(log N)2 ⩽ 0.585179 C(N)N
(log N)2 , (24)

S8 ⩽ (1 + o(1))
 (36
5
 ∫ 1
10

1
13.27
 log(2 − 3t)
t(1 − t)2 dt + 8 ∫ 1
3

1
10
 log(2 − 3t)
t(1 − t) dt

) C(N)N
(log N)2

9

⩽ 5.279581 C(N)N
(log N)2 , (25)

S9 ⩽ (1 + o(1))
 

8 ∫ 7.24

1927
727
 log ( 1927
727 −
 2654
727
t+1 )

t dt



 C(N)N
(log N)2 ⩽ 5.372410 C(N)N
(log N)2 , (26)

S10 ⩽ (1 + o(1))
 

36
5
 ∫ 1
10

1
13.27
 ∫ 1
8.24

t1
 ∫ 1
8.24

t2
 ∫ 1
8.24

t3
 ω ( 1−t1−t2−t3−t4
t2
 )

t1t
2
2t3t4 (1 − t1) dt4dt3dt2dt1

+ 8 ∫ 1
8.24

1
10
 ∫ 1
8.24

t1
 ∫ 1
8.24

t2
 ∫ 1
8.24

t3
 ω ( 1−t1−t2−t3−t4
t2
 )

t1t
2
2t3t4 dt4dt3dt2dt1


 C(N)N
(log N)2

⩽ 0.104338 C(N)N
(log N)2 , (27)

S11 ⩽ (1 + o(1))
 

36
5
 ∫ 1
10

1
13.27
 ∫ 1
8.24

t1
 ∫ 1
8.24

t2
 ∫ 1
2 − 2
13.27 −t3

1
8.24
 ω ( 1−t1−t2−t3−t4
t2
 )

t1t
2
2t3t4 (1 − t1) dt4dt3dt2dt1

+ 8 ∫ 1
8.24

1
10
 ∫ 1
8.24

t1
 ∫ 1
8.24

t2
 ∫ 1
2 − 2
13.27 −t3

1
8.24
 ω ( 1−t1−t2−t3−t4
t2
 )

t1t
2
2t3t4 dt4dt3dt2dt1


 C(N)N
(log N)2

⩽ 0.576364 C(N)N
(log N)2 . (28)

Finally, by Lemma 2.1 and (9)–(28) we get

3S1 + S2 + S5 + S6 ⩾ 60.439497 C(N)N
(log N)2 ,

S3 + S4 + 2S7 + S8 + S9 + S10 + S11 ⩽ 55.427138 C(N)N
(log N)2 ,

4D1,2(N) ⩾ (3S1 + S2 + S5 + S6)

− (S3 + S4 + 2S7 + S8 + S9 + S10 + S11)

⩾ 5.012 C(N)N
(log N)2 ,

D1,2(N) ⩾ 1.253 C(N)N
(log N)2 .

Theorem 1.1 is proved. Since the detail of the proof of Theorem 1.2 is similar to those of
Theorem 1.1 and Theorem 1.1 in [13] so we omit it in this paper.
10

4. Proof of Theorem 1.3

In this section, sets B and P are deﬁned respectively. For S′
1 and S′
2, by Buchstab’s
identity, we have

S′
1 = S (B; P, x 1
12 ) = S (B; P, x 1
500 ) − ∑

x 1
500 ⩽p<x 1
12 S (Bp; P, x 1
500 )

+ ∑

x 1
500 ⩽p2<p1<x 1
12 S (Bp1p2; P, x 1
500 )

− ∑

x 1
500 ⩽p3<p2<p1<x 1
12 S (Bp1p2p3; P, p3) (29)

and
 S′
2 = S (B; P, x 1
7.2 ) = S (B; P, x 1
500 ) − ∑

x 1
500 ⩽p<x 1
7.2 S (Bp; P, x 1
500 )

+ ∑

x 1
500 ⩽p2<p1<x 1
7.2 S (
Bp1p2; P, x 1
500 )

− ∑

x 1
500 ⩽p3<p2<p1<x 1
7.2 S (Bp1p2p3; P, p3) . (30)

By Iwaniec’s linear sieve method and arguments in [14] and [15] we have

S′
1 ⩾ (1 + o(1)) 1
eγ
 (
500f (500ϑ
′ 1
500
 ) − 500 ∫ 1
12

1
500
 F (500(ϑ0(t, 1
500 , 1
500 ) − t))
t dt

+ 500 ∫ 1
12

1
500
 ∫ t1

1
500
 f (500(ϑ0(t1, t2, 1
500 ) − t1 − t2))
t1t2 dt2dt1

− ∫ 1
12

1
500
 ∫ t1

1
500
 ∫ t2

1
500
 F ( (ϑ0(t1,t2,t3)−t1−t2−t3)
t3
 )

t1t2t
2
3 dt3dt2dt1


 C2x
(log x)2

⩾ 6.737438 C2x
(log x)2 (31)

and
 S′
2 ⩾ (1 + o(1)) 1
eγ
 (
500f (
500ϑ′ 1
500
 ) − 500 ∫ 1
7.2

1
500
 F (500(ϑ0(t, 1
500 , 1
500 ) − t))
t dt

+ 500 ∫ 1
7.2

1
500
 ∫ t1

1
500
 f (500(ϑ0(t1, t2, 1
500 ) − t1 − t2))
t1t2 dt2dt1

− ∫ 1
7.2

1
500
 ∫ t1

1
500
 ∫ t2

1
500
 F ( (ϑ0(t1,t2,t3)−t1−t2−t3)
t3
 )

t1t2t
2
3 dt3dt2dt1


 C2x
(log x)2

11

⩾ 4.008831 C2x
(log x)2 , (32)

where ϑ′ 1
500 = 16483
26750 and ϑ0(t1, t2, t3) is deﬁned as the same as in [15]. Similarly, for S′
3–S′
6 we
have
 S′
3 = ∑

x 1
12 ⩽p2<p1<x 1
7.2 S (
Bp1p2; P, x 1
12 )

= ∑

x 1
12 ⩽p2<p1<x 1
7.2 S (
Bp1p2; P, x 1
500 )

− ∑

x 1
500 ⩽p3<x 1
12 ⩽p2<p1<x 1
7.2 S (Bp1p2p3; P, p3) (33)

⩾ (1 + o(1)) 1
eγ
 (
500 ∫ 1
7.2

1
12
 ∫ t1

1
12
 f (500(ϑ0(t1, t2, 1
500 ) − t1 − t2))
t1t2 dt2dt1

− ∫ 1
7.2

1
12
 ∫ t1

1
12
 ∫ 1
12

1
500
 F ( (ϑ0(t1,t2,t3)−t1−t2−t3)
t3
 )

t1t2t
2
3 dt3dt2dt1


 C2x
(log x)2

⩾ 0.874549 C2x
(log x)2 , (34)

S′
4 = ∑

x 1
12 ⩽p2<x 1
7.2 ⩽p1<min(x 2
7 ,x 17
42 p−1
2 )
 S (
Bp1p2; P, x 1
12 )

= ∑

x 1
12 ⩽p2<x 1
7.2 ⩽p1<x 25
107 S (
Bp1p2; P, x 1
12 )

+ ∑

x 1
12 ⩽p2<x 1
7.2 <x 25
107 ⩽p1<min(x 2
7 ,x 17
42 p−1
2 )
 S (
Bp1p2; P, x 1
12 )

= ∑

x 1
12 ⩽p2<x 1
7.2 ⩽p1<x 25
107 S (
Bp1p2; P, x 1
500 )

− ∑

x 1
500 ⩽p3<x 1
12 ⩽p2<x 1
7.2 ⩽p1<x 25
107 S (Bp1p2p3; P, p3)

+ ∑

x 1
12 ⩽p2<x 1
7.2 <x 25
107 ⩽p1<min(x 2
7 ,x 17
42 p−1
2 )
 S (
Bp1p2; P, x 1
12 ) (35)

⩾ (1 + o(1)) 1
eγ
 (
500 ∫ 25
107

1
7.2
 ∫ 1
7.2

1
12
 f (500(ϑ0(t1, t2, 1
500 ) − t1 − t2))
t1t2 dt2dt1

− ∫ 25
107

1
7.2
 ∫ 1
7.2

1
12
 ∫ 1
12

1
500
 F ( (ϑ0(t1,t2,t3)−t1−t2−t3)
t3
 )

t1t2t
2
3 dt3dt2dt1

12

+ 12 ∫ 1
7.2

1
12
 ∫ min( 2
7 , 17
42 −t1)

25
107
 f (12(ϑ0(t2) − t1 − t2))
t1t2 dt2dt1
) C2x
(log x)2

⩾ 2.151637 C2x
(log x)2 , (36)

S′
5 = ∑

x 1
12 ⩽p<x 25
107 S (
Bp; P, x 1
12 )

= ∑

x 1
12 ⩽p<x 25
107 S (
Bp; P, x 1
500 )

− ∑

x 1
500 ⩽p2<x 1
12 ⩽p1<x 25
107 S (
Bp1p2; P, x 1
500 )

+ ∑

x 1
500 ⩽p3<p2<x 1
12 ⩽p1<x 25
107 S (Bp1p2p3; P, p3) (37)

⩽ (1 + o(1)) 1
eγ
 (
500 ∫ 25
107

1
12
 F (500(ϑ0(t, 1
500 , 1
500 ) − t))
t dt

− 500 ∫ 25
107

1
12
 ∫ 1
12

1
500
 f (500(ϑ0(t1, t2, 1
500 ) − t1 − t2))
t1t2 dt2dt1

+ ∫ 25
128

1
12
 ∫ 1
12

1
500
 ∫ t2

1
500
 F ( (ϑ0(t1,t2,t3)−t1−t2−t3)
t3
 )

t1t2t
2
3 dt3dt2dt1


 C2x
(log x)2

⩽ 6.231479 C2x
(log x)2 , (38)

S′
6 = ∑

x 25
107 ⩽p<x 2
7 −ε S (Bp; P, x 1
12 )

= ∑

x 25
107 ⩽p<x 2
7 −ε S (Bp; P, x 1
500 )

− ∑

x 1
500 ⩽p2<x 1
12 <x 25
107 ⩽p1<x 2
7 −ε S (Bp1p2; P, p2) (39)

⩽ (1 + o(1)) 1
eγ
 (
500 ∫ 2
7

25
107
 F (500(ϑ0(t, 1
500 , 1
500 ) − t))
t dt

− ∫ 2
7

25
107
 ∫ 1
12

1
500
 f ( (ϑ0(t1)−t1−t2)
t2
 )

t1t
2
2 dt2dt1


 C2x
(log x)2

⩽ 2.112817 C2x
(log x)2 , (40)

13

where ϑ0(t) is deﬁned as the same as in [15]. For other terms, by the arguments in [3] and
[20], we have

S′
7 ≪ εC2x
(log x)2 , (41)

S′
8 ⩽ (1 + o(1)) 12
eγ
 (∫ ( 4
7 − 2
7 )12

( 11
20 − 29
100 )12
 F (t)
2 × 12 − tdt

)
 ⩽ 0.111039 C2x
(log x)2 , (42)

S′
9 ⩽ (1 + o(1)) 12
eγ
 (∫ ( 11
20 − 29
100 )12

( 11
20 − 1
3 )12
 F (t)
11
20 × 12 − tdt

)
 ⩽ 1.169696 C2x
(log x)2 , (43)

S′
10 ≪ εC2x
(log x)2 , (44)

S′
11 ⩽ (1 + o(1))
 

4 ∫ 1
10
 1
12
1+2t1
2 ⩾ 2+t2
4
 ∫ 2
5

1
3
 1
t1t2 (1 + 2t1) (1 − t1 − t2) dt2dt1

+ 8 ∫ 1
10
 1
12
1+2t1
2 ⩽ 2+t2
4
 ∫ 2
5

1
3
 1
t1t2 (2 + t2) (1 − t1 − t2) dt2dt1

+ 4 ∫ 1
10
 1
12
1+2t1
2 ⩾1−t2
 ∫ 1−t1
2

2
5
 1
t1t2 (1 + 2t1) (1 − t1 − t2) dt2dt1

+ 2 ∫ 1
10
 1
12
1+2t1
2 ⩽1−t2
 ∫ 1−t1
2

2
5
 1
t1t2 (1 − t2) (1 − t1 − t2) dt2dt1

+ 16 ∫ 1
5
 1
10
5−2t1
8 ⩾ 2+t2
4
 ∫ 2
5

1
3
 1
t1t2 (5 − 2t1) (1 − t1 − t2) dt2dt1

+ 8 ∫ 1
5
 1
10
5−2t1
8 ⩽ 2+t2
4
 ∫ 2
5

1
3
 1
t1t2 (2 + t2) (1 − t1 − t2) dt2dt1

+ 16 ∫ 1
5
 1
10
5−2t1
8 ⩾1−t2
 ∫ 1−t1
2

2
5
 1
t1t2 (5 − 2t1) (1 − t1 − t2) dt2dt1

+ 2 ∫ 1
5
 1
10
5−2t1
8 ⩽1−t2
 ∫ 1−t1
2

2
5
 1
t1t2 (1 − t2) (1 − t1 − t2)dt2dt1

+ 8 ∫ 3
14

1
5
 ∫ 1−t1
2

1
3
 1
t1t2 (2 + t2) (1 − t1 − t2) dt2dt1

+ 8 ∫ 1
4

3
14
 ∫ 1−t1
2

1
3
 1
t1t2 (2 + t2) (1 − t1 − t2)dt2dt1

14

+ 8 ∫ 2
7

1
4
 ∫ 1−t1
2

1
3
 1
t1t2 (2 + t2) (1 − t1 − t2)dt2dt1

+ 8 ∫ 2
7

1
3
 ∫ 1−t1
2

1
3
 1
t1t2 (2 + t2) (1 − t1 − t2) dt2dt1
) C2x
(log x)2

⩽ 2.02916 C2x
(log x)2 , (45)

S′
12 ⩽ (1 + o(1))
 

16 ∫ 1
5
 1
7.2
5−2t1
8 ⩾ 2+t2
4
 ∫ 2
5

2
7
 1
t1t2 (5 − 2t1) (1 − t1 − t2) dt2dt1

+ 8 ∫ 1
5
 1
7.2
5−2t1
8 ⩽ 2+t2
4
 ∫ 2
5

2
7
 1
t1t2 (2 + t2) (1 − t1 − t2) dt2dt1

+ 16 ∫ 1
5
 1
7.2
5−2t1
8 ⩾1−t2
 ∫ 1−t1
2

2
5
 1
t1t2 (5 − 2t1) (1 − t1 − t2) dt2dt1

+ 2 ∫ 1
5
 1
7.2
5−2t1
8 ⩽1−t2
 ∫ 1−t1
2

2
5
 1
t1t2 (1 − t2) (1 − t1 − t2)dt2dt1

+ 16 ∫ 3
14
 1
5
5−2t1
8 ⩾ 2+t2
4
 ∫ 1−t1
2

2
7
 1
t1t2 (5 − 2t1) (1 − t1 − t2) dt2dt1

+ 8 ∫ 3
14
 1
5
5−2t1
8 ⩽ 2+t2
4
 ∫ 1−t1
2

2
7
 1
t1t2 (2 + t2) (1 − t1 − t2) dt2dt1

+ 12 ∫ 1
4
 3
14
3+2t1
6 ⩾ 2+t2
4
 ∫ 1−t1
2

2
7
 1
t1t2 (3 + 2t1) (1 − t1 − t2) dt2dt1

+ 8 ∫ 1
4
 3
14
3+2t1
6 ⩽ 2+t2
4
 ∫ 1−t1
2

2
7
 1
t1t2 (2 + t2) (1 − t1 − t2)dt2dt1

+ 6 ∫ 2
7
 1
4
2−t1
3 ⩾ 2+t2
4
 ∫ 1−t1
2

2
7
 1
t1t2 (2 − t2) (1 − t1 − t2) dt2dt1

+ 8 ∫ 2
7
 1
4
2−t1
3 ⩽ 2+t2
4
 ∫ 1−t1
2

2
7
 1
t1t2 (2 + t2) (1 − t1 − t2) dt2dt1


 C2x
(log x)2

⩽ 1.77427 C2x
(log x)2 , (46)

15

S′
13 ⩽ (1 + o(1)) ∫ 1
3

2
7
 log ( 1
t − 2)

t(2 + t)(1 − t) dt ⩽ 0.16203 C2x
(log x)2 , (47)

S′
14 ⩽ (1 + o(1))
 

4 ∫ 1
10

1
12
 ∫ 1
7.2

t1
 ∫ 1
7.2

t2
 ∫ 1
7.2

t3
 ω ( 1−t1−t2−t3−t4
t2
 )

t1t
2
2t3t4 (1 + 2t1) dt4dt3dt2dt1

+ 16 ∫ 1
7.2

1
10
 ∫ 1
7.2

t1
 ∫ 1
7.2

t2
 ∫ 1
7.2

t3
 ω ( 1−t1−t2−t3−t4
t2
 )

t1t
2
2t3t4 (5 − 2t1) dt4dt3dt2dt1


 C2x
(log x)2

⩽ 0.05331 C2x
(log x)2 , (48)

S′
15 ⩽ (1 + o(1))
 

4 ∫ 1
10

1
12
 ∫ 5
42

t1
 ∫ 5
42

t2
 ∫ 2
7

1
7.2
 ω ( 1−t1−t2−t3−t4
t2
 )

t1t
2
2t3t4 (1 + 2t1) dt4dt3dt2dt1

+ 16 ∫ 5
42

1
10
 ∫ 5
42

t1
 ∫ 5
42

t2
 ∫ 2
7

1
7.2
 ω ( 1−t1−t2−t3−t4
t2
 )

t1t
2
2t3t4 (5 − 2t1) dt4dt3dt2dt1


 C2x
(log x)2

⩽ 0.10505 C2x
(log x)2 , (49)

S′
16 ⩽ (1 + o(1))
 

4 ∫ 1
10

1
12
 ∫ 5
42

t1
 ∫ 1
7.2

5
42
 ∫ 17
42 −t3

1
7.2
 ω ( 1−t1−t2−t3−t4
t2
 )

t1t
2
2t3t4 (1 + 2t1) dt4dt3dt2dt1

+ 16 ∫ 5
42

1
10
 ∫ 5
42

t1
 ∫ 1
7.2

5
42
 ∫ 17
42 −t3

1
7.2
 ω ( 1−t1−t2−t3−t4
t2
 )

t1t
2
2t3t4 (5 − 2t1) dt4dt3dt2dt1


 C2x
(log x)2

⩽ 0.12188 C2x
(log x)2 , (50)

S′
17 ⩽ (1 + o(1))
 

4 ∫ 1
10

1
12
 ∫ 1
7.2

5
42
 ∫ 1
7.2

t2
 ∫ 17
42 −t3

1
7.2
 ω ( 1−t1−t2−t3−t4
t2
 )

t1t
2
2t3t4 (1 + 2t1) dt4dt3dt2dt1

+ 16 ∫ 5
42

1
10
 ∫ 1
7.2

5
42
 ∫ 1
7.2

t2
 ∫ 17
42 −t3

1
7.2
 ω ( 1−t1−t2−t3−t4
t2
 )

t1t
2
2t3t4 (5 − 2t1) dt4dt3dt2dt1


 C2x
(log x)2

⩽ 0.04359 C2x
(log x)2 , (51)

S′
18 ⩽ (1 + o(1))
 

16 ∫ 1
7.2

5
42
 ∫ 1
7.2

t1
 ∫ 1
7.2

t2
 ∫ 17
42 −t3

1
7.2
 ω ( 1−t1−t2−t3−t4
t2
 )

t1t
2
2t3t4 (5 − 2t1) dt4dt3dt2dt1




⩽ 0.00608 C2x
(log x)2 . (52)

16

Finally, by Lemma 2.2 and (29)–(52) we get

3S′
1 + S′
2 + S′
3 + S′
4 ⩾ 27.247319 C2x
(log x)2 ,

2S′
5 + 2S′
6 + S′
7 + S′
8 + S′
9 + S′
10 + S′
11 + S′
12

+ 2S′
13 + S′
14 + S′
15 + S′
16 + S′
17 + S′
18 ⩽ 22.426727 C2x
(log x)2 ,

4π1,2(x) ⩾ (3S′
1 + S′
2 + S′
3 + S′
4)

− (2S′
5 + 2S′
6 + S′
7 + S′
8 + S′
9 + S′
10 + S′
11 + S′
12
+ 2S′
13 + S′
14 + S′
15 + S′
16 + S′
17 + S′
18)

⩾ 4.82 C2x
(log x)2 ,

π1,2(x) ⩾ 1.205 C2x
(log x)2 .

Theorem 1.3 is proved.
 References

[1] Y. Cai. A remark on Chen’s theorem. Acta Arith., 102(4):339–352, 2002.
[2] Y. Cai. On Chen’s theorem. II. J. Number Theory, 128(5):1336–1357, 2008.
[3] Y. Cai. A remark on Chen’s theorem (II). Chinese Ann. Math. Ser. B, 29(6):687–698, 2008.
[4] Y. Cai and M. Lu. On Chen’s theorem. In Analytic number theory (Beijing/Kyoto, 1999), volume 6 of
Dev. Math., pages 99–119. Kluwer Acad. Publ., Dordrecht, 2002.
[5] J. R. Chen. On the representation of a larger even integer as the sum of a prime and the product of at
most two primes. Sci. Sinica, 16:157–176, 1973.
[6] J. R. Chen. Further improvement on the constant in the proposition ‘1+2’: On the representation of a
large even integer as the sum of a prime and the product of at most two primes (II). Sci. Sinica, pages
477–494(in Chinese), 1978.
[7] J. R. Chen. On the representation of a large even integer as the sum of a prime and the product of at
most two primes. II. Sci. Sinica, 21(4):421–430, 1978.
[8] J. R. Chen. On some problems in prime number theory. In S´eminaire de th´eorie des nombres, Paris
1979-80, pages 167–170. Birkh¨auser, Boston, 1981.
[9] E. Fouvry and F. Grupp. On the switching principle in sieve theory. J. Reine Angew. Math.,
1986(370):101–126, 1986.
[10] H. Halberstam. A proof of Chen’s theorem. In Journ´ees Arithm´etiques de Bordeaux (Conf., Univ.
Bordeaux, 1974),, Ast´erisque, No. 24-25,, pages 281–293. ,, 1975.
[11] H. Halberstam and H.-E. Richert. Sieve methods, volume No. 4. Academic Press [Harcourt Brace Jo-
vanovich, Publishers], London-New York, 1974.
[12] H. Li. Additive representations of natural numbers. Ramanujan J., 60(4):999–1024, 2023.
[13] R. Li. Remarks on additive representations of natural numbers. arXiv e-prints, page arXiv:2309.03218,
September 2023.
[14] J. D. Lichtman. A modiﬁcation of the linear sieve, and the count of twin primes. arXiv e-prints, page
arXiv:2109.02851, September 2021.
[15] J. D. Lichtman. Primes in arithmetic progressions to large moduli, and Goldbach beyond the square-root
barrier. arXiv e-prints, page arXiv:2309.08522, August 2023.
[16] H.-Q. Liu. On the prime twins problem. Sci. Sinica, 33(3):281–298, 1990.
[17] P. M. Ross. On linear combinations of primes and numbers having at most two prime factors. Ph.D.
Thesis, University of London, 1976.
[18] J. Wu. Sur la suite des nombres premiers jumeaux. Acta Arith., 55(4):365–394, 1990.
17

[19] J. Wu. Chen’s double sieve, Goldbach’s conjecture and the twin prime problem. Acta Arith., 114(3):215–
273, 2004.
[20] J. Wu. Chen’s double sieve, Goldbach’s conjecture and the twin prime problem. II. Acta Arith.,
131(4):367–387, 2008.

The High School Affiliated to Renmin University of China International Curriculum
Center, Beijing, China
Email address: runbo.li.carey@gmail.com
 18
