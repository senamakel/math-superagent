<!-- source: https://math.mit.edu/classes/18.095/2024IAP/L5N.pdf | converted from PDF -->

Continued Fraction Notes

Peter Shor

Continued fractions are a topic in number theory which has applications to rational
approximations of real numbers. We will ﬁrst explain what a continued fraction is,
prove some basic theorems about them, and then show how they can be used to ﬁnd
good rational approximations.
A continued fraction is a number of the form

a0 + 1

a1 + 1

a2 + 1

a3 + 1

a4 + 1
. . .

Note that the numerator of all these fractions is 1. There are generalizations that
don’t require this; these are called generalized continued fractions. We will limit these
notes to regular continued fractions, where the numerator is 1.
How do we ﬁnd a continued fraction expansion of a number? It is relatively
straightforward. As an example, let’s ﬁnd the continued fraction expansion of 37
112 .
We start by dividing 112 by 37 and get a remainder of 11. This gives

37
112 = 1

3 + 11
37

We then just keep expanding the last piece of the denominator in the same way:

37
112 = 1

3 + 11
37
 = 1

3 + 1

3 + 4
11
 = 1

3 + 1

3 + 1

2 + 3
4
 = 1

3 + 1

3 + 1

2 + 1

1 + 1
3

We will denote this as 37
112 = CF [0, 3, 3, 2, 1, 3]. Here 0 is the integer part of our
number; 149
112 would be CF [1, 3, 3, 2, 1, 3].
The following theorem is not hard to prove, so we will leave it as an exercise for
the reader:

Theorem 1. A continued fraction expansion of R terminates if and only if R is a
rational number.
 1

If a number is not rational, it has a unique inﬁnite continued fraction.
Let’s look at the continued fraction expansion of the golden ratio: √5+1
2 . We have

√5 + 1
2 = 1 +
 √5 − 1
2 = 1 + (√5 − 1)(
√5 + 1)
2(√5 + 1) = 1 + 1
√5 + 1
2

But we can now use this equation to replace the √5+1
2 in the denominator to get

√5 + 1
2 = 1 + 1

1 + 1

1 + 1
1 + . . .

or √5+1
2 = CF [1, 1, 1, 1, 1, . . .].
This is a special case of the theorem

Theorem 2. A continued fraction expansion of R is eventually periodic if and only if
R is a solution to a quadratic equation with integer coefﬁcients, i.e., R = a+
√b
c .

What eventually periodic means here is that after an initial segment, it starts repeating.
Before we prove this theorem, let’s give an example for the forward direction that
shows how the proof works. Let’s look at the continued fraction CF = [0, 3, 5, 3, 5, 3, 5, . . .].
That is, 1

3 + 1

5 + 1

3 + 1
5 + . . .
Let its value be x. Then, we have
 x = 1

3 + 1
5 + x
.

We can simplify this, We get
 x = 5 + x
16 + 3x ,

or x(16 + 3x) = 5 + x.

This gives the quadratic equation 3x2 + 15x − 5 = 0, which has solutions −15±√285
6 .
Since the solution is positive, it must be √285−15
6 .

2

In fact, any expression of the form:

a0 + 1

a1 + 1

a2 + 1

a3 + 1
. . . 1
ak + x
,

where a1, a2, . . . ak are nonnegative integers, reduces to a fraction of the form rx+s
tx+u
where r, s, t, u are integers. Setting
 x = rx + s
tx + u

gives a quadratic equation tx2 + (n − r)x − s = 0, which has solutions of the form
a±√b
c .
How about the other direction? Let’s look at the continued fraction for 1+
√17
2 . We
have
√17 + 1
2 = 2+ 1
2 (
√17−3) = 2+ (
√17 − 3)(
√17 + 3)
2(
√17 + 3) = 2+ 1

1
4 (√17 + 3) = 2+ 1

1 + 1
4 (
√17 − 1)

Continuing with similar calculations (which we omit), we ﬁnd

2 + 1

1 + 1
4 (
√17 − 1) = 2 + 1

1 + 1

1 + 1
4 (
√17 − 3)
 = 2 + 1

1 + 1

1 + 1

3 + 1
2 (√17 − 3)
,

and since we saw 1
2 (√17−3) earlier in our calculations, we see that the continued frac-
tion has begun to repeat. Thus, 1
2 (
√17 + 1) = CF (2, 1, 1, 3, 1, 1, 3, 1, 1, 3, 1, 1, . . .).
It’s clear from the calculations that the remainder on the ith step will be of the from
a+b√17
c . What we have to show is that a, b, and c are integers that are bounded, i.e.,
they don’t grow to inﬁnity as the level of the continued fraction increases. If we can
show that, then by the pigeonhole principle they must start repeating at some point, and
we have an eventually periodic continued fraction.
How do we get around the fact that a, b, c, might keep growing indeﬁnitely? The
ﬁrst proofs of this theorem were quite complicated, but I found a beautiful way to prove
this in a set of lecture notes by Aaron Pollack. It depends on the following lemma:

3

Lemma 1. Any fraction of the form
 b√d − a
c ,

where a, b, c, d are nonnegative integers can be written in the form
√d′ − p
q

where p, q, d′ are nonnegative integers and q | d
′ − p
2.

(Here the symbol s | t means “s divides t”.)

Proof. The proof of this is relatively simple. We let q = c2, d
′ = c
2b
2d, and p = ac.
Then √d′ − p
q =
 √b2c2d − (ac)
2

c2 = b√d − a
c

and d
′ − p
2 = c2b2d − (ac)
2, which is divisible by c2.

Now, we are ready to prove the theorem.

Theorem 3. Suppose we have a quadratic number of the form √d−p
q where q | d − p
2.
Then the continued fraction associated with it is eventually periodic.

Proof. We will show that one step of the continued fraction algorithm starting with
√d−p
q with q | d − p2 will take you to another continued fraction with √
d−p′

q′ with
q′ | d − p′2, keeping the same d. We also show that for any d, there are only a ﬁnite
number of p and q satisfying q | d − p2, meaning that by the pigeonhole principle, at
some point we must come to a triple (d, p, q) that we have seen before. At this point,
the continued fraction starts repeating.
First, why are there only a ﬁnite number of (p, q) with q|d − p
2? It’s clear that
p < √d and q < d, so there are only a ﬁnite number of possible such p and q.
Next, we need to show that if we start with such a √d−p
q , we get on the next step a
√d−p′

q′ . For a continued fraction step, the ﬁrst thing we do is take the reciprocal:

( √d − p
q
 )−1
 = q
√d − p = q(
√d + p)
d − p2

Now since we have q | d − p2, we can let q′ = d−p2

q , and we have

( √d − p
q
 )−1
 =
 √d + p
q′ ,

and it is still true that q′ | d − p
2.
 4

The next step is to subtract an integer from this quantity to make it between 0 and 1.
Let this integer be ℓ. this means we now have
√d + p
q′ − ℓ =
 √d + p − ℓq′

q .

Letting p
′ = p − ℓq′, it is still the case that q′ | d − p′2, because

d − p
′2 = d − p
2 + 2pℓq′ + ℓ
2q′2,

which is a multiple of q′ because d−p
2 is a multiple of q′. So each step of the continued
fraction preserves the relation qi | d − p
2
i ,

and by the pigeonhole principle, the continued fraction must be eventually periodic.

The last thing to do is show that if we have a continued fraction that cannot be put
into the form √d−p
q with d > p2 and q | d − p
2, then after some number of continued
fraction iterations, it will be in this form. I will leave this as an exercise.

0.1 Using Continued Fractions for Diophantine Approximation

Continued approximations can be used for ﬁnding good approximations of reals by
fractions. For example, the approximations

π ≈ 3, π ≈ 22/7 ≈ 3.143, π ≈ 333
106 ≈ 3.14151,

can all be found by looking at the convergents of the continued fraction for π.
The convergents of a continued fraction are the continued fractions made from an
initial sequence of the elements. For example, we have

615
2048 = 1

3 + 1

3 + 1

33 + 1

1 + 1
5
,

so 615
2048 = CF (0, 3, 3, 33, 1, 5).
The convergents of this continued fraction are CF (0), CF (0, 3), CF (0, 3, 3),
CF (0, 3, 3, 33), and CF (0, 3, 3, 33, 1). Here are their numerical values:

1
3 = 1
3 ≈ 0.3333,

1

3 + 1
3
 = 3
10 ≈ 0.3,

5

1

3 + 1

3 + 1
33
 = 100
333 ≈ 0.3003003,

1

3 + 1

3 + 1

33 + 1
1
 = 103
343 ≈ 0.3002915,

You can see that these values keep getting closer to 615/2048 ≈ .30029297.
We now show that all the closest approximations to a real number are convergents
of its continued fraction. Speciﬁcally, we show:

Theorem 4. if |R − p
q | ≤ 1
2q2 , then p
q is one of the convergents of r.

How do we show this theorem? We ﬁrst prove a lemma:

Lemma 2. Suppose p
q < R < p′

q′ and pq′ = 1 + p′q. With these conditions if q < q′,

then p
q is one of the convergents of R, and if q′ < q, then p
′

q′ is one of the convergents
of R.

Let’s take as an example R = 615/2048 ≈ .30030293. We have

3
10 = 0.3 < 615/2048 = 0.30030293 < 10
33 = 0.30303.

We can easily check that 3 · 33 + 1 = 10 · 10 This shows that 3
10 is a convergent. ( 33
100
is not, although it is something called a semiconvergent).
Proof of Lemma 2:
First, let’s look at the continued fractions for p
q and p′

q′ . I claim that they cannot be of
the forms p
q = 1

a + 1
b + . . .
and p
′

q′ = 1

a′ + 1
b′ + . . .

with a > a′. Suppose they were. Then the fraction 1
a would be between p
q and p′

q′ , and

would have a lower denominator than either, and it would be impossible for p′

q′ − p
q =
1
qq′ . Thus, p
′ and q′ both must start with a = a
′. Now, let’s consider the continued
fractions p
q = 1
a + b
c and p
′

q′ = 1
a + b′
c′

6

We will show p
′q − pq′ = 1 if and only if b
′c − bc
′ = 1.
First, we calculate
 p
q = c
ac + b and p′

q′ = c
′

ac′ + b′

so p′q − pq′ = c(ac
′ + b
′) − c′(ac + b) = b
′c − bc
′.

What this shows is that if the two continued fractions

p
q = 1

a + 1

b + 1
c + . . .
 and p′

q′ = 1

a′ + 1

b′ + 1
c′ + . . .
,

satisfy | p′

q′ − p
q | = 1
qq′ , then the continued fractions

r
s = 1

b + 1
c + . . .
 and r′

s′ = 1

b′ + 1
c′ + . . .
,

satisfy | r
s − r′
s′ | = 1
ss′ . We can in this way keep removing the ﬁrst terms of the continued
fractions and preserve the relation between the remaining terms. When can this process
end? It can only end when one of the two continued fractions has been reduced to the
form 1
a . At this point, the other continued fraction must look like

1

a + 1
b + . . .
,

so the ﬁrst continued fraction is a convergent of the second one. And since R is sand-
wiched between them, the ﬁrst continued fraction must also be a convergent of R.
We now use the lemma to prove the theorem. Suppose that p
q < R (the case of

p′

q′ > R is completely analogous) and that R − p
q < 1
2q2 . Now, p
q must be the closest
fraction to R with denominator at most q, because two fractions with denominator
less than or equal to q cannot be closer to each other than 1
q(q−1) . There must also

be a smallest fraction larger than p
q with denominator at most q. Call this fraction p′

q′ .

Because there are no fractions between p
q and p′

q′ with denominator at most q, we must
have pq′ + 1 = p′q. And we must have

p
q < R < p
′

q′

7

Let’s consider the fraction p+p′

q+q′ . We have

p + p
′

q + q′ − p
q = q(p + p
′) − p(q + q′)
q(q + q′)

= p
′q − q′p
q(q + q′)

= 1
q(q + q′) > 1
2q2

This is larger than the distance between p
q and R, so R must be between p
q and p+p′

q+q′ .
And clearly the denominator q is less than the denominator q + q′. This shows that
p
q satisﬁes the conditions of Lemma 2 to be a convergent of R, and we have proved
Theorem 4.
 8
