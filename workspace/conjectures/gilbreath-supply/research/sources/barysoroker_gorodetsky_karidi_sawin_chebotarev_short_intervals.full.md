<!-- source: https://arxiv.org/pdf/1810.06201 | converted from PDF -->

arXiv:1810.06201v2  [math.NT]  20 Nov 2019
CHEBOTAREV DENSITY THEOREM IN SHORT INTERVALS
FOR EXTENSIONS OF Fq(T )

LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

Abstract. An old open problem in number theory is whether Chebotarev den-
sity theorem holds in short intervals. More precisely, given a Galois extension E
of Q with Galois group G, a conjugacy class C in G and an 1 ≥ ε > 0, one wants
to compute the asymptotic of the number of primes x ≤ p ≤ x + x
ε with Frobe-
nius conjugacy class in E equal to C. The level of diﬃculty grows as ε becomes
smaller. Assuming the Generalized Riemann Hypothesis, one can merely reach
the regime 1 ≥ ε > 1/2. We establish a function ﬁeld analogue of Chebotarev
theorem in short intervals for any ε > 0. Our result is valid in the limit when
the size of the ﬁnite ﬁeld tends to ∞ and when the extension is tamely ramiﬁed
at inﬁnity. The methods are based on a higher dimensional explicit Chebotarev
theorem, and applied in a much more general setting of arithmetic functions,
which we name G-factorization arithmetic functions.

1. Introduction

The goal of this paper is to provide support to an open problem in the distri-
bution of primes with a given Frobenius conjugacy class. We do this by resolving
a function ﬁeld version of the problem. We start by introducing the problem in
number ﬁelds, and then we present our results.

1.1. The Chebotarev Density Theorem in short intervals. One of the main
theorems in algebraic number theory is the Chebotarev Density Theorem about
the distribution of Frobenius conjugacy classes in Galois extensions of global ﬁelds.
To keep the presentation as simple as possible, we ﬁx the base ﬁeld to be Q. Let
E be a ﬁnite Galois extension of Q with Galois group G = Gal(E/Q) and with
ring of integers OE. For a prime number p, we deﬁne
(E/Q
p
 ) ⊆ G,

2010 Mathematics Subject Classiﬁcation. Primary 11N05; Secondary 11T06, 12F10.
LBS was partially supported by a grant of the Israel Science Foundation. Part of the work
was done while LBS was a member of Simons CRM Scholar-in-Residence Program.
The research of OG was supported by the European Research Council under the European
Union’s Seventh Framework Programme (FP7/2007-2013) / ERC grant agreement n
o 320755.
This research was partially conducted during the period WS served as a Clay Research Fellow,
and partially conducted during the period he was supported by Dr. Max R¨ossler, the Walter
Haefner Foundation and the ETH Zurich Foundation.
1

2 LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

to be the set of all σ ∈ G for which there exists a prime P of E lying above p such
that σ(x) ≡ x
p mod P,

for all x ∈ OE. If p is unramiﬁed in E, then ( E/Q
p ) is called the Frobenius at p
and it is a conjugacy class in G.
The Chebotarev Density Theorem says that as p varies, the Frobenius equidis-
tributes in the set of conjugacy classes (with the obvious weights). More precisely,
let π(x) = #{p ≤ x : p prime number}

be the prime counting function. By the Prime Number Theorem, we know that
Li(x) = ∫ x
2 dt
log t ∼ x
log x well approximates π(x); that is to say, for any A > 1 we
have π(x) = Li(x) + OA(x/(log x)A), x → ∞.

For a conjugacy class C ⊆ G, let

πC(x; E) = # {p ≤ x : p prime number and ( E/Q
p
 ) = C}

be the function that counts primes with Frobenius equals to C. The Chebotarev
Density Theorem [35, Theorem 2.2, Chapter I] says that

(1) πC(x; E) ∼ |C|
|G|Li(x), x → ∞.

This theorem is a vast generalization of the Prime Number Theorem for arithmetic
progressions which follows from (1) applied to cyclotomic ﬁelds.
It is both natural and important for applications to consider the Chebotarev
Density Theorem in short intervals. Balog and Ono [2] studied the non-vanishing
of Fourier coeﬃcients of modular forms in short intervals. For this application
they prove that

(2) πC(x + y; E) − πC(x; E) ∼ |C|
|G| y
log x , x → ∞,

for x
1−1/c(E)+ε ≤ y ≤ x, and where c(E) > 0 is a constant depending only on E
(and in fact only on [E : Q]). Thorner [38, Corollary 1.1] improves the range of y
for which (2) holds true.
Naively, we expect that (2) holds for any y = y(x) ≤ x that grows ‘suﬃciently
fast’. From (1), it follows that the average gap between primes with ( E/Q
p ) = C

is |G|
|C| log x. Thus it makes sense to only consider y-s satisfying limx→∞ y
log x = ∞.
The Maier phenomenon [24] about primes tells us that (2) fails unless y ≫ (log x)A

for all A > 1. A folklore conjecture says that for any ﬁxed ε > 0 and y = x
ε the
asymptotic formula (2) holds true:

CHEBOTAREV DENSITY THEOREM IN SHORT INTERVALS 3

Conjecture 1.1. Let E/Q be a Galois extension with Galois group G, 1 ≥ ε > 0,
and C ⊆ G a conjugacy class. Then

πC(x + x
ε; E) − πC(x; E) ∼ |C|
|G| x
ε

log x , x → ∞.

When E = Q, Conjecture 1.1 reduces to primes in short intervals, and we refer
the reader to the excellent survey [36] for further reading on this case.
One approach for Conjecture 1.1 is to study the error term in Chebotarev Den-
sity Theorem. Let
 ∆E;C(x) = πC(x, E) − |C|
|G| Li(x)

and let dE be the absolute value of the discriminant of E. Under the Riemann
Hypothesis for the Dedekind zeta function ζE of E, Lagarias and Odlyzko [20] gave
the bound

(3) ∆E;C(x) = O(|C|x
1/2(log x + log dE
|G| )),

where the implied constant is eﬀective and absolute. We borrow the above for-
mulation from [34, Theorem. 4]. See [15, Cor. 1] for a calculation of the implied
constants and [25, Cor. 3.7] for an improved dependence on |C|.
From (3), in particular conditionally on the Riemann Hypothesis for ζE, one
immediately gets Conjecture 1.1 for any ε > 1/2. As discussed above, there are
unconditional results. However, the case ε ≤ 1/2 falls beyond the Generalized
Riemann Hypothesis.

1.2. The Chebotarev Density Theorem in function ﬁelds. The function
ﬁeld Chebotarev Density Theorem has a long history, starting with Reichardt [30]
who ﬁrst established it. Lang [21] gave a square-root cancellation, based on the
Riemann Hypothesis for curves over ﬁnite ﬁelds, and explicit estimates were given
by Cohen and Odoni in the appendix to [10] and by Halter-Koch [16, Satz 2].
Fried and Jarden [13, Proposition 6.4.8] and Murty and Scherk [19] gave explicit
bounds on the error term.
However, unlike the number ﬁeld case, there are two obstructions in the Cheb-
otarev Density Theorem. One obstruction comes from the arithmetic part of the
Frobenius and the other appears when considering short intervals. For a more
concise presentation of the obstruction we introduce some notation.
Let q be a power of a prime number p, let Fq be the ﬁnite ﬁeld of q elements,
and let Fq(T ) be the ﬁeld of rational functions over Fq. We deﬁne Pn,q as the
set of primes of Fq(T ) of degree n. If n > 1, we identify Pn,q with the set of
monic irreducible polynomials in the ring of polynomials Fq[T ], and we identify
P1,q with the degree-1 monic polynomials and 1/T ‘the inﬁnite prime’. The prime

4 LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

polynomial theorem says that

πq(n) = #Pn,q = qn

n (1 + O(q−n/2)),

and so we use qn

n as an estimate for πq(n).
Given a Galois extension E/Fq(T ) with Galois group G = Gal(E/Fq(T )), for
each P ∈ Pn,q we deﬁne the Frobenius at P ,

(4) (E/Fq(T )
P
 ) ⊆ G,

as in the number ﬁeld setting: it is the set of σ ∈ G for which there exists a prime
P of E lying above P such that

σ(x) ≡ x
|P | mod P,

for all x ∈ E which are integral at P and where |P | = qn. As before, if P is
unramiﬁed in E, then ( E/Fq(T )
P ) is a conjugacy class in G. Given a conjugacy
class C ⊆ G, we set

πC;q(n; E) = # {P ∈ Pn,q : ( E/Fq(T )
P
 ) = C} ,

the function that counts primes with Frobenius C.
To describe the obstruction for a conjugacy class to be a Frobenius of a prime
of degree n, we introduce the restriction map. Let Fqν be the ﬁeld of scalars of
E, that is, the algebraic closure of Fq in E. Let φ : Fqν → Fqν , φ(x) = x
q be
the generator of the cyclic group G0 = Gal(Fqν /Fq). We have the restriction of
automorphisms map G ։ G0, which is surjective. Since G0 is abelian, if C ⊆ G
is a conjugacy class, then all σ ∈ C map to the same power φC of φ. Then the
Chebotarev Density Theorem for function ﬁelds says that if φC = φn, then

(5) ∣
∣
∣
∣πC;q(n; E) − ν |C|
|G| qn

n
 ∣
∣
∣
∣ ≪ ν |C|
|G| max{genus(E), |G|
ν } qn/2

n

and otherwise πC;q(n; E) = 0. The implied constant is absolute.
Next we turn to short intervals. Following Keating and Rudnick [18, §2.1],
we deﬁne a short interval around a polynomial f of degree n with parameter
0 ≤ m < n to be I(f, m) = {f + g : deg g ≤ m}.

The size of the interval is #I(f, m) = qm+1.

To compare with the number ﬁeld interval {x ≤ n ≤ x + x
ε}, we see that x
corresponds to |f | = qn and x
ε corresponds to qm+1, so ε = m+1
n . Having the
analogy with number ﬁelds in mind, one would naively expect that (5) implies a

CHEBOTAREV DENSITY THEOREM IN SHORT INTERVALS 5

Chebotarev Density Theorem for the short interval I(f, m) whenever m + 1 > n/2
(i.e., ε > 1/2). However, there seems to be no direct such implication. Letting

πC;q(I(f, m); E) = # {P ∈ Pn,q ∩ I(f, m) : (E/Fq(T )
P
 ) = C} ,

then unlike in the number ﬁeld case, we cannot express πC;q(I(F, m); E) as the
diﬀerence of values of πC;q(n; E) in order to utilize the error term (5).
In fact, there is an obstruction to Chebotarev in short intervals coming from the
fact that E is not necessarily linearly disjoint from the cyclotomic ﬁeld Ln−m−1
associated to a power of the inﬁnite prime (see [32, Chapter 12]). Thus one needs
to modify the asymptotic formula according to the intersection of E and Ln−m−1.
Applying (5) to the compositum of ELn−m−1 would yield a Chebotarev in short
intervals for ε > 1/2. We note that the extensions Ln−m−1 are wildly ramiﬁed at
the inﬁnite prime.
Our main result is a Chebotarev Density Theorem for short intervals with any
ε > 0 for extensions that are tamely ramiﬁed at the inﬁnite prime. Thus the result
goes beyond the Riemann Hypothesis. For simplicity of presentation we consider
only geometric extensions. We indicate at the end of the paper how to handle
non-geometric extensions.

Theorem 1.2. For every B > 0 there exists a constant MB satisfying the following
property. Let q be a prime power. Let n > m ≥ 2 if q is odd and n > m ≥ 3
otherwise. Let G be a ﬁnite group and let E/Fq(T ) be a geometric G-extension.
Assume that the inﬁnite prime is tamely ramiﬁed in the ﬁxed ﬁeld Eab in E of the
commutator of G. Further assume that genus(E), n, |G| ≤ B. Let f ∈ Fq[T ] be
monic of degree n. Then
∣
∣
∣
∣ 1
qm+1 πC;q(I(f, m); E) − |C|
|G| 1
n
∣
∣
∣
∣ ≤ MBq−1/2.

It follows in particular that for any ε > 0 we have

(6) lim
n→∞ lim
q→∞ max
f,E
 ∣
∣
∣
∣ 1
qm+1 πC;q(I(f, m); E) − |C|
|G| 1
n
 ∣
∣
∣
∣ = 0,

where E runs over all G-Galois extensions of Fq(T ) of bounded genus that are
tamely ramiﬁed at inﬁnity and f ∈ Fq[T ] runs over all monic polynomials of
degree n. Hence we have proved a version of Conjecture 1.1 in the function ﬁeld
setting.
It would be desirable to change the order of the limits in (6). As explained
above, for ε > 1/2 this follows from the Riemann Hypothesis for curves. For
ε ≤ 1
2, it is open and we know of no approach to attack it. A yet more challenging
task is to ﬁx q and take n → ∞, and also here the problem is open, and we know
of no approach to attack it.
Our method gives more general results, and may be applied for instance to
problems about norms. In Theorem 5.1 we count, in the large-q limit, how many

6 LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

polynomials g ∈ I(f, m) satisfy (g) = NormE/Fq(T )I for some ideal I in OE. Our
most general result is given in Theorem 4.3, for which the terminology of §3–4 is
needed.
It would be interesting to generalize our results to a function ﬁeld of a general
curve in place of Fq(T ).
 2. Methods

We outline our approach when E is a geometric extension of Fq, which, under
the notation used in (5), means that ν = 1. We introduce a general notion of G-
factorization arithmetic functions (Deﬁnition 3.1), which are arithmetic functions
on Fq[T ], whose value on a polynomial f (T ) depends only on the Frobenius at
the prime factors of f (T ). These functions are closely related to Serre’s Frobenian
functions [33] and to the extensions by Odoni [27, 28] and Coleman [11].
Given a short interval, we relate such an arithmetic function ψ to a class function
ψ′ on a subgroup of the wreath product G ≀ Sn using a higher dimensional function
ﬁeld Chebotarev Density Theorem. The main property of this association is that
the expected value of ψ on the short interval is asymptotically equal to the average
of ψ′ on the subgroup, as q → ∞ (Theorem 4.3). The main technical part of the
work is to compute the subgroup: it equals to the wreath product G ≀ Sn itself.
Applying the above to the indicator function of primes with Frobenius C (Ex-
ample 3.2) reduces Theorem 1.2 to either a combinatorial computation in G ≀ Sn
or the classical Chebotarev Density Theorem.
Finally, for the subgroup computation, we take an algebraic approach, using
elementary group theory and Artin-Schreier and Kummer theories. Our methods
are in the spirit of the works [9, 4, 3] which assume genus(E) = 0 and G cyclic.

3. G-factorization arithmetic functions

For a ﬁnite group G we consider the space

ˆΩG = {σI : σ ∈ G, I ≤ G}

of all cosets of subgroups. The group G acts on ˆΩG by conjugation and we write

ΩG = ˆΩG/G

for the set of conjugacy classes of cosets of subgroups. If I = 1 is the trivial
subgroup, we identify σI ∈ ˆΩG with σ. So the image of σI in ΩG is the conjugacy
class C = {τ −1στ : τ ∈ G} of σ.
We want to encode the combinatorial data of degrees, multiplicities, and the
Frobenius at the prime factors of a polynomial. A G-factorization type is a
function λ : N × N × ΩG → Z≥0

CHEBOTAREV DENSITY THEOREM IN SHORT INTERVALS 7

with ﬁnite support. We deﬁne Λ = ΛG to be the set of all G-factorization types.
For λ ∈ Λ we let
 deg(λ) = ∑

d,e,ω λ(d, e, ω)de,

where the sum runs over d, e ∈ N and ω ∈ ΩG. For a monic polynomial f ∈ Fq[T ]
with prime factorization f = P e1
1 · · · P er
r and for a G-Galois extension E/Fq(T ) we
deﬁne
 λf ;E/Fq(T )(d, e, ω) = # {i : deg Pi = d, ei = e, (E/Fq(T )
Pi
 ) = ω} .

When there is no risk of confusion we simplify the notation and write λf for
λf ;E/Fq(T ). Obviously, we have that deg(f ) = deg(λf ).

Deﬁnition 3.1. A G-factorization arithmetic function is a function on G-
factorization types. We denote by

Λ∗ = {ψ : Λ → C}

the space of G-factorization arithmetic functions.
Given a G-Galois extension E/Fq(T ), each ψ ∈ Λ∗ induces an arithmetic func-
tion ψE/Fq(T ) on Fq[T ] by setting

ψE/Fq(T )(f ) = ψ(λf ;E/Fq(T )),

for monic f ∈ Fq[T ]. By abuse of notation, ψE/Fq(T ) is also called G-factorization
arithmetic function.

Deﬁnition 3.1 vastly extends some families of arithmetic functions – see [31, 5]
for similar deﬁnitions in the cases E = Fq(T ) (G = {e}) and E = Fq(√−T )
(G = Z/2Z).
The following example of a G-factorization arithmetic function is crucial for our
main result.

Example 3.2. Fix a conjugacy class C ⊆ G. Consider the G-factorization arith-
metic function

1C(λ) =
 {
1, if λ(d, e, ω) > 0 ⇒ ω = C and d = deg λ,
0, otherwise.

For any G-Galois extension E/Fq(T ) and monic f ∈ Fq[T ] we have

1C,E/Fq(T )(f ) =
 {1, if f is irreducible and ( E/Fq(T )
f ) = C,

0, otherwise.

8 LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

4. G-factorization arithmetic functions on wreath products

Recall the construction of the permutational wreath product: Let Sn be
the symmetric group on X = {1, 2, . . . , n} (with left action (σ, x) ↦→ σ.x), let G
be a ﬁnite group, and let GX := {ξ : X → G}
be the group of functions from X to G with pointwise multiplication. Then Sn
acts (from the right) on GX by

ξσ(x) = ξ(σ.x), σ ∈ Sn, x ∈ X.

The corresponding semidirect product

G ≀ Sn := GX ⋊ Sn
is the wreath product of G and Sn. For the reader’s convenience we recall that
the multiplication is given by

(ξ1, σ1)(ξ2, σ2) = (ξ1ξσ−1
1
2 , σ1σ2), ξ1, ξ2 ∈ GX, σ1, σ2 ∈ Sn.

The imprimitive action of G ≀ Sn on the set G × X, given explicitly by

(7) (ξ, σ).(g, x) = (ξ(σ.x)g, σ.x), ξ ∈ GX, σ ∈ Sn, g ∈ G, x ∈ X,

makes G ≀ Sn into a transitive permutation group.
For (ξ, σ) ∈ G ≀ Sn we attach a G-factorization type: Let σ = σ1 · · · σr be
the factorization of σ to disjoint cycles. We include the trivial cycles so that∑r
i=1 ord(σi) = n. For each i = 1, . . . , r, if we write σi = (j1 · · · jd), then we set
C(ξ,σ),σi to be the conjugacy class in G of the element

ξ(jd) · · · ξ(j1).

The conjugacy class C(ξ,σ),σi is well deﬁned, since ξ(ja) · · · ξ(j1)ξ(jd) · · · ξ(ja+1) is
conjugate to ξ(jd) · · · ξ(j1). Now we set

(8) λ(ξ,σ)(d, e, ω) =
 {
0, if e > 1,
#{i : ord(σi) = d, C(ξ,σ),σi = w}, if e = 1.

Any ψ ∈ Λ∗ induces a function ψG≀Sn : G ≀ Sn → C by

ψG≀Sn((ξ, σ)) = ψ(λ(ξ,σ))

and we refer to such functions on G ≀ Sn as G-factorization arithmetic functions as
well. Below we show that the set of G-factorization arithmetic functions on G ≀ Sn
actually coincides with the set of class functions.

Example 4.1. Recall the G-factorization arithmetic function 1C from Exam-
ple 3.2. Then, for (ξ, σ) ∈ G ≀ Sn we have

1C(ξ, σ) =
 {1, if σ is an n-cycle and C(ξ,σ),σ = C,
0, otherwise.

CHEBOTAREV DENSITY THEOREM IN SHORT INTERVALS 9

Next, we prove that conjugation in G ≀ Sn preserve the G-factorization type. Let
τ ∈ Sn and identify it with (1, τ ) ∈ G≀Sn. Then τ στ −1 = ρ1 · · · ρr with ρi = τ σiτ −1.
If σi = (j1 · · · jd), then ρi = (τ (j1) · · · τ (jd)). Now, as τ (ξ, σ)τ −1 = (ξτ −1, τ στ −1)
we have that

(9) ξτ −1(τ (jd)) · · · ξτ −1(τ (j1)) = ξ(jd) · · · ξ(j1)

and so C(ξ,σ),σi = Cτ (ξ,σ)τ −1,ρi. We thus conclude that

λ(ξ,ρ) = λτ (ξ,ρ)τ −1.

Similarly, if η ∈ GX and we identify it with (η, 1) ∈ G ≀ Sn, then

(10) η(ξ, σ)η−1 = (ηξη−σ−1, σ)

and we have

(ηξη−σ−1)(jd) · · · (ηξη−σ−1(j1))

= η(jd)ξ(jd)η(jd−1)−1 · η(jd−1) · · · η(j1)−1 · η(j1)ξ(j1)η(jd)−1

= η(jd)ξ(jd) · · · ξ(j1)η(jd)−1.

Here we used that σ−1
i = (jd · · · j1). In particular, C(ξ,σ),σi = Cη(ξ,σ)η−1,σi and thus

λ(ξ,ρ) = λη(ξ,ρ)η−1 .

We thus deduce that if (ξ, σ) and (η, ρ) are conjugate, then λ(ξ,ρ) = λ(η,ρ).
The converse is also true. Indeed, λ(ξ,σ) = λ(ζ,ρ) implies that we have r conjugacy
classes C1, . . . , Cr (possibly with repetitions) and factorization to disjoint cycles
ρ = ρ1 · · · ρr and σ = σ1 · · · σr such that ord(σi) = ord(ρi) and

C(ξ,σ),σi = Ci = C(ζ,ρ),ρi.

Without loss of generality we may assume that σ = ρ and σi = ρi for all i (indeed,
conjugate by τ ∈ Sn such that τ σiτ −1 = ρi for all i and use (9)). Thus, if
σi = (j1 · · · jd), then
 gξ(jd) · · · ξ(j1)g−1 = ζ(jd) · · · ζ(j1)

for some g ∈ G. By (10) it suﬃces to ﬁnd η ∈ GX such that ηξη−σ−1 = ζ. Deﬁning

η(jd) = g and η(ja) = ζ −1(ja+1)η(ja+1)ξ(ja+1), 1 ≤ a ≤ d − 1

on the orbits of σi, for each σi gives the desired solution. We thus proved

Lemma 4.2. The elements (ξ, σ), (ζ, ρ) ∈ G ≀ Sn are conjugate if and only if
λ(ξ,σ) = λ(ζ,ρ).
In particular, every class function on G ≀ Sn may be realized as a G-factorization
arithmetic function.

10 LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

We prove the following general theorem which connects the averages of a G-
factorization arithmetic function on a short interval to the average on the wreath
product. A piece of notation is needed: for a non-empty ﬁnite set X and a function
ψ on X we denote the mean value by

⟨ψ(f )⟩f ∈X := 1
#X
 ∑

f ∈X ψ(f ).

Theorem 4.3. For every B > 0 there exists a constant MB satisfying the following
property. Let q be a prime power. Let n > m ≥ 2 if q is odd and n > m ≥ 3
otherwise. Let G be a ﬁnite group and let E/Fq(T ) be a geometric G-extension.
Assume that the inﬁnite prime is tamely ramiﬁed in the ﬁxed ﬁeld Eab in E of the
commutator of G. Let f0 ∈ Fq[T ] be monic of degree n, and ψ ∈ Λ∗. Assume that
genus(E), n, |G| ≤ B. Then
∣
∣
∣
〈
ψE/Fq(T )(f )〉

deg(f −f0)≤m − ⟨ψG≀Sn(τ )⟩τ ∈G≀Sn
∣
∣
∣ ≤ MBq−1/2 max
deg(λ)=n |ψ(λ)|.

We postpone the proof of Theorem 4.3 to §7.

5. Applications of Theorem 4.3

From Theorem 4.3 it follows immediately that in the large-q limit, the average
on a short interval is the same as on the ‘long interval’ — the set of all degree-n
monics Mn,q = I(T n, n − 1).
Moreover, Theorem 4.3 reduces the computations of averages of arithmetic func-
tions to combinatorics of group theory. This also works vice versa.

5.1. Proof of Theorem 1.2. We give two proofs to exemplify the ways to apply
Theorem 4.3.

First proof: The assumptions allow us to apply Theorem 4.3 with the G-
factorization arithmetic function 1C, and to get that the average on a short interval
is the same as over a long interval. The latter is given by (5), as needed.

Second proof: The assumptions allow us to apply Theorem 4.3 with the G-
factorization arithmetic function 1C, and to get that the average on a short in-
terval is the same as on the wreath product. We compute the latter: Using
Example 4.1, we ﬁnd that 1C(ξ, σ) ̸= 0 implies that σ = (j1 · · · jn) is an n-cycle
and ξ(jn) · · · ξ(j1) ∈ C. So we may choose ξ(j1), . . . , ξ(jn−1) arbitrarily and then
we have |C| choices for ξ(jn). So

⟨1C(ξ, σ)⟩(ξ,σ)∈G≀Sn = (n − 1)!|G|n−1|C|
n!|G|n = 1
n |C|
|G|,

as needed. □

CHEBOTAREV DENSITY THEOREM IN SHORT INTERVALS 11

5.2. Norms in short intervals. Here we discuss two G-factorization arithmetic
functions related to norms, and our results on their mean value in short intervals.
For a function ﬁeld E/Fq(T ), we deﬁne the following arithmetic functions. For
f ∈ Mn,q, we deﬁne

bE/Fq(T )(f ) =
 {
1, if ∃I ⊆ OE : (f ) = NormE/Fq(T )(I),
0, otherwise,

rE/Fq(T )(f ) = #{I ideal in OE : NormE/Fq(T )(I) = (f )}.

The number ﬁeld versions of r, b were studied extensively: Let E/Q be a ﬁnite
extension. Odoni [26, Thm. 1] computed the asymptotic of the mean value of bE/Q.
When E/Q is Galois, the work of Ramachandra [29] gives the mean value of bE/Q
in [x, x + x
ε] for some 0 < ε < 1.
Weber [39] computed the mean value of rE/Q, and studied the error term. We
refer to Bourgain and Watt [7, Thm. 2] for the state-of-the-art result on the error
term when E = Q(i), and to Lao [22] for more general E. These results in
particular gives the expected asymptotics for the mean value of rE/Q in [x, x + x
ε]
for some 0 < ε < 1.
In Appendix A, we prove a function ﬁeld analogue of Odoni’s result on the
average of bE/Fq(T ) in long intervals when E/Fq(T ) is Galois. This is to be done
in the most general limit qn → ∞. Appendix A also treats rE/Fq(T ) for which the
rationality of the corresponding Dedekind zeta function gives a closed formula for
the mean value.
The result to be presented is a computation of the mean values in short intervals.

Theorem 5.1. For every B > 0 there exists a constant MB satisfying the following
property. Let q be a prime power. Let n > m ≥ 2 if q is odd and n > m ≥ 3
otherwise. Let G be a ﬁnite group and let E/Fq(T ) be a geometric G-extension
which has is tamely ramiﬁed at the inﬁnite prime. Let f0 ∈ Fq[T ] monic of degree
n. Assume that genus(E), n, |G| ≤ B. Then
〈
bE/Fq(T )(f )〉

deg(f −f0)≤m = 1 + OB(q−1/2),

〈
rE/Fq(T )(f )〉

deg(f −f0)≤m = (n + 1
|G| − 1
n
 ) + OB(q−1/2).

To see how Theorem 5.1 is deduced from Theorem 4.3 we need to express r, b
as G-factorization arithmetic functions (Example 5.3) and to compute the mean
value on the wreath product, or alternatively apply the results from Appendix A.
Let E/Fq(T ) be a Galois extension. Given a prime polynomial P ∈ Fq[T ], we
denote by g(P ; E), f (P ; E) and e(P ; E) the number of distinct primes in E lying
above P , the inertia degree of P in E and the ramiﬁcation index of P , respectively.

Lemma 5.2. Let E/Fq(T ) be a geometric G-extension.
(1) The functions bE/Fq(T ) and rE/Fq(T ) are multiplicative.

12 LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

(2) Let f ∈ Mn,q with prime factorization f = ∏k
i=1 P ai
i . Then

(11) bE/Fq(T )(f ) =
 {1, if f (Pi; E) | ai for all i,
0, otherwise,

and if we put bi = ai/f (Pi; E) and gi = g(Pi; E), then we have

(12) rE/Fq(T )(f ) = bE/Fq(T )(f ) ·
 k∏

i=1
 (
bi + gi − 1
gi − 1
 )
.

Proof. Let P be a prime polynomial and let P be a prime ideal of OE lying above
P . Then NormE/Fq(T )P = (P )f (P ;E).
By multiplicativity of the norm map and by unique factorization in OE, it follows
that the image of NormE/Fq(T ) on the non-zero ideals in OE is the semigroup
generated by {(P )f (P ;E)}P ∈Pq , which establishes (11). It now immediately follows
that bE/Fq(T ) is multiplicative.
If f1 and f2 are relatively prime polynomials, then from unique factorization
of ideals in OE, every ideal I of OE with NormE/Fq(T )I = (f1f2) has a unique
factorization I = I1I2, with NormE/Fq(T )Ij = (fj). Indeed, if I = ∏ P
ai
i take Ij be
the product of P
ai
i with Pi | fj. Thus,

rE/Fq(T )(f1f2) = ∑

NormE/Fq (T )I=(f1f2) 1 = ∑

NormE/Fq (T )I1=(f1)
NormE/Fq (T )I2=(f2)
 1 = rE/Fq(T )(f1)rE/Fq(T )(f2).

This implies that rE/Fq(T ) is multiplicative. In particular, it suﬃces to prove (12)
for f = P a a prime power.
If f (P ; E) ∤ a, then bE/Fq(T )(P a) = 0, hence also rE/Fq(T )(P a) = 0. Assume now
that f (P ; E) | a and let b = a/f (P ; E). Let P1, . . . , Pg be the primes of OE lying
above P . Since NormE/Fq(T )Pj = P f (P ;E), the solutions to NormE/Fq(T )I = P a,
are of the form I = ∏g
j=1 P
cj
j with cj ≥ 0 and ∑g
j=1 cj = b. As there are (
b+g−1
g−1 )

many such sequences of cj, the proof is done. □

Lemma 5.2 allows us to realize bE/Fq(T ), rE/Fq(T ) as G-factorization arithmetic
functions.

Example 5.3. Let ω ∈ ΩG, and let Σ ∈ ω. So Σ is a coset of a subgroup of G,
say Σ = σI. Let eω = |I|, fω = [⟨σ, I⟩ : I], and gw = |G|/ewfw. Now we deﬁne the
G-factorization arithmetic functions

b(λ) =
 {1, if λ(d, a, ω) > 0 ⇒ fω | a,
0, otherwise.

r(λ) = b(λ) · ∏

(d,a,w)
 (
a/fw + gw − 1
gw − 1
 )λ(d,a,w)(13)
 CHEBOTAREV DENSITY THEOREM IN SHORT INTERVALS 13

Let E/Fq(T ) be a geometric G-Galois extension. Then

(14) bE/Fq(T )(f ) = b(λf ;E/Fq(T )) and rE/Fq(T )(f ) = r(λf ;E/Fq(T )).

Indeed, by (11) and (12), it suﬃces to note that w = ( E/Fq(T )
P ), then ew = e(P ; E),
fw = f (P ; E), and gw = g(P ; E).

Proof of Theorem 5.1. By Theorem 4.3, it suﬃces to compute the average of the
G-factorization arithmetic functions b and r given in (14) on the group G ≀ Sn. For
brevity we compute them together by computing the average of rs for any s ∈ C
(and noting that r = r1 and b = r0). Put N = |G| and let s ∈ C. We show that

〈
rs
G≀Sn(ξ, σ)〉

(ξ,σ)∈G≀Sn = (
n + N s−1 − 1
n
 )
.

Let σ = σ1 · · · σr be the factorization of σ ∈ Sn to disjoint cycles and let ξ ∈ Gn.
Recall that if we write σi = (j1 · · · jℓ), then C(ξ,σ),σi is deﬁned to be the conjugacy
class of the element ξ(jℓ) · · · ξ(j1).

Let d, a ≥ 1 and ω ∈ ΩG with λ(ξ,σ)(d, a, ω) > 0. Then a = 1 and ω = C(ξ,σ),σi
for some i. In particular, eω = 1, and thus fω = 1 if and only if C(ξ,σ),σi = 1, where
eω and fω are as deﬁned in Example 5.3.
By (13), we have that rs
G≀Sn(ξ, σ) ̸= 0 if and only if fω | a for all (d, a, ω)
with λ(ξ,σ)(d, a, ω) > 0. So if rs
G≀Sn(ξ, σ) ̸= 0, then a = 1, hence fω = 1, and so
C(ξ,σ),σi = 1, for all i. As gω = N
eωfω = N, and so (a/e+g−1
g−1 ) = N, we deduce from
(13) that

rs
G≀Sn(ξ, σ) =
 {∏

(d,a,ω):λ(ξ,σ)(d,a,ω)>0 N sλ(ξ,σ)(d,a,ω), if C(ξ,σ),σi = 1 for all i,

0, otherwise.

Put Xn = {(ξ, σ) ∈ G ≀ Sn : C(ξ,σ),σi = 1, ∀i},

so that

(15) 〈
rs
G≀Sn(ξ, σ)〉

(ξ,σ)∈G≀Sn =
 ∑

(ξ,σ)∈Xn(N s)r(σ)

#G ≀ Sn ,

where r(σ) is the number of cycles in σ. For a ﬁxed σ ∈ Sn with a factorization
σ = σ1 . . . σr to disjoint cycles, we have

(16) ∑

ξ∈Gn:(ξ,σ)∈Xn(N s)r(σ) = (N s)rN n−r = N n · (N s−1)r,

since if σi = (j1 . . . jd), then ξ(j1), . . . , ξ(jd−1) can be chosen arbitrarily and ξ(jd)
must be equal to ∏d−1
k=1 ξ(jk)−1, so we lose one power of N for each orbit. Plugging

14 LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

(16) in (15), we ﬁnd that

(17) 〈
rs
G≀Sn(ξ, σ)〉

(ξ,σ)∈G≀Sn =
 ∑

σ∈Sn(N s−1)r(σ)

#Sn .

We apply the exponential formula for permutations [37, Cor. 5.1.9] with f (i) =
N s−1 the constant function and h deﬁned by h(0) = 1 and

h(i) = ∑

σ∈Si(N s−1)r(σ).

Then the formula gives that

E(x) :=
 ∞∑

i=0 h(i) x
i

i! = exp(∑

i≥1 N s−1 x
i

i ).

As ∑

i≥1 x
i/i = − ln(1 − x), we can simplify the right hand side using the binomial
series to get that
 E(x) = (1 − x)−N s−1 = ∑

i≥0 (−1)i(
−N s−1

i
 )
x
i.

In particular, by (17) we have

〈
rs
G≀Sn(ξ, σ)〉

(ξ,σ)∈G≀Sn = h(n)
n! = (−1)n(
−N s−1

n
 ) = (n + N s−1 − 1
n
 ),

as needed. □

6. Galois Theory

6.1. G-factorization arithmetic functions and the Frobenius automor-
phism. Let ψ be a G-factorization arithmetic function and E/Fq(T ) a G-Galois
geometric extension. The goal of this section is, for a given a = (a0, . . . , an−1) ∈ Fn
q ,
to naturally construct an element φa ∈ G ≀ Sn such that

(18) ψE/Fq(T )(T n + an−1T n−1 + · · · + a0) = ψG≀Sn(φa).

We start with a general construction which we later specialize to our setting. Let F
be a ﬁeld and π : C → A1
F a branched covering of smooth geometrically connected
F -curves with function ﬁeld extension E/F (T ). Assume that E/F (T ) is Galois
with Galois group G.

CHEBOTAREV DENSITY THEOREM IN SHORT INTERVALS 15

This gives rise to the following cover of varieties with corresponding function
ﬁelds

(19) C n

πn
  
 E1 · · · En

An
F

s
  
 F (Y1, . . . , Yn)

An
F = An/Sn F (A0, . . . , An).

Here Sn acts on An by permuting the coordinates: if (Y1, . . . , Yn) are the coordi-
nates of An and (A0, . . . , An−1) of An = An/Sn, then the map s is given by

A0 = (−1)nY1 · · · Yn , . . . , An−1 = −(Y1 + . . . + Yn).

Also, Ei is the function ﬁeld of the i-th copy of C in C n, in particular, for every i
there exists an isomorphism

(20) ϕi : Ei → E

with ϕi(Yi) = T that ﬁxes F . Put ϕi,j : Ei → Ej to be ϕ−1
j ◦ ϕi. Let D1(T )Fq[T ] be
the discriminant ideal of π and D2(A0, . . . , An−1) = discT (T n+An−1T n−1+. . .+A0)
and put

(21) D(A0, . . . , An−1) = D2(A0, . . . , An−1) ∏

i D1(Yi) ∈ F [A0, . . . , An−1]

which is a non-zero polynomial in the Ai-s. Then, for a point a ∈ An(F ) we have

(22) D(a) ̸= 0 =⇒ a is unramiﬁed in C n.

If we write f (T ) = T n + an−1T n−1 + · · · + a0, then the condition D(a) ̸= 0 is
equivalent to f being a separable polynomial that does not vanish on the branch
points of π which are exactly the roots of D1. The Riemann-Hurwitz formula (see
e.g. [13, Thm. 3.6.1]) gives that deg D1 ≪ genus(C) + |G|. On the other hand,
deg D2 ≪ n. So, if B ≥ max{genus(C), |G|, n} then deg D is bounded in terms of
B.
The extension E1 · · · En/F (A1, . . . , An) is a Galois extension with Galois group
isomorphic to G ≀ Sn. More explicitly, the action of an element (ξ, σ) ∈ G ≀ Sn on
E1 · · · En is given by

(ξ, σ).ei = ξ(σ(i))(ϕi,σ(i)(ei)), ei ∈ Ei.(23)

This is compatible with the imprimitive action (7).
If F = Fq is a ﬁnite ﬁeld, then any point a ∈ An(F ) with D(a) ̸= 0 induces a
Frobenius conjugacy class φa ⊆ G ≀ Sn, which is the higher dimensional version of
(4) and is deﬁned similarly. Now we can prove (18):

16 LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

Proposition 6.1. Let F = Fq, let f (X) = T n + an−1T n−1 + · · · + a0 ∈ Fq[T ] such
that the point a = (a0, . . . , an−1) is unramiﬁed in C n and let φa ⊆ G ≀ Sn be the
Frobenius conjugacy class. Then (18) holds for every ψ ∈ Λ∗ .

Proof. To ease notation we identify each of the Ei with E via the map φi. Let
f = P1 · · · Pr be the prime factorization of f with Pi monic irreducible of degree
di. For each i = 1, . . . , r, let αi,1 ∈ A1(Fq) be a root of Pi and βi,1 ∈ C(Fq) with
αi,1 = π(βi,1) and let αi,j = αqj−1
i,1 be the other roots, and respectively βi,j = βqj−1
i,j ,
j = 1, . . . , di − 1. We replace the indices of C n and of the middle An in (19) to be
I = {(i, j) : i = 1, . . . , r, j = 1, . . . , di}.
So (βi,j)(i,j)∈I ∈ C n(Fq) maps under πn to (αi,j)(i,j)∈I ∈ An(Fq) which maps
under s to a = (a0, . . . , an−1) ∈ An(Fq).
To this end, let φa be the corresponding Frobenius element of (βi,j)(i,j)∈I and let
h ∈ Ei,1 be a rational function that is regular at all βi,j. Then, by deﬁnition,

(φdi
a h)(βi,1) = (h(βi,1))qdi .

Write φa = (ξ, σ); then φdi
a = (∏di
k=1 ξσk−1, σdi). The coordinate σ ∈ Sn is induced
from the action of the Frobenius automorphism on the roots of f , so since αi,j =
αqj−1
i,1 , we have that Yi,j = σj(Yi,1), j = 0, . . . , di − 1 and Yi,1 = σdi(Yi,1). The latter
also implies that Ei,1 maps to itself under σdi, hence

(φdi
a h)(βi,1) = (
 di∏

k=1 ξσk−1(i, 1)h)(βi,1) = (
 di∏

j=1 ξ(i, j)h)(βi,1).

To conclude, we obtained

(
 di∏

j=1 ξ(i, j)h)(βi,1) = (h(βi,1))qdi ,

but the Frobenius at Pi in E is the unique element of G satisfying this, so FrobPi =
∏di
j=1 ξ(i, j). Thus, λφa = λf ;E/Fq(T ), which completes the proof. □

6.2. Computation of a Galois group. We keep the notation as in §6.1, in
particular F is a ﬁeld and π : C → A1
F is a branched covering of geometrically
irreducible F -curves that is generically Galois with Galois group G. For a =
(a0, . . . , an−1) ∈ An and for 0 ≤ m < n, we consider the following subspace of An

(24) W = Wa,m = {(w0, . . . , wn−1) ∈ An : wi = ai, i = m+1, . . . , n−1} ∼= Am+1.

So if An is the space of coeﬃcients of polynomials, then W is the short interval
I(T n + an−1T n−1 + · · · + a0, m). Let U and V be irreducible components of (s ◦
πn)−1(W ) and s−1(W ), respectively. Let M, L, and K be the function ﬁelds of U,
V , and W , where A0, . . . , Am are independent variables and the yi-s satisfy

CHEBOTAREV DENSITY THEOREM IN SHORT INTERVALS 17

C n

πn
  
 Uoo
 πn
  
 M

An
F

s
  
 Voo
 s
  
 L = K(y1, . . . , yn)

An
F Woo K = F (A0, . . . , Am)

Figure 1. Variety and ﬁeld diagrams

f (T ) = T n + an−1T n−1 + · · · + am+1T m+1 + AmT m + · · · + A0 =
 n∏

i=1(T − yi).

Then, M/K is a Galois extension and if D(an−1, . . . , am+1, Am, . . . , A0) ̸= 0, then
by (22), it is unramiﬁed, hence its Galois group is canonically isomorphic to the
subgroup the generic Galois group G ≀ Sn given in (23); namely all elements that
generically map U to itself. We identify Gal(M/K) with this subgroup, in partic-
ular H = Gal(M/L) ≤ Gn.

We have that Gal(M/K) equals G ≀ Sn if and only if (s ◦ πn)−1(W ) is irreducible,
i.e. equals to U.
We prove that this is indeed the case if the ramiﬁcation at inﬁnity is tame.

Proposition 6.2. Under the notation above, assume that m ≥ 2 if q is odd and
m ≥ 3 if q is even. Further assume that the inﬁnite prime is tamely ramiﬁed in
the ﬁxed ﬁeld Eab in E of the commutator of G. Then

Gal(M/K) = G ≀ Sn.

Remark 6.3. Proposition 4.6 in [3] coincides with the special case of Proposi-
tion 6.2 where G = Z/2Z, C = A1 and π(x) = x
2. Cyclic extensions with genus 0
were partly treated by Cohen [9, Thm. 12].

6.2.1. Reduction steps. Since by [4, Proposition 3.6], Gal(L/K) = Sn and since
Gal(M/K) ≤ G ≀ Sn, in order to prove that Gal(M/K) = G ≀ Sn it suﬃces to show
that H = Gn.
The proof of Proposition 6.2 is reduced, by elementary ﬁnite group theory, to
the following statements:

Lemma 6.4. Proposition 6.2 holds true if G is abelian.

Lemma 6.5. For each i ̸= j the projection on the i, j-th coordinates H → Gn →
G2 is surjective.

18 LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

Proof that Lemmas 6.4 and 6.5 imply Proposition 6.2. From Lemma 6.4 applied
to the abelianization Gab of G, we get that H surjects onto (Gab)n. This in
particular means that H is contained in no proper normal subgroup with abelian
quotient. By Lemma 6.5, H surjects onto any projection to two coordinates. To
ﬁnish the proof we need that these two group theoretical properties suﬃce to imply
that H = Gn and this is indeed the case, as the lemma below shows. □

Lemma 6.6. Let H be a subgroup of Gn. Suppose that H maps surjectively onto
G2 under each possible projection onto two copies. If H is a proper subgroup of
Gn, then it is contained in a proper normal subgroup with abelian quotient.

Proof. The case n = 2 is trivial, and by induction, we may assume this is true for
n − 1 and that n ≥ 3. If any map from H to the product of n − 1 copies of G is not
surjective, then the image of H is contained in a normal subgroup with abelian
quotient, so H is as well. So we may assume that the projections from H to any
product of n−1 copies of G are surjective. Now apply Goursat’s lemma to Gn−1 and
G. We get that there is a group G′, surjections a : Gn−1 → G′ and b : G → G′, such
that H consists of tuples (g1, . . . , gn) in Gn with a(g1, ..., gn−1) = b(gn). Moreover
since H is a proper subgroup, G′ is non-trivial.
Now because the map H → Gn−1 obtained by dropping the i-th coordinate is
surjective, for any gn there exists some gi such that (e, . . . , e, gi, e, . . . , gn) ∈ H,
and so a(e, . . . , e, gi, . . . , e) = b(gn). Putting G1 = {(g1, e, . . . , e) : g1 ∈ G} and
G2 = {(e, g2, e, . . . , e) : g2 ∈ G}, we conclude that a maps both G1 and G2 onto G′.
Thus as G1 and G2 commute, we get that G′ must be abelian. Thus the pre-image
of G′ is the desired normal subgroup with abelian quotient. □

To ﬁnish the proof of Proposition 6.2, it remains to prove Lemmas 6.4 and 6.5.
Since the former lemma is technical, we start by proving the latter assuming the
former.

6.2.2. Proof of Lemma 6.5 using Lemma 6.4. We look at the covering Υ of W
deﬁned by adjoining two roots yi, yj of the polynomial; i.e., Υ is the quotient space
of V under the action of Sn−2, so Gal(V /Υ) ∼= Sn−2, the group of all permutations
ﬁxing i, j. Let Γ be the Galois group of U/Υ. So, the restriction-of-automorphisms
map induces a surjection Γ → Gal(V /Υ) = Sn−2.
The covering Υ maps to A2 by sending to the two roots. The ﬁbers are connected
because we just add two congruence conditions. We have the covering C 2 → A2

with Galois group G2, and its ﬁber product Υ ×A2 (C 2) is geometrically connected,
since the ﬁber of Υ → A2 is geometrically connected. This implies that Γ surjects
onto G2.
We apply Goursat’s lemma to these two maps. They are jointly surjective unless
some quotient of G2 matches some quotient of Sn−2. But all normal subgroups of
Sn−2 are contained in An−2, so this can only happen if there is some non-trivial
relation with order two quotients of G. This is not possible by the abelian case,
hence the proof is done. □

CHEBOTAREV DENSITY THEOREM IN SHORT INTERVALS 19

The proof of Lemma 6.4 is more technical and requires some preparation.

6.2.3. Some more group theory. This section contains well known facts that we
summarize for the convenience of the reader. We start by stating two well known
facts on the symmetric group. The ﬁrst is on normal subgroups:

Lemma 6.7. Let n ≥ 1. The group Sn does not have any normal subgroups of
odd prime index.

The second is about the invariant subspaces of the standard representation of
Sn on Fn
p acting by permuting the coordinates.

Lemma 6.8. The invariant subspaces of Fn
p under Sn (n ≥ 3) are:
(1) V0 = {(0, . . . , 0)},
(2) V1 = spFp{(1, . . . , 1)},
(3) Vn−1 = {(x1, . . . , xn) ∈ Fn
p : ∑n
i=1 xi = 0}, and
(4) Vn = Fn
p .

Recall that the Frattini subgroup Φ(G) of a group G is deﬁned by Φ(G) =⋂
U ≤mG U, where the intersection is over the maximal subgroups of G. It has the
property that for every H ≤ G, if H/H ∩ Φ(G) = G/Φ(G), then H = G. If G is
ﬁnite and p | |G|, then the subgroup Φp(G) = [G, G]Gp generated by commutators
and p-th power of elements is normal and G/Φp(G) ∼= (Z/pZ)r. Thus,

(25) Φp(G) = U1 ∩ · · · ∩ Ur,

with Ui the kernel of the projection on the i-th coordinate, so Ui is normal in G
of index p.

Lemma 6.9. Let G be a ﬁnite abelian group and H ≤ G. Assume that H/(H ∩
Φp(G)) ∼= G/Φp(G) for every p | |G|. Then H = G.

Proof. Since G is abelian, Φ(G) = ⋂
p||G| Φp(G) and G/Φ(G) ∼= ∏

p||G| G/Φp(G).
So the assumption gives that H/(H ∩ Φ(G)) = G/Φ(G) and so H = G. □

Let L be a ﬁeld and p a prime. If p ∤ char(L) let ℘(x) = x
p and L
◦ = L
×,
otherwise let ℘(x) = x
p − x and L
◦ = L. We say that elements in L
◦ are p-
independent if they are linearly independent in L
◦/℘(L
◦), considered as a Fp-vector
space.

Lemma 6.10. Let G be a ﬁnite abelian group and H ≤ G. Let L be a ﬁeld such
that for every p | |G|, either L contains a primitive p-th root of unity or L is of
characteristic p. Let M/L be an H-Galois extension. For a prime divisor p of |G|,
put U1, . . . , Ur(p) as in (25). Then, for every 1 ≤ i ≤ r there exists αi,p ∈ L such
that M H∩Ui = L(βi,p), ℘(βi,p) = αi,p.
Moreover, if α1,p, . . . , αr(p),p are p-independent for all p | |G|, then H = G.

20 LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

Proof. First we note that H/(H ∩Ui) ≤ G/Ui = Z/pZ so Gal(M H∩U )i/L) ≤ Z/pZ,
and Kummer theory (if char(L) ̸= p) or Artin-Schreier theory (otherwise) give us
the required elements αi,p. Now, if the αi,p-s are p-independent, then by (25),
Kummer theory and Artin-Schreier theory, we ﬁnd that

(Z/pZ)r(p) ∼= Gal(M H∩Φp(G)/L) ∼= H/(H ∩ Φp(G)).

So by Lemma 6.9, H = G. □

6.2.4. Rational functions. We borrow the following from [3, Lem. 4.5].

Lemma 6.11. Let ˜f (T ) ∈ K[T ] be a separable polynomial and let f (T ) = ˜f (T ) +
A ∈ K(A)[T ] where A is transcendental over K(T ). Then disc(f ) ∈ K[A] is not
divisible by A.

Lemma 6.12. Let F be a ﬁeld and let A = (A1, . . . , Am) be an m-tuple of variables
(m ≥ 2). Let α = (α1, . . . , αm) be an m-tuple of scalars from F . Let f0(T ) ∈ F [T ]
be a polynomial of degree > m. Then F (A, T ) = f0(T ) + ∑m
i=1 AiT i + ∑m
i=1 Aiαi
is separable in T .

Proof. It suﬃces to show that F is irreducible in T , because F ′ is linear in A1 and
in particular non-zero. Since F is primitive in T , it is irreducible in T if and only
if it is irreducible in R = F (A2, . . . , Am)[A1, T ] by Gauss’s lemma. Since

F = (T + α1)A1 + G,

with G = f0(T ) + ∑

i>1 Ai(T i + αi), either F is primitive in A1, then again by
Gauss it is irreducible in A1 and thus in T , or T + α1 divides G in R. In the
latter case, H = A1 + G
T +α1 is irreducible in T (again primitivity and linearity) and
degA2 ∂H
∂T = 1 hence it is non-zero, so H is separable in T . Moreover, H|T =−α1 ̸= 0,
so we get that F = (T + α1)H is separable, as needed. □

Lemma 6.13. Let F be an algebraically closed ﬁeld of characteristic p. Let A =
(A0, . . . , Am) be an (m+1)-tuple of variables, m ≥ 1. Let f0(T ) ∈ F [T ] be a monic
polynomial of degree n > m. Let f (T ) = f0(T ) + ∑m
i=0 AiT i be a polynomial with
coeﬃcients in K = F (A). Let L be the splitting ﬁeld of f (T ) = ∏n
i=1(T − yi).
Let D(T ) = r1(T )
r2(T ) ∈ F (T )× be a reduced rational function with deg r2 ≥ deg r1,

and r2(T ) = c ∏d
j=1(T − αj) (c ∈ F ×, αj ∈ F ). We have

(26)
 n∑

i=1 D(yi) = h(A)
∏d
j=1 f (αj)

where h ∈ F [A] is coprime to ∏d
j=1 f (αj) as a polynomial in A0.

Proof. We ﬁrst prove (26) in the special case D(T ) = 1/(T − α)k. Let

(27) g(T ) := f ( 1
T + α)T n

f (α) = f0( 1
T + α)T n + ∑m
i=0 Ai(1 + αT )iT n−i

f (α) .

CHEBOTAREV DENSITY THEOREM IN SHORT INTERVALS 21

We have

(28) g(T ) =
 n∏

i=1(T − 1
yi − α ).

By Newton’s identities, if pk := ∑n
i=1 1
(yi−α)k and ei := ∑

1≤a1<a2<...<ai≤n ∏i
j=1 1
yaj −α,
then

(29) pk = ∑

ν1+2ν2+...+kνk=k
ν1≥0,...,νk≥0
 (−1)k k(ν1 + . . . + νk − 1)!
ν1!ν2! . . . νk!
 k∏

i=1(−ei)νi,

and the coeﬃcients are in fact integers. By (27) and (28), ej has denominator
f (α) and numerator independent of A0, . . . , Aj−1. Thus all the summands in (29),
except e
k
1, are of the form s(A)
f (α)j for some j < k and s ∈ F [A1, . . . , Am]. Moreover, e
k
1
has denominator f (α)k and non-zero numerator (it is (−(f ′
0(α) + ∑m
i=1 iAiαi−1))k,
which depends on A1). From (29) we establish (26) with D = 1
(T −α)k .
To prove (26) for general D, we write r2 as c ∏e
i=1(T − βi)ki, where βi ∈ F are
distinct. The partial fraction decomposition of D is given by

(30) D(T ) = c0 +
 e∑

i=1
 ki∑

j=1
 ci,j
(T − βi)j , (c0, ci,j ∈ F, ci,ki ̸= 0).

Applying (26) to each summand in (30) and summing, we obtain (26) in its gen-
erality. □

Lemma 6.14. Let F be a ﬁeld of characteristic p, K = F (A0) a ﬁeld of rational
functions and ℘(x) = x
p − x. Suppose that

(31) a
b ≡ c
d mod ℘(K)

where both fractions are in reduced form, and that b, d coprime. Then b, d are p-th
powers.

Proof. From (31), ad−cb
bd = zp − z for z ∈ K. Writing z = z1
z2 in reduced form,
it follows that the denominator of zp − z is a perfect p-th power, and so bd is a
perfect p-th power, and the conclusion follows since b, d are coprime. □

6.2.5. Proof of Lemma 6.4. Let ¯F be an algebraic closure of F . Since

Gal(M ¯F /K ¯F ) ≤ Gal(M/K) ≤ G ≀ Sn,

it suﬃces to prove that Gal(M ¯F /K ¯F ) ∼= G ≀ Sn. Therefore we may assume w.l.o.g.
that F = ¯F . In particular, if p | |G| and p ̸= char(F ), the ﬁeld F contains a
primitive p-th root of unity.
As explained before Lemma 6.4 it suﬃces to prove that Gal(M/L) = Gn. To do
this we apply Lemma 6.10 to M/L with the group Gn instead of G.

22 LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

For a prime p | |G| with p ∤ char(F ), let D1(T ), . . . , Dr(T ) ∈ F [T ] be p-powerfree
polynomials that are p-independent such that

EΦp(G) = L( p√D1(T ), . . . , p√Dr(T )).

If p | char(F ), |G|, let D1(T ), . . . , Dr(T ) ∈ F (T ) be rational functions that are
p-independent such that

(32) EΦp(G) = L(β1, . . . , βr), βp
i − βi = Di(T ).

So the αi,p-s of Lemma 6.10 can be taken to be Di(yj) with i = 1, . . . , r and
j = 1, . . . , n. Then, it suﬃces to prove that the Di(yj) are p-independent to ﬁnish
the proof. We separate this part into two cases depending on whether char(F ) = p
or not.

Case A: char(F ) ̸= p

Step 1: r = 1.
Put D = D1 and wj = D(yj). Let V be the space of linear dependencies of the
wj-s:

(33) V = {(v1, . . . , vn) ∈ Fn
p : wv1
1 · · · wvn
n ≡ 1 mod (L
×)p}.

We need to prove that V = 0. Since V is an invariant subspace of Fn
p under the
action of Sn = Gal(L/K), by Lemma 6.8 it suﬃces to prove that V ̸= V1, Vn−1, Vn.

Sub-step 1a: (1, . . . , 1) ̸∈ V ; hence V ̸= V1, Vn.
We assume in contradiction that (1, . . . , 1) ∈ V . In other words, there exists
z ∈ L such that

(34) D(y1) · · · D(yn) = zp.

We factor D over F (recall that we reduced to the case F = ¯F ):

(35) D(T ) = c
 d∏

j=1(T − αj), αj ∈ F, c ∈ F ×.

Since
 (−1)nf (αj) =
 n∏

i=1(yi − αj),

and using (34) and (35) we obtain

(36) zp = D(y1) · · · D(yn) = cn d∏

j=1
 n∏

i=1(yi − αj) = (−1)ndcn d∏

j=1 f (αj).

In particular, K(z)/K is a Galois subextension of the Sn-extension L/K of degree
p or 1. Put H = Gal(L/K(z)) so that by Lemma 6.7, either H = 1, H = Sn or
H = An, where the latter is possible only if p = 2.
If H = 1, then K(z) = L, so n! = 1 or n! = p, which contradicts n > 2. Thus,
H ̸= 1.
 CHEBOTAREV DENSITY THEOREM IN SHORT INTERVALS 23

Now we show that H ̸= Sn. If H = Sn, then [K(z) : K] = 1. Therefore z ∈ K,
as such z is a rational function in the Ai-s. From (36), it follows that ∏d
j=1 f (αj)
is a p-th power in K. Each f (αj), as a polynomial in A0, is linear with leading
coeﬃcient 1, so it must appear a multiple of p times. On the other hand, by
comparing the coeﬃcient of A1, the equality f (αj) = f (αk) implies that αj = αk.
As D is p-th powerfree in F [T ] by assumption, we arrive to contradiction.
So H = An and p = 2 and in particular the characteristic is ̸= 2. There
is a unique ﬁeld K ′ such that K ⊆ K ′ ⊆ L with Gal(L/K ′) = An, namely
K ′ = K(√disc(f )). Thus, K(z) = K(√disc(f )), and so by (36)

(37) (−1)ndcn d∏

j=1 f (αj) · disc(f ) ∈ (K ×)2.

The linear-in-A0 polynomial f (αj) is coprime to disc(f ). Indeed, put A = f (αj)
and apply Lemma 6.12 to ˜f (T ) = f (T ) − A, to obtain that ˜f (T ) is separable in
T and thus by Lemma 6.11, disc(f ) is not divisible by A = f (α1), hence coprime
to it, as needed. But then disc(f ) is a square by (37), which contradicts the fact
that Gal(L/K) = Sn.

Sub-step 1b: (1, −1, 0, . . . , 0) /∈ V ; hence V ̸= Vn−1 and V ̸= Vn.
Assume in contradiction that (1, −1, 0, ..., 0) ∈ V . So, there exists z ∈ L such
that

(38) D(y1) = D(y2)zp.

Consider the following diagram of ﬁelds

L
 Sn−2

✲ ✭ ✩✤

✚
✖
✑
Sn
 ✓
✕
✖
✘
✚
✜
✢
✤✦✧✩ ✫ ✭ ✮ ✰

K(y1, y2)(z)

1 or p

K(y1, y2)

n−1

K(y1)

K

with Gal(L/K(y1, y2)) = Sn−2 and K(y1, y2)(z)/K(y1, y2) Galois of degree 1 or p.
Assume in contradiction that [K(y1, y2)(z) : K(y1, y2)] = 1, then z ∈ K(y1, y2).
Applying the norm map

(39) N : K(y1, y2) → K(y1)

24 LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

on (38), multiplying by D(y1), and considering (36), we obtain

(40) D(y1)n = D(y1)D(y2) · · · D(yn)N(z)p = (−1)dncn d∏

j=1 f (αj)N(z)p.

The ﬁeld K(y1) is the ﬁeld of rational functions in A0, A2, . . . , Am, y1 over F since
A1 = − A0+A2y2
1+···
y1 .
This implies that f (αj) and f (αk), as elements in F (A2, · · · , Am, y1)[A0] are
associate if and only if αj = αk. Since D is p-th powerfree, for every j the
multiplicity of f (αj) in the right hand side product in (40) is ̸≡ 0 mod p. On the
other hand, on the left hand side of (40) the multiplicity of f (αj) is 0 since A0
does not appear. This contradicts (40), therefore [K(y1, y2)(z) : K(y1, y1)] = p.
By Lemma 6.7, p = 2 and thus the characteristic is ̸= 2. As L/K(y1, y2) is an
Sn−2-extension, it has a unique subextension of degree 2 which is the ﬁxed ﬁeld
of An−2 = An ∩ Sn−2 hence is generated by √disc(f ). But z also generates a
quadratic subextension, hence

(41) D(y1)
D(y2) disc(f ) = z2disc(f ) ∈ (K(y1, y2)×)2.

Apply the norm map (39) to obtain

(42) D(y1)n

D(y1) · · · D(yn) · discn−1(f ) ∈ (K(y1)×)2.

If n is even, then (1, . . . , 1) ∈ Vn−1 (as p = 2). Therefore, by Sub-step 1a, V ̸=
V1, Vn−1, Vn, that is, V = 0, in contradiction to the assumption that (1, −1, 0, . . . , 0) ∈
V . Thus, n is odd. By (42) and (36)

(43) D(y1) ≡
 d∏

j=1 f (αj) mod (F (y1, A0, A2, · · · , Am)×)2.

As D is not a square and each of the f (αj) is linear in A0, and by the fact that
f (αj) and f (αk) are associate only if αj = αk, we must have that A0 appears in
the left hand side, which is a contradiction.

Step 2: General r.
Put wi,j = Di(yj) and as before let V be the space of linear dependencies:

(44) V = {(vi,j)1≤i≤r,1≤j≤n ∈ Fnr
p :
 r∏

i=1
 n∏

j=1 Dvi,j
i (yj) ∈ (L
×)p}

and we want to prove that V = 0.
Here the action of Sn = Gal(L/K) on the wi,j is by permuting the j-th index,
so V is an Sn-invariant space with respect of the action of Sn given by permuting
the columns.

CHEBOTAREV DENSITY THEOREM IN SHORT INTERVALS 25

Assume in contradiction that V ̸= 0. We begin by constructing a matrix B in
V of rank 1. Let A ∈ V be a non-zero matrix. Denote its columns by v1, · · · , vn.
If rk(A) = 1 we take B = A. Otherwise, assume without loss of generality that v1
and v2 are linearly independent. Then the matrix

B = A − (v2 | v1 | v3 | v4 | · · · ) = (v1 − v2 | v2 − v1 | 0 | · · · ) ∈ V.

has rank 1, as needed.
There are non-zero vectors a = (a1, . . . , ar) ∈ Fr
p, b = (b1, . . . , bn) ∈ Fn
p such
that
 Bi,j = ai · bj.

The relation B ∈ V is equivalent to

(45)
 r∏

i=1
 n∏

j=1 Dai·bj
i (yj) ∈ (L
×)p.

Let D(T ) := ∏r
i=1 Dai
i (T ). We have ∏n
j=1 Dbj (yj) ∈ (L
×)p, which by Step 1 implies
that bj = 0 for all j, contradicting the fact that b ̸= 0. This concludes the proof
of Case A.

Case B: char(F ) = p
From now on, ℘(x) = x
p−x. Let v be the discrete valuation at the inﬁnite prime;
that is to say, v(h(T )/g(T )) = deg h − deg g. Since E/Fq(T ) is tamely ramiﬁed at
v, the extension generated by a root of X p − X = Di(T ) is unramiﬁed at v. This
implies that there exists some gi(T ) with v(Di + gp
i − gi) ≥ 0. We may replace
Di by Di + gp
i − g, to assume without loss of generality that v(Di(T )) ≥ 0. We
may further assume that the roots in the denominators of Di(T ) have multiplicity
indivisible by p [23, §2]. The proof goes analogously to Case A:

Step 1: r = 1.
Put D = D1 and wj = D(yj). Let V be the space of linear dependencies of the
wj-s:

(46) V = {(v1, . . . , vn) ∈ Fn
p :
 n∑

i=1 wivi ≡ 0 mod ℘(L)}

We need to prove that V = 0. Since V is an invariant subspace of Fn
p under the
action of Sn = Gal(L/K), by Lemma 6.8 it suﬃces to prove that V ̸= V1, Vn−1, Vn.

Sub-step 1a: (1, . . . , 1) ̸∈ V ; hence V ̸= V1, Vn.
We assume in contradiction that (1, . . . , 1) ∈ V . In other words, there exists
z ∈ L such that

(47) D(y1) + . . . + D(yn) = zp − z.

26 LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

Write D = r1(T )
r2(T ) where r1, r2 are coprime, and r2(T ) = c ∏d
j=1(T − αj) (c ∈
F ×, αj ∈ F ). By Lemma 6.13,

(48) zp − z =
 n∑

i=1 D(yi) = h(A)
∏d
j=1 f (αj),

where h(A) ∈ F [A] is coprime to the denominator as polynomials in A0. In
particular, K(z)/K is a Galois subextension of the Sn-extension L/K of degree
p or 1. Put H = Gal(L/K(z)) so that by Lemma 6.7, either H = 1, H = Sn or
H = An, where the latter is possible only if p = 2.
If H = 1, then K(z) = L, so n! = 1 or n! = p, which contradicts n > 2. Thus,
H ̸= 1.
Now we show that H ̸= Sn. If H = Sn, then [K(z) : K] = 1. Therefore z ∈ K.
The denominator of zp − z is a (possibly trivial) p-th power in K, so that by (48)
it follows ∏d
j=1 f (αj) is a p-th power in K. Each f (αj), as a polynomial in A0, is
linear with leading coeﬃcient 1, so it must appear a multiple of p times. On the
other hand, by comparing the coeﬃcient of A1, the equality f (αj) = f (αk) implies
that αj = αk. As αi have multiplicity indivisible by p by our assumption on r2(T ),
we arrive to contradiction.
So H = An and p = 2. In characteristic 2, we must use the Berlekamp dis-
criminant Berl(f )1 in place of the usual disc(f ). There is a unique ﬁeld K ′ such
that K ⊆ K ′ ⊆ L with Gal(L/K ′) = An, namely K ′ = K(δ) for δ which satisﬁes
δ2 − δ = Berl(f ). Thus, K(z) = K(δ), or equivalently

(49) ℘(z) ≡ ℘(δ) mod ℘(K),

which by (48) becomes

(50) Berl(f ) ≡ h(A)
∏d
j=1 f (αj) mod ℘(K).

As in Sub-step 1a in the Kummer case, the linear-in-A0 polynomial f (αj) is co-
prime to disc(f ). The Berlekamp discriminant is of the form N(f )/disc(f ) for
some polynomial N in the coeﬃcients of f . Thus, the denominators of the two
fractions in (50) are coprime as polynomials in A0. By Lemma 6.14, this implies
that the denominator ∏d
j=1 f (αj) is a square, contradicting the fact that the αj
have odd multiplicity by our assumption on r2(T ).

Sub-step 1b: (1, −1, 0, . . . , 0) /∈ V ; hence V ̸= Vn−1 and V ̸= Vn.
Assume in contradiction that (1, −1, 0, ..., 0) ∈ V . So, there exists z ∈ L such
that

(51) D(y1) = D(y2) + zp − z.

1See [6] or [8] for a recent use in a similar setting.

CHEBOTAREV DENSITY THEOREM IN SHORT INTERVALS 27

We have Gal(L/K(y1, y2)) = Sn−2 and K(y1, y2)(z)/K(y1, y2) Galois of degree 1 or
p. Assume in contradiction that [K(y1, y2)(z) : K(y1, y2)] = 1, then z ∈ K(y1, y2).
Applying the trace map

(52) T : K(y1, y2) → K(y1).

on (51), adding by D(y1), and considering (48), we obtain

(53) nD(y1) = h(A)
∏d
j=1 f (αj) + T (z)p − T (z) ≡ h(A)
∏d
j=1 f (αj) mod ℘(K(y1)).

The ﬁeld K(y1) is the ﬁeld of rational functions in A0, A2, . . . , Am, y1 over F since
A1 = − A0+A2y2
1+···
y1 .
This implies that f (αj) and f (αk), as elements in F (A2, · · · , Am, y1)[A0] are
associate if and only if αj = αk. The denominator in the left hand side of (53)
does not involve A0 and so it is coprime to the denominator in the right hand
side. By Lemma 6.14, this means that the denominator in the right hand side is
a p-th power, contradicting the fact that for every j, the multiplicity of f (αj) is
̸≡ 0 mod p. Therefore [K(y1, y2)(z) : K(y1, y1)] = p, and by Lemma 6.7, p = 2.
As L/K(y1, y2) is an Sn−2-extension, it has a unique subextension of degree 2
which is the ﬁxed ﬁeld of An−2 = An ∩ Sn−2 hence is generated by δ ∈ L which
satisﬁes δ2 − δ = Berl(f ). But z also generates a quadratic subextension, hence

(54) D(y1) − D(y2) + Berl(f ) = z2 − z + Berl(f ) ∈ ℘(K(y1, y2)).

Apply the trace map (52) to obtain

(55) nD(y1) − (D(y1) + . . . + D(yn)) + (n − 1)Berl(f ) ∈ ℘(K(y1)).

If n is even, then (1, . . . , 1) ∈ Vn−1 (as p = 2). Therefore, by Sub-step 1a, V ̸=
V1, Vn−1, Vn, that is, V = 0, in contradiction to the assumption that (1, −1, 0, . . . , 0) ∈
V . Thus, n is odd. By (55) and (48)

(56) r1(y1)
r2(y1) ≡ h(A)
∏d
j=1 f (αj) mod ℘(F (y1, A0, A2, · · · , Am)).

The denominator in the left hand side does not involve A0 and so it is coprime to
the denominator in the right hand side as a polynomial in A0. By Lemma 6.14, this
means that the denominator in the right hand side is a square. This contradicts
the fact that for every j, the multiplicity of f (αj) is odd, and that f (αj) and f (αk)
are associate if and only if αj = αk.

Step 2: General r.
Put wi,j = Di(yj) and let V be the space of linear dependencies:

(57) V = {(vi,j)1≤i≤r,1≤j≤n ∈ Fnr
p :
 r∑

i=1
 n∑

j=1 vi,jDi(yj) ∈ ℘(L)}

28 LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

and we want to prove that V = 0. Assume in contradiction that V ̸= 0. As in
Step 2 of the Kummer case, there exists B in V of rank 1. There are non-zero
vectors a = (a1, . . . , ar) ∈ Fr
p, b = (b1, . . . , bn) ∈ Fn
p such that

Bi,j = ai · bj.

The relation B ∈ V is equivalent to

(58)
 r∑

i=1
 n∑

j=1 aibjDi(yj) ∈ ℘(L).

Let D(T ) := ∑r
i=1 aiDi(T ). We have ∑n
j=1 bjD(yj) ∈ ℘(L), which by Step 1
implies that bj = 0 for all j, contradicting the fact that b ̸= 0. This concludes the
proof of Case B. □

7. Proof of Theorem 4.3

First we prove the assertion for ψ = δλ, where λ is a G-factorization type
supported on e = 1 with deg λ = n and δλ ∈ Λ∗ is given by

δλ(λ′) =
 {
1, if λ′ = λ,
0, otherwise.

Let C = {h ∈ G ≀ Sn : λh = λ} ⊆ G ≀ Sn. Since λ is supported on e = 1 and
deg λ = n, by Lemma 4.2, C is a conjugacy class.
Write f0 = T n+∑n−1
i=0 aiT i and put W = Wa,m as in (24). Every (w0, . . . , wn−1) ∈
W (Fq) corresponds in a bijective way to f = T n+∑n−1
i=0 wiT i with deg(f −f0) ≤ m.
By the explicit Chebotarev theorem
2 and by Proposition 6.2,

#{w ∈ W (Fq) : w is unramiﬁed in U and φw ∈ C}
qm+1 = |C|
|G ≀ Sn| + O(q−1/2),

where the implied constant is bounded in terms of the complexity of U, which is
bounded in terms of |G|, genus(C), and n and hence in terms of B. This ﬁnishes
the proof of this case since |C|
|G≀Sn| = 〈
δλ(λ(ξ,σ))〉

(ξ,σ)∈C, for unramiﬁed w we have
δλ(f ) = δλ(φw) by Lemma 6.1, there are OB(qm) ramiﬁed w (the zeros of D given
in (21)), and so

⟨δλ(f )⟩deg(f −f0)≤m = #{w ∈ W (Fq) : w is unramiﬁed in U and φw ∈ C}
qm+1 +OB(q−1).

2For a version which is suﬃciently uniform in the parameters see either [1, Appendix] or [12,
Thm. 3]. In the former there is a mistake in the formulation of the theorem, in the notation of
loc. cit. the error term should be dependent on the complexity of S and not on the complexity
of R and deg F as written. In the setting where R is a polynomial ring in several variables and
S is the ring generated by adding roots of a polynomial F ∈ R[X], then the complexity of S is
bounded in terms of the complexity of R and the total degree of F .

CHEBOTAREV DENSITY THEOREM IN SHORT INTERVALS 29

For general ψ, we partition Λ = Λ1 ∪ Λ2 ∪ Λ3, where Λ1 consists of λ-s of degree
n supported on e = 1, Λ2 consists of the other λ-s of degree n, and Λ3 consists of
λ-s of degree ̸= n. This decomposes ψ = ψ1 + ψ2 + ψ3 with ψi supported on Λi.
Now, as deg(f − f0) ≤ m implies that deg f = n, we have

⟨ψ3(f )⟩deg(f −f0)≤m = 0.

Since ψ2(f ) = 0 if f is squarefree and there are OB(qm) non-squarefrees satisfying
deg(f − f0) ≤ m [17, Thm. 1.3], we get that

⟨ψ2(f )⟩deg(f −f0)≤m = OB(q−1).

The function ψ1 decomposes as ψ1 = ∑

λ∈Λ1 ψ1(λ)δλ1, so by the special case proved
above
 ⟨ψ1(f )⟩deg(f −f0)≤m = ∑

λ∈Λ1 ψ1(λ) ⟨δλ(f )⟩deg(f −f0)≤m

= ∑

λ∈Λ1 ψ1(λ) ⟨δλ(ξ, σ)⟩(ξ,σ)∈G≀Sn + OB(q−1/2)

= ⟨ψ1(ξ, σ)⟩(ξ,σ)∈G≀Sn + OB(q−1/2).

This completes the proof as ψ1(ξ, σ) = ψ(ξ, σ). □

8. Non-geometric extensions

Here we explain how the results for non-geometric extensions may be reduced to
geometric extensions over a ﬁeld extension: Let G be a ﬁnite group, let E/Fq(T )
be a G-extension and let Eab be the ﬁxed ﬁeld of the commutator of G in E.
Assume that Eab is tamely ramiﬁed at inﬁnity and that E (or equivalently Eab) is
not geometric. Let Fqν be the algebraic closure of Fq in E, Cν = Gal(Fqν /Fq), and
H = Gal(E/Fqν (T )). By replacing E with EFqµ for some large µ, we may assume
without loss of generality that G = H ⋊ Cν. Now we apply the construction
of §6 to the extension E/Fqν (T ) to get that the corresponding Galois group is
Gal(M/K) = H ≀ Sn and we have a diagram of ﬁelds whose right column is as in
Figure 6.2 M

L0 = K0(y1, . . . , yn) L = K(y1, . . . , yn)

K0 = Fq(A0, . . . , Am) K = Fqν (A0, . . . , Am)

Now, Gal(L0/K0) = Sn for the same reason that Gal(L/K) = Sn, and Gal(K/K0) ∼=
Gal(Fqν /Fq) = Cν. Thus, Gal(L/K0) = Sn × Cν. With a little more eﬀort, one can
verify that in fact M/K0 is Galois, and that Gal(M/K0) = (H ≀ Sn) ⋊ Cν with Cν

30 LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

acting trivially on Sn and acting diagonally on H n. Now we can apply the higher
dimensional Chebotarev theorem, to get a Chebotarev theorem in short intervals
for this extension.
 Appendix A. Norms in full intervals

We use the notation of §5. The goal of this appendix is to compute the mean
value of bE/Fq(T ) and of rE/Fq(T ) in the most general setting of the limit qn → ∞.

Theorem A.1. Let E/Fq(T ) be a non-trivial geometric G-extension. Then

(59) 〈
bE/Fq(T )(f )〉

f ∈Mn,q = KE
(
n + 1
|G| − 1
n
 )
(1 + Ogenus(E),|G|( 1
√qn)),

where KE is a positive constant that satisﬁes

(60) KE = 1 + Ogenus(E),|G|( 1
√q ).

The mean value of rE/Fq(T ) depends on the following zeta function

ζOE (s) = ∑

0̸=I ideal in OE
 1
(#OE/I)s .

Proposition A.2. Let E/Fq(T ) be a non-trivial geometric extension of degree d.
If n ≫genus(E),d 1 then

(61) 〈
rE/Fq(T )(f )〉

f ∈Mn,q = λE log q,

where λE > 0 is the residue of ζOE (s) at s = 1, and it satisﬁes

(62) λE log q = 1 + Ogenus(E),d( 1
√q ).

Unlike the rest of the paper, here the methods are analytic.

A.1. Bounds on prime counting functions. We use the notation Pn,q intro-
duced in §1.2, with one modiﬁcation – we do not include the inﬁnite prime in P1,q.
For any positive integer f , deﬁne

πE;f (n) = ∑

P ∈Pn,q,
f (P ;E)=f
 1

and set ψE(n) = ∑

df |n df πE;f (d).

Lemma A.3. We have

|πE;1(n) − qn

n|G|| ≪ max{genus(E), |G|}
n qn/2.

CHEBOTAREV DENSITY THEOREM IN SHORT INTERVALS 31

Proof. Let e be the identity element of G. The number πC;q(n; E) with C = {e}
is equal to πE;1(n), up to a contribution of ramiﬁed primes:

(63) |π{e};q(n; E) − πE;1(n)| ≤ ∑

P ∈Pn,q, ramiﬁed in E 1.

The Riemann-Hurwitz formula [32, Thm. 7.16] shows that

(64) ∑

P ∈Pn,q, ramiﬁed in E 1 ≪ max{genus(E), |G|}
n .

By (5) with C = {e}, we have

(65) |π{e};q(n; E) − qn

n|G| | ≪ max{genus(E), |G|}
|G| qn/2

n .

From (63)–(65) and the triangle inequality, the proof follows. □

Proposition A.4. We have
∣
∣
∣
∣ψE(n) − qn

|G|
 ∣
∣
∣
∣ ≪ max{genus(E), |G|}q n
2 .

Proof. We separate the summands in ψE(n) according to whether d = n (a case
which contributes nπE;1(n)) or not:

ψE(n) = nπE;1(n) + T (n).

The triangle inequality gives us

(66) ∣
∣
∣
∣ψE(n) − qn

|G|
 ∣
∣
∣
∣ ≤ ∣
∣
∣
∣nπE;1(n) − qn

|G|
∣
∣
∣
∣ + T (n).

We may bound T (n) from above as follows, using the fact that |Pn,q| ≤ qn

n :

T (n) ≤
 ⌊ n
2 ⌋∑

d=1
 ⌊ n
d ⌋∑

f =1 df πE;f (d) ≤ n
 ⌊ n
2 ⌋∑

d=1
 ⌊ n
d ⌋∑

f =1 πE;f (d) ≤ n
 ⌊ n
2 ⌋∑

d=1
 qd

d .

One can show by induction that
 m∑

i=1
 qi

i ≤ 4 qm

m

for all m ≥ 1, which implies that

(67) T (n) ≪ qn/2.

From (66), (67) and Lemma A.3, we conclude the proof of the proposition. □

32 LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

A.2. Proof of Theorem A.1. Consider the power series

(68) DE(u) = ∑

f ∈Fq[T ], monic bE/Fq(T )(f )udeg f = ∑

n≥0⟨bE/Fq(T )(f )⟩f ∈Mn,q (qu)n.

Lemma 5.2 shows that DE admits the following Euler product:

DE(u) = ∏

P ∈Pq
 (
1 + udeg(P f (P ;E)) + udeg(P 2·f (P ;E)) + . . .
)

= ∏

P ∈Pq
 (
1 − uf (P ;E) deg P )−1 = exp
 

 ∑

P ∈Pq
 ∑

k≥1
 uf (P ;E) deg P ·k

k
 

 .

From the deﬁnition of πE;f (n) and ψE(n), we may write the above expression as

(69) DE(u) = exp
 

∑

n≥1
 un

n
 ∑

df |n df πE;f (d)


 = exp
 (∑

n≥1
 un

n ψE(n)
)
 .

For any positive integer n, deﬁne

en = ψE(n) − qn

|G|.

Let
 a(u) = exp
 (∑

n≥1
 enun

n
 )
 , b(u) = (1 − qu)− 1
|G| .

By (69), we have DE(u) = exp (∑

n≥1 qnun

n|G| ) exp (∑

n≥1 enun
n ) = a(u)b(u), and so

⟨bE/Fq(T )(f )⟩f ∈Mn,q = q−n[un]DE(u) = q−n[un]a(u)b(u),

where [un]F (u) is a notation for the coeﬃcient of un in a power series F . From
Proposition A.4 we have
 |en| ≪ max{genus(E), |G|}qn/2.

Hence we may apply [14, Thm. 3.3] with a(u), b(u) and obtain

⟨bE/Fq(T )(f )⟩f ∈Mn,q = (n + 1
|G| − 1
n
 ) (
a(q−1) + E) ,

where
 |E| ≪genus(E),|G| 1
√qn.

which establishes (59) with KE = a(q−1). By [14, Rem. 3.6] we have (60). □

CHEBOTAREV DENSITY THEOREM IN SHORT INTERVALS 33

A.3. Proof of Proposition A.2. Let

ZE(u) = ∏

P a prime in E(1 − udeg P)−1,

ZOE (u) = ∏

P a prime in OE(1 − udeg P)−1,

be the Dedekind zeta function of E and of OE; in particular, ZOE (q−s) = ζOE (s).
They are related by

(70) ZOE (u) = ZE(u) ∏

P|P∞(1 − udeg P),

where P∞ denotes the inﬁnite prime of Fq(T ). Suppose that P∞ = P e1
1 · · · P em
m
with Pi distinct primes of E and put fi = f (Pi; E). Then we have

(71) ∏

P|P∞(1 − udeg P) =
 m∏

i=1(1 − ufi).

As E/Fq(T ) is geometric, the Riemann Hypothesis for Function Fields (RH) im-
plies that ZE is a rational function of the form

(72) ZE(u) = PE(u)
(1 − qu)(1 − u),

where deg PE = 2genus(E), PE(0) = 1 and the inverse absolute value of the roots
of PE is √q. From (70)–(72),

(73) ZOE (u) = PE(u)
(1 − qu) · ∏m
i=1(1 − ufi)
1 − u = ˜PE(u)
(1 − qu),

with ˜PE(u) = PE(u) ·
 ∏m
i=1(1−ufi )
1−u . The function ZOE (u) is a generating function for
the mean value of rE/Fq(T ):

(74) ZOE (u) = ∑

n≥0⟨rE/Fq(T )(f )⟩f ∈Mn,q(qu)n.

From (73), (74), it follows that if n ≥ deg ˜PE, we have

⟨rE/Fq(T )(f )⟩f ∈Mn,q = ˜PE( 1
q ).

As ZOE (q−s) = ζOE (s), we have ˜PE( 1
q ) = λE log q. As fi, m ≤ d, we have deg ˜PE =
2genus(E) + ∑m
i=1 fi − 1 ≪genus(E),d 1. Finally, RH implies that

λE log q = (1 + O( 1
√
q ))2genus(E)(1 + O( 1
q ))O(d2) = 1 + Ogenus(E),d( 1
√q ),

as needed. □

34 LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

Acknowledgment

We wish to thank to Kumar Murty for helpful discussion on Chebotarev theo-
rem.
 References

1. J. C. Andrade, L. Bary-Soroker, and Z. Rudnick, Shifted convolution and the Titchmarsh
divisor problem over Fq[t], Philos. Trans. Roy. Soc. A 373 (2015), no. 2040, 20140308, 18.
MR 3338116 2
2. Antal Balog and Ken Ono, The Chebotarev density theorem in short intervals and some
questions of Serre, J. Number Theory 91 (2001), no. 2, 356–371. MR 1876282 1.1
3. Efrat Bank, Lior Bary-Soroker, and Arno Fehm, Sums of two squares in short intervals in
polynomial rings over ﬁnite ﬁelds, Amer. J. Math. 140 (2018), no. 4, 1113–1131. MR 3828042
2, 6.3, 6.2.4
4. Efrat Bank, Lior Bary-Soroker, and Lior Rosenzweig, Prime polynomials in short intervals
and in arithmetic progressions, Duke Math. J. 164 (2015), no. 2, 277–295. MR 3306556 2,
6.2.1
5. Lior Bary-Soroker and Arno Fehm, Correlations of sums of two squares and other arithmetic
functions in function ﬁelds, International Mathematics Research Notices (2017), rnx250. 3
6. E. R. Berlekamp, An analog to the discriminant over ﬁelds of characteristic two, J. Algebra
38 (1976), no. 2, 315–317. MR 0404197 1
7. Jean Bourgain and Nigel Watt, Mean square of zeta function, circle problem and divisor
problem revisited, arXiv preprint arXiv:1709.04340 (2017). 5.2
8. Dan Carmon, The autocorrelation of the M¨obius function and Chowla’s conjecture for the
rational function ﬁeld in characteristic 2, Philos. Trans. Roy. Soc. A 373 (2015), no. 2040,
20140311, 14. MR 3338117 1
9. S. D. Cohen, The Galois group of a polynomial with two indeterminate coeﬃcients, Paciﬁc
J. Math. 90 (1980), no. 1, 63–76. MR 599320 2, 6.3
10. S. D. Cohen and R. W. K. Odoni, The Farey density of norm subgroups of global ﬁelds. II,
Glasgow Math. J. 18 (1977), no. 1, 57–67. MR 0432597 1.2
11. Mark D. Coleman, The Hooley-Huxley contour method for problems in number ﬁelds. III.
Frobenian functions, J. Th´eor. Nombres Bordeaux 13 (2001), no. 1, 65–76, 21st Journ´ees
Arithm´etiques (Rome, 2001). MR 1838070 2
12. Alexei Entin, Monodromy of hyperplane sections of curves and decomposition statistics over
ﬁnite ﬁelds, arXiv preprint arXiv:1805.05454 (2018). 2
13. Michael D. Fried and Moshe Jarden, Field arithmetic, second ed., Ergebnisse der Mathematik
und ihrer Grenzgebiete. 3. Folge. A Series of Modern Surveys in Mathematics [Results in
Mathematics and Related Areas. 3rd Series. A Series of Modern Surveys in Mathematics],
vol. 11, Springer-Verlag, Berlin, 2005. MR 2102046 1.2, 6.1
14. Oﬁr Gorodetsky, A polynomial analogue of Landau’s theorem and related problems, Mathe-
matika 63 (2017), no. 2, 622–665. MR 3706601 A.2
15. Lo¨ıc Greni´e and Giuseppe Molteni, An explicit Chebotarev density theorem under GRH., J.
Number Theory 200 (2019), 441–485 (English). 1.1
16. Franz Halter-Koch, Der ˇCebotarev’sche Dichtigkeitssatz und ein Analogon zum Dirich-
let’schen Primzahlsatz f¨ur Algebraische Funktionenk¨orper, Manuscripta Math. 72 (1991),
no. 2, 205–211. MR 1114006 1.2

CHEBOTAREV DENSITY THEOREM IN SHORT INTERVALS 35

17. Jonathan Keating and Zeev Rudnick, Squarefree polynomials and M¨obius values in short
intervals and arithmetic progressions, Algebra Number Theory 10 (2016), no. 2, 375–420.
MR 3477745 7
18. Jonathan P. Keating and Ze´ev Rudnick, The variance of the number of prime polynomials
in short intervals and in residue classes, Int. Math. Res. Not. IMRN (2014), no. 1, 259–288.
MR 3158533 1.2
19. Vijaya Kumar Murty and John Scherk, Eﬀective versions of the Chebotarev density theo-
rem for function ﬁelds, C. R. Acad. Sci. Paris S´er. I Math. 319 (1994), no. 6, 523–528.
MR 1298275 1.2
20. J. C. Lagarias and A. M. Odlyzko, Eﬀective versions of the Chebotarev density theorem,
Algebraic number ﬁelds: L-functions and Galois properties (Proc. Sympos., Univ. Durham,
Durham, 1975), Academic Press, London, 1977, pp. 409–464. MR 0447191 1.1
21. Serge Lang, Sur les s´eries L d’une vari´et´e alg´ebrique, Bull. Soc. Math. France 84 (1956),
385–407. MR 0088777 1.2
22. Huixue Lao, On the distribution of integral ideals and Hecke Gr¨ossencharacters, Chin. Ann.
Math. Ser. B 31 (2010), no. 3, 385–392. MR 2652933 5.2
23. Daniel J. Madden, Arithmetic in generalized Artin-Schreier extensions of k(x), J. Number
Theory 10 (1978), no. 3, 303–323. MR 506641 6.2.5
24. Helmut Maier, Primes in short intervals, Michigan Math. J. 32 (1985), no. 2, 221–225.
MR 783576 1.1
25. M. Ram Murty, V. Kumar Murty, and N. Saradha, Modular forms and the Chebotarev density
theorem, Amer. J. Math. 110 (1988), no. 2, 253–281. MR 935007 1.1
26. R. W. K. Odoni, On the norms of algebraic integers, Mathematika 22 (1975), no. 1, 71–80.
MR 0424757 5.2
27. , Solution of some problems of Serre on modular forms: The method of Frobenian
functions., Recent progress in analytic number theory, Symp. Durham 1979, Vol. 2, London
; New York : Academic Press, 1981, pp. 159–169. 2
28. , Notes on the method of Frobenian functions with applications to Fourier coeﬃcients
of modular forms, Elementary and analytic theory of numbers (Warsaw, 1982), Banach
Center Publ., vol. 17, PWN, Warsaw, 1985, pp. 371–403. MR 840484 2
29. K. Ramachandra, Some problems of analytic number theory, Acta Arith. 31 (1976), no. 4,
313–324. MR 0424723 5.2
30. Hans Reichardt, Der Primdivisorsatz f¨ur algebraische Funktionenk¨orper ¨uber einem
endlichen Konstantenk¨orper, Math. Z. 40 (1936), no. 1, 713–719. MR 1545595 1.2
31. Brad Rodgers, Arithmetic functions in short intervals and the symmetric group, Algebra
Number Theory 12 (2018), no. 5, 1243–1279. MR 3840876 3
32. Michael Rosen, Number theory in function ﬁelds, Graduate Texts in Mathematics, vol. 210,
Springer-Verlag, New York, 2002. MR 1876657 1.2, A.1
33. Jean-Pierre Serre, Divisibilit´e de certaines fonctions arithm´etiques, (1975), 28. MR 0392831
2
34. , Quelques applications du th´eor`eme de densit´e de Chebotarev, Inst. Hautes ´Etudes
Sci. Publ. Math. (1981), no. 54, 323–401. MR 644559 1.1
35. , Abelian l-adic representations and elliptic curves, Research Notes in Mathematics,
vol. 7, A K Peters, Ltd., Wellesley, MA, 1998, With the collaboration of Willem Kuyk and
John Labute, Revised reprint of the 1968 original. MR 1484415 1.1
36. K. Soundararajan, The distribution of prime numbers, Equidistribution in number theory,
an introduction, NATO Sci. Ser. II Math. Phys. Chem., vol. 237, Springer, Dordrecht, 2007,
pp. 59–83. MR 2290494 1.1

36 LIOR BARY-SOROKER, OFIR GORODETSKY, TAELIN KARIDI, AND WILL SAWIN

37. Richard P. Stanley, Enumerative combinatorics. Vol. 2, Cambridge Studies in Advanced
Mathematics, vol. 62, Cambridge University Press, Cambridge, 1999, With a foreword by
Gian-Carlo Rota and appendix 1 by Sergey Fomin. MR 1676282 5.2
38. Jesse Thorner, A variant of the Bombieri-Vinogradov theorem in short intervals and
some questions of Serre, Math. Proc. Cambridge Philos. Soc. 161 (2016), no. 1, 53–63.
MR 3505669 1.1
39. H. Weber, Lehrbuch der Algebra. In zwei B¨anden. 2. Band., Braunschweig : Friedrich Vieweg
und Sohn, 1896. 5.2

Raymond and Beverly Sackler School of Mathematical Sciences, Tel Aviv Uni-
versity, Tel Aviv 69978, Israel
E-mail address: barylior@post.tau.ac.il

Raymond and Beverly Sackler School of Mathematical Sciences, Tel Aviv Uni-
versity, Tel Aviv 69978, Israel
E-mail address: ofir.goro@gmail.com

Department of Mathematics, Caltech, Pasadena, CA 91125, USA
E-mail address: tkaridi@caltech.edu

Department of Mathematics, Columbia University, New York, NY 10027, USA
E-mail address: sawin@math.columbia.edu
