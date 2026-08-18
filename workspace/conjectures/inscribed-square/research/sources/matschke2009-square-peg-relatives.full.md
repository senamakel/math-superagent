<!-- source: https://arxiv.org/pdf/1001.0186 | converted from PDF -->

On the Square Peg Problem and Its Relatives

Benjamin Matschke

Abstract

Toeplitz’s Square Peg Problem asks whether every continuous simple closed curve in the plane
contains the four vertices of a square. It has been proved for various classes of suﬃciently smooth
curves, some of which are dense, none of which are open. In this paper we prove it for several open
classes of curves, one of which is also dense. This can be interpreted in saying that the Square Peg
Problem is solved for generic curves. The latter class contains all previously known classes for which
the Square Peg Problem has been proved in the aﬃrmative.1

We also prove results about rectangles inscribed in immersed curves. Finally, we show that the
problem of ﬁnding a regular octahedron on metric 2-spheres has a “topological counter-example”, that
is, a certain test map with boundary condition exists.

1 Introduction

The Square Peg Problem was ﬁrst posed by Otto Toeplitz [39] in 1911:

Conjecture 1.1 (Square Peg Problem). Every continuous embedding γ : S1 → R 2 contains four points
that are the vertices of a square.

Figure 1: Example for Conjecture 1.1. Figure 2: Jordan curve without an inscribed
square that lies completely inside.

The name Square Peg Problem might be slightly misleading: We do not require the square to lie inside
the curve, otherwise there are easy counter-examples, see Figure 2.
Toeplitz’ problem has been solved aﬃrmatively for various restricted classes of curves such as convex
curves and curves that are “smooth enough”, by various authors: Emch [6, 7, 8] for piecewise analytic
curves with only ﬁnitely many inﬂection points and other singularities where the left and right sided
tangents at the ﬁnitely many non-smooth points exist, Hebbert [15] for quadrilaterals, Zindler [42] and
Christensen [5] for convex curves, Jerrard [17] for analytic curves, Nielsen–Wright [31] for curves that
are symmetric across a line or about a point, Makeev [22] for star-shaped C2-curves that intersect every
circle in at most 4 points (more generally he proved that any circular quadrilateral can be inscribed in
such curves), Stromquist [37] for locally monotone curves, Vre´cica–ˇZivaljevi´c [41] for Stromquist’s class of
curves, Pak [32] for piecewise linear curves, Sagols–Mar´ın [34, 35] for similar discretisations, and Canta-
rella–Denne–McCleary [4] for curves with bounded total curvature without cusps and for C1-curves. The
strongest version so far was due to Stromquist [37, Thm. 3] who established the Square Peg Problem for
locally monotone Jordan curves. Here a curve γ : S1 → R 2 is called locally monotone if at every point

1Since the appearance of this article on the arXiv, some new results have been proved, see Section 1.2. In particular,
Tao’s class of curves [38] contains curves that do not lie in the classes given in the current article.

1arXiv:1001.0186v2  [math.MG]  18 Mar 2022
x ∈ S1 there exists a neighborhood U of x and a linear function α : R 2 → R such that α ◦ γ|U is strictly
increasing.
All known proofs are based on the fact that “generically” the number of squares on a curve is odd,
which can be measured in various topological ways. See Klee–Wagon [20], Pak [32], Vre´cica–ˇZivaljevi´c [41],
and [29] for surveys. For general embedded plane curves, the problem is still open.

Related is the Rectangular Peg Problem, which was only recently proved by Greene and Lobb [11];
compare with Section 1.2(5).

Theorem 1.2 (Rectangular Peg Problem, Greene–Lobb theorem). Every C∞ embedding γ : S1 → R 2

contains four points that are the vertices of a rectangle with a prescribed aspect ratio r > 0.

We state it for smooth curves only, since already this is (was) a hard problem. Equivalently one could
state Theorem 1.2 for piecewise linear curves. Before the present article and the recent results listed in
Section 1.2(3)–(5), it was only known to hold in the case r = 1, that is, for inscribed squares. The proof
in Griﬃths’s paper [12] contains unfortunately an error in the calculation of intersection numbers, see
[26] for details. The diﬃculty comes from the fact that, counted with orientations, every smooth curve
inscribes generically zero rectangles of a prescribed aspect ratio, see Section 4.1. E.g. an ellipse inscribes
two rectangles with opposite orientations.

Awards. The author has put 100 Euros each of these two problems; only for Conjecture 1.1 the bounty is
still available.

1.1 The main results

1.) In Section 2 we essentially prove the Square Peg Problem for two new classes of curves.

Figure 3: Example
for Theorem 1.3.

The ﬁrst one is the ﬁrst known open set of continuous maps S1 → R 2 in the
compact-open topology (equivalently, in ((R 2)S1, ||.||∞)) for which the Square Peg
Problem holds. It does neither require the curve to be smooth nor injective; see
Section 2 for the rather simple proof and some variations of the statement.

Theorem 1.3. Let A denote the annulus {x ∈ R 2 | 1 ≤ ||x|| ≤ 1 + √2}. Suppose
that γ : S1 → A is a continuous closed curve in A that represents the generator of
π1(A) = Z . Then γ inscribes a square of side length at least √2.

Figure 3 shows an example. This class does not contain all previous known
classes of curves for which the Square Peg Problem is proved, and it is not even
dense, but it is the ﬁrst result that bounds the size of an inscribed square from below.
2.) The second class is considerably more technical, but it is open, dense, and it contains all previous
classes.

Theorem 1.4. The Square Peg Problem holds for all curves in an explicit open and dense neighbourhood
of Stromquist’s locally monotone curves in the space of all injective maps S1 → R 2 with respect to the
C0-topology. In this sense, any generic Jordan curve inscribes a square.

Explicit versions of this theorem are given in Corollaries 2.9, 2.10, and 2.12. Moreover, in Corollary 2.13
we prove that curves C0-close to C2-embedded curves inscribe squares, which can be regarded as a version
of Theorem 1.3 for more general shapes.
3.) In Section 4 we prove the following ﬁrst non-square special case of the Rectangular Peg Problem.

Theorem 1.5. Let γ : S1 → R 2 be a C∞ curve whose angular convexity is at most 60◦. Then γ inscribes
a rectangle with aspect ratio √3.
 2

Here we say that a smooth plane curve γ has angular convexity at most α, if the signed curvature of
γ restricted to any positively oriented arc is at least −α; here the signs are chosen in such a way that a
positively oriented arc on the unit circle of length α has signed curvature +α; see Figure 11. A smooth
curve γ is convex if and only if its angular convexity is at most 0. The proof of Theorem 1.5 uses a hidden
symmetry that appears for r = √3, which is a geometric piece of information.
4.) In Section 3 we deal with immersed planar curves and the parity of their inscribed squares.
Cantarella [3] conjectured that this parity is an isotopy invariant and he stated a precise formula based on
examples. We disprove Cantarella’s conjecture and state in Theorem 3.1 how the parity can be computed
from the angles at the intersection points. Theorem 3.2 gives a similar formula for the parity of inscribed
rectangles of a ﬁxed aspect ratio.

The last section, Section 5, treats higher-dimensional analogs. We ask for inscribed d-dimensional
regular crosspolytopes in metric (d−1)-spheres. The problem is open for all d ≥ 3, but we use Koschorke’s
obstruction theory [21] to derive that for d = 3, a natural topological approach for a proof fails: The
strong test map in question exists.
Parts of this paper have been obtained in [26, Chap. III] and [28, Chap. II]. Some of the new results
have been announced in [27].

1.2 Recent progress

After this article appeared on the arXiv, some progress was made with respect to both Conjectures 1.1
and 1.2.

1. Pettersson–Tverberg– ¨Osterg˚ard [33] showed that any Jordan curve in the 12 × 12 square grid in-
scribes a square whose size is at least 1/
√2 times the size of the largest axis parallel square that
ﬁts into the interior of the curve.

2. Van Heijst [16] proved that algebraic curves of degree d inscribe at most (d4 = 5d2 + 4d)/4 squares
or inﬁnitely many. For this he makes use of Bernstein’s theorem, which states that the number
of common zeros in (C ∗)k of k generic Laurent polynomials in k variables with prescribed Newton
polytopes equals the mixed volume of these polytopes.

3. Tao [38] proved that Jordan curves given as the union of two graphs of (1 − ε)-Lipschitz functions
f, g : [0, 1] → R with f (0) = g(0) and f (1) = g(1) inscribe squares. He makes use of an area
argument, using certain conserved integrals of motion when moving squares in the plane, which
appeared in a similar form already in Karasev [19]. Two special features of his approach are
that he uses the Lipschitz condition as a global condition, whereas all previous results (except for
Theorem 1.3) only argue locally, and that he can avoid the topological parity argument for the
number of inscribed squares, which so far always creates technical problems for non-smooth curves.
If the Lipschitz constant is suitably adjusted, Tao’s proof also extends to inscribed rectangles and
more generally equilateral trapezoids [38, Rem. 3.10].

4. The area argument by Karasev and Tao was then used by Akopyan and Avvakumov [1] and the
author [30] to prove Theorem 1.2 in the special case of convex curves, also for more general inscribed
quadrilaterals.

5. Greene and Lobb [11] proved Theorem 1.2 (thus winning one of the two above awards). Their
proof is based on symplectic geometry and uses in particular that the Klein bottle does not admit a
Lagrangian embedding into C 2. In [10] they extended this furthermore to all circular quadrilaterals,
thus settling a conjecture of Makeev [22, 24].
 3

2 Inscribed squares

2.1 Notations and a convenient parameter space of inscribed polygons

For an element x of the circle S1 ∼= R /Z and t ∈ R we deﬁne x + t ∈ S1 as the counter-clockwise rotation
of x by the angle 2πt around 0. For any space X, we denote by ∆X n := {(x, . . . , x) ∈ X n} the thin
diagonal of X n. Let σn = {(t1, . . . , tn+1) ∈ R n+1
≥0 | ∑ ti = 1} be the standard n-simplex.
The natural parameter space of n-gons is

Pn := S1 × σn−1.

It parametrises n-gons on S1 or on some given curve S1 → R ∞ by their vertices in the following way

ϕ : Pn → (S1)n : (x; t1, . . . , tn) ↦→ (x, x + t1, x + t1 + t2, . . . , x + n−1∑

i=1 ti).

The so parametrised polygons are the ones that are lying counter-clockwise on S1. The map ϕ is not
injective, as all (x; 0, . . . , 0, 1, 0, . . . , 0) are mapped to the same point (x, . . . , x); but it is injective on
Pn\(S1 × vert(σn−1)), and on this set ϕ bijects to (S1)n\∆(S1)n. Let P ◦
n = S1 × (σn−1)◦ denote the
interior of Pn. The map ϕ identiﬁes P ◦
n with the set of n-tuples of pairwise distinct points in counter-
clockwise order on S1. We deﬁne the boundary as ∂P ◦
n := Pn\P ◦
n .
We let Z /n = ⟨ε⟩ act on Pn by

ε · (x; t1, . . . , tn) = (x + t1; t2, . . . , tn, t1).

This corresponds to a cyclic relabeling of the vertices of the parametrised polygon. It makes Pn clearly
into a free Z /n-space.

Remark 2.1 (Other natural coordinates). Z /n acts on S1 via ε·x = x+ 1
n and on σn−1 via ε·(t1, . . . , tn) =
(t2, . . . , tn, t1). Then Pn is in fact as a Z /n-space isomorphic to the product S1 × σn (with the diagonal
Z /n-action). A particularly convenient isomorphism is the map Pn −→Z /4 S1 × σn deﬁned by

(x; t1, . . . , tn) ↦→ (x + n∑

i=1
 n + 1 − 2i
2n ti; t1, . . . , tn),

since it sends (x; 1
n , . . . , 1
n ) to (x; 1
n , . . . , 1
n ).

An arc on S1 from x ∈ S1 to y ∈ S1 will always mean the arc that goes counter-clockwise, and for
x = y it is degenerate to a point. For x, y ∈ S1, we denote by y − x the length of the arc from x to y,
normalised with the factor 1
2π . For an n-tuple (x1, . . . , xn) ∈ ϕ(Pn) ⊆ (S1)n we write

[x1, . . . , xn] := (x1; x2 − x1, x3 − x2, . . . , xn − xn−1, 1 − n∑

k=2
(xk − xk−1)) ∈ Pn.

The function [. . .] : ϕ(Pn) → Pn is right-inverse to ϕ, but not continuous.
Smooth will always mean C∞. An ε-close square is a quadrilateral whose ratios between the edges
and diagonals are up to an ε-error the ones of a square. The precise deﬁnition will not matter. We will
use “ε-closeness” with other polygons analogously.

2.2 Schnirelman’s proof for the smooth Square Peg Problem

We start with Schnirelman’s proof [36], since it is in my point of view the most beautiful one, and we
will extend it in Section 2.3. The following presentation uses transversality and a bordism argument; in
Schnirelman’s days, these notions had not been formalised and baptised yet, but his argument works like
this.
 4

Proof. Suppose that γ is smooth. P4 parametrises quadrilaterals on γ. Let f : P4 → R 6 be the function
that measures the four edges and the two diagonals of the quadrilaterals,

f : P4 −→ R 4 × R 2

[x1, x2, x3, x4] ↦−→ (||γ(x1) − γ(x2)||, ||γ(x2) − γ(x3)||, ||γ(x3) − γ(x4)||,

||γ(x4) − γ(x1)||, ||γ(x1) − γ(x3)||, ||γ(x2) − γ(x4)||)
 (1)

Let ∆ := ∆R 4 ×∆R 2 = {(a, a, a, a, b, b) ∈ R 6}. The map f measures squares, since Q := f −1(∆)\∆(S1)4 =
f −1(∆) ∩ P ◦
4 is the set of all squares that lie counter-clockwise on γ. Moreover f is Z /4-equivariant with
respect to the natural Z /4-actions. We can deform f relative to a small neighborhood of ∂P ◦
4 equivariantly
by a small ε-homotopy to make it transversal to ∆. So Q becomes a free Z /4-manifold that parametrises
ε-close squares. As the codimension of ∆ in R 6 agrees with dim P4 = 4, Q is zero-dimensional. If we
deform the curve smoothly to another curve, e.g. the ellipse, which can also be performed in R 4 to
construct such a homotopy easily, then Q changes by a Z /4-bordism. If the homotopy is chosen smoothly
then this bordism stays away from the boundary of P ◦
4 , since then no curve inscribes ε-close squares which
have arbitrarily small edges (the angles get too close to π). Hence Q represents a unique class [Q] in the
zero-dimensional unoriented bordism group MO0(P ◦
4 /Z /4) ∼= H0(P ◦
4 /Z /4; Z /2) ∼= Z /2. If γ is an ellipse
then f is already transversal to ∆ and Q consists of one point. Hence [Q] is the generator of Z /2, thus
Q is non-empty for any smooth curve γ. Taking a convergent subsequence of ε-close squares ﬁnishes the
proof.

If γ is only continuous one might try to approximate it with smooth curves and then take a convergent
subsequence of the squares that are inscribed in them. The problem is to guarantee that this subsequence
does not converge to a square that degenerates to a point. Natural candidates for which this works are
continuous curves with bounded total curvature without cusps, see Cantarella, Denne & McCleary [4].
So far, nobody managed to do this for all continuous curves.
Schnirelman’s proof can be reﬁned to get a slightly stronger result.

Corollary 2.2 (of the proof). We may assume that γ is parametrised counter-clockwise around its inte-
rior. Then one can ﬁnd four vertices of a square on γ and order them such that they lie counter-clockwise
on γ and also label the square counter-clockwise.

Proof. This can be achieved by restricting Q in the above proof to the set Q′ of 4-tuples [x1, x2, x3, x4]
in P4 that label the vertices of a square (γ(x1), . . . , γ(x4)) in counter-clockwise order. Along a bordism
the orientation of the parametrised square cannot change (here we take a bordism that is induced by a
isotopy of the curve in the plane). If γ is an ellipse then it is clear that Q′ equals Q, thus it represents
the generator in MO0(P ◦
4 /Z /4).

2.3 New cases: A simple open class of curves

In this section we prove Theorem 1.3 from the introduction together with the following two versions,
whose proofs are very similar. See Figures 2.3 and 2.4 for examples.

Theorem 2.3. Let A denote the area [−3, 3]2\(−1, 1)2. Suppose that γ : S1 → A is a continuous closed
curve in A that represents the generator of π1(A) = Z . Then γ inscribes a square of side length at least√2.

Theorem 2.4. Let ∆ be an equilateral triangle in R 2 whose center point is the origin. Let A be the
closure of ((1 + √3) · ∆)\∆. Suppose that γ : S1 → A is a continuous closed curve in A that represents
the generator of π1(A) = Z . Then γ inscribes a square of side length at least 2
√3 − 3.

It seems to be desirable to extend this method for much more general shapes in order to possibly
prove the Square Peg Problem for all curves.
The proofs of Theorems 1.3, 2.3, and 2.4 follow from the following lemma.

5

Figure 4: Example for Theorem 2.3. Figure 5: Example for Theorem 2.4.

Lemma 2.5. Let A be an open subset of R 2. Let SA be the set of 4-tuples (P1, . . . , P4) ∈ A4 that form
the vertices of a possibly degenerate square in counter-clockwise order. Let C be a connected component of
an ε-neighborhood of SA that does not contain degenerate squares, that is, points of the form (P, P, P, P ).
Let ̃γ : S1 → A be a generic curve that contains an odd number of squares in C. Then every continuous
curve γ : S1 → A that is homotopic to ̃γ in A contains a square in C as well.

Here, by a generic curve ̃γ we mean a curve such that the corresponding test map that measures
squares in C hits the test-space transversally.

Proof of Lemma 2.5. The proof is a simple bordism argument, similarly to Schnirelmann’s proof above.
First assume that γ is generic in the sense that its test map is transversal to the test-space. When
deforming γ to ̃γ within A, their inscribed squares change by a bordism, except that problems may
appear close to degenerate squares. However when we restrict the bordism to squares that are in the
component C, this problem disappears. Thus, γ and ̃γ have modulo 2 the same number of inscribed
squares within C, and by assumption this number is odd.
If γ was not generic, there is several ways to make it generic. Possibly the simplest one is to replace
γ by a slightly deformed copy within A that is generic (this can be achieved by allowing deformations of
γ by local bumps and using the transversality theorem, as in Section 4.4). The previous argument then
yields a square in C that is almost inscribed in γ. Taking better and better approximations to γ in the
C0-norm, and using the compactness of γ, we obtain a square inscribed in γ, which is non-degenerate as
C is bounded away from degenerate squares.

Proof of Theorem 1.3. For r ∈ [1, ∞], let Ar = {x ∈ R 2 | 1 ≤ ||x|| ≤ r}, and consider its set of inscribed
squares SAr as deﬁned in Lemma 2.5. For small enough r, SAr has two connected components, which
we call the components of big squares and of small squares. The component of big squares deformation
retracts Z /4-equivariantly to the set of inscribed squares on the unit circle, and the component of small
squares deformation retracts Z /4-equivariantly to the set of degenerate squares in Ar. For large enough r,
SAr becomes obviously connected. To understand the phase transition, consider the path of squares Qα
(α ∈ [0, 3
4 π]) with vertex set {e±iα, e±iα + 2 sin α}. It connects the degenerate square Q0 on the unit
circle S1 to a square Q3π/4 that is inscribed in S1, such that for each α, two adjacent vertices of Qα lie
on S1 and the other two lie in the exterior of S1. This is a path in SA∞ between Q0 and Q3π/4 with
the minimal possible maxα maxP ∈vert(Qα) ||P ||. One computes that for the path Qα this maximum vertex
norm is r0 := 1 + √2 and it is attained at α0 = arctan(1 + √2). This implies that for any r < r0, SAr
has two connected components (as above), whereas for r ≥ r0, SAr is connected. Moreover, Qα0 has side
length (√2 + 2)1/2 > √2, and we see that the smallest squares in the component of big squares of SA,r
for r < r0 are the ones inscribed in S1, which have side length √2.
To prove the theorem, we may assume that γ is actually a curve in the interior of A = Ar0. The other
cases follow by a limit argument: Approximate γ by a sequence of curves in the interior, show that each
approximating curve inscribes a square with side length at least √2, and take a convergent subsequence
of such squares. Thus we may replace A by Ar∗ for some r∗ < r0, such that still γ ⊂ Ar∗.
Let ̃γ be an ellipse in Ar∗ that represents a generator of π1(Ar∗). We apply Lemma 2.5 to Ar∗, γ
and ̃γ, noting that the unique (generic) square inscribed in ̃γ lies in the component of SAr∗ of big squares.
This proves the theorem.
 6

Remark 2.6. For any r > 1 + √
2 it is open whether Theorem 1.3 holds for the annulus Ar.

The proofs of Theorems 2.3 and 2.4 are analogous, using the fact that for a slightly smaller set A the
set of inscribed squares becomes disconnected.

2.4 New cases: An open and dense class of curves

First we will establish the main theorem of this section, which gives a quite general but somewhat technical
condition for the existence of inscribed squares. Then we deduce four less and less technical corollaries
that demonstrate its scope.
Let γ : S1 → R 2 be a simple closed curve (that is, injective and continuous). We need some prepa-
ration. Let f : P4 → R 6 be the corresponding test map that measure the four edges and two diagonals,
which was deﬁned in equation (1) in Section 2.2. For a path ω : S1 → (S1)2\∆(S1)2, ω(t) = (ω1(t), ω4(t)),
we deﬁne

P4(ω) := {[ω1(t), x2, x3, ω4(t)] ∈ P ◦
4 | t ∈ S1, x2, x3 ∈ S1 such that (ω1(t), x2, x3, ω4(t)) ∈ ϕ(P4)},

which is the set of quadrilaterals that are counter-clockwise inscribed in S1 where the ﬁrst and last vertex
are of the form ω1(t) and ω4(t) for t ∈ S1.
P4(ω) can be parametrised by g : S1 × σ2 → P4(ω), where S1 parametrises ω and σ2 the three arc
lengths between the points ω1(t), x2, x3 and ω4(t). The map g is injective if and only if ω is.

Deﬁnition 2.7. We call an inscribed quadrilateral in γ given by [x1, x2, x3, x4] a special trapezoid if

f ([x1, x2, x3, x4]) = (a, a, a, b, e, e) with a > b, for some reals a, b, e. (2)

The size of a special quadrilateral [x1, x2, x3, x4] is the normalised arc length x4 − x1.

γ a
 a
 a

b a > b

x1
x2x3x4
 γ(x1)

γ(x2)γ(x3)

γ(x4)
2πε

Figure 6: Example of a special trapezoid of size ε.

Let S ⊂ P4 denote the set of all special trapezoids. Deﬁne i(S, P4(ω)) ∈ F 2 as the mod-2 intersection
number of f ◦ g and V := {(a, a, a, b, e, e) ∈ R 6 | a ≥ b} (3)

in R 6. This is only well-deﬁned if f (g(S1 × ∂σ2)) ∩ V = ∅ and im(f ◦ g) ∩ ∂V = ∅. The ﬁrst requirement
is trivially fulﬁlled because a quadrilateral [x1, x2, x3, x4] with xi = xi+1 for some i ∈ {1, 2, 3} cannot be
special as a > 0. The second requirement holds if and only if P4(ω) parametrised no inscribed quadrilateral
γ that is a square. The map f ◦ g can now be deformed by a homotopy relative to S1 × ∂σ2, such that
at no time it intersects the boundary of V , and such that it becomes transversal to V . The intersection
number then counts the preimages of V under f ◦ g modulo 2.

Theorem 2.8. Suppose there is a path ω : S1 → (S1)2\∆(S1)2 ∼= P ◦
2 , ω(t) = (ω1(t), ω4(t)), that represents
a generator in π1((S1)2\∆(S1)2) ∼= π1(S1) ∼= Z . If γ does not inscribe a square then the mod-2 intersection
number i(S, P4(ω)) is well-deﬁned and it equals 1.

The mod-2 intersection number will be described in the proof, see Section 2.4.1. First let us state and
prove a few less technical corollaries.
 7

Corollary 2.9. Suppose there is a path ω : S1 → (S1)2\∆(S1)2 = P ◦
2 , ω(t) = (ω1(t), ω4(t)), that represents
a generator in π1((S1)2\∆(S1)2) ∼= π1(S1) ∼= Z . If P4(ω) ∩ S = ∅, then γ has an inscribed square.

Proof. The mod-2 intersection number in Theorem 2.8 is here trivially zero.

Corollary 2.10. Suppose there is an ε ∈ (0, 1), such that γ inscribes no (or generically an even number
of ) special trapezoid of size ε. Then γ has an inscribed square.

Proof. Use Theorem 2.8 with ω(t) := (t, t + ε).

Remark 2.11. The following piece of intuition might be useful. Let 0 < ε < 1/2 and let us call an
inscribed square [x1, x2, x3, x4] of size larger than ε if {x1, x2, x3, x4} ⊂ S1 does not lie in an arc of
normalised length ε. Suppose everything is generic, and we change ε continuously or γ by an ambient
isotopy. Then the set of inscribed special trapezoids of size ε changes by an unoriented bordism, except
at points when a becomes equal to b (compare with Figure 6), at which point an inscribed square of size
larger than ε (with vertices cyclically on γ) will appear or disappear and the parity of the number of
special trapezoids of size ε changes as well.
We remark that Corollary 2.10 holds indeed for any ε, not only small ones.

Corollary 2.12. The class of curves in Corollary 2.10 is an open and dense neighbourhood of Stromquist’s
locally monotone curves in the space of all injective maps S1 → R 2 with respect to the C0-topology. In
this sense, any generic Jordan curve has an inscribed square.

This implies Theorem 1.4 from the introduction.

Proof. The class of γ without inscribed special trapezoids of size ε is open, even for ﬁxed ε. By compact-
ness, for any locally monotone curve γ, there exists an ε such that for any x ∈ S1, there exists a linear
function α : R 2 → R such that α◦γ|[x,x+ε] is strictly increasing. For this ε, γ inscribes no special trapezoid
of size ε, because a special trapezoid ABCD with short edge AB cannot be orthogonally projected to
a line such that A and B project to the endpoints of the projection’s image. The density statement is
obvious, since already the class of smooth curves is dense.

Corollary 2.13. Let γ0 : S1 ↪→ R 2 be a C2-embedding with curvature bounded above by k. Then any
continuously embedded γ : S1 → R 2 in the 1
4k -neighbourhood of γ0 with respect to the C0-metric has an
inscribed square.

Proof. We may and do assume that γ0 is parametrised by arc-length and that k = 1. Let δ = 1
4 . The
following calculation shows that γ does not inscribe a special trapezoid of size ε = 2 arccos( 1
3 ).
Assume ABCD was such a hypothetical special trapezoid with parameters x1, x2, x3, x4 that satisfy (2)
and x4 − x1 = ε. They also parametrise an inscribed quadrilateral A0B0C0D0 in γ0. We have a ≥ b =
||A − D|| ≥ ||A0 − D0|| − 2δ ≥ 2 sin ε
2 − 2δ =: d1, where the ﬁrst inequality is the triangle inequality, and
the latter one uses the given curvature bound and the formula for the length of a chord in the unit circle
with central angle ε. On the other hand, for some 1 ≤ i ≤ 3, xi+1 − xi ≤ ε
3 , say for i = 1 (the other
cases are analogous). Then a = ||B − A|| ≤ ||B0 − A0|| + 2δ ≤ ε
3 + 2δ := d2. Together, both bounds yield
d2 ≤ d1, which is impossible for the chosen values of δ and ε.
The result follows from Corollary 2.10.

Remark 2.14. We remark that in Corollary 2.13, δ = 1
4k is not best possible. It could be replaced by
1
3k , as a more detailed analysis shows that there will be no inscribed special trapezoids of size ε = π
2k . It
is to check that in any arc a of length ε there is no special trapezoid ABCD with AD as the shortest
edge such that A is 1
3k -close to one end point of a, D is 1
3k -close to the other end point, and B and C are
1
3k -close to a, see Figure 7. On the other hand, for example δ = 1
2k is out of reach with our method.

8

Figure 7: 1
3k -neighborhood of a. In this particular ﬁgure, a has constant curvature k.

2.4.1 Proof of Theorem 2.8

The proof is based on equivariant obstruction theory. This was ﬁrst used in connection to the Square Peg
Problem by Vre´cica and ˇZivaljevi´c [41], who applied it to the Fulton–MacPherson compactiﬁcation of the
conﬁguration space P ◦
4 . Here, we will apply it to suitable closed subsets of P ◦
4 .
We will need the following instance of basic relative obstruction theory. Consider a rank k vector
bundle ϕ : E → B over a connected k-dimensional manifold B with non-empty connected boundary ∂B.
Let 0ϕ ⊂ E denote the zero section. Given a nowhere vanishing section u : ∂B → E over the boundary,
there is a relative Stiefel–Whitney class wk(u) ∈ H k(B, ∂B; F 2) ∼= H0(B; F 2) = F 2, which is the primary
obstruction for the existence of a nowhere vanishing extension of u to all of B modulo 2. If s is an
arbitrary extension of u to all of B, then the parity of the generic number of zeros of s coincides with
the Poincar´e dual of wk(u) in F 2. If u1, u2 are two nowhere vanishing sections of ϕ|∂B then the primary
obstruction to the existence of a ﬁberwise homotopy between u1 and u2 is the so-called diﬀerence cocycle
d(u1, u2) ∈ H k−1(∂B; F 2) ∼= H0(∂B; F 2) = F 2. Moreover, if δ denotes the connecting homomorphism
H k−1(∂B; F 2) → H k(B, ∂B; F 2), which is an isomorphism in our setting since H k(B; F 2) = 0, then
δ(d(u1, u2)) = wk(u1) − wk(u2). Moreover, choose a third nowhere vanishing section t over ∂B. Consid-
ering t, ui as sections in the associated sphere bundle of ϕ∂B, we can deﬁne mod-2 intersection numbers
i(t, ui), i = 1, 2. Then the Poincar´e dual of d(u1, u2) equals i(t, u1) − i(t, u2). Therefore, considered as
elements of F 2, wk(u1) − wk(u2) = i(t, u1) − i(t, u2).

Proof of Theorem 2.8. First we prove the theorem in the special case when ω is the path ωε(t) := (t, t + ε)
for some ﬁxed 0 < ε < 1/2; we may choose ε = 1/4. Then P4(ω) ∩ S is the set of inscribed special
trapezoids of size ε.
Let P ε
4 := {(x; t1, . . . , t4) ∈ P4 | t1, . . . , t4 ≤ 1 − ε} = S1 × T ε,

where T ε := {(t1, . . . , t4) ∈ σ3 | t1, . . . , t4 ≤ 1 − ε} is a truncated tetrahedron. Let T ′
1, . . . , T ′
4 be the
triangular facets of T ε, and H ′
1, . . . , H ′
4 the hexagonal facets. That is, T ′
i = {t ∈ T ε | ti = 1 − ε} and
H ′
i = {t ∈ T ε | ti = 0}. Moreover, deﬁne Ti := S1 × T ′
i and Hi := S1 × H ′
i for 1 ≤ i ≤ 4. Note that for
our choice of ω, P4(ω) = T4. Moreover, ∂P ε
4 = ⋃i Ti ∪ ⋃ Hi.
Now assume that ∂P ε
4 parametrises no inscribed square (otherwise we are done). Then the parity of
the generic number of inscribed squares up to Z /4-symmetry that are parametrised by B := P ε
4 /Z /4 is
well-deﬁned, call it nε(γ).
Let ϕ : E → B denote the canonical projection from E := P ε
4 ×Z /4(R 6/∆) to B. This is a rank 4 vector
bundle with ﬁber R 6/∆. Let 0ϕ denote its zero-section. The test map f induces a section s1 : B → E
and s−1
1 (0ϕ) is the set of all inscribed squares up to Z /4-symmetry that are parametrised by B, and put
u1 := s1|∂B. Moreover nε(γ), the generic parity of s−1
1 (0ϕ) (assuming that u1 is nowhere zero), equals the
Poincar´e dual of the top relative Stiefel–Whitney class w4(u1) ∈ H 4(B, ∂B; F 2) ∼= F 2.
Similarly let s2 : B → E be the analog section that is induced from an arc-length parametrised ellipse
γ0 instead of γ, and let u2 := s2|∂B.
By the above discussion, nε(γ) − nε(γ0) = i(t, u1) − i(t, u2) (as elements in F 2) for any nowhere
vanishing section t of ϕ|∂B. A nowhere vanishing section t of ϕ|∂B is the same thing as a Z /4-equivariant
map t′ : ∂P ε
4 → (R 6/∆)\0. We construct a suitable t via t′ as follows. For any p = (x; t1, . . . , t4) ∈ T4 ⊂
∂P ε
4 deﬁne t′(p) as (1, 1, 1, 0, 0, 0) + ∆. Let R ⊂ R 6/∆ be the ray from 0 through this vector, that is,
R/∆ = V /∆, where V was deﬁned in (3). Then f (p) ∈ R if and only if p parametrises a special trapezoid
or a square. Extend t′ Z /4-equivariantly to ⋃i Ti.
 9

Now extend t′ furthermore continuously on H4 such that for all p = (x; t1, . . . , t4) ∈ H4, t′(p) =
(a1, a2, a3, a4, 0, 0) + ∆ with a4 > min(a1, a2, a3), and such that t′ is equivariantly extendable to ⋃i Hi.
An explicit way to do this is to deﬁne

t′(p) = (r(t1), r(t2), r(t3), 1 + 3∏

i=1 ti(1 − ε − ti), 0, 0) + ∆, for p = (x; t1, . . . , t4) ∈ H4,

where r : [0, 1 − ε] → [0, 1] is deﬁned by r(x) = 1 for x ∈ [0, 1/2], r(1 − ε) = 0, and linearly between 1/2
and 1 − ε.
Any inscribed quadrilateral that is parametrised by p ∈ H4 has a degenerate third edge. Therefore
R ≥0 · f (p) will never coincide with R ≥0 · t′(p) for p ∈ H4. Equivalently, R ≥0 · s1([p]) will never coincide
with R ≥0 · t([p]) for p ∈ H4, where [p] denotes the image of p in B = P ε
4 /Z /4.
Thus i(t, u1) is precisely the parity of the generic number of inscribed special trapezoids of size ε for γ,
and i(t, u2) is the same for the ellipse.
By inspecting the ellipse, which is particularly easy for small ε, we get nε(γ0) = 1 and i(t, u2) = 0,
hence nε(γ0) − i(t, u1) = 1 in F 2. Therefore for γ we get nε(γ) = 1 + i(t, u1) in F 2, which proves the
theorem for the above ωε.

For general ω, we reduce to the previous argument for ωε as follows. By possibly reversing the
orientation of ω, we may assume that ω and ωε are homotopic within (S1)2\∆(S1)2 via some homotopy Ωτ ,
τ ∈ [0, 1], with Ω0 = ωε and Ω1 = ω. Using Ωτ we will construct a Z /4-map h : P ε
4 → P ◦
4 such that
for each 1 ≤ i ≤ 4, Hi is sent into {(x; t1, . . . , t4) | ti = 0}, and such that T4 ∼= S1 × σ2 is sent
homeomorphically to P4(ω). Explicitly, we may deﬁne h as follows. Choose ε′ ∈ (ε, 1/2), e.g. ε′ = 1/3
if ε = 1/4. On the subset P ε′
4 , we let h be the identity. The complement P ε
4 \P ε′
4 has four connected
components, one of which is the set of all p = (x; t1, . . . , t4) ∈ P ε
4 that satisfy t4 > 1 − ε′. At such p, we
deﬁne τ (p) := ((1 − ε) − t4)/(ε′ − ε), ω(p) = (ω(p)
1 , ω(p)
4 ) := Ωτ (p), c(p) := τ (p) + (1 − τ (p))(ω(p)
4 − ω(p)
1 )/ε, and

h(p) = (ω(p)
1 (x); c
(p)t1, c
(p)t2, c
(p)t3, 1 − c
(p)(1 − t4)).

We extend h to the other three connected components of P ε
4 \P ε′
4 by Z /4-equivariance. This makes h
well-deﬁned, continuous, and it satisﬁes the mentioned properties. Let s′
1 : B → E be the section induced
by f ◦ h, and let u′
1 = s′
1|∂B. As with ωε, we apply an analogous obstruction theory argument, this time
to s′
1 instead of s1, to obtain w4(u′
1) = 1 + i(t, u′
1) ∈ F 2. The diﬀerence is that now, (i) i(t, u′
1) counts
the parity of the generic number of inscribed special trapezoids in P4(ω), instead of those of size ε, and
(ii) the Poincar´e dual of the relative Stiefel–Whitney class w4(u′
1) counts via s′
1 the generic number of
Z /4-orbits [p] ∈ B such that h(p) parametrises an inscribed square in γ. This proves the theorem.

2.4.2 Remarks

1. The proof of Theorem 2.8 gives slightly more: Let qε be the parity of the generic number of inscribed
squares up to symmetry whose parametrisation (x; t0, . . . , t3) ∈ P4 satisﬁes ♯{i | ti ≤ 1−ε} = 0 mod 2.
And let sε be the parity of the generic number of inscribed special trapezoids of size ε. If one of qε, sε
is well-deﬁned then both of them are, and qε ̸= sε mod 2. An analog statement holds for arbitrary ω.

2. P4(ω) can be regarded as a “membrane”, which separates P4 into two components if ω is injective. If
γ circumscribes no square then there is an odd number of paths in S that pass through P4(ω) and
approach the boundary at S1 × e3, e3 being the one vertex of σ3. These paths might look very chaotic
close to the boundary. On the other side of the membrane P4(ω), this odd number of paths cannot all
end in each other. One of them has to end somewhere else. It might end suddenly in P ◦
4 , which means
that it found a square, or it might end somewhere else at ∂P ◦
4 . The latter is (unfortunately) possible:

The drawn path of special trapezoids starts in the middle of the spiral at S1 × e3 with a quadrilateral
that is degenerate to a point, and it stops when x1 and x4 meet again, x4 − x1 = 1.

10

3. The original proof of Theorem 2.8 from [28] is slightly more elementary (but admittedly more diﬃcult
to digest).

4. The corollaries are sometimes good for proving the existence of a square, if the curve is piecewise C1

but has cusps (points in which the tangent vector changes the direction). This however works not in
a large generality as the previous example shows.

5. Theorem 2.8 and its proof deal with the curve intrinsically, since the only datum of γ we used is
the distances between points on γ. If we deﬁne a square in a metric space (X, d) to be a 4-tuple
(x0, . . . , x3) ∈ X 4 such that d(x0, x1) = d(x1, x2) = d(x2, x3) = d(x3, x0) and d(x0, x2) = d(x1, x3),
then the theorem also holds for curves γ : S1 → X. More generally, X does not need to fulﬁll the
triangle inequality. In other words, we do not need an embedded curve but a distance deﬁning function
d : S1 × S1 → R that is continuous, positive deﬁnite, and symmetric.

3 Immersed curves

3.1 Squares inscribed in immersed curves

Toeplitz’s conjecture is about inscribed squares on simple closed curves in the plane. There are plenty of
ways to generalize this problem. In this section we study what we can say about the number of inscribed
squares if we omit the requirement that γ has to be injective. In this setting it makes sense to more
generally allow γ to be a ﬁnite union of curves, γ : X → R 2, X = ∐n
i=1 S1. There are several kinds of
degenerate squares, which we have to deal with in that case. To be able to count inscribed squares in
a stable manner, we will only consider generic smooth curves and we will not count degenerate squares.
Here, generic means that: (i) self-intersections of γ are transversal with a non-orthogonal intersection
angle, (ii) the test map (4) is transversal to the test-space V , and (iii) no non-degenerate inscribed square
has a vertex at a self-intersection point of γ. If any of these condition fails, the number of inscribed
squares might not be stable under small ambient isotopies of γ.
Given γ : X → R 2, we construct a test map

t : X 4\D → R 6 ⊃ ∆ (4)

with the same pointwise formula as in (1), ∆ = ∆R 4 × ∆R 2 as before, and where D = {x ∈ X 4 | γ(x1) =
γ(x2) = γ(x3) = γ(x4)} = (γ4)−1(∆(R 2)4) parametrises the set of degenerate inscribed squares.
We call the self-intersections of γ crossings. These crossings together with the connecting arcs of γ form
a planar graph, which is 4-regular. Hence its dual graph is bipartite, which means that we can (uniquely)
color the components of the complement of γ in black and white such that adjacent components obtain
diﬀerent colors and such that the unbounded component is white. This is sometimes called a chequerboard
coloring of the complement of γ, see Figure 8. Let b(γ) be the number of black components. We say that
a crossing is fat if the black angles at this crossing are larger than 90◦. The fat crossings in Figure 8 are
marked with black dots. Let f (γ) be the number of fat crossings.

Theorem 3.1. Suppose that γ is an immersion of a closed 1-manifold in the plane that is generic in
the above sense. Then the number of non-degenerate squares inscribed in γ is congruent to b(γ) + f (γ)
modulo 2.
 11

Figure 8: Chequerboard coloring associated to γ. Dots mark the fat crossings.

Proof. By genericity of the curve, no inscribed square will have a vertex at a crossing. Thus at each
crossing c we can ﬁnd a neighborhood Nc ⊂ R 2 of c that contains no vertex of a non-degenerate inscribed
square of γ and in which γ is C2-close to two intersecting straight line segments. We may deform γ slightly
(in the C1-sense) within each Nc, such that in a suitably smaller neighborhood N ′
c of c, γ becomes the
intersection of two such straight line segments with the same intersection angle. If N ′
c is small enough, the
set of non-degenerate inscribed squares stays invariant: Inscribed squares with parameter 4-tuple close
to D cannot appear due to the smoothness of γ; others don’t appear due to the continuity of t and the
smallness of N ′
c.
Next, at each crossing c we perform a surgery as in Figure 9 in a suﬃciently small neighborhood
N ′′
c ⊂ N ′
c of c, smoothening the crossing with two convex arcs in such a way that the white angles open
up. In this way, all white components merge into one unbounded component, and the number of black
component stays invariant.
We need to study how the surgery changes the number of inscribed squares: Non-degenerate squares
that were inscribed before the surgery stay inscribed. New inscribed squares must have at least one vertex
in N ′′
c for some c. We argue that in fact all four vertices lie in N ′
c: If not, then the 4-tuple parametrising
this square is bounded away from D, and hence by continuity of t we may assume that all N ′′
c were chosen
small enough so that such a new square could not have appeared after the surgery. It remains to consider
newly inscribed squares with all four vertices in some N ′
c. Such a square appears in N ′
c if and only if the
black angle at c is larger than 90◦, in which case the square is unique (see Figure 9): If the two arcs are
arcs of an ellipse, this is an elementary but technical calculation, which we omit.
Thus, during the surgery, the number of inscribed squares increases by f (γ). The new curve consists of
b(γ) separated simple closed curves. We can deform them by an ambient isotopy such that they become
b(γ) suﬃciently small ellipses with mid-points aligned on a ﬁxed line with suﬃciently large distance
between them, such that there is trivially no inscribed square with vertices in more than one component.
Therefore the resulting union of ellipses inscribes exactly b(γ) squares. Using a bordism argument as in
Section 2.2, the parity of the number of inscribes squares did not change during the isotopy. Since every
ellipse inscribes exactly one square, this ﬁnishes the proof.
 vs.

Figure 9: When we smoothen a non-orthogonal straight line crossing then a new square appears if and
only if we opened the smaller angle.

3.2 Rectangles inscribed in immersed curves

The analog theorem for rectangles of prescribed aspect ratio 0 < r < 1 that are inscribed in an immersed
closed 1-manifold is slightly diﬀerent. Let 0 < α(r) < π/2 be the intersection angle of the two diagonals
of a rectangle with aspect ratio r. Let γ be a generic immersion of a ﬁnite union of circles in the plane,
and consider again the chequerboard coloring from above. Here, generic means that (i) all crossings are
transversal with intersection angles are neither α(r) nor π − α(r), (ii) the test map tr : X 4\D → R 4

with the same formula as in (5) is transversal to (0, 0, r) (i.e. all non-degenerate inscribed rectangles with

12

aspect ratio r are generic), and (iii) no (non-degenerate) inscribed rectangle with aspect ratio r has a
vertex at a self-intersection point of γ.
We call a crossing of γ α-orthogonal , if its angle lies in the interval (α, π − α). Let o(γ, r) denote the
number of α(r)-orthogonal crossings.

Theorem 3.2. Let 0 < r < 1. Suppose that γ is a generic immersion of a closed 1-manifold in the
plane. Then the number of non-degenerate rectangles with aspect ratio r inscribed in γ is congruent to
b(γ) + o(γ, r) modulo 2.

Proof. The proof is analogous to the one of Theorem 3.1. The only diﬀerence is that when we smoothen
the crossing, then zero, one, or two new rectangles will appear, depending on whether the angle β that
we smoothen satisﬁes β < α, α < β < π − α, or π − α < β; compare with Figure 10.

α

Figure 10: Smoothening a crossing changes the parity of the number of inscribed rectangles with aspect
ratio r if and only if the crossing is α-orthogonal.

4 Inscribed rectangles

The Rectangular Peg Problem, Theorem 1.2, was a very challenging and from the author’s point of view
the most beautiful open problem2 in this area of inscribing and circumscribing problems.
Griﬃths [12] gave a proof, however there are unfortunately some errors in his computation concerning
orientations (see [26, Chap. III.7] for details). Hence the problem is open.
In Section 4.1 we show that the standard topological approach, the conﬁguration space/test map
scheme, fails to prove the Rectangular Peg Problem since the test map in question exists. Then we prove
Theorem 1.5 under some technical assumptions concerning transversality; see Section 4.3. We show in
Section 4.4 that these assumptions can be made. These technicalities seem not to be obvious in advance
for two reasons: The natural group action on one solution manifold (namely P ) is in general not free;
and transversality has to be achieved for several maps simultaneously since we need to relate solution
manifolds of diﬀerent maps in the proof.

4.1 The test map exists

In this section we show that a standard topological approach, called conﬁguration space/test map method,
does not work to prove the Rectangular Peg Problem 1.5.
Assume we are given a smooth simple closed planar curve γ : S1 ↪→ R 2. As above let P ◦
4 ⊂ (S1)4 be
the set of four pairwise distinct points on the circle that lie counter-clockwise on it. Then P ◦
4 ∼= S1 ×(σ3)◦,
where (σ3)◦ denotes the interiour of the 3-simplex. We construct from γ a natural test map,

t : P ◦
4 −→ R 2 × R × R ,

[x1, x2, x3, x4] ↦−→ (v, ℓ, a), (5)

where v is the diﬀerence between the midpoints of the diagonals in the quadrilateral with vertices
γ(x1), . . . , γ(x4); ℓ is the diﬀerence of the length of these diagonals, and a is the aspect ratio.
We let Z /2 = {0, ε2} ⊂ Z /4 act on P ◦
4 by ε2 · [x1, x2, x3, x4] = [x3, x4, x1, x2]. The map t is then Z /2-
equivariant with respect to the corresponding group action on R 4. Since γ is smooth, there is an ε > 0,

2Update: see Section 1.2.
 13

such that t maps no point of B := U[ε](∂(P ◦
4 )) ∩ P ◦
4 to zero, where U[ε] denotes the closed ε-neighborhood
and ∂P ◦
4 the topological boundary of P ◦
4 ⊂ P4. The map t|B : B → R 4\{0} is uniquely given up to Z /2-
homotopy. R := t−1(0, 0, r) is the set of rectangles of aspect ratio r whose vertices lie counter-clockwise
on γ. R is generically a zero-dimensional free Z /2-manifold. Using the preimage orientation for R, Z /2
acts orientation preserving on R. Therefore R determines an element [R] in the oriented zero-dimensional
bordism group Ω0(P ◦
4 /Z /2) ∼= Z , which is the primary obstruction for extending t|U : U → R 4\{0} to a
map P ◦
4 → R 4\{0}. If γ is an ellipse then R consists of two orbits, since an ellipse inscribes exactly two
rectangles. A computation shows that their orientation is opposite, see [25]. Therefore [R] = 0 and the
obstruction class vanishes. Since this is the only obstruction, we can ﬁnd a map t′ : P ◦
4 → R 4\{0} such
that t′|B = t|B. That is there is no purely topological argument that can show the existence of a rectangle
of aspect ratio r on γ, at least as long as we are not using more geometric information.
The smooth Square Peg Problem can be solved using this conﬁguration space/test map scheme, since
squares have more symmetry. Here the group of symmetry is Z /4 and on an ellipse we ﬁnd only one
Z /4-orbit of squares.

4.2 Topological criteria

Above we saw that due to the lack enough symmetry, purely topological arguments will not work to
prove the Rectangular Peg Problem. But they give some intuition, here are two approaches. Assuming
that Theorem 1.2 admitted a counter-example (γ, r), both lemmas derive conclusions that seem to be
unintuitive, but more geometric ideas are needed to yield a contradiction.
If α : S1 → P ◦
4 is a one-parameter family of quadrilaterals, then we call [p1 ◦ α] ∈ π1(S1) = Z its
winding number, where p1 : P ◦
4 → S1 denotes the projection to the ﬁrst coordinate.

Lemma 4.1. Suppose there was a counter-example (γ, r) for the (smooth) Rectangular Peg Problem.
Then for all ε > 0, there is a Z /2-invariant one-parameter family S1 → P ◦
4 of ε-close parallelograms with
aspect ratio in [r − ε, r + ε] and with an odd winding number, such that during the whole one-parameter
family one of the diagonals stays larger than the other one.

Proof. Given γ, r and ε as in the lemma, let εn := ε/n for some n ≥ 1. Consider the Z /2-equivariant test
map g : P ◦
4 −→ R 2 × R

[x1, x2, x3, x4] ↦−→ ((γ(x1) + γ(x3)) − (γ(x2) + γ(x4)),

(||γ(x1) − γ(x2)|| + ||γ(x3) − γ(x4)||)−

r · (||γ(x2) − γ(x3)|| + ||γ(x4) − γ(x1)||)).

The preimage P = (g|P ◦
4 )−1(0) of the ﬁxed point 0 is the Z /2-invariant set of inscribed parallelograms
of aspect ratio r whose vertices lie cyclically on γ. As γ is smooth, ∂P ◦
4 has a closed neighborhood N
in P4 that does not intersect P . As Z /2 acts moreover freely on P ◦
4 , we can deform g by an equivariant
εn-homotopy relative to N to a new map g′ : P ◦
4 → R 3 that is transversal to 0. Its preimage P ′ = g′−1(0)
becomes a one-dimensional compact Z /2-manifold of εn-close inscribed parallelograms. The bordism
argument of Section 2.2 carries over to show that [P ′/Z /2] ∈ MO1(P ◦
4 /Z /2) = MO1(S1/Z /2) = Z /2
represents the same element as P does when γ is the unit circle, and thus this element is the generator
of Z /2. Let C be a component of P ′. If C is not Z /2-invariant, then [(Z /2·C)/Z /2] is 0 in MO1(P ◦
4 /Z /2). If
C is Z /2-invariant, then [C/Z /2] is the generator of MO1(P ◦
4 /Z /2) if and only if the winding number of C is
odd. Thus P ′ has an odd number of Z /2-invariant components with odd winding number. Consider such
a component C. If for some n, along the one-parameter family of εn-close parallelograms parametrised
by C, one diagonal stays always longer than the other, then the lemma is proved.
Otherwise for each n, by the intermediate value theorem at least one of these quadrilaterals must
be an εn-close rectangle Rn. As γ is smooth, (Rn)n can be uniformly bounded away from ∂P ◦
4 . Thus
some convergent subsequence of (Rn)n converges to a non-degenerate inscribed rectangle of aspect ratio r,
which is a contradiction.
 14

Remark 4.2. In Lemma 4.1, instead of considering the set of parallelograms with aspect ratio r, we
might look as well on the set of parallelograms whose diagonals intersect in an angle α, where α is the
intersection angle of the diagonals in a rectangle of aspect ratio r. This gives an analogous lemma, which
might be easier to deal with geometrically.

Lemma 4.3. Suppose there was a counter-example (γ, r). Then for all ε > 0, there is a Z /4-invariant
one-parameter family S1 → P ◦
4 of ε-close rectangles.

Proof. Let f : P ◦
4 −→Z /4 R 4 × R 2 be the restricted map (1) from Section 2.2, measuring the edges and
diagonals of inscribed quadrilaterals.
First, make f Z /4-equivariantly transversal to ∆ = ∆R 4 × ∆R 2 by a small δ-homotopy, where δ is a
positive function that decreases suﬃciently fast near the boundary of P ◦
4 , and let Q := f −1(∆) be the
set of all squares (as measured with an error bounded by δ). Then make f Z /4-equivariantly transversal
to the Z /4-invariant subspace ∆′ := {(a, b, a, b, e, e) ∈ R 4 × R 2} by a small δ-homotopy which leaves Q
ﬁxed, and let R := f −1(∆′). If δ was chosen small enough in terms of a given ε > 0, R parametrises
inscribed ε-close rectangles.
Let RQ be the set of all components of R that contain a square. We may assume that all these
components are circles, otherwise a component would come arbitrary close to the boundary of P ◦
4 , so
there would be an ε-close rectangle on it with aspect ratio r. If we could do this for all ε, then a limit
argument would give us a proper rectangle of aspect ratio r. So if need be, we choose a smaller ε for
which this does not happen.
R is a one-dimensional Z /4-manifold, so Z /4 acts on RQ as well. We decompose RQ = R1 ˙∪R2 ˙∪R4,
where R1 is the set of components with isotropy group ⟨0⟩, R2 with isotropy group Z /2 = ⟨ε2⟩ ⊂ Z /4
and R4 with Z /4. Now we only need to count the number of squares on each Ri.

• ♯Q = 4 mod 8, since modulo Z /4 it is odd (see Section 2.2).

• Every component C ∈ RQ contains an even number of squares, since while passing a square the
rectangle changes from fat to skinny or vice versa (this follows from the bijectivity of the diﬀerential
df at points in Q).

• 4 divides ♯R1, and every component in R1 contains an even number of squares. So the number of
squares in the components of R1 is divisible by 8.

• 2 divides ♯R2, and if a component in R2 contains a square S, then it inscribes also ε2 · S. When it
goes through a square and changes from fat to skinny, then so it does at ε2 · S. Hence it has to go
through 4k squares, k ≥ 1. Thus the total number of squares in the components of R2 is divisible
by 8.

• If a component C of R4 goes through a square S and changes from fat to skinny, then it also goes
through ε · S and changes from skinny to fat. That is, in between it had to go through an even
number of squares, all of which of course belong to a diﬀerent Z /4-orbit. Hence the number of
square-orbits on C is odd, ♯(Q ∩ C) = 4 mod 8.

Putting this modulo 8 together, we get ♯R4 = 1 mod 2, which is even a bit stronger than what is
stated in the lemma.

Remark 4.4. Another viewpoint for the proof of Lemma 4.3 is the following. As a 1-manifold, R is
a union of circles and segments. The endpoint of the segments correspond to degenerate rectangles.
These rectangles are either “skinny” or “fat”, and the segment s has either endpoints of the same type
or of diﬀerent type; we say that s type-preserving or type-reversing, respectively. This feature of s stays
invariant under the action of Z /4. One property is that type-preserving s contains an even number of
squares, and type-reversing s an odd number.
 15

By a bordism argument one can show that the number of type-reversing s mod Z /4 equals 1 plus
the number of Z /4-invariant circle components of R modulo 2. Moreover, type-reversing segments in R
contain rectangles of any aspect ratio. Thus this yields another proof of the lemma.

4.3 Inscribed rectangles with aspect ratio √3

In the case r = √3 there is a “hidden” symmetry that we will use to prove Theorem 1.5.

< −60
◦

Figure 11: Example of a curve that
is not 60◦-angular convex.
 γ(y2)

γ(y1)
 γ(z1)γ(z2)

γ(x1)
 γ(x2)

Figure 12: A star containing three 60◦-parallelograms;
x1z1x2z2 is skinny, the other two are fat.

We leave all technical details concerning transversality to the subsequent Section 4.4. Suppose we are
given a smooth curve γ : S1 ↪→ R 2. Deﬁne a map

f : (S1)
4 −→G R 2 × S1

(x1, x2, y1, y2) ↦−→ (v, α),

where v is again the diﬀerence of the diagonal midpoints in the quadrilateral (γ(x1), γ(y1), γ(x2), γ(y2))
and α is the mod-180◦ angle between these diagonals (we measure angles always in counter-clockwise
sense). If one diagonal is degenerate to a point we take the tangent of γ at this point to deﬁne α.
The map f is G-invariant, where G := Z /2 × Z /2 = {¯0x, ¯1x} × {¯0y, ¯1y} acts on (S1)4 by ¯1x ·
(x1, x2, y1, y2) = (x2, x1, y1, y2) and ¯1y · (x1, x2, y1, y2) = (x1, x2, y2, y1).
Let P := f −1(0, 60◦) be the set of inscribed parallelograms in γ having a 60◦-angle modulo 180◦

between their diagonals. We call them 60◦-parallelograms. We may assume that P is a union of connected
1-dimensional submanifolds Ki of (S1)4,

P = K1 ∪ . . . ∪ Kn, Ki ∼= S1.

P does not contain points (x1, x2, y1, y2) ∈ P with x1 = x2 or y1 = y2, since γ was assumed to be 60◦-
angular convex. Thus, G acts freely on P . We denote (S1)4/G = M 2 where M := (S1)2/Z /2 is the M¨obius
strip. The ﬁrst factor M parametrises x1 and x2 without their order and the second M parametrises y1
and y2. Let L1 ∪ . . . ∪ Lm ⊂ M 2 be the quotient manifold (
⋃ Ki)/G. Then L represents an element in the
1-dimensional unoriented bordism group MO1(M 2) ∼= MO1((S1)2) ∼= (Z /2)2, since all 60◦-angular convex
curves are isotopic in the plane and G-homotopies of f change K1 ∪ . . . ∪ Kn by a G-bordism.
If γ is the unit circle then we see that P is the disjoint union of two circles that get identiﬁed by G.
Their quotient L is one circle that represents (¯1, ¯1) ∈ MO1(M 2) ∼= (Z /2)2, where ¯1 ∈ Z /2 is the generator.
P does not contain parallelograms that have an edge that is degenerate to a point. Hence the x1
and x2-coordinates will always diﬀer from the y1 and y2-coordinates at any point (x1, x2, y1, y2) ∈ P .
Therefore the circles Li can only represent the elements (¯0, ¯0) and (¯1, ¯1) of MO1(M 2) ∼= (Z /2)2.
Now we come to the “hidden symmetry”, that is, the geometric piece of information that is the key
in this proof. Let W := {(α, β, γ) ∈ (S1)3 | α + β + γ = 0◦ mod 180◦}. We deﬁne a map

F : (S1)6 −→ (R 2)
3 × W

(x1, x2, y1, y2, z1, z2) ↦−→ (mx, my, mz, αyz, αzx, αxy),

16

where mx is the mid-point of the segment (γ(x1), γ(x2)), αyz is the mod-180◦-angle between the lines
through (γ(y1), γ(y2)) and (γ(z1), γ(z2)) (if y1 = y2, we take instead the tangent of γ at this point, and
analogously in case z1 = z2), and analogously for the the other coordinates. F is equivariant with respect
to the natural actions of the wreath product G′ := (Z /2)3 ⋊ Z 3. Let

̃S := F −1(∆(R 2)3 × {(60
◦, 60
◦, 60
◦)}).

We may assume that ̃S is a 0-dimensional free G′-manifold. We call S := ̃S/G′ the set of stars. Every
star s ∈ S contains three 60◦-parallelograms on γ, namely Pyz, Pzx and Pxz, see Figure 12. Modulo G
they lie in some components Li, Lj, and Lk (they are not necessarily pairwise distinct). We say that this
star s relates Li, Lj, and Lk. Saying this is unique up to cyclic permutation of Li, Lj, and Lk. So we can
draw a directed graph D (with possibly multiple arcs and loops) whose nodes are the components of L,
and we draw for each star a directed triangle Li → Lj → Lk → Li.
Assume that γ does not inscribe a rectangle of aspect ratio √3. These are exactly the rectangles
whose diagonals cross in a 60◦-angle. Then all 60◦-parallelograms on γ are skinny or fat in the sense that
the x-diagonal is longer or shorter than the y-diagonal, respectively. By continuity this does not change
along the components of L. Hence we can call the Li’s fat or skinny.
Along a component Ki, {x1, x2} and {y1, y2} never intersect: If they did, by mx = my and αxy = 60◦,
all four points would need to coincide, but at the tangent at that point of γ would also need to have
two directions, which diﬀer by 60◦, which is impossible. Thus for each i, [Li] ∈ MO1(M 2) is either (¯0, ¯0)
or (¯1, ¯1). Correspondingly, we say that the winding number w(Li) of Li is ¯0 (even) or ¯1 (odd), respectively.
Let x, y : M 2 → M be the projections to the ﬁrst and to the second factor, respectively. An arc Li →
Lj in the graph D corresponds to an intersection of y(Li) and x(Lj). The number of such intersections is

♯(y(Li) ∩ x(Lj)) = w(Li) · w(Lj) mod 2. (6)

We will derive a contradiction by double counting the number of stars ♯S.
By (6), components of L with even winding number will have no inﬂuence on what follows. Let s
be the number of skinny components of L with odd winding number, and let f be the number of fat
components of L with odd winding number.
We know that [L] = ∑
i[Li] = (¯1, ¯1), thus

s + f = 1 mod 2.

Note that no star relates three skinny or three fat 60◦-parallelograms with each other. Hence every star
gives exactly one arc from a skinny to a fat component of L. Modulo 2 and using (6), there are congruent
s · f = 0 mod 2 of these arcs. Therefore,
 ♯S = 0 mod 2.

On the other hand, every star relates three components, two of which are skinny or two of which are
fat. So every star gives exactly one arc between two skinny components or between two fat components.
Using (6), the number of arcs between skinny components modulo two is

s2 = s mod 2,

and the number of arcs between fat components modulo two is

f 2 = f mod 2.

Together this gives, ♯S = s + f = 1 mod 2.

This is a contradiction, which ﬁnishes the proof of Theorem 1.5.

17

4.4 Technical Details

In the previous section we assumed that the set of inscribed 60◦-parallelograms P is a 1-dimensional
manifold in the 4-manifold M 2. Also the set of stars should be ﬁnite. At the same time, when two
parallelograms p1 and p2 have a common diagonal y(p1) = x(p2) they form a star. Thus there should
be another parallelogram p3 such that x(p1) = y(p3) and y(p2) = x(p3). These triple intersection points
come from the geometry, but they are in some sense not generic. That is, we need to be careful on how
to make the test maps f and F simultaneously transversal in order to keep the geometric property of a
star and without violating the equivariance. We solve this issue by perturbing the following two maps.
Let m : (S1)
2 → R 2

be the map that sends (x1, x2) ∈ (S1)2 to the mid-point γ(x1)+γ(x2)
2 . Let

α : (S1)
2 → S1

be the map that sends (x1, x2) ∈ (S1)2 to the mod-180◦ angle of the line through γ(x1) and γ(x2) and
some ﬁxed line in the plane. The maps f and F can written in terms of m and α,

f (x1, x2, y1, y2) = (m(y1, y2) − m(x1, x2), α(y1, y2) − α(x1, x2))

and similarly F .
Let ϕi : S1 → [0, 1], i = 1 . . . k, be a partition of unity of S1 subordinate to a covering of S1 with
small ε-balls. We will perturb the maps m and α with two sets of parameters Sm := ([−ε, +ε]2)(
k+1
2 ) and
Sα := [−ε, +ε](
k+1
2 ) as follows:

m
′ : Sm × (S1)
2 −→ R 2

(sm, x1, x2) ↦−→ m(x1, x2) + ∑

i≤j (ϕi(x1)ϕj(x2) + ϕi(x2)ϕj(x1)) · (sm)i,j,

and α′ : Sα × (S1)2 −→ S1

(sα, x1, x2) ↦−→ α(x1, x2) + ∑

i≤j (ϕi(x1)ϕj(x2) + ϕi(x2)ϕj(x1)) · (sα)i,j,

This deﬁned analogous functions f ′ : Sm × Sα × (S1)4 −→G R 2 × S1 and F ′ : Sm × Sα × (S1)6 −→K
(R 2)3 × W . Because of the additional parameter space f ′ and F ′ are transversal to the respective test-
spaces {(0, 60◦)} and ∆(R 2)3 × {60◦, 60◦, 60◦}. By the transversality theorem [14, p. 68], for almost all
choices s := (sm, sα) (up to a zero set), the perturbations f ′
s := f ′(s, ) and F ′
s := F ′(s, ) are transversal
to the test-spaces as well. Similarly one can show that for almost all s, y(Ki) intersects x(Kj) transversally
for all i, j.

5 Inscribed crosspolytopes

In Klee & Wagon [20, Problem 11.5] is was asked whether every 3-dimensional convex body circumscribes
the vertices of a regular octahedron. Makeev [23] proved this for smooth convex bodies and Karasev [18]
generalised the proof to smoothly embedded spheres in higher dimensions as follows.

Theorem 5.1 (Makeev, Karasev). Let d be an odd prime power. Then every smooth embedding Γ :
Sd−1 → R d contains the vertices of a regular d-dimensional crosspolytope.

18

In 1965 H. Guggenheimer [13] gave already a proof for all d, however there is unfortunately an error
in his main lemma due to some connectivity arguments, which seems to invalidate the proof. Recently,
Akopyan and Karasev [2] proved by a careful and non-trivial approximation argument that for d = 3, the
smooth embedding Γ can be replaced by the boundary of a simple polytope.
An interesting possible extension seems to be the following. Let M be a Riemann manifold. By
an inscribed crosspolytope P in M we mean a set of 2d pairwise distinct points vε
i ∈ M , ε ∈ {+, −},
i ∈ {1, . . . , d}. We call two vertices vε
i and vδ
j opposite if i = j and ε = −δ. If any pair of non-opposite
vertices of P have the same distance in M then we call P a regular crosspolytope.

Conjecture 5.2 (“Crosspolytopal peg problem for manifolds”). Let d be a positive integer. Then every
smooth embedding Γ : Sd−1 → M into a Riemann manifold contains the vertices of a regular d-dimensional
crosspolytope.

The aim of this section is to show that the conjecture in general is probably very diﬃcult.

The topological counter-example. A solution of the conjecture would involve deeper geometric
reasoning, since there is the following “topological counter-example” for d = 3. Suppose we are given a
smooth embedding Γ : S2 → M . Let G ∼= (Z /2)3 ⋊ S3 be the symmetry group of the regular octahedron
and Gor ⊂ G be the subgroup of orientation preserving symmetries. G acts on (S2)6 by permuting the
coordinates in the same way as it permutes the vertices of the regular octahedron. Let G act on R 12

by permuting the coordinates in the same way as it permutes the edges of the regular octahedron. The
subrepresentation (∆R 12)⊥ ⊂ R 12 is denoted by Y . Let ∆fat
(S2)6 be the space of all 6-tuples in (S2)6 that

contain at least two equal elements, that is, the fat diagonal. Let B be a small ε-neighborhood of ∆fat
(S2)6,
where ε depends only on an isotopy of Γ to some nice embedding, that we will describe later. Then the
complement X := (S2)6\B is a free compact G-manifold with boundary and

X ≃G {(x1, . . . , x6) ∈ (S2)6 | xi are pairwise distinct} = (S2)
6\∆fat
(S2)6.

Then Γ induces a test map t : X −→G Y,

which measures the lengths of the edges of the parametrised octahedra modulo 1 = (1, . . . , 1). This map
depends only on the distance function d : M × M → R on M . Since ε was chosen to be small, t|∂X
maps into Y \{0} and this map is unique up to G-homotopy. We will use this fact later to assume that
Γ is actually some nice embedding of Sd−1 into R d. The solution set S of regular octahedra inscribed in
Γ, in the sense that all edge lengths coincide, is S := t−1(0). The subset Sor ⊂ S of positively oriented
inscribed octahedra is a part of the preimage t−1(0), and t induces an isomorphism of Gor-vector bundles
over Sor, T Sor ⊕ (iSor)
∗(X × Y ) ∼= (iSor)
∗(T X),

where iSor denotes the inclusion Sor ↪→ X, and X × Y is considered as the trivial vector bundle over
X with ﬁber Y . Thus Sor together with this normal data represents an element [Sor] in the equivariant
normal bordism group (see Koschorke [21, Chap. 2])

ΩGor
1 (X, X × Y − T X) = Ω1(X/Gor, X ×Gor Y − T (X/Gor)),

which is well-deﬁned, since Z /2-homotopies of d relative to a small neighborhood of ∆M 2 change S only
by a normal bordism that stays away from the ∂X if ε was chosen small enough, and components of
octahedra of diﬀerent orientation are always separated from each other. In Koschorke’s notation, [Sor] is
the obstruction ̃ω1(R
∼, X ×Gor Y, (id∂X , t|∂X )/Gor),

where R
∼ denotes the trivial line bundle.
 19

Theorem 5.3. The above deﬁned [Sor] is zero. Hence

[S] ∈ Ω
G
1 (X, X × Y − T X)

is zero as well. In particular, the test map t can be deformed G-equivariantly relative to ∂X to a map t′,
such that 0 ̸∈ t′(X).

The existence of the test map t′ that fulﬁlls the boundary conditions is what we call a topological
counter-example.

Sketch of Proof. To construct a convenient representative for [Sor] we take for Γ a parametrisation of the
ellipsoid {(x, y, z) | x2 + y2 + 2z2 = 8}, which has a rotational symmetry about the z-axis. We let t and S
be the corresponding test map and solution set, respectively. We compute S explicitly as a real algebraic
variety; the relevant SageMath script is available at [25]. One inscribed regular octahedron has the six
vertices ±(2, 0, √
2) and ±(1, ±
√3, −
√2). If we rotate this octahedron around the z-axis then we get up
to symmetry all inscribed octahedra in Γ, and S is a disjoint union of 16 = 1
3 · ♯G circles; see Figure 13.

Figure 13: Orthogonal projection of Γ into the xy-plane together with an inscribed regular octahedron.

The G-bundles X × Y and T X are G-orientable. Therefore the relevant part of Koschorke’s exact
sequence [21, Thm. 9.3] becomes

H2(X/Gor; Z ) → Z /2 → Ω1(X/Gor,X ×Gor Y − T (X/Gor))

→ H1(X/Gor; Z ) → 0.

It is not diﬃcult to see that the image of [Sor] in H1(X/Gor; Z ) = H1(Gor; Z ) is zero. This is because
the 120 degrees rotation of a regular octahedron about the line connecting the midpoints of two opposite
triangles is an element of the commutator of Gor. It requires more visualisation to see that [Sor] is in
fact the image of the generator of Z /2. The hard part is to show that Z /2 unfortunately lies in the
image of H2(X/Gor; Z ), which we computed with a rather long computer program, see [25]. It ﬁnds that
H2(X/Gor; Z ) ∼= Z /4 × (Z /2)3, where one can choose the generators such that the ﬁrst three map to zero
and the last one to the generator of Z /2.
The Gor-null-bordism of Sor can be extended to a G-null-bordism of S. By Theorem 3.1 of Koschorke
[21], we can extend the section as stated.

Remarks to the algorithm. An economical S6-CW-complex structure on (S2)6 is based on an S6-cell
decomposition of R 2 of Fuks [9] and Vassiliev [40], which has few high dimensional cells. ∆fat
(S2)6 is a
subcomplex, so one can compute

H2(X/Gor) ∼= H 10((S2)
6/Gor, (∆fat
(S2)6)/Gor).

The Smith normal form is used to compute this cellular cohomology and the LLL-algorithm to choose
economical generators. The image in Z /2 is determined by computing second Stiefel-Whitney classes,
which have been implemented as obstruction classes.

20

Acknowledgements

I want to thank to Karim Adiprasito, Ulrich Bauer, Pavle Blagojevi´c, Jason Cantarella, Roman Karasev,
Sergey Melikhov, Carsten Schultz, John Sullivan, Helge Tverberg, Siniˇsa Vre´cica, G¨unter Ziegler, Aleksey
Zinger, and Rade ˇZivaljevi´c for many very useful discussions. Moreover I thank the referees for very
valuable comments and questions.
This work was supported by Studienstiftung des dt. Volkes and Deutsche Telekom Stiftung at Tech-
nische and at Freie Universit¨at Berlin, NSF Grant DMS-0635607 at Institute for Advanced Study, by
an EPDI fellowship at Institut des Hautes Etudes Scientiﬁques, Forschungsinstitut f¨ur Mathematik, and
Isaac Newton Institute, by Max Planck Institute for Mathematics Bonn, and by Simons Foundation grant
#550023 at Boston University.

References

[1] Arseniy Akopyan and Sergey Avvakumov. Any cyclic quadrilateral can be inscribed in any closed convex
smooth curve. arXiv:1712.10205, 2017.
[2] Arseniy Akopyan and Roman N. Karasev. Inscribing a regular octahedron into polytopes. Discrete Math.,
313(1):122–128, 2013.
[3] Jason Cantarella. Webpage on the square peg problem. http://www.jasoncantarella.com/webpage/index.php?
title=Square Peg problem, 2008.
[4] Jason Cantarella, Elizabeth Denne, and John McCleary. Transversality in Conﬁguration Spaces and the
“Square-Peg” Problem. arXiv:1402.6174, 2014.
[5] Carl Marius Christensen. A square inscribed in a convex ﬁgure (in Danish). Matematisk Tidsskrift B, 1950:22–
26, 1950.
[6] Arnold Emch. Some properties of closed convex curves in a plane. Amer. J. Math, 35:407–412, 1913.
[7] Arnold Emch. On the medians of a closed convex polygon. Amer. J. Math, 37:19–28, 1915.
[8] Arnold Emch. On some properties of the medians of closed continuous curves formed by analytic arcs. Amer.
J. Math., 38(1):6–18, 1916.
[9] Dmitry. B. Fuks. Cohomology of the braid group mod 2. Functional Anal. Appl., 24:143–151, 1970.
[10] Joshua E. Greene and Andrew Lobb. Cyclic quadrilaterals and smooth Jordan curves. arXiv:2011.05216, 2020.
[11] Joshua E. Greene and Andrew Lobb. The Rectangular Peg Problem. arXiv:2005.09193, 2020.
[12] H. Brian Griﬃths. The topology of square pegs in round holes. Proc. London Math. Soc., 62(3):647–672, 1990.
[13] Heinrich W. Guggenheimer. Finite sets on curves and surfaces. Israel J. Math., 3:104–112, 1965.
[14] Victor Guillemin and Alan Pollack. Diﬀerential topology. Prentice Hall, 1974.
[15] Clarence M. Hebbert. The inscribed and circumscribed squares of a quadrilateral and their signiﬁcance in
kinematic geometry. Ann. of Math. (2), 16(1-4):38–42, 1914/15.
[16] Wouter van Heijst, 2014. Master thesis, in preparation.
[17] Richard P. Jerrard. Inscribed squares in plane curves. Trans. Amer. Math. Soc., 98:234–241, 1961.
[18] Roman N. Karasev. Inscribing a regular crosspolytope. arXiv:0905.2671, 2009.
[19] Roman N. Karasev. A note on Makeev’s conjectures. J. Math. Sci., 212(5):521–526, 2016.
[20] Victor Klee and Stan Wagon. Old and new unsolved problems in plane geometry and number theory. Dolciani
Mathematical Expositions. The Math. Ass. America, 1996.
[21] Ulrich Koschorke. Vector Fields and Other Vector Bundle Morphisms - A Singularity Approach, volume 847
of Lecture Notes in Math. Springer, 1981.
[22] Vladimir V. Makeev. On quadrangles inscribed in a closed curve. Math. Notes, 57(1-2):91–93, 1995.
[23] Vladimir V. Makeev. Universally inscribed and outscribed polytopes. PhD thesis, Saint-Petersburg State
University, 2003.
[24] Vladimir V. Makeev. On quadrangles inscribed in a closed curve and the vertices of the curve. J. Math. Sci.,
131(1):5395–5400, 2005.
[25] Benjamin Matschke. https://github.com/bmatschke/on-the-square-peg-problem.
[26] Benjamin Matschke. Equivariant topology and applications. Diploma thesis, TU Berlin, 2008.
[27] Benjamin Matschke. Square pegs and beyond. In Oberwolfach Reports, volume 2, pages 51–54, 2009. (extended
abstract).
[28] Benjamin Matschke. Equivariant topology methods in discrete geometry. PhD thesis, Freie Universit¨at Berlin,
2011.
 21

[29] Benjamin Matschke. A survey on the square peg problem. Notices Amer. Math. Soc., 61(4):346–352, 2014.
[30] Benjamin Matschke. Quadrilaterals inscribed in convex curves. arXiv:1801.01945, 2018.
[31] Mark J. Nielsen and Stephen E. Wright. Rectangles inscribed in symmetric continua. Geom. Dedicata,
56(3):285–297, 1995.
[32] Igor Pak. Lectures on Discrete and Polyhedral Geometry. http://www.math.ucla.edu/∼pak/book.htm, 2010.
[33] Ville H. Pettersson, Helge A. Tverberg, and Patric R. J. ¨Osterg˚ard. A note on Toeplitz’ conjecture. Discrete
Comput. Geom., 51(3):722–728, 2014.
[34] Feli´u Sagols and Ra´ul Mar´ın. The inscribed square conjecture in the digital plane. In Combinatorial image
analysis, volume 5852 of Lecture Notes in Comput. Sci., pages 411–424. Springer, 2009.
[35] Feli´u Sagols and Ra´ul Mar´ın. Two discrete versions of the inscribed square conjecture and some related
problems. Theoret. Comput. Sci., 412(15):1301–1312, 2011.
[36] Lev G. Schnirelman. On some geometric properties of closed curves. (in Russian) Usp. Mat. Nauk, 10:34–44,
1944. Available at http://ega-math.narod.ru/Nquant/Square.djv. Posthumous reproduction and extension of
the author’s original article in Sbornik Rabot Matematiˇceskogo Razdela Sekcii Estestvennyh i Toˇcnyh Nauk
Komakademii, Moscow, 1929.
[37] Walter R. Stromquist. Inscribed squares and square-like quadrilaterals in closed curves. Mathematika, 36:187–
197, 1989.
[38] Terence Tao. An integration approach to the Toeplitz square peg problem. Forum Math. Sigma, 5:e30, 63 pp,
2017.
[39] Otto Toeplitz. Ueber einige Aufgaben der Analysis situs. Verhandlungen der Schweizerischen Naturforschenden
Gesellschaft in Solothurn, 4:197, 1911.
[40] Victor A. Vassiliev. Braid group cohomologies and algorithm complexity. Functional Anal. Appl., 22:182–190,
1988.
[41] Siniˇsa Vre´cica and Rade T. ˇZivaljevi´c. Fulton–MacPherson compactiﬁcation, cyclohedra, and the polygonal
pegs problem. Israel J. Math., 184(1):221–249, 2011.
[42] Konrad Zindler. ¨Uber konvexe Gebilde. Monatshefte f¨ur Mathematik und Physik, 31:25–56, 1921.

Boston University
matschke@bu.edu
 22
