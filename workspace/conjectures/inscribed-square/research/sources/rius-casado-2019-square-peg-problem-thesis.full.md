<!-- source: https://diposit.ub.edu/bitstreams/faaf3e1f-d770-4fab-b829-c543947edef7/download | converted from PDF -->

GRAU DE MATEM `ATIQUES

Treball ﬁnal de grau

THE SQUARE PEG PROBLEM

Autora: Raquel Rius Casado

Director: Dr. Joan Carles Naranjo Del Val

Realitzat a: Departament de Matem`atiques i Inform`atica

Barcelona, 15 de juny de 2019

Contents

1 Introduction 1

2 Jordan Theorem 3

3 Square Peg Problem 8
3.1 History of the problem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
3.2 Several results . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2.1 Witty and easy results . . . . . . . . . . . . . . . . . . . . . . . . . 9
3.2.2 Arnold Emch . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 12
3.2.3 Lev Schnirelmann . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
3.3 Previous tools . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18
3.4 Walter Stromquist’s proof . . . . . . . . . . . . . . . . . . . . . . . . . . . 23

4 Latest study 38

Bibliography 41

Abstract

The Square Peg Problem, also known as Toeplitz’ Conjecture, is an unsolved problem
in the mathematical areas of geometry and topology which states the following: every
Jordan curve in the plane inscribes a square.
Although it seems like an innocent statement, many authors throughout the last century
have tried, but failed, to solve it. It is proved to be true with certain “smoothness
conditions” applied on the curve, but the general case is still an open problem. We intend
to give a general historical view of the known approaches and, more speciﬁcally, focus on
an important result that allowed the Square Peg Problem to be true for a great sort of
curves: Walter Stromquist’s theorem.

2010 Mathematics Subject Classiﬁcation. 54A99, 53A04, 51M20

Acknowledgements

Primer de tot, m’agradaria agrair al meu tutor Joan Carles Naranjo la paci`encia i el
recolzament que m’ha oferit durant aquest treball. Moltes gr`acies per acompanyar-me en
aquest trajecte ﬁnal.

Aquesta carrera ha suposat un gran repte personal a nivell mental. ´Es per aix`o que voldria
agrair, en especial, a les meves amigues i companyes de carrera Soraya i Laura. ´Es amb
elles amb qui he unit forces durant tots aquests anys per poder acabar graduant-nos les
tres juntes. Tamb´e voldria fer especial menci´o al Marc, amb qui comparteixo la passi´o
per les matem`atiques i qui m’ha oferit el seu recolzament total tant com a parella com a
matem`atic. Afrontar la carrera amb vosaltres tres ha fet que aprendre matem`atiques fos
encara m´es bonic del que ja ´es (i que l’aprovat d’EDOS fos possible). Moltes gr`acies per
creure en mi quan ni jo ho feia.

Finalment, voldria agrair a la meva fam´ılia per donar-me el seu recolzament moral des
del principi i aguantar els meus estats d’`anim durant aquests anys, i a les meves amistats
externes del m´on de les matem`atiques per acceptar la meva abs`encia durant les `epoques
d’ex`amens (i durant tota la carrera en general).

Chapter 1

Introduction

The Square Peg Problem, also known as the Inscribed Square Problem or Toeplitz’ Con-
jecture, is a still open problem which numerous authors have tried to solve for the last
hundred years. It is usually attributed to the German mathematician Otto Toeplitz.
The problem asks whether every Jordan curve in the plane has four points which form a
square:

Conjecture 1.1 (Square Peg Problem). Every continuous simple closed curve in the
plane γ : S1 −→ R2 contains four points that are the vertices of a square.

A continuous simple closed curve in the plane is also called a Jordan curve, and it is the
same as a continuous injective map from the unit circle into de plane. In other words, a
topological embedding S1 ↪→ R2.
Notice that Conjecture 1.1 does not require the square to lie fully inside the curve. We
can see an example in Figure 1.1.

Figure 1.1: Example of the Square Peg Problem

The problem has been solved for curves that are “smooth enough”, but remains open
for the continuous general case. Several authors found positive results by varying the
smoothness condition, which has become weaker over the years. Most of these studies
have in common the claim that there is an odd number of inscribed squares in such a
smooth curve, since proving this fact is a guarantee of the existence of a square.

But, why is the general case still unsolved? One may think that it is natural to approach
the problem by approximating a given continuous curve by a sequence of smooth curves,
which, each of them, is known to inscribe a square (using one of the existing smooth
results). By converging the sequence we would get, therefore, an inscribed square in the
original continuous curve. In other words, given a Jordan curve γ approximated by a

1

2 Introduction

sequence γn of certain smooth curves, then, since any γn inscribes a square Qn, there is a
converging subsequence (Qnk )k (by compactness) whose limit is an inscribed square for the
curve γ. However, it could happen that the approximated inscribed squares degenerate to
a point in the limit. Even if the given curve γ is smooth except for a single singular point,
all squares in the approximating curves could concentrate into that singular point in the
limit. This problem is the reason why it has not been possible to remove the smoothness
condition in the known positive results of the problem so far.

The aim of this text is to show some of the proofs obtained throughout these years. We
focus on a particular result that had a great impact on the problem’s history: Walter
Stromquist’s theorem. He proved the Square Peg Problem for curves that are “locally
monotone”, a smoothness condition that is satisﬁed for curves that are convex, polygon
or, under certain restrictions, piecewise of class C1 (in Section 3.4 we give the accurate
deﬁnition as well as the mentioned proof). We also provide an abstract of the proof of
the ﬁrst historical result (satisﬁed for ”smooth enough” convex curves, found in Section
3.2.2) and a survey through most of the solutions found during the last hundred of years.

In order to see the previous matter, we have divided the work into the following three
parts:

In Chapter 2, we recall the deﬁnition of Jordan curve, state the Jordan curve theorem
and give a short proof of it.

We start Chapter 3 by giving a deeper historical review of the so far obtained results. We
complement this part by showing some easy results as a motivation of the problem and
then proceed to overview two of the historical proofs which meant an important progress
of the Square Peg Problem.
At the end of the chapter, we provide some topological tools required to follow Stromquist’s
proof. These are from simplicial and singular homology. We conclude Chapter 3 by show-
ing Walter Stromquist’s proof, which is our main object of study.

We have added an extra chapter, Chapter 4, to remark the furthest result of the Square
Peg Problem, provided by the mathematician Terence Tao. It is a quick review of his
work, since its diﬃculty escapes from the degree’s level.

Chapter 2

Jordan Curve Theorem

The Square Peg Problem is stated for a Jordan curve, as we have seen in the ﬁrst chapter.
There is a classical theorem in topology which asserts an essential fact about Jordan
curves: the Jordan curve theorem. This theorem was originally conjectured by Camile
Jordan in 1892.
In this chapter, we will introduce the Jordan curve theorem as well as a short proof of
it, using the theorem of the Brouwer ﬁxed point. This ingenious proof belongs to Ryuji
Maehara, who wrote it in [6]. But, before we start, let us give the deﬁnition of a Jordan
curve:

Deﬁnition 2.1. A Jordan curve is a continuous simple closed curve in R2. That is, the
image of an injective continuous map of the unit circle into the plane:

γ : S1 −→ R2.

Thus, a Jordan curve is the homeomorphic image of a circle.
We will also be talking about “arcs”. We denote by arc the homeomorphic image of a
closed interval [a, b], where a < b.

Now we are ready to introduce the chapter’s main theorem:

Theorem 2.2 (Jordan Curve Theorem). The complement in the plane R2 of a Jordan
curve J consists of two components, each of which has J as its boundary.

In other words, the Jordan curve theorem states something geometrically visual: a simple
closed curve always divides the plane into two parts, the outer and the inner part. Let us
note two facts concerning the components of R2 − J, where J is the Jordan curve:

1. R2 − J has exactly one unbounded component.

2. Each component of R2 − J is path-connected and open.

The assertion (1) follows from the boundedness of J, and (2) from the local path-
connectedness of R2 and the closedness of J.

In order to prove the Jordan curve theorem, we will ﬁrst introduce two theorems: the
Brouwer ﬁxed point and Tietze extension theorem. The Brouwer ﬁxed point theorem will

3

4 Jordan Theorem

be used during the main proof, as we mentioned before, while Tietze extension theorem
will be applied to prove our ﬁrst lemma (Lemma 2.5, found below).

Theorem 2.3 (Brouwer Fixed Point Theorem). Every continuous map from a disk into
itself has a ﬁxed point.

Theorem 2.4 (Tietze Extension Theorem). Let X be a normal space and A a closed
subspace of X.

1. Any continuous map from A to the closed interval [a, b] of R can be extended to a
map from all X to [a, b].

2. Any continuous map from A to R can be extended to a continuous map from all X
to R.

We will now introduce and prove two lemmas which will be needed during Jordan curve
theorem’s proof. Once we have proved them, we will ﬁnally proceed with the chapter’s
main proof.

Lemma 2.5. If R2 − J is not connected, then each component has J as its boundary.

Proof. By assumption, R2 − J has at least two components. Let U be an arbitrary
component. Since any other component W is disjoint from U and is open, we have that
W contains no point of the closure U and, hence, no point of the boundary U ∩ U c of U .
Thus, U ∩ U c ⊂ J.

Now we suppose that U ∩ U c ̸= J. We will show that this leads to a contradiction.

Since U ∩ U c ̸= J, there exists an arc A ⊂ J such that U ∩ U c ⊂ A. By (1), we know that
R2 − J has at least one bounded component. Let o be a point in a bounded component.
If U itself is bounded, we choose o in U .

Let D be a large disk with center o such that its interior contains J. Then the boundary
of D, which we will note by S, is contained in the unbounded component of R2 − J. Since
A is an arc, we know it is homeomorphic to the interval [0, 1]. By the Tietze Extension
Theorem, the identity map A −→ A has a continuous extension r : D −→ A. This is
possible since D is a normal space and A is a closed interval of R.

We deﬁne a map q : D −→ D − {o}, according as if U is bounded or not. If U is bounded
we deﬁne it by
 q(z) =
 {
r(z) f or z ∈ U ,

z f or z ∈ U c,

Otherwise by
 q(z) =
 {
z f or z ∈ U ,

r(z) f or z ∈ U c.
 5

By U ∩ U c ⊂ A, the intersection of the two closed sets U and U c lies on A, on which r is
the identity map. Thus, q is well deﬁned and continuous. Note that q(z) = z if z ∈ S.

Now let p : D − {o} −→ S be the natural projection and let t : S −→ S be the antipodal
map. Then the composition t ◦ p ◦ q : D −→ S ⊂ D has no ﬁxed point. This contradicts
the Brouwer ﬁxed point theorem and, therefore, we prove the lemma.

The previous proof implicity contains a proof that no arc separates R2. This is often a
lemma to the Jordan curve theorem.

Before getting into the next lemma, let us denote the rectangular set {(x, y) | a ≤ x ≤
b, c ≤ y ≤ d} in the plane R2 as E(a, b; c, d), where a < b and c < d.

Lemma 2.6. Let h(t) = (h1(t), h2(t)) and v(t) = (v1(t), v2(t)), where −1 ≤ t ≤ 1, be
continuous paths in E(a, b; c, d) satisfying

h1(−1) = a, h1(1) = b, v2(−1) = c, v2(1) = d.

Then the two paths meet, i.e., h(s) = v(t) for some s,t in [−1, 1].

In other words, when t = −1, h(−1) = (a, h2(−1)) and v(−1) = (v1(−1), c). Whereas
when t = 1, we have h(1) = (b, h2(1)) and v(1) = (v1(1), d). This means that h(t) will
trace its path horizontally from a to b, while v(t) will do it vertically from c to d. Then,
both will meet at some point.

Proof. Suppose h(s) ̸= v(t) for all s, t. Let N (s, t) denote the maximum-norm of h(s)−v(t)

N (s, t) = max{|h1(s) − v1(t)|, |h2(s) − v2(t)|}.

Then N (s, t) ̸= 0 for all s, t. We deﬁne a continuous map F from E(−1, 1; −1, 1) into
itself by
 F (s, t) = ( v1(t) − h1(s)
N (s, t) , h2(s) − v2(t)
N (s, t)
 ) .

Notice that if N (s, t) takes the value |h1(s) − v1(t)|, then

F (s, t) = (
±1, h2(s) − v2(t)
|h1(s) − v1(t)|
 ) .

While if N (s, t) = |h2(s) − v2(t)|, then

F (s, t) = ( v1(t) − h1(s)
|h2(s) − v2(t)| , ±1
) .

Therefore, the image of F is in the boundary of E(−1, 1; −1, 1) and, in fact, the map F
goes from E(−1, 1; −1, 1) into itself, as we previously said.

We need to see that F has no ﬁxed point, so it contradicts the Brouwer ﬁxed point
theorem.
Assume F (s0, t0) = (s0, t0). By the above remark, we have |s0| = 1 or |t0| = 1. Suppose,

6 Jordan Theorem

for example, s0 = −1. Since h1(−1) = a, v1(t0) − a ≥ 0. Also, N (−1, t0) ≥ 0. Then, the
ﬁrst coordinate of F (−1, t0), (v1(t0) − h1(−1)/N (−1, t0)), is nonnegative. Hence, it can
not equal s0 (= −1). Similarly, the other cases of |s0| = 1 or |t0| = 1 can not occur. This
implies that F (s, t) has no ﬁxed point. But since E(−1, 1; −1, 1) is homeomorphic to a
disk, this contradicts the Brouwer ﬁxed point theorem.

Now that we have seen both lemmas, we can prove the Jordan curve theorem.

Proof (Jordan curve theorem). By Lemma 2.5, we only need to show that R2 − J has one
and only one bounded component. This is because by assertion (1) R2 − J has exactly
one unbounded component. So if we see, that besides this one, R2 − J has one bounded
component, Lemma 2.5 will imply that both components have J as their boundary, which
is exactly what Jordan curve theorem says.

The proof will be divided into three parts: establishing the notation and deﬁning a point
z0 in R2 − J, proving that the component U containing z0 is bounded and proving that
there is no bounded component other than U .

Since J is compact, there exist points a, b in J such that the distance ∥a−b∥ is the largest.
We may assume that a = (−1, 0) and b = (1, 0). Then the rectangular set E(−1, 1; −2, 2)
contains J, and its boundary, that we will denote by Γ, meets J at exactly two points a
and b, as shown in Figure 2.1.

Figure 2.1: Construction of E(−1, 1; −2, 2) containing J

Let n be the middle point of the top side of E(−1, 1; −2, 2), n = (0, 2), and s the middle
point of the bottom side, s = (0, −2). The segment ns meets J by Lemma 2.6, where
we take h(t) as J and v(t) as ns. Let l be the y-maximal point (that means the point

7

(0, y) with maximal y) in J ∩ ns. Points a and b divide J into two arcs. We denote the
one containing l by Jn, and the other by Js. Let m be the y-minimal point in Jn ∩ ns.
Possibly l = m. Then the segment ms meets Js; otherwise the path nl + lm
⌢ + ms (where
lm
⌢ denotes the subarc of Jn with end points l and m) could not meet Js, contradicting
Lemma 2.6. Let p and q denote the y-maximal point and the y-minimal point in Js ∩ ms,
respectively. Finally, let z0 be the middle point of the segment mp.

We have deﬁned our point z0, which we have ensured to be in R2 − J via the previous
construction and, more speciﬁcally, in the supposed bounded component of R2 − J. Now
we will show that U , the component of R2 − J that contains z0, is, in fact, bounded. To
prove so, let us suppose U is unbounded. Since U is path-connected, there exists a path
α in U from z0 to a point outside E(−1, 1; −2, 2). Let w be the ﬁrst point at which α
meets the boundary Γ of E(−1, 1; −2, 2). We denote αw the part of α from z0 to w. If w
is on the lower half of Γ, we can ﬁnd a path ws⌢ in Γ from w to s which contains neither a
nor b. Now consider the path nl + lm
⌢ + mz0 + αw + ws⌢. This path does not meet Js, by
hypothesis, contradicting Lemma 2.6. Similarly, if w is on the upper half of Γ, the path
sz0 + αw + wn⌢ fails to meet Jn, where wn⌢ is the shortest path in Γ from w to n. The
contradiction shows that U is a bounded component.

We have proven the existence of the bounded component. Let us see its uniqueness.
Suppose that there exists another bounded component W (W ̸= U ) of R2 − J. Clearly,
W ⊂ E(−1, 1; −2, 2). We denote by β the path nl + lm
⌢ + mp + pq⌢ + qs, where pq⌢ is the
subarc of Js, from p to q. Notice that β has no point of W . This is because the path mp
belongs to U , since it meets z0, and we have supposed that W ̸= U . Also, the subarcs lm
⌢

and pq⌢ can not be in W because lm
⌢ ⊂ Jn and pq⌢ ⊂ Js. Since a and b are not on β, there
are circular neighborhoods Va, Vb of a, b, respectively, such that each of them contains no
point of β. By Lemma 2.5, a and b are in the closure W . Hence, there exist a1 ∈ W ∩ Va
and b1 ∈ W ∩ Vb.
Since W is path-connected, there exists a path from a1 to b1. Let a1b1⌢ be this path in W .
Then, the path aa1+ a1b1⌢
+b1b fails to meet β, because we have shown that β has no point
of W . But by Lemma 2.6 we know that the path intersects β. This is a contradiction
and, therefore, this completes our proof.

Chapter 3

Square Peg Problem

In this chapter we will focus on the history of the Square Peg Problem. We will start by
introducing the most important studies with their chronological order and overviewing
some of these proofs. More precisely, we will see in detail the ﬁrst proof provided by
Arnold Emch, so we acknowledge the initial attempts of the problem. At the end of the
chapter we will study Walter Stromquist’s proof and see how he managed to get one of
the weakest smoothness conditions.

3.1 History of the problem

Most part of the historical chronology found in this section has been extracted from the
survey [7] made by Benjamin Matschke.

The Square Peg Problem ﬁrst appeared in 1911. Otto Toeplitz gave a talk whose second
part had the title “On some problems in topology”, in which he mentioned the problem
and claimed to have the solution only for convex curves. However, it seems that Toeplitz
never published the proof.

In 1913, Arnold Emch proved it for “smooth enough” convex curves [1], which was the
ﬁrst major result. Two years later, Emch published in [2] a further proof that required a
weaker smoothness condition and in which he wrote that he did not know that Toeplitz
and his students discovered the problem independently two years earlier. Despite this
fact, the conjecture is usually attributed to Toeplitz. Emch presented a third paper in
1916 [3], where he proved the Square Peg Problem for curves that are piecewise analytic
with a ﬁnite number of inﬂexions and other singularities. We will show his ﬁrst proof in
the next section (Section 3.2.2).

In 1929, Schnirelmann proved the problem for a class of curves that is slightly larger than
C2: curves with piecewise continuous curvature. This paper was published in a Russian
publication, but an extended version, which corrects some minor errors, was published
posthumously in 1944 [13]. Schnirelmann noted that for a generic curve, the parity of the
number of inscribed squares must be invariant as the curve is deformed. The proof uses
a local lemma on existence of inscribed square for closed curves. Heinrich Guggenheimer
studied Schnirelmann’s proof and claimed that it still contained errors. He corrected

8

3.2 Several results 9

several technical points and concluded that the curve needs to have a bounded variation
so the proof works.

In 1961, Jerrard [5] examined the case of real-analytic curves (curves whose coordinate
functions are each real-analytic) and showed that each such curve admits an odd number
of inscribed squares.

In 1989, Walter Stromquist [14] proved one of the furthest results of the Square Peg
Problem. He introduced the smoothness condition “locally monotone” which is satisﬁed
when the curve is convex, polygon or, under certain restrictions, piecewise of class C1.
We will study this proof in detail at the end of this chapter (Section 3.4).

Other results are due to Hebbert, when γ is a quadrilateral, Nielsen and Wright for curves
that are symmetric across a line or about a point (see Section 3.2.1), Pak [12] for piecewise
linear curves, Cantarella, Denne, McCleary for C1 curves and Matschke [8] for an open
dense class of curves (curves that did not contain small trapezoids of a certain form), as
well as curves that were contained in annuli in which the ratio between the outer and the
inner radius is at most 1 + √2.

The latest result is due to Terence Tao [15] in 2017, where he proves the Square Peg
Problem if the curve is the union of two Lipschitz graphs that agree at the endpoints,
and whose Lipschitz constants are strictly less than one. The condition he provides goes
a little bit further than the condition of locally monotone. We will overview Tao’s paper
in the next chapter (Chapter 4).

3.2 Several results

3.2.1 Witty and easy results

Before we get into the important dense results obtained by some of the previously men-
tioned authors, we would like to oﬀer some quick and clever proofs as a motivation of the
problem.

Square inscribed in a function

Suppose we form a simple closed curve by adjoining the segment of the x-axis from x = 0
to x = 1 to the graph of a continuous function

f : [0, 1] −→ R

such that f (0) = f (1) = 0 and f (x) > 0, for 0 < x < 1, as seen in Figure 3.1. Let us see
that this curve inscribes a square.

Proof. We will only need the extreme value theorem and the intermediate value theorem
in order to proof it.

First, by the extreme value theorem, the function f assumes its maximum value m at
some x1. In other words, f (x1) = m, where f (x) ≤ m for any value of x.

Now, we deﬁne a function g : [0, 1] −→ R such that

g(x) = x + f (x).

10 Square Peg Problem

Then, we have
 g(0) = 0

g(1) = 1

Using the intermediate value theorem, there is some x2 between 0 and 1 so that

g(x2) = x1.

Now, we deﬁne another function h like

h(x) = f (x) − f (g(x)).

To assure that this deﬁnition makes sense, we will consider f (x) = 0 for all values of x
outside [0, 1]. Then, h(x1) = f (x1) − f (g(x1)) = m − f (g(x1)) which is positive or zero,
since m is the maximum value of the function f . But we also have h(x2) = f (x2) −
f (g(x2)) = f (x2) − f (x1) = f (x2) − m, which is negative or zero.
By the intermediate value theorem, there is a value x0 between x1 and x2 such that
h(x0) = 0, which is the same as
 f (x0) = f (x0 + f (x0)).

Therefore, the points x = x0 and x = x0 + f (x0) on the x-axis are the base corners of the
inscribed square, as shown in Figure 3.1.

Figure 3.1: Square inscribed in a function

Square inscribed in symmetric curve

In this case, we are going to see the theorem proved by Mark J. Nielsen and S.E. Wright
in [11], where the curve is a Jordan curve symmetric about a point.

Theorem 3.1. Every simple closed curve that is symmetric about the origin has an
inscribed square.

3.2 Several results 11

Figure 3.2: Jordan curve symmetric about O

Proof. Let J be a Jordan curve symmetric about the origin O. This means that for each
point P on J, the point −P (whose coordinates are negatives of the coordinates of P )
is also on J. Let f : R2 −→ R2 be the function that rotates each point in the plane 90
degrees about the origin.

Figure 3.3: J and its rotated image f (J)

We can see in Figure 3.3 that J and its rotated image f (J) intersect each other. If we
suppose they do, they must share a point in common. Then, if we choose a point f (P ) on
f (J) that is also on J, the points P, f (P ), −P, −f (P ) form the vertices of a square (see
Figure 3.4). And, since all four points are on J, then we have that J inscribes a square.

All that remains now is to see that J and f (J) intersect. To show this, consider Pnear
and Pf ar to be the points on the curve J that are at minimum and maximum distance
from the origin respectively. Then, f (Pnear) is as close to O as any point of J, since f

12 Square Peg Problem

does not change any distance, and f (Pf ar) is as far from O as any point of J. Thus, we
have the cases of f (Pnear) being inside or on J and f (Pf ar) being outside or on J.
If either of them is on J, we are done, since J and f (J) would intersect on that point.
Otherwise, if f (Pnear) is inside J and f (Pf ar) is outside J, then f (J) must connect both
points, and hence it must cross J somewhere (because of the Jordan curve theorem).

Figure 3.4: P, f (P ), −P, −f (P ) form the vertices of a square

3.2.2 Arnold Emch

Arnold Emch provided the ﬁrst result of the Square Peg Problem for convex curves. Here
we will give an overview of his paper Some Properties of Closed Convex Curves in a Plane,
noting the theorems and previous conditions he states before proving the main theorem:
It is always possible to inscribe a square in an oval.
Emch denotes a “closed convex curve” with the term “oval”, as we will deﬁne below. The
aim of his work, then, is to prove that at least one square is inscribed in a convex closed
curve.

Let us ﬁrst introduce his deﬁnition of “oval”. He considers a convex domain as the
regular deﬁnition of convex domain (a ﬁnite, closed domain which contains with any two
points also the entire segment between them), indicating that through every point of the
boundary of such a domain, there is at least one straight line so that all points of the
domain which are not on the line lie only on one side of the line. This line is denoted
with the term supporting line. Then, an oval encloses such a domain, including the oval
itself. Emch deﬁnes it parametrically by two distinct continuous single-valued periodic
functions x = φ(t), y = ψ(t),

where t ∈ R and both have period w.

Now, he places several restrictions on these functions. First, he considers its derivatives
φ′(t), ψ′(t) w-periodic and continuous for all deﬁnite values of t. He excludes singular

3.2 Several results 13

points by assuming that both derivatives φ′(t), ψ′(t) do not vanish simultaneously for any
values of t and he excludes any straight portions of the boundary by including in the
deﬁnition of an oval that for no parts of the period-interval, the functions φ(t) and ψ(t)
remain constant or depend linearly upon t.

He also assumes that at every point of the oval there exists a deﬁnite tangent and, if the
point of tangency varies continuously, the direction of the tangent varies continuously.
Also, for t = 0 or t = w, none of the functions φ(t), ψ(t), φ′(t), ψ′(t) vanish and we have
φ(0) = φ(w), φ′(0) = φ′(w), ψ(0) = ψ(w), ψ′(0) = ψ′(w).

Now that we have deﬁned all the conditions on the oval imposed by Emch, we will intro-
duce some theorems he states ﬁrst in order to prove the main result afterwards.

Theorem 3.2. There are always two and only two tangents to an oval parallel to any
given direction.

This is true since if there were three distinct parallel tangents t1, t2, t3, with t2 between
the other two, then there would be points belonging to the domain of both sides of t2,
which can not occur (according to the property of a supporting line).

Emch denotes by “reentrant quadrangle” a quadrangle A1A2A3A4 in which one of the
vertices lies within the boundary of the triangle formed by the remaining three, as seen
in Figure 3.5, where the mentioned vertex corresponds to A4. This is shown by getting in
contradiction with the assertion that all points outside of a segment AiAj are excluded
from the domain. Then, we have:

Theorem 3.3. No reentrant quadrangle can be inscribed in an oval.

Figure 3.5: Reentrant quadrangle A1A2A3A4.

Theorem 3.4. Two distinct rhombs with corresponding parallel sides or parallel axes can
never be inscribed in the same oval.

14 Square Peg Problem

This is proved by using the fact that wherever the two rhombs are placed, four of their
vertices will always form a reentrant quadrangle. Thus, no oval can pass through them.

Theorem 3.5. Let a and b be two distinct real numbers, and let λ = φ1(θ), µ = ψ1(θ)
be two uniform continuous real functions of a parameter θ, subject to the only condition
that two distinct values α and β of the parameter θ exist, so that

φ1(α) = ψ1(β) = a,

φ1(β) = ψ1(α) = b;

then there exists at least one value of θ, say θ = γ, for which φ1(γ) = ψ1(γ).

This follows from the fact that φ1(θ) − ψ1(θ) is continuous and, hence, takes every value
between a−b and b−a. That is, there is at least one value of θ, γ, such that φ1(γ) = ψ1(γ).

Using all the previous results, Emch proves the main theorem:

Theorem 3.6. It is always possible to inscribe a square in an oval.

Proof. Emch uses a geometric construction to prove the existence of a rhombus inside an
oval, seen in Figure 3.8. He proceeds as follows:
Having our curve placed in the plane, we assume any point O, outside the curve, and
we draw any line lα through this point. Now, we draw the chords of the oval parallel to
lα, determining their respective midpoints, and we add the tangents parallel to lα as well
as their points of tangency, denoted by Sα and Tα. If we connect all the midpoints, we
obtain a continuous curve Cα from Sα to Tα. In his later publications, Emch will denote
this locus of midpoints by median. This construction is seen in Figure 3.6.

Figure 3.6: Chords of the oval parallel to lα and the curve Cα through their midpoints.

3.2 Several results 15

Next, we draw through O a line lβ perpendicular to lα, and we repeat the same construc-
tion with respect to this line. Thus, we obtain a continuous curve Cβ extending from Sβ
to Tβ, as well as the two tangents of the oval parallel to lβ.

The two tangents parallel to lα and the two parallel to lβ form a rectangle. Also, the
curves Cα and Cβ necessarily intersect within the domain of the oval. In fact, there is
always only one real point of intersection between Cα and Cβ, that we will denote as Pαβ.
This is true, since if there were two points of intersection, then there would exist two
rhombs with parallel axes inscribed in the oval, in contradiction with Theorem 3.4. We
can see the construction of the chords parallel to lβ and the curve Cβ in Figure 3.7, where
the old construction is on a slightly softer colour and the newer one is on a stronger one.

Figure 3.7: Chords of the oval parallel to lβ and the curve Cβ through their midpoints.

If we draw the lines parallel to lα and lβ that pass through Pαβ, we see that they intersect
the oval at four points A, B, A′, B′, which form a rhombus ABA′B′. Thus, with every
pair of orthogonal rays lα and lβ through O is associated one deﬁnite rhombus inscribed
in the oval, and this same rhombus is evidently obtained when lα and lβ are interchanged.

Now that we have shown that a rhombus is inscribed in the curve, the ﬁnal step is to
prove that this rhombus becomes a square.

Emch notes that if we turn a line lξ through O continuously from lα to lβ, then its
orthogonal ray lη will turn in the same sense from lβ to lα. The corresponding curves
Cξ and Cη also change continuously, since their extremities Sξ, Sη, Tξ and Tη on the oval
change continuously. Therefore, their point of intersection Pξη describes a continuous
curve and hence the corresponding rhombus, denoted by XY X ′Y ′, changes continuously.
Then, the axes λ = XX ′ and µ = Y Y ′ of this rhombus may be expressed as uniform

16 Square Peg Problem

and continuous functions of a parameter θ associated with the direction of lξ, within the
interval between lα and lβ (including these limits). This θ may be chosen as the positive
angle between lξ and the positive part of the axis X.

Now, if we designate the diagonals of the original rhombus by a and b, the parameters
associated with lα and lβ by α and β, and the axes of the rhombus by

λ = φ(θ), µ = ψ(θ)

within the interval α ≤ θ ≤ β, where λ and µ are the uniform and continuous functions
of θ, then we have a = φ(α), b = ψ(α).

If now we turn the line lξ from lα to lβ, the rhombus XY X ′Y ′ changes from ABA′B′ to
BA′B′A, so that in the second position we have

λ = φ(β) = b, µ = ψ(β) = a.

That is, the diagonals are interchanged in the positions θ = α and θ = β. Thus, the
situation is exactly as stated in Theorem 3.5. There exists, therefore, at least one direction
lγ for which φ(γ) = ψ(γ) (λ = µ), i.e., where the rhombus becomes a square. In Figure
3.8 we have an overview of the whole construction.

Figure 3.8: Rhombs in the oval

Notice that Emch gives strong conditions on the curve, such as being diﬀerential and
excluding straight portions of the curve. This, as we mentioned, was the ﬁrst approach (or
at least the ﬁrst one known) of the Square Peg Problem. When we introduce Stromquist’s

3.2 Several results 17

proof at the end of this chapter, we will see that his results are much stronger than this
one.

Let us brieﬂy summarize the idea of the above proof using the notation Emch uses in his
later publications. He denotes by set of medians the set of all midpoints of the secants
(chords) of the curve parallel to a given direction. He shows that all medians of a closed
convex analytic curve are continuous and analytic curves. With each pair of directions σ
and τ there are associated two medians Mσ and Mτ , which always intersect in one and
only one point. Moreover, he sees that with every pair (σ, τ ) there is a rhomb associated
whose diagonals are parallel to σ and τ and whose vertices lie on the curve. Finally, he
concludes that to every closed convex analytic curve without rectilinear segments, at least
one square may be inscribed.

Besides this paper, Emch published two further proofs in [2] and [3], as we mentioned
before. In his second paper, On the Medians of a Closed Convex Polygon, he proves that
at least one square may be inscribed in any convex rectilinear polygon, and generally
in any closed convex curve formed by a ﬁnite number of ordinary analytic arcs. In his
third paper, On some properties of the Medians of Closed Continuous Curves formed by
Analytic Arcs, he generalises his result for any closed continuous curve composed of a
ﬁnite number of analytic arcs with a ﬁnite number of inﬂexions and other singularities.

3.2.3 Lev Schnirelmann

In 1929, Lev G. Schnirelmann oﬀered a solution for curves with piecewise continuous
curvature.

The following summary’s idea is obtained from [7], since we were not able to access to
Schnirelmann’s oﬃcial publication.

Schnirelmann’s idea is to describe the set of inscribed squares as a preimage. For instance,
in the following way:
Let γ : S1 −→ R2 be the given curve. The space (S1)4 parameterizes quadrilaterals that
are inscribed in γ. We construct a so-called test-map

fγ : (S1)
4 −→ R6,

which sends a 4-tuple (x1, x2, x3, x4) of points on the circle to the mutual distances between
γ(x1), . . . , γ(x4) ∈ R2, i.e., to (||γ(x1)−γ(x2)||, ||γ(x2)−γ(x3)||, ||γ(x3)−γ(x4)||, ||γ(x4)−
γ(x1)||, ||γ(x1) − γ(x3)||, ||γ(x2) − γ(x4)||).

Let V be the 2-dimensional linear subspace of R6 that corresponds to the points where
all four edges are of equal length and the two diagonals are of equal length. The preimage
f −1
γ (V ) is parameterizing the set of inscribed squares. Within this set, there are degener-
ate components. That is, points where x1 = x2 = x3 = x4 and, more generally, 4-tuples
where x1 = x3 and x2 = x4.

Schnirelmann claims that an ellipse inscribes exactly one square up to symmetry. Using
some smooth isotopy, he deforms the ellipse into the given curve γ via other curves
γt, where t ∈ [0, 1]. By smoothness, these inscribed squares do not come close to the

18 Square Peg Problem

degenerate quadrilaterals during the deformation. Thus, they do not degenerate to a
point. Therefore, the nondegenerate part of all preimages f −1
γt (V ) forms a 1-manifold
that connects the solution sets for γ and the ellipse. Using this result, he sees that the
parities of the number of inscribed squares on γ and on the ellipse coincide, leading to
the conclusion that any smooth curve inscribes generically an odd number of squares.

3.3 Previous tools

In this section we will give some previous needed theory in order to follow the proof
provided by Walter Stromquist. The following homology theory is extracted from [10]
and [4]. We only intend to give a basic and general idea of it, in order to understand the
tools required in the next section. This is why, we will state a summarized scheme.

Our object of study will be simplicial and singular homology. Simplicial homology de-
pends on an associated topological space which allows a triangulation (we will work with
simplicial complexes, see Deﬁnition 3.10), this is why it makes it easy to compute. Sin-
gular homology, on the other hand, is better adapted to theory than computation, which
gives it much advantage over singular homology. It is deﬁned for all topological spaces
and depends only on the topology, not on any triangulation.
We will begin with the properties of simplicial homology, followed by the ones for sigular
homology. At the end, we will see that both agree for spaces that can be triangulated.

In this section, RN will denote the aﬃne euclidian space of dimension N with the topology
ﬁxed with the euclidian distance.
Let v0, v1, . . . , vn be points of RN . These are aﬃnely independent if the vectors v1 −
v0, . . . , vn−v0 are linearly independent. Equivalently, these points are aﬃnely independent
if there is no aﬃne subvariety of RN of dimension less than n where the points lie. In this
case, every point of the generated aﬃne subvariety allows a unique expression represented

by x = λ0v0 + . . . + λnvn, where λi ∈ R verify n∑

i=0 λi = 1

Deﬁnition 3.7 (Simplex). Let N > 0 and v0, v1, . . . , vn, with n ≥ 0, n + 1 aﬃnely
independent points of RN . A n-dimensional simplex of vertices v0, . . . , vn is a subset
∆(v0, . . . , vn) of RN deﬁned by

∆(v0, . . . , vn) = {x ∈ RN | x =
 n∑

i=0 λivi,
 n∑

i=0 λi = 1 , λi ≥ 0, i = 0, . . . , n}.

When referring to a simplex of dimension n we will use the expression n-simplex. Thus,
0-simplices are points, 1-simplices are segments, 2-simplices are triangles, etc., as shown
in Figure 3.9.

Lemma 3.8. 1. Every simplex is a compact, connected, locally path-connected and con-
tractible space.
2. Any two n-dimensional simplices are homeomorphic.

3.3 Previous tools 19

Figure 3.9: Example of 0-simplex, 1-simplex, 2-simplex and 3-simplex

Deﬁnition 3.9. Let ∆(v0, . . . , vn) be an n-simplex and k ≥ 0. We call k-dimensional
faces of ∆(v0, . . . , vn) the simplices
∆(vi0, vi1, . . . , vik ),

where 0 ≤ i0 < . . . < ik ≤ n.

If we delete one of the n + 1 vertices of an n-simplex ∆(v0, . . . , vn), then the remaining n
vertices span an (n − 1)-simplex which is a face of ∆(v0, . . . , vn). We adopt the following
convention: The vertices of a face, or of any subsimplex spanned by a subset of the
vertices, will always be ordered according to their order in the largest simplex.

Deﬁnition 3.10. A simplicial complex is a ﬁnite set of simplices of RN , K = {σ1, σ2, . . . , σn},
such that

1. If σi is a simplex of K, then all the faces of σi belong to K.

2. If σi and σj are simplices of K, then σi ∩ σj = ∅ or σi ∩ σj is a face of σi and σj.

Deﬁnition 3.11. Given a simplicial complex K, the simplicial polyhedron associated to
K, and denoted by |K|, is the subspace of RN deﬁned by the reunion of all the simplices
of K: |K| = ∪σi∈Kσi.

The simplicial polyhedrons are topological spaces. This fact will allow us to relate both
homologies (the simplicial and the singular one) on the polyhedrons.
If K is a simplicial complex, the simplices σi ∈ K are the faces of K and K is a triangu-
lation of |K|.

Deﬁnition 3.12. Let K be an ordered simplicial complex. For every p ≥ 0, it is called
group of p-dimensional chains of K, and is denoted by Cp(K), the free abelian group
generated by the set of p-dimensional ordered faces. In other words, the group of p-
dimensional chains is Cp(K) := ⊕Z[σ],

where the direct sum extents to the set of p-dimensional ordered faces.

If p > dimK, then Cp(K) = 0.

The p-dimensional chains can be written as ﬁnite formal sums ∑
i kiσi, where ki ∈ Z are
coeﬃcients. Such a sum can be thought of as a ﬁnite collection (or “chain”) of p-simplices
in K with integer multiplicities.

20 Square Peg Problem

For instance, in the case of a 2-simplex [v0, v1, v2], it has associated the ordered sim-
plicial complex formed by the 2-dimensional face [v0, v1, v2], the 1-dimensional faces
[v0, v1], [v0, v2], [v1, v2] and the 0-dimensional faces [v0], [v1], [v2]. Then, we would have:

C0(∆) = Z[v0] ⊕ Z[v1] ⊕ Z[v2] ∼= Z
3,

C1(∆) = Z[v0, v1] ⊕ Z[v0, v2] ⊕ Z[v1, v2] ∼= Z
3,

C2(∆) = Z[v0, v1, v2] ∼= Z.

As we can see in Figure 3.10, the boundary of a n-simplex [v0, . . . , vn] consists of the
various (n − 1)-dimensional simplices [v0, . . . , ̂vi, . . . , vn] (where the hat over ̂vi indicates
that this vertex is removed from the sequence v0, . . . , vn). In terms of chains, we would
like to say that the boundary of [v0, . . . , vn] is the (n − 1)-chain formed by the sum of
the faces [v0, . . . , ̂vi, . . . , vn]. However, it turns out to be better to insert certain signs
and let the boundary of [v0, . . . , vn] be ∑
i(−1)i[v0, . . . , ̂vi, . . . , vn]. This is because the
signs will take the orientation into account, so that all faces of the simplex are oriented.
The “boundary operator”, which we will deﬁne below, is the algebraic version of this
geometrical concept.

Figure 3.10: Examples of the boundary operator

Deﬁnition 3.13. Let K be an ordered simplicial complex. For every p ≥ 1, the boundary
operator ∂p : Cp(K) −→ Cp−1(K) is the morphism of abelian groups deﬁned by

∂p[vi0, . . . , vip] =
 p∑

k=0(−1)
k[vi0, . . . , ̂vik , . . . , vip],

where [vi0, . . . , ̂vik , . . . , vip] denotes the ordered (p − 1)-simplex obtained when we delete
the vertex vik . For p = 0, we deﬁne ∂0 = 0.

As we can see in Figure 3.10, for the case of a 1-simplex [v0, v1] we would have ∂1[v0, v1] =
[v1] − [v0]. Also, for the case of the 2-simplex [v0, v1, v2], we would have

∂2[v0, v1, v2] = [v1, v2] − [v0, v2] + [v0, v1].

This, in fact, gives us the simplex ordered.

In the following proposition we introduce an important property of the boundary operator.
This fact will be applied in the demonstration of Stromquist.

3.3 Previous tools 21

Proposition 3.14. Let K be an ordered simplicial complex. The composition

Cp+1(K) ∂p+1
−−−→ Cp(K) ∂p
−→ Cp−1(K)

is null for every p ≥ 1, i.e., ∂2 = 0.

We are now ready to deﬁne the simplicial homology group, which is our main object of
study in this section.

Deﬁnition 3.15. Let K be a simplicial complex. For every p ≥ 0, the pth simplicial
homology group of K is deﬁned as the quotient group

Hp(K) := Zp(K)/Bp(K),

where Zp(K) := ker (∂p : Cp(K) −→ Cp−1(K))

is the group of p-dimensional cycles of K and

Bp(K) := im (∂p+1 : Cp+1(K) −→ Cp(K))

is the group of p-dimensional boundaries.

Notice that Hp(K) = 0 if p > dimK.

The simplicial homology is only applied to one class of topological spaces: the polyhe-
drons. However, the singular homology is deﬁned for every topological space, is functorial
regarding continuous maps and matches with the simplicial homology on polyhedrons.
Everything described above can be applied equally to singular simplices.

Let ∆p denote a p-simplex, where p ≥ 0 is an integer.

Deﬁnition 3.16. Let X be a topological space. A singular p-simplex of X is a continuous
map σ : ∆p −→ X.

Deﬁnition 3.17. Let X be a topological space. The group of singular p-dimensional
chains of X, denoted by Sp(X), is the free abelian group generated by the singular p-
simplices of X:
 Sp(X) = {
 r∑

i=1 λiσi; λi ∈ Z, σi : ∆
p −→ X continuous}.

The boundary operator is introduced as ∂p : Sp(X) −→ Sp−1(X) and it is deﬁned by

∂p(σ) =
 p∑

i=0(−1)
iσ ◦ δi,

where δi : ∆p−1 −→ ∆p, 0 ≤ i ≤ p, is the continuous map deﬁned by

δi(x0, x1, . . . , xp−1) = (x0, x1, . . . , xi−1, 0, xi, . . . , xp−1).

22 Square Peg Problem

So we can deﬁne the singular homology group by

Hp(X) = Ker ∂p/Im ∂p+1.

Proposition 3.18. Let X, Y be topological spaces and f : X −→ Y a continuous map.
Then f induces a morphism of complexes

S∗(f ) : S∗(X) −→ S∗(Y )

such that Sp(f )(σ) = f ◦ σ,

for every singular p-simplex σ of X.

Now that we have translated all the simplicial properties to the singular ﬁeld, it is time
to introduce the functoriality of the singular homology, where Top will represent the
category of topological spaces and Ab the category of abelian groups:

Proposition 3.19. Let X, Y be topological spaces and f : X −→ Y a continuous map.
Then, the morphism S∗(f ) induces a group morphism

H∗(f ) : H∗(X) −→ H∗(Y )

such that, if [c] is a cycle of X, then H∗(f )([c]) = [S∗(f )(c)].
If f = idX , then H∗(idX ) = idH∗(X),

and, if g : Y −→ Z is another continuous map, then

H∗(g ◦ f ) = H∗(g) ◦ H∗(f ).

Thus, H∗ deﬁnes a functor H∗ : Top −→ Ab∗.

From this functoriality it immediately follows the topological invariance of the singular
homology:

Theorem 3.20 (Topological invariance). Let X, Y be topological spaces and f : X −→ Y
a homeomorphism. Then, the morphism

H∗(f ) : H∗(X) −→ H∗(Y )

is an isomorphism.

We also have that singular homology is invariant under homotopy. Recall that, given
two topological spaces X and Y , they are of the same homotopy type if there exists
f : X −→ Y and g : Y −→ X continuous such that the compositions f ◦ g and g ◦ f are
homotopic to the corresponding identities: f ◦ g ≃ idY , g ◦ f ≃ idX .

3.4 Walter Stromquist’s proof 23

Theorem 3.21 (Homotopic invariance). Let X, Y be topological spaces and f, g : X −→ Y
continuous maps. Then, if f is homotopic to g,

H∗(f ) = H∗(g) : H∗(X) −→ H∗(Y ).

As an immediate consequence of this result, we get:

Corollary 3.22. Let X and Y be topological spaces of the same type of homotopy. Then,
the groups of singular homology of X and Y are isomorphic, i.e., H∗(X) ∼= H∗(Y ).

We have seen the basic properties of simplicial and singular homology required for Strom-
quist’s proof. We need a ﬁnal step to relate both homologies. We show that these
properties allow us to compare the simplicial homology of a polyhedron to its singular
homology.

Let K be an ordered simplicial complex and V = {v1, v2, . . . , vr} its vertices. Let C∗(K)
be the complex of simplicial chains of K. The polyhedron |K| associated to the complex
K is a topological space and, hence, we can consider the complex of singular chains of
|K|: S∗(|K|).

If s is an ordered p-dimensional simplicial face of K, s = [vi0, . . . , vip], s deﬁnes a singular
simplex p-dimensional σ = (vi0, . . . , vip). Then, we have the map

ν : C∗(K) −→ S∗(|K|)

s ↦−→ σ

Lemma 3.23. The morphism ν is a morphism of complexes, natural in K.

Therefore, ν induces a morphism in the respective homologies

H∗(ν) : H∗(C∗(K)) −→ H∗(S∗(|K|)),

that is, we have the morphism
H∗(ν) : H∗(K) −→ H∗(|K|)

from the simplicial homology of the simplicial complex K to the singular homology of the
topologic space |K|.

3.4 Walter Stromquist’s proof

In this section we present Walter Stromquist’s result, which is titled Inscribed squares and
square-like quadrilaterals in closed curves. We will provide some extra annotations to his
original proof.

In this proof, we use the term smooth to refer to a curve which has a continuous turning
tangent, i.e., which is C1. We will show that for every smooth curve in Rn, there is a
quadrilateral with equal sides and equal diagonals whose vertices lie on the curve. In the
case of a smooth plane curve, the quadrilateral corresponds to a square.

We will give a weaker smoothness condition which will still satisfy the existence of an
inscribed square for curves that are convex, polygon or piecewise of class C1 (with certain
restrictions that we will state later).

24 Square Peg Problem

Deﬁnitions and necessary tools Let us begin with some initial deﬁnitions. A simple
closed curve is a continuous function w : R −→ Rn which satisﬁes w(x) = w(y) if, and
only if, x − y is an integer, where w is determined by its values in [0, 1]. This can also
be seen as an injective continuous map S1 −→ Rn where, if n = 2, it is a Jordan curve.
Henceforth, “curve” will mean simple closed curve.

The curve w is smooth if it has a continuous non-vanishing derivative. Any curve with
a continuously turning tangent can be parameterized so as to be smooth in this sense.

A quadrilateral is inscribed in the curve w if all of its vertices lie on w. In the case of
Rn, a quadrilateral may be inscribed even if its sides do not lie in the interior of the curve.

We shall introduce some required tools before getting into the ﬁrst lemma. We will work
with a simplex Q, which will represent the set of quadrilaterals inscribed in w. That is,
all possible geometric elements inscribed in w that could be the square we want. We will
also work with four subsets Q1, Q2, Q3, Q4 that will cover our Q and whose intersection
will correspond to a set of inscribed rhombuses (we will see the deﬁnition of rhombus at
the end of this section). This set is going to be our main object of study, as we will see
later.

Denote by Q the set

Q = {(x1, x2, x3, x4) ∈ R4 | 0 ≤ x1 ≤ x2 ≤ x3 ≤ x4 ≤ 1}.

This is a 4-simplex with vertices
 v0 = (1, 1, 1, 1),

v1 = (0, 1, 1, 1),

v2 = (0, 0, 1, 1),

v3 = (0, 0, 0, 1),

v4 = (0, 0, 0, 0),

and faces F0, . . . , F4 numbered so that each Fi is opposite vi. Each face Fi is generated
by all the vertices stated above except for vi. For instance, the face F0 is formed by
v1, v2, v3, v4.
We will use the notation x to represent an element (x1, x2, x3, x4) of Q.

In Figure 3.11 we illustrate the simplex Q. Since it is a 4-dimensional object, it is diﬃcult
to represent. Let us note some details to clarify the form of our Q. Each face Fi is a
tetrahedron, since it is a 3-simplex. However, notice that in Figure 3.11 we have not
drawn F0 and F4 as tetrahedrons. Also, the face F0 ∩ F4 is a 2-simplex, which means that
it is actually a triangle. But in our illustration we have represented it as a line segment
(the right edge of the ﬁgure).

Given a curve w, we associate with each point x ∈ Q an inscribed quadrilateral with
vertices w(x1), w(x2), w(x3), w(x4). That is, we identify the points of Q with the cor-
responding geometric ﬁgures on w and refer to points of Q as quadrilaterals. Thus, Q
represents the set of quadrilaterals inscribed in w.

3.4 Walter Stromquist’s proof 25

Figure 3.11: The simplex Q of quadrilaterals

The vertices of each quadrilateral have the same cyclic order in the quadrilateral as in
w. Some of these quadrilaterals are degenerate (have one or more sides of zero length),
and some of the degenerate quadrilaterals are one-point quadrilaterals (all four sides have
zero length). That is, the possibility x1 = x2 = x3 = x4 is not excluded.

Let us mention an important fact about the faces F0 and F4. You can think of F0 as
quadrilaterals with the vertex w(0) ﬁxed, while F4 is the face where quadrilaterals have
vertex w(1) ﬁxed. Thus, both faces are morally the same since w(0) = w(1) (by deﬁnition
of simple closed curve). In other words, if we deﬁne h : F0 −→ F4 by

h(0, x, y, z) = (x, y, z, 1),

then h(x) represents the same quadrilateral as x but with the vertices numbered diﬀer-
ently. Hence, the points of F4 represent the same quadrilaterals as the points of F0.

Now, for each i = 1, 2, 3, 4, we deﬁne

si(x) = ∥ w(xi+1) − w(xi) ∥

as the length of the i-th side of the quadrilateral corresponding to x. For the case
i = 4, xi+1 becomes x1. Each si is a continuous function on Q.

For each i, we deﬁne Qi to be the closure of the set

{x ∈ Q
0 | si(x) = max
j sj(x)}.

Here Q0 denotes the interior of Q. Qi is the set of quadrilaterals whose i-th side is their
longest side, except that a quadrilateral in ∂Q is included in Qi only if it is the limit of
quadrilaterals in Q0 with the same property.
Each Qi is still closed and we still have ⋃
i Qi = Q. The purpose of this device is to prevent
one-point quadrilaterals from being elements of every Qi, as we will need afterwards.
But the device works perfectly only if the curve is suﬃciently smooth. We will see this
smoothness requirement later.

26 Square Peg Problem

Now we will introduce a lemma that requires w to be smooth. We are going to prove its
stronger version later (see Lemma 3.30), as well as specify the smoothness condition that
we will apply.

We will work as it follows: ﬁrst we will prove the Square Peg Problem for curves that
satisfy the following Lemma 3.24, i.e., which are smooth. Once we have this proof, we
will introduce a new smoothness condition called “Condition A” that will still guarantee
this Lemma 3.24 and, hence, the proof of the Square Peg Problem will still be implied.
Therefore, the following lemma is a tool to be able to prove the Square Peg Problem later
for this so called “Condition A”. Let us ﬁrst introduce it and then explain its meaning.

Lemma 3.24. If w is a smooth curve, then each one-point quadrilateral is contained in
only one set Qi. In particular, vi ∈ Qi for i = 1, 2, 3 and x ∈ Q4 for each x on the edge
connecting v0 and v4.

In order to understand better the above lemma, we will explain it more precisely. The
vertices v0, v1, v2, v3, v4 are one-point quadrilaterals. This is because w(0) = w(1), by
deﬁnition of w, and hence for each vi we have s1 = s2 = s3 = s4 = 0, where i = 0, 1, 2, 3, 4.
Then, we will have that v1 ∈ Q1, v2 ∈ Q2, v3 ∈ Q3, whereas v0, v4 and the whole edge
between them will be in Q4 (this fact will be proven in the stronger version of the lemma).
So, why do we consider the case of the edge connecting v0 and v4 diﬀerently?

Since v0 = (1, 1, 1, 1) and v4 = (0, 0, 0, 0), all points placed on this edge are represented by
(λ, λ, λ, λ), where λ ∈ [0, 1]. Therefore, all their associated quadrilaterals are one-point
quadrilaterals. This does not occur on the other edges of Q. For instance, the points on
the edge connecting v3 = (0, 0, 0, 1) and v4 are represented by the quadruple (0, 0, 0, λ).
These correspond to quadrilaterals with only one side with no zero length (except for the
limit cases where λ = 0 or λ = 1). It works similarly for the edges between the other
vertices.

Therefore, all points settled on the edges joining our ﬁve vertices (excluding the vertices
themselves) represent quadrilaterals with three sides of zero length, except for the case of
the edge linking v0 and v4, where they are associated to one-point quadrilaterals.

Furthermore, we can take a look at the points on the faces of Q. The points situated on
the 2-simplices are associated to a quadrilateral with one side of zero length. For example,
the points in F0 ∩ F4 are represented by (0, µ, λ, 1), where µ, λ ∈ [0, 1], and since our curve
w is closed (w(0) = w(1)), two of its vertices are associated implying that its quadrilateral
is degenerate (has one side of zero length).

Also, the points found on faces F1, F2 and F3 are, as well, degenerate quadrilaterals with
one of their sides with length equal to zero. But, points situated in the interior of F0 and
F4 might be non degenerate quadrilaterals. In the case of F0, its points are represented by
(0, λ, µ, γ) and for F4 we have (λ, µ, γ, 1), where λ, µ, γ ∈ [0, 1]. Both of them with one of
its vertices ﬁxed (w(0) and w(1) respectively). Therefore, their points are non degenerate
unless λ = µ, λ = γ or µ = γ.

We intend to avoid all of the degenerate cases, so we can proof the existence of a quadri-
lateral with equal sides and equal diagonals. This is why we will work with faces F0 and
F4, where their points are generically non degenerate quadrilaterals.

3.4 Walter Stromquist’s proof 27

For i = 1, 2, 3 notice that Qi includes vi but does not intersect the opposite face Fi (where
si(x) = 0). For instance, v1 ∈ Q1, but the points of F1 are represented by (λ, λ, µ, γ),
λ, µ, γ ∈ [0, 1]. Then s1 = ∥w(λ) − w(λ)∥ = 0, which means that s1 is not the largest
side of any associated quadrilateral in F1. The case of i = 4 is diﬀerent: Q4 includes the
entire segment from v0 to v4, and avoids the opposite 2-simplex F0 ∩ F4.

The smoothness of w is only required for this lemma. Henceforth, we assume that w is
any curve for which the result of Lemma 3.24 is valid.

Now let R = ⋂i Qi. Since we deﬁned Qi as the set of quadrilaterals whose i-th side is
their longest side and R as the intersection of all Qi, then R corresponds to the set of
those quadrilaterals which have all four sides with the same value. We call a point x ∈ R
a rhombus. Thus, a rhombus corresponds to an inscribed quadrilateral whose sides are
equal and nonzero (we made sure that each one-point quadrilateral can only be in one
Qi). A square-like quadrilateral is a rhombus which satisﬁes

d13(x) = d24(x)

where d13(x) = ∥w(x3) − w(x1)∥

and d24(x) = ∥w(x4) − w(x2)∥.

In other words, a square-like quadrilateral is an inscribed quadrilateral with equal sides
and equal diagonals. In R2, a square-like quadrilateral is an inscribed square, but we use
the term rhombus to include equilateral quadrilaterals which do not lie in a plane.

A thin rhombus is one which satisﬁes d13 ≥ d24, and a fat rhombus is one such that
d13 ≤ d24. A rhombus which is both thin and fat is a square-like quadrilateral.

Denote by RT HIN and RF AT the subsets of R consisting of thin and fat rhombuses
respectively. Then, R = RT HIN ∪ RF AT . Note that if x ∈ F0 is a rhombus, then so is
h(x). But if x is thin, then h(x) is fat and vice versa.

Before continuing, let us make a quick overview of the general strategy. So far we have
seen the deﬁnitions and tools required to set the problem we would like to solve. Our
strategy will consist on studying the set of rhombuses in Q, and especially the rhombuses
on F0 and F4. We will show that there must be, in a sense, an odd number of rhombuses in
F0. Notice that if we proved that the number of rhombuses is even, we would not discard
the case of a zero number of rhombuses. Therefore, we need to see that the number is
odd.

Moreover, if the number of thin rhombuses on F0 is even, for instance, then the number
of fat rhombuses on this face must be odd. The correspondence based on the function h
shows that these parities must be reversed on F4. But we will also show that the parities
can not be reversed - in eﬀect because the bottom face can be lifted continuously up
through Q onto the top face - unless RT HIN and RF AT intersect.

To prove all of this we will need some machinery from homology theory.

28 Square Peg Problem

The degree of a set of rhombuses In this part of the section we will deﬁne the
concept of the degree of a subset K of a simplex, given a cover of the simplex by closed
sets. In the next part, our K will be a set of rhombuses, and the degree will be our way
of counting the rhombuses modulo 2. Additionally, all homology groups will be simplicial
homology groups with coeﬃcients in Z2.

Let A be an n-simplex. We will use the notations vi and Fi for the vertices and faces of
A respectively. A cover of closed vertex neighborhoods in A, or simply a cover, is a
family of closed subsets A0, . . . , An of A such that vi ∈ Ai but Fi ∩ Ai = ∅ for each i, and
such that ⋃i Ai = A. This cover is denoted as {Ai}. We are going to show that ⋂ Ai is
nonempty and that, in a certain well deﬁned sense, it is odd.

Let {Ai} be a cover. Let K be any subset of ⋂ Ai which is both open and closed relative
to ⋂ Ai. We include the possibilities K = ∅ and K = ⋂ Ai. In other words, we take K as
a connected component of ⋂ Ai and we want to deﬁne the degree of the cover {Ai} around
our K. This degree is an element of Z2; in eﬀect it tells whether we should consider K
to be even or odd.

A reversing map for the cover {Ai} is a function

f : (A − ⋂ Ai) −→ ∂A

which maps each set Ai into the opposite face Fi; that is, f (Ai) ⊆ Fi for each i. We see
this fact more precisely once we deﬁne our f . Let us show that a reversing map always
exists. For each i, let d(x, Ai) denote the distance from x to Ai and deﬁne f by

f (x) = ∑

i
 d(x, Ai)
∑
j d(x, Aj) vi.

The sum ∑j d(x, Aj) normalises each coeﬃcient, since it is the sum of all distances from
x to each Ai, for i = 0, . . . , n. Notice that we can not have the case where all distances
have zero value, since no x is in the intersection ⋂ Ai.
Given a k, if x belongs to Ak, then
 d(x, Ak) = 0.

Therefore we would get a lineal combination with all vertices except the vertex vk, which
implies that f (x) is in Fk (face which does not have vk). Thus, each x is sent to the
opposite face of the subset where it belongs.

Normalising the coeﬃcients ensures that the image is restricted to that speciﬁc boundary;
it gives f (x) as a convex combination of the vertices vi so that f (x) ∈ A.

Now let L = ⋂ Ai − K. Triangulate A ﬁnely enough that no simplex of the triangulation
touches both K and L. Let Γ be the n-chain consisting of the n-simplices which touch
K. We triangulated A such that only one face of each n-simplex touches K. A face of an
n-simplex is an (n − 1)-simplex. Then, the boundary of Γ represents an homology class
γ ∈ Hn−1(A − ⋂ Ai). The (n − 1)-dimension is due to the faces of the n-simplices touching
K; and it is an homology of A − ⋂ Ai because the n-simplices only touch K with one

3.4 Walter Stromquist’s proof 29

of their faces. Therefore, the boundary of Γ consists of the n-simplices (contained in A)
without the faces that do not touch K (which are in the set ⋂ Ai since ⋂ Ai = L ∪ K).
We denote this class by γK. It is the unique homology class that surrounds all of K but
none of L.

The degree of {Ai} around K is deﬁned as the image f∗(γK) in Hn−1(∂A), where f is
any reversing map for {Ai}. The group Hn−1(∂A) can be identiﬁed with Z2, and we will
regard the degree to be an element of Z2. Its value is independent of the choices made
in the above construction. We will denote it by deg{Ai}K or, when the cover is identiﬁed
by context, by degK.

In particular, suppose B is any simplex and f : A − ⋂ Ai −→ ∂B is any function which
maps each Ai into a diﬀerent face of B. Then the degree of K could just as well have
been deﬁned as f∗(γK) in Hn−1(∂B), since there is an isomorphism g : B −→ A which
makes gf a reversing map, and (gf )∗(γK) = f∗(γK) (both being regarded as elements of
Z2). In this case we say that f is “isomorphic to a reversing map”.

We can collect some facts about these degrees. If K = ∅, then γK = 0 (the zero element
of Hn−1(A − ⋂ Ai)). If K is the disjoint union of open and closed subsets K1 and K2,
then γK = γK1 + γK2. Therefore we have the following lemmas:

Lemma 3.25. deg ∅ = 0.

Lemma 3.26. If K = K1 ∪ K2, then degK = degK1 + degK2.

Lemma 3.27. deg(
⋂ Ai) = 1.

In other words, Lemma 3.27 tells us that the degree of ⋂ Ai is odd, as we wanted to show.
Let us see its proof.

Proof (Lemma 6). Let Sn−1 denote the (n − 1)-sphere, and let g : Sn−1 −→ Sn−1 be
any continuous map without ﬁxed points. We see that a map that has no ﬁxed points is
homotopic to the antipodal map of Sn−1:

Let a : Sn−1 −→ Sn−1 be the antipodal map of the sphere. Since g has no ﬁxed points,
we have that g(x) ̸= x, for x ∈ Sn−1. We denote by O the center of the sphere. We
know that the segment [a(x), x], for x ∈ Sn−1, passes through the center O. This implies
that the segment [a(x), g(x)] does not pass through O (using that g(x) ̸= x). Thus,
tg(x) + (1 − t)a(x) does not pass through O either, for t ∈ [0, 1], implying that it cannot
be equal to zero. Taking into account this result, we can deﬁne an homotopy

H : I × Sn−1 −→ Sn−1

(t, x) ↦−→ tg(x) + (1 − t)a(x)
||tg(x) + (1 − t)a(x|| .

This is continuous and, therefore, well-deﬁned.

30 Square Peg Problem

Then we have that g is homotopic to the antipodal map, as we wanted to show. This
implies that g and a generate the same map in homology; that is, g∗ = a∗. But a is an
homeomorphism of the sphere; and so g∗ : Hn−1(Sn−1) −→ Hn−1(Sn−1) is the identity
map. Now, since A is an n-simplex, ∂A is homeomorphic to Sn−1 and any reversing map
f restricts to a function ∂A −→ ∂A without ﬁxed points, so f induces the identity map
on Hn−1(∂A) = Z2. Looking at ∂A itself as a representative of the homology class that
generates Hn−1(∂A), we can conclude that f∗(∂A) = 1. But ∂A surrounds ⋂ Ai, and so
represents γ∩Ai. Therefore f∗(γ∩Ai) = 1, which proves the lemma.

The main result We are now ready to return to the problem of searching for a square-
like quadrilateral in the simplex Q.

In Lemma 3.24 we saw that if w is smooth, then each one-point quadrilateral is in a
diﬀerent Qi. Here we are going to prove the Square Peg Problem for the case of w being
smooth, and hence for the curves that satisfy Lemma 3.24.

Theorem 3.28. If w is a smooth curve, then w admits an inscribed quadrilateral with
equal sides and equal diagonals.

Proof. Let Q, R and their subsets be as before. We will suppose that there is no square-
like quadrilateral in Q. Then, R can be written as a disjoint union R = RT HIN ⊔ RF AT .
The face F0 is a simplex, and it has a cover {F0 ∩ Qi} of closed vertex neighborhoods for
i = 1, 2, 3, 4 (each Qi includes vi, this is why we can build this cover with the family of
closed subsets F0 ∩ Q1, F0 ∩ Q2, F0 ∩ Q3 and F0 ∩ Q4). Since R = ⋂i Qi, the intersection
of the above sets in the cover is

F0 ∩ R = (F0 ∩ RT HIN ) ⊔ (F0 ∩ RF AT ).

From Lemma 3.26 and Lemma 3.27 we have

deg(F0 ∩ RT HIN ) + deg(F0 ∩ RF AT ) = deg(F0 ∩ R) = 1,

from which we deduce that

deg(F0 ∩ RT HIN ) ̸= deg(F0 ∩ RF AT ). (3.1)

We will obtain a contradiction by showing that each side of (3.1) is equal to deg(F4 ∩
RT HIN ), which is measured in the simplex F4. Notice that this idea is reasonable, since
deg(F0 ∩ RF AT ) and deg(F4 ∩ RT HIN ) should be equal because the quadrilaterals on both
faces are the same but with the vertices numbered diﬀerently and deg(F0 ∩ RT HIN ) =
deg(F4 ∩ RT HIN ) should also occur since the degree of RT HIN must change continuously
from one face to the other (as we will prove afterwards).

The map h : F0 −→ F4 is not only an homeomorphism of the faces, it is also an iso-
morphism of the covers {F0 ∩ Qi} and {F4 ∩ Qi}. As we have mentioned, h will change
F0 ∩ RF AT into F4 ∩ RT HIN because they are the same quadrilaterals but with the order
of the vertices changed. Which means that the longest diagonal of one rhombus (d24 for

3.4 Walter Stromquist’s proof 31

the fat rhombus) will become the shortest one, while the originally shortest diagonal will
play the role of the new longest diagonal (d13). Thus,

deg{F0∩Qi}(F0 ∩ RF AT ) = deg{F4∩Qi}(h(F0 ∩ RF AT )) = deg{F4∩Qi}(F4 ∩ RT HIN ).

That takes care of the right side of (3.1).

Let us prove the left side of (3.1) by showing that deg(F0 ∩ RT HIN ) = deg(F4 ∩ RT HIN ).
We claim that degRT HIN is the same whether it is measured in F0 or in F4. Intuitively,
this is true because the degree of RT HIN must change continuously (i.e., remain constant)
as we progress smoothly up through slices of Q from the bottom face to the top face of
the simplex. Making this arguments precisely takes some work.
Construct f : (Q − R) −→ ∂F0 as follows:

d(x, Qi) = distance from x to Qi;

f (x) =
 4∑

i=1
 d(x, Qi)
∑
j d(x, Qj) vi.

Then f maps each Qi into the face F0 ∩Fi of F0. Therefore f restricted to F0 is a reversing
map for the cover {F0 ∩ Qi}, and also f restricted to F4 is isomorphic to a reversing map
for the cover {F4 ∩ Qi}.

Triangulate Q ﬁnely enough that no simplex touches both RT HIN and RF AT , and let
∆ be the 4-chain consisting of simplices of the triangulation which touch RT HIN . Now
∂∆ is a 3-chain in (Q − R). Let Γ be the 3-chain consisting of those simplices in ∂∆
which are not contained in F0 or F4. In the simplest cases, Γ can be thought of as a tube
surrounding RT HIN , and with its ends abutting F0 and F4, as in the ﬁgure shown below.
More generally, Γ may consist of many tubes and more complicated shapes.

Figure 3.12: Simplest case of Γ

Now the boundary ∂Γ is a 2-chain which must represent the zero element of H2(Q − R).
This is because ∂Γ is the boundary of the boundary, and by homology this is zero. There-
fore f∗(∂Γ) = 0 ∈ H2(F0). But ∂Γ contains two components: one surrounds (RT HIN ∩F0)
in F0, and one surrounds (RT HIN ∩ F4) in F4. We have:

0 = f∗(∂Γ) = f∗(∂Γ ∩ F0) + f∗(∂Γ ∩ F4);

32 Square Peg Problem

so
 f∗(∂Γ ∩ F0) = f∗(∂Γ ∩ F4) (3.2)

But the left side of (3.2) measures the degree of RT HIN ∩ F0, and the right side measures
the degree of RT HIN ∩F4. Therefore, these two degrees are equal, completing the promised
contradiction and establishing the theorem.

The smoothness requirement. So far we have proved the Square Peg Problem for
curves that are smooth which satisfy Lemma 3.24. In this part we give a weaker hypoth-
esis: Condition A. It is suﬃcient for Lemma 3.24. and, therefore, for the existence of an
inscribed square or square-like quadrilateral. Smooth curves satisfy it, and so do polygons
with only obtuse angles (corners where the curve changes direction by less than 90◦). We
will talk about chords. A chord is a line segment joining two points of w.

Deﬁnition 3.29. A curve w satisﬁes Condition A if each point w(y) of the curve has a
neighborhood U (y) in Rn such that no two chords in U (y) are perpendicular.

This deﬁnition is purely geometric: it depends only on the image Im w and not on the
parameterization. An equivalent deﬁnition, intuitively, is that each point of the curve has
a neighborhood (in the curve) in which any two chords (oriented in the direction of the
curve) diﬀer in direction by less than 90◦. More precisely, we have the following: if w
satisﬁes Condition A, then each y ∈ R has a neighborhood (y − µ, y + µ) such that, if
x1, x2, x3, x4 ∈ (y − µ, y + µ) with x1 < x2 and x3 < x4, then

(w(x2) − w(x1)) · (w(x4) − w(x3)) > 0.

The periodicity of w and the compactness of [0, 1] insure that µ can be chosen indepen-
dently of y.

As we have mentioned, this condition is satisﬁed for smooth curves and polygons with all
their angles being obtuse:
Any point w(y) situated on a smooth curve w will always have a suﬃciently small neigh-
borhood U (y) in which all the chords will form an angle > 90◦. In Figure 3.13 we can
see that, although it may seem that the chords will be perpendicular in an speciﬁc neigh-
borhood, we can choose an even smaller neighborhood where no two chords will diﬀer in
direction by less than 90◦.

Figure 3.13: Smooth curves satisfy Condition A

3.4 Walter Stromquist’s proof 33

For the case of polygons, we ask them to have all their angles obtuse. In Figure 3.14 we
have an example of a polygon with an angle of < 90◦. In this case, although we choose a
small neighborhood in this corner, we will always have at least two chords that form the
same angle of the polygon’s angle. And, since this is < 90◦, we will not have Condition
A satisﬁed. On the other hand, if our polygon had all their angles obtuse, there would
always be a neighborhood where the chords form, at least, the same angle as the respective
obtuse angle. Thus, Condition A would be satisﬁed.

Figure 3.14: Polygons with a non obtuse angle do not satisfy Condition A

Now, let us introduce Lemma 3.24 for curves that satisfy Condition A. If we prove that
curves with this weaker smoothness condition satisfy 3.24, then this will imply that they
admit an inscribed square, as shown in Theorem 3.28.

Lemma 3.30. If w satisﬁes Condition A, then each one-point quadrilateral in Q is con-
tained in exactly one set Qi. In particular, vi ∈ Qi for i = 1, 2, 3 and y ∈ Q4 for each y
on the edge connecting v0 and v4.

Proof. Let y = (y, y, y, y) be a one-point quadrilateral on the edge from v0 to v4. We shall
show that y has a neighborhood in Q such that, for any x in the neighborhood which is
also in Q0, the fourth side of x is the unique longest side. This will imply that y is in
Q4, but not in any other Qi.

Let µ be as above. The required neighborhood of y consists of those elements x ∈ Q
whose coordinates x1, . . . , x4 are in (y−µ, y+µ). Let x be an element of this neighborhood
which is also in Q0. Therefore we have 0 < x1 < . . . < x4 < 1. Let z1, z2, z3, z4 be vectors
in Rn representing the sides of the quadrilateral x. We have z1 = w(xi+1) − w(xi) for
i = 1, 2, 3 and z4 = w(x4) − w(x1). We will show that z4 is the longest of these sides. Let
us see, for instance, that z4 > z2. We have

z4 = z1 + z2 + z3,

so z4 · z2 = z1 · z2 + z2 · z2 + z3 · z2,

and since all of these dot products are positive, in particular we have

z4 · z2 > z2 · z2.

34 Square Peg Problem

But if z4 has a larger component in the direction of z2 than z2 itself does, then the fourth
side must be strictly longer that the second side. Similarly, the fourth side is longer than
the ﬁrst and the third sides. Since the fourth side is the unique longest side, x is in Q4
and no other Qi’s. Then, if it is true for every x ∈ Q0 suﬃciently near y, it is also true
for y itself.

This proof, taken literally, works for v0 and v4. The cases of v1, v2 and v3 require more
delicacy in their statement, but are essentially similar.

Lemma 3.30 implies the following improvement of Theorem 3.28:

Theorem 3.31. If w satisﬁes Condition A, then w admits an inscribed quadrilateral with
equal sides and equal diagonals.

Locally monotone curves in R2. In this part we deﬁne a much less restrictive smooth-
ness condition: local monotonicity. We will see that this condition still guarantees the
existence of an inscribed square. Smooth curves, convex curves polygons, and most piece-
wise C1 curves satisfy this condition. This is, therefore, the strongest result provided by
Stromquist.

Let us begin by deﬁning this smoothness condition and all the previous deﬁnitions required
to understand it.

Deﬁnition 3.32. A segment of a curve w corresponding to an interval (a, b) is the
restriction of the function to that interval. That is: w|(a,b).

We call (b − a) the length of the segment. This length is measured in parameter space
and not in R2.

Deﬁnition 3.33. The segment is monotone in the direction u (where u is a non-zero
vector in R2) if the dot product w(x)·u is a strictly increasing function of x, for x ∈ (a, b).

We can think of this as the orthogonal projection of w(x) onto u. Notice that if u was a
unit vector, we would have w(x) · u = ∥w(x)∥ · ∥u∥ = cos α, where α is the angle formed
by w(x) and u.
 Figure 3.15: Segment monotone in the direction of u

No square inscribed in w (at least, not one with its vertices in the same cyclic order in the
square as in the curve) can be inscribed in a monotone segment of w. If the vertices of
the square were all placed on a monotone segment, it would imply that the square itself
is monotone to a given direction, but this is not true.

3.4 Walter Stromquist’s proof 35

Deﬁnition 3.34. The curve is locally monotone if, for every y ∈ R, there is an interval
(y − µ, y + µ) and a direction u(y) such that w|(y−µ,y+µ) is monotone in the direction of
u(y).

If w has this property, then the periodicity of w and the compactness of [0, 1] allow us
to choose the number µ to be a constant, independent of y. In this case, every segment
of w with length at most 2µ is monotone in some direction, and we say that w is locally
monotone with constant µ.

Since locally monotonicity is a geometric condition, we oﬀer an equivalent deﬁnition which
is more visual and, hence, easier to understand:

Deﬁnition 3.35 (Equivalent deﬁnition of 2.12). A curve w is locally monotone if for
every point w(y) of the curve, there are a neighborhood U (y) in R2 and a direction n(y)
such that no chord of the curve is contained in U (y) and parallel to n(y). The direction
n(y) is normal to u(y) and can be thought of as a kind of a normal vector (even if the
curve is not diﬀerentiable).

We will motivate this deﬁnition with the examples in Figure 3.16 and Figure 3.17. Let p
be a point of the curve w. We consider the neighborhood of p in R2 to be the open ball
B(p, ϵ), with center p and radius ϵ > 0. To check whether w is locally monotone, we need
to see that no chord of w contained in B(p, ϵ) is parallel to n(p).

Figure 3.16: Locally monotone curves

In Figure 3.16 we have two curves that are locally monotone. Let us start with the ﬁgure
on the left side. The shaded region represents the union of lines containing a chord in
w ∩ B(p, ϵ). In this case, we have two regions separating the plane. Then, any vector
crossing the shaded region may play the role of n(p) (as seen in the image).

As long as w is smooth in the neighborhood of p, this union of lines is close to a straight
line and ﬁnding n(p) is simple. But if w has sudden changes in B(p, ϵ), as shown in the
ﬁgure on the right side, then this shaded region covers a greater area. In our example,
since the union of lines containing a chord in w′ ∩ B(p′, ϵ′) covers all the plane, there does
not exist any possible assignment of n(p′). Then, to see in this case that w′ is locally
monotone we may use a smaller value of ϵ′, so we can choose a n(p′).

36 Square Peg Problem

In Figure 3.17 we have an example of a non locally monotone curve. We have replaced
the spiral found in Figure 3.16 with another spiral which has inﬁnitely many turns, but
preserving the Jordan curve. The resulting curve will not be locally monotone.

Figure 3.17: Non-locally monotone curve

As we have mentioned before, smooth curves, convex curves polygons and most piecewise
C1 curves are locally monotone curves.

Let us start by seeing that smooth curves are locally monotone. Note that these are
C1 curves. Using Deﬁnition 3.35, we could take n(y) to be the normal vector on each
neighborhood U (y). No chord contained in U (y) would be parallel to this vector. We
could also use Deﬁnition 3.34 by taking u(y) = w′(y). In this case, for every y ∈ R there
would be an interval where w would be monotone in the direction of w′(y).

The case of convex curves is even simpler. To see that convex curves are locally monotone,
take n(y) to be a vector from w(y) toward any interior point.

Let us make precise which piecewise C1 curves are locally monotone. We say that a curve
is piecewise C1 if there exist numbers x0, . . . , xk satisfying 0 = x0 < . . . < xk = 1 such
that w has a continuous non-vanishing derivative w′ on each interval [xi−1, xi], including
the one-sided derivatives at the endpoints. We denote the one-sided derivatives at xi by
w′
−(xi) and w′
+(xi). The curve has a cusp at xi if these two vectors point in opposite
directions; that is, if w′
+(xi) is a negative multiple of w′
−(xi). Then it can be shown that
a piecewise C1 curve without cusps is locally monotone. For the direction u(xi) take any
convex combination of w′
−(xi) and w′
+(xi).
Geometrically, we could see why a piecewise C1 curve with cusps is non locally monotone
using the same tools we used in the above examples. In this case, the shaded region would
cover the whole plane, incapacitating the choice of n(p).

We are now ready to extend the main result to locally monotone curves in R2.

Theorem 3.36. If w is a locally monotone curve in R2, then w admits an inscribed
square.

Proof. Assume that w is locally monotone with constant µ.

3.4 Walter Stromquist’s proof 37

Our strategy in this proof will be to approximate w using smooth curves wϵ, each of which
contains an inscribed square by Theorem 3.28. As ϵ → 0, a subsequence of these inscribed
squares converge to a square inscribed in w. The diﬃculty is in proving that the limiting
square does not have size zero, i.e., is non degenerate. To show this, we will ﬁrst show
that each wϵ is itself locally monotone with constant at least 1
2 µ. This will allow us to
establish a lower bound on the size of the square we ﬁnd in wϵ.

For this proof, we deﬁne the size |x| of an element x = (x1, x2, x3, x4) ∈ Q to be the
smallest of these four numbers: (x4 − x1), ((1 + x3) − x4), ((1 + x2) − x3) or ((1 + x1) − x2).
Therefore, |x| is the same as the length of the smallest segment of the curve that can
contain all of the points w(x1), w(x2), w(x3), w(x4). Note that |x| is measured in param-
eter space, and it is not directly related to the lengths of the sides of the corresponding
quadrilateral or any other measurement in R2. Nevertheless, the only quadrilaterals with
size zero are the one-point quadrilaterals and, since |x| is continuous on Q, any sequence
of quadrilaterals whose sizes have a positive lower bound can not converge to a one-point
quadrilateral.

Now, let ϵ > 0 and choose δ > 0 such that |x − y| < δ implies that ∥w(x) − w(y)∥ < ϵ. In
any case, choose δ < 1
2 µ. Deﬁne wϵ : R −→ R2 by

wϵ(x) = 1
δ
 ∫ δ

t=0 w(x + t)dt.

Then, wϵ satisﬁes ∥wϵ(x) − w(x)∥ < ϵ, since

∥wϵ(x) − w(x)∥ = ∥ 1
δ
 ∫ δ

t=0 w(x + t)dt − 1
δ
 ∫ δ

t=0 w(x)dt∥ ≤ 1
δ
 ∫ δ

t=0∥w(x + t) − w(x)dt∥ < ϵ

for all x, and wϵ has a continuous non-vanishing derivative given by

w′
ϵ(x) = 1
δ (w(x + δ) − w(x)).

For suﬃciently small ϵ, using the local monotonicity of w, we see that wϵ is actually a
smooth curve. We may, therefore, apply Theorem 3.28 to ﬁnd a square Sϵ inscribed in
wϵ, whose vertices are in the same cyclic order in the square as in the curve.

We will show that wϵ is locally monotone with constant 1
2 µ. Let y ∈ R and let u(y) be
chosen such that w|(y−µ,y+µ) is monotone in the direction u(y). Let x1, x2 be contained
in (y − 1
2 µ, y + 1
2 µ), with x1 < x2. Then

(wϵ(x2) − wϵ(x1)) · u(y) = 1
δ
 ∫ δ

t=0(w(x2 + t) − w(x1 + t))dt) · u(y) > 0,

because we have chosen w to be monotone in the direction u(y). That is, the monotonicity
of w forces the integrand to be strictly positive. Therefore, the chord from wϵ(x1) to wϵ(x2)
has a positive component in the direction of u(y), as required.

It follows that the inscribed square Sϵ can not have size less than µ, or its vertices would
be contained in some interval of length µ, in which wϵ would have to be monotone (but
we have seen that a square can not be inscribed in a monotone segment of the curve). We
repeat this construction for a sequence of values of ϵ approaching zero. Some subsequence
of the squares Sϵ will converge to a square S, which must have size at least µ and must
be inscribed in w. This completes the proof of Theorem 3.36.

Chapter 4

Latest study

After a whole century’s history, the Square Peg Problem remains open for its full gen-
erality. The latest work is due to Terence Tao, who published in 2017 An integration
approach to the Toeplitz Square Peg Problem [15].

Terence Chi-Shen Tao, borned in Australia in 1975, has been professor of mathematics at
the University of California, Los Angeles (UCLA) since 1999. He started to learn calculus
when he was 7, as well as beginning high school at that same age. By 9 he was already
very good at university-level calculus. He earned his Ph.D. from Princeton University
when he was 20, and UCLA promoted him to full professor at age 24.

Tao was awarded the prestigious Fields Medal in 2006 “for his contributions to partial
diﬀerential equations, combinatorics, harmonic analysis and additive number theory”.
Many mathematicians, like John Garnett, professor and former chair of mathematics at
UCLA, think that Tao could be the best mathematician in the world right now.

Tao himself tried to solve the Square Peg Problem, as we have mentioned. Here, we intend
to give a general idea of his new approach to the problem and explain in what diﬀers from
the other previous results.

In his paper, Tao proposes to modify the homological approach to the problem, by focusing
not only on the parity of intersections between some geometric objects associated to the
curve, but also on bounding certain integrals associated to these curves. He still needs
to establish a certain regularity (i.e., smoothness condition) on the curves, as in previous
results from other authors, in order to initially deﬁne these integrals. Thus, there is still
an inability to remove smoothness conditions. But, the integrals enjoy more stability
properties under limits than intersection numbers. This is why it may oﬀer a way to
establish more cases of the Square Peg Problem.

Tao gives a positive result, which appears to be new:

For any I ⊂ R and any function f : I −→ R, we deﬁne the graph Graphf : I −→ R2 to
be the function Graphf (t) := (t, f (t)), so in particular, Graphf (I) ⊂ R2 is the set

Graphf (I) := {(t, f (t)) : t ∈ I}.

Such a function f is said to be C-Lipschitz for a given C > 0 if |f (s) − f (t)| ≤ C|s − t|
for all s, t ∈ I.
 38
 39

This C is actually giving us the approximate maximum slope the curve can have. Since

|f (s) − f (t)|
|s − t| ≤ C,

we would have that there is an angle α such that

tan α = |f (s) − f (t)|
|s − t|

which is smaller that the value of C.

Theorem 4.1 (The case of small Lipschitz constant). Let [t0, t1] be an interval, and let
f, g : [t0, t1] −→ R be (1 − ϵ)-Lipschitz functions for some ϵ > 0. Suppose also that
f (t0) = g(t0), f (t1) = g(t1), and f (t) < g(t) for all t0 < t < t1. Then, the set

Graphf ([t0, t1]) ∪ Graphg([t0, t1])

inscribes a square.

In other words, the Square Peg Problem holds for curves that traverse two Lipschitz
graphs, as long as the Lipschitz constants are strictly less than one. Tao notes that
the condition of having Lipschitz constant less than one is superﬁcially similar to the
property of being locally monotone, as Stromquist considered in his result. However,
due to a potentially unbounded amount of oscillations at the endpoints Graphf (t0) =
Graphg(t0) and Graphf (t1) = Graphg(t1), the sets in Theorem 4.1 are not necessarily
locally monotone at the endpoints. Thus, the results in Stromquist’s proof do not directly
imply Theorem 4.1. Similarly for the other existing positive results on the Square Peg
Problem. Therefore, by proving this fact, he achieves a slightly further case of the Square
Peg Problem regarding the so far seen previous results.

Tao explains that without the hypothesis of small Lipschitz constant, the Jordan curve
theorem would no longer be available, and he does not know how to adapt the argument
to prove the Square Peg Problem in full generality.

Conclusions

Although the Square Peg Problem looks like an innocent conjecture, it has been an open
problem for more than a century. We have shown several results throughout this text,
some with weaker smoothness conditions than others.
Stromquist made an incredible step by proving it for locally monotone curves, since it
includes a great variety of curves, like the smooth ones. However, it seems like we are still
not able to remove a certain smoothness condition, incapacitating, therefore, the proof
for its full generality.
At present, Terence Tao is the mathematician who has gone further on this topic. But he
has needed too complex machinery in order to only sightly weaken Stromquist’s result.

Bibliography

[1] A. Emch, Some Properties of Closed Convex Curves in a Plane , American Journal
of Mathematics, Vol. 35, No. 4 (Oct., 1913), 407–412.

[2] A. Emch, On the Medians of a Closed Convex Polygon, American Journal of Math-
ematics, Vol.37 (1915), 19–28

[3] A. Emch, On Some Properties of the Medians of Closed Continuous Curves Formed
by Analytic Arcs , American Journal of Mathematics, Vol. 38, No. 1 (Jan., 1916),
6–18

[4] A. Hatcher, Algebraic Topology, Cambridge University Press, 2001.

[5] Richard P. Jerrard. Inscribed squares in plane curves. Trans. Amer. Math. Soc.,
1961, 98: 234–241.

[6] R. Maehara, The Jordan Curve Theorem via the Brouwer Fixed Point Theorem,
The American Mathematical Monthly, Vol. 91 (1984), 641–643.

[7] B. Matschke, A survey on the Square Peg Problem, Notices of the AMS, Vol. 61,
No. 4, 2012.

[8] B. Matschke. Equivariant topology methods in discrete geometry. PhD thesis, Freie
Universit¨at Berlin, 2011.

[9] James R. Munkres, Topolog´ıa, 2a Edici´on, Prentice Hall, Pearson Educaci´on, 427–
446.

[10] V. Navarro, P. Pascual, Topologia Algebraica, Edicions Universitat de Barcelona,
Col·lecci´o UB.

[11] M. J. Nielsen, Figures Inscribed in Curves (a short tour of an old problem), webpage:
https://www.webpages.uidaho.edu/ markn/squares/

[12] I. Pak, The Discrete Square Peg Problem, arxiv:0804.0657, 2008.

[13] Lev G. Schnirelman, On some geometric properties of closed curves (in Russian),
Usp. Mat. Nauk, 10:34–44, 1944.

[14] W. Stromquist, Inscribed Squares and Square-like Quadrilaterals in Closed Curves,
Mathematika, Vol.36, Part 2, No. 72 (1989).

41

42 BIBLIOGRAPHY

[15] T. Tao, An integration approach to the Toeplitz Square Peg Problem,
arxiv:1611.07441v2, 2017.

[16] P. Wiederhold, Combinatorial Image Analysis, Springer, Lecture Notes in Computer
Science, 2009.
