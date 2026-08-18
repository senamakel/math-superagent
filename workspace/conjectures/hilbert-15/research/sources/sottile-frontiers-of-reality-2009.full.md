<!-- source: https://arxiv.org/pdf/0907.1847 | converted from PDF -->

arXiv:0907.1847v2  [math.AG]  6 Aug 2009
Manuscript, November 29, 2021 ArXiV.org/0907.1847

FRONTIERS OF REALITY IN SCHUBERT CALCULUS

FRANK SOTTILE

Abstract. The theorem of Mukhin, Tarasov, and Varchenko (formerly the Shapiro
conjecture for Grassmannians) asserts that all (a priori complex) solutions to certain
geometric problems in the Schubert calculus are actually real. Their proof is quite
remarkable, using ideas from integrable systems, Fuchsian diﬀerential equations, and
representation theory. There is now a second proof of this result, and it has ramiﬁca-
tions in other areas of mathematics, from curves to control theory to combinatorics.
Despite this work, the original Shapiro conjecture is not yet settled. While it is false as
stated, it has several interesting and not quite understood modiﬁcations and general-
izations that are likely true, and the strongest and most subtle version of the Shapiro
conjecture for Grassmannians remains open.

Introduction

While it is not unusual for a univariate polynomial f with real coeﬃcients to have
some real roots—under reasonable assumptions we expect √deg f real roots [37]—it is
rare for a polynomial to have all of its roots real. In a sense, the only natural example of
a polynomial with all of its roots real is the characteristic polynomial of a real symmetric
matrix, as all eigenvalues of a symmetric matrix are real.
Similarly, when a system of real polynomial equations has ﬁnitely many (a priori
complex) solutions, we expect some, but likely not all, solutions to be real. In fact,
upper bounds on the number of real solutions [1, 33] sometimes ensure that not all
solutions can be real. As before, the most natural example of a system with only
real solutions is the system of equations for the eigenvectors and eigenvalues of a real
symmetric matrix.
Here is another system of polynomial equations that has only real solutions. The
Wronskian of univariate polynomials f0, . . . , fn ∈ C[t] is the determinant

det
 





 f0(t) f1(t) · · · fn(t)
f ′
0(t) f ′
1(t) · · · f ′
n(t)
. . . . . .
f (n)
0 (t) f (n)
1 (t) · · · f (n)
n (t)





 .

Up to a scalar multiple, the Wronskian depends only upon the linear span P of the
polynomials f0, . . . , fn. This scaling retains only the information of the roots and their
multiplicities. Recently, Mukhin, Tarasov, and Varchenko [40] proved the remarkable
(but seemingly innocuous) result.

Theorem 1. If the Wronskian of a vector space P of polynomials has only real roots,
then P has a basis of real polynomials.

2000 Mathematics Subject Classiﬁcation. 14M15, 14N15.
Key words and phrases. Schubert calculus, Bethe ansatz, Wronskian, Calogero-Moser space.
Work of Sottile supported by NSF grant DMS-0701050.
1

2 FRANK SOTTILE

While not immediately apparent, those (n+1)-dimensional subspaces P of C[t] with
a given Wronskian W are the solutions to a system of polynomial equations that de-
pend on the roots of W . In Section 1, we explain how the Shapiro conjecture for
Grassmannians is equivalent to Theorem 1.
The proof of Theorem 1 uses the Bethe ansatz for the (periodic) Gaudin model on
certain modules (representations) of the Lie algebra sln+1C. The Bethe ansatz is a
method to ﬁnd pure states, called Bethe vectors, of quantum integrable systems [21].
Here, that means common eigenvectors for a family of commuting operators called the
Gaudin Hamiltonians which generate a commutative Bethe algebra B. As B commutes
with the action of sln+1C, this also decomposes a module of sln+1C into irreducible
submodules. It includes a set-theoretic map from the Bethe eigenvectors to spaces of
polynomials with a given Wronskian. A coincidence of numbers, from the Schubert
calculus and from representation theory, implies that this map is a bijection. As the
Gaudin Hamiltonians are symmetric with respect to the positive deﬁnite Shapovalov
form, their eigenvectors and eigenvalues are real. Theorem 1 follows as eigenvectors
with real eigenvalues must come from real spaces of polynomials. We describe this in
Sections 2, 3, and 4.
There is now a second proof [45] of Theorem 1, also passing through integrable
systems and representation theory. It provides a deep connection between the Schubert
calculus and the representation theory of sln+1C, strengthening Theorem 1 to include
transversality.
The geometry behind the statement of Theorem 1 appears in many other guises, some
of which we describe in Section 6. These include linear series on the projective line [9],
rational curves with prescribed ﬂexes [32], and the feedback control of a system of linear
diﬀerential equations [5, 12]. A special case of the Shapiro conjecture concerns rational
functions with prescribed critical points, and was proved in this form by Eremenko
and Gabrielov [13]. They showed that a rational function whose critical points lie on a
circle in the Riemann sphere maps that circle to another circle. Using the strengthening
of Theorem 1 involving transversality, Purbhoo [49] discovered that the fundamental
combinatorial algorithms on Young Tableaux come from the monodromy of the map
that takes spaces of polynomials to their Wronskians.
A generalization of Theorem 1 by Mukhin, Tarasov, and Varchenko [44] implies the
following attractive statement from matrix theory. Let b0, b1, . . . , bn be distinct real
numbers, α0, . . . , αn be complex numbers, and consider the matrix

Z :=
 




 α0 (b0 − b1)−1 · · · (b0 − bn)−1

(b1 − b0)−1 α1 · · · (b1 − bn)−1
. . . . . .
(bn − b0)−1 (bn − b1)−1 · · · αn
 



 .

Theorem 2. If Z has only real eigenvalues, then α1, . . . , αn are real.

Unlike its proof, the statement of Theorem 2 has nothing to do with Schubert calculus
or representations of sln+1C or integrable systems, and it remains a challenge to prove
it directly. We discuss this in Section 5.
The statement and proof of Theorem 1 is only part of this story. Theorem 1 settles (for
Grassmannians) a conjecture in Schubert calculus made by Boris Shapiro and Michael
Shapiro in 1993/4. While this Shapiro conjecture is false for most other ﬂag manifolds,

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 3

there are appealing corrections and generalizations supported by theoretical evidence
and by overwhelming computational evidence, and the strongest and most subtle form
remains open. We sketch this in Section 7.

First steps: the problem of four lines. We close this Introduction by illustrat-
ing the Schubert calculus and the Shapiro conjecture with some beautiful geometry.
Consider the set of all lines in three-dimensional space. This set (a Grassmannian) is
four-dimensional, which we may see by counting the degrees of freedom for a line ℓ as
follows. Fix planes Π and Π
′ that meet ℓ in points p and p′ as shown.

ℓ
 p
 p′
 Π
Π
′

Since each point p, p′ has two degrees of freedom to move within its plane, we see that
the line ℓ enjoys four degrees of freedom.
Similarly, the set of lines that meet a ﬁxed line is three-dimensional. More parameter
counting tells us that if we ﬁx four lines, then the set of lines that meet each of our ﬁxed
lines will be zero-dimensional. That is, it consists of ﬁnitely many lines. The Schubert
calculus gives algorithms to determine this number of lines. We instead use elementary
geometry to show that this number is 2.
The Shapiro conjecture asserts that if the four ﬁxed lines are chosen in a particular
way, then both solution lines will be real. This special choice begins by specifying
a twisted cubic curve, γ. While any twisted cubic will do, we’ll take the one with
parametrization

(1) γ : t ↦−→ (6t
2 − 1, 7
2 t
3 + 3
2 t, 3
2t − 1
2t
3) .

Our ﬁxed lines will be four lines tangent to γ.
We understand the lines that meet our four tangent lines by ﬁrst considering lines
that meet three tangent lines. We are free to ﬁx the ﬁrst three points of tangency to be
any of our choosing, for instance, γ(−1), γ(0), and γ(1). Then the three lines ℓ(−1),
ℓ(0), and ℓ(1) tangent at these points have parametrizations

(−5 + s, 5 − s, −1) , (−1, s, s) , and (5 + s, 5 + s, 1) for s ∈ R.

These lines all lie on the hyperboloid H of one sheet deﬁned by

(2) x
2 − y2 + z2 = 1 ,

which has two rulings by families of lines. The lines ℓ(−1), ℓ(0), and ℓ(1) lie in one
family, and the other family consists of the lines meeting ℓ(−1), ℓ(0), and ℓ(1). This
family is drawn on the hyperboloid H in Figure 1.
The lines that meet ℓ(−1), ℓ(0), ℓ(1), and a fourth line ℓ(s) will be those in this second
family that also meet ℓ(s). In general, there will be two such lines, one for each point of
intersection of line ℓ(s) with H, as H is deﬁned by the quadratic polynomial (2). The

4 FRANK SOTTILE

remarkable geometric fact is that every such tangent line, ℓ(s) for s ̸∈ {−1, 0, 1}, will
meet the hyperboloid in two real points. We illustrate this when s = 0.31 in Figure 1,
highlighting the two solution lines.

ℓ(s) ℓ(1)

ℓ(−1)

ℓ(0)

γ(s)
 
 
 
 
 
 
 
 
  ✒

γ
 H
solutions
PPPq❅
❅
❅
❅
❅
❅❘

Figure 1. The problem of four lines.

The Shapiro conjecture and its extensions claim that this reality always happens:
If the conditions for a Schubert problem are chosen in a particular way relative to a
rational normal curve (here, tangent lines to the twisted cubic curve γ of (1)), then
all solutions will be real. When the Schubert problem comes from a Grassmannian
(like this problem of four lines), the Shapiro conjecture is true—this is the theorem of
Mukhin, Tarasov, and Varchenko. For most other ﬂag manifolds, it is known to fail,
but in very interesting ways.

Acknowledgments. We thank those who have helped us to understand this story
and to improve this exposition. In particular, we thank Eugene Mukhin, Alexander
Varchenko, Milen Yakimov, Aaron Lauve, Zach Teitler, and Nickolas Hein.

1. The Shapiro conjecture for Grassmannians

Let Cd[t] be the set of complex polynomials of degree at most d in the indeterminate
t, a vector space of dimension d+1. Fix a positive integer n < d and let G(n, d) be
the set of all (n+1)-dimensional linear subspaces P of Cd[t]. This Grassmannian is a
complex manifold of dimension (n+1)(d−n) [23, Ch. 1.5].
The main character in our story is the Wronski map, which associates to a point
P ∈ G(n, d) the Wronskian of a basis for P . If {f0(t), . . . , fn(t)} is a basis for P , its

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 5

Wronskian is the determinant of the derivatives of the basis,

(1.1) Wr(f0, . . . , fn) := det
 





f0 f ′
0 · · · f (n)
0
f1 f ′
1 · · · f (n)
1
. . . . . .
fn f ′
n · · · f (n)
n
 




 ,

which is a nonzero polynomial of degree at most (n+1)(d−n). This does not quite
deﬁne a map G(n, d) → C(n+1)(d−n)[t], as choosing a diﬀerent basis for P multiplies
the Wronskian by a nonzero constant. If we consider the Wronskian up to a nonzero
constant, we obtain the
 Wronski map

(1.2) Wr : G(n, d) −→ P(C(n+1)(d−n)[t]) ≃ P(n+1)(d−n) ,

where P(V ) denotes the projective space consisting of all 1-dimensional linear subspaces
of a vector space V .
We restate Theorem 1, the simplest version of the Theorem of Mukhin, Tarasov, and
Varchenko [40].

Theorem 1. If the Wronskian of a space P of polynomials has only real roots, then P
has a basis of real polynomials.

The problem of four lines in the Introduction is a special case of Theorem 1 when
d = 3 and n = 1. To see this, note that if we apply an aﬃne function a + bx + cy + dz to
the curve γ(t) of (1), we obtain a cubic polynomial in C3[t], and every cubic polynomial
comes from a unique aﬃne function. A line ℓ in C3 (actually in P3) is cut out by
a two-dimensional space of aﬃne functions, which gives a 2-dimensional space Pℓ of
polynomials in C3[t], and hence a point Pℓ ∈ G(1, 3).
It turns out that the Wronskian point Pℓ ∈ G(1, 3) is a quartic polynomial with a
root at s ∈ C if and only if the corresponding line ℓ meets the line ℓ(s) tangent to the
curve γ at γ(s). Thus a line ℓ meets four lines tangent to γ at real points if and only
if the Wronskian of Pℓ ∈ G(1, 3) vanishes at these four points. Since these points are
real, Theorem 1 implies that Pℓ has a basis of real polynomials. Thus ℓ is cut out by
real aﬃne functions, and hence is real.

1.1. Geometric form of the Shapiro conjecture. Let P ∈ G(n, d) be a subspace.
We consider the order of vanishing at a point s ∈ C of polynomials in a basis for P .
There will be a minimal order a0 of vanishing for these polynomials. Suppose that f0
vanishes to this order. Subtracting an appropriate multiple of f0 from each of the other
polynomials, we may assume that they vanish to order greater than a0 at s. Let a1 be
the minimal order of vanishing at s of these remaining polynomials. Continuing in this
fashion, we obtain a basis f0, . . . , fn of P and a sequence

0 ≤ a0 < a1 < · · · < an ≤ d ,

where fi vanishes to order ai at s. Call this sequence aP (s) the ramiﬁcation of P at s.
For a sequence a : 0 ≤ a0 < · · · < an ≤ d, write Ω
◦
a(s) for the set of points P ∈ G(n, d)
with aP (s) = a, which is a Schubert cell of G(n, d). It has codimension

|a| := a0 + a1−1 + · · · + an−n ,

6 FRANK SOTTILE

as may be seen by expressing the basis f0, . . . , fn of P in terms of the basis {(t − s)i |
i = 0, . . . , d} of Cd[t]. Since f (i)
j vanishes to order at least aj − i at s and f (i)
i vanishes
to order exactly ai − i at s, the Wronskian of a subspace P ∈ Ω
◦
a(s) vanishes to order
exactly |a| at s.
Let G(n, d)◦ be the dense open subset of G(n, d) consisting of those P having a basis
f0, . . . , fn where fi has degree d−n+i. When P ∈ G(n, d)◦, we obtain the Pl¨ucker
formula for the total ramiﬁcation of a general subspace P of Cd[t],

(1.3) dim G(n, d) = ∑

s∈C |aP (s)| .

In general, the total ramiﬁcation of P is bounded by the dimension of G(n, d). (One
may also deﬁne ramiﬁcation at inﬁnity for subspaces P ̸∈ G(n, d)◦ to obtain the Pl¨ucker
formula in its full generality.) If aP (s) : 0 < 1 < · · · < n, so that |aP (s)| = 0, then P
is unramiﬁed at s. Theorem 1 states that if a subspace P ∈ G(n, d) is ramiﬁed only at
real points, then P has a basis of real polynomials.
We introduce some more geometry. Let W = ∏

s(t − s)|aP (s)| be the Wronskian of P .
Then P ∈ ⋂

s : W (s)=0 Ω
◦
aP (s)(s) ,

and this intersection consists of all subspaces with the same ramiﬁcation as P . In
particular, P lies in the intersection of the closures of these Schubert cells, which we
now describe. For each s ∈ C, Cd[t] has a complete ﬂag of subspaces

F•(s) : C · (t−s)d ⊂ C1[t] · (t−s)d−1 ⊂ · · · ⊂ Cd−1[t] · (t−s) ⊂ Cd[t] .

More generally, a ﬂag F• is a sequence of subspaces

F• : F1 ⊂ F2 ⊂ · · · ⊂ Fd ⊂ Cd[t] ,

where Fi has dimension i. For a sequence a and a ﬂag F•, the Schubert variety

(1.4) {P ∈ G(n, d) | dim (P ∩ Fd+1−aj ) ≥ n+1−j, for j = 0, 1, . . . , n} ,

is a subvariety of G(n, d), written ΩaF•. It consists of linear subspaces P having special
position (encoded by a) with respect to the ﬂag F•. Since dim(P ∩Fd+1−i(s)) counts the
number of linearly independent polynomials in P that vanish to order at least i at s, we
see that Ω
◦
a(s) ⊂ ΩaF•(s). More precisely, ΩaF•(s) is the closure of the Schubert cell
Ω
◦
a(s) and it is the disjoint union of cells Ω
◦
b(s) for b ≥ a, where ≥ is componentwise
comparison.
Given sequences a
(1), . . . , a
(m) and ﬂags F (1)
• , . . . , F (m)
• , the intersection

(1.5) Ωa(1)F (1)
• ⋂ Ωa(2)F (2)
• ⋂ · · · ⋂ Ωa(m)F (m)
•

consists of those linear subspaces P ∈ G having speciﬁed position a
(i) with respect
to the ﬂag F (i)
• , for each i = 1, . . . , m. Kleiman [34] showed that if the ﬂags F (i)
• are
general, then the intersection (1.5) is (generically) transverse.
A Schubert problem is a list A := (a
(1), . . . , a
(m)) of sequences satisfying

|a
(1)| + · · · + |a
(m)| = (n+1)(d−n) ( = dim G(n, d) ) .

Given a Schubert problem, Kleiman’s Theorem implies that a general intersection (1.5)
will be zero-dimensional and thus consist of ﬁnitely many points. By transversality, the

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 7

number δ(A) of these points is independent of choice of general ﬂags. The Schubert
calculus [35], through the Littlewood-Richardson rule [18], gives algorithms to determine
δ(A).
We mention an important special case. Let ι : 0 < 1 < · · · < n−1 < n+1 be the
unique ramiﬁcation sequence with |ι| = 1, and write ιn,d for the Schubert problem in
which ι occurs (n+1)(d−n) times. Schubert [54] gave the formula

(1.6) δ(ιn,d) = [(n+1)(d−n)]! 1!2! · · · n!
(d−n)!(d−n+1)! · · · d! .

By the Pl¨ucker Formula (1.3), the total ramiﬁcation (aP (s) : |aP (s)| > 0) of a sub-
space P ∈ G(n, d)◦ is a Schubert problem. Let W be the Wronskian of P . We would
like the intersection containing P ,

(1.7) ⋂

s : W (s)=0 ΩaP (s)F•(s) ,

to be transverse and zero-dimensional. However, Kleiman’s Theorem does not apply,
as the ﬂags F•(s) for s a root of W are not generic. For example, in the problem of four
lines, if the Wronskian is t
4 − t, then the corresponding intersection (1.7) of Schubert
varieties is not transverse. (This has been worked out in detail in [9, §9].)
We can see that this intersection (1.7) is however always zero-dimensional. Note
that any positive-dimensional subvariety meets ΩιF•, for any ﬂag F•. (This is because,
for example, ΩιF• is a hyperplane section of G(n, d) in its Pl¨ucker embedding into
projective space.) In particular, if the intersection (1.7) is not zero-dimensional, then
given a point s ∈ P1 with W (s) ̸= 0, there will be a point P ′ in (1.7) which also lies in
ΩιF•(s). But then the total ramiﬁcation of P ′ does not satisfy the Pl¨ucker formula (1.3),
as its ramiﬁcation strictly contains the total ramiﬁcation of P .
A consequence of this argument is that the Wronski map (1.2) is a ﬂat, ﬁnite map.
In particular, it has ﬁnite ﬁbers. The intersection number δ(ιn,d) in (1.6) is an upper
bound for the cardinality of a ﬁber. By Sard’s Theorem, this upper bound is obtained
for generic Wronskians. An argument that proves this in somewhat greater generality
was given by Eisenbud and Harris [9].

Theorem 1.8. There are ﬁnitely many spaces of polynomials P ∈ G(n, d) with a given
Wronskian. For a general polynomial W (t) of degree (n+1)(d−n), there are exactly
δ(ιn,d) spaces of polynomials with Wronskian W (t).

When W has distinct roots, these spaces of polynomials are exactly the points in the
intersection (1.7), where aP (s) = ι at each root s of W . A limiting argument, in which
the roots of the Wronskian are allowed to collide one-by-one, proves a local form of
Theorem 1. We say that the roots s = s1, . . . , s(n+1)(d−n) of the Wronskian are clustered
if, up to an automorphism of RP1, they satisfy

(1.9) 0 < s1 ≪ s2 ≪ · · · ≪ s(n+1)(d−n) .

Theorem 1.10 ([61]). If the roots of a polynomial W (t) of degree (n+1)(d−n) are real,
distinct, and clustered, then there are δ(ιn,d) real spaces of polynomials with Wronskian
W (t) and the intersection (1.7) is transverse.

We noted that the intersection (1.7) is not transverse when d = 3, n = 1, and
W (t) = t
4 − t. It turns out that it is always transverse when the roots of the Wronskian

8 FRANK SOTTILE

are distinct and real. This is the stronger form of the Theorem of Mukhin, Tarasov,
and Varchenko, proven in [45].

Theorem 1.11. For any Schubert problem A = (a
(1), . . . , a
(m)) and any distinct real
numbers s1, . . . , sm, the intersection

(1.12) Ωa(1)F•(s1) ⋂ Ωa(2)F•(s2) ⋂ · · · ⋂ Ωa(m)F•(sm)

is transverse and consists solely of real points.

This theorem (without the transversality) is the original statement of the conjecture of
Boris Shapiro and Michael Shapiro for Grassmannians, which was posed in exactly this
form to the author in May 1995. The Shapiro conjecture was ﬁrst discussed and studied
in detail in [62], where signiﬁcant computational evidence was presented (see also [67]
and [50]). These results and computations, as well as Theorem 1.10, highlighted the key
role that transversality plays in the conjecture. Apparently, this Shapiro conjecture was
in part an attempt to propose a reason for the results in the thesis [59] which showed
that for G(1, d), there are choices of real ﬂags F i
• in (1.12) so that the intersection
is transverse with all points real. This was extended to all problems in the special
Schubert calculus on all Grassmannians [61]. Later, Vakil [66] showed that this was
true for all Schubert problems on all Grassmannians.
The main ingredient in the proof of Theorem 1.11 is an isomorphism between alge-
braic objects associated to the intersection (1.12) and to certain representation-theoretic
data. This isomorphism provides a very deep link between Schubert calculus for the
Grassmannian and the representation theory of sln+1C.
We sketch the proof of Theorem 1 in the next three sections.

2. Spaces of polynomials with given Wronskian

Theorem 1.8 enables the reduction of Theorem 1 to a special case. Since the Wronski
map is ﬁnite, a standard limiting argument (given for example in Section 1.3 of [40]
or Remark 3.4 of [62]) shows that it suﬃces to prove Theorem 1 when the Wronskian
has distinct real roots that are suﬃciently general. Since δ(ιn,d) is the upper bound
for the number of spaces of polynomials with given Wronskian, it suﬃces to construct
this number of distinct spaces of real polynomials with a given Wronskian, when the
Wronskian has distinct real roots that are suﬃciently general. In fact, this is exactly
what Mukhin, Tarasov, and Varchenko do [40].

Theorem 1′. If s1, . . . , s(n+1)(d−n) are generic real numbers, there are δ(ιn,d) distinct
real vector spaces of polynomials P with Wronskian ∏

i(t − si).

The proof ﬁrst constructs δ(ιn,d) distinct spaces of polynomials with a given Wron-
skian having generic complex roots, which we describe in Section 2.1. This uses a
Fuchsian diﬀerential equation given by the critical points of a remarkable symmetric
function, called the master function. The next step uses the Bethe ansatz in a certain
representation V of sln+1C: critical points of the master function give Bethe eigenvec-
tors of the Gaudin Hamiltonians which turn out to be a highest weight vectors for an
irreducible submodule of V . This is described in Section 3, where the eigenvalues of the
Gaudin Hamiltonians on a Bethe vector are shown to be the coeﬃcients of the Fuchsian
diﬀerential equation giving the corresponding spaces of polynomials. This is the germ of
the new, deep connection between representation theory and Schubert calculus that led

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 9

to Theorem 1.11. Finally, the Gaudin Hamiltonians are real symmetric operators when
the Wronskian has only real roots, so their eigenvalues are real, and thus the Fuchsian
diﬀerential equation has real coeﬃcients and the corresponding space of polynomials is
also real. Figure 2 presents a schematic of this extraordinary proof.

Critical points of the master function

 
 
 
 
 
 
 ✠
 ❅
❅
❅
❅
❅
❅❅❘

Fuchsian
diﬀerential
equations
 Bethe
ansatz

!
Wr−1(yn(t)) ✛ ✲ Integrable systems and
Representation theory

✻
Eigenvalues of a
symmetric matrix
(forces reality)
✛
Real spaces
of polynomials(Wr−1(yn(t)))

Figure 2. Schematic of proof of Shapiro conjecture.

2.1. Critical points of master functions. The construction of δ(ιn,d) spaces of
polynomials with a given Wronskian begins with the critical points of a symmetric
rational function that arose in the study of hypergeometric solutions to the Knizhnik-
Zamolodchikov equations [52], and the Bethe ansatz method for the Gaudin model.
The master function depends upon parameters s := (s1, . . . , s(n+1)(d−n)), which are
the roots of our Wronskian W , and an additional (
n+1
2 )(d−n) variables

x := (x
(1)
1 , . . . , x
(1)
d−n, x
(2)
1 , . . . , x
(2)
2(d−n), . . . , x
(n)
1 , . . . , x
(n)
n(d−n)) .

Each set of variables x
(i) := (x
(i)
1 , . . . , x
(i)
i(d−n)) will turn out to be the roots of certain
intermediate Wronskians.
Deﬁne the master function Φ(x; s) by the (rather formidable) formula

(2.1)
 n∏

i=1
 ∏

1≤j<k≤i(d−n)
(x
(i)
j − x
(i)
k )2 · ∏

1≤j<k<(n+1)(d−n)(sj − sk)2

n−1∏

i=1
 i(d−n)∏

j=1
 (i+1)(d−n)∏

k=1 (x
(i)
j − x
(i+1)
k ) ·
 n(d−n)∏

j=1
 (n+1)(d−n)∏

k=1 (x
(n)
j − sk)
 .

This is separately symmetric in each set of variables x
(i). The Cartan matrix for sln+1
appears in the exponents of the factors (x
(i)
∗ − x
(j)
∗ ) in (2.1). This hints at the relation
of these master functions to Lie theory, which we do not discuss.
The critical points of the master function are solutions to the system of equations

(2.2) 1
Φ ∂

∂x
(i)
j Φ(x; s) = 0 for i = 1, . . . , n, j = 1, . . . , i(d−n) .

10 FRANK SOTTILE

When the parameters s are generic, these Bethe ansatz equations turn out to have
ﬁnitely many solutions. The master function is invariant under the group

S := Sd−n × S2(d−n) × · · · × Sn(d−n) ,

where Sm is the group of permutations of {1, . . . , m}, and the factor Si(d−n) permutes
the variables in x
(i). Thus S acts on the critical points. The invariants of this action
are polynomials whose roots are the coordinates of the critical points.
Given a critical point x, deﬁne monic polynomials px := (p1, . . . , pn) where the
components x
(i) of x are the roots of pi,

(2.3) pi :=
 i(d−n)∏

j=1 (t − x
(i)
j ) for i = 1, . . . , n .

Also write pn+1 for the Wronskian, the monic polynomial with roots s. The discriminant
Discr(f ) of a polynomial f is the square of the product of diﬀerences of its roots and
the resultant Res(f, g) is the product of all diﬀerences of the roots of f and g [8]. Then
the formula for the master function (2.1) becomes

(2.4) Φ(x; s) =
 n+1∏

i=1 Discr(pi)
∕ n∏

i=1 Res(pi, pi+1) .

The connection between the critical points of Φ(x; s) and spaces of polynomials with
Wronskian W is through a Fuchsian diﬀerential equation. Given (an orbit of) a critical
point x represented by the list of polynomials px, deﬁne the fundamental diﬀerential
operator Dx of the critical point x by

(2.5) ( d
dt − ln
′( W
pn
 )) · · · ( d
dt − ln
′(p2
p1
 ))( d
dt − ln′(p1)) ,

where ln
′(f ) := d
dt ln f . The kernel Vx of Dx is the fundamental space of the critical
point x.

Example 2.6. Since
( d
dt − ln′(p)) p = ( d
dt − p′

p
 ) p = p′ − p′

p p = 0 ,

we see that p1 is a solution of Dx. It is instructive to look at Dx and Vx when n = 1.
Suppose that f a solution to Dx that is linearly independent from p1. Then

0 = ( d
dt − ln′(W
p1
 ))( d
dt − ln
′(p1)) f = ( d
dt − ln′(W
p1
 ))(f ′ − p′
1
p1 f ) .

This implies that W
p1 = f ′ − p′
1
p1 f ,

so W = Wr(f, p1), and the kernel of Dx is a 2-dimensional space of functions with
Wronskian W .

What we just saw is always the case. The following result is due to Scherbak and
Varchenko [53] for n = 1 and to Mukhin and Varchenko [47, §5] for all n.

Theorem 2.7. Suppose that Vx is the fundamental space of a critical point x of the
master function Φ with generic parameters s which are the roots of W .

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 11

(1) Then Vx is an (n+1)-dimensional space of polynomials of degree d lying in
G(n, d)◦ with Wronskian W .
(2) The critical point x is recovered from Vx in some cases as follows. Suppose
that f0, . . . , fn are monic polynomials in Vx with deg fi = d−n + i, each fi is
square-free, and that the pairs fi and fi+1 are relatively prime. Then, up to
scalar multiples, the polynomials p1, . . . , pn in the sequence px are

f0 , Wr(f0, f1) , Wr(f0, f1, f2) , . . . , Wr(f0, . . . , fn−1) .

Statement (2) includes a general result about factoring a linear diﬀerential operator
into diﬀerential operators of degree 1. Linearly independent C ∞ functions f0, . . . , fn
span the kernel of the diﬀerential operator of degree n+1,

det
 





 f0 f1 · · · fn 1
f ′
0 f ′
1 · · · f ′
n d
dt
. . . . . . .
f (n+1)
0 f (n+1)
1 · · · f (n+1)
n dn+1

dtn+1
 




 .

If we set pi+1 := Wr(f0, . . . , fi), then (2.5) is a factorization over C(t) of this determinant
into diﬀerential operators of degree 1. This follows from some interesting identities
among Wronskians shown in the Appendix of [47].
Theorem 2.7 is deeper than this curious fact. When the polynomials p1, . . . , pn, W
are square-free, consecutive pairs are relatively prime, and s is generic, it implies that
the kernel V of an operator of the form (2.5) is a space of polynomials with Wronskian
W having roots s if and only if the polynomials p1, . . . , pn come from the critical points
of the master function (2.1) corresponding to W .
This gives an injection from S-orbits of critical points of the master function Φ with
parameters s to spaces of polynomials in G(n, d)◦ whose Wronskian has roots s. Mukhin
and Varchenko showed that this is a bijection when s is generic.

Theorem 2.8 (Theorem 6.1 in [48]). For generic complex numbers s, the master func-
tion Φ has nondegenerate critical points that form δ(ιn,d) distinct orbits.

The structure (but not of course the details) of their proof is remarkably similar to the
structure of the proof of Theorem 1.10; they allow the parameters to collide one-by-one,
and study how the orbits of critical points behave. Ultimately, they obtain the same
recursion as in [61], which mimics the Pieri formula for the branching rule for tensor
products of representations of sln+1 with its fundamental representation Vωn. This same
structure is also found in the main argument in [11]. In fact, this is the same recursion
in a that Schubert established for intersection numbers δ(a, ι, . . . , ι), and then solved
to obtain the formula (1.6) in [54].

3. The Bethe ansatz for the Gaudin model

The Bethe ansatz is a general (conjectural) method to ﬁnd pure states, called Bethe
vectors, of quantum integrable systems. The (periodic) Gaudin model is an integrable
system consisting of a family of commuting operators called the Gaudin Hamiltonians
that act on a representation V of sln+1C. In this Bethe ansatz, a vector-valued rational
function is constructed so that for certain values of the parameters it yields a complete
set of Bethe vectors. As the Gaudin Hamiltonians commute with the action of sln+1C,

12 FRANK SOTTILE

the Bethe vectors turn out to be highest weight vectors generating irreducible submod-
ules of V , and so this also gives a method for decomposing some representations V of
sln+1C into irreducible submodules. The development, justiﬁcation, and reﬁnements of
this Bethe ansatz are the subject of a large body of work, a small part of which we
mention.

3.1. Representations of sln+1C. The Lie algebra sln+1C (or simply sln+1) is the space
of (n+1) × (n+1)-matrices with trace zero. It has a decomposition

sln+1 = n− ⊕ h ⊕ n+ ,

where n+ (n−) are the strictly upper (lower) triangular matrices, and h consists of the
diagonal matrices with zero trace. The universal enveloping algebra Usln+1 of sln+1 is
the associative algebra generated by sln+1 subject to the relations uv − vu = [u, v] for
u, v ∈ sln+1 where [u, v] is the Lie bracket in sln+1.
We consider only ﬁnite-dimensional representations of sln+1 (equivalently, of Usln+1).
For a more complete treatment, see [19]. Any representation V of sln+1 decomposes
into joint eigenspaces of h, called weight spaces,

V = ⊕

µ∈h∗ V [µ] ,

where, for v ∈ V [µ] and h ∈ h, we have h.v = µ(h)v. The possible weights µ of
representations lie in the integral weight lattice. This has a distinguished basis of
fundamental weights ω1, . . . , ωn that generate the cone of dominant weights.
An irreducible representation V has a unique one-dimensional weight space that
is annihilated by the nilpotent subalgebra n+ of sln+1. The associated weight µ is
dominant, and it is called the highest weight of V . Any nonzero vector with this weight
is a highest weight vector of V , and it generates V . Furthermore, any two irreducible
modules with the same highest weight are isomorphic. Write Vµ for the highest weight
module with highest weight µ. Lastly, there is one highest weight module for each
dominant weight.
More generally, if V is any representation of sln+1 and µ is a weight, then the singular
vectors in V of weight µ, written sing(V [µ]), are the vectors in V [µ] annihilated by n+.
If v ∈ sing(V [µ]) is nonzero, then the submodule Usln+1.v it generates is isomorphic
to the highest weight module Vµ. Thus V decomposes as a direct sum of submodules
generated by the singular vectors,

(3.1) V = ⊕

µ Usln+1.sing(V [µ]) ,

so that the multiplicity of the highest weight module Vµ in V is simply the dimension
of its space of singular vectors of weight µ.
When V is a tensor product of highest weight modules, the Littlewood-Richardson
rule [18] gives formulas for the dimensions of the spaces of singular vectors. Since this is
the same rule for the number of points in an intersection (1.5) of Schubert varieties from
a Schubert problem, these geometric intersection numbers are equal to the dimensions
of spaces of singular vectors. In particular, if Vω1 ≃ Cn+1 is the deﬁning representation
of sln+1 and Vωn = ∧
nVω1 = V ∗
ω1 (these are the ﬁrst and last fundamental representations

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 13

of sln+1), then

(3.2) dim sing(V ⊗(n+1)(d−n)
ωn [0]) = δ(ιn,d) .

It is important to note that this equality of numbers is purely formal, in that the same
formula governs both numbers. A direct connection remains to be found.

3.2. The (periodic) Gaudin model. The Bethe ansatz is a conjectural method to
obtain a complete set of eigenvectors for the integrable system on V := V ⊗m
ωn given by
the Gaudin Hamiltonians (deﬁned below). Since these Gaudin Hamiltonians commute
with sln+1, the Bethe ansatz has the additional beneﬁt of giving an explicit basis for
sing(V [µ]), thus explicitly giving the decomposition (3.1).
The Gaudin Hamiltonians act on V ⊗m
ωn and depend upon m distinct complex numbers
s1, . . . , sm and a complex variable t. Let gln+1 be the Lie algebra of (n+1) × (n+1)
complex matrices. For each i, j = 1, . . . , n+1, let Ei,j ∈ gln+1 be the matrix whose only
nonzero entry is a 1 in row i and column j. For each pair (i, j) consider the diﬀerential
operator Xi,j(t) acting on V ⊗m
ωn -valued functions of t,

Xi,j(t) := δi,j d
dt −
 m∑

k=1
 E(k)
j,i
t − sk ,

where E(k)
j,i acts on tensors in V ⊗m
ωn by Ej,i in the kth factor and by the identity in other
factors. Deﬁne a diﬀerential operator acting on V ⊗m
ωn -valued functions of t,

M := ∑

σ∈S sgn(σ) X1,σ(1)(t) X2,σ(2)(t) · · · Xn+1,σ(n+1)(t) ,

where S is the group of permutations of {1, . . . , n+1} and sgn(σ) = ± is the sign of a
permutation σ ∈ S. Write M in standard form

M = dn+1

dtn+1 + M1(t) dn

dtn + · · · + Mn+1(t) .

These coeﬃcients M1(t), . . . , Mn+1(t) are called the (higher) Gaudin Hamiltonians.
They are linear operators that depend rationally on t and act on V ⊗m
ωn . We collect
together some of their properties.

Theorem 3.3. Suppose that s1, . . . , sm are distinct complex numbers. Then

(1) The Gaudin Hamiltonians commute, that is, [Mi(u), Mj(v)] = 0 for all i, j =
1, . . . , n+1 and u, v ∈ C.
(2) The Gaudin Hamiltonians commute with the action of sln+1 on V ⊗m
ωn .

Proofs are given in [38], as well as Propositions 7.2 and 8.3 in [41], and are based
on results of Talalaev [65]. A consequence of the second assertion is that the Gaudin
Hamiltonians preserve the weight space decomposition of the singular vectors of V ⊗m
ωn .
Since they commute, the singular vectors of V ⊗m
ωn have a basis of common eigenvec-
tors of the Gaudin Hamiltonians. The Bethe ansatz is a method to write down joint
eigenvectors and their eigenvalues.

14 FRANK SOTTILE

3.3. The Bethe ansatz for the Gaudin model. This begins with a rational function
that takes values in a weight space V ⊗m
ωn [µ],

v : Cl × Cm ↦−→ V ⊗m
ωn [µ] .

This universal weight function was introduced in [52] to solve the Knizhnik-Zamolodchi-
kov equations with values in V ⊗m
ωn [µ]. When (x, s) is a critical point of a master function,
the vector v(x, s) is both singular and an eigenvector of the Gaudin Hamiltonians. (This
master function is a generalization of the one deﬁned by (2.1).) The Bethe ansatz
conjecture for the periodic Gaudin model asserts that the vectors v(x, s) form a basis
for the space of singular vectors.
Fix a highest weight vector vn+1 ∈ Vωn[ωn]. Then v⊗m
n+1 generates V ⊗m
ωn as a Usln+1⊗m-
module. In particular, any vector in V ⊗m
ωn is a linear combination of vectors that are
obtained from v⊗m
n+1 by applying a sequence of operators E(k)
i+1,i, for 1 ≤ k ≤ m and
1 ≤ i ≤ n. The universal weight function is a linear combination of such vectors of
weight µ.
When m = (n+1)(d−n), l = (n+1
2 )(d−n), and µ = 0, the universal weight function
is a map v : C(n+1
2 )(d−n) × C(n+1)(d−n) −→ V ⊗(n+1)(d−n)
ωn [0] .
To describe it, note that a vector Ea+1,aEb+1,b · · · Ec+1,c.vn+1 is nonzero only if

(a, b, . . . , c) = (a, a+1, . . . , n−1, n) .

Write va for this vector. The vectors v1, . . . , vn+1 form a basis of Vωn. Thus only
some sequences of operators E(k)
i+1,i applied to v⊗(n+1)(d−n)
n+1 give a nonzero vector. These
sequences are completely determined once we know the weight of the result. The
operator E(k)
i+1,i lowers the weight of a weight vector by the root αi. Since

(3.4) (n+1)ωn = α1 + 2α2 + · · · + nαn ,

there are i(d−n) occurrences of E(k)
i+1,i, which is the number of variables in x
(i).
Let B be the set of all sequences (b1, b2, . . . , b(n+1)(d−n)), where 1 ≤ bk ≤ n+1 for each
k and we have #{k | bk ≤ i} = i(d−n) .
Given a sequence B in B, deﬁne

vB := vb1 ⊗ vb2 ⊗ · · · ⊗ vb(n+1)(d−n)

=
 (n+1)(d−n)⊗

k=1
 (E(k)
bk+1,bk · · · E(k)
n,n−1 · E(k)
n+1,n)
.vn+1 ,

where the operator E(k)
bk+1,bk · · · E(k)
n,n−1 · E(k)
n+1,n is the identity if bk = n + 1. Then vB is
a vector of weight 0, by (3.4). The universal weight function is a linear combination of
these vectors vB, v(x; s) = ∑

B∈B wB(x; s) · vB ,

where wB(x, s) is separately symmetric in each set of variables x
(i).
To describe wB(x; s), suppose that

z = (z(1), z(2), . . . , z((n+1)(d−n)))

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 15

is a partition of the variables x into (n+1)(d−n) sets of variables where the kth set z(k)

of variables has exactly one variable from each set x
(i) with bk ≤ i (and is empty when
bk = n+1). That is, if bk ≤ n, then

(3.5) z(k) = (x
(bk)
cbk , x
(bk+1)
cbk +1 , . . . , x
(n)
cn ) ,

for some indices cbk , . . . , cn. If bk = n+1, set w(k)(z) := 1, and otherwise

w(k)(z; s) := 1

x
(bk)
cbk − x
(bk+1)
cbk +1 · · · 1

x
(n−1)
cn−1 − x
(n)
cn · 1

x
(n)
cn − sk ,

in the notation (3.5). Then we set

w(z; s) :=
 (n+1)(d−n)∏

k=1 w(k)(z; s) .

Finally, wB(x; s) is the sum of the rational functions w(z; s) over all such partitions z
of the variables x. (Equivalently, the symmetrization of any single w(z; s).)
While v(x, s) is a rational function of x and hence not globally deﬁned, if the co-
ordinates of s are distinct and x is a critical point of the master function (2.1), then
the vector v(x, s) ∈ V ⊗(n+1)(d−n)
ωn [0] is well-deﬁned, nonzero and it is in fact a singular
vector (Lemma 2.1 of [48]). Such a vector v(x, s) when x is a critical point of the mas-
ter function is called a Bethe vector. Mukhin and Varchenko also prove the following,
which is the second part of Theorem 6.1 in [48].

Theorem 3.6. When s ∈ C(n+1)(d−n) is general, the Bethe vectors form a basis of the
space sing(V ⊗(n+1)(d−n)
ωn [0]).

These Bethe vectors are the joint eigenvectors of the Gaudin Hamiltonians.

Theorem 3.7 (Theorem 9.2 in [41]). For any critical point x of the master func-
tion (2.1), the Bethe vector v(x, s) is a joint eigenvector of the Gaudin Hamiltonians
M1(t), . . . , Mn+1(t). Its eigenvalues µ1(t), . . . , µn+1(t) are given by the formula

(3.8) dn+1

dtn+1 + µ1(t) dn

dtn + · · · + µn(t) d
dt + µn+1(t) =
( d
dt + ln
′(p1))( d
dt + ln
′(p2
p1
 )) · · · ( d
dt + ln
′( pn
pn−1
 ))( d
dt + ln
′( W
pn
 )) ,

where p1(t), . . . , pn(t) are the polynomials (2.3) associated to the critical point x and
W (t) is the polynomial with roots s.

Observe that (3.8) is similar to the formula (2.5) for the diﬀerential operator Dx
of the critical point x. This similarity is made more precise if we replace the Gaudin
Hamiltonians by a diﬀerent set of operators. Consider the diﬀerential operator formally
conjugate to (−1)n+1M,

K = dn+1

dtn+1 − dn

dtn M1(t) + · · · + (−1)n d
dtMn(t) + (−1)n+1Mn+1(t)

= dn+1

dtn+1 + K1(t) dn

dtn + · · · + Kn(t) d
dt + Kn+1(t) .

16 FRANK SOTTILE

These coeﬃcients Ki(t) are operators on V ⊗(n+1)(d−n)
ωn that depend rationally on t, and
are also called the Gaudin Hamiltonians. Here are the ﬁrst three,

K1(t) = −M1(t) , K2(t) = M2(t) − nM ′
1(t) ,

K3(t) = −M3(t) + (n−1)M ′′
2 (t) − (
n
2
)M ′′′
1 (t) ,

and in general Ki(t) is a diﬀerential polynomial in M1(t), . . . , Mi(t).
Like the Mi(t), these operators commute with each other and with sln+1, and the
Bethe vector v(x, s) is a joint eigenvector of these new Gaudin Hamiltonians Ki(t). The
corresponding eigenvalues λ1(t), . . . , λn+1(t) are given by the formula

(3.9) dn+1

dtn+1 + λ1(t) dn

dtn + · · · + λn(t) d
dt + λn+1(t) =
( d
dt − ln′(W
pn
 ))( d
dt − ln
′( pn
pn−1
 )) · · · ( d
dt − ln
′(p2
p1
 ))( d
dt − ln
′(p0)) ,

which is (!) the fundamental diﬀerential operator Dx of the critical point x.

Corollary 3.10. Suppose that s ∈ C(n+1)(d−n) is generic.

(1) The Bethe vectors form an eigenbasis of sing(V ⊗(n+1)(d−n)
ωn [0]) for the Gaudin
Hamiltonians K1(t), . . . , Kn+1(t).
(2) The Gaudin Hamiltonians K1(t), . . . , Kn+1(t) have simple spectrum in that their
eigenvalues separate the basis of eigenvectors.

Statement (1) follows from Theorems 3.6 and 3.7. For Statement (2), suppose that
two Bethe vectors v(x, s) and v(x
′, s) have the same eigenvalues. By (3.9), the corre-
sponding fundamental diﬀerential operators would be equal, Dx = Dx′. But this implies
that the fundamental spaces coincide, Vx = Vx′. By Theorem 2.7 the fundamental space
determines the orbit of critical points, so the critical points x and x
′ lie in the same
orbit, which implies that v(x, s) = v(x
′, s).

4. Shapovalov form and the proof of the Shapiro conjecture

The last step in the proof of Theorem 1 is to show that if s ∈ R(n+1)(d−n) is generic
and x is a critical point of the master function (2.1), then the fundamental space Vx of
the critical point x has a basis of real polynomials. The reason for this reality is that
the eigenvectors and eigenvalues of a symmetric matrix are real.
We begin with the Shapovalov form. The map τ : Ei,j ↦→ Ej,i induces an antiauto-
morphism on sln+1. Given a highest weight module Vµ, and a highest weight vector
v ∈ Vµ[µ], the Shapovalov form ⟨·, ·⟩ on Vµ is deﬁned recursively by

⟨v, v⟩ = 1 and ⟨g.u, v⟩ = ⟨u, τ (g).v⟩ ,

for g ∈ sln+1 and u, v ∈ V . In general, this Shapovalov form is nondegenerate on Vµ
and positive deﬁnite on the real part of Vµ.
For example, the Shapovalov form on Vωn is the standard Euclidean inner product,
⟨vi, vj⟩ = δi,j, in the basis v1, . . . , vn+1 of Section 3.3. This induces the symmetric
(tensor) Shapovalov form on the tensor product V ⊗(n+1)(d−n)
ωn , which is positive deﬁnite
on the real part of V ⊗(n+1)(d−n)
ωn .

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 17

Theorem 4.1 (Proposition 9.1 in [41]). The Gaudin Hamiltonians are symmetric with
respect to the tensor Shapovalov form,

⟨Ki(t).u, v⟩ = ⟨u, Ki(t).v⟩ ,

for all i = 1, . . . , n+1, t ∈ C, and u, v ∈ V ⊗(n+1)(d−n)
ωn .

We give the most important consequence of this result for our story.

Corollary 4.2. When the parameters s and variable t are real, the Gaudin Hamiltoni-
ans K1(t), . . . , Kn+1(t) are real linear operators with real spectrum.

Proof. The Gaudin Hamiltonians M1(t), . . . , Mn+1(t) are real linear operators which
act on the real part of V ⊗(n+1)(d−n)
ωn , by their deﬁnition. The same is then also true of
the Gaudin Hamiltonians K1(t), . . . , Kn+1(t). But these are symmetric with respect to
the Shapovalov form and thus have real spectrum.

Proof of Theorem 1. Suppose that s ∈ R(n+1)(d−n) is general. By Corollary 4.2, the
Gaudin Hamiltonians for t ∈ R acting on sing(V (n+1)(d−n)
ωn [0]) are symmetric operators
on a Euclidean space, and so have real eigenvalues. The Bethe vectors v(x, s) for critical
points x of the master function with parameters s form an eigenbasis for the Gaudin
Hamiltonians. As s is general, the eigenvalues are distinct by Corollary 3.10 (2), and
so the Bethe vectors must be real.
Given a critical point x, the eigenvalues λ1(t), . . . , λn+1(t) of the Bethe vectors are
then real rational functions, and so the fundamental diﬀerential operator Dx has real
coeﬃcients. But then the fundamental space Vx of polynomials is real.
Thus each of the δ(ιn,d) spaces of polynomials Vx whose Wronskian has roots s that
were constructed in Section 2 is in fact real. This proves Theorem 1.

5. Other proofs of the Shapiro conjecture

The proofs of diﬀerent Bethe ans¨atze for other models (other integrable systems)
and other Lie algebras, which is ongoing work of Mukhin, Tarasov, and Varchenko, and
others, can lead to generalizations of Theorem 1. One generalization is given in an
appendix of [40], where it is conjectured that for real parameters s, orbits of critical
points of generalized master functions are real. For the Lie algebra sln+1, this holds as
the polynomials pi of Section 2.1 are real. This new conjecture also holds for the Lie
algebras sp2n and so2n+1, by the results in Section 7 of [47].
We also discuss other proofs of the Shapiro conjecture.

5.1. Discrete Wronskians to Calogero-Moser spaces. The XXX model is another
integrable system studied by Mukhin, Tarasov, and Varchenko [44]. This work is similar
to their work on the periodic Gaudin model, including Wronskians, a Bethe ansatz, and
symmetric operators. One diﬀerence is that Ugln+1 is replaced by the Yangians, Y gln+1,
which are a deformation of the universal enveloping algebra of the current algebra
gln+1[t]. (The current algebra gln+1[t] consists of polynomials in t with coeﬃcients in
gln+1.) Another is that the usual Wronskian is replaced by the discrete Wronskian,

18 FRANK SOTTILE

which depends upon a real number h,

Wrh(f0, . . . , fn) := det
 




f0(t) f0(t + h) · · · f0(t + nh)
f1(t) f1(t + h) · · · fn(t + nh)
. . . . . .
fn(t) fn(t + h) · · · fn(t + nh)




 ,

and the functions are
 quasi-polynomials, fi(t) = e
bitgi(t), where gi(t) is a polyno-
mial. The linear span V of quasi-polynomials e
b0tg0(t), . . . , e
bntgn(t) is a space of
quasi-polynomials. This discrete Wronskian has the form w(t)e
P bi·t, where w(t) is
a polynomial that is well-deﬁned up to a scalar.

Theorem 5.1 (Theorem 2.1 of [44]). Let V be a space of quasi-polynomials with discrete
Wronskian Wrh(V ) = ∏N
i=1(t − si)e
P bi·t whose roots are real and satisfy

|si − sj| ≥ |h| for all i ̸= j ,

then V has a basis of real quasi-polynomials.

This condition on the separation of roots cannot be relaxed if the theorem is to hold
for all exponents bi. When n = 1 and b0 = b1 = 0, this is a special case of the main
theorem in Eremenko, et al. [15]. We will not discuss the proof of Theorem 5.1, except
to remark that it depends upon the results of [41, 43].
In the limit as h → 0, the discrete Wronskian becomes the usual Wronskian, which
yields the following theorem.

Theorem 5.2 (Theorem 4.1 of [44]). Let V be a space of quasi-polynomials whose
Wronskian has only real roots. Then V has a basis of real quasi-polynomials.

When the exponents bi are all zero, this reduces to Theorem 1, and therefore is a
generalization of the Shapiro conjecture. It implies Theorem 2 from the Introduction.
Suppose that b0, . . . , bn are distinct real numbers, α0, . . . , αn are complex numbers, and
consider the matrix

(5.3) Z :=
 




 α0 (b0 − b1)−1 · · · (b0 − bn)−1

(b1 − b0)−1 α1 · · · (b1 − bn)−1
. . . . . .
(bn − b0)−1 (bn − b1)−1 · · · αn
 



 .

Theorem 2 (Theorem 5.4 of [44]). If Z has only real eigenvalues, then the numbers
α0, . . . , αn are real.

Proof. We follow [44], deducing this from Theorem 5.2 and some matrix identities.
Since

(5.4) dm

dtm (t − a)e
bt = b
m(t − a)e
bt + mb
m−1e
bt ,

if A is the diagonal matrix diag(a0, . . . , an), E := diag(e
b0t, . . . , e
bnt), V is the Vander-
monde matrix (b
i
j)n
i,j=0, and W := (ib
i−1
j )n
i,j=0, then (5.4) implies that
( di

dti (t − aj)e
bj t)n

i,j=0 = [V (It − A) + W ] E ,

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 19

and therefore

(5.5) Wr((t − a0)e
b0t , . . . , (t − an)e
bnt)

= e
P bi·t · ∏

i<j (bj − bi) · det [It − (A − V −1W )] .

We deduce a formula for V −1W . The inverse of the Vandermonde comes from La-
grange’s interpolation formula. For each i = 0, . . . , n, set

ℓi(u) :=
 ∏

k̸=i(u − bk)
∏

k̸=i(bi−bk) =
 n∑

j=0 ℓi,juj .

Since ℓi(bj) = δi,j, we see that V −1 = (ℓi,j)n
i,j=0. But then

V −1W = (ℓ′
i(bj))n
i,j=0 .

This gives formulas for the entries of V −1W = (mi,j)n
i,j=0,

mi,j =
 ∏

k̸=i,j(bj − bk)
∏

k̸=i(bi − bk) if i ̸= j and

mi,i = ∑

k̸=i
 1
bi − bk .

Let B be the diagonal matrix diag(∏

k̸=i(bi − bk), i = 0, . . . , n) and M be the diagonal
of V −1W . We leave the following calculation to the reader,

B−1ZB = diag(α0, . . . , αn) + M − V −1W .

Combining this with (5.5), we see that if

(5.6) ai = αi + mi,i i = 0, . . . , n ,

then the eigenvalues of Z are exactly the roots of the Wronskian (5.5).
Since the matrix Z has only real eigenvalues, Theorem 5.2 implies that the span of
(t − a0)e
b0t, . . . , (t − an)e
bnt has a basis of real quasi-polynomials. Since the exponents
bi are real and distinct, the numbers a0, . . . , an are real as are the entries of V −1W , and
so (5.6) implies that the entries αi of Z are real.
Theorem 2 has an interesting consequence.

Corollary 5.7. Suppose that X and Z are square complex matrices such that

(5.8) [X, Z] = I − K ,

where K has rank 1. If both X and Z have real eigenvalues, then they may be simulta-
neously conjugated to real matrices.

Proof. It suﬃces to show this for a dense open subset of such pairs (X, Z) of matri-
ces. Suppose that X is diagonalizable with eigenvalues b0, . . . , bn and that we have
conjugated (X, Z) so that X is diagonal. If we write Z = (zi,j)n
i,j=0, then

(5.9) [X, Z] = (zi,j(bj − bi))n
i,j=0 .

The rank 1 matrix K has the form (βiγj)n
i,j=0, where β, γ are complex vectors. By (5.8)
and (5.9), the diagonal entries of K are all 1, so that βiγi = 1, so in fact β, γ ∈ (C×)n+1

20 FRANK SOTTILE

with γ = β−1. Conjugating (5.8) by β (considered as a diagonal matrix), we may
assume that K is the matrix whose every entry is 1, and so

zi,j(bj − bi) = δi,j − 1 ,

or, if i ̸= j, bi ̸= bj, and zi,j = (bi − bj)−1. But then Z has the form (5.3) (where
αi = zi,i), and Theorem 2 implies that all of its entries are real.

Mukhin, Tarasov, and Varchenko noted that Theorem 5.2 follows from Theorem 2
by the duality studied in [42], and that the Shapiro conjecture for Grassmannians is
the case of Corollary 5.7 when Z is nilpotent. We close this section with an interesting
circle of ideas related to Corollary 5.7.
Let C n be the set of all pairs (X, Z) of (n+1) × (n+1) complex matrices such that
[X, Z] − I has rank 1. The group Gln+1(C) acts on C n by simultaneous conjugation and
Wilson [70] deﬁnes the Calogero-Moser space Cn to be the quotient of C n by Gln+1(C).
He shows this is a smooth aﬃne variety of dimension 2n. It has many incarnations.
It is the phase space of the (complex) Calogero-Moser integrable system [31], Etingof
and Ginzburg [16] showed that Cn parametrizes irreducible representations of a certain
rational Cherednik algebra, and Wilson’s adelic Grassmannian [70] is naturally the
union of all the spaces Cn.
Let Cn(R) be the real points of Cn. This turns out to be image of the real points
of C n under the quotient map πn : Cn → Cn. The map that takes a matrix to its
eigenvalues induces a map
 Υ : Cn −→ C(n+1) × C(n+1) ,

where C(n+1) := Cn+1/Sn+1. Etingof and Ginzburg showed that Υ is a ﬁnite map of
degree (n+1)! We restate Corollary 5.7.

Corollary 5.7. Υ−1(R(n+1) × R(n+1)) ⊂ Cn(R).

This in turn implies the Shapiro conjecture for Grassmannians, which is the case of
Corollary 5.7 when Z is nilpotent,

Υ−1(R(n+1) × {0}) ⊂ Cn(R) .

The rational Cherednik algebra Hn [16] is generated by the polynomial subalgebras
C[x0, . . . , xn] and C[z0, . . . , zn] and the group algebra CSn+1 subject to

(5.10) σijxi = xjσij [xi, zj] = σij if i ̸= j ,

σijzi = zjσij [xi, zi] = − ∑

j̸=i σij ,

where σij ∈ Sn+1 is the transposition (i, j). The symmetrizing idempotent is

e := 1
(n+1)!
 ∑

σ∈Sn+1 σ .

For p ∈ Cn, write Cp for the 1-dimensional representation of the coordinate ring of Cn
in which a function f acts by the scalar f (p).

Theorem 5.11 ([16], Theorems 1.23 and 1.24).
(1) eHne is isomorphic to the coordinate ring of Cn.

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 21

(2) Irreducible representations of Hn are parametrized by the points p of Cn, where
the corresponding representation is

Mp := Hne ⊗eHne Cp .

(3) Mp is isomorphic to CSn+1 as an Sn+1-module.

Etingof and Ginzburg connect the structure of the representations Mp to the Calogero-
Moser space. Let Sn act on the indices {0, . . . , n−1}. Then xn and zn both stabilize
the subspace M Sn
p of invariants, which has dimension n+1.

Theorem 5.12 ([16], Theorem 11.16). In any basis of M Sn
p , xn, zn act by a pair of
matrices (X, Z) ∈ C n such that πn(X, Z) = p.

5.2. Transversality in the Shapiro conjecture. While Mukhin, Tarasov, and Var-
chenko prove Theorem 1.11 in [45], their actual result is much deeper. Each ramiﬁcation
sequence a for G(n, d) corresponds to a dominant weight µ(a) for sln+1 such that, given
a Schubert problem A := (a
(1), . . . , a
(m)), the intersection number δ(A) is equal to the
dimension of the space of singular vectors
(
Vµ(a(1)) ⊗ Vµ(a(2)) ⊗ · · · ⊗ Vµ(a(m))) [0] ,

as both numbers are determined by the same formula based on the Littlewood-Richardson
rule. The result of [45] links more subtle scheme-theoretic information about the inter-
section of Schubert varieties to algebraic information about the action of commuting
operators on the singular vectors.
The coordinate ring RA(s) of an intersection of Schubert varieties (1.12) is an Artin
algebra of dimension δ(A), because the Pl¨ucker formula (1.3) forces the intersection
to be zero dimensional. It is semisimple exactly when the intersection is transverse.
Because of the Pl¨ucker formula, the intersection lies in the big Schubert cell G(n, d)◦,
and so RA(s) is a quotient of the coordinate ring R of G(n, d)◦. Then the coregular
representation of RA(s) on its dual RA(s)∗ induces an action of R on RA(s)∗. This is
the scheme-theoretic information.
Given a ﬁnite-dimensional representation V of gln+1 and a complex number s, requir-
ing t to act on V via scalar multiplication by s, gives the evaluation module V (s) of the
current algebra gln+1[t]. If µ = (µ1, . . . , µm) are dominant weights and s = (s1, . . . , sm)
are distinct complex numbers, then the evaluation module

Vµ(s) := Vµ1(s1) ⊗ Vµ2(s2) ⊗ · · · ⊗ Vµm(sm)

is an irreducible gln+1[t]-module [7].
The universal enveloping algebra Ugln+1[t] has a commutative subalgebra B, called
the Bethe algebra [21, 65]. As B commutes with gln+1, it acts on spaces of singular
vectors in the evaluation module Vµ(s). The action of the Bethe algebra on the singular
vectors Vµ(s)[0] is the algebraic information from representation theory. Let Bµ(s) be
the image of B in the endomorphism algebra of Vµ(s)[0].
A main result in [45] is that these two actions, R on RA(s) and B on Vµ(s)[0], are
isomorphic when µ = (µ(a
1), . . . , µ(a
m)), which we write as µ(A). This requires that
we identify R with B in some way. For that, the big cell G(n, d)◦ can be identiﬁed with
(n+1) × (d−n) matrices (yi,j), whose entries identify R with C[yi,j]. The Bethe algebra
has generators Bi,j, where 1 ≤ i ≤ n+1 and 1 ≤ j. Deﬁne the map τ : R ֒→ B by

τ (yi,j) = Bi,j .

22 FRANK SOTTILE

Mukhin, Tarasov, and Varchenko also give a linear bijection φ : RA(s)∗ → Vµ(s)[0].

Theorem 5.13. Let A = (a
1, . . . , a
m) be a Schubert problem for G(n, d) and s =
(s1, . . . , sm) be distinct complex numbers. Then the map τ induces an isomorphism of
algebras τ : RA(s) ∼
−→ Bµ(A)(s) so that, for f ∈ RA(s) and g ∈ RA(s)∗, µ(f ∗g) =
τ (f )µ(g). That is, (τ, µ) gives an isomorphism between the coregular representation of
RA(s) on its linear dual RA(s)∗ and the action of the Bethe algebra Bµ(A)(s) on the
singular vectors Vµ(s)[0].

Theorem 1.11 now follows, as the image of the Bethe algebra on the singular vectors
Vµ(s)[0] is generated by the Gaudin Hamiltonians, which are diagonalizable when the
parameters si are real. Thus Bµ(A)(s) and hence RA(s) are semisimple, which implies
that the intersection of Schubert varieties (1.12) was transverse.
We remark that this uses the general form of the results in [40] which we did not
describe in these notes. Also, the coincidence of numbers, δ(A) = dim(Vµ(A)(s)[0]), is
an important ingredient in the proof that µ is a bijection.
Very recently, Mukhin, Tarasov, and Varchenko related this Bethe algebra to the
center of the rational Cherednik algebra of Section 5.1, and to the algebra of regular
functions on the Calogero-Moser space [46].

6. Applications of the Shapiro conjecture

Theorem 1 and its stronger version, Theorem 1.11, have other applications in math-
ematics. Some are straightforward, such as linear series on P1 with real ramiﬁcation.
Here, we discuss this application in the form of maximally inﬂected curves and rational
functions with real critical points, as well as Purbhoo’s considerably deeper application
in which he recovers the basic combinatorial algorithms of Young tableaux from the
monodromy of the Wronski map. We close with Eremenko and Gabrielov’s computa-
tion of the degree of the real Wronski map, which implies that when d is even and W
is a generic real polynomial, there are many spaces of real polynomials with Wronskian
W .

6.1. Maximally inﬂected curves. One of the earliest occurrences of the central
mathematical object of these notes, spaces of polynomials with prescribed ramiﬁ-
cation, was in algebraic geometry, as these spaces of polynomials are linear series
P ⊂ H 0(P1, O(d)) on P1 with prescribed ramiﬁcation. Their connection to Schubert
calculus originated in work of Castelnuovo in 1889 [6] on g-nodal rational curves, and
this was important in Brill-Noether theory (see Ch. 5 of [25]) and the Eisenbud-Harris
theory of limit linear series [9, 10].
A linear series P on P1 of degree d and dimension n+1 (a point in G(n, d)) gives rise
to a degree d map

(6.1) ϕ : P1 −→ Pn = P(P ∗)

of P1 to projective space. We will call this map a curve. The linear series is ramiﬁed
at points s ∈ P1 where ϕ is not convex (the derivatives ϕ(s), ϕ′(s), . . . , ϕ(n)(s) do not
span Pn). Call such a point s a ﬂex of the curve (6.1).
A curve is real when P is real. It is maximally inﬂected if it is real and all of its
ﬂexes are real. The study of these curves was initiated in [32], where restrictions on the
topology of plane maximally inﬂected curves were established.

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 23

Let us look at some examples. There are two types of real rational cubic curves,
which are distinguished by their singular points. The singular point of the curve on the
left below is a node and it is connected to the rest of the curve, while the singular point
on the other curve is isolated from the rest of the curve, and is called a solitary point.

y2 = x
3 + x
2 y2 = x
3 − x
2

While both curves have one of their three ﬂexes at inﬁnity, only the curve on the right
has its other two ﬂexes real (the dots) and is therefore maximally inﬂected. A nodal
cubic cannot be maximally inﬂected.
Similarly, a maximally inﬂected quartic with six ﬂexes has either 1 or 0 of its (neces-
sarily 3) singular points a node, and necessarily 2 or 3 solitary points. We draw the two
types of maximally inﬂected quartics having six ﬂexes, omitting their solitary points.
Due to the symmetry in the placement of the ﬂexes, the ﬁrst quartic has two ﬂexes on
its node—one for each branch through the node.

When d ≥ 3, the image of a rational curve γ : P1 → P2 of degree d is a singular
curve of arithmetic genus (d−1
2 ). In general, the singularities consist of (
d−1
2 ) ordinary
double points, which are where two smooth branches of the curve meet transversally. A
real rational curve has three types of such double points. We have already seen nodes
and solitary points. The third kind of real double point consists of a pair of complex
conjugate double points, and is invisible in RP2.
The examples we gave had few nodes. This is always the case.

Theorem 6.2 (Corollary 3.3 and Theorem 4.1 of [32]). Given a maximally inﬂected
plane curve of degree d, let δ, η, c be its numbers of solitary points, nodes, and pairs of
complex conjugate double points. Then we have

d − 2 ≤ δ ≤ (
n − 1
2
 ) and 0 ≤ η + 2c ≤ (
n − 2
2
 ) .

Furthermore, there exist maximally inﬂected curves of degree d with (n−1
2 ) solitary points
(and hence no other singularities), and there exist curves with (n−2
2 ) nodes and d−2
solitary points.

While many constructions of maximally inﬂected curves were known, Theorem 1,
and in particular Theorem 1.11, show that there are many maximally inﬂected curves:
Any curve ϕ : P1 → Pn whose ramiﬁcation lies in RP1 must be real and is therefore
maximally inﬂected.

24 FRANK SOTTILE

Theorem 6.2 is proven using the Pl¨ucker formula (1.3) and the Klein formula from
topology. This result and some intriguing calculations in Section 6 of [32] suggest
that the number of solitary points is a deformation invariant. That is, if the points of
inﬂection move, then the number of solitary points is constant. Examples show that the
number of nodes may change under a continuous deformation of the inﬂection points,
with a pair of nodes colliding to become a pair of complex conjugate double points, but
we have not observed collisions of solitary points.

6.2. Rational functions with real critical points. A special case of Theorem 1,
proved earlier by Eremenko and Gabrielov, serves to illustrate the breadth of mathe-
matical areas touched by this Shapiro conjecture. When n = 1, we may associate a
rational function ϕP := f1(t)/f2(t) to a basis {f1(t), f2(t)} of a vector space P ∈ G(1, d)
of polynomials. Diﬀerent bases give diﬀerent rational functions, but they all diﬀer from
each other by a fractional linear transformation of the image P1. We say that such
rational functions are equivalent.
The critical points of a rational function are the points of the domain P1 where the
derivative of ϕP ,
 dϕP := f ′
1f2 − f1f ′
2
f 2
2 = 1
f 2
2 · det (f1 f2
f ′
1 f ′
2
) ,

vanishes. That is, at the roots of the Wronskian. These critical points only depend
upon the equivalence class of the rational function. Eremenko and Gabrielov [13] prove
the following result about the critical points of rational functions.

Theorem 6.3. A rational function ϕ whose critical points lie on a circle in P1 maps
that circle to a circle.

To see that this is equivalent to Theorem 1 when n = 1, note that we may apply
a change of variables to ϕ so that its critical points lie on the circle RP1 ⊂ P1. Simi-
larly, the image circle may be assumed to be RP1. Reversing these coordinate changes
establishes the equivalence.
The proof used methods speciﬁc to rational functions. Goldberg showed [22] that
there are at most cd := 1
d(2d−2
d−1 ) rational functions of degree d with a given collection
of 2d − 2 simple critical points. If the critical points of a rational function ϕ of degree
d lie on a circle C ⊂ CP1 and if ϕ maps C to C, then ϕ−1(C) forms a graph on the
Riemann sphere with nodes the 2d−2 critical points, each of degree 4, and each having
two edges along C and one edge on each side of C. We mark one of the critical points
to ﬁx the ordered list of the critical points. It turns out that there are also cd such
abstract graphs with a distinguished vertex. Call these graphs nets. (In fact, cd is
Catalan number, which counts many objects in combinatorics [64, Exer. 6.19, p. 219].)
Here are the c4 = 5 nets for d = 4:

Eremenko and Gabrielov used the uniformization theorem in complex analysis to con-
struct such a rational function ϕ for each net and choice of critical points on C. Since

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 25

cd is the upper bound for the number of such rational functions, this gave all rational
functions with given set of critical points and thus proved Theorem 6.3.
More recently, Eremenko and Gabrielov [14] found an elementary proof of Theo-
rem 6.3 which is based upon analytic continuation and a very reﬁned version of the
construction underlying Theorem 1.10. This has unfortunately never been published.
By Theorem 1.10, there exists a Wronski polynomial W0(t) of degree 2d−2 with
distinct real roots for which there are cd spaces of real polynomials with Wronskian
W0(t). Suppose that W0 is a member of a continuous family Wτ for τ ∈ [0, 1] of
polynomials of degree 2d−2 with distinct real roots. Since there are cd distinct spaces
of polynomials with Wronskian W0, there are cd distinct lifts of the path Wτ to paths
of spaces of polynomials with Wronskian Wτ , at least for τ near zero. The obstruction
to analytically continuing these cd lifts occurs at critical points of the Wronski map
Wr : G(1, d)R → RP2d−2. Since this map is at most cd to 1, the ﬁrst critical point in a
ﬁber is a point where two of the lifted paths collide.
Eremenko and Gabrielov show that such a collision cannot occur. The reason is sim-
ple: nets are constant along paths of spaces of polynomials in G(1, d) whose Wronskian
has 2d − 2 distinct roots, and each of the spaces of polynomials above W0(t) has a dif-
ferent net. Thus each lifted path has a diﬀerent net, and no collision is possible. They
show that nets are constant along paths by a simple set-theoretic/topological argument.
A similar elementary argument applied to the construction of the spaces of polynomials
in Theorem 1.10 shows that each space has a distinct net. The proof is completed by
observing that any Wronski polynomial may be joined to W0 along some path Wτ .
The elementary and constructive nature of this proof suggests that the Shapiro Con-
jecture for Grassmannians may have an elementary proof, if a suitable substitute for
nets can be found when n > 1.

6.3. Tableaux combinatorics. Starting from Theorems 1 and 1.11 for the Schubert
problem ιn,d, Purbhoo [49] shows that the basic combinatorial properties and algo-
rithms for Young tableaux are realized geometrically via the monodromy groupoid of
the Wronski map, Wr : G(n, d) → P(C(n+1)(d−n)[t]). In particular, Sch¨utzenberger slides,
evacuation, Knuth equivalence and dual equivalence all arise geometrically. Purbhoo
uses his analysis of the monodromy groupoid to get a new proof of the Littlewood-
Richardson rule.
A partition is a weakly decreasing sequence of nonnegative integers λ : λ0 ≥ λ1 ≥
· · · ≥ λn ≥ 0. We impose the restriction that n−d ≥ λ0. Partitions are ramiﬁcation
sequences in disguise, with a : 0 ≤ a0 < a1 < · · · < an ≤ d corresponding to

(6.4) λ(a) : an − n ≥ · · · ≥ a1 − 1 ≥ a0 .

We identify a partition with its diagram, which is a left-justiﬁed array of boxes with
λi boxes in the ith row. For example,

λ = 5322 ←→ .

Write |λ| for the number of boxes in λ. By (6.4), |a| = |λ(a)|.
The partial order on ramiﬁcation sequences induces the partial order of component-
wise comparison on partitions, which is the inclusion of their diagrams. The minimal
partition is ∅ and the maximal partition (for us) is (d−n, . . . , d−n), which has d−n

26 FRANK SOTTILE

repeated n+1 times. Write this as . Given µ ≤ λ, the skew partition λ/µ is the
diﬀerence of their diagrams. We set |λ/µ| := |λ| − |µ|. For example,

5322/21 = and |5322/21| = 9 .

A standard Young tableau of shape λ/µ is a ﬁlling of the boxes of λ/µ with the
integers 1, 2, . . . , |λ/µ| so that the entries increase across each row and down each
column. Here are three ﬁllings of the shape 331/1; only the ﬁrst two are tableaux.

1 3
2 5 6
4
 2 4
1 3 5
6
 2 6
5 4 3
1

Let SYT(λ/µ) be the set of all standard Young tableaux of shape λ/µ.
The degree δ(ιn,d) of the Wronski map equals the cardinality of SYT( ). By
Theorem 1.11, the Wronski map is unramiﬁed over the locus of polynomials with distinct
real roots, and so the points in each ﬁber are in bijection with the set SYT( ).
This identiﬁcation is almost canonical because in the region where the roots of the
Wronskian are clustered (1.9) the identiﬁcation is canonical, by the work of Eremenko
and Gabrielov [11], and the Wronski map is unramiﬁed over the locus of polynomials
with distinct roots. Since nets are in natural bijection with tableaux, this identiﬁcation
for n = 1 was done by Eremenko and Gabrielov in [14].
This identiﬁcation can be extended to skew tableaux. Given a partition λ, its dual
is λ
∨ : d−n−λn ≥ · · · ≥ d−n−λ0. For partitions µ ≤ λ, set

G(λ/µ) := Ωa(µ)F•(0) ⋂ Ωa(λ∨)F•(∞) .

The Wronskian of a space of polynomials P ∈ G(λ/µ) has degree at most |λ| and van-
ishes to order least |µ| at zero. Let P(λ/µ) be the projective space of such polynomials.
This has dimension |λ/µ|, which is equal to the dimension of G(λ/µ). The restriction
of the Wronski map to G(λ/µ),

Wr : G(λ/µ) −→ P(λ/µ) ,

is ﬁnite, ﬂat, and has degree equal to the cardinality of SYT(λ/µ). Lastly, the Wronski
map is unramiﬁed over the locus of polynomials in P(λ/µ) with |λ/µ| distinct nonzero
real roots, and there is an identiﬁcation of the ﬁbers with SYT(λ/µ).
Purbhoo gives an explicit identiﬁcation of the ﬁbers of the Wronski map by extending
the notion of standard tableaux. Let s = {s1, . . . , s|λ/µ|} ⊂ RP1 be a set of |λ/µ| real
numbers, possibly including ∞, that satisfy

(I) If i ̸= j, then |si| ̸= |sj|.
(II) 0 ∈ s only if µ = ∅ and ∞ ∈ s only if λ = .

We identify such a subset s with the polynomial Ws := t
|µ| ∏
s∈s(t − s) in P(λ/µ)
vanishing at s. A standard Young tableau of shape λ/µ with entries in s is a ﬁlling
of the boxes of λ/µ with elements of s such that if we replace each entry si with its
absolute value |si|, then the entries increase across each row and down each column.
Let SYT(λ/µ; s) be the set of all standard Young tableaux of shape λ/µ with entries
in s. Replacing each entry si in a tableau by k if si has the kth smallest absolute value

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 27

in s deﬁnes the map ord : SYT(λ/µ; s) → SYT(λ/µ). For example,
√2 4

e −8 π2

−6
 ord
↦−→
 1 3

2 5 6

4

Let s(τ ) for τ ∈ [a, b] be a continuous path of subsets of RP1 where s(τ ) satisﬁes
Conditions (I) and (II), except for ﬁnitely many points τ ∈ (a, b) at which Condition
(I) is violated exactly once in that si(τ ) = −sj(τ ) for some i ̸= j. A path that is
transverse to the locus where si = −sj for all i ̸= j is generic. Given a standard Young
tableau Ta of shape λ/µ and ﬁlling s(a), we can try to lift Ta to a family Tτ of standard
tableaux for all τ ∈ [a, b]. We do this by requiring that the entries in the boxes of Tτ
vary continuously, unless the condition that Tτ forms a tableau is violated.
In any interval where s(τ ) satisﬁes Condition (I), the entries of Tτ vary continuously
and ord(Tτ ) is constant. Suppose that τ0 is a point of the path where Condition (I) is
violated, and that si(τ0) = −sj(τ0) is the pair witnessing this violation. If si and sj are
in diﬀerent rows and columns, they remain in their respective boxes as τ passes τ0 and
ord(Tτ ) changes as τ passes τ0. If si and sj are in the same row or column, then they
are adjacent and leaving them in their respective boxes violates the condition that Tτ is
a tableau, so we require them to switch places and ord(Tτ ) does not change as τ passes
τ0.
Given a generic path s(τ ) for τ ∈ [a, b] and a tableau Ta ∈ SYT(λ/µ; s(a)), deﬁne
slides(τ )(Ta) to be the result of this process applied to Ta. This gives a bijection between
SYT(λ/µ; s(a)) and SYT(λ/µ; s(b)).

Example 6.5. We show this on a tableau of shape (4, 4, 2), for the path s(τ ) =
{τ, −1, . . . , −9} for τ ∈ [0, 10]. We only display when the tableau Tτ changes.

τ −1 −3 −8

−2 −4 −6 −9

−5 −7
 τ =1
−−−−→
 −1 τ −3 −8

−2 −4 −6 −9

−5 −7
 τ =3
−−−−→
 −1 −3 τ −8

−2 −4 −6 −9

−5 −7
 τ =6
−−−−→

−1 −3 −6 −8

−2 −4 τ −9

−5 −7
 τ =9
−−−−→
 −1 −3 −6 −8

−2 −4 −9 τ

−5 −7
 τ =10
−−−−→
 −1 −3 −6 −8

−2 −4 −9 10

−5 −7

The combinatorial enthusiast will note that the box containing τ has just performed
a Sch¨utzenberger slide through the subtableau formed by the negative entries. For
comparison, we show the tableaux ord(T0) and ord(T10).

1 2 4 9
3 5 7 10
6 8
 1 3 6 8
2 4 9 10
5 7

We give Purbhoo’s main theorem about the monodromy groupoid of the Wronski
map Wr : G(λ/µ) → P(λ/µ).

Theorem 6.6 ([49], Theorem 3.5). For each s = {s1, . . . , s|λ/µ|} ⊂ RP1 satisfying Con-
ditions (I) and (II), there is a correspondence P ↔ T (P ) between points P ∈ G(λ/µ)

28 FRANK SOTTILE

with Wronskian Ws and tableaux T (P ) ∈ SYT(λ/µ; s). Under this correspondence, if
s(τ ) ⊂ RP1 is a generic path for τ ∈ [a, b] and Pτ is any lifting of that path to G(λ/µ),
then T (Pb) = slides(τ )T (Pa) .

Thus the combinatorial operation of sliding a tableau along a generic path s(τ ) exactly
describes analytic continuation in the ﬁbers of the Wronski map above that path. This
sliding operation contains Sch¨utzenberger’s jeu de taquin [55], and much of tableaux
combinatorics [18, 51, 64] may be recovered from the geometry of the Wronski map.
Suppose s = {s1, . . . , s|λ/µ|} with |s1| < · · · < |s|λ/µ||. If T ∈ SYT(λ/µ; s) and
t = {si, . . . , sj} with i < j, then the entries of T in the set t form a subtableau T |t.
Now suppose that s = t∪u where the elements of t are positive, those of u are negative,
and we additionally have that |t| < |u| for t ∈ t and u ∈ u. Write |t| < |u| when this
occurs. Let t′ be a set of |λ/µ| positive numbers with |u| < |t′| and suppose that
s(τ ) for τ ∈ [0, 1] is a generic path from s = t ∪ u to s
′ = u ∪ t′. Given a tableau
S ∈ SYT(λ/µ; s), let S′ := slides(τ )S ∈ SYT(λ/µ; s
′), and deﬁne the subtableaux,

T := S|t , U := S|u , T ′ := S|t′ , and U ′ := S|u .

Because |t| < |u| < |t′|, T is inside of U and during the slide T and U move through
each other to obtain the tableaux U ′ and T ′ with U ′ inside of T ′. Schematically,

T U
 slides(τ )
−−−−−−−→ U ′ T ′

We write U ′ = slideT U and T ′ = slideU T .
Reversing the path s(τ ) enables the deﬁnition of U = slideT ′U ′ and T = slideU ′T ′.
These notions are independent of the choice of path s(τ ), by Theorem 6.6. In fact
slideT U does not depend upon the set t′. This geometrically deﬁned operation was
studied from a combinatorial perspective [3], where it was called tableaux switching,
and its independence from choices was Theorem 2.2(4) ibid.

Deﬁnition 6.7. Let u be a set of negative numbers. Two tableaux U1, U2 ∈ SYT(λ/µ; u)
are equivalent if, for any set t of |µ| positive numbers with |t| < |u| and any T1, T2 ∈
SYT(µ; t), we have slideT1U1 = slideT2U2 .
Two tableaux U1, U2 ∈ SYT(λ/µ; u) are dual equivalent if, for any sets t, t′ of positive
numbers with |t| < |u| < |t′|, shapes µ/ν, κ/λ, and tableaux T ∈ SYT(µ/ν; t) and
T ′ ∈ SYT(κ/λ; t′), each pair

(slideT U1 , slideT U2) and (slideT ′U1 , slideT ′U2)

has the same shape. Replacing numbers by their negatives extends these deﬁnitions to
tableaux with positive entries.

These are the fundamental equivalence relations on tableaux of Knuth-equivalence
and of Haiman’s dual equivalence [24]. Purbhoo shows that these combinatorial equiva-
lence relations coincide with geometrically-deﬁned relations that come from nonreduced
ﬁbers of the Wronski map.

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 29

Suppose that s = {s1, . . . , s(n+1)(d−n)} is a subset of RP1 satisfying Condition (I)
with |s1| < · · · < |s(n+1)(d−n)|, and suppose that t = {si, si+1, . . . , sj} are the positive
elements of s and let u = s − t be its nonpositive elements. Pick a positive number
a ∈ [si, sj] and consider any path s(τ ) for τ ∈ [0, 1] that satisﬁes Condition (I) for τ ∈
[0, 1) with s(0) = s, has constant nonpositive elements u, but whose positive elements
all approach a as t → 1 so that s(1) = {s1, . . . , si−1, a, . . . , a, sj+1, . . . , s(n+1)(d−n)}.
Given a tableau T ∈ SYT( ; s) corresponding to a point PT ∈ G(n, d) with Wron-
skian Ws, we may analytically continue PT in the ﬁbers of the Wronski map over the
path Ws(τ ). When τ ̸= 1, this continuation will be PTτ , but when τ = 1 it will be
limτ →1 PTτ . Write PT (τ ) for these points. For each τ < 1 the points PT (τ ) are distinct
for diﬀerent T ∈ SYT( ; s(τ )), but in the limit as τ → 1 some paths may coalesce,
as the ﬁber of the Wronskian is nonreduced at s(1).

Theorem 6.8 ([49]). Let T, T ′ ∈ SYT( ; s). Then Tt is equivalent to T ′|t if and
only if PT (1) = PT ′(1).

Let s
′(τ ) for τ ∈ [0, 1] be another generic path with s
′(0) = s in which the positive
elements are constant, but the others converge to some ﬁxed negative number a. We
deﬁne P ′
T (τ ) to be the analytic continuation of PT over the path s
′(τ ).

Theorem 6.9 ([49]). Let T, T ′ ∈ SYT( ; s). Then Tt is dual equivalent to T ′|t if
and only if P ′
T (1) = P ′
T ′(1).

6.4. Degree of the real Wronski map. Recall that the complex Wronski map
Wr : G(n, d) → P(n+1)(d−n) has degree (1.6)

δ(ιn,d) = [(n+1)(d−n)]! 1!2! · · · n!
(d−n)!(d−n+1)! · · · d! .

If we restrict the domain to the real Grassmannian, we get the real Wronski map
WrR : G(n, d)R → RP(n+1)(d−n). By Theorem 1.11, over the locus of polynomials with
(n+1)(d−n) distinct real roots, this is a δ(ιn,d)-to-one cover. Eremenko and Gabrielov [11]
studied this real Wronski map, computing its topological degree.
This requires some explanation, for real projective spaces and Grassmannians are
not always orientable, and hence maps between them do not necessarily have a degree.
However, the Wronski map can be lifted to their orienting double covers, after which
its degree is well-deﬁned up to a sign. By the Pl¨ucker formula, the Wronski map
restricted to the big Schubert cell G(n, d)◦
R of the Grassmannian is a ﬁnite, proper map
to R(n+1)(d−n), realized as the space of monic real polynomials of degree (n + 1)(d − n).
The compute the degree of the Wronski map over this big cell.
Fix a standard tableau T0 ∈ SYT( ). Given any tableau T ∈ SYT( ), let σT be
the permutation in S(n+1)(d−n) with σT (i) = j if the entries i in T0 and j in T occupy
the same cell of . Deﬁne
 δ(ιn,d)R := ∑

T ∈SYT( ) |σT | ,

where |σ| = ± is the sign of the permutation σ.

Theorem 6.10 (Theorem 2 of [11]). deg WrR = δ(ιn,d)R.

30 FRANK SOTTILE

This statistic, δ(ιn,d)R, was computed by White [69], who showed that it vanishes
unless d is even, and in that case it equals

1!2! · · · (p−1)!(m−1)!(m−2)! · · · (m−p+1)!( mp
2 )!
(m−p+2)!(m−p+4)! · · · (m+p−2)! ( m−p+1
2 )! ( m−p+3
2 )! · · · ( m+p−1
2 )! ,

where m := max{n+1, d−n} and p := min{n+1, d−n}.
The signiﬁcance of these results is that δ(ιn,d)R is a lower bound for the number of
real spaces of polynomials with given real Wronskian. This gave the ﬁrst example of a
geometric problem possessing a nontrivial lower bound on its number of real solutions.
In the 1990’s, Kontsevich [36] determined the number Nd of complex rational curves
of degree d interpolating 3d−1 general points in the plane. Work of Welschinger [68],
Mikhalkin [39], and Itenberg, et al. [28, 29] established a nontrivial lower bound Wd on
the number of real curves interpolating real points. Not only is Wd > 0, but

lim
d→∞ log Wd
log Nd = 1 (!)

More recently, Solomon [57] realized this number Wd as the degree of a map.
Such lower bounds, if they were widespread, could have signiﬁcant value for applica-
tions of mathematics, as they are existence proofs for real solutions. (On application
of the nontriviality of W3 = 8 is given in [17].) Initial steps in this direction were made
in [58, 30], which established lower bounds for certain systems of sparse polynomials.

7. Extensions of the Shapiro conjecture

The Shapiro conjecture for Grassmannians makes sense for other ﬂag manifolds. In
this more general setting, it is known to fail, but in very interesting ways. In some
cases, we have been able to modify it to give a conjecture that holds under scrutiny.
The Shapiro conjecture also admits some appealing generalizations, but its strongest
and most subtle form remains open for Grassmannians.

7.1. Lagrangian and Orthogonal Grassmannians. The Lagrangian and orthogo-
nal Grassmannians are closely related to the classical Grassmannian. For each of these,
the Shapiro conjecture is particularly easy to state.
The (odd) orthogonal Grassmannian requires a nondegenerate symmetric bilinear
form ⟨·, ·⟩ on C2n+1. This vector space has a basis e1, . . . , e2n+1 such that

⟨ei, e2n+2−j⟩ = δi,j .

A subspace V of C2n+1 is isotropic if ⟨V, V ⟩ = 0. Isotropic subspaces have dimension
at most n. The (odd) orthogonal Grassmannian OG(n) is the set of all maximal (n-
dimensional) isotropic subspaces V of C2n+1. This variety has dimension (n+1
2 )
.
The Shapiro conjecture for OG(n) begins with a particular rational normal curve γ
having parametrization

t ↦−→ e1 + te2 + t
2

2 e3 + · · · + t
n

n! en+1

− t
n+1

(n + 1)! en+2 + t
n+2

(n + 2)! en+3 − · · · + (−1)n t
2n

(2n)! e2n+1 .

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 31

This has special properties with respect to the form ⟨·, ·⟩. For t ∈ C, deﬁne the ﬂag
F•(t) in C2n+1 by
 Fi(t) := Span{γ(t), γ′(t) , . . . , γ(i−1)(t)} .

Then F•(t) is isotropic in that
 ⟨Fi(t), F2n+1−i(t)⟩ = 0 .

In general, an isotropic ﬂag F• of C2n+1 is a ﬂag such that ⟨Fi, F2n+1−i⟩ = 0.
Schubert varieties of OG(n) are deﬁned with respect to an isotropic ﬂag, F•, and are
the restriction of Schubert varieties of G(n−1, 2n)—the Grassmannian of n dimensional
subspaces of C2n+1—under the inclusion OG(n) ֒→ G(n−1, 2n). Schubert varieties for
OG(n) are indexed by strict partitions, which are integer sequences

κ : n ≥ κ
1 > κ
2 > · · · > κ
k > 0 .

Set ∥κ∥ = κ
1 + · · · + κ
k. We do not give the precise relation between these indices and
the ramiﬁcation sequences a of Section 1, but this may be done using the descriptions
given in [20, § 6.1] or [60]. Write XκF• for the Schubert variety of OG(n) deﬁned by
the Schubert index κ and an isotropic ﬂag F•. It has codimension ∥κ∥. A Schubert
problem is a list (κ1, . . . , κm) of Schubert indices such that

∥κ1∥ + ∥κ2∥ + · · · + ∥κm∥ = dim OG(n) = (
n + 1
2
 ) .

We state the Shapiro conjecture for OG(n).

Conjecture 7.1. If (κ1, . . . , κm) is a Schubert problem for OG(n) and s1, . . . , sm are
distinct real numbers, then the intersection

Xκ1F•(s1) ⋂ Xκ2F•(s2) ⋂ · · · ⋂ XκmF•(sm)

is transverse with all points real.

Besides optimism based upon the validity of the Shapiro conjecture for Grassmanni-
ans, the evidence for Conjecture 7.1 comes in two forms. Several tens of thousands of
instances have been checked with a computer and when each ∥κi∥ = 1 and the points
si are clustered (1.9), the intersection is transverse with all points real [63].

There is a similar story but with a diﬀerent outcome for the Lagrangian Grassman-
nian. Let ⟨·, ·⟩ be a nondegenerate skew symmetric bilinear form on C2n. This vector
space has a basis e1, . . . , e2n such that

⟨ei, e2n+1−j⟩ = { δi,j if i ≤ n
−δi,j if i > n .

Isotropic subspaces in C2n may have any dimension up to n, and those of maximal
dimension are called Lagrangian subspaces. The Lagrangian Grassmannian LG(n) is
the set of all Lagrangian subspaces V of C2n. This variety has dimension (n+1
2 ).

32 FRANK SOTTILE

For the Shapiro conjecture for LG(n), we have the rational normal curve γ with
parametrization

t ↦−→ e1 + te2 + t
2

2 e3 + · · · + t
n

n! en+1

− t
n+1

(n + 1)! en+2 + t
n+2

(n + 2)! en+3 − · · · + (−1)n−1 t
2n−1

(2n − 1)! e2n .

For t ∈ C, deﬁne the ﬂag F•(t) in C2n+1 by

Fi(t) := Span{γ(t), γ′(t) , . . . , γ(i−1)(t)} .

The ﬂag F•(t) is isotropic in that

⟨Fi(t), F2n−i(t)⟩ = 0 .

More generally, an isotropic ﬂag F• of C2n is a ﬂag such that ⟨Fi, F2n−i⟩ = 0.
As with OG(n), given an isotropic ﬂag, Schubert varieties for LG(n) are induced
from Schubert varieties of G(n−1, 2n−1) by the inclusion LG(n) ֒→ G(n−1, 2n−1).
Schubert varieties XκF• of LG(n) are also indexed by strict partitions κ and ∥κ∥ is
the codimension of XκF•. We give the relation between strict partitions for LG(n)
and ramiﬁcation sequences for G(n−1, 2n−1). Given a strict partition κ : n ≥ κ
1 >
· · · > κ
k, let µ : 0 < µ1 < · · · < µn−k be the complement of the set {κ
1, . . . , κ
k} in
{1, 2, . . . , n}. Call k the length of the strict partition κ. For example, if n = 6 and
κ = 4, 2, then k = 2 and µ = 1, 3, 5, 6. If we deﬁne a(κ) = (a0, . . . , an−1) to be the
sequence

0 ≤ n − κ
1 < · · · < n − κ
k < n−1 + µ1 < · · · < n−1 + µn−k ≤ 2n−1 ,

then XκF• = Ωa(κ)F• ∩ LG(n), so that

XκF• = {V ∈ LG(n) | F2n−aj ≥ n − j, for j = 0, 1, . . . , n−1} .

A Schubert problem is a list (κ1, . . . , κm) such that

∥κ1∥ + ∥κ2∥ + · · · + ∥κm∥ = dim LG(n) = (
n + 1
2
 ) .

The obvious generalization of Theorem 1 and Conjecture 7.1 to LG(n) turns out to be
false. We oﬀer a modiﬁcation that we believe is true. Belkale and Kumar [2] deﬁne a
notion they call Levi movability. A Schubert problem (κ1, . . . , κm) for LG(n) is Levi
movable if the corresponding Schubert indices, (a(κ1), . . . , a(κm)) also form a Schubert
problem for G(n−1, 2n−1). Unraveling the deﬁnitions shows that this is equivalent to
having the lengths of the strict partitions (κ1, . . . , κm) sum to n.

Conjecture 7.2. If (κ1, . . . , κm) is a Schubert problem for LG(n) and s1, . . . , sm are
distinct real numbers, then the intersection

Xκ1F•(s1) ⋂ Xκ2F•(s2) ⋂ · · · ⋂ XκmF•(sm)

is transverse. If (κ1, . . . , κm) is Levi movable, then all points of intersection are real,
but if it is not Levi movable, then no point in the intersection is real.

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 33

The strongest evidence in favor of Conjecture 7.2 is that it is true when the Schubert
problem (κ1, . . . , κm) is Levi movable. This follows from the deﬁnition of Levi movable
and the Shapiro conjecture for Grassmannians. Further evidence is that if each κi is
simple in that ∥κi∥ = 1, then a local version, similar to Theorem 1.10 but without
transversality, is true [63]. That is, if the si are clustered (1.9), then no point in the
intersection is real. Lastly, several tens of thousands of instances have been checked
with a computer.

7.2. Monotone conjecture for ﬂag manifolds. The Shapiro conjecture was origi-
nally made for the classical (type-A) ﬂag manifold, where is fails spectacularly. It is
false for the ﬁrst nontrivial Schubert problem on a ﬂag variety that is not a Grassman-
nian. Namely, the geometric problem of partial ﬂags consisting of a line ℓ lying on a
plane Λ in 3-dimensional space where ℓ meets three ﬁxed lines and Λ contains two ﬁxed
points.
This is just the problem of four lines in disguise. Suppose that p and q are the two
ﬁxed points that Λ is required to contain. Then Λ contains the line p, q they span.
Since ℓ ⊂ Λ, it must meet p, q. As ℓ must also meet three lines, this problem reduces to
the problem of four lines. In this way, there are two solutions to this Schubert problem.
Now let us investigate the Shapiro conjecture for this Schubert problem, which posits
that both ﬂags ℓ ⊂ Λ will be real, if we require that ℓ meets three ﬁxed tangent lines
to a rational curve and Λ contains two ﬁxed points of the rational curve. Let γ be
the rational normal curve (1) from the Introduction and suppose that the three ﬁxed
lines of our problem are its tangent lines ℓ(−1), ℓ(0), and ℓ(1). These lines lie on the
hyperboloid H of one sheet (2). Here is another view of these lines, the curve γ, and
the hyperboloid.
 ℓ(−1) ℓ(0)

ℓ(1)

γ
 H

If we require ℓ to meet the three tangent lines ℓ(−1), ℓ(0), and ℓ(1) and Λ to contain
the two points γ(v) and γ(w) of γ, then ℓ also meets the line λ(v, w) spanned by these
two points. As in the Introduction, the lines ℓ that we seek will come from points where
the secant line λ(v, w) meets H.
Figure 3 shows an expanded view down the throat of the hyperboloid, with a secant
line λ(v, w) that meets the hyperboloid in two points. For these points γ(v) and γ(w)
there will be two real ﬂags ℓ ⊂ Λ satisfying our conditions. This is consistent with the
Shapiro conjecture.

34 FRANK SOTTILE

ℓ(1) ℓ(−1)

ℓ(0)

γ

λ(v, w)
 γ(v)

✻
 γ(w)

✻

Figure 3. A secant line meeting H.

In contrast, Figure 4 shows a secant line λ(v, w) that does not meet the hyperboloid
in any real points. For these points γ(v) and γ(w), neither ﬂag ℓ ⊂ Λ satisfying our

ℓ(1) ℓ(−1)

ℓ(0)

γ
 λ(v, w) γ(v)
✄
✄
✄
✄
✄
✄
✄
✄✄✎

γ(w)
✡✡
✡✡
✡
✡✡
✡
✡✣

Figure 4. A secant line not meeting H.

conditions is real. This is a counterexample to the Shapiro conjecture.

This failure of the Shapiro conjecture is however quite interesting. If we label the
points −1, 0, 1 with 1 (conditions on the line) and v, w by 2 (conditions on the plane),
then along γ they occur in order

(7.3) 11122 in Figure 3 and 11212 in Figure 4.

The sequence for Figure 3 is monotone increasing and in this case both solutions are
always real, but the sequence for Figure 4 is not monotone. This example suggests a
way to correct the Shapiro conjecture, that we call the monotone conjecture.

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 35

Speciﬁcally, let n : 0 ≤ n1 < · · · < nk < d be a sequence of integers. The manifold
Fℓn,d of ﬂags of type n is the set of all sequences of subspaces

E• : En1 ⊂ En2 ⊂ · · · ⊂ Enk ⊂ Cd[t]

with dim Eni = ni + 1. The forgetful map E• ↦→ Eni induces a projection

πi : Fℓn,d −→ G(ni, d)

to a Grassmannian. A Grassmannian Schubert variety is a subvariety of Fℓn,d of the
form π−1
i ΩaF•. That is, it is the inverse image of a Schubert variety in a Grassmannian
projection. Write X(a,ni)F• for this Grassmannian Schubert variety and call (a, ni) a
Grassmannian Schubert condition.
A Grassmannian Schubert problem is a list

(7.4) (a
(1), n
(1)), (a
(2), n
(2)), . . . , (a
(m), n
(m)),

of Grassmannian Schubert conditions satisfying |a
(1)| + · · · + |a
(m)| = dim Fℓn,d. We
state the monotone conjecture.

Conjecture 7.5. Let ((a
(1), n
(1)), . . . , (a
(m), n
(m))) be a Grassmannian Schubert prob-
lem for the ﬂag variety Fℓn,d with n
(1) ≤ n
(2) ≤ · · · ≤ n
(m). Whenever s1 < s2 < · · · <
sm are real numbers, the intersection

X(a(1),n(1))F•(s1) ⋂ X(a(2),n(2))F•(s2) ⋂ · · · ⋂ X(a(m),n(m))F•(sm) ,

is transverse with all points of intersection real (when it is nonempty).

There is signiﬁcant evidence for this monotone conjecture. First, the Shapiro con-
jecture for Grassmannians is the special case case when m = 1 so then n = n1 and
Fℓn,d = G(n1, d): the monotonicity condition s1 < · · · < sm is empty as any reordering
of the Schubert conditions remains sorted.
This conjecture was formulated in [50]. That project was based upon computer
experimentation using 15.76 gigaHertz-years of computing to study over 520 million
instances of 1126 diﬀerent Schubert problems on 29 ﬂag manifolds. Some of this com-
putation studied intersections of Schubert varieties that were not necessarily monotone.
For example, consider the Schubert problem on Fℓ1<2,5,

(7.6) (0<2 , 1)4 , (0<1<3 , 2)4 ,

where the exponent indicates a repeated condition. Table 1 displays the computation
on this Schubert problem. The rows are labeled by diﬀerent orderings of the conditions
along the rational normal curve γ in the notation of (7.3). Each cell contains the number
of computed instances with a given ordering and number of real solutions. The empty
cells indicate no observed instances. Only the ﬁrst row tests the monotone conjecture:
Each of the 400,000 computed instances had all 12 solutions real. The other rows reveal
a very interesting pattern; for nonmonotone orderings of the conditions along γ, not all
solutions are always real and there seems to be a lower bound on the number of real
solutions. Only in the last row, which represents the maximal possible intertwining of
the conditions, were no real solutions observed.
A third piece of evidence for the monotone conjecture was provided by Eremenko,
et. al [15], who showed that it is true for two-step ﬂag manifolds, when n = d−2 < d−1.
This is a special case of their main theorem, which asserts the reality of a rational

36 FRANK SOTTILE

Number of Real Solutions
0 2 4 6 8 10 12
11112222 400000
11211222 118 65425 132241 117504 84712
11122122 104 65461 134417 117535 82483
11221122 1618 57236 188393 92580 60173
11212212 25398 90784 143394 107108 33316
11221212 2085 79317 111448 121589 60333 25228
11121222 7818 34389 58098 101334 81724 116637
12121212 15923 41929 131054 86894 81823 30578 11799

Table 1. The Schubert problem (7.6) on Fℓ1<2,5.

function ϕ with prescribed critical points on RP1 and certain prescribed coincidences
ϕ(v) = ϕ(w), when v, w are real.
This result of Eremenko, et. al can be described in terms of G(d−2, d), where it
becomes a statement about real points in an intersection of Schubert varieties given by
ﬂags that are secant to a rational normal curve in a particular way. This condition on
secant ﬂags makes sense for any Grassmannian, and the resulting secant conjecture is
also a generalization of the Shapiro conjecture.
A ﬂag F• is secant along an arc I of a rational normal curve γ if every subspace in
the ﬂag is spanned by its intersections with I. A collection of ﬂags that are secant to
γ is disjoint if they are secant along disjoint arcs of γ. The secant conjecture asserts
that a Schubert problem given by disjoint secant ﬂags has all solutions real. We give a
more precise statement.

Conjecture 7.7. If (a1, . . . , am) is a Schubert problem for G(n, d) and F 1
• , . . . , F m
• are
disjoint secant ﬂags, then the intersection

Ωa1F 1
• ⋂ Ωa2F 2
• ⋂ · · · ⋂ ΩamF m
•
is transverse with all points real.

The main result of [13] is that an intersection of Schubert varieties in G(d − 2, d)
given by disjoint secant ﬂags is transverse with all points real. The Shapiro conjecture
is a limiting case of the secant conjecture, as the ﬂag osculating γ at a point s is the
limit of ﬂags that are secant along arcs that shrink to the point s.
Consider this secant conjecture for the problem of four lines. The hyperboloid in
Figure 5 contains three lines that are secant to γ along disjoint arcs. Any line secant
along the arc I (which is disjoint from the other three arcs) meets the hyperboloid in
two points, giving two real solutions to this instance of the secant conjecture.
This secant conjecture is currently being studied on a supercomputer whose day
job is calculus instruction. For each of hundreds of Schubert problems, thousands to
millions of instances of the secant conjecture are being tested, and much more. The
overlap number measures how far a collection of secant ﬂags is from being disjoint,
and it is zero if and only if the ﬂags are disjoint. This experiment tests instances of
the secant conjecture and near misses when the ﬂags have low overlap number. The
results (number of real solutions vs. overlap number) are stored in a publicly accessible

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 37

γ ❍❍❍❥
 ✻

I

Figure 5. The problem of four secant lines.

database accessible from the webpage [56]. In the ﬁrst nine months of operation, this
has studied over 1.3 billion instances of Schubert problems and consumed over 600
gigaHertz-years of computing.
Table 2 shows the results for a Schubert problem with 16 solutions on G(2, 5). Com-
puting the 20, 000, 000 instances of this problem used 4.473 gigaHertz-years. The rows
are labeled with the even integers from 0 to 16 as the number of real solutions has the
same parity as the number of complex solutions. The column with overlap number 0

#
real
solns.
 Overlap Number
0 1 2 3 4 5 6 · · · Total
0 20 · · · 7977
2 116 · · · 88578
4 6154 23561 526 3011 · · · 542521
6 25526 63265 2040 9460 · · · 1571582
8 33736 78559 2995 13650 · · · 2834459
10 25953 39252 2540 11179 · · · 3351159
12 35578 44840 3271 14160 · · · 2944091
14 17367 17180 1705 7821 · · · 1602251
16 4568553 182668 583007 468506 36983 83169 · · · 7057382
Total 4568553 182668 727321 735163 50060 142586 · · · 20000000
Table 2. Number of Real solutions v.s. overlap number.

represents tests of the secant conjecture. Since its only entries are in the row for 16
real solutions, the secant conjecture was veriﬁed in 4, 568, 553 instances. The column
labeled 1 is empty because ﬂags for this problem cannot have overlap number 1. The
most interesting feature is that for overlap number 2, all solutions were still real, while
for overlap numbers 3, 4, and 5, at least 4 of the 16 solutions were real, and only with
overlap number 6 and greater does the Schubert problem have no real solutions. This
inner border, which indicates that the secant conjecture does not completely fail when
there is small overlap, is found on many of the other problems that we investigated and
is a new phenomenon that we do not understand. A description of the technical aspects
of this running experiment is given in [27].

38 FRANK SOTTILE

7.3. Discriminant conjecture. Despite the proofs of Theorems 1 and 1.11 (weak and
strong form of the Shapiro for Grassmannians), the strongest and most subtle form of
that conjecture remains open.
The discriminant of a polynomial W = ∏

i(t − si) is ∏

i<j(si − sj)2, the symmetric
function of its roots having lowest degree that vanishes when W has a double root.
More generally, suppose that we have a family of polynomial systems in a space X that
are parametrized by a space S. (For example, the intersection in Theorem 1.11,

(1.12) Ωa(1)F•(s1) ⋂ Ωa(2)F•(s2) ⋂ · · · ⋂ Ωa(m)F•(sm)

in which X = G(n, d) and S is Cm or (P1)m.) Then the discriminant variety of this
system is the subvariety Σ ⊂ S where the system is not transverse. This is expected to
be a hypersurface, and the discriminant of the system is the function that deﬁnes Σ.
By Theorem 1.11 this discriminant does not vanish when the parameters si are real
and distinct. However, in the few cases when it has been computed much more is true,
it is a sum of squares [62] and therefore nonnegative. For example, for the Schubert
problem ι1,4 with 5 solutions, if we ﬁx s5 = 0 and s6 = ∞, then the discriminant is a
homogeneous polynomial of degree 20 in the four variables s1, . . . , s4 with 711 terms,
which turns out to be a sum of squares. This is remarkable because Hilbert [26] showed
that, except for m = 3 and deg = 4, not all nonnegative homogeneous polynomials in
m > 2 variables of degree more than 2 are sums of squares. Work of Blekherman [4]
suggests that it is extremely rare for a nonnegative polynomial to be a sum of squares.

Conjecture 7.8 (Question 4 of [62]). The discriminant of an intersection (1.12) of a
Schubert problem on a Grassmannian given by osculating ﬂags is sum of squares in the
parameters s1, . . . , sm.

We conjecture that this remains true for any cominuscule ﬂag variety, which includes
the Lagrangian Grassmannian, the orthogonal Grassmannian, quadrics, as well as the
two exceptional cases E6/D5 and E7/E6. There is also a form of this conjecture, Conjec-
ture 2.10 of [50], involving preorders for the semialgebraic set of monotone parameters
s1 < s2 < · · · < sm.
We close with the remark that we have not yet investigated the Shapiro conjecture
for other ﬂag manifolds, and do not yet know when it fails, or how to repair the failures.
Also, the methods of Mukhin, Tarasov, and Varchenko only work for the Grassmannian,
and it is completely unclear how to even approach a proof of these generalizations.

References

[1] D. J. Bates, F. Bihan, and F. Sottile, Bounds on the number of real solutions to polynomial
equations, Int. Math. Res. Not. IMRN (2007), no. 23, Art. ID rnm114, 7.
[2] P. Belkale and S. Kumar, Eigenvalue problem and a new product in cohomology of ﬂag varieties,
Invent. Math. 166 (2006), no. 1, 185–228.
[3] G. Benkart, F. Sottile, and J. Stroomer, Tableau switching: algorithms and applications, J. Com-
bin. Theory Ser. A 76 (1996), no. 1, 11–43.
[4] G. Blekherman, There are signiﬁcantly more nonnegative polynomials than sums of squares, Israel
J. Math. 153 (2006), 355–380.
[5] C. I. Byrnes, Pole assignment by output feedback, Three decades of mathematical system theory,
Lecture Notes in Control and Inform. Sci., vol. 135, Springer, Berlin, 1989, pp. 31–78.
[6] G. Castelnuovo, Numero delle involuzioni razionali gaicenti sopra una curva di dato genere, Rendi.
R. Accad. Lincei 4 (1889), no. 5, 130–133.

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 39

[7] V. Chari and A. Pressley, Weyl modules for classical and quantum aﬃne algebras, Represent.
Theory 5 (2001), 191–223 (electronic).
[8] D. Cox, J. Little, and D. O’Shea, Ideals, varieties, and algorithms, third ed., Undergraduate Texts
in Mathematics, Springer, New York, 2007.
[9] D. Eisenbud and J. Harris, Divisors on general curves and cuspidal rational curves, Invent. Math.
74 (1983), no. 3, 371–418.
[10] D. Eisenbud and J. Harris, When ramiﬁcation points meet, Invent. Math. 87 (1987), 485–493.
[11] A. Eremenko and A. Gabrielov, Degrees of real Wronski maps, Discrete Comput. Geom. 28 (2002),
no. 3, 331–347.
[12] , Pole placement static output feedback for generic linear systems, SIAM J. Control Optim.
41 (2002), no. 1, 303–312 (electronic).
[13] , Rational functions with real critical points and the B. and M. Shapiro conjecture in real
enumerative geometry, Ann. of Math. (2) 155 (2002), no. 1, 105–129.
[14] , Elementary proof of the B. and M. Shapiro conjecture for rational functions, 2005,
arXiv:math/0512370.
[15] A. Eremenko, A. Gabrielov, M. Shapiro, and A. Vainshtein, Rational functions and real Schubert
calculus, Proc. Amer. Math. Soc. 134 (2006), no. 4, 949–957 (electronic).
[16] P. Etingof and V. Ginzburg, Symplectic reﬂection algebras, Calogero-Moser space, and deformed
Harish-Chandra homomorphism, Invent. Math. 147 (2002), no. 2, 243–348.
[17] S. Fiedler-Le Touz´e, Pencils of cubics as tools to solve an interpolation problem, Appl. Algebra
Engrg. Comm. Comput. 18 (2007), no. 1-2, 53–70.
[18] Wm. Fulton, Young tableaux, London Mathematical Society Student Texts, vol. 35, Cambridge
University Press, Cambridge, 1997, With applications to representation theory and geometry.
[19] Wm. Fulton and J. Harris, Representation theory, Graduate Texts in Mathematics, vol. 129,
Springer-Verlag, New York, 1991, A ﬁrst course, Readings in Mathematics.
[20] Wm. Fulton and P. Pragacz, Schubert varieties and degeneracy loci, Lecture Notes in Mathematics,
vol. 1689, Springer-Verlag, Berlin, 1998.
[21] M. Gaudin, La fonction d’onde de Bethe, Collection du Commissariat `a l’´Energie Atomique: S´erie
Scientiﬁque., Masson, Paris, 1983.
[22] L. R. Goldberg, Catalan numbers and branched coverings by the Riemann sphere, Adv. Math. 85
(1991), no. 2, 129–144.
[23] P. Griﬃths and J. Harris, Principles of algebraic geometry, J. Wiley and Sons, 1978.
[24] Mark D. Haiman, Dual equivalence with applications, including a conjecture of Proctor, Discrete
Math. 99 (1992), no. 1-3, 79–113.
[25] J. Harris and I. Morrison, Moduli of curves, Graduate Texts in Mathematics 187, Springer-Verlag,
1998.
[26] D. Hilbert, ¨Uber die Darstellung deﬁniter Formen als Summe von Formen-quadraten, Math. Ann.
32 (1888), 342–350.
[27] C. Hillar, L. Garc´ıa-Puente, A. Mart´ın del Campo, J. Ruﬀo, Z. Teitler, Stephen L. Johnson, and
F. Sottile, Experimentation at the frontiers of reality in Schubert calculus, 2009, arXiv:0906.2497.
[28] I. V. Itenberg, V. M. Kharlamov, and E. I. Shustin, Welschinger invariant and enumeration of
real rational curves, Int. Math. Res. Not. (2003), no. 49, 2639–2653.
[29] , Logarithmic equivalence of the Welschinger and the Gromov-Witten invariants, Uspekhi
Mat. Nauk 59 (2004), no. 6(360), 85–110.
[30] M. Joswig and N. Witte, Products of foldable triangulations, Adv. Math. 210 (2007), no. 2, 769–
796.
[31] D. Kazhdan, B. Kostant, and S. Sternberg, Hamiltonian group actions and dynamical systems of
Calogero type, Comm. Pure Appl. Math. 31 (1978), no. 4, 481–507.
[32] V. Kharlamov and F. Sottile, Maximally inﬂected real rational curves, Mosc. Math. J. 3 (2003),
no. 3, 947–987, 1199–1200.
[33] A. G. Khovanski˘ı, Fewnomials, Translations of Mathematical Monographs, vol. 88, American
Mathematical Society, Providence, RI, 1991.
[34] S. L. Kleiman, The transversality of a general translate, Compositio Math. 28 (1974), 287–297.
[35] S. L. Kleiman and D. Laksov, Schubert calculus, Amer. Math. Monthly 79 (1972), 1061–1082.

40 FRANK SOTTILE

[36] M. Kontsevich and Yu. Manin, Gromov-Witten classes, quantum cohomology, and enumerative
geometry, Comm. Math. Phys. 164 (1994), no. 3, 525–562.
[37] E. Kostlan, On the distribution of roots of random polynomials, From Topology to Computation:
Proc. Smalefest (Berkeley, CA, 1990), Springer, New York, 1993, pp. 419–431.
[38] P. P. Kulish and E. K. Sklyanin, Quantum spectral transform method. Recent developments, Inte-
grable quantum ﬁeld theories: proceedings of the symposium held at Tvarminne, Finland, 23-27
March, 1981 (J. Hietarinta and C. Montonen, eds.), Lecture Notes in Phys., vol. 151, Springer,
Berlin, 1982, pp. 61–119.
[39] G. Mikhalkin, Enumerative tropical algebraic geometry in R2, J. Amer. Math. Soc. 18 (2005),
no. 2, 313–377.
[40] E. Mukhin, V. Tarasov, and A. Varchenko, The B. and M. Shapiro conjecture in real algebraic
geometry and the Bethe ansatz, 2005, Annals of Mathematics, to appear.
[41] , Bethe eigenvectors of higher transfer matrices, J. Stat. Mech. Theory Exp. (2006), no. 8,
P08002, 44 pp. (electronic).
[42] , Bispectral and (glN , glM ) dualities, Funct. Anal. Other Math. 1 (2006), no. 1, 47–69.
[43] , Generating operator of XXX or Gaudin transfer matrices has quasi-exponential kernel,
SIGMA Symmetry Integrability Geom. Methods Appl. 3 (2007), Paper 060, 31 pp.
[44] , On reality property of Wronski maps, 2007, Conﬂuentes Mathematici, to appear.
[45] , Schubert calculus and representations of general linear group, 2007, Journal of the AMS,
to appear.
[46] , Bethe algebra of gaudin model, calogero-moser space and cherednik algebra, 2009,
arXiv:0906.5185.
[47] E. Mukhin and A. Varchenko, Critical points of master functions and ﬂag varieties, Commun.
Contemp. Math. 6 (2004), no. 1, 111–163.
[48] , Norm of a Bethe vector and the Hessian of the master function, Compos. Math. 141
(2005), no. 4, 1012–1028.
[49] K. Purbhoo, Jeu de taquin and a monodromy problem for Wronskians of polynomials, 2009,
arXiv:0902.1321.
[50] J. Ruﬀo, Y. Sivan, E. Soprunova, and F. Sottile, Experimentation and conjectures in the real
Schubert calculus for ﬂag manifolds, Experiment. Math. 15 (2006), no. 2, 199–221.
[51] B. Sagan, The symmetric group, second ed., Graduate Texts in Mathematics, vol. 203, Springer-
Verlag, New York, 2001.
[52] V. Schechtman and A. Varchenko, Arrangements of hyperplanes and Lie algebra homology, Invent.
Math. 106 (1991), no. 1, 139–194.
[53] I. Scherbak and A. Varchenko, Critical points of functions, sl2 representations, and Fuchsian
diﬀerential equations with only univalued solutions, Mosc. Math. J. 3 (2003), 621–645, 745.
[54] H. Schubert, Anzahl-Bestimmungen f¨ur lineare R¨aume beliebiger Dimension, Acta. Math. 8
(1886), 97–118.
[55] M. P. Sch¨utzenberger, Quelques remarques sur une construction de Schensted, Math. Scand. 12
(1963), 117–128.
[56] Secant Team, Frontiers of Reality in Schubert Calculus, www.math.tamu.edu/~secant.
[57] J. Solomon, Intersection theory on the moduli space of holomorphic curves with Lagrangian bound-
ary conditions, math.SG/0606429.
[58] E. Soprunova and F. Sottile, Lower bounds for real solutions to sparse polynomial systems, Adv.
Math. 204 (2006), no. 1, 116–151.
[59] F. Sottile, Enumerative geometry for the real Grassmannian of lines in projective space, Duke
Math. J. 87 (1997), no. 1, 59–85.
[60] , Pieri-type formulas for maximal isotropic Grassmannians via triple intersections, Colloq.
Math. 82 (1999), no. 1, 49–63.
[61] , The special Schubert calculus is real, Electron. Res. Announc. Amer. Math. Soc. 5 (1999),
35–39 (electronic).
[62] , Real Schubert calculus: polynomial systems and a conjecture of Shapiro and Shapiro,
Experiment. Math. 9 (2000), no. 2, 161–182.

FRONTIERS OF REALITY IN SCHUBERT CALCULUS 41

[63] , Some real and unreal enumerative geometry for ﬂag manifolds, Michigan Math. J. 48
(2000), 573–592, Dedicated to William Fulton on the occasion of his 60th birthday.
[64] R. P. Stanley, Enumerative combinatorics. Vol. 2, Cambridge Studies in Advanced Mathematics,
vol. 62, Cambridge University Press, Cambridge, 1999.
[65] D. Talalaev, Quantization of the gaudin system, 2004, arXiv:hep-th/0404153.
[66] R. Vakil, Schubert induction, Ann. of Math. (2) 164 (2006), no. 2, 489–512.
[67] J. Verschelde, Numerical evidence for a conjecture in real algebraic geometry, Experiment. Math.
9 (2000), no. 2, 183–196.
[68] J.-Y. Welschinger, Invariants of real rational symplectic 4-manifolds and lower bounds in real
enumerative geometry, C. R. Math. Acad. Sci. Paris 336 (2003), no. 4, 341–344.
[69] D. White, Sign-balanced posets, J. Combin. Theory Ser. A 95 (2001), no. 1, 1–38.
[70] G. Wilson, Collisions of Calogero-Moser particles and an adelic Grassmannian, Invent. Math.
133 (1998), no. 1, 1–41, With an appendix by I. G. Macdonald.

Department of Mathematics, Texas A&M University, College Station, TX 77843,
USA
E-mail address: sottile@math.tamu.edu
URL: www.math.tamu.edu/~sottile
