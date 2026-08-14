<!-- source: https://math.ovgu.de/Institute/IAG/Lehrveranstaltungen/wise15/GP/_/ln_lattice_polytopes-version-by-paffenholz.pdf | converted from PDF -->

Lecture Notes on Lattice Polytopes

(preliminary version of December 7, 2012)

Winter 2012
Fall School on Polyhedral Combinatorics
TU Darmstadt

Christian Haase • Benjamin Nill • Andreas Paffenholz

text on this page — prevents rotating

Chapter
Contents

1 Polytopes, Cones, and Lattices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
1.1 Cones . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
1.2 Polytopes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
1.3 Lattices . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 18

2 An invitation to lattice polytopes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 19
2.1 Lattice polytopes and unimodular equivalence . . . . . . . . . . . . . . . . . . . 20
2.2 Lattice polygons . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
2.3 Volume of lattice polytopes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 24
2.4 Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 26

3 Ehrhart Theory . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.1 Motivation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.1.1 Why do we count lattice points? . . . . . . . . . . . . . . . . . . . . . . . . . 27
3.1.2 First Ehrhart polynomials . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
3.2 Triangulations and Half-open Decompositions . . . . . . . . . . . . . . . . . . . 30
3.3 EHRHART’s Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 33
3.3.1 Encoding Points in Cones: Generating Functions . . . . . . . . . . 33
3.3.2 Counting Lattice Points in Polytopes . . . . . . . . . . . . . . . . . . . . . 37
3.3.3 Counting the Interior: Reciprocity . . . . . . . . . . . . . . . . . . . . . . . 41
3.3.4 Ehrhart polynomials of lattice polygons . . . . . . . . . . . . . . . . . . 45
3.4 The Theorem of Brion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
3.5 Computing the Ehrhart Polynomial: Barvinok’s Algorithm . . . . . . . . 48
3.5.1 Basic Version of the Algorithm . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
3.5.2 A versatile tool: LLL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 52
3.6 Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 57

4 Geometry of Numbers . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
4.1 Minkowski’s Theorems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
4.2 Lattice packing and covering . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 64
4.3 The Flatness Theorem . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
4.4 Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 68

5 Reﬂexive and Gorenstein polytopes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
5.1 Reﬂexive polytopes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
5.1.1 Dimension 2 and the number 12 . . . . . . . . . . . . . . . . . . . . . . . . . 71
5.1.2 Dimension 3 and the number 24 . . . . . . . . . . . . . . . . . . . . . . . . . 72
5.2 Gorenstein polytopes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 74
5.3 The combinatorics of simplicial reﬂexive polytopes . . . . . . . . . . . . . . 77
5.3.1 The maximal number of vertices . . . . . . . . . . . . . . . . . . . . . . . . . 77

— vii —

viii
 5.3.2 The free sum construction . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
5.3.3 The addition property . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
5.3.4 Vertices between parallel facets . . . . . . . . . . . . . . . . . . . . . . . . . . 79
5.3.5 Special facets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
5.4 Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 81

6 Unimodular Triangulations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
6.1 Regular Triangulations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
6.2 Pulling Triangulations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
6.3 Compressed Polytopes . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 84
6.4 Special Simplices in Gorenstein Polytopes . . . . . . . . . . . . . . . . . . . . . . . 86
6.5 Dilations . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
6.5.1 Composite Volume . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
6.5.2 Prime Volume . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 89
6.6 Problems . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 90

References . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 91

Index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 93

Name Index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 97

1
Polytopes, Cones, and Lattices

In this chapter we want to introduce the basic objects that we will look at for the
rest of the semester. We will start with polyhedral cones, which are the intersection
of a ﬁnite set of linear half spaces. Generalizing to intersections of afﬁne half
spaces leads to polyhedra. We are mainly interested in the subset of bounded
polyhedra, the polytopes. Specializing further, we will deal with integral polytopes.
We will not prove all theorems in this chapter. For more on polytopes you may
consult the book of Ziegler [28].
In the second part of this chapter we link integral polytopes to lattices, discrete
subgroups of the additive group Rd . This gives a connection to commutative al-
gebra by interpreting a point v ∈ Zd as the exponent vector of a monomial in d
variables.
We use Z, Q, R and C to denote the integer, rational, real and complex num-
bers. We also use Z>, Z≥, Z<, Z≤, R<, R≤, R>, R≥.

1.0.1 Deﬁnition. Let x1, . . . , xk ∈ Rn, and λ1, . . . , λk ∈ R. Then ∑k
i=1 λi xi is
called a linear combination of the vectors x1, . . . , xk. It is further a
(1) conic combination, if λi ≥ 0,
(2) afﬁne combination, if ∑k
i=1 λi = 1, and a
(3) convex combination, if it is conic and afﬁne.
The linear (conic, afﬁne, convex) hull of a set X ∈ Rn is the set of all points that
are a linear (conic, afﬁne, convex) combination of some ﬁnite subset of X . It is
denoted by lin(X ) (or, cone(X ), aff(X ), conv(X ), respectively). X is a linear space
(cone, afﬁne space, convex set if X equals its linear hull (or conic hull, afﬁne hull,
convex hull, respectively).

1.0.2 Deﬁnition (hyperplanes and half-spaces). For any non-zero α ∈ (Rd )
⋆

and δ ∈ R the set
 1

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

Figure missing

Fig. 1.1
 Hα,δ := {x | α(x) ≤ 0} is an afﬁne hyperplane, and

Hα := {x | α(x) ≤ δ} is a linear hyperplane.

The corresponding positive and negative half-spaces are

H +
α,δ := {x | α(x) ≥ δ} H −
α,δ := {x | α(x) ≤ δ}

H +
α := {x | α(x) ≥ 0} H −
α := {x | α(x) ≤ 0} .

Then H +
α,δ ∩ H −
α,δ = Hα,δ. Let H := Hα,b ⊆ Rd be a hyperplane. We say that a point
y ∈ Rd is beneath H if α( y) < b and beyond H if α( y) > b.

1.1 Cones

Cones are the basic objects for most of what we will study in these notes. In
this section we will introduce two deﬁnitions of polyhedral cones. The WEYL-
MINKOWSKI Theorem will tell us that these two deﬁnitions coincide. In the next
section we will use this to study polytopes. Cones will reappear prominently when
we start counting lattice points in polytopes. In the next chapter we will learn
that counting in polytopes is best be done by studying either the cone over the
polytope, or the vertex cones of the polytope.

1.1.1 Deﬁnition. A subset C ⊆ Rd is a cone if for all x, y ∈ C and λ, µ ∈ R≥ also
λx +µ y ∈ C. A cone C is polyhedral (ﬁnitely constrained) if there are α1, . . . , αm ∈
(Rd )
⋆ such that

C =
 m⋂

i=1 H −
αi = {x ∈ Rn | αi(x) ≤ 0 for 1 ≤ i ≤ m}. (1.1.1)

A cone C is called ﬁnitely generated by vectors v1, . . . , vr ∈ Rn if

C = cone(v1, . . . , vn) :=
 ( n∑

i=1 λi vi | λi ≥ 0 for 1 ≤ i ≤ n
)
 . (1.1.2)

It is easy to check that any set of the form (1.1.1) or (1.1.2) indeed deﬁnes a
cone.

1.1.2 Example. See Figure 1.1.

The two notions of a ﬁnitely generated and ﬁnitely constrained cone are in fact
equivalent. This is the result of the WEYL-MINKOWSKI Duality for cones.

1.1.3 Theorem (WEYL-MINKOWSKI Duality for Cones). A cone is polyhedral if and
only if it is ﬁnitely generated.

We have to defer the proof a little bit until we know more about cones.

1.1.4 Lemma. Let C ⊆ Rd+1 be a polyhedral cone and π : Rd+1 → Rd the projec-
tion onto the last d coordinates. Then also π(C) is a polyhedral cone.

Proof. We use a technique called FOURIER-MOTZKIN Elimination for this. Let C be
deﬁned by
 C = {(x0, x) | λi x0 + αi(x) ≤ 0 for 1 ≤ i ≤ n}

for some linear functionals αi ∈ (Rd )
⋆ and λi ∈ R, 1 ≤ i ≤ m. Then

— 2 — Haase, Nill, Paffenholz: Lattice Polytopes

Polytopes, Cones, and Lattices (preliminary version of December 7, 2012)

C ′ := π(C) = {x | ∃x0 ∈ R : (x0, x) ∈ C} .

We can assume that there are a, b ∈ Z≥ such that

λi =
 





= 0 for 1 ≤ i ≤ a
> 0 for a + 1 ≤ i ≤ b
< 0 for b + 1 ≤ i ≤ m .

Deﬁne functionals βi j := λiα j − λ jαi for a < i ≤ b < j ≤ m. Then

C ′ ⊆ D := {x | αi(x) ≤ 0, 1 ≤ i ≤ a, βi j(x) ≤ 0, a < i ≤ b < j ≤ m} .

We want to show D ⊆ C ′. Let x ∈ D. Then for any x0 ∈ R and 1 ≤ i ≤ a

λi x0 + αi(x) ≤ 0 ,

as λi = 0. Further, βi j(x) ≤ 0 implies

1

λ j α j(x) ≥ 1

λi αi(x)

for all a < i ≤ b < j ≤ m. Hence, there is x0 such that

min
a+1≤i≤b
 ‡ 1

λ j α j(x)

„
 ≤ −x0 ≤ max
b+1≥ j≤m
  1

λi αi(x)
 .

This means
 λi x0 + α(x) ≤ 0 for a + 1 ≤ i ≤ b

λ j x0 + α(x) ≤ 0 for b + 1 ≤ j ≤ m .

Hence, (x0, x) in C, so x ∈ C ′. ⊓⊔

This sufﬁces to prove one direction of the WEYL-MINKOWSKI Theorem.

1.1.5 Theorem (WEYL’s Theorem). Let C be a ﬁnitely generated cone. Then C is
polyhedral.

Proof. Let v1, . . . , vn ∈ Rd be generators of C, i.e.

C :=
 ( n∑

i=1 λi vi | λi ≥ 0 for 1 ≤ i ≤ n
)
 .

Then
 C =
 (
x ∈ Rd | ∃λ1, . . . , λn ∈ R : x −
 n∑

i=1 λi vi = 0, λ1, . . . , λn ≥ 0
)
 .

The cone C is the projection onto the last d coordinates of the set

C ′ :=
 (
(λ, x) | x −
 n∑

i=1 λi vi = 0, λ1, . . . , λn ≥ 0
)
 .

This is clearly a polyhedral cone. By Lemma 1.1.4 C is polyhedral. ⊓⊔
 Figure missing

Fig. 1.2

Haase, Nill, Paffenholz: Lattice Polytopes — 3 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

Figure missing

Fig. 1.3
 1.1.6 Theorem (FARKAS Lemma). Let a cone C be generated by v1, . . . , vn ∈ Rd .
Then for x ∈ Rd exactly one of the following holds.

(1) x ∈ C, or
(2) there is α ∈ (Rd )
⋆ such that α( y) ≤ 0 for all y ∈ C and α(x) > 0.

The second option thus tells us that if x ̸∈ C, then there is a hyperplane that
separates x from the cone C.

Proof (of Theorem 1.1.6). We show ﬁrst that not both conditions can hold at the
same time. Assume that there is λ1, . . . , λn ≥ 0 such that x = ∑n
i=1 λi vi and α
such that α( y) ≤ 0 for all y ∈ C, but α(x) > 0. Then

0 < α(x) = α
   n∑

i=1 λi vi
!
 =
 n∑

i=1 λiα(vi) ≤ 0 ,

a contradiction.
By WEYL’s Theorem 1.1.5, the cone C is polyhedral, i.e. there are linear func-
tionals α1, . . . , αm ∈ (Rd )
⋆ such that

C = { y | α1( y) ≤ 0, . . . , αm( y) ≤ 0} .

Now x ̸∈ C holds if and only if there 1 ≤ j0 ≤ m such that α j0 (x) > 0. However,
v1, . . . , vn ∈ C implies, that for any λ1, . . . , λn and 1 ≤ j ≤ m

α j
   n∑

i=1 λi vi
!
 =
 n∑

i=1 λiα j(vi) ≤ 0 .

Any y ∈ C has a representation as y = ∑n
i=1 λi vi for some λi ≥ 0, 1 ≤ i ≤ n.
Hence, α j0 ( y) ≤ 0 for all y ∈ C, and α is as desired. ⊓⊔

1.1.7 Deﬁnition (polar (dual)). Let X ⊆ Rd . The polar (dual) of X is the set

X ⋆ := ¦
α ∈ (Rd )
⋆ | α(x) ≤ 0 for all x ∈ X © ⊆ (Rd )
⋆ .

See Figure 6.2 for an example of the dual of a cone. If X = cone(v1, . . . , vn) is a
ﬁnitely generated cone, then it is immediate from the deﬁnition of the dual cone
that it sufﬁces to check the condition α(x) ≤ 0 for the generators v1, . . . , vn of X .
Using this we can rephrase the FARKAS Lemma.

1.1.8 Corollary (FARKAS Lemma II). Let C ⊆ Rd be a ﬁnitely generated cone and
x ∈ Rd . Then either x ∈ C or there is α ∈ C ⋆ such that α(v) ≤ 0 for all v ∈ C and
α(x) > 0 but not both. ⊓⊔

We want to examine descriptions of the dual of a polyhedral and a ﬁnitely
generated cone.

1.1.9 Proposition. Let C := cone(v1, . . . , vn) be a ﬁnitely generated cone. Then
C ⋆ = {α | vi(α) = α(vi) ≤ 0 for 1 ≤ i ≤ n}. In particular, C ⋆ is polyhedral.

Proof. Let α ∈ C ⋆. By deﬁnition this means that α(x) ≤ 0 for any x ∈ C. Hence,
α(vi) ≤ 0 for 1 ≤ i ≤ n.
If conversely α satisﬁes α(vi) ≤ 0 for 1 ≤ i ≤ n, then for any λ1, . . . , λn ≥ 0

α
   n∑

i=1 λi vi
!
 =
 n∑

i=1 λiα(vi) ≤ 0 ,

— 4 — Haase, Nill, Paffenholz: Lattice Polytopes

Polytopes, Cones, and Lattices (preliminary version of December 7, 2012)

hence α ∈ C ⋆. ⊓⊔

Clearly, we can repeat the process of dualization. We abbreviate (X ⋆)
⋆ by X ⋆⋆. The
notion of dualization suggests that repeating this process should bring us back to
where we started. This is, however not, true in general. It is, if we have ﬁnitely
generated cones, by the next lemma.

1.1.10 Lemma. Let C ⊆ Rd be a ﬁnitely generated cone. Then C ⋆⋆ = C.

Proof. Let C := cone(v1, . . . , vn) for some v1, . . . , vn ∈ Rd . Then C ⋆ = {α ∈ (Rd )
⋆ |
α(vi) ≤ 0 for 1 ≤ i ≤ n}.
If x ∈ C, then α(x) ≤ 0 for all α ∈ C ⋆. Hence, x ∈ C ⋆⋆. Conversely, if x ̸∈ C,
then by FARKAS Lemma II (Corollary 1.1.8), we know that there is α ∈ C ⋆ such
that αi(vi) ≤ 0 for 1 ≤ i ≤ n and α(x) > 0. Hence, x ̸∈ C ⋆⋆. ⊓⊔

This immediately implies the following description of the dual of a polyhedral
cone.

1.1.11 Corollary. Let C := {x | α1(x) ≤ 0, . . . , αm(x) ≤ 0} be a polyhedral cone.
Then C ⋆ = cone(α1, . . . , αm). ⊓⊔

With this observation we can prove the converse direction of the WEYL-MINKOWSKI
Theorem.

1.1.12 Theorem (MINKOWSKI’s Theorem). Let C be a polyhedral cone. Then C is
non-empty and ﬁnitely generated.

Proof. Let C := {x | α1(x) ≤ 0, . . . , αm(x) ≤ 0}. Then 0 ∈ C, so C is not empty.
Let D := {∑m
i=1 λiαi | λ1, . . . , λm ≥ 0}. Then D ⊆ (Rd )
⋆ is a ﬁnitely generated
cone, and D⋆ = C. By WEYL’s Theorem (Theorem 1.1.5), D is also a polyhedral
cone, so there are v1, . . . , vn such that D = {β | β(v1) ≤ 0, . . . , β(vn) ≤ 0}. But D
is the polar dual of the ﬁnitely generated cone E := {∑n
i=1 µi vi | µ1, . . . , µn ≥ 0},
i.e. E⋆ = D. Dualizing this again gives E⋆⋆ = D⋆. By Lemma 1.1.10 we have that
E⋆⋆ = E, so C = D⋆ = E. Hence, C is ﬁnitely generated. ⊓⊔

This ﬁnally allows us to prove the WEYL-MINKOWSKI Duality for cones.

Proof (Proof of Theorem 1.1.3). This follows immediately from Theorem 1.1.5
and Theorem 1.1.12. ⊓⊔

1.1.13 Deﬁnition (MINKOWSKI sum). The MINKOWSKI sum of two sets X , Y ⊆ Rd

is the set
 X + Y := {x + y | x ∈ X , y ∈ Y } .

1.1.14 Deﬁnition (lineality space). Let C be a polyhedral cone. The lineality
space of C is
 lineal C := { y | x + λ y ∈ C for all x ∈ C, λ ∈ R} .

C is pointed if lineal C = {0}.

Let C ⊆ Rd , L := lineal C and W a complementary linear subspace to L in Rd . Let
D be the projection of C onto W . Then D is a cone and

C = L + D and lineal D = {0} .

Hence, up to a MINKOWSKI sum with a linear space we can restrict our consider-
ations to pointed polyhedra. We can characterize a pointed cone C also via the
condition that there is α ∈ (Rd )
⋆ such that α(x) < 0 for all x ∈ C − {0}.

Haase, Nill, Paffenholz: Lattice Polytopes — 5 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

1.1.15 Proposition. Let C = {x ∈ Rd | α1(x) ≤ 0, . . . , αm(x) ≤ 0} be a cone. Then

lineal C = { y | αi( y) = 0, 1 ≤ i ≤ m}.

Proof. Let L := { y | αi( y) = 0, for 1 ≤ i ≤ m}. Then L ⊆ lineal C. Suppose
conversely that y ∈ lineal C, but αi( y) ̸= 0 for some index i. Let x ∈ C. Then
0 ≥ α(x +λ y) = α(x)+λα( y) > 0 for sufﬁciently large λ. This is a contradiction,
so αi( y) = 0. ⊓⊔

1.2 Polytopes

In this section we introduce polytopes. We will study their properties by reducing
to the case of cones and using the results from the previous section.

1.2.1 Deﬁnition (polytope). A polytope is the convex hull conv(v1, . . . , vn) of a
ﬁnite number of points in Rd .

A cone is the special case of a polytope where all half spaces are linear. We will use
the results for cones to prove similar characterizations for polytopes. We associate
a cone with a polytope.

1.2.2 Deﬁnition (cone over a polytope). Let P ⊆ Rd be a polytope. The cone
over P is the set
 CP := {1} × P := conv  1
x
  | x ∈ P .

We can recover the polytope P from its cone by intersecting with the hyperplane
H0 := {(x0, x) | x0 = 1} (and projecting). By Theorem 1.1.3, we can write CP as

CP = ˆ x0
x
  |
| (−b|A)  x0
x
  ≤ 0
˙

for some v1, . . . , vn, w1, . . . , wl ∈ Rd (recall that we can scale generators of a cone
with a positive factor). Intersecting with H0 gives

P = {x | Ax ≤ b}

so any polytope can be written as the intersection of a ﬁnite number of afﬁne half
spaces. This intersection deﬁnes a bounded subset of Rd .
Conversely given a bounded intersection P := {x | Ax ≤ b} of a ﬁnite number
of afﬁne half-spaces, we can deﬁne the cone

C := ˆ x0
x
  |
| (−b|A)  x0
x
  ≤ 0
˙

The intersection with H0 recovers the set P. By the MINKOWSKI-WEYL-Theorem
there are ﬁnitely many vectors
‡ v(1)
0
v(1)
 „
 , . . . ,
 ‡ v(k)
0
v(k)
 „

that generate C. By construction we have v(i)
0 ≥ 0 for all i. We claim that the v(i)
0

are even positive. Otherwise, assume that v(1)
0 = 0. Then λ
 ‡ v(1)
0
v(1)
 „
 ∈ C implies

that
 — 6 — Haase, Nill, Paffenholz: Lattice Polytopes

Polytopes, Cones, and Lattices (preliminary version of December 7, 2012)

Av(1)λv ≤ 0

for all λ ≥ 0. Hence, P would be unbounded. So v(i)
0 > 0 for all i. After scaling
each generator with a positive scalar we can assume that v0(i) = 1, so that

C = conv  1
v(1)
  , . . . ,  1
v(k)
 

= { ∑ λi∑ λi v(i)
  | λi ≥ 0} .

Intersecting with H0 gives
 P = conv(v(1), . . . , v(k)) .

This proves the following duality theorem for polytopes.

1.2.3 Theorem (WEYL-MINKOWSKI-Duality). A bounded set P ⊆ Rd is a polytope if
and only if it is the bounded intersection of a ﬁnite number of afﬁne half spaces. ⊓⊔

By this theorem we have two equivalent descriptions of a polytope:

(1) as the convex hull of a ﬁnite set of points in Rd ,
(2) as the bounded intersection of a ﬁnite set of afﬁne half spaces.

The ﬁrst is called the interior or V-description, the second is the exterior or H-
description. Both are important in polytope theory, as some things are easy to
describe in one and may be difﬁcult to deﬁne in the other.
Although the proof of the WEYL-MINKOWSKI duality is constructive, it is not
efﬁcient. We used FOURIER-MOTZKIN elimination to project a polyhedral cone onto
a lower dimensional cone. Examining this method more closely shows that in each
step we may roughly square the number of necessary inequalities. This behaviour
does indeed occur. For an example, we may consider the standard unit cube. Let
e1, . . . , ed ∈ Rd be the standard unit vectors and δ1, . . . , δd ∈ (Rd )
⋆ the dual basis.
Then
 Cd :=
 d⋂

i=1
(H −
−δi ,0 ∩ H −
δi ,1) = conv
   d∑

i=1 λi ei | λi ∈ {0, 1}, 1 ≤ i ≤ d
!
 .

Both descriptions are irredundant, and we have 2d inequalities, but 2d genera-
tors.

Let P = ⋂
i∈I H −
i ⊆ Rd be a polytope given by a hyperplane description. A half
space H −
i for some i ∈ I is an implied equality if P ⊆ Hi. The set of all implied
equalities of P is
 eq(P) := { j ∈ I | P ⊆ H j} .

Observe that this is a property of the speciﬁed hyperplane description, not of the
polytope itself. The afﬁne hull of P is given by the intersection of the implied
equations,
 aff(P) = ⋂

j∈eq(P) H j .

The dimension of P is the dimension of its afﬁne hull,

dim P := dim aff P .

Haase, Nill, Paffenholz: Lattice Polytopes — 7 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

A polytope is full dimensional if dim P = d. The hyperplane description is irredun-
dant if no proper subset of the half spaces deﬁnes the same polytope, and redun-
dant otherwise. Note that an irredundant representation need not be unique. You
could e.g. think of a ray in R2.
Let P := {x | α1(x) ≤ b1, . . . , αm(x) ≤ bm} be a polytope. A point x ∈ P is an
interior point of P if

αi(x) = bi for all i ∈ eq(P) αi(x) < bi for all i ̸∈ eq(P) .

Any polytope has an interior point.

1.2.4 Deﬁnition (valid and supporting hyperplanes). Let X ⊆ Rd and α ∈
(Rd )
⋆ − {0}, δ ∈ R. The hyperplane Hα,δ is a valid hyperplane of X if

X ⊆ H −
α,δ .

Hα,δ is supporting if in addition Hα,δ ∩ X ̸= ∅.

1.2.5 Deﬁnition (faces). Let P be a polytope. A face F of P is either P itself or
the intersection of P with a valid linear hyperplane. If F ̸= P then F is a proper
face.

For any face F we have
 F ∩ P = lin F ∩ P .

1.2.6 Proposition. Let P be a polytope and F a face of P. Then F is a polytope. ⊓⊔

The dimension of a face of a polytope P is its dimension as a polytope,

dim F := dim aff F .

1.2.7 Theorem. Let P := {x | α1(x) ≤ b1, . . . , αm(x) ≤ bm} be a polytope. If F is a
proper face of P, then F = {x | αi(x) = bi for i ∈ I} ∩ P for a subsystem I ⊆ [m] of
the inequalities of P.

Proof. Let F be deﬁned by a hyperplane H := Hα,b, i.e.

F = H ∩ P and P ⊆ H − .

We work with the homogenizations ˆP := homog P and ˆF := homog F of P and F .
Let ˆαi : R × Rd → R, (x0, x) 7→ bi x0 + αi(x) for 1 ≤ i ≤ m and ˆα : R × Rd → R,
(x0, x) 7→ bx0 + α(x). Then

ˆP = {(x0, x) | ˆαi((x0, x)) ≤ 0, 1 ≤ i ≤ m}

and
 ˆF = ˆP ∩ {(x0, x) | ˆα((x0, x)) = 0} , ˆP ⊆ {(x0, x) | ˆα((x0, x)) ≤ 0} .

Hence, it sufﬁces to show that

ˆF = {(x0, x) | ˆαi((x0, x)) = 0 for i ∈ I} ∩ ˆP .

ˆP is a polyhedral cone, so ˆα ∈ (ˆP)
⋆, as ˆα((x0, x)) ≤ 0 for all (x0, x) ∈ ˆP.

— 8 — Haase, Nill, Paffenholz: Lattice Polytopes

Polytopes, Cones, and Lattices (preliminary version of December 7, 2012)

By Corollary 1.1.11 we know that (ˆP)
⋆ is ﬁnitely generated by ˆα1, . . . , ˆαm, so
there are λ1, . . . , λm ≥ 0 such that ˆα = ∑m
i=1 λi ˆαi. Let I := {i ∈ [m] | λi ̸= 0}.
Then ˆα = ∑
i∈I λi ˆαi. Let ˆF ′ := {(x0, x) | ˆαi((x0, x)) = 0 for i ∈ I} ∩ ˆP For any
(c0, c) ∈ ˆF we have
 0 = ˆα((c0, c)) = ∑

i∈I λi ˆαi((c0, c)) ≤ 0 .

λi > 0 for i ∈ I implies that any inequality ˆαi(c0, c)) for i ∈ I must vanish sepa-
rately. Hence, ˆF ⊆ ˆF ′.
Conversely, if ˆαi((x0, x)) = 0 for all i ∈ I, then

ˆα((x0, x)) = ∑

i∈I λi ˆαi((x0, x)) = 0 ,

so ˆF ′ ⊆ ˆF . ⊓⊔

1.2.8 Remark. The argument we have used in the proof is a variation of the com-
plementary slackness theorem of linear programming.

1.2.9 Corollary. Let P be a polytope. Then P has only a ﬁnite number of faces. ⊓⊔

1.2.10 Deﬁnition (facet). Let P ⊆ Rd be a polytope. A proper face F is a facet of
P if it has dimension dim P − 1.

1.2.11 Theorem. Let P := {x | α1(x) ≤ b1, . . . , αm(x) ≤ bm} ⊆ Rd be full dimen-
sional and α1, . . . , αm irredundant.
Then F is a facet of P if and only if F = {x | αi(x) = bi} ∩ C for some 1 ≤ i ≤ m.

Proof. Let x ∈ C be an interior point of C. Then αi(x) < bi for all 1 ≤ i ≤ m, as
P is full dimensional. Let i ∈ [m] and F := {x | αi(x) = bi} ∩ P. By irredundancy,
there is z ∈ Rd such that

αi(z) > bi and α j(z) ≤ b j for all j ̸= i .

Hence, there is y on the segment between x and z such that

αi( y) = bi and α j( y) < b j for all j ̸= i .

So aff(F ) = {x | αi(x) = bi}, and dim F = d − 1, so F is a facet.
If conversely F is a facet, then there is I ⊆ [m] such that F = {x | αi(x) =
bi for all i ∈ I} ∩ P. If |I| ≥ 1, then F is as required. If |I| ≥ 2, then let J be a non-
empty proper subset of I and G = {x | α j(x) = 0 for all j ∈ J}. By irredundancy,
F ⊊ G, so dim F < dim G < dim P, and F would not be a facet. ⊓⊔

1.2.12 Corollary. Let P := {x | α1(x) ≤ b1, . . . , αm(x) ≤ bm} ⊆ Rd be a polytope.

(1) If P is full dimensional, then α1, . . . , αm are unique up to scaling with a positive
factor.
(2) Any proper face of P is contained in a facet.
(3) If F1, F2 are proper faces, then F1 ∩ F2 is a proper face of P. ⊓⊔

1.2.13 Deﬁnition (minimal face). Let P be a polytope. A face F of P is minimal
if there is no non-empty proper face G of P with G ⊊ F .

1.2.14 Proposition. Let P be a polytope and F a face of P.

(1) F is minimal if and only if F = aff F .

Haase, Nill, Paffenholz: Lattice Polytopes — 9 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

(2) F is minimal if and only if it is a translate of lineal P.

Proof. proof missing

1.2.15 Deﬁnition (vertices of a polytope). The minimal faces of a pointed poly-
tope are called vertices. They are points in Rd . The set of all vertices is denoted
by V(P).

1.2.16 Corollary. Let C be a polyhedral cone. Then lineal C is the unique minimal
face of C.

1.2.17 Proposition. Let P = ∩m
i=1H −
i be a polytope and d0 := dim lineal P. If F is a
face of dimension d0 + 1, then there are I, J ⊆ [m], |I| ≤ 2 such that

F = ⋃

i∈I H −
i ∩ ⋃

j∈J H j .

In particular, F has at most two facets, which are minimal faces of P, so

F = e + lineal P

for a segment or ray e ⊆ Rd .

If P is pointed, then F is an edge of P, if e is a segment, and a extremal ray
otherwise. If P is a cone, then F is called a minimal proper face. Two minimal face
of P are adjacent if they are contained in the same face of dimension d0 + 1.

Proof (Proof of Proposition 1.2.17). proof missing

1.2.18 Theorem. Let P = ⋃m
i=1 H −
i and L := lineal P. Let

(1) F1, . . . , Fn be the minimal faces of P, and
(2) G1, . . . , Gl the minimal proper faces of rec P.

Choose

vi ∈ Fi and wi ∈ G j − L for 1 ≤ i ≤ n, 1 ≤ j ≤ l

and a basis b1, . . . , bk of L. Then

P = conv(v1, . . . , vn) + cone(w1, . . . , wl ) + lin(b1, . . . , bk) .

Proof. proof missing

1.2.19 Deﬁnition ( f -vector, face vector). Let P be a polytope. The f -vector (or
face vector) of P is the vector

f(P) := (f−1(P), f0(P), . . . , fd−1(P)) ,

where fi(P) is the number of i-dimensional faces of P, for −1 ≤ i ≤ d − 1.

1.3 Lattices

Now we introduce the central tool for this book. It will link our geometric objects,
the polytopes, to algebraic objects, namely toric ideals and toric varieties.
Throughout this section, V will be a ﬁnite-dimensional real vector space
equipped with the topology induced by a norm ∥ . ∥ and with a translation in-
variant volume form.

— 10 — Haase, Nill, Paffenholz: Lattice Polytopes

Polytopes, Cones, and Lattices (preliminary version of December 7, 2012)

Lattices can be deﬁned in two different (but equivalent) ways: as the integral
generation of a linearly independent set of vectors, or as a discrete abelian sub-
group of the vector space. We will start with the latter characterization of a lattice
as it is often very useful to describe lattices without the explicit choice of a basis.
We will deduce the other representation in the next paragraphs.
A subset Λ ⊆ Rd is an additive subgroup of Rd if for any x, y ∈ Λ

(1) 0 ∈ Λ

(2) x + y ∈ Λ for any x, y ∈ Λ

(3) −x ∈ Λ for any x ∈ Λ .

1.3.1 Deﬁnition (lattice). A lattice Λ in V is a discrete additive subgroup Λ of V :
for all x ∈ Λ there is ϵ > 0 such that Bϵ(x) ∩ Λ = {x}.
The rank of Λ is the dimension of its linear span rank Λ := dim lin Λ.

1.3.2 Example. (1) The standard integer lattice is the lattice spanned by the d
standard unit vectors e1, . . . , ed . It is commonly denoted by Zd . We will later
see that essentially any lattice looks like this integer lattice.
(2) root systems
(3) Subgroups of lattices are lattices. In particular, {x ∈ Z
2 | x1 + x2 ≡ 0 mod 3}
is a lattice.

1.3.3 Lemma. Let B = {b1, . . . , bd } ⊆ V be linearly independent. Then the sub-
group
 Λ(B) :=
 ( d∑

i=1 λi bi | λi ∈ Z, 1 ≤ i ≤ d
)

generated by B is a lattice.

Proof. The linear map Rd → lin B given by λ 7→ ∑d
i=1 λi bi is bijective, and hence
a homeomorphism. It maps the discrete set Zd ⊆ Rd onto Λ(B).
Let z ∈ Rd ∩ Π(b1, . . . , bd ) be an interior point of Π(b1, . . . , bd ). Then there
is ϵ > 0 such that Bϵ(z) ⊆ Π(b1, . . . , bd ). We claim that Bϵ(x) ∩ Λ = {x} for all
x ∈ Λ. Indeed, if y ∈ Bϵ(x) ∩ Λ = {x} and y ̸= x, Then x ′ := x − y ∈ Λ and
x ′ + z ∈ Π(b1, . . . , bd ), a contradiction to Proposition 1.3.10. ⊓⊔

1.3.4 Deﬁnition (lattice basis). A linearly independent subset B ⊆ V is called a
lattice basis (or Λ-basis) if it generates the lattice: Λ = Λ(B).

1.3.5 Example. { 3
0
,  −1
1 
} is a basis of the lattice in Example 1.3.2(3).

1.3.6 Deﬁnition (dual lattice). Let Λ ⊆ V be a lattice with lin Λ = V . Then set

Λ⋆ := {α ∈ V ⋆ | α(a) ∈ Z for all a ∈ Λ}

is the dual lattice to Λ.

1.3.7 Lemma. If b1, . . . , bd is a basis of Λ and α1, . . . , αd is the corresponding dual
basis (i.e. αi(b j) = 1 if i = j, and αi(b j) = 0 otherwise), then Λ⋆ is spanned by
α1, . . . , αd as a lattice. Hence, the dual lattice is indeed a lattice. Further, dualizing
twice gives us back the original lattice, Λ⋆⋆ = Λ, as b1, . . . , bd is a dual basis to
α1, . . . , αd .

1.3.8 Theorem. Every lattice has a basis.

For the proof we need some prerequisites.

Haase, Nill, Paffenholz: Lattice Polytopes — 11 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

Figure missing

Fig. 1.4: A parallelepiped spanned by
some vectors
 1.3.9 Deﬁnition (parallelepiped). For a ﬁnite subset A = {v1, . . . , vk} ⊆ Rd the
half-open zonotope Π(A ) spanned by these vectors is the set

Π(A ) :=
 ( k∑

i=1 λi vi | 0 ≤ λi < 1 for 1 ≤ i ≤ k
)
 .

If A is linearly independent, the zonotope is a parallelepiped.

See Figure 1.4 for an example.

1.3.10 Proposition. Let Λ be a lattice in V with basis B = {b1, . . . , bd } . Then any
point x ∈ lin Λ has a unique representation x = a + y for a ∈ Λ and y ∈ Π(B).

Proof. There are unique λ1, . . . , λd ∈ R such that x = ∑d
i=1 λi bi . Set a :=
∑d
i=1 ⌊λ⌋i bi and y := ∑d
i=1 {λ}i bi. Then y ∈ Π(B), a ∈ Λ, and x = a + y.
Now assume that there is a second decomposition x = a′ + y ′ with a ̸= a′ (and
thus also y ̸= y ′). We can write y and y ′ as

y =
 d∑

i=1 αi bi y ′ =
 d∑

i=1 α
′
i bi

for some 0 ≤ αi, α
′
i < 1, 1 ≤ i ≤ d. Hence, |αi − α
′
i| < 1. From

a′ − a = y − y ′ =
 d∑

i=1 (αi − α
′
i)bi

and a′ − a ∈ Λ we know that αi − α
′
i ∈ Z for 1 ≤ i ≤ d. Hence, αi − α
′
i = 0, so
y = y ′. Hence, also a = a′. ⊓⊔

1.3.11 Corollary. Let Λ be a lattice in Rd with basis B := {b1, . . . , bd } and fun-
damental parallelepiped Π := Π(b1, . . . , bd ). Then Rd is the disjoint union of all
translates of Π by vectors in Λ. ⊓⊔

1.3.12 Lemma. If K ⊆ V is bounded, then K ∩ Λ is ﬁnite.

1.3.13 Deﬁnition (Λ-rational subspace). A subspace U ⊆ V is Λ-rational if it is
generated by elements of Λ.

1.3.14 Proposition. Let V be a ﬁnite-dimensional real vector space, let Λ ⊆ V be a
lattice, and let U ⊆ V be a Λ-rational subspace. Denote the quotient map π: V →
V /U .

(1) Then π(Λ) ⊆ V /U is a lattice.
(2) Furthermore, if Λ ∩ U has a basis b1, . . . , br , and π(Λ) has a basis c1, . . . , cs,
then any choice of preimages ˆci ∈ Λ of the ci for 1 ≤ i ≤ s yields a Λ-basis
b1, . . . , br , ˆc1, . . . , ˆcs.

In the situation of the proposition, we will often write Λ/U for π(Λ).

Proof. (1) As the image of a group under a homomorphism, π(Λ) is a subgroup
of V /U.
The hard part of the proposition is to prove that π(Λ) is discrete in V /U.
Because U is Λ-rational, we can choose a vector space basis {v1, . . . , vr } ⊆ Λ ∩ U
of U. Extend it to a vector space basis B = {v1, . . . , vd } ⊆ Λ of lin Λ. These bases
yield maximum norms

— 12 — Haase, Nill, Paffenholz: Lattice Polytopes

Polytopes, Cones, and Lattices (preliminary version of December 7, 2012)

‖
‖
‖
‖
‖
 d∑

i=1 λi vi
‖
‖
‖
‖
‖ := max{|λi| : i = 1, . . . , d}

on lin Λ and ‖
‖
‖
‖
‖

  d∑

i=1 λi vi
!
 + U
‖
‖
‖
‖
‖

′
 := max{|λi| : i = r + 1, . . . , d}

on lin Λ/U. Denote the unit ball of lin Λ by W . By Lemma 1.3.12, the set W ∩ Λ
is ﬁnite. Set ϵ := min  
{1} ∪ {∥v + U∥′ : v ∈ W ∩ Λ \ U} .

This minimum over a ﬁnite set of positive numbers is positive. Now suppose v =
∑d
i=1 λi vi ∈ Λ with ∥v + U∥′ < ϵ. Then v′ := ∑r
i=1(λi − ⌊λi⌋)vi + ∑d
i=r+1 λi vi ∈ Λ
represents the same coset: v + U = v′ + U, and v′ ∈ W ∩ Λ. We conclude v′ ∈ U
and thus v′ + U = 0 ∈ V /U.
(2) Let b1, . . . , br , ˆc1, . . . , ˆcs be as in the proposition, and let v ∈ Λ. Because
the c j form a lattice basis of π(Λ), there are integers λ1, . . . , λs so that π(v) =
∑s
j=1 λ j c j. Thus, v − ∑s
j=1 λ jˆc j ∈ ker π = U. Because the bi form a lattice basis

of Λ ∩ U, there are integers µ1, . . . , µr so that v − ∑s
j=1 λ jˆc j = ∑r
i=1 µi bi. So
b1, . . . , br , ˆc1, . . . , ˆcs generate Λ. They must be linearly independent for dimension
reasons. ⊓⊔

1.3.15 Deﬁnition (primitive vector). A non-zero lattice vector v ∈ Λ is primitive
if it is not a positive multiple of another lattice vector: conv(0, v) ∩ Λ = {0, v}.

Proof (Theorem 1.3.8). We proceed by induction on r := rank Λ. For r = 0, the
empty set is a basis for Λ. For r = 1, a primitive vector yields a basis.
Assume r ≥ 2. Let b ∈ Λ be primitive, and set U := lin b. Then {b} is a
basis for U ∩ Λ, and Λ/U is a lattice by the ﬁrst statement of Proposition 1.3.14.
Because rank Λ/U = r − 1, it has a basis by induction. By the second statement of
Proposition 1.3.14, we can lift to a basis of Λ.

Proof. We have to show that there are b1, . . . , bd ∈ Rd that span Λ as a lattice.
Clearly, as Λ spans Rd , we can ﬁnd d linearly independent vectors w1, . . . , wd
in Λ. We construct a basis of Λ from these vectors. Let V0 := {0} and

Vk := lin(w1, . . . , wk) .

We use induction over k to construct a basis of the lattice Λ ∩ Vk. For k = 1
let v1 ∈ (Λ − {0}) ∩ V1 be such that ∥v1∥ is minimal. Such a point exists by
Lemma 1.3.16.Any other lattice point a ∈ (Λ − {0}) ∩ V1 can then be written
as
 a = λv1

for some λ ∈ R. If λ ̸∈ Z, then 0 < {λ} < 1 and

{λ} v1 = a − ⌊λ⌋ v1 ∈ (Λ − {0}) ∩ V1 .

but ∥ {λ} v1∥ = | {λ} |∥v1∥ < ∥v1∥ contradicting our choice of v1. Hence λ ∈ Z and
v1 is a basis of Λ ∩ V1.
Now let k ≥ 2. We already have a basis v1, . . . , vk−1 of the lattice Λ ∩ Vk−1. Let
vk ∈ (Λ ∩ Vk) − Vk−1 be with minimal distance to Vk−1 (by Lemma 1.3.16). Then
vk can be written as

Haase, Nill, Paffenholz: Lattice Polytopes — 13 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

vk =
 k∑

i=1 λi vi

for some λi ∈ R. Let v ∈ Λ ∩ Vk be some other lattice point. This also has a
representation
 vk =
 k∑

i=1 µi vi .

for µi ∈ R. If α := µk/λk is not an integer, then 0 < 
µ	 < 1 and

v′
k := v − ⌊α⌋ vk = v − αvk + {α} vk = {α} λkwk +
 k−1∑

i=1 (µi − ⌊α⌋i)wi

is a lattice point in (Λ∩ Vk)− Vk−1. However, for any point x = ∑k
i=1 ηi wi we have

d(x, Vk−1) = |ηk| d(wk, Vk−1) ,

so v′
k is closer to Vk−1 than vk. A contradiction, so α is integral, and v1, . . . , vk
spans the lattice Λ ∩ Vk. ⊓⊔

Recall the distance function in Rd ,

d(x, y) := ∥x − y∥

and d(x, S) := inf
z∈S(d(x, z))

for any x, y ∈ Rd , S ⊆ Rd .

1.3.16 Lemma. Let Λ ⊆ Rd be a lattice and v1, . . . , vk ∈ Λ, k < d, linearly indepen-
dent. Deﬁne V := lin(v1, . . . , vk).
Then there is v ∈ Λ − V and x ∈ V such that

d(v, x) ≤ d(w, y) for any y ∈ V, w ∈ Λ − V .

Proof. Let Π := Π(v1, . . . , vk). Then Π is a compact subset of Rd . Choose any
a ∈ Λ − V and set r := d(a, Π). Let

Br (Π) := {x | d(x, Π) ≤ r} .

Then a ∈ (Br (Π) − V ) ∩ Λ, and Br (Π) is bounded, so br (Π) ∩ Λ is ﬁniteby Prob-
lem 1.2. Hence, we can choose some v ∈ (Br (Π) − V ) ∩ Λ that minimizes d(v, Π).
Choose some x ∈ Π such that d(v, x) attains this minimal distance. We will show
that these choices satisfy the requirements of the proposition.
Let w ∈ Λ−V and y ∈ V . By deﬁnition of V there are coefﬁcients λ1, . . . , λk ∈ R
such that

y =
 k∑

i=1 λi vi . Set z :=
 k∑

i=1 ⌊λ⌋i vi , z′ :=
 k∑

i=1 {λ}i vi ,

Then z, w − z ∈ Λ and z′ = y − z ∈ Π. Further, w − z ̸∈ V . Hence,

d( y, w) = d( y − z, w − z)

≥ d(w − z, Π) ≥ d(v, Π, =) d(v, x) . ⊓⊔

— 14 — Haase, Nill, Paffenholz: Lattice Polytopes

Polytopes, Cones, and Lattices (preliminary version of December 7, 2012)

1.3.17 Deﬁnition (unimodular transformation). Let Λ and Λ′ be lattices. A lin-
ear map T: lin Λ → lin Λ′ which induces a bijection Λ → Λ′ is called unimodular
or a lattice transformation.

1.3.18 Lemma. Let B and B
′ be bases of the lattices Λ and Λ′ respectively. Then a
linear map T: lin Λ → lin Λ′ is unimodular if and only if the matrix representation
A of T with respect to the bases B and B′ is integral and satisﬁes | det A| = 1.

Proof. The matrix A has only integral entries if and only if T(Λ) ⊆ Λ′.
Similarly, if T is unimodular, then the inverse transformation exists, and its
matrix A
−1 also has integral entries. Thus, det A and det A
−1 are integers with
product 1.
Conversely, if A is integral with | det A| = 1, then, by CRAMER’s rule A
−1 exists
and is integral. ⊓⊔

1.3.19 Lemma. Let A ∈ Zd×d be non-singular. Then Aλ = µ has an integral solution
λ for any integral µ ∈ Zd if and only if | det A| = 1.

Proof. “⇒”: By CRAMER’s rule, the entries of λ are λi = ± det(Ai), where Ai is the
matrix obtained from A by replacing the i-th column with µ.
“⇐”: If | det A| > 1, then 0 < | det A
−1| < 1, so A
−1 contains a non-integer entry
ai j. If e j ∈ Zm is the j-th unit vector, then Aλ = e j has no integer solution. ⊓⊔

1.3.20 Corollary. An integral matrix A ∈ Zd×d is the matrix representation of a
unimodular transformation of a lattice if and only if | det A| = 1. ⊓⊔

1.3.21 Corollary. Let Λ be a lattice with basis b1, . . . , bd lin Λ. Then c1, . . . , cd ∈ Λ
is another basis of Λ if and only if there is a unimodular transformation T :∈ Λ →
lin Λ such that T(bi) = ci for 1 ≤ i ≤ d. ⊓⊔

We are now ready to deﬁne an important invariant of a lattice.

1.3.22 Deﬁnition (Determinant of a lattice). Let Λ′ ⊆ Λ be lattices with lin Λ =
lin Λ′, and let B and B
′ be bases of Λ and Λ′ respectively. Let A be the matrix
representation of the identity lin Λ′ → lin Λ with respect to the bases B
′ and B.
Then the determinant of Λ′ in Λ is the integer

det
Λ Λ′ := | det A| .

If Λ = Zd , we will often write det Λ′ for det Zd Λ′.

By Lemma 1.3.18 and Corollary 1.3.21 this deﬁnition is independent of the cho-
sen bases.

1.3.23 Deﬁnition (sublattice and index). Let Λ ⊆ Rd be a lattice. Any lattice
Γ ⊆ Λ is a sublattice of Λ.
Sets of the form a + Γ := {a + x | x ∈ Γ } for some a ∈ Λ are cosets of Γ in Λ.
The set of all cosets is Λ/Γ . The size |Γ /Λ| is the index of Γ in Λ.

Next we study a way to obtain a “nice” basis for a lattice generated by a set of
(not necessarily linearly independent) vectors in Zd .

1.3.24 Deﬁnition (HERMITE normal form). Let A = (ai j) ∈ Zm×d with m ≥ d. A
is in HERMITE normal form if

◃ ai j = 0 for j < i and
◃ aii > ai j ≥ 0 for i > j .

Haase, Nill, Paffenholz: Lattice Polytopes — 15 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

So a matrix in HERMITE normal form is an upper triangular matrix, and the largest
entry in each column is on the diagonal. We remark that, depending on the con-
text, sometimes we use the transposed matrix, i.e. we claim that a matrix is in
HERMITE normal form if it has at least as many columns as rows, it is lower trian-
gular, and the largest entry in each row is on the diagonal (and if the matrix is
square we can also consider upper triangular matrices).

1.3.25 Theorem (HERMITE normal form). Let A ∈ Zm×d . Then there is U ∈ Zd×d

such that AU is in HERMITE normal form.

Proof. proof missing

1.3.26 Theorem. Let Λ′ ⊆ Λ be lattices with lin Λ = lin Λ′. Then there is a basis
b1, . . . , br of Λ and integers k1, . . . , kr ∈ Z> with λi|λi+1 for 1 ≤ i ≤ d − 1
such that k1 b1, . . . , kr br is a basis of Λ′.

Proof. We proceed by induction on r := rank Λ = rank Λ′. For r = 1, a Λ-primitive
vector has a positive integral multiple which is Λ′-primitive.
Assume r ≥ 2. Because lin Λ = lin Λ′, for every v ∈ Λ there is a positive integer
k so that kv ∈ Λ′. Choose br ∈ Λ and kr ∈ Z> so that br is Λ-primitive, and so
that kr is minimal.
Set U := lin br . Then br is a basis for U ∩ Λ, and kr br is a basis for U ∩ Λ′.
By Proposition 1.3.14, Λ′/U ⊆ Λ/U are lattices of rank r − 1. By induction, there
is a basis b1, . . . , br−1 of Λ/U together with positive integers k1, . . . , kr−1 so that
k1 b1, . . . , kr−1 br−1 is a basis for Λ′/U.
Let ˆbi ∈ Λ be representatives of the bi for i = 1, . . . , r − 1. Then there are
representatives ci ∈ Λ′ of the ki bi. By Proposition 1.3.14, b1, . . . , br is a basis
for Λ, and c1, . . . , cr−1, kr br is a basis for Λ′. By adding a suitable multiple of
kr br ∈ Λ′ to the ci, we may assume that ci = kiˆbi + li br for 0 ≤ li < kr and for all
i = 1, . . . , r − 1.
But then, ci is a positive integral multiple of some Λ-primitive vector: ci = mi ai.
The two expressions for ci together imply li = 0 or mi ≤ li < kr in contradiction
to the minimality of kr .
Altogether, we obtain li = 0 for all i, and hence, ci = kiˆbi as required. ⊓⊔

1.3.27 Corollary. Let Λ′ ⊆ Λ be lattices with lin Λ = lin Λ′, and let B
′ be a basis of
Λ′. Then
 |Λ/Λ′| = |Π(B
′) ∩ Λ| = det
Λ Λ′ .

Proof. The quotient map π: Λ → Λ/Λ
′ induces a bijection Π(B
′) ∩ Λ → Λ/Λ
′

by Proposition 1.3.10. So the ﬁrst two quantities are equal, and in particular the
second one is independent of the chosen Λ′-basis.
That means, for the proof that the last two quantities agree, we can choose
bases as in Theorem 1.3.26. Then the change of bases matrix is diagonal with
determinant k1 · . . . · kr , while the set Π(B′) ∩ Λ consists of the points ∑
i li bi for
0 ≤ li ≤ ki − 1. ⊓⊔

In dimensions d ≥ 2 there are inﬁnitely many unimodular matrices. Hence,
there are also inﬁnitely many different bases of a lattice. In Section 3.5.2 we deal
with the problem of ﬁnding bases of a lattice with some nice properties. We will
e.g. construct bases with “short” vectors.
Let v1, . . . , vn ∈ Λ. Then C := cone(v1, . . . , vn) is a polyhedral cone. Let SC :=
C ∩ Λ Then SC with addition is a semi-group, the semi-group of lattice points in C.

— 16 — Haase, Nill, Paffenholz: Lattice Polytopes

Polytopes, Cones, and Lattices (preliminary version of December 7, 2012)

Indeed, 0 ∈ SC and if x, y ∈ SC , then x + y ∈ SC . A set H ⊆ SC generates SC as a
semigroup if for any x ∈ SC there are λh ∈ Z≥ for h ∈ H such that

x = ∑

h∈H λhh .

Such a set is a HILBERT basis of SC . A HILBERT basis is minimal if any other HILBERT
basis of SC contains this basis.
Observe that in general an inclusion-minimal HILBERT basis is not unique.
Consider e.g. the cone C = R2. Then both H1 := {e1, e2, −(e+e2)} and H2 :=
{±e1, ±e2} are minimal HILBERT bases, but they differ even in size.
A vector a ∈ Zd is primitive if gcd(a1, . . . , ad ) = 1.

1.3.28 Theorem. Let v1, . . . , vn ∈ Λ, C := cone(v1, . . . , vn), and S := C ∩ Zd the
semi-group of lattice points in C. Then SC has a HILBERT basis.
If C is pointed, then SC has a unique minimal HILBERT basis.

Proof. Deﬁne the parallelepiped

Π :=
 ( k∑

i=1 λi yi | 0 ≤ λi ≤ 1, 1 ≤ i ≤ k
)
 .

Let H := Π ∩ Λ. We will prove that H is a HILBERT basis.
(1) H generates C, as y1, . . . , yk ∈ H.
(2) Let x ∈ C ∩ Λ be any lattice vector in C. Then there are η1, . . . , ηk ≥ 0 such
that x = ∑k
i=1 ηi yi. We can rewrite this as

x =
 k∑

i=1
  
⌊ηi⌋ + {ηi} yi ,

so that
 x −
 k∑

i=1 ⌊ηi⌋ yi =
 k∑

i=1 {ηi} yi .

The left side of this equation is a lattice point. Hence, also the right side is a
lattice point. But
 h :=
 k∑

i=1 {ηi} yi ∈ Π ,

so h ∈ Π ∩ Zn = H. This implies that x is a integral conic combination of
points in H. So H is a HILBERT basis.
Now assume that C is pointed. Then there is b ∈ Rn such that

bt x > 0 for all x ∈ C − {0} .

Let K := ¦ y ∈ C ∩ Zm | y ̸= 0, y not a sum of
two other integral vectors in C© .

Then K ⊆ H, so K is ﬁnite.
Assume that K is not a HILBERT basis. Then there is x ∈ C such that x ̸∈ Z≥K.
Choose x such that bt x is as small as possible.
Since x ̸∈ K, there must be are x1, x2 ∈ C such that x = x1 + x2. But

Haase, Nill, Paffenholz: Lattice Polytopes — 17 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

bt x1 ≥ 0 , bt x2 ≥ 0, bt x ≥ 0 and bt x = bt x1 + bt x2 ,

so bt x1 ≤ bt x , bt x2 < bt x .

By our choice of x we get x1, x2 ∈ Z≥K, so that x ∈ Z≥K, a contradiction. ⊓⊔

1.3.29 Deﬁnition (homogeneous). Let Λ ⊆ Rd be a lattice and C ⊆ Rd a ﬁnitely
generated cone with generators v1, . . . , vd ∈ Λ. C is homogeneous with respect to
some linear functional c ∈ Zd if there is λ ∈ Z such that c t vj = λ for 1 ≤ j ≤ d.

Problems

1.1 Prove Caratheodory’s Theorem.

1.2 Let Λ be a discrete subset of Rd and B ⊆ Rd bounded. Then Λ ∩ B is a ﬁnite
set.

1.3 Let Λ ⊆ Rd be a lattice and v1, . . . , vd ∈ Λ be such that vol Π(v1, . . . , vd ) =
det Λ. Then v1, . . . , vd is a basis of Λ.

1.4 Dualizing non-polyhedral cones.

1.5 Existence of a Hilbert basis

1.6 Hermite normal form

— 18 — Haase, Nill, Paffenholz: Lattice Polytopes

2
An invitation to lattice polytopes

Lattice polytopes are ubiquitous throughout mathematics — pure and applied.
An apparent reason is their simple deﬁnition: polytopes whose vertices lie in a
given lattice, such as Zd . There are two major ingredients here. On the one hand,
polytopes: beautiful and ancient objects studied in convex and discrete geometry
and geometric combinatorics. On the other hand, lattices: they have an algebraic
structure and give rise to questions in Diophantine geometry. As such, lattice poly-
topes are objects of the classical theory of the geometry of numbers: the relation
between geometric data of a convex body (such as its shape or volume) with data
coming from their lattice points (such as their number or distribution). So, why is
there such an ongoing interest in these objects? This can be explained by two de-
velopments. First, the rise of the computer pushed the successful development of
linear and combinatorial optimization with all its pervasive modern applications,
while integer optimization is largely concerned with questions on lattice points
in polytopes. Second, toric geometry allowed an unforeseen interaction between
geometric combinatorics and algebraic geometry leading to applications in enu-
merative geometry, mirror symmetry, and polytope theory, to name but a few.
There are several results on lattice polytopes for which the only known proofs
involve the theory of algebraic varieties.
While lattice polytopes are used in many areas of mathematics, there is not
yet one source of reference focusing solely on these objects. Many results are
scattered throughout the literature. Most existing books are either motivated by
its relations to toric varieties or ignore some of the more recent developments in
Ehrhart theory and the geometry of numbers. In these lecture notes we present
the theory of lattice polytopes in a self-contained and unifying way. The goal is
to get students and researchers acquainted with the most important and widely
used results, closely related to topics of recent research. Some presentations and
results are new.
 19

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

Fig. 2.1: Lattice Triangles
 In this chapter we introduce the major deﬁnitions and prove the basic results.
To name a few examples: We will learn about unimodular equivalence, PICK’s
Theorem, and the normalized volume. After having read this chapter, the reader
will have encountered methods and types of results studied in more detail later:
among them are triangulations, lattice point counting, estimating volumes, and
several classiﬁcation results.

2.1 Lattice polytopes and unimodular equivalence

Here is the key player of these lectures:

2.1.1 Deﬁnition. A lattice polytope is a polytope in Rd with vertices in a given
lattice Λ ⊆ Rd .

Note that dim(P) ≤ rank(Λ). Usually we will consider full-dimensional lattice
polytopes, i.e., dim(P) = rank(Λ). However, we note that we can always consider
P as a full-dimensional lattice polytope with respect to its ambient lattice aff(P)∩Λ
of rank dim(P) in its ambient afﬁne space aff(P).
Throughout (except when explicitly noted otherwise), the reader should assume
Λ = Zd . In this case, a lattice polytope is also called integral polytope. We will
use more general lattices only at very few places in the chapter on Geometry of
Numbers (Chapter 4).
Having introduced the objects of our interest, we should next state when two
of them are considered isomorphic. Figure 2.1 shows three examples of lattice
polygons in dimension two. As the reader should notice, all three triangles look
quite different: their vertices have different Euclidean distances and different an-
gles. Still, the top one is considerably distinguished from the lower two: it has
four lattice points, while the others have only three. Actually, more is true: the
second and third are isomorphic.

2.1.2 Deﬁnition. Two lattice polytopes P ⊆ Rd and P ′ ⊆ Rd ′ (with respect to
lattices Λ ⊆ Rd and Λ′ ⊆ Rd ′ ) are isomorphic or unimodularly equivalent, if there
is an afﬁne lattice isomorphism of the ambient lattices Λ ∩ aff(P) → Λ′ ∩ aff(P ′)
mapping the vertices of P onto the vertices of P ′.

Recall that a lattice isomorphism is just an isomorphism of abelian groups.
Moreover, an afﬁne lattice isomorphism is an isomorphism of afﬁne lattices. Here,
note that an afﬁne lattice does not need to have an origin (e.g., consider the set
of lattice points in a hyperplane). However, if we ﬁx some lattice point to be the
origin, an afﬁne lattice isomorphism can be deﬁned as a lattice isomorphism fol-
lowed by a translation, i.e., x 7→ T x + b where T : Λ → Λ′ is a (linear) lattice
isomorphism and b ∈ Λ′.

Luckily, in our usual situation Λ = Zd = Λ′ there is an easy criterion to check
when a linear map Rd → Rd is a lattice automorphism of Zd (see Exercise 2.2).

2.1.3 Lemma. A linear map L : Rd → Rd induces a lattice automorphism of Zd

if and only if its (d × d)-matrix has entries in Z and its determinant is equal to
±1. ⊓⊔

The set of such matrices is denoted by Gl(d, Z). Again, as we have seen from the
example above, it is very important to realize that in our category isomorphisms
do not preserve angles or distances! Let us note an immediate consequence of
Lemma 2.1.3.

2.1.4 Corollary. Unimodularly equivalent lattice polytopes have the same number
of lattice points and the same volume. ⊓⊔

— 20 — Haase, Nill, Paffenholz: Lattice Polytopes

An invitation to lattice polytopes (preliminary version of December 7, 2012)

Let us again consider the example above. The matrix

A = 1 2
1 3



is an element of Gl(d, Z). The afﬁne lattice isomorphism

Z
2 → Z
2 : x 7→ Ax − 1
3



maps the vertices of the ﬁrst triangle T1 to the vertices of the second triangle T2.
This proves that they are unimodularly equivalent.
This is an instance of a remarkable result (referred to as PICK’s Theorem). For
this let us denote by ∆2 := conv(0, e1, e2)

the standard or unimodular triangle.

2.1.5 Proposition (PICK’s Theorem). Any two lattice triangles with three lattice
points are isomorphic to ∆2. In particular, they have area 1/2.

Its proof is sketched in Exercise 2.5. Theorem 2.2.1 below generalizes this re-
sult to arbitrary lattice polygons. Unfortunately, the corresponding statement of
Proposition 2.1.5 in dimension 3 fails(see Exercise 2.4).

2.2 Lattice polygons

To get started, let us prove two famous results on lattice polygons. The ﬁrst is a
surprisingly elegant formula for the computation of the area of a lattice polygon
just by counting lattice points! To ﬁnd some generalization to higher dimensions
(if any) is the topic of the chapter on Ehrhart theory (Chapter 3).

2.2.1 Theorem (PICK’s Formula). Let P be a lattice polygon with i interior lattice
points, b lattice points on the boundary, and (Euclidean) volume a. Then

a = i + b

2 − 1 .

Proof. We prove the theorem by induction on the number l := b + i of lattice
points of P.
Any triangle in R2 with b = 3 and i = 0 is unimodularly equivalent to ∆2
by Proposition 2.1.5, and has area 1/2. So the claimed formula is true in this
case. There are two cases to consider for the induction, either P has b ≥ 4 lattice
points on the boundary, or b = 3 and we have at least one interior lattice point,
i.e. i ≥ 1.
If P has at least four lattice points on the boundary then we can cut P into
two lattice polygons Q1 and Q2 by cutting along a chord e through the interior
of P given by two boundary lattice points. Let Q j, j = 1, 2 have volume a j, b j
boundary lattice points, and i j interior lattice points. Let e have ie interior lattice
points (and two boundary lattice points). Both Q1 and Q2 have less lattice points,
so by induction PICK’s Formula holds for Q and Q′, i.e.

a1 = i1 + b1
2 − 1 , a2 = i2 + b2
2 − 1 .

Further

Haase, Nill, Paffenholz: Lattice Polytopes — 21 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

Fig. 2.2: Splitting P into pieces.
The ﬁrst image is for the case b ≥
4, the second for i ≥ 1.

Fig. 2.3: P in a box
 i = i1 + i2 + ie , b = b1 + b2 − 2ie − 2 ,

so
 a = a1 + a2 = i1 + i2 + 1

2 (b1 + b2) − 2

= i − ie + 1

2 (b + 2ie + 2) − 2 = i + b

2 − 1 .

If b = 3 and i ≥ 1 then we can split P into three pieces Q1, Q2, and Q3 by
coning over some interior point of P. See Figure 2.2. Again, all three pieces have
fewer lattice points than P, so we know PICK’s Formula for those by our induction
hypothesis. A similar computation to the one above shows that PICK’s Formula
also holds for P. ⊓⊔

Note that the proof shows along the way that any lattice polygon can be subdi-
vided into unimodular triangles. This is not true in higher dimensions. See Exer-
cise 2.4. Questions about the existence of such triangulations will be discussed in
the last chapter of this book.
The second fundamental result shows that we can predict precisely how large
the lattice polygon can be at most if we know that a lattice polygon has a certain
(non-zero) number of interior lattice points! Problems like these, which relate in-
formation about lattice points of a convex body to its geometric shape or invari-
ants are subject of the ﬁeld of Geometry of Numbers. We deal with such questions
in Chapter 4.

2.2.2 Theorem (SCOTT, 1976 [24]). Let P ⊆ R2 be a lattice polygon with i ≥ 1
interior lattice points. Then either P = 3∆2 and, hence, vol P = 9/2 and i = 1, or
vol P ≤ 2(i + 1).

Proof. Let a := vol P be the Euclidean area of P. Using PICK’s Theorem 2.2.1 we
can reformulate the condition to
 b ≤ a + 4

unless P = 3∆2, in which case b = 9 and a = 9/2.
Using unimodular transformations we can assume that the polygon P is con-
tained in a rectangle with vertices (0, 0), (p′, 0), (0, p) and (p′, p) such that p is
minimal with this property. As P has at least one interior lattice point we know
that 2 ≤ p ≤ p′. The polygon P intersects the bottom and top edge of the rectan-
gle in edges of length qb and qt . See Figure 2.3. Then

b ≤ qb + qt + 2p (2.2.1)

a ≥ p(qb + qt )

2 . (2.2.2)

Further, PICK’s Theorem 2.2.1 implies that a ≥ b/2. We consider four different
cases for the parameters p, qb and qt :

(1) p = qb + qt = 3, or
(2) p = 2 or qb + qt ≥ 4, or
(3) p = 3 and qb + qt ≤ 2, or
(4) p ≥ 4 and qb + qt ≤ 2

In the ﬁrst case, (2.2.1) gives b ≤ 9. If b ≤ 8, then a ≥ b/2 implies b ≤ a + 4. So
assume that b = 9. If a ≥ 5, then again b ≤ a + 4, so also assume a = 9/2. This

— 22 — Haase, Nill, Paffenholz: Lattice Polytopes

An invitation to lattice polytopes (preliminary version of December 7, 2012)

Fig. 2.4: Case (4). y and y ′ in the right image correspond to wr and wl in the text, x and
x ′ to vt an vb.

implies i = 1. Up to unimodular equivalence there are only ﬁnitely many lattice
polygons with qb + qt = 3, p = 3, and a = 9/2, and of these, only 3∆2 has nine
lattice points on the boundary.

For the second case we subtract (2.2.2) from (2.2.1) to obtain

2b − 2a = 2(qb + qt + 2p) − p(qb + qt ) = (qb + qt − 4)(2 − p) + 8 ≤ 8 ,

where the last inequality follows from p = 2. Rearranging this gives the claim.

In the third case we have b ≤ 8, so the claim follows from a ≥ b/2.

The last case requires slightly more work. Pick points vb := ( yl , 0) and vt :=
( yr , p) in such a way that δ := | yb − yt | is minimal. See Figure 2.4. Using a
unimodular transformation of the type   1 k
0 1  we can assume that

δ ≤ p − qb − qt
2 .

The transformed polygon still satisﬁes p ≤ p′ by the choice of p, so

p′ − δ ≥ p − p − qb − qt
2 ≥ p + qb + qt
2 .

Choose point wl and wr on the left and right edge of the rectangle. We consider
the triangles given by wl , vt , vb and wr , vt , vb. By shifting one vertex we can make
the edge vt , vb vertical in each triangle (see Figure 2.4). The area of the two
triangles is at most the area of our original polygon. Hence, we can estimate

a ≥ 1

2 · p · p + qb + qt
2 .

This implies
 4(b − a) ≤ 4(qb + qt + 2p) − (p + qb + qt )

≤ p(8 − p) − (p − 4)(qb + qt ) ≤ p(8 − p) ≤ 16 .

Solving for b gives the claim. This ﬁnally proves Scott’s Theorem. ⊓⊔

Note that there is no such upper bound on the volume of polytopes not all of
whose whose vertices are lattice points. An example is in Figure 2.5.
 Fig. 2.5: An arbitrarily big rational tri-
angle with one interior lattice point

Haase, Nill, Paffenholz: Lattice Polytopes — 23 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

2.3 Volume of lattice polytopes

This section is devoted to a fundamental result on lattice polytopes in arbitrary
dimension d. In the previous section we have shown that for polygons the num-
ber of interior lattice points and the volume are connected. Here we will prove
that in any dimension d there are only ﬁnitely many isomorphism classes of d-
dimensional lattice polytopes of ﬁxed volume. For polygons, this implies that there
are only ﬁnitely many isomorphism types with a ﬁxed number of interior lattice
points. Unfortunately, no such result is true in dimensions three and above. You
will construct examples in Exercise 2.4. It is an extremely important point to
realize that starting already in dimension three, having information about the
volume of a lattice polytope is much stronger than just knowing the number of
its (interior) lattice points.

2.3.1 Remark. Note that we always take the volume as induced by the lattice Λ,
i.e., the volume of a fundamental parallelepiped equals one. For instance, [0, 1]d

is a fundamental parallelepiped for Zd .

2.3.2 Deﬁnition. ∆d := conv(0, e1, . . . , ed ) is called the standard or unimodular
d-simplex. We also call any polytope isomorphic to ∆d a unimodular d-simplex.

In other words, a lattice polytope is a unimodular simplex if and only if its vertices
form an afﬁne lattice basis. This is the simplest possible lattice polytope. Note
that vol(∆d ) = 1/d!, see Exercise 2.6. The following observation shows that this
simplex is indeed the smallest possible lattice polytope:

2.3.3 Proposition. Let P ⊆ Rd be a d-dimensional simplex. Then there is an afﬁne
lattice homomorphism ϕ : Zd → Zd , x 7→ Ax + b mapping the vertices of ∆d onto
the vertices of P. In this case,

d! vol(P) = | det(ϕ)| ∈ N≥1.

Proof. We may assume that P = conv(0, v1, . . . , vd ). In this case, ϕ is given by
ei 7→ vi for i = 1, . . . , d. Hence,

vol(P) = | det(ϕ)| vol(∆d ) = |
|
|det ••v1 · · · vd −−|
|
| 1

d! . ⊓⊔

2.3.4 Corollary. Let P ⊆ Rd be a d-dimensional lattice polytope. Then d! vol(P) ∈
N≥1. We have d! vol(P) if and only if P is a unimodular simplex.

Proof. We triangulate the polytope into simplices without introducing additional
vertices apart from those of P. In particular, any simplex is a d-dimensional lattice
simplex. Now, the statement follows from the previous proposition. ⊓⊔

This motivates the following deﬁnition.

2.3.5 Deﬁnition. The normalized volume of a d-dimensional lattice polytope P ⊆
Rd is deﬁned as the positive integer

Vol(P) := d! vol(P).

2.3.6 Remark. Note that it makes sense to extend the previous deﬁnition also to
low-dimensional lattice polytopes by considering them as full-dimensional poly-
topes with respect to their ambient lattice. Hence, Vol(P) ≥ 1 for any lattice
polytope.
 — 24 — Haase, Nill, Paffenholz: Lattice Polytopes

An invitation to lattice polytopes (preliminary version of December 7, 2012)

Note that, if P = conv(0, v1, . . . , vd ) is a d-dimensional lattice simplex in Rd , then
by Proposition 2.3.3 the normalized volume of P equals the volume of the paral-
lelepiped spanned by v1, . . . , vd .
As we have seen, lattice polytopes have normalized volume at least 1. Given a
triangulation of a lattice polytope P of normalized volume V into lattice simplices,
we see that this triangulation can have at most V simplices. This observation gives
us an empirical reason why there should be only ﬁnitely many lattice polytopes
of given volume and dimension (of course, up to unimodular transformations).
Finally, let us give the formally correct proof.

2.3.7 Theorem. Let P ⊆ Rd be a d-dimensional lattice polytope, Vol(P) = V . Then
there exists some lattice polytope Q ⊆ Rd such that Q ⊆ [0, d · V ]d and P ∼= Q.
Moreover, if P is a simplex, then d · V may be substituted by V .

2.3.8 Corollary. There exist only ﬁnitely many isomorphism classes of lattice poly-
topes of given dimension and volume.

We will ﬁrst prove Theorem 2.3.7 for simplices. We need the following useful
observation to extend this result to arbitrary polytopes.

2.3.9 Lemma. Let P ⊆ Rd be a d-dimensional polytope. Then there exists a d-
dimensional simplex S ⊆ P whose vertices are vertices of P such that

S ⊆ P ⊆ (−d)(S − x) + x,

where x is the centroid of S. In other words, if v0, . . . , vd are the vertices of S, then

S ⊆ (−d)S +
 d∑

i=0 vi.

The proof is given in Exercise 2.7.

Proof (of Theorem 2.3.7). First, let P = conv(v0, . . . , vd ) be a simplex (assume
v0 = 0). By the HERMITE normal form theorem 1.3.25 there exists U ∈ Gld (Z)
such that
 U ·
 





 ... ... ...
v1 v2 · · · vd
... ... ...
 




 =
 









 a11 0 · · · · · · 0
a21 ≤ a22 0 · · · 0
... ... ... ...
... ... ... 0
ad1 ≤ ad2 · · · · · · add
 










We denote the columns of the right matrix by u1, . . . , ud . Therefore, U deﬁnes a
unimodular transformation mapping P to

Q := conv(0, u1, . . . , ud ) ⊆ [0, a11 · · · add ]d .

Hereby, Vol(P) = Vol(Q) = det(u1, . . . , ud ) = a11 · · · add .
In general, there exists a lattice d-simplex S ⊆ P as in Lemma 2.3.9. Then the
previous part of the proof shows that there exists a unimodular transformation
ϕ : Zd → Zd such that ϕ(S) ⊆ [0, Vol(S)]d .

Let S have vertices v0, . . . , vd . Then

P ∼= ϕ(P) ⊆ (−d)ϕ(S) +
 d∑

i=0 ϕ(vi) ⊆ [0, −d Vol(S)]d +
 d∑

i=0 ϕ(vi).

Haase, Nill, Paffenholz: Lattice Polytopes — 25 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

Since Vol(S) ≤ Vol(P), the statement follows after an afﬁne unimodular transfor-
mation (translating by − ∑d
i=0 ϕ(vi) and multiplying by −1). ⊓⊔

2.4 Problems

2.1 Extend Deﬁnition 2.1.2 to homomorphisms of lattice polytopes in order to
ﬁnish the deﬁnition of a category of lattice polytopes.

2.2 Prove Lemma 2.1.3.

2.3 Show that the converse of Corollary 2.1.4 is wrong in dimension two.

2.4 Show that there are inﬁnitely many, non-isomorphic lattice tetrahedra con-
taining only four lattice points.

2.5 Prove Proposition 2.1.5. Here are some hints: 1. Translate the triangle so that
it is given as conv(0, v, w). Then consider the reﬂection x 7→ v + w − x. Deduce
that the parallelogram conv(0, v, w, v + w) has only its vertices as lattice points.
2. Look at the tiling of R2 by translations of this parallelogram. Deduce that any
lattice point in Z
2 is of the form k1 v + k2w. Why does this prove the statement?

2.6 Show that ∆d has volume 1/d!. (Hints: think of ∆d as iterated pyramids or
subdivide [0, 1]d into d! simplices).

2.7 Prove Lemma 2.3.9.

2.8 A vector v ∈ Z
2 (or in any lattice) is called primitive if it is not a non-trivial
integer multiple of some other lattice vector.

(1) Show that any primitive v ∈ Z
2 is part of a lattice basis.
(2) Show that every rational simplicial 2-dimensional cone is unimodularly equiv-
alent to a cone spanned by ( 1//0 ) and ( p//q ) for integers 0 ≤ p < q.

2.9 Let Λ ⊆ Rd be a lattice wit fundamental parallelepiped Π. Show that the
lattice translates of Π cover Rd without overlap, i.e.
⋃

x∈Λ(x + Π) = Rd

and (x + Λ) ∩ ( y + Λ) = ∅ for x, y ∈ Λ, x ̸= y.

2.10 Let Λ ⊆ Zd be a sub-lattice of rank d, and let v1, . . . , vd be a basis of Λ with
fundamental parallelepiped

Π(v1, . . . , vd ) = n∑ λi bi | λi ∈ [0, 1)
o .

Show that
 |Zd /Λ| = |Π(v1, . . . , vd ) ∩ Zd | = det Λ .

— 26 — Haase, Nill, Paffenholz: Lattice Polytopes

3
Ehrhart Theory

In this chapter we will learn all about counting lattice points in polytopes. The
central theorem of this chapter gives a very beautiful relation between geometry
and algebra. It is due to Eugène EHRHART and tells us that the function counting
the number of lattice points in dilates of a polytope P ⊆ Rd ,

|k · P ∩ Zd | ,

is the evaluation of a polynomial ehrP (t) of degree d in k. The polynomial ehrP (t)
is the Ehrhart polynomial of P, and the main part of this chapter deals with meth-
ods to compute this and related functions.

3.1 Motivation

3.1.1 Why do we count lattice points?

Before we delve into the theory and compute Ehrhart polynomials of polytopes
we want to introduce some problems where counting, enumerating or sampling
lattice points appear naturally if one wants to solve the problem.

Knapsack type problems Assume that you are given a container C of size ℓ
(the knapsack), and k goods of a certain sizes s1, . . . , sk and values v1, . . . , vk. Two
important variants of a knapsack problem are the tasks to ﬁll the container either
with goods of the highest possible total value, i.e. to solve the problem

max x1 v1 + · · · + xk vk
subject to x1s1 + · · · + xksk ≤ ℓ

xi ∈ {0, 1} for 1 ≤ i ≤ k ,
 27

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

or to ﬁll the container completely with goods of a prescribed total value v, i.e. to
solve
 x1 v1 + · · · + xk vk = v

x1s1 + · · · + xksk = ℓ

xi ∈ {0, 1} for 1 ≤ i ≤ k .

Here is a simple example of such a problem. The U.S. currency has four dif-
ferent coins that are in regular use, the penny (1¢), nickel (5¢), dime (10¢), and
the quarter (25¢). You may wonder how many different ways there are to pay 1$
using exactly ten coins. With a little consideration you probably come up with the
solution
 100 = 5 · 1 + 0 · 5 + 2 · 10 + 3 · 25

= 0 · 1 + 6 · 5 + 2 · 10 + 2 · 25

= 0 · 1 + 3 · 5 + 6 · 10 + 1 · 25

= 0 · 1 + 0 · 5 + 10 · 10 + 0 · 25 ,

so there are essentially four different ways. This is exactly the number of lattice
points in the polytope

P := ˆx ∈ R4 |
|
| x1, x2, x3, x4 ≥ 0, x1 + x2 + x3 + x4 = 10,

x1 + 5x2 + 10x3 + 25x4 = 100
 ˙ .

This may look like a much more complicated approach than just testing with some
coins. But what if you want to ﬁnd the 182 ways to pay 10$ using 100 coins, or
the 15876 ways to pay 100$ with 1000 coins?

Contingency Tables Consider the following table (which is a simpliﬁed version
of a table produced by the Statistische Landesamt Berlin for academic degrees
awarded at Berlin universities in 2005)

Diploma PhD Teacher

FU 1989 1444 299 3732
TU 1868 421 115 2404
HU 920 441 373 1774

4817 2306 787

You may ask how likely it is to have exactly this distribution of the entries of the
table, if its margins, i.e. the totals of degrees awarded at each university, and the
totals of different degrees awarded, are given. Assuming a uniform distribution,
you would need to know the number of possible tables with these margins. This
is the number of lattice points in the polytope

P :=
 



X ∈ R3×3
≥0
 |
|
| x11 + x12 + x13 = 3732, x21 + x22 + x23 = 2404,
x31 + x32 + x33 = 1774, x11 + x21 + x31 = 4817,
x12 + x22 + x32 = 2306, x13 + x23 + x33 = 787
 



 .

There are 714,574,663,432 of them.

We hope that these examples have awoken your interest in a more systematic
study on how one can compute those numbers. In the next section we will explore

— 28 — Haase, Nill, Paffenholz: Lattice Polytopes

Ehrhart Theory (preliminary version of December 7, 2012)

methods to obtain them, and to enumerate lattice points, and more generally
study the structure of lattice points in polytopes. Our strategy to count lattice
points in (dilates of) polytopes is to treat simplices ﬁrst. We can then subdivide
general polytopes into simplices and use inclusion-exclusion to generalize our
results.

3.1.2 First Ehrhart polynomials

Let S ⊆ Rd , and let k ∈ Z>. The k-th-dilation of a set of S is the set

kS := {kx | x ∈ S} .

In this section we will apply the methods developed in the previous section to
count integral points in dilations of a polytope P and its interior. We introduce
the following counting function.

3.1.1 Deﬁnition. The Ehrhart counting function of a bounded subset S ⊆ Rd is
the function N → N
 ehrS(k) := |kS ∩ Zd | .

We want to look at some simple examples of Ehrhart counting functions. Let
L := [a, b] ⊆ R, a, b ∈ R be an interval on the real line. Here, counting is easy,
L contains ⌊b⌋ − ⌈a⌉ + 1 integers. The k-th dilate of P is [ka, kb]. By the same
argument it contains ⌊kb⌋ − ⌈ka⌉ + 1 integral points, so

ehrL(k) = ⌊kb⌋ − ⌈ka⌉ + 1 .

Figure 3.1 shows the interval I = [0, 3
2 ] and its second and third dilation.
If the boundary points a and b are integral and a ≤ b, then we can simplify
the formula. In this case also all multiples of a and b are integral, and we can
omit the ﬂoor and ceiling operations to obtain

ehrL(k) = k(b − a) + 1 .

We observe that this is a polynomial of degree 1 in k. We will see that this ob-
servation is a very special case of the Theorem of EHRHART that we will prove
below.
Now we turn to an example in arbitrary dimension. The d-dimensional stan-
dard simplex is the convex hull

∆d := conv(0, e1, . . . , ed )

of the origin and the d standard unit vectors. Its exterior description is given by

xi ≥ 0 for 1 ≤ i ≤ d and
 d∑

i=1 xi ≤ 1 .

3.1.2 Proposition. Let ∆d be the d-dimensional standard simplex. Then

ehr∆d (k) = d + k

d
  = (d + k) · (d + k − 1) · . . . · (k + 1)

d! .

Observe that this is a polynomial in the variable k of degree d with leading coef-
ﬁcient 1/d! .
 L
2L
3L
 Fig. 3.1

Fig. 3.2: Lattice points in a stan-
dard simplex.

Haase, Nill, Paffenholz: Lattice Polytopes — 29 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

Fig. 3.3: The upper ﬁgure
is not a polyhedral complex.
The second is, but it is not
pure, the third is also pure.
 Proof. There is a bijection between the lattice points in k∆d and sequences of
k dots and d bars: to each such sequence, assign the vector x ∈ Rd whose ith
coordinate equals the number of dots between the (i − 1)st bar and the ith bar.

· · | · · · ||· ↔ x = (2, 3, 0, 1)

This yields a bijection between the sequences and lattice points with non-negative
coordinates and with ∑ xi ≤ k. ⊓⊔

Another simple, but very important example is the unit cube

Cd := {x ∈ Rd | 0 ≤ x ≤ 1} = [0, 1]d .

This is the exterior and interior description of the cube. It has 2d facets and
the 2d 0/1-vectors as its vertices. We will return to this example at many places
throughout these notes. The k-th dilate of the cube is kCd = k · [0, 1]d = [0, k]d .
Hence, the Ehrhart counting function is given by

ehrCd (k) = (k + 1)d .

Note again that this is a polynomial in k of degree d.

3.2 Triangulations and Half-open Decompositions

We start our considerations with subdivisions of polytopes into smaller pieces and
study polyhedral complexes and triangulations. Our approach will lead beyond
the classic theory of subdivisions, as we will want to decompose the polytopes
and cones into half-open simplices and simplicial cones for a ﬁner analysis of
lattice points.

3.2.1 Deﬁnition (polyhedral complex). A polyhedral complex C is a ﬁnite family
of polyhedra (the cells of the complex) such that for all P, Q ∈ C

(1) if P ∈ C and F is a face of P then F ∈ C, and
(2) F := P ∩ Q is a face of both P and Q.

A cell P is maximal if there is no Q ∈ C strictly containing it. These cells
are sometimes also called the facets of C. The dimension of C is the maximal
dimension of a cell of the complex. A complex is pure if all maximal cells have the
same dimension. In this case the maximal cells are the facets of the complex. We
will denote by C[k] the set of k-dimensional faces of C.
A polyhedral complex S is a subcomplex of C if its cells are a subset of the cells
of C.

3.2.2 Example. Here are some examples of a polyhedral complex. See also Fig-
ure 3.3.

(1) Any polytope or cone can be viewed as a polyhedral complex. This complex
has one maximal cell, the cone or polytope itself. This is also called the trivial
subdivision of the cone or polytope. In general, subdivisions are deﬁned with
the next deﬁnition below.
(2) The boundary complex of a d-dimensional polytope naturally has the struc-
ture of a pure polyhedral complex. The maximal cells are the facets of the
polytope, and its dimension is d − 1, the dimension of the facets of the poly-
tope.
(3) See the middle ﬁgure in Figure 3.3 for a non-pure polyhedral complex. It has
three 2-dimensional maximal cells and one 1-dimensional maximal cell.

— 30 — Haase, Nill, Paffenholz: Lattice Polytopes

Ehrhart Theory (preliminary version of December 7, 2012)

(4) Fans naturally have the structure of a polyhedral complex. In this case all cells
are cones.

3.2.3 Deﬁnition (subdivision and triangulation). A subdivision of a polytope
(cone) P is a polyhedral complex S such that P = ⋃
F ∈S F .
A subdivision T is a triangulation of P if all cells are simplices (simplicial
cones). It is without new vertices, if V(∆d ) ⊆ V(P) for any ∆d ∈ T.

We will use the basic fact that for every ﬁnite V ⊆ Rd the polytope conv V has
a triangulation with vertex set V . Similarly, the cone pos V has a triangulation
with rays {R≥0 v : v ∈ V } [11].
If we are given a triangulation of a polytope we cannot simply add the number
of lattice points of the cells because the cells overlap. In order to avoid inclusion-
exclusion, we will now describe a way to partition the cone into pairwise disjoint
half-open simplicial cones [6, 18]. There are various ways to do this. We will use
a generic reference point as an arbiter to decide which points belong to which
cells.

3.2.4 Deﬁnition (half-open decomposition). Let V = {v1, . . . , vd } ⊆ Rd be lin-
early independent, and C := cone V . Call a point x ∈ Rd generic with respect to
C if all coefﬁcients λv in the unique representation x = ∑ λv v are non-zero. Set
I+(x) := {v ∈ V : λv > 0} and I−(x) := {v ∈ V : λv < 0}.
In case x is generic, deﬁne the near half-open cone C(x], the near half-open
parallelepiped i (V, x), the far half-open cone C[x), and the far half-open paral-
lelepiped i
(V, x) as follows.

C(x] := n∑
v∈V µv v : µv > 0 for v ∈ I+(x) and µv ≥ 0 for v ∈ I−(x)
o

i (V, x) := n∑
v∈V µv v : µv ∈ (0, 1] for v ∈ I+(x) and µv ∈ [0, 1) for v ∈ I−(x)
o

C[x) := n∑
v∈V µv v : µv ≥ 0 for v ∈ I+(x) and µv > 0 for v ∈ I−(x)
o

i
(V, x) := n∑
v∈V µv v : µv ∈ [0, 1) for v ∈ I+(x) and µv ∈ (0, 1] for v ∈ I−(x)
o

See Figure 3.4 for an illustration. For x strictly in the relative interior of C we
abbreviate
 Π(V ) := i
(V, x)

and call Π(V ) the fundamental parallelepiped of C with generating set V .

This means that a point y belongs to C(x] if and only if y ∈ C and all V
coordinates for v ∈ I+ are strictly positive; y belongs to C[x) if and only if y ∈ C
and all V coordinates for v ∈ I− are strictly positive. Also, observe that C[x) =
C(−x] and i
(V, x) = i (V, −x).

3.2.5 Proposition. Let V = {v1, . . . , vd } ⊆ Rd be linearly independent, and suppose
x ∈ Rd is generic with respect to the simplicial cone C := cone V . Denote by Λ the
lattice generated by V .
Then any point w ∈ Rd has a unique representation w = y + z with y ∈ Λ and
z ∈ i
(V, x). Alternatively, we could choose z ∈ i (V, x).

Proof. Replacing x with −x, we only need to prove the assertion with z ∈i
(V, x). As above, let x = ∑ λv v be the unique representation of x in the gener-
ators of the cone and set I± := {v : λv ≷ 0}.
 0

v1 v2

x x ′

i
(V, x) = i (V, x ′)

Fig. 3.4: C[x) = C(x ′]

Haase, Nill, Paffenholz: Lattice Polytopes — 31 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

For the existence, given w, write w = ∑ µv v, and set

y := ∑

v∈I+
 
µv v + ∑

v∈I−(

µv − 1)v and

z := w − y .

Then clearly y ∈ Λ and w = y + z. Also, the coefﬁcients of z satisfy µv − 
µv ∈
[0, 1) for v ∈ I+ and µv − (

µv − 1) ∈ (0, 1] for v ∈ I−, so that z ∈ i
(V, x).
For the uniqueness, assume that there is a second decomposition w = y ′ + z′.
We can write z = ∑ αv v and z′ = ∑ α
′
v v with αv, α
′
v ∈ [0, 1) for v ∈ I+ and
αv, α
′
v ∈ (0, 1] for v ∈ I−. Hence, |αv − α
′
v| < 1 for all v ∈ V .
From z′ − z = y − y ′ ∈ Λ we conclude that αv − α
′
v ∈ Z so that αv = α
′
v. This
implies z = z′ and y = y ′. ⊓⊔

We can further decompose each of the half-open cones into half-open boxes.
Recall that NV stands for the set of N-linear combinations of V .

3.2.6 Corollary. In the notation of Deﬁnition 3.2.4, the half-open cones can be de-
composed into a disjoint union of translates of half-open boxes.

C[x) = ⊔

w∈NV w + i
(V, x) and C(x] = ⊔

w∈NV w + i (V, x) .

Proof. The fact that the translates by Λ-vectors are pairwise disjoint follows from
the uniqueness in Proposition 3.2.5. From the existence part we see that Rd is
covered by all Λ-translates of i
(V, x). It remains to observe that for w ∈ Λ

C[x) ∩ •w + i
(V, x)
− =
 ¨w + i
(V, x) for w ∈ NV
; else,

and mutatis mutandis for C(x]. ⊓⊔

Let a triangulation of a cone D be given. In the following proposition we show
how to construct a decomposition of D into disjoint half-open simplicial cones
from this triangulation. This needs a preliminary lemma that we will prove ﬁrst.
For y ∈ Rd and ϵ ∈ R write yϵ := (1 − ϵ) y + ϵ x for a point on the line through y
and x. With this notation, we can recharacterize the half-open cones as follows.

3.2.7 Lemma. Let V = {v1, . . . , vd } ⊆ Rd be linearly independent, and suppose
x ∈ Rd is generic with respect to the simplicial cone C := cone V . Then y ∈ C[x) if
and only if yϵ ∈ relint C for all small enough ϵ > 0. Similarly, y ⊆ C(x] if and only
if y−ϵ ∈ relint C for all small enough ϵ > 0.

Proof. In the notation of Deﬁnition 3.2.4, the vth V -coordinate of yϵ equals (1 −
ϵ)µv + ϵλv. The ﬁrst equivalence of the lemma amounts to observing that

(1 − ϵ)µv + ϵλv > 0 for all small enough ϵ > 0

if and only if µv > 0 or  
µv = 0 and λv > 0 .

The second equivalence of the lemma amounts to observing that

(1 + ϵ)µv − ϵλv > 0 for all small enough ϵ > 0

if and only if
 — 32 — Haase, Nill, Paffenholz: Lattice Polytopes

Ehrhart Theory (preliminary version of December 7, 2012)

µv > 0 or  
µv = 0 and λv < 0 . ⊓⊔

3.2.8 Proposition. Let T be a triangulation of the d-cone C, and let x ∈ C be
generic with respect to all cones D ∈ T. Then we have the following decompositions
into pairwise disjoint half-open cones:

C = ⊔

D∈T[d] D[x) and relint C = ⊔

D∈T[d] D(x] .

Of course, genericity of x implies x ∈ relint D ⊆ relint C for some D ∈ T[d]. A
half-open decomposition in this way is illustrated in Figure 3.5.

Proof. For y ∈ C, there is a unique D ∈ T[d] so that yϵ ∈ relint D for small enough
ϵ > 0. By Lemma 3.2.7 this is the unique D with y ∈ D[x).
As x ∈ relint C, we have y−ϵ ∈ C if and only if y ∈ relint C. In that case, again
by Lemma 3.2.7, there is a unique D with y ∈ D(x]. ⊓⊔

3.3 Ehrhart’s Theorem

In this section we will prove that ehrP (k) is indeed a polynomial. This requires us
to ﬁnd an efﬁcient way to encode lattice points in (multiples of) a polytope. We
will see that it is convenient to work with the cone over a polytope and encode its
lattice points. We will do this in the following section. The next section will then
use this to write down the Ehrhart polynomial.

3.3.1 Encoding Points in Cones: Generating Functions

At the beginning of this chapter we have seen some basic examples where count-
ing integer points in a polytope appears, and we have seen some simple instances
of Ehrhart polynomials. Now let us think for a moment how one could attack
the problem of computing the Ehrhart polynomial and enumerate or count lattice
points in a polytope. A ﬁrst question we will have to solve is to ﬁnd a way to
encode all lattice points in a lattice polytope in an efﬁcient way. For example, let
us list all lattice points in the polytope P[0,3] := [0, 3], see Figure 3.6. The naive
approach is to list all points in P:
 0, 1, 2, 3 .

Instead, we could replace each lattice point by the monomial with this exponent
(vector) and sum up:
 1 + t + t 2 + t 3 .

Going even further we can replace the polynomial by a geometric series:

G[0,3] (t) := 1 − t 4

1 − t .

Writing the lattice points as a polynomial, or even rewriting the polynomial as a
rational function may look strange at ﬁrst. This idea reveals its power when we
try to do the same for the dilated polyhedron [0, 10002]. Enumerating the points

0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, . . .

would be a tedious task. Similarly, the second approach
 x

x

Fig. 3.5: A triangulation and its
half open decomposition.

Fig. 3.6: The polytope P[0,3].

Haase, Nill, Paffenholz: Lattice Polytopes — 33 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

Fig. 3.7: The polygon of Exam-
ple 3.3.1.
 1 + t + t 2 + t 3 + t 4 + t 5 + t 6 + t 7 + t 8 + t 9 + t 10 + t 11 + t 12 + · · ·

does not work well. The third, however, does not require much change compared
to the ﬁrst example:
 G[0,10002] (t) := 1 − t 10003

1 − t .

If we try to do the same for the unbounded polyhedron [0, ∞), then our ﬁrst two
approaches obviously become infeasible. However, the third turns out to be even
shorter and more appealing:
 G[0,∞) (t) := 1

1 − t .

As this extended example suggests, the generating function we used to encode
the lattice points will indeed provide a powerful bookkeeping tool for counting
and enumerating lattice points in polytopes. We will back up this idea with more
evidence for its usefulness in the next section. To actually count the points using
this generating function we have to evaluate G[0,3] (t) = 1−t 4

1−t at t = 1. Unfortu-
nately, this is a zero of the denominator of the function. Even worse, we will see
that this not just happens in this example, but it is always the case. Luckily, this
singularity can always be removed, as we will later see.
For reasons that will soon become apparent we want to encode lattice points
not only in polytopes, but more generally in any bounded or unbounded subset
of Rd . You should keep this in mind for the following considerations. In the above
example of the one-dimensional cone x ≥ 0 ⊆ R we have seen that we can use
rational functions in one variable t to describe the inﬁnite series of all monomials
corresponding to the lattice points in the cone. We want to formalize this idea
and generalize it to all dimensions. Let k be some ground ﬁeld (you can think of
k = C). We assign the monomial

t a := t a1
1 t a2
2 · · · t ad
d

in d variables to a lattice point a = (a1, . . . , ad ) ∈ Zd . In the above example all
lattice points were non-negative and thus lead to the “usual kind” of monomials.
In general, coordinates ai may be negative, so this is a Laurent polynomial living
in the ring L := k[t ±1
1 , . . . , t ±1
d ]. Moreover, note that the sum of monomials for the
cone x ≥ 0 is inﬁnite. Since we do not care about convergence, we will consider
our sums as series in a subset of the L-module bL := k⟦t ±1
1 , . . . , t ±1
d ⟧ of formal
Laurent series.

3.3.1 Example. Let P be the polygon

P := conv  0 2 2 3
1 −1 2 0
 

(see Figure 3.7). We list the lattice points as monomials in the Laurent polyno-
mial t 2
1 t 2
2
+ t2 + t1 t2 + t 2
1 t2

+ t1 + t 2
1 + t 3
1
+ t 2
1/t2 .

— 34 — Haase, Nill, Paffenholz: Lattice Polytopes

Ehrhart Theory (preliminary version of December 7, 2012)

3.3.2 Deﬁnition (integer point series). For S ⊆ Rd the integer point series bGS is
the formal Laurent series
 bGS := ∑

a∈S∩Zd t a ∈ bL .

A Laurent series bG ∈ bL is summable if there is a Laurent polynomial g ∈ L such
that the series g bG is a Laurent polynomial.

Clearly all Laurent polynomials are summable. Translating a set S ⊆ Rd by some
integral vector a ∈ Zd amounts to multiplication of its generating series with t a,

bGa+S (t) = t a bGS (t) .

We will denote the set of all summable Laurent series by Lsum. We leave the proof
of the following proposition to the reader in Exercise 3.1.

3.3.3 Proposition. Lsum is a L-submodule of bL. ⊓⊔

We will consider summable series in the following only for (possibly half-open)
cones and fundamental parallelepipeds. We discuss some important examples be-
fore we study the general case.

(1) Consider ﬁrst the polyhedron P∞ = [0, ∞) that we introduced above. The
integer point series is

bGP∞ (t) = ∑

a∈Z≥ t a = 1 + t + t 2 + t 3 + · · · .

Using the polynomial g(t) := (1 − t) we obtain g(t)bGP∞ (t) = 1, so bGP∞ (t) is
a summable series.
(2) Now let C := cone(e1, e2) for the standard unit vectors e1, e2 ∈ R2. Then

bGC (t, s) = ∑

a,b∈Z≥ t as b = 1 + t + s + t 2 + s2 + ts + t 3 + · · · .

Similar to the previous case we can use the polynomial g(t, s) := (1− t)(1−s)
to obtain g(t, s)bGC (t, s) = 1. Hence, bGC (t, s) is a summable series.
(3) Finally, let V := {a1, . . . , ad } and C = cone V be a rational cone. Let x ∈ C
and Π the fundamental parallelepiped given by V . By Proposition 3.2.5 we
can write x ∈ C ∩ Zd uniquely as x = y + z for y ∈ Π and z ∈ NV , and
conversely, y + z′ ∈ C ∩ Zd for any z′ ∈ NV . Furthermore,

d∏

i=1 (1 − t ai ) · ∑

z∈NV t z = 1 .

With this observation we can compute

d∏

i=1 (1 − t ai ) · ∑

x∈C∩Zd t x =
 d∏

i=1 (1 − t ai ) · ∑

y∈Π∩Zd
 ∑

z∈NV t y+z

=
 d∏

i=1 (1 − t ai ) · ∑

y∈Π∩Zd t y · ∑

z∈NV t y = ∑

y∈Π∩Zd t y .

Hence, bGC (t) is summable.

Haase, Nill, Paffenholz: Lattice Polytopes — 35 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

In Exercise 3.2 you will prove the following proposition.

3.3.4 Proposition. There is a natural homomorphism from summable series to ra-
tional functions
 Φ : Lsum −→ R := k(t1, . . . , td ) ,

mapping bG to f /g if g bG = f in bL. ⊓⊔

3.3.5 Deﬁnition (integer point generating function). Suppose C ⊆ Rd is a

point set so that bGC (t) is summable. The integer point generating function of C is

GC (t) := Φ(bGC (t)) .

L is a submodule of Lsum, and Φ|L is the identity map. If X ⊆ Rd is bounded, then

GX (t) = ∑

a∈X ∩Zd t a ,

so evaluating GX at t = 1 gives the number of lattice points:

GX (1) = |X ∩ Zd | .

In the one-dimensional example P∞ = [0, ∞) above we have already computed
the image of the generating series in R, it is GP∞ (t) = 1
1−t . In order to understand
the situation for higher-dimensional cones C ⊆ Zd we will use the half-open
decomposition from Section 3.2. So we have to study the generating series for
half-open simplicial cones. The following theorem generalizes our considerations
for the general simplicial cone that we made in the third example above.

3.3.6 Theorem. Let V = {v1, . . . , vd } ⊆ Zd be a linearly independent set of primitive
vectors, let C = cone V , and let x ∈ Rd be generic with respect to V . Then the integer
point generating function of the half-open cone C[x) is summable, and

GC[x) (t) = G i
(V,x) (t)

(1 − t v1 )(1 − t v2 ) · · · (1 − t vd ) . (3.3.1)

Proof. Let Λ = Λ(V ) be the lattice generated by V . By Proposition 3.2.5 every
lattice point in C[x) can be written uniquely as a sum of a Λ-point in C and a Zd -
point in i
(V, x). This translates into the following identity of summable formal
power series:

bGC[x) (t) = ∑

v∈ i
(V,x)∩Zd
 ∑

w∈C∩Λ t v+w = ∑

v∈ i
(V,x)∩Zd t v ∑

w∈C∩Λ t w .

Applying Φ yields the desired identity of rational functions. ⊓⊔

In particular, this covers the case x ∈ int (C), which gives the integer point gener-
ating function for simplicial cones with fundamental parallelepiped Π(V )

GC[x) (t) = GΠ(V ) (t)

(1 − t v1 )(1 − t v2 ) · · · (1 − t vd ) . (3.3.2)

3.3.7 Corollary. Let C be a rational cone in Rd , let T be a triangulation of C into
rational simplicial cones, and let x ∈ C be generic. Then

— 36 — Haase, Nill, Paffenholz: Lattice Polytopes

Ehrhart Theory (preliminary version of December 7, 2012)

bGC (t) = ∑

S∈T[d] bGS[x) (t) , and bGint C (t) = ∑

S∈T[d] bGS(x] (t) . (3.3.3)

In particular, both series are summable, and equation (3.3.3) also holds on the level
of rational functions.

Proof. Equation (3.3.3) is a translation of Proposition 3.2.8 into generating func-
tions. By Theorem 3.3.6, all the summands are summable Laurent series. ⊓⊔

Theorem 3.3.6 shows that the hard part of computing the integer point gener-
ating function bG of a cone is to determine all integer points in the fundamental
parallelepiped of the cone.

3.3.2 Counting Lattice Points in Polytopes

We have seen in Theorem 3.3.6 how we can encode lattice points in simplicial
(half-open) cones. We want to use this to count integral points in dilations of a
lattice polytope. The connection will be given by the following deﬁnition. The
cone over a polytope is the cone

C(P) := cone  1
x
  |
|
| x ∈ P .

See Figure 3.8 for the cone over a triangle. For any k ≥ 0 we can recover the
k-th dilate of P by intersecting C(P) with the hyperplane x0 = k, and the lattice
points in kP by intersecting with {k} × Zd . We want to connect this to the integer
point generating function of the cone C(P). To emphasize the special role of the
additional variable t0, we write points in the cone in the form

t := (t0, t) .

The 0th coordinate functional u: Zd+1 → Z yields the monomial substitution
t = (t0, 1, . . . , 1). Hence,

bGC(P)  t0, 1 = 1 + ∑

k≥1 |kP ∩ Zd | t k
0 = 1 + ∑

k≥1 ehrP (k) t k
0 ,

and the resulting power series in one variable is summable.

3.3.8 Deﬁnition. Let P be a lattice d-polytope. The Ehrhart series of P is the
summable formal power series

bEhrP (t) := 1 + ∑

k≥1 ehrP (t) t k ∈ k⟦t⟧

in one variable t. The corresponding rational function will be denoted EhrP (t) :=
Φ(bEhrP (t)) ∈ k(t).

We summarize the above observation in the following proposition.

3.3.9 Proposition. Let P ⊆ Rd be a lattice polytope, let T be a triangulation of the
cone C(P) which is induced by a lattice triangulation of P, and let x ∈ C(P) be
generic. Then bEhrP (t) is summable with sum

EhrP (t) = GC(P) (t, 1) =
 ∑

S∈T[d+1] G i
(S,x) (t, 1)

(1 − t)d+1 . (3.3.4)
 Fig. 3.8

Haase, Nill, Paffenholz: Lattice Polytopes — 37 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

Our next goal is to show that the Ehrhart counting function of a lattice polytope
is given by a polynomial.

3.3.10 Proposition. Let S be a d-simplex. Then

EhrS(t) = h
⋆(t)

(1 − t)d+1

where h
⋆ is a polynomial of degree ≤ d and h
⋆(1) ̸= 0. Further, for h
⋆(t) =
∑d
k=0 h
⋆
k t k, we have
 h
⋆
k = #(Π(C(S)) ∩ Zd+1 ∩ {x | x0 = k}).

Proof. Let S be a lattice simplex with vertex set V := {v0, v1, . . . , vd }. We let vi =
(1, vi), so that C(S) = cone(v0, v1, . . . , vd ) with fundamental parallelepiped Π(V ).
Combining Proposition 3.3.9 with (3.3.2) we obtain that

EhrS(t) = h
⋆(t0)

(1 − t0)d+1

for some Laurent polynomial h
⋆(t0) = GΠ(V )  
(t0, 1)

.
We need to examine the degree of t0 in GΠ(V )  
(t0, t)

. The t0-degree of a

monomial t a that appears in this Laurent polynomial is the ﬁrst coordinate of the
vector a. As all vi have a 1 in the ﬁrst coordinate and

a = λ0 v0 + . . . + λd vd

for some 0 ≤ λ0, . . . , λd < 1, we know that the ﬁrst coordinate a0 of a satisﬁes

0 ≤ a0 ≤ λ0 + · · · + λd < d + 1 .

This implies that the t0-degree of t a is at most d. So evaluating bGΠ(V )  t at
t = (t, 1, . . . , 1) results in a polynomial of degree at most d. Further, it has a
non-zero constant coefﬁcient, as

bGΠ(V ) ((1, . . . , 1)) = |Π(V ) ∩ Zd+1|

and 0 ∈ Π(V ).
The second claim follows from the above observation that the t0-degree of a
monomial t a in bGΠ(C(S))  t is the coordinate a0 of the exponent a. But this is
exactly the height of a in the cone C(S). ⊓⊔

3.3.11 Example. h
⋆ of ∆d .

To proceed we need a well-known result on generating functions.

3.3.12 Proposition. Let f , g : R → R be such that

∞∑

t=0 f (t)z t = g(z)

(1 − z)d+1 .

Then f (t) is a polynomial of degree d if and only if g(z) = g0+g1z+g2z2+. . .+gd zd

is a polynomial of degree at most d with non-vanishing constant coefﬁcient. In this
case:
 — 38 — Haase, Nill, Paffenholz: Lattice Polytopes

Ehrhart Theory (preliminary version of December 7, 2012)

f (t) = g0
t + d

d
  + g1
t + d − 1

d
  + . . . + gd
  t

d
 .

Proof. We deﬁne the polynomials f j(t) :=  t+d− j
d  for 0 ≤ j ≤ d. The set
{ fo, . . . , fd } is a basis of R[t]≤d .
Let f be a polynomial of degree d. Then there are g0, . . . , gd such that

f (t) =
 d∑

j=0 g j f j(t) =
 d∑

j=0 g j
t + d − j

d
  .

The coefﬁcient of t d is 1
d! ∑ g j, so this sum is non-zero. We compute

∑

t≥0
 d∑

j=0 g j
t + d − j

d
 zk =
 d∑

j=0 g j ∑

t≥0
 t + d − j

d
 zk

=
 d∑

j=0 g j ∑

t≥ j
 t + d − j

d
 zk

=
 d∑

j=0 g j ∑

t≥0
 t + d

d
 z t+ j =
 d∑

j=0 g jz j ∑

t≥0
 t + d

d
 zk

=
 ∑d
j=0 g jz j

(1 − z)d+1 = g(z)

(1 − z)d+1

where the second equality follows as the binomial coefﬁcient is 0 unless k− j+1 ≥
0. Clearly deg g ≤ d and g(1) = ∑ g j ̸= 0. The converse direction is similar. ⊓⊔

Using this Proposition and a standard inclusion-exclusion argument which we
leave to the reader, EHRHART’s theorem is now proved.

3.3.13 Theorem (EHRHART’s Theorem). Let P be a lattice polytope in Rd . Then

EhrP (t) = 1 + ∑

k≥1 ehrP (k) t k = h
⋆(t)

(1 − t)d+1

where ehrP (t) is a polynomial of degree d, h
⋆ is a polynomial of degree ≤ d with
integer coefﬁcients, and h
⋆(1) ̸= 0.

By Proposition 3.3.12

ehrP (t) = t + d

d
  + h
⋆
1
t + d − 1

d
  + · · · + h
⋆
d−1
t + 1

d
  + h
⋆
d
  t

d
 . (3.3.5)

The previous result shows that the Ehrhart counting function k 7→ ehrP (k) ex-
tends to a polynomial function t 7→ ehrP (t). We will use the same symbol for
these two functions.

3.3.14 Deﬁnition (Ehrhart polynomial). For a polytope P the polynomial ehrP (t)
as in the previous theorem is the Ehrhart polynomial of P.

3.3.15 Deﬁnition (h
⋆-polynomial). The polynomial h
⋆ that appears in the nu-
merator of the rational generating function of the Ehrhart series is the h
⋆-
polynomial of P.

Let P be a d-dimensional polytope and ehrP (t) := c0 + c1 t + c2 t 2 + · · · + cd t d its
Ehrhart polynomial with coefﬁcients c0, c1, . . . , cd ∈ R.

Haase, Nill, Paffenholz: Lattice Polytopes — 39 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

3.3.16 Proposition. cd is the volume of P.

Proof. This follows from a simple computation:

vol(P) :=
 ∫
P dx = lim
k→∞ 1

kd |P ∩ 1

k Zd | = lim
k→∞ 1

kd |kP ∩ Zd |

= lim
k→∞ 1

kd ehrP (k) = cd . ⊓⊔

3.3.17 Deﬁnition. The normalized volume Vol(P) of a d-dimensional lattice poly-
tope P is Vol(P) = d!cd = d! vol P.

Using (3.3.5) and the observation that, for any k,  t+d−k
d  has degree d with lead-
ing coefﬁcient 1, we get the following immediate consequence of this proposition.

3.3.18 Corollary. h
⋆(1) = ∑d
i=0 h
⋆
i = Vol(P). ⊓⊔

3.3.19 Corollary. Let P be a lattice d-polytope. Then the constant term of the
Ehrhart polynomial is 1.

Proof. We evaluate (3.3.5) for t = 0. Note that by Theorem 3.3.23 the constant
coefﬁcient of h
⋆ is 1. So we can compute

ehrP (0) = d

d
 + h
⋆
1
d − 1

d
  + · · · + h
⋆
d−1
1

d
 + h
⋆
d
 0

d
 = d

d
 = 1 . ⊓⊔

3.3.20 Corollary. Let P be a lattice d-polytope. Then h
⋆
1 = ehrP (1) − d − 1 = |P ∩
Zd | − d − 1.

Proof. We evaluate (3.3.5) for t = 1:

ehrP (1) = d + 1

d
  + h
⋆
1
d

d
 + · · · + h
⋆
d−1
2

d
 + h
⋆
d
 1

d
 = (d + 1) + h
⋆
1 . ⊓⊔

The proof of the following result is Exercise 3.7.

3.3.21 Corollary. Let P be a lattice d-polytope with Ehrhart polynomial ehrP (t) =
1 + c1 t + c2 t 2 + · · · + cd t d . Then d!c j ∈ Z for 1 ≤ j ≤ d.

3.3.22 Example. Note that c1, . . . , cd−2 can be negative! As an example, consider
the Reeve simplex conv(0, e1, e2, e1 + e2 + 18e3). Then the Ehrhart polynomial is
1 − t + t 2 + 3t 3.

Using disjoint decompositions into half open cones we can improve on Ehrhart’s
theorem. This important result shows why the h
⋆-polynomial — albeit just a trans-
formation of the Ehrhart polynomial — is often more convenient to work with.

3.3.23 Theorem (STANLEY’s Non-Negativity Theorem). Let P be a d-dimensional
lattice polytope with
 bEhrP (t) = h
⋆
0 + h
⋆
1 t + h
⋆
2 t 2 + · · · + h
⋆
d t d

(1 − t)d+1 .

Then h
⋆
1, . . . , h
⋆
d ≥ 0 and h
⋆
0 = 1.

— 40 — Haase, Nill, Paffenholz: Lattice Polytopes

Ehrhart Theory (preliminary version of December 7, 2012)

Proof. Let C = C(P) be the cone over P. Let T be a triangulation of C induced by
a triangulation of P into lattice simplices. We have v0 = 1 for all generators v of
rays in T.
Let x ∈ C be generic with respect to T. Then

bEhrP (t) = GC (t, 1, . . . , 1)

= ∑

S∈T[d+1] GS[x) (t, 1, . . . , 1)

= ∑

S∈T[d+1]
 G i
(S,x) (t, 1, . . . , 1)
∏
v∈V (S)(1 − t v0 )

= ∑

S∈T[d+1]
 ∑
a∈ i
(S,x)∩Zd+1 t a0

(1 − t)d+1 .

So the numerator polynomial of each summand has non-negative integral coef-
ﬁcients. A summand has non-zero constant coefﬁcient if and only if there is a
lattice point a in i(S, x) with a0 = 0. By construction, this requires a = 0, so
there is at most one such point in each cone. But 0 ∈ S[x) if and only if all coefﬁ-
cients are allowed to be 0, i.e. x ∈ relint S. This happens for exactly one cone, so
h
⋆
0 = 1. ⊓⊔

Finally, let us note the following theorem proved by STANLEY in [26]. A completely
different proof appears in (Beck, Sottile [6]). The reader can give a proof using
the methods developed above in Exercise 3.9.

3.3.24 Theorem (STANLEY’s Monotonicity theorem). Let P and Q be two lattice
polytopes such that P ⊆ Q, d = dim Q and let h
⋆
P and h
⋆
Q be their h
⋆-polynomials.
Then h
⋆
P,i ≤ h
⋆
Q,i for all 0 ≤ i ≤ d.

Proof. proof missing

3.3.3 Counting the Interior: Reciprocity

The interior of L = [a, b] is int L = (a, b). For integers a, b we can count the
lattice points inside int L:
 ehrint L(k) = k(b − a) − 1 .

Evaluating ehrL(k) at −k for some positive integer k gives

ehrL(−k) = (−k)(b − a) + 1 = − ((−k)(b − a) − 1) = −ehrint L(−k) .

So for intervals the Ehrhart polynomial evaluated at negative integers counts
(up to a sign) the lattice points in the interior of the interval. This would be a
nice property, but maybe the example of an interval is too special to conjecture
such a relation in general. So let us compute the interior lattice points in a more
complicated example.
We consider the d-dimensional standard simplex ∆d that we have already seen
in the beginning of this chapter. We use the following observation to count lattice
points in the interior ∆d . When we only want to count the lattice points in the
interior of the k-th dilate of the simplex, then we can also look at all lattice points,
and leave out lattice points

(1) that have a 0 among their coordinates, or
(2) whose coordinates sum up to k.

Haase, Nill, Paffenholz: Lattice Polytopes — 41 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

This just means that we only want to count lattice points that satisfy the inequal-
ities xi ≥ 1 for 1 ≤ i ≤ d, and whose coordinates sum up to at most k − 1. Hence,
we want to count lattice points in the set deﬁned by the inequalities

xi ≥ 1 and
 d∑

i=1 xi ≤ k − 1 .

Translating this by 1 gives the simplex deﬁned by the inequalities

xi ≥ 0 and
 d∑

i=1 xi ≤ k − d − 1 ,

and this simplex clearly contains the same number of lattice points. We have
computed this number above, so

ehrint ∆d (k) = k − 1

d
  .

So also the number of interior points is a polynomial in k of degree d. From
d − k

d
  = (−1)d k − d + d − 1

d
  = (−1)d k − 1

d
 

we can conclude that
 ehrint ∆d (k) = (−1)d ehr∆d (−k) .

We can make the same observation as for the interval: The lattice points in the
interior of the k-th dilation of the simplex are (up to a sign) the evaluation at −k
of the Ehrhart polynomial!
Let us check one more example, before we attempt to prove our observation.
Consider the standard unit cube Cd . Counting the interior points in this case is
rather simple. We obtain

ehrint C (k) = (k − 1)d = (−1)d ((−k) + 1)d = (−1)d ehrC (−k) ,

and again, the number of lattice points in the interior is given by the Ehrhart
polynomial evaluated at negative values.

Let x = (x1, . . . , xd ) ∈ (Rd − {0})d . Then 1
x denotes the vector  1
x1 , . . . , 1
xd
 
.

3.3.25 Lemma. Let P ⊆ Rd be a simplicial cone with primitive generators V =
{v1, . . . , vd }, and let x ∈ Rd be generic.
Then the map
 α : i
(V, x) ∩ Zd+1 −→ i (V, x) ∩ Zd+1

x 7−→
 d∑

i=0 vi − x

is a bijection.

Proof. Let y ∈ i
(V, x), so y has a representation of the form

y = ∑

v∈I λv v + ∑

v∈J µv v for 0 < λv ≤ 1, 0 ≤ µv < 1

— 42 — Haase, Nill, Paffenholz: Lattice Polytopes

Ehrhart Theory (preliminary version of December 7, 2012)

Hence
 d∑

i=0 vi − y = ∑

v∈I (1 − λv)v + ∑

v∈J (1 − µv)v ∈ i (V, x) ∩ Zd+1 ,

which proves the claim. ⊓⊔

Let C be a polyhedral cone with a triangulation T, and let x ∈ C be generic
with respect to T. Then C = ⊔
S∈T[d] S[x) is a decomposition of C into half-open
simplicial cones.

3.3.26 Theorem (STANLEY’s Reciprocity Theorem). Let C be a d-dimensional
polyhedral cone with rational generators. Then

GC (t) = (−1)d Gint C
  1

t
  .

Proof. Let T by a triangulation of C and x ∈ C generic as above. For S ∈ T[d] let
V (S) be the set of primitive generators of S, and let s(S) = ∑
v∈V (S) v denote their
sum. Then, Lemma 3.3.25 implies

G i
(S,x) (t) = ∑

a∈ i
(S,x)∩Zd t a = ∑

a∈i (S,x)∩Zd t s(S)−a = t s(S) G
i (S,x)
  1

t
  .

We can just sum up this equation over all maximal cones to obtain the desired
result:

GC (t) = ∑

S∈T[d] GS[x) (t) = ∑

S∈T[d]
 G i
(S,x) (t)
∏
v∈V (S)(1 − t v) = ∑

S∈T[d]
 t s(S) G
i (S,x) • 1
t −

∏
v∈V (S)(1 − t v)

= (−1)d ∑

S∈T[d]
 G
i (S,x) • 1
t −

∏
v∈V (S)(1 − 1
t v ) = (−1)d ∑

S∈T[d] GS(x]
  1

t
 

= (−1)d Gint C
  1

t
  . ⊓⊔

Now we can state a theorem that formalizes our observation from the beginning
of this section.

3.3.27 Theorem (EHRHART-MACDONALD Reciprocity). Let P be a lattice d-polytope
with Ehrhart polynomial ehrP (t), and let k ∈ Z>. Then

ehrP (−k) = (−1)d | int kP ∩ Zd | .

The proof needs a little fact about the map Φ mapping summable Laurent series
to rational functions.

3.3.28 Lemma. Let f be a polynomial and g +, g − the rational functions corre-
sponding to ∑
k≥0 f (k)t k and ∑
k≤−1 f (k)t k. Then g +(t) + g −(t) ≡ 0.

Proof. It sufﬁces to prove this for the basis fm :=  t+m
m , m ∈ N, of R[t]. So pick
some m. Then
 ∑

k≥0 fm(k)t k = ∑

k≥0
 k + m

m
 t k = 1

(1 + t)m+1 .

Haase, Nill, Paffenholz: Lattice Polytopes — 43 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

We compute the other sum:

∑

k≤−1 fm(k)t k = ∑

k≤−1
 k + m

m
 t k = ∑

k≥1
 −k + m

m
 t −k

= ∑

k≥1(−1)mk − 1

m
 t −k = ∑

k≥m+1(−1)mk − 1

m
 t −k

= ∑

k≥0(−1)mk + m

m
 t −k−m−1 = (−1)m t −(m+1) ∑

k≥0
 k + m

m
 t −k

= (−1)m t −(m+1) 1

(1 − 1
t )m+1 = (−1)m

t m+1(1 − 1
t )m+1

= (−1)m

(t − 1)m+1 = (−1)m+1(−1)m

(1 − t)m+1

= − 1

(1 − t)m+1 . ⊓⊔

Proof (Proof of the EHRHART-MACDONALD-Reciprocity, Theorem 3.3.27). We con-
sider the generating function of the Ehrhart polynomial and compute:
∑

k≥1 ehrint P (k) t k = bEhrint P (t) = Gint C(P) (t, 1, . . . , 1)

3.3.26
= (−1)d+1 GC(P)
  1

t , 1, . . . , 1 = (−1)d+1bEhrP
  1

t
 

= (−1)d+1 ∑

k≥0 ehrP (k) 1

t k
 3.3.28
= (−1)d ∑

k≤−1 ehrP (k) 1

t k

= (−1)d ∑

k≥1 ehrP (−k) t k .

Comparing coefﬁcients in this equation gives the desired result. ⊓⊔

Let us give some more applications regarding the h
⋆-polynomial.

3.3.29 Deﬁnition (Degree and Codegree). The degree of P is deﬁned as

deg(P) := max(k ∈ N : h
⋆
k ̸= 0).

The codegree of P is deﬁned as

codeg(P) := d + 1 − deg(P).

Ehrhart’s theorem implies 0 ≤ deg(P) ≤ d, so 1 ≤ codeg(P) ≤ d + 1. The degree
of a lattice polytope can be seen as an algebraic measure of the complexity of a
lattice polytope. Its concrete geometric interpretation is given by the codegree.

3.3.30 Corollary. The codegree of a d-dimensional lattice polytope equals the small-
est positive integer k such that kP contains an interior lattice point.

Proof. This follows from Lemma 3.3.31 and Theorem 3.3.27. ⊓⊔

3.3.31 Lemma. Let p be a polynomial of degree d with rational generating function

— 44 — Haase, Nill, Paffenholz: Lattice Polytopes

Ehrhart Theory (preliminary version of December 7, 2012)

∑

t≥0 p(t)z t = h
⋆
0 + h
⋆
1 t + h
⋆
2 t 2 + · · · + h
⋆
d t d

(1 − t)d+1

Then h
⋆
d = h
⋆
d−1 = . . . = h
⋆
k+1 = 0 and hk ̸= 0 if and only if p(−1) = p(−2) = . . . =
p(−(d − k)) = 0 and p(−(d − k + 1)) ̸= 0. In this case, h
⋆
k = p(−(d + 1 − k)).

You will prove this result in Exercise 3.8. Applied to our situation this has the
following immediate consequence.

3.3.32 Corollary. Let P be a lattice polytope. The highest non-zero coefﬁcient h
⋆
deg(P)
of h
⋆ equals the number of lattice points in int P. ⊓⊔

Finally, using reciprocity it is possible to compute the second highest coefﬁcient
of the Ehrhart polynomial.

3.3.33 Proposition. Let P be a lattice polytope with Ehrhart polynomial ehrP (t) =
c0 + c1 t + c2 t 2 + · · · + cd t d . Then cd−1 equals half of the normalized surface area of
the boundary of P.

You will prove this result in Exercise 3.20.

3.3.4 Ehrhart polynomials of lattice polygons

As an example, we will completely classify Ehrhart polynomials of lattice poly-
gons in this section. Essentially, the main work was already done in the previous
chapter by proving Scott’s inequality in Theorem 2.2.2. Now, we just have to ex-
ploit the properties of the h
⋆-polynomial.

3.3.34 Proposition. A polynomial h
⋆
2 t 2+h
⋆
1 t +1 for h
⋆
1, h
⋆
2 ∈ N is the h
⋆-polynomial
of a lattice polygon if and only if

(1) h
⋆
2 = 0 and h
⋆
1 is arbitrary. Then P has no interior lattice points.
(2) h
⋆
2 = 1 and h
⋆
1 = 7. Then P ∼= 3∆2.
(3) 1 ≤ h
⋆
2 ≤ h
⋆
1 ≤ 3h
⋆
2 + 3. Then P has interior lattice points.

Proof. Let us ﬁrst show that these conditions are necessary. Note that h
⋆
2 is the
number of interior lattice points i, while h
⋆
1 = b + i − 3, where b is the number of
boundary lattice points. Moreover, vol(P) = Vol(P)/2 = (1 + h
⋆
1 + h
⋆
2)/2. Hence,
Scott’s theorem tells us that, if i ≥ 1 and P ̸∼= 3∆2, then h
⋆
1 ≤ 3h
⋆
2 + 3. Finally, if
i ≥ 1, then h
⋆
2 = i ≤ h
⋆
1 = b + i − 3, since b ≥ 3.
It sufﬁces to realize lattice polygons satisfying each of these conditions. For
i = 0, any b ≥ 3 can be realized by lattice polygons of the form as depicted in
Figure 3.9. In fact, as Exercise 3.21 shows these are precisely the lattice polygons
without interior lattice points.
Let i ≥ 1. The condition h
⋆
2 ≤ h
⋆
1 ≤ 3h
⋆
2 + 3 is equivalent to 3 ≤ b ≤ 2i + 6. The
case b = 3 is easy to realize, so let b ≥ 4. Then any of these cases is realized by
Figure 3.10. ⊓⊔

All possible pairs (h
⋆
1, h
⋆
2) are depicted in Figure 3.11.
Let us now deduce all Ehrhart polynomials c2 t 2 +c1 t +1 of lattice polygons. By
Pick’s Theorem 2.2.1 c2 equals the area of P, and by Proposition 3.3.33, c1 is half
the number of boundary lattice points of P. The following theorem characterizes
all pairs (c1, c2) that correspond to an Ehrhart polynomial of a polygon.

3.3.35 Corollary. A polynomial c2 t 2 +c1 t +1 with c1, c2 ∈ 1/2Z and c1 ≥ 3/2 deﬁnes
the Ehrhart polynomial of a lattice polygon P if and only if one of the following three
conditions is satisﬁed:

(1) c1 − c2 = 1. Then P has no interior lattice points.
(2) c1 = c2 = 9/2. Then P is 3∆2.
(3) c1 ≤ c2/2 + 2. Then P has interior lattice points.
 Fig. 3.9

(0, 0) (2, 0)

(2, b − 4)

(1, i + 1)

Fig. 3.10: Lattice polygons re-
alizing 4 ≤ b ≤ 2i + 6

Haase, Nill, Paffenholz: Lattice Polytopes — 45 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

Fig. 3.11: (h
⋆
2, h
⋆
1) of lattice polygons

3.4 The Theorem of Brion

The goal of this ﬁnal section is the celebrated Theorem of BRION. It relates for any
lattice d-polytope the integer point generating functions of all vertex cones of P
to the integer point generating function of the polytope.
Let P be a rational d-dimensional polytope and F a face of P. The tangent cone
of F in P is the cone

TF P := {x | ∃ p ∈ F, ϵ > 0 : p + ϵ(x − p) ∈ P} .

The tangent cone is the common intersection of all supporting half-spaces at F .
Note that the tangent cones are not cones in the usual sense, as their apex is not
in the origin. We call them afﬁne cone if we want to emphasize this. We can use a
point x ∈ F to shift the cone into the origin.

3.4.1 Proposition. The shifted cone TF P − x is dual to the normal cone of F .

Proof. proof missing

We can use the generating series of tangent cones to compute the generating
series of the polytope.

3.4.2 Theorem (Brianchon-Gram). Let P be a rational d-polytope. Then

bGP (t) = ∑

F ≼P(−1)
dim F bGTF P (t) ,

where the sum is over all non-empty faces of P.

Proof. Think of the Laurent polynomial on the left hand side as an inﬁnite Laurent
series that contains all possible monomials, but most coefﬁcients are 0. To prove
this relation we compare coefﬁcients of an arbitrary monomial t m on both sides.
Let f(P) := (f0(P), . . . , fd (P)) be the f -vector of P. We have to distinguish the two
cases m ∈ P and m ̸∈ P.

(1) m ∈ P: Then m ∈ TF P for any face F of P. Hence, the coefﬁcient of t m on the
right hand side is

— 46 — Haase, Nill, Paffenholz: Lattice Polytopes

Ehrhart Theory (preliminary version of December 7, 2012)

∑

F ≼P(−1)
dim F =
 d∑

i=0 (−1)ifi = 1 ,

where the last equality follows from EULER’S relation.

(2) m ̸∈ P: See Figure 3.12. Let S := {F ≼ P | m is beyond F } be the set of faces
such that x violates any supporting hyperplane of F . Then

m ∈ TF P ⇐⇒ F ̸∈ S .

Deﬁne K := {G ≺ P | there is F ∈ S such that G ≺ F } .

Then K is a polyhedral complex. Let f(K) := (f0(K), . . . , fd (K)) be its face
vector. The coefﬁcient of t m is

d∑

i=0 (−1)i(fi(P) − fi(K)) = 1 −
 d∑

i=0 (−1)ifi(K) = 1 − 1 = 0 .
 ⊓⊔

Now recall the map Φ : bL −→ R that we introduced in Section 3.3.1. There we
have only applied it to pointed polyhedral cones. We now want to study this map
also in the case of cones that have a nontrivial lineality space. Recall that for a
cone C the lineality space is deﬁned as lin(C) := C ∩(−C). It is the maximal linear
subspace contained in C.

We start with a simple example that explains the basic idea of our next theo-
rem. Consider the sets

C + := [0, ∞) ⊆ R C − := 3 − C + = (−∞, 3] P := [0, 3] .

C0 is a one-dimensional cone, and P is the intersection of C0 and C −, P = C +∩C −.
We compute the integer point generating function and the image under Φ for C +

and C −:

bGC + (t) = ∑

k≥0 t k bGC − (t) = ∑

k≤3 t k = t 3 ∑

k≤0 t k = t 3 ∑

k≥0 t −k

GC + (t) = Φ(bGC + (t)) = 1

1 − t GC − (t) = Φ(bGC − (t)) = t 3 1

1 − 1
t = −t 4

1 − t

The integer point generating function of P is the ﬁnite geometric series

bGP (t) = GP (t) = 1 − t 4

1 − t = 1 + t + t 2 + t 3 .

We observe that
 GP (t) = GC + (t) + GC − (t) .

Using the construction of the map Φ we can make the following symbolic calcu-
lation
 GP (t) = Φ(bGC + (t)) + Φ(bGC − (t)) = Φ(bGC + (t) + bGC − (t))

= Φ(bGR+P (t)) = Φ(bGR (t)) + Φ(bGP (t))
 m

Fig. 3.12: m ̸∈ P. The com-
plex S is drawn in red.

Haase, Nill, Paffenholz: Lattice Polytopes — 47 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

(0, 0) (1, 0)

(1, 1)(0, 1)
 Fig. 3.13
 This can only hold if Φ(bGR (t)) = 0, i.e. if Φ maps the inﬁnite series ∑
k∈Z t k to 0.
The following proposition shows that this indeed holds in general for cones with
nontrivial lineality space.

3.4.3 Proposition. Let C ⊆ Rd be a polyhedral cone with integer point series bGC (t).
If lineal C ̸= {0} then Φ(bGC ) = 0.

Proof. Let v ∈ lineal(C) − {0}. Then Rv ⊆ C, so that

t v bGC (t) = bGC (t) .

Applying the map Φ gives

t vΦ(bGC (t)) = Φ(bGC (t)) ⇐⇒ (1 − t v)Φ(bGC (t)) = 0 .

v ̸= 0 implies Φ(bGC ) = 0. ⊓⊔

We can apply the observation of this proposition to obtain a very simple formula
for the integer point generating function of a polytope.

3.4.4 Theorem (Brion). Let P be a rational d-polytope. Then

GP (t) = ∑

v vertex of P GTv P (t) .

Proof. Apply the map Φ to both sides of the Brianchon-Gram Identity of The-
orem 3.4.2. The only non-pointed tangent cones are those originating from a
vertex of P, so by Proposition 3.4.3 only the contributions of the vertices are non-
zero on the right hand side. ⊓⊔

3.4.5 Example. Let P be the = 0/1-square in R2. See Figure 3.13. Then

GP  x, y = 1

(1 − x)(1 − y) + x

(1 − 1
x )(1 − y) + y

(1 − x)(1 − 1
y ) + x y

(1 − 1
x )(1 − 1
y )

= 1

(1 − x)(1 − y) + −x 2

(1 − x)(1 − y) + − y 2

(1 − x)(1 − y) + x 2 y 2

(1 − x)(1 − y)

= (1 − x 2)(1 − y 2)

(1 − x)(1 − y) = 1 + x + y + x y

So GP (1, 1) = 1 + 1 + 1 + 1 = 4.

The theorem provides us with a general method to explicitly compute the function
GP (t). We have seen in Corollary 3.3.6 how we can compute the integer point
generating series of a simplicial cone. To use this formula in the Theorem of
Brion we triangulate the polytope P, and compute the generating function of
each simplex in the triangulation (including the lower dimensional ones). We
then sum up the generating functions using the principle of inclusion-exclusion.

3.5 Computing the Ehrhart Polynomial: Barvinok’s
Algorithm

Now we want to discuss an algorithm to compute the number of integral points
in a polytope, due to Barvinok [1] and Barvinok and Pommersheim [4]. If the di-
mension is ﬁxed, then the algorithm is polynomial in the input size. The algorithm
is implemented in the software package LattE [10, 17].

— 48 — Haase, Nill, Paffenholz: Lattice Polytopes

Ehrhart Theory (preliminary version of December 7, 2012)

3.5.1 Basic Version of the Algorithm

The basic idea of the algorithm is to use BRION’s Theorem and a signed decompo-
sition of cones to compute the multivariate rational generating function GP (t) of
the lattice points in a polytope P. Counting then amounts to evaluating GP (t) at
t = 1. This however cannot be done by just inserting 1 in the rational function,
as 1 is always a pole of GP (t). We need tools from complex analysis to evaluate.
You can use GP (t) also to solve linear programs. If you want to maximize over
a functional c ∈ Zd , then you can just substitute t = (zc1 , zc2 , . . . , zcd ). The highest
degree of a monomial in the result is the optimal solution.
To use BRION’s Theorem, we have to compute the integer point generating
functions of all vertex cones. So we need a polynomial method (in ﬁxes dimen-
sion) to compute integer point generating functions of cones. We know how to
do this if the cone is simplicial. The formula is just given by Theorem 3.3.6. To
compute the generating function for general cones we have to break them into
simplicial ones, preferably unimodular, or close to this, as we have to enumerate
lattice points in their fundamental parallelepipeds. However, we may need expo-
nentially many unimodular simplicial cones in a triangulation of a cone. It sufﬁces
to look at dimension 2 to see this. Consider the cone C := conv(e1, e1 + ke2) for
some k ∈ Z>. We need k cones in a unimodular triangulation.
An exponential number of cones necessarily leads to an exponential running
time for our algorithm. If we want a polynomial algorithm we need a better way
to subdivide. So here is the key idea of the algorithm. Instead of just triangulating
cones, we use signed decompositions. It was the achievement of Barvinok [1] to
show that with this method you can get away with a polynomial number of (even
unimodular) cones.
To make this precise, let P be a d-dimensional lattice polytope and v a vertex
of P with tangent cone C ′ := Tv P = v+C for a linear cone C spanned by primitive
rays v1, . . . , vd . We deﬁne the index of the cone C to be

Index(C) := #(Π(v1, . . . , vd ) ∩ Zd )

= | det(v1, . . . , vd )|

= vol Π(v1, . . . , vd )

The cone C is unimodular if and only if Index(C) = 1, so we have to continue
subdividing C as long as Index(C) > 1. Furthermore, if F is a face of C then
Index(F ) ≤ Index(C).
To proceed, we need an important theorem due to Minkowski. It is the funda-
mental theorem in Geometry of Numbers, which is the topic of the next chapter.
We postpone the proof until then (see Theorem 4.1.2), and just state (a slightly
simpliﬁed version of the) theorem.

3.5.1 Theorem. Let K ⊆ Rd be compact convex and centrally-symmetric with
vol K ≥ 2d . Then there exists a ̸= 0 in K ∩ Zd . ⊓⊔

If Index(C) > 1, then K := 1
dp
Index C {∑ λ1 vi | −1 ≤ λi ≤ 1} has volume vol(K) =

2d . Hence, by Minkowski’s Theorem there is w ∈ K ∩ Zd different from 0. Then

w = α1 v1 + α2 v2 + · · · + αd vd for 0 ≤ |αi| ≤ (Index(C))
 1
d .

Unfortunately, the proof of Minkowski’s theorem is not constructive, and it is
generally difﬁcult to compute such a point w. We will deal with one option later
in detail, the LLL-algorithm of Lenstra, Lenstra, and Lovasz. here, we only state
the result. For a full treatment check the next Section 3.5.2.

Haase, Nill, Paffenholz: Lattice Polytopes — 49 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

3.5.2 Proposition (LLL). Let Λ ⊆ Rd be a lattice. Then there is a constant M only
depending on d such that we can ﬁnd a basis v1, . . . , vd of Λ in time O (d 6 log
3 l),
where l is the length of the longest vector among the vi with

∥v1∥ · . . . · ∥vd ∥ ≤ M det Λ

The constant M is quite large. We will prove later that we can take M = 2
 1
2 (d
2).
Given such a short basis we can ﬁnd a shortest lattice vector by a ﬁnite enumera-
tion. This needs the following lemma.

3.5.3 Lemma. Let Λ be a lattice and v1, . . . , vd a short basis given by the previous
proposition, together with the constant M . Let w ∈ Λ\{0} be a shortest lattice vector.
Then
 w =
 d∑

i=1 λi vi with |λi| ≤ pd M .

Proof. Let v1 be shortest among v1, . . . , vd and V the matrix with columns v1, . . . , vd .
Then w = V λ for λ = (λ1, . . . , λd ). Hence, λ = V −1w. By Cramer’s rule all entries
of V −1 are determinants of (d − 1) × (d − 1)-minors of V , divided by det V . So
each entry of V −1 is bounded by

∥v2∥ · . . . · ∥vd ∥ · 1

det V ≤ M

∥v1∥ .

So
 |λ j| ≤ ∑ |wi| M

∥v1∥ ≤ pD∥w∥ M

∥v1∥ ≤ pd M (∥w∥ ≤ ∥v1∥) ⊓⊔

Hence, to ﬁnd a shortest lattice vector we compute a short basis and enumerate
all N := (2pd M )d possibilities for the coefﬁcients of the shortest vector.

3.5.4 Lemma. Suppose v1, . . . , vd is a basis of the lattice Λ such that

∥v1∥ · . . . · ∥vd ∥ ≤ M det Λ ,

and let u ∈ Λ \ {0} be a shortest vector. Then u = ∑d
i=1 λi vi with |λi| ≤ pd M In
particular, there are less than N = (
pd M )d many candidates for u.

Proof. Assume v1 is shortest among the vi. Denote the matrix with columns vi by
V . Then λ = V −1u. The entries of V −1 are (d − 1) × (d − 1)-minors of V , divided
by det Λ. Hence, they are bounded in absolute value by ∥v2∥ · . . . · ∥vd ∥/ det Λ ≤
M /∥v1∥.
Therefore, |λ j| ≤ ∑d
i=1 |ui| M /∥v1∥ ≤ pd ∥u∥ M /∥v1∥ ≤ pd M for all j as
∥u∥ ≤ ∥v1∥. ⊓⊔

This leads to the following theorem.

3.5.5 Theorem. In ﬁxed dimension d we can ﬁnd w ∈ Π0 ∩ Zd , w ̸= 0 in time
polynomial in log
3 max(∥vi∥).

By replacing w with −w if necessary we can assume that w, v1, . . . , vd lie in a
common half-space, and that w is primitive. By construction, |λi| ≤ (Index C)
− 1
d .
We deﬁne new cones

C j := cone(v1, . . . , vj−1, w, vj+1, . . . , vd ) for 1 ≤ j ≤ d .

— 50 — Haase, Nill, Paffenholz: Lattice Polytopes

Ehrhart Theory (preliminary version of December 7, 2012)

We compute the index of these new cones:

Index C j = | det(v1, . . . , vj−1, w, vj+1, . . . , vd )|

=
 d∑

k=1 |λk| · | det(v1, . . . , vj−1, vk, vj+1, . . . , vd )|

= |λ j| · | det(v1, . . . , vd )|

= |λ j|(Index C) ≤ (Index C)
− 1
d (Index C)

= (Index C)
 d−1
d

and the right hand side is strictly less than Index C) if Index C ≥ 2. We deﬁne a
corresponding sign function to make a signed subdivision of C with the cones C j.

ϵi :=
 




 0 if dim C j < d
1 if det(v1, . . . , vd ) = det(v1, . . . , vj−1, w, vj+1, . . . , vd )
−1 otherwise.

We can use this decomposition to write the integer point generating series as a
signed sum via

bGC (t) =
 d∑

j=1 ϵ j bGC (t) + lower dimensional contributions.

In this decomposition we have

◃ at most d d-dimensional cones,
◃ at most 2d d cones of any dimension.

We repeat this decomposition for each cone of index ≥ 2. After n steps of this

procedure, any cone in the decomposition has index at most (Index C)

• d−1
d −n . For
a unimodular triangulation we want this to be less than 2 (recall that the index
is integral, so it must be 1).

(Index C)

• d−1
d −n !
< 2 for unimodular decomposition

⇐⇒  d − 1

d
 n lg2(Index C) < lg2 2 = 1

⇐⇒ n lg2
  d − 1

d
  + lg2 lg2(Index C) < 0

⇐⇒ lg2 lg2(Index C) < n lg2
  d

d − 1
 

choose n >
 



 lg2 lg2(Index C)

lg2  d
d−1
 
 



 + 1 = O (d lg2 lg2 Index C).

Then (Index C)

• d−1
d −n < 2, so all indices in the decomposition are 1. In this de-
composition we have

(d2d )n = 2nd lg2 d ≤ 2M d 2 lg2 d lg2 lg2 Index C

= (lg2 Index C)M d 2 lg2 d

Haase, Nill, Paffenholz: Lattice Polytopes — 51 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

Algorithm 3.5.1: Barvinok’s Algorithm: Original Version

Input: A polyhedron P = {x | Ax ≤ b} with vertices v1, . . . , vk.
Output: The integer point generating function for P as

GP (t) = ∑

i∈I ϵi t ai

(1 − t vi1 ) · · · (1 − t viki )

for ϵi ∈ {−1, 1}, ai, vi j ∈ Zd .
for i ← 1 to k do
Compute vertex cone Ci at vertex vi;
Triangulate Ci into ki simplicial cones Ci j;
for j ← 1 to ki do
do a signed decomposition of Ci j into unimodular cones C k
i j.;

compute the unique interior point ak
i j in C k
i j;
endfor
sum up the contributions using the inclusion-exclusion principle;
endfor
sum up the contributions using the inclusion-exclusion principle;

= (lg2 Index C)
O (d 2 lg2 d).

cones. Hence, in ﬁxed dimension, the number of cones is bounded by a poly-
nomial in lg2 Index C, which is the input size. We summarize the algorithm in
Algorithm 3.5.1 and the following theorem.

3.5.6 Theorem. Let d ∈ Z> be ﬁxed. Then there is a polynomial time algorithm
that computes the integer point generating function GP (t) in the form

GP (t) := ∑

i∈I ϵi t ai

(1 − t vi1 ) · · · (1 − t vid ) ,

where ϵi ∈ {−1, 1}, a ∈ Zd , vi j ∈ Zd − {0} for all i, j, for any d-dimensional
polyhedron P given in its exterior description.

We ﬁnally need to discuss how we can evaluate our generating function at 1.

◃ Evaluate at t = (1, . . . , 1): t u
∏(1−t v j )
Make univariate: t j 7→ zλ j for some λ = (λ1, . . . , λd ). New exponent in de-
nominator is z〈vj ,λ〉 (choose λ such that d j := 〈vj, λ〉 ̸= 0 ∀vj)

⇝ this gives zn
∏
 j (1−zd j ) at z=1
←− replace z = x + 1 ⇝ expansion at x = 0

3.5.2 A versatile tool: LLL

Here, we describe an efﬁcient way to construct a lattices basis sharing several
nice properties from any given lattice basis. The algorithm was ﬁrst described by
Arjen Lenstra, Hendrik Lenstra and László Lovász in 1982 [19], and it is known
as the LLL-algorithm.

3.5.7 Proposition. Let Λ ⊆ Rd be a lattice. Then there is a vector v ∈ Λ \ {0} such
that
 ∥v∥ ≤ pd(det Λ)
1/d .

Proof. Follows from Minkowski’s Theorem 4.1.2 . proof missing ⊓⊔

— 52 — Haase, Nill, Paffenholz: Lattice Polytopes

Ehrhart Theory (preliminary version of December 7, 2012)

We ﬁx some notation. Let Λ ⊆ Rd be a lattice with a basis v1, v2, . . . , vd ∈ Rd .
The order of the basis vectors in important for the following considerations. We
consider the increasing chain of subspaces

V0 := {0} Vk := lin(v1, . . . , vk) for 1 ≤ k ≤ d .

We deﬁne the induces lattices Λk := Λ ∩ Vk and the invariant

D(v1, . . . , vd ) :=
 d∏

j=1 det Λ j .

3.5.8 Lemma. Let Λ ⊆ Rd be a lattice with basis v1, . . . , vd . Let λ1 := minu∈Λ\{0}(∥u∥).
Then
 D(v1, . . . , vd ) ≥ λ(d
2) d∏

i=1 i−i/2 .

Proof. Clearly λ1 ≤ minu∈Λ j \{0}(∥u∥) for all 1 ≤ j ≤ d. From Proposition 3.5.7 we
conclude
 det Λ j ≥ ∥v∥ j
p j j ≥ λ j
p j j .

Multiplying the last equation for all 1 ≤ j ≤ d gives the lemma. ⊓⊔

Let πk := Rd → Vk be the orthogonal projection onto Vk. We deﬁne

wk := vk − πk−1(vk)

for 1 ≤ k ≤ d. This is the GRAM-SCHMIDT-orthogonalization of v1, . . . , vd . The
vectors w1, . . . , wd are pairwise orthogonal, so

det Λ =
 d∏

i=1 wi . and det Λk =
 k∏

i=1 wi .

By construction, we can ﬁnd coefﬁcients λi j ∈ R, 1 ≤ j < i ≤ d such that

vi = wi +
 i−1∑

j=1 λi j w j . (3.5.1)

3.5.9 Deﬁnition ((weakly) reduced basis). The basis v1, . . . , vd of Λ is weakly
reduced if |λi j| ≤ 1/2 for all 1 ≤ j < i ≤ d.
It is reduced if in addition it satisﬁes

d(
,2)(vk, Vk−1) ≤ 4

3 d(
,2)(vk+1, Vk) (3.5.2)

for 1 ≤ k ≤ d − 1.

Geometrically a basis is reduced if the vector vj+1 is not much closer to the sub-
space spanned by the ﬁrst k − 1 basis vectors than the vector vj. For an orthogo-
nal basis of the vector space we could ﬁnd a permutation such that the distances
strictly increase. The condition for a weakly reduced basis is a relaxation of this.
We prove the following theorem.

Haase, Nill, Paffenholz: Lattice Polytopes — 53 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

3.5.10 Theorem (Lenstra, Lenstra, Lovász, 1982). Any lattice basis can be
transformed into a reduced basis in polynomial time.

We need some preparations for the proof of this theorem. Consider the represen-
tation of our given basis in (3.5.1). Assume that for some pair of indices l < k the
coefﬁcient λkl is larger than 1/2. Then there is a unique µkl ∈ R and akl ∈ Z such
that
 |µkl | ≤ 1/2 λkl = akl + µkl .

We replace vk by vi − akl vl . This leaves the subspaces Vl , 0 ≤ j ≤ n and the
GRAM-SCHMIDT orthogonalization w1, . . . , wn invariant, and the sets

v1, . . . , vj

are still a basis of the lattice Λ j. So the only coefﬁcients in the representa-
tion (3.5.1) that might change are those involved in the representation of vk,

vk − akl vl = wk +
 k−1∑

j=1 λk j w j − akl vl .

The vector vl is in the subspace Vl , so it has a representation

vl =
 l∑

j=1 η j w j .

vl − wl ∈ Vl−1, so ηl = 1. This implies that

vk − akl vl = wk +
 l∑

j=1(λk j − η j)w j +
 k−1∑

j=l+1 λk j w j ,

and |λkl − ηl | = |λkl − akl | ≤ 1/2. So the new coefﬁcient is weakly reduced, and to
achieve this we apart from λkl only had to change coefﬁcients λk j for j < k. So
always starting with the largest index k that has a coefﬁcient λkl such that |λkl | >

1/2 gives us a weakly reduced basis. There are  d
2 coefﬁcients, and reducing λkl
with the above procedure we have to touch at most l ≤ d other coefﬁcients,
so this process terminates after at most O (d 3) steps. We summarize this in the
following proposition.

3.5.11 Proposition. Any lattice Λ has a weakly reduced basis. More precisely, we
can transform any basis into a weakly reduced one in time O (d 3). ⊓⊔

We can use the construction of a weakly reduced basis as an intermediate step
for a reduced basis. If in a weakly reduced basis a pair of vectors vj, vj+1 violates
the condition given in (3.5.2), then we can ﬁx this by exchanging vk and vk+1 in
the basis. However, the new basis might not be weakly reduced anymore, so we
make it weakly reduced with the previous algorithm. We repeat these two steps
until we reach a reduced basis.
The algorithm clearly outputs a reduced basis if it terminates. So to prove
Theorem 3.5.10 we only have to show that it terminates after an polynomial
number of steps. We use the invariant D(v1, . . . , vd ) := ∏d
j=1 det Λ j introduced
above and show that each iteration of the algorithm reduces it by a factor of p
3/2.
As Proposition 3.5.7 gives a lower bound only depending on the dimension of the
lattice, this will prove the theorem.

— 54 — Haase, Nill, Paffenholz: Lattice Polytopes

Ehrhart Theory (preliminary version of December 7, 2012)

Algorithm 3.5.2: Weakly Reduced Basis

Input: A lattice basis v1, . . . , vd .
Output: A weakly reduced lattice basis v′
1, . . . , v′
d
Compute the GRAM-SCHMIDT orthogonalization w1, . . . , wd ;
Compute coefﬁcients λi j, 1 ≤ j < i ≤ d such that vi = ∑i
j=1 λi j w j;
while Basis not reduced do
Let k be the largest index such that |λkl | > 1/2;
Let µkl ∈ R, akl ∈ Z such that |µkl | < 1/2, λkl = µkl + akl ;
Determine η j, 1 ≤ j ≤ l with vl = ∑ η j w j;
Replace λk j ← λk j − η j for 1 ≤ j ≤ l;
endw
return v1, . . . , vd ;

Let us determine the change in D := D(v1, . . . , vd ) after one iteration. Making a
basis weakly reduced does not change the subspaces Vi and the lattices Λi, hence
it also does not change D. So assume that vj and vj+1 satisfy

d(
,2)(vk, Vk−1) > 4

3 d(
,2)(vk+1, Vk)

and let v′
1, . . . , v′
d be the basis obtained by exchanging vj and vj+1, i.e.

v′
j+1 := vj v′
j := vj+1 v′
i := vi for i ̸= j, j + 1 .

Let w′
1, . . . , w′
d be its GRAM-SCHMIDT orthogonalization and V ′
i , Λ′
i be the new
subspaces and lattices, 1 ≤ i ≤ d. Then

V ′
i = Vi Λ′
i = Λi for i ̸= j ,

while
 V ′
j := lin(v′
1, . . . , v′
j−1, v′
j) = lin(v1, . . . , vj−1, vj+1) .

Consequently, the vectors w j and w′
j satisfy

∥w′
j∥ <
 p
3

2 ∥w j∥

while for all other i we have w′
i = wi. Hence

det Λ′
j <
 p
3

2 det Λi ,

so also
 D(v′
1, . . . , v′
d ) < D(v1, . . . , vd ) .

Together with the lower bound for D(v1, . . . , vd ) in Proposition 3.5.8 this proves
Theorem 3.5.10. We collect some nice consequences of a reduced basis.

3.5.12 Proposition. Let Λ ⊆ Rd be a lattice with reduced basis v1, . . . , vd . Let
w1, . . . , wd be its GRAM-SCHMIDT orthogonalization. Then

∥w j∥2 ≤ ∥vj∥2 ≤ ∥w j∥2 + 1

4
 j−1∑

i=1 ∥wi∥2 for 1 ≤ j ≤ d

Haase, Nill, Paffenholz: Lattice Polytopes — 55 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

Algorithm 3.5.3: LLL

Input: A lattice basis V := {v1, . . . , vd }.
Output: A reduced lattice basis v′
1, . . . , v′
d
Make V weakly reduced (Algorithm 3.5.2);
while V not reduced do
Find a pair vj, vj+1 that violates (3.5.2) and exchange the two vectors;
Make the basis weakly reduced;
endw
return V ;

∥w j∥2 ≥ 1

2 ∥w j−1∥2 for 2 ≤ j ≤ d .

Proof. By the deﬁnition of a weakly reduced basis we have

vj = w j +
 j−1∑

k=1 λ jkwk

for coefﬁcients −1/2 ≤ λk j ≤ 1/2. Taking the norm and using that the scalar prod-
uct of any two of the wi’s is 0 implies

∥vj∥2 = ∥w j∥2 +
 j−1∑

k=1 λ2
jk∥wk∥2 ≤ ∥w j∥2 + 1

4
 j−1∑

k=1 ∥wk∥2 .

This proves the ﬁrst inequality. Further, we have

d((, v) j, Vj−1)
2 = ∥w j∥

d((, v) j+1, Vj−1)
2 = ∥w j+1∥2 + λ j+1, j∥w j∥2 ≤ ∥w j+1∥2 + 1

4 ∥w j∥ .

By assumption
 d((, v) j+1, Vj−1)
2 ≥ 3

4 d((, v) j, Vj−1)
2

so
 ∥w j+1∥2 + 1

4 ∥w j∥ ≥ 3

4 ∥w j∥2

The second inequality follows. ⊓⊔

3.5.13 Corollary. Let Λ ⊆ Rd be a lattice with reduced basis v1, . . . , vd . Then

d∏

i=1 ∥vi∥ ≤ 2
 1
2 (d
2) det Λ .

Proof. We compute

∥vj∥2 ≤ ∥w j∥2 + 1

4
 j−1∑

k=1 ∥wk∥2 ≤ ∥w j∥2

1 + 1

4
 j−1∑

k=1 2 j−k!
 ≤ 2 j−1∥w j∥2

and
 — 56 — Haase, Nill, Paffenholz: Lattice Polytopes

Ehrhart Theory (preliminary version of December 7, 2012)

d∏

j=1 ∥vj∥ ≤
 d∏

j=1 2 j−1∥vw j∥2

= 2
 1
2 (d
2) ∏ j = 1d ∥w j∥ ≤ 2
 1
2 (d
2) det Λ . ⊓⊔

3.5.14 Proposition. Let Λ ⊆ Rd be a lattice with a reduced basis v1, . . . , vd . Let
λ1 := mina∈Λ−{0} ∥a∥ be the ﬁrst successive minimum of the lattice and assume we

have a vector x ∈ Λ with ∥x∥ ≤ αλ1 for some α ≥ 1 and x = ∑d
i=1 ηi vi. Then

|ηi| ≤ 2
 d−1
2  3

2
 d−i α ≤ 3d α for 1 ≤ i ≤ d .

Proof. proof missing ⊓⊔

3.6 Problems

3.1 The goal of this exercise is to give a proof of Proposition 3.3.3.

(1) Show that the set Lsum of summable Laurent series is an L-submodule of ˆL,
i.e. show that for f ∈ L and g, h ∈ Lsum also f · g and g + h are summable.
(2) Prove that this turns Φ into a homomorphism of L-modules, i.e. show that
Φ( f · g) = f Φ(g) and Φ( f + g) = Φ( f ) + Φ(g).

3.2 Prove that there is a natural homomorphism from summable series to ratio-
nal functions
 Φ : bL −→ R := k(x1, . . . , xd ) ,

mapping bG to f /g if g bG = f in bL.

3.3 Let P be a lattice polytope with Ehrhart polynomial ehrP (t). Compute the
Ehrhart polynomial of the bipyramid over P.

3.4 Compute the Ehrhart polynomial of the cross polytope.

3.5 A simplex which is unimodularly equivalent to the standard simplex is called
unimodular. A triangulation is unimodular if all its simplices are.

(1) For a k-dimensional unimodular simplex ∆ and t ∈ Z≥1 show that

|Zk ∩ relint(t∆)| = t − 1

k
  .

(2) Suppose P admits a unimodular triangulation T with f0(T) vertices, f1(T)
edges, . . . , fd (T) d-simplices. Show that

ehrP (t) =
 d∑

k=0 fk(T) t − 1

k
  .

(3) Conclude that any two unimodular triangulations have the same f -vector
( f0, . . . , fd ) .

3.6 Let P be a lattice d-polytope. Show that the leading coefﬁcient of the Ehrhart
polynomial ehrP (t) equals the volume vol P of the polytope.

3.7 Prove Corollary 3.3.21.

Haase, Nill, Paffenholz: Lattice Polytopes — 57 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

3.8 Prove Lemma 3.3.31.

3.9 Prove Theorem 3.3.24.

3.10 For integers p,q with gcd(p, q) = 1 deﬁne the tetrahedron

∆pq = conv Ł 0 1 0 1
0 0 1 p
0 0 0 q
 Ÿ .

(1) Argue that its vertices are its only lattice points. (White proved a converse:
every lattice tetrahedron with only four lattice points is unimodularly equiv-
alent to a ∆pq.)
(2) Compute the Ehrhart polynomial and the h
⋆-polynomial of ∆pq.
(3) For which parameters are ∆pq and ∆p′q′ unimodularly equivalent?

3.11 A simplex which is unimodularly equivalent to the standard simplex is
called unimodular. A triangulation is unimodular if all its simplices are.
For a k-dimensional unimodular simplex ∆ and t ∈ Z≥1 show that

|Zk ∩ relint(t∆)| = t − 1

k
  .

Suppose P admits a unimodular triangulation T with f0(T) vertices, f1(T)
edges, . . . , fd (T) d-simplices. Show that

ehrP (t) =
 d∑

k=0 fk(T) t − 1

k
  .

Conclude that any two unimodular triangulations have the same f -vector
( f0, . . . , fd ) .

3.12 Determine the Ehrhart polynomial ehr⋄d (t) of the d-dimensional cross-
polytope ⋄d = conv[±e1, . . . , ±ed ] .

3.13 Let P be a d-dimensional lattice polytope in Rd . We deﬁne the lattice pyra-
mid over P as
 Pyr(P) := conv(P × {0}, ed+1) ⊆ Rd+1,

where e1, . . . , ed+1 is the standard basis of Rd+1. Show that h
⋆
Pyr(P) = h
⋆
P .

3.14 Let m ∈ Z≥1. Use Exercise 3.13 to show that

fm(k) :=
 k∑

j=1 jm

is a polynomial in k. What is its degree and leading coefﬁcient?

3.15 Let P be a d-dimensional lattice polytope with Ehrhart polynomial ∑d
k=0 ck t k.
Show that
 cd−1 = 1

2 vol(∂ P).

Here, vol(∂ P) denotes the surface area of P, namely,

vol(∂ P) := ∑

F ∈F(P) vol(F ),

— 58 — Haase, Nill, Paffenholz: Lattice Polytopes

Ehrhart Theory (preliminary version of December 7, 2012)

where F(P) is the set of facets of P and vol(F ) denotes the (non-normalized) vol-
ume with respect to the lattice aff(F )∩Zd . For instance, note that vol(conv((1, 0), (0, 1)))
equals 1 and not p
2. Hence,

vol(∂ conv((1, 0), (0, 1), (−1, 0), (0, −1))) = 4 .

3.16 Let P be a d-dimensional lattice polytope. Show that

codeg(P) := d + 1 − deg(P) = min{k ∈ N≥1 : int (kP) ∩ Zd ̸= ;},

and h
∗
d (P) = | int ( codeg(P)P) ∩ Zd |.

(Hint: Use reciprocity.)

3.17 Calculate the h
∗-polynomial of an empty 3-dimensional lattice polytope P
with a vertices and of normalized volume b. Here empty means that any lattice
point in P is a vertex of P. Deduce the h
∗-polynomials of the tetrahedra ∆pq of
Exercise 2.2. Check that you get the same solution for the Ehrhart polynomial as
before :-)

3.18 Let Q, P be lattice polytopes with Q ⊆ P. Show that there exists a triangu-
lation of P that restricts to a triangulation of Q.
(Hint: Let V denote the set of vertices. Choose ﬁrst a generic regular triangu-
lation w : V(Q) → R, leading to linear functions lσ on simplices σ of the trian-
gulation. Now, choose generic values of w on V(P)\V(Q) such that w(v) > lσ(v)
for all σ in the triangulation of Q and vertices v ∈ V(P)\V(Q).)

3.19 Let Q, P be lattice polytopes with Q ⊆ P. Show Stanley’s monotonicity the-
orem: h
∗
Q ≤ h
∗
P coefﬁcientwise.

(Hint: Choose a triangulation as in the previous exercise.)

3.20 Prove Proposition 3.3.33.

3.21 Let P be a lattice polygon. Show that P has no interior lattice points if and
only if P is unimodular equivalent to 2∆2 or it is unimodularly equivalent to
conv((0, 0), (a, 0), (0, 1), (0, b)) for some a, b ≥ 0.

3.22 Apply Brion’s identity to

P := conv  0 2 2 3
1 −1 2 0
 

and verify that both rational functions coincide (you may want to use a computer
for this).

Haase, Nill, Paffenholz: Lattice Polytopes — 59 —

text on this page — prevents rotating 4
Geometry of Numbers

Geometry of numbers deals with the relation between two objects: convex bodies
on the one hand, and lattices one the other hand. A typical question in this area
is whether and how the volume and the number of lattice points of convex body
are related.
The term “geometry of numbers” was coined by Minkowski who used con-
vex geometric methods, in particular his fundamental theorem 4.1.2, in order to
bound class numbers in algebraic number theory. In the 20th century geometry
of numbers has grown into an established ﬁeld of research with connections into
many branches of mathematics.
While most of the theory treats general convex bodies, in these notes we will
focus on those tools which we need to prove results that apply only to lattice
polytopes.

4.1 Minkowski’s Theorems

In this section, we prove the basic Theorem 4.1.2 which was the starting point
of the theory. We conclude with some applications and extensions which we will
need in the next sections. Throughout, Λ ⊆ Rd is a lattice of rank d (the reader
may think of Zd ).

4.1.1 Theorem (Blichfeldt, 1914). Let S ⊆ Rd be a (Lebesgue measurable) set
with vol S > det Λ. Then there are p, q ∈ S, p ̸= q, such that p − q ∈ Λ.

Proof. Choose a fundamental parallelepiped Π := Π(Λ) of Λ. Then det Λ = vol Π.
For any x ∈ Λ let
 Sx := { y ∈ Π | x + y ∈ S} = Π ∩ (S − x)
 x
 S

x + S

0
 Fig. 4.1

61

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

0

Fig. 4.2: A triangle in the plane to-
gether with two scaled copies with
scaling factors λ1 and λ2.
 The sets (x + Π) ∩ S cover S without overlap (by Corollary 1.3.11). Hence,

vol S = ∑

x∈Λ vol ((x + Π) ∩ S) = ∑

x∈Λ vol Sx .

Assume that Sx ∩ S y = ∅ for all x, y ∈ Λ, x ̸= y. Then

vol
   ⋃

x∈Λ Sx
 !
 = ∑

x∈Λ vol Sx = vol S > vol Π .

This is a contradiction to ⋃
x∈Λ Sx ⊆ Π. Hence, there exist x, y ∈ Λ, x ̸= y, such
that Sx ∩ S y ̸= ∅. Let a be the point in the intersection and p := a + x, q := a + y.
Then p, q ∈ S and p − q = x − y is a non-zero lattice point. ⊓⊔

4.1.2 Theorem (Minkowski’s First Theorem, 1896). Let K ⊆ Rd be convex and
centrally-symmetric with vol K > 2d det Λ. Then there exists a ̸= 0 in K ∩ Λ.
If K is also compact, then it sufﬁces to assume vol K ≥ 2d det Λ.

Proof. Let T := 1
2 K. Then vol T = vol K
2d > det Λ. Hence, by Blichfeldt’s Theo-
rem 4.1.1, there are p, q ∈ K such that

x := 1

2 p − 1

2 q = 1

2 (p + (−q))

is a non-zero lattice point. By central symmetry of K, −q ∈ K, so x ∈ K by
convexity of K.
Let K be compact and vol K = 2d det Λ. For any k ≥ 1, applying the previous
argument yields a non-zero lattice point xk ∈ k+1
k K ⊆ 2K. Compactness of 2K
yields the existence of a converging subsequence (xki )i≥1. Since Λ is discrete, this
sequence gets stationary, i.e., xki =: x for all i ≥ i0. In particular, 0 ̸= x ∈ Λ. On

the other hand, x = limi→∞ ki
ki +1 xki ∈ K. ⊓⊔

Centrally-symmetric convex bodies with the origin as their only interior lattice
point which have maximal volume 2d det(Λ) are also called extremal bodies.
Minkowski’s theorem does not tell us how to ﬁnd the integral point, it just tells us
it exists. There are polynomial time algorithms to explicitly ﬁnd such a point, but
only for a much larger volume bound. See Section 3.5.2 on the LLL-Algorithm for
a method. Finding a short lattice vector is a very important problem in integer
optimization and in cryptography, see e.g. [23, 22, 14]

4.1.3 Deﬁnition (Successive Minima). Let K ∈ C. For 1 ≤ k ≤ d we deﬁne the
k-th successive minimum of K to be the number

λk := inf
λ>0
{dim lin(λK ∩ Λ) ≥ k}.

Then λ1 ≤ λ2 ≤ · · · ≤ λd .

Note that λ1 > 0 as Λ is discrete. The following corollary is equivalent to 4.1.2.

4.1.4 Corollary. Let K ∈ C. Then

λd
1 vol K ≤ 2d det Λ.

It is non-trivial to sharpen this bound in the following way.

— 62 — Haase, Nill, Paffenholz: Lattice Polytopes

Geometry of Numbers (preliminary version of December 7, 2012)

4.1.5 Theorem (Minkowski’s Second Theorem, 1896). Let K ∈ C. Then

1

d! · 2d det Λ ≤ λ1 · · · λd vol K ≤ 2d det Λ.

We will not prove this much stronger theorem here. We will, however need a
reﬁnement of Minkowski’s ﬁrst Theorem due to van der Corput (Theorem 4.1.7
below). For this we have to extend Theorem 4.1.1 ﬁrst.

4.1.6 Theorem (Generalized Blichfeldt’s theorem). Let S ⊆ Rd be a (Lebesgue
measurable) set with vol(S) > m det(Λ) for a positive integer m. Then there exist
m + 1 distinct points p1, . . . , pm+1 ∈ S such that pi − p j ∈ Λ for all i, j.

Proof. By considering a sufﬁciently large subset, we may assume that S is bounded.
We deﬁne Π and Sx (for x ∈ Λ) as in the proof of Theorem 4.1.1. Let idx be the
indicator function on Sx (i.e., it evaluates to one on Sx and zero elsewhere). We
deﬁne the function f := ∑

x∈Λ idx .

Note that this is well-deﬁned, since Sx ̸= ; for only ﬁnitely many x ∈ Λ. Hence,
∫

Π f d x = ∑

x∈Λ
 ∫

Π idx d x = ∑

x∈Λ vol(Sx )

= ∑

x∈Λ vol(S ∩ (x + Π)) = vol(S).

Since ∫

Π 1 d x = vol(Π) = det(Λ), our assumption yields that there has to exist
some point y ∈ Π with f ( y) > m. Since f only evaluates to integers, we get
f ( y) ≥ m + 1. In particular, there exist x1, . . . , xm+1 ∈ Λ such that y ∈ Sx1 ∩ · · · ∩
Sxm+1 . Therefore, deﬁning pi := y + xi ∈ S for i = 1, . . . , m + 1 yields m + 1 points
which have the desired properties. ⊓⊔

4.1.7 Theorem (van der Corput, 1935). Let K ⊆ Rd be a centrally symmetric
convex set with vol(K) > m2d det(Λ) for a positive integer m. Then there exist m
distinct pairs of non-zero lattice points ±x1, . . . , ±xm in K.

Proof. Let T := 1
2 K. Then vol T = vol K
2d > m det Λ. Hence, by Blichfeldt’s Theo-
rem 4.1.6, there are m + 1 distinct points p1, . . . , pm+1 ∈ T such that pi − p j ∈ Λ
for all i, j. Choose xi := pi − pm+1 for i = 1, . . . , m as the desired lattice points.
Note that xi = pi + (−pm+1) ∈ T + T = K. ⊓⊔

4.1.8 Corollary. Let K ⊆ Rd be a centrally symmetric convex set. Then

vol(K) ≤ (| int K ∩ Zd | + 1) 2d−1.

Let us ﬁnish this section with another of Minkowski’s gems.

4.1.9 Theorem (Minkowski, 1910). Let K ⊆ Rd be a centrally symmetric convex
set with int (K) ∩ Λ = {0}. Then |K ∩ Λ| ≤ 3d .

Proof. We may choose Λ = Zd . Assume the statement fails. We consider the map
ϕ : Zd → (Z/3Z)d given by assigning each coordinate its congruence class
modulo 3. This is a homomorphism (so ϕ(x ± y) = ϕ(x) ± ϕ( y)). Note that
(Z/3Z)d has 3d elements. Hence, by the pigeon hole principle there exist two
distinct lattice points x, y ∈ Zd with ϕ(x) = ϕ( y). Therefore, ϕ(x − y) = 0, thus

Haase, Nill, Paffenholz: Lattice Polytopes — 63 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

p := x − y

3 ∈ Λ

Since K is centrally-symmetric, 0 ̸= p = x
3 + − y
3 ∈ 2
3 K, a contradiction. ⊓⊔

Recently, it was shown that up to unimodular transformations the standard cube
[−1, 1]d is the only centrally-symmetric lattice polytope with int (K) ∩ Λ = {0}
and |K ∩ Λ| = 3d [12].

4.2 Lattice packing and covering

In this section, we will give a short discussion about lattices and metric geometry
(mainly following [Barvinok2008]). This is the ﬁrst point in the book where Λ
really is meant to be a (non-standard) lattice in Rd . An interesting geometric
application can be found in the next section.

Usually, when dealing with lattice polytopes we start with an abstract lattice
Λ ∼= Zd and associate an abstract vector space Λ ⊗Z R ∼= Rd with the volume form
which evaluates as 1/d! on a fundamental domain of Λ. In particular, note that
the ’length’ of a vector is not well-deﬁned. In general, we deﬁne the dual lattice
as Λ⋆ := HomZ(Λ, Z)

and the dual vector space as

(Λ ⊗Z R)
⋆ := HomR(Λ ⊗Z R, R).

Note that the dual lattice naturally sits inside of the dual vector space. While these
deﬁnitions are abstract, they stress the point that in general it is not necessary and
often misleading to identify dual spaces or lattices.
In contrast, in lattice theory the viewpoint is opposite to ours. The starting
point is an euclidean vector space, say, Rd with the usual scalar product 〈 ·, · 〉.
Now, the choice of the embedded lattice matters! For instance, their determinants
differ. In this section, we will follow this convention.
So, let Λ ⊆ Rd be a lattice of full rank, and we assume that we have a scalar
product 〈 ·, · 〉. Now, we can identify Rd and (Rd )
⋆:

Rd ∼= (Rd )
⋆, x → 〈 ·, x 〉.

In particular, we get under this identiﬁcation

Λ⋆ = {x ∈ Rd : 〈 x, y 〉 ∈ Z ∀ y ∈ Λ} ⊆ Rd .

Note that while Λ⋆⋆ = Λ, it may happen that Λ⋆ ̸= Λ. For instance, if Λ = Zd /2,
then Λ⋆ = 2Zd .

Here is the ﬁrst important deﬁnition from lattice theory. Using the notion of
successive minima we can deﬁne the packing radius of a lattice.

4.2.1 Deﬁnition. The packing radius of Λ is deﬁned as

ϱ(Λ) := 1

2 λ1(B1(0), Λ).

Thus, the packing radius equals one half of the length of a shortest lattice vector.
In other words, the packing radius is the largest r such that Rd is ﬁlled by con-
gruent non-overlapping balls of radius r centered at the lattice points. Here is the
dual notion to successive minima.

— 64 — Haase, Nill, Paffenholz: Lattice Polytopes

Geometry of Numbers (preliminary version of December 7, 2012)

4.2.2 Deﬁnition. For a convex body K ⊆ Rd , we deﬁne µk(K, Λ) as the inﬁmum
over all τ > 0 such that
 (Λ + τK) ∩ L ̸= ;

for every (d − k)-dimensional afﬁne subspace L ⊆ Rd . An important instance is
the covering radius, which is deﬁned as

µ(Λ) := µd (B1(0), Λ) .

In other words, the covering radius equals the smallest r such that Rd is covered
by congruent balls of radius r centered at the lattice points. Equivalently, µ(Λ)
equals the largest possible distance of a point in Rd from the closest lattice point
nearby.
In the following, we are interested in relations between the following invari-
ants: det(Λ), det(Λ⋆), ϱ(Λ), ϱ(Λ⋆), µ(Λ), µ(Λ⋆). Let us start with an observation,
which we leave to the reader as as an exercise.

4.2.3 Lemma. det(Λ) det(Λ⋆) = 1 .

Our ﬁrst result shows that if we ﬁx the determinant, then the packing density
cannot be too large.

4.2.4 Proposition. The covering radius satisﬁes ϱ(Λ) ≤ 1
2 pd det(Λ)
1/d .

Proof. Our task is to determine a radius for a ball centered at the origin that
guarantees that the ball contains another (non-zero) lattice point. We want to
use Minkowski’s theorem for this. Clearly,

− r
pd , r
pd
 d ⊆ Br (0)

so that
 vol Br (0) > 2d r d
pd d .

If we choose r := pd det(Λ)
1/d , then

vol Br (0) ≥ 2d det(Λ) .

So by Minkowski’s Theorem 4.1.2 there is a non-zero lattice point in this ball.
This proves the claim. ⊓⊔

Combining with Lemma 4.2.3 this yields:

4.2.5 Corollary.
 ϱ(Λ) ϱ(Λ⋆) ≤ d

4 . ⊓⊔

The main result of this section are the following bounds:

4.2.6 Theorem.
 1

4 ≤ µ(Λ) ϱ(Λ⋆) ≤ 1

4
 √
√
√
√ d∑

k=1 k2 ≤ d
 3
2

4 .

Haase, Nill, Paffenholz: Lattice Polytopes — 65 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

u
⊥

π(x)

x v

w

w + ( y − v)
≤ ∥u∥
2

Fig. 4.3
 The proof of the middle inequality is inductive and relies on the following lemma.

4.2.7 Lemma. Let 0 ̸= u ∈ Λ be primitive. We consider the orthogonal projection

π : Rd → u
⊥ ∼= Rd−1

x 7→ x − 〈x, u〉

〈u, u〉 u

Then

(1) Λ1 := π(Λ) is a lattice of rank d − 1.
(2) Let Λ∗
1 ⊆ u
⊥ be the dual lattice. Then Λ∗
1 ⊆ Λ∗.
(3)
 µ(Λ)
2 ≤ 1

4 ∥u∥2 + µ(Λ1)
2.

Proof. (1) There exists a lattice basis u1, u2, . . . , ud of Λ such that u1 = u. There-
fore, π(u2), . . . , π(ud ) is a lattice basis of Λ1.
(2) Let y ∈ Λ∗
1 ⊆ u
⊥ and x ∈ Λ. Then 〈 y, x 〉 = 〈 y, π(x) 〉 ∈ Z.
(3) Let x ∈ Rd . We have to estimate d(x, Λ). For this, let y := π(x). We choose
a lattice point v ∈ Λ1 closest to y. See also Figure 4.3. Then we ﬁnd a lattice
point w ∈ Λ with π(w) = v such that d(x, w + y − v) ≤ 1
2 ∥u∥. Using the
triangle inequality

d(x, w)
2 ≤ d(x, w + y − v)
2 + d(w + y − v, w)
2.

we obtain
 d(x, Λ)
2 ≤ 1

4 ∥u∥2 + µ(Λ1)
2.

Now the statement follows by the deﬁnition of the covering radius. ⊓⊔

Proof (Proof of Theorem 4.2.6). For the left inequality recursively choose recur-
sively ui ∈ Λ such that ui has the shortest length of all lattice points in Λ such that
u1, . . . , ui is linearly independent, for i = 1, . . . , d. We claim that µ(Λ) ≥ 1
2 ∥ud ∥.

Assume not. Let x := 1
2 ud . Then there exists some a ∈ Λ such that ∥a − x∥ <
1
2 ∥ud ∥. Hence, ∥a∥ ≤ ∥a − x∥ + ∥x∥ < ∥ud ∥,

and ∥2a − ud ∥ = 2∥a − x∥ < ∥ud ∥.

Hence, by our choice of ud , lin(u1, . . . , ud−1) contains a and 2a −ud , and thus also
ud , a contradiction.
Let v ∈ Λ⋆ such that ϱ(Λ⋆) = 1
2 ∥v∥. Then there exists some i ∈ {1, . . . , d} such
that 〈 v, ui 〉 ̸= 0, in particular, |〈 ui, v 〉| ≥ 1. Now, combining the previous results
with the Cauchy-Schwartz inequality yields:

µ(Λ) ϱ(Λ⋆) ≥ 1

4 ∥ud ∥∥v∥ ≥ 1

4 ∥ui∥∥v∥ ≥ 1

4 |〈 ui, v 〉| ≥ 1

4 .

We prove the middle inequality by induction on d. You will prove the initial
case d = 1 for the induction in Exercise 4.5.
Let d ≥ 2. We choose a shortest non-zero lattice vector u ∈ Λ, thus, ∥u∥ =
2 ϱ(Λ). Let us consider π, Λ1, and Λ⋆
1 as in Lemma 4.2.7. Since, Λ⋆
1 ⊆ Λ⋆, we
have ϱ(Λ⋆) ≤ ϱ(Λ⋆
1). Now, Lemma 4.2.7(3) and Corollary 4.2.5 yields

— 66 — Haase, Nill, Paffenholz: Lattice Polytopes

Geometry of Numbers (preliminary version of December 7, 2012)

µ(Λ)
2 ϱ(Λ⋆)
2 ≤ ϱ(Λ)
2 ϱ(Λ⋆)
2 + µ(Λ1)
2 ϱ(Λ⋆)
2 ≤ 1

16 d 2 + µ(Λ1)
2 ϱ(Λ⋆
1)
2.

Therefore, the induction hypothesis yields the desired statement.
Finally, the right inequality follows from the following well-known fact (which
you will prove in Exercise 4.6).

d∑

i=0 k2 = d + 2

3
  + d + 1

3
  = 1

3 d 3 + 1

2 d 2 + 1

6 d ≤ d 3. ⊓⊔

4.3 The Flatness Theorem

In this section we prove a version of the celebrated ﬂatness theorem. We will
not prove the best possible bound, this is beyond the scope of this book. We will
follow a version of the proof outlined in [3].

4.3.1 Deﬁnition (width). Let K ⊆ Rd be a full-dimensional convex body. The
width of K with respect to a non-zero lattice vector a ∈ Λ⋆ is deﬁned as

ω(K; a) := max
x∈K a(x) − min
x∈K a(x).

We deﬁne the width of K with respect to Λ as

ωΛ(K) := inf(ω(K; a) : a ∈ Λ⋆ \ {0}).

Extending our result on empty lattice polytopes, playing around with two-
dimensional convex sets one gets the impression that a convex body without in-
terior lattice points cannot have arbitrary width. It is the main goal of this lecture
to give a proof of this observation.

4.3.2 Theorem (Flatness). Let K ⊆ Rd be a convex body with K ∩ Λ = ;. Then

ωΛ(K) ≤ d
 5
2 .

Note that the upper bound only depends on the dimension and not on the given
lattice! d
 5
2 is not the optimal bound, it was improved to d
 3
2 . Still it is unknown
and an active subject of current research, whether the sharp bound is actually of
the form O(d). Let us ﬁrst deal with the crucial case that K is simply a ball. Here,
calculating the width is directly related to the considerations about lattices in the
previous section.

4.3.3 Proposition. Let B be a ball in Rd . If B ∩Λ = ;, then

ωΛ(B) ≤ 4 ϱ(Λ⋆) µ(Λ) ≤ d
 3
2 .

Proof. Let B be a ball of radius r centered at m that satisﬁes the assumption. The
assumption yields r ≤ µ(Λ), as otherwise (Λ + (B −m)) would cover the space
(cf. Figure 4.4). Choose a shortest lattice vector v ̸= 0 in Λ⋆. By the deﬁnition of
the packing radius we have ∥v∥ = 2 ϱ(Λ⋆). We can estimate the width via

ω(B; v) = ∥v∥2r ≤ 4 ϱ(Λ⋆) µ(Λ) ≤ d
 3
2 .

where the last inequality follows from Theorem 4.2.6. ⊓⊔
 mv
 B
 Fig. 4.4

Haase, Nill, Paffenholz: Lattice Polytopes — 67 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

It is straightforward to generalize this result from balls to ellipsoids. Recall that an
ellipsoid is the image of a ball under a linear transformation of Rd , in particular,
it has a unique center.

4.3.4 Corollary. Let E be an ellipsoid. If E ∩ Λ = ; then

ωΛ(E) ≤ d
 3
2 .

Proof. Let T be the linear transformation of Rd mapping a ball B to E and deﬁne
Λ′ := T −1(Λ). The induced maps

T : Λ′ ∼=
7−→ Λ and T ⋆ : Λ⋆ ∼=
7−→ Λ′⋆

are isomorphisms. This implies

ωΛ(E) = inf
a∈Λ⋆\{0} ω(T (B); a) = inf
a∈Λ′ ⋆\{0} ω(B; T ∗(a)) = ωΛ′ (B) .

Our assumption yields B ∩ Λ′ = ;. Thus, we can apply Proposition 4.3.3. ⊓⊔

The proof of the Flatness theorem can be deduced from the following powerful
observation.

4.3.5 Proposition. Let E be an ellipsoid in K (with center a) of maximal volume.
Then K ⊆ d(E − a) + a.

In fact, this maximal volume ellipsoid is even unique. We refer for the elementary-
analytic proof of Proposition 4.3.5 to (Barvinok [2]).

Proof (Proof of Theorem 4.3.2). Let E be a maximal volume ellipsoid contained in
K with center a. Proposition 4.3.5 yields K ⊆ d(E − a) + a. Hence, the statement
follows from Corollary 4.3.4:

ωΛ(K) ≤ d ωΛ(E) ≤ d
 5
2 . ⊓⊔

4.4 Problems

4.1 Show that ∆2 and [0, 1]2 are up to unimodular equivalence the only empty
lattice polygons.

4.2 Show that multiplying with a element coprime to D in Z induces a group
automorphism of Z/DZ.

4.3 Show that lattice pyramids of lattice polytopes do not change the h
⋆-polynomial.

4.4 Prove that for any d-dimensional polytope P which is not a simplex there
exists a vertex such that the convex hull of the other vertices is full-dimensional.

4.5 Prove the case d = 1 of Theorem 4.2.6(2).

4.6 Show that ∑d
i=0 k2 =  d+2
3  +  d+1
3 

— 68 — Haase, Nill, Paffenholz: Lattice Polytopes

5
Reﬂexive and Gorenstein polytopes

Reﬂexive polytopes were introduced by Victor Batyrev in the context of mirror
symmetry, a fascinating phenomenon in string theory. Their striking feature is that
they always appear in dual pairs. Since then these special lattice polytopes have
been intensively studied and classiﬁed by mathematicians and physicists alike. By
now, all isomorphism classes of reﬂexive polytopes in dimension 4, nearly half a
billion, are known! Despite all these efforts, still many questions remain open.
Amazingly, from the viewpoint of EHRHART theory reﬂexive polytopes (and their
slightly more general relatives, Gorenstein polytopes) can be recognized from
having a symmetric h
⋆-vector. What else is there to discover?
In this chapter, we deﬁne reﬂexive polytopes, and explore some of their basic
features. Next, we present some of their surprising properties in dimensions 2
and 3. In Section 5.2 we also consider ‘divisors’ of reﬂexive polytopes, called
Gorenstein polytopes, and show that this is a natural class of lattice polytopes to
work with. In Section 5.3 we explore the combinatorics of reﬂexive polytopes in
the more tractable situation, where all facets are simplices. Finally, we consider
the question how many Gorenstein polytopes exist using results in Ehrhart theory
and the geometry of numbers developed in the previous chapters.

5.1 Reﬂexive polytopes

Let P ⊆ Rd be a d-dimensional lattice polytope (with respect to Λ = Zd ).

5.1.1 Deﬁnition. Let F (P) be the set of facets of P, F ∈ F (P), then there exists
a unique primitive inner normal ηF ∈ Λ∗ and a unique integer cF ∈ Z such that

〈 ηF , x 〉 = cF ∀x ∈ F

〈 ηF , x 〉 ≥ cF ∀x ∈ P
 69

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

cF + 1 cF

no lattice points

F

ηF ∈ Λ∗

Fig. 5.1: Proof of Proposition 5.1.3.
 5.1.2 Deﬁnition. A polytope P is called reﬂexive, if there exists w ∈ int P ∩ Λ such
that all facets have lattice distance 1 from w.
Equivalently, for any facet F ∈ F (P) there exists a lattice point u ∈ Λ⋆ such
that 〈 u, x 〉 = 〈 u, w 〉 + 1 for any x ∈ V(F ). Note that in this case u is necessarily
primitive, so u = ηF .

As the following observation shows, there is no ambiguity about the interior
point w.

5.1.3 Proposition. Let P be a reﬂexive polytope with respect to w, then

int P ∩ Λ = {w}

Proof. Let F ∈ F (P). By deﬁnition, no lattice point lies strictly between the hy-
perplanes aff(F ) and its parallel hyperplane through w. See Figure5.1. Therefore,
conv(w, F ) ∩ Λ = {w} ∪ (F ∩ Λ). Since P = ⋃
F ∈F (P) conv(w, F ), the statement
follows.

Usually, the unique interior lattice points of a reﬂexive polytope is assumed to
be the origin. We give the deﬁnition of a reﬂexive polytope in this generality
in order to allow reﬂexive polytopes to be invariant under (afﬁne) unimodular
transformations. It is also more natural in the study of Gorenstein polytopes, as
we will see later.
Reﬂexive polytopes were introduced because of their beautiful duality prop-
erty. Let us recall the deﬁnition of a dual polytope.

5.1.4 Deﬁnition (polar dual). Let P ⊆ Rd be a full-dimensional polytope with
0 ∈ P. The dual polytope or polar dual of P is deﬁned as

P ⋆ := {α ∈ (Rd )
⋆ | α(x) ≤ 1 for all x ∈ P}

It is well-known that the vertices of P ⋆ correspond one-to-one to facets of P.
More precisely, the vertices are the unique inner facet normals evaluating as −1
on facets.
The most important result is the duality theorem (which holds more generally
for convex bodies containing the 0 in their interior):

P ⋆⋆ = P

As a consequence, here is the promised characterization of reﬂexive polytopes
(Exercise 5.1).

5.1.5 Proposition. Let P be a d-dimensional lattice polytope in Rd with 0 ∈ int P.
Then the following are equivalent:

◃ P reﬂexive,
◃ P ∗ lattice polytope
◃ P ∗ reﬂexive. ⊓⊔

Coming back to Proposition 5.1.3, the reader will prove in Exercise 5.2 that any
lattice polygon with one interior lattice points is also a reﬂexive polygon. How-
ever, this is not true in dimension 3 and higher (Exercise 5.3).

— 70 — Haase, Nill, Paffenholz: Lattice Polytopes

Reﬂexive and Gorenstein polytopes (preliminary version of December 7, 2012)

5.1.1 Dimension 2 and the number 12

We turn to a remarkable result about reﬂexive polygons.

5.1.6 Theorem. The numbers of boundary lattice points of a reﬂexive polygon and
its dual add up to 12.

At least ﬁve different proofs appear in [21, 15]: by exhaustion, by a walk in the
space of polygons, using toric varieties, using modular forms, or via relations in
SL2(Z).
We will pursue the walk-in-the-space-of-polygons strategy. It yields a more gen-
eral version of the 12 for unimodular fans. But this needs some preparation. Two
adjacent lattice points on the boundary of a reﬂexive polygon form a lattice ba-
sis by PICK’s theorem. The cones these lattice points generate form a complete
unimodular fan.

5.1.7 Lemma. Let Ж be a complete unimodular fan in R2. Every ray ϱ ∈ Ж[1]
with primitive generator v is contained in precisely two 2-cones σ = cone(v, w) and
σ′ = cone(v, w′) in Ж.
In this situation, there is a unique integer a(τ) such that

w + w′ = a(τ)v .

Proof. Since w, v form a lattice basis of Z
2, we have w′ = k1w + k2 v. Since v, w′

form a lattice basis, we deduce k1 = ±1. Hence, k1 = −1 by our assumption on
the cones. Therefore, w + w′ = k2 v. ⊓⊔

5.1.8 Lemma. Let P be a reﬂexive polygon, and let v1, v2, v3 be consecutive lattice
points on the boundary of P with v1 + v3 = av2, for a ∈ Z.
If v2 is a vertex of P, then the edge of P ⋆ dual to v2 has length 2 − a. (If v2 is not
a vertex, then a = 2.)

Proof. Let {v⋆
1, v⋆
2} be the basis dual to the basis {v1, v2}. Then the vertices of P ⋆

dual to the edges v1, v2 and v2, v3 are v⋆
1 + v⋆
2 and (a − 1)v⋆
1 + v⋆
2, respectively. ⊓⊔

In light of this lemma, Theorem 5.1.6 follows from the following theorem.

5.1.9 Theorem. Let Ж be a complete unimodular fan in R2. Then
∑

τ∈Ж[1](3 − a(τ)) = 12 . (5.1.1)

This is the theorem we will prove by walking in the space of fans. Here are the
steps in our walk.

5.1.10 Deﬁnition. Let Ж be a unimodular fan in R2, and let σ ∈ Ж[2] with
primitive generators v1, v2. Set ϱ := cone(v1 + v2), and

pull(Ж; ϱ) := Ж \ {σ} ∪ {ϱ, cone(ϱ, v1), cone(ϱ, v2)} .

We say that the fan pull(Ж; ϱ) is obtained as a smooth blow-up of σ in Ж.

The deﬁning property of such a smooth blow-up is the fact that the new ray ϱ
has ray parameter a(ϱ) = 1. As the reader can verify in Exercise 5.5, these steps
preserve the validity of equation (5.1.1).

5.1.11 Lemma. If the complete unimodular fan Ж in R2 satisﬁes (5.1.1), and Ж
′

is a smooth blow-up of Ж, then Ж
′ also satisﬁes (5.1.1).
 Fig. 5.2: The fan deﬁned by a reﬂexive
polygon

Fig. 5.3: The dual edge has length 2− a

Fig. 5.4: Smooth blow-up of a 2-
dimensional fan

Fig. 5.5: Not a smooth blow-up

Haase, Nill, Paffenholz: Lattice Polytopes — 71 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

Fig. 5.6: Unimodularly subdividing a 2-
cone
 Fig. 5.7: Diﬀerent λ’s
 It remains to show that these steps connect the space of fans.

5.1.12 Theorem. Let Ж and Ж
′ be two complete unimodular fans in R2. Then
there is another complete unimodular fan Ж
′′ which can be obtained by a sequence
of smooth blow-ups from both Ж and Ж
′.

The corresponding statement in general dimension has been conjectured by Oda.
This Strong Oda Conjecture is still wide open. Connectivity of the space of com-
plete unimodular fans has been shown in all dimensions. It was the foundation
of the celebrated Weak Factorization Theorem.
For the proof of Theorem 5.1.12 we need three lemmas.

5.1.13 Lemma. Let σ ⊆ R2 be a pointed 2-cone. Then there is a unimodular fan
Ж with support σ.

Proof. Consider the polyhedron P := conv(σ ∩ Z
2 \ {0}). The bounded segments
of P generate cones which form a fan with support σ. For any such segment,
the triangle it forms with 0 does not contain any other lattice points. Hence, it is
unimodular by Pick’s theorem. ⊓⊔

The proof of the following observation is Exercise 5.6.

5.1.14 Lemma. Let Ж be a unimodular fan in R2, and let v1, v2, v3 ∈ Z
2 be primi-
tive so that σ1 := cone(v1, v2) and σ2 := cone(v2, v3) (together with all their faces)
form a fan, and so that v1 + v3 = av2. Then

(1) cone(v1, v2) ∪ cone(v2, v3) is a pointed cone if and only if a ≥ 1, but
(2) v2 is a vertex of conv(0, v1, v2, v3) if and only if a ≤ 1.

Proof. proof missing

Using this fact we can prove a crucial step towards connectivity:

5.1.15 Lemma. Let Ж be a unimodular fan in R2 which reﬁnes a unimodular fan
Ж
′. Then Ж can be obtained from Ж
′ by a sequence of smooth blow-ups.

Proof. Use induction on r := |Ж[1] \ Ж
′|. If r = 0, we have Ж = Ж
′.
If r ≥ 1, all ray parameters of rays of Ж that do not belong to Ж
′ must be
≥ 1 by Lemma 5.1.14(1). On the other hand, if σ ∈ Ж
′[2] contains rays of Ж
in the interior, then the convex hull of the primitive generators has a vertex in
the interior of σ. The corresponding ray falls into case (2) of Lemma 5.1.14 and
hence must have parameter = 1. ⊓⊔

Proof (Theorem 5.1.12). The collection Ж := {σ ∩ σ′ : σ ∈ Ж, σ′ ∈ Ж
′} is a
complete fan. By Lemma 5.1.13, there is a complete unimodular fan Ж
′′ reﬁning
Ж. Now, we use the previous lemma. ⊓⊔

Putting it all together, Lemma 5.1.11 and Theorem 5.1.12 imply Theorem 5.1.9.

5.1.2 Dimension 3 and the number 24

In dimension three, there is a possibly even more striking result.

5.1.16 Theorem. If P is a 3-dimensional reﬂexive polytope, then
∑

e edge of P length e · length e⋆ = 24 .

— 72 — Haase, Nill, Paffenholz: Lattice Polytopes

Reﬂexive and Gorenstein polytopes (preliminary version of December 7, 2012)

This result was ﬁrst proved by Dimitrios Dais as follows. By [5], a general
anticanonical hypersurface Z in the toric variety associated with P must be a 2-
dimensional Calabi–Yau, i.e., a K3-surface which has Euler characteristic χ(Z) =
24. By [9], the above sum computes χ(Z). For about a decade, this remained the
only proof (apart from exhaustion). We will provide an elementary proof in the
present section.
Sadly, the story does not continue in dimensions ≥ 4. But in dimension three,
we can carry out a similar program as we did in dimension two. First, we de-
scribe parameters for unimodular fans which will replace dual edge lengths (Ex-
ercise 5.8).

5.1.17 Lemma. Let Ж be a complete unimodular fan in Rd . Every (d − 1)-cone
τ ∈ Ж[d − 1] with primitive generators v1, . . . , vd−1 is contained in precisely two
d-cones σ = cone(τ, vd ) and σ′ = cone(τ, v′
d ) in Ж.
In this situation, there are unique integers a(τ, vi) so that

vd + v′
d =
 d−1∑

i=1 a(τ, vi)vi .

Next, we construct a complete unimodular fan from a reﬂexive 3-polytope.

5.1.18 Proposition. Let P be a 3-dimensional reﬂexive polytope, and let T be a full
lattice triangulation of its boundary. Then Ж := {cone σ : σ ∈ T} is a complete
unimodular fan.
Further, if conv(v1, v2) ∈ T[1] is contained in an edge e of P, then the dual edge
e⋆ of P ⋆ has length 2 − a(τ, v1) − a(τ, v2) where τ = cone(v1, v2) ∈ Ж. (Otherwise
a(τ, v1) + a(τ, v2) = 2.)

Proof. For Ж, we only need to prove unimodularity. Every triangle σ in a full
triangulation is unimodular in its afﬁne span by Pick’s theorem. Because P is
reﬂexive, this afﬁne span has distance one to the origin, so that conv(0, σ) is
unimodular.
In order to compute the length of e⋆, consider the two 3-cones σ = cone(τ, v3)
and σ′ = cone(τ, v′
3) of Ж containing τ. By deﬁnition of the parameters we have

v′
3 = −v3 + a(τ, v1)v1 + a(τ, v2)v2 .

As in dimension two, let {v⋆
1, v⋆
2, v⋆
3} be the basis dual to the basis {v1, v2, v3}. Then
the vertices of P ⋆ dual to the facets of P containing {v1, v2, v3} and {v1, v2, v′
3} are
v⋆
1 + v⋆
2 + v⋆
3 and v⋆
1 + v⋆
2 + (a(τ, v1) + a(τ, v2) − 1)v⋆
3, respectively. ⊓⊔

Thus, Theorem 5.1.16 follows from the following fan version.

5.1.19 Theorem. Let Ж be a complete unimodular fan in R3. Then
∑

τ∈Ж[2]
with primitive
generators v1,v2
  
2 − a(τ, v1) − a(τ, v2)
 = 24 .

We could, again, prove this theorem using a walk in the space of fans. The
invariance under smooth blow-ups is elementary. But connectivity of the space
of fans is a deep theorem, way beyond the scope of these notes. Luckily, one can
deduce the 24 from the 12 by double counting.

5.1.20 Lemma. Let Ж be a complete unimodular fan in R3, and let ϱ ∈ Ж[1]
with primitive generator v. Then the projection π: R3 → R3/Rv maps star(ϱ; Ж)

Haase, Nill, Paffenholz: Lattice Polytopes — 73 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

Fig. 5.8: Quotient fan Ж/ϱ
 to a complete unimodular fan Ж/ϱ. If τ ∈ star(ϱ; Ж) is a 2-cone with primitive
generators v, v′, then the corresponding ray π(τ) of Ж/ϱ has parameter a(π(τ)) =
a(τ, v′).

Proof. Let v1 and v2 be the additional primitive generators of the 3 cones contain-
ing τ. Then v1 + v2 = a(τ, v)v + a(τ, v′)v′. Applying π yields π(v1) + π(v2) =
a(τ, v′)π(v′). ⊓⊔

Proof (Theorem 5.1.19). Let us ﬁrst collect what we need. Our fan Ж gives
rise to a triangulation of the 2-sphere with vertex set Ж[1], edge set Ж[2],
and triangle set Ж[3]. As such, we have 3|Ж[1]| − |Ж[2]| = 6 from Eu-
ler’s formula and double counting of edge-triangle-incidences. Also, we have∑
v∈Ж[1] deg v = 2|Ж[2]|, where deg v denotes the number of edges contain-
ing the vertex v. Armed with these formulas we compute
∑

τ∈Ж[2]
with primitive
generators v1,v2
  
2 − a(τ, v1) − a(τ, v2)


= ∑

cone(v)∈Ж[1]
 ∑

τ∈Ж[2]
τ=cone(v,w)
 (1 − a(τ, w))

= ∑

cone(v)∈Ж[1]
 ∑

τ∈Ж[2]
τ=cone(v,w)
 ((3 − a(τ, w)) − 2)

= ∑

cone(v)∈Ж[1] 12 − 2 deg v = 12|Ж[1]| − 4|Ж[2]| = 24 .

Here we have used Theorem 5.1.9 for the quotient fans Ж/ϱ in the third equality.
⊓⊔

5.2 Gorenstein polytopes

In this section, we will generalize the deﬁnition and duality of reﬂexive polytopes
in a setting which is more natural from the viewpoint of cones as well as from
Ehrhart theory. For this, let P be a full-dimensional lattice polytope in Rd . Let’s
recall some deﬁnitions.

5.2.1 Deﬁnition. Let Λ = Zd and ¯Λ = Zd+1. Then

CP := pos(P × 1) ⊆ Rd+1

C ⋆
P := {u ∈ (Rd+1)
∗ 〈u, x〉 ≥ 0 ∀x ∈ CP }

For F ∈ F (P) there exists a unique primitive inner normal uF ∈ ¯Λ⋆ such that

〈 uF , x 〉 = 0 ∀x ∈ F × 1

〈 uF , x 〉 ≥ 0 ∀x ∈ P × 1

Actually, uF = (ηF , −cF ), since

〈 (ηF , −cF ), (x, 1) 〉 = 〈 ηF , x 〉 − cF
 ¨= 0 x ∈ F
≥ 0 x ∈ P

— 74 — Haase, Nill, Paffenholz: Lattice Polytopes

Reﬂexive and Gorenstein polytopes (preliminary version of December 7, 2012)

By duality of cones we have the correspondence:

facets of P ↔ rays of C ∨
P
F ↔ pos(uF )

We are going to denote cones associated to lattice polytopes as Gorenstein cones.

5.2.2 Deﬁnition. Let C ⊆ Rd+1 be a (d + 1)-dimensional pointed rational cone.
Then C is called Gorenstein cone, if there exists a d-dimensional lattice polytope
P ⊆ Rd such that C ∼= CP .
Equivalently, C is a Gorenstein cone if and only if there exists a lattice point
uC ∈ ¯Λ⋆ such that 〈 uC , x 〉 = 1 for all primitive generators of the rays of C. In this
case, uC is necessarily primitive.

Our main result gives a complete characterization of lattice polytopes whose
cones have dual Gorenstein cones in terms of Ehrhart theory. The reader may
have to recall the deﬁnition of the degree and codegree of a lattice polytopes
from Chapter 3.

5.2.3 Theorem. The following are equivalent for a d-dimensional lattice polytope
P ⊆ Rd of degree s and codegree r:

(1) C ∨
P Gorenstein cone
(2) r P reﬂexive
(3) ∀k ≥ r: int(kP) ∩ Λ = w + (k − r)P ∩ Λ for some w ∈ int(r P) ∩ Λ
(4) bEhrP •t −1− = (−1)d+1 t r bEhrP (t)
(5) ehrP (−k) = (−1)d ehrP (k − r) ∀k ∈ Z
(6) h
⋆
i = h
⋆
s−i ∀i = 0, . . . , s

In this case: uC ⋆
P = w × {r} and r is the unique k ∈ N≥1 such that kP is reﬂexive.

Proof. Let us identify P with P × 1. We recall the Ehrhart series:

bEhrP (t) =
 ∑s
i=0 h
⋆
i t i

(1 − t)d+1

Ehrhart reciprocity yields:
∑

k≥1 | int kP ∩ ¯Λ|t k = ∑

k≥1(−1)d ehrP (−k) t k

= (−1)d+1bEhrP •t −1−

=
 ∑s
i=0 h
⋆
i t d+1−i

(1 − t)d+1

=
 ∑r+s=d+1
i=r h
⋆
d+1−i t i

(1 − t)d+1

Comparing the coefﬁcients yields (4) ⇔ (5) ⇔ (6).
(5) ⇔ | int kP ∩ ¯Λ = |(k − r)P ∩ ¯Λ| ∀k ≥ r: Note that w ∈ int r P ∩ ¯Λ ⇒
w + ((k − r)P ∩ ¯Λ) ⊆ int kP ∩ ¯Λ. See Figure 5.9 for an illustration. This implies
(5) ⇔ (3).
Let us prove (3) ⇒ (1): Let w ∈ int r P ∩ ¯Λ, F ∈ F (P). We want to show that
〈 uF , w 〉 = 1. This would prove that C ⋆
P is a Gorenstein cone. For this let us deﬁne
 r P
w
 kP

(k − r)P + w
 (k − r)P

w

Fig. 5.9

Haase, Nill, Paffenholz: Lattice Polytopes — 75 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

0
1 0

P F

kP kF

uC ∨
P

Fig. 5.10
 CP

(0, 1) P
 C ∨
P

u = (1, 2), 〈u, ·〉 = 3

(−1, 2) (0, 1)
P ∨

Fig. 5.11

P = [0, 1]2

Fig. 5.12

2P

(2P −   1
1 
)
∗

Fig. 5.13
 C ′ := pos(w, F ). By Exercise 5.10 C ′ contains a lattice basis b1, . . . , bd+1 such that
b1, . . . , bd ∈ pos(F ) and bd+1 /∈ pos(F ). Therefore, bd+1 ∈ int CP ∩ ¯¯Λ, in particular,
there exists some k ≥ r such that bd+1 ∈ int kP ∩ ¯Λ. By our assumption (3) there
exists some m ∈ (k − r)P ∩ ¯Λ such that bd+1 = w + m. Let us deﬁne the dual lattice
basis b∗
1, . . . , b∗
d+1 ∈ ¯Λ⋆. Since
 〈b∗
d+1, pos(F )〉 = 0

〈uF , pos(F )〉 = 0

and b∗
d+1 is primitive, we see b∗
d+1 = uF . Therefore, 1 = 〈uF , bd+1〉 = 〈uF , w〉 +
〈uF , m〉, hence, 〈uF , w〉 = 1, as desired.
(1) ⇒ (2): Let w := uC ⋆
P ∈ int CP ∩ ¯Λ. Then there exists k ≥ r such that w ∈
int kP ∩ ¯Λ. Let F ∈ F (P), so, 〈w, uF 〉 = 1. Restricting uF to the afﬁne lattice
Zd × {k} yields an afﬁne-linear form u
′
F such that 〈u
′
F , w〉 − 〈u
′
F , kF 〉 = 1. See
Figure 5.10 for an illustration. Hence, kP is reﬂexive (w.r.t. w).
Let us show the additional last statement in the theorem. Assume k > r, then

| int kP ∩ ¯Λ| ≥ |w + (k − r)P ∩ ¯Λ| = |(k − r)P ∩ ¯Λ|

≥ |P ∩ ¯Λ| > 1

This is a contradiction.
(2)⇒(1): Let r P be reﬂexive, and F ∈ F (P). We know that uF = (ηF , cF ) and
〈ηF , r F × r〉 = r cF . Hence, 〈ηF , w〉 = r cF + 1, so 〈uF , (w, r)〉 = 〈ηF , w〉 − cF r = 1.
(2) ⇒ (3): The inclusion "⊇" is clear.
Let us prove "⊆". Let x ∈ int(kP) ∩ ¯Λ, k ≥ r. Then

〈uF , x − w〉 = 〈uF , x〉
︸ ︷︷ ︸
≥1
 − 〈uF , w〉
︸ ︷︷ ︸
=1
 ≥ 0 ∀F ∈ F (P)

In particular, x − w ∈ (C ⋆
P )
⋆ = CP and 〈uP , x − w〉 = k − r. Hence, x − w ∈
(k − r)P ∩ Λ, as desired. ⊓⊔

This motivates our main deﬁnition.

5.2.4 Deﬁnition (Gorenstein polytope). P is a Gorenstein polytope if (1) − (6)
holds.

In other words, a lattice polytope P is a Gorenstein polytope if some multiple
kP is a reﬂexive polytope. This multiple k is necessarily equal to the codegree
by Proposition 5.1.3. For instance, reﬂexive polytopes are precisely Gorenstein
polytopes of codegree 1.

5.2.5 Example. 42

(1) See Figure 5.11. C ∨
P is not a Gorenstein cone, ⇒ P is not a Gorenstein poly-
tope. r = codeg P = 1, int P ∩ Λ = 2 > 1; h
∗
0 = 1, h
∗
1 = 2.
(2) See Figure 5.12. P = [0, 1]2 is a Gorenstein polytope of codegree r =
codeg(P) = 2. (2P is reﬂexive, see Figure 5.13.
(3) The Birkhoff polytope Bn is a famous polytope which is deﬁned as the convex
hull of all n × n-permutation matrices. It is a Gorenstein polytope of codegree
n, see Exercise 5.11.

— 76 — Haase, Nill, Paffenholz: Lattice Polytopes

Reﬂexive and Gorenstein polytopes (preliminary version of December 7, 2012)

There is a natural duality of Gorenstein polytopes extending the one of reﬂexive
polytopes. Since Gorenstein polytopes do not have interior lattice points, if r > 1,
we have to use the duality of cones.

5.2.6 Proposition. Let P be a Gorenstein polytope (as in Theorem 5.2.3). Then

P ∨ := {x ∈ C ⋆
P : 〈uC ⋆
P , x〉 = 1}

= conv(ηF : F ∈ F (P))

is also a Gorenstein polytope of the same dimension, degree and codegree as P, called
the dual Gorenstein polytope.

Proof. uC ⋆
P = w, hence, 〈 uC ⋆
P , uP 〉 = r. Let G ∈ F (P ⋆). Then 〈 uG, G 〉 = 0 and
〈 uG, uCP 〉 = 1. Therefore, r P ⋆ is reﬂexive. ⊓⊔

Note that this duality is quite subtle. For instance, for r > 1, P ∨ does not lie in
the hyperplane Rd × 1. Thus, it is not intrinsically embedded in Rd . It is merely
given as a d-dimensional polytope in Rd+1. Moreover, except for codegree 1,
P ∨ is not isomorphic to (r P − w)
∗, as one might guess at ﬁrst. For instance, in
Example 5.2.5(2) with r = 2, P ∨ is just isomorphic to P.
Let us consider the case of a reﬂexive polytope P, say, 0 ∈ int(P). Then we
recover the duality of reﬂexive polytopes:

P ∨ = {x ∈ (Rd+1)
∗ : 〈x, ( y, 1)〉 ≥ ∀ y ∈ P, 〈x, (0, 1)〉 = 1}

= {(x, 1) : 〈x, y〉 ≥ −1 ∀ y ∈ P}

= P ⋆ × 1.

This gives another proof of Proposition 5.1.5.

5.3 The combinatorics of simplicial reﬂexive polytopes

Throughout, let P ⊆ Rd be a d-dimensional reﬂexive polytope with the origin of
the lattice Λ = Zd in its interior.

5.3.1 The maximal number of vertices

It is a natural question to ask for the maximal number of vertices of a d-
dimensional reﬂexive (or Gorenstein) polytope. Let us look at small dimension
d ≤ 4, where the answer is known by the classiﬁcation of Kreuzer and Skarke.

5.3.1 Example.

d = 2: |V(P)| ≤ 6, only attained by the reﬂexive hexagon H , see Figure 5.14
d = 3: |V(P)| ≤ 14, only attained by the polytope in Figure 5.15
d = 4: |V(P)| ≤ 36, only attained by H × H .

Based upon these observations we state the following daring conjecture.

5.3.2 Conjecture. |V(P)| ≤ 6
 d
2 , equality holds for d even and P ∼= H
 d
2 .

This question is still wide open. It has been shown to hold for simple centrally
symmetric reﬂexive polytopes, since this class of reﬂexive polytopes can be com-
pletely classiﬁed. In the following we will present some of the techniques used to
prove this.
 Fig. 5.14: the hexagon H

Fig. 5.15: a reﬂexive 3-polytope

Haase, Nill, Paffenholz: Lattice Polytopes — 77 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

5.3.2 The free sum construction

Our main motivation is to determine the maximal number of vertices of a sim-
plicial reﬂexive polytope and to ﬁnd out how the extremal polytopes look like.
For this, we present a direct way how to construct higher-dimensional reﬂexive
polytopes, called the free-sum construction:

5.3.3 Deﬁnition (Free Sum). Pi ⊆ Rdi di-dim polytope with 0 ∈ int (Pi) (i =
1, 2). Then
 P1 ◦ P2 := conv  P1 × {0}
{0} × P2
  ⊆ Rd1+d2

free sum (d1 + d2)-dim. polytope, 0 ∈ int(P1 ◦ P2).

5.3.4 Example. 42

(1) P1 = P2 ⇒ P1 ◦ P2 =

(2) P1 = H , P2 = [−1, 1] ⇝ P1 ◦ P2 = bipyramid(H ) =

It follows directly from the deﬁnition that the free-sum construction is the dual
operation to products:
 (P1 ◦ P2)
∗ = P ∗
1 × P ∗
2

In particular, if P1, P2 are reﬂexive, then P1 ◦ P2, P1 × P2 are reﬂexive.
There are nice formulas how the Ehrhart- and h
∗-polynomials behave under
the free sum and product construction.

5.3.5 Proposition. Let P1, P2 be reﬂexive. Then

ehrP1×P2 = ehrP1 ehrP2 , h
⋆
P1◦P2 = h
⋆
P1 h
⋆
P2 .

While the ﬁrst result follows directly from the construction, the second one is not
obvious. We will leave this as an exercise. Here is our main theorem. Its proof will
occupy the remainder of this section.

5.3.6 Theorem. Let P be simplicial. Then |V(P)| ≤ 3d, and equality holds only if d
is even and P ∼= H ◦ . . . ◦ H︸ ︷︷ ︸

d
2
 .

Simplicial reﬂexive d-polytopes with 3d−1 vertices are also completely known.

5.3.3 The addition property

Lattice points in reﬂexive polytopes satisfy a partial addition property. For this let
us deﬁne a relation.

5.3.7 Deﬁnition. Let x, y ∈ ∂ P ∩ Λ, x ̸= y. Then x ∼ y, if there exists a facet of
P containing x and y.

Here is the main observation:

5.3.8 Proposition. Let x, y ∈ ∂ P ∩ Λ, x ̸= y. Then

— 78 — Haase, Nill, Paffenholz: Lattice Polytopes

Reﬂexive and Gorenstein polytopes (preliminary version of December 7, 2012)

(1) either x ∼ y
(2) or x + y = 0
(3) or x + y ∈ ∂ P ∩ Λ.

If (3) holds, then x ∼ x + y or y ∼ x + y. Moreover, there exist a, b ∈ N≥1 such
that z := ax + b y ∈ ∂ (P) ∩ Λ such that x ∼ z ∼ y. In this case, a = 1 or b = 1.

Proof. Assume (1), (2) do not hold and (3) is wrong. Then duality yields that
there exists a facet F ∈ F (P) such that −1 > 〈ηF , x + y〉 ∈ Z. Hence, −2 ≥
〈ηF , x + y〉 = 〈ηF , x〉 + 〈ηF , y〉 where 〈ηF , x〉, 〈ηF , y〉 ≥ 1. This would imply
x, y ∈ F , a contradiction.
Now, let F ∈ F (P) such that −1 = 〈ηF , x + y〉 = 〈ηF , x〉 + 〈ηF , y〉. Since
〈ηF , x〉, 〈ηF , y〉 ∈ Z≥−1, we get either x ∈ F and 〈ηF , y〉 = 0 or y ∈ F, 〈ηF , x〉 = 0.
Let us assume the ﬁrst case. We consider the pair x + y, y. If x + y ∼ y, we are
done. So assume not. Then we get (x + y)+ y ∈ ∂ P ∩Λ. Hence, since 〈 ηF , y 〉 = 0,
we still have x + 2 y ∈ F . Now, we consider the pair x + 2 y, y. Since |P ∩ Λ| < ∞,
we cannot repeat this argument ad inﬁmum, so there has to exist some b ∈ N≥1
such that x + b y ∼ y. ⊓⊔

Note that even if x, y are vertices, z does not have to be a vertex again, if
the dimension of P is larger than two. This result has many applications. As an
immediate result we deduce the following constraints on the combinatorics of a
simplicial reﬂexive polytope (Exercise 5.12).

5.3.9 Corollary. The diameter of the vertex-edge graph of a simplicial reﬂexive poly-
tope is at most three.

5.3.4 Vertices between parallel facets

In this section, we use the partial addition of lattice points to deduce the pre-
cise form of vertices that lie between two parallel facets of a simplicial reﬂexive
polytope.
Let us ﬁx a facet F of a simplicial reﬂexive d-polytope P. We denote the vertices
of F by b1, . . . , bd . Let Fi ∈ F (P) such that Fi ∩ F = conv(b1, . . . , ˆbi, . . . , bd ).
Then there exists a unique mi ∈ V(P) such that V(Fi) = {b1, . . . , mi, . . . , bd } for
i = 1, . . . , d.
Note that b1, . . . , bd is in general not a lattice basis. We can still deﬁne the dual
(vector-space) basis b∗
1, . . . , b∗
d ∈ (Rd )
∗. These are in general no lattice points.
The next lemma shows in particular, that there are at most d vertices which lie
on the adjacent parallel hyperplane to a facet.

5.3.10 Lemma. v ∈ V(P), 〈ηF , v〉 = 0.

(1) Let i ∈ {1, . . . , d}
 v ∈ Fi ⇐⇒ v = mi ⇐⇒ 〈b∗
i , v〉 < 0.

In particular, such i exists.
(2) If 〈b∗
i , mi〉 = −1, 〈ηF , mi〉 = 0 ∀i = 1, . . . , d, then b1, . . . , bd is a lattice basis.

Proof. i ∈ {1, . . . , d}.
Let
 αi := −1 − 〈ηF , mi〉

〈b∗
i , mi〉 ,

where 〈b∗
i , mi〉 < 0 since 0 ∈ int(P). Since 〈ηF , mi〉 ≥ 0, we have αi > 0.
We claim that

Haase, Nill, Paffenholz: Lattice Polytopes — 79 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

ηFi = ηF + αi b∗
i .

It sufﬁces to check this equality for the vertices of Fi, where the left side always
evaluates to −1: j ̸= i: 〈ηF , b j〉 + αi〈b∗
i , b j〉 = −1,
〈ηF , mi〉 + αi〈b∗
i , mi〉 = −1.
Now, we can prove (1) and (2).

(1) ηF = −b∗
1 − . . . − b∗
d , 〈ηF , v〉 = 0 ⇒ ∃i : 〈b∗
i , v〉 < 0. Moreover, 〈b∗
i , v〉 < 0
⇐⇒ 〈ηF + αi b∗
i , v〉 < 0 ⇐⇒ 〈ηFi , v〉 < 0 ⇐⇒ v ∈ Fi ⇐⇒ v = mi.
(2) Here: αi = 1 ∀i = 1, . . . , d, hence b∗
i = ηFi − ηF ∈ Λ∗ ∀i = 1, . . . , d. Therefore

x = ∑d
i=1 λi bi ∈ Λ ⇒ λi = 〈b∗
i , x〉 ∈ Z ⇒ b1, . . . , bd is a lattice basis. ⊓⊔

Combining this lemma with the addition property for the lattice points in the dual
reﬂexive polytope yields our desired result.

5.3.11 Proposition. v ∈ V(P), 〈ηF , v〉 = 0. If −F ∈ F (P), then there are I, J ⊆
{1, . . . , d}, I ∩ J = ;, |I| = |J| such that

v = ∑

j∈J b j − ∑

i∈I bi.

Proof. We use the notation in the proof of the previous lemma. Let I := {i ∈

{1, . . . , d}s.t.〈b∗
i , v〉 < 0} ̸= ;. Then i ∈ I (1)
⇒ v = mi.

−F ∈ F (P) ⇒ Fi ∩F = ; ⇒ ηFi ̸∼ η−F = −ηF
 Addition
⇒ ηFi −ηF ∈ ∂ P ∗∩Λ∗ ⇒ −1 ≤

〈α
∗
i b∗
i , ±b∗
i 〉 = ±αi ∈ Z αi >0
⇒ αi = 1 ⇒ 〈b∗
i , v〉 = 〈ηFi − ηF , v〉 = 〈ηFi , v〉
︸ ︷︷ ︸
=−1
 − 〈ηF , v〉
︸ ︷︷ ︸
=0
 ⇒

〈b∗
i , v〉 = −1. Same argument for −F shows that 〈b∗
j , v〉 > 0 ⇒ 〈b∗
j , v〉 = 1. ⊓⊔

5.3.5 Special facets

We can now prove Theorem 5.3.6. The key idea is the following notion (due to
Øbro).

5.3.12 Deﬁnition (Special Facet). Let F ∈ F (P) such that ∑
v∈V(P) v ∈ pos(F ).
Such a facet is called special.

From now on, let F be a special facet. Obviously, special facets exist. Let us
slice the polytope (for i ∈ {−1, 0, 1, . . .}):

HP (F, i) := {v ∈ V(P) : 〈ηF 〉v = i} ∀i ∈ Z≥−1

Clearly, |HP (F, 0)| = d.

Moreover, Lemma 5.3.10 yields
 |HP (F, 1)| ≤ d.

By deﬁnition of a special facet we have the following inequality:

0 ≥ 〈ηF , ∑

v∈V(P) v〉 = ∑

i≥−1 i|HP (F, i)| = −d + ∑

i≥1 i|HP (F, i)|. (5.3.1)

Hence, we can simply count the vertices:

— 80 — Haase, Nill, Paffenholz: Lattice Polytopes

Reﬂexive and Gorenstein polytopes (preliminary version of December 7, 2012)

|V(P)| = ∑

i≥−1 |HP (F, i)| ≤ |HP (F, −1)|
︸ ︷︷ ︸
=d
 + |HP (F, 0)|
︸ ︷︷ ︸
≤d
 + ∑

i≥1 |HP (F, i)|

︸ ︷︷ ︸
≤d
 ≤ 3d. (5.3.2)

It remains to consider the equality case (|V(P)| = 3d).
In this case, equality in Equation 5.3.1 yields that

〈ηF , ∑

v∈V(P) v〉 = 0.

Hence, ∑
v∈V(P) v = 0, so any facet of P is special. Moreover, equalities in Equa-
tion 5.3.1 and show that any vertex of P lies in HP (F, i) for i = −1, 0, 1. There-
fore, −ηF ∈ P ⋆. So, −P ⋆ ⊆ P ⋆, and thus −P ⋆ = P ⋆. In other words, P is centrally
symmetric.
Since |V(P) = 3d and |HP (F, −1)| = |HP (F, 1)| = d, we have |HP (F, 0)| = d.
Lemma 5.3.10(1) yields
 HP (F, 0) = {m1, . . . , md },

as deﬁned in the previous subsection. Let k ∈ {1, . . . , k}. By Proposition 5.3.11
there are I, J ⊆ {1, . . . , d}, I ∩ J = ;, |I| = |J| such that mk = ∑
 j∈J b j − ∑
i∈I bi.
Since all m1, . . . , md are pairwise different, Lemma 5.3.10(1) yields that mk =
b jk − bk for some jk ∈ {1, . . . , d}, jk ̸= k. In other words,

σ : {1, . . . , d} → {1, . . . , d}

k 7→ jk

is a ﬁxed-point free (σ(i) ̸= i) involution (σ2 = 1, jjk = k). We may assume that
this permutation is of the form

σ = (1 2)(3 4) · · · (d − 1 d).

In particular, d is even. Moreover,

P = conv(±b1, ±(b1 − b2), ±b2, . . . , ±bd , ±(bd−1 − bd ), ±bd ).

It remains to show that b1, . . . , bd is a lattice basis, since it that case

P ∼= H ◦ · · · ◦ H︸ ︷︷ ︸

d
2
 .

See Figure 5.16. We observe that for any i = 1, . . . , d

〈b∗
i , mi〉 = 〈b∗
i , b ji − bi〉 = −1

〈ηF , mi〉 = 0

Hence, Lemma 5.3.10(2) ﬁnishes the argument. This proves Theorem 5.3.6.

5.4 Problems

5.1 Prove Proposition 5.1.5.
 b2
 b1

b1 − b2

Fig. 5.16: The situation for d = 2.

Haase, Nill, Paffenholz: Lattice Polytopes — 81 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

5.2 Show that a lattice polygon is reﬂexive if and only if it contains precisely one
interior lattice point.

5.3 Take [−1, 1]d , remove one vertex and take the convex hull of the remaining
lattice points. Show that it still contains precisely one interior lattice point. Is this
a reﬂexive polytope?

5.4 Compute h
∗-polynomial and Ehrhart polynomial of a 3-dimensional reﬂexive
polytope having b many lattice points.

5.5 Prove Lemma 5.1.11.

5.6 Prove Lemma 5.1.14.

5.7 Classify unimodular fans in R2 which are minimal with respect to blow-ups.

5.8 Prove Lemma 5.1.17.

5.9 Deﬁne smooth blow-ups for three-dimensional unimodular fans (or higher-
dimensional); and show the invariance of the equality in Theorem 5.1.19 under
smooth blow-ups.

5.10 Let Λ ⊆ Rd be a lattice of rank d. We may choose (why ?) v1, . . . , vd ∈ Λ
recursively such that vi+1 has the minimal non-zero distance from the subspace
〈v1, . . . , vi〉. Show that v1, . . . , vd is a lattice basis of Λ. In particular, any primitive
vector of Λ can be completed to a lattice basis.

5.11 Prove that the Birkhoff polytope Bn (the convex hull of n × n-permutation
matrices) is a Gorenstein polytope of codegree n. What is its dimension and de-
gree? What is the unique interior lattice point of nBn ?

5.12 Prove Lemma 5.3.9.

— 82 — Haase, Nill, Paffenholz: Lattice Polytopes

6
Unimodular Triangulations

It this chapter, we study under which assumptions a lattice polytope admits a tri-
angulation into unimodular simplices. Such unimodular triangulations of lattice
polytopes arise in algebraic geometry, commutative algebra, integer programming
and, of course, combinatorics. Because of the nice implications, having a unimod-
ular triangulation is a desirable property. But presumably, “most” lattice polytopes
do not admit a unimodular triangulation.
We will deﬁne unimodular triangulations, and prove our ﬁrst theorem for
cones in Section 6.2. Then, we deﬁne the particularly nice class of compressed
polytopes in Section 6.3, and give a few examples of important triangulations.
Section 6.4 can be regarded as a capstone section of these notes. We use uni-
modular triangulations to prove unimodality of the h
⋆ coefﬁcients of Gorenstein
polytopes with regular unimodular triangulation, tying together ideas from Chap-
ters 3, 5, and 6. Finally, in Section 6.5, we prove a mysterious theorem from the
early days of toric geometry which, to this day, raises more questions than it
answers. Some further examples and motivation for (regular) unimodular trian-
gulations are hidden in the exercises.

6.1 Regular Triangulations

6.1.1 Deﬁnition (regular subdivision). A subdivision S with vertices {v1, . . . , vm}
is regular if there is a weight vector w such that S is the projection of the lower
hull of
 conv((wi, vi) | 1 ≤ i ≤ m) ,

where the lower hull is the polyhedral complex of those facets whose normal has
negative ﬁrst coordinate.
 83

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

Figure missing

Fig. 6.1
 Given a set of points V := {v1, . . . , vm} and a weight vector w ∈ Rm we denote
by RSw(V ) the regular subdivision obtained as the lower hull of RLw(V ) :=
conv((wi, vi) | 1 ≤ i ≤ m).

6.1.2 Theorem. Any polytope admits a regular triangulation.

Proof. proof missing

6.2 Pulling Triangulations

Pulling reﬁnements are a useful tool for constructing regular triangulations.

6.2.1 Deﬁnition (Pulling Reﬁnements). Let S be a lattice subdivision of the lat-
tice polytope P ⊆ Rd , and let v ∈ P ∩ Zd . Then we obtain the pulling reﬁnement
pull(S; v) when we replace every face F ∈ S which contains v by the pyramids
conv(v, F ′) where F ′ runs over all faces of F which do not contain v.
The deﬁnition works mutatis mutandis for subdivisions of fans.

Here are some facts about the structure of pulling subdivisions.

6.2.2 Proposition.

(1) Pulling preserves regularity.
(2) Pulling all lattice points in P in some order results in a full triangulation.
(3) If only vertices of P are pulled, then every maximal cell is the join of the ﬁrst
pulled vertex v1 with a maximal cell in the pulling subdivisions of the facets not
containing v1.

In particular, we see that every (regular) lattice subdivision of a lattice polytope
has a (regular) reﬁnement which is a full triangulation.

Proof. (1): Let S = RSw(A ) be a regular subdivision of P, certiﬁed by weights
w ∈ RA (A = P ∩ Zd ), with lifted polyhedron RLw(P) = conv((wa, a) : a ∈ A )
in Rd+1. Let m ∈ A . Set w′
m := min{h : (m, h) ∈ RLw(P)} − ε and w′
a := wa for
all a ∈ A \ {m}. Then, for small enough ε > 0, the pulling reﬁnement pull(S; m)
is induced by the weights w′.
(2): Every face of pull(S; m) which contains m is a pyramid with apex m. If
Q ∈ S has n as an apex, then every face of pull(S; m) inside Q and containing n
still has n as an apex. After strongly pulling all lattice points, all lattice points are
vertices of the subdivision, and the cells have each of their vertices as apices so
they are simplices.
(3): If we apply the previous argument to the trivial subdivision of P, we see
that v1 is an apex of every cell. ⊓⊔

6.2.3 Theorem. Every rational cone has a regular unimodular triangulation.

Proof. proof missing

6.3 Compressed Polytopes

The notion of compressed polytopes was coined by Richard STANLEY [25]. Sur-
prisingly many well-known polytopes fall into this category.

6.3.1 Deﬁnition. A lattice polytope P ⊆ Rd is compressed if all lattice points in P
are vertices, and all pulling triangulations are unimodular.

— 84 — Haase, Nill, Paffenholz: Lattice Polytopes

Unimodular Triangulations (preliminary version of December 7, 2012)

Compressed polytopes admit several characterizations. A lattice polytope P has
width 1 with respect to a facet F , if it lies between the hyperplane spanned by
this facet and the next parallel lattice hyperplane, that is, ω(P; ηF ) = 1 for the
primitive inner normal innPF of F .
The main implication of the following Theorem is due to Francisco SANTOS.
The proof we present here is the original one (MSRI 1997, unpublished). It was
subsequently also proven by Ohsugi and Hibi [20] and by Sullivant [27].

6.3.2 Theorem. Let P be a lattice polytope. Then the following is equivalent:
(1) P is compressed.
(2) P has width one with respect to all its facets.
(3) P is lattice equivalent to the intersection of a unit cube with an afﬁne space.

Proof. (2) =⇒ (1): By decreasing induction on the dimension one sees that ev-
ery face of P has width 1 with respect to all facets. The restriction of a pulling
triangulation to any face is a pulling triangulation itself and thus unimodular (by
another induction). Hence, every maximal simplex in the triangulation of P is the
join of a unimodular simplex in some facet with the ﬁrst lattice point that was
pulled.
The other implications are easy. ⊓⊔

Examples of compressed polytopes include the Birkhoff polytope, order polytopes
and hypersimplices, stable set polytopes of perfect graphs.
We can apply the above characterization of compressed polytopes to triangu-
late “bigger” polytopes using hyperplane arrangements.
Let A := {n1, . . . , nr } ⊆ Zd be a collection of vectors that span Rd and form a
unimodular matrix, i.e., such that all (d × d)–minors are either 0, 1 or −1. Such
a collection induces an inﬁnite arrangement of hyperplanes

{x ∈ Rd : 〈ni, x〉 = k} for i = 1, . . . , r and k ∈ Z ,

which subdivide Rd regularly into lattice polytopes. These subdivisions are stud-
ied under the name of lattice dicing in the literature [13]. We call a lattice poly-
tope P whose collection of primitive facet normals forms a unimodular matrix
facet unimodular. Every face of a facet unimodular polytope is again facet uni-
modular in its own lattice. The above hyperplane arrangement slices P into dic-
ing cells. We call this subdivision the canonical subdivision of a facet unimodular
polytope. The canonical subdivision subdivides faces canonically.

6.3.3 Theorem. Suppose that P ⊆ Rd is a facet unimodular lattice polytope. Then
P has a regular unimodular triangulation.

Proof. The dicing cells have width one with respect to all their facets by construc-
tion. Thus, any pulling reﬁnement of the canonical subdivision will be unimodu-
lar. ⊓⊔

As a direct application of Theorem 6.3.3, ﬂow polytopes as well as polytopes
with facets in the root system of type A have regular unimodular triangulations.
This method also shows that every dilation cP of a polytope P with a (regular)
unimodular triangulation also admits such a triangulation (Theorem 6.3.4).

6.3.4 Theorem. If P has a (regular) unimodular triangulation T then its dilation
cP has one too, for every positive integer c.

In Section 6.5 below, it is convenient to use a very speciﬁc triangulation of a
dilated simplex.

Haase, Nill, Paffenholz: Lattice Polytopes — 85 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

Figure missing

Fig. 6.2
 6.3.5 Deﬁnition. The vertices 0, ed , ed + ed−1, . . . , 1 of the simplex

∆
′
d := {x ∈ Rd : 0 ≤ x1 ≤ . . . ≤ xd ≤ 1}

are totally ordered component wise. For c ∈ Z>1, the type-A hyperplane arrange-
ment triangulates the dilated simplex c∆
′
d unimodularly. We call this triangula-
tion the standard triangulation of c∆
′
d .
If S is any lattice simplex, an ordering of V(S) induces an afﬁne isomorphism
c∆
′
d → cS. The image of the standard triangulation of c∆
′
d is a lattice trian-
gulation which we call the standard triangulation of cS. Every simplex in this
triangulation has volume vol(S).

This triangulation is induced by the following weights. Let ϕ(m) := ∑
i m2
i +∑
i< j(mi − m j)
2, and evaluate at the difference to the barycenter ˆm of c∆d ( ˆmi =

ci
d+1 ): ωm := ϕ(m − ˆm). Then this triangulation as well as the weights restrict to
the faces with the induced vertex ordering. If we globally order the lattice points
in P, and choose the induced ordering on all simplices of T, we get a regular
unimodular triangulation T′ of cP.

6.4 Special Simplices in Gorenstein Polytopes

The goal of this section is to prove the following theorem of Bruns and Römer.

6.4.1 Theorem. The h
⋆-vector of a Gorenstein polytope with a regular unimodular
triangulation is unimodal. That is, 1 = h
⋆
1 ≤ . . . ≤ h
⋆
⌊s/2⌋ ≥ . . . ≥ h
⋆
s .

This theorem and its proof are due to Bruns and Roemer [JCTA 2007]. For general
Gorenstein polytopes the theorem fails, as shown by Payne and Mustata [Math
Ann 2005]. However, it is still open whether the following property might sufﬁce.

6.4.2 Deﬁnition. A lattice d-polytope P ⊆ Rd is called integrally-closed, if for
every k ∈ N≥2 and for every lattice point x ∈ kP∩Zd there exist x1, . . . , xk ∈ P∩Zd

such that x = x1 + · · · + xk.

Equivalently, let C ⊆ Rd+1 be the cone spanned by P × {1}. Then P is integrally
closed if and only if the semigroup of lattice points in C is generated by lattice
points in P × {1}. As Exercise 6.2 shows, being integrally-closed is weaker than
having a unimodular triangulation.
The central tool in the proof of Theorem 6.4.1 is the notion of a special
simplex. The use of special simplices in this context had been pioneered by
Athanasiadis [Crelle 2005]

6.4.3 Deﬁnition. A simplex S ⊆ P inside a polytope P is special if S ∩ F is a facet
of S for all facets F of P.

6.4.4 Example. cube, tetrahedron, circuit → dimension a priori ambiguous; Birkhoff

6.4.5 Lemma. Every integrally closed Gorenstein polytope has a special simplex.

Proof. Let P ⊆ Rd be integrally closed and Gorenstein with degree s. Let uP ∈ CP
be the Gorenstein point in the cone over P.
Because P is integrally closed, we can write uP = v1 + . . . + vs for v1, . . . , vs ∈
({1} × P) ∩ Zd+1. We claim that S := conv(v1, . . . , vs) is a special simplex.
Every facet F of P is dual to a vertex w of the Gorenstein dual {1} × P ∨. Then
〈 w, vi 〉 ≥ 0 and 〈 w, uP 〉 = 1. Thus, S ∩ F contains all but one of the vi. ⊓⊔

— 86 — Haase, Nill, Paffenholz: Lattice Polytopes

Unimodular Triangulations (preliminary version of December 7, 2012)

The punchline in the proof of Theorem 6.4.1 will be that we project the poly-
tope along a special simplex, and obtain a reﬂexive polytope with the same h
∗-
vector which inherits a regular unimodular triangulation from P. The following
deﬁnition describes a subcomplex of P which will project bijectively onto the
boundary of that reﬂexive polytope.

6.4.6 Deﬁnition. Let S = conv(v1, . . . , vs) ⊆ P be a special simplex. Denote by
Γ (P, S) the subcomplex of ∂ P generated by faces of the form F1 ∩ . . . ∩ Fs where
Fi is a facet of P with vi ̸∈ Fi for i = 1, . . . , s.

6.4.7 Lemma. Let S ⊆ P be a special simplex in a Gorenstein polytope, and let T
be a triangulation of Γ (P, S). Then the complex T ⋆ S generated by {conv(S ∪ F ) :
F ∈ T} is a triangulation of P. This triangulation is unimodular if T was, and it is
regular if T is the restriction to Γ (P, S) of a regular triangulation of P.

Proof. We need to show four things.

(1) If F is a (unimodular) simplex in Γ , then conv(S ∪ F ) is a (unimodular)
simplex.
(2) The conv(S ∪ F ) cover P.
(3) The conv(S ∪ F ) and their faces form a polyhedral complex.
(4) If T is the restriction to Γ (P, S) of a regular triangulation of P then T ⋆ S is
regular. ⊓⊔

The proof of Theorem 6.4.1 uses h-vectors of triangulations. Its relation to the
h
∗-vector is given by the following result [7]:

6.4.8 Theorem (Betke and McMullen 1985). Let P be a lattice polytope with a
triangulation T. Let h
⋆ be the h
⋆-vector of P and h the h-vector of the triangula-
tion. Then h
⋆
i ≤ hi for 0 ≤ i ≤ d with equality if and only if the triangulation is
unimodular.

Proof (Theorem 6.4.1). If the Gorenstein polytope P has a regular unimodular tri-
angulation, then it is integrally closed (Exercise 6.2). By Lemma 6.4.5 P contains
a special simplex S, and we can deﬁne the complex Γ (P, S). By Lemma 6.4.7 we
can modify the given triangulation of P, if necessary, to obtain a regular unimod-
ular triangulation of the form T ⋆ S for a unimodular triangulation T of Γ (P, S).
Thus h
⋆(P) = h
⋆(Γ (P, S)) = h(T) by Theorem 6.4.8.
It remains to show that T is combinatorially isomorphic to the boundary com-
plex of a simplicial polytope. Then, the g-theorem implies that h(T) is unimodal.
For this, let Φ be a strictly convex piecewise linear function on T ⋆ S. As S is a
face of the triangulation, there is a linear functional u such that 〈 u, v 〉 = Φ(v) for
all v ∈ S and 〈 u, v 〉 < Φ(v) for all v ̸∈ S.
Now let L be an afﬁne space meeting S transversally in its relative interior.
Then, for small ϵ > 0, Q := {x ∈ L : Φ(x) − 〈 u, v 〉 ≤ ϵ} is a polytope whose
boundary complex has the same combinatorics as Γ (P, S). ⊓⊔

As a corollary we can prove now the missing part of Proposition 5.3.5.

6.4.9 Corollary. Let P1, P2 be reﬂexive. Then

h
⋆
P1◦P2 = h
⋆
P1 h
⋆
P2 .

Haase, Nill, Paffenholz: Lattice Polytopes — 87 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

Proof. In this situation, P := P1 ∗ P2 is also called the free join of P1 and P2. It’s
h
⋆-polynomial is given by the product of those of P1 and P2 (Exercise 6.3). The
origins in P1 and P2 form a special simplex S of P. As remarked in the proof (Exer-
cise 6.4), projecting along the afﬁne span of S does not change the h
⋆-polynomial.
Its image is the reﬂexive polytope P1 ◦ P2. ⊓⊔

6.5 Dilations

One of the ﬁrst theorems about unimodular triangulations was proved in the
early days of toric geometry by Knudsen, Mumford, and Waterman [16]. They
were interested in semi-stable reduction of families of algebraic varieties.

6.5.1 Theorem ([16]). There is a factor c = c(P) ∈ Z>0 such that the dilation c · P
admits a regular unimodular triangulation.

We say that c(P) is a KMW-number of P. The KMW-theorem raises more questions
than it answers, such as:

◃ What is the minimum c(P) for a given polytope P? Is there a c(d) that is a
KMW-number for every polytope of dimension d?
◃ What is the structure of the set of KMW-numbers of a given P? Is it a monoid?
Theorem 6.3.4 implies it is closed under taking multiples of an element, but
it is not clear whether it is closed under taking sums. On the other end, no
polytope P and integer c are known so that c is a KMW-number for P but
c + 1 is not.

For the proof of Theorem 6.5.1 we follow the strategy of the original ingenious
proof [16] (we omit the regularity bit). Compare also [8, §§3.A&3.B].

Proof (Proof of Theorem 6.5.1). The theorem is true for lattice polyhedral com-
plexes: every cell F is a lattice polytope in its own lattice ΛF , and these lattices
are compatible along intersections. In fact, the additional ﬂexibility offered by this
structure is used in the proof. Every triangulation of P carries two distinguished
lattice structures: the one given by the embedding P ⊆ Rd on the one hand, and
the one which declares every simplex to be unimodular on the other.
Starting from a full triangulation of P, the proof proceeds by induction on the
maximal normalized volume V of a cell. If V is a prime number, the different cells
of volume V do not interfere. They can be subdivided independently. But if V is
composite, then this very fact is used to interpolate between the unimodular lat-
tice structure and a multiple of the given one. The two cases of the induction step
are treated in Lemmas 6.5.6 and 6.5.2 below. The proofs occupy the remainder
of this section. ⊓⊔

6.5.1 Composite Volume

For the induction step, we need some preparation. It is convenient to embed
our lattice simplicial complex S on vertices v1, . . . , vN into RN via vi 7→ ei. For
every face F ∈ S this yields a linear map ϕF : ΛF → RN , and we denote ˆΛ the
sum of the images of these lattices. Observe that ϕF (ΛF ) is generated by convex
combinations of unit vectors, and therefore every element has integral coordinate
sum. If vi ∈ F , call xi an F -coordinate of x. In this setting, we can actually dilate
S by a positive integer (and keep the lattice ˆΛ).
For each F ∈ S, the fundamental parallelepiped of F is the half open cube

Π(F ) := {x ∈ RN : xi ∈ [0, 1) if vi ∈ F, and xi = 0 if vi ̸∈ F }.

— 88 — Haase, Nill, Paffenholz: Lattice Polytopes

Unimodular Triangulations (preliminary version of December 7, 2012)

A box point of F is an element of Π(F ) ∩ ˆΛ. It is in the relative interior if all its F -
coordinates are strictly positive. The box points of F represent the elements of the
ﬁnite abelian group (ZN + ϕF (ΛF ))/ZN ; their number, the index [ZN + ϕF (ΛF ) :
ZN ], equals the normalized volume of F .

6.5.2 Lemma. Let V be a composite integer, and suppose that for every lattice sim-
plicial complex S all whose cells have volume less than V there is a factor c ∈ Z>0
such that cS has a unimodular triangulation.
Then the same is true for all lattice simplicial complexes all whose cells have
volume no more than V .

Proof. Let F1, . . . , FM be the volume V faces of S. For each of them choose non-
zero box points mi ∈ Π(Fi) ∩ ˆΛ of order strictly less than V in ˆΛ/ZN . Deﬁne
lattices Λ0 := ZN , Λi := Λi−1 + Zmi for i = 1, . . . , M , and ΛM +1 := ˆΛ. To begin
with, S is unimodular with respect to Λ0. The maximal volume of a simplex of
S with respect to Λ1 is bounded by the index [Λ1 : Λ0] which by choice of m1
is less than V . By induction, there is a c1 ∈ Z>0 so that c1S has a unimodular
triangulation with respect to Λ1. In Λ2, this triangulation can only have simplices
of volume [Λ2 : Λ1] which by choice of m2 is less than V . Continuing this way,
we obtain a ΛM -unimodular triangulation of cM · . . . · c1S. But now, the index
[ΛM +1 : ΛM ] is also less than V . So some cM +1 · . . . · c1S has a ˆΛ-unimodular
triangulation. ⊓⊔

6.5.2 Prime Volume

Throughout the remainder of this section V is a prime number, and S is a lattice
simplicial complex with maximal simplex volume V . The (open) star, star(S; F ),
of a face F of a simplicial complex S is the set of all faces that contain F . The
closed star, star(S; F ), contains additionally all faces of elements of star(S; F ).
The boundary, ∂ star(S; F ), of star(S; F ) is the difference star(S; F ) \ star(S; F ).

6.5.3 Lemma. The set of volume V simplices is a pairwise disjoint union of open
stars of inclusion minimal volume V simplices. Each inclusion minimal volume V
simplex has V − 1 relative interior box points.

Proof. Suppose F ∈ S has volume V , and G is a face of F with a relative interior
box point m. Since V is prime, m generates the group (ZN + ϕF (ΛF ))/ZN . As
all non-G-coordinates of m vanish, the same is true for all multiples of m, and
therefore for all box points of F . ⊓⊔

6.5.4 Lemma. If F ∈ S is an inclusion minimal simplex of volume V , then there is
a c ≤ d so that c · star(S; F ) has a subdivision which induces the standard hyper-
simplicial subdivision on c · ∂ star(S; F ) with the property that all simplices in any
pulling triangulation have volume < V .

Proof. Let m be a box point of F . Set c := ∑
i mi so that m ∈ relint cF . As all
non-F -coordinates of m vanish and all F -coordinates are less than one, we have
c < dim F + 1. Integrality implies c ≤ d. (We could use the symmetry of Π(F ) to
obtain c ≤ ⌈d/2⌉.)
Subdivide the facets of c · ∂ star(S; F ) canonically into hypersimplices. Subdi-
vide c · star(S; F ) into pyramids over these hypersimplices with apex m.
Now, let G be a cell of a pulling triangulation reﬁning this subdivision. Then
G = conv(m, G′) where G′ lives inside cF ′ for some facet F ′ of ∂ star(S; F ). There
is a unique vertex vj of F not in F ′, and the normalized volume of G equals
m j · V < V . ⊓⊔

Haase, Nill, Paffenholz: Lattice Polytopes — 89 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

6.5.5 Lemma. d!S has a triangulation into simplices of volume < V .

Proof. Subdivide every simplex of volume less than V canonically into hypersim-
plices.
For every inclusion minimal simplex F of volume V , choose c and subdivide
c · star(S; F ) as in Lemma 6.5.4. Now, d! · star(S; F ) = d!
c · (c · star(S; F )) has a
canonical subdivision into pyramids over hypersimplices. (Need to say something
about this.) It restricts to the canonical subdivision on the boundary.
Now pull all the lattice points. ⊓⊔

Corollary:

6.5.6 Lemma. Let V be a prime number, and suppose that for every lattice simplicial
complex S all whose cells have volume less than V there is a factor c ∈ Z>0 such that
cS has a unimodular triangulation.
Then the same is true for all lattice simplicial complexes all whose cells have
volume no more than V .

6.6 Problems

6.1 Prove Theorem 6.3.4 by using Theorem 6.3.3.

6.2 Show that a lattice polytope is integrally-closed, if it admits a unimodular
triangulation.

6.3 Let P ⊆ Rn and Q ⊆ Rm be lattice polytopes. Show that the product of their
h
⋆-polynomials equals the h
⋆-polynomial of the convex hull of P × {0} × {0} and
{0} × Q × {1}.

6.4 Use the methods of proof of Theorem 6.4.1 to show that the projection of
a Gorenstein polytope of codegree r along a special simplex of dimension r − 1
yields a reﬂexive polytope with the same h
⋆-polynomial.

— 90 — Haase, Nill, Paffenholz: Lattice Polytopes

Chapter
References

1. Barvinok, A.: Computing the ehrhart polynomial of a convex lattice polytope. Discrete
Comput. Geom. 12(1), 35–48 (1994)
2. Barvinok, A.: A course in convexity, Graduate Studies in Mathematics, vol. 54. American
Mathematical Society, Providence, RI (2002)
3. Barvinok, A.: Integer Points in Polyhedra. European Mathematica Society Lecture Notes
(2008)
4. Barvinok, A.I., Pommersheim, J.E.: An algorithmic theory of lattice points in polyhedra. In:
New perspectives in algebraic combinatorics (Berkeley, CA, 1996–97), pp. 91–147. Cam-
bridge Univ. Press, Cambridge (1999)
5. Batyrev, V.V.: Dual polyhedra and mirror symmetry for Calabi–Yau hypersurfaces in toric
varieties. J. Alg. Geom. 3, 493–535 (1994)
6. Beck, M., Sottile, F.: Irrational proofs for three theorems of Stanley. Eur. J. Comb. 28(1),
403–409 (2007). DOI 10.1016/j.ejc.2005.06.003
7. Betke, U., McMullen, P.: Lattice points in lattice polytopes. Monatsh. Math. 99, 253–265
(1985). DOI 10.1007/BF01312545
8. Bruns, W., Gubeladze, J.: Polytopes, Rings, and K-Theory. Monographs in Mathematics.
Springer-Verlag (2009). XIV, 461 p. 52 illus.
9. Danilov, V.I., Khovanski˘ı, A.G.: Newton polyhedra and an algorithm for computing Hodge–
Deligne numbers. Math. USSR Izvestiya 29(2), 279–298 (1987)
10. De Loera, J.A., Hemmecke, R., Yoshida, R., Tauzer, J.: lattE (2005). http://www.math.
ucdavis.edu/~latte/
11. deLoera, J., Santos, F., Rambau, J.: Triangulations, Algorithms and Computation in Mathe-
matics, vol. 25. Springer (2010)
12. Draisma, J., McAllister, T.B., Nill, B.: Lattice width directions and minkowski’s 3d -theorem
(2009)
13. Erdahl, R.M., Ryshkov, S.S.: On lattice dicing. Eur. J. Comb. 15(5), 459–481 (1994). DOI
10.1006/eujc.1994.1049
14. Grötschel, M., Lovász, L., Schrijver, A.: Geometric algorithms and combinatorial optimiza-
tion, Algorithms and Combinatorics, vol. 2, second edn. Springer-Verlag, Berlin (1993)
15. Hille, L., Skarke, H.: Reﬂexive polytopes in dimension 2 and certain relations in SL2(Z). J.
Algebra Appl. 1(2), 159–173 (2002). DOI 10.1142/S0219498802000124
16. Kempf, G.R., Knudsen, F.F., Mumford, D., Saint-Donat, B.: Toroidal Embeddings I, Lecture
Notes in Mathematics, vol. 339. Springer–Verlag (1973)
17. Köppe, M.: Latte macchiato – an improved version of latte (2007). http://www.math.
uni-magdeburg.de/~mkoeppe/latte/
18. Köppe, M., Verdoolaege, S.: Computing parametric rational generating functions with a
primal barvinok algorithm. Electronic journal of Combinatorics 15 (2008)
19. Lenstra, A.K., Lenstra, H.W., Lovász, L.: Factoring polynomials with rational coefﬁcients.
Math. Ann. 261(4), 515–534 (1982)
20. Ohsugi, H., Hibi, T.: Convex polytopes all of whose reverse lexicographic initial ideals are
squarefree. Proc. Am. Math. Soc. 129(9), 2541–2546 (2001)
21. Poonen, B., Rodriguez-Villegas, F.: Lattice polygons and the number 12. Amer. Math.
Monthly 107(3), 238–250 (2000)
22. Schrijver, A.: Theory of linear and integer programming. Wiley-Interscience Series in Dis-
crete Mathematics. A Wiley-Interscience Publication. Chichester: John Wiley & Sons Ltd.
(1986)
23. Schrijver, A.: Combinatorial optimization. Polyhedra and efﬁciency (3 volumes). Algorithms
and Combinatorics 24. Berlin: Springer. (2003)
24. Scott, P.R.: On convex lattice polygons. Bull. Austral. Math. Soc. 15(3), 395–399 (1976)

— 91 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

25. Stanley, R.P.: Decompositions of rational convex polytopes. Ann. Discrete Math. 6, 333–342
(1980). Combinatorial mathematics, optimal designs and their applications (Proc. Sympos.
Combin. Math. and Optimal Design, Colorado State Univ., Fort Collins, Colo., 1978)
26. Stanley, R.P.: A monotonicity property of h-vectors and h
∗-vectors. European J. Combin.
14(3), 251–258 (1993). DOI 10.1006/eujc.1993.1028. URL http://dx.doi.org/10.
1006/eujc.1993.1028
27. Sullivant, S.: Compressed polytopes and statistical disclosure limitation. Tohoku Math.
J. (2) 58(3), 433–445 (2006). URL http://projecteuclid.org/getRecord?id=
euclid.tmj/1163775139. Preprint arXiv:math.CO/0412535
28. Ziegler, G.M.: Lectures on Polytopes, GTM, vol. 152. Springer–Verlag (1995)

— 92 — Haase, Nill, Paffenholz: Lattice Polytopes

Index

— Symbols —

h
⋆-polynomial . . . . . . . . . . . . 39, 39, 41, 44 f.
PICK’s formula . . . . . . . . . . . . . . . . . . . . . . . . . 21
PICK’s theorem . . . . . . . . . . . . . . . . . . . . . . . . . 21
f-vector . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

— A —

addition property . . . . . . . . . . . . . . . . . . 78, 80
adjacent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
afﬁne combination . . . . . . . . . . . . . . . . . . . . . . 1
algorithm
Barvinok’s ∼ . . . . . . . . . . . . . . . . . . . . . 48, 52
LLL . . . . . . . . . . . . . . . . . . . . 49 f., 52, 54, 56
weakly reduced basis . . . . . . . . . . . . . . . . 55

— B —

Barvinok’s algorithm . . . . . . . . . . . . . . . 48, 52
basis
of a lattice . . . . . . . . . . . . . . . . . . . . . . . . . . 11
beneath . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
beyond . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
Birkhoff polytope . . . . . . . . . . . . . . . . . . . . . . 76
Blichfeldt’s Theorem . . . . . . . . . . . . . . . . . . . 61
boundary complex . . . . . . . . . . . . . . . . . . . . . 30
Brianchon-Gram identity. . . . . . . . . . . . . . .46
Brion
Theorem of ∼. . . . . . . . . . . . . . . . . . . . . . . .49
Brion’s Theorem . . . . . . . . . . . . . . . . . . . 48, 49

— C —

cell
maximal . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
of a polyhedral complex . . . . . . . . . . . . . 30
codegree
of a lattice polytope . . . . . . . . . . . . . . . . . 44
complex
cell of a polyhedral ∼ . . . . . . . . . . . . . . . . 30
dimension of a polyhedral ∼ . . . . . . . . . 30
polyhedral
dimension . . . . . . . . . . . . . . . . . . . . . . . . . 30
facets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
maximal cell . . . . . . . . . . . . . . . . . . . . . . . 30
pure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
subcomplex . . . . . . . . . . . . . . . . . . . . . . . . 30
polyhedral ∼ . . . . . . . . . . . . . . . . . . . . . . . . 30
compressed polytope . . . . . . . . . . . . . . . . . . 84
cone
dual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
face of. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .8
ﬁnitely generated . . . . . . . . . . . . . . . . . . . . . 2
fundamental parallelepiped . . . . . . . . . 31
Gorenstein . . . . . . . . . . . . . . . . . . . . . . . . . . 75
half-open . . . . . . . . . . . . . . . . . . 31, 35 f., 43
homogeneous . . . . . . . . . . . . . . . . . . . . . . . 18
index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
 lineality space . . . . . . . . . . . . . . . . . . . . . . . . 5
minimal proper face . . . . . . . . . . . . . . . . . 10
over a polytope . . . . . . . . . . . . . . . . . . . 6, 37
pointed. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .5
polar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
polyhedral. . . . . . . . . . . . . . . . . . . . . . . . . . . .2
proper face of . . . . . . . . . . . . . . . . . . . . . . . . 8
subdivision . . . . . . . . . . . . . . . . . . . . . . . . . . 31
triangulation . . . . . . . . . . . . . . . . . . . . . . . . 31
cone . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
conic combination . . . . . . . . . . . . . . . . . . . . . . 1
contingency table . . . . . . . . . . . . . . . . . . . . . . 28
convex combination . . . . . . . . . . . . . . . . . . . . 1
coset . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
counting function . . . . . . . . . . . . . . . . 29, 38 f.
covering radius . . . . . . . . . . . . . . . . . . . . . . . . 65

— D —

degree
of a lattice polytope . . . . . . . . . . . . . . . . . 44
determinant
of a lattice . . . . . . . . . . . . . . . . . . . . . . . . . . 15
dilation of a set . . . . . . . . . . . . . . . . . . . . . . . . 29
dimension
of a face . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
of a polyhedral complex . . . . . . . . . . . . . 30
of a polytope . . . . . . . . . . . . . . . . . . . . . . . . . 7
distance function . . . . . . . . . . . . . . . . . . . . . . 14
dual lattice . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11

— E —

edge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
Ehrhart counting function . . . . . . . . 29, 38 f.
Ehrhart polynomial 27, 33, 39, 39, 41, 43,
45
Ehrhart series . . . . . . . . . . . . . . . . . . . . . 37, 39
Ehrhart’s theorem . . . . . . . . . . . . . . . . . . . . . 39
Ehrhart-Macdonald reciprocity . . . . . . . . . 43
extremal ray . . . . . . . . . . . . . . . . . . . . . . . . . . . 10

— F —

face
dimension . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
minimal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 9
minimal proper . . . . . . . . . . . . . . . . . . . . . 10
of a polytope . . . . . . . . . . . . . . . . . . . . . . . . . 8
proper, of a polytope. . . . . . . . . . . . . . . . . .8
face vector . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
facet
special . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
facets
of a polyhedral complex . . . . . . . . . . . . . 30
fan
smooth blow-up . . . . . . . . . . . . . . . . . . . . . 71
far half-open cone . . . . . . . . . . . . . . . . . 31, 36
far half-open parallelepiped . . . . . . . . . . . . 31

— 93 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

Farkas Lemma . . . . . . . . . . . . . . . . . . . . . . . . . . 4
formal Laurent series . . . . . . . . . . . . . . . . . . 34
free sum. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .78
full dimensional . . . . . . . . . . . . . . . . . . . . . . . . 8
fundamental parallelepiped . . . . 31, 35, 49

— G —

Generalized Blichfeldt’s Theorem . . . . . . 63
generic reference point . . . . . . . . . . . . . . . . 31
Gorenstein cone . . . . . . . . . . . . . . . . . . . . . . . 75
Gorenstein polytope . . . . . . . . 69, 74, 76, 77
Gram-Schmidt orthogonalization. . . . . . .53

— H —

half-open cone . . . . . . . . . . . . . . . 31, 35 f., 43
half-open decomposition . . . . . 31, 35 f., 43
half-open parallelepiped . . . . . . . . . . . . . . . 31
half-open simplex. . . . . . . . . . . . . . . . . . . . . .31
half-space
afﬁne. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1
linear . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
Hermite normal form . . . . . . . . . . . . . . . . . . 15
Hilbert basis . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
minimal . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17
homogeneous . . . . . . . . . . . . . . . . . . . . . . . . . 18
hyperplane
afﬁne. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .1
linear . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 1
supporting . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
valid . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8

— I —

implied equality . . . . . . . . . . . . . . . . . . . . . . . . 7
index
of a cone . . . . . . . . . . . . . . . . . . . . . . . . . . . . 49
of a lattice . . . . . . . . . . . . . . . . . . . . . . . . . . 15
inner normal
primitive . . . . . . . . . . . . . . . . . . . . . . . . . . . . 69
integer point generating function 36, 36 f.,
46, 48
integer point series . . . . . . . . . . . . . . . . 35, 36
summable . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
integral polytope . . . . . . . . . . . . . . . . . . . . . . 20
integrally closed . . . . . . . . . . . . . . . . . . . . . . . 86
interior point . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
irredundant. . . . . . . . . . . . . . . . . . . . . . . . . . . . .8

— K —

KMW number . . . . . . . . . . . . . . . . . . . . . . . . . 88
KMW Theorem . . . . . . . . . . . . . . . . . . . . . . . . 88
Knapsack problem . . . . . . . . . . . . . . . . . . . . . 27

— L —

lattice. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .11, 64
basis . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 11
determinant . . . . . . . . . . . . . . . . . . . . . . . . . 15
index . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
 reduced basis . . . . . . . . . . . . . . . . . . . . . . . 53
standard integer ∼ . . . . . . . . . . . . . . . . . . . 11
sublattice . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
transformation . . . . . . . . . . . . . . . . . . . . . . 15
unimodular . . . . . . . . . . . . . . . . . . . . . . . . . 15
weakly reduced basis . . . . . . . . . . . . . . . . 53
lattice isomorphic . . . . . . . . . . . . . . . . . . . . . 20
lattice isomorphism . . . . . . . . . . . . . . . . . . . . 20
lattice polytope . . . . . . . . . . . . . . . . . . . . . . . . 20
codegree . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
compressed . . . . . . . . . . . . . . . . . . . . . . . . . 84
degree . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 44
lattice isomorphic . . . . . . . . . . . . . . . . . . . 20
normalized volume . . . . . . . . . . . . . . 24, 40
unimodularly equivalent. . . . . . . . . . . . .20
lattice transformation . . . . . . . . . . . . . . . . . . 15
Laurent polynomial . . . . . . . . . . . . . . . . . . . . 34
Laurent polynomial ring . . . . . . . . . . . . . . . 34
Laurent series . . . . . . . . . . . . . . . . . . . 34, 35 f.
summable . . . . . . . . . . . . . . . . . . . . . . . . . . . 35
lineality space
of a cone . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
linear combination . . . . . . . . . . . . . . . . . . . . . . 1
LLL . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 50
LLL algorithm . . . . . . . . . . . . . . 49, 52, 54, 56

— M —

minimal face
of a polytope . . . . . . . . . . . . . . . . . . . . . . . . . 9
minimal proper face . . . . . . . . . . . . . . . . . . . 10
Minkowski sum . . . . . . . . . . . . . . . . . . . . . . . . . 5
Minkowski’s First Theorem . . . . . . . . 62, 63
Minkowski’s Second Theorem . . . . . . . . . . 63
Minkowski’s Theorem . . . . . . . . . . . . . . . . . . . 5
mirror symmetry . . . . . . . . . . . . . . . . . . . . . . 69

— N —

near half-open cone . . . . . . . . . . . . . . . 31, 36
near half-open parallelepiped . . . . . . . . . . 31
normal form
Hermite ∼ . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
normalized volume . . . . . . . . . . . . . . . . 24, 40

— P —

packing radius . . . . . . . . . . . . . . . . . . . . . . . . . 64
parallelepiped . . . . . . . . . . . . . . . . . . . . . . . . . 12
fundamental. . . . . . . . . . . . . . . . .31, 35, 49
half-open. . . . . . . . . . . . . . . . . . . . . . . . . . . .31
Pick’s Theorem . . . . . . . . . . . . . . . . . . . . 21, 71
polar polytope . . . . . . . . . . . . . . . . . . . . . . . . . 70
polyhedral complex . . . . . . . . . . . . . . . . . . . . 30
cell . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
dimension. . . . . . . . . . . . . . . . . . . . . . . . . . .30
facets . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
maximal cell . . . . . . . . . . . . . . . . . . . . . . . . 30
pure . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
subcomplex . . . . . . . . . . . . . . . . . . . . . . . . . 30
polynomial
h
⋆ . . . . . . . . . . . . . . . . . . . . . . 39, 39, 41, 44 f.
Ehrhart . . . . . . 27, 33, 39, 39, 41, 43, 45

— 94 — Haase, Nill, Paffenholz: Lattice Polytopes

Index (preliminary version of December 7, 2012)

Laurent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
polynomial ring
Laurent . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 34
polytope. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .6, 6
boundary complex . . . . . . . . . . . . . . . . . . 30
compressed . . . . . . . . . . . . . . . . . . . . . . . . . 84
cone over a . . . . . . . . . . . . . . . . . . . . . . . . . . . 6
dimension . . . . . . . . . . . . . . . . . . . . . . . . . . . . 7
edge . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
extremal ray . . . . . . . . . . . . . . . . . . . . . . . . 10
face of. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .8
free sum . . . . . . . . . . . . . . . . . . . . . . . . . . . . 78
Gorenstein . . . . . . . . . . . . . . . 69, 74, 76, 77
integral . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
integrally closed . . . . . . . . . . . . . . . . . . . . . 86
interior point . . . . . . . . . . . . . . . . . . . . . . . . . 8
lattice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 20
minimal face . . . . . . . . . . . . . . . . . . . . . . . . . 9
normalized volume . . . . . . . . . . . . . . 24, 40
polar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 70
proper face of . . . . . . . . . . . . . . . . . . . . . . . . 8
reﬂexive . . . . . . . . . 69, 70, 70 ff., 74, 77 f.
special simplex . . . . . . . . . . . . . . . . . . . . . . 86
subdivision . . . . . . . . . . . . . . . . . . . . . . . . . . 31
triangulation . . . . . . . . . . . . . . . . . . . . . . . . 31
vertex of . . . . . . . . . . . . . . . . . . . . . . . . . . . . 10
primitive . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 13
primitive inner normal . . . . . . . . . . . . . . . . . 69
pulling reﬁnement . . . . . . . . . . . . . . . . . . . . . 84

— R —

rational subspace . . . . . . . . . . . . . . . . . . . . . . 12
reduced basis . . . . . . . . . . . . . . . . . . . . . . . . . . 53
redundant . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 8
reﬂexive polytope . . 69, 70, 70 ff., 74, 77 f.
addition property . . . . . . . . . . . . . . . 78, 80
regular subdivision . . . . . . . . . . . . . . . . . . . . 83

— S —

Scott’s theorem . . . . . . . . . . . . . . . . . . . . . . . . 22
series
Ehrhart . . . . . . . . . . . . . . . . . . . . . . . . . 37, 39
formal Laurent . . . . . . . . . . . . . . . . . . . . . . 34
Laurent . . . . . . . . . . . . . . . . . . . . . . . 34, 35 f.
summable . . . . . . . . . . . . . . . . . . . . . . . . . 35
set
dual . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
polar . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
simplex
half-open. . . . . . . . . . . . . . . . . . . . . . . . . . . .31
standard . . . . . . . . . . . . . . . . . . . . . . . . 24, 29
unimodular . . . . . . . . . . . . . . . . . . . . . . . . . 24
unit . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
smooth blow-up
of a fan . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 71
special facet . . . . . . . . . . . . . . . . . . . . . . . . . . . 80
special simplex . . . . . . . . . . . . . . . . . . . . . . . . 86
standard simplex . . . . . . . . . . . . . . . . . . 24, 29
standard triangulation of dilated simplex
86
Stanley Reciprocity . . . . . . . . . . . . . . . . . . . . 43
 Stanley’s Monotonicity theorem . . . . . . . . 41
subcomplex . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
subdivision . . . . . . . . . . . . . . . . . . . . . . . . . . . . 31
regular . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 83
trivial . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 30
sublattice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
successive minimum . . . . . . . . . . . . . . . . . . . 62
summable . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 35

— T —

Theorem
Generalized Blichfeldt’s ∼ . . . . . . . . . . . . 63
KMW . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
Minkowski’s First ∼ . . . . . . . . . . . . . . 62, 63
Minkowski’s Second ∼ . . . . . . . . . . . . . . . 63
of Brianchon-Gram . . . . . . . . . . . . . . . . . . 46
of Brion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
of Minkowski . . . . . . . . . . . . . . . . . . . . . . . . . 5
of Pick . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
of Weyl . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 3
Pick’s ∼. . . . . . . . . . . . . . . . . . . . . . . . . . . . . .71
Stanley’s Monotonicity . . . . . . . . . . . . . . 41
van der Corput’s ∼ . . . . . . . . . . . . . . . . . . . 63
Weyl-Minkowski . . . . . . . . . . . . . . . . . . . . . . 2
theorem
PICK’s . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 21
Blichfeldt . . . . . . . . . . . . . . . . . . . . . . . . . . . 61
Ehrhart-Macdonald . . . . . . . . . . . . . . . . . . 43
ﬂatness . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67
of Ehrhart . . . . . . . . . . . . . . . . . . . . . . . . . . . 39
Scott’s . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
Stanley Reciprocity . . . . . . . . . . . . . . . . . . 43
Stanley’s nonnegativity∼ . . . . . . . . . . . . . 40
Theorem of Brianchon-Gram . . . . . . . . . . . 46
Theorem of Brion . . . . . . . . . . . . . . . . . . . . . . 49
transformation
lattice . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
unimodular . . . . . . . . . . . . . . . . . . . . . . . . . 15
triangulation . . . . . . . . . . . . . . . . . . . . . . 31, 36
pulling reﬁnement. . . . . . . . . . . . . . . . . . .84
standard of dilated simplex . . . . . . . . . . 86
unimodular . . . . . . . . . . . . . . . . . . . . . . . . . 83
without new vertices . . . . . . . . . . . . . . . . 31
trivial subdivision. . . . . . . . . . . . . . . . . . . . . .30

— U —

unimodular
of a lattice . . . . . . . . . . . . . . . . . . . . . . . . . . 15
triangulation . . . . . . . . . . . . . . . . . . . . . . . . 83
unimodular simplex . . . . . . . . . . . . . . . . . . . 24
unimodular transformation . . . . . . . . . . . . 15
unimodularly equivalent . . . . . . . . . . . . . . . 20
unit simplex . . . . . . . . . . . . . . . . . . . . . . . . . . . 29
university degrees . . . . . . . . . . . . . . . . . . . . . 28

— V —

vertex
of a polytope . . . . . . . . . . . . . . . . . . . . . . . . 10
vertex-edge graph . . . . . . . . . . . . . . . . . . . . . 79
volume

Haase, Nill, Paffenholz: Lattice Polytopes — 95 —

Lecture Notes Fall School “Polyhedral Combinatorics” — Darmstadt 2012 (preliminary version of December 7, 2012)

normalized . . . . . . . . . . . . . . . . . . . . . . 24, 40

— W —

weakly reduced basis . . . . . . . . . . . . . . 53, 55
Weyl’s Theorem . . . . . . . . . . . . . . . . . . . . . . . . . 3
Weyl-Minkowski Duality . . . . . . . . . . . . . . . . 2
width . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 67

— 96 — Haase, Nill, Paffenholz: Lattice Polytopes

Name Index

— A —

Athanasiadis. . . . . . . . . . . . . . . . . . . . . . . . . . .86

— B —

Barvinok . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48
Betke . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
Blichfeldt . . . . . . . . . . . . . . . . . . . . . . . . . . 61, 63
Brianchon . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46
Brion . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 48 f.
Bruns . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86

— E —

Ehrhart . . . . . . . . . . . . . . . . . . . . 29, 37, 39, 43

— F —

Fourier . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2

— G —

Gram . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 46

— H —

Hermite . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 15
Hibi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85
Hilbert . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 17

— K —

Knudson . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88

— L —

Lenstra, Arjen. . . . . . . . . . . . . . . . . .49, 52, 54
Lenstra, Hendrik . . . . . . . . . . . . . . . 49, 52, 54
Lovász, László . . . . . . . . . . . . . . . . . 49, 52, 54

— M —

Macdonald . . . . . . . . . . . . . . . . . . . . . . . . . . . . 43
McMullen . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 87
Minkowski . . . . . . . . . . . . . . . . . . . . . . . . 2, 62 f.
Motzkin . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2
Mumford . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88

— O —

Oshugi . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85

— P —

Pick. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .21, 71
Pommersheim . . . . . . . . . . . . . . . . . . . . . . . . . 48
 — R —

Römer . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 86

— S —

Santos. . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . .85
Scott . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 22
Stanley . . . . . . . . . . . . . . . . . . . . . . 40 f., 43, 84
Sullivant . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 85

— V —

van der Corput . . . . . . . . . . . . . . . . . . . . . . . . 63

— W —

Waterman . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 88
Weyl . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 2

— 97 —
