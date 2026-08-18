<!-- source: https://arxiv.org/pdf/1010.0665 | converted from PDF -->

arXiv:1010.0665v3  [math.AG]  24 Jan 2012
THE SECANT CONJECTURE IN THE REAL SCHUBERT CALCULUS

LUIS D. GARC´IA-PUENTE, NICKOLAS HEIN, CHRISTOPHER HILLAR,
ABRAHAM MART´IN DEL CAMPO, JAMES RUFFO, FRANK SOTTILE, AND ZACH TEITLER

Abstract. We formulate the Secant Conjecture, which is a generalization of the Shapiro
Conjecture for Grassmannians. It asserts that an intersection of Schubert varieties in a Grass-
mannian is transverse with all points real if the ﬂags deﬁning the Schubert varieties are secant
along disjoint intervals of a rational normal curve. We present theoretical evidence for this
conjecture as well as computational evidence obtained in over one terahertz-year of computing,
and we discuss some of the phenomena we observed in our data.

1. Introduction

Some solutions to a system of real polynomial equations are real and the rest occur in
complex conjugate pairs. While the total number of solutions is determined by the structure of
the equations, the number of real solutions depends rather subtly on the coeﬃcients. Sometimes
there is ﬁner information available in terms of upper bounds [19, 2] or lower bounds [7, 31] on
the number of real solutions. The Shapiro and Secant Conjectures assert the extreme situation
of having only real solutions.
The Shapiro Conjecture for Grassmannians posits that if the Wronskian of a vector space of
univariate complex polynomials has only real roots, then that space is spanned by real polyno-
mials. This striking instance of unexpected reality was proven by Eremenko and Gabrielov for
two-dimensional spaces of polynomials [8, 9], and the general case was established by Mukhin,
Tarasov, and Varchenko [23, 25]. While the statement concerns spaces of polynomials, or
more generally the Schubert calculus on Grassmannians, its proofs complex analysis [8, 9] and
mathematical physics [23, 25]. This story was described in the AMS Bulletin [35].
The Shapiro conjecture ﬁrst gained attention through partial results and computations [33,
38], and further work [34] led to an extension that appears to hold for ﬂag manifolds, the
Monotone Conjecture. This extension was made in [27], which also reported on partial results
and experimental evidence. The Monotone Conjecture for a certain family of two-step ﬂag
manifolds was proved by Eremenko, Gabrielov, Shapiro, and Vainshtein [10].
The result of [10] was in fact a proof of reality in the Grassmannian of codimension-two planes
for intersections of Schubert varieties deﬁned with respect to certain disjoint secant ﬂags. The
Secant Conjecture postulates an extension of this result to all Grassmannians. We give the

1991 Mathematics Subject Classiﬁcation. 14M25, 14P99.
Research of Sottile supported in part by NSF grant DMS-070105 and DMS-1001615.
Research of Hillar supported in part by an NSF Postdoctoral Fellowship and an NSA Young Investigator
grant.
This research conducted in part on computers provided by NSF SCREMS grant DMS-0922866.

1

2 GARC´IA-PUENTE, HEIN, HILLAR, MART´IN DEL CAMPO, RUFFO, SOTTILE, AND TEITLER

simplest open instance of the Secant Conjecture. Let x1, . . . ,x6 be indeterminates and consider
the polynomial

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
 ,

which depends upon parameters s, t, and u.

Conjecture 1.1. Let s1 < t1 < u1 < s2 < t2 < · · · < u5 < s6 < t6 < u6 be real numbers.
Then the system of polynomial equations

(1.2) f (si,ti,ui; x) = 0 i = 1, . . . ,6

has ﬁve distinct solutions, and all of them are real.

Geometrically, the equation f (s,t,u; x) = 0 says that the 2-plane (spanned by the ﬁrst two
rows of the matrix in (1.1)) meets the 3-plane which is secant to the rational curve γ : y ↦→
(1,y,y2,y3,y4) at the points γ(s),γ(t),γ(u). The hypotheses imply that each of the six 3-planes is
secant to γ along an interval [si,ui], and these six intervals are pairwise disjoint. The conjecture
asserts that all of the 2-planes meeting six 3-planes are real when the 3-planes are secant to the
rational normal curve along disjoint intervals. This statement was true in each of the 285,502
instances we tested.
The purpose of this paper is to explain the Secant Conjecture and its relation to the other
reality conjectures, to describe the data supporting it from a large computational experiment,
and to highlight some other features in our data beyond the Secant Conjecture. These data
may be viewed online [40]. We will assume some background on the Shapiro Conjecture as
described in the survey [35] and paper [27], and we will not describe the execution of the
experiment, as the methods paper [14] presented the software framework we have developed for
such distributed computational experiments.
This paper is organized as follows. In Section 2, we present the full Secant Conjecture,
giving a history of its formulation. Section 3 presents some theoretical justiﬁcation for the
Secant Conjecture as well as a generalization based on limiting cases. In Section 4 we analyze
the problem of lines meeting all possible conﬁgurations of four secant lines, giving conditions
on the secant lines that imply that both solutions are real. Section 5 describes a statistic, the
overlap number, which measures the extent of overlap among intervals of secancy. In Section 6
we explain the data from our experiment. About 3/4 of our over 2 billion computations did
not directly test the Secant Conjecture, but rather tested geometric conﬁgurations that were
close to those of the conjecture. Consequently, our data contain much more information than
that in support of the Secant Conjecture, and we explore that information in the remaining
sections. Section 7 discusses the lower bounds on the numbers of real solutions we typically
observed for small overlap number, producing a striking inner border in the tabulation of our
data. Finally, in Section 8, we discuss Schubert problems with provable lower bounds and gaps

THE SECANT CONJECTURE IN THE REAL SCHUBERT CALCULUS 3

in their numbers of real solutions, a phenomenon we ﬁrst noticed while trying to understand
our data.
We thank Brian Osserman and the referee for their comments on earlier versions of this
paper.
 2. Schubert Calculus and the Secant Conjecture

We give background from the Schubert Calculus necessary to state the Secant Conjecture,
and then we state the equivalent dual Cosecant Conjecture.

2.1. Schubert Calculus. The Schubert Calculus [11, 12] involves problems of determining the
linear spaces that have speciﬁed positions with respect to other, ﬁxed (ﬂags of) linear spaces.
For example, what are the 3-planes in C7 meeting 12 given 4-planes non-trivially? (There
are 462 [28].) The speciﬁed positions are a Schubert problem, which determines the number
of solutions. The actual solutions depend upon the linear spaces imposing the conditions, or
instance of the Schubert problem.
The Grassmannian G(k,n) is the set of all k-dimensional linear subspaces of Cn, which is an
algebraic manifold of dimension k(n−k). A ﬂag F• is a sequence of linear subspaces

F• : F1 ⊂ F2 ⊂ · · · ⊂ Fn ,

where dim Fi = i. A partition λ : (n−k) ≥ λ1 ≥ · · · ≥ λk ≥ 0 is a weakly decreasing sequence
of integers. A ﬁxed ﬂag F• and a partition λ deﬁne a Schubert variety XλF•,

XλF• := {H ∈ G(k,n) | dim H ∩ Fn−k+i−λi ≥ i for i = 1, . . . ,k} ,

which is a subvariety of codimension |λ| := λ1 + · · ·+ λk. Not every element of the ﬂag is needed
to deﬁne the Schubert variety.
A Schubert problem is a list λ1, . . . ,λm of partitions with |λ1| + · · · + |λm| = k(n − k). For
suﬃciently general ﬂags F 1
• , . . . ,F m
• , the intersection

Xλ1F 1
• ∩ Xλ2F 2
• ∩ · · · ∩ XλmF m
•

is transverse [20] and consists of a certain number, d(λ1, . . . ,λm), of points, which may be
computed using algorithms in the Schubert Calculus (see [11, 21]). (Transverse means that at
each point of the intersection, the annihilators of the tangent spaces to the Schubert varieties
are in direct sum.) We write a Schubert problem multiplicatively, λ1 · · · λm = d(λ1, . . . ,λm).
For example, writing for the partition (1,0) with | | = 1, we have · · · · · = 6 = 5
for the Schubert problem on G(2,5) involving six partitions, each equal to . In this notation,
Schubert’s problem that we mentioned above is 12 = 462 on G(3,7).
A rational normal curve γ : R → Rn is aﬃnely equivalent to the moment curve

γ : t ↦−→ (1, t, t
2, . . . , t
n−1) .

The osculating ﬂag F•(t) has i-dimensional subspace the span of the ﬁrst i derivatives γ(t),γ′(t), . . . ,γ(i−1)(t)
of γ at t. We state the Theorem of Mukhin, et al. [23, 25].

4 GARC´IA-PUENTE, HEIN, HILLAR, MART´IN DEL CAMPO, RUFFO, SOTTILE, AND TEITLER

Theorem 2.1 (The Shapiro Conjecture). For any Schubert problem λ1, . . . ,λm on a Grass-
mannian G(k,n) and any distinct real numbers t1, . . . ,tm, the intersection

Xλ1F•(t1) ∩ Xλ2F•(t2) ∩ · · · ∩ XλmF•(tm)

is transverse and consists of d(λ1, . . . ,λm) real points.

Transversality is unexpected as osculating ﬂags are not general.
The Shapiro Conjecture concerns intersections of Schubert varieties given by ﬂags osculating
a rational normal curve, and in this form it makes sense for every ﬂag manifold G/P . Purbhoo
showed that it holds for the orthogonal Grassmannians [26], but counterexamples are known
for other ﬂag manifolds. There is an appealing version of it—the Monotone Conjecture—that
appears to hold for the classical ﬂag variety [27].

2.2. The Secant Conjecture. Eremenko, et al. [10] proved a generalization of the Monotone
Conjecture for ﬂags consisting of a codimension-two plane lying on a hyperplane, where it
becomes a statement about real rational functions. Their theorem asserts that a Schubert
problem on G(n−2,n) has only real solutions if the ﬂags satisfy a special property that we now
describe. A ﬂag F• of linear subspaces is secant along an interval I of a rational normal curve
γ if every subspace in the ﬂag is spanned by its intersection with I. This means that there are
distinct points t1, . . . ,tn−1 ∈ I such that for each i = 1, . . . ,n−1, the subspace Fi of the ﬂag F•
is spanned by γ(t1), . . . ,γ(ti).

Secant Conjecture 2.2. For any Schubert problem λ1, . . . ,λm on a Grassmannian G(k,n) and
any ﬂags F 1
• , . . . ,F m
• that are secant to a rational normal curve γ along disjoint intervals, the
intersection Xλ1F 1
• ∩ Xλ2F 2
• ∩ · · · ∩ XλmF m
•
is transverse and consists of d(λ1, . . . ,λm) real points.

Conjecture 1.1 is the case of this Secant Conjecture for the Schubert problem 6 = 5 on
G(2,5). The Schubert variety X F• is

X F• = {H ∈ G(2,5) | dim H ∩ F3 ≥ 1} ;

that is, the set of 2-planes meeting a ﬁxed 3-plane non-trivially. Since F4 and F5 are irrelevant
we drop them from the ﬂag and refer to F3 and X F3. For every Schubert condition, there is a
largest element of the ﬂag imposing a relevant condition; call this the relevant subspace. The
relevant subspace in this example is F3.
For s,t,u ∈ R, let F3(s,t,u) be the linear span of γ(s), γ(t), and γ(u), a 3-plane secant to γ
with points γ(s), γ(t), and γ(u) of secancy. Thus, the condition f (s,t,u; x) = 0 of Conjecture 1.1
implies that the linear span H of the ﬁrst two rows of the matrix in (1.1)—a general 2-plane in
5-space—meets the linear span F3(s,t,u) of the last three rows. Thus

f (s,t,u; x) = 0 ⇐⇒ H ∈ X F3(s,t,u) .

Lastly, the condition on the ordering of the points si,ti,ui in Conjecture 1.1 implies that the six
ﬂags F3(si,ti,ui) are secant along disjoint intervals.

THE SECANT CONJECTURE IN THE REAL SCHUBERT CALCULUS 5

2.3. Grassmann Duality and the Cosecant Conjecture. Associating a linear subspace
H of a vector space V ≃ Cn to its annihilator δ(H) := H ⊥ ⊂ V ∗ induces an isomorphism
δ : G(k,n) → G(n−k,n) called Grassmann duality. This notion extends to ﬂags and the dual
of an osculating ﬂag is an osculating ﬂag. Secancy is not preserved under duality. We next
formulate the (equivalent) dual statement to the Secant Conjecture, which we call the Cosecant
Conjecture.
Grassmann duality respects Schubert varieties. Given a ﬂag F• ⊂ Cn, let F ⊥
• be the ﬂag
whose i-dimensional subspace is F ⊥
i := (Fn−i)⊥. Then

δ(XλF•) = XλT F ⊥
• ,

where λT is the conjugate partition to λ. For example,

T = , T = , and T = .

That is, if we represent λ by its Young diagram—a left-justiﬁed array of boxes with λi boxes
in row i—then the diagram of λT is the matrix-transpose of the diagram of λ.
If γ(t) = (1,t,t
2, . . . ,t
n−1) is the rational normal curve, then the dual of the family Fn−1(t) of
its osculating (n−1)-planes is a curve γ⊥(t) := (Fn−1(t))⊥, which is

γ⊥(t) = ((n−1
n−1
)(−t)n−1 , . . . , − (
n−1
3 )t
3 , (n−1
2 )
t
2 , − (n−1)t , 1 ) ,

in the basis dual to the standard basis. Moreover, (Fn−k(t))⊥ is the osculating k-plane to
this dual rational normal curve γ⊥ at the point γ⊥(t). Thus Grassmann duality preserves
Schubert varieties given by ﬂags osculating the rational normal curve, and the dual statement
to Theorem 2.1 is simply itself.
This is however not the case for secant ﬂags. The general secant (n−1)-plane

Fn−1(s1,s2, . . . ,sn−1) = span{γ(s1) , γ(s2) , . . . , γ(sn−1)} ,

secant to γ at the points γ(s1), . . . ,γ(sn−1), has dual space spanned by the vector
((−1)n−1en−1 , . . . , − e3 , e2 , − e1 , 1) ,

where ei is the ith elementary symmetric function in the parameters s1, . . . ,sn−1. This dual
space is not secant to the dual rational normal curve γ⊥.
In general, a cosecant subspace is a subspace that is dual to a secant subspace. If

Fk(s1,s2, . . . ,sk) = span{γ(s1) , γ(s2) , . . . , γ(sk)} ,

then the corresponding cosecant subspace is

F ⊥
n−1(s1) ∩ F ⊥
n−1(s2) ∩ · · · ∩ F ⊥
n−1(sk) ,

the intersection of k hyperplanes osculating the rational normal curve γ⊥. A cosecant ﬂag is a
ﬂag whose subspaces are cut out by hyperplanes osculating γ. It is cosecant along an interval
of γ if these hyperplanes osculate γ at points of the interval.
Thus, under Grassmann duality the Secant Conjecture for G(n−k,n) becomes the following
equivalent Cosecant Conjecture for G(k,n).

6 GARC´IA-PUENTE, HEIN, HILLAR, MART´IN DEL CAMPO, RUFFO, SOTTILE, AND TEITLER

Conjecture 2.3 (Cosecant Conjecture). For any Schubert problem λ1, . . . ,λm on a Grassman-
nian G(k,n) and any ﬂags F 1
• , . . . ,F m
• that are cosecant to a rational normal curve γ along
disjoint intervals, the intersection

Xλ1F 1
• ∩ Xλ2F 2
• ∩ · · · ∩ XλmF m
•
is transverse and consists of d(λ1, . . . ,λm) real points.

3. Some special cases of the Secant Conjecture

A degree of justiﬁcation for posing the Secant Conjecture is provided by the history of its
development from the Shapiro and Monotone Conjectures, as this shows its connection to
proven results and established conjectures, and its validity for G(n−2,n) [10]. Here, we give
more concrete justiﬁcations, which include proofs in some special cases.

3.1. Arithmetic progressions of secancy. Fix a parametrization γ : R → Rn of a rational
normal curve. For t ∈ R and h > 0, let F h
• (t) be the ﬂag whose i-dimensional subspace is

F h
i (t) := span{γ(t), γ(t+h), . . . , γ(t+(i−1)h)} ,

which is spanned by an arithmetic progression of length i with step size h. Work of Mukhin,
et al. [24] implies the Secant Conjecture for the Schubert problem

(3.1) k(n−k) = [k(n−k)]! 1!2! · · · (k−1)!
(n−k)! · · · (n−2)!(n−1)!

for such secant ﬂags.
Let Cn−1[t] be the space of polynomials of degree at most n−1. The discrete Wronskian with
step size h of polynomials f1, . . . ,fk is the determinant

(3.2) Wh(f1,f2, . . . ,fk) := det
 




f1(t) f1(t + h) · · · f1(t + (k−1)h)
f2(t) f2(t + h) · · · f2(t + (k−1)h)
. . . . . .
fk(t) fk(t + h) · · · fk(t + (k−1)h)




 .

For general f1, . . . ,fk ∈ Cn−1[t], this polynomial has degree k(n−k). Up to a scalar, the
polynomial Wh depends only on the linear span of the polynomials f1, . . . ,fk, giving a map

Wh : G(k, Cn−1[t]) −→ Pk(n−k) ,

where Pk(n−k) is the projective space of polynomials of degree at most k(n − k). Mukhin, et
al. [24] show that Wh is a ﬁnite map. It is a linear projection of the Grassmannian in its Pl¨ucker
embedding, so the ﬁber over a general polynomial w(t) ∈ Pk(n−k) consists of d(
 k(n−k)) reduced
points, each of which is a space V of polynomials with discrete Wronskian w(t). As a special
case of Theorem 2.1 in [24], we have the following statement.

Proposition 3.1. Let V ⊂ Cn−1[t] be a k-dimensional space of polynomials whose discrete
Wronskian Wh(V ) has distinct real roots z1, . . . ,zN , each of multiplicity 1. If for all i ̸= j, we
have |zi − zj| ≥ h, then the space V has a basis of real polynomials.

THE SECANT CONJECTURE IN THE REAL SCHUBERT CALCULUS 7

Corollary 3.2. Set N := k(n−k) and suppose that F h
• (z1), . . . ,F h
• (zN ) are disjoint secant ﬂags
with zi + (n−1)h < zi+1 for each i = 1, . . . ,N − 1. Then the intersection

(3.3) X F h
• (z1) ∩ X F h
• (z2) ∩ · · · ∩ X F h
• (zN )

in G(n−k,n) is transverse with all points real.

Proof. We identify points in the intersection (3.3) with the ﬁbers of the discrete Wronski map
Wh over the polynomial (t−z1) · · · (t−zk(n−k)), which will prove reality. Transversality follows by
an argument of Eremenko and Gabrielov given in [36, Ch. 13]: a ﬁnite analytic map between
complex manifolds that has only real points in its ﬁbers above an open set of real points is
necessarily unramiﬁed over those points.
A polynomial of degree n−1 is the composition of the parametrization γ : C → Cn of the
rational normal curve with a linear form Cn → C. In this way, a subspace V of polynomials of
dimension k corresponds to a surjective map V : Cn → Ck. We will identify such a map with
its kernel H, which is a point in G(n−k,n).
The column space of the matrix in (3.2) is the image under V of the linearly independent
vectors γ(t),γ(t+h), . . . ,γ(t+(k−1)h). These vectors span F h
k (t). Thus the determinant Wh(V )
vanishes at a point t exactly when the map

V : F h
k (t) −→ Ck

does not have full rank; that is, when

dim H ∩ F h
k (t) ≥ 1 ,

which is equivalent to H ∈ X F h
• (t) ⊂ G(n−k,n).
It follows that points in the intersection (3.3) correspond to k-dimensional spaces of poly-
nomials V with discrete Wronskian (t − z1) · · · (t − zk(n−k)), and each of these are real, by
Proposition 3.1. □

3.2. The Shapiro Conjecture is the limit of the Secant Conjecture. The osculating
plane Fi(s) is the unique i-dimensional plane having maximal order of contact with the rational
normal curve γ at the point γ(s). This implies that it is a limit of secant planes, and in fact
every limit of secant planes in which the points come together is an osculating plane.

Lemma 3.3. Let {s(j)
1 , . . . ,s(j)
i } for j = 1,2, . . . be a sequence of lists of i distinct complex
numbers that all converge to the same number, limj→∞ s(j)
p = s, for each p = 1, . . . ,i and for
some number s. Then
 lim
j→∞ span{γ(s(j)
1 ),γ(s(j)
2 ), . . . ,γ(s(j)
i )} = Fi(s) .

As transversality and reality are preserved under perturbation, we conclude that Theorem 2.1
is a limiting case of the Secant Conjecture. Conversely, Theorem 2.1 implies the following.

Theorem 3.4. Let λ1, . . . ,λm be a Schubert problem and t1, . . . ,tm be distinct points of the
rational normal curve γ. Then there exists an ǫ > 0 such that if for each i = 1, . . . ,m, F i
• is a
ﬂag secant to γ along an interval of length ǫ containing ti, then the intersection

(3.4) Xλ1F 1
• ∩ Xλ2F 2
• ∩ · · · ∩ XλmF m
•

8 GARC´IA-PUENTE, HEIN, HILLAR, MART´IN DEL CAMPO, RUFFO, SOTTILE, AND TEITLER

is transverse with all points real.

This implies that for generic secant ﬂags F 1
• , . . . ,F m
• , the intersection (3.4) is transverse,
which implies that secant ﬂags are suﬃciently general for the Schubert Calculus. Furthermore,
Theorem 3.4 reduces the Secant Conjecture 2.2 to its transversality statement.

3.3. Generalized Secant Conjecture. Theorem 3.4 suggests a conjecture involving ﬂags that
are intermediate between secant and osculating, and which includes the Secant Conjecture and
Theorem 2.1 as special cases.
A generalized secant subspace to the rational normal curve γ is spanned by osculating sub-
spaces of γ. This notion includes secant subspaces, for a one-dimensional subspace that oscu-
lates γ is simply one that is spanned by a point of γ. A ﬂag F• is generalized secant to γ if
each of the linear spaces in F• are generalized secant subspaces. A generalized secant ﬂag is
secant along an interval of γ if the osculating subspaces that span its linear spaces osculate γ
at points of the interval.

Conjecture 3.5 (Generalized Secant Conjecture). For any Schubert problem λ1, . . . ,λm on a
Grassmannian G(k,n) and any generalized secant ﬂags F 1
• , . . . ,F m
• that are secant to a rational
normal curve γ along disjoint intervals, the intersection

Xλ1F 1
• ∩ Xλ2F 2
• ∩ · · · ∩ XλmF m
•
is transverse and consists of d(λ1, . . . ,λm) real points.

This includes the Secant Conjecture as the case when all of the ﬂags are secant ﬂags, but it
also includes Theorem 2.1, which is when all ﬂags are osculating. Many of the computations in
our experiment tested instances of this conjecture where one or two ﬂags were osculating while
the rest were secant ﬂags. This choice was made to make the computation feasible for some
Schubert problems.
There is also a Generalized Cosecant Conjecture and a corresponding version of Theorem 3.4,
which we do not formulate.

4. The problem of four secant lines

We give an in-depth look at the Schubert problem 4 = 2 on G(2,4) where denotes the
Schubert condition that a two-plane in C4 meets a ﬁxed two-plane nontrivially. Equivalently,
4 = 2 is the Schubert problem of lines in P3 that meet four ﬁxed lines. Let γ : R → P3 be
a rational normal curve. We consider the lines in P3 that meet four lines ℓ1,ℓ2,ℓ3,ℓ4 which are
secant to γ.
For s1, s2 ∈ R let ℓ(s1,s2) denote the secant line to γ through γ(s1), γ(s2). Given s1 < · · · <
s8, the Secant Conjecture (which is in this case a theorem of Eremenko, et al. [10]) asserts that
both lines meeting the four ﬁxed lines

ℓ(s1,s2) , ℓ(s3,s4) , ℓ(s5,s6) , ℓ(s7,s8)

are real. We investigate phenomena beyond the Secant Conjecture by letting ρ be a permutation
of {1, . . . ,8} and taking ℓ1,ℓ2,ℓ3,ℓ4 to be ℓ(sρ(1), sρ(2)), . . . , ℓ(sρ(7), sρ(8)).

THE SECANT CONJECTURE IN THE REAL SCHUBERT CALCULUS 9

There are 17 combinatorial conﬁgurations of four secant lines along γ ≃ S1. These are
indicated by the chord diagrams in Table 1, which shows the number of real solutions found
when we computed 100,000 instances of each conﬁguration. For most conﬁgurations, we only

Table 1. Conﬁgurations of four secant lines with results of an experiment.

real 0 23723 29398
roots 2 100000 100000 76277 100000 100000 100000 100000 70602

0 52395 65783
2 100000 100000 100000 47605 100000 100000 100000 34217 100000

observed real solutions, and in only four conﬁgurations did we ﬁnd any non-real solutions. We
will give a simple explanation of this observation.
Counting constants shows there is a unique doubly-ruled quadric surface Q that contains the
lines ℓ1, ℓ2, and ℓ3 in one ruling, as shown in Figure 1. The two lines of the second ruling of Q

γ ❍❍❍❥

ℓ1
 ℓ2

ℓ3

Figure 1. Quadric through three secant lines.

through the two points of intersection of ℓ4 with Q are the solutions to the Schubert problem
4 = 2 for these four secant lines.
The quadric Q divides its complement in RP3 into two connected components (the domains
where the quadratic form is positive or negative), called the sides of Q. Three lines ℓ1, ℓ2, ℓ3
give six points of secancy which are the intersections of γ with Q and which divide γ into six
segments that alternate between the two sides of Q. If the fourth secant line ℓ4 has its two
points of secancy lying on opposite sides of Q, then ℓ4 has a real intersection with Q, so that
the Schubert problem has one (and hence two) real solutions. The points of secancy of ℓ4 lie

10 GARC´IA-PUENTE, HEIN, HILLAR, MART´IN DEL CAMPO, RUFFO, SOTTILE, AND TEITLER

on opposite sides of Q if in the interval between the two points of secancy, the curve γ crosses
Q an odd number of times. That is, the interval contains an odd number of points of secancy
of the lines ℓ1, ℓ2, and ℓ3.
This simple topological argument shows that if at least one of the four secant lines has such an
odd interval of secancy, then the Schubert problem will have only real solutions, independently
of the actual positions of the secant lines. Twelve of the 17 conﬁgurations have at least one odd
interval of secancy, and therefore will always give two real solutions. Four conﬁgurations with
only even intervals of secancy were observed to have either zero or two real solutions. Only the
conﬁguration with disjoint intervals of secancy has even intervals of secancy, and yet has only
real solutions. This deeper fact was proven in [10].

5. Overlap number

For most Schubert problems, the number of diﬀerent conﬁgurations of secant ﬂags is astro-
nomical. Consider the problem 4 · 2 = 12 on the Grassmannian of 3-planes in 7-space.
The condition has relevant subspace F4 and the condition has relevant subspace F5. The
resulting 26 points of secancy have at least
⌈( 26
4,4,4,4,5,5

) · 1
4! · 1
2! · 1
26 · 1
2
 ⌉ = 3,381,948,761,563

combinatorially diﬀerent conﬁgurations. To cope with this complexity, we introduce a statistic
on these conﬁgurations—the overlap number—which is zero if and only if the ﬂags are disjoint,
and we tabulate the results of our experiment using this statistic.
In an instance of a Schubert problem λ1, . . . ,λm with relevant subspaces of respective dimen-
sions i1, . . . ,im, to deﬁne the relevant subspaces of the jth secant ﬂag,

F j
1 ⊊ F j
2 ⊊ · · · ⊊ F j
ij ,

we need a choice of an ordered set Tj of ij points of γ. The overlap number measures how much
these sets of points T1, . . . ,Tm ⊂ γ overlap.
Let T be their union. Since γ is topologically a circle, removing a point p ∈ γ \ T , we may
assume that T1, . . . ,Tm ⊂ R. Each set Tj deﬁnes an interval Ij of R and we let oj be the number
of points of T \ Tj lying in Ij. This sum Σ := o1 + · · · + om depends upon p ∈ γ \ T , and the
overlap number is the minimum of these sums as p varies.
For example, consider a Schubert problem with relevant subspaces of dimensions 3, 2, and
2. Suppose that we have chosen seven points on γ in groups of 3, 2, and 2. This is represented
schematically on the left in Figure 2, in which γ is a circle, and the points in the sets T1, T2,
and T3 are represented by circles ( ), squares ( ), and triangles ( ), respectively. For each
of three points p1, p2, and p3 of γ, we compute the number oi and their sum Σ, displaying
the results in the table on the right-hand side of Figure 2. The minimum of the sum Σ for all
choices of points is achieved by p3.
If one (or more) of the ﬂags are osculating, we compute the overlap number by treating the
point of osculation as a point with multiplicity equal to the dimension of the relevant subspace.

THE SECANT CONJECTURE IN THE REAL SCHUBERT CALCULUS 11

Figure 2. Computation of overlap number.

p1 p2

p3
 Σ
p1 3 1 2 6
p2 4 1 2 7
p3 1 1 2 4

6. Experimental evidence for the Secant Conjecture

We tested the Secant Conjecture by conducting a massive experiment whose data are available
on-line [40]. This experiment used symbolic exact arithmetic to compute the number of real
solutions for speciﬁc instances of Schubert problems. These computations are possible because
Schubert problems are readily modeled on a computer, and for those of moderate size, we may
algorithmically determine the number of real solutions with software tools. Our experiment
primarily used the mathematical software Singular [6] and Maple (see [14] for further details
about the implementation of the computations, including a comprehensive list of software tools
used). If the software is reliably implemented, which we believe, then this computation provides
a proof that the given instance has the computed number of real solutions. This procedure may
be semi-automated and run on supercomputers (as described in [14]), which allows us to amass
the considerable evidence we have collected in support of the Secant Conjecture.

6.1. Experimental data. Table 2 shows how many Schubert problems on each Grassmannian
of k-planes in n-space had been studied when we halted the experiment on 26 May 2010. Our

Table 2. Schubert problems studied

k\n−k 2 3 4 5 6
2 1 5 22 81 55
3 5 64 114 79
4 22 107 67
5 81

experiment not only tested the Secant Conjecture but also studied the relationship between
the overlap number and the number of real solutions for many Schubert problems on small
Grassmannians. We computed 2,058,810,000 instances of 703 Schubert problems. About one-
fourth of these (498,737,669) were instances of the (Generalized) Secant Conjecture, and the rest
involved non-disjoint secant ﬂags. The Generalized Secant Conjecture held in every computed
instance. The remaining 1,560,072,331 instances involved secant ﬂags with some overlap in
their intervals of secancy, measured by the overlap number.

12 GARC´IA-PUENTE, HEIN, HILLAR, MART´IN DEL CAMPO, RUFFO, SOTTILE, AND TEITLER

The experiment computed Schubert problems using either 0, 1, or 2 osculating ﬂags, with
the rest secant ﬂags. In the on-line database [40], this number of osculating ﬂags determines
the computation type which is 1, 2, or 3 for 0, 1, or 2 osculating ﬂags. The experiment used
randomly chosen ﬂags, which were generated using random generator seeds that are stored in
our database, so that all computations are reproducible.
Table 3 shows part of the data we obtained testing the full Secant Conjecture for the Schubert
problem 4 · 2 = 12 on G(3,7). We used 7.52 gigahertz-years to compute 10,000,000 instances

Table 3. Experimental data for 4 · 2 = 12 with all secant ﬂags.

Overlap NumberRealSolutions
\ 0 1 2 3 4 5 6 · · · 9 · · · Total
0 · · · 1 · · · 691
2 9 7 · · · 8 · · · 72857
4 79 917 1990 · · · 524 · · · 523362
6 814 5713 12550 18330 · · · 4531 · · · 1418911
8 635 4646 15947 17180 · · · 6055 · · · 1983639
10 1226 6912 18403 17236 · · · 6801 · · · 1649923
12 2320873 51120 99413 206398 203426 179955 · · · 42883 · · · 4350617
Total 2320873 51120 102088 223748 251252 234698 · · · 60803 · · · 10000000

of this Schubert problem, all involving secant ﬂags. The rows are labeled with the even integers
from 0 to 12, as the number of real solutions has the same parity as the number of complex
solutions. The ﬁrst column with overlap number 0 represents tests of the Secant Conjecture.
Since the only entry is in the row for 12 real solutions, the Secant Conjecture was veriﬁed
in 2,320,873 instances. The column labeled overlap number 1 is empty because ﬂags for this
problem cannot have overlap number 1. Perhaps the most interesting feature is that for overlap
number 2, all computed solutions were real, while for overlap number 3 at least six solutions
were real, and for overlap number 4, at least four were real. It is only with overlap number 9
and above that we computed an instance with no real solutions.
We also computed 200,000,000 instances of this same Schubert problem with four secant ﬂags
(for the Schubert variety X ) and two osculating ﬂags (for the Schubert variety X ). These
data are compiled in Table 4. This computation took 261 gigahertz-days—twenty times as many
instances as Table 3 in about one-tenth of the time. This speed-up occurs because using two
osculating ﬂags gives a formulation with only four variables instead of 12. This computation
tested the Generalized Secant Conjecture; its computed instances form the ﬁrst column. As the
only entry in that column is in the row for 12 real solutions, the Generalized Secant Conjecture
was veriﬁed in 49,743,228 instances. As with Table 3 there is visibly an inner border to these
data, but for this computation there are instances with no real solutions starting with overlap
number eight.

6.2. Computing Schubert problems. A k × (n−k) matrix X ∈ Ck×(n−k) determines a
general point in G(k,n), namely the row space H of the k × n matrix (also written H)

(6.1) H := (Ik : X) .

THE SECANT CONJECTURE IN THE REAL SCHUBERT CALCULUS 13

Table 4. Experimental data for 6 · 2 = 12 with two osculating ﬂags.

Overlap NumberRealSolutions
\ 0 1 2 3 4 5 6 · · · Total
0 · · · 13894
2 3799 19 · · · 1357929
4 24756 93214 186521 · · · 12146335
6 210843 495977 731938 · · · 29925437
8 254875 640663 508884 · · · 36708450
10 153520 442928 229530 · · · 26500908
12 49743228 1171814 2324847 5900258 5944524 3971316 · · · 93347047
Total 49743228 1171814 2324847 6544252 7621105 5628208 · · · 200000000

If we represent an i-plane Fi as the row space of an i × n matrix Fi of full rank, then

(6.2) dim H ∩ Fi ≥ j ⇐⇒ rank (H
Fi
) ≤ k + i − j ,

which is given by the vanishing of all (k+i−j+1) × (k+i−j+1) subdeterminants. We represent
a ﬂag F• by a full rank n × n matrix whose ﬁrst i rows span Fi. Then (6.2) leads to equations
for the Schubert variety XλF• in the coordinate patch (6.1). In practice, we only need an
(n−k+i−λi) × n matrix, where λi is the last nonzero part of λ.
To represent a secant i-plane, we use an i × n matrix Fi(t1, . . . ,ti) whose jth row is the vector
γ(tj), where t1, . . . ,ti ∈ R, and γ(t) = (1,t, . . . ,t
n−1) is the rational normal curve. Similarly, the
i-plane Fi(t) osculating γ at the point γ(t) is represented by the i × n matrix whose jth row is
γ(j−1)(t).
For example, Conjecture 1.1 involves the Schubert problem 6 = 5 on G(2,5) where is the
Schubert condition of a 2-plane meeting a 3-plane. The solutions are 2-planes spanned by the
ﬁrst two rows of the matrix in (1.1). The last three rows in the matrix are the points γ(si),
γ(ti), γ(ui) that span the 3-plane of a secant ﬂag.
We use the computer algebra system Singular [6] to compute an eliminant of the polynomial
system modeling a given instance of the Schubert problem λ1, . . . ,λm. This is a univariate
polynomial f (x) whose roots are all the x-coordinates of solutions to the Schubert problem in
the patch (6.1). (See, for example, [5, Chap. 2].) By the Shape Lemma [4], when the eliminant
f (x) has degree equal to d(λ1, . . . ,λm) and is square-free, then the solutions to the Schubert
problem are in one-to-one correspondence with the roots of the eliminant f (x), with real roots
corresponding to real solutions. We use the realroot command of the mathematical software
Maple to compute the number of real roots of the eliminant f (x).
If the eliminant does not satisfy these hypotheses, then we compute an eliminant with respect
to a diﬀerent coordinate of the patch (6.1). It is sometimes the case that no coordinate provides
a satisfactory eliminant. This will occur if there is a solution with multiplicity (the Schubert
varieties do not meet transversally) or if the coordinate patch does not contain all solutions.
In general it will occur when the computed instance lies in a discriminant hypersurface in
the space of all instances. When developing and testing our software for this experiment, we

14 GARC´IA-PUENTE, HEIN, HILLAR, MART´IN DEL CAMPO, RUFFO, SOTTILE, AND TEITLER

observed that this situation was extremely rare, and it only occurred when the overlap number
was positive and there were multiple solutions, which agrees with the transversality assertion
in the Secant Conjecture. When our software detects that no coordinate provides a satisfactory
eliminant, it deterministically perturbs the points of secancy, preserving the overlap number,
and repeats this elimination procedure. This has always worked to give an eliminant satisfying
the hypotheses.
As with Tables 3 and 4, working in a diﬀerent set of local coordinates enables us to eﬃciently
compute instances of the Generalized Secant Conjecture 3.5 for one (and sometimes two) os-
culating ﬂags. With one ﬂag osculating at γ(∞), we may use local coordinates as described
in [27].
With two osculating ﬂags, there is a smaller choice of local coordinates available. Suppose
that e1, . . . ,en are the standard basis vectors corresponding to columns of our matrices. Then
the ﬂag F•(∞) osculating the rational normal curve γ at γ(∞) = en and the ﬂag F•(0) osculating
at γ(0) = e1 have

Fi(∞) = span{en+1−i, . . . , en−1, en} and Fi(0) = span{e1, e2, . . . , ei} .

General points in XλF•(∞) ∩ XµF•(0) are represented by k × n matrices where row i has a 1
in column λk+1−i + i, arbitrary entries in subsequent columns up to column n−k−1+i−µi, and
0’s elsewhere. Here is such a matrix with k = 3, n = 8, λ = , and µ = :



1 ∗ ∗ 0 0 0 0 0
0 0 1 ∗ ∗ ∗ 0 0
0 0 0 0 1 ∗ ∗ ∗



 .

6.3. Numerical experimentation. In [13], 25,000 instances of the Shapiro Conjecture for the
Schubert problem 8 = 126 were computed, and for each instance the software alphaCertiﬁed
used 256-bit precision to softly certify that all solutions were real. (A soft certiﬁcate is one
computed with ﬂoating point arithmetic that would be rigorous if computed with exact rational
arithmetic.) The solutions were computed using the software package Bertini [3], which is
based on numerical homotopy continuation [30]. Given a system of n polynomial equations
in n unknowns, Smale’s α-theory [29] gives algorithms for certifying that Newton iterations
applied to an approximate solution will converge to a solution, and also may be used to certify
that the solution is real. As explained in [13], this Schubert problem has such a formulation.
These algorithms are implemented in the software alphaCertiﬁed [13].

7. Lower bounds and inner borders

The most ubiquitous and enigmatic phenomenon that we have observed in our data is the
apparent “inner border” in many of the tables. Typically, we do not observe instances with
zero or few real solutions when the overlap number is small. This is manifested by a prominent
staircase separating observed pairs of (real solutions, overlap number) from unobserved pairs.
This feature is clearly visible in Tables 3 and 4, and in Table 5 for the problem 8 = 14 in
G(2,6). There, it is only with overlap number 8 or larger that we observe instances with two

THE SECANT CONJECTURE IN THE REAL SCHUBERT CALCULUS 15

Table 5. Real solutions vs. overlap number for 8 = 14.

\ 0 1 2 3 4 5 6 · · · Total
0 · · · 4272
2 · · · 127217
4 693 1481 6660 · · · 879658
6 224 510 2541 · · · 2304233
8 526 939 3561 · · · 2914837
10 1052 2074 6985 · · · 2205198
12 1556 2595 7300 · · · 1224667
14 3328772 60860 120625 310819 246910 237704 · · · 5339918
Total 3328772 60860 120625 305870 254509 264751 · · · 15000000

real solutions; and with overlap number 16 or larger, instances with no real solutions. (These
columns are not displayed for reasons of space.)
This problem involves 2-planes meeting eight secant 4-planes. There are over 1018 conﬁgu-
rations of eight secant 4-planes, and hence it is impossible to systematically study all conﬁgu-
rations as in Section 4. This is the case for most of the problems we studied. Because of the
coarseness of our measure of overlap, we doubt it is possible to formulate a meaningful conjec-
ture about this inner border based on our data. Nevertheless, we believe that this problem, like
the problem of four lines, contains rich geometry, with certain conﬁgurations having a lower
bound on the number of real solutions.
There are many meaningful polynomial systems or geometric problems having a non-zero
lower bound on their number of real solutions. These include rational curves interpolating points
on toric del Pezzo surfaces [15, 16, 17, 22, 39], sparse polynomial systems from posets [18, 31],
and some lower bounds in the Schubert calculus [1, 7].
Lower bounds and inner borders were also observed studying the Monotone Conjecture [27,
§ 3.2.2]. The original example of a lower bound was due to Eremenko and Gabrielov [7]. The
Wronskian of linearly independent polynomials f1(t),f2(t), . . . ,fk(t) of degree n−1,

W(f1,f2, . . . ,fk) := det
 





f1(t) f ′
1(t) f ′′
1 (t) · · · f (k−1)
1 (t)
f2(t) f ′
2(t) f ′′
2 (t) · · · f (k−1)
2 (t)
. . . . . . .
fk(t) f ′
k(t) f ′′
k (t) · · · f (k−1)
k (t)





 ,

has degree k(n−k), which gives a ﬁnite map W : G(k, Cn−1[t]) −→ Pk(n−k) with the general
ﬁber consisting of d(
 k(n−k)) (see (3.1)) linear spaces of polynomials. Theorem 2.1 implies that
if w(t) is a polynomial with k(n−k) distinct real roots then each of the d( k(n−k)) points in
the ﬁber of W over w(t) is real. Eremenko and Gabrielov showed that if n is odd, there is a
non-trivial lower bound on the number of real spaces of polynomials in the ﬁber of W over any
polynomial w(t) with real coeﬃcients.

16 GARC´IA-PUENTE, HEIN, HILLAR, MART´IN DEL CAMPO, RUFFO, SOTTILE, AND TEITLER

Azar and Gabrielov [1] studied the problem 2n−4 in G(n−2,n) of (n−2)-planes in Cn which
meet one secant line and 2n−5 tangent lines. When the interval of secancy contains no tangent
points, this is an instance of the Generalized Secant Conjecture 3.5. They establish lower
bounds on the number of real solutions which depend upon the conﬁguration of the points of
secancy and tangency.
 8. Gaps

The Schubert problem 4 = 6 on G(4,8) involves 4-planes whose intersection with each of four
general 4-planes is at least two-dimensional. We computed 1,000,000 instances of this problem,
obtaining the results in Table 6. A system of real polynomial equations with 6 solutions can,

Table 6. Real solutions vs. overlap number for W 4 = 6.

0 1 2 3 4 5 6 · · · Total
0 0
2 1441 7730 14277 16636 · · · 147326
4 0
6 280304 13131 25708 62833 55919 57719 · · · 852674
Total 280304 0 13131 27149 70563 70196 74355 · · · 1000000

a priori, have 0, 2, 4, or 6 real solutions; yet, strikingly, this Schubert problem only has 2 or 6
real solutions, never 0 or 4.
Although our observations involved only secant ﬂags, this phenomenon holds for any real ﬂags.
As we describe below, this follows from ideas in Vakil’s discussion of this Schubert problem in
[37, §3.13]. (Vakil’s discussion, however, focuses on explaining a diﬀerent phenomenon, namely,
Derksen’s observation that the Galois group of this Schubert problem is deﬁcient, i.e., smaller
than the symmetric or alternating group.)
We consider the auxiliary Schubert problem 4 = 4 on G(2,8), counting 2-planes which
meet four general 4-planes. Given 4-planes W1, . . . ,W4, let P1, . . . ,P4 be the 2-planes which
meet them. Then the solutions to the original Schubert problem W 4 = 6 are precisely the 6
sums of the form Pi + Pj. Such a sum is real if and only if Pi and Pj are each real or if Pi and
Pj are a pair of complex conjugate subspaces.
If the Wi are real, then there can be 0, 1, or 2 complex conjugate pairs among the Pi. Then
the number of solutions Pi + Pj which are real is, respectively, 6, 2, and 2. This explains the
observations in Table 6.
This is the ﬁrst in a family of Schubert problems in G(4,2n) for n ≥ 4 with such gaps in
their numbers of real solutions. These involve enumerating the 4-planes which have at least a
two-dimensional intersection with each of four general n-planes in C2n. For each, there is an
auxiliary Schubert problem on G(2,2n) of 2-planes meeting four general n-planes. This will have
n solutions, and the solutions to the original problem are 4-planes spanned by pairs of solutions
to the auxiliary problem. The original problem will have (
n
2) solutions, corresponding to pairs
of solutions to the auxiliary problem. A solution is real either when both elements of the pair

THE SECANT CONJECTURE IN THE REAL SCHUBERT CALCULUS 17

are real or when the pair consists of complex conjugate solutions. We remark that the auxiliary
problem may have any number r of real solutions, where 0 ≤ r ≤ n and n−r is even—this
may be deduced from the description of the Schubert problem in terms of elementary geometry
given, for example, in [32, § 8.1]. These restrictions are identical to restrictions on the number
of real quadratic factors of a general real polynomial of degree n, as in [31, Theorem 7.8]. We
summarize this discussion.

Theorem 8.1. The Schubert problem of 4-planes that have at least a two-dimensional inter-
section with each of four general real n-planes in C2n has (
n
2) solutions. The number of real
solutions is (r
2
) + c ,

where the auxiliary problem of 2-planes meeting each of four general real n-planes in C2n has
r real solutions and c pairs of complex conjugate solutions and r + 2c = n.

References

[1] M. Azar and A. Gabrielov, Lower bounds in B. and M. Shapiro conjecture, Discr. Comput. Geometry
(2011), DOI: 10.1007/s00454–010–9314–8.
[2] D. J. Bates, F. Bihan, and F. Sottile, Bounds on the number of real solutions to polynomial equations, Int.
Math. Res. Not. IMRN (2007), no. 23, Art. ID rnm114, 7.
[3] D.J. Bates, J.D. Hauenstein, A.J. Sommese, and C.W. Wampler, Bertini: Software for numerical algebraic
geometry, Available at http://www.nd.edu/~sommese/bertini.
[4] E. Becker, M.G. Marinari, T. Mora, and C. Traverso, The shape of the Shape Lemma, Proceedings ISSAC-
94, 1993, pp. 129–133.
[5] David A. Cox, John Little, and Donal O’Shea, Using algebraic geometry, second ed., Graduate Texts in
Mathematics, vol. 185, Springer, 2005.
[6] W. Decker, G.-M. Greuel, G. Pﬁster, and H. Sch¨onemann, Singular 3-1-1 — A computer algebra system
for polynomial computations, 2010, http://www.singular.uni-kl.de.
[7] A. Eremenko and A. Gabrielov, Degrees of real Wronski maps, Discrete Comput. Geom. 28 (2002), no. 3,
331–347.
[8] , Rational functions with real critical points and the B. and M. Shapiro conjecture in real enumerative
geometry, Ann. of Math. (2) 155 (2002), no. 1, 105–129.
[9] , Elementary proof of the B. and M. Shapiro conjecture for rational functions, Notions of Positivity
and the Geometry of Polynomials (Petter Br¨and´en, Mikael Passare, and Miha Putinar, eds.), Springer
Base, 2011, pp. 167–178.
[10] A. Eremenko, A. Gabrielov, M. Shapiro, and A. Vainshtein, Rational functions and real Schubert calculus,
Proc. Amer. Math. Soc. 134 (2006), no. 4, 949–957 (electronic).
[11] W. Fulton, Young tableaux, London Mathematical Society Student Texts, vol. 35, Cambridge University
Press, Cambridge, 1997.
[12] W. Fulton and P. Pragacz, Schubert varieties and degeneracy loci, Lecture Notes in Mathematics, vol. 1689,
Springer-Verlag, Berlin, 1998.
[13] J.D. Hauenstein and F. Sottile, alphacertiﬁed: certifying solutions to polynomial systems, ACM Transactions
on Mathematical Software, to appear, 2011.
[14] C. Hillar, L. Garc´ıa-Puente, A. Mart´ın del Campo, J. Ruﬀo, Z. Teitler, S. L. Johnson, and F. Sottile,
Experimentation at the frontiers of reality in Schubert calculus, Gems in Experimental Mathematics, Con-
temporary Mathematics, vol. 517, Amer. Math. Soc., Providence, RI, 2010, pp. 365–380.

18 GARC´IA-PUENTE, HEIN, HILLAR, MART´IN DEL CAMPO, RUFFO, SOTTILE, AND TEITLER

[15] I. V. Itenberg, V. M. Kharlamov, and E. I. Shustin, Welschinger invariant and enumeration of real rational
curves, Int. Math. Res. Not. (2003), no. 49, 2639–2653.
[16] , Logarithmic equivalence of the Welschinger and the Gromov-Witten invariants, Uspekhi Mat. Nauk
59 (2004), no. 6(360), 85–110.
[17] , A Caporaso-Harris type formula for Welschinger invariants of real toric del Pezzo surfaces, Com-
ment. Math. Helv. 84 (2009), no. 1, 87–126.
[18] M. Joswig and N. Witte, Products of foldable triangulations, Adv. Math. 210 (2007), no. 2, 769–796.
[19] A.G. Khovanskii, Fewnomials, Trans. of Math. Monographs, 88, AMS, 1991.
[20] S. L. Kleiman, The transversality of a general translate, Compositio Math. 28 (1974), 287–297.
[21] S. L. Kleiman and Dan Laksov, Schubert calculus, Amer. Math. Monthly 79 (1972), no. 10, 1061–1082.
[22] G. Mikhalkin, Enumerative tropical algebraic geometry in R2, J. Amer. Math. Soc. 18 (2005), no. 2, 313–377
(electronic).
[23] E. Mukhin, V. Tarasov, and A. Varchenko, The B. and M. Shapiro conjecture in real algebraic geometry
and the Bethe ansatz, Ann. of Math. (2) 170 (2009), no. 2, 863–881.
[24] , On reality property of Wronski maps, Conﬂuentes Math. 1 (2009), no. 2, 225–247.
[25] , Schubert calculus and representations of the general linear group, J. Amer. Math. Soc. 22 (2009),
no. 4, 909–940.
[26] K. Purbhoo, Reality and transversality for Schubert calculus in OG(n,2n + 1), Math. Res. Lett. 17 (2010),
no. 6, 1041–1046.
[27] J. Ruﬀo, Y. Sivan, E. Soprunova, and F. Sottile, Experimentation and conjectures in the real Schubert
calculus for ﬂag manifolds, Experiment. Math. 15 (2006), no. 2, 199–221.
[28] H. Schubert, Anzahl-Bestimmungen f¨ur lineare R¨aume beliebiger Dimension, Acta. Math. 8 (1886), 97–118.
[29] S. Smale, Newton’s method estimates from data at one point, The merging of disciplines: new directions in
pure, applied, and computational mathematics (Laramie, Wyo., 1985), Springer, New York, 1986, pp. 185–
196.
[30] A.J. Sommese and C.W. Wampler, II, The numerical solution of systems of polynomials arising in engi-
neering and science, World Scientiﬁc Publishing Co. Pte. Ltd., Hackensack, NJ, 2005.
[31] E. Soprunova and F. Sottile, Lower bounds for real solutions to sparse polynomial systems, Adv. Math. 204
(2006), no. 1, 116–151.
[32] F. Sottile, Enumerative geometry for the real Grassmannian of lines in projective space, Duke Math. J. 87
(1997), no. 1, 59–85.
[33] , Real Schubert calculus: polynomial systems and a conjecture of Shapiro and Shapiro, Experiment.
Math. 9 (2000), no. 2, 161–182.
[34] , Some real and unreal enumerative geometry for ﬂag manifolds, Michigan Math. J. 48 (2000),
573–592.
[35] , Frontiers of reality in Schubert calculus, Bull. Amer. Math. Soc. (N.S.) 47 (2010), no. 1, 31–71.
[36] , Real solutions to equations from geometry, University Lecture Series, vol. 57, American Mathe-
matical Society, 2011.
[37] R. Vakil, Schubert induction, Ann. of Math. (2) 164 (2006), no. 2, 489–512.
[38] J. Verschelde, Numerical evidence for a conjecture in real algebraic geometry, Experiment. Math. 9 (2000),
no. 2, 183–196.
[39] J.-Y. Welschinger, Invariants of real rational symplectic 4-manifolds and lower bounds in real enumerative
geometry, C. R. Math. Acad. Sci. Paris 336 (2003), no. 4, 341–344.
[40] Secant experimental project, 2010, http://www.math.tamu.edu/~secant/secant/flagview.php.

THE SECANT CONJECTURE IN THE REAL SCHUBERT CALCULUS 19

Luis Garc´ıa-Puente, Department of Mathematics and Statistics, Sam Houston State Univer-
sity, Huntsville, TX 77341, USA
E-mail address: lgarcia@shsu.edu
URL: http://www.shsu.edu/~ldg005

Nickolas Hein, Department of Mathematics, Texas A&M University, College Station, Texas
77843, USA
E-mail address: nhein@math.tamu.edu
URL: http://www.math.tamu.edu/~nhein

Christopher Hillar, Mathematical Sciences Research Institute, 17 Gauss Way, Berkeley,
CA 94720-5070, USA
E-mail address: chillar@msri.org
URL: http://www.msri.org/people/members/chillar

Abraham Mart´ın del Campo, Department of Mathematics, Texas A&M University, College
Station, Texas 77843, USA
E-mail address: asanchez@math.tamu.edu
URL: http://www.math.tamu.edu/~asanchez

James Ruffo, Department of Mathematics, Computer Science, & Statistics, State University
of New York, College at Oneonta, Oneonta, NY 13820, USA
E-mail address: ruffojv@oneonta.edu
URL: http://employees.oneonta.edu/ruffojv

Frank Sottile, Department of Mathematics, Texas A&M University, College Station, Texas
77843, USA
E-mail address: sottile@math.tamu.edu
URL: http://www.math.tamu.edu/~sottile

Zach Teitler, Department of Mathematics, Boise State University, Boise, Idaho 83725, USA
E-mail address: zteitler@boisestate.edu
URL: http://math.boisestate.edu/~zteitler
