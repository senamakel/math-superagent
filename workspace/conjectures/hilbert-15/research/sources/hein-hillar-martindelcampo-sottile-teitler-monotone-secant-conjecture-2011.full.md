<!-- source: https://arxiv.org/pdf/1109.3436 | converted from PDF -->

arXiv:1109.3436v3  [math.AG]  19 Oct 2014
THE MONOTONE SECANT CONJECTURE IN THE
REAL SCHUBERT CALCULUS

NICKOLAS HEIN, CHRISTOPHER J. HILLAR, ABRAHAM MART´IN DEL CAMPO,
FRANK SOTTILE, AND ZACH TEITLER

Abstract. The monotone secant conjecture posits a rich class of polynomial systems,
all of whose solutions are real. These systems come from the Schubert calculus on ﬂag
manifolds, and the monotone secant conjecture is a compelling generalization of the Shapiro
conjecture for Grassmannians (Theorem of Mukhin, Tarasov, and Varchenko). We present
some theoretical evidence for this conjecture, as well as computational evidence obtained
by 1.9 teraHertz-years of computing, and we discuss some of the phenomena we observed in
our data.
 1. Introduction

A system of real polynomial equations with ﬁnitely many solutions has some, but likely
not all, of its solutions real. In fact, sometimes the structure of the equations implies an
upper bound on the number of real solutions [2, 12], ensuring that not all solutions are real.
The monotone secant conjecture posits a family of systems of polynomial equations with the
extreme property that all of their solutions are real.
The Shapiro conjecture asserts that a zero-dimensional intersection of Schubert subvari-
eties of a Grassmannian consists only of real points provided that the Schubert varieties are
given by ﬂags tangent to a real rational normal curve. While the statement concerns the
Schubert calculus on Grassmannians, its proofs involve complex analysis [5, 6] or integrable
systems and representation theory [14, 15]. A complete story of this conjecture and its proof
can be found in [20].
The Shapiro conjecture is false for non-Grassmannian ﬂag manifolds, but in a very inter-
esting manner. This failure was ﬁrst noticed in [18] and systematic computer experimen-
tation suggested a correction, the monotone conjecture [17, 19], that appears to be valid
for ﬂag manifolds of type A. Eremenko, Gabrielov, Shapiro, and Vainshtein [7] proved a re-
sult that implies the monotone conjecture for some manifolds of two-step ﬂags and concerns
codimension-two subspaces that meet ﬂags which are secant to the rational normal curve

1991 Mathematics Subject Classiﬁcation. 14M25, 14P99.
Key words and phrases. Shapiro conjecture, Schubert calculus, ﬂag manifold.
Research supported in part by NSF grants DMS-0701050, DMS-0915211, and DMS-1001615.
Research of Hillar supported in part by an NSF Postdoctoral Fellowship and an NSA Young Investigator
grant.
This research conducted in part on computers provided by NSF SCREMS grant DMS-0922866.

1

2 HEIN, HILLAR, MART´IN DEL CAMPO, SOTTILE, AND TEITLER

along disjoint intervals. This suggested the secant conjecture, which asserts that an intersec-
tion of Schubert varieties in a Grassmannian is transverse with all points real, provided that
the Schubert varieties are deﬁned by ﬂags secant to a rational normal curve along disjoint
intervals. This was posed and evidence was presented for its validity in [10].
The monotone secant conjecture is a common extension of both the monotone conjecture
and the secant conjecture. It is also the last of the conjectures our group has made concerning
reality in Schubert calculus of osculating ﬂags. In addition to those mentioned, there is a
version of the Shapiro conjecture for the orthogonal Grassmannian which was proven by
Purbhoo [16], and a version for the Lagrangian Grassmannian described in [21, Ch. 14.2].
Exploratory computations in other ﬂag manifolds suggest there is no regularity in the number
of real solutions to Schubert calculus problems given by osculating ﬂags.
We give here an open instance of the monotone secant conjecture, expressed as a system
of polynomial equations in local coordinates for the variety of ﬂags E2 ⊂ E3 in C5, where
dim Ei = i. Let x1, . . . ,x8 be indeterminates and consider the polynomials

(1.1) f (s,t,u; x) := det
 







1 0 x1 x2 x3
0 1 x4 x5 x6
1 s s2 s3 s4

1 t t
2 t
3 t
4

1 u u2 u3 u4






 , g(v,w; x) := det
 







1 0 x1 x2 x3
0 1 x4 x5 x6
0 0 1 x7 x8
1 v v2 v3 v4

1 w w2 w3 w4






 ,

which depend upon parameters s,t,u and v,w respectively.

Conjecture 1.1. Let s1 < t1 < u1 < · · · < s4 < t4 < u4 < v1 < w1 < · · · < v4 < w4 be real
numbers. Then the system of polynomial equations

f (s1,t1,u1; x) = f (s2,t2,u2; x) = f (s3,t3,u3; x) = f (s4,t4,u4; x) = 0(1.2) g(v1,w1; x) = g(v2,w2; x) = g(v3,w3; x) = g(v4,w4; x) = 0

has twelve solutions, and all of them are real.

These equations have geometric meaning. Let E2 be the span of the ﬁrst two rows of either
matrix and E3 the span of the ﬁrst three rows of the second matrix that deﬁnes g. Then
E2 ⊂ E3 is a general ﬂag. If we let F3(s,t,u) be the span of the last three rows of the matrix
for f , then this is a 3-plane that is secant to the rational normal curve γ : y ↦→ (1,y,y2,y3,y4)
at the points γ(s),γ(t),γ(u). The equation f (s,t,u; x) = 0 is the condition that E2 meet
F3(s,t,u) non-trivially. Smilarly, if F2(u,v) is the span of the last two rows of the second
matrix, which is 2-plane secant to γ at γ(u) and γ(v), then the equation g(v,w; x) = 0 is the
condition that E3 meet F2(u,v) non-trivially.
The monotonicity hypothesis is that the four 3-planes given by si,ti, ui are secant along
intervals [si,ui] which are pairwise disjoint and occur before the pairwise disjoint intervals
[vi, wi] where the 2-planes are secant. If the order of the intervals [s4,u4] and [v1, w1] is
reversed, the evaluation is no longer monotone. We tested 3,000,000 instances of Conjec-
ture 1.1, ﬁnding only real solutions. In contrast, we tested 21,000,000 with the monotonicity
condition violated, of which 18,085,537 had some non real solutions.

MONOTONE SECANT CONJECTURE 3

We formulate the monotone secant conjecture, explain its relation to the other reality
conjectures, describe data supporting it from a large computational experiment, and discuss
some features observed in our data that go beyond the monotone secant conjecture. This
experiment veriﬁed the monotone secant conjecture in each of the 768,846,000 instances it
tested. We have created a website [9] for viewing the data online. This includes pages for
browsing the data and viewing the results for each Schubert problem. We only sketch the
other reality conjectures, for they are described in the cited literature, and we also only sketch
the design and execution of this experiment, for the purpose of the paper [11] was to present
the software environment we developed for such distributed computational experiments.
This paper is organized as follows. In Section 2 we illustrate the main point of the
monotone secant conjecture through the classical problem of four lines. Section 3 is a primer
on ﬂag manifolds and contains a precise statement of the monotone secant conjecture while
also explaining its relation to the Shapiro, secant, and monotone conjectures. In Section 4 we
expand on the relation between the monotone secant and monotone conjectures, discuss the
experimental evidence for the monotone secant conjecture, and some phenomena we observed
in our data. Lastly, in Section 5 we sketch the methods we used to test the conjecture.

2. The problem of four lines

The classical problem of four lines asks for the ﬁnitely many lines m that meet four given
general lines ℓ1, ℓ2, ℓ3, ℓ4 in (projective) three-space. This has a pleasing synthetic solution,
which leads to the ﬁrst interesting case of the monotone secant conjecture.
Three general lines ℓ1, ℓ2, ℓ3 lie in one ruling of a doubly-ruled quadric surface Q, with
the other ruling consisting of all lines that meet the ﬁrst three. The line ℓ4 meets Q in two
points, and through each of these points there is a line in the second ruling. These two lines,
m1 and m2, are the solutions to this problem. If the lines ℓ1, ℓ2, ℓ3, ℓ4 are real, then so is
Q, but the intersection of Q with ℓ4 is either two real points or a pair of complex conjugate
points. In the ﬁrst case, the problem of four lines has two real solutions, while in the second,
it has no real solutions.
Let us consider a variant in the manifold of ﬂags consisting of a line m lying on a plane M
in 3-space, m ⊂ M. Consider the Schubert problem in which m meets three lines ℓ1, ℓ2, ℓ3
and M contains two points, p and q. Then M contains the aﬃne span p,q of p and q. Since
m ⊂ M, we must have that m also meets p,q and is therefore a solution to the problem of
four lines given by ℓ1, ℓ2, ℓ3 and p,q. As M is spanned by m and p,q, we see that solving
this auxiliary problem of four lines solves our original Schubert problem. Furthermore, if the
lines and points are real, then a solution m ⊂ M is real if and only if m is real.
Suppose that the three lines are secant to a rational normal curve γ along disjoint intervals
and the points are p = γ(s) and q = γ(t), which do not lie in any interval of secancy. There
are two possible combinatorial placements of the two points. Removing the three intervals
of secancy from γ results in three disjoint intervals along γ ≃ RP1. Either both points γ(s)
and γ(t) lie in the same interval or they lie in diﬀerent intervals. We examine each case.

4 HEIN, HILLAR, MART´IN DEL CAMPO, SOTTILE, AND TEITLER

Fixing secant lines ℓ1, ℓ2, ℓ3, the quadric Q described above is a hyperboloid of one sheet.
This is displayed in Figures 1 and 2, along with γ and the lines. Suppose that γ(s) and γ(t)
lie in the same interval, say I, as indicated in Figure 1. Then the secant line they span,

γ ❍❍❍❥
 ✻

I
 Q

Figure 1. The problem of four secant lines.
ℓ(s,t), lies in the direction of I and meets the hyperboloid Q in two real points. Thus, in
this ﬁrst case, our Schubert problem has two real solutions. (This is also an instance of the
secant conjecture, which holds for this problem of four lines [10, §4].)
In the second case, where the points γ(s) and γ(t) do not lie in the same interval, it is
possible to have no real solutions. Consider the choice of points γ(s) and γ(t) as shown
in Figure 2, so that the secant line ℓ(s,t) does not meet the quadric Q. By our previous

γ ❍
❍❍❥
 ✲ℓ(s,t) Q

Figure 2. A non-monotone evaluation.

analysis, there will be no real lines m meeting these four secant lines, and therefore no real
solutions m ⊂ M to our Schubert problem.
We conclude that the positions of the points γ(s),γ(t) relative to the other intervals of
secancy may aﬀect whether or not the solutions are real. The schematic in Figure 3 illustrates
the relative positions of the secancies along γ (which is homeomorphic to the circle). The
idea behind the monotone secant conjecture is to attach to each interval the dimension of
that part of the ﬂag which it aﬀects. This is 1 for m and 2 for M. The schematic on the left
has labels 1,1,1,2,2, reading clockwise, starting just past the point s, while that on the right
reads 1,1,2,1,2. The labels increase monotonically in the ﬁrst and do not in the second.

MONOTONE SECANT CONJECTURE 5

s t
All solutions real
 s t

Not all solutions real

Figure 3. Schematic for the secancies.

3. Background

We develop the background for the statement of the monotone secant conjecture, deﬁning
ﬂag varieties and their Schubert problems. More may be found in the book of Fulton [8].
Fix positive integers a• := (a1 < · · · < ak) and n with ak < n. A ﬂag E• of type a• is a
sequence of subspaces

E• : {0} ⊂ Ea1 ⊂ Ea2 ⊂ · · · ⊂ Eak ⊂ Cn , where dim(Eai) = ai .

The set of all such ﬂags forms the ﬂag manifold Fℓ(a•; n), which has dimension dim(a•) :=
∑k
i=1(n − ai)(ai − ai−1), where a0 := 0. When a• = (a) is a singleton, Fℓ(a•; n) is the
Grassmannian of a-planes in Cn, written Gr(a,n). Flags of type 1 < 2 < · · · < n − 1 in Cn

are complete.
The positions of ﬂags relative to a ﬁxed complete ﬂag F• stratify Fℓ(a•; n) into topological
cells whose closures are Schubert varieties. These positions are indexed by certain permu-
tations. The descent set δ(σ) of a permutation σ ∈ Sn is the set of numbers i such that
σ(i) > σ(i+1). For a permutation σ ∈ Sn with δ(σ) ⊂ a•, the Schubert variety XσF• is

XσF• = {E• ∈ Fℓ(a•; n) | dim Eai ∩ Fj ≥ #{l ≤ i | j + σ(l) > n} ∀i,j}.

Flags E• in XσF• have position σ relative to F•. A permutation σ with descent set contained
in a• is a Schubert condition on ﬂags of type a•. The Schubert variety XσF• is irreducible
with codimension ℓ(σ) := |{i < j | σ(i) > σ(j)}|. A Schubert problem for Fℓ(a•; n) is a list
σ := (σ1, . . . , σm) of Schubert conditions for Fℓ(a•; n) satisfying ℓ(σ1)+· · ·+ℓ(σm) = dim(a•).
Given a Schubert problem σ for Fℓ(a•; n) and complete ﬂags F 1
• , . . . , F m
• , the intersection

(3.1) Xσ1F 1
• ∩ · · · ∩ XσmF m
•

is an instance of σ. When the ﬂags are in general position, this intersection is transverse and
zero-dimensional [13], and it consists of all ﬂags E• ∈ Fℓ(a•; n) having position σi relative to
F i
•, for each i = 1, . . . , m. Such a ﬂag E• is a solution to this instance of σ.
The degree of a zero-dimensional intersection (3.1) is independent of the choice of the ﬂags
and we call this number d(σ) the degree of the Schubert problem σ. When the intersection
is transverse, the number of solutions to σ equals its degree.

6 HEIN, HILLAR, MART´IN DEL CAMPO, SOTTILE, AND TEITLER

When the ﬂags F 1
• , . . . , F m
• are real, the solutions to the Schubert problem need not be
real. The monotone secant conjecture posits a method to select the ﬂags F• so that all
solutions are real, for a certain class of Schubert problems.
Let γ : R → Rn be a rational normal curve, which is any curve aﬃnely equivalent to the
moment curve t ↦→ (1,t,t
2, . . . ,t
n−1). Consider this projectively, so that γ is homeomorphic
to RP1, which is a circle. A ﬂag F• is secant along an interval I of γ if every subspace in the
ﬂag is spanned by its intersection with I. A list of ﬂags F 1
• , . . . ,F m
• secant to γ is disjoint
if the intervals of secancy are pairwise disjoint. Disjoint ﬂags are naturally ordered by the
order in which their intervals of secancy lie within RP1. We remark that this order is to be
taken cyclically as in Figure 3, and with respect to one of the two orientations of RP1.
A permutation σ is Grassmannian if it has a unique descent, for these, let δ(σ) be the
descent. A Grassmannian Schubert problem is one that involves only Grassmannian Schu-
bert conditions. A list of disjoint secant ﬂags F 1
• , . . . ,F m
• is monotone with respect to a
Grassmannian Schubert problem (σ1, . . . ,σm) if the function F i
• ↦→ δ(σi) is monotone with
respect to one of the two orientations of RP1. In other words, if

δ(σi) < δ(σj) =⇒ F i < F j , for all i,j ,

where < is induced by one of the two cyclic orderings of RP1.

Monotone Secant Conjecture 3.1. For any Grassmannian Schubert problem (σ1, . . . , σm)
on the ﬂag manifold Fℓ(a•; n) and any disjoint secant ﬂags F 1
• , . . . ,F m
• that are monotone
with respect to the Schubert problem, the intersection

Xσ1F 1
• ∩ Xσ2F 2
• ∩ · · · ∩ XσmF m
•
is transverse with all points real.

Conjecture 1.1 is the monotone secant conjecture for a Schubert problem on Fℓ(2,3; 5)
involving the Schubert conditions σ := 13245 and τ := 12435, where we write permutations
in one-line notation, so that σ(2) = 3 and τ (2) = 2. Then δ(σ) = 2, δ(τ ) = 3, and ℓ(σ) =
ℓ(τ ) = 1, so that (σ,σ,σ,σ,τ,τ,τ,τ ) is a Schubert problem for Fℓ(2,3; 5), as dim(Fℓ(2,3; 5)) = 8.
We use exponential notation for repeated conditions, so that this Schubert problem is written
as (σ4,τ 4). The corresponding Schubert varieties are

XσF• = {E• ∈ Fℓ(2,3; 5) | dim E2 ∩ F3 ≥ 1} ,
Xτ F• = {E• ∈ Fℓ(2,3; 5) | dim E3 ∩ F2 ≥ 1} ,

that is, the set of ﬂags E• whose 2-plane E2 meets a ﬁxed 3-plane F3 non-trivially, and the
set of E• where E3 meets a ﬁxed 2-plane F2 non-trivially, respectively. Consequently, we
write XσF3 for XσF• and Xτ F2 for Xτ F•.
For s,t,u,v,w ∈ R, let F3(s,t,u) be the linear span of γ(s), γ(t), and γ(u) and F2(v,w)
be the linear span of γ(v) and γ(w); these are a secant 3-plane and a secant 2-plane to
the rational normal curve, respectively. The condition f (s,t,u; x) = 0 of Conjecture 1.1 is
equivalent to the membership E• ∈ XσF3(s,t,u). Similarly, the condition g(v,w; x) = 0 is
equivalent to the membership E• ∈ Xτ F2(v,w). Lastly, the condition on the ordering of

MONOTONE SECANT CONJECTURE 7

the points si,ti,ui,vj,wj in Conjecture 1.1 implies that the relevant subspaces F3(si,ti,ui) and
F2(vj,wj) for i,j = 1, . . . ,4 lie in disjoint secant ﬂags that are monotone with respect to this
Schubert problem.
Three conjectures that have driven progress in enumerative real algebraic geometry are
specializations of the monotone secant conjecture. For the Grassmannian Gr(a; n), any
list of disjoint secant ﬂags F 1
• , . . . ,F m
• is monotone with respect to any Schubert problem
(σ1, . . . ,σm), as all the conditions have the same descent. In this way, the monotone secant
conjecture reduces to the secant conjecture.

Secant Conjecture 3.2. For any Schubert problem (σ1, . . . , σm) on any Grassmannian and
any disjoint secant ﬂags F 1
• , . . . , F m
• , the intersection

Xσ1F 1
• ∩ Xσ2F 2
• ∩ · · · ∩ XσmF m
•
is transverse with all points real.

We studied this conjecture in a large-scale experiment whose results are described in [10],
solving 1,855,810,000 instances of 703 Schubert problems on 13 diﬀerent Grassmannians,
verifying the secant conjecture in each of the 448,381,157 instances checked. This took 1.065
teraHertz-years of computing.
The osculating ﬂag F•(t) is the ﬂag whose j-dimensional subspace Fj(t) is the span of
the ﬁrst j derivatives γ(t),γ′(t), . . . ,γ(j−1)(t) of γ at t. This subspace Fj(t) is the unique j-
dimensional subspace having maximal order of contact, namely j, with γ at γ(t). It follows
that the limit of any family of ﬂags whose intervals of secancy shrink to a point γ(t) is this
osculating ﬂag F•(t). In this way, the limit of the monotone secant conjecture, as the secant
ﬂags become osculating ﬂags, is a similar conjecture where we replace monotone secant ﬂags
by monotone osculating ﬂags.

Monotone Conjecture 3.3. For any Schubert problem (σ1, . . . , σm) on the ﬂag manifold
Fℓ(a•; n) and any ﬂags F 1
• , . . . , F m
• osculating a rational normal curve γ at real points that
are monotone with respect to the Schubert problem, the intersection

Xσ1F 1
• ∩ Xσ2F 2
• ∩ · · · ∩ XσmF m
•
is transverse with all points real.

Ruﬀo, et al. [17] formulated and studied this conjecture, establishing special cases and
giving substantial experimental evidence in support of it.
The Shapiro conjecture is a specialization of the monotone secant conjecture that both
restricts to the Grassmannian and to osculating ﬂags. This was posed around 1995 by
Boris Shapiro and Michael Shapiro and studied in [18]. Proofs were given by Eremenko and
Gabrielov for Gr(n−2; n) [5, 6] using complex analysis and in complete generality by Mukhin,
Tarasov, and Varchenko [14, 15] using integrable systems and representation theory.

Shapiro Conjecture 3.4. For any Schubert problem (σ1, . . . , σm) in a Grassmannian and
any distinct real numbers t1, . . . , tm, the intersection

Xσ1F•(t1) ∩ Xσ2F•(t2) ∩ · · · ∩ XσmF•(tm)

8 HEIN, HILLAR, MART´IN DEL CAMPO, SOTTILE, AND TEITLER

is transverse with all points real.
 4. Results

A consequence of the example discussed in Section 2 is that the secant conjecture (like the
Shapiro conjecture before it) does not hold for ﬂag manifolds Fℓ(a•; n) that are not Grass-
mannians. The monotonicity condition appears to correct this failure in both conjectures.
We give more details on the relation of the monotone conjecture to the monotone secant
conjecture and give a conjecture that interpolates between the two. Then we discuss some
of our data in an experiment that tested both conjectures.

4.1. The monotone conjecture is the limit of the monotone secant conjecture.
The osculating plane Fi(s) is the unique i-dimensional subspace having maximal order of
contact with the rational normal curve γ at the point γ(s), and therefore it is a limit of
secant planes. We give a more precise statement of this fact.

Proposition 4.1. Let {s(j)
1 . . . , . . . , s(j)
i } for j = 1,2, . . . be a sequence of lists of i distinct
complex numbers with the property that for each p = 1, . . . , i, we have

lim
j→∞ s(j)
p = s ,

for some number s. Then,

lim
j→∞ span{γ(s(j)
1 ), . . . , γ(s(j)
i )} = Fi(s) .

As explained in the previous section, by this proposition, the monotone secant conjecture
implies the monotone conjecture. This has a partial converse which follows from a standard
limiting argument.

Theorem 4.2. Let (σ1, . . . , σm) be a Schubert problem on Fℓ(a; n) for which the monotone
conjecture holds. Then, for any distinct real numbers that are monotone with respect to
(σ1, . . . ,σm), there exists a number ǫ > 0 such that, if for each i = 1, . . . ,m, F i
• is a ﬂag
secant to γ along an interval of length ǫ containing ti, then the intersection

Xσ1F 1
• ∩ Xσ2F 2
• ∩ · · · ∩ XσmF m
•
is transverse with all points real.

4.2. Generalized monotone secant conjecture. We generalize the monotone secant con-
jecture, replacing secant ﬂags by ﬂags which are spanned by osculating subspaces, as in [10,
§ 3.3]. By Proposition 4.1, such ﬂags are intermediate between secant and osculating ﬂags,
so this new conjecture interpolates between the monotone secant and monotone conjectures.
A generalized secant subspace to the rational normal curve γ is a subspace that is spanned
by subspaces osculating γ at real points. This notion includes secant subspaces as well as
osculating subspaces, as a point of γ generates a one-dimensional subspace osculating γ. A
generalized secant ﬂag is one consisting of generalized secant subspaces. A generalized secant

MONOTONE SECANT CONJECTURE 9

ﬂag is secant along an interval I if the osculating subspaces spanning its subspaces osculate
γ at points of I.

Conjecture 4.3 (Generalized monotone secant conjecture). For any Grassmannian Schubert
problem (σ1, . . . , σm) on the ﬂag manifold Fℓ(a•; n) and any disjoint generalized secant ﬂags
F 1
• , . . . ,F m
• that are monotone with respect to the Schubert problem, the intersection

Xσ1F 1
• ∩ Xσ2F 2
• ∩ · · · ∩ XσmF m
•
is transverse with all points real.

This conjecture contains the monotone and monotone secant conjectures as special cases,
and interpolates between the two.

4.3. Experimental evidence for the monotone secant conjecture. While its rela-
tion to existing conjectures led to the monotone secant conjecture, we believe the immense
weight of empirical evidence is the strongest support for it. We conducted an experiment
that tested 11,141,897,000 instances of 1300 Schubert problems on 19 ﬂag manifolds. Of
these, 768,846,000 were instances of the monotone secant conjecture, which was veriﬁed
in every case tested. We also tested 918,902,000 instances of the monotone conjecture for
comparison. The remaining instances involved non-monotone evaluations of either disjoint
secant ﬂags or osculating ﬂags. Our data consistently displayed a striking inner border, and
a number of Schubert problems exhibited lower bounds on their numbers of real solutions.
This experiment used 1.9 teraHertz-years of computing.
Table 1 shows the data we obtained for the Schubert problem (σ4,τ 4) with 12 solutions on
the ﬂag manifold Fℓ(2,3; 5) introduced in Conjecture 1.1. We computed 24,000,000 instances

Real SolutionsNecklace
0 2 4 6 8 10 12 Total
22223333 1000000 1000000
22233233 31 205380 545269 1245017 1004303 3000000
22322333 196 403485 1071579 967226 557514 3000000
22332233 391 801525 1200700 651183 346201 3000000
22323323 1025 70009 300121 938430 1123770 566645 3000000
22323233 33488 950203 1256341 560205 164020 35743 3000000
22232333 93232 284316 460016 1010425 750171 401840 3000000
23232323 885953 854550 830122 298843 104574 23741 2217 3000000
Total 885953 982295 2135268 3725711 5431182 4925128 5914463 24000000

Table 1. Necklaces vs. real solutions for (σ4,τ 4) in Fℓ(2,3; 5).

of this problem, all involving ﬂags that were secant to the rational normal curve along disjoint
intervals. This took 17.618 gigaHertz-years. The columns are indexed by even integers from
0 to 12, indicating the number of real solutions. The rows are indexed by necklaces, which are
sequences δ(σ1), . . . ,δ(σm), where δ(σi) denotes the descent of the Grassmannian permutation
σi, as described in Section 3. In the table a 2 represents the condition on the two-plane E2

10 HEIN, HILLAR, MART´IN DEL CAMPO, SOTTILE, AND TEITLER

given by the permutation σ = 13245, and a 3 represents the condition on E3 given by the
permutation τ = 12435.
In Table 1, the ﬁrst row labeled with 22223333 represents tests of the monotone secant
conjecture, since the only entries are in the column for 12 real solutions, the monotone secant
conjecture was veriﬁed in 3,000,000 instances. This is the only row with only real solutions.
Compare this to the 16,000,000 instances of the same Schubert problem, but with oscu-
lating ﬂags, which we present in Table 2. This computation took 85.203 gigahertz-days.
Both tables are similar with nearly identical “inner borders”, except for the shaded box

Real SolutionsNecklace
0 2 4 6 8 10 12 Total
22223333 2000000 2000000
22233233 1041 246876 581972 582865 587246 2000000
22322333 1480 263981 621920 584508 528111 2000000
22332233 8882 217100 861124 503562 409332 2000000
22323323 120195 402799 665766 549653 261587 2000000
22323233 7329 255114 431074 664551 420699 221233 2000000
22232333 25552 137116 227922 415553 424582 769275 2000000
23232323 49197 125725 557851 395992 516675 244212 110348 2000000
Total 49197 158606 1081679 2185744 4327561 3310081 4887132 16000000

Table 2. Necklaces vs. real solutions for (σ4,τ 4) in Fℓ(2,3; 5).

in Table 2. In fact, by a standard argument similar to that which implied Theorem 4.2,
we may conclude that every number of real solutions to a Schubert problem observed for a
given necklace with osculating ﬂags also occurs for that Schubert problem and necklace with
secant ﬂags, where the points of secancy are suﬃciently clustered. That is, the support of a
table for the monotone conjecture will be a subset of the support of the corresponding table
for the monotone secant conjecture. There are some Schubert problems for which we did
not observe this containment; the reason for this is that we aparently did not compute an
instance with secant ﬂags whose points of secancy were suﬃciently clustered.

4.4. Lower bounds and inner borders. The most enigmatic phenomenon that we observe
in our data is the presence of an “inner border” for many geometric problems, as we have
pointed out in example of Table 1. That is, for some necklaces (besides the monotone ones),
there appears to be a lower bound on the number of real solutions. We do not understand
this phenomenon, even conjecturally. Our software that displays the tables is designed to
highlight this feature of our data.
Another common phenomenon is that for many problems, there are always at least some
real solutions, for any necklace. (Note that the last rows of Tables 1 and 2 had instances with
no real solutions). Table 3 displays an example of this for a Schubert problem (σ3,τ 5) on
Fℓ(2,3; 6) with 21 solutions, where σ := 142356 has δ(σ) = 2 and ℓ(σ) = 2 and τ := 124356
has δ(τ ) = 3 and ℓ(τ ) = 1. Very prominently, it appears that at least 11 of the solutions
will always be real. This computation took 7.67 gigaHertz-years.

MONOTONE SECANT CONJECTURE 11

Real SolutionsNecklace
1 3 5 7 9 11 13 15 17 19 21 Total
22233333 80000 80000
22323333 921 16549 26267 14475 21788 80000
22332333 39 1208 24559 39013 13947 1234 80000
23233233 612 9544 43256 23583 2927 78 80000
23232333 3244 19887 31931 13688 3632 7618 80000
Total 3895 31560 116295 102551 34981 110718 400000

Table 3. Enumerative Problem W 3X 5 = 21 on Fℓ(2, 3; 6)

Such lower bounds and inner borders were observed when studying the monotone con-
jecture [17]. Eremenko and Gabrielov established lower bounds for the Wronski map [4] in
Schubert calculus for the Grassmannian, more recently Azar and Gabrielov [1] established
lower bounds for some instances of the monotone conjecture which were observed in [17].

5. Methods

Our experimentation was possible as instances of Schubert problems are simple to model
on a computer. The procedure we use may be semi-automated and run on supercomputers.
We will not describe how this automation is done, for that is the subject of the paper [11];
instead, we explain here the computations we performed.
For a Schubert condition σ on a ﬂag variety Fℓ(a•; n), let j(σ) be the dimension of the
largest subspace in a ﬂag F• that is needed to deﬁne XσF•. For example, we have seen that
j(13245) = 3 and j(12435) = 2.
To compute an instance of a Schubert problem (σ1, . . . , σm) corresponding to a necklace
ν, we ﬁrst select N := N(σ1) + . . . + N(σm) real numbers and then group them into disjoint
subsets s(1), . . . ,s(m) where s(i) consists of N(σi) consecutive numbers. Furthermore, the
relative ordering of the subsets corresponds to the necklace ν. Having done this, each subset
s(i) deﬁnes a secant (partial) ﬂag F•(s(i)). We use these ﬂags to formulate the instance of
the Schubert problem
Xσ1F•(s(1)) ∩ Xσ2F•(s(2)) ∩ · · · ∩ XσmF•(s(m))

as a system of polynomials in dim(a•) local coordinates for Fℓ(a•; n), whose common zeroes
represent the solutions to this instance of the Schubert problem. This was illustrated in the
Introduction when Conjecture 1.1 was presented. See [8, 17, 18] for details.
Given this system of polynomials, we use Gr¨obner bases to compute a polynomial in one
variable of minimal degree in the ideal of these equations. This univariate polynomial is called
an eliminant. If the eliminant is square-free and has degree equal to the expected number
of complex solutions (this is easily veriﬁed) then the number of real roots of the eliminant
equals the number of real solutions to the Schubert problem. This follows from the form of a
lexicographic Gr¨obner basis for the ideal, as described by the Shape Lemma [3]. This is given
in more detail in §2.2 of [21]. We determine the number of real solutions to the Schubert

12 HEIN, HILLAR, MART´IN DEL CAMPO, SOTTILE, AND TEITLER

problem by computing the number of real roots of the eliminant. For this, we use MAPLE’s
realroot command, which uses symbolic methods based on Sturm sequences to determine
the number of real roots of a univariate polynomial. If the software is reliably implemented,
which we believe, then this computation provides a proof that the given instance has the
computed number of real solutions to the original Schubert problem.
In our computations, for a given Schubert problem, we ﬁrst make a choice of N real
numbers, and then use these same N numbers for all necklaces for that problem. Then we
make another choice, and so on, ultimately making thousands to millions of such choices.
For each Schubert problem we studied, we not only tested many instances of the monotone
secant conjecture, but also of the monotone conjecture, comparing the two as we did for the
Schubert problem (σ4,τ 4) in Fℓ(2,3; 5), where σ = 13245 and τ = 12435. To compute
instances of the monotone conjecture, we choose real numbers s1, . . . ,sm and use osculating
ﬂags F•(s1), . . . ,F•(sm). This is also described in [17, § 5].
For many Schubert problems, it was infeasible to compute instances of the monotone
secant conjecture, and we instead computed instances of the generalized monotone secant
conjecture. For these, one of the ﬂags was the ﬂag F•(∞) osculating the rational normal curve
at inﬁnity. Then we used local coordinates for Xσ1F•(∞), in place of the local coordinates
for Fℓ(a•; n); this uses ℓ(σi) fewer local coordinates.
For some Schubert problems we wanted to study, there were several hundred to many
thousands of necklaces, and for these we uniformly chose a much smaller set of necklaces to
compute, which we called coarse necklaces. In our on-line tables, we encoded these choices
in a variable called computation type. Computation types 4 and 7 were for instances of
the monotone conjecture, 5 and 8 for the monotone secant conjecture, and 6 and 9 for the
generalized monotone secant conjecture. In each of these, the ﬁrst number indicates that we
used all necklaces, while the second we used coarse necklaces.

References

[1] Monique Azar and Andrei Gabrielov, Some lower bounds in the B. and M. Shapiro conjecture for ﬂag
varieties, Discrete Comput. Geom. 46 (2011), no. 4, 636–659.
[2] D.J. Bates, F. Bihan, and F. Sottile, Bounds on the number of real solutions to polynomial equations,
Int. Math. Res. Not. IMRN (2007), no. 23, Art. ID rnm114, 7.
[3] E. Becker, M.G. Marinari, T. Mora, and C. Traverso, The shape of the Shape Lemma, Proc. ISSAC
’94, ACM Press, New York, 1994.
[4] A. Eremenko and A. Gabrielov, Degrees of real Wronski maps, Discrete Comput. Geom. 28 (2002),
no. 3, 331–347.
[5] A. Eremenko and A. Gabrielov, Rational functions with real critical points and the B. and M. Shapiro
conjecture in real enumerative geometry, Ann. of Math. (2) 155 (2002), no. 1, 105–129.
[6] A. Eremenko and A. Gabrielov, An elementary proof of the B. and M. Shapiro conjecture for rational
functions, Notions of positivity and the geometry of polynomials, Springer, Basel, 2011, pp. 167–178.
[7] A. Eremenko, A. Gabrielov, M. Shapiro, and A. Vainshtein, Rational functions and real Schubert
calculus, Proc. Amer. Math. Soc. 134 (2006), no. 4, 949–957 (electronic).
[8] W. Fulton, Young tableaux, London Mathematical Society Student Texts, vol. 35, Cambridge University
Press, Cambridge, 1997.
 MONOTONE SECANT CONJECTURE 13

[9] L. Garc´ıa-Puente, J. Hauenstein, N. Hein, C. Hillar, A. Mart´ın del Campo, J. Ruﬀo, F. Sottile, and
Z. Teitler, Frontiers of reality in Schubert calculus, 2010, www.math.tamu.edu/~secant.
[10] L.D. Garc´ıa-Puente, N. Hein, C. Hillar, A. Mart´ın del Campo, J. Ruﬀo, F. Sottile, and Z. Teitler, The
Secant Conjecture in the real Schubert calculus, Experimental Math., 21 (2012), pp. 252–265.
[11] C. Hillar, L. Garc´ıa-Puente, A. Mart´ın del Campo, J. Ruﬀo, Z. Teitler, S. L. Johnson, and F. Sottile,
Experimentation at the frontiers of reality in Schubert calculus, Gems in Experimental Mathematics,
Contemporary Mathematics, vol. 517, Amer. Math. Soc., Providence, RI, 2010, pp. 365–380.
[12] A.G. Khovanskii, Fewnomials, Trans. of Math. Monographs, 88, AMS, 1991.
[13] S. L. Kleiman, The transversality of a general translate, Compositio Math. 28 (1974), 287–297.
[14] E. Mukhin, V. Tarasov, and A. Varchenko, The B. and M. Shapiro conjecture in real algebraic geometry
and the Bethe ansatz, Ann. of Math. (2) 170 (2009), no. 2, 863–881.
[15] E. Mukhin, V. Tarasov, and A. Varchenko, Schubert calculus and representations of the general linear
group, J. Amer. Math. Soc. 22 (2009), no. 4, 909–940.
[16] K. Purbhoo, Reality and transversality for Schubert calculus in OG(n,2n + 1), Math. Res. Lett. 17
(2010), no. 6, 1041–1046.
[17] J. Ruﬀo, Y. Sivan, E. Soprunova, and F. Sottile, Experimentation and conjectures in the real Schubert
calculus for ﬂag manifolds, Experiment. Math. 15 (2006), no. 2, 199–221.
[18] F. Sottile, Real Schubert calculus: polynomial systems and a conjecture of Shapiro and Shapiro, Ex-
periment. Math. 9 (2000), no. 2, 161–182.
[19] F. Sottile, Some real and unreal enumerative geometry for ﬂag manifolds, Michigan Math. J. 48 (2000),
573–592.
[20] F. Sottile, Frontiers of reality in Schubert calculus, Bull. Amer. Math. Soc. (N.S.) 47 (2010), no. 1,
31–71.
[21] F. Sottile, Real solutions to equations from geometry, University Lecture Series, vol. 57, American
Mathematical Society, 2011.

Nickolas Hein, Department of Mathematics, University of Nebraska at Kearney, Kear-
ney, Nebraska 68849, USA
E-mail address: heinnj@unk.edu
URL: http://www.unk.edu/academics/math/faculty/About_Nickolas_Hein/

Christopher J. Hillar, Mathematical Sciences Research Institute, 17 Gauss Way, Berke-
ley, CA 94720-5070, USA
E-mail address: chillar@msri.org
URL: http://www.msri.org/people/members/chillar

Abraham Mart´ın del Campo, IST Austria, Am Campus 1, 3400 Klosterneuburg, Austria
E-mail address: abraham.mc@ist.ac.at
URL: http://pub.ist.ac.at/~adelcampo/

Frank Sottile, Department of Mathematics, Texas A&M University, College Station,
Texas 77843, USA
E-mail address: sottile@math.tamu.edu
URL: http://www.math.tamu.edu/~sottile

Zach Teitler, Department of Mathematics, Boise State University, Boise, Idaho 83725,
USA
E-mail address: zteitler@math.boisestate.edu
URL: http://math.boisestate.edu/~zteitler
