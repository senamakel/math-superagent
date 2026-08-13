<!-- source: https://pub.math.leidenuniv.nl/~tijdemanr/shoreyt.pdf | converted from PDF -->

Diophantine Equations
Editor: N. Saradha
Copyright c⃝2007 Tata Institute of Fundamental Research
Publisher: Narosa Publishing House, New Delhi, India

Highlights in the Research Work of
T.N. Shorey

R. Tijdeman

Abstract

We state a number of important results which we owe to Tarlok
Shorey.

1 Shorey’s Contributions to Linear Form
Estimates and Some Applications

One of the ﬁrst results of Shorey concerns a sharpening of a theorem of
Sylvester. Sylvester proved in 1892 that a product of k consecutive positive
integers greater than k is divisible by a prime exceeding k. By combining
a result of Jutila which depends on estimates for exponential sums and an
estimate on linear forms in logarithms, Shorey [45] proved in 1974 that it
suﬃces to take constant times k(log logk)/logk consecutive integers in place
of k consecutive integers in the above result of Sylvester. This improved on
results of Erd˝os, Tijdeman, and Ramachandra and Shorey and is still the
best known.
The used estimate for the linear form itself is an important contribution
of Shorey to the theory on estimating linear forms in logarithms of alge-
braic numbers which had been developed by Baker in the preceding decade.
Since estimates on linear forms play an important role in Shorey’s work, we
state his result. If a and b are coprime integers then the size of the rational
number a/b is deﬁned as |b| + |a/b|. All the constants C1, C2, . . . appearing
in this article are eﬀectively computable. This means that they can be de-
termined explicitly in terms of the various parameters under consideration.
Let n > 1 be an integer. Let

α1 = m
m′ , α2 = p2
p′
2 , . . . , αn = pn
p′
n

1

2 R. Tijdeman

where p2, . . . , pn, p′
2, . . . , p′
n are pairwise distinct prime numbers and none
of them is a divisor of the positive integers m, m′. Suppose the sizes of
α1, . . . , αn do not exceed S and A is a constant > 1 such that

| log αi| ≤ exp(− 1
A log S) f or i = 1, . . . , n. (1.1)

If β1, . . . , βn−1 are rational numbers of size at most S, then

|β1 log α1 + · · · + βn−1 log αn−1 − log αn| > exp(−(nA)
C1n log S) (1.2)

where C1 > 0 is independent of n, A and S.
The novelty of Shorey’s estimate was two-sided. On the one hand the
factor log S in the exponent of the lower bound of (1.2) is remarkably
sharp and in fact the best possible. This was made possible by imposing
condition (1.1) which implies that the numbers αi are quite close to 1. The
studies of linear forms in logarithms with αi’s close to 1 were continued
by Waldschmidt in 1980 and they led to a remarkable estimate of Laurent,
Mignotte and Nesterenko [25] on linear forms in two logarithms in 1995.
It has several important applications. For example, it has been applied by
Bennett [3] in 2001 to establish the striking theorem that for any positive
integer a, the equation

(a + 1)x
n − ayn = 1 in integers x ≥ 1, y ≥ 1, n ≥ 3 (1.3)

has no non-trivial solution, i.e. has no solution other than x = y = 1. An-
other application of Shorey’s linear form estimate concerns the conjecture
of Grimm that if x, x + 1, . . . , x + k − 1 are all composite integers, then
the number of distinct prime factors of x(x + 1) · · · (x + k − 1) is at least
k. Ramachandra, Shorey and Tijdeman [30] conﬁrmed Grimm’s conjecture
when (logx)/(logk)
2 exceeds some absolute constant. The assumption that
x, x + 1, . . . , x + k − 1 are all composites is not required in this result.
The other novelty in Shorey’s estimate (1.2) was that the dependence
on n was much better than in previous estimates. Until then there had
been a factor n2 in the exponent. In 1976 Shorey [48] published a linear
form estimate with the same dependence on n in the more general case that
the numbers αi and βi are algebraic numbers of bounded degree and size.
Apart from the constant C1, this estimate was best known with respect
to its dependence on n until 2000 when Matveev [26] replaced nC1n by
eC2n. The dependence on n has several applications some of which will be
mentioned in the next section.

Highlights in the Research Work of T.N. Shorey 3

2 Applications of Linear Form Estimates to
Values of Polynomials, Recurrence Sequen-
ces and Continued Fractions

For an integer ν with |ν| > 1, we denote by P (ν) the greatest prime factor
of ν and by ω(ν) the number of distinct prime divisors of ν, respectively.
Further we put P (1) = P (−1) = 1 and ω(1) = ω(−1) = 0. Let f (X)
be a polynomial with integer coeﬃcients and at least two distinct roots.
For a suﬃciently large integer x, estimates for linear forms in logarithms
yield that ω(f (x)) is at least constant times loglogx/logloglogx whenever
logP (f (x)) ≤ (loglogx)
2. This implies that P (f (x)) at integer x with |x| ≥
C3 exceeds C4log log|x| for some numbers C3 and C4 > 0 depending only
on f . In fact Shorey and Tijdeman [62] obtained lower bounds for

max
1≤i≤yP (f (x + i))

for log y ≤ (loglog x)
C5 where C5 is any absolute constant. By applying a
p-adic analogue of the above result on linear forms in logarithms, Shorey,
van der Poorten, Tijdeman and Schinzel [61] extended the result on a lower
bound for P (f (x)) to all binary forms with at least three pairwise non-
proportional linear factors in their factorizations over C.
For given integers m > 1 and n > 1 with mn ≥ 6, a result of Mahler
from 1956 states that P (ax
m − byn) tends to inﬁnity as max (|x|, |y|) → ∞
with gcd (x, y) = 1. The proof of Mahler is non-eﬀective but an eﬀective
version follows from the theory of linear forms in logarithms. In fact Shorey,
van der Poorten, Tijdeman and Schinzel applied this theory to prove that
P (ax
m−byn) tends to inﬁnity with m uniformly in integers x, y with |x| > 1
and gcd (x, y) = 1. The proof depends on the above mentioned result on
the greatest prime factor of a binary form. In 1980 Shorey made the proof
independent of this result and it led him to give a quantitative version
P (ax
m − byn) ≥ C6((log m)(log log m))
1/2 which has been improved by
Bugeaud [7] to P (ax
m − byn) ≥ C7log m where C6 > 0 and C7 > 0 depend
only on a, b and n.
For relatively prime positive integers A and B with A > B, it has
been conjectured that P (A
n − Bn)/n tends to inﬁnity with n. The ﬁrst
result, from 1904, is due to Birkhoﬀ and Vandiver and states that P (A
n −
Bn) > n for n > 6. In 1962 this was improved to P (A
n − Bn) > 2n − 1
by Schinzel if AB is a square or twice a square unless n ̸= 4, 6, 12 when
(A, B) = (2, 1). In 1975 Stewart conﬁrmed the conjecture for all n with
ω(n) ≤ K log log n where 0 < K < 1/ log 2 which is satisﬁed for almost
all n. The year thereafter Erd˝os and Shorey [15] gave lower bounds for

4 R. Tijdeman

P (A
n − Bn)/n by applying estimates for linear forms in logarithms. In
particular they proved for primes p that

P (2p − 1) > C8p log p

where C8 > 0 is an absolute constant. They also combined the theory of
linear forms in logarithms with Brun’s Sieve to show that

P (2p − 1) > p (log p)
2/(log log p)
3

for almost all primes p.
The sequence {A
n − Bn}∞
n=1 is a special case of a binary recursive
sequence. Let r and s ̸= 0 be integers with r2 + 4s ̸= 0. Let u0, u1, . . .
be integers such that un = run−1 + sun−2 for n = 2, 3, . . .. Hence there
exist numbers a, b, α, β such that un = aα
n + bβn for n ≥ 0. We assume
that ab ̸= 0 and that α/β is not a root of unity. In 1934 Mahler proved,
ineﬀectively, that P (un) tends to inﬁnity with n and an eﬀective version
is due to Schinzel in 1967. For n > m > 0 with unum ̸= 0, Shorey [50]
generalized a result of Stewart by proving that

P ( un
gcd(un, um)
 ) ≥ C9
 ( n
log n
 )1/(d1+1) (2.1)

where d1 = [Q(α, β) : Q] and C9 > 0 depends only on α and β. It follows
from (2.1) that ul | um with l > m implies that l is bounded by a number
depending only on the sequence {un}.
Let α be an irrational real number with [a0, a1, . . .] as its simple con-
tinued fraction expansion. Let pn/qn and αn = [an, an+1, . . .] be the n-th
convergent and the n-th complete quotient in the simple continued frac-
tion expansion of α, respectively. If α is algebraic of degree ≥ 3 and dαn
denotes the denominator of αn, then Gy˝ory and Shorey [17] showed that
dαn ≥ C10Cn
11 and P (dαn ) ≥ C12 log n where n > 1 and C10, C11, C12 > 1
are positive numbers depending only on α. As an application of the es-
timate on linear forms in logarithms mentioned in the beginning of this
article, Shorey [47] derived that P (pnqn) ≥ C13 log log qn if α is algebraic.
Here C13 > 0 depends only on α. This is an improved and eﬀective ver-
sion of a result of Mahler that P (pnqn) tends to inﬁnity with n. In 1939
Erd˝os and Mahler conjectured that if P (pnqn) is bounded for inﬁnitely
many n, then α has to be a Liouville number. Shorey [49] showed that if
α is a non-Liouville number such that P (pnk qnk ) is bounded for k ≥ 1 and
n1 < n2 < · · · , then
 lim
k→∞ log log nk
log k = ∞.

Highlights in the Research Work of T.N. Shorey 5

3 Some Irrationality Measures and Transcen-
dence Results

Shorey [44] proved a p-adic analogue of a result of Tijdeman on a bound for
the number of zeros of a general exponential polynomial in a disk and he
applied it to give p-adic analogues of the results of Tijdeman on algebraic
independence of certain numbers connected with the exponential function.
As an application of much more general theorems he proved that for a prime
p > 2 at least two of the numbers

ep, epe
p, epe
2p , epe
3p

are algebraically independent. This implies that at least one of the last
three numbers is transcendental.
A result of Siegel and Schneider (re-discovered by Lang and Ramachan-
dra) states that
 | 2π − α1 | + | 2π2 − α2 | + | 2π3 − α3 | (3.1)

is positive where α1, α2 and α3 are algebraic numbers. The question whether
at least one of the numbers 2π and 2π2 is transcendental remains open and
is a special case of the well-known four exponential conjecture. Shorey [46]
gave a positive lower bound for (3.1) in terms of the heights and degrees of
α1, α2 and α3.
In 2001 the theorem of Baker that a linear form in logarithms of alge-
braic numbers with algebraic coeﬃcients is either zero or transcendental
was applied by Adhikari, Saradha, Shorey and Tijdeman [1] to prove the
transcendence of certain inﬁnite series. For example, they showed that

L(1, χ) with χ a non-principal character as well as
 ∞∑

n=1
 Fn
n2n with (Fn) the

Fibonacci sequence are transcendental.

4 Results on the Ramanujan τ -function

Consider the Ramanujan τ -function

∞∑

n=1 τ (n)qn = q
 ∞∏

m=1
(1 − qm)
24.

Let p be a prime such that τ (p) ̸= 0. Shorey [54] applied the theory of
linear forms in logarithms to prove that τ (pm) ̸= τ (pn) whenever m > n
and m ≥ C14. In fact he gave an explicit lower bound for the diﬀerence of

6 R. Tijdeman

these numbers. Kumar Murty, Ram Murty and Shorey [28] showed that
for non-zero odd integer a, the equation

τ (n) = a

implies that log n ≤ (2|a|)
C15 where C15 is an absolute constant. In partic-
ular, the above equation has only ﬁnitely many solutions in integers n ≥ 1.

5 The Ramanujan-Nagell Equation

Ramanujan conjectured and Nagell proved that the equation, now known
as the Ramanujan-Nagell equation,

x
2 + 7 = 2n in integers x ≥ 1, n ≥ 1

has only solutions (x, n) = (1, 3), (3, 4), (5, 5), (11, 7), (181, 15). Let y ≥
2, D1 and D2 be positive integers such that gcd(D1, D2) = 1, D = D1D2
and λ ∈ {21/2, 2}. We consider the generalized Ramanujan-Nagell equation

D1x
2 + D2 = λ
2yn (5.1)

in integers x ≥ 1 and n ≥ 1. We denote by N (λ, D1, D2, y) the number
of solutions (x, n) of (5.1) and we write p for a prime. Le proved in 1997
and 1999 that N (λ, D1, D2, p) ≤ 2 except for an explicitly given ﬁnite
set of exceptions. There are three inﬁnite families of triples (D1, D2, y)
for which N (λ, D1, D2, y) ≥ 2. Bugeaud and Shorey [12] showed that if
(D1, D2, p) does not belong to any of these three inﬁnite families, then
N (λ, D1, D2, p) ≤ 1 except for an explicitly given ﬁnite set of possibilities
and that if (D1, D2, p) belongs to one of these three inﬁnite families, then
N (λ, D1, D2, p) = 2. This settled an old question. The proof depends on a
theorem of Bilu, Hanrot and Voutier. The more diﬃcult equation x
2 + 7 =
yn and many similar equations have been completely solved recently by
Bugeaud, Mignotte and Siksek, see [10] and [11]. Now all the equations
x
2 + D2 = yn with 1 ≤ D2 ≤ 100 are completely solved, see [14] and [11].

6 Other Extensions of the Theorem of
Sylvester

For positive integers x and k ≥ 2, we write

△1 = △1(x, k) = x(x + 1) · · · (x + k − 1)

Highlights in the Research Work of T.N. Shorey 7

and give lower bounds for P (△1) and ω(△1). As stated in the ﬁrst section,
Sylvester proved that
 P (△1(x, k)) > k if x > k.

The assumption x > k cannot be removed since P (△1(1, k)) ≤ k. Improv-
ing on results of Sylvester and Hanson, Laishram and Shorey [22] proved
that P (△1) > 1.95k if x > k except for an explicitly given ﬁnite set of pos-
sibilities. Here we observe that 1.95 cannot be replaced by 2, since there are
arbitrarily long chains of composite positive integers. There is no exception
when k > 270 or x > k + 11.
We turn to lower bounds for ω(△1). We see that k! divides △1(x, k) and
therefore Sylvester’s theorem can be re-formulated as

ω(△1) > π(k) if x > k.

A well-known conjecture states that 2p − 1 is prime for inﬁnitely many
primes p. Thus ω(△1) = 2 for inﬁnitely many primes p when x = 2p−1, k =
2 according to the above conjecture. Therefore we assume that k ≥ 3.
Saradha and Shorey [39] improved Sylvester’s theorem to

ω(△1) ≥ π(k) + [ 1
3 π(k)] + 2 if x > k

except for an explicitly given ﬁnite set of possibilities. The above estimate
is best known for k ≤ 18. For k ≥ 19, Laishram and Shorey [21] sharpened
it to ω(△1) ≥ π(k) + [ 3
4 π(k)] − 1 if x > k

except for explicitly given ﬁnitely many possibilities. We refer to [39] and
[21] for the set of exceptions to the above estimates. These exceptions
satisfy ω(△1) ≥ π(2k) − 1.
Now we consider Sylvester’s theorem and its sharpenings for a product
of terms in arithmetic progression. For relatively prime positive integers
x, d ≥ 2 and k ≥ 3, we put

△ = △(x, d, k) = x(x + d) · · · (x + (k − 1)d)

and we give lower bounds for P (△) and ω(△). We observe that P (△(x, d, 2)) =
2 if and only if x = 1 and d + 1 is a power of 2. Therefore we assume that
k ≥ 3. In 1892 Sylvester proved that P (△) > k if x ≥ d + k. In 1976/77
Langevin replaced the assumption x ≥ d + k by x > k. Further Shorey and
Tijdeman [66] showed that

P (△) > k unless (x, d, k) = (2, 7, 3).

8 R. Tijdeman

Laishram and Shorey [23] proved that

P (△(x, d, k)) > 2k for d > 2

unless k = 3, (x, d) = (1, 4), (1, 7), (2, 3), (2, 7), (2, 23), (2, 79), (3, 61), (4, 23),
(5, 11), (18, 7); k = 4, (x, d) = (1, 3), (1, 13), (3, 11); k = 10, (x, d) = (1, 3).
There is no loss of generality in assuming that d > 2, since the case d = 2
is similar to that of d = 1 considered above. A conjecture states that

P (△) > ak for d > a

where a is a positive integer. Thus the conjecture has been conﬁrmed for
a = 1, 2 according to the above inequalities.
Next we consider lower bounds for ω(△) in terms of π(k). Shorey and
Tijdeman [64] proved that ω(△) ≥ π(k) and Moree showed that ω(△) >
π(k) for k ≥ 4 and (x, d, k) ̸= (1, 2, 5). Schinzel’s Hypothesis H implies
that there are inﬁnitely many d such that 1 + d, 1 + 2d, 1 + 3d, 1 + 4d
are all primes. Thus Hypothesis H implies that the estimate of Moree is
best possible for k = 4, 5. For k ≥ 6, Saradha, Shorey and Tijdeman [43]
sharpened and extended the preceding inequality. Their result was further
reﬁned by Laishram and Shorey [23] as

ω(△) ≥ π(2k) − 1 unless (x, d, k) = (1, 3, 10)

conﬁrming a conjecture of Moree. This is best possible when d = 2 by
considering ω(△(k + 1, 2, k)) = π(2k) − 1. The proof of this result depends
on explicit estimates for the number of primes in arithmetic progression
due to Ramar´e and Rumely.

7 Arithmetical Progressions and Perfect
Powers

Erd˝os and Selfridge proved in 1975 that a product of two or more consec-
utive positive integers is never a power. In 2001 Saradha and Shorey [37]
showed that there are no powers other than

6!
5 = (12)
2, 10!
7 = (720)
2, 1.2.4 = 2.4 = 23

which are product of k −1 distinct integers out of k ≥ 3 consecutive positive
integers x, x + 1, . . . , x + k − 1. This settled a conjecture of Erd˝os and
Selfridge. The proof depends on combining the elementary method of Erd˝os
and Selfridge with the method of Wiles on the Fermat equation.

Highlights in the Research Work of T.N. Shorey 9

Let m > 2 be a prime, k ≥ 3 and x > km. Erd˝os and Selfridge showed
more generally that a product x(x + 1) · · · (x + k − 1) is not of the form bym

with P (b) < k. The assumption P (b) < k has been relaxed to P (b) ≤ k
by Saradha for k ≥ 4 and by Gy˝ory for k = 3. The particular case b = k!
of the result of Saradha and Gy˝ory was already settled by Erd˝os for k ≥ 4
and by Gy˝ory for k = 3. Hanrot, Saradha and Shorey [18] showed that the
product in the result of Saradha and Shorey in the preceding paragraph is
not of the form bym with P (b) < k unless k = 4 and it is not of the form
bym with P (b) ≤ k unless k ∈ {3, 4, 5} which cases were covered by Bennett
[4]. The analogous result for m = 2 is given in Saradha and Shorey [39]
where it has been proved that a product of k − 1 distinct integers out of
x, x+1, . . . , x+k −1 with x > k2 and k ≥ 4 is of the form by2 with P (b) ≤ k
only when (x, k) = (24, 4), (47, 4), (48, 4). Here the assumption k ≥ 4 is
necessary, since Pell’s equations have inﬁnitely many integer solutions.
Some authors have shown that k is bounded if more than Cmk numbers
from a block of k consecutive numbers have a product of the form bym with
P (b) ≤ k, y > 1, m > 1 for suitable Cm. Shorey [51], [53] proved that this
is true with C3 = .84, C4 = .71, C5 = .65, C6 = .62. It follows from the
work of Nesternko and Shorey [29] that Cm = 4
m suﬃces for m ≥ 7.
For relatively prime positive integers x, d and positive integer b with
P (b) ≤ k, we consider the equation

x(x + d) · · · (x + (k − 1)d) = bym in integers x > 0, y > 0, k ≥ 3, m ≥ 2.
(7.1)
We assume that d ≥ 2 as the case d = 1 has already been considered. We
always suppose in (7.1) that (x, d, k) ̸= (2, 7, 3) so that, as already stated,
the left-hand side of (7.1) is divisible by a prime exceeding k. There is no
loss of generality in assuming that m is prime in (7.1) which we suppose in
this section. We further assume in this paragraph that (7.1) holds and k
exceeds a suﬃciently large absolute constant. Erd˝os conjectured that k is
bounded by an absolute constant. Marszalek conﬁrmed the conjecture for
ﬁxed d. Further Shorey and Tijdeman [65], [67] showed that

d ≥ kC16 log log k

where C16 > 0 is an absolute constant and Shorey [59, p.490] applied
this inequality to derive the conjecture of Erd˝os from the abc-conjecture
if m > 3. Further Granville (unpublished) showed that the abc-conjecture
implies the conjecture of Erd˝os with m = 2, 3. For a proof, see Laishram
[20]. Shorey [58], [56] applied linear forms in logarithms with αi’s close
to 1 and irrationality measures of Baker obtained by the hypergeometric
method to show that x ≥ kC17log log k for m ≥ 7 where C17 > 0 is an
absolute constant. Thus k is bounded by a number depending only on x

10 R. Tijdeman

whenever m ≥ 7. If m ≥ 3, Shorey [55] applied the theory of linear forms
in logarithms for proving that k is bounded by a number depending only
on the greatest prime factor of d. Let d1 be the maximal divisor of d such
that all the prime divisors of d1 are congruent to 1 mod m. Then Shorey
[55] showed that d1 > 1 which implies that we need to verify the preceding
assertion for only ﬁnitely many m. The proof depends on estimates for the
magnitude of solutions of Thue-Mahler equations. Moreover, for a given
m ≥ 2, Shorey and Tijdeman [65] proved that k is bounded by a number
depending only on ω(d).
A stronger version of the conjecture of Erd˝os, referred as ES, states
that if (7.1) holds, then (k, m) ∈ (3, 2), (4, 2), (3, 3). In each of the above
three cases, one can ﬁnd b such that (7.1) has inﬁnitely many solutions.
Let m > 2 and k ≥ 4. Saradha and Shorey [37] showed that Shorey’s
inequality d1 > 1 for suﬃciently large k is valid for all k whenever (7.1)
holds. Thus (7.1) implies that d is divisible by a prime congruent to 1 mod
m. Consequently (7.1) never holds for d of the form 2a3b5c > 1 where
a, b, c are integers. Thus conjecture ES is conﬁrmed for inﬁnitely many d.
Saradha and Shorey [40] conﬁrmed conjecture ES for a large number of
other values of d. If ω(d) = 1, i.e. d is a prime power, Saradha and Shorey
[38] showed that a product of four or more terms in arithmetic progression
is never a square. The case k = 3 of the preceding result remains open and
it is likely that (7.1) with b = 1, k = 3 and ω(d) = 1 has inﬁnitely many
solutions. Finally Laishram and Shorey [24] conﬁrmed conjecture ES when
b = 1 and ω(d) = 2, 3, 4.
Now we consider (7.1) with k ﬁxed and without any restriction on d.
First we consider the case of squares i.e. m = 2. The earliest result is due
to Euler that there are no four squares in arithmetic progression. This is
also the case when k = 5 by Obl´ath and 6 ≤ k ≤ 110 by Hirata-Kohno,
Laishram, Shorey and Tijdeman [19]. The cases 6 ≤ k ≤ 11 had been
covered independently by Bennett, Bruin, Gy˝ory and Hajdu [5]. Let m > 2
be prime. The result that n, n + d, n + 2d are not all m-th powers is due to
Darmon and Merel. Gy˝ory showed that (7.1) with k = 3 and P (b) < k is
not possible. This is also the case when k = 4, 5, b = 1 according to Gy˝ory,
Hajdu, Saradha [16] and when 6 ≤ k ≤ 11, b = 1 by Bennett, Bruin, Gy˝ory,
Hajdu.

8 The Nagell-Ljunggren Equation

Consider the equation

ym = x
n − 1
x − 1 in integers x > 1, y > 1, m > 1, n > 2. (8.1)

Highlights in the Research Work of T.N. Shorey 11

The equation asks for powers with all the digits equal to 1 in their x-
adic expansions. It is called the Nagell-Ljunggren equation as Nagell and
Ljunggren made the initial contributions that (8.1) is not possible whenever
4 divides n or m = 2, respectively. The equation has solutions given by

(x, y, n, m) = (3, 11, 5, 2), (7, 20, 4, 2), (18, 7, 3, 3).

It has been conjectured that (8.1) has only ﬁnitely many solutions. This is
a consequence of the abc-conjecture, see [59]. Shorey [51] showed that (8.1)
has only ﬁnitely many solutions when n is divisible by a prime congruent
to 1 mod m. The result of Bennett on (1.3) stated above implies that (8.1)
does not hold whenever n is congruent to 1 mod m.
Shorey and Tijdeman [63] showed that (8.1) has only ﬁnitely many
solutions whenever x is ﬁxed. By using the p-adic analogue of linear forms in
logarithms with αi’s close to 1, Bugeaud solved (8.1) completely for several
values of x. In particular, Bugeaud and Mignotte [8] settled a problem, due
to Inkeri, that there is no m-th power > 1 with digits identically equal
to 1 in its decimal expansion. Saradha and Shorey [36] showed that (8.1)
is not possible if x = z2 such that z runs through all integers > 31 and
z ∈ {2, 3, 4, 8, 9, 16, 27}. Further Bugeaud, Mignotte, Roy and Shorey [9]
covered the remaining cases. Hence (8.1) is not possible if x is a square.
This was also proved, independently, by Bennett [4] who derived it from
his general result on (1.3). Further Saradha and Shorey [36] showed that
(8.1) implies that x is divisible by a prime congruent to 1 mod m whenever
max (x, y, m, n) exceeds a suﬃciently large absolute constant.

9 Goormaghtigh’s Equation

We turn to an equation of Goormaghtigh:

ym − 1
y − 1 = x
n − 1
x − 1 in integers x > 1, y > 1, m > 2, n > 2, m > n. (9.1)

We observe that x > y and (9.1) asks for positive integers with all their dig-
its equal to one with respect to two distinct bases. Goormaghtigh observed
in 1917 that
 31 = 25 − 1
2 − 1 = 53 − 1
5 − 1 , 8191 = 213 − 1
2 − 1 = 903 − 1
90 − 1

and it has been conjectured that these are the only solutions of (9.1). It
follows from the abc- conjecture that (9.1) has only ﬁnitely many solutions,
see [59, p.473]. In 1961 Davenport, Lewis and Schinzel showed that (8.1)

12 R. Tijdeman

has only ﬁnitely many solutions if m and n are ﬁxed. They showed that
the underlying polynomial for (9.1)

X n − 1
X − 1 − Y m − 1
Y − 1

is irreducible over C and has positive genus. Then the assertion follows
from a well-known theorem of Siegel on integer solutions of polynomial
equations in two variables and therefore, is non-eﬀective. On the other
hand, they showed that it is eﬀective when gcd(m − 1, n − 1) > 1. Shorey
[57] showed that 31 and 8191 are the only primes N with ω(N − 1) ≤ 5
such that all the digits of N are equal to one with respect to two distinct
bases. For positive integers A, B, x > 1 and y > 1 with x ̸= y, Shorey [52]
showed that there are at most 24 integers with all the digits equal to A
in their x−adic expansions and all the digits equal to B in their y−adic
expansions. If AB = 1, Bugeaud and Shorey [13] replaced 24 by 2, and
even by 1 if x exceeds 1011 or gcd(x, y) > 1. Balasubramanian and Shorey
[2] proved that (8.1) implies that max (x, y, m, n) is bounded by a number
depending only on the greatest prime factor of x and y.

10 Arithmetical Progressions With Equal
Products

It has been conjectured by Erd˝os and Graham that the equation

X(X + 1) · · · (X + K − 1)Y (Y + 1) · · · (Y + L − 1) = Z 2

in integers K ≥ 3, L ≥ 3 and X ≥ Y + L has only ﬁnitely many solutions
in all the integral variables X > 0, Y > 0, Z > 0, K and L. This conjecture
implies that

x(x + 1) · · · (x + k − 1) = y(y + 1) · · · (y + k + l − 1)

has only ﬁnitely many solutions in x > 0, y > 0, k ≥ 3 and l ≥ 0 satisfying
x ≥ y + k + l. More generally, for positive integers A and B, Erd˝os conjec-
tured that there are only ﬁnitely many integers x > 0, y > 0, k ≥ 3, l ≥ 0
with x ≥ y + k + l satisfying

Ax(x + 1) · · · (x + k − 1) = By(y + 1) · · · (y + k + l − 1). (10.1)

The ﬁrst result in this direction is due to Mordell that (10.1) with A =
B = 1 and k = 2, l = 1 has no solution in integers x > 0 and y > 0
and we refer to [6] for more early results. Beukers, Shorey and Tijdeman

Highlights in the Research Work of T.N. Shorey 13

[6] applied a well-known theorem of Siegel on integral points on curves to
conﬁrm the conjecture if k and l are ﬁxed. The work involves establishing
irreducibility and computing genus of the curve under consideration so that
the assumptions of the theorem of Siegel are satisﬁed. Because of the
ineﬀective nature of Siegel’s result, we do not know any explicit estimate
for the magnitude of the solutions. Saradha and Shorey [31] conﬁrmed the
Erd˝os’ conjecture when x and y are composed of ﬁxed primes. The proof
depends on several applications of linear forms in logarithms. Further they
showed that (10.1) implies that x − y ≥ C18x
2/3 where C18 > 0 depends
only on A and B.
We consider (10.1) with A = B = 1 and k + l an integral multiple of k.
In this case, for an integer m ≥ 2,

x(x + 1) · · · (x + k − 1) = y(y + 1) · · · (y + mk − 1) (10.2)

in integers x > 0, y > 0, k ≥ 2.
We refer to [6] for an account of early results. Saradha and Shorey [33],
by extending an old eﬀective method of Runge to exponential diophantine
equations, proved that (10.2) implies that max (x, y, k) is bounded by a
number depending only on m. Saradha and Shorey [32] and Mignotte and
Shorey [27] showed that (10.2) with 2 ≤ m ≤ 6 implies that x = 8, y =
1, k = 3, m = 2. Shorey has conjectured that (10.2) with m > 6 has no
solution.
For positive integers l, m, d1 and d2 with l < m and gcd (l, m) = 1, we
consider a more general equation than (10.2), namely,

x(x + d1) · · · (x + (lk − 1)d1) = y(y + d2) · · · (y + (mk − 1)d2) (10.3)

in integers x > 0, y > 0, k ≥ 2.
By using Runge’s method, Saradha and Shorey [34], [35] and Saradha,
Shorey and Tijdeman [41] showed that (10.3) implies that either max
(x, y, k) is bounded by a number depending only on m, d1, d2 or m = 2, k =
2, d1 = 2d
2
2, x = y2 + 3d2y. On the other hand, (10.3) with m = 2 is
satisﬁed whenever the latter possibilities hold.
Let l = m = 1 in (10.3). It is clear that (10.3) with k = 2 has inﬁnitely
many solutions. Further Gabovich gave an inﬁnite class of solutions of
(10.3) with k = 3, 4. Some inﬁnite classes of solutions of (10.3) with k = 5
were given by Szymiczek and Choudhry where the latter also provided
an inﬁnite class of solutions of (10.3) with arbitrary k. Next we take d1
and d2 ﬁxed. There is no loss generality in assuming that x > y and gcd
(x, y, d1, d2) = 1. Then d1 < d2. Saradha, Shorey and Tijdeman [42] proved
that either max (x, y, k) is bounded by a number depending only on d2, or
x = k + 1, y = 2, d1 = 1, d2 = 4. The latter possibilities cannot be excluded
in view of (k + 1) · · · (2k) = 2. · 6 · · · (4k − 2), an observation of Makowski.

14 R. Tijdeman

Acknowledgements This paper is based on a paper of T.N. Shorey [60]
entitled ’Diophantine Approximations, Diophantine equations, Transcen-
dence and Applications” which we have cited without further mention. In
that paper the reader can ﬁnd more details, references and, in particular,
a complete list of Shorey’s papers until his 60th birthday.

References

[1] S.D. Adhikari, N. Saradha, T.N. Shorey, and R. Tijdeman, Transcen-
dental Inﬁnite Sums, Indag. Math. N.S. 12 (2001), 1–14.

[2] R. Balasubramanian and T.N. Shorey, On the equation a(x
m − 1)/(x −
1) = b(yn − 1)/(y − 1), Math. Scand. 46 (1980), 177–182.

[3] M.A. Bennett, Rational approximation to algebraic numbers of small
height : the Diophantine equation |ax
n − byn| = 1, J. Reine Angew.
Math. 535 (2001), 1–49.

[4] M.A. Bennett, Product of consecutive integers, Bull. London Math.
Soc. 36 (2004), 683–694.

[5] M. Bennett, N. Bruin, K. Gy˝ory and L. Hajdu, Powers from products
of consecutive terms in arithmetic progression, Proc. London Math.
Soc. 92 (2006), 273–306.

[6] F. Beukers, T.N. Shorey, and R. Tijdeman, Irreducibility of polynomi-
als and arithmetic progressions with equal products of terms, Number
Theory in Progress, Volume 1 (1999), Walter de Gruyter, Berlin, 11–
26.

[7] Y. Bugeaud, Sur le plus grand facteur premier de ax
m + byn, C. R.
Acad. Sci. Paris Sr. I Math. 326 (1998), no. 6, 661–665.

[8] Y. Bugeaud and M. Mignotte, On integers with identical digits, Math-
ematika 46 (1999), 411–417.

[9] Y. Bugeaud, M. Mignotte, Y. Roy and T.N. Shorey, The equation
xn−1
x−1 = yq has no solution with x square, Math. Proc. Camb. Phil.
Soc. 127 (1999), 353–372.

[10] Y. Bugeaud, M. Mignotte and S. Siksek, Classical and modular ap-
proaches to exponential diophantine equations I, Fibonacci and Lucas
perfect powers, Ann. of Math. 163 (2006), 969–1018.

[11] Y. Bugeaud, M. Mignotte and S. Siksek, Classical and modular ap-
proaches to exponential diophantine equations II, The Lebesgue-Nagell
equation, Compositio Math. 142 (2006), 31–62.

Highlights in the Research Work of T.N. Shorey 15

[12] Y. Bugeaud and T.N. Shorey, On the number of solutions of the gener-
alised Ramanujan-Nagell equation, J. Reine Angew. Math. 539 (2001),
55–74.

[13] Y. Bugeaud and T.N. Shorey, On an equation of 0 II, Paciﬁc J. Math.
207 (2002), 61–76.

[14] J.H.E. Cohn, The diophantine equation x
2 + C = yn, Acta Arith. 65
(1993), 367–381.

[15] P. Erd˝os and T.N. Shorey, On the greatest prime factor of 2p − 1 and
other expressions, Acta Arith. 30 (1976), 257–265.

[16] K. Gy˝ory, L. Hajdu and N. Saradha, On the diophantine equation
n(n + d) · · · (n + (k − 1)d) = byl, Canadian Math. Bulletin 47 (2004),
373–384.

[17] K. Gy˝ory and T.N. Shorey, On the denominators of equivalent algebraic
numbers, Indag. Math. 50 (1988), 29–41.

[18] G. Hanrot, N. Saradha, and T.N. Shorey, Almost perfect powers in
consecutive integers, Acta Arith. 99 (2001), 13–25.

[19] N. Hirata-Kohno, Sh. Laishram, T.N. Shorey, and R. Tijdeman, An
extension of a theorem of Euler, submitted.

[20] Sh. Laishram, Topics in diophantine equations, Thesis (2004), Univer-
sity of Mumbai.

[21] Sh. Laishram and T.N. Shorey, Number of prime divisors in a product
of consecutive integers, Acta Arith. 113 (2004), 327–341.

[22] Sh. Laishram and T.N. Shorey, The greatest prime divisor of a product
of consecutive integers, Acta Arith. 120 (2005), 299–306.

[23] Sh. Laishram and T.N. Shorey, The greatest prime divisor of a product
of terms in an arithmetic progression, Indag. Math. (N.S.) 15 (2004),
505–521.

[24] Sh. Laishram and T.N. Shorey, The equation n(n+d) · · · (n+(k−1)d) =
by2 with ω(d) = 2, 3, 4, in preparation.

[25] M. Laurent, M. Mignotte and Y. Nesterenko, Formes lin´eaires en
deux logarithmes et d´eterminants d’interpolation, J. Number Theory
55 (1995), 285–321.

[26] M. Matveev, An explicit lower bound for a homogeneous rational linear
form in logarithms of algebraic numbers II, Izv. Ross Akad. Nauk Ser.
Mat 64 (2000), 125–180, English transl.in Izv. Math. 64 (2000), 1217–
1269.

[27] M. Mignotte and T.N. Shorey, The equations (x + 1) · · · (x + k) =
(y + 1) · · · (y + mk), m = 5, 6, Indag. Math., N.S. 7 (1996), 215–225.

16 R. Tijdeman

[28] Ram Murty, Kumar Murty and T.N. Shorey, Odd values of Ramanujan
τ -function, Bull. Soc. Math. France 115 (1987), 391–395.

[29] Yu.V. Nesterenko and T.N. Shorey, Perfect powers in products of in-
tegers from a block of consecutive integers (II), Acta Arith. 76 (1996),
191–198.

[30] K. Ramachandra, T.N. Shorey, and R. Tijdeman, On Grimm’s problem
relating to factorisation of a block of consecutive integers II, J. Reine
Angew. Math. 288 (1976), 192–201.

[31] N. Saradha and T.N. Shorey, On the ratio of two blocks of consecutive
integers, Proc. Indian Acad. Sci. (Math. Sci.) 100 (1990), 107–132.

[32] N. Saradha and T.N. Shorey, The equations (x + 1) · · · (x + k) = (y +
1) · · · (y + mk) with m = 3, 4, Indag. Math., N.S. 2 (1991), 489–510.

[33] N. Saradha and T.N. Shorey, On the equation (x + 1) · · · (x + k) =
(y + 1) · · · (y + mk), Indag. Math. N.S. 3 (1992), 79–90.

[34] N. Saradha and T.N. Shorey, On the equation x(x + d) · · · (x + (k −
1)d) = y(y+d) · · · (y+(mk−1)d), Indag. Math. N.S. 3 (1992), 237–242.

[35] N. Saradha and T.N. Shorey, On the equation x(x + d1) · · · (x +
(k − 1)d1) = y(y + d2) · · · (y + (mk − 1)d2), Proc. Indian Acad. Sci.
(Math.Sci.) 104 (1994), 1–12.

[36] N. Saradha and T.N. Shorey, The equation xn−1
x−1 = yq with x square,
Math. Proc. Camb. Phil. Soc. 125 (1999), 1–19.

[37] N. Saradha and T.N. Shorey, Almost perfect powers in arithmetic pro-
gression, Acta Arith. 99 (2001), 363–388.

[38] N. Saradha and T.N. Shorey, Almost squares in arithmetic progression,
Compositio Math. 138 (2003), 73–111.

[39] N. Saradha and T.N. Shorey, Almost squares and factorisations in
consecutive integers, Compositio Math. 138 (2003), 113–124.

[40] N. Saradha and T.N. Shorey, Contributions towards a conjecture of
Erd˝os on perfect powers in arithmetic progressions, Compositio Math.
141 (2005), 541–560.

[41] N. Saradha, T.N. Shorey, and R. Tijdeman, On arithmetic progressions
with equal products, Acta Arith. 68 (1994), 89–100.

[42] N. Saradha, T.N. Shorey, and R. Tijdeman, On arithmetic progressions
of equal lengths with equal products, Math. Proc. Camb. Phil. Soc. 117
(1995), 193–201.

[43] N. Saradha, T.N. Shorey, and R. Tijdeman, Some extensions and re-
ﬁnements of a theorem of Sylvester, Acta Arith. 102 (2002), 167–181.

Highlights in the Research Work of T.N. Shorey 17

[44] T.N. Shorey, Algebraic independence of certain numbers in the P -adic
domain, Indag. Math. 34 (1972), 423–435.

[45] T.N. Shorey, On gaps between numbers with a large prime factor II,
Acta Arith. 25 (1974), 365–373.

[46] T.N. Shorey, On the sum ∑3
k=1 | 2πk − αk |, αk algebraic numbers, J.
Number Theory 6 (1974), 248–260.

[47] T.N. Shorey, Some applications of linear forms in logarithms, Seminar
Delange - Pisot Poitou 1975/76, Paris, Exp.3.

[48] T.N. Shorey On linear forms in the logarithms of algebraic numbers,
Acta Arith. 30 (1976), 27–42.

[49] T.N. Shorey, Divisors of convergents of a continued fraction, J. Num-
ber Theory 17 (1983), 127–133.

[50] T.N. Shorey, Linear forms in members of a binary recursive sequence,
Acta Arith. 43 (1984), 317–331.

[51] T.N. Shorey, Perfect powers in values of certain polynomials at integer
points, Math. Proc. Camb. Phil. Soc. 99 (1986), 195–207.

[52] T.N. Shorey, On the equation ax
m − byn = k, Indag. Math. 48 (1986),
353–358.

[53] T.N. Shorey, Perfect powers in products of integers from a block of
consecutive integers, Acta Arith. 49 (1987), 71–79.

[54] T.N. Shorey, Ramanujan and binary recursive sequences, J. Indian
Math. Soc. 52 (1987), 147–157.

[55] T.N. Shorey, Some exponential Diophantine equations, New Advances
in Transcendence Theory, ed. by A. Baker, Cambridge University Press
(1988), 352–365.

[56] T.N. Shorey, Some exponential Diophantine equations II, Number The-
ory and Related Topics ed. by S. Raghavan, Tata Institute of Funda-
mental Research, Bombay (1988), 217–229.

[57] T.N. Shorey, Integers with identical digits, Acta Arith. 53 (1989), 81–
99.

[58] T.N. Shorey, Perfect powers in products of arithmetical progressions
with ﬁxed initial term, Indag. Math. N.S. 7 (1996), 521–525.

[59] T.N. Shorey, Exponential diophantine equations involving products of
consecutive integers and related equations, Number Theory ed. R.P.
Bambah, V.C. Dumir and R.J. Hans-Gill, Hindustan Book Agency
(1999), 463–495.

18 R. Tijdeman

[60] T.N. Shorey, Diophantine approximations, Diophantine equations,
transcendence and applications, Indian J. Pure Appl. Math. 37 (2006),
9–39.

[61] T.N. Shorey, A.J. van der Poorten, R. Tijdeman and A. Schinzel,
Applications of the Gel’fond-Baker method to Diophantine equations,
Transcendence Theory: Advances and Applications, ed. by A. Baker
and D.W. Masser, Academic Press, London, (1977), 59–77.

[62] T.N. Shorey and R. Tijdeman, On the greatest prime factors of poly-
nomials at integer points, Compositio Math. 33 (1976), 187–195.

[63] T.N. Shorey and R. Tijdeman, New applications of Diophantine ap-
proximations to Diophantine equations, Math. Scand. 39 (1976), 5–18.

[64] T.N. Shorey and R. Tijdeman, On the number of prime factors of an
arithmetical progression, J. Sichuan Univ. 26 (1989), 72–74.

[65] T.N. Shorey and R. Tijdeman, Perfect powers in products of terms in
an arithmetical progression, Compositio Math. (1990), 307–344.

[66] T.N. Shorey and R. Tijdeman, On the greatest prime factor of an
arithmetical progression, A Tribute to Paul Erd˝os, ed. A. Baker, B.
Bollobas and A. Hajnal, Cambridge University Press (1990), 385–389.

[67] T.N. Shorey and R. Tijdeman, Perfect powers in products of terms in
an arithmetical progression (II), Compositio Math. 82 (1992), 119–
136.

Mathematisch Instituut, Leiden University, Postbus 9512,
2300 RA Leiden, The Netherlands.
E-mail: tijdeman@math.leidenuniv.nl
