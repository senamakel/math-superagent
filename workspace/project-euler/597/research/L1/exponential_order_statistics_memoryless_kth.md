# Summary — Exponential order statistics and the memoryless property

Source: Timo Koski, "Order statistics for independent exponential variables",
KTH Royal Institute of Technology, course SF2955 (Computer intensive methods).
URL: https://www.math.kth.se/matstat/gru/sf2955/exponorderstats.pdf
Full text is in this same file (the downloader's whole-document conversion).

## What it establishes

For X_1..X_n i.i.d. with density f, the joint density of the order statistics
X_(1)<...<X_(n) is n!·∏ f(y_k) on the ordered region (Theorem 1.1).

Specializing to Exp(1) (Theorem 2.1), the spacings

    Y_1 = X_(1),   Y_i = X_(i) − X_(i−1)  (i=2..n)

are **independent** and exponentially distributed with

    Y_i ∈ Exp( 1/(n+1−i) )   i.e. rate (n+1−i).

This is proved by a Jacobian (change of variables Y = A·X, det A = 1) factor
into a product of independent exponential densities. Equivalently: the waiting
time to the k-th arrival of n i.i.d. exponential clocks is exponential with
rate n+1−k, independent of the earlier waiting times — the memoryless
"clocks" view.

## Why it bears on the Torpids problem

The boats' speeds v_j are i.i.d. Exp(1). The memoryless/order-statistic
structure is exactly what memory.md predicted governs an exact (non-Monte
Carlo, non-enumerative) integration over the speeds: after seeing the smallest
of a set of independent exponentials, the remaining ones are still independent
exponentials with their original rates, so event-by-event (bump vs finish)
conditioning decomposes into products over independent exponential rates
rather than high-dimensional integrals. This is the theoretical route to an
answer whose cost grows with the number of boats' *structure* (n small, 13),
not with any enumerable bound.


Avd. Matematisk statistik

Sf 2955: Computer intensive methods :
ORDER STATISTICS FOR INDEPENDENT EXPONENTIAL
VARIABLES / Timo Koski

1 Order Statistics

Let X1, . . . , Xn be I.I.D. random variables with a continuous distribution.
The order statistic of X1, . . . , Xn is the ordered sample:

X(1) < X(2) < . . . < X(n),

Here X(1) = min (X1, . . . , Xn)

X(n) = max (X1, . . . , Xn)

and X(k) = kth smallest of X1, . . . , Xn .

The variable X(k) is called the kth order variable. The following theorem has
been proved in, e.g., Allan Gut: An Intermediate Course in Probability. 2nd
Ed., Springer Verlag, Dordrecht e.t.c., 2009, ch. 4.3., theorem 3.1..

Theorem 1.1 Assume that X1, . . . , Xn are I.I.D. random variables with the
density f . The joint density of the order statistic is

fX(1),X(2),...,X(n) (y1, . . . , yn) = { n! ∏n
k=1 f (yk) if y1 < y2 < . . . < yn,
0 elsewhere. (1.1)

1

2 Exponential Order Variables

Let X1, . . . , Xn be I.I.D. random variables with distribution Exp(θ). Thus
the density function of each Xi is

f (x; θ) = { 1
θ e
−x/θ if x ≥ 0
0 if x < 0. (2.2)

We are interested in the diﬀerences of the order variables

X(1), X(i) − X(i−1), i = 2, . . . , n.

Note that we may consider X(1) = X(1) − X(0), if X(0) = 0. We shall next
show the following theorem.

Theorem 2.1 Assume that X1, . . . , Xn are I.I.D. random variables under
Exp(1). Then

(a)
 X(1) ∈ Exp ( 1
n
) , X(i) − X(i−1) ∈ Exp ( 1
n + 1 − i
) ,

(b) X(1), X(i) −X(i−1) for i = 2, . . . , n, are n independent random variables.

Proof: We deﬁne Yi for i = 1, . . . , n by

Y1 = X(1), Yi = X(i) − X(i−1).

Then we introduce
 A =
 







 1 0 0 . . . 0 0
−1 1 0 . . . 0 0
0 −1 1 . . . 0 0
... ... ... . . . ... ...
0 0 0 . . . −1 1
 






 . (2.3)

so that if
 Y =
 







 Y1
Y2
Y3
...
Yn
 






 , X =
 







 X(1)
X(2)
X(3)
...
X(n)
 






 ,

2

we have Y = AX.

It is clear that the inverse matrix A−1 exists, because we can uniquely ﬁnd
X from Y by X(1) = Y1, X(i) = Yi + Yi−1 + . . . + Y1.

We write these lastmentioned equalities in matrix form by

X = A−1Y.

Then we have the well known change of variable formula (se Gut work cited
chap I)
 fY (y) = fX (A−1y) 1
| det A|. (2.4)

But now we evoke (1.1) to get

fX (
A−1y) = n!f (y1) f (y1 + y2) · · · f (y1 + y2 + . . . + yn) , (2.5)

since y1 < y1 + y2 < . . . < y1 + y2 + . . . + yn. As f (x) = e
−x, we get

f (y1) f (y1 + y2) · · · f (y1 + y2 + . . . + yn) = e
−y1e
−(y1+y2) · · · e
−(y1+y2+...+yn)

and rearrange and use y1 = x(1) and yi = x(i) − x(i−1),

= e
−ny1e
−(n−1)y2 · · · e
−2yn−1e
−yn

= e
−nx(1)e
−(n−1)(x(2)−x(1)) · · · e
−(x(n)−x(n−1)).

Hence, if we insert the last result in (2.4) and distribute the factors in n! =
n(n − 1) · · · 3 · 2 · 1 into the product of exponentials we get

fY (y) = ne
−nx(1)(n − 1)e
−(n−1)(x(2)−x(1)) · · · e
−(x(n)−x(n−1)) 1
| det A| (2.6)

Since A in (2.3) is a triangular matrix, its determinant equals the product of
its diagonal terms, c.f. L. R˚ade and B. Westergren: Mathematics Handbook
for Science and Engineering, Studneetlitteratur, Lund, 2009, p. 93. Hence
from (2.3) we get det A = 1. In other words, we have obtained

fX(1),X(2)−X(1),...,X(n)−X(n−1) (x(1), x(2) − x(1), . . . , x(n) − x(n))

3

= ne
−nx(1)(n − 1)e
−(n−1)(x(2)−x(1)) · · · 2e
−2(x(n−1)−x(n−2))e
−(x(n)−x(n−1)). (2.7)

But, checking against (2.2), ne
−nx(1) is the probabilty density of Exp ( 1
n )
, (n−
1)e
−(n−1)(x(2)−x(1)) is nothing but the probability density of Exp ( 1
n−1)
, and so
on, the generic factor in the product in (2.7) being (n+1−i)e
−(n+1−i)(x(i)−x(i−1)),
which is the density of Exp ( 1
n+1−i )
.
Hence we have that the product in (2.7) is a product of the respective
probability densities for the variables X(1) ∈ Exp ( 1
n ) and for X(i) − X(i−1) ∈
Exp ( 1
n+1−i ). Thus we have established the cases (a) and (b) in the theorem
as claimed.

*[excerpt ends; 456 characters not shown — see `research/exponential_order_statistics_memoryless_kth.full.md`]*
