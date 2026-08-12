<!-- source: https://biology.kenyon.edu/HHMI/posters_2014/weinerz.pdf | converted from PDF -->

Searching for and Characterizing Abundancy Outlaws

Zach Weiner1 and Judy Holdener
1

1Dept. Of Mathematics, Kenyon College

Abstract

For a positive integer n, the abundancy index I(n) is deﬁned to be the

sum of its divisors divided by the number itself, or σ(n)/n. The function

I : N → Q ∩ (1, ∞) is not onto; rationals not in the range of I are
called “abundancy outlaws." Identifying and characterizing abundancy
outlaws could prove helpful to better understand the existence of odd
perfect numbers, a question over 2000 years old. In our research, we

consider rationals of the form (σ(n) + t)/n, where t is a positive integer,

to produce and characterize as-yet undiscovered outlaws.

Introduction

The study of the abundancy index is motivated by interest in perfect

numbers. A positive integer is a perfect number if it is equal to the sum
of its proper divisors. The smallest perfect number is 6 = 1 + 2 + 3,

followed by 28, 496, and 8128. Euclid showed that even numbers of the

form 2
p−1(2
p − 1) are perfect when p and 2
p − 1 are prime, while Euler

later showed that every even perfect number must have this form. Thus

we have a complete characterization for even perfect numbers: ﬁnding

one is equivalent to ﬁnding prime p such that 2
p − 1 is prime. Currently

there are 48 known perfect numbers—all of which are even. As a search
to 10300 found no odd perfect numbers, the question is whether it can

be proved that no odd perfect numbers exist.

The abundancy index has been studied as a means to ﬁnd such a proof,
which is deﬁned by I(n) = σ(n)/n, i.e., the ratio of the sum of the
divisors of n σ(n) = Σd|nd and n itself. An integer n having I(n) = 2
is perfect; for example, I(6) = (1 + 2 + 3 + 6)/6 = 2; integers having

other integer-valued indices are multiperfect. “Deﬁcient" n have index
less than 2 and “abundant" n have non-integer index greater than 2.

Thus, the abundancy index measures the “perfection" of a number.

Figure 1: Abundancy index of the ﬁrst 5,100 integers coded by color
 Abundancy Outlaws

As I : N → Q ∩ [1, ∞) is not onto, rationals not in the range of I are

termed abundancy outlaws. Finding outlaws is particularly important as

the existence of an odd perfect number is equivalent to the existence of

an abundancy index of a particular form [1]:

Theorem: There exists an odd perfect number if and only if there exist

positive integers p, n, and α such that p ≡ α ≡ 1 (mod 4), where p is

a prime not dividing n, and

I(n) = 2pα(p − 1)
pα+1 − 1 .

For example, if there exists n such that I(n) = 5/3, then 5n is an
odd perfect number. Thus, a proof that such rationals are abundancy

outlaws would prove that no odd perfect number exists.

Rationals of the form (σ(N ) + t)/N with t negative were characterized

by Paul Erdős, who proved that if (k, m) = 1 and m < k < σ(m), then

k/m is an abundancy outlaw. For example, 5/4 is an outlaw because

(5, 4) = 1 and 4 < 5 < σ(4) = 7.

Our research searched for outlaws of the same form with positive t.

Searching for Outlaws

The main search method utilized the theorem below, which requires the

following deﬁnition:

Deﬁnition: If m and n are positive integers, let mn denote the largest

divisor of m each of whose prime factors divide n.

Example: 6010 = (2
2 · 3 · 5)2·5 = 2
2 · 5 = 20

Theorem: Given a positive integer N , let v be such that I(v) is minimal

given the following:

(i) N |v

(ii) σ(v)N| (v/N ).

If t is a positive integer smaller than I(v)N −σ(N ) with (σ(N )+t, N ) =

1, then (σ(N ) + t)/N is an abundancy outlaw.

N σ(N ) v/N I(v) t < Outlaws

12 = 22 · 3 28 3 91/36 2.3 29/12

20 = 22 · 5 42 5 217/100 1.4 43/20

24 = 23 · 3 60 23 127/48 3.5 61/24

30 = 2 · 3 · 5 72 3 · 5 403/150 8.6 73/30, 77/30, 79/30

40 = 23 · 5 90 5 93/40 3 91/40

42 = 2 · 3 · 7 96 3 · 73 36413/14406 10.2 97/42, 101/42, 103/42

45 = 32 · 5 78 5 403/225 2.6 79/45

48 = 24 · 3 124 22 127/48 3 125/48

56 = 23 · 7 120 7 855/392 2.1 121/56

60 = 22 · 3 · 5 168 3 · 5 2821/900 20.1 169/60, 173/60, 179/60, 181/60, 187/60

66 = 2 · 3 · 11 144 3 · 11 1729/726 13.2 145/66, 149/66, 151/66, 155/66, 157/66

70 = 2 · 5 · 7 144 5 · 7 5301/2450 7.5 149/70, 151/70

72 = 23 · 32 195 2 403/144 6.5 197/72, 199/72

78 = 2 · 3 · 13 168 3 · 133 30941/13182 15.1 173/78, 175/78, 179/78, 181/78

80 = 24 · 5 186 2 189/80 3 187/80

84 = 22 · 3 · 7 224 3 · 7 247/84 23 227/84, 229/84, 233/84, 235/84, 239/84, 241/84

88 = 23 · 11 180 11 1995/968 1.4 181/88

90 = 2 · 32 · 5 234 32 · 5 3751/1350 16.1 239/90, 241/90, 247/90

96 = 25 · 3 252 23 511/192 3.5 253/96

99 = 32 · 11 156 11 1729/1089 1.2 157/99
Figure 2: Outlaws of the form (σ(N ) + t)/N for N < 100, with newly
discovered outlaws in purple.
 Characterizing Outlaws

In the results of our main search technique, we observe several patterns.
In particular, we are able to characterize an upper bound on t given

certain conditions on N :

Theorem: Let p be a prime and α ≥ 1 be odd. For integers m
and t, assume there exists prime q|p + 1 not dividing mt, and assume

(σ(pαm) + t, p
αm) = 1. If t < σ(m)/p, then σ(pαm)+t
pαm is an outlaw.

Theorem: Let p be a prime and α ≥ 2 be even. For integers m and t,

assume (σ(pα), mt) = 1 and that (σ(pαm)+t, p
αm) = 1. If there exists
prime q < p dividing σ(p) but not mt, then σ(p
αm)+t
pαm is an outlaw for

t < (1/p + 1/p2)σ(m). Otherwise σ(pαm)+t
pαm is an outlaw for t < σ(m)/p.

Theorem: Assume N = Πk
i=1pαi
i , with k > 1, and suppose t is a

positive integer satisfying:

(i) (σ(N ) + t, N ) = 1 and (t, σ(N )) = 1

(ii) t < min
 


 1
pjΠi̸=jσ(pαi
i )





k

j=1
(iii) t < σ(σ(N )) − σ(N ).

Then σ(N )+t
N is an outlaw.

The three results each ﬁnd a number of additional outlaws.

Limitations and Further Research

The main search technique is limited when (N, σ(N )) = 1, σ(N )N =
1|(nN/N ). Then v = N and t < I(N )N − σ(N ) = 0, so we
ﬁnd no outlaws. In particular, no outlaws are found for prime N as

(σ(N ) = N + 1, N ) = 1 Thus we are able to say nothing about rationals

of the form σ(p)+1
p = p+2
p , which have long eluded characterization. Thus
it seems new methods of searching for outlaws will be required to, for

example, determine whether 5/3 is an outlaw.
Our characterizations of outlaws also runs into diﬃculty when N is

divisible by 2 and 3, again suggesting the need for new machinery with

which to discover abundancy outlaws.

Acknowledgements and References

Thanks to Professor Judy Holdener, the Kenyon Summer Science Schol-

ars Program, and the Kenyon College Department of Mathematics.

[1] Holdener, Judy. “Conditions Equivalent to the Existence of Odd

Perfect Numbers.” Mathematics Magazine, Vol. 79, No. 5. (Dec.,

2006), pp. 389-291.

[2] Stanton, Will and Judy Holdener. “Abundancy ‘Outlaws’ of the

Form σ(N )+t
N ,” Journal of Integer Sequences, Vol 10 (2007),

Article 07.9.6.

[3] Weiner, Paul. “The Abundancy Ratio, a Measure of Perfection”.

Mathematics Magazine, Vol. 73, No. 4. (Oct., 2000), pp.

307-310.

[4] Laatsch, Richard. “Measuring the Abundancy of Integers”.

Mathematics Magazine, Vol. 59 (1986), pp. 84-92.

Searching for and Characterizing Abundancy Outlaws
