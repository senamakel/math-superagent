<!-- source: https://arxiv.org/pdf/1908.07095 | converted from PDF -->

Nonuniform Distributions of Residues of Prime
Sequences in Prime Moduli

David Wu
Abstract

For positive integers q, Dirichlet’s theorem states that there are inﬁnitely many
primes in each reduced residue class modulo q. A stronger form of the theorem states
that the primes are equidistributed among the ϕ(q) reduced residue classes modulo q.
This paper considers patterns of sequences of consecutive primes (pn, pn+1, . . . , pn+k)
modulo q. Numerical evidence suggests a preference for certain prime patterns. For
example, computed frequencies of the pattern (a, a) modulo q up to x are much less
than the expected frequency π(x)/ϕ(q)2. We begin to rigorously connect the Hardy-
Littlewood prime k-tuple conjecture to a conjectured asymptotic formula for the fre-
quencies of prime patterns modulo q.

1 Introduction

Analytic number theory uses real and complex analysis techniques to prove properties about
the integers. It turns out that many properties of prime numbers are encoded in the proper-
ties of special functions. For example, the behavior of the zeros of the Riemann zeta function
strengthens a famous asymptotic formula known as the Prime Number Theorem (PNT) [1].
The Riemann Hypothesis (RH), one of the most well-known open problems in number the-
ory, conjectures that all nontrivial zeros of the Riemann zeta function have real part 1
2; RH
would imply a stronger form of PNT.
The Riemann zeta function is only one of a more general class of functions, the Dirichlet
L-functions. Peter Dirichlet [2] used these L-functions to prove that arithmetic progressions
with coprime ﬁrst term and common diﬀerence contain an inﬁnite number of primes: this
is Dirichlet’s theorem. Dirichlet’s use of L-functions invoked the realm of analysis to prove
statements about integers, thus beginning the study of analytic number theory.
The ϕ(d) classes of residues modulo d coprime to d are referred to as the reduced residue
classes, where ϕ(n) is Euler’s totient function. For example, the set of residues congruent
to 1 modulo 4 is a reduced residue class. Applying Dirichlet’s theorem to the arithmetic
progression with ﬁrst term 1 and common diﬀerence 4 shows that there are inﬁnitely many
primes in the reduced residue class 1 modulo 4. A natural followup question asks how prime
sequences are distributed among the reduced residue classes modulo d.
Before we discuss the distribution of primes among reduced residue classes, we introduce
a few standard deﬁnitions. Let π(x) be the usual prime counting function, i.e. the number of
primes less than or equal to x. Furthermore, let p(x) ∼ q(x) denote asymptotic equivalence,
i.e. lim
x→∞ p(x)
q(x) = 1. We also make extensive use of big O notation. We say f (x) = O(g(x))

1arXiv:1908.07095v1  [math.NT]  19 Aug 2019
if there exists some absolute constant C such that |f (x)| ≤ C|g(x)| for suﬃciently large x.
The similar notation f (x) = On(g(x)) means the constant C in the deﬁnition of O(g(x))
depends on n.
A key idea in analytic number theory is to compare a discrete function such as π(x) to
a continuous function such as the logarithmic integral li(x) = ´ x
2 dt
log t . The famous Prime
Number Theorem states that π(x) ∼ li(x), and Schoenfeld [3] showed that RH implies that
|π(x) − li(x)| < √x log x
8π , for x ≥ 2657.
We introduce notation analogous to π(x) for the purposes of this discussion following
Lemke Oliver and Soundararajan’s notation [4]. Let pn refer to the nth prime when the
primes are listed in increasing order, the pattern a = (a1, a2, . . . , ak) be a vector of length k,
and q ≥ 3 be a positive integer. Deﬁne

π(x; q, a) = #{pn ≤ x : pn+i−1 ≡ ai (mod q) for 1 ≤ i ≤ k}.

This notation counts the number of consecutive prime sequences that follow the pattern a
modulo q. Using this notation, the PNT for arithmetic progressions applied to the simple
case where a = (a) yields
 π(x; q, a) ∼ li(x)
ϕ(q). (1.1)

Although (1.1) shows that primes are roughly equidistributed among the reduced residue
classes modulo q, Chebyshev [5] observed that there are almost always more primes of the
form 4k + 3 than of the form 4k + 1; this bias was explained by Rubinstein and Sarnak [6]
to arise from the error term of O(x1/2+ϵ) in PNT when assuming RH. Chebyshev’s bias is
one of the ﬁrst mentions of nonuniform behavior of the primes when reduced modulo q.
Larger biases manifest when the length of a is greater than or equal to 2 that cannot be
solely attributed to error terms of size O(x1/2+ϵ). In [4] the frequencies of consecutive prime
pairs modulo 10 are tabulated, and it was observed that π(10
8; 10, (1, 1)) ≈ 4.62 × 10
6 and
π(10
8; 10, (9, 1)) ≈ 7.99 × 10
6, both of which are very diﬀerent than the expected frequency
of 10
8/ϕ(10)
2 = 6.25 × 10
6 predicted by naively generalizing (1.1) by replacing ϕ(q) with
ϕ(q)
2.
While it is known that primes are roughly equidistributed among reduced residue classes
according to (1.1), it is not known whether for arbitrary a with the length of a at least 2,
the modiﬁed prime counting function π(x; q, a) tends to inﬁnity as x tends to inﬁnity. Shiu
[7] proved that π(x; q, (a, a, . . . , a)) tends to inﬁnity as x tends to inﬁnity, and Maynard [8]
strengthened this to π(x; q, (a, a, . . . , a)) > Cπ(x) for some constant C and suﬃciently large
x. We can explain the preferences for certain prime patterns by appealing to conjectural
statements similar in nature to the PNT. For example, the Hardy-Littlewood prime k-tuple
conjecture gives us the density of speciﬁc tuples such as twin primes (p, p + 2) and twin sexy
primes (p, p + 2, p + 6) in a form analogous to that of the PNT. By appropriately combining
speciﬁc cases of the Hardy-Littlewood prime k-tuple conjecture, we obtain conjectures about
the density of the patterns modulo q.
As an example of how speciﬁc prime tuples relate to prime patterns, consider q = 3
and the pattern a = (1, 1). Then we are restricting our consideration to consecutive primes
(p1, p2) where p1 ≡ p2 ≡ 1 (mod 3). For m ≡ 1 (mod 3), these patterns include speciﬁc

2

tuples of the form (m, m + 6), (m, m + 12), (m, m + 18), and so on. The densities of these
speciﬁc tuples can be analyzed with the Hardy-Littlewood prime k-tuple conjectures. In this
manner, we obtain conjectures that partially account for the observed preferences for certain
patterns modulo q.
Lemke Oliver and Soundararajan [4] provide a conjectural explanation for the biases
for certain prime patterns. However, their heuristic argument omits lower order terms that
cause their conjectured form to not be in agreement with the data at smaller values of
x. We expand the conjecture to include further terms and begin rigorously connecting the
Hardy-Littlewood prime k-tuple conjecture and the main conjecture in [4].
In Section 2, we lay out the deﬁnitions and notation important to our discussion. In
Section 3, we determine the lower order terms by tightening the asymptotics in the heuristic
in [4]. In Section 4, we prove the lemmas necessary for the main proof. In Appendices A and
B, we account for discarded terms in the asymptotic formula for the conjectured behavior
to extend the form of an integral to more closely ﬁt the actual behavior of prime patterns
and extend our data gathering capabilities by 8 orders of magnitude. We identify a plausible
lower order term for the conjectured formula.

2 Preliminaries

We begin with the statement of the Hardy-Littlewood prime k-tuple conjecture. Heuristi-
cally, the conjecture generalizes the PNT by assuming the probability of an integer n being
prime as roughly 1
log n . While the integrand is derived by assuming primality is independent,
the constant in front of the integral corrects for this assumption.

Conjecture 2.1 (Hardy-Littlewood prime k-tuple conjecture). Let H be a ﬁnite set of
nonnegative integers and π(x, H) denote the number of integers n ≤ x such that n + h is a
prime for all h in H. Furthermore, let νp(H) denote the number of residue classes occupied
by the members of H modulo p. Then we have that

π(x, H) = S(H) ˆ x

2
 dt
(log t)|H| + O(x1/2+ϵ),

where the singular series is deﬁned as

S(H) = ∏

p prime
 1 − νp(H)
p
(1 − 1
p )|H| .

The singular series is modiﬁed in [9] to an inclusion-exclusion form

S0(H) = ∑

T ⊂H(−1)
|H\T |S(T ).

In [4], Lemke Oliver and Soundararajan modify the singular series to range over primes p
not dividing q to account for the prime patterns modulo q as follows.

Deﬁnition 2.1. The modiﬁed singular series Sq(H) is deﬁned to be

Sq(H) = ∏

p∤q
 1 − νp(H)
p
(1 − 1
p )|H| .
 3

Lemke Oliver and Soundararajan [4] introduce the same inclusion-exclusion form Sq,0
involving alternating sums of Sq is deﬁned to introduce cancellations that lead to Conjecture
2.2. Let q ≥ 3 be a positive integer and a and b be reduced residue classes modulo q. Set
h ≡ b − a (mod q). Also, let pn be the nth prime. We are speciﬁcally interested in the case
where pn ≡ a (mod q) and pn+1 = pn + h; this guarantees pn+1 ≡ b (mod q). Let 1P(x) be
the prime indicator function, deﬁned to be 1 if x is prime and 0 otherwise; Lemke Oliver
and Soundararajan [4] start with the statement that

π(x; q, a, b) = ∑

n≤x
n≡a (mod q)
 1P(n)1P(n + h) ∏

0<t<h
(t+a,q)=1

(1 − 1P(n + t)). (2.1)

Following a series of manipulations and using a conjecture similar to the Hardy-Littlewood
prime k-tuple conjecture, they conjecture the following asymptotic for π(x; q, (a, b)) (see [4,
E4449–E4450] for more details).

Conjecture 2.2 (Lemke Oliver & Soundararajan [4]). Let

α(y) = 1 − q
ϕ(q) log y and ϵq(a, b) = #{0 < t < h : (t + a, q) = 1} − ϕ(q)
q h.

Then
 π(x; q, (a, b)) ∼ 1
q
 ˆ x

2 α(y)ϵq(a,b)Ç q
ϕ(q)α(y) log y
 å2D(a, b; y)dy,

where D(a, b; y) is deﬁned to be

∑

h>0
h≡b−a (mod q)
 ∑

A⊂{0,h}
 ∑

T ⊂[1,h−1]
(t+a,q)=1 ∀t∈T
 (−1)
|T |Sq,0(A ∪ T )

Ç q
ϕ(q)α(y) log y
 å|T |α(y)hϕ(q)/q.

We analyze the growth of D(a, b; y). For readability purposes, deﬁne logk x to be
log log . . . log
︸ ︷︷ ︸
k logs x, where log x is the natural logarithm.

3 A Closer Analysis of the Conjecture

We provide more precise asymptotics for π(x; q, (a, b)) as in Conjecture 2.2. Because q = 2
is trivial, we only consider the case where q is an odd prime. However, the results readily
generalize to composite q. In particular, we are interested in D(a, b; y), which is equal to

∑

h>0
h≡b−a (mod q)
 ∑

A⊂{0,h}
 ∑

T ⊂[1,h−1]
(t+a,q)=1 ∀t∈T
 (−1)
|T |Sq,0(A ∪ T )

Ç q
ϕ(q)α(y) log y
 å|T |α(y)
hϕ(q)/q, (3.1)

in accordance with [4]. Lemke Oliver and Soundararajan heuristically argue that the relevant
terms in (3.1) are those where A = T = ∅ and |A| + |T | = 2.
 4

We convert (3.1) into a form more friendly to partitioning by the size of T . Deﬁne for
convenience z = z(q, y) = q
ϕ(q)α(y) log y

and g = g(q, y) = α(y)
ϕ(q)/q.

We rewrite the innermost sum of (3.1) as a sum over ℓ element subsets of [1, h − 1] where ℓ
ranges from 0 to h − 1 to obtain

D(a, b; y) = ∑

h>0
h≡b−a (mod q)
 gh ∑

A⊂{0,h}
 h−1∑

ℓ=0(−z)ℓ ∑

T ⊂[1,h−1]
(t+a,q)=1 ∀t∈T
|T |=ℓ
 Sq,0(A ∪ T ). (3.2)

Evaluating (3.2) is diﬃcult because the terms are unwieldy when h is large. However,
recalling the role of h in (2.1), we see that large h correspond to large prime gaps. Lemma
4.3 constrains the behavior of large prime gaps and hence of (3.2) when h is large.
Let c be a suﬃciently large positive integer depending on n and deﬁne M = c log2 y.
We split the outermost sum over h in (3.2) into two regions: One with 0 < h ≤ M log y and
one with h > M log y. The sum where h > M log y counts contributions where gn > M log y.
However, this portion of the sum can only contribute if its terms exist at all, therefore, the
sum where h > M log y is bounded above by the probability that gn > M log y. Hence, by
Lemma 4.3, the sum where h > M log y is bounded above by 1
logc y . Thus, by controlling c,
we can discard the portion of the sum where h > M log y. For the remainder of this paper,
we consider h ≤ M log y.
For n = 0, 1, 2, Lemke Oliver and Soundararajan deﬁne Dn(a, b; y) to be the terms
obtained from (3.1) where |T | = n and A = T = ∅ or |A| + |T | = 2. However, note
that Dn(a, b; y) is precisely the term obtained by isolating the ℓ = n term in (3.2). Starting
the sum over ℓ in (3.2) at ℓ = n rather than ℓ = 0 is the ﬁrst step towards investigating

Dn(a, b; y). Deﬁne D≥n(a, b; y) = M log y∑

i≥n Di(a, b; y). Written explicitly, the terms of (3.2) we

are interested in are

D≥n(a, b; y) = ∑

0<h≤M log y
h≡b−a (mod q)
 gh ∑

A⊂{0,h}
 h−1∑

ℓ=n(−z)
ℓ ∑

T ⊂[1,h−1]
(t+a,q)=1 ∀t∈T
|T |=ℓ
 Sq,0(A ∪ T ). (3.3)

Furthermore, deﬁne

Ah,ℓ = ∑

T ⊂[1,h−1]
(t+a,q)=1
|T |=ℓ
 Sq,0(T ), Bh,ℓ = ∑

T ⊂[1,h−1]
(t+a,q)=1
|T |=ℓ
 Sq,0({0} ∪ T ),

Ch,ℓ = ∑

T ⊂[1,h−1]
(t+a,q)=1
|T |=ℓ
 Sq,0({h} ∪ T ), Dh,ℓ = ∑

T ⊂[1,h−1]
(t+a,q)=1
|T |=ℓ
 Sq,0({0, h} ∪ T ).
 5

We partition the summation in (3.3) into four terms S∅, S{0}, S{h}, and S{0,h}, based
on A. For example,
 S∅ = ∑

0<h<M log y
h≡b−a (mod q)
 gh h−1∑

ℓ=n(−z)ℓAh,ℓ, (3.4)

with S{0}, S{h}, and S{0,h} deﬁned analogously with sums over Bh,ℓ, Ch,ℓ, and Dh,ℓ, respec-
tively.
In order to handle Ah,ℓ, Bh,ℓ, Ch,ℓ, and Dh,ℓ, we modify the following result of Mont-
gomery and Soundararajan [9], which states the average order of S0. They show that

∑

T ⊂[1,h]
|T |=ℓ
 S0(T ) = µℓ
ℓ! (−h log h + Ah)
ℓ/2 + O(h
ℓ/2−1/7ℓ+ϵ), (3.5)

where µℓ is the ℓ th moment of the standard normal distribution and A is an absolute constant
between −1 and 0. We expect that ∑ Sq,0(T ) has a similar growth rate, up to minor
corrections such as the exact value of A and leading factors depending on q. Moreover, these
arguments used to justify Theorem 3.1 are expected to be robust against these modiﬁcations.
We prove the following theorem concerning the growth rates of S∅, S{0}, S{h}, and S{0,h},
which proves a weaker version of the claim in [4] that Dn(a, b; y) is On( (log2 y)n/2

(log y)n/2−1 ).

Theorem 3.1. Assuming that (3.5) holds in a similar form for Sq,0, we have that S∅,
S{0} log y, S{h} log y, and S{0,h}(log y)2 are all

On
Ç (log2 y)
n

(log y)n/2−1
 å
.

In particular, Dn(a, b; y) and D≥n(a, b; y) are both On( (log2 y)n

(log y)n/2−1 ), allowing us to truncate
D(a, b; y) at speciﬁc values of n and control the error terms in Conjecture 2.2.

We defer the proofs of Lemmas 4.1-4.4 used in the proof of Theorem 3.1 to Section 4.

Proof. We begin by evaluating S∅ according to (3.4). We are interested in the case where
q is prime, and thus ϕ(q) = q − 1 and α(y) = 1 − q
(q−1) log y . Because q is an odd prime,

ϕ(q)
q ≥ 2
3. Thus,
 1 − 3
2 log y ≤ α(y) < 1 − 1
log y .

For suﬃciently large y, the deﬁnition of z gives

z = q
ϕ(q)α(y) log y < 3
2(1 − 3
2 log y ) log y < 3
3
2 log y = 2
log y .

Appealing to our conjectured form for ∑ Sq,0 according to (3.5), we replace Ah,ℓ in (3.4)
with µℓ
ℓ! (−h log h + Ah)
ℓ/2 + O(h
ℓ/2−1/7ℓ+ϵ). Note that µℓ = 0 when ℓ is odd, so we analyze
the sum based on the parity of ℓ.
 6

Case 1: ℓ is even. For convenience, deﬁne m = ℓ/2. We split the single sum over h into a
sum over j, k and h and swap the order of summation so that (3.4) is less than

M log y−1∑

m= n
2
 M
log3 y∑

j=0
 (j+1) log3 y−1∑

k=j log3 y
 (k+1) log y∑

h=k log y+1
h≡b−a (mod q)
 ghÇ 2
log y
 å2mÇ µ2m
(2m)! (−h log h + Ah)
må
. (3.6)

We bound (3.6) above by a series of substitutions. Deﬁne B = −A > 0 and take the
absolute value of the terms of (3.6). Lemma 4.1 implies (h log h + Bh)
m has an upper bound
of 2
m[(h log h)
m + (Bh)
m], where we include the extra factor of 2 for convenience. Because

g = (
1 − q
ϕ(q) log y
 )ϕ(q)/q and ϕ(q)
q ≥ 2
3, We have

g <
 Ç1 − 3
2 log y
 å2/3 < e
−2/(3 log y).

Thus, gh has an upper bound of e
−2j log3 y log y/(3 log y) = (log2 y)
−2j/3. We then maximize
all instances of h by replacing h with hmax = (k + 1) log y and remove the sum over h by
multiplying the summand by log y. Finally, note that µ2m = (2m − 1)!!, so µ2m
(2m)! = 1
2mm!.
These substitutions yield

M log y−1∑

m= n
2
 M
log3 y∑

j=0
 (j+1) log3 y−1∑

k=j log3 y
 (log y)
1−2m

(log2 y)2j/3
 Ç 2
2m

2mm!(2m[(hmax log hmax)
m + (Bhmax)
m])

å
. (3.7)

Applying Lemma 4.1 to (log hmax)
m = (log(k + 1) + log2 y)m implies

(hmax log hmax)
m ≤ (2(k + 1) log y)
m[(log(k + 1))m + (log2 y)m]. (3.8)

Substituting (3.8) into (3.7), distributing the factor of (2/ log y)
2m, and cancelling the factor
of 2m yields

M log y−1∑

m= n
2
 M
log3 y∑

j=0
 (j+1) log3 y−1∑

k=j log3 y
 log y
(log2 y)2j/3
 Ñ 1
m!
 ñÇ8(k + 1) log(k + 1)
log y
 åm

+
 Ç8(k + 1) log2 y
log y
 åmôé

.

Again, we maximize k and remove the sum over k by multiplying by log3 y, leaving

M log y−1∑

m= n
2
 M
log3 y∑

j=0
 log y log3 y
(log2 y)2j/3
 Ñ 1
m!
 ñÇ8((j + 1) log3 y)(log(j + 1) + log4 y))
log y
 åm

+
 Ç8(j + 1) log2 y log3 y
log y
 åmôé

. (3.9)

7

We split the sum in (3.9) up into four cases based on the value of j.
Case 1A: j = 0. When j = 0, the sum in (3.9) becomes

log y log3 y
 M log y−1∑

m= n
2
 1
m!
 ñÇ8 log3 y log4 y
log y
 åm +
 Ç8 log2 y log3 y
log y
 åmô
. (3.10)

Note that (3.10) is a truncated Taylor polynomial of ex. We show that (3.10) is O(f (n)),
where f (n) is the ﬁrst term of the truncated Taylor polynomial. With this in mind, because
the summation in (3.10) is a truncated series of positive terms, it is less than the value of
the complete Taylor series e8 log3 y log4 y/ log y + e
8 log2 y log3 y/ log y.
Simplifying and noting that (loga y)b is O(log y) for any a ≥ 2 and b ≥ 0, Lemma 4.2,
whose statement and proof can be found in Appendix 4, implies that the expression is O(1).
Because the Taylor series is O(1), the growth rate of (3.10) for varying n is determined by
the ﬁrst term. Hence, (3.10) is
 On
( (log2 y)
n/2(log3 y)
n/2+1

(log y)n/2−1
 )
. (3.11)

Case 1B: j = 1. Analyzing the j = 1 term follows similar logic; the asymptotic we obtain is
also
 On
( (log2 y)
n/2(log3 y)
n/2+1

(log y)n/2−1
 )
. (3.12)

Case 1C: 2 ≤ j < 3 log2 y
2 log3 y . Because j ≥ 2, we know

(log2 y)
−2j/3 < (log2 y)
−4/3 < 1
log2 y .

We also know that j+1 ≤ 3 log2 y
2 log3 y . Maximizing (log2 y)−2j/3 and j+1, removing the summation

by multiplying by 3 log2 y
2 log3 y , and cancelling log( log2 y
log3 y
 ) with log4 y yields

3 log y
2
 M log y−1∑

m= n
2
 1
m!
 ñÇ12 log2 y log3 y
log y
 åm +
 Ç12(log2 y)
2

log y
 åmô
. (3.13)

As before, the sum in (3.13) is a truncated Taylor series that is O(1). Hence, (3.13) is

On
Ç (log2 y)
n

(log y)n/2−1
 å
. (3.14)

Case 1D: 3 log2 y
2 log3 y ≤ j ≤ M
log3 y . When j > 3 log2 y
2 log3 y , the factor (log2 y)−2j/3 is no greater than
(log2 y)
− log2 y/ log3 y = 1
log y . Substituting for (log2 y)
−j with 1
log y and j + 1 with M
log3 y , which
is allowed because M
log3 y + 1 is the same size as M
log3 y , the summation in (3.9) becomes, after
simpliﬁcation,
 M log y−1∑

m= n
2
 M
log3 y∑

j= log2 y
log3 y
 log3 y
Ñ 1
m!
 ñÇ8M log M
log y
 åm +
 Ç8M log2 y
log y
 åmôé

. (3.15)

8

We remove the summation in (3.15) by multiplying the summand by M
log3 y , truncate the
resulting Taylor series, and apply Lemma 4.2 to obtain the ﬁnal contribution from this case
as (8c)n/2

(n/2)!
 [ (c log2 y)n/2+1(log3 y)n/2

(log y)n/2 + (log2 y)n+1

(log y)n/2
 ] = On
Ç(log2 y)n+1

(log y)n/2
 å. (3.16)

Case 2: ℓ is odd. We proceed analogously to the even ℓ case, noting that if an arbitrary
function f is O(h
ℓ/2−1/7ℓ+ϵ), then f is also O(h
ℓ/2). Therefore, for odd ℓ, (3.4) is less than

M −1∑

k=0
 (k+1) log y∑

h=k log y+1
h≡b−a (mod q)
 gh h−1∑

ℓ=n
ℓ odd
(−z)
ℓO(h
ℓ/2). (3.17)

For ℓ ∈ [0, M − 1], let Cℓ be the implied constant in the O(h
ℓ/2) term. Deﬁning Cmax =
max{Cℓ} allows us to pull −Cmax out of the sum and remove the big O notation. We also
switch the order of sums in (3.17) to obtain

−Cmax
 M log y∑

ℓ=n
ℓ odd
 M log y∑

h>max{ℓ,log y} ghzℓh
ℓ/2. (3.18)

Since h ≥ log y, we know gh ≤ e
−2h/3 log y. It thus follows that z < 2
log y and h ≤ M log y.
Thus, maximizing gh, zℓ, and h
ℓ/2 implies that (3.18) has an upper bound of

−Cmax
 M log y∑

ℓ=n
ℓ odd
 Ç 2
log y
 åℓ(M log y)
ℓ/2 M log y∑

h>max{ℓ,log y} e−2h/3 log y.

The sum over h is a geometric series that is less than e−2/3

1−e−2/3 log y , which is less than log y for

log y > 1. Next, we distribute the ( 2
log y
 )ℓ into (M log y)ℓ/2 and sum the resulting geometric
series; this yields
 −Cmax log y (4M/ log y)n/2(1 − (4M/ log y)
M log y+1)
1 − M/ log y . (3.19)

For large y, both 1 − (M/ log y)M log y+1 and 1 − M/ log y are O(1). Thus, (3.19) becomes

−Cmax M n/2

(log y)n/2−1 = On
( (log2 y)n/2

(log y)n/2−1
 )
. (3.20)

Note that for suﬃciently large y, each of the cases based on j are smaller than (3.14).
Thus, the contributions from Cases 1A, 1B, 1D, and 2 as stated in (3.11), (3.12), (3.16), and
(3.20), respectively, are all smaller than the contribution from Case 1C as stated in (3.14).
Therefore, S∅ = On( (log2 y)n

(log y)n/2−1 ), as desired.
Lemma 4.4 implies that summations of Bh,ℓ, Ch,ℓ, or Dh,ℓ are closely related to sum-
mations of Ah,ℓ. In order to take advantage of the cancellation suggested by the form
Bh−1,ℓ−1 = Ah,ℓ − Ah−1,ℓ, we consider the sign of A
′′
h,ℓ = ∂2
∂h2 Ah,ℓ. Namely, if A
′′
h,ℓ > 0, then

A′
h−1,ℓ < Ah,ℓ − Ah−1,ℓ < A
′
h,ℓ.
 9

Otherwise, if A′′
h,ℓ < 0, then
 A′
h−1,ℓ > Ah,ℓ − Ah−1,ℓ > A
′
h,ℓ.

Regardless of the sign of A
′′
h,ℓ, we insert the appropriate upper bound given by either A′
h,ℓ or
A
′
h−1,ℓ into S{0} and S{h}. In evaluating S{0,h}, we take A
′′′
h,ℓ and use appropriate bounds for
Ah,ℓ − 2Ah−1,ℓ + Ah−2,ℓ.
We proceed to evaluate S{0}, S{h}, and S{0,h} in an analogous manner to the method of
evaluating S∅. In loose terms, taking k derivatives of Ah,ℓ corresponds to adding a factor
of (log y)k to the denominator of the asymptotic in Theorem 3.1, thus leading to S{0} log y,
S{h} log y, and S{0,h}(log y)
2.
Recall that from the deﬁnition of S∅, S{0}, S{h}, and S{0,h}, the relevant contribution to
D≥n(a, b; y), after discarding terms where h > M log y, is S∅ +S{0} +S{h} +S{0,h}. Therefore,
D≥n(a, b; y) is On( (log2 y)n

(log y)n/2−1 ) as well. Since

Dn(a, b; y) = D≥n+1(a, b; y) − D≥n(a, b; y),

it is also On( (log2 y)n

(log y)n/2−1 ). Thus, the theorem is proved.

4 Proofs of the Lemmas

We now prove the lemmas that were used to prove the main theorem.

Lemma 4.1. Let a and b be nonnegative real numbers and n be a positive integer. Then

(a + b)n ≤ 2
n−1(an + bn).

Proof. Since xn is convex for nonnegative x and positive integers n, Jensen’s inequality yields
( a
2 + b
2)n ≤ 1
2an + 1
2bn. Clearing denominators gives (a + b)
n ≤ 2
n−1(an + bn), as desired.

Lemma 4.2. For any real constants a and c, we have

lim
x→∞
(log x)c(log2 x)a/ log x = 1.

Proof. Since the limit L = lim
x→∞(log x)(log2 x)a/ log x

does not depend on c, we set c = 1; if we prove L = 1 then certainly L
c = 1 and the lemma
follows. Taking logarithms, it suﬃces to show that

lim
x→∞ (log2 x)
a

log x = 0.

However, any power of log2 t grows slower than log t for all suﬃciently large t, so the limit
indeed equals 0. The lemma is thus proved.
 10

Lemma 4.3. Let N be a real number and P[gn > x] denote the probability that the gap gn
between the nth and (n + 1)th prime is greater than x for 1 ≤ n ≤ N . Then

lim
N →∞ P[gn > c log2 pN log pn] < 1
(log N )c .

We sketch the details of the proof here. Although not fully rigorous, we expect the key
ingredients of the proof to be present.

Proof. In the following proof, we omit the limits as N goes to inﬁnity for readability. Gal-
lagher [10] showed that P[1 ≤ n ≤ N | gn > λ log pn] < e
−λ.

Setting λ = c log2 pN implies P[gn > c log2 pN log pn] < 1
(log pN )c . It is clear that pN > N ;
hence 1
(log pN )c < 1
(log N )c .

Thus,
 P[gn > c log2 pN log pn] < 1
(log N )c ,

as desired.

Lemma 4.4. The sums over subsets of [1, h − 1] of size ℓ, given by Ah,ℓ, Bh,ℓ, Ch,ℓ, and Dh,ℓ,
satisfy the following relations:

Bh−1,ℓ−1 = Ch−1,ℓ−1 = Ah,ℓ − Ah−1,ℓ,
Dh−1,ℓ−1 = Ah,ℓ − 2Ah−1,ℓ + Ah−2,ℓ.

Proof. Note that Ah,ℓ is a sum that ranges over all subsets T of [1, h − 1]. We can partition
this sum by max{T }. Setting m = max{T }, we can write

Ah,ℓ =
 h−1∑

m=ℓ
 ∑

T ∈[1,m−1]
|T |=ℓ−1
(t+a,q)=1
 Sq,0({m} ∪ T ). (4.1)

From Deﬁnition 2.1, Sq,0(T ) = Sq,0(s − T ) for any integer s. Using the translational
invariance of Sq,0 and noting that

Cm,ℓ−1 = ∑

T ∈[1,m−1]
|T |=ℓ−1
(t+a,q)=1
 Sq,0({m} ∪ T ),

we can rewrite (4.1) as Ah,ℓ = h−1∑

m=ℓ Cm,ℓ−1. Now consider Ah,ℓ − Ah−1,ℓ; every term in this

diﬀerence cancels except Ch−1,ℓ−1, so Ah,ℓ − Ah−1,ℓ = Ch−1,ℓ−1, as desired.
 11

Similarly, we can partition a sum over subsets T of [1, h − 1] to a sum over sets T whose
minimum value is m. Thus

Ah,ℓ =
 h−1∑

m=ℓ
 ∑

T ∈[m−ℓ+1,h−1]
|T |=ℓ−1
(t+a,q)=1
 Sq,0({m − ℓ} ∪ T ).

Translational invariance implies that

Bm,ℓ−1 = ∑

T ∈[m−ℓ+1,h−1]
|T |=ℓ−1
(t+a,q)=1
 Sq,0({m − ℓ} ∪ T ),

so Ah,ℓ − Ah−1,ℓ telescopes as before and only Bh−1,ℓ−1 remains. Therefore, Ah,ℓ − Ah−1,ℓ =
Bh−1,ℓ−1 as well.
Finally, in order to relate Ah,ℓ to Dh,ℓ, we write the sum over subsets of [1, h−1] as a sum
over m and over sets T where max{T } − min{T } = m. By translational invariance, because
there are h − m + 1 possibilities for min{T }, there are h − m + 1 copies of Sq,0({1, m} ∪ T ).
Hence, the deﬁnition for Ah,ℓ can be rewritten as

Ah,ℓ =
 h−1∑

m=ℓ
 ∑

T ∈[2,m−1]
|T |=ℓ−2
(t+a,q)=1
 (h − m + 1)Sq,0({1, m} ∪ T ). (4.2)

Recall that Dh,ℓ = ∑

T ⊂[1,h−1]
(t+a,q)=1
|T |=ℓ
 Sq,0({0, h} ∪ T ), so Ah,ℓ − Ah−1,ℓ = h−1∑

m=ℓ Dm,ℓ−1. Therefore, we

express (4.2) as Ah,ℓ = h−1∑

m=ℓ
(h − m + 1)Dm,ℓ−2. Note that the sum telescopes when two

successive diﬀerences are taken. What remains is Dh−1,ℓ−2 = (Ah,ℓ − Ah−1,ℓ) − (Ah−1,ℓ −
Ah−2,ℓ) = Ah,ℓ − 2Ah−1,ℓ + Ah−2,ℓ, as desired.

5 Acknowledgments

The author would like to thank his mentor Robert Burklund for his extremely helpful guid-
ance. He is also very grateful for the extensive advice and feedback provided by John Rickert
and Tanya Khovanova. The author would like to thank Robert Lemke Oliver for his helpful
comments on my ideas. Finally, the author would like to thank Lawrence Washington for
sacriﬁcing his own time to explain the background of the project.

A Numerical Results

The following simpliﬁed asymptotic for the case π(x; 3, (a, b)) is provided in [4]:

π(x; 3, (a, b)) = li(x)
4
 Ç1 ± 1
2 log x log
 Ç2π log x
q
 åå + O
Ç x
(log x)11/4
 å, (A.1)

12

with the plus or minus sign being plus if a ̸= b and minus if a = b.
We compare (A.1) to the actual behavior of the primes, and ﬁnd that because the
approximations that were necessary to arrive at (A.1), the data deviate from the conjectured
form. Using SageMath’s find fit function suggested a possible lower order term of size
O( (log2 x)2

(log x)2 ). We modiﬁed the data gathering process to approximate values of π(x; q, (a, b))
for x ≤ 10
18. Finally, we include more terms in the approximation of D(a, b; y) to improve
its accuracy in future work. Graphs may be found in Appendix B.
Lemke Oliver and Soundararajan [4] gathered values of π(x; q, (a, b)) up to x = 10
12.
We gathered data up to x = 10
18. We gathered complete raw data using SageMath for
1 ≤ x ≤ 10
10. For 1010 < x ≤ 10
18, a sampling technique was used to approximate the
ratio π(x; q, (a, b))/π(x). Lemke Oliver’s C++ code counts prime patterns in ﬁxed intervals
[X, Y ); the program was modiﬁed to only consider the ﬁrst 108 primes larger than X. We
used X = 10
b1 and Y = 10
b1+1 for 10 ≤ b1 ≤ 18. The program estimated pattern frequencies
at X + i · 10
b1 for 1 ≤ i ≤ 9.
Theorem 3.1 shows that the contributions S∅, S{0}, S{h}, and S{0,h} to D(a, b; y) decline
quickly with n. After dividing by li(x), the main terms in the main conjecture in [4] are of size
O(1), O( log log x
log x ), and O( 1
log x). When |T | = 6, Theorem 3.1 implies that S∅ ∈ O( (log2 y)6

(log y)2 ).
Thus, for n ≥ 6, S∅, S{0}, S{h}, and S{0,h} make negligible contributions to D. This implies
that long range correlations between prime patterns are negligible, which in turn implies
that even though we only take the ﬁrst 10
8 primes after X, the sample can be reasonably
assumed to be unbiased.
Following Cram´er’s model, we model primality as a binomial event with x being prime
with probability 1
log x and assume that primality of x and y are independent events. Then
the standard deviation of our sampling distribution is proportional to 1√C , where C is the
number of primes sampled in order to estimate the frequency of π(x; q, (a, b)) at x.
For each point estimate at X + i · 10
b1, we sampled with C = 10
8, giving a precision of
roughly 10−4. The sample gives a sampling frequency

fa,b = π(x + x0; q, (a, b)) − π(x; q, (a, b))
π(x + x0) − π(x) ,

where π(x + x0) − π(x) = 107. In a crude sense, the sampling frequency fa,b is the derivative
of π(x; q, (a, b)), so we used a Riemann sum with 10 equally spaced subintervals to estimate
π(X + i · 10
b1; q, (a, b)) from fa,b. We thus computed

∑b1
β=1 ∑9
α=1 fa,b[li((α + 1) · 10
β) − li(α · 10
β)]
li(9 · 10b1) . (A.2)

Note that (A.2) approximates the the ratio π(10b1+1;q,(a,b))
π(x) and hence allows us to extend our
data to x = 10
18.
We restate the conjectured form for π(x; q, (a, b)) as in Conjecture 2.2 for convenience
as
 π(x; q, (a, b)) ∼ 1
q
 ˆ x

2 α(y)ϵq(a,b)Ç q
ϕ(q)α(y) log y
 å2D(a, b; y)dy. (A.3)

13

The numerical model in [4] is evaluated by partitioning D(a, b; y) into ∑
n Dn(a, b; y) and
discarding Dn(a, b; y) for n ≥ 3. Thus Sq,0 is estimated only for zero and two term sets to
approximate D(a, b; y). For example, in [4], only the zero and two term sets for D1(a, b; y)
are considered. Lemke Oliver and Soundararajan then write

D1(a, b; y) ≈ − q
ϕ(q)α(y) log y
 ∑

h>0
h≡b−a (mod q)
 ∑

t∈[1,h−1]
(t+a,q)=1
 Sq,0({0, t}) + Sq,0({t, h}). (A.4)

However, Theorem 3.1 suggests that only considering zero and two term sets may not
accurate enough. Hence, we add terms to D0, D1, and D2, as well as truncating at D5 instead
of D2 to approximate D in (A.3). For example, recalling that D1(a, b; y) contains all terms
of (3.1) with |T | = 1, we write

D1(a, b; y) = − q
ϕ(q)α(y) log y
 ∑

h>0
h≡b−a (mod q)
 ∑

t∈[1,h−1]
(t+a,q)=1
 Sq,0({0, t})+Sq,0({t, h})+Sq,0({0, t, h}).

This is essentially (A.4) but with three term sets included. The values of singular series
Sq,0(H) were computed up to ﬁve term sets with max H ≤ 150 and prepared for future work
numerically integrating (A.3) by truncating at D5(a, b; y).

B Plots of Data and Model

This appendix contains the plots of raw data, extended data, curve ﬁtting.

Figure 1: The proportion π(x;3,(1,1))
π(x) for x0 ≤ x ≤ x1 where π(x0) = 104 and π(x1) = 109.

14

Figure 2: The extended data for (1, 1)
modulo 3. The slight bump at 5 · 10
10 is due
to combining the raw and sampled data.
 Figure 3: The extended data for (1, 2)
modulo 3. The slight bump at 5 · 10
10 is
due to stitching the raw data and sampled
data together.

Figure 4: The residuals when (A.1) is sub-
tracted from π(x; 3, (1, 1)) for x0 ≤ x ≤ x1
where π(x0) = 104 and π(x1) = 1018, using
the extended data.
 Figure 5: The residuals when curve ﬁtted
terms of size O((log2 y)
2/(log y)2) and (A.1)
are subtracted from π(x; 3, (1, 1)) for x0 ≤
x ≤ x1 where π(x0) = 104 and π(x1) = 1018,
using the extended data.

References

[1] T. M. Apostol, Introduction to Analytic Number Theory. Springer, 1998.

[2] P. G. L. Dirichlet, Beweis des Satzes, dass jede unbegrenzte arithmetische Progression,
deren erstes Glied und Diﬀerenz ganze Zahlen ohne gemeinschaftlichen Factor sind,
unendlich viele Primzahlen enth¨alt, p. 342–359. Cambridge Library Collection - Math-
ematics, Cambridge University Press, 2013.

[3] L. Schoenfeld, “Sharper Bounds for the Chebyshev functions θ(x) and ψ(x). ii,” Math-
ematics of Computation, vol. 30, no. 134, pp. 337–360, 1976.

[4] R. J. L. Oliver and K. Soundararajan, “Unexpected biases in the distribution of con-
secutive primes,” 2016.

[5] “Lettre de M. le Professeur Tch´ebychev `a M. Fuss sur un nouveaux th´eor`eme relatif
aux nombres premiers contenus dans les formes 4n + 1 et 4n + 3,” 1853.

[6] M. Rubinstein and P. Sarnak, “Chebyshev’s bias,” Experiment. Math., vol. 3, no. 3,
pp. 173–197, 1994.
 15

[7] D. K. Shiu, “Strings of congruent primes,” Journal of the London Mathematical Society,
vol. 61, no. 2, pp. 359–373, 2000.

[8] J. Maynard, “Dense clusters of primes in subsets,” Compositio Mathematica, vol. 152,
no. 7, pp. 1517–1554, 2016.

[9] H. L. Montgomery and K. Soundararajan, “Primes in short intervals,” Communications
in Mathematical Physics, 2004.

[10] P. Gallagher, “On the distribution of primes in short intervals,” Mathematika, vol. 23,
no. 1, pp. 4–9, 1976.
 16
