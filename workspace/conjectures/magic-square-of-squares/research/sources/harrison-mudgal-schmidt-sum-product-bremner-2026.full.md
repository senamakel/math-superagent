<!-- source: https://arxiv.org/pdf/2603.06483 | converted from PDF -->

UNIFORM SUM-PRODUCT PHENOMENON FOR ALGEBRAIC
GROUPS AND BREMNER’S CONJECTURE

JOSEPH HARRISON, AKSHAT MUDGAL, HARRY SCHMIDT

Abstract. In this paper we combine methods from additive combinatorics and Diophan-
tine geometry to study the generalised sum-product phenomenon in algebraic groups. As
an application of this circle of ideas, we resolve a conjecture of Bremner on arithmetic pro-
gressions in coordinates of elliptic curves, along with various other generalisations studied
in the literature.
We also prove a uniform Bourgain–Chang-type sum-product estimate for general 1-
dimensional algebraic groups G over C. Using these ideas, we provide an alternative solution
to a problem of Bays–Breuillard. Furthermore, we show an Elekes–Szab´o type result in
the same setting for sets with small doubling, improving upon an earlier result of Bays–
Breuillard when G is not Ga. Our power saving here can be shown to be quantitatively
optimal.
We use a combination of deep, classical results in Diophantine geometry due to David–
Philippon, Laurent and Evertse–Schmidt–Schlickewei along with the recent breakthrough
work on the weak Polynomial Freiman–Ruzsa conjecture over integers due to Gowers–
Green–Manners–Tao.
 1. Introduction

Many questions in number theory concern an incongruence between two distinct arith-
metic structures. Bremner [5] made this observation in the course of his investigations into
the length of arithmetic progressions in the coordinates of the rational points of an elliptic
curve. Here, additive structure, represented by an arithmetic progression, and the group
structure on the elliptic curve should not correlate with each other, which led him to suspect
that the length of a possible arithmetic progression should be bounded solely in terms of the
rank of the curve. He confirmed his suspicions partly in work with Silverman and Tzanakis
[4].
Another example of this phenomenon is the infamous sum–product conjecture in combi-
natorial number theory due to Erd˝os–Szemer´edi [17]. This concerns expansion of finite sets
of integers under the operation of taking sums or products, a manifestation of the incom-
patibility of additive and multiplicative structure. Progress towards this type of problem
has led to a variety of applications in number theory and harmonic analysis.
A third example of this phenomenon concerns expansion of arbitrary sets of real numbers
under sufficiently non-degenerate polynomial maps. This was first investigated by Elekes–
R´onyai [13] and Elekes–Szab´o [14], and since their work, this subject has seen significant
activity, in part due to its connections to questions in combinatorial geometry and topics in

2020 Mathematics Subject Classification. 11B13, 11B25, 11B30, 11G05.
Key words and phrases. Bourgain–Chang sum-product result over algebraic groups, Bremner’s conjec-
ture, Mordell–Lang, Freiman–Ruzsa theorem, Elekes–Szab´o.
1arXiv:2603.06483v1  [math.NT]  6 Mar 2026
2 JOSEPH HARRISON, AKSHAT MUDGAL, HARRY SCHMIDT

model theory. In this paper, we unify these a priori disparate themes and prove effective,
quantitative results regarding them.
We first turn towards the question of Bremner which concerns upper bounds on possible
lengths of arithmetic progressions in the coordinates of the rational points of an elliptic
curve. Replacing the additive structure by the multiplicative one, one may similarly suspect
that the length of a geometric progression should be bounded, see work of Bremner–Ulas
[6]. Another line of inquiry, in the same spirit, concerns the length of the longest sequence
of consecutive squares in the coordinates of rational points on elliptic curves, see work of
Kamel–Sadek [28].
As a straightforward consequence of the methods discussed in this article, we confirm
Bremner’s speculation [5, §5] in the following general result.

Theorem 1.1. There is an effectively computable constant C ≥ 1 with the following prop-
erty. Let E be an elliptic curve in Weierstrass form

y2 = x
3 + ax + b, a, b ∈ Q, (1.1)

and let r be the rank of E(Q). Let X = {x(P ) : P ∈ E(Q)} and Y = {y(P ) : P ∈ E(Q)}.
Let A be either an arithmetic progression, a geometric progression or a set of the form

{u
2, (u + d)
2, (u + 2d)
2, . . . , (u + dl)
2},

with u, d ∈ Q, and l ∈ N. If A ⊆ X or A ⊆ Y , then |A| ≤ C 1+r.

We note that the constant C in Theorem 1.1 does not depend on a, b, and for families
of elliptic curves of bounded rank we obtain a uniform bound. It is to this day unclear
whether there exist elliptic curves of arbitrary large rank. Recently, an elliptic curve of rank
at least 29 was discovered [15, 16]. It is straightforward to see that Siegel’s theorem for
S-integral points [25, Theorem D.9.1] on elliptic curves implies that there can be no infinite
arithmetic or geometric sequence or sequence of squares in E(Q). However, it does not
provide a uniform bound, even for a fixed elliptic curve, since the number of primes that
need inverting depends on the particular sequence.
For arithmetic progressions, Garcia–Fritz and Pasten [21] prove a bound of the form C 1+r

with C depending on E but it is conceivable that their methods could lead to a uniform
bound, had they used a uniform version of Mordell–Lang, e.g., [11]. However, for geometric
progressions and consecutive squares no such general bounds seem to be known, even when
allowing a dependence on E. We prove a more general version of Theorem 1.1 (Corollary 2.2)
for correspondences and finite rank groups that applies to a plethora of similar sequences.
Theorem 1.1 can also be formulated in terms of rational points on a surface of general type
in a high dimensional projective space. As a consequence we determine the Zariski closure
of the rational points of certain projective surfaces (see Theorem A.1).
We now turn towards the sum-product phenomenon. Thus, given finite sets A, B ⊆ C,
we define the sumset and the product set as

A + B = {a + b : a ∈ A, b ∈ B} and A · B = {ab : a ∈ A, b ∈ B}.

It is expected that if |A + A| is small in terms of |A|, then A should be additively structured,
and if |A·A| is small in terms of |A|, then A should be multiplicatively structured. Speculat-
ing that these two types of structures should not coexist simultaneously, Erd˝os–Szemer´edi

SUM-PRODUCT PHENOMENON FOR ALGEBRAIC GROUPS AND BREMNER’S CONJECTURE 3

[17] conjectured that for any finite set A ⊆ C, either A + A or A · A must have size close to
|A|
2. More generally, writing

gA = {a1 + · · · + ag : a1, . . . , ag ∈ A} and A(g) = {a1 . . . ag : a1, . . . , ag ∈ A},

for any g ∈ N, Erd˝os–Szemer´edi conjectured the following.

Conjecture 1.2. For any g ∈ N, any ε > 0 and any set A ⊆ C, one should have

max{|gA|, |A(g)|} ≫g,ε |A|
g−ε.

A significant body of work addresses this conjecture, mostly focusing on the case when
g = 2. Some of the highlights in this setting have been the works of Elekes [12] and Solymosi
[41], who used geometric insights to provide short proofs of strong sum-product estimates.
The current best known result here arises from some very recent work of Cushman [10], who
employed incidence geometric and additive combinatorial methods to prove that

max{|2A|, |A(2)|} ≫ε |A| 4
3 + 10
4407 −ε

for all sets A ⊆ R and all ε > 0.
One can interpret the sum-product phenomenon as a disruption of structure between two
non-isogenous algebraic groups. Indeed, one can set Gm = (C∗, ×) and Ga = (C, +) and
take C to be the correspondence whose complex points are of the form (x, x) for x ∈ Gm(C).
See §3 for a brief introduction about algebraic groups and correspondences between them.
We let π1 : C → Gm and π2 : C → Ga be the standard projection maps. Given a finite set
A ⊆ Gm(C), we write C(A) = ⋃

x∈A π2(π−1
1 (x)).

Note that C(A) is a subset of Ga(C). The sum-product phenomenon is now equivalent to
saying that for any finite A ⊆ Gm(C), either |A + A| or |C(A) + C(A)| must be much larger
than |A|.
In a very nice paper, Bays–Breuillard [1] employed a model theoretic approach to gener-
alise this circle of ideas to a much more broader family of algebraic groups. In particular,
given 1-dimensional, connected, non-isogenous algebraic groups G and H over C and given
some algebraic correspondence C between G and H of degree d, Bays–Breuillard
1 proved
that there exists some δ = δ(G, H, C) > 0 such that for any finite set A ⊆ G, one has

max{|A + A|, |C(A) + C(A)|} ≫G,H,C |A|
1+δ. (1.2)

In contrast to the g = 2 setting of Conjecture 1.2, much less is known about the case
when one requires unbounded expansion, that is, given any real number k > 1, one wishes
to find some 1 ≤ g ≪k 1 such that

max{|gA|, |A(g)|} ≫k |A|
k (1.3)

holds for all finite sets A ⊆ C. While incidence geometric methods seem to work quite
effectively when k ≤ 2, they do not seem to give any results when k > 2. In a breakthrough
paper, Bourgain–Chang [3] employed intricate harmonic analytic techniques along with a

1Bays–Breuillard [1] actually proved that for non-constant rational maps f1 : G → C and f2 : H → C,
and all finite sets A ⊆ C, one either has |f −1
1 (A)+f −1
1 (A)| ≥ c|A|1+δ or |f −1
2 (A)+f −1
2 (A)| ≥ c|A|1+δ, where
c, δ > 0 are constants depending on G, H, f1 and f2. This can be written in the framework of correspondences
by considering the correspondence given by an irreducible component of {(x, y) ∈ G × H : f1(x) = f2(y)}.

4 JOSEPH HARRISON, AKSHAT MUDGAL, HARRY SCHMIDT

clever arithmetic lemma to prove that (1.3) holds for all finite sets A ⊆ Q. Their work was
subsequently simplified and quantitatively improved by P´alv¨olgyi–Zhelezov [36], giving the
best known bounds for g in terms of k for this problem. These ideas have since been extended
by replacing the sumset gA by other measures of additive structure. In particular, Hanson–
Roche-Newton–Zhelezov [24] proved an analogue of (1.3) with the sumset gA replaced by the
shifted product set (A + 1)
(g). This has been further generalised by the second author [35],
who proved analogues of (1.3) with gA first replaced by the sumset φ1(A) + · · · + φg(A) and
then by the product set φ1(A) . . . φg(A), for suitably chosen polynomials φ1, . . . , φg ∈ Z[x]
with bounded degree.
All the aforementioned results in [3, 36, 24, 35] crucially employed properties about prime
factorisation of integers, and subsequently do not generalise to sets of real numbers. In fact,
an important problem in this area was to prove (1.3) for sets A ⊆ R. Building on earlier
work of Chang [7], the second author [34] utilised results from diophantine geometry to
prove this conditionally on an infamous conjecture in additive combinatorics known as the
weak polynomial Freiman–Ruzsa conjecture over Z. The latter has now been resolved in
the spectacular work of Gowers–Green–Manners–Tao [22].
Our main result on the generalised sum-product phenomenon is a Bourgain–Chang type
unbounded expansion result in the vastly broader setting of 1-dimensional, connected alge-
braic groups over C.

Theorem 1.3. Given integers k ≥ 1 and d ≥ 2, there exists an integer g ≥ 1 such that
the following holds. Let G and H be algebraic groups of dimension 1, and let C1, · · · , Cg be
correspondences of degree d between G and H. Suppose no Ci is a translate of an algebraic
subgroup, and suppose that G is not isomorphic to Ga. Then for all finite, non-empty sets
A ⊆ G, one has max{|gA|, |C1(A) + · · · + Cg(A)|} ≫d,k |A|
k.

Setting G = Gm and H = Ga, we let Ci be given by the graph of the inclusion C∗ ↪→ C.
The conclusion of Theorem 1.3 then immediately implies (1.3) for arbitrary finite sets A ⊆ C.
Similarly setting G = Gm and H = Gm or Ga and setting Ci to be given by the graph of
(x, φi(x)) in G×H for suitably chosen polynomials φ1, . . . , φg delivers the following corollary.

Corollary 1.4. For all integers k ≥ 2, there exists an integer g ≥ 2 such that the following
holds. For any non-constant φ1, . . . , φg ∈ C[x] with degree at most d and any finite set
A ⊆ C, one has max{|A
(g)|, |φ1(A) + · · · + φg(A)|} ≫d,k |A|k.

Moreover, if each φi(x) for 1 ≤ i ≤ g is not of the form axn for any a ∈ C and any n ∈ N,
then we also have max{|A
(g)|, |φ1(A) . . . φg(A)|} ≫d,k |A|
k.

This recovers the results of [24, 35] qualitatively in the much more general setting where
A ⊆ C instead of A ⊆ Q and the polynomials φ1, . . . , φg are allowed to have complex
coefficients instead of rational coefficients. We defer further applications of our methods,
including an alternative proof of a conjecture of Bays–Breuillard, to §2.
We also consider problems concerning expansion in the image set of polynomials as well as
intersection of varieties with discrete boxes in algebraic groups. This relates to Elekes–Szab´o
and Elekes–R´onyai type problems. We briefly describe the former, and so, given n ≥ 3 and

SUM-PRODUCT PHENOMENON FOR ALGEBRAIC GROUPS AND BREMNER’S CONJECTURE 5

some polynomial P ∈ C[x1, . . . , xn], when is it the case that for any finite, non-empty set
A ⊆ C, one has
 |{(a1, . . . , an) ∈ An : P (a1, . . . , an) = 0}| ≪ |A|
n−1−η (1.4)

for some constant η > 0? Such a characterisation was first studied by Elekes–Szab´o [14],
and since then, has seen a flurry of activity, in part due to its connections to a variety of
combinatorial geometric problems [38, 37, 42] as well as to model theoretic results [9, 1, 8].
In their aforementioned work, Bays–Breuillard [1] introduced a model theoretic approach
to this question, thus generalising the above results for irreducible algebraic sets in C
n.
They further noted that upon restricting to a special family of sets A ⊆ C, one can obtain
power saving of the shape (1.4) for a much broader collection of varieties. In particular, in
the setting of a 1-dimensional, complex, connected algebraic group G, they proved that for
any subvariety V ⊆ G
n which is not a coset of a subgroup, there exist constants ε, η > 0
depending only on G and V such that for any finite set A ⊆ G satisfying |A + A| ≤ |A|
1+ε,
one has |An ∩ V| ≪G,V |A|
dim(V)−η. (1.5)

It is natural to ask what is the best possible value of η that is admissible in (1.5). When
G is not isomorphic to Ga, we resolve this question.

Theorem 1.5. Let G be a connected algebraic group over C of dimension 1. Suppose that
G is not isomorphic to Ga. Let A ⊆ G be a finite set such that |A + A| ≤ K|A| for some
K ≥ 1. Then for any irreducible subvariety V ⊆ G
g, that is not a translate of an algebraic
subgroup of Gg, one has
 |V ∩ A
g| ≪g,deg(V) K C + |A|dim(V)−1,

where C > 0 is some constant depending only on deg(V) and g.

In particular, when G is not isomorphic to Ga and V is not a translate of an algebraic
subgroup, there exists some ε > 0 depending only on V and g, such that whenever |A + A| ≤
|A|
1+ε, one has |V ∩ A
g| ≪g,deg(V) |A|dim(V)−1.

We further note that this upper bound is of the right order.

Example 1.6. Let G = Gm and g = 3. The variety V defined by the polynomial

P (X1, X2, X3) = X2X3 − X1 + 1 (1.6)

contains the translates X2X3 = γ, X1 = γ + 1 of the algebraic subgroup X2X3 = 1, X1 = 1,
for any γ ̸∈ {−1, 0}. Setting

A = {γi : −N ≤ i ≤ N } ∪ {γ + 1},

it is easy to see that for all N ≥ 3, we have |V ∩ A
3| ≫ |A| and |A · A| ≤ 3|A|. However, V
is not a translate of an algebraic subgroup.

In fact, our methods deliver even stronger upper bounds that depend on the largest
dimension of a maximal translate of an algebraic subgroup contained in V, see Theorem 2.6
for further details.

6 JOSEPH HARRISON, AKSHAT MUDGAL, HARRY SCHMIDT

We also note that while previous approaches to Elekes–Szab´o type problems employed
combinatorial geometric methods or model theory, our own approach utilises a novel inter-
action between Mordell–Lang and S-unit type results along with recent developments in
additive combinatorics involving Freiman–Ruzsa type results.
One can similarly consider expansion in the image set of polynomials, that is, given some
polynomial P ∈ C[x1, . . . , xn] and some finite set A ⊆ C, when is the set

P (A, . . . , A) = {P (a1, . . . , an) : a1, . . . , an ∈ A}

significantly larger than A. The first result in this direction is due to Elekes–R´onyai [13]
who proved that either P ∈ C[x, y] is degenerate, in the sense that P = h(f (x) + g(y))
or P = h(f (x)g(y)) for some univariate polynomials f, g, h, or one has |P (A, A)| ≫ |A|1+η

for every finite A ⊆ C, with η > 0 being an absolute constant. There have been various
subsequent quantitative improvements, as well as explorations of cases where, as before, one
restricts to a special family of sets A in order to widen the choices for P and get better
quantitative values of η, see [1, 26, 34] as well as [24, 35] for related sum-product type
problems.
Our main result in this direction is a significant generalisation of the above result in the
wider setting of algebraic groups. In order to state this, we will need the following definition.

Definition 1.7. Let G be a 1-dimensional, connected algebraic group over C, and let B be
a projective variety of positive dimension. Let π1 : Gg × B → G
g and π2 : Gg × B → B be
the canonical projection maps. We call an irreducible subvariety V ⊆ Gg × B degenerate,
if there exists a connected algebraic group H ⊆ G
g of positive dimension, and a proper
subvariety W ⊊ Gg/H × B such that
 V = π−1
H (W),

for the projection πH : G
g ×B → Gg/H ×B. If V is not degenerate, we call V non-degenerate.

An example of a degenerate subvariety is given by the equation P (X1, X2, X3) = t, where
P is given by (1.6). An example of a non-degenerate subvariety is provided after the state-
ment of Theorem 1.8 below.
With this in hand, we state our result as follows.

Theorem 1.8. Let G, B, π1 and π2 be as in Definition 1.7, with G not isomorphic to Ga.
Let V ⊆ G
g × B be non-degenerate of dimension g and degree d, and such that π1 and π2
restricted to V are dominant. Let A ⊆ G be a finite, non-empty set such that |A+A| ≤ K|A|.
Then for all X ⊆ A, we have

|π2((X g × B) ∩ V)| ≫d,g |X|
g

K Od,g(1) . (1.7)

As an example, one may set G = Gm, B = P1 and the variety V to be defined by the
equation P (x1, . . . , xg) = t, where P ∈ C[x1, . . . , xg] is some polynomial. We refer to P as
non-degenerate with respect to G
g if the variety V is non-degenerate. One can see that this
is equivalent to the fact that P (x) ̸= F (m1(x), . . . , mg−1(x)) for any choice of monomials
m1, . . . , mg−1 ∈ C[x1, . . . , xg] and any F ∈ C[y1, . . . , yg−1]. In this case, we have

π2((A
g × B) ∩ V) = P (A, . . . , A).

SUM-PRODUCT PHENOMENON FOR ALGEBRAIC GROUPS AND BREMNER’S CONJECTURE 7

Thus (1.7) implies that for any finite set A ⊆ C
∗ satisfying |A · A| ≤ K|A|, one has

|P (A, . . . , A)| ≫d,g |A|
g

K Od,g(1) . (1.8)

The lower bound in (1.8) was proved in [34] conditional on the weak PFR conjecture over
Z. In fact, Theorem 1.8 can be seen as a generalisation of the results from [34] to the much
broader setting of varieties in 1-dimensional algebraic groups over C.
Apart from having applications to various sum-product type questions, a nice aspect of
this notion of degeneracy is that it is optimal. In particular, if a polynomial P is degenerate
in the above sense, then [34, Proposition 1.2] implies that for any finite A ⊊ Z with |A · A| ≤
K|A| one has |P (A, . . . , A)| ≪P K OP (1)|A|
g−1.
Furthermore, the lower bound in (1.7) is almost optimal in the sense that it matches the
trivial upper bound |X|
g up to factors of K Od,g(1).
We note that in some of our results, including Theorem 1.8, we assume that the algebraic
group G is not isomorphic to Ga. In fact, this is a necessary condition for many of these to
hold. For example, Theorem 1.8 is not true for the case when G = Ga.

Example 1.9. Let P (x, y, z) = xy + yz + zx. One can show that this polynomial is non-
degenerate with respect to G3
a, see Appendix B. Moreover, the set A = {1, 2, . . . , N } is a
subset of Ga with |A + A| ≤ 2|A|. Finally, |P (A, A, A)| ≪ N 2 = |A|2 implying that a
conclusion akin to (1.8) in this case fails to hold true.

It is worth mentioning that Theorem 1.8 can be employed to prove its counterpart where
we replace the condition that A has a small sumset with A lying in a subgroup of small
rank, see Theorem 4.2. In particular, given some subgroup Γ ⊆ G of rank r and some finite
set Y ⊆ Γ, Theorem 1.8 implies that one must have

|π2((Y g × B) ∩ V)| ≫d,g |Y |
g

2Od,g(r) . (1.9)

Indeed, let Γ be generated by γ1, . . . , γr. Now, given any finite set Y ⊆ Γ, we can find some
L ∈ N such that Y ⊆ A, where A = {n1γ1 + · · · + nrγr : |n1|, . . . , |nr| ≤ L}. Moreover,
note that |A + A| ≤ 2
r|A|. We may now apply Theorem 1.8 to obtain (1.9). Furthermore,
this means that we may deduce Theorem 1.1 and its generalisation Corollary 2.2 via a
combination of inequality (1.9) and Proposition 5.1.
An important step towards proving our results is that the above implication can be roughly
reversed as well. We perform this reversal by combining the recent resolution of the weak
polynomial Freiman–Ruzsa conjecture due to Gowers–Green–Manners–Tao [22] along with
various additive combinatorial techniques and the fact that a finite subgroup of an algebraic
group has a uniformly bounded number of generators, which is a simple consequence of its
Lie theory.
Thus, it suffices to work in the setting where our sets are lying in subgroups of bounded
rank. One of our key results here is Theorem 4.2, whose conclusion is also recorded in
(1.9). This is where a significant portion of our input from Diophantine geometry comes in,
including utilisation of a uniform version of Mordell–Lang by David–Philippon [11] and the
S-unit bounds by Evertse–Schlickewei–Schmidt [18].
A third step that is required to prove our sum-product results such as Theorem 1.3, in-
volves showing that an auxiliary variety, which captures the movement of additive structure

8 JOSEPH HARRISON, AKSHAT MUDGAL, HARRY SCHMIDT

through the correspondences, is non-degenerate in the sense of Definition 1.7. This is pre-
cisely the content of Proposition 5.1. For the proof, which can be found in section 5, we
work on the tangent space of our algebraic groups. We note that Proposition 5.1, when
combined with Theorem 4.2, implies a suitable variant of Theorem 1.3 which holds for sets
contained in finite rank subgroups, see Theorem 2.1. The latter is already sufficient for our
applications to Bremner’s conjecture.
There is little doubt in the authors minds that the slick interaction of Diophantine ge-
ometry with additive combinatorics that is apparent here seems to suggest that correspon-
dences between algebraic groups present a very suitable framework to conceptualise the
sum-product phenomenon. One way of viewing this interaction is that the weak polynomial
Freiman–Ruzsa conjecture over Z is a statement concerning simply addition in Z
r. The
latter can be embedded into algebraic groups via rank r groups in a myriad ways. This
is combined with the algebraic structure that is implicitly present in Ga, Gm and elliptic
curves. Ultimately, the Mordell–Lang conjecture tells us how the group arithmetic interacts
with the Zariski-topology of the groups. This is especially convincing, if we remember the
special role played by isogenies as these are precisely the maps that respect both the alge-
braic and the group structure. Any correspondence that is not a translate of an algebraic
subgroup should destroy the approximate group structure of any finite set as it transports
the set from one group law to another.

Outline. We will present some further applications of our ideas in §2. We use §3 to give
a brief introduction about algebraic groups and correspondences, as well as record some
consequences of the uniform version of Mordell–Lang by David–Philippon [11] and the S-
unit bounds by Evertse–Schlickewei–Schmidt [18]. We dedicate §4 to proving Theorem 4.2,
and in §5, we will prove Proposition 5.1. We use §6 to prove the additive combinatorial
structural results that we require for the proofs of our results. Finally in §7, we provide all
the proofs of our results from §1 and §2. In Appendix A, we give some applications of our
results to Diophantine equations. Moreover, we make some brief remarks about properties
of degenerate polynomials in Appendix B.

Notation. We use Vinogradov notation. Thus we write X ≪z Y to mean that |X| ≤ CY
where C > 0 is some constant depending on the parameter z. We write X = O(Y ) to mean
X ≪ Y , and we write X ≍ Y to mean X ≪ Y ≪ X. We will often write A ⊆ G for a finite
set A and an algebraic group G. In this case we identify (by abuse of notation) A with a
0-dimensional algebraic subvariety consisting of the points of A with multiplicity 1.

Acknowledgements. The second author is supported by a Leverhulme early career fel-
lowship ECF-2025-148.
 2. Further Applications

2.1. Generalised Bremner. We mention a generalised version of Theorem 1.1 for corre-
spondences between algebraic groups. We first record an expansion version for correspon-
dences.

Theorem 2.1. For all integers d ≥ 1 and g ≥ 2, there is a positive constant 0 < c(d, g) < 1
with the following property. Let C1, · · · , Cg be correspondences of degree d between algebraic
groups G and H of dimension 1. Suppose no Ci is a translate of an algebraic subgroup and

SUM-PRODUCT PHENOMENON FOR ALGEBRAIC GROUPS AND BREMNER’S CONJECTURE 9

that G is not isomorphic to the additive group Ga. Let Γ ⊆ G(C) be a subgroup of finite
rank r. Then for any finite subset A ⊆ Γ, one has

|C1(A) + · · · + Cg(A)| ≥ c(d, g)
1+r|A|
g.

We note that the theorem is slightly asymmetric as we can not allow G to be isomorphic
to Ga. This is indeed necessary as for example Γ = Z, H = Gm and ∆ the diagonal as
described above shows that if we drop that assumption that would imply that any set in Z
has big product set, which is wrong.
It is also worth noting that fixing an elliptic curve E over a number field K, there are
only finitely many elliptic curves over K, that are isogenous to it, even over an algebraic
closure. This is a consequence of Faltings’s famous theorem [19], later significantly improved
by Masser–W¨ustholz [31], which shows that, even for a fixed number field, our theorems
apply to a vast zoo of non-isogenous algebraic groups.
Given k ∈ N, we define a proper generalised arithmetic progression of rank k to be a set
P of the form P = {P0 + ℓ1P1 + · · · + ℓkPk : 0 ≤ ℓi ≤ Li − 1}, (2.1)

where P0, . . . , Pk ∈ H and L1, . . . , Lk ≥ 2 are integers and one has |P | = L1 . . . Lk. These
sets play a crucial role in additive combinatorics and number theory since they act as an
important family of sets that exhibit additive structure. With this in hand, we now prove
our main result on Bremner’s conjecture and related questions.

Corollary 2.2. For all integers d ≥ 1 there exists a constant D = D(d) with the following
property. Let G be either Gm or an elliptic curve E, and let C be a correspondence of degree
at most d between G and an algebraic group H of dimension 1, that is not the translate of
an algebraic subgroup. Then for any subgroup Γ ⊆ G(C) of rank r, a proper generalised
arithmetic progression P of rank k in C(Γ) satisfies

|P | ≤ D1+r.

Theorem 1.1 follows in a straightforward manner from the above result, see §7. Corollary
2.2 also gives a more general and uniform version of [21, Theorem 6.1].
A nice aspect of our upper bound is that it is completely independent of the rank k of
the progression. Moreover, generalised arithmetic progressions are indeed a strictly more
general pattern. For example, the generalised arithmetic progression P ′ as described in (2.1)
can not be covered by fewer than C k arithmetic progressions, for some constant C > 1, but
we still obtain a uniform upper bound of the form |P ′| ≤ D1+r for some 0 < D ≪d 1 which
is independent of k.

2.2. Sum-product phenomenon. Returning to the generalised sum-product phenome-
non, Bays–Breuillard [1] speculated that the exponent δ in their result recorded in (1.2)
should be independent of G and H. Significantly generalising this model-theoretic and
incidence-geometric framework, Chernikov–Peterzil–Starchenko [8] confirmed the specula-
tion of Bays–Breuillard in a quantitative sense. In particular, they proved that δ = 1/21
is admissible in (1.2). As an application of our methods, we prove an asymmetric, uniform
version of (1.2), thus confirming the speculation of Bays–Breuillard via a very different set
of techniques.

10 JOSEPH HARRISON, AKSHAT MUDGAL, HARRY SCHMIDT

Theorem 2.3. Given d ∈ N, there exists some constant D = D(d) > 0 such that the
following is true. Let δ > 0, let G and H be connected algebraic groups of dimension 1 with
G not isomorphic to Ga, and let C be an algebraic correspondence between G and H of degree
d ≥ 2 that is not the translate of an algebraic subgroup. Then for any finite, non-empty set
A ⊆ G, one has either

|A + A| > |A|
1+δ or |C(A) + C(A)| ≥ D−1|A|
2−Dδ. (2.2)

Indeed, Theorem 2.3 implies that δ = 1/(D + 1) is admissible in (1.2). While this choice
of δ is much smaller than 1/21, the main novelty of our result lies in the asymmetry between
the lower bounds for |A + A| and |C(A) + C(A)| in (2.2). For instance, if we set G = Gm and
H = Ga or Gm and the correspondence C to be given by the graph of y = φ(x) for some
suitable polynomial φ ∈ C[x], we obtain the following corollary.

Corollary 2.4. Let A ⊆ C be a finite set, let d ≥ 1 be an integer, let K ≥ 1 and let φ ∈ C[x]
have deg φ = d. If |A · A| ≤ K|A|, then

|φ(A) + φ(A)| ≫d |A|
2/K D (2.3)

where D > 0 is some constant depending on d. Moreover, if φ(x) is not of the form cxd for
any c ∈ C, then we also have
 |φ(A) · φ(A)| ≫d |A|
2/K D.

We note that simply setting φ = x in (2.3) immediately delivers the so-called weak Erd˝os–
Szemer´edi Conjecture over C. This was first proven by Bourgain–Chang [3] for sets A ⊆ Q,
with work of Chang [7] delivering this conclusion for sets A ⊆ R, conditional on the weak
PFR conjecture over Z. Building on the work of Chang and employing the resolution of the
weak PFR conjecture over Z due to Gowers–Green–Manners–Tao [22], the second author
proved that for any finite set A ⊊ C with |A · A| ≤ K|A|, one has at most |A|2/K O(1) many
quadruples a1, . . . , a4 ∈ A such that a1 + a2 = a3 + a4, see [33, Proposition 1.5]. This then
immediately implies that |A + A| ≥ |A|
2/K O(1).

2.3. Elekes–Szab´o. As remarked in §1, we are able to prove a more general upper bound
for quantities of the form |V ∩ Ag| which depend on the maximal dimension of a translate of
an algebraic subgroup contained in V. In order to elaborate on this, we present the following
definition.

Definition 2.5. For an irreducible subvariety V ⊆ Gg, we define the coset defect, denoted
codef(V), to be the maximal dimension of a connected algebraic group H ⊆ G
g, such that
γ + H ⊆ V for some γ ∈ G
g(C).

With this in hand, we state our result.

Theorem 2.6. Let G be a 1-dimensional, connected algebraic group over C not isomorphic
to Ga. Let A ⊆ G be a finite set such that |A + A| ≤ K|A| for some K ≥ 1. Then for any
irreducible subvariety V ⊆ G
g, one has

|V ∩ A
g| ≪g,deg(V) (K C + |A|codef(V)),

where the constant C > 0 depends only on deg(V) and g.

SUM-PRODUCT PHENOMENON FOR ALGEBRAIC GROUPS AND BREMNER’S CONJECTURE 11

We note that V might be covered by translates of algebraic subgroups even though V
is not a translate of an algebraic subgroup. However, Theorem 2.6 still applies to such
varieties. For example, for g = 3 the variety V defined by X1X 2
2 X3 − X2X3 − 1 = 0 is not a
coset, but is covered by cosets of the form X2X3 = γ, X1X2 = (1 + γ)/γ for γ ∈ C \ {−1, 0}.
Theorem 2.6 admits the following corollary.

Corollary 2.7. For every d, g ≥ 1 there exists ϵ > 0, such that for an irreducible variety
V ⊆ G
g of degree at most d, if |A + A| ≤ |A|
1+ϵ and codef(V) ≥ 1, then

|A
g ∩ V| ≪g,deg(V) |A|
codef(V). (2.4)

Finally, if V does not contain a positive dimensional coset, then for every ϵ > 0, if |A+A| ≤
|A|
1+ϵ, then |V ∩ A
g| ≪g,deg(V) |A|
Cϵ,
where C > 0 is some constant depending on deg(V) and g.

As in the case of Theorem 1.5 and Example 1.6, one can show that the upper bounds in
Theorem 2.6 and inequality 2.4 are of the right order.

3. Setup

3.1. Algebraic groups. We will be working with connected algebraic groups over C of
dimension 1. An algebraic group (over C) is an algebraic variety G with a morphism from
G × G to G that induces a group operation on G(C). As an example, consider the algebraic
group given by the variety A1 along with the morphism which maps (x, y) to x + y. We
refer to this algebraic group as the additive group Ga. Another example is the algebraic
group given by the algebraic variety A1 \ {0} with the morphism that maps (x, y) to xy.
We refer to this algebraic group as the multiplicative group Gm. A third example of this is
an elliptic curve over C with its canonical group operation [40, III.2].
All the above three examples are 1-dimensional, connected algebraic groups over C, and
in fact, these are essentially the only possible examples. In order to see this, note that the
analytification of G is a complex Lie group, and therefore has an exponential map

expG : C → G(C),

which is analytic and non-constant, since it is a local diffeomorphism [30, Proposition 20.8
(f)]. When G is commutative, expG is a morphism of Lie groups. For this, see [30, Exer-
cise 20-8] or the Baker–Campbell–Hausdorff formula. The following argument in complex
analysis now implies that expG is surjective with discrete kernel.

Proposition 3.1. Let G and H be complex Lie groups of dimension 1. Suppose that H
is connected. Every morphism of complex Lie groups from G to H is either trivial or is
surjective with discrete kernel.

Proof. Suppose the morphism f is not trivial. Discreteness of the kernel follows from the
uniqueness of analytic continuation. Since dim(G) = dim(H) = 1, the open mapping
theorem implies that the image U of f is open. The set U is also a Lie subgroup of H.
Therefore H is a disjoint union of the cosets of U , each of which is open. Since H is
connected, there can be at most one coset, i.e., U = H. □

There are therefore three options for G depending on the kernel of expG.

12 JOSEPH HARRISON, AKSHAT MUDGAL, HARRY SCHMIDT

(1) The kernel is trivial. In this case G(C) is isomorphic to the additive group of complex
numbers C.
(2) The kernel is a lattice of rank one. In this case G(C) is isomorphic to the multiplicative
group of complex numbers C
∗. For example, the linear map on the tangent space C
that takes the kernel of expG to the lattice 2πiZ is such an isomorphism.
(3) The kernel is a lattice Λ of rank two. In this case G(C) is isomorphic to the complex
torus C/Λ. It can be shown via the classical Weierstrass theory [40, Proposition VI.3.6]
that G is isomorphic to the group of complex points of an elliptic curve.
In each case, the isomorphism of G(C) with C, C
∗ or C/Λ can be promoted to an isomor-
phism of G with Ga, Gm or an elliptic curve E by extending the isomorphism to the closure
of G(C) in some projective space, and applying Serre’s GAGA theorem.
The exponential map expG of an algebraic group admits a local inverse, which we denote
by logG. We note that expGa(C) = idC and expGm(C) is the usual exponential function
exp : C → C∗. Furthermore, when G is an elliptic curve embedded into P
2 via its Weierstrass
form, then expG : C → G(C) ⊆ P
2(C) satisfies

expG(z) = (2σ(z)3℘(z) : σ(z)3℘
′(z) : 2σ(z)3)

for all z ∈ C, where ℘ and σ denote the classical Weierstrass ℘-function and σ-function
associated to the lattice given by the kernel of expG.
We remark that this classification of connected algebraic groups of dimension 1 extends
to any algebraically closed field in characteristic zero. This follows from the Barsotti–
Chevalley–Rosenlicht theorem, see [32, Theorem 10.25].
If G is an algebraic group, then a closed subvariety of G is called an algebraic subgroup if
it is an algebraic group with the same group operation. In particular, we require algebraic
subgroups to be closed, but not irreducible.
Given algebraic groups G and H, a morphism from G to H is a morphism of the underlying
varieties that also induces a group homomorphism from G(C) to H(C). For example, every
morphism from Gm to Gm is given by sending x to xn for some n ∈ Z. Moreover, every
morphism from Gm to Ga is trivial; that is, it sends x to 0. The kernel of a morphism
of algebraic groups is an algebraic subgroup. Moreover, if dim(G) = dim(H) = 1, then
any morphism of algebraic groups from G to H is either trivial or it is surjective with
finite kernel. This follow from Proposition 3.1 upon observing that the kernel is discrete
in the analytic topology and closed in the Zariski topology. Morphisms of algebraic groups
that are surjective with finite kernel are called isogenies. Moreover, G and H are called
isogenous if there is an isogeny from G to H. Thus, any morphism of algebraic groups of
dimension 1 is either trivial or an isogeny. If two connected algebraic groups of dimension
1 are isogenous, then they are either isomorphic or they are elliptic curves. We will use the
following well-known fact about complex algebraic groups.

Lemma 3.2. Let G, H be one dimensional complex connected algebraic groups and C ⊊
G × H an algebraic correspondence. Suppose that there is a one dimensional vector space
V ⊊ C2, b ∈ C2 and a non-empty open set U ⊆ C
2, such that U ∩ (V + b) is non-empty and

expG×H(U ∩ (V + b)) ⊆ C(C).

Then C is a translate of an algebraic group.

We will provide a proof for the benefit of the reader.

SUM-PRODUCT PHENOMENON FOR ALGEBRAIC GROUPS AND BREMNER’S CONJECTURE 13

Proof. We can translate C by P = expG×H(b) so that we can assume that b = 0 and U is a
neighbourhood of the identity. Now expG×H(U ∩ V ) ⊆ C(C). There is an open non-empty
set U ′ ⊆ U , such that U + x ∩ U is non-empty for all x ∈ U ′. Thus exp(U ′) ⊊ Stab(C) =
{P ∈ C(C); P + C = C}. Since the stabiliser Stab is an algebraic variety and C is irreducible
C = Stab(C). We also note that the stabilizer is a group and thus an algebraic subgroup of
G × H. □

3.2. Degrees. Given an algebraic group G and some subvariety V of G, we will often need
to define the degree of V. It is worth mentioning that our varieties will always be pure
dimensional and otherwise we talk about Zariski-closed sets. In order to define the degree
of V, we need a map from from G to projective space Pn for some n ∈ N. Such maps are
parameterised by line bundles.
Thus, let G be an algebraic group of dimension 1. If G is Ga or Gm, we fix a canonical
open immersion G → P
1. In this case, the Zariski closure G of G in P
1 satisfies G = P1. We
let LG denote the line bundle OP1(1) on P1. If G is an elliptic curve, let LG be the ample
line bundle OG(O), where O is the identity of E. Moreover, in the case of elliptic curves,
we have G = G.
On a product of algebraic groups G1 × · · · × Gg, we will always use the line bundle

L = (π∗
1LG1) ⊗ · · · ⊗ (π∗
gLGg ),

where for each i ∈ {1, . . . , g}, the map

πi : G1 × · · · × Gg → Gi

is the projection morphism, and π∗
i is the pullback morphism on line bundles.
With the line bundle L fixed, the degree degL(V) of a (quasi-projective) subvariety V of
dimension n in G1 × · · · × Gg is the intersection product

degL(V) = c1(L)
n · [V ],

where c1(L) is the first Chern class of L. For the definition of the intersection product and
Chern classes, see [20, Chapter 2.5]. A viewpoint requiring less machinery is that a multiple
of L is very ample and gives an embedding into projective space. The degree of V is then
the degree of the image of the embedding.

Remark 3.3. If G is Ga or Gm and V is a hypersurface defined by a single polynomial,
the above definition somewhat closely resembles an intuitive definition of the degree of
polynomial. In particular, letting X1, . . . Xg denote the cartesian coordinates of G
g, we
view the hypersurface V as a subvariety of A
g defined by some polynomial

fV = ∑

λ∈A c(λ)X λ,

where A is some finite, non-empty subset of Z
g
≥0, c(λ) ̸= 0 for all λ ∈ E, and X λ =
X λ1
1 . . . X λg
g . Then it turns out that degL(V) = j1 + · · · + jg, where for each 1 ≤ i ≤ k,
the number ji is the largest non-negative integer j such that there is a monomial X λ, with
λ ∈ E, which is divisible by X j
i . This can be strictly larger than the usual total degree of a
polynomial, which is defined as the largest degree of a monomial with non-zero coefficient.

14 JOSEPH HARRISON, AKSHAT MUDGAL, HARRY SCHMIDT

3.3. Correspondences. We first make the concept of a correspondence precise.

Definition 3.4. Let X and Y be irreducible curves. A correspondence C between X and
Y is an irreducible curve C ⊆ X × Y such that the canonical projections πX : C → X and
πY : C → Y are dominant. Moreover, for any set A ⊆ X(C), we define

C(A) = {πY (π−1
X (x)) : x ∈ A} = πY (C ∩ (A × Y )).

Here, we recall that the projection πX is finite if for every x ∈ X, the set π−1
X (x) = {z ∈
C(C) : πX(z) = x} is finite. Since all curves involved are irreducible this is equivalent to πX
being dominant. We recall that the projection πX is dominant if πX(C(C)) is dense in X.
Note that here we use the fact that πX(C(C)) is either finite, empty or co-finite; this is not
true for an arbitrary dense set A ⊆ X(C).
If A ⊆ X(C) is a finite set, then C(A) is also finite by our assumptions on the dimensions
of X, Y and C. If dX and dY are the degrees of the projection maps πX and πY , then since
X, Y, C are irreducible algebraic curves, dX, dY are equal to the maximal cardinality of a
fibre. Thus |C(A)| ≤ dX|A| and
 1
dY |A| ≤ |C(A)|

if A lies in the image of πY . In particular, the lower bound holds for all finite sets A when
πY is surjective.
Let LX and LY be line bundles on projective varieties X and Y , respectively, and let
L = π∗
XLX ⊗ π∗
Y LY . If C is a correspondence between X and Y , then

degL(C) = degLX ((πX)∗[C]) + degLY ((πY )∗[C]) = dX degLX (X) + dY degLY (Y )

by the projection formula. Thus if LX and LY are ample, then

|C(A)| ≍degL(C) |A|

for all finite sets A. In particular this will be true in our setup, described above in Section
3.2.
We will be working with correspondences between algebraic groups. If there is a corre-
spondence between algebraic groups G and H that is the translate of an algebraic group,
then G and H are isogenous. Let us now give two intuitive examples.

Example 3.5. We can fix a rational map φ : X → Y that is well-defined on an open
U ⊆ X and then consider C to be the Zariski-closure of the graph of φ. Bremner’s question,
discussed in the introduction, concerns the case where X is an elliptic curve in Weierstrass
form y2 = x3 + ax + b, U = X \ {O} is X without its point at infinity, Y = Ga, and
φ(x, y) = x. If A ⊆ U (C) is a finite set, then C(A) is the set of all x-coordinates occuring
among points of A.

Example 3.6. Let φ be a polynomial of degree d ≥ 1. We can consider a correspondence
between Gm × Gm whose complex points are given by {(x, φ(x)) : x ∈ Gm(C)}. One
can see that the degree of this correspondence is d + 1. Moreover, C is a translate of an
algebraic subgroup if and only if φ is of the form cx
d for some c ∈ C. This is precisely the
correspondence that we use for our deduction of Corollary 1.4 from Theorem 1.3.

SUM-PRODUCT PHENOMENON FOR ALGEBRAIC GROUPS AND BREMNER’S CONJECTURE 15

3.4. Mordell–Lang and S-unit equations. We recall here the deep results of Laurent,
David–Philippon and Evertse–Schlickewei–Schmidt on the Mordell–Lang conjecture.

Theorem 3.7. [11, 29, 18] For any positive integers d, g, there exists a constant C =
C(d, g) ∈ N with the following property. Suppose G is an elliptic curve or Gm. Let V ⊆ G
g

be an algebraic variety of degree d and V co be

V co = V \ ⋃

R+B⊂V,dim(B)>0(R + B),

where R runs through points in Gg and B through connected algebraic subgroups. Then

|V co ∩ Γ| ≤ C 1+r

for any subgroup Γ ⊆ G
g(C) of rank r. More generally, one has

V ∩ Γ =
 C1+r
⋃

i=1 (γi + Hi) ∩ Γ,

where γ1, . . . , γC1+r are elements of Γ, and H1, . . . , HC1+r are connected subgroups of G
g

whose degrees are bounded in terms of d.

Proof. If G is an elliptic curve then this theorem follows directly from [11, Th´eor`eme 1.13].
For G = Gm, we first prove the first part. We fix polynomials Q1, . . . , Qk ∈ C[X1, . . . , Xg],
such that V is their common zero-set. Their degree is bounded by the degree of V and the
number of non-zero monomials in Qi is bounded by deg(Qi)
g for i = 1, . . . , g. If we have a
point γ ∈ V ∩ Γ, then Qi(γ) = 0, i = 1, . . . , k and if γ ∈ V co, then there is at least one i,
such that no subsum of the monomials in Qi vanishes if evaluated at γ. This follows from
the proof of Laurent [29]. The number of solutions of Qi(γ) = 0 with no vanishing subsum
is bounded by c(deg(Qi), g)1+r for all i [18]. This gives the first claim.
For the general statement we follow the proof of Laurent [29]. Each maximal algebraic
group contained in V corresponds to a partition of the support of its defining equations.
Thus, their number and degree is bounded only in terms of the degree of V. For each
algebraic subgroup given by a partition, Laurent constructs a map that reduces counting
the number of intersection points to the S-unit equation for which we can apply the main
theorem in [18].
Finally, the fact that the degree of each Hi is bounded in terms of d follows from the
argument in [2, Lemma 2]. □

Note that V co might be empty, even if V is not a coset. An easy example is a product
C × Gm ⊆ G
3
m for a curve C, that is covered by cosets of the form {P } × Gm.

4. Projecting cartesian products

The main goal of this section is to prove Theorem 4.2 which describes expansion properties
for certain projections of varieties.
Thus, let G to be some 1-dimensional, connected algebraic group over C, not isomorphic
to Ga, and let B be a projective variety of positive dimension. Let π1 : G
g × B → Gg and
π2 : Gg × B → B be the canonical projection maps. We recall the notion of a degenerate
variety as described in Definition 1.7.

16 JOSEPH HARRISON, AKSHAT MUDGAL, HARRY SCHMIDT

Definition 4.1. We call an irreducible subvariety V ⊆ Gg × B degenerate, if there exists
a connected algebraic group H ⊆ G
g of positive dimension, and a proper subvariety W ⊆
G
g/H × B such that V = π−1
H (W),
for the projection πH : G
g ×B → Gg/H ×B. If V is not degenerate, we call V non-degenerate.

With this in hand, we now state our version of Theorem 1.8 for sets lying in low rank
subgroups.

Theorem 4.2. Let V ⊆ G
g × B be a non-degenerate subvariety of dimension g, such that
π1 and π2 restricted to V are dominant. Let Γ ⊆ G(C) be subgroup of rank r. Then for any
finite set A ⊆ Γ we have
 |π2((A
g × B) ∩ V)| ≥ c(g, deg(V))
1+r|A|
g,

for a constant c = c(g, deg(V)) > 0 depending only on g and deg(V).

In order to prove Theorem 4.2, we will require the following lemma.

Lemma 4.3. Suppose that V ⊆ G
g × B is a non-degenerate subvariety of dimension g,
and suppose that the maps π1 and π2 are dominant. Then there exists a proper Zariski
closed set Z ⊆ G
g, such that if there is a positive dimensional subgroup H ⊆ G
g and
(P, Q) ∈ (Gg × B)(C) with
 {(P + T, Q) : T ∈ H(C)} ⊆ V, (4.1)

then P + H ⊆ Z. Moreover, the degree of the components of Z and their number is bounded
by a constant depending only on g, deg(V).

Proof. We first fix a connected algebraic subgroup H of dimension k, and show that all P
such that (P + H) × {Q} ⊆ V for some Q are contained in a Zariski closed set ZH, that
depends on H. The lemma will be proved by taking a union of such sets ZH. Let pH be the
restriction of the quotient map πH : G
g × B → (G
g/H) × B to V. By Chevalley’s theorem
[23, Theorem 1.3.1] the set

Z H = {y ∈ V(C) : dim(p
−1
H (pH(y))) ≥ k}

is closed. Thus if (P + H) × {Q} ⊆ V then (P + H) × {Q} ⊆ p−1
H (pH(P, Q)), and so
(P, Q) ∈ Z H.
Since B is projective, the projection π1 : G
g × B → G
g is closed [39, Theorem 1.11].
Therefore ZH = π1(Z H) is closed in G
g. If ZH = G
g then Z H has dimension g, and is
therefore equal to V. Also, the degree of ZH is bounded by the degree of Z H, by the
projection formula. It therefore suffices to show that Z H is not equal to V and that the
degree of Z H is bounded in terms of g and deg(V).
We will first prove that Z H ̸= V, and so, suppose that Z H = V. Then consider W, the
Zariski closure of πH(V) and Z ′ = π−1
H (W), which is a subvariety of Gg × B containing V.
Firstly, W is irreducible, because V is irreducible. Since H is connected, the fibres of πH
are irreducible, and so [39, Theorem 1.26] implies that Z ′ is irreducible. Since πH(V) is
constructible it contains U that is Zariski–open (dense) in W. We thus have that Z ′ =
π−1
H (U ) ∪ E, where E is the a finite union of irreducible subvarieties E = π−1
H (E′), with
E′ running over all irreducible components of W \ U . By the fibre dimension theorem
dim(E) < dim(Z ′) for all E. Since π−1
H (U ) ⊂ V, we have that Z ′ ⊆ V ∪ E, and a dimension

SUM-PRODUCT PHENOMENON FOR ALGEBRAIC GROUPS AND BREMNER’S CONJECTURE 17

count shows that dim(V) = dim(Z ′). Since both V and Z ′ are irreducible V = Z ′. This
means that V = π−1
H (W)

and so V is degenerate. This contradicts our assumption on V.
We will now prove that the degree of Z H is bounded in terms of g and deg(V). For g ≥ 1,
define expGg the exponential of Gg at the identity and F a suitably chosen fundamental
domain for expG. The graph expG restricted to F is a sub-Pfaffian set of complexity bounded
by an absolute (effectively computable) constant, see work of Jones and the third author
[27]. Each algebraic group H, corresponds to a vector space TH, such that expGg (TH) = H.
We then consider the set

T H = {γ ∈ F g : there exists b ∈ B(C) such that expGg (γ + TH) ⊆ V ∩ (Gg × {b})},

which is a sub-Pfaffian set of complexity ccomp, where ccomp depends only on deg(V). We
then have Z H = expGg (T H), which has also bounded complexity, and it is a closed algebraic
variety. The complexity of Z H bounds its degree, and so, we have proven this claim as well.
Finally, suppose P + H is a maximal translate lying in the fibre VQ = π−1
2 (Q) ∩ V. Note
that deg(VQ) ≪g deg(V) by B´ezout’s theorem. By an argument of Bombieri–Zannier [2,
Lemma 2], if H is an algebraic subgroup appearing in a maximal translate of VQ, then H
belongs to a finite set {H1, . . . , Hℓ} with ℓ ≪g,deg(V) 1. The lemma is proved upon taking
Z = ZH1 ∪ · · · ∪ ZHℓ. □

In order to prove Theorem 4.2, we combine Lemma 4.1 with the estimates coming from
uniform Mordell–Lang (Theorem 3.7). In order to get control on the contribution of the
closed set Z from Lemma 4.1 we need the following Schwartz–Zippel type estimate.

Lemma 4.4. Let Z ⊆ Gg be an algebraic sub-variety. Then for any finite set A ⊆ G(C)

|Z ∩ Ag| ≪g,deg(Z) |A|
dim(Z).

Proof. We prove this by induction on the dimension. We may suppose that Z is irreducible,
since we can argue component wise. We can also pass to the closure Z of Z in G
g. If
dim(Z) = 0, this is trivial. So assume that dim(Z) ≥ 1. We can choose a factor G in
G
g such that the projection from Z to G is surjective. Without loss of generality, we can
assume this is the first factor. Then the intersection Z ∩ ({a} × G
g−1) has dimension equal
to dim(Z) − 1. By B´ezout’s theorem

deg(Z ∩ ({a} × G
g−1)) ≤ deg(Z) deg(G
g−1) ≪g deg(Z).

We then conclude by induction that

|Z ∩ Ag| ≤ ∑

a∈A |Ag ∩ ({a} × G
g−1) ∩ Z| ≪g,deg(Z) |A||A|
dim(Z)−1. □

We are now ready to prove Theorem 4.2.

Proof of Theorem 4.2. As V is non-degenerate, a coset contained in a fibre VQ = π−1
2 (Q) ∩ V
is contained in a closed set Z ⊆ V not depending on Q. This is Lemma 4.1. We set
A
′ = A
g \ Z(C) and by Lemma 4.4, |Z ∩ Ag| ≪deg(V) |A|g−1. Since the projection π1 from
V to Gg is dominant and B is projective, π1 is actually surjective, because it is closed [39].

18 JOSEPH HARRISON, AKSHAT MUDGAL, HARRY SCHMIDT

Hence for each point a ∈ A′, there is a point b ∈ B such that (a, b) ∈ (A′ × B) ∩ V. On the
other hand, it follows from Theorem 3.7 that for every b ∈ B(C), one has

|(A′ × {b}) ∩ V| ≤ c(r, g, deg(V))
r+1

Thus the image π2((A
g × B) ∩ V) contains at least

c(r, g, deg(V))
−1−r(|A|
g − c′|A|
g−1)

elements for a constant c
′ > 0 depending only on deg(V) and g, which finishes the proof of
Theorem 4.2. □

5. Correspondences and cosets

In this section we construct a variety Vsum with the property that π2((A
g × H) ∩ Vsum)
is roughly the sumset C1(A) + · · · + Cg(A), for correspondences C1, . . . , Cg between algebraic
groups G and H. We would like to apply Theorem 4.2 to Vsum, and so this section is
dedicated to showing that this variety is non-degenerate, in the sense of Definition 1.7.
Now let G and H be connected algebraic groups of dimension 1, such that G is not
isomorphic to Ga. We compactify H as described at the beginning of to section 3.2. Thus
H is either P
1 or an elliptic curve, depending on whether H is isomorphic to Ga, Gm or to
an elliptic curve. We also consider the g-fold sum map on H

psum : H g → H

(Q1, . . . , Qg) ↦→ Q1 + · · · + Qg,

its graph Γ(psum) ⊆ H g × H, and its closure Γ(psum) in H g+1.
Let C1, . . . , Cg ⊆ G × H be correspondences, none of which is the translate of an algebraic
subgroup. We set

V ∗ = {(P1, . . . , Pg, Q1, . . . , Qg+1) : (Q1, . . . , Qg+1) ∈ Γ(psum), (Pi, Qi) ∈ Ci},

which is an irreducible variety. The projection πGg×H : Gg × H g+1 → Gg × H onto G
g and
the last coordinate of H g+1 is a closed map by [39, Theorem 1.11]. We set

Vsum = πGg×H(V ∗) (5.1)

which is an irreducible variety since it is the image of an irreducible variety under a closed
map. Thus the role of the projective variety B in Section 4 is played by H.
Our main goal in this section is to prove the following.

Proposition 5.1. The variety Vsum ⊆ Gg × H is non-degenerate of dimension g. The
projection π1 : Vsum → G
g is surjective and the projection π2 : Vsum → H is dominant.

As we exclusively work over complex algebraic groups, we will prove a lemma about
holomorphic maps between tangent spaces of algebraic groups.

Lemma 5.2. Let U = U1 × · · · × Ug be an open set of Cg and fi : Ui → C non-constant,
holomorphic functions for 1 ≤ i ≤ g. Suppose that there is a vector space W ⊆ C
g of
dimension 1 such that for any b ∈ C
g, (f1, . . . , fg) restricted to (W + b) ∩ U satisfies

f1(z1) + · · · + fg(zg) ≡ const.

Then there is at least one j ∈ {1, . . . , g} such that fj is affine linear.

SUM-PRODUCT PHENOMENON FOR ALGEBRAIC GROUPS AND BREMNER’S CONJECTURE 19

Proof. After possibly permuting coordinates we can parameterise any co-set W + b by

(b1, . . . , bg−k, z, a1z + c1, . . . , ak−1z + ck−1)

where k ≥ 1 is an integer, a1, . . . , ak−1 ∈ C∗ depend on W and b1, . . . , bg−k, c1, . . . , ck−1
depend on W + b. We may assume that k ̸= 1 since otherwise fg is constant. We apply the
invertible linear transformation

L : C
g−k × C × C
k−1 → C
g−k × C × C
k−1

L(z, z, w) = (z, z, w1 − a1z, · · · , wk−1 − ak−1z)

to U and the open set L(U ) then contains a product set ˜U = ˜U1 × · · · × ˜Ug. Taking the
total derivative with respect to z we obtain

∂zg−k+1fg−k+1(z) + a1∂zg−k+2fg−k+2(a1z + c1) + · · · + ak−1∂zg fg(ak−1z + ck−1) = 0,

for all (b1, . . . , bg−k, z, c1, . . . , ck−1) ∈ ˜U . Since k ≥ 2, we may fix any

(z0, c1,0, . . . , ck−2,0) ∈ ˜Ug−k+1 × · · · × ˜Ug−1
to find that fg is affine linear. □

Corollary 5.3. Let U1 × · · · × Ug be an open set of Cg and fi : Ui → C holomorphic non-
constant functions i = 1, . . . , g. Suppose that there is a vector space V ⊊ Cg of dimension
k such that for any b ∈ Cg, (f1, . . . , fg) restricted to (V + b) ∩ U satisfies

f1(z1) + · · · + fg(zg) ≡ const.

Then fj is affine linear for at least one j ∈ {1, . . . , g}.

Proof. We can cover V by translates of a one dimensional vector space L and thus any
translate of V contains a translate of L. Thus Corollary 5.3 is implied by Lemma 5.2. □

Proof of Proposition 5.1. Let V o be the variety given by the points (P1, . . . , Pg, Q) ∈ Gg ×H
such that there exists (Pi, Qi) ∈ Ci∩(G×H(C)), with Q1+· · ·+Qg = Q. Note that V o is open
in Vsum. For all but finitely many P ∈ G(C), there exists Q ∈ H(C) such that (P, Q) ∈ Ci(C)
for i = 1, . . . , g. Thus, π1 is dominant and by [39, Theorem 1.11] it is surjective. Also, for
Q ∈ H(C), we can find (Q1, . . . , Qg) ∈ H(C) such that Q1 + · · · + Qg = Q. It follows
that π2 is dominant. Now suppose that Vsum is degenerate, that is, there exists a connected
algebraic group H ′ ⊆ G
g of positive dimension, and a proper subvariety W ⊆ (G
g/H ′) × H
such that Vsum = π−1
H ′ (W), (5.2)
for the projection πH ′ : G
g × H → (G
g/H ′) × H.
Now, let s1, . . . , sg be analytic functions on an open U ⊆ G(C)) with target H(C), such
that the graph of si coincides with Ci(C) restricted to U × H(C). By (5.2) the sum ∑g
i=1 si
(where we sum in H) is constant along H ′ + P for all P ∈ Gg(C). After perhaps shrinking
U to ensure that it is simply connected, we lift these functions to functions from the tangent
space of G to the tangent space of H, via setting fi = expH ◦si ◦ logG, i = 1, . . . , g. Now
setting V to be the tangent space of H ′, and recalling that the sum ∑g
i=1 si is constant along
translates of H ′, we deduce that f1, . . . , fg satisfy the conditions of Corollary 5.3. Thus at
least one of fi is affine linear. Lemma 3.2 implies that at least one Ci is the translate of an
algebraic subgroup, which contradicts our assumption on the correspondences and concludes
the proof. □

20 JOSEPH HARRISON, AKSHAT MUDGAL, HARRY SCHMIDT

6. Freiman–type structural theorems

For the purposes of this section and the next, given a 1-dimensional, connected algebraic
group H and some finite, non-empty set A ⊊ H, we denote rk(A) to be the smallest integer
r ≥ 1 such that there exist ξ1, . . . , ξr ∈ H satisfying

A ⊆ {n1ξ1 + · · · + nrξr : n1, . . . , nr ∈ Z}.

The main aim of this section is to prove the following structural result.

Lemma 6.1. Let H be a connected algebraic group of dimension 1, let A ⊆ H be a finite,
non-empty set, let n ≥ 2 be an integer such that |nA| ≤ K|A| for some K > 1. Then there
exists some integer 1 ≤ d and some subset A
′ ⊆ A such that

d ≪ 1 + log(4K)
log n and |A′| ≫ |A|

K
 C log 2
log n and rk(A′) ≤ d,

where C > 0 is some absolute constant.

We will begin by proving the n = 2 version of this.

Lemma 6.2. Let H be a connected algebraic group of dimension 1, let A ⊆ H be a finite,
non-empty set such that |A + A| ≤ K|A| for some K > 1. Then there exists some integer
1 ≤ d ≤ C log(400K), and some subset A′ ⊆ A such that |A′| ≥ |A|/(100K)C′ and rk(A′) ≤
d, where C = 140 and C ′ = 110.

In order to prove Lemma 6.2, we will need the following very nice result of Gowers–Green–
Manners–Tao [22, Theorem 1.3] on the resolution of the weak polynomial Freiman–Ruzsa
conjecture over Z.

Lemma 6.3. Let D be a positive integer, let A ⊊ Z
D be a finite, non-empty set such that
|A + A| ≤ K|A| for some K > 1. Then there exists some integer 1 ≤ d ≤ C log(4K), some
elements x1, . . . , xd ∈ Z
D and some subset A′ ⊆ A such that |A
′| ≥ |A|/K C′ and

A
′ ⊆ {n1x1 + · · · + ndxd : n1, . . . , nd ∈ Z},

where C = 140 and C ′ = 110.

We will also need the following simple lemma.

Lemma 6.4. Let H be a connected algebraic group of dimension 1, let A ⊊ H be a finite,
non-empty set. Then the subgroup generated by S is isomorphic to some subgroup of Z
D ×
Z/nZ × Z/mZ, for some non-negative integer D and some n, m ∈ N.

Proof. This is true when H = (C, +) since any finitely generated subgroup of (C, +) is
isomorphic to Z
D for some D ∈ N. This is slightly more non-trivial when H = (C∗, ·), but it
is a standard fact that any finitely generated subgroup of (C
∗, ·) is isomorphic to Z
D ×Z/N Z
for some non-negative integer D and some N ∈ N. Finally, when H is some elliptic curve
over C, we may use the fact, mentioned in Section 3.1, that H is isomorphic to C/L, where
L is some lattice of rank two in C, to deduce that any finitely generated subgroup of H is
isomorphic to some subgroup of Z
D × Z/nZ × Z/mZ for some non-negative integer D and
some n, m ∈ N. □

We are now ready to prove Lemma 6.2

SUM-PRODUCT PHENOMENON FOR ALGEBRAIC GROUPS AND BREMNER’S CONJECTURE 21

Proof of Lemma 6.2. Let Γ be the subgroup generated by S. We can use Lemma 6.4 to
view Γ as a subgroup of Zl × Z/nZ × Z/mZ for some integers n, m ≥ 1 and some integer
l ≥ 0. Now, for any 0 ≤ i, j ≤ 9, define

Ai = {x ∈ Z : in/10 ≤ x < (i + 1)n/10} (mod n)

and Bj = {x ∈ Z : jm/10 ≤ x < (j + 1)m/10} (mod m).

Thus Z/nZ × Z/mZ = ∪0≤i,j≤9(Ai × Bj). Moreover, let Si,j = S ∩ (Z
l × Ai × Bj) for every
0 ≤ i, j ≤ 9. Since ∑

0≤i,j≤9 |Si,j| = |S|,

by the pigeonhole principle, there exist some 0 ≤ i, j ≤ 9 such that |Si,j| ≥ |S|/100.
Let π : Z
l × Z/nZ × Z/mZ → Z
l+2 be the map satisfying

π(x, a (mod n), b (mod m)) = (x, a, b)

for all x ∈ Z
l and a ∈ {0, 1, . . . , n − 1} and b ∈ {0, 1, . . . , m − 1}. We now claim that for
any s1, s2, s3, s4 ∈ Si,j, one has

π(s1) + π(s2) = π(s3) + π(s4) if and only if s1 + s2 = s3 + s4. (6.1)

In order to see this, first note that since π−1 is just the projection map, it suffices to check
that equality on the right hand side implies equality on the left hand side. Writing

sl = (xl, al (mod n), bl (mod m))

for every 1 ≤ l ≤ 4, we see that s1 + s2 = s3 + s4 implies that

a1 + a2 − a3 − a4 ≡ 0 (mod n) and b1 + b2 − b3 − b4 ≡ 0 (mod m).

Since in/10 ≤ a1, a2, a3, a4 < (i + 1)n/10, we see that

a1 + a2 − a3 − a4 ∈ [−n/5, n/5] ∩ Z.

The preceding congruence condition now necessitates that a1 + a2 = a3 + a4. A similar
argument gives us that b1 + b2 = b3 + b4.
Thus, writing S1 = π(Si,j), the equivalence in (6.1) implies that

|S1 + S1| = |Si,j + Si,j| ≤ |S + S| ≤ K|S| ≤ 100K|Si,j| = 100K|S1|

Since S1 ⊆ Z
l+2, we may now apply Lemma 6.3 to find some subset S′
1 ⊆ S1 such that
|S′
1| ≥ |S1|/(100K)
C′ and

S′
1 ⊂ {n1x1 + · · · + ndxd : n1, . . . , nd ∈ Z},

where x1, . . . , xd ∈ Zl+2 are some elements and 1 ≤ d ≤ C log(400K) is some integer. This
implies that
 π−1(S′
1) ⊂ {n1π−1(x1) + · · · + ndπ−1
1 (xd) : n1, . . . , nd ∈ Z}.

Setting S′ = π−1(S′
1) finishes the proof of Lemma 6.2. □

We now present our proof of Lemma 6.1.

22 JOSEPH HARRISON, AKSHAT MUDGAL, HARRY SCHMIDT

Proof of Lemma 6.1. Since n ≥ 2, we have that |2S| ≤ |nS|, and so, whenever 2 ≤ n ≤ 16,
we may apply Lemma 6.1 and adjust the implicit constant in the Vinogradov notation
to obtain the desired result. Thus, we assume that n > 16, in which case, writing k =
⌊(log n)/(log 2)⌋, we see that k ≥ 4. Now since |2kS| ≤ |nS| ≤ K|S|, we get that

K ≥ |2
kS|
|S| = ∏

1≤j≤k
 |2
jS|
|2j−1S| ,

whence, there exists some 1 ≤ j ≤ k such that

|2
jS| = |2
j−1S + 2
j−1S| ≤ K 1/k|2
j−1S|. (6.2)

Applying Lemma 6.2 for the set 2
j−1S, we get that there exists some set X ⊆ 2
j−1S such
that
 |X| ≫ |2
j−1S|
K C/k and X ⊆ {n1ξ1 + · · · + ndξd : n1, . . . , nd ∈ Z}, (6.3)

for some
 d ≪ 1 + log(4K)
k
and some points ξ1, . . . , ξd ∈ H.
Thus, it suffices to prove that there exists a large subset of S which is contained in a
translate of the set −X. In order to do this, note that

|X||S| = ∑

y∈X+S |(y − X) ∩ S| ≤ |X + S| max
y∈X+S |(y − X) ∩ S|.

Hence, it suffices to show that |X + S|
|X| ≪ K C′/k,

for some absolute constant C ′ > 0. In order to see this, we combine the fact that X ⊆ 2j−1S
along with (6.2) and (6.3) to get that

|X + S|
|X| ≤ |2
j−1S + 2
j−1S|
|X| ≪ K C/k |2
jS|
|2j−1S| ≪ K (C+1)/k.

This concludes our proof of Lemma 6.1. □

We briefly remark that structural results akin to Freiman’s inverse theorem are often used
in unison with covering results. One such result is known as Ruzsa’s covering lemma.

Lemma 6.5. Let G be an abelian group, let A, B ⊆ G be non-empty sets such that |A+B| ≤
K|B|. Then there exists some non-empty set X ⊆ A such that |X| ≤ K and A ⊆ X +B −B.

This immediately combines with Lemma 6.2 to deliver the following result.

Lemma 6.6. Let H be a connected algebraic group of dimension 1, let A ⊆ H be a finite,
non-empty set such that |A + A| ≤ K|A| for some K > 1. Then there exists some integer
1 ≤ d ≤ C log(400K), some finite subset T ⊊ H with rk(T ) = d and some non-empty
X ⊆ H such that |X| ≤ (100K)
C′+1 and A ⊆ X + T,
where C = 140 and C ′ = 110.

SUM-PRODUCT PHENOMENON FOR ALGEBRAIC GROUPS AND BREMNER’S CONJECTURE 23

7. Proofs of main results

In this section, we present the proofs of all of our results mentioned in §1 and §2.
We begin by deducing Theorem 1.1 from Corollary 2.2.

Proof of Theorem 1.1. Setting G to be an elliptic curve in Weierstrass form (1.1), H = Ga
and C the correspondence given by (x, y, x), we can apply Corollary 2.2 to obtain the first
part of Theorem 1.1. We can proceed similarly with H = Gm to obtain the desired conclusion
for geometric progressions. Setting C equal to (x, y, z), x = (u + z)
2 we get the bound on
successive squares. Also, for example choosing z2 = x, we can also bound the length of
arithmetic progressions in certain higher genus curves. □

We will now prove Theorem 1.3 by combining Theorem 2.1 and Lemma 6.1.

Proof of Theorem 1.3. Let k ≥ 1 and d ≥ 2 be integers, let g ∈ N be sufficiently large in
terms of d, k. We may further assume that |gA| ≤ |A|k since otherwise we would be done.
In this case, we may apply Lemma 6.1 to find some ξ1, . . . , ξr ∈ G and some A′ ⊆ A such
that r ≪ k log |A|/ log g and

|A
′| ≫ |A|
1−Ck/ log g and A
′ ⊆ {n1ξ1 + · · · + ndξd : n1, . . . , nd ∈ Z}.

The latter condition implies that the subgroup generated by A
′ has rank at most r, and so,
we may apply Theorem 2.1 to deduce that

|C1(A) + · · · + Cg(A)| ≥ |C1(A′) + · · · + C2k(A′)|

≥ c(d, 2k)
−1−r|A
′|
2k

≫k c(d, 2k)−1|A|
− k log c(d,2k)
log g |A
′|
2k

≫k,d |A|
2k− 2Ck2
log g − k log c(2k,d)
log g .

Choosing g to be sufficiently large so as to ensure that

2Ck2

log g < k/2 and k log c(d, 2k)
log g < k/2 and 2k < g,

we get that
 |C1(A) + · · · + Cg(A)| ≥ |C1(A) + · · · + C2k(A)| ≫k,d |A|
k.

This finishes the proof of Theorem 1.3. □

Theorem 1.5 is a special case of Theorem 2.6. Indeed, if V is an irreducible subvariety of Gg

which is not a coset of a subgroup, then we have the trivial inequality codef(V) ≤ dim(V)−1.
Thus, we will now prove Theorem 1.8.

Proof of Theorem 1.8. Since |A + A| ≤ K|A|, we may apply Lemma 6.6 to deduce that
A ⊆ Y + T , where T is contained in a subgroup Γ of H with rank d ≪ log K and Y ⊂ H
satisfies |Y | ≤ K O(1). Now, since X ⊆ A, this means that X is also contained in at most
K O(1) translates of some subgroup Γ. By the pigeonhole principle, we can find some X ′ ⊆ X
with |X ′| ≥ |X|/K O(1) such that X ′ is contained in a translate of Γ, and so, X ′ is contained

24 JOSEPH HARRISON, AKSHAT MUDGAL, HARRY SCHMIDT

in a subgroup of rank d + 1. We now apply Theorem 4.2 to deduce that

|π2((X g × B) ∩ V)| ≥ |π2((X ′g × B) ∩ V)| ≥ |X ′|
g

C 2+d

≥ |X|
g

K O(g)2C′ log K ≫ |X|
g

K C′′

where C, C ′, C ′′ > 0 are constants depending only on g, deg(V). □

Next, we prove Theorem 2.1.

Proof of Theorem 2.1. We consider the variety Vsum as described in (5.1) and note that for
any finite set A ⊂ G, the set

π2((A
g × H) ∩ Vsum) = C1(A) + · · · + Cg(A).

Proposition 5.1 implies that this variety Vsum is non-degenerate of dimension g and the
projections π1 to G
g is surjective and π2 to H restricted to V is dominant. Thus, we may
apply Lemma 4.2 to deduce that

|C1(A) + · · · + Cg(A)| ≥ c(g, deg(V ))1+r|A|g. □

We will now deduce Corollary 2.2 from Theorem 2.1.

Proof of Corollary 2.2. Throughout this proof, let C1, C2, C3 > 0 be positive constants de-
pending only on d. Suppose that A is a generalised arithmetic progression in C(Γ) of rank k
for some k ∈ N. We will first show that k ≤ C 1+r for some constant 0 < C ≪d 1. In order
to see this, let P ′ = {P0 + ℓ1P1 + · · · + ℓkPℓ : 0 ≤ ℓi ≤ 1}. (7.1)
Since L1, . . . , Lk ≥ 2, we get that P ′ ⊆ P . Since P is proper, we get that P ′ is also proper,
and so, one has |P ′ + P ′| ≤ 3
k = |P ′|
 log 3
log 2 .
Applying Theorem 2.1 for P ′, we get that

|P ′|
2C −1−r
1 ≪ |P ′ + P ′| ≪ |P ′|
 log 3
log 2 ,

whence 2
k = |P ′| ≤ C 1+r
2 . Now, we consider the set P and use the preceding upper bound
on |P ′| to observe that

|P + P | ≤ (2L1 − 1) . . . (2Lk − 1) ≤ 2
kL1 . . . Lk = 2
k|P | ≤ C 1+r
2 |P |.

We can now apply Theorem 2.1 to deduce that

C −1−r
1 |P |
2 ≤ |P + P | ≤ C 1+r
2 |P |,

and so, we obtain the desired claim |P | ≤ C 1+r
3 . □

We now consider Theorem 2.3. As in the proof of Theorem 1.3, we will derive this by
putting together Theorem 2.1 and Lemma 6.1.

Proof of Theorem 2.3. Let A ⊆ G be a finite, non-empty set. We may assume that |A+A| ≤
|A|
1+δ, since otherwise we would be done. In this case, we apply Lemma 6.2 to obtain
ξ1, . . . , ξr ∈ G such that r ≤ 140(δ log |A| + log 400)

SUM-PRODUCT PHENOMENON FOR ALGEBRAIC GROUPS AND BREMNER’S CONJECTURE 25

and some subset A
′ ⊆ A satisfying

|A
′| ≥ |A|
(100|A|δ)110 and A
′ ⊆ {n1ξ1 + · · · + nrξr : n1, . . . , nr ∈ Z}.

The latter condition implies that A
′ is contained in a subgroup of rank ≤ r whence we may
apply Theorem 2.1 to deduce that

|C(A′) + C(A
′)| ≥ c(d, 2)−(r+1)|A
′|
2

≥ c|A|
2−δ(140 log c(d,2)+220).

Combining this with the fact that |C(A) + C(A)| ≥ |C(A
′) + C(A′)| then delivers the claimed
estimate. □

We prove Theorem 2.6 by combining Theorem 3.7 and Lemma 6.6.

Proof of Theorem 2.6. Since V is not a co-set, we have for every subgroup Γ of rank r, the
equality
 V ∩ Γ =
 S⋃

i=1(γi + Hi) ∩ Γ,

where the Hi are connected subgroups whose degree is bounded in terms of the degree of
V, and S ≤ c
1+r, where c = c(deg(V), g) > 0 is a constant, see Theorem 3.7.
As |A + A| ≤ K|A|, there exists 1 ≤ d ≤ C log(400K), some finite subset T ⊊ G, with
rk(T ) = d and some non-empty subset X ⊊ G, such that |X| ≤ (100K)C′+1, and A ⊆ X +T ,
where C = 140, C ′ = 110, see Lemma 6.6. We deduce that Ag is contained in the translate
of a finite subset Tg of rank gd translated by a set Xg of cardinality (100K)gC′+g. Let ΓA
be the group generated by the elements in Tg. Note that the rank r of ΓA satisfies

r ≤ gd ≪ g log(100K).

Let x ∈ Xg. From Theorem 3.7 it follows that γ ∈ (V − x) ∩ ΓA either lies in a co-set of
degree bounded in terms of the degree of V or in a set of cardinality c1+r. The number of
co-sets for fixed x is bounded by c1+gr and so applying Lemma 4.4 to each co-set contained
in V, we get the desired bound. □

Appendix A. Diophantine equations

We show that our results related to Bremner’s conjecture have some consequences for the
Mordell–Lang conjecture. Roughly speaking, the theorems of David–Philippon and Evertse–
Schmidt–Schlickewei give very uniform bounds on the number of points on a variety that lie
on a finitely generated group. However, they generally do not provide effective bounds for the
height of these points. The situation is, in a strong sense even more dire for elliptic curves.
The points on an elliptic curve with coordinates in a number field form a finitely generated
group, but there is no known algorithm to determine its generators. It is straightforward to
pass from a number estimate to a (partly) effective version of Mordell–Lang. For example
for a given curve C with a bound t on the number of rational points C(K) (with K being
some number field), we can easily say that the rational points on C t+1(K) lie on a finite
union of proper subvarieties given by setting some coordinates equal to each other. However,
this is still a far cry from actually determining the Zariski-closure of C t+1(K). Our work
does not resolve this issue in general but, fixing a number field K, and allowing for a very

26 JOSEPH HARRISON, AKSHAT MUDGAL, HARRY SCHMIDT

high dimensional power of an elliptic curve Et, we can construct large families of surfaces,
for which we can determine the Zariski-closure of their rational points. In what follows we
let E be an elliptic curve in Weierstrass form given by

y2 = x
3 + ax + b,

with a, b ∈ K, where K is a number field. Let r be the rank of E(K). A tuple (a1, a2, . . . , at)
forms an arithmetic progression if and only if it is a point on the plane P in A
t defined by
the equations
 Zj+2 − 2Zj+1 + Zj = 0. (A.1)

for j ∈ {1, . . . , t − 2}.
Now consider the subvariety of (A
2)
t × At defined by the equations

Y 2
j − X 3
j − aXj − b = 0

for j ∈ {1, . . . , t} and
 Zj+2 − 2Zj+1 + Zj = 0

for j ∈ {1, . . . , t − 2}. Such a variety is merely the product U t × P of t copies of an affine
elliptic curve
 U : y2 = x
3 + ax + b

with the plane P , and thus has dimension t + 2. The points on this variety correspond to
t-tuples of points of an elliptic curve and t-term arithmetic progressions, with no relation
between them.
Finally we impose algebraic relations

Pi(Xi, Yi, Zi) = 0, i = 1, . . . , t

between the points on the elliptic curve, and the terms of the arithmetic progression. So we
also ask that Pi /∈ K[Xi, Yi] ∪ K[Zi] is irreducible such that they induce a correspondence.
For example, one can take
Pi(Xi, Yi, Zi) = Xi − Z 2
i , i = 1, . . . , t,

which encodes the condition that the x-coordinates of the points on U should be squares
of elements of an arithmetic progression. Each of these new relations Pi decreases the
dimension by one, because they only involve the variables (Xi, Yi, Zi). It follows that the
subvariety of U t × P defined by the t new relations is a surface SA. A similar construction
works with the quadratic equations

Zj+1Z1 = ZjZ2, j = 2, . . . , t − 1. (A.2)

We get a variety U t × Q and imposing the algebraic conditions given by Pi result in a
surface SG. We denote by D ⊊ SA, SB, the subvariety, that is given by the additional
equation Z1 = Z2. Thus the points of D correspond to degenerate arithmetic or geometric
progressions.
This is all slightly technical but for Pi = Zi − Xi the rational point SA(K) correspond
to arithmetic progressions in E(K) of length t and similarly for SG(K) and geometric
progressions. It is not hard to see, and we give the details in the paragraph below, that
these surfaces SA, SB are then of general type. The Mordell–Lang conjecture predicts that
the Zariski-closure of SA(K), SB(K) consists of a finite union of elliptic curves and points.

SUM-PRODUCT PHENOMENON FOR ALGEBRAIC GROUPS AND BREMNER’S CONJECTURE 27

This implies that there are only finitely many arithmetic or geometric sequences of length
3 in an elliptic curve.
In this setting, Corollary 2.2 delivers a more precise version that exactly predicts the
distribution of rational points, albeit for t depending on K.

Theorem A.1. For each d, r ≥ 0, there exists and effectively computable t, such that
SA(K) = SB(K) = D(K).

The variety D is either the empty set or a finite union of copies of the elliptic curve E.
We can embed A3t into P3t via

(X1, Y1 . . . , Xt, Yt, Z1, . . . , Zt) ↪→ [X1, Y1, . . . , Xt, Yt, Z1, . . . , Zt, 1]

and the Zariski-closure SA of SA is a projective surface. Let d1, . . . , dt be the degrees
P1, . . . , Pt and if SA is smooth, then the degree of the canonical class of SA is

d1 + · · · + dt + t − 3,

see [25, Examples 5.1.1]. Thus SA is of general type. A similar argument works for SG.

Appendix B. Degenerate polynomials

Let G, B, π, π2 be as in Definition 1.7. We denote P ∈ C[x1, . . . , xg] to be degenerate
with respect to Gg if the variety V ⊆ G
g
a × B defined by the equation P (x1, . . . , xg) = t is
degenerate. In this section, we briefly comment on possible ways to check whether a given
polynomial P ∈ C[x1, . . . , xg] is degenerate with respect to G
g when G = Ga or G = Gm.
In the latter case, it was shown by the second author [34] that the polynomial
∑

α∈E cαxα1
1 . . . xαg
g ,

where E ⊆ Cg is a finite, non-empty set and cα ̸= 0 for all α ∈ E, is non-degenerate if and
only if {
∑
α∈E zα · α : zα ∈ C} = Cg.
We will now provide a criterion to check whether a polynomial P ∈ C[x1, . . . , xg] is
non-degenerate with respect to Gg
a.

Lemma B.1. If P ∈ C[x1, . . . , xg] is degenerate with respect to Gg
a, then there exists non-
zero v ∈ C
g such that the identity

v · ((∇P )(x1, . . . , xg)) = 0

holds.

Proof. Let V be given by the variety P (x) = t, where, by abuse of notation, we denote
x = (x1, . . . , xg). Since G = Ga and V is degenerate, one can deduce that

P (x) = F (L1, . . . , Lk)

for some 0 ≤ k < g and some linear forms L1, . . . , Lk ∈ C[x1, . . . , xg] and some F ∈
C[y1, . . . , yk]. Since k < g, there exists some non-zero v = (v1, . . . , vg) ∈ C
g such that the
identity Li(x) = Li(x + t · v)
holds for all 1 ≤ i ≤ k and all t ∈ R. Here t · v = (tv1, . . . , tvg). In particular, we have the
identity P (x) = P (x + t · v).

28 JOSEPH HARRISON, AKSHAT MUDGAL, HARRY SCHMIDT

Differentiating with respect to t, we get that

0 =
 k∑

j=1
 ( ∂F
∂yj
 ) (L1(x + t · v), . . . , Lk(x + t · v)) ·
 g∑

l=1
 ( ∂Lj
∂xl
 ) (x + t · v) · vl

for all t ∈ R. Setting t = 0 and rearranging the sums, we get that

0 =
 g∑

l=1 vl
 ( k∑

j=1
 ( ∂F
∂yj
 ) (L1(x), . . . , Lk(x)) · (∂Lj
∂xl
 ) (x)
)
 = v · ((∇P )(x)). □

We will use this to prove that the polynomial P (x, y, z) = xy + yz + zx is non-degenerate
with respect to G
3
a. Indeed, if P were to be degenerate with respect to G3
a, then Lemma B.1
implies that there would exist some non-zero v = (v1, v2, v3) ∈ C3 such that the identity

v · ((∇P )(x, y, z)) = v1(y + z) + v2(x + y) + v3(z + x) = 0

holds. In particular, this would mean that

v1 + v2 = v2 + v3 = v3 + v1 = 0,

that is, v1 = v2 = v3 = 0. This contradicts the hypothesis that v is non-zero, and so, P
must be non-degenerate with respect to G
3
a.

References

1. Martin Bays and Emmanuel Breuillard, Projective geometries arising from Elekes-Szab´o problems, Ann.
Sci. ´Ec. Norm. Sup´er. (4) 54 (2021), no. 3, 627–681. MR 4311096
2. E. Bombieri and U. Zannier, Heights of algebraic points on subvarieties of abelian varieties, Ann. Sc.
Norm. Super. Pisa, Cl. Sci., IV. Ser. 23 (1996), no. 4, 779–792 (English).
3. Jean Bourgain and Mei-Chu Chang, On the size of k-fold sum and product sets of integers, J. Amer.
Math. Soc. 17 (2004), no. 2, 473–497. MR 2051619
4. A. Bremner, J. H. Silverman, and N. Tzanakis, Integral points in arithmetic progression on y2 =
x(x2 − n2), J. Number Theory 80 (2000), no. 2, 187–208 (English).
5. Andrew Bremner, On arithmetic progressions on elliptic curves, Experiment. Math. 8 (1999), no. 4,
409–413. MR 1737236
6. Andrew Bremner and Maciej Ulas, Rational points in geometric progressions on certain hyperelliptic
curves, Publ. Math. Debr. 82 (2013), no. 3-4, 669–683 (English).
7. Mei-Chu Chang, Some consequences of the polynomial Freiman-Ruzsa conjecture, C. R. Math. Acad.
Sci. Paris 347 (2009), no. 11-12, 583–588. MR 2532910
8. Artem Chernikov, Ya’acov Peterzil, and Sergei Starchenko, Model-theoretic Elekes-Szab´o for stable and
o-minimal hypergraphs, Duke Math. J. 173 (2024), no. 3, 419–512. MR 4729440
9. Artem Chernikov and Sergei Starchenko, Model-theoretic Elekes-Szab´o in the strongly minimal case, J.
Math. Log. 21 (2021), no. 2, Paper No. 2150004, 20. MR 4290493
10. Adam Cushman, A note on the sum-product problem and the convex sumset problem, arXiv:2512.13849.
11. Sinnou David and Patrice Philippon, Minorations des hauteurs normalis´ees des sous-vari´et´es des
puissances des courbes elliptiques, Int. Math. Res. Pap. IMRP (2007), no. 3, Art. ID rpm006, 113.
MR 2355454
12. Gy¨orgy Elekes, On the number of sums and products, Acta Arith. 81 (1997), no. 4, 365–367. MR 1472816
13. Gy¨orgy Elekes and Lajos R´onyai, A combinatorial problem on polynomials and rational functions, J.
Combin. Theory Ser. A 89 (2000), no. 1, 1–20. MR 1736139
14. Gy¨orgy Elekes and Endre Szab´o, How to find groups? (and how to use them in Erd¨os geometry?),
Combinatorica 32 (2012), no. 5, 537–571. MR 3004808
15. N. D. Elkies and Z. Klagsbrun, Z
29 in E(Q), Number theory list server archives, 2024.

SUM-PRODUCT PHENOMENON FOR ALGEBRAIC GROUPS AND BREMNER’S CONJECTURE 29

16. Noam D. Elkies and Zev Klagsbrun, New rank records for elliptic curves having rational torsion, ANTS
XIV. Proceedings of the fourteenth algorithmic number theory symposium, Auckland, New Zealand,
virtual event, June 29 – July 4, 2020, Berkeley, CA: Mathematical Sciences Publishers (MSP), 2020,
pp. 233–250 (English).
17. Paul Erd˝os and E. Szemer´edi, On sums and products of integers, Studies in Pure Mathematics, Mem.
of P. Tur´an, 213-218 (1983)., 1983.
18. J.-H. Evertse, H. P. Schlickewei, and W. M. Schmidt, Linear equations in variables which lie in a
multiplicative group, Ann. Math. (2) 155 (2002), no. 3, 807–836 (English).
19. G. Faltings, Endlichkeitss¨atze f¨ur abelsche Variet¨aten ¨uber Zahlk¨orpern, Invent. Math. 73 (1983), no. 3,
349–366. MR 718935
20. William Fulton, Intersection theory., 2nd ed. ed., Ergeb. Math. Grenzgeb., 3. Folge, vol. 2, Berlin:
Springer, 1998 (English).
21. Natalia Garcia-Fritz and Hector Pasten, Elliptic curves with long arithmetic progressions have large
rank, Int. Math. Res. Not. IMRN (2021), no. 10, 7394–7432. MR 4259152
22. W. T. Gowers, Ben Green, Freddie Manners, and Terence Tao, On a conjecture of Marton, Ann. of
Math. (2) 201 (2025), no. 2, 515–549. MR 4880432
23. A. Grothendieck, ´El´ements de g´eom´etrie alg´ebrique. IV: ´Etude locale des sch´emas et des morphismes de
sch´emas (Quatri`eme partie). R´edig´e avec la colloboration de J. Dieudonn´e, Publ. Math., Inst. Hautes
´Etud. Sci. 32 (1967), 1–361 (French).
24. Brandon Hanson, Oliver Roche-Newton, and Dmitrii Zhelezov, On iterated product sets with shifts, II,
Algebra Number Theory 14 (2020), no. 8, 2239–2260. MR 4172707
25. Marc Hindry and Joseph H. Silverman, Diophantine geometry. An introduction, Grad. Texts Math.,
vol. 201, New York, NY: Springer, 2000 (English).
26. Yifan Jing, Souktik Roy, and Chieu-Minh Tran, Semialgebraic methods and generalized sum-product
phenomena, Discrete Anal. (2022), Paper No. 18, 23. MR 4527758
27. Gareth Jones and Harry Schmidt, Pfaffian definitions of Weierstrass elliptic functions, Math. Ann. 379
(2021), no. 1-2, 825–864. MR 4211105
28. Mohamed Kamel and Mohammad Sadek, Sequences of consecutive squares on quartic elliptic curves,
Funct. Approximatio, Comment. Math. 60 (2019), no. 2, 245–252 (English).
29. Michel Laurent, ´Equations diophantiennes exponentielles, Invent. Math. 78 (1984), no. 2, 299–327.
MR 767195
30. John M. Lee, Introduction to smooth manifolds, 2nd revised ed ed., Grad. Texts Math., vol. 218, New
York, NY: Springer, 2013 (English).
31. D. W. Masser and G. W¨ustholz, Estimating isogenies on elliptic curves, Invent. Math. 100 (1990),
no. 1, 1–24 (English).
32. J. S. Milne, Algebraic groups. The theory of group schemes of finite type over a field, Camb. Stud. Adv.
Math., vol. 170, Cambridge: Cambridge University Press, 2017 (English).
33. Akshat Mudgal, On commuting pairs in arbitrary sets of 2 × 2 matrices, arXiv:2411.10404.
34. , An Elekes-R´onyai theorem for sets with few products, Int. Math. Res. Not. IMRN (2024), no. 13,
10410–10424. MR 4770374
35. , Unbounded expansion of polynomials and products, Math. Ann. 390 (2024), no. 1, 381–415.
MR 4800917
36. D¨om¨ot¨or P´alv¨olgyi and Dmitrii Zhelezov, Query complexity and the polynomial Freiman-Ruzsa conjec-
ture, Adv. Math. 392 (2021), Paper No. 108043, 18. MR 4319771
37. Orit E. Raz, Micha Sharir, and Frank De Zeeuw, Polynomials vanishing on Cartesian products: the
Elekes-Szab´o theorem revisited, Duke Math. J. 165 (2016), no. 18, 3517–3566. MR 3577370
38. Orit E. Raz, Micha Sharir, and J´ozsef Solymosi, Polynomials vanishing on grids: the Elekes-R´onyai
problem revisited, Amer. J. Math. 138 (2016), no. 4, 1029–1065. MR 3538150
39. Igor R. Shafarevich, Basic algebraic geometry 1. Varieties in projective space. Translated from the Rus-
sian by Miles Reid, 3rd ed. ed., Berlin: Springer, 2013 (English).
40. Joseph H. Silverman, The arithmetic of elliptic curves, 2nd ed. ed., Grad. Texts Math., vol. 106, New
York, NY: Springer, 2009 (English).

30 JOSEPH HARRISON, AKSHAT MUDGAL, HARRY SCHMIDT

41. J´ozsef Solymosi, Bounding multiplicative energy by the sumset, Adv. Math. 222 (2009), no. 2, 402–408.
MR 2538014
42. Jozsef Solymosi and Joshua Zahl, Improved Elekes-Szab´o type estimates using proximity, J. Combin.
Theory Ser. A 201 (2024), Paper No. 105813, 9. MR 4638826

Mathematics Institute, Zeeman Building, University of Warwick, Coventry CV4 7AL,
United Kingdom
Email address: joseph.s.harrison@warwick.ac.uk
Email address: Akshat.Mudgal@warwick.ac.uk
Email address: Harry.Schmidt@warwick.ac.uk
