<!-- source: http://elib.mi.sanu.ac.rs/files/journals/flmt/177/flmn177p4613-4636.pdf | converted from PDF -->

Filomat 35:14 (2021), 4613–4636
https://doi.org/10.2298/FIL2114613P Published by Faculty of Sciences and Mathematics,
University of Nivs, Serbia
Available at: http://www.pmf.ni.ac.rs/filomat

From Euclid to Corner Sums – a Trail of Telescoping Tricks

Pedro Patr´ıcio
a, Robert E. Hartwigb

aCMAT – Centro de Matem´atica and Departamento de Matem´atica, Universidade do Minho, 4710-057 Braga, Portugal.
bMathematics Department, North Carolina State University, Raleigh, NC 27695-8205, U.S.A.

Abstract. Euclid’s algorithm is extended to binomials, geometric sums and corner sums. Two-sided
non-commuting, non-constant linear diﬀerence equations will be solved, and the solution is applied to
corner sums, thereby presenting an explicit formula for the generator of the bi-module spanned by the two
starting corner sums.

1. Introduction

Euclid’s Algorithm is, without question, one of the most important “super algorithms” in mathematics.
It is fast and can be executed eﬃciently via recurrence relations. In this paper we shall extend this algorithm
to binomials, geometric sums and corner sums.
“Telescoping sums” appear in many branches of mathematics, from block matrices to convergence and
from iteration to polynomial division.
The most common telescoping sum is the “corner sum”

Γk(x, c, y) = xk−1c + x
k−2cy + .. + xcy
k−2 + cy
k−1, (1)

in which the parameters need not commute! Indeed, we may consider elements from an arbitrary (non
necessarily abelian) ring R with unity 1. These sums arise naturally when powering a triangular matrix:
the corner element is precisely Γk(x, c, y). We shorten Γk(x, 1, y) to Γk(x, y).
These sums are a generalization of the Diﬀerence Quotient

x
n − y
n

x − y = x
n−1 + x
n−2y + · · · + y
n−1,

for two commuting variables x and y.

2020 Mathematics Subject Classiﬁcation. Primary 39A06
Keywords. Telescoping Sum, Corner Sum, Polynomials, Recurrence Relation
Received: 30 October 2020; Accepted: 07 February 2021
Communicated by Dragan S. Djordjevi´c
Research partially ﬁnanced by Portuguese Funds through FCT (Fundac¸ ˜ao para a Ciˆencia e a Tecnologia) within the Projects
UIDB/00013/2020 and UIDP/00013/2020.
Email addresses: pedro@math.uminho.pt (Pedro Patr´ıcio), hartwig@unity.ncsu.edu (Robert E. Hartwig)

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4614

Corner sums can be expressed in terms of Hankel matrices which have the form

H =
 

 a1 a2 · · · an
a2 an 0
... .. .

an 0
 
 =
 n∑

i=1 aiHi where Hi =
 

 0 · · · 1 · · · 0
... .. . ...

1 .. .

... .. .

0 · · · 0
 

 (2)

has its i-th counter diagonal ﬁlled with ones.
Since Γk(x, c, y) is a bilinear form we may express it as

Γk(x, c, y) = [1, x, .., x
n−1](cHk)
 

 1
y
...
yn−1
 
 = xT(cHk)y. (3)

On the other hand, if we introduce a polynomial form f (x) = a1 + a2x + .. + anx
n−1, then we also have the
bilinear form

W f (x, y) = x
TH f y = [1, x, .., x
n−1]
 

 a1 a2 · · · an
a2 an 0
... .. .

an 0
 

 

 1
y
...
yn−1
 
 =
 n∑

k=1 Γk(x, ak, y) (4)

where H f =
 

 a1 a2 · · · an
a2 an 0
... .. .

an 0
 

. As such we see that Hk+1 = Hxk .

Corner sums appear naturally when we examine matrix equations and matrix powering. For example, if

AX−XB = C, then AkX−XBk = Γk(A, C, B). Likewise when we power a block triangular matrix M = [ x c
0 y
 ]

it follows that

Mk = [ x c
0 y
 ]k = [ x
k Γk(x, c, y)
0 y
k
 ] . (5)

As such we see that corner sums appear whenever we block diagonalize matrices to obtain canonical forms,
as for example, in the cyclic decomposition theorem [6].
Corner sums do not just generalize diﬀerence quotients, they actually act very much like “a derivative”.
Indeed, consider a given polynomial form f (x) = a1 + a2x + · · · + anx
n−1 for which we deﬁne its right and
left evaluations by f (r)(x) = a1 + a2x + · · · + anx
n−1

and f (ℓ)(x) = a1 + xa2 + · · · + x
n−1an.

These lead to the left and right corner sums. Indeed, for M as above,

f (r)(M) = [ f (r)(x) Γ
(r)
f (x, c, y)
0 f (r)(y)
 ] , (6)

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4615

where the right and left corner sums are deﬁned by

Γ
(r)
f (x, c, y) =
 n∑

i=1 aiΓi(x, c, y) and Γ
(ℓ)
f (x, c, y) =
 n∑

i=1 Γi(x, c, y)ai. (7)

These clearly ensure that

Γxk (x, c, y) = Γk(x, c, y). (8)

Now if x = y, c = 1, and aix = xai then

f ([ x 1
0 x
 ]) = [ f (x) f ′(x)
0 f (x)
 ] ,

from which we see that Γ f (x, 1, x) = f ′(x).
Without assuming any commutivity we may state the following generalizations of the “diﬀerence
quotient”

xW f (x, y) − W f (x, y)y = f (ℓ)(x) − f (r)(y), (9)

which uses

xΓk(x, c, y) − Γk(x, c, y)y = x
kc − cy
k. (10)

Since the vector x commutes with the scalar x we see that xW f = xx
TH f y = x
T(xH f )y and so

f (ℓ)(x) − f (r)(y) = xW f − W f y = x
T(xH f − H f y)y.

Replacing x by A and y by B, we see that X = W f (A, B) is a solution to AX − XB = C f (A, B), provided ai
commutes with A.
We may go one step further and use two polynomials, extending the Bezoutian concept for two com-
muting variables
 f (x)1(y) − f (y)1(x)
x − y =
 n∑

i, j=1 bijx
i y j = xTBy.

Consider

f (ℓ)(x)1
(r)(y) − f (r)(x)1
(ℓ)(x) = f (ℓ)(x)[1(r)(y) − 1(ℓ)(x)] + [ f (ℓ)(x) − f (r)(y)]1(ℓ)(x)

= (xW f − W f y)1(ℓ)(x) − f (ℓ)(x)(xW1 − W1 y)

= xT[xH f − H f y]y1(ℓ)(x) − f (ℓ)(x)[xT(xH1 − H1 y)y].
 (11)

An important special case is when c = 1 = y. In this case the corner sum Γn(x, 1, 1) reduces to the
geometric progression (GP) (also called geometric sum)

Gn(x) = 1 + x + x2 + · · · + x
n−1. (12)

Needless to say, if just y = 1 then we obtain

Γk(x, c, 1) = Gk(x)c. (13)

When x, y and c commute then

Γk(x, c, y) = y
k−1Gk(x/y)c. (14)

This shows that each identity involving G(x) generates a corresponding identity for Γk(x, c, y) with commut-
ing variables, and conversely.

Applications of GPs are even more numerous, and can be found in:

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4616

(i) the study of nilpotent elements, including matrices;
(ii) the study of convergence, such as in the ratio test in Calculus;
(iii) in Euclid’s Division algorithm applied to special polynomials;
(iv) in powers and generalized inverses of the unit shifts 1 + ab and 1 + ba;
(v) in the “inversion” of the telescoping process;
(vi) in many iterative schemes, such as in the Picard iteration Xk+1 = Axk + B, with X0 = C. In fact, its
solution takes the form [11]

Xk = Gk(A)B + AkC. (15)

Likewise the Cesaro-Neumann iteration makes repeated use of telescoping identities [8].

2. More Properties of Corner sums

Let us next examine some of the basic properties of corner sums. When there is no risk of confusion, we
shall write Γk for Γk(x, c, y) .

Proposition 2.1. The corner sum Γk(x, c, y) has the following properties:

1. It is “self reciprocal” i.e.

Γk(x, c, y) = x
k−1Γk( 1
x , c, 1
y )y
k−1, (16)

2.
 Γk+1(x, c, y) = x
kc + Γk(x, c, y).y = xΓk(x, c, y) + cy
k, (17)

3. The “internal” addition law

Γk(x, c + d, y) = Γk(x, c, y) + Γk(x, d, y) (18)

and the “external” addition law

Γr+s(x, c, y) = x
rΓs(x, c, y) + Γr(x, c, y)y
s, (19)

hold, which for y = 1 = c the latter reduces to

Gr+s(x) = xrGs(x) + Gr(x) = x
sGr(x) + Gs(x). (20)

4. The homogeneity conditions are

Γk(x, xd, y) = xΓk(x, d, y) and Γk(x, dy, y) = Γk(x, d, y)y. (21)

Being self reciprocal implies that a geometric progression Gk(x) is also self reciprocal, i.e. xk−1Gk(1/x) =
Gk(x).
Setting y = 1 = c in (17) gives the fundamental telescoping identity

(1 − x)Gn(x) = 1 − x
n. (22)

As such, we may write Gn(x) = 1 − x
n
1 − x with the understanding that x , 1. We shall refer to x
n − 1 as the
“binomial of the GP”.
We also have

(1 − x2)Gn(x) = 1 + x − x
n − xn+1. (23)

We may use (20) to obtain Gn(x) = x
2Gn−2(x) + (1 + x), since n = (n − 2) + 2.
As an application of the homogeneity conditions, we consider the case where c = ax − xb. Then
Γk(a, c, b) = Γk(a, ax − xb, b) = aΓk(a, x, b) − Γk(a, x, b)b = a
kx − xbk.

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4617

Proposition 2.2. For polynomials f and 1 and M as in (5),

1. the external addition law is extended to

Γ
(t)
1h(x, c, y) = 1(t)(x)Γ
(t)
h (x, c, y) + Γ(t)
1 (x, c, y)h
(t)(y). (24)

where t is either ℓ or r (left or right), using the fact that (1h)(M) = 1(M)h(M).
2. the composition law

f (r)(1(r)(M)) = f (r) ([ 1(r)(x) Γ
(r)
1 (x, c, y)
0 1(r)(y)
 ])

= [ f (r)(1
(r)(x)) Γ(r)
f (1(r)(x), Γ
(r)
1 (x, c, y), 1(r)(y))
0 f (r)(1(r)(y))
 ]

holds.
A similar result holds for the left evaluations. Consequently

Γ f (r)◦1(r)(x, c, y) = Γ
(r)
f (1(r)(x), Γ(r)
1 (x, c, y), 1(r)(y)). (25)

Note that the composition law contains a corner sum within a corner sum!
Taking f (x) = x
r and 1(x) = x
s in the composition law, we arrive at the product rule:

Proposition 2.3 (Product rule).

Γrs(x, c, y) = Γr(xs, Γs(x, c, y), y
s) = Γs(x
r, Γr(x, c, y), y
r). (26)

The product rule may also be written as

Γrs(x, c, y) = Γr(x, Γs(xr, c, y
r), y) = Γs(x, Γr(x
s, c, y
s), y), (27)

which follows by directly computation.

For example, Γ10(x, c, y) = Γ5(x2, Γ2(x, c, y), y
2) = Γ2(x5, Γ5(x, c, y), y
5).
Related to these is the identity

Γr(xb, Γs(xa, c, y
a), y
b) = Γs(x
a, Γr(x
b, c, yb), ya), (28)

which is easily veriﬁed directly.
Combining the external addition law with the homogeneity condition, we also have

Γt(x
a, Γr+s(x, c, y), y
a) = Γt(x
a, x
rΓs(x, c, y) + Γr(x, c, y)ys, y
a)

which reduces to

Γt(x
a, Γr+s(x, c, y), y
a) = x
rΓt(xa, Γs(x, c, y), y
a) + Γt(xa, Γr(x, c, y), y
a)ys. (29)

For example,

Γp(x
r, Γr+s(x, c, y), y
r) = Γp+1(x
r, Γs(x, c, y), y
r) − Γs(x, c, y)ypr + Γp(x
r, Γr(x, c, y), y
r)y
s. (30)

In particular when p = r = 3 and s = 8 this reduces to

Γ3(x3, Γ11(x, c, y), y
3) = Γ4(x3, Γ8(x, c, y), y
3) − Γ8(x, c, y)y
9 + Γ9(x, c, y)y
8, (31)

in which Γ9(x, c, y)y8 − Γ8(x, c, y)y9 = x
8cy
8.
Using the homogeneity condition the product rule takes the form

Γrs(x, c, y) =
 s−1∑

i=0 (xr)
s−1−iΓr(x, c, y)(y
r)i. (32)

Now if n = mq + r with 0 ≤ r < m ≤ n, then we may combine the addition and multiplicative laws, (19)
and (27) to give the non-commutative “division algorithm” for corner sums:

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4618

Proposition 2.4. Given n = mq + r with 0 ≤ r < m ≤ n, then

Γr+mq(x, c, y) = x
rΓm(x, Γq(x
m, c, y
m), y) + Γr(x, c, y)y
mq. (33)

Setting y = 1 = c, gives the GP division algorithm

Gn(x) = xrGq(x
m)Gm(x) + Gr(x) = x
rGm(xq)Gq(x) + Gr(x). (34)

For n = mq,

Gmq(x) = Gm(x)Gq(x
m). (35)

For example, G2m = G2(x
m)Gm(x).

If x is nilpotent, say x
N = 0, then

xΓN(x, c, y) − ΓN(x, c, y)y = −cyN, (36)

which for y = 1 = c reduces to (1 − x)GN(x) = 1 and (1 − x)
−1 = GN(x). For n ≤ N we then arrive at

(1 − xn)−1 = Gk(x
n) = 1 + x
n + · · · + x
n(k−1), where k = ⌊N/n⌋ + 1. (37)

Moreover we have Gn(x) = (1 − x)−1(1 − x
n) and hence

Gn(x)−1 = (1 − x)(1 − x
n)
−1 = (1 − x)(1 + xn + · · · + xn(k−1)). (38)

Another application of the geometric sum can be found in the study of generalized inverses [13]. For
example

Lemma 2.5. For elements in an associative ring with unity,

1. If ba = 0 then (a + b)n = Γn+1(a, b).
2. If b
2 = b then Γn+1(a, b) = a
n + Gn(a)b.
3. If eb = 0 = be and e
2 = e then (b + e)n = bn + e.
Of particular interest is the case b = a
2a−, e = aa−, where a is a (von Neumann) invertible element and a−

denotes an inner inverse of a (i.e. aa
−a = a).

A GP can also be obtained from its binomial, using the idea of a Drazin inverse. Indeed ([9]) if A is a
matrix with minimal polynomial ψA(λ) = (λ − 1)s f (λ) such that 1cd(λ − 1, f ) = 1, then

Gn(A) =
 n−1∑

i=0 Ai = (I − A)
D(I − An) +
 s−1∑

i=0
 ( n
i + 1

)(A − I)iZ
0
i , (39)

where the Z
0
i are the principal idempotents of A.
The Cesaro sum is deﬁned as Cn(A) = Gn(A)/n and is used in iteration, Probability Theory, Markov
Chains and Non-Negative matrices.
It can be shown that PANQ −→ 0 as N → ∞ iﬀ PGN(A)Q converges as N → ∞ ([11]) where P and Q are
invertible matrices.

3. Polynomials

Much of polynomial theory deals with the Division Algorithm and in particular with Euclid’s Algo-
rithm. In the special case of a linear divisor, we recall the Bezout Theorem, which heavily depends on
the telescoping trick. Indeed, much of matrix theory uses the divisor λI − A, leading up to the study of
annihilating polynomials, adjoints and elementary divisors. All use telescoping repeatedly.

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4619

To study polynomials in one variable we often have to study polynomials in two variables. The catch
however, is that for polynomials in two (possibly non-commuting) variables, there is no unique division
algorithm (but we can use Groebner bases) and the set of such polynomials is not a PID and there is no gcd!
We shall now show that Euclid’s construction for the gcd of two integers, induces parallel gcd algorithms
for binomials and Geometric sums as well as “gcd-like” construction for the gcd of two corner sums in
non-commuting variables x and y.
For a given m and n, say n = mq + r, with 0 ≤ r < m ≤ n, Euclid’s Algorithm gives a sequence of
integer quotients and remainders (qi, ri). We shall now show that for three special classes of polynomials,
the sequences (qi, ri), will induce the corresponding quotient and remainder sequences (Qi, Ri), and we give
explicit expressions for them.
These sequences are of the form

(i) x
k − 1 (binomial)
(ii) Gk(x) (geometric progression)
(iii) Γk(x, c, y) (corner sums).

The story of Euclid’s algorithm is really one of ﬁnding the generator for the principal ideal generated
by the starting elements.
Indeed,

(i) for integers if rN+1 = 1cd(r0, r1) then rN+1R = r0R + r1R, where R is the ring of integers Z.
(ii) for binomials, if xrN+1 − 1 = 1cd(x
r0 − 1, xr1 − 1) then (x
rN+1 − 1)R = (x
r0 − 1)R + (xr1 − 1)R where R = Z[x].
(iii) For geometric sums, if GrN+1 (x) = 1cd(Gr0 (x), Gr1 (x)) then GrN+1 (x)R = Gr0 (x)R+Gr1 (x))R, where R = Z[x].
We shall also solve the recurrence relation used in Euclid’s algorithm and use it to give explicit
formula, in the ﬁrst two cases, for the coeﬃcients of the generator equation of the principle ideal.
(iv) For corner sums, when x and y do not commute, the ideal has to be replaced by the bi-module
generated by Γr0 and Γr0 , which we address shortly.

3.1. Finding the gcd

We now show that there is a precise parallel between Euclid’s Algorithm for two integers m and n, and
the algorithm for the corresponding binomials x
m − 1 and x
n − 1.
We recall (34) and start by multiplying (34) by x − 1, to obtain the following pivotal binomial identity,
valid over any ring R with 1.

x
n − 1 = x
r(xmq − 1) + (x
r − 1) = (x
m − 1)x
r[xm(q−1) + x
m(q−2) + ... + 1] + (x
r − 1) (40)

or more compactly

n = mq + r ⇔ (x
n − 1) = (x
m − 1)Q(x) + (x
r − 1) , (41)

where Q(x) = xr[xm(q−1) + x
m(q−2) + ... + 1] = xrGq(x
m).
This show that the geometric sum does indeed enter naturally into the division algorithm!
An immediate consequence is that

m | n iﬀ (x
m − 1) | (x
n − 1) iﬀ Gm(x)|Gn(x). (42)

This ﬁrst part of this chain is used with x = 2 in the construction of Mersenne primes and the construction
of Fermat and Miller pseudo primes as used in cryptography [14].
Alternatively we could use the fact that a|b iﬀ a|(b − a).
For the corner sum, the fact that m|n will result in a compact functional equation.
A second by-product is the following result:

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4620

Theorem 3.1. Over a Euclidean domain,

gcd(x
m − 1, x
n − 1) = x
gcd(m,n) − 1 = (x − 1) · gcd[Gm(x), Gn(x)]. (43)

Proof. We may use this “parallel division” to obtain three parallel Euclid-chains starting with r0 = n and
r1 = m or with xr0 − 1 and xr1 − 1 or with Gr0 and Gr1 .

r0 = r1q1 + r2 x
r0 − 1 = (xr1 − 1)Q1 + (x
r2 − 1) Gr0 (x) = Gr1 (x)Q1 + Gr2 (x)
r1 = r2q2 + r3
... ... ...
ri−1 = riqi + ri+1 x
ri−1 − 1 = (x
ri − 1)Qi + (x
ri+1 − 1) Gri−1 (x) = Gri(x)Qi + Gri+1 (x)
... ... ...
rN−1 = rNqN + rN+1 x
rN−1 − 1 = (x
rN − 1)QN + (x
rN+1 − 1) GrN−1 (x) = GrN (x)Qi + GrN+1 (x)
rN = rN+1qN+1 + 0 x
rN − 1 = (x
rN+1 − 1)QN+1 + 0(x) GrN (x) = GrN+1(x)QN+1 + 0(x)
 .

Note that rN+2 = 0.
Since Qi = x
ri+1 Gqi(xri) we see how the geometric sums are related via

Gri−1 (x) = x
ri+1 Gri(x) · Gqi(x
ri) + Gri+1 (x) = x
ri+1 Gqiri(x) + Gri+1 (x). (44)

At the last stage, when rN = rN+1qN+1, this gives

GrN (x) = x
0 · GrN+1 (x) · GqN+1 (x
rN+1),

which checks (35).

The result corresponding to (43) is false for lcms , i.e. lcm(x
m − 1, x
n − 1) , xlcm(m,n) − 1, as seen from
the case n = 3 and m = 2. Since gcd(m, n) = 1, we know that gcd((x2 − 1), (x3 − 1)) = x − 1 and hence
lcm[(x
2 − 1), (x3 − 1)] = (x2 − 1)(x3 − 1)/(x − 1) = (x + 1)(x
3 − 1). This clearly divides (x
6 − 1) but will not equal
it. The quotient equals x2 − x + 1.
If we set ri = uir0 + vir1, i = 0, . . . , k + 1, then the ui and vi satisfy the same recurrence as the ri, i.e.
ri+1 = ri−1 − qiri, except with diﬀerent initial conditions. Indeed

ui+1 = ui−1 − qiui, u0 = 1, u1 = 0

and vi+1 = vi−1 − qivi, v0 = 0, v1 = 1

We may do exactly the same for the polynomials xri − 1 and Gri−1 (x) with recurrences

x
ri+1 − 1 = (xri−1 − 1) − Qi(x)(xri − 1) and Gri+1 (x) = Gri−1 − Qi · Gri(x)

to give

x
ri − 1 = Ui(x)[x
r0 − 1] + Vi(x)[x
r1 − 1] and Gri = Ui(x)Gr0 + Vi(x)Gr1 (45)

The Ui(x) and Vi(x) satisfy

Ui+1(x) = Ui−1(x) − Qi(x)Ui(x), U0(x) = 1, U1(x) = 0

and Vi+1(x) = Vi−1(x) − Qi(x)Vi(x), V0(x) = 0, V1(x) = 1.

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4621

At the ﬁnal stage, where i = N + 1, we arrive at the “ideal equation”

rN+1 = gcd(ro, r1) = uN+1r0 + vN+1r1,
xrN+1 − 1 = gcd[x
r0 − 1, x
r1 − 1] = UN+1(x)(x
r0 − 1) + VN+1(x)(x
r1 − 1)
GrN+1 (x) = gcd[Gr0 (x), Gr1 (x)] = UN+1(x)Gr0 (x) + VN+1(x)Gr1 (x).

The corresponding result for corner sums is more complicated, and the expression for the coeﬃcients
will be given in the section on Sandwich Recurrence Relations.

Consequently, recalling that r0 = n and r1 = m, we see that

(m, n) = 1 = (r0, r1) ⇔ rN+1 = 1 ⇔ (x − 1) = gcd[x
r0 − 1, x
r1 − 1] ⇔ 1 = gcd[Gr0 (x), Gr1 (x)] (46)

In which case 1 = uN+1n + vN+1m as well as

x − 1 = UN+1(x)(x
n − 1) + VN+1(x)(x
m − 1) and 1 = UN+1(x)Gn(x) + VN+1(x)Gm(x). (47)

For convenience we shall write U(x) for UN+1 and V(x) for VN+1.
Note that in the above we had assumed that n ≥ m. If the opposite holds, then we have to interchange
U and V.
We shall next see that there is a parallel algorithm for corner sums.

4. The Corner Recurrence

Recall by the addition law and the product rule, that

Γr+mq(x, c, y) = x
r Γm(x, Γq(x
m, c, y
m), y) + Γr(x, c, y)ym. (48)

Parallel to the sequences (rk), (x
rk − 1) and (Grk ) we may construct the corresponding sequence of corner
sums as

Γr0 (x, c, y) = x
r2 Γr1 (x, Γq1 (xr1 , c, yr1 ), y) + Γr2 (x, c, y)y
r1q1 (49)

Γr1 (x, c, y) = x
r3 Γr2 (x, Γq2 (xr2 , c, yr2 ), y) + Γr3 (x, c, y)yr2q2 (50)

Γr2 (x, c, y) = x
r4 Γr3 (x, Γq3 (xr3 , c, yr3 ), y) + Γr4(x, c, y)yr3q3 (51)
... (52)

Γrk−1 (x, c, y) = x
rk+1 Γrk (x, Γqk (x
rk , c, y
rk ), y) + Γrk+1 (x, c, y)y
rkqk . (53)

At the ﬁnal stage, when k = N + 1 and rN+2 = 0, we have

ΓrN (x, c, y) = ΓrN+1(x, ΓqN+1 (x
rN+1 , c, y
rN+1 ), y). (54)

The process of “back-substituting” the Γri to obtain ΓrN+1 as an “expression” in terms of the initial values
Γr0 and Γr1 , can be done by hand for small cases. For larger cases it is best done by setting up a “diﬀerence
equation” that is satisﬁed by a “weighted version” of the Γis. This we now pursue.
Let us ﬁrst recall (32), and introduce the following abbreviation:
xrk −→ xk, y
rk −→ yk, Γrk (x, c, y) −→ Γk and deﬁne the product Pk = yqk
k · · · y
q1
1 = y
qkrk+···+q1r1. We also set
P0 = 1 = P−1.
We may rewrite the above steps as

Γ0 = x2
 q1−1∑

i=0 (x1)q1−1−iΓ1 y
i
1 + Γ2yq1
1 . (55)

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4622

Γ1 = x3
 q2−1∑

i=0 (x2)q2−1−iΓ2yi
2 + Γ3y
q2
2 (56)

and generally

Γk−1 = xk+1
 qk−1∑

i=0 (xk)
qk−1−iΓk y
i
k + Γk+1yqk
k . (57)

If we now deﬁne Fk = ΓkPk−1 and multiply through on the right by Pk−1, then we arrive at

Γk−1Pk−1 = xk+1
 qk−1∑

i=0 (xk)
qk−1−i(ΓkPk−1)y
i
k + Γk+1(yk)qk Pk−1. (58)

This gives the recurrence

Fk+1 = −xk+1
 qk−1∑

i=0 (xk)
qk−1−iFk y
i
k + Fk−1(y
qk−1
k−1 ) (59)

We thus have a “sandwich” recurrence relation of the form

wk+1 =
 qk−1∑

i=0 a
(k)
i wkα(k)
i + wk−1βk.

where a
(k)
i = x
rk+1+rk(qk−1−i) , α(k)
i = yrki and βk = y
qk−1
k−1 . It is clear that the latter two commute. We shall for
convenience drop the brackets in the exponents.
The initial conditions are w0 = F0 = Γ0(x, c, y) = Γr0 and w1 = Γ1 = Γr1 (x, c, y).
This recurrence is a special case of the more general two-sided sandwich recurrence

wk+1 =
 qk−1∑

i=0 ak
i wkαk
i +
 pk−1∑

i=0 bk
i wk−1βk
i , w0 = λ, w1 = µ, (60)

where the coeﬃcients are not constant and do not (necessarily) commute. On account of the linearity, this
may be split as wk = Xk + Yk, where (Xk) and (Yk) satisfy the same recurrence but with initial conditions
X0 = λ, X1 = 0 and Y0 = 0, Y1 = µ respectively.
We next address the solution process.

5. The Matrix Recurrence

We start by writing the sandwich recurrence relation (60) in matrix from as

wk+1 = Akwkαk + Bkwk−1βk, with w0 = λ, w1 = µ, (61)

where Ak = [a
k
0, .., a
k
qk−1], Bk = [bk
0, .., bk
qk−1] and αk =
 

 αk
0
...
αk
qk−1
 

, βk =
 

 βk
0
...
βk
qk−1
 
.

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4623

Likewise we consider the associated recurrences

Xk+1 = AkXkαk + BkXk−1βk, with X0 = λ, X1 = 0, (62)

and
 Yk+1 = AkYkαk + BkYk−1βk, with Y0 = 0, Y1 = µ. (63)

Following Euclid, we back substitute at each step and write

wk = Ukw0U′
k + Vkw1V′
k, (64)

where the matrix coeﬃcients satisfy the following row/columns recurrence relations

Uk+1 = [AkUk, BkUk−1] (as rows) U0 = 1, U1 = 0 (65)

and
 U′
k+1 = [ U′
kαk
U′
k−1βk
 ] (as columns) U′
0 = 1, U′
1 = 0 (66)

with similar recurrences for Vk and V′
k and associated initial conditions V0 = V′
0 = 0, V1 = V′
1 = 1.
Comparing the two settings we see that

Xk = UkλU′
k, Yk = VkµV′
k, with X0 = λ, X1 = 0, Y0 = 0, Y1 = µ. (67)

Let us now generate the ﬁrst few terms of these recurrences.

w2 = A1µα1 + B1λβ1

w3 = (A2A1)µ(α1α2) + A2(B1λβ1)α2 + B2µβ2 = [A2A1, B2]µ [ α1α2
β2
 ] + (A2B1)λ(β1α2)

From this, or from the recurrence, we see that

V2 = [A1, 0], V′
2 = [ α1
0
 ] , U2 = [0, B1], U′
2 = [ 0
β1
 ]

as well as
 V3 = [A2A1, B2], V′
3 = [ α1α2
β2
 ]

and
 U3 = [0, A2B1, 0], U′
3 =
 

 0
β1α2
0
 
 .

Likewise
 V4 = [A3A2A1, A3B2, B3A1, 0] and V′
4 =
 

 α1α2α3
β2α3
α1β3
0
 


in addition to
 U4 = [0, A3A2B1, 0, 0, B3B1] and U′
4 =
 

 0
β1α2α3
0
0
β1β3
 

 .

We now make two important observations:

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4624

(1) It suﬃces to only compute the left-hand coeﬃcients Vk and Uk, because the right-hand coeﬃcients
follow immediately by symmetry (with entries in reversed order).
(ii) The Vk rows have a much simpler pattern than the Uk, with a last entry that vanishes.

(iii) If we set all α1 = 1 = βi, then V′
k = [ e
0
 ] and since we multiply VkµV′
k we obtain the terms in the

left-handed recurrence vk+1 = Akvk + Bkvk−1, by adding the terms in the row Vk! (the zero term drops
out!) Indeed, v2 = a1, v3 = a2a1 + b2, and v4 = a3a2a1 + a3b2 + b3a1 etc.

Needless to say we may reverse this argument, and use the one-sided (say left) recurrence to generate
the vectors Vk, and V′
k for the sandwich recurrence.
Before we shall do this let us ﬁrst digress and complete the gcd story.

5.1. The gcd for corner sums

The “gcd story” for corner sums is more complicated because of the non-commutativity of the variables.
The “ideal” structure that is associated with the gcd concept in the ﬁrst three cases, (those of the integer,
binomial and geometric sum cases) has to be replaced by the corresponding bi-module structure.
Trying to express the terminal “gcd” ΓrN+1 (x, c, y) in terms of the initial corner sums Γr0 and Γr1 amounts
to “solving” the sandwich recurrence (59). We need both the product rule (26) as well as the actual solution
form (64).
We begin by deﬁning the proper setting.
Given two rings R and S, with common elements a and b. The bi-module generated by a and b, relative
to R, S is deﬁned and denoted by

Deﬁnition 5.1. M(a, b) = ⟨a, b⟩R,S = ∑K
i=1 riasi + ∑N
j=1 ρjbσj, for all K, N = 1, 2, . . . , and all ri, ρj ∈ R and all
si, σj ∈ S.

It is clear that
(i) M(a, b) + M(a, b) ⊆ M(a, b) (ii) RM(a, b) ⊆ M(a, b) and (iii) M(a, b)S ⊆ S.

These show that M(a, b) is a “two-sided” bi-module, which generalizes the ideal concept. We shall call
M(a, b) the bi-module generated by a and b – relative to the rings R and S.

We shall refer to M(a, b) a principal bi-module, if there exists a generator d ∈ R ∩ S, such that M(a, b) = M(d).
In other words,

x ∈ M(a, b) iﬀ x =
 L∑

i=1 πidλi, (68)

for some πi ∈ R and λi ∈ S. In particular this means that

d =
 K∑

i=1 riasi +
 N∑

j=1 r
′
jbs
′
j, (69)

for some K and N, and ri, r
′
j ∈ R and si, s′
j ∈ S, as well as

a =
 T∑

i=1 πidλi and b =
 L∑

i=1 π
′
i dλ′
i , (70)

for some T and L and πi, π
′
i ∈ R and λi, λ
′
i ∈ S.
In order to complete the gcd parallel, we deﬁne “division” in the bi-module as

Deﬁnition 5.2. x|a if a = ∑K
i=1 rixsi, for some K and ri ∈ R and si ∈ S.

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4625

It follows immediately from (68) and (70) that d generates M(a, b) iﬀ d|a, d|b and x|a, x|b implies x|d.
The division deﬁned above will be a partial order provided a = ∑K
i=1 riasi forces all ri = 1 = si. This will
be the case for corner sums with integer polynomial rings R = Z[x] and S = Z[y].
For the terminal corner sum, the solution

ΓrN+1 = UrN+1 Γr0 U′
rN+1 + VrN+1 Γr1 V′
rN+1 (71)

shows that ΓrN+1 ∈ ⟨Γr0 , Γr1 ⟩Z[x],Z[x], while the product rule and the fact that rN+1|r0 and rN+1|r1 ensure that

Γr0 ∈ ⟨ΓrN+1 ⟩, Γr1 ∈ ⟨ΓrN+1 ⟩.

As such we see that ΓrN+1 indeed generates the bi-module M(Γr0 , Γr1 ).

6. The NC2 Case

We next focus on the NON-commutative, NON-constant (i.e. NC2) (left-handed) linear Recurrence
Relation

wk+1 = akwk + bkwk−1, w0 = λ, w1 = µ. (72)

where ak and bk need NOT commute.

It is clear that the special case where all bi = 1, reduces to Euclid’s integer recurrence relation.

The solution may of course be expressed in terms of companion matrices. In fact if we let wi = [ wi+1
wi
 ] , w0 =
[ µ
λ
 ] and set Li = [ ai bi
1 0
 ]
. Then

wi = Liwi−1 = (LiLi−1..L1)w0, (73)

however this tells us nothing about the representation of the wk.

For example, [ w4
w3
 ] = [ a3 b3
1 0
 ] [ a2 b2
1 0
 ] [ a1 b1
1 0
 ] [ µ
λ
 ]
.

The use of companion matrices was also presented in [12].

We begin with the special case where v0 = 0, v1 = 1. The general solution to the case where v0 = 0, v1 = µ
is obtained by post multiplication of µ.

When v0 = 0, v1 = 1 then the ﬁrst few links are

v2 = a1, v3 = a2a1 + b2,
v4 = a3a2a1 + a3b2 + b3a1,
v5 = a4a3a2a1 + a4a3b2 + a4b3a1 + b4a2a1 + b4b2
v6 = a5a4a3a2a1 + a5a4a3b2 + a5a4b3a1 + a5b4a2a1 + a5b4b2 + b5a3a2a1 + b5a3b2 + b5b3a1,
v7 = a6a5a4a3a2a1 + (a6a5a4a3b2 + a6a5a4b3a1 + a6a5b4a2a1 + a6b5a3a2a1 + b6a4a3a2a1) +
(a6a5b4b2 + a6b5a3b2 + a6b5b3a1 + b6a4a3b2 + b6a4b3a1 + b6b4a2a1) + b6b4b2.

To keep track of the pattern, the solutions can best be expressed in terms of blocks!

Consider vk+1 and observe the following facts about its words (i.e. terms or products):

1. the starting subscript is k;

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4626

2. the subscripts decrease from left to right;
3. each word contains at most two types of letters, ai and bj;
4. after an ai the subscript goes down by ONE; after a bj it goes down by TWO;
5. the word length L ranges from 1 to k;
6. if t is the number of bj, then t + L = k and t ≤ L; hence t ≤ ⌊ k
2 ⌋;

7. the words come in blocks Et(ℓ) of length L = k − t, and cardinality (L
r)
;

8. we have to allocate t slots for the bi out of L slots in (L
t) ways.

For notational convenience we replace ar by r and bs by s and have

vk+1 =
 ⌊ k
2 ⌋∑

t=0 Et(k − t). (74)

A block of words is written in matrix form, and by the “addition” of these arrays we mean the addition
of each of its rows to the total.
The solution for the IC v0 = 0 and v1 = µ is obtained by post multiplying by µ the solution when v0 = 0
and v1 = 1.
Examples.

(i) k = 1. v2 = E0(1) = [1] = a1.
(ii) k = 2. v3 = E0(2) + E1(1) = [2, 1] + 2 = a2a1 + b2.

(iii) k = 3. v4 = E0(3) + E1(2) = [3, 2, 1] + [ 3 2
3 1
 ] = a3a2a1 + (a3b2 + b3a1).

(iv) k = 4. v5 = E0(4) + E1(3) + E2(2) = a4a3a2a1 + (a4a3b2 + a4b3a1 + b4a2a1) + b4b2, i.e. v5 = [4, 3, 2, 1] +

 4 3 2
4 3 1
4 2 1
 
 + [4, 2].

(v) k = 5. v6 = E0(5) + E1(4) + E2(3) = a5a4a3a2a1 + (a5a4a3b2 + a5a4b3a1 + a5b4a2a1 + b5a3a2a1) + (a5b4b2 +
b5a3b2 + b5b3a1)
(vi) k = 6. ⌊ k
2 ⌋ = 3 and v7 = E0(6) + E1(5) + E2(4) + E3(3) in which

E0(6) = [6, 5, 4, 3, 2, 1], E1(5) =
 

 6 5 4 3 2
6 5 4 3 1
6 5 4 2 1
6 5 3 2 1
6 4 3 2 1
 

 , E2(4) =
 

 6 5 4 2
6 5 3 2
6 5 3 1
6 4 3 2
6 4 3 1
6 4 2 1
 

 ,

and E3(3) = [6, 4, 2]. The cardinality of v7 is #(v7) = (6
0) + (5
1) + (4
2) + (3
3) = 1 + 5 + 6 + 1 = 13 elements.

(vii) k = 7. ⌊ k
2 ⌋ = 3. v8 = E0(7) + E1(6) + E2(5) + E3(4) in which

E0(7) = [7, 6, 5, 4, 3, 2, 1], E1(6) =
 

 7 6 5 4 3 2
7 6 5 4 3 1
7 6 5 4 2 1
7 6 5 3 2 1
7 6 4 3 2 1
7 5 4 3 2 1
 


,

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4627

E2(5) =
 

 7 6 5 4 2
7 6 5 3 2
7 6 5 3 1
7 6 4 3 2
7 6 4 3 1
7 6 4 2 1
7 5 4 3 2
7 5 4 3 1
7 5 4 2 1
7 5 3 2 1
 

 and E3(4) =
 

 7 6 4 2
7 5 4 2
7 5 3 2
7 5 3 1
 
.

Thus #(v8) = (7
0) + (6
1
) + (5
2) + (4
3) = 1 + 6 + 10 + 4 = 21.

The proof follows by induction and the fact that

akEt(k − t − 1) + bkEt−1(k − t − 1)) = Et(k − t), t = 0, 1, . . . , [k/2]. (75)

The latter follows from the fact that each term (i.e. row) from akEt(k − t − 1) as well as each row from
bkEt−1(k − t − 1) is contained in the set of rows from Et(k − t). Moreover both sides have the same cardinality,
because of the identity
(k
t
) + ( k
t − 1

) = (k + 1
t
 ). (76)

As such we must have equality. Right multiplication by µ gives the solutions for the case where v0 = 0, v1 =
µ.

Recalling (74) we may write

vk+1 = ∑

ω∈E0(k) ω + ∑

ω∈E1(k−1) ω + ∑

ω∈E2(k−2) ω + · · · (77)

where ω is a “word” appearing in the sum, and can at the same time obtain the sandwich solution

Vk+1 = ∑

ω∈E0(k) ωµωop + ∑

ω∈E1(k−1) ωµωop + ∑

ω∈E2(k−2) ωµω
op + · · · , (78)

where ωop is the reversed word associated with ω. Needless to say, this has the same number of terms as
the one-sided solution vk.

Let us next examine the ﬁrst few terms of the sequence (uk). The links are :
u2 = b1, u3 = a2b1, u4 = (a3a2 + b3)b1 ,
u5 = (a4a3a2 + a4b3 + b4a2)b1,
u6 = [a5a4a3a2 + (a5a4b3 + a5b4a2 + b5a3a2) + b5b3]b1, etc.

The ui may be obtained from the vi as follows.

1. In each term in vk+1 i.e. in each row of Et(k − t) for t = 0, 1, . . . , ⌊ k
2 ⌋, replace ai by ai+1 and bj by bj+1.
That is, we replace Et(k − t) by Ct(k − t) for t = 0, 1, . . . , l f loor k
2 ⌋.
2. Multiply each row in Ct(k − 1) on the right by b1 giving Dt+1(k + 1 − t).
3. This gives uk+2.
We note that the blocks Ct(k − t) are sub-matrices of Bt(k + 1 − t).

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4628

The validity of this construction can be seen from the companion matrix product expression as given in
(73). Indeed, recall that
[ uk+2
uk+1
 ] = (Lk+1Lk−1..L1) [ 0
1
 ] and [ vk+1
vk
 ] = (LkLk−1..L1) [ 1
0
 ]

and observe that L2
 [ 1
0
 ] b1 = L2
 [ b1
0
 ] = L2L1
 [ 1
0
 ] .

Alternatively, we can construct the uk from vk as follows:
(i) drop all words (i.e. rows) not ending in 1.
(ii) replace 1 by 1.
This gives uk.
This may also be seen from the companion product representation.

Examples.

1. v3 = [2, 1] + 2 −→ [3, 2] + 3 −→ [3, 2, 1] + [3, 1] = a3a2b1 + b3b1 = u4.

2. v4 = [3, 2, 1] + [ 3 2
3 1
 ] → [4, 3, 2] + [ 4 3
4 2
 ] → [4, 3, 2, 1] + [ 4 3 1
4 2 1
 ] = D1(4) + D2(3) = (a4a3a2 +

a4b3 + b4a2)b1 = u5.
3. v7 = E0(6) + E1(5) + E2(4) + E3(3) →

[7, 6, 5, 4, 3, 2] +
 

 7 6 5 4 3
7 6 5 4 2
7 6 5 3 2
7 6 4 3 2
7 5 4 3 2
 

 +
 

 7 6 5 3
7 6 4 3
7 6 4 2
7 5 4 3
7 5 4 2
7 5 3 2
 

 + [7, 5, 3] = C0(6) + C1(5) + C2(4) + C3(3).

We next add in the terms b1 to give

D2(6) + D3(5) + D4(4) = [7, 6, 5, 4, 3, 2, 1] +
 

 7 6 5 4 3 1
7 6 5 4 2 1
7 6 5 3 2 1
7 6 4 3 2 1
7 5 4 3 2 1
 

 +
 

 7 6 5 3 1
7 6 4 3 1
7 6 4 2 1
7 5 4 3 1
7 5 4 2 1
7 5 3 2 1
 

 + [7, 5, 3, 1] =

a7a6a5a4a3a2b1 + (a7a6a5a4b3b1 + a7a6a5b4a2b1 + a7a6b5a3a2b1 + a7b6a4a3a2b1 + b7a5a4a3a2b1) + (a7a6b5b3b1 +
a7b6a4b3b1 + a7b6b4a2b1 + b7a5a4b3b1 + b7a5b4a2b1 + b7b5a3a2b1) + b7b5b3b1 = u8.
4. Using the alternative method we may construct u6 as follows.

v6 = [5, 4, 3, 2, 1] +
 

 5 4 3 2
5 4 3 1
5 4 2 1
5 3 2 1
 
 +
 

 5 4 2
5 3 2
5 3 1
 
.

We keep [5, 4, 3, 2, 1] +
 

 5 4 3 1
5 4 2 1
5 3 2 1
 
 + [5, 3, 1] and replace 1 by 1 to give

[5, 4, 3, 2, 1] +
 

 5 4 3 1
5 4 2 1
5 3 2 1
 
 + [5, 3, 1] = u6

In general we have

uk+1 = D1(k) + D2(k − 1) + D3(k − 2) + · · · (79)

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4629

Remarks
(i) An alternative approach using matrix products and continued fractions was given in [1].
(ii) It is not clear how the “master solution”, as used in [2], and [5], comes into play in the non-constant
case.

Right multiplication by λ gives the solution when u0 = λ and u1 = 0.

Example n = 5 and m = 3.

Clearly 5 = 3 · 1 + 2 and 3 = 2 · 1 + 1, so that r0 = 5, r1 = 3, r2 = 2, r3 = 1 and q1 = 1, q2 = 1. Thus N = 2 and
r3 = U3r0 + V3r1.
Now recall that V3 = E1(3) = [2, 1] + 2 = a2a1 + b2 in which ai = −qi and b1 = 1. So we get V3 = Q2Q1 + 1.
Also V2 = [1] so that U3 = [2, 1] = a2b1 = −Q2. But we know that Qi = x
ri+1 Gqi(xri) and G1(.) = 1, so that we
obtain
U3 = −Q2 = −x
r3 Gq2 (xr2 ) = −xG1(x2) = −x and
V3 = 1 + Q1Q2 = 1 + [x
r2 Gq1(x
r1 ][x
r3 Gq2 (xr2 ] = 1 + x2G1(.)xG1(.) = 1 + x3.
This gives the ideal equation

−x(x
5 − 1) + (1 + x
3)(x3 − 1) = x − 1 . (80)

We may use the same sequence of remainders (ri), to obtain the corner sum iterates:

Γ5(x, c, y) = x
2Γ3(x, Γ1(x
3, c, y3), y) + Γ2(x, c, y)
Γ3(x, c, y) = xΓ2(x, (Γ1(x2, c, y
2) + Γ1(x, c, y)y3

Γ2(x, c, y) = x0Γ1(x, Γ(x, c, y), y).

Since Γ1 = c, and writing Γi for Γi(x, c, y) we arrive at

Γ1y
5 = x
3Γ3 + Γ3 y
3 − xΓ5. (81)

Example n = 58 and m = 22.

This time 58 = 2 · 22 + 14, 22 = 1 · 14 + 8, 14 = 1 · 8 + 6, 8 = 1 · 6 + 2 and 6 = 3 · 2 + 0. Thus r0 = 58, r1 =
22, r2 = 14, r3 = 8, r4 = 6, r5 = 2 and q1 = 2, q2 = 1, q3 = 1, q4 = 1. The terminal parameter is N = 4 and
R5 = U5r0 + V5r1.

Next we recall that v5 = E0(4) + E1(3) + E2(2) = [4, 3, 2, 1] + ([4, 3, 2] + [4, 3, 1] + [4, 2, 1]) + [4, 2] = a4a3a2a1 +
(a4a3b2 + a4b3a1 + b4a2a1) + b4b2 = Q4Q3Q2Q1 + Q4Q3 + Q4Q1 + Q2Q1 + 1.
On the other hand, because v4 = [3, 2, 1] + [3, 2] + [3, 1] we see that u5 = [4, 3, 2, 1] + [4, 3, 1] + [4, 2, 1] =
−Q4Q3Q2 − Q4 − Q2.
Lastly, we compute Q1 = x
14G2(x
22) = x14(1 + x22) and Q2 = x
8G1(?) = x8 as well as Q3 = x
6 and Q4 = x
2. We
then get
U5 = −(x
2x6x
8 + x
2 + x
8) = −(x
16 + x
8 + x
2) and
V5 = x
30(1 + x22) + x
2x6 + x2x
‘14(1 + x22) + x
22(1 + x
22) + 1 = x52 + x44 + x38 + x30 + x22 + x16 + x8 + 1.

The ideal equation becomes

−(x16 + x8 + x
2)(x
58 − 1) + (x
52 + x
44 + x
38 + x
30 + x
22 + x
16 + x
8 + 1)(x
22 − 1) = x
2 − 1 . (82)

It goes without saying that we may divide by x − 1 and obtain the corresponding ideal equation for
geometric sums

−(x
16 + x
8 + x
2)G58(x) + (x
52 + x
44 + x
38 + x
30 + x
22 + x
16 + x
8 + 1)G22(x) = G2(x)

Remark
As an example of the solution to the sandwich recurrence we return to the corner sums.

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4630

7. Sandwiched Corner Sums

As a special application let us examine the sandwich recurrence for the corner sums:

Fk+1 = AkFkαk + BkFk−1βk, (83)

where Ak = −xk+1[x
qk−1
k , ..., xk, 1] = −x
rk+1 [(x
rk )
qk−1..., xrk , 1]

αk =
 

 1
yk
...
y
qk−1
k
 

 =
 

 1
yrk
...
y
rk(qk−1)
 

 and βk = yqk−1
k−1 = yrk(qk−1).

To illustrate the solution process we examine the case where r0 = 11 and r1 = 8.
We shall obtain the desired expansion for the “terminal” gcd corner sum ΓrN+1 by solving the sandwich
recurrence and contrast it with the solution that is obtained by “back substitution”. To follow Euclid, we
shall do the latter ﬁrst.

Let r0 = 11 and r1 = 8. Following Euclid we have r0 = 11 = 1 · 8 + 2, r1 = 8 = 2 · 3 + 2, r2 = 3 = 1 · 2 + 1,
r3 = 2 = 2 · 1 + 0, r4 = 1, r5 = 0. Also, q1 = 1, q2 = 2, q3 = 1, q4 = 2.

Since N + 1 = 4, we shall need three steps of the iteration which are as follows:

(i) Γ3 · y8 = Γ11 − x3Γ8
(ii) Γ2 · y
6 = Γ8 − x
2Γ3(x, 1C2(x
3, c, y
3), y)
(iii) Γ1 · y
2 = Γ3 − xΓ2.

To perform the back substitution we multiply the latter equation by y6 giving Γ1 · y
8 = (Γ3 · y
6) − x(Γ2 · y
6).
Substituting from (ii) we get Γ1 · y
8 = (Γ3 · y6) − x[Γ8 − x
2Γ3(x, Γ2(x
3, c, y3), y)] and hence

Γ1 · y8 = (Γ3.y
6) − xΓ8 + x
3Γ3(x, Γ2(x3, c, y
3), y)].

We next multiply this by y8 and use (i), to give

Γ1 · y
16 = (Γ3 · y
8)y6 − xΓ8 · y8 + x
3Γ3(x, Γ2(x
3, c, y3), y)y8.

Substituting from (i) we arrive at:

Γ1 · y16 = (Γ11 − x
3Γ8)y
6 − xΓ8 · y
8 + x3[Γ11(x, Γ2(x
3, c, y3), y) − x
3Γ8(x, Γ2(xx, c, y
3), y)].

And hence we get

cy16 = [Γ11 · y
6 + x
3[Γ11(x, Γ2(x3, c, y
3), y)] − [x
3Γ8 · y
6 + xΓ8 · y
8 + x
6Γ8(x, Γ2(x3, c, y
3), y)], (84)

which may be checked by direct computation. We next have to express this just in terms of Γ11 and Γ8.
Recall that Γ11(x, Γ2(x
3, c, y
3), y) = Γ2(x3, Γ11, y
3) and that Γ8(x, Γ2(x
3, c, y3), y)] = Γ2(x
3, Γ8, y
3)] = Γ11. This
shows that

cy16 = Γ11 · y
6 + x
3[x
3Γ11 + Γ11 y
3] − x
3Γ8 · y6 − xΓ8 · y8 − x6[x3Γ8 + Γ8 · y3] (85)

or in compact form

cy16 = Γ3(x
3, Γ11, y
3) − Γ4(x3, Γ8, y
3) + [Γ8 · y
6 − xΓ8 · y8] (86)

in which the last diﬀerence exactly equals cy16 − x8cy
8. This gives

Γ3(x
3, Γ11, y3) = Γ4(x
3, Γ8, y
3) + xΓ8 · y8. (87)

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4631

which we met earlier in (31).

Let us next use the sandwich recurrence to check this result.

In our example, P1 = 8, P2 = y
14 and P3 = y
16. We must compute F4 = Γr4 P3 = Γ1.y
16 = cy
16. From the
sandwich recurrence we have F4 = I + II, where,

I = {(A3A2A1)F1(α1α2α3) + (A3B2)F1(β2α3) + (B3A1)F1(α1β3)}

and II = (A3A2B1)F0(β1α2α3) + (B3B1)F0(β1β3).

We next compute the coeﬃcients as:
(i) A1 = −x3, A2 = −x
2[x3, 1], A3 = −x

(ii) α1 = 1, α2 = [ 1
y3
 ], α3 = 1. (iii) β1 = 1, β2 = y
8, β3 = y
6 and all Bi = 1. Hence (A3A2A1)F1(α1α2α3) =

(−x){−x
2[x
3, 1](x3F1.1) [ 1
y
3
 ]
}1 = x
8F1 + x
5F1y
3, in addition to (A3B2)F1(β2α3) = (−x{1F1 · y
8} · 1) = −xF1y
8

and (B3A1)F1(α1β3)} = x
3F1y6.

For the second part we compute

(i) (A3A2B1)F0(β1α2α3) = −x{−x
2[x
3, 1](1 · F0 · 1) [ 1
y3
 ]}1 = x6F0 + x
3F0y3 + F0 · y6.

(ii) B3B1)F0(β1β3) = 1(1 · F0 · 1)y
6 = F0 · y
6.
This shows that

F4 = −x
9F1 + x6F1y3 − xF1y
11 − x
3F1y
6 + x
6F0 + x
3F0y
3 + F0y6. (88)

Lastly setting F4 = cy
16, F1 = Γ8 and F0 = Γ11, again yields

cy
16 = [x
6Γ11 + x
3Γ11 y
3 + Γ11 · y6] − [x
9Γ8 − x
6Γ8y
3 + xΓ8 y
8 + x
3Γ8 · y
6. (89)

7.1. The third order case
The above block book-keeping method can be extended to higher order NC
2 recurrences. We shall
restrict ourselves to the third order case.
When we have a third order NC2 diﬀerence equation,

wk+1 = akwk + bkwk−1 + ckwk−2, w0 = λ, w1 = µ, w2 = ν, (90)

we have three variable words in our solution and we must use multinomial coeﬃcients to count the
number of words. For the special case where w0 = 0, w1 = 0, w2 = 1 we obtain the following links:

w3 = a2,

w4 = a3a2 + b3,

w5 = a4a3a2 + (a4b3 + b4a2) + c4,

w6 = a5a4a3a2 + (a5a4b3 + a5b4a2 + b5a3a2) + (a5c4 + b5b3) + c5a2.

We denote by E
k
L(a, b, c) the set of all words ω of length L on ai, bi and ci, where a, b and c denote de
number of ai, bi and ci, resp., in which the (positive) subscripts start in k and decrease from left to right and
such that the subscript drops by 1 after an ai, by two after a bi and by three after a ci.
We aim to show that
 wk+1 =
 k−1∑

a+2b+3c=k−1
a+b+c=L
L=1
 E
k
L(a, b, c).

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4632

The proof will follow by (complete) induction.
Each word in

k∑

a+2b+3c=k
a+b+c=L
L=1
 E
k+1
L (a, b, c) (91)

either starts with ak+1, with bk+1 or with ck+1.

(i) Words that start in (91) with ak+1 are of the form

ak+1
 k∑

a+2b+3c=k−1
a+b+c=L
L=0
 E
k
L(a, b, c) = ak+1
 k−1∑

a+2b+3c=k−1
a+b+c=L
L=1
 E
k
L(a, b, c)

since there are no singleton words for k ≥ 6.
By induction,
 ak+1
 k∑

a+2b+3c=k−1
a+b+c=L
L=0
 E
k
L(a, b, c) = ak+1
 k−1∑

a+2b+3c=k−1
a+b+c=L
L=1
 E
k
L(a, b, c) = ak+1wk+1.

(ii) Words that start in (91) with bk+1 are of the form (recall the subscript drops by 2 after bk+1)

bk+1
 k−1∑

a+2b+3c=k−2
a+b+c=L
L=0
 E
k−1
L (a, b, c).

As in the previous case, the bounds for L can be rewritten since L = 0 cannot occur. Also, L = k − 1
would mean a + b + c = k − 1 and a + 2b + 3c = k − 2, which in turn implies b + 2c = −1. Therefore, L
varies between 1 and k − 2.
Therefore, such words are of the form

bk+1
 k−2∑

a+2b+3c=k−2
a+b+c=L
L=1
 E
k−2
L (a, b, c) = bk+1wk,

by the inductive step.
(iii) Words that start in (91) with ck+1 are of the form (recall the subscript drops by 3 after ck+1)

ck+1
 k−1∑

a+2b+3c=k−3
a+b+c=L
L=0
 E
k−2
L (a, b, c).

Again, the bounds for L can be rewritten since L = 0 can not occur. Also, L > k − 3 would mean
a + b + c > k − 2 and a + 2b + 3c = k − 3, which in turn implies b + 2c < 0. Therefore, L varies between 1
and k − 3.
Therefore, such words are of the form

ck+1
 k−3∑

a+2b+3c=k−3
a+b+c=L
L=1
 E
k−2
L (a, b, c) = ck+1wk−1,

by the inductive step.

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4633

Using (i)–(iii) in (91), we obtain

k∑

a+2b+3c=k
a+b+c=L
L=1
 Ek+1
L (a, b, c) = ak+1wk+1 + bk+1wk + ck+1wk−1 = wk+2.

7.2. Examples

As a ﬁrst example, take k = 6 so that we compute w7. We will need E
6
L(a, b, c), for L = 1, . . . 5. The possible
sets of words are E
6
5(5, 0, 0), E
6
4(3, 1, 0), E
6
3(2, 0, 1), E
6
3(1, 2, 0) and E
6
2(0, 1, 1) to give

w7 = E
6
5(5, 0, 0) + E
6
4(3, 1, 0) + E
6
3(2, 0, 1) + E
6
3(1, 2, 0) + E
6
2(0, 1, 1).

Again, we will simplify the notation by writing j for aj, ¯j for bj and ¯¯j for cj. We obtain

E
6
5(5, 0, 0) = [ 6 5 4 3 2 ] , E
6
4(3, 1, 0) =
 

 6 5 4 ¯3
6 5 ¯4 2
6 ¯5 3 2
¯6 4 3 2
 
 , E
6
3(2, 0, 1) =
 

 6 5 ¯¯4
6 ¯¯5 2
¯¯6 3 2
 


and
 E
6
3(1, 2, 0) =
 

 6 ¯5 ¯3
¯6 4 ¯3
¯6 ¯4 2
 
 , E
6
2(0, 1, 1) = [ ¯6 ¯¯4
¯¯6 ¯3
 ] .

The numbers of terms are
 a b c
5 − − ( 5
5,0,0)

3 1 ( 4
3,1,0)

1 2 − ( 3
2,0,1)

2 − 1 ( 3
1,2,0)

− 1 1 ( 2
0,1,1)
 .

Parallel to (wk), we have the recurrence relations

uk+1 = akuk + bkuk−1 + ckuk−2, u0 = 1, u1 = u2 = 0

and vk+1 = akvk + bkvk−1 + ckvk−2, v0 = 0, v1 = 1, v2 = 0.

Let us compute, for future purpose, the ﬁrst terms.

u3 = c2
u4 = a3c2
u5 = a4a3c2 + b4c2
u6 = a5a4a3c2 + a5b4c2 + b5a3c2 + c5c2

and
 v3 = b2
v4 = a3b2 + c3
v5 = a4a3b2 + a4c3 + b4b2
v6 = a5a4a3b2 + a5a4c3 + a5b4b2 + b5a3b2 + b5c3 + c5b2

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4634

In order to give an algorithm that would allow us to present the terms of (uk) and (vk), we note that



 wk+1
wk
wk−1
 
 = LkLk−1 · · · L2
 

 1
0
0
 
 ,

where

Lk =
 

 ak bk ck
1 0 0
0 1 0
 
 . (92)

(I) The sequence (uk).

Since
 

 uk+1
uk
uk−1
 
 = LkLk−1 · · · L2
 

 0
0
1
 
 , where the matrices Li are as in (92) and L2
 

 0
0
1
 
 =
 

 1
0
0
 
 c2 then we get



 uk+1
uk
uk−1
 
 =
 k∏

i=3 Li
 

 1
0
0
 
 c2.

Note that ∏k
i=3 Li
 

 1
0
0
 
 gives essentially (wk), with a index shift by one. This allows us to obtain uk+1 as

follows:

1. Obtain wk;
2. Replace xi by xi+1, where x ∈ {a, b, c};
3. Multiply every summand on the right by c2.

As an example, let us apply the above algorithm to compute u6.

1. We are given w5 = a4a3a2 + a4b3 + b4a2 + c4;
2. We change the indices to get a5a4a3 + a5b4 + b5a3 + c5;
3. Multiplying on the right by c2, we obtain

u6 = a5a4a3c2 + a5b4c2 + b5a3c2 + c5c2.

(II) The sequence (vk).
From


 vk+1
vk
vk−1
 
 = LkLk−1 · · · L2
 

 0
1
0
 


= Lk · · · L3
 



 1
0
0
 
 b2 +
 

 0
0
1
 





= Lk · · · L3
 

 1
0
0
 
 b2 + Lk · · · L3
 

 0
0
1
 
 ,

which shows that we may compute vk+1 by simultaneously using wk and uk as follows:

1. (a) obtain wk
(b) replace xi by xi+1, where x ∈ {a, b, c},
(c) multiply every summand on the right by b2.

P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4635

2. (a) obtain uk
(b) replace xi by xi+1, where x ∈ {a, b, c}
3. add all the expressions obtained.

Let us give an example by computing v6:

1. We use w5 to give a5a4a3b2 + a5b4b2 + b5a3b2 + c5b2
2. We use u5 to give a5a4c3 + b5c3
3. v6 = a5a4a3b2 + a5b4b2 + b5a3b2 + c5b2 + a5a4c3 + b5c3

Our second example uses the computer program SageMath [15] to check the solutions to the NC
2 three term
Recurrence relation. We shall only use the initial conditions w0 = 0, w1 = 0, w1 = 1, from which the other two
can be derived. The code is available at http://w3.math.uminho.pt/ pedro/Telescoping/telescoping.html.
For the case where k = 15, all words of length 7 must be of the form

#(ai) #(bj) #(ck) number o f words
0 7 0 ( 7
0,7,0) = 1
1 5 1 ( 7
1,5,1
) = 42
2 3 2 ( 7
2,3,2) = 210
3 1 3 ( 7
3,1,3) = 140

The set of the 42 possible words with 1 a, 5 b’s and 1 c is as follows

a15b14b12b10b8b6c4, a15b14b12b10b8c6b3, a15b14b12b10c8b5b3,

a15b14b12c10b7b5b3, a15b14c12b9b7b5b3, a15c14b11b9b7b5b3,

b15a13b12b10b8b6c4, b15a13b12b10b8c6b3, b15a13b12b10c8b5b3,

b15a13b12c10b7b5b3, b15a13c12b9b7b5b3, b15b13a11b10b8b6c4,

b15b13a11b10b8c6b3, b15b13a11b10c8b5b3, b15b13a11c10b7b5b3,

b15b13b11a9b8b6c4, b15b13b11a9b8c6b3, b15b13b11a9c8b5b3,

b15b13b11b9a7b6c4, b15b13b11b9a7c6b3, b15b13b11b9b7a5c4,

b15b13b11b9b7c5a2, b15b13b11b9c7a4b3, b15b13b11b9c7b4a2,

b15b13b11c9a6b5b3, b15b13b11c9b6a4b3, b15b13b11c9b6b4a2,

b15b13c11a8b7b5b3, b15b13c11b8a6b5b3, b15b13c11b8b6a4b3,

b15b13c11b8b6b4a2, b15c13a10b9b7b5b3, b15c13b10a8b7b5b3,

b15c13b10b8a6b5b3, b15c13b10b8b6a4b3, b15c13b10b8b6b4a2,

c15a12b11b9b7b5b3, c15b12a10b9b7b5b3, c15b12b10a8b7b5b3,

c15b12b10b8a6b5b3, c15b12b10b8b6a4b3, c15b12b10b8b6b4a2.

8. Concluding remarks and questions

1. We may extend the two-sided recurrence to three or more terms.
2. We note that recurrence relation for corner sums correspond to annihilating polynomials for 2 × 2
matrices M, which leads to Division Algorithms.
3. How can we relate annihilating polynomials to the corner sums?
4. Can we ﬁnd other uses or applications of GPs?
5. Are there any other classes of objects such as matroids for which we can apply the telescoping tricks,
and mimic Euclid’s construction?
6. How do Hankel matrices telescope?
7. Are there any other relations such as the switching identity Gm(x
n)/Gm(x) = Gn(x
m)/Gn(x), using three
powers x
mnk − 1?
 P. Patr´ıcio, R.E. Hartwig / Filomat 35:14 (2021), 4613–4636 4636

Acknowledgements

The authors thank the anonymous referee for his/her valuable corrections.

References

[1] F. G. Boese, On ordinary diﬀerence equations with variable coeﬃcients, J. Math. Anal. Appl., 273 (2002), 378-408.
[2] N. Castro-Gonz´alez, R. E. Hartwig, More on Companion matrices, preprint.
[3] M. Drazin, The equation ac = cb, unpublished note.
[4] F. R. Gantmacher, The theory of matrices Vol. 2, Translated from the Russian by K. A. Hirsch. Reprint of the 1959 translation. AMS
Chelsea Publishing, Providence, RI, 1998.
[5] R. E. Hartwig, Note on a linear diﬀerence equation, Amer. Math. Monthly 113 (2006), no. 3, 250–256.
[6] R. E. Hartwig, All you should know about your Companion, Bulletin CIM, 27, Jan 2010, pp.22–32.
[7] R. E. Hartwig, X. Chen, The Picard iteration and its application, Linear Multilinear Algebra 54 (2006), no. 5, 329–341.
[8] R. E. Hartwig, F. Hall, Algebraic properties of governing matrices used in Ces`aro-Neumann iterations, Revue Roum. Math. Pures
Appl. 26 (1981), 959–978.
[9] R. E. Hartwig, P. Patricio, A note on power bounded matrices, Electron. J. Linear Algebra 23 (2012), 625–645.
[10] R. E. Hartwig, P. Patricio, Two by two units, Electron. J. Linear Algebra 27 (2014), 489–503.
[11] R. E. Hartwig, P. Semrl, Constrained convergence, Rocky Mountain J. Math., 29 (1999), 177–195.
[12] R. K. Mallik, Solutions of Linear Diﬀerence Equations with Variable Coeﬃcients, J. Math. Anal. Appl. 222 (1998), 79–91.
[13] P. Patricio, R. E. Hartwig, Some regular sums, Linear and Multilinear Algebra, 63(1) (2015), 185–200.
[14] K. Rosen, Elementary number theory and its applications, 5th edition AT&T, 2005.
[15] SageMath, the Sage Mathematics Software System (Version 9.2), The Sage Developers, 2020, https://www.sagemath.org.
