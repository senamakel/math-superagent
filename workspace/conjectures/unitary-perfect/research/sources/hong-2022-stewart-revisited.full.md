<!-- source: https://arxiv.org/pdf/2204.01858 | converted from PDF -->

arXiv:2204.01858v1  [math.NT]  4 Apr 2022Stewart’s Theorem revisited: suppressing the
norm ±1 hypothesis

Haojie Hong

April 6, 2022

Abstract
Let γ be an algebraic number of degree 2 and not a root of unity.
In this note we show that there exists a prime ideal p of Q(γ) satisfying
νp(γn − 1) ≥ 1, such that the rational prime p underlying p grows quicker
than n.

Contents

1 Introduction 1
2 Preliminary results 2
2.1 Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
2.2 Uniform explicit version of Stewart’s theorem . . . . . . . . . . . . . . . . . . . 3
2.3 Cyclotomic polynomials and primitive divisors . . . . . . . . . . . . . . . . . . 3
2.4 Estimates for the arimetical functions . . . . . . . . . . . . . . . . . . . . . . . 4
3 Proof of Theorem 1.2 4
3.1 Case (3.9) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
3.2 Case (3.10) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6

1 Introduction

Let P (m) denote the largest prime factor of integer m, with the convention
P (0) = P (±1) = 1. For any integer n, we denote the n-th cyclotomic polynomial
in x by Φn(x) as usual.
Schinzel [8] asked if there exists any integers a, b with ab ̸= ±2c2, ±ch(h ≥ 2)
such that P (an − bn) > 2n for all suﬃciently large n. Erd˝os [4] conjectured that
P (2n − 1) grows quicker than n.
Let un be the nth term of a Lucas sequence. In 2013, Stewart [10] gave a
lower bound of the largest prime factor of un, which is of the form
n exp(log n/104 log log n). What Stewart actually proved is the following, see [1,
Theorem 1.1].

Theorem 1.1. Let γ be a non-zero algebraic number, not a root of unity. De-
note ω(γ) the number of primes p of the ﬁeld K = Q(γ) with the property
νp(γ) ̸= 0. Let P be the biggest element of the set

{p: p is a rational prime lying below a prime p of K, with νp(Φn(γ)) ≥ 1}.

1

If γ satisﬁes one of the following conditions:

• γ ∈ Q,

• [Q(γ) : Q] = 2 and N γ = ±1.

There exists a n0, which is eﬀectively computable in terms of ω(γ) and the
discriminant of K, such that, for all n > n0,

P > n exp (log n/104 log log n) .

Using this result, Stewart answered questions of Schinzel and Erd˝os in a
wider context, see [10] for more historical details.
A totally explicit expression of n0 in the above theorem was given in [1],
which also showd that n0 depends only on the ﬁeld K = Q(γ) but not on ω(γ).
Let q and a be integers such that q ≥ 2 and |a| < 2√
q. Assume α and ¯α are
the roots of x
2 − ax + q. In [2], the authors concentrate on big prime factors of
#E(Fq) = q − a+ 1 = (α− 1)(¯α − 1), the order of group of Fq-points on a certain
elliptic curve E. A Stewart-type result was proved for recurrent sequences of
order 4 rather than Lucas sequence.
This article is motivated by [1] and [2], we prove the following theorem.

Theorem 1.2. Suppose γ is an algebraic number of degree 2 and not a root
of unity. Set n0 = exp exp(max{1010, 3|DK|}). Let n be a positive integer
satisfying n ≥ n0. There exists a prime ideal p of K = Q(γ) such that νp(γn −
1) ≥ 1 and the underlying rational prime p of p satisﬁes

p ≥ n exp (0.0001 log n
log log n
 ) .

Note that this theorem suppresses the assumption N γ = ±1 when [Q(γ) :
Q] = 2 in Theorem 1.1, and it can also be seen as a generalization of Schinzel’s
question and Erd˝os’ conjecture. The proof uses ingredients from [1] and [2], all
of which rely heavily on lower bound for p-adic logarithmic form.

2 Preliminary results

2.1 Notation

Denote by log+ = max{log, 0}, log− = min{log, 0}, log∗ = max{log, 1}.
Let K be a number ﬁeld of degree d. We denote by DK the discriminant of
K. Suppose γ ∈ K, h(γ) denotes the usual absolute logarithmic height of γ:

h(γ) = [K : Q]
−1 ∑

v∈MK dv log+ |γ|v,

where dv denotes the local degree. The places v ∈ MK are normalized to extend
standard places of Q.
 2

Let σ : K ֒→ C be an arbitrary complex embedding of K, p be a prime ideal
of the ring of integers OK. The following formulas are immediate consequences
of the above deﬁnition:

h(γ) = 1
d
 ( ∑

σ:K֒→C log+ |γσ| + ∑

p max{0, −νp(γ)} log N p
)
 . (2.1)

h(γ) = 1
d
 ( ∑

σ:K֒→C − log− |γσ| + ∑

p max{0, νp(γ)} log N p
)
 . (2.2)

2.2 Uniform explicit version of Stewart’s theorem

The following two theorems go back to Stewart, see [10, Lemma 4.3], but in
present form they are Theorem 1.4 and Theorem 1.5 of [1].

Theorem 2.1. Let γ be a non-zero algebraic number of degree d, not a root
of unity. Set p0 = exp(80000d(log∗d)
2). Then for every prime p of the ﬁeld
K = Q(γ) whose absolute norm N p satisﬁes N p ≥ p0, and every positive inte-
ger n we have

νp(γn − 1) ≤ N p exp (
−0.002d
−1 log N p
log log N p
 ) h(γ) log∗n.

Theorem 2.2. Let γ be a non-zero algebraic number of degree 2, not a root of
unity. Assume that N γ = ±1. Set p0 = exp exp(max{108, 2|DK|}), where DK
is the discriminant of the quadratic ﬁeld K = Q(γ). Then for every prime p
of K with underlying rational prime p ≥ p0, and every positive integer n we
have
 νp(γn − 1) ≤ p exp (
−0.001 log p
log log p
 ) h(γ) log∗n. (2.3)

2.3 Cyclotomic polynomials and primitive divisors

The following proposition, which is about eatimates of cyclotomic polynomials,
goes back to Schinzel [9], but in the present form, item 1 is [3, Theorem 3.1]
and item 2 is proved in [1, Proposition 8.1].

Proposition 2.3. 1. Let γ be an algebraic number. Then

h(Φn(γ)) = ϕ(n)h(γ) + O1(2ω(n) log(πn)),

where A = O1(B) means |A| ≤ B.

2. Let γ be a complex algebraic number of degree d, non-zero and not a root
of unity. Then
 log |Φn(γ)| ≥ −1014d
5h(γ) · 2ω(n) log∗n. (2.4)

3

Let K be a number ﬁeld of degree d and γ ∈ K × not a root of unity. We
consider the sequence un = γn − 1. Let p be a prime ideal of OK, We call p
primitive divisor of un if

νp(un) ≥ 1, νp(uk) = 0 (k = 1, . . . n − 1).

Let us recall some basic properties of primitive divisors. Items 1 of the following
proposition are well-known and easy, and item 2 is Lemma 4 of Schinzel [9]; see
also [3, Lemma 4.5].

Proposition 2.4. 1. Let p be a primitive divisor of un. Then νp(Φn(γ)) ≥ 1
and N p ≡ 1 mod n; in particular, N p ≥ n + 1.

2. Assume that n ≥ 2d+1. Let p be not a primitive divisor of un. Then
νp(Φn(γ)) ≤ νp(n).

2.4 Estimates for the arimetical functions

Denote by ϕ(n), ω(n), τ (n) the Euler’s totient function, the number of distnct
prime factors of n, the number of divisors of n, respectively.
We will use the following bounds for these arithmetic functions:

ϕ(n) ≥ 0.5 n
log log n (n ≥ 1020), (2.5)

ω(n) ≤ 1.4 log n
log log n (n ≥ 3), (2.6)

τ (n) ≤ exp (
1.1 log n
log log n
 ) (n ≥ 3). (2.7)

See [7, Theorem 15], [6, Th´eor`eme 11], [5, Theorem 1].

3 Proof of Theorem 1.2

Let P be the biggest element of the set

{p: p is a rational prime lying below a prime p of K, with νp(Φn(γ)) ≥ 1}.

It is suﬃcient to show that

P > n exp (0.0001 log n
log log n
 ) (3.1)

One may assume P ≤ n2, since otherwise there is nothing to prove.
By (2.2),

2h(Φn(γ)) = − log
− |Φn(γ)| − log− |Φn(γσ)| + ∑

p max{0, νp(Φn(γ))} log N p,

(3.2)

4

where σ is the generator of Gal(K/Q).
We use item 2 of Proposition 2.3,

− log− |Φn(γ)| − log− |Φn(γσ)| ≤ 26 · 1014h(γ) · 2ω(n) log n. (3.3)

We split the sum in (3.2):
∑

p max{0, νp(Φn(γ))} log N p = ∑

p primi-
tive
 + ∑

p non-
primitive
 = Σp + Σnp,

where p primitive, p non-primitive means those prime ideals p which are prim-
itive, non-primitive divisors of γn − 1, respectively. By item 2 of Proposition
2.4, Σnp ≤ ∑

p νp(n) log N p ≤ 2 log n. (3.4)

Thus h(Φn(γ)) ≤ 1016h(γ) · 2ω(n) log n + Σp/2 + log n. (3.5)

On the other hand, by item 1 of Proposition 2.3,

h(Φn(γ)) ≥ ϕ(n)h(γ) − 2ω(n) log(πn). (3.6)

Combining (3.5) and (3.6), we have

Σp/2 ≥ ϕ(n)h(γ) − 2ω(n) log(πn) − 1016h(γ)2ω(n) log n − log n. (3.7)

Inequalities (2.5), (2.6) and our assumption n ≥ n0 ≥ 1010 imply that the
right-hand side of (3.7) is bounded from below by 0.4ϕ(n)h(γ). Thus we get
the lower bound of Σp Σp ≥ 0.8ϕ(n)h(γ). (3.8)

Now primes may have residue degree 1 or 2. Denote by

Σp1 := ∑

p primitive
fp=1
 max{0, νp(Φn(γ))} log N p

and Σp2 := ∑

p primitive
fp=2
 max{0, νp(Φn(γ))} log N p.

We have either Σp1 ≥ 0.4ϕ(n)h(γ), (3.9)

or Σp2 ≥ 0.4ϕ(n)h(γ). (3.10)

5

3.1 Case (3.9)

By item 1 of Proposition 2.4, we have N p = p ≡ 1 mod n. Since n ≥ n0
and n0 = exp exp(max{1010, 3|DK|}) is bigger than p0 in Theorem 2.1, the
underlying prime p is bigger than p0. So Theorem 2.1 applies,

νp(Φn(γ)) = νp(γn − 1) ≤ p exp (
−0.001 log p
log log p
 ) h(γ) log n.

We obtain

Σp1 ≤ ∑

p≡1 mod n
p≤P
 max{0, νp(Φn(γ))} log p

≤ π(P ; n, 1)P exp (
−0.001 log n
log log n
 ) h(γ) log n log P,
 (3.11)

where π(P ; m, a) counts primes p ≤ x satisfying p ≡ a mod m. We estimate
trivially π(P ; n, 1) ≤ P/n. Thus

Σp1 ≤ 2P 2 exp (
−0.001 log n
log log n
 ) h(γ) (log n)
2

n . (3.12)

Combining this with (3.9) and use (2.5), we have

P 2 ≥ 0.1 n2

(log n)2 log log n exp(0.001 log n
log log n ).

This implies (3.1) for n ≥ n0.

3.2 Case (3.10)

In this case, since fp = 2, we write p instead of p. Suppose σ is the generator
of Gal(K/Q). For such p we have νp(γn − 1) = νp((γσ)
n − 1). Let β = γσ/γ,
we obtain the following inequalities:

νp(βn − 1) ≥ νp((γσ)
n − 1 − (γn − 1)) ≥ νp(γn − 1) ≥ νp(Φn(γ)).

Hence (3.10) implies ∑

p∈P νp(βn − 1) log p ≥ 0.2ϕ(n)h(γ). (3.13)

where P = {p : p is inert in K and νp(γn − 1) > 0}.

Denote vn = βn − 1. If νp(vn) > 0 then there exists a unique divisor d of n such
that p is primitive for vn/d. We denote it by dp. Since βn − 1 = ∏

d|n Φd(β),

νp(vn) ≤ νp(vn/dp ) + ∑

m|n
m̸=n/dp
 νp(Φm(β)).

6

By item 2 of Proposition 2.4,

∑

m|n
m̸=n/dp
 νp(Φm(β)) ≤ ∑

m|n νp(m) +
 7∑

m=1 νp(Φm(β)).

It follows that

∑

p∈P νp(βn − 1) log p ≤ νp(vn/dp ) log p + ∑

m|n log m +
 7∑

m=1
 ∑

p∈P νp(Φm(β)) log p.

(3.14)
Trivially ∑

m|n log m ≤ τ (n) log n. (3.15)

Notice that νp(Φm(β)) ≤ νp(vm) ≤ 1
2 νp((γm − (γσ)
m)
2)

and (γm − (γσ)
m)
2 is a rational integer of absolute value not exceeding
4(max{|γ|, |γσ|})
2m, we have
∑

p νp(vm) log p ≤ log 2 + m log+(max{|γ|, |γσ|}) ≤ log 2 + 2mh(γ). (3.16)

Hence 7∑

m=1
 ∑

p∈P νp(Φm(β)) log p ≤ 7 log 2 + 56h(γ). (3.17)

Combining (3.13)(3.14)(3.15)(3.17), we obtain
∑

p∈P νp(vn/dp ) log p ≥ 0.2ϕ(n)h(γ) − τ (n) log n − 56h(γ) − 7 log 2.

3.2.1 Big dp

Using (3.16),

∑

dp≥τ (n) log n
 ∑

p∈P νp(vn/dp ) log p ≤ 2nh(γ) ∑

d|n
d≥τ (n) log n
 1
d + τ (n) log 2.

The sum on the right is trivially bounded by

τ (n)
τ (n) log n = 1
log n .

Hence ∑

dp≥τ (n) log n νp(vn/dp ) log p ≤ 2nh(γ)
log n + τ (n) log 2.

7

Denote by P ′ the subset of P consisting of p with dp < τ (n) log n:

P ′ = {p ∈ P : dp < τ (n) log n}.

So we have
∑

p∈P ′ νp(vn/dp ) log p ≥0.2ϕ(n)h(γ) − τ (n) log n − 56h(γ) − 7 log 2

− 2nh(γ)
log n − τ (n) log 2.

Using (2.5)(2.7), since n ≥ exp exp(1010), we obtain
∑

p∈P ′ νp(vn/dp ) log p ≥ 0.1ϕ(n)h(γ). (3.18)

3.2.2 Small dp : dp < τ (n) log n

In subsections 3.2.2 and 3.2.3 of [2], the authors use estimates of counting func-
tion for S-units to bound #{d | n : d < τ (n) log n} and then give a upper bound
for #P ′. One can verify that these bounds are still eﬀective in our case, as
following:
 #{d | n : d < τ (n) log n} ≤ exp (
70 log n log log log n
(log log n)2
 ) . (3.19)

#P ′ ≤ ( P
n + 1) exp (
80 log n log log log n
(log log n)2
 ) . (3.20)

3.2.3 Using Theorem 2.2

By item 1 of Proposition 2.4, for p ∈ P ′, we have n | p2 − 1. Hence p > n1/2 ≥
n1/2
0 . Since n1/2
0 ≥ p0 = exp exp(max{108, 2|DK|}), Theorem 2.2 applies:

νp(βn − 1) ≤ p exp (
−0.001 log p
log log p
 ) h(β) log n

≤ 2P exp (
−0.0005 log n
log log n
 ) h(γ) log n. (3.21)

The last inequality holds because

p ≤ P, log p
log log p ≥ 1
2 log n
log log n , h(β) ≤ 2h(γ).

Since νp(vn/dp ) ≤ νp(βn − 1), we obtain,

∑

p∈P ′ νp(vn/dp ) log p ≤ 2P exp (
−0.0005 log n
log log n
 ) h(γ) log P log n#P ′. (3.22)

8

Combining (3.18)(3.22),

0.1ϕ(n)h(γ) ≤ 2P exp (
−0.0005 log n
log log n
 ) h(γ) log P log n#P ′.

Using (3.20) and (2.5), we obtain, for n ≥ exp exp(1010),

40P (P + n) log P ≥ n2

log n log log n exp ( log n(log log n − 160000 log log log n)
2000(log log n)2
 )

≥ n2 exp (
0.0004 log n
log log n
 ) .

Obviously P ≥ n, so we have

80P 2 log P ≥ n2 exp (
0.0004 log n
log log n
 ) ,

which implies (3.1) and we are done.

Acknowledgments The author thanks Yuri Bilu for checking the proof, pol-
ishing the exposition and helpful discussions. The author also acknowledges
support of China Scholarship Council grant CSC202008310189.

References

[1] Yuri Bilu, Haojie Hong, and Sanoli Gun, Uniform explicit Stewart’s theorem on prime
factors of linear recurrences, arXiv:2108.09857 (2021).

[2] Yuri Bilu, Haojie Hong, and Florian Luca, Big prime factors in orders of elliptic curves
over ﬁnite ﬁelds, arXiv:2112.07046 (2021).

[3] Yuri Bilu and Florian Luca, Binary polynomial power sums vanishing at roots of unity,
Acta Arith. 198 (2021), no. 2, 195–217. MR 4228301

[4] P. Erd˝os, Some recent advances and current problems in number theory, Lectures on
Modern Mathematics, Vol. III, pp. 196–244. Wiley, New York, 1965.

[5] J.-L. Nicolas and G. Robin, Majorations explicites pour le nombre de diviseurs de N ,
Canad. Math. Bull. 26 (1983), no. 4, 485–492. MR 716590

[6] Guy Robin, Estimation de la fonction de Tchebychef θ sur le k-i`eme nombre premier et
grandes valeurs de la fonction ω(n) nombre de diviseurs premiers de n, Acta Arith. 42
(1983), no. 4, 367–389. MR 736719

[7] J. Barkley Rosser and Lowell Schoenfeld, Approximate formulas for some functions of
prime numbers, Illinois J. Math. 6 (1962), 64–94. MR 137689

[8] A. Schinzel, On primitive prime factors of an − bn, Proc. Cambridge Philos. Soc. 58
(1962), 555–562. MR 0143728

[9] A. Schinzel, Primitive divisors of the expression An − Bn in algebraic number ﬁelds, J.
Reine Angew. Math. 268(269) (1974), 27–33. MR 344221

[10] Cameron L. Stewart, On divisors of Lucas and Lehmer numbers, Acta Math. 211 (2013),
no. 2, 291–314. MR 3143892

Haojie Hong: Institut de Math´ematiques de Bordeaux, Universit´e de Bor-
deaux & CNRS, Talence, France
 9
