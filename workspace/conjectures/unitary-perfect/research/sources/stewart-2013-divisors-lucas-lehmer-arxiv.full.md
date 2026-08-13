<!-- source: https://arxiv.org/pdf/1008.1274 | converted from PDF -->

arXiv:1008.1274v1  [math.NT]  6 Aug 2010
ON DIVISORS OF LUCAS AND LEHMER NUMBERS

C.L. STEWART

Abstract. Let un be the n-th term of a Lucas sequence or a Lehmer sequence.
In this article we shall establish an estimate from below for the greatest prime
factor of un which is of the form n exp(log n/104 log log n). In so doing we are
able to resolve a question of Schinzel from 1962 and a conjecture of Erd˝os from
1965. In addition we are able to give the ﬁrst general improvement on results
of Bang from 1886 and Carmichael from 1912.

1. Introduction

Let α and β be complex numbers such that α + β and αβ are non-zero coprime
integers and α/β is not a root of unity. Put

un = (α
n − βn)/(α − β) for n ≥ 0.

The integers un are known as Lucas numbers and their divisibility properties have
been studied by Euler, Lagrange, Gauss, Dirichlet and others (see [11, Chapter
XVII]). In 1876 Lucas [24] announced several new results concerning Lucas se-
quences (un)
∞
n=0 and in a substantial paper in 1878 [25] he gave a systematic treat-
ment of the divisibility properties of Lucas numbers and indicated some of the
contexts in which they appeared. Much later Matijasevic [26] appealed to these
properties in his solution of Hilbert’s 10th problem.
For any integer m let P (m) denote the greatest prime factor of m with the
convention that P (m) = 1 when m is 1, 0 or −1. In 1912 Carmichael [8] proved
that if α and β are real and n > 12 then

P (un) ≥ n − 1. (1)

Results of this character had been established earlier for integers of the form
an − bn where a and b are integers with a > b > 0. Indeed Zsigmondy [49] in 1892
and Birkhoﬀ and Vandiver [6] in 1904 proved that for n > 2

P (an − bn) ≥ n + 1, (2)

while in the special case that b = 1 the result is due to Bang [4] in 1886.
In 1930 Lehmer [22] showed that the divisibility properties of Lucas numbers
hold in a more general setting. Suppose that (α + β)
2 and αβ are coprime non-zero
integers with α/β not a root of unity and, for n > 0, put

˜un =
 {(α
n − βn)/(α − β) for n odd,
(α
n − βn)/(α
2 − β2) for n even.

2000 Mathematics Subject Classiﬁcation. 11B39, 11J86.
Key words and phrases. greatest prime factor, recurrence sequences, Lucas numbers.
Research supported in part by the Canada Research Chairs Program and by Grant A3528 from
the Natural Sciences and Engineering Research Council of Canada.

1

2 C.L. STEWART

Integers of the above form have come to be known as Lehmer numbers. Observe
that Lucas numbers are also Lehmer numbers up to a multiplicative factor of α + β
when n is even. In 1955 Ward [45] proved that if α and β are real then for n > 18,

P (˜un) ≥ n − 1, (3)

and four years later Durst [13] observed that (3) holds for n > 12.
A prime number p is said to be a primitive divisor of a Lucas number un if
p divides un but does not divide (α − β)
2u2 · · · un−1. Similarly p is said to be
a primitive divisor of a Lehmer number ˜un if p divides ˜un but does not divide
(α
2 − β2)
2 ˜u3 · · · ˜un−1. For any integer n > 0 and any pair of complex numbers α
and β, we denote the n-th cyclotomic polynomial in α and β by Φn(α, β), so

Φn(α, β) =
 n∏

j=1
(j,n)=1

(α − ζjβ),

where ζ is a primitive n-th root of unity. One may check, see [38], that Φn(α, β) is
an integer for n > 2 if (α + β)
2 and αβ are integers. Further, see Lemma 6 of [38],
if, in addition, (α + β)
2 and αβ are coprime non-zero integers, α/β is not a root
of unity and n > 4 and n is not 6 or 12 then P (n/(3, n)) divides Φn(α, β) to at
most the ﬁrst power and all other prime factors of Φn(α, β) are congruent to 1 or
−1 modulo n. The last assertion can be strengthened to all other prime factors of
Φn(α, β) are congruent to 1 (mod n) in the case that α and β are coprime integers.
Since α
n − βn = ∏

d|n Φd(α, β), (4)

Φ1(α, β) = α − β and Φ2(α, β) = α + β we see that if n exceeds 2 and p is
a primitive divisor of a Lucas number un or Lehmer number ˜un then p divides
Φn(α, β). Further, a primitive divisor of a Lucas number un or Lehmer number ˜un
is not a divisor of n and so it is congruent to ±1 (mod n). Estimates (1), (2) and (3)
follow as consequences of the fact that the n-th term of the sequences in question
possesses a primitive divisor. It was not until 1962 that this approach was extended
to the case where α and β are not real by Schinzel [31]. He proved, by means of
an estimate for linear forms in two logarithms of algebraic numbers due to Gelfond
[17], that there is a positive number C, which is eﬀectively computable in terms of
α and β, such that if n exceeds C then ˜un possesses a primitive divisor. In 1974
Schinzel [35] employed an estimate of Baker [2] for linear forms in the logarithms
of algebraic numbers to show that C can be replaced by a positive number C0,
which does not depend on α and β, and in 1977 Stewart [39] showed C0 could be
taken to be e452467. This was subsequently reﬁned by Voutier [42, 43] to 30030. In
addition Stewart [39] proved that C0 can be taken to be 6 for Lucas numbers and
12 for Lehmer numbers with ﬁnitely many exceptions and that the exceptions could
be determined by solving a ﬁnite number of Thue equations. This program was
successfully carried out by Bilu, Hanrot and Voutier [5] and as a consequence they
were able to show that for n > 30 the n-th term of a Lucas or Lehmer sequence has
a primitive divisor. Thus (1) and (3) hold for n > 30 without the restriction that
α and β be real.
In 1962 Schinzel [30] asked if there exists a pair of integers a, b with ab diﬀerent
from ±2c2 and ±ch with h ≥ 2 for which P (an − bn) exceeds 2n for all suﬃciently

ON DIVISORS OF LUCAS AND LEHMER NUMBERS 3

large n. In 1965 Erd˝os [14] conjectured that

P (2n − 1)
n → ∞ as n → ∞.

Thirty ﬁve years later Murty and Wong [28] showed that Erd˝os’ conjecture is a
consequence of the abc conjecture [41]. They proved, subject to the abc conjecture,
that if ε is a positive real number and a and b are integers with a > b > 0 then

P (an − bn) > n2−ε,

provided that n is suﬃciently large in terms of a, b and ε. In 2004 Murata and
Pomerance [27] proved, subject to the Generalized Riemann Hypothesis, that

P (2n − 1) > n4/3/ log log n (5)

for a set of positive integers n of asymptotic density 1.
The ﬁrst unconditional reﬁnement of (2) was obtained by Schinzel [30] in 1962.
He proved that if a and b are coprime and ab is a square or twice a square then

P (an − bn) ≥ 2n + 1

provided that one excludes the cases n = 4, 6, 12 when a = 2 and b = 1. Schinzel
proved his result by showing that the term an − bn was divisible by at least 2
primitive divisors. To prove this result he appealed to an Aurifeuillian factorization
of Φn. Rotkiewicz [29] extended Schinzel’s argument to treat Lucas numbers and
then Schinzel [32, 33, 34] in a sequence of articles gave conditions under which
Lehmer numbers possess at least 2 primitive divisors and so under which (3) holds
with n + 1 in place of n − 1, see also [21]. In 1975 Stewart [37] proved that if κ is a
positive real number with κ < 1/ log 2 then P (an − bn)/n tends to inﬁnity with n
provided that n runs through those integers with at most κ log log n distinct prime
factors, see also [15]. Stewart [38] in the case that α and β are real and Shorey
and Stewart [36] in the case that α and β are not real generalized this work to
Lucas and Lehmer sequences. Let α and β be complex numbers such that (α + β)
2

and αβ are non-zero relatively prime integers with α/β not a root of unity. For
any positive integer n let ω(n) denote the number of distinct prime factors of n
and put q(n) = 2ω(n), the number of square-free divisors of n. Further let ϕ(n) be
the number of positive integers less than or equal to n and coprime with n. They
showed, recall (4), if n (> 3) has at most κ log log n distinct prime factors then

P (Φn(α, β)) > C(ϕ(n) log n)/q(n), (6)

where C is a positive number which is eﬀectively computable in terms of α, β and
κ only. The proofs depend on lower bounds for linear forms in the logarithms of
algebraic numbers in the complex case when α and β are real and in the p-adic case
otherwise.
The purpose of the present paper is to answer in the aﬃrmative the question
posed by Schinzel [30] and to prove Erd˝os’ conjecture in the wider context of Lucas
and Lehmer numbers.

Theorem 1. Let α and β be complex numbers such that (α + β)
2 and αβ are
non-zero integers and α/β is not a root of unity. There exists a positive number C,
which is eﬀectively computable in terms of ω(αβ) and the discriminant of Q(α/β),
such that for n > C,
 P (Φn(α, β)) > n exp(log n/104 log log n). (7)

4 C.L. STEWART

Our result, with the aid of (4) gives an improvement of (1), (2), (3) and (6),
answers the question of Schinzel and proves the conjecture of Erd˝os. Speciﬁcally, if
a and b are integers with a > b > 0 then

P (an − bn) > n exp(log n/104 log log n), (8)

for n suﬃciently large in terms of the number of distinct prime factors of ab. We
remark that the factor 104 which occurs on the right hand side of (7) has no
arithmetical signiﬁcance. Instead it is determined by the current quality of the
estimates for linear forms in p-adic logarithms of algebraic numbers. In fact we
could replace 104 by any number strictly larger than 14e2. The proof depends upon
estimates for linear forms in the logarithms of algebraic numbers in the complex
and the p-adic case. In particular it depends upon [48] where improvements upon
the dependence on the parameter p in the lower bounds for linear forms in p-adic
logarithms of algebraic numbers are established. This allows us to estimate directly
the order of primes dividing Φn(α, β). The estimates are non-trivial for small primes
and, coupled with an estimate from below for |Φn(α, β)|, they allow us to show
that we must have a large prime divisor of Φn(α, β) since otherwise the total non-
archimedean contribution from the primes does not balance that of |Φn(α, β)|. By
contrast for the proof of (6) a much weaker assumption on the greatest prime factor
is imposed and it leads to the conclusion that then Φn(α, β) is divisible by many
small primes. This part of the argument from [36] and [38] was also employed in
Murata and Pomerance’s [27] proof of (5) and in estimates of Stewart [40] for the
greatest square-free factor of ˜un.
For any non-zero integer x let ordpx denote the p-adic order of x. Our next
result follows from a special case of Lemma 8 of this paper. Lemma 8 yields a
crucial step in the proof of Theorem 1. An unusual feature of the proof of Lemma
8 is that we artiﬁcially inﬂate the number of terms which occur in the p-adic linear
form in logarithms which appears in the argument. We have chosen to highlight it
in the integer case.

Theorem 2. Let a and b be integers with a > b > 0. There exists a number C1,
which is eﬀectively computable in terms of ω(ab), such that if p is a prime number
which does not divide ab and which exceeds C1 and n is an integer with n ≥ 2 then

ordp(an − bn) < p exp(− log p/52 log log p) log a + ordpn. (9)

If a and b are integers with a > b > 0, p is an odd prime number which does not
divide ab and n ⩾ 2 then, as in the proof of Theorem 2,

ordp(an − bn) ≤ ordp(ap−1 − bp−1) + ordpn.

In particular if p exceeds C1 then

ordp(ap−1 − bp−1) < p exp(− log p/52 log log p) log a.

Yamada [46], by making use of a reﬁnement of an estimate of Bugeaud and Laurent
[7] for linear forms in two p-adic logarithms, proved that there is a positive number
C2, which is eﬀectively computable in terms of ω(a), such that

ordp(ap−1 − 1) < C2(p/(log p)
2) log a. (10)

ON DIVISORS OF LUCAS AND LEHMER NUMBERS 5

By following our proof of Theorem 1 and using (10) in place of Lemma 8 it is possible
to show that there exist positive numbers C3, C4 and C5, which are eﬀectively
computable in terms of ω(a) such that if n exceeds C3 then

P (an − 1) > C4 ϕ(n)(log n log log n) 1
2

and so, by Theorem 328 of [19],

P (an − 1) > C5 n(log n/ log log n) 1
2 . (11)
This gives an alternative proof of the conjecture of Erd˝os, although the lower bound
(11) is weaker than the bound (8).

The research for this paper was done in part during visits to the Hong Kong
University of Science and Technology, Institut des Hautes ´Etudes Scientiﬁques and
the Erwin Schr¨odinger International Institute for Mathematical Physics and I would
like to express my gratitude to these institutions for their hospitality. In addition I
wish to thank Professor Kunrui Yu for helpful remarks concerning the presentation
of this article and for our extensive discussions on estimates for linear forms in
p-adic logarithms which led to [48].

2. Preliminary lemmas

Let α and β be complex numbers such that (α+β)
2 and αβ are non-zero integers
and α/β is not a root of unity. We shall assume, without loss of generality, that

|α| ≥ |β|.

Observe that
 α = √
r + √
s
2 , β = √
r − √s
2
where r and s are non-zero integers with |r| ̸= |s|. Further Q(α/β) = Q(
√
rs). Note
that (α
2 − β2)
2 = rs and we may write rs in the form m2d with m a positive integer
and d a square-free integer so that Q(
√
rs) = Q(
√
d).
For any algebraic number γ let h(γ) denote the absolute logarithmic height of γ.
In particular if a0(x − γ1) · · · (x − γd) in Z[x] is the minimal polynomial of γ over
Z then
 h(γ) = 1
d
 

log a0 +
 d∑

j=1 log max(1, |γj|)



 .

Notice that

αβ(x − α/β)(x − β/α) = αβx
2 − (α
2 + β2)x + αβ = αβx
2 − ((α + β)
2 − 2αβ)x + αβ

is a polynomial with integer coeﬃcients and so either α/β is rational or the poly-
nomial is a multiple of the minimal polynomial of α/β. Therefore we have

h(α/β) ≤ log |α|. (12)

We ﬁrst record a result describing the prime factors of Φn(α, β).

Lemma 1. Suppose that (α + β)
2 and αβ are coprime. If n > 4 and n ̸= 6, 12 then
P (n/(3n)) divides Φn(α, β) to at most the ﬁrst power. All other prime factors of
Φn(α, β) are congruent to ±1 (mod n).

Proof. This is Lemma 6 of [38]. □

6 C.L. STEWART

Let K be a ﬁnite extension of Q and let ℘ be a prime ideal in the ring of algebraic
integers OK of K. Let O℘ consist of 0 and the non-zero elements α of K for which ℘
has a non-negative exponent in the canonical decomposition of the fractional ideal
generated by α into prime ideals. Then let P be the unique prime ideal of O℘ and
put K℘ = O℘/P. Further for any α in O℘ we let α be the image of α under the
residue class map that sends α to α + P in K℘.
Our next result is motivated by work of Lucas [25] and Lehmer [22].

Lemma 2. Let d be a square-free integer diﬀerent from 1, θ be an algebraic integer
of degree 2 over Q in Q(
√
d) and let θ′ denote the algebraic conjugate of θ over Q.
Suppose that p is a prime which does not divide 2θθ′. Let ℘ be a prime ideal of the
ring of algebraic integers of Q(
√
d) lying above p. The order of θ/θ′ in (Q(
√
d)℘)
×

is a divisor of 2 if p divides (θ2 − θ′2)
2 and a divisor of p − (d/p) otherwise.

Proof. We ﬁrst note that θ and θ′ are p-adic units. If p divides (θ2 − θ′2)
2 then
either p divides (θ − θ′)
2 or p divides θ + θ′ and in both cases (θ/θ′)
2 ≡ 1 (mod ℘).
Thus the order of θ/θ′ divides 2.
Thus we may suppose that p does not divide 2θθ′(θ2 − θ′2)
2 and, in particular,
p ∤ d. Since
 2θ = (θ + θ′) + (θ − θ′) and 2θ′ = (θ + θ′) − (θ − θ′) (13)

we see, on raising both sides of the above equations to the p-th power and subtract-
ing, that 2p(θp − θ′p) − 2(θ − θ′)
p is p(θ − θ′) times an algebraic integer. Hence,
since p is odd, θp − θ′p

θ − θ′ ≡ (θ − θ′)
p−1 (mod p).

But
 (θ − θ′)
p−1 = ((θ − θ′)
2) p−1
2 ≡ ( (θ − θ′)
2

p
 ) (mod p)

and ( (θ − θ′)
2

p
 ) = ( d
p
 ) ,

so θp − θ′p

θ − θ′ ≡ ( d
p
 ) (mod p). (14)

By raising both sides of equation (13) to the p-th power and adding we ﬁnd that

θp + θ′p

θ + θ′ ≡ (θ + θ′)
p−1 (mod p)

and since ( (θ+θ′)2

p ) = 1,
 θp + θ′p

θ + θ′ ≡ 1 (mod p). (15)

If ( d
p ) = −1 then adding (14) and (15) we ﬁnd that

2 θp+1 − θ′p+1

θ2 − θ′2 ≡ 0 (mod p)

hence, since p does not divide 2θθ′(θ2 − θ′2)
2,

(θ/θ′)
p+1 ≡ 1 (mod ℘)

ON DIVISORS OF LUCAS AND LEHMER NUMBERS 7

and the result follows. If ( d
p ) = 1 then subtracting (14) and (15) we ﬁnd that

2θθ′ θp−1 − θ′p−1

θ2 − θ′2 ≡ 0 (mod p)

hence, since p does not divide 2θθ′(θ2 − θ′2)
2,

(θ/θ′)p−1 ≡ 1 (mod ℘)

and this completes the proof. □

Let ℓ and n be integers with n ≥ 1 and for each real number x let π(x, n, ℓ)
denote the number of primes not greater than x and congruent to ℓ modulo n. We
require a version of the Brun-Titchmarsh theorem, see [18, Theorem 3.8].

Lemma 3. If 1 ≤ n < x and (n, ℓ) = 1 then

π(x, n, ℓ) < 3x/(ϕ(n) log(x/n)).

Our next result gives an estimate for the primes p below a given bound which
occur as the norm of an algebraic integer in the ring of algebraic integers of Q(α/β).

Lemma 4. Let d be a squarefree integer with d ̸= 1 and let pk denote the k-th
smallest prime of the form N πk = pk where N denotes the norm from Q(
√
d) to Q
and πk is an algebraic integer in Q(
√
d). Let ε be a positive real number. There is
a positive number C, which is eﬀectively computable in terms of ε and d, such that
if k exceeds C then
 log pk < (1 + ε) log k.

Proof. Let K = Q(
√
d) and denote the ring of algebraic integers of K by OK. A
prime p is the norm of an element π of OK provided that it is representable as the
value of the primitive quadratic form qK(x, y) given by x
2 − dy2 if d ̸≡ 1 (mod 4)
and x
2 + xy + ( 1−d
4 ) y2 if d ≡ 1 (mod 4). By [16, Chapter VII, (2.14)], a prime p is
represented by qK(x, y) if and only if p is not inert in K and all prime ideals ℘ of OK
above p have trivial narrow class in the narrow ideal class group of K. Let KH be the
strict Hilbert class ﬁeld of K. KH is normal over K and G, the Galois group of KH
over K, is isomorphic with the narrow ideal class group of K and so |G| = h+, the
strict ideal class number of K, see Theorem 7.1.2 of [10]. The prime ideals ℘ of OK
which do not ramify in KH and which are principal are the only prime ideals of OK
which do not ramify in KH and which split completely in KH , see Theorem 7.1.3
of [10]. These prime ideals may be counted by the Chebotarev Density Theorem.

Let [ KH /K
℘ ] denote the conjugacy class of Frobenius automorphisms corresponding
to prime ideals P of OKH above ℘. In particular, for each conjugacy class C of G
we deﬁne πC (x, KH /K) to be the cardinality of the set of prime ideals ℘ of OK
which are unramiﬁed in KH , for which [ KH /K
℘ ] = C and for which NK/Q℘ ≤ x.
Denote by C0 the conjugacy class consisting of the identity element of G. Note that
the number of inert primes p of OK for which NK/Q p ≤ x is at most x
1/2. Thus
the number of primes p up to x for which p is the norm of an element π of OK is
bounded from below by
 πC0(x, KH /K) − x
1/2. (16)

8 C.L. STEWART

It follows from Theorem 1.3 and 1.4 of [23] that there is a positive number C1,
which is eﬀectively computable in terms of d, such that for x greater than C1 the
quantity (16) exceeds x
2h+ log x .

Further x
2h+ log x > k

when x is at least 4h+k log k and
 k/ log k > 4h+. (17)

Thus, provided (17) holds and x exceeds C1,

pk < 4h+k log k. (18)

Our result now follows from (18) on taking logarithms. □

3. Estimates for linear forms in p-adic logarithms of algebraic
numbers

Let α1, . . . , αn be non-zero algebraic numbers and put K = Q(α1, . . . , αn) and
d = [K : Q]. Let ℘ be a prime ideal of the ring OK of algebraic integers in K lying
above the prime number p. Denote by e℘ the ramiﬁcation index of ℘ and by f℘ the
residue class degree of ℘. For α in K with α ̸= 0 let ord℘α be the exponent to which
℘ divides the principal fractional ideal generated by α in K and put ord℘0 = ∞.
For any positive integer m let ζm = e2πi/m and put α0 = ζ2u where ζ2u ∈ K and
ζ2u+1 ̸∈ K.
Suppose that α1, . . . , αn are multiplicatively independent ℘-adic units in K. Let
α0, α1, . . . , αn be the images of α0, α1, . . . , αn under the residue class map at ℘
from the ring of ℘-adic integers in K onto the residue class ﬁeld K℘ at ℘. For any
set X let |X| denote its cardinality. Let ⟨α0, α1, . . . , αn⟩ be the subgroup of (K℘)
×

generated by α0, α1, . . . , αn. We deﬁne δ by

δ = 1 if [K(α
1/2
0 , α
1/2
1 , . . . , α
1/2
n ) : K] < 2n+1

and δ = (pf℘ − 1)/|⟨α0, α1, . . . , αn⟩|
if [K(α
1/2
0 , α
1/2
1 , . . . , α
1/2
n ) : K] = 2n+1. (19)

Lemma 5. Let p be a prime with p ≥ 5 and let ℘ be an unramiﬁed prime ideal of
OK lying above p. Let α1, . . . , αn be multiplicatively independent ℘-adic units. Let
b1, . . . , bn be integers, not all zero, and put

B = max(2, |b1|, . . . , |bn|).

Then

ord℘(α
b1
1 · · · α
bn
n − 1) < Ch(α1) · · · h(αn) max(log B, (n + 1)(5.4n + log d))

where
 C = 376(n + 1)
1/2 (
7e p − 1
p − 2
 )n d
n+2 log∗ d log(e4(n + 1)d)·

max ( pfp

δ
 ( n
fp log p
 )n , enfp log p) .

ON DIVISORS OF LUCAS AND LEHMER NUMBERS 9

Proof. We apply the Main Theorem of [48] and in (1.16) we take C1(n, d, ℘, a)h(1)

in place of the minimum. Further (1.15) holds since our result is symmetric in the
bi’s. Next we note that, since ℘ is unramiﬁed and p ≥ 5, we may take c(1) = 1794,
a(1) = 7 p−1
p−2 , a(1)
0 = 2 + log 7 and a(1)
1 = a(1)
2 = 5.25. We remark that condition
(19) ensures that we may take {θ1, . . . , θn} to be {α1, . . . , αn}. Finally the explicit
version of Dobrowolski’s Theorem due to Voutier [44] allows us to replace the ﬁrst
term in the maximum deﬁning h(1) by log B. Therefore we ﬁnd that

ord℘(α
b1
1 · · · α
bn
n − 1) < C1h(α1) · · · h(αn) max(log B, G1, (n + 1)f℘ log p)

where
 G1 = (n + 1)((2 + log 7)n + 5.25 + log((2 + log 7)n + 5.25) + log d)

and, on denoting log max(x, e) by log∗ x,

C1 = 1794 (
7 ( p − 1
p − 2
 ))n (n + 1)
n+1

n! d
n+2 log∗ d
2u(f℘ log p)2

· max ( pf℘

δ
 ( n
f℘ log p
 )n , enf℘ log p) · max(log(e4(n + 1)d), f℘ log p).

Note that 2u ≥ 2 and f℘ log p ≥ log 5. Further, by Stirling’s formula, see 6.1.38
of [1], (n + 1)
n+1

n! ≤ en+1(n + 1)
1/2
√
2π
and so

ord℘(α
b1
1 · · · α
bn
n − 1) < C2h(α1) · · · h(αn) max ( log B
log 5 , G1
log 5 , n + 1) (20)

where
 C2 = 1794
2 e
√2π (n + 1)
1/2 (
7e p − 1
p − 2
 )n d
n+2 log∗ d

max ( pf℘

δ
 ( n
f℘ log p
 )n , enf℘ log p) (log(e4(n + 1)d)
log 5 . (21)

We next observe that G1 ≤ (n + 1)(5.4n + log d)

and as a consequence

max ( log B
log 5 , G1
log 5 , n + 1) = max ( log B
log 5 , (n + 1)(5.4n + log d)
log 5
 ) . (22)

The result now follows from (20), (21) and (22). □

4. Further preliminaries

Let (α + β)
2 and αβ be non-zero integers with α/β not a root of unity. We may
suppose that |α| ≥ |β|. Since there is a positive number c0 which exceeds 1 such
that |α| ≥ c0 we deduce from Lemma 3 of [39], see also Lemmas 1 and 2 of [35],
that there is a positive number c1 which we may suppose exceeds (log c0)
−1 such
that for n > 0

log 2 + n log |α| ≥ log |α
n − βn| ≥ (n − c1 log(n + 1)) log |α|. (23)

10 C.L. STEWART

The proof of (23) depends upon an estimate for a linear form in the logarithms of
two algebraic numbers due to Baker [2].
For any positive integer n let µ(n) denote the M¨obius function of n. It follows
from (4) that Φn(α, β) = ∏

d|n(α
n/d − βn/d)
µ(d). (24)

We may now deduce, following the approach of [35] and [39], our next result.

Lemma 6. There exists an eﬀectively computable positive number c such that if
n > 2 then |α|
ϕ(n)−cq(n) log n ≤ |Φn(α, β)| ≤ |α|ϕ(n)+cq(n) log n, (25)

where q(n) = 2ω(n).

Proof. By (24) log |Φn(α, β)| = ∑

d|n µ(d) log |α
n/d − βn/d|

and so by (23)
∣
∣
∣
∣
∣
∣
log |Φn(α, β)| − ∑

d|n µ(d) n
d log |α|
∣
∣
∣
∣
∣
∣ ≤ ∑

d|n
µ(d)̸=0
 c1 log(n + 1) log |α|

since c1 exceeds (log c0)
−1. Our result now follows. □

Lemma 7. There exists an eﬀectively computable positive number c1 such that if
n exceeds c1 then
 log |Φn(α, β)| ≥ ϕ(n)
2 log |α|. (26)

Proof. For n suﬃciently large

ϕ(n) > n/2 log log n and q(n) < n1/ log log n.

Since |α| ≥ c0 > 1 it follows from (25) that if n is suﬃciently large

|Φn(α, β)| > |α|ϕ(n)/2,

as required. □

Lemma 8. Let n be an integer larger than 1, let p be a prime which does not
divide αβ and let ℘ be a prime ideal of the ring of algebraic integers of Q(α/β)
lying above p which does not ramify. Then there exists a positive number C, which
is eﬀectively computable in terms of ω(αβ) and the discriminant of Q(α/β), such
that if p exceeds C then

ord℘((α/β)
n − 1) < p exp(− log p/51.9 log log p) log |α| log n.

Proof. Let c1, c2, . . . denote positive numbers which are eﬀectively computable in
terms of ω(αβ) and the discriminant of Q(α/β). We remark that since α/β is of
degree at most 2 over Q the discriminant of Q(α/β) determines the ﬁeld Q(α/β)
and so knowing it one may compute the class number and regulator of Q(α/β) as
well as the strict Hilbert class ﬁeld of Q(α/β) and the discriminant of this ﬁeld.
Further let p be a prime which does not divide 6dαβ where d is deﬁned as in the
ﬁrst paragraph of §2.

ON DIVISORS OF LUCAS AND LEHMER NUMBERS 11

Put K = Q(α/β) and
 α0 =
 {i if i ∈ K
−1 otherwise.

Let v be the largest integer for which

α/β = α
j
0θ2
v , (27)

with 0 ≤ j ≤ 3 and θ in K. To see that there is a largest such integer we ﬁrst note
that either there is a prime ideal q of OK, the ring of algebraic integers of K, lying
above a prime q which occurs to a positive exponent in the principal fractional ideal
generated by α/β or α/β is a unit. In the former case h(α/β) ≥ 2v−1 log q and in
the latter case, since α/β is not a root of unity, there is a positive number c1, see
[12], such that h(α/β) ≥ 2vc1.
Notice from (27) that h(α/β) = 2vh(θ). (28)

Further, by Kummer theory, see Lemma 3 of [3],

[K(α
1/2
0 , θ1/2) : K] = 4. (29)

Furthermore since p ∤ αβ and α and β are algebraic integers

ord℘((α/β)
n − 1) ≤ ord℘((α/β)
4n − 1). (30)

For any real number x let [x] denote the greatest integer less than or equal to x.
Put
 k = [ log p
51.8 log log p
 ] . (31)

Then, for p > c2, we ﬁnd that k ≥ 2 and

max
 (

p ( k
log p
 )k , ek log p
)
 = p ( k
log p
 )k . (32)

Our proof splits into two cases. We shall ﬁrst suppose that Q(α/β) = Q so that
α and β are integers. For any positive integer j with j ≥ 2 let pj denote the j − 1-th
smallest prime which does not divide pαβ. We put

m = n2v+2 (33)

and α1 = θ/p2 · · · pk.

Then
 θm − 1 = ( θ
p2 · · · pk
 )m pm
2 · · · pm
k − 1 = α
m
1 pm
2 · · · pm
k − 1 (34)

and by (27), (30), (33) and (34)

ordp((α/β)
n − 1) ≤ ordp(α
m
1 pm
2 · · · pm
k − 1). (35)

Note that α1, p2, . . . , pk are multiplicatively independent since α/β is not a root
of unity and p2, . . . , pk are primes which do not divide pαβ. Further, since p2, . . . , pk
are diﬀerent from p and p does not divide αβ, we see that α1, p2, . . . , pk are p-adic
units.

12 C.L. STEWART

We now apply Lemma 5 with δ = 1, d = 1, f℘ = 1 and n = k to conclude that

ordp(α
m
1 pm
2 · · · pm
k − 1) ≤ c3(k + 1)
3 log p (
7e p − 1
p − 2
 )k

max
 (

p ( k
log p
 )k , ek)
 (log m)h(α1) log p2 · · · log pk.

(36)

Put t = ω(αβ).

Let qi denote the i-th prime number. Note that

pk ≤ qk+t+1

and thus log p2 + · · · + log pk ≤ (k − 1) log qk+t+1.

By the prime number theorem with error term, for k > c4,

log p2 + · · · + log pk ≤ 1.001(k − 1) log k. (37)

By the arithmetic geometric mean inequality

log p2 · · · log pk ≤ ( log p2 + · · · + log pk
k − 1
 )k−1

and so, by (37), log p2 · · · log pk ≤ (1.001 log k)
k−1. (38)

Since h(α1) ≤ h(θ) + log p2 · · · pk it follows from (37) that

h(α1) ≤ c5h(θ)k log k. (39)

Further m = 2v+2n is at most n2
v+2 and so by (12) and (28)

h(θ) log m ≤ 4h(α/β) log n ≤ 4 log |α| log n. (40)

Thus, by (32), (35), (36), (38), (39) and (40),

ordp((α/β)
n − 1) < c6k4 log p (
7e p − 1
p − 2 1.001 k log k
log p
 )k p log |α| log n.

Therefore, by (31), for p > c7

ordp((α/β)
n − 1) < pe− log p
51.9 log log p log |α| log n. (41)

We now suppose that [Q(α/β) : Q] = 2. Let π2, . . . , πk be elements of OK with
the property that N (πi) = pi where N denotes the norm from K to Q and where
pi is a rational prime number which does not divide 2dpαβ. We now put θi = πi/π′
i
where π′
i denotes the algebraic conjugate of πi in Q(α/β). Notice that p does not
divide πiπ′
i = pi and if p does not divide (πi − π′
i)
2 then
( (πi − π′
i)
2

p
 ) = ( d
p
 ) ,

since Q(α/β) = Q(
√
d) = Q(πi). Thus, by Lemma 2, the order of θi in (Q(α/β)℘)
×

is a divisor of 2 if p divides π2
i − π′2
i and a divisor of p − ( d
p ) otherwise. Since p is

ON DIVISORS OF LUCAS AND LEHMER NUMBERS 13

odd and p does not divide d we conclude that the order of θi in (Q(α/β)℘)
× is a

divisor of p − ( d
p ) .
Put α1 = θ/θ2 · · · θk. (42)

Then
 θm − 1 = ( θ
θ2 · · · θk
 )m θm
2 · · · θm
k − 1

and, by (27), (30), (33) and (42),

ord℘((α/β)
n − 1) ≤ ord℘(α
m
1 θm
2 · · · θm
k − 1). (43)

Observe that α1, θ2, . . . , θk are multiplicatively independent since α/β is not a
root of unity, p2, . . . , pk are primes which do not divide αβ and the principal prime
ideals [πi] for i = 2, . . . , k do not ramify since p ∤ 2d. Further since p2, . . . , pk are
diﬀerent from p and p does not divide αβ we see that α1, θ2, . . . , θk are ℘-adic units.
Notice that

K(α
1/2
0 , θ1/2, θ1/2
2 , . . . , θ1/2
k ) = K(α
1/2
0 , α
1/2
1 , θ1/2
2 , . . . , θ1/2
k ).

Further [K(α
1/2
0 , θ1/2, θ1/2
2 , . . . , θ1/2
k ) : K] = 2k+1, (44)

since otherwise, by (29) and Kummer theory, see Lemma 3 of [3], there is an integer
i with 2 ≤ i ≤ k and integers j0, . . . , ji−1 with 0 ≤ jb ≤ 1 for b = 0, . . . , i − 1 and
an element γ of K for which
θi = α
j0
0 θj1 θj2
2 · · · θji−1
i−1 γ2. (45)

But the order of the prime ideal [πi] on the left-hand side of (45) is 1 whereas the
order on the right-hand side of (45) is even which is a contradiction. Thus (44)
holds.
Since p does not divide the discriminant of K and [K : Q] = 2 either p splits, in
which case f℘ = 1 and ( d
p ) = 1, or p is inert, in which case f℘ = 2 and ( d
p ) = −1,

see [20]. Observe that if ( d
p ) = 1 then

pfp /δ ≤ p. (46)

Let us now determine |⟨α0, θ, θ2, . . . , θk⟩| in the case ( d
p ) = −1. By our earlier

remarks the order of θi is a divisor of p + 1 for i = 2, . . . , k. Further by (27) since
N (α/β) = 1 we ﬁnd that N (θ) = ±1 and so N (θ2) = 1. By Hilbert’s Theorem
90, see eg. Theorem 14.35 of [9], θ2 = ̺/̺′ where ̺ and ̺′ are conjugate algebraic
integers in Q(α/β). Note that we may suppose that the principal ideals [̺] and [̺′]
have no principal ideal divisors in common. Further since p does not divide αβ
and, since ( d
p ) = −1, [p] is a principal prime ideal of OK and we note that p does

not divide ̺̺′. It follows from Lemma 2 that the order of θ2 in (Q(α/β)℘)
× is a
divisor of p + 1 hence θ has order a divisor of 2(p + 1). Since α
4
0 = 1 we conclude
that |⟨α0, θ, θ2, . . . , αk⟩| ≤ 2(p + 1)

and so δ = (p2 − 1)/|⟨α0, θ, θ2, . . . , θk⟩| ≥ (p − 1)/2. (47)

14 C.L. STEWART

We now apply Lemma 5 noting, by (46) and (47), that

pfp /δ ≤ 2p2/(p − 1).

Thus, by (32),

ord℘(α
m
1 θm
2 · · · θm
k − 1) ≤ c8(k + 1)
3 log p (
7e p − 1
p − 2
 )k 2kp ( k
log p
 )k

(log m)h(α1)h(θ2) · · · h(θk). (48)

Notice that θi = πi/π′
i and that pi(x − πi/π′
i)(x − π′
i/πi) = pix
2 − (π2
i + π′2
i )x + pi
is the minimal polynomial of θi over the integers since [πi] is unramiﬁed. Either the
discriminant of Q(α/β) is negative in which case |πi| = |π′
i| or it is positive in which
case there is a fundamental unit ε > 1 in OK. We may replace πi by πiεu for any
integer u and so without loss of generality we may suppose that p1/2
i ≤ |πi| ≤ p1/2
i ε
and consequently that p1/2
i ε−1 ≤ |π′
i| ≤ p1/2
i . Therefore

h(θi) ≤ 1
2 log piε2 = 1
2 log pi + log ε for d > 0

and
 h(θi) ≤ 1
2 log pi for d < 0.

Let us put
 R =
 {
log ε for d > 0
0 for d < 0.

Then
 h(θi) ≤ 1
2 log pi + R (49)

for i = 2, . . . , k. In a similar fashion we ﬁnd that

h(θ2 · · · θk) ≤ 1
2 log p2 · · · pk + R, (50)

and so
 h(α1) ≤ h(θ) + 1
2 log p2 · · · pk + R. (51)

Put t1 = ω(2dpαβ).

Let qi denote the i-th prime number which is representable as the norm of an
element of OK. Note that pk ≤ qk+t1
and thus log p2 + · · · + log pk ≤ (k − 1) log qk+t1 .

Therefore by Lemma 4 for k > c9,

log p2 + · · · + log pk ≤ 1.0005(k − 1) log k (52)

and so, as for the proof of (38),

log p2 · · · log pk ≤ (1.0005 log k)
k−1.

Accordingly, since pk ≥ k, for k > c10

2k−1h(θ2) · · · h(θk) ≤ (log p2 + 2R) · · · (log pk + 2R) ≤ (1.001 log k)
k−1. (53)

ON DIVISORS OF LUCAS AND LEHMER NUMBERS 15

Furthermore as for the proof of (39) and (40) we ﬁnd that from (51),

h(α1) ≤ c11h(θ)k log k (54)

and, from (12), (28) and (33),

h(θ) log m ≤ 8 log |α| log n. (55)

Thus by (43), (48), (51), (53), (54) and (55),

ord℘((α/β)
n − 1) < c12k4 log p (
7e ( p − 1
p − 2
 ) 1.001 k log k
log p
 )k p log |α| log n. (56)

Therefore, by (31), for p > c13 we again obtain (41) and the result follows. □

5. Proof of Theorem 1

Let c1, c2, . . . denote positive numbers which are eﬀectively computable in terms
of ω(αβ) and the discriminant of Q(α/β). Let g be the greatest common divisor of
(α + β)
2 and αβ. Note that ϕ(n) is even for n > 2 and that

Φn(α, β) = gϕ(n)/2Φn(α1, β1)

where α1 = α/√
g and β1 = β/√g. Further (α1 + β1)
2 and α1β1 are coprime and
plainly P (Φn(α, β)) ≥ P (Φn(α1, β1)).

Therefore we may assume, without loss of generality, that (α + β)
2 and αβ are
coprime non-zero integers.
By Lemma 7 there exists c1 such that if n exceeds c1 then

log |Φn(α, β)| ≥ ϕ(n)
2 log |α|. (57)

On the other hand

Φn(α, β) = ∏

p|Φn(α,β) pordpΦn(α,β) . (58)

If p divides Φn(α, β) then, by (4), p does not divide αβ and so

ordpΦn(α, β) ≤ ord℘((α/β)
n − 1), (59)

where ℘ is a prime ideal of OK lying above p. By Lemma 1 if p divides Φn(α, β)
and p is not P (n/(3, n)) then p is at least n − 1 and thus for n > c2, by Lemma 8,

ord℘((α/β)
n − 1) < p exp(− log p/51.9 log log p) log |α| log n. (60)

Put Pn = P (Φn(α, β)).

Then, by (58) and Lemma 1,

log |Φn(α, β)| ≤ log n + ∑

p≤Pn
p∤n
 log p ordpΦn(α, β). (61)

Comparing (57) and (61) and using (59) and (60) we ﬁnd that, for n > c3,

ϕ(n) log |α| < ∑

p≤Pn
p∤n
 c4(log p)p exp(− log p/51.9 log log p) log |α| log n

16 C.L. STEWART

hence ϕ(n)
log n < (π(Pn, n, 1) + π(Pn, n, −1))Pn exp(− log Pn/51.95 log log Pn),

and, by Lemma 3,

c5 ϕ(n)
log n < P 2
n
ϕ(n) log(Pn/n) exp(− log Pn/51.95 log log Pn).

Since ϕ(n) > c6n/ log log n,

Pn > n exp(log n/104 log log n),

for n > c7, as required.
 6. Proof of Theorem 2

Since p does not divide ab

ordp (an − bn) = ordp((a/g)
n − (b/g)
n)
where g is the greatest common divisor of a and b. Thus we may assume, without
loss of generality, that a and b are coprime. Put un = an − bn for n = 1, 2, · · ·
and let ℓ = ℓ(p) be the smallest positive integer for which p divides uℓ. Certainly ℓ
divides p − 1. Further, as in the proof of Lemma 3 of [38], if n and m are positive
integers then
 (un, um) = u(n,m).
Thus if p divides un then p divides u(n,ℓ). By the minimality of ℓ we see that
(n, ℓ) = ℓ so that ℓ divides n. In particular ℓ divides p − 1. Furthermore, by (4),
we see that
 ordpuℓ = ordpΦℓ(a, b).
If ℓ divides n then, by Lemma 2 of [38],

(un/uℓ, uℓ) divides n/ℓ, (62)
and so
 ordp up−1 = ordpuℓ (63)

Suppose that p divides Φn(a, b). Then p divides un and so ℓ divides n. Put n = tℓpk

with (t, p) = 1 and k a non-negative integer. Since Φn(a, b) divides un/un/t for t > 1
we see from (62), since (t, p) = 1, that t = 1. Thus n = ℓpk. For any positive integer
m
 ump/um = pb(m−1)p + (
p
2
)
b(m−2)pum + · · · + up−1
m

and if p is not 2 and p divides um then ordp(ump/um) = 1. It then follows that if
p is an odd prime then

ordpΦℓpk (a, b) = 1 for k = 1, 2, · · · .

ON DIVISORS OF LUCAS AND LEHMER NUMBERS 17

If n is a positive integer not divisible by ℓ = ℓ(p) then |un|p = 1. On the other
hand if ℓ divides n and p is odd then

|un|p = |uℓ|p · |n/ℓ|p. (64)

It now follows from (63) and (64) and the fact that ℓ ≤ p − 1 that if p is an odd
prime and ℓ divides n then
 |un|p = |up−1|p · |n|p. (65)

Therefore if p is an odd prime and n a positive integer

ordp(an − bn) ≤ ordp(ap−1 − bp−1) + ordpn, (66)

and our result now follows from (66) on taking n = p − 1 in Lemma 8.

References

[1] M. Abramowitz and I.A. Stegun, Handbook of Mathematical Functions with Formulas,
Graphs and Mathematical Tables, Dover Publications, New York, 1972.
[2] A. Baker, A sharpening of the bounds for linear forms in logarithms, Acta Arith. 21 (1972),
117–129.
[3] A. Baker and H.M. Stark, On a fundamental inequality in number theory, Ann. Math. 94
(1971), 190–199.
[4] A.S. Bang, Taltheoretiske undersøgelser, Tidsskrift for Mat. 4 (1886), 70–78, 130–137.
[5] Y. Bilu, G. Hanrot and P.M. Voutier, Existence of primitive divisors of Lucas and Lehmer
numbers, J. reine angew. Math. 539 (2001), 75–122.
[6] G.D. Birkhoﬀ and H.S. Vandiver, On the integral divisors of an − bn, Ann. Math. 5 (1904),
173–180.
[7] Y. Bugeaud and M. Laurent, Minoration eﬀective de la distance p-adique entre puissances de
nombres alg´ebriques, J. Number Theory 61, (1996) 311-342.
[8] R.D. Carmichael, On the numerical factors of the arithmetic forms αn ± βn, Ann. Math. 15
(1913), 30–70.
[9] H. Cohn, A classical invitation to algebraic numbers and class ﬁelds, Springer-Verlag, New
York, 1978.
[10] H. Cohn, Introduction to the construction of class ﬁelds, Cambridge studies in advanced
mathematics 6, Cambridge University Press, Cambridge, 1985.
[11] L.E. Dickson, History of the theory of numbers, Vol. I, The Carnegie Institute of Washington,
New York, 1952.
[12] E. Dobrowolski, On a question of Lehmer and the number of irreducible factors of a polyno-
mial, Acta Arith. 34 (1979), 391–401.
[13] L.K. Durst, Exceptional real Lehmer sequences, Paciﬁc J. Math. 9 (1959), 437–441.
[14] P. Erd˝os, Some recent advances and current problems in number theory, Lectures on modern
mathematics, Vol. III (ed. T.L. Saaty), Wiley, New York, 1965, 196–244.
[15] P. Erd˝os and T.N. Shorey, On the greatest prime factor of 2p − 1 for a prime p and other
expressions, Acta Arith. 30 (1976), 257–265.
[16] A. Fr¨ohlich and M.J. Taylor, Algebraic number theory, Cambridge studies in advanced math-
ematics 27, Cambridge University Press, Cambridge, 1991.
[17] A.O. Gelfond, Transcendental and algebraic numbers, Dover Publications, New York, 1960.
[18] H. Halberstam and H.-E. Richert, Sieve methods, Academic Press, London, 1974.
[19] G.H. Hardy and E.M. Wright, An introduction to the theory of numbers, Oxford University
Press, 5th ed, Oxford (1979).
[20] E. Hecke, Lectures on the theory of algebraic numbers, Graduate Texts in Mathematics 77,
Springer-Verlag, New York, 1981.
[21] R. Juricevic, Lehmer numbers with at least 2 primitive divisors, Ph.D. thesis, University of
Waterloo, 2007.
[22] D.H. Lehmer, An extended theory of Lucas’ functions, Ann. Math. 31 (1930), 419–448.

18 C.L. STEWART

[23] J.C. Lagarias and A.M. Odlyzko, Eﬀective versions of the Chebotarev Density Theorem, in
Algebraic Number Fields (L-functions and Galois properties), edited by A. Fr¨ohlich, Aca-
demic Press, London, 1977, 409–464.
[24] E. Lucas, Sur les rapports qui existent entre la th´eorie des nombres et le calcul int´egral, C.R.
Acad. Sci. Paris 82 (1876), 1303–1305.
[25] E. Lucas, Th´eorie des fonctions num´eriques simplement p´eriodiques, Amer. J. Math. 1 (1878),
184–240, 289–321.
[26] Y. Matijasevic, Enumerable sets are diophantine (Russian), Dokl. Akad. Nauk SSSR 191
(1970), 279–282. Improved English translation: Soviet Math. Doklady 11 (1970), 354–357.
[27] L. Murata and C. Pomerance, On the largest prime factor of a Mersenne number, CRM Proc.
Lecture Notes 36, H. Kisilevsky and E.Z. Goren, editors, Amer. Math. Soc., Providence, R.I.,
2004, 209–218.
[28] R. Murty and S. Wong, The ABC conjecture and prime divisors of the Lucas and Lehmer
sequences, Number Theory for the Millennium III, edited by M.A. Bennett, B.C. Berndt,
N. Boston, H.G. Diamond, A.J. Hildebrand and W. Philipp, A.K. Peters, Natick, MA, 2002,
43–54.
[29] A. Rotkiewicz, On Lucas numbers with two intrinsic prime divisors, Bull. Acad. Polon. Sci.
S´er. Math. Astr. Phys. 10 (1962), 229–232.
[30] A. Schinzel, On primitive prime factors of an − bn, Proc. Cambridge Philos. Soc. 58 (1962),
555–562.
[31] A. Schinzel, The intrinsic divisors of Lehmer numbers in the case of negative discriminant,
Ark. Mat. 4 (1962), 413–416.
[32] A. Schinzel, On primitive prime factors of Lehmer numbers, I, Acta Arith. 8 (1963), 213–223.
[33] A. Schinzel, On primitive prime factors of Lehmer numbers, II, Acta Arith. 8 (1963), 251–257.
[34] A. Schinzel, On primitive prime factors of Lehmer numbers, III, Acta Arith. 15 (1968), 49–69.
[35] A. Schinzel, Primitive divisors of the expression An − Bn in algebraic number ﬁelds, J. reine
angew. Math. 268/269 (1974), 27–33.
[36] T.N. Shorey and C.L. Stewart, On divisors of Fermat, Fibonacci, Lucas and Lehmer numbers,
II, J. London Math. Soc. 23 (1981), 17–23.
[37] C.L. Stewart, The greatest prime factor of an − bn, Acta Arith. 26 (1975), 427–433.
[38] C.L. Stewart, On divisors of Fermat, Fibonacci, Lucas and Lehmer numbers, Proc. London
Math. Soc. 35 (1977), 425–447.
[39] C.L. Stewart, Primitive divisors of Lucas and Lehmer numbers, Transcendence theory: ad-
vances and applications (eds. A. Baker and D.W. Masser), Academic Press, London, 1977,
79–92.
[40] C.L. Stewart, On divisors of Fermat, Fibonacci, Lucas and Lehmer numbers, III, J. London
Math. Soc. 28 (1983), 211–217.
[41] C.L. Stewart and K. Yu, On the abc conjecture, II, Duke Math. J. 108 (2001), 169–181.
[42] P.M. Voutier, Primitive divisors of Lucas and Lehmer sequences, II, J. Th. Nombres Bordeaux
8 (1996), 251–274.
[43] P.M. Voutier, Primitive divisors of Lucas and Lehmer sequences, III, Math. Proc. Camb.
Phil. Soc. 123 (1998), 407–419.
[44] P.M. Voutier, An eﬀective lower bound for the height of algebraic numbers, Acta Arith. 74
(1996), 81–95.
[45] M. Ward, The intrinsic divisors of Lehmer numbers, Ann. Math. 62 (1955), 230–236.
[46] T. Yamada, A note on the paper by Bugeaud and Laurent “Minoration eﬀective de la distance
p-adique entre puissances de nombres alg´ebriques”, J. Number Theory 130, (2010) 1889-1897.
[47] K. Yu, P −adic logarithmic forms and group varieties I, J. reine angew. Math. 502 (1998),
29–92.
[48] K. Yu, New advances in p-adic theory of logarithmic forms, to appear.
[49] K. Zsigmondy, Zur Theorie der Potenzreste, Monatsh. Math. 3 (1892), 265–284.

C.L. Stewart, Department of Pure Mathematics, University of Waterloo, Waterloo,
Ontario, Canada, email: cstewart@uwaterloo.ca
