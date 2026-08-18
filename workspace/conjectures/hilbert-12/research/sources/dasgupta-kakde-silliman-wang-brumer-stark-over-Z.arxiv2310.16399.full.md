<!-- source: https://arxiv.org/pdf/2310.16399 | converted from PDF -->

arXiv:2310.16399v1  [math.NT]  25 Oct 2023
The Brumer–Stark Conjecture over Z

Samit Dasgupta
Mahesh Kakde
Jesse Silliman
Jiuya Wang

October 26, 2023

Contents

1 Introduction 2
1.1 The Brumer–Stark Conjecture . . . . . . . . . . . . . . . . . . . . . . . . . . 3
1.2 Ritter–Weiss Modules . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4

2 Ritter–Weiss Modules and Brumer–Stark 6
2.1 Properties of Ritter–Weiss Modules . . . . . . . . . . . . . . . . . . . . . . . 6
2.2 Brumer–Stark . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
2.3 Minimal Sets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
2.4 Character Group Rings . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
2.5 Inclusion Implies Equality . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
2.6 Summary . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
2.7 Ribet’s Lemma . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

3 Modular Forms 21
3.1 Hecke Algebra . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
3.2 Cusp form and homomorphism . . . . . . . . . . . . . . . . . . . . . . . . . 24
3.3 Galois Representation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27

4 Construction of Generalized Ritter–Weiss Modules 30
4.1 Class modules and class formations . . . . . . . . . . . . . . . . . . . . . . . 30
4.2 Class ﬁeld theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 32
4.3 The Ritter–Weiss complex . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.3.1 Global complex . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.3.2 Local complexes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
4.4 Construction of the Ritter–Weiss complex . . . . . . . . . . . . . . . . . . . 36

1

4.5 Quadratic presentation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 40
4.6 ∇T
S (H) and Galois cohomology . . . . . . . . . . . . . . . . . . . . . . . . . 44
4.7 Fitting Ideals and Transposes . . . . . . . . . . . . . . . . . . . . . . . . . . 46

5 A Duality Theorem for Class Formations 48
5.1 Duality (G ﬁnite) . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
5.2 Functoriality . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 54
5.3 Duality theorem (G proﬁnite) . . . . . . . . . . . . . . . . . . . . . . . . . . 54

1 Introduction

Let F be a totally real ﬁeld and let H be a ﬁnite abelian CM extension of F . Let p denote
a prime ideal of F that splits completely in H. The Brumer–Stark conjecture states the
existence of a p-unit in H whose valuations at the primes above p are related to the values
L(χ, 0) as χ ranges over the characters of the extension H/F . See Theorem 1.1 below for a
precise statement. In previous work, the ﬁrst two named authors proved the Brumer–Stark
conjecture over Z[1/2], i.e. we proved the existence of an element in the p-unit group tensored
with Z[1/2] with the desired properties.
In this paper, we give a complete proof of the Brumer–Stark conjecture over Z. In fact
we obtain a strong reﬁnement of the Brumer–Stark conjecture that yields the Fitting ideal
of certain Ritter–Weiss modules. In a companion paper to this one, we show how to use this
result to deduce the minus part of the Equivariant Tamagawa Number Conjecture (ETNC)
for the Tate motive associated to H/F . Again, we obtain this integrally over Z and not
just over Z[1/2]. The proof of ETNC, which is obtained by applying an idea of Bullach–
Burns–Daoud–Seo to the results on Brumer–Stark proven here, yields many important new
corollaries. These include Rubin’s higher rank Brumer–Stark conjecture, the integral Gross–
Stark conjecture, and the higher rank version due to Popescu. One should also obtain the
classical Main Conjecture of Iwasawa Theory over totally real ﬁelds at the prime p = 2,
though there does not appear to be a precise statement of the classical Main Conjecture at
p = 2 in the literature (but see [5, Conjecture 3.1]). Our proof of ETNC is rather formal,
with the main arithmetic input being Theorem 1.2 from this paper.
There are two conceptual diﬃculties that occur when attempting to generalize our pre-
vious work on the Brumer–Stark conjecture to the prime p = 2. The ﬁrst of these is in the
application of Ribet’s method, which provides a strategy for constructing nontrivial exten-
sions of a p-adic Galois representation ρ1 by another such representation ρ2. Our previous
proof of Brumer–Stark over Zp for p odd is an application of a very general version of Ribet’s
method. However, an important assumption that occurs throughout the literature is that
the representations ρi are residually distinguishable, i.e. that

ρ1 ̸∼= ρ2 (mod p).

2

In the setting of Brumer–Stark, ρ1 is the trivial character and ρ2 is a totally odd character
χ. When p is odd, χ(c) = −1 ̸≡ 1 (mod p), where c denotes complex conjugation. Ribet’s
method therefore carries through. However when p = 2, we may have χ ≡ 1 (mod 2), and a
new construction is necessary. This issue was handled in our paper [12], whose main theorem
is a general version of Ribet’s Lemma that applies in the residually indistinguishable case.
The next issue at p = 2 concerns the Ritter–Weiss module ∇Σ′
Σ (H) appearing in our
previous work. It turns out that this module is not what appears in the Galois representations
that we study locally at 2. We must alter the module ∇Σ′
Σ (H) by modifying the local
conditions at the archimedean places. On the analytic side this modiﬁcation is reﬂected in
the power of 2 in the denominator of the constant terms of Eisenstein series for F .
These modiﬁcations have an important eﬀect on our constructions with group-ring valued
Hilbert modular forms. In the case that the extension H/F is not ramiﬁed at any primes
above 2, the set Σ that one would naturally like to take is empty; however it is an important
assumption in our study of Ritter–Weiss modules that Σ is non-empty. One is therefore
led to introduce an auxiliary prime l that does not divide the conductor of the extension
H/F into the set Σ. The inclusion of this prime leads to the presence of oldforms in our
constructions with Hilbert modular forms, which in turn yields a Hecke algebra T that is
not reduced. Working with a non-reduced Hecke algebra involves new ideas to show that
the Galois representations we construct have the desired properties. Therefore, the main
technical contribution of this paper is the introduction of our new generalized Ritter–Weiss
module ∇Σ′
Σ (H) in which the depletion set Σ need not contain the archimedean primes, as well
as a delicate handling of the constructions with modular forms and Galois representations
that ensue; the connection between our Ritter–Weiss modules and Galois cohomology is
handled in a more conceptual way than in [11], and requires new results on class formations.

We conclude the introduction by stating precisely our main arithmetic results. First
we recall the statement of the Brumer–Stark conjecture, and next we describe our stronger
results involving Ritter–Weiss modules.

1.1 The Brumer–Stark Conjecture

Recall that we have ﬁxed a totally real ﬁeld F of degree n and a ﬁnite abelian extension
H/F that is a CM ﬁeld. Write G = Gal(H/F ). Let S and T denote ﬁnite disjoint sets of
places of F . Associated to any character χ : G −→ C∗ one has the Artin L-function

LS(χ, s) = ∏

p̸∈S
p ﬁnite
 1
1 − χ(p)Np−s , Re(s) > 1, (1)

and its “T -smoothed” version

LS,T (χ, s) = LS(χ, s) ∏

p∈T
p ﬁnite
(1 − χ(p)Np1−s). (2)

3

Assume now that S contains the set S∞ of real places and the set Sram of ﬁnite primes
ramifying in H. Assume that T satisﬁes the Deligne–Ribet condition ensuring the integrality
of LS,T (χ, 0), namely that T contains two primes of diﬀerent residue characteristic, or one
prime of residue characteristic larger than n + 1.

Theorem 1.1 (Brumer–Stark Conjecture). Let p ̸∈ S ∪ T be a prime of F that splits
completely in H. Fix a prime P of H above p. There exists an element u ∈ H ∗ satisfying
the following.

• We have |u|w = 1 for all places w of H not lying above p, including the complex places.

• We have ∑

σ∈G χ(σ) ordσ−1(P)(u) = LS,T (χ, 0) (3)

for all characters χ : G −→ C∗.

• We have u ≡ 1 (mod qOH) for all q ∈ T .

1.2 Ritter–Weiss Modules

For the moment, let F be an arbitrary number ﬁeld, and H a ﬁnite abelian extension of F
with G = Gal(H/F ). Denote by S∞ the set of archimedean places of F and Sram the set
of ﬁnite places of F that ramify in H. Let Σ, Σ
′ denote disjoint ﬁnite sets of places of F
satisfying the following conditions:

(A1) Σ ∪ Σ
′ ⊃ S∞ ∪ Sram.

(A2) The torsion subgroup of

O∗
H,S∞,Σ′ = {u ∈ O∗
H : u ≡ 1 (mod q) for all primes q above primes in Σ
′}

is trivial.

We will deﬁne a Z[G]-module ∇Σ′
Σ (H) that generalizes the construction of Ritter–Weiss [23]
(which did not consider the smoothing set Σ
′) and our previous work [11] (which imposed
an additional condition Σ ⊃ S∞). The module ∇Σ′
Σ (H) sits in a short exact sequence of
Z[G]-modules 0 −→ ClΣ′
Σ (H) −→ ∇Σ′
Σ (H) −→ XH,Σ −→ 0.

Here XH,Σ denotes the group of degree zero divisors on the set of places of H above those
in Σ, and ClΣ′
Σ (H) is the Σ-depleted, Σ
′-smoothed class group of H (for a deﬁnition see
[11, page 292]).
To state our main result, we specialize the situation and impose further conditions on
Σ, Σ
′. Assume that F is totally real and that H is a CM ﬁeld. Denote by c ∈ G the complex
conjugation, and deﬁne Z[G]− = Z[G]/(1 + c).

4

Note that Z[G]− is ﬁnite free as a Z-module and in particular has no torsion. For any
Z[G]-module M, we deﬁne
 M− = M ⊗Z[G] Z[G]− = M/(1 + c)M.

Fix a prime p. We impose the further conditions

(A3) Σ ̸= ∅.

(A4) Σ ⊃ {v ∈ Sram : v | p}.

(A5) Σ
′ ⊃ {v ∈ Sram : v ∤ p}.

We write ∇Σ′
Σ (H)p,− = ∇Σ′
Σ (H) ⊗Z[G] Zp[G]−.

Under conditions (A1)–(A5), we prove that ∇Σ′
Σ (H)p,− is quadratically presented over Zp[G]−,
and hence that its Fitting ideal is principal. The following is our main result.

Theorem 1.2. Under conditions (A1)–(A5), we have

FittZp[G]−(∇Σ′
Σ (H)p,−) = (ΘΣ,Σ′/2t),

where t = #(S∞ ∩ Σ
′).

Here ΘΣ′
Σ /2t denotes the unique element of Zp[G]− such that

χ(ΘΣ′
Σ /2t) = LΣ,Σ′(χ
−1, 0)/2t (4)

for all odd characters χ ∈ ˆG. The congruence of Deligne–Ribet [15, Corollary 8.9] together
with the argument of Kurihara recalled in [11, Lemma 3.4] implies that there exists an
element satisfying (4) in c−1
2 Zp[G]. The existence of ΘΣ′
Σ /2t ∈ Zp[G]− follows. We thank
Kurihara for pointing this out to us.
Theorem 1.2 was proven for p odd in [11], so it suﬃces to prove the result for p = 2.
However, since most of the arguments presented here work for all p, we do not in general
set p = 2 in what follows (though we do provide certain arguments only for p = 2 when the
analogous results for p odd were already proven in [11]).

The paper is organized as follows. In §2, we state the main properties of the Ritter–
Weiss modules ∇Σ′
Σ (H) that we construct later. We explain how to deduce the Brumer–Stark
conjecture from Theorem 1.2 stated above. In §2.3–§2.4 we establish some notation. In §2.5
we prove the important and surprisingly delicate result that an inclusion in Theorem 1.2
is suﬃcient to imply an equality. In §2.7 we state precisely the main theorem from [12]
on Ribet’s Lemma in the residually indistinguishable case and thereby reduce the proof of
Theorem 1.2 to the construction of a triple ( ˜T, ϕ, ρ) satsifying certain properties, where ˜T

5

is a Hecke algebra, ϕ is certain homomorphism on ˜T, and ρ is a Galois representation of GF
valued in Frac( ˜T).
In §3 we construct these objects and verify their properties. We deﬁne ˜T as the Hecke
algebra of a space of group-ring valued Hilbert modular forms, as deﬁned in [11]. The ho-
momorphism ϕ arises through the construction of a group-ring family F that is congruent
to a family of Eisenstein series modulo Θ#
Σ,Σ′/2n. Here # denotes the Z-linear map from
Z[G] to itself given by g ↦→ g−1 for all g ∈ G. The Galois representation ρ is deﬁned from
the Galois representations associated to Hilbert modular cusp forms, with special care taken
in the case that ˜T is not reduced, a new feature which arises here from the insertion of an
auxiliary prime l into the set Σ.
In §4 we construct the Ritter–Weiss modules ∇Σ′
Σ (H) and establish their properties,
as outlined earlier in §2. We provide a less computational approach than given in our
previous work [11], which allows for the more general version required here and establishes
a connection with Galois cohomology even at the prime p = 2. This last feature requires a
new duality theorem on class formations that is proven in §5.

We would like to thank Frank Calegari, David Leoﬄer, and Sug Woo Shin for helpful
discussions regarding the constructions of §3, particularly the results in §3.3. We would also
like to thank Cristian Popescu, Masato Kurihara, and Andreas Nickel for helpful discussions.
The ﬁrst named author is supported by NSF grant DMS–2200787. The second named
author is supported by DST-SERB grant SB/SJF/2020-21/11, SERB MATRICS grant
MTR/2020/000215, SERB SUPRA grant SPR/2019/000422, and DST FIST program - 2021
[TPN - 700661]. The fourth named author is supported by NSF grant DMS 2201346.

2 Ritter–Weiss Modules and Brumer–Stark

In this section we ﬁrst state precisely the properties satisﬁed by the generalized Ritter–
Weiss modules ∇Σ′
Σ (H) that we construct in §4. We then explain how Theorem 1.2 implies
the Brumer–Stark conjecture. Next, we will establish some preliminaries and outline the
proof of Theorem 1.2.

2.1 Properties of Ritter–Weiss Modules

Consider an abelian extension of global ﬁelds H/F , with G = Gal(H/F ). Fix ﬁnite disjoint
sets of places S, T of F , such that S ∪ T contains all inﬁnite places of F . We do not require
that all inﬁnite places lie in S, unlike previous constructions of Ritter–Weiss [23] and of the
ﬁrst two named authors [11].
We will construct a Z[G]-module ∇T
S (H), the generalized Ritter–Weiss module, as the
cokernel of a map V θ −→ Bθ of ﬁnitely generated Z[G]-modules. In this section we state
the main properties of the modules ∇T
S (H). These properties will be proved in §4.

6

Consider the following conditions:

(A) S ∪ T contains all ﬁnite places of F that ramify in H.

(B) For all ﬁnite places v ∈ T , Hw/Fv is tamely ramiﬁed.

(Bp) For all ﬁnite places v ∈ T , Hw/Fv is p-tamely ramiﬁed (the wild inertia subgroup of
Hw/Fv has order coprime to p).

(C) The reduction map µ(H) −→ F
∗
T = ∏

ﬁnite w∈TH(OH /w)∗

is injective, i.e. O∗
H,S,T is torsion-free. Here O∗
H,S,T is the set of all S-units congruent
to 1 modulo all primes above primes in T .

Although we typically assume (A), (Bp), and (C) in the body of this paper, in §2.2 we
brieﬂy consider a Ritter–Weiss module where condition (A) does not hold. The following
theorems also distinguish between results for general extensions H/F where S contains all
the inﬁnite places, versus results for CM extensions H/F where S ∪T contains all the inﬁnite
places. The former results have largely been proven in [23] and [11], and we reprove them
for the sake of completeness.

Theorem 2.1. We have:

1. The module ∇T
S (H) contains Cl
T
S (H) as a Z[G]-submodule, giving an exact sequence

0 −→ ClT
S (H) −→ ∇T
S (H) −→ X −→ 0. (5)

Under assumption (A), X = XH,S.

2. If H/F is a CM extension and S contains a place v such that the complex conjugation
c ∈ G belongs to the decomposition group Gv, then

0 −→ ClT
S (H)− −→ ∇T
S (H)− −→ X− −→ 0 (6)

is an exact sequence of Z[G]− modules.

Theorem 2.2. Assume (B) and (C).

1. When S contains all the inﬁnite places, the modules V θ and Bθ are projective Z[G]-
modules. There is an exact sequence

0 −→ O∗
H,S,T −→ V θ −→ Bθ −→ ∇T
S (H) −→ 0.

If we additionally assume (A), this is a quadratic presentation.

7

2. Suppose that H/F is a CM extension. When S ̸= ∅, there exists a map of ﬁnitely-
generated projective Z[G]−-modules V ′ −→ (Bθ)−, giving the following presentation of
∇T
S (H)−: 0 −→ (O∗
H,S,T )− −→ V ′ −→ (Bθ)− −→ ∇T
S (H)− −→ 0. (7)

If we additionally assume (A), this is a quadratic presentation.

If we assume (Bp) instead of (B), analogous results hold after tensoring (over Z) all the
modules above with Z(p).

We will prove that ∇T
S (H) has the following relationship to Galois cohomology.

Theorem 2.3. Assume (A) and either (B) or (Bp). Assume S ̸= ∅, and ﬁx v0 ∈ S. Let N
be a ﬁnite G-module, and if we are in case (Bp) assume that N is a p-group. Suppose we
are given a 1-cocycle κ : GF −→ N and xv ∈ N for v ∈ S \ {v0} such that

1. κ(GFv0 ) = 0

2. κ|GFv is unramiﬁed for v /∈ (S ∪ T )

3. κ|GFv is tamely ramiﬁed for ﬁnite v ∈ T

4. for v ∈ S, κ(σv) = (σv − 1)xv for all σv ∈ GFv.

Then there exists a G-equivariant map ∇T
S (H) −→ N whose image is the Z[G]-submodule
generated by κ(GF ) and the xv.

2.2 Brumer–Stark

As mentioned in the introduction, we will prove in a forthcoming paper that Theorem 1.2
implies the Equivariant Tamagawa Number Conjecture for the minus part of the Tate mo-
tive associated to H/F . This is a powerful statement with many corollaries, including the
Brumer–Stark conjecture. Because of its singular importance, however, we would like to
prove here that the Brumer–Stark conjecture follows directly from Theorem 1.2.
Let S and T be as in the statement of Theorem 1.1.

Theorem 2.4. We have
 Θ#
S,T /2n−1 ∈ AnnZ[G]−((Cl
T (H)−)∨), (8)

or equivalently ΘS,T /2n−1 ∈ AnnZ[G]−(ClT (H)−). (9)

The equivalence of the statements follows since the annihilators of a module and its
Pontryagin dual are related by #.
 8

Proof. The statement (8) over Z[1/2] follows from the result

Θ#
S,T ∈ FittZ[1/2][G]−(ClT (H)∨ ⊗Z[G] Z[1/2][G]−)

known as the Strong Brumer–Stark conjecture that is proved in [11]. So it remains to consider
the statement (8) after tensoring with Z2. We ﬁx a real place w of F and deﬁne

Σ = {w} ∪ {v ∈ Sram : v | 2}, Σ
′ = T ∪ {v ∈ Sram, v ∤ 2} ∪ S∞ \ {w}.

Then Theorem 1.2 applies and we have

FittZ2[G]−(∇Σ′
Σ (H)2,−) = (ΘΣ,Σ′/2n−1).

Let SelΣ′
Σ (H)− denote the transpose of ∇Σ′
Σ (H)− over Z[G]− associated to the presentation
(7) deﬁning this latter Z[G]−-module, as described in §4.
Let s = #{v ∈ Sram, v ∤ 2}. The argument of [11, Theorem 3.7] applies directly to yield

FittZ2[G]−(SelT
Σ(H)2,−) = Fitts
Z2[G]−(∇T
Σ(H)2,−)#

= (ΘΣ,T /2n−1)# ∏

v∈Sram, v∤2
(NIv, 1 − σvev).

Let s′ = #Sram. The arguments of [11, Appendix B] yield

FittZ2[G]−(SelT
{w}(H)2,−) = Fitt
s′
Z2[G]−(∇T
{w}(H)2,−)#

= (Θ∅,T /2n−1)# ∏

v∈Sram
(NIv, 1 − σvev)

⊃ (ΘS,T /2n−1)#.

It follows that Θ#
S,T /2n−1 annihilates SelT
{w}(H)2,−. By Lemma 4.21, we have a short exact
sequence
 0 −→ (∇T
{w}(H)−)∨
tors −→ SelT
{w}(H)− −→ (HomZ(O∗
H,{w},T , Z))−)∨ −→ 0.

By Proposition 4.7, (∇T
{w}(H)−)∨
tors has (Cl
T (H)−)∨ as a quotient. It follows that Θ#
S,T /2n−1

annihilates (ClT (H)−)∨ as desired.

The Brumer–Stark conjecture follows easily from Theorem 2.4; in fact we get a stronger
statement with ΘS,T replaced by ΘS,T /2n−2.

Proof of Theorem 1.1. Let P be as in the statement of Theorem 1.1. Theorem 2.4 implies
that ΘS,T /2n−1 annihilates the class of P in ClT (H)−. We may therefore write

P
ΘS,T /2n−1 = (z)a1+c (10)

9

where z ≡ 1 (mod T ) and a ∈ IT (H) is a fractional ideal of H coprime to T . Applying 1 − c
to (10), writing u = z1−c, and noting (1 − c)ΘS,T = 2ΘS,T , we obtain

P
ΘS,T /2n−2 = (u) (11)

where u ≡ 1 (mod T ) and u has absolute value 1 under every complex embedding. Clearly
u is a p-unit and satisﬁes (3) with ΘS,T replaced by ΘS,T /2n−2. Our result is proven as
long as n ≥ 2. But n = 1 happens when F = Q, and the Brumer–Stark conjecture here is
Stickelberger’s classical theorem.

2.3 Minimal Sets

It will be convenient in our constructions with modular forms to consider certain minimal
sets Σ. To relate the modules ∇ and Stickelberger elements Θ as Σ, Σ
′ vary, we note the
following result proven in §4.7.

Lemma 2.5. Assume (A1)–(A5). We have the following:

• Let w ∈ Σ
′ be a real place. Then

FittZp[G](∇Σ′\w
Σ∪{w}(H)) = 2 FittZp[G](∇Σ′
Σ (H)).

• Let l ̸∈ Σ ∪ Σ
′, so by the assumptions, l is a ﬁnite prime unramiﬁed in H. Put σl for
the associated Frobenius element. Then

FittZp[G](∇Σ′
Σ∪{l}(H)) = (1 − σ−1
l ) FittZp[G](∇Σ′
Σ (H))

and ΘΣ∪{l},Σ′ = (1 − σ−1
l )ΘΣ,Σ′.

Similarly we have

FittZp[G](∇Σ′∪{l}
Σ (H)) = (1 − σ−1
l Nl) FittZp[G](∇Σ′
Σ (H))

and ΘΣ,Σ′∪{l} = (1 − σ−1
l Nl)ΘΣ,Σ′.

Lemma 2.5 shows that if Σ ⊂ Σ1 and Σ
′ ⊂ Σ
′
1, then Theorem 1.2 for (Σ, Σ
′) implies
the result for (Σ1, Σ
′
1). Furthermore the distribution of real places between Σ, Σ
′ does not
aﬀect the validity of the conjecture (as long as we always maintain the assumption that Σ is
nonempty). In what follows, we will therefore ﬁx certain pairs (Σ, Σ
′) with Σ minimal and
prove the result in this setting. As in [11], it is convenient to establish two cases that will
appear throughout the paper.

Case 1. There are no primes above p ramiﬁed in H/F .

10

In this case, we ﬁx a prime l of F that is unramiﬁed in H such that the associated
Frobenius σl ∈ G is the complex conjugation c. We then deﬁne

Σ = {l},

Σ
′ = T ∪ S∞ ∪ Sram.

Any other pair (Σ, Σ
′) with minimal Σ in Case 1 will either have the form

Σ1 = {l′},

Σ
′
1 = T ∪ S∞ ∪ Sram

for another ﬁnite prime l′ or have the form

Σ2 = {v},

Σ
′
2 = T ∪ (S∞ \ {v}) ∪ Sram

for a real place v. Lemma 2.5 yields

ΘΣ1,Σ′
1 = 1
2 Θ{l′,l},Σ′
1 = 1 − σ−1
l′
2 ΘΣ,Σ′

FittZp[G]−(∇Σ′
1
Σ1(H)p,−) = 1
2 FittZp[G]−(∇Σ′
1
{l,l′}(H)p,−) = 1 − σ−1
l′
2 FittZp[G]−((∇Σ′
Σ )p,−).

Therefore the statements of Theorem 1.2 for the pairs (Σ, Σ
′) and (Σ1, Σ
′
1) are equivalent.
A similar calculation holds for (Σ2, Σ
′
2); by Lemma 2.5, moving an inﬁnite place from Σ
′ to
Σ multiplies the Fitting ideal of ∇ by 2. Therefore, in Case 1, proving Theorem 1.2 for the
particular pair (Σ, Σ
′) above implies the result for all pairs satisfying our conditions.

Case 2. There exists a prime above p ramiﬁed in H/F .

In this case, there is a unique minimal Σ, and it suﬃces to prove Theorem 1.2 in this
setting:
 Σ = {v ∈ Sram : v | p},

Σ
′ = T ∪ S∞ ∪ {v ∈ Sram : v ∤ p}.

2.4 Character Group Rings

Let O denote the ring of integers of a ﬁnite extension of Qp containing the values of all
characters χ ∈ ˆG. There is a Zp-algebra injection

Zp[G] −→ ∏

χ∈ ˆG O, x ↦→ (χ(x)).

11

In our constructions with modular forms, we would like to work with local rings (as opposed
to the semilocal ring Zp[G]−). Furthermore, it will be convenient if the Stickelberger ele-
ment ΘΣ,Σ′ is a nonzerodivisor in our ring. To this end, for every Gal(Qp/Qp)-stable set of
characters Ψ ⊂ ˆG we deﬁne the associated character group ring

RΨ = Image(Zp[G] −→ ∏

χ∈Ψ O), x ↦→ (χ(x)).

If we deﬁne Ψ = {χ ∈ ˆG : χ is odd and χ(Gv) ̸= 1 for all v ∈ Σ}

then the image of the Stickelberger element ΘΣ,Σ′ in RΨ is a nonzerodivisor. If M is any
Zp[G]-module, we write MΨ = M ⊗Zp[G] RΨ.

Write G = Gp × G′ where Gp is a p-group and G′ has order relatively prime to p. For
each Gal(Qp/Qp)-conjugacy class of characters Φ of G′, we deﬁne

Φ0 = {χ ∈ ˆG : χ is odd , χ|G′ ∈ Φ, and χ(Gv) ̸= 1 for all v ∈ Σ}. (12)

Then each RΦ0 is a local ring in which ΘΣ,Σ′ is a nonzerodivisor, and we have a decomposition

RΨ = ∏

Φ RΦ0, (13)

where Φ runs through all Gal(Qp/Qp)-conjugacy classes of characters of G′.
The following result was proven in [11, Lemmas 2.4 and 2.5].

Lemma 2.6. Let M be a quadratically presented module over a character group ring RΨ
such that FittRΨ(M) = (x). Then M is ﬁnite if and only if x is a nonzerodivisor, and in
this case we have #M = #(RΨ/(x)) = #(Zp / ∏

ψ∈Ψ ψ(x)).

Here # denotes size.

2.5 Inclusion Implies Equality

We recall the setting. We have a totally real ﬁeld F and a CM abelian extension H/F . We
write G = Gal(H/F ). Fix a prime p and deﬁne

Σ = S∞ ∪ {v ∈ Sram : v | p},

Σ
′ = T ∪ {v ∈ Sram : v ∤ p}.

Let Φ0 be as in (12). Our goal in this section is to prove:

12

Theorem 2.7. Suppose that for every setting as above, we have

FittRΦ0 (∇Σ′
Σ (H)Φ0) ⊂ (ΘΣ,Σ′). (14)

Then every such inclusion is actually an equality, and

FittZp[G]−(∇Σ′
Σ (H)p,−) = (ΘΣ,Σ′). (15)

Remark 2.8. In the previous section we deﬁned certain minimal sets (Σ, Σ
′). As mentioned,
moving t inﬁnite primes from Σ
′ to Σ multiplies the Fitting ideal of ∇ by 2t. Furthermore
removing a prime l from Σ whose Frobenius equals c (when Σ \ {l} is nonempty) has the
eﬀect of dividing both Θ and the Fitting ideal of ∇ by 2. So Theorem 2.7 implies that if we
always have FittZp[G]−(∇Σ′
Σ (H)p,−) ⊂ (ΘΣ,Σ′/2t)

for our minimal (Σ, Σ
′), then these inclusions are all equalities, and (15) holds.

Theorem 2.7 was proven for p odd in [11], so we will assume for the remainder of this
section that p = 2. Let

Ψ = {χ ∈ ˆG : χ is odd and χ(Gv) ̸= 1 for all v ∈ Σ}

and let RΨ be the associated character group ring. In view of the product decomposition
(13), the following lemma implies that the ﬁrst assertion of Theorem 2.7 implies the second.

Lemma 2.9. With notation as above, if

FittRΨ(∇Σ′
Σ (H)Ψ) = (ΘΣ,Σ′),

then FittZp[G]−(∇Σ′
Σ (H)p,−) = (ΘΣ,Σ′).

Lemma 2.9 was proven in [11, Lemma 7.1]. The key point is that if Ψ denotes the set of
odd characters of G not lying in Ψ, then

FittRΨ(∇Σ′
Σ (H)Ψ) = 0 = ΘΣ,Σ′RΨ.

We now prove the ﬁrst assertion of Theorem 2.7. By Proposition 4.13 the module
∇Σ′
Σ (H)Ψ is quadratically presented and therefore its Fitting ideal is principal. Write

FittRΨ(∇Σ′
Σ (H)Ψ) = (x).

Since RΨ = ∏

Φ RΦ0, (14) implies that (x) ⊂ (ΘΣ,Σ′) in RΨ and hence it suﬃces to prove
that #RΨ/(x) = #RΨ/(ΘΣ,Σ′).

13

Now it follows from Lemma 2.6 that

#∇Σ′
Σ (H)Ψ = #RΨ/(x) = #Z2 ∕ ∏

α∈Ψ α(x)

and #RΨ/(ΘΣ,Σ′) = #Z2 ∕ ∏

α∈Ψ LΣ,Σ′(α−1, 0) = 2-part of ∏

α∈Ψ LΣ,Σ′(α−1, 0).

We must therefore show #∇Σ′
Σ (H)Ψ .
= ∏

α∈Ψ LΣ,Σ′(α−1, 0), (16)

where .
= indicates equality up to a 2-adic unit. This will be achieved through the analytic
class number formula. We prove (16) by partitioning Ψ into Gal(Q2/Q2) conjugacy classes.
For such a conjugacy class Φ, we have

#∇Σ′
Σ (H)Φ .
= ∏

α∈Φ α(x),

and we will show:

Theorem 2.10. With notation as above, under the assumption of Theorem 2.7, we have

#∇Σ′
Σ (H)Φ .
= ∏

α∈Φ LΣ,Σ′(α−1, 0). (17)

Taking the product of (17) over all possible Gal(Q2/Q2) conjugacy classes Φ ⊂ Ψ yields
(16) and completes the proof of Theorem 2.7. In the remainder of the section, we prove
Theorem 2.10. Let HΦ denote the ﬁxed ﬁeld in H of the kernel of any character in Φ.

Lemma 2.11. We have ∇Σ′
Σ (H)Φ ∼= ∇Σ′
Σ (HΦ)Φ. (18)

Proof. Since ∇Σ′
Σ (H)Φ ∼= (∇Σ′
Σ (H)Gal(H/HΦ))Φ, this follows from Lemma 4.6.

Write GΦ = Gal(HΦ/F ). The conjugacy class Φ can be written Φ = φ0φ1 where φ0
is a conjugacy class of 2-power order characters and φ1 is a conjugacy class of odd order
characters. This corresponds to the decomposition GΦ = G2 × G′ of GΦ as a product of a
2-group and an odd order group. Since G′ has odd order and we are working over Z2, we
have a decomposition Z2[GΦ]− = ∏

ψ Rψ, (19)

where the product ranges over the Galois conjugacy classes of characters of G that can be
written φ0φ′, where φ′ is a conjugacy class of characters of G′. The essential point here is
that every odd character of GΦ has restriction to G2 lying in φ0. (This is the key point where

14

p = 2 is being used in this proof, and explains why the argument of [11, §5] for p odd was
diﬀerent.)
In view of (19), we have
 ClΣ′(HΦ)− = ∏

ψ ClΣ′(HΦ)ψ.

By [11, Lemma 5.2], we have ClΣ′(HΦ)ψ ∼= ClΣ′(Hψ)ψ. (20)

To avoid trivial zeroes, we need to consider

Σc = {v ∈ Σ : c ∈ Gv} ⊃ S∞.

Let Σψ = Σc ∪ {v ∈ Sram(Hψ/F ), v | 2}.

We have the short exact sequence

0 −→ Cl
Σ′
Σψ (Hψ)ψ −→ ∇Σ′
Σψ (Hψ)ψ −→ (XΣψ,Hψ )ψ −→ 0.

The inclusion (14) for the ﬁeld Hψ implies that
∏

α∈ψ LΣψ,Σ′(α−1, 0) | #∇Σ′
Σψ (Hψ)ψ = # Cl
Σ′
Σψ (Hψ)ψ · #(XΣψ,Hψ)ψ, (21)

where the divisiblity occurs in Z2.

Lemma 2.12. We have

• LΣψ,Σ′(α−1, 0) = LΣc,Σ′(α−1, 0).

• Cl
Σ′
Σψ (Hψ)ψ ∼= ClΣ′
Σc(Hψ)ψ.

• (XΣψ,Hψ )ψ ∼= (XΣc,Hψ )ψ ∼= (XΣc,HΦ)ψ

Proof. The ﬁrst bullet point is clear, since by deﬁnition, if v ∈ Σψ \ Σc then any α ∈ ψ is
ramiﬁed at v. For the second bullet point, the kernel of

ClΣ′
Σc(Hψ) −։ ClΣ′
Σψ (Hψ)

is the subgroup generated by the primes lying above v ∈ Σψ \ Σc. Such a prime is ﬁxed by
the inertia subgroup Iv, but since any α ∈ ψ is ramiﬁed at v there exists a σ ∈ Iv such that
α(σ) ̸= 1 for all α ∈ ψ. Since c ̸∈ Gv, Iv has odd order and α(σ) is an odd order root of unity.
Thus 1 − α(σ) is a 2-adic unit, and the image of the class represented by v in Cl
Σ′
Σc(Hψ)ψ is
trivial.
The proof of the ﬁrst isomorphism in the third bullet point is similar, and the second
isomorphism is elementary.
 15

Combining (20), (21), and Lemma 2.12, and taking the product over all ψ, we obtain
∏

α∈ ˆGΦ, α odd LΣc,Σ′(α−1, 0) | # Cl
Σ′
Σc(HΦ)− · #(XΣc,HΦ)−. (22)

Lemma 2.13. The divisibility in (22) is an equality up to sign.

Proof. By the Artin formalism for L-functions, the left side of (22) may be written
∏

α∈ ˆGΦ, α odd LΣc,Σ′(α−1, 0) = LΣc,Σ′(HΦ/H +
Φ , ǫ, 0)

where H +
Φ denotes the maximal totally real subﬁeld of the CM ﬁeld HΦ, and ǫ is the non-
trivial character of Gal(HΦ/H +
Φ ). Dividing the analytic class number formulas for ζHΦ,Σc,Σ′(s)
and ζH +
Φ ,Σc,Σ′(s) at s = 0 (see [11, Equation (25)]) yields

LΣc,Σ′(HΦ/H +
Φ , ǫ, 0) = ± # ClΣ′
Σc(HΦ)

# ClΣ′
Σc(H +
Φ ) · RΣ′
Σc(HΦ)
RΣ′
Σc(H +
Φ ) . (23)

The groups associated to the indicated regulators are the same, namely

O∗
HΦ,Σc,Σ′ = O∗
H +
Φ ,Σc,Σ′,

but the normalization of the absolute values is oﬀ by a factor of 2 in each entry of the regulator
matrix. As a result, the ratio of the regulators on the right side of (23) is 2#(Σc)HΦ −1. It
remains to prove that # ClΣ′
Σc(HΦ)

# Cl
Σ′
Σc(H +
Φ ) = # Cl
Σ′
Σc(HΦ)− (24)

and #(XΣc,HΦ)− = 2#(Σc)HΦ −1. (25)

The second of these is straightforward and follows from the short exact sequence

0 −→ (XΣc,HΦ)− −→ (YΣc,HΦ)− −→ Z− = Z/2Z −→ 0.

(The left exactness of this sequence can be established directly, and also follows from
Lemma 4.8, which implies TorZ[G]
1 (Z, Z[G]−) = Z+[2] = 0.) Indeed, for v ∈ Σc we have
c ∈ Gv so the module (Yv,HΦ)− ∼= Z[GΦ/Gv]/2 has size 2#{w|v}, where the exponent is the
number of places w of HΦ dividing v. This proves (25).
To prove (24), we note there is a short exact sequence

1 ClΣ′
Σc(HΦ)− ClΣ′
Σc(HΦ) ClΣ′
Σc(H +
Φ ) 1,
N (26)

where the labelled arrow is given by the norm. Here the superscript on Cl
Σ′
Σc(HΦ)− denotes
the largest subgroup (rather than quotient, which is indicated by a subscript) on which c acts

16

as −1. It is clear that ClΣ′
Σc(HΦ)− contains the kernel of the norm but a small observation is
needed to deduce equality: suppose aac = (x)b where x ∈ (HΦ)∗
Σ′ and b is in the subgroup of
fractional ideals generated by the primes above Σc. Dividing this equation by its conjugate,
we see that (x/x
c) = (1). Therefore x/x
c ∈ O∗
HΦ,S∞,Σ′ = O∗
H +
Φ ,∅,Σ′. But x/x
c has absolute
value 1 in every complex embedding, and O∗
H +
Φ ,S∞,Σ′ contains no nontrivial roots of unity, so

x = x
c, i.e. x ∈ (H +
Φ )∗
Σ′. Thus a lies in the kernel of the norm.
We should also comment on the surjectivity of the norm map in (26). By class ﬁeld theory,
the cokernel of this map is identiﬁed with the Galois group of the largest subextension of
HΦ/H +
Φ in which the primes in Σc split completely. Since this includes the inﬁnite primes,
the largest such subextension is trivial (the point here is that in the deﬁnition of ClΣ′
Σc(H +
Φ )
one takes the quotient by principal ideals generated by all elements of (H +
Φ )∗
Σ′, not just the
totally positive elements).
To conclude the proof, we just need to note the equality # ClΣ′
Σc(HΦ)− = # ClΣ′
Σc(HΦ)−,
which follows from the tautological short exact sequence

1 ClΣ′
Σc(HΦ)− ClΣ′
Σc(HΦ) ClΣ′
Σc(HΦ) Cl
Σ′
Σc(HΦ)− 1.
1+c

In view of Lemma 2.13, it follows that all the divisibilities (21) used to deduce (22) are
equalities up to 2-adic units. For ψ = Φ this says

#∇Σ′
ΣΦ(HΦ)Φ .
= ∏

α∈Φ LΣΦ,Σ′(α−1, 0). (27)

Now, the primes in Σ\ΣΦ are unramiﬁed for the characters in HΦ. Adding unramiﬁed primes
to the smoothing set simply multiplies the Fitting ideal of ∇ by the Euler factor (1 − σ−1
v )
at those primes, so we immediately obtain from (27)

#∇Σ′
Σ (HΦ)Φ .
= ∏

α∈Φ LΣ,Σ′(α−1, 0).

In view of Lemma 2.11, this concludes the proof of Theorem 2.10 and hence of Theorem 2.7.

2.6 Summary

The following result summarizes the results obtained in §2 so far.

Theorem 2.14. Fix a prime p. In Case 1 (no primes above p are ramiﬁed in H) let

Σ = {l}

for some ﬁnite unramiﬁed prime l ∤ p whose Frobenius in G equals the complex conjugation
c. In Case 2, let Σ = {v ∈ Sram : v | p}.

17

In both cases let Σ
′ = T ∪ {v ∈ Sram : v ∤ p} ∪ S∞.

For each Gal(Qp/Qp)-conjugacy class of characters Φ of G′, let

Φ0 = {χ ∈ ˆG : χ is odd, χ(Gv) ̸= 1 for all v ∈ Σ, and χ|G′ ∈ Φ}

and let R = RΦ0 be the associated character group ring. Suppose that for each Φ we have
an R-module N and a cocycle κ ∈ Z 1(GF , N) satisfying the conditions of Theorem 2.3 such
that FittR(N) ⊂ (ΘΣ,Σ′/2n)R. (28)

Then we have FittZp[G]−(∇Σ′
Σ (H)p,−) = (ΘΣ,Σ′/2n) (29)

and in particular, the p-part of the Brumer–Stark conjecture holds.

Proof. Theorem 2.3 yields a surjective map ∇Σ′
Σ (H)R −→ N, which in conjunction with the
inclusion (28) yields FittR(∇Σ′
Σ (H)R) ⊂ (ΘΣ,Σ′/2n)R.

By Theorem 2.7, the equality (29) holds. The p-part of the Brumer–Stark conjecture holds
from the discussion of §2.2.

2.7 Ribet’s Lemma

The following version of Ribet’s Lemma applicable to our setting is proved in [12]. Of central
importance is the fact that the condition of residual distinguishability χ ̸≡ ψ (mod m) is
not assumed.

Theorem 2.15. Let T ⊂ ˜T be an inclusion of commutative Noetherian rings, with T local.
Suppose that T and ˜T are complete with respect to the maximal ideal of T. Let ˜I ⊂ ˜T be
a nontrivial ideal and let I = ˜I ∩ T. Let K = Frac( ˜T) be the total ring of fractions of ˜T
and assume that the maximal ideals of K are principal. Suppose we are given a continuous
representation ρ : GF −→ GL2(K)

satisfying the following conditions.

• For σ ∈ GF , the characteristic polynomial Pρ(σ)(x) lies in T[x]. Furthermore we have

Pρ(σ)(x) ≡ (x − χ(σ))(x − ψ(σ)) (mod I)

for two characters χ, ψ : GF −→ T∗.
 18

• Let K0 = red(K) denote the maximal reduced quotient of K. Write K0 = ∏m
i=1 ki as a
product of ﬁelds. For every projection K → K0 → ki, the projection of ρ to GL2(ki) is
an irreducible representation of GF over ki.

• There is a set of primes S such that for all v ∈ S, there exists a basis in which the
restriction of ρ to a decomposition group Gv ⊂ GF has the form

ρ|Gv ∼= (ηv 0
∗ ξv
) (30)

for two characters ξv, ηv : Gv −→ ˜T∗.

• There is a subset Σ ⊂ S such that for each v ∈ Σ, we have ξv ≡ ψ|Gv (mod ˜I).

• Let P = S \ Σ. For all v ∈ P, we have (ξv)|Iv ≡ χ|Iv (mod ˜I). Here Iv ⊂ Gv denotes
the inertia group at v.

If Σ is nonempty, ﬁx v0 ∈ Σ. Choose an element σv ∈ Gv for each v ∈ P. Then there exists
a ﬁnitely generated T-module N and a continuous cocycle

κ ∈ Z 1(GF , N(χψ−1))

satisfying the following conditions.

• The module N is generated over T by κ(GF ) and the yv, v ∈ Σ \ {v0}.

• The cohomology class represented by κ is unramiﬁed at any prime for which ρ is un-
ramiﬁed.

• If Σ is nonempty, we have κ(Gv0) = 0 and for each v ∈ Σ \ {v0}, there exists yv ∈ N
such that κ(σ) = (χψ−1(σ) − 1)yv

for all σ ∈ Gv.

• For each v ∈ P, we have κ(σ) = 0 for all σ ∈ Iv.

• We have ∏

v∈P(ξv(σv) − χ(σv)) FittT(N) ⊂ ˜I. (31)

We conclude this section by combining Theorems 2.14 and 2.15 to show that in order to
prove our main result (Theorem 1.2), it suﬃces to construct a Galois representation with
the desired properties. As explained in [11, §4.1], we may assume that T (and hence also Σ
′)
contains no primes above p, as removing such primes alters neither of the ideals (ΘΣ,Σ′/2n)
nor FittR(∇Σ′
Σ (H)R).
 19

Theorem 2.16. Let the notation be as in the statement of Theorem 2.14. Suppose we are
given an inclusion of commutative Noetherian rings T ⊂ ˜T, with T local. Suppose that
T and ˜T are complete with respect to the maximal ideal of T. Suppose further we have a
continuous Galois representation
 ρ : GF −→ GL2(Frac( ˜T))

satisfying the properties of Theorem 2.15 where:

• The set Σ is as in Theorem 2.14 and P is equal to the set of primes above p that are
not in Σ.

• The representation ρ is unramiﬁed outside Σ ∪ Σ
′ ∪ P.

• We have ψ = ψψψ, where ψψψ is the canonical character ψψψ : GF −→ G −→ T∗. We have
χ ≡ 1 (mod pm) for some positive integer m large enough that (Θ#
Σ,Σ′/2n) divides pm

in R.

• T/I is cyclic as an R-module, i.e. the structure map R −→ T/I is surjective.

• If y ∈ R and (∏

v∈P (ξv(σv) − χ(σv)))y ∈ ˜I, then y ∈ (Θ#
Σ,Σ′/2n)R.

Then Theorem 1.2 follows.

Proof. Theorem 2.15 provides a T-module N and a cocycle κ ∈ Z 1(GF , N(χψψψ−1)). We
consider N = N/(IN, pmN). The projection of κ to N can be viewed as a cocycle

κ ∈ Z 1(GF , N(ψψψ−1))

since χ ≡ 1 (mod pm).
Since T/I is a cyclic R-module, the T-module generators of N reduce to R-module
generators of N. All of the properties required by Theorem 2.3 are directly seen to be
satisﬁed by the corresponding properties in Theorem 2.15, except for possibly the discussion
of ramiﬁcation. The Galois representation ρ is unramiﬁed outside Σ ∪ Σ
′ ∪ P, so κ is
unramiﬁed outside this set. Furthermore, we are given in Theorem 2.15 that κ is unramiﬁed
at P, and that the local conditions at Σ hold. Finally, κ is tamely ramiﬁed at the ﬁnite
primes in Σ
′ since our module is pro-p and Σ
′ contains no primes above p.
To conclude, we must explain why FittR(N (ψψψ−1)) ⊂ (ΘΣ,Σ′/2n), or equivalently,

FittR(N) ⊂ (Θ#
Σ,Σ′/2n). (32)

We have

FittR(N ) ⊂ FittR(N/IN) + pmR ⊂ FittT(N/IN) + pmR ⊂ FittT(N) + I + pmR.

20

Therefore, if y ∈ FittR(N), there exists r ∈ R and i ∈ I such that y + i + pmr ∈ FittT(N),
so by (31) we have ∏

v∈P(ξv(σv) − χ(σv))(y + pmr) ⊂ ˜I.

The last assumption of the theorem then yields y + pmr ∈ (Θ#
Σ,Σ′/2n) and since Θ#
Σ,Σ′/2n

divides pm, we obtain y ∈ (Θ#
Σ,Σ′/2n) as desired.

In §3, we will use group-ring valued Hilbert modular forms to construct the Galois rep-
resentation required by Theorem 2.16.

3 Modular Forms

Let Σ, Σ
′, and R = RΦ0 be as in the statement of Theorem 2.14. Recall that Σ
′ contains no
primes above p (see comment preceding Theorem 2.16).
The goal of this section is to describe certain Hecke algebras Tm ⊂ ˜Tm, which will be
Noetherian R-algebras that are complete with respect to the maximal ideal m ⊂ T. We will
associate to this algebra:

1. An R-algebra homomorphism ϕ : ˜Tm −→ W where W is another R-algebra, satisfying
the following:

(a) The homomorphism ϕ is Eisenstein in the sense that ϕ(Tq) = 1 + ψψψ(q) for primes
q ̸∈ Σ ∪ Σ
′, q ∤ p.

(b) The restriction of ϕ to Tm induces an isomorphism Tm ∼= R/(xΘ#
Σ,Σ′/2n) where x
is a certain nonzerodivisor in R.

(c) For a speciﬁc element U ∈ ˜Tm to be deﬁned later, if y ∈ R and ϕ(Uy) = 0, then
y ∈ (Θ#
Σ,Σ′/2n)R.

2. A continuous Galois representation

ρ : GF −→ GL2(K), K = Frac( ˜Tm)

such that tr(ρ(Frobq)) = Tq for q ̸∈ Σ ∪ Σ
′, q ∤ p.

The homomorphism ϕ and representation ρ will satisfy certain other local properties as
required in Theorem 2.16. The construction of ϕ follows the argument in [11] with one
exception—the introduction of the prime l ∈ Σ in Case 1 requires an altered deﬁnition
of the necessary cusp form (Corollary 3.6). Similarly in the construction of the Galois
representation ρ, subtleties arising from forms old at l arise in Case 1. In this section we will
focus only on these new aspects, while stating without proof the results carried over directly
from [11]. For simplicity, we will simply write Θ# for Θ#
Σ,Σ′ in this section.

21

3.1 Hecke Algebra

We use the deﬁnitions and notations concerning Hilbert modular forms and group-ring valued
Hilbert modular forms as given in [11, §7.2–7.3]. We will follow closely the construction of
loc. cit. §8. Deﬁne
 n = cond(H/F ) ∏

q|T q,

P = gcd(p∞, n),

P
′ = ∏

p|p,p∤P p.

Recall also the cases that were deﬁned in §2.3 above—Case 1 is when P = 1 and Case 2
is when P ̸= 1. In Case 1 we introduced an auxiliary prime l to ensure that Σ is non-empty.
We deﬁne
 ˜n = { nl in Case 1
n in Case 2.

We will be considering group-ring valued Hilbert modular forms of level ˜nP
′ and weight k,
where k is a large positive integer congruent to 1 modulo (p − 1)pN for N suﬃciently large.
We denote by ψψψ : GF −→ G −→ R∗

the canonical character and consider the space of p-ordinary cusp forms Sk(˜nP
′, R, ψψψ)p−ord.
Let T ⊂ EndR(Sk(˜nP
′, R, ψψψ)p−ord) denote the Hecke algebra of this space generated over
R by the following operators:

• Tq for q ∤ ˜nP
′,

• Up for p | P,

• the diamond operators S(a) for (a, ˜nP
′) = 1.

Let ˜T ⊃ T denote algebra generated over T by the operators Up for p | P
′, and in Case 1,
the operator Ul.

In the next subsection, we will construct a modular form Fk(ψψψ) ∈ Sk(˜nP
′, R, ψψψ)p−ord that
is congruent to an Eisenstein series modulo the maximal ideal of R (in fact we prove a much
stronger congruence). The existence of this form implies the following.

Lemma 3.1. Let k denote the residue ﬁeld of the local ring R. There is an R-algebra
homomorphism ϕ : T −→ k given by

• ϕ(Tq) = 1 + ψψψ(q) for q ∤ ˜np;

• ϕ(Up) = 1 for p | P;
 22

• ϕ(S(a)) = ψψψ(a).

Denote by m ⊂ T the kernel of ϕ. Denote by Tm and ˜Tm = ˜T ⊗T Tm the m-adic
completions of T and ˜T, respectively.
We now describe these Hecke algebras more concretely. Denote by M the set of p-ordinary
cuspidal newforms of weight k, level dividing ˜nP
′ and nebentypus ψ for all characters ψ ∈ Ψ.
For each f ∈ M, denote by fp the ordinary stabilization of f with respect to all primes p | p.
Let E = Ef denote the ﬁnite extension of Qp generated by the Fourier coeﬃcients of f , let
O be the ring of integers of E, and let π be a uniformizer for E. Let

M = {f ∈ M : c(1, (fp)|t) ≡ ϕ(t) (mod π) for all t ∈ T}.

We can state this another way. For each f ∈ M, let Pf denote the prime ideal of T
corresponding to the ordinary p-stabilization fp, i.e. the ideal generated by t − c(1, (fp)|t) for
all t ∈ T. Then M is the set of f ∈ M such that Pf ⊂ m.
For f ∈ M , write K = Frac( ˜Tm) for the total ring of fractions of ˜Tm. Write Kf for the
total ring of fractions of the localization ˜TPf = TPf ⊗T ˜T. Then we have

K = ∏

f ∈M Kf . (33)

We can be explicit about Kf . First note that Frac(TPf ) = E = the ﬁnite extension of Qp
generated by the Fourier coeﬃcients of f . Next we note that Up ∈ Frac(T) for p | P
′, which
results from the discussion of [11, §8.5]. However, the same is not necessarily true in Case 1
for Ul. As we outline below, there are two situations that occur.

• We are in Case 2, or in Case 1 and the newform f has level divisible by l. Then
Kf = E.

• We are in Case 1 and the newform f has level not divisible by l. Then

Kf = E[Ul]/g(Ul) (34)

where g(x) = x
2 − c(f, l)x + ψ(l)Nlk−1

is the Hecke polynomial at l of f . As always there are three possibilities for the
quadratic polynomial g(x): it may be irreducible over E, in which case Kf is a quadratic
ﬁeld extension of E; it may split as a product of distinct linear factors, in which case
Kf ∼= E × E; it may factor as a square, in which case Kf ∼= E[x]/x
2 is the ring of dual
numbers over E (and is in particular not reduced but has a principal maximal ideal).

23

3.2 Cusp form and homomorphism

We now deﬁne the modular forms whose existence yields the desired homomorphism ϕ on
˜Tm. We will work in a weight k > 1 such that k ≡ 1 (mod (p − 1)pN ) for N suﬃciently
large. For now, it will be convenient to ensure that

ǫ
k−1
cyc ≡ 1 (mod Θ#/2n), (35)

where ǫcyc is the p-adic cycotomic character. Therefore we choose a positive integer m large
enough such that Θ#/2 divides pm in R and ensure that N ≥ m, so that ǫ
k−1
cyc ≡ 1 (mod pm).
The integer N will need to be made further suﬃciently large in the results below.
We ﬁrst recall the following theorem of Silliman [24], generalizing an earlier construction
of Hida–Wiles.

Theorem 3.2. Let m be a positive integer. For positive integers k ≡ 0 (mod (p−1)pN ) with
N suﬃciently large, there is a modular form Vk ∈ Mk(1, Zp, 1) such that Vk ≡ 1 (mod pm),
and such that the normalized constant term cA(0, Vk) for each cusp [A] ∈ cusps(1) is con-
gruent to 1 (mod pm).

We next refer the reader to [11, §8.3, Eqn. (102)], where a certain group-ring family of
Eisenstein series Wk(ψψψ, 1) ∈ Mk(n, R, ψψψ) was deﬁned. In the (easier) Case 2, the construction
of [11, Theorem 8.18] works without change for our application. We only remark that the
factor of 2n was ignored in loc. cit. since this factor is a unit for p odd, but we must be
careful about recording this factor now that we are including p = 2.

Theorem 3.3. Suppose we are in Case 2. For an integer k > 1 with k ≡ 1 (mod (p − 1)pN )
and N suﬃciently large, there exists a group ring form Hk(ψψψ) ∈ Mk(n, R, ψψψ) such that

˜Fk(ψψψ) = e
ord
P (W1(ψψψ, 1)Vk−1 − (Θ#/2n)Hk(ψψψ))

lies in Sk(n, R, ψψψ).

In Case 1, we need to modify the construction of [11] to account for the new prime l.

Lemma 3.4. Let the notation be as in Theorem 3.2, with N ≥ m. For any prime l ∤ p, the
form Vk − Vk|l ∈ Mk(l, Zp, 1)

has constant terms divisible by pm at each cusp.

Proof. We freely borrow notation from [10] here. If we are given a cusp A ∈ C∞(l) (see
[10, §3.5]), then by [10, Lemma 3.13] the constant term of Vk|l at A is equal to the constant
term of Vk at the cusp denoted A′ in loc. cit. The result is then immediate since the
normalized constant term of Vk at every cusp is congruent to 1 (mod pm).

24

As we will explain, when A ∈ C0(l), a similar calculation shows that the constant term
of Vk|l at A equals Nl−k times the constant term of Vk at A′. This will give the desired result
since k ≡ 0 (mod pN (p − 1)) and N ≥ m, so Nl−k ≡ 1 (mod pm).
Let A ∈ C0(l). A direct calculation using the deﬁnitions [10, equations (4) and (11)]
reduces the statement above to proving bA′ = bAl−1αµ. We have

bA′ = ααµOF + γ(tµd)−1

= ααµOF + γαµ(tλd)−1l−1

= (αl + γ(tλd)−1)αµl−1. (36)

By deﬁniton of bA, we have OF = αb
−1
A +γ(tλd)−1b
−1
A . Since A ∈ C0(l), the ideal γ(tλd)−1b
−1
A
is coprime to l. Therefore OF = αlb
−1
A + γ(tλd)−1b
−1
A ,

or equivalently, bA = αl + γ(tλd)−1. Substituting into (36) gives the desired result bA′ =
bAl−1αµ.

Theorem 3.5 ([11, Theorem 8.17]). Suppose we are in Case 1. For k > 1 and k ≡ 1
(mod (p − 1)pN ) with N suﬃciently large, there exists a group ring form

˜Fk(ψψψ) = xW1(ψψψ, 1)Vk−1 − Wk(ψψψ, 1) − (xΘ#/2n)Hk(ψψψ)

that lies in Sk(n, R, ψψψ), where x = ΘS∞(1 − k)/ΘS∞(0) ∈ R is a nonzero-divisor.

The modiﬁciation we need in Case 1 to incorporate the prime l is the following.

Corollary 3.6. Suppose we are in Case 1. For k > 1 and k ≡ 1 (mod (p − 1)pN ) with N
suﬃciently large, there exists a group ring form Hk(ψψψl) ∈ Mk(nl, R, ψψψ) such that

˜Fk(ψψψl) = xW1(ψψψl, 1)Vk−1 − Wk(ψψψl, 1) − (xΘ#/2n)Hk(ψψψl)

lies in Sk(nl, R, ψψψ). Here x ∈ R is as above.

Proof. Put ˜Fk(ψψψl) = ˜Fk(ψψψ) − ˜Fk(ψψψ)|l, ˜Hk(ψψψl) = Hk(ψψψ) − Hk(ψψψ)|l. (37)

Then

˜Fk(ψψψl) = xW1(ψψψ, 1)Vk−1 − Wk(ψψψ, 1) − (xΘ#/2n)Hk(ψψψ)−
(xW1(ψψψ, 1)Vk−1 − Wk(ψψψ, 1) − xΘ#Hk(ψψψ))|l
= x
(W1(ψψψ, 1)Vk−1 − W1(ψψψ, 1)|lVk−1|l) − Wk(ψψψl, 1) − (xΘ#/2n) ˜Hk(ψψψl)

= xW1(ψψψl, 1)Vk−1 − Wk(ψψψl, 1) − (xΘ#/2n) ˜Hk(ψψψl) + xW1(ψψψ, 1)|l(Vk−1 − Vk−1|l)

By Lemma 3.4 this form has constant terms divisible by xpm. One can then ﬁnish the proof
as in [11, Theorem 8.17].
 25

Remark 3.7. Here W1(ψψψl, 1) and Wk(ψψψl, 1) are Eisenstein series with ψψψ viewed as having
modulus divisible by the prime l. On the other hand, ˜Fk(ψψψl) and Hk(ψψψl) are just notations,
deﬁned by (37).

Recall that our ring R is associated to a Gal(Qp/Qp)-conjugacy class of characters Φ of
G′ ⊂ G. Let χ ∈ Φ and deﬁne P
′′ = ∏

p|P′,χ(p)̸=1 p.

This is of course independent of the choice of χ ∈ Φ. The proof of Corollaries 8.19 and 8.21
of [11] applies directly to deduce the following from Corollary 3.6.

Corollary 3.8. Suppose we are in Case 1. For k > 1 and k ≡ 1 (mod (p − 1)pN ) with N
suﬃciently large, there exists a cuspidal group ring family Fk(ψψψl) ∈ Sk(nPl, R, ψψψ)p−ord such
that
 Fk(ψψψl) ≡
 {
xW1(ψψψl, 1) − Wk(ψψψl, 1p) (mod xΘ#/2n) if P
′ ̸= P
′′,
W1(ψψψlp, 1) (mod Θ#/2n) if P
′ = P
′′. (38)

In Case 2 there exists a cuspidal group ring family Fk(ψψψ) ∈ Sk(nP
′, R, ψψψ)p−ord such that

Fk(ψψψ) ≡ W1(ψψψPP′′, 1) (mod Θ#/2n).

Lemma 3.1 stated above follows directly from Corollary 3.8 as in [11, Lemma 8.22].

Theorem 3.9. In both Cases 1 and 2, there exists a non-zerodivisor x ∈ R, an R/(xΘ#/2n)-
algebra W , and a surjective R-algebra homomorphism ϕ : ˜Tm −→ W satisfying the following
properties. We have x = 1 unless we are in Case 1 and P
′ ̸= P
′′.

• The structure map R/(xΘ#/2n) −→ W is an injection.

• The restriction of ϕ to Tm takes values in R/(xΘ#/2n) ⊂ W . More precisely,

ϕ(S(a)) = ψψψ(a) for a ∈ G+,

ϕ(Tq) = ǫ
k−1
cyc (q) + ψψψ(q) for q ∤ np, (39)

ϕ(Up) = 1 for p | P. (40)

• In Case 1 we have
 ϕ(Ul) =
 {
ǫ
k−1
cyc (l) if P
′ ̸= P
′′

1 if P = P
′′. (41)

• Let U = ∏

p|P′(Up − ϕ(p)) ∈ ˜Tm.

If y ∈ R and ϕ(U)y = 0 in W , then y ∈ (Θ#/2n).

26

Proof. This result is proved using the forms Fk(ψψψl) and Fk(ψψψ) exactly as in the proof of
[11, Theorem 8.23]. The only extra feature is that in Case 1, we must verify that

Fk(ψψψl)|Ul ≡
 {
Nlk−1Fk(ψψψl) (mod xΘ#/2n) if P
′ ̸= P
′′

Fk(ψψψl) (mod Θ#/2n) if P
′ = P
′′.

This follows directly from (38). (Note that the ﬁrst case uses (35).)

3.3 Galois Representation

It remains now to construct the Galois representation ρ : GF −→ GL2(K). We do this on
each factor of K = ∏

f ∈M Kf in the decomposition (33). To each f (say with nebentypus ψ),
Hida and Wiles [25, Theorems 1 and 2] attach a continuous irreducible Galois representation

ρf : GF −→ GL2(E) (42)

satisfying the following properties:

• ρf is unramiﬁed outside ˜np.

• For all primes q ∤ ˜np, the characteristic polynomial of ρ(Frobq), where Frobq denotes
arithmetic Frobenius, is given by

char(ρf (Frobq))(x) = x
2 − c(q, f )x + ψ(q)ǫ
k−1
cyc (q), (43)

• For all p | p, we have
 ρf |Gp ∼ (
ηp 0
∗ ξp
) (44)

where ηp, ξp : Gp → E∗ are characters with ηp unramiﬁed and satisfying ηp(Frobp) =
c(p, fp). Here Frobp denotes a lifting to Gab
p of the Frobenius element on the maximal
unramiﬁed extension of Fp.

We now deﬁne ˜ρf = ρf ⊗E Kf : GF −→ GL2(Kf ).

We need to show that ˜ρf satisﬁes a statement analogous to (44) for (ρf )|Gl in Case 1. Before
stating this, we need the following lemma which will allow us to reﬁne our choice of l.

Lemma 3.10. Let f be a Hilbert modular newform of weight greater than 1. Then there is
a density one set of primes q of F such that ρf |Gq is not a scalar.

Proof. As the weight of f is greater than 1, the projectivization of ρf has inﬁnite image.
The ˘Cebotarev density theorem gives a density one set of primes of F with non-trivial image
under the projectivization of ρf .
 27

Until now, in Case 1 we have put no assumption on l except that it is coprime to np
and that its Frobenius is the complex conjugation in Gal(H/F ). Using Lemma 3.10 we now
choose l such that it additionally satisﬁes the following condition: for each f ∈ M with level
not divisible by l, we have that ρf |Gl is not scalar. Note that this is not circular, since the
set of f ∈ M with level not divisible by l is a ﬁxed ﬁnite set that is independent of l.

Lemma 3.11. In Case 1 we have
 ˜ρf |Gl ∼ ( ηl 0
∗ ξl
 ) (45)

where ηl, ξl : Gl → E∗ are characters with ηl unramiﬁed and satisfying ηl(Frobl) = Ul.

Proof. If l divides the level of f , then since l2 does not divide the level of f and the nebentypus
ψ is unramiﬁed at l, the desired form (45) follows from a result of Carayol [6]. Indeed, the
local automorphic representation associated to f is an unramiﬁed twist of Steinberg (see [7]
or [17, Proposition 2.8(2)]), and the Galois representation corresponding to this under local
Langlands is described in [6, §6.6].
Now suppose that l does not divide the level of f . Then the representation ρf is unramiﬁed
at l, and equation (43) is satisﬁed for q = l. We must therefore simply show that ρ(Frobl)

is conjugate to a matrix of the form (
Ul 0
∗ ∗
) over GL2(Kf ), where Kf is as in (34). This

follows from the following elementary result in linear algebra.

Lemma 3.12. Let E be a ﬁeld and A ∈ M2(E). Suppose that A has minimal polynomial
g(x) = x
2 − cx + d and let K = E[U]/g(U). Then A is conjugate via GL2(K) to a matrix

of the form (
U 0
∗ ∗
)
.

Proof. Let U ′ = c − U denote the other root in the factorization g(x) = (x − U)(x − U ′) over
K. We must simply show that A has an eigenvector v ∈ K 2 with eigenvalue U ′ such that v
can be completed to a basis of K 2. The rational canonical form shows that A is conjugate

via GL2(E) to ( 0 1
−d c
)
. Let {v1, v2} be the associated basis. Then v = v1 + v2U ′ is the

desired vector.

Remark 3.13. Lemmas 3.11 and 3.12 make it clear why we must insist that ρf (Frobl) is not
scalar in Case 1 when l does not divide the level of f —a scalar matrix is only conjugate to
itself. Interestingly, the situation where ρ(Frobl) has one eigenvalue with multiplicity 2 but
is not scalar is conjectured to never occur. It is curious and somewhat fortuitous that we
can still handle this conjecturally vacuous case via Lemma 3.12, and that we cannot handle
via similar means the case where ρ(Frobl) is scalar (which does occur), but that we can avoid
the scalar case by the ˘Cebotarev argument of Lemma 3.10.

28

We deﬁne ρ by putting the ˜ρf together:

ρ = ∏

f ∈M ˜ρf : GF −→ GL2(K). (46)

By construction, the representation ρ satisﬁes the following properties:

• ρ is unramiﬁed outside ˜np.

• For all primes q ∤ ˜np, the characteristic polynomial of ρ(Frobq) is given by

char(ρ(Frobq))(x) = x
2 − Tqx + ψψψ(q)ǫ
k−1
cyc (q). (47)

• For all primes p | p, and for p = l in Case 1, we have

ρ|Gp ∼ (ηp 0
∗ ξp
) ,

where ηp, ξp : Gp −→ ˜T∗ are characters with ηp unramiﬁed and ηp(Frobp) = Up.

Next we show that ρ satisﬁes all the properties required by Theorem 2.15, as speciﬁed further
in Theorem 2.16. Let P = {p | p, p ̸∈ Σ} and S = Σ ∪ P.

Theorem 3.14. Let χ = ǫ
k−1
cyc . The representation ρ satsiﬁes the following.

1. For σ ∈ GF , the characteristic polynomial Pρ(σ)(x) lies in T[x]. Furthermore we have

Pρ(σ)(x) ≡ (x − χ(σ))(x − ψψψ(σ)) (mod I).

2. Let K0 = red(K) denote the maximal reduced quotient of K. Write K0 = ∏m
i=1 ki as a
product of ﬁelds. For every projection K → K0 → ki, the projection of ρ to GL2(ki) is
an irreducible representation of GF over ki.

3. For each v ∈ Σ, we have ξv ≡ ψψψ|Gv (mod ˜I).

4. For all v ∈ P, we have (ξv)|Iv = χ|Iv.

Proof. We verify the statements in turn.

(1) Since ϕ(Tq) = χ(q) + ψψψ(q) by (39), we have

char(ρ(Frobq))(x) ≡ (x − ǫ
k−1
cyc (Frobq))(x − ψψψ(Frobq)) (mod I)

for all q ∤ ˜np. Since the Frobq are dense in GF by ˘Cebotarev, we have char(ρ(σ))(x) ∈ T[x]
for all σ ∈ GF and
 char(ρ(σ))(x) ≡ (x − ǫ
k−1
cyc (σ))(x − ψψψ(σ)) (mod I).

29

(2) The projections of ρ to the ﬁeld factors of the reduced quotient of K are just the
representations ρf , which are irreducible.

(3) For v ∈ Σ, we have ξv = χψψψη−1
v . We must show that χ|Iv ≡ ηv (mod ˜I). In Case
1, we have Σ = {l}. Then ηl and χ are both unramiﬁed at l. Furthermore ηl(Frobl) = Ul.
If P
′ ̸= P
′′, then Ul ≡ χ(l) (mod ˜I) by (41), so we are done. If P
′ = P
′′ then (41) states
Ul ≡ 1 (mod ˜I). But in this case we have x = 1 so Θ#/2n ∈ ˜I, whence the congruence χ ≡ 1
(mod Θ#/2n) speciﬁed in (35) yields the desired result. In Case 2, we have Σ = {p | P}
and a similar argument holds. We again have x = 1 so χ ≡ 1 (mod ˜I), and (40) shows that
ηp ≡ 1 (mod ˜I) as well.

(4) For v ∈ P, we again have ξv = χψψψη−1
v , which equals χ on Iv since ηv and ψψψ are
unramiﬁed at v.

We conclude this section by noting that in the application of Theorems 2.15 and 2.16 we
choose for p ∈ P the elements σp ∈ Gp to be lifts of Frobp ∈ Gab
p . Then

ξp(σp) − χ(σp) = ǫ
k−1
cyc (σp)(ψψψ(p)U −1
p − 1)

is a unit multiple of (Up − ψψψ(p)). Hence the implication

y ∈ R and ( ∏

v∈P(ξv(σv) − χ(σv)))
y ∈ ˜I =⇒ y ∈ (Θ#/2n)R

required by Theorem 2.16 follows from the last bullet point of Theorem 3.9. This con-
cludes the proof that the Hecke algebras Tm ⊂ ˜Tm, the homomorphism ϕ, and the Galois
representation ρ satisfy the properties used in §2.

4 Construction of Generalized Ritter–Weiss Modules

In the remainder of the paper we construct our generalized Ritter–Weiss modules ∇T
S (H)
and establish the properties stated in §2.1. We will use the language of class formations; for
the beneﬁt of the reader, we recall this terminology in §4.1.

4.1 Class modules and class formations

We recall the basic properties of class modules following [20]. Let G be a ﬁnite group. A
discrete G-module C is a class module if

1. H 1(G, C) = 0,

2. H 2(G, C) is cyclic of order #G.
 30

For class module C, a choice of generator γG ∈ H 2(G, C) is known as a fundamental
class. For any G-module C, an element γ ∈ H 2(G, C) deﬁnes a 2-extension of the form

0 −→ C −→ C(γ) −→ Z[G] −→ Z −→ 0. (48)

Theorem 4.1 (Tate). Let C be a discrete G-module and γ ∈ H 2(G, C). The following are
equivalent:

1. C is a class module with fundamental class γ.

2. C(γ) is G-cohomologically trivial.

3. For all i ∈ Z and all subgroups H ⊂ G, the cup product on Tate cohomology

∪ resG,H(γ) : ̂H i(H, Z) −→ ̂H i+2(H, C)

is an isomorphism.

In particular, if C is a class module for G, cup-product with γ deﬁnes the Nakayama
map: Gab = ̂H −2(G, Z) ∼= ̂H 0(G, C) = C G/NG(C).

The reciprocity map is then deﬁned to be

rec : C G −→ C G/NG(C) ∼= Gab.

Now, consider a proﬁnite group G and a discrete G-module C. The pair (G, C) is called
a class formation if, for all open subgroups H ′ ⊂ H of G with H ′ normal in H, the H/H ′-
module C H ′ is a class module for H/H ′ equipped with a choice of fundamental class γH/H ′.
The fundamental classes are required to satisfy certain compatibilities under inﬂation and
restriction ([20], Deﬁnition 3.1.8). When working with a ﬁxed class formation, we will
abbreviate C(H/H ′) := C(γH/H ′).
For a proﬁnite class formation (G, C) and an open subgroup H of G, there is a reciprocity
map rec : C H −→ H ab, deﬁned as the inverse limit of the reciprocity maps C H −→ (H/H ′)ab

over open normal subgroups H ′ ⊂ H. The reciprocity map induces an isomorphism

rec : ̂(C H)norm ∼= H ab,

where ̂(C H)norm := lim
←−H ′ C H/NH/H ′(C H ′) is the completion in the norm topology on C H.
We will also consider, for any open normal subgroup H ⊂ G, the 2-extension

0 −→ H ab −→ E(G/H) −→ Z[G/H] −→ Z −→ 0 (49)

corresponding to pushing out the 2-extension

0 −→ C H −→ C(G/H) −→ Z[G/H] −→ Z −→ 0

31

along the map C H −→ H ab. The module E(G/H) is topologized using the proﬁnite topology
on H ab and the discrete topology on Z[G/H].
An inclusion of class formations (G′, C ′) −→ (G, C) consists of inclusions G′ ⊂ G,
C ′ ⊂ C, such that for all open subgroups H ′ ⊂ H of G with H ′ normal in H, the image of
γH/H ′ along H 2(H/H ′, C H) −→ H 2((G′ ∩ H)/(G′ ∩ H ′), C H)

equals the image of γG′ along

H 2((G′ ∩ H)/(G′ ∩ H ′), (C ′)(G′∩H ′)) −→ H 2((G′ ∩ H)/(G′ ∩ H ′), C H).

For an open normal subgroup H ⊂ G, let H ′ = G′ ∩ H. The methods of [23, §2 and §4]
deﬁne a map C ′(G′/H ′) −→ C(G/H) such that the following diagram commutes:

(C ′)H ′ C ′(G′/H ′) Z[G′/H ′]

C H C(G/H) Z[G/H].

We obtain a commutative diagram

(H ′)ab E(G′/H ′) Z[G′/H ′]

H ab E(G/H) Z[G/H].

4.2 Class ﬁeld theory

The main results of class ﬁeld theory can be summarized as:

Theorem 4.2. We have

1. For Fv a local ﬁeld, (GFv, ⋃
Hv/Fv H ∗
v ) is a class formation.

2. For F a global ﬁeld, (GF , ⋃

H/F A∗
H/H ∗) is a class formation.

3. There is an inclusion of class formations

(GFv, ⋃

Hv/Fv H ∗
v ) −→ (GF , ⋃

H/F A∗
H/H ∗).

Proof. For (1), (2), see [2]. For (3), see [8, pp. 195–196].

We will also need the following well-known facts about the local and global reciprocity
maps.
 32

Theorem 4.3. 1. For Hw an archimedean local ﬁeld, we have an exact sequence

0 (H ∗
v )◦ H ∗
v Gab
Hv 0,
recv

where (H ∗
v )◦ denotes the connected component of the identity.

2. For Hw a nonarchimedean local ﬁeld, we have an exact sequence

0 H ∗
v Gab
Hv ̂Z/Z 0.
recv

3. For H a global ﬁeld, the following diagram commutes:

∏′
w H ∗
w A∗
H/H ∗

∏′
w Gab
Hw Gab
H .

recw

Let S be a ﬁnite set of places of H containing the archimedean places. Restricting the
local terms from H ∗
w to O∗
w for w ̸∈ S, we have a commutative diagram with exact rows:

∏

w∈S H ∗
w ∏

w̸∈S O∗
w A∗
H/H ∗ ClS(H) 0

∏

w∈S rec(H ∗
w) ∏

w̸∈S rec(O∗
w) Gab
H ClS(H) 0.

recw rec =

Now we ﬁx a ﬁnite Galois extension of number ﬁelds H/F and let G = Gal(H/F ). The
fundamental class γG ∈ H 2(G, A∗
H/H ∗) deﬁnes the global Tate sequence

0 −→ A∗
H/H ∗ −→ V −→ B −→ Z −→ 0, (50)

an exact sequence of Z[G]-modules, where B = Z[G]. For w a place of H with decomposition
group Gw ⊂ G, the fundamental class γGw ∈ H 2(Gw, H ∗
w) deﬁnes the local Tate sequence

0 −→ H ∗
w −→ Vw −→ Bw −→ Z −→ 0, (51)

an exact sequence of Gw-modules, where Bw = Z[Gw].
There is a map from the local Tate sequence to the global Tate sequence:

Vw Bw

V B

33

(see §4.1). This is a diagram of Z[Gw]-modules, giving rise to a diagram of Z[G]-modules

Ind
G
Gw (Vw) IndG
Gw(Bw)

V B,
 (52)

where the induced complex only depends on the place v of F under w.
As in Theorem 4.3, there are compatible reciprocity maps:

H ∗
w Gab
Hw

A∗
H/H ∗ Gab
H .

recw

rec

If we push out the local and global Tate sequences along these reciprocity maps, we obtain
prodiscrete modules Vw,2 and V2 sitting in a commutative diagram

0 Gab
Hw Vw,2 Bw Z 0

0 Gab
H V2 B Z 0,

4.3 The Ritter–Weiss complex

For each place v of F ﬁx a place w | v of H. We will deﬁne, for each place v of F , a complex
of Z[Gw]-modules. Unless mentioned otherwise, all the two term complexes below are in
degree 0 and 1.

4.3.1 Global complex

The global Tate sequence corresponds to the two-term complex

V −→ B, (53)

where B = Z[G]. By Theorems 4.1 and 4.2, V is a cohomologically trivial G-module. Of
course, the same is true for B as well.

4.3.2 Local complexes

Fix ﬁnite disjoint sets of places S, T of F , such that S ∪ T contains all inﬁnite places of F .

Case v ∈ S. The local Tate sequence corresponds to the two-term complex

Vw −→ Bw, (54)

34

where Bw = Z[Gw]. As in the global case, both Vw and Bw are cohomologically trivial
Gw-modules.

Case v ∈ T (ﬁnite). Deﬁne Uw = O∗
w,1 (the 1-units) for w ∈ TH ﬁnite. Consider the
two-term complex Uw −→ 0. (55)

Note that Uw is Gw-cohomologically trivial in case (B), and Uw ⊗Z Z(p) is Gw-cohomologically
trivial in case (Bp) (see [11, Lemma A.4]).

Case v ∈ T (inﬁnite). Deﬁne Uw = Hw for w ∈ TH inﬁnite. Consider the two-term
complex Uw −→ 0. (56)

This maps to Vw −→ Bw (and hence to V −→ B) via Hw exp
−−→ H ∗
w −→ Vw. It is easy to see
that Uw (= R or C) is cohomologically trivial for Gw (= {1} or Z/2Z).

Case v /∈ S ∪ T (ramiﬁed). Consider the module Ww = Vw/O∗
w. Let ∆Gw denote the
augmentation ideal of Z[Gw], and let Iw ⊂ Gw denote the inertia subgroup at w. The norm
N(Iw) = ∑

τ ∈Iw τ deﬁnes a map

N(Iw) : Z[Gw/Iw] −→ Z[Gw].

Let σw ∈ Gw/Iw denote the arithmetic Frobenius. The module Ww is shown in [23, §3] to
have the following description:

Ww ∼= {(x, y) ∈ ∆Gw × Z[Gw/Iw] | x = (1 − σ−1
w )y}. (57)

There are two maps π1, π2 : Ww −→ Z[Gw], given by π1((x, y)) = x and π2((x, y)) = N(Iw)y.
Thus we obtain two maps π1, π2 : Vw −→ Z[Gw]. consider the two-term complex

Vw (π1,π2)
−−−−→ Z[Gw]2. (58)

The terms of this complex are Gw-cohomologically trivial, and it has H 0 = O∗
w and H 1 =
W ∗
w = HomZ(Ww, Z) (see [11] (138)–(139)).

Case v /∈ S ∪ T (unramiﬁed). When Hw/Fv is unramiﬁed, the complex

O∗
w −→ 0 (59)

is quasi-isomorphic to the complex Vw −→ Ww, (60)

and the terms of either complex are Gw-cohomologically trivial (see [11] Lemma A.4).

35

4.4 Construction of the Ritter–Weiss complex

Let S′ be a ﬁnite set of places of F unramiﬁed in H such that S′ is disjoint from S ∪ T . Let

S′′ = S ∪ S′ ∪ {v : v /∈ (S ∪ T ), v ramiﬁed in H}.

We deﬁne
 Vloc := ∏

v∈S′′ IndG
Gw(Vw) × ∏

w∈T IndG
Gw(Uw) × ∏

v /∈(S′′∪T ) Ind
G
Gw (O∗
w),

Bloc := ∏

v∈S Ind
G
Gw (Bw) × ∏

v∈S′ IndG
Gw(Ww) × ∏

w∈(S′′\(S∪S′)) IndG
Gw(Z[Gw]2),

C ∗
loc : Vloc −→ Bloc,

C ∗
global : V −→ B.

Note that C ∗
loc is simply the product, over all places w of H, of the inductions of the local
complexes deﬁned above, each of which comes with a map to C ∗
global (see (52)). The set
S′ determines which of the two quasi-isomorphic complexes to use for unramiﬁed places
v /∈ S ∪ T . Thus we have a map
 θ : C ∗
loc −→ C ∗
global. (61)

We deﬁne the Ritter–Weiss complex:

C ∗
RW,S′ = cone(θ)[−1]. (62)

Lemma 4.4. Up to canonical quasi-isomorphism, C ∗
RW,S′ is independent of the auxiliary set
S′.

Proof. This follows immediately from the fact that the two complexes (59) and (60), which
the set S′ chooses between, are quasi-isomorphic.

The generalized Ritter–Weiss module is deﬁned to be

∇T
S (H) := H 1(C ∗
RW). (63)

Deﬁne the logarithmic (S, T )-units:

U T
S (H) :=
 


(xw, y) ∈ ( ∏

w∈(TH )∞ Hw) × O∗
H,S,T : exp(xw) = σw(y)



 . (64)

Lemma 4.5. The cohomology of C ∗
RW is

H 0(C ∗
RW) = U T
S (H),

H 1(C ∗
RW) = ∇T
S (H),

H 2(C ∗
RW) = coker ( ∏

w∈SH Z × ∏

w /∈(S∪T )
w ramiﬁed
 W ∗
w −→ Z
).

36

If we assume (A), we have H 2(C ∗
RW) =
 {
Z if S = ∅,
0 otherwise.
There is a short exact sequence

0 −→ ClT
S (H) −→ ∇T
S (H) −→ X −→ 0 (65)

where X = ker ( ∏

w∈SH Z × ∏

w /∈(S∪T )
w ramiﬁed
 W ∗
w −→ Z
). (66)

If we assume (A), we have X = XS,H.

Proof. We may assume S′ = ∅. There is an exact triangle

C ∗
loc −→ C ∗
global −→ C ∗
RW.

Computing cohomologies of the ﬁrst two complexes, the associated long exact sequence in
cohomology becomes
 0 H 0(C ∗
RW)

∏

w∈SH H ∗
w × ∏

w∈TH Uw × ∏

w /∈(SH ∪TH )
O∗
w A∗
H/H ∗ H 1(C ∗
RW)

∏

w∈SH Z × ∏

w /∈(S∪T )
w ramiﬁed
 W ∗
w Z H 2(C ∗
RW) 0.

The calculation of H ∗(C ∗
RW) follows, as does the short exact sequence (65). The stated
calculations under the assumption (A) are immediate.

Lemma 4.6. Assume condition (A) holds and that S ̸= ∅. Let K be a subﬁeld of H contain-
ing F . Then ∇T
S (H)Gal(H/K) = ∇T
S (K), where the left side denotes Gal(H/K)-coinvariants.

Proof. First, note that the Ritter–Weiss complex for K is isomorphic to the coinvariants of
the complex for H: C ∗
RW(H)Gal(H/K) = C ∗
RW(K). This follows from Lemma 5.2 applied to
the local and global Tate sequences.
Fix v0 ∈ S. Since IndG
Gv0 (Bw0) −→ B is an isomorphism, we obtain the following presen-
tation of ∇T
S (H):
 ∇T
S (H) ∼= V ⊕ ∏

v∈S\v0 IndG
Gw(Bw)

Vloc . (67)

37

By the right-exactness of coinvariants,

∇T
S (H)Gal(H/K) ∼= (V ⊕ ∏

v∈S\v0 Ind
G
Gw (Bw))Gal(H/K)
(Vloc)Gal(H/K) ∼= ∇T
S (K).

Proposition 4.7. If H/F is a CM extension and S contains a place v such that c ∈ Gv,
then TorZ[G]
1 (X, Z[G]−) = 0, whence

0 −→ ClT
S (H)− −→ ∇T
S (H)− −→ X− −→ 0 (68)

is an exact sequence of Z[G]− modules.

Before we prove this proposition, we need a lemma on TorZ[G]
∗ (·, N) where N = Z[G]−
or Z[G]+. We will suppress the ring Z[G] in our notation.

Lemma 4.8. 1. For i ≥ 1 and any Z[G]-module M, we have

Tori(M, Z[G]+) = Tori+1(M, Z[G]−), Tori(M, Z[G]−) = Tori+1(M, Z[G]+). (69)

2. For every Z[G]-module M, we have

Tor1(M, Z[G]+) = M−[2], Tor1(M, Z[G]−) = M+[2].

Proof. First, notice that there are two short exact sequences of Z[G]-modules

0 Z[G]+ Z[G] Z[G]− 0,
c+1 (70)

and 0 Z[G]− Z[G] Z[G]+ 0,
c−1 (71)

where the inclusion maps are multiplication by c + 1 and c − 1 respectively. To verify that
the ﬁrst of these maps is injective, let x = ∑ αgg ∈ Z[G] and note

x(c + 1) = 0 ⇐⇒ αg + αgc = 0 for all g ∈ G ⇐⇒ x = (c − 1) ∑

g∈G/⟨c⟩ αgg.

Similarly for the second map.
If we apply ⊗Z[G]M to the sequence (70), we obtain a long exact sequence

· · · −→ Tor1(M, Z[G]−) −→ M ⊗ Z[G]+ −→ M ⊗ Z[G] −→ M ⊗ Z[G]− −→ 0. (72)

Since Z[G] is projective and hence ﬂat, we obtain the ﬁrst equality of (69):

Tori(M, Z[G]+) = Tori+1(M, Z[G]−).

38

Similarly, we also obtain the second equality of (69) using (71). This ﬁnishes the proof of
the ﬁrst statement of the lemma.
The long exact sequence (72) together with the the vanishing of Tor1(M, Z[G]), yields

Tor1(M, Z[G]−) = (M+)−.

Notice that c acts trivially on M+, so (M+)− = M+[2]. We calculate Tor1(M, Z[G]+) similarly
from (71).

Proof of Proposition 4.7. Recall from (66) the short exact sequence

0 −→ X −→ Y −→ Z −→ 0

where Y = ∏

w∈SH Z × ∏

w /∈(S∪T )
w ramiﬁed
 W ∗
w. (73)

Applying ⊗Z[G]− to the sequence, we obtain a long exact sequence

−→ Tor2(Y, Z[G]−) −→ Tor2(Z, Z[G]−) −→ Tor1(X, Z[G]−) −→ Tor1(Y, Z[G]−) −→ . (74)

Writing Yv for the local components of Y given in (73), we have

Tor1(Y, Z[G]−) = ⊕v∈Σ Tor1(Yv, Z[G]−) = ⊕v∈Σ(Yv)+[2].

If c ∈ Gv, then c acts trivially on Yv, therefore

(Yv)+[2] = Yv[2] = 0.

If c /∈ Gv, then (Yv)+ = Yv/(c − 1)Yv is still torsion-free, so again (Yv)+[2] = 0. Therefore
Tor1(Y, Z[G]−) = 0. In view of (74), it remains to prove that

Tor2(Y, Z[G]−) −→ Tor2(Z, Z[G]−) (75)

is surjective.
We ﬁrst note that by Lemma 4.8, we have

Tor2(Z, Z[G]−) = Tor1(Z, Z[G]+) = Z/2Z.

Next we compute Tor2(Y, Z[G]−) = ⊕v∈Σ(Yv)−[2] as above. If c ∈ Gv, then c acts trivially
and (Yv)− is just Yv/2Yv. The component of (75) is the surjective map Yv/2Yv −→ Z/2Z
induced by the surjection Yv −→ Z. This concludes the proof. (Incidentally, we note that
the condition c ∈ Gv for some v ∈ S is necessary, since if c /∈ Gv, then (Yv)− is torsion free,
thus (Yv)−[2] = 0.)
 39

4.5 Quadratic presentation

Lemma 4.9. We have

1. V loc −→ V is surjective when ∪v∈S′Gv = G and ClT
S′(H) = 0.

2. Bloc −→ B is surjective when ∪v∈S′Gv = G and S ̸= ∅.

Proof. See [23] Page 162 or [11] §A.1.

Now suppose that S′ is suﬃciently large to satisfy both conditions in Lemma 4.9, and
that S ̸= ∅. Consider V θ −→ Bθ, (76)

where V θ = ker(Vloc −→ V ), Bθ = ker(Bloc −→ B).

This complex is quasi-isomorphic to C ∗
RW.

Corollary 4.10. Suppose that S ̸= ∅, S′ is suﬃciently large to satsify both conditions in
Lemma 4.9, and that condition (C) holds.

1. The Z[G]-modules V θ and Bθ are ﬁnitely generated and projective, and there is an
exact sequence
 0 −→ U T
S (H) −→ V θ −→ Bθ −→ ∇T
S (H) −→ 0.

2. If H/F is a CM extension, the Z[G]−-modules (V θ)− and Bθ
− are ﬁnitely generated
and projective, and there is an exact sequence

0 −→ U T
S (H)− −→ (V θ)− −→ Bθ
− −→ ∇T
S (H)− −→ 0.

Proof. For (1), we note that the modules V θ and Bθ are G-cohomologically trivial, as they
are kernels of surjective maps of G-cohomologically trivial modules. It is clear that Bθ is
torsion-free, and if we assume condition (C), then V θ is as well. Since the modules V θ

and Bθ are ﬁnitely generated, torsion free, and cohomologically trivial, they are projective
Z[G]-modules by a result of Nakayama [19]. Statement (2) follows from the fact that (·)− is
left-exact, (·)− is right-exact, and N − ∼= N− for G-cohomologically trivial Z[G]-modules.

The following two lemmas are an adaptation of the results of [19] to the setting of Z[G]−-
modules. Write G = Gp × G′ where Gp is the p-Sylow subgroup of G and G′ is the subgroup
of prime-to-p order elements of G. In the statement of part (1) below, note that if p ̸= 2
then the composition Zp[Gp] −→ Zp[G] −→ Zp[G]− is injective.

Lemma 4.11. We have:
 40

1. If p ̸= 2, a Zp[G]−-module B is projective if and only if it is projective with respect to
the subring Zp[Gp].

2. If p = 2, a Zp[G]−-module B is projective if and only if it is projective with respect to
the subring Zp[Gp]−.

Proof. (1) p ̸= 2. One direction is clear since Zp[G]− is free as a Zp[Gp]-module. For the
other direction, note that we have an isomorphism of Zp[G]− modules

Zp[G]− ⊗Zp[Gp] B ∼= Zp[G′]− ⊗Zp B, (77)

where

• G acts on the left on the left side

• G acts via G′ on the left factor and Gp on the right factor on the right side.

If B is projective over Zp[Gp], then the left side of (77) is projective over Zp[G]−. The result
now follows as in [19, Prop. 0’], as B is a direct summand as a Zp[G]−-module of the right
side of (77), since the size of G′ is coprime to p.
(2) When p = 2 the proof is the same using the isomorphism

Zp[G]− ⊗Zp[Gp]− B ∼= Zp[G/Gp] ⊗Zp B.

Lemma 4.12. Suppose we have a short exact sequence of Z[G]− modules

0 −→ P −→ Q −→ A −→ 0,

with P and Q projective and A ﬁnitely-generated and Z-torsion free. Then A is a projective
Z[G]−-module.

Proof. It will suﬃce to show that, for all primes p, A ⊗ Zp is a projective Zp[G]− module.
By Lemma 4.11, we may instead show that A ⊗ Zp is a projective Zp[Gp]−-module (when
p = 2) or a projective Zp[Gp]-module (when p ̸= 2).
When p = 2, the ring Z[G2]− ⊗ Z/2Z is isomorphic to (Z/2Z)[G2/⟨c⟩]. Since A is 2-
torsion-free, the sequence 0 −→ P/2P −→ Q/2Q −→ A/2A −→ 0 is exact. The module
P and Q are projective as Z2[G2]−-modules by Lemma 4.11, and so P/2P and Q/2Q are
projective (Z/2Z)[G2/⟨c⟩]-modules. Thus we ﬁnd that A/2A is a cohomologically trivial
G2/⟨c⟩-module, and hence is a free (Z/2Z)[G2/⟨c⟩]-module by [18, pg. 42]. By Nakayama’s
Lemma, a (Z/2Z)[G2/⟨c⟩]-basis of A/2A lifts to Z2[G2]−-generators of A ⊗ Z2. This gives
an exact sequence 0 −→ K −→ ⊕
n
i=1Z2[G2]− −→ A ⊗ Z2 −→ 0.

41

Since A ⊗ Z2 is 2-torsion-free, we may tensor with Z/2Z to conclude that K/2K = 0, and
hence by Nakayama’s Lemma K = 0. Therefore A ⊗ Z2 is a free Z2[G2]−-module.
When p ̸= 2, we can simply apply the results of [19] directly to see that the Gp-
cohomologically trivial, ﬁnitely-generated, p-torsion free module A ⊗ Zp is a free Zp[Gp]-
module.

Proposition 4.13. Suppose that S ̸= ∅, and that conditions (A), (B) or (Bp), and (C) hold.
In case (B):

1. If S contains all the inﬁnite places, then ∇T
S (H) is quadratically presented.

2. If H/F is a CM extension, then ∇T
S (H)− is quadratically presented.

In case (Bp), (1) and (2) hold for ∇T
S (H)⊗ZZ(p) and ∇T
S (H)−⊗ZZ(p) respectively, as modules
over Z(p)[G] and Z(p)[G]−, respectively.

Proof. We give the proof in case (B). The proof in case (Bp) is exactly the same—tensor all
complexes with Z(p), and note that (Uw) ⊗Z Z(p) is cohomologically trivial for all w ∈ TH .
(1) If S contains all inﬁnite places, consider the exact sequence

0 −→ O∗
H,S,T −→ V θ −→ Bθ −→ ∇T
S (H) −→ 0.

Since V θ and Bθ are ﬁnitely generated and projective, to show quadratic presentation
it remains to show that, on each connected component of Spec(Z[G]), V θ and Bθ have
the same rank. Since Z[G] ⊗Z C = ∏

χ C, we must show that dimC(O∗
H,S,T ⊗ C)χ equals
dimC(∇T
S (H) ⊗ C)χ for all χ. This follows from the fact that

O∗
H,S,T ⊗ C ∼= XS,H ⊗ C ∼= ∇T
S (H) ⊗ C.

Note that this ﬁnal isomorphism follows from (65) under condition (A).
(2) Consider the exact sequence of Corollary 4.10 (2):

0 −→ U T
S (H)− −→ (V θ)− −→ (Bθ)− −→ (∇T
S )− −→ 0. (78)

The rank of (V θ)− is larger than that of (Bθ)−, and hence we will need to replace (V θ)− by
a quotient in order to obtain a quadratic presentation.
We have an exact sequence

0 −→ ⊕

v∈TH
complex
 2πiZ −→ U T
S (H) −→ O∗
H,S,T −→ 0.

Taking minus-parts, we get

0 −→ ⊕

v∈TH
complex
 2πiZ −→ U T
S (H)− −→ (O∗
H,S,T )− −→ 0,

42

where right-exactness follows from H 1(⟨c⟩, Z) = 0.
Deﬁne V ′ := (V θ)−/ ⊕

v∈TH
complex
 2πiZ.

We obtain an exact sequence

0 −→ (O∗
H,S,T )− −→ V ′ −→ (Bθ)− −→ ∇T
S (H)− −→ 0. (79)

Note that ⊕

v∈TH
complex
 2πiZ ∼= ⊕

v∈T∞ Z[G]−.

Therefore V ′ is a quotient of projective Z[G]−-modules. Furthermore V ′ is torsion free by
(79) since (O∗
H,S,T )− is torsion free by condition (C). By Lemma 4.12, this implies that V ′ is
itself projective.
Since V ′ and (Bθ)− are projective, to show quadratic presentation for ∇T
S (H)− it remains
to show that, on each connected component of Spec(Z[G]−), V ′ and (Bθ)− have the same
rank. Since Z[G]− ⊗Z C ∼= ∏

χ odd C,

we must show that dimC(O∗
H,S,T ⊗ C)χ equals

dimC(∇T
S (H) ⊗ C)χ = dimC(XS,H ⊗ C)χ

for all odd χ. As O∗
H,S,T ⊗ C ∼= XS∪T∞,H ⊗ C

by Dirichlet’s Unit Theorem, the claim follows from the fact that

K := XS∪T∞,H/XS,H ∼= ⊕w∈TH,∞Z

satisﬁes K ⊗ C[G]− = 0.

Remark 4.14. When H/F is a CM extension and conditions (B) and (C) hold, but not
(A), we still may construct the module V ′ and obtain the exact sequence (79).

43

4.6 ∇T
S (H) and Galois cohomology

In this section, we will assume that condition (A) is satisﬁed. We consider the following
variant of C ∗
RW, using the modiﬁed Tate sequences introduced in §4.2:

Vloc,2 := ∏

v∈S Ind
G
Gw(Vw,2) × ∏

v∈T
v ﬁnite
 IndG
Gw(Uw) × ∏

v /∈(S∪T ) IndG
Gw(O∗
w),

Bloc,2 := ∏

v∈S Ind
G
Gw(Bw),

C ∗
loc,2 : Vloc,2 −→ Bloc,2,

C ∗
global,2 : V2 −→ B,

C ∗
RW,2 := cone(C ∗
loc,2 −→ C ∗
global,2)[−1].

Combining the local and global reciprocity maps, we have a map

rec : C ∗
RW −→ C ∗
RW,2. (80)

Note that we can omit the inﬁnite places in T from Vloc,2 as recw(Uw) = 0 for w ∈ (TH)∞.

Proposition 4.15. The reciprocity map deﬁnes an isomorphism ∇T
S (H) ∼= H 1(C ∗
RW,2).

Proof. We have an exact sequence
∏

w∈SH Gab
Hw × ∏

w∈TH Uw × ∏

w /∈(SH ∪TH )
O∗
w −→ Gab
H −→ H 1(C ∗
RW,2) −→ ∏

w∈SH Z −→ Z

from which we deduce the short exact sequence

0 −→ ClT
S (H) −→ H 1(C ∗
RW,2) −→ X −→ 0

as in (65). Therefore the canonical map ∇T
S (H) = H 1(C ∗
RW) −→ H 1(C ∗
RW,2) is an isomor-
phism.

Proposition 4.15 implies that

∇T
S (H) ∼= ker
 ( V2 ⊕ ∏

v∈S Ind
G
Gw(Bw)
Vloc,2 −→ B
)
 . (81)

Now assume S ̸= ∅, and ﬁx v0 ∈ S. Since Ind
G
Gv0 (Bw0) −→ B is an isomorphism, we
obtain the following presentation of ∇T
S (H):

∇T
S (H) ∼= V2 ⊕ ∏

v∈S\v0 IndG
Gw(Bw)

Vloc,2 . (82)

44

Theorem 4.16. Fix v0 ∈ S, and let A be a prodiscrete G-module. Then Homcts,G(∇T
S (H), A)
may be identiﬁed with the set of tuples (κ, (xv)v∈S\{v0}), where κ : GF −→ A is a 1-cocycle
and xv ∈ A, such that:

1. for v ∈ S \ {v0}, κ(σv) = (σv − 1)xv for all σv ∈ GFv,

2. κ(GFv0 ) = 0,

3. for ﬁnite w ∈ TH , κ|GHw (Uw) = 0, i.e. κ|GHw is tamely ramiﬁed,

4. for w /∈ (SH ∪ TH), κ|GHw (O∗
Hw) = 0, i.e. κ|GHw is unramiﬁed.

The image of the map ∇T
S (H) −→ A corresponding to (κ, (xv)) is generated over Z[G] by
κ(GF ) ∪ {xv | v ∈ S \ {v0}}.

The proof of this theorem relies on a technical result on class formations, Theorem 5.5,
whose proof will be the topic of §5.

Proof. The presentation (82) implies that Homcts,G(∇T
S (H), A) is the kernel of

HomG,cts(V2 ⊕ ∏

v∈S\v0 IndG
Gv(Bw), A) −→

HomG,cts ( ∏

v∈S IndG
Gw(Vw,2) ⊕ ∏

v∈T ﬁnite IndG
Gw(Uw) ⊕ ∏

v /∈(S∪T ) IndG
Gw(O∗
w), A
)
.

By Theorem 5.5, this is the same as the kernel of

Z 1(GF , A) ⊕ ∏

v∈S\v0 C 0(GFv, A) −→ (83)

∏

v∈S Z 1(GFv, A) ⊕ ∏

v∈T ﬁnite HomGw,cts(Uw, A) ⊕ ∏

v /∈(S∪T ) HomGw,cts(O∗
w, A). (84)

As the maps here are the ones arising from restriction and boundary maps in group coho-
mology, we obtain the ﬁrst part of the theorem.
It remains to show the claim regarding the image of ∇T
S (H) −→ A. This image is
generated over Z by the images of f : V2 −→ A

and g : ⊕

v∈S\v0 IndG
Gw(Bw) ∼= ⊕

v∈S\v0 Z[G] −→ A.

The map g sends 1 in the v-component to xv ∈ A. The map f is determined by the
factorization κ : Z[GF ] κuniv−−−→ V2 f
−→ A.

Since κuniv is surjective (see Theorem 5.5), we conclude that the image of ∇T
S (H) −→ A
equals the Z[G]-submodule of A generated by κ(GF ) and the elements xv.

45

Remark 4.17. If we assume that H/F is tamely ramiﬁed at v ∈ T , then condition (3) is
equivalent to κ|GFv being tamely ramiﬁed. If we assume that H/F is p-tamely ramiﬁed at v
and that A is a pro-p group, then condition (3) is equivalent to κ|GFv being tamely ramiﬁed.

Remark 4.18. Condition (4) is equivalent to κ|GFv being unramiﬁed (using the fact that
H/F is unramiﬁed at v /∈ (S ∪ T )).

4.7 Fitting Ideals and Transposes

In this section we establish some elementary properties of the Fitting ideal of ∇S,T (H)− as
certain places are moved in or out of S and T .

Lemma 4.19. With the same hypotheses as Proposition 4.13, let H/F be a CM extension,
and assume S ̸= ∅. For any inﬁnite place v ∈ T , we have

FittZ[G]−(∇T \{v}
S∪{v}(H)−) = 2 FittZ[G]−(∇T
S (H)−).

Proof. Let C ∗
S,T : VS,T −→ BS,T

be the quadratic presentation of ∇T
S (H)− produced in Proposition 4.13. This complex is the
kernel of the map of complexes

θ : (V −
loc/ ⊕

w∈TH,∞ 2πiZ −→ Bloc,−) −→ (V − −→ B−).

The local complex for w ∈ TH,∞ is C−/2πiZ −→ 0. The local complex for w ∈ SH,∞ is
V −
w −→ Bw,−, which has kernel (C∗)− and cokernel Z−. The natural map between these
local complexes, compatible with the global complex, ﬁts into the following diagram:

0 C−/2πiZ C−/2πiZ 0 0 0

0 (C∗)− V −
w (Bw)− Z− 0

The exponential map gives an isomorphism C−/2πiZ ∼= (C∗)−, and so the cokernel of the
map of local complexes, Vw,−/(C∗)− −→ Bw,−, is simply 2Z[Gal(C/R)]− −→ Z[Gal(C/R)]−
as Gal(C/R)-modules.
If we move an inﬁnite place from T to S, we obtain a map between our quadratic presen-
tations: C ∗
S,T −→ C ∗
S∪{v},T \{v}. This map is injective, with cokernel given by the induction
IndG
Gw applied to Vw,−/(C∗)− −→ Bw,−. Therefore the cokernel of C ∗
S,T −→ C ∗
S∪{v},T \{v} is
the complex Ind
G
Gw(2Z[Gw]−) −→ IndG
Gw(Z[Gw]−), i.e. 2Z[G]− −→ Z[G]−, whose Z[G]−-
determinant is 2.
 46

The following lemma is well-known, but since our construction of ∇ is diﬀerent than
what has previously appeared in the literature, we include it for completeness.

Lemma 4.20. With the same hypotheses as Proposition 4.13, let H/F be a CM extension,
and assume S ̸= ∅. Let v be a place of F that is unramiﬁed in H/F , v /∈ S ∪ T .

1. FittZ[G]−(∇T
S∪{v}(H)−) = (1 − σ−1
v ) FittZ[G]−(∇T
S (H)−)

2. FittZ[G]−(∇T ∪{v}
S (H)−) = (1 − σ−1
v N(v)) FittZ[G]−(∇T
S (H)−)

Proof. Let C ∗
S,T : VS,T −→ BS,T

be the quadratic presentation of ∇T
S (H)− produced in Proposition 4.13.
For (1), we assume that v /∈ S′. We consider the map between the relevant local com-
plexes: (Uw −→ 0) −→ (O∗
Hw −→ 0).

We ﬁnd that C ∗
S,T ∪{v} −→ C ∗
S,T has cokernel Ind
G
Gw(F
∗
w) −→ 0, which satisﬁes

Fitt(Ind
G
Gw(F
∗
w)) = (σv − N(v)).

For (2), we assume that v ∈ S′. We consider the map between the relevant local com-
plexes: (Vw −→ W ′
w) −→ (Vw −→ Bw).

We ﬁnd that C ∗
S,T −→ C ∗
S∪{v},T has cokernel 0 −→ IndG
Gw(Z[Gw]/(σv − 1)Z[Gw]), which
satisﬁes Fitt(Ind
G
Gw(Z[Gw]/(σv − 1)Z[Gw])) = (σv − 1).

Lemma 4.21. Suppose S ̸= ∅ and H/F is a CM extension. Assume conditions (B) and
(C), so that we may consider the presentation (7) of ∇T
S (H)−. Let SelT
S (H)− denote the
transpose of ∇T
S (H)− over Z[G]− associated to (7) in the sense of Jannsen, i.e., the module
deﬁned by the exact sequence

HomZ[G]−((Bθ)−, Z[G]−) −→ HomZ[G]−(V ′, Z[G]−) −→ Sel
T
S (H)− −→ 0.

We have a short exact sequence

0 −→ (∇T
S (H)−)∨
tors −→ SelT
S (H)− −→ HomZ((O∗
H,S,T )−, Z) −→ 0. (85)

47

Proof. Split up (7) into two short exact sequences

0 −→ (O∗
H,S,T )− −→ V ′ −→ V ′/(O∗
H,S,T )− −→ 0,

0 −→ V ′/(O∗
H,S,T )− −→ (Bθ)− −→ ∇T
S (H)−.

Note that there is an identiﬁcation of functors on the category of Z[G]−-modules

HomZ[G]−(−, Z[G]−) = HomZ(−, Z).

Applying F (−) = HomZ(−, Z) to the two sequences above, we obtain

0 −→ F (V ′/(O∗
H,S,T )−) −→ F (V ′) −→ F ((O∗
H,S,T )−) −→ 0 (86)

since V ′/(O∗
H,S,T )− ⊂ (Bθ)− is a free Z-module, and

F ((Bθ)−) −→ F (V ′/(O∗
H,S,T )−) −→ Ext1
Z(∇T
S (H)−, Z) −→ 0. (87)

Modding out the ﬁrst two nontrivial terms of (86) by the image of F ((Bθ)−) in each, applying
(87), and noting that Ext1
Z(∇T
S (H)−, Z) ∼= (∇T
S (H)−)∨
tors,

we obtain the desired exact sequence (85).

5 A Duality Theorem for Class Formations

Consider a class formation (G, C) and an open normal subgroup H. In this section we will
prove that, given a prodiscrete Z[G/H]-module A, the complex

HomZ[G/H](Z[G/H], A) −→ HomZ[G/H],cts(E(G/H), A),

dualizing the modiﬁed Tate extension (49), is isomorphic to τ≤1C ∗(G, A), the truncation of
Galois cohomology. This result was used in in the proof of Theorem 4.16 above, which gave
an interpretation of the module ∇T
S (H) in terms of Galois cohomology. Our results in this
section may be of independent interest.

5.1 Duality (G ﬁnite)

Consider a class formation (G, C) with G ﬁnite. Recall the extension (49) obtained by
pushing out the extension (48) along C H −→ C H/NH(C) ∼= H ab:

0 −→ C H/NH(C) −→ E(G/H) −→ Z[G/H] −→ Z −→ 0, (88)

where E(G/H) := C(G/H)/NH(C).
Let C bar
∗ : Z[G] ←− Z[G2] ←− · · ·

be the bar resolution of Z by G-modules. For a discrete G/H-module A,

48

• C ∗(H, A) := HomZ[H](C bar
∗ , A) is a complex of G/H-modules whose cohomology equals
H ∗(H, A) as a G/H-module.

• C ∗(G, A) := HomZ[G](C bar
∗ , A) is a complex whose cohomology equals H ∗(G, A).

We will restrict our attention to the truncation τ≤1C ∗(G, A), i.e.

τ≤1C ∗(G, A) : C 0(G, A) −→ Z 1(G, A). (89)

Theorem 5.1. Consider a class formation (G, C) with G ﬁnite, a normal subgroup H ⊂ G,
and a discrete G/H-module A.

1. The truncation τ≤1C ∗(H, A) is isomorphic to

Hom(Z[G/H], A) −→ Hom(E(G/H), A),

where the map on ﬁrst cohomology equals the dual of the reciprocity map.

2. The truncation τ≤1C ∗(G, A) is isomorphic to

HomZ[G/H](Z[G/H], A) −→ HomZ[G/H](E(G/H), A).

3. The inhomogeneous 1-cocycle Z[G] −→ E(G/H) corresponding to the universal ele-
ment κuniv ∈ Z 1(G, E(G/H)) is surjective.

We begin with some preparatory lemmas.

Lemma 5.2. Consider a class formation (G, C). For H ⊂ G an normal subgroup, we have
C(G)H ∼= C(G/H). In particular, C(G)G ∼= C G. There is a commutative diagram with exact
rows 0 C C(G) Z[G] Z 0

0 C H C(G/H) Z[G/H] Z 0,

where the vertical map on the left term is the norm NH and the map Z[G] −→ Z[G/H] is
the canonical projection.

Proof. Write IG ⊂ Z[G] for the augmentation ideal. Multiplying by the norm NH = ∑

h∈H h
yields a commutative diagram

CH C(G)H (IG)H 0

0 C H C(G)H (IG)H.

NH NH NH (90)

49

Let K(G, H) denote the kernel of NH : (IG)H −→ (IG)H. The snake lemma applied to (90)
yields a map K(G, H) −→ C H/NH(C). (91)

Since C(G) is H-cohomologically trivial, the middle vertical arrow in (90) is an isomorphism,
whence (91) is an isomorphism as well.
Note that (IH)H ∼= H ab is contained in K(G, H). In fact, these are equal: since both
Z[G] and Z[H] are H-cohomologically trivial, we have

̂H −1(H, IG) ∼= ̂H −2(H, Z) ∼= ̂H −1(H, IH).

Therefore the image of the norm map (IG)H −→ (IG)H is isomorphic to

IG/(Z[G]IH) ∼= IG/H.

This proves that C(G)H is an extension

0 −→ C H −→ C(G)H −→ IG/H −→ 0.

It remains to verify that C(G/H) ∼= C(G)H. There is a commutative diagram with exact
rows 0 C C(G) Z[G] Z 0

0 C H C(G)H Z[G]H Z 0

0 C A Z[G]H Z 0.

NH

The map from the ﬁrst row to the second row on the middle two terms is the canonical
projection. The map from the second row to third row is the pushout along the inclusion
C H ⊂ C. The bottom two rows imply that C(G)H −→ Z[G]H , viewed as an element of
Ext2
Z[G/H](Z, C H ), inﬂates to the extension A −→ Z[G]H under the map

Ext2
Z[G/H](Z, C H) −→ Ext2
Z[G](Z, C).

On the other hand, this diagram implies that A −→ Z[G]H is equivalent, as a 2-extension,
to the pushout of the ﬁrst row along the map

C NH−−→ C H ⊂ C.

The map NH : Ext2
Z[G](Z, C) −→ Ext2
Z[G](Z, C)

equals multiplication by |H|, as can be veriﬁed using a dimension-shifting argument, since
NH gives this multiplication on degree 0.
 50

This implies that the 2-extension C(G)H −→ Z[G]H , when inﬂated to an element of
H 2(G, C), equals |H|γG. This is the same as the inﬂation of γG/H. Since inﬂation

H 2(G/H, C H) −→ H 2(G, C)

is an injection, this implies that the 2-extension C(G)H −→ Z[G]H is equivalent, as a 2-
extension of (G/H)-modules, to C(G/H) −→ Z[G/H]. Moreover, this implies that the
1-extension 0 −→ C H −→ C(G)H −→ IG/H −→ 0

is isomorphic to 0 −→ C H −→ C(G/H) −→ IG/H −→ 0,

and hence that C(G)H ∼= C(G/H).

Lemma 5.3. The isomorphisms C(G)G ∼= C G and (IG)G ∼= Gab identify the map

C(G)G −→ (IG)G

with the reciprocity map C G −→ Gab.

Proof. The exact sequence in Tate cohomology associated to the short exact sequence

0 −→ C −→ C(G) −→ IG −→ 0

yields a boundary map δ : ̂H −1(G, IG) ∼= ̂H 0(G, C).

Note that ̂H −1(G, IG) = (IG)G and ̂H 0(G, C) = C G/NG(C). After identifying (IG)G ∼= Gab,
the map δ is by deﬁnition the Nakayama map.
By the construction of boundary maps in Tate cohomology, δ has the following direct
description: take an element of (IG)G, lift it to C(G), apply the norm map to get an element
of C(G)G, observe that it is contained in C G, and project to C G/NG(C).
The reciprocity map is therefore given by

C G ∼= C(G)G C(G)G ։ (IG)G.
∼
N −1
G

The composition of the ﬁrst two maps is the identiﬁcation C G ∼= C(G)G from Lemma 5.2.

We can now prove the duality theorem.

Proof of Theorem 5.1. (1) Since Z and IG/H are Z-free, the sequence (88) remains exact
after applying Hom(−, A). It follows that

Hom(Z[G/H], A) −→ Hom(E(G/H), A) (92)

51

has cohomology
 H 0 = Hom(Z, A) = H 0(H, A),

H 1 = Hom(C H/NH(C), A) = Hom(H ab, A) = H 1(H, A),

where the last equalities on each line hold since A has trivial H-action. Therefore the
complex (92) has the same cohomology as τ≤1C ∗(H, A), and our goal is to show that these
two complexes are in fact quasi-isomorphic as complexes of Z[G/H]-modules.
Using the lifting property for projective Z[G]-modules, we may choose a commutative
diagram Z[G3] Z[G2] Z[G]

C C(G) Z[G]

=

Applying HomZ[H](·, A) to the ﬁrst complex gives the ﬁrst few terms of the complex
C ∗(H, A). We obtain a map of chain complexes of Z[G/H]-modules:

τ≤1 HomZ[H](C −→ C(G) −→ Z[G], A) −→ τ≤1C ∗(H, A).

By Lemma 5.2, this becomes:

τ≤1 Hom(CH −→ C(G/H) −→ Z[G/H], A) −→ τ≤1C ∗(H, A).

The map CH −→ C(G/H) factors as CH NH−−→ C H ⊂ C(G/H). Therefore we obtain a map
of complexes: Hom(E(G/H) −→ Z[G/H], A) −→ τ≤1C ∗(H, A).

It remains to check that the induced map on H 1, Hom(C H/NH(C), A) −→ H 1(H, A),
is dual to the reciprocity map, and hence is an isomorphism. We can reduce to the case
G = H, using the map

(C −→ C(H) −→ Z[H]) −→ (C −→ C(G) −→ Z[G])

considered as complexes of Z[H]-modules.
The partial resolution 0 −→ IH −→ Z[H] −→ Z −→ 0 of Z induces a map

H 1(H, A) −→ HomZ[H](IH, A) = HomZ[H](IH, A) = Hom(H ab, A)

which is the usual isomorphism. This partial resolution can be extended to C(H) −→
Z[H] −→ Z −→ 0, inducing a map

H 1(H, A) ∼= HomZ[H](IH , A) −→ HomZ[H](C(H), A).

52

By Lemma 5.3, the second map is dual to the reciprocity map.
(2) The argument of (1) implies that τ≤1C ∗(G, A) is isomorphic to

τ≤1 HomZ[G](C −→ C(G) −→ Z[G], A).

Using Lemma 5.2, we ﬁnd that the following sequence is exact:

0 −→ Hom(E(G/H), A) −→ HomZ[H](C(G), A) −→ HomZ[H](C, A).

Hence, by left-exactness of H 0(G/H, ·), the following sequence is exact as well:

0 −→ HomZ[G/H](E(G/H), A) −→ HomZ[G](C(G), A) −→ HomZ[G](C, A).

Therefore τ≤1 HomZ[G](C −→ C(G) −→ Z[G], A) is isomorphic to

HomZ[G](E(G/H) −→ Z[G], A).

(3) The inhomogeneous 1-cocycle κuniv : G −→ E(G/H) in Z 1(G, E(G/H)) corresponds
to the homogeneous 1-cocycle Z[G2] −→ E(G/H) occuring in:

Z[G3] Z[G2] Z[G]

H ab E(G/H) Z[G/H]

Since we have an exact sequence

0 −→ H ab −→ E(G/H) −→ IG/H −→ 0,

we must show that f : Z[G2] −→ IG/H is surjective, and that ker(f ) surjects onto H ab.
The map Z[G2] −→ IG −→ Z[G/H]

has image equal to IG/H. The H-submodule Z[H 2] ⊂ Z[G2] is contained in ker(f ). The
restriction of Z[G2] −→ E(G/H) to Z[H 2] is a homogeneous 1-cocycle Z[H 2] −→ E(G/H)
whose image is H ab, corresponding to

id ∈ Hom(H ab, H ab) = H 1(H, H ab).

The result follows.
 53

5.2 Functoriality

Lemma 5.4 (Functoriality). Suppose we have a map of class formations (G′, C ′) −→ (G, C).
Let H be a subgroup of G, and let H ′ = G′ ∩ H. Let A be a Z[G/H]-module. The restriction
map Z 1(G, A) −→ Z 1(G′, A)

is dual to E(G′/H ′) −→ E(G/H).

Proof. The argument of Theorem 5.1 proves that the complex

0 −→ H ab −→ Z[G2]H/Z[G3]H −→ Z[G/H] −→ Z −→ 0

is isomorphic to
 0 −→ C H/NH(C) −→ E(G/H) −→ Z[G/H] −→ Z −→ 0.

Since we have a commutative diagram

(H ′)ab (C ′)H ′/NH ′(C ′)

H ab C H/NH(C),

we obtain a commutative diagram

Z[(G′)2]H ′/Z[(G′)3]H ′ E(G′/H ′)

Z[G2]H/Z[G3]H E(G/H).

Applying HomZ[G′/H ′](·, A) to the ﬁrst row and HomZ[G/H](·, A) to the second, we obtain
the required compatibility.

5.3 Duality theorem (G proﬁnite)

Recall that a prodiscrete group is an inverse limit of discrete groups with surjective transition
maps. Note that, for a class formation (G, C), the Z[G/H]-module E(G/H) is prodiscrete.

Theorem 5.5. Let (G, C) be a class formation and let H be an open normal subgroup of G.
For any prodiscrete Z[G/H]-module A:

1. The complex τ≤1C ∗(H, A) is isomorphic to

Hom(Z[G/H], A) −→ Homcts(E(G/H), A).

54

2. The complex τ≤1C ∗(G, A) is isomorphic to

HomZ[G/H](Z[G/H], A) −→ HomZ[G/H],cts(E(G/H), A).

3. The inhomogeneous 1-cocycle Z[G] −→ E(G/H) corresponding to the universal ele-
ment κuniv ∈ Z 1(G, E(G/H)) is surjective.

Proof. (1) We may assume that A is discrete, since

lim
←−
n Homcts(E(G/H), A/An) ∼= Homcts(E(G/H), lim
←−
n A/An) = Homcts(E(G/H), A)

and lim
←−
n Z 1(H, A/An) ∼= Z 1(H, lim
←−
n A/An) ∼= Z 1(H, A).

Since A is discrete, Z 1(H, A) = lim
−→H ′ Z 1(H/H ′, A) and

Homcts(E(G/H), A) = lim
−→
H ′ Hom(E((G/H ′)/(H/H ′)), A).

As E((G/H ′)/(H/H ′)) comes from the ﬁnite class formation (G/H ′, C H ′), we may apply
Theorem 5.1 to deduce that Hom(E((G/H ′)/(H/H ′)), A) ∼= Z 1(H/H ′, A).
(2) and (3) follow from Theorem 5.1 via a similar argument.

Suppose we have a map of class formations (G′, C ′) −→ (G, C). Let H be an open
subgroup of G, and let H ′ = G′ ∩ H.

Lemma 5.6 (Functoriality). For any prodiscrete Z[G/H]-module A, the map

Z 1(H, A) −→ Z 1(H ′, A)

is the continuous dual Homcts(·, A) of the map E(G′/H ′) −→ E(G/H).

Proof. This follows from the analogous result in the ﬁnite case, Lemma 5.4.

References

[1] Mahiro Atsuta and Takenori Kataoka. On the minus component of the equivariant Tamagawa number
conjecture for Gm. 2021. https://arxiv.org/abs/2112.04783.

[2] Emil Artin and John Tate. Class ﬁeld theory. W. A. Benjamin, Inc., New York-Amsterdam, 1968.

[3] David Buchsbaum. A generalized Koszul complex. I. Trans. Amer. Math. Soc. 111:183–196, 1964.

[4] David Buchsbaum and Dock S. Rim. A generalized Koszul complex. Bull. Amer. Math. Soc. 69:382–
385, 1963.

[5] David Burns, Masato Kurihara, and Takamichi Sano. On Iwasawa theory, zeta elements for Gm, and
the equivariant Tamagawa number conjecture. Algebra and Number Theory 11 (7):1527–1571, 2017.

55

[6] Henri Carayol. Sur les repr´esentations l-adiques associ´ees aux formes modulaires de Hilbert. Ann.
Sci. ´Ecole Norm. Sup. (4) 19 (3):409–468, 1986.

[7] William Casselman. On some results of Atkin and Lehner. Math. Ann. 201:301–314, 1973.

[8] J. W. S. Cassels and A. Fr¨ohlich, editors. Algebraic number theory. Academic Press, London; Thomp-
son Book Co., Inc., Washington, D.C., 1967.

[9] Corrado De Concini and Claudio Procesi. The invariant theory of matrices. University Lecture Series,
vol. 69. American Mathematical Society, Providence, RI, 2017.

[10] Samit Dasgupta and Mahesh Kakde. On constant terms of Eisenstein series. Acta Arithmetica
200:119–147, 2021.

[11] . On the Brumer-Stark conjecture. Ann. of Math. (2) 197 (1):289–388, 2023.

[12] Samit Dasgupta, Mahesh Kakde, Jesse Silliman, and Jiuya Wang. The Residually Indistinguishable
Case of Ribet’s Method for GL2.

[13] Eric M. Friedlander and Brian J. Parshall. Cohomology of Lie algebras and algebraic groups. Amer.
J. Math. 108 (1):235–253 (1986), 1986.

[14] Edward Cline, Brian J. Parshall, Leonard Scott, and Wilberd van der Kallen. Rational and generic
cohomology. Invent. Math. 39 (2):143–163, 1977.

[15] Pierre Deligne and Kenneth A. Ribet. Values of abelian L-functions at negative integers over totally
real ﬁelds. Invent. Math. 59 (3):227–286, 1980.

[16] Jens Carsten Jantzen. Representations of algebraic groups. Mathematical Surveys and Monographs,
vol. 107. American Mathematical Society, Providence, RI, 2nd ed., 2003.

[17] David Loeﬄer and Jared Weinstein. On the computation of local components of a newform. Math.
Comp. 81 (278):1179–1200, 2012.

[18] Tadasi Nakayama. On modules of trivial cohomology over a ﬁnite group. Illinois J. Math. 1:36–43,
1957.

[19] . On modules of trivial cohomology over a ﬁnite group. II. Finitely generated modules. Nagoya
Math. J. 12:171–176, 1957.

[20] J¨urgen Neukirch, Alexander Schmidt, and Kay Wingberg. Cohomology of number ﬁelds. Grundlehren
der mathematischen Wissenschaften [Fundamental Principles of Mathematical Sciences], vol. 323.
Springer-Verlag, Berlin, 2000.

[21] Amit Ophir and Ariel Weiss. On Ribet’s Lemma for GL2 modulo prime powers. 2021.
https://arxiv.org/abs/2111.01559.

[22] Alison E. Parker. On the good ﬁltration dimension of Weyl modules for a linear algebraic group. J.
Reine Angew. Math. 562:5–21, 2003.

[23] J¨urgen Ritter and Alfred Weiss. A Tate sequence for global units. Compositio Math. 102 (2):147–178,
1996.

[24] Jesse Silliman. Group Ring Valued Hilbert Modular Forms. 2020.
https://arxiv.org/abs/2111.01559.

[25] A. Wiles. On ordinary λ-adic representations associated to modular forms. Invent. Math. 94 (3):529–
573, 1988.
 56
