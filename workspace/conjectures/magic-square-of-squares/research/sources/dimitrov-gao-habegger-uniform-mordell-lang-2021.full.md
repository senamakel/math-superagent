<!-- source: https://arxiv.org/pdf/2001.10276 | converted from PDF -->

arXiv:2001.10276v3  [math.NT]  31 Mar 2021
UNIFORMITY IN MORDELL–LANG FOR CURVES

VESSELIN DIMITROV, ZIYANG GAO AND PHILIPP HABEGGER

Abstract. Consider a smooth, geometrically irreducible, projective curve of genus
g ≥ 2 deﬁned over a number ﬁeld of degree d ≥ 1. It has at most ﬁnitely many rational
points by the Mordell Conjecture, a theorem of Faltings. We show that the number
of rational points is bounded only in terms of g, d, and the Mordell–Weil rank of the
curve’s Jacobian, thereby answering in the aﬃrmative a question of Mazur. In addition
we obtain uniform bounds, in g and d, for the number of geometric torsion points of the
Jacobian which lie in the image of an Abel–Jacobi map. Both estimates generalize our
previous work for 1-parameter families. Our proof uses Vojta’s approach to the Mordell
Conjecture, and the key new ingredient is the generalization of a height inequality due
to the second- and third-named authors.

Contents

1. Introduction 1
2. Betti map and Betti form 7
3. Setup and notation for the height inequality 13
4. Intersection theory and height inequality on the total space 16
5. Proof of the height inequality Theorem 1.6 22
6. Preparation for counting points 23
7. N´eron–Tate distance between points on curves 29
8. Proof of Theorems 1.1, 1.2, and 1.4 31
Appendix A. The Silverman–Tate Theorem revisited 36
Appendix B. Full version of Theorem 1.6 40
References 47

1. Introduction

Let F be a ﬁeld. By a curve deﬁned over F we mean a geometrically irreducible,
projective variety of dimension 1 deﬁned over F . Let C be a smooth curve of genus at
least 2 deﬁned over a number ﬁeld F . As was conjectured by Mordell and proved by
Faltings [Fal83], C(F ), the set of F -rational points of C, is ﬁnite.
We let Jac(C) denote the Jacobian of C. Recall that Jac(C)(F ) is a ﬁnitely generated
abelian group by the Mordell–Weil Theorem.
The aim of this paper is to bound #C(F ) from above. Here is our ﬁrst result.

Theorem 1.1. Let g ≥ 2 and d ≥ 1 be integers. Then there exists a constant c =
c(g, d) ≥ 1 with the following property. If C is a smooth curve of genus g deﬁned over a

2000 Mathematics Subject Classiﬁcation. 11G30, 11G50, 14G05, 14G25.

1

UNIFORMITY IN MORDELL–LANG FOR CURVES 2

number ﬁeld F with [F : Q] ≤ d, then

(1.1) #C(F ) ≤ c1+ρ

where ρ is the rank of Jac(C)(F ).

This theorem gives an aﬃrmative answer to a question posed by Mazur [Maz00,
Page 223]. See also [Maz86, top of page 234] for an earlier question. Before this, Lang
formulated a related conjecture [Lan78, page 140] on the number of integral points of
elliptic curves.
The method of our theorem builds up on the work of many others. At the core we
follow Vojta’s proof [Voj91] of the Mordell Conjecture. Vojta’s proof was later simpliﬁed
by Bombieri [Bom90] and further developed by Faltings [Fal91]. Silverman [Sil93] proved
a bound of the quality (1.1) if C ranges over twists of a given smooth curve. The bound
by de Diego [dD97] is of the form c(g)7ρ, where c(g) > 0 depends only on g; the value 7
had already arisen in Bombieri’s work. But she only counts points whose height is large
in terms of a height of C. Work of David–Philippon [DP02] and R´emond [R´em00a] led
to explicit estimates. Recently, Alpoge [Alp18] [Alp20, Theorem 6.1.1] improved 7 to
1.872 and, for g large enough, even to 1.311.
On combining the Vojta and Mumford Inequalities one gets an upper bound for the
number of large points in C(F ); these are points whose height is suﬃciently large relative
to a suitable height of C. A lower bound for the N´eron–Tate height, such as proved by
David–Philippon [DP02], can be used to count the number of remaining points which we
sometimes call small points. Indeed, R´emond [R´em00a] made the Vojta and Mumford
Inequalities explicit and obtained explicit upper bounds for the number of rational points
on curves embedded in abelian varieties. The resulting cardinality bounds depend on a
suitable notion of height of C, an artifact of the lower bounds for the N´eron–Tate height.
Later, David–Philippon [DP07] proved stronger height lower bounds in a power of an
elliptic curve. They then obtained uniform estimates of the quality (1.1) for a curve in
a power of elliptic curves, thus providing evidence that Mazur’s Question had a positive
answer, see also David–Nakamaye–Philippon’s work [DNP07].
We give an overview of the general method in more detail in §1.1 below.
The main innovation of this paper is to prove a lower bound for the N´eron–Tate height
that is suﬃciently strong to eliminate the dependency on the height of C. This leads
to a uniform estimate as in Theorem 1.1. In prior work [DGH19] we applied the earlier
height lower bound [GH19] to recover a variant of Theorem 1.1 in a one-parameter family
of smooth curves.
We now explain some further results that follow from the approach described above.
For an integer g ≥ 1, let Ag,1 denote the coarse moduli space of principally polarized
abelian varieties of dimension g. This is an irreducible quasi-projective variety which we
can take as deﬁned over Q, the algebraic closure of Q in C. Suppose we are presented
with an immersion ι : Ag,1 → Pm
Q into projective space. Let h : Pm
Q (Q) → R denote the
absolute logarithmic Weil height, cf. [BG06, §1.5.1]. For brevity, we sometimes call h
the Weil height. If C is a smooth curve of genus g ≥ 2 deﬁned over Q and if P0 ∈ C(Q),
then we can consider C − P0 as a curve in Jac(C) via the Abel–Jacobi map. We use
[Jac(C)] to denote the point in Ag,1(Q) parametrizing Jac(C).

UNIFORMITY IN MORDELL–LANG FOR CURVES 3

An abelian group Γ is said to have ﬁnite rank if Γ ⊗ Q is a ﬁnite dimensional Q-vector
space. In this case dim Γ⊗Q is the rank of Γ. Consider an abelian variety A deﬁned over
C and let Γ be a ﬁnite rank subgroup of A(C). Lang [Lan65] conjectured that a curve
in A intersects Γ in a ﬁnite set unless the curve is smooth of genus 1. The Conjecture
follows from Faltings’s Theorem [Fal83] and work of Raynaud [Ray83].
The following theorem is more in the spirit of [Maz86, top of page 234].

Theorem 1.2. Let g ≥ 2 and let ι be as above. Then there exist two constants c1 =
c1(g, ι) ≥ 0 and c2 = c2(g, ι) ≥ 1 with the following property. Let C be a smooth curve
of genus g deﬁned over Q, let P0 ∈ C(Q), and let Γ be a subgroup of Jac(C)(Q) of ﬁnite
rank ρ ≥ 0. If h(ι([Jac(C)])) ≥ c1, then

#(C(Q) − P0) ∩ Γ ≤ c1+ρ
2 .

The following corollary follows from Theorem 1.2 applied to Γ = Jac(C)(Q)tors, which
has rank 0.

Corollary 1.3. Let g ≥ 2 and let ι be as above. Then there exist two constants c1 =
c1(g, ι) ≥ 0 and c2 = c2(g, ι) ≥ 1 with the following property. Let C be a smooth curve
of genus g deﬁned over Q and let P0 ∈ C(Q). If h(ι([Jac(C)])) ≥ c1, then

#(C(Q) − P0) ∩ Jac(C)(Q)tors ≤ c2.

As in Theorem 1.1 we can drop the condition on the height of the Jacobian by working
over a number ﬁeld of bounded degree.

Theorem 1.4. Let g ≥ 2 and d ≥ 1 be integers. Then there exists a constant c =
c(g, d) ≥ 1 with the following property. Let C be a smooth curve of genus g deﬁned over
a number ﬁeld F ⊆ Q with [F : Q] ≤ d and let P0 ∈ C(Q), then

#(C(Q) − P0) ∩ Jac(C)(Q)tors ≤ c.

Let us recall some previous results towards Mazur’s Question for rational points, i.e.,
towards Theorem 1.1. Based on the method of Vojta, Alpoge [Alp18] proved that the
average number of rational points on a curve of genus 2 with a marked Weierstrass point
is bounded. Let C be a smooth curve of genus g ≥ 2 deﬁned over a number ﬁeld F ⊆ Q.
The Chabauty–Coleman approach [Cha41, Col85] yields estimates under an additional
hypothesis on the rank of Mordell–Weil group. For example, if Jac(C)(F ) has rank at
most g − 3, Stoll [Sto19] showed that #C(F ) is bounded solely in terms of [F : Q]
and g if C is hyperelliptic; Katz–Rabinoﬀ–Zureick-Brown [KRZB16] later, under the
same rank hypothesis, removed the hyperelliptic hypothesis. Checcoli, Veneziano, and
Viada [CVV17] obtain an eﬀective height bound under a restriction on the Mordell–Weil
rank.
As for algebraic torsion points, i.e., in the direction of Theorem 1.4, DeMarco–Krieger–
Ye [DKY20] proved a bound on the cardinality of torsion points on any genus 2 curve
that admits a degree-two map to an elliptic curve when the Abel–Jacobi map is based
at a Weierstrass point. Moreover, their bound is independent of [F : Q].

1.1. N´eron–Tate distance of algebraic points on curves. Let C be a smooth curve
deﬁned over Q of genus g ≥ 2, let P0 ∈ C(Q), and let Γ be a subgroup of Jac(C)(Q)

UNIFORMITY IN MORDELL–LANG FOR CURVES 4

of ﬁnite rank ρ. For simplicity we identify C with its image under the Abel–Jacobi
embedding C → Jac(C) via P0.
Our proof of Theorem 1.2 follows the spirit of the method of Vojta, later generalized by
Faltings. Let ˆh : Jac(C)(Q) → R denote the N´eron–Tate height attached to a symmetric
and ample line bundle on Jac(C). We divide C(Q) ∩ Γ into two parts:

• Small points {
P ∈ C(Q) ∩ Γ : ˆh(P ) ≤ B(C)}
;

• Large points {P ∈ C(Q) ∩ Γ : ˆh(P ) > B(C)}

where B(C) is allowed to depend on a suitable height of C. It turns out that we can take
B(C) = c0 max{1, h(ι([Jac(C)]))} for some c0 = c0(g, ι) > 0. The constant c0 is chosen
in a way that accommodates both the Mumford inequality and the Vojta inequality.
Combining these two inequalities yields an upper bound on the number of large points
by c1(g)1+ρ, see for example Vojta’s [Voj91, Theorem 6.1] in the important case where
Γ is the group of points of Jac(C) rational over a number ﬁeld or more generally in the
work of David–Philippon [DP02, DP07] and R´emond [R´em00a].
Thus in order to prove Theorem 1.2, it suﬃces to bound the number of small points.
In this paper we ﬁnd such a bound by studying the N´eron–Tate distance of points in
C(Q).
Roughly speaking, we ﬁnd positive constants c1, c2, c3, and c4 that depend on g and
ι, but not on C, such that if h(ι([Jac(C)])) ≥ c1 then for all P ∈ C(Q) we have the
following alternative.
• Either P lies in a subset of C(Q) of cardinality at most c2,
• or {
Q ∈ C(Q) : ˆh(Q − P ) ≤ h(ι([Jac(C)]))/c3} < c4.

This dichotomy is stated in Proposition 7.1. In this paper, we make the statement
precise by referring to the universal family of genus g smooth curves with suitable level
structure, and the N´eron–Tate height on each Jacobian attached to the tautological line
bundle. The setup is done in §6.
This proposition can be seen as a relative version of the Bogomolov conjecture for
abelian varieties with large height. It has the following upshot: If h(ι([Jac(C)])) ≥ c1,
then the small points in C(Q) ∩ Γ lie in a set of uniformly bounded cardinality, or are
contained in (1 + c0c3)ρ balls in the N´eron–Tate metric, with each ball containing at
most c4 points. This will yield the desired bound in Theorem 1.2, as executed in §8.

1.2. Height inequality and non-degeneracy. We follow the framework presented in
our previous work [DGH19]. In loc.cit. we proved the result for 1-parameter families, as
an application of the second- and third-named authors’ height inequality [GH19, Theo-
rem 1.4]. Passing to general cases requires generalizing this height inequality to higher
dimensional bases. The generalization has two parts: generalizing the inequality itself
under the non-degeneracy condition and generalizing the criterion of non-degenerate
subvarieties. We execute the ﬁrst part in the current paper while the second part was
done by the second-named author in [Gao20a]. Let us explain the setup.
Let k be an algebraically closed subﬁeld of C. Let S be a regular, irreducible, quasi-
projective variety deﬁned over k that is Zariski open in an irreducible projective variety
S ⊆ Pm
k . Let π : A → S be an abelian scheme of relative dimension g ≥ 1. We suppose
that we are presented with a closed immersion A → Pn
k × S over S. On the generic ﬁber

UNIFORMITY IN MORDELL–LANG FOR CURVES 5

of π we assume that this immersion comes from a basis of the global sections of the l-th
power of a symmetric and ample line bundle with l ≥ 4. If k = Q and as described in
§3.1 we obtain two height functions, the restriction of the Weil height h : S(Q) → R and
the N´eron–Tate height ˆhA : A(Q) → R.
Let ℓ ≥ 3 be an integer. Throughout the whole paper, by level-ℓ-structure we always
mean symplectic level-ℓ-structure. For the purpose of our main applications, including
Theorems 1.1 and 1.2, it suﬃces to work under the following hypothesis.
(Hyp): A → S carries a principal polarization and has level-ℓ-structure for some ℓ ≥ 3.
So in the main body of the paper, we will focus on the case (Hyp). The general case
where (Hyp) is not assumed will be handled in Appendix B.
The non-degenerate subvarieties of A are deﬁned using the Betti map which we brieﬂy
describe here; the precise deﬁnition will be given by Proposition B.2 and in Proposi-
tion 2.1 under (Hyp).
For any s ∈ S(C), there exists an open neighborhood ∆ ⊆ San of s which we may
assume is simply-connected. Then one can deﬁne a basis ω1(s), . . . , ω2g(s) of the period
lattice of each ﬁber s ∈ ∆ as holomorphic functions of s. Now each ﬁber As = π−1(s)
can be identiﬁed with the complex torus Cg/(Zω1(s)⊕· · ·⊕Zω2g(s)), and each point x ∈
As(C) can be expressed as the class of ∑2g
i=1 bi(x)ωi(s) for real numbers b1(x), . . . , b2g(x).
Then b∆(x) is deﬁned to be the class of the 2g-tuple (b1(x), . . . , b2g(x)) ∈ R2g modulo
Z
2g. We obtain with a real-analytic map

b∆ : A∆ = π−1(∆) → T
2g,

which is ﬁberwise a group isomorphism and where T
2g is the real torus of dimension 2g.

Deﬁnition 1.5. An irreducible subvariety X of A is said to be non-degenerate if there
exists an open non-empty subset ∆ of San, with the Betti map b∆ : A∆ := π−1(∆) → T
2g,
such that

(1.2) max
x∈X sm,an∩A∆ rankR(db∆|X sm,an)x = 2 dim X

where db∆ denotes the diﬀerential and X sm,an is the analytiﬁcation of the regular locus
of X.

As the inequality ≤ in (1.2) trivially holds true, (1.2) is equivalent to: there exists
x ∈ X sm,an ∩ A∆ such that rankR(db∆|X sm,an)x = 2 dim X.
In Proposition 2.2(iii) we give another characterization of non-degenerate subvarieties.
We can now formulate the height inequality.

Theorem 1.6. Suppose that A and S are as above with k = Q; in particular, A satisﬁes
(Hyp). Let X be a closed irreducible subvariety of A deﬁned over Q that dominates S.
Suppose X is non-degenerate, as deﬁned in Deﬁnition 1.5. Then there exist constants
c1 > 0 and c2 ≥ 0 and a Zariski open dense subset U of X with
ˆhA(P ) ≥ c1h(π(P )) − c2 for all P ∈ U(Q).

Note that [GH19, Theorem 1.4] is, up to some minor reduction, precisely Theorem 1.6
for dim S = 1 together with the criterion for X to be non-degenerate when dim S = 1.
In general, the degeneracy behavior of X is fully studied in [Gao20a]. See [Gao20a, The-
orem 1.1] for the criterion. However in practice, we sometimes still want to understand

UNIFORMITY IN MORDELL–LANG FOR CURVES 6

the height comparison on some degenerate X. One way to achieve this is by apply-
ing [Gao20a, Theorem 1.3], which asserts the following statement: If X satisﬁes some
reasonable properties, then we can apply Theorem 1.6 after doing some simple operations
with X.
For the purpose of proving Proposition 7.1 and furthermore Theorem 1.2, we work in
the following situation.
Let Ag,ℓ denote the moduli space of principally polarized g-dimensional abelian vari-
eties with level-ℓ-structure. It is a classical fact that Ag,ℓ is represented by an irreducible,
regular, quasi-projective variety deﬁned over a number ﬁeld, see [MFK94, Theorem 7.9
and below] or [OS80, Theorem 1.9], so it is a ﬁne moduli space. Let Mg,ℓ be the ﬁne mod-
uli space of smooth curves of genus g whose Jacobian is equipped with level-ℓ-structure;
see [DM69, (5.14)] or [OS80, Theorem 1.8] for the existence. Then Mg,ℓ is an irreducible,
regular, quasi-projective variety deﬁned over a number ﬁeld.
To avoid confusion on diﬀerent notations in diﬀerent references, we make the following
convention throughout the paper. We will take Ag,ℓ and Mg,ℓ as geometrically irreducible
varieties. Some authors deﬁne Ag,ℓ over Z[1/ℓ] (or over Z) and then consider it over
Q by base change. The Q-variety thus obtained may not be irreducible, and each
irreducible component is deﬁned over Q(ζℓ) for some root of unity ζℓ of order ℓ. Choosing
a geometrically irreducible component of Ag,ℓ amounts to ﬁxing a complex root of unity
of order ℓ. We ﬁx such a choice once and for all and consider Ag,ℓ as an irreducible
variety deﬁned over Q. The same holds for Mg,ℓ. We will usually ﬁx ℓ and abbreviate
Ag,ℓ (resp. Mg,ℓ) by Ag (resp. Mg). It is often convenient to consider Ag and Mg as over
Q, but sometimes we will recall that both arise from varieties deﬁned over the number
ﬁeld Q(ζℓ). We denote the coarse moduli space of smooth curves of genus g with Mg,1.
Furthermore, let Cg → Mg be the universal curve and Ag → Ag be the universal
abelian variety. Taking the Jacobian of a smooth curve leads to the Torelli morphism
Mg → Ag which is ﬁnite-to-1 (but not injective as we have level structure). Moreover, for
M ≥ 2 let DM denote the M-th Faltings–Zhang morphism ﬁberwise deﬁned by sending

(1.3) (P0, P1, . . . , PM ) ↦→ (P1 − P0, . . . , PM − P0);

we give a precise deﬁnition of this morphism in §6.1. Roughly speaking, we will apply
Theorem 1.6 to
 X := DM (Cg ×Mg · · · ×Mg Cg
︸ ︷︷ ︸
(M +1)-copies
 ) ⊆ Ag ×Mg · · · ×Mg Ag
︸ ︷︷ ︸
M -copies

for a suitable M. To verify non-degeneracy we will refer to the second-named author’s
work [Gao20a, Theorem 1.2’] which applies if M is large in terms of g. So we can apply
Theorem 1.6 to such X. This will eventually lead to Proposition 7.1.
The morphism and its variants are powerful tools in diophantine geometry, see [Fal91,
Lemma 4.1]. It is closely connected to problems involving small N´eron–Tate height,
see [Zha98, Lemma 3.1]. Stoll [Sto19] used a variant of (1.3) to show that a conjec-
ture of Pink [Pin05b] on unlikely intersections implies Theorem 1.2 with the condition
h(ι([Jac(C)])) ≥ c1 removed and with C allowed to be deﬁned over C.
At this stage it is worth outlining the main steps of the proof of [Gao20a, Theorem 1.2’],
or the more general [Gao20a, Theorem 1.3], due to its importance to the current paper.
The major step is to establish a criterion, in simple geometric terms, for an irreducible

UNIFORMITY IN MORDELL–LANG FOR CURVES 7

subvariety X of the universal abelian variety Ag to be degenerate. Roughly speaking, the
proof of the desired criterion is divided into two steps. Step 1 transfers the degeneracy
property to an unlikely intersection problem in Ag by invoking the mixed Ax–Schanuel
theorem for Ag [Gao20b, Theorem 1.1]. More precisely we show that X is degenerate if
and only if X is the union of subvarieties satisfying an appropriate unlikely intersection
property. Step 2 solves this unlikely intersection problem, and the key point is to use
[Gao20b, Theorem 1.4] to prove that the union mentioned above is a ﬁnite union. In
this step the notion of weakly optimal subvarieties introduced by the third-named author
and Pila [HP16] is involved.

1.3. General notation. We collect here an overview of notation used throughout the
text.
Let S be an irreducible, quasi-projective variety deﬁned over an algebraically closed
ﬁeld k. Then Ssm denotes the regular locus of X. If π : A → S is an abelian scheme
then [N] : A → A is the multiplication-by-N morphism for all N ∈ N = {1, 2, 3, . . .},
and if s ∈ S(k), the ﬁber As = π−1(s) is an abelian variety deﬁned over k. If k ⊆ C,
then San denotes the analytiﬁcation of S; it carries a natural topology that is Hausdorﬀ.
We write T for the circle group {z ∈ C : |z| = 1}.

Acknowledgements. The authors would like to thank Shou-wu Zhang for relevant
discussions and Gabriel Dill for the argument involving torsion points to bound h1 on
page 32. We would also like to thank Lars K¨uhne and Ngaiming Mok for discussions
on Hermitian Geometry; our paper is much inﬂuenced by K¨uhne’s approach towards
bounded height [K¨uh20] and by Mok’s approach to study the Mordell–Weil rank over
function ﬁelds [Mok91]. We thank Gabriel Dill, Lars K¨uhne, Fabien Pazuki, and Joseph
H. Silverman for corrections and comments on a draft of this paper. We also thank the
referees for their careful reading and valuable comments. VD would like to thank the
NSF and the Giorgio and Elena Petronio Fellowship Fund II for ﬁnancial support for
this work. VD has received funding from the European Union’s Seventh Framework Pro-
gramme (FP7/2007–2013) / ERC grant agreement n
◦ 617129. ZG has received funding
from the French National Research Agency grant ANR-19-ERC7-0004, and the Euro-
pean Research Council (ERC) under the European Union’s Horizon 2020 research and
innovation programme (grant agreement n
◦ 945714). PH has received funding from the
Swiss National Science Foundation project n
◦ 200020 184623. Both VD and ZG would
like to thank the Institute for Advanced Study and the special year “Locally Symmetric
Spaces: Analytical and Topological Aspects” for its hospitality during this work.

2. Betti map and Betti form

The goals of this section are to revisit the Betti map, the Betti form and make a
link between them. In this paper we construct the Betti map using the universal family
of principally polarized abelian varieties with level-ℓ-structure and bypass the ad-hoc
construction found in [GH19].
In this section we will make the following assumptions. All varieties are deﬁned
over the ﬁeld C. Let S be an irreducible, regular, quasi-projective variety over C.
Let π : A → S be an abelian scheme of relative dimension g, that carries a principal

UNIFORMITY IN MORDELL–LANG FOR CURVES 8

polarization, and such that A is equipped with level-ℓ-structure, for some ℓ ≥ 3, i.e.,
(Hyp) is satisﬁed.

Proposition 2.1. Let s0 ∈ S(C). Then there exist an open neighborhood ∆ of s0 in San,
and a map b∆ : A∆ := π−1(∆) → T
2g, called the Betti map, with the following properties.
(i) For each s ∈ ∆ the restriction b∆|As(C) : As(C) → T
2g is a group isomorphism.
(ii) For each ξ ∈ T
2g the preimage b
−1
∆ (ξ) is a complex analytic subset of A∆.
(iii) The product (b∆, π) : A∆ → T
2g × ∆ is a real analytic isomorphism.

The properties (i) – (iii) do not uniquely determine b∆. Indeed, composing b∆ with an
automorphism of the topological group T
2g, i.e., an element of GL2g(Z), leads to a new
Betti map satisfying (i) – (iii). After shrinking ∆ we may assume that it is connected.
In this case, an application of the Baire Category Theorem shows that b∆ is uniquely
determined by (i) and (iii) up to composition with a unique element of GL2g(Z).
Andr´e, Corvaja, and Zannier [ACZ20] recently began the study of the maximal rank
of the Betti map, especially the submersivity, using a slightly diﬀerent deﬁnition. A
full study of this maximal rank was realized in [Gao20a]. Closely related to the Betti
map is the Betti form, a semi-positive (1, 1)-form on Aan, which was ﬁrst introduced in
Mok [Mok91].

Proposition 2.2. There exists a closed (1, 1)-form ω on Aan, called the Betti form, such
that the following properties hold.
(i) The (1, 1)-form ω is semi-positive, i.e., at each point the associated Hermitian
form is positive semi-deﬁnite.
(ii) For all N ∈ Z we have [N]∗ω = N 2ω.
(iii) If X is an irreducible subvariety of A of dimension d and ∆ ⊆ San is open with
X sm,an ∩ A∆ ̸= ∅, then

ω|∧d
X sm,an ̸≡ 0 if and only if max
x∈X sm,an∩A∆ rankR(db∆|X sm,an)x = 2d.

We will prove both propositions during the course of this section using the universal
abelian variety. A dynamical approach can be found in [CGHX21, §2].

2.1. Betti map for the universal abelian variety. Our proof of Proposition 2.1
follows the construction in [Gao20a, §3-§4]. We divide it into several steps.
We start to prove Proposition 2.1 for S = Ag, the moduli space of principally polarized
abelian variety of dimension g with level-ℓ-structure; it is a ﬁne moduli space. Let
πuniv : Ag → Ag be the universal abelian variety.
The universal covering Hg → Aan
g , where Hg is the Siegel upper half space, gives a
polarized family of abelian varieties AHg → Hg ﬁtting into the diagram

AHg := Ag ×Aan
g Hg uB //

  
 A
an
g

πuniv
  
Hg // Aan
g .

For the universal covering u : Cg × Hg → AHg and for each Z ∈ Hg, the kernel of u|Cg×{Z}
is Z
g + ZZ
g. Thus the map Cg × Hg → Rg × Rg × Hg → R2g, where the ﬁrst map is the

UNIFORMITY IN MORDELL–LANG FOR CURVES 9

inverse of (a, b, Z) ↦→ (a + Zb, Z) and the second map is the natural projection, descends
to a real analytic map b
univ : AHg → T
2g.

Now for each s0 ∈ Ag(C), there exists a contractible, relatively compact, open neigh-
borhood ∆ of s0 in Aan
g such that Ag,∆ := (πuniv)−1(∆) can be identiﬁed with AHg,∆′ for
some open subset ∆
′ of Hg. The composite b∆ : Ag,∆ ∼= AHg,∆′ → T
2g is real analytic
and satisﬁes the three properties listed in Proposition 2.1. Thus b∆ is the desired Betti
map in this case. Note that for a ﬁxed (small enough) ∆, there are inﬁnitely choices of
∆
′; but for ∆ small enough, if ∆
′
1 and ∆
′
2 are two such choices, then ∆
′
2 = α · ∆
′
1 for
some α ∈ Sp2g(Z) ⊆ SL2g(Z). Thus we have proved Proposition 2.1 for Ag → Ag.

2.2. Betti form for the universal abelian variety. For the universal covering u =
uB ◦ u : Cg × Hg → A
an
g , we will use (w, Z) to denote the coordinates on Cg × Hg. Below
Im denotes imaginary part.

Lemma 2.3. Deﬁne
 ˆωuniv := √−1∂∂ (2(Imw)
⊺(ImZ)−1(Imw)) .

Then ˆωuniv is a closed semi-positive (1, 1)-form on Cg × Hg satisfying

(2.1) ˆωuniv = √−1(dZY −1Im(w) − dw)⊺ ∧ Y −1 (dZY −1Im(w) − dw)

with Y = Im(Z); here and below the symbol ∧ is used as a combination of wedge product
and matrix multiplication when appropriate. Moreover, if N ∈ Z and if we denote by
̃N : Cg × Hg → Cg × Hg the map (w, Z) ↦→ (Nw, Z), then ̃N ∗ ˆωuniv = N 2 ˆωuniv.

Proof. The (1, 1)-form ˆωuniv is closed since d = ∂ + ∂. We will prove the semi-positivity
by direct computation.
We have the following formulae for partial derivatives

∂Imw = √−1
2 dw, ∂(Y −1) = − √−1
2 Y −1dZY −1,

∂Imw = −√−1
2 dw, ∂(Y −1) = √−1
2 Y −1dZY −1.

Let us prove the formulae on the right. We hereby do it for ∂(Y −1) = √−1
2 Y −1dZY −1 and
the other one is similar. Taking partial derivatives on both sides of Y Y −1 = I, we get
(∂Y )Y −1 + Y ∂(Y −1) = 0. So ∂(Y −1) = −Y −1(∂Y )Y −1. But ∂Y = ∂ImZ = − √−1
2 dZ.
Hence we get the desired formula for ∂(Y −1).
Using these formulae and the Leibniz rule (note that Z = Z
⊺ and hence dZ = dZ
⊺),
we get
 ˆωuniv = √−1((dw)
⊺Y −1 ∧ dw + (Imw)
⊺Y −1dZ ∧ Y −1dZY −1(Imw)

− (Imw)
⊺Y −1dZY −1 ∧ dw − (dw)
⊺ ∧ Y −1dZY −1(Imw))
.

Rearranging yields the desired equality (2.1). The associated form is

H : ((ξw, ξZ), (ηw, ηZ)) ↦→ (ξZY −1Im(w) − ξw)⊺Y −1 (ηZY −1Im(w) − ηw) ,

UNIFORMITY IN MORDELL–LANG FOR CURVES 10

for ξw, ηw ∈ Cg and ξZ, ηZ ∈ Matg(C) symmetric, is Hermitian and so ˆωuniv is real.
Moreover,
 H(
(ξw, ξZ), (ξw, ξZ)) = v
⊺Y −1v with v = ξZY −1Im(w) − ξw.

But Y is positive deﬁnite as a real symmetric matrix and thus positive deﬁnite as a
Hermitian matrix. We see that H is positive semi-deﬁnite and this implies that ˆωuniv is
positive semi-deﬁnite.
The “moreover” part of the lemma is clear. □

Next we want to show that ˆωuniv descends to a (1, 1)-form on A
an
g . To do this, we
ﬁrst show that ˆωuniv can be written in a simple form under an appropriate change of
coordinates.
Deﬁne the complex space X2g,a, which is the universal covering of A
an
g , as follows:

• As a real algebraic space, X2g,a := R2g × Hg.
• The complex structure on X2g,a is given by

(2.2) R2g × Hg = Rg × Rg × Hg ∼= Cg × Hg, (a, b, Z) ↦→ (a + Zb, Z).

Lemma 2.4. Let ˆωuniv be as in Lemma 2.3. Then under the change of coordinates (2.2),
we have ˆωuniv = 2(da)
⊺ ∧ db.

Proof. For the moment we write Z = X + √
−1Y with X and Y the real and imaginary
part of Z ∈ Hg, respectively. Note that w = a + Zb = (a + Xb) + √−1Y b. Hence
Y −1(Imw) = b and dw = da + Zdb + dZb. Using this and noting that Z is symmetric,
we have that (2.1) becomes

ˆωuniv = √−1 (√−1(db)
⊺Y + (db)
⊺X + (da)
⊺) ∧ Y −1 (da + Xdb − √−1Y db
)

= √−1(√−1(db)
⊺ ∧ da + (db)
⊺ ∧ Y db + (db)
⊺X ∧ Y −1da + (db)
⊺X ∧ Y −1Xdb+

(da)
⊺ ∧ Y −1da + (da)
⊺ ∧ Y −1Xdb − √−1(da)
⊺ ∧ db
).

Many terms will vanish. Indeed, if M is a matrix, then (db)
⊺ ∧ Mda = −(da)
⊺ ∧ M
⊺db.
As (XY −1)

⊺ = Y −1X and as (db)
⊺X ∧Y −1da = (db)
⊺ ∧XY −1da we ﬁnd (db)
⊺X ∧Y −1da+
(da)
⊺ ∧ Y −1Xdb = 0. Observe that Y is symmetric, and so (db)
⊺ ∧ Y db = −(db)
⊺ ∧ Y db
vanishes. Arguing along the same line and using that Y −1 and XY −1X are symmetric
we ﬁnd (da)
⊺ ∧ Y −1da = 0 and (db)
⊺X ∧ Y −1X = (db)
⊺ ∧ XY −1Xdb = 0. We are left
with ˆωuniv = 2(da)
⊺ ∧ db. □

Corollary 2.5. Let ˆC be an irreducible, 1-dimensional, complex analytic subset of an
open subset of X2g,a = R2g × Hg and ˆC sm its smooth locus. Then ˆωuniv restricted to ˆC sm

is trivial if and only if ˆC ⊆ {r} × Hg for some r ∈ R2g.

Proof. First, assume that the coordinates (a, b) of R2g are constant on ˆC. Then ˆωuniv,
which is simply 2(da)
⊺ ∧ db by Lemma 2.4, vanishes on ˆC sm.
Conversely, suppose that ˆωuniv vanishes identically on ˆC sm. This time we use (2.1)
from Lemma 2.3. As Y −1 is positive deﬁnite we ﬁnd dZY −1Im(w) = dw on ˆC sm. Using
the change of coordinates w = a + Zb we deduce Im(w) = Y b and dw = da + dZb + Zdb.
So dZb = dZY −1Im(w) = dw = da + dZb + Zdb on ˆC sm. This equality simpliﬁes to

UNIFORMITY IN MORDELL–LANG FOR CURVES 11

da+Zdb = 0 on ˆC sm. As a and b are real valued and as Z ∈ Hg we conclude da = db = 0
on ˆC sm. So a and b are constant on ˆC. □

Lemma 2.6. Let ˆωuniv be as in Lemma 2.3. Then ˆωuniv descends to a semi-positive
(1, 1)-form ωuniv on Ag. Moreover, for N ∈ Z we have [N]
∗ωuniv = N 2ωuniv.

Proof. Let Sp2g be the symplectic group deﬁned over Q, and let V2g be the vector group
over Q of dimension 2g. Then the natural action of Sp2g on V2g deﬁnes a group P2g,a :=
V2g ⋊ Sp2g.
We use the classical action of Sp2g(R) on Hg, it is transitive. The real coordinate on
X2g,a on the left hand side of (2.2) has the following advantage. The group P2g,a(R) acts
transitively on X2g,a by the formula

(v, h) · (v′, Z) := (v + hv′, hZ)

for (v, h) ∈ P2g,a(R) and (v′, Z) ∈ R2g × Hg = X2g,a. The space A
an
g is then obtained as
the quotient of X2g,a by a congruence subgroup of P2g,a(Q). We refer to [Pin89, 10.5–10.9]
or [Pin05a, Construction 2.9 and Example 2.12] for these facts.
It is clear that both V2g(R) and Sp2g(R) preserve 2(da)
⊺ ∧ db. Thus this 2-form is
invariant under the action of P2g,a(R) on X2g,a.
So by Lemma 2.4, the previous two paragraphs imply that ˆωuniv descends to a (1, 1)-
form ωuniv on Ag. The semi-positivity of ωuniv follows from Lemma 2.3.
The property [N]
∗ωuniv = N 2ωuniv follows from the “moreover” part of Lemma 2.3
and the following commutative diagram

Cg × Hg ̃N //

  
 Cg × Hg

  
A
an
g [N ] // A
an
g . □

This semi-positive (1, 1)-form ωuniv will be the Betti form for Ag → Ag, as desired in
Proposition 2.2. To show this, it suﬃces to establish property (iii) of Proposition 2.2.
Hence it suﬃces to prove the following proposition.

Proposition 2.7. Assume A → S is Ag → Ag. Let X be an irreducible subvariety of
Ag of dimension d and let ∆ be an open subset of San with X sm,an ∩ A∆ ̸= ∅. Then

(2.3) ωuniv|∧d
X sm,an ̸≡ 0 if and only if max
x∈X sm,an∩A∆ rankR(db∆|X sm,an)x = 2d.

Proof. We begin by reformulating Corollary 2.5. If C is an irreducible, 1-dimensional,
complex analytic subset of an open subset of A∆, then

(2.4) ωuniv|Csm = 0 if and only if b∆(C) is a point;

indeed, this claim is local and it follows using the universal covering u : Cg × Hg → Ag.
We assume ﬁrst that the right side of (2.3) is false, i.e., the maximal rank is strictly less
than 2d = 2 dim X. So every x ∈ X sm,an ∩ A∆ is a non-isolated point of b
−1
∆ (r) ∩ X sm,an

where r = b∆(x). Because b
−1
∆ (r) is a complex analytic subset of A∆ (by Proposi-
tion 2.1.(ii) for Ag → Ag) and X sm,an is complex analytic in a neighborhood of x in Aan,
there exists an irreducible complex analytic curve C in b
−1
∆ (r) ∩ X sm,an passing through
x. In particular, b∆(C) is a point and so ωuniv|Csm ≡ 0 by (2.4).

UNIFORMITY IN MORDELL–LANG FOR CURVES 12

The upshot of the previous paragraph is that the Hermitian form attached to the semi-
positive (1, 1)-form ωuniv|X sm,an vanishes along the tangent space of C sm; it is degenerate.
We can complete a tangent vector of C sm to a basis of the tangent space of X sm,an.
Considering holomorphic local coordinates we ﬁnd ωuniv|∧d
X sm,an = 0 at every point of
C sm. By continuity it also vanishes at x ∈ C. Since x ∈ X sm,an ∩ A∆ was arbitrary, we
conclude ωuniv|∧d
X sm,an ≡ 0.
For the converse we assume ωuniv|∧d
X sm,an ≡ 0. So the Hermitian form attached to this
semi-positive (1, 1)-form is degenerate. Thus for each x ∈ X sm,an, using holomorphic
local coordinates we ﬁnd an irreducible, 1-dimensional, complex analytic subset Cx which
passes through x and is contained in X sm,an such that ωuniv|X sm,an vanishes along the
tangent space of C sm
x . So ωuniv|Csm
x ≡ 0, and hence b∆(Cx) is a point by (2.4). Letting
the point x run over X sm,an, we conclude that the rank on the right side of (2.3) is
strictly less than 2d. □

2.3. General case. We now prove Propositions 2.1 and 2.2 for π : A → S as near the
beginning of this section. In particular, we assume (Hyp). With the construction in
§2.1, the rest of the proof of Proposition 2.1 follows the construction in [Gao20a, §4].
As Ag is a ﬁne moduli space there exists a Cartesian diagram

A ι //

π   
 ❴✤ Ag

  
S ιS // Ag.

Now let s0 ∈ S(C). Applying Proposition 2.1 to the universal abelian variety Ag → Ag
and ιS(s0) ∈ Ag(C), we obtain an open neighborhood ∆0 of ιS(s0) in Aan
g and a map

b∆0 : Ag|∆0 → T
2g

satisfying the properties listed in Proposition 2.1.
Now let ∆ = ι
−1
S (∆0). Then ∆ is an open neighborhood of s in San. Denote by
A∆ = π−1(∆) and deﬁne b∆ = b∆0 ◦ ι : A∆ → T
2g.

Then b∆ satisﬁes the properties listed in Proposition 2.1 for A → S. Hence b∆ is our
desired Betti map.
Next let us turn to the Betti form. Let ωuniv be the semi-positive (1, 1)-form on Ag as
in Lemma 2.6. Deﬁne ω := ι
∗ωuniv. We will show that ω satisﬁes the properties listed
in Proposition 2.2.
The (1, 1)-form ω is semi-positive as it is the pull-back of the semi-positive form
ωuniv. Moreover, it satisﬁes [N]
∗ω = N 2ω since ωuniv has this property. Hence we have
established properties (i) and (ii) of Proposition 2.2.
Let us verify (iii) of Proposition 2.2. Suppose X is an irreducible subvariety of A of
dimension d. Let ∆ be an open subset of San with X sm,an ∩ A∆ ̸= ∅; we may shrink ∆
subject to this condition. Let Z = ι(X) and observe dim Z ≤ d.
Since ω = ι
∗ωuniv, we have

(2.5) ω|∧d
X sm,an ̸≡ 0 if and only if ωuniv|∧d
Z sm,an ̸≡ 0.

UNIFORMITY IN MORDELL–LANG FOR CURVES 13

Next by deﬁnition of b∆, we have the following property: For suitable non-empty open
subsets ∆ of San and ∆0 of Aan
g such that ιS(∆) ⊆ ∆0, we have
(2.6) max
x∈X sm,an∩A∆ rankR(db∆|X sm,an)x ≤ max
x∈Z sm,an∩Ag,∆0 rankR(db∆0|Z sm,an)x ≤ 2 dim Z ≤ 2d.

Suppose ﬁrst that ω|∧d
X sm,an ̸≡ 0, then (2.5) implies ωuniv|∧d
Z sm,an ̸≡ 0 and in particular d =
dim Z. We can apply Proposition 2.2(iii) to Z and obtain maxx∈Z sm,an∩Ag,∆0 rankR(db∆0|Z sm,an)x =
2d. Now ι|X : X → Z is generically ﬁnite as dim X = dim Z, so the ﬁrst inequality in
(2.6) is an equality. We conclude

(2.7) max
x∈X sm,an∩A∆ rankR(db∆|X sm,an)x = 2d.

Conversely, assume (2.7) holds true. Then we have equalities throughout in (2.6). By
Proposition 2.2(iii) applied to Z and by (2.5) we get ω|∧d
X sm,an ̸≡ 0.

3. Setup and notation for the height inequality

In the next few sections we will prove Theorem 1.6. Let us ﬁrst ﬁx the setting.
All varieties are over an algebraically closed subﬁeld k of C. The ambient data is
given as above Theorem 1.6. We repeat it here.
• Let S be a regular, irreducible, quasi-projective variety over k that is Zariski
open in an irreducible projective variety S ⊆ Pm
k .
• Let π : A → S be an abelian scheme presented by a closed immersion A → Pn
k ×S
over S.
• From the previous point, we get a closed immersion of the generic ﬁber A of
A → S into Pn
k(S). We assume that A → Pn
k(S) arises from a basis of the global
sections of the l-th power L of a symmetric ample line bundle with l ≥ 4.
• Finally, we assume (Hyp) as on page 5.
From the third bullet power, we see that the image of A is projectively normal in
Pn
k(S), cf. [Mum70, Theorem 9]. By the fourth bullet point, Proposition 2.2 provides the
Betti form ω on Aan.
For s ∈ S(k) we write As for the abelian variety π−1(s).

Remark 3.1. Let S be as in the ﬁrst bullet point. Let π : A → S be an abelian scheme.
Suppose L0 is a symmetric and ample line bundle on A, the generic ﬁber of π. An
immersion of A as in the second bullet point can be obtained as follows. By [Ray70,
Th´eor`eme XI 1.13] there exists an S-ample line bundle L on A whose restriction to the
generic ﬁber of A → S is isomorphic to L
⊗l
0 for some integer l ≥ 4. We may assume
in addition that L satisﬁes [−1]∗L ∼= L and even that L becomes trivial when pulled
back under the zero section S → A, see [Ray70, Remarque XI 1.3a]. After replacing
L by a suﬃciently high power, we may assume that L is very ample over S. We ﬁx a
basis of global sections of L
⊗l
0 and, as l ≥ 4, thereby realize the generic ﬁber of π as
a projectively normal subvariety of Pn
k(S). Now we can take L in the third bullet point
to be L
⊗l
0 , which is the restriction of L to A. A closed immersion A → Pn
k × S as in
the second bullet point arises from L ⊗ π∗M for some very ample line bundle M on S;
see [Gro61, Proposition 4.4.10.(ii) and Proposition 4.1.4]. On restricting to a ﬁber of
A → S the induced closed immersion As → Pn
k comes from the restriction L|As.

UNIFORMITY IN MORDELL–LANG FOR CURVES 14

Write A for the Zariski closure of A in Pn
k ×S. Then A is irreducible but not necessarily
regular. On any product of r projective spaces and if a1, . . . , ar ∈ Z, we let O(a1, . . . , ar)
denote the tensor product over all i ∈ {1, . . . , r} of the pull-back under the i-th projection
of O(ai). We write L for the restriction of O(1, 1) to A.

3.1. Height functions on A. If k = Q we have several height functions on A(Q).
For any n ∈ N, we always consider the absolute logarithmic Weil height function
Pn
Q(Q) → R, or just Weil height, deﬁned as in [BG06, §1.5.1].
Now say P ∈ A(Q), we write P = (P ′, π(P )) with P ′ ∈ Pn
Q(Q) and π(P ) ∈ Pm
Q (Q).
The sum of Weil heights

(3.1) h(P ) = h(P ′) + h(π(P ))

deﬁnes our ﬁrst height A(Q) → [0, ∞) which we call the naive height on A. It depends
on the ﬁxed immersion of A.
The line bundle [−1]∗L|A ⊗ L|⊗−1
A of A restricted to the generic ﬁber A of A → S
equals [−1]∗L ⊗ L
⊗−1. By the third bullet point above this line bundle is trivial. So it
equals π∗K for some line bundle K of S by [Gro67, Corollaire 21.4.13 (pp. 361 of EGA
IV-4, in Errata et Addenda, liste 3)]. We conclude [−1]∗L|As ∼= L|As for all s ∈ S(Q).
So the function (3.1) represents the height function, deﬁned up-to Os(1), given by the
Height Machine, cf. [BG06, Theorem 2.3.8], applied to (As, Ls). As Ls is symmetric, the
ﬁberwise N´eron–Tate or canonical height ˆhA : A(Q) → [0, ∞), deﬁned by the convergent
limit

(3.2) ˆhA(P ) = lim
N →∞ h([N](P ))
N 2 ,

is a quadratic form on As(Q). In the notation [BG06, Chapter 9] the height (3.2) is
ˆhAs,Ls where s = π(P ).

Remark 3.2. We use here the notation of Remark 3.1. So that the immersion A → Pn
S
arises via L
⊗l
0 . To normalize, we divide (3.2) by l and obtain the N´eron–Tate height
ˆhA,L0 : A(Q) → [0, ∞).
Let us verify that ˆhA,L0 depends only on L0. Suppose L′ is another line bundle on
A that restricts to L
⊗l
0 , then L′ ⊗ L⊗−1 is trivial on A. By [Gro67, Corollaire 21.4.13
(pp. 361 of EGA IV-4, in Errata et Addenda, liste 3)], this diﬀerence is the pull-back
of some line bundle on S under A → S. So the restriction of L′ ⊗ L⊗−1 to As for each
s ∈ S(C) is trivial. Thus L|As and L′|As induce the same N´eron–Tate height on As(Q),
see [BG06, §9.2].

3.2. Integration against the Betti form. Let A and S be as in the beginning of this
section, so they are deﬁned over an algebrically closed subﬁeld k of C. Recall that ω is
the Betti form on Aan as provided by Proposition 2.2. In particular, it is a semi-positive
(1, 1)-form on Aan such that [N]
∗ω = N 2ω for all N ∈ Z. We discuss here a modiﬁcation
of the Betti form that has compact support.
Fix X to be an irreducible closed subvariety of A of dimension d, such that π|X : X →
S is dominant.
We are not allowed to integrate ω∧d over X sm,an as ω∧d may not have compact support.
So we modify ω in the following way.

UNIFORMITY IN MORDELL–LANG FOR CURVES 15

Suppose we are provided with a base point s0 ∈ San. Let furthermore ∆ be a relatively
compact, contractible, open neighborhood of s0 in San. Denote by A∆ the open subset
π−1(∆) of Aan. Fix a smooth bump function ϑ : San → [0, 1] with compact support
K ⊆ ∆ such that ϑ(s0) = 1. Finally, we deﬁne θ = ϑ ◦ π : Aan → [0, 1]. Then θω is
a semi-positive smooth (1, 1)-form on Aan; unlike the Betti form, it may not be closed.
By construction, the support of θω lies in π−1(K) which is compact as π is proper and
K is compact.

Remark 3.3. Suppose X is non-degenerate, namely X satisﬁes one of the two equivalent
conditions in property (iii) of Proposition 2.2. Then X an contains a smooth point P0 at
which ω|∧d
X sm,an > 0. Then we will take s0 = π(P0).

3.3. The graph construction. Let N ∈ Z. The multiplication-by-N morphism [N] : A →
A may not extend to a morphism A → A. We overcome this by using the graph con-
struction.
Recall that we have identiﬁed A ⊆ A ⊆ Pn
k × S ⊆ Pn
k × Pm
k .
We write ρ1, ρ2 : Pn
k × Pn
k × Pm
k → Pn
k × Pm
k for the two projections ρ1(P, Q, s) = (P, s)
and ρ2(P, Q, s) = (Q, s).
Consider ΓN the graph of [N], determined by

ΓN = {(P, [N](P )) : P ∈ A(k)}.

We consider it as an irreducible closed subvariety of A ×S A.
Let X be an irreducible closed subvariety of A of dimension d. The graph XN of [N]
restricted to X is an irreducible closed subvariety of ΓN determined by

{(P, [N]P ) : P ∈ X(k)}.

Observe that ρ1|ΓN : ΓN → A is an isomorphism; it maps (P, [N](P )) to P . So we can
use ρ1|−1
ΓN to identify X with XN .
Moreover, ρ2|ΓN maps (P, [N](P )) to [N](P ). Therefore

(3.3) ρ2|ΓN ◦ ρ1|−1
ΓN = [N].

Let XN be the Zariski closure of XN in A×SA ⊆ Pn
S×SPn
S = Pn
k ×Pn
k ×S ⊆ Pn
k ×Pn
k ×Pm
k .
Then XN is an irreducible projective variety (which is not necessarily regular) with
dim XN = dim XN = dim X.
In the next section, we will use the following line bundles on XN . Deﬁne

(3.4) F = ρ
∗
2O(1, 1)|XN = O(0, 1, 1)|XN
and

(3.5) M = O(0, 0, 1)|XN .

Let us close this subsection by relating the height functions deﬁned by F and M with
the ones in §3.1. Assume k = Q. Let P ∈ X(Q). Write P = (P ′, π(P )) with P ′ ∈ Pn
Q(Q)
and π(P ) ∈ Pm
Q (Q). We have [N](P ) = (P ′
N , π(P )) for some P ′
N ∈ Pn
Q(Q).
Under the immersion XN ⊆ Pn
Q×Pn
Q×Pm
Q , the point (P, [N]P ) in XN (Q) becomes PN =
(P ′, P ′
N , π(P )) ∈ (Pn
Q × Pn
Q × Pm
Q )(Q). The function PN ↦→ h([N](P )) = h(P ′
N ) + h(π(P ))
deﬁned in (3.1) represents the height attached by the Height Machine to (XN , F ) and
PN ↦→ h(π(P )) represents the height attached to (XN , M).

UNIFORMITY IN MORDELL–LANG FOR CURVES 16

4. Intersection theory and height inequality on the total space

We keep the notation of §3. So we have a closed immersion A → Pn
k × S over S
satisfying the properties stated near the beginning of §3. Moreover, S is a Zariski open
subset of an irreducible projective variety S ⊆ Pm
k . We assume in addition k = Q.
Let X be a closed irreducible subvariety of A of dimension d deﬁned over Q, such that
π|X : X → S is dominant. Let ω be the Betti form on A as deﬁned in Proposition 2.2.

Proposition 4.1. We keep the notation from above and suppose that X an contains a
smooth point at which ω|∧d
X sm,an > 0. Then there exists a constant c1 > 0 satisfying the
following property. Let N ∈ N be a power of 2, there exist a Zariski open dense subset
UN of X deﬁned over Q and a constant c2(N) such that

h([N]P ) ≥ c1N 2h(π(P )) − c2(N) for all P ∈ UN (Q).

The goal of this section is to prove Proposition 4.1. The key idea is to apply a theorem
of Siu [Laz04, Theorem 2.2.15]. Let us brieﬂy explain the main points before moving on
to the proof.
Let X be as in Proposition 4.1, and let P ∈ X(Q). For each N ∈ N, we work with
XN ⊆ A ×S A, the graph of [N] : A → A, and its Zariski closure XN in A ×S A ⊆
Pn
k × Pn
k × Pm
k . The point P gives rise to a point PN ∈ XN ; see §3.3. Consider the line
bundles F = O(0, 1, 1)|XN and M = O(0, 0, 1)|XN . Choosing representatives as in last
paragraph of §3.3 our height inequality in Proposition 4.1 is equivalent to

hXN ,F (PN ) ≥ c1N 2hXN ,M(PN ) − c′
2(N)

for some c′
2(N) independent of P (which may be diﬀerent from c2(N)). By the Height
Machine it suﬃces to ﬁnd positive integers p and q, independent of N, such that F ⊗q ⊗
M⊗−pN 2 is a big line bundle on XN ; we can then take c1 = p/q.
Both F and M are nef line bundles. Thus a criterion of bigness by Siu [Laz04,
Theorem 2.2.15], states that F ⊗q ⊗ M⊗−pN 2 is big if (F ·d) > dc1(M⊗N 2 · F ·(d−1)). Note
that (M⊗N 2 · F ·(d−1)) = N 2(M · F ·(d−1)) by multi-linearity of intersection numbers.
Thus our task becomes comparing two intersection numbers. Our application continues
to work if the numerical factor d = dim X is replaced by any positive factor that depends
only on the dimension. So it remains to prove an appropriate lower bound for (F ·d) and
an appropriate upper bound for (M · F ·(d−1)).
The proof of Proposition 4.1 will be organized as follows in this section. We ﬁrst
prove the appropriate lower bound for (F ·d) in Proposition 4.2. This is where we use the
hypothesis that ω|∧d
X sm,an > 0 at some smooth point of X an. Next we prove the appropriate
lower bound for (M · F ·(d−1)) in Proposition 4.3. At this step the assumption of N being
a power of 2 is used. Then we ﬁnish the proof of Proposition 4.1 by applying Siu’s
theorem in §4.3.

4.1. Bounding an intersection number from below. Let X be as in Proposi-
tion 4.1. For each N ∈ N, let XN ⊆ Pn
k × Pn
k × Pm
k be as in §3.3. In particular,
dim XN = d. Let F = O(0, 1, 1)|XN be as in (3.4). The top self-intersection of F on XN
is bounded from below in the following proposition. To prove it, we may replace X by
its base change to C.
 UNIFORMITY IN MORDELL–LANG FOR CURVES 17

Proposition 4.2. Suppose X an contains a smooth point at which ω|∧d
X sm,an > 0. Then
there exists a constant κ > 0, independent of N, such that (F ·d) ≥ κN 2d for all N ∈ N.

Proof. We ﬁx a point P0 ∈ X sm,an at which ω|∧d
X sm,an is positive and let s0 = π(P0), ∆, ϑ, θ,
and K be as in §3.2, see Remark 3.3. In particular ϑ(P0) = θ ◦ π(P0) = 1. We extend
ϑ to a smooth function on (Pm
C )an by setting it 0 outside of the compact set K ⊆ San.
This extends θ = ϑ ◦ π to all of (Pn
C × Pm
C )an.
Let α be the pull-back of the Fubini–Study form under the analytiﬁcation of the Segre
morphism Pn
C × Pm
C → P(n+1)(m+1)−1
C . We replace α by its restriction to Aan. Thus α
represents the Chern class of O(1, 1) ∈ Pic(Pn
C × Pm
C ) restricted to A
an, using common
notation.
Note that α is strictly positive on all of Aan. Since ∆ is relatively compact we can
ﬁnd a constant C > 0 with

(4.1) Cα|A∆ − ω|A∆ ≥ 0.

As the smooth and non-negative function θ = ϑ ◦ π on Aan has support in π−1(K) ⊆
π−1(∆) = A∆ we have Cθα − θω ≥ 0.
We pull this (1, 1)-form back under the holomorphic map [N] : Aan → Aan and get

(4.2) C[N]∗(θα) − N 2θω = C[N]
∗(θα) − [N]
∗(θω) ≥ 0

where we used [N]∗ω = N 2ω and [N]∗θ = θ; the former is a property of the Betti form,
see Proposition 2.2(ii) and the latter holds as θ is the pull-back from the base of ϑ.
We deﬁne β = C[N]∗(θα) − N 2θω,
which is a (1, 1)-form on Aan. It is semi-positive by (4.2). The support of θ is contained
in π−1(K), which we have identiﬁed as compact at the end of §3.2. So C[N]
∗(θα) and
N 2θω have compact support on Aan.
We claim that ∫

X sm,an(C[N]
∗(θα))∧d ≥ ∫

X sm,an(N 2θω)∧d.
First observe that both integrals are well-deﬁned as both [N]∗(θα) and N 2θω have
compact support on Aan; this follows from work of Lelong [Lel57] which we use freely
below. A textbook proof can be found in [Voi02, Theorem 11.21] and [Dem12, §III.2.B].
To prove the inequality let us write β = γ − δ with γ = C[N]
∗(θα) and δ = N 2θω. Then
(4.3)
∫

X sm,an γ∧d − ∫

X sm,an δ∧d = ∫
X sm,an(δ + β)∧d − ∫

X sm,an δ∧d =
 d−1∑

i=0
 (
d
i
) ∫

X sm,an δ∧i ∧ β∧(d−i)

as the exterior product is commutative on even degree forms. We know that β ≥ 0 on
Aan and it is also crucial that δ ≥ 0 on Aan, the latter follows from ω ≥ 0, property
(i) of Proposition 2.2, and from θ ≥ 0. Then δ∧i ∧ β∧(d−i) is semi-positive on Aan;
see [Dem12, Proposition III.1.11]1. Thus the right-hand side of (4.3) is non-negative,
see [Dem12, Theorem III.2.7], and our claim is settled.

1As our convention is somewhat diﬀerent from Demailly’s, let us explain how to apply [Dem12,
Proposition III.1.11]. Our deﬁnition of semi-positive (1, 1)-form coincides with that of positive (1, 1)-
form of [Dem12, Chapter III] by Corollary 1.7 of loc.cit., and thus are precisely the strongly positive
(1, 1)-forms of [Dem12, Chapter III] by Corollary 1.9 of loc.cit. Therefore we can apply the cited
proposition.
 UNIFORMITY IN MORDELL–LANG FOR CURVES 18

The claim implies

(4.4) C d ∫

X sm,an[N]∗(θα)∧d ≥ κ
′N 2d where κ
′ = ∫

X sm,an(θω)∧d.

We have κ
′ > 0. Indeed, (θω)∧d is semi-positive on Aan because ω ≥ 0 (Proposi-
tion 2.2(i)) and θ ≥ 0 (by construction). But ω|∧d
X sm,an is positive at P0 ∈ X sm,an by
choice of P0 and θ ◦ π(P0) = 1 by choice of θ. So (θω)|∧d
X sm,an is positive at P0 ∈ X sm,an.
Thus κ
′ > 0.
Next we want to relate the integral on the left in (4.4) with an intersection number.
First we recall that [N] is given in terms of the graph construction, cf. (3.3). So we may
rewrite

(4.5) ∫

X sm,an[N]∗(θα)∧d = ∫
X sm,an(ρ2|ΓN ◦ ρ1|−1
ΓN )∗(θα)∧d = ∫

X sm,an(ρ1|−1
ΓN )∗ρ2|∗
ΓN (θα)∧d,

here ΓN , ρ1, and ρ2 are as deﬁned in §3.3.
Because ρ1|Γan
N : Γan
N → Aan is biholomorphic we can change coordinates and integrate
over XN , which is a complex analytic subset of the graph ΓN , itself a complex manifold.
More precisely, we have

(4.6) ∫
X sm,an(ρ1|−1
ΓN )∗ρ2|∗
ΓN (θα)∧d = ∫

X sm,an
N ρ2|∗
ΓN (θα)∧d.

Recall that α is the restriction to Aan of a (1, 1)-form on (Pn
C × Pm
C )an. Moreover, ρ2
is also deﬁned on all of Pn
C × Pn
C × Pm
C . So ρ2|∗
ΓN (θα) is the restriction to ΓN of a (1, 1)-
form deﬁned on (Pn
C × Pn
C × Pm
C )an. Observe that X sm,an
N ⊆ XN an and the diﬀerence has
dimension strictly less than d = dim XN . This justiﬁes

(4.7) ∫

X sm,an
N ρ2|∗
ΓN (θα)∧d = ∫
XN an ρ
∗
2(θα)∧d

where we take XN an as a complex analytic subset of the analytiﬁcation of Pn
C × Pn
C × Pm
C
and ρ
∗
2(θα) as a (1, 1)-form on this ambient space. Now θ takes values in [0, 1] and so

(4.8) ∫

XN an ρ
∗
2(θα)∧d ≤ ∫

XN an(ρ
∗
2α)∧d.

The pull-back ρ
∗
2α represents ρ
∗
2O(1, 1) ∈ Pic(Pn
C × Pn
C × Pm
C ) in the Picard group and
has compact support as (Pn
C × Pn
C × Pm
C )an is compact. But integration coincides with
the intersection pairing in the compact case; see [Voi02, Theorem 11.21]. In particular,
we have

(4.9) ∫

XN an(ρ
∗
2α)∧d = (ρ
∗
2O(1, 1)·d[XN ])

where the intersection takes place in Pn
C × Pn
C × Pm
C . We recall (3.4) and apply the
projection formula to obtain

(4.10) (ρ
∗
2O(1, 1)·d[XN ]) = (O(0, 1, 1)·d[XN ]) = (F ·d).

The (in)equalities (4.5), (4.6), (4.7), (4.8), (4.9), and (4.10) yield
∫
X sm,an[N]
∗(θα)∧d ≤ (F ·d).

UNIFORMITY IN MORDELL–LANG FOR CURVES 19

We recall the lower bound (4.4) to obtain (F ·d) ≥ (κ
′/C d)N 2d where C comes from (4.1)
and κ
′ > 0 comes from (4.4). The proposition follows with κ = κ
′/C d. □

4.2. Bounding an intersection number from above. We keep the notation from
the last subsection with k = Q. So X is as above Proposition 4.1 with dim X = d
For each N ∈ N, let XN ⊆ Pn
k × Pn
k × Pm
k be the graph construction as in §3.3. In
particular, dim XN = d. Here we need F = O(0, 1, 1)|XN as deﬁned in (3.4) and also
M = O(0, 0, 1)|XN as deﬁned in (3.5).

Proposition 4.3. Assume d ≥ 1. There exists a constant c > 0 depending on the data
introduced above with the following property. Say N ≥ 1 is a power of 2, then

(M · F ·(d−1)) ≤ cN 2(d−1).

Let us make some preliminary remarks before the proof. A similar upper bound for
the intersection number was derived by the third-named author in [Hab09, Hab13] using
Philippon’s version [Phi86] of B´ezout’s Theorem for multiprojective space. The approach
here is similar but does not refer to Philippon’s result. Rather, we rely on the following
well-known positivity property of the intersection theory of multiprojective space: any
eﬀective Weil divisor on a multiprojective space is nef. This approach was motivated by
K¨uhne’s [K¨uh20] work on semiabelian varieties.

Proof of Proposition 4.3. Recall that [2] : A → A is the multiplication-by-2 morphism on
A. For the symmetric and ample line bundle L on A, we have [2]∗L ∼= L
⊗4. Recall that A
is projectively normal in Pn
k(S). By a result of Serre, [Wal87, Corollaire 2, Appendix II],
the morphism [2] is represented by homogeneous polynomials f0, . . . , fn in the n + 1
projective coordinates of Pn of degree 4, with coeﬃcients in k(S) and with no common
zeros in A.
Recall that the family A is embedded in Pn
k × S ⊆ Pn
k × Pm
k . We can spread out
the f0, . . . , fn. More precisely, there exist a Zariski closed, proper subset Z ⊊ A and
polynomials f0, . . . , fn ∈ k[X, S] that are bihomogeneous of degree (4, D′) in the (n + 1)-
tuple of projective coordinates X of Pn
k and the (m + 1)-tuple of projective coordinates
S of Pm
k , with the following properties:
(i) the polynomials f0, . . . , fn have no common zeros on (A \ Z)(k), and
(ii) if (P, s) ∈ (A \ Z)(k), then [2](P, s) = ([f0(P, s) : · · · : fn(P, s)], s)
.
Moreover, as f0, . . . , fn have no common zero on the generic ﬁber, we may assume that
π(Z) is Zariski closed and proper in S. So we may assume that Z = π−1(π(Z)) ⊊ A
and in particular, [2] maps A \ Z to itself.
The 4 in the bidegree (4, D′) comes from 22 = 4. The degree D′ with respect to the
base coordinates S is more mysterious. However, by successively iterating we will get it
under control.
For each integer l ≥ 1 we require polynomials f (l)
0 , . . . , f (l)
n to describe multiplication-
by-2l, cf. [GH19, §9]. In order to obtain information on the degree with respect to S we
construct them by iterating the f (1)
0 = f0, . . . , f (1)
n = fn. For all i ∈ {0, . . . , n} we set

f (l+1)
i (X, S) = fi ((
f (l)
0 (X, S), . . . , f (l)
n (X, S)), S
)

for all i; it is bihomogeneous in X and S. So for all l ≥ 1

UNIFORMITY IN MORDELL–LANG FOR CURVES 20

(i) the polynomials f (l)
0 , . . . , f (l)
n have no common zeros on (A \ Z)(k), and
(ii) if (P, s) ∈ (A \ Z)(k), then [2l](P, s) = ([f (l)
0 (P, s) : · · · : f (l)
n (P, s)], s)
.

If for all i the polynomials f (l)
i are bihomogeneous of degree (Dl, D′
l), then all f (l+1)
i
are bihomogeneous of degree (4Dl, D′ + 4D′
l). Recall that (D1, D′
1) = (4, D′), thus the
recurrence relations Dl+1 = 4Dl and D′
l+1 = D′ + 4D′
l
imply

(4.11) Dl = 4l and D′
l = 4l − 1
3 D′ ≤ 4lD′

for all l ≥ 1. Up-to the constant linear factor D′ the bidegrees both grow like 4l.
We proceed as follows to cut out the graph XN where N = 2l. We start out with
X ⊆ Pn
k × Pm
k . As X dominates S but Z does not, there is an i such that f (l)
i does not
vanish identically on X, without loss of generality we assume i = 0.
Then as i varies over {1, . . . , n} we obtain n trihomogeneous polynomials

gi := Yif (l)
0 (X, S) − Y0f (l)
i (X, S)

where Y0, . . . , Yn are the projective coordinates on the middle factor of Pn
k × Pn
k × Pm
k .
The tridegree of these polynomials is (Dl, 1, D′
l). Their zero locus on X × Pn
k has the
graph XN as an irreducible component; by permuting coordinates we consider X × Pn
k
as a subvariety of Pn
k × Pn
k × Pm
k . We will see below that this is a proper component
of the said intersection. However, there may be further irreducible components in this
intersection, some could even have dimension greater than dim XN .
This issue is clariﬁed by the positivity result [Ful98, Corollary 12.2.(a)]. We apply it
to the ambient variety Pn
k ×Pn
k ×Pm
k , which becomes X in Fulton’s notation; observe that
the tangent bundle of a product of projective spaces is generated by its global sections,
cf. [Ful98, Examples 12.2.1.(a) and (c)]. For i ∈ {1, . . . , n}, the Vi in Fulton’s notation is
the zero set of gi, and Vn+1 is X ×Pn
k . So r = n+ 1 and V1, . . . , Vn+1 are equidimensional.
Observe that

r∑

i=1 dim Vi − (r − 1) dim Pn
k × Pn
k × Pm
k = (2n + m − 1)(r − 1) + dim X × Pn
k − (r − 1)(2n + m)

= dim X = dim XN ,

so, and as announced above, XN is a proper component in the intersection of V1, . . . , Vn,
and X × Pn
k . By Fulton’s [Ful98, Corollary 12.2.(a)] the cycle class attached to the
intersection of X × Pn
k with the zero locus of g1, . . . , gn is represented by a positive cycle
on Pn
k × Pn
k × Pm
k , one of whose components is XN . As O(0, 0, 1) and O(0, 1, 1) are
numerically eﬀective we conclude

(O(0, 0, 1)O(0, 1, 1)·(d−1)[XN ]) ≤ (
O(0, 0, 1)O(0, 1, 1)·(d−1)O(Dl, 1, D′
l)·n[X × Pn
k ]
) .
(4.12)

The cycle [X × Pn
k ] is linearly equivalent to ∑
i+p=n+m−d aipH ·i
1 H ·p
2 , with H1 and H2
hyperplane pullbacks of the factors Pn
k ×Pm
k ⊇ X, respectively, and with aip non-negative

UNIFORMITY IN MORDELL–LANG FOR CURVES 21

integers that depend only on X. Thus the left-hand side of (4.12) is at most
∑

i+p=n+m−d aip (O(0, 0, 1)O(0, 1, 1)·(d−1)O(Dl, 1, D′
l)·nO(1, 0, 0)·iO(0, 0, 1)·p) .

We can expand the sum using linearly of intersection numbers to ﬁnd that it equals
∑

i+p=n+m−d
j′+p′=d−1
i′′+j′′+p′′=n
 aip
(
d − 1
j′, p′
 )( n
i′′, j′′, p′′
)
Dli′′D′
lp′′ (
O(1, 0, 0)·(i+i′′)O(0, 1, 0)·(j′+j′′)O(0, 0, 1)·(1+p+p′+p′′))

Only terms with i + i
′′ ≤ n and j′ + j′′ ≤ n and 1 + p + p′ + p′′ ≤ m contribute to the sum.
On the other hand, any term in the sum satisﬁes i + i
′′ + j′ + j′′ + 1 + p + p′ + p′′ = 2n + m.
So we can assume i + i
′′ = n and j′ + j′′ = n and 1 + p + p′ + p′′ = m in the sum which
thus simpliﬁes to ∑

i+p=n+m−d,i+i′′=n
j′+p′=d−1,j′+j′′=n
i′′+j′′+p′′=n,p+p′+p′′=m−1
 aip
(
d − 1
j′, p′
 )( n
i′′, j′′, p′′
)Dli′′D′
lp′′.

Note i
′′ + p′′ = n − j′′ = j′ = d − 1 − p′ ≤ d − 1. We recall (4.11) and conclude that the
left-hand side of (4.12) is at most

(4.13) (4lD′)d−1 ∑

i+p=n+m−d
j′+p′=d−1
i′′+j′′+p′′=n
 aip
(
d − 1
j′, p′
 )( n
i′′, j′′, p′′
) ≤ (4lD′)d−12d−13n ∑

i+p=n+m−d aip.

We recall N = 2l and use the projection formula with the estimates above to ﬁnd

(O(0, 0, 1)|XN O(0, 1, 1)|·(d−1)
XN ) ≤ cN 2(d−1)

where c > 0 depends only on X. Recall our deﬁnition F = O(0, 1, 1)|XN and M =
O(0, 0, 1)|XN . So we get (M · F ·(d−1)) ≤ cN 2(d−1), as desired. □

4.3. Proof of Proposition 4.1. Now let us prove Proposition 4.1 by comparing the
intersection number inequalities in Propositions 4.2 and 4.3.
Let X be of dimension d as in Proposition 4.1. The case d = 0 is trivial. So we assume
d ≥ 1. We may assume N = 2l with l ∈ N. Let XN ⊆ Pn
k × Pn
k × Pm
k be as in §3.3. In
particular dim XN = d.
Let κ > 0 be as in Proposition 4.2. Then (F ·d) ≥ κN 2d. Let c > 0 be as in
Proposition 4.3. Then (M · F ·(d−1)) ≤ cN 2(d−1). We have indicated how to obtain κ and
c at the end of the proof of each one of the corresponding propositions.
Fix a rational number c1 such that

(4.14) 0 < c1cd < κ.

Let q be a multiple of the denominator of c1. Using the bounds above and linearity of
intersection numbers we get

d(M⊗qc1N 2·(F ⊗q)·(d−1)) = dqdc1N 2(M·F ·(d−1)) ≤ dqdc1N 2cN 2(d−1) < κqdN 2d ≤ ((F ⊗q)·d).

UNIFORMITY IN MORDELL–LANG FOR CURVES 22

Then F ⊗q ⊗ M⊗−qc1N 2 is a big line bundle on XN by a theorem of Siu [Laz04, Theorem
2.2.15]. After possibly replacing q by a multiple the line bundle F ⊗q ⊗ M⊗−qc1N 2 admits
a non-zero global section. Say hXN ,F and hXN ,M are representives of heights on XN
attached by the Height Machine to F and M, respectively. After canceling q we conclude
that hXN ,F − c1N 2hXN ,M is bounded from below on a Zariski open and dense subset of
XN . The image of this subset under the projection ρ1 contains a Zariski open and dense
subset UN of X. It follows from the end of §3.3 that there exists c2(N) such that

h([N](P )) ≥ c1N 2h(π(P )) − c2(N) for all P ∈ UN (Q). □

5. Proof of the height inequality Theorem 1.6

We keep the notation of §3. In particular, S is a regular, irreducible, quasi-projective
variety over Q and π : A → S is an abelian scheme of relative dimension g ≥ 1. Moreover,
we have immersions as in §3 and we assume (Hyp) from page 5. We use the heights
introduced in §3.1. Let X be an irreducible closed subvariety of A deﬁned over Q. We
assume that X dominates S and is non-degenerate as deﬁned in Deﬁnition 1.5
The upshot of (Hyp) is that we obtain from Proposition 2.2 the Betti form ω on Aan.
Moreover, part (i) and (iii) of Proposition 2.2 implies that, for d = dim X,

(5.1) ω|∧d
X sm,an > 0 at some smooth point of X an.

Our assumption (5.1) allows us to apply Proposition 4.1 to X. There exists a constant
c1 > 0 as in (4.14) such that the following holds. Let N ∈ N be a power of 2, there
exists a Zariski open dense subset UN ⊆ X and a constant c2(N) ≥ 0 such that

(5.2) h([N]P ) ≥ c1N 2h(π(P )) − c2(N)

for all P ∈ UN (Q); we stress that UN and c2 ≥ 0 may depend on N in addition to X, A,
and the various immersions such as A ⊆ Pn
Q × Pm
Q .
By the Theorem of Silverman-Tate, see [Sil83, Theorem A] and Theorem A.1, there
exist a constant c0 ≥ 0 such that

(5.3) |ˆhA(P ) − h(P )| ≤ c0 max{1, h(π(P ))} ≤ c0(1 + h(π(P )))

for all P ∈ A(Q).
Next we kill Zimmer constants as in Masser’s [Zan12, Appendix C]. For any P ∈
UN (Q), we have

ˆhA([N](P )) ≥ h([N](P )) − c0(1 + h(π([N](P )))) (by (5.3))

= h([N](P )) − c0(1 + h(π(P ))) (as π([N](P )) = π(P ))

≥ c1N 2h(π(P )) − c2(N) − c0(1 + h(π(P ))) (by (5.2)).

We use ˆhA([N]P ) = N 2ˆhA(P ), divide by N 2, and rearrange to get

ˆhA(P ) ≥ (
c1 − c0
N 2
 ) h(π(P )) − c2(N) + c0
N 2

for all N ∈ N that are powers of 2 and all P ∈ UN (Q).

UNIFORMITY IN MORDELL–LANG FOR CURVES 23

Recall that c0 and c1 are independent of N. We ﬁx N ∈ N to be the least power of 2
such that N 2 ≥ 2c0/c1. As h(π(P )) is non-negative we get

ˆhA(P ) ≥ c1
2 h(π(P )) − c2(N) + c0
N 2

for all P ∈ UN (Q). Since N is now ﬁxed, the Zariski open dense subset UN of X is also
ﬁxed. The theorem follows after adjusting c1 and c2. □

Remark 5.1. In the proof of Theorem 1.6 we can keep track of the process to compute the
constant c1 > 0. Use the notation in §3. In particular ω is the Betti form on A, we have
an immersion A ⊆ Pn
C × Pm
C , α is a (1, 1)-form on Pn
C × Pm
C representing the Chern class
of O(1, 1), ∆ ⊆ San is open and relative compact, and θ : Aan → [0, 1] (which factors
through San) is a smooth function with compact support contained in A∆ := π−1(∆).
The function θ should furthermore satisfy θ(P0) = 1 for some P0 ∈ X sm(C) such that
(ω|X sm)∧d is positive at P0, where d = dim X.
Assume d ≥ 1. The proof of Theorem 1.6 tells us that one half of any rational number
satisfying the inequality (4.14) can be taken as c1. So the constant c1 > 0 can be taken
to be any rational number in (0, κ/(2cd)), such that:

• κ = κ
′/C d, where κ
′ = ∫

X sm,an(θω)∧d, as in (4.4), and C satisﬁes Cα|A∆ −ω|A∆ ≥
0, as in (4.1),
• c is a constant depending on a certain degree of X and coming from (4.13).

6. Preparation for counting points

6.1. The universal family and non-degeneracy. In this section, we ﬁx the basic
setup to prove Proposition 7.1, described as the alternative on page 4, and our main
results.
Fix an integer g ≥ 2. Recall from §1.2 that Mg denotes the ﬁne moduli space of smooth
curves of genus g, with level-ℓ-structure where ℓ ≥ 3 is ﬁxed, cf. [ACG11, Chapter XVI,
Theorem 2.11 (or above Proposition 2.8)], [DM69, (5.14)], or [OS80, Theorem 1.8]. It
is known that Mg is a regular, quasi-projective variety of dimension 3g − 3. We regard
it over Q; it is irreducible according to our convention introduced below Theorem 1.6.
There exists a universal curve Cg over Mg, it is smooth and proper over Mg and its ﬁbers
are smooth curves of genus g. Moreover, Cg → Mg is projective, cf. [DM69, Corollary
to Theorem 1.2] or [BLR90, Remark 2, §9.3].
Denote by Jac(Cg) the relative Jacobian of Cg → Mg. It is an abelian scheme coming
with a natural principal polarization and equipped with level-ℓ-structure, see [MFK94,
Proposition 6.9].
Recall from §1.2 that Ag denotes the ﬁne moduli space of principally polarized abelian
varieties of dimension g, with level-ℓ-structure. Moreover, Ag is regular and quasi-
projective; see [MFK94, Theorem 7.9 and below] or [OS80, Theorem 1.9]. We regard it
as deﬁned over Q; it is irreducible according to our convention. Let π : Ag → Ag be the
universal abelian variety; it is an abelian scheme. Note that π is projective; we refer to
Remark 3.1 for this and other details.

UNIFORMITY IN MORDELL–LANG FOR CURVES 24

As Ag is a ﬁne moduli space we have the following Cartesian diagram

(6.1)
 Jac(Cg) //

  
 ❴✤ Ag

π
  
Mg τ // Ag

the bottom arrow is the Torelli morphism. As we have level structure, the Torelli
morphism need not be injective on C-points, but it is ﬁnite-to-one on such points, cf.
[OS80, Lemma 1.11].
We also ﬁx an ample line bundle M on Ag, where Ag is a, possibly non-regular,
projective variety containing Ag as a Zariski open and dense subset. The Height Ma-
chine provides an equivalence class of height functions of which we ﬁx a representative
hAg,M : Ag(Q) → R.
Next we ﬁx a projective embedding of Ag over Ag. There is a relatively ample line
bundle L on Ag/Ag with [−1]∗L = L; see [Ray70, Th´eor`eme XI 1.4]. After replacing L
by L⊗N , with N ≥ 4 large enough, we can assume that L is very ample relative over
Ag and [−1]∗L = L. By [Gro61, Proposition 4.4.10(ii) and Proposition 4.1.4], we then
have a closed immersion Ag → Pn
Q × Ag over Ag arising from L ⊗ π∗(M|⊗p
Ag ) for some
integer p ≥ 1, note that M|Ag is ample. For each s ∈ Ag(Q), the ﬁber Ag,s = π−1(s) is
realized as a projective subvariety of Pn
Q and the induced closed immersion Ag,s → Pn
Q
comes from the restriction L|Ag,s which is ample. Flatness of Ag → Ag implies that
dim H 0(Ag,s, LAg.s) is independent of s. So Ag,s is projectively normal inside Pn
Q, a
property that will play a role later on.
Recall that L is symmetric and very ample on each ﬁber of Ag. By Tate’s Limit
Argument we obtain the ﬁberwise N´eron–Tate height, cf. (3.2),

(6.2) ˆh : Ag(Q) → [0, ∞).

Let M ≥ 1 be an integer. We write A
[M ]
g for the M-fold ﬁbered power Ag ×Ag · · ·×Ag Ag
over Ag. Then A
[M ]
g → Ag is an abelian scheme.
By taking the product we obtain closed immersions A
[M ]
g → (Pn
Q)M × Ag. The ﬁber

of A
[M ]
g → Ag above s ∈ Ag(Q) is the M-fold power of Ag,s. The associated ﬁberwise
N´eron–Tate height ˆh : A
[M ]
g (Q) → [0, ∞) is the sum of the N´eron–Tate heights, as in
(6.2), of the M coordinates.
Let us now deﬁne the Faltings–Zhang morphism. In our setting the relative Picard
scheme Pic(Cg/Mg) exists as a group scheme over Mg. It is a union over all p ∈ Z of open
and closed subschemes Picp(Cg/Mg), where p indicates the degree of a line bundle. By
deﬁnition we have Jac(Cg) = Pic0(Cg/Mg). We cannot expect to have a section of Cg →
Mg, so we cannot expect to ﬁnd an immersion of Cg into Jac(Cg/Mg). As constructed
in the proof of [MFK94, Proposition 6.9] we do have a morphism Cg → Pic1(Cg/Mg)
over Mg. Let C
[M ]
g and Picp(Cg/Mg)[M ] denote the respective M-th ﬁbered powers over
Mg. The diﬀerence morphism coming from the group scheme law Pic(Cg/Mg) ×Mg
Pic(Cg/Mg) → Pic(Cg/Mg) restricts to a morphism Pic
1(Cg/Mg) ×Mg Pic
1(Cg/Mg) →
Jac(Cg/Mg) of schemes over Mg. We take the appropriate product morphism over Mg

UNIFORMITY IN MORDELL–LANG FOR CURVES 25

to get a morphism

(6.3) C
[M +1]
g → Jac(Cg/Mg)[M ]

over Mg. The choice of product is modeled after (1.3). More precisely, consider the
situation above a k-point of Mg, where k is an algebraically closed ﬁeld. The ﬁber of Cg →
Mg above this point is a smooth curve C deﬁned over k of genus g. For P0, . . . , PM ∈ C(k)
the morphism (6.3) maps (P0, P1, . . . , PM ) ↦→ (P1 − P0, P2 − P0, . . . , PM − P0) where the
diﬀerence takes place in the Jacobian of C.
Recall (6.1). We take the M-fold product and compose with (6.3) to obtain a com-
mutative diagram of morphisms of schemes

(6.4)
 C
[M +1]
g //

  
 A
[M ]
g

  
Mg τ // Ag.

If S → Mg is a morphism of schemes then we deﬁne CS = Cg ×Mg S and C
[M ]
S =
C
[M ]
g ×Mg S. If S is irreducible, then so is C
[M ]
S by induction on M and a topological
argument using that CS → S is smooth and hence open. Taking the ﬁbered product with
S and composing with (6.4) yields a commutative diagram of morphisms of schemes

C
[M +1]
S //

  
 A
[M ]
g

  
S τ ◦(S→Mg)
// Ag.

By the universal property of the ﬁbered product we get a morphism of schemes

(6.5) C
[M +1]
S DM //
 &&▼▼▼▼▼▼▼▼▼▼▼▼ A
[M ]
g ×Ag S

  
S

over S. We call DM the Faltings–Zhang morphism (over S). Then DM is proper since
the diagonal arrow in (6.5) is proper.
Let for the moment S → Mg be the identity. If s ∈ Mg(Q), then Cs is the curve
parametrized by s, and Ag,τ (s) is its Jacobian. To embed Cs into Ag,τ (s) we must work
with a base point P ∈ Cs(Q). Then Cs − P = D1({P } × Cs) is an irreducible curve inside
Ag lying above τ (s). Hence it provides a closed immersion Cs − P ⊆ Pn
Q.
Let deg X denote the degree of an irreducible closed subvariety X of Pn
Q and let h(X)
denote its height, cf. [BGS94].

Lemma 6.1. There exists a constant c such that the following two properties hold for
all s ∈ Mg(Q).

(i) We have deg(Cs − P ) ≤ c for all P ∈ Ag,τ (s)(Q).
(ii) There exists Ps ∈ Cs(Q) such that h(Cs − Ps) ≤ c max{1, hAg,M(τ (s))}.

UNIFORMITY IN MORDELL–LANG FOR CURVES 26

Proof. We need a quasi-section of Cg → Mg as provided by [Gro67, Corollaire 17.16.3(ii)].
So there is an aﬃne scheme S and a morphism S → Cg that factors through a surjec-
tive, quasi-ﬁnite, ´etale morphism S → Mg. We consider the product Cg ×Mg S → C
[2]
g
composed with the Faltings–Zhang morphism D1 : C
[2]
g → Ag ×Ag Mg over Mg and then
the projection of Ag. This is a morphism of schemes Cg ×Mg S → Ag. Its image is a
constructible subset of Ag. So it is a union of ﬁnitely many irreducible Zariski locally
closed subsets {Xi}i of Ag. We have the following property.
Given a point s ∈ Mg(Q), there is an i such that the ﬁber of π|Xi : Xi → Ag above
τ (s) is a ﬁnite union of irreducible curves, up-to ﬁnitely many points one of these curves
is Cs − Ps with Ps ∈ Cs(Q).
We have a closed immersion Ag → Pn
Q × Ag. Moreover, a suﬃciently large positive
power of M induces a closed immersion of Ag → Pm
Q for some m. Thus, we consider Ag
as a Zariski locally closed subset Pm
Q . We identify each Xi with its image in Pn
Q × Pm
Q ,
an irreducible Zariski locally closed set. Then Cs − Ps ⊆ Pn
Q arises as an irreducible
component of the intersection of some Zariski closure Xi with Pn
Q × {τ (s)}.

We use the Segre embedding Pn
Q × Pm
Q → P(n+1)(m+1)−1
Q to embed our situation into
projective space. By B´ezout’s Theorem [Ful98, Example 8.4.6], deg(Cs − Ps) is bounded
from above uniformly in s. Translating a curve inside Ag,τ (s) by a point of Ag,τ (s)(Q)
does not change its degree. So if P ∈ Ag,τ (s), then deg(Cs − P ) = deg(Cs − Ps). This
yields (i).
Part (ii) follows as (i) but this time we use the Arithmetic B´ezout Theorem, still
executing the intersection after applying the Segre embedding. Indeed, recall that Cs−Ps
as an irreducible of the intersection of some Xi with Pn
Q × {τ (s)}. The height and degree
of Xi are bounded from above independently of s; the same holds for the degree of
Pn
Q × {τ (s)}. The height of Pn
Q × {τ (s)} is bounded from above linearly in terms of
h(τ (s)). Finally, we can apply [Phi95, Th´eor`eme 3]. Finally, note that by the Height
Machine the absolute logarithmic Weil height h(τ (s)), where τ (s) is understood as an
element of Pm
Q (Q), is bounded from above linearly in terms of hAg,M(τ (s)). □

6.2. Non-degeneracy of DM (C
[M +1]
S ) for large M. In this subsection all varieties are
deﬁned over the ﬁeld C. We keep the notation of the previous subsection and let S be
an irreducible variety with a quasi-ﬁnite morphism S → Mg. Note that DM (C
[M +1]
S )
is Zariski closed in A
[M ]
g ×Ag S because DM is proper. We endow this image with the
reduced induced scheme structure.
The following non-degeneracy theorem proved by the second-named author is crucial
to prove our main result. It conﬁrms that Theorem 1.6 can be applied to DM (C
[M +1]
S )
for M ≥ 3g − 2. We obtain a height inequality on a Zariski open dense subset.

Theorem 6.2 ([Gao20a, Theorem 1.2’]). Let S be an irreducible variety with a (not
necessarily dominant) quasi-ﬁnite morphism S → Mg. Assume g ≥ 2 and M ≥ 3g −
2. Then DM (C
[M +1]
S ), which is a closed irreducible subvariety of A
[M ]
g ×Ag S, is non-
degenerate in the sense of Deﬁnition 1.5.

The ﬁbered product in the theorem involves S → Mg τ
−→ Ag.

UNIFORMITY IN MORDELL–LANG FOR CURVES 27

More precisely, the meaning of the conclusion of the theorem is as follows. For the
abelian scheme π : A = A
[M ]
g ×Ag S → S and for the irreducible subvariety X :=
DM (C
[M +1]
S ) of A, there exists a open non-empty subset ∆ of San, with the Betti map
b∆ : A∆ = π−1(∆) → T
2g, such that

(6.6) rankR(db∆|X sm,an)x = 2 dim X for some x ∈ X sm,an ∩ A∆,

when g ≥ 2 and M ≥ 3g − 2.

Proof. This theorem, essentially [Gao20a, Theorem 1.2’], is a consequence of Theorem 1.3
of loc.cit. Because of its importance to the current paper, we hereby give more details
of the deduction.
We start by showing the result for the case where CS → S admits a section ǫ. In
this case ǫ induces an Abel–Jacobi embedding jǫ : CS → Jac(CS/S), which is a closed
immersion of S-schemes. The modular map is the Cartesian diagram

Jac(CS/S) ι //

  
 ❴✤ Ag

  
S // Ag

with the bottom morphism being the composite of the given S → Mg with the Torelli
map τ : Mg → Ag. The Torelli map τ is quasi-ﬁnite; see [OS80, Lemma 1.11]. Thus the
bottom morphism is quasi-ﬁnite. Hence ι is quasi-ﬁnite.
We wish to apply [Gao20a, Theorem 1.3] to the subvariety jǫ(CS) of the abelian scheme
Jac(CS/S) → S. We need to verify the hypotheses. First of all ι|jǫ(CS ) is generically ﬁnite
because ι is quasi-ﬁnite. Hypothesis (a) is satisﬁed since dim jǫ(CS) = dim S +1 > dim S.
For hypotheses (b) and (c), note that for any s ∈ S(C), the ﬁber jǫ(CS)s is the Abel–
Jacobi embedding of Cs in its Jacobian via the point ǫ(s). Thus hypothesis (b) is satisﬁed
because each curve generates its Jacobian, and hypothesis (c) holds true since g ≥ 2.
Thus we can apply [Gao20a, Theorem 1.3.(ii)] and obtain that DM (C
[M +1]
S ) is non-
degenerate
2 if M ≥ jǫ(CS) = dim S + 1. But dim S ≤ dim Mg = 3g − 3. Hence
DM (C
[M +1]
S ) is non-degenerate if M ≥ 3g − 2.
For an arbitrary S, the generic ﬁber of CS → S has a rational point over some
ﬁnite extension of K(S), the function ﬁeld of S. Thus there exists a quasi-ﬁnite ´etale
dominant (not necessarily surjective) morphism ρ : S′ → S, with S′ irreducible, such
that CS′ = CS ×S S′ → S′ admits a section. Thus X ′ := DM (C
[M +1]
S′ ), as a subvariety of
A′ := A
[M ]
g ×Ag S′, is non-degenerate by the previous case. So there exists a connected,
open non-empty subset ∆
′ of S′an, with the Betti map b∆′ : A′
∆′ → T
2g, such that for
some x
′ ∈ X ′sm,an ∩ A′
∆′ we have

rankR(db∆′|X ′sm,an)x′ = 2 dim X ′.

We may furthermore shrink ∆
′ so that ρ|∆′ is a diﬀeomorphism. In particular ∆ := ρ(∆
′)
is open in San.

2Observe that DM (C[M+1]
S ) = D A
M (jǫ(C[M+1]
S )), with D A
M be as in [Gao20a, Theorem 1.3.(ii)] with
A = Ag ×Ag S ∼= Jac(CS/S). See below (6.3).

UNIFORMITY IN MORDELL–LANG FOR CURVES 28

Denote by ρ
′
A : A′ = A ×S S′ → A the projection to the ﬁrst factor. Then ρ
′
A|A′
∆′ is
a diﬀeomorphism. Both A → S and A′ → S′ carry level-ℓ-structures. By construction
and uniqueness properties of the Betti map, we may assume that b∆ : A∆ → T
2g equals
b∆′ ◦ (ρ
′
A|A′
∆′ )−1. Thus
 rankR(db∆|X sm,an)x = 2 dim X ′

with x = ρA(x
′). So (6.6) holds true because dim X ′ = dim X. Hence we are done. □

6.3. Technical lemmas. The following lemma will be useful in the proofs of the desired
bounds. Let for the moment k be an algebraically closed ﬁeld and M ≥ 1, n ≥ 1 integers.
If Z is a Zariski closed subset of (Pn
k )M we let deg Z denote the sum of the degrees of all
irreducible components of Z with respect to O(1, . . . , 1).

Lemma 6.3. Let C ⊆ Pn
k be an irreducible curve deﬁned over k and let Z ⊆ (Pn
k )M be
a Zariski closed subset of (Pn
k )M such that C M = C × · · · × C ̸⊆ Z. Then there exists a
number B, depending only on M, deg C, and deg Z, satisfying the following property. If
Σ ⊆ C(k) has cardinality ≥ B, then Σ
M = Σ × · · · × Σ ̸⊆ Z(k).

Proof. Let us prove this lemma by induction on M. The case M = 1 follows easily from
B´ezout’s Theorem.
Assume the lemma is proved for 1, . . . , M − 1. Let q : (Pn
k )M → Pn
k be the projection
to the ﬁrst factor.
The number of irreducible components of Z ∩ C M and their degrees are bounded
from above in terms of M, deg C, and deg Z by B´ezout’s Theorem applied to the Segre
embedding. Let Z ′ be the union of all irreducible components Y of Z ∩ C M with
dim q(Y ) ≥ 1, let Z ′′ be the union of all other irreducible components.
Note that q(Z ′) ⊆ C. For all P ∈ C(k) the ﬁber q|−1
Z ′ (P ) = Z ′ ∩ ({P } × (Pn
k )M −1) has
dimension at most dim Z ′ − 1 ≤ M − 2. So the projection of q|−1
Z ′ (P ) to the ﬁnal factors
(Pn
k )M −1 does not contain C M −1. By B´ezout’s Theorem the degree of this projection is
bounded in terms of M, deg C, and deg Z. We apply the induction hypothesis to the
projection of q|−1
Y (P ) to (Pn
k)M −1 and obtain a number B′, depending only on M, deg C,
and deg Z satisfying the following property. If Σ ⊆ C(k) has cardinality ≥ B′, then
{P } × Σ
M −1 ̸⊆ Z ′(k) for all P ∈ C(k).
Now dim q(Z ′′) = 0, so q(Z ′′) is a ﬁnite set of cardinality at most B′′, the number of
irreducible components of Z ∩ C M .
The lemma follows with B = max{B′, B′′ + 1}. □

In the next lemma we use the Faltings–Zhang morphism in a single abelian variety A,
i.e., DM : A
M +1 → A
M deﬁned by (P0, . . . , PM ) ↦→ (P1 − P0, . . . , PM − P0).

Lemma 6.4. Let A be an abelian variety deﬁned over Q and suppose C is a smooth
curve of genus g ≥ 2 contained in A. If Z is an irreducible Zariski closed and proper
subset of DM (C M +1), then

#{P ∈ C(Q) : (C − P )M ⊆ Z} ≤ 84(g − 1).

Proof. For simplicity denote by Ξ = {P ∈ C(Q) : (C − P )M ⊆ Z}. Fix P0 ∈ Ξ. It
suﬃces to prove that there are only 84(g − 1) possibilities for P1 − P0 when P1 runs over
Ξ.
 UNIFORMITY IN MORDELL–LANG FOR CURVES 29

Say P1 ∈ Ξ and let i ∈ {0, 1}. Note that Z ⊊ DM (C M +1) and so dim Z <
dim DM (C M +1) ≤ M + 1, as DM (C M +1) irreducible. Note that (C − Pi)M ⊆ Z, and so
both have dimension M. As Z is irreducible we ﬁnd (C − Pi)M = Z for i = 0 and i = 1.
Applying the ﬁrst projection A
M → A yields C −P1 = C −P0. In other words, P1 −P0
stabilizes C. By Hurwitz’s Theorem [Hur92], a smooth curve over Q of genus g ≥ 2 has
at most 84(g − 1) automorphisms. Hence we are done. □

7. N´eron–Tate distance between points on curves

The goal of this section is to prove Proposition 7.1, below. Namely we will show
that Q-points on smooth curves are rather “sparse”, in the sense that the N´eron–Tate
distance between two Q-points on a smooth curve C is in general large compared with
the Weil height of C.
We use the notation from §6.1. Recall that we have ﬁxed a projective compactiﬁcation
Ag of Ag over Q, an ample line bundle M, and a height function hAg,M : Ag(Q) → R
attached to this pair. We also ﬁxed a closed immersion Ag into Pn
Q × Ag over Ag and let
τ : Mg → Ag denote the Torelli morphism. If s ∈ Mg(Q) then Cs is a smooth curve of
genus g deﬁned over Q. Moreover, if P, Q ∈ Cs(Q), then P − Q is a well-deﬁned element
of Ag(Q) and so is its N´eron–Tate height ˆh(P − Q), see (6.2).

Proposition 7.1. Let S be an irreducible closed subvariety of Mg deﬁned over Q. There
exist positive constants c1, c2, c3, c4 depending on the choices made above and on S with
the following property. Let s ∈ S(Q) with hAg,M(τ (s)) ≥ c1. There exists a subset
Ξs ⊆ Cs(Q) with #Ξs ≤ c2 such that any P ∈ Cs(Q) satisﬁes the following alternative.

(i) Either P ∈ Ξs;
(ii) or #{Q ∈ Cs(Q) : ˆh(Q − P ) ≤ hAg ,M(τ (s))/c3} < c4.

Proof. We ﬁx an immersion of Mg into some projective space and let Mg denote its
Zariski closure. By a standard triangle inequality estimate, there exist constants c′′ > 0
and c′′′ ≥ 0 such that

(7.1) h(s) ≥ c′′hAg,M(τ (s)) − c′′′

for all s ∈ Mg(Q); see [Sil11, Lemma 4], the left-hand side is the Weil height and
represents a height function coming from an ample line bundle on Mg. If hAg,M(τ (s)) ≥
c1 with c1 ≥ 2c′′′/c′′ then h(s) ≥ c′′hAg,M(τ (s))/2. We ﬁnd that it suﬃces to prove the
alternative with hAg,M(τ (s)) replaced by h(s) in (ii) and adjusting c3. Our proof is by
induction on dim S.
If dim S = 0, then the proposition follows by enlarging c1.
If dim S ≥ 1, we ﬁx M = 3g − 2. Applying Theorem 6.2 to the immersion Ssm ֒→ Mg,
we conclude that the closed irreducible subvariety X := DM (C
[M +1]
Ssm ) of the abelian
scheme A = A
[M ]
g ×Ag Ssm → Ssm is non-degenerate. Hence we can apply Theorem 1.6
to A and X (and the compactiﬁcation S is the Zariski closure of S in Mg). So, combined
with (7.1), there exist constants c > 0 and c′ as well as a Zariski open dense subset U of
X, satisfying the following property. For all s ∈ S(Q) and all P, Q1, . . . , QM ∈ Cs(Q),

UNIFORMITY IN MORDELL–LANG FOR CURVES 30

we have

(7.2) ch(s) ≤ ˆh(Q1 − P ) + · · · + ˆh(QM − P ) + c′ if (Q1 − P, . . . , QM − P ) ∈ U(Q).

Observe that π(X) = Ssm, where π : A → Ssm is the structure morphism. Therefore,
S \ π(U) is not Zariski dense in S. Let S1, . . . , Sr be the irreducible components of the
Zariski closure of S \ π(U) in S. Then dim Sj ≤ dim S − 1 for all j.
By the induction hypothesis, this proposition holds for all Sj. Thus it remains to
prove the conclusion of this proposition for curves above

(7.3) s ∈ S(Q) \
 r⋃

j=1 Sj(Q) ⊆ π(U(Q)).

First we construct Ξs and then we will show that we are in one of the two alternatives.
It is convenient to ﬁx a base point Ps ∈ Cs(Q) and consider (Cs − Ps)M as a subvariety
of As = π−1(s).
Let us set W = X \ U, it is a Zariski closed and proper subset of X. By (7.3) we ﬁnd
Ws ⊊ Xs = DM (C
[M +1]
s ).
Let Z be an irreducible component of Ws. Consider the set

ΞZ := {P ∈ Cs(Q) : (Cs − P )M ⊆ Z}.

Apply Lemma 6.4 to A = (Ag)τ (s), C = Cs − Ps ⊆ A, and Z. As Z ⊊ DM (C
[M +1]
s ) we
have #ΞZ ≤ 84(g − 1).
Let Ξs = ⋃
Z ΞZ where Z runs over all irreducible components of Ws. The number of
irreducible components is bounded from above in an algebraic family. So the number of
irreducible components of Ws is bounded from above by a number that is independent of
s; but it may depend on W . We take c2 to be such a number multiplied with 84(g − 1).
Thus #Ξs ≤ c2 if (7.3) and with c2 independent of s and P .
Say P ∈ Cs(Q) and P ̸∈ Ξs. So we are not in case (i) of the proposition. Then
(Cs − P )M ̸⊆ Ws. We want to apply Lemma 6.3 to Cs − P and Ws.
Recall that the abelian scheme Ag is embedded in Pn
Q × Ag over Ag, cf. §6.1. So A
is embedded in (Pn
Q)M × Ssm over Ssm. We may identify Cs − P with a smooth curve
in Pn
Q. The degree of Cs − P as a subvariety of Pn
Q is bounded independently of s by
Lemma 6.1(i); applying the Torelli morphism τ does not aﬀect the degree. Moreover,
Ws is Zariski closed in Xs ⊆ As. Still holding s ﬁxed we may take Ws as a Zariski closed
subset of (Pn
Q)M . Being the ﬁber above s of a subvariety of (Pn
Q)M × Ssm, we ﬁnd that
the degree of Ws is bounded from above independently of s. From Lemma 6.3 we thus
obtain a number c4, depending only on these bounds and with the following property.
Any subset Σ ⊆ Cs(Q) with cardinality ≥ c4 satisﬁes (Σ − P )M ̸⊆ Ws. It is crucial that
c4 is independent of s.
We work with Σ = {Q ∈ Cs(Q) : ˆh(Q − P ) ≤ h(s)/c3} with c3 = 2M/c. If #Σ < c4,
then we are in alternative (ii) of the proposition.
Finally, let us assume #Σ ≥ c4. The discussion above implies that there exist
Q1, . . . , QM ∈ Σ such that (Q1 − P, . . . , QM − P ) ̸∈ Ws(Q), i.e., (Q1 − P, . . . , QM − P ) ∈
U(Q). Thus we can apply (7.2) and obtain

h(s) ≤ 1
c
 (
M ch(s)
2M + c′) = 1
2 h(s) + c′

c .

UNIFORMITY IN MORDELL–LANG FOR CURVES 31

Hence h(s) ≤ 2c′/c. Now (7.1) implies hAg,M(τ (s)) < c1 if c1 > (2c′/c + c′′′)/c′′. So this
case cannot occur if hAg,M(τ (s)) ≥ c1 and c1 is suﬃciently large. □

8. Proof of Theorems 1.1, 1.2, and 1.4

The goal of this section is to prove the theorems and the corollary in the introduction.
To this end let g ≥ 2; we retain the notation of §6.1. In particular, π : Ag → Ag is the
universal family of principally polarized abelian varieties of dimension g with level-ℓ-
structure where ℓ ≥ 3 and τ : Mg → Ag is the Torelli morphism.

Proposition 8.1. The exist constants c1 ≥ 0, c2 ≥ 1 depending on the choices made
above with the following property. Let s ∈ Mg(Q) with hAg,M(τ (s)) ≥ c1. Suppose Γ is
a ﬁnite rank subgroup of Ag,τ (s)(Q) with rank ρ ≥ 0. If P0 ∈ Cs(Q), then

#(Cs(Q) − P0) ∩ Γ ≤ c1+ρ
2 .

The proof combines Vojta’s approach to the Mordell Conjecture with the results ob-
tained in §7. We will use R´emond’s quantitative version [R´em00a, R´em00b] of Vojta’s
method. A similar approach was used in the authors’s earlier work [DGH19] which also
contains a review of Vojta’s method in §2. Let us recall the fundamental facts before
proving Proposition 8.1.
Suppose we are given an abelian variety A of dimension g that is deﬁned over Q and
is presented with a symmetric and very ample line bundle L. We assume also that we
have a closed immersion of A into some projective space Pn
Q determined by a basis of
the global sections of L. We assume that A becomes a projectively normal subvariety
of Pn
Q. This is the case if L is an at least fourth power of a symmetric and ample line
bundle.
Suppose C is an irreducible curve in A. Then let deg C denote the degree of C
considered as subvariety of A ⊆ Pn
Q, i.e., deg C = (C.L). Moreover, let h(C) denote the
height of C.
On the ambient projective space we have the Weil height h : Pn
Q(Q) → [0, ∞). Tate’s

Limit Argument, compare (3.2), applied to h yields the N´eron–Tate height ˆhL : A(Q) →
[0, ∞). It vanishes precisely on the points of ﬁnite order. Moreover, it follows from
Tate’s construction that there exists a constant cNT ≥ 0, which depends on A, such that

(8.1) |ˆhL(P ) − h(P )| ≤ cNT

for all P ∈ A(Q).
Finally, we need a measure for the heights of homogeneous polynomials that deﬁne the
addition and substraction on A, as required in R´emond’s [R´em00b]. Consider the n + 1
global sections of O(1) corresponding to the projective coordinates of Pn
Q. They restrict
to global sections ξ0, . . . , ξn of L on A. Let f : A × A → A × A denote the morphism
induced by (P, Q) ↦→ (P + Q, P − Q), and let p1, p2 : A × A → A be the ﬁrst and section
projection, respectively. For all i, j ∈ {0, . . . , n} there are Pij ∈ Q[X, X′] with

(8.2) f ∗(p∗
1ξi ⊗ p∗
2ξj) = Pij((p∗
1ξ0, . . . , p∗
1ξn), (p∗
2ξ0, . . . , p∗
2ξn))

and where Pij is bihomogeneous of bidegree (2, 2) in X = (X0, . . . , Xn) and X′ =
(X ′
0, . . . , X ′
n); see [R´em00b, Proposition 5.2] with a = b = 1 for the existence of the

UNIFORMITY IN MORDELL–LANG FOR CURVES 32

Pij. Here we require that ξ0, . . . , ξn constitute a basis of H 0(A, L). Let h1 denote the
Weil height of the point in projective space whose coordinates are all coeﬃcients of all
Pij.
We point out a minor omission in [DGH19, §2]: h1 there must also involve both
addition and subtraction on A, and not just the addition.
The lemma below is [DGH19, Corollary 2.3] which is itself a standard application of
R´emond’s explicit formulation of the Vojta and Mumford inequalities. We thus obtain
a bound that is exponential in the rank of the subgroup Γ for points of suﬃciently large
N´eron–Tate height.

Lemma 8.2. Let C be an irreducible curve in A. There exists a constant c = c(n, deg C) ≥
1 depending only on n and deg C with the following property. Suppose Γ is a subgroup
of A(Q) of ﬁnite rank ρ ≥ 0. If C is not the translate of an algebraic subgroup of A,
then # {
P ∈ C(Q) ∩ Γ : ˆhL(P ) > c max{1, h(C), cNT, h1}} ≤ cρ.

Proof of Proposition 8.1. As in §6.1 we have a closed immersion Ag → Pn
Q × Ag over Ag.
Let s ∈ Mg(Q) with

(8.3) hAg ,M(τ (s)) ≥ max{1, c1},

where c1 comes from Proposition 7.1 applied to S = Mg.
We now bound two quantities attached to the abelian variety A = Ag,τ (s) taken with
its closed immersion into Pn
Q. Observe that this closed immersion satisﬁes the condition
imposed at the beginning of this section with L = L|A where L is as in §6.1. These
quantities may depend on s. Below, c > 0 denotes a constant that depends on the ﬁxed
data such as g, n, and the ambient objects such as Ag but not on s. We will increase c
freely and without notice.

Bounding cNT. For this we require the Silverman–Tate Theorem, Theorem A.1,
applied to π : Ag → Ag. Recall that h is the Weil height on Pn
Q(Q). For all P ∈ A(Q)

we have |h(P ) − ˆh(P )| ≤ c max{1, hAg,M(τ (s))}; note that we can bound hS(π(P )) from
above linearly in terms of hAg ,M(τ (s)) by the Height Machine. So we may take

(8.4) cNT = c max{1, hAg,M(τ (s))}.

Bounding h1. Recall that f : A
2 → A
2 sends (P, Q) to (P + Q, P − Q). We know
that Pij as above exist. Here we will construct such a family with controlled height.
To this end we consider points P = [ζ0 : · · · : ζn], Q = [η0 : · · · : ηn] ∈ A(Q). Then
f (P, Q) = ([ν+
0 : · · · : ν+
n ], [ν−
0 : · · · : ν−
n ]). Recall that A = Ag,τ (s) is presented as
a projectively normal subvariety of Pn
Q by the construction in §6.1. By (8.2) there is
for each i, j ∈ {0, . . . , n} a bihomogeneous polynomial Pij of bidegree (2, 2) that is
independent of P and Q, with

(8.5) ν+
i ν−
j = λPij((ζ0, . . . , ζn), (η0, . . . , ηn))

for some non-zero λ ∈ Q that may depend on (P, Q). We eliminate λ and consider

(8.6) ν+
i ν−
j Pi′j′((ζ0, . . . , ζn), (η0, . . . , ηn)) − ν+
i′ ν−
j′ Pij((ζ0, . . . , ζn), (η0, . . . , ηn)) = 0

UNIFORMITY IN MORDELL–LANG FOR CURVES 33

as a system of homogeneous linear equations parametrized by (i, j), (i
′, j′) ∈ {0, . . . , n}2,
the unknowns are the coeﬃcients of the Pij. As each Pij is bihomogeneous of bidegree
(2, 2), the number of unknowns is N = (n + 1)2(n+2
2 )2 which is independent of s.
Each pair of points (P, Q) ∈ A(Q)2 yields one system of linear equations. We know
that there is a non-trivial solution (Pij)ij that solves for all (P, Q) simultaneously and
such that some Pij does not vanish identically on A × A. Our goal is to ﬁnd such a
common solution of controlled height.
First, observe that a common solution for when (P, Q) runs over all torsion points of
A
2(Q) is a common solution for all pairs (P, Q). Indeed, this follows as torsion points
of A
2(Q) lie Zariski dense in A
2. Second, observe that the full system has ﬁnite rank
M < N so it suﬃces to consider only ﬁnite many torsion points (P, Q).
Our task is thus to ﬁnd a common solution to (8.6) for all (i, j), (i
′, j′), where some
Pij does not vanish identically on A × A, and where [ζ0 : · · · : ζn],[η0 : · · · : ηn], and
[ν±
0 : · · · : ν±
n ] are certain torsion points on A(Q). We may assume that some ζi is 1 and
similarly for ηi and ν±
i . So all coordinates are in Q. Moreover, the height of each torsion
point is at most cNT by (8.1). The resulting system of linear equations is represented by
an M × N matrix with algebraic coeﬃcients. By elementary properties of the height,
each coeﬃcient in the system has aﬃne Weil height c · cNT, for c large enough. It is
tempting, but unnecessary, to invoke Siegel’s Lemma to ﬁnd a non-trivial solution. As
M, N are bounded in terms of n, Cramer’s Rule establishes the existence of a basis of
non-zero solution such that the Weil height of the coeﬃcient vector is at most c · cNT.
Among this basis there is one solution where one Pij does not vanish identically on
A × A. By (8.4) we ﬁnd

(8.7) h1 ≤ c max{1, hAg,M(τ (s))}

for the projective height of the tuple (Pij)ij. Thus (8.6) holds and so we get (8.5) on all
of A
2(Q), at least with λ a rational function on A × A that is not identically zero. But λ
cannot vanish anywhere on A × A, as otherwise the left-hand side of (8.5) would vanish
at some point of A × A for all (i, j). Hence λ is a non-zero constant. Replacing Pij by
λPij does not change the projective height; we get (8.2) with the desired bound for h1.

Bounding height and degree of a curve. By Lemma 6.1 we have

(8.8) deg(Cs − Ps) ≤ c and h(Cs − Ps) ≤ c max{1, hAg,M(τ (s))}

for some Ps ∈ Cs(Q).

We now follow the argumentation in [DGH19]. Let Γ be a subgroup of Ag,τ (s)(Q) for
ﬁnite rank ρ. We ﬁrst prove the proposition in the case P0 = Ps. We apply Lemma 8.2
to the curve C = Cs − Ps ⊆ Ag,τ (s) = A and use the bounds (8.4), (8.7), and (8.8). Note
that C is a smooth curve of genus g ≥ 2. So it cannot be the translate of an algebraic
subgroup of A. It follows that the number of points P ∈ Cs(Q) with P − Ps ∈ Γ and
ˆh(P − Ps) > R2 where

(8.9) R = (c max{1, hAg,M(τ (s))})1/2

is at most cρ ≤ c1+ρ.
 UNIFORMITY IN MORDELL–LANG FOR CURVES 34

The burden of this paper is to ﬁnd a bound of the same quality for the number of
pairwise distinct points P1, P2, P3, . . . in Cs(Q) with ˆh(Pi − Ps) ≤ R2. This is where
Proposition 7.1 enters. Recall our assumption (8.3) on s. Let c′
2 be the constant c2 from
Proposition 7.1; it is independent of s. As #Ξs ≤ c′
2 we may assume Pi ̸∈ Ξs for all i.
So we may assume that each Pi is in the second alternative of Proposition 7.1.
As in [DGH19] we use the Euclidean norm | · | deﬁned by ˆh
1/2 on the ρ-dimensional R-
vector space Γ ⊗ R. Let r ∈ (0, R]. By an elementary ball packing argument, any subset
of Γ ⊗ R contained in a closed ball of radius R is covered by at most (1 + 2R/r)ρ closed
balls of radius r centered at elements of the given subset; see [R´em00a, Lemme 6.1].
We apply this geometric argument to R as in (8.9) and to r, the positive square-root of
hAg,M(τ (s))/c3 = max{1, hAg,M(τ (s))}/c3. The contribution of the height hAg ,M(τ (s))
cancels in the quotient R/r. We ﬁnd R/r ≤ c. So the number of balls in the covering is
at most c1+ρ.
By Proposition 7.1(ii) the number of the Pi’s that map to a single closed ball of radius
r is at most c4. Thus after increasing c we ﬁnd that #{Pi ∈ Cs(Q) ∩ Γ : ˆh(Pi − Ps) ≤
R2} ≤ c4c1+ρ, as desired. This completes the proof of the proposition in the case P0 = Ps
for suﬃciently large c2.
The case of a general base point follows easily as our estimates depend only on the
rank ρ of Γ. Indeed, let P0 ∈ Cs(Q) be an arbitrary point and let Γ′ be the subgroup of
Ag,τ (s)(Q) generated by Γ and P0 − Ps. Its rank is at most ρ + 1.
Now if Q ∈ Cs(Q) − P0 lies in Γ, then Q + P0 − Ps ∈ Cs(Q) − Ps lies in Γ′. The
number of such Q is at most c2+ρ
2 by what we already proved. The proposition follows
as c2+ρ
2 ≤ (c2
2)1+ρ and since we may replace c2 by c2
2. □

Proof of Theorem 1.1. It is possible to deduce Theorem 1.1 from Theorem 1.2, which
we prove below. However in view of the importance of Theorem 1.1, we hereby give it
a complete proof.
This proof works for any level ℓ ≥ 3, but we may ﬁx ℓ = 3 for deﬁniteness. Let
Ag, Ag, M, and hAg,M be as in §6.1.
Our curve C corresponds to an F -rational point sF of Mg,1, the coarse moduli space
of smooth genus g curves without level structure.
The ﬁne moduli space Mg of smooth genus g curves with level-ℓ-structure is a ﬁnite
cover of Mg,1. For this proof it is convenient to recall that Mg is deﬁned over the
cyclotomic ﬁeld generated by a third root of unity; recall the convention that we ﬁxed
a third root of unity and that Mg is geometrically irreducible. Say s ∈ Mg(Q) maps to
sF . Then F ′ = F (s) is a number ﬁeld and [F ′ : F ] is bounded above only in terms of g
and ℓ. We may identify CF ′ = C ⊗F F ′ with Cs, the ﬁber of Cg → Mg above s.
Constructing the Jacobian commutes with ﬁnite ﬁeld extension. We thus view Γ =
Jac(C)(F ) as a subgroup of Jac(C)(Q) = Jac(CF ′)(Q).
To prove the theorem we may assume C(F ) ̸= ∅. So ﬁx P0 ∈ C(F ). We con-
sider the Abel–Jacobi embedding C − P0 ⊆ Jac(C) deﬁned over F . Then #C(F ) ≤
#(CF ′(Q) − P0) ∩ Γ = #(Cs(Q) − P0) ∩ Γ. If hAg,M(τ (s)) ≥ c1, the theorem follows from
Proposition 8.1. Note that in this case, the constant c in (1.1) is independent of d.
So we may assume that the height of τ (s) is less than c1. As [F ′ : Q] ≤ [F ′ : F ][F :
Q] ≤ [F ′ : F ]d, Northcott’s Theorem implies that τ (s) comes from a ﬁnite set in Ag(Q)

UNIFORMITY IN MORDELL–LANG FOR CURVES 35

that depends only on g, d, and ℓ. The same holds for s and thus F ′ = F (s) since
the Torelli morphism τ is ﬁnite-to-1 and thus has ﬁbers of bounded cardinality. This
means that the remaining C are twists in ﬁnitely many F ′-isomorphism classes. But
then it suﬃces to apply R´emond’s estimate [DP02, page 643] to a single CF ′ and use
#C(F ) ≤ #(CF ′(Q) − P0) ∩ Γ to conclude the theorem.
Silverman’s older result [Sil93, Theorem 1] also handles uniformity among twists. □

Let us explain how to obtain some extra uniformity in the second case of the proof.
More precisely, we show that the constant c(g, d) in (1.1) grows polynomially in d. We
retain the above proof’s notation.
Denote by ρ : Ag = Ag,ℓ → Ag,1 the natural morphism to the coarse moduli space
which forgets the level structure. We recall that Ag is presented as a closed subvariety
of projective space induced by a basis of global sections of a positive powers of ample
line bundle M. Let ι : Ag,1 → Pm
Q be an immersion, as before Theorem 1.2. By [Sil11,
Lemma 4], there exist c′ > 0 and c′′ ≥ 0 depending on the immersions such that
h(ι(ρ(t))) ≤ c′hAg ,M(t) + c′′ for all t ∈ Ag(Q). So h(ι(ρ(τ (s)))) ≤ c′c1 + c′′ is bounded
uniformly in the second case.
By fundamental work of Faltings [Fal83, §3 including the proof of Lemma 3], see
also [FC90, the remarks below Proposition V.4.4 and Proposition V.4.5], the stable
Faltings height of Ag,τ (s) is bounded from above in terms of c′c1 + c′′ and g only. The
height hDP(Ag,τ (s)) used by David and Philippon is bounded similarly by work of Bost
and David, see [DP02, Corollaire 6.9] and [Paz12].
In R´emond’s bound [DP02, page 643] for #(CF ′(Q) − P0) ∩ Γ, the base in the expo-
nential depends polynomially on D max{1, hDP(Ag,τ (s))}, where D is the degree over Q
of a suitable ﬁeld of deﬁnition of Ag,τ (s). As this abelian variety can be deﬁned over F ′

we may assume D ≤ [F ′ : F ]d is bounded linearly in d. Recall that deg(CF ′ − P0) is
bounded from above uniformly. So R´emond’s bound implies that c(g, d) in (1.1) can be
chosen to grow at most polynomially in d.
The deﬁnition of hDP(Ag,τ (s)) involves theta functions and a diﬀerent kind of level
structure. Using standard results on heights and by going down and up in the level
structure it is likely that one can bound hDP(Ag,τ (s)) from above directly in terms of
hAg,M(τ (s)). For this one would need to work with a diﬀerent level ℓ in the proof of
Theorem 1.1.

Proof of Theorem 1.2. We keep the same notation as in the proof of Theorem 1.1. So
ℓ = 3 and Ag, Ag, M, and hAg,M are as in §6.1.
Let C be a smooth curve of genus g ≥ 2 deﬁned over Q, and let Γ be a ﬁnite rank
subgroup of Jac(C)(Q). Let P0 ∈ C(Q).
The curve C corresponds to a Q-point sc of Mg,1.
The ﬁne moduli space Mg of smooth genus g curves with level-ℓ-structure is a ﬁnite
covering of Mg,1. So there exists an s ∈ Mg(Q) that maps to sc. Thus C is isomorphic,
over Q, to the ﬁber Cs of the universal family Cg → Mg. We thus view Γ as a ﬁnite rank
subgroup of Jac(Cs)(Q), and P0 ∈ Cs(Q).
Consider the Abel–Jacobi embedding C − P0 ⊆ Jac(C). Then #(C(Q) − P0) ∩ Γ =
#(Cs(Q)−P0)∩Γ. If hAg,M(τ (s)) ≥ c1, then #(C(Q)−P0)∩Γ ≤ c1+ρ
2 by Proposition 8.1.

UNIFORMITY IN MORDELL–LANG FOR CURVES 36

Thus it suﬃces to ﬁnd a constant c′
1 ≥ 0 that is independent of C and such that
h(ι([Jac(C)])) ≥ c′
1 implies hAg,M(τ (s)) ≥ c1.
As after the proof of Theorem 1.1 denote by ρ : Ag = Ag,ℓ → Ag,1 the natural mor-
phism. As in the proof of Theorem 1.2 we use h(ι(ρ(t))) ≤ c′hAg,M(t) + c′′ for all
t ∈ Ag(Q). The theorem follows since ρ(τ (s)) = [Jac(C)]. □

Remark 8.3. It is possible to prove Theorem 1.1 (without the dependency claims on
c(g, d)) using Theorem 1.2. Let C be a smooth curve of genus g ≥ 2 deﬁned over a
number ﬁeld F ⊆ Q. Then by taking Γ = Jac(C)(F ) in Theorem 1.2, we can conclude
Theorem 1.1 if h(ι([Jac(C)])) ≥ c1. The case h(ι([Jac(C)])) < c1 can be handled as
in the proof of Theorem 1.1, and one can furthermore obtain extra uniformity for c2
in Theorem 1.2 by applying R´emond’s bound [DP02, page 643] as after the proof of
Theorem 1.1.

Proof of Theorem 1.4. Let C be a smooth curve of genus g ≥ 2 deﬁned over a number
ﬁeld F ⊆ Q.
Apply Theorem 1.2 to CQ, P0 ∈ C(Q) and Γ = Jac(C)(Q)tors, whose rank is 0. Then
we obtain c1 ≥ 0 and c2 ≥ 1 such that

#(C(Q) − P0) ∩ Jac(C)(Q)tors ≤ c2

if h(ι([Jac(CQ)])) ≥ c1.
By the Northcott property and Torelli’s Theorem, there are up-to Q-isomophism
only ﬁnitely many CQ’s deﬁned over a number ﬁeld F with [F : Q] ≤ d such that
h(ι([Jac(CQ)])) < c1. By applying Raynaud’s result on the Manin–Mumford Conjecture
to each one of these ﬁnitely many curves separately, we obtain Theorem 1.4. □

Appendix A. The Silverman–Tate Theorem revisited

Our goal in this appendix is to present a treatment of the Silverman–Tate Theorem,
[Sil83, Theorem A], using the language of Cartier divisors. Using Cartier divisors as
opposed to Weil divisors allows us to relax the ﬂatness hypotheses imposed on π in
the notation of [Sil83, §3]. Apart from this minor tweak we closely follow the original
argument presented by Silverman.
Suppose S is a regular, irreducible, quasi-projective variety over Q. Let π : A → S be
an abelian scheme. We write η for the generic point of S and Aη for the generic ﬁber of
π. Then Aη is an abelian variety deﬁned over Q(η).
Suppose we are presented with a closed immersion A → Pn
Q × S over S and with a
projective variety S containing S as a Zariski open and dense subset. We will assume
that S is embedded into Pm
Q . We do not assume that S is regular.
We identify A with a subvariety of Pn
Q × S. Moreover, let A denote the Zariski closure
of A in Pn
S = Pn
Q × S ⊆ Pn
Q × Pm
Q .
We set L = O(1, 1)|A and L = L|A. We will assume in addition that [−1]∗Lη ∼= Lη
where Lη is the restriction of L to Aη. This implies [2]∗Lη ∼= L⊗4
η .
Given these immersions, we have several height functions. For (P, s) ∈ A(Q) ⊆
Pn
Q(Q) × Pm
Q (Q) we deﬁne h(P, s) = h(P ) + h(s) using the Weil height. Moreover, for

UNIFORMITY IN MORDELL–LANG FOR CURVES 37

s ∈ S(Q) ⊆ Pm
Q (Q) we deﬁne hS(s) = h(s). Finally, for all P ∈ A(Q) we denote by

ˆhA(P ) = lim
N →∞ h([N](P ))
N 2

the N´eron–Tate height with respect to L; it is well-known that the limit converges, cf.
the reference around (3.2).
We will prove the following variant of the Silverman–Tate Theorem.

Theorem A.1. There exists a constant c > 0 such that for all P ∈ A(Q) we have
∣
∣ˆhA(P ) − h(P )∣
∣ ≤ c max{1, hS(π(P ))}.

The constant c depends on A and on the various immersions but not on P . The proof
is distributed over the next subsections.

A.1. Extending multiplication-by-2. We keep the notation from the previous sub-
section. We have constructed a (very naive) projective model A of A. Note that A and
S may fail to be regular. Moreover, the natural morphism A → S, which we also denote
by π, may fail to be smooth or even ﬂat.
Multiplication-by-2 is a morphism [2] : A → A that extends to a rational map A 99K
A. We consider the graph of [2] on A as a subvariety of A ×S A. Let A
′ be the Zariski
closure of this graph inside A×S A. Write ρ : A′ → A for the restriction of the projection
onto the ﬁrst factor and [2] for the restriction onto the second factor. We may identify
A with a Zariski open subset of A′. Under this identiﬁcation, ρ restricts to the identity
on A and [2] restricts to multiplication-by-2 on A.
The following diagram commutes
 A

⊇
 A
′ρ
oo
 ⊇
 [2] // A

⊇

A A [2] // A

where the ﬁrst and third inclusions are equal and the middle one comes from the iden-
tiﬁcation involved in the graph construction.

A.2. Proof of the Silverman–Tate Theorem. We keep the notation from the pre-
vious subsection.

Proposition A.2. There exists a constant c1 > 0 such that

(A.1) |h([2](P )) − 4h(P )| ≤ c1 max{1, hS(π(P ))}

holds for all P ∈ A(Q).

Proof. We deﬁne

(A.2) F ′ = [2]
∗L ⊗ ρ
∗L⊗(−4) ∈ Pic(A′).

Recall that we have identiﬁed A with a Zariski open subset of A′. The restriction of
[2]∗L to the generic ﬁber Aη ⊆ A ⊆ A
′ coincides with [2]∗Lη and the restriction of ρ
∗L
to Aη is identiﬁed with Lη. Using our assumption [2]∗Lη ∼= L⊗4
η on the generic ﬁber Aη
we see that F ′ is trivial on Aη.

UNIFORMITY IN MORDELL–LANG FOR CURVES 38

By [Gro67, Corollaire 21.4.13 (pp. 361 of EGA IV-4, in Errata et Addenda, liste 3)]
applied to A → S there exists a line bundle M on S such that π|∗
AM ∼= F ′|A.
Let us ﬁrst desingularize the compactiﬁed base S by applying Hironaka’s Theorem.
Thus there is a proper, birational morphism b : S′ → S that is an isomorphism above
S such that S′ is regular. We consider S as Zariski open in S′. Note that b is even
projective and S′ is integral. So S′ is an irreducible, regular, projective variety.
Now consider the base change A
′ ×S S′. This new scheme may fail to be irreducible
or even reduced. However, recall that b is an isomorphism above the regular S ⊆ S. So
(A′ ×S S′)S = A
′ ×S S is isomorphic to A and thus integral. We may consider A as
an open subscheme of A
′ ×S S′. It must be contained in an irreducible component of
A′ ×S S′. We endow this irreducible component with the reduced induced structure and
obtain an integral, closed subscheme A ⊆ A′ ×S S′. We get a commutative diagram

A ⊆

π   
 A f //

π   
 A′

π◦ρ   
S ⊆ S′ // S

The horizontal morphisms compose to the identity on the domain.
We consider S as a Zariski open subset of S′. As S′ is regular, we can extend M
to a line bundle on the regular S′, cf. [GW10, Corollary 11.41]. The pull-back f ∗F ′ ⊗
π∗M⊗(−1) is trivial on A ⊆ A.
By Hironaka’s Theorem there is a proper, birational morphism β : ̃A → A that is an
isomorphism above A (which is regular) such that ̃A is regular. We may identify A with
a Zariski open subset of ̃A.
Now we pull everything back to the regular ̃A. More precisely, we set F = β∗f ∗F ′.
Then F ⊗ β∗π∗M⊗(−1) is trivial when restricted to A.
To a Cartier divisor D we attach its line bundle O(D). As ̃A is integral we may ﬁx
a Cartier divisor D on ̃A with O(D) ∼= F ⊗ β∗π∗M⊗(−1). Let cyc(D) denote the Weil
divisor of ̃A attached to D. The linear equivalence class of cyc(D) restricted to A is
trivial. By [GW10, Proposition 11.40] cyc(D) is linearly equivalent to a Weil divisor
∑r
i=1 niZi with Zi ⊆ ̃A \ A irreducible and of codimension 1 in ̃A.
We let ̃π denote the composition ̃A → A → S′. Let us consider ̃π(Zi) = Yi. As ̃π is
proper, each Yi is an irreducible closed subvariety of S′. Moreover, Yi ⊆ ̃π( ̃A\A) ⊆ S′\S.
So Yi has dimension at most dim S′ − 1. But Yi could have codimension at least 2 and
thus fail to be the support of a Weil divisor. On the regular S′ a Cartier divisor is
the same thing as a Weil divisor; see [GW10, Theorem 11.38(2)]. For each i we ﬁx a
Cartier divisor Ei of S′ such that cyc(Ei) equals a prime Weil divisor supported on an
irreducible subvariety containing Yi. Since cyc(Ei) is eﬀective, we ﬁnd that Ei is eﬀective,
see [GW10, Theorem 11.38(1)] and its proof. An eﬀective Cartier divisor and its image
under the cycle map cyc(·) have equal support. So the subscheme of S′ attached to Ei
contains Yi.
 UNIFORMITY IN MORDELL–LANG FOR CURVES 39

The pull-back ̃π∗Ei is well-deﬁned as a Cartier divisor, we do not require that π is
ﬂat, cf. [GW10, Proposition 11.48(b)]. By [GW10, Corollary 11.49] the inverse image
̃π−1(Ei), taken as a subscheme of ̃A is the subscheme attached to ̃π∗Ei and ̃π∗Ei is
eﬀective.
Note that ̃π−1(Ei) ⊇ ̃π−1(Yi) ⊇ Zi. The support satisﬁes Supp(̃π∗Ei) ⊇ Zi. Moreover,
as ̃π∗Ei is eﬀective, cyc(̃π∗Ei) is eﬀective and Supp(cyc(̃π∗Ei)) = Supp(̃π∗Ei). Thus

±
 r∑

i=1 niZi ≤ cyc
 (
̃π∗ r∑

i=1 |ni|Ei
)
 .

Recall that cyc(D) = cyc(divφ)+∑r
i=1 niZi for some rational function φ on ̃A. There-
fore,
 0 ≤ cyc
 (

±(D − divφ) + ̃π∗ r∑

i=1 |ni|Ei
)
 .

Since ̃A is regular and in particular normal, we ﬁnd that

(A.3) ± (D − divφ) + ̃π∗ r∑

i=1 |ni|Ei

is an eﬀective Cartier divisor for both signs; see [GW10, Theorem 11.38(1)] and its proof.
Moreover, its support equals the support of

0 ≤ cyc
 (
±(D − divφ) + ̃π∗ r∑

i=1 |ni|Ei
)
 = ±cyc(D − divφ) +
 r∑

i=1 |ni|cyc(̃π∗Ei).

Thus the support of (A.3) lies in ⋃r
i=1 Supp(̃π∗Ei).
We apply O(·) and pass again to line bundles. Let us denote E = O(∑r
i=1 |ni|Ei), a
line bundle on S′. The line bundle attached to (A.3) is (F ⊗ β∗π∗M⊗(−1))⊗(±1) ⊗ ̃π∗E.
Since (A.3) is eﬀective, both (F ⊗β∗π∗M⊗(−1))⊗(±1)⊗̃π∗E have a non-zero global section.
By the Height Machine this translates to

h ̃A,(F ⊗β∗π∗M⊗(−1))⊗(±1)⊗̃π∗E(P ) ≥ O(1)

for all ̃P ∈ ̃A(Q) with ̃π( ̃P ) ̸∈ ⋃
i Supp(Ei). By functoriality properties of the Height
Machine we obtain

|hA
′,F ′(f (β( ̃P )))| ≤ hS′,E(̃π( ̃P )) + |hS′,M(π(β( ̃P )))| + O(1)

for the same ̃P . We recall (A.2) and again use the Height Machine to ﬁnd

|h([2](P ′)) − 4h(ρ(P ′))| ≤ hS′,E(̃π( ̃P )) + |hS′,M(̃π( ̃P ))| + O(1)

where P ′ = f (β( ̃P )). Observe that all points of A(Q) are in the image of f ◦ β.
We recall that the desingularization morphism S′ → S is an isomorphism above S
and that we have identiﬁed A with a Zariski open subset of A′ and of A. Under these
identiﬁcations and if P ′ corresponds to P ∈ A(Q), then [2](P ′) is the duplicate of P ,
ρ(P ′) = P , and ̃π( ̃P ) = π(ρ(P ′)) = π(P ). We apply the Height Machine a ﬁnal time
and use that hS arises from the Weil height restricted to S(Q). We ﬁnd

|h([2](P )) − 4h(P )| ≤ c1 max{1, hS(π(P ))}

UNIFORMITY IN MORDELL–LANG FOR CURVES 40

for all P ∈ A(Q) with ̃π( ̃P ) ̸∈ ⋃
i Supp(Ei), under the identiﬁcations above.
Let P ∈ A(Q). As the Yi lie in ̃π( ̃A \ A) we can choose all Ei above to avoid π(P ).
After doing this ﬁnitely often (using noetherian induction) and replacing the Ei from
before and adjusting c1, we ﬁnd

|h([2](P )) − 4h(P )| ≤ c1 max{1, hS(π(P ))}

for all P ∈ A(Q) where c1 > 0 is independent of P . □

Proof of Theorem A.1. Having (A.1) at our disposal the proof follows a well-known ar-
gument. Indeed, say l ≥ k ≥ 0 are integers. Then applying the triangle inequality to
the appropriate telescoping sum yields
∣
∣
∣
∣h([2l](P ))
4l − h([2k](P ))
4k
 ∣
∣
∣
∣ ≤
 l−1∑

m=k
 ∣
∣
∣
∣ h([2m+1](P ))
4m+1 − h([2m](P ))
4m
 ∣
∣
∣
∣

≤
 l−1∑

m=k 4−(m+1) ∣
∣h([2m+1](P )) − 4h([2m](P ))
∣
∣ .

We apply (A.1) to [2m](P ) and ﬁnd that the sum is bounded by c1x ∑l−1
m=k 4−(m+1) ≤
c1x4−k where x = max{1, hS(π(P ))}. So (h([2l](P ))/4l)
l≥1 is a Cauchy sequence with

limit ˆhA(P ). Taking k = 0 and l → ∞ we obtain from the estimates above that
|ˆhA(P ) − h(P )| ≤ c1x, as desired. □

Appendix B. Full version of Theorem 1.6

The goal of this section is to prove the full version of Theorem 1.6, i.e., without
assuming (Hyp). Let S be an irreducible quasi-projective variety deﬁned over Q and let
π : A → S be an abelian scheme of relative dimension g ≥ 1.
Let L be a relative ample line bundle on A → S with [−1]∗L = L, and let M be an
ample line bundle on a compactiﬁcation S of S. All data above are assumed to be deﬁned
over Q. Set ˆhA,L : A(Q) → R to be the ﬁberwise N´eron–Tate height ˆhA,L(P ) = ˆhAs,Ls(P )
with s = π(P ), and hS,M : S(Q) → R to be a representative of the height provided by
the Height Machine; cf. [BG06, Chapter 2 and 9].
The main result of this appendix is the following theorem.

Theorem B.1. Let X be an irreducible subvariety of A deﬁned over Q. Suppose X
is non-degenerate, as deﬁned in Deﬁnition B.4. Then there exist constants c1 > 0 and
c2 ≥ 0 and a Zariski open dense subset U of X with

(B.1) ˆhA,L(P ) ≥ c1hS,M(π(P )) − c2 for all P ∈ U(Q).

Compared to Theorem 1.6, A → S is no longer required to satisfy (Hyp). Other
minor improvements are that S is not required to be regular and X is not required to
be closed.
In Deﬁnition 1.5, we deﬁned non-degenerate subvarieties using the generic rank of the
Betti map if A → S satisﬁes (Hyp). For an arbitrary A → S, the deﬁnition is similar.
But we need to ﬁrst of all extend our construction of the Betti map, Proposition 2.1, to
an arbitrary A → S.
 UNIFORMITY IN MORDELL–LANG FOR CURVES 41

B.1. Betti map. In this subsection, we extend the construction of the Betti map, i.e.,
Proposition 2.1, to an arbitrary A → S with S regular. In this subsection, let S be
an irreducible, regular, quasi-projective variety over C and let π : A → S be an abelian
scheme of relative dimension g ≥ 1.

Proposition B.2. Let s0 ∈ S(C). Then there exist an open neighborhood ∆ of s0 in
San, and a map b∆ : A∆ := π−1(∆) → T
2g, called the Betti map, with the following
properties.

(i) For each s ∈ ∆ the restriction b∆|As(C) : As(C) → T
2g is a group isomorphism.
(ii) For each ξ ∈ T
2g the preimage b
−1
∆ (ξ) is a complex analytic subset of A∆.
(iii) The product (b∆, π) : A∆ → T
2g × ∆ is a real analytic isomorphism.

Just as in the case of Proposition 2.1, the Betti map is uniquely determined by prop-
erties (i) and (iii) up-to the action of GL2g(Z) if ∆ is connected. Composing with an
α ∈ GL2g(Z) does not change the rank. So by the discussion on the uniqueness above,
any map A∆ → T
2g satisfying the three properties listed in Proposition B.2 will be
called Betti map.

Proof. Our proof of Proposition B.2 follows the construction in [Gao20a, §3-§4]. We
divide it into several steps.
By [GN09, §2.1], A → S carries a polarization of type D = diag(d1, . . . , dg) for some
positive integers d1|d2| · · · |dg.
Case: Moduli space with level structure. Fix ℓ ≥ 3 with (ℓ, dg) = 1. We
start by proving Proposition B.2 for S = Ag,D,ℓ, the moduli space of abelian varieties
of dimension g polarized of type D with level-ℓ-structure. It is a ﬁne moduli space;
see [GN09, Theorem 2.3.1]. Let πuniv
D : Ag,D,ℓ → Ag,D,ℓ be the universal abelian variety.
The universal covering Hg → Aan
g,D,ℓ [GN09, Proposition 1.3.2], where Hg is the Siegel
upper half space, gives a family of abelian varieties AHg,D → Hg ﬁtting into the diagram

AHg,D := Ag,D,ℓ ×Ag,D,ℓ Hg //

  
 A
an
g,D,ℓ

πuniv
D
  
Hg // Aan
g,D,ℓ.

The family AHg,D → Hg is polarized of type D. For the universal covering u : Cg × Hg →
AHg,D and for each Z ∈ Hg, the kernel of u|Cg×{Z} is DZ
g+ZZ
g. Thus the map Cg ×Hg →
Rg × Rg × Hg → R2g, where the ﬁrst map is the inverse of (a, b, Z) ↦→ (Da + Zb, Z) and
the second map is the natural projection, descends to a real analytic map

b
univ : AHg,D → T
2g.

Now for each s0 ∈ Ag,D,ℓ(C), there exists a contractible, relatively compact, open neigh-
borhood ∆ of s0 in Aan
g,D,ℓ such that Ag,D,ℓ,∆ := (πuniv
D )−1(∆) can be identiﬁed with AHg,∆′
for some open subset ∆
′ of Hg. The composite b∆ : Ag,D,ℓ,∆ ∼= AHg,D,∆′ → T
2g clearly
satisﬁes the three properties listed in Proposition B.2. Thus b∆ is the desired Betti map
in this case.
 UNIFORMITY IN MORDELL–LANG FOR CURVES 42

Case: With level structure. Assume that A → S carries level-ℓ-structure for some
ℓ ≥ 3 with (ℓ, dg) = 1. As Ag,D,ℓ is a ﬁne moduli space there exists a Cartesian diagram

A ι //

π   
 ❴✤ Ag,D,ℓ

  
S ιS // Ag,D,ℓ.

Now let s0 ∈ S(C). Applying Proposition B.2 to the universal abelian variety Ag,D,ℓ →
Ag,D,ℓ and ιS(s0) ∈ Ag,D,ℓ(C), we obtain an open neighborhood ∆0 of ιS(s0) in Aan
g,D,ℓ
and a real analytic map b∆0 : Ag,∆0 → T
2g

satisfying the properties listed in Proposition B.2.
Now let ∆ = ι
−1
S (∆0). Then ∆ is an open neighborhood of s0 in San. Denote by
A∆ = π−1(∆) and deﬁne b∆ = b∆0 ◦ ι : A∆ → T
2g.

Then b∆ satisﬁes the properties listed in Proposition B.2 for A → S. Hence b∆ is our
desired Betti map.

Case: General case. Let s0 ∈ S(C) and ℓ ≥ 3 be a prime with (ℓ, dg) = 1.
Fix any irreducible component S0 of the kernel ker[ℓ] of [ℓ] : A → A. It is Zariski open
in ker[ℓ] as S is regular, so we consider it with its natural open subscheme structure.
Then S0 → ker[ℓ] is both a closed and open immersion. So S0 → S, the composition
with the ﬁnite ´etale morphism ker[ℓ] → S, is ﬁnite and ´etale. The upshot is that the base
change of A → S by S0 → S admits an ℓ-torsion section. After repeating this ﬁnitely
many times we obtain a ﬁnite and ´etale morphism ρ : S′ → S where S′ is irreducible
and such that A′ := A ×S S′ → S′ has level-ℓ-structure. Note that S′ is regular as
S is regular and regularity ascends along ´etale morphisms. Moreover, A′ → S′ is still
polarized of type D.
Let s′
0 ∈ ρ
−1(s0). Applying Proposition B.2 to A′ → S′ and s′
0 ∈ S′(C), we obtain an
open neighborhood ∆
′ of s′
0 in (S′)an and a map b∆′ : A′
∆′ → T
2g satisfying the properties
listed in Proposition B.2.
Let ∆ = ρ(∆
′). Up to shrinking ∆
′, we may assume that ρ|∆′ : ∆
′ → ∆ is a home-
omorphism and that ∆ is an open neighborhood of s0 in San. Thus A′
∆′ ∼= A∆. Now
deﬁne b∆ : A∆ → T
2g

to be the composite of the inverse of A′
∆′ ∼= A∆ and b∆′. Then b∆ is our desired Betti
map. □

Here is an easy property of the generic rank of the Betti map.

Lemma B.3. Let b∆ : A∆ → T
2g be a Betti map as in Proposition B.2. Let X be an
irreducible subvariety of A with X an ∩ A∆ ̸= ∅. Let U be a Zariski open dense subset of
X. Then

(B.2) max
x∈X sm(C)∩A∆ rankR(db∆|X sm,an)x = max
u∈U sm(C)∩A∆ rankR(db∆|U sm,an)u.

UNIFORMITY IN MORDELL–LANG FOR CURVES 43

Proof. The statement (B.2) is true on replacing “=” by “≥”, as X sm,an ⊇ U sm,an.
For the converse inequality we set maxx∈X sm,an∩A∆ rankR(db∆|X sm,an)x = r and pick x ∈
X sm,an ∩ A∆ satisfying rankR(db∆|X sm,an)x = r. Then there exists an open neighborhood
V of x in X sm,an such that rankR(db∆|X sm,an)u = r for all u ∈ V . But U sm(C) ∩ V ̸= ∅
since U sm ̸= ∅ is Zariski open in X and V is Zariski dense in X. Thus there exists a
u ∈ U sm(C) ∩ V . Then we must have rankR(db∆|U sm,an)u = r and the lemma follows. □

B.2. Non-degenerate subvariety and Theorem 1.6. We keep the notation as in
the beginning of this appendix.

Deﬁnition B.4. An irreducible subvariety X of A is said to be non-degenerate if there
exists an open non-empty subset ∆ of Ssm,an, with the Betti map b∆ : A∆ := π−1(∆) →
T
2g as in Proposition B.2, such that X sm,an ∩ A∆ ̸= ∅ and

max
x∈X sm(C)∩A∆ rankR(db∆|X sm,an)x = 2 dim X.

Now we are ready to prove Theorem B.1.

Proof of Theorem B.1. Let ℓ ≥ 3 be a prime. We will reduce the current theorem to
Theorem 1.6 by successively assuming, in addition to the hypothesis of Theorem B.1,
that
(i) X is Zariski closed in A,
(ii) π|X : X → S is dominant,
(iii) S is regular,
(iv) A → S is S-isogenous to an abelian scheme which carries a principal polarization,
(v) A → S carries a principal polarization,
(vi) A carries a level ℓ-structure, and
(vii) we have the same hypothesis as Theorem 1.6.
We will proceed the proof with six d´evissage steps. In d´evissage step n we will deduce
the theorem under the hypotheses (i),. . . ,(n − 1) from the theorem under the hypotheses
(i),. . . ,(n).
First d´evissage: reduction to the case where X is Zariski closed in A.
Let X denote the Zariski closure of X in A. Then X is a Zariski open dense subset
of X and dim X = dim X. Therefore, X is non-degenerate if X is non-degenerate. Now
if (B.1) holds true on a Zariski open dense subset U of X, then (B.1) clearly holds true
on U ∩ X, which is Zariski open and dense in X. Thus it suﬃces to prove (B.1) with X
replaced by X.
Second d´evissage: reduction to the case where π|X : X → S is dominant.
As X is non-degenerate, there exists a non-empty open subset ∆ of Ssm,an, with Betti
map b∆, such that rankR(db∆|X sm,an)x = 2 dim X for some x ∈ X sm(C) ∩ A∆.
Endow the Zariski closed set S′ = π(X) with the reduced induced subscheme structure
and set A′ = A ×S S′ = π−1(S′). Then X ×S S′ identiﬁes with X via the natural
projection A′ → A. Hence there exists a non-empty open subset ∆
′ of (S′)sm,an with
π(x) ∈ ∆
′ ⊆ ∆ and rankR(db∆′|X sm,an)x = 2 dim X.
Thus X is a non-degenerate subvariety of A′. On the other hand, the conclusion of
Theorem B.1 does not change with A → S replaced by A′ → S′, L replaced by L|A′

UNIFORMITY IN MORDELL–LANG FOR CURVES 44

and M replaced by M|S′, where S′ is the Zariski closure of S′ in S. Hence it suﬃces to
prove Theorem B.1 after these replacements and thus we may assume that X dominates
S.Third d´evissage: reduction to the case where S is regular.
Recall that Ssm is the regular locus of S. Now π|X : X → S is dominant, so X ′ =
X ∩ π−1(Ssm) is Zariski open and dense in X. Since X is non-degenerate it follows by
deﬁnition that X ′ is non-degenerate. Moreover, the conclusion of Theorem B.1 does not
change if we replace A → S by A′ = π−1(Ssm) → Ssm, L by L|A′, and X by X ′. Finally,
observe that X ′ is Zariski closed in A′ and π(X ′) = π(X) ∩ Sreg, so π|X ′ : X ′ → Sreg is
dominant.
Fourth d´evissage: reduction to the case where π : A → S is S-isogenous to an abelian
scheme which carries a principal polarization.
By [Mum74, §23, Corollary 1], each abelian variety over an algebraic closed ﬁeld is
isogenous to a principally polarized one. Applying this to the geometric generic ﬁber of
A → S, we obtain a quasi-ﬁnite ´etale dominant morphism ρ : S′ → S with S′ irreducible
and the following property: There exists a principally polarized A
′
0 that is isogenous
over Q(S′) to the generic ﬁber A
′ of A′ := A ×S S′ → S′. Up to replacing S′ by an open
dense subscheme, we may furthermore assume that A
′
0 extends to an abelian scheme
A′
0 → S′. Denote by ρA : A′ = A ×S S′ → A the natural projection; it is a quasi-ﬁnite
´etale dominant morphism.
As regularity ascends along ´etale morphisms and as S is regular we conclude that S′

is regular. Thus A′
0 → S′ carries a principal polarization by [Ray70, Th´eor`eme XI 1.4],
and the isogeny A
′
0 → A
′ extends to an S′-isogeny A′
0 → A′ by [Ray70, Lemme XI 1.15].
There is an irreducible component X ′ of ρ
−1
A (X) with dim X ′ = dim X. Then X ′ is
Zariski closed in A′, the image ρA(X ′) is Zariski dense in X, and thus X ′ dominates S′

(it even surjects to S′ since A′ → S′ is proper and X ′ is closed). We claim that X ′,
as a subvariety of A′, is non-degenerate. Indeed, ρA(X ′) contains a Zariski open dense
subset U of X. Since X is a non-degenerate subvariety of A, so is U by Lemma B.3.
So there exists an open subset ∆ of San with the Betti map b∆ : A∆ → T
2g such that
rankR(db∆|U an,sm)u = 2 dim U = 2 dim X for all u from a non-empty open subset of U an .
Take ∆
′ to be a connected component of ρ
−1(∆) such that X ′∩(π′)−1(∆
′) ̸= ∅. Set A′
∆′ =
(π′)−1(∆
′), and replace ∆ by ρ(∆
′). Note that ρ|∆′ : ∆
′ ∼= ∆ is then bianalytic after
possibly shrinking ∆
′ (and so is ρA : A′
∆′ ∼= A∆). Now b∆ ◦ ρA|A′
∆′ : A′
∆′ → T
2g satisﬁes
the three properties listed in Proposition B.2. So b∆ ◦ ρA|A′
∆′ is the Betti map, which we
denote for simplicity by b∆′; see below Proposition B.2. For u′ ∈ (ρA|A′
∆′ )−1(u) ∩ X ′an

and for suﬃciently general u, we have rankR(db∆′|X ′an,sm)u′ = 2 dim X. So X ′, as a
subvariety of the abelian scheme A′ over S′, is non-degenerate.
Now we have a non-degenerate subvariety X ′ of the abelian scheme π′ : A′ → S′. The
line bundle ρ
∗
AL on A′ is relatively ample. Suppose that M′ is an ample line bundle on
some compactiﬁcation S′ of S′.
Assume that Theorem B.1 holds for π′ : A′ → S′, ρ
∗
AL, M′, and X ′. Thus there exist
constants c′
1 > 0, c′
2 ≥ 0 and a Zariski open non-empty subset U ′ of X ′ with

ˆhA′,ρ∗
AL(P ′) ≥ c′
1hS′,M′(π′(P ′)) − c′
2 for all P ′ ∈ U ′(Q).

Denote by P = ρA(P ′). By the Height Machine we have ˆhA′,ρ∗
AL(P ′) = ˆhA,L(P ).

UNIFORMITY IN MORDELL–LANG FOR CURVES 45

By [Sil11, Lemma 4] applied to ρ : S′ → S and the line bundles M′ and M, there
exist c′ = c′(ρ, M′, M) > 0 and c′′ = c′′(ρ, M′, M) ≥ 0 such that hS′,M′(π′(P ′)) ≥
c′hS,M(ρ(π′(P ′))) − c′′ = c′hS,M(π(P )) − c′′ for all P ′ ∈ A′(Q). Hence the height in-
equality above implies
ˆhA,L(P ) ≥ c′
1c′hS,M(π(P )) − (c′
1c′′ + c′
2) for all P ∈ ρA(U ′)(Q).

Now that ρA(U ′) contains a Zariski open non-empty (hence dense) subset U of X by
Chevalley’s Theorem. Thus Theorem B.1 also holds true for π : A → S, L, M, and X.
In summary, we have shown that it suﬃces to prove Theorem B.1 for π′ : A′ → S′,
ρ
∗
AL, M′ and X ′. Thus we are reduced to the case where the generic ﬁber of A → S is
isogenous to a principally polarized abelian variety.
Fifth d´evissage: reduction to the case where π : A → S carries a principal polarization.
From the previous d´evissage, there exists a principally polarized abelian scheme
π0 : A0 → S with an S-isogeny λ : A0 → A. Note that λ is a ﬁnite ´etale mor-
phism. The line bundle λ∗L on A0 is relatively ample. By the Height Machine we
have ˆhA0,λ∗L(P ′) = ˆhA,L(λ(P ′)) for all P ′ ∈ A0(Q).
There is an irreducible component X0 of λ−1(X) with dim X0 = dim X. Then X0 is
Zariski closed in A0 and thus X0 dominates S (it even surjects to S since X = λ(X0)).
We claim that X0, as a subvariety of A0, is non-degenerate. Assume this. Then it suﬃces
to prove the height inequality (B.1) with A → S replaced by A0 → S, X replaced by
X0, and L replaced by λ∗L.
It remains to prove that X0 is a non-degenerate subvariety of A0. To do this, we need
some preparation on Betti maps. Let ∆ be an open subset of San with the Betti map
b∆ : A∆ → T
2g. Set A0,∆ = π−1
0 (∆), and denote by λ∆ the restriction of λ : A0 → A to
A0,∆. Up to shrinking ∆ we have a Betti map b0,∆ : A0,∆ → T
2g. By property (iii) of
Proposition B.2, we have two real analytic isomorphisms (b0,∆, π0) : A0,∆ ∼= T
2g × ∆ and
(b∆, π) : A∆ ∼= T
2g × ∆. Thus there exists a real analytic map λ′ : T
2g × ∆ → T
2g × ∆
such that the following diagram commutes

A0,∆
(b0,∆,π0)

∼ //

λ∆   
 T
2g × ∆

λ′
  
A∆ (b∆,π)
∼ // T
2g × ∆.

As λ is a ﬁnite map, (λ′)−1(r) is a ﬁnite set for each r ∈ T
2g ×∆. As λ is an S-morphism,
for each s ∈ ∆ we have λ′(T
2g × {s}) ⊆ T
2g × {s}.
By property (i) of Proposition B.2, for each s ∈ ∆ the restriction λ′|T2g ×{s} is a group
homomorphism T
2g → T
2g. Thus ker(λ′|T2g×{s}) is a ﬁnite, hence discrete, subgroup
of T
2g. In particular, ker(λ′|T2g×{s}) is locally constant. Up to shrinking ∆, we may
assume ker(λ′|T2g ×{s}) = H for each s ∈ ∆. Set λT : T
2g → T
2g the quotient by the ﬁnite
subgroup H. Then the diagram above induces a commutative diagram

(B.3) A0,∆ b0,∆ //

λ∆   
 T
2g

λT
  
A∆ b∆ // T
2g.

UNIFORMITY IN MORDELL–LANG FOR CURVES 46

Note that λT is a local homeomorphism.
Now we turn to proving that X0 is non-degenerate in A0. Indeed, as X is a non-
degenerate subvariety of A, there exists an open subset ∆ of San with the Betti map
b∆ : A∆ → T
2g such that rankR(db∆|X an,sm)x = 2 dim X for all x from a non-empty
open subset of X an. For x0 ∈ λ−1(x) ∩ X an
0 and for suﬃciently general x, we have
rankR(d(λT ◦ b0,∆)|X an,sm
0 )x0 = 2 dim X = 2 dim X0. But λT is a local homeomorphism,
so rankR(db0,∆|X an,sm
0 )x0 = 2 dim X0. Thus X0 is non-degenerate.
Sixth d´evissage: reduction to the case where A/S carries level ℓ structure.
As in the treatment of the general case in the proof of Proposition B.2 there exists
a ﬁnite and ´etale morphism S′ → S where S′ is regular and irreducible such that
A′ := A ×S S′ carries level ℓ-structure.
Denote by ρA : A′ → A the natural projection. By a similar argument as the fourth
d´evissage step, it suﬃces to prove the height inequality (B.1) with A → S replaced by
A′ → S′, X replaced by an irreducible component of ρ
−1
A (X) with dim X ′ = dim X, and
L replaced by ρ
∗
AL, and M replaced by an ample line bundle on some compactiﬁcation
of S′. As in the fourth d´evissage X ′ dominates S′. Finally, A′/S′ still carries a principal
polarization.
Seventh d´evissage: reduction to Theorem 1.6.
It remains to prove the height inequality (B.1) with the extra hypotheses (i) - (v) listed
above using Theorem 1.6. In this theorem we assumed in addition that the ﬁberwise
N´eron–Tate height on A(Q) is induced by a closed immersion A → Pn
Q × S satisfying
the second and third bullet at the beginning of §3 and that the height on S(Q) is
the restriction of the absolute logarthmic Weil height coming from a closed immersion
S → Pm
Q .
A basis of the global sections of the line bundle M⊗p, for some p large enough, gives
rise to a closed immersion S ⊆ Pm
Q . This gives the ﬁrst bullet point at the beginning of
§3. Note that the Weil height h on Pm
Q (Q) restricted to S(Q) via this immersion diﬀers
from phS,M by a bounded function.
For the line bundle L on A, which is ample relative over S, we have that L⊗4 is
relatively very ample on A/S. Thus by [Gro61, Proposition 4.4.10.(ii) and Proposi-
tion 4.1.4], there is a closed immersion A → Pn
S = Pn × S given by global sections of
L⊗4 ⊗ π∗M⊗q for some large q. When restricted to the generic ﬁber A of A → S, we get
a closed immersion A → Pn
k(S) which arises from a basis of the global sections of L
⊗4,
where L is the restriction of L over the generic ﬁber A. Moreover L is ample since L is
relatively ample, and L is symmetric since [−1]∗L = L. Thus we also have the second
and third bullet points at the beginning of §3.
Note that the height function ˆhA deﬁned in (3.2) is then

ˆhA : A(Q) → [0, ∞), P → ˆhAs,L⊗4
s (P )

where s = π(P ). So ˆhA,L = (1/4)ˆhA.
The full hypothesis of Theorem 1.6 is now satisﬁed for A and X, e.g., (Hyp) is just
(iv) and (v). We get constants c1 > 0 and c2 and a Zariski open dense subset U of X
such that ˆhA(P ) ≥ c1h(π(P )) − c2 for all P ∈ U(Q).

UNIFORMITY IN MORDELL–LANG FOR CURVES 47

Thus (B.1) holds true with c1 replaced by (c1p)/4 and c2 replaced by c2/4+OS(1), where
OS(1) is a bounded function on S(Q). So we are done. □

References

[ACG11] E. Arbarello, M. Cornalba, and P. Griﬃths. Geometry of Algebraic Curves, II (with a con-
tribution by J. Harris), volume 268 of Grundlehren der mathematischen Wissenschaften.
Springer-Verlag, Berlin, 2011.
[ACZ20] Yves Andr´e, Pietro Corvaja, and Umberto Zannier. The Betti map associated to a section
of an abelian scheme (with an appendix by Z. Gao). Inv. Math., 222:161–202, 2020.
[Alp18] L. Alpoge. The average number of rational points on genus two curves is bounded.
arXiv:1804.05859, 2018.
[Alp20] L. Alpoge. Points on Curves. PhD thesis, Princeton University, 2020.
[BG06] E. Bombieri and W. Gubler. Heights in Diophantine Geometry. Cambridge University Press,
2006.
[BGS94] J.-B. Bost, H. Gillet, and C. Soul´e. Heights of projective varieties and positive Green forms.
J. Amer. Math. Soc., 7(2):903–1027, 1994.
[BLR90] S. Bosch, W. L¨utkebohmert, and M. Raynaud. N´eron models, volume 21 of Ergebnisse der
Mathematik und ihrer Grenzgebiete (3). Springer-Verlag, Berlin, 1990.
[Bom90] E. Bombieri. The Mordell conjecture revisited. Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4),
17(4):615–640, 1990.
[CGHX21] S. Cantat, Z. Gao, P. Habegger, and J. Xie. The geometric Bogomolov conjecture. Duke
Math. J., 170(2):247–277, 2021.
[Cha41] C. Chabauty. Sur les points rationnels des courbes alg´ebriques de genre sup´erieur `a l’unit´e.
C. R. Acad. Sci. Paris, 212:882–885, 1941.
[Col85] R. .F. Coleman. Eﬀective Chabauty. Duke Math. J., 52(3):765–770, 1985.
[CVV17] S. Checcoli, F. Veneziano, and E. Viada. On the explicit torsion anomalous conjecture.
Trans. Amer. Math. Soc., 369(9):6465–6491, 2017.
[dD97] T. de Diego. Points rationnels sur les familles de courbes de genre au moins 2. J. Number
Theory, 67(1):85–114, 1997.
[Dem12] J.P. Demailly. Complex analytic and diﬀerential geometry. 2012. Available at
https://www-fourier.ujf-grenoble.fr/~demailly/manuscripts/agbook.pdf.
[DGH19] V. Dimitrov, Z. Gao, and P. Habegger. Uniform bound for the number of rational points on a
pencil of curves. Int. Math. Res. Not. IMRN, (rnz248):https://doi.org/10.1093/imrn/rnz248,
2019.
[DKY20] L. DeMarco, H. Krieger, and H. Ye. Uniform Manin-Mumford for a family of genus 2 curves.
Ann. of Math., 191:949–1001, 2020.
[DM69] P. Deligne and D. Mumford. The irreducibility of the space of curves of given genus. Inst.
Hautes ´Etudes Sci. Publ. Math., (36):75–109, 1969.
[DNP07] S. David, M. Nakamaye, and P. Philippon. Bornes uniformes pour le nombre de points
rationnels de certaines courbes. In Diophantine geometry, volume 4 of CRM Series, pages
143–164. Ed. Norm., Pisa, 2007.
[DP02] S. David and P. Philippon. Minorations des hauteurs normalis´ees des sous-vari´et´es de
vari´et´es abeliennes. II. Comment. Math. Helv., 77(4):639–700, 2002.
[DP07] S. David and P. Philippon. Minorations des hauteurs normalis´ees des sous-vari´et´es des puis-
sances des courbes elliptiques. Int. Math. Res. Pap. IMRP, (3):Art. ID rpm006, 113, 2007.
[Fal83] G. Faltings. Endlichkeitss¨atze f¨ur abelsche Variet¨aten ¨uber Zahlk¨orpern. Invent. Math.,
73:349–366, 1983.
[Fal91] G. Faltings. Diophantine approximation on abelian varieties. Ann. of Math. (2), 133(3):549–
576, 1991.
[FC90] G. Faltings and C.-L. Chai. Degeneration of abelian varieties, volume 22 of Ergebnisse der
Mathematik und ihrer Grenzgebiete (3) [Results in Mathematics and Related Areas (3)].
Springer-Verlag, Berlin, 1990. With an appendix by David Mumford.

UNIFORMITY IN MORDELL–LANG FOR CURVES 48

[Ful98] W. Fulton. Intersection theory, volume 2 of Ergebnisse der Mathematik und ihrer Grenzge-
biete. 3. Folge. A Series of Modern Surveys in Mathematics [Results in Mathematics and
Related Areas. 3rd Series. A Series of Modern Surveys in Mathematics]. Springer-Verlag,
Berlin, second edition, 1998.
[Gao20a] Z. Gao. Generic rank of Betti map and unlikely intersections. Compos. Math., 156(12):2469–
2509, 2020.
[Gao20b] Z. Gao. Mixed Ax-Schanuel for the universal abelian varieties and some applications. Com-
pos. Math., 156(11):2263–2297, 2020.
[GH19] Z. Gao and P. Habegger. Heights in Families of Abelian Varieties and the Geometric Bogo-
molov Conjecture. Ann. of Math., 189(2):527–604, 2019.
[GN09] A. Genestier and B.C. Ngˆo. Lecture on Shimura varieties. In Autour de motifs, Ecole d’´et´e
Franco-Asiatique de G´eom´etrie Alg´ebrique et de Th´eorie des Nombres/Asian-French Sum-
mer School on Algebraic Geometry and Number Theory. Vol. I, pages 187–236. Panor.
Synth`ese 29, Soc. Math. France, 2009.
[Gro61] A. Grothendieck. ´El´ements de g´eom´etrie alg´ebrique. II. ´Etude globale ´el´ementaire de
quelques classes de morphismes. Inst. Hautes ´Etudes Sci. Publ. Math., (8), 1961.
[Gro67] A. Grothendieck. ´El´ements de g´eom´etrie alg´ebrique. IV. ´Etude locale des sch´emas et des
morphismes de sch´emas I-IV. Inst. Hautes ´Etudes Sci. Publ. Math., (20,24,28,32), 1964–
1967.
[GW10] U. G¨ortz and T. Wedhorn. Algebraic geometry I. Advanced Lectures in Mathematics. Vieweg
+ Teubner, Wiesbaden, 2010. Schemes with examples and exercises.
[Hab09] P. Habegger. On the bounded height conjecture. Int. Math. Res. Not. IMRN, (5):860–886,
2009.
[Hab13] P. Habegger. Special Points on Fibered Powers of Elliptic Surfaces. J.Reine Angew. Math.,
685:143–179, 2013.
[HP16] P. Habegger and J. Pila. O-minimality and certain atypical intersections. Ann. Sci. ´Ecole
Norm. Sup., 49:813–858, 2016.
[Hur92] A. Hurwitz. ¨Uber algebraische Gebilde mit eindeutigen Transformationen in sich. Math.
Ann., 41(3):403–442, 1892.
[KRZB16] E. Katz, J. Rabinoﬀ, and D. Zureick-Brown. Uniform bounds for the number of rational
points on curves of small Mordell-Weil rank. Duke Math. J., 165(16):3189–3240, 2016.
[K¨uh20] L. K¨uhne. The Bounded Height Conjecture for Semiabelian Varieties. Compos. Math,
156:1405–1456, 2020.
[Lan65] S. Lang. Division points on curves. Ann. Mat. Pura Appl. (4), 70:229–234, 1965.
[Lan78] S. Lang. Elliptic curves: Diophantine analysis, volume 231 of Grundlehren der Mathematis-
chen Wissenschaften [Fundamental Principles of Mathematical Sciences]. Springer-Verlag,
Berlin-New York, 1978.
[Laz04] R. Lazarsfeld. Positivity in Algebraic Geometry I. Springer, 2004.
[Lel57] P. Lelong. Int´egration sur un ensemble analytique complexe. Bull. Soc. Math. France,
85:239–262, 1957.
[Maz86] B. Mazur. Arithmetic on curves. Bulletin of the American Mathematical Society, 14(2):207–
259, 1986.
[Maz00] B. Mazur. Abelian varieties and the Mordell-Lang conjecture. In Model theory, algebra, and
geometry, volume 39 of Math. Sci. Res. Inst. Publ., pages 199–227. Cambridge Univ. Press,
Cambridge, 2000.
[MFK94] D. Mumford, J. Fogarty, and F. Kirwan. Geometric invariant theory, volume 34 of Ergebnisse
der Mathematik und ihrer Grenzgebiete (2) [Results in Mathematics and Related Areas (2)].
Springer-Verlag, Berlin, third edition, 1994.
[Mok91] N. Mok. Aspects of K¨ahler geometry on arithmetic varieties. In Several complex variables
and complex geometry, Part 2 (Santa Cruz, CA, 1989), volume 52 of Proc. Sympos. Pure
Math., pages 335–396. Amer. Math. Soc., Providence, RI, 1991.
[Mum70] D. Mumford. Varieties deﬁned by quadratic equations. In Questions on Algebraic Varieties
(C.I.M.E., III Ciclo, Varenna, 1969), pages 29–100. Edizioni Cremonese, Rome, 1970.

UNIFORMITY IN MORDELL–LANG FOR CURVES 49

[Mum74] D. Mumford. Abelian Varieties, 2nd ed. Oxford University Press, London, 1974.
[OS80] F. Oort and J. Steenbrink. The local Torelli problem for algebraic curves. In Journ´ees
de G´eometrie Alg´ebrique d’Angers, Juillet 1979/Algebraic Geometry, Angers, 1979, pages
157–204. Sijthoﬀ & Noordhoﬀ, Alphen aan den Rijn—Germantown, Md., 1980.
[Paz12] F. Pazuki. Theta height and Faltings height. Bull. Soc. Math. France, 140(1):19–49, 2012.
[Phi86] P. Philippon. Lemmes de z´eros dans les groupes alg´ebriques commutatifs. Bull. Soc. Math.
France, 114:355–383, 1986.
[Phi95] P. Philippon. Sur des hauteurs alternatives III. J. Math. Pures Appl., 74:345–365, 1995.
[Pin89] R. Pink. Arithmetical compactiﬁcation of mixed Shimura varieties. PhD thesis, Bonner
Mathematische Schriften, 1989.
[Pin05a] R. Pink. A combination of the conjectures of Mordell-Lang and Andr´e-Oort. In Geomet-
ric methods in algebra and number theory, volume 235 of Progr. Math., pages 251–282.
Birk¨auser, 2005.
[Pin05b] R. Pink. A Common Generalization of the Conjectures of Andr´e-Oort, Manin-Mumford,
and Mordell-Lang. Preprint, page 13pp, 2005.
[Ray70] M. Raynaud. Faisceaux amples sur les sch´emas en groupes et les espaces homog`enes. Lecture
Notes in Mathematics, Vol. 119. Springer-Verlag, Berlin-New York, 1970.
[Ray83] M. Raynaud. Courbes sur une vari´et´e ab´elienne et points de torsion. Invent. Math.,
71(1):207–233, 1983.
[R´em00a] G. R´emond. D´ecompte dans une conjecture de Lang. Invent. Math., 142(3):513–545, 2000.
[R´em00b] G. R´emond. In´egalit´e de Vojta en dimension sup´erieure. Ann. Scuola Norm. Sup. Pisa Cl.
Sci. (4), 29(1):101–151, 2000.
[Sil83] J. H. Silverman. Heights and the specialization map for families of abelian varieties. J. Reine
Angew. Math., 342:197–211, 1983.
[Sil93] J. H. Silverman. A uniform bound for rational points on twists of a given curve. J. London
Math. Soc. (2), 47(3):385–394, 1993.
[Sil11] J. H. Silverman. Height estimates for equidimensional dominant rational maps. J. Ramanu-
jan Math. Soc., 26(2):145–163, 2011.
[Sto19] M. Stoll. Uniform bounds for the number of rational points on hyperelliptic curves of small
Mordell-Weil rank. J. Eur. Math. Soc. (JEMS), 21(3):923–956, 2019.
[Voi02] C. Voisin. Hodge theory and complex algebraic geometry. I, volume 76 of Cambridge Studies
in Advanced Mathematics. Cambridge University Press, Cambridge, English edition, 2002.
[Voj91] P. Vojta. Siegel’s theorem in the compact case. Ann. of Math. (2), 133(3):509–548, 1991.
[Wal87] M. Waldschmidt. Nombres transcendants et groupes alg´ebriques. Ast´erisque, (69-70):218,
1987. With appendices by Daniel Bertrand and Jean-Pierre Serre.
[Zan12] U. Zannier. Some problems of unlikely intersections in arithmetic and geometry, volume 181
of Annals of Mathematics Studies. Princeton University Press, Princeton, NJ, 2012. With
appendixes by David Masser.
[Zha98] S. Zhang. Equidistribution of small points on abelian varieties. Ann. of Math. (2),
147(1):159–165, 1998.

Department of Mathematics, University of Toronto, 40 St. George Street, Toronto,
Ontario, Canada M5S 2E4
Email address: dimitrov@math.toronto.edu

CNRS, IMJ-PRG, 4 place Jussieu, 75005 Paris, France
Email address: ziyang.gao@imj-prg.fr

Department of Mathematics and Computer Science, University of Basel, Spiegel-
gasse 1, 4051 Basel, Switzerland
Email address: philipp.habegger@unibas.ch
