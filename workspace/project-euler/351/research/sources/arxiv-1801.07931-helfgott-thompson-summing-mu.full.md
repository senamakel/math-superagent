<!-- source: https://arxiv.org/pdf/1801.07931 | converted from PDF -->

arXiv:1801.07931v3  [math.PR]  26 Aug 2020
On tail behaviour of stationary second-order Galton–Watson
processes with immigration

M´aty´as Barczy
∗,⋄, Zsuzsanna B˝osze
∗∗, Gyula Pap∗∗∗

* MTA-SZTE Analysis and Stochastics Research Group, Bolyai Institute, University of Szeged,
Aradi v´ertan´uk tere 1, H–6720 Szeged, Hungary.

** Institute for Mathematical Stochastics, Georg-August-Universit¨at G¨ottingen, Goldschmidt-
str. 7, 37077 G¨ottingen, Germany.

*** Bolyai Institute, University of Szeged, Aradi v´ertan´uk tere 1, H-6720 Szeged, Hungary.

e-mail: barczy@math.u-szeged.hu (M. Barczy), zsuzsanna.boesze@uni-goettingen.de (Zs.
B˝osze).

⋄ Corresponding author.
 Abstract

A second-order Galton–Watson process with immigration can be represented as a coor-
dinate process of a 2-type Galton–Watson process with immigration. Suﬃcient conditions
are derived on the oﬀspring and immigration distributions of a second-order Galton–
Watson process with immigration under which the corresponding 2-type Galton–Watson
process with immigration has a unique stationary distribution such that its common
marginals are regularly varying. In the course of the proof suﬃcient conditions are given
under which the distribution of a second-order Galton–Watson process (without immigra-
tion) at any ﬁxed time is regularly varying provided that the initial sizes of the population
are independent and regularly varying.

1 Introduction

Branching processes have been frequently used in biology, e.g., for modeling the spread of an in-
fectious disease, for gene ampliﬁcation and deampliﬁcation or for modeling telomere shortening,
see, e.g., Kimmel and Axelrod [18]. Higher-order Galton–Watson processes with immigration
having ﬁnite second moment (also called Generalized Integer-valued AutoRegressive (GINAR)
processes) have been introduced by Latour [19, equation (1.1)]. P´enisson and Jacob [21] used
higher-order Galton–Watson processes (without immigration) for studying the decay phase of an

2010 Mathematics Subject Classiﬁcations: 60J80, 60G70.
Key words and phrases: second-order Galton–Watson process with immigration, regularly varying distri-
bution, tail behavior.
Supported by the Hungarian Croatian Intergovernmental S & T Cooperation Programme for 2017-2018
under Grant No. 16-1-2016-0027. M´aty´as Barczy is supported by the J´anos Bolyai Research Scholarship of the
Hungarian Academy of Sciences.
 1

epidemic, and, as an application, they investigated the Bovine Spongiform Encephalopathy epi-
demic in Great Britain after the 1988 feed ban law. As a continuation, P´enisson [20] introduced
estimators of the so-called infection parameter in the growth and decay phases of an epidemic.
Recently, Kashikar and Deshmukh [16, 17] and Kashikar [15] used second order Galton–Watson
processes (without immigration) for modeling the swine ﬂu data for Pune, India and La-Gloria,
Mexico. Kashikar and Deshmukh [16] also studied their basic probabilistic properties such as
a formula for their probability generator function, probability of extinction, long run behavior
and conditional least squares estimation of the oﬀspring means. Higher-order Galton–Watson
processes with immigration are special multi-type Galton–Watson processes with immigration,
and to give an example for an application of such processes for modeling epidemics, for exam-
ple, we can mention D´enes et al. [7], where a 17-type Galton–Watson process with immigration
has been applied to describe the risk of a major epidemic in connection with the 2012 UEFA
European Football Championship took place in Ukraine and Poland between 8 June and 1 July
2012.

Let Z+, N, R, R+, R++, and R−− denote the set of non-negative integers, positive
integers, real numbers, non-negative real numbers, positive real numbers and negative real
numbers, respectively. For functions f : R++ → R++ and g : R++ → R++, by the notation
f (x) ∼ g(x), f (x) = o(g(x)) and f (x) = O(g(x)) as x → ∞, we mean that limx→∞ f (x)
g(x) = 1,

limx→∞ f (x)
g(x) = 0 and lim supx→∞ f (x)
g(x) < ∞, respectively. The natural basis of Rd will be
denoted by {e1, . . . , ed}. For x ∈ R, the integer part of x is denoted by ⌊x⌋. Every
random variable will be deﬁned on a probability space (Ω, A, P). Equality in distributions of
random variables or stochastic processes is denoted by D
=.

First, we recall the Galton–Watson process with immigration, which assumes that an indi-
vidual can reproduce only once during its lifetime at age 1, and then it dies immediately. The
initial population size at time 0 will be denoted by X0. For each n ∈ N, the population
consists of the oﬀsprings born at time n and the immigrants arriving at time n. For each
n, i ∈ N, the number of oﬀsprings produced at time n by the i
th individual of the (n − 1)th

generation will be denoted by ξn,i. The number of immigrants in the n
th generation will be
denoted by εn. Then, for the population size Xn of the n
th generation, we have

(1.1) Xn =
 Xn−1∑

i=1 ξn,i + εn, n ∈ N,

where ∑0
i=1 := 0. Here {
X0, ξn,i, εn : n, i ∈ N} are supposed to be independent non-negative
integer-valued random variables, and {ξn,i : n, i ∈ N} and {εn : n ∈ N} are supposed to
consist of identically distributed random variables, respectively. If εn = 0, n ∈ N, then we
say that (Xn)n∈Z+ is a Galton–Watson process (without immigration).

Next, we introduce the second-order Galton–Watson branching model with immigration.
In this model we suppose that an individual reproduces at age 1 and also at age 2, and
then it dies immediately. For each n ∈ N, the population consists again of the oﬀsprings born
at time n and the immigrants arriving at time n. For each n, i, j ∈ N, the number of

2

oﬀsprings produced at time n by the i
th individual of the (n − 1)th generation and by the
jth individual of the (n − 2)nd generation will be denoted by ξn,i and ηn,j, respectively,
and εn denotes the number of immigrants in the n
th generation. Then, for the population
size Xn of the n
th generation, we have

(1.2) Xn =
 Xn−1∑

i=1 ξn,i +
 Xn−2∑

j=1 ηn,j + εn, n ∈ N,

where X−1 and X0 are non-negative integer-valued random variables (the initial population
sizes). Here {
X−1, X0, ξn,i, ηn,j, εn : n, i, j ∈ N} are supposed to be non-negative integer-
valued random variables such that {(X−1, X0), ξn,i, ηn,j, εn : n, i, j ∈ N} are independent,
and {ξn,i : n, i ∈ N}, {ηn,j : n, j ∈ N} and {εn : n ∈ N} are supposed to consist of
identically distributed random variables, respectively. Note that the number of individuals
alive at time n ∈ Z+ is Xn + Xn−1, which can be larger than the population size Xn of
the n
th generation, since the individuals of the population at time n − 1 are still alive at
time n, because they can reproduce also at age 2. The stochastic process (Xn)n⩾−1 given
by (1.2) is called a second-order Galton–Watson process with immigration or a Generalized
Integer-valued AutoRegressive process of order 2 (GINAR(2) process), see, e.g., Latour [19].
Especially, if ξ1,1 and η1,1 are Bernoulli distributed random variables, then (Xn)n⩾−1 is also
called an Integer-valued AutoRegressive process of order 2 (INAR(2) process), see, e.g., Du
and Li [8]. If ε1 = 0, then we say that (Xn)n⩾−1 is a second-order Galton–Watson process
without immigration, introduced and studied by Kashikar and Deshmukh [16] as well.

The process given in (1.2) with the special choice η1,1 = 0 gives back the process given
in (1.1), which will be called a ﬁrst-order Galton–Watson process with immigration to make a
distinction.

For notational convenience, let ξ, η and ε be random variables such that ξ D
= ξ1,1, η D
= η1,1
and ε D
= ε1, and put mξ := E(ξ) ∈ [0, ∞], mη := E(η) ∈ [0, ∞] and mε := E(ε) ∈ [0, ∞].

If (Xn)n∈Z+ is a (ﬁrst-order) Galton–Watson process with immigration such that mξ ∈
(0, 1), P(ε = 0) < 1, and ∑∞
j=1 P(ε = j) log(j) < ∞, then the Markov process (Xn)n∈Z+
admits a unique stationary distribution µ, see, e.g., Quine [22]. If ε is regularly varying with
index α ∈ R++, i.e., P(ε > x) ∈ R++ for all x ∈ R++, and

lim
x→∞ P(ε > qx)
P(ε > x) = q−α for all q ∈ R++,

then, by Lemma E.5, ∑∞
j=1 P(ε = j) log(j) < ∞. The content of Theorem 2.1.1 in Basrak et
al. [3] is the following statement.

1.1 Theorem. Let (Xn)n∈Z+ be a (ﬁrst-order) Galton–Watson process with immigration such
that mξ ∈ (0, 1) and ε is regularly varying with index α ∈ (0, 2). In case of α ∈ [1, 2),
assume additionally that E(ξ2) < ∞. Then the tail of the unique stationary distribution µ

3

of (Xn)n∈Z+ satisﬁes

µ((x, ∞)) ∼
 ∞∑

i=0 m
iα
ξ P(ε > x) = 1
1 − m
α
ξ P(ε > x) as x → ∞,

and hence µ is also regularly varying with index α.

Note that in case of α = 1 and mε = ∞ Basrak et al. [3, Theorem 2.1.1] assume
additionally that ε is consistently varying (or in other words intermediate varying), but,
eventually, it follows from the fact that ε is regularly varying. Basrak et al. [3, Remark
2.2.2] derived the result of Theorem 1.1 also for α ∈ [2, 3) under the additional assumption
E(ξ3) < ∞ (not mentioned in the paper), and they remark that the same applies to all
α ∈ [3, ∞) (possibly under an additional moment assumption E(ξ⌊α⌋+1) < ∞).

In Barczy et al. [2] we study regularly varying non-stationary (ﬁrst-order) Galton–Watson
processes with immigration.

As the main result of the paper, in Theorem 2.1, in the same spirit as in Theorem 1.1, we
present suﬃcient conditions on the oﬀspring and immigration distributions of a second-order
Galton–Watson process with immigration under which its associated 2-type Galton–Watson
process with immigration has a unique stationary distribution such that its common marginals
are regularly varying. According to our knowledge, such a result has not been established so
far, e.g., we could not ﬁnd any reference which would address regularly varying GINAR(2)
processes. Our result and the applied technique might be extended to a p-th order Galton–
Watson branching process with immigration, however such an extension is not immediate, for
example, it is not clear what would replace the constant ∑∞
i=0 m
α
i in Theorem 2.1. More
generally, one can pose an open problem, namely, under what conditions on the oﬀspring
and immigration distributions of a general p-type Galton–Watson branching process with
immigration, its unique (p-dimensional) stationary distribution is jointly regularly varying. We
also note that there is a vast literature on tail behavior of regularly varying time series (see,
e.g., Hult and Samorodnitsky [12]), however, the available results do not seem to be applicable
for describing the tail behavior of the stationary distribution for regularly varying branching
processes. The link between GINAR and autoregressive processes is that their autocovariance
functions are identical under ﬁnite second moment assumptions, but we can not see that it
would imply anything for the tail behavior of a GINAR process knowing the tail behaviour of a
corresponding autoregressive process. Further, in our situation the second moment is inﬁnite,
so the autocovariance function is not deﬁned.

Very recently, B˝osze and Pap [5] have studied regularly varying non-stationary second-order
Galton–Watson processes with immigration. They have found some suﬃcient conditions on the
initial, the oﬀspring and the immigration distributions of a non-stationary second-order Galton-
Watson process with immigration under which the distribution of the process in question is
regularly varying at any ﬁxed time. The results in B˝osze and Pap [5] can be considered as
extensions of the results in Barczy et al. [2] on not necessarily stationary (ﬁrst-order) Galton–
Watson processes with immigration. Concerning the results in B˝osze and Pap [5] and in the

4

present paper, there is no overlap, for more details see Remark 2.2.

The paper is organized as follows. In Section 2, ﬁrst, for a second-order Galton–Watson
process with immigration, we give a representation of the unique stationary distribution and its
marginals, respectively, then our main result, Theorem 2.1, is formulated. The rest of Section
2 is devoted to the proof of Theorem 2.1. In the course of the proof, we formulate an auxiliary
result about the tail behaviour of a second-order Galton–Watson process (without immigration)
with a regularly varying initial distribution at time 0 and with value 0 at time −1, see
Proposition 2.3. We close the paper with seven appendices which are used throughout the
proofs. In Appendix A, we recall a representation of a second-order Galton–Watson process
without or with immigration as a (special) 2-type Galton–Watson process without or with
immigration, respectively. In Appendix B, we derive an explicit formula for the expectation of
a second-order Galton–Watson process with immigration at time n and describe its asymptotic
behavior as n → ∞. Appendix C is about the existence and estimation of higher order moments
of a second-order Galton–Watson process (without immigration). In Appendix D, we recall a
representation of the unique stationary distribution for a 2-type Galton–Watson process with
immigration. In Appendix E, we collect several results on regularly varying functions and
distributions, to name a few of them: convolution property, Karamata’s theorem and Potter’s
bounds. Appendix F is devoted to recall and (re)prove a result on large deviations for sums of
non-negative independent and identically distributed regularly varying random variables due
to Tang and Yan [26, part (ii) of Theorem 1]. Finally, in Appendix G, we present a variant of
Proposition 2.3, where the initial values X−1 and X0 are independent and regularly varying
together with a second type of proof, see Proposition G.1.

2 Tail behavior of the marginals of the stationary distri-
bution of second-order Galton–Watson processes with
immigration

Let (Xn)n⩾−1 be a second order Galton–Watson process with immigration given in (1.2), and
let us consider the Markov chain (Y k)k∈Z+ given by

Y n :=
 [
Yn,1
Yn,2
]
 :=
 [ Xn
Xn−1
]
 =
 Yn−1,1∑

i=1
 [
ξn,i
1
 ]
 +
 Yn−1,2∑

j=1
 [
ηn,j
0
 ]
 +
 [
εn
0
 ]
 , n ∈ N,

which is a (special) 2-type Galton–Watson process with immigration, and (e
⊤
1 Y k)k∈Z+ =
(Xk)k∈Z+, (e
⊤
2 Y k+1)k⩾−1 = (Xk)k⩾−1 (for more details, see Appendix A). If mξ ∈ R++,
mη ∈ R++, mξ + mη < 1, P(ε = 0) < 1 and E(1{ε̸=0} log(ε)) < ∞, then there exists a unique
stationary distribution π for (Y n)n∈Z+, see Appendix D, since then M ξ,η is primitive due
to the fact that
 M 2
ξ,η =
 [
mξ mη
1 0
 ]2
 =
 [m
2
ξ + mη mξmη
mξ mη
 ]
 ∈ R2
++.

5

Moreover, the stationary distribution π of (Y n)n∈Z+ has a representation

π D
=
 ∞∑

i=0 V (i)
i (εi),

where (V (i)
k (εi))k∈Z+, i ∈ Z+, are independent copies of a (special) 2-type Galton–Watson
process (V k(ε))k∈Z+ (without immigration) with initial vector V 0(ε) = ε and with the same
oﬀspring distributions as (Y k)k∈Z+, and the series ∑∞
i=0 V (i)
i (ε) converges with probability 1,
see Appendix D. Using the considerations for the backward representation in Appendix A, we
have (e
⊤
1 V k(ε))k∈Z+ = (Vk(ε))k∈Z+ and (e
⊤
2 V k+1(ε))k⩾−1 = (Vk(ε))k⩾−1, where (Vk(ε))k⩾−1
is a second-order Galton–Watson process (without immigration) with initial values V0(ε) = ε
and V−1(ε) = 0, and with the same oﬀspring distributions as (Xk)k⩾−1. Consequently, the
marginals of the stationary distribution π are the same distributions π, and it admits the
representation
 π D
=
 ∞∑

i=0 V (i)
i (εi),

where (V (i)
k (εi))k∈Z+, i ∈ Z+, are independent copies of (Vk(ε))k⩾−1. This follows also from
the fact that the stationary distribution π is the limit in distribution of Y n as n → ∞ and

Y n =
 [ Xn
Xn−1
]
 , n ∈ Z+,

thus the coordinates of Y n converge in distribution to the same distribution π as n → ∞.

Note that (Xn)n⩾−1 is only a second-order Markov chain, but not a Markov chain. More-
over, (Xn)n⩾−1 is strictly stationary if and only if the distribution of the initial population
sizes (X0, X−1)⊤ coincides with the stationary distribution π of the Markov chain (Y k)k∈Z+.

Indeed, if (X0, X−1)⊤ D
= π, then Y 0 D
= π, thus (Y k)k∈Z+ is strictly stationary, and hence

for each n, m ∈ Z0, (Y 0, . . . , Y n) D
= (Y m, . . . , Y n+m), yielding

(X0, X−1, X1, X0, . . . , Xn, Xn−1) D
= (Xm, Xm−1, Xm+1, Xm, . . . , Xn+m, Xn+m−1).

Especially, (X−1, X0, X1, . . . , Xn) D
= (Xm−1, Xm, Xm+1, . . . , Xn+m), hence (Xn)n⩾−1 is strictly
stationary. Since (Xm, Xm−1, Xm+1, Xm, . . . , Xn+m, Xn+m−1) is a continuous function of
(Xm−1, Xm, Xm+1, . . . , Xn+m), these considerations work backwards as well. Consequently,
π is the unique stationary distribution of the second-order Markov chain (Xn)n⩾−1.

2.1 Theorem. Let (Xn)n⩾−1 be a second-order Galton–Watson process with immigration such
that mξ ∈ R++, mη ∈ R++, mξ + mη < 1 and ε is regularly varying with index α ∈ (0, 2).
In case of α ∈ [1, 2), assume additionally that E(ξ2) < ∞ and E(η2) < ∞. Then the tail
of the marginals π of the unique stationary distribution π of (Xn)n⩾−1 satisﬁes

π((x, ∞)) ∼
 ∞∑

i=0 m
α
i P(ε > x) as x → ∞,

6

where m0 := 1 and

mk := λk+1
+ − λk+1
−
λ+ − λ− , λ+ := mξ + √m
2
ξ + 4mη

2 , λ− := mξ − √m
2
ξ + 4mη

2
(2.1)

for k ∈ N. Consequently, π is also regularly varying with index α.

Note that λ+ and λ− are the eigenvalues of the oﬀspring mean matrix M ξ,η given in
(B.2) related to the recursive formula (B.1) for the expectations E(Xn), n ∈ N. For each
k ∈ Z+, the assumptions mξ ∈ R++ and mη ∈ R++ imply mk ∈ R++. Further, by (B.4),
for all k ∈ Z+, we have mk = E(Vk,0), where (Vn,0)n⩾−1 is a second-order Galton–Watson
process (without immigration) with initial values V0,0 = 1 and V−1,0 = 0, and with the same
oﬀspring distributions as (Xn)n⩾−1. Consequently, the series ∑∞
i=0 m
α
i appearing in Theorem
2.1 is convergent, since for each i ∈ N, we have mi = E(Vi,0) ⩽ λi
+ < 1 by (B.5) and the
assumption mξ + mη < 1.

We point out that in Theorem 2.1 only the regular variation of the marginals π of π is
proved, the question of the joint regular variation of π remains open.

2.2 Remark. Note that there is no overlap between the results in the recent paper of B˝osze
and Pap [5] on non-stationary second-order Galton-Watson processes with immigration and in
the present paper. In [5] the authors always suppose that the initial values X0 and X−1
of a second-order Galton-Watson process with immigration (Xn)n⩾−1 are independent, so in
the results of [5] the distribution of (X0, X−1) can not be chosen as the unique stationary
distribution π, since the marginals of π are not independent in general. ✷

For the proof of Theorem 2.1, we need an auxiliary result on the tail behaviour of second-
order Galton–Watson processes (without immigration) having regularly varying initial distri-
butions.

2.3 Proposition. Let (Xn)n⩾−1 be a second-order Galton–Watson process (without immigra-
tion) such that X0 is regularly varying with index β0 ∈ R+, X−1 = 0, mξ ∈ R++ and
mη ∈ R+. In case of β0 ∈ [1, ∞), assume additionally that there exists r ∈ (β0, ∞) with
E(ξr) < ∞ and E(ηr) < ∞. Then for all n ∈ N,

P(Xn > x) ∼ m
β0
n P(X0 > x) as x → ∞,

where mi, i ∈ Z+, are given in Theorem 2.1, and hence, Xn is also regularly varying with
index β0 for each n ∈ N.

Proof of Proposition 2.3. Let us ﬁx n ∈ N. In view of the additive property (A.4), it is
suﬃcient to prove
 P
( X0∑

i=1 ζ (n)
i,0 > x

)
 ∼ m
β0
n P(X0 > x) as x → ∞.

7

This relation follows from Proposition E.13, since E(ζ (n)
1,0 ) = mn ∈ R++, n ∈ N, by (B.4). ✷

In Appendix G, we present a variant of Proposition 2.3, where the initial values X−1 and
X0 are independent and regularly varying together with a second type of proof, see Proposition
G.1.

Proof of Theorem 2.1. First, note that, by Lemma E.5, E(1{ε̸=0} log(ε)) < ∞. We will use
the ideas of the proof of Theorem 2.1.1 in Basrak et al. [3]. Due to the representation (A.4),
for each i ∈ Z+, we have
 V (i)
i (εi) D
=
 εi∑

j=1 ζ (i)
j,0,

where {εi, ζ (i)
j,0 : j ∈ N} are independent random variables such that {ζ (i)
j,0 : j ∈ N} are
independent copies of Vi,0, where (Vk,0)k⩾−1 is a second-order Galton–Watson process (without
immigration) with initial values V0,0 = 1 and V−1,0 = 0, and with the same oﬀspring
distributions as (Xk)k⩾−1. For each i ∈ Z+, by Proposition 2.3, we obtain P(V (i)
i (εi) >
x) ∼ m
α
i P(ε > x) as x → ∞, yielding that random variables V (i)
i (εi), i ∈ Z+, are also
regularly varying with index α. Since V (i)
i (εi), i ∈ Z+, are independent, for each n ∈ Z+,
by Lemma E.10, we have

P
( n∑

i=0 V (i)
i (εi) > x
) ∼
 n∑

i=0 m
α
i P(ε > x) as x → ∞,(2.2)

and hence the random variables ∑n
i=0 V (i)
i (εi), n ∈ Z+, are also regularly varying with index
α. For each n ∈ N, using that V (i)
i (εi), i ∈ Z+, are non-negative, we have

lim inf
x→∞ π((x, ∞))
P(ε > x) = lim inf
x→∞ P(∑∞
i=0 V (i)
i (εi) > x)
P(ε > x) ⩾ lim inf
x→∞ P(∑n
i=0 V (i)
i (εi) > x)
P(ε > x) =
 n∑

i=0 m
α
i ,

hence, letting n → ∞, we obtain

(2.3) lim inf
x→∞ π((x, ∞))
P(ε > x) ⩾
 ∞∑

i=0 m
α
i .

Moreover, for each n ∈ N and q ∈ (0, 1), we have

lim sup
x→∞ π((x, ∞))
P(ε > x) = lim sup
x→∞
 P(∑n−1
i=0 V (i)
i (εi) + ∑∞
i=n V (i)
i (εi) > x
)

P(ε > x)

⩽ lim sup
x→∞
 P(∑n−1
i=0 V (i)
i (εi) > (1 − q)x
) + P(∑∞
i=n V (i)
i (εi) > qx
)

P(ε > x) ⩽ L1,n(q) + L2,n(q)

with

L1,n(q) := lim sup
x→∞
 P(∑n−1
i=0 V (i)
i (εi) > (1 − q)x
)

P(ε > x) , L2,n(q) := lim sup
x→∞
 P(∑∞
i=n V (i)
i (εi) > qx
)

P(ε > x) .

8

Since ε is regularly varying with index α, by (2.2), we obtain

L1,n(q) = lim sup
x→∞
 P(∑n−1
i=0 V (i)
i (εi) > (1 − q)x
)

P(ε > (1 − q)x) · P(ε > (1 − q)x)
P(ε > x) = (1 − q)−α n−1∑

i=0 m
α
i

and

L2,n(q) = lim sup
x→∞
 P(∑∞
i=n V (i)
i (εi) > qx
)

P(ε > qx) · P(ε > qx)
P(ε > x) = q−α lim sup
x→∞
 P(∑∞
i=n V (i)
i (εi) > qx
)

P(ε > qx) ,

and hence
 lim
n→∞ L1,n(q) = (1 − q)−α ∞∑

i=0 m
α
i ,

lim
n→∞ L2,n(q) = q−α lim
n→∞ lim sup
x→∞
 P(∑∞
i=n V (i)
i (εi) > qx
)

P(ε > qx) .

The aim of the following discussion is to show

(2.4) lim
n→∞ lim sup
x→∞
 P(∑∞
i=n V (i)
i (εi) > qx
)

P(ε > qx) = 0, q ∈ (0, 1).

First, we consider the case α ∈ (0, 1). For each x ∈ R++, n ∈ N and δ ∈ (0, 1), we have

P
( ∞∑

i=n V (i)
i (εi) > x

)

= P

(∑

i⩾n V (i)
i (εi) > x, sup
i⩾n ̺
iεi > (1 − δ)x

)
 + P
(∑

i⩾n V (i)
i (εi) > x, sup
i⩾n ̺
iεi ⩽ (1 − δ)x

)

= P

(∑

i⩾n V (i)
i (εi) > x, sup
i⩾n ̺
iεi > (1 − δ)x

)

+ P
(∑

i⩾n V (i)
i (εi)1{εi⩽(1−δ)̺−ix} > x, sup
i⩾n ̺
iεi ⩽ (1 − δ)x

)

⩽ P(
sup
i⩾n ̺
iεi > (1 − δ)x
) + P
(
∑

i⩾n V (i)
i (εi)1{εi⩽(1−δ)̺−ix} > x

)
 =: P1,n(x, δ) + P2,n(x, δ),

where ̺ is given in (B.6). By subadditivity of probability,

P1,n(x, δ) ⩽ ∑

i⩾n P(̺
iεi > (1 − δ)x) = ∑

i⩾n P(ε > (1 − δ)̺
−ix).

Using Potter’s upper bound (see Lemma E.12), for δ ∈ (0, α
2 ), there exists x0 ∈ R++ such
that

(2.5) P(ε > (1 − δ)̺
−ix)
P(ε > x) < (1 + δ)[(1 − δ)̺
−i]
−α+δ < (1 + δ)[(1 − δ)̺
−i]− α
2

9

if x ∈ [x0, ∞) and (1 − δ)̺
−i ∈ [1, ∞), which holds for suﬃciently large i ∈ N due to
̺ ∈ (0, 1). Consequently, if δ ∈ (0, α
2 ), then

lim
n→∞ lim sup
x→∞ P1,n(x, δ)
P(ε > x) ⩽ lim
n→∞
 ∑

i⩾n (1 + δ)[(1 − δ)̺
−i]− α
2 = 0,

since ̺ α
2 < 1 (due to ̺ ∈ (0, 1)) yields ∑∞
i=0(̺
−i)−α/2 < ∞. Now we turn to prove that
limn→∞ lim supx→∞ P2,n(x,δ)
P(ε1>x) = 0. By Markov’s inequality,

P2,n(x, δ) ⩽ 1
x
 ∑

i⩾n E(V (i)
i (εi)1{εi⩽(1−δ)̺−ix}).

By the representation V (i)
i (εi) D
= ∑εi
j=1 ζ (i)
j,0, we have

E
(V (i)
i (εi)1{εi⩽(1−δ)̺−ix}) = E

( εi∑

j=1 ζ (i)
j,01{εi⩽(1−δ)̺−ix}
)
 = E
[

E

( εi∑

j=1 ζ (i)
j,01{εi⩽(1−δ)̺−ix}
 ∣
∣
∣
∣
∣ εi
)]

= E

( εi∑

j=1 E(ζ (i)
1,0)1{εi⩽(1−δ)̺−ix}
)
 = E(ζ (i)
1,0) E
(
εi1{εi⩽(1−δ)̺−ix})
,

since {ζ (i)
j,0 : j ∈ N} and εi are independent. Moreover,

E(εi1{εi⩽(1−δ)̺−ix}) = E
(ε1{ε⩽(1−δ)̺−ix}) = ∫ ∞

0 P(ε1{ε⩽(1−δ)̺−ix} > t
) dt

= ∫ (1−δ)̺−i x

0 P(t < ε ⩽ (1 − δ)̺
−ix) dt ⩽ ∫ (1−δ)̺−i x

0 P(ε > t) dt.

By Karamata’s theorem (see, Theorem E.11), we have

lim
y→∞
 ∫ y
0 P(ε > t) dt
y P(ε > y) = 1
1 − α ,

thus there exists y0 ∈ R++ such that
∫ y

0 P(ε > t) dt ⩽ 2y P(ε > y)
1 − α , y ∈ [y0, ∞),

hence ∫ (1−δ)̺−ix

0 P(ε > t) dt ⩽ 2(1 − δ)̺
−ix P(ε > (1 − δ)̺
−ix)
1 − α
whenever (1 − δ)̺
−ix ∈ [y0, ∞), which holds for i ⩾ n with suﬃciently large n ∈ N
and x ∈ [(1 − δ)−1̺
ny0, ∞) due to ̺ ∈ (0, 1). Thus, for suﬃciently large n ∈ N and
x ∈ [(1 − δ)−1̺
ny0, ∞), we obtain

P2,n(x, δ)
P(ε > x) ⩽ 1
x P(ε > x)
 ∑

i⩾n E(ζ (i)
1,0) ∫ (1−δ)̺−ix

0 P(ε > t) dt

⩽ 2(1 − δ)
1 − α
 ∑

i⩾n
 P(ε > (1 − δ)̺
−ix)
P(ε > x) ,

10

since E(ζ (i)
1,0) ⩽ ̺
i, i ∈ Z+, by (B.5) and ζ (0)
1,0 = 1. Using (2.5), we get

P2,n(x, δ)
P(ε > x) ⩽ 2(1 − δ)
1 − α
 ∑

i⩾n (1 + δ)[(1 − δ)̺
−i]
− α
2

for δ ∈ (0, α
2 ), for suﬃciently large n ∈ N and for all x ∈ [max(x0, (1 − δ)−1̺
ny0), ∞). Hence
for δ ∈ (0, α
2 ) we have

lim
n→∞ lim sup
x→∞ P2,n(x, δ)
P(ε > x) ⩽ lim
n→∞ 2(1 − δ2)
1 − α
 ∑

i⩾n [(1 − δ)̺
−i]
− α
2 = 0,

where the last step follows by the fact that the series ∑∞
i=0(̺
i) α
2 is convergent, since ̺ ∈ (0, 1).

Consequently, due to the fact that P(∑∞
i=n V (i)
i (εi) > x) ⩽ P1,n(x, δ) + P2,n(x, δ), x ∈ R++,
n ∈ N, δ ∈ (0, 1), we obtain (2.4), and we conclude limn→∞ L2,n(q) = 0 for all q ∈ (0, 1).
Thus we obtain

lim sup
x→∞ π((x, ∞))
P(ε > x) ⩽ lim
n→∞ L1,n(q) + lim
n→∞ L2,n(q) = (1 − q)−α ∞∑

i=0 m
α
i

for all q ∈ (0, 1). Letting q ↓ 0, this yields

lim sup
x→∞ π((x, ∞))
P(ε > x) ⩽
 ∞∑

i=0 m
α
i .

Taking into account (2.3), the proof of (2.4) is complete in case of α ∈ (0, 1).

Next, we consider the case α ∈ [1, 2). Note that (2.4) is equivalent to

lim
n→∞ lim sup
x→∞
 P(∑∞
i=n V (i)
i (εi) > √x
)

P(ε > √x) = lim
n→∞ lim sup
x→∞
 P((∑∞
i=n V (i)
i (εi))2 > x
)

P(ε2 > x) = 0.

Repeating a similar argument as for α ∈ (0, 1), we obtain

P
(( ∞∑

i=n V (i)
i (εi)
)2 > x

)

= P
(( ∞∑

i=n V (i)
i (εi)
)2 > x, sup
i⩾n ̺
2iε2
i > (1 − δ)x

)

+ P
(( ∞∑

i=n V (i)
i (εi)
)2 > x, sup
i⩾n ̺
2iε2
i ⩽ (1 − δ)x

)

= P
(( ∞∑

i=n V (i)
i (εi)
)2 > x, sup
i⩾n ̺
2iε2
i > (1 − δ)x

)

+ P
(( ∞∑

i=n V (i)
i (εi)1{ε2
i ⩽(1−δ)̺−2i x}
)2 > x, sup
i⩾n ̺
2iε2
i ⩽ (1 − δ)x

)

11

⩽ P(sup
i⩾n ̺
2iε2
i > (1 − δ)x
) + P
(( ∞∑

i=n V (i)
i (εi)1{ε2
i ⩽(1−δ)̺−2ix}
)2 > x

)

=: P1,n(x, δ) + P2,n(x, δ)

for each x ∈ R++, n ∈ N and δ ∈ (0, 1). By the subadditivity of probability,

P1,n(x, δ) ⩽
 ∞∑

i=n P(̺
2iε2
i > (1 − δ)x) =
 ∞∑

i=n P(ε2 > (1 − δ)̺
−2ix)

for each x ∈ R++, n ∈ N and δ ∈ (0, 1). Since ε2 is regularly varying with index α
2
(see Lemma E.3), using Potter’s upper bound (see Lemma E.12) for δ ∈ (0, α
4 ), there exists
x0 ∈ R++ such that

(2.6) P(ε2 > (1 − δ)̺
−2ix)
P(ε2 > x) < (1 + δ)[(1 − δ)̺
−2i]
− α
2 +δ < (1 + δ)[(1 − δ)̺
−2i]− α
4

if x ∈ [x0, ∞) and (1 − δ)̺
−2i ∈ [1, ∞), which holds for suﬃciently large i ∈ N (due to
̺ ∈ (0, 1)). Consequently, if δ ∈ (0, α
4 ), then

lim
n→∞ lim sup
x→∞ P1,n(x, δ)
P(ε2 > x) ⩽ lim
n→∞
 ∞∑

i=n (1 + δ)[(1 − δ)̺
−2i]
− α
4 = 0,

since ̺ α
2 < 1 (due to ̺ ∈ (0, 1)). By Markov’s inequality, for x ∈ R++, n ∈ N and
δ ∈ (0, 1), we have

P2,n(x, δ)
P(ε2 > x) ⩽ 1
x P(ε2 > x) E
(( ∞∑

i=n V (i)
i (εi)1{ε2
i ⩽(1−δ)̺−2ix}
)2)

= 1
x P(ε2 > x) E
( ∞∑

i=n V (i)
i (εi)21{ε2
i ⩽(1−δ)̺−2ix}
)

+ 1
x P(ε2 > x) E

( ∞∑

i,j=n, i̸=j V (i)
i (εi)V (j)
j (εj)1{ε2
i ⩽(1−δ)̺−2ix}1{ε2
j ⩽(1−δ)̺−2j x}
)

=: J2,1,n(x, δ) + J2,2,n(x, δ)

for each x ∈ R++, n ∈ N and δ ∈ (0, 1). By Lemma C.2, (B.4) and (B.5) with X0 = 1 and
X−1 = 0, we have

E(V (i)
i (n)2) = E
 


( n∑

j=1 ζ (i)
j,0
)2

 =
 n∑

j=1 E (
(ζ (i)
j,0)2) +
 n∑

j,ℓ=1, j̸=ℓ E (
ζ (i)
j,0) E (ζ (i)
ℓ,0)

⩽ csub
 n∑

j=1 ̺
i +
 n∑

j,ℓ=1, j̸=ℓ ̺
i̺
i ⩽ csubn̺
i + (n
2 − n)̺
2i ⩽ csub̺
in + ̺
2in
2

12

for i, n ∈ N. Hence, using that (εi, V (i)
i (εi)) D
= (εi, ∑εi
j=1 ζ (i)
j,0) and that εi and {ζ (i)
j,0 : j ∈ N}
are independent, we have

J2,1,n(x, δ) =
 ∞∑

i=n
 E(V (i)
i (εi)21{ε2
i ⩽(1−δ)̺−2ix})

x P(ε2 > x)

=
 ∞∑

i=n
 E((∑εi
j=1 ζ (i)
j,0)21{εi⩽(1−δ) 1
2 ̺−ix 1
2 })

x P(ε2 > x)

=
 ∞∑

i=n
 ∑
0⩽ℓ⩽(1−δ) 1
2 ̺−ix 1
2 E
((∑ℓ
j=1 ζ (i)
j,0)2) P(εi = ℓ)

x P(ε2 > x)

⩽
 ∞∑

i=n
 ∑

0⩽ℓ⩽(1−δ) 1
2 ̺−ix 1
2 (csub̺
iℓ + ̺
2iℓ2) P(ε = ℓ)

x P(ε2 > x)

=
 ∞∑

i=n csub̺
i E(ε1{ε2⩽(1−δ)̺−2ix})
x P(ε2 > x) +
 ∞∑

i=n ̺
2i E(ε21{ε2⩽(1−δ)̺−2ix})
x P(ε2 > x)

=: J2,1,1,n(x, δ) + J2,1,2,n(x, δ).

Since ε2 is regularly varying with index α
2 ∈ [ 1
2, 1) (see Lemma E.3), by Karamata’s theorem
(see, Theorem E.11), we have
 lim
y→∞
 ∫ y
0 P(ε2 > t) dt
y P(ε2 > y) = 1
1 − α
2 ,

thus there exists y0 ∈ R++ such that
∫ y

0 P(ε2 > t) dt ⩽ 2y P(ε2 > y)
1 − α
2 , y ∈ [y0, ∞),

hence

E(ε21{ε2⩽(1−δ)̺−2ix}) = ∫ ∞

0 P(ε21{ε2⩽(1−δ)̺−2i x} > y) dy

= ∫ (1−δ)̺−2i x

0 P(y < ε2 ⩽ (1 − δ)̺
−2ix) dy

⩽ ∫ (1−δ)̺−2i x

0 P(ε2 > t) dt ⩽ 2(1 − δ)̺
−2ix P(ε2 > (1 − δ)̺
−2ix)
1 − α
2

whenever (1 − δ)̺
−2ix ∈ [y0, ∞), which holds for i ⩾ n with suﬃciently large n ∈ N, and
x ∈ [(1 − δ)−1̺
2ny0, ∞) due to ̺ ∈ (0, 1). Thus for δ ∈ (0, α
4 ), for suﬃciently large n ∈ N
(satisfying (1 − δ)̺
−2n ∈ (1, ∞) as well) and for all x ∈ [max(x0, (1 − δ)−1̺
2ny0), ∞), using

13

(2.6), we obtain

J2,1,2,n(x, δ) ⩽ 2(1 − δ)
1 − α
2
 ∞∑

i=n
 P(ε2 > (1 − δ)̺
−2ix)
P(ε2 > x) ⩽ 2(1 − δ)
1 − α
2
 ∞∑

i=n (1 + δ)[(1 − δ)̺
−2i]
− α
4

= 2(1 − δ2)
1 − α
2
 ∞∑

i=n [(1 − δ)̺
−2i]
− α
4 .

Hence for δ ∈ (0, α
4 ), we have

lim
n→∞ lim sup
x→∞ J2,1,2,n(x, δ) ⩽ 2(1 − δ2)
1 − α
2 lim
n→∞
 ∞∑

i=n [(1 − δ)̺
−2i]− α
4 = 0,

yielding limn→∞ lim supx→∞ J2,1,2,n(x, δ) = 0 for δ ∈ (0, α
4 ). Further, if α ∈ (1, 2), or α = 1
and mε < ∞, we have
 J2,1,1,n(x, δ) ⩽ csub
 ∞∑

i=n ̺
i mε
x P(ε2 > x) ,

and hence, using that limx→∞ x P(ε2 > x) = ∞ (see Lemma E.4),

lim
n→∞ lim sup
x→∞ J2,1,1,n(x, δ) ⩽ csubmε lim
n→∞

( ∞∑

i=n ̺
i)
 lim sup
x→∞ 1
x P(ε2 > x) = 0,

yielding limn→∞ lim supx→∞ J2,1,1,n(x, δ) = 0 for δ ∈ (0, 1).

If α = 1 and mε = ∞, then we have

J2,1,1,n(x, δ) =
 ∞∑

i=n csub̺
i E (ε1{ε⩽(1−δ) 1
2 ̺−ix 1
2 })

x P(ε2 > x)

for x ∈ R++, n ∈ N and δ ∈ (0, 1). Note that

E(ε1{ε⩽y}) ⩽ ∫ ∞

0 P(ε1{ε⩽y} > t) dt = ∫ y

0 P(t < ε ⩽ y) dt ⩽ ∫ y

0 P(t < ε) dt =: ̃L(y)

for y ∈ R+. Because of α = 1, Proposition 1.5.9a in Bingham et al. [4] yields that ̃L is a
slowly varying function (at inﬁnity). By Potter’s bounds (see Lemma E.12), for every δ ∈ R++,
there exists z0 ∈ R++ such that
 ̃L(y)
̃L(z) < (1 + δ) (y
z
 )δ

for z ⩾ z0 and y ⩾ z. Hence, for x ⩾ z2
0, we have

E(
ε1{ε⩽(1−δ) 1
2 ̺−ix 1
2 }) ⩽ ̃L
((1 − δ) 1
2 ̺
−ix 1
2 ) ⩽ ̃L(̺
−ix 1
2 ) ⩽ (1 + δ)̺
−iδ ̃L(x 1
2 ), i ⩾ n,

14

where we also used that ̃L is monotone increasing. Using this, we conclude that for every
δ ∈ R++, there exists z0 ∈ R++ such that for x ⩾ z2
0, we have

J2,1,1,n(x, δ) ⩽ (1 + δ)csub ̃L(x 1
2 )
x P(ε2 > x)
 ∞∑

i=n ̺
−iδ.

Here, since ̺ ∈ (0, 1) and δ ∈ R++, we have limn→∞ ∑∞
i=n ̺
−iδ = 0, and

̃L(√x)
x P(ε2 > x) = ̃L(√x)
x1/4 · 1
x3/4 P(ε > √x) → 0 as x → ∞,

by Lemma E.4, due to the fact that ̃L is slowly varying and the function R++ ∋ x ↦→ P(ε >
√x) is regularly varying with index −1/2. Hence limn→∞ lim supx→∞ J2,1,1,n(x, δ) = 0 for
δ ∈ (0, 1) in case of α = 1 and mε = ∞.

Consequently, we have limn→∞ lim supx→∞ J2,1,n(x, δ) = 0 for δ ∈ (0, α
4 ).

Now we turn to prove limn→∞ lim supx→∞ J2,2,n(x, δ) = 0 for δ ∈ (0, 1). Using that
{(εi, V (i)
i (εi) : i ∈ N} are independent, we have

J2,2,n(x, δ) ⩽ 1
x P(ε2 > x)
 ∞∑

i,j=n, i̸=j E(V (i)
i (εi)1{ε2
i ⩽(1−δ)̺−2ix}) E(V (j)
j (εj)1{ε2
j ⩽(1−δ)̺−2j x}).

Here, using that (εi, V (i)
i (εi)) D
= (εi, ∑εi
j=1 ζ (i)
j,0), where εi and {ζ (i)
j,0 : j ∈ N} are independent,
and (B.5) with X0 = 1 and X−1 = 0, we have

E(V (i)
i (εi)1{ε2
i ⩽(1−δ)̺−2i x}) = E
 (( εi∑

j=1 ζ (i)
j,0
)1{ε2
i ⩽(1−δ)̺−2ix}
)

=
 ⌊(1−δ) 1
2 ̺−ix 1
2 ⌋∑

ℓ=0 E
 ( ℓ∑

j=1 ζ (i)
j,0
)
 P(εi = ℓ)

≤
 ⌊(1−δ) 1
2 ̺−ix 1
2 ⌋∑

ℓ=0 ℓ̺
i P(εi = ℓ) = ̺
i E(εi1{ε2
i ⩽(1−δ)̺−2ix})

for x ∈ R++ and δ ∈ (0, 1). If α ∈ (1, 2), or α = 1 and mε < ∞, then

J2,2,n(x, δ) ⩽ 1
x P(ε2 > x)
 ∞∑

i,j=n, i̸=j ̺
i+j E(εi1{ε2
i ⩽(1−δ)̺−2ix}) E(εj1{ε2
j ⩽(1−δ)̺−2j x})

⩽ m
2
ε
x P(ε2 > x)
 ∞∑

i,j=n, i̸=j ̺
i+j ⩽ m
2
ε
x P(ε2 > x)
 ( ∞∑

i=n ̺
i)2

15

for x ∈ R++ and δ ∈ (0, 1), and then, by Lemma E.4,

lim
n→∞ lim sup
x→∞ J2,2,n(x, δ) ⩽ m
2
ε lim
n→∞
 ( ∞∑

i=n ̺
i)2 lim sup
x→∞ 1
x P(ε2 > x)

= m
2
ε
 ( lim
n→∞ ̺
2n

(1 − ̺)2
 ) · 0 = 0,

yielding that limn→∞ lim supx→∞ J2,2,n(x, δ) = 0.

If α = 1 and mε = ∞, then we can apply the same argument as for J2,1,1,n(x, δ). Namely,

J2,2,n(x, δ) ⩽ (1 + δ)2

x P(ε2 > x)
 ∞∑

i,j=n, i̸=j ̺
(1−δ)(i+j)(̃L(x 1
2 ))2

⩽ (1 + δ)2 (̃L(x 1
2 ))2

x P(ε2 > x)
 ∞∑

i,j=n, i̸=j ̺
(1−δ)(i+j) = (1 + δ)2 (̃L(x 1
2 ))2

x P(ε2 > x)
 ( ∞∑

i=n ̺
(1−δ)i)2

for x ∈ R++ and δ ∈ (0, 1), where

(̃L(x 1
2 ))2

x P(ε2 > x) =
 ( ̃L(x 1
2 )

x 1
2
 )2 1

x 3
4 P(ε > √x) → 0 as x → ∞,

yielding that limn→∞ lim supx→∞ J2,2,n(x, δ) = 0 for δ ∈ (0, 1) in case of α = 1 and mε = ∞
as well.

Consequently, limn→∞ lim supx→∞ P2,n(x,δ)
P(ε2>x) = 0 for δ ∈ (0, α
4 ) yielding (2.4) in case of
α ∈ [1, 2) as well, and we conclude limn→∞ L2,n(q) = 0 for all q ∈ (0, 1). The proof can be
ﬁnished as in case of α ∈ (0, 1). ✷

2.4 Remark. The statement of Theorem 2.1 remains true in the case when mξ ∈ (0, 1) and
mη = 0. In this case we get the statement for classical Galton–Watson processes, see Theorem
2.1.1 in Basrak et al. [3] or Theorem 1.1. However, note that this is not a special case of
Theorem 2.1, since in this case the mean matrix M ξ,η is not primitive. ✷

Appendices

A Representations of second-order Galton–Watson pro-
cesses without or with immigration

First, we recall a representation of a second-order Galton–Watson process without or with
immigration as a (special) 2-type Galton–Watson process without or with immigration, respec-
tively. Let (Xn)n⩾−1 be a second-order Galton–Watson process with immigration given in

16

(1.2), and let us introduce the random vectors

Y n :=
 [
Yn,1
Yn,2
]
 :=
 [ Xn
Xn−1
]
 , n ∈ Z+.(A.1)

Then we have
 Y n =
 Yn−1,1∑

i=1
 [
ξn,i
1
 ]
 +
 Yn−1,2∑

j=1
 [
ηn,j
0
 ]
 +
 [
εn
0
 ]
 , n ∈ N,(A.2)

hence (Y n)n∈Z+ is a (special) 2-type Galton–Watson process with immigration and with initial
vector
 Y 0 =
 [ X0
X−1
]
 .

In fact, the type 1 and 2 individuals are identiﬁed with individuals of age 0 and 1, respectively,
and for each n, i, j ∈ N, at time n, the i
th individual of type 1 of the (n − 1)th generation
produces ξn,i individuals of type 1 and exactly one individual of type 2, and the jth individual
of type 2 of the (n − 1)th generation produces ηn,j individuals of type 1 and no individual of
type 2.

The representation (A.2) works backwards as well, namely, let (Y k)k∈Z+ be a special 2-type
Galton–Watson process with immigration given by

Y k =
 Yk−1,1∑

j=1
 [
ξk,j,1,1
1
 ]
 +
 Yk−1,2∑

j=1
 [
ξk,j,2,1
0
 ]
 +
 [
εk,1
0
 ]
 , k ∈ N,(A.3)

where Y 0 is a 2-dimensional integer-valued random vector. Here, for each k, j ∈ N and
i ∈ {1, 2}, ξk,j,i,1 denotes the number of type 1 oﬀsprings in the kth generation produced by
the jth oﬀspring of the (k − 1)th generation of type i, and εk denotes the number of type
1 immigrants in the kth generation. For the second coordinate process of (Y k)k∈Z+, we get
Yk,2 = Yk−1,1, k ∈ N, and substituting this into (A.3), the ﬁrst coordinate process of (Y k)k∈Z+
satisﬁes
 Yk,1 =
 Yk−1,1∑

j=1 ξk,j,1,1 +
 Yk−2,1∑

j=1 ξk,j,2,1 + εk,1, k ⩾ 2.

Thus, the ﬁrst coordinate process of (Y k)k∈Z+ given by (A.3) satisﬁes equation (1.2) with
Xn := Yn,1, ξn,i := ξn,i,1,1, ηn,j := ξn,j,2,1, εn := εn,1, n, i, j ∈ N, and with initial values
X0 := Y0,1 and X−1 := Y0,2, i.e., it is a second-order Galton–Watson process with immigration.
Moreover, the second coordinate process of (Y k)k∈Z+ also satisﬁes equation (1.2) with Xn :=
Yn+1,2, ξn,i := ξn,i,1,1, ηn,j := ξn,j,2,1, εn := εn,1, n, i, j ∈ N, and with initial values X0 := Y0,1
and X−1 := Y0,2, i.e., it is also a second-order Galton–Watson process with immigration.

Note that, for a second-order Galton–Watson process (Xn)n⩾−1 (without immigration), the
additive (or branching) property of a 2-type Galton–Watson process (without immigration) (see,

17

e.g. in Athreya and Ney [1, Chapter V, Section 1]), together with the law of total probability,
for each n ∈ N, imply

(A.4) Xn D
=
 X0∑

i=1 ζ (n)
i,0 +
 X−1∑

j=1 ζ (n)
j,−1,

where {
(X0, X−1), ζ (n)
i,0 , ζ (n)
j,−1 : i, j ∈ N} are independent random variables such that {ζ (n)
i,0 : i ∈
N} are independent copies of Vn,0 and {ζ (n)
j,−1 : j ∈ N} are independent copies of Vn,−1, where
(Vk,0)k⩾−1 and (Vk,−1)k⩾−1 are second-order Galton–Watson processes (without immigration)
with initial values V0,0 = 1, V−1,0 = 0, V0,−1 = 0 and V−1,−1 = 1, and with the same
oﬀspring distributions as (Xk)k⩾−1.

Moreover, if (Xn)n⩾−1 is a second-order Galton–Watson process with immigration, then
for each n ∈ N, we have

(A.5) Xn = V (n)
0 (X0, X−1) +
 n∑

i=1 V (n−i)
i (εi, 0),

where {
V (n)
0 (X0, X−1), V (n−i)
i (εi, 0) : i ∈ {1, . . . , n}} are independent random variables such
that V (n)
0 (X0, X−1) represents the number of newborns at time n, resulting from the initial
individuals X0 at time 0 and X−1 at time −1, and for each i ∈ {1, . . . , n}, V (n−i)
i (εi, 0)
represents the number of newborns at time n, resulting from the immigration εi at time i.
Indeed, considering the (special) 2-type Galton–Watson process (Y k)k∈Z+ with immigration
given in (A.1) and applying formula (1.1) in Kaplan [14], we obtain

(A.6) Y n = V (n)
0 (Y 0) +
 n∑

i=1 V (n−i)
i (εi) with εi :=
 [
εi
0
 ]
 , i ∈ N,

for each n ∈ N, where {
V (n)
0 (Y 0), V (n−i)
i (εi) : i ∈ {1, . . . , n}} are independent random
vectors such that V (n)
0 (Y 0) represents the number of individuals alive at time n, resulting
from the initial individuals Y 0 at time 0, and for each i ∈ {1, . . . , n}, V (n−i)
i (εi) represents
the number of individuals alive at time n, resulting from the immigration εi at time i.
Clearly, (V (k)
0 (Y 0))k∈Z+ and (V (k)
i (εi))k∈Z+, i ∈ {1, . . . , n}, are (special) 2-type Galton–
Watson processes (without immigration) of the form (A.3) with initial vectors V (0)
0 (Y 0) = Y 0
and V (0)
i (εi) = εi, i ∈ {1, . . . , n}, respectively, and with the same oﬀspring distributions
as (Y k)k∈Z+. Using the considerations for the backward representation presented before,
the ﬁrst coordinates in (A.6) gives (A.5), where (V (k)
0 (X0, X−1))k⩾−1 and (V (k)
i (εi, 0))k⩾−1,
i ∈ {1, . . . , n}, are second-order Galton–Watson processes (without immigration) with initial
values V (0)
0 (X0, X−1) = X0, V (−1)
0 (X0, X−1) = X−1, V (0)
i (εi, 0) = εi and V (−1)
i (εi, 0) = 0,
i ∈ {1, . . . , n}, and with the same oﬀspring distributions as (Xk)k⩾−1.

18

B On the expectation of second-order Galton–Watson
processes with immigration

Our aim is to derive an explicit formula for the expectation of a second-order Galton–Watson
process with immigration at time n and to describe its asymptotic behavior as n → ∞.

Recall that ξ, η and ε are random variables such that ξ D
= ξ1,1, η D
= η1,1 and ε D
= ε1,
and we put mξ = E(ξ) ∈ [0, ∞], mη = E(η) ∈ [0, ∞] and mε = E(ε) ∈ [0, ∞]. If mξ ∈ R+,
mη ∈ R+, mε ∈ R+, E(X0) ∈ R+ and E(X−1) ∈ R+, then (1.2) implies

E(Xn | F X
n−1) = Xn−1mξ + Xn−2mη + mε, n ∈ N,

where F X
n := σ(X−1, X0, . . . , Xn), n ∈ Z+. Consequently,

E(Xn) = mξ E(Xn−1) + mη E(Xn−2) + mε, n ∈ N,

which can be written in the matrix form

(B.1)
 [ E(Xn)

E(Xn−1)
]
 = M ξ,η
 [
E(Xn−1)

E(Xn−2)
]
 +
 [mε
0
 ]
 , n ∈ N,

with

(B.2) M ξ,η :=
 [mξ mη
1 0
 ]
 .

Note that M ξ,η is the mean matrix of the 2-type Galton–Watson process (Y n)n∈Z+ given in
(A.1). Thus, we conclude

(B.3)
 [ E(Xn)

E(Xn−1)
]
 = M n
ξ,η
 [ E(X0)

E(X−1)

]
 +
 n∑

k=1 M n−k
ξ,η
 [
mε
0
 ]
 , n ∈ N.

Hence, the asymptotic behavior of the sequence (E(Xn))n∈N depends on the asymptotic
behavior of the powers (M n
ξ,η)n∈N, which is related to the spectral radius ̺ of M ξ,η, see
Lemma B.1 and (B.6). If (Xn)n⩾−1 is a second-order Galton–Watson process with immigration
such that mξ ∈ R+ and mη ∈ R+, then (Xn)n⩾−1 is called subcritical, critical or supercritical
if ̺ < 1, ̺ = 1 or ̺ > 1, respectively. It is easy to check that a second-order Galton–Watson
process with immigration is subcritical, critical or supercritical if and only if mξ + mη < 1,
mξ + mη = 1 or mξ + mη > 1, respectively. We call the attention that for the classiﬁcation
of second-order Galton–Watson process with immigration we do not suppose the ﬁniteness of
the expectation of X0, X−1 or ε.

B.1 Lemma. Let (Xn)n⩾−1 be a second-order Galton–Watson process with immigration such
that mξ ∈ R+, mη ∈ R+, mε ∈ R+, E(X0) ∈ R+ and E(X−1) ∈ R+.

If mξ = 0 and mη = 0, then, for all n ∈ N, we have E(Xn) = mε.

19

If mξ + mη > 0, then, for all n ∈ N, we have

(B.4) E(Xn) = λn+1
+ − λn+1
−
λ+ − λ− E(X0) + λn
+ − λn
−
λ+ − λ− mη E(X−1) + Cn(λ+, λ−)
λ+ − λ− mε

with
 Cn(λ+, λ−) :=
 




λ+ 1−λn
+
1−λ+ − λ− 1−λn
−
1−λ− if λ+ ̸= 1,

n − λ− 1−λn
−
1−λ− if λ+ = 1,

where λ+ and λ− are given in (2.1), and hence

E(Xn) =
 



 mε
(1−λ+)(1−λ−) + O(λn
+) if λ+ ∈ (0, 1),

mε
1−λ− n + O(1) if λ+ = 1,

1
λ+−λ− (
λ+ E(X0) + mη E(X−1) + λ+
λ+−1mε)λn
+ + O(1 + |λ−|n) if λ+ ∈ (1, ∞)

as n → ∞. Moreover, λ+ is the spectral radius ̺ of M ξ,η.

Further, in case of mε = 0, we have the following more precise statements:

If mξ = 0, mη > 0 and mε = 0, then, for all k ∈ N, we have E(X2k−1) = E(X−1)λ2k
+
and E(X2k) = E(X0)λ2k
+ .

If mξ > 0, mη = 0 and mε = 0, then, for all n ∈ N, we have E(Xn) = E(X0)λn
+.

If mξ > 0, mη > 0 and mε = 0, then

E(Xn) = λ+ E(X0) + mη E(X−1)
λ+ − λ− λn
+ + O(|λ−|n) as n → ∞.

If mε = 0, i.e., there is no immigration, then

(B.5) E(Xn) ⩽ ̺
n E(X0) + ̺
n−1mη E(X−1), n ∈ N.

Proof. We are going to use (B.3). The matrix M ξ,η has eigenvalues

λ+ = mξ + √m
2
ξ + 4mη

2 , λ− = mξ − √
m
2
ξ + 4mη

2 ,

satisfying λ+ ∈ R+ and λ− ∈ [−λ+, 0], hence the spectral radius of M ξ,η is

(B.6) ̺ = λ+ = mξ + √m
2
ξ + 4mη

2 .

In what follows, we suppose that mξ+mη > 0, which yields that λ+ ∈ R++ and λ− ∈ (−λ+, 0].
One can easily check that the powers of M ξ,η can be written in the form

(B.7) M n
ξ,η = λn
+
λ+ − λ−
 [λ+ mη
1 −λ−
]
 + λn
−
λ+ − λ−
 [−λ− −mη
−1 λ+
 ]
 , n ∈ Z+.

20

Consequently,
 ̺
−nM n
ξ,η → 1
λ+ − λ−
 [
λ+ mη
1 −λ−
]
 as n → ∞.

Moreover, (B.3) and (B.7) yield
[ E(Xn)

E(Xn−1)
]
 = E(X0)
λ+ − λ−
 [
λn+1
+ − λn+1
−
λn
+ − λn
−
 ]
 + E(X−1)
λ+ − λ−
 [ mη(λn
+ − λn
−)

−λ−λn
+ + λ+λn
−
]

+ mε
λ+ − λ−
 n∑

k=1
 [
λn−k+1
+ − λn−k+1
−
λn−k
+ − λn−k
−
 ]
 , n ∈ Z+,

and hence, we obtain (B.4) and (B.5). Indeed, by (B.7) and by λ+ ∈ R++ and −λ+ < λ− ⩽ 0,
for each k ∈ Z+, we have

λ2k+1
+ − λ2k+1
−
λ+ − λ− =
 2k∑

i=0 λi
−λ2k−i
+ = λ2k
+ +
 k∑

j=1(λ2j−1
− λ2k−2j+1
+ + λ2j
− λ2k−2j
+ ) ⩽ λ2k
+ ,

since λ2j−1
− λ2k−2j+1
+ + λ2j
− λ2k−2j
+ = λ2j−1
− λ2k−2j
+ (λ+ + λ−) ⩽ 0, and, in a similar way,

λ2k+2
+ − λ2k+2
−
λ+ − λ− =
 2k+1∑

i=0 λi
−λ2k+1−i
+ = λ2k+1
+ +
 k∑

j=1(λ2j−1
− λ2k−2j+1
+ + λ2j
− λ2k−2j
+ ) + λ2k+1
− ⩽ λ2k+1
+ .

Further, if λ+ ∈ (0, 1), then

mε
λ+ − λ− Cn(λ+, λ−) = mε
λ+ − λ−
 λ+ − λ− + λn+1
+ (λ− − 1) + λn+1
− (1 − λ+)
(1 − λ+)(1 − λ−)

= mε
(1 − λ+)(1 − λ−) + O(λn
+)

as n → ∞. The other statements easily follow from (B.4). ✷

C Moment estimations

The ﬁrst moment of a second-order Galton–Watson process (Xn)n⩾−1 (without immigra-
tion) can be estimated by (B.5). Next, we present an auxiliary lemma on higher moments of
(Xn)n⩾−1.

C.1 Lemma. Let (Xn)n⩾−1 be a second-order Galton–Watson process (without immigration)
such that E(X r
−1) < ∞, E(X r
0 ) < ∞, E(ξr) < ∞ and E(ηr) < ∞ with some r > 1. Then
E(X r
n) < ∞ for all n ∈ N.
 21

Proof. By power means inequality, we have

E(X r
n | F X
n−1) = E
 ((Xn−1∑

i=1 ξn,i +
 Xn−2∑

j=1 ηn,j
)r ∣
∣
∣
∣
∣ F X
n−1
)

⩽ 2r−1 E
 ((Xn−1∑

i=1 ξn,i
)r
 +
 (Xn−2∑

j=1 ηn,j
)r ∣
∣
∣
∣
∣ F X
n−1
)

⩽ 2r−1 E
 (
X r−1
n−1
 Xn−1∑

i=1 ξr
n,i + X r−1
n−2
 Xn−2∑

j=1 ηr
n,j
 ∣
∣
∣
∣
∣ F X
n−1
)

= 2r−1 (X r
n−1 E(ξr) + X r
n−2 E(ηr)) < ∞

for all n ∈ N. Hence E(X r
n) ⩽ 2r−1( E(X r
n−1) E(ξr) + E(X r
n−2) E(ηr)), n ∈ N. By induction
we obtain the statement. ✷

Moreover, we present an auxiliary lemma on an estimation of the second moment of a second-
order Galton–Watson process (without immigration). This lemma is valid for the subcritical,
critical and supercritical cases as well, however, in the proofs we only use it for the subcritical
case.

C.2 Lemma. Let (Xn)n⩾−1 be a second-order Galton–Watson process (without immigration)
such that X0 = 1, X−1 = 0, E(ξ2) < ∞ and E(η2) < ∞. Then for all n ∈ N,

E(X 2
n) ⩽
 



csub ̺
n, if ̺ ∈ (0, 1),

ccrit n, if ̺ = 1,

csup ̺
2n, if ̺ ∈ (1, ∞),

(C.1)

where

csub := 1+ Var(ξ)
̺(1 − ̺) + Var(η)
̺2(1 − ̺) , ccrit := 1+Var(ξ)+Var(η), csup := 1+ Var(ξ)
̺(̺ − 1) + Var(η)
̺3(̺ − 1) .

Proof. By formula (A2) in Lemma A.1 in Isp´any and Pap [13], we have

Var(Y n) =
 n−1∑

j=0 M j
ξ,η[
(e
⊤
1 M n−j−1
ξ,η e1)V ξ + (e⊤
2 M n−j−1
ξ,η e1)V η]
(M ⊤
ξ,η)j,

where (Y n)n∈Z+ is given by (A.1) with Y 0 = [1 0]⊤, and

V ξ := Var
 ([ξ

1
])
 = Var(ξ)e1e
⊤
1 , V η := Var
 ([
η

0
])
 = Var(η)e1e
⊤
1 ,

where ξ and η are random variables such that ξ D
= ξ1,1 and η D
= η1,1. Here we note
that formula (A2) in Lemma A.1 in Isp´any and Pap [13] is stated only for critical processes,

22

but it also holds in the subcritical and supercritical cases as well; the proof is the very same.
Consequently,

Var(Xn) = Var(e
⊤
1 Y n) = e
⊤
1 Var(Y n)e1

= e⊤
1
 n−1∑

j=0 M j
ξ,η[
(e⊤
1 M n−j−1
ξ,η e1) Var(ξ)e1e
⊤
1 + (e
⊤
2 M n−j−1
ξ,η e1) Var(η)e1e
⊤
1 ](M ⊤
ξ,η)je1

=
 n−1∑

j=0(e
⊤
1 M j
ξ,ηe1)2[
Var(ξ)(e
⊤
1 M n−j−1
ξ,η e1) + Var(η)(e
⊤
2 M n−j−1
ξ,η e1)],

where we used that e
⊤
1 (M ⊤
ξ,η)je1 = e
⊤
1 M j
ξ,ηe1. Using (B.3) with X0 = 1 and X−1 = 0, we
have e
⊤
1 M j
ξ,ηe1 = E(Xj) and e
⊤
2 M j
ξ,ηe1 = E(Xj−1) for each j ∈ Z+, hence

Var(Xn) = Var(ξ)
 n−1∑

j=0 [E(Xj)]2 E(Xn−j−1) + Var(η)
 n−2∑

j=0[E(Xj)]2 E(Xn−j−2),

where we used that X−1 = 0. We note that the above formula for Var(Xn) can also be found
in Kashikar and Deshmukh [16, page 562]. Using (B.5) with X0 = 1 and X−1 = 0, we obtain

E(X 2
n) = Var(Xn) + [E(Xn)]2 ⩽ Var(ξ)
 n−1∑

j=0 ̺
n+j−1 + Var(η)
 n−2∑

j=0 ̺
n+j−2 + ̺
2n

=
 {n Var(ξ) + (n − 1) Var(η) + 1, if ̺ = 1,

Var(ξ) ̺n−1−̺2n−1

1−̺ + Var(η) ̺n−2−̺2n−3

1−̺ + ̺
2n, if ̺ ̸= 1,

yielding (C.1). Indeed, for example, if ̺ ∈ (1, ∞), then

̺
n−2 − ̺
2n−3

1 − ̺ = ̺
2n−3(1 − ̺
−n+1)
̺ − 1 ⩽ ̺
2n−3

̺ − 1 = ̺
2n

̺3(̺ − 1) , n ∈ N.
 ✷

D Representation of the unique stationary distribution
for 2-type Galton–Watson processes with immigra-
tion

First, we introduce 2-type Galton–Watson processes with immigration. For each k, j ∈ Z+
and i, ℓ ∈ {1, 2}, the number of individuals of type i born or arrived as immigrants in the
kth generation will be denoted by Xk,i, the number of type ℓ oﬀsprings produced by the jth

individual who is of type i belonging to the (k − 1)th generation will be denoted by ξk,j,i,ℓ,

23

and the number of type i immigrants in the kth generation will be denoted by εk,i. Then
we have

(D.1)
 [
Xk,1
Xk,2
]
 =
 Xk−1,1∑

j=1
 [
ξk,j,1,1
ξk,j,1,2
]
 +
 Xk−1,2∑

j=1
 [
ξk,j,2,1
ξk,j,2,2
]
 +
 [
εk,1
εk,2
]
 , k ∈ N.

Here {
X 0, ξk,j,i, εk : k, j ∈ N, i ∈ {1, 2}} are supposed to be independent, and {ξk,j,1 : k, j ∈
N}, {ξk,j,2 : k, j ∈ N} and {εk : k ∈ N} are supposed to consist of identically distributed
random vectors, where

X 0 :=
 [
X0,1
X0,2
]
 , X k :=
 [
Xk,1
Xk,2
]
 , ξk,j,i :=
 [
ξk,j,i,1
ξk,j,i,2
]
 , εk :=
 [
εk,1
εk,2
]
 .

For notational convenience, let ξ1, ξ2 and ε be random vectors such that ξ1 D
= ξ1,1,1,

ξ2 D
= ξ1,1,2 and ε D
= ε1, and put mξ1 := E(ξ1) ∈ [0, ∞]2, mξ2 := E(ξ2) ∈ [0, ∞]2, and
mε := E(ε) ∈ [0, ∞]2, and put

M ξ := [
mξ1 mξ2] ∈ [0, ∞]
2×2.

We call M ξ the oﬀspring mean matrix, and note that many authors deﬁne the oﬀspring mean
matrix as M ⊤
ξ . If mξ1 ∈ R2
+, mξ2 ∈ R2
+, and mε ∈ R2
+, then for each n ∈ Z+, (D.1)
implies
 E(X n | F X
n−1) = Xn−1,1 mξ1 + Xn−1,2 mξ2 + mε = M ξ X n−1 + mε, n ∈ N,

where F X
n := σ(X 0, . . . , X n), n ∈ Z+. Consequently, E(X n) = M ξ E(X n−1) + mε, n ∈ N,
which implies
 E(X n) = M n
ξ E(X 0) +
 n∑

k=1 M n−k
ξ mε, n ∈ N.

Hence, the asymptotic behavior of the sequence (E(X n))n∈Z+ depends on the asymptotic
behavior of the powers (M n
ξ )n∈N of the oﬀspring mean matrix, which is related to the spectral
radius r(M ξ) ∈ R+ of M ξ (see the Frobenius–Perron theorem, e.g., Horn and Johnson [11,
Theorems 8.2.8 and 8.5.1]). A 2-type Galton–Watson process (X n)n∈Z+ with immigration is
referred to respectively as subcritical, critical or supercritical if r(M ξ) < 1, r(M ξ) = 1 or
r(M ξ) > 1 (see, e.g., Athreya and Ney [1, V.3] or Quine [22]). We extend this classiﬁcation
for all 2-type Galton–Watson processes with immigration.

If mξ1 ∈ R2
+, mξ2 ∈ R2
+, r(M ξ) < 1, M ξ is primitive, i.e., there exists m ∈ N such that
M m
ξ ∈ R2×2
++ , P(ε = 0) < 1 and E(1{ε̸=0} log((e1 + e2)⊤ε)) < ∞, then, by the Theorem in
Quine [22], there exists a unique stationary distribution π for (X n)n∈Z+. As a consequence
of formula (16) for the probability generating function of π in Quine [22], we have

n∑

i=0 V (i)
i (εi) D
−→ π as n → ∞,

24

where (V (i)
k (εi))k∈Z+, i ∈ Z+, are independent copies of a 2-type Galton–Watson process
(V k(ε))k∈Z+ (without immigration) with initial vector V 0(ε) = ε and with the same oﬀspring
distributions as (X k)k∈Z+. Consequently, we have

∞∑

i=0 V (i)
i (εi) D
= π,

where the series ∑∞
i=0 V (i)
i (εi) converges with probability 1, see, e.g., Heyer [10, Theorem
3.1.6]. The above representation of the stationary distribution π for (X n)n∈Z+ can be
interpreted in a way that we consider independent 2-type Galton–Watson processes without
immigration such that the i
th one admits initial vector εi, i ∈ Z+, evaluate the i
th 2-type
Galton-Watson processes at time point i, and then sum up all these random variables.

E Regularly varying distributions

First, we recall the notions of slowly varying and regularly varying functions, respectively.

E.1 Deﬁnition. A measurable function U : R++ → R++ is called regularly varying at inﬁnity
with index ρ ∈ R if for all q ∈ R++,
 lim
x→∞ U(qx)
U(x) = qρ.

In case of ρ = 0, U is called slowly varying at inﬁnity.

Next, we recall the notion of regularly varying random variables.

E.2 Deﬁnition. A non-negative random variable X is called regularly varying with index
α ∈ R+ if U(x) := P(X > x) ∈ R++ for all x ∈ R++, and U is regularly varying at inﬁnity
with index −α.

E.3 Lemma. If ζ is a non-negative regularly varying random variable with index α ∈ R+,
then for each c ∈ R++, ζ c is regularly varying with index α
c .

Proof. For any q ∈ R++, we have

lim
x→∞ P(ζ c > qx)
P(ζ c > x) = lim
x→∞ P(ζ > q1/cx
1/c)
P(ζ > x1/c) = q−α/c,

as desired. ✷

E.4 Lemma. If L : R++ → R++ is a slowly varying function (at inﬁnity), then

lim
x→∞ x
δL(x) = ∞, lim
x→∞ x
−δL(x) = 0, δ ∈ R++.

25

For Lemma E.4, see, Bingham et al. [4, Proposition 1.3.6. (v)].

E.5 Lemma. If ε is a non-negative regularly varying random variable with index α ∈ R++,
then E(1{ε̸=0} log(ε)) < ∞ and E(log(ε + 1)) < ∞.

Proof. Since E(1{ε̸=0} log(ε)) ⩽ E(log(ε + 1)), it is enough to prove that E(log(ε + 1)) < ∞.
Since log(ε + 1) ⩾ 0, we have

E(log(ε + 1)) = ∫ ∞

0 P(log(ε + 1) ⩾ x) dx = ∫ ∞

0 P(ε ⩾ e
x − 1) dx

= ∫ 1

0 P(ε ⩾ e
x − 1) dx + ∫ ∞

1 P(ε ⩾ e
x − 1) dx := I1 + I2.

Here I1 ⩽ 1, and, by substitution y = e
x − 1,

I2 = ∫ ∞

e−1 y−αL(y) 1
1 + y dy,

where L(y) := yα P(ε > y), y ∈ R++, is a slowly varying function. By Lemma E.4, there
exists y0 ∈ (e − 1, ∞) such that y− α
2 L(y) ⩽ 1 for all y ∈ [y0, ∞). Hence

I2 = ∫ y0

e−1 y−αL(y) 1
1 + y dy + ∫ ∞

y0 y−αL(y) 1
1 + y dy

⩽ ∫ y0

e−1 y−αL(y) 1
1 + y dy + ∫ ∞

y0 y− α
2 1
1 + y dy

⩽ ∫ y0

e−1 y−αL(y) 1
1 + y dy + ∫ ∞

y0 y− α
2 −1 dy

⩽ ∫ y0

e−1
 1
1 + y dy + ∫ ∞

y0 y− α
2 −1 dy < ∞,

since y−αL(y) = P(ε > y) ⩽ 1 for all y ∈ R++. ✷

E.6 Lemma. If η is a non-negative regularly varying random variable with index α ∈ (1, 2),
then for every ̺ ∈ (α, ∞), there exist y0 ∈ R++ and B ∈ R++ such that

P(η > z)
P(η > y) ⩽ B ( z
y
 )−̺ , y ⩾ z ⩾ y0,

or equivalently, P(η > θy)
P(η > y) ⩽ Bθ−̺, θ ∈ (0, 1], y ⩾ y0
θ .

For Lemma E.6, see Proposition 2.2.1 in Bingham et al. [4].

For the next lemma, see Fa¨y et al. [9, Lemma 4.4]. Here we present a proof as well, since
we state their result in a little bit extended form.

26

E.7 Lemma. Let h : R+ → R++ be a function such that limx→∞ h(x) = 0. Then there
exists a monotone increasing, left-continuous, slowly varying (at inﬁnity) function L such that
L(x) ⩾ 1, x ∈ R+, limx→∞ L(x) = ∞ and limx→∞ L(x)h(x) = 0. One can also choose a
version of L which is right-continuous with all the other properties remaining true.

Proof. We can construct L as follows. Let L(x) := 1 for x ∈ [0, x0], where x0 :=
sup{y ∈ R+ : h(y) > 1}, and we deﬁne sup ∅ := 0. Since limx→∞ h(x) = 0, we have
x0 ∈ R+. Let L(x) := 2 for x ∈ (x0, x1], where x1 := max{2x0, sup{y ∈ R+ : h(y) > 2−2}}.
Let L(x) := 3 for x ∈ (x1, x2], where x2 := max{3x1, sup{y ∈ R+ : h(y) > 3−2}}, and
continue this construction in the straightforward way: L(x) := k + 1 for x ∈ (xk−1, xk], where
xk := max{(k + 1)xk−1, sup{y ∈ R+ : h(y) > (k + 1)−2}}, k ∈ N. Since h takes positive
values and limx→∞ h(x) = 0, we have limx→∞ L(x) = ∞, and, since for all k ∈ Z+ and
x > xk,
 L(x)h(x) =
 ∞∑

i=k L(x)h(x)1(xi,xi+1](x) ⩽
 ∞∑

i=k (i + 2) 1
(i + 1)21(xi,xi+1](x) ⩽ k + 2
(k + 1)2 ,

we have limx→∞ L(x)h(x) = 0. It remains to check that L is slowly varying (at inﬁnity).
For this it is enough to verify that for any q ∈ R++ and suﬃciently large x ∈ R++, we have
x and qx are either in the same interval of type (xk−1, xk] or in two neighbouring intervals
of this type, since in this case for suﬃciently large x ∈ R++:

L(qx)
L(x) ∈ {
1, kx
kx + 1, kx + 1
kx
 }

with some kx ∈ N, and for suﬃciently large x ∈ R++ and for y ⩾ x,
∣
∣
∣
∣ L(qy)
L(y) − 1∣
∣
∣
∣ ∈ {0, ∣
∣
∣
∣ky + 1
ky − 1∣
∣
∣
∣ , ∣
∣
∣
∣ ky
ky + 1 − 1∣
∣
∣
∣

} = {
0, 1
ky , 1
ky + 1
 } ,

where ky ⩾ kx and limy→∞ ky = ∞, yielding that limx→∞ L(qx)
L(x) = 1. To ﬁnish the proof, if
x ∈ (xk−1, xk] with some k ∈ N, then in case of q ⩾ 1, we have qx ∈ (xk−1, xk] ∪ (xk, xk+1]
provided that k + 2 ⩾ q, and in case of q ∈ (0, 1), we have qx ∈ (xk−2, xk−1] ∪ (xk−1, xk]
provided that k > 1
q . Indeed, xk ⩾ (k + 1)xk−1, k ∈ N, and if k + 2 ⩾ q, then
qx ⩽ qxk ⩽ (k + 2)xk ⩽ xk+1, as desired, and if k > 1
q , then qx > qxk−1 > 1
k xk−1 ⩾ xk−2, as
desired. ✷

E.8 Lemma. If X and Y are non-negative random variables such that X is regularly
varying with index α ∈ R+ and there exists r ∈ (α, ∞) with E(Y r) < ∞, then P(Y >
x) = o(P(X > x)) as x → ∞.

For a proof of Lemma E.8, see, e.g., Barczy et al. [2, Lemma C.6].

E.9 Lemma. If X1 and X2 are non-negative regularly varying random variables with index
α1 ∈ R+ and α2 ∈ R+, respectively, such that α1 < α2, then P(X2 > x) = o(P(X1 > x))
as x → ∞.
 27

For a proof of Lemma E.9, see, e.g., Barczy et al. [2, Lemma C.7].

E.10 Lemma. (Convolution property) If X1 and X2 are non-negative random variables
such that X1 is regularly varying with index α1 ∈ R+ and P(X2 > x) = o(P(X1 > x)) as
x → ∞, then P(X1 + X2 > x) ∼ P(X1 > x) as x → ∞, and hence X1 + X2 is regularly
varying with index α1.

If X1 and X2 are independent non-negative regularly varying random variables with index
α1 ∈ R+ and α2 ∈ R+, respectively, then

P(X1 + X2 > x) ∼
 




P(X1 > x) if α1 < α2,

P(X1 > x) + P(X2 > x) if α1 = α2,

P(X2 > x) if α1 > α2,

as x → ∞, and hence X1 + X2 is regularly varying with index min{α1, α2}.

The statements of Lemma E.10 follow, e.g., from parts 1 and 3 of Lemma B.6.1 of Buraczewski
et al. [6] and Lemma E.9 together with the fact that the sum of two slowly varying functions
is slowly varying.

E.11 Theorem. (Karamata’s theorem) Let U : R++ → R++ be a locally integrable func-
tion such that it is integrable on intervals including 0 as well.

(i) If U is regularly varying (at inﬁnity) with index −α ∈ [−1, ∞), then R++ ∋ x ↦→
∫ x
0 U(t) dt is regularly varying (at inﬁnity) with index 1 − α, and

lim
x→∞ xU(x)
∫ x
0 U(t) dt = 1 − α.

(ii) If U is regularly varying (at inﬁnity) with index −α ∈ (−∞, −1), then R++ ∋ x ↦→
∫ ∞
x U(t) dt is regularly varying (at inﬁnity) with index 1 − α, and

lim
x→∞ xU(x)
∫ ∞
x U(t) dt = −1 + α.

For Theorem E.11, see, e.g., Resnick [23, Theorem 2.1].

E.12 Lemma. (Potter’s bounds) If U : R++ → R++ is a regularly varying function (at
inﬁnity) with index −α ∈ R, then for every δ ∈ R++, there exists x0 ∈ R+ such that

(1 − δ)q−α−δ < U(qx)
U(x) < (1 + δ)q−α+δ, x ∈ [x0, ∞), q ∈ [1, ∞).

For Lemma E.12, see, e.g., Resnick [23, Proposition 2.6].

Finally, we recall a result on the tail behaviour of regularly varying random sums.

28

E.13 Proposition. Let τ be a non-negative integer-valued random variable and let {ζ, ζi :
i ∈ N} be independent and identically distributed non-negative random variables, independent
of τ , such that τ is regularly varying with index β ∈ R+ and E(ζ) ∈ R++. In case of
β ∈ [1, ∞), assume additionally that there exists r ∈ (β, ∞) with E(ζ r) < ∞. Then we have

P( τ∑

i=1 ζi > x
) ∼ P(τ > x
E(ζ)
) ∼ (E(ζ))β P(τ > x) as x → ∞,

and hence ∑τ
i=1 ζi is also regularly varying with index β.

For a proof of Proposition E.13, see, e.g., Barczy et al. [2, Proposition F.3].

F Large deviations

We recall a result about large deviations for sums of non-negative independent and identically
distributed regularly varying random variables, see, Tang and Yan [26, part (ii) of Theorem 1].
We use it in the second proof of Theorem G.1 in case of α ∈ (1, 2). Here we present a complete
proof as well, since the one in Tang and Yan [26, part (ii) of Theorem 1] contains a gap.

F.1 Theorem. (Large deviations) If (ηj)j∈N are independent, identically distributed non-
negative regularly varying random variables with index α ∈ (1, 2), then for each γ ∈
(E(η1), ∞), there exists a constant C ∈ R++ such that

P(η1 + · · · + ηn > y) ⩽ Cn P(η1 > y)

for all n ∈ N and y ∈ [γn, ∞).

Proof. We will follow the proof of part (ii) of Theorem 1 in Tang and Yan [26]. Let q ∈ (0, 1)
and
 ̃ηj := ηj1{ηj ⩽qy}, j ∈ N, ̃Sj :=
 j∑

i=1 ̃ηi, j ∈ N.

Then for all n ∈ N,

P(η1 + · · · + ηn > y)

= P(η1 + · · · + ηn > y, max
1⩽j⩽n ηj > qy) + P(η1 + · · · + ηn > y, max
1⩽j⩽n ηj ⩽ qy)

⩽ P( max
1⩽j⩽n ηj > qy) + P(̃η1 + · · · + ̃ηn > y, max
1⩽j⩽n ηj ⩽ qy)

⩽ P( max
1⩽j⩽n ηj > qy) + P( ̃Sn > y)

⩽
 n∑

j=1 P(ηj > qy) + P( ̃Sn > y)

= n P(η1 > qy) + P( ̃Sn > y), y ∈ R+.

(F.1)
 29

Here
 P(η1 > qy) = P(η1 > qy)
P(η1 > y) · P(η1 > y), y ∈ R++,

and since limy→∞ P(η1>qy)
P(η1>y) = q−α, there exists an y∗ ∈ R++ such that P(η1>qy)
P(η1>y) ⩽ 2q−α

for all y ⩾ y∗. Now we check that P(η1>qy)
P(η1>y) is bounded on the interval [0, y∗]. Since

limy→0 P(η1>qy)
P(η1>y) = 1, there exists an y1 ∈ R++ such that y1 < y∗ and P(η1>qy)
P(η1>y) ⩽ 2 on the

interval [0, y1]. On the interval [y1, y∗] the quantity P(η1>qy)
P(η1>y) can be bounded from above by

P(η1>qy1)
P(η1>y∗) . Hence the function R+ ∋ y ↦→ P(η1>qy)
P(η1>y) is bounded, and consequently, there exists a
constant C1(q) ∈ R++ (depending possibly on the distribution of η1 as well) such that

n P(η1 > qy) ⩽ C1(q)n P(η1 > y), y ∈ R++, n ∈ N.(F.2)

Let a(n, y) := max{− log(n P(η1 > y), 1}, n ∈ N, y ∈ R++. Then a(n, y) tends to ∞
uniformly for y ⩾ γn as n → ∞, i.e., limn→∞ inf y⩾γn a(n, y) = ∞, since, by Lemma E.4,

n P(η1 > y) ⩽ n P(η1 > γn) = n(γn)−αLη1(γn) = γ−αn
1−αLη1(n) Lη1(γn)
Lη1(n) → γ−α · 0 · 1 = 0

(F.3)

as n → ∞, where Lη1(y) := yα P(η1 > y), y ∈ R++, is a slowly varying (at inﬁnity) function.
For any y ∈ R++, h ∈ R++ and n ∈ N, we have

P( ̃Sn > y)
n P(η1 > y) ⩽ e
−hy E(e
h ̃Sn)
n P(η1 > y) = e
−hy(E(e
h̃η1))n

n P(η1 > y)

= e
−hy (∫ qy
0 e
ht Fη1(dt))n

n P(η1 > y) = e
−hy (∫ qy
0 (e
ht − 1) Fη1(dt) + 1)n

n P(η1 > y)

⩽ e
−hy exp {n ∫ qy
0 (e
ht − 1) Fη1(dt)}

e−a(n,y) ,

where the last step follows from (1 + y)n ⩽ e
ny, y ∈ R+, n ∈ N, and from a(n, y) ⩾
− log(n P(η1 > y)), yielding e
−a(n,y) ⩽ n P(η1 > y). Using that a(n, y) ⩾ 1, n ∈ N,
y ∈ R++, let us consider the decomposition

∫ qy

0 (e
ht − 1) Fη1(dt) = ∫ qy
a(n,y)

0 (e
ht − 1) Fη1(dt) + ∫ qy

qy
a(n,y) (e
ht − 1) Fη1(dt) =: I1 + I2.

Using the inequality e
y − 1 ⩽ ye
y, y ∈ R+, we have

I1 = ∫ qy
a(n,y)

0 (e
ht − 1) Fη1(dt) ⩽ ∫ qy
a(n,y)

0 hte
ht Fη1(dt)

⩽ e
 hqy
a(n,y) ∫ qy
a(n,y)

0 ht Fη1(dt) ⩽ he
 hqy
a(n,y) E(η1).

30

Now we turn to treat I2. Applying Lemma E.6, for all ̺ > α, there exist y0 ∈ R++ and
B ∈ R++ (possibly depending on ̺ and on the distribution of η1) such that

P (
η1 > qy
a(n,y) )

P (η1 > y) ⩽ B ( q
a(n, y)
)−̺ whenever y ⩾ qy
a(n, y) ⩾ y0.

The aim of the following discussion is to show that for each n ∈ N, there exists ̃y0(n) ∈ R++
such that y ⩾ qy
a(n,y) ⩾ y0 holds for all y ⩾ ̃y0(n). For each n ∈ N, the ﬁrst inequality holds
for suﬃciently large y, since limy→∞ a(n, y) = ∞. Moreover, for each n ∈ N, the second
inequality holds for suﬃciently large y, since limy→∞ a(n,y)
y = 0. Indeed, for each n ∈ N we
have a(n, y) = − log(n P(η1 > y)) for suﬃciently large y, and hence

a(n, y)
y = − log(n P(η1 > y))
y = − log(ny−αLη1(y))
y = − log(n) + α log(y) − log(Lη1(y))
y .

By Lemma E.4, for any δ ∈ R++, we have y−δ ⩽ Lη1(y) ⩽ yδ for suﬃciently large y. Taking
logarithm, dividing by y, and using that limy→∞ log(y)
y = 0, one concludes limy→∞ a(n,y)
y = 0.

Set
 h := h(n, y, K) := a(n, y) − K̺ log(a(n, y))
Kqy ,

where ̺ > α and K > 1 will be chosen later. We show that there exists N1 ∈ N such that
h > 0 and a(n, y) > 1 for all y ⩾ γn and n ⩾ N1. Since limx→∞ log(x)
x = 0, there exists
M > 0 such that log(x)
x < 1
K̺ for all x ⩾ M. Since limn→∞ inf y⩾γn a(n, y) = ∞, there exists

n0(M) ∈ N such that a(n, y) ⩾ M for all y ⩾ γn with n ⩾ n0(M). Hence log(a(n,y))
a(n,y) < 1
K̺
for all y ⩾ γn with n ⩾ n0(M), as desired. Hence for all ̺ > α and y ⩾ max{̃y0(n), γn}
with n ⩾ N1, we have

I2 = ∫ qy

qy
a(n,y) (e
ht − 1) Fη1(dt) ⩽ e
hqy P (
η1 > qy
a(n, y)
)

⩽ exp { a(n, y) − K̺ log(a(n, y))
K
 } B ( q
a(n, y)
)−̺ P(η1 > y)

= Bq−̺e
 a(n,y)
K P(η1 > y) = Bq−̺(n P(η1 > y))− 1
K P(η1 > y),

where we used that 1 < a(n, y) = − log(n P(η1 > y)). Putting together the bounds for I1
and I2 and using that hqy
a(n,y) ⩽ 1
K for y ⩾ γn with n ⩾ N1, we obtain that

(F.4) P( ̃Sn > y)
n P(η1 > y) ⩽ exp {nh E(η1)e 1
K + Bq−̺(n P(η1 > y))1− 1
K − hy + a(n, y)}

for y ⩾ max{̃y0(n), γn} with n ⩾ N1. Noting that n P(η1 > y) → 0 uniformly for y ⩾ γn
as n → ∞ (see, (F.3)), we obtain that there exists C2 ∈ R++ such that the right-hand side

31

of (F.4) can be bounded by

C2 exp {
nh E(η1)e 1
K − hy + a(n, y)}

= C2 exp
 {

hy
(e 1
K n E(η1)
y − 1
)
 + a(n, y)
}

⩽ C2 exp
 {a(n, y) − K̺ log(a(n, y))
Kq
 ( e 1
K E(η1)
γ − 1
)
 + a(n, y)
}

for all ̺ > α, suﬃciently large n ∈ N (greater than N1) and y ⩾ max{̃y0(n), γn}. Since
γ > E(η1), we can choose K > 1 suﬃciently large such that 1
γ e 1
K E(η1) < 1, then we choose
q > 0 suﬃciently small such that
1
Kq
 ( e 1
K E(η1)
γ − 1) + 2 < 0,

i.e., q < 1
2K (1 − 1
γ e 1
K E(η1)). Then we have

P( ̃Sn > y)
n P(η1 > y) ⩽ C2 exp {(a(n, y) − K̺ log(a(n, y)))(−2) + a(n, y)}

= C2 exp {2K̺ log(a(n, y)) − a(n, y)}

for all ̺ > α, suﬃciently large n ∈ N (greater than N1) and y ⩾ max{̃y0(n), γn},
where we used that a(n, y) − K̺ log(a(n, y)) > 0 for y ⩾ γn with n ⩾ N1. Here
C2 exp {2K̺ log(a(n, y)) − a(n, y)} tends to 0 uniformly for y ⩾ γn as n → ∞, i.e.,

sup
y⩾γn exp {2K̺ log(a(n, y)) − a(n, y)} = exp { sup
y⩾γn(2K̺ log(a(n, y)) − a(n, y))} → 0

as n → ∞. Indeed, this will be a consequence of supy⩾γn(2K̺ log(a(n, y)) − a(n, y)) → −∞
as n → ∞. We have

(F.5) sup
y⩾γn(2K̺ log(a(n, y)) − a(n, y)) ⩽ S1(n) + S2(n),

where
 S1(n) := sup
y⩾γn
(
2K̺ log(a(n, y)) − 1
2 a(n, y))
,

S2(n) := sup
y⩾γn
(
−1
2 a(n, y)) = −1
2 inf
y⩾γn a(n, y) → −∞ as n → ∞.

Moreover, limx→∞ log(x)
x = 0 implies that there exists ̃M > 0 such that log(x)
x < 1
4K̺ for all

x ⩾ ̃M . Since limn→∞ inf y⩾γn a(n, y) = ∞, there exists n0( ̃M ) ∈ N such that a(n, y) ⩾ ̃M
for all y ⩾ γn with n ⩾ n0( ̃M ). Hence log(a(n,y))
a(n,y) < 1
4K̺ for all y ⩾ γn with n ⩾ n0( ̃M ),

32

thus 2K̺ log(a(n, y)) < 1
2 a(n, y). Consequently, we obtain S1(n) ⩽ 0 for all n ⩾ n0( ̃M ),
and hence, by (F.5), we conclude supy⩾γn(2K̺ log(a(n, y)) − a(n, y)) → −∞ as n → ∞, as
desired. So we have
 lim
n→∞ sup
y⩾γn P( ̃Sn > y)
n P(η1 > y) = 0.

Consequently, there exists an N ∈ N such that

sup
n⩾N, y⩾γn P( ̃Sn > y)
n P(η1 > y) < ∞.

This, together with (F.1) and (F.2) yield that

sup
n⩾N, y⩾γn P(Sn > y)
n P(η1 > y) < ∞.(F.6)

Finally, using the convolution property (see, Lemma E.10),

sup
1⩽n⩽N, y⩾γn P(Sn > y)
n P(η1 > y) ⩽
 N∑

n=1 sup
y⩾γn P(Sn > y)
n P(η1 > y) < ∞.(F.7)

The desired statement readily follows from (F.6) and (F.7). ✷

G Tail behavior of second-order Galton–Watson pro-
cesses (without immigration) having regularly vary-
ing initial distributions

G.1 Proposition. Let (Xn)n⩾−1 be a second-order Galton–Watson process (without immi-
gration) such that X0 and X−1 are independent, X0 is regularly varying with index
β0 ∈ R+, X−1 is regularly varying with index β−1 ∈ R+ and mξ, mη ∈ R++. In case of
max{β0, β−1} ∈ [1, ∞), assume additionally that there exists r ∈ (max{β0, β−1}, ∞) with
E(ξr) < ∞ and E(ηr) < ∞. Then for each n ∈ N,

P(Xn > x) ∼
 




m
β0
n P(X0 > x) if 0 ⩽ β0 < β−1,

m
β0
n P(X0 > x) + m
β−1
n−1m
β−1
η P(X−1 > x) if β0 = β−1,

m
β−1
n−1m
β−1
η P(X−1 > x) if β−1 < β0

as x → ∞, where mi, i ∈ Z+, are given in Theorem 2.1 and hence, Xn is regularly varying
with index min{β0, β−1} for each n ∈ N.

First proof of Proposition G.1. Let us ﬁx n ∈ N. In view of the additive property
(A.4), the independence of X0 and X−1, and the convolution property of regularly varying
distributions described in Lemma E.10, it is suﬃcient to prove

(G.1) P
( X0∑

i=1 ζ (n)
i,0 > x

)
 ∼ m
β0
n P(X0 > x), P
(X−1∑

j=1 ζ (n)
j,−1 > x

)
 ∼ m
β−1
n−1m
β−1
η P(X−1 > x)

33

as x → ∞. These relations follow from Proposition E.13, since E(ζ (n)
1,0 ) = mn ∈ R++ and
E(ζ (n)
1,−1) = mn−1mη ∈ R++, n ∈ N, by (B.4). ✷

Second proof of Proposition G.1. Let us ﬁx n ∈ N. In view of the additive property
(A.4), the independence of X0 and X−1, and the convolution property of regularly varying
distributions described in Lemma E.10, it is suﬃcient to prove (G.1). We show only the ﬁrst
relation in (G.1), since the second one can be proven in the same way. Note that E(ζ (n)
1,0 ) = mn
by (B.4). First, we prove
 lim inf
x→∞ P(∑X0
i=1 ζ (n)
i,0 > x
)

P(X0 > x) ⩾ m
β0
n .(G.2)

Let q ∈ (0, 1) be arbitrary. For suﬃciently large x ∈ R++, we have ⌊(1 + q)x/mn⌋ ⩾ 1,
since mn > 0. Using that for each i ∈ N, ζ (n)
i,0 is non-negative, we obtain

P
( X0∑

i=1 ζ (n)
i,0 > x

)
 ⩾
 ∞∑

k=⌊(1+q)x/mn⌋ P
 ( k∑

i=1 ζ (n)
i,0 > x

)
 P(X0 = k)

⩾ P
(⌊(1+q)x/mn⌋∑

i=1 ζ (n)
i,0 > x

) ∞∑

k=⌊(1+q)x/mn⌋ P(X0 = k)

= P
( 1
⌊(1 + q)x/mn⌋
 ⌊(1+q)x/mn⌋∑

i=1 ζ (n)
i,0 > x
⌊(1 + q)x/mn⌋
)
 P(X0 ⩾ ⌊(1 + q)x/mn⌋)

⩾ P
( 1
⌊(1 + q)x/mn⌋
 ⌊(1+q)x/mn ⌋∑

i=1 ζ (n)
i,0 > x
⌊(1 + q)x/mn⌋
)
 P(X0 > (1 + q)x/mn)

for suﬃciently large x ∈ R++. For suﬃciently large x ∈ R++, we have x
⌊(1+q)x/mn⌋ ⩽ mn
1+(q/2) ,
since x
⌊(1+q)x/mn⌋ → mn
1+q as x → ∞ and mn
1+q < mn
1+(q/2) . Hence, for suﬃciently large x ∈ R++,
we have

P
( X0∑

i=1 ζ (n)
i,0 > x

)
 ⩾ P
( 1
⌊(1 + q)x/mn⌋
 ⌊(1+q)x/mn ⌋∑

i=1 ζ (n)
i,0 > mn
1 + (q/2)
)
 P (
X0 > (1 + q)x
mn
 ) .

We have

(G.3) 1
N
 N∑

i=1 ζ (n)
i,0 a.s.
−→ E(ζ (n)
1,0 ) =mn as N → ∞

by the strong law of large numbers, hence mn
1+(q/2) < mn yields

P
( 1
⌊(1 + q)x/mn⌋
 ⌊(1+q)x/mn ⌋∑

i=1 ζ (n)
i,0 > mn
1 + (q/2)
)
 → 1 as x → ∞.

34

Thus, using that X0 is regularly varying with index β0, we have

P
( 1
⌊(1 + q)x/mn⌋
 ⌊(1+q)x/mn⌋∑

i=1 ζ (n)
i,0 > mn
1 + (q/2)
 )
 P(
X0 > (1 + q)x
mn
 ) ∼ P (
X0 > (1 + q)x
mn
 )

∼ ( mn
1 + q
 )β0 P(X0 > x)

as x → ∞. Consequently,

lim inf
x→∞ P(∑X0
i=1 ζ (n)
i,0 > x
)

P(X0 > x) ⩾ ( mn
1 + q
 )β0, q ∈ (0, 1),

and, by q ↓ 0, we conclude (G.2).

Next, we prove
 lim sup
x→∞
 P(∑X0
i=1 ζ (n)
i,0 > x
)

P(X0 > x) ⩽ m
β0
n .(G.4)

Let q ∈ (0, 1) be arbitrary. For suﬃciently large x ∈ R++, we have ⌊(1 − q)x/mn⌋ ⩾ 1, and
hence

P
( X0∑

i=1 ζ (n)
i,0 > x

)
 ⩽ P(X0 > ⌊(1 − q)x/mn⌋) +
 ⌊(1−q)x/mn⌋∑

k=1 P
 ( k∑

i=1 ζ (n)
i,0 > x

)
 P(X0 = k)

= P(
X0 > (1 − q)x
mn
 ) +
 ⌊(1−q)x/mn⌋∑

k=1 P
 ( k∑

i=1 ζ (n)
i,0 > x

)
 P(X0 = k).

Since X0 is regularly varying with index β0, we have

P
(X0 > (1 − q)x
mn
 ) ∼ ( mn
1 − q
 )β0 P(X0 > x) as x → ∞,

hence, by taking the limit q ↓ 0, we get (G.4) provided we check

(G.5) p(x, q) :=
 ⌊(1−q)x/mn⌋∑

k=1 P
 ( k∑

i=1 ζ (n)
i,0 > x

)
 P(X0 = k) = o (P (X0 > x)) as x → ∞

for all suﬃciently small q ∈ (0, 1). (In fact, it will turn out that (G.5) holds for any q ∈ (0, 1).)

First, we consider the case β0 ∈ (0, 1). Let 0 < δ < (1 − q)/mn. Then for suﬃciently
large x ∈ R++, we have ⌊δx⌋ < ⌊(1 − q)x/mn⌋, and then

p(x, q) =
 ⌊δx⌋∑

k=1 P
 ( k∑

i=1 ζ (n)
i,0 > x

)
 P(X0 = k) +
 ⌊(1−q)x/mn⌋∑

k=⌊δx⌋+1 P
 ( k∑

i=1 ζ (n)
i,0 > x

)
 P(X0 = k)

=: p1(x, δ) + p2(x, δ, q).
 35

At ﬁrst, we show that p2(x, δ, q) = o(P(X0 > x)) as x → ∞ for all 0 < δ < (1 − q)/mn.
Here, using that ζ (n)
i,0 is non-negative for each i ∈ N, we obtain

p2(x, δ, q) ⩽ P
(
⌊(1−q)x/mn ⌋∑

i=1 ζ (n)
i,0 > x

) ⌊(1−q)x/mn⌋∑

k=⌊δx⌋+1 P(X0 = k)

⩽ P
(
⌊(1−q)x/mn ⌋∑

i=1 ζ (n)
i,0 > x

)
 P(X0 > ⌊δx⌋) = P
(⌊(1−q)x/mn⌋∑

i=1 ζ (n)
i,0 > x

)
 P(X0 > δx).

For suﬃciently large x ∈ R++, we have x
⌊(1−q)x/mn⌋ ⩾ mn
1−(q/2) , since x
⌊(1−q)x/mn⌋ → mn
1−q as
x → ∞ and mn
1−q > mn
1−(q/2) . Hence, for suﬃciently large x ∈ R++, we have

P
(⌊(1−q)x/mn⌋∑

i=1 ζ (n)
i,0 > x

)
 = P

( 1
⌊(1 − q)x/mn⌋
 ⌊(1−q)x/mn⌋∑

i=1 ζ (n)
i,0 > x
⌊(1 − q)x/mn⌋
)

⩽ P
( 1
⌊(1 − q)x/mn⌋
 ⌊(1−q)x/mn⌋∑

i=1 ζ (n)
i,0 > mn
1 − (q/2)
)
.

Again by the strong law of large numbers (see (G.3)), mn
1−(q/2) > mn yields

P
( 1
⌊(1 − q)x/mn⌋
 ⌊(1−q)x/mn ⌋∑

i=1 ζ (n)
i,0 > mn
1 − (q/2)
 )
 → 0 as x → ∞,

hence we obtain

(G.6) P
(⌊(1−q)x/mn⌋∑

i=1 ζ (n)
i,0 > x

)
 → 0 as x → ∞.

Using that X0 is regularly varying with index β0, we have P(X0 > δx) ∼ δ−β0 P(X0 > x)
as x → ∞, hence p2(x, δ, q) = o(P(X0 > x)) as x → ∞ for all 0 < δ < (1 − q)/mn and
q ∈ (0, 1). Now we turn to prove

lim sup
δ↓0 lim sup
x→∞ p1(x, δ)
P(X0 > x) = 0.

By Markov’s inequality,
 P
 ( k∑

i=1 ζ (n)
i,0 > x

)
 ⩽ 1
x
 k∑

i=1 E(ζ (n)
i,0 ) = mnk
x

for all k ∈ N and x ∈ R++, and hence

p1(x, δ) ⩽ mn
x
 ⌊δx⌋∑

k=0 k P(X0 = k) = mn
x E(X01{X0⩽⌊δx⌋}) = mn
x
 ∫ ∞

0 P(X01{X0⩽⌊δx⌋} > t) dt

= mn
x
 ∫ ⌊δx⌋

0 P(X01{X0⩽⌊δx⌋} > t) dt ⩽ mn
x
 ∫ ⌊δx⌋

0 P(X0 > t) dt.

36

Since R+ ∋ x ↦→ P(X0 > x) is locally integrable (due to the fact that it is bounded), it is
integrable on intervals including 0 as well, and since it is regularly varying (at inﬁnity) with
index −β0, by Karamata’s theorem (see Theorem E.11),

lim
x→∞ x P(X0 > x)
∫ x
0 P(X0 > t) dt = 1 − β0,

and hence ∫ ⌊δx⌋

0 P(X0 > t) dt ∼ 1
1 − β0 ⌊δx⌋ P(X0 > ⌊δx⌋) = 1
1 − β0 ⌊δx⌋ P(X0 > δx)

as x → ∞. Then using that P(X0 > δx) ∼ δ−β0 P(X0 > x) as x → ∞, we have

p1(x, δ)
P(X0 > x) ⩽ mn
x
 ∫ ⌊δx⌋
0 P(X0 > t) dt
P(X0 > x) ∼ mn
1 − β0 δ P(X0 > δx)
P(X0 > x) ∼ mn
1 − β0 δ1−β0

as x → ∞. Consequently,

lim sup
x→∞ p1(x, δ)
P(X0 > x) ⩽ mn
1 − β0 δ1−β0 for all 0 < δ < 1 − q
mn ,

and hence lim supδ↓0 lim supx→∞ p1(x,δ)
P(X0>x) ⩽ limδ↓0 mn
1−β0 δ1−β0 = 0. Combining the parts we get
p(x, q) = o(P(X0 > x)) as x → ∞ for any q ∈ (0, 1), as desired.

Next, we consider the case β0 ∈ (1, 2). Using Lemma E.7, we check that there exists a
non-negative random variable ̃ζ (n) having the following properties:

• ̃ζ (n) is regularly varying with index β0,

• P(ζ (n)
1,0 > x) ⩽ P(̃ζ (n) > x), x ∈ R+,

• P(̃ζ (n) > x) = o(P(X0 > x)) as x → ∞,

• E(ζ (n)
1,0 ) ⩽ E(̃ζ (n)) < ∞.

By Lemma C.1, E((ζ (n)
1,0 )r) < ∞, and hence, by Lemma E.8, P(ζ (n)
1,0 > x) = o(P(X0 > x)) as
x → ∞. Thus, by Lemma E.7, there exists a monotone increasing, right-continuous, slowly
varying (at inﬁnity) function L̃ζ (n) such that L̃ζ (n)(x) ⩾ 1, x ∈ R+, limx→∞ L̃ζ (n)(x) = ∞

and limx→∞ L̃ζ (n)(x) P(ζ (n)
1,0 >x)
P(X0>x) = 0. Hence, using also that P(X0 ⩾ x) ⩽ 1, x ∈ R+, there

exists x
′ ∈ R+ such that L̃ζ (n)(x) P(ζ (n)
1,0 >x)
P(X0>x) ⩽ 1 and P(X0>x)
L̃ζ(n) (x) ⩽ 1 hold for all x ⩾ x
′. Let

̃ζ (n) be a random variable such that

P(̃ζ (n) > x) :=
 



1 if x ⩽ x
′,

P(X0>x)
L̃ζ(n) (x) if x > x
′.

37

Such a non-negative random variable exists, since R++ ∋ x ↦→ P(X0>x)
L̃ζ(n) (x) is monotone decreasing,

converges to 0 as x → ∞ and right-continuous. For all q ∈ R++,

lim
x→∞ P(̃ζ (n) > qx)

P(̃ζ (n) > x) = lim
x→∞ L̃ζ (n)(x)

L̃ζ (n)(qx) P(X0 > qx)
P(X0 > x) = 1 · q−β0 = q−β0,

yielding that ̃ζ (n) is regularly varying with index β0. For x ⩽ x
′, we have P(ζ (n)
1,0 > x) ⩽
1 = P(̃ζ (n) > x). For x > x
′, we have

P(ζ (n)
1,0 > x) = L̃ζ (n)(x) P(ζ (n)
1,0 > x)
P(X0 > x) P(̃ζ (n) > x) ⩽ P(̃ζ (n) > x).

Further,
 lim
x→∞ P(̃ζ (n) > x)
P(X0 > x) = lim
x→∞ P(X0 > x)
L̃ζ (n)(x) P(X0 > x) = 0,

since limx→∞ L̃ζ (n)(x) = ∞. Since P(ζ (n)
1,0 > x) ⩽ P(̃ζ (n) > x), x ∈ R+, we have

E(ζ (n)
1,0 ) = ∫ ∞

0 P(ζ (n)
1,0 > x) dx ⩽ ∫ ∞

0 P(̃ζ (n) > x) dx = E(̃ζ (n)),

and since ̃ζ (n) is regularly varying with index β0 ∈ (1, 2), we have E(̃ζ (n)) < ∞.

Let (̃ζ (n)
j )j∈N be a sequence of independent identically distributed random variables with
common distribution as that of ̃ζ (n). By some properties of ﬁrst order stochastic dominance
(see, e.g., Shaked and Shanthikumar [25, part (b) of Theorem 1.A.3 and Theorem 1.A.4]), we
have

(G.7) P
 ( k∑

i=1 ζ (n)
i,0 > x

)
 ⩽ P
 ( k∑

i=1 ̃ζ (n)
i > x

)

for all x ∈ R+ and k ∈ N. Put ̃mn := E(̃ζ (n)). Let us consider the decomposition

p(x, q) =
 ⌊(1−q)x/ ̃mn ⌋∑

k=1 P
 ( k∑

i=1 ζ (n)
i,0 > x

)
 P(X0 = k)

+
 ⌊(1−q)x/mn⌋∑

k=⌊(1−q)x/ ̃mn⌋+1 P
 ( k∑

i=1 ζ (n)
i,0 > x

)
 P(X0 = k) =: p1(x, q) + p2(x, q), x ∈ R+.

Here mn ⩽ ̃mn, and hence ⌊(1 − q)x/ ̃mn⌋ ⩽ ⌊(1 − q)x/mn⌋, x ∈ R+, q ∈ (0, 1). Applying
Theorem F.1 with γ := ̃mn
1−q > ̃mn, we conclude the existence of a constant C(q, n) ∈ R++
(not depending on k and x, but on q and n) such that

(G.8) P
 ( k∑

i=1 ̃ζ (n)
i > x

)
 ⩽ C(q, n)k P(̃ζ (n) > x) for all x ⩾ γk, k ∈ N.

38

Using (G.7) and (G.8), we obtain

p1(x, q) ⩽
 ⌊(1−q)x/ ̃mn⌋∑

k=1 P
 ( k∑

i=1 ̃ζ (n)
i > x

)
 P(X0 = k)

⩽ C(q, n)
 ⌊(1−q)x/ ̃mn⌋∑

k=1 k P(̃ζ (n) > x) P(X0 = k) ⩽ C(q, n) E(X0) P(̃ζ (n) > x), x ∈ R+.

Hence for each q ∈ (0, 1),

lim sup
x→∞ p1(x, q)
P(X0 > x) ⩽ C(q, n) E(X0) lim sup
x→∞ P(̃ζ (n) > x)
P(X0 > x) = 0,

where the last step follows by the corresponding property of ̃ζ (n). Moreover,

p2(x, q) ⩽ P
 



⌊(1−q)x/mn⌋∑

i=1 ζ (n)
i,0 > x




 ⌊(1−q)x/mn⌋∑

k=⌊(1−q)x/ ̃mn⌋+1 P(X0 = k)

⩽ P
 



⌊(1−q)x/mn⌋∑

i=1 ζ (n)
i,0 > x



 P(X0 > ⌊(1 − q)x/ ̃mn⌋)

= P
 


⌊(1−q)x/mn⌋∑

i=1 ζ (n)
i,0 > x



 P (
X0 > (1 − q)x
̃mn
 ) .

Since X0 is regularly varying with index β0, we have

lim
x→∞
 P (X0 > (1−q)x
̃mn
 )

P(X0 > x) = ( ̃mn
1 − q
 )β0 ,

hence, for each q ∈ (0, 1), applying (G.6), we conclude

lim sup
x→∞ p2(x, q)
P(X0 > x) ⩽ 0 · ( ̃mn
1 − q
 )β0 = 0.

Finally, we turn to the case β0 = 1. For each q ∈ (0, 1), we have

p(x, q) =
 ⌊(1−q)x/mn⌋∑

k=1 P
 ( k∑

i=1 ζ (n)
i,0 > x

)
 P(X0 = k)

=
 ⌊(1−q)x/mn⌋∑

k=1 P
 ( k∑

i=1 ζ (n)
i,0 − kmn > x − kmn
)
 P(X0 = k).

Let r′ ∈ (1, 2]. According to Lemma 2.1 in Robert and Segers [24] with γ = mnq
1−q , there
exist positive numbers v and C = C(v, q, n) such that for all x ∈ R+ and k ∈ N with

39

k ⩽ ⌊(1 − q)x/mn⌋,

P
 ( k∑

i=1 ζ (n)
i,0 − kmn > x − kmn
)
 ⩽ k P
(ζ (n)
1,0 − mn > v(x − kmn)) + C
(x − kmn)r′ ,

since x − kmn ⩾ γk for all x ∈ R+ and k ∈ N with k ⩽ ⌊(1 − q)x/mn⌋. Consequently,

p(x, q) =
 ⌊(1−q)x/mn⌋∑

k=1 P
 ( k∑

i=1 ζ (n)
i,0 − kmn > x − kmn
)
 P(X0 = k)

⩽
 ⌊(1−q)x/mn⌋∑

k=1 P(X0 = k) (
k P(
ζ (n)
1,0 − mn > v(x − kmn)) + C
(x − kmn)r′
 )

⩽
 ⌊(1−q)x/mn⌋∑

k=1 P(X0 = k) (
k P(
ζ (n)
1,0 > v(x − kmn)) + C
(x − kmn)r′
 )

⩽ P(ζ (n)
1,0 > qvx)
 ⌊(1−q)x/mn⌋∑

k=1 k P(X0 = k) + C
(qx)r′

⩽ P(ζ (n)
1,0 > qvx) E (X01{X0⩽⌊(1−q)x/mn⌋}) + C
(qx)r′ ,

where for the last but one step, we used that x − kmn ⩾ qx for k ∈ {1, . . . , ⌊(1 − q)x/mn⌋}.
Since r′ ∈ (1, 2], by Lemma E.4, we have C/(qx)r′ = o(P(X0 > x)) as x → ∞, so we only
have to work with the ﬁrst term. If E(X0) < ∞, then E (
X01{X0⩽⌊(1−q)x/mn⌋}) ⩽ E(X0) < ∞
also holds, and

P(ζ (n)
1,0 > qvx)
P(X0 > x) = P(X0 > qvx)
P(X0 > x) · P(ζ (n)
1,0 > qvx)
P(X0 > qvx) → 0 as x → ∞,

where we used that X0 is regularly varying with index 1, and that P(ζ (n)
1,0 > x) = o(P(X0 > x))
as x → ∞ also holds (as it was already proved earlier). Now we consider the case E(X0) = ∞.
By Markov’s inequality, P(ζ (n)
1,0 > qvx) ⩽ E((ζ (n)
1,0 )r)/(qvx)r (note that in this case, E((ζ (n)
1,0 )r)

exists, see Lemma C.1), and using the fact that lim supx→∞ E(X01{X0⩽x})
xs P(X0>x) = 0 for some 1 < s < r
(see the remark after Theorem 3.2 in Robert and Segers [24]), we have

P(ζ (n)
1,0 > qvx) E (X01{X0⩽⌊(1−q)x/mn⌋})

P(X0 > x) ⩽ E((ζ (n)
1,0 )r) E (X01{X0⩽⌊(1−q)x/mn⌋})

(qvx)r P(X0 > x)

= E((ζ (n)
1,0 )r)
(qv)r · E (X01{X0⩽⌊(1−q)x/mn⌋})

xs P(X0 > x) · 1
xr−s

= E((ζ (n)
1,0 )r)
(qv)r · ⌊(1 − q)x/mn⌋
s

xs · P (X0 > ⌊(1 − q)x/mn⌋)
P(X0 > x)

× E (X01{X0⩽⌊(1−q)x/mn⌋})

⌊(1 − q)x/mn⌋s P(X0 > ⌊(1 − q)x/mn⌋) · 1
xr−s → 0 as x → ∞.

40

Putting parts together, we have p(x, q) = o(P(X0 > x)) as x → ∞, as desired. ✷

G.2 Remark. For a corresponding result for (ﬁrst-order) Galton–Watson processes (without
immigration), see Barczy et al. [2, Proposition 2.2]. A formal application of Proposition G.1
also gives this result, namely, for each n ∈ N, we have P(Xn > x) ∼ m
nβ0
ξ P(X0 > x) as
x → ∞. In case of mξ = 0 and mη ∈ R++, Proposition 2.2 in Barczy et al. [2] gives
that P(Xn > x) ∼ m
 n
2 β0
η P(X0 > x) as x → ∞ if n ∈ N is even, and P(Xn > x) ∼

m
 n+1
2 β−1
η P(X−1 > x) as x → ∞ if n ∈ N is odd. ✷

Acknowledgements

We would like to thank the referee and Prof. Yuliya Mishura, Co-editor-in-chief, for their
comments that helped us to improve the paper.

References

[1] Athreya, K. B. and Ney, P. E. (1972). Branching Processes, Springer-Verlag, New
York-Heidelberg.

[2] Barczy, M., B˝osze, Zs. and Pap, G. (2018). Regularly varying non-stationary Galton–
Watson processes with immigration. Statistics & Probability Letters 140 106–114.

[3] Basrak, B., Kulik, R. and Palmowski, Z. (2013). Heavy-tailed branching process
with immigration. Stochastic Models 29(4) 413–434.

[4] Bingham, N. H., Goldie, C. M. and Teugels, J. L. (1987). Regular variation. Cam-
bridge University Press, Cambridge.

[5] B˝osze, Zs. and Pap, G. (2019). Regularly varying nonstationary second-order Galton–
Watson processes with immigration. Stochastic Models 35(2) 132–147.

[6] Buraczewski, D., Damek, E. and Mikosch, T. (2016). Stochastic models with power-
law tails. The equation X = AX + B. Springer, Cham.

[7] D´enes, A., Kevei, P., Nishiura, H. and R¨ost, G. (2013). Risk of infectious disease
outbreaks by imported cases with application to the European Football Championship
2012. International Journal of Stochastic Analysis Art. ID 576381, 9 pp.

[8] Du, J. G. and Li, Y. (1991). The integer valued autoregressive (INAR(p)) model. Journal
of Time Series Analysis 12(2) 129–142.

[9] Fa¨y, G., Gonz´alez-Ar´evalo, B., Mikosch, T. and Samorodnitsky, G. (2006).
Modeling teletraﬃc arrivals by a Poisson cluster process. Queueing Systems 54 121–140.

41

[10] Heyer, H. (2010). Structural aspects in the theory of probability, 2nd ed. World Scientiﬁc
Publishing Co. Pte. Ltd., Hackensack, NJ.

[11] Horn, R. A. and Johnson, Ch. R. (2013). Matrix Analysis, 2nd ed. Cambridge Uni-
versity Press, Cambridge.

[12] Hult, H. and Samorodnitsky, G. (2008). Tail probabilities for inﬁnite series of regu-
larly varying random vectors. Bernoulli 14(3) 838–864.

[13] Isp´any, M. and Pap, G. (2014). Asymptotic behavior of critical primitive multi-type
branching processes with immigration. Stochastic Analysis and Applications 32(5) 727–
741.

[14] Kaplan, N. (1974). The supercritical p-dimensional Galton–Watson process with immi-
gration. Mathematical Biosciences 22 1–18.

[15] Kashikar, A. S. (2017). Estimation of growth rate in second order branching process.
Journal of Statistical Planning and Inference 191 1–12.

[16] Kashikar, A. S. and Deshmukh, S. R. (2015). Probabilistic properties of second order
branching process. Annals of the Institute of Statistical Mathematics 67 557–572.

[17] Kashikar, A. S. and Deshmukh, S. R. (2016). Estimation in second order branching
processes with application to swine ﬂu data. Communications in Statistics – Theory and
Methods 45(4) 1031–1046.

[18] Kimmel, M. and Axelrod, D. E. (2015). Branching Processes in Biology, 2nd ed.
Springer, New York.

[19] Latour, A. (1997). The multivariate GINAR(p) process. Advances in Applied Probability
29(1) 228–248.

[20] P´enisson, S. (2014). Estimation of the infection parameter of an epidemic modeled by a
branching process. Electronic Journal of Statistics 8(2) 2158–2187.

[21] P´enisson, S. and Jacob, Ch. (2012). Stochastic methodology for the study of an epi-
demic decay phase, based on a branching model. International Journal of Stochastic Anal-
ysis Art. ID 598701, 32 pp.

[22] Quine, M. P. (1970). The multi-type Galton–Watson process with immigration. Journal
of Applied Probability 7(2) 411–422.

[23] Resnick, S. I. (2007). Heavy-Tail Phenomena: Probabilistic and Statistical Modeling.
Springer.

[24] Robert, C. Y. and Segers, J. (2008) Tails of random sums of a heavy-tailed number
of light-tailed terms. Insurance: Mathematics and Economics 43 85–92.

42

[25] Shaked, M. and Shanthikumar, J. G. (2007). Stochastic orders. Springer Series in
Statistics. Springer, New York.

[26] Tang, Q. and Yan, J. (2002). A sharp inequality for the tail probabilities of sums of
i.i.d. r.v.’s with dominatedly varying tails. Science in China (Series A) 45(8) 1006-1011.

43
