<!-- source: https://kconrad.math.uconn.edu/blurbs/ugradnumthy/ordersmodm.pdf | converted from PDF -->

ORDERS OF UNITS IN MODULAR ARITHMETIC

KEITH CONRAD

1. Introduction

If a mod m is a unit then aϕ(m) ≡ 1 mod m by Euler’s theorem. Depending on a, it might
happen that an ≡ 1 mod m for a positive integer n that is smaller than ϕ(m).

Example 1.1. Let m = 7. The following table shows that the ﬁrst time a unit mod 7
has a power congruent to 1 varies with the unit. While Euler’s theorem (or Fermat’s little
theorem) tells us that a6 ≡ 1 mod 7 for a ̸≡ 0 mod 7, we see in the table that the exponent
6 can be replaced by a smaller positive exponent when a ̸≡ 3 or 5 mod 7.
k 1 2 3 4 5 6
1k mod 7 1
2k mod 7 2 4 1
3k mod 7 3 2 6 4 5 1
4k mod 7 4 2 1
5k mod 7 5 4 6 2 3 1
6k mod 7 6 1

Example 1.2. Let m = 15. Since ϕ(15) = 8, Euler’s theorem says a8 ≡ 1 mod 15 when
(a, 15) = 1. But in fact exponent 8 is higher than necessary: the table below shows we can
use exponent 1, 2, or 4. k 1 2 3 4
1k mod 15 1
2k mod 15 2 4 8 1
4k mod 15 4 1
7k mod 15 7 4 13 1
8k mod 15 8 4 2 1
11k mod 15 11 1
13k mod 15 13 4 7 1
14k mod 15 14 1

The fact that sometimes an ≡ 1 mod m where 0 < n < ϕ(m), depending on a, leads us
to give a name to the ﬁrst exponent that ﬁts this condition when the base is a.

Deﬁnition 1.3. The order of a unit a mod m is the least n ≥ 1 such that an ≡ 1 mod m.

Example 1.4. By the table in Example 1.1, 2 mod 7 has order 3, 3 mod 7 has order 6, and
4 mod 7 has order 3.

Example 1.5. By Example 1.2, we see 2 mod 15 has order 4 and 11 mod 15 has order 2.

Example 1.6. Always 1 mod m has order 1. If (a, m) = 1 and a ̸≡ 1 mod m then a mod m
has order greater than 1. 1

2 KEITH CONRAD

Example 1.7. A unit mod m and its inverse (like 2 mod 15 and 8 mod 15) have the same
order, since their powers are the same except in reverse order.

Example 1.8. For a fraction a/b in reduced form with (10, b) = 1, the number of digits in
the repeating part of its decimal expansion is the order of 10 mod b. We will discuss this in
Section 4.

We do not deﬁne the order of a mod m when (a, m) > 1. Why? Because in order for the
condition an ≡ 1 mod m to hold for some n ≥ 1 the number a must be relatively prime to
m: if an ≡ 1 mod m then an = 1 + md for some integer d, so any common factor or a and
m is a factor of 1 and thus is ±1.
To emphasize that the order of a mod m is the least n ≥ 1 making an ≡ 1 mod m, we
can express the deﬁnition of a mod m having order n like this:

a
n ≡ 1 mod m, aj ̸≡ 1 mod m for 1 ≤ j < n.

Example 1.9. If m > 2 then −1 mod m has order 2 since (−1)2 ≡ 1 mod m and (−1)1 =
−1 ̸≡ 1 mod m. When m = 2, −1 ≡ 1 mod 2, so −1 mod 2 has order 1.

The order of any unit mod m is at most ϕ(m), by Euler’s theorem. We will see that
the relation is stronger than an inequality: the order is a factor of ϕ(m). For instance, in
Example 1.1 we see that the order of every unit mod 7 is a factor of 6.

Warning. If an ≡ 1 mod m, this does not mean a mod m has order n, since the exponent
might not be as small as possible. For example, (−1)4 ≡ 1 mod m, but this doesn’t mean
−1 mod m has order 4, and in fact it does not since (−1)2 ≡ 1 mod m.

In Section 2 we will relate the order of a mod m to periodicity properties of the sequence
of powers 1, a, a2, a3, . . . mod m. In Section 3 we will see how the order of a mod m tells us
the order of any power ak mod m. In Section 5 we will discuss the order of a product of two
units if we know the order of each unit already. Some applications of orders, including to
decimal periods, are in Section 4. Finally, in Section 6 we will show that for prime p there
is a unit modulo p with order p − 1.

2. Orders, divisibility, and periodicity

To see how closely the order of a mod m is tied up with the whole sequence of powers
a, a2, a3, . . . mod m, let’s look at the ﬁrst 20 powers of each unit mod 7:
k 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
1k mod 7 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1 1
2k mod 7 2 4 1 2 4 1 2 4 1 2 4 1 2 4 1 2 4 1 2 4
3k mod 7 3 2 6 4 5 1 3 2 6 4 5 1 3 2 6 4 5 1 4 5
4k mod 7 4 2 1 4 2 1 4 2 1 4 2 1 4 2 1 4 2 1 4 2
5k mod 7 5 4 6 2 3 1 5 4 6 2 3 1 5 4 6 2 3 1 2 3
6k mod 7 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1 6 1
Each row looks periodic. More precisely, the order of a mod 7 tells us the number of
diﬀerent powers of a mod 7 before the powers start to repeat. In general, we want to
show that if a mod m has order n then the sequence of powers of a mod m looks like
1, a, a2, . . . , an−1, 1, a, a2, . . . mod m with a repeating block of length n and this repeating
block is as small as possible:
(1) (Repeating Block) Every power of a mod m is ar mod m where 0 ≤ r ≤ n − 1,

ORDERS OF UNITS IN MODULAR ARITHMETIC 3

(2) (Minimality) The powers 1, a, a2, . . . , an−1 mod m are distinct.

Theorem 2.1. Let a mod m have order n. For k ≥ 0, ak ≡ 1 mod m if and only if n | k.

Proof. If n | k, say k = nn′, then ak = ann′ = (an)n′ ≡ 1 mod m since an ≡ 1 mod m.
Now assume ak ≡ 1 mod m. We want to prove n | k. Using division with remainder we
can write k = nq + r where q and r are integers and 0 ≤ r < n. Our goal is to show r = 0.
We have ak = a
nq+r = (an)qa
r =⇒ a
k ≡ (a
n)
qar mod m.

The left side of the congruence is 1 by hypothesis and an ≡ 1 mod m by part of the deﬁnition
of n being the order of a mod m. Therefore the congruence becomes 1 ≡ ar mod m. Since
0 ≤ r < n and n is the least positive exponent that makes a power of a congruent to
1 mod m, r is not positive. Thus r = 0, so k = nq, which says n | k. □

Corollary 2.2. If (a, m) = 1 and a mod m has order n then n | ϕ(m).

Proof. By Euler’s theorem, aϕ(m) ≡ 1 mod m. Now apply Theorem 2.1. □

Example 2.3. Suppose a ̸≡ 0 mod 19. Since 19 is prime, we have (a, 19) = 1 and ϕ(19) =
18, so a18 ≡ 1 mod 19. Thus the order of a mod 1 divides 18, so it is 1, 2, 9, or 18. Let’s
use this to determine the order of 2 mod 19. Certainly it is not 1. It is not 2 either, since
22 = 4 ̸≡ 1 mod 19. Could the order be 9? We can ﬁnd 29 by repeated multiplication by 2,
starting from the familiar power 25:

25 = 32 ≡ 13 ≡ −6 mod 19 =⇒ 2
6 ≡ −12 ≡ 7 mod 19

=⇒ 2
9 = 2
3 · 2
6 ≡ 8 · 7 = 56 ≡ −1 mod 19.

Thus 29 ̸≡ 1 mod 19. The order of 2 mod 19 is not 1, 2, or 9, so it has to be 18. We don’t
have to check this directly since we have instead eliminated all the other potential options.

When an ≡ 1 mod m, the powers of a mod m repeat themselves every n turns: for any
integers q ≥ 0 and ℓ ≥ 0,

(2.1) a
ℓ+nq = aℓanq = a
ℓ(an)q ≡ a
ℓ(1
q) ≡ aℓ mod m.

This next theorem and corollary show this repetition doesn’t happen more often than every
n turns.

Theorem 2.4. Let a mod m have order n. For integers k and ℓ ≥ 0, ak ≡ aℓ mod m if
and only if k ≡ ℓ mod n.

Proof. Without loss of generality, k ≤ ℓ. Since a mod m is invertible,

(2.2) a
k ≡ aℓ mod m ⇐⇒ a
k ≡ akaℓ−k mod m ⇐⇒ a
ℓ−k ≡ 1 mod m,

and Theorem 2.1 says aℓ−k ≡ 1 mod m if and only if n | (ℓ − k), or k ≡ ℓ mod n. □

Corollary 2.5. Let a mod m have order n. Then every power of a mod m is ar mod m for
a unique r from 0 to n − 1.

Proof. This will be another application of division with remainder.
Given an arbitrary power ak, write k = nq + r where 0 ≤ r ≤ n − 1. Then ak ≡ ar mod m
by (2.1) with ℓ = r. Thus every power of a mod m is ar mod m where 0 ≤ r ≤ n − 1. If
0 ≤ r < s ≤ n − 1 then we ar ̸≡ as mod m because r ̸≡ s mod n (Theorem 2.4). □

4 KEITH CONRAD

We have shown the powers 1, a, a2, . . . , an−1 mod m are distinct from one another and
describe all possible powers of a mod m without repetition. This gives a nice combinatorial
interpretation of the order of a mod m: it is the number of distinct powers of a mod m. For
example, 2 mod 7 has order 3 and there are 3 diﬀerent powers of 2 mod 7.

3. Orders of powers

When a mod m has order n, what is the order of a power ak mod m? Since (ak)n =
(an)k ≡ 1k ≡ 1 mod m, the order of ak mod m divides n by Theorem 2.1. Which factor of
n is it?

Example 3.1. Suppose a mod m has order 12, so a12 ≡ 1 mod m and ai ̸≡ 1 mod m for
i = 1, 2, . . . , 11. Any power of a mod m has order that is a factor of 12. It is plausible
that a2 mod m has order 6: since a mod m takes 12 powers until it ﬁrst cycles around to
1, a2 mod m takes only 6 powers to get there. Thus a2 mod m has order 6 = 12/2. On the
other hand, it is absurd to say a8 mod m has order 12/8, as 12/8 is not an integer. The
successive powers of a8 mod m are

a8 ̸≡ 1 mod m, (a
8)2 = a16 ≡ a
4 ̸≡ 1 mod m, (a
8)
3 = a
24 = (a
12)
3 ≡ 1
3 ≡ 1 mod m,

so a8 mod m has order 3, which we can write as 12/4. What we divide 12 by to get the
order of a8 mod m is not 8, but the largest factor that 8 has in common with 12, namely 4.

Theorem 3.2. Let a mod m have order n and k be a positive integer.
(1) If k | n then ak mod m has order n/k.
(2) If (k, n) = 1 then ak mod m has order n. That is, raising a mod m to a power
relatively prime to its order doesn’t change the order.
(3) For general k ∈ Z+, ak mod m has order n/(k, n).

The third part includes the ﬁrst two parts as special cases (if k | n then n/(k, n) = n/k,
and if (k, n) = 1 then n/(k, n) = n), but we state those special cases separately because
they are worth knowing on their own and because they can be proved independently of the
general case. Understanding the proof of the ﬁrst two parts of the theorem will help you
better understand the proof of the third part. Basic to everything will be Theorem 2.1.

Proof. Let t be the (unknown) order of ak mod m, so (ak)t ≡ 1 mod m and t is the minimal
positive exponent that ﬁts this congruence. We want to show t = n/k if k | n, t = n if
(k, n) = 1, and t = n/(k, n) in general.
1) We assume k | n. The condition (ak)t ≡ 1 mod m is the same as akt ≡ 1 mod m, so
n | kt by Theorem 2.1. Thus n ≤ kt, so n/k ≤ t. We also have the reverse inequality: since
(ak)n/k = ak(n/k) = an ≡ 1 mod m, t ≤ n/k by the deﬁnition of what the order of a unit is.
From n/k ≤ t and t ≤ n/k, we have t = n/k.
2) We assume (k, n) = 1 and want to show ak mod m has order n.
The equation (ak)t ≡ 1 mod m is the same as akt ≡ 1 mod m, so n | kt by Theorem 2.1.
Since n and k are relatively prime, from n | kt we conclude that n | t, so n ≤ t. We have
the reverse inequality too: (ak)n = akn = (an)k ≡ 1k ≡ 1 mod m, so t ≤ n by the deﬁnition
of the order of a unit. Therefore t = n.
3) In the general case, for each k ≥ 1 we want to show t = n/(k, n). The congruence
(ak)t ≡ 1 mod m is the same as akt ≡ 1 mod m, which is the same as n | kt by Theorem
2.1. So t is the smallest positive integer such that n | kt.

ORDERS OF UNITS IN MODULAR ARITHMETIC 5

Factor (k, n) out of both k and n: set k = (k, n)k′ and n = (k, n)n′ with k′, n′ ∈ Z. Then
(k′, n′) = 1. We have
 n | kt =⇒ (k, n)n′ | (k, n)k′t =⇒ n′ | k′t.

Since (k′, n′) = 1, we get n′ | t, so n′ ≤ t.
We have the reverse inequality too:

(a
k)
n′ = akn′ !
= a
nk′ = (an)
k′ ≡ 1
k′ ≡ 1 mod m.

Let’s explain the equality with the exclamation point: kn′ = nk′ since both products
equal kn/(k, n). From (ak)n′ ≡ 1 mod m we have t ≤ n′. Earlier we saw n′ ≤ t, so
t = n′ = n/(k, n) and we are done. □

Example 3.3. If a mod m has order 12, here is a list of orders of powers of a mod m. The
order of ak mod m is equal to 12/(k, 12). Compute successive powers of ak mod m for each
k to verify directly that the values in the table are correct.
k 1 2 3 4 5 6 7 8 9 10 11 12
order of ak mod m 12 6 4 3 12 2 12 3 4 6 12 1

Example 3.4. If a mod m has order 12 then ak mod m has order 12 precisely when
(k, 12) = 1. Look at the table above and notice 12 appears under k = 1, 5, 7, and 11,
which are relatively prime to 12.

4. Applications of orders

As a ﬁrst application of orders, we determine all consecutive powers of 2 and 3.

Theorem 4.1. The consecutive powers of 2 and 3 in Z+ are (1, 2), (2, 3), (3, 4), and (8, 9).

Proof. The condition that 2m and 3n (where m and n are nonnegative integers) are consec-
utive is that 2m − 3n = 1 or 3n − 2m = 1. In both cases we will list the solutions for small
m and then prove there are no solutions for larger m.
Case 1: 2m − 3n = 1. Letting m = 0, 1, 2 and trying to solve for n, the only solutions are
(2m, 3n) = (2, 1) and (4, 3). We want to show there is no solution when m ≥ 3. If m ≥ 3
then 2m is divisible by 8, so
 3
n = 2
m − 1 ≡ −1 ≡ 7 mod 8.

This is impossible: since 32 ≡ 1 mod 8, we have 3even ≡ 1 mod 8 and 3odd ≡ 3 mod 8, so
the powers of 3 mod 8 do not include 7 mod 8. (This did not use anything about orders.
The next case will.)
Case 2: 3n − 2m = 1. Letting m = 0, 1, 2, 3 and trying to solve for n, the only solutions
are (2m, 3n) = (2, 3) and (8, 9). To show there are no solutions when m ≥ 4, write

3
n = 1 + 2m ≡ 1 mod 16.

Check yourself that the order of 3 mod 16 is 4. Then 4 | n, say n = 4ℓ, so

(4.1) 2
m = 3
n − 1 = 3
4ℓ − 1 = 81
ℓ − 1.

However, 81ℓ − 1 is divisible by 5 (indeed, 81 ≡ 1 mod 5 ⇒ 81ℓ ≡ 1 mod 5), so (4.1) is
impossible because the right side is divisible by 5 and the left side is a power of 2. □

6 KEITH CONRAD

For our second application, we will factor 232 + 1. Here is the background context. The
values of 22k + 1 when k = 0, 1, 2, 3, 4 are 3, 5, 17, 257, and 65537, which are all prime. In
1640, Fermat claimed that 22k + 1 is prime for all k ≥ 0. This was disproved almost 100
years later by Euler [2], in the 1730s, when he pointed out that 232 + 1 = 4,294,967,297
is divisible by 641. (Keep in mind that all calculations at that time were done by hand.)
Explicitly, 2
32 + 1 = 4,294,967,297 = 641 · 6700417.

No prime values of 22k + 1 when k ≥ 5 have ever been found, and it is now widely believed
that 22k + 1 is never prime when k ≥ 5.
Euler did not discover 641 divides 232 + 1 by a brute force divisibility check using 2, 3, . . .
until he reached 641. What he did can be explained in modern terms using orders.

Theorem 4.2. The number 232 + 1 is divisible by 641.

Proof. Let p be a prime factor of 232 + 1: p | (232 + 1) implies 232 ≡ −1 mod p, so (square
both sides) 264 ≡ 1 mod p. That implies the order of 2 mod p divides 64. Since proper
factors of 64 divide 32 and 232 ≡ −1 ̸≡ 1 mod p, 2 mod p has order 64. Thus 64 | (p − 1) by
Fermat’s little theorem, so p = 64n + 1 for some n ≥ 1. This means the only primes even
worth testing as factors of 232 + 1 are primes of the form 64n + 1. The table below says
64n + 1 is not prime when n = 1, 2, 5, 6, and 8 since these 64n + 1 are divisible by 3 or 5.

n 1 2 3 4 5 6 7 8 9 10
64n + 1 65 129 193 257 321 385 449 513 577 641
a factor 5 3 ? ? 3 5 ? 3 ? ?

When n = 3, 4, 7, 9, and 10, Euler could check by hand whether 64n + 1 divides 232 + 1 =
4,294,967,297, so he only needed to carry out ﬁve divisibility calculations. Divisibility fails
at the ﬁrst four n but there is divisibility at n = 10, thus revealing 641 to be a factor:
(232 + 1)/641 = 4,294,967,297/641 = 6700417. □

Remark 4.3. The argument above that p | (232 + 1) implies p ≡ 1 mod 64 generalizes to
show for all k ≥ 0 that p | (22k + 1) implies p ≡ 1 mod 2k+1. Euler knew this. In the 1870s,
the mathematician Lucas improved the conclusion to p ≡ 1 mod 2k+2 if k ≥ 2. When k = 5
this means prime factors of 232 + 1 satisfy p ≡ 1 mod 128, not just p ≡ 1 mod 64, which
lets us reach the prime 641 = 128 · 5 + 1 in two steps rather than ﬁve, since 128n + 1 is not
prime when n = 1, 3, and 4, as in these cases 128n + 1 is a multiple of 3 or 5.

Fermat’s little theorem and its consequences (like the Fermat test) show the importance
of considering an−1 ≡ 1 mod n. Could we ever have an ≡ 1 mod n? Using a computer it’s
not hard to ﬁnd 3n ≡ 1 mod n when n = 1, 2, 4, 8, 16, 20, 32, 40, . . ., 4n ≡ 1 mod n when
n = 1, 3, 9, 21, 27, 63, 81, 147, . . ., and 5n ≡ 1 mod n when n = 1, 2, 4, 6, 8, 12, 16, 18, . . ., but
the case a = 2 is diﬀerent and this will be our second application of orders.

Theorem 4.4. There is no n > 1 for which 2n ≡ 1 mod n.

Proof. Suppose 2n ≡ 1 mod n. Let p be the smallest prime factor of n, so p is the smallest
factor of n that’s greater than 1.
Let m be the order of 2 mod p. Since 2n ≡ 1 mod n =⇒ 2n ≡ 1 mod p we have m | n.
Also m | (p − 1), so m ≤ p − 1. The only factor of n less than p is 1, so m = 1. Thus the
condition 2m ≡ 1 mod n becomes 2 ≡ 1 mod n, so n = 1. □

ORDERS OF UNITS IN MODULAR ARITHMETIC 7

The base 2 in this theorem is the only one that ﬁts: for each a > 2 there are inﬁnitely
many n > 1 for which an ≡ 1 mod n: use n = (a − 1)k for all k ≥ 1.
Our next application of orders, which is the original reason mathematicians became
interested in them, is their link to periodic decimal expansions. A decimal expansion is called
periodic if from some point onwards it has a repeating block of digits, and purely periodic
if the repeating block occurs right from the start. For example, 4/27 = .148148148 . . . is
purely periodic while 19/54 = .3518518518 . . . is periodic but not purely periodic. The
period length of a repeating decimal is the number of digits in its smallest repeating block,
so the decimal expansions of 4/27 and 19/54 have period length 3.1

Theorem 4.5. Every purely periodic decimal expansion is a rational number between 0 and
1 with denominator relatively prime to 10, and conversely all such rational numbers have
purely periodic decimal expansions. Moreover, if a/b is in reduced form between 0 and 1
with (10, b) = 1 then the period length of its decimal expansion is the order of 10 mod b. In
particular, the period length of a/b divides ϕ(b) and is independent of a.

Proof. We start by writing a purely periodic decimal as a fraction. If x = .c1c2. . .cd has a
periodic block of d terms then the digit c1 occurs in positions for 10−1, 10−(d+1), 10−(2d+1),
and so on, the digit c2 occurs in positions 10−2, 10−(d+2), 10−(2d+2), and so on, so

x = c1 ∑

k≥0
 1
10dk+1 + c2 ∑

k≥0
 1
10dk+2 + · · · + cd ∑

k≥0
 1
10dk+d

= ( c1
10 + c2
102 + · · · + cd
10d
 ) ∑

k≥0
 1
10dk

= ( c1
10 + c2
102 + · · · + cd
10d
 ) 1
1 − 1/10d ,

by the formula for the sum of a geometric series. Rewriting 1/(1 − 1/10d) as 10d/(10d − 1)
and multiplying through the ﬁrst factor in the numerator with the 10d, we get

x = c110d−1 + c210d−2 + · · · + cd
10d − 1 .

This is a fraction between 0 and 1 with denominator relatively prime to 10.
Conversely, suppose a/b is rational between 0 and 1 with (10, b) = 1. If b = 10d − 1
for some d then we could run the calculations above in reverse to show a/b has a purely
periodic decimal expansion. Most b where (10, b) = 1 do not usually have the form 10d − 1
for some d, but we can rewrite a/b to give it such a denominator: since (10, b) = 1 we have
10ϕ(b) ≡ 1 mod b by Euler’s theorem, so 10ϕ(b) − 1 = bc for some integer c. Then
a
b = ac
bc = ac
10ϕ(b) − 1 .

This fraction is between 0 and 1 with denominator 10ϕ(b) − 1, so calculations at the start of
the proof can be read in reverse to show the fraction has a purely periodic decimal expansion
with a repeating part of ϕ(b) digits. (If ac has fewer than ϕ(b) base 10 digits, append 0’s
to the front of it; see Examples 4.7 and 4.8.)
A repeating part with ϕ(b) digits may not be the smallest repeating part. When the
smallest repeating part has d digits, d is the smallest positive integer for which a/b can

1Logically speaking, 4/27 = .148148 . . . could be said to have a repeating block “148148” of length 6.
The period length is the minimal possible size of a repeating part.

8 KEITH CONRAD

be given the denominator 10d − 1. Since a/b is in reduced form, its possible denominators
are multiples of b, so its decimal period length is the smallest d ≥ 1 for which 10d − 1 is a
multiple of b, or equivalently 10d ≡ 1 mod b. The least d is the order of 10 mod b, which
divides ϕ(b) by Theorem 2.1. □

Example 4.6. The order of 10 mod 27 is 3: 101 ≡ 10 mod 27, 102 = 100 ≡ 19 mod 27,
103 = 190 ≡ 1 mod 27. Therefore every reduced fraction a/27 has a decimal period length
3. For example, to ﬁnd the decimal of 20/27 we rewrite the fraction to have denominator
103 − 1: 20
27 = 20(103 − 1)/27
103 − 1 = 20(37)
103 − 1 = 740
103 − 1 .

Since the numerator is 740, the proof of Theorem 4.5 tells us 20/27 = .740.

Example 4.7. The order of 10 mod 57 is 18, so 1/57 has decimal period length 18. Ex-
plicitly,
 1
57 = (1018 − 1)/57
1018 − 1 =
 17 digits
︷ ︸︸ ︷
17543859649122807
1018 − 1 = .017543859649122807.

The initial 0 occurs since the decimal period length is 18 but (1018 − 1)/57 has 17 digits.

Example 4.8. The order of 10 mod 239 is 7, so 2/239 has decimal period length 7. Ex-
plicitly, 2
239 = 2(107 − 1)/239
107 − 1 = 83682
107 − 1 = .0083682.

Two initial 0’s occur since the decimal period length is 7 while 2(107 − 1)/239 has 5 digits.

Remark 4.9. Fractions a/b and a′/b with the same denominator are guaranteed to have
the same decimal period length when they are both in reduced form
2 but reduced and
non-reduced fractions with the same denominator could have diﬀerent decimal periods:
1/21 = .047619 has decimal period 6 while 7/21 = 1/3 = .3 does not.

If (10, b) = 1 then the decimal period length of 1/b divides ϕ(b). Since ϕ(b) = b − 1 if b is
prime and ϕ(b) < b − 1 if b is composite, the decimal period length of 1/b can be b − 1 only
for prime b (other than 2 and 5), and this happens if and only if 10 mod b generates the
units mod b. When b < 100, this occurs for b = 7, 17, 19, 23, 29, 47, 59, 61, 97. For example,

1
7 = .142857︸ ︷︷ ︸
6 digits , 1
17 = .0588235294117647︸ ︷︷ ︸
16 digits , 1
19 = .052631578947368421︸ ︷︷ ︸
18 digits .

It is believed that 10 mod p has order p − 1 for inﬁnitely many primes p, or equivalently
1/p has decimal period length p − 1 for inﬁnitely many primes p. This is a special case of
Artin’s primitive root conjecture, which will be described at the end of Section 6.
Everything we have done with decimal expansions in base 10 can be carried over with no
essential changes to others bases, provided the fraction has a denominator relatively prime
to the base. For example, using base 2, a reduced fraction a/b with odd denominator has
binary period length equal to the order of 2 mod b.

2More generally, the decimal period lengths are equal when (a, b) = (a
′, b).

ORDERS OF UNITS IN MODULAR ARITHMETIC 9

Example 4.10. The order of 10 mod 11 is 2 while the order of 2 mod 11 is 10, so 1/11 has
decimal period length 2 and binary period length 10:

1
11 = (102 − 1)/11
102 − 1 = 9
102 − 1 = .09

and
 1
11 = (210 − 1)/11
210 − 1 = 93
210 − 1 =
 7 digits
︷ ︸︸ ︷
10111012
210 − 1 = .0001011101.

5. Order of products

How is the order of a product a1a2 mod m related to the orders of the factors a1 mod m
and a2 mod m? In this generality not much can be said!

Example 5.1. Suppose a mod m has order 5. Then a4 mod m, the inverse of a mod m,
has order 5 and a2 mod m also has order 5, but the product aa4 ≡ 1 mod m has order 1
while the product aa2 = a3 mod m has order 5.

When the orders of a1 mod m and a2 mod m are relatively prime, we can say exactly
what the order of a1a2 mod m is:

Theorem 5.2. Let a1 mod m and a2 mod m have respective orders n1 and n2. If (n1, n2) =
1 then a1a2 mod m has order n1n2.

In words, for units with relatively prime orders, the order of their product is the product
of their orders.

Proof. Since
 (a1a2)
n1n2 = an1n2
1 a
n1n2
2 = (an1
1 )n2(an2
2 )n1 ≡ 1 · 1 ≡ 1 mod m,

we see a1a2 mod m has order dividing n1n2 by Theorem 2.1.
Let n be the order of a1a2 mod m. In particular, (a1a2)n ≡ 1 mod m. From this we will
show n1 | n and n2 | n. Since

(5.1) an
1 an
2 ≡ 1 · 1 ≡ 1 mod m,

raising both sides of (5.1) to the power n2 (to kill oﬀ the a2 factor) gives us

a
nn2
1 ≡ 1 mod m.

Therefore n1 | nn2 by Theorem 2.1. Since (n1, n2) = 1, we conclude n1 | n. Now raising
both sides of (5.1) to the power n1 gives a
nn1
2 ≡ 1 mod m, so n2 | nn1 by Theorem 2.1, and
thus n2 | n.
Since n1 | n, n2 | n, and (n1, n2) = 1, we conclude that n1n2 | n. Since we already showed
n | n1n2 (in the ﬁrst paragraph of the proof), we conclude n = n1n2. □

Example 5.3. Mod 21, −1 has order 2 and 4 has order 3. Therefore −4 = 17 has order 6.

Example 5.4. If a1 mod m has order 5 and a2 mod m has order 8, then a1a2 mod m has
order 40.

Corollary 5.5. If a1, . . . , ar mod m are units with orders n1, . . . , nr and the ni are pairwise
relatively prime, then the product a1 · · · ar mod m has order n1 · · · nr.

Proof. Induct on r, with Theorem 5.2 being the case r = 2. Details are left to the reader. □

10 KEITH CONRAD

Remark 5.6. While Theorem 5.2 shows that a product of units with relatively prime orders
has a predictable order, what can be said if we start with a mod m of order n and write
n = n1n2 where (n1, n2) = 1: is a mod m a product of units with orders n1 and n2? The
answer is yes, and those units are unique.
Suppose a ≡ a1a2 mod m where a1 mod m has order n1 and a2 mod m has order n2.
Therefore an1 ≡ a
n1
2 mod m and an2 ≡ a
n2
1 mod m. To remove the exponents on a2 and a1
we want to raise to an additional power that is an inverse of the exponent modulo the order
of a2 or a1. In powers of a1 the exponent only matters modulo n1, and in powers of a2 the
exponent only matters modulo n2. Since (n1, n2) = 1, n1x + n2y = 1 for some x, y ∈ Z, so
n1x ≡ 1 mod n2 and n2y ≡ 1 mod n1. Thus

a
n1 ≡ a
n1
2 mod m =⇒ an1x ≡ an1x
2 ≡ a2 mod m,

a
n2 ≡ an2
1 mod m =⇒ an2y ≡ an2y
1 ≡ a1 mod m,
so we solved for a1 mod m and a2 mod m as particular powers of a mod m. Conversely,
a = a1 = an1x+n2y = (an2y)(an1x) where an2y mod m has order n1 while an1x mod m has
order n2.

Dropping the assumption that n1 and n2 are relatively prime, a1a2 mod m has order
dividing n1n2 since (a1a2)n1n2 = a
n1n2
1 a
n1n2
2 ≡ 1 · 1 ≡ 1 mod m. More precisely, the order
of a1a2 mod m divides the least common multiple [n1, n2]: (a1a2)[n1,n2] = a
[n1,n2]
1 a
[n1,n2]
2 ≡
1 · 1 ≡ 1 mod m. For example, if a1 mod m has order 6 and a2 mod m has order 4, then
a1a2 mod m has order dividing 12, not just 24.
The least common multiple is not just an upper bound on the order of a product of two
units, but can be realized as the order of some product of their powers:

Corollary 5.7. Let a1 mod m and a2 mod m be two units with respective orders n1 and
n2. For some positive integers k1 and k2, ak1
1 ak2
2 has order [n1, n2].

Proof. The basic idea is to write [n1, n2] as a product of two relatively prime factors and
then ﬁnd exponents k1 and k2 such that ak1
1 mod m and a
k2
2 mod m have orders equal to
those factors. Then the order of a
k1
1 mod m and ak2
2 mod m will be equal to the product of
the factors (Theorem 5.2), which is [n1, n2] by design.
Here are the details. Factor n1 and n2 into primes:

n1 = p
e1
1 · · · per
r , n2 = p
f1
1 · · · pfr
r .

We use the same list of (distinct) primes in these factorizations, and use an exponent 0 on
a prime that is not a factor of one of the integers. The least common multiple is

[n1, n2] = pmax(e1,f1)
1 · · · pmax(er,fr)
r .

Break this into a product of two factors, one being a product of the prime powers where
ei ≥ fi and the other using prime powers where ei < fi. Call these two numbers ℓ1 and ℓ2:

ℓ1 = ∏

ei≥fi pei
i , ℓ2 = ∏

ei<fi p
fi
i .

Then [n1, n2] = ℓ1ℓ2 and (ℓ1, ℓ2) = 1 (since ℓ1 and ℓ2 have no common prime factors).
By construction, ℓ1 | n1 and ℓ2 | n2. Then a
n1/ℓ1
1 mod m has order ℓ1 and a
n2/ℓ2
2 mod m
has order ℓ2. Since these orders are relatively prime and the two powers of a1 mod m and
a2 mod m commute with each other, an1/ℓ1
1 a
n2/ℓ2
2 mod m has order ℓ1ℓ2 = [n1, n2]. □

ORDERS OF UNITS IN MODULAR ARITHMETIC 11

Example 5.8. Suppose a1 mod m has order n1 = 60 = 22 · 3 · 5 and a2 mod m has order
n2 = 630 = 2 · 32 · 5 · 7. Then [n1, n2] = 22 · 32 · 5 · 7. We can write this as (22 · 5) · (32 · 7),
where the ﬁrst factor appears in n1, the second in n2, and the factors are relatively prime.
Then a3
1 mod m has order 22 · 5 and a10
2 mod m has order 32 · 7 (why?). These orders are
relatively prime, so a3
1a10
2 mod m has order 22 · 5 · 32 · 7 = [n1, n2].
Since the same power of 5 appears in both n1 and n2, there is another factorization of
[n1, n2] we can use: placing the 5 in the second factor, we have [n1, n2] = (22)(32 · 5 · 7).
Then a15
1 mod m has order 22 and a2
2 mod m has order 32 · 5 · 7 (why?). These orders are
relatively prime, so a15
1 a2
2 mod m has order 22 · 32 · 5 · 7 = [n1, n2].

6. A generating unit modulo a prime

For some m ≥ 2, there is a unit mod m whose order is ϕ(m): its powers ﬁll up all the
units.

Example 6.1. The order of 3 mod 7 is 6 = ϕ(7) and every unit mod 7 is a power of 3. We
can see this in the row of powers of 3 mod 7 in the table in Example 1.1.

Example 6.2. The order of 2 mod 9 is 6 = ϕ(9): the powers of 2 mod 9 are 2, 4, 8, 7, 5,
1, which are all the units mod 9.

A unit mod m whose order is ϕ(m) is called a generator or primitive root mod m. For
instance, Examples 6.1 and 6.2 tell us that 3 is a generator mod 7 and 2 is a generator mod
9. Example 1.2 shows there is no generator for modulus 15 since there are 8 units modulo
15 and their orders are 1, 2, or 4.
In a 1769 paper on decimal expansions, Lambert [6] conjectured that the units modulo
a prime always have a generator. A proof was given by Euler in 1774 [3, Art. 37, 38],
Legendre in 1785 [7, pp. 471–473], and Gauss in 1801 [4, Art. 52–55]. Gauss went farther
than anyone else by classifying all m ≥ 2 such that the units mod m have a generator:
2, 4, pk, and 2pk for odd primes p. We will focus just on the case of a prime modulus.

Theorem 6.3. When p is a prime, there is a unit mod p with order p − 1.

A common feature of all proofs of this theorem is that they are not constructive. There
is no algorithm known for ﬁnding a generator of (Z/(p))× that is substantially faster than
a brute force search: try a = 2, 3, . . . until you ﬁnd an element with order p − 1. What
makes Theorem 6.3 important, despite its nonconstructive nature, is that it guarantees a
brute force search will eventually succeed.
3

Theorem 6.3 is important not only in pure mathematics, but also in cryptography. A
choice of generator for (Z/(p))× is one of the ingredients in two public key cryptosystems:
Diﬃe-Hellman (this is the original public key system, if we discount earlier classiﬁed work
by British intelligence) and ElGamal. You can look up these cryptosystems online.
We are now ready to prove Theorem 6.3.

Proof. Step 1: We have the following equality in (Z/(p))[T ]:

T p−1 − 1 = (T − 1)(T − 2) · · · (T − (p − 1)).

Fermat’s little theorem tells us T p−1 − 1 has roots 1, 2, . . . , p − 1 mod p. Therefore in
(Z/(p))[T ], T p−1 − 1 is divisible by T − 1, T − 2, . . . , T − (p − 1). These linear factors are

3The Generalized Riemann Hypothesis implies a brute force search runs in polynomial time in log p.

12 KEITH CONRAD

pairwise relatively prime, so in (Z/(p))[T ]

T p−1 − 1 = (T − 1)(T − 2) · · · (T − (p − 1))h(T )

for some polynomial h(T ). Computing the degrees of both sides shows deg h = 0, so h(T )
is a nonzero constant. Then looking at leading coeﬃcients on both sides shows h(T ) = 1,
and we’re done.

Step 2: If d and n are positive integers with d | n then (T d − 1) | (T n − 1).
Let n = dd′. Then T n − 1 = T dd′ − 1 = (T d)d′ − 1.
The polynomial T d′ − 1 has 1 as a root, so it is divisible by T − 1:

T d′ − 1 = (T − 1)g(T ).

(Explicitly, g(T ) = T d′−1 + T d′−2 + · · · + T + 1.) Substituting T d for T in this polynomial
equation, we get T n − 1 = (T d − 1)g(T d),
showing T d − 1 is a factor of T n − 1.

Step 3: For each prime power qe that divides p − 1, there is a unit mod p with order qe.
That a unit a mod p has order qe is is the same as saying

a
qe ≡ 1 mod p, a
qe−1 ̸≡ 1 mod p.

This means a mod p is a root of T qe − 1 and is not a root of T qe−1 − 1. And that is what
we will do: show T qe − 1 has a root in Z/(p) that is not a root of T qe−1 − 1.
From Step 2, with d = qe and n = p − 1, T p−1 − 1 is divisible by T qe − 1. Since
T p−1 − 1 in (Z/(p))[T ] is a product of T − 1, T − 2, . . . , T − (p − 1) by Step 1, any monic
factor of T p−1 − 1 in (Z/(p))[T ] must be a product of some of these linear factors (unique
factorization!). Therefore T qe − 1 has qe distinct roots in Z/(p), and by similar reasoning
T qe−1 − 1 has qe−1 distinct roots in Z/(p). As qe > qe−1, there must be an integer mod p
that is a root of T qe − 1 and not a root of T qe−1 − 1.

Step 4: There is an integer mod p that has order p − 1.
Write p − 1 as a product of primes:

p − 1 = qe1
1 qe2
2 · · · qer
r .

By Step 3, there is a unit ai mod p with order qei
i . Then Corollary 5.5 tells us a1 · · · ar mod p
has order qe1
1 qe2
2 · · · qer
r = p − 1. □

Is each integer a other than 0, 1, −1 a generator modulo p for inﬁnitely many primes p?
Not if a is a perfect square: for odd primes p, if a = b2 in Z then a(p−1)/2 = bp−1 ≡ 1 mod p,
so a mod p has order at most (p − 1)/2. Emil Artin conjectured in 1927 that for all other
integers a (not 0, ±1, or perfect squares) the answer is yes. This is called Artin’s primitive
root conjecture, and Hooley [5] showed in 1967 that this conjecture is a consequence of the
Generalized Riemann Hypothesis.
 References

[1] M. Bullynck, Decimal periods and their tables: a German research topic (1765–1801), Historia Mathe-
matica 36 (2009), 137–160. URL https://halshs.archives-ouvertes.fr/halshs-00663295/document.
[2] L. Euler, “Observationes de theoremate quodam Fermatiano aliisque ad numeros primos spec-
tantibus,” Commentarii academiae scientiarum Petropolitanae, 6 (1738), 103–107. URL https://
scholarlycommons.pacific.edu/euler-works/26.

ORDERS OF UNITS IN MODULAR ARITHMETIC 13

[3] L. Euler, “Demonstrationes circa residua ex divisione potestatum per numeros primos resultan-
tia,” Novi Commentarii academiae scientiarum Petropolitanae 18 (1773), 85–135. URL https://
scholarlycommons.pacific.edu/euler-works/449/.
[4] C. F. Gauss, Disquisitiones Arithmeticae, translated by A. A. Clarke, Yale Univ. Press, New Haven,
1966.
[5] C. Hooley, On Artin’s conjecture, J. Reine Angew. Math. 225 (1967), 209–220.
[6] J. H. Lambert, “Adnotata quaedam de numeris eorumque anatomia,” Nova Acta Eruditorum LXIX
(1769), 107–128.
[7] A. M. Legendre, “Recherches d’Analyse Ind´etermin´ee,” M´emoires de Math´ematiques et de Physique
de l’Acad´emie Royale des Sciences de Paris (1785), 465–559. URL https://gallica.bnf.fr/
ark:/12148/bpt6k35847/f649.image.
