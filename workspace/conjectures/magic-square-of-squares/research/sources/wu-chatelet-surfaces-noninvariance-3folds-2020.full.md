<!-- source: https://arxiv.org/pdf/2010.04919 | converted from PDF -->

arXiv:2010.04919v2  [math.NT]  18 Feb 2021
CHÂTELET SURFACES AND NON-INVARIANCE OF THE
BRAUER-MANIN OBSTRUCTION FOR 3-FOLDS

HAN WU

Abstract. In this paper, we construct three kinds of Châtelet surfaces, which have
some given arithmetic properties with respect to ﬁeld extensions of number ﬁelds. We
then use these constructions to study the properties of weak approximation with Brauer-
Manin obstruction and the Hasse principle with Brauer-Manin obstruction for 3-folds,
which are pencils of Châtelet surfaces parameterized by a curve, with respect to ﬁeld
extensions of number ﬁelds. We give general constructions (conditional on a conjecture
of M. Stoll) to negatively answer some questions, and illustrate these constructions and
some exceptions with some explicit unconditional examples.

1. Introduction

1.1. Background. Let X be a proper algebraic variety deﬁned over a number ﬁeld K.
Let ΩK be the set of all nontrivial places of K. Let ∞K ⊂ ΩK be the subset of all
archimedean places, and let S ⊂ ΩK be a ﬁnite subset. Let Kv be the completion of K
at v ∈ ΩK. Let AK be the ring of adèles of K. If the set of K-rational points X(K) ̸= ∅,
then the set of adelic points X(AK) ̸= ∅. The converse is known as the Hasse principle.
We say that X is a counterexample to the Hasse principle if X(AK) ̸= ∅ whereas X(K) = ∅.
A well know counterexample to the Hasse principle is Selmer’s cubic curve deﬁned over
Q by 3w3
0 + 4w3
1 + 5w3
2 = 0 with homogeneous coordinates (w0 : w1 : w2) ∈ P2. Let
prS : AK → AS
K be the natural projection of the ring of adèles and adèles without S
components, which induces a natural projection prS : X(AK) → X(AS
K) if X(AK) ̸= ∅.
For X is proper, the set of adelic points X(AS
K) is equal to ∏
v∈ΩK \S X(Kv), and the adelic
topology of X(AS
K) is indeed the product topology of v-adic topologies. Viewing X(K)
as a subset of X(AK) (respectively of X(AS
K)) by the diagonal embedding, we say that
X satisﬁes weak approximation (respectively weak approximation oﬀ S) if X(K) is dense
in X(AK) (respectively in X(AS
K)), cf. [Sko01, Chapter 5.1]. Cohomological obstructions
have been used to explain failures of the Hasse principle and nondensity of X(K) in X(AS
K).
Let Br(X) = H 2
ét(X, Gm) be the Brauer group of X. The Brauer-Manin pairing

X(AK) × Br(X) → Q/Z,

suggested by Brauer-Manin [Man71], between X(AK) and Br(X), is provided by local class
ﬁeld theory. The left kernel of this pairing is denoted by X(AK)
Br, which is a closed subset
of X(AK). By the global reciprocity in class ﬁeld theory, there is an exact sequence:

0 → Br(K) → ⊕

v∈ΩK Br(Kv) → Q/Z → 0.

It induces an inclusion: X(K) ⊂ prS(X(AK)
Br). We say that the failure of the Hasse prin-
ciple of X is explained by the Brauer-Manin obstruction if X(AK) ̸= ∅ and X(AK)
Br = ∅.
For the failure of the Hasse principle of a smooth, projective, and geometrically connected
curve over K, if the Tate-Shafarevich group and the rational points set of its Jacobian are
ﬁnite, then this failure can be explained by the Brauer-Manin obstruction, cf. [Sch99].
A counterexample to the Hasse principle such that its failure of the Hasse principle is

2020 Mathematics Subject Classiﬁcation. 11G35, 14G12, 14G25, 14G05.
Key words and phrases. rational points, Hass principle, weak approximation, Brauer-Manin obstruc-
tion, Châtelet surfaces, Châtelet surface bundles over curves.

1

2 HAN WU

not explained by the Brauer-Manin obstruction, was constructed ﬁrstly by Skoroboga-
tov [Sko99], subsequently by Poonen [Poo10], Harpaz and Skorobogatov [HS14], Colliot-
Thélène, Pál and Skorobogatov [CTPS16] and so on. We say that X satisﬁes weak approx-
imation with Brauer-Manin obstruction (respectively with Brauer-Manin obstruction oﬀ S) if
X(K) is dense in X(AK)
Br (respectively in prS(X(AK)
Br)). For an elliptic curve deﬁned
over Q, if its analytic rank equals one, then this elliptic curve satisﬁes weak approximation
with Brauer-Manin obstruction, cf. [Wan96]. For an abelian variety deﬁned over K, if its
Tate-Shafarevich group is ﬁnite, then this abelian variety satisﬁes weak approximation with
Brauer-Manin obstruction oﬀ ∞K, cf. [Sko01, Proposition 6.2.4]. For any smooth, proper
and rationally connected variety X deﬁned over an number ﬁeld, it is conjectured by J.-L.
Colliot-Thélène that X satisﬁes weak approximation with Brauer-Manin obstruction. The
Colliot-Thélène’s conjecture holds for Châtelet surfaces, cf. [CTSSD87a, CTSSD87b]. For
any smooth, projective, and geometrically connected curve C deﬁned over an number ﬁeld
K, it is conjectured by Stoll [Sto07] that C satisﬁes weak approximation with Brauer-Manin
obstruction oﬀ ∞K : see Conjecture 4.0.1 for more details. Before the Stoll’s conjecture,
if this curve C is a counterexample to the Hasse principle, Skorobogatov [Sko01, Chapter
6.3] asked a weaker open question: is the failure of the Hasse principle of C explained by
the Brauer-Manin obstruction?

1.2. Questions. Given a nontrivial extension of number ﬁelds L/K, and a ﬁnite subset
S ⊂ ΩK, let SL ⊂ ΩL be the subset of all places above S. Let X be a smooth, projective,
and geometrically connected variety deﬁned over K. Let XL = X ×Spec K Spec L be the
base change of X by L. In this paper, we consider the following questions.

Question 1.2.1. If the variety X has a K-rational point, and satisﬁes weak approxima-
tion with Brauer-Manin obstruction oﬀ S, must XL also satisfy weak approximation with
Brauer-Manin obstruction oﬀ SL?

Question 1.2.2. Assume that the varieties X and XL are counterexamples to the Hasse
principle. If the failure of the Hasse principle of X is explained by the Brauer-Manin
obstruction, must the failure of the Hasse principle of XL also be explained by the Brauer-
Manin obstruction?

1.3. Main results for Châtelet surfaces. A Châtelet surface deﬁned over Q, which is
a counterexample to the Hasse principle, was constructed by Iskovskikh [Isk71]. Poonen
[Poo09] generalized it to any given number ﬁeld. For any number ﬁeld K, Liang [Lia18]
constructed a Châtelet surface deﬁned over K, which has a K-rational point and does not
satisfy weak approximation oﬀ ∞K. By using weak approximation and strong approxima-
tion oﬀ all 2-adic places for A1 (cf. Lemma 2.0.1) to choose elements in K, and using
Čebotarev’s density theorem (cf. Theorem 2.0.2) to add some splitting conditions, we
construct three kinds of Châtelet surfaces to generalize their arguments.

Proposition 1.3.1. For any extension of number ﬁelds L/K, and any ﬁnite subset S ⊂
ΩK\{all complex and 2-adic places} splitting completely in L, there exist Châtelet surfaces
V1, V2, V3 deﬁned over K, which have the following properties.

• The subset V1(AS
K) ⊂ V1(ASL
L ) is nonempty, but V1(Kv) = V1(Lv′) = ∅ for all
v ∈ S and all v′ ∈ SL, cf. Proposition 3.1.1.
• The Brauer group Br(V2)/Br(K) ∼= Br(V2L)/Br(L) ∼= Z/2Z, is generated by an
element A ∈ Br(V2). The subset V2(K) ⊂ V2(L) is nonempty.
For any v ∈ S, there exist Pv and Qv in V2(Kv) such that the local invariants
invv(A(Pv)) = 0 and invv(A(Qv)) = 1/2. For any other v /∈ S, and any Pv ∈
V2(Kv), the local invariant invv(A(Pv)) = 0.
For any v′ ∈ SL, there exist Pv′ and Qv′ in V2(Lv′ ) such that the local invariants
invv′ (A(Pv′ )) = 0 and invv′ (A(Qv′ )) = 1/2. For any other v′ /∈ SL, and any
Pv′ ∈ V2(Lv′ ), the local invariant invv′ (A(Pv′ )) = 0, cf. Proposition 3.2.1.
• The Brauer group Br(V3)/Br(K) ∼= Br(V3L)/Br(L) ∼= Z/2Z, is generated by an
element A ∈ Br(V3). The subset V3(AK) ⊂ V3(AL) is nonempty.
For any v ∈ ΩK, and any Pv ∈ V3(Kv), the local invariant invv(A(Pv)) = 0 if

CHÂTELET SURFACES AND NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR 3-FOLDS3

v /∈ S; the local invariant invv(A(Pv)) = 1/2 if v ∈ S.
For any v′ ∈ ΩL, and any Pv′ ∈ V3(Lv′ ), the local invariant invv′ (A(Pv′ )) = 0 if
v′ /∈ SL; the local invariant invv′(A(Pv′ )) = 1/2 if v′ ∈ SL, cf. Proposition 3.3.1.

Combining our construction method with the global reciprocity law, we have the following
results for Châtelet surfaces.

Corollary 1.3.2 (Corollary 3.2.4). For any extension of number ﬁelds L/K, and any ﬁnite
nonempty subset S ⊂ ΩK\{all complex and 2-adic places} splitting completely in L, there
exists a Châtelet surface V deﬁned over K such that V (K) ̸= ∅. For any subﬁeld L′ ⊂ L
over K, the Brauer group Br(V )/Br(K) ∼= Br(VL′)/Br(L′) ∼= Z/2Z. And the surface VL′
has the following properties.

• For any ﬁnite subset T ′ ⊂ ΩL′ such that T ′ ∩ SL′ ̸= ∅, the surface VL′ satisﬁes
weak approximation oﬀ T ′.
• For any ﬁnite subset T ′ ⊂ ΩL′ such that T ′ ∩ SL′ = ∅, the surface VL′ does not
satisfy weak approximation oﬀ T ′. In particular, the surface VL′ does not satisfy
weak approximation.

Corollary 1.3.3 (Corollary 3.3.3). For any extension of number ﬁelds L/K, there exists
a Châtelet surface V deﬁned over K such that V (AK) ̸= ∅. For any subﬁeld L′ ⊂ L over
K, the Brauer group Br(V )/Br(K) ∼= Br(VL′ )/Br(L′) ∼= Z/2Z. And the surface VL′ has
the following properties.

• If the degree [L′ : K] is odd, then the surface VL′ is a counterexample to the Hasse
principle. In particular, the surface V is a counterexample to the Hasse principle.
• If the degree [L′ : K] is even, then the surface VL′ satisﬁes weak approximation.
In particular, in this case, the set V (L′) ̸= ∅.

1.4. Main results for Châtelet surface bundles over curves. We will apply our
results for Châtelet surfaces to construct Châtelet surface bundles over curves to give
negative answers to Questions 1.2.

1.4.1. A negative answer to Question 1.2.1. For any quadratic extension of number ﬁelds
L/K, and assuming the Stoll’s conjecture, a Châtelet surface bundle over a curve was
constructed by Liang[Lia18] to give a negative answer to Question 1.2.1. Also an uncon-
ditional example with explicit equations was given for L = Q(
√
5) and K = Q in loc. cit.
His method only works for quadratic extensions. In this paper, we generalize it to any
nontrivial extension of number ﬁelds.

For any nontrivial extension of number ﬁelds L/K, assuming the Stoll’s conjecture, we
have the following theorem to give a negative answer to Question 1.2.1.

Theorem 1.4.1.1 (Theorem 6.2.1). For any nontrivial extension of number ﬁelds L/K,
and any ﬁnite subset T ⊂ ΩL, assuming the Stoll’s conjecture, there exists a Châtelet
surface bundle over a curve: X → C deﬁned over K such that

• X has a K-rational point, and satisﬁes weak approximation with Brauer-Manin
obstruction oﬀ ∞K,
• XL does not satisfy weak approximation with Brauer-Manin obstruction oﬀ T.

For K = Q and L = Q(
√
3), based on the method given in Theorem 6.2.1, we give an
explicit unconditional example in Subsection 7.1.

1.4.2. Negative answers to Question 1.2.2. To the best knowledge of the author, Question
1.2.2 has not yet been seriously discussed in the literature.

For any number ﬁeld K, and any nontrivial ﬁeld extension L of odd degree over K, assuming
the Stoll’s conjecture, we have the following theorem to give a negative answer to Question
1.2.2.

4 HAN WU

Theorem 1.4.2.1 (Theorem 6.3.1). For any number ﬁeld K, and any nontrivial ﬁeld
extension L of odd degree over K, assuming the Stoll’s conjecture, there exists a Châtelet
surface bundle over a curve: X → C deﬁned over K such that

• X is a counterexample to the Hasse principle, and its failure of the Hasse principle
is explained by the Brauer-Manin obstruction,
• XL is a counterexample to the Hasse principle, but its failure of the Hasse principle
cannot be explained by the Brauer-Manin obstruction.

Let ζ7 be a primitive 7-th root of unity. For K = Q and L = Q(ζ7 + ζ−1
7 ), based on the
method given in Theorem 6.3.1, we give an explicit unconditional example in Subsection 7.2.
The 3-fold X is a smooth compactiﬁcation of the following 3-dimensional aﬃne subvariety
given by equations
{
y2 − 377z2 = 14(x
4 − 89726)y′2 + (x
2 − 878755181)(5x
2 − 4393775906)
y′2 = x
′3 − 343x
′ − 2401

in (x, y, z, x
′, y′) ∈ A5.

For any number ﬁeld K having a real place, and any nontrivial ﬁeld extension L/K having a
real place, assuming the Stoll’s conjecture, we have the following theorem to give a negative
answer to Question 1.2.2.

Theorem 1.4.2.2 (Theorem 6.3.2). For any number ﬁeld K having a real place, and any
nontrivial ﬁeld extension L/K having a real place, assuming the Stoll’s conjecture, there
exists a Châtelet surface bundle over a curve: X → C deﬁned over K such that

• X is a counterexample to the Hasse principle, and its failure of the Hasse principle
is explained by the Brauer-Manin obstruction,
• XL is a counterexample to the Hasse principle, but its failure of the Hasse principle
cannot be explained by the Brauer-Manin obstruction.

For K = Q and L = Q(
√
3), based on the method given in Theorem 6.3.2, we give an ex-
plicit unconditional example in Subsection 7.3. The 3-fold X is a smooth compactiﬁcation
of the following 3-dimensional aﬃne subvariety given by equations
{y2 + 23z2 = 5(x
4 + 805)(x
′ − 4)
2 − 5(x
4 + 115)
y′2 = x
′3 − 16

in (x, y, z, x
′, y′) ∈ A5.

Exceptions 1.4.2.3 (Subsection 7.4). For Question 1.2.2, besides cases of Theorem 6.3.1
and Theorem 6.3.2, there are some exceptions. When the degree [L : K] is even and L
has no real place, we can give some unconditional examples, case by case, to give negative
answers to Question 1.2.2, although we do not have a uniform way to construct them. In
Subsection 7.4, we give an example to explain how it works for the case that K = Q and
L = Q(i). The 3-fold X, is a smooth compactiﬁcation of the following 3-dimensional aﬃne
subvariety given by equations
{y2 + 15z2 = (x
4 − 10x
2 + 15)(y′2 + 32)/8 − (5x
4 − 39x
2 + 75)y′/2
y′2 = x
′3 − 16

in (x, y, z, x
′, y′) ∈ A5.

1.4.3. Main ideas behind our constructions in the proof of theorems. Given a nontrivial
extension of number ﬁelds L/K, we start with a curve C such that C(K) and C(L) are ﬁnite,
nonempty and C(K) ̸= C(L). Using our results for Châtelet surfaces and a construction
method from Poonen [Poo10], we construct a Châtelet surface bundle over this curve:
β : X → C such that the ﬁber of each C(K) point is isomorphic to V∞, and that the
ﬁber of each C(L)\C(K) point is isomorphic to V0. Assuming the Stoll’s conjecture, by
a main proposition from [Poo10, Proposition 5.4] and the functoriality of Brauer-Manin
pairing, the Brauer-Manin sets of X, roughly speaking, is the union of adelic points sets

CHÂTELET SURFACES AND NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR 3-FOLDS5

of rational ﬁbers. Using some ﬁbration arguments, the arithmetic properties of V∞ and V0
will determined the arithmetic properties of X. For Theorem 6.2.1 and 6.3.1, these ideas
will be enough. For Theorems 6.3.2, we choose the curve C with an additional connected
condition at one real place, and make full use of this real place information.

2. Notation and preliminaries

Given a number ﬁeld K, let OK be the ring of its integers, and let ΩK be the set of all its
nontrivial places. Let ∞K ⊂ ΩK be the subset of all archimedean places, and let 2K ⊂ ΩK
be the subset of all 2-adic places. Let ∞
r
K ⊂ ∞K be the subset of all real places, and let
∞
c
K ⊂ ∞K be the subset of all complex places. Let Ωf
K = ΩK\∞K be the set of all ﬁnite
places of K. Let Kv be the completion of K at v ∈ ΩK. For v ∈ ∞K, let τv : K ֒→ Kv be
the embedding of K into its completion. For v ∈ Ωf
K, let OKv be its valuation ring, and let
Fv be its residue ﬁeld. Let S ⊂ ΩK be a ﬁnite subset, and let OS = ⋂

v∈Ω
f
K \S(K ∩ OKv ) be

the ring of S-integers. Let AK, AS
K be the ring of adèles and adèles without S components
of K. A strong approximation theorem [CF67, Chapter II §15] states that K is dense in
AS
K for any nonempty S. In this paper, we only use the following special case:

Lemma 2.0.1. Let K a number ﬁeld. The set K is dense in A2K
K .

In this paper, we always assume that a ﬁeld L is a ﬁnite extension of K. Let SL ⊂ ΩL be
the subset of all places above S.

It is not diﬃcult to generalize [Neu99, Theorem 13.4] to the following version of Čebotarev’s
density theorem.

Theorem 2.0.2 (Čebotarev). Let L/K be an extension of number ﬁelds. Then the set of
places of K splitting completely in L, has positive density.

2.1. Hilbert symbol. We use Hilbert symbol (a, b)v ∈ {±1}, for a, b ∈ K ×
v and v ∈ ΩK.
By deﬁnition, (a, b)v = 1 if and only if x
2
0 − ax
2
1 − bx
2
2 = 0 has a Kv-solution in P2 with
homogeneous coordinates (x0 : x1 : x2), which equivalently means that the curve deﬁned
over Kv by the equation x
2
0 − ax
2
1 − bx
2
2 = 0 in P2, is isomorphic to P1. The Hilbert symbol
gives a symmetric bilinear form on K ×
v /K ×2
v with value in Z/2Z, cf. [Ser79, Chapter XIV,
Proposition 7]. And this bilinear form is nondegenerate, cf. [Ser79, Chapter XIV, Corollary
7].

2.2. Preparation lemmas. We state the following lemmas for later use.

Lemma 2.2.1. Let K be a number ﬁeld, and let v be an odd place of K. Let a, b ∈ K ×
v
such that v(a), v(b) are even. Then (a, b)v = 1.

Proof. Choose a prime element πv ∈ Kv. Let a1 = aπ−v(a)
v and b1 = bπ−v(b)
v . Since the
valuations v(a) and v(b) are even, the elements π−v(a)
v and π−v(b)
v are in K ×2
v . So (a, b)v =
(a1, b1)v and a1, b1 ∈ O×
Kv . By Chevalley-Warning theorem (cf. [Ser73, Chapter I §2,
Corollary 2]), the equation x
2
0 − ¯a1x
2
1 − ¯b1x
2
2 = 0 has a nontrivial solution in Fv. For v is
odd, by Hensel’s lemma, this solution can be lifted to a nontrivial solution in OKv . Hence
(a, b)v = (a1, b1)v = 1. □

Lemma 2.2.2. Let K be a number ﬁeld, and let v be an odd place of K. Let a, b, c ∈ K ×
v
such that v(b) < v(c). Then (a, b + c)v = (a, b)v.

Proof. For v(b) < v(c), we have v(b−1c) > 0. By Hensel’s lemma, we have 1 + b−1c ∈ K ×2
v .
So (a, b + c)v = (a, b(1 + b−1c))v = (a, b)v. □

Lemma 2.2.3. Let K be a number ﬁeld, and let v ∈ ΩK. Then K ×2
v is an open subgroup
of K ×
v . If v ∈ Ωf
K, then O×
Kv is also an open subgroup of K ×
v . So, they are nonempty open
subset of Kv.

6 HAN WU

Proof. It is obvious for v ∈ ∞K. Consider v ∈ Ωf
K. Let p be the prime number such that
v|p in K. Then by Hensel’s lemma, the group K ×2
v ∩ O×
Kv contains the set 1 + p3OKv , which
is an open subgroup of K ×
v . Hence K ×2
v and O×
Kv are open subgroups of K ×
v . □

Lemma 2.2.4. Let K be a number ﬁeld, and let v ∈ Ωf
K. For any n ∈ Z, the set {x ∈
Kv|v(x) = n} is a nonempty open subset of Kv.

Proof. By Lemma 2.2.3, the set O×
Kv is an open subgroup of K ×
v . Choose a prime element
πv ∈ Kv. Then the set {x ∈ K ×
v |v(x) = n} = πn
v O×
Kv , so it is a nonempty open subset of
Kv. □

Lemma 2.2.5. Let K be a number ﬁeld, and let v ∈ Ωf
K. For any a ∈ K ×
v , the sets
{x ∈ K ×
v |(a, x)v = 1}, {x ∈ K ×
v |(a, x)v = 1} ∩ OKv and {x ∈ O×
Kv |(a, x)v = 1} are
nonempty open subsets of Kv.

Proof. For the unit 1 belongs to these sets, they are nonempty. By Lemma 2.2.3, the sets
K ×2
v and O×
Kv are nonempty open subsets of Kv. The set {x ∈ K ×
v |(a, x)v = 1} is a union
of cosets of K ×2
v in the group K ×
v . So the sets are open in Kv. □

Lemma 2.2.6. Let K be a number ﬁeld, and let v ∈ Ωf
K. For any a ∈ K ×
v , the sets
{x ∈ K ×
v |(a, x)v = −1} and {x ∈ K ×
v |(a, x)v = −1} ∩ OKv are open subsets of Kv.
Furthermore, if a /∈ K ×2
v , then they are nonempty.

Proof. If the set {x ∈ K ×
v |(a, x)v = −1} ̸= ∅, then it is a union of cosets of K ×2
v in the
group K ×
v . By Lemma 2.2.3, it is an open subset of Kv. For OKv is open in Kv, the sets are
open subsets of K ×
v . Nonemptiness is from the nondegeneracy of the bilinear form given
by the Hilbert symbol, and from multiplying a square element in OKv to denominate an
element in K ×
v . □

Lemma 2.2.7. Let K be a number ﬁeld, and let v ∈ Ωf
K. For any a ∈ K ×
v with v(a) odd,
the set {x ∈ O×
Kv |(a, x)v = −1} is a nonempty open subset of Kv.

Proof. By Lemmas 2.2.3 and 2.2.6, the set is open in Kv. We need to show that it is
nonempty. For a /∈ K 2
v , by the nondegeneracy of the bilinear form given by the Hilbert
symbol, there exists an element b ∈ K ×
v such that (a, b)v = −1. If v(b) is odd, let b′ = −ab.
Then (a, b′)v = (a, −ab)v = (a, −a)v(a, b)v = −1. Replacing b by b′ if necessary, we can
assume that v(b) is even. Choose a prime element πv ∈ Kv. Then π−v(b)
v ∈ K ×2
v , so the
element bπ−v(b)
v is in this set. □

Lemma 2.2.8. Let L/K be an extension of number ﬁelds, and let v ∈ ΩK\∞
c
K. We
assume that v′ ∈ ΩL splits over v, i.e. Lv′ = Kv. Given an element a ∈ K, if v is a ﬁnite
place, we assume that v(a) is odd; if v is an archimedean place, we assume τv(a) < 0. Then
a /∈ L×2.

Proof. The condition that v(a) is odd for the ﬁnite place v, or that τv(a) < 0 for the
archimedean place v, implies that a /∈ K ×2
v . For Lv′ = Kv, we have a /∈ L×2
v′ , so a /∈ L×2. □

3. Main results for Châtelet surfaces

In this section, we will construct three kinds of Châtelet surfaces. Each kind in each
following subsection has the arithmetic properties mentioned in Subsection 1.3.

Let K be a number ﬁeld. Châtelet surfaces are smooth projective models of conic bundle
surfaces deﬁned by the equation

(1) y2 − az2 = P (x)

in K[x, y, z] such that a ∈ K ×, and that P (x) is a separable degree-4 polynomial in K[x].
Given an equation (1), let V 0 be the aﬃne surface in A3
K deﬁned by this equation. The
natural smooth compactiﬁcation V of V 0 given in [Sko01, Section 7.1] is called the Châtelet
surface given by this equation, cf. [Poo09, Section 5].

CHÂTELET SURFACES AND NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR 3-FOLDS7

Remark 3.0.1. For any local ﬁeld Kv, if a ∈ K ×2
v , then V is birational equivalent to P2

over Kv. By the implicit function theorem, there exists a Kv-point on V.

Remark 3.0.2. For any local ﬁeld Kv, by smoothness of V, the implicit function theorem
implies that the nonemptiness of V 0(Kv) is equivalent to the nonemptiness of V (Kv), and
that V 0(Kv) is open dense in V (Kv). Given an element A ∈ Br(V ), the evaluation of
A on V (Kv) is locally constant. By the properness of V, the space V (Kv) is compact.
So the set of all possible values of the evaluation of A on V (Kv) is ﬁnite. Indeed, by
[Sko01, Proposition 7.1.2], there only exist two possible values. It is determined by the
evaluation of A on V 0(Kv). In particular, if the evaluation of A on V 0(Kv) is constant,
then it is constant on V (Kv).

Remark 3.0.3. In [CTPS16, Proposition 6.1], it is shown that whether the Brauer-Manin
set of a smooth, projective, and geometrically connected variety is empty, is determined by
its birational equivalence class. Here birational equivalence means birational equivalence
between smooth, projective, and geometrically connected varieties. It is proved in the
papers [CTSSD87a, Theorem B; CTSSD87b] (also explained in the book [Sko01, Theorem
7.2.1]), that the Brauer-Manin obstruction to the Hasse principle and weak approximation
is the only one for Châtelet surfaces. Hence, all smooth projective models of a given
equation (1) are the same as to the discussion of the Hasse principle, weak approximation,
the failure of the Hasse principle explained by the Brauer-Manin obstruction, and weak
approximation with Brauer-Manin obstruction.

Remark 3.0.4. If the polynomial P (x) has a factor x
2 − a, i.e. there exists a degree-2
polynomial f (x) such that P (x) = f (x)(x
2 − a), then Y = xy+az
x2−a and Z = y+xz
x2−a give
a birational equivalence between V and a quadratic surface given by Y 2 − aZ 2 = f (x)
with aﬃne coordinates (x, Y, Z). By the Hasse-Minkowski theorem and Remark 3.0.3, the
surface V satisﬁes weak approximation.

In this section, we always use the following way to choose an element for the parameter a
in the equation (1).

3.0.1. Choosing an element for the parameter a in the equation (1). Given an extension
of number ﬁelds L/K, and a ﬁnite subset S ⊂ ΩK\(∞
c
K ∪ 2K), we will choose an element
a ∈ OK\K 2 with respect to these L/K and S in the following way.

If S = ∅, by Theorem 2.0.2, we can take a place v0 ∈ Ωf
K\2K splitting completely in L.
Then replace S by {v0} to continue the following step.

Now, suppose that S ̸= ∅. For v ∈ ΩK, by Lemma 2.2.3, the set K ×2
v is a nonempty open
subset of Kv. For v ∈ Ωf
K, by Lemma 2.2.4, the set {a ∈ Kv|v(a) is odd} is a nonempty
open subset of Kv. Using weak approximation for the aﬃne line A1, we can choose an
element a ∈ K × satisfying the following conditions:

• τv(a) < 0 for all v ∈ S ∩ ∞K,
• a ∈ K ×2
v for all v ∈ 2K,
• v(a) is odd for all v ∈ S\∞K.

These conditions do not change by multiplying an element in K ×2, so we can assume
a ∈ OK. The conditions that v(a) is odd for all v ∈ S\∞K, and that τv(a) < 0 for all
v ∈ S ∩ ∞K, imply a ∈ OK\K 2
v for all v ∈ S. So a ∈ OK \K 2.

Remark 3.0.5. Let S′ = {v ∈ ∞
r
K|τv(a) < 0} ∪ {v ∈ Ωf
K\2K|v(a) is odd}, then S′ is a
ﬁnite set. By the conditions that τv(a) < 0 for all v ∈ S ∩ ∞K, and that v(a) is odd for all
v ∈ S\∞K, we have S′ ⊃ S. Then S′ ̸= ∅.

Remark 3.0.6. If there exists one place in S splitting completely in L or S = ∅, then by
the choice of a above and Lemma 2.2.8, the element a ∈ OK\L2.

Remark 3.0.7. For the choice of a, we can enlarge S in ΩK\(∞
c
K ∪ 2K) if necessary.

3.1. Châtelet surfaces without Kv point for any v ∈ S. In this subsection, we will
construct a Châtelet surface of the ﬁrst kind mentioned in Subsection 1.3.

8 HAN WU

3.1.1. Choice of parameters for the equation (1). Given an extension of number ﬁelds L/K,
and a ﬁnite subset S ⊂ ΩK\(∞
c
K ∪ 2K), we choose an element a ∈ OK\K 2 as in Subsub-
section 3.0.1.

If S = ∅, then let P (x) = 1 − x
4. Then the Châtelet surface V1 given by y2 − az2 = 1 − x
4,
has a rational point (x, y, z) = (0, 1, 0).

Now, suppose that S ̸= ∅. We will choose an element b ∈ K × with respect to the chosen a
in the following way.

Let S′ = {v ∈ ∞
r
K|τv(a) < 0} ∪ {v ∈ Ωf
K\2K|v(a) is odd} be as in Remark 3.0.5, then
S′ ⊃ S is a ﬁnite set. If v ∈ S\∞K, then v(a) is odd, which implies a /∈ K ×2
v . Then
by Lemma 2.2.6, the set {b ∈ K ×
v |(a, b)v = −1} is a nonempty open subset of Kv. If
v ∈ S′\(S ∪ ∞K), then by Lemma 2.2.5, the set {b ∈ K ×
v |(a, b)v = 1} is a nonempty
open subset of Kv. Using weak approximation for aﬃne line A1, we can choose an element
b ∈ K × satisfying the following conditions:

• τv(b) < 0 for all v ∈ S ∩ ∞K,
• τv(b) > 0 for all v ∈ (S′\S) ∩ ∞K,
• (a, b)v = −1 for all v ∈ S\∞K,
• (a, b)v = 1 for all v ∈ S′\(S ∪ ∞K).

We will choose an element c ∈ K × with respect to the chosen a, b in the following way.

Let S′′ = {v ∈ Ωf
K\2K|v(b) is odd}, then S′′ is a ﬁnite set. The same argument as in the
previous paragraph, we can choose an element c ∈ K × satisfying the following conditions:

• c ∈ K ×2
v for all v ∈ S,
• v(c) is odd for all v ∈ S′′\S′.

These conditions do not change by multiplying an element in K ×2, so we can assume
b, c ∈ OK.

Let P (x) = b(x
4 − ac), and let V1 be the Châtelet surface given by y2 − az2 = b(x
4 − ac).

Proposition 3.1.1. For any extension of number ﬁelds L/K, and any ﬁnite subset S ⊂
ΩK\(∞
c
K ∪ 2K) splitting completely in L, there exists a Châtelet surface V1 deﬁned over
K such that V1(AS
K) ⊂ V1(ASL
L ) is nonempty, but that V1(Kv) = V1(Lv′) = ∅ for all v ∈ S
and all v′ ∈ SL.

Proof. For the extension L/K, and the ﬁnite set S, we will check that the Châtelet surface
V1 chosen as in Subsubsection 3.1.1, has the properties.

For S = ∅, it is clear.

Now, suppose that S ̸= ∅. We will check these properties by local computation.

Suppose that v ∈ (∞K\S′) ∪ 2K. By the choice of a, we have a ∈ K ×2
v . By Remark 3.0.1,
the surface V1 admits a Kv-point.
Suppose that v ∈ (S′\S) ∩ ∞K. Take x0 ∈ K such that τv(x
4
0 − ac) > 0. By the choice
of b, we have τv(b(x
4
0 − ac)) > 0. So (a, b(x
4
0 − ac))v = 1, which implies that V 0
1 admits a
Kv-point with x = x0.
Suppose that v ∈ S′\(S ∪ ∞K), then by the choice of b, we have (a, b)v = 1. Take x0 ∈ Kv
such that the valuation v(x0) < 0, then by Lemma 2.2.2, we have (a, x
4
0 − ac)v = (a, x
4
0)v =
1. So (a, b(x
4
0 − ac))v = (a, b)v = 1, which implies that V 0
1 admits a Kv-point with x = x0.
Suppose that v ∈ S′′\S′. By the choice of a, b, c, the valuations v(a) and v(−abc) are even.
By Lemma 2.2.1, we have (a, −abc)v = 1, which implies that V 0
1 admits a Kv-point with
x = 0.
Suppose that v ∈ Ωf
K\(S′ ∪ S′′ ∪ 2K). Take x0 ∈ Kv such that the valuation v(x0) < 0,
then by Lemma 2.2.2, we have (a, x
4
0 − ac)v = (a, x
4
0)v = 1. For v(a) and v(b) are even, by
Lemma 2.2.1), we have (a, b)v = 1. So (a, b(x
4
0 − ac))v = 1, which implies that V 0
1 admits
a Kv-point with x = x0.
So, the subset V1(AS
K) ⊂ V1(ASL
L ) is nonempty.

CHÂTELET SURFACES AND NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR 3-FOLDS9

Suppose that v ∈ S ∩ ∞K . Then by the choice of a, b, c, we have τv(a), τv(b) and τv(ac) are
negative. So (a, b(x
4 − ac))v = −1 for all x ∈ Kv, which implies that V 0
1 has no Kv-point.
By Remark 3.0.2, we have V1(Kv) = ∅.
Suppose that v ∈ S\∞K. Then by the choice of b, we have (a, b)v = −1. Let x ∈ Kv. If
4v(x) < v(ac), then by Lemma 2.2.2, we have (a, x
4 − ac)v = (a, x
4)v = 1. If 4v(x) > v(ac),
then by Lemma 2.2.2, we have (a, x
4 −ac)v = (a, −ac)v = (a, c)v = 1 (by the choice of c, the
last equality holds). For c ∈ K ×2
v , the valuation v(ac) is odd. So, the equality 4v(x) = v(ac)
cannot happen. In each case, we have (a, b(x
4 − ac))v = (a, b)v(a, x
4 − ac)v = −1, which
implies that V 0
1 has no Kv-point. By Remark 3.0.2, we have V1(Kv) = ∅.
So, the set V1(Kv) = ∅ for all v ∈ S.

Take a place v′
0 ∈ SL. Let v0 ∈ S be the restriction of v′
0 on K. By the assumption that v0
splits completely in L, we have Kv0 = Lv′
0. Hence V1(Kv0 ) = V1(Lv′
0).
So, the set V1(Lv′ ) = ∅ for all v′ ∈ SL. □

Remark 3.1.2. By the choice of elements a, c in Subsubsection 3.1.1, if v ∈ S\∞K, then
by comparing the valuation, the polynomial P (x) is irreducible over Kv. In this case, since
the choice of c is not unique, we choose another one to get a new polynomial P ′(X), so the
polynomials P (x) and P ′(x) are coprime in K. For v ∈ S ∩ ∞K, the polynomial P (x) is a
product of two irreducible factors over Kv.

Using the construction method in Subsubsection 3.1.1, we have the following examples,
which are special cases of Proposition 3.1.1. They will be used for further discussion.

Example 3.1.3. Let K = Q, and let ζ7 be a primitive 7-th root of unity. Let α = ζ7 + ζ−1
7
with the minimal polynomial x
3 + x
2 − 2x − 1. Let L = Q(α). Then the degree [L : K] = 3.
Let S = {29}. For 29 ≡ 1 mod 7, the place 29 splits completely in L, indeed in Q(ζ7).
Using the construction method in Subsubsection 3.1.1, we choose data: S = {29}, S′ =
{13, 29}, S′′ = {7}, a = 377, b = 14, c = 238 and P (x) = 14(x
4 − 89726). Then the
Châtelet surface given by y2 − 377z2 = P (x), has the properties of Proposition 3.1.1.

Example 3.1.4. Let K = Q, and let L = Q(
√
3). Using the construction method in
Subsubsection 3.1.1, we choose data: S = {∞K}, S′ = ∞K ∪ {23}, S′′ = {5}, a =
−23, b = −5, c = 5 and P (x) = −5(x
4 + 115). Then the Châtelet surface given by
y2 + 23z2 = P (x), has the properties of Proposition 3.1.1.

Example 3.1.5. Let K = Q, and let L = Q(
√
3). Then the place 23 splits completely in
L. Using the construction method in Subsubsection 3.1.1, we choose data: S = {23}, S′ =
∞K ∪ {23}, S′′ = {5}, a = −23, b = 5, c = 35 and P (x) = 5(x
4 + 805). Then the Châtelet
surface given by y2 + 23z2 = P (x), has the properties of Proposition 3.1.1.

3.2. Châtelet surfaces with rational points and not satisfying weak approxi-
mation. Given an number ﬁeld K, Liang [Lia18, Proposition 3.4] constructed a Châtelet
surface over K, which has a K-rational point and does not satisfy weak approximation oﬀ
∞K. Using the same method as in [Poo09, Section 5] to choose the parameters for the
equation (1), he constructed a Châtelet surface, and there exists an element in the Brauer
group of this surface, which has two diﬀerent local invariants on a given ﬁnite place, i.e. this
element gives an obstruction to weak approximation for this surface. In this subsection,
we generalize it.

Next, we will construct a Châtelet surface of the second kind mentioned in Subsection 1.3.

3.2.1. Choice of parameters for the equation (1). Given an extension of number ﬁelds L/K,
and a ﬁnite subset S ⊂ ΩK\(∞
c
K ∪ 2K), we choose an element a ∈ OK\K 2 as in Subsub-
section 3.0.1.

We will choose an element b ∈ K × with respect to the chosen a in the following way.

Let S′ = {v ∈ ∞
r
K|τv(a) < 0} ∪ {v ∈ Ωf
K\2K|v(a) is odd} be as in Remark 3.0.5, then
S′ ⊃ S is a ﬁnite set. By Lemma 2.2.4, for v ∈ S\∞K, the set {b ∈ Kv|v(b) = −v(a)}
is a nonempty open subset of Kv; for v ∈ S′\(S ∪ ∞K), the set {b ∈ Kv|v(b) = v(a)}

10 HAN WU

is a nonempty open subset of OKv . By Lemma 2.0.1, we can choose a nonzero element
b ∈ OS[1/2] satisfying the following conditions:

• v(b) = −v(a) for all v ∈ S\∞K,
• v(b) = v(a) for all v ∈ S′\(S ∪ ∞K).

We will choose an element c ∈ K × with respect to the chosen a, b in the following way.

Let S′′ = {v ∈ Ωf
K\2K|v(b) ̸= 0}, then S′′ is a ﬁnite set and S′\∞K ⊂ S′′. By Theorem
2.0.2, we can take two diﬀerent ﬁnite places v1, v2 ∈ Ωf
K\S′′ splitting completely in L. If
v ∈ S\∞K, then v(a) is odd. In this case, by Lemma 2.2.7, the set {c ∈ O×
Kv |(a, c)v = −1}
is a nonempty open subset of OKv . If v ∈ {v1, v2}, then b ∈ O×
Kv . In this case, by Lemma
2.2.4, the sets {c ∈ Kv|v(c) = 1} and {c ∈ Kv|v(1 + cb2) = 1} are nonempty open subsets
of OKv . Also by Lemma 2.0.1, we can choose a nonzero element c ∈ OK[1/2] satisfying the
following conditions:

• τv(1 + cb2) < 0 for all v ∈ S ∩ ∞K,
• τv(c) > 0 for all v ∈ (S′\S) ∩ ∞K,
• (a, c)v = −1 and v(c) = 0 for all v ∈ S\∞K,
• v1(c) = 1 and v2(1 + cb2) = 1 for the chosen v1, v2 above.

Let P (x) = (cx
2 + 1)((1 + cb2)x
2 + b2), and let V2 be the Châtelet surface given by
y2 − az2 = (cx
2 + 1)((1 + cb2)x
2 + b2).

Proposition 3.2.1. For any extension of number ﬁelds L/K, and any ﬁnite subset S ⊂
ΩK\(∞
c
K ∪ 2K) splitting completely in L, there exists a Châtelet surface V2 deﬁned over
K, which has the following properties.

• The Brauer group Br(V2)/Br(K) ∼= Br(V2L)/Br(L) ∼= Z/2Z, is generated by an
element A ∈ Br(V2). The subset V2(K) ⊂ V2(L) is nonempty.
• For any v ∈ S, there exist Pv and Qv in V2(Kv) such that the local invariants
invv(A(Pv)) = 0 and invv(A(Qv)) = 1/2. For any other v /∈ S, and any Pv ∈
V2(Kv), the local invariant invv(A(Pv)) = 0.
• For any v′ ∈ SL, there exist Pv′ and Qv′ in V2(Lv′ ) such that the local invariants
invv′ (A(Pv′ )) = 0 and invv′ (A(Qv′ )) = 1/2. For any other v′ /∈ SL, and any
Pv′ ∈ V2(Lv′ ), the local invariant invv′ (A(Pv′ )) = 0.

Proof. For the extension L/K, and the ﬁnite set S, we will check that the Châtelet surface
V2 chosen as in Subsubsection 3.2.1, has the properties.

We need to prove the statement about the Brauer group, and ﬁnd the element A in this
proposition.

By the choice of the places v1, the polynomial x
2 + c is an Eisenstein polynomial, so
it is irreducible over Kv1 . Since v1(a) is even, we have K(
√
a)Kv1 ≇ Kv1[x]/(cx
2 + 1).
So K(
√
a) ≇ K[x]/(cx
2 + 1). The same argument holds for the place v2 and polynomial
(1+cb2)x
2 +b2. For all places of S split completely in L, then by Remark 3.0.6, we have a ∈
OK \L2. By the splitting condition of v1, v2, we have L(
√
a) ≇ L[x]/(cx
2 + 1) and L(
√
a) ≇
L[x]/((1 + cb2)x
2 + b2). So P (x) = (cx
2 + 1)((1 + cb2)x
2 + b2) is separable and a product
of two degree-2 irreducible factors over K and L. According to [Sko01, Proposition 7.1.1],
the Brauer group Br(V2)/Br(K) ∼= Br(V2L)/Br(L) ∼= Z/2Z. Furthermore, by Proposition
7.1.2 in loc. cit, we take the quaternion algebra A = (a, cx
2 + 1) ∈ Br(V2) as a generator
element of this group. Then we have the equality A = (a, cx
2 + 1) = (a, (1 + cb2)x
2 + b2)
in Br(V2).

For (x, y, z) = (0, b, 0) is a rational point on V 0
2 , the set V2(K) is nonempty. We denote
this rational point by Q0.

We need to compute the evaluation of A on V2(Kv) for all v ∈ ΩK.

For any v ∈ ΩK, the local invariant invv(A(Q0)) = 0. By Remark 3.0.2, it suﬃces to
compute the local invariant invv(A(Pv)) for all Pv ∈ V 0
2 (Kv).
Suppose that v ∈ (∞K\S′) ∪ 2K. Then a ∈ K ×2
v , so invv(A(Pv)) = 0 for all Pv ∈ V2(Kv).

CHÂTELET SURFACES AND NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR 3-FOLDS11

Suppose that v ∈ (S′\S) ∩ ∞K . For any x ∈ K, by the choice of c, we have τv(cx
2 + 1) > 0.
Then (a, cx
2 + 1)v = 1, so invv(A(Pv)) = 0 for all Pv ∈ V2(Kv).
Suppose that v ∈ S′\(S ∪∞K). Take an arbitrary Pv ∈ V 0
2 (Kv). If invv(A(Pv)) = 1/2, then
(a, cx
2 + 1)v = −1 = (a, (1 + cb2)x
2 + b2)v at Pv. By Lemma 2.2.2, the ﬁrst equality implies
v(x) ≤ 0. For v(a) = v(b) > 0 and v(c) ≥ 0, by Lemma 2.2.2, we have (a, (1+cb2)x
2+b2)v =
(a, x
2)v = 1, which is a contradiction. So invv(A(Pv)) = 0.
Suppose that v ∈ Ωf
K\(S′∪2K). Take an arbitrary Pv ∈ V 0
2 (Kv). If invv(A(Pv)) = 1/2, then
(a, cx
2 + 1)v = −1 = (a, (1 + cb2)x
2 + b2)v at Pv. For v(a) is even, by Lemma 2.2.1, the ﬁrst
equality implies that v(cx
2 + 1) is odd. For c ∈ OK[1/2], we have v(x) ≤ 0. So v(c + x
−2)
is odd and positive. For v(b) ≥ 0, by Hensel’s lemma, we have 1 + b2(c + x
−2) ∈ K ×2
v .
So (a, (1 + cb2)x
2 + b2)v = (a, x
2)v(a, 1 + b2(c + x
−2))v = 1, which is a contradiction. So
invv(A(Pv)) = 0.

Suppose that v ∈ S ∩ ∞K. Take Pv = Q0, then invv(A(Pv)) = 0. By the choice of b, c,

we have τv( b
2
−cb2−1 ) > τv( 1
−c ) > 0. Take x0 ∈ K such that τv(x0) > √
τv( b2
−cb2−1 ), then

τv((cx
2
0 + 1)((1 + cb2)x
2
0 + b2)) > 0 and τv(cx
2
0 + 1) < 0. So there exists a Qv ∈ V 0
2 (Kv)
with x = x0. Then invv(A(Qv)) = 1/2.
Suppose that v ∈ S\∞K. Take Pv = Q0, then invv(A(Pv)) = 0. Take x0 ∈ Kv such that
v(x0) < 0. For v(b) = −v(a) < 0 and v(c) = 0, by Lemma 2.2.2, we have (a, cx
2
0 + 1)v =
(a, cx
2
0)v = (a, c)v and (a, (1 + cb2)x
2
0 + b2)v = (a, cb2x
2
0)v = (a, c)v. So (a, (cx
2
0 + 1)((1 +
cb2)x
2
0 + b2))v = (a, c)v(a, c)v = 1. Hence, there exists a Qv ∈ V 0
2 (Kv) with x = x0. For
(a, c)v = −1, we have invv(A(Qv)) = 1/2.

Finally, we need to compute the evaluation of A on V2(Lv′ ) for all v′ ∈ ΩL.

For any v′ ∈ ΩL, the local invariant invv′ (A(Q0)) = 0.
Suppose that v′ ∈ SL. Let v ∈ ΩK be the restriction of v′ on K. By the assumption that v
is split completely in L, we have Kv = Lv′ . So V2(Kv) = V2(Lv′). By the argument already
shown, there exist Pv, Qv ∈ V2(Kv) such that invv(A(Pv)) = 0 and invv(A(Qv)) = 1/2.
View Pv, Qv as elements in V2(Lv′), and let Pv′ = Pv and Qv′ = Qv. Then invv′ (A(Pv′ )) =
invv(A(Pv)) = 0 and invv′ (A(Qv′ )) = invv(A(Qv)) = 1/2.
Suppose that v′ ∈ ΩL\SL. This local computation is the same as the case v ∈ ΩK\S. □

Remark 3.2.2. For any v ∈ S, and any Pv ∈ V2(Kv), the local invariant of the eval-
uation of A on Pv is 0 or 1/2. Let U1 = {Pv ∈ V2(Kv)| invv(A(Pv)) = 0} and U2 =
{Pv ∈ V2(Kv)| invv(A(Pv)) = 1/2}. Then U1 and U2 are nonempty disjoint open subsets
of V2(Kv), and V2(Kv) = U1 ⊔ U2.

The following proposition states that the surface V2 in Proposition 3.2.1, has the following
weak approximation properties.

Proposition 3.2.3. Given an extension of number ﬁelds L/K, and a ﬁnite subset S ⊂
ΩK\(∞
c
K ∪ 2K) splitting completely in L, let V2 be a Châtelet surface satisfying those
properties of Proposition 3.2.1. If S = ∅, then V2 and V2L satisfy weak approximation. If
S ̸= ∅, then V2 satisﬁes weak approximation oﬀ S′ for any ﬁnite subset S′ ⊂ ΩK such that
S′ ∩ S ̸= ∅, while it fails for any ﬁnite subset S′ ⊂ ΩK such that S′ ∩ S = ∅. And in the
case S ̸= ∅, the surface V2L satisﬁes weak approximation oﬀ T for any ﬁnite subset T ⊂ ΩL
such that T ∩ SL ̸= ∅, while it fails for any ﬁnite subset T ⊂ ΩL such that T ∩ SL = ∅.

Proof. According to [CTSSD87a, Theorem B; CTSSD87b], the Brauer-Manin obstruction
to the Hasse principle and weak approximation is the only one for Châtelet surfaces, so
V2(K) is dense in V2(AK)
Br.

Suppose that S = ∅, then for any (Pv)v∈ΩK ∈ V2(AK), by Proposition 3.2.1, the sum∑v∈ΩK invv(A(Pv)) = 0. For Br(V2)/Br(K) is generated by the element A, we have
V2(AK)
Br = V2(AK). So V2(K) is dense in V2(AK)
Br = V2(AK ), i.e. the surface V2 satisﬁes
weak approximation.

Suppose that S′ ∩ S ̸= ∅. Take v0 ∈ S′ ∩ S. For any ﬁnite subset R ⊂ ΩK\{v0},
take a nonempty open subset M = V2(Kv0 ) × ∏
v∈R Uv × ∏
v /∈R∪{v0} V2(Kv) ⊂ V2(AK).
Take an element (Pv)v∈ΩK ∈ M. By Proposition 3.2.1 and v0 ∈ S, we can take an

12 HAN WU

element P ′
v0 ∈ V2(Kv0) such that invv0 A(P ′
v0 ) = 1/2. By Proposition 3.2.1, the sum∑v∈ΩK \{v0} invv(A(Pv)) is 0 or 1/2 in Q/Z. If it is 1/2, then we replace Pv0 by P ′
v0 . In this
way, we get a new element (Pv)v∈ΩK ∈ M. And the sum ∑v∈ΩK invv(A(Pv)) = 0 in Q/Z.
So (Pv)v∈ΩK ∈ V2(AK)
Br ∩ M. For V2(K) is dense in V2(AK)
Br, the set V2(K) ∩ M ̸= ∅,
which implies that V2 satisﬁes weak approximation oﬀ {v0}. So V2 satisﬁes weak approxi-
mation oﬀ S′.

Suppose that S ̸= ∅ and S′∩S = ∅. Take v0 ∈ S, and let Uv0 = {Pv0 ∈ V2(Kv0 )| invv0 (A(Pv0 )) =
1/2}. For v ∈ S\{v0}, let Uv = {Pv ∈ V2(Kv)| invv(A(Pv)) = 0}. For any v ∈ S, by Remark
3.2.2, the set Uv is a nonempty open subset of V2(Kv). Let M = ∏v∈S Uv ×∏
v /∈S V2(Kv). It
is a nonempty open subset of V2(AK ). For any (Pv)v∈ΩK ∈ M, by Proposition 3.2.1 and the
choice of Uv, the sum ∑v∈ΩK invv(A(Pv)) = 1/2 is nonzero in Q/Z. So V2(AK )
Br ∩ M = ∅,
which implies V2(K) ∩ M = ∅. Hence V2 does not satisfy weak approximation oﬀ S′.

The same argument applies to V2L. □

Applying the construction method in Subsubsection 3.2.1, we have the following weak
approximation properties for Châtelet surfaces.

Corollary 3.2.4. For any extension of number ﬁelds L/K, and any ﬁnite nonempty subset
S ⊂ ΩK\(∞
c
K ∪2K) splitting completely in L, there exists a Châtelet surface V deﬁned over
K such that V (K) ̸= ∅. For any subﬁeld L′ ⊂ L over K, the Brauer group Br(V )/Br(K) ∼=
Br(VL′ )/Br(L′) ∼= Z/2Z. And the surface VL′ has the following properties.

• For any ﬁnite subset T ′ ⊂ ΩL′ such that T ′ ∩ SL′ ̸= ∅, the surface VL′ satisﬁes
weak approximation oﬀ T ′.
• For any ﬁnite subset T ′ ⊂ ΩL′ such that T ′ ∩ SL′ = ∅, the surface VL′ does not
satisfy weak approximation oﬀ T ′. In particular, the surface VL′ does not satisfy
weak approximation.

Proof. For the extension L/K, and S, let V be the Châtelet surface chosen as in Subsubsec-
tion 3.2.1. Applying the same argument about the ﬁeld L to its subﬁeld L′, the properties
that we list, are just what we have explained in Proposition 3.2.1 and Proposition 3.2.3. □

Using the construction method in Subsubsection 3.2.1, we have the following example,
which is a special case of Proposition 3.2.1. It will be used for further discussion.

Example 3.2.5. Let K = Q, L = Q(
√
3), and let S = {73}. The prime numbers 11, 23, 73
split completely in L. Using the construction method in Subsubsection 3.2.1, we choose
data: S = S′ = S′′ = 73, v1 = 11, v2 = 23, a = 73, b = 1/73, c = 99 and P (x) =
(99x
2 + 1)(5428x
2/5329 + 1/5329). Then the Châtelet surface given by y2 − 73z2 = P (x),
has the properties of Proposition 3.2.1, Proposition 3.2.3.

3.3. Châtelet surfaces related to the Hasse principle. Iskovskikh [Isk71] gave an
example of the intersection of two quadratic hypersurfaces in P4
Q, which is a Châtelet
surface over Q given by y2 + z2 = (x
2 − 2)(−x
2 + 3). He showed that this Châtelet surface
is a counterexample to the Hasse principle. Similarly, Skorobogatov [Sko01, Pages 145-
146] gave a family of Châtelet surfaces with a parameter over Q. He discussed the property
of the Hasse principle for this family. Poonen [Poo09, Proposition 5.1] generalized their
arguments to any number ﬁeld. Given an number ﬁeld K, he constructed a Châtelet surface
deﬁned over K, which is a counterexample to the Hasse principle. He used the Čebotarev’s
density theorem for some ray class ﬁelds to choose the parameters for the equation (1). The
Châtelet surface that he constructed, has the property of [Poo09, Lemma 5.5] (a special
situation of the following Proposition 3.3.1: the case when S = {v0} for some place v0
associated to some large prime element in OK), which is the main ingredient in the proof
of [Poo09, Proposition 5.1]. In this subsection, we generalize them.

Next, we will construct a Châtelet surface of the third kind mentioned in Subsection 1.3.

CHÂTELET SURFACES AND NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR 3-FOLDS13

3.3.1. Choice of parameters for the equation (1). Given an extension of number ﬁelds L/K,
and a ﬁnite subset S ⊂ ΩK\(∞
c
K ∪ 2K), we choose an element a ∈ OK\K 2 as in Subsub-
section 3.0.1.

We will choose an element b ∈ K × with respect to the chosen a in the following way.

Let S′ = {v ∈ ∞
r
K|τv(a) < 0} ∪ {v ∈ Ωf
K\2K|v(a) is odd} be as in Remark 3.0.5, then
S′ ⊃ S is a ﬁnite set. If v ∈ S\∞K, then v(a) is odd. Then by Lemma 2.2.7, the set
{b ∈ O×
Kv |(a, b)v = −1} is a nonempty open subset of OKv . If v ∈ S′\(S ∪ ∞K), then by
Lemma 2.2.5, the set {b ∈ O×
Kv |(a, b)v = 1} is a nonempty open subset of OKv . By Lemma
2.0.1, we can choose a nonzero element b ∈ OK[1/2] satisfying the following conditions:

• τv(b) < 0 for all v ∈ S ∩ ∞K,
• τv(b) > 0 for all v ∈ (S′\S) ∩ ∞K,
• (a, b)v = −1 and v(b) = 0 for all v ∈ S\∞K,
• (a, b)v = 1 and v(b) = 0 for all v ∈ S′\(S ∪ ∞K).

We will choose an element c ∈ K × with respect to the chosen a, b in the following way.

Let S′′ = {v ∈ Ωf
K\2K|v(b) ̸= 0}, then S′′ is a ﬁnite set and S′ ∩S′′ = ∅. By Theorem 2.0.2,
we can take two diﬀerent ﬁnite places v1, v2 ∈ Ωf
K\(S′ ∪ S′′ ∪ 2K) splitting completely in
L. If v ∈ (S′\∞K) ∪ {v1, v2}, then b ∈ O×
Kv . In this case, by Lemma 2.2.4, the sets
{c ∈ Kv|v(bc + 1) = v(a) + 2}, {c ∈ Kv|v(c) = 1} and {c ∈ Kv|v(bc + 1) = 1} are nonempty
open subsets of OKv . If v ∈ S′′, by Lemma 2.2.5, the set {c ∈ O×
Kv |(a, c)v = 1} is a
nonempty open subset of OKv . Also by Lemma 2.0.1, we can choose a nonzero element
c ∈ OK[1/2] satisfying the following conditions:

• 0 < τv(c) < −1/τv(b) for all v ∈ S ∩ ∞K,
• τv(bc + 1) < 0 for all v ∈ (S′\S) ∩ ∞K,
• v(bc + 1) = v(a) + 2 for all v ∈ S′\∞K,
• (a, c)v = 1 for all v ∈ S′′,
• v1(c) = 1 and v2(bc + 1) = 1 for the chosen v1, v2 above.

Let P (x) = (x
2 − c)(bx
2 − bc − 1), and let V3 be the Châtelet surface given by y2 − az2 =
(x
2 − c)(bx
2 − bc − 1).

Proposition 3.3.1. For any extension of number ﬁelds L/K, and any ﬁnite subset S ⊂
ΩK\(∞
c
K ∪ 2K) splitting completely in L, there exists a Châtelet surface V3 deﬁned over
K, which has the following properties.

• The Brauer group Br(V3)/Br(K) ∼= Br(V3L)/Br(L) ∼= Z/2Z, is generated by an
element A ∈ Br(V3). The subset V3(AK) ⊂ V3(AL) is nonempty.
• For any v ∈ ΩK, and any Pv ∈ V3(Kv),

invv(A(Pv)) =
 {0 if v /∈ S,
1/2 if v ∈ S.

• For any v′ ∈ ΩL, and any Pv′ ∈ V3(Lv′),

invv′ (A(Pv′ )) =
 {0 if v′ /∈ SL,
1/2 if v′ ∈ SL.

Proof. For the extension L/K, and the ﬁnite set S, we will check that the Châtelet surface
V3 chosen as in Subsubsection 3.3.1, has the properties.

Firstly, we need to check that V3 has an AK-adelic point.

Suppose that v ∈ (∞K\S′) ∪ 2K. Then a ∈ K ×2
v . By Remark 3.0.1, the surface V3 admits
a Kv-point.
Suppose that v ∈ (S′\S) ∩ ∞K. Let x0 = 0. For τv(b) > 0 and τv(bc + 1) < 0, we have
τv(c) < 0 and τv((x
2
0 − c)(bx
2
0 − bc − 1)) = τv(c(bc + 1)) > 0, which implies that V 0
3 admits
a Kv-point with x = 0.
Suppose that v ∈ S′\(S ∪ ∞K). Take x0 ∈ Kv such that the valuation v(x0) < 0. For
b ∈ O×
Kv and c ∈ OK[1/2], by Lemma 2.2.2, we have (a, x
2
0 − c)v = (a, x
2
0)v = 1 and

14 HAN WU

(a, bx
2
0 − bc − 1)v = (a, bx
2
0)v = (a, b)v. By the choice of b, we have (a, b)v = 1. Hence
(a, (x
2
0 − c)(bx
2
0 − bc − 1))v = (a, b)v = 1, which implies that V 0
3 admits a Kv-point with
x = x0.
Suppose that v ∈ S′′. By the choice of a, b, c, we have (a, c)v = 1, v(a) even, and bc + 1 ∈
O×
Kv . By Lemma 2.2.1, we have (a, bc+1)v = 1. Let x0 = 0. Then (a, (x
2
0−c)(bx
2
0−bc−1))v =
(a, c(bc+1))v = (a, c)v(a, bc+1)v = 1, which implies that V 0
3 admits a Kv-point with x = 0.
Suppose that v ∈ Ωf
K\(S′ ∪ S′′ ∪ 2K). Then v(b) = 0. Take x0 ∈ Kv such that the valuation
v(x0) < 0. For b ∈ O×
Kv and c ∈ OK[1/2], by Lemma 2.2.2, we have (a, x
2
0 −c)v = (a, x
2
0)v =
1 and (a, bx
2
0 − bc − 1)v = (a, bx
2
0)v = (a, b)v. For v(a) and v(b) are even, by Lemma 2.2.1,
we have (a, b)v = 1. So (a, (x
2
0 − c)(bx
2
0 − bc − 1))v = (a, b)v = 1, which implies that V 0
3
admits a Kv-point with x = x0.
Suppose that v ∈ S ∩ ∞K. Let x0 = 0. Then by the choice of a, b, c, we have τv(a) < 0,
τv(c) > 0 and τv(bc + 1) > 0. So (a, (x
2
0 − c)(bx
2
0 − bc − 1))v = (a, c(bc + 1))v = 1, which
implies that V 0
3 admits a Kv-point with x = 0.
Suppose that v ∈ S\∞K. Choose a prime element πv and take x0 = πv. By the choice of
a, b, c, we have b, c ∈ O×
Kv , v(bx
2
0) = 2, and v(bc + 1) = v(a) + 2 ≥ 3. By Lemma 2.2.2, we
have (a, x
2
0 − c)v = (a, −c)v and (a, bx
2
0 − bc − 1)v = (a, bx
2
0)v. By Hensel’s lemma, we have
−bc = 1 − (bc + 1) ∈ K ×2
v . So (a, (x
2
0 − c)(bx
2
0 − bc − 1))v = (a, −bcx
2
0)v = 1, which implies
that V 0
3 admits a Kv-point with x = πv.

Secondly, we need to prove the statement about the Brauer group, and ﬁnd the element A
in this proposition.

By the choice of the places v1, the polynomial x
2 − c is an Eisenstein polynomial, so
it is irreducible over Kv1. Since v1(a) is even, we have K(
√
a)Kv1 ≇ Kv1[x]/(x
2 − c).
So K(
√
a) ≇ K[x]/(x
2 − c). The same argument holds for the place v2 and polynomial
bx
2 − bc − 1. For all places of S split completely in L, then by Remark 3.0.6, we have
a ∈ OK \L2. By the splitting condition of v1, v2, we have L(
√
a) ≇ L[x]/(x
2 − c) and
L(
√
a) ≇ L[x]/(bx
2 − bc − 1). So P (x) = (x
2 − c)(bx
2 − bc − 1) is separable and a product
of two degree-2 irreducible factors over K and L. According to [Sko01, Proposition 7.1.1],
the Brauer group Br(V3)/Br(K) ∼= Br(V3L)/Br(L) ∼= Z/2Z. Furthermore, by Proposition
7.1.2 in loc. cit, we take the quaternion algebra A = (a, x
2 − c) ∈ Br(V3) as a generator
element of this group. Then we have the equality A = (a, x
2 − c) = (a, bx
2 − bc − 1) in
Br(V3).

Thirdly, We need to compute the evaluation of A on V3(Kv) for all v ∈ ΩK.

By Remark 3.0.2, it suﬃces to compute the local invariant invv(A(Pv)) for all Pv ∈ V 0
3 (Kv)
and all v ∈ ΩK.

Suppose that v ∈ (∞K\S′) ∪ 2K. Then a ∈ K ×2
v , so invv(A(Pv)) = 0 for all Pv ∈ V3(Kv).
Suppose that v ∈ (S′\S) ∩ ∞K. By the choice of b, c, we have τv(b) > 0 and τv(bc + 1) < 0.
So, for any x ∈ K, we have (a, bx
2−bc−1)v = 1. Hence invv(A(Pv)) = 0 for all Pv ∈ V 0
3 (Kv).
Suppose that v ∈ S′\(S ∪ ∞K). By the choice of b, we have (a, b)v = 1. Take an arbitrary
Pv ∈ V 0
3 (Kv). If v(x) < 0 at Pv, by Lemma 2.2.2, we have (a, x
2 − c)v = (a, x
2)v = 1.
If v(x) > 0 at Pv, since b, c ∈ O×
Kv and v(bc + 1) = v(a) + 2 ≥ 3, by Lemma 2.2.2, we
have (a, x
2 − c)v = (a, −c)v. By Hensel’s lemma, we have −bc = 1 − (bc + 1) ∈ K ×2
v . So
(a, x
2 − c)v = (a, −c)v = (a, −bc)v = 1. If v(x) = 0 at Pv, since b ∈ O×
Kv and v(bc + 1) =
v(a)+2 ≥ 3, by Lemma 2.2.2, we have (a, bx
2−bc−1)v = (a, bx
2)v = 1. So invv(A(Pv)) = 0.
Suppose that v ∈ Ωf
K\(S′ ∪ 2K). Take an arbitrary Pv ∈ V 0
3 (Kv). If invv(A(Pv)) = 1/2,
then (a, bx
2 − bc − 1)v = (a, x
2 − c)v = −1 at Pv. For v(a) is even, by Lemma 2.2.1, the last
equality implies that v(x
2 − c) is odd, so it is positive. So v(bx
2 − bc − 1) = 0. By Lemma
2.2.1, we have (a, bx
2 − bc − 1)v = 1, which is a contradiction. So invv(A(Pv)) = 0.

Suppose that v ∈ S ∩∞K . Take an arbitrary Pv ∈ V 0
3 (Kv). If A(Pv) = 0, then (a, bx
2 −bc−
1)v = (a, x
2 − c)v = 1 at Pv. The last equality implies that τv(x
2 − c) > 0. By the choice
of b, we have τv(b) < 0, so τv(bx
2 − bc − 1) < 0, which contradicts (a, bx
2 − bc − 1)v = 1.
So invv(A(Pv)) = 1/2.
Suppose that v ∈ S\∞K. By the choice of b, we have (a, b)v = −1. Take an arbitrary
Pv ∈ V 0
3 (Kv). If v(x) ≤ 0 at Pv, for b ∈ O×
Kv and v(bc + 1) = v(a) + 2 ≥ 3, by Lemma

CHÂTELET SURFACES AND NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR 3-FOLDS15

2.2.2, we have (a, bx
2 − bc − 1)v = (a, bx
2)v = −1. If v(x) > 0 at Pv, for b, c ∈ O×
Kv and
v(bc + 1) = v(a) + 2 ≥ 3, by Lemma 2.2.2, we have (a, x
2 − c)v = (a, −c)v. By Hensel’s
lemma, we have −bc = 1 − (bc + 1) ∈ K ×2
v . So (a, x
2 − c)v = (a, −c)v = −(a, −bc)v = −1.
So invv(A(Pv)) = 1/2.

Finally, we need to compute the evaluation of A on V3(Lv′ ) for all v′ ∈ ΩL.

Suppose that v′ ∈ SL. Let v ∈ ΩK be the restriction of v′ on K. By the assumption
that v is split completely in L, we have Kv = Lv′ . So V3(Kv) = V3(Lv′). Then for any
Pv′ ∈ V3(Lv′), denote Pv′ in V3(Kv) by Pv. Then by the argument already shown, the local
invariant invv′ (A(Pv′ )) = invv(A(Pv)) = 1/2.
Suppose that v′ ∈ ΩL\SL. This local computation is the same as the case v ∈ ΩK\S. □

Remark 3.3.2. If the surface V3 has a K-rational point Q, then by the global reciprocity law,
the sum ∑

v∈ΩK invv(A(Q)) = 0 in Q/Z. If the number ♯S is odd, then from Proposition
3.3.1 that we get, this sum is ♯S/2, which is nonzero in Q/Z. So, in this case, the surface
V3 has no K-rational point, which implies that the surface V3 is a counterexample to the
Hasse principle. If the number ♯S is even, then for any (Pv)v∈ΩK ∈ V3(AK), by Proposition
3.3.1, the sum ∑v∈ΩK invv(A(Pv)) = ♯S/2 = 0 in Q/Z. For Br(V3)/Br(K) is generated by
the element A, we have V3(AK)
Br = V3(AK) ̸= ∅. According to [CTSSD87a, Theorem B;
CTSSD87b], the Brauer-Manin obstruction to the Hasse principle and weak approximation
is the only one for Châtelet surfaces. So, in this case, the set V3(K) ̸= ∅, and it is dense
in V3(AK)
Br = V3(AK), i.e. the surface V3 has a K-rational point and satisﬁes weak
approximation. In particular, if the number ♯S = 0, i.e. S = ∅, though the Brauer group
Br(V3)/Br(K) is nontrivial, it gives no obstruction to week approximation for V3.

Applying the construction method in Subsubsection 3.3.1, we can relate the properties in
Proposition 3.2.1 to the Hasse principle and weak approximation.

Corollary 3.3.3. For any extension of number ﬁelds L/K, there exists a Châtelet surface
V deﬁned over K such that V (AK) ̸= ∅. For any subﬁeld L′ ⊂ L over K, the Brauer group
Br(V )/Br(K) ∼= Br(VL′ )/Br(L′) ∼= Z/2Z. And the surface VL′ has the following properties.

• If the degree [L′ : K] is odd, then the surface VL′ is a counterexample to the Hasse
principle. In particular, the surface V is a counterexample to the Hasse principle.
• If the degree [L′ : K] is even, then the surface VL′ satisﬁes weak approximation.
In particular, in this case, the set V (L′) ̸= ∅.

Proof. By Theorem 2.0.2, we can take a place v0 ∈ ΩK\(∞
c
K∪2K) splitting completely in L.
Let S = {v0}. Using the construction method in Subsubsection 3.3.1, there exists a Châtelet
surface V deﬁned over K having the properties of Proposition 3.3.1. By the same argument
as in the proof of Proposition 3.3.1, we have Br(V )/Br(K) ∼= Br(VL′ )/Br(L′) ∼= Z/2Z. For
v0 splits completely in L, it also does in L′. For ♯S is odd, if [L′ : K] is odd, then ♯SL′ is
odd; if [L′ : K] is even, then ♯SL′ is even. Applying the same argument about the ﬁeld L
to its subﬁeld L′, the properties that we list, are just what we have explained in Remark
3.3.2. □

Remark 3.3.4. Though the Brauer group Br(V )/Br(K) ∼= Br(VL′ )/Br(L′) ∼= Z/2Z in
Corollary 3.3.3, is nontrivial, it gives an obstruction to the Hasse principle for V, also VL′ if
[L′ : K] is odd; but no longer gives an obstruction to week approximation for VL′ if [L′ : K]
is even.

Using the construction method in Subsubsection 3.3.1, we have the following example,
which is a special case of Proposition 3.3.1. It will be used for further discussion.

Example 3.3.5. Let K = Q and L = Q(ζ7 + ζ−1
7 ) be as in Example 3.1.3, and let S =
{13}. For 132 ≡ 1 mod 7, 412 ≡ 1 mod 7 and 43 ≡ 1 mod 7, the places 13, 41, 43 split
completely in L. Using the construction method in Subsubsection 3.3.1, we choose data:
S = {13}, S′ = {13, 29}, S′′ = {5}, v1 = 43, v2 = 41, a = 377, b = 5, c = 878755181
and P (x) = (x
2 − 878755181)(5x
2 − 4393775906). Then the Châtelet surface given by
y2 − 377z2 = P (x), has the properties of Proposition 3.3.1.

16 HAN WU

4. Stoll’s conjecture for curves

Whether all failures of the Hasse principle of smooth, projective, and geometrically con-
nected curves deﬁned over a number ﬁeld, are explained by the Brauer-Manin obstruction,
was considered by Skorobogatov [Sko01, Chapter 6.3] and Scharaschkin [Sch99] indepen-
dently. Furthermore, Stoll [Sto07, Conjecture 9.1] made the following conjecture.

Given a curve C deﬁned over a number ﬁeld K, let C(AK )• = ∏v∈∞K {connected com-
ponents of C(Kv)} × C(Af
K ). The product topology of ∏v∈∞K {connected components
of C(Kv)} with discrete topology and C(Af
K ) with adelic topology, gives a topology for
C(AK )•. For any A ∈ Br(C), and any v ∈ ∞K, the evaluation of A on each connected
component of C(Kv) is constant. So, the notation C(AK )
Br makes sense.

Conjecture 4.0.1. [Sto07, Conjecture 9.1] For any smooth, projective, and geometrically
connected curve C deﬁned over a number ﬁeld K, the set C(K) is dense in C(AK )
Br. In
particular, the curve C satisﬁes weak approximation with Brauer-Manin obstruction oﬀ
∞K.

Remark 4.0.2. If Conjecture 4.0.1 holds for a given curve, which is a counterexample to the
Hasse principle, then its failure of the Hasse principle is explained by the Brauer-Manin
obstruction. For an elliptic curve deﬁned over K, if its Tate-Shafarevich group is ﬁnite,
then by the dual sequence of Cassels-Tate, Conjecture 4.0.1 holds for this elliptic curve.
With the eﬀort of Kolyvagin [Kol90, Kol91], Gross and Zagier [GZ86], and many others, for
an elliptic curve deﬁned over Q, if its analytic rank equals zero or one, then its Mordell-Weil
rank equals its analytic rank, and its Tate-Shafarevich group is ﬁnite. So, Conjecture 4.0.1
holds for this elliptic curve.

Deﬁnition 4.0.3. Given a nontrivial extension of number ﬁelds L/K, let C be a smooth,
projective, and geometrically connected curve deﬁned over K. We say that a triple (C, K, L)
is of type I if C(K) and C(L) are ﬁnite nonempty sets, C(K) ̸= C(L) and Stoll’s Conjecture
4.0.1 holds for the curve C. We say that a triple (C, K, L) is of type II if (C, K, L) is of
type I, and there exists a real place v′ ∈ ∞L such that C(Lv′ ) is connected.

Lemma 4.0.4. Given a nontrivial extension of number ﬁelds L/K, if Conjecture 4.0.1 holds
for all smooth, projective, and geometrically connected curves deﬁned over K, then there
exists a curve C deﬁned over K such that the triple (C, K, L) is of type I. Furthermore, if
L has a real place, then this triple (C, K, L) is of type II.

Proof. Since L is a ﬁnite separable extension over K, there exists a θ ∈ L such that
L = K(θ). Let f (x) be the minimal polynomial of θ. Let n = deg(f ), then n = [L : K] ≥ 2.
Let ˜f (w0, w1) be the homogenization of f. If n is odd, we consider a curve C deﬁned over
K by a homogeneous equation: wn+2
2 = ˜f (w0, w1)(w2
1 − w2
0) with homogeneous coordinates
(w0 : w1 : w2) ∈ P2. For the polynomials f (x) and x
2 −1 are separable and coprime in K[x],
the curve C is smooth, projective, and geometrically connected. By genus formula for a
plane curve, the genus of C equals g(C) = n(n + 1)/2 > 1. By Faltings’s theorem, the sets
C(K) and C(L) are ﬁnite. It is easy to check that (w0 : w1 : w2) = (1 : 1 : 0) ∈ C(K) and
(θ : 1 : 0) ∈ C(L)\C(K). By the assumption that Conjecture 4.0.1 holds for all smooth,
projective, and geometrically connected curves over K, we have that the triple (C, K, L)
is of type I. Since n + 2 is odd, the space C(Kv′ ) is connected for all v′ ∈ ∞L. So, if
L has a real place, then this triple (C, K, L) is of type II. If n is even, we replace the
homogeneous equation wn+2
2 = ˜f (w0, w1)(w2
1 − w2
0) by wn+3
2 = ˜f (w0, w1)w1(w2
1 − w2
0). The
same argument applies to this new curve and new triple. □

Remark 4.0.5. For some nonsquare integer d, let K = Q and L = Q(
√

d). Consider an
elliptic curve Ed deﬁned by a Weierstraß equation: y2 = x
3 + d. Let E(d)
d be the quadratic
twist of Ed by d. The curve Ed is connected over R. It is easy to check that the point
(x, y) = (0, √
d) ∈ C(L)\C(K). If both Ed(Q) and E(d)
d (Q) are ﬁnite, then the set Ed(L)
is ﬁnite, cf. [Sil09, Exercise 10.16]. If additionally, the Tate-Shafarevich group X(Ed, Q)
is ﬁnite, then the triple (Ed, K, L) is of type II.

CHÂTELET SURFACES AND NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR 3-FOLDS17

5. Poonen’s proposition

For our result is base on Poonen’s proposition [Poo10, Proposition 5.4]. We recall that
paper and his general result ﬁrst. There exist some remarks on it in [Lia18, Section 4.1].
Colliot-Thélène [CT10, Proposition 2.1] gave another proof of that proposition.

Recall 5.0.1. Let B be a smooth, projective, and geometrically connected variety over
a number ﬁeld K. Let L be a line bundle on B, assuming the set of global sections
Γ(B, L
⊗2) ̸= 0. Let E = OB ⊕ OB ⊕ L. Let a be a constant in K ×, and let s be a nonzero
global section in Γ(B, L
⊗2). The zero locus of (1, −a, −s) ∈ Γ(B, OB ⊕ OB ⊕ L
⊗2) ⊂
Γ(B, Sym2 E) in the projective space bundle Proj(E) is a projective and geometrically in-
tegral variety, denoted by X with the natural projection X → B. Let K be an algebraic
closure ﬁeld of K. Denote B ×Spec K Spec K by B.

Proposition 5.0.2. [Poo10, Proposition 5.3] Given a number ﬁeld K, all notations are
the same as in Recall 5.0.1. Let α : X → B be the natural projection. Assume that

• the closed subscheme deﬁned by s = 0 in B is smooth, projective, and geometrically
connected,
• BrB = 0 and X(AK) ̸= ∅.

Then X is smooth, projective, and geometrically connected. And α
∗ : Br(B) → Br(X) is
an isomorphism.

6. Main results for Châtelet surface bundles over curves

6.1. Preparation Lemmas. We state the following lemmas, which will be used for the
proof of our theorems.

Fibration methods are used to do research on weak approximation, weak approximation
with Brauer-Manin obstruction between two varieties. We modify those ﬁbration methods
to ﬁt into our context.

Lemma 6.1.1. Given a number ﬁeld K, and a ﬁnite subset S ⊂ ΩK, let f : X → Y be a
K-morphism of proper K-varieties X and Y . We assume that

(1) the set Y (K) is ﬁnite,
(2) the variety Y satisﬁes weak approximation with Brauer-Manin obstruction oﬀ S,
(3) for any P ∈ Y (K), the ﬁber XP of f over P satisﬁes weak approximation oﬀ S.

Then X satisﬁes weak approximation with Brauer-Manin obstruction oﬀ S.

Proof. For any ﬁnite subset S′ ⊂ ΩK\S, take an open subset N = ∏
v∈S′ Uv×∏
v /∈S′ X(Kv) ⊂
X(AK) such that N ⋂ X(AK)
Br ̸= ∅. Let M = ∏

v∈S′ f (Uv) × ∏

v /∈S′ f (X(Kv)), then by
the functoriality of Brauer-Manin pairing, M ⋂ Y (AK)
Br ̸= ∅. By Assumptions (1) and (2),
we have Y (K) = prS(Y (AK )
Br). So there exists P0 ∈ prS(M ) ⋂ Y (K). Consider the ﬁber
XP0 . Let L = ∏
v∈S′ [XP0(Kv) ⋂ Uv]×∏
v /∈S′∪S XP0 (Kv), then it is a nonempty open subset
of XP0(AS
K ). By Assumption (3), there exists Q0 ∈ L ⋂ XP0 (K). So Q0 ∈ X(K) ⋂ N, which
implies that X satisﬁes weak approximation with Brauer-Manin obstruction oﬀ S. □

Lemma 6.1.2. Given a number ﬁeld K, and a ﬁnite subset S ⊂ ΩK, let f : X → Y be a
K-morphism of proper K-varieties X and Y . We assume that

(1) the set Y (K) is ﬁnite,
(2) the morphism f ∗ : Br(Y ) → Br(X) is surjective,
(3) there exists some P ∈ Y (K) such that the ﬁber XP of f over P does not satisfy
weak approximation oﬀ S, and that ∏
v∈S XP (Kv) ̸= ∅.

Then X does not satisfy weak approximation with Brauer-Manin obstruction oﬀ S.

Proof. By Assumption (3), take a P0 ∈ Y (K) such that the ﬁber XP0 does not satisfy weak
approximation oﬀ S, and that ∏v∈S XP0(Kv) ̸= ∅. Then there exist a ﬁnite nonempty sub-
set S′ ⊂ ΩK\S and a nonempty open subset L = ∏v∈S′ Uv × ∏v /∈S′ XP0 (Kv) ⊂ XP0 (AK)

18 HAN WU

such that L ⋂ XP0 (K) = ∅. By Assumption (1), the set Y (K) is ﬁnite, so we can take a
Zariski open subset VP0 ⊂ Y such that VP0 (K) = {P0}. For any v ∈ S′, since Uv is open
in XP0(Kv) ⊂ f −1(VP0 )(Kv), we can take an open subset Wv of f −1(VP0 )(Kv) such that
Wv ∩ XP0 (Kv) = Uv. Consider the open subset N = ∏

v∈S′ Wv × ∏

v /∈S′ X(Kv) ⊂ X(AK),
then L ⊂ N. By the functoriality of Brauer-Manin pairing and Assumption (2), we have L ⊂
N ⋂ X(AK)
Br. So N ⋂ X(AK)
Br ̸= ∅. But N ⋂ X(K) = N ⋂ XP0 (K) = L ⋂ XP0 (K) = ∅,
which implies that X does not satisfy weak approximation with Brauer-Manin obstruction
oﬀ S. □

We use the following lemma to choose a dominant morphism from a given curve to P1.

Lemma 6.1.3. Given a nontrivial extension of number ﬁelds L/K, let C be a smooth,
projective, and geometrically connected curve deﬁned over K. Assume that the triple
(C, K, L) is of type I (Deﬁnition 4.0.3). For any ﬁnite K-subscheme R ⊂ P1\{0, ∞}, there
exists a dominant K-morphism γ : C → P1 such that γ(C(L)\C(K)) = {0} ⊂ P1(K),
γ(C(K)) = {∞} ⊂ P1(K), and that γ is étale over R.

Proof. Let K(C) be the function ﬁeld of C. For C(K) and C(L) are ﬁnite nonempty
sets and C(L)\C(K) ̸= ∅, by Riemann-Roch theorem, we can choose a rational function
φ ∈ K(C)
×\K × such that the set of its poles contains C(K), and that the set of its zeros
contains C(L)\C(K). This rational function φ gives a dominant K-morphism γ0 : C → P1

such that γ0(C(L)\C(K)) = {0} ⊂ P1(K) and γ0(C(K)) = {∞} ⊂ P1(K). We can choose
an automorphism ϕλ0 : P1 → P1, (u : v) ↦→ (λ0u : v) with λ0 ∈ K × such that the branch
locus of γ0 has no intersection with ϕλ0 (R). Let λ = (ϕλ0 )
−1 ◦ γ0. Then the morphism λ is
étale over R and satisﬁes other conditions. □

The following lemma is well known.

Lemma 6.1.4. Let C be a curve over a ﬁeld, and let B = C × P1. Then BrB = 0.

Proof. By [Gro68, III, Corollary 1.2], the Brauer group for a given curve over an algebraic
closed ﬁeld is zero. So Br(C × P1) ∼= Br(C) = 0. □

Deﬁnition 6.1.5. Let C be a smooth, projective, and geometrically connected curve
deﬁned over a number ﬁeld. We say that a morphism β : X → C is a Châtelet surface
bundle over the curve C, if

• X is a smooth, projective, and geometrically connected variety,
• the morphism β is faithfully ﬂat, and proper,
• the generic ﬁber of β is a Châtelet surface over the function ﬁeld of C.

Next, we construct Châtelet surface bundles over curves to give negative answers to Ques-
tions 1.2.

6.2. Non-invariance of weak approximation with Brauer-Manin obstruction. For
any quadratic extension of number ﬁelds L/K, and assuming Conjecture 4.0.1, Liang [Lia18,
Theorem 4.5] constructed a Châtelet surface bundle over a curve to give a negative answer
to Question 1.2.1. Assuming that the extension L/K is quadratic, he constructed a Châtelet
surface deﬁned over K such that the property of weak approximation is not invariant under
the extension of L/K. Then choosing a higher genus curve, he combined this Châtelet
surface with the construction method of Poonen [Poo10] to get the result. His method
only works for quadratic extensions. In this subsection, we generalize his result to any
extension L/K.

Theorem 6.2.1. For any nontrivial extension of number ﬁelds L/K, and any ﬁnite subset
T ⊂ ΩL, assuming that Conjecture 4.0.1 holds over K, there exists a Châtelet surface
bundle over a curve: X → C deﬁned over K such that

• X has a K-rational point, and satisﬁes weak approximation with Brauer-Manin
obstruction oﬀ ∞K,
• XL does not satisfy weak approximation with Brauer-Manin obstruction oﬀ T.

CHÂTELET SURFACES AND NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR 3-FOLDS19

Proof. Firstly, we will construct two Châtelet surfaces. Let S ⊂ ΩK be the set of all
restrictions of T on K. By Theorem 2.0.2, we can take a ﬁnite place v0 ∈ Ωf
K\(S ∪ 2K)
splitting completely in L. For the extension L/K, and S = {v0}, let V0 be the Châtelet
surface chosen as in Subsubsection 3.2.1. Then V0 deﬁned by y2 − az2 = P0(x) over K
having the properties of Proposition 3.2.1. Let P∞(x) = (1 − x
2)(x
2 − a), and let V∞
be the Châtelet surface deﬁned by y2 − az2 = P∞(x). By the argument in the proof of
Proposition 3.2.1, two degree-2 irreducible factors of P0(x) are prime to x
2 − a in K[x]. So,
the polynomials P0(x) and P∞(x) are coprime in K[x].

Secondly, we will construct a Châtelet surface bundle over a curve. Let ˜P∞(x0, x1) and
˜P0(x0, x1) be the homogenizations of P∞ and P0. Let (u0 : u1)×(x0 : x1) be the coordinates
of P1 × P1, and let s′ = u2
0 ˜P∞(x0, x1) + u2
1 ˜P0(x0, x1) ∈ Γ(P1 × P1, O(1, 2)
⊗2). For P0(x)
and P∞(x) are coprime in K[x], by Jacobian criterion, the locus Z ′ deﬁned by s′ = 0 in
P1 × P1 is smooth. Then the branch locus of the composition Z ′ ֒→ P1 × P1 pr1
→ P1, denoted
by R, is ﬁnite over K. By the assumption that Conjecture 4.0.1 holds over K, and Lemma
4.0.4, we can take a curve C deﬁned over K such that the triple (C, K, L) is of type I.
By Lemma 6.1.3, we can choose a K-morphism γ : C → P1 such that γ(C(L)\C(K)) =
{0} ⊂ P1(K), γ(C(K)) = {∞} ⊂ P1(K), and that γ is étale over R. Let B = C × P1.
Let L = (γ, id)
∗O(1, 2), and let s = (γ, id)
∗(s′) ∈ Γ(B, L
⊗2). For γ is étale over the
branch locus R, the locus Z deﬁned by s = 0 in B is smooth. Since Z is deﬁned by
the support of the global section s, it is an eﬀective divisor. The invertible sheaf L (Z ′)
on P1 × P1 is isomorphic to O(2, 4), which is a very ample sheaf on P1 × P1. And (γ, id)
is a ﬁnite morphism, so the pull back of this ample sheaf is again ample, which implies
that the invertible sheaf L (Z) on C × P1 is ample. By [Har97, Chapter III Corollary
7.9], the curve Z is geometrically connected. So the curve Z is smooth, projective, and
geometrically connected. By Lemma 6.1.4, the Brauer group Br(B) = 0. Let X be the zero
locus of (1, −a, −s) ∈ Γ(B, OB ⊕ OB ⊕ L
⊗2) ⊂ Γ(B, Sym2 E) in the projective space bundle
Proj(E) with the natural projection α : X → B. Using Proposition 5.0.2, the variety X is
smooth, projective, and geometrically connected. Let β : X α
→ B = C × P1 pr1
→ C be the
composition of α and pr1. Then β is a Châtelet surface bundle over the curve C.

At last, we will check that X has the properties.

We will show that X has a K-rational point. For any P ∈ C(K), the ﬁber β−1(P ) ∼= V∞.
The surface V∞ has a K-rational point (x, y, z) = (0, 0, 1), so the set X(K) ̸= ∅.
We will show that X satisﬁes weak approximation with Brauer-Manin obstruction oﬀ ∞K.
By Remark 3.0.4, the surface V∞ satisﬁes weak approximation. So, for the morphism
β, Assumption (3) of Lemma 6.1.1 holds. Since Conjecture 4.0.1 holds for the curve C,
using Lemma 6.1.1 for the morphism β, the variety X satisﬁes weak approximation with
Brauer-Manin obstruction oﬀ ∞K.

We will show that XL does not satisfy weak approximation with Brauer-Manin obstruc-
tion oﬀ T. By Proposition 5.0.2, the map α
∗
L : Br(BL) → Br(XL) is an isomorphism, so
β∗
L : Br(CL) → Br(XL) is an isomorphism. By the choice of the curve C and morphism β,
for any Q ∈ C(L)\C(K), the ﬁber β−1(Q) ∼= V0L. By Proposition 3.2.3, the surface V0L
does not satisfy weak approximation oﬀ T ∪ ∞L. For V0(L) ̸= ∅, by Lemma 6.1.2, the va-
riety XL does not satisfy weak approximation with Brauer-Manin obstruction oﬀ T ∪ ∞L.
So it does not satisfy weak approximation with Brauer-Manin obstruction oﬀ T. □

6.3. Non-invariance of the failures of the Hasse principle explained by the
Brauer-Manin obstruction. For extensions L/K of the following two cases, assum-
ing Conjecture 4.0.1, we construct Châtelet surface bundles over curves to give negative
answers to Question 1.2.2.

Theorem 6.3.1. For any number ﬁeld K, and any nontrivial ﬁeld extension L of odd
degree over K, assuming that Conjecture 4.0.1 holds over K, there exists a Châtelet surface
bundle over a curve: X → C deﬁned over K such that

• X is a counterexample to the Hasse principle, and its failure of the Hasse principle
is explained by the Brauer-Manin obstruction,

20 HAN WU

• XL is a counterexample to the Hasse principle, but its failure of the Hasse principle
cannot be explained by the Brauer-Manin obstruction.

Proof. Firstly, we will construct two Châtelet surfaces. By Theorem 2.0.2, we can take two
diﬀerent ﬁnite places v1, v2 ∈ Ωf
K\2K splitting completely in L. For the extension L/K,
and S = {v1, v2}, we choose an element a as in Subsubsection 3.0.1. For the extension
L/K, and S1 = {v1}, by Remark 3.0.7, choosing other parameters for the equation (1) as
in Subsubsection 3.3.1, we have a Châtelet surface V0 deﬁned by y2 − az2 = P0(x) over
K having the properties of Proposition 3.3.1. For the extension L/K, and S2 = {v2}, by
Remark 3.0.7, choosing other parameters for the equation (1) as in Subsubsection 3.1.1,
we have a Châtelet surface V∞ deﬁned by y2 − az2 = P∞(x) over K having the properties
of Proposition 3.1.1. By Remark 3.1.2, the polynomial P∞(x) is irreducible over K. For
P0(x) is a product of two degree-2 irreducible factors over K, the polynomials P0(x) and
P∞(x) are coprime in K[x].

Secondly, we will construct a Châtelet surface bundle over a curve. Let ˜P∞(x0, x1) and
˜P0(x0, x1) be the homogenizations of P∞ and P0. Let (u0 : u1)×(x0 : x1) be the coordinates
of P1 × P1, and let s′ = u2
0 ˜P∞(x0, x1) + u2
1 ˜P0(x0, x1) ∈ Γ(P1 × P1, O(1, 2)
⊗2). For P0(x)
and P∞(x) are coprime in K[x], by Jacobian criterion, the locus Z ′ deﬁned by s′ = 0 in
P1 × P1 is smooth. Then the branch locus of the composition Z ′ ֒→ P1 × P1 pr1
→ P1, denoted
by R, is ﬁnite over K. By the assumption that Conjecture 4.0.1 holds over K, and Lemma
4.0.4, we can take a curve C deﬁned over K such that the triple (C, K, L) is of type I.
By Lemma 6.1.3, we can choose a K-morphism γ : C → P1 such that γ(C(L)\C(K)) =
{0} ⊂ P1(K), γ(C(K)) = {∞} ⊂ P1(K), and that γ is étale over R. Let B = C × P1.
Let L = (γ, id)
∗O(1, 2), and let s = (γ, id)
∗(s′) ∈ Γ(B, L
⊗2). By the same argument as
in the proof of Theorem 6.2.1, the locus Z deﬁned by s = 0 in B is smooth, projective,
and geometrically connected; the Brauer group Br(B) = 0. Let X be the zero locus of
(1, −a, −s) ∈ Γ(B, OB ⊕ OB ⊕ L
⊗2) ⊂ Γ(B, Sym2 E) in the projective space bundle Proj(E)
with the natural projection α : X → B. By Proposition 5.0.2, the variety X is smooth,
projective, and geometrically connected. Let β : X → C be the composition of α and pr1.
Then β is a Châtelet surface bundle over the curve C.

At last, we will check that X has the properties.

We will show X(AK) ̸= ∅. For any P ∈ C(K), the ﬁber β−1(P ) ∼= V∞. By Proposi-
tion 3.1.1, the set V∞(A{v2}
K ) ̸= ∅. So X(A{v2}
K ) ̸= ∅. For v2 splits completely in L, take
a place v′
2 ∈ Ωf
L above v2, i.e. v′
2|v2 in L. Then Kv2 = Lv′
2. By Proposition 3.3.1, the
set V0(AL) ̸= ∅. Take a point Q ∈ C(L)\C(K), then the ﬁber β−1(Q) ∼= V0L. We have
X(Kv2) = XL(Lv′
2) ⊃ β−1(Q)(Lv′
2 ) ∼= V0((Lv′
2 ) ̸= ∅. So X(AK) ̸= ∅.
We will show X(AK)
Br = ∅. By Conjecture 4.0.1, the set C(K) is ﬁnite, and C(K) =
pr∞K (C(AK)
Br). By the functoriality of Brauer-Manin pairing, we have pr∞K (X(AK)
Br) ⊂⊔P ∈C(K) β−1(P )(A∞K
K ). But by Proposition 3.1.1, the set V∞(Kv2) = ∅, so we have
pr∞K (X(AK)
Br) ⊂ ⊔
P ∈C(K) β−1(P )(A∞K
K ) ∼= V∞(A∞K
K ) × C(K) = ∅, which implies that
X(AK)
Br = ∅.
So, the variety X is a counterexample to the Hasse principle, and its failure of the Hasse
principle is explained by the Brauer-Manin obstruction.

We will show XL(AL)
Br ̸= ∅. By Proposition 5.0.2, the map α
∗
L : Br(BL) → Br(XL) is
an isomorphism, so β∗
L : Br(CL) → Br(XL) is an isomorphism. By the functoriality of
Brauer-Manin pairing, the set XL(AL)
Br contains ⊔Q∈C(L)\C(K) β−1(Q)(AL) ∼= V0(AL) ×
(C(L)\C(K)), which is nonempty.
We will show X(L) = ∅. By the assumption that the degree [L : K] is odd, and v1 splitting
completely in L, the number ♯S1L is odd. By Proposition 3.3.1 and the global reciprocity
law explained in Remark 3.3.2, the set V0(L) = ∅. By Proposition 3.1.1, the set V∞(AL) = ∅.
Since each L-rational ﬁber of β is isomorphic to V0L or V∞L, the set X(L) = ∅.
So, the variety XL is a counterexample to the Hasse principle, but its failure of the Hasse
principle cannot be explained by the Brauer-Manin obstruction. □

CHÂTELET SURFACES AND NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR 3-FOLDS21

In the case when both ﬁelds K and L have real places, making use of these real place
information, and assuming the Stoll’s conjecture, we have the following theorem to give a
negative answer to Question 1.2.2

Theorem 6.3.2. For any number ﬁeld K having a real place, and any nontrivial ﬁeld
extension L/K having a real place, assuming that Conjecture 4.0.1 holds over K, there
exists a Châtelet surface bundle over a curve: X → C deﬁned over K such that

• X is a counterexample to the Hasse principle, and its failure of the Hasse principle
is explained by the Brauer-Manin obstruction,
• XL is a counterexample to the Hasse principle, but its failure of the Hasse principle
cannot be explained by the Brauer-Manin obstruction.

Proof. Firstly, we will construct two Châtelet surfaces. Take a real place v′
0 of L, and
let v0 ∈ ∞K be the restriction of v′
0 on K. By Theorem 2.0.2, we can take a ﬁnite place
v1 ∈ Ωf
K\2K splitting completely in L. For the extension L/K, and S = {v0, v1}, we
choose an element a as in Subsubsection 3.0.1. For the trivial extension K/K (respectively
the extension L/K), and S1 = {v0} (respectively S2 = {v1}), by Remark 3.0.7, choosing
other parameters for the equation (1) as in Subsubsection 3.1.1, we have a Châtelet surface
V0 (respectively V∞) deﬁned by y2 − az2 = P0(x) (respectively by y2 − az2 = P∞(x))
over K having the properties of Proposition 3.1.1. By Remark 3.1.2, the polynomial
P∞(x) is irreducible over Kv1. If the polynomials P0(x) and P∞(x) are not coprime, then
P0(x) = λP∞(x) for some λ ∈ K ×. By Remark 3.1.2, we choose another P∞(x)
′ to replace
P∞(x) so that the new polynomial P∞(x) is prime to P0(x).

Secondly, we will construct a Châtelet surface bundle over a curve. Let ˜P∞(x0, x1) and
˜P0(x0, x1) be the homogenizations of P∞ and P0. Let (u0 : u1)×(x0 : x1) be the coordinates
of P1 × P1, and let s′ = u2
0 ˜P∞(x0, x1) + u2
1 ˜P0(x0, x1) ∈ Γ(P1 × P1, O(1, 2)
⊗2). For P0(x) and
P∞(x) are coprime in K[x], by Jacobian criterion, the locus Z ′ deﬁned by s′ = 0 in P1 × P1

is smooth. Then the branch locus of the composition Z ′ ֒→ P1 × P1 pr1
→ P1, denoted by R,
is ﬁnite over K. By the assumptions that Conjecture 4.0.1 holds over K, and that the ﬁeld
L has a real place, using Lemma 4.0.4, we can take a curve C deﬁned over K such that the
triple (C, K, L) is of type II. By Lemma 6.1.3, we can choose a K-morphism γ : C → P1

such that γ(C(L)\C(K)) = {0} ⊂ P1(K), γ(C(K)) = {∞} ⊂ P1(K), and that γ is étale
over R. Let B = C × P1. Let L = (γ, id)
∗O(1, 2), and let s = (γ, id)
∗(s′) ∈ Γ(B, L
⊗2). By
the same argument as in the proof of Theorem 6.2.1, the locus Z deﬁned by s = 0 in B is
smooth, projective, and geometrically connected; the Brauer group Br(B) = 0. Let X be
the zero locus of (1, −a, −s) ∈ Γ(B, OB ⊕OB ⊕L
⊗2) ⊂ Γ(B, Sym
2 E) in the projective space
bundle Proj(E) with the natural projection α : X → B. By the same argument as in the
proof of Theorem 6.3.1, the variety X is smooth, projective, and geometrically connected.
Let β : X → C be the composition of α and pr1. Then β is a Châtelet surface bundle over
the curve C.

At last, we will check that X has the properties.

We will show X(AK) ̸= ∅. For any P ∈ C(K), the ﬁber β−1(P ) ∼= V∞. By Proposition
3.1.1, the set V∞(A{v1}
K ) ̸= ∅. So X(A{v1}
K ) ̸= ∅. For v1 splits completely in L, take a
place v′
1 ∈ Ωf
L above v1, i.e. v′
1|v1 in L. Then Kv1 = Lv′
1. By Proposition 3.1.1, the
set V0(Kv1) ̸= ∅. Take a point Q ∈ C(L)\C(K), then the ﬁber β−1(Q) ∼= V0L. We have
X(Kv1) = XL(Lv′
1) ⊃ β−1(Q)(Lv′
1 ) ∼= V0(Lv′
1 ) ̸= ∅. So X(AK) ̸= ∅.
By the same argument as in the proof of Theorem 6.3.1, the set X(AK)
Br = ∅. So, the
variety X is a counterexample to the Hasse principle, and its failure of the Hasse principle
is explained by the Brauer-Manin obstruction.

We will show XL(AL)
Br ̸= ∅. By Proposition 3.1.1, the set V0(A{v0}
K ) ̸= ∅ and V∞(Kv0 ) ̸= ∅.
By Proposition 5.0.2, the map β∗
L : Br(CL) → Br(XL) is an isomorphism. By our choice, the
space C(Kv0 ) ∼= C(Lv′
0 ) ∼= C(R) is connected. For any A ∈ Br(CL), since the evaluation
of A on C(Lv′ ) is locally constant for all v′ ∈ ΩL, it is constant on C(Kv0 ), so it is
constant on C(Lv′ ) for all v′ ∈ S1L. Take points P ∈ C(K) and Q ∈ C(L)\C(K). By the

22 HAN WU

functoriality of Brauer-Manin pairing and isomorphism of β∗
L : Br(CL) → Br(XL), the set
XL(AL)
Br ⊃ β−1(Q)(AS1L
L ) × ∏
v′∈S1L β−1(P )(Lv′ ) ∼= V0(AS1L
L ) × ∏
v′∈S1L V∞(Lv′ ) ̸= ∅.
We will show X(L) = ∅. By Proposition 3.1.1, the set V0(Kv0 ) = ∅, so the set V0(Lv′
0) =
V0(Kv0 ) = ∅. By Proposition 3.1.1, the set V∞(AL) = ∅. Since each L-rational ﬁber of β is
isomorphic to V0L or V∞L, the set X(L) = ∅.
So, the variety X is a counterexample to the Hasse principle, but its failure of the Hasse
principle cannot be explained by the Brauer-Manin obstruction. □

7. Explicit unconditional examples

Firstly, we will give explicit examples without assuming Conjecture 4.0.1 for Theorem 6.2.1,
Theorem 6.3.1 and Theorem 6.3.2. Secondly, when K = Q and L = Q(i), besides cases of
Theorem 6.3.1 and Theorem 6.3.2, we construct an explicit Châtelet surface bundle over a
curve in Subsection 7.4 to give a negative answer to Question 1.2.2.

7.1. An explicit unconditional example for Theorem 6.2.1. In the subsection, let
K = Q and L = Q(
√
3). We will construct an explicit Châtelet surface bundle over a curve
having properties of Theorem 6.2.1.

7.1.1. Choosing an elliptic curve. Let E be an elliptic curve deﬁned over Q by a homoge-
neous equation: w2
1w2 = w3
0 − 16w3
2
with homogeneous coordinates (w0 : w1 : w2) ∈ P2. This is an elliptic curve with complex
multiplication. Its quadratic twist E(3) is isomorphic to an elliptic curve deﬁned by a
homogeneous equation: w2
1w2 = w3
0 − 432w3
2 with homogeneous coordinates (w0 : w1 :
w2) ∈ P2. These elliptic curves E and E(3) deﬁned over Q, are of analytic rank 0. Then the
Tate-Shafarevich group X(E, Q) is ﬁnite, so E satisﬁes weak approximation with Brauer-
Manin obstruction oﬀ ∞K. The Mordell-Weil groups E(K) and E(3)(K) are ﬁnite, so E(L)
is ﬁnite. Indeed, the Mordell-Weil groups E(K) = {(0 : 1 : 0)} and E(L) = {(4 : ±4√
3 :
1), (0 : 1 : 0)}. So the triple (E, K, L) is of type I.

7.1.2. Choosing a dominant morphism. Let P2\{(0 : 1 : 0)} → P1 be a morphism over
Q given by (w0 : w1 : w2) ↦→ (w0 − 4w2 : w2). Composite with the natural inclusion
E\{(0 : 1 : 0)} ֒→ P2\{(0 : 1 : 0)}. We get a morphism E\{(0 : 1 : 0)} → P1, which can be
extended to a dominant morphism γ : E → P1 of degree 2. The morphism γ maps E(K)
to {∞} = {(1 : 0)}, and maps (4 : ±4√
3 : 1) to 0 point: (0 : 1). By Bézout’s Theorem
[Har97, Chapter I. Corollary 7.8] or Hurwitz’s Theorem [Har97, Chapter IV. Corollary 2.4],
the branch locus of γ is {(1 : 0), (2 3√
2 − 4 : 1), (2 3√
2e2πi/3 − 4 : 1), (2 3√
2e−2πi/3 − 4 : 1)}.

7.1.3. Construction of a Châtelet surface bundle. Let P∞(x) = (1 − x
2)(x
2 − 73), and let
P0(x) = (99x
2 + 1)(5428x
2/5329 + 1/5329). Notice that these polynomials P∞ and P0 are
separable. Let V∞ be the Châtelet surface given by y2 − 73z2 = P∞(x). As mentioned in
Example 3.2.5, let V0 be the Châtelet surface given by y2 − 73z2 = P0(x). Let ˜P∞(x0, x1)
and ˜P0(x0, x1) be the homogenizations of P∞ and P0. Let (u0 : u1) × (x0 : x1) be the
coordinates of P1×P1, and let s′ = u2
0 ˜P∞(x0, x1)+u2
1 ˜P0(x0, x1) ∈ Γ(P1×P1, O(1, 2)
⊗2). For
P0(x) and P∞(x) are coprime in K[x], by Jacobian criterion, the locus Z ′ deﬁned by s′ = 0
in P1×P1 is smooth. Then the branch locus of the composition Z ′ ֒→ P1×P1 pr1
→ P1, denoted
by R, is ﬁnite, and contained in P1\{(1 : 0)}. Let B = E × P1. Let L = (γ, id)
∗O(1, 2), and
let s = (γ, id)
∗(s′) ∈ Γ(B, L
⊗2). With these notations, we have the following lemma.

Lemma 7.1.1. The curve Z deﬁned by s = 0 in B is smooth, projective, and geometrically
connected.

Proof. For smoothness of Z, we need to check that the branch locus R does not intersect
with the branch locus of γ : E → P1. For R is contained in P1\{(1 : 0)}, we can assume the
homogeneous coordinate u1 = 1, then the point in R satisﬁes one of the following equations:
5329u2
0 − 537372 = 0, 389017u2
0 − 1 = 0, 27625536u4
0 + 157730624u2
0 + 5329 = 0. The

CHÂTELET SURFACES AND NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR 3-FOLDS23

polynomials of these equations are irreducible over Q. By comparing the degree [Q(u0) : Q]
with the branch locus of γ, we get the conclusion that these two branch loci do not intersect.
The same argument as in the proof of Theorem 6.2.1, the locus Z deﬁned by s = 0 in B is
geometrically connected. So it is smooth, projective, and geometrically connected. □

Let X be the zero locus of (1, −a, −s) ∈ Γ(B, OB ⊕ OB ⊕ L
⊗2) ⊂ Γ(B, Sym2 E) in the
projective space bundle Proj(E) with the natural projection α : X → B. By the same
argument as in the proof of Theorem 6.3.1, the variety X is smooth, projective, and
geometrically connected. Let β : X → E be the composition of α and pr1. Then it is a
Châtelet surface bundle over the curve E. For this X, we have the following proposition.

Proposition 7.1.2. For K = Q and L = Q(
√
3), the 3-fold X has the following properties.

• X has a K-rational point, and satisﬁes weak approximation with Brauer-Manin
obstruction oﬀ ∞K.
• XL does not satisfy weak approximation with Brauer-Manin obstruction oﬀ ∞L.

Proof. This is the same as in the proof of Theorem 6.2.1. □

The 3-fold X that we constructed, has an aﬃne open subvariety deﬁned by the following
equations, which is a closed subvariety of A5 with aﬃne coordinates (x, y, z, x
′, y′).
{y2 − 73z2 = (1 − x
2)(x
2 − 73)(x
′ − 4)
2 + (99x
2 + 1)(5428x
2/5329 + 1/5329)
y′2 = x
′3 − 16

7.2. An explicit unconditional example for Theorem 6.3.1. In the subsection, let
K = Q, and let ζ7 be a primitive 7-th root of unity. Let α = ζ7 + ζ−1
7 with the minimal
polynomial x
3 + x
2 − 2x − 1. Let L = Q(α). Then the degree [L : K] = 3. We will construct
an explicit Châtelet surface bundle over a curve having properties of Theorem 6.3.1.

7.2.1. Choosing an elliptic curve. Let E be an elliptic curve deﬁned over Q by a homoge-
neous equation: w2
1w2 = w3
0 − 343w0w2
2 − 2401w3
2
with homogeneous coordinates (w0 : w1 : w2) ∈ P2. This elliptic curve deﬁned over Q, is
of analytic rank 0, so it satisﬁes weak approximation with Brauer-Manin obstruction oﬀ
∞K. By computer calculation, we have the Mordell-Weil groups E(K) = {(0 : 1 : 0)} and
E(L) = {(7α
2 + 14α − 7 : 0 : 1), (7α
2 − 7α − 14 : 0 : 1), (−14α
2 − 7α + 21 : 0 : 1), (0 : 1 : 0)}.
So the triple (E, K, L) is of type I.

7.2.2. Choosing a dominant morphism. Let P2\{(1 : 0 : 0)} → P1 be a morphism over Q
given by (w0 : w1 : w2) ↦→ (w1 : w2). Composite with the natural inclusion E ֒→ P2\{(1 :
0 : 0)}. We get a morphism γ : E → P1, which is a dominant morphism of degree 3. The
morphism γ maps E(K) to {∞} = {(1 : 0)}, and maps E(L)\E(K) to {0} = {(0 : 1)}. By
Bézout’s Theorem [Har97, Chapter I. Corollary 7.8] or Hurwitz’s Theorem [Har97, Chapter
IV. Corollary 2.4], the branch locus of γ is {(1 : 0)} ⋃
{(u0 : 1)|27u4
0 +129654u2
0−5764801 =
0}.

7.2.3. Construction of a Châtelet surface bundle. Let P∞(x) = 14(x
4 − 89726), and let
P0(x) = (x
2 − 878755181)(5x
2 − 4393775906). Notice that these polynomials P∞ and
P0 are separable. As mentioned in Example 3.1.3 and Example 3.3.5, let V∞ be the
Châtelet surface given by y2 − 377z2 = P∞(x), and let V0 be the Châtelet surface given
by y2 − 377z2 = P0(x). Let ˜P∞(x0, x1) and ˜P0(x0, x1) be the homogenizations of P∞ and
P0. Let (u0 : u1) × (x0 : x1) be the coordinates of P1 × P1, and let s′ = u2
0 ˜P∞(x0, x1) +
u2
1 ˜P0(x0, x1) ∈ Γ(P1×P1, O(1, 2)
⊗2). For P0(x) and P∞(x) are coprime in K[x], by Jacobian
criterion, the locus Z ′ deﬁned by s′ = 0 in P1 × P1 is smooth. Then the branch locus of
the composition Z ′ ֒→ P1 × P1 pr1
→ P1, denoted by R, is ﬁnite and contained in P1\{(1 : 0)}.
Let B = E × P1. Let L = (γ, id)
∗O(1, 2), and let s = (γ, id)
∗(s′) ∈ Γ(B, L
⊗2). With these
notations, we have the following lemma.

24 HAN WU

Lemma 7.2.1. The curve Z deﬁned by s = 0 in B is smooth, projective, and geometrically
connected.

Proof. For smoothness of Z, we need to check that the branch locus R does not inter-
sect with the branch locus of γ : E → P1. For R is contained in P1\{(1 : 0)}, we can
assume the homogeneous coordinate u1 = 1, then the point in R satisﬁes one of the
following equations: 14u2
0 + 5 = 0, 44863u2
0 − 137894762198231040 = 0, 70345184u4
0 −
216218987126801139936u2
0+ 1 = 0. The polynomials of these equations are irreducible over
Q. By comparing these irreducible polynomials with the branch locus of γ, we get the
conclusion that these two branch loci do not intersect. The same argument as in the proof
of Theorem 6.2.1, the locus Z deﬁned by s = 0 in B is geometrically connected. So it is
smooth, projective, and geometrically connected. □

Let X be the zero locus of (1, −a, −s) ∈ Γ(B, OB ⊕ OB ⊕ L
⊗2) ⊂ Γ(B, Sym2 E) in the
projective space bundle Proj(E) with the natural projection α : X → B. By the same
argument as in the proof of Theorem 6.3.1, the variety X is smooth, projective, and
geometrically connected. Let β : X → E be the composition of α and pr1. Then it is a
Châtelet surface bundle over the curve E. For this X, we have the following proposition.

Proposition 7.2.2. For K = Q and L = Q(ζ7 + ζ−1
7 ), the 3-fold X has the following
properties.

• X is a counterexample to the Hasse principle, and its failure of the Hasse principle
is explained by the Brauer-Manin obstruction.
• XL is a counterexample to the Hasse principle, but its failure of the Hasse principle
cannot be explained by the Brauer-Manin obstruction.

Proof. This is the same as in the proof of Theorem 6.3.1. □

The 3-fold X that we constructed, has an aﬃne open subvariety deﬁned by the following
equations, which is closed subvariety of A5 with aﬃne coordinates (x, y, z, x
′, y′).
{
y2 − 377z2 = 14(x
4 − 89726)y′2 + (x
2 − 878755181)(5x
2 − 4393775906)
y′2 = x
′3 − 343x
′ − 2401

7.3. An explicit unconditional example for Theorem 6.3.2. In the subsection, let
K = Q and L = Q(
√
3). We will construct an explicit Châtelet surface bundle over a curve
having properties of Theorem 6.3.2.

7.3.1. Choosing an elliptic curve and a dominant morphism. Let E and γ : E → P1 be the
same as in Subsection 7.1. For E(R) is connected, the triple (E, K, L) is of type II.

7.3.2. Construction of a Châtelet surface bundle. Let P∞(x) = 5(x
4+805), and let P0(x) =
−5(x
4 + 115). Notice that these polynomials P∞ and P0 are irreducible. As mentioned in
Example 3.1.4 and Example 3.1.5, let V∞ be the Châtelet surface given by y2 + 23z2 =
P∞(x), and let V0 be the Châtelet surface given by y2 + 23z2 = P0(x). Let ˜P∞(x0, x1) and
˜P0(x0, x1) be the homogenizations of P∞ and P0. Let (u0 : u1)×(x0 : x1) be the coordinates
of P1 × P1, and let s′ = u2
0 ˜P∞(x0, x1) + u2
1 ˜P0(x0, x1) ∈ Γ(P1 × P1, O(1, 2)
⊗2). For P0(x)
and P∞(x) are coprime in K[x], by Jacobian criterion, the locus Z ′ deﬁned by s′ = 0 in
P1 × P1 is smooth. Then the branch locus of the composition Z ′ ֒→ P1 × P1 pr1
→ P1, denoted
by R, is ﬁnite, and contained in P1\{(1 : 0)}. Let B = E × P1. Let L = (γ, id)
∗O(1, 2), and
let s = (γ, id)
∗(s′) ∈ Γ(B, L
⊗2). With these notations, we have the following lemma.

Lemma 7.3.1. The curve Z deﬁned by s = 0 in B is smooth, projective, and geometrically
connected.

Proof. For smoothness of Z, we need to check that the branch locus R does not intersect
with the branch locus of γ : E → P1. For R is contained in P1\{(1 : 0)}, we can assume the
homogeneous coordinate u1 = 1, then the point in R satisﬁes one of the following equations:

CHÂTELET SURFACES AND NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR 3-FOLDS25

u2
0 − 1 = 0, 7u2
0 − 1 = 0. By comparing this locus with the branch locus of γ, these two
branch loci do not intersect. The same argument as in the proof of Theorem 6.2.1, the
locus Z deﬁned by s = 0 in B is geometrically connected. So it is smooth, projective, and
geometrically connected. □

Let X be the zero locus of (1, −a, −s) ∈ Γ(B, OB ⊕ OB ⊕ L
⊗2) ⊂ Γ(B, Sym2 E) in the
projective space bundle Proj(E) with the natural projection α : X → B. By the same
argument as in the proof of Theorem 6.3.1, the variety X is smooth, projective, and
geometrically connected. Let β : X → E be the composition of α and pr1. Then it is a
Châtelet surface bundle over the curve E. For this X, we have the following proposition.

Proposition 7.3.2. For K = Q and L = Q(
√
3), the 3-fold X has the following properties.

• X is a counterexample to the Hasse principle, and its failure of the Hasse principle
is explained by the Brauer-Manin obstruction.
• XL is a counterexample to the Hasse principle, but its failure of the Hasse principle
cannot be explained by the Brauer-Manin obstruction.

Proof. This is the same as in the proof of Theorem 6.3.2. □

The 3-fold X that we constructed, has an aﬃne open subvariety deﬁned by the following
equations, which is closed subvariety of A5 with aﬃne coordinates (x, y, z, x
′, y′).
{y2 + 23z2 = 5(x
4 + 805)(x
′ − 4)
2 − 5(x
4 + 115)
y′2 = x
′3 − 16

7.4. Exceptions. For Question 1.2.2, when the degree [L : K] is even and L has no real
place, besides cases of Theorem 6.3.1 and Theorem 6.3.2, we can give some unconditional
examples, case by case, to give negative answers to Question 1.2.2, although we do not
have a uniform way to construct them. In this subsection, we give an explicit example to
explain how it works for the case that K = Q and L = Q(i).

7.4.1. Choosing an elliptic curve. Let E be an elliptic curve deﬁned over Q by a homoge-
neous equation: w2
1w2 = w3
0 − 16w3
2
with homogeneous coordinates (w0 : w1 : w2) ∈ P2. This is an elliptic curve with complex
multiplication. Its quadratic twist E(−1) is isomorphic to an elliptic curve deﬁned by a
homogeneous equation: w2
1w2 = w3
0 + 16w3
2 with homogeneous coordinates (w0 : w1 : w2) ∈
P2. These elliptic curves E and E(−1) deﬁned over Q, are of analytic rank 0. Then the Tate-
Shafarevich group X(E, Q) is ﬁnite, so E satisﬁes weak approximation with Brauer-Manin
obstruction oﬀ ∞K. The Mordell-Weil groups E(K) and E(−1)(K) are ﬁnite, so E(L) is
ﬁnite. Indeed, the Mordell-Weil group E(K) = {(0 : 1 : 0)} and E(L) = {(0 : ±4i : 1), (0 :
1 : 0)}. So the triple (E, K, L) is of type I.

7.4.2. Choosing a dominant morphism. Let P2\{(1 : 0 : 0)} → P1 be a morphism over Q
given by (w0 : w1 : w2) ↦→ (w1 : 4w2). Composite with the natural inclusion E ֒→ P2\{(1 :
0 : 0)}, then we get a morphism γ : E → P1, which is a dominant morphism of degree 3.
The dominant morphism γ maps E(K) to {∞} = {(1 : 0)}, and maps (0 : ±4i : 1) to
(±i : 1). By Bézout’s Theorem [Har97, Chapter I. Corollary 7.8] or Hurwitz’s Theorem
[Har97, Chapter IV. Corollary 2.4], the branch locus of γ is {(1 : 0), (±i : 1)}.

7.4.3. Properties of Châtelet surfaces. Let P∞(x) = 2(x
4 − 10x
2 + 15), P0(x) = −2(5x
4 −
39x
2+75), and let P1(x) = P∞(x)+iP0(x). Notice that all those polynomials P∞, P0, P1 are
separable, and P1(x) = −2[x
2 − (5 + i)][(−1 + 5i)x
2 − 15i]. The two polynomials x
2 − (5 + i)
and (−1 + 5i)x
2 − 15i are irreducible over Q(i) (indeed, they are irreducible over Q(i)3).
Let V∞ be the Châtelet surface over Q given by y2 + 15z2 = P∞(x), and let V1 be the
Châtelet surface over Q(i) given by y2 + 15z2 = P1(x). With these notations, we have the
following lemmas.

26 HAN WU

Lemma 7.4.1. The Châtelet surface V∞ given by y2 + 15z2 = 2(x
4 − 10x
2 + 15), has a
Qv-point for all v ∈ ΩQ\{5}, but no Q5-point.

Proof. Suppose that v = ∞Q. Let x0 = 0. Then (−15, P∞(x0))v = (−15, 30)v = 1, which
implies that the surface V 0
∞ admits a R-point with x = 0.
Suppose that v = 2. For −15 ≡ 1 mod 8, by Hensel’s lemma, the element −15 is a square
in Q2. By Remark 3.0.1, the surface V∞ admits a Q2-point.
Suppose that v = 3. Let x0 = 2. Then (−15, P∞(x0))v = (−15, −18)v = (−15, 9)v(−15, −2)v =
1, which implies that the surface V 0
∞ admits a Q3-point with x = 2.
Suppose that v ∈ Ωf
Q\{2, 3, 5}. Take x0 ∈ Qv such that the valuation v(x0) < 0. Then by
Lemma 2.2.2, we have (−15, P∞(x0))v = (−15, 2)v = 1, which implies that V 0
∞ admits a
Qv-point with x = x0.
Suppose that v = 5. Then (−15, 2)v = −1. Let x ∈ Q5. If v(x) ≤ 0, then by Lemma
2.2.2, we have (−15, P∞(x))v = (−15, 2x
4)v = −1. If v(x) > 0, then by Lemma 2.2.2, we
have (−15, P∞(x))v = (−15, 30)v = −1. In each case, we have (−15, P∞(x))v = −1, which
implies that V 0
∞ has no Q5-point. By Remark 3.0.2, we have V∞(Q5) = ∅. □

Lemma 7.4.2. For any v′ ∈ ΩQ(i), the Châtelet surface V1 given by y2 + 15z2 = −2[x
2 −
(5 + i)][(−1 + 5i)x
2 − 15i], has a Q(i)v′-point.

Proof. For the only archimedean place is complex, we only need to consider ﬁnite places.
Suppose that v′ is a 2-adic place. For −15 ∈ Q×2
2 , by Remark 3.0.1, the surface V1 admits
a Q(i)v′-point.
Suppose that v′ = 3. For −2 ∈ Q×2
3 , we have (−15, −2)v′ = 1. By Lemma 2.2.2, we
have (−15, (−4 − i)(−1 − 10i))v′ = (−15, (1 + i)
2)v′ . Let x0 = 1. Then (−15, P1(x0))v′ =
(−15, −2(−4 − i)(−1 − 10i))v′ = (−15, (1 + i)
2)v′ = 1, which implies that V 0
1 admits a
Q(i)3-point with x = 1.
Suppose that v′|5, then Q(i)v′ ∼= Q5. By Lemma 2.2.2, we have (−15, −2(−5 + i)(−10 −
17i))v′ = (−15, −34)v′. Let x0 = 1 + i. Then (−15, P1(x0))v′ = (−15, −2(−5 + i)(−10 −
17i))v′ = (−15, −34)v′ = 1, which implies that V 0
1 admits a Q(i)v′ -point with x = 1 + i.
Suppose that v′|13, then Q(i)v′ ∼= Q13. Let x0 = 1. By Lemma 2.2.1, we have (−15, P1(x0))v′ =
(−15, −2(−4 − i)(−1 − 10i))v′ = 1, which implies that V 0
1 admits a Q(i)v′ -point with x = 1.
Suppose that v′ ∈ Ωf
Q(i)\{2, 3, 5, 13}. Take x0 ∈ Qv′ such that the valuation v′(x0) < 0.
By Lemma 2.2.2, we have (−15, P∞(x0))v′ = (−15, −2(−1 + 5i)x
4
0)v′ . By Lemma 2.2.1, we
have (−15, −2(−1 + 5i))v′ = 1, so (−15, P∞(x0))v′ = 1, which implies that V 0
1 admits a
Q(i)v′ -point with x = x0. □

For P1(x) is a product of two degree-2 irreducible factors, according to [Sko01, Proposition
7.1.1], the Brauer group Br(V1)/Br(Q(i)) ∼= Z/2Z. Furthermore, by Proposition 7.1.2 in
loc. cit, we take the quaternion algebra A = (−15, (−1 + 5i)x
2 − 15i) ∈ Br(V1) as a
generator element of this group. Then we have the equality A = (−15, (−1 + 5i)x
2 − 15i) =
(−15, −2(x
2 − (5 + i))) in Br(V1). With these notations, we have the following lemmas.

Lemma 7.4.3. For any v′ ∈ ΩQ(i) and any Pv′ ∈ V1(Q(i)v′ ),

invv′(A(Pv′ )) =
 {0 if v′ ̸= 3
1/2 if v′ = 3

Proof. By Remark 3.0.2, it suﬃces to compute the local invariant invv′ (A(Pv′ )) for all
Pv′ ∈ V 0
1 (Q(i)v′ ).

Suppose that v′ is an archimedean place or a 2-adic place or a 181-adic place. Then
−15 ∈ Q(i)
×2
v′ , so invv′ (A(Pv′ )) = 0 for all Pv′ ∈ V1(Q(i)v′ ).
Suppose that v′|5. Let x ∈ Q(i)v′ . If v′(x) ≤ 0, then by Lemma 2.2.2, we have (−15, (−1 +
5i)x
2−15i)v′ = (−15, −x
2)v′ = 1. If v′(x) > 0, then by Lemma 2.2.2, we have (−15, −2(x
2−
(5 + i)))v′ = (−15, 2i)v′ = 1. So invv′ (A(Pv′ )) = 0 for all Pv′ ∈ V 0
1 (Q(i)v′ ).
Suppose that v′ ∈ Ωf
Q(i)\{3, all 2-adic, 5-adic and 181-adic places}. Take an arbitrary Pv′ ∈
V 0
1 (Q(i)v′). If invv′ (A(Pv′ )) = 1/2, then (−15, (−1 + 5i)x
2 − 15i)v′ = −1 = (−15, −2(x
2 −

CHÂTELET SURFACES AND NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR 3-FOLDS27

(5 + i)))v′ at Pv′ . By Lemma 2.2.1, the ﬁrst and last equalities imply that v′((−1 + 5i)x
2 −
15i) and v′(x
2 − (5 + i)) are odd, so they are positive. Hence v′((−1 + 5i)x
2 − 15i −
(−1 + 5i)(x
2 − (5 + i))) = v′(−10 + 9i) > 0. But v′ ∤ 181, which is a contradiction. So
invv′ (A(Pv′ )) = 0.

Suppose that v′ = 3. Take an arbitrary Pv′ ∈ V 0
1 (Q(i)v′ ). If invv′ (A(Pv′ )) = 1, then
(−15, (−1 + 5i)x
2 − 15i)v′ = 1 = (−15, −2(x
2 − (5 + i)))v′ at Pv′ . For (−15, −1 + 5i)v′ = −1,
the ﬁrst equality implies that v′(x) > 0. Then by Lemma 2.2.2, we have (−15, x
2 − (5 +
i))v′ = (−15, −(5 + i))v′ = −1, so (−15, −2(x
2 − (5 + i)))v′ = (−15, −2)v′(−15, −5 − i)v′ =
−1, which is a contradiction. So invv′ (A(Pv′ )) = 1/2. □

Lemma 7.4.4. The Châtelet surface V1 has no Q(i)-rational point.

Proof. If there exists Q(i)-rational point P, by the global reciprocity law ∑
v∈ΩQ(i) invv(A(P )) =
0 in Q/Z. But from Lemma 7.4.3, this sum is 1/2, which is nonzero in Q/Z. So V1 has no
Q(i)-rational point. □

7.4.4. Construction of a Châtelet surface bundle. Let ˜P∞(x0, x1) and ˜P0(x0, x1) be the
homogenizations of P∞ and P0. Let (u0 : u1) × (x0 : x1) be the coordinates of P1 × P1,
and let s′ = (u2
0 + 2u2
1) ˜P∞(x0, x1) + u0u1 ˜P0(x0, x1) ∈ Γ(P1 × P1, O(1, 2)
⊗2). By Jacobian
criterion, the locus Z ′ deﬁned by s′ = 0 in P1 × P1 is smooth. Then the branch locus of
the composition Z ′ ֒→ P1 × P1 pr1
→ P1 is ﬁnite, and contained in P1\{(1 : 0), (±i, 1)}. Let
B = E × P1. Let L = (γ, id)
∗O(1, 2), and let s = (γ, id)
∗(s′) ∈ Γ(B, L
⊗2). With these
notations, we have the following lemma.

Lemma 7.4.5. The curve Z deﬁned by s = 0 in B is smooth, projective, and geometrically
connected.

Proof. For the branch locus of the composition Z ′ ֒→ P1 × P1 pr1
→ P1 is contained in
P1\{(1 : 0), (±i, 1)}, and the branch locus of γ : E → P1 is {(1 : 0), (±i, 1)}, they do
not intersect, which implies the smoothness of Z. The same argument as in the proof of
Theorem 6.2.1, the locus Z deﬁned by s = 0 in B is geometrically connected. So it is
smooth, projective, and geometrically connected. □

Let X be the zero locus of (1, −a, −s) ∈ Γ(B, OB ⊕ OB ⊕ L
⊗2) ⊂ Γ(B, Sym2 E) in the
projective space bundle Proj(E) with the natural projection α : X → B. By the same
argument as in the proof of Theorem 6.3.1, the variety X is smooth, projective, and
geometrically connected. Let β : X → E be the composition of α and pr1. Then it is a
Châtelet surface bundle over the curve E. For this X, we have the following proposition.

Proposition 7.4.6. For K = Q and L = Q(i), the 3-fold X has the following properties.

• X is a counterexample to the Hasse principle, and its failure of the Hasse principle
is explained by the Brauer-Manin obstruction.
• XL is a counterexample to the Hasse principle, but its failure of the Hasse principle
cannot be explained by the Brauer-Manin obstruction.

Proof. Let σ be the generator element of Galois group Gal(L/K). We will show X(AK) ̸= ∅.
By our construction, each K-rational ﬁber of β is isomorphic to V∞. By Lemma 7.4.1, the
set V∞(A{5}
K ) ̸= ∅. So X(A{5}
K ) ̸= ∅. For 5 splits completely in L, take a place v′ ∈ ΩL
above 5, i.e. v′|5 in L. Then Q5 ∼= Lv′. By Lemma 7.4.2, the set V1(AL) ̸= ∅. Since
V1 ⊔ σ(V1) ∼= ⊔

P ∈E(L)\E(K) β−1(P ) ⊂ XL, the set X(Q5) = X(Lv′) ⊃ V1(Lv′ ) ̸= ∅. So
X(AK) ̸= ∅.
We will show X(AK)
Br = ∅. For E(K) = pr∞K (C(AK )
Br), the functoriality of Brauer-
Manin pairing implies pr∞K (X(AK)
Br) ⊂ ⋃
P ∈E(K) β−1(P )(A∞K
K ). By Lemma 7.4.1, the
set V∞(Q5) = ∅, so pr∞K (X(AK)
Br) ⊂ ⋃
P ∈E(K) β−1(P )(A∞K
K ) ∼= V∞(A∞K
K ) = ∅, which
implies that X(AK)
Br = ∅.
So, the variety X is a counterexample to the Hasse principle, and its failure of the Hasse
principle is explained by the Brauer-Manin obstruction.

28 HAN WU

We will show XL(AL)
Br ̸= ∅. By Proposition 5.0.2, the map α
∗
L : Br(CL) → Br(XL) is an
isomorphism. By the functoriality of Brauer-Manin pairing, the set XL(AL)
Br contains
V1(AL), which is nonempty.
We will show X(L) = ∅. By Lemma 7.4.4, the set V1(L) = ∅, so also σ(V1)(L) = ∅. For
5 splits completely in L, the emptiness of V∞(Q5) implies V∞(AL) = ∅. Since X(L) ⊂⊔P ∈E(L) β−1(P )(L) ∼= V∞(L) ⋃ V1(L) ⋃ σ(V1)(L), the set X(L) = ∅.
So, the variety XL is a counterexample to the Hasse principle, but its failure of the Hasse
principle cannot be explained by the Brauer-Manin obstruction. □

The 3-fold X that we constructed, has an aﬃne open subvariety deﬁned by the following
equations, which is closed subvariety of A5 with aﬃne coordinates (x, y, z, x
′, y′).
{y2 + 15z2 = (x
4 − 10x
2 + 15)(y′2 + 32)/8 − (5x
4 − 39x
2 + 75)y′/2
y′2 = x
′3 − 16

Acknowledgements. The author would like to thank my thesis advisor Y. Liang for proposing the related

problems, papers and many fruitful discussions. The author was partially supported by NSFC Grant No.
12071448.
 References

[CF67] J. Cassels and A. Fröhlich, Algebraic number theory, Academic Press, 1967. ↑2
[CT10] J.-L. Colliot-Thélène, Zéro-cycles de degré 1 sur les solides de Poonen, Bull. Soc. Math.
France 138 (2010), 249–257 (French). ↑5
[CTPS16] J.-L. Colliot-Thélène, A. Pál, and A. Skorobogatov, Pathologies of the Brauer-Manin ob-
struction, Math. Z. 282 (2016), 799–817. ↑1.1, 3.0.3
[CTSSD87a] J.-L. Colliot-Thélène, J.-J. Sansuc, and S. Swinnerton-Dyer, Intersections of two quadrics
and Châtelet surfaces I, J. Reine Angew. Math. 373 (1987), 37–107. ↑1.1, 3.0.3, 3.2.1, 3.3.2
[CTSSD87b] , Intersections of two quadrics and Châtelet surfaces II, J. Reine Angew. Math. 374
(1987), 72–168. ↑1.1, 3.0.3, 3.2.1, 3.3.2
[Gro68] A. Grothendieck, Le groupe de Brauer III: Exemples et compléments. In: Dix exposés sur
la cohomologie des schémas, Advanced Studies in Pure Mathematics, vol. 3, North-Holland,
1968 (French). pp. 88-188. ↑6.1
[GZ86] B. Gross and D. Zagier, Heegner points and derivatives of L-series, Invent. Math. 84 (1986),
225–320. ↑4.0.2
[Har97] R. Hartshorne, Algebraic geometry, Graduate Texts in Mathematics, vol. 52, Springer-Verlag,
1997. ↑6.2, 7.1.2, 7.2.2, 7.4.2
[HS14] Y. Harpaz and A. Skorobogatov, Singular curves and the étale Brauer-Manin obstruction
for surfaces, Ann. Sci. Éc. Norm. Supér. 47 (2014), 765–778. ↑1.1
[Isk71] V. Iskovskikh, A counterexample to the Hasse principle for systems of two quadratic forms
in ﬁve variables, Mat. Zametki 10 (1971), 253–257. ↑1.3, 3.3
[Kol90] V. Kolyvagin, Euler systems. In: The Grothendieck festschrift II, Progress in Mathematics,
vol. 87, Birkhäuser, 1990. pp. 435-483. ↑4.0.2
[Kol91] , On the Mordell-Weil and the Shafarevich-Tate group of modular elliptic curves. In:
Proceedings of the international congress of mathematicians, Vol. I, Springer-Verlag, 1991.
pp. 429-436. ↑4.0.2
[Lia18] Y. Liang, Non-invariance of weak approximation properties under extension of the ground
ﬁeld, Preprint, arXiv:1805.08851v1 [math.NT] (2018). ↑1.3, 1.4.1, 3.2, 5, 6.2
[Man71] Y. Manin, Le groupe de Brauer-Grothendieck en géométrie diophantienne. In: Actes du Con-
grès International des Mathématiciens, Vol. 1, Gauthier-Villars, 1971 (French). pp. 401-411.
↑1.1
[Neu99] J. Neukirch, Algebraic number theory, Springer-Verlag, 1999. ↑2
[Poo09] B. Poonen, Existence of rational points on smooth projective varieties, J. Eur. Math. Soc. 11
(2009), 529–543. ↑1.3, 3, 3.2, 3.3
[Poo10] , Insuﬃciency of the Brauer-Manin obstruction applied to étale covers, Ann. of Math.
171 (2010), 2157–2169. ↑1.1, 1.4.3, 5, 5.0.2, 6.2
[Sch99] V. Scharaschkin, Local-global problems and the Brauer-Manin obstruction, Thesis, University
of Michigan (1999). ↑1.1, 4
[Ser73] J.-P. Serre, A course in arithmetic, Graduate Texts in Mathematics, vol. 7, Springer-Verlag,
1973. ↑2.2
[Ser79] , Local ﬁelds, Graduate Texts in Mathematics, vol. 67, Springer-Verlag, 1979. ↑2.1
[Sil09] J. Silverman, The arithmetic of elliptic curves, Graduate Texts in Mathematics, vol. 106,
Springer-Verlag, 2009. ↑4.0.5
[Sko01] A. Skorobogatov, Torsors and rational points, Cambridge Tracts in Mathematics, vol. 144,
Cambridge University Press, 2001. ↑1.1, 3, 3.0.2, 3.0.3, 3.2.1, 3.3, 3.3.1, 4, 7.4.3

CHÂTELET SURFACES AND NON-INVARIANCE OF THE BRAUER-MANIN OBSTRUCTION FOR 3-FOLDS29

[Sko99] , Beyond the Manin obstruction, Invent. Math. 135 (1999), 399–424. ↑1.1
[Sto07] M. Stoll, Finite descent obstructions and rational points on curves, Algebra Number Theory
1 (2007), 349–391. ↑1.1, 4, 4.0.1
[Wan96] L. Wang, Brauer-Manin obstruction to weak approximation on abelian varities, Israel J.
Math. 94 (1996), 189–200. ↑1.1

University of Science and Technology of China, School of Mathematical Sciences, No.96,
JinZhai Road, Baohe District, Hefei, Anhui, 230026. P.R.China.

Email address: wuhan90@mail.ustc.edu.cn
