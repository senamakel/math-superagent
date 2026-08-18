<!-- source: https://repositori.urv.cat/repositori/getDocument/imarina%3A6466319?ds=DocumentPrincipal&mime=application/pdf | converted from PDF -->

Asymptotic expansion of the Dulac map and time
for unfoldings of hyperbolic saddles: local setting

D. Marín and J. Villadelprat

BGSMath and Departament de Matemàtiques, Facultat de Ciències,
Universitat Autònoma de Barcelona, 08193 Bellaterra, Barcelona, Spain

Departament d’Enginyeria Informàtica i Matemàtiques, ETSE,
Universitat Rovira i Virgili, 43007 Tarragona, Spain

Abstract. In this paper we study unfoldings of planar vector ﬁelds in a neighbourhood of a hyperbolic
resonant saddle. We give a structure theorem for the asymptotic expansion of the local Dulac time (as
well as the local Dulac map) with the remainder uniformly ﬂat with respect to the unfolding parameters.
Here local means close enough to the saddle in order that the normalizing coordinates provided by a
suitable normal form can be used. The principal part of the asymptotic expansion is given in a monomial
scale containing a deformation of the logarithm, the so-called Roussarie-Ecalle compensator. Especial
attention is paid to the remainder’s properties concerning the derivation with respect to the unfolding
parameters.

Contents

1 Introduction and statements of the results 1

2 Further results on Roussarie’s series expansion 7

3 Dulac map 16

4 Dulac time 19

A Results about the class F K
L (W ) 25

B Diﬀerentiation formulas and integration of series 32

1 Introduction and statements of the results

In this paper we study unfoldings of planar vector ﬁelds in a neighbourhood of a hyperbolic resonant saddle.
It can be viewed as the continuation of a previous paper where we give a C K normal form for the unfolding
with respect to the conjugacy relation, see [10, Theorem A]. By means of this normal form in that paper

2010 AMS Subject Classiﬁcation: 34C07; 34C20; 34C23.
Key words and phrases: Dulac map, Dulac time, asymptotic expansion, uniform ﬂatness.
This work has been partially funded by the Ministry of Science, Innovation and Universities of Spain through the grants
MTM2015-66165-P and MTM2017-86795-C3-2-P, the Agency for Management of University and Research Grants of Catalonia
through the grants 2017SGR1725 and 2017SGR1617, and by the “María de Maeztu” Programme for Units of Excellence in
R&D (MDM-2014-0445).
 1

Σ1

Σ′
1 Σ′
2 Σ2

1
 1
φ

D0

P1
 P2

Figure 1: Auxiliary transverse sections in the decomposition of the Dulac map D = P2 ◦ D0 ◦ P1
and the Dulac time T = T1 + T0 ◦ P1 + T2 ◦ D0 ◦ P1, where P1 (respectively, P2) is the Poincaré
map from Σ1 to Σ′
1 (respectively, Σ2 to Σ′
2) and T1 (respectively T2) is the time that spends
the ﬂow to do this transition. Here the local Dulac map is D0 and the local Dulac time is T0.

we also determine an asymptotic expansion, uniform with respect to the parameters, for the local Dulac
time of a resonant saddle, see [10, Theorem B]. The Dulac map of a saddle is the transition map from a
transverse section Σ1 at the stable separatrix to a transverse section Σ2 at the unstable separatrix, whereas
the Dulac time is the time that spends the ﬂow to do this transition, see Figure 1. By local we mean that
Σ1 and Σ2 cannot be at arbitrary distance from the saddle but close enough in order that we can use the
normalizing coordinates provided by the normal form. In other words, and more precisely, the local Dulac
map (respectively, local Dulac time) is the Dulac map (respectively, Dulac time) of the normal form.

The asymptotic expansion of the Dulac map (see [15, Chapter 5] and references therein) is a key tool to
study the cyclicity of a polycycle Γ (i.e., the maximum number of limit cycles that bifurcate from Γ) and
to this end the remainder in the asymptotic expansion must be uniformly ﬂat. In this respect recall that
the second part of Hilbert’s 16th problem asks for the maximum number of limit cycles, called H(n), of a
polynomial vector ﬁeld P (x, y)∂x + Q(x, y)∂y as a function of n = max(deg(P ), deg(Q)). It is still unknown
whether H(n) is ﬁnite. In case that the return map of the polycycle is the identity then there is an annulus
foliated by periodic orbits where the period function (i.e., the time of the return map) is deﬁned. In this
context the object of study are the so-called critical periodic orbits, which are the critical points of the
period function. Similarly as with Hilbert’s 16th problem, it arises the notion of criticality of a polycycle Γ,
i.e., the maximum number of critical periodic orbits that bifurcate from Γ, see [7, 9]. In the same way as
for the cyclicity, an asymptotic expansion of the Dulac time with remainder uniformly ﬂat constitutes a
key tool to study the criticality of a polycycle. Both asymptotic expansions are of similar nature, they are
given in a monomial scale containing the so-called Roussarie-Ecalle compensator, which is deformation of
the logarithm.

The asymptotic expansion of the local Dulac map (respectively, time) is a basic building block for
establishing an asymptotic expansion of the Dulac map (respectively, time) and, in its turn, the latter is
essential to study the cyclicity (respectively, criticality) of polycycles. In the present paper we focus on
the local setting. Our main result for the local Dulac time is an asymptotic expansion that improves the
one we previously obtained, see [10, Theorem B], in two aspects. Firstly because it gives a more precise
description of the monomials appearing in the principal part. And secondly, more important, it shows that
the remainder can be smoothly extended also with respect to the unfolding parameters. This was in fact
our initial motivation to tackle the problem. In order to state our main theorems some results concerning

2

normal forms are needed.
Let V be an open subset of RN and consider a C ∞ unfolding {Xµ}µ∈V of a hyperbolic saddle point at
the origin. More precisely, Xµ = A(x, y; µ)x∂x + B(x, y; µ)y∂y,

where A, B ∈ C ∞(U × V ), for some neighbourhood U of (0, 0) ∈ R2, with A(0, 0; µ) > 0 and B(0, 0; µ) < 0
for all µ ∈ V. The hyperbolicity ratio of the saddle is

λ = λ(µ) = − B(0, 0; µ)
A(0, 0; µ) .

Given m, n ∈ Z we also consider the collinear family

Yµ = 1
xmyn Xµ.

The reason why we permit this “polar” factor is because, when dealing with polynomial vector ﬁelds, a
special attention must be paid to the study of those polycycles with vertices at inﬁnity in the Poincaré disc.
The factor can come from the line at inﬁnity in a saddle at inﬁnity or, more generally, appear in a divisor
after desingularizing more general singular points at inﬁnity of a polycycle. The case of lines of zeros in at
least one of the separatrices is also allowed as it can appear after desingularizing a degenerate singular point
at ﬁnite distance. It is important to remark that (by means of a reparametrization of time) this factor can
be neglected to study the Dulac map but, on the contrary, this cannot be done when dealing with the Dulac
time. For the same reason, to study the Dulac time we need normal forms with respect to the conjugacy
relation rather than the equivalence relation.
We recall at this point Theorem A in [10], which generalizes well-known orbital normal forms with
respect to the equivalence relation (see [6, 15] and references therein). To this end let us ﬁx µ0 ∈ V and
denote λ0 = λ(µ0) for shortness. If λ0 ∈ Q, say λ0 = p/q with (p, q) = 1, then that result shows that for
any k ∈ N the family {Yµ}µ∈V is C k conjugated, by means of a diﬀeomorphism Φ(x, y, µ) = (φ(x, y, µ), µ)
deﬁned in a neighbourhood of (0, 0, µ0) ∈ R2 × V , to the normal form

Y N F
µ = 1
η(µ)xmyn + uℓQ(u; µ)
 (x∂x + ( − λ(µ) + P (u; µ)
)y∂y),

where η is a C ∞ function, P and Q are polynomials in the resonant monomial u = xpyq with the coeﬃcients
being also C ∞ functions in µ, and

ℓ :=
 



 ⌈
max ( m
p , n
q )⌉ if mq − np ̸= 0,
⌈
max ( m
p , n
q )⌉ + 1 if mq − np = 0. (1)

Finally, if λ0 /∈ Q then the result shows that we can take P = Q = 0. (In this paper we use the common
notation ⌊ · ⌋ and ⌈ · ⌉ for the ﬂoor and ceiling functions respectively.)

As we already explained, our aim in this paper is to study the Dulac time (as well as the Dulac map)
associated to Y N F
µ . (Note in this respect that the only interesting case is the resonant one, i.e., λ0 ∈ Q,
because otherwise both maps can be computed explicitly.) More generally, we consider the polynomial
normal family
 Yα,β := 1

β0xmyn + uℓ ∑M
i=1 βiui−1 Xα (2)

where
 Xα := x∂x + 1
q (−p + ∑N −1
i=0 αi+1u
i) y∂y. (3)

3

In this way, setting α = (α1, . . . , αN ) ∈ RN and β = (β0, . . . , βM ) ∈ RM +1, we thus consider the coeﬃcients
of the polynomials P ( · ; µ) and Q( · ; µ) in the normal form Y N F
µ as independent parameters. Naturally we
work with α1 ≈ 0 because
 λ = λ(α1) := p − α1
q .

Note also that, with regard to the Dulac map, we can ignore the time and take Xα instead of Yα,β. That
being said, we denote the Dulac map between (0, 1) × {1} and {1} × (0, 1) by D( · ; α). Similarly, the Dulac
time between the same sections is denoted by T ( · ; α, β). More explicitly, let ϕ(t; s, α) be the solution of Xα
passing through (s, 1) ∈ R2 with s > 0 at t = 0. Then, since this solution reaches {y = 1} at time t = − ln s
due to ϕ1(t; s, α) = se
t, it turns out that D(s; α) = ϕ2(− ln s; s, α). Likewise, if φ(t; s, α, β) is the solution
of Yα,β passing through (s, 1) ∈ R2 with s > 0 then the Dulac time is the function T ( · ; α, β) verifying

φ1(t; s, α, β)|t=T (s;α,β) = 1 for all s > 0 small enough.

The present paper has two main results, namely: Theorem A, devoted to the Dulac map D(s; α), and
Theorem B, addressed to the Dulac time T (s; α, β). The idea behind the proof, and also the aim of the
result, is the same for both theorems. We show ﬁrstly that we can write the function as an inﬁnite series
for s > 0 and α1 small enough. Secondly, that we can truncate this series in order that the tail is uniformly
ﬂat at s = 0. And, thirdly, that the ﬁnite truncation can be expressed in terms of a polynomial in s
p and
s
pω(s; α1), where ω is a deformation of the logarithm (see Deﬁnition 1.3), the so-called Ecalle-Roussarie
compensator.

In this paper we use a more general notion of ﬂatness (see Deﬁnition 1.2), which constitutes the key
point in our approach as well as the main motivation to tackle the problem. Let us advance that it has
better properties with respect to parameters and that this enables us to elucidate a delicate point which we
think did not received the required attention in the literature (see Remark 1.4).

Deﬁnition 1.1. Consider K ∈ Z≥0 ∪ {+∞} and an open subset U of RN . We say that a function ψ(s; µ)
belongs to the class C K
s>0(U ), respectively C K
s=0(U ), if there exist an open neighbourhood Ω of

{(s, µ) ∈ RN +1; s = 0, µ ∈ U } = {0} × U

in RN +1 such that (s, µ) ↦→ ψ(s; µ) is C K on Ω ∩ ((0, +∞) × U ), respectively Ω. □

More formally, the deﬁnition of C K
s>0(U ) and C K
s=0(U ) must be thought in terms of germs with respect
to relative neighborhoods of {0} × U in (0, +∞) × U . In doing so these sets become rings and we have the
inclusions C K(U ) ⊂ C K
s=0(U ) ⊂ C K
s>0(U ). These facts are implicitly used in Lemma A.3.

We can now introduce the notion of (ﬁnitely) ﬂatness that we shall use in the sequel.

Deﬁnition 1.2. Consider K ∈ Z≥0 ∪ {+∞} and an open subset U of RN . Given some L ∈ R and ˆµ ∈ U ,
we say that ψ(s; µ) ∈ C K
s>0(U ) is (L, K)-ﬂat with respect to s at ˆµ, and we write ψ ∈ F K
L (ˆµ), if for each
ν = (ν0, . . . , νN ) ∈ Z
N +1
≥0 with |ν| = ν0 + · · · + νN ⩽ K there exist a neighbourhood V of ˆµ and C, s0 > 0
such that ∣
∣
∣
∣ ∂|ν|ψ(s; µ)
∂sν0 ∂µ
ν1
1 · · · ∂µ
νN
N
 ∣
∣
∣
∣ ⩽ Cs
L−ν0 for all s ∈ (0, s0) and µ ∈ V . (4)

If W is a (not necessarily open) subset of U then deﬁne F K
L (W ) := ⋂
ˆµ∈W F K
L (ˆµ). □

The class F K
L (W ) consists in those functions ψ(s; µ) that are (ﬁnitely) ﬂat along {0} × W. The usual
notion of (ﬁnitely) ﬂatness is addressed to functions ψ that are smooth at s = 0 and not depending on
parameters. In that context one simply requires the s derivatives of ψ to vanish at s = 0 up to order K − 1.
When dealing with functions that are not smooth at s = 0, the natural and common deﬁnition is to require

4

the estimates in (4). In this non-smooth context, and when the function depends on parameters, one can
alternatively require (4) to hold for all µ ∈ V but only for derivation with respect to s. This is precisely
the notion of ﬂatness used in [14, 15] for the remainder of the asymptotic expansion of the Dulac map (cf.
Remark 1.4). For instance the function (s, µ) ↦→ s
µ is obviously L-ﬂat at any ˆµ > L according to this
alternative notion whereas to show that (s, µ) ↦→ s
µ belongs to F ∞
L ({µ > L}) requires some computations
(see Lemma A.4). Coming again to Deﬁnition 1.2, note that the case L < K is not excluded (and so it may
occur that L − ν0 is negative) and that the case L = K corresponds to the usal notion of (ﬁnitely) ﬂatness.

The principal part of D( · ; α) and T ( · ; α, β) will be expressed in terms of the following deformation of
the logarithm.

Deﬁnition 1.3. The function deﬁned for s > 0 and κ ∈ R by means of

ω(s; κ) =
 { s
−κ−1
κ if κ ̸= 0,
− ln s if κ = 0,

is called the Ecalle-Roussarie compensator. □

Lemma A.4 gives several properties of the Ecalle-Roussarie compensator in relation with the class F K
L (W )
as introduced in Deﬁnition 1.2. It shows in particular that (s, κ) ↦→ ω(s; κ) belongs to F ∞
−ε({κ < ε}) for all
ε > 0. With regard to the parameter space of the family of vector ﬁelds in (3), hereafter we denote

U0 := {α ∈ RN ; α1 = 0} = {0} × RN −1.

We can now state our two main results. In both statements we set ω = ω(s; α1) and λ = λ(α1) for the sake
of shortness. The ﬁrst one is a structure theorem for the asymptotic expansion of the local Dulac map.

Theorem A. Let D( · ; α) be the Dulac map of the vector ﬁeld Xα in (3) between the sections (0, 1) × {1}
and {1} × (0, 1). Then for each L ∈ R there exists a unique ∆(z, w; α) ∈ Q[z, w, α], with deg(z,w) ∆ ⩽ L
p − 1
q ,
and DL ∈ F ∞
L (U0) such that D(s; α) = s
λ∆(s
p, s
pω; α) + DL(s; α).

Moreover, ∆(0, 0; α) = 1 in case that L ⩾ p
q and ∆ ≡ 0 otherwise.

This result has strong connections with the seminal works on the structure of the local Dulac map by
A. Mourtada and R. Roussarie. Indeed, we write the principal part along the same lines as Mourtada, see
[13, Proposition 2], in the sense that it is the Dulac map of the linear vector ﬁeld x∂x − λy∂y, i.e., s ↦→ s
λ,
multiplied by a unity (that we show is polynomial in s
p and s
pω). Roussarie (see [14, Theorem F] or [15,
Chapter 5]) writes the principal part in a diﬀerent way and it is diﬃcult to compare since he considers the
case p = q = 1 only, which does not ﬁt very well for q ̸= 1. Next we make some further comments about it.

Remark 1.4. The proof of Theorem A (and also the forthcoming Theorem B) relies on some previous
results by R. Roussarie in [14] (see also [15, Chapter 5]) that we gather in Lemma 2.1 and constitute our
starting point. In that paper the author studies the cyclicity of a saddle loop and to this aim he proves
Theorem F, which describes the structure of the local Dulac map D(s; α). That result is very similar to our
Theorem A, but important diﬀerences exist. Firstly his result is addressed to the case p = q = 1 because at
that time it was already well-known that the cyclicity of a saddle loop with λ0 ̸= 1 is at most one. Secondly
his result is more precise in the description of the principal part, i.e., D − DL, since he divides it in the
ideal generated by the coeﬃcients α1, α2, . . . , αN . And, thirdly, his proof concerning the remainder consists
in showing that it veriﬁes ∣
∣∂k
s DL(s; α)
∣
∣ ⩽ Cs
L−k.

This kind of estimate, similar to (4) but without derivation with respect to parameters, behaves well through
the so-called derivation-division algorithm that yields to the main result in [14] on the cyclicity of the saddle

5

loop (which in our opinion is perfectly right and, what is more, correctly proved). However it does not enable
to assert that DL extends to a C L function in (s, α) at s = 0 (see Example A.2 for a counterexample).
Sadly enough, this is precisely what the author states in Theorem F with regard to the remainder DL (see
also Theorem 14 in [15, page 103]). This inexactness yields to a crucial gap in a subsequent paper by the
same author [16]. Indeed, in that paper he studies the smoothness property of the bifurcation diagram of a
generic saddle loop unfolding of codimension 2, and to prove the main result he appeals to this (unproved)
claim in Theorem F. To be more precise, by taking advantage of the smoothness with respect to parameters
of the remainder, he is able to apply an ad hoc implicit function theorem to prove Proposition 3.2. In
our Theorem A we show that DL ∈ F ∞
L (U0), i.e., that the above bound holds for derivation with respect
parameters as well, and on the other hand we prove (see Lemma A.1) that any function in F K
L (U0) with
L > K extends to a C K function in a neighbourhood of {0} × U0 in RN +1. We can thus ﬁll the gap between
the proof of [14, Theorem F] and its statement. This shows in particular the validity of the proof of [16,
Proposition 3.2], which constitutes a key step to show the main result in that paper. □

Next result provides the structure of the asymptotic expansion of the local Dulac time and in its statement
we assume that ⌈
max ( m
p , n
q )⌉ ⩾ 0. Let us point out however that we do not need this assumption in any of
the previous auxiliary results. In this regard note that this hypothesis is satisﬁed if m and n are not both
negative. From the point of view of the bifurcation of critical periodic orbits, the most interesting situation
comes from the Dulac time associated to a saddle placed in the line at inﬁnity, and in this case either m > 0
or n > 0.

Theorem B. Let T ( · ; α, β) be the Dulac time of the vector ﬁeld Yα,β in (2) between the sections (0, 1)×{1}
and {1} × (0, 1). Suppose that κ := ⌈max ( m
p , n
q )⌉ ⩾ 0. Then for each L ∈ R we can write

T (s; α, β) = T L(s; α, β) + TL(s; α, β),

where

(1) the principal part is given by

T L(s; α, β) := τ0(β) ln s + s
λnτ1(s
p, s
pω; α, β) − s
mτ1(s
p, 0; α, β) + s
κpτ2(s
p, s
pω; α, β),

with τ0(β) ∈ Q[β], τ1(z, w; α, β) ∈ Q(α1)[z, w, α2, . . . , αN , β] and τ2(z, w; α, β) ∈ Q[z, w, α, β],

(2) and the remainder TL(s; α, β) belongs to F ∞
L (U0 × RM +1).

Moreover the principal part veriﬁes the following:

(a) τ1 is linear in β and without poles along α1 = 0.

(b) τ2 is linear in β and τ2(z, 0; α, β) = 0.

(c) τ1 = 0 if mq − np = 0.

(d) τ0 = −β0 if (m, n) = (0, 0) and τ0 = −β1 if ℓ = 0, whereas τ0 = 0 in any other case.

In a previous paper we already give a structure theorem for the asymptotic expansion of the local Dulac
time, see [10, Theorem B]. The main diﬀerence between both results is that we can now guarantee that
the remainder TL is ﬂat along s = 0, not only for the derivation with respect to s, but also with respect
to α and β (cf. Deﬁnition 1.2). Consequently, as we explain in Remark 1.4, by applying Lemma A.1 we
can assert that if K < L then the remainder TL(s; α, β) extends to a C K function in a neighbourhood of
{0} × U0 × RM +1 in R × RN × RM +1. We are convinced that this regularity of the remainder will be crucial
in future applications, for instance to have a better understanding of the bifurcation diagram of the critical
periodic orbits of the Loud’s centers, see [9]. In fact this kind of property has already been used to study the

6

period of the limit cycle appearing in one-parameter saddle loop bifurcations (see [4, Theorem 16]). To this
end the authors prove Proposition 23, which corresponds to Theorem B particularized to m = n = 0 and
K = L = 1. (As a matter of fact while trying to extend it we realized that their proof contains a bridgeable
mistake that we correct here, see Remark 2.4.) Coming back to our previous result in [10], let us note that
the principal part T L that we provide here is more precise than the one given there.

The paper is organized as follows. In Section 2, taking Roussarie’s results in [15, Chapter 5] as starting
point, we consider the solution ϕ(t; s, α) of Xα passing through (s, 1) ∈ R2 at t = 0 and we expand ϕ2(t; s, α)
as a power series in s for each ﬁxed t and α. We obtain sharp uniform estimates for the radius of convergence
of this series (see Lemma 2.5) and also for the derivatives of its coeﬃcients (see Lemma 2.7). Next, on account
of D(s; α) = ϕ2(− ln s; s, α), in Section 3 we use these results to prove Theorem A. Section 4 is devoted to
the proof of Theorem B and to this end, see (2), we take advantage of the previous results thanks to the
identity
 T (s; α, β) = ∫ − ln s

0
 (

β0xmyn +
 M +ℓ−1∑

i=ℓ βi+1−ℓ(xpyq)
i)∣
∣
∣
∣
∣{(x,y)=ϕ(t;s,α)} dt.

Some technical but crucial issues about the sets F K
L (W ) are treated in Appendix A. Among other properties
we show that any g(s; µ) ∈ F K
L (W ) with L > K extends to a C K-function (on s and the parameter µ) along
s = 0. (This applies in particular to the remainder DL in Theorem A, as well as to TL in Theorem B.) Finally,
in Appendix B we recall some speciﬁc results from analysis and calculus, in particular the multivariate Faa di
Bruno formula for higher-order derivatives of a composite function (see Theorem B.1) that we use repeatedly
all over the paper.

2 Further results on Roussarie’s series expansion

Observe that performing the singular change of variables {u = xpyq, x = x}, the diﬀerential equation given
by the vector ﬁeld Xα in (3) is brought to the following form:
{ ˙x = x,

˙u = P (u; α) := ∑N
i=1 αiu
i.

The ﬁrst equation gives x(t, x0) = x0e
t and we denote by u(t, u0; α) the solution of the second one with
initial condition u(0, u0; α) = u0. For each ﬁxed t and α, we expand it as a power series in u0,

u(t, u0; α) =
 +∞∑

i=1 gi(t; α)ui
0. (5)

In what follows, for any given δ > 0 we deﬁne

Uδ := {α = (α1, . . . , αN ) ∈ RN ; |α1| < δ}.

Following this notation, Roussarie [15, §5.1.2] shows the next result with regard to the series in (5).

Lemma 2.1. The following assertions hold:

(a) For all i ∈ N, gi(t; α) = eα1t¯gi−1(t; α) with ¯gi(t; α) ∈ Q[α, Ω] where Ω := eα1t−1
α1 and degΩ ¯gi ⩽ i.

(b) For each compact set C ⊂ Uδ with δ ∈ (0, 1
2 ] there exist K0, C0 > 0 such that if t ⩾ 0, |u0| < C −1
0 e−δt

and α ∈ C then the series (5) is absolutely convergent and |u(t, u0; α)| ⩽ K0|u0|eδt.

(c) For all i ∈ N, t ⩾ 0 and α ∈ C, |gi(t; α)| ⩽ K0C −1
0 (C0eδt)
i.

7

Proof. The assertion in (a) is proved in Proposition 10. To show (b) we note that, by applying Lemma 18
and following the author’s notation,

|u(t, u0; α)| ⩽
 +∞∑

i=1 |gi(t; α)||u0|
i ⩽
 +∞∑

i=1 Gi(t)|u0|i.

On account of this, the result follows by using the estimates that he obtains in the proof of Lemma 19, more
concretely the upper bound for Gi(t) given in (5.18) replacing e
− 1
2 t by e−δt. Finally (c) follows from (b) by
applying the Cauchy’s estimates (see for instance [18, Theorem 10.26]).

Corollary 2.2. For each compact set C ⊂ Uδ with δ ∈ (0, 1
2 ] there exist C0 > 0 such that the function
u(t, u0; α) is analytic on an open set containing

{(t, u0, α) ∈ RN +2; t ⩾ 0, |u0| < C −1
0 e
−δt, α ∈ C}.

Proof. Recall that u(t, u0; α) is the solution of ˙u = P (u; α) with initial condition u(0, u0; α) = u0. Let us
denote its maximal interval of existence by (ω−, ω+), where ω± = ω±(u0, α). Since P is analytic on RN +1,

D = {(t, u0, α) ∈ RN +2; ω−(u0, α) < t < ω+(u0, α)}

is an open set in RN +2 and u(t, u0; α) is analytic in D (see [5, Theorem 1.1] and [19, page 34]). Moreover, for
the same reason, if ω+ is ﬁnite then |u(t, u0; α)| tends to +∞ as t ↗ ω+ (see [1, Theorem 1.263] or [19, page
17] for instance). Note on the other hand that, by Lemma 2.1, if |u0| < C −1
0 e
−δt then |u(t, u0; α)| ⩽ K0C −1
0
for all t ∈ (0, ω+) and α ∈ C. Arguing by contradiction this implies that ω+ > − 1
δ ln(C0|u0|) and concludes
the proof of the result.

Given ν = (ν0, ν1, . . . , νN ) ∈ Z
N +1
≥0 , we write

∂ν
t,α = ∂|ν|

∂tν0∂αν1
1 · · · ∂ανN
N

and, following this notation, we expand ∂ν
t,αu(t, u0; α) as a power series in u0,

∂ν
t,αu(t, u0; α) =
 +∞∑

i=1 hi(t, α)u
i
0. (6)

Similarly as in Lemma 2.1, we want to estimate the functions hi and the convergence of the above series in
terms of t and α. This is the aim of the next result, where we also write ν = (ν0, ¯ν) with ¯ν = (ν1, . . . , νN )
for the sake of convenience.

Theorem 2.3. For all ν ∈ Z
N +1
≥0 there exists a real number ρ¯ν, satisfying 1 ⩽ ρ¯ν ⩽ max(|¯ν|, 1) and
independent from ν0, such that for each compact set C ⊂ Uδ with δ ∈ (0, 1
2 ] there exist C¯ν > 0, independent
from ν0, and Kν > 0 such that if t ⩾ 0, α ∈ C and |u0| < C −1
¯ν e−δt then

(i) |∂ν
t,αu(t, u0; α)| ⩽ Kν|u0|eρ¯ν δt, and

(ii) the series in (6) is absolutely convergent.

Moreover, for all i ∈ N, α ∈ C and t ⩾ 0, hi(t, α) = ∂ν
t,αgi(t; α) and
∣
∣∂ν
t,αgi(t; α)
∣
∣ ⩽ Kνeρ¯ν δt (C¯νeδt)i−1 .

Finally there exists M > 0 such that if |u0| < (2C0)
−1e−δt then

|∂2
u0u(t, u0; α)| ⩽ M eα1tΩ(t, α1) where Ω(t, α1) := eα1t−1
α1 .

for all t ⩾ 0 and α ∈ C.
 8

Proof. We begin by proving assertions (i) and (ii) in case that ν0 = 0, i.e., only derivation with respect to
parameters. To this end for the sake of shortness we use the compact notation

∂(0,ν1,...,νN )
t,α = ∂ ¯ν
α = ∂|¯ν|

∂αν1
1 · · · ∂ανN
N where ¯ν = (ν1, . . . , νN ).

The proof follows by induction on |¯ν|. The base case |¯ν| = 0 is (b) in Lemma 2.1. To show the induction
step we ﬁrst perform the partial derivation ∂ ¯ν
α on both sides of the equality ∂tu = P (u; α) and then apply
Theorem B.1 to obtain

∂t∂ ¯ν
αu(t, u0; α) =∂ ¯ν
αP (u(t, u0; α); α)

= ∑

1⩽|λ|⩽|¯ν| ∂λP (u; α) ∑

p(¯ν,λ) ¯ν!
 q∏

j=1
 (∂ℓj
α u)kj0 ∏N
i=1(∂ℓj
α αi)
kji

kj!(ℓj!)|kj |
 ∣
∣
∣
∣
∣u=u(t,u0;α) . (7)

Here, for λ = (λ0, . . . , λN ) ∈ Z
N +1
≥0 , we use the notation ∂λP (u; α) = ∂|λ|P (u;α)

∂uλ0 ∂αλ1
1 ···∂α
λN
n and, for kj ∈ Z
N +1
≥0 ,

we write kj = (kj0, . . . , kjN ). Note also that both summations are multidimensional and the second one is
subject to the coupling conditions p(¯ν, λ) deﬁned in (37), namely ∑q
i=1 ki = λ and ∑q
i=1 |ki|ℓi = ¯ν. In this
respect we observe the following:

(a) The only summand in (7) that contains a factor ∂ℓj
α u with |ℓj| = |¯ν| is ∂uP (u; α)∂ ¯ν
αu. Indeed, this is
so because if ℓj = ¯ν and kj0 ̸= 0 then |ki| = 0 for i ̸= j and λ = kj = (1, 0, . . . , 0).

(b) If kj0 = 0 for all j then λ0 = 0. Consequently any summand in (7) not containing a factor ∂ℓu with
|ℓ| > 0 has the factor ∂(0,ℓ)P (u; α) = ∑N
i=1(∂ℓ
ααi)u
i, which is a polynomial vanishing at u = 0.

Accordingly we can split the right hand side of the equation (7) so that it writes as

∂t∂ ¯ν
αu(t, u0; α) = ∂uP (u(t, u0; α); α)∂ ¯ν
αu(t, u0; α) + R1
¯ν(t, u0, α) + R2
¯ν(t, u0, α),

where we deﬁne R1
¯ν to be the sum of those summands with kj0 = 0 for all j = 1, 2, . . . , q while R2
¯ν is the
sum of the remaining summands. Note then that

R1
¯ν(t, u0, α) = uS(u; α)|u=u(t,u0;α)

for some polynomial S(u; α) with degu S = N − 2. The above equality is a ﬁrst order linear diﬀerential
equation for ∂ ¯ν
αu(t, u0; α) that, setting R¯ν = R1
¯ν + R2
¯ν and

B(t, u0, α) := exp (∫ t

0 ∂uP (u(s, u0; α); α)ds
) (8)

for the sake of shortness, yields to

∂ ¯ν
αu(t, u0; α) = B(t, u0, α) ∫ t

0
 R¯ν(s, u0, α)
B(s, u0, α) ds. (9)

Note that we can write ∂uP (u(s, u0; α); α) = ∑∞
i=0 pi(s, α)u
i
0 with the same radius of convergence as (5)
because ∂uP ( · ; α) is polynomial. In addition we have p0(s; α) ≡ α1. Thus, applying (b) in Lemma 2.1 and
setting K1 := sup{|∂uP (u; α) − α1|; |u| ⩽ K0C −1
0 , α ∈ C}, if |u0| < C −1
0 e−δt then
∣
∣
∣
∣
∫ t

0 (∂uP (u(s, u0; α); α) − α1) ds∣
∣
∣
∣ ⩽
 ∞∑

i=1
 ∫ t

0 |pi(s; α)||u0|ids ⩽ K1
 ∞∑

i=1
 ∫ t

0 (C −1
0 eδs)i|u0|
ids

= K1
 ∞∑

i=1 C i
0|u0|
i eδit − 1
δi ⩽ K1
δ
 ∞∑

i=1(C0|u0|eδt)i < +∞,

9

where in the second inequality we use Cauchy’s estimates (see [18, Theorem 10.26]). Thus, by Lemma B.5,

∫ t

0 ∂uP (u(s, u0; α); α)ds =
 +∞∑

i=0
 (∫ t

0 pi(s; α)ds) u
i
0

and the series converges absolutely for |u0| < C −1
0 e
−δt. Furthermore, setting K2 := K1
δ , if |u0| ⩽ (2C0)
−1e−δt

then
 α1t − K2 ⩽ ∫ t

0 ∂uP (u(s, u0; α); α)ds ⩽ α1t + K2 for all t ⩾ 0 and α ∈ C.

Consequently, recall (8), if |u0| ⩽ (2C0)
−1e−δt then

e−K2eα1t ⩽ B(t, u0, α) ⩽ eK2 eα1t for all t ⩾ 0 and α ∈ C. (10)

On the other hand, since x ↦→ e±x are entire functions, the Taylor series of B(t, u0, α) and 1/B(t, u0, α) at
u0 = 0 converge absolutely for all t ⩾ 0 and α ∈ C provided that |u0| < C −1
0 e−δt. Therefore, from (9) and
taking the previous bounds into account, we get that if |u0| ⩽ (2C0)
−1e−δt then

|∂ ¯ν
αu(t, u0; α)| ⩽ e2K2 e
α1t ∫ t

0 |R¯ν(s, u0, α)| e−α1sds for all t ⩾ 0 and α ∈ C. (11)

We are now in position to prove the validity of assertions (i) and (ii) for the case ν0 = 0 and to this end
recall that R¯ν = R1
¯ν + R2
¯ν. Let us begin with the study of R2
¯ν by noting that in each one of its summands
we have that (∂ℓj u(t, u0; α))kj0 veriﬁes |ℓj| < |¯ν| for j = 1, 2, . . . , q and that there is at least one exponent
kj0 strictly positive. Accordingly, thanks to the induction hypothesis, for each j = 1, 2, . . . , q we know that
if |u0| < C −1
ℓj e−δt then |(∂ℓj u(t, u0; α))kj0| ⩽ (Kℓj |u0|eρℓj δt)
kj0 for all t ⩾ 0 and α ∈ C. We deﬁne

p⋆(¯ν) := ⋃

1⩽|λ|⩽|¯ν| {(k1, . . . , kq; ℓ1, . . . , ℓq) ∈ p(¯ν, λ) ; |ℓj| < |¯ν|} ,

which is nonempty if and only if |¯ν| > 1. Taking this into account, if |¯ν| > 1 then we set

C¯ν := max (2C0, max (Cℓj ; (k1, . . . , kq; ℓ1, . . . , ℓq) ∈ p⋆(¯ν)
))
,

ρ¯ν := max (1, max (∑q
j=1 kj0ρℓj ; (k1, . . . , kq; ℓ1, . . . , ℓq) ∈ p⋆(¯ν)
))

and
 K3 := max (∏q
j=1(Kℓj )
kj0; (k1, . . . , kq; ℓ1, . . . , ℓq) ∈ p⋆(¯ν)
) ,

whereas if |¯ν| = 1 then we deﬁne C¯ν = 2C0, ρ¯ν = 1 and K3 = 1. Furthermore we deﬁne

K4 := sup {
|∂λP (u; α)|; |u| ⩽ K0C −1
0 , α ∈ C, 1 ⩽ |λ| ⩽ |¯ν|
}

and
 K5 := sup {∑
1⩽|λ|⩽|¯ν| ∑

p(¯ν,λ) ν! ∏q
j=1
 ∏N
i=1(∂ℓj αi)kji

kj !(ℓj !)|kj | ; α ∈ C}

Note moreover that |u0|∑q
j=1 kj0 ⩽ |u0| due to ∑q
j=1 kj0 ⩾ 1 and |u0| ⩽ 1. On account of these deﬁnitions
and applying (b) in Lemma 2.1, from (7) it follows that if |u0| < C −1
¯ν e−δt then |R2
¯ν(t, u0, α)| ⩽ K6|u0|eρ¯ν δt

for all t ⩾ 0 and α ∈ C, where we set K6 := K3K4K5. Let us proceed next with the study of R1
¯ν. In this
case, due to R1
¯ν(t, u0, α) = uS(u; α)|u=u(t,u0;α) , we deﬁne

K7 := sup {|S(u; α)|; |u0| ⩽ K0C −1
0 , α ∈ C} .

10

Thus, by applying Lemma 2.1, if |u0| < C −1
0 e−δt then |R1
¯ν(t, u0, α)| ⩽ K0K7|u0|eδt for all t ⩾ 0 and α ∈ C.
Finally, taking C¯ν ⩾ C0 into account, we can assert that if |u0| < C −1
¯ν e−δt then

|R¯ν(t, u0, α)| ⩽ |R1
¯ν(t, u0, α)| + |R2
¯ν(t, u0, α)| ⩽ K0K7|u0|eδt + K6|u0|eρ¯ν δt ⩽ K8|u0|eρ¯ν δt (12)

for all t ⩾ 0 and α ∈ C, where we set K8 := max(K6, K0K7) and we use that ρ¯ν ⩾ 1. We can now plug this
inequality in (11) to obtain that if |u0| < C −1
¯ν e−δt then

|∂ ¯ν
αu(t, u0; α)| ⩽ K8e2K2 |u0|eα1t ∫ t

0 e
(ρ¯ν δ−α1)sds = K8e2K2|u0|eα1t e(ρ¯ν δ−α1)t − 1
ρ¯νδ − α1 ⩽ Kν|u0|eρ¯ν δt

for all t ⩾ 0 and α ∈ C, where Kν := K8e2K2
K9 with K9 := inf{ρ¯νδ − α1; α ∈ C}, which is strictly positive
because |α1| < δ ⩽ ρ¯νδ. This proves the inductive step with regard to assertion (i). Let us turn now to
assertion (ii). Since R¯ν is a polynomial of ∂ℓu with 0 ⩽ |ℓ| < |¯ν| on account of property (a), by the induction
hypothesis we get that the Taylor series of R¯ν(t, u0, α) at u0 = 0 is absolutely convergent for all t ⩾ 0 and
α ∈ C provided that |u0| < C −1
¯ν e−δt. Furthermore, from (12), if |u0| < C −1
¯ν e
−δt then

|R¯ν(t, u0, α)| ⩽ K8C −1
¯ν e(ρ¯ν −1)δt for all t ⩾ 0 and α ∈ C.

Recall on the other hand that the Taylor series of 1
B(t,u0,α) at u0 = 0 is absolutely convergent for all t ⩾ 0
and α ∈ C provided that |u0| < C −1
0 e−δt. In addition (10) shows that 1
|B(t,u0,α)| ⩽ eK2e−α1t for this range

of values. Hence, due to C0 < 2C0 ⩽ C¯ν, if |u0| < C −1
¯ν e−δt then the series R¯ν (t,u0,α)
B(t,u0,α) = ∑∞
i=0 ri(t; α)u
i
0 is
absolutely convergent and the upper bound
∣
∣
∣
∣ R¯ν(t, u0, α)
B(t, u0, α)
 ∣
∣
∣
∣ ⩽ K8C −1
¯ν eK2 e((ρ¯ν −1)δ−α1)t ⩽ K8C −1
¯ν eK2eρ¯ν δt

holds for all t ⩾ 0 and α ∈ C due to |α1| < δ. Note also that r0(t; α) ≡ 0. As we did before, the Cauchy’s
estimates show that
 |ri(t; α)| ⩽ K8C −1
¯ν eK2C i
¯νe
(ρ¯ν +i)δt for all i ∈ N, t ⩾ 0 and α ∈ C.

Consequently, for all i ∈ N, t ⩾ 0 and α ∈ C, we get

∫ t

0 |ri(s; α)|ds ⩽ K8C −1
¯ν eK2 C i
¯ν e(ρ¯ν +i)δt − 1
(ρ¯ν + i)δ ⩽ K9C i
¯νe(ρ¯ν +i)δt,

where K9 = K8C−1
¯ν eK2
ρ¯ν δ . Thanks to these estimates we can assert that if |u0| < C −1
¯ν e−δt then

∣
∣
∣
∣
∫ t

0
 R¯ν(s, u0, α)
B(s, u0, α) ds
∣
∣
∣
∣ ⩽
 +∞∑

i=1 |u0|i ∫ t

0 |ri(s; α)|ds ⩽ K9eρ¯ν δt +∞∑

i=1
 (C¯ν|u0|eδt)i < ∞

for all t ⩾ 0 and α ∈ C. Therefore, by Lemma B.5,

∫ t

0
 R¯ν(s, u0, α)
B(s, u0, α) ds =
 +∞∑

i=1
 (∫ t

0 ri(s; α)ds) u
i
0

and the series converges absolutely for |u0| < C −1
¯ν e−δt. Since we already prove this fact for the Taylor
series of B(t, u0, α) at u0 = 0, from (9) it follows that the Taylor series of ∂ ¯ν
αu(t, u0; α) at u0 = 0 converges
absolutely for all t ⩾ 0 and α ∈ C provided that |u0| < C −1
¯ν e−δt. This shows the inductive step concerning
assertion (ii) for the case ν0 = 0.
 11

Let us turn now to the proof of the case ν0 > 0. Since ∂tu = P (u; α) we deduce that ∂n
t u = Pn(u; α)
for all n ∈ N, where Pn := P ∂uPn−1 with P0(u; α) := u. The application of Faa di Bruno formula given by
Theorem B.1 yields to

∂(ν0,ν1,...,νN )
t,α u(t, u0; α) = ∂ ¯ν
αPν0(u(t, u0; α))

= ∑

1⩽|λ|⩽|¯ν| ∂λPν0 (u; α) ∑

p(¯ν,λ) ¯ν!
 q∏

j=1
 (∂ℓj
α u)
kj0 ∏N
i=1(∂ℓj
α αi)kji

kj!(ℓj!)|kj |
 ∣
∣
∣
∣
∣
u=u(t,u0;α) (13)

= ˆR1
ν(t, u0, α) + ˆR2
ν(t, u0, α),

where ˆR1
ν consists in all the summands with kj0 = 0 for all j. Accordingly, due to Pν0(0; α) ≡ 0, exactly as
we did to show (b), we can write ˆR1
ν(t, u0, α) = uSν(u; α)|u=u(t,u0;α) for some polynomial Sν. Thus, setting

K10 := sup {
|Sν(u; α)|; |u| ⩽ K0C −1
0 , α ∈ C}

and applying (b) in Lemma 2.1, if |u0| < C −1
0 e−δt then |R1
ν(t, u0, α)| ⩽ K0K10|u0|eδt for all t ⩾ 0 and α ∈ C.
On the other hand, since we have already proved the validity of (i) for the particular case ν0 = 0, it follows
that for each j there exist Kℓj , Cℓj > 0 and ρℓj ⩾ 1 such that |∂ℓj
α u(t, u0; α)| ⩽ Kℓj |u0|etρℓj for all t ⩾ 0
and α ∈ C provided that |u0| ⩽ C −1
ℓj e−δt. Thus, taking upper bounds in (13) as we did before with R2
¯ν,
it follows that there exists Kν > 0 (which we take satisfying Kν ⩾ 2K0K10 for convenience) such that if
|u0| < C −1
¯ν e−δt then | ˆR2
ν(t, u0, α)| ⩽ 1
2 Kν|u0|e
ρ¯ν δt for all t ⩾ 0 and α ∈ C. (Here we remark that ρ¯ν ⩾ 1 and
C¯ν ⩾ C0 are the ones previously deﬁned when we tackle the case ν0 = 0.) Hence, if |u0| < C −1
¯ν e−δt then

|∂ ¯ν
t,αu(t, u0; α)| ⩽ | ˆR1
ν(t, u0, α)| + | ˆR2
ν(t, u0, α)| ⩽ K0K10|u0|eδt + 1
2 Kν|u0|eρ¯ν δt ⩽ Kν|u0|eρν δt

for all t ⩾ 0 and α ∈ C. Finally the fact that the Taylor series of ∂ν
t,αu(t, u0; α) is absolutely convergent for

all t ⩾ 0 and α ∈ C provided that |u0| < C −1
¯ν e−δt follows from (13) using that this is true for ∂ℓj
α u(t, u0; α)
for all j and that ∂λPν0 (u; α) is polynomial in u.

So far we have proved assertions (i) and (ii) except for the validity of the upper bound ρ¯ν ⩽ max(|¯ν|, 1).
Lemma 2.1 shows that this is true for |¯ν| = 0 because we can take ρ0 = 1. The proof for |¯ν| ⩾ 1 follows by
induction taking into account that

ρ¯ν := max (1, max (∑q
j=1 kj0ρℓj ; (k1, . . . , kq; ℓ1, . . . , ℓq) ∈ p⋆(¯ν)
)) .

The base case is also true by deﬁnition because ρ¯ν = 1 for |¯ν| = 1 (recall that in this case the set p⋆(¯ν) is
empty). The inductive step follows by noting that, due to the deﬁnition of p(¯ν, λ),

q∑

j=1 kj0ρℓj ⩽
 q∑

j=1 kj0|ℓj| ⩽
 q∑

j=1(kj0 + · · · + kjN )|ℓj| =
 q∑

j=1 |kj|(ℓj1 + · · · + ℓjN ) = |¯ν|,

where in the ﬁrst inequality we use the inductive step and in the last equality take ∑q
j=1 |kj|ℓj = ¯ν into
account.

Let us prove next the statement concerning the coeﬃcients hi(t, α) in the series (6). To this aim observe
that, by assertion (ii), this series converges absolutely for all t ⩾ 0 and α ∈ C provided that |u0| < C −1
¯ν e
−δt.
This implies that, for each ﬁxed t ⩾ 0 and α ∈ C,

hi(t, α) = 1
i! ∂i
u0 ∂ν
t,αu(t, u0; α)∣
∣u0=0 for all i ∈ N. (14)

On the other hand, thanks to assertion (i), if |u0| < C −1
¯ν e−δt then

|∂ν
t,αu(t, u0; α)| ⩽ Kν|u0|eρ¯ν δt < KνC −1
¯ν e
(ρ¯ν −1)δt.

12

Therefore, by applying the Cauchy’s estimates,

|hi(t; α)| ⩽ KνC −1
¯ν e(ρ¯ν −1)δt (C¯νeδt)i = K¯νe
ρ¯ν δt (C¯νeδt)i−1

for all i ⩾ 1, α ∈ C and t ⩾ 0. Recall in addition that, by (b) in Lemma 2.1, if |u0| < C −1
0 e
−δt then
u(t, u0; α) = ∑+∞
i=1 gi(t, α)u
i
0 converges absolutely for all t ⩾ 0 and α ∈ C. In particular, for each ﬁxed t ⩾ 0
and α ∈ C, we can assert that gi(t, α) = 1
i! ∂i
u0u(t, u0; α)
∣
∣u0=0 holds for all i ∈ N. Consequently

hi(t, α) = 1
i! ∂i
u0∂ν
t,αu(t, u0; α)
∣
∣u0=0 = 1
i! ∂ν
t,α∂i
u0 u(t, u0; α)
∣
∣u0=0 = ∂ν
t,αgi(t, α),

where in the ﬁrst equality we use (14) and in the second one Corollary 2.2.

It only remains to be proved the upper bound for |∂2
u0 u(t, u0, α)|. To this end we observe that

∂u0u(t, u0; α) = exp (∫ t

0 ∂uP (u(s, u0; α); α)ds) = B(t, u0, α),

where we use ∂t∂u0u = ∂uP (u; α)∂u0u in the ﬁrst equality and (8) in the second one. Therefore

∂2
u0u(t, u0; α) = B(t, u0, α) ∫ t

0 ∂2
uP (u(s, u0; α); α)B(s, u0, α)ds.

Setting K11 := sup {|∂2
uP (u; α)|; |u| ⩽ K0C −1
0 , α ∈ C} , (b) in Lemma 2.1 and the inequalities in (10) show
that if |u0| < (2C0)
−1e−δt then

|∂2
u0u(t, u0; α)| ⩽ K11e2K2eα1t ∫ t

0 eα1sds = M eα1tΩ(t, α1),

where we take M = K11e2K2. This completes the proof of the result.

Remark 2.4. Let us mention that Theorem 2.3 corrects a mistake in the proof of [4, Propositon 23]. The
authors of that paper split the proof into two intermediate claims. The second one is a particular case of
assertion (i) in Theorem 2.3 (it corresponds to |¯ν| = 1 and N = 1) but the proof given there is not right.
Indeed, they consider in page 283 the series p(u(ξ, u0)) = ∑+∞
i=1 pi(ξ)u
i
0 but the summation index should
run from i = 0. This may seem a typo but it has important consequences in order to bound the derivative
with respect to parameters because, transferred to our proof, it yields to the factor eα1t in (10). That being
said, except for this bridgeable mistake in the proof of [4, Propositon 23], the main result in that paper
with regard to the period of the limit cycle emerging from a saddle loop bifurcation is perfectly correct. □

At this point let us denote by t ↦→ (x(t, p0; α), y(t, p0; α)) the solution of the diﬀerential system given
by the vector ﬁeld Xα in (3) passing through p0 = (x0, y0) ∈ R2. It is clear that x(t, p0; α) = x0e
t. We are
interested in the analytical properties of y(t, p0; α) with the initial condition p0 = (s, 1). This is the reason
why we ﬁrst studied u = xpyq and in this respect, by Lemma 2.1, we know that

u(t, u0; α) =
 +∞∑

i=1 gi(t; α)u
i
0 = u0eα1t +∞∑

i=0 ¯gi(t; α)u
i
0,

where the series converge absolutely and we use that gi(t; α) = eα1t¯gi−1(t; α). Thus, since x(t, p0; α) = x0et,

(y(t, p0; α))q = e−ptyq
0eα1t +∞∑

i=0 ¯gi(t; α)ui
0 = yq
0e(α1−p)t (

1 +
 +∞∑

i=1 ¯gi(t; α)u
i
0
)
 . (15)

13

Since (1 + z)
η = ∑+∞
k=0 (η
k)zk for |z| < 1, with the aim of computing (y(t, x0, y0; α)
)j for any j ∈ Z we set

ψj
0 := 1 and, for k ∈ N, ψj
k :=
 k∑

r=1
 (j/q
r
 ) ∑

i1+···+ir=k ¯gi1 · · · ¯gir . (16)

Our next task is to prove the following result.

Lemma 2.5. For each compact set C ⊂ Uδ with δ ∈ (0, 1
2 ] there exist C0, M > 0 such that the identity

(y(t, s, 1; α))j = e−λjt +∞∑

k=0 ψj
k(t; α)s
kp

holds for all j ∈ Z, t ⩾ 0, α ∈ C and s > 0 with s
p max (M Ω(t, α1), 4C0eδt) < 2, Moreover under these
conditions the series is absolutely convergent.

Proof. Since gi(t; α) = eα1t¯gi−1(t; α) and ¯g0 = 1, from (5) we get

+∞∑

i=1 ¯gi(t; α)u
i
0 = u(t, u0; α) − u0eα1t

u0eα1t = ∂2
u0u(t, ξ; α)u2
0
2u0eα1t for some ξ ∈ [0, u0],

where in the second equality we apply Taylor’s theorem to the function u0 ↦→ u(t, u0; α) taking u(t, 0; α) = 0
and ∂u0u(t, 0; α) = eα1t into account. By applying Theorem 2.3, there exist C0, M > 0 such that if
|u0| < (2C0)
−1e
−δt then
 |∂2
u0u(t, u0; α)| ⩽ M eα1tΩ(t, α1) for all t ⩾ 0 and α ∈ C.

Hence if |u0| < (2C0)
−1e−δt then ∣
∣
∣∑+∞
i=1 ¯gi(t; α)u
i
0∣
∣
∣ ⩽ M
2 Ω(t, α1)|u0| for all t ⩾ 0 and α ∈ C. Therefore, if

|u0| < min ( 2
M Ω(t,α1) , (2C0)
−1e−δt) then ∣
∣
∣∑+∞
i=1 ¯gi(t; α)u
i
0∣
∣
∣ < 1 for all t ⩾ 0 and α ∈ C. Accordingly, since

(1 + z)j/q = ∑+∞
k=0 (j/q
k )zk for |z| < 1, from (15) and (16) it follows that

(y(t, x0, y0; α)
)j = yj
0ej(α1−p)t/q (

1 +
 +∞∑

i=1 ¯gi(t; α)ui
0
)j/q
 = yj
0ej(α1−p)t/q +∞∑

k=0 ψj
k(t; α)u
k
0

for all t ⩾ 0 and α ∈ C provided that |u0| < 1/ max ( M
2 Ω(t, α1), 2C0eδt). Furthermore the second series
converges absolutely because so it does the ﬁrst one thanks to Lemma 2.1. Finally, since u0 = xp
0yq
0 and
λ = p−α1
q , the result follows taking (x0, y0) = (s, 1).

The following is a technical lemma that will be used in the proof of our last result in this section.

Lemma 2.6. For each m, n ∈ Z≥0 there exist Pmn, Qmn ∈ Z[x, y] with degx Pmn = degx Qmn = m and
degy Pmn = degy Qmn = n such that for any a ∈ R,

∂n
x ∂m
y eaxy = a
meaxyPmn(x, ay) and ∂n
x ∂m
y xy = xy−nQmn(ln x, y).

In particular, there exist M1, M2 > 0 such that
∣
∣∂n
x ∂m
y eaxy∣
∣ ⩽ M1 max(1, |x|, |ay|)
m+n|a|meaxy and ∣
∣∂n
x ∂m
y xy∣
∣ ⩽ M2 max(1, | ln x|, |y|)m+nxy−n.

Proof. Note that ∂n
x ∂m
y eaxy = ∂n
x (eaxy(ax)
m) and ∂n
x ∂m
y xy = ∂n
x (xy(ln x)m). From here the proof follows
by induction on n. To this end we set Pm0(x, y) = Qm0(x, y) = xm. Then the inductive step follows by
taking Pm,n+1 = yPmn + ∂xPmn and Qm,n+1 = (y − n)Qmn + ∂xQmn.

14

Lemma 2.7. For each compact set C ⊂ Uδ with δ ∈ (0, 1
2 ], j ∈ Z and ν ∈ Z
N +1
≥0 there exist Cjν, Kν > 0
such that |∂ν
t,αψj
k(t; α)| ⩽ Kν(k + 1)3|ν|(Cjν)k max(1, t)
|ν|e(3k+|ν|)δt

for all k ∈ Z≥0, t ⩾ 0 and α ∈ C.

Proof. Note ﬁrst that, on account of the deﬁnition in (16),

∂νψj
k =
 k∑

r=1
 (j/q
r
 ) ∑

i1+···+ir=k ∂ν(¯gi1 · · · ¯gir ),

where, due to gi(t; α) = eα1t¯gi−1(t; α) and applying Theorem B.2,

∂ν(¯gi1 · · · ¯gir ) = ∑

ℓ0+...+ℓr=ν aℓ0,...,ℓr ∂ℓ0(e−α1rt)∂ℓ1gi1+1 · · · ∂ℓr gir+1.

We remark that this summation is multidimensional with ℓ0, . . . , ℓr ∈ Z
N +1
≥0 and aℓ0,...,ℓr = ( ν
ℓ0,...,ℓr) are
the generalized multinomial coeﬃcients (cf. Remark B.3). Setting ℓ0 = (ℓ00, . . . , ℓ0N ) then, by Lemma 2.6,
∂ℓ0 (e−α1rt) = ∂ℓ00
t ∂ℓ01
α1 (e−α1rt) = (−r)
ℓ01 e−α1rtPℓ01ℓ00 (t, −α1r) if ℓ02 = . . . = ℓ0N = 0 and zero otherwise.
In addition |∂ℓ0(e−α1rt)| ⩽ Mℓ0 max(1, |t|, |rα1|)
|ℓ0|rℓ01e−α1rt. On the other hand, by Theorem 2.3,

|∂ℓ
t,αgi+1(t; α)| ⩽ Kℓeρℓδt(Cℓeδt)
i for all i ∈ N, α ∈ C and t ⩾ 0.

Thus, if we set ˆMν := max(Mℓ; ℓ ⩽ ν), ˆCν := max(Cℓ; ℓ ⩽ ν) and ˆKν := max(Kℓ; ℓ ⩽ ν), then

|∂ν (¯gi1 · · · ¯gir ) (t; α)| ⩽ ∑

ℓ0+...+ℓr=ν aℓ0,...,ℓr ˆMν( ˆKν)
r max(1, |t|)
|ν|r2|ν|e(r+ρℓ1 +...+ρℓr )δt( ˆCνeδt)i1+...+ir .

Here we use |α1| ⩽ δ < 1, ℓ0 ⩽ ν and r ⩾ 1, which implies

max(1, |t|, |rα1|)
|ℓ0|rℓ01 ⩽ max(1, |t|, |r|)
|ν|rν1 ⩽ max(1, |t|)
|ν|r2|ν|.

Hence, since ρν ⩽ max(|ν|, 1) ⩽ 1 + |ν| thanks to Theorem 2.3 and, on the other hand, |ℓ0| + . . . + |ℓr| = |ν|
and r ⩽ k = i1 + · · · + ir, we obtain

|∂ν (¯gi1 · · · ¯gir ) (t; α)| ⩽ ˆMν( ˆKν ˆCν)
kk2|ν| max(1, t)
|ν|e
(3k+|ν|)δt ∑

ℓ0+...+ℓr=ν aℓ0,...,ℓr .

Thus, since ∑

ℓ0+...+ℓr=ν aℓ0,...,ℓr = (r + 1)|ν| ⩽ (k + 1)|ν| thanks to Remark B.3, we get

|∂ν (¯gi1 · · · ¯gir ) (t; α)| ⩽ ˆMν( ˆKν ˆCν)
k(k + 1)3|ν| max(1, t)|ν|e(3k+|ν|)δt.

Accordingly, since |
(j/q
r )| ⩽ max(|j/q|, 1)
r ⩽ max(|j|, 1)k for all j ∈ Z,

∣
∣
∣∂νψj
k(t; α)
∣
∣
∣ ⩽ ˆMν( ˆKν ˆCν)
k(k + 1)3|ν| max(1, t)
|ν|e(3k+|ν|)δt k∑

r=1 max(|j|, 1)
k ∑

i1+···+ir=k 1

= ˆMνp(k) (max(|j|, 1) ˆKν ˆCν)k (k + 1)3|ν| max(1, t)|ν|e(3k+|ν|)δt,

where p(k) is the number of partitions of k and it is easy to see that p(k) ⩽ (2k−1
k ) ⩽ 22k−1 ⩽ 4
k. Hence,
setting Cjν = 4 max(|j|, 1) ˆKν ˆCν and Kν = ˆMν, the result follows.

15

3 Dulac map

This section is entirely devoted to prove Theorem A, that will follow almost immediately from Theorem 3.3.
In the proof of this result, and the forthcoming Proposition 4.2, we will use the following lemma together
with this easy observation:

Remark 3.1. The function φ(s) = s
α(− ln s)
m is monotonous increasing on the interval (0, 1
e ) provided
that α > m ⩾ 0 because ∂sφ(s) = −s
α−1(− ln(s))
m−1(m + α ln s). □

Lemma 3.2. For every ρ ∈ (0, 1) and n ∈ Z+ there exists A > 0 such that ∑

k⩾K knrk ⩽ AK nrK for all
K ∈ N and 0 ⩽ r ⩽ ρ.

Proof. Setting cℓ := (n
ℓ) ∑+∞
i=0 i
n−ℓρi and A := ∑n
ℓ=0 cℓ we obtain

+∞∑

k=K knrk =
 +∞∑

i=0(i + K)
nri+K = rK n∑

ℓ=0
 (n
ℓ
)K ℓ +∞∑

i=0 i
n−ℓri ⩽ rK n∑

ℓ=0 cℓK ℓ ⩽ AK nrK,

where in the last inequality we take K ⩾ 1 into account.

Theorem 3.3. Consider the family of vector ﬁelds {Xα}α∈Uδ deﬁned in (3) and let D( · ; α) be the Dulac
map of Xα between the transversal sections {y = 1} and {x = 1}. Then the following holds:

(a) For each compact set C ⊂ Uδ with δ ∈ (0, 1
2 ] there exists s0 > 0 such that

D(s; α) =
 +∞∑

k=0 ψ1
k(− ln s; α)s
kp+λ, for all s ∈ (0, s0) and α ∈ C,

and the series is absolutely convergent. Moreover, for each K ∈ N there exists ∆(z, w; α) ∈ Q[z, w, α]
with degz,w(∆) < K and ∆(0, 0; α) = 1 such that

K−1∑

k=0 ψ1
k(− ln s; α)s
kp+λ = s
λ∆(s
p, s
pω; α), where ω = ω(s; α1).

(b) Finally, for each L ∈ R there exists KL ∈ Z≥0 such that

+∞∑

k=KL ψ1
k(− ln s; α)s
kp+λ ∈ F ∞
L (U0). (17)

Proof. The solution x(t, x0, y0; α) = x0et of Xα with initial condition (x0, y0) = (s, 1) intersects the
transversal section {x = 1} at t = − ln s. Hence the Dulac map is given by D(s; α) = y(t, s, 1; α)|t=− ln s.
On account of this, the ﬁrst assertion in (a) will follow by applying Lemma 2.5 once we show that we can
take s0 > 0 small enough such that

s
p max (M Ω(t, α1), 4C0eδt)∣
∣t=− ln s < 2 for all s ∈ (0, s0).

In this respect observe that, by applying (b) in Lemma A.4, s
pΩ(− ln s, α1) = s
pω(s; α1) tends to 0 as s → 0+

uniformly in α1 ∈ (−δ, δ), and this is also true for s
p−δ because p − δ ⩾ p − 1
2 > 0. Consequently it is clear
that there exists s0 > 0 small enough such that the above inequality holds and so the ﬁrst assertion is true.
With regard to second one, from (a) in Lemma 2.1 and (16) it follows that ψ1
k(− ln s; α) = ηk(ω; α) where
ηk ∈ Q[ω, α] with degω(ηk) ⩽ k. Then it is clear that, for each k = 0, 1, . . . , K −1, there exists a homogeneous

16

polynomial ˆηk ∈ Q[z, w, α] with degw(ˆηk) ⩽ k such that we can write ψ1
k(− ln s; α)s
kp = ˆηk(s
p, s
pω; α). Since
ˆη0 ≡ 1, this shows the validity of the second assertion in (a).

In order to prove (b) we claim that for each ν ∈ Z
N +1
≥0 there exists s0 > 0 small enough such that the
series ∑

k⩾0 ∂ν
s,α(ψ1
k(− ln s; α)s
pk+λ) converges uniformly on (0, s0) × C, where C is any compact set in Uδ
that we hereafter. By the Weierstrass M -test, to this end it suﬃces to show that there exists a sequence of
positive numbers {Mk}k∈N with ∑

k⩾1 Mk < ∞ such that, for some kν ∈ N large enough,

|∂ν
s,α(ψ1
k(− ln s; α)s
kp+λ)| ⩽ Mk, for all k ⩾ kν, s ∈ (0, s0) and α ∈ C.

By applying Theorem B.2 we have that

∂ν(ψ1
k(− ln s; α)s
kp+λ) = ∑

ℓ1+ℓ2=ν aℓ1ℓ2∂ℓ1(ψ1
k(− ln s; α))∂ℓ2(s
pk+λ) (18)

with aℓ1ℓ2 = ( ν
ℓ1,ℓ2). Setting ˆℓ1 = (0, ℓ11, . . . , ℓ1N ) it turns out that, for each ﬁxed s and α,

|∂ℓ1
s,α(ψ1
k(− ln s; α))| = |∂ℓ10
s (∂ ˆℓ1
α ψ1
k)(− ln s; α)| ⩽ Cℓ10s
−ℓ10 max
j∈{0,...,ℓ10} |(∂(j,ℓ11,...,ℓ1N )ψ1
k)(− ln s, α)|,

where Cℓ10 > 0 depends only on ℓ10. The above inequality is clear in case that ℓ10 = 0, whereas for ℓ10 ⩾ 1
it follows easily by applying the one-dimensional Faa di Bruno formula

∂n
s (f (g(s))) =
 n∑

j=1(∂j
sf )(g(s)) ∑

p(n,j) n!
 n∏

i=1
 (∂ig(s))ki

(ki!)(i!)ki

taking n = ℓ10, f = ∂ ˆℓ1
α ψ1
k and g = − ln s and noting that, in doing so, ∂ig(s) = (−1)
i(i − 1)!s
−i and∑n
i=1 iki = n. Thus by applying Lemma 2.7 we deduce that, for all s ∈ (0, 1/e) and α inside a compact
subset C of Uδ with δ ∈ (0, 1
2 ],

|∂ℓ1
s,α(ψ1
k(− ln s; α))| ⩽ ˆKℓ1 (k + 1)3|ℓ1|( ˆCℓ1)
k(− ln s)|ℓ1|s
−(3k+|ℓ1|)δ−ℓ10 , (19)

where, following the notation in that result,

ˆKℓ1 = Cℓ10 max(K(j,ℓ11,...,ℓ1N ); j = 0, . . . , ℓ10) and ˆCℓ1 = max(C1,(j,ℓ11,...,ℓ1N ); j = 0, . . . , ℓ10)

and we use that max(1, − ln s) = − ln s for s ∈ (0, 1/e). In addition, since λ = p−α1
q , Lemma 2.6 shows that

|∂ℓ2(s
pk+λ)| = |∂ℓ20
s ∂ℓ21
α1 (s
pk+λ)| ⩽ M2 max(− ln s, pk + λ)
|ℓ2|s
pk+λ−ℓ20 q−ℓ21

⩽ Cℓ2 (k + 1)|ℓ2|(− ln s)
|ℓ2|s
pk+λ−ℓ20,

because pk + λ ⩽ p(k + 1) + 1 ⩽ 2p(k + 1) due to p, q ⩾ 1, |α1| ⩽ δ < 1 and we set Cℓ2 = (2p)|ℓ2|q−ℓ21 M2.
Here we also use that max(x, y) ⩽ xy when x, y ⩾ 1. Using this inequality and the one in (19), from (18)
we obtain |∂ν(ψ1
k(− ln s; α)s
kp+λ)| ⩽ ¯Kν( ¯Cν)
k(k + 1)3|ν|(− ln s)
|ν|s
(p−3δ)k+λ−|ν|δ−ν0, (20)

where we set ¯Cν := max( ˆCℓ1; ℓ1 ⩽ ν) and, on account of ∑

ℓ1+ℓ2=ν aℓ1ℓ2 = 2
|ν|,

¯Kν := 2
|ν| max( ˆKℓ1Cℓ2; ℓ1 + ℓ2 = ν).

Let us remark that the above estimate holds for all s ∈ (0, 1/e) and α ∈ C ⊂ Uδ with δ ∈ (0, 1
2 ]. As a matter
of fact, at this point we shrink it so that δ ∈ (0, 1
4 ), which in particular implies p − 3δ ⩾ 1
4 . Consequently,
using also the fact that λ > 0, from (20) we get

|∂ν(ψ1
k(− ln s; α)s
kp+λ)| ⩽ ¯Kν( ¯Cν)
k(k + 1)3|ν|(− ln s)
|ν|s
(k−|ν|)/4−ν0 =: mk(s). (21)

17

On account of Remark 3.1 it easily follows that a suﬃcient condition for s ↦→ mk(s) to be monotonous
increasing on (0, 1/e) is that k > 9|ν| =: kν.

Note on the other hand that

mk(s) = ¯Kν( ¯Cνs
1/4)k(k + 1)3|ν|(− ln s)
|ν|s
−|ν|/4−ν0.

Thus if we take s0 := min ( 1
e , (2 ¯Cν)
−4) then the series with general term Mk := mk(s0) is summable and,
additionally, from (21) and the monotonicity of mk(s) on (0, 1/e),

|∂ν(ψ1
k(− ln s; α)s
kp+λ)| ⩽ mk(s) < Mk for all s ∈ (0, s0) and k ⩾ kν.

This proves the validity of the claim and consequently, by applying Lemma B.4 recursively, if s ∈ (0, s0)
and α ∈ Uδ then
 ∂ν
s,α
 ( +∞∑

k=KL ψ1
k(− ln s; α)s
pk+λ)
 =
 +∞∑

k=KL ∂ν
s,α (ψ1
k(− ln s; α)s
pk+λ) (22)

for all ν ∈ Z
N +1
≥0 and KL ∈ N. (We stress that the above identity is valid regardless of KL ⩾ kν and this is
crucial in what follows because kν depends on ν.)

We are now in position to ﬁnish the proof. We will show that (17) holds taking KL := max(0, ⌈4L⌉ + 4).
To this end, recall Deﬁnition 1.2, we ﬁx any ν ∈ Z
N +1
≥0 and α⋆ = (0, α2, . . . , αN ) ∈ U0 = {0} × RN −1, and
we take a relatively compact neighbourhood V of α⋆ contained in Uδ with δ = min( 1
4 , 1
|ν| ). Then, from (22)
and using the upper bound in (20), for each s ∈ (0, s0) and α ∈ V we have
∣
∣
∣
∣
∣∂ν
s,α
 ( +∞∑

k=KL ψ1
k(− ln s; α)s
pk+λ)∣
∣
∣
∣
∣ ⩽
 +∞∑

k=KL
 ∣
∣∂ν
s,α(ψ1
k(− ln s; α)s
pk+λ)
∣
∣

⩽ ¯Kν(− ln s)
|ν|s
λ−|ν|δ−ν0 +∞∑

k=KL(k + 1)3|ν|( ¯Cνs
p−3δ)k

⩽ ¯KνMνs
−|ν|δ−ν0A(KL + 1)3|ν|( ¯Cν)
KL s
(p−3δ)KL

⩽ ¯KνMνA(KL + 1)3|ν|( ¯Cν)KLs 1
4 KL−1−ν0 ⩽ Cs
L−ν0 .

In the third inequality above we apply Lemma 3.2 and set Mν := sup{s
λ(− ln s)
|ν|; s ∈ (0, s0), |α1| ⩽ δ}.
Next, in the fourth inequality, we take δ = min( 1
4 , 1
|ν| ) into account. Finally in the last inequality we set

C := ¯KνMνA(KL + 1)3|ν|( ¯Cν)KL and use that KL ⩾ 4(L + 1). This completes the proof of the result.

Proof of Theorem A. By Theorem 3.3, for each compact set C ⊂ Uδ with δ ∈ (0, 1
2 ] there exists s0 > 0
such that
 D(s; α) =
 +∞∑

k=0 ψ1
k(− ln s; α)s
kp+λ for all s ∈ (0, s0) and α ∈ C.

In addition, for each L ∈ R there exists KL ∈ Z≥0 such that

DL(s; α) :=
 +∞∑

k=KL ψ1
k(− ln s; α)s
kp+λ ∈ F ∞
L (U0).

If KL = 0 then the result follows taking ∆ ≡ 0. If, on the contrary, KL ∈ N then by Theorem 3.3 we know
that there exists ˆ∆(z, w; α) ∈ Q[z, w, α] with ˆ∆(0, 0; α) = 1 such that

KL−1∑

k=0 ψ1
k(− ln s; α)s
kp+λ = s
λ ˆ∆(s
p, s
pω; α),

18

where ω = ω(s; α1). By gathering the homogenous part of ˆ∆ of i-th degree, for i = 0, 1, . . . , ˆd := deg(z,w) ˆ∆,

it turns out that we can write s
λ ˆ∆(s
p, s
pω) = ∑ ˆd
i=0 s
λ+pipi(ω; α) where pi(w; α) ∈ Q[w, α] with degw pi ⩽ i.
Then, due to λ = p−α1
q and by (d) in Lemma A.4, note that s
λ+pipi(ω; α) ∈ F ∞
L (U0) provided that i > L
p − 1
q .
Consequently if L ⩾ p
q then there exists a unique polynomial ∆(z, w; α) ∈ Q[z, w, α] with ∆(0, 0; α) = 1
and deg(z,w) ∆ ⩽ ⌊ L
p − 1
q ⌋ =: d, such that

∆(z, w; α) =
 d∑

i=0 s
pipi(ω; α) and
 ˆd∑

i=d+1 s
λ+pipi(ω; α) ∈ F ∞
L (U0),

where, in case that ˆd ⩽ d, the second summation is void and we set pi ≡ 0 for i > ˆd. Hence the result
follows taking ∆ and ∑+∞
k=d+1 ψ1
k(− ln s; α)s
kp+λ instead of ˆ∆ and DL respectively. Observe on the other
hand that if L < p
q then s
λ ˆ∆(s
p, s
pω) = ∑d
i=0 s
λ+pipi(ω; α) ∈ F ∞
L (U0) and so in this case the result follows

taking ∆ ≡ 0 instead of ˆ∆. This concludes the proof of the result since the uniqueness of the polynomial ∆
in the statement follows from the fact that s
λ+piωℓ /∈ F ∞
L (U0) if i ⩽ d.

4 Dulac time

In this section we will prove Theorem B. To this aim, for the sake of convenience, we begin by introducing

Tijk(s; α) := ∫ − ln s

0 e(i−λj)tψj
k(t; α)dt, for i, j ∈ Z and k ∈ N, (23)

and in its regard we prove the following result.

Lemma 4.1. For each i, j ∈ Z and δ ∈ (0, 1
2 ] there exists k0 ∈ Z≥0 such that for all ν ∈ Z
N +1
≥0 and compact
set C ⊂ Uδ there exist Cν, Kν > 0 so that the upper bound

|∂νTijk(s; α)| ⩽ Kν(k + 1)3|ν|(Cν)k(− ln s)
|ν|s
λj−i−ν0−(3k+|ν|)δ

holds for all k ⩾ k0, s ∈ (0, 1/e) and α ∈ C.

Proof. The result follows by applying Lemma 2.7 to the given compact set C ⊂ Uδ and ν ∈ Z
N +1
≥0 . Denote
ν = (ν0, ν1, . . . , νN ) and suppose ﬁrst that ν0 = 0. In this case if s ∈ (0, 1/e) and α ∈ C then

|∂ν(Tijk(s; α)| ⩽ ∑

ℓ1+ℓ2=ν
 ( ν
ℓ1, ℓ2
) ∫ − ln s

0
 ∣
∣
∣∂ℓ1
α (e(i−λj)t)∂ℓ2
α ψj
k(t; α)
∣
∣
∣ dt

⩽ 2|ν| ˆKν(k + 1)3|ν|(Cν)
k ∫ − ln s

0 e(i−λj)t(jt/q)ℓ11 max(1, t)
|ℓ2|e(3k+|ℓ2|)δtdt

⩽ Kν(k + 1)3|ν|(Cν)
k(− ln s)|ν| ∫ − ln s

0 e
(i−λj+(3k+|ν|)δ)tdt

⩽ Kν(k + 1)3|ν|(Cν)
k(− ln s)|ν|s
λj−i−(3k+|ν|)δ,

where in the ﬁrst inequality we apply Theorem B.2, in the second one Lemma 2.7 and Remark B.3, in
the third one we set Kν := 2|ν|(j/q)
ν1 ˆKν and we use that max(1, t) ⩽ − ln s for all t ∈ (0, − ln s) due to
s ∈ (0, 1/e), and in the last one we take

k ⩾ k0 := max (0, ⌈ 1
3δ (1 − i + p+δ
q |j|)⌉) (24)

19

in order that i − λj + (3k + |ν|)δ) ⩾ 1 holds for all α ∈ Uδ and k ⩾ k0. Here we use that λ ∈ ( p−δ
q , p+δ
q ) due

to |α1| < δ and λ = p−α1
q . We stress, and this is crucial, that k0 is independent from ν and C. This proves
the result for ν0 = 0. Let us consider next the case ν0 ⩾ 1 and to this end we denote ν′ := (ν0 −1, ν1, . . . , νN ).
Thus, from (23) and Theorem B.2,

∂νTijk(s; α) = −s
−1∂ν′(s
λj−iψj
k(− ln s; α)) = −s
−1 ∑

ℓ1+ℓ2=ν′
 ( ν′

ℓ1, ℓ2
)
∂ℓ1(s
λj−i)∂ℓ2(ψj
k(− ln s; α)).

Then the application of Lemma 2.6 and Lemma 2.7 show respectively
∣
∣∂ℓ1 (s
λj−i)∣
∣ ⩽ Mℓ1(− ln s)
|ℓ1| max(1, |λj − i|)
|ℓ1|s
λj−i−ℓ10(|j|/q)ℓ10

and, since max(1, − ln s) = − ln s due to s ∈ (0, 1/e),
∣
∣
∣∂ℓ2 (ψj
k(− ln s; α))∣
∣
∣ ⩽ ˆKℓ2 (k + 1)3|ℓ2|( ˆCjℓ2 )
k(− ln s)
|ℓ2|s
−(3k+|ℓ2|)δ.

Setting ¯Kν := sup {
Mℓ1 ˆKℓ2 max(1, |λj − i|)|ℓ1|(|j|/q)ℓ10; α ∈ C, ℓ1 + ℓ2 = ν′} and Cν := max( ˆCjℓ2; ℓ2 ⩽ ν′),

we can assert that if s ∈ (0, 1/e) and α ∈ C then

|∂νTijk(s; α)| ⩽ 2
|ν|−1 ¯Kν(k + 1)3|ν|(Cν)
k(− ln s)|ν|s
λj−i−ν0−(3k+|ν|)δ.

Here we also take ℓ1 + ℓ2 = ν′ = ν − (1, 0, . . . , 0) and Remark B.3 into account. Consequently, setting k0 := 0
and Kν := 2
|ν|−1 ¯Kν, the result follows in case that ν0 ⩾ 1.

Recall at this point, see (2), that Theorem B concerns with the Dulac time associated to

Yα,β = 1

β0xmyn + uℓ ∑M
i=1 βiui−1 Xα,

where m, n, ℓ ∈ Z and u = xpyq with p, q ∈ N. For this reason, as an intermediate step, we next consider the
Dulac time Tij( · ; α) of 1
xiyj Xα for any i, j ∈ Z. In its regard the next statement explains the convenience
of introducing Tijk, see (23).

Proposition 4.2. For each compact set C ⊂ Uδ with δ ∈ (0, 1
4 ] there exists s0 > 0 such that the Dulac time
Tij( · ; α) of the vector ﬁeld 1
xiyj Xα, where i, j ∈ Z, writes as

Tij(s; α) =
 +∞∑

k=0 s
i+pkTijk(s; α) for all s ∈ (0, s0) and α ∈ C (25)

and the series is absolutely convergent. Moreover, for each L ∈ R there exists KL ∈ Z≥0 such that

+∞∑

k=KL s
i+pkTijk(s; α) ∈ F ∞
L (U0). (26)

Proof. Let t ↦→ (x(t, p0; α), y(t, p0; α)
) be the solution of Xα passing through p0 ∈ R2 at t = 0. Note that
if p0 = (s, 1) with s > 0 then x(t, p0; α) = se
t intersects the transversal section {x = 1} at t = − ln s. Thus
the time Tij(s; α) that spends the solution of 1
xiyj Xα starting at (s, 1) with s > 0 to reach the transversal
section {x = 1} is given by

Tij(s; α) = ∫ − ln s

0 (x(t, s, 1; α))i(y(t, s, 1; α))
jdt = ∫ − ln s

0 s
ie
(i−λj)t +∞∑

k=0 ψj
k(t; α)s
kpdt,

20

where in the second equality we apply Lemma 2.5. In this respect observe that, due to ∂tΩ(t, α1) = eα1t > 0,
for all t ∈ (0, − ln s) we have

s
p max ( M
2 Ω(t, α1), 2C0eδt) < s
p max ( M
2 Ω(t, α1), 2C0eδt)∣
∣t=− ln s = s
p max ( M
2 ω(s; α1), 2C0s
−δ) < 1,

provided that s > 0 is small enough because lims→0+ s
p−δ = 0 and, by (b) in Lemma A.4, s
pω(s; α1) tends
to zero as s → 0
+ uniformly on Uδ. Consequently, recall the deﬁnition in (23), the ﬁrst assertion in the
statement will follow by applying Lemma B.5 once we show that for each compact set C ⊂ Uδ with δ ∈ (0, 1
4 ]
there exists s0 > 0 such that

+∞∑

k=0
 ∫ − ln s

0 s
i+kpe(i−λj)t ∣
∣
∣ψj
k(t; α)
∣
∣
∣ dt < +∞ for all s ∈ (0, s0) and α ∈ C. (27)

With this aim let us note that, by applying Lemma 2.7 with |ν| = 0,

∫ − ln s

0 s
i+kpe(i−λj)t ∣
∣
∣ψj
k(t; α)∣
∣
∣ dt ⩽ K0(Cj0)ks
i+kp ∫ − ln s

0 e(i−λj+3kδ)tdt

= K0(Cj0)
ks
i+kp s
−(i−λj+3kδ) − 1
i − λj + 3kδ ⩽ K0(Cj0)
ks
k(p− 3
4 )+λj,

where in the last inequality we use that p − 3δ ⩾ 1
4 , due to δ ∈ (0, 1
4 ), and we take k large enough so that
i − λj + 3kδ ⩾ 1. Thus the above upper bound readily shows the validity of (27) taking s0 = (Cj0)
−1/(p− 3
4 )

because it guarantees that Cj0s
p− 3
4 < 1 for all s ∈ (0, s0).

With regard to the last assertion in the statement let us ﬁrst note that, by applying Theorem B.2,

∂ν (s
i+pkTijk(s; α)
) = ∑

ℓ1+ℓ2=ν
 ( ν
ℓ1, ℓ2
)
∂ℓ1(s
i+pk)∂ℓ2(Tijk(s; α)).

Accordingly, by Lemma 4.1, there exists k0 ∈ Z≥0 such that, for all ν ∈ Z
N +1
≥0 and compact set C ⊂ Uδ,

|∂ν(s
i+pkTijk(s; α))| ⩽ ∑

ℓ1+ℓ2=ν
( ν
ℓ1, ℓ2
)
Kℓ2 |i + kp|
ℓ10(k + 1)3|ℓ2|(Cℓ2 )
k(− ln s)
|ℓ2|s
λj+pk−ℓ10−ℓ20−(3k+|ν|)δ

provided that k ⩾ k0, s ∈ (0, 1
e ) and α ∈ C. Since |i + pk| ⩽ (k + 1)(|i| + p), setting ˆCν = max(Cℓ2; ℓ2 ⩽ ν)
and ˆKν := 2
|ν| max(Kℓ2(|i| + p)
ℓ10; ℓ1 + ℓ2 = ν), we can assert that if k ⩾ k0, s ∈ (0, 1/e) and α ∈ C then

|∂ν(s
i+pkTijk(s; α))| ⩽ ˆKν(k + 1)4|ν|( ˆCν)
k(− ln s)
|ν|s
λj+(p−3δ)k−ν0−|ν|δ (28)

⩽ ˆKν(k + 1)4|ν|( ˆCν)
k(− ln s)
|ν|s
γ+(k−|ν|)/4−ν0 =: mk(s),

where in the ﬁrst inequality we also take ℓ1 + ℓ2 = ν and Remark B.3 into account, and in the second one
we use that δ ∈ (0, 1
4 ), p ⩾ 1 and λj ⩾ − p+δ
q |j| =: γ. (Let us remark, it will be important later on when we
use the previous inequalities, that k0 is independent from ν and C.) On account of Remark 3.1, a suﬃcient
condition for s ↦→ mk(s) to be monotonous increasing on (0, 1/e) is that k > 9|ν| + 4(ν0 − γ), and for this
reason we set ¯kν := max (⌈5|ν| + 4(ν0 − γ)⌉ , k0) .

Note on the other hand that, due to

mk(s) = ˆKν( ˆCνs
1/4)k(k + 1)4|ν|(− ln s)
|ν|s
γ−|ν|/4−ν0,

21

if we set s0 := min(1/e, (2 ˆCν)
−4) then the series with general term Mk := mk(s0) is summable and, moreover,
thanks to the monotonicity of mk(s) on (0, 1/e),

|∂ν(s
i+pkTijk(s; α))| ⩽ mk(s) ⩽ Mk for all s ∈ (0, s0), α ∈ C and k ⩾ ¯kν.

Hence, thanks to the Weierstrass M-test, for each ν ∈ Z
N +1
≥0 the series ∑∞
k=0 ∂ν(s
i+pkTijk(s; α)) converges
uniformly for s ∈ (0, s0) and α ∈ C. Consequently, by applying recursively Lemma B.4 starting from (25),
we have that for each compact set C ⊂ Uδ and ν ∈ Z
N +1
≥0 there exists s0 > 0 small enough such that if
s ∈ (0, s0) and α ∈ C then

∂νTij(s; α) = ∂ν(+∞∑

k=0 s
i+pkTijk(s; α)

)
 =
 +∞∑

k=0 ∂ν(s
i+pkTijk(s; α)
) . (29)

We are now in position to ﬁnish the proof. Indeed, we claim that (26) holds taking

KL := max (k0, ⌈
4L + 4p+1
q |j|⌉ + 8) .

(Recall that k0 is the nonnegative integer given by Lemma 4.1, see (24), which is relevant for our purpose
because it guarantees the upper bound (28) for k ⩾ k0.) We point out that KL is independent from ν and C.
In order to show (26), recall Deﬁnition 1.2, we ﬁx any ν ∈ Z
N +1
≥0 and α⋆ = (0, α2, . . . , αN ) ∈ U0 = {0}×RN −1,
and we take a relatively compact neighbourhood V of α⋆ contained in Uδ with δ = min( 1
4 , 1
|ν| ). Then,
from (29) and using the upper bound in (28), for each s ∈ (0, s0) and α ∈ V we have
∣
∣
∣
∣
∣∂ν
s,α
 ( +∞∑

k=KL(s
i+pkTijk(s; α)
)∣
∣
∣
∣
∣ ⩽
 +∞∑

k=KL
 ∣
∣∂ν
s,α(s
i+pkTijk(s; α))
∣
∣

⩽ ˆKν(− ln s)
|ν|s
λj−|ν|δ−ν0 +∞∑

k=KL(k + 1)4|ν|( ˆCνs
p−3δ)
k

⩽ ˆKν ˆMνs
λj−|ν|δ−ν0−1A(KL + 1)4|ν|( ˆCν)
KL s
(p−3δ)KL

⩽ ˆKν ˆMνA(KL + 1)4|ν|( ˆCν)KLs
λj+ 1
4 KL−2−ν0 ⩽ Cs
L−ν0.

In the third inequality above we apply Lemma 3.2 and set ˆMν := sup{s(− ln s)
|ν|; s ∈ (0, s0)}. Next, in the
fourth inequality, we take δ = min( 1
4 , 1
|ν| ) and p ⩾ 1 into account. Finally in the last inequality we use the

deﬁnition of KL, which implies λj+ 1
4 KL−2 ⩾ L due to λ < p+δ
q , and we set C := ˆKν ˆMνA(KL+1)
4|ν|( ˆCν)
KL.
This completes the proof of the result.

Finally, and this will be the last ingredient for the proof of Theorem B, we next study the ﬁnite truncation
of the series given in (25). We will show that it can be written in terms of polynomials in s
p and s
pω.

Lemma 4.3. Consider i, j ∈ Z and K ∈ N and deﬁne

T K
ij (s; α) :=
 K−1∑

k=0 s
i+pkTijk(s; α).

Then, setting ω = ω(s; α1), the following holds:

(a) If iq − jp ̸= 0 then there exists τ K
ij (z, w; α) ∈ Q(α1)[z, w, α2, . . . , αN ], with degz,w(τ K
ij ) < K and not
having poles along α1 = 0, such that T K
ij (s) = s
λjτ K
ij (s
p, s
pω; α) − s
iτ K
ij (s
p, 0; α).

(b) If (i, j) = r(p, q) with r ∈ N then there exists ϱK
ij (z, w; α) ∈ Q[z, w, α], with degz,w(ϱK
ij ) < K + r and
ϱK
ij (z, 0; α) = 0, such that T K
ij (s) = ϱK
ij (s
p, s
pω; α).

22

Proof. By applying (a) in Lemma 2.1, from the deﬁnition in (16) we get the existence of a polynomial
Rj
k(z; α) ∈ Q[z, α] with degz(Rj
k) ⩽ k such that

ψj
k(t; α) = Rj
k(Ω(t; α1); α), where Ω(t; α) = eα1t−1
α1 .

Accordingly, from the deﬁnition in (23) and by performing the coordinate change w = Ω(t; α1), we get

Tijk(s; α) = ∫ − ln s

0 e(i−λj)tRj
k (Ω(t; α1); α) dt = ∫ ω(s;α1)

0 (1 + α1w)
 i−λj
α1 −1Rj
k(w; α)dw, (30)

where we use that Ω(− ln s; α1) = ω(s; α1) by deﬁnition. If i − λj|α1=0 ̸= 0, which is equivalent to pj−qi ̸= 0,
after integrating by parts k times we obtain

Tijk(s; α) = (1 + α1w)
 i−λj
α1
i − λj
 (

Rj
k(w; α) − ∂wRj
k(w; α)(1 + α1w)
i − λj + α1

+ ∂2
wRj
k(w; α)(1 + α1w)
2

(i − λj + α1)(i − λj + 2α1) + · · · + (−1)k∂k
wRj
k(w; α)(1 + α1w)k

(i − λj + α1) · · · (i − λj + kα1)
 )∣
∣
∣
∣
∣
ω(s;α1)

0 .

It is clear then that there exists a polynomial τijk(w; α) ∈ Q(α1)[w, α2, . . . , αN ], not having poles along
α1 = 0 and with degw(τijk) ⩽ k, such that we can write

s
i+kpTijk(s; α) = s
i+kp ((1 + α1ω)
 i−λj
α1 τijk(ω; α) − τijk(0; α)) = s
λj+kpτijk(ω; α) − τijk(0; α)s
i+kp,

where we set ω = ω(s; α1) for shortness and in the second equality we use that 1 + α1ω = s
−α1. On account
of this there exists ˆτijk(z, w; α) ∈ Q(α1)[z, w, α2, . . . , αN ], which is homogenous of degree k in z and w, such
that s
i+kpTijk(s; α) = s
λj ˆτijk (s
p, s
pω; α) − s
i ˆτijk(s
p, 0; α).

In view of this it is clear that the assertion in (a) follows taking τ K
ij := ∑K−1
k=0 ˆτijk. With regard to the one
in (b) we note that, since (p, q) = 1, the equality pj − qi = 0 holds if and only if there exists r ∈ Z such that
(i, j) = r(p, q). In this case, from (30), we deduce that

Tijk(s; α) = ∫ ω(s;α1)

0 (1 + α1w)
r−1Rj
k(w; α)dw.

If r ∈ N then Tijk(s; α) = ϱijk(ω; α) − ϱijk(0; α), where ϱijk(z; α) ∈ Q[z, α] with degz(ϱijk) ⩽ k + r. Hence
there exists ˆϱijk(z, w; α) ∈ Q[z, w, α], homogeneous of degree k + r in z and w, such that

s
i+kpTijk(s; α) = s
p(r+k)Tijk(s; α) = ˆϱijk (s
p, s
pω; α) − ˆϱijk(s
p, 0; α).

Since T K
ij (s; α) = ∑K−1
k=0 s
i+pkTijk(s; α), this shows that (b) follows taking

ϱK
ij (z, w; α) :=
 K−1∑

k=0 (ϱijk(z, w; α) − ϱijk(z, 0; α)) ,

which concludes the proof of the result.

We are now in position to prove our second main result.

23

Proof of Theorem B. Recall that the family of vector ﬁelds under consideration is given by

Yα,β = 1

β0xmyn + ∑M +ℓ−1
i=ℓ βi+1−ℓ ui Xα,

where ℓ ∈ Z is deﬁned in (1), u = xpyq, (p, q) = 1 and

Xα = x∂x + 1
q (−p + ∑N −1
i=0 αi+1u
i) y∂y.

Let us denote the solution of Xα passing through p0 ∈ R2 at t = 0 by t ↦→ (x(t, p0; α), y(t, p0; α)
). Then, if
p0 = (s, 1) with s > 0, x(t, p0; α) = se
t intersects the transversal section {x = 1} at t = − ln s. Consequently
the time T (s; α, β) that spends the solution of Yα,β starting at (s, 1) with s > 0 to reach the transversal
section {x = 1} is given by

T (s; α, β) = ∫ − ln s

0
 (

β0xmyn +
 M +ℓ−1∑

i=ℓ βi+1−ℓ(xpyq)
i)∣
∣
∣
∣
∣{x=x(t,s,1;α),y=y(t,s,1;α)} dt

= β0Tmn(s; α) +
 M +ℓ−1∑

i=ℓ βi+1−ℓTip,iq(s; α),

where Tij( · ; α) is the Dulac time of 1
xiyj Xα, which is precisely our concern in Proposition 4.2 and Lemma 4.3.
It is clear then that, by applying Proposition 4.2, for each compact set C ⊂ Uδ with δ ∈ (0, 1
4 ] there exists
s0 > 0 such that
 T (s; α, β) =
 +∞∑

k=0 s
kp (

β0s
mTmnk(s; α) +
 M +ℓ−1∑

i=ℓ βi+1−ℓs
ipTip,iq,k(s; α)

)

for all s ∈ (0, s0) and α ∈ C and the series is absolutely convergent. Furthermore we can assert that, for the
given L ∈ R, there exists KL ∈ Z≥0 such that

TL(s; α, β) :=
 +∞∑

k=KL s
kp (
β0s
mTmnk(s; α) +
 M +ℓ−1∑

i=ℓ βi+1−ℓs
ipTip,iq,k(s; α)

)
 ∈ F ∞
L (U0 × RM +1),

where U0 × RM +1 stands for the set {(α, β) ∈ RM +N +1; α1 = 0}. This assertion follows by taking (26) into
account and applying, in this order, (c), (b) (g) and (e) in Lemma A.3.

On the other hand, by Lemma 4.3, there exist τ0(z, w; α) ∈ Q(α1)[z, w, α2, . . . , αN ] without poles along
α1 = 0 and ϱi(z, w; α) ∈ Q[z, w, α] with ϱi(z, 0; α) = 0, i = 0, 1, . . . , M , such that such that setting

L0(s; α) :=
 



 s
λnτ0(s
p, s
pω; α) − s
mτ0(s
p, 0; α) if mq − np ̸= 0,

s
κpϱ0(s
p, s
pω; α) if mq − np = 0 and (m, n) ̸= (0, 0),

− ln s if (m, n) = (0, 0),

L1(s; α) :=
 { s
ℓpϱ1(s
p, s
pω; α) if ℓ > 0,
− ln s if ℓ = 0,

and
 Li(s; α) :=s
(ℓ+i−1)pϱi(s
p, s
pω; α), for i = 2, 3, . . . , M,

24

then
 T L(s; α, β) :=
 KL−1∑

k=0 s
kp (
β0s
mTmnk(s; α) +
 M +ℓ−1∑

i=ℓ βi+1−ℓs
ipTip,iq,k(s; α)

)

=β0L0(s; α) + β1L1(s; α) +
 M∑

i=2 βiLi(s; α). (31)

With regard to the cases considered in the deﬁnition of L0, let us note that if mq − np = 0 then, due to
(p, q) = 1, there exists η ∈ Z such that (m, n) = η(p, q). Thus, by assumption, η = κ := ⌈max ( m
p , n
q )⌉ ⩾ 0
and hence, on account of Deﬁnition 1, ℓ = η + 1 > 0. (In particular, if mq − np = 0 and (m, n) ̸= (0, 0)
then η = κ ∈ N, and so the assertion with respect to L0 follows by (b) in Lemma 4.3.) If, on the contrary,
mq − np ̸= 0 then, by Deﬁnition 1 again, ℓ = κ ⩾ 0. Note also that if (i, j) = (0, 0) then Tij(s; α) = − ln s,
which yields to the subcases (m, n) = (0, 0) and ℓ = 0 in L0 and L1, respectively. In this respect,
L0(s; α) = − ln s in case that (m, n) = (0, 0), which implies ℓ ⩾ 1, and then, L1(s; α) ̸= − ln s. On the
other hand, L1(s; α) = − ln s in case that ℓ = 0, which implies mq − np ̸= 0 due to (1) and the assumption
κ ⩾ 0. Accordingly, in this case, L0(s; α) ̸= − ln s.

Taking the previous considerations into account, the assertions with respect to T L follow from (31).
This concludes the proof of the result.

A Results about the class F K
L (W )

The present section is devoted to show a number of general properties about the class F K
L (W ). We ﬁrst
prove that any g(s; µ) ∈ F K
L (W ) extends to a ﬁnitely smooth function (on s and the parameter µ) along
s = 0. (This applies in particular to the remainder DL in Theorem A, as well as to TL in Theorem B.) On
the contrary, we will provide an example showing that a function g(s; µ) verifying the estimates in (4) but
only with respect to the s derivative (i.e., with ν1 = . . . = νN = 0) may not have an extension along s = 0
which is C L on s and the parameter µ (see Example A.2).

Lemma A.1. Let U be an open set of RN , K ∈ Z≥0 and g(s; µ) ∈ C K
s>0(U ) such that, for some W ⊂ U and
L ∈ R, g(s; µ) ∈ F K
L (W ). If L > K then g extends to a C K-function ˆg, deﬁned in some open neighbourhood
of {0} × W in RN +1, and satisfying ∂ν ˆg(0; µ) = 0 for all µ ∈ W and ν ∈ Z
N +1
≥0 with |ν| ⩽ K.

Proof. Due to g(s; µ) ∈ C K
s>0(U ), by deﬁnition there exists an open neighbourhood V of {0} × U in RN +1

such that (s, µ) ↦→ g(s; µ) is C K on V+ := V ∩ ((0, +∞) × U ). Then the function

ˆg(s; µ) := { g(|s|; µ) if s ̸= 0 and (|s|, µ) ∈ V+,
0 if s = 0 and µ ∈ U ,

is well deﬁned on {(s, µ) ∈ RN +1; (|s|, µ) ∈ V+} ∪ ({0} × U ), which is an open neighbourhood of {0} × U in
RN +1. Moreover, for ν = (ν0, ν1, . . . , νN ) ∈ Z
N +1
≥0 with |ν| ⩽ K, it is easy to show (by induction on ν0) that

∂ν ˆg(s; µ) = sgn(s)
ν0∂νg(|s|; µ) for s ̸= 0 with (|s|, µ) ∈ V+. (32)

Next we ﬁx any ˆµ ∈ W . Then, due to g(s; µ) ∈ F K
L (ˆµ), by deﬁnition there exist s0, ε, C > 0 such that, for
each ν ∈ Z
N +1
≥0 with |ν| ⩽ K,

|∂νg(s; µ)| ⩽ Cs
L−ν0 for all s ∈ (0, s0) and ∥µ − ˆµ∥ < ε. (33)

We claim that ˆg(s; µ) is of class C K in a neighbourhood of (0, ˆµ) and that ∂ν ˆg(0; ˆµ) = 0 for all ν ∈ Z
N +1
≥0
with |ν| ⩽ K. Since ˆµ is arbitrary and, on account of (32), ˆg is C K on {
(s, µ) ∈ RN +1; (|s|, µ) ∈ V+}, the

25

result will follow once we prove the claim. To prove it we will show by induction on ν0 that if |ν| ⩽ K
then |∂ν ˆg(s; µ)| ⩽ C|s|
L−ν0 for all (s, µ) with s ∈ (−s0, s0) and ∥µ − ˆµ∥ < ε. (This will imply that ∂ν ˆg is
continuous and vanishes at any (0, µ) with ∥µ − ˆµ∥ < ε.) Denote ¯ν = (ν1, ν2, . . . , νN ) ∈ Z
N
≥0 for shortness
so that ν = (ν0, ¯ν). The base case ν0 = 0 is clear because, taking (32) and ˆg(0; µ) = 0 into account,

∂(0;¯ν)ˆg(s; µ) = { ∂(0;¯ν)g(|s|; µ) if s ̸= 0,
0 if s = 0,

that has absolute value smaller than C|s|
L if ∥µ− ˆµ∥ < ε and s ∈ (−s0, s0) thanks to (33) and ∂(0;¯ν)ˆg(0; µ) =
0. Let us take next any ν0 ⩾ 1 and show the inductive step. Then, by using (32) and that ∂(ν0−1,¯ν)ˆg(0; µ) = 0
due to the induction hypothesis, we get

∂ν ˆg(s; µ) =
 



 sgn(s)ν0∂νg(|s|; µ) if s ̸= 0,

lim
z→0
 ∂(ν0−1,¯ν) ˆg(z,µ)
z if s = 0.

Therefore |∂ν ˆg(s; µ)| = |sgn(s)ν0∂νg(|s|; µ)| ⩽ C|s|
L−ν0 in case that 0 < |s| < s0, thanks to (33), whereas

∂ν ˆg(0; µ) = 0 because the induction hypothesis implies ∣
∣
∣ ∂(ν0 −1,¯ν) ˆg(z,µ)
z ∣
∣
∣ ⩽ C|z|
L−ν0+1

|z| = C|z|
L−ν0, which

tends to zero as z → 0 due to L > K ⩾ |ν| ⩾ ν0. Accordingly |∂ν ˆg(s; µ)| ⩽ C|s|
L−ν0 for all (s, µ) with
s ∈ (−s0, s0) and ∥µ − ˆµ∥ < ε, and this proves the induction step. Consequently the claim is true and the
result follows.

Example A.2. With regard to the previous result we now exhibit a C ∞ function g(s; µ) on (0, +∞) × R
verifying |∂i
sg(s; µ)| ⩽ Cs
L−i for all s > 0, µ ∈ R and i = 0, 1, . . . , L, but such that ∂µg(s; µ) does not have
a continuous extension along s = 0.

Let us begin by taking a C ∞ bump function ϕ : R −→ [0, +∞) deﬁned by ϕ(x) = exp(−x
2/(x
2 − 1)2) if
|x| ⩽ 1 and zero otherwise. Let us ﬁx besides any α ∈ (0, 1) and deﬁne β = 1+α
2 . Then, for each k ∈ Z≥0,
deﬁne Ek := {(s, µ) ∈ R2; pk(s, µ) ⩽ 1} where

pk(s, µ) := ( 2(s − βαk)
αk(1 − β)
 )2 + ( µ
α(L+1)k
 )2 .

The sets Ek, k ∈ Z≥0, are pairwise disjoint and, furthermore, every (s, µ) ̸= (0, 0) has an open neighbourhood
that intersects at most one Ek. This shows that

g(s; µ) :=
 +∞∑

k=0 αLkϕ(pk(s, µ))

is a well deﬁned C ∞ function on R2\{(0, 0)}. For the same reason we can commute derivation and summation
and then, by applying Theorem B.1,

∂n
s g(s; µ) =
 +∞∑

k=0 αLk n∑

j=1 ϕ
(j)(pk(s; µ)) ∑

r1,...,rn n!
 n∏

i=1
 (∂i
spk(s, µ)
)ri

ri!(i!)ri , for all (s, µ) ̸= (0, 0),

where the third summation is subject to the coupling conditions ∑n
i=1 ri = j and ∑n
i=1 iri = n. Observe

that ∂i
spk(s, µ) = 2 ( 2(s−βαk)
αk(1−β) )2−i ( 2
αk(1−β) )i for i = 1, 2 and zero for i ⩾ 3. Thus, if (s, µ) ∈ Ek then

|∂i
spk(s, µ)| ⩽ 2 ( 2
αk(1−β) )i for all i ∈ N. Consequently, if (s, µ) ∈ Ek0 and n ∈ N then we get

|∂n
s g(s, µ)| ⩽ C ′αLk0 n∏

i=1
(α−k0)
iri = C ′αk0(L−n) ⩽ Cα(k0+1)(L−n) ⩽ Cs
L−n,

26

where C ′ is a positive constant (depending on n, α and ∥ϕ
(j)∥, j = 1, 2, . . . , n), C := C ′αn−L and we use use
that s ∈ [αk0+1, αk0]. The same inequality is valid for n = 0 since |g(s; µ)| ⩽ αLk0 = α−LαL(k0+1) ⩽ α−Ls
L.
Accordingly g veriﬁes the desired bounds with respect to the s derivatives.

The sequence of points (si, µi) := (βαi, 2
−1/2αLi) ∈ Ei tends to (0, 0) as i → ∞ and, on the other hand,
an easy computations gives
 |∂µg(si; µi)| = αLi|∂µϕ(pi(si, µi))| = α−i|ϕ
′(1/2)|,

which tends to +∞ as i → ∞. This shows that ∂µg(s; µ) does not have a continuous extension at (0, 0). □

Next result gathers some general properties with regard to operations between functions in F K
L (W ) with
K ∈ Z≥0 ∪ {∞} and L ∈ R. Let us point out that the inclusions in (b) and (c) must be thought with the
natural identiﬁcation of functions on RM to functions on RM × RM ′ via the projection RM × RM ′ → RM .

Lemma A.3. Let U and U ′ be open sets of RN and RN ′ respectively and consider W ⊂ U and W ′ ⊂ U ′.
Then the following holds:

(a) F K
L (W ) ⊂ F K
L ( ˆW ) for any ˆW ⊂ W and ⋂
n F K
L (Wn) = F K
L (
⋃
n Wn).

(b) F K
L (W ) ⊂ F K
L (W × W ′)

(c) C K(U ) ⊂ C K
s=0(U ) ⊂ F K
0 (W ).

(d) If K ⩾ K ′ and L ⩾ L
′ then F K
L (W ) ⊂ F K′
L′ (W ).

(e) F K
L (W ) is closed under addition.

(f ) If f ∈ F K
L (W ) and ν ∈ Z
N +1
≥0 with |ν| ⩽ K then ∂νf ∈ F K−|ν|
L−ν0 (W ).

(g) F K
L (W ) · F K
L′ (W ) ⊂ F K
L+L′(W ).

(h) Assume that φ : U ′ −→ U is a C K function with φ(W ′) ⊂ W and let us take g ∈ F K
L′ (W ′) with L
′ > 0
and verifying g(s; η) > 0 for all η ∈ W ′ and s > 0 small enough. Consider also any f ∈ F K
L (W ). Then
h(s; η) := f (g(s; η); φ(η)) is a well-deﬁned function that belongs to F K
LL′(W ′).

Proof. Let us begin by showing (g) since the previous assertions are straightforward. Take f (s; µ) ∈ F K
L (W )
and g(s; µ) ∈ F K
L′ (W ) and ﬁx ˆµ ∈ W and ˆν ∈ Z
N +1
≥0 with |ˆν| ⩽ K. Then, by deﬁnition, it follows that there
exist a neighbourhood V of ˆµ and C, s0 > 0 such that |∂νf (s; µ)| ⩽ Cs
L−ν0 and |∂νg(s; µ)| ⩽ Cs
L′−ν0 for
all µ ∈ V , s ∈ (0, s0) and ν ∈ Z
N +1
≥0 with |ν| ⩽ |ˆν|. Thus, by applying Leibniz’s rule (see Theorem B.2), if
µ ∈ V and s ∈ (0, s0) then

∣
∣∂ ˆν(f (s; µ)g(s; µ)
)∣
∣ ⩽ ∑

ν1+ν2=ˆν
 ( ˆν
ν1, ν2
)|∂ν1 f (s; µ)| |∂ν2 g(s; µ)| ⩽ ˆCs
L+L′−ˆν0 ,

where we use that ν10 + ν20 = ˆν0 and set ˆC := C 2 ∑

ν1+ν2=ˆν ( ˆν
ν1,ν2) = C 22
|ˆν|. Thus f g ∈ F K
L+L′(W ).

Let us turn next to show the assertion in (h). To this end ﬁx any ˆν ∈ Z
N ′+1
≥0 and ˆη ∈ U ′ ⊂ RN ′. Then, by
deﬁnition, it follows that there exist a neighbourhood V ′ of ˆη and C ′, s1 > 0 such that |∂νg(s; η)| ⩽ C ′s
L
′−ν0

for all η ∈ V ′, s ∈ (0, s1) and ν ∈ Z
N ′+1
≥0 with |ν| ⩽ |ˆν|. On the other hand, there exist a neighbourhood V
of ˆµ := φ(ˆη) ∈ U ⊂ RN and C, s2 > 0 such that |∂νf (s; µ)| ⩽ Cs
L−ν0 for all µ ∈ V , s ∈ (0, s2) and
ν ∈ Z
N +1
≥0 with |ν| ⩽ |ˆν|. Consider now a relatively compact neighbourhood V ′′ of ˆη with V ′′ ⊂ V ′ and
φ(V ′′) ⊂ V. Then, on account of L
′ > 0, there exists s3 ∈ (0, s1) such that g(s; η) ∈ (0, s2) for all s ∈ (0, s3)

27

and η ∈ V ′′. The application of Faà di Bruno formula (see Theorem B.1) to compute the derivative of
h(s; η) = f (g(s; η); φ(η)) yields

∂ ˆνh(s; η) = ∑

1⩽|λ|⩽|ˆν| ∂λf (u; µ)
∣
∣{u=g(s;η),µ=φ(η)} ∑

p(ˆν,λ)
(ˆν!)
 q∏

i=1 Ckiℓi(∂ℓig(s, η))ki0 N∏

j=1(∂ℓi φi(η))kij .

Here we set Ckiℓi := 1
ki!(ℓi!)|ki| and q := −1 + ∏N ′

i=0(ˆνi + 1) for shortness. Note that the vectors λ, ki ∈ Z
N +1
≥0
and ℓi ∈ Z
N ′+1
≥0 are subject to the coupling conditions ∑q
i=1 ki = λ and ∑q
i=1 |ki|ℓi = ˆν. So if we deﬁne

C 1
kℓ := ∏q
i=1 Ckiℓi and C 2
kℓ := sup {∏q
i=1 ∏N
j=1 |∂ℓiφi(η)|
kij ; η ∈ V ′′} and we take any s ∈ (0, s3) and η ∈ V ′′,

|∂ ˆνh(s; η)| ⩽ ∑

1⩽|λ|⩽|ˆν| Cg(s; η)L−λ0 ∑

p(ˆν,λ)
(ˆν!)C 1
kℓC 2
kℓ
 q∏

i=1
(C ′s
L′−ℓi0)
ki0

= ∑

1⩽|λ|⩽|ˆν| Cg(s; η)L−λ0 ∑

p(ˆν,λ) C 3
kℓs
∑q
i=1(L′−ℓi0)ki0

⩽ ∑

1⩽|λ|⩽|ˆν| C(C ′s
L′)
L−λ0 ∑

p(ˆν,λ) C 3
kℓs
L′λ0−ˆν0

where we set C 3
kℓ := (ˆν!)C 1
kℓC 2
kℓ ∏q
i=1(C ′)
ki0 = (ˆν!)C 1
kℓC 2
kℓ(C ′)
λ0 and we use that ∑q
i=1 ki0ℓi0 ⩽ ˆν0. Con-
sequently, setting ˆC := ∑
1⩽|λ|⩽|ˆν| C(C ′)L−λ0 ∑

p(ˆν,λ) C 3
kℓ, this shows that |∂ ˆνh(s; η)| ⩽ ˆCs
LL′−ˆν0 for all
s ∈ (0, s3) and η ∈ V ′′, which proves the validity of (h). This completes the proof of the result.

Next result gathers some interesting properties of the Ecalle-Roussarie compensator that will be used in
this (and a subsequent) paper. In the statement we use the notation x+ := max(x, 0) and x− := max(−x, 0)
for, respectively, the positive and negative part of a given x ∈ R. Note in particular that then x = x+ − x−

and |x| = x+ + x−.

Lemma A.4. The following assertions hold:

(a) For each compact set I ⊂ R and ν ∈ Z
2
≥0 there exists a constant C > 0 such that

|∂νω(s; α)| ⩽ Cs
−α
+−ν0| ln s|
|ν|+1for all α ∈ I and s ∈ (0, 1/e).

Moreover lims→0+ 1
ω(s;α) = α− uniformly on α ∈ R so that, in particular, lim(s,α)→(0+,0) 1
ω(s;α) = 0.

(b) For each ε > 0, (s, α) ↦→ ω(s; α) belongs to F ∞
−ε({α < ε}) and (s; α) ↦→ 1
ω(s;α) belongs to F ∞
−ε(R).

(c) For each L ∈ R and ℓ ∈ Z, (s, α, β) ↦→ s
βωℓ(s; α) belongs to F ∞
L ({(α, β) ∈ R2 ; β > L + ℓ
+α+}).

(d) If p(z; µ) ∈ C K(U )[z, z−1], where U is some open set of RN , then the function (s, α, β, µ) ↦→ s
βp(ω(s; α); µ)
belongs to F K
L ({(α, β, µ) ∈ R2 × U ; α = 0, β > L}).

Proof. For the sake of convenience we prove ﬁrst the assertion (c) for ℓ = 0. To this end we apply Lemma 2.6,
which shows that for each i, j ∈ Z≥0 there exists M > 0 so that, for every s ∈ (0, 1/e),

|∂i
s∂j
βs
β| ⩽ M s
β−i max(| ln s|, |β|)
i+j = M sL−is
β−L max(| ln s|, |β|)
i+j. (34)

Let us ﬁx ˆβ ∈ R with ˆβ > L and take a compact neighborhood I of ˆβ such that β − L > 0 for all β ∈ I. Thus
C := M sup {s
β−L max(| ln s|, |β|)
i+j; β ∈ I, s ∈ (0, 1/ε)
} is ﬁnite and so, from (34), |∂i
s∂j
βs
β| ⩽ Cs
L−i for all

28

s ∈ (0, 1/e) and β ∈ I. Hence s
β belongs to F ∞
L ({β > L}), which is a subset of F ∞
L ({(α, β) ∈ R2; β > L})
by (b) in Lemma A.3.

We show next the validity of the inequality in (a). Take ν = (ν0, ν1) ∈ Z
2
≥0 and a compact set I of R
and let us consider ﬁrst the case ν0 > 0. Then, if α ∈ I and s ∈ (0, 1/e),

|∂νω(s; α)| = |∂(ν0−1,ν1)s
−α−1| ⩽ M s−α−ν0 max(| ln s|, |α + 1|)
|ν|−1

⩽ Cs
−α−ν0| ln s||ν|−1 ⩽ Cs
−α+−ν0| ln s||ν|+1,

where the ﬁrst inequality follows from (34) taking i = ν0 − 1, j = ν1 and β = −α − 1, and the second one
setting C := M max(1, sup{|α + 1|; α ∈ I})
|ν|−1 and using previously that max(a, b) ⩽ a max(1, b) for any
a ⩾ 1 and b ⩾ 0. In order to prove the same inequality for ν0 = 0 note that ω(s; α) = F (α ln s) ln s with
F (x) := e−x−1
x and so, in this case, ∂νω(s; α) = ∂ν1
α (F (α ln s) ln s) = (ln s)
ν1+1F (ν1)(α ln s). We claim that

|F (n)(x)| ⩽ ex− for all x ∈ R and n ∈ Z≥0.

In this respect observe that, due to x−|x=α ln s = max(−α ln s, 0) = − ln s max(α, 0) = ln(s
−α+), the claim
will imply |∂νω(s; α)| ⩽ s
−α+| ln s|ν1+1 = s
−α
+−ν0| ln s|
|ν|+1 for all s ∈ (0, 1/e) and α ∈ R and, consequently,
the validity of the inequality in (a) for ν0 = 0 as well. To prove the claim we note that F is an entire function
which, diﬀerentiating term by term its Taylor’s series at x = 0, veriﬁes

F (n)(x) = −
 +∞∑

r=n
 (−1)n(−x)
r−n

(r − n)!(r + 1) = (−1)n+1 +∞∑

k=0
 (−x)
k

k!(k + n + 1) for all x ∈ R.

Hence, on account of 1
k+n+1 ⩽ 1, we get |F (n)(x)| ⩽ e|x| for all x ∈ R. In its turn this implies the claim for
x ⩽ 0 because, in this case, x− = |x|. The proof of the claim for x ⩾ 0 is a little more involved. We must

show that ∣
∣
∣∂n
x ( e−x−1
−x )∣
∣
∣ ⩽ 1 for all x ⩾ 0, and it is clear that this will follow once we prove that

0 < ∂n
x
 ( ex − 1
x
 ) ⩽ 1 for all x ⩽ 0. (35)

To prove these two inequalities we ﬁrst check by induction on n ∈ Z≥0 that

∂n
x
 ( ex − 1
x
 ) = e
xn!
 +∞∑

k=0
 (−x)
k

(k + n + 1)! ,

which is valid for all x ∈ R because x ↦→ ex−1
x is an entire function. Hence, for any n ∈ Z≥0, we can assert
that ∂n
x ( ex−1
x ) > 0 for all x ⩽ 0. In particular this implies ∂n−1
x ( ex−1
x ) ⩽ ∂n−1
x ( ex−1
x ) ∣
∣x=0 = 1
n ⩽ 1 for all
x ⩽ 0 and n ∈ N. Thus both inequalities in (35) are true and so the claim follows for x ⩾ 0 as well.

Let us prove now that lims→0+ 1
ω(s;α) = α− uniformly on α ∈ R. By distinguishing the cases α < 0,
α = 0 and α > 0, one can check that 1
ω(s;α) − α− = 1
ω(s;|α|) , which is strictly positive in case that s ∈ (0, 1)

due to ω(s; α) = ∫ 1
s x−α−1dx. Accordingly, for each given ε > 0 we must ﬁnd s0 ∈ (0, 1) small enough such
that if s ∈ (0, s0) then ∣
∣
∣
∣ 1
ω(s; α) − α−∣
∣
∣
∣ = 1
ω(s; |α|) < ε for all α ∈ R. (36)

If α ̸= 0 then 1
ω(s;|α|) = |α|
s−|α|−1 . So, in this case, the above inequality holds if and only if s < (1 + |α|/ε)−1/|α| .
In this regard note that, for every ε > 0 and α ∈ R,

e− 1
ε = lim
α→0
 (1 + |α|
ε
 )− 1
|α| ⩽ (1 + |α|
ε
 )− 1
|α|

29

because the function x ↦→ (1 + x
ε )−1/x is increasing on (0, +∞) for every ε > 0. Hence this shows that, for
α ̸= 0, the inequality in (36) follows taking s0 = e−1/ε. This is also true for α = 0 because in this case the
inequality in (36) simply writes as − 1
ln s < ε. Thus lims→0+ 1
ω(s;α) = α− uniformly on α ∈ R, as desired.

We turn next to the proof of the two assertions in (b). To show the ﬁrst one we consider the given ε > 0
and any ˆα < ε, and we take a compact neighbourhood I of ˆα such that α < ε for all α ∈ I. Then, by
applying (a), for each ν ∈ Z
2
≥0 there exists C > 0 such that

|∂νω(s; α)| ⩽ Cs
−ε−ν0s
ε−α
+| ln s|
|ν|+1 for all α ∈ I and s ∈ (0, 1/e).

Thus, since α+ < ε if and only if α < ε, taking ˆC := C sup{s
ε−α+| ln s||ν|+1; s ∈ (0, 1/e), α ∈ I}, from
the previous estimate we get |∂νω(s; α)| ⩽ ˆCs
−ε−ν0 for all s ∈ (0, 1/e) and α ∈ I. This proves that
ω(s; α) ∈ F ∞
−ε({α < ε}), as desired. Let us prove next that 1
ω(s;α) ∈ F ∞
−ε(R) for all ε > 0. So consider any
ˆα ∈ R and take a compact neighbourhood I of ˆα. Theorem B.1 shows that, for any ν ∈ Z
2
≥0 with |ν| ⩾ 1,

∂ν ( 1
ω(s; α)
 ) =
 |ν|∑

n=1
(−1)nn!(ω(s; α))−1−n ∑

p(ν,n) ν!
 q∏

i=1 Ckiℓi(∂ℓiω(s; α))ki,

with Ckiℓi = 1
ki!(ℓi)|ki| and q = (ν0 +1)(ν1 +1)−1, and where the second summation is multidimensional and

subject to the coupling conditions ∑q
i=1 ki = n and ∑q
i=1 ℓiki = ν. On account of this and the inequality
in (a) there exists C ′ > 0 such that ∏q
i=1 |∂ℓiω(s; α)|
ki ⩽ C ′s
−nα
+−ν0 | ln s|
n+|ν| for all α ∈ I and s ∈ (0, 1/ε).
Consequently, taking s
−α
+ = max(1, s
−α) = max(1, 1 + αω(s; α)) also into account, we can assert that there
exist suitable positive constants C ′′ and C such that if s ∈ (0, 1/e) and α ∈ I then

∣
∣
∣
∣∂ν ( 1
ω(s; α)
 )∣
∣
∣
∣ ⩽ C ′′s
−ε−ν0 |ν|∑

n=1
 max(1, 1 + αω(s; α))n

ω(s; α)n+1 s
ε| ln s|
n+|ν| ⩽ Cs
−ε−ν0,

where in the second inequality we also use that, by applying (a), lims→0+ 1
ω(s;α) = α− uniformly on α ∈ R.

Observe that, by the same reason, lims→0+ sε
ω(s;α) = 0 uniformly for α ∈ I, which implies that the above
inequality holds for |ν| = 0 as well. This proves that the function 1
ω(s;α) belongs to F ∞
−ε(R) for any ε > 0.

With regard to the assertion in (c) recall that the case ℓ = 0 is already proved. Here, for the sake of
shortness in the exposition, we shall use the Heaviside step function H(ℓ), which is deﬁned by H(ℓ) = 0 if
ℓ < 0 and H(ℓ) = 1 if ℓ > 0. By applying (b) together with Lemma A.3, and distinguishing the cases ℓ < 0
and ℓ > 0, it can be easily checked that

ωℓ(s; α) ∈ F ∞
−|ℓ|ε({α ∈ R; H(ℓ)α < ε}
) ⊂ F ∞
−|ℓ|ε({(α, β) ∈ R2; H(ℓ)α < ε, β > L}).

Similarly, but applying (c) with ℓ = 0, we get

s
β ∈ F ∞
L ({β > L}
) ⊂ F ∞
L ({(α, β) ∈ R2; H(ℓ)α < ε, β > L}
).

Consequently, by (g) in Lemma A.3,

s
βωℓ(s; α) ∈ F ∞
L−|ℓ|ε({(α, β) ∈ R2; H(ℓ)α < ε, β > L}) for all L ∈ R and ε > 0.

Hence s
βωℓ(s; α) ∈ F ∞
L ({(α, β) ∈ R2; H(ℓ)α < ε, β > L + |ℓ|ε}
) for all L ∈ R and ε > 0. Thus, by (a) in
Lemma A.3, the function (s, α, β) ↦→ s
βωℓ(s; α) belongs to

⋂

ε>0 F ∞
L ({(α, β) ∈ R2; H(ℓ)α < ε, β > L + |ℓ|ε}
) = F ∞
L
 ( ⋃

ε>0
 {
(α, β) ∈ R2; H(ℓ)α < ε, β > L + |ℓ|ε}
)

= F ∞
L ({(α, β) ∈ R2; β > L + ℓ+α+}
),

30

where once again the second equality follows by distinguishing the cases ℓ > 0 and ℓ < 0. This proves
assertion (c) for ℓ ̸= 0. Finally assertion (d) follows by applying (c) in the present result and, in this order,
(c), (b), (g) and (e) in Lemma A.3. This concludes the proof of the result.

Next we introduce the set of functions IK(W ) that we previously used in [8, 9, 11, 12] to describe the
properties of the remainder TL of the Dulac time. In this respect let us quote that Mourtada uses essentially
the same deﬁnition in his study of the cyclicity of the hyperbolic polycycles (see for instance [13]). This
set of functions is not used in the present paper and our aim is only to relate it with the set F L
K(W ) for
completeness and reader’s convenience.

Deﬁnition A.5. Consider K ∈ Z≥0 ∪ {+∞} and an open subset U of RN . Let D := s∂s be the Euler
operator and consider some ˆµ ∈ U . We say that ψ(s; µ) ∈ C K
s>0(U ) belongs to the class IK(ˆµ) if for each
k = 0, 1, . . . , K there exists a neighbourhood V of ˆµ such that

lim
s→0+ D kψ(s; µ) = 0 uniformly on µ ∈ V .

If W is a (not necesarily open) subset of U then we deﬁne IK(W ) = ⋂
ˆµ∈W IK(ˆµ). □

The following result shows that the remainder DL in Theorem A and TL in Theorem B can be written
in terms of the class Ik(W ), which is more suitable in order to perform the derivation-division algorithm.

Lemma A.6. Let U be an open set of RN , W ⊂ U, L ∈ R, K ∈ Z≥0 ∪ {+∞} and ε > 0. Then the inclusion
F K
L+ε(W ) ⊂ s
LIK(W ) holds.

Proof. Clearly it suﬃces to show that F K
L+ε(ˆµ) ⊂ s
LIK(ˆµ) for any ˆµ ∈ W because then, by deﬁnition,

F K
L+ε(W ) = ⋂

ˆµ∈W F K
L+ε(ˆµ) ⊂ ⋂

ˆµ∈W s
LIK(ˆµ) ⊂ s
L ⋂

ˆµ∈W IK(ˆµ) = s
LIK(W ).

So ﬁx ˆµ ∈ W and let us show that F K
L+ε(ˆµ) ⊂ s
LIK(ˆµ). To this end we note that one can easily verify by
induction that for all k ∈ Z≥0 there exist ηik ∈ Z≥0, i = 0, 1, . . . , k, such that the identity

D kg(s; µ) =
 k∑

i=0 ηiks
i∂i
sg(s; µ)

holds for any C k-function g. On the other hand, if ψ ∈ F K
L+ε(ˆµ) then for each i = 0, 1, . . . , K there exist a
neighbourhood Vi of ˆµ and Ci, si > 0 such that |∂i
sψ(s; µ)| ⩽ Cis
L+ε−i for all s ∈ (0, si) and µ ∈ Vi. Thus,
setting ¯Vk := ∩
k
i=0Vi, ˆsk := min(si; i = 0, . . . , k) and ˆCk := ∑k
i=0 ηikCi, by applying the above identity we
get that if k = 0, 1, . . . , K then

|D kψ(s; µ)| ⩽
 k∑

i=0 ηiks
i|∂i
sψ(s; µ)| ⩽
 ( k∑

i=0 ηikCi
)
 s
L+ε = ˆCks
L+ε for all s ∈ (0, ˆsk) and µ ∈ ¯Vk.

Taking this into account, since

D i (s
−Lψ(s; µ)
) =
 i∑

k=0
 ( i
k
)D i−k(s
−L)D kψ(s; µ) =
 i∑

k=0
 ( i
k
)(−L)
i−ks
−LD kψ(s; µ),

we can assert that

∣
∣D i (s
−Lψ(s; µ)
)∣
∣ ⩽
 i∑

k=0
 ( i
k
)|L|i−k ˆCks
ε = ˜Cis
ε for all s ∈ (0, ˜si) and µ ∈ ˜Vi,

31

where ˜Vi := ∩
i
k=0 ¯Vk, ˜si := min(ˆsk; k = 0, . . . , i) and ˜Ci := ∑i
k=0 ( i
k)|L|
i−k ˆCk. It is clear that the above upper
bound implies that lims→0+ D i (s
−Lψ(s; µ)) = 0 uniformly on µ ∈ ˜Vi for i = 0, 1, . . . , K, which implies
s
−Lψ(s; µ) ∈ IK(ˆµ), as desired. This proves the validity of the result.

Corollary A.7. For each ℓ ∈ Z, (s, α, β) ↦→ s
βωℓ(s; α) belongs to s
LI∞({(α, β) ∈ R2; β > L + ℓ
+α+}) for
all L ∈ R.

Proof. The result follows by noting that

s
βωℓ(s; α) ∈ ⋂

ε>0 F ∞
L+ε({(α, β) ∈ R2; β > L + ε + ℓ
+α+}) ⊂ ⋂

ε>0 s
LI∞({(α, β) ∈ R2; β > L + ε + ℓ
+α+}
)

= s
LI∞
( ⋃

ε>0
 {
(α, β) ∈ R2; β > L + ε + ℓ
+α+}
)
 = s
LI∞({(α, β) ∈ R2; β > L + ℓ
+α+}),

where we apply ﬁrstly Lemma A.4 and secondly Lemma A.6.

B Diﬀerentiation formulas and integration of series

In this section, for reader’s convenience, we state some speciﬁc results from analysis and calculus that we
use all along. To begin with, since we use several times the multivariate Faa di Bruno formula to calculate
the derivative of a composition of functions, we provide its explicit expression according to [3, Theorem 2.1].
To this end some notation is needed. If ν = (ν1, . . . , νd) ∈ Z
d
≥0 and x = (x1, . . . , xd) ∈ Rd then we deﬁne

|ν| =
 d∑

i=1 νi, ν! =
 d∏

i=1
(νi!), ∂ν
x = ∂|ν|

∂ν1
x1 · · · ∂νd
xd and x
ν =
 d∏

i=1 xνi
i .

Moreover, if ℓ = (ℓ1, . . . , ℓd) ∈ Z
d
≥0, we write ℓ ⩽ ν provided ℓi ⩽ νi for i = 1, . . . , d. Let f (y1, . . . , ym) and
g(1)(x1, . . . , xd), . . . , g(m)(x1, . . . , xd) be real-valued functions and set

h(x1, . . . , xd) = f (
g(1)(x1, . . . , xd), . . . , g(m)(x1, . . . , xd)
) .

Theorem B.1 (Multivariate Faa di Bruno formula). Let ν = (ν1, . . . , νd) ∈ Z
d
≥0 with |ν| > 0 and x0 ∈ Rd

be given. Suppose that all the partial derivatives ∂ℓ
x with ℓ ⩽ ν of g1, . . . , gm exist and are continuous
in a neighbourhood of x0. Assume moreover that all the partial derivatives ∂λ
y f (y), with λ ∈ Z
m
≥0 and
|λ| ⩽ |ν|, exist and are continuous in a neighbourhood of (g1(x0), . . . , gm(x
0)) ∈ Rm. Then ∂ν
x h(x) exits in
a neighbourhood of x0 and it is given by

hν (x) = ∑

1⩽|λ|⩽|ν| fλ(g(x)) ∑

p(ν,λ)
(ν!)
 q∏

i=1
 (gℓi(x))ki

(ki!)(ℓi!)|ki| ,

where
 p(ν, λ) =
 {

(k1, . . . , kq; ℓ1, . . . , ℓq) :
 q∑

i=1 ki = λ and
 q∑

i=1 |ki|ℓi = ν
}
 . (37)

In the statement ℓ1, . . . , ℓq ∈ Z
d
≥0 is a complete listing of all vectors ℓ ⩽ ν with |ℓ| > 0, k1, . . . , kq ∈ Z
m
≥0
and q = −1+∏d
i=1(νi+1). We also set hν (x) = ∂ν
x h(x), fλ(y) = ∂λ
y f (y) and gℓ(x) = (g(1)
ℓ (x), . . . , g(m)
ℓ (x))

where g(i)
ℓ (x) = ∂ℓ
xg(i)(x).

We will also appeal to the following Leibniz formula for the partial derivatives of a product of functions
(see for instance [2, Theorem C, p. 132]).
 32

Theorem B.2. If f1, . . . , fr ∈ C ∞(U ) for some open subset U of Rd and ν ∈ Z
d
≥0 then

∂ν r∏

i=1 fi = ∑

ℓ1+...+ℓr=ν
 ( ν
ℓ1, . . . , ℓr
) r∏

i=1 ∂ℓifi,

where ℓ1, . . . , ℓr ∈ Z
d
≥0 and ( ν
ℓ1,...,ℓr) := ν!
ℓ1!···ℓr! = d∏

i=1
 νi!
ℓ1i!···ℓri! .

Remark B.3. The generalized multinomial coeﬃcients ( ν
ℓ1,...,ℓr) satisfy

r|ν| =
 d∏

i=1
 

 r∑

j=1 1




νi
 =
 d∏

i=1
 ( ∑

ℓ1+...+ℓr=ν
 νi!
ℓ1i! · · · ℓri!
 )
 = ∑

ℓ1+...+ℓr=ν
 d∏

i=1
 νi!
ℓ1i! · · · ℓri! = ∑

ℓ1+...+ℓr=ν
 ( ν
ℓ1, . . . , ℓr
)

thanks to the multinomial identity (see [2, Theorem B, p 28])
( m∑

i=1 xi
)n
 = ∑ n!
a1! · · · am! xa1
1 · · · x
am
m ,

where the summation takes place over all (a1, . . . , am) ∈ Z
m
≥0 such that a1 + . . . + am = n. □

The following result is also well-known (see [17, Theorem 7.17] for instance).

Lemma B.4. Suppose that {fn} is a sequence of functions, diﬀerentiable on [a, b] and such that {fn(x0)}
converges for some point x0 ∈ [a, b]. If {f ′
n} converges uniformly on [a, b], then {fn} converges uniformly
on [a, b] to a function f such that
 f ′(x) = lim
n→∞ f ′
n(x) for all x ∈ [a, b].

Lemma B.5. Let E be a measurable set of R and consider a sequence of measurable functions {fn}n∈N. If∑

n⩾1 ∫
E |fn(x)|dx < +∞ then ∫
E ∑

n⩾1 fn(x)dx = ∑

n⩾1 ∫
E fn(x)dx.

Proof. The problem is to show that

lim
k→+∞
 ∫

E ψk(x)dx = ∫

E lim
k→+∞ ψk(x)dx, where ψk(x) :=
 k∑

n=1 fn(x) for each k ∈ N,

and this follows by the Lebesgue’s dominated convergence theorem (see [17, Theorem 11.32]) because

|ψk(x)| ⩽
 k∑

n=1 |fn(x)| ⩽
 +∞∑

n=1 |fn(x)| =: Ψ(x) for all k ∈ N

and, on the other hand, ∫
E Ψ(x)dx < +∞ by hypothesis. In this regard let us remark that, due to |fn| ⩾ 0
for all n ∈ N, the equality ∑
n⩾1 ∫
E |fn(x)|dx = ∫
E ∑
n⩾1 |fn(x)|dx holds (see [17, Theorem 11.30]).

References

[1] C. Chicone, “Ordinary diﬀerential equations with applications”, Texts in Applied Mathematics, 34.
Springer, New York, 2006.
 33

[2] L. Comtet, “Advanced combinatorics. The art of ﬁnite and inﬁnite expansions", D. Reidel Publishing
Co., Dordrecht, 1974.

[3] G. M. Constantine and T. H. Savits, A multivariate Faà di Bruno formula with applications, Trans.
Amer. Math. Soc. 348 (1996) 503–520.

[4] A. Gasull, V. Mañosa and J. Villadelprat, On the period of the limit cycles appearing in one-parameter
bifurcations, J. Diﬀerential Equations 213 (2005) 255–288.

[5] S. N. Chow and J. K. Hale, “Methods of bifurcation theory", Grundlehren der Mathematischen Wis-
senschaften 251. Springer-Verlag, New York-Berlin, 1982.

[6] Yu. Il’yashenko and S. Yakovenko, Finitely smooth normal forms of local families of diﬀeomorphisms
and vector ﬁelds, (Russian) Uspekhi Mat. Nauk 46 (1991) 3–39, 240; translation in Russian Math.
Surveys 46 (1991) 1–43.

[7] F. Mañosas, D. Rojas and J. Villadelprat, Analytic tools to bound the criticality at the outer boundary
of the period annulus, J. Dyn. Diﬀ. Equat. 30 (2018) 883–909.

[8] P. Mardešić, D. Marín and J. Villadelprat, On the time function of the Dulac map for families of
meromorphic vector ﬁelds, Nonlinearity 16 (2003) 855–881.

[9] P. Mardešić, D. Marín and J. Villadelprat, The period function of reversible quadratic centers, J.
Diﬀerential Equations 224 (2006) 120–171.

[10] P. Mardešić, D. Marín and J. Villadelprat, Unfolding of resonant saddles and the Dulac time, Discrete
Contin. Dyn. Syst. 21 (2008) 1221–1244.

[11] P. Mardešić, D. Marín, M. Saavedra and J. Villadelprat, Unfoldings of saddle-nodes and their Dulac
time, J. Diﬀerential Equations 261 (2016) 6411–6436.

[12] D. Marín and J. Villadelprat, On the return time function around monodromic polycycles, J. Diﬀerential
Equations 228 (2006) 226–258.

[13] A. Mourtada, Cyclicité ﬁnie des polycycles hyperboliques de champs de vecteurs du plan: mise sous
forme normale, in: Bifurcations of Planar Vector Fields (J.P. Françoise and R Roussarie, eds.), Lecture
Notes in Math. 1455, Springer-Verlag, Berlin - Heidelberg - New York (1990), 272-314.

[14] R. Roussarie, On the number of limit cycles which appear by perturbation of separatrix loop of planar
vector ﬁelds, Bol. Soc. Brasil. Mat. 17 (1986) 67–101.

[15] R. Roussarie, “Bifurcations of planar vector ﬁelds and Hilbert’s sixteenth problem”, [2013] reprint of
the 1998 edition. Modern Birkhäuser Classics. Birkhäuser/Springer, Basel, 1998.

[16] R. Roussarie, Smoothness property for bifurcation diagrams, Proceedings of the Symposium on Planar
Vector Fields (Lleida, 1996). Publ. Mat. 41 (1997) 243–268.

[17] W. Rudin, “Real and complex analysis”, McGraw-Hill Book Co., New York-Toronto, Ont.-London 1966.

[18] W. Rudin, “Principles of mathematical analysis”, International Series in Pure and Applied Mathematics.
McGraw-Hill Book Co., New York-Auckland-Düsseldorf, 1976.

[19] J. Sotomayor, “Lições de equações diferenciais ordinárias", Projeto Euclides, 11, Instituto de
Matemática Pura e Aplicada, Rio de Janeiro, 1979.

34
