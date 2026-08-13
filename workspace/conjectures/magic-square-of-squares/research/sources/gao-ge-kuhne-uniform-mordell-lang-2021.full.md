<!-- source: https://arxiv.org/pdf/2105.15085 | converted from PDF -->

THE UNIFORM MORDELL–LANG CONJECTURE

ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

Abstract. The Mordell–Lang conjecture for abelian varieties states that the
intersection of an algebraic subvariety X with a subgroup of finite rank is
contained in a finite union of cosets contained in X. In this article, we prove a
uniform version of this conjecture, meaning that the number of cosets necessary
depend only on the dimension of the ambient variety and the degree (with
respect to some polarization) of the subvariety X. To achieve this, we prove
a general gap principle on algebraic points that extends the new gap principle
for curves embedded into their Jacobians, previously obtained by Dimitrov–
Gao–Habegger and K¨uhne. Our new gap principle also implies the full uniform
Bogomolov conjecture in abelian varieties.

Contents

1. Introduction 1
2. Preliminaries on abelian varieties 8
3. Hilbert schemes and non-degeneracy 11
4. Applying the height inequality 18
5. Applying equidistribution 27
6. Proof of the gap principle (Theorem 1.2) 36
7. Proof of the uniform Mordell–Lang conjecture (Theorem 1.1) 38
8. Proof of the uniform Bogomolov conjecture (Theorem 1.3) 44
Appendix A. R´emond’s theorem revisited 45
References 52

1. Introduction

Throughout this article, F is an algebraically closed field of characteristic
0; particularly relevant cases are F = Q and F = C. Furthermore, we let A be
an abelian variety defined over F and consider an ample line bundle L on A. The
translates of abelian subvarieties by closed points in A are called cosets.

2000 Mathematics Subject Classification. 11G10, 14G05, 14G25, 14K12.
1arXiv:2105.15085v4  [math.NT]  26 Mar 2026
2 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

The main result of our article is the following uniform version of the well-
known Mordell–Lang conjecture (see [Lan62, p. 138]).

Theorem 1.1 (Uniform Mordell–Lang Conjecture). For all integers g, d ≥ 0,
there exists a constant c(g, d) > 0 with the following property. Let X ⊆ A be an
irreducible closed subvariety and Γ ⊆ A(F ) a subgroup of finite rank. Then the
intersection X(F ) ∩ Γ is covered by at most

c(dim A, degL X)
1+rkΓ

cosets contained in X.

For readers’ convenience, let us restate this theorem in a more explicit
fashion. For every polarized abelian variety of dimension g, every irreducible
closed subvariety X ⊆ A of degree d (with respect to the given polarization) and
every subgroup Γ of finite rank ρ, it claims the existence of cosets

xi + Bi ⊆ X, 1 ≤ i ≤ N ≤ c(g, d)1+ρ,

such that

(1.1) X(F ) ∩ Γ =
 N⋃

i=1
(xi + Bi)(F ) ∩ Γ.

The original Mordell–Lang conjecture asserts that finitely many cosets

xi + Bi ⊆ X, 1 ≤ i ≤ N,

are sufficient to cover the intersection X(F ) ∩ Γ as in (1.1), without suggest-
ing any further quantitative control on their number. This original version,
which combines both the Manin–Mumford conjecture [Ray83] and the Mordell
conjecture [Fal83], was established by Faltings [Fal91, Fal94], following work of
Hindry [Hin88] and Vojta [Voj91]. An explicit upper bound for the number of
cosets was obtained by R´emond [R´em00a], which additionally depends on the
ambient abelian variety A via its Faltings height hFal(A).
The novelty here is the complete removal of this very dependence on the am-
bient abelian variety A, confirming a folklore expectation that can be found for ex-
ample in [DP07, Conj. 1.8]. It is known under the name of uniform Mordell–Lang
conjecture because the number N in (1.1) must depend on g, d and ρ. For curves
embedded in their Jacobian, it dates back to a question of Mazur [Maz86, top
of p. 234], which has been answered affirmatively by work of Dimitrov, the first-
named author, Habegger and the third-named author [DGH21, K¨uh21]. Readers

THE UNIFORM MORDELL–LANG CONJECTURE 3

may profit from the survey of the first-named author [Gao21] for an overview of
these previous works and their implications for rational points on algebraic curves.
Let us remark that before these works, the only uniform results of Mordell-Lang
type were obtained by David and Philippon [DP07, Thm. 1.13] for subvarieties
of self-products of an elliptic curve. It should be also noted that they give a
completely explicit constant in this special case. In this regard, it is interesting
to ask whether the present arguments can yield explicit upper bounds on the
number of cosets similar to those of David and Philippon [DP07] or if substantial
new ideas are necessary.
Our proof of Theorem 1.1 relies on the ideas established in the series of
work [DGH19, DGH21, DGH22, K¨uh21] building upon Vojta’s approach [Voj91]
to the Mordell conjecture. However, several new difficulties arise in the higher-
dimensional case considered here; see §1.3 for a short discussion. A comprehensive
outline of all other sections can be found at the end of the introduction.

1.1. The Ueno locus and first reductions. The Ueno locus of X is the union
of positive dimensional cosets contained in X. A result of Kawamata [Kaw80,
Thm. 4] states that it is Zariski closed. Write X ◦ for its complement in X; then
X ◦ is a Zariski open set. Note that the Ueno locus of a smooth, proper curve of
genus g ≥ 2 embedded into its Jacobian is empty.
A recursive argument in §7.4 reduces Theorem 1.1 to the following weaker
statement.

Theorem 1.1′. For all integers g, d ≥ 0, there exists a constant c(g, d) > 0
with the following property. Let X ⊆ A be an irreducible closed subvariety and
Γ ⊆ A(F ) a subgroup of finite rank. Then

(1.2) #X ◦(F ) ∩ Γ ≤ c(dim A, degL X)
1+rkΓ.

Besides reducing to Theorem 1.1′, we also use a specialization argument
of Masser [Mas89] to assume F = Q in our main arguments. This is an essen-
tial reduction, since we will mostly work with arithmetical arguments around
the theory of heights. Although Theorem 1.1
′ could itself be understood as a
purely geometric assertion (e.g. for F = C), we heavily rely on arithmetic tools
throughout our proof.

1.2. A generalized gap principle. Our approach is modeled on Vojta’s proof of
the Mordell conjecture [Voj91] and its later refinements, notably the quantitative
ones obtained by R´emond [R´em00a, R´em00b]. His method leads to a dichotomy
between algebraic points of large and small N´eron–Tate height, which we call
large and small points for simplicity.

4 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

A uniform count of large points can be done by using the work of R´emond
[R´em00a, R´em00b], which provides explicit, generalized versions of Mumford’s
and Vojta’s inequalities. Compared to the case of curves in their Jacobians
dealt with in [DGH19, DGH21], some extra work is actually needed to establish
Mumford’s inequality. In particular, we need to invoke the induction hypothesis
twice to handle large points. We give a detailed account in Appendix A without
claiming originality.
Our main contribution is a uniform count of small points, and we achieve
this by establishing another kind of gap principle for algebraic points. In the case
of curves in their Jacobians, preceding work [DGH21,K¨uh21] has been subsumed
under such a New Gap Principle [Gao21, Thm. 4.1]. In this article, we take
the same perspective and generalize it as follows. We say that a subvariety
X ⊆ A generates A if the smallest abelian subvariety containing X − X is A.
Furthermore, we let ˆhL⊗[−1]∗L denote the N´eron–Tate height on A(Q) associated
with the symmetric ample line bundle L ⊗ [−1]∗L.

Theorem 1.2 (New Gap Principle). Given two positive integers g and d, there
exist positive constants c1 = c1(g, d) and c2 = c2(g, d) with the following property:
For any polarized abelian variety (A, L) of dimension g and any irreducible closed
subvariety X ⊆ A that generates A of degree degL X ≤ d, the set

(1.3) {
P ∈ X ◦(Q) : ˆhL⊗[−1]∗L(P ) ≤ c1 max{1, hFal(A)}} ,

is contained in X ′(Q) for a proper Zariski closed X ′ ⊊ X with degL(X ′) < c2.

Note that this theorem has been predicted by [Gao21, Conj. 10.5’]. The
two examples constructed at the end of [Gao21, §10.2] show that, in contrast to
the case of curves embedded into their Jacobians, one can neither get rid of the
assumption that X generates A nor assert that (1.3) is a finite set of uniformly
bounded cardinality.

We remark that Theorem 1.2 implies a uniform version of the Bogomolov
conjecture, generalizing [K¨uh21, Thm. 3] in the case of curves embedded in their
Jacobians. Since this result is of independent interest, we state it here explicitly.

Theorem 1.3 (Uniform Bogomolov Conjecture). Given two positive integers g
and d, there exist positive constants c3 = c3(g, d) and c3 = c3(g, d) with the follow-
ing property: For any abelian variety (A, L) of dimension g and any irreducible
closed subvariety X ⊆ A that generates A of degree degL X ≤ d, we have

(1.4) # {
P ∈ X ◦(Q) : ˆhL⊗[−1]∗L(P ) ≤ c3} < c4.

THE UNIFORM MORDELL–LANG CONJECTURE 5

We emphasize that as in the case of curves, to obtain Theorem 1.1
′ it is
necessary to use the New Gap Principle for (1.3) instead of (1.4) because the
dichotomy of large and small points is in comparison to max{1, hFal(A)}. Unlike
the case of curves embedded in their Jacobians, this theorem is not formally a
special case of Theorem 1.2, although a deduction from Theorem 1.2 is easy and
given in §8.
An analogue of Theorem 1.3 for curves in algebraic tori was proven by
Bombieri–Zannier [BZ95] (compare also [DP99, AD06]). For the case of abelian
varieties considered here, Theorem 1.3 was known only in some cases [DP07,
DKY20,K¨uh21]. Let us note that all these results except for [K¨uh21] have rather
explicit constants, in contrast to our general Theorem 1.3 here.

After the first version of the current article appeared as a preprint, Yuan
[Yua26] gave another proof of Theorem 1.2 in the case of curves embedded into
their Jacobians previously considered in [DGH21, K¨uh21]. His approach has the
advantage to work in the function field case (in positive characteristic) as well. It
relies on previous work of Zhang, Cinkir, and de Jong [Zha93,Zha10,Cin11,dJ18]
for lower bounds on the self-intersection numbers of the admissible canonical bun-
dles of curves over global fields. Little is known in this direction for subvarieties
of higher dimension and it seems very hard to generalize Yuan’s proof to the
setting considered here. He also uses the new theory of Yuan–Zhang [YZ26] on
adelic line bundles on quasi-projective varieties.

1.3. Ideas of the proof. Non-degenerate subvarieties of abelian schemes, a no-
tion introduced by Habegger [Hab13] and extensively studied by the first-named
author [Gao20], have played a central role in previous work [DGH19, DGH21,
DGH22, K¨uh21] and continue to do so in the current article. They derive their
importance from the fact that they are the natural setting for both
(1) the height inequality of [DGH21, Thm. 1.6 and B.1], which allows a com-
parison of the N´eron–Tate height and the height on the base variety, and
(2) the equidistribution theorem [K¨uh21, Thm. 1].
More recently, Yuan and Zhang have reproven both these results using their
general theory of adelic line bundles over quasi-projective varieties [YZ26].
A starting problem in the current paper is hence the construction of an
appropriate non-degenerate subvariety. In the case of curves embedded in their
Jacobians, by the quasi-finiteness of the Torelli map, we could restrict ourselves
to consider subvarieties of an abelian scheme A → S of maximal variation, that
is, the moduli map from S to the moduli space of abelian varieties is generically
finite. In the current paper, we need a space parametrizing all subvarieties of
a fixed degree in abelian varieties of a fixed dimension and polarization. While

6 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

there is a natural candidate, the Hilbert scheme, the moduli map from it to the
moduli space of abelian varieties has positive dimensional fibers. This makes the
construction of the relevant non-degenerate subvarieties significantly harder than
the case of curves.
We resolve this problem by showing that the moduli map on the total
space, when restricted to the universal family over an open subset of the Hilbert
scheme (3.6), becomes still generically finite after taking a high enough fibered
power (Lemma 3.3), as inspired by the second-named author’s work [Ge24, §3].
Then [Gao20, Thm. 10.1] gives us the desired non-degeneracy (Proposition 3.4).
We expect the idea of this construction to be applicable in other settings, for
example to study uniformity problems for semiabelian varieties, which would
extend in particular the uniform results of Bombieri–Zannier [BZ95] on algebraic
tori, and even to study related problems in some families of dynamical systems
as in [GTV26]. The need for non-degeneracy makes it necessary to shift back and
forth to fibered products. In the course of this, we have to control the exceptional
sets appearing. For this purpose, we provide a technical key Lemma 4.3.
To prove uniform bounds as in Theorem 1.1′, it is important to work with
only finitely many families at all times. While this is automatic in the setting for
curves embedded into their Jacobians (by an induction on the dimension of the
subvariety), we have to carefully handle the invariants involved, in particular the
polarization type. Even if one is only interested in the case of principal polariza-
tion, our inductive proof generally invokes abelian varieties of any polarization
degree. We use various techniques to overcome these problems, including a clas-
sical result of Mumford and the Poincar´e biextension on the universal abelian
variety.

1.4. Outline of the article. In §2, we review basic facts on abelian varieties
and polarization types. In particular, we give a bound Lemma 2.5 on the degree
of the abelian subvariety generated by X, using an argument suggested to us by
Marc Hindry. This allows us to avoid any dependence on the polarization degree
degL(A) in the final results.
In §3, we construct the families of non-degenerate subvarieties used in our
main arguments. We also deduce the key result to establish their non-degeneracy
here (Proposition 3.4) from the results of [Gao20].
In §4, we apply the height inequality [DGH21, Thm.1.6 and B.1] to these
non-degenerate subvarieties. The main result of this section is Proposition 4.1,
which roughly proves an analogue of Theorem 1.2, albeit invoking more invariants,
with (1.3) replaced by the set
{
x ∈ X ◦(Q) : ˆhL⊗[−1]∗L(x) ≤ c
′
1 max{1, hFal(A)} − c′
3}

THE UNIFORM MORDELL–LANG CONJECTURE 7

for certain uniform c′
1, c
′
3 > 0. Note that this set is exactly (1.3) if hFal(A) ≥
max{1, 2c
′
3/c
′
1} up to changing constants, but becomes trivially empty if max{1, hFal(A)} <
c′
3/c
′
1. For counting purposes, a key technical Lemma 4.3 allows us to use the
non-degenerate fibered products of the (in general degenerate) Hilbert schemes
constructed in §3.
The main result of §5 is Proposition 5.1, which again has the same form as
Theorem 1.2 but without hFal(A); here, the set (1.3) replaced by the set
{
x ∈ X ◦(Q) : ˆhL⊗[−1]∗L(x) ≤ c′′
3}

for a certain uniform c
′′
3 > 0. Its proof invokes the equidistribution theorem
[K¨uh21, Thm. 1] for the same non-degenerate subvarieties as in §4. The proof
follows the classical strategy of Ullmo [Ull98] and Zhang [Zha98] with substan-
tially new technical difficulties. Lemma 4.3 is used again.
In §6, we combine Propositions 4.1 and 5.1 into the desired gap principle
stated in Theorem 1.2.
In §7, we show how to deduce the uniform Mordell–Lang conjecture by
combining the gap principle with a result of R´emond. In addition, we use a
specialization argument of Masser to reduce to the case F = Q (Lemma 7.3). We
also include an argument to deduce Theorem 1.1 from Theorem 1.1
′.
In §8, we show how to deduce the uniform Bogomolov conjecture from the
new gap principle (Theorem 1.2).
In Appendix A, we give a more detailed account of R´emond’s result that is
one of the two essential ingredients for the proof in §7.

Acknowledgements. The authors would like to thank Marc Hindry for the ar-
gument for Lemma 2.5. The authors would like to thank Gabriel Dill for his valu-
able comments on a previous version of the manuscript, especially for a correction
of the argument for Lemma 3.1, the reference [Dil22, Lemma 2.4], discussions on
the specialization argument and on the optimality of our formulation of Theorem
1.1. We thank Dan Abramovich and Philipp Habegger for comments on a draft
of this paper and Abbey Bourdon for a relevant discussion on the consequence of
our main result on rational points. We would like to thank the referee for their
careful reading and helpful comments.
ZG received funding from the European Research Council (ERC) under
the European Union’s Horizon 2020 research and innovation programme (grant
agreement n◦ 945714). TG received funding from NSF grant DMS-1759514 and
DMS-2100548. LK received funding from the European Union’s Horizon 2020
research and innovation programme under the Marie Sklodowska-Curie grant

8 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

agreement No. 101027237. A revision of this article was supported by the Na-
tional Science Foundation under Grant No. DMS-1928930, while the three authors
were in residence at the SL-Math in Berkeley, California, during its semester on
“Diophantine Geometry” in 2023.

2. Preliminaries on abelian varieties

In this section, we include some basic results on abelian varieties. Through-
out the section, let A be an abelian variety defined over Q of dimension g, where
Q is an algebraic closure of Q in C.

2.1. Polarizations. Let Pic(A) be the Picard group of A and Pic0(A) be the
connected component of the identity. For L ∈ Pic(A), we denote its Chern
class by c1(L) ∈ H 2(A(C), Z). Let A∨ be the dual abelian variety of A. Then
Pic
0(A) = A
∨(Q).
For each a ∈ A(Q), let ta : A → A be the translation-by-a map. Given
L ∈ Pic(A), it induces a group homomorphism between dual abelian varieties
ϕL : A → A
∨ by sending a ∈ A(Q) to t
∗
aL ⊗ L⊗−1 ∈ Pic
0(A).
When L is ample, the homomorphism ϕL is moreover an isogeny, i.e. a
surjective group homomorphism with finite kernel, in which case we say ϕL is a
polarization of A. The polarization is called a principal polarization if ϕL is an
isomorphism.
The polarization is uniquely determined by the Chern class of the line
bundle by the following lemma [Deb05, Theorem 6.10]:

Lemma 2.1. Let L and L′ be two ample line bundles on A. Then L and L′ define
the same polarization if and only if c1(L) = c1(L
′).

A polarized abelian variety (A, L) is defined as an abelian variety A equipped
with an ample line bundle L serving as a representative of the Chern class c1(L).
Write A(C) = C
g/Λ for some lattice Λ ⊆ C
g of rank 2g. There is a
canonical isomorphism between H 2(A(C), Z) and Alt
2(Λ, Z), the group of Z-
bilinear alternating forms Λ × Λ → Z. Thus c1(L) defines a Z-bilinear alternating
form

(2.1) E : Λ × Λ → Z.

As L is ample, c1(L) is positive definite, and hence E is non-degenerate.
So there exists a basis (γ1, . . . , γ2g) of Λ under which the matrix of E is

(2.2) [ 0 D
−D 0
 ]

THE UNIFORM MORDELL–LANG CONJECTURE 9

where D = diag(d1, . . . , dg) with d1| · · · |dg positive integers; see [Deb05, Propo-
sition 6.1]. Moreover, the matrix D is uniquely determined. We say D is the
polarization type of (A, L). Define the Pfaffian by

Pf(L) := det(D).

Lemma 2.2. Let L be an ample line bundle on A. Then
(i) dim H 0(A, L) = Pf(L);
(ii) degL(A) = g! · Pf(L);
(iii) if f : A′ → A be an isogeny, then dim H 0(A
′, f ∗L) = deg(f ) dim H 0(A, L);
(iv) there exists an abelian variety A0, an ample line bundle L0 on A0 defining
a principal polarization, and an isogeny u0 : A → A0 such that L ∼= u
∗
0L0;
moreover, deg(u0) = degL(A)/g!.

Proof. For (i), (ii) and (iii), it suffices to prove the assertions over C. Then (i)
is [BL04, Corollary 3.2.8], (ii) is just the Riemann–Roch theorem [BL04, Section
3.6] and (iii) is [Deb05, Cororollary 6 to Proposition 6.12]. (iv) is [Mum74, pp.
234, Corollary 1 and its proof]. □

We often work with symmetric ample line bundles for N´eron-Tate heights.
For this purpose, we need the following lemma.

Lemma 2.3. Let L and L
′ be two symmetric ample line bundles on A. If c1(L
′) =
c1(L), then ˆhL = ˆhL′.

Proof. We have c1(L
′ ⊗ L⊗−1) = c1(L
′) − c1(L) = 0. So L′ ⊗ L⊗−1 ∈ Pic
0(A) =
A
∨(Q). The homomorphism ϕL : A → A
∨, a ↦→ t∗
aL ⊗ L⊗−1, is an isogeny because
L is ample. So there exists a ∈ A(Q) such that ϕL(a) = L′⊗L⊗−1. Thus L
′ ∼= t
∗
aL.
Therefore for each x ∈ A(Q), we have

(2.3) ˆhL′(x) = ˆht∗
aL(x) = ˆhL(a + x).

Taking x = 0, x ∈ A(Q)tor, we get ˆhL(a) = 0 for the symmetric ample line
bundles L and L′. But then a ∈ A(Q)tor since L is symmetric ample, and hence
(2.3) yields ˆhL′(x) = ˆhL(a + x) = ˆhL(x) for all x ∈ A(Q). □

2.2. Degree estimates. The degree of a closed subvariety X of A with respect
to an ample line bundle L is defined as follows. If X is irreducible, set degL X :=
c1(L)
dim X ∩ [X] where [X] is the cycle of A given by X. For general X, set
degL X := ∑

i degL Xi where X = ⋃ Xi is the decomposition into irreducible
components. We use the notation from [Ful98, Chapters 1 and 2] freely in the
following.

10 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

Lemma 2.4. Assume that L is very ample. Let Y and Y ′ be irreducible subva-
rieties of A. Then

(2.4) degL(Y + Y ′) ≤ 4
dim Y +dim Y ′ degL Y · degL Y ′.

Proof. Write pi : A × A → A, i = 1, 2, for the natural projection to the i-th
factor. Then L
⊠2 := p
∗
1L ⊗ p
∗
2L is an ample line bundle on A × A and we have
c1(L
⊠2) = p∗
1c1(L) + p∗
2c1(L). For readability, write d and d
′ for the dimension of
Y and Y ′, respectively. By [Ful98, Prop. 2.5 and Rmk. 2.5.3], it follows that

degL⊠2(Y × Y ′) = c1(L
⊠2)
d+d′ ∩ [Y × Y ′](2.5)
 =
 d+d′
∑

i=0
 (
d + d′

i
 )

c1(p∗
1L)
i ∩ c1(p
∗
2L)
d+d′−i ∩ [Y × Y ′]

=
 d+d′
∑

i=0
 (
d + d′

i
 )

(c1(p∗
1L)
i ∩ [Y ]) × (c1(p
∗
2L)
d+d′−i ∩ [Y ′]).

For reasons of dimension, the only non-vanishing term in this sum is i = d. So

(2.6) degL⊠2(Y × Y ′) =
 (
d + d′

d
 )
 degL Y · degL Y ′.

Consider the isogeny

α : A × A −→ A × A, (x, y) ↦−→ (x + y, x − y),

of degree 2
2g. We recall that c1(α∗L
⊠2) = 2c1(L
⊠2) by [HS00, Prop. A.7.3.3]. By
(2.6), it follows that

degα∗L⊠2(Y × Y ′) = 2d+d′(
d + d′

d
 )
 degL Y · degL Y ′ ≤ 4
d+d′ degL Y · degL Y ′.

We are ready to prove (2.4). Indeed, using p1(α(Y × Y ′)) = Y + Y ′ we obtain

degL(Y + Y ′) ≤ degp∗
1L⊗p∗
2L(α(Y × Y ′)) ≤ degα∗p∗
1L⊗α∗p∗
2L(Y × Y ′) = degα∗L⊠2(Y × Y ′);

the first inequality follows for example from [Dil22, Lem. 2.4] and the second
one from the projection formula [Ful98, Prop. 2.5(c)]. We conclude the proof by
combining the last two inequalities and using (
d+d′

d ) ≤ 2
d+d′. □

Lemma 2.5. Let X be an irreducible subvariety of A and let A′ denote the abelian
subvariety generated by X − X. Then degL A′ ≪g degL(X)
2g.

THE UNIFORM MORDELL–LANG CONJECTURE 11

Proof. Replacing L by L
⊗3, we may and do assume that L is very ample. We
write r = dim X.
The ascending chain

(X − X) ⊆ (X − X) + (X − X) ⊆ (X − X) + (X − X) + (X − X) ⊆ · · ·

of closed irreducible subvarieties becomes stationary as soon as two consecutive
elements are equal. By dimension reasons, we infer that

A
′ = (X − X) + (X − X) + · · · + (X − X)
︸ ︷︷ ︸
g copies

so the chain certainly becomes stationary after at most g steps.
To conclude the proof, we claim the inequality

degL((X − X) + · · · + (X − X)
︸ ︷︷ ︸
k copies ) ≤ 8
2kr degL(X)
2g

for every k ≥ 1. For k = 1, we apply (2.4) to Y = X and Y ′ = −X and get

degL(X − X) ≤ 8r(degL X)
2.

Similarly, we get

degL((X − X) + · · · + (X − X)
︸ ︷︷ ︸
k copies ) ≤ 8
kr·degL((X − X) + · · · + (X − X)
︸ ︷︷ ︸
(k − 1) copies
 )·degL(X−X)

for every integer k ≥ 2. Combining these inequalities, we obtain

degL(A′) ≤ 8(g+···+2)r degL(X − X)
g < 8
(g+1)2r degL(X)
2g,

whence the assertion of the lemma. □

3. Hilbert schemes and non-degeneracy

Let r ≥ 1 and d ≥ 1 be two integers. In this section, we work over Q, i.e.
all objects and morphisms are defined over Q unless stated otherwise.
Our goal is to introduce the restricted Hilbert schemes (3.6) and prove a
non-degeneracy result, Proposition 3.4. This is one of the main new ingredients to
prove the uniform Mordell–Lang Conjecture for higher dimensional subvarieties
of abelian varieties compared to the case of curves.
As we will work with Hilbert schemes, we make the following convention.
All schemes are assumed to be separated and of finite type over the base. By

12 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

a variety defined over Q, we mean a reduced scheme over Q. Hence an integral
scheme (i.e. a reduced irreducible scheme) is the same as an irreducible variety.
For general information on Hilbert schemes and Hilbert polynomials, we
refer to [Gro62], [ACG11, Chap. 9] and [Kol99, §I.1].

3.1. Parameterizing subvarieties of an abelian variety. Let A be an abelian
variety and let L be a very ample line bundle. All degrees below will be with
respect to L.
The following result can be deduced from [Gro62, Thm. 2.1(b) and Lem. 2.4],
which itself is proved by comparing the Hilbert scheme and the Chow variety:
There is a finite set Ξ of polynomials such that the Hilbert polynomial of any
irreducible subvariety of A of dimension r and degree d is an element of Ξ. In-
deed, in the notation of [Gro62, Thm. 2.1(b) and Lem. 2.4], we can take X = A,
S = Spec(Q), OX(1) = L, K = Q, Y ⊆ A the irreducible subvarieties of degree
d, F the structure sheaf of such a subvariety Y , and E the set of the classes of all
these structure sheaves.
Let Hr,d(A) := ⋃

P ∈Ξ HP (A), where HP (A) is the Hilbert scheme that
parameterizes subschemes of A with Hilbert polynomial P and is constructed
in [Gro62, Thm. 3.2]. As Ξ is a finite set, Hr,d(A) is a projective variety over
Q. By construction, there exists a universal family Xr,d(A) → Hr,d(A) endowed
with a natural closed Hr,d(A)-immersion

(3.1) Xr,d(A) ˜   //
 ''

A × Hr,d(A)

πA

Hr,d(A)

where πA is the projection to the second factor. Over each point s ∈ Hr,d(A)(Q),
the fiber Xr,d(A)s is precisely the subscheme of A parametrized by s, and the
horizontal immersion restricts to its natural closed immersion in A.
By the definition of Hilbert schemes, the morphism πA|Xr,d(A) is flat and
proper. By [Gro67, Thm. 12.2.4.(viii)],

(3.2) {s ∈ Hr,d(A) : Xr,d(A)s is geometrically integral}

is a Zariski open subset of Hr,d(A), which we endow with the induced sub-
scheme structure. We write Hr,d(A)
◦ for the maximal reduced subscheme of
this scheme. Note that Hr,d(A)
◦ is a quasi-projective variety defined over Q.
Its points Hr,d(A)
◦(Q) parametrize all irreducible Q-subvarieties X of A with
dim X = r and degL X = d (by our choice of Ξ above). For each irreducible

THE UNIFORM MORDELL–LANG CONJECTURE 13

component V of Hr,d(A), the intersection V ∩ Hr,d(A)
◦ is either a dense Zariski
open in V or empty.

Lemma 3.1. Let V be a (not necessarily irreducible) subvariety of Hr,d(A)
◦.
Then there exist m0 = m0(V ) points P1, . . . , Pm0 ∈ A(Q) such that the Zariski
closed subset of V defined by

{[X] ∈ V (Q) : P1 ∈ X(Q), . . . , Pm0 ∈ X(Q)}

has dimension 0, i.e. is a non-empty finite set.

Proof. Fix [X0] ∈ V (Q). For each k ∈ {0, . . . , dim V }, we claim the following
statement: There are finitely many points Pk,1, . . . , Pk,nk in X0(Q) such that

Vk := {[X] ∈ V (Q) : Pk,1 ∈ X(Q), . . . , Pk,nk ∈ X(Q)}

has dimension ≤ dim V − k.

Taking k = dim V , this claim immediately yields the lemma; the set Vdim V
thus obtained is non-empty since it contains [X0].
We prove this claim by induction on k. The base step k = 0 trivially holds
true because we can take any finite set of points in X0(Q).
Assume the claim holds true for 0, . . . , k − 1. We have thus obtained points
Pk−1,1, . . . , Pk−1,nk−1 ∈ X0(Q) such that

Vk−1 := {[X] ∈ V (Q) : Pk−1,i ∈ X(Q) for all i = 1, . . . , nk−1}

has dimension ≤ dim V − k + 1.
For each irreducible component W of Vk−1 with dim W > 0, there exists
some [XW ] ∈ W (Q) such that XW ̸= X0 as (irreducible) subvarieties of A.
Take PW ∈ (X0 \ XW )(Q). Then {[X] ∈ W (Q) : PW ∈ X(Q)} has dimension
≤ dim W − 1 ≤ dim V − k + 1 − 1 = dim V − k.
Thus it suffices to take {Pk,1, . . . , Pk,nk} := {Pk−1,1, . . . , Pk−1,nk−1}∪(
⋃

W {PW })
with W running over all positive dimensional irreducible components of Vk−1. □

For each m ≥ 1, set Xr,d(A)
[m] := Xr,d(A) ×Hr,d(A) . . . ×Hr,d(A) Xr,d(A).
Then (3.1) induces

(3.3) Xr,d(A)
[m] ×Hr,d(A) Hr,d(A)
◦ ˜   //
 **

A
m × Hr,d(A)
◦

π[m]
A

 ι
[m]
A // Am

Hr,d(A)
◦

where ι[m]
A is the natural projection.

14 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

Lemma 3.2. Let V be a (not necessarily irreducible) subvariety of Hr,d(A)
◦.
Then there exists m0 = m0(V ) ≥ 1 with the following property. For each m ≥ m0,
there exists P ∈ A
m(Q) such that

(ι
[m]
A |Xr,d(A)[m]×Hr,d(A)V )
−1(P )

has dimension 0, i.e. is a non-empty finite set.

Proof. Let P1, . . . , Pm0 ∈ A(Q) be from Lemma 3.1. For each k ≥ m0, we set
Pk = Pm0.
Set P = (P1, . . . , Pm) ∈ A
m(Q). To prove the lemma, it suffices to prove
that (ι[m]
A |Xr,d(A)[m]×Hr,d(A)V )
−1(P ) is a non-empty finite set.

It is clear that π[m]
A |{P }×V is an isomorphism. Therefore, π[m]
A induces an
isomorphism

({P } × V ) ∩ Xr,d(A)
[m] ∼= π[m]
A (
({P } × V ) ∩ Xr,d(A)
[m]) .

The left hand side of this isomorphism is precisely (ι
[m]
A |Xr,d(A)[m]×Hr,d(A)V )
−1(P ).
So it suffices to prove that the right hand side of this isomorphism is a non-empty
finite set. A direct computation shows that the right hand side is

{[X] ∈ V (Q) : P1 ∈ X(Q), . . . , Pm0 ∈ X(Q)},

which is non-empty and finite by Lemma 3.1. □

3.2. Parameterizing subvarieties in families. We next extend the setting of
the previous subsection to the case of families of abelian varieties. Let πuniv : Ag →
Ag be the universal abelian variety over the fine moduli space of principally
polarized abelian varieties of dimension g with level-4-structure. For each b ∈
Ag(Q), the abelian variety parametrized by b is (Ag)b = (πuniv)
−1(b).
We fix a symmetric relatively ample line bundle Lg on Ag/Ag satisfy-
ing the following property: for each principally polarized abelian variety (A, L)
parametrized by b ∈ Ag(Q), we have c1(Lg|(Ag)b) = 2c1(L); see [MFK94, Prop. 6.10]
for the existence of Lg. The line bundle L⊗4
g is relatively very ample on Ag/Ag.
Again by [Gro62, Thm. 2.1(b) and Lem. 2.4], there are finitely many pos-
sibilities for the Hilbert polynomials of irreducible subvarieties of (Ag)b (for all
b ∈ Ag(Q)) of dimension r and degree d with respect to L⊗4
g |(Ag)b.[1] Let Ξ be this
finite set of polynomials.

[1]In the notation of [Gro62, Thm. 2.1(b) and Lem. 2.4], X = Ag, S = Ag, OX (1) = L
⊗4
g , K = Q, Y the
irreducible subvarieties of degree d, F the structure sheaf of such a subvariety Y , and E the set of the classes of
all these structure sheaves.

THE UNIFORM MORDELL–LANG CONJECTURE 15

Consider the Ag-scheme

(3.4) H := ⊔

P ∈Ξ HP (Ag/Ag) ιH−→ Ag

with HP (Ag/Ag) the Ag-scheme representing the functor from Ag-schemes to sets
associating with an Ag-scheme T the set of proper subschemes W ⊆ Ag ×Ag T that
are flat over T and have Hilbert polynomial P . Each HP (Ag/Ag) is projective
over Ag. Since Ξ is a finite set, the structure morphism ιH is of finite type.
Similarly to the previous subsection, there is a universal family endowed
with a closed H-immersion

(3.5) X := Xr,d(Ag/Ag) ˜   //
 ))

Ag ×Ag H =: A

π

H

with π|X flat and proper.

To ease notation, we set SS := S ×H S for every H-scheme S → H and
every morphism S → H. In particular, we do so for X and A as well as for their
fibered self-products over H. If S is a variety, then AS → S is an abelian scheme,
and XS is a subvariety of AS which dominates S.

As for (3.2), the set

(3.6) {s ∈ H : Xr,d(Ag/Ag)s is geometrically integral}

is Zariski open in H and hence has an induced structure as an open subscheme.
We write Hr,d(Ag/Ag)
◦ for the maximal reduced subscheme of this subscheme,
which is a quasi-projective variety defined over Q. In the sequel, Hr,d(Ag/Ag)
◦ is
called the restricted Hilbert scheme. In addition, we denote it simply by H◦ if r,
d and g are clear from context.
By our choice of Ξ and the construction (3.4), H
◦(Q) parametrizes all
pairs ((A, L), X) consisting of a principally polarized abelian variety defined over
Q and an irreducible subvariety X of A defined over Q with dim X = r ≥ 1
and degL⊗4
g |A X = d.[2] For each irreducible component S of H, the intersection
S ∩ H◦ is either a dense Zariski open set in S or empty. For convenience, we set
ιH◦ := ιH|H◦ for the restriction of the structural morphism. The fiber ι
−1
H◦(b) is
precisely the subvariety Hr,d(Ab)◦ defined in the previous subsection.

[2]Here (A, L) gives rise to a point b ∈ Ag(Q), and we identify A with (Ag)b.

16 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

For each m ≥ 1, let X [m]
H◦ (resp. A[m]
H◦ ) denote the m-fold fibered power of
XH◦ over H
◦ (resp. of AH◦ over H
◦). There is a commutative diagram

(3.7) X [m]
H◦ ˜   //
 ""

A
[m]
H◦

π[m]

 ι[m] // A[m]
g
 πuniv,[m]

H◦ ιH◦ // Ag.

Taking fibers in this diagram over a point b ∈ Ag(Q), we obtain again the diagram
(3.3) for the abelian variety A = (Ag)b.

Lemma 3.3. Let S be an irreducible subvariety of H
◦. Then there exists m0 =
m0(S) ≥ 1 such that the restriction of ι
[m] to X [m]
S is generically finite onto its
image for every m ≥ m0.

Proof. Choose some b ∈ ιH◦(S)(Q). We use the notation from (3.3) with A = Ab.
For any P ∈ (πuniv,[m])
−1(b)(Q) = Am
b (Q), we have

(3.8) (ι[m])
−1(P ) ∩ X [m]
S = (ι
[m]
Ab |Xr,d(Ab)[m]×Hr,d(Ab)V )
−1(P ),

where V = (ιH◦|S)
−1(b) ⊆ ι
−1
H◦(b) = Hr,d(Ab)
◦. Thus there exists P such that
(ι
[m]|
X [m]
S )
−1(P ) has dimension 0 by Lemma 3.2.

The asserted generic finiteness follows if X [m]
S is irreducible. To prove this
irreducibility, we use that XH◦ → H◦ is flat by construction, and so are the
morphisms X [m]
H◦ → H◦ and X [m]
S → S. Openness of flat morphisms [Gro67,
Thm. 2.4.6] implies that every irreducible component of X [m]
S dominates S, i.e.
its projection contains the generic point of S. But since Xs is geometrically
irreducible for all s ∈ H
◦(Q), there can be only one such irreducible component
of X [m]
S by [Gro67, Prop. 9.7.8]. □

3.3. Non-degeneracy. We keep the notation from the previous subsection, in
particular those in (3.5). For later applications of both the height inequality
of [DGH21, Thm. 1.6 and B.1] and the equidistribution result [K¨uh21, Thm. 1],
we need to work with appropriate non-degenerate subvarieties in certain families
of abelian varieties. Here, we give the main proposition providing such non-
degenerate subvarieties, inspired by a result of the second-named author [Ge24,
Prop. 3.4] and using a theorem of the first-named author [Gao20, Thm. 10.1].

Proposition 3.4. Let S ⊆ H
◦ be an irreducible subvariety and consider XS ⊆
AS → S. Writing ¯η for the geometric generic point of S, assume that the follow-
ing hypotheses hold true:

THE UNIFORM MORDELL–LANG CONJECTURE 17

(i) X¯η is an irreducible subvariety of A¯η;
(ii) Xs generates As for each s ∈ S(C);
(iii) the subvariety X¯η has finite stabilizer.

Then there exists m0 = m0(S) ≥ 1 such that X [m]
S is a non-degenerate subvariety
of A[m]
S for each m ≥ m0.

Non-degenerate subvarieties over C are defined as in [DGH21, Defn. 1.5 and
B.4]. A subvariety defined over Q is said to be non-degenerate if its base change
to C is non-degenerate.

Proof of Proposition 3.4. We wish to invoke [Gao20, Thm. 10.1.(i)] with t = 0. In
fact, as the conventions of [Gao20] deviate a litte bit from standard terminology,
we apply it in the formulation of [Gao21, Thm. 6.5.(i)].
All hypotheses of [Gao21, Thm. 6.5] are satisfied: indeed, hypothesis (a)
clearly holds true because we fixed r ≥ 1 at the beginning of this section, hy-
pothesis (b) holds true by (ii), and hypothesis (c) holds true by (iii). Thus we
can apply [Gao21, Thm. 6.5.(i)] to the abelian scheme AS → S and the subva-
riety XS. It yields that X [m]
S is non-degenerate if m ≥ dim S and ι
[m]|
X [m]
S is

generically finite. By Lemma 3.3 there exists m0 ≥ 1 such that ι
[m]|
X [m]
S is gener-
ically finite for each m ≥ m0. So the conclusion holds true with m0 replaced by
max{m0, dim S}. □

We conclude with a further lemma useful in later sections.

Lemma 3.5. For a (not necessarily irreducible) subvariety S ⊆ H◦, we define
the subset

Sgen := {s ∈ S(Q) : the stabilizer of Xs in As is finite, and Xs generates As}.(3.9)

Endow each irreducible component S′ of Sgen (the Zariski closure of Sgen in S)
with the reduced induced subscheme structure. Then XS′ ⊆ AS′ → S′ satisfies
the hypotheses (i)–(iii) of Proposition 3.4.

Proof. Let ¯η be the geometric generic point of S′.
To verify the condition (i), we can use again [Gro67, Prop. 9.7.8] as in
the proof of Lemma 3.3 above. As there, we simply use the fact that Xs′ is
(geometrically) irreducible for all s
′ ∈ H
◦(Q).
The condition (ii) clearly holds true, for example by Chevalley’s Theorem
on the upper semicontinuity of the fiber dimension [Gro67, Thm. 13.1.3].
To prove (iii), let C be the identity component of StabA¯η (X¯η). There
exists a quasi-finite dominant morphism ρ : S′′ → S′ such that C extends to an
abelian subscheme C of AS′′ = AS′ ×S′ S′′ → S′′. Clearly, Cs′′ ⊆ StabAs′′ (Xs′′)

18 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

for each s′′ ∈ S(Q). Since ρ(S′′) contains a Zariski open dense subset of S′,
there exists a point s
′ ∈ ρ(S′′)(Q) ∩ Sgen as in the previous paragraph. Choosing
a point s′′ ∈ S′′(Q) over s
′ ∈ S′(Q), the fiber As′′ is naturally identified with
As′, which also induces an identification of Xs′′ with Xs′. It follows that Cs′′ ⊆
StabAs′′ (Xs′′) = StabAs′ (Xs′). By the definition of Sgen (3.9), StabAs′ (Xs′) is
finite and hence Cs′′ is the identity element of As′′. Thus C is the zero section of
AS′′ → S′′, and C = C¯η is the origin of A¯η, whence (iii). □

4. Applying the height inequality

Proposition 4.1. Let g, l, r ≤ g and d be positive integers. There exist constants
c′
1 = c′
1(g, l, r, d) > 0, c
′
2 = c′
2(g, l, r, d) > 0 and c′
3 = c′
3(g, l, r, d) > 0 satisfying
the following property: For
• every polarized abelian variety (A, L) over Q of dimension g and degree
degL A = l, and
• every irreducible subvariety X of A with dim X = r, degL X = d and such
that X generates A,
the set

(4.1) {
x ∈ X ◦(Q) : ˆhL⊗[−1]∗L(x) ≤ c
′
1 max{1, hFal(A)} − c′
3} ,

is contained in X ′(Q) for a proper Zariski closed X ′ ⊊ X with degL(X ′) < c′
2.

For the proof of the proposition, we start by providing a similar result
(Proposition 4.2) for the universal families over the restricted Hilbert schemes
constructed in §3.2. Next, we deduce Proposition 4.1 in the case where (A, L) is
principally polarized. Finally, we handle the polarization type and prove the full
Proposition 4.1.

4.1. A preliminary result for restricted Hilbert schemes. We use the no-
tation from §3.2. In particular, we have a symmetric relatively ample line bun-
dle Lg on the universal abelian variety Ag → Ag with level-4-structure satisfy-
ing the following property: for each principally polarized abelian variety (A, L)
parametrized by b ∈ Ag(Q), we have c1(Lg|(Ag)b) = 2c1(L). If we identify
A = (Ag)b, then c1(Lg|A) = c1(L ⊗ [−1]∗L).
For each 1 ≤ r ≤ g and each d ≥ 1, we have the restricted Hilbert
scheme H◦ := Hr,d(Ag/Ag)
◦ from (3.6). Recall that it is a variety defined over Q
whose closed points parametrizes all pairs (X, (A, L)) of a principally polarized
abelian variety (A, L) and an irreducible subvariety X of A with dim X = r and
degL
⊗4
g |A X = d.
 THE UNIFORM MORDELL–LANG CONJECTURE 19

For AH◦ := Ag ×Ag H◦, we have a commutative diagram ((3.7) with m = 1)

(4.2) XH◦ ˜   //
 ""
AH◦

π

 ι // Ag

πuniv

H◦ ιH◦ // Ag

where π|XH◦ : XH◦ → H
◦ is the universal family. Every object in the diagram
(4.2) is a variety over Q, and every morphism is defined over Q.
Set L := ι
∗L⊗4
g . Notice that L is relatively very ample with respect to
AH◦ → H
◦.
Fix an ample line bundle M on a compactification Ag of Ag. The morphism
ιH◦ extends to a morphism ιH◦ : H◦ → Ag for some compactification H◦ of H◦.
We can do these constructions such that H◦ is a projective variety defined over
Q which contains H
◦ as a Zariski open dense subset. Set M := ιH◦ ∗M.

Proposition 4.2. Let S ⊆ H
◦ be a (not necessarily irreducible) subvariety de-
fined over Q. Let Sgen ⊆ S(Q) be the subset defined by (3.9).
There exist constants c′
1 = c′
1(r, d, S) > 0, c′
2 = c′
2(r, d, S) > 0 and c
′
3 =
c′
3(r, d, S) > 0 with the following property. For each s ∈ Sgen, the set

(4.3) Σs := {
x ∈ X ◦
s : ˆhL(x) ≤ c
′
1 max{1, hH◦,M(s)} − c′
3}

is contained in X ′(Q) for a proper Zariski closed X ′ ⊊ Xs with degLs(X ′) < c′
2.

This proposition is a generalization of the corresponding result for the uni-
versal curve [DGH21, Prop. 7.1], though our formulation here is closer to [Gao21,
Prop. 7.2]. Notice that the case S = H
◦ contains the full strength of the proposi-
tion. Furthermore, it is the only case we use below in the proof of Proposition 4.4.
However, the above formulation is more convenient for the proof by induction.

Proof of Proposition 4.2. It suffices to prove the proposition for S irreducible,
which we assume from now on.
For the proof, we use an induction on dim S. The base case dim S = 0 is
straightforward as we may choose c
′
3 large enough to render Σs empty.
Endow each irreducible component S′ of Sgen with the reduced induced
subscheme structure. Lemma 3.5 allows us to invoke Proposition 3.4 for XS′ ⊆
AS′ → S′. Let m0(S′) > 0 be as in Proposition 3.4, and let m = maxS′{m0(S′)}
with S′ running over all irreducible components of Sgen. Then X [m]
S′ is a non-
degenerate subvariety of A
[m]
S′ . Note that m = m(S) > 0 depends only on S.

20 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

Let X [m],∗
S′ be X [m]
S′ deprived of its 0-th degeneracy locus; a definition of
the 0-th degeneracy can be found in [Gao20, Defn. 1.6]. By [Gao20, Thm. 1.8],
it is a Zariski open subset of X [m]
S′ . It is defined over Q since X [m]
S′ is and it is
dense in X [m]
S′ because of the non-degeneracy of X [m]
S′ .
Consider the abelian scheme π[m] : A[m]
H◦ → H
◦.
Consider S′ \ π[m](X [m],∗
S′ ) endowed with the reduced induced subscheme
structure; it has dimension ≤ dim S′ − 1 ≤ dim S − 1. Let S1, . . . , Sk be the
irreducible components of ⋃
S′ S′\π[m](X [m],∗
S′ ) with S′ running over all irreducible
components of Sgen. The set {S1, . . . , Sk} is uniquely determined by S and m.
As m = m(S) > 0 depends only on S, it is actually already determined by S.
Let s ∈ Sgen(Q). Then either s ∈ ⋃k
i=1 Si(Q) or s ∈ π[m](X [m],∗
S′ )(Q) for
some irreducible component S′ of Sgen. For the remaining proof of the proposition,
we distinguish between these two cases.
Case (i): s ∈ ⋃k
i=1 Si(Q).

For each i ∈ {1, . . . , k}, we can apply the induction hypothesis to Si as
dim Si ≤ dim S − 1. In this way, we obtain constants c
′
i,1 = c′
i,1(r, d, Si) > 0,
c′
i,2 = c
′
i,2(r, d, Si) > 0, and c′
i,3 = c
′
i,3(r, d, Si) > 0 such that for each s ∈ Si(Q),
the set

(4.4) Σi,s := {
x ∈ X ◦
s (Q) : ˆhL(x) ≤ c′
i,1 max{1, hH◦,M(s)} − c′
i,3}

is contained in X ′(Q) for some proper Zariski closed X ′ ⊊ Xs with degLs(X ′) <
c′
i,2. Let c′
deg,1 = min1≤i≤k{c
′
i,1} > 0, c′
deg,2 = max1≤i≤k{c
′
i,2} > 0 and c′
deg,3 =
max1≤i≤k{c
′
i,3} > 0. As the set {S1, . . . , Sk} is uniquely determined by S, the
constants c
′
deg,1, c′
deg,2 and c′
deg,3 depend only on g, d, r and S. Moreover, for each
s ∈ ⋃k
i=1 Si(Q), the set

(4.5) Σdeg,s := {
x ∈ X ◦
s (Q) : ˆhL(x) ≤ c
′
deg,1 max{1, hH◦,M(s)} − c′
deg,3}

must be contained in Σi,s for some i. So Σdeg,s is contained in X ′(Q) for some
proper Zariski closed X ′ ⊊ Xs with degLs(X ′) ≤ c
′
deg,2. This concludes the
induction step in Case (i).

Case (ii): s ∈ π[m](X [m],∗
S′ )(Q) for some irreducible component S′ of Sgen.

By the height inequality [DGH21, Thm. 1.6] (in the version of [Gao21,
Thm. 7.1]), there exist constants c = c(S′) > 0 and c′ = c
′(S′) such that

(4.6) ˆhL(x1) + · · · + ˆhL(xm) ≥ chH◦,M(s) − c′

THE UNIFORM MORDELL–LANG CONJECTURE 21

for all (x1, . . . , xm) ∈ (X [m],∗
S′ )s(Q). We set c
′
S′,1 = c/m and c′
S′,3 = (c + c
′)/m;
these constants depend only on S′ and m. Consider

(4.7) ΣS′,s = {
x ∈ X ◦
s (Q) : ˆhL(x) ≤ c′
S′,1 max{1, hH◦,M(s)} − c′
S′,3} ⊆ Xs(Q).

If Σm
S′,s ∩ X [m],∗
S′ (Q) were non-empty, then there would exist some

(x1, . . . , xm) ∈ Σm
S′,s ∩ X [m],∗
S′ (Q),

in contradiction of the height inequality (4.6). Hence Σ
m
S′,s ⊆ (X [m]
S′ \X [m],∗
S′ )s(Q).
Our case assumption implies (X [m],∗
S′ )s ̸= ∅ and thus

X m
s = (X [m]
S′ )s ̸= (X [m]
S′ \ X [m],∗
S′ )s.

We may hence apply Lemma 4.3 below to X = Xs, L = Ls|Xs, Z = (X [m]
S′ \
X [m],∗
S′ )s and Σ = ΣS′,s. It yields a Zariski closed subset X ′ of Xs such that

(i) X ′ ⊊ Xs,
(ii) degLs(X ′) < c(m, r, d, degL⊠m
s (X [m]
S′ \ X [m],∗
S′ )s), and
(iii) ΣS′,s ⊆ X ′(Q).

The degree degL⊠m
s (X [m]
S′ \ X [m],∗
S′ )s is bounded from above solely in terms
of S′ and m. Hence (ii) implies a bound of the form degLs(X ′) < c′
S′,2 with c′
S′,2
depending only on m, r, d and S′. In summary, the set ΣS′,s defined in (4.7) is
contained in X ′(Q) for a proper Zariski closed X ′ ⊊ Xs with degLs(X ′) < c
′
S′,2.
Letting S′ runs over all irreducible components of Sgen, we set c
∗′
1 :=
minS′{c
′
S′,1} > 0, c∗′
2 := maxS′{c
′
S′,2} > 0 and c
∗′
3 := maxS′{c
′
S′,3} > 0. As
the Zariski closed subset Sgen of S is determined by S, so are its irreducible
components S′. Moreover, m = m(S) > 0 depends only on S. Therefore, the
constants c∗′
1 , c∗′
2 and c∗′
3 can be expressed only in terms of r, d and S.
Let us summarize the result of the above discussion: For each s ∈ ⋃

S′ π[m](X [m],∗
S′ )(Q),
the set

(4.8) Σ
∗
s := {
x ∈ X ◦
s (Q) : ˆhL(x) ≤ c∗′
1 max{1, hH◦,M(s)} − c∗′
3 }

must be contained in ΣS′,s for some S′; thus Σ∗
s is contained in X ′(Q) for some
proper Zariski closed X ′ ⊊ Xs with degLs(X ′) < c
∗′
2 . This concludes the proof in
Case (ii). □

22 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

Lemma 4.3. Let k be a field, X an irreducible projective variety over k and L a
very ample line bundle on X. Consider a closed subvariety Z ⊊ X M . Then there
exists a constant
 c = c(M, dim X, degL X, degL⊠M (Z)) > 0

such that, for any subset Σ ⊆ X(k) satisfying ΣM ⊆ Z(k), there exists a proper
Zariski closed X ′ ⊊ X with Σ ⊆ X ′(k) and degL(X ′) < c.

Proof. We prove this lemma by induction on M . The base case M = 1 is trivial
as one may take X ′ := Z.
Assume next that the lemma is proved for 1, . . . , M − 1 ≥ 1. Let q : X M →
X be the projection to the first factor. We write Z ′ for the union of all irreducible
components Y of Z such that q(Y ) = X and Z ′′ for the union of the other
components. Setting Σ′′ := q (
Σ
M ∩ Z ′′(k)
)
, we notice that (Σ \ Σ
′′) × ΣM −1 ⊆
Z ′(k). By [Gro67, Thm. 13.1.3 and Prop. 13.2.3], the fiber q|
−1
Z′ (P ) over a generic
point P ∈ X has dimension

dim Z ′ − dim X < M · dim X − dim X = (M − 1) dim X,

and the set
 W := {P ∈ X : {P } × X M −1 ⊆ Z ′} ⊊ X

is Zariski closed in X.
Case (i): Σ \ Σ′′ ̸⊆ W (k).

Take a point P ∈ Σ \ Σ′′ such that P /∈ W (k) and set Z1 := Z ′ ∩ ({P } ×
X M −1). Since {P } × Σ
M −1 ⊆ Z ′(k), we can apply the induction hypothesis for
M − 1, Σ ⊆ X(k) and Z1 ⊆ X M −1, tacitly identifying {P } × X M −1 with X M −1.
It implies the existence of a closed subvariety X ′ ⊊ X such that Σ ⊆ X ′(k) and

(4.9) degL(X ′) < c(M − 1, dim X, degL X, degL⊠(M −1)(Z1)).

We claim that the constant on the right hand side can be expressed solely in
terms of M , dim X, degL(X) and degL⊠M (Z); this evidently suffices to complete
the proof in this case. Indeed, we have

degL⊠(M −1)(Z1) = degL⊠M (Z ′ ∩ ({P } × X M −1))

and
 degL⊠M (Z ′ ∩ ({P } × X M −1)) ≤ degL⊠M (Z ′) degL⊠(M −1)(X M −1)

THE UNIFORM MORDELL–LANG CONJECTURE 23

by B´ezout’s theorem. Using (2.6) inductively by taking Y := X and Y ′ := X i

for i = 1, 2, ..., M − 2, we have

degL⊠(M −1)(X M −1) = ((M − 1) dim X)!
((dim X)!)M −1 (degL X)
M −1.

Moreover degL⊠M (Z ′) ≤ degL⊠M (Z). In conclusion, we get

degL⊠(M −1)(Z1) ≤ ((M − 1) dim X)!
((dim X)!)M −1 degL⊠M (Z)(degL X)
M −1.

Hence the right hand side of (4.9) depends only on M , dim X, degL X and
degL⊠M (Z). This proves the claim and ends the proof.
Case (ii): Σ \ Σ′′ ⊆ W (k).

In this case, (Σ \ Σ′′) × X M −1 ⊆ Z ′. We also assume that k is algebraically
closed, which we may by enlarging the base field if needed. As Z ′ ⊊ X M , there
exists a point x ∈ X M −1(k) such that (X × {x}) ∩ Z ′ ̸= X × {x}. Thus (X ×
{x}) ∩ Z ′ = X ′′ × {x} for some closed subset X ′′ ⊊ X. We have Σ \ Σ
′′ ⊆ X ′′(k)
by construction, and

degL X ′′ ≤ degL⊠M (X × {x}) degL⊠M (Z) = degL X degL⊠M (Z)

by B´ezout’s theorem.
To control the points in Σ
′′, note that the closed subset q(Z ′′) is properly
contained in X by definition. Moreover, we have

degL q(Z ′′) ≤ degL⊠M (Z ′′) ≤ degL⊠M (Z);

the first inequality follows again from [Dil22, Lem. 2.4]. In summary, it suffices
to take X ′ := X ′′ ∪ q(Z ′′) ⊊ X in this case. □

4.2. The case of principally polarized abelian varieties. We next prove
Proposition 4.1 in the special case of principally polarized abelian varieties.

Proposition 4.4. Let g, r and d be positive integers. There exist constants
c′
1 = c
′
1(g, r, d) > 0, c′
2 = c′
2(g, r, d) > 0 and c′
3 = c′
3(g, r, d) > 0 satisfying the
following property: For
• every principally polarized abelian variety (A, L) defined over Q of dimen-
sion g,
• and every irreducible subvariety X of A with dim X = r and degL X = d
generating A,

24 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

the set
 Σ := {
x ∈ X ◦(Q) : ˆhL⊗[−1]∗L(x) ≤ c′
1 max{1, hFal(A)} − c′
3}

is contained in X ′(Q) for some proper Zariski closed X ′ ⊊ X with degL(X ′) < c′
2.

Proof. For simplicity denote by L− := [−1]
∗L.
Let Ag → Ag and Lg be as from the beginning of §4.1. Then each principally
polarized abelian variety (A, L) defined over Q gives rise to a point b ∈ Ag(Q),
such that A ∼= (Ag)b and c1(Lg|(Ag)b) = 2c1(L) = c1(L ⊗ L−). In the rest of the
proof, we identify A with (Ag)b.
Let X be an irreducible subvariety of A generating A such that d = degL X
and r = dim X. We may assume r ≥ 1 because otherwise the result is trivial.
We have

(4.10) degL
⊗4
g |A X = (4c1(Lg|A))
r · [X] = (8c1(L))
r · [X] = 8r degL X = 8rd.

Consider the restricted Hilbert scheme H◦ := H
◦
r,8rd(Ag/Ag) from (3.6) and
recall the commutative diagram (4.2)

XH◦ ˜   //
 ""
AH◦

π

 ι // Ag

πuniv

H◦ ιH◦ // Ag

of varieties and morphisms defined over Q. Note that π|XH◦ : XH◦ → H◦ is the
universal family.
The pair (X, (A, L)) is parametrized by a point s ∈ H
◦(Q) such that X =
Xs, A = As = (Ag)b and ιH◦(s) = b.

For the line bundle M = ιH◦ ∗M on H◦ defined above Proposition 4.2, we
have
 hH◦,M(s) = hAg,M(ιH◦(s)) = hAg,M(b).

By fundamental work of Faltings [MB85, Thm. 1.1], hFal(A) is bounded from
above in terms of hAg,M(b) = hH◦,M(s) and g only. More precisely,

max{1, hFal(A))} ≤ c(g)hH◦,M(s) + c′(g) log(hH◦,M(s) + 2)(4.11)
 ≤ (c(g) + c
′(g))hH◦,M(s) + 2c′(g)

for some constants c(g) > 0 and c
′(g) > 0.

THE UNIFORM MORDELL–LANG CONJECTURE 25

For the line bundle L = ι
∗L
⊗4
g on AH◦ defined above Proposition 4.2, we
have L|As = L
⊗4
g |(Ag)ι(s) = L
⊗4
g |(Ag)b, and hence L|A = L
⊗4
g |A via the identification
A = As = (Ag)b fixed above. Thus c1(L|A) = 4c1(L ⊗ L−). Moreover, both L|A
and (L ⊗ L−)
⊗4 are symmetric and ample on A, so Lemma 2.3 implies

(4.12) ˆhL|A(x) = 4ˆhL⊗L−(x) for each x ∈ A(Q).

Let H◦
gen be the subset of H◦(Q) as defined by (3.9). If the stabilizer
StabA(X) of X in A has positive dimension, then X ◦ = ∅ by the definition of the
Ueno locus and hence the proposition trivially holds true. Therefore, we may and
do assume that StabA(X) is finite. Then the point s ∈ H◦(Q) parameterizing
(X, (A, L)) is in H
◦
gen.
Invoking Proposition 4.2 with S = H◦, we obtain constants c′
1, c
′
2 and c′
3
depending only on r, 8
rd and H◦ (and hence ultimately only on g, d and r) and
a proper Zariski closed X ′ ⊊ X with degL|A(X ′) < c′
2 such that the set

Σs := {
x ∈ X ◦(Q) : ˆhL|A(x) ≤ c
′
1 max{1, hH◦,M(s)} − c′
3}

is contained in X ′(Q).
Notice that degL(X ′) < degL|A(X ′) because of 8c1(L) = c1(L|A) and hence
degL(X ′) < c′
2.
By (4.11) and (4.12), we have
{x ∈ X ◦(Q) : ˆhL⊗L−(x) ≤ c′
1
4(c(g) + c′(g)) max{1, hFal(A)} − c′
3 + 2c′
1
4
 } ⊆ Σs

We are done on replacing c
′
1 with c′
1/4(c(g) + c′(g)) and c
′
3 with (c′
3 + 2c
′
1)/4. □

4.3. Proof of Proposition 4.1. Let (A, L) be a polarized abelian variety with
degL A = l and let X be an irreducible subvariety generating A and such that
degL X = d.
By Lemma 2.2.(iv), there exists a principally polarized abelian variety
(A0, L0) and an isogeny u0 : A → A0 such that L = u
∗
0L0; moreover, deg(u0) =
l/g!. A basic property of the Faltings height [Ray85, Prop. 1.4.1] yields the bound

(4.13) |hFal(A) − hFal(A0)| ≤ 1
2 log deg u0 = 1
2 log(l/g!).

It is well-known that there exists an isogeny u : A0 → A such that u0 ◦ u =
[deg u0] on A0. So u
∗L = (u0 ◦ u)∗L0 = [l/g!]∗L0, and deg u = (deg u0)
2g−1 =
(l/g!)
2g−1.

26 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

Let X0 be an irreducible component of u−1(X). Then u(X0) = X as u is
´etale and X0 generates A0. By the projection formula [Ful98, Prop. 2.5], we have

(4.14) d′ := degu∗L X0 = c1(u
∗L)
dim X · [X0]

= deg(u|X0) · (c1(L)
dim X · [X]) ≤ deg(u) · degL X = d(l/g!)
2g−1.

It is easy to infer from the definition of the Ueno locus that X ◦ = u(X0)◦ ⊆ u(X ◦
0 ).
Let c′
0,1(g, r, d
′) > 0, c′
0,2(g, r, d
′) > 0 and c
′
0,3(g, r, d
′) > 0 be the constants
from Proposition 4.4 with d replaced by d′. Set

c′
1 := min
1≤d′≤d(l/g!)2g−1{c′
0,1(g, r, d
′)} > 0,

c′
2 := max
1≤d′≤d(l/g!)2g−1{c′
0,2(g, r, d
′)} > 0,

and
 c
′
3 := max
1≤d′≤d(l/g!)2g−1{c′
0,3(g, r, d
′)} > 0.

Then c′
1, c
′
2 and c′
3 depend only on g, r and d. Proposition 4.4 yields the following
assertion: the set

Σ0 := {
x0 ∈ X ◦
0 (Q) : ˆhL0⊗[−1]∗L0(x0) ≤ c
′
1 max{1, hFal(A0)} − c′
3}

is contained in X ′
0(Q) for a proper Zariski closed X ′
0 ⊊ X0 with degL0(X ′
0) ≤ c
′
2.
Let

Σ := {
x ∈ X ◦(Q) : (g!/l)2ˆhL⊗[−1]∗L(x) ≤ c
′
1 max{1, hFal(A)} − c′
3 − (1/2) log(l/g!)} .

As X ◦ ⊆ u(X ◦
0 ) and u∗(L ⊗ [−1]
∗L) ∼= (L0 ⊗ [−1]
∗L0)
⊗(l/g!)2, (4.13) yields Σ ⊆
u(Σ0).
Set X ′ := u(X ′
0). Then X ′ ⊊ X, Σ ⊆ X ′(Q), and

degL X ′ = c1(L)
dim X ′ · [X ′] ≤ c1(u
∗L)
dim X ′ · [X ′
0] = degu∗L X ′
0 ≤ c
′
2.

Replacing c
′
1 with (l/g!)
2c′
1 and c
′
3 with (l/g!)
2(c
′
3 + (1/2) log(l/g!)), we obtain the
assertion of Proposition 4.1. □

THE UNIFORM MORDELL–LANG CONJECTURE 27

5. Applying equidistribution

Proposition 5.1. Let g, l, r and d be positive integers. There exist constants
c′′
2 = c
′′
2(g, l, r, d) > 0 and c
′′
3 = c
′′
3(g, l, r, d) > 0 with the following property. For

• every polarized abelian variety (A, L) of dimension g defined over Q with
degL A = l, and
• every irreducible subvariety X ⊆ A generating A with dim X = r and
degL X = d,
the set

(5.1) Σ := {
x ∈ X ◦(Q) : ˆhL⊗[−1]∗L(x) ≤ c
′′
3}

is contained in X ′(Q) for a proper Zariski closed X ′ ⊊ X with degL(X ′) < c′′
2.

The main idea of the proof this proposition is similar to that of the proof
of Proposition 4.1: We put the various pairs of polarized abelian varieties (A, L)
and subvarieties X ⊂ A into finitely many families over the components of the
restricted Hilbert scheme constructed in (3.6). The technical core of this section is
a related result for each such family (Proposition 5.2). To achieve the uniformity
as stated, we need to do however also a careful bookkeeping.

5.1. A preliminary result for the restricted Hilbert scheme. We retain
the notation from §4.1. In particular πuniv : Ag → Ag is the universal abelian
variety over the fine moduli space of principally polarized abelian varieties with
level-4-structure, and Lg is a symmetric relatively ample line bundle Lg on Ag/Ag
satisfying the following property: for each principally polarized abelian variety
(A, L) parametrized by b ∈ Ag(Q), we have c1(Lg|(Ag)b) = 2c1(L).
For each 1 ≤ r ≤ g and each d ≥ 1, let H
◦ := Hr,d(Ag/Ag)◦ be the
restricted Hilbert scheme from (3.6); recall that its Q-points parametrize all pairs
(X, (A, L)) of a principally polarized abelian variety (A, L) and an irreducible
subvariety X ⊆ A with dim X = r and degL
⊗4
g |A X = d.
We have a commutative diagram over Q ((3.7) with m = 1)

(5.2) XH◦ ˜   //
 ""
AH◦

π

 ι // Ag

πuniv

H◦ ιH◦ // Ag

where π|XH◦ : XH◦ → H
◦ is the universal family. Set L := ι∗L
⊗4
g .

28 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

Proposition 5.2. Let S ⊆ H◦ be a (not necessarily irreducible) subvariety and
let Sgen ⊆ S(Q) be the subset defined by (3.9).
There exist constants c
′′
2 = c
′′
2(r, d, S) > 0 and c
′
3 = c
′′
3(r, d, S) > 0 such that
the following property holds true. For each s ∈ Sgen(Q), the set

(5.3) Σs := {
x ∈ X ◦
s (Q) : ˆhL(x) ≤ c′′
3}

is contained in a proper Zariski closed subset X ′ ⊊ Xs with degLs(X ′) < c′′
2.

This proposition is a generalization of [K¨uh21, Prop. 21] on families of
curves. For convenience of the reader, we divide the proof into five steps. The
goal of the first four steps is to run a family version of the classical approach of
Ullmo [Ull98] and Zhang [Zha98] to the Bogomolov conjecture in order to obtain
a generic lower bound on heights that are closely related to ˆhL, which is our
height of interest. In the final step, we then deduce Proposition 5.2 from this
height bound. As in the proof of Proposition 4.2, we use Lemma 4.3 to deal with
the non-generic points for which we do not obtain a height bound; this gives rise
to the exceptional set X ′.
This family version of the Ullmo–Zhang approach differs from the classical
one mainly in two aspects. First, a version of equidistribution is used that applies
to families of abelian varieties; for our purpose, [K¨uh21, Thm. 1] or the more
general results [YZ26, Thm. 6.7] and [Gau26] are sufficient replacements of the
classical equidistribution result of Szpiro–Ullmo–Zhang [SUZ97]. Second and
in contrast to [SUZ97], a new condition, namely non-degeneracy as defined in
[DGH21, Defn. B.4], has to be verified for the subvarieties under consideration.
Notice that every subvariety is non-degenerate in the case of a single abelian
variety. So this extra verification is a genuinely new aspect of working in families
and in practice this step is often very difficult.

Proof of Proposition 5.2. Decomposing S into its irreducible components, it suf-
fices to prove the proposition for irreducible S.
We prove the proposition by induction on dim S. The base case dim S = 0
is in fact contained in the first three steps of the following proof. In contrast to
Proposition 4.2 it is a highly non-trivial statement, namely the classical Bogo-
molov conjecture. One could alternatively cite [Ull98, Zha98] for the base case
and hence we do not state its proof separately as an induction start here. The in-
duction hypothesis is only utilized in Step 5 and is unnecessary in case dim S = 0.

Step 1: Construction of non-degenerate subvarieties

Endow each irreducible component S′ of Sgen with the reduced induced
subscheme structure. Lemma 3.5 allows us to invoke Proposition 3.4 for XS′ ⊆
AS′ → S′.
 THE UNIFORM MORDELL–LANG CONJECTURE 29

Let m0(S′) > 0 be from Proposition 3.4, and let m = maxS′{m0(S′)} with
S′ running over all irreducible components of Sgen. Then X [m]
S′ is a non-degenerate
subvariety of A
[m]
S′ by Proposition 3.4. Notice that m > 0 depends only on S. Let
us write ωm for the Betti form on A[m]
S′ . By [DGH21, Prop. 2.2.(iii)], there exists
a point z ∈ (X [m]
S′ )
sm(C) such that

(5.4) (ωm|
∧(rm+dim(S′))

X [m]
S′ (C) )z ̸= 0.

Since this condition on z is open (in the usual topology), we may and do assume
that z lies over a smooth point of S′.
For each M ≥ 1, we consider the proper S′-morphism

D0 : (A
[m]
S′ )
[M +1] −→ (A[m]
S′ )[M ](5.5)
 (a0, a1, . . . , aM ) ↦−→ (a1 − a0, . . . , aM − a0),

using the fiberwise group structure.
Let ¯η be the geometric generic point of S′. By the proof of [Zha98, Lem. 3.1],
there exists M0(S′) > 0 with the following property: For each M ≥ M0(S′),
the generic fiber of the restriction of D0 to X m(M +1)
¯η is an orbit under the ac-
tion of StabAm
¯η (X m
¯η ) ⊆ A
m
¯η diagonally embedded into (Am
¯η )M +1. Notice that
StabAm
¯η (X m
¯η ) = StabA¯η (X¯η)
m is finite by the definition of Sgen. We set M =
maxS′{M0(S′)} > 0 where S′ runs over all irreducible components of Sgen. Then
M = M (S) > 0 depends only on S.
We further define the S′-morphism

D ′
0 := (id, D0) : A[m]
S′ ×S′ (A
[m]
S′ )
[M +1] −→ A[m]
S′ ×S′ (A
[m]
S′ )[M ]

and its restriction

(5.6) D : X [m]
S′ ×S′ (X [m]
S′ )[M +1] = X [m(M +2)]
S′ −→ D ′
0(X [m(M +2)]
S′ ).

(Note that we also (co-)restrict on the range to simplify our notation.) For later
use, we set
 G¯η := {0} × StabA¯η (X¯η)m ⊆ A
m
¯η × (Am
¯η )
M +1 = A
m(M +2)
¯η ;

then the fibers of D|η are naturally orbits under Gη.
The subvarieties

X [m(M +2)]
S′ ⊆ A
[m(M +2)]
S′ and D(X [m(M +2)]
S′ ) ⊆ A
[m(M +1)]
S′

30 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

are both non-degenerate. For the former one, this follows directly from our choice
of m. For the latter one, we remark that

D(X [m(M +2)]
S′ )) = X [m]
S′ ×S′ D0((X [m]
S′ )[M +1]),

whose non-degeneracy follows from the non-degeneracy of X [m]
S′ ; see for example
[K¨uh21, Lem. 24] or [Gao21, Lem. 6.2].

Step 2: Defining non-proportional measures µS′,1 and D ∗µS′,2 on A[m(M +2)]
S′ (C)

Write ωm(M +2) (resp. ωm(M +1)) for the Betti form on A
[m(M +2)]
S′ (C) (resp.
A
[m(M +1)]
S′ (C)). Furthermore, let µS′,1 (resp. µS′,2) on X [m(M +2)]
S′ (C) (resp. D(X [m(M +2)]
S′ )(C))
be the equilibrium measure for which [K¨uh21, Thm. 1] holds. By its proof (com-
pare the end of Section 3 in [K¨uh21]), the measure µS′,1 (resp. µS′,2) is propor-
tional to the restriction of

(ωm(M +2))
∧(rm(M +2)+dim(S′)) (resp. (ωm(M +1))
∧(rm(M +2)+dim(S′))).)

We use this to prove that the measures µS′,1 and D ∗µS′,2 are non-proportional.
In particular, µS′,1 ̸= D ∗µS′,2.
For every point t ∈ (X [m]
S′ )(C), write

∆t := (t, . . . , t) ∈ (X [m]
S′ )
[M +1](C) = X [m(M +1)]
S′ (C).

for its (M + 1)-fold self product. For the point z ∈ (X [m]
S′ )
sm(C) chosen above
(5.4), the point (z, ∆z) is a smooth point of (X [m]
S′ ×S′ (X [m]
S′ )[M +1])(C) and

(µS′,1)(z,∆z) ̸= 0;

see for example [K¨uh21, Lem. 11 and 25].
By definition, we have D((z, ∆z)) = (z, 0, . . . , 0) and hence

D −1D((z, ∆z)) = {(z, ∆t) | t ∈ X [m]
S′ (C)}.

As this is of dimension rm + dim S′ > 0 locally at (z, ∆z), the differential

dD : T(z,∆z)X [m(M +2)]
S′ −→ TD(z,∆z)D(X [m(M +2)]
S′ )

has a non-trivial kernel. So
 (D ∗µS′,2)(z,∆z) = 0,

and, consequently, µS′,1 ̸= D ∗µS′,2.

THE UNIFORM MORDELL–LANG CONJECTURE 31

Step 3: Choice of test functions fS′,1, fS′,2 and εS′ > 0
As µS′,1 ̸= D ∗µS′,2, there exists a constant ϵS′ > 0 as well as a function
fS′,1 ∈ C 0
c (X [m(M +2)]
S′ (C)) such that

(5.7)
 ∣
∣
∣
∣
∣
∫

X [m(M +2)]
S′ (C) fS′,1µS′,1 − ∫

X [m(M +2)]
S′ (C) fS′,1D ∗µS′,2
∣
∣
∣
∣
∣ > 2εS′.

This is, however, not enough for our purposes. We want fS′,1 to be of the form

fS′,1 = fS′,2 ◦ D

for some fS′,2 ∈ C 0
c (D(X [m(M +2)]
S′ )(C)).
To achieve this goal, let Gη be the finite group defined in Step 1. By
abuse of notation denote the projection by π : A
[m(M +2)]
S′ → S′. There exists a
Zariski open dense U ⊆ S′ such that Gη extends to a flat group scheme G over
U . Furthermore, there exists a Zariski open dense subset V ⊆ D(X [m(M +2)]
U )
such that D|D −1(V ) : D −1(V ) → V is finite ´etale and each of its fibers D −1(y),
y ∈ V (C), is a Gπ(y)-orbit, where Gπ(y) is the restriction of G to the fiber over
π(y). We may and do assume that fS′,1 is supported in V ⊆ π−1(U ) without
compromising (5.7). Furthermore, we can replace fS′,1 by

fS′,1 : X [m(M +2)]
U −→ R

(z0, z1, . . . , zM ) ↦−→ ∑

t∈Gs fS′,1(z0 + t, . . . , zM + t)

where Gs is the restriction of G to the fiber over s = π(z0, . . . , zM ) and (5.7)
remains valid; indeed, both µS′,1 and µS′,2 are translation invariant since they are
exterior powers of Betti forms, which are translation invariant.
In summary, fS′,1 is constant on the fibers of D. Since its support is con-
tained in the locus where D is ´etale, there exists a unique function fS′,2 such that
fS′,1 = fS′,2 ◦ D.

Step 4: Obtaining a height lower bound via equidistribution
We apply the equidistribution result [K¨uh21, Thm. 1] in the form of [K¨uh21,
Lem. 23] twice. Applied to X [m(M +2)]
S′ , fS′,1 and εS′, we obtain a constant δεS′ ,1 >
0 and a Zariski closed subset ZS′,1 ⊊ X [m(M +2)]
S′ such that

(5.8)
 ∣
∣
∣
∣
∣
∣

∫

X [m(M +2)]
S′ (C) fS′,1µS′,1 − 1
#O(x)
 ∑

y∈O(x) fS′,1(y)

∣
∣
∣
∣
∣
∣ < εS′

32 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

for all x ∈ (X [m(M +2)]
S′ \ ZS′,1)(Q) with ˆhL⊠m(M +2)(x) ≥ δεS′ ,1; here O(x) is the
Galois orbit of x (over Q). Applying the lemma to D(X [m(M +2)]
S′ ), fS′,2 and εS′,
we obtain similarly a constant δεS′ ,2 > 0 and a Zariski closed subset ZS′,2 ⊊
D(X [m(M +2)]
S′ ) such that

(5.9)
 ∣
∣
∣
∣
∣
∣

∫

D(X [m(M +2)]
S′ )(C) fS′,2µS′,2 − 1
#O(x′)
 ∑

y′∈O(x′) fS′,2(y′)
∣
∣
∣
∣
∣
∣ < εS′

for all x
′ ∈ (D(X [m(M +2)]
S′ ) \ ZS′,2)(Q) with ˆhL⊠m(M +1)(x
′) ≥ δεS′ ,2.
Set δS′ := min{δεS′ ,1, δεS′ ,2} > 0 and define the Zariski closed set ZS′ =
ZS′,1 ∪ D −1(ZS′,2). Note that ZS′ ̸= X [m(M +2)]
S′ as D is generically finite.

Claim: For each point x ∈ (X [m(M +2)]
S′ \ ZS′)(Q), we have

(i) either ˆhL⊠m(M +2)(x) ≥ δS′,
(ii) or ˆhL⊠m(M +1)(D(x)) ≥ δS′.

Indeed, assume both conditions were violated. Then (5.8) would hold true,
and (5.9) with x
′ = D(x) would also hold true.
But
 1
#O(x)
 ∑

y∈O(x) fS′,1(y) = 1
#O(D(x))
 ∑

y′∈O(D(x)) fS′,2(y′)

because fS′,1 = fS′,2 ◦ D. So we would have
∣
∣
∣
∣
∣

∫

X [m(M +2)]
S′ (C) fS′,1µS′,1 − ∫

D(X [m(M +2)]
S′ )(C) fS′,2µS′,2
∣
∣
∣
∣
∣ ≤ 2εS′,

which contradicts (5.7) as fS′,1 = fS′,2 ◦ D. This finishes the proof of the claim.
Before moving on, let us take a closer look at the constants and objects
obtained up to now. In Step 1, we introduced the integers m = m(S) > 0 and
M = M (S) > 0, which depend only on S. The measures µS′,1 and µS′,2 from
Step 2 clearly depend only on S′, m and M , and so do the test functions fS′,1,
fS′,2 and the constant εS′ > 0 chosen in Step 3. In this step, we obtained a closed
subvariety ZS′ ⊊ X [m(M +2)]
S′ and a constant δS′ for each irreducible component S′

of Sgen; these depend only on fS′,1, fS′,2 and εS′ > 0 and hence ultimately only
on S′, m and M .

Step 5: Conclusion and induction step

THE UNIFORM MORDELL–LANG CONJECTURE 33

The argument of this step is similar to the proof of Proposition 4.2. The
main difference is that the the height inequality [DGH21, Thm. 1.6 and B.1] is
replaced by the height lower bound from Step 4.
By abuse of notation, let π : AS′ → S′ denote the structural morphism.
Consider the complement S′ \ π(X [m(M +2)]
S′ \ ZS′) endowed with its reduced in-
duced subscheme structure; it has dimension ≤ dim S′ − 1 ≤ dim S − 1. Let
S1, . . . , Sk be the irreducible components of ⋃
S′ S′ \ π(X [m(M +2)]
S′ \ ZS′) with S′

running over all irreducible components of Sgen. The set {S1, . . . , Sk} is uniquely
determined by S, m and M . As both m and M depend only on S, the set
{S1, . . . , Sk} is actually completely determined by S.
As in the proof of Proposition 4.2, we need to distinguish two cases in order
to prove the proposition for a given s ∈ Sgen(Q).

Case (i): s ∈ ⋃k
i=1 Si(Q).

Since dim Si ≤ dim S − 1 for all i ∈ {1, . . . , k}, we can apply the induc-
tion hypothesis for each subvariety Si separately. This yields constants c′′
i,2 =
c′′
i,2(r, d, Si) > 0 and c′′
i,3 = c
′′
i,3(r, d, Si) > 0 such that, for each s ∈ Si(Q), the set

(5.10) Σi,s := {
x ∈ X ◦
s (Q) : ˆhL(x) ≤ c′′
i,3}

is contained in X ′(Q) for a proper Zariski closed X ′ ⊊ Xs with degLs(X ′) < c
′′
i,2.
Set c′′
deg,2 := max1≤i≤k{c′′
i,2} > 0 and c
′′
deg,3 := min1≤i≤k{c
′′
i,3} > 0. As the set
{S1, . . . , Sk} is completely determined by S, the constants c
′′
deg,2 and c′′
deg,3 depend
only on r, d and S.
For each s ∈ ⋃k
i=1 Si(Q), the set

(5.11) Σdeg,s := {
x ∈ X ◦
s (Q) : ˆhL(x) ≤ c′′
deg,3}

must be contained in Σi,s for some i. Therefore, Σdeg,s is contained in X ′(Q) for
some proper Zariski closed X ′ ⊊ Xs with degLs(X ′) < c′′
deg,2. This proves the
assertion of the proposition in this case.
Case (ii): s ∈ π(X [m(M +2)]
S′ \ ZS′)(Q) for some irreducible component S′ of
Sgen.
 Set c′′
S′,3 = δS′/4m(M + 2) and consider

(5.12) ΣS′,s = {
x ∈ X ◦
s (Q) : ˆhL(x) ≤ c
′′
S′,3} ⊆ Xs(Q).

We claim that

(5.13) Σ
m(M +2)
S′,s ⊆ Zs(Q).

34 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

Assume to the contrary that there exists some x = (x1, . . . , xm(M +2)) ∈ (Σm(M +2)
S′,s \
Zs)(Q). Then,

ˆhL⊠m(M +2)(x) =
 m(M +2)∑

i=1 ˆhL(xi) ≤ m(M + 2)c′′
S′,3 < δS′

and

ˆhL⊠m(M +1)(D(x)) =
 m∑

i=1 ˆhL(xi)+
 M∑

i=2
 m∑

j=1 ˆhL(xi·m+j −xm+j) ≤ 4m(M +1)c′′
S′,3 < δS′.

This contradicts the alternative height bounds obtained in Step 4, establishing
the claim.
By the assumption of this case, X m(M +2)
s ̸= Zs. Therefore, we can apply
Lemma 4.3 to X = Xs, L = Ls|Xs, Z = Zs and Σ = ΣS′,s. In this way, we obtain
a proper Zariski closed X ′ ⊊ Xs such that
(i) degLs(X ′) ≤ c(m(M + 2), r, d, degL⊠m
s Zs), and
(ii) ΣS′,s ⊆ X ′(Q).
As the degree degL⊠m
s Zs depends only on S′, m and M , property (i) sim-
plifies to degLs(X ′) ≤ c
′′
S′,2 with a constant c′′
S′,2 depending only on r, d, S′, m
and M . In summary, the set ΣS′,s is contained in X ′(Q) for some Zariski closed
X ′ ⊊ Xs with degLs(X ′) ≤ c′′
S′,2.
Set c∗′′
2 := maxS′{c′′
S′,2} > 0 and c∗′′
3 := minS′{c′′
S′,3} > 0 where S′ runs over
all irreducible components of Sgen. The subset Sgen of S is uniquely determined by
S. Hence the set {S′} of irreducible components of Sgen is uniquely determined
by S. Moreover m = m(S) > 0 and M = M (S) > 0 depend only on S.
Consequently, the constants c
∗′′
2 and c∗′′
3 depend only on r, d and S.
For each s ∈ ⋃

S′ π(X [m(M +2)]
S′ \ ZS′)(Q), the set

(5.14) Σ∗
s := {
x ∈ X ◦
s (Q) : ˆhL(x) ≤ c
∗′′
3 }

must be contained in ΣS′,s for some S′. So Σ∗
s is contained in X ′(Q) for a proper
Zariski closed X ′ ⊊ Xs with degLs(X ′) < c∗′′
2 . This concludes the induction step
in this case. □

5.2. Proof of Proposition 5.1. Proposition 5.1 can be deduced from Proposi-
tion 5.2 by an almost verbal copy of the proof of Proposition 4.4 and the argument
in §4.3. Even more, the arguments needed here are simpler because we no longer

THE UNIFORM MORDELL–LANG CONJECTURE 35

need to deal with the Faltings height hFal(A). Instead of repeating the proof, we
hereby give a brief summary and leave it to the reader to supplement details from
the previous sections.
Let (A, L) be a polarized abelian variety defined over Q with degL A = l.
Let X be an irreducible subvariety of A with dim X = r and degL X = d such
that X generates A. We may assume r ≥ 1; otherwise the proposition is trivial.
We start with the case where (A, L) is principally polarized, i.e. l = g!.
Recall the universal abelian variety Ag → Ag and the symmetric relatively
ample line bundle Lg on Ag/Ag from the beginning of §5.1. The pair (A, L) gives
rise to a point b ∈ Ag(Q) such that (Ag)b ∼= A and c1(Lg|A) = 2c1(L) = c1(L⊗L−)
for L− = [−1]∗L. By (4.10), degL⊗4
g |A X = 8rd. For the line bundle L = ι∗L⊗4
g ,

we have seen in (4.12) that ˆhL|A = 4ˆhL⊗L− as height functions on A(Q).
Consider the restricted Hilbert scheme H◦ := H
◦
r,8rd(Ag/Ag) from (3.6) and
retain the commutative diagram (5.2)

XH◦ ˜   //
 ""
AH◦

π

 ι // Ag

πuniv

H◦ ιH◦ // Ag

where π|XH◦ : XH◦ → H
◦ is the universal family. All varieties and morphisms in
this diagram are defined over Q. The pair (X, (A, L)) is parametrized by a point
s ∈ H
◦(Q), which means that X = Xs, A = As = (Ag)b, and ιH◦(s) = b.
Let H
◦
gen be the subset of H◦ as defined by (3.9). If the stabilizer StabA(X))
of X in A has positive dimension, then X ◦ = ∅ by definition of the Ueno locus and
the proposition trivially holds true. Thus we may and do assume that StabA(X)
is finite. Then the point s ∈ H
◦(Q) which parametrizes (X, (A, L)) is in H◦
gen
We apply Proposition 5.2 to S = H◦, and hence obtain constants c
′′
2 and c
′′
3
that depend only on r, 8
rd and H
◦ (so only on g, d and r) such that the set

Σ := {
x ∈ X ◦
s (Q) : ˆhL|A(x) ≤ c
′′
3} = {
x ∈ X ◦(Q) : ˆhL⊗L−(x) ≤ c′′
3/4
}

is contained in some proper Zariski closed X ′ ⊊ X with degL|A(X ′) ≤ c′′
2. Thus
Proposition 5.1 for this case holds true because degL X ′ < degL|A(X ′) (since
c1(L|A) = 4c1(Lg|A) = 8c1(L)).
Now let us turn to arbitrary polarized abelian varieties (A, L). By Lemma 2.2.(iv),
there exist a principally polarized abelian variety (A0, L0) defined over Q and an
isogeny u : A0 → A such that u
∗L = [l/g!]
∗L0; see below (4.13). In particular,
u∗(L ⊗ L−) ∼= (L0 ⊗ (L0)−)⊗(l/g!)2, where (L0) = [−1]∗L0.

36 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

Let X0 be an irreducible component of u
−1(X). Then degu∗L X0 ≤ d(l/g!)
2g−1

by (4.14), and X0 is not contained in any proper subgroup of A0. Thus we can
apply the conclusion for the principally polarized case to X0 ⊆ A0 and get two
constants c′′
2 and c′′
3 depending only on g, r, l and d.[3]

By definition of the Ueno locus, we have X ◦ = u(X0)
◦ ⊆ u(X ◦
0 ). So we
have Σ ⊆ u(Σ0) for
 Σ := {
x ∈ X ◦(Q) : ˆhL⊗L−(x) ≤ c
′′
3}

and
 Σ0 = {
x0 ∈ X ◦
0 (Q) : ˆhL0⊗(L0)−(x0) ≤ (l/g!)2c′′
3} .

The conclusion follows from the principally polarized case upon replacing c′′
3 by
(l/g!)
2c′′
3. □

6. Proof of the gap principle (Theorem 1.2)

In this section we combine Proposition 4.1 and Proposition 5.1 to finish
the proof of the generalized New Gap Principle (Theorem 1.2) with the same
argument for curves [Gao21, Prop. 9.2]; this argument is eventually related to
[DGH22, Prop. 2.3].

Proposition 6.1. Let g, l, r, and d be positive integers. There exist constants
c1 = c1(g, l, r, d) > 0 and c2 = c2(g, l, r, d) > 0 with the following property. For
• each polarized abelian variety (A, L) of dimension g defined over Q with
degL A = l,
• and each irreducible subvariety X of A with dim X = r and degL X = d,
such that X generates A,
the set

(6.1) {
P ∈ X ◦(Q) : ˆhL⊗[−1]∗L(P ) ≤ c1 max{1, hFal(A)}}

is contained in X ′(Q) for a proper Zariski closed X ′ ⊊ X with degL X ′ < c2.

Proof. Let (A, L) and X be as in the proposition. Denote for simplicity by L− :=
[−1]
∗L.
By Proposition 4.1, there exist constants c′
1 = c
′
1(g, l, r, d) > 0 ,c′
2 =
c′
2(g, l, r, d) > 0 and c
′
3 = c
′
3(g, l, r, d) > 0 such that

(6.2) {
P ∈ X ◦(Q) : ˆhL⊗L−(P ) ≤ c
′
1 max{1, hFal(A)} − c′
3}

[3]Again, we first of all get constants c′′
0,2(g, r, d′) > 0 and c′′
0,3(g, r, d′) > 0 for each 1 ≤ d′ ≤ d, and then set
c′′
2 := max1≤d′≤d(l/g!)2g−1 {c′′
0,2(g, r, d′)} and c′′
3 := min1≤d′≤d(l/g!)2g−1 {c′′
0,3(g, r, d′)}.

THE UNIFORM MORDELL–LANG CONJECTURE 37

is contained in a proper Zariski closed X ′ ⊆ X with degL X ′ < c
′
2.
By Proposition 5.1, there exist constants c′′
2 = c
′′
2(g, l, r, d) > 0 and c′′
3 =
c′′
3(g, l, r, d) > 0 such that

(6.3) {
P ∈ X ◦(Q) : ˆhL⊗L−(P ) ≤ c′′
3}

is contained in a proper Zariski closed X ′ ⊆ X with degL X ′ < c
′′
2.
Now set

(6.4) c1 := min { c′′
3
max{1, 2c
′
3/c
′
1} , c′
1
2
 } and c2 := max{c
′
2, c
′′
2}.

We will prove that these are the desired constants.
To prove this, it suffices to prove the following claim.
Claim: If P ∈ X ◦(Q) satisfies ˆhL⊗L−(P ) ≤ c1 max{1, hFal(A)}, then P is in
either the set (6.2) or the set (6.3).
Let us prove this claim. Suppose P ∈ X ◦(Q) is not in (6.2) or (6.3), i.e.,
ˆhL⊗L−(P ) > c′
1 max{1, hFal(A)} − c′
3 and ˆhL⊗L−(P ) > c′′
3. We wish to prove
ˆhL⊗L−(P ) > c1 max{1, hFal(A)}.
We split up to two cases on whether or not max{1, hFal(A)} ≤ max{1, 2c
′
3/c
′
1}.
In the first case, i.e., max{1, hFal(A)} ≤ max{1, 2c′
3/c
′
1}, we have

ˆhL⊗L−(P ) > c′′
3 ≥ c
′′
3 max{1, hFal(A)}
max{1, 2c
′
3/c
′
1} = c′′
3
max{1, 2c
′
3/c
′
1} max{1, hFal(A)} ≥ c1 max{1, hFal(A)}.

In the second case, i.e., max{1, hFal(A)} > max{1, 2c′
3/c
′
1}, we have c
′
1 max{1, hFal(A)}−
c′
3 ≥ (c
′
1/2) max{1, hFal(A)} and hence

ˆhL⊗L−(P ) > c′
1
2 max{1, hFal(A)} ≥ c1 max{1, hFal(A)}.

Hence we are done. □

Proof of Theorem 1.2. Let A be an abelian variety of dimension g, let L be an
ample line bundle, and let X be an irreducible subvariety which generates A.
Assume all these objects are defined over Q. Then (A, L) is a polarized abelian
variety.
Write d = degL X, r = dim X, l = degL A. Then l ≤ c(g, d) by Lemma 2.5.
Since X generates A, we have that r ≥ 1. Thus we can apply Proposi-
tion 6.1 to (A, L) and X. Then we obtain constants c1 = c1(g, l, r, d) > 0 and
c2 = c2(g, l, r, d) > 0 such that the set

Σ := {
P ∈ X ◦(Q) : ˆhL⊗[−1]∗L(P ) ≤ c1 max{1, hFal(A)}
}

38 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

is contained in a proper Zariski closed X ′ ⊊ X with degL X ′ < c2.
Now we can conclude by replacing c1 by min1≤r≤g,1≤l≤c(g,d){c1(g, l, r, d)} > 0
and replacing c2 by max1≤r≤g,1≤l≤c(g,d){c2(g, l, r, d)} > 0. □

7. Proof of the uniform Mordell–Lang conjecture (Theorem 1.1)

7.1. A theorem of R´emond. In this subsection, we work over Q.
We start by recalling the following result, which is a consequence of R´emond’s
generalized Vojta’s Inequality [R´em00b, Thm. 1.2] for points in X ◦(Q), the gen-
eralized Mumford’s Inequality [R´em00a, Thm. 3.2] for points in X ◦(Q) ∩ Γ, and
the technique to remove the height of the subvariety [R´em00a, §3.b)].

Let A be an abelian variety of dimension g, and L be a symmetric ample
line bundle on A.
Let X be an irreducible subvariety of A, and Γ be a finite rank subgroup of
A(Q). We say that the assumption (Hyp pack) holds true for (A, L), X and Γ,
if there exists a constant c0 = c0(g, degL X) > 0 satisfying the following property:
for each P0 ∈ X(Q),
(7.1)
# {
P − P0 ∈ (X ◦(Q) − P0) ∩ Γ : ˆhL(P − P0) ≤ c
−1
0 max{1, hFal(A)}} ≤ c
rkΓ+1
0 .

Theorem 7.1 (R´emond). Assume that (Hyp pack) holds true for all (A, L), X,
Γ (as above) such that X generates A.
Then for each polarized abelian variety (A, L) with L symmetric, each ir-
reducible subvariety X of A and each finite rank subgroup Γ of A(Q), we have

(7.2) #X ◦(Q) ∩ Γ ≤ c(g, degL X, degL A)rkΓ+1.

A more detailed proof of this theorem can be found in Appendix A. We
hereby give a brief explanation by taking David–Philippon’s formulation of R´emond’s
result.

Proof. We start with a d´evissage. More precisely, we reduce to the case where
X generates A. Indeed, let A
′ be the abelian subvariety of A generated by
X − X. Then X ⊆ A
′ + Q for some Q ∈ A(Q). The subgroup Γ′ of A(Q)
generated by Γ and Q has rank ≤ rkΓ + 1. We have (X − Q)◦ = X ◦ − Q by
definition of the Ueno locus, (X ◦(Q) − Q) ∩ Γ ⊆ (X ◦(Q) − Q) ∩ Γ
′ = X ◦(Q) ∩ Γ′

and degL(X − Q) = degL X. By Lemma 2.5, we have degL A
′ ≤ c′(g, degL X).
Therefore if (7.2) holds true for X − Q ⊆ A
′, L|A′ and Γ
′ ∩ A
′(Q), then #X ◦(Q) ∩
Γ ≤ c(g, degL X)
rkΓ′+1 ≤ c(g, degL X)
rkΓ+2. So we can conclude by replacing c
with c2. Thus we are reduced to the case where X generates A.

THE UNIFORM MORDELL–LANG CONJECTURE 39

From now on, assume X generates A. We take the formulation of David–
Philippon [DP07, Thm. 6.8] of R´emond’s result [R´em00a].
It follows from Tate’s construction that there exists a constant cNT(A) ≥ 0,
which depends on A, such that |ˆhL(P ) − h(P )| ≤ cNT(A) for all P ∈ A(Q).
Let h1(A) denote the Weil height of the polynomials defining the addition
and the substraction on A.
It is known that cNT(A), h1(A) ≤ c
′ max{1, hFal(A)} for some c
′ = c
′(g, degL A) >
0; see [DP07, equation (6.41)]. Alternatively this can be deduced from [DGH21,
(8.4) and (8.7)].
Let η ≥ 1 be a real number. Then

(7.3) # {
P ∈ X ◦(Q) ∩ Γ : ˆhL(P ) ≤ η max{1, cNT(A), h1(A)}}

≤ # {
P ∈ X ◦(Q) ∩ Γ : ˆhL(P ) ≤ ηc′ max{1, hFal(A)}} .

Since X generates A, we can apply (7.1) to X − P0 for each P0 ∈ X(Q).
Set R = (ηc
′ max{1, hFal(A)})
1/2 and r = (c
−1
0 max{1, hFal(A)})
1/2 with c0
from (7.1).
Consider the real vector space Γ ⊗Q R endowed with the Euclidean norm
|·| = ˆh
1/2
L . By an elementary ball packing argument, any subset of Γ⊗R contained
in a closed ball of radius R centered at 0 is covered by at most (1 + 2R/r)rkΓ

closed balls of radius r centered at the elements P − P0 of the given subset (7.1);
see [R´em00a, Lem. 6.1]. Thus the number of balls in the covering is at most
(1 + 2
√
ηc′c0)
rkΓ. But each closed ball of radius r centered at some P − P0 in
(7.1) contains at most c elements by (7.1). So

(7.4) # {
P ∈ X ◦(Q) ∩ Γ : ˆhL(P ) ≤ ηc′ max{1, hFal(A)}} ≤ c0(1 + 2√ηc′c0)rkΓ.

So (7.3) and (7.4) yield, for each real number η ≥ 1,
(7.5)
# {
P ∈ X ◦(Q) ∩ Γ : ˆhL(P ) ≤ η max{1, cNT(A), h1(A)}} ≤ c0(1 + 2√
ηc′c0)rkΓ.

Thus [DP07, Thm. 6.8] implies

(7.6) #X ◦(Q) ∩ Γ ≤ (c
′′)
rkΓ+1 · c0(1 + 2√c′′c′c0)
rkΓ

for some c′′ = c′′(g, degL X) > 0. Therefore (7.2) holds true by letting c =
(c′′c0(1 + 2√c′′c′c0))
2. □

40 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

7.2. Proof of Theorem 1.1′ over Q. Now we are ready to prove Theorem 1.1′

over Q. In view of R´emond’s result (Theorem 7.1) cited above, the most impor-
tant ingredient is the following proposition.

Proposition 7.2. Let A be an abelian variety of dimension g and L be an ample
line bundle on A. Then with L replaced by L ⊗ [−1]
∗L, (Hyp pack) holds true
for each irreducible subvariety X of A which generates A and each finite rank
subgroup Γ of A(Q).

Proof. Write d = degL X. Denote for simplicity by L− := [−1]
∗L.
We prove this result by induction on r := dim X.
The base step is r = 0, in which case trivially holds true.
For an arbitrary r ≥ 1. Assume the theorem is proved for 0, 1, . . . , r − 1.
We wish to prove (7.1) with L replaced by L ⊗ L−. Let P0 ∈ X(Q).
Then degL(X − P0) = degL X = d. Moreover, (X − P0)
◦(Q) = X ◦(Q) − P0
by definition of the Ueno locus. Notice that X − P0 still generates A because
(X − P0) − (X − P0) = X − X.
Apply Theorem 1.2 to X−P0. Then we have constants c1 = c1(g, d) > 0 and
c2 = c2(g, d) > 0 such that for {
P − P0 ∈ X ◦(Q) − P0 : ˆhL⊗L−(P − P0) ≤ c1 max{1, hFal(A)}}

is contained in a proper Zariski closed X ′ ⊊ X − P0 with degL X ′ < c2. In par-
ticular, the number of irreducible components of X ′ is < c2.
Let X † be an irreducible component of X ′. Then dim X † ≤ dim X − 1 ≤
r − 1. Let A† be the abelian subvariety of A generated by X † − X †. Then
X † ⊆ A
† + Q for some Q ∈ A(Q). Now dim(X † − Q) = dim X † ≤ r − 1.
Let Γ
† be the subgroup of A(Q) generated by Γ and Q. Then rkΓ† ≤ rkΓ+1.
Apply the induction hypothesis to A†, L|A†, the irreducible subvariety X † − Q
and Γ† ∩ A†(Q). Then we have

(7.7) #(X † − Q)◦(Q) ∩ Γ† ≤ (c
†)
rkΓ†+1 ≤ (c
†)
rkΓ+2

for some c† = c†(dim A
†, degL(X † − Q)) > 0. But dim A† ≤ dim A = g and
degL(X † − Q) = degL X † ≤ degL X ′ < c2 = c2(g, d).
But (X † − Q)
◦(Q) = (X †)◦(Q) − Q by definition of the Ueno locus, and
Q ∈ Γ
†. So (7.7) yields

(7.8) #(X †)
◦(Q) ∩ Γ† ≤ (c
†)
rkΓ+2

Now that (X ′)◦(Q) ∩ Γ ⊆ ⋃
X †(X †)
◦(Q) ∩ Γ† with X † running over all
irreducible components of X ′ and Γ† constructed accordingly, (7.8) implies

(7.9) #(X ′)
◦(Q) ∩ Γ ≤ c2 max
X † {c†}rkΓ+2 ≤ c
rkΓ+1
3

THE UNIFORM MORDELL–LANG CONJECTURE 41

where c3 = (maxX †{c2, c
†})
3 > 0 depends only on g and d.
But {
P − P0 ∈ X ◦(Q) − P0 : ˆhL⊗L−(P − P0) ≤ c1 max{1, hFal(A)}
} ⊆ X ′(Q)
by construction of X ′. Moreover, (X ′)
◦ ⊇ X ◦ ∩X ′ by definition of the Ueno locus.
So (7.9) yields
(7.10){
P ∈ (X ◦(Q) − P0) ∩ Γ : ˆhL⊗L−(P − P0) ≤ c−1
0 max{1, hFal(A)}
} ≤ c
rkΓ+1
0

with c0 = max{c1, c3} > 0 which depends only on g and d. Hence we are done. □

Proof of Theorem 1.1′ with F = Q. Let A be an abelian variety of dimension g
and L be an ample line bundle on A. Let X be a closed irreducible subvariety of
A. Assume that all varieties are defined over Q. Set l = degL A and d = degL X.
Let Γ be a subgroup of A(Q) of finite rank.
Notice that degL⊗[−1]∗L X = 2dim X degL X ≤ 2gd and degL⊗[−1]∗L A =
2
g degL A = 2
gl.
Let X ◦ be the complement of the Ueno locus of X.
As before, we start by reducing to the case where X generates A. Indeed,
let A′ be the abelian subvariety of A generated by X − X. Then X ⊆ A
′ + Q
for some Q ∈ A(Q). The subgroup Γ
′ of A(Q) generated by Γ and Q has rank
≤ rkΓ + 1. We have (X − Q)
◦ = X ◦ − Q by definition of the Ueno locus,
(X ◦(Q) − Q) ∩ Γ ⊆ (X ◦(Q) − Q) ∩ Γ
′ = X ◦(Q) ∩ Γ
′ and degL(X − Q) = degL X.
If (1.2) holds true for X − Q ⊆ A
′, L|A′ and Γ
′ ∩ A′(Q), then #X ◦(Q) ∩ Γ ≤
c(g, d)
rkΓ′+1 ≤ c(g, d)
rkΓ+2. So we can conclude by replacing c with c
2. Thus we
are reduced to the case where X generates A. In particular, we have l ≤ c
′(g, d)
by Lemma 2.5.

By Proposition 7.2 and Theorem 7.1, we have #X ◦(Q) ∩ Γ ≤ c(g, l, d)
rkΓ+1.
Thus (1.2) holds true because l ≤ c′(g, d). Hence we are done. □

7.3. From Q to arbitrary F of characteristic 0. The following lemma of
specialization allows us to pass from Q to F .

Lemma 7.3. Assume Theorem 1.1
′ holds true for F = Q. Then Theorem 1.1
′

holds true, under the extra assumptions that Γ is finitely generated, for arbitrary
F of characteristic 0 with F = F .

Proof. Assume Theorem 1.1′ holds true for F = Q. Then we obtain a function
c : N2 → N such that Theorem 1.1
′ holds true with this function c viewed as a
constant depending only on g and the degree of the subvariety in question.
Now let F be an arbitrary algebraic closed field of characteristic 0. Let A,
L, X and Γ be as in Theorem 1.1′ with Γ finitely generated. Write ρ = rkΓ. Let
γ1, . . . , γr ∈ A(F ) be generators of Γ with γρ+1, . . . , γr torsion.

42 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

There exists a field K, finitely generated over Q, such that A, all elements
of End(A),[4] X, and γ1, . . . , γr are defined over K. Then K is the function field
of some regular, irreducible quasi-projective variety V defined over Q.
Up to replacing V by a Zariski open dense subset, we have
• A extends to an abelian scheme A → V of relative dimension g,
• L extends to a relatively ample line bundle L on A/V ,
• each element of End(A) extends to an element of End(A/V ) (this can be
achieved since End(A) is a finitely generated group); in particular, each
abelian subvariety B of A extends to an abelian subscheme B of A → V ,
• X extends to a flat family X → V (i.e., X is the generic fiber of X → V ),
• γ1, . . . , γr extend to sections of A → V ; we retain the symbols γ1, . . . , γr
for these sections. Use ΓV to denote the sub-V -group of A generated by
γ1, . . . , γr.
Moreover, up to replacing V by a Zariski open dense subset, we may choose X over
V to be a “Good model” as explained in [Maz00, p. 219–220] (which uses [Hin88,
App. 1, Lemma A]) such that the Ueno locus of Xv is the specialization of the
Ueno locus of X for each v ∈ V (Q). Hence X
◦
v is the specialization of X ◦.
As X → V is flat, we have degL X = degLv Xv for each v ∈ V (Q).
We define the specialization of Γ at v, which we denote with Γv, to be the
subgroup of Av(Q) generated by γ1(v), . . . , γr(v). There exists then a specializa-
tion homomorphism Γ → Γv for each v ∈ V (Q). Note that rkΓv ≤ ρ.
The extension of elements of End(A) to elements of End(A/V ) yields a
specialization End(A) → End(Av) for each v ∈ V (Q). Denote this map by
α ↦→ αv.
Set

Θ := {v ∈ V (Q) : Γ → Γv is injective and End(A) ∼= End(Av)}.

Masser [Mas89, Main Theorem and Scholium 1] and [Mas96, Main Theorem]
guarantee that Θ is Zariski dense in V .
Let v ∈ Θ. Then #X ◦(F ) ∩ Γ ≤ #X◦
v(Q) ∩ Γv. By the result over Q,
we have #X
◦
v(Q) ∩ Γv ≤ c(g, degLv Xv)
1+rkΓv ≤ c(g, degL X)
1+ρ. Hence we are
done. □

Now we are ready to finish the proof of Theorem 1.1
′.

Proof of Theorem 1.1′ for arbitrary F . Let F be an arbitrary algebraic closed
field of characteristic 0. Let A, L and X be as in Theorem 1.1′. Let Γ be a
subgroup of A(F ) of finite rank ρ.

[4]We can do this because End(A) is a finitely generated group.

THE UNIFORM MORDELL–LANG CONJECTURE 43

By the definition of a finite rank group, there exists a finitely generated
subgroup Γ0 of A(F ) with rank ρ such that

Γ ⊆ {x ∈ A(F ) : [N ]x ∈ Γ0 for some N ∈ N}.

Moreover, we may choose such a Γ0 satisfying that Γ0 = End(A) · Γ0.
For each n ∈ N, define

1
nΓ0 := {x ∈ A(F ) : [n]x ∈ Γ0}.

Then 1
n Γ0 is again a finitely generated subgroup of A(F ) of rank ρ, and is invariant
under End(A).
We have proved Theorem 1.1
′ over Q in §7.2. Thus Theorem 1.1′ holds
true for 1
n Γ0 and our F by the specialization result above (Lemma 7.3). So there
exists a constant c = c(g, degL X) > 0 such that

(7.11) #X ◦(F ) ∩ 1
nΓ0 ≤ c
1+ρ.

Note that { 1
n Γ0}n∈N is a filtered system and Γ ⊆ ⋃
n∈N 1
n Γ0. But the bound
(7.11) is independent of n. So
#X ◦(F ) ∩ Γ ≤ c
1+ρ.

This is precisely Theorem 1.1′. Hence we are done. □

7.4. From Theorem 1.1
′ to Theorem 1.1. Now that we have proved Theo-
rem 1.1′, we can conclude for Theorem 1.1 with the following lemma.

Lemma 7.4. Assume Theorem 1.1
′ holds true for all (A, L), X, and Γ. Then
Theorem 1.1 also holds true.

Proof. Using the same argument as in the proof of Theorem 1.1
′ with F = Q at
the end of §7.2, we may and do assume that X generates A.
We start with the following finer description of the Ueno locus of X. Let
Σ(X; A) be the set of abelian subvarieties B ⊆ A with dim B > 0 satisfying:
x + B ⊆ X for some x ∈ A(F ), and B is maximal for this property. Then for
each B ∈ Σ(X; A), there exists a closed subvariety XB of X such that the Ueno
locus of X is ⋃
B∈Σ(X;A)(XB + B).
The union above can be expressed in a quantitative way. First, by Bogo-
molov [Bog81, Thm. 1], each B ∈ Σ(X; A) satisfies degL B ≤ c3 for some con-
stant c3 = c3(dim A, degL X) > 0, and hence #Σ(X; A) ≤ c4 = c4(dim A, degL X)
by [R´em00a, Prop. 4.1]; here we used Lemma 2.5. Next, XB can be constructed as

44 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

follows. Let B⊥ be a complement of B, i.e. B ∩B⊥ is finite and B +B⊥ = A. It is
possible to choose such a B⊥ with degL B⊥ ≤ c
′
5(g, degL A, degL B); see [MW93].
Then we can choose XB := ⋂
b∈B(F )(X − b) ⋂ B⊥. Notice that by dimension
reasons, this intersection must be the component of a finite intersection of at
most dim X ≤ dim A members. So degL XB ≤ c5(dim A, degL X) by B´ezout’s
Theorem and Lemma 2.5. In particular XB has ≤ c5 irreducible components
XB,1, . . . , XB,mB .
As the Bi’s in (1.1) satisfies xi + Bi ⊆ X and dim Bi > 0, we may and do
assume Bi ∈ Σ(X; A) by definition of the Ueno locus. Now (1.1) becomes

(7.12) X(F ) ∩ Γ = ⋃

B∈Σ(X;A)
 nB⋃

j=1
(xB,j + B)(F ) ∩ Γ ∐ X ◦(F ) ∩ Γ.

Moreover, each xB,j can be chosen to be in X ◦
B(F ) ∩ Γ, where X ◦
B = ⋃mB
k=1 X ◦
B,k.
See [R´em00a, Lem. 4.6]; notice that p|XB is finite for the quotient p : A → A/B.
In particular, nB ≤ #X ◦
B(F ) ∩ Γ.
Let us bound nB for each B ∈ Σ(X; A). Applying Theorem 1.1
′ to each
irreducible component XB,k of XB, we get #X ◦
B,k(F ) ∩ Γ ≤ c1+rkΓ for some
c = c(dim A, degL XB,k) > 0. But we have seen that XB has ≤ c5 components
and that degL XB,k ≤ degL XB ≤ c5. So #X ◦
B(F ) ∩ Γ, and hence nB, is ≤
c6(dim A, degL X)
1+rkΓ.
From the bounds on Σ(X; A) and nB above, we get from (7.12) that N ≤
c4c1+rkΓ
6 + #X ◦(F ) ∩ Γ. Hence Theorem 1.1 holds true by applying Theorem 1.1′

again to X ◦(F ) ∩ Γ. □

8. Proof of the uniform Bogomolov conjecture (Theorem 1.3)

Proof of Theorem 1.3. Let A be an abelian variety of dimension g, let L be an
ample line bundle, and let X be an irreducible subvariety. Assume all these
objects are defined over Q.
Write d = degL X and r = dim X. Let c = c(g) be the constant from
Lemma 2.5. Let c′′′
2 = c′′
2(g, cd2g, r, d) > 0 and c
′′′
3 = c′′
3(g, cd2g, r, d) > 0 be
from Proposition 5.1. Moreover, set c3 := min1≤r≤g{c
′′
3(g, cd
2g, r, d)} > 0 and
c2 := max1≤r≤g{c′′
2(g, cd2g, r, d)} > 0; both c3 and c2 depend only on g and d.
We prove the theorem by induction on r. The base step r = 0 trivially
holds true.
For arbitrary r, assume the theorem is proved for 0, . . . , r − 1.
Let A
′ be the abelian subvariety of A generated by X − X, then degL A′ ≤
cd2g by Lemma 2.5. We can apply Proposition 5.1 to X and (A
′, L|A′) to conclude

THE UNIFORM MORDELL–LANG CONJECTURE 45

that the set

(8.1) Σ := {
P ∈ X ◦(Q) : ˆhL⊗L−(P ) ≤ c3} ,

where L− = [−1]
∗L, is contained in X ′(Q), for some proper Zariski closed X ′ ⊊ X
with degL(X ′) < c2. Each irreducible component of X ′ has dimension ≤ r−1, and
X ′ has ≤ c2 irreducible components. Hence the conclusion follows by applying
the induction hypothesis to each irreducible component of X ′ and appropriately
adjusting c3 and c2. □

Appendix A. R´emond’s theorem revisited

The goal of this appendix is to give a more detailed proof of R´emond’s
theorem, which we cited as Theorem 7.1, to make the current paper more com-
plete. We will explain how R´emond’s generalized Vojta’s Inequality, generalized
Mumford’s Inequality, and the technique to remove the height of the subvariety
together imply the desired Theorem 7.1. The proof follows closely the arguments
presented in [R´em00a].
We work over Q.
Let A be an abelian variety and let L be a symmetric ample line bundle
on A. To ease notation, we may and do assume L is very ample and gives a
projectively normal closed immersion into some projective space, by replacing L
by L⊗4.
Let us restate Theorem 7.1.
Let X be an irreducible subvariety of A, and Γ be a finite rank subgroup of
A(Q). We say that the assumption (Hyp pack) holds true for (A, L), X and Γ,
if there exists a constant c0 = c0(g, degL X) > 0 satisfying the following property:
for each P0 ∈ X(Q),

(7.1) {
P ∈ (X ◦(Q) − P0) ∩ Γ : ˆhL(P − P0) ≤ c
−1
0 max{1, hFal(A)}} ≤ c
rkΓ+1
0 .

Theorem 7.1. Assume that (Hyp pack) holds true for all (A, L), X, Γ (as
above) such that X generates A.
Then for each polarized abelian variety (A, L) with L symmetric and very
ample, each irreducible subvariety X of A and each finite rank subgroup Γ of
A(Q), we have

(7.2) #X ◦(Q) ∩ Γ ≤ c(g, degL X, degL A)rkΓ+1.

Moreover, we may and do assume that the function c is increasing in all
three invariables, by replacing c(g, d, l) by maxg′≤g,d′≤d,l′≤l c(g′, d
′, l′).

46 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

In what follows, we will introduce many constants c4, c5, . . .. All these
constants are assumed to depend only on g, degL X, and degL A unless stated
otherwise.

A.1. Preliminary setup. We have H 0(A, L) = degL A/g! by Lemma 2.2. Thus
A can be embedded into the projective space PdegL A/g!−1 using global sections of
H 0(A, L). Thus the integer n in [R´em00b,R´em00a] can be taken to be degL A/g!−
1. The closed immersion A ⊆ P
degL A/g!−1 defines a height function h : A(Q) →
R. The Tate Limit Process then gives rise to a height function

ˆhL : A(Q) → [0, ∞), P ↦→ lim
N →∞ h([N 2]P )
N 4 .

For P, Q ∈ A(Q) we set ⟨P, Q⟩ = (ˆhL(P + Q) − ˆhL(P ) − ˆhL(Q))/2 and
often abbreviate |P | = ˆhL(P )1/2. The notation |P | is justified by the fact that it
induces a norm after tensoring with the reals.
Let cNT(A) and h1(A) be as from [DP07, Thm. 6.8]. It is known that

(A.1) cNT(A), h1(A) ≤ c
′ max{1, hFal(A)}

for some c
′ = c
′(g, degL A) > 0; see [DP07, equation (6.41)].
Finally for any irreducible subvariety X of the projective space P
degL A/g!−1,
one can define the height h(X); see [BGS94].

A.2. Generalized Vojta’s Inequality.

Theorem A.1 ([R´em00b, Thm. 1.1]). There exist constants c4 = c4(g, degL X, degL A) >
0 and c5 = c5(g, degL X, degL A) > 0 with the following property. If P0, . . . , Pdim X ∈
X ◦(Q) satisfy

⟨Pi, Pi+1⟩ ≥ (1 − 1
c4
 ) |Pi||Pi+1| and |Pi+1| ≥ c4|Pi|,

then
 |P0|
2 ≤ c5 max{1, h(X), hFal(A)}.

Proof. This follows immediately from [R´em00b, Thm. 1.1] (with n = degL A/g! −
1) and (A.1) and dim X ≤ g. □

THE UNIFORM MORDELL–LANG CONJECTURE 47

A.3. Generalized Mumford’s Inequality. Let Ddim X : X dim X+1 → A
dim X be
the morphism defined by (x0, x1, . . . , xdim X) ↦→ (x1 − x0, . . . , xdim X − x0).

Proposition A.2 ([R´em00a, Prop. 3.4]). There exist constants c4 = c4(g, degL X, degL A) >
0 and c5 = c5(g, degL X, degL A) > 0 with the following property. Let P0 ∈ X(Q).
Suppose P1, . . . , Pdim X ∈ X(Q) with (P0, P1, . . . , Pdim X) isolated in the fiber of
Ddim X : X dim X+1 → A
dim X. If

⟨P0, Pi⟩ ≥ (1 − 1
c4
 ) |P0||Pi| and ∣
∣|P0| − |Pi|
∣
∣ ≤ 1
c4 |P0|

then
 |P0|
2 ≤ c5 max{1, h(X), hFal(A)}.

Proof. This follows immediately from [R´em00a, Prop. 3.4] (with n = degL A/g! −
1) and (A.1) and dim X ≤ g. □

Proposition A.3 ([R´em00a, Prop. 3.3]). Let Ξ ⊆ X ◦(Q). We are in one of the
following alternatives.

(i) Either for any x ∈ X(Q), there exist pairwise distinct x1, . . . , xdim X ∈ Ξ
such that (x, x1, . . . , xdim X) is isolated in the fiber of Ddim X : X dim X+1 →
A
dim X;
(ii) or Ξ is contained in a proper Zariski closed subset X ′ ⊊ X with deg X ′ <
(degL X)
2 dim X.

Proof. Denote by 0 the origin of the abelian variety A. We may and do assume
that the stabilizer of X in A, denoted by Stab(X) has dimension 0; otherwise
X ◦ = ∅ and the proposition trivially holds true.
The points in the fiber of Ddim X in question can be written as (x + a, x1 +
a, . . . , xr + a) with a running over the Q-points of (X − x) ∩ (X − x1) ∩ · · · ∩
(X − xdim X). Thus (x, x1, . . . , xdim X) is isolated in the fiber of the image of
X dim X+1 → A
dim X if and only if

(A.2) dim0(X − x) ∩ (X − x1) ∩ · · · (X − xdim X) = 0.

Assume we are not in case (i). Then there exists i0 ≤ dim X − 1 satisfying
the following property. There are pairwise distinct points x1, . . . , xi0 such that
for W := (X − x) ∩ (X − x1) ∩ · · · ∩ (X − xi0), we have

(A.3) dim0 W = dim0 W ∩ (X − y) = dim X − i0 for all y ∈ Ξ.

48 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

Let C1, . . . , Cs be the irreducible components of W passing through 0 with
dim Cj = dim X − i0 ≥ 1. Then s ≤ ∑s
j=1 deg Cj ≤ (deg X)i0+1 ≤ (deg X)
dim X

by B´ezout’s Theorem. Moreover,

dim0 W ∩ (X − y) = dim0 W = dim X − i0 ⇔ Cj ⊆ X − y for some j ∈ {1, . . . , s}

⇔ y ∈ ⋂

c∈Cj (Q)
(X − c) for some j ∈ {1, . . . , s}.

So (A.3) is equivalent to Ξ ⊆ ⋃s
j=1 ⋂
c∈Cj (Q)(X − c). Each ⋂

c∈Cj (Q)(X − c)
is a finite intersection of at most dim X members because of dimension rea-
sons. So deg ⋂

c∈Cj (Q)(X − c) ≤ (deg X)
dim X by B´ezout’s Theorem. Moreover,
each irreducible component of ⋂
c∈Cj (Q)(X − c) has dimension < dim X because
dim Stab(X) = 0. Hence we are in case (ii) by setting X ′ = ⋃s
j=1 ⋂

c∈Cj (X − c).
So we are done. □

A.4. Removing h(X).

Lemma A.4 ([R´em00a, Lem. 3.1]). Assume S ⊆ X(Q) a finite set. Assume that
each equidimensional subvariety Y ⊇ S of X of dimension dim X − 1 satisfies
degL Y > degL A(degL X)
2/g!. Then

h(X) ≤ (degL A/g! + 1)dim X+1 degL X (
max
x∈S h(x) + 3 log(degL A/g!)
) .

Proof. This is precisely [R´em00a, Lem. 3.1] with n = degL A/g! − 1. □

A.5. Proof of Theorem 7.1. Let X be an irreducible subvariety of A, and let
Γ be a subgroup of A(Q) of finite rank.
We start by reducing to the case where X generates A. Indeed, let A
′ be
the abelian subvariety of A generated by X − X. Then X ⊆ A
′ + Q for some
Q ∈ A(Q). The subgroup Γ
′ of A(Q) generated by Γ and Q has rank ≤ rkΓ + 1.
We have (X − Q)◦ = X ◦ − Q by definition of the Ueno locus, (X ◦(Q) − Q) ∩ Γ ⊆
(X ◦(Q)−Q)∩Γ′ = X ◦(Q)∩Γ′ and degL(X −Q) = degL X. By Lemma 2.5, (Hyp)
yields degL A
′ ≤ c
′(g, degL X). Therefore if (7.2) holds true for X − Q ⊆ A
′, L|A′
and Γ
′ ∩ A′(Q), then #X ◦(Q) ∩ Γ ≤ c(g, degL X)
rkΓ′+1 ≤ c(g, degL X)
rkΓ+2. So
we can conclude by replacing c with c2. Thus we are reduced to the case where
X generates A.
From now on, assume X generates A. We prove (7.2) by induction on

(A.4) r := dim X.

The base step is r = 0, in which case trivially holds true.

THE UNIFORM MORDELL–LANG CONJECTURE 49

For an arbitrary r ≥ 1. Assume (7.2) holds true for 0, 1, . . . , r − 1.
Observe that both Theorem A.1 and Proposition A.2 hold with c4 and c5
replaced by some larger value. We let c4 (resp. c5) denote the maximum of both
constants c4 (resp. c5) from these two theorems. Both constants depend only on
g, degL X and degL A.

Step 1: Handle large points by both inequalities of R´emond. The goal of this step
is to prove the following bound: there exists a constant c6 = c6(g, degL X, degL A) >
0 such that

(A.5) # {
P ∈ X ◦(Q) ∩ Γ : ˆhL(P ) ≥ c5 max{1, h(X), hFal(A)}} ≤ c
rkΓ+1
6 .

The proof follows a standard classical argument involving the inequalities
of Vojta and Mumford. Consider the rkΓ-dimensional real vector space Γ ⊗ R
endowed with the Euclidean norm |·| = ˆh
1/2
L . We may and do assume rkΓ ≥ 1. By
elementary geometry, the vector space can be covered by at most ⌊(1+(8c4)
1/2)
rkΓ⌋
cones on which ⟨P, Q⟩ ≥ (1 − 1/c4)|P ||Q| holds.
Let P0, P1, P2, . . . , PN ∈ X ◦(Q) ∩ Γ be pairwise distinct points in one such
cone such that

(A.6) c5 max{1, h(X), hFal(A)} < |P0|
2 ≤ |P1|
2 ≤ |P2|
2 ≤ · · · ≤ |PN |
2.

Notice that

(A.7) ⟨Pi, Pj⟩ ≥ (1 − 1
c4
 ) |Pi||Pj| for all i, j ∈ {0, . . . , N }.

Set N ′ := (degL X)
2gc(g, (degL X)
2g, degL A)
rkΓ+1 + 1, with c the constant
from (7.2).
Consider the subset Ξj = {Pj+1, . . . , Pj+N ′} with j ∈ {0, . . . , N − N ′}; it
has N ′ pairwise distinct elements. We claim that Ξ cannot be contained in a
proper Zariski closed subset X ′ ⊊ X with degL X ′ ≤ (degL X)
2 dim X. Indeed if
such an X ′ exists, then by definition of the Ueno locus we have (X ′)
◦ ⊇ X ◦ ∩ X ′.
So Ξ ⊆ (X ′)
◦(Q) ∩ Γ. As dim X ′ < dim X = r, we can apply the induction
hypothesis (7.2) to each irreducible component of X ′. As X ′ has ≤ (degL X)
2r

irreducible components and each component has degree ≤ (degL X)
2r, we then
get #Ξ ≤ (degL X)
2rc(g, (degL X)
2r, degL A)rkΓ+1. This contradicts our choice of
N ′ because c is increasing in all the three variables.
By Proposition A.3 applied to Ξj and Pj, we then get pairwise distinct
points Pi1, . . . , Pir ∈ Ξj such that (Pj, Pi1, . . . , Pir) is isolated in the fiber of
Dr : X r+1 → Ar. But the hypotheses of Proposition A.2 cannot hold true by

50 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

(A.6) and (A.7). So there exists k ∈ {i1, . . . , ir} such that |Pk| − |Pj| > 1
c4 |Pj|.
As k ≤ j + N ′, we then have
|Pj+N ′| > (1 + 1
c4 )|Pj|.

This holds true for each j ∈ {0, . . . , N − N ′}. So

(A.8) |Pj+N ′k| > (1 + 1
c4 )
k|Pj|

for all j ≥ 0 and k ≥ 1.
Next we choose an integer M ≥ 0 such that (1 + 1/c4)
M ≥ c4. We may and
do assume that M depends only on g, degL X and degL A (since c4 does). Then
by (A.8), |P(k+1)M N ′| > (1 + 1/c4)
M |PkM N ′| ≥ c4|PkM N ′| for each k ≥ 0.
We claim N < rM N ′ ≤ gM N ′. Indeed, assume N ≥ rM N ′. Then we
have r + 1 pairwise distinct points P0, PM N ′, P2M N ′, . . . , PrM N ′. The hypotheses
of Theorem A.1 for these points cannot hold true by (A.6) and (A.7). Thus there
exists k such that |P(k+1)M N ′| < c4|PkM N ′|. But this contradicts the conclusion
of last paragraph. So we much have N < rM N ′ ≤ gM N ′.
Recall that we have covered Γ ⊗ R by at most ⌊(1 + (8c4)1/2)rkΓ⌋ cones
and each cone contains < gM N ′ points P ∈ X ◦(Q) ∩ Γ with ˆhL(P ) = |P |2 ≥
c5 max{1, h(X), hFal(A)}. Thus

# {
P ∈ X ◦(Q) ∩ Γ : ˆhL(P ) ≥ c5 max{1, h(X), hFal(A)}
} ≤ (1 + (8c4)1/2)rkΓgM N ′

All constants on the right hand side depend only on g, degL X and degL A. So
(A.5) holds true by choosing c6 appropriately.

Step 2: Remove the dependence on h(X). More precisely, set

(A.9) c7 := degL A(degL X)2/g! · c(g, degL A(degL X)2/g!, degL A) and N ′′ := crkΓ+1
7 + 1.

The goal of this step is to prove: There exist positive constants c8, c9, c10, depend-
ing only on g, degL X, and degL A with the following property. If P0, . . . , PN ′′
are pairwise distinct points in X ◦(Q) ∩ Γ, then

(A.10) # {
P ∈ X ◦(Q) ∩ Γ : ˆhL(P − P0) ≥ c
2
8 max
1≤i≤N ′′ ˆhL(Pi − P0) + c9 max{1, hFal(A)}
} ≤ crkΓ+1
10 .

The proof follows closely [R´em00a, Prop. 3.6]. We wish to apply Lemma A.4 to
X − P0 and the set S = {Pi − P0 : 0 ≤ i ≤ N ′′}. Let us verify the hypothesis. Let
Y ⊆ X−P0 with Y equidimensional of dimension dim X−1 = r−1 and S ⊆ Y (Q),

THE UNIFORM MORDELL–LANG CONJECTURE 51

and set Y ′ := Y + P0. Then Pi ∈ (Y ′)
◦(Q) ∩ Γ.
[5] Each irreducible component
of Y ′ has dimension ≤ r − 1. Thus we can apply induction hypothesis (7.2) to
each irreducible component of Y ′. So N ′′ ≤ ∑

Y ′′ c(g, degL Y ′′, degL A)rkΓ+1, with
Y ′′ running over all irreducible components of Y ′. Since degL Y = degL Y ′ =∑

Y ′′ degL Y ′′ and c is increasing in all the three variables, this bound implies

N ′′ ≤ degL Y · c(g, degL Y, degL A)rkΓ+1.

We claim degL Y > degL A(degL X)
2/g!. Indeed, assume degL Y ≤ degL A(degL X)
2/g!.
Then N ′′ ≤ degL A(degL X)
2/g! · c(g, degL A(degL X)
2/g!, degL A)
rkΓ+1 because c
is increasing in all the three variables. This contradicts the definition of N ′′ from
(A.9).
Thus the assumption of Lemma A.4 is satisfied. So

h(X) ≤ c11(g, degL X, degL A) ( max
1≤i≤N ′′ ˆhL(Pi − P0) + max{1, hFal(A)}
) .

Here we also used (A.1). Thus by (A.5), we can find the desired constants c8, c9,
c10 such that (A.10) holds true.

Step 3: Prove the following alternative.

(i) Either #X ◦(Q) ∩ Γ ≤ N ′′(8c8 + 1)rkΓ + crkΓ+1
10 ;
(ii) or there exists Q ∈ X ◦(Q) ∩ Γ such that #{P ∈ X ◦(Q) ∩ Γ : ˆhL(P − Q) ≥
2c9 max{1, hFal(A)}} ≤ c
rkΓ+1
10 .

The proof follows closely [R´em00a, Prop. 3.7]. Assume we are not in case
(i), i.e. #X ◦(Q) ∩ Γ > N ′′(8c8 + 1)rkΓ + crkΓ+1
10 . Let c12 be the smallest real
number such that there exists Q ∈ X ◦(Q) ∩ Γ with

(A.11) #{P ∈ X ◦(Q) ∩ Γ : |P − Q| ≥ c12} ≤ c
rkΓ+1
10 .

Consider the set Ξ := {P ∈ X ◦(Q) ∩ Γ : |P − Q| ≤ c12} in the rkΓ-
dimensional Euclidean space (Γ ⊗ R, | · |). Then #Ξ ≥ #X ◦(Q) ∩ Γ − #{P ∈
X ◦(Q) ∩ Γ : |P − Q| ≥ c12} > N ′′(4c8 + 1)rkΓ. By an elementary ball packing
argument, Ξ (being a subset of Γ ⊗ R contained in a closed ball of radius c12
centered at Q) is covered by at most (8c8 + 1)
rkΓ balls of radius c12/4c8 centered
at points in X ◦(Q) ∩ Γ; see [R´em00a, Lem. 6.1]. By the Pigeonhole Principle,

[5]As Y ′ ⊆ X, we have (Y ′)◦ ⊇ X ◦ ∩ Y ′ by definition of the Ueno locus. So Pi ∈ (Y ′ ∩ X ◦)(Q) ∩ Γ ⊆
(Y ′)◦(Q) ∩ Γ.

52 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

one of the balls contains ≥ N ′′ + 1 points in X ◦(Q) ∩ Γ, say P0, P1, . . . , PN ′′. We
have |Pi − P0| ≤ c12/2c8 for each i. Thus (A.10) yields

# {
P ∈ X ◦(Q) ∩ Γ : ˆhL(P − P0) ≥ c2
12/4 + c9 max{1, hFal(A)}
} ≤ c
rkΓ+1
10 .

Therefore by the minimality of c12, we have c
2
12 ≤ c
2
12/4 + c9 max{1, hFal(A)}, and
hence c2
12 ≤ 2c9 max{1, hFal(A)}. So we are in case (ii) by (A.11).

Step 4: Conclude by the standard packing argument.
Recall our assumption that X generates A. The assumption of Theorem 7.1
says that (Hyp pack) holds true for X and Γ, i.e. we have (7.1).
Assume we are in case (i) from Step 3. Recall the definition of N ′′ = c
rkΓ+1
7 +
1 from (A.9). Then #X ◦(Q) ∩ Γ ≤ c
rkΓ+1 for c := 2 max{(c7 + 1)(8c8 + 1), c10}.
Hence we can conclude for this case.
Assume we are in case (ii) from Step 3. Set R = (2c9 max{1, hFal(A)})
1/2

and R0 = (c
−1
0 max{1, hFal(A)})
1/2. By an elementary ball packing argument, any
subset of Γ ⊗ R contained in a closed ball of radius R centered at Q is covered by
at most (1 + 2R/R0)
rkΓ closed balls of radius R0 centered at the elements P − P0
with P from the given subset (7.1); see [R´em00a, Lem. 6.1]. Thus the number of
balls in the covering is at most (1 + 2
√
2c9c0)
rkΓ. But each closed ball of radius
r centered at some P − P0 in (7.1) contains at most c elements by (7.1). So
(A.12)
# {
P ∈ X ◦(Q) ∩ Γ : ˆhL(P − Q) ≤ 2c9 max{1, hFal(A)}} ≤ c0(1 + 2√
2c9c0)
rkΓ.

Thus we have #X ◦(Q)∩Γ ≤ c0(1+2
√2c9c0)rkΓ +crkΓ+1
10 . So #X ◦(Q)∩Γ ≤ crkΓ+1

for c := 2 max{c0, 1 + 2
√2c9c0, c10}. Hence we can conclude are this case.
Therefore, it suffices to take c = 2 max{(c7+1)(8c8+1), c0, 1+2√2c9c0, c10},
which is a constant depending only on g, degL X and degL A. We are done.

References

[ACG11] E. Arbarello, M. Cornalba, and P. Griffiths. Geometry of Algebraic Curves, II (with a contribution by
J. Harris), volume 268 of Grundlehren der mathematischen Wissenschaften. Springer-Verlag, Berlin,
2011.
[AD06] F. Amoroso and S. David. Points de petite hauteur sur une sous-vari´et´e d’un tore. Compos. Math.,
142(3):551–562, 2006.
[BGS94] J.-B. Bost, H. Gillet, and C. Soul´e. Heights of projective varieties and positive Green forms. J. Amer.
Math. Soc., 7(2):903–1027, 1994.
[BL04] C. Birkenhake and H. Lange. Complex Abelian Varieties. Springer, 2004.
[Bog81] F. Bogomolov. Points of finite order on an abelian variety. Izv. Math., 17:55–72, 1981.
[BZ95] E. Bombieri and U. Zannier. Algebraic points on subvarieties of Gn
m. Internat. Math. Res. Notices,
(7):333–347, 1995.
[Cin11] Z. Cinkir. Zhang’s conjecture and the effective Bogomolov conjecture over function fields. Invent.
Math., 183:517–562, 2011.
[Deb05] O. Debarre. Complex Tori and Abelian Varieties, volume 11 of Collection SMF. AMS and SMF, 2005.

THE UNIFORM MORDELL–LANG CONJECTURE 53

[DGH19] V. Dimitrov, Z. Gao, and P. Habegger. Uniform bound for the number of rational points on a pencil
of curves. Int. Math. Res. Not. IMRN, (rnz248):https://doi.org/10.1093/imrn/rnz248, 2019.
[DGH21] V. Dimitrov, Z. Gao, and P. Habegger. Uniformity in Mordell–Lang for curves. Annals of Mathemat-
ics, 194(1):237–298, 2021.
[DGH22] V. Dimitrov, Z. Gao, and P. Habegger. A consequence of the relative Bogomolov conjecture. Journal
of Number Theory (Prime), Proceedings of the First JNT Biennial Conference 2019, 230:146–160,
2022.
[Dil22] G. Dill. Torsion points on isogenous abelian varieties. Compos. Math., 158(5):1020–1051, 2022.
[dJ18] R. de Jong. N´eron-tate heights of cycles on Jacobians. Journal of Algebraic Geometry, 27:339–381,
2018.
[DKY20] L. DeMarco, H. Krieger, and H. Ye. Uniform Manin-Mumford for a family of genus 2 curves. Ann. of
Math., 191:949–1001, 2020.
[DP99] S. David and P. Philippon. Minorations des hauteurs normalis´ees des sous-vari´et´es des tores. Ann.
Scuola Norm. Sup. Pisa Cl. Sci. (4), 28(3):489–543, 1999.
[DP07] S. David and P. Philippon. Minorations des hauteurs normalis´ees des sous-vari´et´es des puissances des
courbes elliptiques. Int. Math. Res. Pap. IMRP, (3):Art. ID rpm006, 113, 2007.
[Fal83] G. Faltings. Endlichkeitss¨atze f¨ur abelsche Variet¨aten ¨uber Zahlk¨orpern. Invent. Math., 73:349–366,
1983.
[Fal91] G. Faltings. Diophantine approximation on abelian varieties. Ann. of Math. (2), 133(3):549–576,
1991.
[Fal94] G. Faltings. The general case of S. Lang’s conjecture. In Barsotti Symposium in Algebraic Geometry
(Abano Terme, 1991), volume 15 of Perspect. Math., pages 175–182. Academic Press, San Diego,
CA, 1994.
[Ful98] W. Fulton. Intersection theory, volume 2 of Ergebnisse der Mathematik und ihrer Grenzgebiete. 3.
Folge. A Series of Modern Surveys in Mathematics [Results in Mathematics and Related Areas. 3rd
Series. A Series of Modern Surveys in Mathematics]. Springer-Verlag, Berlin, second edition, 1998.
[Gao20] Z. Gao. Generic rank of Betti map and unlikely intersections. Compos. Math., 156(12):2469–2509,
2020.
[Gao21] Z. Gao. Recent developments of the Uniform Mordell–Lang Conjecture. arXiv: 2104.03431, 2021.
[Gau26] T. Gauthier. Good height functions on quasi-projective varieties: equidistribution and applications
in dynamics. Annales de la facult´e des sciences de Toulouse Math´ematiques, 35(1):57–94, 2026.
[GTV26] T. Gauthier, J. Taflin, and G. Vigny. Sparsity of postcritically finite maps of Pk and beyond: A
complex analytic approach. Publications Math´ematiques de l’IH ´ES, online first, 1–96, 2026.
[Ge24] T. Ge. Uniformity of quadratic points. International Journal of Number Theory, 20(4):1041–1071,
2024.
[Gro62] A. Grothendieck. Techniques de construction et th´eor`emes d’existence en g´eom´etrie alg´ebrique IV : les
sch´emas de Hilbert. In Fondements de la g´eometrie alg´ebrique, S´eminaire Bourbaki n◦ 221, 1957–62.
Socr. Math. Paris, 1962.
[Gro67] A. Grothendieck. ´El´ements de g´eom´etrie alg´ebrique. IV. ´Etude locale des sch´emas et des morphismes
de sch´emas I-IV. Inst. Hautes ´Etudes Sci. Publ. Math., (20,24,28,32), 1964–1967.
[Hab13] P. Habegger. Special Points on Fibered Powers of Elliptic Surfaces. J.Reine Angew. Math., 685:143–
179, 2013.
[Hin88] M. Hindry. Autour d’une conjecture de Serge Lang. Invent. Math., 94(3):575–603, 1988.
[HS00] M. Hindry and J. Silverman. Diophantine geometry, volume 201 of Graduate Texts in Mathematics.
Springer-Verlag, New York, 2000. An introduction.
[Kaw80] Y. Kawamata. On Bloch’s Conjecture. Inv. math., 57:97–100, 1980.
[Kol99] J. Kollar. Rational Curves on Algebraic Varieties. Ergebnisse der Mathematik und ihrer Grenzgebiete.
3. Folge / A Series of Modern Surveys in Mathematics. Springer Berlin Heidelberg, 1999.
[K¨uh21] L. K¨uhne. Equidistribution in Families of Abelian Varieties and Uniformity. arXiv:2101.10272, 2021.
[Lan62] S. Lang. Diophantine geometry. Interscience Tracts in Pure and Applied Mathematics, No. 11. Inter-
science Publishers (a division of John Wiley & Sons, Inc.), New York-London, 1962.
[Mas89] D. Masser. Specializations of finitely generated subgroups of abelian varieties. Trans. Amer. Math.
Soc., 311(1):413–424, 1989.
[Mas96] D. Masser. Specialization of endomorphism rings of abelian varieties. Bulletin de la SMF, 124(3):457–
476, 1996.
[Maz86] B. Mazur. Arithmetic on curves. Bulletin of the American Mathematical Society, 14(2):207–259, 1986.
[Maz00] B. Mazur. Abelian varieties and the Mordell-Lang conjecture. In Model theory, algebra, and geometry,
volume 39 of Math. Sci. Res. Inst. Publ., pages 199–227. Cambridge Univ. Press, Cambridge, 2000.

54 ZIYANG GAO, TANGLI GE, LARS K ¨UHNE

[MB85] L. Moret-Bailly. Compactifications, hauteurs et finitude. In S´eminaire sur les pinceaux arithm´etiques
: la conjecture de Mordell (Paris, 1983/84). Ast´erisque, number 127, pages 113–129. 1985.
[MFK94] D. Mumford, J. Fogarty, and F. Kirwan. Geometric invariant theory, volume 34 of Ergebnisse der
Mathematik und ihrer Grenzgebiete (2) [Results in Mathematics and Related Areas (2)]. Springer-
Verlag, Berlin, third edition, 1994.
[Mum74] D. Mumford. Abelian Varieties, 2nd ed. Oxford University Press, London, 1974.
[MW93] D. Masser and G. W¨ustholz. Periods and minimal abelian subvarieties. Ann. Math., 137:407–458,
1993.
[Ray83] M. Raynaud. Sous-vari´et´es d’une vari´et´e ab´elienne et points de torsion. In Arithmetic and geometry,
Vol. I, volume 35 of Progr. Math., pages 327–352. Birkh¨auser Boston, Boston, MA, 1983.
[Ray85] M. Raynaud. Hauteurs et isog´enies. In S´eminaire sur les pinceaux arithm´etiques : la conjecture de
Mordell (Paris, 1983/84). Ast´erisque, number 127, pages 199–234. 1985.
[R´em00a] G. R´emond. D´ecompte dans une conjecture de Lang. Invent. Math., 142(3):513–545, 2000.
[R´em00b] G. R´emond. In´egalit´e de Vojta en dimension sup´erieure. Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4),
29(1):101–151, 2000.
[SUZ97] L. Szpiro, E. Ullmo, and S. Zhang. Equir´epartition des petits points. Inv. Math., 127:337–347, 1997.
[Ull98] E. Ullmo. Positivit´e et discr`etion des points alg´ebriques des courbes. Ann. of Math. (2), 147(1):167–
179, 1998.
[Voj91] P. Vojta. Siegel’s theorem in the compact case. Ann. of Math. (2), 133(3):509–548, 1991.
[Yua26] X. Yuan. Arithmetic bigness and a uniform Bogomolov-type result. Ann. of Math. (2), 203(1):15–119,
2026.
[YZ26] X. Yuan and S. Zhang. Adelic line bundles on quasi-projective varieties, Annals of Mathematical
Studies, Princeton University Press, 2026.
[Zha93] S. Zhang. Admissible pairing on a curve. Inv. Math., 112(1):171–193, 1993.
[Zha98] S. Zhang. Equidistribution of small points on abelian varieties. Ann. of Math. (2), 147(1):159–165,
1998.
[Zha10] S. Zhang. Gross–Schoen cycles and dualising sheaves. Inv. Math., 179(1):1–73, 2010.

Department of Mathematics, UCLA, Los Angeles, CA 90095, USA
Email address: ziyang.gao@math.ucla.edu

Department of Mathematics, Princeton University, Princeton, NJ 08544, USA
Email address: tangli@princeton.edu

School of Mathematics and Statistics, University College Dublin, Dublin 4, Ireland
Email address: lars.kuehne@ucd.ie
