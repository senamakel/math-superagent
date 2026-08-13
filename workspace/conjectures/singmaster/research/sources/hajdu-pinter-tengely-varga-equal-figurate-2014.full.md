<!-- source: https://shrek.unideb.hu/~tengely/hptvrevised.pdf | converted from PDF -->

EQUAL VALUES OF FIGURATE NUMBERS

LAJOS HAJDU, ´AKOS PINT´ER, SZABOLCS TENGELY, AND N ´ORA VARGA

Abstract. Some eﬀective results for the equal values of ﬁgu-
rate numbers are proved. Using a state-of-the-art computational
method for the small parameter values the corresponding Diophan-
tine equations are resolved.

1. Introduction

There are several results concerning arithmetical and Diophantine
properties of certain combinatorial numbers. Let k, m be integers with
k ≥ 3 and m ≥ 3, further, denote by

fk,m(X) = X(X + 1) . . . (X + k − 2)((m − 2)X + k + 2 − m)
k!
the Xth ﬁgurate number with parameters k and m. For some problems
and theorems related to these families of combinatorial numbers, we
refer to the books [11] and [10]. The power and equal values of special
cases of fk,m(X), including, for instance, binomial coeﬃcients (for m =
3), polygonal numbers (for k = 2) and pyramidal numbers (for k = 3)
have been studied intensively, see [1], [20], [4], [23], [8], [9], [14], [18],
[19], [17], [16] and references therein. Brindza, Pint´er and Turj´anyi [5]
conjectured that apart from the case (m, n) = (5, 4) the equation

f3,m(x) = f2,n(y)

has only ﬁnitely many solutions in integers x, y which can be eﬀectively
determined. Recently, Pint´er and Varga [24] conﬁrmed this conjecture.

2010 Mathematics Subject Classiﬁcation. 11D41.
Key words and phrases. Diophantine equations, ﬁgurate numbers.
Research was supported in part by the Hungarian Academy of Sciences, OTKA
grants T67580, K75566, K100339, NK101680, NK104208 and by Projects T ´AMOP-
4.2.2/B-10/1-2010-0024, T ´AMOP-4.2.2.C-11/1/KONV-2012-0001, and T ´AMOP
4.2.4. A/2-11-1-2012-0001 National Excellence Program - Elaborating and oper-
ating an inland student and researcher personal support system” subsidized by the
European Union and co-ﬁnanced by the European Social Fund. This work was
partially also supported by the European Union and the European Social Fund
through project Supercomputer, the national virtual lab (grant no.: T ´AMOP-
4.2.2.C-11/1/KONV-2012-0010). 1

2 LAJOS HAJDU, ´AKOS PINT´ER, SZABOLCS TENGELY, AND N ´ORA VARGA

The purpose of the note at hand is to give eﬀective ﬁniteness statements
for the more general equation

(1) fk,m(x) = f2,n(y)

in integers x and y and to provide numerical results for small values
of parameters (k, m, n). In a forthcoming paper we will deal with the
equation fk,m(x) = fl,n(y).
However, in this generality we can give only ineﬀective ﬁniteness the-
orems.
 2. Main results

Theorem 2.1. Let m, n, k be integers with k ≥ 3 and (m, n, k) ̸=
(5, 4, 3), (6, 4, 4). If k is even, then assume further that k!D is not
of the form r2, 2r2, where D = gcd(k!(n − 4)
2, 8d(n − 2)) with d =
gcd(k, m − 2). Then equation (1) has only ﬁnitely many solutions in
x, y which can be eﬀectively determined.

If (m, n, k) = (5, 4, 3), (6, 4, 4), then one can easily see that equation
(1) has inﬁnitely many solutions in x, y. As an immediate consequence
of Theorem 2.1, we obtain the following statement.

Corollary 2.1. Let m, n, k be integers with k ≥ 4. If k is even, then
assume further that there exists a prime p with k/2 < p < k such that
p ∤ n − 2. Then equation (1) has only ﬁnitely many solutions in x, y
which can be eﬀectively determined.

Remark. Note that if k > 2n, then the condition in Corollary 2.1 is
satisﬁed. Indeed, Bertrand’s postulate guarantees the existence of a
prime p with k/2 < p < k. Since now p > k/2 = n > n − 2, we also
have p ∤ n − 2.

Theorem 2.2. Suppose that k ≥ 3, m ≥ 3, n ≥ 3 are integers with

10m − 26 ≤ n.

Then equation (1) possesses only ﬁnitely many solutions in x, y which
can be eﬀectively determined.

We closely follow arguments of Erd˝os [12, 13] and resolve an inﬁnite
family of Diophantine equations.

Theorem 2.3. The only solution of the equation

(2) fk,k+2(x) = f2,4(y)

in integers k ≥ 5, x ≥ k − 2 and y ≥ 1 is (k, x, y) = (5, 47, 3290).

EQUAL VALUES OF FIGURATE NUMBERS 3

For k = 5, our theorem follows from a classical theorem by Meyl [22].
The resolution of another parametric family of Diophantine problems
(
x + k − 1
k
 ) = fk,3(x) = f2,4(y) = y2

in integers x, y and k follows from the result of Gy˝ory [14] on the power
values of binomial coeﬃcients.
Consider now the case k = 5. Then equation (1) can be reduced to
the Diophantine equation

(3) 15(n−2)x(x+1)(x+2)(x+3)((m−2)x+7−m)+(15(4−n))2 = z2,

where z = 30(n − 2)y + 15(4 − n).
The curve (3) is a genus 2 hyperelliptic curve except for ﬁnitely many
pairs of (m, n), where m, n ≥ 3. The exceptional pairs (m, n) could be
explicitly given by Runge’s method. However, this would require a lot
of calculations, involving a large amount of technical data. Since this
point is not vital for our purposes, we suppress the details.
We computed the rank r (an upper bound for the rank in some cases)
of the Jacobian of the corresponding hyperelliptic curve for m, n ∈
{3, 4, 5, 6, 7, 8}.
n \ m 3 4 5 6 7 8
3 6 5 5 6 4 6
4 1 ≤ r ≤ 5 2 ≤ r ≤ 6 2 ≤ r ≤ 6 3 ≤ r ≤ 7 - 1 ≤ r ≤ 5
5 4 5 4 4 2 5
6 6 5 5 6 4 6
7 5 5 5 5 4 5
8 6 5 7 7 4 6

We note that the problem in case of (m, n) = (3, 3) yields the equation
(x + 4
5
 ) = (
y + 1
2
 )
.

All integral points were determined by Bugeaud, Mignotte, Siksek, Stoll
and Tengely [6] on the related curve hyperelliptic curve. They com-
bined Baker’s method and the so-called Mordell-Weil sieve to obtain
the result. We follow their method to ﬁnd all integral points on the
curve (3) with m = 7 and n = 5, and hence to obtain all solutions of
(1) for these values of parameters.

Theorem 2.4. The set of integral points (x, y) on the curve (3) with
(m, n) = (7, 5) is

{(−3, 0), (−2, 0), (−1, 0), (0, 0), (1, 1)}.

4 LAJOS HAJDU, ´AKOS PINT´ER, SZABOLCS TENGELY, AND N ´ORA VARGA

3. Auxiliary results

In the proof of Theorem 2.1 the next result plays the key role. In
fact it provides more information than is needed to prove Theorem 2.1.

Proposition 3.1. Let t ≥ 0 be an integer, and write Pt(x) = x(x +
1) . . . (x + t). Let f (x) ∈ Z[x] and v ∈ Z \ {0} such that g(x) :=
Pt(x)f (x) + v is a primitive polynomial.
• If t ≥ 3 and deg(g) is odd, then g(x) has at least three roots of
odd multiplicities.
• If t ≥ 2, deg(g) is even and v is not of the form ±r2, ±2r2,
then g(x) has at least three roots of odd multiplicities.
• Let ℓ ≥ 3. If t ≥ 3 and deg(f ) < (t + 1)(ℓ − 1), then g(x) has
at least two roots with multiplicities not divisible by ℓ.

Proof. To prove the ﬁrst part, suppose that deg(g) is odd, but it has
less than three roots of odd multiplicities. Then we can write

Pt(x)f (x) + v = (h(x))
2(ax + b)

with some h ∈ Z[x] and a, b ∈ Z. Further, a ̸= 0, and by the primitivity
of g we have gcd(a, b) = 1. As 0, −1, −2, −3 are roots of Pt(x), we
obtain

(h(0))
2b = (h(−1))2(b − a) = (h(−2))
2(b − 2a) = (h(−3))
2(b − 3a).

Observe that since v ̸= 0, none of the above numbers is zero. As
gcd(a, b) = 1, this implies that either b, b − a, b − 2a, b − 3a or −b, a −
b, 2a−b, 3a−b are all squares. However, by classical results of Euler and
Fermat we have that four distinct squares cannot form an arithmetic
progression (see [11], pp. 440 and 635). Hence our statement follows
in this case.
To prove the second part, assume that deg(g) is even, but it has less
than three roots of odd multiplicities. As v is not a square, by our
assumptions g(x) cannot be a constant (integral) multiple of a square
of a polynomial in Z[x]. Thus the only possibility is that we have

Pt(x)f (x) + v = (h(x))
2(ax
2 + bx + c)

with some h ∈ Z[x] and a, b, c ∈ Z. Further, a ̸= 0, and by the
primitivity of g we have gcd(a, b, c) = 1. Since t ≥ 2, now we obtain

(h(0))
2c = (h(−1))
2(a − b + c) = (h(−2))2(4a − 2b + c) = v.

As v ̸= 0, none of the above numbers is zero. By a simple calculation
we get that only gcd(c, a−b+c, 4a−2b+c) = 1, 2 are possible. Assume
that there is an odd prime q occurring on an odd power in the prime
factorization of c. Then by the above equalities, q also occurs on an

EQUAL VALUES OF FIGURATE NUMBERS 5

odd exponent in the prime factorization of v, whence q | a − b + c and
q | 4a − 2b + c follows. However, this is impossible. Hence c is one
of the form ±r2, ±2r2. But then the same is true for v, which is a
contradiction. Hence the statement follows also in this case.
To prove the third part, suppose to the contrary that g(x) has at
most one root of multiplicity not divisible by ℓ. Consider ﬁrst the case
where g(x) is an ℓ-th power in Z[x], that is

Pt(x)f (x) + v = (h(x))ℓ

with some h ∈ Z[x]. Writing F and H for the degrees of f and h
respectively, we get t + 1 + F = ℓH.

On the other hand, by our assumption we have

F < (t + 1)(ℓ − 1).

Combining these assertions, we obtain that H < t + 1. On the other
hand, we have
 h(0) = h(−1) = · · · = h(−t) = v,

that is, h takes the same value at t + 1 diﬀerent places. It yields that
h(x) is identically constant. It is a contradiction, and our statement
follows in this case.
Finally, we are left with the possibility

Pt(x)f (x) + v = (h(x))
ℓ(ax + b)s

with some h ∈ Z[x], a, b ∈ Z with gcd(a, b) = 1 and s with 1 ≤ s < ℓ.
As t ≥ 3, we have

(h(0))
ℓbs = (h(−1))ℓ(b − a)
s = (h(−2))
ℓ(b − 2a)
s = (h(−3))ℓ(b − 3a)
s.

As gcd(a, b) = 1, similarly as in case of ℓ = 2 we get that

b
s, (b − a)
s, (b − 2a)
s, (b − 3a)
s

are all non-zero perfect ℓ-th powers. This by s < ℓ yields that

b, b − a, b − 2a, b − 3a

are all perfect ℓ′-th powers with some ℓ′ = ℓ
gcd(s,ℓ) ≥ 2. However, by a
deep result of Darmon and Merel [7] four distinct ℓ
′-th powers cannot
form an arithmetic progression. Hence our statement follows. □

Our next lemma is a classical result from the modern theory of Dio-
phantine equations.

6 LAJOS HAJDU, ´AKOS PINT´ER, SZABOLCS TENGELY, AND N ´ORA VARGA

Lemma 3.1. Let t(X) ∈ Q[X] and suppose that the polynomial t(X)
possesses at least three zeros of odd multiplicities. Then the equation
t(x) = y2 in integers x, y implies that max(|x|, |y|) < C, where C is an
eﬀectively computable constant depending only on the polynomial t(X).

Proof. The result is a consequence of the Theorem in Brindza [3]. □

4. Proofs

Proof of Theorem 2.1. Equation (1) can be rewritten as

8(n − 2)x(x + 1) . . . (x + k − 2)((m − 2)x + k + 2 − m)
k! + (n − 4)
2 =

= (2(n − 2)y + n − 4)2.

(4)

So to prove the statement we only need to show that the polynomial
T (x) on the left hand side of the above equation has at least three
zeroes of odd multiplicities. If n = 4, then one can easily check that
this assertion is valid, provided that (m, k) ̸= (5, 3), (6, 4). So from this
point on we may assume that n ̸= 4.
Write d := gcd(k, m − 2), and D := gcd(k!(n − 4)2, 8(n − 2)d). Then
we obviously have that k!T (x)/D is a primitive polynomial in Z[x],
with constant term k!(n − 4)
2/D. Hence in view of Proposition 3.1,
the theorem follows. □

Proof of Corollary 2.1. Observe that by d | k, we have d = k or d ≤
k/2. Further, k ≥ 4 also yields 2 ≤ k/2. Hence if there exists a prime
p with the desired properties, then obviously, p divides k!(n − 4)2 on
an odd exponent, but p ∤ D is valid. Thus the statement immediately
follows from Theorem 2.1. □

Proof of Theorem 2.2. Observe that equation (1) can be rewritten as

8(n − 2)fk,m(X) + (n − 4)
2 = z2,

where z = 2(n − 2)y + n − 4. Suppose that α is a multiple zero of the
polynomial

8(n − 2)fk,m(X) + (n − 4)
2 =

= 8(n − 2)(m − 2)
k! X(X +1)(X +2) . . . (
X + k
m − 2 − 1
)+(n−4)
2.

Then α is a zero of the polynomial

g(X) := (
X(X + 1) . . . (X + k − 2) (
X + k
m − 2 − 1
))′ .

EQUAL VALUES OF FIGURATE NUMBERS 7

In case of k
m−2 −1 /∈ H := {0, −1, . . . , −k+2}, using Rolle’s theorem one
can check that these zeros are real and belong to the interval (1 − k, 1).
When k
m−2 −1 ∈ H, this property can be easily veriﬁed by checking the
sign of g(X) in small neighborhoods of the elements of H. For m = 3
the statetement follows from a nice result of Gy˝ory [14]. Thus we may
assume that m ≥ 4. Hence for an arbitrary real number β ∈ (1 − k, 1)
the product
∣
∣
∣
∣β · (β + 1) · . . . · (β + k − 2) (
β + k
m − 2 − 1)∣
∣
∣
∣

is smaller than

(k − 1)! (
k − 1 − k
m − 2 + 1) = k!m − 3
m − 2.

This shows that for any multiple root α of the polynomial

8(n − 2)fk,m(X) + (n − 4)
2

we have

(n−4)2 = |8(n − 2)fk,m(α)| < 8(m−2)(n−2)m − 3
m − 2 = 8(m−3)(n−2).

That is, the above polynomial has no multiple roots, provided that

8(m − 3)(n − 2) ≤ (n − 4)2.

Observe that this inequality cannot hold for n < 14. As 10m − 26 ≤ n
implies that 8(m − 3)(n − 2) ≤ (n − 4)
2 whenever n ≥ 14, Lemma 3.1
ﬁnishes our proof. □

Proof of Theorem 2.3. Equation (2) can be rewritten as

(5) x
2(x + 1) . . . (x + k − 2) = (k − 1)!y2.

First, using standard arguments, but with a slight modiﬁcation implied
by the presence of the factor k − 1 on the right hand side of (5), we
can write

(6) x + i = aix
2
i (i = 1, . . . , k − 2),

where the ai are square-free positive integers with P (ai) ≤ k − 1, where
P (u) denotes the greatest prime factor of u, with the convention P (1) =
1. First we prove that the coeﬃcients ai are pairwise diﬀerent. Assume
to the contrary that ai = aj holds with some i < j. Then we have

k − 2 > (x + j) − (x + i) = aix
2
j − aix
2
i = ai(x
2
j − x
2
i ) ≥

≥ ai((xi + 1)2 − x
2
i ) > 2√
aix
2
i ≥ 2
√x + 1.

8 LAJOS HAJDU, ´AKOS PINT´ER, SZABOLCS TENGELY, AND N ´ORA VARGA

On the other hand, as x ≥ k − 2, by Corollary 1 of Laishram and
Shorey [21] we obtain that up to fourteen exceptions listed explicitly,
the product (x + 1) . . . (x + k − 2) has a prime factor > 1.8(k − 2). As
one can easily check, these exceptions do not yield solutions to equation
(2). Indeed, for example when x + 1 = 8, k − 2 = 3, the product is
given by 8·9·10, with greatest prime factor 5, and 5 < 1.8·3. However,
then we have x = 7 and k = 5, and equation (2) does not hold. The
remaining exceptional case can be excluded similarly. Thus we may
assume that q is a prime such that q divides (x + 1) . . . (x + k − 2) and
q > 1.8(k − 2). Observe that then q divides exactly one term x + i
(i = 1, . . . , k − 2). Since q > k − 1 as k ≥ 5, q occurs in x + i on at
least the second power. This yields

3.24(k − 2)
2 < q2 ≤ x + k − 2.

Combining this bound with the above estimate k − 2 > 2√
x + 1, in
view of x ≥ k − 2, we get a contradiction. This implies that ai ̸= aj
indeed, whenever i ̸= j.
Now we prove that the product a1 · · · ak−2 divides (k − 1)!. For this,
rewrite (2) as
 A := a1 · · · ak−2
(k − 1)! = y2

z2

where z = x · x1 · · · xk−2. Let p be any prime, and let νp(A) = α. Here
νp(A) is the exponent of p in A; note that α may be negative, too.
Then, recalling that the coeﬃcients ai are square-free, by Liouville’s
formula concerning the exponents of primes in a factorial we clearly
have
 α ≤ [ k − 2
p
 ] + 1 − [ k − 1
p
 ] ≤ 1.

Since α must obviously be even, this yields α ≤ 0, which immediately
implies our claim a1 · · · ak−2 | (k − 1)!. This of course gives

a1 · · · ak−2 ≤ (k − 1)!.

If 5 ≤ k < 15, then the only solution is given by (k, x, y) = (5, 47, 3290).
This fact can be checked in the following way. First observe that by
(6) we have

(7) (x + 1) · · · (x + k − 2) = uv2,

where u = a1 · · · ak−2 and v = x1 · · · xk−2. Further, here q | v, therefore
the greatest prime divisor of v is greater than k − 2. Thus, by a result
of Gy˝ory [15] we have that if k −1 is not a prime, then the only solution
of (7) is given by (x, k, u, v) = (47, 5, 6, 140). This shows that the only
solution to equation (1) is (k, x, y) = (5, 47, 3290) in this case. Hence we

EQUAL VALUES OF FIGURATE NUMBERS 9

may assume that k−1 is a prime, i.e. k = 6, 8, 12, 14. The investigation
of these cases is similar, so we illustrate our method only for k = 6.
Then equation (1) is given by x
2(x + 1)(x + 2)(x + 3)(x + 4) = 120y2.
Checking the greatest common divisors of x + i and x + j (1 ≤ i <
j ≤ 4), we get the possible values of a1, a2, a3 in (6). Hence we obtain
elliptic equations of the form

(x + 1)(x + 2)(x + 3) = Az2,

where A is square-free, and z is given by z = Bx1x2x3 with AB2 =
a1a2a3. It turns out that we have A ∈ {1, 2, 3, 5, 6, 10, 15, 30}. We
used a MAGMA [2] code to solve these equations and we got that
the only solutions are given by (x, z) = (7, 12) with A = 5, (x, z) =
(0, 1), (1, 2), (47, 140) with A = 6, (x, z) = (2, 2) with A = 15 and
(x, z) = (3, 2) with A = 30. It follows that the only solution of (1) is
(k, x, y) = (5, 47, 3290).
Assume now that k ≥ 15. Then, since the numbers a1, . . . , ak−2 are
k − 2 pairwise diﬀerent square-free integers, we have

a1 . . . ak−2 ≥ 1·2·3·5·6·7·10·11·13·. . .·(k−1)·k·(k+1)·(k+2) > (k−1)!.

(The second inequality follows from the fact that k · (k + 1) · (k + 2) >
4 · 8 · 9 · 12, as k ≥ 15.) However, this by the previous inequality yields
a contradiction. That is, equation (2) has no solutions for k ≥ 15, and
the theorem follows. □

Proof of Theorem 2.4. The curve (3) with m = 7 and n = 5 is isomor-
phic to

(8) X 2(X + 1)(X + 2)(X + 3) + 1 = Y 2.

Let J(Q) be the Jacobian of the genus two curve (8). Using MAGMA
[2] we get that J(Q) is free of rank 2 with Mordell-Weil basis given by

D1 = (−1, 1) − ∞,
D2 = (ω, 2ω + 3) + (ω, 2ω + 3) − 2∞,

where ω is a root of the polynomial z2+3z+2. The MAGMA procedures
used to compute these data are based on Stoll’s papers [25], [26], [27].
Let f = X 2(X + 1)(X + 2)(X + 3) + 1 and α be a root of f. We will
choose for coset representatives of J(Q)/2J(Q) the linear combinations∑2
i=1 niDi, where ni ∈ {0, 1}. Then

X − α = κξ2,

where κ is from a ﬁnite set. Such a ﬁnite set can be constructed fol-
lowing Lemma 3.1 in [6]. In case of the curve (8) we obtain that
κ ∈ {1, −α − 1, α2 + α, α2 + 3α + 2}. We applied Theorem 9.2 in [6] to

10 LAJOS HAJDU, ´AKOS PINT´ER, SZABOLCS TENGELY, AND N ´ORA VARGA

get a large upper bound for log |X|. A MAGMA code were written to
obtain such bounds, it can be found at
http://www.warwick.ac.uk/∼maseap/progs/intpoint/bounds.m. In
our case this bound turned out to be

log |X| ≤ 6.647 × 10412.

A search reveals 13 rational points on the genus 2 curve (8):

∞, (−3, ±1), (−2, ±1), (−1, ±1),
(−7/4, ±17/32), (0, ±1), (1, ±5).

Let W be the image of the set of these known rational points in J(Q).
There are three points in the coset represented by 0:

±6D1 = (−7/4, ±17/32) − ∞

and ∞. There are two points in the same coset as D1 :

±D1 = (−1, ±1) − ∞.

In the coset of D2 we obtain 6 points:

±(2D1 + 3D2) = (−3, ±1) − ∞,
±(2D1 + D2) = (0, ∓1) − ∞,
±(2D1 − 3D2) = (1, ±5) − ∞.

Finally, two points belong to the coset of D1 + D2 :

±(D1 − D2) = (−2, ±1) − ∞.

Applying the Mordell-Weil sieve explained in [6] we obtain that ȷ(C(Q)) ⊆
W + BJ(Q), where

B = 2841720553897526432308772658708262465848000.

We follow an extension of the Mordell-Weil sieve due to Siksek to obtain
a long decreasing sequence of lattices in Z
2. After that we apply Lemma
12.1 in [6] to obtain a lower bound for possible unknown rational points.
We have that if (X, Y ) is an unknown integral point, then

log |X| ≥ 3.32 × 10
494.

This contradicts the bound for log |X| obtained by Baker’s method.
Hence the set of integral points on the curve (8) is

{(−3, ±1), (−2, ±1), (−1, ±1), (0, ±1), (1, ±5)}.

These points correspond to the following set of integral points on (3):

{(−3, 0), (−2, 0), (−1, 0), (0, 0), (1, 1)}.
 □

EQUAL VALUES OF FIGURATE NUMBERS 11

5. Acknowledgements

The authors are grateful to the referee for her/his useful and helpful
remarks.
 References

[1] `E. T. Avanesov. Solution of a problem on ﬁgurate numbers. Acta Arith.,
12:409–420, 1966/1967.
[2] W. Bosma, J. Cannon, and C. Playoust. The Magma algebra system. I. The
user language. J. Symbolic Comput., 24(3-4):235–265, 1997. Computational
algebra and number theory (London, 1993).
[3] B. Brindza. On S-integral solutions of the equation ym = f (x). Acta Math.
Hungar., 44(1-2):133–139, 1984.
[4] B. Brindza. On a special superelliptic equation. Publ. Math. Debrecen, 39(1-
2):159–162, 1991.
[5] B. Brindza, ´A. Pint´er, and S. Turj´anyi. On equal values of pyramidal and
polygonal numbers. Indag. Math. (N.S.), 9(2):183–185, 1998.
[6] Y. Bugeaud, M. Mignotte, S. Siksek, M. Stoll, and S. Tengely. Integral points
on hyperelliptic curves. Algebra Number Theory, 2(8):859–885, 2008.
[7] H. Darmon and L. Merel. Winding quotients and some variants of Fermat’s
last theorem. J. Reine Angew. Math., 490:81–100, 1997.
[8] B. M. M. de Weger. A binomial Diophantine equation. Quart. J. Math. Oxford
Ser. (2), 47(186):221–231, 1996.
[9] B. M. M. de Weger. Equal binomial coeﬃcients: some elementary considera-
tions. J. Number Theory, 63(2):373–386, 1997.
[10] E. Deza and M. M. Deza. Figurate numbers. World Scientiﬁc Publishing Co.
Pte. Ltd., Hackensack, NJ, 2012.
[11] L. E. Dickson. History of the theory of numbers. Vol. II: Diophantine analysis.
Chelsea Publishing Co., New York, 1966.
[12] P. Erd˝os. Note on the product of consecutive integers (II). J. London Math.
Soc., 14:245–249, 1939.
[13] P. Erd˝os. On a Diophantine equation. J. London Math. Soc., 26:176–178, 1951.
[14] K. Gy˝ory. On the Diophantine equation (n
k) = xl. Acta Arith., 80(3):289–295,
1997.
[15] K. Gy˝ory. On the Diophantine equation n(n + 1) · · · (n + k − 1) = bxl. Acta
Arith., 83(1):87–92, 1998.
[16] K. Gy˝ory, A. Dujella, and ´A. Pint´er. On the power values of pyramidal num-
bers, II. manuscript.
[17] K. Gy˝ory, A. Dujella, and ´A. Pint´er. On the power values of pyramidal num-
bers, I. Acta Arith., 155(2):217–226, 2012.
[18] L. Hajdu and ´A. Pint´er. Combinatorial Diophantine equations. Publ. Math.
Debrecen, 56(3-4):391–403, 2000. Dedicated to Professor K´alm´an Gy˝ory on
the occasion of his 60th birthday.
[19] M. Kaneko and K. Tachibana. When is a polygonal pyramid number again
polygonal? Rocky Mountain J. Math., 32(1):149–165, 2002.
[20] P. Kiss. On the number of solutions of the Diophantine equation (x
p) = (
y
2).
Fibonacci Quart., 26(2):127–130, 1988.

12 LAJOS HAJDU, ´AKOS PINT´ER, SZABOLCS TENGELY, AND N ´ORA VARGA

[21] S. Laishram and T. N. Shorey. The greatest prime divisor of a product of
consecutive integers. Acta Arith., 120(3):299–306, 2005.
[22] A. J. J. Meyl. Solution de question 1194. Nouv. Ann. Math., 17:464–467, 1878.
[23] ´A. Pint´er. A note on the Diophantine equation (x
4) = (y
2)
. Publ. Math. Debre-
cen, 47(3-4):411–415, 1995.
[24] ´A. Pint´er and N. Varga. Resolution of a nontrivial diophantine equation with-
out reduction methods. Publ. Math. Debrecen, 79(3-4):605–610, 2011.
[25] M. Stoll. On the height constant for curves of genus two. Acta Arith.,
90(2):183–201, 1999.
[26] M. Stoll. Implementing 2-descent for Jacobians of hyperelliptic curves. Acta
Arith., 98(3):245–277, 2001.
[27] M. Stoll. On the height constant for curves of genus two. II. Acta Arith.,
104(2):165–182, 2002.

Institute of Mathematics
P. O. Box 12, H-4010 Debrecen, Hungary
E-mail address: hajdul@science.unideb.hu, tengely@science.unideb.hu

Institute of Mathematics
MTA-DE Research Group ”Equations, Functions and Curves”
Hungarian Academy of Sciences and University of Debrecen
P. O. Box 12, H-4010 Debrecen, Hungary
E-mail address: apinter@science.unideb.hu, nvarga@science.unideb.hu
