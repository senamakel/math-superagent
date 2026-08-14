<!-- source: https://web.maths.unsw.edu.au/~mikeh/webpapers/paper21.pdf | converted from PDF -->

A simple proof of Jacobi’s two-square theorem

1. In a recent note, John A. Ewell [1] derives Fermat’s two-square theorem:

A prime p = 4n + 1 is the sum of two squares

from the triple-product identity.

I have observed that from the triple-product identity one can obtain the stronger
result due to Jacobi, namely:

THEOREM 1. The number r2(n) of representations of the positive integer n as

a sum of two squares is given by

r2(n) = 4(d1(n) − d3(n)),

where
 di(n) = ∑

d|n, d≡i (mod 4) 1.

2. The triple-product identity is

(1)
 ∏

n≥1
(1 + ax
2n−1)(1 + a
−1x
2n−1)(1 − x2n) =
 ∞∑

−∞ a
nx
n2,

and this holds for each pair of complex numbera a, x with a ̸= 0 and |x| < 1.

Put −a
2x for a, then x for x
2, multiply by a and we obtain the identity, invariant

Typeset by AMS-TEX
1

2

under a → −a
−1,

(2)
 (a − a
−1) ∏

n≥1
(1 − a
2xn)(1 − a
−2xn)(1 − x
n)

=
 ∞∑

−∞(−1)
na
2n+1x
(n2+n)/2

=
 ∞∑

−∞ a
4n+1x2n2+n −
 ∞∑

−∞ a
4n−1x
2n2−n

= a ∏

n≥1
(1 + a
4x4n−1)(1 + a
−4x
4n−3)(1 − x4n)

− a
−1 ∏

n≥1
(1 + a
4x
4n−3)(1 + a
−4x
4n−1)(1 − x4n).

Diﬀerentiate (2) with respect to a, put a = 1, divide by 2, and we ﬁnd

(3) ∏

n≥1
(1 − xn)
3 = ∏

n≥1
(1 + x4n−3)(1 + x
4n−1)(1 − x4n)

×
 


1 − 4 ∑

n≥1
 ( x4n−3

1 + x4n−3 − x4n−1

1 + x4n−1
 )


 .

[The derivative of the inﬁnite product of the left of (2) is unimportant, since it
vanishes on substituting a = 1, while the derivatives of the inﬁnite products on
the right of (2) are found from



 ∏

n≥1 un



′
 =
 

 ∏

n≥1 un


 ∑

n≥1
 u′
n
un .]

Divide (3) by
∏

n≥1
(1 + x
n)
2(1 − x
n) = ∏

n≥1
(1 + xn)(1 − x2n)
 3

= ∏

n≥1
(1 + x2n−1)(1 + x2n)(1 − x2n)

= ∏

n≥1
(1 + x2n−1)(1 − x4n)

= ∏

n≥1
(1 + x4n−3)(1 + x4n−1)(1 − x4n),

and we have

(4)
 ∏

n≥1
 ( 1 − xn

1 + xn
 )2 = 1 − 4 ∑

n≥1
 ( x
4n−3

1 + x4n−3 − x
4n−1

1 + x4n−1
 ) .

Now, ∏

n≥1
 ( 1 − x
n

1 + xn
 ) = ∏

n≥1
 (1 − x2n−1)(1 − x
2n)
(1 + xn)

= ∏

n≥1
(1 − x2n−1)(1 − xn)

= ∏

n≥1
(1 − x2n−1)(1 − x2n−1)(1 − x2n)

=
 ∞∑

−∞(−1)
nx
n2,

so (4) is

(5) ( ∞∑

−∞(−1)
nx
n2)2 = 1 − 4 ∑

n≥1
 ( x4n−3

1 + x4n−3 − x4n−1

1 + x4n−1
 ) .

Put −x for x, and we obtain

(6) ( ∞∑

−∞ x
n2)2 = 1 + 4 ∑

n≥1
 ( x
4n−3

1 − x4n−3 − x4n−1

1 − x4n−1
 ) ,

4

from which Theorem 1 follows immediately [2].

References

1. John A. Ewell, A simple proof of Fermat’s two-square theorem, this MONTHLY,
90 (1983) 635-637.

2. G. H. Hardy and E. M. Wright, An Introduction to the Theory of Numbers,
4th ed., Clarendon Press, Oxford, 1960, p. 258.
