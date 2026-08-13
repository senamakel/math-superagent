<!-- source: http://cseweb.ucsd.edu/~dakane/combinations.pdf | converted from PDF -->

NEW BOUNDS ON THE NUMBER OF

REPRESENTATIONS OF t AS A BINOMIAL COEFFICIENT

Daniel Kane

Abstract. For t > 1, let N (t) denote the number of ways that t can be written as a binomial

coeﬃcient. We prove that N (t) = O  log t·log log log t
(log log t)2  .

1. Introduction and statement of results

If t > 1, then let N (t) denote the number of ways that t can be written as a binomial
coeﬃcient. Abbot, Erd˝os, and Hanson show in [1] that

N (t) = O ( log t
log log t
 ) .

They also note that if Cramer’s conjecture is true (i.e. if for some x0 and all x > x0 there
is always a prime number between x and x + log2 x), then this bound can be improved to

N (t) = O ((log t)
(2/3+ϵ))

for any ϵ > 0. It has also been conjectured by D. Singrester that N (t) = O(1).
We improve on the ﬁrst of these bounds by proving the following theorem.

Theorem 1. With N (t) deﬁned above,

N (t) = O ( log t · log log log t
(log log t)2
 ) .
 Typeset by AMS-TEX
1

2 DANIEL KANE

2. Preliminary Lemmas

Here are several important facts that we shall be using. If Γ(z) denotes the Euler gamma-
function, then

(2.1) log Γ(z + 1) = 1
2 log(2π) + (z + 1
2
 ) log(z) − z + 1
12z + O ( 1
z3
 ) .

This holds uniformly in the region of the complex plane where ℜ(z) > 1. This follows readily
from the m = 2 case of
(see [2])

log Γ(z+1) = 1
2 log(2π)+
(z + 1
2
 ) log(z)−z+
 m∑

j=1
 B2j
(2j − 1)(2j)z2j−1 − 1
2m
 ∫ ∞

0
 B2m(x − [x])
(x + z)2m dx.

Also note that since
 N (t) = ∣
∣
∣
∣
{
(n, m) ∈ N2 : t = ( n
m
 )}∣
∣
∣
∣ ,

we have by the symmetry of Pascal’s triangle that

(2.2) N (t) ≤ 2 ∣
∣
∣
∣
{
(n, m) ∈ N2 : t = ( n
m
 ) , 2m ≤ n}∣
∣
∣
∣ .

Lemma 2.1. If F (x) : R → R is an inﬁnitely diﬀerentiable function and if F (x) = 0 for
x = x1, x2, ..., xn+1 (where x1 < x2 < ... < xn+1), then F (n)(y) = 0 for some y ∈ (x1, xn+1).

Proof of Lemma 2.1. We proceed by induction on n. The case of n = 1 is Rolle’s Theorem.
Given the statement of Lemma 2.1 for n − 1, if there exists such an F with n + 1 zeroes,
x1 < x2 < ... < xn+1, then by Rolle’s theorem, there exist points yi ∈ (xi, xi+1) (1 ≤ i ≤ n)
so that F ′(yi) = 0. Then since F ′ has at least n roots, by the induction hypothesis there
exists a y with x1 < y1 < y < yn < xn+1, and F (n)(y) = (F ′)
(n−1)(y) = 0. □

If we let F (x) equal f (x) − p(x) where p(x) is a degree n polynomial, we get that

Corollary 2.1. If f (x) is an inﬁnitely diﬀerentiable function and if p(x) is a polynomial of
degree n so that f (x) = p(x) for x = x1, x2, ..., xn+1 where x1 < x2 < ... < xn+1, then there
exists a y ∈ (x1, xn+1) so that f (n)(y) = p(n)(y).

3. approximation of the terms in binomial coefficients equal to t

Suppose that for n ≥ 2m ( n
m
 ) = t.

BINOMIAL REPRESENTATIONS 3

We can take logs of both sides, and then we have by (2.1) that

log t + log(m!) =

log(n!) − log((n − m)!)

= (n + 1
2
 ) log(n) − n + 1
12n − (n − m + 1
2
 ) log(n − m) + (n − m) − 1
12(n − m) + O ( 1
n3
 )

= m log(n) − (n − m + 1
2
 ) log (1 − m
n
 ) − m + O ( m
n2
 )

= m log(n) + (n − m + 1
2
 ) ( m
n + m
2

2n2
 ) − m + O ( m
3

n2
 )

= m log(n) + m
n
 ( −m + 1
2
 ) + O ( m
3

n2
 )

= m log(n − (m − 1)/2) + O ( m3

n2
 ) .

Hence we have that
 log(n − (m − 1)/2) = log t + log(m!)
m + O ( m
2

n2
 ) .

So,
 n = exp ( log t + log(m!)
m
 ) (
1 + O ( m2

n2
 )) + m − 1
2

= exp ( log t + log(m!)
m
 ) + m − 1
2 + O ( m2

n
 ) .(3.1)

Notice that if we deﬁne ( n
m
 ) = Γ(n + 1)
Γ(m + 1)Γ(n − m + 1)

we can use this to deﬁne an analytic function f (z) by

(3.2) ( f (z)
z
 ) = t

that satisﬁes
 f (z) = exp ( log t + log Γ(z + 1)
z
 ) + z − 1
2 + O ( z2

f (z)
 )

uniformly, so long as |f (z)| > |2z|. This will hold when
∣
∣
∣
∣exp ( log t + log Γ(z + 1)
z
 )∣
∣
∣
∣ > |6z|.

4 DANIEL KANE

By (2.1), this holds when ℜ(z) > 1 and
∣
∣
∣
∣exp ( log t
z
 )∣
∣
∣
∣ > C,

for some constant C. This clearly holds if |ℑ(log z)| < π/4 and if |z| < K log t for some
constant K.
Suppose that for log log t > α > 1.2 ( m
α

m
 ) = t.

We have by (3.1) and (2.1) that

m
α = exp ( log t
m
 ) m
e (1 + O(log m/m)) + m − 1
2 + O(m2−α).

So, we get that (α − 1)m log m = log(t) + O(m).

Or that m log m = log t
α − 1 + O(m).

Hence for suﬃciently large t

(3.3) log t
log log t(α − 1) < m < ( log t
log log t(α − 1)
 ) (
1 + 1
log log t
 ) .

4. Approximations of the derivatives of f (z).

We wish to ﬁnd bounds for 1
k! dk

dxk f (x)

where k ≥ 2 is an integer and for f (x) as deﬁned in (3.2) and x real, less than K log t/2,
and more than 2. Notice that as a complex analytic function,

z2

f (z) = O (z exp ( − log t
z
 )) .

Hence, by Cauchy’s Integral Formula we have

1
k! dk

dxk x
2

f (x) = ∫

C O (w exp ( − log t
w
 ) (w − x)
−k−1) dw.

BINOMIAL REPRESENTATIONS 5

Here C denotes the contour consisting of the circle of radius x/3 centered at x traversed
once in the counterclockwise direction. Notice that on this contour,

ℜ ( 1
w
 ) ≥ 3
4x .

Therefore, the integral is
 O(x
1−k3
kt−3/4x) = O(x
2−k3
kf (x)
−3/4).

It is clear that dk

dxk x − 1
2 = 0.

Notice that by (2.1) log Γ(z + 1)
z = log z − 1 + O ( log z
z
 )

holds for complex z. This means that, by Cauchy’s Integral Formula

1
k! dk

dxk log Γ(x + 1)
x = (−1)
k+1

kxk + ∫

C O ( log w
w(w − x)k+1
 ) dw,

where C is the circle about x through 1. This is then

(−1)
k+1

kxk + O((log2 x)(x
−k−1)).

Therefore, 1
k! dk

dxk log t + log Γ(x + 1)
x = (−1)
k

xk+1 (log t + O(log2 x + x/k)).

This has the same sign as (−1)
k as long as x < k log t, which will hold in the case we are
considering where x < K log t/2 and k ≥ 1. We now wish to analyze the kth derivative with
respect to x of
 g(x) = exp ( log t + log Γ(x + 1)
x
 ) .

Using our previous result, and expanding a Taylor series we ﬁnd that

g(y) =
 exp ( log t + log Γ(y + 1)
y
 ) =

exp ( log t + log Γ(x + 1)
x
 ) exp(a1(y − x) − a2(y − x)
2 + ... + O((y − x)
k+1))

6 DANIEL KANE

where ai = −1
xk+1 (log t + O(log2 x + x/k)) < 0. This means that the coeﬃcients of the Taylor
series about 0 of g(x − y) are all positive. Therefore, d
k

dyk g(y) has the same sign as (−1)
k.
Furthermore, the absolute values of these coeﬃcients is at least

exp ( log t + log Γ(x + 1)
x
 ) |a1|
k

k! =

(f (x) + O(x)) ( log t + O(x/k)
x2
 )k 1
k! >

f (x) + O(x)
xkk! .

To ﬁnd an upper bound on the absolute value of the kth coeﬃcient, we note that if we write

exp ( log t + log Γ(x + 1)
y
 ) =

exp ( log t + log Γ(x + 1)
x
 ) exp(b1(y − x) − b2(y − x)
2 + ... + O((y − x)
k+1))

then bi and ai will have the same sign, but |ai| < |bi|. Therefore, we know that the kth
coeﬃcient of the Taylor series for g(y) at x is at most
∣
∣
∣
∣ 1
k! dk

dyk exp ( log t + log Γ(x + 1)
y
 )∣
∣
∣
∣y=x .

Using Cauchy’s Integral Formula, we ﬁnd that
∣
∣
∣
∣ 1
k! dk

dxk exp ( c
x
 )∣
∣
∣
∣ = ∣
∣
∣
∣ 1
2πi
 ∫

C exp ( c
w
 ) (w − x)
−k−1dw∣
∣
∣
∣ ,

where C is the contour that traverses the circle about x with radius x
log(x) once counter
clockwise. The right hand side of the preceding equation is at most

exp ( c
x
 (1 + O ( 1
log(x)
 ))) ( x
log(x)
 )−k .

Hence we have that for large x, ∣
∣
∣
∣ 1
k! dk

dxk g(x)
∣
∣
∣
∣ <

exp ( log t + log Γ(x + 1)
x
 )1+2/(log x) x
−k(log x)
k <

f (x)
1+2/ log(x)x
−k(log x)
k.

BINOMIAL REPRESENTATIONS 7

Hence, we have that if f (x)
7/4 > x
23k+1k!,

then we have that

(4.1) 0 < ∣
∣
∣
∣ 1
k! dk

dxk f (x)
∣
∣
∣
∣ < 2f (x)e
2 log f (x)
log x x
−k(log x)
k

5. The Strategy

Let
 A(t) = ∣
∣
∣
∣
{
(n, m) ∈ N2 : t = ( n
m
 ) , 2m < n < m
6/5}∣
∣
∣
∣

B(t) = ∣
∣
∣
∣
{
(n, m) ∈ N2 : t = ( n
m
 ) , m6/5 < n < m
 log log(t)
24 log log log(t) }∣
∣
∣
∣

C(t) = ∣
∣
∣
∣
{
(n, m) ∈ N2 : t = ( n
m
 ) , m
 log log(t)
24 log log log(t) < n
}∣
∣
∣
∣ .

It is clear that

(5.1) N (t) = 2A(t) + 2B(t) + 2C(t) + O(1).

We now have to prove that

A(t), B(t), C(t) ≤ O ( log t · log log log t
(log log t)2
 ) .

6. Bounds on A(t)

It is clear that if 2m < n < m
6/5 and
t = ( n
m
 ) ,

then by (3.3) n < (log(t))
6/5 and from the proof of theorem 3 in [1] (pg. 258) ,

(6.1) A(t) ≤ (log(t))
3/4 = O ( log t · log log log t
(log log t)2
 ) .

8 DANIEL KANE

7. Bounds on B(t)

Let k = log log t
12 log log log t .

Here we shall consider real x so that x
 log log t
24 log log log t > f (x) > x
6/5. Notice that logx f (x) is
a decreasing function of x by (3.3). Notice also that f (x)
7/4x
−2 is also a decreasing function
of x by (3.2). Therefore, in this range, f (x)
7/4x
−2 is minimal when f (x) = x
6/5. In this
case, we have that f (x)
7/4x
−2 is x
1/10, and by (3.3), this is at least

(log t)
1/10(log log t)
−1/10.

Whereas we have that,

3
kk! < exp(k log k + k) < exp ( 1
12 (log log t) (1 + 1
log log log t
 )) < f (x)
7/4x
−2

for all suﬃciently large t.
Additionally, we have by (3.3) that

x < ( 5 log t
log log t
 ) (
1 + 1
log log t
 ) < K log t
2

for suﬃciently large t. Hence for suﬃciently large t, and x in this range, the conditions of
(4.1) are satisﬁed.
Therefore, by (4.1)
 0 < ∣
∣
∣
∣ 1
k! dk

dxk f (x)
∣
∣
∣
∣

<2f (x)e
2 log f (x)
log x x
−k(log x)
k

<2x
k/2e
kx
−k(log x)
k

<2e
kx
−k/2(log x)
k

<2e
k ( log t
k log log t
 )−k/2 (log log t)
k

<2(log t)
−k/2(e log log t)
2k

<(log t)
−(k+1)/3(7.1)

for all suﬃciently large t.
Suppose that m1 < m2 < ... < mk+1 are integers and that f (mi) is also an integer for all
1 ≤ i ≤ k + 1. Then if we deﬁne the polynomial

P (x) =
 k+1∑

i=1
 f (mi) ∏i̸=j
1≤j≤k+1(x − mj)
∏i̸=j
1≤j≤k+1(mi − mj) ,

BINOMIAL REPRESENTATIONS 9

Then P is of degree k, and P (mi) = f (mi) for all 1 ≤ i ≤ k + 1. We also have that

1
k! dk

dxk P (x) =
 k+1∑

i=1
 f (mi)
∏i̸=j
1≤j≤k+1(mi − mj) .

This is an integer multiple of

M =
 

 ∏

1≤i<j≤k+1(mj − mi)





−1
 > (mk+1 − m1)
−k(k+1)/2.

Therefore if 1
k! dk

dxk P (x) ̸= 0,

then

(7.2) ∣
∣
∣
∣ 1
k! dk

dxk P (x)
∣
∣
∣
∣ > (mk+1 − m1)
−k(k+1)/2.

Hence, if f (mi) > m6/5
i and f (mi) < mk/2
i for all i, we have by the corollary to Lemma
2.1, (7.1) and (7.2) that
 (mk+1 − m1)
−k(k+1)/2 < (log t)
−(k+1)/3,

or that
 mk+1 − m1 >(log t)
1/3k

=(log t)
 4 log log log t
log log t

=(log log t)
4.(7.3)

Let m1 < m2 < ... < mB(t) be all of the integers so that for all i, f (mi) is an integer
where m
k/2
i > f (mi) > m6/5
i . It is clear that 0 < m1 < mB(t) < log t. Therefore,

[B(t)/(k+1)]∑

i=1 (m(k+1)i − m(k+1)(i−1)+1) < log(t).

Therefore, by (7.3) [B(t)/(k+1)]∑

i=1 (log log t)
4 < log(t).

Or, [B(t)/(k + 1)] < (log t)(log log t)
−4. Therefore,

(7.4) B(t) < k + (k + 1)(log t)(log log t)
−4 < log t
(log log t)3 = O ( log t · log log log t
(log log t)2
 ) .

10 DANIEL KANE

8. Bounds on C(t)

We have by (3.3) that if f (x) > x
 log log t
24 log log log t that

x = O ( log t · log log log t
(log log t)2
 ) .

Therefore the largest m appearing in an element of

{
(n, m) ∈ N2 : t = ( n
m
 ) , m
 log log(t)
24 log log log(t) < n
}

is
 O ( log t · log log log t
(log log t)2
 ) .

Which implies that

(8.1) C(t) = O ( log t · log log log t
(log log t)2
 ) .

Our result that
 N (t) = O ( log t · log log log t
(log log t)2
 )

now follows from (5.1), (6.1), (7.4) and (8.1).
Remark. This process can be done without the use of complex analysis except for the
possible exception of the bounding of the derivatives of log Γ(x + 1)/x. This is done by

claiming that solutions to t = ( n
m
 ) correspond to points near the curve f (x) = (t · x!)
1/x +

(x − 1)/2. This method requires that there be better bounds on the number of points where
n and m are closer to each other (we would need bounds for solutions where n < m
2),
but this can be provided by looking at the greatest common divisors of products of nearby
sequences of integers.
 References

[1] Abbot, H. L.; Erd¨os, P.; Hanson, D., On the Number of Times an Integer Occurs as a Binomial
Coeﬃcient, Amer. Math. Monthly 81 (1974), 256-261.
[2] Hans Rademacher, Topics in Analytic Number Theory, Springer-Verlag, Berlin-Heidelberg-New
York, 1970.

Daniel Kane, Random Hall, 290 Massachusetts Avenue, Cambridge MA 02139
E-mail address: dankane@mit.edu
