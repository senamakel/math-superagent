<!-- source: https://pub.math.leidenuniv.nl/~luijkrmvan/cubics/cubics.pdf | converted from PDF -->

CUBIC POINTS ON CUBIC CURVES AND THE
BRAUER-MANIN OBSTRUCTION ON K3 SURFACES

RONALD VAN LUIJK

Abstract. We show that if over some number ﬁeld there exists a certain
diagonal plane cubic curve that is locally solvable everywhere, but that does
not have points over any cubic galois extension of the number ﬁeld, then the
algebraic part of the Brauer-Manin obstruction is not the only obstruction to
the Hasse principle for K3 surfaces.

1. Introduction

If we want to prove that a variety X deﬁned over the ﬁeld of rational numbers
Q does not have any rational points, it suﬃces to show that X has no real points
or no p-adic points for some prime number p. For some varieties the converse
holds as well. Conics, for instance, have a rational point if and only if they have
a real point and a p-adic point for every prime p, i.e., if and only if they have a
point locally everywhere. This is phrased by saying that conics satisfy the Hasse
principle. Selmer’s famous example of the plane curve given by

(1) 3x
3 + 4y3 + 5z3 = 0

shows that cubic curves in general do not satisfy the Hasse principle, as this smooth
curve has points everywhere locally, but it has no points over Q (see [20]).
Some varieties with points locally everywhere have no global points because of
the socalled Brauer-Manin obstruction to the Hasse principle. This obstruction
is based on the Brauer group of the variety. We refer to [25], section 5.2, for a
good description of this obstruction. The main idea is the following. For a smooth,
projective, geometrically integral variety X over a number ﬁeld k, the set X(Ak)
of adelic points on X equals the product ∏
v X(kv), where v runs over all places of
k and kv denotes the completion of k at v. This product is nonempty if and only
if X has points locally everywhere. Based on class ﬁeld theory, one associates to
each element g in the Brauer group Br X of X a certain subset X(Ak)
g of X(Ak)
that contains the set X(k) of k-points on X, embedded diagonally in X(Ak). We
say there is a Brauer-Manin obstruction to the Hasse principle if X(Ak) ̸= ∅, but
for some subset B ⊂ Br(X) we have ⋂
g∈B X(Ak)
g = ∅, and thus X(k) = ∅. Often
one focuses on the set B = Br1 X of socalled algebraic elements, deﬁned as the
kernel of the map Br X → Br Xk, where k denotes an algebraic closure of k. These
algebraic elements are relatively easy to get our hands on.
For certain classes of varieties the Brauer-Manin obstruction is the only obstruc-
tion to the Hasse principle. For a cubic curve C with ﬁnite Tate-Shafarevich group,
for instance, it is indeed true that if C has points locally everywhere and there is no

2000 Mathematics Subject Classiﬁcation. 11G05, 14J28, 14C22.
Key words and phrases. K3 surfaces, abelian points, cubic curves, Brauer-Manin obstruction.

1

2 RONALD VAN LUIJK

Brauer-Manin obstruction, then C contains a rational point (see [12], or [25], Thm.
6.2.3). It is conjectured that the Brauer-Manin obstruction is the only obstruction
to the Hasse principle on all curves of genus at least 2 and all smooth, proper,
geometrically integral, rationally connected varieties over number ﬁelds (see [18]
and [5], p. 3).
For K3 surfaces, however, it is not at all clear whether the Brauer-Manin ob-
struction is the only one. Even if in general this is not the case, it could still be true
for special K3 surfaces, such as singular K3 surfaces, which are those with maximal
Picard number 20. A priori, it could be true that the algebraic part already gives
an obstruction, if there is any.
In this paper, a k-cubic point is a point deﬁned over some galois (Z/3Z)-extension
of k. Our main theorem states the following.

Theorem 1.1. Let k be a number ﬁeld. Suppose we have a smooth curve C ⊂ P2
k
given by ax
3 + by3 + cz3 = 0, such that

(1) the product abc is not a cube in k,
(2) the curve C has points locally everywhere,
(3) the curve C has no k-cubic points.

Then there exists a quotient of C × C, deﬁned over k, such that its minimal desin-
gularization Y is a singular K3 surface satisfying Y (Ak)
Br1 Y ̸= ∅ and Y (k) = ∅.

In other words, if a certain cubic curve exists, then the Brauer-Manin obstruction
coming from the algebraic part of the Brauer group is not the only obstruction to
the Hasse principle for singular K3 surfaces, let alone for K3 surfaces in general.
The existence of any plane cubic curve satisfying the third condition in Theorem
1.1 is unknown and an interesting object of study by itself. The curve given by (1)
satisﬁes the ﬁrst two conditions mentioned in Theorem 1.1. Several people have
wondered whether it satisﬁes the third condition as well. It turns out that this is
not the case, as the intersection points of that curve with the lines

711x + 172y + 785z = 0,

657x + 124y + 815z = 0,
4329x + 3988y + 2495z = 0

are all Q-cubic points.
In the following section we will construct the quotient X of the surface C × C
associated to a general plane cubic C that will be used in the proof of Theorem 1.1.
We give explicit equations in the case of diagonal cubics and cubics in Weierstrass
form and discuss some of the arithmetic properties of X and its desingularization Y .
In section 3 we will go deeper into the geometry in the case that k has characteristic
0 and investigate the N´eron-Severi group of Y . In section 4 we will prove the main
theorem. The fact that there is no Brauer-Manin obstruction will follow from the
fact that Br1 Y is isomorphic to Br k, which never yields an obstruction. Some
related open problems are stated in the last section.
The author would like to thank Hershy Kisilevsky, Michael Stoll, Bjorn Poonen,
and Bas Edixhoven for helpful discussions and suggestions. He also thanks Uni-
versidad de los Andes, PIMS, University of British Columbia, and Simon Fraser
University for their support.

CUBIC POINTS AND THE BRAUER-MANIN OBSTRUCTION ON K3 SURFACES 3

2. A K3 surface associated to a plane cubic curve

Let k be any ﬁeld of characteristic not equal to 2 or 3, and C any smooth
projective cubic curve in P2
k. We extend the regular notion of collinearity by saying
that any three points P, Q, and R on C are collinear if the divisor (P ) + (Q) + (R)
is linearly equivalent with a line section of C. By Bezout’s theorem we know that
for any two points P and Q on C there is a unique third point R on C such that
P, Q, and R are collinear. If P equals Q, then R is the “third” intersection point
of C with the tangent to C at P . This yields a natural isomorphism

(2) C × C ∼ { (P, Q, R) ∈ C 3 : P , Q, and R are collinear }.

Let ρ be the automorphism of C ×C that sends (P, Q) to (Q, R), where P, Q, and R
are collinear. Under the identiﬁcation of (2) this corresponds to sending (P, Q, R)
to (Q, R, P ). Clearly ρ has order 3. We let XC denote the quotient (C × C)/ρ, and
write X = XC if C is understood. Let π : C × C → X denote the quotient map.
The surface XC is the quotient mentioned in Theorem 1.1. It is also used in [7],
where the number of rational points on XC is related to random matrix theory.
The ﬁxed points of ρ are exactly the nine points (P, P ) where P runs through
the ﬂexes of C. Let P be such a ﬂex and let r and s be two copies of a uniformizer
at P . Then modulo the square of the maximal ideal at (P, P ) in C × C, the
automorphism ρ is given by (r, s) ↦→ (s, t) with t = −r − s, c.f. [23], p. 115. The
subring of k[r, s] of invariants under the automorphism (r, s) ↦→ (s, t) is generated
as k-algebra by a = −rs − rt − st = r2 + rs + s2, b = 3rst = −3rs(r + s), and
c = r2s + s
2t + t2r = r3 + 3r2s − s
3. They satisfy the equation a
3 = b2 + bc + c
2,
which locally describes the corresponding singularity on XC up to higher degree
terms, which do not change the type of singularity. We conclude that XC has
nine singular points, all double points. Each is resolved after one blow-up, with
two smooth (−2)-curves above it, intersecting each other in one point. Let YC
denote the blow-up of XC in its singular points. Again, we write Y = YC if C is
understood. As the singular locus of X is deﬁned over k, so is Y .

Deﬁnition 2.1. A K3 surface over k is a smooth, projective, geometrically integral
surface Z over k with trivial canonical sheaf, for which H 1(Z, OZ ) = 0.

Proposition 2.2. The surface Y is a smooth K3 surface.

Proof. We have seen that ρ only has isolated ﬁxed points. The corresponding singu-
larities are A2-singularities, which are rational double points. From the symmetry
of the right-hand side of (2), it follows that ρ ﬁxes the unique (up to scaling) non-
vanishing regular diﬀerential of C × C. By [11], Thm. 2.4, these conditions imply
that a relatively minimal model of X is a K3 surface. By [11], Lemma 2.7, this
model is isomorphic to the minimal resolution Y of X. □

We now discuss some of the arithmetic properties of X and Y .

Lemma 2.3. The surface X has a k-rational point if and only if Y does.

Proof. Any k-rational point of Y maps to a k-rational point of X. Conversely,
suppose X has a k-rational point P . If P is not a singular point, then the unique
point of Y above P is also k-rational. If P is a singular point, then the unique
intersection of the two irreducible components in the exceptional divisor above P
is a k-rational point on Y . □

4 RONALD VAN LUIJK

Corollary 2.4. If k is a number ﬁeld and C has points locally everywhere, then so
does Y .

Proof. Let v be any place of k and kv the corresponding completion. By assumption,
C contains a kv-rational point P . Then π((P, P )
) is a kv-rational point on X.
Applying Lemma 2.3 to kv, we ﬁnd that Y has a kv-rational point as well, so Y
has points locally everywhere. □

Lemma 2.5. The k-rational points of X correspond to triples (P, Q, R), up to cyclic
permutation, of collinear points on C that are deﬁned over some galois (Z/3Z)-
extension l of k and permuted by Gal(l/k).

Proof. Suppose l is a galois (Z/3Z)-extension of k and (P, Q, R) a triple of l-rational
collinear points, permuted by Gal(l/k). Then all permutations of (P, Q, R) induced
by Gal(l/k) are even, so the orbit {(P, Q), (Q, R), (R, P )} of ρ is galois invariant and
yields a k-rational point of X. Conversely, any k-rational point of X corresponds
to a galois invariant orbit of ρ, say {(P, Q), (Q, R), (R, P )}. This implies that galois
permutes {P, Q, R}, but only by even permutations, so P, Q, and R are deﬁned
over k or over some galois (Z/3Z)-extension of k. They are collinear because (P, Q)
and (Q, R) are in the same orbit of ρ. □

Remark 2.6. Note that the words “permuted by Gal(l/k)” mean that the points
P, Q, and R are either all deﬁned over k, or they are all conjugates.

Lemma 2.7. The surface Y has a k-rational point if and only if there exists a
galois (Z/3Z)-extension l of k such that C contains three collinear points deﬁned
over l and permuted by Gal(l/k).

Proof. This follows immediately from Lemmas 2.3 and 2.5. □

Corollary 2.8. If C has no k-cubic points, then Y has no k-rational points.

Proof. This follows immediately from Lemma 2.7. □

Let J = Jac C denote the Jacobian of C. The following proposition is not needed
for the proof of the main theorem, but it is an interesting fact, conveyed and proved
to the author by Bjorn Poonen.

Proposition 2.9. Suppose that J(k) is ﬁnite and that 3 does not divide the order
of J(k). Then the converse of Corollary 2.8 holds as well.

Proof. Suppose that C contains a k-cubic point P . If P is k-rational, then (P, P ) ∈
C × C maps to a k-rational point on X, so Y has a k-rational point by Lemma
2.3. If P is not k-rational then it is deﬁned over a (Z/3Z)-extension l of k and
has two conjugates Q and R. Let L denote a line section of C. Then we have
(P ) + (Q) + (R) − L ∈ J(k), while by assumption J(k) = 3J(k), so there is an
element D ∈ J(k) such that (P ) + (Q) + (R) − L ∼ 3D. By Riemann-Roch there
exist unique points P ′, Q
′, R′ ∈ C(l) that are linearly equivalent with P − D, Q − D,
and R−D respectively. Then (P ′)+(Q
′)+(R′) ∼ L, so P ′, Q
′, and R′ are collinear.
Since Gal(l/k) ﬁxes D, it permutes P ′, Q
′, and R′. By Lemma 2.7 the surface Y
has a k-rational point. □

Remark 2.10. The Jacobian of the Selmer curve C given by (1) has trivial Mordell-
Weil group over Q. Since C does not have any Q-rational points, by the proofs
of Lemmas 2.3, 2.5, and Proposition 2.9 this implies that the galois conjugates of

CUBIC POINTS AND THE BRAUER-MANIN OBSTRUCTION ON K3 SURFACES 5

any Q-cubic point on C are collinear, so it is no surprise that the Q-cubic points
mentioned in the introduction come from intersecting C with a line.

We now show how to ﬁnd explicit equations for XC. Let ˘P
2 denote the dual of
P
2 and let τ : C × C → ˘P
2 be the map that sends (P, Q) to the line through P and
Q, and (P, P ) to the tangent to C at P . By Bezout’s theorem, for a general line L
in P
2 we have #(L ∩ C) = 3, so there are 6 ordered pairs (P, Q) ∈ C × C that map
under τ to L. We conclude that τ is generically 6-to-1. The map τ factors through
π, inducing a 2-to-1 map ϕ : X → ˘P
2 that is ramiﬁed over the dual ˘C of C.

C × C π
 τ
X ϕ ˘P
2

The dual ˘C has nine cusps, corresponding to the nine ﬂexes of C. As a double
cover of P
2 ramiﬁed over a curve with a cusp yields the same singularity as the
A2-singularities of XC, we conclude that XC is not only birational, but in fact
isomorphic to a double cover of P
2, ramiﬁed over a sextic with nine cusps.

Remark 2.11. Suppose that an aﬃne piece of C is given by f (x, y) = 0. Then the
function ﬁeld k(C × C) of C × C is the quotient ﬁeld of the ring

k[x1, y1, x2, y2]/
(f (x1, y1), f (x2, y2)
).

The line L through the generic points (x1, y1) and (x2, y2) on C is given by

(3) L : y = y2 − y1
x2 − x1 x + x2y1 − x1y2
x2 − x1 .

Let the coordinates of ˘P
2 be given by r, s, t, where the point [r : s : t] corresponds
to the line in P
2 given by rx + sy + tz = 0, or in aﬃne coordinates y = − r
s x − t
s .
Comparing this to equation (3), we ﬁnd that the inclusion of function ﬁelds

τ ∗ : k(˘P
2) = k ( r
s , t
s
 ) → k(C × C)

is given by r
s = − y2 − y1
x2 − x1 , and t
s = − x2y1 − x1y2
x2 − x1 .

Let x3 ∈ k(C × C) be the x-coordinate of the third intersection point of the line
L and C. Then the element d = (x1 − x2)(x2 − x3)(x3 − x1) is invariant under
ρ, so it is contained in the function ﬁeld k(X) of X, embedded in k(C × C) by
π∗. The element d is not contained in k(˘P
2), as it is only invariant under even
permutations of the xi. Hence d generates the quadratic extension k(X)/k(˘P
2).
We may therefore identify k(X) with the ﬁeld k( r
s , t
s , d) ⊂ k(C × C).

Example 2.12. After applying a linear transformation deﬁned over some ﬁnite ex-
tension of k, we may assume that one of the 9 inﬂection points of C is equal to
[0 : 1 : 0] and that the tangent at that point is the line at inﬁnity given by z = 0.
Assume this can be done over k itself. Then the aﬃne part given by z = 1 is given
by a Weierstrass equation and as the characteristic of k is not equal to 2 or 3, we
can arrange for C to be given by

y2 = x
3 + Ax + B

6 RONALD VAN LUIJK

with A, B ∈ k. With the point O = [0 : 1 : 0] as origin, C obtains the structure
of an elliptic curve. Note that the inﬂection points of C are exactly the 3-torsion
points on the elliptic curve.
To ﬁnd an explicit model for XC, we ﬁnd a relation among r
s , t
s , and d. The
x-coordinates x1, x2, x3 of the intersection points of C with the generic line L given
by rx + sy + t = 0 are the solutions to the equation

− (− r
s x − t
s
 )2 + x
3 + Ax + B = 0.

The square of d = (x1 − x2)(x2 − x3)(x3 − x1) is exactly the discriminant of this
polynomial, which is easy to compute. We ﬁnd that XC can be given in weighted
projective space P(1, 1, 1, 3) with coordinates r, s, t, u by

u2 = 4Br6 − 4Ar5t + A
2r4s
2 + 36Br3s
2t − 4r3t3 − 18ABr2s
4

− 30Ar2s
2t2 + 24A
2rs4t − (4A
3 + 27B2)s
6 + 54Bs
4t2 − 27s
2t4,

with u = s3d. This is exactly the same as in [7], with b = −r/s and a = −t/s for
their variables a and b. The map ϕ : X → ˘P
2 ramiﬁes where the right-hand side of
the equation vanishes, which describes the dual ˘C of C. We can describe the cusps
of ˘C very explicitly. The cusp corresponding to O is [0 : 0 : 1]. The slopes dy/dx at
the inﬂection points of C that are not equal to O are the roots of the polynomial

F = u8 + 18Au4 + 108Bu2 − 27A
2.

If α is a root of F , then the corresponding inﬂection point is (x, y) = ( 1
3 α2, α
4+3A
6α ).
The corresponding cusp on ˘C is [r : s : t] = [6α2 : −6α : 3A − α4]. Note that the
splitting ﬁeld of F is exactly k(C[3]), the ﬁeld of deﬁnition of all 3-torsion.

Example 2.13. Suppose C is given by

ax
3 + by3 + c = 0.

Then as in Example 2.12 we ﬁnd that in this case XC ⊂ P(1, 1, 1, 3) can be given
by 3u2 = 2abc(cr3s
3 + br3t3 + as
3t3) − b2c
2r6 − a
2c
2s
6 − a
2b2t6,
with u = 1
9 a
2s
3d = 1
9 a
2s
3(x1 − x2)(x2 − x3)(x3 − x1). Each of the coordinate axes
x = 0 and y = 0 and the line z = 0 at inﬁnity intersects the curve C at three ﬂexes.
Each of the corresponding nine cusps on ˘C lies on one of the coordinate axes given
by rst = 0 in ˘P
2.

In the next section we will investigate the geometry of Y and ﬁnd its Picard group
Pic Y , at least in the general case that C does not admit complex multiplication.
The group Pic Y is generated by irreducible curves on Y , of which we will now
describe some explicitly.
Let Π denote the set of the nine cusps of ˘C. We will freely identify the elements
of Π with the ﬂexes on C that they correspond to. A priori one would not expect
there to be any conics going through six points of Π, but it turns out there are 12.
They are described by Proposition 2.14. Fix a point O ∈ Π to give C the structure
of an elliptic curve. Then Π is the group C[3] of 3-torsion and thus Π obtains the
structure of an F3-vectorspace in which a line is any translate of any 1-dimensional
linear subspace. The three points on such lines are actually collinear as points on
C. The set of these 12 lines in Π is thus in bijection with the set of triples of
collinear points in Π, and therefore independent of the choice of O.

CUBIC POINTS AND THE BRAUER-MANIN OBSTRUCTION ON K3 SURFACES 7

Proposition 2.14. The six points on any two parallel lines in Π lie on a conic
whose pull-back to X consists of two components.

Proof. It suﬃces to prove this in the setting of Example 2.12. Let l and m be two
parallel lines in Π. After translation by an element of Π = C[3] we may assume
that O is not contained in l ∪ m. Let P be a point other than O on the linear
subspace that l and m are translates of. By Example 2.12, the point P corresponds
to a root α of F , which factors as F = (u2 − α2)fα. The point −P corresponds to
−α and the points in l ∪ m correspond to the roots of fα. These points all lie on
the conic given by

(4) 27t2 − 6α2rt + (α4 + 18A)r2 + (α6 + 21Aα2 + 81B)s
2 = 0.

From Example 2.12 we ﬁnd that the pull back of this conic to X is given by (4)
and α2u2 = (Ar3 + 9Brs
2 + 3rt2 − 6As
2t)
2,
which indeed contains two components. □

Remark 2.15. Consider the situation of the proof of Proposition 2.14. Over the
ﬁeld k(α, √−3), the polynomial fα splits as the product of two cubics such that
the points of l correspond to the roots of one of the two cubics and the points of
m correspond to the roots of the other.

Remark 2.16. The fact that the conics of Proposition 2.14 have a reducible pull
back to X also follows without explicit equations. Set H = τ ∗L for any line L ⊂ ˘P
2

that does not go through any of the P ∈ Π. For each P ∈ Π, let ΘP ∈ Div Y be
the sum of the two (−2)-curves above the singular point on X corresponding to P .
As these curves intersect each other once, we ﬁnd Θ2
P = −2, while we also have
H · ΘP = 0 and H 2 = 2. Any curve Γ ⊂ ˘P
2 of degree m that goes through P ∈ Π
with multiplicity aP pulls back to a curve on X whose strict transformation to Y
is linearly equivalent with
 D = mH − ∑

P ∈Π aP ΘP .

We have D2 = 2m2 − 2 ∑ a
2
P . For a conic Γ through six of the points of Π we get
D2 = −4. Let pa(D) be the arithmetic genus of D. As the canonical divisor KY of
Y is trivial, we ﬁnd from the adjunction formula 2pa(D) − 2 = D · (D + KY ) (see
[9], Prop. V.1.5) that pa(D) = −1 is negative, which implies that D is reducible.
We can use the same idea to ﬁnd (−2)-curves on Y . For instance, the strict
transformation on Y of any pull back to X of a line through 2 points of Π, or of a
conic through 5 points of Π will be such a curve.

3. The geometry of the surface

In this section we investigate some geometric properties of X and Y . As our
main theorem only concerns characteristic 0, we will for convenience assume that
the ground ﬁeld k equals C throughout this section. Several of the results, however,
also hold in positive characteristic, which we will point out at times. We start with
a quick review of lattices.
A lattice is a free Z-module L of ﬁnite rank, endowed with a symmetric, bilinear,
nondegenerate map L × L → Q, (x, y) ↦→ x · y, called the pairing of the lattice.
An integral lattice is a lattice with a Z-valued pairing. A lattice L is called even if

8 RONALD VAN LUIJK

x · x ∈ 2Z for every x ∈ L. Every even lattice is integral. If L is a lattice and m
a rational number, then L(m) is the lattice obtained from L by scaling its pairing
by a factor m. A sublattice of a lattice Λ is a submodule L of Λ such that the
induced bilinear pairing on L is nondegenerate. The orthogonal complement in Λ
of a sublattice L of Λ is

L
⊥ = {λ ∈ Λ : λ · x = 0 for all x ∈ L}

A sublattice L of Λ is primitive if Λ/L is torsion-free. The minimal primitive
sublattice of Λ containing a given sublattice L is (L
⊥)
⊥ = (L ⊗ Q) ∩ Λ. The
Gram matrix of a lattice L with respect to a given basis x = (x1, . . . , xn) is Ix =
(⟨xi, xj⟩)i,j. The discriminant of L is deﬁned by disc L = det Ix for any basis x of L.
A unimodular lattice is an integral lattice with disriminant ±1. For any sublattice
L of ﬁnite index in Λ we have disc L = [Λ : L]
2 · disc Λ. The dual lattice of a lattice
L is ˇL = {x ∈ L ⊗ Q : x · λ ∈ Z for all λ ∈ L}.
If L is integral, then L is contained in ˇL with ﬁnite index [ ˇL : L] = | disc L| and the
quotient AL = ˇL/L is called the dual-quotient of L. If L is a primitive sublattice
of a unimodular lattice Λ, then the dual-quotients AL and AL⊥ are isomorphic as
groups, and we have | disc L| = | disc L
⊥|. For more details on these dual-quotients
and the discriminant form deﬁned on them, see [16].

If Z is a smooth projective irreducible surface, let Pic
0 Z ⊂ Pic Z denote the
group of divisor classes that are algebraically equivalent to 0. The quotient NS(Z) =
Pic Z/ Pic0 Z is called the N´eron-Severi group of Z. The exponential map C →
C
∗, z ↦→ exp(2πiz) induces a short exact sequence 0 → Z → OZ → O∗
Z → 1
of sheaves on the complex analytic space Zh associated to Z. The induced long
exact sequence includes H 1(Zh, OZ ) → H 1(Zh, O∗
Z ) → H 2(Zh, Z). There is an
isomorphism H 1(Zh, O∗
Z ) ∼ Pic Z and the image of the ﬁrst map H 1(Zh, OZ ) →
H 1(Zh, O∗
Z ) is exactly Pic0 Z. We conclude that there is an embedding NS(Z) ֒→
H 2(Zh, Z). The intersection pairing induces a pairing on NS(Z), which coincides
with the cup-product on H 2(Zh, Z). By abuse of notation we will write H 2(Z, Z) =
H 2(Zh, Z). See [9], App. B.5, for statements and [22] and [2], §IV.2, for more
details.

Proposition 3.1. If Z is a K3 surface, then Pic0 Z = 0 and we have an isomor-
phism Pic Z ∼ NS(Z).

Proof. By deﬁnition we have H 1(Z, OZ ) = 0, so from the above we ﬁnd Pic
0 Z = 0.
The isomorphism follows immediately. □

Note that by ﬁxing a point on C, the surface C × C obtains the structure of an
abelian surface.

Proposition 3.2. Let Z be an abelian surface (resp. K3 surface). Then H(Z, Z)
is an even lattice with discriminant −1 of rank 6 (resp. 22) in which NS(Z) embeds
as a primitive sublattice.

Proof. The lattice H(Z, Z) is even by [2], Lemma VIII.3.1. If Z is an abelian
surface, then this lattice is unimodular by [2], §V.3, and indeﬁnite by the Hodge
index theorem, see [9], Thm. V.1.9. From the classiﬁcation of even indeﬁnite
unimodular lattices we ﬁnd that H(Z, Z) is isomorphic with U 3, where U is the

CUBIC POINTS AND THE BRAUER-MANIN OBSTRUCTION ON K3 SURFACES 9

hyperbolic lattice with discriminant −1, see [21], Thm. V.5. A similar argument
holds for K3 surfaces, see [2], Prop. VIII.3.3 (VIII.3.2 in ﬁrst edition). This implies
that in both cases the map H 2(Z, Z) → H 2(Z, C) is injective, so NS(Z) is the image
of Pic Z in H 2(Z, C). By [2], Thm. IV.2.13 (IV.2.12 in ﬁrst edition), this image is
the intersection of H 2(X, Z) with the C-vectorspace H 1,1(X, ΩX ) inside H 2(X, C).
This implies the last part of the claim. □

Remark 3.3. From Propositions 3.1 and 3.2 it follows that linear, algebraic, and nu-
merical equivalence all coincide on a complex K3 surface. In positive characteristic
this is the case as well, see [4], Thm. 5.

Lemma 3.4. Let Z be an abelian variety or a K3 surface. Let D be a curve on Z
with arithmetic genus pa(D). Then we have D2 = 2pa(D) − 2.

Proof. The canonical divisor KZ is trivial for both abelian varieties and K3 surfaces.
The adjunction formula therefore gives 2pa(D) − 2 = D · (D + KZ) = D2 (see [9],
Prop. V.1.5). □

Lemma 3.5. Take any point R ∈ C and deﬁne the divisors

D1 = { (P, Q) : P, Q, R collinear }, D2 = C × {R}, D3 = {R} × C

on C × C. The automorphism ρ acts on the Di as the permutation (D1 D2 D3).
The images in NS(C × C) of the Di are independent of the choice of R. We have
Di · Dj = 1 if i ̸= j and D2
i = 0. The elements D1, D2, D3 are numerically
independent.

Proof. The ﬁrst statement is obvious. All ﬁbers of the projection of C × C onto
the second copy of C are algebraically equivalent to each other, so the image of D2
in NS(C × C) is independent of R. As D1 and D3 are in the orbit of D2 under ρ,
their images are independent of R as well. The divisors D2 and D3 intersect each
other transversally in one point, so D2 · D3 = 1. As D2 is isomorphic to C, the
genus pa(D2) of D2 equals 1, so Lemma 3.4 gives D2
2 = 0. The other intersection
numbers follow by applying ρ. The last statement follows immediately. □

For any R ∈ C the three divisors Di of Lemma 3.5 all map birationally to the
same curve on XC, namely the pull back ϕ∗( ˘R) of the dual ˘R of R, i.e., the line in
˘P
2 consisting of all lines in P
2 going through R.
For each P ∈ Π, let LP ⊂ NS(Y ) be the lattice generated by the two (−2)-curves
above the singularity on X corresponding to P . Then the lattice L generated by all
these (−2)-curves is isomorphic to the orthogonal direct sum ⊕P ∈Π LP . For each
P ∈ Π, the dual-quotient ALP is a 1-dimensional F3-vectorspace. Let Λ = (L
⊥)
⊥

be the minimal primitive sublattice of NS(Y ) that contains L. Then Λ is contained
in the dual ˇL of L, so Λ/L is a subspace of the dual-quotient AL ∼ ⊕P ∈Π ALP .

Lemma 3.6. We can identify each ALP with F3 and give Π the structure of an
F3-vectorspace in such a way that

Λ/L ⊂ ⊕

P ∈Π ALP ∼ F
Π
3

consists of all aﬃne linear functions Π → F3.

Proof. See [3], Thm. 2.5. The subspace Λ/L corresponds to L3 as deﬁned on page
269 of [3]. □

10 RONALD VAN LUIJK

Corollary 3.7. We have [Λ : L] = 27 and disc Λ = 27.

Proof. The ﬁrst equality follows from Lemma 3.6 and the fact that there are 27
aﬃne linear functions F
2
3 → F3. The second equality then follows from the equation
[Λ : L]
2 · disc Λ = disc L = 3
9. □

Remark 3.8. Fix a point O ∈ Π. Then C obtains the structure of an elliptic
curve and Π corresponds to the group C[3] of 3-torsion elements, which naturally
has the structure of an F3-vectorspace. The 24 nonconstant aﬃne linear functions
Π → F3 correspond to the irreducible components of the 12 pull backs of the conics
of Proposition 2.14.

Let TC×C and TY denote the othogonal complements of NS(C × C) and NS(Y )
in H 2(C × C, Z) and H 2(Y, Z) respectively. The main result of this section is the
following.

Proposition 3.9. There is a natural isomorphism TY ∼ TC×C(3) of lattices.

Proof. For convenience write H ρ
C×C = H 2(C × C, Z)
⟨ρ⟩. From Katsura’s table
in [11], p. 17, we ﬁnd rk H ρ
C×C = 4 and the remaining eigenvalues of ρ∗ acting
on H 2(C × C, Z) are ζ and ζ 2, where ζ is a primitive cube root of unity. Let
Γ′ ⊂ NS(C × C) denote the sublattice generated by the Di of Proposition 3.5, and
set D = D1 + D2 + D3. By Proposition 3.5, D is ﬁxed by ρ. As ρ∗ acts unitarily on
H 2(C ×C, C), its eigenspaces corresponding to diﬀerent eigenvalues are orthogonal.
We conclude from Proposition 3.5 that the orthogonal complement Γ of ⟨D⟩ inside
Γ′ corresponds to the eigenvalues ζ and ζ 2, which in turn implies H ρ
C×C = Γ
⊥ inside
the unimodular lattice H 2(C × C, Z), because H ρ
C×C corresponds to the eigenvalue
1. The lattice Γ is generated by D1 − D2 and D2 − D3 and has discriminant 3, so
it is primitive and we also have | disc H ρ
C×C| = | disc Γ| = 3. Set N = Γ′⊥. Taking
orthogonal complements in Γ ⊂ Γ′ ⊂ NS(C × C) we ﬁnd TC×C ⊂ N ⊂ H ρ
C×C.
From the fact that (Γ
′/Γ)⊗ Q is generated by D, it follows that N is the orthogonal
complement of D inside H ρ
C×C.
Let HX denote the orthogonal complement of L (or Λ) in the unimodular lattice
H 2(Y, Z), so that by Corollary 3.7 we have | disc HX | = | disc Λ| = 27. Recall that
π denotes the quotient map C × C → XC. There are maps π∗ : HX → H ρ
C×C and
π∗ : H ρ
C×C → HX such that π∗ and π∗ send transcendental cycles to transcendental
cycles and (i) π∗(x) · π∗(y) = 3x · y, ∀x, y ∈ HX ,
(ii) π∗(x) · π∗(y) = 3x · y, ∀x, y ∈ H ρ
C×C,
(iii) π∗(π∗(x)) = 3x, ∀x ∈ HX ,
(iv) π∗(π∗(x)) = 3x, ∀x ∈ H ρ
C×C,

see [10], §1, and [3], p. 273. From (iv) and the fact that H 2(C ×C, Z) is torsion-free,
we ﬁnd that π∗ is injective. Therefore, by (ii) we have an isomorphism π∗(H ρ
C×C) ∼
H ρ
C×C(3) and

| disc π∗(H ρ
C×C)| = | disc H ρ
C×C(3)| = 3
rk H ρ
C×C · | disc H ρ
C×C| = 3
5.

From [HX : π∗(H ρ
C×C)]
2 · | disc HX | = | disc π∗(H ρ
C×C)|,

we then ﬁnd [HX : π∗(H ρ
C×C)] = 3.

CUBIC POINTS AND THE BRAUER-MANIN OBSTRUCTION ON K3 SURFACES 11

Recall that π∗(D1) = π∗(D2) = π∗(D3) = H, where H denotes the class of the
strict transformation of the pull back of a line in ˘P
2 to X. Therefore, π∗(D) = 3H.
From 9 ∤ 6 = D2 we conclude D ̸∈ 3H ρ
C×C, and thus 3H = π∗(D) ̸∈ 3π∗(H ρ
C×C),
which implies H ∈ HX \ π∗(H ρ
C×C). As the index [HX : π∗(H ρ
C×C)] = 3 is prime,
it follows that HX /π∗(H ρ
C×C) is generated by H, so the orthogonal complement
π∗(N ) of 3H = π∗(D) in π∗(H ρ
C×C) is primitive in HX . From the primitive inclusion
π∗(TC×C) ⊂ π∗(N ) it follows that also π∗(TC×C) is primitive in HX , and thus in
H 2(Y, Z).
From L ⊂ NS(Y ) we ﬁnd TY ⊂ HX . From (i)-(iv) and the fact that π∗
and π∗ send transcendental elements to transcendental elements, we ﬁnd 3TY ⊂
π∗(TC×C) ⊂ TY . This implies rk TY = rk TC×C and together with the fact that
π∗(TC×C) is primitive in H 2(Y, Z), it follows that we have TY = π∗(TC×C) ∼
TC×C(3), where the last isomorphism follows from π∗(H ρ
C×C ) ∼ H ρ
C×C(3). □

Remark 3.10. Proposition 3.9 is mentioned without proof in [17], where it is claimed
that the proof is exactly the same as in the classical Kummer case, where Y is the
desingularization of the quotient X of an abelian surface A by an involution ι.
Indeed there are many similarities between the proof of the classical case (see for
instance [14], Prop. 4.3) and the one just presented, but there are some essen-
tial diﬀerences. A ﬁrst diﬀerence is that in the classical case ι acts trivially on
H 2(A, Z). There is, however, a much more signiﬁcant diﬀerence. In the classical
case the lattice π∗H(A, Z)
⟨ι⟩ is easily proved to be primitive in the orthogonal com-
plement HX of the lattice L generated by the 16 exceptional divisors on Y . This
immediately implies that π∗TA is primitive in H 2(Y, Z). As in our case the index
[HX : π∗H ρ
C×C] = 3 is not trivial, the classical proof does certainly not directly
apply.

As before, let Jac C denote the Jacobian of C and End Jac(C) its endomorphism
ring, which is isomorphic to Z or an order in either an imaginary quadratic ﬁeld or
a quaternion algebra.

Proposition 3.11. We have rk NS(C × C) = 2 + rk End Jac C.

Proof. Note that for a curve D the group Pic
0 D is the kernel of the degree map
Pic D → Z, so that we have an isomorphism NS(D) ∼ Z. The statement then
follows from [24], App., or [1], Thm. 3.11. □

Proposition 3.12. With r = rk End Jac C we have

rk NS(Y ) = 18 + r and disc NS(Y ) = 3
4−r disc NS(C × C).

Proof. From Propositions 3.2 and 3.11 we get rk TC×C = 6 − rk NS(C × C) = 4 − r.
From Propositions 3.2 and 3.9 we then conclude

rk NS(Y ) = 22 − rk TY = 22 − rk TC×C = 18 + r.

From Proposition 3.9 we also get

disc TY = disc TC×C(3) = 3
rk TC×C disc TC×C = 3
4−r disc TC×C.

From Proposition 3.2 we then ﬁnd

disc NS = − disc TY = −3
4−r disc TC×C = 3
4−r disc NS(C × C).
 □

12 RONALD VAN LUIJK

Remark 3.13. The conclusion rk NS(Y ) = 18 + rk End Jac C of Proposition 3.12
is much weaker than the statement of Proposition 3.9 as it suﬃces to work with
coeﬃcients in Q or C instead of Z in the cohomology. By working with ´etale
cohomology instead, we can deduce the same equation in positive characteristic.
For most of the details, see [11], which only gives rk NS(Y ) ≥ 19 ([11], p. 17).

Corollary 3.14. If C does not admit complex multiplication, then the N´eron-Severi
lattice NS(YC) has rank 19, discriminant 54, and is generated by the pull back H
of a line in ˘P
2, the irreducible components above the P ∈ Π, and the irreducible
components of the pull backs of the conics of Proposition 2.14.

Proof. If C does not admit complex multiplication, then End Jac C has rank r = 1
by deﬁnition, so by Proposition 3.12 we have rk NS(YC) = 19 and 27| disc NS(Y ).
The lattice Λ generated by the irreducible components above the P ∈ Π and the
conics of Proposition 2.14 has rank 18 and discriminant 27 by Corollary 3.7 and
Remark 3.8. The class H is orthogonal to Λ and satisﬁes H 2 = 2, so ⟨H⟩ ⊕ Λ has
discriminant 27 · 2 = 54 and rank 19, and thus ﬁnite index in NS(Y ). From

disc NS(Y ) · [NS(Y ) : ⟨H⟩ ⊕ Λ]2 = disc⟨H⟩ ⊕ Λ = 54,

and the fact that 27| disc NS(Y ), we ﬁnd that the index equals 1, so NS(Y ) =
⟨H⟩ ⊕ Λ. □

4. Diagonal cubics and the proof of the main theorem

Let C ⊂ P
2 be a diagonal cubic, deﬁned over a number ﬁeld k, given by ax3 +
by3 + cz3 = 0. Let ζ ∈ k denote a primitive cube root of unity. Then J = Jac C is
an elliptic curve of j-invariant 0, with endomorphism ring End J ∼ Z[ζ]. Consider
the automorphism ζx : [x : y : z] ↦→ [ζx : y : z] of C. The line through a point
P = [x0 : y0 : z0] and ζxP is given by z0y − y0z = 0 and also goes through ζ 2
xP ,
so the map τ : C × C → ˘P
2 sends both (P, ζxP ) and (P, ζ 2
xP ) to [0 : z0 : −y0]. It
follows that both curves

D4 = { (P, ζxP ) ∈ C × C : P ∈ C }

D5 = { (P, ζ 2
xP ) ∈ C × C : P ∈ C }

map under τ to the line Lr in ˘P
2 given by r = 0. However, the two curves are both
ﬁxed by ρ, so they map to diﬀerent curves in XC. Hence, the pull back to XC of
Lr consists of two irreducible components. The same could be concluded from an
argument similar to that in Remark 2.16. The line Lr goes through three cusps of
˘C (see Example 2.13), so the strict transform D on YC of the pull back to XC of
Lr is linearly equivalent to H − ∑P ∈Π∩Lr ΘP , which implies D2 = −4 < −2, so D
is reducible. Obviously, the same holds for the lines given by s = 0 and t = 0.
By Proposition 3.11 we have rk NS(C × C) = 4. The divisors D1, D2, D3 of
Proposition 3.5 and D4 from above mutuallly intersect each other exactly once.
They are all isomorphic to C, so they have genus 1 and we have D2
i = 0 by Lemma
3.4. It follows that the Di (1 ≤ i ≤ 4) generate a sublattice V of NS(C × C) of rank
4 and discriminant −3. As this discriminant is squarefree, we ﬁnd NS(C × C) = V ,
and thus disc NS(C × C) = −3. By Proposition 3.12 we conclude disc NS(Y ) = −27
and rk NS(Y ) = 20. We will now describe the N´eron-Severi group more concretely.
By Example 2.13, the pull back of the line Lr given by r = 0 to XC ⊂ P(1, 1, 1, 3)
is given by r = 0 and −3u2 = a
2(bt3 − cs
3)
2. We will denote the two components

CUBIC POINTS AND THE BRAUER-MANIN OBSTRUCTION ON K3 SURFACES 13

by Dω
r , where ω ∈ {ζ, ζ 2} is such that 1 + 2ω = a(bt3 − cs
3)/u on the corresponding
component. We have Dζ
r + Dζ2
r ∼ H − ∑P ∈Π∩Lr ΘP with ΘP as in Remark 2.16.
Similarly, Dω
s and Dω
t denote the irreducible components above s = 0 and t = 0
with ω such that 1 + 2ω equals the value along the corresponding component of
b(cr3 − at
3)/u and c(as
3 − br3)/u respectively.
Choose elements α, β ∈ k such that α3 = −c/b and β3 = −a/c, and set γ =
−α−1β−1, so that γ3 = −b/a. The ﬂexes of C are given by [0 : α : ζ i], [ζ i : 0 : β],
and [γ : ζ i : 0], with 0 ≤ i ≤ 2. The corresponding cusps of ˘C are [0 : −ζ i : α],
[β : 0 : −ζ i], and [−ζ i : γ : 0] respectively. Let O, P , and Q denote the cusps
[0 : −1 : α], [0 : −ζ : α], and [β : 0 : −1] respectively. Identifying the cusps of ˘C
with the ﬂexes of C, the curve C gets the structure of an elliptic curve with origin
O. The following addition table shows what the other cusps correspond to.

O Q −Q
O [0 : −1 : α] [β : 0 : −1] [−1 : γ : 0]
P [0 : −ζ : α] [β : 0 : −ζ] [−ζ : γ : 0]
−P [0 : −ζ 2 : α] [β : 0 : −ζ 2] [−ζ 2 : γ : 0]

The curve in ˘P
2 given by

r2 + α2β2s
2 + β2t2 + αβrs − βrt − αβ2st = 0

is one of the conics of Proposition 2.14, going through the points nQ ± P for any
integer n. Its pullback to XC ⊂ P(1, 1, 1, 3) is given by the same equation together
with α2u = ±β2c
2rst, therefore containing two irreducible components that we
will denote according to the sign in the equation by D±
α,β. By choosing α and β
diﬀerently, we get nine out of the twelve conics of Proposition 2.14. The remaining
three are the three possible pairs out of the three lines given by rst = 0.
Take any α′ ∈ {α, ζα, ζ 2α} and consider the aﬃne coordinates u′ = u/s3,
r′ = r/s, and t′ = t/s + α′. By Example 2.13, XC is locally given by u′2 =
−3a
2b2α′4t′2 + (higher order terms), where the point R = [0 : −1 : α′] corresponds
to (0, 0, 0). Therefore, the square of the ratio 3abα′2t′/u′ equals −3 on both irre-
ducible components of the exceptional divisor of the blow-up at R. We denote these
components by Θ
ω
r,α′ or Θ
ω
R, with ω ∈ {ζ, ζ 2} such that 1 + 2ω = 3abα′2t′/u′ =

3abα′2s
2(t + α′s)/u on the corresponding component. Note that Θ
ζ
R + Θ
ζ2

R = ΘR,
c.f. Remark 2.16. Similarly, for β′ ∈ {β, ζβ, ζ 2β} and R = [β′ : 0 : −1], we
denote the irreducible components above R by Θ
ω
s,β′ or Θ
ω
R, with ω such that
1 + 2ω = 3bcβ′2t2(r + β′t)/u. For γ′ ∈ {γ, ζγ, ζ 2γ} and R = [−1 : γ′ : 0], we denote
the irreducible components above R by Θ
ω
t,γ′ or Θ
ω
R in such a way that we have
1 + 2ω = 3acγ′2r2(s + γ′r)/u on the corresponding component.
We will see that the 43 divisors H, Θω
R, Dω
v and D±
α′,β′ generate the N´eron-Severi
group. Their intersection numbers are easily computed from the above and given
by
 H 2 = 2, H · Dω
v = 1, D+
α′,β′ · D−
α′′,β′′ = 0,
H · Θ
ω
R = 0, H · D±
α′,β′ = 2, Dω
v · D±
α′,β′ = 0,

14 RONALD VAN LUIJK

Θ
ω1
v,δ · Θ
ω2
w,δ′ =
 
 −2 if v = w and δ = δ′ and ω1 = ω2,
1 if v = w and δ = δ′ and ω1 ̸= ω2,
0 otherwise,

Dω1
v · Dω2
w =
 
 −2 if v = w and ω1 = ω2,
1 if v ̸= w and ω1 ̸= ω2,
0 otherwise,

Dǫ
α′,β′ · Dǫ
α′′,β′′ =
 
 −2 if α′′ = α′ and β′′ = β′,
1 if α′′α′−1 = β′′β′−1 ̸= 1,
0 otherwise,

Dω1
v · Θ
ω2
w,δ = { 1 if v = w and ω1 = ω2,
0 otherwise,

Dǫ
α′,β′ · Θ
ω
v,δ =
 
 1 if v = r and α′/δ = ωǫ,
1 if v = s and β′/δ = ωǫ,
1 if v = t and γ′/δ = ωǫ (γ′ = −(α′β′)
−1),
0 otherwise

for any R ∈ Π, v, w ∈ {r, s, t}, ω ∈ {ζ, ζ 2}, ǫ ∈ {+, −}, α′, α′′ ∈ {α, ζα, ζ 2α},
β′, β′′ ∈ {β, ζβ, ζ 2β}, δ ∈ {ζ iα, ζ iβ, ζ iγ : 0 ≤ i ≤ 2} and ω+ = ω and ω− = ω−1.
The names of all the divisors are chosen to optimize symmetry. In particular, under
the identiﬁcation of the multiplicative group µ3 with the additive group F3, and
with the F3-vectorspace structure on Π coming from the addition on the elliptic
curve, the superscripts of the Θ
ω
R correspond exactly with the choices that need
to be made in Lemma 3.6. Many of these intersection numbers follow from that
lemma, but we preferred this concrete distinction between the Θ
ζ
R and Θ
ζ2

R , which
more easily reveals the intersection numbers with the Dω
v and where the galois
action on these divisors is given by the action on the superscripts and subscripts.

Proposition 4.1. The N´eron-Severi group of Y has rank 20 and discriminant −27.
It is generated by the galois-invariant set
{
Dζ
r , Dζ2
r } ∪ {
Θ
ω
R : R ∈ Π, ω ∈ {ζ, ζ 2}
}

∪ {
D+
α′,β′ : α′ ∈ {α, ζα, ζ 2α}, β′ ∈ {β, ζβ, ζ 2β}
} .

Proof. The 29 given divisors generate a lattice Λ of rank 20 and discriminant −27.
As we had already seen rk NS(Y ) = 20 and disc NS(Y ) = −27, we conclude Λ =
NS(Y ). □

Proposition 4.2. If abc is not a cube in k, then we have H 1(k, Pic
 Y ) = {1}.

Proof. From Proposition 4.1 we know a galois-invariant set of generators for Pic Y .
Let ρ, σ, τ be the automorphisms of Pic Y induced by acting as follows on the
superscript and subscripts.
 ρ : (α, β, ζ) ↦→ (ζα, β, ζ),

σ : (α, β, ζ) ↦→ (α, ζβ, ζ),

τ : (α, β, ζ) ↦→ (α, β, ζ 2).

The automorphisms ρ and σ commute and the group G = ⟨ρ, σ, τ ⟩ is isomorphic to
the semi-direct product ⟨ρ, σ⟩ ⋊ ⟨τ ⟩ ∼ (Z/3Z)
2 ⋊ Z/2Z, where τ acts on ⟨ρ, σ⟩ by
inversion. The group Pic Y is deﬁned over k(ζ, α, β), so we have H 1(k, Pic Y ) ∼

CUBIC POINTS AND THE BRAUER-MANIN OBSTRUCTION ON K3 SURFACES 15

H 1(k(ζ, α, β)/k, Pic Y ). The galois group Gal(k(ζ, α, β)/k) injects into G. In for
instance magma we can compute H 1(H, Pic Y ) for every subgroup H of G, see [28].
It turns out that if H 1(H, Pic Y ) is nontrivial, then H is contained in ⟨ρσ, τ ⟩. This
implies that if H 1(k(ζ, α, β)/k, Pic Y ) is nontrivial, then Gal(k(ζ, α, β)/k) injects
into the group ⟨ρσ, τ ⟩, so β/α is ﬁxed by the action of galois and therefore contained
in k, so abc = (cβ/α)
3 is a cube in k. □

Proof of Theorem 1.1. By Proposition 2.2 the surface Y is a K3 surface. As its
Picard number equals 20 by Proposition 4.1, it is in fact a singular K3 surface. By
Corollary 2.8 we have Y (k) = ∅. By Corollary 2.4 the surface Y has points locally
everywhere, so Y (Ak) ̸= ∅. By the Hochschild-Serre spectral sequence we have an
exact sequence Br k → Br1 Y → H 1(k, Pic Y ), see [25], Cor. 2.3.9. By Proposition
4.2 we ﬁnd Br1 Y = im Br k. As Br k never yields a Brauer-Manin obstruction, we
ﬁnd Y (Ak)
Br1 Y ̸= ∅. □

Remark 4.3. For some ﬁelds k the conditions (2) and (3) of Theorem 1.1 imply
condition (1). To see this, assume that we have a smooth curve C ⊂ P2
k given by
ax
3 + by3 + cz3 = 0 that satisﬁes conditions (2) and (3) while abc is a cube in the
number ﬁeld k, say abc = d3. For any λ ∈ k we consider e = λ3b/a. Then the
linear transformation [x : y : z] → [x : λ−1y : λ−2b−1dz] sends C isomorphically
to the curve given by x3 + ey3 + e
2z3, so without loss of generality we will assume
a = 1 and b = e and c = e
2. By picking λ suitably, we may also assume that e is
integral. Let p be a place of k. If 3 ∤ vp(e), then C is not locally solvable at p as the
three terms of the deﬁning equation have diﬀerent valuations, so we ﬁnd 3|vp(e) for
each place p of k, which means that the ideal (e) is the cube of some ideal I of the
ring Ok of integers of k. Now assume that the class number of k is not a multiple
of 3. Then from the fact that I 3 is principal we ﬁnd that I itself is principal, so
e = uv3, for some v ∈ Ok and u ∈ O∗
k. By rescaling y and z by a factor v and v2

respectively, we may assume v = 1, so that C is given by x3 + ux3 + u2z3 = 0. This
means that C is isomorphic to one in a ﬁxed ﬁnite set of curves, depending on k,
namely those curves given by x3 + wy3 + w2z3 = 0 where w ∈ O∗
k runs over a set
of representatives of O∗
k/(O∗
k)
3. For some ﬁelds k, none of these curves satisfy both
(2) and (3) so that we have a contradiction. For k = Q for instance, the group
O∗
k/(O∗
k)
3 is trivial and the curve x3 + y3 + z3 = 0 does not satisfy (3) as it contains
the point [0 : −1 : 1]. For any imaginary quadratic ﬁeld the same argument holds,
except for k = Q(
√−3), where O∗
k/(O∗
k)
3 is generated by a primitive cube root ζ
of unity. In that case there is one extra isomorphism class represented by the curve
given by x
3 + ζy3 + ζ 2z3 = 0, which contains the rational point [1 : 1 : 1]. We
conclude that if k = Q or k is an imaginary quadratic ﬁeld whose class number is
not a multiple of 3, then conditions (2) and (3) of Theorem 1.1 imply condition (1).

5. Open problems

Question 1. Is there any (not necessarily diagonal) plane cubic curve over a num-
ber ﬁeld k that has points locally everywhere, but no k-cubic points?

Question 2. Is there any diagonal plane cubic curve over a number ﬁeld k that
has points locally everywhere, but no k-cubic points?

Question 3. Is the Brauer-Manin obstruction the only obstruction to the Hasse
principle on K3 surfaces?

16 RONALD VAN LUIJK

References

[1] P. Argentin, Sur certaines surfaces de Kummer, Ph.D. thesis, Universit´e de Gen`eve, 2006.
[2] W. Barth, K. Hulek, C. Peters, and A. Van de Ven, Compact Complex Surfaces, Second
Enlarged Edition, Ergebnisse der Mathematik und ihrer Grenzgebiete, 3. Folge, Band 4, A
Series of Modern Surveys in mathematics 4, Springer-Verlag, 2004.
[3] J. Bertin, R´eseaux de Kummer et surfaces K3, Invent. Math. 93 (1988), pp. 267–284.
[4] E. Bombieri and D. Mumford, Enriques’ classiﬁcation of surfaces in char. p, II, Complex
Analysis and Algebraic Geometry — Collection of papers dedicated to K. Kodaira, ed. W.L.
Baily and T. Shioda, Iwanami and Cambridge Univ. Press (1977), pp. 23–42.
[5] J.-L. Colliot-Th´el`ene, Points rationnels sur les ﬁbrations, Higher dimensional varieties and
rational points, Proceedings of the 2001 Budapest conference (K. B¨or¨oczky, J. Koll´ar, and
T. Szamuely, eds.), Springer, 2003, Bolyai Society Colloquium Publications, pp. 171–221.
[6] A. Grothendieck et al., Th´eorie des Intersections et Th´eor`eme de Riemann-Roch, Lect. Notes
in Math. 225, Springer-Verlag, Heidelberg, 1971.
[7] J. Fearnley and H. Kisilevsky, Vanishing and non-vanishing Dirichlet twists of L-functions
of elliptic curves, Research report, Concordia University, 2004.
[8] R. Hartshorne, Equivalence relations of algebraic cycles and subvarieties of small codimen-
sion, Algebraic Geometry, Arcata 1974, Amer. Math. Soc. Proc. Symp. Pure Math. 29
(1975), pp. 129–164.
[9] R. Hartshorne, Algebraic Geometry, GTM 52, Springer, 1977.
[10] H. Inose, On certain Kummer surfaces which can be realized as non-singular quartic surfaces
in P3, J. Fac. Sci. Univ. Tokyo Sect IA Math. 23 (1976), pp. 545–560.
[11] T. Katsura, Generalized Kummer surfaces and their unirationality in characteristic p, J.
Fac. Sci. Univ. Tokyo Sect IA Math. 34 (1987), pp. 1–41.
[12] Yu.I. Manin, Le groupe de Brauer-Grothendieck en g´eom´etrie diophantienne, in: Actes
Congr`es Int. Math. Nice, 1970, tome I, Gauthier-Villars (1971), pp. 401–411.
[13] J.S. Milne, ´Etale Cohomology, Princeton Mathematical Series 33, Princeton University
Press, New Jersey, 1980.
[14] D. Morrison, On K3 surfaces with large Picard number, Invent. Math. 75 (1984), pp. 105–
121.
[15] T. Mutsasaka, The Criteria for Algebraic Equivalence and the Torsion Group, Am. J. Math.,
Vol. 79, No. 1 (1957), pp. 53–66.
[16] V. Nikulin, Integral symmetric bilinear forms and some of their applications, Math. USSR
Izvestija 14, 1 (1980), pp. 103–167.
[17] H. ¨Onsiper and S. Sert¨oz, Generalized Shioda-Inose structures on K3 surfaces, Manuscripta
Math. 98 (1999), pp. 491–495.
[18] P. Poonen, Heuristics for the Brauer-Manin obstruction for curves, Experimental Math. 15
(2006), no. 4, pp. 415–420.
[19] D. Eriksson and V. Scharaschkin, On the Brauer-Manin obstruction for zero-cycles on
curves, preprint, available on arXiv:math/0602355.
[20] E.S. Selmer, The Diophantine equation ax3 + by3 + cz3 = 0, Acta Math. 85 (1951), pp.
203–362.
[21] J.-P. Serre, A course in Arithmetic, GTM 7, Springer, 1973.
[22] J.-P. Serre, G´eom´etrie alg´ebrique et g´eom´etrie analytique, Annales de l’institut Fourier,
Tome 6 (1956), pp. 1–42.
[23] J. Silverman, The Arithmetic of Elliptic Curves, GTM 106, Springer, 1986.
[24] T. Shioda, Algebraic Cycles on Certain K3 Surfaces in Characteristic p, Manifolds-Tokyo
1973, ed. A. Hattori, Univ. of Tokyo Press (1975), pp. 357–364.
[25] A. Skorobogatov, Torsors and Rational Points, Cambridge Tracts in Mathematics 144,
Cambridge University Press, 2001.
[26] J. Tate, Algebraic cycles and poles of zeta functions, Arithmetical Algebraic Geometry, ed.
O.F.G. Schilling (1965), pp. 93–110.
[27] R. van Luijk, An elliptic K3 surface associated to Heron triangles, J. of Number Theory
123 (2007), pp. 92–119.
[28] Electronic ﬁle with magma-code to verify some of the computations in this article, available
from the author upon request.

CUBIC POINTS AND THE BRAUER-MANIN OBSTRUCTION ON K3 SURFACES 17

Dept. of Math., Simon Fraser University, Burnaby, BC, Canada, V5A 1S6
E-mail address: rmluijk@gmail.com
