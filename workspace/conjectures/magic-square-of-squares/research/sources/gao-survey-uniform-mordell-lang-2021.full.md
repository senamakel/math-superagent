<!-- source: https://arxiv.org/pdf/2104.03431 | converted from PDF -->

arXiv:2104.03431v5  [math.NT]  26 Dec 2021
RECENT DEVELOPMENTS OF THE UNIFORM MORDELL–LANG
CONJECTURE

ZIYANG GAO

Abstract. This expository survey is based on my online talk at the ICCM 2020. It aims to
sketch key steps of the recent proof of the uniform Mordell–Lang conjecture for curves embedded
into Jacobians (a question of Mazur). The full version of this conjecture is proved by combining
Dimitrov–Gao–Habegger [DGH21] and K¨uhne [K¨uh21a]. We include in this survey a detailed
proof on how to combine these two results, which was implicitly done in [DGH20] but not
explicitly written in existing literature. At the end of the survey we state some future aspects.

Contents

1. Introduction 1
2. The Height Machine 6
3. Vojta’s method 8
4. Basic setup and Statement of the New Gap Principle 10
5. Betti map and Betti form 12
6. Non-degenerate subvarieties 15
7. The height inequality and its application 17
8. Equidistribution on non-degenerate subvarieties and its application 20
9. Proof of the New Gap Principle and proof of Uniform Mordell–Lang for curves 24
10. Further aspects 27
References 32

1. Introduction

Let F be a ﬁeld of characteristic 0. A smooth curve C deﬁned over F is a geometrically
irreducible, smooth, projective curve deﬁned over F . Let Jac(C) be the Jacobian of C.
The goal of this survey is to report the recent development of the following theorem, known
as the Uniform Mordell–Lang Conjecture for curves embedded into Jacobians. It is a question
posed by Mazur [Maz86, top of pp.234].

Theorem 1.1 (Dimitrov–Gao–Habegger + K¨uhne). Let g ≥ 2 be an integer. Then there exists
a constant c(g) ≥ 1 with the following property. Let C be a smooth curve of genus g deﬁned over
F , let P0 ∈ C(F ), and let Γ be a subgroup of Jac(C)(F ) of ﬁnite rank ρ. Then

(1.1) #(C(F ) − P0) ∩ Γ ≤ c(g)
1+ρ

where C − P0 is viewed as a curve in Jac(C) via the Abel–Jacobi map based at P0.

A specialization argument using Masser’s result [Mas89] reduces this theorem to F = Q;
see [DGH20, Lem.3.1]. Then Theorem 1.1 is proved by a combination of the recent works
of Dimitrov–Gao–Habegger [DGH21] and K¨uhne [K¨uh21a]. More precisely, Dimitrov–Gao–
Habegger’s [DGH21, Thm.1.2] proves Theorem 1.1 for curves C whose modular height is larger

2000 Mathematics Subject Classiﬁcation. 11G10, 11G50, 14G25, 14K15.

1
 2

than a number δ = δ(g) depending only on the genus g, and it can be complemented by
K¨uhne’s [K¨uh21a, Thm.3] because [K¨uh21a, Thm.3] can handle curves with small modular
height.
The way to combine these results to obtain Theorem 1.1 is not immediate; it was implicitly
done in [DGH20, §2.3 and 2.4] but did not appear explicitly in literature. In this survey, we
include this argument in §9.

There are already some excellent surveys on the topic of the Mordell–Lang Conjecture, for
example [Hin98] and [Maz00], where aspects on function ﬁelds can also be found. The current
survey focuses on the uniformity aspect.

Here is a ﬁrst digest on the conclusion of Theorem 1.1 and its consequences, including two
particularly interesting cases (rational points and algebraic torsion points). In what follows
g ≥ 2.
(1) Rational points. A particularly important case of Theorem 1.1 is when F is a number
ﬁeld and Γ = Jac(C)(F ). In this case, the Mordell–Weil Theorem says that Jac(C)(F )
is a ﬁnitely generated abelian group. Thus (1.1) becomes a bound on the number of
rational points #C(F ) ≤ c(g)1+rkJac(C)(F ). This improves [DGH21, Thm.1.1], which
proves #C(F ) ≤ c(g, [F : Q])1+rkJac(C)(F ). However, #C(F ) must depend on [F : Q] in
some way; in the stronger bound this dependence is encoded in rkJac(C)(F ).
In the case of rational points, the most ambitious bound is that #C(F ) is bounded
above solely in terms of g and [F : Q]. Caporaso–Harris–Mazur and Pacelli [CHM97,
Pac97] proved this bound assuming a widely open conjecture of Lang.
[1] Techniques
developed by Abramovich in [Abr95] were used in Pacelli’s work.
(2) Arbitrary ﬁnite rank subgroup. If we pass from rational points to an arbitrary Γ
and proceed with quasi-orthogonality (Vojta’s method), then the bound (1.1) is optimal.
Indeed, #(C(F ) − P0) ∩ Γ must depend on g and ρ = rkΓ. Moreover, the exponent 1 + ρ
is optimal: While it is clear that the exponent should be at least ρ = rkΓ for a general
Γ, we need the extra value 1 to handle torsion points; see the next case.
(3) Algebraic torsion points. Another particularly interesting case of Theorem 1.1 is
when F = C and Γ = Jac(C)tor. In this case (1.1) becomes #(C(C) − P0) ∩ Jac(C)tor ≤
c(g), the Uniform Manin–Mumford Conjecture for curves in their Jacobians. In this
case, [K¨uh21a, Thm.3] suﬃces to conclude.
[K¨uh21a, Thm.3] is sometimes known as the Uniform Bogomolov Conjecture for
curves embedded into Jacobians and is of independent interest. It can be deduced from
the Relative Bogomolov Conjecture [DGH20, Conj.1.1] which is still open. We will have a
discussion on this in §10.1. In this survey, the Uniform Bogomolov Conjecture is merged
to be part of the New Gap Principle, Theorem 4.1; the latter is the major new input
which, based on Vojta’s proof of the Mordell Conjecture and classical results of many
others, leads to Theorem 1.1; see §1.2 and §1.3.

Let us step back and give a historical point of view. The problem is divided into several
grades.
- Finiteness. Faltings [Fal83] proved the celebrated Mordell conjecture, which claims
that a smooth curve of genus g ≥ 2 deﬁned over a number ﬁeld has only ﬁnitely many
rational points. This is precisely the ﬁniteness of C(F ), the rational point problem
mentioned in (1) above. A new proof was later on given by Vojta [Voj91], which was
simpliﬁed by Faltings [Fal91] and further simpliﬁed by Bombieri [Bom90]. Notice that

[1]When the number ﬁeld F is ﬁxed, [CHM97, CHM21] proved more: Assuming the widely open Strong Lang
Conjecture, the cardinality #C(F ) is bounded above solely in terms of g except for ﬁnitely many F -isomorphic
classes of curves C of genus g ≥ 2.
 3

up to replacing F by a ﬁnite extension, this implies the ﬁniteness of (C(Q) − P0) ∩ Γ
for Γ an arbitrary ﬁnitely generated subgroup. Raynaud [Ray83a] explained how to pass
from ﬁnitely generated subgroups to ﬁnite rank subgroups.
As for algebraic torsion points as mentioned in (3) above, Raynaud [Ray83b] proved
the Manin–Mumford conjecture, claiming the ﬁniteness of (C(C) − P0) ∩ Jac(C)tor.
Faltings [Fal91] also further generalized Vojta’s proof to allow high dimensional sub-
varieties of an abelian variety, and Hindry [Hin88] proved how to pass from ﬁnitely
generated subgroups to ﬁnite rank subgroups in this more general situation. Thus the
Mordell–Lang Conjecture for abelian varieties was proved by [Fal91] and [Hin88].
- Bounds. Bombieri’s proof [Bom90] was the ﬁrst to give eﬀective bounds for the number
of rational points. Silverman [Sil93] proved a bound on the number of rational points
when C ranges over twists of a given smooth curve. The Bogomolov conjecture, proved
by Ullmo [Ull98] and S. Zhang [Zha98a], allows to bound #(C(Q) − P0) ∩ Γ for arbitrary
Γ. The bound thus obtained depends on C and is not explicit.
An explicit upper bound of #(C(Q)−P0)∩Γ was later on proved by R´emond [R´em00a].
Apart from g and rk(Γ), R´emond’s bound depends also on a suitable height of Jac(C)
and the degree of the deﬁnition ﬁeld of C. Setting P0 ∈ C(F ) and Γ = Jac(C)(F )
then leads to a bound of the number for the rational point problem mentioned in (1)
above. Based on this result, a more explicit bound for the number of rational points was
obtained for a particular kind of curves [R´em10]. R´emond’s bound holds true for high
dimensional subvarieties of abelian varieties.
- Uniform bounds. Let us turn to previous results towards Theorem 1.1. In the direction
of rational points, i.e. the bound #C(F ) ≤ c(g, [F : Q])1+rkJac(C)(F ) for F a number
ﬁeld mentioned in (1) above. Based on the method of Vojta, David–Philippon [DP07]
proved this bound if Jac(C) is contained in a power of an elliptic curve, and David–
Nakamaye–Philippon proved this bound for some families of curves [DNP07]. More
recently, Alpoge [Alp18] [Alp20, Chap.5] proved that the average number of rational
points on a curve of genus 2 with a marked Weierstrass point is bounded. Pazuki [Paz15,
Paz17] showed that a suitable version of the far-reaching Lang–Silverman conjecture
implies the desired bound; some unconditional results are obtained in some cases [Paz15,
Cor.1.10]. The Chabauty–Coleman approach [Cha41, Col85] yields estimates under an
additional hypothesis on the rank of Mordell–Weil group. For example, if Jac(C)(F )
has rank at most g − 3, Stoll [Sto19] showed that #C(F ) is bounded solely in terms of
[F : Q] and g if C is hyperelliptic; Katz–Rabinoﬀ–Zureick-Brown [KRZB16] later, under
the same rank hypothesis, removed the hyperelliptic hypothesis.
In the direction of torsion points, i.e. F = C and Γ = Jac(C)tor mentioned in (3),
the desired bound #(C(C) − P0) ∩ Jac(C)tor ≤ c(g) was proved by DeMarco–Krieger–
Ye [DKY20] for any genus 2 curve admitting a degree-two map to an elliptic curve
when the Abel–Jacobi map is based at a Weierstrass point. Katz–Rabinoﬀ–Zureick-
Brown [KRZB16] proved a weaker bound (in the form of [DGH21, Thm.1.4]) assuming
that C has good reduction at a small prime. Over function ﬁelds [2] and if C is not
isotrivial, Looper–Silverman–Wilms [LSW21] proved an explicit bound c(g) = 112g2 +
240g + 380; Wilms’s result remains true over positive characteristic.
Stoll [Sto19] showed that a far-reaching conjecture of Pink [Pin05] on unlikely inter-
sections implies Theorem 1.1.
- Eﬀective Mordell. This is not directly related to the topic of the current survey. As
a question it is fundamental but currently out of reach.

[2]Namely, F is an algebraic closure of k(B), where k is an algebraically closed ﬁeld and B is a smooth curve
deﬁned over k.
 4

For the rational point problem as mentioned in (1), the eﬀective Mordell conjecture is
to ﬁnd an explicit bound for the height of P ∈ C(F ) which is linear in terms of a suitable
height of C; see [HS00, Conj.F.4.3.2]. Little is known for this conjecture. In spirit of
the Manin-Demjanenko method [Ser13, §5.2], Checcoli, Veneziano, and Viada [CVV17,
CVV19, VV20] have some results on this. There are also p-adic approaches (Chabauty–
Coleman–Kim, Lawrence–Venkatesh) to this question, for which we refer to the survey
[BBB+21].

1.1. Key new ingredients. The proof of Theorem 1.1 is based on Vojta’s approach to prove
the Mordell conjecture [Voj91]. A key new notion to prove Theorem 1.1 is the non-degenerate
subvarieties of any given abelian scheme over Q; see §6. This notion was introduced by Habegger
in [Hab13], and played an important role in the proof of the Geometric Bogomolov Conjecture
over characteristic 0 by Gao–Habegger and Cantat–Gao–Habegger–Xie [GH19, CGHX21].
In the course of the proof, the following aspects on non-degenerate subvarieties have been
developed.
(i) The geometric criterion of non-degenerate subvarieties and some related constructions.
(ii) A height inequality on any given non-degenerate subvariety.
(iii) An equidistribution result on any given non-degenerate subvariety.
Part (i) was done by Gao in [Gao20a], part (ii) was done by Dimitrov–Gao–Habegger in [DGH21],
and part (iii) was done by K¨uhne in [K¨uh21a]. For 1-parameter families of abelian varieties, (i)
and (ii) were proved in [Hab13] for ﬁbered power of elliptic surfaces and in [GH19] in its full
generality.
Dimitrov–Gao–Habegger’s [DGH21, Thm.1.2] uses (i) and (ii). The blueprint was laid down
in [DGH19], where we used [GH19] to prove [DGH21, Thm.1.2] for 1-parameter families.
K¨uhne’s [K¨uh21a, Thm.3] uses (i) and (iii), and implicitly part (ii) as it was used in K¨uhne’s
proof of the equidistribution result.
More recently, Yuan–Zhang extended the deﬁnition of non-degenerate subvarieties to polarized
dynamical systems [YZ21, §6.2.2]. They proved a more general height inequality and a more
general equidistribution theorem [YZ21, Thm.6.5 and Thm.6.7]. Their proof uses deep theory
of adelic line bundles, arithmetic intersection theory and arithmetic volumes. Notice that in the
case of abelian schemes, this leads to new proofs of (ii) and (iii) above.

1.2. Quick summary of Vojta’s method. Before moving on, let us take a step back to
brieﬂy recall Vojta’s method. Let Ag,1 be the coarse moduli space of principally polarized
abelian varieties of dimension g. Fix an immersion ι : Ag,1 → Pm
Q . Let h : Pm
Q → R be the
absolute logarithmic Weil height. In what follows, we will identify Ag,1 with its image under ι.
Let ˆh : Jac(C)(Q) → [0, ∞) denote the N´eron–Tate height attached to a symmetric and ample
line bundle on Jac(C). We divide C(Q) ∩ Γ into two parts:

• Small points {
P ∈ C(Q) ∩ Γ : ˆh(P ) ≤ B(C)
}
;

• Large points {P ∈ C(Q) ∩ Γ : ˆh(P ) > B(C)
}

where B(C) is allowed to depend on a suitable height of C. Denote by [Jac(C)] the point in
Pm(Q) induced by Jac(C) and ι. It turns out that we can take B(C) = c0 max{1, h([Jac(C)])}
for some c0 = c0(g) > 0. The constant c0 is chosen in a way that accommodates both the
Mumford inequality and the Vojta inequality. Combining these two inequalities yields an upper
bound on the number of large points by c1(g)1+ρ, see for example Vojta’s [Voj91, Thm.6.1] in
the important case where Γ is the group of points of Jac(C) rational over a number ﬁeld or
more generally in the work of David–Philippon [DP02,DP07] and R´emond [R´em00a]. Moreover,
in the case for rational points, de Diego [dD97] proved that the number of large points is at
most c(g)7ρ, where c(g) > 0 depends only on g; the value 7 had already appeared in Bombieri’s

5

work [Bom90]. Recently, Alpoge [Alp18] [Alp20, Thm.6.1.1] improved 7 to 1.872 and, for g large
enough, even to 1.311.
David–Philippon [DP02, DP07] also showed that an appropriate lower bound on the essential
minimum of subvarieties of Jac(C) yields a bound on the number of small points.

1.3. A New Gap Principle. As said above, the combination of [DGH21] and [K¨uh21a] to
imply Theorem 1.1 is not immediate. This is done via proving the following New Gap Principle.
We refer to Theorem 4.1 for the precise statement.
Roughly speaking, we ﬁnd positive constants c1 and c2 that depend only on g such that each
P ∈ C(Q) satisﬁes

(1.2) # {Q ∈ C(Q) : ˆh(Q − P ) ≤ c1 max{1, h([Jac(C)])}
} < c2.

Up to some ﬁnite set of uniformly bounded cardinality, this New Gap Principle is precisely
[DGH21, Prop.7.1] provided that h([Jac(C)]) ≥ δ for some δ = δ(g). It was explained in [DGH20,
Prop.2.3 and Prop.2.5] how this extra condition on h([Jac(C)]) can be removed by assuming the
Relative Bogomolov Conjecture. Following a similar proof, we show in §9 that this extra condition
on h([Jac(C)]) can also be removed by using [K¨uh21a, Thm.3], which itself can be deduced from
the Relative Bogomolov Conjecture.
Here is a sketch. The proof of [DGH21, Prop.7.1] shows that the bound above holds true (for
any curve) with c1 max{1, h([Jac(C)])} replaced by c1 max{1, h([Jac(C)])} − c3, for some c3 =
c3(g). Hence what remains to be done is to remove this constant term c3. This is exactly what
[K¨uh21a, Thm.3] (#{Q ∈ C(Q) : ˆh(Q − P ) ≤ c3} < c2 up to adjusting c3 and c2 appropriately)
accounts for.

1.4. Structure of the survey. In §2, we give a quick recall to the Height Machine. In §3, we
brieﬂy go through the key ingredients of Vojta’s approach to prove the Mordell conjecture. In
particular, we will summarize the classical results on bounding the number of large points, by
Mumford’s and Vojta’s inequality; in the end we state the classical results in the relative setting.
In §4, we give our setup involving several universal families, and state the New Gap Principle.
In §5, we recall the Betti map and Betti form, which are fundamental tools to study non-
degeneracy.
In §6–8, we explain the three key new ingredients listed in §1.1, each occupying a section.
We will state the main results and focus on presenting how they are applied. In §6, we give the
deﬁnition of non-degenerate subvarieties in two equivalent ways and explain how to construct
non-degenerate subvarieties from given varieties; this construction is important in applications.
In §7, we state the height inequality and give an example on how it is used in Diophantine
Geometry. This example is in line with [DGH21, Prop.7.1]; a minor improvement is that it
provides more explicit constants. In §8, we state the equidistribution result, and give a detailed
proof on how it is used to prove [K¨uh21a, Thm.3].
We will give a detailed proof of the New Gap Principle in §9 using the height inequality and the
equidistribution result from the previous section. The proof is in line with [DGH20, Prop.2.3].
Then we shortly explain how to conclude for Theorem 1.1.
We will discuss some related open problems in §10. In §10.1, we state the Relative Bogomolov
Conjecture and explain how it implies [K¨uh21a, Thm.3]. In §10.2, we discuss brieﬂy the Uni-
form Mordell–Lang Conjecture for high dimensional subvarieties of abelian varieties. We give
several equivalent formulations of this conjecture and prove their equivalence. We also formulate
(without proof) the generalized New Gap Principle.

Acknowledgements. I would like to thank my collaborators Philipp Habegger and Vesselin
Dimitrov on this project, and I would like to thank Yves Andr´e, Serge Cantat, Pietro Corvaja,
Junyi Xie, and Umberto Zannier for collaboration on related problems. I would like to thank Lars
K¨uhne for sending me his preprints [K¨uh21a, K¨uh21b]. I would like to thank Dan Abramovich,

6

Marc Hindry, and Barry Mazur for their encouragement, comments, and suggestions on the
conjectures about the high dimensional subvarieties discussed in §10.2. I would like to thank
Camille Amoyal, Laura DeMarco, Gabriel Dill, Philipp Habegger, Marc Hindry, Lars K¨uhne,
Myrto Mavraki, Barry Mazur, Fabien Pazuki, Yunqing Tang, Xinyi Yuan, and Umberto Zannier
for their valuable comments on a previous version of the manuscript. I would like to thank
Gabriel Dill for providing me the references [Ray83a] and for an argument to ﬁx a gap of
Lemma 10.4 in a previous version. I would like to thank Ga¨el R´emond for providing me the
two examples at the end of the survey; they helped me achieve the current formulation for
Conjecture 10.5. This project has received funding from the European Research Council (ERC)
under the European Union’s Horizon 2020 research and innovation programme (grant agreement
n◦ 945714).
 2. The Height Machine

In this section, we recollect some basic facts on the Height Machine and the canonical height
functions on an abelian variety. There are many standard textbooks on this, for example [BG06]
and [HS00].
All varieties, line bundles and morphisms in this section are assumed to be deﬁned over Q.

2.1. Naive height function on projective spaces. We refer to [BG06, Chap.1] and [HS00,
B.1 and B.2].
We start with the simplest case. Let x ∈ P1(Q). There is a unique way to write x as [a : b]
with a, b ∈ Z such that we are in one of the following two cases:
• a = 0, b = 1 or a = 1, b = 0;
• a > 0 and b ̸= 0 are coprime.
Then the height of x is deﬁned to be 0 in the ﬁrst case and log max{|a|, |b|} in the second case,
with | · | being the standard absolute value.
Now let us generalize this deﬁnition to Pn(K) for any integer n ≥ 1 and any number ﬁeld K.
A place of a number ﬁeld K is an absolute value | · |v : K → [0, ∞) whose restriction to Q is
either the standard absolute value or a p-adic absolute value for some prime p with |p| = p−1.
Let Kv be the completion of K at v with respect to | · |v. Set dv = [Kv : R] in the former and
dv = [Kv : Qp] in the latter case. The absolute logarithmic Weil height, or just height, of a point
x = [x0 : . . . : xn] ∈ Pn(K) with x0, . . . , xn ∈ K is

(2.1) h(x) = 1
[K : Q]
 ∑

v dv log max{|x0|v, . . . , |xn|v}

where the sum runs over all places v of K. The value h(x) is independent of the choice of
projective coordinates by the Product Formula, and for x ∈ P1(Q) this h(x) coincides with the
height deﬁned in the previous paragraph. Moreover, the height does not change when replacing
K by another number ﬁeld that contains the coordinates of x. Therefore, h(·) is a well-deﬁned
function

(2.2) h : Pn(Q) → [0, ∞).

We call this function the naive height function on Pn
Q.

2.2. Height Machine. We refer to [BG06, Chap.2] and [HS00, B.3].
Let X be an irreducible projective variety deﬁned over Q. Denote by RX(Q) the set of functions
X(Q) → R, and by O(1) the subset of bounded functions.
The Height Machine associates to each line bundle L ∈ Pic(X) a unique class of functions
RX(Q)/O(1), i.e. a map

(2.3) hX : Pic(X) → RX(Q)/O(1), L ↦→ hX,L.
 7

Let hX,L : X(Q) → R a representative of the class hX,L; it is called a height function associated
with (X, L).
One can construct hX,L as follows. In each case below, hX,L depends on some extra data
and hence is not unique. However, it can be shown that any two choices diﬀer by a bounded
functions on X(Q), and thus the class of hX,L is well-deﬁned.

(i) If L is very ample, then the global sections of L give rise to a closed immersion ι : X → Pn

for some n. Set hX,L = h ◦ ι, with h the naive height function on Pn from (2.2).
(ii) If L is ample, then L⊗m is very ample for some m ≫ 1. Set hX,L = (1/m)hX,L⊗m .
(iii) For an arbitrary L, there exist ample line bundles L1 and L2 on X such that L ≃
L1 ⊗ L⊗−1
2 . Set hX,L = hX,L1 − hX,L2.

Here are some basic properties of the Height Machine. These properties, or more precisely
properties (i)-(iii), also uniquely determine (2.3).

Proposition 2.1. We have

(i) (Normalization) Let h be the naive height function from (2.2). Then for all x ∈ Pn(Q),
we have hPn,O(1)(x) = h(x) + O(1).

(ii) (Functoriality) Let φ : X → Y be a morphism of irreducible projective varieties and let
L be a line bundle on Y . Then for all x ∈ X(Q), we have

hX,φ∗L(x) = hY,L(φ(x)) + O(1).

(iii) (Additivity) Let L and M be two line bundles on X. Then for all x ∈ X(Q), we have

hX,L⊗M (x) = hX,L(x) + hX,M (x) + O(1).

(iv) (Positivity) If s ∈ H 0(X, L) is a global section, then for all x ∈ (X \ div(s))(Q) we have

hX,L(x) ≥ O(1).

(v) (Northcott property) Assume L is ample. Let K0 be a number ﬁeld on which X is deﬁned.
Then for any d ≥ 1 and any constant B, the set

{x ∈ X(K) : [K : K0] ≤ d, hX,L(x) ≤ B}

is a ﬁnite set.

The O(1)’s that appear in the proposition depend on the varieties, line bundles, morphisms,
and the choices of the representatives in the classes of height functions. But they are independent
of the points on the varieties.
In applications, we often do not have projective varieties, but only quasi-projective varieties.
For example, f : X → Y a morphism between quasi-projective varieties. Then f can be viewed
as a rational map X //❴❴❴ Y . In this case, we have the following result of Silverman.

Theorem 2.2. Let f : X //❴❴❴ Y be a generically ﬁnite rational map between projective vari-
eties. Let L be an ample line bundle on X and M be an ample line bundle on Y . Then

(i) there exist constants c1 > 0 and c2 such that hY,M (f (x)) ≤ c1hX,L(x) + c2 for all x ∈
X(Q) such that f (x) is well-deﬁned;
(ii) there exist constants c′
1 > 0, c′
2 and a Zariski open dense subset U ⊆ X such that
hY,M (f (x)) ≥ c′
1hX,L(x) − c′
2 for all x ∈ U (Q).

While part (i) [Sil11, Lem.4] is an easy application of the triangular inequality, part (ii) [Sil11,
Thm.1] is highly non-trivial.
 8

2.3. N´eron–Tate height function on abelian varieties. We refer to [BG06, Chap.9] and
[HS00, B.5].
In this subsection, we turn to abelian varieties. Let A be an abelian variety and L be a line
bundle on A. Assume furthermore that L is symmetric, i.e. L ≃ [−1]∗L.
The Tate Limit Process provides a distinguished representative in the class of height functions
associated with (A, L) provided by the Height Machine (2.3). Indeed, let hA,L be a representative
of this class, and set

(2.4) ˆhA,L(x) := lim
N →∞ hA,L([2N ]x)
4N .

The function ˆhA,L is called the canonical height or N´eron–Tate height on A with respect to L.
It satisﬁes, and is uniquely determined by, the following properties.
[3]

Proposition 2.3. We have, for all x ∈ A(Q),

(i) ˆhA,L(x) = hA,L(x) + O(1);
(ii) ˆhA,L([N ]x) = N 2ˆhA,L(x) for all N ∈ Z.

Note that (i) implies that ˆhA,L is in the same class of height functions as hA,L. The bounded
function O(1) in (i) depends on A, L and the choice of the representative hA,L in the class of
height functions.
In practice, we often work with symmetric ample line bundles. We have the following theorem.

Theorem 2.4. Assume L is ample. Then
(i) ˆhA,L(x) ≥ 0 for all x ∈ A(Q);
(ii) ˆhA,L(x) = 0 if and only if x ∈ A(Q)tor;
(iii) ˆhA,L extends R-linearly to a positive deﬁnite quadratic form A(Q) ⊗Q R → R, which by
abuse of notation is still denoted by ˆhA,L.

In the context where the abelian variety is clear, we often abbreviate ˆhA,L by ˆhL.
We close this section by discussing the relative setting. Let S be an irreducible variety and
let π : A → S be an abelian scheme of relative dimension g ≥ 1. Let L be a relatively ample
line bundle on A/S such that [−1]∗L ≃ L. In particular over each s ∈ S(Q), the line bundle
Ls := L|As on As := π−1(s) is ample and symmetric. The ﬁberwise N´eron–Tate height with
respect to L is deﬁned to be

(2.5) ˆhA,L : A(Q) → [0, ∞), x ↦→ ˆhAπ(x),Lπ(x)(x).

In the rest of the paper, we often abbreviate it as ˆhL.
We close this section with the following theorem of Silverman–Tate; see [Sil83, Thm.A] and
[DGH21, Thm.A.1]. Let M be an ample line bundle on S, a compactiﬁcation of S. Then the
Height Machine provides a height function hS,M : S(Q) → R.

Theorem 2.5. There exists a constant c = c(A/S, L, M) > 0 such that

|ˆhL(x) − hA,L(x)| ≤ c max{1, hS,M(π(x))} for all x ∈ A(Q).

3. Vojta’s method

In this section we give an overview of Vojta’s approach to prove the Mordell Conjecture.
Let A be an abelian variety deﬁned over Q equipped with a very ample and symmetrical line
bundle L. Then L gives rise to a normalized height function ˆhL : A(Q) → [0, ∞) as constructed
in (2.4).

[3]In particular, ˆhA,L does not depend on the choice of the representative hA,L in (2.4).
 9

For P, Q ∈ A(Q) we set ⟨P, Q⟩ = (ˆhL(P + Q) − ˆhL(P ) − ˆhL(Q))/2 and often abbreviate
|P | = ˆhL(P )1/2. The notation |P | is justiﬁed by the fact that it induces a norm after tensoring
with the reals.

3.1. Mordell conjecture. The following fundamental inequalities are the keys to prove the
ﬁniteness of rational points on curves of genus at least 2. They are called the Mumford inequality
(or Mumford’s Gap Principle) and the Vojta inequality. We state them together.

Theorem 3.1. Let g ≥ 2 and C be a smooth curve of genus at least 2 deﬁned over Q. Let
P0 ∈ C(Q), and j : C → Jac(C) be the Abel–Jacobi embedding via P0.
There exists a constant R = R(C, P0) > 0 such that the following properties hold true. Con-
sider all distinct points P, Q ∈ C(Q) such that |j(Q)| ≥ |j(P )| ≥ R and

(3.1) ⟨j(P ), j(Q)⟩ ≥ 3
4 |j(P )||j(Q)|,

then we have
(i) (Mumford Inequality) |j(Q)| ≥ 2|j(P )|.
(ii) (Vojta Inequality) there exists a constant κ = κ(g) > 0 such that |j(Q)| ≤ κ|j(P )|.

Notice that these two inequalities hold true for all algebraic points, not only rational points,
on the curve C.

Let us have a digest of the inequalities.
We start with the assumptions of the properties. The hypothesis |j(Q)| ≥ |j(P )| can be
assumed to hold true up to exchanging P and Q. The assumption (3.1) should be understood
to be saying that the angle between j(P ) and j(Q) is bounded above by a constant cos−1(3/4).
More precisely, if we ﬁx a subgroup Γ of Jac(C)(Q) of ﬁnite rank and consider only P, Q ∈ Γ,
then j(P ), j(Q) ∈ Γ ⊗Q R and (Γ ⊗Q R, | · |) is a normed Euclidean space of ﬁnite dimension,
and ⟨j(P ), j(Q)⟩/|j(P )||j(Q)| is precisely the angle between j(P ) and j(Q). Observe that it is
possible to divide Γ ⊗Q R into 7rkΓ cones Λ such that each two points in the same cone satisﬁes
(3.1).
Now we turn to the conclusions. Part (i) says that each two distinct points in a same cone Λ are
“far” from each other, while part (ii) says that they cannot be “too far” either, unless at least one
of these two points has small norm. Now if there is a sequence of distinct points P0, P1, . . . , Pm
in Λ such that |j(Pm)| ≥ · · · ≥ |j(P1)| ≥ |j(P0)| ≥ R, then |j(Pm)| ≥ 2|j(Pm−1)| · · · ≥ 2m|j(P0)|
by (i) and |j(Pm)| ≤ κ|j(P0)| by (ii). Thus m ≤ log κ/ log 2. As there are 7rkΓ cones, we obtain

(3.2) #{P ∈ Γ : |j(P )| ≥ R} ≤ (log κ/ log 2 + 1)7
rkΓ.

Notice that (3.2) suﬃces to prove the Mordell conjecture. Assume C is deﬁned over a number
ﬁeld K. Take P0 ∈ C(K) and the Abel–Jacobi embedding j : C → Jac(C) via P0. By the
Mordell–Weil theorem, Γ := Jac(C)(K) is a ﬁnitely generated group. Thus the set Γtor of
torsion points in Γ is a ﬁnite set. So to prove the ﬁniteness of C(K) ≃ Γ ∩ j(C)(Q) we may
identify Γ with its image in Γ ⊗Z R. Consider the Euclidean space (Γ ⊗Z R, | · |). By (3.2), to
prove #C(K) < ∞ it suﬃces to prove the ﬁniteness of C(K)small := {P ∈ C(K) : |j(P )| < R},
or equivalently the ﬁniteness of j(C(K)small). But after modulo the ﬁnite set Γtor, j(C(K)small)
is a subset of {z ∈ Γ : |z| < R} which consists of lattice points of bounded norm and hence is
immediately a ﬁnite set. Hence we are done.

3.2. Relative setting. Mumford’s and Vojta’s inequality (Theorem 3.1) can be realized in
families. The ﬁrst explicitly written result in this direction is de Diego [dD97, Thm.2 and
below]. The version we state here can be obtained as a consequence of R´emond’s quantitative
versions of the Mumford and the Vojta inequalities, [R´em00a, Thm.3.2] and [R´em00b, Thm.1.2].
All varieties and morphisms below are assumed to be deﬁned over Q.
 10

Let S be an irreducible variety and let π : A → S be an abelian scheme of relative dimension
g ≥ 1. Let L be a relatively ample line bundle on A/S such that [−1]∗L ≃ L. We write
ˆhL : A(Q) → [0, ∞) for the ﬁberwise N´eron–Tate height (2.5).
Moreover, let M be an ample line bundle over a compactiﬁcation S of S. Then we obtain
a function hS,M : S(Q) → R which is a representative of the height provided by the Height
Machine (2.3).
If C is an irreducible closed subvariety of A and s ∈ S(Q), then we write Cs for π|
−1
C (s).

Theorem 3.2. Let C ⊂ A be an irreducible closed subvariety that dominates S and such
that C → S is a ﬂat family of curves of genus at least 2. Then there exists a constant
c = c(π, L, M; C) ≥ 1 with the following property. Suppose s ∈ S(Q) and Γ is a subgroup
of As(Q) of ﬁnite rank ρ ≥ 0, then

(3.3) # {
P ∈ Cs(Q) ∩ Γ : ˆhL(P ) > c max{1, hS,M(s)}
} ≤ c
ρ.

It is possible to prove Theorem 3.2 by adapting appropriately the arguments in [dD97]. Alter-
natively, Theorem 3.2 can be proved more directly and with more explicit constants as a conse-
quence of R´emond’s quantitative versions of the Mumford and the Vojta inequalities, [R´em00a,
Thm.3.2] and [R´em00b, Thm.1.2], with the (Arithmetic) B´ezout Theorem; see [DGH21, proof
of Prop.8.1] for more details.

4. Basic setup and Statement of the New Gap Principle

Fix an integer g ≥ 2 and an integer ℓ ≥ 3. By level-ℓ-structure we mean symplectic level-ℓ-
structure.

4.1. Universal families. It is natural to work with families to prove uniform bounds. In this
subsection we introduce the various universal families which will be used.

(i) The universal curve Cg → Mg. Here Mg is the ﬁne moduli space of smooth projective
curves of genus g with level-ℓ-structure, and each ﬁber over s ∈ Mg(C) is isomorphic
to the curve parametrized by s. It is known that Mg is an irreducible regular quasi-
projective variety of dimension 3g − 3. It is an irreducible variety deﬁned over Q. We
refer to [DM69, (5.14)], or [OS80, Thm.1.8].
(ii) The universal abelian variety π : Ag → Ag. Here Ag is the ﬁne moduli space of principally
polarized abelian varieties of dimension g with level-ℓ-structure, and each ﬁber over
s ∈ Ag(C) is isomorphic to the abelian variety parametrized by s. It is known that Ag is
an irreducible regular quasi-projective variety of dimension g(g+1)/2. It is an irreducible
variety deﬁned over Q. We refer to [MFK94, Thm.7.9 and below] or [OS80, Thm.1.9].

The two universal families can be related in the following way. Let Jac(Cg/Mg) be the relative
Jacobian of Cg → Mg. It is an abelian scheme equipped with a natural principal polarization
and with level-ℓ-structure; see [MFK94, Prop.6.9]. Attaching the Jacobian to a smooth curve
induces the Torelli morphism τ : Mg → Ag. The famous Torelli theorem states that, absent
level structure, the Torelli morphism is injective on C-points. In our setting, τ is a quasi-ﬁnite
morphism cf. [OS80, Lem.1.11]. As Ag is a ﬁne moduli space we have the following Cartesian
diagram

(4.1) Jac(Cg/Mg) //

  
 ❴✤ Ag

π
  
Mg τ // Ag
 11

4.2. The Faltings–Zhang map. The New Gap Principle from §1.3 concerns the diﬀerences of
the points on each curve C taken in its Jacobian Jac(C). This operation can be made precise by
setting the subvariety C − C of Jac(C) to be the image of C × C → Jac(C) = Pic
0(C), (P, Q) ↦→
[Q − P ]. By abuse of notation we denote by (P, Q) ↦→ Q − P .
[4]

We need to realize this diﬀerence in families. Let Pic(Cg/Mg) be the relative Picard scheme; it
is a group scheme over Mg and can be decomposed as the union of open and closed subschemes
Picp(Cg/Mg) for all p ∈ Z, where p indicates the degree of a line bundle. The diﬀerence group law
Pic(Cg/Mg) ×Mg Pic(Cg/Mg) → Pic(Cg/Mg), when restricted to Pic
1(Cg/Mg) ×Mg Pic1(Cg/Mg),
induces an Mg-morphism

Pic1(Cg/Mg) ×Mg Pic1(Cg/Mg) → Pic
0(Cg/Mg) = Jac(Cg/Mg).

From [MFK94, proof of Prop.6.9] we get a Mg-morphism Cg → Pic1(Cg/Mg). Thus the Mg-
morphism above induces an Mg-morphism

(4.2) D1 : Cg ×Mg Cg → Jac(Cg/Mg).

The restriction of D1 to each ﬁber is precisely (P, Q) ↦→ Q − P . We thus denote by Cg − Cg the
image of D1.
This construction can be generalized to more factors. Let M ≥ 1 be an integer. Let C[M ]
g
and Jac(Cg/Mg)[M ] denote the respective M -th ﬁbered powers over Mg. Then we get an Mg-
morphism

(4.3) DM : C[M +1]
g → Jac(Cg/Mg)
[M ],

such that over each ﬁber it is (P0, P1, . . . , PM ) ↦→ (P1 − P0, . . . , PM − P0).

4.3. Height functions. To give a precise statement of the New Gap Principle, we need to ﬁx
the height functions. All line bundles below are assumed to be deﬁned over Q.
Let L be a line bundle on Jac(Cg/Mg) ample over Mg such that [−1]∗L ≃ L; see [Ray70,
Thm.XI 1.4]. This deﬁnes a ﬁberwise N´eron–Tate height (2.5)

(4.4) ˆhL : Jac(Cg/Mg)(Q) → [0, ∞).

We also ﬁx an ample line bundle M on Mg, where Mg is a compactiﬁcation of Mg. The Height
Machine (2.3) provides an equivalence class of height function of which we ﬁx a representative

(4.5) hMg,M : Mg(Q) → R.

4.4. The New Gap Principle. We are now ready to give the precise statement of the new
Gap Principle. By deﬁnition of the moduli space and the universal curve, each smooth curve
C of genus g ≥ 2 deﬁned over Q is isomorphic to Cs, the ﬁber of Cg → Mg over s, for some
s ∈ Mg(Q). Use the height functions from §4.3.

Theorem 4.1 (Dimitrov–Gao–Habegger + K¨uhne). There exist positive constants c1, c2 de-
pending only on g (apart from L and M) with the following property. For each s ∈ Mg(Q) and
each P ∈ Cs(Q), we have

(4.6) # {Q ∈ Cs(Q) : ˆhL(Q − P ) ≤ c1 max{1, hMg ,M(s)}
} < c2.

In the statement (4.6), the height hMg,M(s) can be replaced by any modular height of
[Jac(C)] ∈ Ag,1(Q); see [DGH21, proof of Thm.1.2 and above]. Here Ag,1 is the coarse moduli
space of principally polarized abelian varieties of dimension g. The key point is that the Torelli
map τ : Mg → Ag is quasi-ﬁnite and the triangular inequality Theorem 2.2.(i). By a fundamental

[4]Notice that for any Abel–Jacobi embedding j : C → Jac(C), we have C − C = j(C) − j(C), where the
diﬀerence on the right hand side is taken as the group operation on the abelian variety. This is because doing the
diﬀerence cancels out the base point of the Abel–Jacobi embedding.
 12

work of Faltings [Fal83, §3 including the proof of Lemma 3] to compare the modular height with
the Faltings height of any given abelian variety, hMg,M(s) can furthermore be replaced by the
Faltings height hFal(Jac(C)).
The proof of Theorem 4.1 is a combination of [DGH21, Prop.7.1 (and its proof)] and [K¨uh21a,
Thm.3]. Roughly speaking, the former result handles curves of large height, and the latter result
handles curves of small height. More precisely, an adjustment of the proof of [DGH21, Prop.7.1]
proves (4.6) with c1 max{1, hMg ,M(s)} replaced by c1 max{1, hMg ,M(s)} − c3, and hence what
remains to be done is to remove the constant term c3. Then [K¨uh21a, Thm.3] proves (4.6) with
c1 max{1, hMg ,M(s)} replaced by some c′
3 > 0, which is exactly what is needed to remove the c3.

4.5. Polarization type. Let d1| · · · |dg be positive integers, and set D := diag(d1, . . . , dg).
In this subsection, we introduce a new moduli space and the universal family, cf. [GN09, §1.2 and 1.3].
Let Ag,ℓ,D be the moduli space of abelian varieties polarized of type D (so of dimension g) with
level-ℓ-structure. If ℓ ≥ 3, then Ag,ℓ,D is a ﬁne moduli space, and hence admits a universal family
Ag,ℓ,D → Ag,ℓ,D.
The universal covering in the category of complex spaces for Ag,ℓ,D is given by Hg → Aan
g,ℓ,D, where
Hg = {Z ∈ Matg×g(C) : Z = Z
⊺, Im(Z) > 0} is the Siegel upper half space. Let Sp2g,D be the Q-group
deﬁned by

(4.7) Sp2g,D(Q) = {
g ∈ SL2g(Q) : g [ 0 D
−D 0
 ] g
⊺ = [ 0 D
−D 0
 ]} .

Then Sp2g,D(R) acts transitively on Hg as described in [GN09, §1.2], and the uniformization above induces
Aan
g,ℓ,D ≃ Sp2g,D(1 + ℓZ)\Hg with Sp2g,D(1 + ℓZ) = Ker(Sp2g,D(Z) → Sp2g,D(Z/ℓZ)).
In the context, we often abbreviate Ag,ℓ,D by Ag,D, and Ag,ℓ,D by Ag,D.
Now let S be an irreducible variety over C and π : A → S be an abelian scheme of relative dimension
g ≥ 1. By [GN09, §2.1], A → S is polarizable of type D for some diagonal matrix D as above. Then up
to taking a ﬁnite cover of S and taking the appropriate base change of A → S, there exists a Cartesian
diagram

(4.8) A ι //

π   
 ❴✤ Ag,D

  
S ιS // Ag,D.

The morphism ι is called the modular map.

5. Betti map and Betti form

This section introduces two fundamental tools in the course of proving Theorem 1.1, the Betti
map and the Betti form.
In this section, let S be an irreducible variety over C and π : A → S be an abelian scheme
of relative dimension g ≥ 1. By [GN09, §2.1], there exist positive integers d1| · · · |dg such that
A → S is polarizable of type D := diag(d1, . . . , dg).

5.1. Betti map. The Betti map is a useful tool in Diophantine Geometry. It was already used
in early works of Corvaja, Masser and Zannier on the Relative Manin–Mumford Conjecture; see
§10.1. The name “Betti map” was proposed by Bertrand.

The idea to deﬁne the Betti map is simple: one identiﬁes each closed ﬁber As with the real
torus T2g under the period matrices. Here is a brief construction. For any s ∈ S(C), there exists
an open neighborhood ∆ ⊆ San of s which we may assume is simply-connected. Then one can
deﬁne the Betti map

(5.1) b∆ : A∆ = π−1(∆) → T2g,
 13

as follows. As ∆ is simply-connected, one deﬁnes a basis ω1(s), . . . , ω2g(s) of the period lattice
of each ﬁber s ∈ ∆ as holomorphic functions of s. Now each ﬁber As = π−1
S (s) can be identiﬁed
with the complex torus Cg/Zω1(s)⊕· · ·⊕Zω2g(s), and each point x ∈ As(C) can be expressed as
the class of ∑2g
i=1 bi(x)ωi(s) for real numbers b1(x), . . . , b2g(x). Then b∆(x) is deﬁned to be the
class of the 2g-tuple (b1(x), . . . , b2g(x)) ∈ R2g modulo Z2g. We thus obtain (5.1). The map b∆ is
not unique, but it is unique up to GL2g(Z) ≃ Aut(T2g). In fact, later on we will see that b∆ is
in fact unique up to Sp2g,D(Z) with the group Sp2g,D deﬁned in (4.7) if the basis is well-chosen.

The following Betti rank is of particular importance; see [ACZ20].

Deﬁnition 5.1. Let X be an irreducible subvariety of A and let x ∈ X sm(C). The Betti rank
of X at x is deﬁned to be

(5.2) rankBetti(X, x) := rankR(db∆|X sm,an )x

where ∆ is an open neighborhood of π(x) in San and b∆ is the Betti map.

The right hand side of (5.2) does not depend on the choice of ∆ or b∆.

More concrete constructions of the Betti map can be found in [ACZ20] via 1-motives, in
[CGHX21] by means of Arithmetic Dynamics, and in [Gao20a] using the universal abelian va-
rieties. An ad hoc construction when dim S = 1 can be found in [GH19]. In the course of the
constructions, the following proposition can be proved.

Proposition 5.2. The Betti map b∆ satisﬁes the following properties.
(i) For each t ∈ T2g, we have that b−1
∆ (t) is complex analytic.
(ii) For each s ∈ ∆, the restriction b∆|As is a group isomorphism.
(iii) The map (b∆, π) : A∆ → T2g × ∆ is a real analytic isomorphism.

We hereby take the construction from [Gao20a, §3 and 4], and brieﬂy sketch for the case
Ag,D → Ag,D. The general case follows easily from it by composing with the modular map ι
from (4.8).
The universal covering Hg → Aan
g,D, where Hg = {Z ∈ Matg×g(C) : Z = Z
⊺, Im(Z) > 0} is the
Siegel upper half space, gives a polarized family of abelian varieties AHg → Hg ﬁtting into the
diagram
 AHg := Aan
g,D ×Aan
g,D Hg uB //

  
 Aan
g,D

πuniv
  
Hg // Aan
g,D.

For the universal covering u : Cg × Hg → AHg and for each Z ∈ Hg, the kernel of u|Cg×{Z} is
DZg + ZZg. Thus the map Cg × Hg → Rg × Rg × Hg → R2g, where the ﬁrst map is the inverse
of (a, b, Z) ↦→ (Da + Zb, Z) and the second map is the natural projection, descends to a real
analytic map buniv : AHg → T2g.

Now for each s0 ∈ Ag,D(C), there exists a contractible, relatively compact, open neighborhood
∆ of s0 in Aan
g,D such that Ag,D,∆ := (πuniv)−1(∆) can be identiﬁed with AHg,∆′ for some open
subset ∆′ of Hg. The composite b∆ : Ag,D,∆ ≃ AHg,∆′ → T2g is real analytic and satisﬁes the
three properties for the Betti map. Thus b∆ is the desired Betti map in this case. Note that for
a ﬁxed (small enough) ∆, there are inﬁnitely choices of ∆′; but for ∆ small enough, if ∆′
1 and
∆′
2 are two such choices, then ∆′
2 = α · ∆′
1 for some α ∈ Sp2g,D(Z) ⊂ SL2g(Z).
The last sentence of the previous paragraph implies the following property. Fix a Betti map
b∆ : Ag,D,∆ → T2g, then any other Betti map Ag,D,∆ → T2g is α · b∆ for some α ∈ Sp2g,D(Z).
 14

5.2. Betti form. The Betti form is a closed semi-positive smooth (1, 1)-form ω on Aan with
the property [N ]∗ω = N 2ω such that the following property holds true: For any subvariety X
of A and any x ∈ X sm(C), we have

(5.3) rankBetti(X, x) = 2 dim X ⇔ (ω|
∧ dim X
X )x ̸= 0.

There are several ways to construct the Betti form ω. In [DGH21, §2.2 and 2.3] by using a
formula given by Mok [Mok91, pp.374], and in [CGHX21, §2] by means of Arithmetic Dynamics.
We hereby state a third construction via the Betti map. It is closely related to the construction
in [DGH21].

Construction 5.3. Use (a, b) = (a1, b1; . . . ; ag, bg) to denote the coordinates of T2g. Let ∆ be
a simply-connected open subset of San and b∆ : A∆ → T2g be the Betti map from (5.1). Deﬁne
the 2-form on A∆

(5.4) ω∆ = b−1
∆ (
2(Dda)
⊺ ∧ db) = b−1
∆
 

2
 g∑

j=1 djdaj ∧ dbj


 .

Observe that ω∆ is well-deﬁned, because two diﬀerent choices of b∆ diﬀer from an element in
Sp2g,D(Z) (see above §5.2) and 2(Dda)
⊺ ∧ db is preserved by Sp2g,D(R).
Moreover, it is not hard to check that these ω∆ glue together to a 2-form ω on Aan.
This ω is the desired Betti form.

For the ω constructed above, the facts that ω is smooth and [N ]∗ω = N 2ω are not hard to
check. To check that ω is a (1, 1)-form and is semi-positive, one can do an explicit computation
by the change of coordinates (b∆, π) : A∆ → T2g × ∆ from Proposition 5.2.(iii). In fact, by a
similar computation executed in [DGH21, §2.2], one can prove the following statement. For the
uniformization u : Cg × Hg → Aan
g,D and the Betti form ω on Aan
g,D, we have

(5.5) u∗ω = √
−1∂∂ (2(Imw)
⊺ (ImZ)
−1(Imw)
)

where we use (w, Z) to denote the coordinates on Cg × Hg. The symmetric real matrix repre-
senting u∗ω is

(5.6) [ 1 −(Imw)
⊺(ImZ)−1

−(ImZ)−1(Imw) (ImZ)−1(Imw)(Imw)
⊺ (ImZ)−1
] ⊗ (ImZ)
−1.

Now (5.3) a consequence of (5.4); see [K¨uh21a, Lem.10].

Remark 5.4. For each integer M ≥ 1, set A[M ] = A ×S . . . ×S A (M -copies). Then p∗
1ω +
· · · + p∗
M ω is a choice of the Betti form on (A[M ])an, with each pi : A[M ] → A the projection to
the i-th factor.

We close this section by pointing out a more geometric property of the Betti form, which is
a geometric motivation behind [DGH21] and [K¨uh21a].
Assume ℓ ≥ 3 is even. There exists a tautological relatively ample line bundle Lg,D on
Ag,D/Ag,D, namely for each s ∈ Ag,D(C), ((Ag,D)s, (Lg,D)s) is the polarized abelian variety
parametrized by s. Moreover [−1]∗Lg,D = Lg,D. We refer to [Pin89, Prop.10.8 and 10.9].

Proposition 5.5. The cohomology class of the Betti form ω on Aan
g,D coincides with the ﬁrst
Chern class c1(Lg,D) of Lg,D.

This proposition can be deduced from [Mok91, pp.374] or [CGHX21, Lem.2.4].
 15

6. Non-degenerate subvarieties

This section is based on [Gao20a]. In this section, let S be an irreducible variety over C and
π : A → S be an abelian scheme of relative dimension g ≥ 1. Let ω be the Betti form on A from
Construction 5.3.

Deﬁnition 6.1. An irreducible subvariety X of A is said to be non-degenerate if one of the
following equivalent conditions holds true:
(i) rankBetti(X, x) = 2 dim X for some x ∈ X sm(C);
(ii) (ω|∧ dim X
X )x ̸= 0 for some x ∈ X sm(C).

The conditions (i) and (ii) are equivalent by (5.3). By (ii) and Proposition 5.5, non-degeneracy
should be understood to be some bigness condition of an appropriate line bundle.
[5]

6.1. A ﬁrst discussion. In this section, we abbreviate Ag,D → Ag,D by Ag → Ag, with the
polarization type D clear according to the context.
Consider the Cartesian diagram from (4.8), with the modular map ι,

(6.1) A ι //

π   
 ❴✤ Ag

  
S ιS // Ag.

The Betti map b∆ from (5.1) factors through ι. Thus rankBetti(X, x) ≤ 2 dim ι(X) trivially
holds true. So from (i) of Deﬁnition 6.1, ι|X must be generically ﬁnite if X is non-degenerate.
On the other hand, the target of b∆ is T2g. So rankBetti(X, x) ≤ 2g trivially holds true. So from
(i) of Deﬁnition 6.1, dim X ≤ g if X is non-degenerate. To sum it up, the trivial bounds yield

(6.2) X non-degenerate ⇒ ι|X is generically ﬁnite and dim X ≤ g.

Thus, Cg −Cg deﬁned below (4.2) is a degenerate subvariety of Jac(Cg/Mg), because its dimension
is greater than g.
The converse of (6.2) is in general false; see [Gao20a, Thm.1.4(ii)] for an example. But the
converse of (6.2) is true if the geometric generic ﬁber of A → S is a simple abelian variety;
see [Gao20a, Thm.1.4(i)(a)].
Another useful observation is the following lemma.

Lemma 6.2. Let X and Y be irreducible subvarieties of A such that π|X and π|Y are both
dominant. Assume that X is non-degenerate. Then X ×S Y is a non-degenerate subvariety of
A ×S A.

Proof. By generic smoothness, we may assume that S is smooth, and both X sm → S and
Y sm → S are smooth morphisms.
We have dim X ×S Y = dim X + dim Y − dim S. Since X is non-degenerate, there exists
x ∈ X sm(C) such that rankBetti(X, x) = 2 dim X. Let s = π(x) ∈ S(C).
As the Betti map is a group isomorphism when restricted to As = π−1(s) (Proposition 5.2.(ii)),
we have that rankBetti(Y, y) ≥ 2 dim Ys = 2(dim Y − dim S) for a generic y ∈ Y sm
s (C). Thus
y ∈ Y sm(C) as S is smooth and Y sm → S is a smooth morphism.
Now (x, y) ∈ (X ×S Y )sm(C) and rankBetti(X ×S Y, (x, y)) = 2(dim X +dim Y −dim S). Hence
we are done. □

The proof of the lemma above also has the following consequence. Let M ≥ 1 be an integer.
For notation, let X [M ] = X ×S . . . ×S X (M -copies) for any subvariety X of A, and ωM be the
Betti form on A[M ] := A ×S · · · ×S A (M -copies).

[5]In the particular case where X is a projective subvariety of Ag,D, X is non-degenerate if and only if Lg,D|X
is a big line bundle.
 16

Lemma 6.3. Assume π|X sm is smooth and x ∈ X sm(C) satisﬁes (ω|∧ dim X
X )x ̸= 0. Then we
have (ωM |∧ dim X [M ]
X [M ] )(x,...,x) ̸= 0.

Proof. We have rankBetti(X, x) = 2 dim X by (5.3). Let s = π(x). By assumption, (x, . . . , x) ∈
(X [m])sm(C). Thus rankBetti(X [m], (x, . . . , x)) = 2 dim X + 2(m − 1) dim Xs = 2 dim X [m]. Hence
we are done by (5.3). □

6.2. A construction of non-degenerate subvarieties. In applications, especially [DGH21]
and [K¨uh21a], it is necessary to have some reasonable non-degenerate subvariety to start with.
The following result [Gao20a, Thm.1.2’], and more generally [Gao20a, Thm.1.3], play a crucial
role.

Theorem 6.4. Let S → Mg be a generically ﬁnite morphism. Let DM be as from (4.3). Then
DM (C[M +1]
g ) ×Mg S is a non-degenerate subvariety of Jac(Cg/Mg)[M ] ×Mg S for M ≥ dim S + 1;

Theorem 6.4 is a particular case of the more general [Gao20a, Thm.10.1], which we state
now. We expect [Gao20a, Thm.10.1] (with t = 0) to have more applications, for example for
the uniform Mordell–Lang conjecture for higher dimensional subvarieties of abelian varieties.
Let π : A → S be an abelian scheme as at the beginning of this section, and ι : A → Ag be
the modular map from (4.8). For each integer M ≥ 1, set A[M ] := A ×S · · · ×S A (M -copies).
Deﬁne the Faltings–Zhang map

(6.3) D A
M : A[M +1] → A[M ]

to be the S-morphism ﬁberwise deﬁned by (P0, P1, . . . , PM ) ↦→ (P1 − P0, . . . , PM − P0).
For each M ≥ 1, let ι[M ] : A[M ] → AM g be the modular map. As the convention of [Gao20a] is
somewhat diﬀerent from standard notation, we state the result under the formulation of [Gao21,
Thm.4.4.4].

Theorem 6.5. Let X be an irreducible subvariety of A such that π|X is dominant to S. Assume
that Xη (the geometric generic ﬁber of X → S) is irreducible.[6]

Assume furthermore
(a) dim X > dim S.
(b) Xs is generates As for each s ∈ S(C).
(c) On the geometric generic ﬁber Aη of A → S, the stabilizer of Xη, which we denote by
StabAη (Xη), is ﬁnite.

Then as subvarieties of A[M ], we have that
(i) X [M ] is non-degenerate if M ≥ dim S and ι[M ]|X [M ] is generically ﬁnite.
(ii) D A
M (X [M +1]) is non-degenerate if M ≥ dim X and ι[M ]|D A
M (X [M +1]) is generically ﬁnite.

Here X [M ] = X ×S · · · ×S X (M -copies) for each integer M ≥ 1.

In practice, to verify the extra generic ﬁniteness required in (i) and (ii), one can sometimes
use the following observations. For (i), ι[M ]|X [M ] is generically ﬁnite if ι|X is generically ﬁnite.
For (ii), ι[M ]|D A
M (X [M +1]) is generically ﬁnite if ι (and not ι|X ) is quasi-ﬁnite.
Although hypothesis (b) implies hypothesis (a), but we still list hypothesis (a) here to em-
phasize that this construction does not work if X → S is a multi-section.
In fact, [Gao20a, Thm.10.1] is stronger than Theorem 6.5. It says that Theorem 6.5 still holds
true with hypothesis (c) replaced by the weaker hypothesis

[6]This assumption is harmless because it can always be achieved in the following way. There exists a quasi-ﬁnite
´etale morphism S′ → S such that some component X ′ of X ×S S′ satisﬁes that X ′
η is irreducible. But X ′ dominates
X under the natural projection X ×S S′ → X. In applications, we apply this theorem to X ′ ⊆ A ×S S′ → S′.
 17

(c’) On the geometric generic ﬁber Aη of A → S, the neutral component of StabAη (Xη) is
contained in the C(η)/C-trace of Aη, where C(η) is an algebraic closure of the function
ﬁeld of S.
For the general criterion of non-degeneracy, we refer to [Gao20a, Thm.1.1] and [Gao21,
Thm.4.3.1]. In some particular cases, the criterion can be simpliﬁed; see e.g. [Gao20a, (1.4)].

6.3. The degeneracy locus. In this subsection we state another fundamental result about
non-degeneracy. It claims that being non-degenerate is in fact an algebraic property.

Theorem 6.6. To each X, one can associate an intrinsically deﬁned Zariski closed subset X deg

of X such that the following property holds true: X is non-degenerate if and only if X ̸= X deg.
Moreover if X is deﬁned over an algebraically closed ﬁeld F , so is X deg.

This formulation of Theorem 6.6 is taken from [Gao21, Thm.4.3.1 and Prop.4.2.4]. The result
follows essentially from [Gao20a, Thm.1.7 and Thm.1.8] and their proofs.
To be able to compute the constant c(g) from Theorem 1.1, one needs a better understanding
of X deg. We refer to [Gao20a, §1.2] and [Gao21, §4.2] for the deﬁnition and some further
discussions on X deg.
We close the main part of this section by outlining the main steps of to study the non-
degeneracy in [Gao20a]. Both Theorem 6.5 and Theorem 6.6 are proved following this guideline,
where functional transcendence and the unlikely intersection theory are heavily used. The ma-
jor step is to establish a criterion, in simple geometric terms, for an irreducible subvariety X of
the universal abelian variety Ag to be degenerate. Roughly speaking, the proof of the desired
criterion is divided into two steps. Step 1 transfers the degeneracy property to an unlikely inter-
section problem in Ag by invoking the mixed Ax–Schanuel theorem for Ag [Gao20b, Thm.1.1].
More precisely we show that X is degenerate if and only if X is the union of subvarieties sat-
isfying an appropriate unlikely intersection property. Step 2 solves this unlikely intersection
problem, and the key point is to use [Gao20b, Thm.1.4] to prove that the union mentioned
above is a ﬁnite union. In this step the notion of weakly optimal subvarieties introduced by
Habegger–Pila [HP16] is involved.

6.4. 1-parameter case. When dim S = 1, the criterion of non-degeneracy and the degeneracy locus are
easier to describe.

Deﬁnition 6.7. An irreducible closed subvariety Y of A is called a generically special subvariety of
A, or just generically special, if it dominates S and if its geometric generic ﬁber Y ×S Spec C(S) is a
ﬁnite union of (Z ⊗C C(S)) + B, where Z is a closed irreducible subvariety of A
C(S)/C (the C(S)/C-trace
of A) and B is a torsion coset in A ⊗C(S) C(S).

We then have the following results from [GH19, Thm.5.1, Prop.1.3].

Theorem 6.8. Assume dim S = 1. Let X be an irreducible closed subvariety of A which is dominant to
S. Then
(i) X is degenerate if and only if X is generically special;
(ii) we have
 X deg = ⋃

Y ⊆X
Y is a generically special
subvariety of A
 Y.

The union is a ﬁnite union.

7. The height inequality and its application

This section is based on [DGH21]. Let S be a quasi-projective irreducible variety and let
π : A → S be an abelian scheme of relative dimension g, both over Q.
 18

Let L be a relatively ample line bundle on A/S with [−1]∗L ≃ L, and let M be a line bundle
over a compactiﬁcation S of S. All these data are assumed to be deﬁned over Q. Then we have
a ﬁberwise N´eron–Tate height function ˆhL : A(Q) → [0, ∞) as in (2.5), and a height function
hS,M : S(Q) → R provided by the Height Machine (2.3).

7.1. Statement of the height inequality. For any irreducible subvariety X of A, set X ∗ =
X \ X deg with X deg the Zariski closed subset of X from Theorem 6.6. Then X ∗ ̸= ∅ if and only
if X is non-degenerate.
Here is the height inequality of Dimitrov–Gao–Habegger from [DGH21]. When dim S = 1 it
is proved in [GH19].

Theorem 7.1. Let X be an irreducible subvariety of A deﬁned over Q. Let X ∗ = X \ X deg be
the Zariski open subset of X as deﬁned above; it is deﬁned over Q.
There exist constants c > 0 and c′, depending only on X and the data of the height functions,
such that

(7.1) ˆhL(P ) ≥ chS,M(π(P )) − c
′ for all P ∈ X ∗(Q).

This theorem is non-trivial only if X is non-degenerate (otherwise X ∗ = ∅). The version
stated here is a minor improvement of [DGH21, Thm.1.6 and Thm.B.1]. It follows from a
simple Noetherian induction from [DGH21, Thm.B.1], the Zariski closedness of X deg and the
geometric description of X deg; cf. [Gao21, Thm.4.4.2]. Another minor improvement is that M
is not required to be ample on S as in [DGH21], as this extra requirement can easily be dropped
by the Height Machine.
In practice, to apply Theorem 7.1, one needs to have some non-degenerate subvarieties to start
with. For this purpose, apart from directly applying the criterion of non-degeneracy [Gao20a,
Thm.1.1], the construction in Theorem 6.5 is a useful tool.
We point out that the constants in (7.1) are eﬀective; see [DGH21, Rmk.5.1] for comments
on c (which is denoted by c′
1 in loc.cit.).

7.2. Application to the New Gap Principle. In this subsection, we use Theorem 7.1 and
Theorem 6.5 to prove a proposition in the ﬂavor of the New Gap Principle Theorem 4.1. In fact,
applying the proposition to an appropriate family yields [DGH21, Prop.7.1], which is a weaker
version of the New Gap Principle; see the end of §9.2.
This proof, in line with [DGH21, Prop.7.1], is a good example for how the height inequality
Theorem 7.1 is applied to Diophantine problems. Moreover, the framework of the proof will also
be used in Proposition 8.3 (Step 4) and Lemma 10.2.
We also render the constants from [DGH21, Prop.7.1] more explicit, by applying the reﬁned
height inequality and by making Lemma 7.3 (which is [DGH21, Lem.6.3]) explicit.
Let A/S, L and M be as the beginning of this section. Write ι : A → Ag for the modular
map (6.1).

Proposition 7.2. Let C ⊆ A be an irreducible subvariety satisfying the following properties.
Each ﬁber Cs of C → S is an irreducible curve which generates As and is not a translate of an
elliptic curve, and ι|C×S S′ is generically ﬁnite for all subvarieties S′ ⊆ S.
Then there exist constants c′
1, c′
2 and c′
3 such that for each s ∈ S(Q), we have

(7.2) # {x ∈ Cs(Q) : ˆhL(x) ≤ c
′
1 max{1, hS,M(s)} − c
′
3} < c
′
2.

Proof. We prove this proposition by induction on dim S. The proof for the base step dim S = 0
is contained in the induction step.
Fix M ≥ dim S. The properties of C allows us to apply Theorem 6.5(i) applied to C ⊆ A → S.
So C[M ] is a non-degenerate subvariety of A[M ]. Set X := C[M ]. Let X deg be the degeneracy

19

locus of X from Theorem 6.6; it is Zariski closed in X and is deﬁned over Q. Moreover X deg ̸= X
as X is non-degenerate.
Let X ∗ = X \X deg; it is Zariski open dense in X. Applying the height inequality, Theorem 7.1,
to X and A → S, we get

(7.3) ˆhL(x1) + · · · + ˆhL(xM ) ≥ chS,M(s) − c
′

for all s ∈ S(Q) and (x1, . . . , xM ) ∈ X ∗(Q) in the ﬁber above s.
As X ∗ is Zariski open dense in X, each irreducible component of S \ π(X ∗) has dimension
≤ dim S − 1. By induction hypothesis, it suﬃces to prove the proposition with S replaced by
S \ S \ π(X ∗). Therefore we may and do assume π(X ∗) = S. Thus for each s ∈ S(Q), the ﬁber
of X ∗ over s is non-empty.
Use Xs, X ∗
s and X deg
s to denote the corresponding ﬁbers over s. Then the last sentence of
the previous paragraph says X ∗
s ̸= ∅ for each s ∈ S(Q). Equivalently,

(7.4) X deg
s ̸= Xs = CM
s .

This allows us to apply Lemma 7.3 to V = As, L = Ls, C = Cs and Z = X deg
s . Thus setting

(7.5) c
′
2 := max
s∈S(Q) degLs(Cs)
M (M +1)/2 degLs(As)
M (M −1)/2 degL⊠M
s (X deg
s ) + 1,

the following holds true. [7] If a subset Σ ⊆ Cs(Q) has cardinality ≥ c′
2, then ΣM ̸⊆ X deg
s .
We work with Σ = {x ∈ Cs(Q) : ˆhL(x) ≤ c′
1 max{1, hS,M(s)} − c′
3}, with

(7.6) c
′
1 = c/2M and c
′
3 = (c + c
′)/M,

where c and c′ come from the height inequality (7.3).
We claim that #Σ < c′
2. Assume otherwise, then ΣM ̸⊆ X deg
s , and thus there exist x1, . . . , xM ∈
Σ such that (x1, . . . , xM ) ̸∈ X deg
s . Hence (7.3) holds true, and we thus obtain

chS,M(s) − c
′ ≤ M c
′
1 max{1, hS,M(s)} − M c
′
3 = 1
2 c max{1, hS,M(s)} − (c + c
′).

As c max{1, hS,M(s)} ≤ c(1 + hS,M(s)), the inequality above implies

c max{1, hS,M(s)} − c − c
′ ≤ 1
2 c max{1, hS,M(s)} − (c + c
′).

But this last inequality cannot hold true. So we get a contradiction, and hence #Σ < c′
2. This
is precisely the desired bound, and hence we are done. □

The following lemma as well as the proof presented here is nothing but [DGH21, Lem.6.3],
with the bound written explicitly. Let k be an algebraically closed ﬁeld and all varieties are
assumed to be deﬁned over k. Let M ≥ 1 be an integer.

Lemma 7.3. Let V be a projective irreducible variety with an ample line bundle L. Let C be an
irreducible curve in V and let Z be a Zariski closed subset of V M . Assume C M ̸⊆ Z. Then if
Σ ⊆ C(k) has cardinality > degL(C)M (M +1)/2 degL(V )M (M −1)/2 degL⊠M (Z), then ΣM ̸⊆ Z(k).

Proof. We prove this lemma by induction on M . The base step M = 1 follows immediately from B´ezout’s
Theorem.
Assume the lemma is proved for 1, . . . , M − 1 ≥ 1. Let q : V M → V be the projection to the ﬁrst
factor.
B´ezout’s Theorem implies ∑
Y degL⊠M (Y ) ≤ degL(C)
M degL⊠M (Z) with Y running over all irreducible
components of CM ∩ Z. Let Z ′ be the union of such Y ’s with dim q(Y ) ≥ 1, and Z ′′ be the union of the
other components. Then degL⊠M (Z ′), degL⊠M (Z ′′) ≤ ∑
Y degL⊠M (Y ) and hence

(7.7) degL⊠M (Z ′) ≤ degL(C)
M degL⊠M (Z), degL⊠M (Z ′′) ≤ degL(C)
M degL⊠M (Z)

[7]In a ﬂat family, all ﬁbers have the same degree. Thus c
′
2 exists, possibly by a Noetherian induction.
 20

Note that q(Z ′) ⊆ q(CM ∩ Z) ⊆ C. For all P ∈ C(k), the ﬁber q|−1
Z′ (P ) = Z ′ ∩ ({P } × V M−1) has
dimension at most dim Z ′ − 1 ≤ M − 2. So {P } × CM−1 ̸⊆ Z ′ ∩ ({P } × V M−1). Write i : {P } × V M−1 ≃
V M−1 for the natural isomorphism. Then we can apply the induction hypothesis and conclude: if
Σ ⊆ C(k) has cardinality > degL(C)
M(M−1)/2 degL(V )
(M−1)(M−2)/2 degL⊠(M −1) i(Z ′ ∩ ({P } × V M−1)),
then ΣM−1 ̸⊆ i(Z ′ ∩ ({P } × V M−1))(k).
But degL⊠(M −1) i(Z ′ ∩ ({P } × V M−1)) = degL⊠M (Z ′ ∩ ({P } × V M−1)) (since degL(P ) = 1) and
degL⊠M (Z ′ ∩ ({P } × V M−1)) ≤ degL⊠M (Z ′) degL(V )
M−1 by B´ezout’s Theorem. So we can replace
degL⊠(M −1) i(Z ′ ∩ ({P } × V M−1)) in the conclusion of last paragraph by degL⊠M (Z ′) degL(V )
M−1. Thus
by (7.7) we get: if Σ ⊆ C(k) satisﬁes

#Σ > degL(C)
M(M−1)/2 degL(V )
(M−1)(M−2)/2 · degL(C)
M degL⊠M (Z) degL(V )
M−1,

then {P } × ΣM−1 ̸⊆ Z ′(k) for all P ∈ C(k) (and hence ΣM ̸⊆ Z ′(k)). Notice that the right hand side is
precisely degL(C)
M(M+1)/2 degL(V )
M(M−1)/2 degL⊠M (Z).
Now dim q(Z ′′) = 0, so q(Z ′′) is a ﬁnite set of cardinality at most the number of irreducible components
of Z ′′, which is at most degL⊠M (Z ′′) by deﬁnition of the degree. Hence #q(Z ′′) ≤ degL(C)
M degL⊠M (Z)
by (7.7). So if Σ ⊆ C(k) has cardinality > degL(C)
M degL⊠M (Z), then ΣM ̸⊆ Z ′′(k).
Thus the lemma holds true since Z = Z ′ ∪ Z ′′. □

8. Equidistribution on non-degenerate subvarieties and its application

This section is based on [K¨uh21a]. Let S be a quasi-projective irreducible variety and let
π : A → S be an abelian scheme of relative dimension g, both over Q.
Let L be a relatively ample line bundle on A/S deﬁned over Q such that [−1]∗L ≃ L. Then
we have a ﬁberwise N´eron–Tate height function ˆhL : A(Q) → [0, ∞) as in (2.5).

8.1. The equidistribution result. Let ω be the Betti form on A as provided by Construc-
tion 5.3.
The following equidistribution result is proved by K¨uhne [K¨uh21a, Thm.1].

Theorem 8.1. Let X be a non-degenerate subvariety of A deﬁned over Q. There exists a
constant k = k(X, ω) > 0 such that the following property holds true. For any generic sequence
{xn}n∈N in X (namely xn converges to the generic point of X) satisfying ˆhL(xn) → 0, we have

(8.1) 1
#O(xn)
 ∑

y∈O(xn) f (y) → k ∫

X an f (ω|X)
∧ dim X

for all f ∈ C 0
c (X an) (continuous compactly supported in X(C)). Here O(xn) means the Galois
orbit of xn.

The sequence {xn} in Theorem 8.1 will be called a generic small sequence in X.
This equidistribution result was proved by DeMarco–Mavraki [DM20, Cor.1.2] when A → S
is a ﬁber product of elliptic surfaces and X is a section.

The ﬁrst step to use equidistribution to study Bogomolov type problems is through the fol-
lowing corollary, which is a minor improvement of [K¨uh21a, Lem.22]. The idea already showed
up in the work of Ullmo [Ull98] and S. Zhang [Zha98a]. We include the proof in this survey as it
is not complicated and because of the importance of the corollary. This proof is almost a literal
copy of [K¨uh21a, Lem.22].

Corollary 8.2. Let X be a non-degenerate subvariety of A deﬁned over Q. Set µ = k(ω|X )∧ dim X

to be the measure on X(C) with k = k(X, ω) > 0 the constant from Theorem 8.1.
For each function f ∈ C 0
c (X an) and every ǫ > 0, there exist a proper subvariety Zf,ǫ of X
and a constant δǫ > 0 such that each x ∈ (X \ Zf,ǫ)(Q) satisﬁes the following alternative:

(i) Either ˆhL(x) ≥ δǫ;
(ii) or ∣
∣
∣ 1
#O(x) ∑y∈O(x) f (y) − ∫
X an f µ∣
∣
∣ < ǫ.
 21

Proof. To invoke Theorem 8.1, we need a generic small sequence in X. Let us ﬁrst explain why we can
assume this.
Consider, for each n ∈ N, the set Xn := {x ∈ X(Q) : ˆhL(x) < 1/n}. Then we have a descending chain
· · · ⊇ Xn ⊇ Xn+1 ⊇ · · · . Assume that Xn is not Zariski dense in X for some n. Then for any f and ǫ,
one can take δǫ = 1/n and Zf,ǫ = XnZar. Notice that in this case, part (i) always holds true.
So from now on, we assume that Xn is Zariski dense in X for all n ≫ 1. There are only countably many
proper closed subvarieties of X deﬁned over Q, say {Zn}n∈N. For each n ∈ N, take xn ∈ Xn \Zn(Q). Such
an xn exists because Xn is Zariski dense in X and X \ Zn is Zariski open dense in X. Then ˆhL(xn) → 0,
and xn converges to the generic point of X. Hence {xn}n∈N is a generic small sequence in X. Therefore
we are in the situation of Theorem 8.1.
Suppose that the conclusion is false. Then there exist some f ∈ Cc(X an) and some ǫ > 0 with the
following property. For any δ > 0, the set

Bδ :=
 



x ∈ X(Q) : ˆhL(x) < δ and
 ∣
∣
∣
∣
∣
∣
 1
#O(x)
 ∑

y∈O(x) f (y) − ∫
X an f µ
∣
∣
∣
∣
∣
∣ ≥ ǫ





is Zariski dense in X. Then as in the previous paragraph, we can ﬁnd a generic small sequence {xn}n∈N
in X, with each xn ∈ B1/n, such that
∣
∣
∣
∣
∣
∣
 1
#O(xn)
 ∑

y∈O(xn) f (y) − ∫
X an f µ
∣
∣
∣
∣
∣
∣ ≥ ǫ

for all n. This contradicts the equidistribution (8.1). Hence we are done. □

8.2. Application to uniform Bogomolov. Ullmo [Ull98] and S. Zhang [Zha98a] used equidis-
tribution results to prove the Bogomolov conjecture on a single abelian variety over Q. A key
idea in this approach is to apply the equidistribution result twice and compare the measures on
two varieties linked by the Faltings–Zhang map. The upshot is that we are not in case (ii) of
the alternative in the single-abelian-variety version of Corollary 8.2.
It is natural to expect that the equidistribution result in families (Theorem 8.1) can be
applied to solve some family-version Bogomolov type problems, provided that there are some
non-degenerate subvarieties to start with.
A useful tool to construct non-degenerate subvarieties is Theorem 6.5. Starting from this
construction, K¨uhne ran a modiﬁed version of Ullmo–Zhang’s approach on families of curves in
abelian schemes using his family version of the equidistribution (more precisely, Corollary 8.2).
In the end, with a ﬁberwise consideration as in the proof of Proposition 7.2, he proved the
following result [K¨uh21a, Prop.21]. We include this beautiful proof in this survey.
Let ι : A → Ag be the modular map from (6.1).

Proposition 8.3. Let C ⊆ A be an irreducible subvariety satisfying the following properties.
Each ﬁber Cs of C → S is an irreducible curve which generates As and is not a translate of an
elliptic curve, and ι|C×S S′ is generically ﬁnite for all subvarieties S′ ⊆ S.
Then there exist constants c′′
2 and c′′
3 such that for each s ∈ S(Q), we have

(8.2) #{x ∈ Cs(Q) : ˆhL(x) ≤ c
′′
3} < c
′′
2.

Before moving on to the proof, we point out that Proposition 8.3 applied to a suitable family
yields [K¨uh21a, Thm.3] immediately. See the end of §9.2.

Proof of Proposition 8.3. We prove this proposition by induction on dim S. The proof for the
base step dim S = 0 is contained in the induction step.
For readers’ convenience, we divide the proof into several steps.
Step 1 Construct non-degenerate subvarieties.

Fix m ≥ dim S. Consider C[m] := C ×S · · · ×S C (m-copies) and A[m] → S. By generic
smoothness, there exists a Zariski open dense subset S◦ of S such that (C[m])sm ×S S◦ → S◦

22

is a smooth morphism. Moreover up to replacing S◦ by a Zariski open dense subset, we may
and do assume S◦ is smooth. Now that each irreducible component of S \ S◦ has dimension
≤ dim S − 1, by induction hypothesis it suﬃces to prove the proposition with S replaced by S◦.
Hence we may and do assume:

(8.3) S is smooth and (C[m])
sm → S is a smooth morphism.

By Theorem 6.5(i) applied to C ⊆ A → S, we have that C[m] := C ×S · · · ×S C (m-copies)
is a non-degenerate subvariety of A[m]. By Deﬁnition 6.1, for the Betti form ωm of A[m], there
exists a point x ∈ (C[m])sm(C) such that

(8.4) (ωm|
∧ dim C[m]
C[m] )x ̸= 0.

For each M ≫ 1, recall the proper S-morphism (for A[m] instead of A) from (6.3)

(8.5) D A[m]
M : (A[m])
[M +1] → (A[m])
[M ]

ﬁberwise deﬁned by (a0, a1, . . . , aM ) ↦→ (a1 − a0, . . . , aM − a0), with each ai ∈ A[m](Q).
By assumption on C (no ﬁber is a translate of an elliptic curve), it is known that D A[m]
M |(C[m])[M +1]
is generically ﬁnite for M ≫ 1.
A key point of the classical Ullmo–Zhang approach is to use D A[m]
M . A novelty in K¨uhne’s
proof is to consider an extra factor

(8.6) D := (id, D A[m]
M ) : A[m] ×S (A[m])
[M +1] → A[m] ×S (A[m])
[M ],

which is generically injective. In A[m] ×S (A[m])[M +1], we have a non-degenerate subvariety
C[m] ×S (C[m])[M +1].
Let us show that D(C[m] × (C[m])[M +1]) is non-degenerate in A[m] ×S (A[m])[M ]. Indeed,

D(C[m] ×S (C[m])
[M +1]) = C[m] ×S D A[m]
M ((C[m])
[M +1]),

and hence is non-degenerate because C[m] is non-degenerate; see Lemma 6.2.
Now we have obtained the two desired non-degenerate subvarieties C[m] ×S (C[m])[M +1] and
D(C[m] × (C[m])[M +1]). In particular, we are in the situation of Corollary 8.2 for both.
Step 2 Choose suitable functions f1, f2 and constant ǫ > 0 for later applications of Corol-
lary 8.2.
Let µ1 be the measure on C[m] ×S (C[m])[M +1](C) = C[m(M +2)](C) as in Corollary 8.2, and
let µ2 be the measure on D(C[m] × (C[m])[M +1])(C) = D(C[m(M +2)])(C) as in Corollary 8.2. We
will prove µ1 ̸= D|∗
C[m(M +2)]µ2. Assuming this, then there exist a constant ǫ > 0 and a function
f1 ∈ C 0
c (C[m(M +2)],an) such that

(8.7) ∣
∣
∣
∣

∫
C[m(M +2)],an f1µ1 − ∫
C[m(M +2)],an f1D|
∗
C[m(M +2)]µ2
∣
∣
∣
∣ > 2ǫ.

Moreover, since D|C[m(M +2)] is generically ﬁnite, it is not hard to show that one can choose an
f1 satisfying the following property: There exists a unique f2 ∈ C 0
c (D(C[m(M +2)])an) such that
f1 = f2 ◦ D.
Now let us prove µ1 ̸= D|∗
C[m(M +1)]µ2.
[8]

For the point x ∈ (C[m])sm(C) from (8.4), denote by ∆x the point (x, . . . , x) in (C[m])[M +1](C).
Then (x, ∆x) ∈ (C[m] ×S (C[m])[M +1])(C), which is furthermore a smooth point by (8.3). We
have (µ1)(x,∆x) ̸= 0 by Lemma 6.3.

[8]It is for this purpose that we need the C[m] before constructing the two desired non-degenerate subvarieties
linked by the Faltings–Zhang map.
 23

On the other hand, D A[m]
M (∆x) is the origin of ﬁber of (A[m])[M ] → S in question (which
we call (Am
s )M ), so D A[m]
M |
−1
C[m(M +1)](D A[m]
M (∆x)) contains the diagonal of Cm
s ⊆ Am
s in (Am
s )M

(which for the moment we denote by ∆Cm
s ).
Therefore for the morphism D = (id, D A[m]
M ) from (8.6), D|
−1
C[m]×S (C[m])[M +1] (x, D A[m]
M (∆x))

contains (x, ∆Cm
s ). In particular Thus dim D|
−1
C[m]×S (C[m])[M +1](x, D A[m]
M (∆x)) > 0, and so the
linear map

dD|C[m]×S(C[m])[M +1] : T(x,∆x)(C[m] ×S C[m(M +1)]) → T
(x,D A[m]
M (∆x))D(C[m] ×S C[m(M +1)])

has non-trivial kernel. Thus (D|∗
C[m(M +1)]µ2)(x,∆x) = 0.
Thus we get µ1 ̸= D|∗
C[m(M +2)]µ2 by looking at their evaluations at (x, ∆x). Hence we are done
for this step.
Step 3 Prove some height lower bounds on C[m(M +2)] or D(C[m(M +2)]).
We apply the equidistribution result, or more precisely Corollary 8.2, twice.
Apply Corollary 8.2 to C[m] ×S (C[m])[M +1], f1 and ǫ. We thus obtain a constant δǫ,1 > 0
and a Zariski closed proper subset Z1 := Zf1,ǫ of C[m] ×S (C[m])[M +1]. Apply Corollary 8.2 to
D(C[m] ×S (C[m])[M +1]), f2 and ǫ. We thus obtain a constant δǫ,2 > 0 and a Zariski closed proper
subset Z2 := Zf2,ǫ of D(C[m] ×S (C[m])[M +1]).
Let δ := min{δǫ,1, δǫ,2} > 0, and let Z = Z1 ⋃ D|
−1
C[m]×S (C[m])[M +1](Z2) ⋃ Z3, where Z3 is the

largest Zariski closed subset of C[m] ×S (C[m])[M +1] on which D is not injective. Then Z is Zariski
closed in X := C[m] ×S (C[m])[M +1] = (C[m])[M +2], and is proper because D|C[m]×S(C[m])[M +1] is

generically injective. If a point x ∈ (C[m(M +2)] \ Z)(Q) is such that ˆhL⊠m(M +2)(x) < δ and
ˆhL⊠m(M +1)(D(x)) < δ, then case (ii) of Corollary 8.2 holds true for both x, f1, µ1 and D(x), f2, µ2.
Thus
∣
∣
∣
∣
∣
∣

∫
C[m(M +2)],an f1µ1 − 1
#O(x)
 ∑

y∈O(x) f1(y)

∣
∣
∣
∣
∣
∣ < ǫ and
 ∣
∣
∣
∣
∣
∣

∫

D(C[m(M +2)])an f2µ2 − 1
#O(D(x))
 ∑

y∈O(D(x)) f2(y)

∣
∣
∣
∣
∣
∣ < ǫ

where O(·) is the Galois orbit. But 1
#O(x) ∑y∈O(x) f1(y) = 1
#O(D(x)) ∑y∈O(D(x)) f2(y) because

f1 = f2 ◦ D and D is injective on C[m(M +2)] \ Z. So we have
∣
∣
∣
∣
∣

∫
C[m(M +2)],an f1µ1 − ∫
D(C[m(M +2)])an f2µ2
∣
∣
∣
∣
∣ ≤ 2ǫ.

This contradicts (8.7) because f1 = f2 ◦ D.
Hence for each point x ∈ (C[m(M +2)] \ Z)(Q), we are in one of the following alternatives.

(i) Either ˆhL⊠m(M +2)(x) ≥ δ,
(ii) or ˆhL⊠m(M +1) (D(x)) ≥ δ.

Step 4 Finish the proof with a similar argument to the proof of Proposition 7.2.

Denote by π : A[m(M +2)] → S the structural morphism. As Z is proper Zariski closed in
X, each irreducible component of S \ π(C[m(M +2)] \ Z) has dimension ≤ dim S − 1. Thus by
induction hypothesis, it suﬃces to prove the proposition with S replace by S \ π(C[m(M +2)] \ Z).
Therefore we may and do assume the following:

(8.8) For each s ∈ S(Q), we have Zs ̸= Cm(M +2)
s .

By (8.8) and Lemma 7.3, there exists a constant c′′
2 such that the following property holds.
If a subset Σ ⊆ Cs has cardinality ≥ c′′
2, then Σm(M +2) ̸⊆ Zs. This number c′′
2 depends only on

24

m(M + 2), the degree of Cs, and the degree of Zs. Hence c′′
2 can be chosen to be independent of
s. Let c′′
3 = δ/4m(M + 2). Set Σ := {x ∈ Cs(Q) : ˆhL(x) ≤ c′′
3}. It suﬃces to prove #Σ < c′′
2.
Suppose not. Then there exist x1, . . . , xm(M +2) ∈ Σ such that x := (x1, . . . , xm(M +2)) ̸∈ Zs.

Then ˆhL⊠m(M +2) (x) = ∑m(M +2)
i=1 ˆhL(xi) ≤ m(M + 2)c′′
3 < δ. On the other hand, each component
of D(x) is of the form xk or of the form xj − xi for some i and j, and ˆhL(xj − xi) ≤ 2ˆhL(xj) +
2ˆhL(xi) ≤ 4c′′
3. So ˆhL⊠m(M +1)(D(x)) ≤ m(M + 1)4c′′
3 < δ. Thus we have reached a contradiction
to the height bounds at the end of Step 3. Hence we are done. □

9. Proof of the New Gap Principle and proof of Uniform Mordell–Lang for
curves

9.1. Parametrizing space of Abel–Jacobi embeddings. Let π : Cg → Mg be the universal
curve of genus g.
Each closed point in Cg(Q) parametrizes a pair (C, P ) with C a smooth curve of genus g
deﬁned over Q and P ∈ C(Q). Each such pair determines an Abel–Jacobi embedding from a
curve to its Jacobian jP : C → Jac(C), and all Abel–Jacobi embeddings arise in this way. Thus
Cg is the parametrizing space of Abel–Jacobi embeddings.
Let us take a closer look at this. Consider the pullback of the relative Jacobian Jac(Cg/Mg) →
Mg along the universal curve π : Cg → Mg:

(9.1) JCg := Jac(Cg/Mg) ×Mg Cg → Cg.

This is an abelian scheme of relative dimension g.

Proposition 9.1. There is a tautological family C → Cg, with C ⊆ ICg a closed Cg-immersion,
satisfying the following property. For each P ∈ Cg(Q),

(9.2) the ﬁber CP (of C → Cg over P ) is precisely Cπ(P ) − P ,

with Cπ(P ) being the ﬁber of π : Cg → Mg in which P lies.
Moreover, (X ⊆ A → S) := (C ⊆ ICg → Cg) satisﬁes all the hypotheses of Theorem 6.5, and
ι|C×SS′ is generically ﬁnite for the modular map ι : JCg → Ag and for each irreducible subvariety
S′ ⊆ S.

Before proving Proposition 9.1, let us summarize the morphisms and families in the following
diagram.

(9.3) C   • //
 ((◗◗◗◗◗◗◗◗◗◗◗◗◗◗◗◗◗◗ Jac(Cg/Mg) ×Mg Cg = JCg

  
 p1 //
❴
✤ Jac(Cg/Mg)

  
Cg π // Mg.

Proof of Proposition 9.1. The projection to the ﬁrst factor Cg ×Mg Cg → Cg and the morphism
D1 : Cg ×Mg Cg → Jac(Cg/Mg) from (4.2) induce an Mg-morphism

(9.4) λ : Cg ×Mg Cg → Jac(Cg/Mg) ×Mg Cg = JCg

which over each point in Mg(Q) becomes (P, Q) ↦→ (Q − P, P ). Set

C := λ(Cg ×Mg Cg) ⊆ JCg .

Then C is a subvariety of JCg which dominates Cg. The claim (9.2) is not hard to check by
deﬁnition of C. In particular, dim C = dim Cg + 1 = 3g − 1, and the geometric generic ﬁber of
C → Cg is irreducible. Hypotheses (a)-(c) of Theorem 6.5 are easy to check for C ⊆ JCg → Cg.
Thus it remains to check that ι|C×Cg S′ is generically ﬁnite for the modular ι : JCg → Ag and
for each irreducible subvariety S′ ⊆ Cg. But in this case, ι is the composite of the natural

25

projection p1 : JCg → Jac(Cg/Mg) in (9.3) and the quasi-ﬁnite morphism Jac(Cg/Mg) → Ag
from (4.1). Thus it suﬃces to check that p1|C×Cg S′ is generically ﬁnite. This is true, because
dim C ×Cg S′ = dim S′ + 1, and p1(C ×Cg S′) = D1(Cg ×Mg S′) which has dimension 1+ dim S′. □

9.2. Proof of the New Gap Principle. We are ready to prove the New Gap Principle,
Theorem 4.1.
The proof is by applying the following Proposition 9.2 to the C ⊆ ICg → Cg constructed in
§9.1. Proposition 9.2 is proved, following the same line of [DGH20, Prop.2.3], by a combination
of Proposition 7.2 and Proposition 8.3.
[9]

We retain the notations from the beginning of §7. In particular, S is a quasi-projective
irreducible variety and π : A → S is an abelian scheme of relative dimension g; L is a relatively
ample line bundle on A/S with [−1]∗L ≃ L, and M is a line bundle over a compactiﬁcation S of
S. Assume all data are deﬁned over Q, and thus we have two height functions ˆhL : A(Q) → [0, ∞)
from (2.5) and hS,M : S(Q) → R given by the Height Machine (2.3).

Let ι : A → Ag be the modular map from (6.1).

Proposition 9.2. Let C ⊆ A be an irreducible subvariety satisfying the following properties.
Each ﬁber Cs of C → S is an irreducible curve which generates As and is not a translate of an
elliptic curve, and ι|C×S S′ is quasi-ﬁnite for all subvarieties S′ of S.
Then there exist constants c1 and c2 such that for each s ∈ S(Q), we have

(9.5) # {x ∈ Cs(Q) : ˆhL(x) ≤ c1 max{1, hS,M(s)}
} < c2.

Proof. By Proposition 7.2, there exist constants c′
1, c′
2 and c′
3 such that for each s ∈ S(Q), we
have

(9.6) {x ∈ Cs(Q) : ˆhL(x) ≤ c
′
1 max{1, hS,M(s)} − c
′
3}

has cardinality < c′
2.
By Proposition 8.3, there exist constants c′′
2 and c′′
3 such that for each s ∈ S(Q), we have

(9.7) {x ∈ Cs(Q) : ˆhL(x) ≤ c
′′
3}

has cardinality < c′′
2.
Now set

(9.8) c1 := min { c′′
3
max{1, 2c′
3/c′
1} , c′
1
2
 } and c2 := max{c
′
2, c
′′
2}.

We will prove that these are the desired constants.
To prove this, it suﬃces to prove the following claim.
Claim: If x ∈ Cs(Q) satisﬁes ˆhL(x) ≤ c1 max{1, hS,M(s)}, then x is in either the set (9.6) or
the set (9.7).
Let us prove this claim. Suppose x ∈ Cs(Q) is not in (9.6) or (9.7), i.e., ˆhL(x) > c′
1 max{1, hS,M(s)}−

c′
3 and ˆhL(x) > c′′
3. We wish to prove ˆhL(x) > c1 max{1, hS,M(s)}.
We split up to two cases on whether max{1, hS,M(s)} ≤ max{1, 2c′
3/c′
1}.
In the ﬁrst case, i.e., max{1, hS,M(s)} ≤ max{1, 2c′
3/c′
1}, we have

ˆhL(x) > c
′′
3 ≥ c
′′
3 max{1, hS,M(s)}

max{1, 2c′
3/c′
1} = c′′
3
max{1, 2c′
3/c′
1} max{1, hS,M(s)} ≥ c1 max{1, hS,M(s)}.

[9]Alternatively one can also prove Theorem 4.1, up to some ﬁnite set of uniformly bounded cardinality, by
combining (a slight change of) [DGH21, Prop.7.1] and [K¨uh21a, Thm.3] in the same way. Having this extra ﬁnite
set does not matter for Theorem 1.1. We take the current approach to have a “cleaner” statement for the New
Gap Principle.
 26

In the second case, i.e., max{1, hS,M(s)} > max{1, 2c′
3/c′
1}, we have c′
1 max{1, hS,M(s)} − c′
3 ≥
(c′
1/2) max{1, hS,M(s)} and hence

ˆhL(x) > c′
1
2 max{1, hS,M(s)} ≥ c1 max{1, hS,M(s)}.

Hence we are done. □

Now we are ready to prove the New Gap Principle by applying Proposition 9.2 to the family
constructed in §9.1.

Proof of the New Gap Principle (Theorem 4.1). Let C ⊆ ICg → Cg be as in Proposition 9.1.
Then we are in the situation of Proposition 9.2, with (A → S) = (ICg → Cg). Let us now
explain how the line bundles are chosen.
Recall from §4.3 that we have ﬁxed a line bundle L on Jac(Cg/Mg) ample over Mg such that
[−1]∗L ≃ L, and an ample line bundle M over Mg, a compactiﬁcation of Mg. Both line bundles
are deﬁned over Q.
Use the notations in the diagram (9.3).
Set L := p∗
1L for the natural projection p1 : JCg → Jac(Cg/Mg) from (9.3). Then L is a
relatively ample line bundle on A/S such that [−1]∗L ≃ L.
The morphism π : Cg → Mg extends to a morphism π : Cg → Mg deﬁned over Q, with Cg a
suitable compactiﬁcation of Cg. Set M := π∗M.
Now we are ready to invoke Proposition 9.2 and get the following conclusion. For each
P ∈ Cg(Q), we have

(9.9) # {x ∈ CP (Q) : ˆhL(x) ≤ c1 max{1, hCg ,M(P )}
} < c2.

Moreover the ﬁber of ICg → Cg over P ∈ Cg(Q), denoted by (ICg )P , satisﬁes that p1((ICg )P ) =
Jac(Cg/Mg)π(P ) (the ﬁber of Jac(Cg/Mg) → Mg over π(P )). As Jac(Cg/Mg)π(P ) = Jac(Cπ(P ))
for Cπ(P ) deﬁned below (9.2), we then have ˆhL|(ICg )P = ˆhp∗
1L|(ICg )P = ˆhL|Jac(Cπ(P )).

For each s ∈ Mg(Q) and each P ∈ Cs(Q), we have P ∈ Cg(Q) with π(P ) = s. By (9.2),
we have CP = Cs − P . So each x ∈ CP (Q) is Q − P with some Q ∈ Cs(Q). We have seen
ˆhL|(ICg )P = ˆhL|Jac(Cs) from the last paragraph. Moreover hCg,M(P ) = hCg ,π∗M(P ) = hMg,M(s).

Thus (9.9) becomes # {Q − P ∈ Cs(Q) − P : ˆhL(Q − P ) ≤ c1 max{1, hMg ,M(s)}
} < c2. So

# {Q ∈ Cs(Q) : ˆhL(Q − P ) ≤ c1 max{1, hMg ,M(s)}
} < c2,

which is precisely the desired cardinality bound. □

One can recover the weaker statements [DGH21, Prop.7.1] and [K¨uh21a, Thm.3] using the
same argument: instead of Proposition 9.2, it suﬃces to apply the weaker Proposition 7.2
(resp. Proposition 8.3) to the family constructed in §9.1 in order to get [DGH21, Prop.7.1]
(resp. [K¨uh21a, Thm.3]).

9.3. Proof of Uniform Mordell–Lang. We are now ready to prove Theorem 1.1 by a packing
argument using Theorem 3.2 and Theorem 4.1.
A specialization argument using Masser’s result [Mas89] reduces this theorem to F = Q;
see [DGH20, Lem.3.1]. From now on, we may and do assume F = Q.
Let C be a smooth curve of genus g deﬁned over Q, P0 ∈ C(Q) and Γ a subgroup of Jac(C)(Q)
of rank ρ. Then there exists s ∈ Mg(Q) which parametrizes the curve C. Thus the ﬁber of
π : Cg → Mg over s, Cs, is isomorphic to C over Q. We thus view P0 ∈ Cs(Q) ⊆ Cg(Q), and Γ a
subgroup of Jac(Cs)(Q) of rank ρ. Notice that π(P0) = s.
 27

There exists a surjective quasi-ﬁnite ´etale morphism S → Mg such that Cg ×Mg S → S admits
a section. This induces a morphism σ : S → Cg. Thus we can construct the following morphism,

which should be seen as the Abel–Jacobi embedding in family, Cg ×Mg S (id,σ)
−−−→ Cg ×Mg Cg D1−→
Jac(Cg/Mg). For each s ∈ Mg(Q), an irreducible component of the image (which we call C) is
Cs − Ps for some Ps ∈ Cs(Q).
Apply Theorem 3.2 to (A → S) = (Jac(Cg/Mg) → Mg), C, L and M. Then we have

# {
P − Ps ∈ (Cs − Ps)(Q) ∩ Γ : ˆhL(P − Ps) > c max{1, hMg ,M(s)}
} ≤ c
ρ

for some constant c depending only on the family and the line bundles.
Set R := (c max{1, hMg ,M(s)})1/2.

We start by the case where P0 = Ps. Then it remains to prove

(9.10) # {
P − Ps ∈ (Cs − Ps)(Q) ∩ Γ : ˆhL(P − Ps) ≤ c max{1, hMg ,M(s)}
} ≤ c
1+ρ

up to increasing c.
Let c1 and c2 be as in Theorem 4.1. Set r = (c1 max{1, hMg ,M(s)})1/2/2. Consider the real

vector space Γ ⊗ R endowed with the Euclidean norm | · | = ˆh
1/2
L . By an elementary ball packing
argument, any subset of Γ ⊗ R contained in a closed ball of radius R centered at 0 is covered by
at most (1 + 2R/r)ρ closed balls of radius r centered at the elements P − Ps of the given subset

(9.10); see [R´em00a, Lem.6.1]. Thus the number of balls in the covering is at most (1+4
√cc
−1
1 )ρ.
But each closed ball of radius r centered at some P − Ps in (9.10) contains at most c2 elements

by Theorem 4.1. So (9.10) contains at most c2(1 + 4
√cc
−1
1 )ρ ≤ c1+ρ elements for a suitable c.
So we are done for this case.

For arbitrary P0, let Γ′ be the subgroup of Jac(Cs)(Q) generated by Γ and P0 − Ps. Then
rkΓ′ ≤ ρ+ 1. For any P ∈ C(Q)− P0, we have P + P0 − Ps ∈ Cs(Q)− Ps. So #(Cs − P0)(Q)∩ Γ ≤
#(Cs − Ps)(Q) ∩ Γ′, which is ≤ c2+ρ ≤ (c2)1+ρ by the previous case. So we are done by replacing
c with c2.
 10. Further aspects

10.1. Relative Bogomolov Conjecture. In this subsection, we state the Relative Bogomolov
Conjecture and explain how it induces [K¨uh21a, Thm.3], known as the Uniform Bogomolov
Conjecture for curves embedded into Jacobians.
The Relative Bogomolov Conjecture is a folklore conjecture. The formulation we state here
is taken from [DGH20, Conj.1.1].
Let S be an irreducible quasi-projective variety. Let π : A → S be an abelian scheme of
relative dimension g ≥ 1. Let L be a relatively ample line bundle on A/S such that [−1]∗L ≃ L.
Assume that S, π and L are all deﬁned over Q. We thus have a ﬁberwise N´eron–Tate height
ˆhL : A(Q) → [0, ∞) as deﬁned in (2.5).
We will use the following notation. For any subvariety X of A that dominates S, denote by
Xη the geometric generic ﬁber of X. In particular, Aη is an abelian variety over an algebraically
closed ﬁeld.

Conjecture 10.1 (Relative Bogomolov Conjecture). Let X be a subvariety of A deﬁned over
Q that dominates S. Assume that Xη is irreducible and not contained in any proper algebraic
subgroup of Aη. If codimA X > dim S, then there exists ǫ > 0 such that

X(ǫ; L) := {x ∈ X(Q) : ˆhL(x) ≤ ǫ}

is not Zariski dense in X.
 28

The name Relative Bogomolov Conjecture is reasonable: the same statement with ǫ = 0
is precisely the relative Manin–Mumford conjecture proposed by Pink [Pin05, Conj.6.2] and
Zannier [Zan12], which is proved when dim X = 1 in a series of papers [MZ12, MZ14, MZ15,
CMZ18, MZ20]. The Betti map is heavily used in these works.
The classical Bogomolov conjecture, proved by Ullmo [Ull98] and S. Zhang [Zha98a], is pre-
cisely Conjecture 10.1 for dim S = 0. When dim S = 1 and X is the image of a section,
Conjecture 10.1 is equivalent to S. Zhang’s conjecture in his 1998 ICM note [Zha98b, §4] if Aη
is simple and is proved by DeMarco–Mavraki [DM20, Thm.1.4] if A → S is isogenous to a ﬁber
product of elliptic surfaces. The latter proof was simpliﬁed and strengthened by DeMarco–
Mavraki in [DM21]: in [DM20] the authors reduced their Theorem 1.4 to the case of torsion
points treated by [MZ14], whereas in [DM21] the authors proved this result (among other gen-
eralizations [DM21, Thm.1.5]) directly.
K¨uhne [K¨uh21b] recently proved Conjecture 10.1 if A → S is isogenous to a ﬁber product of
elliptic surfaces. In general Conjecture 10.1 is still open. Notice that the proof of Proposition 8.3
can be adapted to show that Conjecture 10.1 holds true for C[m] for some suitable m ≫ 1; see
the conclusion of Step 3.

Using the proof pattern of Proposition 7.2, it is not hard to show that the Relative Bogomolov
Conjecture implies the Uniform Bogomolov Conjecture for curves embedded into Jacobians
[K¨uh21a, Thm.3].

Proposition 10.2. Conjecture 10.1 implies Proposition 8.3, and hence [K¨uh21a, Thm.3] [10] .

Proof. We prove this proposition by induction on dim S. The proof of the base step dim S = 0
is contained in the induction step.
Let C ⊆ A → S and L be from Proposition 8.3. Consider the ﬁbered powers C[M ], A[M ] and
L⊠M over S. As C ̸= A, we have

codimA[M ] C[M ] = M (g − 1) > dim S

for some M ≫ 1. Thus we can apply Conjecture 10.1 to C[M ] ⊆ A[M ] → S and L⊠M to conclude
that C[M ](ǫ; L⊠M ) := {x ∈ C[M ](Q) : ˆhL⊠M (x) ≤ ǫ}
is not Zariski dense in C[M ], for some ǫ > 0.
Set Z to be the Zariski closure of C[M ](ǫ; L⊠M ). Then each irreducible component of S \ π(C[M ] \ Z)
has dimension ≤ dim S − 1. Thus by induction hypothesis, it suﬃces to prove the lemma with
S replaced by S \ π(C[M ] \ Z). Thus we may and do assume the following:

(10.1) For each s ∈ S(Q), we have Zs ̸= CM
s .

By (10.1) and Lemma 7.3, there exists a constant c′′
2 such that the following property holds.
If a subset Σ ⊆ Cs(Q) has cardinality ≥ c′′
2, then ΣM ̸⊆ Zs. This number c′′
2 depends only on
M , the degree of Cs, and the degree of Zs. Hence c′′
2 can be chosen to be independent of s.
Let c′′
3 := ǫ/M , and Σ = {x ∈ Cs(Q) : ˆhL(x) ≤ c′′
3}. It suﬃces to prove #Σ < c′′
2. Suppose
not. Then there exist x1, . . . , xM ∈ Σ such that x := (x1, . . . , xM ) ̸∈ Zs. Then ˆhL⊠M (x) =
∑ ˆhL(xi) ≤ M c′′
3 = ǫ. This contradicts the deﬁnition of Z. Hence we are done. □

10.2. High dimensional subvarieties. Let F be a ﬁeld of characteristic 0 with F = F . In
this subsection, all varieties and line bundles are assumed to be deﬁned over F .
Let A be an abelian variety of dimension g, and let L be an ample line bundle on A. By a
coset in A we mean the translate of an abelian subvariety of A by a point in A(F ).
Let X be a closed irreducible subvariety. Faltings [Fal91] and Hindry [Hin88] proved the
following Mordell–Lang Conjecture. If Γ is a ﬁnite rank subgroup of A(F ), then there exist

[10]See the end of §9.2.
 29

ﬁnitely many x1, . . . , xn ∈ X(F ) ∩ Γ and B1, . . . , Bn abelian subvarieties of A, with xi + Bi ⊆ X
and (xi + Bi)(F ) ∩ Γ not a ﬁnite set for each i, such that

(10.2) X(F ) ∩ Γ =
 n⋃

i=1
(xi + Bi)(F ) ∩ Γ ∐ S

for a ﬁnite set S. In particular, each Bi satisﬁes dim Bi > 0.

Conjecture 10.3. #S ≤ c(g, degL X, degL A)rkΓ+1.

This conjecture is a natural generalization of Theorem 1.1. Indeed, let C be a curve of genus
g ≥ 2 and P0 ∈ C(F ) as in Theorem 1.1. Let Jac(C) be the Jacobian of C and view C − P0
as a curve in Jac(C) via the Abel–Jacobi embedding based at P0. As g ≥ 2, C − P0 does not
contain any positive dimensional coset in Jac(C). Thus for X = C − P0 and A = Jac(C), (10.2)
becomes (C − P0)(F ) ∩ Γ = S. It is a classical result that there exists a line bundle L on Jac(C)
with degL Jac(C) = g! and degL(C − P0) = degL C = g.
[11] Hence Conjecture 10.3 implies
Theorem 1.1.

We will see that Conjecture 10.3 self improves to the following stronger conjecture proposed
by David–Philippon [DP07, Conj.1.8].

Conjecture 10.3′. There exists a partition (10.2) such that n+#S ≤ c(g, degL X, degL A)rkΓ+1.

Let us show that Conjecture 10.3 self improves to Conjecture 10.3′. To do this, we recall the
Ueno locus or the Kawamata locus deﬁned as follows. Consider the union ⋃x+B⊆X(x+B), where
x runs over A(F ) and B runs over abelian subvarieties of A with dim B > 0. Bogomolov [Bog81,
Thm.1] proved that this union is a closed subset of X. Denote by X ◦ its complement in X. It
is not hard to check that the S from (10.2) is X ◦(F ) ∩ Γ.
Set Σ(X; A) to be the set of abelian subvarieties B ⊆ A with dim B > 0 satisfying: x+ B ⊆ X
for some x ∈ A(F ), and B is maximal for this property. Then Bogomolov [Bog81, Thm.1] says
that Σ(X; A) is a ﬁnite set.

Lemma 10.4. If Conjecture 10.3 holds true for all X (in addition to Γ, A and L), then Con-
jecture 10.3′ also holds true.

Proof. For arbitrary X. By Bogomolov [Bog81, Thm.1], each B ∈ Σ(X; A) satisﬁes degL B ≤ c3
for some constant c3 = c3(g, degL X) > 0. Thus #Σ(X; A) ≤ c4 = c4(g, degL X, degL A)
by [R´em00a, Prop.4.1].
The Ueno locus of X deﬁned above is a ﬁnite union ⋃
B∈Σ(X;A)(XB +B), with XB constructed
as follows. Let B⊥ be a complement of B, i.e. B ∩ B⊥ is ﬁnite and B + B⊥ = A. It is possible to
choose such a B⊥ with degL B⊥ ≤ c′
5(g, degL A, degL B); see [MW93]. Set XB := ⋂
b∈B(F )(X −
b) ⋂ B⊥. This intersection must be a ﬁnite intersection (of at most dim X ≤ g members) by
dimension reasons. Recall that degL B ≤ c3(g, degL X). So degL XB ≤ c5(g, degL A, degL X) by
B´ezout’s Theorem. In particular XB has ≤ c5 irreducible components XB,1, . . . , XB,mB .
As the Bi’s in (10.2) satisﬁes xi+Bi ⊆ X and dim Bi > 0, we may and do assume Bi ∈ Σ(X; A)
by deﬁnition of the Ueno locus. It is not hard to check that the ﬁnite set S from (10.2) is
X ◦(F ) ∩ Γ. So (10.2) becomes

(10.3) X(F ) ∩ Γ = ⋃

B∈Σ(X;A)
 nB⋃

j=1
(xB,j + B)(F ) ∩ Γ ∐ S.

[11]In fact, here we do not need the explicit functions in g. So it suﬃces to use the existence of the universal
curve Cg → Mg to conclude that both degL Jac(C) and degL C can be assumed to depend only on g.
 30

Moreover, each xB,j can be chosen to be in X ◦
B(F ) ∩ Γ, where X ◦
B = ⋃mB
k=1 X ◦
B,k. See [R´em00a,
Lem.4.6]; notice that p|XB is ﬁnite for the quotient p : A → A/B. In particular, nB ≤ #X ◦
B(F )∩
Γ. We need to take a closer look at the union in (10.3). First, we have seen #Σ(X; A) ≤
c4(g, degL X, degL A) above.
Next we bound nB for each B ∈ Σ(X; A). Let B ∈ Σ(X; A). Conjecture 10.3 applied
to each irreducible component XB,k of XB says that #X ◦
B,k(F ) ∩ Γ ≤ crkΓ+1 for some c =
c(g, degL XB,k, degL A) > 0. But we have seen that XB has ≤ c5(g, degL A, degL X) components
and that degL XB,k ≤ degL XB ≤ c5(g, degL X) before. So #X ◦
B(F )∩Γ ≤ c6(g, degL X, degL A)rkΓ+1.
In particular, nB ≤ c6(g, degL X, degL A)rkΓ+1 for each B ∈ Σ(X; A).
By (10.3), Conjecture 10.3′ is equivalent to

(10.4) ∑

B∈Σ(X;A) nB + #S ≤ c(g, degL X, degL A)
rkΓ+1.

We have bounded #Σ(X; A) and nB in terms of g, degL X, degL A and rkΓ as desired. It remains
to bound #S. But this is exactly what Conjecture 10.3 claims. Hence we are done. □

A natural question is whether the left hand side of Conjecture 10.3′ can be replaced by degL(X(F ) ∩
Γ)
Zar, which is ∑n
i=1 degL Bi + #S in view of (10.2) for some well-chosen Bi. Unfortunately this is not
possible in general, because in the proof of Lemma 10.4 (B(F ) ∩ Γ)
Zar could be any abelian subvariety of
B and hence we cannot expect a bound for its degree. For example, let X = A = E2 be the square of an
elliptic curve deﬁned over Q. The graph EN ⊆ E2 of [N ] : E → E then has degree N 2. Take a subgroup
Γ of EN (Q) of rank 1, then deg(X(Q) ∩ Γ)
Zar = deg EN = N 2. This provides a counterexample.
However, the proof of Lemma 10.4 suggests that this is the only obstacle. In fact, as degL B ≤
c3(g, degL X) for each B ∈ Σ(X; A), in the proof (10.4) can be improved to ∑B∈Σ(X;A) nB degL B+#S ≤
c(g, degL X, degL A)
rkΓ+1. Thus if Conjecture 10.3 holds true for all X and Γ (in addition to A and L),
then the following conjecture holds true.[12]

Conjecture 10.3′′. If Γ is saturate for each B ∈ Σ(X; A), i.e. (B(F )∩Γ)
Zar = B for each B ∈ Σ(X; A),
then degL(X(F ) ∩ Γ)
Zar ≤ c(g, degL X, degL A)
rkΓ+1.

On the other hand, Conjecture 10.3′′ implies both Conjecture 10.3 and Conjecture 10.3′. Indeed by
dimension reasons and the assumption F = F , for any ﬁnite rank subgroup Γ of A(F ) and any abelian
subvariety B of A, there exists a subgroup ΓB ⊇ Γ of rank ≤ rkΓ + dim B ≤ rkΓ + g such that ΓB is
saturate for B. Applying this successively to each B ∈ Σ(X; A), we get a subgroup ΓX ⊇ Γ of rank
≤ rkΓ + g#Σ(X; A) ≤ rkΓ + g · c4(g, degL X, degL A) which is saturate for all B ∈ Σ(X; A). Assume
Conjecture 10.3
′′. Then ∑
B∈Σ(X;A) nB degL B + #S ≤ c(g, degL X, degL A)
rkΓX +1 ≤ crkΓ+gc4+1 ≤
(cgc4+1)
rkΓ+1. Thus n + #S = ∑B∈Σ(X;A) nB + #S ≤ (cgc4+1)
rkΓ+1. Hence Conjecture 10.3′ and
Conjecture 10.3 both hold true with c replaced by cgc4+1.

As in the case of curves, to prove Conjecture 10.3 it suﬃces to work with F = Q by a standard
specialization argument using Masser’s result [Mas89]. So from now on we assume F = Q. We
also assume that L is symmetric; this can be achieved by replacing L by L ⊗ [−1]∗L (and
degL⊗[−1]∗L(X) = 2dim X degL(X)).
R´emond proved the generalized Vojta’s Inequality [R´em00b, Thm.1.2] for points in X ◦(Q)
and the generalized Mumford’s Inequality [R´em00a, Thm.3.2] for points in X ◦(Q) ∩ Γ. As in
the case for curves, these two generalized inequalities also yield the desired bound (the one in
Conjecture 10.3) for the number of large points in X ◦(Q)∩ Γ. A modiﬁed version of these results
then reduces Conjecture 10.3 to studying the small points, i.e. to prove a bound in the form of

(10.5) {P ∈ X ◦(Q) ∩ Γ : ˆhL(P ) ≤ c max{1, hFal(A)}
} ≤ c
rkΓ+1

[12]Conjecture 10.3
′′ is suggested to me by Dan Abramovich.
 31

for some c = c(g, degL X, degL A) > 0. We refer to [DP07, Thm.6.8] for this reduction.
[13]

But one can and should do one more step. Let A′ be the abelian subvariety of A generated
by X − X. Then X ⊆ A′ + Q for some Q ∈ A(Q). The subgroup Γ′ of A(Q) generated by
Γ and Q has rank ≤ rkΓ + 1. We have (X − Q)◦ = X ◦ − Q by deﬁnition of the Ueno locus,
(X ◦(Q) − Q) ∩ Γ ⊆ (X ◦(Q) − Q) ∩ Γ′ = X ◦(Q) ∩ Γ′ and degL(X − Q) = degL X. So we may
replace X by X − Q, A by A′ and Γ by Γ′ ∩ A′(Q) and the constant c in the conclusion by c2.
Thus Conjecture 10.3 is reduced to the following bound: Assume X generates A, then

(10.6) {P ∈ X ◦(Q) ∩ Γ : ˆhL(P ) ≤ c max{1, hFal(A)}
} ≤ c
rkΓ+1

for some c = c(g, degL X, degL A) > 0.

The following conjecture is a natural generalization of the New Gap Principle to high dimen-
sional cases. Recall X ◦ deﬁned above Lemma 10.4.

Conjecture 10.5. Assume that X generates A. There exist constants c1 = c1(g, degL X, degL A) >
0 and c2 = c2(g, degL X, degL A) > 0 satisfying the following property. For each P0 ∈ X ◦(Q),
the set

(10.7) {
P ∈ X ◦(Q) : ˆhL(P − P0) ≤ c1 max{1, hFal(A)}
}

is contained in a proper Zariski closed subset X ′ ⊊ X with degL X ′ < c2.

This conjecture is equivalent to the following conjecture, because (X − P0)◦ = X ◦ − P0 and
degL(X − P0) = degL X.

Conjecture 10.5′. Assume that X generates A. There exist constants c1 = c1(g, degL X, degL A) >
0 and c2 = c2(g, degL X, degL A) > 0 satisfying the following property. The set

(10.8) {P ∈ X ◦(Q) : ˆhL(P ) ≤ c1 max{1, hFal(A)}
}

is contained in a proper Zariski closed subset X ′ ⊊ X with degL X ′ < c2.

If Conjecture 10.5′ holds true for all A, X and L, then one can also handle points on the Ueno
locus by induction.
It is not hard to prove that Conjecture 10.5 implies (10.6) by induction on dim X and the
standard packing argument as presented in §9.3. Thus we have

Proposition 10.6. If Conjecture 10.5 (or Conjecture 10.5′) holds true, then Conjecture 10.3
holds true.

Let us brieﬂy explain why the assumption “X generates A” is added in Conjecture 10.5
and Conjecture 10.5′. Suppose X is contained in a proper abelian subvariety A′ of A, and
A = A′ × A′′. Then hFal(A) = hFal(A′) + hFal(A′′). We are free to create examples with hFal(A′′)
arbitrarily large, and (10.8) ultimately says that all points in X ◦(Q) are actually contained in a
proper Zariski closed subset of X. This is impossible.
Next let us brieﬂy explain why we do not directly conjecture the set (10.8) to have cardinality
< c2. Suppose A = B × J a product of two abelian varieties and X = Y × C, with Y ⊆ B
and C ⊆ J the Abel–Jacobi embedding of a curve of genus ≥ 2 via some point; in particular
0J ∈ C(Q). It is possible to choose an appropriate ample line bundle L := LB ⊠ LJ such that
degLJ J = g! and degLJ C = g. Then for each y ∈ Y ◦(Q), we have (y, 0J ) ∈ X ◦(Q). It is
possible to choose C and J with hFal(J) arbitrarily large. If the set (10.8) has cardinality < c2,
then this yields #Y ◦(Q) < ∞, and this is not true in general. Notice that in this example, the

[13]The constants cNT and h1 in [DP07] are bounded by max{1, hFal(A)} by an argument similar to [DGH21,
(8.4) and (8.7)].
 32

statement of Conjecture 10.5′ can be related to the New Gap Principle for curves embedded into
Jacobians (Theorem 4.1).
Finally, we remark that the problems revealed by both examples above do not occur if we
only consider the setup for Uniform Bogomolov, i.e. replace c1 max{1, hFal(A)} from (10.8) by a
constant c3. Indeed, in both examples above, eventually what prevents us to get a more general
statement for Conjecture 10.5′ is the fact hFal(A) can be arbitrarily large.

References

[Abr95] Dan Abramovich. Uniformit´e des points rationnels des courbes alg´ebriques sur les extensions quadra-
tiques et cubiques. Comptes Rendus de l’Academie des Sciences-Serie I-Mathematique, 321(6):755–758,
1995.
[ACZ20] Yves Andr´e, Pietro Corvaja, and Umberto Zannier. The Betti map associated to a section of an abelian
scheme (with an appendix by Z. Gao). Inv. Math., 222:161–202, 2020.
[Alp18] L. Alpoge. The average number of rational points on genus two curves is bounded. arXiv:1804.05859,
2018.
[Alp20] L. Alpoge. Points on Curves. PhD thesis, Princeton University, 2020.
[BBB
+21] J.S. Balakrishnan, A. Best, F. Bianchi, B. Lawrence, J.S. M¨uller, N. Triantaﬁllou, and J. Vonk.
Two recent p-adic approaches towards the (eﬀective) Mordell conjecture. In Arithmetic L-Functions
and Diﬀerential Geometric Methods: Regulators IV, May 2016, Paris, volume 338 of Progr. Math.
Birkh¨auser Basel, 2021.
[BG06] E. Bombieri and W. Gubler. Heights in Diophantine Geometry. Cambridge University Press, 2006.
[Bog81] F. Bogomolov. Points of ﬁnite order on an abelian variety. Izv. Math., 17:55–72, 1981.
[Bom90] E. Bombieri. The mordell conjecture revisited. Annali della Scuola Normale Superiore di Pisa-Classe
di Scienze, 17(4):615–640, 1990.
[CGHX21] S. Cantat, Z. Gao, P. Habegger, and J. Xie. The geometric Bogomolov conjecture. Duke Math. J.,
170:247–277, 2021.
[Cha41] C. Chabauty. Sur les points rationnels des courbes alg´ebriques de genre sup´erieur `a l’unit´e. C. R.
Acad. Sci. Paris, 212:882–885, 1941.
[CHM97] L. Caporaso, J. Harris, and B. Mazur. Uniformity of rational points. J. Amer. Math. Soc., 10(1):1–35,
1997.
[CHM21] L. Caporaso, J. Harris, and B. Mazur. Corrections to Uniformity of rational points and further com-
ments. arXiv: 2012.14461, 2021.
[CMZ18] P. Corvaja, D. Masser, and U. Zannier. Torsion hypersurfaces on abelian schemes and Betti coordi-
nates. Mathematische Annalen, 371(3):1013–1045, 2018.
[Col85] R. .F. Coleman. Eﬀective Chabauty. Duke Math. J., 52(3):765–770, 1985.
[CVV17] S. Checcoli, F. Veneziano, and E. Viada. On the explicit torsion anomalous conjecture. Trans. Amer.
Math. Soc., 369(9):6465–6491, 2017.
[CVV19] S. Checcoli, F. Veneziano, and E. Viada. The eﬀective mordell conjecture for families of curves. Forum
of Mathematics Sigma, 7:e31, 2019.
[dD97] T. de Diego. Points rationnels sur les familles de courbes de genre au moins 2. J. Number Theory,
67(1):85–114, 1997.
[DGH19] V. Dimitrov, Z. Gao, and P. Habegger. Uniform bound for the number of rational points on a pencil
of curves. Int. Math. Res. Not. IMRN, (rnz248):https://doi.org/10.1093/imrn/rnz248, 2019.
[DGH20] V. Dimitrov, Z. Gao, and P. Habegger. A consequence of the relative Bogomolov conjecture. Journal
of Number Theory (Prime), Proceedings of the First JNT Biennial Conference 2019, 2020.
[DGH21] V. Dimitrov, Z. Gao, and P. Habegger. Uniformity in Mordell–Lang for curves. Annals of Mathematics,
194(1):237–298, 2021.
[DKY20] L. DeMarco, H. Krieger, and H. Ye. Uniform Manin-Mumford for a family of genus 2 curves. Ann. of
Math., 191:949–1001, 2020.
[DM69] P. Deligne and D. Mumford. The irreducibility of the space of curves of given genus. Inst. Hautes
´Etudes Sci. Publ. Math., (36):75–109, 1969.
[DM20] L. DeMarco and N.M. Mavraki. Variation of canonical height and equidistribution. American Journal
of Mathematics, 142(2):443–473, 2020.
[DM21] L. DeMarco and N.M. Mavraki. Elliptic surfaces and arithmetic equidistribution for R-divisors on
curves. arXiv: 2012.14529, 2021.
[DNP07] S. David, M. Nakamaye, and P. Philippon. Bornes uniformes pour le nombre de points rationnels de
certaines courbes. In Diophantine geometry, volume 4 of CRM Series, pages 143–164. Ed. Norm., Pisa,
2007.
 33

[DP02] S. David and P. Philippon. Minorations des hauteurs normalis´ees des sous-vari´et´es de vari´et´es abeli-
ennes. II. Comment. Math. Helv., 77(4):639–700, 2002.
[DP07] S. David and P. Philippon. Minorations des hauteurs normalis´ees des sous-vari´et´es des puissances des
courbes elliptiques. Int. Math. Res. Pap. IMRP, (3):Art. ID rpm006, 113, 2007.
[Fal83] G. Faltings. Endlichkeitss¨atze f¨ur abelsche variet¨aten ¨uber zahlk¨orpern. Inventiones mathematicae,
73(3):349–366, 1983.
[Fal91] G. Faltings. Diophantine approximation on abelian varieties. Ann. of Math. (2), 133(3):549–576, 1991.
[Gao20a] Z. Gao. Generic rank of Betti map and unlikely intersections. Compos. Math., 156(12):2469–2509,
2020.
[Gao20b] Z. Gao. Mixed Ax-Schanuel for the universal abelian varieties and some applications. Compos. Math.,
156(11):2263–2297, 2020.
[Gao21] Z. Gao. Distribution of points on varieties: various aspects and interactions. HDR (Habilitation `a
Diriger des Recherches), Sorbonne Universit´e, 2021.
[GH19] Z. Gao and P. Habegger. Heights in Families of Abelian Varieties and the Geometric Bogomolov
Conjecture. Ann. of Math., 189(2):527–604, 2019.
[GN09] A. Genestier and B.C. Ngˆo. Lecture on Shimura varieties. In Autour de motifs, Ecole d’´et´e Franco-
Asiatique de G´eom´etrie Alg´ebrique et de Th´eorie des Nombres/Asian-French Summer School on Al-
gebraic Geometry and Number Theory. Vol. I, pages 187–236. Panor. Synth`ese 29, Soc. Math. France,
2009.
[Hab13] P. Habegger. Special Points on Fibered Powers of Elliptic Surfaces. J.Reine Angew. Math., 685:143–
179, 2013.
[Hin88] M. Hindry. Autour d’une conjecture de Serge Lang. Invent. Math., 94(3):575–603, 1988.
[Hin98] M. Hindry. Introduction to abelian varieties and the Mordell-Lang conjecture, pages 85–100. Springer
Berlin Heidelberg, 1998.
[HP16] P. Habegger and J. Pila. O-minimality and certain atypical intersections. Ann. Sci. ´Ecole Norm. Sup.,
49:813–858, 2016.
[HS00] M. Hindry and J.H. Silverman. Diophantine Geometry An Introduction. Springer, 2000.
[KRZB16] E. Katz, J. Rabinoﬀ, and D. Zureick-Brown. Uniform bounds for the number of rational points on
curves of small Mordell-Weil rank. Duke Math. J., 165(16):3189–3240, 2016.
[K¨uh21a] L. K¨uhne. Equidistribution in families of abelian varieties and uniformity. arXiv: 2101.10272, 2021.
[K¨uh21b] L. K¨uhne. The Relative Bogomolov Conjecture for ﬁbered products of elliptic surfaces. arXiv:
2103.06203, 2021.
[LSW21] N. Looper, J. Silverman, and R. Wilms. An uniform quantitative Manin–Mumford-type theorem for
curves over function ﬁelds. arXiv: 2101.11593v2, 2021.
[Mas89] D. Masser. Specializations of ﬁnitely generated subgroups of abelian varieties. Trans. Amer. Math.
Soc., 311(1):413–424, 1989.
[Maz86] B. Mazur. Arithmetic on curves. Bulletin of the American Mathematical Society, 14(2):207–259, 1986.
[Maz00] B. Mazur. Abelian varieties and the Mordell-Lang conjecture. In Model theory, algebra, and geometry,
volume 39 of Math. Sci. Res. Inst. Publ., pages 199–227. Cambridge Univ. Press, Cambridge, 2000.
[MFK94] D. Mumford, J. Fogarty, and F. Kirwan. Geometric invariant theory, volume 34 of Ergebnisse der
Mathematik und ihrer Grenzgebiete (2) [Results in Mathematics and Related Areas (2)]. Springer-
Verlag, Berlin, third edition, 1994.
[Mok91] N. Mok. Aspects of K¨ahler geometry on arithmetic varieties. In Several complex variables and complex
geometry, Part 2 (Santa Cruz, CA, 1989), volume 52 of Proc. Sympos. Pure Math., pages 335–396.
Amer. Math. Soc., Providence, RI, 1991.
[MW93] D.W. Masser and G. W¨ustholz. Periods and minimal abelian subvarieties. Ann. Math., 137:407–458,
1993.
[MZ12] D. Masser and U. Zannier. Torsion points on families of squares of elliptic curves. Mathematische
Annalen, 352(2):453–484, 2012.
[MZ14] D. Masser and U. Zannier. Torsion points on families of products of elliptic curves. Advances in
Mathematics, 259:116 – 133, 2014.
[MZ15] D. Masser and U. Zannier. Torsion points on families of simple abelian surfaces and Pell’s equation
over polynomial rings (with an appendix by E. V. Flynn). Journal of the European Mathematical
Society, 17:2379–2416, 2015.
[MZ20] D. Masser and U. Zannier. Torsion points, Pell’s equation, and integration in elementary terms. Acta
Mathematica, 225(2):227–312, 2020.
[OS80] F. Oort and J. Steenbrink. The local Torelli problem for algebraic curves. In Journ´ees de G´eometrie
Alg´ebrique d’Angers, Juillet 1979/Algebraic Geometry, Angers, 1979, pages 157–204. Sijthoﬀ & No-
ordhoﬀ, Alphen aan den Rijn—Germantown, Md., 1980.
 34

[Pac97] P. Pacelli. Uniform boundedness for rational points. Duke Math. J., 88:77–102, 1997.
[Paz15] F. Pazuki. Bornes sur le nombre de points rationnels des courbes – en quˆete d’uniformit´e, with an
appendix by s. david and p. philippon. Contemp. Math., to appear, 2015.
[Paz17] F. Pazuki. Probl`emes d’arithm´etique sur les vari´et´es ab´eliennes. HDR (Habilitation `a Diriger des
Recherches), Universit´e de Bordeaux, 2017.
[Pin89] R. Pink. Arithmetical compactiﬁcation of mixed Shimura varieties. PhD thesis, Bonner Mathematische
Schriften, 1989.
[Pin05] R. Pink. A Common Generalization of the Conjectures of Andr´e-Oort, Manin-Mumford, and Mordell-
Lang. Preprint, page 13pp, 2005.
[Ray70] M. Raynaud. Faisceaux amples sur les sch´emas en groupes et les espaces homog`enes. Lecture Notes in
Mathematics, Vol. 119. Springer-Verlag, Berlin-New York, 1970.
[Ray83a] M. Raynaud. Around the Mordell conjecture for function ﬁelds and a conjecture of Serge Lang. In
Michel Raynaud and Tetsuji Shioda, editors, Algebraic Geometry, pages 1–19, Berlin, Heidelberg,
1983. Springer Berlin Heidelberg.
[Ray83b] M. Raynaud. Sous-vari´et´es d’une vari´et´e ab´elienne et points de torsion. In Arithmetic and geometry,
Vol. I, volume 35 of Progr. Math., pages 327–352. Birkh¨auser Boston, Boston, MA, 1983.
[R´em00a] G. R´emond. D´ecompte dans une conjecture de Lang. Invent. Math., 142(3):513–545, 2000.
[R´em00b] G. R´emond. In´egalit´e de Vojta en dimension sup´erieure. Ann. Scuola Norm. Sup. Pisa Cl. Sci. (4),
29(1):101–151, 2000.
[R´em10] G. R´emond. Nombre de points rationnels des courbes. Proc. Lond. Math. Soc. (3), 101(3):759–794,
2010.
[Ser13] J.P. Serre. Lectures on the Mordell-Weil Theorem. Aspects of Mathematics. Vieweg+Teubner Verlag,
2013.
[Sil83] J.H. Silverman. Heights and the specialization map for families of abelian varieties. J. Reine Angew.
Math., 342:197–211, 1983.
[Sil93] J. H. Silverman. A uniform bound for rational points on twists of a given curve. J. London Math. Soc.
(2), 47(3):385–394, 1993.
[Sil11] J. H. Silverman. Height estimates for equidimensional dominant rational maps. J. Ramanujan Math.
Soc., 26(2):145–163, 2011.
[Sto19] M. Stoll. Uniform bounds for the number of rational points on hyperelliptic curves of small mordell-weil
rank. J. Eur. Math. Soc. (JEMS), 21:923–956, 2019.
[Ull98] E. Ullmo. Positivit´e et discr`etion des points alg´ebriques des courbes. Ann. of Math. (2), 147(1):167–
179, 1998.
[Voj91] P. Vojta. Siegel’s theorem in the compact case. Ann. of Math. (2), 133(3):509–548, 1991.
[VV20] F. Veneziano and E. Viada. Explicit height bounds for k-rational points on transverse curves in powers
of elliptic curves. Paciﬁc Journal of Mathematics (to appear), 2020.
[YZ21] X. Yuan and S. Zhang. Adelic line bundles over quasi-projective varieties. arXiv, 2021.
[Zan12] U. Zannier. Some problems of unlikely intersections in arithmetic and geometry, volume 181 of Annals
of Mathematics Studies. Princeton University Press, Princeton, NJ, 2012. With appendixes by David
Masser.
[Zha98a] S. Zhang. Equidistribution of small points on abelian varieties. Ann. of Math. (2), 147(1):159–165,
1998.
[Zha98b] S Zhang. Small points and Arakelov theory. In Proceedings of the International Congress of Mathe-
maticians. Volume II, pages 217–225, 1998.

CNRS, IMJ-PRG, 4 place Jussieu, 75005 Paris, France
Email address: ziyang.gao@imj-prg.fr
