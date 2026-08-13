<!-- source: https://arxiv.org/pdf/2103.01784 | converted from PDF -->

arXiv:2103.01784v3  [math.NT]  14 Apr 2021
NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR
SURFACES

HAN WU

Abstract. In this paper, we study the properties of weak approximation with Brauer-
Manin obstruction and the Hasse principle with Brauer-Manin obstruction for surfaces
with respect to ﬁeld extensions of number ﬁelds. We assume a conjecture of M. Stoll.
For any nontrivial extension of number ﬁelds L/K, we construct two kinds of smooth,
projective, and geometrically connected surfaces deﬁned over K. For the surface of the
ﬁrst kind, it has a K-rational point, and satisﬁes weak approximation with Brauer-
Manin obstruction oﬀ ∞K , while its base change by L does not so oﬀ ∞L. For the
surface of the second kind, it is a counterexample to the Hasse principle explained
by the Brauer-Manin obstruction, while the failure of the Hasse principle of its base
change by L cannot be so. We illustrate these constructions with explicit unconditional
examples.
 1. Introduction

1.1. Background. For a proper scheme X over a number ﬁeld K, if its K-rational points
set X(K) ̸= ∅, then its adelic points set X(AK) ̸= ∅. The converse, as has been known,
does not always hold. We say that X is a counterexample to the Hasse principle if the set
X(AK) ̸= ∅ whereas the set X(K) = ∅. Let S ⊂ ΩK be a ﬁnite subset. By the diagonal
embedding, we always view X(K) as a subset of X(AK) (respectively of X(AS
K)). We
say that X satisﬁes weak approximation (respectively weak approximation oﬀ S) if X(K) is
dense in X(AK) (respectively in X(AS
K)), cf. [Sko01, Chapter 5.1]. Manin [Man71] used
the Brauer group of X to deﬁne a closed subset X(AK)
Br ⊂ X(AK), and showed that this
closed subset can explain some failures of the Hasse principle and nondensity of X(K) in
X(AS
K). The global reciprocity law gives an inclusion: X(K) ⊂ X(AK)
Br. We say that the
failure of the Hasse principle of X is explained by the Brauer-Manin obstruction if the set
X(AK) ̸= ∅ and the set X(AK)
Br = ∅. We say that X satisﬁes weak approximation with
Brauer-Manin obstruction (respectively with Brauer-Manin obstruction oﬀ S) if X(K) is dense
in X(AK)
Br (respectively in prS(X(AK)
Br)). For a smooth, projective, and geometrically
connected curve C deﬁned over a number ﬁeld K, assume that the Tate-Shafarevich group
and the rational points set of its Jacobian are both ﬁnite. By the dual sequence of Cassels-
Tate, Skorobogatov [Sko01, Chapter 6.2] and Scharaschkin [Sch99] independently observed
that C(K) = pr∞K (C(AK )
Br). In particular, if this curve C is a counterexample to the
Hasse principle, then this failure can be explained by the Brauer-Manin obstruction. Stoll
[Sto07] generalized this observation, and made a conjecture that for any smooth, projective,
and geometrically connected curve, it satisﬁes weak approximation with Brauer-Manin
obstruction oﬀ ∞K : see Conjecture 3.0.1 for more details.

1.2. Questions. Let L/K be a nontrivial extension of number ﬁelds. Let S ⊂ ΩK be
a ﬁnite subset, and let SL ⊂ ΩL be the subset of all places above S. Given a smooth,
projective, and geometrically connected variety X over K, let XL = X ×Spec K Spec L be
its base change by L. In this paper, we consider the following questions.

Question 1.2.1. If the variety X has a K-rational point, and satisﬁes weak approxima-
tion with Brauer-Manin obstruction oﬀ S, must XL also satisfy weak approximation with
Brauer-Manin obstruction oﬀ SL?

2020 Mathematics Subject Classiﬁcation. Primary 11G35; Secondary 14G12, 14F22, 14G05.
Key words and phrases. rational points, Hasse principle, weak approximation, Brauer-Manin
obstruction.
 1

2 HAN WU

Question 1.2.2. Assume that the varieties X and XL are counterexamples to the Hasse
principle. If the failure of the Hasse principle of X is explained by the Brauer-Manin
obstruction, must the failure of the Hasse principle of XL also be explained by the Brauer-
Manin obstruction?

1.3. Main results. In this paper, we will construct smooth, projective, and geometrically
connected surfaces to give negative answers to Questions 1.2.

1.3.1. A negative answer to Question 1.2.1. For any number ﬁeld K, assuming Stoll’s
conjecture, Liang[Lia18] found a quadratic extension L, and constructed a 3-fold to give a
negative answer to Question 1.2.1. When L = Q(
√
5) and K = Q, using the construction
method, he gave an unconditional example with explicit equations in loc. cit. The author
[Wu21] generalized his argument to any nontrivial extension of number ﬁelds. The varieties
constructed there, are 3-folds. In this paper, we will prove the same statement for smooth,
projective, and geometrically connected surfaces.

For any nontrivial extension of number ﬁelds L/K, assuming Stoll’s conjecture, we have
the following theorem to give a negative answer to Question 1.2.1.

Theorem 1.3.1.1 (Theorem 4.1.7). For any nontrivial extension of number ﬁelds L/K,
assuming Stoll’s conjecture, there exists a smooth, projective, and geometrically connected
surface X deﬁned over K such that

• the surface X has a K-rational point, and satisﬁes weak approximation with
Brauer-Manin obstruction oﬀ ∞K,
• the surface XL does not satisfy weak approximation with Brauer-Manin obstruction
oﬀ T for any ﬁnite subset T ⊂ ΩL.

When K = Q and L = Q(i), using the construction method given in Theorem 4.1.7, we
give an explicit unconditional example in Subsection 5.2. The smooth, projective, and
geometrically connected surface X is deﬁned by the following equations:
{(w0w2 + w2
1 + 16w2
2)(x
2
0 + x
2
1 − x
2
2) + (w0w1 + w1w2)(x
2
0 − x
2
1) = 0
w2
1w2 = w3
0 − 16w3
2

in P2 × P2 with bi-homogeneous coordinates (w0 : w1 : w2) × (x0 : x1 : x2).

1.3.2. A negative answer to Question 1.2.2. For any number ﬁeld K, suppose that Stoll’s
conjecture holds. Assuming some conditions on the nontrivial extension L over K, the
author [Wu21] constructed a 3-fold to give a negative answer to Question 1.2.1. Uncondi-
tional examples with explicit equations were given in loc. cit. The varieties constructed
there, are 3-folds. In this paper, we will prove the same statement for smooth, projective,
and geometrically connected surfaces.

For any nontrivial extension of number ﬁelds L/K, assuming Stoll’s conjecture, we have
the following theorem to give a negative answer to Question 1.2.2.

Theorem 1.3.2.1 (Theorem 4.2.9). For any nontrivial extension of number ﬁelds L/K,
assuming Stoll’s conjecture, there exists a smooth, projective, and geometrically connected
surface X deﬁned over K such that

• the surface X is a counterexample to the Hasse principle, and its failure of the
Hasse principle is explained by the Brauer-Manin obstruction,
• the surface XL is a counterexample to the Hasse principle, but its failure of the
Hasse principle cannot be explained by the Brauer-Manin obstruction.

When K = Q and L = Q(i), using the construction method given in Theorem 4.2.9, we
give an explicit unconditional example in Subsection 5.3. The smooth, projective, and
geometrically connected surface X is deﬁned by the following two equations:




(w0w2 + w2
1 + 16w2
2)(x
2
0 − 41x
2
1)(x
2
0 − 3x
2
1)(x
2
0 − 123x
2
1)(y2
0 − 13y2
1)(y3
0 − 41y3
1)
+(w0w1 + w1w2)(x
2
0 − 17x
2
1)(x
2
0 − 13x
2
1)(x
2
0 − 221x
2
1)(y2
0 − 53y2
1)(y3
0 − 53y3
1) = 0
w2
1w2 = w3
0 − 16w3
2

NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR SURFACES 3

in P2 × P1 × P1 with tri-homogeneous coordinates (w0 : w1 : w2) × (x0 : x1) × (y0 : y1).

1.3.3. Main ideas behind our constructions in the proof of theorems. Let L/K be a nontriv-
ial extension of number ﬁelds. We ﬁnd a smooth, projective, and geometrically connected
curve C such that C(K) and C(L) are both ﬁnite, nonempty, and that C(K) ̸= C(L).
Then we construct a pencil of curves parametrized by the curve C : β : X → C such that
the ﬁber of each C(K) point is isomorphic to one given curve denoted by C∞, and that
the ﬁber of each C(L)\C(K) point is isomorphic to another given curve denoted by C0.
By combining some ﬁbration arguments with the functoriality of Brauer-Manin pairing,
the arithmetic properties of C∞ and C0 will determine the arithmetic properties of X. We
carefully choose the curves C∞ and C0 to meet the needs of theorems.

2. Notation and preliminaries

Let K be a number ﬁeld, and let OK be the ring of its integers. Let ΩK be the set of
all nontrivial places of K. Let ∞K ⊂ ΩK be the subset of all archimedean places, and
let Ωf
K = ΩK\∞K. Let ∞
r
K ⊂ ∞K be the subset of all real places, and let 2K ⊂ ΩK
be the subset of all 2-adic places. For v ∈ ΩK, let Kv be the completion of K at v. For
v ∈ ∞
r
K, let τv : K ֒→ R be the embedding of K into its completion. Given a ﬁnite subset
S ⊂ ΩK, let AK (respectively AS
K) be the ring of adèles (adèles without S components) of
K. We say that an element is a prime element, if the ideal generated by this element is a
prime ideal. For a prime element p ∈ OK, we denote its associated place by vp. We ﬁx an
algebraic closure K of K, and let ΓK = Gal(K/K). We always assume that a ﬁeld L is a
ﬁnite extension of K. Let SL ⊂ ΩL be the subset of all places above S.

In this paper, a K-scheme will mean a reduced, separated scheme of ﬁnite type over K,
and all geometric objects are K-schemes. A K-curve will mean a proper K-scheme such
that every irreducible components are of dimension one. In particular, a K-curve may
have more than one irreducible component, and may have singular points. We say that a
K-scheme is a K-variety if it is geometrically integral. Be cautious that in our deﬁnition, a
integral K-scheme may be not a variety, i.e. it may have multiple geometrically irreducible
components. Given a proper K-scheme X, if X(AK) ̸= ∅, let prS : X(AK) → X(AS
K) be
the projection induced by the natural projection prS : AK → AS
K. All cohomology groups
in this paper are Galois or étale cohomology groups, and let Br(X) = H 2
ét(X, Gm).

By combining the Čebotarev density theorem with global class ﬁeld theory, we have the
following lemma to choose prime elements. This lemma is a generalization of Dirichlet’s
theorem on arithmetic progressions.

Lemma 2.0.1. Given an extension of number ﬁelds L/K, let I ⊂ OK be a proper nonzero
ideal. Let x ∈ OK. Suppose that the image of x in OK/I is invertible. Then there exists
a prime element p ∈ OK such that

(1) p ≡ x mod I,
(2) τv(p) > 0 for all v ∈ ∞
r
K,
(3) additionally, if x = 1, then p splits completely in L.

And the set of places associated to such prime elements has positive density.

Proof. Let m∞ be the product of all places in ∞
r
K, and let m = Im∞ be a modulus of
K. Let Km be the ray class ﬁeld of modulus m. Let Im be the group of fractional ideals
that are prime to I. Let Pm ⊂ Im be the subgroup of principal ideals generated by some
a ∈ K × with a ≡ 1 mod I and τv(a) > 0 for all v ∈ ∞
r
K. Then by Artin reciprocity law
(cf. [Neu99, Theorem 7.1 and Corollary 7.2]), the classical Artin homomorphism θ gives
an exact sequence:
 0 → Pm ֒→ Im θ
→ Gal(Km/K) → 0.

By the generalized Dirichlet density theorem (cf. [Neu99, Theorem 13.2]), the set of places
associated to the prime elements satisfying conditions (1) and (2), has density 1/[Km : K].
Let M be a smallest Galois extension of K containing L, then a place of K splits completely

4 HAN WU

in L if and only if it splits completely in M. Let M Km be a composition ﬁeld of M and
Km. If x = 1, then by the Čebotarev density theorem (cf. [Neu99, Theorem 13.4]), the set
of places associated to the prime elements satisfying all these conditions (1), (2) and (3),
has density 1/[M Km : K]. □

2.1. Hilbert symbol. For a, b ∈ K ×
v and v ∈ ΩK, we use Hilbert symbol (a, b)v ∈ {±1}.
By deﬁnition, (a, b)v = 1 if and only if the curve deﬁned over Kv by the equation x
2
0 −
ax
2
1 − bx
2
2 = 0 in P2 with homogeneous coordinates (w0 : w1 : w2), has a Kv-point.

3. Stoll’s conjecture for curves

For a smooth, projective, and geometrically connected curve C deﬁned over a number
ﬁeld K, if the Tate-Shafarevich group and the rational points set of its Jacobian are both
ﬁnite, then by combining the Cassels-Tate pairing with the Brauer evaluation pairing,
Skorobogatov [Sko01, Chapter 6.2] and Scharaschkin [Sch99] independently observed that
C(K) = pr∞K (C(AK )
Br). In particular, if this curve C is a counterexample to the Hasse
principle, then this failure can be explained by the Brauer-Manin obstruction. Stoll [Sto07,
Theorem 8.6] generalized this observation. Furthermore, he [Sto07, Conjecture 9.1] made
the following conjecture.

Conjecture 3.0.1. [Sto07, Conjecture 9.1] For any smooth, projective, and geometrically
connected curve C deﬁned over a number ﬁeld K, the set C(K) is dense in pr∞K (C(AK )
Br).
In particular, if C(K) is ﬁnite, then C(K) = pr∞K (C(AK )
Br).

Remark 3.0.2. It is well known that for an elliptic curve over Q of analytic rank 0, its
Mordell-Weil group and Tate-Shafarevich group are both ﬁnite. By the dual sequence of
Cassels-Tate, Conjecture 3.0.1 holds for this elliptic curve.

The following deﬁnition and lemma have already been stated in the paper [Wu21]. We give
them below for the convenience of reading.

Deﬁnition 3.0.3. ([Wu21, Deﬁnition 4.0.3]) Given a smooth, projective, and geometrically
connected curve C deﬁned over a number ﬁeld K, let L/K be a nontrivial extension of
number ﬁelds. We say that a triple (C, K, L) is of type I if

• the sets C(K) and C(L) are both ﬁnite and nonempty,
• C(K) ̸= C(L),
• Stoll’s conjecture 3.0.1 holds for the curve C.

Lemma 3.0.4. ([Wu21, Lemma 4.0.4]) Let L/K be a nontrivial extension of number
ﬁelds. Suppose that Conjecture 3.0.1 holds for all smooth, projective, and geometrically
connected curves deﬁned over K. Then there exists a smooth, projective, and geometrically
connected curve C deﬁned over K such that the triple (C, K, L) is of type I.

The following lemma is a strong form of [Wu21, Lemma 6.1.3]. It will be used to choose a
dominant morphism from a given curve to P1.

Lemma 3.0.5. Let L/K be a nontrivial extension of number ﬁelds. Given a smooth,
projective, and geometrically connected curve C deﬁned over K, suppose that the triple
(C, K, L) is of type I (Deﬁnition 3.0.3). For any ﬁnite K-subscheme R ⊂ P1, there exists
a dominant K-morphism γ : C → P1 such that

• γ(C(K)) = {∞} ⊂ P1(K),
• γ(C(L)\C(K)) = {0} ⊂ P1(K),
• γ is étale over R.

Proof. The proof is along the same idea as the proof of [Wu21, Lemma 6.1.3], where the
statement was shown for R ⊂ P1\{0, ∞}. We will put one more condition for choosing
a rational function. Let K(C) be the function ﬁeld of C. For C(K) and C(L) are both
ﬁnite nonempty, and C(K) ̸= C(L), by Riemann-Roch theorem, we can choose a rational
function φ ∈ K(C)
×\K × such that

NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR SURFACES 5

• the set of its poles contains C(K),
• the set of its zeros contains C(L)\C(K),
• all poles and zeros are of multiplicity one.

Then this rational function φ gives a dominant K-morphism γ0 : C → P1 such that

• γ0(C(L)\C(K)) = {0} ⊂ P1(K),
• γ0(C(K)) = {∞} ⊂ P1(K),
• γ0 is étale over {0, ∞}.

Then the branch locus of γ0 is ﬁnite and contained in P1\{0, ∞}. We can choose an auto-
morphism ϕλ0 : P1 → P1, (u : v) ↦→ (λ0u : v) with λ0 ∈ K × such that the branch locus of
γ0 has no intersection with ϕλ0 (R). Let γ = (ϕλ0 )
−1 ◦ γ0. Then the morphism γ is étale
over R, and satisﬁes other conditions. □

4. Main results

In this section, we will construct smooth, projective, and geometrically connected surfaces
to give negative answers to Questions 1.2.

4.1. Non-invariance of weak approximation with Brauer-Manin obstruction for
surfaces. For any number ﬁeld K, assuming Conjecture 3.0.1, Liang [Lia18, Theorem
4.5] found a quadratic extension L, and constructed a 3-fold to give a negative answer to
Question 1.2.1. The author [Wu21, Theorem 6.2.1] generalized his result to any nontriv-
ial extension of number ﬁelds. Although the strategies of these two papers are diﬀerent,
the methods used there are combining the arithmetic properties of Châtelet surfaces with
a construction method from Poonen [Poo10]. Thus the varieties constructed there, are
3-folds. For any extension of number ﬁelds L/K, assuming Conjecture 3.0.1, in this sub-
section, we will construct a smooth, projective, and geometrically connected surface to give
a negative answer to Question 1.2.1. The method that we will use, is to combine some
ﬁbration lemmas with the arithmetic properties of curves, whose irreducible components
are projective lines.

4.1.1. Preparation Lemmas. We state the following lemmas, which will be used for the
proof of Theorem 4.1.7.

The following ﬁbration lemma has already been stated in the paper [Wu21]. We give them
below for the convenience of reading.

Lemma 4.1.1. ([Wu21, Lemma 6.1.1]) Let K be a number ﬁeld, and let S ⊂ ΩK be a
ﬁnite subset. Let f : X → Y be a K-morphism of proper K-varieties X and Y . Suppose
that

(1) the set Y (K) is ﬁnite,
(2) the variety Y satisﬁes weak approximation with Brauer-Manin obstruction oﬀ S,
(3) for any P ∈ Y (K), the ﬁber XP of f over P satisﬁes weak approximation oﬀ S.

Then the variety X satisﬁes weak approximation with Brauer-Manin obstruction oﬀ S.

The following ﬁbration lemma can be viewed as a modiﬁcation of [Wu21, Lemma 6.1.2] to
ﬁt into our context.

Lemma 4.1.2. Let K be a number ﬁeld, and let S ⊂ ΩK be a ﬁnite subset. Let f : X → Y
be a K-morphism of proper K-varieties X and Y . We assume that

(1) the set Y (K) is ﬁnite,
(2) there exists some P ∈ Y (K) such that the ﬁber XP of f over P does not satisfy
weak approximation with Brauer-Manin obstruction oﬀ S.

Then the variety X does not satisfy weak approximation with Brauer-Manin obstruction
oﬀ S.

6 HAN WU

Proof. By Assumption (2), take a P0 ∈ Y (K) such that the ﬁber XP0 does not satisfy weak
approximation with Brauer-Manin obstruction oﬀ S. Then there exist a ﬁnite nonempty
subset S′ ⊂ ΩK\S and a nonempty open subset L = ∏v∈S′ Uv × ∏v /∈S′ XP0 (Kv) ⊂
XP0 (AK) such that L ∩ XP0(AK)
Br ̸= ∅, but that L ∩ XP0(K) = ∅. By Assumption (1), the
set Y (K) is ﬁnite, so we can take a Zariski open subset VP0 ⊂ Y such that VP0 (K) = {P0}.
For any v ∈ S′, since Uv is open in XP0 (Kv) ⊂ f −1(VP0 )(Kv), we can take an open
subset Wv of f −1(VP0 )(Kv) such that Wv ∩ XP0 (Kv) = Uv. Consider the open subset
N = ∏
v∈S′ Wv × ∏v /∈S′ X(Kv) ⊂ X(AK), then L ⊂ N. By the functoriality of Brauer-
Manin pairing, we have XP0 (AK)
Br ⊂ X(AK)
Br. So the set N ∩X(AK)
Br ⊃ L∩XP0(AK)
Br,
is nonempty. But N ∩ X(K) = N ∩ XP0 (K) = L ∩ XP0(K) = ∅, which implies that X does
not satisfy weak approximation with Brauer-Manin obstruction oﬀ S. □

The following lemma states that a K-scheme with multiple geometrically irreducible com-
ponents will violate weak approximation.

Lemma 4.1.3. Let K be a number ﬁeld, and let S ⊂ ΩK be a ﬁnite subset. Let X be a K-
scheme, which is not a K-variety, i.e. it has multiple geometrically irreducible components.
We assume ∏

v∈ΩK X(Kv) ̸= ∅, then the variety X does not satisfy weak approximation
oﬀ S.

Proof. Let X 0 be the smooth locus of X. Claim that X 0 ⊂ X is an open dense subscheme.
We prove the claim ﬁrst. For X is reduced and K is of characteristic 0, the scheme X
is geometrically reduced. For any geometrically irreducible component of X, by [Har97,
Chapter II. Corollary 8.16], its smooth locus is open dense in this geometrically irreducible
component. So the claim follows. From this claim, we have X and X 0 have the same
number of geometrically irreducible components.

By assumption that X has multiple geometrically irreducible components, let X 0
1 and X 0
2
be two diﬀerent geometrically irreducible components of X 0, deﬁned over the number ﬁelds
K1 and K2 respectively. By Lang-Weil estimate [LW54], the varieties X 0
1 and X 0
2 have local
points for almost all places of K1 and K2 respectively. By the Čebotarev density theorem,
we can take two diﬀerent places v1, v2 ∈ Ωf
K\S such that v1, v2 split in K1 and also in K2,
and that X 0
1 (Kv1 ) ̸= ∅ and X 0
2 (Kv2 ) ̸= ∅. For ∏
v∈ΩK X(Kv) ̸= ∅, we consider a nonempty
open subset L = X 0
1 (Kv1) × X 0
2 (Kv2 ) × ∏
v∈ΩK \{v1,v2} X(Kv) ⊂ ∏v∈ΩK X(Kv). For X 0 is
smooth, and the varieties X 0
1 , X 0
2 are diﬀerent geometrically irreducible components, we
have X 0
1 (Kv1 ) ∩ X 0
2 (Kv1) = ∅, which implies X(K) ∩ L = ∅. Hence X does not satisfy weak
approximation oﬀ S. □

The following two lemmas state that two projective lines meeting at one point will violate
weak approximation with Brauer-Manin obstruction.

Lemma 4.1.4. Let C be a curve deﬁned over a number ﬁeld K by a homogeneous equation:
x
2
0 − x
2
1 = 0 in P2 with homogeneous coordinates (x0 : x1 : x2). Then the natural restriction
map Br(K) → Br(C), is an isomorphism.

Proof. Let C1 and C2 be two irreducible components of C. Let i1, i2 and i3 be the natural
embeddings of C1, C2 and C1 ∩ C2 in C respectively. Then we have the following sequence
of étale sheaves on C :

0 → OC → i1∗OC1 ⊕ i2∗OC2 → i3∗OC1∩C2 → 0,

where the map i2∗OC2 → i3∗OC1∩C2 is the opposite of the restriction map, and other
maps are canonical restriction maps. By checking the exactness of this sequence at each
geometric point of C, and [Mil80, Chapter II. Theorem 2.15], it is exact. It gives rise to an
exact sequence of étale sheaves on C :

0 → Gm,C → i1∗Gm,C1 ⊕ i2∗Gm,C2 → i3∗Gm,C1∩C2 → 0.

For the intersection C1∩C2 is a rational point, this sequence splits. Using étale cohomology,
for any integer n ≥ 0, we have an exact sequence:

0 → H n
ét(C, Gm) → H n
ét(C, i1∗Gm,C1 ⊕ i2∗Gm,C2) → H n
ét(C, i3∗Gm,C1∩C2) → 0.

NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR SURFACES 7

For i1, i2 and i3 are closed embeddings, by [Mil80, Chapter II. Corollary 3.6], the functors
i1∗, i2∗ and i3∗ are exact. Since C1 and C2 are isomorphic to P1, we have the following
commutative diagram:

0 // H n
ét(C, Gm) // H n
ét(C, i1∗Gm,C1 ⊕ i2∗Gm,C2) //

∼=
  
 H n
ét(C, i3∗Gm,C1∩C2) //

∼=
  
 0

0 // H n
ét(C, Gm) // H n
ét(P1, Gm) ⊕ H n
ét(P1, Gm) // H n(ΓK, K ×) // 0

with exact rows. By taking n = 2, we have an exact sequence:

0 → Br(C) → Br(K) ⊕ Br(K) → Br(K) → 0.

So we have Br(K) ∼= Br(C). □

Remark 4.1.5. In [HS14], Harpaz and Skorobogatov used another exact sequence of étale
sheaves on C (cf. Proposition 1.1 in loc. cit.) to calculate the Brauer group of C. By easy
computation, this lemma can be gotten from their Corollary 1.5 in loc. cit.

Lemma 4.1.6. Let K be a number ﬁeld, and let S ⊂ ΩK be a ﬁnite subset. Let C be a
curve deﬁned over K by a homogeneous equation: x
2
0 − x
2
1 = 0 in P2 with homogeneous
coordinates (x0 : x1 : x2). Then the curve C does not satisfy weak approximation with
Brauer-Manin obstruction oﬀ S.

Proof. For the curve C has K-rational points and two irreducible components, by Lemma
4.1.3, it does not satisfy weak approximation oﬀ S. By Lemma 4.1.4, we have Br(K) ∼=
Br(C). So the curve C does not satisfy weak approximation with Brauer-Manin obstruction
oﬀ S. □

Theorem 4.1.7. For any nontrivial extension of number ﬁelds L/K, assuming that Con-
jecture 3.0.1 holds over K, there exists a smooth, projective, and geometrically connected
surface X deﬁned over K such that

• the surface X has a K-rational point, and satisﬁes weak approximation with
Brauer-Manin obstruction oﬀ ∞K,
• the surface XL does not satisfy weak approximation with Brauer-Manin obstruction
oﬀ T for any ﬁnite subset T ⊂ ΩL.

Proof. We will construct a smooth, projective, and geometrically connected surface X. Let
C∞ be a projective line deﬁned over K by a homogeneous equation: x
2
0 + x
2
1 − x
2
2 = 0 in
P2 with homogeneous coordinates (x0 : x1 : x2). Let C0 be a curve deﬁned over K by a
homogeneous equation: x
2
0 − x
2
1 = 0 in P2 with homogeneous coordinates (x0 : x1 : x2). Let
(u0 : u1)×(x0 : x1 : x2) be the coordinates of P1 ×P2, and let s′ = u0(x
2
0 +x
2
1 −x
2
2)+u1(x
2
0 −
x
2
1) ∈ Γ(P1 × P2, O(1, 2)). Let X ′ be the locus deﬁned by s′ = 0 in P1 × P2. For the curves
C∞ and C0 meet transversally, the locus X ′ is smooth. Let R be the locus over which the
composition X ′ ֒→ P1 × P2 pr1
→ P1 is not smooth. Then by [Har97, Chapter III. Corollary
10.7], it is ﬁnite over K. By the assumption that Conjecture 3.0.1 holds over K, and Lemma
3.0.4, we can take a smooth, projective, and geometrically connected curve C deﬁned over
K such that the triple (C, K, L) is of type I. By Lemma 3.0.5, we can choose a K-morphism
γ : C → P1 such that γ(C(L)\C(K)) = {0} ⊂ P1(K), γ(C(K)) = {∞} ⊂ P1(K), and that
γ is étale over R. Let B = C × P2, and let (γ, id) : B → P1 × P2. Let L = (γ, id)
∗O(1, 2),
and let s = (γ, id)
∗(s′) ∈ Γ(B, L). Let X be the zero locus of s in B. For γ is étale over
the locus R, the surface X is smooth. Since X is deﬁned by the support of the global
section s, it is an eﬀective divisor. The invertible sheaf L (X ′) on P1 × P2 is isomorphic to
O(1, 2), which is a very ample sheaf on P1 × P2. And (γ, id) is a ﬁnite morphism, so the
pull back of this ample sheaf is again ample, which implies that the invertible sheaf L (X)
on C × P2 is ample. By [Har97, Chapter III. Corollary 7.9], the surface X is geometrically
connected. So the surface X is smooth, projective, and geometrically connected. Let

8 HAN WU

β : X ֒→ B = C × P2 pr1
→ C be the composition morphism. By our construction, we have
the following Cartesian diagram:
 X• _

  
 //

β
 ##
 X ′• _

  
C × P2

pr1
  
 (γ,id) // P1 × P2

pr1
  
C γ // P1

Next, we will check that the surface X has the properties.

We will show that X has a K-rational point. For any P ∈ C(K), the ﬁber β−1(P ) ∼= C∞.
The projective line C∞ has a K-rational point, so the set X(K) ̸= ∅.
We will show that X satisﬁes weak approximation with Brauer-Manin obstruction oﬀ ∞K.
Since the projective line C∞ satisﬁes weak approximation, also weak approximation oﬀ
∞K, we consider the morphism β, then Assumption (3) of Lemma 4.1.1 holds. Since
Conjecture 3.0.1 holds for the curve C, using Lemma 4.1.1 for the morphism β, the surface
X satisﬁes weak approximation with Brauer-Manin obstruction oﬀ ∞K.

For any ﬁnite subset T ⊂ ΩL, we will show that XL does not satisfy weak approximation
with Brauer-Manin obstruction oﬀ T. We take a point Q ∈ C(L)\C(K), by the choice of
the curve C and morphism β, the ﬁber β−1(Q) ∼= C0L. By Lemma 4.1.6, the curve C0L does
not satisfy weak approximation with Brauer-Manin obstruction oﬀ T ∪ ∞L. By Lemma
4.1.2, the surface XL does not satisfy weak approximation with Brauer-Manin obstruction
oﬀ T ∪ ∞L. So it does not satisfy weak approximation with Brauer-Manin obstruction oﬀ
T. □

4.2. Non-invariance of the failures of the Hasse principle explained by the
Brauer-Manin obstruction for surfaces. For an extension of number ﬁelds L/K, as-
suming that the degree [L : K] is odd, or that the ﬁeld L has one real place, also assuming
Conjecture 3.0.1, the author [Wu21, Theorem 6.3.1 and Theorem 6.3.2] constructed 3-folds
to give negative answers to Question 1.2.2. The method used there is combining the arith-
metic properties of Châtelet surfaces with a construction method from Poonen [Poo10].
Thus the varieties constructed there, are 3-folds. For any extension of number ﬁelds L/K,
assuming Conjecture 3.0.1, in this subsection, we will construct a smooth, projective, and
geometrically connected surface to give a negative answer to Question 1.2.2.

4.2.1. Preparation lemmas. We state the following lemmas, which will be used for Choosing
curves.

Lemma 4.2.1. Let K be a number ﬁeld. Let p1, p2 be two odd prime elements, and
vp1 ̸= vp2 . If (p1, p2)vp1 = 1, then p2 ∈ K ×2
vp1 . Otherwise, if (p1, p2)vp1 = −1, then p2 /∈ K ×2
vp1 .

Proof. Consider the case (p1, p2)vp1 = 1. By deﬁnition, the equation x
2
0 − p1x
2
1 − p2x
2
2 = 0
has a nontrivial solution in Kvp1 . Let (x0, x1, x2) = (a, b, c) be a primitive solution of this
equation. By comparing the valuations, we have vp1 (a) = vp1 (c) = 0. So a2 − p2c2 ≡ 0
mod p1. For p1 is an odd prime element, by Hensel’s lemma, we have p2 ∈ K ×2
vp1 . This
proves the ﬁrst part of this lemma. If p2 ∈ K ×2
vp1 , then (p1, p2)vp1 = 1, which implies the
last argument. □

Lemma 4.2.2. Let K be a number ﬁeld, and let v ∈ Ωf
K. Then there exists a proper
nonzero ideal I ⊂ OK such that for any a ∈ OK, if a ≡ 1 mod I, then a ∈ K ×2
v .

Proof. Let p be the prime number such that v|p in K. Let I be the ideal generated by p3.
Then by Hensel’s lemma, we have 1 + p3OKv ⊂ K ×2
v , which implies this lemma. □

NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR SURFACES 9

Lemma 4.2.3. Let K be a number ﬁeld. Let p1, p2 be two odd prime elements, and
vp1 ̸= vp2 . Let I ⊂ OK be the ideal generated by p1p2. Then there exists an element
x ∈ OK such that

• the image of x in OK/I is invertible,
• for any a ∈ OK, if a ≡ x mod I, then (p1, a)vp1 = −1 and (p2, a)vp2 = 1.

Proof. We take an element x1 ∈ (OK /p1)\(OK /p1)
2, and let x1 ∈ OK be a lift of x1. By
Chinese remainder theorem, we choose an element x ∈ OK such that x ≡ x1 mod p1 and
x ≡ 1 mod p2. By the similar argument as in the proof of Lemma 4.2.1, this element x
satisﬁes the conditions. □

4.2.2. Choosing one curve with respect to an extension. In this subsubsection, we will
choose one curve with some given arithmetic properties. Given an extension of number
ﬁelds L/K, by Lemmas 4.2.2 and 2.0.1, we can choose an odd prime element p1 ∈ OK
satisfying the following conditions:

• τv(p1) > 0 for all v ∈ ∞
r
K,
• p1 ∈ K ×2
v for all v ∈ 2K,
• p1 splits in L.

By Lemmas 4.2.1, 4.2.2 and 2.0.1, we can choose an odd prime element p2 ∈ OK satisfying
the following conditions:

• (p1, p2)vp1 = 1,
• p2 splits in L,
• vp2 ̸= vp1 .

Let L′ = L(
√
p1, √
p2). By Lemma 2.0.1, we can choose an odd prime element p3 ∈ OK
such that vp3 /∈ {vp1 , vp2 }, and that vp3 splits in L′. Let f (x0, x1; y0, y1) = (x
2
0 − p1x
2
1)(x
2
0 −
p2x
2
1)(x
2
0 − p1p2x
2
1)(y2
0 − p3y2
1)(y3
0 − p3y3
1) be a bi-homogeneous polynomial, and let Z f be
the zero locus of f in P1 × P1 with bi-homogeneous coordinates (x0 : x1) × (y0 : y1). With
the notation, we have the following lemmas.

Lemma 4.2.4. Let Z f ⊂ P1 × P1 be the zero locus deﬁned over K by the bi-homogeneous
polynomial f (x0, x1; y0, y1). Then the curves Z f and Z f
L violate the Hasse principle.

Proof. By the condition that the prime elements p1, p2 and p3 split in L, the set Z f (K) =
Z f (L) = ∅. It will be suﬃce to prove that for any v ∈ ΩK, the equation (x
2
0 − p1x
2
1)(x
2
0 −
p2x
2
1)(x
2
0 − p1p2x
2
1) = 0 has a Kv-solution in P1 with homogeneous coordinates (x0 : x1).

Suppose that v ∈ ∞K ∪ 2K. Then, by the choice of p1, we have p1 ∈ K ×2
v , so the equation
x
2
0 − p1x
2
1 = 0 has a Kv-solution in P1.
Suppose that v = vp1 . Then, by the choice of p2, we have (p1, p2)vp1 = 1. By Lemma 4.2.1,
we have p2 ∈ K ×2
vp1 . Hence the equation x
2
0 − p2x
2
1 = 0 has a Kv-solution in P1.
Suppose that v = vp2 . Using the product formula ∏v∈ΩK (p1, p2)v = 1, we have (p1, p2)vp2 =
1. By Lemma 4.2.1, we have p1 ∈ K ×2
vp2 . Hence the equation x
2
0 −p1x
2
1 = 0 has a Kv-solution
in P1.
Suppose that v ∈ ΩK\(∞K ∪ 2K ∪ {vp1 , vp2 }), then, by the quadratic reciprocity law, at
least one of equations: x
2
0 − p1x
2
1 = 0, x
2
0 − p2x
2
1 = 0, x
2
0 − p1p2x
2
1 = 0, has a Kv-solution
in P1.
So Z f (AK ) ̸= ∅. □

Lemma 4.2.5. The natural restriction map Br(L) → Br(Z f
L), is an isomorphism.

Proof. Let C1 (respectively C2) be the locus deﬁned over L by the equation (x
2
0 −p1x
2
1)(x
2
0 −
p2x
2
1)(x
2
0 − p1p2x
2
1) = 0 (respectively (y2
0 − p3y2
1)(y3
0 − p3y3
1) = 0) in P1 × P1 with bi-
homogeneous coordinates (x0 : x1) × (y0 : y1). Then C1 and C2 are smooth curves in Z f
L,
and Z f
L = C1 ∪ C2. Let i1, i2 and i3 be the natural embeddings of C1, C2 and C1 ∩ C2 in

10 HAN WU

C respectively. Similar to the proof of Lemma 4.1.4, we have the following exact sequence
of étale sheaves on Z f
L :

0 → OZf
L → i1∗OC1 ⊕ i2∗OC2 → i3∗OC1∩C2 → 0,

where the map i2∗OC2 → i3∗OC1∩C2 is the opposite of the restriction map, and other
maps are canonical restriction maps. This sequence gives rise to an exact sequence of étale
sheaves on C :
 0 → Gm,Zf
L → i1∗Gm,C1 ⊕ i2∗Gm,C2 → i3∗Gm,C1∩C2 → 0.

By the long exact sequence of étale cohomology, we have the following exact sequence:

H 1
ét(Z f
L, i3∗Gm,C1∩C2) → H 2
ét(Z f
L, Gm) → H 2
ét(Z f
L, i1∗Gm,C1⊕i2∗Gm,C2) → H 2
ét(Z f
L, i3∗Gm,C1∩C2).

For i1, i2 and i3 are closed embeddings, it gives the following exact sequence:

(1) H 1
ét(C1 ∩ C2, Gm) → Br(Z f
L) → Br(C1) ⊕ Br(C2) → Br(C1 ∩ C2).

By our choice, two diﬀerent places vp1 and vp2 split in L, so we have number ﬁelds L(
√
p1),
L(
√
p2), L(
√
p1p2), denoted by L10, L20, L30 respectively. And

C1 ∼= (Spec L10 ×Spec L P1) ⊔
(Spec L20 ×Spec L P1) ⊔(Spec L30 ×Spec L P1).

So Br(C1) ∼= ⊕3
i=1 Br(Li0).

Similarly, we have number ﬁelds L(
√
p3), L( 3√
p3), denoted by L01, L02 respectively. And

C2 ∼= (P1 ×Spec L Spec L01) ⊔(P1 ×Spec L Spec L02).

Then Br(C2) ∼= ⊕2
j=1 Br(L0j).

Since the diﬀerent places vp1 , vp2 and vp3 split in L, for any i ∈ {1, 2, 3}, and any j ∈ {1, 2},
we have number ﬁelds Li0 ⊗L L0j, denoted by Lij. Then

C1 ∩ C2 ∼=
 3⊔

i=1
 2⊔

j=1 Spec Lij.

So Br(C1 ∩ C2) ∼= ⊕3
i=1 ⊕2
j=1 Br(Lij).

By Hilbert’s Theorem 90, we have H 1
ét(C1 ∩ C2, Gm) = 0. By the exact sequence (1), we
have an exact sequence:

(2) 0 → Br(Z f
L) → Br(C1) ⊕ Br(C2) → Br(C1 ∩ C2).

By Lemma 4.2.4, the set Z f
L(AL) ̸= ∅. Indeed, from the prove of Lemma 4.2.4, the set
C1(AL) ̸= ∅. We take an adelic point (Pv′ )v′∈ΩL ∈ C1(AL), then the evaluation of elements
in Br(C1) on this adelic point gives a map: Br(C1) → ⊕
v′∈ΩL Br(Lv′ ), which makes the
following diagram:
 Br(L)
 &&◆◆◆◆◆◆◆◆◆◆◆ // Br(Z f
L) // Br(C1)

ww♣♣♣♣♣♣♣♣♣♣♣♣

⊕v′∈ΩL Br(Lv′)

commutative. By the reciprocity law of global class ﬁeld theory, the map Br(L) →
⊕v′∈ΩL Br(Lv′) is injective, so the natural map Br(L) → Br(Z f
L) is injective. We have the

NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR SURFACES 11

following commutative diagram:

Br(L)• _

  
0 // Br(Z f
L) // Br(C1) ⊕ Br(C2) //

∼=
  
 Br(C1 ∩ C2)

∼=
  
0 // Br(Z f
L) // ⊕3
i=1 Br(Li0) ⊕ ⊕2
j=1 Br(L0j) // ⊕3
i=1 ⊕2
j=1 Br(Lij)

with exact rows. Next, we will prove that the natural map Br(L) → Br(Z f
L) is surjective.
By the commutative diagram, we need to prove that the sequence:

Br(L) →
 3⊕

i=1 Br(Li0) ⊕
 2⊕

j=1 Br(L0j) →
 3⊕

i=1
 2⊕

j=1 Br(Lij)

is exact. Notice that by our choice, the map ⊕2
j=1 Br(L0j) → ⊕3
i=1 ⊕2
j=1 Br(Lij ) is the
opposite of the restriction map, and other maps are canonical restriction maps. Take
an element (αi0, α0j) ∈ ⊕3
i=1 Br(Li0) ⊕ ⊕2
j=1 Br(L0j). Suppose that it goes to zero in
⊕3
i=1 ⊕2
j=1 Br(Lij). So the restrictions of αi0 and α0j to Br(Lij) coincide. Also con-
sider the adelic point (Pv′ )v′∈ΩL and the map: Br(C1) → ⊕
v′∈ΩL Br(Lv′). By Br(C1) ∼=
⊕3
i=1 Br(Li0), we view (αi0) as an element in Br(C1) and let (av′ )v′∈ΩL be its image in⊕
v′∈ΩL Br(Lv′). Then for any j ∈ {1, 2}, we have the following commutative diagram:

(3) Br(C1)

  
0 // Br(L)

  
 // ⊕
v′∈ΩL Br(Lv′ )

  
 // Q/Z

[L0j :L]
  
 // 0

0 // Br(L0j) // ⊕v′∈ΩL Br(L0j ⊗L Lv′) // Q/Z // 0.

By the reciprocity law of global class ﬁeld theory, two rows of this diagram are exact.
For the restrictions of αi0 and α0j to Br(Lij ) coincide, the restrictions of (av′ )v′∈ΩL and
α0j to ⊕
v′∈ΩL Br(L0j ⊗L Lv′ ) coincide. So [L0j : L] ∑
v′∈ΩL invv′ (av′ ) = 0 in Q/Z. For
the degrees [L01 : L] = 2 and [L02 : L] = 3, we have ∑v′∈ΩL invv′ (av′ ) = 0 in Q/Z. By
the exact sequence of the ﬁrst row, let a ∈ Br(L) be the element such that its image in⊕v′∈ΩL Br(Lv′) equals (av′ )v′∈ΩL . Let a|L0j and a|Li0 be the restrictions of a to Br(L0j)
and Br(Li0) respectively. Then from the diagram (3), we have a|L0j = α0j. For any
i ∈ {1, 2, 3}, we consider the element αi0 − a|Li0 . For the restrictions of αi0 − a|Li0 and
α0j − a|L0j = 0 to Br(Lij) coincide, they are zero in Br(Lij). By the standard restriction-
corestriction argument, we have [L0j : L](αi0 − a|Li0) = 0 in Br(Li0). For the degrees
[L01 : L] = 2 and [L02 : L] = 3, we have a|Li0 = αi0. So the element a maps to the element
(αi0, α0j), which implies that the map Br(L) → Br(Z f
L) is surjective. □

Remark 4.2.6. In our proof, the map Br(C1) → ⊕

v′∈ΩL Br(Lv′ ), depends on the choice of
the adelic point (Pv′ )v′∈ΩL in C1(AL). We use this adelic point to illustrate that the map
Br(L) → Br(Z f
L) is injective. In order to prove this injection, by using the information from
C2, the curve Z f
L contains closed points of degree 2 and 3, then one can use the standard
restriction-corestriction argument to get this injection. The idea to proof that this map is
surjective, comes from [HS14, Proposition 3.1].

12 HAN WU

4.2.3. Choosing another curve with respect to an extension. In this subsubsection, we will
choose another curve with some given arithmetic properties. Given an extension of number
ﬁelds L/K, similar to the choice of p1, we can choose an odd prime element p4 ∈ OK
satisfying the following conditions:

• τv(p4) > 0 for all v ∈ ∞
r
K,
• p4 ∈ K ×2
v for all v ∈ 2K,
• p4 splits in L,
• vp4 /∈ {vp1, vp2 , vp3 }.

By Lemmas 4.2.3 and 2.0.1, we choose an odd prime element p5 ∈ OK satisfying the
following conditions:

• (p4, p5)vp4 = −1,
• vp5 /∈ {vp1, vp2 , vp3 , vp4 }.

Similarly, by Lemmas 4.2.3 and 2.0.1, we choose an odd prime element p6 ∈ OK satisfying
the following conditions:

• (p4, p6)vp4 = −1,
• (p5, p6)vp5 = 1,
• vp6 /∈ {vp1, vp2 , vp3 , vp4 , vp5 }.

Let g(x0, x1; y0, y1) = (x
2
0 − p4x
2
1)(x
2
0 − p5x
2
1)(x
2
0 − p4p5x
2
1)(y2
0 − p6y2
1)(y3
0 − p4y3
1) be a bi-
homogeneous polynomial, and let Z g be the zero locus of g in P1 × P1 with bi-homogeneous
coordinates (x0 : x1) × (y0 : y1). With the notation, we have the following lemma.

Lemma 4.2.7. Let Z g ⊂ P1 × P1 be the zero locus deﬁned over K by the bi-homogeneous
polynomial g(x0, x1; y0, y1). Then Z g(A{vp4 }
K ) ̸= ∅ but Z g(Kvp4 ) = ∅.

Proof. Suppose that v ∈ ∞K ∪ 2K. Then, by the choice of p4, we have p4 ∈ K ×2
v . So the
equation x
2
0 − p4x
2
1 = 0 has a Kv-solution in P1 with homogeneous coordinates (x0 : x1).
Suppose that v = vp5 . Then, by the choice of p6, we have (p5, p6)vp5 = 1. By Lemma
4.2.1, we have p6 ∈ K ×2
vp5 . So the equation y2
0 − p6y2
1 = 0 has a Kv-solution in P1 with
homogeneous coordinates (y0 : y1).
Suppose that v ∈ ΩK\(∞K ∪ 2K ∪ {vp4 , vp5 }), then, by the quadratic reciprocity law, at
least one of equations: x
2
0 − p4x
2
1 = 0, x
2
0 − p5x
2
1 = 0, x
2
0 − p4p5x
2
1 = 0, has a Kv-solution
in P1 with homogeneous coordinates (x0 : x1).
So Z g(A{vp4 }
K ) ̸= ∅.

Suppose that v = vp4 . Then the equations x
2
0 −p4x
2
1 = 0, x
2
0 −p4p5x
2
1 = 0 and y3
0 −p4y3
1 = 0
has no Kv-solution in P1 with homogeneous coordinates (x0 : x1) and (y0 : y1) respectively.
By the choice of p5, p6, we have (p4, p5)vp4 = −1 and (p4, p6)vp4 = −1. By Lemma 4.2.1,
we have p5 /∈ K ×2
vp4 and p6 /∈ K ×2
vp4 . So the equations x
2
0 − p5x
2
1 = 0 and y2
0 − p6y2
1 = 0 have
no Kv-solution in P1 with homogeneous coordinates (x0 : x1) and (y0 : y1) respectively. So
Z g(Kvp4 ) = ∅. □

Example 4.2.8. For K = Q and L = Q(i), let prime elements (p1, p2, p3, p4, p5, p6) =
(17, 13, 53, 41, 3, 13). Then they satisfy all chosen conditions of Subsubsections 4.2.2 and
4.2.3. They will be used for construction of our explicit unconditional example.

Theorem 4.2.9. For any nontrivial extension of number ﬁelds L/K, assuming that Con-
jecture 3.0.1 holds over K, there exists a smooth, projective, and geometrically connected
surface X deﬁned over K such that

• the surface X is a counterexample to the Hasse principle, and its failure of the
Hasse principle is explained by the Brauer-Manin obstruction,
• the surface XL is a counterexample to the Hasse principle, but its failure of the
Hasse principle cannot be explained by the Brauer-Manin obstruction.

NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR SURFACES 13

Proof. We will construct a smooth, projective, and geometrically connected surface X. For
the extension L/K, we choose odd prime elements p1, p2, p3, p4, p5, p6 ∈ OK as in Subsub-
sections 4.2.2 and 4.2.3. Let f (x0, x1; y0, y1) = (x
2
0 − p1x
2
1)(x
2
0 − p2x
2
1)(x
2
0 − p1p2x
2
1)(y2
0 −
p3y2
1)(y3
0 − p3y3
1) and g(x0, x1; y0, y1) = (x
2
0 − p4x
2
1)(x
2
0 − p5x
2
1)(x
2
0 − p4p5x
2
1)(y2
0 − p6y2
1)(y3
0 −
p4y3
1) be two bi-homogeneous polynomials, and let Z f and Z g be the zero loci of f and
g respectively in P1 × P1 with bi-homogeneous coordinates (x0 : x1) × (y0 : y1). Let
(u0 : u1) × (x0 : x1) × (y0 : y1) be the coordinates of P1 × P1 × P1, and let s′ =
u0g(x0, x1; y0, y1) + u1f (x0, x1; y0, y1) ∈ Γ(P1 × P1 × P1, O(1, 6, 5)). Let X ′ be the locus
deﬁned by s′ = 0 in P1 × P1 × P1. For the curves Z f and Z g meet transversally, the locus
X ′ is smooth. Let R be the locus over which the composition X ′ ֒→ P1 × P1 × P1 pr1
→ P1

is not smooth. Then by [Har97, Chapter III. Corollary 10.7], it is ﬁnite over K. By
the assumption that Conjecture 3.0.1 holds over K, and Lemma 3.0.4, we can take a
smooth, projective, and geometrically connected curve C deﬁned over K such that the
triple (C, K, L) is of type I. By Lemma 3.0.5, we can choose a K-morphism γ : C → P1

such that γ(C(L)\C(K)) = {0} ⊂ P1(K), γ(C(K)) = {∞} ⊂ P1(K), and that γ is étale
over R. Let B = C × P1 × P1, and let (γ, id) : B → P1 × P1 × P1. Let L = (γ, id)
∗O(1, 6, 5),
and let s = (γ, id)
∗(s′) ∈ Γ(B, L). Let X be the zero locus of s in B. By the same argument
as in the proof of Theorem 4.1.7, the surface X is smooth, projective, and geometrically
connected. Let β : X ֒→ B = C × P1 × P1 pr1
→ C be the composition morphism. By our
construction, we have the following Cartesian diagram:

X• _

  
 //

β
 ''
 X ′• _

  
C × P1 × P1

pr1
  
 (γ,id) // P1 × P1 × P1

pr1
  
C γ // P1

Next, we will check that the surface X has the properties.

We will show X(AK) ̸= ∅. For any P ∈ C(K), the ﬁber β−1(P ) ∼= Z g. By Lemma 4.2.7,
the set Z g(A{vp4 }
K ) ̸= ∅. So the set X(A{vp4 }
K ) ̸= ∅. For vp4 splits in L, we take a place
v′ ∈ Ωf
L above vp4 such that Kvp4 = Lv′ . By Lemma 4.2.4, the set Z f (AL) ̸= ∅. Take
a point Q ∈ C(L)\C(K), then the ﬁber β−1(Q) ∼= Z f
L. We have X(Kvp4 ) = XL(Lv′) ⊃
β−1(Q)(Lv′ ) ∼= Z f (Lv′ ) ̸= ∅. So the set X(AK) ̸= ∅.
We will show X(AK)
Br = ∅. By our choice and Conjecture 3.0.1, the set C(K) is ﬁnite,
and C(K) = pr∞K (C(AK )
Br). By the functoriality of Brauer-Manin pairing, we have
pr∞K (X(AK)
Br) ⊂ ⊔
P ∈C(K) β−1(P )(A∞K
K ). But by Lemma 4.2.7, the set Z g(Kvp4 ) = ∅,
so we have pr∞K (X(AK)
Br) ⊂ ⊔
P ∈C(K) β−1(P )(A∞K
K ) ∼= Z g(A∞K
K ) × C(K) = ∅, which
implies that X(AK)
Br = ∅.
So, the surface X is a counterexample to the Hasse principle, and its failure of the Hasse
principle is explained by the Brauer-Manin obstruction.

We will show XL(AL)
Br ̸= ∅. Take a point Q ∈ C(L)\C(K). By Lemma 4.2.5, the set
Z f
L(AL)
Br = Z f
L(AL). By Lemma 4.2.4, it is nonempty. By the functoriality of Brauer-
Manin pairing, the set XL(AL)
Br contains β−1(Q)(AL)
Br ∼= Z f
L(AL)
Br, so XL(AL)
Br ̸= ∅.
We will show X(L) = ∅. By Lemma 4.2.7 and the condition that vp4 splits in L, we have
Z g(AL) = ∅, so the set Z g(L) = ∅. By Lemma 4.2.4, the set Z f (L) = ∅. Since each L-
rational ﬁber of β is isomorphic to Z g
L or Z f
L, the set X(L) = ∅.
So, the variety XL is a counterexample to the Hasse principle, but its failure of the Hasse
principle cannot be explained by the Brauer-Manin obstruction. □

5. Explicit unconditional examples

In this section, let K = Q and L = Q(i). For this extension L/K, we will give explicit
examples without assuming Conjecture 3.0.1 for Theorem 4.1.7 and Theorem 4.2.9.

14 HAN WU

5.1. Choosing an elliptic curve and a dominant morphism. For the extension L/K,
as in the proof of Theorem 4.1.7 and Theorem 4.2.9, we can choose a common elliptic curve
over K for these examples.

5.1.1. Choosing an elliptic curve. For the extension L/K, we will choose an elliptic curve
such that the triple (E, K, L) is of type I. Let E be an elliptic curve deﬁned over Q by a
homogeneous equation: w2
1w2 = w3
0 − 16w3
2
in P2 with homogeneous coordinates (w0 : w1 : w2). Its quadratic twist E(−1) is isomor-
phic to an elliptic curve deﬁned by a homogeneous equation: w2
1w2 = w3
0 + 16w3
2. The
elliptic curves E and E(−1) over Q, are of analytic rank 0. Then the Tate-Shafarevich
group X(E, K) is ﬁnite, so the curve E satisﬁes weak approximation with Brauer-Manin
obstruction oﬀ ∞K. The Mordell-Weil groups E(K) and E(−1)(K) are both ﬁnite, so the
group E(L) is ﬁnite. Using [Ste12, SageMath], we check that the Mordell-Weil group
E(K) = {(0 : 1 : 0)} and E(L) = {(0 : ±4i : 1), (0 : 1 : 0)}. So the triple (E, K, L) is of
type I.

5.1.2. Choosing a dominant morphism. We choose the following dominant morphism from
the elliptic curve E to P1, which satisﬁes some conditions of Lemma 3.0.5.

Let P2\{(1 : 0 : 0), (−16 : 0 : 1), (−1 : ±√
15i : 1)} → P1 be a morphism over Q given by
(w0 : w1 : w2) ↦→ (w0w2 + w2
1 + 16w2
2 : w0w1 + w1w2). Composing the natural inclusion
E ֒→ P2\{(1 : 0 : 0), (−16 : 0 : 1), (−1 : ±√
15i : 1)} with it, we get a morphism
γ : E → P1, which is a dominant morphism of degree 6. The dominant morphism γ maps
E(K) to {∞} = {(1 : 0)}, and maps (0 : ±4i : 1) to 0 := (0 : 1). By Bézout’s Theorem
[Har97, Chapter I. Corollary 7.8] and calculation, the branch locus of γ is contained in
P1\{∞}. Let (u0 : 1) ∈ P1 be a branch point of γ. For ﬁxed u0, we use Jacobian criterion
for the intersection of two curves E and w0w2 + w2
1 + 16w2
2 = (w0w1 + w1w2)u0 in P2. For
the point (0 : 1 : 0) ∈ P2 is not in this intersection, we let w2 = 1 to dehomogenize these
two curves. By Jacobian criterion, the branch locus satisﬁes the following equations:




w2
1 = w3
0 − 16
w2
1 + w0 + 16 = w1(w0 + 1)u0
3(2w1 − w0u0 − u0)w2
0 + 2w1(1 − w1u0) = 0.

Then the branch locus equals
{(u0 : 1)
∣
∣u12
0 + 60627u10
0
4913 + 159828u8
0
4913 − 3505917u6
0
19652 − 42057961u4
0
58956 + 76076u2
0
14739 − 4112
132651 = 0} .

Let (u0 : 1) be a branch point, then the degree [Q(u0) : Q] = 12.

5.2. An explicit unconditional example for Theorem 4.1.7. For K = Q and L =
Q(i), in this subsection, we will construct a smooth, projective, and geometrically connected
surface having properties of Theorem 4.1.7.

5.2.1. Construction of a smooth, projective, and geometrically connected surface. We will
construct a smooth, projective, and geometrically connected surface X as in Theorem 4.1.7.
Let (u0 : u1) × (x0 : x1 : x2) be the coordinates of P1 × P2, and let s′ = u0(x
2
0 + x
2
1 − x
2
2) +
u1(x
2
0 − x
2
1) ∈ Γ(P1 × P2, O(1, 2)). The locus X ′ deﬁned by s′ = 0 in P1 × P2 is smooth.
Let R be the locus over which the composition X ′ ֒→ P1 × P2 pr1
→ P1 is not smooth. By
calculation, the locus R = {(0 : 1), (±1 : 1)}. Let B = E × P2, and let (γ, id) : B → P1 × P2.
Let L = (γ, id)
∗O(1, 2), and let s = (γ, id)
∗(s′) ∈ Γ(B, L). Let X be the zero locus of s in
B. For the locus R does not intersect with the branch locus of γ : E → P1, the surface X
is smooth. So it is smooth, projective, and geometrically connected. By our construction,
the surface X is deﬁned by the following equations:
{(w0w2 + w2
1 + 16w2
2)(x
2
0 + x
2
1 − x
2
2) + (w0w1 + w1w2)(x
2
0 − x
2
1) = 0
w2
1w2 = w3
0 − 16w3
2

NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR SURFACES 15

in P2 × P2 with bi-homogeneous coordinates (w0 : w1 : w2) × (x0 : x1 : x2). For this surface
X, we have the following proposition.

Proposition 5.2.1. For K = Q and L = Q(i), the smooth, projective, and geometrically
connected surface X has the following properties.

• The surface X has a K-rational point, and satisﬁes weak approximation with
Brauer-Manin obstruction oﬀ ∞K.
• The surface XL does not satisfy weak approximation with Brauer-Manin obstruc-
tion oﬀ T for any ﬁnite subset T ⊂ ΩL.

Proof. This is the same as in the proof of Theorem 4.1.7. □

5.3. An explicit unconditional example for Theorem 4.2.9. For K = Q and L =
Q(i), in this subsection, we will construct a smooth, projective, and geometrically connected
surface having properties of Theorem 4.2.9.

5.3.1. Construction of a smooth, projective, and geometrically connected surface. We choose
odd prime elements (p1, p2, p3, p4, p5, p6) = (17, 13, 53, 41, 3, 13) as in Example 4.2.8. Then
they satisﬁes all chosen conditions of Subsubsections 4.2.2 and 4.2.3. Let f (x0, x1; y0, y1) =
(x
2
0 − 17x
2
1)(x
2
0 − 13x
2
1)(x
2
0 − 221x
2
1)(y2
0 − 53y2
1)(y3
0 − 53y3
1) and g(x0, x1; y0, y1) = (x
2
0 −
41x
2
1)(x
2
0 − 3x
2
1)(x
2
0 − 123x
2
1)(y2
0 − 13y2
1)(y3
0 − 41y3
1) be two bi-homogeneous polynomials.
Let Z f and Z g be the zero loci of f and g respectively in P1 × P1 with bi-homogeneous
coordinates (x0 : x1) × (y0 : y1). Let (u0 : u1) × (x0 : x1) × (y0 : y1) be the coordinates of
P1 ×P1 ×P1, and let s′ = u0g(x0, x1; y0, y1)+u1f (x0, x1; y0, y1) ∈ Γ(P1 ×P1 ×P1, O(1, 6, 5)).
The locus X ′ deﬁned by s′ = 0 in P1 × P1 × P1 is smooth. Let R be the locus over which
the composition X ′ ֒→ P1 × P1 × P1 pr1
→ P1 is not smooth. It is ﬁnite over Q. We can
use computer to calculate this locus, and we give the calculation in Appendix 6. Let
B = E × P1 × P1, and let (γ, id) : B → P1 × P1 × P1. Let L = (γ, id)
∗O(1, 6, 5), and let
s = (γ, id)
∗(s′) ∈ Γ(B, L). Let X be the zero locus of s in B. For the locus R does not
intersect with the branch locus of γ : E → P1, the surface X is smooth. So it is smooth,
projective, and geometrically connected. By our construction, the surface X is deﬁned by
the following two equations:




(w0w2 + w2
1 + 16w2
2)(x
2
0 − 41x
2
1)(x
2
0 − 3x
2
1)(x
2
0 − 123x
2
1)(y2
0 − 13y2
1)(y3
0 − 41y3
1)
+(w0w1 + w1w2)(x
2
0 − 17x
2
1)(x
2
0 − 13x
2
1)(x
2
0 − 221x
2
1)(y2
0 − 53y2
1)(y3
0 − 53y3
1) = 0
w2
1w2 = w3
0 − 16w3
2

in P2 × P1 × P1 with tri-homogeneous coordinates (w0 : w1 : w2) × (x0 : x1) × (y0 : y1). For
this surface X, we have the following proposition.

Proposition 5.3.1. For K = Q and L = Q(i), the smooth, projective, and geometrically
connected surface X has the following properties.

• The surface X is a counterexample to the Hasse principle, and its failure of the
Hasse principle is explained by the Brauer-Manin obstruction.
• The surface XL is a counterexample to the Hasse principle, but its failure of the
Hasse principle cannot be explained by the Brauer-Manin obstruction.

Proof. This is the same as in the proof of Theorem 4.2.9. □

6. Appendix

6.1. The locus R in Example 5.3. Let f (x0, x1; y0, y1) = (x
2
0 − 17x
2
1)(x
2
0 − 13x
2
1)(x
2
0 −
221x
2
1)(y2
0 − 53y2
1)(y3
0 − 53y3
1) and g(x0, x1; y0, y1) = (x
2
0 − 41x
2
1)(x
2
0 − 3x
2
1)(x
2
0 − 123x
2
1)(y2
0 −
13y2
1)(y3
0 − 41y3
1) be two bi-homogeneous polynomials. Let X ′ be the locus deﬁned by
u0g(x0, x1; y0, y1)+u1f (x0, x1; y0, y1) = 0 in P1 ×P1 ×P1 with tri-homogeneous coordinates
(u0 : u1) × (x0 : x1) × (y0 : y1). Let R be the locus over which the composition X ′ ֒→
P1 × P1 × P1 pr1
→ P1 is not smooth. We will calculate this ﬁnite locus R. For Z f and Z g are

16 HAN WU

curves with singularity, we have {(0 : 1), (1 : 0)} ⊂ R. Next, let u1 = 1. We consider aﬃne
pieces of X ′.

Let x1 = 1 and y1 = 1. Then this gives an aﬃne piece of X ′ by u0g(x0, 1; y0, 1) +
f (x0, 1; y0, 1) = 0 in A3 with aﬃne coordinates (u0, x0, y0). For ﬁxed u0, we use Jacobian
criterion to calculate the singularity. Then u0 satisﬁes the following equations:




u0g(x0, 1; y0, 1) + f (x0, 1; y0, 1) = 0
u0 ∂g(x0,1;y0,1)
∂x0 + ∂f (x0,1;y0,1)
∂x0 = 0
u0 ∂g(x0,1;y0,1)
∂y0 + ∂f (x0,1;y0,1)
∂y0 = 0.

Using computer to calculate, we have u0 = 0, or −10553413/620289 or satisﬁes one of the
following three equations:

u4
0 + 442306822591
11644065108 u3
0 + 15378563320976329
38789291891025 u2
0 + 8833702498605138892
6891564192638775 u0 + 1151555233848533056
7244977740979225 = 0,

u6
0− 795599865190
1146914361 u5
0− 852352831544631911
52055002102707 u4
0+ 304535075034759072450076
2362620380435562609 u3
0+ 23484429357868605046160829719
3971564859512180745729 u2
0+
8311232379540782587276725670120990
180257414278679347506402123 u0 + 959341731692466689320791603186246739997
8181343261866419545273073156601 = 0,

u24
0 − 1282484299432205
828072168642 u23
0 + 3122323546639431087642188987593
5017342803508279669201200 u22
0 −
9220867294873355192932709492986698418282151
152002022053223167005295465603491600 u21
0 −
30999681746654846295693028728045879521729132080169271161
7580165253814008879739256663670726076436640000 u20
0 −
45212516638352229837933187085366694204283058079529344651463540951
2235578160515817023818667222976763042314131108360640000 u19
0 +
18075149338451367526195790572251308674104245881489906934937358864775825826797
7325858627130126160176176715795586051349128034014867346496000000 u18
0 +
1929728458747328554854199670272434548177432513569626746401857766397194600755599
37545025464041896570902905668452378513164281174326195150792000000 u17
0 +
10813082002346392222114449555829223571485436674784220052152543359916740809425000843
57725476650964415977763217465245531963990082305526525044342700000000 u16
0 −
4276548928854862536400602684047575693721206178955942137599822672373098084587625072121
887529203508577895658109468528150053946347515447470322556769012500000 u15
0 −
108138440749666040998151800754157496874442091422159386570663670108546710511792028190429
1849019173976203949287728059433645945721557323848896505326602109375000 u14
0 −
212274800596274205751056409361280330744666951660783687161854079450560419076576526369
2150022295321167382892707045853076681071578283545228494565816406250 u13
0 +
40608008582318322879285505067991388627920915662962695473224278401472213071209607698108369
17334554756026912024572450557190430741139599911083404737436894775390625 u12
0 +
20176896364376034775914854511315952401902515577025172947699198733258383180655210587584504
1155636983735127468304830037146028716075973327405560315829126318359375 u11
0 +
158963792583731661630620955844842160301301960511243192646826835314389326180471483775057248
5778184918675637341524150185730143580379866637027801579145631591796875 u10
0 −
1270266243361503789508103099955850762203604422488301533325846718541482312691517964711577728
5778184918675637341524150185730143580379866637027801579145631591796875 u9
0 −
2666552467620466751632153917355955257796687326989260716214069955543289610262819714744442624
1926061639558545780508050061910047860126622212342600526381877197265625 u8
0 −
6882635355470258602823490665258239441168362415110817180409141527410617503796536388374673408
1926061639558545780508050061910047860126622212342600526381877197265625 u7
0 −
9084247577733305667444515416361134105121434380512329964462666543221760153655964901019889664
1926061639558545780508050061910047860126622212342600526381877197265625 u6
0 −
200506323738234616331085970009338835768870364737332320830237673581818041659073075288342528
71335616279946140018816668959631402226911933790466686162291748046875 u5
0 −
7334044106882599637223250735958076270786299935006967560560521012299445936011083944820736
23778538759982046672938889653210467408970644596822228720763916015625 u4
0 +
2816647995777364092376808098177039066661618029531562491562800915395753104512565060304896
71335616279946140018816668959631402226911933790466686162291748046875 u3
0 +
7665757353406683133913491047865070214413497147217395178477629570300922332642644328448
880686620740075802701440357526313607739653503586008471139404296875 u2
0 +
251119825007641874397975890381670516864055856553441761611195723154227892347520155648
528411972444045481620864214515788164643792102151605082683642578125 u0 +
23272944755213194420743946309558908540171345437132830639580649605274861417105719296
2642059862220227408104321072578940823218960510758025413418212890625 = 0.

Let x1 = 1 and y0 = 1. Then this gives an aﬃne piece of X ′ by u0g(x0, 1; 1, y1) +
f (x0, 1; 1, y1) = 0 in A3 with aﬃne coordinates (u0, x0, y1). For ﬁxed u0, we use Jacobian
criterion to calculate the singularity. Then u0 satisﬁes the following equations:




u0g(x0, 1; 1, y1) + f (x0, 1; 1, y1) = 0
u0 ∂g(x0,1;1,y1)
∂x0 + ∂f (x0,1;1,y1)
∂x0 = 0
u0 ∂g(x0,1;1,y1)
∂y1 + ∂f (x0,1;1,y1)
∂y1 = 0.

Using computer to calculate, we have u0 = 0, or −48841/15129 or satisﬁes one of the
following three equations:

u4
0 + 157460599
21846276 u3
0 + 1949002009
136539225 u2
0 + 398554348
45513075 u+
0 3125824
15171025 = 0,

u6
0− 795599865190
1146914361 u5
0− 852352831544631911
52055002102707 u4
0+ 304535075034759072450076
2362620380435562609 u3
0+ 23484429357868605046160829719
3971564859512180745729 u2
0+
8311232379540782587276725670120990
180257414278679347506402123 u+
0 959341731692466689320791603186246739997
8181343261866419545273073156601 = 0,

NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR SURFACES 17

u24
0 − 1282484299432205
828072168642 u23
0 + 3122323546639431087642188987593
5017342803508279669201200 u22
0 −
9220867294873355192932709492986698418282151
152002022053223167005295465603491600 u21
0 −
30999681746654846295693028728045879521729132080169271161
7580165253814008879739256663670726076436640000 u20
0 −
45212516638352229837933187085366694204283058079529344651463540951
2235578160515817023818667222976763042314131108360640000 u19
0 +
18075149338451367526195790572251308674104245881489906934937358864775825826797
7325858627130126160176176715795586051349128034014867346496000000 u18
0 +
1929728458747328554854199670272434548177432513569626746401857766397194600755599
37545025464041896570902905668452378513164281174326195150792000000 u17
0 +
10813082002346392222114449555829223571485436674784220052152543359916740809425000843
57725476650964415977763217465245531963990082305526525044342700000000 u16
0 −
4276548928854862536400602684047575693721206178955942137599822672373098084587625072121
887529203508577895658109468528150053946347515447470322556769012500000 u15
0 −
108138440749666040998151800754157496874442091422159386570663670108546710511792028190429
1849019173976203949287728059433645945721557323848896505326602109375000 u14
0 −
212274800596274205751056409361280330744666951660783687161854079450560419076576526369
2150022295321167382892707045853076681071578283545228494565816406250 u13
0 +
40608008582318322879285505067991388627920915662962695473224278401472213071209607698108369
17334554756026912024572450557190430741139599911083404737436894775390625 u12
0 +
20176896364376034775914854511315952401902515577025172947699198733258383180655210587584504
1155636983735127468304830037146028716075973327405560315829126318359375 u11
0 +
158963792583731661630620955844842160301301960511243192646826835314389326180471483775057248
5778184918675637341524150185730143580379866637027801579145631591796875 u10
0 −
1270266243361503789508103099955850762203604422488301533325846718541482312691517964711577728
5778184918675637341524150185730143580379866637027801579145631591796875 u9
0 −
2666552467620466751632153917355955257796687326989260716214069955543289610262819714744442624
1926061639558545780508050061910047860126622212342600526381877197265625 u8
0 −
6882635355470258602823490665258239441168362415110817180409141527410617503796536388374673408
1926061639558545780508050061910047860126622212342600526381877197265625 u7
0 −
9084247577733305667444515416361134105121434380512329964462666543221760153655964901019889664
1926061639558545780508050061910047860126622212342600526381877197265625 u6
0 −
200506323738234616331085970009338835768870364737332320830237673581818041659073075288342528
71335616279946140018816668959631402226911933790466686162291748046875 u5
0 −
7334044106882599637223250735958076270786299935006967560560521012299445936011083944820736
23778538759982046672938889653210467408970644596822228720763916015625 u4
0 +
2816647995777364092376808098177039066661618029531562491562800915395753104512565060304896
71335616279946140018816668959631402226911933790466686162291748046875 u3
0 +
7665757353406683133913491047865070214413497147217395178477629570300922332642644328448
880686620740075802701440357526313607739653503586008471139404296875 u2
0 +
251119825007641874397975890381670516864055856553441761611195723154227892347520155648
528411972444045481620864214515788164643792102151605082683642578125 u0 +
23272944755213194420743946309558908540171345437132830639580649605274861417105719296
2642059862220227408104321072578940823218960510758025413418212890625 = 0.

Let x0 = 1 and y1 = 1. Then this gives an aﬃne piece of X ′ by u0g(1, x1; y0, 1) +
f (1, x1; y0, 1) = 0 in A3 with aﬃne coordinates (u0, x1, y0). For ﬁxed u0, we use Jacobian
criterion to calculate the singularity. Then u0 satisﬁes the following equations:




u0g(1, x1; y0, 1) + f (1, x1; y0, 1) = 0
u0 ∂g(1,x1;y0,1)
∂x1 + ∂f (1,x1;y0,1)
∂x1 = 0
u0 ∂g(1,x1;y0,1)
∂y0 + ∂f (1,x1;y0,1)
∂y0 = 0.

Using computer to calculate, we have u0 = 0, or −2809/533 or satisﬁes one of the following
three equations:

u4
0 + 442306822591
11644065108 u3
0 + 15378563320976329
38789291891025 u2
0 + 8833702498605138892
6891564192638775 u+
0 1151555233848533056
7244977740979225 = 0,

u6
0 − 16289590
75809 u5
0 − 357314231
227427 u4
0 + 2613868156
682281 u3
0 + 4127069879
75809 u2
0 + 29904922990
227427 u+
0 70675038317
682281 = 0,

u24
0 − 1282484299432205
828072168642 u23
0 + 3122323546639431087642188987593
5017342803508279669201200 u22
0 −
9220867294873355192932709492986698418282151
152002022053223167005295465603491600 u21
0 −
30999681746654846295693028728045879521729132080169271161
7580165253814008879739256663670726076436640000 u20
0 −
45212516638352229837933187085366694204283058079529344651463540951
2235578160515817023818667222976763042314131108360640000 u19
0 +
18075149338451367526195790572251308674104245881489906934937358864775825826797
7325858627130126160176176715795586051349128034014867346496000000 u18
0 +
1929728458747328554854199670272434548177432513569626746401857766397194600755599
37545025464041896570902905668452378513164281174326195150792000000 u17
0 +
10813082002346392222114449555829223571485436674784220052152543359916740809425000843
57725476650964415977763217465245531963990082305526525044342700000000 u16
0 −
4276548928854862536400602684047575693721206178955942137599822672373098084587625072121
887529203508577895658109468528150053946347515447470322556769012500000 u15
0 −
108138440749666040998151800754157496874442091422159386570663670108546710511792028190429
1849019173976203949287728059433645945721557323848896505326602109375000 u14
0 −
212274800596274205751056409361280330744666951660783687161854079450560419076576526369
2150022295321167382892707045853076681071578283545228494565816406250 u13
0 +
40608008582318322879285505067991388627920915662962695473224278401472213071209607698108369
17334554756026912024572450557190430741139599911083404737436894775390625 u12
0 +
20176896364376034775914854511315952401902515577025172947699198733258383180655210587584504
1155636983735127468304830037146028716075973327405560315829126318359375 u11
0 +
158963792583731661630620955844842160301301960511243192646826835314389326180471483775057248
5778184918675637341524150185730143580379866637027801579145631591796875 u10
0 −
1270266243361503789508103099955850762203604422488301533325846718541482312691517964711577728
5778184918675637341524150185730143580379866637027801579145631591796875 u9
0 −
2666552467620466751632153917355955257796687326989260716214069955543289610262819714744442624
1926061639558545780508050061910047860126622212342600526381877197265625 u8
0 −
6882635355470258602823490665258239441168362415110817180409141527410617503796536388374673408
1926061639558545780508050061910047860126622212342600526381877197265625 u7
0 −
9084247577733305667444515416361134105121434380512329964462666543221760153655964901019889664
1926061639558545780508050061910047860126622212342600526381877197265625 u6
0 −

18 HAN WU

200506323738234616331085970009338835768870364737332320830237673581818041659073075288342528
71335616279946140018816668959631402226911933790466686162291748046875 u5
0 −
7334044106882599637223250735958076270786299935006967560560521012299445936011083944820736
23778538759982046672938889653210467408970644596822228720763916015625 u4
0 +
2816647995777364092376808098177039066661618029531562491562800915395753104512565060304896
71335616279946140018816668959631402226911933790466686162291748046875 u3
0 +
7665757353406683133913491047865070214413497147217395178477629570300922332642644328448
880686620740075802701440357526313607739653503586008471139404296875 u2
0 +
251119825007641874397975890381670516864055856553441761611195723154227892347520155648
528411972444045481620864214515788164643792102151605082683642578125 u0 +
23272944755213194420743946309558908540171345437132830639580649605274861417105719296
2642059862220227408104321072578940823218960510758025413418212890625 = 0.

Let x0 = 1 and y0 = 1. Then this gives an aﬃne piece of X ′ by u0g(1, x1; 1, y1) +
f (1, x1; 1, y1) = 0 in A3 with aﬃne coordinates (u0, x1, y1). For ﬁxed u0, we use Jacobian
criterion to calculate the singularity. Then u0 satisﬁes the following equations:





u0g(1, x1; 1, y1) + f (1, x1; 1, y1) = 0
u0 ∂g(1,x1;1,y1)
∂x1 + ∂f (1,x1;1,y1)
∂x1 = 0
u0 ∂g(1,x1;1,y1)
∂y1 + ∂f (1,x1;1,y1)
∂y1 = 0.

Using computer to calculate, we have u0 = 0, or −1 or satisﬁes one of the following three
equations:

u4
0 + 157460599
21846276 u3
0 + 1949002009
136539225 u2
0 + 398554348
45513075 u+
0 3125824
15171025 = 0,

u6
0 − 16289590
75809 u5
0 − 357314231
227427 u4
0 + 2613868156
682281 u3
0 + 4127069879
75809 u2
0 + 29904922990
227427 u+
0 70675038317
682281 = 0,

u24
0 − 1282484299432205
828072168642 u23
0 + 3122323546639431087642188987593
5017342803508279669201200 u22
0 −
9220867294873355192932709492986698418282151
152002022053223167005295465603491600 u21
0 −
30999681746654846295693028728045879521729132080169271161
7580165253814008879739256663670726076436640000 u20
0 −
45212516638352229837933187085366694204283058079529344651463540951
2235578160515817023818667222976763042314131108360640000 u19
0 +
18075149338451367526195790572251308674104245881489906934937358864775825826797
7325858627130126160176176715795586051349128034014867346496000000 u18
0 +
1929728458747328554854199670272434548177432513569626746401857766397194600755599
37545025464041896570902905668452378513164281174326195150792000000 u17
0 +
10813082002346392222114449555829223571485436674784220052152543359916740809425000843
57725476650964415977763217465245531963990082305526525044342700000000 u16
0 −
4276548928854862536400602684047575693721206178955942137599822672373098084587625072121
887529203508577895658109468528150053946347515447470322556769012500000 u15
0 −
108138440749666040998151800754157496874442091422159386570663670108546710511792028190429
1849019173976203949287728059433645945721557323848896505326602109375000 u14
0 −
212274800596274205751056409361280330744666951660783687161854079450560419076576526369
2150022295321167382892707045853076681071578283545228494565816406250 u13
0 +
40608008582318322879285505067991388627920915662962695473224278401472213071209607698108369
17334554756026912024572450557190430741139599911083404737436894775390625 u12
0 +
20176896364376034775914854511315952401902515577025172947699198733258383180655210587584504
1155636983735127468304830037146028716075973327405560315829126318359375 u11
0 +
158963792583731661630620955844842160301301960511243192646826835314389326180471483775057248
5778184918675637341524150185730143580379866637027801579145631591796875 u10
0 −
1270266243361503789508103099955850762203604422488301533325846718541482312691517964711577728
5778184918675637341524150185730143580379866637027801579145631591796875 u9
0 −
2666552467620466751632153917355955257796687326989260716214069955543289610262819714744442624
1926061639558545780508050061910047860126622212342600526381877197265625 u8
0 −
6882635355470258602823490665258239441168362415110817180409141527410617503796536388374673408
1926061639558545780508050061910047860126622212342600526381877197265625 u7
0 −
9084247577733305667444515416361134105121434380512329964462666543221760153655964901019889664
1926061639558545780508050061910047860126622212342600526381877197265625 u6
0 −
200506323738234616331085970009338835768870364737332320830237673581818041659073075288342528
71335616279946140018816668959631402226911933790466686162291748046875 u5
0 −
7334044106882599637223250735958076270786299935006967560560521012299445936011083944820736
23778538759982046672938889653210467408970644596822228720763916015625 u4
0 +
2816647995777364092376808098177039066661618029531562491562800915395753104512565060304896
71335616279946140018816668959631402226911933790466686162291748046875 u3
0 +
7665757353406683133913491047865070214413497147217395178477629570300922332642644328448
880686620740075802701440357526313607739653503586008471139404296875 u2
0 +
251119825007641874397975890381670516864055856553441761611195723154227892347520155648
528411972444045481620864214515788164643792102151605082683642578125 u0 +
23272944755213194420743946309558908540171345437132830639580649605274861417105719296
2642059862220227408104321072578940823218960510758025413418212890625 = 0.

In summary, the locus R = {(0 : 1), (1 : 0), (−10553413 : 620289), (−48841 : 15129), (−2809 :
533), (−1 : 1)} ∪ {(u0 : 1)|u0 satisﬁes one of the following ﬁve equations }.

u4
0 + 442306822591
11644065108 u3
0 + 15378563320976329
38789291891025 u2
0 + 8833702498605138892
6891564192638775 u0 + 1151555233848533056
7244977740979225 = 0,

u4
0 + 157460599
21846276 u3
0 + 1949002009
136539225 u2
0 + 398554348
45513075 u+
0 3125824
15171025 = 0,

u6
0− 795599865190
1146914361 u5
0− 852352831544631911
52055002102707 u4
0+ 304535075034759072450076
2362620380435562609 u3
0+ 23484429357868605046160829719
3971564859512180745729 u2
0+
8311232379540782587276725670120990
180257414278679347506402123 u0 + 959341731692466689320791603186246739997
8181343261866419545273073156601 = 0,

u6
0 − 16289590
75809 u5
0 − 357314231
227427 u4
0 + 2613868156
682281 u3
0 + 4127069879
75809 u2
0 + 29904922990
227427 u+
0 70675038317
682281 = 0,

NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR SURFACES 19

u24
0 − 1282484299432205
828072168642 u23
0 + 3122323546639431087642188987593
5017342803508279669201200 u22
0 −
9220867294873355192932709492986698418282151
152002022053223167005295465603491600 u21
0 −
30999681746654846295693028728045879521729132080169271161
7580165253814008879739256663670726076436640000 u20
0 −
45212516638352229837933187085366694204283058079529344651463540951
2235578160515817023818667222976763042314131108360640000 u19
0 +
18075149338451367526195790572251308674104245881489906934937358864775825826797
7325858627130126160176176715795586051349128034014867346496000000 u18
0 +
1929728458747328554854199670272434548177432513569626746401857766397194600755599
37545025464041896570902905668452378513164281174326195150792000000 u17
0 +
10813082002346392222114449555829223571485436674784220052152543359916740809425000843
57725476650964415977763217465245531963990082305526525044342700000000 u16
0 −
4276548928854862536400602684047575693721206178955942137599822672373098084587625072121
887529203508577895658109468528150053946347515447470322556769012500000 u15
0 −
108138440749666040998151800754157496874442091422159386570663670108546710511792028190429
1849019173976203949287728059433645945721557323848896505326602109375000 u14
0 −
212274800596274205751056409361280330744666951660783687161854079450560419076576526369
2150022295321167382892707045853076681071578283545228494565816406250 u13
0 +
40608008582318322879285505067991388627920915662962695473224278401472213071209607698108369
17334554756026912024572450557190430741139599911083404737436894775390625 u12
0 +
20176896364376034775914854511315952401902515577025172947699198733258383180655210587584504
1155636983735127468304830037146028716075973327405560315829126318359375 u11
0 +
158963792583731661630620955844842160301301960511243192646826835314389326180471483775057248
5778184918675637341524150185730143580379866637027801579145631591796875 u10
0 −
1270266243361503789508103099955850762203604422488301533325846718541482312691517964711577728
5778184918675637341524150185730143580379866637027801579145631591796875 u9
0 −
2666552467620466751632153917355955257796687326989260716214069955543289610262819714744442624
1926061639558545780508050061910047860126622212342600526381877197265625 u8
0 −
6882635355470258602823490665258239441168362415110817180409141527410617503796536388374673408
1926061639558545780508050061910047860126622212342600526381877197265625 u7
0 −
9084247577733305667444515416361134105121434380512329964462666543221760153655964901019889664
1926061639558545780508050061910047860126622212342600526381877197265625 u6
0 −
200506323738234616331085970009338835768870364737332320830237673581818041659073075288342528
71335616279946140018816668959631402226911933790466686162291748046875 u5
0 −
7334044106882599637223250735958076270786299935006967560560521012299445936011083944820736
23778538759982046672938889653210467408970644596822228720763916015625 u4
0 +
2816647995777364092376808098177039066661618029531562491562800915395753104512565060304896
71335616279946140018816668959631402226911933790466686162291748046875 u3
0 +
7665757353406683133913491047865070214413497147217395178477629570300922332642644328448
880686620740075802701440357526313607739653503586008471139404296875 u2
0 +
251119825007641874397975890381670516864055856553441761611195723154227892347520155648
528411972444045481620864214515788164643792102151605082683642578125 u0 +
23272944755213194420743946309558908540171345437132830639580649605274861417105719296
2642059862220227408104321072578940823218960510758025413418212890625 = 0.

Let (u0 : 1) be a closed point in R, then the degree [Q(u0) : Q] ∈ {1, 4, 6, 24}.

Acknowledgements. The author would like to thank my thesis advisor Y. Liang for proposing the
related problems, papers and many fruitful discussions. This paper was inspired by the work of Harpaz

and Skorobogatov [HS14]. The author was partially supported by NSFC Grant No. 12071448.

References

[Har97] R. Hartshorne, Algebraic geometry, Graduate Texts in Mathematics, vol. 52, Springer-Verlag,
1997. ↑4.1.1, 4.1.1, 4.2.3, 5.1.2
[HS14] Y. Harpaz and A. Skorobogatov, Singular curves and the étale Brauer-Manin obstruction for
surfaces, Ann. Sci. Éc. Norm. Supér. 47 (2014), 765–778. ↑4.1.5, 4.2.6, 6.1
[Lia18] Y. Liang, Non-invariance of weak approximation properties under extension of the ground ﬁeld,
Preprint, arXiv:1805.08851v1 [math.NT] (2018). ↑1.3.1, 4.1
[LW54] S. Lang and A. Weil, Number of points of varieties in ﬁnit ﬁelds, Amer. J. Math. 76 (1954),
819–827. ↑4.1.1
[Man71] Y. Manin, Le groupe de Brauer-Grothendieck en géométrie diophantienne. In: Actes du Congrès
International des Mathématiciens, Vol. 1, Gauthier-Villars, 1971 (French). pp. 401-411. ↑1.1
[Mil80] J. Milne, Étale cohomology, Princeton University Press, 1980. ↑4.1.1
[Neu99] J. Neukirch, Algebraic number theory, Springer-Verlag, 1999. ↑2
[Poo10] B. Poonen, Insuﬃciency of the Brauer-Manin obstruction applied to étale covers, Ann. of Math.
171 (2010), 2157–2169. ↑4.1, 4.2
[Sch99] V. Scharaschkin, Local-global problems and the Brauer-Manin obstruction, Thesis, University of
Michigan (1999). ↑1.1, 3
[Sko01] A. Skorobogatov, Torsors and rational points, Cambridge Tracts in Mathematics, vol. 144, Cam-
bridge University Press, 2001. ↑1.1, 3
[Ste12] W. Stein, Sage for power users, https://www.sagemath.org/, 2012. ↑5.1.1
[Sto07] M. Stoll, Finite descent obstructions and rational points on curves, Algebra Number Theory 1
(2007), 349–391. ↑1.1, 3, 3.0.1
[Wu21] H. Wu, Non-invariance of the Brauer-Manin obstruction for surfaces, Preprint,
arXiv:2103.01784v2 [math.NT] (2021). ↑1.3.1, 1.3.2, 3, 3.0.3, 3.0.4, 3, 3, 4.1, 4.1.1, 4.1.1,
4.1.1, 4.2

University of Science and Technology of China, School of Mathematical Sciences, No.96,
JinZhai Road, Baohe District, Hefei, Anhui, 230026. P.R.China.

Email address: wuhan90@mail.ustc.edu.cn
