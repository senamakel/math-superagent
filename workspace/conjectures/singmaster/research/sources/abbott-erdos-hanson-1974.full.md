<!-- source: https://www.renyi.hu/~p_erdos/1974-23.pdf | converted from PDF -->

(1)
 ON THE NUMBER OF TIMES AN INTEGER OCCURS
AS A BINOMIAL COEFFICIENT

H . L. ABBOTT, P . ERDőS, AND D . HANSON

Let N(t) denote the number of times the integer t > 1 occurs as a binomial co-

efficient ; that is, N(t) is the number of solutions of t = ( n in integers n and r.
r

We have N(2) = 1, N(3) = N(4) = N(5) = 2, N(6) = 3, etc . In a recent note in the

research problems section of the MONTHLY, D . Singmaster [1] proved that

N(t) = O(log t).

He conjectured that N(t) = 0(1) but pointed out that this conjecture, if it is in fact

true, is perhaps very deep . In [1] and [5], Singmaster points out that N(t) = 6 for

the following values of t <_ 248 ; t = 120, 210, 1540, 7140, 11628 and 24310 . It has

been shown by Singmaster [5] and D . Lind [6] that N(t) >_ 6 inflaitely often . Sing-

master has verified that the only value of t <_ 2 48 for which N(t) >_ 8 is t = 3003,

for which N(t) = 8.

In this note we obtain some additional information about the behavior of N(t) .

In Theorem 1 we prove that the average and normal order of N(t) is 2 ; in fact, we

prove somewhat more than this, namely, the number of integers t, 1 < t 5 x, for

which N(t) > 2 is 0( \/x). (See [4] p . 263 and p . 356, for the definitions of average

and normal order .) In Theorem 2 we give an upper bound for N(t) in terms of the

number of distinct prime factors of t . Our main result is Theorem 3, in which we

show that (1) can be improved to N(t) = O(log t/log log t). Finally, in Theorem 4,

we consider the related problem of determining the number of representations of an

integer as a product of consecutive integers .

THEOREM 1. The average and normal order of N(t) = 2 .

Proof. For integral x, let n be defined by(nn 12) < x <_ (2n)

We have
 E N(t) = 2

 E 1- E 1
1<t!x

 1<(' ) Sx

 1< (kk ) 5_ s
2r5m

256
 so that n = 0(log x) .

1974]

 MATHEMATICAL NOTES

 2 57

(2)
 = 2{ E 1 +

 1 + E 1~ -
1<(i)Sx

 1<(Z)Sx

 1<( m)Sx

 1<(k Sr
 1

3S_r5_m/2
= 2x + 22x1/2 + O( x i/3 n)

= 2x + 2 á/2x i/2 + O(x 113 log x).

It follows that the average order of N(t) is 2.

Let f(x) be the number of integers t, 1 < t <- x, such that N(t) = 2 and g(x) the
number such that N(t) > 2, so that f (x) + g(x) = x - 2. We have

(3)

 = 2(x - 2 - g(x)) + 3g(x) + 1

= 2x + 2g(x) - 3.

It follows from (2) and (3) that g(x) = O(x112) and this implies

order of N(t) is 2.

THEOREM 2 . Let w(t) denote the number of distinct prime factors of the integer

t > 1 . For all t satisfying w(t) < log s/loglogt we have

2w(t) log t
(4)

 N(t) < log t - w(t) log log t

Proof. The theorem can be verified directly for t S 20. In what follows we

therefore assume t >- 21 . Let k = k(t) be the largest integer for which t = (k ) for

some n >- 2k . Then clearly

(5)
 E N(t) >_ 2f (x) + 3g(x) + 1
1<t5x
 that the normal

N(t) < 2k .

By an easy induction argument we have, for k >- 4, t = (k) >_ k) >_ ek . Since

we are assuming t >- 21 > e 3, the inequality t ? ek holds for all k >_ 1 . Equivalently,

(6)

 k 5 log t and log k S log log t.

Let P a be the highest power of the prime P which divides t. Then, according to the
well-known theorem of Legendre,

[1lRpl]
 ~LPiJ
 - [ n Ptk] -
 [k

Each term in the sum on the right is either 0 or 1 . The number of non-zero terms is

therefore a and we must have

2 58

 H . L . ABBOTT, P . ERDŐS AND D . HANSON

 [March

(7) P' S n .

From t = n' and the inequality (k) >_ (n , we obtain
k)

 k)

(8)

 n < kt 1Ik

and from (7) and (8) it follows that

t = IIP° < n '(`) < kw()tw( .)lk

If we take logarithms and substitute from the second inequality in (6) we get, after
some manipulations,
 k <

 w(t) log t
- log t - w(t) log log t '

and this, together with (5), yields (4). This completes the proof of Theorem 2 .
We come now to our main result .

THEOREM 3 . N(t) = O (log t/log log t) .

Proof. We shall need to make use of the following deep result of A. E. Ingham [2]
on the distribution of the primes : If a >= 5/8, there is a prime between x and x + x'
for all sufficiently large x.

For a given integer t, let S = {n : t = (k ) for some k _<_ n/2}. Write S = Sl V SZ

where S l = {n : n e S, n > (log t)
615
} and S z = {n : n e S, n _5 (log t)615 } . We first

estimate the size of S, Let n e Sl and let t = ( k )
. We have at our disposal the

following inequalities :
 t = ( k) > (k
 )

k

(10)

 t > ek (see the proof of Theorem 2)

(11)

 n > (log t)
6rs

Thus
 k < tog t <

 log t <

 log t

log n/k - log (n/log t) - log (log t)u5

_ - O log t

log log t '

where we have used, successively, (9), (10) and (11) . It follows that

Sl Í = O(log tflog log t) .

(9)

1974]

 MATHEMATICAL NOTES

 2 5 9

Next we must estimate the size of S 2. Let N be the largest number in S2 and let

t = (
K)
 . We have the inequalities

N <_ (logt)6f5 and t _< N R

from which we get N <- (K log N) 6t5 This in turn implies, for N sufficiently large,

N 5 K 815 < K 815 + K,

and it is easy to see that this last inequality implies

(N - K) + (N - K) 5t8 < N .

We are now in a position to apply the theorem of Ingham . By this theorem, there is a
largest prime P satisfying K S N - K < P _<_ N. It follows that P divides t and
hence that n ? P for all n e S2. Hence all of the numbers in S2 lie between P
and N . The number of numbers in S2 is thus

SZ I <_ N - P <_ P5/8 < N518 <_ (log t) 3/a = O (log t/log log t),

where, in obtaining the second inequality, we again appeal to Ingham's result . This
completes the proof of Theorem 3 .
We remark that if one makes use of the unproved conjecture of Cramér [3]

asserting that there is a prime between x and x + (log x) Z for all sufficiently large x,
then our argument gives N(t) = 0((logt) 213+E ) The proof is basically the same
as before, except that one puts S, = {n : n e S, log n > (log t) 113-E }. We omit the
rather laborious details of the argument .
We conclude with a brief discussion of a somewhat related problem . Let G(t)

denote the number of representations of the positive integer t as a product of con-

secutive integers; that is, G(t) is the number of solutions of t = (n + 1)(n + 2) . . .
(n + 1) in integers n and 1. For any such solution we have t >_ 1! and consequently
we get G(t) = O (log t1log log t). For this problem, however, we can get a substan-
tially stronger result.

THEOREM 4 . G(t) = O (J log t).

Proof. Let S = fl: t = (n+ 1)(n+2) . . . (n + l) for some n}. Let L o be the
largest number in S and let

S, = {1 : l e S, Lo - Clog t) 112 < 1 <_ Lo} and S2 = { 1 : 1 e S,1 <_ Lo - C(log t)1i2 }.

C is a constant . It is clear that IS, I <_ C(logt)112 . It remains to estimate the size

of I S2 I . Let 2" be the highest power of 2 which divides t. Then, for some constant C 1,

(12)

 a >_ E [ L0 1 >= LO - C, log L o .
i=1 2j

260

 H . L . ABBOTT, P . ERDÖS AND D . HANSON

 [Marsh

Let L be the largest number in S2 and let t = (N + 1) (N + 2) .. (N + L). Let

2° be the highest power of 2 which divides one of (N + 1), (N + 2),,. . ., (4V + L), say
N + k . Then
 CD

 -

 '-] .
(13)

 a - + j
FIr2' kJ + jI1 [k 21 1

In fact (13) follows from the observation that the first sum on the right is the exponent

to which 2 divides the product (N + k + 1) (N + k + 2) . . .(N + L), while the second
sum is the exponent to which 2 divides the product (N + 1) (N + 2) . . . (N + k - 1).

It follows from (13) that

(14)

 a<_fl+EILI<=tg+L .
J=1 2'

Thus,
 >_ a-L

>_ (Lo - C l logL,,) - (Lo - C (log t)1/2)

(15)

 >_ C (log t) 112 - C IIog L o

> CZ (log t)1/2,

where we have used (14), (12), the definition of S 2 and the estimate L o = O (log t).

We need two further inequalities ; the first of which is obvious . These are

(16)

 (N + 1) L _< t

and, for t sufficiently large,

(17)

 N + L > 2f -1

To obtain (17)' we simply have to notice that N + L >_ N + k > 2f, so that N + 1

20 - (L - 1) and (17) now follows from (15) and the fact that L = O (log t) .

It now follows from (15), (16) and (17) that L 5 C3 (log t)1 /2 , where C 3 is a

positive constant depending on C2, and hence on C . This completes the proof of
Theorem 4.
We remark that by choosing C = (1 +6)(log 2) -1/2 ,, our argument yields

G(t) < (2 + s) (log t/log 2)1 /2 for every s > 0, provided t >- to(s).

Refereaces-

1. D. Singmaster, How often does .an_integer occur as :a-binomial coefficient, this MoN. TiiLY, 78

(1971) 385-386.
2. A . E. Ingham, On the difference between consecutive primes ; Quart. J: Math. Oxford, 8 (1937)

255-266.
3. H. Cramér, On the order of`magnitude,of the difference between consecutive prime numbers,
Acta. Arith., 2 (1936) 23-46 .

1974]

 MATHEMATICAL NOTES

 261

4. G . H. Hardy and E . M. Wright, Introduction to the Theory of Numbers, Oxford University
Press, New York. 1960 .
5. D. Singmaster, Repeated binomial coefficients and Fibonacci Numbers, (to appear in Fibona-

cci Quarterly).
6. Douglas Lind, The quadratic field Q( .J5) and a certain diophantine equation, Fibonacci

Quarterly, 6 (1968) 86-94 .

DEPARTMENT OF MATHEMATICS, UNIVERSITY OF ALBERTA, EDMONTON, ALBERTA, CANADA .

DEPARTMENT OF MATHEMATICS, UNIVERSITY OF CALGARY, CALGARY, ALBERTA, CANADA .

DEPARTMENT OF MATHEMATICS, UNIVERSITY OF SASKATCHEWAN, REGINA, SASKATCHEWAN,
CANADA .
