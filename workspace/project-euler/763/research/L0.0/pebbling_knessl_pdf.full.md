<!-- source: https://arxiv.org/pdf/1009.5731 | converted from PDF -->

arXiv:1009.5731v1  [math.CO]  29 Sep 2010
An Explicit Solution to the Chessboard Pebbling

Problem

Qiang Zhen∗ and Charles Knessl†

September 24, 2010

Abstract

We consider the chessboard pebbling problem analyzed by Chung, Graham, Morrison

and Odlyzko [3]. We study the number of reachable conﬁgurations G(k) and a related

double sequence G(k, m). Exact expressions for these are derived, and we then consider

various asymptotic limits.

Keywords: Chessboard pebbling; reachable conﬁgurations; asymptotics.

1 Introduction

The following problem has attracted some attention recently. We begin with an inﬁnite

chessboard, which consists of the lattice points {(i, j) : i, j ≥ 0} in the ﬁrst quadrant. We

∗Corresponding author. Department of Mathematics and Statistics, University of North Florida, 1 UNF
Dr, Bldg 14/2731, Jacksonville, FL 32224-7699, USA. Email: q.zhen@unf.edu. Tel: (904) 620-2042. Fax:
(904) 620-2818.
†Department of Mathematics, Statistics, and Computer Science, University of Illinois at Chicago, 851
South Morgan Street (M/C 249), Chicago, IL 60607-7045, USA. Email: knessl@uic.edu. This author’s work
was partly supported by NSA grant H 98230-08-1-0102.

1

refer to an individual lattice point as a “cell”. We start with a single pebble placed at (0, 0).

The ﬁrst “step” consists of removing this pebble and placing two pebbles at the cells (0, 1)

and (1, 0). At each subsequent step we remove a pebble at cell (i, j) and place two pebbles at

cells (i + 1, j) and (i, j + 1), provided that the latter two cells are unoccupied. We consider

all possible choices of (i, j). After k steps, there will be a total of k + 1 pebbles on the board,

in various arrangements or conﬁgurations.

We let G(k) be the total number of reachable conﬁgurations with k pebbles. We deﬁne

the level sets L(l) = {(i, j) : i + j = l}, so that ∪l≥0L(l) is the entire quadrant. The original

problem, posed by Kontsevich [1], was to show that L(1) ∪ L(2) ∪ L(3) is unavoidable, in that

such a set must contain at least one pebble for any reachable conﬁguration. A partial analysis

of this fact was published thereafter by Khodulev [2]. The ﬁrst complete proof was given by

Chung, Graham, Morrison and Odlyzko [3]. It was also shown in [3] that L(1) ∪ L(2) is an

unavoidable set, as well as certain properties relating to the number of unavoidable sets with

k pebbles, including the geometric growth rate of this quantity as k → ∞. In [4], Knessl

obtained some further asymptotic properties relating to the enumeration of unavoidable sets.

Various extensions of this problem are studied by Eriksson [5] and Warren [6].

Suppose we allow more than one pebble per cell and start with an initial conﬁguration of

one pebble in cells (0, m + 1) and (m + 1, 0) and two pebbles in each of the cells (1, m), (2, m −

1), ..., (m − 1, 2), (m, 1). Thus there are a total of 2m + 2 pebbles in the level set L(m + 1),

and we assume that L(M) are empty for M > m + 1. Again the pebble at (i, j) can only be

moved if the cells (i+ 1, j) and (i, j + 1) are empty. Let the number of reachable conﬁgurations

corresponding to this starting arrangement be denoted by G(k, m). In [3], a recurrence relation

for G(k, m) is derived, and it is shown that, for k ≥ 2, G(k, 0) = G(k). It is also established

that as k → ∞, G(k) ∼ c∗a
k where a = 2.321642199494 · · · and c∗ = 0.12268707 · · · . These

constants are characterized in terms of a continued fraction representation of the generating

2

function of G(k). In [7], Knessl obtained a more explicit analytic characterization of the

growth rate a of the number of reachable conﬁgurations, and showed that this constant can

be obtained by solving a transcendental equation that involves two series, each resembling

Jacobi elliptic functions. Other asymptotic properties of G(k, m) for k and/or m → ∞ are

also established in [7].

In this paper, we derive an exact expression for the number of reachable conﬁgurations

G(k) and G(k, m). Using the exact expression, we recover the asymptotic results given in [7],

and obtain more explicit analytic expressions for each asymptotic scale. These asymptotic

scales are k → ∞ with m = O(1); k and m → ∞ simultaneously with 2k/m
2 > 1; and

k, m → ∞ with l = k − m(m + 5)/2 = O(1).

The paper is organized as follows. In Section 2, we state the basic equations and summarize

the main results for G(k, m) in Theorem 2.1 and 2.2, and for G(k) in Corollary 2.1 and 2.2.

In Section 3, we provide brief derivations.

2 Summary of results

It is shown in [3] that G(k, m) satisﬁes the following recurrence equations:

G(k, 0) = 2G(k − 1, 0) + G(k, 1) + δ(k, 2) (2.1)

G(k, 1) = G(k − 3, 0) + 2G(k − 2, 1) + G(k − 1, 2) + G(k − 4, 1) (2.2)

G(k, m) = G(k − m − 2, m − 1) + 2G(k − m − 1, m) + G(k − m, m + 1), m ≥ 2.(2.3)

Here δ(i, j) is the Kronecker delta symbol. As shown in [7], the boundary condition (2.1) can

be replaced by
 G(k, 0) = 2k−2 +
 k∑

l=1 2k−lG(l, 1), k ≥ 2. (2.4)

3

Using (2.4) in (2.2), G(k, 0) can be eliminated, which leads to

G(k, 1) = 2G(k − 2, 1) + G(k − 1, 2) + G(k − 4, 1) + 2k−5 +
 k−3∑

l=1 2k−l−3G(l, 1), k ≥ 5. (2.5)

We introduce a generation function of G(k, m), with

Vm(z) = (−1)mz−m ∞∑

k=0 G(k, m)zk. (2.6)

By explicitly solving for Vm(z), we obtain the following integral representation for G(k, m).

Theorem 2.1 The number of reachable conﬁgurations G(k, m) has the following exact ex-

pression
 G(k, m) = 1
2πi
 ∮

C(−1)mzm−k−1Vm(z)dz. (2.7)

Here C is a closed counterclockwise contour around the origin in the z-plane, with |z| < 1/2

on C,
 Vm(z) = z1+m(m+1)/2

S(z)
 ∞∑

n=1(−1)n+mzn(n+1)/2+nm m∏

L=0
 1
1 − zL+n
 n−1∏

L=1
 1
(1 − zL)2 (2.8)

and
 S(z) = (2z2 − 3z + 2)S1(z) − (4z2 − 4z + 1)S2(z) + 2z2 − z − 1, (2.9)

where
 Sk(z) =
 ∞∑

i=1 (−1)i+1zi2/2+(2k−1)i/2 i∏

j=1
 1
(1 − zj)2 . (2.10)

Since the total number of reachable conﬁgurations for the original problem is G(k) =

G(k, 0), using (2.7) in (2.4) with m = 1 we get the exact expression of G(k):

4

Corollary 2.1 An exact expression for the total number of reachable conﬁgurations G(k) is

G(k) = 2k−2 + 1
2πi
 ∮
C
 2k − z−k

1 − 2z V1(z)dz,

where V1(z) is given by (2.8) with m = 1.

Using (2.7), we obtain the following asymptotic expressions for G(k, m). These asymp-

totic results were ﬁrst obtained in [7], but there some parameters could only be determined

numerically.

Theorem 2.2 The number of reachable conﬁgurations G(k, m) has the following asymptotic

expressions:

1. When k → ∞ and m = O(1),

G(k, m) ∼ zm(m+3)/2−k
∗ S′(z∗)
 ∞∑

n=1(−1)n+1zn(n+1)/2+nm
∗
 m∏

L=0
 1
1 − zL+n
∗
 n−1∏

L=1
 1
(1 − zL
∗ )2 , (2.11)

where z∗ > 0 is the unique root of S(z) = 0 for |z| < 1/2 and S′(z∗) is the ﬁrst derivative

of S(z) evaluated at z = z∗. The numerical approximation of z∗ to 15 decimal places is

given below
 z∗ = 0.43072 95931 37930 · · · .

2. When k, m → ∞ with 2k/m
2 > 1,

G(k, m) ∼ zm(m+5)/2−k+1
∗ S′(z∗)
 ∞∏

L=0
 1
1 − zL+1
∗ . (2.12)

3. When l = k − m(m + 5)/2 and 2 ≤ l ≤ m + 3,

G(k, m) = − 1
(l − 2)! lim
z→0 dl−2

dzl−2
 [ 1
S(z)
 ∞∏

L=0
 1
1 − zL+1
 ]. (2.13)

5

When k and m → ∞ with l > m + 3, (2.13) holds asymptotically, and then reduces to

(2.12).

Now we consider the asymptotic expression for G(k) when k → ∞. Since z∗ < 1/2, we can

neglect the term 2k−2 in the right of (2.4) and use (2.11) in (2.4) with m = 1. Since z∗ < 1/2,

we have k∑

l=1 2k−lz−l
∗ ∼ z−k
∗
1 − 2z∗ , k → ∞,

and hence the following corollary.

Corollary 2.2 The total number of reachable conﬁgurations G(k) has the following asymp-

totic expression, when k → ∞:

G(k) ∼ z2
∗
(1 − 2z∗)S′(z∗)
 [ ∞∑

n=1
 (−1)n+1zn(n+3)/2
∗
(1 − zn
∗ )(1 − zn+1
∗ )
 n−1∏

L=1
 1
(1 − zL
∗ )2
 ]( 1
z∗
 )k.

Here S(z) is as in (2.9) and (2.10).

3 Brief derivations

Using the generating function (2.6) in (2.3), we obtain the following recurrence equation for

Vm(z)
 Vm+1(z) + Vm−1(z) = (2 − z−m−1)Vm(z).

We notice that this equation is of the same form as (3.12) given in [7], with z = 1/a. Two

linearly independent solutions are given by (3.29) and (3.30) in [7]. We reject the growing

solution given by (3.30) in [7] since we expect that Vm(z) will be bounded as m → ∞. Hence,

6

we have
 Vm(z) = C(z) 2π
log z exp ( π2

2 log z
 ) ∞∑

J=m+1(−1)m+J+1z−(m−J)2/2−(m−J)/2

×
 m∏

L=0
 1
1 − zL−J
 ∞∏

L=m+1, L̸=J
 1
(1 − zL−J )2

= C(z) 2π
log z exp ( π2

2 log z
 ) ∞∑

n=1(−1)n+1z−n2/2+n/2 m∏

L=0
 1
1 − z−L−n

×
 ∞∏

L=1, L̸=n
 1
(1 − zL−n)2 , (3.1)

where C(z) is independent of m. We note that we can rewrite the two products in (3.1) as

follows: m∏

L=0
 1
1 − z−L−n = (−1)m+1z(n+m/2)(m+1) m∏

L=0
 1
1 − zL+n (3.2)

and ∞∏

L=1, L̸=n
 1
(1 − zL−n)2 = zn(n−1) n−1∏

L=1
 1
(1 − zL)2
 ∞∏

L=1
 1
(1 − zL)2 . (3.3)

Using (3.2) and (3.3) in (3.1) leads to

Vm(z) = C(z) 2π
log z exp ( π2

2 log z
 ) ∞∏

L=1
 1
(1 − zL)2
 { ∞∑

n=1(−1)n+mzn2/2−n/2+(n+m/2)(m+1)

×
[ m∏

L=0
 1
1 − zL+n
 ][ n−1∏

L=1
 1
(1 − zL)2
 ]}
. (3.4)

To determine C(z), we use (2.6) in the boundary condition (2.5), which yields

(
z4 + 2z2 − 1 + z3

1 − 2z
 )V1(z) − z2V2(z) = z4

1 − 2z . (3.5)

7

We note that (3.5) holds for |z| < 1/2. We introduce the function Um(z)

Um(z) =
 ∞∑

n=1(−1)n+mzn2/2−n/2+(n+m/2)(m+1) m∏

L=0
 1
1 − zL+n
 n−1∏

L=1
 1
(1 − zL)2 ,

and then Vm(z) in (3.4) is

Vm(z) = C(z) 2π
log z exp ( π2

2 log z
 )[ ∞∏

L=1
 1
(1 − zL)2
 ]
Um(z). (3.6)

Using (3.6) with m = 1 and m = 2 in (3.5), we obtain C(z) as

C(z) = [
(−2z5 + z4 − 3z3 + 2z2 + 2z − 1)U1(z) − z2(1 − 2z)U2(z)]−1

×log z
2π exp ( − π2

2 log z
 )
z4 ∞∏

L=1
(1 − zL)2. (3.7)

Instead of using (3.7) in (3.6), we introduce the functions Sk(z) deﬁned in (2.10) and rewrite

C(z) in terms of the Sk(z). (The reason for making this change is that it allows us to verify

the equivalence of S(z) = 0 with equation (3.39) in [7], which we will discuss later.) Using

(2.10), U1(z) and U2(z) in (3.7) can be expressed as

U1(z) = −S1(z) + (1 + 1
z
 )S2(z) − 1
z S3(z) (3.8)

and
 U2(z) = −S1(z) + (
1 + 1
z + 1
z2
 )S2(z) − ( 1
z + 1
z2 + 1
z3
 )S3(z) + 1
z3 S4(z). (3.9)

We rewrite Sk(z) in (2.10) as

Sk(z) =
 ∞∑

i=1 (−1)i+1zi2/2+(2k−1)i/2 i+1∏

j=1
 1
(1 − zj)2 (1 − 2zi + z2i),

8

and then, after some calculation, we obtain the following recurrence equation

z1−kSk−1(z) + (1 − 2z1−k)Sk(z) + z1−kSk+1(z) = 1. (3.10)

Hence, we can use (3.10) with k = 2 and k = 3 to eliminate S3(z) and S4(z) from (3.8) and

(3.9). Thus, after some simpliﬁcation, we obtain C(z) as

C(z) = z
S(z) log z
2π exp ( − π2

2 log z
 ) ∞∏

L=1
(1 − zL)2, (3.11)

where S(z) is deﬁned in (2.9). Using (3.11) in (3.6), we obtain (2.8) in Theorem 2.1. Then

we have the integral expression of G(k, m) in (2.7).

In the remainder of this section, we discuss the asymptotic approximations to G(k, m). We

ﬁrst consider k → ∞ and m = O(1). By using Rouch´e’s theorem, or by plotting S(z) given

in (2.9) numerically, we notice that there is a single real root for |z| < 1/2. We denote this

single root as z∗, which satisﬁes S(z∗) = 0. Then in the z-plane with |z| < 1/2, the integrand

in (2.7) has a simple pole at z = z∗, which is the dominant singularity. We use the residue

theorem to evaluate the integral in (2.7) asymptotically, which yields (2.11). We note that

it’s not hard to verify that S(z) = 0 is equivalent to (3.39) in [7], after we substitute 1/z for a

in (3.39). Thus z−1
∗ = a, whose numerical approximation to 100 decimal places is given in [7].

By comparing (2.11) in this paper with formula (3.37) in [7], we obtain an analytic expression

for the constant c1 in (3.38) in [7] as follows:

c1 = −log z∗
2π exp ( − π2

2 log z∗
 ) 1
S′(z∗)
 ∞∏

j=1(1 − zj
∗)2. (3.12)

By evaluating (3.12) numerically, we ﬁnd that the numerical values of c1 and c1K∗ provided

in (3.42) and (3.43) in [7] are only correct to about 5 decimal places, though they are given

9

to 15 places. The correct values to 15 decimal places are

c1 = 2.02740 20474 68498 · · ·

and
 c1K∗ = 0.28777 77049 35052 · · · .

In the limit when k, m → ∞ simultaneously, the n = 1 term in (2.11) dominates, which

yields (2.12). This recovers the result given in (4.18) in [7], but now with c1 computed

explicitly.

Next, we consider k and m large with l = k − m(m + 5)/2 = O(1). Note that l = 2

corresponds to the smallest number of possible conﬁgurations, as G(k, m) = 0 for l ≤ 1.

Following [7] we denote G(k, m) as W (l, m) and rewrite (2.7) as

G(k, m) ≡ W (l, m) = 1
2πi
 ∮
C
 1
zl−1 1
S(z)
 ∞∑

n=1(−1)nz(n−1)(n/2+m+1)

×
 m∏

L=0
 1
1 − zL+n
 n−1∏

L=1
 1
(1 − zL)2 dz. (3.13)

For a suﬃciently small closed contour C around the origin in the z-plane and l ≥ 2, z = 0 is

the only pole inside of C, and it is of order l − 1. Thus, using the residue theorem in (3.13)

leads to
 W (l, m) = 1
(l − 2)! lim
z→0 dl−2

dzl−2
 { 1
S(z)
 ∞∑

n=1(−1)nz(n−1)(n/2+m+1)

×
 m∏

L=0
 1
1 − zL+n
 n−1∏

L=1
 1
(1 − zL)2
 }. (3.14)

10

The ﬁrst two terms from the inﬁnite sum in the right-hand side of (3.14) are

−
 m∏

L=0
 1
1 − zL+1 + zm+2

(1 − z)2
 m∏

L=0
 1
1 − zL+2 , (3.15)

and the remaining terms are of order O(z2m+5) as z → 0. We notice that after taking l − 2

derivatives, the second term in (3.15) is of order O(zm−l+4) as z → 0. This implies that as

long as m − l + 4 ≥ 1, i.e., l ≤ m + 3, only the n = 1 term in the inﬁnite sum in (3.14)

contributes to the derivative at z = 0, which yields

W (l, m) = − 1
(l − 2)! lim
z→0 dl−2

dzl−2
 [ 1
S(z)
 m∏

L=0
 1
1 − zL+1
 ]
, 2 ≤ l ≤ m + 3. (3.16)

Rewriting the expression in the brackets in (3.16) as

1
S(z)
 m∏

L=0
 1
1 − zL+1 = 1
S(z)
 ∞∏

L=0
 1
1 − zL+1
 ∞∏

L=m+1
(1 − zL+1),

we see that (3.16) is independent of m. This leads to (2.13), and gives an analytic expression

for W0(l), which appears in [7] but there no explicit expression is given. This concludes our

derivation.

References

[1] M. Kontsevich, Problem M715, Kvant., November 1981, p. 21. (In Russian.)

[2] A. Khodulev, Pebble spreading, Kvant., July 1982, p. 28–31 and 55. (In Russian.)

[3] F. Chung, R. Graham, J. Morrison, A. Odlyzko, Pebbling a chessboard, Amer. Math.

Monthly 102 (1995) 113–123.
 11

[4] C. Knessl, Geometrical optics and chessboard pebbling, Appl. Math. Lett. 14 (2001) 365–

373.

[5] H. Eriksson, Pebblings, Electron. J. Combin. 2 (1995), Research Paper 7, 18 pp.

[6] R. H. Warren, Disks on a chessboard, Amer. Math. Monthly 103 (1996), 305–307.

[7] C. Knessl, On the number of reachable conﬁgurations for the chessboard pebbling problem,

Math. Comput. Modelling 47 (2008), 127–139.

12
