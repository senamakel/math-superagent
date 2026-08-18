<!-- source: https://arxiv.org/pdf/2207.08805 | converted from PDF -->

arXiv:2207.08805v1  [math.NT]  6 Jul 2022
THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH
ALMOST TWIN PRIMES

LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

Abstract. We consider the exceptional set in the binary Goldbach problem for sums
of two almost twin primes. Our main result is a power-saving bound for the exceptional
set in the problem of representing m = p1 + p2 where p1 + 2 has at most 2 prime
divisors and p2 + 2 has at most 3 prime divisors. There are three main ingredients
in the proof: a new transference principle like approach for sieves, a combination of
the level of distribution estimates of Bombieri–Friedlander–Iwaniec and Maynard with
ideas of Drappeau to produce power savings, and a generalisation of the circle method
arguments of Montgomery and Vaughan that incorporates sieve weights.

Contents

Part I. Introduction and proof methods 1
1. Introduction 1
2. Proof methods and limitations 3
3. Notation 8
4. Key Propositions 12

Part II. Sieves and transference 15
5. Proof of Theorem 1.1 assuming Key Propositions 15

Part III. Level of distribution estimates with power savings 22
6. Bombieri–Vinogradov range – Proof of Key Proposition 1 22
7. The case of two Chen primes – Proof of Theorem 1.2 30
8. Beyond the 1/2 barrier – Proof of Key Proposition 2 33
9. An application – Proof of Theorem 1.3 58

Part IV. The Montgomery–Vaughan result with sieve weights 60
10. Proof of Key Proposition 3 60
11. Auxiliary results 75
References 90

Part I. Introduction and proof methods

1. Introduction

In this paper, we study the exceptional set in the binary Goldbach problem with almost
twin primes. There are diﬀerent ways to deﬁne what an almost twin prime should be. We
1

2 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

shall consider here those primes p for which p + 2 has few prime factors. We deﬁne

Pk := {m ∈ N : m has at most k prime factors},

and abbreviate P1 as P. Thanks to a celebrated result of Chen [3], we know that there are
inﬁnitely many primes p such that p + 2 ∈ P2.
Based on standard heuristics of Hardy–Littlewood type, we expect that every large
m ≡ 4 (mod 6) can be written as m = p1 + p2 with pi, pi + 2 ∈ P; needless to say, this is
far out of reach as it would imply as special cases both the twin prime conjecture and the
Goldbach conjecture (for large numbers congruent to 4 (mod 6)). However, it is natural
to ask what can be said for ﬁxed k1, k2 ≥ 2 about representations of the form

m = p1 + p2 with pi ∈ P, pi + 2 ∈ Pki.(1)

We deﬁne the size of the exceptional set related to this problem by

E(N, k1, k2) := |{m ≤ N : m ≡ 4 (mod 6), m ̸= p1 + p2 ∀pi ∈ P ∩ (Pki − 2)}|;

here the restriction to m ≡ 4 (mod 6) is imposed since almost all elements of P ∩ (Pk − 2)
are ≡ 5 (mod 6).
Our main result is a power-saving estimate for E(N, 2, 3).

Theorem 1.1. There is a constant δ > 0 such that

E(N, 2, 3) ≪ N 1−δ.

Both δ and the implied constant in this theorem are eﬀective and could in principle be
computed.
This generalises the celebrated result of Montgomery and Vaughan [23] that all but a
power-saving number of even integers up to N are the sum of two primes, which implies
in our notation1
 E(N, ∞, ∞) ≪ N 1−δ.

The best known value of δ for this problem, after a series of improvements by several
authors, including Chen and Pan, Chen and Liu, Li, and Lu [17], is due to a pre-print of
Pintz [25] with δ = 0.28.
If we want both primes in (1) to be Chen primes, we are able to obtain the following
weaker estimate for the exceptional set.

Theorem 1.2. For any A > 0, we have

E(N, 2, 2) ≪A N (log N )
−A.

Here the implied constant is ineﬀective.

Theorems 1.1 and 1.2 improve upon the following estimates. For any A > 0, we have

E(N, 5, 7) ≪A N (log N )
−A,

E(N, 3, ∞) ≪A N (log N )
−A,

E(N, 2, 7) ≪A N (log N )
−A;

(2)

the ﬁrst result is due to Tolev [29], the second one is due to Meng [22], and the third one
(which improves on the other two) is due to Matom¨aki [18]. All the implied constants
appearing in (2) are ineﬀective.

1We use the notation P∞ := N.

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 3

The ternary equation m = p1 + p2 + p3 with pi being Chen primes was solved by
Matom¨aki and Shao in [20] for all large m. Even though it is not explicitly stated there,
the methods of [20] can be adapted to handle the binary case with only minor modiﬁcations
(see [28, Proposition 2.1] of the second author for a binary version of the method in [20]),
and a back-of-the-envelope calculation seems to yield an estimate of the form

E(N, 2, 2) ≪ N (log log log N )
−c.

1.1. An application to level of distribution of the M¨obius function

Let µ denote the M¨obius function. As a side product of our proof of Theorem 1.1, we
obtain the following result about the distribution of µ in arithmetic progressions to very
large moduli, when weighted by a suitably factorable function, see Deﬁnition 3.5.

Theorem 1.3 (Level of distribution 3/5 for the M¨obius function with triply well-factorable
weights). Let k ≥ 1, a ∈ Z \ {0}, A ≥ 1 and ε > 0 be ﬁxed, with ε suﬃciently small. Let
N ≥ 2 and P ≤ N ε. Let |λd| ≤ τk(d) be any triply well-factorable sequence. Then, there
exists an eﬀective constant Cε and an ineﬀective constant CA such that
∣
∣
∣
∣
∣
 ∑

d≤N 3/5−ε
d−>P
(d,a)=1
 λd( ∑

n≤N
n≡a(d)
 µ(n) − 1
ϕ(d)
 ∑

n≤N µ(n)
)∣
∣
∣
∣
∣ ≤ Cε min{CAN (log N )
−A, N P −1/200},

where d− denotes the smallest prime divisor
2 of d.

Here the range 3/5 and the notion of triply well-factorability are closely related to
Maynard’s [21, Theorem 1.1]. Theorem 1.3 extends [21, Theorem 1.1] by replacing Λ
by µ, which is a similar but technically slightly more challenging problem as the M¨obius
function is not supported on rough numbers only, and we are additionally able to produce
a saving that goes beyond the Siegel–Walﬁsz savings.

1.2. Acknowledgements

The ﬁrst author received funding from the European Research Council (ERC) under
the European Union’s Horizon 2020 research and innovation programme, grant agreement
no. 851318. The second author was supported by a Titchmarsh Fellowship and Academy
of Finland grant no. 340098.
The authors thank Kaisa Matom¨aki and James Maynard for helpful comments.

2. Proof methods and limitations

2.1. The use of nonnegative models

The proof of Theorem 1.1 is based on a nonnegative model approach, together with
three Key Propositions, stated precisely in Section 4. The Key Propositions all deal with
the problem of evaluating the binary additive convolution

f ∗ g(m) := ∑

n1+n2=m f (n1)g(n2)

for all m ≤ N outside a power-saving exceptional set. Here one or both of f, g are of the
form Λ(n)ω(n + 2), with Λ being the von Mangoldt function and ω some sieve weight;

2Here we set 1
− := ∞.

4 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

thus, these propositions concern binary additive problems for shifted primes weighted by
sieve weights. These propositions will be stated in a fairly general sieve setup for possible
applications to other additive sieve problems.
We (informally) say that a function fmodel is a model function for f : N → C, if we have

f ∗ g(m) = fmodel ∗ g(m)
(1 + o(1)
)
(3)

for all g in a suitable space of “test functions” and all m ≤ N outside a set of size O(N 1−δ).
For certain test functions, Key Propositions 1 and 2 tell us that the function

f (n) = Λ(n)ω(n + 2)(4)

can be modelled by a simpler function in the sense of (3). The simpler function is given by
replacing the sieve ω by its pre-sieve component – this concept is deﬁned precisely later,
but it roughly means that the sieve level becomes N δ and only small primes (roughly
up to N cδ) are sifted for. As these two Key Propositions do not immediately give us an
asymptotic formula, but instead transfer the additive problem to simpler functions, they
can be seen as inspired by Green’s transference principle [13].
Roughly speaking, if f is as in (4), Key Proposition 1 gives us (3) with the just mentioned
simpler model function in the case where ω is a sieve of level N 1/2−ε and g is a fairly
arbitrary function; Key Proposition 2 gives a similar statement extended to the case
where ω is a suitable sieve of level somewhat larger than N 1/2 and g is a pre-sieve of
low level on shifted primes. The ﬁnal ingredient, Key Proposition 3, gives an asymptotic
formula for the left-hand side of (3) when both f and g are of the form (4) with ω being
a pre-sieve. The three Key Propositions act together to give Theorem 1.1, as we shall see
now informally and later rigorously in Section 5.
Let
 Λk(n) := Λ(n)1Pk (n + 2)ρ(n + 2, N αk ),

where αk > 0 are some small constants and ρ(·, z) is the indicator of integers having no
prime factors ≤ z. Then, to prove Theorem 1.1 it suﬃces to prove that

Λ3 ∗ Λ2(m) ≫ N 0.99

for all but ≪ N 1−δ values of m ≤ N , m ≡ 4 (mod 6). Let νk be a minorant function
for Λk, and assume more speciﬁcally that νk(n) is of the form Λ(n)ωk(n + 2), where ωk is
some sieve weight satisfying
 1Pk (n)ρ(n, N αk ) ≥ ωk(n).

Central for our approach is that we use sieve weights that are composed of a pre-sieve
and main-sieve. One can think of the pre-sieve as handling small prime factors with high
accuracy and the main-sieve handling large prime factors with reduced accuracy. It will
come that the main sieve component interacts only weakly with the additive problem as
we will now sketch.
Let ωpre-sieve,±
k stand for the pre-sieve part of ωk and

νpre-sieve,±
k (n) = Λ(n)ωpre-sieve,±
k (n + 2).

Here the ± sign indicates whether the pre-sieve is of upper bound or lower bound form.
With this notation, our proof strategy for Theorem 1.1 can be in simpliﬁed form outlined
in the following chain of inequalities and approximations (valid outside a power-saving set

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 5

of m ≤ N ):
 Λ3 ∗ Λ2(m) sieve
≥ ν3 ∗ Λ2(m)

KP1
≈ νpre-sieve,−
3 ∗ Λ2(m)

KP3
≈ νpre-sieve,+
3 ∗ Λ2(m)

sieve
≥ νpre-sieve,+
3 ∗ ν2(m)

KP2
≈ νpre-sieve,+
3 ∗ νpre-sieve,−
2 (m)

KP3
≈ [expected main term].

Here, in the ﬁrst step we applied the minorant function for Λ3. In the second step, we
used Key Proposition 1 to replace ν3 by its pre-sieve component, which is much easier to
understand. In the third step, we applied Key Proposition 3 that in this context acts as
a fundamental lemma to replace the lower bound sieve νpre-sieve,−
3 with the corresponding
upper bound sieve νpre-sieve,+
3 ; in the pre-sieve range, these two functions are very close to
each other in the ℓ1 norm. In the fourth step, we applied a minorant to Λ2, this being
possible thanks to the nonnegativity of the upper bound sieve νpre-sieve,+
3 . In the ﬁfth step,
we replaced ν2 (which turns out to be a sieve of level N 1/2+η for some small η > 0) by
its pre-sieve part using Key Proposition 2. Finally, the resulting additive convolution is a
version of Λ∗Λ(m) with additional pre-sieves. The case of Λ∗Λ(m) outside a power-saving
exceptional set was handled by Montgomery and Vaughan in [23], and the sifted version
can be evaluated with Key Proposition 3 (with the resulting asymptotic formula including
the contribution of a possible Siegel zero).
Note that if g ≥ ν for some (not necessarily nonnegative) function ν, then the inequality

f ∗ g(m) ≥ f ∗ ν(m)

can be guaranteed to hold pointwise only if f is nonnegative. Therefore, in the fourth
step above it was important that we were able to obtain a nonnegative model function
(otherwise, we would have had to apply the vector sieve, which would have lost a vital
constant factor). Our exploitation of nonnegative models in additive problems is motivated
by the earlier work [14] of the ﬁrst author, see also [20] where Bohr sets are used to produce
nonnegative model functions. The Bohr set approach gives, as mentioned before, worse
error terms, but is more ﬂexible; it is not immediately clear how our strategy would adapt
to the case of Maynard–Zhang type almost twin primes also considered in [20].
The proof of Theorem 1.2 is comparatively simple, the only tool we use is a slightly
generalised form of Key Proposition 1 (see Proposition 6.5).

2.2. Discussion of the Key Propositions

The proof of each of Key Propositions 1, 2 and 3 starts with an application of the
circle method, which translates the problem of understanding f ∗ g(m) into the realm of
understanding the Fourier transforms of f and g. Key Propositions 1 and 2 use pointwise
Fourier information; Key Proposition 1 uses pointwise information on ̂f on the whole of
[0, 1], whereas Key Proposition 2 uses pointwise information on ̂f only on the major arcs

6 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

(see Deﬁnition 3.1) and a bound for ̂g in the complementing minor arcs. Key Proposi-
tion 3 uses a more precise treatment of the contribution of the major arcs, in the spirit of
Montgomery and Vaughan’s work [23].
We thus need diﬀerent types of Fourier information for f (n) = Λ(n)ω(n + 2) with
the sieve ω having as large a level as possible. On the minor arcs, we can only reach
the level N 1/2−ε by the work of Matom¨aki [18] on Bombieri–Vinogradov type bounds
for exponential sums. Key Proposition 1 follows from this result and a version of the
Bombieri–Vinogradov theorem which gives power savings. Such a power-saving estimate
can indeed be achieved with the large sieve if one uses a main term that takes into account
all the characters of conductor ≤ N δ, instead of only the principal character.
While Chen’s approach provides a minorant for Λ2(n) using sieve switching and sieves
of level N 1/2−ε, unfortunately we cannot use this minorant; see Subsection 2.3 for an ex-
planation of this limitation. Thus, our approach is to do without sieve switching. Without
sieve switching, one can still construct a minorant for numbers with at most two prime
divisors, provided that one has level of distribution slightly larger than 1/2, where the
best known value is 0.511 . . .
by work of Greaves [11]. However, we cannot use his type of sieves either, as we can break
the N 1/2 barrier for primes only if the weights enjoy some nice factorability properties.
Fourvry and Grupp [7] found a working compromise and used Laborde’s sieve [16] together
with level of distribution estimates (based on the dispersion method) of Fouvry [6] and
Bombieri–Friedlander–Iwaniec [1] to get a minorant for the Chen primes without switching.
We extend their approach to cover the whole major arcs and give power savings. This
then gives us Key Proposition 2.
Fundamentally, a power saving for applications of the dispersion method is possible
because one can apply the large sieve in the same way as in the power-saving Bombieri–
Vinogradov estimate mentioned above; there is previous work on some dispersion method
estimates with power savings by Drappeau [5]. There are several additional complications
for us when adapting his approach to the work of Fourvry and Grupp [7] and the underlying
dispersion estimates. In particular, we need to set up a version of the dispersion method
that produces power savings and works in quite some generality. This rules out certain
results of Fouvry [6] used in [7]. We rely on an extension of Maynard’s recent work [21]
to patch the gaps in our arithmetic information.
The proof of Key Proposition 3 follows the overall strategy of Montgomery and Vaughan’s
work [23], but the presence of sieve weights complicates matters. Their proof uses that
for (an, q) = 1 one has
 e
( an
q
 ) = 1
ϕ(q)
 ∑

χ(q) χ(an) ∑

b(q)∗ χ(b)e
( b
q
 )
(5)

and so they can translate from major arc integrals to character sums. Montgomery and
Vaughan then reduce to primitive characters and keep careful track of the weight of each
ﬁxed pair of primitive characters. These weights can be called pseudo-singular series,
where the pair of primitive (trivial) characters to the modulus 1 gives the classical singular
series. They conclude the proof by bounding the pseudo-singular series by the classical one
and applying Gallagher’s prime number theorem [10]. To approach Key Proposition 3, we
translate both the divisibility condition of the sieve weights as well as the additive phase
from the circle method (similarly as in (5)) to multiplicative characters. We are then led to

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 7

more complicated pseudo-singular series that contain sieve weights. The required results
for those can be seen as a combination of Montgomery and Vaughan’s pseudo-singular
series bounds with a fundamental lemma of sieve theory. Here the diﬃculty lies in not
incurring any additional losses. This is necessary, since in the power-saving exceptional
set range the savings from Gallagher’s prime number theorem and the fundamental lemma
are very weak, only of the type o(expected main term). Additionally, in order to ensure
this type of saving even when the exceptional zero exists – in which case the expected
main term can be much smaller – we sieve separately for primes dividing the exceptional
modulus.

2.3. Limitations

With our current knowledge, the simplest way to construct a lower bound for Chen
primes is by the use of sieve switching, and indeed we apply it in the proof of Theorem 1.2.
However, its application in a binary additive problem has issues when the exceptional
character enters the picture. To get power saving, one has to consider distribution of
primes in arithmetic progressions with moduli being a power of the summation length,
so that the possible existence of a real zero of a real so-called exceptional character plays
a role. We now give a rough sketch of why that is the case. With sieve switching, one
constructs a lower bound of the form

Λ2(n) ≥ Λ(n)ω−(n + 2) − cswitchingω+(n)ΛE3(n + 2) := Λ
−
2 (n),(6)

where ω± are upper and lower bound sieves and ΛE3(n) is a suitably weighted indicator of
integers having precisely three prime factors. For simplicity, we assume that the sieves are
normalised in such a way that the existence of inﬁnitely many Chen primes then follows
from 1 − cswitching > 0.
If we then consider Λ2 ∗ Λ2(m), by Key Proposition 1 we can remove the main sieve
components from ω±, and by Key Proposition 3 the lower bound sieve can be replaced
with an upper bound one. If the exceptional character ̃χ (mod ˜r) with bad zero ̃β exists,
then, ignoring the contribution of all other characters, we expect that in the additive setup
we have
 Λ(n) ≈ ΛE3(n) ≈ ω+(n)(1 − ̃χ(n)n ̃β−1) log n.

These approximations can be heuristically justiﬁed by assuming that GRH holds outside
the one exceptional zero ̃β. In that case, one can calculate
∑

n≤X f (n)ω±(n + 2)e
( an
q
 )
(7)

with q ≤ X δ and for f = Λ or f = ΛE3 with a high degree of precision. The result is
that the main term is the same as the expected main term for the case f (n) = ω+(n)(1 −
̃χ(n)n ̃β−1). In Part IV, we make this argument rigorous without assuming GRH.
We thus get the expected approximation in an additive setup

Λ
−
2 (n) ≈ ω+(n)ω+(n + 2)
((1 − cswitching) − (̃χ(n) − cswitching ̃χ(n + 2))n ̃β−1)
) log n.

In the binary additive problem Λ
−
2 ∗ Λ2(m), the function Λ2(n) may behave like

ω+(n)ω+(n + 2)(1 − ̃χ(n)n ̃β−1) log n

8 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

(if we do not apply switching; doing otherwise only exacerbates the problem). We then
get a certain Hardy–Littlewood type main term for the additive problem. Its shape is
given by the following heuristics. The terms without characters in both summands give
rise to the usual main term with singular series S(m). Mixed terms where one summand
contributes a character and the other does not are small. The terms with ˜χ(n) give a
secondary main term of the form S(m)m ˜β. Finally, the combination of ̃χ(n) with the
̃χ(n + 2) term gives us a similar term with shifted singular series, ̃S′(m + 2)m ˜β. So we
expect a main term of the form

(1 − cswitching)S(m)m + ̃S(m)m ̃β − cswitching ̃S
′(m + 2)m ̃β.(8)

As in [23], if m is divisible by the exceptional modulus and ̃χ(−1) = −1, we have
̃S(m) = −S(m). In that case

S(m)m + ̃S(m)m ̃β ≈ S(m)(1 − ̃β) log N.

For those bad m we have that ̃S′(m + 2) is small (as ̃r | m implies that (̃r, m + 2) is small).
We consequently get a negative main term

(8) ≈ S(m)
((1 − ̃β) log N − cswitching) < 0,

for any exceptional zero worth its name.
The issue just presented is the reason behind our application of level of distribution
> 1/2 results that are achieved with the dispersion method and ultimately rely on the
spectral theory of automorphic forms. With this increased level of distribution we no
longer require sieve switching and avoid the above-mentioned issue. If we restricted our
attention to E(N, 3, 3), or if the exceptional zero does not exist, we could do without this
heavy machinery.
We remark that the techniques we employ are insuﬃcient to produce a power saving for
sums of two Chen primes, even under the assumption that the exceptional zero does not
exist. Our three Key Propositions allow us to remove the main sieve component of a sieve
and exchange upper and lower bound pre-sieves. This is not enough to ﬁnd a nonnegative
model after an application of sieve switching as in (6). To obtain a power saving for
E(N, 2, 2) one consequently would need to on the one hand improve the nonnegative
model technique we use and on the other hand ﬁnd a way to deal with an exceptional
zero, possibly in a completely diﬀerent manner.
Alternatively, we could avoid the issue of sieve switching completely if a minor arc bound
for Λ(n)ω(n + 2) was proved for a suﬃciently large level sieve (somewhat bigger than
N 1/2), as we are able to handle the Fourier transform of this function on the major arcs.
In another direction, a wide zero-free strip for the relevant L-functions would immediately
solve all our problems. However, breaking the 1/2 barrier on the minor arcs in any form is
a challenge, and the diﬃculty of proving a zero-free strip does not need any explanation.

3. Notation

We now introduce some notation that is used throughout the paper. We also deﬁne
terms related to sieves and the circle method that we need to state our Key Propositions.

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 9

3.1. Asymptotic notation

We use the standard Landau and Vinogradov notation O(·), o(·), ≪, ≫. By A ∼ B we
mean that A < B ≤ 2A.

Convention 1. By c (respectively C) we denote small (respectively large) positive con-
stants that can vary from line to line. Thus, for instance, an estimate X ≪ Y −c means
that there is some constant α > 0 such that X ≪ Y −α.
In contrast, c0 and c1 are ﬁxed small constants that do not vary from line to line. It
will come out of our calculations that the choices

c0 = 1/1000

c1 = c0/100

are admissible.

3.2. Variables

Throughout, we assume N ≥ P ≥ 2 with N large. The variable N stands for the range
in Theorems 1.1 and 1.2 and the related range of the summands. The variable P relates
to sieves; primes up to P will be handled by the pre-sieves. We later choose P to be a
small power of N . To be consistent with other applications of the dispersion method, the
usage of N in Section 8 is diﬀerent.
The variable p always stands for primes, and the variables m, n for natural numbers.
We sometimes abbreviate [D] = {1, . . . , D}.

3.3. Major and minor arcs

In order to apply the circle method, we now ﬁx our choice of the major and minor arcs.

Deﬁnition 3.1 (Major and minor arcs). Let Q = N/P c0 . Deﬁne the major arcs

M(P ) := [0, 1) ∩ ⋃

1≤q≤P c0
 ⋃

(b,q)=1
 [ b
q − 1
Q , b
q + 1
Q
 ]

and the minor arcs
 m(P ) := [0, 1) \ M(P ).

Note that we are taking the major arcs to be slightly wider than usual (width 1/Q
around a/q instead of 1/(qQ)) as this turns out to be technically a more convenient
choice.

3.4. L-functions

We reserve the letters χ and ψ to denote Dirichlet characters and denote by L(s, χ) the
associated L-function. We denote by χ(q)
0 the principal character (mod q). We will also
need the notion of exceptional zeros of L-functions.

Deﬁnition 3.2 (Exceptional zero). By an exceptional zero of level R ≥ 2, we mean a real
zero ˜β ∈ (1 − 10−3/ log R, 1) of some L-function L(s, ˜χ) with ˜χ being primitive and having
modulus ≤ R. The character ˜χ is then called an exceptional character, and its modulus ˜r
is called the exceptional modulus.

10 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

By the Landau–Page theorem (in the form of [24]), if an exceptional zero ˜β of level
R ≥ C exists, it must be unique, and ˜χ must be real and unique.
Related to the exceptional zero is Siegel’s theorem in which the implied constant is not
eﬀectively computable.

Convention 2. Unless otherwise stated, the implied constants in our use of the ≪ and
O(·) notation are eﬀective.

3.5. Arithmetic functions

The symbols Λ, µ, ϕ stand for the von Mangoldt, M¨obius and Euler totient functions.
By τk we denote the k-fold divisor function, and we let τ := τ2.
For an arithmetic function a, we deﬁne its ℓ2 norm as

∥a∥2 :=
 (∑

n |a(n)|
2)1/2 .

We use the standard notation
 eq(a) := e ( a
q
 ) .

For a real number P ≥ 2 and integer n ≥ 1, we factorise n = n≤P · n>P , where the smooth
part n≤P and the rough part n>P are given by

n≤P := ∏

p≤P pvp(n), n>P := ∏

p>P pvp(n),

where vp(n) is the largest integer k such that pk | n. For an integer n ≥ 2, we also deﬁne
n+ (respectively n−) as the largest (respectively smallest) prime factor of n (with the
convention 1+ = 1, 1− = ∞).
We often abbreviate a (mod q) as a(q). Sums over a(q) are taken over a system of
representatives of residues classes; similarly, sums over χ(q) are taken over characters to
the modulus q. We denote by ∑

a(q)∗, ∑

χ(q)∗

sums over primitive residue classes and primitive characters, respectively.
For two integers n1, n2, we denote by (n1, n2) and [n1, n2] the greatest common divisor,
respectively the least common multiple, of |n1| and |n2|. By n we denote the inverse of n
(mod q) when q is clear from context.
Given a character χ (mod q) and a factorisation q = q1q2 with q1, q2 ≥ 1 coprime, we
can uniquely factorise χ = χ(q1)χ(q2), where χ(qi) (mod qi) are characters. In particular,
we have the complete factorisation of χ (mod q) as

χ = ∏

p|q χ(pα(q)),(9)

where χ(pα(p)) is a character modulo pα(p). We denote furthermore by χ(pα∗(p)) the p-
component of the primitive character inducing χ. By τ (χ) we denote the usual Gauß sum∑a(q) χ(a)e(a/q).

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 11

We denote by ∗ and ⋆ the additive and multiplicative convolution operators, respectively.
That is, for any two arithmetic functions α, β, we write

α ∗ β(m) = ∑

a+b=m α(a)β(b)

α ⋆ β(m) = ∑

ab=m α(a)β(b).

3.6. Sieves

The letter P is reserved for squarefree integers. We further use the following notation
for the case that it is the product of all primes in a certain range:

P(w, z) := ∏

w<p≤z p, P(z) := P(1, z).

We also need the related rough number indicators

ρ(n, z) := 1(n,P(z))=1, ρ(n, w, z) := 1(n,P(w,z))=1.

Deﬁnition 3.3 (Sieve). We say that ω is a sieve of range P, level D and order k, if

ω(n) = ∑

d|n λd

for some coeﬃcient sequence |λd| ≤ τk(d) supported only on {d ≤ D : d|P}. If the range
is P(1, z) for some z, we sometimes say that the range is z.

To describe the interaction of a sieve ω with a sequence that has a local density function
1/ϕ(d), we deﬁne
 V(ω) := ∑

d
 λd
ϕ(d) .(10)

One expects that the sieve weights λ approximate the M¨obius function, so that V(ω) is
comparable to
 V (P) := ∑

d|P
 µ(d)
ϕ(d) = ∏

p|P
 (
1 − 1
p − 1
 ) .(11)

If P = P(z1, z2), we simply denote the quantity above by V (z1, z2).
Several of our results will depend on the fact that the appearing sieve weights can be
suitably factorised.

Deﬁnition 3.4 (Well-factorable sequences). We say that a sequence λ : [D] → C is well-
factorable of level D and order k if |λd| ≤ τk(d) and, for any R, S ≥ 1 with D = RS, there
exist sequences |α(d)|, |β(d)| ≤ τk(d) supported on [1, R] and [1, S], respectively, such that
λ = α ⋆ β.

As is well known, the important linear sieve weights are essentially well-factorable.
The notion of triply well-factorable weights was introduced by Maynard [21] as a stronger
condition than well-factorability.
3

3Strictly speaking, Maynard asks for the sequences to be 1-bounded. This is purely technical and we
chose to keep in line with what we need in our application in the case of Well-factorable sequences.

12 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

Deﬁnition 3.5 (Triply well-factorable sequences). We say that a sequence λ : [D] → C is
triply well-factorable of level D and order k if |λd| ≤ τk(d) and, for any R, S, T ≥ 1 with
D = RST , there exist sequences |α(d)|, |β(d)|, |γ(d)| ≤ τk(d) supported on [1, R], [1, S],
[1, T ], respectively, such that λ = α ⋆ β ⋆ γ.

4. Key Propositions

In this section, we state our three Key Propositions for proving Theorem 1.1, which give
information about binary additive convolutions of a certain type outside a power-saving
exceptional set.
Before stating the Key Propositions, we need to deﬁne the types of sieves that appear
in them. When working with a problem involving sieves of large level, it is often very
convenient to assume that the sieves at hand factor as the product of a pre-sieve and
a main sieve. Thus, we wish to work with sieves ω of level D and range z that factor
as ω = ω1ω2 with ω1, ω2 sieves of ranges P(P ) and P(P, z). Then, the pre-sieve ω1 is
amenable to the fundamental lemma of sieve theory, and ω2 has been separated from the
inﬂuence of the small prime factors. In particular, since P is larger than the major arc
cut-oﬀ P c0, one may hope that ω2 behaves much like a constant function in the setup of
the circle method.
While the aforementioned linear sieve is suitable for sieving for rough numbers and
enjoys good factorisation properties, the situation is more delicate if one sieves for numbers
with few prime factors. In that case, one can no longer expect well-factorable behaviour.
We now deﬁne the required level and partial well-factorisation properties that we are able
to handle on the major as well as minor arcs.

Deﬁnition 4.1 (Admissible main sieve). Let N ≥ 2. We call an arithmetic function
ω : N → R an admissible main sieve with parameters P, ε, k if
• ω(n) = ∑d|n λ(d) is a sieve of level N 1/2−ε, range P and order k where P − > P .
• λ = ∑j≤C log N αj ⋆ λ′
j, where for each j there exists tj ≥ 0 such that |αj| ≤
1[Y,2Y ](j) for Y = N tj , 0 ≤ tj ≤ 1/3− ε and λ′
j is well-factorable of level N 1/2−tj −ε

and order k.

Remark 4.2. The reason for limiting the level of the sieve to slightly less than N 1/2

in this deﬁnition is the Bombieri–Vinogradov theorem, or more precisely a version of it
with additive character twists and well-factorable weights by Matom¨aki [18]. See also [20,
Hypothesis 6.3].

Our ﬁrst Key Proposition allows us to “transfer” a convolution of the form (3) involving
admissible sieves into a much simpler convolution involving only their pre-sieve parts. Here
the test function g can be fairly arbitrary, as long as the loss of taking its ℓ2 norm can be
compensated for.

Key Proposition 1 (Transferring a convolution of sieves to its pre-sieve part I). Let
k ≥ 1 and ε ∈ (0, 10−4) be ﬁxed. Let N ≥ 3 and (log N )C ≤ P ≤ N ε. Let

f (n) := Λ(n)ω1(n + 2)ω2(n + 2),

where ω1 is a sieve of range P , level D0 ≤ N 5ε and order k, and ω2 is an admissible main
sieve with parameters P, ε, k. Let g : [1, N ] → C be any function. Then, for all m ∈ [1, N ]
apart from ≪ N/P c1 exceptions, we have

f ∗ g(m) = V(ω2)fpre-sieve ∗ g(m) + O(∥g∥2N 1/2P −c1),

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 13

where
 fpre-sieve(n) := Λ(n)ω1(n + 2).

Note that, unlike for the case of detecting numbers with at most three prime divisors,
there is no admissible main sieve to lower bound numbers with at most two prime divisors.
Since the level of admissible main sieves is restricted to N 1/2−ε, the parity problem prevents
admissible main sieves from detecting products of at most two primes without the use of
sieve switching; see [12, page 175] for a detailed explanation.
Fouvry and Grupp [7] successfully constructed a lower bound for Chen primes without
the use of sieve switching, by showing that sieves of the following form can be handled on
shifted primes.

Deﬁnition 4.3 (Fouvry–Grupp sieve). Let N ≥ 2 and

gε(t) :=
 



4/7 if 0 ≤ t ≤ 2/7 − ε
11/20 if 2/7 − ε < t ≤ 1/3 − ε
1/2 if 1/3 − ε < t ≤ 1/2 − ε.

We call an arithmetic function ω : N → R a Fouvry–Grupp sieve with parameters P, ε, k,
if • ω(n) = ∑d|n λ(d) is a sieve of level N 4/7−ε, range P and order k with P − > P .
• λ = ∑j≤C log N αj ⋆ λ′
j where for each j there exists tj ≥ 0 such that αj =
1[Y,2Y ]∩P(j) with Y = N tj and λ′
j is well-factorable of level N gε(tj )−tj −ε and order
k.

Remark 4.4. Note that the class of Fouvry–Grupp sieves includes sequences that may
have a level of distribution as large as N 4/7−ε. The exponent 4/7 here corresponds to
the level of distribution in the work of Bombieri–Friedlander–Iwaniec [1]. Observe that if
tj ≤ 2/7 − ε, then ω is well-factorable, so the 4/7 level of distribution result in [1] can
be used to control the behaviour of Λ(n)ω(n + 2). If instead 2/7 − ε ≤ tj ≤ 1/3 − ε,
Fouvry and Grupp succeed by using level of distribution results from [1] and [6], and also
exploiting that αj is assumed to be a prime indicator function and so can be opened with
combinatorial decompositions.

The second Key Proposition extends Key Proposition 1 by replacing an admissible main
sieve by a Fouvry–Grupp sieve. Since we are lacking a minor arc bound for the primes
twisted by Fouvry–Grupp sieves, the price paid for this extension is a restricted choice of
test functions.

Key Proposition 2 (Transferring a convolution of sieves to its pre-sieve part II). Let
k ≥ 1 and ε ∈ (0, 10−9) be ﬁxed. Let N ≥ 3 and (log N )C ≤ P ≤ N ε. Let

f (n) := Λ(n)ω1(n + 2)ω2(n + 2),

where ω1 is a sieve of range P , level D0 ≤ N ε and order k and ω2 is a Fouvry–Grupp
sieve with parameters P, ε, k. Let
g(n) := Λ(n)ω3(n + 2),

where ω3 is a sieve of level D0 ≤ N ε and order k. Then, for all m ∈ [1, N ] apart from
≪ N/P c1 exceptions, we have

f ∗ g(m) = V(ω2)fpre-sieve ∗ g(m) + O((N + ∥g∥2N 1/2)P −c1),

14 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

where
 fpre-sieve(n) := Λ(n)ω1(n + 2).

Key Propositions 1 and 2 allow us to remove main sieve components in binary problems,
thus reducing the task of estimating the binary additive convolutions of the primes twisted
by sieves to the case where the sieves are mere pre-sieves. The ﬁnal main ingredient
for the proof of Theorem 1.1 is an extraction of the main term of the binary additive
convolution (for most n) in the case where both the involved functions only contain a
pre-sieve component. We now deﬁne the relevant sifting ranges.

Deﬁnition 4.5. Let ̃r denote the exceptional modulus to level P c0, and set

̃P := ∏

p|̃r
p>2
 p,

with the interpretation that the product is 1 if ˜r does not exist. Deﬁne furthermore

P † := ∏

p∤̃r
2<p≤P
 p.

Although the dimension of the sieving for almost primes of the form p + 2 is one, our
pre-sieves need to be able to handle higher dimensions. A similar phenomenon occurs in
the study of sieve weights in short intervals, see for example [9, Chapter 6.10] and [19].
The combinatorial β sieve (see [9, Chapter 6.4] for its precise deﬁnition) is our choice of
pre-sieve. We will see that taking β = 750 suﬃces for our purpose, confer (161), (167).
Treating the sieves more carefully would make it possible to reduce the value of β con-
siderably, but it seems inherent to our approach that the natural choice for problems of
dimension 1, i.e. β = 2, is not suﬃcient.

Deﬁnition 4.6 (Admissible pre-sieve). Let N ≥ 2. We call ω an admissible pre-sieve
with parameters P, D0 if ω(n) = ω0(n)1(n, ̃P)=1, where ω0 is an upper or lower bound beta

sieve with β = 750 (see [9, Chapter 6.4]), of range P † and level D0 ≥ P 1000.

Remark 4.7. The upper and lower bound sieves just deﬁned have the property that

ω−(n) ≤ ρ(n, P ) ≤ ω+(n).

Further, since D0 ≥ P 1000, in both upper and lower bound case they fulﬁl a fundamental
lemma to the eﬀect that (recalling the deﬁnitions (10) and (11))

V(ω) = V (P )
(1 + 100θe
− log D0
log P )
), for some |θ| ≤ 1.(12)

See [9, Lemma 6.8]. Note that in the deﬁnition of ω the sieve is required to be exact on
the divisors of the exceptional modulus. This will be important in Key Proposition 3 for
handling the contribution of the exceptional character.

Our third Key Proposition states that we can insert two admissible pre-sieves into
the method of Montgomery–Vaughan [23] while only incurring an additional error term
of fundamental lemma type. As in [23], the main term and error terms depend on the
existence and location of a possible exceptional zero.

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 15

Key Proposition 3 (Sums of two sifted primes). There exist functions M(m), E(m)
such that the following holds. For any choice of ν1, ν2 of the form

νi(n) := Λ(n)ωi(n + 2),

where ωi are admissible pre-sieves with parameters P ≤ N , D0 ≤ N 1/1000, we have

ν1 ∗ ν2(m) = mV (P )
2S(m)
(M(m)
(1 + O(e
−c log D0
log P )
) + O(
e
100
√log N P −c1 + e
−c log N
log P E(m)
))
(13)

for all but ≪ N/P c1 values of m ≤ N , where the singular series is given by

S(m) := 12|m · 2 ∏

p|m(m+4)
p̸=2
 (
1 + p − 4
(p − 2)2
 ) ∏

p|m+2
p̸=2
 (1 + 2
p − 2
 ) ∏

p∤m(m+2)(m+4)
p̸=2
 (1 − 4
(p − 2)2
 )
.

Furthermore, the main term M(m) and the error E(m) satisfy the following:
(i) If there are no exceptional zeros of level P c0, then

M(m) = E(m) = 1.(14)

(ii) If there is an exceptional zero ̃β of level P c0 to the modulus ̃r, then

M(m) ≥ 1 − m ̃β−1 ∏

p|̃r
p∤m
 21
25 − O(̃r−0.99), E(m) = (1 − ̃β) log P.(15)

Remark 4.8. We observe that M(m) > 0 for all m ≥ 2 if P (and hence ˜r) are large
enough. Indeed,

1 − m ˜β−1 = 1 − exp(( ˜β − 1) log m) ≥ 1
10 min{(1 − ˜β) log m, 1} ≥ c/(̃r1/2(log ̃r)
2),

for some c > 0, where we used the elementary inequality 1 − e−x ≥ 1
10 min{x, 1} and the
classical (eﬀective) bound for exceptional zeros. This last bound is > B ˜r−0.9 for any B if
˜r is large enough in terms of B.

Part II. Sieves and transference

5. Proof of Theorem 1.1 assuming Key Propositions

In this section, we deduce Theorem 1.1 from Key Propositions 1, 2, 3. To do so, we
ﬁrst construct sieve minorants for the Chen primes and the primes p with p + 2 ∈ P3 that
have the shape required in Deﬁnitions 4.1 and 4.3.

5.1. Setting up the sieves

The goal of this subsection is to construct an admissible main sieve (cf. Deﬁnition 4.1)
and a Fouvry–Grupp sieve (cf. Deﬁnition 4.3) that are lower bounds for integers with
at most 3, respectively 2, prime divisors. A key ingredient in the construction is the
application of Iwaniec’s linear sieve with well-factorable weights.

Deﬁnition 5.1. We say that a multiplicative function g : N → [0, 1] is a local density
function of dimension κ if we have

κ log log z − C ≤ ∑

p≤z
 g(p)
p ≤ κ log log z + C

16 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

for all z ≥ 3.

Lemma 5.2 (Well-factorable linear sieve). Let ε > 0 and D > z > P > Dε2/(1+ε9) > 2.
Let s = log D
log z . There are sieves ω±
LIN(n) = ω±
LIN(n; D, z, P, ε) = ∑
d|n λ±
d with range P(P, z)
and level D and order 1 with the following properties.
(1) We have ω−
LIN(n) ≤ ρ(n, P, z) ≤ ω+
LIN(n).
(2) The weights are “J(ε) well-factorable” in the following sense. There exists some
J(ε) depending only on ε such that

λ
±
d = ∑

1≤j≤J(ε) λ±,(j)
d ,

where λ±,(j)
d are well-factorable weights of level D and order 1.
(3) For any local density function g of dimension 1, we have
∑

d λ−
d g(d) ≥ V (P, z){f (s) + O(
ε + (log D)
−1/6)
} if s ≥ 2 + ε,

∑

d λ+
d g(d) ≤ V (P, z){F (s) + O(ε + (log D)
−1/6)} if s ≥ 1 + ε,

where f, F stand for the functions of the linear sieve (see [9, Chapter 12.1]).

Proof. This follows from the arguments in the proof of [9, Proposition 12.18]. In fact,
since we do not have a pre-sieve in the statement, the proof is somewhat simpler. □

We now construct an admissible main sieve to lower bound P3 numbers. This is done
with the help of a simple weighted sieve.

Lemma 5.3. For any suﬃciently small ε > 0 and N ε ≤ P ≤ N 1/10, there exists an
admissible main sieve ω−
M(n) with parameters P, ε, C such that for n ≤ N we have

• ω−
M(n)ρ(n, P ) ≤ ρ(n, N 1/10)1P3 (n),
• V(ω−
M) ≫ V (P, N 1/10).

Proof. Put z = N 1/10. Suppose that y satisﬁes

y3z > N, yz < N 1/2−ε.(16)

Then, for n ≤ N , we have

1P3(n)ρ(n, z) ≥ (
1 − 1
2
 ∑

z≤p<y 1p|n)ρ(n, z)

= ρ(n, P )
(ρ(n, P, z) − 1
2
 ∑

z≤p<y 1p|nρ(n, P, z)
).

We split the summation over p dyadically and use lower and upper bound sieves as
given by Lemma 5.2 on the two occurrences of ρ(n, P, z) to deﬁne

ω−
M(n) := ω−
LIN(n, N 1/2−ε, P(P, z), ε)

− 1
2
 ∑

K
∃j≥0: K=2jz
 ∑

K≤p<min{y,2K} 1p|nω+
LIN(n, N 1/2− log K
log N −ε, P(P, z), ε).

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 17

The corresponding sieve weights are given by

λ(d) := λ−
d − 1
2
 ∑

K
∃j≥0: K=2jz
 ∑

K≤p<min{y,2K}
 ∑

d=pd′ λ+
d′(K),

where λ−
d and λ
+
d′(K) are the sieve coeﬃcients corresponding to ω−
LIN(n, N 1/2−ε, P(P, z), ε)

and ω+
LIN(n, N 1/2− log K
log N −ε, P(P, z), ε), respectively.
To calculate V(ω−
M), we apply the third part of Lemma 5.2 separately on each of the
sieves. This gives us

V(ω−
M) ≥ V (P, z)
 



(
f (s) + O(ε)
) − 1
2
 ∑

K
∃j≥0: K=2jz
 ∑

K≤p<min{y,2K}
 1
ϕ(p) (F (sK ) + O(ε))





 ,

where s := log N
2 log z , sK := s − log K
log z . In our range of summation, log p
log z = log K
log z + O( 1
log z ) and
F (sK) ≫ 1, so we get

∑

K
∃j≥0: K=2jz
 ∑

K≤p<min{y,2K}
 1
ϕ(p) (F (sK ) + O(ε)) = ∑

z≤p<y
 F (s − log p
log z )(1 + O(ε))

p .

By comparing the sum to an integral, we conclude that

V(ω−
M) ≥ V (P, z)
 (
f (s) − 1
2
 ∫ log y
log z

1
 F (s − t)
t dt + O(ε)

)
 .

Finally, set y = N 1/3−ε which is compatible with (16) and also makes ω−
M an admissible
main sieve. By a simple numerical calculation (see for example [20, Appendix A] for
details)
 V(ω−
M) ≫ V (P, z)

for any ε > 0 suﬃciently small. □

Next we import the construction from [7] to construct a Fouvry–Grupp sieve that mi-
norises numbers with at most two prime divisors.

Lemma 5.4. For any P ≤ N 1/15 and 0 < ε ≤ c, there exists a Fouvry–Grupp a sieve ω−
FG
with parameters P, ε, C such that, for all n ≤ N ,
• ω−
FG(n)ρ(n, P ) ≤ ρ(n, N 1/15)1P2(n),
• V(ω−
FG) ≫ V (P, N 1/15).

Proof. The statement is a consequence of the construction and calculations in [7, Section
IV]. The only necessary modiﬁcation is a restriction of the range to P(P, N 1/15), but this
is unproblematic. □

We will also require a simple upper bound sieve.

Lemma 5.5. For any P ≤ N 1/10 and ε ∈ (0, 1/10) there exists an admissible main sieve
ω+
M with parameters P, ε, C such that, for all n ≤ N ,

• ρ(n, P, N 1/10) ≤ ω+
M(n),
• V(ω+
M) ≤ (F (4) + O(ε))V (P, N 1/10).

18 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

Proof. We set ω+
M(n) = ω+
LIN(n, N 1/2−ε, N 1/10, P, ε). The statement follows immediately
from Lemma 5.2. □

5.2. The main proof

We require one last ingredient before we begin the proof, namely a type of vector sieve
inequality. However, we do not apply it on the vector (n1, n2) given by the two variables
n1, n2 in the equation n1 + n2 = m, but instead on (ai, bi), where aibi = ni and ai contains
(with multiplicity) all prime divisors of ni up to P . This idea of constructing a lower
bound sieve by composition goes back to Selberg [26]. See also [12], where this approach
appears on multiple occasions throughout the book.

Lemma 5.6. Let A, B ≥ 0 and A±, B± such that

AB− ≤ AB

max{B−, 0} ≤ B+

A
− ≤ A ≤ A
+.

Then
 A
+B− + (A
− − A
+)B+ ≤ AB.

Proof. We have
 AB ≥ AB− = A
+B− + (A − A
+)B−.

Since A − A+ ≤ 0, we can bound this from below by

≥ A
+B− + (A − A
+)B+.

As B+ ≥ 0, this is
 ≥ A
+B− + (A
− − A
+)B+,

as required. □

We have now gathered all the necessary tools to prove our main theorem, assuming the
Key Propositions.

Proof of Theorem 1.1, assuming Key Propositions 1, 2, and 3. Let ε > 0 be ﬁxed and suf-
ﬁciently small (the limiting factor being the constructions of the previous subsection). Let

D0 = N ε2, P = D1/A
0 ,(17)

where the constant A > 1000 is chosen suﬃciently large (but with A small enough in terms
of 1/ε).
We deﬁne the functions

Λ2(n) := Λ(n)1P2(n + 2)ρ(n + 2, N 1/15),

Λ3(n) := Λ(n)1P3(n + 2)ρ(n + 2, N 1/10).

To prove Theorem 1.1 it suﬃces to show the existence of a δ > 0 such that

Λ3 ∗ Λ2(m) ≫ N 0.99 for m ≤ N, m = 4(6), with ≪ N 1−δ exceptions,(18)
 THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 19

since the number of representations of m ≤ N in the form m = pi
1 + pj
2 with p1, p2 primes
and max{i, j} ≥ 2 is certainly ≪ N 1/2. We use Lemma 5.6 with

B = 1P3(n + 2)ρ(n + 2, P, N 1/10)

A = ρ(n + 2, P )

B− = ω−
M(n + 2) as in Lemma 5.3 with parameters P, ε, C

B+ = ω+
M(n + 2) as in Lemma 5.5 with parameters P, ε, C

A
− = ω−(n + 2) as in Deﬁnition 4.6 with parameters P, D0
A
+ = ω+(n + 2) as in Deﬁnition 4.6 with parameters P, D0
to get
Λ3(n) ≥ Λ(n)ω+(n + 2)ω−
M(n + 2) + Λ(n) (ω−(n + 2) − ω+(n + 2)
) ω+
M(n + 2)

:= gM
1 (n) + gM
2 (n),(19)

say. Since Λ2(n) ≥ 0 we have

Λ3 ∗ Λ2(m) ≥ gM
1 ∗ Λ2(m) + gM
2 ∗ Λ2(m).(20)

By construction ω−(n + 2) ≤ ω+(n + 2), and so gM
2 (n) ≤ 0. Consequently, we can use the
majorant
 Λ2(n) ≤ Λ(n)ω+(n + 2)ω+
M(n + 2) := gM
3 (n),

say, to bound
 |gM
2 ∗ Λ2(m)| ≤ |gM
2 ∗ gM
3 (m)|.

We set
 gP
1 (n) := Λ(n)ω+(n + 2)

gP
2 (n) := Λ(n) (ω−(n + 2) − ω+(n + 2)
) .

Note that ∥gM
i ∥2, ∥gP
i ∥2 ≪ N 1/2(log N )O(1) for both i. Let us for this proof write =P , ≥P ,
≤P to denote that the respective statement holds for all m ≤ N with ≪ N/P c1 exceptions.
We have by Key Proposition 1 that

gM
1 ∗ Λ2(m) =P V(ω−
M)gP
1 ∗ Λ2(m) + O (N P −c1) ,(21)

and, now applying Key Proposition 1 twice,

gM
2 ∗ gM
3 (m) =P V(ω+
M)
2gP
2 ∗ gP
1 (m) + O (N P −c1) .(22)

Here the repeated occurrence of V(ω+
M) comes from the fact that the pre-sieve components
of gM
1 and gM
3 are the same. From (20), (21), (22) we conclude that

Λ3 ∗ Λ2(m) ≥P V(ω−
M)gP
1 ∗ Λ2(m) − |V(ω+
M)
2gP
2 ∗ gP
1 (m)| + O(N P −c1).(23)

We ﬁrst deal with the second term on the right of (23). We can apply Key Proposition 3
once to each of the ω± components of gP
2 . The main term is the same in both cases and
so it cancels out. We get

|V(ω+
M)
2gP
2 ∗ gP
1 (m)| =P O(
mV(ω+
M)
2V (P )
2S(m)
(M(m)e
−c log D0
log P + e
100
√log N P −c1

+ e
−c log N
log P E(m)
).
(24)

20 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

We are left with lower bounding the ﬁrst term on the right of (23). We apply sieves
similarly as before, but we can replace the admissible main sieve with a Fouvry–Grupp
sieve, as gP
1 admits a minor arc bound. We have gP
1 (n) ≥ 0 as ω+ is an upper bound sieve.
An application of Lemma 5.6, similar to the one in (19), gives now

gP
1 ∗ Λ2(m) ≥ gP
1 ∗ (gFG
1 + gM
2 )(m),(25)

where gM
2 is as before and gFG
1 is as gM
1 , but with ω−
FG (as in Lemma 5.4)in place of ω−
M.
By Key Proposition 1 and Key Proposition 3 (applied similarly as in (24)) we have

gP
1 ∗ gM
2 (m) =P V(ω−
M)gP
1 ∗ gP
2 (m) + O(N P −c1)

=P O(mV(ω−
M)V (P )
2S(m)
(M(m)e
−c log D0
log P + e
100
√log N P −c1

+ e
−c log N
log P E(m)
) + N P −c1)
.

(26)

Since gP
1 only contains one sieve of suitable range and level and the main sieve component
of gFG
2 is a Fouvry–Grupp sieve, we deduce from Key Proposition 2 that

gP
1 ∗ gFG
1 (m) =P V(ω−
FG)gP
1 ∗ gP
1 (m) + O(N P −c).(27)

Finally, the sieve part of gP
1 is only an admissible pre-sieve, so Key Proposition 3 gives

gP
1 ∗ gP
1 (m) =P mV (P )
2S(m)
(M(m)
(1 + O(e
−c log D0
log P )
) + O(e
100
√log N P −c1 + e
−c log N
log P E(m))
).

(28)

We have
 V(ω−
FG) ≍ V(ω−
M) ≍ V(ω+
M) ≍ V (P, N )

and so from (23), (24), (25), (26), (27), and (28) we conclude that outside of a set of size
≪ N/P c1 we have

Λ3 ∗ Λ2(m)

≫ mV (N )
2S(m)
(M(m)
(1 − Ce
−c log D0
log P ) − Ce
100
√log N P −c1 − Ce
−c log N
log P E(m)
) + O(N P −c1).

(29)

Suppose now that for a suitable choice of ˜c, ˜C (which we now ﬁx) we have

M(m)(1 − ˜Ce
−˜c log D0
log P ) − ˜C(e
100
√log N P −c1 + e
−˜c log N
log P E(m)) ≥ P −c1/2.(30)

Then, using S(m) ≫ 1, we see from (29) that for m ≤ N, m ≡ 4 (mod 6) with ≪ N/P c1/10

exceptions we have
 Λ3 ∗ Λ2(m) ≫ N
(log N )2 P −c1,

and so (18) holds with δ = ε2c1/(10A). We are then left with verifying (30).
If A is chosen large enough in (17), we have

˜Ce
−˜cA ≤ 1/100,(31)

with ˜c, ˜C being the constants in (30). Then we have

1 − ˜Ce
−˜c log D0
log P ≥ 99/100.(32)
 THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 21

Furthermore,
 ˜Ce
100
√log N P −c1 ≤ 1/1000(33)

for all suﬃciently large N .
We now split the rest of the argument into two cases.
Case 1. If the exceptional zero does not exist, then by (32) we have

M(m)(1 − ˜Ce
−˜c log D0
log P ) ≥ 99/100

and
 ˜C(e
100
√log N P −c1 + e
−˜c log N
log P E(m)) ≤ ˜C(e
100
√log N P −c1 + e
−˜c log D0
log P ) ≤ 1
90

by (31) and (33). Therefore (30) holds in this case in a much stronger from.
Case 2. If the exceptional modulus ̃r with exceptional zero ̃β exists, then by (15) we
have
 M(m)(1 − ˜Ce
−˜c log D0
log P ) ≥ 99
100
 (1 − m ̃β−1 ∏

p|̃r
p∤m
 21
25 − C ˜r−0.99)
,

E(m) = (1 − ̃β) log P.

We follow the arguments in [23, Section 8] and ﬁrst discard those m ≤ N for which
(m, ̃r) > P c1/10. The number of discarded m is at most
∑

d|̃r
d>P c1/10
 ∑

m≤N
d|m
 1 ≪ N P −c1/10τ (̃r) ≪ N/P c1/5,

where we used that ̃r ≤ P c0. If there exists a prime such that p | ̃r, p ∤ m, then

M(m) ≥ 1 − 21
25 − C ˜r−0.99 ≥ 1
7 ,

say, provided that N (and hence ˜r) is large. Then we obtain (30) as in the case of no
exceptional zeros (again, in a much stronger form). Since we are only considering m with
(m, ̃r) ≤ P c1/10, and since ˜r/2j is squarefree for some j ≤ 3, the other case that for all
p | ̃r we have p | m can only happen if
 ̃r ≤ 8P c1/10.(34)

By the inequality 1 − e−x ≥ min{1, x}/10, for P ≤ m ≤ N we get

M(m) ≥ 1
10 (1 − ̃β) log P − C ˜r−0.99.

By (31), we have

˜Ce
−˜c log N
log P E(m) ≤ ˜Ce
−˜cA(1 − ̃β) log P ≤ 1
100 (1 − ˜β) log P.

22 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

Putting everything together, by using (32), (34), and the classical (eﬀective) bound for
the distance of exceptional zeros from 1, we conclude that

M(m)(1 − ˜Ce
−˜c log D0
log P ) − ˜C(e
100
√log N P −c1 + e
−˜c log N
log P E(m))

≥ 1 − ˜β
20 log P − C(˜r−0.99 − P −c1/2)

≥ α
˜r1/2(log ˜r)2 − CP −c1/2

≥ α
100 P −c1/10

for some (eﬀective) α > 0, provided again that N (and hence P ) is large enough. Thus,

we get (30) outside an exceptional set of size O(N/P c1/5) = O(N 1− ε2c1
5A ). This concludes
the proof. □

Part III. Level of distribution estimates with power savings

6. Bombieri–Vinogradov range – Proof of Key Proposition 1

6.1. Reduction to exponential sums

Our task in this section is to prove Key Proposition 1. We shall in fact prove it in a
slightly more general form of Proposition 6.5 below, as this generalisation will be needed
for Theorem 1.2. We begin by reducing the problem to estimating exponential sums. This
reduction is also needed for the proof of Key Propositions 2 and 3.

Lemma 6.1. Let η > 0 and N ≥ 1. Let f, g : [1, N ] → C be functions. Suppose that we
have
 sup
α∈R
 ∣
∣
∣
∣
∣
∣
 ∑

n≤N f (n)e(αn)

∣
∣
∣
∣
∣
∣ ≤ ηN.(35)

Then, for all but ≪ η2/3N integers m ∈ [1, N ], we have

|f ∗ g(m)| ≤ η2/3N 1/2∥g∥2.

Proof. Let S ⊂ [1, N ] be the set of m ≤ N for which

|f ∗ g(m)| ≥ η2/3N 1/2∥g∥2

Pick unimodular complex numbers cm such that

cm(f ∗ g(m)) ≥ η2/3N 1/2∥g∥2

for m ∈ S.
Then, summing over m ≤ N and applying the orthogonality of characters, we obtain

η2/3N 1/2∥g∥2|S| ≤ ∑

n1,n2≤N f (n1)g(n2)cn1+n21S (n1 + n2)

= ∫ 1

0 F (α)G(α)S(−α) dα,

(36)
 THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 23

where
 F (α) := ∑

n≤N f (n)e(nα),

G(α) := ∑

n≤N g(n)e(nα),

S(α) := ∑

n≤N cn1S (n)e(nα).

Now, by the assumption (35), we can apply Cauchy–Schwarz and Parseval to (36) to
conclude that

η2/3N 1/2∥g∥2|S| ≪ ηN (∫ 1

0 |G(α)|
2 dα
)1/2 (∫ 1

0 |S(α)|
2 dα
)1/2

≪ ηN ∥g∥2|S|
1/2,

which implies
 |S| ≪ η2/3N,

as desired. □

Recall our notions of major and minor arcs from Deﬁnition 3.1. We also have a slight
variant of the previous lemma where we assume only major arc control on f , but require
additionally minor arc control on g; this will be needed in the proof of Key Proposition 2
later on.

Lemma 6.2. Let η > 0 and N ≥ 1. Let f, g : [1, N ] → C be functions. Suppose that we
have
 sup
α∈M
 ∣
∣
∣
∣
∣
∣
 ∑

n≤N f (n)e(αn)

∣
∣
∣
∣
∣
∣ ≤ ηN(37)

and
 sup
α∈m
 ∣
∣
∣
∣
∣
∣
 ∑

n≤N g(n)e(αn)

∣
∣
∣
∣
∣
∣ ≤ ηN.(38)

Then, for all but ≪ η2/3N integers m ∈ [1, N ], we have

|f ∗ g(m)| ≤ η2/3N 1/2(∥f ∥2 + ∥g∥2).

Proof. The proof is the same as that of Lemma 6.1, except that we split the integral arising
in that proof as
∫ 1

0 F (α)G(α)S(−α) dα = ∫

M F (α)G(α)S(−α) dα + ∫
m F (α)G(α)S(−α) dα

and estimate the ﬁrst term using (37) and the second using (38). □

To handle the major arc exponential sums, we shall apply the following lemma to reduce
matters to multiplicative characters.

24 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

Lemma 6.3. Let η > 0, N ≥ 1. Let f : [1, N ] → C be a function. Suppose that

max
1≤ℓ≤P c0 max
y≤N/ℓ
 ∣
∣
∣
∣
∣
∣
∑

n≤y f (ℓn)χ(n)

∣
∣
∣
∣
∣
∣ ≪ η exp(−√log P )P −3c0/2N(39)

uniformly for all Dirichlet characters χ of modulus ≤ P c0. Then we have

sup
α∈M
 ∣
∣
∣
∣
∣
∣
 ∑

n≤N f (n)e(αn)

∣
∣
∣
∣
∣
∣ ≪ ηN.(40)

Proof. By Deﬁnition 3.1, we can write α ∈ M as α = a/q + β with 1 ≤ a ≤ q ≤ P c0,
(a, q) = 1 and |β| ≤ P c0/N . By the fundamental theorem of calculus, we have

e(βn) = 1 + 2πiβ ∫ N

0 e(βy)1y≤n dy.(41)

Writing e(αn) = e(an/q)e(βn) and substituting this and (41) into (40), we see that it
suﬃces to prove
 max
y≤N
 ∣
∣
∣
∣
∣
∣
∑

n≤y f (n)e ( an
q
 )∣
∣
∣
∣
∣
∣ ≪ ηP −c0N

uniformly for 1 ≤ a ≤ q ≤ P c0 with (a, q) = 1. Writing ℓ = (n, q), we need

max
y≤N
 ∣
∣
∣
∣
∣
∣
∑

ℓ|q
 ∑

n′≤y/ℓ f (ℓn′)1(n′,q/ℓ)=1e ( an′

q/ℓ
 )∣
∣
∣
∣
∣
∣ ≪ ηP −c0N.(42)

We use the Fourier expansion

e ( an
q/ℓ
 ) = 1
ϕ(q/ℓ)
 ∑

χ (mod q/ℓ) τ ( ¯χ)χ(an)

for (n, q/ℓ) = 1, where τ (χ) is the Gauß sum. Applying the classical Gauß sum bound
|τ (χ)| ≤ (q/ℓ)1/2 for χ ̸= χ(q/ℓ)
0 and |τ (χ(q/ℓ)
0 )| ≤ 1 and the triangle inequality, (42) is

≪ ∑

ℓ|q
 ℓ1/2(log log q)
q1/2 max
ℓ|q max
y≤N/ℓ
 ∣
∣
∣
∣
∣
∣
∑

n≤y f (ℓn)χ(n)

∣
∣
∣
∣
∣
∣

for some character χ of modulus dividing q. We observe that

∑

ℓ|q
 ℓ1/2

q1/2 = ∑

u|q
 1
u1/2 = ∏

p|q
 (
1 + p−1/2 + p−1 + p−3/2 + · · · )

≪ exp
 

O
 


∑

p|q p−1/2







≪ exp(
√log q).

Appealing to (39) completes the proof. □

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 25

In the rest of this section, we shall prove a proposition (Proposition 6.5 below) that
contains Key Proposition 1, but involves a slight generalisation to weights other than the
von Mangoldt function, as that will be needed in the proof of Theorem 1.2.

Deﬁnition 6.4 (Weighted indicator of E3 numbers corresponding to Chen’s sieve). Denote
(similarly as in [20, eq. (6.2)])

B1 := {n = p1p2p3 : N 1/10 ≤ p1 < N 1/3−ε < p2 ≤ (N/p1)
1/2, p3 ≥ N 1/10}

B2 := {n = p1p2p3 : N 1/3−ε ≤ p1 ≤ p2 ≤ (N/p1)
1/2, p3 ≥ N 1/10}

and deﬁne normalised indicator functions for these sets as

ΛBi(n) :=
 {
log n, n = p1p2p3 ∈ Bi
0, otherwise,

and write
 ΛE∗
3 (n) = 1
2 ΛB1(n) + ΛB2(n)

The reason for considering ΛE∗
3 will become clear after Lemma 7.2 (a version of Chen’s
sieve inequality). Expanding out the deﬁnition of ΛE∗
3 (n) and applying the Siegel–Walﬁsz
theorem, for any character χ of modulus ≤ (log N )A we have
∑

n≤N ΛE∗
3 (n)χ(n) = cE∗
3 N 1χ=χ0 + OA(N/(log N )
A),(43)

where the implied constant is ineﬀective and cE∗
3 = 1
2 cB1 + cB2 with

cB1 := ∫

1/10≤t1≤1/3−ε≤t2≤(1−t1)/2
1−t1−t2≥1/10
 dt1 dt2
t1t2(1 − t1 − t2)

cB2 := ∫
1/3−ε≤t1≤t2≤(1−t1)/2
1−t1−t2≥1/10
 dt1 dt2
t1t2(1 − t1 − t2) .

In the rest of this section, let
 Λ
∗ ∈ {Λ, ΛE∗
3 }.

Proposition 6.5. Let k ≥ 1, a ̸= 0 and ε ∈ (0, 1/1000) be ﬁxed. Let N ≥ 3 and
(log N )C ≤ P ≤ N ε/10. Let
 f (n) := Λ
∗(n)ω1(n + a)ω2(n + a),

where ω1 is a sieve of range P , level D0 ≤ N ε/2 and order k and ω2 is an admissible main
sieve with parameters P, ε, k. Let g : [1, N ] → C be any function. Then, for all m ∈ [1, N ]
apart from ≪ N/P c1 exceptions, we have

f ∗ g(m) = V(ω2)fpre-sieve ∗ g(m) + O(∥g∥2N 1/2P −c1),

where
 fpre-sieve(n) := Λ
∗(n)ω1(n + a).

26 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

Note that for Λ∗ = Λ and a = 2, this implies Key Proposition 1 (after adjusting ε).
From Lemma 6.1, we see that Proposition 6.5 follows if we show that

sup
α∈R
 ∣
∣
∣
∣
∣
∣
 ∑

n≤N(f (n) − fpre-sieve(n))e(αn)

∣
∣
∣
∣
∣
∣ ≪ N P −3c1/2.(44)

We shall prove (44) by considering the case of minor and major arc α separately. Recall
the splitting
 [0, 1) = M ∪ m,

where the major and minor arcs are given by Deﬁnition 3.1.
By Lemma 6.3, it suﬃces to prove

sup
α∈m
 ∣
∣
∣
∣
∣
∣
 ∑

n≤N f (n)e(αn)

∣
∣
∣
∣
∣
∣ ≪ N P −3c1/2, sup
α∈m
 ∣
∣
∣
∣
∣
∣
 ∑

n≤N fpre-sieve(n)e(αn)

∣
∣
∣
∣
∣
∣ ≪ N P −3c1/2,(45)

and
 max
χ (mod q)
q≤P c0 max
1≤ℓ≤P c0 max
y≤N
 ∣
∣
∣
∣
∣
∣
∑

n≤y(f (ℓn) − fpre-sieve(ℓn))χ(n)

∣
∣
∣
∣
∣
∣ ≪ N P −3c0/2−2c1.(46)

6.2. Bombieri–Vinogradov with power saving

The large sieve allows us to estimate eﬃciently the correlation of a sequence with char-
acters of large conductor on average.

Lemma 6.6. Let Q ≥ P ≥ 2. Let αn be any sequence on (M, M + N ] with M, N ≥ 1.
Then ∑

q≤Q
 1
ϕ(q)
 ∑

ψ (mod q)
cond(ψ)>P
 ∣
∣
∣ ∑

M <n≤M +N αnψ(n)
∣
∣
∣2 ≪ (Q + N/P )(log Q) ∑

M <n≤M +N |αn|
2.

Proof. Writing q = rs with ψ = ψ1ψ2, where ψ1 (mod r) is primitive and ψ2 (mod s) is
principal, we can bound the sum in question with the large sieve inequality for multiplica-
tive characters (see [15, (7.31)]) by
∑

s≤Q
 1
ϕ(s)
 ∑

P ≤r≤Q
 1
ϕ(r)
 ∑

ψ1(r)∗
∣
∣
∣ ∑

n≤N αn1(n,s)=1ψ1(n)
∣
∣
∣2 ≪ (Q + N/P )(log Q) ∑

M <n≤M +N |αn|
2

as stated. □

The Bombieri–Vinogradov theorem states that the approximation
∑

n≤N
n≡a(d)
 Λ(n) ≈ 1
ϕ(d)
 ∑

n≤N Λ(n)(47)

is valid on average for d up to almost N 1/2 with a saving over the trivial bound of type
(log N )−A. This saving comes from the application of the Siegel–Walﬁsz theorem for small
conductor characters and the large sieve for large conductor characters. The term on the
right-hand side of (47) is the contribution of the principal character modulo d, i.e. the
unique character (mod d) that has conductor 1. If we instead include the contribution of

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 27

all the characters with conductor up to a value of P = (log N )Ω(1), we can hope to get a
better error term than (log N )A with the help of Lemma 6.6.
This idea was applied by Drappeau, and following the notation of [5, eq. (5.1)] we write

uP (n; q) := 1
ϕ(q)
 ∑

ψ(q)
cond(ψ)>P
 ψ(n)(48)
 = 1n≡1(q) − 1
ϕ(q)
 ∑

ψ(q)
cond(ψ)≤P
 ψ(n),

With this we can state the following type I and II estimate (see also [5, Lemma 5.2]).

Lemma 6.7 (Simple type I/II estimate). Let C ≥ 1 be ﬁxed. Let N1, N2, y ≥ 1 with
N1N2 ≍ y and let 2 ≤ P ≤ Q ≤ y1/2. Then for any character χ with modulus at most P
we have

∑

q≤Q
 ∑

n1≤N1 τ (n1)
C max
(a,q)=1
y0≥1
 ∣
∣
∣
∣
∣
∣
 ∑

y0≤n2≤y/n1 χ(n2)uP (n1n2a, q)

∣
∣
∣
∣
∣
∣ ≪C N1Q3/2P 1/2(log y)
OC (1).(49)

Let further αn, βn be coeﬃcient sequences of order C, supported on [1, N1] and [1, N2],
respectively. Then it holds that

∑

q≤Q max
(a,q)=1
 ∣
∣
∣
∣
∣
 ∑

n1,n2 αn1βn2uP (n1n2a; q)

∣
∣
∣
∣
∣ ≪C y1/2(Q + y1/2/P + N 1/2
1 + N 1/2
2 )(log y)
OC (1).

(50)

Proof. We have
∑

y0≤n2≤y/n1 χ(n2)uP (n1n2a, q) = 1
ϕ(q)
 ∑

ψ(q)
cond(ψ)>P
 ψ(n1a) ∑

y0≤n2≤y/n1 χψ(n2)

Since χ has modulus at most P , the character χψ (of modulus ≤ P Q) is never prin-
cipal. Applying the P´olya–Vinogradov inequality and trivially bounding the number of
ψ(q), cond(ψ) > P by ϕ(q) proves (49).
The bound (50) follows in a straightforward manner from the Cauchy–Schwarz inequal-
ity and Lemma 6.6. □

As a consequence, we get the following version of the Bombieri–Vinogradov theorem
with an additional character twist and improved error term.

Lemma 6.8 (Bombieri–Vinogradov with large savings). Let χ be any character of modulus
at most P , with 1 ≤ P ≤ Q ≤ N 1/2/P . Then for any y ≤ N we have

∑

q≤Q max
a(q)∗
 ∣
∣
∣
∣
∣
∣
∑

n≤y Λ
∗(n)χ(n)uP (na; q)

∣
∣
∣
∣
∣
∣ ≪ N P −1/4(log N )
O(1).

Proof. We can assume that y ≥ N/P 3, since otherwise a trivial triangle inequality estimate
suﬃces. Applying Vaughan’s identity in the case Λ∗ = Λ (or in the case Λ∗ = ΛE∗
3 the

28 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

fact that each n in the support of ΛE∗
3 has a prime factor in [N 1/4, N 1/2]), it suﬃces to
prove that

∑

d≤Q
(d,a)=1
 max
a(q)∗
 ∣
∣
∣
∣
∣
∣
∣
∣
 ∑

n1n2≤y
n1∼N1,
 an1χ(n1)bn2χ(n2)uP (n1n2a; q)

∣
∣
∣
∣
∣
∣
∣
∣
 ≪ N P −1/4(log N )
O(1),(51)

whenever either of the following holds:
(1) N1 ≤ P 3/2, |an| ≤ τ (n) and bn ≡ 1 or bn ≡ log n (Type I case);
(2) N1 ∈ [P 3/2, y/P 3/2] and |an|, |bn| ≤ τ (n) log n (Type II case).
In the type I case, we may pull the sum over n1 outside with the triangle inequality and
apply Lemma 6.7, obtaining for (51) a bound of

≪ P 3/2Q3/2P 1/2(log y)
O(1) ≪ P 1/2N 3/4(log y)
O(1) ≪ N P −1/4(log y)
O(1).

In the type II case, we ﬁrst split the n1 and n2 variables in (51) into short intervals of
logarithmic length P −1/4, reducing matters to bounding

∑

N ′
1,N ′
2∈[P 3/2,y/P 3/2]
N ′
1N ′
2≤y(1+P −1/4)2

N ′
i =(1+P −1/4)ji for some ji∈N
 ∑

d≤Q max
a(d)∗
 ∣
∣
∣
∣
∣
 ∑

n1n2≤N
n1∼N1
N ′
1≤n1≤N ′
1(1+P −1/4)
N ′≤n≤N ′(1+P −1/4)
 an1χ(n1)bn2χ(n2)uP (n1n2a; q)

∣
∣
∣
∣
∣.

(52)

The contribution of y/(1 + P −1/4)2 ≤ N ′
1N ′
2 ≤ N (1 + P −1/4)2 is trivially admissible by
the triangle inequality. This allows us to delete the cross condition n1n2 ≤ y and the
estimate (52) follows from applying (50) of the previous lemma to the ≪ P 1/2(log P )2

many short sums. □

6.3. Minor arc contribution

Our task in this subsection is to prove (45). Recall that in the statement of Propo-
sition 6.5 we have f (n) = Λ∗(n)ω1(n + a)ω2(n + a), where Λ∗ ∈ {Λ, ΛE∗
3 }. Write
ωi(n) = ∑d|n λi(d) with |λi(d)| ≤ τk(d). Then the two exponential sums in (45) that
we need to bound become
∑

d1≤D0 λ1(d1) ∑

d2≤N 1/2−ε λ2(d2) ∑

n≤N
n≡−a (mod d1d2)
 Λ
∗(n)e(nα),

V(ω2) ∑

d1≤D0 λ1(d) ∑

n≤N
n≡−a (mod d1)
 Λ
∗(n)e(nα).

By the assumption on ω2, we may write

λ1 ⋆ λ2 = ∑

j≤C log N(λ1 ⋆ αj) ⋆ λ′
j := ∑

j≤C log N γj ⋆ λ′
j,

where |γj(d)| ≤ τk+1(d), |λ′
j(d)| ≤ τk(d), γj is supported on [N tj , N tj +ε/2] for some 0 ≤
tj ≤ 1/3 − ε, and λ′
j is well-factorable of level N 1/2−tj −ε. Therefore, to conclude the minor
arc analysis and show (45), it suﬃces to prove the following result (recall c1 = c0/100).

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 29

Lemma 6.9 (Bombieri–Vinogradov with minor arc twist and partially well-factorable
weights). Let ε ∈ (0, 1/100) and k ≥ 1 and a ∈ Z \ {0} be ﬁxed. Let (log N )C ≤ P ≤ N ε/10

with C large enough in terms of k. Let ξ1, ξ2 satisfy |ξi(d)| ≤ τk(d) and suppose that
ξ1 is supported on [1, D1] for some D1 ≤ N 1/3−ε/2 and that ξ2 is well-factorable of level
N 1/2−ε/D1. Then, we have

sup
α∈m
 ∣
∣
∣
∣
∣
∣
∣
∣

∑

d1 ξ1(d1) ∑

d2
(d1d2,a)=1
 ξ2(d2) ∑

n≤N
n≡a (mod d1d2)
 Λ
∗(n)e(nα)

∣
∣
∣
∣
∣
∣
∣
∣
 ≪ N P −c0/20.(53)

Proof. By the Cauchy–Schwarz inequality, standard moment estimates for the divisor
functions, and the fact that P ≥ (log N )C for C large enough, it suﬃces to prove (53)
in the case |ξi(d)| ≤ 1, with the stronger bound N P −c0/9 on the right-hand side. Note
also that the logarithmic weight in the deﬁnition of Λ∗ can be disposed of with partial
summation, replacing the summation over n ≤ N in (53) with summation over n ≤ N ′ for
some N ′ ≤ N . We may assume that N ′ ≥ N 1−ε/10, as otherwise the claim follows from
the Brun–Titchmarsh inequality.
After these reductions, the result follows from work of Matom¨aki [18] and is proved in
detail in [20]. See [20, Lemmas 8.3, 8.4, 8.6]. The considerations there give a saving of
P −c0/8(log N )C ≪ P −c0/9. Observe that the weight that we call ξ1 is in [20] assumed to
be supported on primes only (as we could also assume), but this is not required in the
proof. □

6.4. Major arc contribution

We shall now complete the proof of Proposition 6.5 (and so also that of Key Proposi-
tion 1) by showing (46). Let λ(d) := λ1 ⋆ (λ2 − V(ω2)I), where I(d) := 1d=1. Note that
for 2 ≤ ℓ ≤ P c0 we have Λ∗
E3(ℓn) = 0, and Λ(ℓn) = 0 unless n is of the form pj with j ≥ 2
and p | ℓ. Therefore, our task is to prove

∣
∣
∣
∣
∣
∣
∣
∣
 ∑

(d,a)=1 λ(d) ∑

n≤y
n≡−a (mod d)
 Λ
∗(n)χ(n)

∣
∣
∣
∣
∣
∣
∣
∣
 ≪ N P −3c0/2−2c1

uniformly for y ≤ N and characters χ of modulus ≤ P c0.
Since the two sieve weights λ1 and λ2 are supported only on integers consisting of primes
≤ P and > P , respectively, the sum that we are considering can be rewritten as

∑

(d,a)=1 λ1 ⋆ λ2(d) ∑

n≤y Λ
∗(n)χ(n) (1n≡−a(d) − 1n≡−a(d≤P )
ϕ(d>P )
 ) .

30 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

To make Lemma 6.8 applicable, we rewrite for any d with (d, a) = 1 (denoting by χ(d>P )
0
the principal character (mod d>P ) and by ¯a the inverse of a modulo d)

1n≡−a (mod d) − 1n≡−a (mod d≤P )
ϕ(d>P )

= 1
ϕ(d)
 ∑

ψ1(d) ψ1(−an) − 1
ϕ(d)
 ∑

ψ2(d≤P ) ψ2(−an)χ(d>P )
0 (−an) − 1(n,d>P )̸=11n≡−a (mod d≤P )
ϕ(d>P )

= 1
ϕ(d)
 ∑

ψ(d)
cond(ψ)>P
 ψ(−an) + O( 1(n,d>P )̸=1
ϕ(d>P )
 )

= uP (−an; d) + O( 1(n,d>P )̸=1
ϕ(d>P )
 )
.

The contribution of terms with (n, d>P ) ̸= 1 can be estimated trivially with the Brun–
Titchmarsh inequality (noting that (n, d>P ) ̸= 1 implies the existence of a prime p > P
such that p | n, p | d). Therefore, after an application of the triangle inequality, we have
reduced matters to showing
∣
∣
∣
∣
∣
∣
 ∑

(d,a)=1 λ1 ⋆ λ2(d) ∑

n≤y Λ
∗(n)χ(n)uP (−an; d)

∣
∣
∣
∣
∣
∣ ≪ N P −3c0−2c1.

We can remove the weights λ1 ⋆ λ2(d) with the Cauchy–Schwarz inequality; we thus
reduce to proving
 ∑

d≤N 1/2−ε
(d,a)=1
 ∣
∣
∣
∣
∣
∣
∑

n≤y Λ
∗(n)χ(n)uP (−an; d)

∣
∣
∣
∣
∣
∣ ≪ N P −4(c0+c1),(54)

say. As the d summation goes up to N 1/2−ε, (54) follows from Lemma 6.8. This completes
the proof of (46) and therefore also that of Proposition 6.5 and Key Proposition 1.

7. The case of two Chen primes – Proof of Theorem 1.2

We shall next prove Theorem 1.3. In addition to Proposition 6.5, we will need the
following lemma that allows us to replace Λ and ΛE∗
3 by pre-sieves in the range of saving
of Theorem 1.3.

Lemma 7.1. Let ε > 0 be ﬁxed, and let B ≥ A ≥ 1 be large but ﬁxed. Let N ≥ 2
and let (log N )A2 ≤ P ≤ (log N )B. Let ω+ be the upper bound admissible pre-sieve with
parameters P, N ε as in Deﬁnition 4.6. Then we have

sup
α∈R
 ∣
∣
∣
∣
∣
∣
 ∑

n≤N(Λ(n) − V (P )
−1ω+(n))ω+(n + 2)e(αn)

∣
∣
∣
∣
∣
∣ ≪ N/(log N )
A(55)

and
 sup
α∈R
 ∣
∣
∣
∣
∣
∣
 ∑

2<n≤N(ΛE∗
3 (n) − cE∗
3 V (P )
−1ω+(n))ω+(n − 2)e(αn)

∣
∣
∣
∣
∣
∣ ≪ N/(log N )
A.(56)

Here the implied constants are ineﬀective.

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 31

Proof. Let Λ∗ ∈ {Λ, ΛE∗
3 }, and let c∗ = 1 if Λ∗ = Λ and c∗ = cE∗
3 if Λ∗ = ΛE3.
In the case α ∈ m, for a ∈ {−2, 2} we have

sup
α∈m
 ∣
∣
∣
∣
∣
∣
 ∑

2<n≤N Λ
∗(n)ω+(n + a)e(αn)

∣
∣
∣
∣
∣
∣ ≪ N/(log N )
A

by Lemma 6.9, since ω+(n + a) = ∑d|n+a,d≤N ε λd with |λd| ≪ 1. Similarly, by slight
modiﬁcation of [20, Lemma 8.3], we have

sup
α∈m
 ∣
∣
∣
∣
∣
∣
 ∑

2<n≤N ω+(n)ω+(n + a)e(αn)

∣
∣
∣
∣
∣
∣ ≪ N/(log N )
A

In the case α ∈ M, by Lemma 6.3, it suﬃces to prove
∣
∣
∣
∣
∣
∣
 ∑

2<n≤y(Λ
∗(ℓn) − V (P )
−1ω+(ℓn))ω+(ℓn + a)χ(n)

∣
∣
∣
∣
∣
∣ ≪ N/(log N )
A

uniformly for 1 ≤ ℓ ≤ P c0, y ≤ N/ℓ, a ∈ {−2, 2} and characters χ of modulus ≤ P c0.
We will reduce to the case ℓ = 1. Observe that for 1 < ℓ ≤ P c0, we trivially have
∑

2<n≤N Λ
∗(ℓn) ≪ N 1/2(log N ),

and by H¨older’s inequality and the estimate ω+(n) ≤ τ (n) we have

∑

2<n≤N ω+(ℓn)ω+(ℓn + a) ≤
 

 ∑

n≤N ω+(ℓn)





1/2 

 ∑

n≤N τ (ℓn)
4




1/4 

 ∑

2<n≤N τ (ℓn + a)
4




1/4
 .

The second and third sum on the right are ≪ N (log N )O(1) by Shiu’s bound [27, Theorem
1]. The ﬁrst sum in turn is by the fundamental lemma

∑

d≤D λd ℓN
[d, ℓ] + O(D) = N ∏

p≤P
 (1 − ℓ
[ℓ, p]
 ) + O(N e
−(log D)/(log P ) + D) ≪ N e
−(log N )/(log log N )2 ,

say. Hence, we may assume that ℓ = 1.
Now if χ is non-principal of modulus q ≤ P c0, the Siegel–Walﬁsz theorem and (43) give
∣
∣
∣
∣
∣
∣
 ∑

2<n≤y Λ
∗(n)χ(n)

∣
∣
∣
∣
∣
∣ ≪ N/(log N )
A.

Moreover, we have

∣
∣
∣
∣
∣
∣
 ∑

2<n≤y ω+(n)ω+(n + a)χ(n)

∣
∣
∣
∣
∣
∣ ≤ ∑

d1,d2≤N ε
(d1,q)=1
 ∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 ∑

2<n≤y
n≡0 (mod d1)
n≡−a (mod d2)
 χ(n)

∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
∣
 ,(57)

32 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

and the inner sum is ≪ qd1d2, since for any u ≥ 1, v coprime to q we have
∣
∣
∣
∣
∣
∣
∑

n≤y χ(un + v)

∣
∣
∣
∣
∣
∣ =
 ∣
∣
∣
∣
∣
∣
 1
ϕ(u)
 ∑

ψ(u) ψ(−v) ∑

n≤uy+v χψ(n)

∣
∣
∣
∣
∣
∣ ≤ qu.

Therefore, (57) is small enough.
Finally, assume that χ = χ0 is principal. By the prime number theorem, (43) and the
fundamental lemma, we have
∑

2<n≤y Λ
∗(n)ω+(n + a)χ0(n) = ∑

d≤N ε λdc
∗ y
ϕ(d) + O(N/(log N )
A) = c
∗V (P )y + O(N/(log N )
A).

On the other hand, the fundamental lemma also gives
∑

2<n≤y ω+(n)ω+(n + a)χ0(n) = (1 + O((log N )
−A))V (P )
2y,

and combining these we obtain the claim. □

We shall lastly need a well-known sieve inequality that is a simpliﬁed version of Chen’s
sieve.

Lemma 7.2 (Chen’s sieve). Let Λ2(n) = Λ(n)1P2(n + 2)ρ(n + 2, N 1/15) as before. Let
ε > 0 be a small enough ﬁxed number. Let P ≤ e
√log N and D0 = N ε2. Then there exist
admissible main sieves ω+
M, ω−
M with parameters P, ε, 2, and an admissible pre-sieve ω+

with parameters P, D0 such that

• Λ2(n) ≥ Λ(n)ω+(n + 2)ω−
M(n + 2) − ω+(n)ω+
M(n)ΛE∗
3 (n + 2) + O(E(n))
with ∑n≤N |E(n)| ≪ N e−√log N ,
• V(ω−
M) − cE∗
3 V(ω+
M) ≫ V (P, N ).

Proof. Without the pre-sieves, this follows directly from the construction in [20, Appendix
A]. By restricting the sieves constructed there to primes larger than P we can incorporate
an upper bound pre-sieve into the second summand in a straightforward manner.
In the ﬁrst summand this is done similarly as in the proof of Theorem 1.1 by the
vector sieve inequality, Lemma 5.6, with A−, A+ being lower and upper bound pre-sieves
with parameters P, D0. In contrast to the proof of Theorem 1.1, we can now bound the
contribution of the A− − A+ term in a straightforward manner and include it in the sieve
error term. Indeed, the fundamental lemma and the estimate |ω−
M(n)| ≪ eO((log N )/(log P ))

give us ∣
∣ ∑

n≤N Λ(n)(ω+(n + 2) − ω−(n + 2))ω−
M(n + 2)
∣
∣

≪ (log N )e
O( log N
log P ) ∑

n≤N(ω+(n + 2) − ω−(n + 2))

≪ (log N )e
O( log N
log P ) exp ( − 1
10 log D0
log P log log D0
log P
 )N

≪ N e
−√log N .

This, and the related term with ΛE∗
3 , can be absorbed in the function E(n). □

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 33

Remark 7.3. We would not need to choose β = 750 in the deﬁnition of admissible pre-
sieves for this proposition to hold, as the relatively small choice of P makes the fundamental
lemma saving much stronger. We keep β = 750 only to not increase the number of
employed sieves even further.

We are now ready to prove Theorem 1.2.

Proof of Theorem 1.2. We allow constants in this proof to be ineﬀective.
Set P = (log N )A2. For brevity, for any function f denote f ′(n) := f (n + 2). Recall
that we want to obtain an exceptional set of size O(N (log N )−A), with the constant being
ineﬀective. By Lemma 7.2, we can now estimate

Λ2 ∗ Λ2(m) ≥ (Λω+′ω−
M′ − ω+ω+
MΛ
′
E∗
3 ) ∗ Λ2(m) + O ( N
(log N )A
 ) .

By Proposition 6.5, we can reduce to pre-sieves with parameters P, N ε, and we have
outside a suﬃciently small exceptional set

(Λω+′ω−
M′ − ω+ω+
MΛ
′
E∗
3 ) ∗ Λ2(m) = (Λω+′V(ω−
M) − ω+Λ
′
E∗
3 V(ω+
M)) ∗ Λ2(m) + O ( N
(log N )A
 ) .

We can further simplify by applying Lemmas 7.1 and 6.1 to get outside the exceptional
set that
 (Λω+′V(ω−
M) − ω+Λ
′
E∗
3 V(ω+
M)) ∗ Λ2(m)

= V (P )
−1(V(ω−
M) − cE∗
3 V(ω+
M))ω+ω+′ ∗ Λ2(m) + O ( N
(log N )A
 )

Here ω+(n)ω+(n + 2) consists of two upper bound sieves and so is nonnegative. So we
can lower bound the remaining Λ2 in the same way and get outside of a suﬃciently small
exceptional set

V (P )
−1(V(ω−
M) − cE∗
3 V(ω+
M))ω+ω+′ ∗ Λ2(m)(58)
 ≥ V (P )
−2(V(ω−
M) − cE∗
3 V(ω+
M))
2ω+ω+′ ∗ ω+ω+′(m) + O ( N
(log N )A
 ) .

By the second statement of Lemma 7.2 and Mertens’s theorem, we have V(ω−
M) −
cE∗
3 V(ω+
M) ≫ V (P, N ) ≍ (log P )/(log N ). Moreover, also by Mertens’s theorem we have
V (P )−2 ≍ (log P )2.
By a simple calculation (that is a simpler case of our considerations in Section 10.2)
and the fundamental lemma, one sees for all m ≤ N that

ω+ω+′ ∗ ω+ω+′(m) ≫ V (P )
4S(m)m + O ( N
(log N )A
 ) .

As S(m) ≫ 1 for m ≡ 4 (mod 6), combining this with (58) completes the proof. □

8. Beyond the 1/2 barrier – Proof of Key Proposition 2

8.1. Setup

In this section we prove Key Proposition 2 which states that we can replace the main
sieve component of a Fouvry–Grupp sieve by a constant on the major arcs. To do this,
we extend the results of Bombieri–Friedlander–Iwaniec [1] and Maynard [21] to produce
quantitatively stronger savings by including the contribution of small conductor characters

34 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

in the main term, in the spirit of Lemma 6.8. The proof strategy for these results is to use
the dispersion method to translate the problem into sums of Kloosterman sums. Those
then can be handled in an eﬃcient manner by appealing to the work of Deshouillers–
Iwaniec [4] on the spectral theory of automorphic forms. A similar power-saving result was
obtained by Drappeau in [5] in one special case of the dispersion method. We generalise
his strategy to handle most of the arithmetic information in [1] and [21]. While our
application to a Fouvry–Grupp sieve as in Deﬁnition 4.3 is somewhat special and motivated
by Theorem 1.1, we in particular also obtain all cases that are required for the important
4/7 and 3/5 results of [1] and [21]. Thus, as a side product we also obtain Theorem 1.3.
We make extensive use of the uP notation from (48) and note the trivial bound (see
also [5, eq. (5.2)])
 |uP (n; q)| ≪ 1n≡1(q) + P τ (q)
q ,(59)

which comes from the fact that q has ≤ τ (q) divisors ≤ P and to each such modulus there
are ≤ P characters.
We start by reducing Key Proposition 2 to the following result that involves the dis-
tribution of primes to moduli beyond the 1/2 barrier with certain factorability properties
and a character twist.

Proposition 8.1 (Power-saving level of distribution estimates beyond the 1/2 barrier).
Let a ∈ Z \ {0} and C ≥ 1 be ﬁxed. Let ǫ > 0 be small and ǫ′ > 0 suﬃciently small in
terms of ǫ. Let ξ1, ξ2 satisfy
• ξ1 is well-factorable of level S1 and order C, ξ2 is supported in [1, S2], and |ξi(d)| ≤
τ (d)C for i ∈ {1, 2};
• One of the following holds:
(i) S2 ≤ S1, S1S2 ≤ N 4/7−ǫ.
(ii) ξ2(d) = Λ(d), S1S2 ≤ N 11/20−ǫ, S2 ≤ N 1/3−ǫ.

Then for 1 ≤ P ≤ N ǫ′ and uniformly for primitive characters χ of modulus ≤ P , we have
∑

d1≥1
 ∑

d2≥1
(d1d2,a)=1
 ξ1(d1)ξ2(d2) ∑

n≤N Λ(n)χ(n)uP (an; d1d2) ≪ N (log N )
OC (1)P −1/200.

Proof of Key Proposition 2 assuming Proposition 8.1. By Lemma 6.2, Lemma 6.3, and
Lemma 6.9 (which is used to bound the Fourier transform of g), it suﬃces to show that

max
χ (mod q)
q≤P c0 max
1≤ℓ≤P c0 max
y≤N
 ∣
∣
∣
∣
∣
∣
∑

n≤y(f (ℓn) − fpre-sieve(ℓn))χ(n)

∣
∣
∣
∣
∣
∣ ≪ N P −3c0/2−2c1.

Now, arguing as in Subsection 6.4, it suﬃces to show, uniformly for characters χ of
modulus ≤ P and N/P < y ≤ N , that
∣
∣
∣
∣
∣
∣

∑

d λ1 ⋆ λ2(d) ∑

n≤y Λ(n)χ(n)uP (−an; d)

∣
∣
∣
∣
∣
∣ ≪ N P −3c0/2−2c1,(60)

where λ1, λ2 are the pre-sieve and main sieve weights, respectively. The Fouvry–Grupp
main sieve λ2 is of the shape required for an application of Proposition 8.1, after replacing
the prime indicator function by the von Mangoldt function, using summation by parts.

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 35

The pre-sieve can be absorbed into ξ1. Furthermore, after introducing an admissible error,
we can assume that χ is primitive. □

Our deﬁnition of a Fouvry–Grupp sieve (see Deﬁnition 4.3) and the related level of
distribution estimate of Proposition 8.1 are motivated by the result of Fouvry–Grupp [7]
that shows that the primes obey suitable level of distribution estimates to be combined
with such sieves. As in their [7, Lemma 4] we deduce Proposition 8.1 from a general
estimate on the distribution of bilinear forms in arithmetic progressions. To be more in
line with usual notation, we change the notation for the remainder of this section and
denote by X the summation range that is called N (or the related y) in all other sections
of the paper. We deﬁne the general bilinear sum we are considering as

D := ∑

q∼Q
 ∑

r∼R
(qr,a)=1
 γqδr ∑

m∼M
n∼N
 αmβnuP (mna; qr).(61)

Throughout this section we often use the following assumptions and notation.

Convention 3. Let ǫ > 0 be suﬃciently small in absolute terms and ǫ′ > 0 be suﬃciently
small in terms of ǫ (Given ǫ, the largest admissible choice of ǫ′ is not the same in every
lemma). Fix a ∈ Z \ {0} and C ≥ 1. Let X ≍ M N with

M, N ≥ X ǫ,(62)

and let Q, R be given with
 QR ≤ X 1−ǫ(63)

Let αm, βn, γq, δr be coeﬃcient sequences of order C, supported respectively on m ∼ M, n ∼
N, q ∼ Q, r ∼ R. Let f0 be a nonnegative smooth function supported on [1/2, 5/2] which
is identically equal to 1 on [1, 2].

With this we can state the following result about the distribution of bilinear forms in
arithmetic progression to large moduli, considerably extending the permissible level over
Lemma 6.7.

Proposition 8.2 (Distribution of bilinear sums). Assume Convention 3 and let

D = ∑

q∼Q
 ∑

r∼R
(qr,a)=1
 γqδr ∑

m∼M
n∼N
 αmβnuP (mna; qr)

as in (61). Assume further that one of the following holds:

(T.1) QR ≤ X 1/2−ǫ.
(T.2) γ = γ ′ ⋆ γ ′′, with γ ′, γ ′′ supported respectively on [Q1, 2Q1] and [Q2, 2Q2] (so Q ≍
Q1Q2) with
X ǫR ≤ N ≤ X −ǫ min{X 1/2Q−1/2
1 Q−1
2 , X 2Q−5
1 Q−2
2 R−1, XQ−2
1 Q−3/2
2 R−1/2}.
(T.3) X ǫR ≤ N ≤ X −ǫ min{X 1/2Q−1R1/2, X 2/5Q−2/5, X 1/2Q−3/4}.
(T.4) αm = χ(m)1m∈I for some primitive character χ of modulus ≤ P and some interval
I ⊂ [M, 2M ] and X 1−ǫ ≥ M ≥ X ǫ max{Q, X −1QR4, Q1/2R, X −2Q3R4}.
(T.5) γq = 1q∈I for some interval I ⊂ [Q, 2Q] and X ǫR ≤ N ≤ X 1/3−ǫR−1/3.

Then for any P ≤ X ǫ′, we have

D ≪ X(log X)
OC (1)P −1/7

36 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

The case (T.1) follows immediately from Lemma 6.8 and the Cauchy–Schwarz inequality.
Roughly speaking, (T.2) is a consequence of Lemma 8.1 of Maynard [21], (T.3) is related to
Theorem 2 of Bombieri–Friedlander–Iwaniec [1], and (T.5) is a combination of [1, Theorem
6] with Drappeau’s estimate for sums of Kloosterman sums in arithmetic progressions ([5,
Theorem 2.1]).

Remark 8.3. Throughout this section we optimise neither the dependence of ǫ′ on ǫ nor
the exponent of P . With slightly more eﬀort, along the lines of [5] it should be possible to
improve the estimate in Proposition 8.2 to X(log X)OC (1)P −1.

Remark 8.4. We are missing the cases (S.2) and (S.5) from the set of seven bilinear
estimates in [7, Lemma 4], but we compensate for this by having a stronger case (T.2).
Both of the missing cases, (S.2) and (S.5), originate from work of Fouvry [6]. Fouvry
restricts the coeﬃcients βn to be supported only on n with not too many prime divisors
to introduce certain coprimality conditions, see [6, Lemme 7]. We were unable to get a
power saving with this strategy. While the alternative proof of [7, Lemma 4, (S.2)] given
in [1, Section 10] does not use Fouvry’s coprimality approach and looks like it could give a
power saving, there seems to be an issue at the bottom of [1, p. 231]. To see this, consider
there the case a = h1 = h2 = q0 = q1 = q2 = 1, n1 = 6, n2 = 5, n3 = 3, n4 = 10, so
δ1 = 2, δ2 = 1. Then the ﬁrst expression for the terms in the exponential in the proof
of [1, Lemma 8] is n2
n1 − n4
n3 = −1
6 − 1
3 = − 1
2 ,

whereas the second expression is
( n3n4
δ1δ2 − n1n2
δ1δ2
 ) n2n4/δ1δ2
n1n3 = ( 30
2 − 30
2
 ) n2n4/δ1δ2
n1n3 = 0.

The authors thank James Maynard for making them aware of this issue.

8.2. Combinatorial dissection

We now apply a combinatorial dissection to (both of the) von Mangoldt functions in
the statement of Proposition 8.1 to reduce it to suitable bilinear sum estimates.

Proof of Proposition 8.1, assuming Proposition 8.2. The proofs of the cases (i) and (ii)
are based on the proofs of [1, Theorem 10] and [7, Theorem 2].
We start with Heath-Brown’s identity

Λ(n) = − ∑

1≤j≤J(−1)
j(J
j
 ) ∑

n=n1···n2j
ni≥X 1/J =⇒ i≤j
(log n1)µ(nj+1) · · · µ(n2j)

with J = 7. Observe that the additional character χ in the statement of Proposition 8.1
carries through Heath-Brown’s identity via multiplicativity and can be absorbed in the
sequences α and β unless we are in case (T.4).
We split each of the variables ni in Heath-Brown’s identity to ranges of the form Ni <
ni ≤ (1 + ∆)Ni with ∆ = P −1/200. We get the trivial estimate

∆X(log X)
OC (1)

for the ranges not covered precisely and the bound

∆−14X(log X)
OC (1)P −1/7

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 37

for the remaining ranges, provided that they ﬁt into one of the cases of Proposition 8.2.
Recalling that ∆ = P −1/200, we get a good enough error term.
Let us ﬁrst consider the case (i), that is S2 ≤ S1, S1S2 ≤ N 4/7−ǫ. In that case the
combined weight ξ1 ∗ ξ2 is well-factorable (see [7, Lemma 5]) and so is dealt with, without
a power saving error term, in [1, Section 10]. The proof there is based on an application
of [1, Theorem 1], [1, Theorem 2], and [1, Theorem 5*]. We can replace these three by
(T.2) (with Q2 = 1), (T.3), and (T.4) respectively to get the desired improved error term.
To handle the remaining case (ii), we follow the ideas of Fouvry–Grupp [7, Section III.]
and in particular apply the same combinatorial decomposition as described in [7, Section
III.1]. Write Si = X θi and recall that we are in the case θ1 + θ2 ≤ 11/20 − ǫ, θ2 ≤ 1/3 − ǫ,
and θ2 ≥ θ1 (as otherwise we can apply (i)), and the weight ξ1 is well-factorable. We
deﬁne the intervals
 I1 := [0, 2ǫ]

I2 := (2ǫ, θ1 + 2ǫ]

I3 := (θ1 + 2ǫ, θ2 + 2ǫ]

I4 := (θ2 + 2ǫ, 3/7]

I5 := (3/7, 1].

This diﬀers from the intervals given in [7, Section III.3] only in that we are combining
their J2 and J3. Let Ni = X νi in our splitting of ni into intervals (Ni, (1 + ∆)Ni]. Let ν
denote any nonempty subsum of the νi.
If there is a ν ∈ I4, we apply (T.2) with

M = X 1−ν

N = X ν

Q1 ≤ X θ1+θ2−ν+2ǫ

Q2 = 1

R ≤ X ν−2ǫ.

This is essentially the same as in [7, Section III.3].
Assume now that there is a ν ∈ I2. We start by using the factorability of ξ1 and want
to apply (T.2) with
 M = X 1−ν

N = X ν

Q1 = X θ1−ν+2ǫ

Q2 = X θ2

R = X ν−2ǫ.

The second and third statements in the minimum clearly make no problem, as

ν − 2ǫ + ǫ ≤ ν ≤ ǫ + min{2 − 5θ1 − 2θ2 + 4ν − 8ǫ, 1 − 2θ1 − (3/2)θ2 + (3/2)ν − 3ǫ},

the worst case here being ν = 2ǫ, θ1 = θ2 = 11/40. Thus, we can apply (T.2) as long as

ν + 2θ2 + θ1 ≤ 1 − ǫ.(64)

38 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

If (64) is not fulﬁlled, we apply (T.3) with

M = X 1−ν

N = X ν

Q ≤ X 11/20−ν+2ǫ

R ≤ X ν−2ǫ.

The second and third condition are again easily seen to be fulﬁlled, the worst case being
θ1 = θ2 = 11/20, and for example we have ν ≤ 2/5(1 − 11/20 + ν) as 33/200 ≤ 9/50. In
order to check the condition
 N ≤ X 1/2Q−1R1/2,(65)

we take advantage of the fact that (64) can be assumed to be false. Recalling θ2 < 1/3,
we can assume
 θ1 + θ2 + ν > 2/3 − ǫ.

As QR = X θ1+θ2 this means that

X 1/2Q−1R1/2 ≥ X 5/6−(1/2)δ Q−3/2N −1/2.

So (65) follows from
 N 3/2Q3/2 ≤ X 5/6−(1/2)ǫ

which holds for small enough ǫ as 33/40 < 5/6.
In the next step, Fouvry and Grupp decompose ξ2 with the help of Heath-Brown’s
identity. As the arguments can be applied mostly unchanged, we are brief. Similarly as
at the end of [7, Section III.5] we can reduce the critical range I3 to an interval I ∗
3 =
[θ∗
1 + 2ǫ, τ + 2ǫ]. Indeed, the extensions of I2 can be easily checked with our modiﬁed
argument. The enlargement of I5 and the following application of [7, (S.6), (S.4), (S.7)]
that completes the treatment of I1, I3, I5 can be done exactly as there by replacing the
three cases with our (T.4), (T.3), (T.5). □

8.3. Initial reduction and special case

In this subsection we do an initial reduction of Proposition 8.2 and prove the case (T.4).

Lemma 8.5. It suﬃces to show Proposition 8.2 with the following technical modiﬁcations.
(1) In the cases (T.2), (T.3), (T.4), and (T.5) one may assume that QR > X 1/2−ǫ.
(2) In the case (T.5) one may assume that Q2R ≤ X, and in the cases (T.2), (T.3),
and (T.5) one may assume that QN 3/2 ≤ X 1−ǫ and that Q2RN ≤ X 2−ǫ.
(3) In the cases (T.2), (T.3), and (T.5) one may assume that βn is supported on
squarefree integers only, if the estimate

D ≪ ∥α∥2√
XN (log X)
OC (1)P −1/6(66)
 is obtained for that case.
(4) In the case (T.4) one may replace 1m∈I , I = [M1, M2] ⊂ [M, 2M ] by a smooth
indicator, i.e. take αm = χ(m)fM (m/M ) for some smooth function fM supported
on [(M1/M )(1 − M −ǫ), (M2/M )(1 + M −ǫ)], equal to 1 on [M1/M, M2/M ] with
∥f (j)
M ∥∞ ≪j M ǫj.

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 39

(5) In the case (T.5) one may replace 1q∈I with I = [Q1, Q2] ⊂ [Q, 2Q] by a smooth
indicator, i.e. take γq = fQ(q/Q) for some smooth function fQ supported on
[(Q1/Q)(1 − Q−ǫ), (Q2/Q)(1 + Q−ǫ)], equal to 1 on [Q1/Q, Q2/Q] with ∥f (j)
Q ∥∞ ≪j
Qǫj.

Proof. Statement (1) is clear, as else we get the result by (T.1).
We now show (2). To see that we may assume in the case (T.5) that

Q2R ≤ X,

note that we are counting
 mn = a + qrs,

where m ∼ M , n ∼ N , q ∼ Q, r ∼ R and X ∼ QRs. As both q and s are unweighted
variables, they play the same role, except that s runs through an interval that depends on
m, n, r. By splitting all variables into intervals of multiplicative length X −ǫ′, we get rid of
the dependence of these intervals on m, n, r′; for this to work, we need S := X/(QR) ≫ X ǫ,
which we do have by assumption. Hence, either Q2R ≤ X or S2R ≤ X, and we may
assume that the former holds.
The bound QN 3/2 ≤ X 1−ǫ follows in the case (T.2) from N ≤ X 1/2−ǫQ−1/2
1 Q−1
2 , in the
case (T.3) from N ≤ X 2/5−ǫQ−2/5, and in the case (T.5) from the assumption Q2R ≤ X.
The bound Q2RN ≤ X 2−ǫ follows from QN 3/2 ≤ X 1−ǫ and the assumption QR ≤ X 1−ǫ.
To reduce to squarefree n and obtain statement (3), we follow a routine strategy (see
for example [5, Section 5.2] for a similar but more elaborate approach) and write n = kn′

with n′ squarefree. Let K denote the set of square-full integers. Then

D = ∑

k
k∈K
 ∑

q∼Q
 ∑

r∼R
(qr,a)=1
 γqδr ∑

m∼M
n′∼N/k
 αmµ2(n′)βkn′uP (mn′ka; qr).

By the trivial bound (59) we can estimate the contribution of k > K by

≪ P X(log X)
OC (1)K −1/2.

Write now
 α
′
m = 1k|mαm/k
β′
n = k−ǫµ2(n′)βkn′

so that ∑

q∼Q
 ∑

r∼R
(qr,a)=1
 γqδr ∑

m∼M
n′∼N/k
 αmµ2(n′)βkn′uP (mnka; qr)

= kǫ ∑

q∼Q
 ∑

r∼R
(qr,a)=1
 γqδr ∑

m′∼kM
n′∼N/k
 α
′
m′β′
n′uP (m′n′a; qr).

40 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

If K < X ǫ/2 we can apply (66) with the assumed improved estimate and ǫ/2 taking the
role of ǫ to get
∑

q∼Q
 ∑

r∼R
(qr,a)=1
 γqδr ∑

m′∼kM
n′∼N/k
 α
′
m′β′
n′uP (m′n′a; qr) ≪ ∥α
′∥2√XN (log X)
OC (1)P −1/6

≪ X(log X)
OC (1)P −1/6k−1/2+ǫ.

Consequently we can bound the contribution of k ≤ K by

X(log X)
OC (1)P −1/6 ∑

k≤K
k∈K
 k−1/2+2ǫ ≪ X(log X)
OC (1)P −1/6K 2ǫ.

We obtain the desired result after choosing K = P 3.
In statement (4), the error induced by introducing a smooth cutoﬀ can be estimated
with the help of the trivial bound (59) by

XP (log X)
OC (1)M −ǫ′,

and as P ≤ X ǫ′, M > Q1/2R ≥ X 1/4−ǫ′/2, this is suﬃcient.
Similarly as in (4), in statement (5) the error from replacing the cutoﬀ by a smooth
function can be estimated by
 XP (log X)
OC (1)Q−ǫ,

which is suﬃcient, now for (66), as we have R ≤ X 1/3R−1/3 and QR > X 1/2−ǫ′. □

We also need the following truncated version of the Poisson summation formula on
several occasions.

Lemma 8.6 (Truncated Poisson summation). Let ǫ be small, f be a smooth function
supported on [−10, 10] with ∥f (j)∥∞ ≪j X ǫj, and let M, q ≤ X. Then we have
∑

m≡a(q) f ( m
M ) = M
q
 ∑

|h|≤H
 ̂f ( hM
q )
e
( −ah
q ) + Oǫ(X −100)

for any choice H > X 2ǫq/M .

Proof. By Poisson summation,
∑

m≡a(q) f ( m
M ) = M
q
 ∑

h ̂f ( hM
q )e
( −ah
q ).

The bound ∥f (j)∥∞ ≪j X ǫj together with integration by parts gives ̂f (t) ≪j X ǫjt−j. So
we can bound the contribution of |h| > X 2ǫq/M by

≪j M
q X ǫj ∑

h>X 2ǫq/M
 ( hM
q
 )−j ≪j M
q X ǫj+(−j+1)2ǫ,

which is suﬃciently small, after choosing j large enough in terms of ǫ. □

Given a character χ to the modulus q Gauß sums of the form

cχ(a) := ∑

b(q)∗ χ(b)eq(ba)

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 41

will appear on several occasions. They are multiplicative in the following sense. If q = q1q2
with (q1, q2) = 1 then we have

cχ(a) = cχ(q1)(q2a)cχ(q2)(q1a).

It thus suﬃces to study them from prime powers and we have the following evaluation.

Lemma 8.7. Let χ be a character to the modulus pα and let pα0 denote the modulus of the
primitive character, χ∗, inducing χ. Let pαm = (pα, m). If α0 > α − αm then cχ(m) = 0.
If α0 ≤ α − αm then

cχ(m) = χ∗(m/pαm )χ∗(pα−αm−α0)µ(pα−αm−α0) ϕ(pα)
ϕ(pα−αm ) τ (χ∗)

Proof. This is [23, Lemma 5.4] for prime power moduli. □

We now prove case (T.4) of Proposition 8.2 (based on the work of Bombieri–Friedlander–
Iwaniec [1]), which is diﬀerent from the other cases in that it does not rely on the dispersion
method.

Lemma 8.8 (Variant of [1] Section 12). Proposition 8.2 is true in the case (T.4).

Proof. Recall that D is given by (61) and that by Lemma 8.5 we can assume to be in the
case αm = fM (m/M )χ(m), where χ (mod s) is a primitive character to some modulus
s ≤ P .
We restrict r into a ﬁxed residue class l modulo s and further restrict q such that
(q, s) = sq. Taking the values of l and sq that give the largest contribution, it suﬃces to
show
 D ≪ M N
X ǫ′τ (s)s ,

where
 D := ∑

q,r
(q,s)=sq,r≡l(s)
(qr,a)=1
 γqδr ∑

m,n fM (m/M )χ(m)βnuP (mna; qr).

Set W = [qr, s] and H = X 2ǫ′W/M . By Poisson summation (Lemma 8.6), we have
∑

m
m≡an(qr)
 fM (m/M )χ(m) = M
W
 ∑

c(W )
c≡an(qr)
 χ(c) ∑

|h|≤H
 ̂fM ( hM
W )
e
( −ch
W ) + Oǫ′(X −100)(67)

and 1
ϕ(qr)
 ∑

ψ(qr)
cond(ψ)≤P
 ψ(an) ∑

m fM (m/M )χψ(m)

= M
ϕ(qr)W
 ∑

ψ(qr)
cond(ψ)≤P
 ψ(an) ∑

c(W ) χψ(c) ∑

|h|≤H
 ̂fM ( hM
W )e
( −ch
W ) + Oǫ′(X −100).(68)

The error terms are obviously admissible.

42 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

We ﬁrst consider the case h = 0. We have
∑

c(W )
c≡an(qr)
 χ(c) = χ(an)1s|qr

and ∑

c(W ) χψ(c) = ϕ(W )1cond(χψ)=1.

As s ≤ P , we have that s|qr is equivalent to the existence of a (necessarily unique)
character ψ (mod qr), cond(ψ) ≤ P such that cond(χψ) = 1. For this character it holds
that ψ(an) = χ(an). For s|qr we have furthermore

1
W = ϕ(W )
W ϕ(qr)

and so the h = 0 contributions to the right-hand side of (67) and (68) are equal.
We now consider the h ̸= 0 terms on the right-hand side of (68). The conductor of χψ
is at most P s and so by Lemma 8.7 and the classical bound for Gauß sums we have
∑

c(W ) χψ(c)e
( −ch
W ) ≪ √
P s(W, h).

Therefore, the h ̸= 0 terms in (68) contribute to D at most

M √P s ∑

q,r
(q,s)=sq,r≡l(s)
(qr,a)=1
 |γq||δr|Hτ (W )
W ϕ(qr)
 ∑

n |βn| ≪ X 3ǫ′√P sN,

which is admissible by (62) and the assumptions P, s ≤ X ǫ′.
To bound the contribution of the h ̸= 0 terms on the right-hand side of (67) to D we
write W = W1W2, and analogously χ = χW1χW2, with W1 = (W, (qr)∞) and sr = (s, r)
(which is ﬁxed by r ≡ l(s)), and we observe that

∑

c(W )
c≡an(qr)
 χ(c)e
( −ch
W ) = ∑

c1(W1)
c1≡an(qr)
 χW1(c1)e
( −c1hW2
W1
 ) ∑

c2(W2) χW2(c)e
( −c2hW1
W2
 )

= ∑

d(s,(sqsr)∞) χW1(an + dqr)e
( −(an + dqr)hW2
qr(s, (sqsr)∞) ) ∑

c2(W2) χW2(c2)e
( −c2hW1
W2
 )

= e
(−ah nW2
qr(s, (sqsr)∞) ) ∑

d(s,(sqsr)∞) χW1(an + dqr)e
( −dhW2
(s, (sqsr)∞) )

× ∑

c2(W2) χW2(c2)e
( −c2hW1
W2
 ).

We recall that r ≡ l(s) and that W2(s, (sqsr)∞) ≤ s. Therefore, it suﬃces to show

D′ ≪ N
X ǫ′τ (s)s2 ,

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 43

where
D′ := ∑

q,r
(q,s)=sq,r≡l(s)
(qr,a)=1
 γqδr
W
 ∑

n βn ∑

1≤|h|≤H
 ̂fM ( M h
W )e
(−ah nW2
qr(s, (sqsr)∞) )
e( −d′h
s )

for any ﬁxed d′(s). By deﬁnition W = qrs
[sq,sr] , and we can separate the variables by

̂fM ( M h
W ) = qs
[sq, sr]M
 ∫ ∞

−∞ fM ( ξqs
M [sq, sr] )e
( ξh
r )dξ.

Thus,
 D′ ≪ X ǫ′Q−1 ∑

q∼Q
n∼N
∣
∣
∣ ∑

1≤|h|≤H
 ∑

r
(r,a)=1
r≡l(s)
 δr
r e
( ξh
r )e( −d′h
s )e
(−ah nW2
qr(s, (sqsr)∞) )∣
∣
∣

≪ X ǫ′Q−1 ∑

Q≤q′≤QX ǫ′

N ≤n′≤X ǫ′ N
∣
∣
∣ ∑

1≤|h|≤H
 ∑

r
(r,a)=1
r≡l(s)
 δr
r e
( ξh
r )
e( −d′h
s )e
(−ah n′

q′r )∣
∣
∣

≪ X ǫ′Q−1R−1 ∑

Q≤q′≤QX ǫ′

N ≤n′≤X ǫ′ N
∣
∣
∣ ∑

1≤|h|≤H
 ∑

r
(r,a)=1
 δ(h, r)e
(−ah n′

q′r )∣
∣
∣.

for some |δ(h, r)| ≤ 1. This expression is as in [1, after eq. (12.2)], so the proof there now
goes through (and gives a power-saving). □

8.4. Dispersion method and Kloosterman sums

The cases (T.2), (T.3), (T.5) of Theorem 8.2 are proved with the dispersion method.
We split its application into two lemmas.

Lemma 8.9 (Dispersion of bilinear sums). Assume Convention 3 and let D be as in (61).
Assume further that
 P ≤ X ǫ′
(69)
 R ≤ N X −ǫ(70)
 QN 3/2 ≤ X 1−ǫ(71)
 QR ≤ X 1−ǫ.(72)

Then we have

D ≪ ∥α∥2√
XN P −1/6(log X)
OC (1) + (M R)
1/2(log X)
OC (1)( ∑

ν≤P 1/2
 ∑

q0≤P 1/2
(q0,aν)=1
 |E (q0, ν)|
)1/2,

44 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

where

E (q0, ν) := ∑

r∼R
(r,aν)=1
 ∑

q1,q2
(aν,q1q2)=1
(q1,q2)=1
 γq0q1γq0q2 ∑

n1,n2
(n1,n2)=1
n1≡n2(q0r)
(ni,q0qir)=1
 βνn1βνn2
 


 ∑

m
mνni≡a(q0qir)
 f0( m
M ) − M ̂f0(0)
q0q1q2r
 


 .

(73)

Proof. At the heart of the dispersion method lies the Cauchy–Schwarz inequality. Its
application gives us
 D2 ≤ ∥δ∥
2∥α∥
2S (M, N, Q, R)

≤ R∥α∥
2 (log X)
OC (1)S (M, N, Q, R),

where
 S (M, N, Q, R) := ∑

r∼R
(r,a)=1
 ∑

m∼M
 ∣
∣
∣
∣
∣
 ∑

q∼Q
n∼N
(q,a)=1
 γqβnuP (mn¯a; qr)

∣
∣
∣
∣
∣

2
.

Deﬁne S ∗ = S ∗(M, N, Q, R) similarly to S (M, N, Q, R) but with an additional smooth
weight f0( m
M ) on the m variable. Then S (M, N, Q, R) ≤ S ∗(M, N, Q, R). We recall the
deﬁnition of uP in (48) and expand the square in the deﬁnition of S ∗ to write

S ∗ = S1 − 2Re(S2) + S3,

where

S1 := ∑

r∼R, m
(r,a)=1
 f0( m
M ) ∑

q1,q2
(a,q1q2)=1
 γq1γq2 ∑

n1,n2
mni≡a(qir)
 βn1βn2

S2 := ∑

r∼R, m
(r,a)=1
 f0( m
M ) ∑

q1,q2
(a,q1q2)=1
 γq1γq2
ϕ(q2r)
 ∑

ψ(q2r)
cond(ψ)≤P
 ψ(ma) ∑

n1,n2
mn1≡a(q1r)
 βn1βn2ψ(n2)

S3 := ∑

r∼R, m
(r,a)=1
 f0( m
M ) ∑

q1,q2
(a,q1q2)=1
 γq1γq2
ϕ(q1r)ϕ(q2r)
 ∑

ψi(qir)
cond(ψi)≤P
 ψ1ψ2(ma) ∑

n1,n2 βn1βn2ψ1(n1)ψ2(n2).

We ﬁrst estimate S1. We begin by discarding the terms with (q1, q2) ≥ Q0 and
(n1, n2) ≥ N0 from S1 for Q0 = N0 = P 1/2. This produces an error term which is

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 45

O (
P −1/3XN R−1(log X)OC (1)). Indeed, the contribution of (n1, n2) = ν is crudely

≪ ∑

r∼R
 ∑

M/2≤m≤3M
(r,am)=1
 ∑

q1,q2∼Q
(am,q1q2)=1
(q1q2r,ν)|a
 τ (q1)
Cτ (q2)
C ∑

n1∼N
n1≡am (mod q1r)
ν|n1
 ∑

n2∼N
n2≡am (mod q2r)
ν|n2
 τ (n1)
Cτ (n2)
C

≪ ∑

r∼R
 ∑

M/2≤m≤3M
(r,am)=1
 ∑

n1∼N
n1≡am (mod r)
ν|n1
 ∑

n2∼N
n2≡am (mod r)
ν|n2
 (τ (n1)τ (n2))
C (τ (mn1 − a)τ (mn2 − a))
C+1

≪a ∑

r∼R
 ∑

M/2≤m≤3M
(r,am)=1
 N 2

r2 (log X)
OC (1)τ (ν)
4C+2ν−2

≪ M N 2

R (log X)
OC (1)ν1/100−2,

where for the third line we used the trivial inequality x1 · · · x4 ≤ ∑i≤4 x4
i and a stan-
dard upper bound for ∑n≤x,n≡α (mod s) τ (n)B arising from Shiu’s bound [27, Theorem 1].
This summed over ν ≥ P 1/2 produces ≪ P −1/3XN R−1(log X)OC (1). The contribution of
(q1, q2) ≥ P 1/2 is bounded similarly (cf. [1, p.219]).
Therefore, we obtain

S1 = S ′
1 + O (
P −1/3XN R−1(log X)
OC (1)) ,(74)

where
 S ′
1 := ∑

ν≤P 1/2
 ∑

q0≤P 1/2
(q0,aν)=1
 S1(ν, q0)

and
 S1(ν, q0) := ∑

r∼R, m
(r,aν)=1
 f0( m
M ) ∑

q1,q2
(aν,q1q2)=1
(q1,q2)=1
 γq0q1γq0q2 ∑

n1,n2
(n1,n2)=1
mνni≡a(qir)
 βνn1βνn2.

Changing the order of summation, we have

S1(ν, q0) = ∑

r∼R
(r,aν)=1
 ∑

q1,q2
(aν,q1q2)=1
(q1,q2)=1
 γq0q1γq0q2 ∑

n1,n2
(n1,n2)=1
n1≡n2(r)
(ni,q0qir)=1
 βνn1βνn2 ∑

m
mνni≡a(q0qir)
 f0( m
M )
.

We approximate the sum over m by M ̂f0(0)/(q0q1q2r) so that

S ′
1 = X + ∑

ν≤P 1/2
 ∑

q0≤P 1/2
(q0,aν)=1
 E (q0, ν),

46 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

where E (q0, ν) is as in (73) and

X := M ̂f0(0) ∑

ν≤P 1/2
 ∑

q0≤P 1/2
(q0,aν)=1
 ∑

r∼R
(r,aν)=1
 1
r
 ∑

q1,q2
(aν,q1q2)=1
(q1,q2)=1
 γq0q1γq0q2
q0q1q2
 ∑

n1,n2
(n1,n2)=1
n1≡n2(q0r)
(ni,q0qir)=1
 βνn1βνn2.

We complete the sum over ν ≤ P 1/2, again introducing and admissible error. Then the
above becomes

M ̂f0(0) ∑

q0≤P 1/2
(q0,a)=1
 ∑

r∼R
(r,a)=1
 1
r
 ∑

q1,q2
(a,q1q2)=1
(q1,q2)=1
 γq0q1γq0q2
q0q1q2ϕ(q0r)
 ∑

ψ (mod q0r)
 ∑

n1,n2
(ni,qi)=1
 ψ(n1)βn1ψ(n2)βn2 .

The main term here comes from characters with small conductor, for us those that have
conductor ≤ P . Large conductor characters are handled by the Cauchy–Schwarz inequality
and Lemma 6.6; this gives us
∣
∣
∣ ∑

r∼R
(r,aν)=1
 1
ϕ(q0r)
 ∑

ψ (mod q0r)
cond(ψ)>P
 ∑

n1,n2
(ni,qi)=1
 ψ(n1)βn1ψ(n2)βn2∣
∣
∣

≤ ( ∑

r≤Rq0
 1
ϕ(r)
 ∑

ψ (mod r)
cond(ψ)>P
 ∣
∣ ∑

n
(n,q1)=1
 ψ(n)βn∣
∣2)1/2

× ( ∑

r≤Rq0
 1
ϕ(r)
 ∑

ψ (mod r)
cond(ψ)>P
 ∣
∣ ∑

n
(n,q2)=1
 ψ(n)βn∣
∣2)1/2

≪ (
Rq0 + N
P
 )
N (log X)
OC (1).

Thus we have

X = M ̂f0(0) ∑

q0≤P 1/2
(q0,a)=1
 ∑

r∼R
(r,a)=1
 1
r
 ∑

q1,q2
(a,q1q2)=1
(q1,q2)=1
 γq0q1γq0q2
q0q1q2ϕ(q0r)
 ∑

ψ (mod q0r)
cond(ψ)≤P
 ∑

n1,n2
(ni,qi)=1
 ψ(n1)βn1ψ(n2)βn2

+ O( M N (log X)OC (1)

R (P R + N
P 1/3 ))
.

By (69) and (70), this is acceptable. After completing the sum over q0 again, the main
term here equals up to an admissible error

X := M ̂f0(0) ∑

r
(r,a)=1
 1
r
 ∑

q1,q2
(a,q1q2)=1
 γq1γq2
[q1, q2]ϕ((q1, q2)r)
 ∑

ψ (mod (q1,q2)r)
cond(ψ)≤P
 ∑

n1,n2
(n1,n2)=1
 ψ(n1)βn1ψ(n2)βn2.

To complete the proof of Lemma 8.9, we show that S2 and S3 are also well approximated
by X .
We now consider S2 and follow a strategy that generalises both [5, Section 5.3.2] and [1,
Section 5]. Let c denote the conductor of ψ in the deﬁnition of S2. In the relevant range

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 47

of summation, m is coprime to q1r and we have
∑

ψ(q2r)
cond(ψ)≤P
 ψ(man2) = ∑

c≤P
ψ(c)∗
 ψ(man2)1(n2,q2r)=1
c|q2r 1(m,q2)=1

= ∑

c≤P
ψ(c)∗
 ψ(man2)1(n2,q2r)=1
c|q2r
 ∑

e|(m,q2), (e,q1r)=1 µ(e).

Since e > P 1/2 implies (m, q2) > P 1/2, the contribution of e > P 1/2 to S2 gives an
admissible error. We denote the remaining terms with e ≤ P 1/2 by S ′
2 and sort r into
residue classes modulo c to get

S ′
2 = ∑

c≤P
ψ(c)∗
 ψ(a) ∑

q1,q2
(a,q1q2)=1
 γq1γq2 ∑

e|q2, (e,q1)=1
e≤P 1/2
 µ(e)ψ(e) ∑

n1,n2
(ni,qi)=1
 βn1βn2ψ(n2)

× ∑

c(c)
c≡0(c/(c,q2))
 T (n1, n2, q1, q2, ψ, c, e),

where
 T (n1, n2, q1, q2, ψ, c, e) := ∑

r∼R
(r,aen1n2)=1
r≡c(c)
 1
ϕ(q2r)
 ∑

emn1≡a(q1r) ψ(m)f0( em
M ).

Set W = [q1r, c], H = W eX ǫ′/M so that by Poisson summation (Lemma 8.6)
∑

emn1≡a(q1r) ψ(m)f0( em
M ) = M
eW
 ∑

b(W )
b≡aen1(q1r)
 ψ(b) ∑

|h|≤H
 ̂f0( hM
eW )
e
( −bh
W ) + Oǫ′(X −100).(75)

The error term is negligible. We furthermore have
∑

b(W )
b≡aen1(q1r)
 ψ(b) = ψ(aen1)1c|q1r,

and so the term h = 0 on the right-hand side of (75) contributes to S ′
2

M ̂f0(0) ∑

c≤P
ψ(c)∗
 ∑

q1,q2
(a,q1q2)=1
 ∑

r∼R
(r,an1n2)=1
 1c|r(q1,q2) γq1γq2
ϕ(q2r)q1r
 ∑

e|q2, (e,rq1)=1
e≤P 1/2
 µ(e)
e
 ∑

n1,n2
(ni,qi)=1
 βn1ψ(n1)βn2ψ(n2).

(76)

Observing that
 1
ϕ(q2r)
 ∑

e|q2, (e,rq1)=1
 µ(e)
e = 1
q2r
 ∏

p|q2r
(
1 − 1
p
 )−1 ∏

p|q2
p∤rq1
(
1 − 1
p
 )

= 1
q2r
 ∏

p|(q1,q2)r
(1 − 1
p
 )−1,

48 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

the expression in (76) equals to X up to admissible error after completing the sum over e
again, as we may.
To estimate the contribution of terms with h ̸= 0 to the right-hand side of (75), we
start by writing W = q1rc′̃c with c′ = (c/(c, q1r), (q1r)∞) and observe
∑

b(W )
b≡aen1(q1r)
 ψ(b)e
( −bh
W ) = ∑

b1(q1rc′)
b1≡aen1(q1r)
 ψ(c/̃c)(b1)e
( −b1h
q1rc′ ) ∑

b2(̃c) ψ(̃c)(b2)e
( −b2h
̃c )

= e
(−ah en1
q1rc′ ) ∑

b′(c′) ψ(c/̃c)(aen1 + b′q1r)e
( −b′h
c′ ) ∑

b2(̃c) ψ(̃c)(b2)e
( −b2h
̃c )
,(77)

where we factorised ψ = ψ(c/̃c)ψ(̃c). Given q1 and c, the condition r ≡ c(c) determines
in particular also c′ and ̃c. Thus, after changing the order of summation and trivially
summing over b′ and b2 that come from (77), the contribution of terms with h ̸= 0 in (75)
to T (n1, n2, q1, q2, ψ, c, e) can be estimated by

≪ M
eq1
 ∑

0<|h|≤H
∣
∣
∣ ∑

r∼R
(r,aen1n2)=1
r≡c(c)
 ̂f0( hM
eq1rc′̃c ) 1
rϕ(q2r) e
(−ah en1
q1rc′ )∣
∣
∣

This is almost the same object that is considered in [1, Section 5]. Similarly as there,
a routine calculation using reciprocity, Weil’s Kloosterman sum bound, and partial sum-
mation lets us bound it by
 ≪ X 2ǫ′c
eq1R
 (
N 1/2 + R
N
 ).

This contributes to S ′
2 at most
 QN 2X 2ǫ′P 4

R
 (
N 1/2 + R
N
 )
,

which is admissible by (69), (71), and (72).
We complete the proof of Lemma 8.9 by extracting X out of S3. Our strategy is closely
related to the one in [5, Section 5.3.1]. Set now W = r[q1, q2], H = W X ǫ′/M , and apply
Poisson summation (Lemma 8.6) to get

S3 = ∑

r∼R,
(r,a)=1
 ∑

q1,q2
(a,q1q2)=1
 γq1γq2
ϕ(q1r)ϕ(q2r)
 ∑

ψi(qir)
cond(ψi)≤P
 ψ1ψ2(a) ∑

n1,n2 βn1βn2ψ1(n1)ψ2(n2) ∑

b(W )∗ ψ1ψ2(b)

×
 ( 1
W
 ∑

|h|≤H
 ̂f0( h
H )e
( −bh
W ) + Oǫ′(X −100)

)
.

(78)

The error term is negligible.
We continue with the observation that
∑

b(W )∗ ψ1ψ2(b) = ϕ(W )1cond(ψ1ψ2)=1.

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 49

Since ∑

ψi(qir)
cond(ψi)≤P
 ψ1ψ2(a)ψ1(n1)ψ2(n2)1cond(ψ1ψ2)=1 = ∑

ψ((q1,q2)r)
cond(ψ)≤P
 ψ(n1n2)

and ϕ([q1, q2]r)
ϕ(q1r)ϕ(q2r) = 1
ϕ((q1, q2)r) ,

the h = 0 contribution to S3 in (78) equals X .
The h ̸= 0 contribution can be estimated using the bound (see Lemma 8.7))
∣
∣ ∑

b(W )∗ ψ1ψ2(b)e
( −bh
W )∣
∣ ≪ P (h, W ).

This gives a contribution of

≪ M P (log X) ∑

r∼R,
(r,a)=1
 ∑

q1,q2
(a,q1q2)=1
 ∣
∣γq1γq2∣
∣

W ϕ(q1r)ϕ(q2r)
 ∑

ψi(qir)
cond(ψi)≤P
 ∑

n1,n2
∣
∣βn1βn2∣
∣ ∑

0<|h|≤H(h, W )

≪ X ǫ′P (log X) ∑

r∼R,
(r,a)=1
 τ (r)
3 ∑

q1,q2
(a,q1q2)=1
 ∣
∣τ (q1)2γq1τ (q2)2γq2∣
∣

ϕ(q1r)ϕ(q2r)
 ∑

n1,n2
∣
∣βn1βn2∣
∣

≪ X ǫ′P (log X)
OC (1)N 2R−1.

This is admissible by (62) and (69). □

Next we translate the remaining term of the previous lemma, E(q0, ν), into sums of
Kloosterman sums.

Lemma 8.10 (Reduction to Kloosterman sums). Assume Convention 3 and that

βn is supported on squarefree n only.(79)

Assume further
 Q2RN ≤ X 2−ǫ.(80)

Let E (q0, ν) be given by (73). Then we have

|E (q0, ν)| ≪ M ν5W (q0, ν) + X 1−ǫ′N
R ,

where
 W (q0, ν) := max
l1,l2,l3,l4.l5(ν)
 ∣
∣
∣
∣
∣ 1
q0
 ∑

r∼R
r≡l3
(r,aν)=1
 1
r
 ∑

qi
(aν,q1q2)=1
(q1,q2)=1
qi≡li(ν)
 γq0q1γq0q2
q1q2
 ∑

n1,n2
(n1,n2)=1
n1≡n2(q0r)
(ni,q0qir)=1
n1≡l4(ν)
 βνn1βνn2(81)
 × ∑

0<|h|≤H
h≡l5(ν)
 ̂f0( hM
q0q1q2r )e (ah n2 − n1
q0r νq1n2
q2n1
 ) ∣
∣
∣
∣
∣
.

50 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

Proof. Given ni, qi, r in the range of summation in (73), let ℓ be such that

ℓνn1 ≡ a(q0q1r)

ℓνn2 ≡ a(q0q2r).
(82)

Let
 H := X ǫ′Q2R/M(83)

and apply Poisson summation (Lemma 8.6) to get

∑

m
mνni≡a(q0qir)
 f0( m
M ) − M ̂f0(0)
q0q1q2r = ∑

m
m≡ℓ(q0q1q2r)
 f0( m
M ) − M ̂f0(0)
q0q1q2r

= M
q0q1q2r
 ∑

1≤|h|≤H
 ̂f0
 ( hM
q0q1q2r
 ) e ( −ℓh
q0q1q2r
 ) + O (
X −100) .

(84)

The error term is small enough.
At this point, since we cannot make the assumption (A4) in [1] (roughness of βn) to
reduce to the case ν = 1, we instead follow the argument after [8, (3.18)] almost verbatim.
Write t = (n2 − n1)/(q0r). The congruence conditions (82) are equivalent to

ℓνn1 = a + q0q1ru1
ℓνn2 = a + q0q2ru2

for some integers u1, u2. Thus q2u2n1 − q1u1n2 = at and

u1 ≡ −atq1n2(q2n1).

Furthermore,
 u1 ≡ −arq0q1(ν)

and so, using that by (79) we can assume (n1, ν) = 1,

ℓh
q0q1q2r = ah
νq0q1q2rn1 + u1h
νn1q2

≡ −ah rq0q1q2n1
ν − ath q1n2ν
q2n1 + ah
νq0q1q2rn (mod 1),

so
 e ( −ℓh
q0q1q2r
 ) = e (ah rq0q1q2n1
ν
 ) e (ah n2 − n1
q0r νq1n2
q2n1
 ) + O ( q0|ah|
νN Q2R
 ) .(85)

The contribution of the error terms present in (85) to E (ν, q0) is crudely bounded using
the divisor bound and | ̂f0(y)| ≪ 1 by

≪a q0X 2ǫ′

X N 2Q2

q3
0 ,

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 51

which is admissible by (80). The term we still have to consider is

M
q0
 ∑

r∼R
(r,aν)=1
 1
r
 ∑

q1,q2
(aν,q1q2)=1
(q1,q2)=1
 γq0q1γq0q2
q1q2
 ∑

n1,n2
(n1,n2)=1
n1≡n2(q0r)
(ni,q0qir)=1
 βνn1βνn2

× ∑

0<|h|≤H
 ̂f0
 ( hM
q0q1q2r
 ) e (ah rq0q1q2n1
ν
 ) e (ah n2 − n1
q0r νq1n2
q2n1
 ) .

The lemma follows after restricting r, q1, q2, n1, and h into ﬁxed residue classes (mod ν)
and taking the maximum over those. □

8.5. Estimates for W (q0, ν)

In this section we estimate W (q0, ν) and as a consequence deduce the remaining cases
(T.2), (T.3), and (T.5) of Proposition 8.2.
The following lemma gives us case (T.2).

Lemma 8.11 (Variant of Lemma 8.1 in [21]). Assume Convention 3 and let W (q0, ν) be
as in (81) with q0, ν ≤ X ǫ′. Let further γ = λ ⋆ ρ with λs and ρt being coeﬃcient sequences
of order C supported on t ∼ T , s ∼ S (so ST ≍ Q). Assume that

N 2T 2S < X 1−ǫ,(86)
 N 2T 3S4R < X 2−ǫ,(87)
 N T 2S5R < X 2−ǫ.(88)

Then we have
 W (q0, ν) ≪ N 2

RX ǫ′ .

In particular, case (T.2) of Proposition 8.2 holds.

This result is closely related to Maynard’s [21, Lemma 8.1], but diﬀers in the following
aspects:

• The variables si, ti (appearing after Cauchy–Schwarz) and n1, r, and h are re-
stricted to a congruence class.
• There are factors q0 and ν in the coeﬃcients.
• There is no lower bound for |n1 − n2| and no Fouvry-style N condition.
• The exponential phase is of slightly diﬀerent shape and has an additional ν term.
• The condition (q2s2, rq0) = 1 is missing.
• There is an additional q0 dependence in λ and λ′.
• The variable H ′ is slightly larger, in Maynard’s statement X o(1) replaces X ǫ′.
• There is the ̂f0 ( hM
q0q1q2r ) term.
• Our coeﬃcients are only divisor bounded, not 1-bounded.

These changes are harmless and require no considerable modiﬁcations of the original ar-
gument.

52 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

Proof of Lemma 8.11. First we remove the term ̂f0 ( hM
q0q1q2r ) by summation by parts. We

have | ̂f0(j)(ξ)| ≪j,k |ξ|−k and recall that f is supported on [1/2, 5/2]. Thus

∂k1+k2+k3+k4

∂rk1∂q1k2∂q2k3∂hk4 ̂f0
 ( hM
q0q1q2r
 ) ≪k1,k2,k3,k4 r−k1q1−k2q2−k3h
−k4

and so
 W (q0, ν) ≪ W ′(q0, ν),

where

W ′(q0, ν) = sup
H ′≤2H
R′≤2R
Q1,Q2≤2Q
 ∣
∣
∣
∣
∣ sup
l1,l2,l3,l4.l5(ν)
 ∑

R≤r≤R′
r≡l3(ν)
(r,aν)=1
 1
r
 ∑

q1≤Q1,q2≤Q2
(aν,q1q2)=1
(q1,q2)=1
qi≡li(ν)
 γq0q1γq0q2
q1q2
 ∑

n1,n2
(n1,n2)=1
n1≡n2(q0r)
(ni,q0qir)=1
n1≡l4(ν)
 βνn1βνn2

× ∑

0<|h|≤H ′
h≡l5(ν)
 e (ah n2 − n1
q0r νq1n2
q2n1
 ) ∣
∣
∣
∣
∣
.

For the remainder of the proof we consider the ﬁxed choice of H ′, R′, Q1, Q2, l1, l2, l3, l4
that corresponds to the largest output.
Essential for Maynard’s improvements over [1, Theorem 1] is the factorisation γ = λ ⋆ ρ.
We apply it and furthermore absorb the congruence condition qi ≡ li(ν) and the factor q0
in γq0qi into new coeﬃcients. More precisely, for any ﬁxed q′
0, q′′
0 , l′
i, l′′
i with

q0 = q′
0q′′
0 ,

l1 ≡ l′
1l′′
1 (ν),

l2 ≡ l′
2l′′
2 (ν),

write
 λ
′
s1 = X −ǫ′/100λq′
0s11s1≡l′
1(ν)

λ
′′
s2 = X −ǫ′/100λq′
0s21s2≡l′
2(ν)

ρ′
t1 = X −ǫ′/100ρq′′
0 t11t1≡l′
1(ν)

ρ′′
t2 = X −ǫ′/100ρq′′
0 t21t2≡l′′
2 (ν)

β′
n1 = X −ǫ′/100βνn11n1≡l4(ν)

β′′
n2 = X −ǫ′/100βνn2,

(89)

where the X −ǫ′/100 term ensures that the new coeﬃcients are 1-bounded, if X is suﬃciently
large.
Set
 N ′ = N/ν

and observe that N ′2

RX 2ǫ′ ≪ N 2

Rν2τ (q0)X 11ǫ′/10 .

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 53

Thus, for some choice of q′
0, q′′
0 , li, l′′
i in (89) it suﬃces to show

W1 ≪ N ′2

RX 2ǫ′ ,(90)

where

W1 := ∑

R≤r≤R′
r≡l3(ν)
(r,aν)=1
 1
r
 ∑

s1t1≤Q1,s2t2≤Q2
(aν,s1t1s2t2)=1
(s1t1,s2t2)=1
 λ′
s1ρ′
t1λ′′
s2ρ′′
t2
s1t1s2t2
 ∑

n1,n2
(n1,n2)=1
n1≡n2(q0r)
(ni,q0qir)=1
 β′
n1β′′
n2 ∑

0<|h|≤H ′
h≡l5(ν)
 e (ah n2 − n1
q0r νq1n2
q2n1
 ) .

Here the sequences are supported on
 ni ∼ N ′

si ∼ S′

ti ∼ T ′

for N ′ = N/ν and for some
 S/q0 ≤ S′ ≤ S

T /q0 ≤ T ′ ≤ T.

We now follow the steps in [21, proof of Lemma 8.1] and write

f = (n1 − n2)/(q0r)

for some 1 ≤ |f | ≤ 2N ′/q0R (note that n1 ̸= n2 by (n1, n2) = 1). Thus the exponential
becomes
 e
( ahf νq1s1n2
q2s2n1
 )
,

which is the same as in [21, Lemma 8.1] after the f substitution, except of the additional
ν. We get
 W1 = ∑

1≤|f |≤2N/R
 ∑

ti
(t1t2,a)=1
 ∑

s2
(t2s2,at1)=1
 ∑′

ni
n1≡n2(q0f )
 β′
n1ρ′
t1β′′
n2λ′′
s2ρ′′
t2 q0f
t1t2s2(n1 − n2)

× ∑

s1
(s1,an1s2t2)=1
s1t1≤Q1
 λ′
s1
s1
 ∑

1≤|h|≤H ′
h≡l2(ν)
 e
( ahf νt1s1n2
t2s2n1
 )
,

where ∑′ encodes the following summation conditions

(n1, n2) = 1

(ni, siti) = 1

(n1 − n2)/(f q0) ≡ l1(ν)

((n1 − n2)/(f q0), aν) = 1

Rq0f ≤ n1 − n2 ≤ R′q0f.

54 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

We can remove the condition s1t1 ≤ Q1 by Fourier analysis and apply the Cauchy–
Schwarz inequality, verbatim as in [21, proof of Lemma 8.1], to get

W1 ≪ N ′(log X)3

RT ′S′3/2 sup
θ
 ∣
∣W ′
1(θ)
∣
∣1/2,

where
 W ′
1(θ) := ∑

1≤|f |≤2N ′/R
 ∑

n1,n2∼N ′
n1≡n2(q0f )
 ∑

ti∼Ti
 ∑

s2∼S′
(n2t1,n1t2s2)=1

×
 ∣
∣
∣
∣
∣
 ∑

s1∼S′
(s1,an1t2s2)=1
 S′λ′
s1e(s1θ)
s1
 ∑

1≤|h|≤H ′
h≡l2(ν)
 e
( ahf νt1s1n2
t2s2n1
 )
∣
∣
∣
∣
∣
2,

which is almost the same as Maynard’s W3 with the only diﬀerences being the congruence
condition on h and the term ν in the exponential.
In Maynard’s proof there is no summation with cancellation over the h variable, so we
can drop the congruence condition on h (the two variables b and c that are summed with
cancellation arise in our notation from n2t1 and n1t2s2). Finally, the additional term ν
can be incorporated in the variable Maynard calls z. As a consequence, we replace his bz,y
by
 b′
z,y = ∑

s1,s2∼S′
 ∑

1≤|h1|,|h2|≤H ′
s1s2ν=z
af (h1s2−h1s2)=y
 ∑

f ∼F 1

= 1ν|zbz/ν,y

and this changes Z to Z ′ = νZ. By Maynard’s proof, this increase, the slightly larger
choice of H ′, and the fact that we replace the bound N M ≫ X by

N ′M ≫ X 1−ǫ′

are accounted for if ǫ is suﬃciently large in terms of ǫ′. Thus, observing the upper bounds
S′ ≤ S, T ′ ≤ T , we obtain (90) and so the lemma in the required range.
By Lemmas 8.5, 8.9, 8.10, this proves case (T.2) of Proposition 8.2, after choosing the
ǫ′ there small enough. □

We continue with the case (T.3).

Lemma 8.12 (Variant of [1] Section 9). Assume Convention 3 and let W (q0, ν) as in (81)
with q0, ν ≤ X ǫ′. Assume that
 N 2Q2R−1 ≤ X 1−ǫ

N 5Q2 ≤ X 2−ǫ

N 4Q3 ≤ X 2−ǫ.

Then
 W (q0, ν) ≪ N 2

RX ǫ′ .

In particular, case (T.3) of Proposition 8.2 holds.

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 55

This result is closely related to Bombieri–Friedlander–Iwaniec’s work [1, Section 9] with
the following harmless diﬀerences.

• There is an additional congruence condition on the h and r summation.
• There is an additional term ν in the exponential.
• There is a ν factor in the β coeﬃcients.
• There is the restriction (r, ν) = 1.

Proof. We follow the strategy of proof in [1, Section 9] with the corrections given in [2].
We remove the condition (r, aν) = 1 with the help of M¨obius inversion,

1(r,aν)=1 = ∑

δ|(r,aν) µ(δ).

Afterwards we change the variable r into k (compare [1, eq. (9.3), (9.4)]) with

n2 − n1 = δq0rk

(δq0k, n1n2) = 1

n2 ≡ n1(δq0k)

n2 − n1 ≡ δl3q0k(ν).

To remove the coupling of n2 and k from the congruence condition, we restrict k into
a ﬁxed class k ≡ l(ν). We can now, similarly to the start of the proof of Lemma 8.11,
absorb several of our additional conditions into new coeﬃcients. More precisely, let

γ′
q0q1 = γq0q11q1≡l1(ν)1(q1,ν)=1
γ′′
q0q2 = γq0q21q1≡l2(ν)1(q2,ν)=1
β′
n1 = βνn11n1≡l4(ν)
β′′
n2 = βνn21n2≡l3q0l+l4(ν).

Taking the maximum over li(ν), removing ̂f0 just as in the proof of Lemma 8.11, applying
the triangle inequality, and using the lower bounds r ≥ R, qi ≥ Q/q0, it suﬃces to show

W2 ≪ N 2Q2

νq2
0X ǫ′ ,

where

W2 = ∑

δ|aν
 ∑

1≤|k|≤K
 ∑

qi
(aν,q1q2)=1
(q1,q2)=1
 ∣
∣γ′
q0q1γ′′
q0q2∣
∣∣
∣
∣
∣
∣
 ∑

n1,n2
(n1,n2)=1
n1≡n2(δq0k)
(ni,qiq0k)=1
q0|k|R<|n2−n1|≤q0|k|R′
 β′
n1β′′
n2 ∑

0<|h|≤H ′
h≡l5(ν)
 e (ahk νq1n2
q2n1
 ) ∣
∣
∣
∣
∣,

K0 = N/q0R, R ≤ R′ ≤ 2R, and γ′
q, γ′′
q , β′
n β′′
n are supported on q ∼ Q, n ∼ N ′ = N/ν
respectively.
At this point we can open the congruence condition n2 ≡ n1(δq0k), (n1n2, δq0k) with
the help of characters and the range condition on |n2 − n1| with Fourier analysis, just as

56 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

in [2, eq. (9.7)] and [1, eq. (9.8)] to get

W2 ≪ (log 2N ) ∑

δ|aν
 ∑

1≤|k|≤K0
 ∑

ψ(kδq0)
 1
ϕ(kδq0)
 ∑

qi
(q1,q2)=1
 |γ′
q0q1γ′′
q0q2| ∑

n1
(n1,q1)=1
 |β′
n1|

× ∑

1≤|h|≤H
 ∣
∣
∣
∣
∣
∣
∣
 ∑

n2
(n2,n1q1)=1
 β(h, n2)χψ(n2)e (ahk νq1n2
q2n1
 )∣
∣
∣
∣
∣
∣
∣

for some |β(h, n2)| = |β′′
n2|. This is essentially the same object as in [2, eq. (9.12)], as the
fact that q1, q2 and n1, n2 are associated to diﬀerent sequences is irrelevant. We can absorb
the factor ν into the n2 variable, only increasing this instance of N to νN . Afterwards
the proof in the remainder of [1, section 9] goes through with the simpliﬁcations that as
βn are supposed to be divisor-bounded, we do not actually need the assumption that they
are supported on squarefree n only for this step, and condition [1, (A.5)] holds obviously
(unless ∑n |βn|2 ≪ N 1−ε/10 in which case Proposition 8.2 follows trivially from Cauchy–
Schwarz).
By Lemma 8.5, Lemma 8.9, and 8.10, this proves case (T.3) of Proposition 8.2. □

We end this section with proving the case (T.5). While it is based on the work of
Bombieri–Friedlander–Iwaniec [1, Section 13], the fact that Lemma 8.10 introduces a con-
gruence condition on the qi makes it necessary to use Drappeau’s extension of the argu-
ments on the spectral side given in [5, Theorem 2.1] that is built precisely to handle this
situation.

Lemma 8.13 ([1] Section 13 meets [5] Theorem 2.1). Let W (q0, ν) as in (81) with γq =
fQ(q/Q) as in Lemma 8.5(5). Let further ν, q0 ≤ X ǫ′. Assume that

N 3R ≤ X 1−ǫ(91)
 Q2R ≤ X.(92)

Then we have
 W (q0, ν) ≪ N 2

RX ǫ′ .

In particular, case (T.5) of Proposition 8.2 holds.

This result is closely related to [1, Section 13] with the following diﬀerences.
• There is an additional congruence condition on the h and r summation.
• There is an additional term ν in the exponential.
• There is a ν factor in the β coeﬃcients.
• There is the restriction (r, ν) = 1.
• There is a congruence condition on the qi.
Apart from the congruence condition on the qi, these modiﬁcations are again harmless.

Proof. Similarly as in [1, Section 13] we write

̂fQ( hM
q0q1q2r
 ) = q0q1q2
M
 ∫ ∞

−∞ fQ( ξq0q1q2
M
 )e(ξh/r)dξ

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 57

and detect the condition (a, q1q2) by M¨obius inversion so that

W (q0, ν) = M −1∣
∣
∣
∣
∣ sup
l1,l2,l3,l4.l5(ν)
(l1l2,ν)=1
 ∑

δ1δ2|a
(δ1,δ2)=1
(δ1δ2,ν)=1
 ∫ ∞

−∞
 ∑

r∼R
r≡l3
(r,aν)=1
 1
r
 ∑

qi
(q1,q2)=1
qi≡δ1li(ν)
 γδ1q0q1γδ2q0q2fQ( ξδ1δ2q0q1q2
M
 )

× ∑

n1,n2
(n1,n2)=1
n1≡n2(q0r)
(ni,q0qir)=1
n1≡l4(ν)
 βνn1βνn2 ∑

0<|h|≤H
h≡l5(ν)
 e(ξh/r)e (ah n2 − n1
q0r νq1n2
q2n1
 ) dξ
∣
∣
∣
∣
∣.

Taking the supremum of δ1, δ2, ξ and specialising to the maximal choice of admissible
li, it suﬃces to show
 W3 ≪ N 2Q2

RX 2ǫ′ ,(93)

where
 W3 = ∑

r∼R
r≡l3
(r,aν)=1
 1
r
 ∑

qi
(q1,q2)=1
qi≡δ1li(ν)
 γδ1q0q1γδ2q0q2fQ(ξδ1δ2q0q1q2) ∑

n1,n2
(n1,n2)=1
n1≡n2(q0r)
(ni,q0qir)=1
n1≡l4(ν)
 βνn1βνn2

× ∑

0<|h|≤H
h≡l5(ν)
 e(ξh/r)e (ah n2 − n1
q0r νδ1q1n2
δ2q2n1
 ) .

This is a mixture of Drappeau’s R′′
1 (deﬁned after [5, eq. (5.25)]) and [1, eq. (13.2)].
(Note an inaccuracy in [1, eq. (13.2)]: Similarly as in Remark 8.4, the term δ1 cannot
be made to 1/δ1. Here this is without consequence.). We write W3 in the form of [5, eq.
(2.3)] with

c ← q2 d ← q1 n ← ah(n2 − n1)/(q0r) r ← νδ1n2 s ← δ2n2 q ← ν

C ← Q/(q0δ2) D ← Q/(q0δ1) N ← |a|HN/(q0Rν) R ← δ1N S ← δ2N/ν.

The new coeﬃcients are given by

bn,r,s = ∑

r∼R
r≡l3(ν)
(r,aν)=1
 1
r
 ∑

n1,n2
(n1,n2)=1
n1≡n2(q0r)
n1≡l4(ν)
 βνn1βνn2 ∑

r=νδ1n2
s=δ2n
 ∑

0<|h|≤H
h≡l5(ν)
n=ah(n1−n2)/(q0r)
 e(ξh/r).

By [5, Theorem 2.1], (with the correction in [2] that also applies here and means that
there should be no S−1 factor) we get

W3 ≪ X O(ǫ′)q3/2(
qCS(RS + N )(C + RD) + C2DS√RS + N √R + D2N R
)1/2∥bn,r,s∥2.

Similarly as in [1, eq. (13.3)] we have

∥bn,r,s∥
2
2 ≪ X ǫ′N 2HR−2.

58 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

Plugging in our choice of variables and using that we have ν ≤ X ǫ′ and that by the
assumption Q2R ≤ X we have Q ≤ √X, we get

W3 ≪ X O(ǫ′)(Q2N 4 + Q3N 5/2)1/2N Q(RM )
−1/2

≪ X O(ǫ′) N 2Q2

R R1/2

N QM 1/2
 (
QN 2 + Q3/2N 5/4)

= N 2Q2

R X 1/2+O(ǫ′)(
N 3/2R1/2 + Q1/2R1/2N 3/4).

By (91) and (92) this is suﬃcient for (93).
By Lemmas 8.5, 8.9 and 8.10, this proves case (T.5) of Proposition 8.2. □

9. An application – Proof of Theorem 1.3

We now prove Theorem 1.3 that extends [21, Theorem 1.1]. This extension is possible
as our application of the dispersion method does not require the coeﬃcients after the
combinatorial dissection to be rough, and we work with uP that takes into account the
contribution of all low conductor characters.
We shall prove the following proposition, which directly implies Theorem 1.3.

Proposition 9.1. Let k ≥ 1, a ∈ Z \ {0} and ε > 0 be ﬁxed, with ε suﬃciently small. Let
N ≥ 2 and P ≤ N ε. Let |λd| ≤ τk(d) be any triply well-factorable sequence. Then it holds
that
 ∑

d≤N 3/5−ε
(d,a)=1
 λd
 



 ∑

n≤N
 µ(n)
ϕ(d)
 ∑

ψ(d)
cond(ψ)>P
 ψ(an)





 ≪ N P −1/200.(94)

Applying this with d ↦→ λdρ(d, P ) in place of d ↦→ λd gives Theorem 1.3.
With the notation (48), the statement (94) of Proposition 9.1 that we want to show
becomes
 ∑

d≤N 3/5−ǫ
(d,a)=1
 λd
 

 ∑

n≤N µ(n)uP (na; d)



 ≪ N P −1/200.(95)

We now prove two variants of Maynard’s central results that quickly lead to this using the
methods of the previous sections.

Lemma 9.2 (Variant of Proposition 5.1 in [21]). Let C ≥ 1 be ﬁxed. Assume Convention 3
and let λq be any triply well-factorable sequence of order C and level Q ≤ X 3/5−ǫ, and
assume
 N ≤ X 2/5.

Then for any P ≤ X ǫ′ we have
∑

q≤Q λq ∑

n,m αmβnuP (mna : q) ≪ X(log X)
OC (1)P −1/13.

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 59

Proof. This follows from the case (T.2) of Proposition 8.2 by using triply well-factorability
with Q = RQ1Q2, where (as in [21, Proof of Proposition 5.1])

R = N X −ǫ

Q1 = QX −2/5+ǫ

Q2 = N −1X 2/5.
 □

Lemma 9.3 (Variant of Proposition 5.2 in [21]). Let N1, N2 ≥ X ǫ and N1N2M ≍ X and

Q ≤ ( X
M
 )2/3−ǫ .

Let αm be a sequence with |αm| ≤ mǫ′. Then for P ≤ X ǫ′

∑

q∼Q
 ∣
∣
∣
∣
∣
 ∑

n1∼N1,n2∼N2
m∼M
n1n2m≤X
 αmuP (mn1n2a; q)

∣
∣
∣
∣
∣ ≪ X 1−ǫ′.

Proof. By a suﬃciently ﬁne dissection of the range of the variables n1, n2, m and the
introduction of smooth weights fN1, fN2 as in Lemma 8.5(4), it suﬃces to show

K ≪ X 1−ǫ/2

Q ,

where
 K = sup
(a,q)=1
q∼Q
 ∣
∣
∣
∣
∣
 ∑

m∼M αm ∑

n1,n2 fN1(n/N1)fN2(n/N2)uP (mn1n2a; q)

∣
∣
∣
∣
∣ .

Compare [21, Lemma 7.1]. Note that the derivatives of the smooth weights there are
slightly smaller. This only changes the error term in the application of Poisson summation
in an inconsequential manner. Let the supremum occur at a and q and write K =
|K2 − K1| with

K1 := 1
ϕ(q)
 ∑

ψ(q)
cond(ψ)≤P
 ∑

m∼M αm ∑

n1,n2 fN1(n/N1)fN2(n/N2)ψ(mn1n2a)

K2 := ∑

m∼M αm ∑

n1,n2 fN1(n/N1)fN2(n/N2)1mn1n2≡a(q).

Here K2 is the same Maynard considers and he shows, assuming N1 ≤ N2,

K2 = KMT + O( X 1+o(1)

QN1 + X o(1)M Q1/2)
,

where
 KMT := N1N2̂fN1(0)̂fN2(0) ϕ(q)2

q2 ∑

m∼M
(m,q)=1
 αm.

60 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

This main term can be extracted out of K1 similarly as in the proof of Lemma 8.8 (case
(T.4)). By Poisson summation (Lemma 8.6) we have any character ψ with modulus q that
∑

n1 fN1(n/N1)ψ(n1) = N1
q
 ∑

|h|≤ qXǫ′

N1
 ̂fN1( hn1
q ) ∑

c(q) ψ(c)e
( −ch
q ) + Oǫ′(X −100).

For h = 0, and ψ being the principal character the sum over c equals ϕ(q). In all other
cases, we can estimate it by O(
√P (h, q)), by Lemma 8.7. Thus,

K1 = KMT + O
 (X 1+2ǫ′P 3/2

QN1
 )
 .

This gives the lemma by the condition Ni ≥ X ǫ, Q ≤ (X/M )2/3−ǫ. □

Proof of Proposition 9.1. As we have the same arithmetic information available, the proof
can be done with Heath-Brown’s identity as in [21, Proof of Theorem 1.1]. The only
diﬀerence is the necessity for a ﬁner-than-dyadic dissection and a trivial bound for ranges
not covered completely, for which we gave the details in the proof of Proposition 8.1. □

Part IV. The Montgomery–Vaughan result with sieve weights

10. Proof of Key Proposition 3

Our goal in this section is to prove Key Proposition 3 assuming a few lemmas (Lem-
mas 10.2, 10.3, 10.4, 10.5 and 10.6) relating to singular series and “modiﬁed Gauß sums”
that will be proved in the next section.

10.1. Initial reduction

We start by noting that it suﬃces to consider only

m ≥ N P −c1.(96)

We furthermore can replace Λ in the deﬁnition of νi by

1n∈P log n =: Λ0(n),(97)

as the contribution of prime powers to ν1 ∗ ν2(m) can be trivially bounded by ≪ε N 1/2+ε.
To prove Key Proposition 3, we apply the circle method to the convolution

ν1 ∗ ν2(m) = ∫ 1

0 ̂ν1 ̂ν2(α)e(−αm) dα.

We use the same major and minor arc splitting as in Section 6.1. The minor arcs can
be handled just as in Section 6.3 (taking λ2(d) = 1d=1 there), so we conclude that for all
m ≤ N apart from O(N P −c1) exceptions we have

ν1 ∗ ν2(m) = ∫

M ̂ν1 ̂ν2(α)e(−αm) dα + O(N P −c1).

In contrast to the proof of Propositions 1 and 2, we need to asymptotically estimate
the summands over the moduli q in the expression of the major arc integral as
∫
M ̂ν1 ̂ν2(α)e(−αm) = ∑

q≤P c0
 ∑

a(q)∗ eq(−am) ∫
|η|≤Q−1 ̂ν1 ̂ν2(a/q + η)e(−ηm) dη.

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 61

By the conditions of Key Proposition 3, we may write

νi(n) = Λ0(n) ∑

d|n+2 λi(d),

where λi(d) is the product of the two sieve weights in the deﬁnition of the admissible pre-
sieve νi, i.e. one weight λ
†
i for the primes 3 ≤ p ≤ P , p ∤ ̃r and the sieve of Eratosthenes
weight µ for the primes p ≥ 3, p | ̃r. We recall that ̃r denotes the exceptional modulus, if
it exists, and ̃r = 1 otherwise.
Recall that by Deﬁnition 4.5 we may write the just mentioned sifting ranges as

̃P = ∏

p≥3
p|̃r
 p, P † := ∏

3≤p≤P
p∤̃r
 p.

We now analogously for n ≥ 1 write

̃n = ∏

p|n
p∈ ̃P
 pvp(n), n† = ∏

p|n
p∈P †
 pvp(n).(98)

Note that this only gives a factorisation n = ̃nn† if every prime divisor of n divides ̃PP †

(which happens if and only if n is P smooth and odd).
We need furthermore what we call modiﬁed Gauß sums, namely given a character χ to
the modulus q, we set

cχ(a, j) := ∑∗

b (mod q)
(b+2,rad(q))=(j,rad(q))
 χ(b)eq(ab), where rad(q) := ∏

p|q p.(99)

We will also encounter the sieve-theoretic sums

Si(q, j, e) := 1
ϕ(e)
 ∑

c,d
c|j,(d,qe)=1
 λi(cde)
ϕ(d)
(100)

and their restriction to divisors of P † given by

S†
i (q, j, e) := 1
ϕ(e†)
 ∑

c,d|P †
c|j,(d,qe)=1
 λ
†
i (cde†)
ϕ(d) .

Note that S†
i is invariant under replacing any of its arguments by their † components.
Both modiﬁed Gauß sums and the sieve-related sums will be studied in more detail later,
in Subsections 11.1 and 11.2, respectively.
Finally, deﬁne a modiﬁed Euler function that accounts for the fact that the sifted primes
only occupy p − 2 residue classes modulo a given prime p > 2, as

ϕ2(n) = n ∏

p|n(1 − 2/p)

and
 ϕ2(2
s) = ϕ(2
s).

With this notation, we are ready to state a technical decomposition of ̂νi(α) on the major
arcs.

62 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

Lemma 10.1 (A splitting of the major arc contribution). Let 1 ≤ a ≤ q ≤ P c0, (a, q) = 1.
We have
 ̂νi(a/q + η)

= V ( ̃P)
ϕ2(̃q)ϕ(q/̃q)
 ∑

j†|rad(q†)
l|q
 ∑

e|P † ̃P
(e,q)=1
el≤P 2c0
 µ(̃e)S†
i (q, j, e)
ϕ2(̃e)
 ∑

ψ(e)∗
χ(l)∗
 ψ(−2)c
χχ(q)
0 (a, j†)

× ∑

n≤N Λ0(n)χψ(n)e(ηn) + O(N P −c0/10),

where χ(q)
0 denotes the principal character (mod q).

Proof. Clearly it suﬃces to consider the case i = 1. We begin by translating ̂ν1(a/q + η)
to the language of Dirichlet characters. For (n, q) = 1, we have the Fourier expansion

eq(an) = 1
ϕ(q)
 ∑

b(q)
χ(q)
 eq(ab)χ(b)χ(n).

By orthogonality relations, for n, d odd we have

1d|n+2 = 1
ϕ(d)
 ∑

ψ(d) ψ(−2)ψ(n).

Recalling that we are only sieving for odd primes, the above together result in

̂ν1(a/q + η) = 1
ϕ(q)
 ∑

d
 λ1(d)
ϕ(d)
 ∑

ψ(d)
χ(q)
b(q)
 ψ(−2)eq(ab)χ(b) ∑

n≤N Λ0(n)χψ(n)e(ηn) + O(qN c),

where the error term accounts for those n that are not coprime to 2q and c = 1/100, say.
Note that d is always odd and squarefree in the support of λ1(d), and factorise d = d1d2,
where d1 | q and (d2, q) = 1. Split the sum over the characters ψ accordingly to reach

̂ν1(a/q + η)

= 1
ϕ(q)
 ∑

d1,d2
d1|q,(d2,q)=1
 λ1(d1d2)
ϕ(d1)ϕ(d2)
 ∑

ψ1(d1)
ψ2(d2)
 ∑

χ(q)
b(q)
 ψ1ψ2(−2)χ(b)eq(ab) ∑

n≤N Λ0(n)χψ1ψ2(n)e(ηn)

+ O(qN c).

To simplify, note that for any character χ′ (mod q) we have
∑

ψ1(d1),χ(q)
ψ1χ=χ′
 ψ1(−2)χ(b) = χ′(b) ∑

ψ1(d1) ψ1(−2)ψ1(b)

= χ′(b)ϕ(d1)1d1|b+2.

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 63

Summing over diﬀerent χ′ (mod q) gives us

̂ν1(a/q + η)

= 1
ϕ(q)
 ∑

d1|q,(d2,q)=1
 λ1(d1d2)
ϕ(d2)
 ∑

ψ2(d2)
χ(q)
b(q)
 ψ2(−2)χ(b)1d1|b+2eq(ab) ∑

n≤N Λ0(n)χψ2(n)e(ηn)

+ O(qN c).

Each pair of characters ψ2 and χ in above summation is induced by a unique pair of
primitive characters to some moduli e|d2 and l|q, respectively. We sort the characters
based on those, write d2 = de (with d, e necessarily coprime) and trivially estimate the
error from replacing ψ2, χ with their primitive parts in the n sum to obtain

̂ν1(a/q + η)

= 1
ϕ(q)
 ∑

l|q
 ∑

e
(e,q)=1
 ∑

d1|q,(d,qe)=1
 λ1(d1de)
ϕ(e)ϕ(d)
 ∑

ψ(e)∗
χ(l)∗
 ψ(−2) ∑

b(q) χχ(q)
0 (b)1d1|b+2eq(ab)

× ∑

n≤N Λ0(n)χψ(n)e(ηn) + O(qN c).

As λ1 is supported on squarefree integers only, for each ﬁxed b the summation condition
for d1, that is d1|q, d1|b+2, can be replaced by d1|(b+2, rad(q)). Writing j = (b+2, rad(q))
and sorting according to j|rad(q) gives us

̂ν1(a/q + η)

= 1
ϕ(q)
 ∑

j|rad(q)
l|q
 ∑

e
(e,q)=1
 ∑

d1|j,(d2,q)=1
 λ1(d1de)
ϕ(e)ϕ(d)
 ∑

ψ(e)∗
χ(l)∗
 ψ(−2) ∑

b(q)
(b+2,rad(q))=j
 χχ(q)
0 (b)eq(ab)

× ∑

n≤N Λ0(n)χψ(n)e(ηn) + O(qDN c)

= 1
ϕ(q)
 ∑

j|rad(q)
l|q
 ∑

e
(e,q)=1
 S1(q, j, e) ∑

ψ(e)∗
χ(l)∗
 ψ(−2)c
χχ(q)
0 (a, j) ∑

n≤N Λ0(n)χψ(n)e(ηn) + O(qN c),

with the notation from (99) and (100).
We next bound the contribution of terms with el > P 2c0. By the choice of sieves,
S(q, j, e) vanishes if e > D0P 2c0. By trivial estimates and combining χ, ψ into one char-
acter, we have

1
ϕ(q)
 ∑

j|rad(q)
l|q
 ∑

e
(e,q)=1
el>P 2c0
 S1(q, j, e) ∑

ψ(e)∗
χ(l)∗
 ψ(−2)c
χχ(q)
0 (a, j) ∑

n≤N Λ0(n)χψ(n)e(ηn)

≪ε q1/2+ε ∑

P 2c0 ≤e≤D0P 3c0
χ(e)∗
 1
ϕ(e)
 ∣
∣
∣ ∑

n≤N Λ0(n)χ(n)e(ηn)
∣
∣
∣.

64 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

After reinserting again higher prime powers and dealing with the exponential phase as in
(41), we can apply Lemma 6.6 and Cauchy–Schwarz to give the upper bound

N q1/2+ε(log N )
O(1)P −2c0/3 ≪ N P −c0/10.

To ﬁnish the proof of the lemma, it remains to separate the contribution of the two
sieves in the deﬁnition of λi. The sieve weights λi are composed of two sieve weights, λ
†
1
and µ, with the ranges P † and ̃P as given in Deﬁnition (4.5). Note that e must be odd
and squarefree whenever S1(q, j, e) ̸= 0, and write e = e†̃e, where e†, ̃e are as in (98), and
similarly for j and all other variables that occur. For j | rad(q), we get

S1(q, j, e) = 1
ϕ(e†)ϕ(̃e)
 ∑

d
†
1,d†|P
d
†
1|j†,(d†,e†q)=1
 λ†
1(d
†
1e†d†)
ϕ(d†)
 ∑

̃d1, ̃d| ̃P
̃d1|̃j,( ̃d,̃eq)=1
 µ( ̃d1̃e ̃d)

ϕ( ̃d) .

The sum over ̃d1 vanishes unless ̃j = 1. If ̃j = 1, then

1
ϕ(̃e)
 ∑

̃d1, ̃d| ̃P
̃d1|̃j,( ̃d,̃eq)=1
 µ( ̃d1̃e ̃d)

ϕ( ̃d) = µ(̃e)
ϕ(̃e)
 ∏

p| ̃P
p∤̃eq
 (1 − 1
p − 1
 ) = µ(̃e)ϕ(̃q)V ( ̃P)
ϕ2(̃q)ϕ2(̃e) .

Having simpliﬁed S1(q, j, e), we return to studying ̂ν1. We arrive at

̂ν1(a/q + η)

= V ( ̃P)
ϕ2(̃q)ϕ(q/̃q)
 ∑

j†|rad(q†)
l|q
 ∑

e|P † ̃P
(e,q)=1
el≤P 2c0
 µ(̃e)S†
1(q†, j†, e†)
ϕ2(̃e)
 ∑

ψ(e)∗
χ(l)∗
 ψ(−2)c
χχ(q)
0 (a, j†)

× ∑

n≤N Λ0(n)χψ(n)e(ηn) + O(N P −c0/10),

which we can lastly simplify by recalling that S†
1(q†, j†, e†) = S†
1(q, j, e). □

We expect the contribution of ∑n≤N Λ0(n)χψ(n)e(ηn) in Lemma 10.1 to be small for

|η| ≤ Q−1 for any given pair of primitive characters, except when χψ = χ(1)
0 is the trivial
character or when χψ = ̃χ is the exceptional character. We deﬁne the exponential sums

T (η) := ∑

n≤N e(ηn)

̃T (η) := − ∑

n≤N n ̃β−1e(ηn)

W (χψ, η) := ∑

n≤N Λ0(n)χψ(n)e(ηn) − 1
χψ=χ(1)
0 T (η) − 1χψ=̃χ ̃T (η)

corresponding to the expected contribution of the trivial character, the Siegel character,
and the remainder to ∑n≤N Λ0(n)χψ(n)e(ηn).

In the decomposition given by Lemma 10.1, the cases χψ = χ(1)
0 and χψ = ̃χ can
respectively only happen if e = l = 1 and el = ̃r, since (e, l) = 1 and the ψ, χ are
primitive. Let 2t||̃r. As the exceptional character is quadratic and primitive, we note

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 65

that t ∈ {0, 2, 3} and that ̃r/2t = ̃P. As e is odd and (e, q) = 1, the statement el = ̃r is
equivalent to l = 2trad(̃q) and e = ̃r/(2trad(̃q)). In particular, this can happen only if 2t|q
and e† = 1. These considerations motivate the following deﬁnitions. Write

q′ := 2
trad(̃q)(101)

and set
 νT
1 (a, q, η) := V ( ̃P)
ϕ2(̃q)ϕ(q/̃q)
 ∑

j|q† S†
1(q, j, 1)c
χ(q)
0 (a, j)T (η),

ν ̃T
1 (a, q, η) := 12t|q ̃χ(̃r/q′)(−2)µ(̃r/q′)V ( ̃P)
ϕ2(̃q)ϕ2(̃r/q′)ϕ(q/̃q)
 ∑

j|q† S†
1(q, j, 1)c̃χ(q′ )χ(q)
0 (a, j) ̃T (η),

where, following the notation given in (9), we denote by ̃χ(̃r/q′) and ̃χ(q′) the ̃r/q′ and q′

component of the exceptional character, respectively. We deﬁne further the part of ν1 that
remains after subtracting these terms as

νW
1 (a, q, η) := ̂ν1(a/q + η) − νT
1 (a, q, η) − ν ̃T
1 (a, q, η)

= V ( ̃P)
ϕ2(̃q)ϕ(q/̃q)
 ∑

j|q†
l|q
 ∑

e|P † ̃P
(e,q)=1
el≤P 2c0
 µ(̃e)S†
1(q, j, e)
ϕ2(̃e)
 ∑

ψ(e)∗
χ(l)∗
 ψ(−2)c
χχ(q)
0 (a, j)W (χψ, η).

We use this decomposition and Lemmas 6.1, 10.1 to get for m ≤ N outside a set of size
O(N P −c1) that
∫
M ̂ν1 ̂ν2(α)e(−αm) dα

= ∑

q≤P c0
a(q)∗
 eq(−am) ∫
|η|≤Q−1
(
νT
1 (a, q, η) + ν ̃T
1 (a, q, η) + νW
1 (a, q, η)
)

× (νT
2 (a, q, η) + ν ̃T
2 (a, q, η) + νW
2 (a, q, η)
)e(−ηm) dη + O(N P −c1).

(102)

We split this up into two parts, the main term that consists out of all those pairs that
do not contain the superscript W , and the remaining error term. It will make matters
easier if we enlarge the range of q for the main terms, in the case the exceptional zero
exists, from {q : q ≤ P c0} to {q = 2s̃qq† : ̃q|̃r, 2sq† ≤ P c0} =: Q, say. To justify this,
note that c
χ(q)
0 (a, j) respectively c̃χ(q′)χ(q)
0 (a, j) vanish if ̃q has a square prime divisor and

(j, ̃q) = 1. Furthermore in the added non-overlapping intervals we have q > P c0 and the
estimate
 max
q∈Q,q>P c0{|νT
i (a, q, η)|, |ν ̃T
2 (a, q, η)|} ≤ N (log N )
O(1)P −c0/3

that follows from the trivial estimates |T (η)|, | ̃T (η)| ≤ N . Thus, by Lemma 6.1 for all
m outside a suﬃciently small exceptional set, this larger range main term approximates
the previous one with an admissible error term. In the same way also the error term of
Lemma 10.1 can be handled.

66 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

Now, to ﬁnish the proof of Key Proposition 3, it suﬃces to show that there exist
functions M(m) and E(m) as proposed, such that

∑

q∈Q
a(q)∗
 eq(−am) ∫
|η|≤Q−1
(
νT
1 (a, q, η) + ν ̃T
1 (a, q, η)
) · (
νT
2 (a, q, η) + ν ̃T
2 (a, q, η)
)e(−ηm) dη

= mV (P )
2S(m) (M(m)
(1 + O(e
−c log D0
log P )) + O(e
100
√log N P −c))

(103)

and for i ∈ {1, 2}

∣
∣
∣ ∑

q≤P c0
a(q)∗
 eq(−am) ∫

|η|≤Q−1 νW
i (a, q, η) · (νT
i+1(a, q, η) + ν ̃T
i+1(a, q, η) + νW
i+1(a, q, η)
)e(−ηm) dη∣
∣
∣

≪ mV (P )
2S(m)e
−c log N
log P E(m),

(104)

where the index i + 1 is taken (mod 2).

10.2. Main term

In this subsection, we give the desired asymptotic evaluation (103) of the contribution
of products of all terms in (102) that do not contain a superscript W . To do this, we ﬁrst
need to introduce some auxiliary quantities and some lemmas about them whose proofs
are postponed to the next section.
Let χ1 and χ2 be characters to the modulus q and deﬁne

F (χ1, χ2, j1, j2, m) := ∑∗

a(q) cχ1(a, j1)cχ2(a, j2)eq(−am).(105)

We recall the notation in (9). The following lemmas tell us that F is multiplicative and
that it vanishes if the modulus has a square divisor that is not shared by both conductors
of χ1, χ2.

Lemma 10.2 (F is multiplicative). Let χ1 and χ2 be characters to the modulus q and
factorise χi as in (9). Then we have

F (χ1, χ2, j1, j2, m) = ∏

p|q F (χ(pα1(p))
1 , χ(pα2(p))
2 , j1, j2, m).

Lemma 10.3. If pα || q for some α > 1, we have

F (χ1, χ2, j1, j2, m) = 0 unless α
∗
1(p) = α
∗
2(p) = α.(106)
 THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 67

Now, with F as in (105), we can write
∑

a(q)∗ νT
1 (a, q, η)νT
2 (a, q, η)eq(−am)

= V ( ̃P)2T (η)2

ϕ2(̃q)2ϕ(q/̃q)2 ∑

ji|q† S†
1(q, j1, 1)S†
2(q, j2, 1) ∑

a(q)∗ c
χ(q)
0 (a, j1)c
χ(q)
0 (a, j2)eq(−am)

= V ( ̃P)2T (η)2

ϕ2(̃q)2ϕ(q/̃q)2 ∑

ji|q† S†
1(q, j1, 1)S†
2(q, j2, 1)F (χ(q)
0 , χ(q)
0 , j1, j2, m).

Lemma 10.3 gives that F (χ(q)
0 , χ(q)
0 , j1, j2, m) = 0 unless q is squarefree. We can factorise
it by Lemma 10.2 as

F (χ(q)
0 , χ(q)
0 , j1, j2, m) = F (χ(q†)
0 , χ(q†)
0 , j1, j2, m)F (χ(q/q†)
0 , χ(q/q†)
0 , 1, 1, m),

where we used that ji divides q† and so is coprime to q/q†.
We arrive at
∑

a(q)∗ νT
1 (a, q, η)νT
2 (a, q, η)eq(−am)

= V ( ̃P)2T (η)2F (χ(q/q†)
0 , χ(q/q†)
0 , 1, 1, m)
ϕ2(̃q)2ϕ(q/̃q)2 ∑

ji|q† S†
1(q, j1, 1)S†
2(q, j2, 1)F (χ(q†)
0 , χ(q†)
0 , j1, j2, m)

= V ( ̃P)2T (η)2F (χ(q/q†)
0 , χ(q/q†)
0 , 1, 1, m)
ϕ2(̃q)2ϕ(q/̃q)2 F(q†, m),

say. We follow the same steps for νT
1 ν ̃T
2 and observe that the q† component of ̃χ(̃q)χ(q)
0 is

χ(q†)
0 . We get
∑

a(q)∗ νT
1 (a, q, η)ν ̃T
2 (a, q, η)eq(−am)

= 12t|q ̃χ(̃r/q′)(−2)µ(̃r/q′)V ( ̃P)2T (η) ̃T (η)F (χ(q/q†)
0 , ̃χ(q′)χ(q/q†)
0 , 1, 1, m)
ϕ2(̃q)2ϕ2(̃r/q′)ϕ(q/̃q)2 F(q†, m),

and as F (χ1, χ2, 1, 1, m) = F (χ2, χ1, 1, 1, m) we also have the same formula for
∑

a(q)∗ ν ̃T
1 (a, q, η)νT
2 (a, q, η)eq(−am).

We recall that ̃r/q′ is odd and squarefree, so µ(̃r/q′)2 = 1 and, since ̃χ is a quadratic

character, ̃χ(̃r/q′)2(−2) = 1. We get
∑

a(q)∗ ν ̃T
1 (a, q, η)ν ̃T
2 (a, q, η)eq(−am)

= 12t|q V ( ̃P)2 ̃T (η)2F (̃χ(q′)χ(q/q†)
0 , ̃χ(q′)χ(q/q†)
0 , 1, 1, m)
ϕ2(̃q)2ϕ2(̃r/q′)2ϕ(q/̃q)2 F(q†, m).

68 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

Combining these, we see that the left-hand side of (103) is

V ( ̃P)
2 ∑

q∈Q F(q†, m) ∫
|η|≤Q−1
( T (η)2F (χ(q/q†)
0 , χ(q/q†)
0 , 1, 1, m)
ϕ2(̃q)2ϕ(q/̃q)2

+ 12t|q 2̃χ(̃r/q′)(−2)µ(̃r/q′)T (η) ̃T (η)F (χ(q/q†)
0 , ̃χ(q′)χ(q/q†)
0 , 1, 1, m)
ϕ2(̃q)2ϕ2(̃r/q′)ϕ(q/̃q)2

+ 12t|q ̃T (η)2F (̃χ(q′)χ(q/q†)
0 , ̃χ(q′)χ(q/q†)
0 , 1, 1, m)
ϕ2(̃q)2ϕ2(̃r/q′)2ϕ(q/̃q)2
 )
e(−ηm) dη.

(107)

We now apply the factorisation q = 2s ̃qq† to get

F (χ(q/q†)
0 , χ(q/q†)
0 , 1, 1, m)
ϕ2(̃q)2ϕ(q/̃q)2 = F (χ0,2s ̃q, χ0,2s ̃q, 1, 1, m)
ϕ2(2s ̃q)2 1
ϕ(q†)2 =: L1(2
s ̃q, m) 1
ϕ(q†)2

and
 2̃χ(̃r/q′)(−2)µ(̃r/q′)F (χ(q/q†)
0 , ̃χ(q′)χ(q/q†)
0 , 1, 1, m)
ϕ2(̃q)2ϕ2(̃r/q′)ϕ(q/̃q)2

= 2̃χ(̃r/q′)(−2)µ(̃r/q′)F (χ0,2s ̃q, ̃χ(q′)χ0,2s ̃q, 1, 1, m)
ϕ2(2s ̃q)ϕ2(̃r) 1
ϕ(q†)2

=: L2(2
s ̃q, m) 1
ϕ(q†)2

and
 F (̃χ(q′)χ(q/q†)
0 , ̃χ(q′)χ(q/q†)
0 , 1, 1, m)
ϕ2(̃q)2ϕ2(̃r/q′)2ϕ(q/̃q)2 = F (̃χ(q′)χ0,2s ̃q, ̃χ(q′)χ0,2s ̃q, 1, 1, m)
ϕ2(̃r)2 1
ϕ(q†)2

=: L3(2
s ̃q, m) 1
ϕ(q†)2 ,

say.
By Lemma 10.3 L1(2s ̃q) vanishes if s > 1, L2(2s ̃q) vanishes unless s = t = 0 (as t ̸= 1),
and L3(2s ̃q) vanishes unless s = t. Therefore, with the just introduced notation and the
fact that t ≤ 3, (107) becomes

V ( ̃P)
2 ∑

q∈Q
 F(q†, m)
ϕ(q†)2
 ∫
|η|≤Q−1
(
1s≤1T (η)
2L1(2
s ̃q, m)

+ 1s=t=0T (η) ̃T (η)L2(2
s ̃q, m) + 1s=t ̃T (η)
2L3(2
s ̃q, m)
)e(−ηm) dη

= V ( ̃P)
2 ∫

|η|≤Q−1
 ∑

s≤3
̃q| ̃P
 (
1s≤1T (η)
2L1(2
s ̃q, m)

+ 1s=t=0T (η) ̃T (η)L2(2
s ̃q, m) + 1s=t ̃T (η)
2L3(2
s ̃q, m)
)e(ηm) dη ∑

q†≤P c0 /2s
 F(q†, m)
ϕ(q†)2 ,

(108)

At this point it was helpful that the integration range is independent of q.

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 69

We now evaluate the sum over q† in (108). It is in this evaluation that the singular
series appears. The relevant local factors are

σ(p, m) := F (χ(p)
0 , χ(p)
0 , 1, 1, m)(109)

and the singular series is given by

S(m) := ∏

p
 (1 + σ(p, m)
ϕ2(p)2
 )
.(110)

As we sieve separately for the exceptional modulus and 2, we also require notation for the
partial singular series given by

S(m, 2 ̃P) := ∏

p|2 ̃P
(1 + σ(p, m)
ϕ2(p)2
 )
.

With this notation, we postulate the following evaluation for the sum over q† in (108).
It will be proved in Section 11.3 and can be seen as a combination of the typical completion
of the singular series in the circle method with a fundamental lemma of sieve theory.

Lemma 10.4. Let the notation be as before and assume P ′ ≤ P c0. We have

∑

q†≤P ′
 F(q†, m)
ϕ(q†)2 = V (P †) S(m)

S(m, 2 ̃P )
 (1 + O(
e
−c log D0
log P + e
100
√log N (P ′)
−1)
) .

We recall that V (P †)V ( ̃P) = V (P) so that an application of Lemma 10.4 tells us
that (108) is

= V (P)
2 S(m)

S(m, 2 ̃P)
 ∫

|η|≤Q−1
 ∑

s≤3
̃q| ̃P
 (
1s≤1T (η)
2L1(2
s ̃q, m) + 1s=t=0T (η) ̃T (η)L2(2
s ̃q, m)

+ 1s=t ̃T (η)
2L3(2
s ̃q, m)
)
e(ηm) dη × (
1 + O(e
−c log D0
log P + e
100
√log N P −c0))
(111)

We can complete the integrals over η to obtain
∫

|η|≤Q−1 T (η)
2e(−ηm) dη = ∫ 1

0 T (η)
2e(−ηm) dη + O(Q) = m + O(Q)(112)
 ∫
|η|≤Q−1 ̃T (η)T (η)e(−ηm) dη = ∫ 1

0 ̃T (η)T (η)e(−ηm) dη + O(Q) =: ̃J(m) + O(Q)(113)
 ∫

|η|≤Q−1 ̃T (η)
2e(−ηm) dη = ∫ 1

0 ̃T (η)
2e(−ηm) dη + O(Q) =: ̃I(m) + O(Q).(114)

To prove (112), note that by the geometric sum formula we have |T (η)| ≪ Q for η ∈
[−1/2, 1/2], |η| ≥ 1/Q, and then claim follows by crudely apply the triangle inequality to
the integral over [−1/2, 1/2] \ [−1/Q, 1/Q]. To prove (113) and (114), we argue essentially
in the same way; partial summation gives | ̃T (η)| ≪ Q for η ∈ [−1/2, 1/2] \ [−1/Q, 1/Q],
and then we can again apply a crude pointwise bound.

70 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

We can now deﬁne the main term function M(m) that appears in Proposition 3 and
in (103) as

M(m) := 1

mS(m, 2 ̃P)
 ∑

s≤3
̃q| ̃P
 (1s≤1mL1(2
s ̃q, m) + 1s=t=0 ̃J(m)L2(̃q, m) + 1s=t ̃I(m)L3(2
t ̃q, m)
).

With this deﬁnition, (112), (113), (114), the trivial estimates | ̃J (m)|, |̃I(m)| ≤ N , and
recalling that Q = N P −c0, we see that (111) is

V (P)S(m)
(mM(m)
(1 + O(e
−c log D0
log P )
)

+ O( N eO(
√log N )

P c0S(m, 2 ̃P)
 (∣
∣
∑

s≤1
̃q| ̃P
 L1(2
s ̃q, m)
∣
∣ + ∣
∣
∑

̃q| ̃P L2(̃q, m)
∣
∣ + ∣
∣
∑

̃q| ̃P L3(2
t ̃q, m)
∣
∣)))
(115)

To complete our treatment of the main term, it remains to show that M(m) is as required
in Key Proposition 3 (see (14) and (15)) and to estimate the error term in (115). Both
are achieved if we understand the relation of the sums over Li to S(m, 2 ̃P ).
The functions Li are can be expressed in terms of the local contribution of the excep-
tional modulus and the prime 2 to the binary additive problem. More precisely, if we
deﬁne
 σ′(p, m) := F (χ(p)
0 , ̃χ(p), 1, 1, m)(116)
 ̃σ(p, m) :=
 {
F (̃χ(p), ̃χ(p), 1, 1, m) if p ̸= 2,
F (̃χ(2t), ̃χ(2t), 1, 1, m) if p = 2,
(117)

then by multiplicativity (Lemma 10.2) and the vanishing at higher prime powers (Lemma 10.3)
we have
 L1(2
s ̃q) = 1s≤1|µ(̃q)| ∏

p|2s ̃q
 σ(p, m)
ϕ2(p)2

|L2(̃q)| = |µ(̃q)| 1
ϕ2(̃r)
 ∏

p|̃q
 |σ′(p, m)|
ϕ2(p)

L3(2
t̃q) = |µ(̃q)| 1
ϕ2(̃r)2 ∏

p|2t̃q ̃σ(p, m).

Therefore, we get ∑

s≤1
̃q| ̃P
 L1(2
s ̃q) = ∏

p|2 ̃P
(
1 + σ(p, m)
ϕ2(p)2
 ) = S(m, 2 ̃P)

∣
∣
∑

̃q| ̃P L2(̃q)
∣
∣ ≤ ∏

p| ̃P
 (1 + |σ′(p,m)|
p−2 )

p − 2

∑

̃q| ̃P L3(2
t ̃q) = ̃σ(2, m)
ϕ(2t)2 ∏

p| ̃P
 1 + ̃σ(p, m)
(p − 2)2 .

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 71

The following lemma gives explicitly the value of the three versions of σ. It is proved
in Section 11.1 and also conﬁrms that the singular series matches the one in Key Propo-
sition 3.

Lemma 10.5 (Evaluation of main term local densities). Let p > 2 be a prime. We have

σ(p, m) =
 



p − 4 if p | m or p | m + 4
2p − 4 if p | m + 2
−4 else,
(118)
 σ′(p, m) =
 



−p(̃χp(m) + ̃χp(−2) − ̃χp(m + 2)) − ̃χp(−2) − ̃χp(2) if p | m + 2
−p(̃χp(m) + ̃χp(2) − ̃χp(m + 2)) − ̃χp(−2) − ̃χp(2) if p | m + 4
−p(̃χp(m) − ̃χp(m + 2)) − ̃χp(−2) − ̃χp(2) else,
(119)
 ̃σ(p, m) =
 



(p2 − 3p)̃χp(−1) − 1 if p | m
p(−̃χp(−1) − 2̃χp(2) − 1) − 1 if p | m + 4
p̃χp(−1)(−1 − 2̃χp(2m + 4)) − 1 else.
(120)

We have furthermore
 σ(2, m) =
 {
1 if 2 | m
−1 else,
(121)
 |̃σ(2, m)| ≤
 {
22t−1 if 2 | m
0 else.
(122)

With this evaluation, a short calculation shows that for p | m, p ̸= 2
∣
∣
∣ 1 + ̃σ(p, m)
(p − 2)2
 ∣
∣
∣ = 1 + σ(p, m)
(p − 2)2(123)

and, applying a straightforward estimate for p > 7 and a character table for quadratic
characters for primes up to 7, for p ∤ m, p ̸= 2
∣
∣
∣ 1 + ̃σ(p, m)
(p − 2)2
 ∣
∣
∣
(1 + σ(p, m)
(p − 2)2
 )−1 ≤ 21
25 .

Similarly we get for 2 | m ∣
∣
∣ ̃σ(2, m)
ϕ(2t)2
 ∣
∣
∣ ≤ 2 = 1 + σ(p, m).

Together with the simple bound ̃J(m) ≤ m, the evaluation for σ′(p, m) in (119), and
the inequality ̃I(m) ≤ m ̃β we get consequently

M(m) ≥ 1 − m ̃β−1 ∏

p|̃r
p∤m
 21
25 + O(̃r−0.99).

Here the second and third term are not present in the absence of an exceptional modulus
and we have M(m) = S(m,2)
S(m,2) = 1 in that case. This conﬁrms the proposed behaviour of
the function M(m).

72 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

Finally, we consider the error term in (115). By the same considerations as for M(m),
the sums over s, ̃q are O(S(m, 2 ̃P )) and so the error is admissible, recalling that we consider
m ≥ N P −c1.

10.3. Error term

In this subsection we establish (104). By deﬁnition,

∑

a(q)∗ νW
1 (a, q, η)νW
2 (a, q, η)eq(−am)

= V ( ̃P)2

ϕ2(̃q)2ϕ(q/̃q)2 ∑

ji|q†
li|q
 ∑

ei|P † ̃P
(ei,q)=1
eq≤P 2c0
 µ(̃e1)µ(̃e2)S†
1(q, j1, e1)S†
2(q, j2, e2)
ϕ2(̃e1)ϕ2(̃e2)

× ∑

ψi(ei)∗
χ(li)∗
 ψ1(−2)ψ2(−2)F (χ1χ(q)
0 , χ2χ(q)
0 , j1, j2, m)W (χ1ψ1, η)W (χ2ψ2, η).

For a primitive character ξ, put

W (ξ) := (∫
|η|≤Q−1 |W (ξ, η)|
2 dη)1/2.

This is a larger range of integration than in the analogous integral in [23, formula (6.5)],
but the proof there would go still go through with this wider choice of major arcs and,
just as for the main term, the fact that we chose the range of integration independent of
q again simpliﬁes matters for us.
An application of the Cauchy–Schwarz inequality gives

∑

q≤P c0
a(q)∗
 eq(−am) ∫
|η|≤Q−1 νW
1 (a, q, η)νW
2 (a, q, η)e(−ηm) dη

≤V ( ̃P)
2 ∑

q≤P c0
 1
ϕ2(̃q)2ϕ(q/̃q)2 ∑

ji|q†
li|q
 ∑

ei|P † ̃P
(ei,q)=1
eili≤P 2c0
 |S†
1(q, j1, e1)S†
2(q, j2, e2)|
ϕ2(̃e1)ϕ2(̃e2)

× ∑

ψi(ei)∗
χ(li)∗
 |F (χ1χ(q)
0 , χ2χ(q)
0 , j1, j2, m)| W (χ1ψ1)W (χ2ψ2).

(124)

Just as in the previous subsection we can use Lemma 10.2 to split F into factors over
divisors of P † and ̃P and write q = 2s̃qq†. We furthermore discard the range condition

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 73

2s̃qq† < P c0 to see that (124) is

≤ V ( ̃P)
2 ∑

2s ̃qq†
 ∑

ji|q†
li|q
 ∑

ei|P † ̃P
(ei,q)=1
eili≤P 2c0
 ∑

ψi(ei)∗
χ(li)∗
 |F (χ(l†
1)
1 χ(q†)
0 , χ(l†
2)
1 χ(q†)
0 , j1, j2, m)||S†
1(q, j1, e1)S†
2(q, j2, e2)|
ϕ(q†)2

× |F (χ( ̃l12s)
1 χ(̃q2s)
0 , χ( ̃l22s)
2 χ(̃q2s)
0 , 1, 1, m)|
ϕ2(̃q2s)2ϕ2( ̃e1)ϕ2( ̃e2) W (χ1ψ1)W (χ2ψ2).

(125)

Each ξi := χiψi is a primitive character to the modulus gi := eili ≤ P 2c0. We sort after
ﬁxed pairs ξ1, ξ2 to see that (125) is

≤ V ( ̃P)
2 ∑

gi≤P 2c0
ξi(gi)∗
 ̃G(ξ1, ξ2, m)G†(ξ1, ξ2, m)W (ξ1)W (x2),(126)

where

̃G(ξ1, ξ2, m) := ∑

eili=2gi(2)̃gi
ei| ̃P
 1
ϕ2(e1)ϕ2(e2)
 ∑

q|(2 ̃P)∞
li|q
(q,e1e2)=1
 |F (ξ(l1)
1 χ(q)
0 , ξ(l2)
2 χ(q)
0 , 1, 1, m)|
ϕ2(q)2 ,

(127)

G†(ξ1, ξ2, m) := ∑

eili=g†
i
ei|P †
 ∑

q|(P †)∞
li|q
(q,e1e2)=1
 ∑

ji|q
 |S†
1(q, j1, e1)S†
2(q, j2, e2)F (ξ(l1)
1 χ(q)
0 , ξ(l2)
2 χ(q)
0 , j1, j2, m)|
ϕ(q)2 .

(128)

Here 2gi(2) denotes the 2 component of gi. The product G†(ξ1, ξ2, m) ̃G(ξ1, ξ2, m) can be
seen as a sieve-weighted pseudo-singular series induced by the pair ξ1, ξ2. We can bound
it by the following Lemma that is proved in Subsection 11.3. It is our analogue of [23,
Lemma 5.5].

Lemma 10.6. Let ξi be primitive characters. We have

̃G(ξ1, ξ2, m)G†(ξ1, ξ2, m) ≪ V (P †)
2S(m).(129)

Applying this lemma, we ﬁnd that (126) is

≪ V (P)
2S(m)W 2,

where
 W := ∑

g≤P 2c0
ξ(g)∗
 W (ξ).(130)

Since ∫ 1

0 |T (η)|
2 dη ≪ N, ∫ 1

0 | ̃T (η)|
2 dη ≪ N,

74 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

and we can also apply Lemma 10.6 if one of the characters is primitive modulo 1 or the
exceptional character, we similarly estimate
∑

q≤P c0
a(q)∗
 eq(−am) ∫
|η|≤Q−1 νT
1 (a, q, η)νW
2 (a, q, η)e(−ηm) dη ≪ V (P)
2S(m)N 1/2W

∑

q≤P c0
a(q)∗
 eq(−am) ∫
|η|≤Q−1 ν ̃T
1 (a, q, η)νW
2 (a, q, η)e(−ηm) dη ≪ V (P)
2S(m)N 1/2W .

Of course the same holds for the contribution of νW
1 with νT
2 or ν ̃T
2 .
It remains to bound W . For this we use Gallagher’s prime number theorem.

Lemma 10.7 (Gallagher’s prime number theorem). Let N ≥ R ≥ 2. Then
∑

q≤R
 ∑

χ(q)∗ max
h<x≤N 1
h + N/R
 ∣
∣ ∑#

x−h≤n≤x χ(n)Λ0(n)
∣
∣ ≪ e
−c log N
log R ,(131)

where the # in summation denotes that if q = 1 we need to subtract from the sum the
term ∑

x−h≤n≤x 1,

and if there is an exceptional zero ̃β of level R, then for χ = ̃χ being the exceptional
character we need to subtract
 − ∑

x−h≤n≤x n ̃β−1,

and the bound on the right of (131) may be improved by a factor of

(1 − ̃β)(log R).

Proof. This is [23, Lemma 4.3]. □

We follow the strategy in [23, Section 7]. By Gallagher’s Lemma [23, Lemma 4.2] and
the fact that we accounted for the possible exceptional zero, we have

W (ξ) ≪ (∫ 2N

0
 1
Q
 ∣
∣ ∑#

n≤N
|n−x|≤Q
 ξ(n)Λ0(n)
∣
∣2 dx)1/2

≪ N 1/2 max
x≤2N 1
Q
 ∣
∣
∣ ∑#

n≤N
|n−x|≤Q
 ξ(n)Λ0(n)
∣
∣
∣.

Applying Lemma 10.7 with R = P 2c0 (and recalling (130)) gives us

W ≪ N 1/2 ∑

g≤P 2c0 D0
ξ(g)∗
 max
x≤2N 1
Q
 ∣
∣
∣ ∑#

n≤N
|n−x|≤Q
 ξ(n)Λ0(n)
∣
∣
∣

≪ N 1/2e
−c log N
log P c0

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 75

if there is no exceptional modulus. If the exceptional zero does exist we get the improved
estimate
 W ≪ N 1/2(1 − ̃β)(log P c0)e
−c log N
log P c0 .

As c0 is ﬁxed, this concludes the proof of (104) and also Proposition 3, under the assump-
tion of Lemmas 10.2, 10.3, 10.4, 10.5 and 10.6 whose proofs are postponed to the next
section.
 11. Auxiliary results

The goal of this section is to prove several auxiliary results that were used in the previous
section in the proof of Key Proposition 3.

11.1. Gauß Sums with gcd condition

In this subsection we consider the modiﬁed Gauß sums cχ(a, j) and the related function
F (χ1, χ2, j1, j2, m) deﬁned in (99) and (105) respectively.
We now introduce some more notation to handle the remaining statements. We write
c
χ(q)
0 (a, j) = cq(a, j) if χ is principal. As usual, we also use cχ(a) := ∑b(q)∗ χ(b)eq(ab)

to denote the Gauß sum without a gcd condition and write c
χ(q)
0 (a) = cq(a) (which is a

Ramanujan sum). We use the placeholder ’−’ in place of ji in F (χ1, χ2, j1, j2, m) to denote
that the corresponding Gauß sum has no gcd restriction. For example, this means that

F (χ1, χ2, −, j2, m) := ∑

a(q)∗ cχ1(a)cχ2 (a, j2)eq(−am).

We follow the usual notation and write

τ (χ) := cχ(1).

We start by proving the stated multiplicativity of F .

Proof of Lemma 10.2. Let r, s be coprime integers with q = rs. It suﬃces to show that

F (χ1, χ2, j1, j2, m) = F (χ(r)
1 , χ(r)
2 , j1, j2, m)F (χ(s)
1 , χ(s)
2 , j1, j2, m)

We observe
χi(bi)1(bi+2,q′)=(ji,q′) = χ(r)
i (bi)1(bi+2,r′)=(ji,r′)χ(s)
i (bi)1(bi+2,s′)=(ji,s′).

The lemma now follows from the Chinese remainder theorem since

F (χ1, χ2, j1, j2, m) = ∑

b1,b2(q) χ1(b1)1(b1+2,q′)=(j1,q′)χ2(b2)1(b2+2,q′)=(j2,q′)cq(b1 + b2 − m),

all appearing functions are suitably periodic, and cq(b1 + b2 − m) is multiplicative in q. □

By the principle of inclusion-exclusion we can rearrange the gcd condition. In particular,
if χi are characters whose modulus is a power of p, to calculate F (χ1, χ2, j1, j2, m) we
observe that
 cχi(a, 1) = cχi(a) − cχi(a, p)(132)

and so

F (χ1, χ2, 1, 1, m) = F (χ1, χ2, −, −, m) − F (χ1, χ2, −, p, m) − F (χ1, χ2, p, −, m) + F (χ1, χ2, p, p)
(133)

76 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

and
 F (χ1, χ2, 1, p, m) = F (χ1, χ2, −, p, m) − F (χ1, χ2, p, p, m).(134)

To make use of these decompositions, we recall Lemma 8.7. We can now prove the formu-
las for σ(p, m), σ′(p, m), ̃σ(p, m) that were used for the main term evaluation in Subsec-
tion 10.2. We also prove the following closely related result.

Lemma 11.1. Let p ̸= 2. We have

F (χ(p)
0 , χ(p)
0 , p, 1, m) =
 {
−p + 2 if p | m + 2 or p | m + 4
2 else,
(135)
 F (χ(p)
0 , χ(p)
0 , p, p, m) =
 {
p − 1 if p | m + 4
−1 else.
(136)

Proof of Lemma 10.5 and Lemma 11.1. For arbitrary characters χ1, χ2 to the modulus p
by (133) we have

F (χ1, χ2, 1, 1, m) = ∑

a(p)∗
bi(p)
 χ1(b1)χ2(b2)ep(a(b1 + b2 − m))

− χ1(−2) ∑

a(p)∗
b2(p)
 χ2(b2)ep(a(−2 + b2 − m))

− χ1(−2) ∑

a(p)∗
b1(p)
 χ1(b1)ep(a(b1 − 2 − m))

+ χ1χ2(−2) ∑

a(p)∗ ep(a(−4 − m))

= τ (χ1)τ (χ2)cχ1χ2(−m) − χ1(−2)τ (χ2)cχ2(−m − 2)

− χ2(−2)τ (χ1)cχ1(−m − 2) + χ1χ2(−2)cp(−m − 4).

If χ1 = χ2 = χ(p)
0 then τ (χi) = −1 and (118) follows from Lemma 8.7. For the case
χ1 = χ2 = χ for some quadratic character χ, we have

F (χ, χ, 1, 1, m) = τ (χ)
2cp(−m) − 2χ(−2)τ (χ)cχ(−m − 2) + cp(−m − 4)

Note that χ is primitive and so by Lemma 8.7 we get that cχ(−m − 2) = 0 if p | m + 2.
For the case p ∤ m + 2 we get

χ(−2)τ (χ)cχ(−m − 2) = χ(2(m + 2))τ (χ)
2.

Since χ is quadratic, we have τ (χ)2 = χ(−1)p, so that (120) follows. The remaining results
can be deduced in similar fashion, starting with (134) to show (135) and (136).
The case of p = 2, that is (121) and (122) is as in [23, Section 5], as the gcd condition
has no eﬀect. □

We continue with an estimate that is used later in Section 11.3 in the proof of Lemma 10.6
to bound the contribution of all characters induced by a ﬁxed pair of primitive ones.

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 77

Lemma 11.2. Let χi be characters to the modulus pα, p ̸= 2, α > 0. We have

|F (χ1, χ2, 1, 1, m)| ≤
 {p2α − 3p2α−1 + 1 if χ1 = χ2 and pα | m,
p2α−1/2 + 3p2α−1 else.
(137)

and
 |F (χ1, χ2, j1, j2, m)| ≤ 2p2α−1 if p|j1j2.(138)

Furthermore, for p = 2 we have
 |F (χ1, χ2, 1, 1, m)| ≤ 2
2α.(139)

Proof. For i ∈ {1, 2} we denote by pα∗
i the conductor of χi. Let further pα′ be the conductor
of χ1χ2 and pαm = (pα, m). With the help of the identities (133) and (134), we can reduce
the lemma to the study of

F (χ1, χ2, −, −, m),

F (χ1, χ2, −, p, m) = F (χ2, χ1, p, −, m) and

F (χ1, χ2, p, p, m).

We start by observing that (see also [23, proof of Lemma 5.5])

F (χ1, χ2, −, −, m) = τ (χ1)τ (χ2)cχ1χ2(−m).

We apply Lemma 8.7 to cχ1χ2(−m). If χ1 = χ2 (i.e. α′ = 0) we have

cχ1χ2(−m) = cpα(m) =
 



pα(1 − 1
p ) if pα|m
−pα−1 if pα−1||m
0 else.

If α′ ̸= 0, then cχ1χ2(−m) vanishes, unless α − αn − α′ = 0. We get

|cχ1χ2(−m)| ≤ p(α−αm)/2 ϕ(pα)
ϕ(pα−αm)

≤ pα−1/2.

For τ (χ1), we have the following well-known results

|τ (χ1)| =
 



pα/2 if α∗
1 = α
1 if α∗
1 = 0, α = 1
0 else,
(140)
 τ (χ1)τ (χ1) = χ(−1)|τ (χ1)|
2.(141)

We get
 F (χ1, χ2, −, −, m) = χ1(−1)p2α(1 − 1
p ) if χ1 = χ2, α
∗
1 = α and pα | m(142)
 |F (χ1, χ2, −, −, m)| ≤ p2α−1/2 else.(143)

78 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

We continue with the next case of F and open the divisibility condition in the deﬁnition
of F (χ1, χ2, −, p, m) by characters. This gives us

F (χ1, χ2, −, p, m) = 1
ϕ(p)
 ∑

ψ(p) ψ(−2) ∑

b1(pα) χ1(b1) ∑

b2(pα) χ2ψ(b2) ∑

a(pα)∗ epα(a(b1 + b2 − m))

= 1
ϕ(p)
 ∑

ψ(p) ψ(−2)τ (χ1)τ (χ2ψ)cχ1χ2ψ(−m).(144)

We consider ﬁrst the case α′ ≤ 1. In that case the conductor of χ1χ2ψ is always at
most p. Thus,

cχ1χ2ψ(−m) = ∑

b(pα) χ1χ2ψ(b)epα(−bm)

= ∑

b′(p)∗

b′′(pα−1)
 χ1χ2ψ(b′′p + b′)epα(−(b′′p + b′)m)

= ∑

b′(p)∗ (χ1χ2)∗ψ(b′)epα(−b′m) ∑

b′′(pα−1) epα−1(−b′′m)

= 1pα−1|mpα−1 ∑

b′(p)∗ (χ1χ2)∗ψ(b′)epα(−b′m),

where (χ1χ2)∗ is the primitive character inducing χ1χ2. Plugging this in (144) gives

F (χ1, χ2, −, p, m)

= 1pα−1|mpα−1τ (χ1)
ϕ(p)
 ∑

ψ(p) ψ(−2) ∑

b2(pα) χ2ψ(b2)epα(b2) ∑

b′(p)∗ (χ1χ2)∗ψ(b′)ep(−b′m/pα−1)

= 1pα−1|mpα−1τ (χ1)
ϕ(p)
 ∑

b2(pα) χ2(b2)epα(b2) ∑

b′(p)∗ (χ1χ2)∗(b′)epα(−b′m) ∑

ψ(p) ψ(−2b′b2)

= 1pα−1|mpα−1τ (χ1) ∑

b2(pα) χ2(b2)epα(b2)(χ1χ2)(−2b2)epα(2b2m)

= 1pα−1|mpα−1τ (χ1)χ1χ2(−2)cχ1 (2m + 1).

If pα|m then cχ1(2m + 1) = cχ1(1) = τ (χ1) and we get

F (χ1, χ2, −, p, m) = χ(−1)p2α−1 if χ1 = χ2 and pα|m.(145)

Furthermore, if α1 ≥ 1, then τ (χ1) = 0 unless α∗
1 = α. By Lemma 8.7 and (141), we have

|τ (χ1)cχ1 (2m + 1)| ≤ pα.(146)

If α∗
1 = 0, then τ (χ1) = −1 and |cχ1(2m + 1)| ≤ pα, so again (146) follows. We get (for
the moment still restricted to α′ ≤ 1) the estimate

|F (χ1, χ2, −, p, m)| ≤ p2α−1.(147)
 THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 79

For the case α′ ≥ 2 we observe that for any ψ the conductor of χ1χ2ψ in (144) is pα′.
From Lemma 8.7 we get that cχ1χ2ψ(−m) = 0 unless αm = α − α′ and so we can estimate

|cχ1χ2ψ(−m)| ≤ pα−α′/2

≤ pα−1.

Using this bound, a summation with absolute values over ψ in (144) shows that (147)
holds for any value of α′.
We now consider F (χ1, χ2, p, p, m). We ﬁrst show that

|F (χ1, χ2, p, p, m)| ≤ 1 if χ1 = χ2 and pα | m.(148)

For α = 1 we have
 F (χ1, χ2, p, p, m) = χ1χ2(−2)cp(m − 4)(149)

and (148) follows. Furthermore, we claim

F (χ1, χ2, p, p, m) = 0, if α
′ ≤ 1 and α ≥ 2.(150)

This will give (148) for the remaining α.
To show (150), we note that the choice of α′ implies that χ2 = χ1χ′ for some character
χ′ with conductor at most p. Thus

F (χ1, χ2, p, p, m) = ∑

bi(pα)∗
bi≡−2(p)
 χ1(b1b2)χ′(b2) ∑

a(pα)∗ epα(a(b1 + b2 − m)).

We substitute b2 = b1r so that this equals

χ′(−2) ∑

b1,r(pα)∗
b1≡−2(p),r≡1(p)
 χ1(r) ∑

a(pα)∗ epα(a(b1 + b1r − m)),

where we used that χ′(rb1) = χ′(−2), since rb1 ≡ −2(p) and the conductor of χ′ is at most
p. We consider the sum over b1 and get
∑

b1(pα),
b1≡−2(p)
 epα(a(b1 + b1r)) = epα(−2a(1 + r)) ∑

b′(pα−1) epα−1(b
′a(1 + r))

= 0,

since p ∤ a(1 + r). From (149) and (150) we also get the always valid estimate

|F (χ1, χ2, p, p, m)| ≤ p − 1.(151)

We gather the results and get from (133), (142), (145), and (148) the case χ1 = χ2, pα|m
of (137).The remaining cases of the lemma follow from a combination of the decomposi-
tions (133) or (134) with (143), (147), and (151).
For the statement in (139) the gcd conditions do not play a role and so it follows directly
from the considerations in [23, Section 5]. □

With the tools used in the previous proof, we can now also quickly deduce Lemma 10.3
and complete our considerations of Gauß sums with a gcd condition.

Proof of Lemma 10.3. The statement follows from the fact that τ (χ) vanishes if χ is a
character to the modulus α > 1 that is not primitive (see (140)) and writing the congruence
conditions with the help of characters as in the previous proof. □

80 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

11.2. Sieve results

An application of a sieve of the form

θ(n) = ∑

d|n λd(152)

with range P on a sequence with local density function ϕ(d)−1 gives rise to a main term
of the form ∑

d|P
 λd
ϕ(d) = V (P) ∑

b|P θ(b)h(b).(153)

Here the function h is multiplicative and given on primes by

h(p) = ϕ(p)−1

1 − ϕ(p)−1 .

Let D be the level of the sieve, z = P + and write s = log D
log z . If the sieve fulﬁls a so-called
fundamental lemma we have ∑

d|P(z)
 λd
ϕ(d) = V (P)
(1 + O(e
−cs)
)

which is equivalent to ∣
∣
∣ ∑

b|P
b̸=1
 θ(b)h(b)
∣
∣
∣ ≪ e
−cs.(154)

Since our pre-sieves are interacting with the additive problem we consider, we are led to
the study of Si(q, j, e) as given in (100) instead of (153).
We state the results in this subsection in slightly more general terms and use the nota-
tion g(d) and h(d) with or without subscripts to denote pairs of multiplicative functions
supported on the squarefree numbers with

0 ≤ g(p) < 1

and satisfying the relation
 h(p) = g(p)
1 − g(p) .

The eﬀect of q in Si(q, j, e) can be absorbed into the deﬁnition of the local density function,
and we consider
 g(e) ∑

c|j
d|P/(ej)
 λcdeg(d).

We will see in the next subsection that treating the pseudo-singular series with sieve
weights gives rise to a problem that is very similar to, but slightly more delicate than, what
is encountered in the study of sieve weights in short intervals. The ﬁrst lemma we need
is a technical identity that translates S(q, j, e) into the language of θ, generalising (153).
This result and its proof are motivated by [9, proof of Lemma 6.18] or more precisely [19,
proof of Lemma 5.1] which ﬁxes a mistake in the former.

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 81

Lemma 11.3. Let P be a squarefree integer, λd sieve weights supported on d|P only. Let
j, e be integers with j|P, e|P, and (j, e) = 1. Then it holds that

g(e) ∑

c|j
d|P/(ej)
 λcdeg(d) = V h(j)
g(j) µ(e)h(e) ∑

b|P/j θ(jb)h(b) µ((b, e))
h((b, e)) ,

where V = ∏p|P(1 − g(p)
), and θ(n) is given by (152).

Proof. Let γ(d, j) be a multiplicative function in d, given on primes by

γ(p, j) =
 {g(p) if p ∤ j
1 if p|j.

We have
 g(e) ∑

c|j
d|P/(ej)
 λcdeg(d) = ∑

k|P
k≡0(e)
 λdγ(k, j).

By M¨obius inversion
 λk = ∑

ab=k µ(a)θ(b)

and so ∑

k|P
k≡0(e)
 λdγ(k, j) = ∑

b|P θ(b)γ(b, j) ∑

a|P/b
e
(b,e) |a
 µ(a)γ(a, j)

= ∑

b|P θ(b)γ(b, j)µ(e/(e, b))γ(e/(e, b), j) ∑

a|P/[b,e] µ(a)γ(a, j)

= ∑

b|P θ(b)γ(b, j)µ(e/(e, b))γ(e/(e, b), j) ∏

p|P/[b,e](1 − γ(p, j)).(155)

We recall (e, j) = 1 and so γ(e/(e, b), j) = g(e/(e, b)) and the product in (155) vanishes
unless j|b. If j|b then

∏

p|P/[b,e]
(1 − γ(p, j)) = ∏

p|P/j
(1 − g(p)
) ∏

p|[b,e]/j
(
1 − g(p)
)−1

= V ∏

p|j
 (1 − g(p)
)−1 ∏

p|[b,e]/j
(1 − g(p)
)−1

= V h(j)
g(j)
 ∏

p|[b,e]/j
(1 − g(p)
)−1.

82 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

Plugging this in, recalling again (e, j) = 1, and writing b = jb′, we see that (155) is

V h(j)
g(j)
 ∑

b|P
j|b
 θ(b)γ(b, j)µ(e/(e, b))g(e/(e, b)) ∏

p|[b,e]/j
(
1 − g(p)
)−1

= V h(j)
g(j)
 ∑

b′|P/j θb′jg(b′)µ(e/(e, b′))g(e/(e, b′)) ∏

p|[b′,e]

(1 − g(p)
)−1

= V h(j)
g(j)
 ∑

b′|P/j θb′jµ(e)µ(e, b′)g([b′, e]) ∏

p|[b′,e]

(
1 − g(p)
)−1

= V h(j)
g(j) h(e)µ(e) ∑

b′ |P/j θb′jh(b′) µ((e, b′))
h((e, b′)) ,

as required. □

The fundamental lemma of sieve theory states results of type (154). We require a
slightly diﬀerent form that is easier for us to apply it in the next subsection. This is again
motivated by a similar approach for almost primes in short intervals, see [19, around eq.
(25), (26)].

Lemma 11.4. Let θ belong to an upper or lower bound β sieve with range P0 with P +
0 ≤ z

and level D. Write zr = z( β−1
β+1 )r , s = log D
log z , P0(x, y) = ∏ p∈P0
x<p≤y p, and P0(x) = P0(0, x) .

Assume that s > β + 1. Then it holds that

|θn − 1(n,P0(z))=1| ≤ τ (n)
2 ∑

r>(s−β−1)/2 2
−r1(n,P0(zr))=1.(156)

Proof. The β sieve is a combinatorial sieve that is constructed by iteration with certain
cutoﬀ parameters, see [9, eq. (6.31)–(6.34), (6.54)]. From this it follows immediately that
in the case of an upper bound sieve

θ(n) = 1(n,P0(z))=1 + ∑

r odd Vr(n),

and in the case of a lower bound sieve

θ(n) = 1(n,P0(z))=1 − ∑

r even Vr(n),

where
 Vr(n) = ∑

p1...prd=n
pi∈P0(z), pr<pr−1<...p1
p1p2...prpβ
r ≥D
p1p2...phpβ
h<D for all h<r,h≡r(2)
 1(d,P0(pr))=1.

Let us take a closer look at this sum. By [9, Corollary 6.6] we have that pr ≥ z( β−1
β+1 )r/2.
We also have D ≤ pr+β
1 ≤ zr+β, which is impossible unless r ≥ s − β. Finally, the
number of choices for d is bounded by τ (n) and the number of choices for p1, . . . , pr by
2ω(n)−r ≤ τ (n)2−r. By writing r = 2r′ + 1 or r = 2r′ respectively for the case of an upper
bound or lower bound sieve, the lemma follows. □

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 83

11.3. Singular series

In this subsection we conclude the auxiliary results by proving Lemmas 10.4 and 10.6.

Proof of Lemma 10.4. We recall the notation s0 = log D0
log P and that we have to show

∑

q†≤P ′
 F(q†, m)
ϕ(q†)2 = V (P †) S(m)

S(m, 2 ̃P )
 (
1 + O(
e
−cs0 + e100
√log N

P ′
 ))
,

where the summation runs (by notation) over q†|(P †)∞,

F(q, m) = ∑

ji|q S†
1(q, j1, 1)S†
2(q, j2, 1)F (χ(q)
0 , χ(q)
0 , j1, j2, m),

and S†
i , F , are given by (100), (105) respectively.
We start by applying Lemma 11.3 with

g(p) = g(p, q) =
 { 1
p−1 if p ∤ q
0 else

to get
 S†
i (q, ji, 1) = ∏

p|P †
(1 − g(p, q)
) ∑

b|P †/ji θi(jib)h(b, q).

Here
 h(p, q) =
 { 1
p−2 if p ∤ q
0 else

and ∏

p|P †
(1 − g(p, q)
) = ϕ(q)
ϕ2(q)
 ∏

p|P †
(
1 − 1
p − 1
 )

= ϕ(q)
ϕ2(q) V (P †).

Thus, since ji|q,
 S†
i (q, ji, 1) = V (P †) ϕ(q)
ϕ2(q)
 ∑

b|P †/q θi(jib)h(b),

where h(b) = h(b, 1). Plugging this in and using that F vanishes unless q is squarefree, we
arrive at
∑

q≤P ′

q|(P †)∞
 ∑

ji|q
 S†
1(q, j1, 1)S†
2(q, j2, 1)F (χ(q)
0 , χ(q)
0 , j1, j2, m)
ϕ(q)2

= V (P †)
2 ∑

ji≤P ′

ji|(P †)∞
 ∑

bi|P †/ji θ1(b1j1)h(b1)θ2(b2j2)h(b2) ∑

q≤P ′
[j1,j2]|q
q|P †/((b1,b2))
 F (χ(q)
0 , χ(q)
0 , j1, j2, m)
ϕ2(q)2 .

(157)

84 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

Recall that P † is odd. For any pair j1, j2 with ji|(P †)∞ we have by multiplicativity
(Lemma 10.2)

∑

q≤P ′
[j1,j2]|q
q|P †/((b1,b2))
 F (χ(q)
0 , χ(q)
0 , j1, j2, m)
ϕ2(q)2 = ∏

p|[j1,j2]
( F (χ(p)
0 , χ(p)
0 , j1, j2, m)
(p − 2)2 ) ∑

q≤P ′/[j1,j2]
q|P †/((b1,b2,j1,j2))
 ∏

p|q
 σ(p, m)
(p − 2)2 ,

(158)

where σ(p, m) = F (χ(p)
0 , χ(p)
0 , 1, 1, m) and more generally F (χ(p)
0 , χ(p)
0 , j1, j2, m) are given
explicitly by Lemmas 10.5 and 11.1. The term b1 = b2 = j1 = j2 = 1 in (157) contributes

V (P †)
2 ∑

q≤P ′

q|P †
 ∏

p|q
 σ(p, m)
(p − 2)2 = V (P †)
2
 




 S(m)

S(m, 2 ̃P) − ∑

q>P ′

(q, ̃2P)=1
 ∏

p|q |µ(q)| σ(p, m)
(p − 2)2
 




 .

We use (118) and Rankin’s trick to estimate the tail sum as

∑

q>P ′

(q,2 ̃P)=1
 ∏

p|q |µ(q)| σ(p, m)
(p − 2)2 ≪ ∑

q>P ′
(q,2)=1
 ∏

p|m(m+2)(m+4)
 20
p
 ∏

p|q,p∤m(m+2)(m+4)
 4
(p − 2)2

≪ (P ′)
−1/2 ∏

p|m(m+2)(m+4)
 (1 + p1/2 · 20
p
 )

× ∏

p∤m(m+2)(m+4)
 (1 + p1/2 · 4
(p − 2)2
 )

≪ (P ′)
−1/2 exp( ∑

p|m(m+2)(m+4)
 20
p1/2
 )

≪ (P ′)
−1/2 exp(100ω(m(m + 2)(m + 4))
1/2)

≪ (P ′)
−1/2 exp(100(log N )
1/2).

The remaining part of (157) is part of the error term and to deal with it we ﬁrst esti-
mate (158). For p|j1j2 we have by Lemma 11.1 the always valid bound |F (χ(p)
0 , χ(p)
0 , j1, j2, m)|
≤ p − 1. We get

∣
∣
∣ ∏

p|[j1,j2]
( F (χ(p)
0 , χ(p)
0 , j1, j2, m)
(p − 2)2
 ) ∑

q≤P/[j1,j2]
q|P †/((b1,b2,j1,j2))
 ∏

p|q
 σ(p, m)
(p − 2)2
 ∣
∣
∣

≪
 ∏p|j1j2(1 + 3
p )

[j1, j2]
 ∑

q
 ∏

p|q
 |σ(p, m)|
ϕ2(p)2

≪
 ∏p|j1j2(1 + 3
p )

[j1, j2] S(m),

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 85

where we used that either σ(p, m) > 0 or σ(p, m) = O(1). To complete the proof of
Lemma 10.4 it consequently suﬃces to show

∑

ji|P †
 ∑

bi|P †/ji
b1j1b2j2̸=1
 |θ1(b1j1)θ2(b2j2)| ∏p|b1b2j1j2(1 + O(1)
p )

b1b2[j1, j2] ≪ e
−cs0.(159)

Let us ﬁrst consider the contribution of terms with b1j1 ̸= 1 and b2j2 ̸= 1 to (159). We
can apply Lemma 11.4 (with z = P ) and write ji = dli with (l1, l2) = 1 to estimate it by

≤ ∑

ri>(s0−β−1)/2 2
−r1−r2 ∑

d|P †
 ∑

bili|P †/d
(dbili,P †(Pri ))=1
 τ (d)4τ (b1)2τ (b2)2τ (l1)2τ (l2)2 ∏p|dl1l2b1b2(1 + O(1)
p )

dl1l2b1b2

≤ ∑

ri>(s0−β−1)/2 2
−r1−r2 ∑

db1l1|P †

(db1l1,P †(Pr1 ))=1
 τ (d)4τ (b1)2τ (l1)2 ∏p|dl1b1(1 + O(1)
p )

dl1b1

× ∑

b2l2|P †

(b2l2,P †(Pr2 ))=1
 τ (b2)2τ (l2)2 ∏p|l2b2(
1 + O(1)
p )

l2b2

≤
 ( ∑

r>(s0−β−1)/2 2
−r ∑

b|P †

(b,P †(Pr))=1
 τ (b)6 ∏p|b(1 + O(1)
p )

b
 )2.

(160)

By the deﬁnition of Pr = P ( β−1
β+1 )r in Lemma 11.4 we have

∑

b|P †

(b,P †(Pr))=1
 τ (b)6 ∏p|b(1 + O(1)
p )

b ≪ ∏

Pr<p≤P
 (
1 + 26

p
 )

≪ ( log P
log Pr
 )26

= ( β + 1
β − 1
 )26r.

As long as
 β > 185,(161)

we have ( β+1
β−1 )26 < 2 and so the tail sum over r in (160) converges with exponential
decay in s0. The required estimate (159) follows in the currently considered case j1b1 ̸= 1,
j2b2 ̸= 1. The remaining case that b1j1b2j2 ̸= 1 but b1j1 = 1 or b2j2 = 1 works similarly
but is easier. In fact, it follows directly from a standard application of the fundamental
lemma. □

86 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

We now prove the last remaining result, Lemma 10.6. While the just proved Lemma 10.4
asymptotically evaluates the singular series with sieve weights, we now only require an
upper bound of correct order of magnitude, but need it for any pseudo-singular series
associated with a pair of primitive characters and again including sieve weights.

Proof of Lemma 10.6. We recall that we have to show that for any pair of primitive char-
acters ξ1, ξ2 it holds that
G†(ξ1ξ2, m) ̃G(ξ1, ξ2, m) ≪ V (P †)
2S(m)

and split this task into showing

G†(ξ1, ξ2, m) ≪ V (P †)
2 S(m)

S(m, 2 ̃P)
(162)

and
 ̃G(ξ1, ξ2, m) ≪ S(m, 2 ̃P).(163)

We start with showing (162) and further recall

G†(ξ1, ξ2, m) = ∑

eili=g†
i
ei|P †
 ∑

q|(P †)∞
li|q
(q,e1e2)=1
 ∑

ji|q
 |S†
1(q, j1, e1)S†
2(q, j2, e2)F (ξ(l1)
1 χ(q)
0 , ξ(l2)
2 χ(q)
0 , 1, 1, m)|
ϕ(q)2 ,

where gi is the conductor of ξi and g†
i denotes its P † component.
We start as in the proof of Lemma 10.4 and apply Lemma 11.3. It gives us now,
observing that (ei, q) = 1,

S†
i (q, ji, ei) = V (P †) ϕ(q)
ϕ2(q) µ(ei)h(ei) ∑

b|P/q θi(jib)h(b) µ((ei, b))
h((ei, b)) ,

where h is as before. The condition (q, e1e2) = 1 and [l1, l2]|q can only be fulﬁlled simul-
taneously if (e1e2, l1l2) = 1. Applying the triangle inequality, we thus estimate

G†(ξ1, ξ2, m) ≤ V (P †)
2 ∑

eili=g†
i
(e1e2,l1l2)=1
ei|P †
 ∑

jibi|P † |θ1(b1j1)θ2(b2j2)|h([b1, e1])h([b2, e2])

× ∑

q|(P †)∞
[j1,j2,l1,l2]|q
(q,b1b2e1e2)=1
 |F (ξ(l1)
1 χ(q)
0 , ξ(l2)
2 χ(q)
0 , j1, j2, m)|
ϕ2(q)2 .(164)
 THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 87

Consider the sum over q. The multiplicativity of F (Lemma 10.2) and Lemma 10.3 give
us
 ∑

q|(P †)∞
[j1,j2,l1,l2]|q
(q,b1b2e1e2)=1
 |F (ξ(l1)
1 χ(q)
0 , ξ(l2)
2 χ(q)
0 , j1, j2, m)|
ϕ2(q)2

= ∏

pα||[j1,j2,l1,l2]
 |F (ξ((l1,pα))
1 χ(pα)
0 , ξ((l2,pα))
2 χ(pα)
0 , j1, j2, m)|
ϕ2(pα)2

× ∑

q|(P †)∞
(q,b1b2e1e2j1j2l1l2)=1
 |F (χ(q)
0 , χ(q)
0 , 1, 1, m)|
ϕ2(q)2

≤ ∏

pα||[j1,j2,l1,l2]
 |F (ξ((l1,pα))
1 χ(pα)
0 , ξ((l2,pα))
2 χ(pα)
0 , j1, j2, m)|
ϕ2(pα)2 ∑

q
(q,2 ̃Pl1l2j1j2)=1
 |F (χ(q)
0 , χ(q)
0 , 1, 1, m)|
ϕ2(q)2

= ∏

pα||[j1,j2,l1,l2]
 |F (ξ((l1,pα))
1 χ(pα)
0 , ξ((l2,pα))
2 χ(pα)
0 , j1, j2, m)|

ϕ2(pα)2(1 + |σ(p,m)|
(p−2)2 ) ∏

p∤2 ̃P
(1 + |σ(p, m)|
(p − 2)2
 )

≪ ∏

pα||[j1,j2,l1,l2]
 |F (ξ((l1,pα))
1 χ(pα)
0 , ξ((l2,pα))
2 χ(pα)
0 , j1, j2, m)|

ϕ2(pα)2(1 + |σ(p,m)|
(p−2)2 ) S(m)

S(m, 2 ̃P) .

Thus, by (164) our goal (162) follows if we can show
∑

eili=g†
i
(e1e2,l1l2)=1
ei|P †
 ∑

jibi|P † |θ1(b1j1)θ2(b2j2)|h([b1, e1])h([b2, e2])

× ∏

pα||[j1,j2,l1,l2]
 |F (ξ((l1,pα))
1 χ(pα)
0 , ξ((l2,pα))
2 χ(pα)
0 , j1, j2, m)|

ϕ2(pα)2(
1 + |σ(p,m)|
(p−2)2 ) ≪ 1.

(165)

We continue estimating the remaining Euler factor with the help of Lemma 11.2, starting
with the case p ∤ (j1, j2), (l1, pα) = (l2, pα) = pα, and p|m. We are then possibly in the
bad case of (137) and together with (118) get

|F (ξ(l1,pα)
1 χ(pα)
0 , ξ(l2,pα)
2 χ(pα)
0 , j1, j2, m)|

ϕ2(pα)2(1 + |σ(p,m)|
(p−2)2 ) ≤ p2α − 3p2α−1 + 1

ϕ2(pα)2(1 + (p−4)
(p−2)2 )

= 1 − 3p−1 + p−2α

(1 − 2
p )2(1 + (p−4)
(p−2)2 )

= 1 − 3p−1 + O(p−2)
(1 − 4p−1 + O(p−2)
)(1 + p−1 + O(p−2)
)

= 1 + O(p−2).

88 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

If now p ∤ (j1, j2) and either p2α ∤ l1l2 or p ∤ m we are in the better case of (137) and
together with (118) obtain now

|F (ξ(l1,pα)
1 χ(pα)
0 , ξ(l2,pα)
2 χ(pα)
0 , j1, j2, m)|

ϕ2(pα)2(1 + |σ(p,m)|
(p−2)2 ) ≤ p2α−1/2 + 3p2α−1

ϕ2(pα)2(1 − 4
(p−2)2 )

= p−1/2 + 3p−1

(1 − 2
p )2(1 − 4
(p−2)2 )

≤ p−1/2 + O(p−1).

Finally, if p|(j1, j2) we get with the help of (138)

|F (ξ(l1,pα)
1 χ(pα)
0 , ξ(l2,pα)
2 χ(pα)
0 , j1, j2, m)|

ϕ2(pα)2(1 + |σ(p,m)|
(p−2)2 ) ≤ 2p2α−1

ϕ2(pα)2(1 − 4
(p−2)2 )

= 2p−1

(1 − 2
p )2(1 − 4
(p−2)2 )

= 2p−1(1 + O(p−1)
).

Combining the cases, we estimate the Euler factor by

∏

pα||[j1,j2,l1,l2]
 |F (ξ(l1)
1 χ(pα)
0 , ξ(l2)
2 χ(pα)
0 , j1, j2, m)|

ϕ2(pα)2(1 + |σ(p,m)|
(p−2)2 )

≪ ∏

p|j1j2
 2
p (1 + O(p−1)) ∏

p|l1l2,p∤j1j2
(l1,p∞)̸=(l2,p∞)

(p−1/2 + O(p−1))

≤ τ ([j1, j2]) ∏p|j1j2(1 + 2p−1)

[j1, j2]
 ∏

p|l1l2,p∤j1j2
(l1,p∞)̸=(l2,p∞)
(p−1/2 + O(p−1)).

Plugging this in and changing order of summation shows that the left-hand side of (165)
is
 ≪ ∑

jibi|P †
∣
∣θ1(b1j1)θ2(b2j2)
∣
∣ τ ([j1, j2]) ∏p|j1j2(1 + 2p−1)

[j1, j2]
 ∑

eili=g†
i
(e1e2,l1l2)=1
ei|P †
 h([b1, e1])h([b2, e2])

× ∏

p|l1l2,p∤j1j2
(l1,p∞)̸=(l2,p∞)

(p−1/2 + O(p−1)).

(166)

We can express the sum over eili in multiplicative fashion in the following sense
∏

p|g†
1g†
2
pβ1 ||g†
i
 ∑

eili=pβi
(e1e2,l1l2)=1
ei|P †
 h([b1, e1])h([b2, e2]) ∏

p|l1l2,p∤j1j2
(l1,p∞)̸=(l2,p∞)

(p−1/2 + O(p−1)).

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 89

If β2 = 0, we give an upper bound for the double sum over eili by

h(b2) ∑

e1l1=pβ1
(e1,l1)=1
ei|P †
 h([b1, e1]) ∏

p|l1,p∤j1j2(p−1/2 + O(p−1)) ≤ h(b2)h(b1)
 {2 p|b1j1j2
p−1/2 + O(p−1) p ∤ b1j1j2.

Naturally a similar estimate holds for β1 = 0. If β1β2 ̸= 0, we estimate the double sum by

∑

eili=pβi
(e1e2,l1l2)=1
ei|P †
 h([b1, e1])h([b2, e2]) ∏

p|l1l2,p∤j1j2
(l1,p∞)̸=(l2,p∞)
(p−1/2 + O(p−1))

≤ ∑

eili=pβi
(e1e2,l1l2)=1
ei|P †
 h([b1, e1])h([b2, e2])

= h(b1)h(b2) + 1β1=β2=1h([b1, p])h([b2, p])

≤h(b1)h(b2)
 {2 p|b1b2
1 + O(p−2) p ∤ b1b2.

The estimates of the sum over eili show that the contribution of primes that do not
divide the sieve weighted coeﬃcients bi, ji is O(1). This is crucial for us, as we could
compensate for any losses here only by getting more saving out of Gallagher’s prime
number theorem (Lemma 10.7), i.e. miss power saving. We discard the condition that
p|g†
1g†
2 and get that (166) is

≪ ∑

jibi|P †
∣
∣θ1(b1j1)θ2(b2j2)
∣
∣ τ (j1)2τ (j2)2τ (b1)τ (b2) ∏p|j1j2b1b2(1 + O(p−1))

b1b2[j1, j2] .

This sum is closely related to the one appearing in (159), the only diﬀerence being addi-
tional divisor functions. The same steps as there show that it is 1 + O(e−cs0) under the
stronger condition
 β > 739(167)

that ensures ( β+1
β−1 )28 < 2. The estimate (165) and so (162) follows.
The proof of (163) is similar but considerably simpler as it does not include the sieve
weights. By deﬁnition

̃G(ξ1, ξ2, m) = ∑

eili=2gi(2)̃gi
ei| ̃P
 1
ϕ2(e1)ϕ2(e2)
 ∑

q|(2 ̃P)∞
li|q
(q,e1e2)=1
 |F (ξ(l1)
1 χ(q)
0 , ξ(l2)
2 χ(q)
0 , 1, 1, m)|
ϕ2(q)2 .

90 LASSE GRIMMELT AND JONI TER ¨AV ¨AINEN

By similar steps as for G† we get

̃G(ξ1, ξ2, m) = ∑

eili=2gi(2)̃gi
(e1e2,l1l2)=1
ei| ̃P
 1
ϕ2(e1)ϕ2(e2)
 ∏

pα||[l1,l2]
 F (ξ((l1,pα))
1 , ξ((l2,pα))
2 , 1, 1, m)
ϕ2(p)2

× ∏

p| ̃2P
p∤e1e2l1l2
(
1 + |σ(p, m)|
ϕ2(p)2
 )

≤ ∑

eili=2gi(2)̃gi
(e1e2,l1l2)=1
ei| ̃P
 1
ϕ2(e1)ϕ2(e2)
 ∏

pα||[l1,l2]
 F (ξ((l1,pα))
1 , ξ((l2,pα))
2 , 1, 1, m)

ϕ2(p)2(1 + |σ(p,m)|
ϕ2(p)2 ) S(m, ̃2P).

The required bound

∑

eili=2gi(2)̃gi
(e1e2,l1l2)=1
ei| ̃P
 1
ϕ2(e1)ϕ2(e2)
 ∏

pα||[l1,l2]
 F (ξ((l1,pα))
1 , ξ((l2,pα))
2 , 1, 1, m)

ϕ2(p)2(1 + |σ(p,m)|
ϕ2(p)2 ) ≪ 1

follows from (165), as it is the subsum b1 = b2 = j1 = j2 = 1, and the estimate (139) for
the case that [l1, l2] is even. This completes the proof of Lemma 10.6. □

References

[1] E. Bombieri, J. B. Friedlander, and H. Iwaniec. Primes in arithmetic progressions to large moduli.
Acta Math., 156(3-4):203–251, 1986.
[2] E. Bombieri, J. B. Friedlander, and H. Iwaniec. Some corrections to an old paper. arXiv e-prints, page
arXiv:1903.01371, March 2019.
[3] J. R. Chen. On the representation of a larger even integer as the sum of a prime and the product of
at most two primes. Sci. Sinica, 16:157–176, 1973.
[4] J.-M. Deshouillers and H. Iwaniec. Kloosterman Sums and Fourier Coeﬃcients of Cusp Forms. Invent.
Math., 70:219–219, 1982/83.
[5] S. Drappeau. Sums of Kloosterman sums in arithmetic progressions, and the error term in the disper-
sion method. Proc. London Math. Soc., 114(4):684–732, 2017.
[6] ´E. Fouvry. Autour du th´eor`eme de Bombieri-Vinogradov. II. Ann. Sci. ´Ecole Norm. Sup. (4),
20(4):617–640, 1987.
[7] ´E. Fouvry and F. Grupp. Weighted sieves and twin prime type equations. Duke Math. J., 58(3):731–
748, 1989.
[8] E. Fouvry and H. Iwaniec. Primes in arithmetic progressions. Acta Arith., 42(2):197–218, 1983.
[9] J. Friedlander and H. Iwaniec. Opera de Cribro, volume 57 of American Mathematical Society Collo-
quium Publications. American Mathematical Society, Providence, RI, 2010.
[10] P. X. Gallagher. A large sieve density estimate near σ = 1. Invent. Math., 11(4):329–339, 1970.
[11] G. Greaves. The weighted linear sieve and Selberg’s λ2-method. Acta Arithmetica, 47(1):71–96, 0 1986.
[12] G. Greaves. Sieves in number theory, volume 43 of Ergebnisse der Mathematik und ihrer Grenzgebiete
(3) [Results in Mathematics and Related Areas (3)]. Springer-Verlag, Berlin, 2001.
[13] B. Green. Roth’s theorem in the primes. Ann. of Math., 161(3):1609–1636, 2005.
[14] L. Grimmelt. Goldbach Numbers in Short Intervals – A Nonnegative Model Approach. To appear in
Ann. Scuola Norm-Sci., 2021.
[15] H. Iwaniec and E. Kowalski. Analytic number theory, volume 53 of American Mathematical Society
Colloquium Publications. American Mathematical Society, Providence, RI, 2004.
[16] M. Laborde. Buchstab’s sifting weights. Mathematika, 26(2):250–257 (1980), 1979.

THE EXCEPTIONAL SET IN GOLDBACH’S PROBLEM WITH ALMOST TWIN PRIMES 91

[17] W. C. Lu. Exceptional set of Goldbach number. Journal of Number Theory, 130(10):2359–2392, 2010.
[18] K. Matom¨aki. A Bombieri-Vinogradov type exponential sum result with applications. J. Number
Theory, 129(9):2214–2225, 2009.
[19] K. Matom¨aki. Almost primes in almost all very short intervals. To appear in J. London Math. Soc.,
2021.
[20] K. Matom¨aki and X. Shao. Vinogradov’s three primes theorem with almost twin primes. Compos.
Math., 153(6):1220–1256, 2017.
[21] J. Maynard. Primes in arithmetic progressions to large moduli II: Well-factorable estimates. arXiv
e-prints, page arXiv:2006.07088, June 2020.
[22] X. M. Meng. The Goldbach problems with prime numbers of special type. Acta Math. Sinica (Chin.
Ser.), 50(2):255–260, 2007.
[23] H. L. Montgomery and R. C. Vaughan. The exceptional set in Goldbach’s problem. Acta Arith.,
27:353–370, 1975.
[24] J. Pintz. Elementary methods in the theory of L-functions. V. The theorems of Landau and Page.
Acta Arith., 32(2):163–171, 1977.
[25] J. Pintz. A new explicit formula in the additive theory of primes with applications II. The exceptional
set in Goldbach’s problem. arXiv e-prints, page arXiv:1804.09084, April 2018.
[26] A. Selberg. Sieve methods. In 1969 Number Theory Institute (Proc. Sympos. Pure Math., Vol. XX,
State Univ. New York, Stony Brook, N.Y., 1969), pages 311–351, 1971.
[27] P. Shiu. A Brun-Titchmarsh theorem for multiplicative functions. J. Reine Angew. Math., 313:161–
170, 1980.
[28] J. Ter¨av¨ainen. The Goldbach problem for primes that are sums of two squares plus one. Mathematika,
64(1):20–70, 2018.
[29] D. I. Tolev. Additive problems with prime numbers of special type. Acta Arith., 96(1):53–88, 2000.

Mathematical Institute, University of Oxford, Oxford OX2 6GG, UK
Email address: grimmelt@maths.ox.ac.uk

Department of Mathematics and Statistics, University of Turku, 20014 Turku, Finland
Email address: joni.p.teravainen@gmail.com
