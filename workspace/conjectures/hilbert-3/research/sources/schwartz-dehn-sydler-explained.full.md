<!-- source: https://www.math.brown.edu/reschwar/MathNotes/jessen.pdf | converted from PDF -->

The Dehn-Sydler Theorem Explained

Rich Schwartz

June 10, 2013

1 Introduction

The Dehn-Sydler theorem says that two polyhedra in R3 are scissors con-
gruent iﬀ they have the same volume and Dehn invariant. Dehn [D] proved
in 1901 that equality of the Dehn invariant is necessary for scissors congru-
ence. 64 years passed, and then Sydler [S] proved that equality of the Dehn
invariant (and volume) is suﬃcient. In [J], Jessen gives a simpliﬁed proof
of Sydler’s Theorem. The proof in [J] relies on two results from homolog-
ical algebra that are proved in [JKT]. Also, to get the cleanest statement
of the result, one needs to combine the result in [J] (about stable scissors
congruence) with Zylev’s Theorem, which is proved in [Z].
The purpose of these notes is to explain the proof of Sydler’s theorem
that is spread out in [J], [JKT], and [Z]. The paper [J] is beautiful and
eﬃcient, and I can hardly improve on it. I follow [J] very closely, except that
I simplify wherever I can. The only place where I really depart from [J] is my
sketch of the very diﬃcult geometric Lemma 10.2, which is known as Sydler’s
Fundamental Lemma. To supplement these notes, I made an interactive java
applet that renders Sydler’s Fundamental Lemma transparent. The applet
departs even further from Jessen’s treatment.
[JKT] leaves a lot to be desired. The notation in [JKT] does not match
the notation in [J] and the theorems proved in [JKT] are much more general
than what is needed for [J]. In these notes, I’ll re-write the proofs in [JKT]
so that they exactly handle the cases needed for Sydler’s Theorem. This
makes the proofs easier.
It took me a long time to claw through the short paper [Z] (translated
from Russian). I’ll follow the logic of Zylev’s paper closely, but improve the
exposition.
 1

2 Tensor Products

Let K be a ﬁeld and let V and W be K-vector spaces. One deﬁnes the tensor
product V ⊗K W as follows: Let X1 denote the set of ﬁnite formal sums

∑ ai(vi, wi); ai ∈ K.

Here (vi, wi) ∈ V × W . This is meant to be a formal sum. We will often
write V ⊗ W in place of V ⊗K W . As usual, 1(v, w) is shortened to (v, w)
whenever it comes up. The various pairs (vi, wj) are not meant to be added
together. X1 is naturally a K-vector space. One has addition

∑ ai(vi, wi) + ∑ bi(vi, wi) = ∑(ai + bi)(vi, wi),

and scaling
 k( ∑ ai(vi, wi)) = ∑ kai(vi, wi).

In the case of addition, we allow some of the coeﬃcients to be 0, so that the
two summands involve the same pairs.
Let X2 ⊂ X1 be the span of the following elements.

• (v1 + v2, w) − (v1, w) − (v2, w).

• (v, w1 + w2) − (v, w1) − (v, w2).

• k(v, w) − (kv, w) and k(v, w) − (v, kw).

Then V ⊗ W = X1/X2,

the quotient vector space.
We have the special elements

v ⊗ w = [(v, w)]. (1)

In case {ei} and {e′
j} are bases for V and W respectively, one can show fairly
readily that {ei ⊗ e′
j} is a basis for V ⊗ W . In case L is a ﬁeld extension
of K, and V is additionally an L-vector space, then V ⊗K W is an L-vector
space. The scaling law is deﬁned by (linearly extending) the rule

λ(v ⊗ w) = (λv) ⊗ w. (2)

2

3 The Result

Say that a dissection of a polyhedron P is an expression P = P1 ∪ ... ∪ Pn,
where the polyhedra Pj and Pk have disjoint interiors for all j ̸= k. Say
that two polyhedra P and Q are scissors congruent if they have dissections
P = P1 ∪ ... ∪ Pn and Q = Q1 ∪ ... ∪ Qn such that Pk and Qk are isometric
for all k. In this case, we write P ∼ Q. Our polyhedra are always closed
subsets.
Both R and R/(πQ) are Q-vector spaces. We deﬁne

W = R ⊗Q R/(πQ).

The Dehn invariant of a polyhedron P is given by

∆(P ) =
 n∑

i=1 li ⊗ [αi] ∈ W. (3)

Here [α] is the equivalence class of α in R/(πQ). The sum takes place over
all edges of P . Here li is the length of the ith edge, and αi is the interior
dihedral angle of that edge.

Theorem 3.1 (Dehn) If P ∼ Q then vol(P ) = vol(Q) and ∆(P ) = ∆(Q).

Proof: The statement about volume is obvious. One checks that the Dehn
invariant is preserved by the dissection process, and also obviously under
isometric motion. That is

∆(P ) = ∑ ∆(Pi) = ∑ ∆(Qi) = ∆(Q). (4)

The main point of the check is that the sum of the dihedral angles around
an interior edge is 2π, which is 0 in R/(πQ). ♠

Here is the celebrated converse result.

Theorem 3.2 (Sydler) If vol(P ) = vol(Q) and ∆(P ) = ∆(Q) then P ∼ Q.

In short

Theorem 3.3 (Dehn-Sydler) Two polyhedra in R3 are scissors congruent
iﬀ they have the same volume and Dehn invariant.

3

4 Zylev’s Theorem

Zylev’s Theorem, proved in [Z], works in great generality. Here we prove
a special case. All sets are (possibly disconnected) polyhedra. We draw a
schematic two dimensional picture, but the argument works in any dimension.

Theorem 4.1 Let A, B ⊂ F . If F − A ∼ F − B then A ∼ B.

Proof: Subdividing F − A and F − B if necessary, we can ﬁnd dissections

F = A ∪
 n⋃

k=1 Pk = B ∪
 n⋃

k=1 Qk; ∀k : Pk ∼ Qk and vol(Pk) < vol(A)
2

We call (A, B, F ) a good triple of order n. Our proof goes by induction on
n. If n = 0 it means that F − A = F − B = ∅, so that A = B. In this case,
we are done. Consider the case n > 0.
Now we consider the induction step. The idea is to “eliminate” Qn in
some sense. The volume bound tells us that A − Qn has greater volume than
Qn. This means that we can fund disjoint T1, ..., Tn ⊂ A − Qn such that

Tk ∼ Pk ∩ Qn.

Figure 1 shows the case n = 3. Note that the sets Tk need not be connected.
But, each Tk is a ﬁnite union of polyhedra. We have schematically drawn T1
and T2 just below P1 and P2 respectively, though in actuality the arrangement
could be much more complicated. Now deﬁne

F ′ = F − Qn; Q′
k = Qk; B′ = F ′ −
 n−1⋃

k=1 Q′
k;

P ′
k = (Pk − Qn) ∪ Tk ∼ Q′
k; A
′ = F ′ −
 n−1⋃

k=1 P ′
k; (5)

No relevant volume changes. Hence (A
′, B′, F ′) is a good triple of order
n − 1. We have B′ = B, and by induction A′ ∼ B′. We just need to show
A
′ ∼ A. The idea is to introduce an intermediate region A
′′ and show that
both A′′ ∼ A
′ and A
′′ ∼ A.
 4

B
 A’’

A’

A

Q2

Q3

Q1
 P1 P2 P3

T2T1

Figure 1: Induction Step

We deﬁne A
′′ as in Figure 1. We have colored this set yellow and gold. A
′′

is obtained from A by exchanging Tk with Qn ∩ Pk for all k. Hence A ∼ A
′′.
We get A
′ from A
′′ by dissecting the yellow/gold Qn and moving the pieces
into (Pn − Qn) ∪ Tn. This is possible because Qn ∼ (Pn − Qn) ∪ Tn. Hence
A
′′ ∼ A
′. Hence A ∼ A
′. ♠
 5

5 Stable Scissors Congruence

Let P denote the abelian group of formal ﬁnite sums

a1P1 + ... + anPn; ak ∈ Z (6)

where P1, ..., Pn are polyhedra in R3. The volume and Dehn invariant extend
linearly to all of P. Let E be the subgroup of P generated by the relations
of the form

• P − (P1 + ... + Pn), where P1 ∪ ... ∪ Pn is a dissection of P .

• P − I(P ), where I is a Euclidean isometry.

We call P and Q stable scissors congruent (SSC) if P ≡ Q mod E.

Lemma 5.1 P ∼ Q if and only if P and Q are SSC.

Proof: It is pretty obvious that scissors congruence implies SSC. For the
interesting half of the result, suppose P, Q are SSC. Spreading the sum in P
so that all coeﬃcients are ±1, we get

P − Q = ∑(Ri − ∑ Rij) − ∑(Si − ∑ Sij) + ∑ (Ti − Ui). (7)

The ﬁrst two terms on the right collect all the dissection relations and the
third term on the right collects all the isometry relations. Hence

P + ∑ Si + ∑ Rij + ∑ Ui = Q + ∑ Ri + ∑ Sij + ∑ Ti.

Suitably translating the polyhedra on each of this equation, we ﬁnd polyhedra
P ′ and Q′ such that

P ∩ P ′ = Q ∩ Q′ = ∅; P ′ ∼ Q′; P ∪ P ′ ∼ Q ∪ Q′.

Let A = P and F = P ∪ P ′. Let θ be the piecewise isometry that carries
Q ∪ Q′ to P ∪ P ′. Let B = θ(Q). Then B ∼ Q and θ deﬁnes a scissors
congruence between F − B and Q′. Hence F − A = P ′ ∼ Q′ ∼ F − B. By
Zylev’s Theorem, A ∼ B. Hence P ∼ Q. ♠

In light of Lemma 5.1, the following result ﬁnishes the proof of the Dehn-
Sydler Theorem.

Theorem 5.2 If vol(P ) = vol(Q) and ∆(P ) = ∆(Q), then P, Q are SSC.

6

6 Introducing Prismssimple prism is any polyhedron aﬃnely equivalent to the product

T × I ⊂ R2 × R = R3.

Here T is a triangle and I is an interval.

Lemma 6.1 A simple prism is SSC to [0, 1] × [0, 1] × [0, v]. Here v is the
volume of the prism.

Proof: Here is a sketch of the argument. Stack an inﬁnite number of copies
of the prism on top of each other. The result is a triangular column. A
Z-subgroup of translations acts on this column. A set of the form T × I is a
fundamental domain for the action, and one sees easily that T × I is SSC to
the original prism. Use 2-dimensional cut-and-paste arguments to show that
T × I is equivalent to a block of the form I1 × I2 × I. Again use 2 dimen-
sional arguments to show that I1×I2×I is equivalent to [0, 1]×[0, 1]×[0, v]. ♠

Let F denote the subgroup of P generated by E and by the simple prisms.
By Dehn’s Theorem (or direct calculation) the Dehn invariant of any simple
prism is 0. Also, we have already mentioned that ∆ vanishes on E. Hence,
∆ vanishes identically on F. Thus, ∆ induces a map

δ : V → W; V = P/F. (8)

Lemma 6.2 If δ is an injection, then Theorem 5.2 is true.

Proof: Suppose that P, Q ∈ P have the same volume and Dehn invariant.
Let ⟨P ⟩ and ⟨Q⟩ denote the equivalence classes in V. Since δ is an injection,
we have ⟨P ⟩ = ⟨Q⟩. That is, ⟨P − Q⟩ = 0. But then, we can write

P − Q = R + S − S′

where R ∈ E and S, S′ are positive sums of simple prisms. Since P − Q and
R both have volume 0, the sums S and S′ have the same volume. But then,
by Lemma 6.1, we have S−S′ ∈ E. Hence P −Q ∈ E. Hence P = Q mod E. ♠

7

7 Vector Space Structure

As we already mentioned (for general extension ﬁelds) the operation given
by r(a ⊗ b) = (ra) ⊗ b makes W into a real vector space. Here we explain
how V is a real vector space. There is an obvious scaling operation on P.
Given λ ∈ R and a polyhedron P one deﬁnes λP to be the result of scaling
P by a factor of λ about the center of mass of P . This scaling operaton then
extends to all of P by linearity. The scaling operation makes sense on V, and
the following things are trivial to verify:

• λ(V1 + V2) = λV1 + λV2.

• λ1λ2(V ) = λ1(λ2(V )).

What is more subtle, we must also show that

(λ1 + λ2)v = λ1v + λ2v; ∀v ∈ V. (9)

Any polyhedron can be dissected into tetrahedra. Hence P is generated
by the tetrahedra. To establish Equation 9 it suﬃces to to show, for an
arbitrary tetrahedron T , that (λ1 + λ2)T can be dissected into two prisms,
and translates of λ1T and λ2T .

Figure 3: Projection to the plane

Start with (λ1 + λ2)T . Stick λ1T (red) into one corner and λ2T (green)
into another corner. Then observe that what is left is the union of 2 prisms
(yellow, blue). Figure 3 shows the view of the top 3 faces on the left, and
the view of the bottom face on the right.
Now we observe that δ : V → W is a real linear map, relative to these
vector space structures.
 8

8 A Reformulation of the Result

An orthoscheme is any tetrahedron isometric to the convex hull of the points

(0, 0, 0); (x, 0, 0); (x, y, 0); (x, y, z).

All the faces of an orthoscheme are right-angled triangles, and 3 of the di-
hedral angles are π/2. The Dehn invariant of an orthoscheme is the 3-term
relation in Lemma 14 below.

Lemma 8.1 V is generated by orthoschemes.

Proof: First, any polyhedron can be dissected into tetrahedra. A tetra-
hedron T which is suﬃciently close to regular can be dissected into 24 or-
thoschemes. Each orthoscheme in this dissection is the convex hull of the
center of the inscribed sphere, the projection of this center to some face of
T , the projection of the center to some edge of T , and a vertex of T . The
same construction, in general, gives an expression of a tetrahedron as a ﬁnite
(signed) sum of orthoschemes in V. ♠

Say that a good function is a map φ : R → V such that

• (P1) φ(π) = 0.

• (P2) φ(a + b) = φ(a) + φ(b) for all a, b ∈ R.

• (P3) For any orthoscheme T , we have ⟨T ⟩ = ∑6
i=1 liφ(αi).

The sum takes place over edges of T .

Lemma 8.2 The existence of a good function implies Theorem 5.2.

Proof: Being an abelian homomorphism from R to V, the map φ is actually
Q-linear. In particular, φ vanishes on πQ. Hence φ induces a well deﬁned
Q-linear map R/(πQ) to V. Now we deﬁne Φ : W → V by linearly extending
the rule Φ(x ⊗ y) = xφ(y). One checks easily that this is well-deﬁned.
Comparing P3 above to the deﬁnition of the Dehn invariant, we have

Φ ◦ δ(⟨T ⟩) = Φ ◦ ∆(T ) = ⟨T ⟩ (10)

for any orthoscheme T . Hence Φ ◦ δ is the identity map on (classes of) or-
thoschemes. But the orthoschemes generate V. Hence Φ ◦ δ is the identity
on V. This is only possible if δ is injective. But this implies Theorem 5.2. ♠

9

9 Constructing the Good Function

Given a ∈ (0, 1), let a′ = √(1/a) − 1. (11)

Note that a = sin2(α) ⇐⇒ a′ = cot(α). (12)

For a, b ∈ (0, 1), let T (a, b) denote the orthoscheme whose vertices are

(0, 0, 0); (a′, 0, 0); (a′, a′b′, 0); (a′, a′b′, b′). (13)

A calculation shows that T (a, b) has 3 right angles. Hence ∆(T (a, b)) is
a 3 term expression. Additional calculations show that this expression is

∆(T (a, b)) = cot(α) ⊗ α + cot(β) ⊗ β + cot(α ∗ β) ⊗ (π/2 − α ∗ β), (14)

where α, β, α ∗ β ∈ (0, π/2) are such that

sin2(α) = a; sin2(β) = b; sin2(α ∗ β) = ab. (15)

In the next section we will produce a function h : (0, 1) → V such that

• (H1) ⟨T (a, b)⟩ = h(a) + h(b) − h(ab).

• (H2) If a + b = 1 then ah(a) + bh(b) = 0.

We call h the homological function. One might say that h is the input from
the homological algebra component of the proof. Assume for now that h
exists. Deﬁne

φ(nπ
2
 ) = 0; and otherwise φ(α) = tan(α)h(sin2(α)). (16)

Property P1 is built into the deﬁnition. It remains to show that φ has
properties P2 and P3. The next result establishes some basic symmetries of
the function φ. The result depends crucially on property H2.

Lemma 9.1 φ(π/2 − α) = −φ(α) and φ(α + π/2) = φ(α).

10

Proof: By deﬁnition, φ(π − α) = −φ(α). So, the ﬁrst identity implies the
second. For the ﬁrst identity, set β = π/2 − α, so that α + β = π/2. We want
to show that φ(α) + φ(β) = 0. Let a = sin2(α) and b = sin2(β). Note that
h(a) = φ(α) cot(α), and similarly for b. We have a+b = sin2(α)+sin2(β) = 1.
Hence, by property H2,

0 = 2ah(a) + 2bh(b) = 2 sin2(α)φ(α) cot(α) + 2 sin2(β)φ(β) cot(β) =

2 cos(α) sin(α)φ(α) + 2 cos(β) sin(β)φ(β) =

sin(2α)φ(α) + sin(2β)φ(β) = sin(2α)(φ(α) + φ(β)).

The last equality, which gives us what we want, follows from the fact that
sin(2α) = sin(2β). ♠

Lemma 9.2 φ satisﬁes P3.

Proof: By scaling, it suﬃces to prove P3 for orthoschemes of the form
T (a, b). We have

h(a) = cot(α)φ(α); h(b) = cot(β)φ(β);

h(ab) = cot(α ∗ β)φ(α ∗ β) = − cot(α ∗ β)φ(π/2 − α ∗ β).

Hence ⟨T (a, b)⟩ = h(a) + h(b) − h(ab) =

cot(α)φ(α) + cot(β)φ(β) + cot(α ∗ β)φ(π/2 − α ∗ β) =
 6∑

i=1 liφ(αi).

The other three terms in the last sum vanish, because the corresponding di-
hedral angles are right angles. ♠

By Lemma 9.1, it suﬃces to establish P2 when α, β ∈ (0, π/2).

Lemma 9.3 Let α, β, γ ∈ (0, π/2) be such that α + β + γ = π. Then it is
possible to dissect a rectangular solid into 6 orthoschemes, all sharing a com-
mon diagonal of the solid, such that the dihedral angles (in pairs) associated
to this diagonal are α, β, γ.
 11

Proof: One can orthogonally project an orthoscheme into the plane so that
the longest diagonal maps to a point. The image of the orthoscheme is a
triangle. At the same time, one can orthogonally project a rectangular solid
R into the plane so that one of the diagonals maps to a point. The resulting
ﬁgure is a hexagon with opposite sides parallel, and with each main diagonal
parallel to a pair of opposite sides.

Figure 4: Projection to the plane

The 6 triangles in Figure 4 are all projections of the orthoschemes from
Lemma 9.3. The angles of these triangles, around the central vertex, corre-
spond to the dihedral angles around the diagonal of interest. Adjusting R, we
can make the three angles whatever we like, subject to the given constraints.
♠
 Let R be the rectangular solid from Lemma 9.3. We have ⟨R⟩ = 0 in
V. We scale R so that its diagonals have length 1. We apply P3 to the 6
orthoschemes involved to get:

0 = ⟨R⟩ = (2φ(α) + 2φ(β) + 2φ(γ)) +
 6∑

k=1 lk(φ(θk1) + φ(θk2)). (17)

The ﬁrst summand comes from the angles around the diagonal of interest
to us. The remaining nonzero terms are grouped into 6 pairs, corresponding
to the edges of R that project to the “spokes” of the hexagon above. Each
pair of angles adds to π/2. Applying Lemma 9.1 and summing over these 6
edges, we ﬁnd that the last sum in Equation 17 vanishes. Hence

φ(α) + φ(β) = −φ(γ) = φ(π − γ) = φ(α + β). (18)

This establishes P2.
 12

10 Constructing the Homological Function

Let V be a real vector space. Given g : R+ → V , deﬁne

δg(a, b) = g(a) + g(b) − g(ab). (19)

If δg = 0, then g is a homomorphism. Given F : R2
+ → V we deﬁne

δF (a, b, c) = F (a, b) − F (a, c) + F (ab, c) − F (ac, b). (20)

A short calculation shows that δg is symmetric and δδg = 0.
Note that these deﬁnitions make sense when (0, 1) replaces R+. We will
have occasion to consider both situations.
Here is the ﬁrst result from [JKT].

Theorem 10.1 Let F : (0, 1)2 → V be symmetric with δF = 0. Then
F = δf for some f : (0, 1) → V .

To apply Theorem 10.1, we set V = V and we set F (a, b) = ⟨T (a, b)⟩.
Since T (a, b) and T (b, a) are isometric, we have F (a, b) = F (b, a). Here is
the main geometric lemma behind Sydler’s Theorem.

Lemma 10.2 (Sydler’s Fundamental Lemma) δF = 0.

Applying Theorem 10.1, we ﬁnd that there is some function f which
satisﬁes property H1. Note that h = f − g also satisﬁes H1 if δg = 0. To get
property H2, it suﬃces to show that there exists such a g such that

ag(a) + bg(b) = af (a) + bf (b)

when a + b = 1.
Now we invoke the second result from [JKT].

Theorem 10.3 Let G : R2
+ → V be a symmetric function satisfying

• G(λa, λb) = λG(a, b) for all λ, a, b.

• G(a, b) + G(a + b, c) = G(a, c) + G(a + c, b).

Then there is a homomorphism g : (0, ∞) → V such that

a + b = 1 =⇒ G(a, b) = ag(a) + bg(b). (21)

13

To apply this result, we deﬁne G : R2
+ → V as

G(a, b) = af ( a
a + b
 ) + bf ( b
a + b
 ) (22)

We have G(a, b) = G(b, a) and G(λa, λb) = λG(a, b) and

a + b = 1 =⇒ G(a, b) = af (a) + bf (b). (23)

Lemma 10.4 G(a, b) + G(a + b, c) = G(a, c) + G(a + c, b) for all a, b, c ∈ R+.

When we expand out this relation in terms of f and groups terms, we see
that it boils down to the identity

aF ( a + b
a + b + c, a
a + b
 ) + bF ( a + b
a + b + c, b
a + b
 ) =

aF ( a + c
a + b + c , a
a + c
 ) + cF ( a + c
a + b + c, c
a + c
 ).

This identity comes down to a certain dissection problem. Say that the
corner C(x, y, z) is the tetrahedron with vertices

O = (0, 0, 0); X = (x, 0, 0); Y = (0, y, 0); Z = (0, 0, z).

A corner can be divided into two orthoschemes in three diﬀerent ways. For
example one lets ΠX be the plane containing OX and also the point PX ∈ Y Z
that OP X is perpendicular to Y Z. Then ΠX divides the C(x, y, z) into two
orthoschemes. One gets two other such divisions by permuting the letters.
Equating any two of these subdivisions in V gives a relation. When

x = (bc)1/2; y = (ac)1/2; z = (ab)1/2

and we use ΠX and ΠY , we get the above relation after some computation. ♠

This shows the existence of the desired homomorphism g. Again, the
function h = f − g satisﬁes H2 as well as H1.

14

11 Sketch of Lemma 10.2

To be sure, Jessen checks that T (a, b) + T (ab, c) and T (a, c) + T (ac, b) have
the same volume and Dehn invariant. The volume calculation is elementary.
The Dehn invariant calculation follows from Equation 14.
As a prelude to the main construction, Jessen identiﬁes a certain family
of polyhedra which I’ll call pseudoprisms. A pseudoprism OP QRS satisﬁes
|QS| = 2|P R| and projects orthogonally to an isosceles triangle, as shown in
the top left corner of Figure 5. By chopping oﬀ a suitable tetrahedron from
a pseudoprism and gluing it in a diﬀerent way, one obtains a prism. Figure
5 shows two views of a pseudoprism and the corresponding prism.

O R

P QO
 S

P,R
 Q,S

Figure 5: Pictures of a pseudoprism

Now we come to the main construction. Things are arranged so that
T (a, b) is given vertices ABCD and T (a, c) is given vertices ABEF , and

• BCD and BEF lie in a plane Π0.

• ABC and ABF lie in a plane Π1.

• ABD and ABE lie in a plane Π2.

• Π1 and Π2 are orthogonal to Π0.

(Note: Jessen considers the case when BC and EF do not cross. The crossing
case is similar.) Figure 6 shows the orthogonal projections to each of these
planes. The blue-labelled points lie in the relevant plane, and the black-
labelled points lie to one side. Some points get more than one label. Only
the projection to Π0 shows all the points.

15
 L

I
 M
 K

J
 K

K

E FDB

A
 G
 MJH

Π1

B F

I L

C GD
 HA
Π0
 Π2

H

D

C
 F

G
B
 E

A
 Figure 6: Projections

Again, T (a, b) = ABCD; T (a, c) = ABEF.

The points in this ﬁgure obey certain distance relations:

• ACDEF KLM are all equidistant from H.

• G, I, J are the projections of H respectively to Π0, Π1, Π2.

• CDEF, ACF L, ADEM are equidistant from G, I, J respectively.

• DGF, AHK, AIL, AJM are each evenly spaced and collinear.

• |M K| = |EF | and |KL| = |CD|

• angle(AM D) = angle(AED) and angle(ALF ) = angle(ACB)

These relations, especially the last two, imply

T (ab, c) = ADM K; T (ac, b) = AF LK.

Now let P be the polyhedron with vertics ABDF HIJ. By comparing
the boundaries of the various polyhedra involved, one shows that

P − (AICHD) − (F ICHD) + (DJM HK) = T (a, b) + T (ab, c)

P + (DJEHF ) − (AJEHF ) + (F ILHK) = T (a, c) + T (ac, b)

where the 6 polyhedra (...) are the pseudoprisms in Figure 6.

16

12 Proof of Theorem 10.1

12.1 A Technical Lemma

Lemma 12.1 Let F : R2
+ → V be a function satisfying

• F (a, b) = F (b, a) for all a, b.

• F (a, b) + F (ab, c) = F (a, c) + F (ac, b) for all a, b, c.

• F (a, 1) = F (a, 1/a) = 0 for all a.

Then F (a, b) = f (a) + f (b) − f (ab) for some f : R+ → V .

Let W = R+ × V . Equip W with the operation

(a, x) + (b, y) = (ab, x + y + F (a, b)). (24)

Lemma 12.2 W is an abelian group.

Since F (a, b) = F (b, a), the operation is commutative. The operation is
associative because the two quantities below are equal.

(a, x) + ((b, y) + (c, z)) = (a + b + c, x + y + z, F (b, c) + F (bc, a)).

((a, x) + (b, y)) + (c, z) = (a + b + c, x + y + z, F (b, a) + F (ba, c)).

(1, 0) is the zero element because F (1, a) = 0, and (a, x)−1 = (1/a, x). ♠

Lemma 12.3 Let π : W → R+ be projection. Suppose there is a subgroup
S ⊂ W such that π : S → R+ is a bijection. Then Lemma 12.1 is true.

Proof: Let πV : W → V be projection. Deﬁne f (a) = −πV ◦ π−1(a). Let
x = f (a) and y = f (b). Since π is a homomorphism, bijective on S, the map
π−1 : R+ → S is a group isomorphism. The following calculation ﬁnishes
the proof.
 −f (ab) = πV ◦ π−1(ab) = πV ◦ ((a, x) + (b, y)) =

πV ◦ (ab, x + y + F (a, b)) = −f (a) − f (b) + F (a, b). ♠

17

To ﬁnish the proof of Lemma 12.1, we need to produce the subgroup S.
Let A = R+ for this proof. Here the group law is multiplication. The proof
goes by transﬁnite induction. Note that π(1, 0) = 1. So, we start with the
two trivial subgroups:
 S0 = {(1, 0)}; A0 = {1}.

Now we consider the induction step. Let S1 ⊂ W be a subgroup of W and
let A1 = π(S1). Choose a ∈ A − A1. Let A2 = ⟨A1, a⟩ be the subgroup
generated by A1 and a. Let
 S2 = ⟨S1, (a, x)⟩.

For any choice of x, the sets A2 and S2 are subgroups and π(S2) = A2. We
just have to choose x so that π : S2 → A2 is injective. Any element of π−1(0)
has the form
 [S1] + n(a, x) = [S1] + (an, nx +
 n−1∑

i=1 F (a, ai))
. (25)

Here [S1] denotes some element of S1. Note also that an = −π([S1]) ∈ A1.
If we knew that n(a, x) ∈ S1 then we could conclude that the above element
equals 0W , because π : S1 → A1 is injective. So, we are reduced to the
following problem: Choose x such that

an ∈ A1 =⇒ n(a, x) ∈ S1. (26)

If the left side of Equation 26 never happens, then any choice of x will work.
Otherwise, since S1 is a subgroup, just have to solve the problem for the
minimum positive n such that an ∈ A1. For this value of n, there is some
unique v = vn ∈ V such that
 (an, v) ∈ S1. (27)

We can solve for x:
 x = 1
n
 (v −
 n−1∑

i=1 F (a, ai)) (28)

This choice of x does the job.
 18

12.2 The Extension

Suppose that F : (0, 1) → V satisﬁes the hypotheses of Theorem 10.1. To
apply Lemma 12.1, we just have to show that F extends to some ̂F : R+ → V
satisfying the hypotheses of Lemma 12.1. Then we let ̂f : R+ → V be the
function from Lemma 12.1, and we let f be the restriction of ̂f to (0, 1).
Let T (a, b) = (ab, 1/a). (29)

T and its powers deﬁne an order 6 group action on R2
+, and the domain
of deﬁnition of F , namely {(a, b)| a < 1, b < 1}, is a fundamental domain.
We deﬁne ̂F in such a way that ̂F ◦ T = − ̂F . Concretely, we introduce the
symbol (±, ±, ±) according to the sign of (1 − a, 1 − b, 1 − ab). Our extension
is as follows:

• + + +: ̂F (a, b) = +F (a, b).

• − + +: ̂F (a, b) = −F (ab, 1/a).

• − + −: ̂F (a, b) = +F (b, 1/(ab)).

• − − −: ̂F (a, b) = −F (1/a, 1/b).

• + − −: ̂F (a, b) = +F (1/(ab), a).

• + − +: ̂F (a, b) = −F (ab, 1/b).

A case by case analysis shows that the second hypotheses of Lemma 12.1
is also satisﬁed. For instance, suppose that the triple (a, b, ab) and (a, c, ac)
are of types (−, +, +) and (−, +, −) and abc < 1 Then (ab, c) is of type
(+, +, +) and (ac, b) is of type (−, +, +). Then

̂F (a, b) + ̂F (ab, c) = −F (ab, 1/a) + F (ab, c);

̂F (a, c) + ̂F (ac, b) = F (c, 1/(ac)) − F (abc, 1/(ac)).

Using symmetry, we see that the two relevant quantities are equal iﬀ

F (c, ab) + F (cab, 1/(ac)) = F (c, 1/(ac)) + F (1/a, ab).

Setting α = c and β = ab and γ = 1/(ac), we ﬁnd that the last expression
is the same as F (α, β) + F (αβ, γ) = F (α, γ) + F (αγ, β), which is true given
the properties of F . The other cases are similar. In [JKT], a more concep-
tual (and diﬃcult) argument is also given, which eliminates the case-by-case
checking.
 19

13 Proof of Theorem 10.3

13.1 A Variant

The following variant of Theorem 10.3 is proved in [JKT].

Theorem 13.1 Let G : (0, ∞)2 → R be a function satisfying the hypotheses
of Theorem 10.3. Then there is a function γ : (0, ∞) → V such that

G(a, b) = γ(a + b) − γ(a) − γ(b); γ(ab) = bγ(a) + aγ(b). (30)

Let’s deduce Theorem 10.3 from Theorem 13.1. Let g(x) = −γ(x)/x. We
compute

g(ab) = − γ(ab)
ab = − bγ(a)
ab − aγ(b)
ab = − γ(a)
a − γ(b)
b = g(a) + g(b).

In general, we have

G(a, b) = ag(a) + bg(b) − (a + b)g(a + b).

Note that g(1) = 0. So, when a + b = 1, we have G(a, b) = ag(a) + bg(b).
This shows that Theorem 13.1 implies Theorem 10.3.

13.2 Another Technical Lemma

Lemma 13.2 Let G : R2 → V be a function satisfying the hypotheses of
Theorem 10.3, and also G(a, 0) = G(a, −a) = 0 for all a. Then there exists
a map γ : R → V such that

G(a, b) = γ(a + b) − γ(a) − γ(b); γ(ab) = bγ(a) + aγ(b).

Now we turn to the proof of Lemma 13.2. On W = R × V deﬁne

(a, x)+(b, y) = (a+b, x+y +G(x, y)); (a, x)(b, y) = (ab, bx+ay). (31)

Lemma 13.3 W is a commutative ring with 1.

Proof: The same argument, with (R, +) in place of (R+, ×) shows that
W , equipped with the ﬁrst operation, is an abelian group. The 0 element is
(0, 0). A short calculation shows that the multiplication law is commutative
and associative, and that (1, 0) is the “one” of the ring. Finally, the condition
G(λa, λb) = λG(a, b) translates into the distributive law. ♠

20

Lemma 13.4 Let π : W → R be projection. Suppose that there is a subring
S ⊂ W such that π : S → R is a bijection. Then Lemma 13.2 is true.

Proof: Let πV : W → V be projection. Deﬁne γ(a) = πV ◦π−1(a). The same
argument as in Lemma 12.3 shows that G(a, b) = γ(a + b) − γ(a) − γ(b). This
is the ﬁrst condition. For the second condition, let x = γ(a) and y = γ(b).
Since π is a ring homomorphism, bijective on S, the map π−1 : R → S is a
ring isomorphism. We have

γ(ab) = πV ◦ π−1(ab) = πV (π−1(a) × π−1(b)) =

πV ((a, x)(b, y)) = πV (ab, ay + bx) = ay + bx = aγ(b) + bγ(a).

This does it. ♠

To ﬁnish the proof, we have to produce the subring S ⊂ W such that
π : S → R is a bijection. For this proof, we set A = R. We set S0 = Z1,
where 1 is the unity of the ring W . As the same time, we set A0 = Z ⊂ A.
So far, S0 and A0 are subrings and π : S0 → A0 is a bijection. We will again
argue by transﬁnite induction.
Suppose by induction that we have a subring S1 ⊂ S and a corresponding
subring A1 ⊂ A, such that π : S1 → A1 is an isomorphism. Choose some
a ∈ A − A1. Let A2 = A[a]; S2 = A[(a, x)] (32)

where x ∈ V is yet to be speciﬁed. No matter how we choose x, the map
φ : S2 → A2 is a surjective ring map. We want to choose x so that φ is also
injective.
Let T be a dummy variable. The rings A1 and S1 are isomorphic. Hence,
the polynomial rings A1[T ] and S1[T ] are isomorphic. Let P denote the poly-
nomial in S1[T ] corresponding to the polynomial P ∈ A1[T ]. By construction
π(P ) = P . We just need to make our choice of x such that

P (a) = 0 =⇒ P (a, x) = (0, 0). (33)

If a is transcendental over A1, then the above equation is vacuous, and any
choice of x will work.
Suppose that a is algebraic over A1 and that Q is polynomial of minimal
degree such that Q(a) = 0.
 21

Lemma 13.5 There exists x ∈ V such that Q(a, x) = (0, 0).

Proof: Since G(a, 0) = 0, we have (a, x) = (0, x) + (a, 0). Note also that

(0, x)k = (0, x)(0, x) × (0, x)k−2 = (0, 0); k = 2, 3, 4...

We have

Q(a, x) =1 Q(a, 0) + Q′(a, 0)(0, x) =2 (0, z) + (b, y)(0, x) = (0, z + bx). (34)

Equality 1 comes from expanding Q in a Taylor series about (a, 0) and noting
that all higher order terms vanish. Equality 2 comes from Q(a) = 0 and from
the fact that Q′(a) = b ̸= 0. We have b ̸= 0 because Q′ is nontrivial and has
lower degree than Q. Since b ̸= 0, we can choose x such that Q(a, x) = 0. ♠

The following result ﬁnishes the induction step.

Lemma 13.6 Let x be as above. If P (a) = 0 then P (a, x) = (0, 0).

Proof: Using long division of polynomials, and the minimal degree of Q, we
can ﬁnd some nonzero d ∈ A1 such that dP = QR. Letting

d = π−1(d) = (d, u) ∈ S1,

we have
 (0, dz) = (d, u)(0, z) = d P (a, x) = Q(a, x)R(a, x) = (0, 0).

Hence z = 0. Hence P (a, x) = (0, 0). ♠

13.3 Another Extension Lemma

The extension that promotes Lemma 13.2 to Theorem 10.3 is exactly the
same as we already did, except that we extend from (R+, +) to (R, +) instead
of extending from ((0, 1), ×) to (R+, ×). In short, we work with the group law
formed by addition rather than with the group law formed by multiplication.
Once this change is made, the extension is identical. For example, the (+−−)
case here reads

a > 0, b < 0, a + b < 0; =⇒ ̂G(a, b) = +F (−a − b, a).

The only new step here here is that we also must verify that

̂G(λa, λb) = λ ̂G(a, b),

but this is immediate from the deﬁnitions.

22

14 References

[D] M. Dehn, Uber Dem Rauminhalt, Math Ann. 55 (1902) 465-478

[J] Borge Jessen, The algebra of polyhedra and Sydler’s theorem, Math Scand
22 (1968) pp 241-256

[JKT] Borge Jessen, Jorgen Karfp, Anders Thorup, Some Functional Equa-
tions in Groups and Rings, Math Scand 22 (1968) pp 257-265

[S] J-P Sydler, Conditions necessarires et suﬃsiantes pour l’equivalence des
polyedres de l;espace euclidean a trois dimensions, Comment Math Helv. 40
(1965) 43-80.

[Z] Zylev, Equicomposability of equicomplementary polyhedra, Soviet Math
Doklady 161 (1965, translated to English) pp 453-455

23
