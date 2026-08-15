<!-- source: https://pi.math.cornell.edu/~gautam/ContinuedFractions.pdf | converted from PDF -->

Continued Fractions

Notes for a short course at the Ithaca High School Senior Math Seminar

Gautam Gopal Krishnan
Cornell University

August 22, 2016

1

Contents

1 Introduction 4
1.1 Euclid’s GCD algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.2 Pictorial Description . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
1.3 Deﬁnitions . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.3.1 Simple Continued Fraction . . . . . . . . . . . . . . . . . . . . . . . . 6
1.3.2 Convergents . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7

2 Properties of Continued Fractions 7
2.1 Finite Continued Fractions . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.1.1 Rational Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
2.1.2 Inverting a Fraction . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.2 Multiple Continued Fractions . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.3 Relations between convergents . . . . . . . . . . . . . . . . . . . . . . . . . . 9
2.4 Uniqueness of Continued Fractions . . . . . . . . . . . . . . . . . . . . . . . . 11

3 Computing Continued Fractions 12
3.1 Continued Fraction Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.2 Decimal expansion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
3.3 Converting from Continued Fractions . . . . . . . . . . . . . . . . . . . . . . . 14

4 Properties of Convergents 15
4.1 Monotone Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
4.2 Best Approximations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 16
4.3 Geometric Interpretation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21

5 Quadratic Equations 24
5.1 Examples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
5.2 Periodic Continued Fractions . . . . . . . . . . . . . . . . . . . . . . . . . . . 25
5.3 Fibonacci Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26
5.4 Pell Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27

6 Other Simple Continued Fractions 27
6.1 Negative numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
6.2 Subtraction in Continued Fractions . . . . . . . . . . . . . . . . . . . . . . . . 29
6.3 Diﬃculties with negative terms . . . . . . . . . . . . . . . . . . . . . . . . . . 30
6.4 General Continued Fraction . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30

7 Irrational Numbers 32
7.1 Deﬁnition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
7.2 Properties . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
7.3 Equivalent Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34

8 Appendix 36
8.1 Special constants . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
8.2 Applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 37

2

9 Project Ideas 38
9.1 Cantor Set . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
9.2 Pell’s equation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 38
9.3 Empty parallelogram theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
9.4 Markov triples . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
9.5 Calendars . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40

3

1 Introduction

Continued Fractions are important in many branches of mathematics. They arise naturally in
long division and in the theory of approximation to real numbers by rationals. These objects
that are related to number theory help us ﬁnd good approximations for real life constants.

1.1 Euclid’s GCD algorithm

Given two positive integers, this algorithm computes the greatest common divisor (gcd) of
the two numbers.

Algorithm: Let the two positive integers be denoted by a and b.

1. If a < b, swap a and b.

2. Divide a by b and ﬁnd remainder r. If r = 0, then the gcd is b.

3. If r ̸= 0, then set a = b, b = r and go back to step 1.

This algorithm terminates and we end up ﬁnding the gcd of the two numbers we started with.

Example:
Take a = 43, b = 19.
 43 = 2 × 19 + 5

19 = 3 × 5 + 4

5 = 1 × 4 + 1

4 = 4 × 1 + 0

Hence, by Euclid’s algorithm, the gcd of 43 and 19 is 1.

Observe that the quotient at each step of the algorithm has been highlighted. Using these
numbers we can present the fraction 43
19 in the following manner:

43
19 = 2 + 1

3 + 1

1 + 1
4
In general, it is true that given two positive integers, we can write the fraction in the above
format by using the successive quotients obtained from Euclid’s algorithm.

1.2 Pictorial Description

Lets look at the same example in a pictorial manner.
Consider a rectangle whose length is 43 units and whose width is 19 units.

4

43
 19

Divide it into squares of side length 19 units (coloured in blue) as shown:

43
 19

We are left with a smaller rectangle of length 5 units and width 19 units (in red). Di-
vide it further into squares of side length 5 units (in green).

43
 19

This leaves us with a rectangular strip of length 5 units and width 4 units (in red). We
continue this process of dividing the rectangle into squares of maximum possible side length.
The number of squares in each step gives us precisely the successive quotients from the pre-
vious section.
 5

43
 19

2 (blue) squares of sidelength 19 units. 3 (green) squares of side length 5 units. 1 (yel-
low) square of side length 4 units. 4 (black) squares of side length 1 unit.
Thus, 43
19 = 2 + 1

3 + 1

1 + 1
4

1.3 Deﬁnitions

1.3.1 Simple Continued Fraction

Deﬁnition 1.1. A Simple Continued Fraction is an expression of the form

a0 + 1

a1 + 1

a2 + 1
a3 + ...
where ai are non-negative integers, for i > 0 and a0 can be any integer.

The above expression is cumbrous to write and is usually written in one of these two forms:

a0 + 1
a1+ 1
a2+ 1
a3+

or using the list notation
 [a0, a1, a2, a3, ...]

to mean the same thing as the continued fraction above.

Example: 43
19 = [2, 3, 1, 4]
In this notation, we have
 [a0] = a0
1

[a0, a1] = a0 + 1
a1 = a0a1 + 1
a1

[a0, a1, a2, ..., an] = a0 + 1
[a1, a2, ..., an] = [a0, [a1, a2, ..., an]]

6

More generally, we have

[a0, a1, a2, ..., an] = [a0, a1, ...am−1, [am, am+1, ..., an]], for 1 ≤ m ≤ n

1.3.2 Convergents

Deﬁnition 1.2. We call [a0, ..., am] (for 0 ≤ m ≤ n) the mth convergent to [a0, ..., an].

In our example, the convergents are
 2 = 2
1

2 + 1
3 = 7
3

2 + 1

3 + 1
1
 = 9
4

2 + 1

3 + 1

1 + 1
4
 = 43
19

2 Properties of Continued Fractions

2.1 Finite Continued Fractions

2.1.1 Rational Numbers

Theorem 2.1. Every rational number has a simple continued fraction expansion which is
ﬁnite and every ﬁnite simple continued fraction expansion is a rational number.

Proof. Suppose we start with a rational number, then Euclid’s algorithm terminates in ﬁnitely
many steps. This is because the successive reminders are strictly decreasing as they have to
be less than the respective quotients. By construction, the successive quotients in Euclid’s
algorithm precisely gives us a simple continued fraction expansion for the rational number
we started with.
Conversely, if we have a simple ﬁnite continued fraction expansion [a0, a1, ..., an], then we
can inductively see that [a0, a1, ..., an] = [a0, [a1, ..., an]] = (a0([a1, ..., an]) + 1)/[a1, ..., an].
Hence, [a0, ..., an] is a rational number.
 Q.E.D.

This theorem now says that we can continue working with ﬁnite simple continued frac-
tions as long as we are only working with rational numbers. Henceforth, we will work with
ﬁnite simple continued fractions until section 7 where we will deal with irrational numbers.

Exercise 2.2. (i) Find a simple continued fraction expansion of 13
8 .

(ii) Compute the gcd of (13, 8) using Euclid’s algorithm.
(iii) What are its convergents?
(iv) Write the continued fraction from part (i) in list notation.

7

2.1.2 Inverting a Fraction

Given a non-zero rational number, we simply interchange the numerator and denominator to
get its reciprocal.

For example, the reciprocal of 43
19 is 19
43.

Now we describe how to ﬁnd the reciprocal of a rational number if it is described as a
simple continued fraction:

1. If the simple continued fraction has a 0 as its ﬁrst number, then remove the 0.

2. If the simple continued fraction does not have 0 as its ﬁrst number, then shift all the
numbers to the right and place 0 as the ﬁrst entry.

Examples:
43
19 = [2, 3, 1, 4] =⇒ 19
43 = [0, 2, 3, 1, 4]

3
7 = [0, 2, 3] =⇒ 7
3 = [2, 3]

2.2 Multiple Continued Fractions

Given a rational number, we have seen one way of constructing a simple continued fraction
(namely by Euclid’s algorithm). But is it the only way of getting a simple continued fraction?
In this section and the next few sections we will see that there is essentially a unique way to
write a rational number as a simple continued fraction.

Theorem 2.3. If x is representable by a simple continued fraction with an odd (even) number
of convergents, it is also representable by one with an even (odd) number.

Proof. If an ≥ 2,
 [a0, a1, ..., an] = [a0, a1, ..., an − 1, 1]

If an = 1,
 [a0, a1, ..., an−1, 1] = [a0, a1, ..., an−1 + 1], [1] = [0, 1]
 Q.E.D.

Thus, the proof of this theorem says that there are atleast 2 ways of writing a simple
continued fraction for a rational number.

1. A simple continued fraction ending with some m > 1 i.e. [...., m].

2. A simple continued fraction ending with 1 i.e. replace the ﬁnal m by (m − 1) + 1/1 to
get [...., m − 1, 1].

Examples:
 [1, 2, 3, 4, 5] = [1, 2, 3, 4, 4, 1]
3
2 = 1 + 1
2 = 1 + 1

1 + 1
1

8

2.3 Relations between convergents

In this section, we see some properties of the simple continued fractions in terms of the
numerators and denominators appearing in the convergents.

Theorem 2.4. If pn and qn are deﬁned by
p0 = a0, p1 = a1a0 + 1, pn = anpn−1 + pn−2 for 2 ≤ n
q0 = 1, q1 = a1, qn = anqn−1 + qn−2 for 2 ≤ n,
then
 [a0, a1, ..., an] = pn
qn.

Proof. The proof proceeds by induction. The base cases are seen to be true by the assump-
tions given for n = 0, n = 1. Let us assume the statement to be true for some m. Then

[a0, a1, ...am−1, am] = pm
qm = ampm−1 + pm−2
amqm−1 + qm−2
Hence, we get
 [a0, a1, ...am−1, am, am+1] = [a0, a1, ..., am−1, am + 1
am+1]

= (am + 1
am+1)pm−1 + pm−2

(am + 1
am+1)qm−1 + qm−2

= am+1(ampm−1 + pm−2) + pm−1
am+1(amqm−1 + qm−2) + qm−1

= am+1pm + pm−1
am+1qm + qm−1

= pm+1
qm+1

By the principle of mathematical induction, pn and qn are indeed deﬁned by the recursive
relation stated in the theorem.
 Q.E.D.

It follows that the nth convergent is

pn
qn = anpn−1 + pn−2
anqn−1 + qn−2
Theorem 2.5. The numbers pn and qn satisfy

pnqn−1 − pn−1qn = (−1)n−1

Proof. From the previous theorem, we have

pnqn−1 − pn−1qn = (anpn−1 + pn−2)qn−1 − pn−1(anqn−1 + qn−2)

= −(pn−1qn−2 − pn−2qn−1)

Repeating this step with n − 1, n − 2, ..., 2 in place of n, gives us

9

pnqn−1 − pn−1qn = (−1)n−1(p1q0 − p0q1) = (−1)
n−1(1) = (−1)
n−1
 Q.E.D.

Example:
 225
157 = 1 + 1

2 + 1

3 + 1

4 + 1
5
Its convergents are
 1 = 1
1

1 + 1
2 = 3
2

1 + 1

2 + 1
3
 = 10
7

1 + 1

2 + 1

3 + 1
4
 = 43
30

1 + 1

2 + 1

3 + 1

4 + 1
5
 = 225
157

i.e. 1
1
, 3
2, 10
7 , 43
30, 225
157
The numerators and denominators of these convergents do satisfy

(3)(1) − (1)(2) = (−1)
1−1 = 1

(10)(2) − (3)(7) = (−1)
2−1 = −1

(43)(7) − (10)(30) = (−1)
3−1 = 1

(225)(30) − (43)(157) = (−1)
4−1 = −1

Deﬁnition 2.6. We call
 a
′
m = [am, am+1, ..., an]

the mth complete quotient of the continued fraction

[a0, a1, ..., an]

Let x = [a0, a1, ..., an]. Then

x = a
′
0 = a
′
1a0 + 1
a′
1 = a
′
npn−1 + pn−2
a′
nqn−1 + qn−2

10

This follows by the exact same steps as the proof of Theorem 2.4.

Theorem 2.7. am = [a
′
m], the integral part of a
′
m, except that an−1 = [an−1] − 1 when
an = 1.

Proof. If n = 0, then a0 = a
′
0 = [a
′
0]. If n > 0, then

a
′
m = am + 1
a′
m+1 for (0 ≤ m ≤ n − 1).

Now
 a
′
m+1 > 1 for (0 ≤ m ≤ n − 1)

except that a
′
m+1 = 1 when m = n − 1 and an = 1.
This is because a1, a2, ..., an are all non-negative integers and inductively one can see that
the above statement is true.
Hence
 am < a
′
m < am + 1 for (0 ≤ m ≤ n − 1)

and
 am = [a′
m] for (0 ≤ m ≤ n − 1)

except in the case speciﬁed. And in any case

an = a′
n = [a′
n]
 Q.E.D.

2.4 Uniqueness of Continued Fractions

In this section we use all the properties seen in the above theorems to show that under some
minor conditions, every rational number has a unique ﬁnite simple continued fraction.

Theorem 2.8. If two simple continued fractions

[a0, a1, ..., an], [b0, b1, ..., bN ]

have the same value x, and an > 1, bN > 1, then n = N and the fractions are identical.

Proof. By Theorem 2.7, a0 = b0 = integral part of x. Let us assume that the ﬁrst m terms
in the continued fractions are identical.Then

x = [a0, a1, ..., am−1, a
′
m] = [b0, b1, ..., bm−1, b
′
m]

If m = 1, then
 a0 + 1
a′
1 = b0 + 1
b′
1
which implies a
′
1 = b′
1 and by Theorem 2.7, a1 = b1. If m > 1, then

a
′
mpm−1 + pm−2
a′
mqm−1 + qm−2 = b
′
mpm−1 + pm−2
b′
mqm−1 + qm−2

(a
′
m − b′
m)(pm−1qm − 2 − pm−2qm−1) = 0. But (pm−1qm − 2 − pm−2qm−1) = (−1)
m, by
Theorem 2.5 and so a
′
m = b′
m. By Theorem 2.7, am = bm.
Suppose now, n ≤ N , then we have shown that am = bm∀m ≤ n. If N > n, then

11

pn
qn = [a0, a1, ..., an] = [a0, a1, ..., an, bn+1, bn+2, ..., bN ] = b′
n+1pn + pn−1
b′
n+1qn + qn−1
=⇒ pnqn−1 − pn−1qn = 0

which contradicts Theorem 2.5. Hence, n = N and the fractions are identical.
 Q.E.D.

Theorem 2.3 and Theorem 2.8 together tell us that there are exactly two ways of
writing any rational number as a ﬁnite simple continued fraction. They also tell
us how to convert one simple continued fraction to the other. Since we already know how
to obtain a simple continued fraction by using the Euclid’s algorithm, this is essentially the
only way to obtain a simple continued fraction.
Examples:
 [7] = [6, 1]

[1, 2, 2, 2] = [1, 2, 2, 1, 1]

[0, 1, 2, 3] = [0, 1, 2, 2, 1]

[1, 1, 1, 1, 1] = [1, 1, 1, 2]

[1] = [0, 1]

3 Computing Continued Fractions

We would like to see diﬀerent ways of computing ﬁnite simple continued fractions. We know
that these correspond precisely to rational numbers. In the next few sections we see diﬀerent
ways of representing rational numbers and how to go from one form to another.

3.1 Continued Fraction Algorithm

This algorithm is very similar to Euclid’s algorithm and works even for irrational numbers.
In case we start with an irrational number, the algorithm won’t terminate but it will give us
a way of writing the number as an inﬁnite simple continued fraction.

Algorithm: Let x be a real number. Let x0 = x.

1. Set am to be the integral part of xm.

2. Set ξm to be xm − am.

3. If ξm ̸= 0, set 1
ξm as xm+1 and go back to step 1 to compute am+1.

4. If ξm = 0, terminate this algorithm.

The non-zero ξm obtained by this algorithm gives us the (m + 1)th complete quotients a
′
m+1.
During each iteration, observe that 0 ≤ ξm < 1 and hence am+1 ≥ 1. Also, by construction
we have
 x = [a0, a
′
1] = [a0, a1, a
′
2] = ...

12

where a0, a1, a2, ... are integers with a1 > 0, a2 > 0, ...
Hence this indeed gives us the simple continued fraction for x.

The system of equations
 x = a0 + ξ0
1
ξ0 = a
′
1 = a1 + ξ1

1
ξ1 = a
′
2 = a2 + ξ2
...

is known as the continued fraction algorithm.

This algorithm also gives us a way of quickly computing the simple continued fraction by
using a calculator. However, some rounding errors will creep in when calculating 1/ξm. Once
these intermediate fractions become close to 0, we stop the calculations and that would give
us a good approxiamtion of the number we started with.

Lets see how this works with the help of an example.
Example:
Let x = 2.875
Its integral part is 2 and so the continued fraction starts as [2, ...].
2.875 − 2 = 0.875
Calculate 1/0.875 using a calculator to get 1.14285714285714. Its integral part is 1.
So we now have [2, 1, ...].
1.14285714285714−1 = 0.14285714285714. Calculate 1/0.14285714285714 to get 7.00000000000014
whose integral part is 7.
The continued fraction is now [2, 1, 7, ...].
7.00000000000014 − 7 = 0.00000000000014 which is “almost” 0.
So, we terminate the algorithm here to get [2, 1, 7]. In fact, it is indeed true that

2.875 = 2 + 1

1 + 1
7

3.2 Decimal expansion

If a rational number is given as a fraction, then we know how to use Euclid’s algorithm to get
a simple continued fraction. If the number is given in terms of its decimal expansion, then
the previous algorithm gives us a way of getting a simple continued fraction. Any rational
number has a terminating or eventually repeating (periodic) decimal expansion.
If we have a number with terminating decimal expansion, then we can always represent it as
a proper fraction by using a denominator which is a big enough power of 10. The power of
10 required is just the number of digits to the right of the decimal point.
For instance,
 1.2 is 12/10
2.875 is 2875/1000
0.00075 is 75/100000

Since all such decimal expansions can be converted to fractions, we can now use Euclid’s
algorithm to express them as continued fractions.

13

Example:
2.875 = 2875/1000. Using Euclid’s algorithm for (2875, 1000) gives us

2875 = 2 × 1000 + 875

1000 = 1 × 875 + 125

875 = 7 × 125

So, 2.875 = [2, 1, 7]. There is no need to reduce the fraction to lowest terms to use Euclid’s
algorithm as can be seen from the above example.

3.3 Converting from Continued Fractions

Given a ﬁnite simple continued fraction, we would now like to recover the rational number
from it. The natural way to go about it, is to evaluate the continued fraction from the
right-hand end, simplifying each part in turn

[2, 3, 1, 4] = 2 + 1

3 + 1

1 + 1
4
 = 2 + 1

3 + 1
5/4
 = 2 + 1

3 + 4
5
 = 2 + 1
19/5 = 2 + 5
19 = 43
19

i.e. [2, 3, 1, 4] = [2, 3, 1 + 1/4] = [2, 3, 5/4] = [2, 3 + 1/(5/4)] = [2, 19/5] = [2 + 1/(19/5)] =
[43/5]

There is another way to evaluate the simple continued fraction by going from left to right.
Given [a0, a1, a2, ..., ], we can recursively compute its convergents [a0], [a0, a1], [a0, a1, a2], ...
from the previous convergent.
If pm/qm denotes the mth convergent then pm/qm = (ampm−1 + pm−2)/(amqm−1 + qm−2).
This is the content of Theorem 2.4.

Thus, we have

CF a0 a1 a2 a3
Num a0 a1 × a0 + 1 a2 × (a1 × a0 + 1) + a0 a3 × (a2 × (a1 × a0 + 1) + a0) + (a1 × a0 + 1)
Den 1 a1 × 1 + 0 a2 × a1 + 1 a3 × (a2 × a1 + 1) + a1

It is easier to see this in an example.

Example: [1, 1, 1, 1]
 CF 1 1 1 1
Num 1 2 3 5
Den 1 1 2 3

From this table we see that [1, 1, 1, 1] = 5
3
.

Remark: Observe that the convergents in this example are ratios of Fibonacci numbers!
In general it is true that if the list notation of the continued fraction contains only 1s, then
the convergents that appear are ratios of consecutive Fibonacci numbers.

14

4 Properties of Convergents

In this section, we will continue to use the notation that pm is the numerator and qm is the
denominator of the mth convergent to the simple continued fraction [a0, a1, a2, ..., an].

4.1 Monotone Properties

Let x be given by [a0, a1, ..., an] and let xm denote the mth convergent pm/qm. Then we have
the following theorems

Theorem 4.1. The even convergents x2m increase strictly with m, while the odd convergents
x2m+1 decrease strictly.

Proof. By Theorem 2.4 and Theorem 2.5, we get

xm − xm−2 = pm
qm − pm−2
qm−2

= pm
qm − pm−1
qm−1 + pm−1
qm−1 − pm−2
qm−2

= (−1)m−1

qmqm−1 + (−1)m−2

qm−1qm−2

= (−1)
m(qm − qm−2)
qmqm−2qm−1

= (−1)mamqm−1
qmqm−2qm−1

= (−1)mam
qmqm−2

Since am, qm−2, qm are positive integers, this diﬀerence has a sign (−1)m. Hence, the even
convergents increase strictly while the odd convergents decrease strictly.
 Q.E.D.

Remark: Thus, we have this picture:

x0 < x2 < x4 < x6 < x8 < ...
x1 > x3 > x5 > x7 > x9 > ...

Theorem 4.2. Every odd convergent is greater than any even convergent.

Proof. This proof follows by a similar argument as the previous theorem. Theorem 2.5 tells
us that xm − xm−1 has the sign (−1)m−1. So every odd convergent is greater than its
predecessor and its successor. i.e.

x2m+1 > x2m and x2m+1 > x2m+2 for all m

If there is some r such that x2m+1 ≤ x2r, then by Theorem 4.1 either x2m+1 ≤ x2r < x2m or
x2r+1 < x2m+1 ≤ x2r depending on whether r < m or r > m. In either case this contradicts
the fact that every odd convergent is greater than its predecessor.
 Q.E.D.

15

Remark:
If you want to think in terms of examples, then all we are saying in the above proof is that
if we want to show x3 > x8 then we simply use the chain of inequalities x3 > x5 > x7 > x8.
Similarly, if we want to show x7 > x2, we use the chain of inequalities x7 > x6 > x4 > x2.

Theorem 4.3. The value of the continued fraction is greater than that of any of its even
convergents and less than that of any of its odd convergents(except that it is equal to the last
convergent).

Proof. The value of the continued fraction is the last convergent i.e the nth convergent. If n
is even, then it is the greatest of the even convergents by Theorem 4.1 and less than all odd
convergents by Theorem 4.2. Simliarly, if n is odd, then it is the least of the odd convergents
by Theorem 4.1 and greater than all even convergents by Theorem 4.2. Hence, the value of
the convergent is between the even and odd convergents.
 Q.E.D.

Looking back at some of the examples we have seen, we can quickly check the validity of
these theorems in those speciﬁc examples. In doing so, we also begin to get an idea of why
convergents to a continued fraction are called so. At this point, it would be instructive to go
back to the examples and plot all their convergents on the real line to develop a geometric
picture of what is happening (i.e. the convergents to x must oscillate around x ).

4.2 Best Approximations

In this section we see how close the convergents are to the number that we started with. The
next few theorems try to answer the following question:

What is the best approximation to a given number with small denominators?

For instance, Archimedes found that π is approximately 22
7 . This is a simple and good
approximation whose error is less that 0.002. For all fractions with denominators less than
10, this is the fraction with the least error. More generally, it is possible to ﬁnd such
approximations for any number.

Deﬁnition 4.4. The rational number p/q is the best approximation to a real number x if
the distance from p/q to x on the real line is less than the distance from any other rational
number to x (with denominator less than or equal to q).

Theorem 4.5. The convergents to a simple continued fraction are in their lowest terms.

Proof. If d divides pm and qm for some m, then d divides pm+1qm − pmqm+1 which is (−1)m

by Theorem 2.5. So, pm and qm cannot have any common divisor other than ±1 which
implies all the convergents are in their lowest terms.
 Q.E.D.

Theorem 4.6. The denominators of the convergents satisfy the following inequalities

qn ≥ n, with strict inequality when n > 3.

Proof. q0 = 1, q1 = a1 ≥ 1. For n ≥ 2,

qn = anqn−1 + qn−2 ≥ qn−1 + 1

16

and inductively we see that qn ≥ n. For n > 3,

qn ≥ qn−1 + qn−2 > qn−1 + 1 ≥ n

and hence qn > n.
 Q.E.D.

Theorem 4.7. Every simple continued fraction can be written as an alternating sum in the
following manner:
[a0, a1, ..., an] = a0 + 1
q1q0 − 1
q2q1 + ... + (−1)n−1 1
qnqn−1

Proof. Observe that for any m, the mth convergent pm
qm can be written as

pm
qm = pm
qm − pm−1
qm−1 + pm−1
qm−1 − pm−2
qm−2 + ... + p1
q1 − p0
q0 + p0
q0
Using Theorem 2.5 and setting m = n gives us the desired result.
 Q.E.D.

Theorem 4.8. For any number x with convergents pm
qm,

∣
∣
∣
∣
∣x − pm
qm
∣
∣
∣
∣
∣ < 1
qm+1qm

Proof. We will sketch the idea of the proof here. There are two way to see why the inequality
holds.
The ﬁrst proof uses the previous theorem. Notice that x can be written as

x = c0 − c1 − c2 − ...

where c0 = a0 and cm = pm−1
qm−1 − pm
qm. These cm become smaller and smaller and x minus the

ﬁrst m terms is less than the value of cm+1. This will imply the inequality. Try to compute
these cm for some explicit example to see why this result is true.
The second proof is purely algebraic and uses complete quotients.

x = a
′
m+1pm + pm−1
a′
m+1qm + qm−1

and so
 x − pm
qm = − pmqm−1 − pm−1qm
qm(a′
m+1qm + qm−1) = (−1)m

qm(a′
m+1qm + qm−1) = (−1)
m

qmq′
m+1

where q′
m = a′
mqm−1 + qm−2. Since am is the integral part of a
′
m, qm+1 < q′
m+1 and this
gives us the desired inequality.
 Q.E.D.

Theorem 4.9. pm
qm is the best approximation to x with denominator ≤ qm.

17

Proof. The even convergents are increasing and the odd convergents are decreasing with x

lying in between them. qm > qm−1 implies that pm−1
qm−1 and pm
qm are two convergents with

denominator less than or equal to qm. Suppose p
q is the best approximation to x with

denominator less than or equal to qm, then it has to lie between pm
qm and pm−1
qm−1.

∣
∣
∣
∣
∣ p
q − pm−1
qm−1
∣
∣
∣
∣
∣ =
 ∣
∣
∣
∣
∣ pqm−1 − qpm−1
qqm−1
 ∣
∣
∣
∣
∣ ≥ 1
qqm−1
∣
∣
∣
∣
∣ p
q − pm−1
qm−1
∣
∣
∣
∣
∣ ≤
 ∣
∣
∣
∣
∣ pm
qm − pm−1
qm−1
∣
∣
∣
∣
∣ = 1
qmqm−1

From these two inequalites we get

1
qqm−1 ≤
 ∣
∣
∣
∣
∣ p
q − pm−1
qm−1
∣
∣
∣
∣
∣ ≤ 1
qmqm−1

but we know that q ≤ qm. Therefore, equality must hold everywhere which implies p
q = pm
qm.

Hence, pm
qm is the best approximation to x with denominator less than or equal to qm.

Q.E.D.

This answers the question that was posed at the beginning of this section! If we want to
ﬁnd best approximations to a given number, then we calculate its simple continued fraction
and look at its convergents. Amongst those, we pick a convergent with a huge denominator
and that would give a very good approximation. If we want to get a good approximation
directly from the list notation of a continued fraction, rather than compute its convergents
then the idea would be to stop evaluating a continued fraction right before a large entry.
i.e. If am is a very big number, then [a0, a1, ..., am−1] will give a very good approximation of
the number. The appendix has some approximations to π using what we have discussed here.

All convergents to x are best approximations to x but these are not all the best approx-
imations! Consider the following example:
Example:
 x = 7
38 = [0, 5, 2, 3]

Convergents: 0
1, 1
5
, 2
11
, 7
38

If we look at all fractions with denominators less than or equal to 28, then 5
27 is the best
approximation to x but it is not one of the convergents.

5
27 = [0, 5, 2, 2]

18

This leads us to the following two questions:
1. What are all the best approximations?
2. How are they related to the convergents?

Lemma 4.10. If b, d > 0, then a
b ≤ c
d =⇒ a
b ≤ a + c
b + d ≤ c
d

Proof. a
b ≤ c
d =⇒ ad − bc ≤ 0 =⇒ ad ≤ bc

ab + ad ≤ ab + bc =⇒ a
b ≤ a + c
b + d

ad + cd ≤ bc + cd =⇒ a + c
b + d ≤ c
d Q.E.D.

Deﬁnition 4.11. A semi-convergent or secondary convergent to x is a number of the
form (pk + rpk+1)/(qk + rqk+1) where pk/qk and pk+1/qk+1 are two consecutive convergents
to x = [a0, a1, a2, ...] and r is an integer between 0 and ak.

Note in particular, that the convergents to x are also semi-convergents.

Theorem 4.12. If x is any real number and a/b is not a semi-convergent to x, then a/b is
not the best approximation to x with denominator less than or equal to b.

Proof. Lets assume for simplicity that a/b < x. Since a/b is not a semi-convergent, it should
lie between two convergents of the form pk/qk and pk+2/qk+2 for some k. Lets say for simplic-
ity that pk/qk < pk+1/qk+1 (a similar proof holds if pk/qk > pk+1/qk+1). Then by Lemma
4.10,
 pk
qk < pk + pk+1
qk + qk+1 < pk + 2pk+1
qk + 2qk+1 < ... < pk + akpk+1
qk + akqk+1 = pk+2
qk+2
Therefore,
 pk + rpk+1
qk + rqk+1 < a
b < pk + (r + 1)pk+1
qk + (r + 1)qk+1 for some 0 ≤ r < ak.

1
b(qk + rqk+1) ≤
 ∣
∣
∣
∣
∣ a
b − pk + rpk+1
qk + rqk+1
 ∣
∣
∣
∣
∣

<
 ∣
∣
∣
∣
∣ pk + (r + 1)pk+1
qk + (r + 1)qk+1 − pk + rpk+1
qk + rqk+1
 ∣
∣
∣
∣
∣

= 1
((r + 1)qk+1 + qk)(rqk+1 + qk)

=⇒ 1
b ≤ 1
qk + (r + 1)qk+1 ≤ 1
qk+2 =⇒ qk+2 ≤ b

This says that a
b is not the best approximation to x since pk+2
qk+2 is closer to x than a
b with

denominator less than b.
An analogous argument holds when a/b > x.

19
 Q.E.D.

This tells us that the only candidates for the best approximations are the semi-convergents.
In fact, there is a precise statement which says which semi-convergents are the best approx-
imations which we will not state here. Roughly speaking, about half the semi-convergents
between pk/qk and pk+2/qk+2 which are closest to pk+2/qk+2 are the best approximations to
x.
Going back to our example, 5/27 is a semi-convergent to 7/38 but not a convergent. All the
best approximations to 7/38 = [0, 5, 2, 3] are [0], [0, 3], [0, 4], [0,5], [0,5,2], [0, 5, 2, 2], [0,5,2,3]
(and the highlighted terms are the convergents).
When talking about best approximations we used the distance between a fraction p/q and
x as a measure of how well it approximated x. However, if the denominator increases, then
we should expect better approximations to have smaller distance from x. To take this into
account, one could consider the product of the denominator and the distance between the
fraction from x as measure of how well it approximates x (i.e. q ∣
∣x − p/q∣
∣ = |qx − p|).

Deﬁnition 4.13. A fraction p/q is a best approximation of the second kind to a real
number x if for every fraction a/b with denominator less than or equal to q, we have |qx − p| <
|bx − a|.

Theorem 4.14. The convergents to a real number x are precisely all the best approximations
of the second kind to x.

Proof. We will only prove part of the theorem here by showing that any fraction which is
not a convergent cannot be a best approximation of the second kind to x.
Let us assume that a/b is a best approximation of the second kind to x and its not a
convergent to x. We’ll further assume that a/b < x and it lies between two convergents
pk/qk and pk+2/qk+2 for some k where pk/qk < pk+1/qk+1 (these assumptions are simply to
make the proof easier to write and the proof can be modiﬁed for all cases).

1
bqk ≤
 ∣
∣
∣
∣
∣ a
b − pk
qk
∣
∣
∣
∣
∣

<
 ∣
∣
∣
∣
∣ pk+1
qk+1 − pk
qk
∣
∣
∣
∣
∣

= 1
qkqk+1

=⇒ 1
bqk < 1
qkqk+1 =⇒ qk+1 < b
 20

And we also have
 |qk+1x − pk+1| = qk+1
 ∣
∣
∣
∣
∣x − pk+1
qk+1
∣
∣
∣
∣
∣

≤ qk+1
 ∣
∣
∣
∣
∣ pk+2
qk+2 − pk+1
qk+1
∣
∣
∣
∣
∣

= 1
qk+2

= b 1
bqk+2

≤ b
 ∣
∣
∣
∣
∣ pk+2
qk+2 − a
b
∣
∣
∣
∣
∣

≤ b
 ∣
∣
∣
∣
∣x − a
b
∣
∣
∣
∣
∣

= |bx − a|

Since pk+1
qk+1 has a denominator less than b and |qk+1x − pk+1| ≤ |bx − a|, a
b cannot be a best

approximation of the second kind to x.
 Q.E.D.

4.3 Geometric Interpretation

Look at the coordinate plane where all points with integer coordinates are marked. That
would give us a lattice on the plane. Fix some α and draw the line y = αx on the coordinate
plane. If α is rational, then it would intersect the lattice in inﬁnitely many points. If α is
irrational, then it will not intersect the lattice at any point other than the origin.

21

For example, lets look at what happens when α is 5
7 = [0, 1, 2, 2].

The line segment joins (0, 0) to (14, 10) and the red points are (0, 0), (1, 1), (3, 2), (7, 5), (8, 6), (10, 7), (14, 10).

The convergents to 5
7 are 0, 1
1, 2
3
, 5
7
.
 22

Simlarly, we can consider the case when α is (1 + √5)
2 . This is called the golden ratio.

The red points are (0, 0), (1, 1), (1, 2), (2, 3), (3, 5), (5, 8), (8, 13). The convergents to (1 + √5)
2

are 1
1, 2
1
, 3
2
, 5
3, 8
5
, 13
8 , ....

Theorem 4.15. The closest points in the lattice to the line y = αx are in one-one corre-
spondence with the convergents to the continued fraction of α. Let these points be labelled as
Am = (qm, pm). The point is above the line, if m is odd, and below otherwise.

Proof. The proof follows from the observation that the distance of a point (b, a) to the line

y = αx is |bα − a|
√1 + α2 which is a constant (
√1 + α2) times the measure of whether a
b is a best

approximation of the second kind to α.
 Q.E.D.

Looking at the two examples where the graph has been drawn, we can see that this is
indeed the case. The convergents to α have been highlighted in both cases.

23

Given just the points on the lattice closest to the line, it is also possible to recover the
continued fraction as described by the following theorem:

Theorem 4.16. Let [a0, a1, ..., an] be the continued fraction for α and let the points Am be
the marked points in the lattice as before. Then am is the integral distance between the points
Am and Am+2.

Here, the integral distance between two points refers to the number of points on the line
segment joining the two points minus 1.
These two theorems give us a geometric way of going back and forth between continued
fractions and approximations.

5 Quadratic Equations

5.1 Examples

Lets start with some quadratic equation and try to naively get a continued fraction for its
roots.
Example:
For instance, lets take
 x2 − 5x − 1 = 0

Instead of computing its roots using the quadratic formula, lets do the following steps:

x2 = 5x + 1
x = 5 + 1/x

Since, we have x appearing on the right hand side, lets make the substitution again to get

x = 5 + 1/x = 5 + 1
5 + 1/x

Does this look familiar? By continuing this process, we seem to get the inﬁnite continued
fraction [5, 5, 5, ...].

Example: Consider
 x2 + x = 1

We try to do something similar to the previous example.

x2 + x = 1
x(x + 1) = 1

x = 1
(1 + x)

x = 1

1 + 1
1 + x

Again, by continuing this process we get [0, 1, 1, 1, ...].

Example:
 24

x2 − 2x = 1
x2 = 2x + 1
x = 2 + 1/x

x = 2 + 1

2 + 1
2 + 1/x

This gives us the continued fraction [2, 2, 2, 2, 2, ...]. This number is called the silver ratio
(analogous to the golden ratio). The golden ratio is the continued fraction [1, 1, 1, 1, 1, ...]
and it has the worst possible approximations by rational numbers since the only numbers
appearing in its continued fraction expansion is 1. In this sense, the silver ratio is the second
worst number to be approximated by rational numbers.
We can use this example to get a continued fraction for the root of the next quadratic ex-
pression.

Example:
 x2 − 2 = 0

Setting, y = x + 1, we get
 (y − 1)2 − 2 = 0
y2 − 2y − 1 = 0
y2 − 2y = 1

From the previous example, we know that y = [2, 2, 2, ...]. So x = √2 = [1, 2, 2, 2, ...].
Given any quadratic equation, we can play around with the equation and see if we can
recursively construct a continued fraction. There seems to be some pattern in all these
examples.

1. The roots of all these quadratic equations can be expressed as an inﬁnite continued
fraction.

2. The numbers that appear in the continued fraction repeat after a while.

This will be formalised in the next section.

5.2 Periodic Continued Fractions

Deﬁnition 5.1. A periodic continued fraction is an inﬁnite continued fraction in which

al = al+k

for a ﬁxed positive k and all l ≥ L.The set of partial quotients

aL, aL+1, ..., aL+k−1

is called the period, and the continued fraction may be written

[a0, a1, ..., aL−1, aL, aL+1, ..., aL+k−1].

Theorem 5.2. A periodic continued fraction is a quadratic surd, i.e. an irrational root of a
quadratic equation with integral coeﬃcients.
 25

Proof. Using the notation set up in the deﬁnition, we have

a
′
L = [aL, aL+1, ..., aL+k−1, aL, aL+1, ...]

= [aL, aL+1, ..., aL+k−1, a
′
L]

= p
′a
′
L + p
′′

q′a′
L + q′′

where p
′′/q′′ and p′/q′ are the last two convergents to [aL, aL+1, ..., aL+k−1].
This gives us the equation
 q′a
′2
L + (q′′ − p
′)a
′
L − p
′′ = 0

We know that
 x = pL−1a′
L + pL−2
qL−1a′
L + qL−2

which gives us
 a
′
L = pL−2 − qL−2x
qL−1x − pL − 1

Substituting this value back in the quadratic equation and clearing the denominators gives
us a quadratic equation in x with integer coeﬃcients.
 Q.E.D.

The converse of the theorem is also true.

Theorem 5.3. The continued fraction which represents a quadratic surd is periodic.

This theorem will not be proved here. A proof of this theorem can be found in the
references. This theorem is sometimes called the Continued Fraction Theorem.

5.3 Fibonacci Numbers

Lets start with this quadratic equation

x2 − x − 1 = 0

and try to do simlar computations like in the examples before.

x2 = x + 1
x = 1 + 1/x

x = 1 + 1
1 + 1/x

This gives us the periodic continued fraction [1, 1, 1, ...]. We saw a truncated version of this
continued fraction while discussing an example for computing the numerators and denomi-
nators explicitly for convergents to a continued fraction.

Directly using the quadratic formula tells us that (1 + √5)/2 is the positive root of this
quadratic equation. This is precisely the golden ratio which we saw as an example when we
looked at a geometric interpretation of convergents.

Deﬁnition 5.4. Fibonacci Sequence is an integral sequence deﬁned by

F0 = 0, F1 = 1, Fn = Fn−1 + Fn−2

26

The ﬁrst few Fibonacci numbers are 1, 1, 2, 3, 5, 8, 13, ...

The closed form expression for the nth Fibonacci number is

Fn = φn − (−φ)
−n
√5

where φ is the golden ratio. Thus we see that continued fractions connects the golden ratio
to the Fibonacci sequence. The convergents to the continued fraction of the golden ratio are
precisely the ratio of consecutive Fibonacci numbers.

Exercise 5.5. Prove that any two consecutive Fibonacci numbers are relatively prime.

Exercise 5.6. Prove Cassini’s identity. (Fn−1Fn+1 − F 2
n = (−1)
n)

5.4 Pell Numbers

Deﬁnition 5.7. The Pell numbers (like the Fibonacci sequence) are deﬁned by this recurrence
relation
 P0 = 0, P1 = 1, Pn = 2Pn−1 + Pn−2

The ﬁrst few Pell numbers are 0, 1, 2, 5, 12, 29, 70, ...

The closed form expression for the nth Pell number is

Pn = (1 + √2)n − (1 − √2)n

2
√2

These numbers are the denominators of the convergents to √2 = [1, 2, 2, 2, ...]. If we started
with L0 = 2, L1 = 2 and constructed a sequence with the same recurrence relation as the
Pell numbers then the sequence that we get is twice the numerators of the convergents to √2.

6 Other Simple Continued Fractions

In the previous section, when we were looking at quadratic equations, we didn’t look at a
negative root. We only considered the positive root and constructed its continued fraction.
Now we will see what happens for continued fractions of negative numbers.

6.1 Negative numbers

The natural question to ask is if we need to allow negative numbers in the denominators of
continued fractions to express a negative number as a continued fraction. Recall that, by
deﬁnition, if [a0, a1, a2, ..., ] is a simple continued fraction, then a1 > 0, a2 > 0, .... One naive
thing to do is to negate every number appearing in the continued fraction expansion. i.e If
x = [a0, a1, a2, ...], then −x = [−a0, −a1, −a2, ...]. In doing so, we get negative numbers in
the denominators of the continued fraction.
It turns out that every negative number can be expressed with only a0 < 0 and all other
a1, a2, ... being positive integers.
 27

Let x be a negative number. Let W be the integral part and F be the fractional part
of −x.
 −x = W + F, 0 < F < 1

x = −W − F

x = (−W − 1) + (1 − F )

Notice that 0 < (1 − F ) < 1. Hence we can take the simple continued fraction of (1 − F ), say
[a0, a1, ...] and add (−W − 1) to get a simple continued fraction for x. By doing so, we get

x = [a0 − W − 1, a1, a2, ...]

with a1 > 0, a2 > 0, ...
If F was 0, then the continued fraction of x is x itself.

Example:
Let x = −17/12
−x = 17/12 = 1 + 5/12 =⇒ x = (−1 − 1) + (1 − 5/12) = −2 + 7/12
7/12 = [0, 1, 1, 2, 2] =⇒ −17/12 = [−2, 1, 1, 2, 2]
In this expression, the only negative term in the continued fraction expression is the ﬁrst
term, namely −2.

Given a continued fraction expression of x, is there a way of directly obtaining a contin-
ued fraction of −x? Yes, there is a neat way of going from one to the other!

Let x = [a0, a1, a2, a3...] = [a0, a1, [a2, a3, ...]]

x = a0 + 1

a1 + 1
[a2, a3, ...]

−x = −a0 − 1

a1 + 1
[a2, a3, ...]
 = −a0 − 1 + 1

1 + 1

a1 − 1 + 1
[a2, a3, ...]

Therefore, x = [a0, a1, a2, a3, ...] =⇒ −x = [−a0 − 1, 1, a1 − 1, a2, a3, ...]

Example:
x = 17/12 = [1, 2, 2, 2]
−x = −17/12 = [−1 − 1, 1, 2 − 1, 2, 2] = [−2, 1, 1, 2, 2]

If we were to instead start with x = −17/12 we would do the following:
Example:
x = −17/12 = [−2, 1, 1, 2, 2]
−x = 17/12 = [−(−2) − 1, 1, 1 − 1, 1, 2, 2] = [1, 1, 0, 1, 2, 2]

The continued fraction for 17/12 obtained by starting from the continued fraction of −17/12
doesn’t quite give us the required continued fraction!

The only problem with the above method is that a1 could be 1 which would make a1 − 1 as
0. There is a simple trick to elminate 0 from the continued fraction expression. Whenever
there is a 0, just add the previous term and the next term into a single entry and omit the
0. If 0 is the last term, then simply omit 0 and the previous term i.e.

28

[a0, a1, ..., am, 0, am+1, am+2..] = [a0, a1, ..., am + am+1, am+2, ...]
[a0, a1, ..., an−2, an−1, 0] = [a0, a1, ..., an−2]

Example:
x = 21/8 = [2, 1, 1, 1, 2]
−x = −21/8 = [−2 − 1, 1, 1 − 1, 1, 1, 2] = [−3, 1, 0, 1, 1, 2] = [−3, 1 + 1, 1, 2] = [−3, 2, 1, 2]

6.2 Subtraction in Continued Fractions

Recall that a simple continued fraction can be presented as [a0, a1, ...] with a0, a1, ... being
integers and a1 > 0, a2 > 0, .... Lagrange in the Appendices to his translation of Euler’s
Elements of Algebra points out that it is superﬂous to also have subtraction in the continued
fraction expression. As a ﬁrst step, if we have a continued fraction with subtraction in some
denominator, we can replace it with a continued fraction with only addition and possibly
negative terms. i.e
 a − 1
b + c = a + 1
−b − c

Here, a, b, c can be numbers, convergents or complete quotients.
After doing so, we need a way of removing negative numbers from a continued fraction
expression. With a little bit of algebra, we can see that this is also possible.

am + 1

−am+1 + 1
[am+2, am+3, ...]
 = (am − 1) + 1

1 + 1

(am+1 − 1) − 1
[am+2, am+3, ...]

In other words,

[a0, ..., am, −am+1, [am+2, am+3, ...]] = [a0, ..., am − 1, 1, am+1 − 1, −[am+2, am+3, ...]]
[a0, ..., am, −am+1] = [a0, ..., am − 1, 1, am+1 − 1]

In this process, if a 0 appears then we know how to get rid of it by following the procedure
from the previous section. Observe that removing a negative number might introduce further
negative numbers that appear later on in the continued fraction. We can inductively start
from the left and remove negative numbers from left to right.

Example:
[2, −3, 4] = [2 − 1, 1, 3 − 1, −4]
[1, 1, 2, −4] = [1, 1, 2 − 1, 1, 4 − 1]
[1, 1, 2 − 1, 1, 4 − 1] = [1, 1, 1, 1, 3]
We can indeed check that

[2, −3, 4] = 2 + 1

−3 + 1
4
 = 18
11 = [1, 1, 1, 1, 3] = 1 + 1

1 + 1

1 + 1

1 + 1
3

The next example illustrates all the rules discussed in this section.

Example:
 29

−30/13 = [−3, 1, 2, 4]
[−3, 1, 2, 4] = −[3, −1, −2, −4] We want the ﬁrst entry to be positive.
−[3, −1, 2, 4] = −[2, 1, 0, −[−2, −4]] This is the rule to eliminate a negative sign.
−[2, 1, 0, −[−2, −4]] = −[2, 1, 0, 2, 4] Negative sign distributes to each entry.
−[2, 1, 0, 2, 4] = −[2, 1 + 2, 4] Rule for removing 0.
−[2, 3, 4] = [−3, 1, 2, 4] Rule for negating a continued fraction.

6.3 Diﬃculties with negative terms

There are many practical diﬃculties if we allow negative numbers in continued fractions.

1. Arbitrary length of a continued fraction may reduce to 0
There are many continued fractions one can construct that just reduce to 0. For instance
[1, −1] and [1, 1, 1, −1, 3] are two such examples. Try to construct other continued
fractions for 0.

2. Later terms might collapse a continued fraction.
Since there are many ways of writing 0 as a continued fraction, these may be part
of a bigger continued fraction which makes it irrelevant when converting a continued
fraction to a real number.

3. Uniqueness result of continued fractions no longer holds.
It won’t make sense any more to talk about “the” continued fraction expression of a
real number.

4. Convergents may be inﬁnite.
For instance, the convergents to [1, −2, 1, −2, 1, −2] are 1, 1/2, 0, ∞, 1, 1/2.

5. Convergents may not alternate between larger and smaller numbers and we won’t have
a nice picture as before.
The above example [1, −2, 1, −2, 1, −2] demonstrates this.

6. Convergents may not converge.
Find the convergents to [0, 2, −2]. The word “convergent” isn’t appropriate if we allow
negative terms.

7. Negative values can anyway be written without negative numbers(except the ﬁrst con-
vergent).
This was the content of the beginning of this section where an explicit rule was discussed
to still have a1 > 0, a2 > 0, ....

All these reasons tell us why we should stick to working with simple continued fractions.

6.4 General Continued Fraction

Deﬁnition 6.1. The General Continued Fraction is a simple continued fraction in which
the numerators can be any positive interger (not necessarily 1).

Example:
 √6 = 2 + 2

4 + 2

4 + 2
4 + ...

30

Working with a general continued fraction instead of a simple continued fraction does not
give us any new information but in some cases it is easier to explicitly compute a general
continued fraction rather than a simple continued fraction. There are some examples given
in the Appendix.

Finding a general continued fraction of √n:
Let a be any number with a
2 ≤ n. √n = a + x
n = a2 + 2ax + x2

n − a
2 = x(2a + x)

x = n − a
2

2a + x
√n = a + x = a + n − a2

2a + x = a + n − a2

2a + n − a
2

2a + x
 = ...

Setting n = 6, a = 2 gives us the previous example. Taking a = 1 instead gives us

√6 = 1 + 5

2 + 5

2 + 5
2 + ...

Example:
Consider the quadratic equation x2 − x − 2 = 0.

x2 − x − 2 = 0
x2 = x + 2

x = 1 + 2
x

x = 1 + 2
x = 1 + 2

1 + 2
x

x = 1 + 2

1 + 2

1 + 2
1 + ...

What if we wanted a simple continued fraction for x instead of the above general continued
fraction? We have already seen that the quadratic surds are precisely all the periodic con-
tinued fractions. However, the solution to this quadratic equation is in fact rational. More
precisely
 x2 − x − 2 = 0
(x − 2)(x + 1) = 0
x = 2, x = −1

Notice that x = 2 is the only positive solution to the quadratic equation. Thus we have
obtained a general continued fraction for 2. The only simple continued fractions for 2 are [2]
and [1, 1].
 31

2 = 1 + 2

1 + 2

1 + 2
1 + ...

7 Irrational Numbers

Finite simple continued fractions correspond to rational numbers and every rational number
has a ﬁnite simple continued fraction expression. In the previous sections we have been
loosely using [a0, a1, ...] without formally deﬁning what this means. In this section we will
see how the inﬁnite simple continued fractions correspond to irrational numbers and what
their properties are.

7.1 Deﬁnition

One of the main interests of continued fractions is in its application to the representation of
irrationals.
Suppose a0, a1, a2, ... is a sequence of integers with a1 > 0, a2 > 0, ... so that

xn = [a0, a1, ..., an]

is a simple continued fraction of a rational number xn for every n. If these xn tend to a limit
x when n → ∞, then we say that [a0, a1, ...] is x and we write

x = [a0, a1, a2, ...]

Theorem 7.1. If a0, a1, a2, ... is a sequence of integers with a1 > 0, a2 > 0, ... then xn =
[a0, a1, ..., an] tends to a limit x when n → ∞.

Proof. We have
 xm = pm
qm = [a0, a1, ..., am]

Note that xm is also a convergent to xn if m ≤ n. By Theorem 4.1 and Theorem 4.2, the even
convergents are increasing and less than x1. Simlarly, the odd convergents are decreasing
and greater than x0. Hence, the even convergents will have a limit and the odd convergents
will have a limit.
Theorem 2.5 and Theorem 4.5 tell us that

p2n−1
q2n−1 − p2n
q2n = 1
q2nq2n−1 ≤ 1
2n(2n − 1)

which tends to 0 as n tends to ∞. This implies that the limit for the odd and even convergents
are the same and hence xn will tend to a limit x as n tends to ∞.
 Q.E.D.

In particular, this means that we can always talk about [a0, a1, a2, ...] as it is a well-deﬁned
real number.
 32

7.2 Properties

In this section, we see some properties of these inﬁnite simple continued fractions.

Theorem 7.2. An inﬁnite simple continued fraction is less than any of its odd convergents
and greater than any of its even convergents.

Proof. In the proof of Theorem 7.1, we see that the even convergents increase to the limit
and the odd convergents decrease to the limit. This shows that the value of the continued
fraction is less than any of its odd convergents and greater than any of its even convergents.

Q.E.D.

Theorem 7.3. If [a0, a1, ..] = x, then

a0 = integral part of x, am = integral part of a
′
m.

Proof. This proof is analogous to the case of ﬁnite continued fraction.

a
′
m = [am, am+1, ...] = lim
n→∞[am, am+1, ..., an] = am + 1
a′
m+1

In particular, x = a
′
0 = a0 + 1
a′
1

a
′
m > am, a
′
m+1 > am+1 > 0, 0 < 1
a′
m+1 < 1

Hence, am = integral part of a
′
m.
 Q.E.D.

Theorem 7.4. Two inﬁnite simple continued fractions which have the same value are iden-
tical.

Proof. By the previous theorem, the ﬁrst term of both continued fractions is just the integral
part of the value. We can inductively see that am is the integral part of a
′
m and hence has to
be the same in both inﬁnite continued fraction expressions. Hence, the two inﬁnite continued
fractions must be identical.
 Q.E.D.

Theorem 7.5. Every irrational number can be expressed in just one way as an inﬁnite simple
continued fraction.

Proof. The continued fraction algorithm produces a simple continued fraction for an irrational
number. The algorithm does not terminate as we know that ﬁnite simple continued fractions
correspond to rational numbers and hence we get an inﬁnite continued fraction. By the
previous theorem, this inﬁnite simple continued fraction expression is unique.
 Q.E.D.

33

7.3 Equivalent Numbers

Deﬁnition 7.6. If ξ and η are two numbers such that

ξ = aη + b
cη + d

where a, b, c, d are integers such that ad − bc = ±1, then ξ is said to be equivalent to η.

Theorem 7.7. The above relation is an equivalence relation.

Proof. Any number is equivalent to itself because if we set a = 1, b = 0, c = 0, d = 1 in the
deﬁnition above, we get
 η = 1.η + 0
0.η + 1

with ad − bc = 1.
If ξ is equivalent to η with a, b, c, d as in the deﬁnition then

η = − dξ + b
cξ − a

with (−d)(−a) − bc = ad − bc = ±1 which implies η is equivalent to ξ.
If ξ is equivalent to η with
 ξ = aη + b
cη + d, ad − bc = ±1

and η is equivalent to ω with
 η = a
′ω + b′

c′ω + d′, a
′d′ − b′c
′ = ±1

then
 ξ = Aω + B
Cω + D

with A = aa
′+bc
′, B = ab
′+bd
′, C = ca
′+dc
′, D = cb
′+dd
′, AD−BC = (ad−bc)(a
′d
′−b
′c′) =
±1 which implies ξ is equivalent to ω.
Hence, this is indeed an equivalence relation.
 Q.E.D.

Theorem 7.8. Any two rational numbers are equivalent.

Proof. We will show that any rational number is equivalent to 0 which would imply that any
two rational numbers are equivalent. Let a/b be a non-zero rational number where a and b
are coprime integers. Consider the numbers a, 2a, 3a, ..., (b − 1)a. Since a and b are coprime,
b does not divide any of these numbers. Let us assume that no number in this sequence
leaves the remainder 1 when divided by b. Therefore, two of these numbers must leave the
same remainder when divided by b.
Say m1a and m2a leave the same remainder when divided by b with m1 < m2. Then b divides
(m2 − m1)a which is a contradiction as m2 − m1 is less than b and gcd(a, b) = 1. Hence there
exists integers s and t such that as = bt + 1.
Then
 a
b = t.0 + a
s.0 + b

34

with tb − sa = (−1). This is precisely the condition which says a/b is equivalent to 0.

Q.E.D.

In the above proof we have used the pigeonhole principle to provide a proof by contra-
diction. A more direct proof is explained in the remarks below.
Remarks:
1. The statement that there exists integers s and t such that as − bt = 1 when a and b are
coprime is called Bezout’s identity.
2. An alternative method to prove this using continued fractions is as follows:

Take the continued fraction expression for a
b. Say a
b = [a0, a1, ..., an]. Then a
b = pn
qn which im-

plies a = pn, b = qn since a and b are coprime. Theorem 2.5 implies aqn−1 −bpn−1 = (−1)n−1.
Either (s, t) = (qn−1, pn−1) or (s, t) = (−qn−1, −pn−1) depending on whether n is odd or even.

Theorem 7.9. Two irrational numbers ξ and η are equivalent if and only if

ξ = [a0, a1, ..., am, c0, c1, c2, ...], η = [b0, b1, ..., bn, c0, c1, ...],

the sequence of quotients in ξ after the m-th being the same as the sequence in η after the
n-th for some m and n.

Proof. Suppose ξ and η have continued fraction expressions as in the theorem, then let
ω = [c0, c1, ...]. Then
 ξ = [a0, a1, ..., am, ω] = pmω + pm−1
qmω + qm−1

with pmqm−1 −pm−1qm = (−1)(m−1) and hence ξ is equivalent to ω. Simliarly, η is equivalent
to ω which implies ξ is equivalent to η.
We will not prove the second part of the theorem here.
 Q.E.D.

This says that two irrational numbers are equivalent precisely when their continued frac-
tion expansions are eventually the same.
 35

8 Appendix

8.1 Special constants

Here are some continued fraction expansions of some special numbers which have been known
for a long time:

π = 3 + 1

7 + 1

15 + 1

1 + 1

292 + 1

1 + 1

1 + 1
1 + ...
 = [3, 7, 15, 1, 292, 1, 1, 1, 2, 1, 3, 1, 14, 2, ...]

The ﬁrst few convergents of π are
 [3] = 3
1 = 3

[3, 7] = 22
7 = 3.142857

[3, 7, 15] = 333
106 = 3.14150943...

[3, 7, 15, 1] = 355
113 = 3.14159292...

[3, 7, 15, 1, 292] = 103993
33102 = 3.14159265...

This says that 355
113 is the best approximation to π by a rational number with denominator
≤ 113. In fact, an easy way to remember this number is to write the ﬁrst three odd numbers
twice each, 113355, and the ﬁrst three digits form the denominator while the next three digits
form the numerator.
Here are a few more general continued fraction expressions

4
π = 1 + 12

2 + 3
2

2 + 5
2

2 + 72

2 + ...
4
π = 1 + 12

3 + 2
2

5 + 3
2

7 + 42

9 + ...

π = 3 + 1
2

6 + 32

6 + 5
2

6 + 7
2

6 + ...

36

π
2 = 1 + 1

1 + 1 × 2

1 + 2 × 3

1 + 3 × 4
1 + ...

e − 1 = 1 + 2

2 + 3

3 + 4

4 + 5
5 + ...

e − 1 = 1 + 1

1 + 1

2 + 2

3 + 3
4 + ...

8.2 Applications

1. Along the lines of Bezout’s identity, we can use continued fractions to ﬁnd integer
solutions for the equation ax + by = c, where a, b, c are integers. If the greatest common
divisor of a and b does not divide c, then there are no integer solutions.

Example: 2x + 4y = 7 has no integer solutions.

We might as well assume, a, b are coprime. Then, Bezout’s identity says there exist
integers s, t such that as − bt = 1. Hence, x = cs, y = −ct is a solution to ax + by = c.
In fact, these integers have been explicitly constructed using continued fractions.

2. To show that the real numbers are uncountable, we typically use Cantor’s diagonaliza-
tion argument on the decimal expansion of real numbers. However, the argument is
not very clean because the decimal expansion of a real number is not unique.

Example: 0.¯9 = 1

Instead of the decimal expansion, we can use the continued fraction expressions.

Cantor’s diagonalization argument says that the inﬁnite continued fractions are un-
countable. Since the set of inﬁnite continued fractions is in bijection with the set of
irrational numbers, this says that the irrational numbers are uncountable. The ﬁnite
continued fractions are in 2-1 correspondence with the set of rational numbers and
hence the set of rational numbers is countable.

There are a lot of applications of continued fractions since they give good approxima-
tions to real numbers. Here are some of them:

3. They are used in constructing clockwork models of the solar system (orrery). On a
related subject, one can construct simple calendars which give a better approximation
to a solar year than the current calendar we have (where leap years are omitted).

4. Phyllotaxis is the study of the arrangement of leaves (or any such botanical unit)
around an axis or a stem. The numbers arising from such arrangements are very
closely connected to simple continued fractions and their properties.

5. Continued fractions are used to study solutions of Diophantine equations. A funda-
mental solution for Pell’s equation which is a particular kind of Diophantine equation

37

can be computed using continued fractions. There are algorithms known to compute
these fundamental solutions using continued fractions.

6. In the study of rational tangles and knots, there is a correspondence with continued
fractions. These are especially useful to distinguish rational tangles.

7. There are some trignometric formulae which are known to have simple expressions
(involving square roots). Such expressions can be computed for many other angles
by studying continued fractions. This heavily uses the idea that periodic continued
fractions correspond to quadratic surds.

8. The periodic continued fractions are used in continued fraction factorization method
(CFRAC) to provide an algorithm for (large) integer factorization. Further work has
been done in this area using the properties of continued fractions.

9 Project Ideas

9.1 Cantor Set

Georg Cantor described a subset of [0, 1] interval which is now called the Cantor set (denoted
by C). It is constructed iteratively by removing the middle third from a set of line segments
starting from [0, 1]. The ﬁrst step is to remove ( 1
3 , 2
3 ) to get [0, 1
3 ] ∪ [ 2
3 , 1]. The second step is
to remove the middle thirds from the two line segments obtained in the previous step to get
[0, 1
9 ] ∪ [ 2
9 , 1
3 ] ∪ [ 2
3 , 7
9 ] ∪ [ 8
9 , 1]. We keep removing the middle thirds and whatever set we end
up with is called the Cantor set.
We know that any number in [0, 2] can be written as a sum of two numbers from [0, 1]. After
the ﬁrst step, observe that any number in [0, 2] can still be written as a sum of two numbers
from [0, 1
3 ] ∪ [ 2
3 , 1]. Does this hold true at every step of the process?
Lets ﬁx a postive integer N and look at all continued fractions with bounded terms. Instead
of [0, 2], can we now write some other interval as a sum of two numbers from this set?

• The primary goal of this project is to understand the Cantor set and what happens to
C + C.

• The secondary goal is to relate this to continued fractions with bounded terms. i.e
Expressions of the form
 a0 + 1

a1 + 1

a2 + 1
a3 + ...

where a0, a1, a2, ... are bounded above by some ﬁxed integer N .

9.2 Pell’s equation

x2 − dy2 = 1 is called Pell’s equation. This equation was connected with the name of John
Pell by Euler in a letter (10 August 1730) to Goldbach because Euler believed Pell responsible
for a solution technique. A more general equation is x2 − dy2 = N where N is some ﬁxed
integer and d is an integer greater than 1 that is not a perfect square. The objective is to
ﬁnd integer solutions of these equations.
For instance, consider the equation x2 − 3y2 = 1. The continued fraction of √3 is

38

1 + 1

1 + 1

2 + 1

1 + 1
2 + ...
 = [1, 1, 2]

Observe that the convergents of this continued fraction are 1
1
, 2
1
, 5
3, 7
4
, 19
11
, 26
15
, ... and the in-

teger solutions of Pell’s equation are (2, 1), (7, 4), (26, 15), ... which are the numerators and
denominators of some of the convergents. Does this pattern hold in general? If so, which
convergents give us solutions of Pell’s equation?

• The primary goal is to relate the integer solutions to convergents of an appropriate
continued fraction.

• The secondary goal is to relate the length of periodic continued fractions to solutions
of the above equations when N is negative.

9.3 Empty parallelogram theorem

Let α and β be two diﬀerent irrational numbers and consider the parallelogram in the plane
with sides parallel to the lines y = αx and y = βx and with center at the origin. What can
we say about the area of such a parallelogram if we impose the condition that it shouldn’t
contain any lattice points apart from the origin? (A lattice point is a point on the plane with
integer coordinates.)
Is there a value such that for any such parallelogram with area greater than this value, the
parallelogram deﬁnitely contains a lattice point? Interestingly, it turns out that there is a
lower bound for such a value that is independent of α and β which involves the golden ratio.
The goal of this project is to understand the proof of this theorem using continued fractions.
This project is similar to the topic of computing convergents of a continued fraction (of α)
by seeing which lattice points occur closest to the line y = αx.

39
 X

Y
 y = αx

y = βx

9.4 Markov triples

A Markov triple (m1, m2, m3) consists of three positive integers such that

m2
1 + m
2
2 + m
2
3 = 3m1m2m3
To each Markov triple there is a way of associating a quadratic form

ax2 + bxy + cy2

where a, b, c are integers that depend on m1, m2, m3. A Markov number is an integer that
belongs to at least one Markov triple. Two Markov triples are said to be adjacent to each
other if two of their Markov numbers are the same. For example, (5, 1, 2) is a Markov triple
and its neighbors are (1, 1, 2), (5, 29, 2), (5, 1, 13).
The goal is to start with a Markov triple and iteratively construct Markov triples by con-
structing the neighbors at each step. Certain periodic continued fractions appear as roots of
quadratic forms associated to Markov triples. The secondary goal is to see what the roots
are for the chain of Markov triples.

9.5 Calendars

In this project, the goal is to understand how to construct a calendar based on approximations
of the time period of planet (using continued fractions). Are there better calendars than the
one that we currenly use? If so, how better are they and why aren’t we using them instead?
A related topic is to understand how to choose gear sizes to construct an orrery if there is a
practical constraint on the number of teeth on the gears. This problem is similar in ﬂavor to
the above problem in that it only involves integer arithmetic.

40

References

[1] Hardy, G.H; An Introduction to the theory of numbers, Oxford University Press, 2008

[2] Kiritchenko, V; Continued Fractions and good approximations
www.math.jacobs-university.de/timorin/PM/continued fractions.pdf

[3] Knott, R; Ron Knott’s web page on mathematics
www.maths.surrey.ac.uk/hosted-sites/R.Knott/Fibonacci/cfINTRO.html

[4] Loya, P; Amazing and Aesthetic Aspects of Analysis: On the incredible inﬁnite
people.math.binghamton.edu/dikran/478/Ch7.pdf

[5] Rockett, A; Szusz, P; Continued Fractions, World Scientiﬁc Publishing, 1992

[6] Shreevatsa, R;
shreevatsa.wordpress.com/2011/01/10/not-all-best-rational-approximations-are-the-
convergents-of-the-continued-fraction/
 41
