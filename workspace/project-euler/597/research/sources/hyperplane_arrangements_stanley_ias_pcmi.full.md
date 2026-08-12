<!-- source: https://static.ias.edu/pcmi/2004/program/Stanleynotes.pdf | converted from PDF -->

An Introduction to Hyperplane
Arrangements

Richard P. Stanley

Contents

An Introduction to Hyperplane Arrangements 1

Lecture 1. Basic deﬁnitions, the intersection poset and the characteristic
polynomial 2
Exercises 12

Lecture 2. Properties of the intersection poset and graphical arrangements 13
Exercises 30

Lecture 3. Matroids and geometric lattices 31
Exercises 39

Lecture 4. Broken circuits, modular elements, and supersolvability 41
Exercises 56

Lecture 5. Finite ﬁelds 59
Exercises 78

Bibliography 85

3

IAS/Park City Mathematics Series
Volume 00, 0000
 An Introduction to Hyperplane
Arrangements

July 7, 2004

The author was supported in part by NSF grant DMS-9988459. He is grateful to Lauren Williams
for her careful reading of the original manuscript and many helpful suggestions, and to H´el`ene
Barcelo for a number of additional suggestions.
 c⃝0000 American Mathematical Society

1

2 , HYPERPLANE ARRANGEMENTS
 LECTURE 1
Basic deﬁnitions, the intersection poset and the
characteristic polynomial

1.1. Basic deﬁnitions

The following notation is used throughout for certain sets of numbers:

N nonnegative integers
P positive integers
Z integers
Q rational numbers
R real numbers
R+ positive real numbers
C complex numbers
[m] the set {1, 2, . . . , m} when m ∈ N

We also write [tk]χ(t) for the coeﬃcient of tk in the polynomial or power series χ(t).
For instance, [t2](1 + t)4 = 6.
A ﬁnite hyperplane arrangement A is a ﬁnite set of aﬃne hyperplanes in some
vector space V ∼ K n, where K is a ﬁeld. We will not consider inﬁnite hyperplane
arrangements or arrangements of general subspaces or other objects (though they
have many interesting properties), so we will simply use the term arrangement for
a ﬁnite hyperplane arrangement. Most often we will take K = R, but as we will see
even if we’re only interested in this case it is useful to consider other ﬁelds as well.
To make sure that the deﬁnition of a hyperplane arrangement is clear, we deﬁne a
linear hyperplane to be an (n − 1)-dimensional subspace H of V , i.e.,

H = {v ∈ V : α · v = 0},

where α is a ﬁxed nonzero vector in V and α · v is the usual dot product:

(α1, . . . , αn) · (v1, . . . , vn) = ∑ αivi.

An aﬃne hyperplane is a translate J of a linear hyperplane, i.e.,

J = {v ∈ V : α · v = β},

where α and β are ﬁxed vectors in V with α ̸= 0.
If the equations of the hyperplanes of A are given by L1(x) = a1, . . . , Lm(x) =
am, where x = (x1, . . . , xn), then we call the polynomial

QA(x) = (L1(x) − a1) · · · (Lm(x) − am)

the deﬁning polynomial of A. It is often convenient to specify an arrangement
by its deﬁning polynomial. For instance, the arrangement A consisting of the n
coordinate hyperplanes has QA(x) = x1x2 · · · xn.
The rank rank(A) of an arrangement A in V is the dimension of the space
spanned by the normals to the hyperplanes in A. We say that A is essential if
rank(A) = n. If rank(A) = r then we can ﬁnd an r-dimensional subspace W of V
such that

(1) codimW (H ∩ W ) = 1

LECTURE 1. BASIC DEFINITIONS 3

for all H ∈ A. In other words, H ∩ W is a hyperplane of W , so the set AW :=
{H ∩W : H ∈ A} is an essential arrangement in W . Moreover, the arrangements A
and AW are “essentially the same,” meaning in particular that they have the same
intersection poset (as deﬁned in Deﬁnition 1.1). Let us call AW the essentialization
of A, denoted ess(A). When K = R we can take W to consist of the space spanned
by the normals to the hyperplanes in A. The arrangement A is obtained from
AW by “stretching” the hyperplane H ∩ W ∈ AW orthogonally to H. Thus if
W ⊥ denotes the orthogonal complement to W in V , then H ′ ∈ AW if and only if
H ′ ⊕ W ⊥ ∈ A.

Example 1.1. Let A consist of the lines x = a1, . . . , x = ak in K 2 (with coordinates
x and y). Then we can take W to be the x-axis, and ess(A) consists of the points
x = a1, . . . , x = ak in K.

Now let K = R. A region of an arrangement A is a connected component of
the complement X of the hyperplanes:

X = Rn − ⋃

H∈A H.

Let R(A) denote the set of regions of A, and let

r(A) = #R(A),

the number of regions. For instance, the arrangement A shown below has r(A) = 14.

It is a simple exercise to show that every region R ∈ R(A) is open and convex
(continuing to assume K = R), and hence homeomorphic to the interior of an n-
dimensional ball Bn (Exercise 1). Note that if W is the subspace of V spanned by
the normals to the hyperplanes in A, then R ∈ R(A) if and only if R ∩W ∈ R(AW ).
We say that a region R ∈ R(A) is relatively bounded if R ∩ W is bounded. If A
is essential, then relatively bounded is the same as bounded. We write b(A) for
the number of relatively bounded regions of A. For instance, in Example 1.1 take
K = R and a1 < a2 < · · · < ak. Then the relatively bounded regions are the
regions ai < x < ai+1, 1 ≤ i ≤ k − 1. In ess(A) they become the (bounded) open
intervals (ai, ai+1). There are also two regions of A that are not relatively bounded,
viz., x < a1 and x > ak.
A (closed) half-space is a set {x ∈ Rn : x · α ≥ c} for some α ∈ Rn, c ∈ R. If
H is a hyperplane in Rn, then the complement Rn − H has two (open) components
whose closures are half-spaces. It follows that the closure ¯R of a region R of A is

4 , HYPERPLANE ARRANGEMENTS

a ﬁnite intersection of half-spaces, i.e., a (convex) polyhedron (of dimension n). A
bounded polyhedron is called a (convex) polytope. Thus if R (or ¯R) is bounded,
then ¯R is a polytope (of dimension n).
An arrangement A is in general position if

{H1, . . . , Hp} ⊆ A, p ≤ n ⇒ dim(H1 ∩ · · · ∩ Hp) = n − p

{H1, . . . , Hp} ⊆ A, p > n ⇒ H1 ∩ · · · ∩ Hp = ∅.

For instance, if n = 2 then a set of lines is in general position if no two are parallel
and no three meet at a point.
Let us consider some interesting examples of arrangements that will anticipate
some later material.

Example 1.2. Let Am consist of m lines in general position in R2. We can compute
r(Am) using the sweep hyperplane method. Add a L line to Ak (with AK ∪ {L} in
general position). When we travel along L from one end (at inﬁnity) to the other,
every time we intersect a line in Ak we create a new region, and we create one new
region at the end. Before we add any lines we have one region (all of R2). Hence

r(Am) = #intersections + #lines + 1

= (m
2
 ) + m + 1.

Example 1.3. The braid arrangement Bn in K n consists of the hyperplanes

Bn : xi − xj = 0, 1 ≤ i < j ≤ n.

Thus Bn has (n
2) hyperplanes. To count the number of regions when K = R, note
that specifying which side of the hyperplane xi − xj = 0 a point (a1, . . . , an) lies
on is equivalent to specifying whether ai < aj or ai > aj. Hence the number of
regions is the number of ways that we can specify whether ai < aj or ai > aj for
1 ≤ i < j ≤ n. Such a speciﬁcation is given by imposing a linear order on the
ai’s. In other words, for each permutation w ∈ Sn (the symmetric group of all
permutations of 1, 2, . . . , n), there corresponds a region Rw of Bn given by

Rw = {(a1, . . . , an) ∈ Rn : aw(1) > aw(2) > · · · > aw(n)}.

Hence r(Bn) = n!. Rarely is it so easy to compute the number of regions!
Note that the braid arrangement Bn is not essential; indeed, rank(Bn) = n − 1.
When char(K) ̸= 2 the space W ⊆ K n of equation (1) can be taken to be

W = {(a1, . . . , an) ∈ K n : a1 + · · · + an = 0}.

The braid arrangement has a number of “deformations” of considerable interest.
We will just deﬁne some of them now and discuss them further later. All these
arrangements lie in K n, and in all of them we take 1 ≤ i < j ≤ n. The reader who
likes a challenge can try to compute their number of regions when K = R. (Some
are much easier than others.)
• generic braid arrangement: xi = xj + aij, where the aij’s are “generic”
(e.g., linearly independent over the prime ﬁeld, so K has to be “suﬃciently
large”). The precise deﬁnition of “generic” will be given later. (The prime
ﬁeld of K is its smallest subﬁeld, isomorphic to either Q or Z/pZ for some
prime p.)
• semigeneric braid arrangement: xi −xj = ai, where the ai’s are “generic.”

LECTURE 1. BASIC DEFINITIONS 5

• Shi arrangement: xi − xj = 0, 1 (so n(n − 1) hyperplanes in all).
• Linial arrangement: xi − xj = 1.
• Catalan arrangement: xi − xj = −1, 0, 1.
• semiorder arrangement: xi − xj = −1, 1.
• threshold arrangement: xi + xj = 0 (not really a deformation of the braid
arrangement, but closely related).

An arrangement A is central if ⋂H∈A H ̸= ∅. Equivalently, A is a translate
of a linear arrangement (an arrangement of linear hyperplanes, i.e., hyperplanes
passing through the origin). Many other writers call an arrangement central, rather
than linear, if 0 ∈ ⋂
H∈A H. If A is central with X = ⋂
H∈A H, then rank(A) =
codim(X). If A is central, then note also that b(A) = 0 [why?].
There are two useful arrangements closely related to a given arrangement A.
If A is a linear arrangement in K n, then projectivize A by choosing some H ∈ A
to be the hyperplane at inﬁnity in projective space P n−1
K . Thus if we regard

P n−1
K = {(x1, . . . , xn) : xi ∈ K, not all xi = 0}/ ∼,

where u ∼ v if u = αv for some 0 ̸= α ∈ K, then

H = ({(x1, . . . , xn−1, 0) : xi ∈ K, not all xi = 0}/ ∼) ∼ P n−2
K .

The remaining hyperplanes in A then correspond to “ﬁnite” (i.e., not at inﬁnity)
projective hyperplanes in P n−1
K . This gives an arrangement proj(A) of hyperplanes
in P n−1
K . When K = R, the two regions R and −R of A become identiﬁed in
proj(A). Hence r(proj(A)) = 1
2 r(A). When n = 3, we can draw P 2
R as a disk with
antipodal boundary points identiﬁed. The circumference of the disk represents the
hyperplane at inﬁnity. This provides a good way to visualize three-dimensional real
linear arrangements. For instance, if A consists of the three coordinate hyperplanes
x1 = 0, x2 = 0, and x3 = 0, then a projective drawing is given by

2 1 3

The line labelled i is the projectivization of the hyperplane xi = 0. The hyperplane
at inﬁnity is x3 = 0. There are four regions, so r(A) = 8. To draw the incidences
among all eight regions of A, simply “reﬂect” the interior of the disk to the exterior:

6 , HYPERPLANE ARRANGEMENTS

12

23 24

34 14
13

Figure 1. A projectivization of the braid arrangement B4

2 1 3
 1

2

Regarding this diagram as a planar graph, the dual graph is the 3-cube (i.e., the
vertices and edges of a three-dimensional cube) [why?].
For a more complicated example of projectivization, Figure 1 shows proj(B4)
(where we regard B4 as a three-dimensional arrangement contained in the hyper-
plane x1 + x2 + x3 + x4 = 0 of R4), with the hyperplane xi = xj labelled ij, and
with x1 = x4 as the hyperplane at inﬁnity.

LECTURE 1. BASIC DEFINITIONS 7

We now deﬁne an operation which is “inverse” to projectivization. Let A be
an (aﬃne) arrangement in K n, given by the equations

L1(x) = a1, . . . , Lm(x) = am.

Introduce a new coordinate y, and deﬁne a central arrangement cA (the cone over
A) in K n × K = K n+1 by the equations

L1(x) = a1y, . . . , Lm(x) = amy, y = 0.

For instance, let A be the arrangement in R1 given by x = −1, x = 2, and x = 3.
The following ﬁgure should explain why cA is called a cone.

−1 3
2

It is easy to see that when K = R, we have r(cA) = 2r(A). In general, cA has
the “same combinatorics as A, times 2.” See Exercise 7.

1.2. The intersection poset

Recall that a poset (short for partially ordered set) is a set P and a relation ≤
satisfying the following axioms (for all x, y, z ∈ P ):
(P1) (reﬂexivity) x ≤ x
(P2) (symmetry) If x ≤ y then y ≤ x.
(P3) (transitivity) If x ≤ y and y ≤ z, then x ≤ z.
Obvious notation such as x < y for x ≤ y and x ̸= y, and y ≥ x for x ≤ y will be
used throughout. If x ≤ y in P , then the (closed) interval [x, y] is deﬁned by

[x, y] = {z ∈ P : x ≤ z ≤ y}.

Note that the empty set ∅ is not a closed interval. For basic information on posets
not covered here, see [18].

Deﬁnition 1.1. Let A be an arrangement in V , and let L(A) be the set of all
nonempty intersections of hyperplanes in L(A), including V itself as the intersection
over the empty set. Deﬁne x ≤ y in L(A) if x ⊇ y (as subsets of V ). In other words,
L(A) is partially ordered by reverse inclusion. We call L(A) the intersection poset
of A.

Note. The primary reason for ordering intersections by reverse inclusion rather
than ordinary inclusion is Proposition 3.8. We don’t want to alter the well-established
deﬁnition of a geometric lattice or to refer constantly to “dual geometric lattices.”
The element V ∈ L(A) satisﬁes x ≥ V for all x ∈ L(A). In general, if P is a
poset then we denote by ˆ an element (necessarily unique) such that x ≥ ˆ for all

8 , HYPERPLANE ARRANGEMENTS

Figure 2. Examples of intersection posets

x ∈ P . We say that y covers x in a poset P , denoted x ⋖ y, if x < y and no z ∈ P
satisﬁes x < z < y. Every ﬁnite poset is determined by its cover relations. The
(Hasse) diagram of a ﬁnite poset is obtained by drawing the elements of P as dots,
with x drawn lower than y if x < y, and with an edge between x and y if x ⋖ y.
Figure 2 illustrates four arrangements A in R2, with (the diagram of) L(A) drawn
below A.
A chain of length k in a poset P is a set x0 < x1 < · · · < xk of elements of
P . The chain is saturated if x0 ⋖ x1 ⋖ · · · ⋖ xk. We say that P is graded of rank
n if every maximal chain of P has length n. In this case P has a rank function
rk : P → N deﬁned by:

• rk(x) = 0 if x is a minimal element of P .
• rk(y) = rk(x) + 1 if x ⋖ y in P .

If x < y in a graded poset P then we write rk(x, y) = rk(y) − rk(x), the length
of the interval [x, y]. Note that we use the notation rank(A) for the rank of an
arrangement A but rk for the rank function of a graded poset.

Proposition 1.1. Let A be an arrangement in a vector space V ∼ K n. Then the
intersection poset L(A) is graded of rank equal to rank(A). The rank function of
L(A) is given by
 rk(x) = codim(x) = n − dim(x),

where dim(x) is the dimension of x as an aﬃne subspace of V .

Proof. Since L(A) has a unique minimal element ˆ = V , it suﬃces to show that
(a) if x⋖y in L(A) then dim(x)−dim(y) = 1, and (b) all maximal elements of L(A)
have dimension n − rank(A). By linear algebra, if H is a hyperplane and x an aﬃne
subspace, then H ∩ x = x or dim(x) − dim(H ∩ x) = 1, so (a) follows. Now suppose
that x has the largest codimension of any element of L(A), say codim(x) = d. Thus
x is an intersection of d linearly independent hyperplanes (i.e., their normals are
linearly independent) H1, . . . , Hd in A. Let y ∈ L(A) with e = codim(y) < d. Thus
y is an intersection of e hyperplanes, so some Hi (1 ≤ i ≤ d) is linearly independent
from them. Then y ∩ Hi ̸= ∅ and codim(y ∩ Hi) > codim(y). Hence y is not a
maximal element of L(A), proving (b). □

LECTURE 1. BASIC DEFINITIONS 9

1

−1 −1 −1

112
 −2

−1
 1

Figure 3. An intersection poset and M¨obius function values

1.3. The characteristic polynomial

A poset P is locally ﬁnite if every interval [x, y] is ﬁnite. Let Int(P ) denote the
set of all closed intervals of P . For a function f : Int(P ) → Z, write f (x, y) for
f ([x, y]). We now come to a fundamental invariant of locally ﬁnite posets.

Deﬁnition 1.2. Let P be a locally ﬁnite poset. Deﬁne a function µ = µP :
Int(P ) → Z, called the M¨obius function of P , by the conditions:

µ(x, x) = 1, for all x ∈ P

µ(x, y) = − ∑

x≤z<y µ(x, z), for all x < y in P.(2)
 This second condition can also be written
∑

x≤z≤y µ(x, z) = 0, for all x < y in P.

If P has a ˆ, then we write µ(x) = µ(ˆ, x). Figure 3 shows the intersection poset
L of the arrangement A in K 3 (for any ﬁeld K) deﬁned by QA(x) = xyz(x + y),
together with the value µ(x) for all x ∈ L.
A important application of the M¨obius function is the M¨obius inversion for-
mula. The best way to understand this result (though it does have a simple direct
proof) requires the machinery of incidence algebras. Let I(P ) denote the vector
space of all functions f : Int(P ) → Q. Write f (x, y) for f ([x, y]). For f, g ∈ I(P ),
deﬁne the product f g ∈ I(P ) by

f g(x, y) = ∑

x≤z≤y f (x, z)g(z, y).

It is easy to see that this product makes I(P ) an associative Q-algebra, with mul-
tiplicative identity δ given by

δ(x, y) = { 1, x = y
0, x < y.

Deﬁne the zeta function ζ ∈ I(P ) of P by ζ(x, y) = 1 for all x ≤ y in P . Note that
the M¨obius function µ is an element of I(P ). The deﬁnition of µ (Deﬁnition 1.2) is

10 , HYPERPLANE ARRANGEMENTS

equivalent to the relation µζ = δ in I(P ). In any ﬁnite-dimensional algebra over a
ﬁeld, one-sided inverses are two-sided inverses, so µ = ζ −1 in I(P ).

Theorem 1.1. Let P be a ﬁnite poset with M¨obius function µ, and let f, g : P → K.
Then the following two conditions are equivalent:

f (x) = ∑

y≥x g(y), for all x ∈ P

g(x) = ∑

y≥x µ(x, y)f (y), for all x ∈ P.

Proof. The set K P of all functions P → K forms a vector space on which I(P )
acts (on the left) as an algebra of linear transformations by

(ξf )(x) = ∑

y≥x ξ(x, y)f (y),

where f ∈ K P and ξ ∈ I(P ). The M¨obius inversion formula is then nothing but
the statement ζf = g ⇔ f = µg.
 □
We now come to the main concept of this section.

Deﬁnition 1.3. The characteristic polynomial χA(t) of the arrangement A is de-
ﬁned by

(3) χA(t) = ∑

x∈L(A) µ(x)tdim(x).

For instance, if A is the arrangement of Figure 3, then

χA(t) = t3 − 4t2 + 5t − 2 = (t − 1)2(t − 2).

Note that we have immediately from the deﬁnition of χA(t), where A is in K n,
that χA(t) = tn − (#A)tn−1 + · · · .

Example 1.4. Consider the coordinate hyperplane arrangement A with deﬁning
polynomial QA(x) = x1x2 · · · xn. Every subset of the hyperplanes in A has a
diﬀerent nonempty intersection, so L(A) is isomorphic to the boolean algebra Bn of
all subsets of [n] = {1, 2, . . . , n}, ordered by inclusion.

Proposition 1.2. Let A be given by the above example. Then χA(t) = (t − 1)n.

Proof. The computation of the M¨obius function of a boolean algebra is a standard
result in enumerative combinatorics with many proofs. We will give here a naive
proof from ﬁrst principles. Let y ∈ L(A), r(y) = k. We claim that

(4) µ(y) = (−1)k.

The assertion is clearly true for rk(y) = 0, when y = ˆ. Now let y > ˆ We need to
show that

(5) ∑

x≤y(−1)rk(x) = 0.

LECTURE 1. BASIC DEFINITIONS 11

The number of x such that x ≤ y and rk(x) = i is (k
i), so (5) is equivalent to the
well-known identity (easily proved by substituting q = −1 in the binomial expansion
of (q + 1)k) ∑k=0(−1)i(k
i) = 0 for k > 0. □

12 , HYPERPLANE ARRANGEMENTS

Exercises
We will (subjectively) indicate the diﬃculty level of each problem as follows:

[1] easy: most students should be able to solve it
[2] moderately diﬃcult: many students should be able to solve it
[3] diﬃcult: a few students should be able to solve it
[4] horrendous: no students should be able to solve it (without already knowing how)
[5] unsolved.

Further gradations are indicated by + and −. Thus a [3–] problem is about the
most diﬃcult that makes a reasonable homework exercise, and a [5–] problem is an
unsolved problem that has received little attention and may not be too diﬃcult.
Note. Unless explicitly stated otherwise, all graphs, posets, lattices, etc., are
assumed to be ﬁnite.
(1) [2] Show that every region R of an arrangement A in Rn is an open convex set.
Deduce that R is homeomorphic to the interior of an n-dimensional ball.
(2) [1+] Let A be an arrangement and ess(A) its essentialization. Show that

trk(ess(A))χA(t) = trk(A)χess(A)(t).

(3) [2+] Let A be the arrangement in Rn with equations

x1 = x2, x2 = x3, . . . , xn−1 = xn, xn = x1.

Compute the characteristic polynomial χA(t), and compute the number r(A) of
regions of A.
(4) [2+] Let A be an arrangement in Rn with m hyperplanes. Find the maximum
possible number f (n, m) of regions of A.
(5) [2] Let A be an arrangement in the n-dimensional vector space V whose normals
span a subspace W , and let B be another arrangement in V whose normals span
a subspace Y . Suppose that W ∩ Y = {0}. Show that

χA∪B(t) = t−nχA(t)χB(t).

(6) [2] Let A be an arrangment in a vector space V . Suppose that χA(t) is divisible
by tk but not tk+1. Show that rk(A) = n − k.
(7) [2+] Show that for any arrangement A, we have χcA(t) = (t − 1)χA(t), where
cA denotes the cone over A.
(8) Let A be an essential arrangement in Rn. Let Γ be the union of the bounded
faces of A.
(a) [3] Show that Γ is contractible.
(b) [2] Show that Γ need not be homeomorphic to a closed ball.
(c) [2+] Show that Γ need not be starshaped.
(d) [5] Is Γ pure? I.e., do all maximal faces of Γ have the same dimension?
(e) [5] Suppose that A is in general position. Is Γ homeomorphic to an n-
dimensional closed ball?
 LECTURE 2
Properties of the intersection poset and graphical
arrangements

2.1. Properties of the intersection poset

Let A be an arrangement in the vector space V . A subarrangement of A is a
subset B ⊆ A. Thus B is also an arrangement in V . If x ∈ L(A), deﬁne the
subarrangement Ax ⊆ A by

(6) Ax = {H ∈ A : x ⊆ H}.

Also deﬁne an arrangement Ax in the aﬃne subspace x ∈ L(A) by

Ax = {x ∩ H ̸= ∅ : H ∈ A − Ax}.

Note that if x ∈ L(A), then

(7) L(Ax) ∼ Vx := {y ∈ L(A) : y ≥ x}.
 A

xA
 H
A

x H

Choose H0 ∈ A. Let A′ = A − {H0} and A′′ = AH0. We call (A, A′, A′′) a
triple of arrangements with distinguished hyperplane H0.

13

14 , HYPERPLANE ARRANGEMENTS

A"
 A’
A
 H0

The main goal of this section is to give a formula in terms of χA(t) for r(A)
and b(A) when K = R (Theorem 2.5). We ﬁrst establish recurrences for these two
quantities.

Lemma 2.1. Let (A, A′, A′′) be a triple of real arrangements with distinguished
hyperplane H0. Then

r(A) = r(A′) + r(A′′)

b(A) = { b(A′) + b(A′′), if rank(A) = rank(A′)
0, if rank(A) = rank(A′) + 1.

Note. If rank(A) = rank(A′), then also rank(A) = 1 + rank(A′′). The ﬁgure
below illustrates the situation when rank(A) = rank(A′) + 1.

0H

Proof. Note that r(A) equals r(A′) plus the number of regions of A′ cut into two
regions by H0. Let R′ be such a region of A′. Then R′ ∩ H0 ∈ R(A′′). Conversely,
if R′′ ∈ R(A′′) then points near R′′ on either side of H0 belong to the same region
R′ ∈ R(A′), since any H ∈ R(A′) separating them would intersect R′′. Thus R′ is
cut in two by H0. We have established a bijection between regions of A′ cut into
two by H0 and regions of A′′, establishing the ﬁrst recurrence.
The second recurrence is proved analogously; the details are omitted. □
We now come to the fundamental recursive property of the characteristic poly-
nomial. 2.2. (Deletion-Restriction) Let (A, A′, A′′) be a triple of real arrange-
ments. Then χA(t) = χA′ (t) − χA′′ (t).

LECTURE 2. PROPERTIES OF THE INTERSECTION POSET 15

Figure 1. Two non-lattices

For the proof of this lemma, we will need some tools. (A more elementary proof
could be given, but the tools will be useful later.)
Let P be a poset. An upper bound of x, y ∈ P is an element z ∈ P satisfying
z ≥ x and z ≥ y. A least upper bound or join of x and y, denoted x ∨ y, is an upper
bound z such that z ≤ z′ for all upper bounds z′. Clearly if x ∨ y exists, then it
is unique. Similarly deﬁne a lower bound of x and y, and a greatest lower bound
or meet, denoted x ∧ y. A lattice is a poset L for which any two elements have a
meet and join. A meet-semilattice is a poset P for which any two elements have
a meet. Dually, a join-semilattice is a poset P for which any two elements have a
join. Figure 1 shows two non-lattices, with a pair of elements circled which don’t
have a join.

Lemma 2.3. A ﬁnite meet-semilattice L with a unique maximal element ˆ is a
lattice. Dually, a ﬁnite join-semilattice L with a unique minimal element ˆ is a
lattice.

Proof. Let L be a ﬁnite meet-semilattice. If x, y ∈ L then the set of upper bounds
of x, y is nonempty since ˆ is an upper bound. Hence

x ∨ y = ⋀

z≥x
z≥y
 z.

The statement for join-semilattices is by “duality,” i.e., interchanging ≤ with ≥,
and ∧ with ∨. □
The reader should check that Lemma 2.3 need not hold for inﬁnite semilattices.

Proposition 2.3. Let A be an arrangement. Then L(A) is a meet-semilattice. In
particular, every interval [x, y] of L(A) is a lattice. Moreover, L(A) is a lattice if
and only if A is central.

Proof. If ⋂H∈A H = ∅, then adjoin ∅ to L(A) as the unique maximal element,
obtaining the augmented intersection poset L′(A). In L′(A) it is clear that x ∨ y =
x∩y. Hence L′(A) is a join-semilattice. Since it has a ˆ it is a lattice by Lemma 2.3.

16 , HYPERPLANE ARRANGEMENTS

Since L(A) = L′(A) or L(A) = L′(A) − {ˆ}, it follows that L(A) is always a meet-
semilattice, and is a lattice if A is central. If A isn’t central, then ⋁
x∈L(A) x does
not exist, so L(A) is not a lattice. □
We now come to a basic formula for the M¨obius function of a lattice.

Theorem 2.2. (the Cross-Cut Theorem) Let L be a ﬁnite lattice. Let X be a subset
of L such that ˆ ̸∈ X, and such that if y ∈ L, y ̸= ˆ, then some x ∈ X satisﬁes
x ≤ y. Let Nk be the number of k-element subsets of X with join ˆ. Then

µL(ˆ, ˆ = N0 − N1 + N2 − · · · .

We will prove Theorem 2.2 by an algebraic method. Such a sophisticated proof
is unnecessary, but the machinery we develop will be used later (Theorem 4.13).
Let L be a ﬁnite lattice and K a ﬁeld. The M¨obius algebra of L, denoted A(L), is
the semigroup algebra of L over K with respect to the operation ∨. (Sometimes
the operation is taken to be ∧ instead of ∨, but for our purposes, ∨ is more con-
venient.) In other words, A(L) = KL (the vector space with basis L) as a vector
space. If x, y ∈ L then we deﬁne xy = x ∨ y. Multiplication is extended to all
of A(L) by bilinearity (or distributivity). Algebraists will recognize that A(L) is
a ﬁnite-dimensional commutative algebra with a basis of idempotents, and hence
is isomorphic to K #L (as an algebra). We will show this by exhibiting an explicit
isomorphism A(L) ∼
→ K #L. For x ∈ L, deﬁne

(8) σx = ∑

y≥x µ(x, y)y ∈ A(L),

where µ denotes the M¨obius function of L. Thus by the M¨obius inversion formula,

(9) x = ∑

y≥x σy, for all x ∈ L.

Equation (9) shows that the σx’s span A(L). Since #{σx : x ∈ L} = #L =
dim A(L), it follows that the σx’s form a basis for A(L).

Theorem 2.3. Let x, y ∈ L. Then σxσy = δxyσx, where δxy is the Kronecker
delta. In other words, the σx’s are orthogonal idempotents. Hence

A(L) = ⊕

x∈L K · σx (algebra direct sum).

Proof. Deﬁne a K-algebra A′(L) with basis {σ′
x : x ∈ L} and multiplication
σ′
xσ′
y = δxyσ′
x. For x ∈ L set x′ = ∑
s≥x σ′
s. Then

x′y′ =
 ∑≥x σ′
s

 
∑

t≥y σ′
t


= ∑≥x
s≥y
 σ′
s

= ∑

s≥x∨y σ′
s

= (x ∨ y)′.

Hence the linear transformation ϕ : A(L) → A′(L) deﬁned by ϕ(x) = x′ is an
algebra isomorphism. Since ϕ(σx) = σ′
x, it follows that σxσy = δxyσx. □

LECTURE 2. PROPERTIES OF THE INTERSECTION POSET 17

Note. The algebra A(L) has a multiplicative identity, viz., 1 = ˆ = ∑x∈L σx.
Proof of Theorem 2.2. Let char(K) = 0, e.g., K = Q. For any x ∈ L, we
have in A(L) that ˆ − x = ∑≥ˆ σy − ∑

y≥x σy = ∑

y̸≥x σy.

Hence by the orthogonality of the σy’s we have
∏

x∈X(ˆ − x) = ∑

y σy,

where y ranges over all elements of L satisfying y ̸≥ x for all x ∈ X. By hypothesis,
the only such element is ˆ Hence
∏

x∈X(ˆ − x) = σˆ.

If we now expand both sides as linear combinations of elements of L and equate
coeﬃcients of ˆ the result follows. □
Note. In a ﬁnite lattice L, an atom is an element covering ˆ Let T be the set
of atoms of L. Then a set X ⊆ L − {ˆ} satisﬁes the hypotheses of Theorem 2.2 if
and only if T ⊆ X. Thus the simplest choice of X is just X = T .

Example 2.5. Let L = Bn, the boolean algebra of all subsets of [n]. Let X = T =
{{i} : i ∈ [n]}. Then N0 = N1 = · · · = Nn−1 = 0, Nn = 1. Hence µ(ˆ, ˆ) = (−1)n,
agreeing with Proposition 1.2.

We will use the Crosscut Theorem to obtain a formula for the characteristic
polynomial of an arrangement A. Extending slightly the deﬁnition of a central
arrangement, call any subset B of A central if ⋂
H∈B H ̸= ∅. The following result
is due to Hassler Whitney for linear arrangements. Its easy extension to arbitrary
arrangements appears in [13, Lemma 2.3.8].

Theorem 2.4. (Whitney’s theorem) Let A be an arrangement in an n-dimensional
vector space. Then

(10) χA(t) = ∑

B⊆A
B central

(−1)#Btn−rank(B).

Example 2.6. Let A be the arrangement in R2 shown below.

c d
 a

18 , HYPERPLANE ARRANGEMENTS

The following table shows all central subsets B of A and the values of #B and
rank(B). B #B rank(B)
∅ 0 0
a 1 1
b 1 1
c 1 1
d 1 1
ac 2 2
ad 2 2
bc 2 2
bd 2 2
cd 2 2
acd 3 2

It follows that χA(t) = t2 − 4t + (5 − 1) = t2 − 4t + 4.

Proof of Theorem 2.4. Let z ∈ L(A). Let

Λz = {x ∈ L(A) : x ≤ z},

the principal order ideal generated by z. Recall the deﬁnition

Az = {H ∈ A : H ≤ z (i.e., z ⊆ H)}.

By the Crosscut Theorem (Theorem 2.2), we have

µ(z) = ∑

k (−1)kNk(z),

where Nk(z) is the number of k-subsets of Az with join z. In other words,

µ(z) = ∑

B⊆Az
z=TH∈B H
(−1)#B.

Note that z = ⋂
H∈B H implies that rank(B) = n − dim z. Now multiply both sides
by tdim(z) and sum over z to obtain equation (10). □
We have now assembled all the machinery necessary to prove the Deletion-
Restriction Lemma (Lemma 2.2) for χA(t).
Proof of Lemma 2.2. Let H0 ∈ A be the hyperplane deﬁning the triple
(A, A′, A′′). Split the sum on the right-hand side of (10) into two sums, depending
on whether H0 ̸∈ B or H0 ∈ B. In the former case we get
∑

H0̸∈B⊆A
B central
(−1)#Btn−rank(B) = χA′(t).

In the latter case, set B1 = (B−{H0})H0 , a central arrangement in H0 ∼ K n−1 and
a subarrangement of AH0 = A′′. Since #B1 = #B − 1 and rank(B1) = rk(B) − 1,
we get ∑

H0∈B⊆A
B central
(−1)#Btn−rank(B) = ∑

B1∈A′′(−1)#B1+1t(n−1)−rank(B1)

= −χA′′ (t),

and the proof follows. □

LECTURE 2. PROPERTIES OF THE INTERSECTION POSET 19

2.2. The number of regions

The next result is perhaps the ﬁrst major theorem in the subject of hyperplane
arrangements, due to Thomas Zaslavsky in 1975.

Theorem 2.5. Let A be an arrangement in an n-dimensional real vector space.
Then
 r(A) = (−1)nχA(−1)(11)
 b(A) = (−1)rank(A)χA(1).(12)
First proof. Equation (11) holds for A = ∅, since r(∅) = 1 and χ∅(t) = tn.
By Lemmas 2.1 and 2.2, both r(A) and (−1)nχA(−1) satisfy the same recurrence,
so the proof follows.
Now consider equation (12). Again it holds for A = ∅ since b(∅) = 1. (Recall
that b(A) is the number of relatively bounded regions. When A = ∅, the entire
ambient space Rn is relatively bounded.) Now

χA(1) = χA′ (1) − χA′′ (1).

Let d(A) = (−1)rank(A)χA(1). If rank(A) = rank(A′) = rank(A′′) + 1, then d(A) =
d(A′) + d(A′′). If rank(A) = rank(A′) + 1 then b(A) = 0 [why?] and L(A′) ∼ L(A′′)
[why?]. Thus from Lemma 2.2 we have d(A) = 0. Hence in all cases b(A) and cdA)
satisfy the same recurrence, so b(A) = d(A). □
Second proof. Our second proof of Theorem 2.5 is based on M¨obius inversion
and some instructive topological considerations. For this proof we assume basic
knowledge of the Euler characteristic ψ(∆) of a topological space ∆. (Standard
notation is χ(∆), but this would cause too much confusion with the character-
istic polynomial.) In particular, if ∆ is suitably decomposed into cells with fi
i-dimensional cells, then

(13) ψ(∆) = f0 − f1 + f2 − · · · .

We take (13) as the deﬁnition of ψ(∆). For “nice” spaces and decompositions, it is
independent of the decomposition. In particular, χ(Rn) = (−1)n. Write ¯R for the
closure of a region R ∈ R(A).

Deﬁnition 2.4. A (closed) face of a real arrangement A is a set ∅ ̸= F = ¯R ∩ x,
where R ∈ R(A) and x ∈ L(A).

If we regard ¯R as a convex polyhedron (possibly unbounded), then a face of
A is just a face of some ¯R in the usual sense of the face of a polyhedron, i.e., the
intersection of ¯R with a supporting hyperplane. In particular, each ¯R is a face of
A. The dimension of a face F is deﬁned by

dim(F ) = dim(aﬀ(F )),

where aﬀ(F ) denotes the aﬃne span of F . A k-face is a k-dimensional face of A.
For instance, the arrangement below has three 0-faces (vertices), nine 1-faces, and
seven 2-faces (equivalently, seven regions). Hence ψ(R2) = 3 − 9 + 7 = 1.

20 , HYPERPLANE ARRANGEMENTS

Write F(A) for the set of faces of A, and let relint denote relative interior. Then

Rn = ⊔

F ∈F(A) relint(F ),

where ⊔ denotes disjoint union. If fk(A) denotes the number of k-faces of A, it
follows that (−1)n = ψ(Rn) = f0(A) − f1(A) + f2(A) − · · · .
Every k-face is a region of exactly one Ay for y ∈ L(A). Hence

fk(A) = ∑

y∈L(A)
dim(y)=k
 r(Ay).

Multiply by (−1)k and sum over k to get

(−1)n = ψ(Rn) = ∑

y∈L(A)
(−1)dim(y)r(Ay).

Replacing Rn by x ∈ L(A) gives

(−1)dim(x) = ψ(x) = ∑

y∈L(A)
y≥x
 (−1)dim(y)r(Ay).

M¨obius inversion yields

(−1)dim(x)r(Ax) = ∑

y∈L(A)
y≥x
 (−1)dim(y)µ(x, y).

Putting x = Rn gives

(−1)nr(A) = ∑

y∈L(A)
(−1)dim(y)µ(y) = χA(−1),

thereby proving (11).
The relatively bounded case (equation (12)) is similar, but with one technical
complication. We may assume that A is essential, since b(A) = b(ess(A)) and

χA(t) = tdim(A)−dim(ess(A))χess(A)(t).

In this case, the relatively bounded regions are actually bounded. Let

Fb(A) = {F ∈ F(A) : F is relatively bounded}

Γ = ⋃

F ∈Fb(A) F.

The diﬃculty lies in computing ψ(Γ). Zaslavsky conjectured in 1975 that Γ is
star-shaped, i.e., there exists x ∈ Γ such that for every y ∈ Γ, the line segment

LECTURE 2. PROPERTIES OF THE INTERSECTION POSET 21

a
 dc
 a

b
 c d

Figure 2. Two arrangements with the same intersection poset

joining x and y lies in Γ. This would imply that Γ is contractible, and hence (since
Γ is compact when A is essential) ψ(Γ) = 1. A counterexample to Zaslavsky’s
conjecture was found, but nevertheless Bj¨orner and Ziegler showed that Γ is indeed
contractible. (See [5, Thm. 4.5.7(b)] and Lecture 1, Exercise 8.) The argument just
given for r(A) now carries over mutatis mutandis to b(A). There is also a direct
argument that ψ(Γ) = 1, circumventing the need to show that Γ is contractible.
We will omit proving here that ψ(Γ) = 1. □

Corollary 2.1. Let A be a real arrangement. Then r(A) and b(A) depend only on
L(A).

Figure 2 shows two arrangements in R2 with diﬀerent “face structure” but
the same L(A). The ﬁrst arrangement has for instance one triangular and one
quadrilateral face, while the second has two triangular faces. Both arrangements,
however, have ten regions and two bounded regions.
We now give two basic examples of arrangements and the computation of their
characteristic polynomials.

Proposition 2.4. (general position) Let A be an n-dimensional arrangement of m
hyperplanes in general position. Then

χA(t) = tn − mtn−1 + (m
2
 )tn−2 − · · · + (−1)n(m
n
 ).

In particular, if A is a real arrangement, then

r(A) = 1 + m + (m
2
 ) + · · · + (m
n
 )

b(A) = (−1)n (1 − m + (m
2
 ) − · · · + (−1)n(m
n
 ))

= (m − 1
n
 ).

Proof. Every B ⊆ A with #B ≤ n deﬁnes an element xB = ⋂
H∈B H of L(A).
Hence L(A) is a truncated boolean algebra:

L(A) ∼ {S ⊆ [m] : #S ≤ n},

22 , HYPERPLANE ARRANGEMENTS

Figure 3. The truncated boolean algebra of rank 2 with four atoms

ordered by inclusion. Figure 3 shows the case n = 2 and m = 4, i.e., four lines in
general position in R2. If x ∈ L(A) and rk(x) = k, then [ˆ, x] ∼ Bk, a boolean
algebra of rank k. By equation (4) there follows µ(x) = (1)k. Hence

χA(t) = ∑

S⊆[m]
#S≤n
(−1)#Stn−#S

= tn − mtn−1 + · · · + (−1)n(m
n
 ). ✷

Note. Arrangements whose hyperplanes are in general position were formerly
called free arrangements. Now, however, free arrangements have another meaning
discussed in the note following Example 4.11.
Our second example concerns generic translations of the hyperplanes of a lin-
ear arrangement. Let L1, . . . , Lm be linear forms, not necessarily distinct, in the
variables v = (v1, . . . , vn) over the ﬁeld K. Let A be deﬁned by

L1(v) = a1, . . . , Lm(v) = am,

where a1, . . . , am are generic elements of K. This means if Hi = ker(Li(v) − ai),
then Hi1 ∩ · · · ∩ Hik ̸= ∅ ⇔ Li1 , . . . , Lik are linearly independent.
For instance, if K = R and L1, . . . , Lm are deﬁned over Q, then a1, . . . , am are
generic whenever they are linearly independent over Q.

nongeneric generic

It follows that if x = Hi1 ∩ · · · ∩ Hik ∈ L(A), then [ˆ, x] ∼ Bk. Hence

χA(t) = ∑

B (−1)#Btn−#B,

LECTURE 2. PROPERTIES OF THE INTERSECTION POSET 23

6 3 12 4 121
 Figure 4. The forests on four vertices

where B ranges over all linearly independent subsets of A. (We say that a set of hy-
perplanes are linearly independent if their normals are linearly independent.) Thus
χA(t), or more precisely (−t)nχA(−1/t), is the generating function for linearly
independent subsets of L1, . . . , Lm according to their number of elements. For in-
stance, if A is given by Figure 2 (either arrangement) then the linearly independent
subsets of hyperplanes are ∅, a, b, c, d, ac, ad, bc, bd, cd, so χA(t) = t2 − 4t + 5.
Consider the more interesting example xi − xj = aij, 1 ≤ i < j ≤ n, where the
aij are generic. We could call this arrangement the generic braid arrangement Gn.
Identify the hyperplane xi − xj = aij with the edge ij on the vertex set [n]. Thus
a subset B ⊆ Gn corresponds to a simple graph GB on [n]. (“Simple” means that
there is at most one edge between any two vertices, and no edge from a vertex to
itself.) It is easy to see that B is linearly independent if and only if the graph GB
has no cycles, i.e., is a forest. Hence we obtain the interesting formula

(14) χGn (t) = ∑

F (−1)e(F )tn−e(F ),

where F ranges over all forests on [n] and e(F ) denotes the number of edges of
F . For instance, the isomorphism types of forests (with the number of distinct
labelings written below the forest) on four vertices are given by Figure 4. Hence

χG4 (t) = t4 − 6t3 + 15t2 − 16t.

Equation (11) can be rewritten as

r(A) = ∑

x∈L(A)
(−1)rk(x)µ(x).

(Theorem 3.10 will show that (−1)rk(x)µ(x) > 0, so we could also write |µ(x)| for
this quantity.) It is easy to extend this result to count faces of A of all dimensions,
not just the top dimension n. Let fk(A) denote the number of k-faces of the real
arrangement A.

Theorem 2.6. We have

fk(A) = ∑

x≤y in L(A)
dim(x)=k
 (−1)dim(x)−dim(y)µ(x, y)

= ∑

x≤y in L(A)
dim(x)=k
 |µ(x, y)|.

Proof. As mentioned above, every face F is a region of a unique Ax for x ∈ L(A),
viz., x = aﬀ(F ). In particular, dim(F ) = dim(x). Hence if dim(F ) = k, then r(Ax)
is the number of k-faces of A contained in x. By Theorem 2.5 and equation (7) we
get r(Ax) = ∑

y≥x
(−1)dim(y)−dim(x)µ(x, y),

24 , HYPERPLANE ARRANGEMENTS

where we are dealing with the poset L(A). Summing over all x ∈ L(A) of dimension
k completes the proof. □

2.3. Graphical arrangements

There are close connections between certain invariants of a graph G and an asso-
ciated arrangement AG. Let G be a simple graph on the vertex set [n]. Let E(G)
denote the set of edges of G, regarded as two-element subsets of [n]. Write ij for
the edge {i, j}.

Deﬁnition 2.5. The graphical arrangement AG in K n is the arrangement

xi − xj = 0, ij ∈ E(G).

Thus a graphical arrangement is simply a subarrangement of the braid arrange-
ment Bn. If G = Kn, the complete graph on [n] (with all possible edges ij), then
AKn = Bn.

Deﬁnition 2.6. A coloring of a graph G on [n] is a map κ : [n] → P. The coloring
κ is proper if κ(i) ̸= κ(j) whenever ij ∈ E(G). If q ∈ P then let χG(q) denote the
number of proper colorings κ : [n] → [q] of G, i.e., the number of proper colorings
of G whose colors come from 1, 2, . . . , q. The function χG is called the chromatic
polynomial of G.

For instance, suppose that G is the complete graph Kn. A proper coloring
κ : [n] → [q] is obtained by choosing a vertex, say 1, and coloring it in q ways.
Then choose another vertex, say 2, and color it in q − 1 ways, etc., obtaining

(15) χKn(q) = q(q − 1) · · · (q − n + 1).

A similar argument applies to the graph G of Figure 5. There are q ways to color
vertex 1, then q − 1 to color vertex 2, then q − 1 to color vertex 3, etc., obtaining

χG(q) = q(q − 1)(q − 1)(q − 2)(q − 1)(q − 1)(q − 2)(q − 2)(q − 3)

= q(q − 1)4(q − 2)3(q − 3).

Unlike the case of the complete graph, in order to obtain this nice product formula
one factor at a time only certain orderings of the vertices are suitable. It is not
always possible to evaluate the chromatic polynomials “one vertex at a time.” For
instance, let H be the 4-cycle of Figure 5. If a proper coloring κ : [4] → [q] satisﬁes
κ(1) = κ(3), then there are q choices for κ(1), then q − 1 choices each for κ(2) and
κ(4). On the other hand, if κ(1) ̸= κ(3), then there are q choices for κ(1), then
q − 1 choices for κ(3), and then q − 2 choices each for κ(2) and κ(4). Hence

χH(q) = q(q − 1)2 + q(q − 1)(q − 2)2

= q(q − 1)(q2 − 3q + 3).

For further information on graphs whose chromatic polynomial can be evaluated
one vertex at a time, see Corollary 4.9 and the note following it.
It is easy to see directly that χG(q) is a polynomial function of q. Let ei(G)
denote the number of surjective proper colorings κ : [n] → [i] of G. We can choose
an arbitrary proper coloring κ : [n] → [q] by ﬁrst choosing the size i = #κ([n]) of
its image in (q
i) ways, and then choose κ in ei ways. Hence

(16) χG(q) =
 n∑

i=0 ei
(q
i
).

LECTURE 2. PROPERTIES OF THE INTERSECTION POSET 25

4 2

3

G H
1 3

2 5 4

6 8

9 7

Figure 5. Two graphs

Since (q
i) = q(q−1) · · · (q−i+1)/i!, a polynomial in q (of degree i), we see that χG(q)
is a polynomial. We therefore write χG(t), where t is an indeterminate. Moreover,
any surjection (= bijection) κ : [n] → [n] is proper. Hence en = n!. It follows from
equation (16) that χG(t) is monic of degree n. Using more sophisticated methods
we will later derive further properties of the coeﬃcients of χG(t).

Theorem 2.7. For any graph G, we have χAG(t) = χG(t).

First proof. The ﬁrst proof is based on deletion-restriction (which in the
context of graphs is called deletion-contraction). Let e = ij ∈ E(G). Let G − e
(also denoted G\e) denote the graph G with edge e deleted, and let G/e denote G
with the edge e contracted to a point and all multiple edges replaced by a single
edge (i.e., whenever there is more than one edge between two vertices, replace these
edges by a single edge). (In some contexts we want to keep track of multiple edges,
but they are irrelevant in regard to proper colorings.)

1

2 e
 4
 5

G
 1

2
 3

4
 5
 1
 23
 4
 5

G−e G/e

Let H0 ∈ A = AG be the hyperplane xi = xj. It is clear that AH0 = AG−e.
We claim that

(17) AH0 = AG/e.

Deﬁne an aﬃne isomorphism ϕ : H0 ∼=
→ Rn−1 by

(x1, x2, . . . , xn) ↦→ (x1, . . . , xi, . . . , ˆxj, . . . , xn),

where ˆxj denotes that the jth coordinate is omitted. (Hence the coordinates in
Rn−1 are 1, 2, . . . , ˆj, . . . , n.) Write Hab for the hyperplane xa = xb of A. If neither
of a, b are equal to i or j, then ϕ(Hab ∩ H0) is the hyperplane xa = xb in Rn−1. If
a ̸= i, j then ϕ(Hia ∩ H0) = ϕ(Haj ∩ H0), the hyperplane xa = xi in Rn−1. Hence ϕ
deﬁnes an isomorphism between AH0 and the arrangement AG/e in Rn−1, proving
(17).

26 , HYPERPLANE ARRANGEMENTS
 G

Figure 6. A graph G with edge subset F and closure ¯F

Let n• denote the graph with n vertices and no edges, and let ∅ denote
the empty arrangement in Rn. The theorem will be proved by induction (using
Lemma 2.2) if we show:

(a) Initialization: χn•(t) = χ∅(t)
(b) Deletion-contraction:

(18) χG(t) = χG−e(t) − χG/e(t)

To prove (a), note that both sides are equal to tn. To prove (b), observe that
χG−e(q) is the number of colorings of κ : [n] → [q] that are proper except possibly
κ(i) = κ(j), while χG/e(q) is the number of colorings κ : [n] → [q] of G that are
proper except that κ(i) = κ(j). □
Our second proof of Theorem 2.7 is based on M¨obius inversion. We ﬁrst obtain
a combinatorial description of the intersection lattice L(AG). Let Hij denote the
hyperplane xi = xj as above, and let F ⊆ E(G). Consider the element X =⋂ij∈F Hij of L(AG). Thus

(x1, . . . , xn) ∈ X ⇔ xi = xj whenever ij ∈ F.

Let C1, . . . , Ck be the connected components of the spanning subgraph GF of G
with edge set F . (A subgraph of G is spanning if it contains all the vertices of G.
Thus if the edges of F do not span all of G, we need to include all remaining vertices
as isolated vertices of GF .) If i, j are vertices of some Cm, then there is a path from
i to j whose edges all belong to F . Hence xi = xj for all (x1, . . . , xn) ∈ X. On the
other hand, if i and j belong to diﬀerent Cm’s, then there is no such path. Let

¯F = {e = ij ∈ E(G) : i, j ∈ V (Cm) for some m},

where V (Cm) denotes the vertex set of Cm. Figure 6 illustrates a graph G with
a set F of edges indicated by thickening. The set ¯F is shown below G, with the
additional edges ¯F − F not in F drawn as dashed lines.
A partition π of a ﬁnite set S is a collection {B1, . . . , Bk} of subsets of S, called
blocks, that are nonempty, pairwise disjoint, and whose union is S. The set of all
partitions of S is denoted ΠS, and when S = [n] we write simply Πn for Π[n]. It
follows from the above discussion that the elements Xπ of L(AG) correspond to the
connected partitions of V (G), i.e., the partitions π = {B1, . . . , Bk} of V (G) = [n]

LECTURE 2. PROPERTIES OF THE INTERSECTION POSET 27

ab ac bc bd cd
 bcdacdabd
abc
 abcd

b
 c

d

a
 ab−cdac−bd

Figure 7. A graph G and its bond lattice LG

such that the restriction of G to each block Bi is connected. Namely,

Xπ = {(x1, . . . , xn) ∈ K n : i, j ∈ Bm for some m ⇒ xi = xj}.

We have Xπ ≤ Xσ in L(A) if and only if every block of π is contained in a block of
σ. In other words, π is a reﬁnement of σ. This reﬁnement order is the “standard”
ordering on Πn, so L(AG) is isomorphic to an induced subposet LG of Πn, called
the bond lattice or lattice of contractions of G. (“Induced” means that if π ≤ σ
in Πn and π, σ ∈ L(AG), then π ≤ σ in L(AG).) In particular, Πn ∼ L(AKn).
Note that in general LG is not a sublattice of Πn, but only a sub-join-semilattice of
Πn [why?]. The bottom element ˆ of LG is the partition of [n] into n one-element
blocks, while the top element ˆ is the partition into one block. The case G = Kn
shows that the intersection lattice L(Bn) of the braid arrangement Bn is isomorphic
to the full partition lattice Πn. Figure 7 shows a graph G and its bond lattice LG
(singleton blocks are omitted from the labels of the elements of LG).
Second proof of Theorem 2.7. Let π ∈ LG. For q ∈ P deﬁne χπ(q) to be
the number of colorings κ : [n] → [q] of G satisfying:
• If i, j are in the same block of π, then κ(i) = κ(j).
• If i, j are in diﬀerent blocks of π and ij ∈ E(G), then κ(i) ̸= κ(j).
Given any κ : [n] → [q], there is a unique σ ∈ LG such that κ is enumerated by
χσ(q). Moreover, κ will be constant on the blocks of some π ∈ LG if and only if
σ ≥ π in LG. Hence q|π| = ∑

σ≥π χσ(q) ∀π ∈ LG,

where |π| denotes the number of blocks of π. By M¨obius inversion,

χπ(q) = ∑

σ≥π q|σ|µ(π, σ),

where µ denotes the M¨obius function of LG. Let π = ˆ. We get

(19) χG(q) = χˆ(q) = ∑

σ∈LG µ(σ)q|σ|.

It is easily seen that |σ| = dim Xσ, so comparing equation (19) with Deﬁnition 1.3
shows that χG(t) = χAG (t). □

28 , HYPERPLANE ARRANGEMENTS

Corollary 2.2. The characteristic polynomial of the braid arrangement Bn is given
by χBn(t) = t(t − 1) · · · (t − n + 1).

Proof. Since Bn = AKn (the graphical arrangement of the complete graph Kn),
we have from Theorem 2.7 that χBn(t) = χKn(t). The proof follows from equation
(15). □
There is a further invariant of a graph G that is closely connected with the
graphical arrangement AG.

Deﬁnition 2.7. An orientation o of a graph G is an assignment of a direction
i → j or j → i to each edge ij of G. A directed cycle of o is a sequence of vertices
i0, i1, . . . , ik of G such that i0 → i1 → i2 → · · · → ik → i0 in o. An orientation o is
acyclic if it contains no directed cycles.

A graph G with no loops (edges from a vertex to itself) thus has 2#E(G) orien-
tations. Let R ∈ R(AG), and let (x1, . . . , xn) ∈ R. In choosing R, we have speciﬁed
for all ij ∈ E(G) whether xi < xj or xi > xj . Indicate by an arrow i → j that
xi < xj , and by j → i that xi > xj. In this way the region R deﬁnes an orientation
oR of G. Clearly if R ̸= R′, then oR ̸= oR′ . Which orientations can arise in this
way?

Proposition 2.5. Let o be an orientation of G. Then o = oR for some R ∈ R(AG)
if and only if o is acyclic.

Proof. If oR had a cycle i1 → i2 → · · · → ik → i1, then a point (x1, . . . , xn) ∈ R
would satisfy xi1 < xi2 < · · · < xik < xi1 , which is absurd. Hence oR is acyclic.
Conversely, let o be an acyclic orientation of G. First note that o must have a
sink, i.e., a vertex with no arrows pointing out. To see this, walk along the edges
of o by starting at any vertex and following arrows. Since o is acyclic, we can never
return to a vertex so the process will end in a sink. Let jn be a sink vertex of o.
When we remove jn from o the remaining orientation is still acyclic, so it contains
a sink jn−1. Continuing in this manner, we obtain an ordering j1, j2, . . . , jn of [n]
such that ji is a sink of the restriction of o to j1, . . . , ji. Hence if x1, . . . , xn ∈ R
satisfy xj1 < xj2 < · · · < xjn then the region R ∈ R(A) containing (x1, . . . , xn)
satisﬁes o = oR. □
Note. The transitive, reﬂexive closure ¯o of an acyclic orientation o is a par-
tial order. The construction of the ordering j1, j2, . . . , jn above is equivalent to
constructing a linear extension of o.
Let AO(G) denote the set of acyclic orientations of G. We have constructed a
bijection between AO(G) and R(AG). Hence from Theorem 2.5 we conclude:

Corollary 2.3. For any graph G with n vertices, we have #AO(G) = (−1)nχG(−1).

Corollary 2.3 was ﬁrst proved by Stanley in 1973 by a “direct” argument based
on deletion-contraction (see Exercise 6). The proof we have just given based on
arrangements is due to Greene and Zaslavsky in 1983.
Note. Given a graph G on n vertices, let A# be the arrangement deﬁned by

xi − xj = aij, ij ∈ E(G),

where the aij’s are generic. Just as we obtained equation (14) (the case G = Kn)
we have χA#(t) = ∑

F (−1)e(F )tn−e(F ),

LECTURE 2. PROPERTIES OF THE INTERSECTION POSET 29

where F ranges over all spanning forests of G.

30 , HYPERPLANE ARRANGEMENTS

Exercises
(1) [2–] Let G be a graph on the vertex set [n]. Show that the bond lattice LG is a
sub-join-semilattice of the partition lattice Πn but is not in general a sublattice
of Πn.
(2) [2–] Let G be a forest (graph with cycles) on the vertex set [n]. Show that
LG ∼ BE(G), the boolean algebra of all subsets of E(G).
(3) [2] Let G be a graph with n vertices and AG the corresponding graphical ar-
rangement. Suppose that G has a k-element clique, i.e., k vertices such that any
two are adjacent. Show that k!|r(A).
(4) [2+] Let G be a graph on the vertex set [n] = {1, 2, . . . , n}, and let AG be the
corresponding graphical arrangement (over any ﬁeld K, but you may assume
K = R if you wish). Let Cn be the coordinate hyperplane arrangement, con-
sisting of the hyperplanes xi = 0, 1 ≤ i ≤ n. Express χAG∪Cn(t) in terms of
χAG(t).
(5) [4] Let G be a planar graph, i.e., G can be drawn in the plane without crossing
edges. Show that χAG(4) ̸= 0.
(6) [2+] Let G be a graph with n vertices. Show directly from the the deletion-
contraction recurrence (18) that

(−1)nχG(−1) = #AO(G).

(7) [2+] Let χG(t) = tn − cn−1tn−1 + · · · + (−1)n−1c1t be the chromatic polynomial
of the graph G. Let i be a vertex of G. Show that c1 is equal to the number of
acyclic orientations of G whose unique source is i.
(8) [5] Let A be an arrangement with characteristic polynomial χA(t) = tn −
cn−1tn−1 + cn−2tn−2 − · · · + (−1)nc0. Show that the sequence c0, c1, . . . , cn = 1
is unimodal, i.e., for some j we have

c0 ≤ c1 ≤ · · · ≤ cj ≥ cj+1 ≥ · · · ≥ cn.

(9) [2+] Let f (n) be the total number of faces of the braid arrangement Bn. Find
a simple formula for the generating function
∑

n≥0 f (n) xn

n! = 1 + x + 3 x2

2! + 13 x3

3! + 75 x4

4! + 541 x5

5! + 4683 x6

6! + · · · .

LECTURE 3
Matroids and geometric lattices

3.1. Matroids

A matroid is an abstraction of a set of vectors in a vector space (for us, the normals
to the hyperplanes in an arrangement). Many basic facts about arrangements
(especially linear arrangements) and their intersection posets are best understood
from the more general viewpoint of matroid theory. There are many equivalent
ways to deﬁne matroids. We will deﬁne them in terms of independent sets, which
are an abstraction of linearly independent sets. For any set S we write

2S = {T : T ⊆ S}.

Deﬁnition 3.8. A (ﬁnite) matroid is a pair M = (S, I), where S is a ﬁnite set and
I is a collection of subsets of S, satisfying the following axioms:
(1) I is a nonempty (abstract) simplicial complex, i.e., I ̸= ∅, and if J ∈ I and
I ⊂ J, then I ∈ I.
(2) For all T ⊆ S, the maximal elements of I ∩ 2T have the same cardinality.
In the language of simplicial complexes, every induced subcomplex of I is
pure.

The elements of I are called independent sets. All matroids considered here will
be assumed to be ﬁnite. By standard abuse of notation, if M = (S, I) then we write
x ∈ M to mean x ∈ S. The archetypal example of a matroid is a ﬁnite subset S of
a vector space, where independence means linear independence. A closely related
matroid consists of a ﬁnite subset S of an aﬃne space, where independence now
means aﬃne independence.
It should be clear what is meant for two matroids M = (S, I) and M ′ = (S′, I′)
to be isomorphic, viz., there exists a bijection f : S → S ′ such that {x1, . . . , xj } ∈ I
if and only if {f (x1), . . . , f (xj)} ∈ I′. Let M be a matroid and S a set of points in
Rn, regarded as a matroid with independence meaning aﬃne independence. If M
and S are isomorphic matroids, then S is called an aﬃne diagram of M . (Not all
matroids have aﬃne diagrams.)

Example 3.7. (a) Regard the conﬁguration in Figure 1 as a set of ﬁve points in the
two-dimensional aﬃne space R2. These ﬁve points thus deﬁne the aﬃne diagram
of a matroid M . The lines indicate that the points 1,2,3 and 3,4,5 lie on straight

31

32 , HYPERPLANE ARRANGEMENTS

1
 2
 3
 4
 5

Figure 1. A ﬁve-point matroid in the aﬃne space R2

lines. Hence the sets {1, 2, 3} and {3, 4, 5} are aﬃnely dependent in R2 and therefore
dependent (i.e., not independent) in M . The independent sets of M consist of all
subsets of [5] with at most two elements, together with all three-element subsets of
[5] except 123 and 345 (where 123 is short for {1, 2, 3}, etc.).
(b) Write I = ⟨S1, . . . , Sk⟩ for the simplicial complex I generated by S1, . . . , Sk,
i.e.,
 ⟨S1, . . . , Sk⟩ = {T : T ⊆ Si for some i}

= 2S1 ∪ · · · ∪ 2Sk.

Then I = ⟨13, 14, 23, 24⟩ is the set of independent sets of a matroid M on [4]. This
matroid is realized by a multiset of vectors in a vector space or aﬃne space, e.g., by
the points 1,1,2,2 in the aﬃne space R. The aﬃne diagam of this matroid is given
by
 3,41,2

(c) Let I = ⟨12, 23, 34, 45, 15⟩. Then I is not the set of independent sets of a
matroid. For instance, the maximal elements of I ∩ 2{1,2,4} are 12 and 4, which do
not have the same cardinality.
(d) The aﬃne diagram below shows a seven point matroid.

1 2

3

LECTURE 3. MATROIDS AND GEOMETRIC LATTICES 33

If we further require the points labelled 1,2,3 to lie on a line (i.e., remove 123
from I), we still have a matroid M , but not one that can be realized by real vectors.
In fact, M is isomorphic to the set of nonzero vectors in the vector space F3, where
F2 denotes the two-element ﬁeld.

110
 101100 001

011
111

010

Let us now deﬁne a number of important terms associated to a matroid M .
A basis of M is a maximal independent set. A circuit C is a minimal dependent
set, i.e., C is not independent but becomes independent when we remove any point
from it. For example, the circuits of the matroid of Figure 1 are 123, 345, and 1245.
If M = (S, I) is a matroid and T ⊆ S then deﬁne the rank rk(T ) of T by

rk(T ) = max{#I : I ∈ I and I ⊆ T }.

In particular, rk(∅) = 0. We deﬁne the rank of the matroid M itself by rk(M ) =
rk(S). A k-ﬂat is a maximal subset of rank k. For instance, if M is an aﬃne
matroid, i.e., if S is a subset of an aﬃne space and independence in M is given by
aﬃne independence, then the ﬂats of M are just the intersections of S with aﬃne
subspaces. Note that if F and F ′ are ﬂats of a matroid M , then so is F ∩ F ′ (see
Exercise 2). Since the intersection of ﬂats is a ﬂat, we can deﬁne the closure T of
a subset T ⊆ S to be the smallest ﬂat containing T , i.e.,

T = ⋂

ﬂats F ⊇T F.

This closure operator has a number of nice properties, such as T = T and T ′ ⊆
T ⇒ T ′ ⊆ T .

3.2. The lattice of ﬂats and geometric lattices

For a matroid M deﬁne L(M ) to be the poset of ﬂats of M , ordered by inclusion.
Since the intersection of ﬂats is a ﬂat, L(M ) is a meet-semilattice; and since L(M )
has a top element S, it follows from Lemma 2.3 that L(M ) is a lattice, which we
call the lattice of ﬂats of M . Note that L(M ) has a unique minimal element ˆ viz.,
¯ or equivalently, the intersection of all ﬂats. It is easy to see that L(M ) is graded
by rank, i.e., every maximal chain of L(M ) has length m = rk(M ). Thus if x ⋖ y in
L(M ) then rk(y) = 1 + rk(x). We now deﬁne the characteristic polynomial χM (t),

34 , HYPERPLANE ARRANGEMENTS

2 4 51 3

Figure 2. The lattice of ﬂats of the matroid of Figure 1

in analogy to the deﬁnition (3) of χA(t), by

χM (t) = ∑

x∈L(M ) µ(ˆ, x)tm−rk(x),

where µ denotes the M¨obius function of L(M ) and m = rk(M ). Figure 2 shows the
lattice of ﬂats of the matroid M of Figure 1. From this ﬁgure we see easily that

χM (t) = t3 − 5t2 + 8t − 4.

Let M be a matroid and x ∈ M . If the set {x} is dependent (i.e., if rk({x}) = 0)
then we call x a loop. Thus ¯ is just the set of loops of M . Suppose that x, y ∈ M ,
neither x nor y are loops, and rk({x, y}) = 1. We then call x and y parallel points.
A matroid is simple if it has no loops or pairs of parallel points. It is clear that the
following three conditions are equivalent:
• M is simple.
• ¯ = ∅ and ¯x = x for all x ∈ M .
• rk({x, y}) = 2 for all points x ̸= y of M (assuming M has at least two
points).
For any matroid M and x, y ∈ M , deﬁne x ∼ y if ¯x = ¯y. It is easy to see that ∼ is
an equivalence relation. Let

(20) ˆM = {¯x : x ∈ M },

with an obvious deﬁnition of independence, i.e.,

{¯x1, . . . , ¯xk} ∈ I( ˆM ) ⇔ {x1, . . . , xk} ∈ I(M ).

Then ˆM is simple, and L(M ) ∼ L( ˆM). Thus insofar as intersection lattices L(M )
are concerned, we may assume that M is simple. (Readers familiar with point set
topology will recognize the similarity between the conditions for a matroid to be
simple and for a topological space to be T0.)

Example 3.8. Let S be any ﬁnite set and V a vector space. If f : S → V , then
deﬁne a matroid Mf on S by the condition

I ∈ I(M ) ⇔ {f (x) : x ∈ I ⊆ S} is linearly independent.

Then a loop is any element x satisfying f (x) = 0, and x ∼ y if and only if f (x) is
a nonzero scalar multiple of f (y).

LECTURE 3. MATROIDS AND GEOMETRIC LATTICES 35

Note. If M = (S, I) is simple, then L(M ) determines M . For we can identify
S with the set of atoms of L(M ), and we have

{x1, . . . , xk} ∈ I ⇔ rk(x1 ∨ · · · ∨ xk) = k in L(M ).

See the proof of Theorem 3.8 for further details.
We now come to the primary connection between hyperplane arrangements and
matroid theory. If H is a hyperplane, write nH for some (nonzero) normal vector
to H.

Proposition 3.6. Let A be a central arrangement in the vector space V . Deﬁne
a matroid M = MA on A by letting B ∈ I(M ) if B is linearly independent (i.e.,
{nH : H ∈ B} is linearly independent). Then M is simple and L(M ) ∼ L(A).

Proof. M has no loops, since every H ∈ A has a nonzero normal. Two distinct
nonparallel hyperplanes have linearly independent normals, so the points of M are
closed. Hence M is simple.
Let B, B′ ⊆ A, and set

X = ⋂

H∈B H = XB, X ′ = ⋂

H∈B′ H = XB′.

Then X = X ′ if and only if

span{nH : H ∈ B} = span{nH : H ∈ B′}.

Now the closure relation in M is given by

B = {H ′ ∈ A : nH′ ∈ span{nH : H ∈ B}}.

Hence X = X ′ if and only if B = B′, so L(M ) ∼ L(A). □
It follows that for a central arrangement A, L(A) depends only on the matroidal
structure of A, i.e., which subsets of hyperplanes are linearly independent. Thus
the matroid MA encapsulates the essential information about A needed to deﬁne
L(A).
Our next goal is to characterize those lattices L which have the form L(M ) for
some matroid M .

Proposition 3.7. Let L be a ﬁnite graded lattice. The following two conditions
are equivalent.

(1) For all x, y ∈ L, we have rk(x) + rk(y) ≥ rk(x ∧ y) + rk(x ∨ y).
(2) If x and y both cover x ∧ y, then x ∨ y covers both x and y.

Proof. Assume (1). Let x, y ⋗ x ∧ y, so rk(x) = rk(y) = rk(x ∧ y) + 1 and
rk(x ∨ y) > rk(x) = rk(y). By (1),

rk(x) + rk(y) ≥ (rk(x) − 1) + rk(x ∨ y)

⇒ rk(y) ≥ rk(x ∨ y) − 1
⇒ x ∨ y ⋗ x.

Similarly x ∨ y ⋗ y, proving (2).
For (2)⇒(1), see [18, Prop. 3.3.2]. □

Deﬁnition 3.9. A ﬁnite lattice L satisfying condition (1) or (2) above is called
(upper) semimodular. A ﬁnite lattice L is atomic if every x ∈ L is a join of atoms

36 , HYPERPLANE ARRANGEMENTS

(a) (b) (c)

Figure 3. Three nongeometric lattices

(where we regard ˆ as an empty join of atoms). Equivalently, if x ∈ L is join-
irreducible (i.e., covers a unique element), then x is an atom. Finally, a ﬁnite
lattice is geometric if it is both semimodular and atomic.

To illustrate these deﬁnitions, Figure 3(a) shows an atomic lattice that is not
semimodular, (b) shows a semimodular lattice that is not atomic, and (c) shows a
graded lattice that is neither semimodular nor atomic.
We are now ready to characterize the lattice of ﬂats of a matroid.

Theorem 3.8. Let L be a ﬁnite lattice. The following two conditions are equivalent.
(1) L is a geometric lattice.
(2) L ∼ L(M ) for some (simple) matroid M .

Proof. Assume that L is geometric, and let A be the set of atoms of L. If T ⊆ A
then write ⋁ T = ⋁x∈T x, the join of all elements of T . Let

I = {I ⊆ A : rk(∨I) = #I}.

Note that by semimodularity, we have for any S ⊆ A and x ∈ A that rk((⋁ S)∨x) ≤
rk(⋁ S) + 1. (Hence in particular, rk(⋁ S) ≤ #S.) It follows that I is a simplicial
complex. Let S ⊆ A, and let T, T ′ be maximal elements of 2S ∩ I. We need to show
that #T = #T ′.
Assume #T < #T ′, say. If y ∈ S then y ≤ ⋁ T ′, else T ′′ = T ′ ∪ y satisﬁes
rk(⋁ T ′′) = #T ′′, contradicting the maximality of T ′. Since #T < #T ′ and T ⊆ S,
it follows that ⋁ T < ⋁ T ′ [why?]. Since L is atomic, there exists y ∈ S such that
y ∈ S but t ̸≤ ⋁ T . But then rk(⋁(T ∪ y)) = 1 + #T , contradicting the maximality
of T . Hence M = (A, I) is a matroid, and L ∼ L(M ).
Conversely, given a matroid M , which we may assume is simple, we need to
show that L(M ) is a geometric lattice. Clearly L(M ) is atomic, since every ﬂat is
the join of its elements. Let S, T ⊆ M . We will show that

(21) rk(S) + rk(T ) ≥ rk(S ∩ T ) + rk(S ∪ T ).

Note that if S and T are ﬂats (i.e., S, T ∈ L(M )) then S ∩ T = S ∧ T and
rk(S ∪ T ) = rk(S ∨ T ). Hence taking S and T to be ﬂats in (21) shows that L(M )

LECTURE 3. MATROIDS AND GEOMETRIC LATTICES 37

is semimodular and thus geometric. Suppose (21) is false, so

rk(S ∪ T ) > rk(S) + rk(T ) − rk(S ∩ T ).

Let B be a basis for S ∪ T . Then either #(B ∩ S) > rk(S) or #(B ∩ T ) > rk(T ), a
contradiction completing the proof. □
Note that by Proposition 3.6 and Theorem 3.8, any results we prove about geo-
metric lattices hold a fortiori for the intersection lattice LA of a central arrangement
A. Note. If L is geometric and x ≤ y in L, then it is easy to show using semi-
modularity that the interval [x, y] is also a geometric lattice. (See Exercise 3.) In
general, however, an interval of an atomic lattice need not be atomic.
For noncentral arrangements L(A) is not a lattice, but there is still a connection
with geometric lattices. For a stronger statement, see Exercise 4.

Proposition 3.8. Let A be an arrangement. Then every interval [x, y] of L(A) is
a geometric lattice.

Proof. By Exercise 3, it suﬃces to take x = ˆ. Now [ˆ, y] ∼ L(Ay), where Ay is
given by (6). Since Ay is a central arrangement, the proof follows from Proposi-
tion 3.6. □
The proof of our next result about geometric lattices will use a fundamental
formula concerning M¨obius functions known as Weisner’s theorem. For a proof, see
[18, Cor. 3.9.3] (where it is stated in dual form).

Theorem 3.9. Let L be a ﬁnite lattice with at least two elements and with M¨obius
function µ. Let ˆ ̸= a ∈ L. Then

(22) ∑

x : x∨a=ˆ µ(x) = 0.

Note that Theorem 3.9 gives a “shortening” of the recurrence (2) deﬁning µ.
Normally we take a to be an atom, since that produces fewer terms in (22) than
choosing any b > a. As an example, let L = Bn, the boolean algebra of all subsets
of [n], and let a = {n}. There are two elements x ∈ Bn such that x ∨ a = ˆ = [n],
viz., x1 = [n − 1] and x2 = [n]. Hence µ(x1) + µ(x2) = 0. Since [ˆ, x1] = Bn−1 and
[ˆ, x2] = Bn, we easily obtain µBn(ˆ = (−1)n, agreeing with (4).
If x ≤ y in a graded lattice L, write rk(x, y) = rk(y) − rk(x), the length of
every saturated chain from x to y. The next result may be stated as “the M¨obius
function of a geometric lattice strictly alternates in sign.”

Theorem 3.10. Let L be a ﬁnite geometric lattice with M¨obius function µ, and let
x ≤ y in L. Then
 (−1)rk(x,y)µ(x, y) > 0.

Proof. Since every interval of a geometric lattice is a geometric lattice (Exercise 3),
it suﬃces to prove the theorem for [x, y] = [ˆ, ˆ The proof is by induction on the
rank of L. It is clear if rk(L) = 1, in which case µ(ˆ, ˆ) = −1. Assume the result
for geometric lattices of rank < n, and let rk(L) = n. Let a be an atom of L in
Theorem 3.9. For any y ∈ L we have by semimodularity that

rk(y ∧ a) + rk(y ∨ a) ≤ rk(y) + rk(a) = rk(y) + 1.

38 , HYPERPLANE ARRANGEMENTS

Hence x ∨ a = ˆ if and only if x = ˆ or x is a coatom (i.e., x ⋖ ˆ) satisfying a ̸≤ x.
From Theorem 3.9 there follows

µ(ˆ, ˆ) = − ∑

a̸≤x⋖ˆ µ(ˆ, x).

The sum on the right is nonempty since L is atomic, and by induction every x
indexing the sum satisﬁes (−1)n−1µ(ˆ, x) > 0. Hence (−1)nµ(ˆ, ˆ > 0. □
Combining Proposition 3.8 and Theorem 3.10 yields the following result.

Corollary 3.4. Let A be any arrangement and x ≤ y in L(A). Then

(−1)rk(x,y)µ(x, y) > 0,

where µ denotes the M¨obius function of L(A).

LECTURE 3. MATROIDS AND GEOMETRIC LATTICES 39

Exercises
(1) (a) [1+] Let χG(t) be the characteristic polynomial of the graphical arrange-
ment AG. Suppose that χG(i) = 0, where i ∈ Z, i > 1. Show that
χG(i − 1) = 0.
(b) [2] Is the same conclusion true for any central arrangement A?
(2) [2] Show that F and F ′ are ﬂats of a matroid M , then so is F ∩ F ′.
(3) [2] Prove the assertion in the Note following the proof of Theorem 3.8 that an
interval [x, y] of a geometric lattice L is also a geometric lattice.
(4) [2+] Let A be an arrangement (not necessarily central). Show that there exists
a geometric lattice L and an atom a of L such that L(A) ∼ L − Va, where
Va = {x ∈ L : x ≥ a}.
(5) [2–] Let L be a geometric lattice of rank n, and deﬁne the truncation T (L) to
be the subposet of L consisting of all elements of rank ̸= n − 1. Show that T (L)
is a geometric lattice.
(6) Let Wi be the number of elements of rank i in a geometric lattice (or just in the
intersection poset of a central hyperplane arrangement, if you prefer) of rank n.
(a) [3] Show that for k ≤ n/2,

W1 + W2 + · · · + Wk ≤ Wn−k + Wn−k+1 + · · · + Wn−1.

(b) [2–] Deduce from (a) and Exercise 5 that W1 ≤ Wk for all 1 ≤ k ≤ n − 1.
(c) [5] Show that Wi ≤ Wn−i for i < n/2 and that the sequence W0, W1, . . . , Wn
is unimodal. (Compare Lecture 2, Exercise 8.)
 LECTURE 4
Broken circuits, modular elements, and supersolvability

This lecture is concerned primarily with matroids and geometric lattices. Since
the intersection lattice of a central arrangement is a geometric lattice, all our results
can be applied to arrangements.

4.1. Broken circuits

For any geometric lattice L and x ≤ y in L, we have seen (Theorem 3.10) that
(−1)rk(x,y)µ(x, y) is a positive integer. It is thus natural to ask whether this integer
has a direct combinatorial interpretation. To this end, let M be a matroid on the
set S = {u1, . . . , um}. Linearly order the elements of S, say u1 < u2 < · · · < um.
Recall that a circuit of M is a minimal dependent subset of S.

Deﬁnition 4.10. A broken circuit of M (with respect to the linear ordering O of
S) is a set C − {u}, where C is a circuit and u is the largest element of C (in the
ordering O). The broken circuit complex BCO(M ) (or just BC(M ) if no confusion
will arise) is deﬁned by

BC(M ) = {T ⊆ S : T contains no broken circuit}.

Figure 1 shows two linear orderings O and O′ of the points of the aﬃne matroid
M of Figure 1 (where the ordering of the points is 1 < 2 < 3 < 4 < 5). With respect
to the ﬁrst ordering O the circuits are 123, 345, 1245, and the broken circuits are
12, 34, 124. With respect to the second ordering O′ the circuits are 123, 145, 2345,
and the broken circuits are 12, 14, 234.
It is clear that the broken circuit complex BC(M ) is an abstract simplicial
complex, i.e., if T ∈ BC(M ) and U ⊆ T , then U ∈ BC(M ). In Figure 1 we

2 4
 53
 1

2
 3
 4
 51

Figure 1. Two linear orderings of the matroid M of Figure 1

41

42 , HYPERPLANE ARRANGEMENTS

have BCO(M ) = ⟨135, 145, 235, 245⟩, while BCO′(M ) = ⟨135, 235, 245, 345⟩. These
simplicial complexes have geometric realizations as follows:

4
 5
 2

31 2

4 3
 1

5

Note that the two simplicial complexes BCO(M ) and BCO′ (M ) are not iso-
morphic (as abstract simplicial complexes); in fact, their geometric realizations are
not even homeomorphic. On the other hand, if fi(∆) denotes the number of i-
dimensional faces (or faces of cardinality i − 1) of the abstract simplicial complex
∆, then for ∆ given by either BCO(M ) or BCO′ (M ) we have

f−1(∆) = 1, f0(∆) = 5, f1(∆) = 8, f2(∆) = 4.

Note, moreover, that χM (t) = t3 − 5t2 + 8t − 4.

In order to generalize this observation to arbitrary matroids, we need to introduce
a fair amount of machinery, much of it of interest for its own sake. First we give
a fundamental formula, known as Philip Hall’s theorem, for the M¨obius function
value µ(ˆ, ˆ).

Lemma 4.4. Let P be a ﬁnite poset with ˆ and ˆ, and with M¨obius function µ.
Let ci denote the number of chains ˆ = y0 < y1 < · · · < yi = ˆ in P . Then

µ(ˆ, ˆ = −c1 + c2 − c3 + · · · .

Proof. We work in the incidence algebra I(P ). We have

µ(ˆ, ˆ = ζ −1(ˆ, ˆ)

= (δ + (ζ − δ))−1(ˆ, ˆ

= δ(ˆ, ˆ − (ζ − δ)(ˆ, ˆ) + (ζ − δ)2(ˆ, ˆ) − · · · .

This expansion is easily justiﬁed since (ζ −δ)k(ˆ, ˆ = 0 if the longest chain of P has
length less than k. By deﬁnition of the product in I(P ) we have (ζ − δ)i(ˆ, ˆ = ci,
and the proof follows. □
Note. Let P be a ﬁnite poset with ˆ and ˆ and let P ′ = P − {ˆ, ˆ}. Deﬁne
∆(P ′) to be the set of chains of P ′, so ∆(P ′) is an abstract simplicial complex. The
reduced Euler characteristic of a simplicial complex ∆ is deﬁned by

˜χ(P ) = −f−1 + f0 − f1 + · · · ,

where fi is the number of i-dimensional faces F ∈ ∆ (or #F = i + 1). Comparing
with Lemma 4.4 shows that
 µ(ˆ, ˆ = ˜χ(∆(P ′)).

Readers familiar with topology will know that ˜χ(∆) has important topological sig-
niﬁcance related to the homology of ∆. It is thus natural to ask whether results

LECTURE 4. BROKEN CIRCUITS AND MODULAR ELEMENTS 43

(a)

1 2 3
 321 3
1 2312
 3 2 1
 1

1 1
 1

3
 2 11

2 21

(b)
 (c)

Figure 2. Three examples of edge-labelings

concerning M¨obius functions can be generalized or reﬁned topologically. Such re-
sults are part of the subject of “topological combinatorics,” about which we will
say a little more later.
Now let P be a ﬁnite graded poset with ˆ and ˆ. Let

E(P ) = {(x, y) : x ⋖ y in P },

the set of (directed) edges of the Hasse diagram of P .

Deﬁnition 4.11. An E-labeling of P is a map λ : E(P ) → P such that if x < y in
P then there exists a unique saturated chain

C : x = x0 ⋖ x1 ⋖ x1 ⋖ · · · ⋖ xk = y

satisfying λ(x0, x1) ≤ λ(x1, x2) ≤ · · · ≤ λ(xk−1, xk).

We call C the increasing chain from x to y.

Figure 2 shows three examples of posets P with a labeling of their edges, i.e.
a map λ : E(P ) → P. Figure 2(a) is the boolean algebra B3 with the labeling
λ(S, S ∪ {i}) = i. (The one-element subsets {i} are also labelled with a small
i.) For any boolean algebra Bn, this labeling is the archetypal example of an E-
labeling. The unique increasing chain from S to T is obtained by adjoining to S
the elements of T − S one at a time in increasing order. Figures 2(b) and (c) show
two diﬀerent E-labelings of the same poset P . These labeling have a number of
diﬀerent properties, e.g., the ﬁrst has a chain whose edge labels are not all diﬀerent,
while every maximal chain label of Figure 2(c) is a permutation of {1, 2}.

Theorem 4.11. Let λ be an E-labeling of P , and let x ≤ y in P . Let µ denote
the M¨obius function of P . Then (−1)rk(x,y)µ(x, y) is equal to the number of strictly
decreasing saturated chains from x to y, i.e.,

(−1)rk(x,y)µ(x, y) =

#{x = x0 ⋖ x1 ⋖ · · · ⋖ xk = y : λ(x0, x1) > λ(x1, x2) > · · · > λ(xk−1, xk)}.

Proof. Since λ restricted to [x, y] (i.e., to E([x, y])) is an E-labeling, we can assume
[x, y] = [ˆ, ˆ] = P . Let S = {a1, a2, . . . , aj−1} ⊆ [n − 1], with a1 < a2 < · · · < aj−1.

44 , HYPERPLANE ARRANGEMENTS

Deﬁne αP (S) to be the number of chains ˆ < y1 < · · · < yj−1 < ˆ in P such that
rk(yi) = ai for 1 ≤ i ≤ j − 1. The function αP is called the ﬂag f -vector of P .
Claim. αP (S) is the number of maximal chains ˆ = x0 ⋖ x1 ⋖ · · · ⋖ xn = ˆ such
that λ(xi−1, xi) > λ(xi, xi+1) ⇒ i ∈ S, 1 ≤ i ≤ n.

To prove the claim, let ˆ = y0 < y1 < · · · < yj−1 < yj = ˆ with rk(yi) = ai for
1 ≤ i ≤ j − 1. By the deﬁnition of E-labeling, there exists a unique reﬁnement

ˆ = y0 = x0 ⋖ x1 ⋖ · · · ⋖ xa1 = y1 ⋖ xa1+1 ⋖ · · · ⋖ xa2 = y2 ⋖ · · · ⋖ xn = yj = ˆ

satisfying λ(x0, x1) ≤ λ(x1, x2) ≤ · · · ≤ λ(xa1 −1, xa1 )

λ(xa1 , xa1+1) ≤ λ(xa1+1, xa1+2) ≤ · · · ≤ λ(xa2 −1, xa2 )

· · ·

Thus if λ(xi−1, xi) > λ(xi, xi+1), then i ∈ S, so (23) is satisﬁed. Conversely, given
a maximal chain ˆ = x0 ⋖ x1 ⋖ · · · ⋖ xn = ˆ satisfying the above conditions on λ,
let yi = xai . Therefore we have a bijection between the chains counted by αP (S)
and the maximal chains satisfying (23), so the claim follows.
Now for S ⊆ [n − 1] deﬁne

(24) βP (S) = ∑

T ⊆S(−1)#(S−T )αP (T ).

The function βP is called the ﬂag h-vector of P . A simple Inclusion-Exclusion
argument gives

(25) αP (S) = ∑

T ⊆S βP (T ),

for all S ⊆ [n−1]. It follows from the claim and equation (25) that βP (T ) is equal to
the number of maximal chains ˆ = x0 ⋖ x1 ⋖ · · · ⋖ xn = ˆ such that λ(xi) > λ(xi+1)
if and only if i ∈ T . In particular, βP ([n − 1]) is equal to the number of strictly
decreasing maximal chains ˆ = x0 ⋖ x1 ⋖ · · · ⋖ xn = ˆ of P , i.e.,

λ(x0, x1) > λ(x1, x2) > · · · > λ(xn−1, xn).

Now by (24) we have

βP ([n − 1]) = ∑

T ⊆[n−1]
(−1)n−1−#T αP (T )

= ∑

k≥1
 ∑

ˆ y0<y1<···<yk=ˆ(−1)n−k

= (−1)n ∑

k≥1(−1)kck,

where ci is the number of chains ˆ = y0 < y1 < · · · < yi = ˆ in P . The proof now
follows from Philip Hall’s theorem (Lemma 4.4). □
We come to the main result of this subsection, a combinatorial interpretation
of the coeﬃcients of the characteristic polynomial χM (t) for any matroid M .

LECTURE 4. BROKEN CIRCUITS AND MODULAR ELEMENTS 45

5

1 2 3 4 5

3 3 2
4 2 5 1 4 5 5 4
2

5 54 4 25

1 2 3 4 5

2

Figure 3. The edge labeling ˜λ of a geometric lattice L(M )

Theorem 4.12. Let M be a matroid of rank n with a linear ordering x1 < x2 <
· · · < xm of its points (so the broken circuit complex BC(M ) is deﬁned), and let
0 ≤ i ≤ n. Then (−1)i[tn−i]χM (t) = fi−1(BC(M )).

Proof. We may assume M is simple since the “simpliﬁcation” ˆM has the same
lattice of ﬂats and same broken circuit complex as M (Exercise 1). The atoms xi of
L(M ) can then be identiﬁed with the points of M . Deﬁne a labeling ˜λ : E(L(M )) →
P as follows. Let x ⋖ y in L(M ). Then set

(26) ˜λ(x, y) = max{i : x ∨ xi = y}.

Note that ˜λ(x, y) is deﬁned since L(M ) is atomic.
As an example, Figure 3 shows the lattice of ﬂats of the matroid M of Figure 1
with the edge labeling (26).
Claim 1. Deﬁne λ : E(L(M )) → P by

λ(x, y) = m + 1 − ˜λ(x, y).

Then λ is an E-labeling.
To prove this claim, we need to show that for all x < y in L(M ) there is a
unique saturated chain x = y0 ⋖ y1 ⋖ · · · ⋖ yk = y satisfying

˜λ(y0, y1) ≥ ˜λ(y1, y2) ≥ · · · ≥ ˜λ(yk−1, yk).

The proof is by induction on k. There is nothing to prove for k = 1. Let k > 1 and
assume the assertion for k − 1. Let

j = max{i : xi ≤ y, xi ̸≤ x}.

For any saturated chain x = z0 ⋖ z1 ⋖ · · · ⋖ zk = y, there is some i for which
xj ̸≤ zi and xj ≤ zi+1. Hence ˜λ(zi, zi+1) = j. Thus if ˜λ(z0, z1) ≥ · · · ≥ ˜λ(zk−1, zk),
then ˜λ(z0, z1) = j. Moreover, there is a unique y1 satisfying x = x0 ⋖ y1 ≤ y and
˜λ(x0, y1) = j, viz., y1 = x0 ∨ xj. (Note that y1 ⋗ x0 by semimodularity.)

46 , HYPERPLANE ARRANGEMENTS

By the induction hypothesis there exists a unique saturated chain y1 ⋖ y2 ⋖
· · ·⋖yk = y satisfying ˜λ(y1, y2) ≥ · · · ≥ ˜λ(yk−1, yk). Since ˜λ(y0, y1) = j > ˜λ(y1, y2),
the proof of Claim 1 follows by induction.
Claim 2. The broken circuit complex BC(M ) consists of all chain labels λ(C),
where C is a saturated increasing chain (with respect to ˜λ) from ˆ to some x ∈
L(M ). Moreover, all such λ(C) are distinct.
To prove the distinctness of the labels λ(C), suppose that C is given by ˆ =
y0 ⋖ y1 ⋖ · · · ⋖ yk, with ˜λ(C) = (a1, a2, . . . , ak). Then yi = yi−1 ∨ xai , so C is the
only chain with its label.
Now let C and ˜λ(C) be as in the previous paragraph. We claim that the
set {xa1 , . . . , xak } contains no broken circuit. (We don’t even require that C is
increasing for this part of the proof.) Write zi = xai , and suppose to the contrary
that B = {zi1 , . . . , zij } is a broken circuit, with 1 ≤ i1 < · · · < ij ≤ k. Let B ∪ {xr}
be a circuit with r > ait for 1 ≤ t ≤ j. Now for any circuit {u1, . . . , uh} and any
1 ≤ i ≤ h we have

u1 ∨ u2 ∨ · · · ∨ uh = u1 ∨ · · · ∨ ui−1 ∨ ui+1 ∨ · · · ∨ uh.

Thus zi1 ∨ zi2 ∨ · · · ∨ zij−1 ∨ xr = ⋁

z∈B z = zi1 ∨ zi2 ∨ · · · ∨ zij .

Then yij −1 ∨ xr = yij , contradicting the maximality of the label aij . This proves
Claim 2.
To complete the proof of the theorem, note that we have shown that fi−1(BC(M ))
is the number of chains C : ˆ = y0 ⋖ y1 ⋖ · · · ⋖ yi such that ˜λ(C) is strictly increas-
ing, or equivalently, λ(C) is strictly decreasing. Since λ is an E-labeling, the proof
follows from Theorem 4.11. □

Corollary 4.5. The broken circuit complex BC(M ) is pure, i.e., every maximal
face has the same dimension.

Note (for readers with some knowledge of topology). Let M be a matroid on
the linearly ordered set u1 < u2 < · · · < um. Note that F ∈ BC(M ) if and only if
F ∪ {um} ∈ BC(M ). Deﬁne the reduced broken circuit complex BCr(M ) by

BCr(M ) = {F ∈ BC(M ) : um ̸∈ F }.

Thus BC(M ) = BCr(M ) ∗ um,

the join of BCr(M ) and the vertex um. Equivalently, BC(M ) is a cone over BCr(M )
with apex um. As a consequence, BC(M ) is contractible and therefore has the ho-
motopy type of a point. A more interesting problem is to determine the topological
nature of BCr(M ). It can be shown that BCr(M ) has the homotopy type of a wedge
of β(M ) spheres of dimension rank(M ) − 2, where (−1)rank(M )−1β(M ) = χ′ (1)
(the derivative of χM (t) at t = 1). See Exercise 20 for more information on β(M ).
As an example of the applicability of our results on matroids and geometric
lattices to arrangements, we have the following purely combinatorial description of
the number of regions of a real central arrangement.

Corollary 4.6. Let A be a central arrangement in Rn, and let M be the matroid
deﬁned by the normals to H ∈ A, i.e., the independent sets of M are the linearly

LECTURE 4. BROKEN CIRCUITS AND MODULAR ELEMENTS 47

independent normals. Then with respect to any linear ordering of the points of M ,
r(A) is the total number of subsets of M that don’t contain a broken circuit.

Proof. Immediate from Theorems 2.5 and 4.12. □

4.2. Modular elements

We next discuss a situation in which the characteristic polynomial χM (t) factors is
a nice way.

Deﬁnition 4.12. An element x of a geometric lattice L is modular if for all y ∈ L
we have

(27) rk(x) + rk(y) = rk(x ∧ y) + rk(x ∨ y).

Example 4.9. Let L be a geometric lattice.
(a) ˆ and ˆ are clearly modular (in any ﬁnite lattice).
(b) We claim that atoms a are modular.

Proof. Suppose that a ≤ y. Then a ∧ y = a and a ∨ y = y, so equation
(27) holds. (We don’t need that a is an atom for this case.) Now suppose
a ̸≤ y. By semimodularity, rk(a ∨ y) = 1 + rk(y), while rk(a) = 1 and
rk(a ∧ y) = rk(ˆ = 0, so again (27) holds. □

(c) Suppose that rk(L) = 3. All elements of rank 0, 1, or 3 are modular by
(a) and (b). Suppose that rk(x) = 2. Then x is modular if and only if for
all elements y ̸= x and rk(y) = 2, we have that rk(x ∧ y) = 1.
(d) Let L = Bn. If x ∈ Bn then rk(x) = #x. Moreover, for any x, y ∈ Bn we
have x ∧ y = x ∩ y and x ∨ y = x ∪ y. Since for any ﬁnite sets x and y we
have #x + #y = #(x ∩ y) + #(x ∨ y),
it follows that every element of Bn is modular. In other words, Bn is a
modular lattice.
(e) Let q be a prime power and Fq the ﬁnite ﬁeld with q elements. Deﬁne
Bn(q) to be the lattice of subspaces, ordered by inclusion, of the vector
space Fn. Note that Bn(q) is also isomorphic to the intersection lattice
of the arrangement of all linear hyperplanes in the vector space Fn(q).
Figure 4 shows the Hasse diagrams of B2(3) and B3(2).
Note that for x, y ∈ Bn(q) we have x ∧ y = x ∩ y and x ∨ y = x + y
(subspace sum). Clearly Bn(q) is atomic: every vector space is the join
(sum) of its one-dimensional subspaces. Moreover, Bn(q) is graded of rank
n, with rank function given by rk(x) = dim(x). Since for any subspaces
x and y we have

dim(x) + dim(y) = dim(x ∩ y) + dim(x + y),

it follows that L is a modular geometric lattice. Thus every x ∈ L is
modular.
Note. A projective plane R consists of a set (also denoted R) of
points, and a collection of subsets of R, called lines, such that: (a) every
two points lie on a unique line, (b) every two lines intersect in exactly one
point, and (c) (non-degeneracy) there exist four points, no three of which
are on a line. The incidence lattice L(R) of R is the set of all points

48 , HYPERPLANE ARRANGEMENTS

100 111
010 110 001 101 011

B (3) B (2)

2
 3

Figure 4. The lattices B2(3) and B3(2)

and lines of R, ordered by p < L if p ∈ L, with ˆ and ˆ adjoined. It
is an immediate consequence of the axioms that when R is ﬁnite, L(R)
is a modular geometric lattice of rank 3. It is an open (and probably
intractable) problem to classify all ﬁnite projective planes. Now let P and
Q be posets and deﬁne their direct product (or cartesian product) to be
the set
 P × Q = {(x, y) : x ∈ P, y ∈ Q},

ordered componentwise, i.e., (x, y) ≤ (x′, y′) if x ≤ y and x′ ≤ y′. It is easy
to see that if P and Q are geometric (respectively, atomic, semimodular,
modular) lattices, then so is P × Q (Exercise 7). It is a consequence of the
“fundamental theorem of projective geometry” that every ﬁnite modular
geometric lattice is a direct product of boolean algebras Bn, subspace
lattices Bn(q) for n ≥ 3, lattices of rank 2 with at least ﬁve elements
(which may be regarded as B2(q) for any q ≥ 2) and incidence lattices of
ﬁnite projective planes.

(f) The following result characterizes the modular elements of Πn, which is
the lattice of partitions of [n] or the intersection lattice of the braid ar-
rangement Bn.

Proposition 4.9. A partition π ∈ Πn is a modular element of Πn if
and only if π has at most one nonsingleton block. Hence the number of
modular elements of Πn is 2n − n.

Proof. If all blocks of π are singletons, then π = ˆ which is modular by
(a). Assume that π has the block A with r > 1 elements, and all other
blocks are singletons. Hence the number |π| of blocks of π is given by
n − r + 1. For any σ ∈ Πn, we have rk(σ) = n − |σ|. Let k = |σ| and

j = #{B ∈ σ : A ∩ B ̸= ∅}.

Then |π ∧ σ| = j + (n − r) and |π ∨ σ| = k − j + 1. Hence rk(π) = r − 1,
rk(σ) = n − k, rk(π ∧ σ) = r − j, and rk(π ∨ σ) = n − k + j − 1, so π is
modular.

LECTURE 4. BROKEN CIRCUITS AND MODULAR ELEMENTS 49

Conversely, let π = {B1, B2, . . . , Bk} with #B1 > 1 and #B2 > 1.
Let a ∈ B1 and b ∈ B2, and set

σ = {(B1 ∪ b) − a, (B2 ∪ a) − b, B3, . . . , Bk}.

Then |π| = |σ| = k
π ∧ σ = {a, b, B1 − a, B2 − b, . . . , B3, . . . , Bk} ⇒ |π ∧ σ| = k + 2

π ∨ σ = {B1 ∪ B2, B3, . . . , Bl} ⇒ |π ∨ σ| = k − 1.
Hence rk(π) + rk(σ) ̸= rk(π ∧ σ) + rk(π ∨ σ), so π is not modular. □

In a ﬁnite lattice L, a complement of x ∈ L is an element y ∈ L such that
x ∧ y = ˆ and x ∨ y = ˆ. For instance, in the boolean algebra Bn every element has
a unique complement. (See Exercise 3 for the converse.) The following proposition
collects some useful properties of modular elements. The proof is left as an exercise
(Exercises 4–5).

Proposition 4.10. Let L be a geometric lattice of rank n.
(a) Let x ∈ L. The following four conditions are equivalent.
(i) x is a modular element of L.
(ii) If x ∧ y = ˆ, then rk(x) + rk(y) = rk(x ∨ y).
(iii) If x and y are complements, then rk(x) + rk(y) = n.
(iv) All complements of x are incomparable.
(b) (transitivity of modularity) If x is a modular element of L and y is modular
in the interval [ˆ, x], then y is a modular element of L.
(c) If x and y are modular elements of L, then x ∧ y is also modular.

The next result, known as the modular element factorization theorem [16], is
our primary reason for deﬁning modular elements — such an element induces a
factorization of the characteristic polynomial.

Theorem 4.13. Let z be a modular element of the geometric lattice L of rank n.
Write χz(t) = χ[ˆ,z](t). Then

(28) χL(t) = χz(t)
  ∑

y : y∧z=ˆ µL(y)tn−rk(y)−rk(z)
 .

Example 4.10. Before proceeding to the proof of Theorem 4.13, let us consider
an example. The illustration below is the aﬃne diagram of a matroid M of rank
3, together with its lattice of ﬂats. The two lines (ﬂats of rank 2) labelled x and y
are modular by Example 4.9(c).

y
x x y

50 , HYPERPLANE ARRANGEMENTS

Hence by equation (28) χM (t) is divisible by χx(t). Moreover, any atom a of
the interval [ˆ, x] is modular, so χx(t) is divisible by χa(t) = t − 1. From this it
is immediate (e.g., because the characteristic polynomial χG(t) of any geometric
lattice G of rank n begins xn−axn−1+· · · , where a is the number of atoms of G) that
χx(t) = (t − 1)(t − 5) and χM (t) = (t − 1)(t − 3)(t − 5). On the other hand, since y is
modular, χM (t) is divisible by χy(t), and we get as before χy(t) = (t − 1)(t − 3) and
χM (t) = (t − 1)(t − 3)(t − 5). Geometric lattices whose characteristic polynomial
factors into linear factors in a similar way due to a maximal chain of modular
elements are discussed further beginning with Deﬁnition 4.13.

Our proof of Theorem 4.13 will depend on the following lemma of Greene [11].
We give a somewhat simpler proof than Greene.

Lemma 4.5. Let L be a ﬁnite lattice with M¨obius function µ, and let z ∈ L. The
following identity is valid in the M¨obius algebra A(L) of L:

(29) σˆ := ∑

x∈L µ(x)x =
 ∑

v≤z µ(v)v

  ∑

y∧z=ˆ µ(y)y
 .

Proof. Let σs for s ∈ L be given by (refeq:sigmas). The right-hand side of equation
(29) is then given by

∑

v≤z
y∧z=ˆ
 µ(v)µ(y)(v ∨ y) = ∑

v≤z
y∧z=ˆ
 µ(v)µ(y) ∑

s≥v∨y σs

= ∑

s σs ∑

v≤s,v≤z
y≤s,y∧z=ˆ
 µ(v)µ(y)

= ∑

s σs
 
 ∑

v≤s∧z µ(v)

︸
 ︷︷ ︸
δˆ,s∧z
 
  ∑≤s
y∧z=ˆ
 µ(y)


= ∑

s∧z=ˆ σs
 
 ∑≤s
y∧z=ˆ (redundant)
 µ(y)

︸
 ︷︷ ︸
δˆ,s
 

= σˆ.
 □
Proof of Theorem 4.13. We are assuming that z is a modular element of
the geometric lattice L.
Claim 1. Let v ≤ z and y ∧ z = ˆ (so v ∧ y = ˆ Then z ∧ (v ∨ y) = v (as
illustrated below).

LECTURE 4. BROKEN CIRCUITS AND MODULAR ELEMENTS 51

y

z   y

z
 v
 0

v
 v   yv

Proof of Claim 1. Clearly z ∧ (v ∨ y) ≥ v, so it suﬃces to show that rk(z ∧ (v ∨
y)) ≤ rk(v). Since z is modular we have

rk(z ∧ (v ∨ y)) = rk(z) + rk(v ∨ y) − rk(z ∨ y)
= rk(z) + rk(v ∨ y) − (rk(z) + rk(y) − rk(z ∧ y)
︸ ︷︷ ︸
0
 )

= rk(v ∨ y) − rk(y)
≤ (rk(v) + rk(y) − rk(v ∧ y)
︸ ︷︷ ︸
0
 ) − rk(y) by semimodularity

= rk(v),

proving Claim 1.
Claim 2. With v and y as above, we have rk(v ∨ y) = rk(v) + rk(y).
Proof of Claim 2. By the modularity of z we have

rk(z ∧ (v ∨ y)) + rk(z ∨ (v ∨ y)) = rk(z) + rk(v ∨ y).

By Claim 1 we have rk(z ∧ (v ∨ y)) = rk(v). Moreover, again by the modularity of
z we have

rk(z ∨ (v ∨ y)) = rk(z ∨ y) = rk(z) + rk(y) − rk(z ∧ y) = rk(z) + rk(y).

It follows that rk(v) + rk(y) = rk(v ∨ y), as claimed.
Now substitute µ(v)v → µ(v)trk(z)−rk(v) and µ(y)y → µ(y)tn−rk(y)−rk(z) in the
right-hand side of equation (29). Then by Claim 2 we have

vy → tn−rk(v)−rk(y) = tn−rk(v∨y).

Now v ∨ y is just vy in the M¨obius algebra A(L). Hence if we further substi-
tute µ(x)x → µ(x)tn−rk(x) in the left-hand side of (29), then the product will be
preserved. We thus obtain

∑

x∈L µ(x)tn−rk(x)

︸ ︷︷ ︸
χL(t)
 =
 
∑≤z µ(v)trk(z)−rk(v)

︸
 ︷︷ ︸
χz (t)
 
  ∑

y∧z=ˆ µ(y)tn−rk(y)−rk(z)
 ,

as desired. □

52 , HYPERPLANE ARRANGEMENTS

Corollary 4.7. Let L be a geometric lattice of rank n and a an atom of L. Then

χL(t) = (t − 1) ∑

y∧a=ˆ µ(y)tn−1−rk(y).

Proof. The atom a is modular (Example 4.9(b)), and χa(t) = t − 1. □

4.3. Supersolvable lattices

For some geometric lattices L, there are “enough” modular elements to give a
factorization of χL(t) into linear factors.

Deﬁnition 4.13. A geometric lattice L is supersolvable if there exists a modular
maximal chain, i.e., a maximal chain ˆ = x0 ⋖ x1 ⋖ · · · ⋖ xn = ˆ such that each xi
is modular. A central arrangement A is supersolvable if its intersection lattice LA
is supersolvable.

Note. Let ˆ = x0 ⋖ x1 ⋖ · · · ⋖ xn = ˆ be a modular maximal chain of the
geometric lattice L. Clearly then each xi−1 is a modular element of the interval
[ˆ, xi]. The converse follows from Proposition 4.10(b): if ˆ = x0 ⋖ x1 ⋖ · · · ⋖ xn = ˆ
is a maximal chain for which each xi−1 is modular in [ˆ, xi], then each xi is modular
in L.
Note. The term “supersolvable” comes from group theory. A ﬁnite group Γ
is supersolvable if and only if its subgroup lattice contains a maximal chain all of
whose elements are normal subgroups of Γ. Normal subgroups are “nice” analogues
of modular elements; see [17, Example 2.5] for further details.

Corollary 4.8. Let L be a supersolvable geometric lattice of rank n, with modular
maximal chain ˆ = x0 ⋖ x1 ⋖ · · · ⋖ xn = ˆ. Let T denote the set of atoms of L, and
set ci = #{a ∈ T : a ≤ xi, a ̸≤ xi−1}.

Then χL(t) = (t − c1)(t − c2) · · · (t − cn).

Proof. Since xn−1 is modular, we have

y ∧ xn−1 = ˆ ⇔ y ∈ T and y ̸≤ xn−1, or y = ˆ.

By Theorem 4.13 we therefore have

χL(t) = χxn−1(t)
  ∑

a∈T
a̸≤xn−1
 µ(a)tn−rk(a)−rk(xn−1) + µ(ˆ tn−rk(ˆ −rk(xn−1)
 .

Since µ(a) = −1, µ(ˆ) = 1, rk(a) = 1, rk(ˆ = 0, and rk(xn−1) = n − 1, the
expression in brackets is just t − cn. Now continue this with L replaced by [ˆ, xn−1]
(or use induction on n). □

Example 4.11. (a) Let L = Bn, the boolean algebra of rank n. By Exam-
ple 4.9(d) every element of Bn is modular. Hence Bn is supersolvable.
Clearly each ci = 1, so χBn(t) = (t − 1)n.
(b) Let L = Bn(q), the lattice of subspaces of Fq . By Example 4.9(e) every
element of Bn(q) is modular, so Bn(q) is supersolvable. If [k
j] denotes the

LECTURE 4. BROKEN CIRCUITS AND MODULAR ELEMENTS 53

number of j-dimensional subspaces of a k-dimensional vector space over
Fq, then
 ci = [i
1] − [i−1
1 ]

= qi − 1
q − 1 − qi−1 − 1
q − 1

= qi−1.

Hence
 χBn(q)(t) = (t − 1)(t − q)(t − q2) · · · (t − qn−1).

In particular, setting t = 0 gives

µBn(q)(ˆ = (−1)nq(n
2).

Note. The expression [
k
j] is called a q-binomial coeﬃcient. It is a
polynomial in q with many interesting properties. For the most basic
properties, see e.g. [18, pp. 27–30].
(c) Let L = Πn, the lattice of partitions of the set [n] (a geometric lattice of
rank n − 1). By Proposition 4.9, a maximal chain of Πn is modular if and
only if it has the form ˆ = π0 ⋖ π1 ⋖ · · · ⋖ πn−1 = ˆ where πi for i > 0 has
exactly one nonsingleton block Bi (necessarily with i + 1 elements), with
B1 ⊂ B2 · · · ⊂ Bn−1 = [n]. In particular, Πn is supersolvable and has
exactly n!/2 modular chains for n > 1. The atoms covered by πi are the
partitions with one nonsingleton block {j, k} ⊆ Bi. Hence πi lies above
exactly (i+1
2 ) atoms, so

ci = (i + 1
2
 ) − (i
2

) = i.

It follows that χΠn(t) = (t − 1)(t − 2) · · · (t − n + 1) and µΠn(ˆ =
(−1)n−1(n − 1)!. Compare Corollary 2.2. The polynomials χBn(t) and
χΠn(t) diﬀer by a factor of t because Bn(t) is an arrangement in K n of
rank n − 1. In general, if A is an arrangement and ess(A) its essentializa-
tion, then

(30) trk(ess(A))χA(t) = trk(A)χess(A)(t).

(See Lecture 1, Exercise 2.)

Note. It is natural to ask whether there is a more general class of geometric
lattices L than the supersolvable ones for which χL(t) factors into linear factors
(over Z). There is a profound such generalization due to Terao [22] when L is an
intersection poset of a linear arrangement A in K n. Write K[x] = K[x1, . . . , xn]
and deﬁne
 T(A) = {(p1, . . . , pn) ∈ K[x]n : pi(H) ⊆ H for all H ∈ A}.

Here we are regarding (p1, . . . , pn) : K n → K n, viz., if (a1, . . . , an) ∈ K n, then

(p1, . . . , pn)(a1, . . . , an) = (p1(a1, . . . , an), . . . , pn(a1, . . . , an)).

The K[x]-module structure K[x] × T(A) → T(A) is given explicitly by

q · (p1, . . . , pn) = (qp1, . . . , qpn).

54 , HYPERPLANE ARRANGEMENTS

Figure 5. A graph with eight blocks

Note, for instance, that we always have (x1, . . . , xn) ∈ T(A). Since A is a linear
arrangement, T(A) is indeed a K[x]-module. (We have given the most intuitive
deﬁnition of the module T(A), though it isn’t the most useful deﬁnition for proofs.)
It is easy to see that T(A) has rank n as a K[x]-module, i.e., T(A) contains n,
but not n + 1, elements that are linearly independent over K[x]. We say that A
is a free arrangement if T(A) is a free K[x]-module, i.e., there exist Q1, . . . , Qn ∈
T(A) such that every element Q ∈ T(A) can be uniquely written in the form
Q = q1Q1 + · · · + qnQn, where qi ∈ K[x]. It is easy to see that if T(A) is free,
then the basis {Q1, . . . , Qn} can be chosen to be homogeneous, i.e., all coordinates
of each Qi are homogeneous polynomials of the same degree di. We then write
di = deg Qi. It can be shown that supersolvable arrangements are free, but there
are also nonsupersolvable free arrangements. The property of freeness seems quite
subtle; indeed, it is unknown whether freeness is a matroidal property, i.e., depends
only on the intersection lattice LA (regarding the ground ﬁeld K as ﬁxed). The
remarkable “factorization theorem” of Terao is the following.

Theorem 4.14. Suppose that T(A) is free with homogeneous basis Q1, . . . , Qn. If
deg Qi = di then χA(t) = (t − d1)(t − d2) · · · (t − dn).

We will not prove Theorem 4.14 here. A good reference for this subject is [13,
Ch. 4].
Returning to supersolvability, we can try to characterize the supersolvable prop-
erty for various classes of geometric lattices. Let us consider the case of the bond
lattice LG of the graph G. A graph H with at least one edge is doubly connected if
it is connected and remains connected upon the removal of any vertex (and all in-
cident edges). A maximal doubly connected subgraph of a graph G is called a block
of G. For instance, if G is a forest then its blocks are its edges. Two diﬀerent blocks
of G intersect in at most one vertex. Figure 5 shows a graph with eight blocks, ﬁve
of which consist of a single edge. The following proposition is straightforward to
prove (Exercise 15).

Proposition 4.11. Let G be a graph with blocks G1, . . . , Gk. Then

LG ∼ LG1 × · · · × LGk .

LECTURE 4. BROKEN CIRCUITS AND MODULAR ELEMENTS 55

It is also easy to see that if L1 and L2 are geometric lattices, then L1 and
L2 are supersolvable if and only if L1 × L2 is supersolvable (Exercise 17). Hence
in characterizing supersolvable graphs G (i.e., graphs whose bond lattice LG is
supersolvable) we may assume that G is doubly connected. Note that for any
connected (and hence a fortiori doubly connected) graph G, any coatom π of LG
has exactly two blocks.

Proposition 4.12. Let G be a doubly connected graph, and let π = {A, B} be a
coatom of the bond lattice LG, where #A ≤ #B. Then π is a modular element of
LG if and only if #A = 1, say A = {v}, and the neighborhood N (v) (the set of
vertices adjacent to v) forms a clique (i.e., any two distinct vertices of N (v) are
adjacent).

Proof. The proof parallels that of Proposition 4.9, which is a special case. Suppose
that #A > 1. Since G is doubly connected, there exist u, v ∈ A and u′, v′ ∈ B such
that u ̸= v, u′ ̸= v′, uu′ ∈ E(G), and vv′ ∈ E(G). Set σ = {(A∪u′)−v, (B∪v)−u′}.
If G has n vertices then rk(π) = rk(σ) = n−2, rk(π∨σ) = n−1, and rk(π∧σ) = n−4.
Hence π is not modular.
Assume then that A = {v}. Suppose that av, bv ∈ E(G) but ab ̸∈ E(G). We
need to show that π is not modular. Let σ = {A − {a, b}, {a, b, v}}. Then

σ ∨ π = ˆ, σ ∧ π = {A − {a, b}, a, b, v}

rk(σ) = rk(π) = n − 2, rk(σ ∨ π) = n − 1, rk(σ ∧ π) = n − 4.
Hence π is not modular.
Conversely, let π = {A, v}. Assume that if av, bv ∈ E(G) then ab ∈ E(G).
It is then straightforward to show (Exercise 8) that π is modular, completing the
proof. □
As an immediate consequence of Propositions 4.10(b) and 4.12 we obtain a
characterization of supersolvable graphs.

Corollary 4.9. A graph G is supersolvable if and only if there exists an ordering
v1, v2, . . . , vn of its vertices such that if i < k, j < k, vivk ∈ E(G) and vjvk ∈ E(G),
then vivj ∈ E(G). Equivalently, in the restriction of G to the vertices v1, v2, . . . , vi,
the neighborhood of vi is a clique.

Note. Supersolvable graphs G had appeared earlier in the literature under the
names chordal, rigid circuit, or triangulated graphs. One of their many characteri-
zations is that any circuit of length at least four contains a chord. Equivalently, no
induced subgraph of G is a k-cycle for k ≥ 4.

56 , HYPERPLANE ARRANGEMENTS

Exercises
(1) [2–] Let M be a matroid on a linearly ordered set. Show that BC(M ) = BC( ˆM ),
where ˆM is deﬁned by equation (20).
(2) [2+] Let M be a matroid of rank at least one. Show that the coeﬃcients of the
polynomial χM (t)/(t − 1) alternate in sign.
(3) [2+] Let L be ﬁnite lattice for which every element has a unique complement.
Show that L is isomorphic to a boolean algebra Bn. (What about inﬁnite lattices
with ˆ and ˆ
(4) [3–] Let x be an element of a geometric lattice L. Show that the following four
conditions are equivalent.
(i) x is a modular element of L.
(ii) If x ∧ y = ˆ then
 rk(x) + rk(y) = rk(x ∨ y).

(iii) If x and y are complements, then rk(x) + rk(y) = n.
(iv) All complements of x are incomparable.
(5) [2+] Let x, y be modular elements of a geometric lattice L. Show that x ∧ y is
also modular.
(6) [2] Let L be a geometric lattice. Prove or disprove: if x is modular in L and y
is modular in the interval [x, ˆ then y is modular in L.
(7) [2–] Let L and L′ be ﬁnite lattices. Show that if both L and L′ are geometric
(respectively, atomic, semimodular, modular) lattices, then so is L × L′.
(8) [2] Let G be a (loopless) connected graph and v ∈ V (G). Let A = V (G) − v and
π = {A, v} ∈ LG. Suppose that whenever av, bv ∈ E(G) we have ab ∈ E(G).
Show that π is a modular element of LG.
(9) [2+] Generalize the previous exercise as follows. Let G be a doubly-connected
graph with lattice of contractions LG. Let π ∈ LG. Show that the following two
conditions are equivalent.
(a) π is a modular element of LG.
(b) π satisﬁes the following two properties:
(i) At most one block B of π contains more than one vertex of G.
(ii) Let H be the subgraph induced by the block B of (i). Let K be any
connected component of the subgraph induced by G − B, and let H1
be the graph induced by the set of vertices in H that are connected
to some vertex in K. Then H1 is a clique (complete subgraph) of G.
(10) [2+] Let L be a geometric lattice of rank n, and ﬁx x ∈ L. Show that

χL(t) = ∑

y∈L
x∧y=ˆ
 µ(y)χLy (t)tn−rk(x∨y),

where Ly is the image of the interval [ˆ, x] under the map z ↦→ z ∨ y.
(11) [2+] Let I(M ) be the set of independent sets of a matroid M . Find another
matroid N and a labeling of its points for which I(M ) = BCr(N ), the reduced
broken circuit complex of N .
(12) (a) [2+] If ∆ and Γ are simplicial complexes on disjoint sets A and B, respec-
tively, then deﬁne the join ∆ ∗ Γ to be the simplicial complex on the set
A ∪ B with faces F ∪ G, where F ∈ ∆ and G ∈ Γ. (E.g., if Γ consists of
a single point then ∆ ∗ Γ is the cone over ∆. If Γ consists of two disjoint

LECTURE 4. BROKEN CIRCUITS AND MODULAR ELEMENTS 57

points, then ∆ ∗ Γ is the suspension of ∆.) We say that ∆ and Γ are join-
factors of ∆ ∗ Γ. Now let M be a matroid and S ⊂ M a modular ﬂat, i.e., S
is a modular element of LM . Order the points of M such that if p ∈ S and
q ̸∈ S, then p < q. Show that BC(S) is a join-factor of BC(M ). Deduce
that χM (t) is divisible by χS(t).
(b) [2+] Conversely, let M be a matroid and S ⊂ M . Label the points of M so
that if p ∈ S and q ̸∈ S, then p < q. Suppose that BC(S) is a join-factor of
BC(M ). Show that S is modular.
(13) [1] Show that all geometric lattices of rank two are supersolvable.
(14) [2] Give an example of two nonisomorphic supersolvable geometric lattices of
rank 3 with the same characteristic polynomials.
(15) [2] Prove Proposition 4.11: if G is a graph with blocks G1, . . . , Gk, then LG ∼
LG1 × · · · × LGk .
(16) [2+] Give an example of a nonsupersolvable geometric lattice of rank three whose
characteristic polynomial has only integer zeros.
(17) [2] Let L1 and L2 be geometric lattices. Show that L1 and L2 are supersolvable
if and only if L1 × L2 is supersolvable.
(18) [3–] Let L be a supersolvable geometric lattice. Show that every interval of L is
also supersolvable.
(19) [2] (a) Find the number of maximal chains of the partition lattice Πn.
(b) Find the number of modular maximal chains of Πn.
(20) Let M be a matroid with a linear ordering of its points. The internal activity of
a basis B is the number of points p ∈ B such that p < q for all points q ̸= p not
in the closure B − p of B − p. The external activity of B is the number of points
p′ ∈ M − B such that p′ < q′ for all q′ ̸= p′ contained in the unique circuit that
is a subset of B ∪ {p′}. Deﬁne the Crapo beta invariant of M by

β(M ) = (−1)rk(M )−1χ ′
M (1),

where ′ denotes diﬀerentiation.
(a) [1+] Show that 1−χ ′
M (1) = ψ(BCr), the Euler characteristic of the reduced
broken circuit complex of M .
(b) [3–] Show that β(M ) is equal to the number of bases of M with internal
activity 0 and external activity 0.
 LECTURE 5
Finite ﬁelds

5.1. The ﬁnite ﬁeld method

In this lecture we will describe a method based on ﬁnite ﬁelds for computing the
characteristic polynomial of an arrangement deﬁned over Q. We will then discuss
several interesting examples. The main result (Theorem 5.15) is implicit in the
work of Crapo and Rota [9, §17]. It was ﬁrst developed into a systematic tool for
computing characteristic polynomials by Athanasiadis [1][2], after a closely related
but not as general technique was presented by Blass and Sagan [6].
Suppose that the arrangement A is deﬁned over Q. By multiplying each hyper-
plane equation by a suitable integer, we may assume A is deﬁned over Z. In that
case we can take coeﬃcients modulo a prime p and get an arrangement Aq deﬁned
over the ﬁnite ﬁeld Fq, where q = pr. We say that A has good reduction mod p (or
over Fq) if L(A) ∼ L(Aq).
For instance, let A be the aﬃne arrangement in Q1 = Q consisting of the points
0 and 10. Then L(A) contains three elements, viz., Q, {0}, and {10}. If p ̸= 2, 5
then 0 and 10 remain distinct, so A has good reduction. On the other hand, if
p = 2 or p = 5 then 0 = 10 in Fp, so L(Ap) contains just two elements. Hence A
has bad reduction when p = 2, 5.

Proposition 5.13. Let A be an arrangement deﬁned over Z. Then A has good
reduction for all but ﬁnitely many primes p.

Proof. Let H1, . . . , Hj be aﬃne hyperplanes, where Hi is given by the equation
vi · x = ai (vi, ai ∈ Zn). By linear algebra, we have H1 ∩ · · · ∩ Hj = ∅ if and only if

(31) rank
 
 v1 a1
. .
vj aj
  = rank
 
 v1
.
vj
  .

Moreover, if (31) holds then

dim(H1 ∩ · · · ∩ Hj) = n − rank
 
 v1
.
vj
  .

59

60 , HYPERPLANE ARRANGEMENTS

Now for any r ×s matrix A, we have rank(A) ≥ t if and only if every t×t submatrix
B satisﬁes det(B) ̸= 0. It follows that L(A) ̸∼ L(Ap) if and only if at least one
member S of a certain ﬁnite collection S of subsets of integer matrices B satisﬁes
the following condition:

(∀B ∈ S) det(B) ̸= 0 but det(B) ≡ 0 (mod p).

This can only happen for ﬁnitely many p, viz., for certain B we must have p| det(B),
so L(A) ∼ L(Ap) for p suﬃciently large. □
The main result of this section is the following. Like many fundamental results
in combinatorics, the proof is easy but the applicability very broad.

Theorem 5.15. Let A be an arrangement in Qn, and suppose that L(A) ∼ L(Aq)
for some prime power q. Then

χA(q) = #
 Fn − ⋃

H∈Aq H


= qn − # ⋃

H∈Aq H.

Proof. Let x ∈ L(Aq) so #x = qdim(x). Here dim(x) can be computed either over
Q or Fq. Deﬁne two functions f, g : L(Aq) → Z by

f (x) = #x

g(x) = #
 (

x − ⋃

y>x y
)
 .

In particular,
 g(ˆ) = g(Fn) = #
 Fn − ⋃

H∈Aq H
 .

Clearly
 f (x) = ∑

y≥x g(y).

Let µ denote the M¨obius function of L(A) ∼ L(Aq). By M¨obius inversion (Theo-
rem 1.1),
 g(x) = ∑

y≥x µ(x, y)f (y)

= ∑

y≥x µ(x, y)qdim(y).

Put x = ˆ to get
 g(ˆ) = ∑

y µ(y)qdim(y) = χA(q).
 □
For the remainder of this lecture, we will be concerned with applications of
Theorem 5.15 and further interesting examples of arrangements.

LECTURE 5. FINITE FIELDS 61

Example 5.12. Let G be a graph with vertices 1, 2, . . . , n, so

QAG(x) = ∏

ij∈E(G)(xi − xj ).

Then by Theorem 5.15,

χAG (q) = qn − #{(α1, . . . , αn) ∈ Fn : αi = αj for some ij ∈ E(G)}

= #{(β1, . . . , βn) ∈ Fn : βi ̸= βj ∀ ij ∈ E(G)}

= χG(q),

in agreement with Theorem 2.7. Note that this equality holds for all prime powers
q, not just for pm with p ≫ 0. This is because the matrix with rows ei − ej, where
ij ∈ E(G) and ei is the ith unit coordinate vector in Qn, is totally unimodular, i.e.,
every minor (determinant of a square submatrix) is 0, ±1. Hence the nonvanishing
of a minor is independent of the ambient ﬁeld.

A very interesting class of arrangements, including the braid arrangement, is
associated with root systems, or more generally, ﬁnite reﬂection groups. We will
simply mention some basic results here without proof. A root system is a ﬁnite
set R of nonzero vectors in Rn satisfying certain properties that we will not give
here. (References include [4][7][12].) The Coxeter arrangement A(R) consists of
the hyperplanes α · x = 0, where α ∈ R. There are four inﬁnite (irreducible) classes
of root systems (all in Rn):

An−1 = {ei − ej : 1 ≤ i < j ≤ n} = Bn
Dn = {ei − ej, ei + ej : 1 ≤ i < j ≤ n}
Bn = Dn ∪ {ei : 1 ≤ i ≤ n}

Cn = Dn ∪ {2ei : 1 ≤ i ≤ n}.

We should really regard An−1 as being a subset of the space

{(α1, . . . , αn) ∈ Rn : ∑ αi = 0} ∼ Rn−1.

We thus obtain the following Coxeter arrangements. In all cases 1 ≤ i < j ≤ n
and 1 ≤ k ≤ n.
 A(An−1) = Bn : xi − xj = 0

A(Bn) = A(Cn) : xi − xj = 0, xi + xj = 0, xk = 0
A(Dn) : xi − xj = 0, xi + xj = 0.

See Figure 1 for the arrangements A(B2) and A(D2).
Let us compute the characteristic polynomial χA(Bn)(q). For p ≫ 0 (actually
p > 2) and q = pm we have

χA(Bn)(q) = #{(α1, . . . , αn) ∈ Fn : αi ̸= ±αj (i ̸= j), αi ̸= 0 (1 ≤ i ≤ n)}.

Choose α1 ∈ F∗ = Fq − {0} in q − 1 ways. Then choose α2 ∈ F∗ − {α1, −α1} in
q − 3 ways, then α3 in q − 5 ways, etc., to obtain:

χA(Bn)(t) = (t − 1)(t − 3) · · · (t − (2n − 1)).

In particular,
r(A(Bn)) = (−1)nχA(Bn)(−1) = 2 · 4 · 6 · · · (2n) = 2nn!.

62 , HYPERPLANE ARRANGEMENTS

A(B  ) A(D  )22

Figure 1. The arrangements A(B2) and A(D2)

By a similar but slightly more complicated argument we get (Exercise 1)

(32) χA(Dn)(t) = (t − 1)(t − 3) · · · (t − (2n − 3)) · (t − n + 1).

Note. Coxeter arrangements are always free in the sense of Theorem 4.14 (a result
of Terao [21]), but need not be supersolvable. In fact, A(An) and A(Bn) are
supersolvable, but A(Dn) is not supersolvable for n ≥ 4 [3, Thm. 5.1].

5.2. The Shi arrangement

We next consider a modiﬁcation (or deformation) of the braid arrangement called
the Shi arrangement [15, §7] and denoted Sn. It consists of the hyperplanes

xi − xj = 0, 1, 1 ≤ i < j ≤ n.

Thus Sn has n(n − 1) hyperplanes and rank(Sn) = n − 1. Figure 2 shows the Shi
arrangement S3 in ker(x1 + x2 + x3) ∼ R2 (i.e., the space {(x1, x2, x3) ∈ R3 :
x1 + x2 + x3 = 0}).

Theorem 5.16. The characteristic polynomial of Sn is given by

χSn(t) = t(t − n)n−1.

Proof. Let p be a large prime. By Theorem 5.15 we have

χSn(p) = #{(α1, . . . , αn) ∈ Fn : i < j ⇒ αi ̸= αj and αi ̸= αj + 1}.

Choose a weak ordered partition π = (B1, . . . , Bp−n) of [n] into p − n blocks, i.e.,⋃ Bi = [n] and Bi ∩ Bj = ∅ if i ̸= j, such that 1 ∈ B1. (“Weak” means that we
allow Bi = ∅.) For 2 ≤ i ≤ n there are p − n choices for j such that i ∈ Bj, so
(p−n)n−1 choices in all. We will illustrate the following argument with the example
p = 11, n = 6, and

(33) π = ({1, 4}, {5}, ∅, {2, 3, 6}, ∅).

Arrange the elements of Fp clockwise on a circle. Place 1, 2, . . . , n on some n of
these points as follows. Place elements of B1 consecutively (clockwise) in increasing
order with 1 placed at some element α1 ∈ Fp. Skip a space and place the elements
of B2 consecutively in increasing order. Skip another space and place the elements
of B3 consecutively in increasing order, etc. For our example (33), say α1 = 6.

LECTURE 5. FINITE FIELDS 63

Figure 2. The Shi arrangement S3 in ker(x1 + x2 + x3)

0 1
 2

3

4
5
6

7

8
 9 10 2
 6

3

1

4
 5

Let αi be the position (element of Fp) at which i was placed. For our example
we have (α1, α2, α3, α4, α5, α6) = (6, 1, 2, 7, 9, 3).
It is easily veriﬁed that we have deﬁned a bijection from the (p−n)n−1 weak ordered
partitions π = (B1, . . . , Bp−n) of [n] into p−n blocks such that 1 ∈ B1, together with
the choice of α1 ∈ Fp, to the set Fn −∪H∈(Sn)pH. There are (p−n)n−1 choices for π
and p choices for α1, so it follows from Theorem 5.15 that χSn(t) = t(t − n)n−1. □
We obtain the following corollary immediately from Theorem 2.5.

Corollary 5.10. We have r(Sn) = (n + 1)n−1 and b(Sn) = (n − 1)n−1.

Note. Since r(Sn) and b(Sn) have such simple formulas, it is natural to ask
for a direct bijective proof of Corollary 5.10. A number of such proofs are known;
a sketch that r(Sn) = (n + 1)n−1 is given in Exercise 3.

64 , HYPERPLANE ARRANGEMENTS

Note. It can be shown that the cone cSn is not supersolvable for n ≥ 3 (Ex-
ercise 4) but is free in the sense of Theorem 4.14.

5.3. Exponential sequences of arrangements

The braid arrangement (in fact, any Coxeter arrangement) is highly symmetrical;
indeed, the group of linear transformations that preserves the arrangement acts
transitively on the regions. Thus all regions “look the same.” The Shi arrangement
lacks this symmetry, but it still possesses a kind of “combinatorial symmetry” that
allows us to express the characteristic polynomials χSn(t), for all n ≥ 1, in terms
of the number r(Sn) of regions.

Deﬁnition 5.14. A sequence A = (A1, A2, . . . ) of arrangements is called an expo-
nential sequence of arrangements (ESA) if it satisﬁes the following three conditions.
(1) An is in K n for some ﬁeld K (independent of n).
(2) Every H ∈ An is parallel to some hyperplane H ′ in the braid arrangement
Bn (over K).
(3) Let S be a k-element subset of [n], and deﬁne

AS = {H ∈ An : H is parallel to xi − xj = 0 for some i, j ∈ S}.

Then L(AS) ∼ L(Ak).

Examples of ESA’s are given by An = Bn or An = Sn. In fact, in these cases
we have AS ∼ Ak × K n−k.
The combinatorial properties of ESA’s are related to the exponential formula
in the theory of exponential generating functions [19, §5.1], which we now review.
Informally, we are dealing with “structures” that can be put on a vertex set V such
that each structure is a disjoint union of its “connected components.” We obtain a
structure on V by partitioning V and placing a connected structure on each block
(independently). Examples of such structures are graphs, forests, and posets, but
not trees or groups. Let h(n) be the total number of structures on an n-set V (with
h(0) = 1), and let f (n) be the number that are connected. The exponential formula
states that

(34) ∑

n≥0 h(n) xn

n! = exp ∑

n≥1 f (n) xn

n! .

More precisely, let f : P → R, where R is a commutative ring. (For our purposes,
R = Z will do.) Deﬁne a new function h : N → R by h(0) = 1 and

(35) h(n) = ∑

π={B1,...,Bk}∈Πn f (#B1)f (#B2) · · · f (#Bk).

Then equation (34) holds. A straightforward proof can be given by considering the
expansion
 exp ∑

n≥1 f (n) xn

n! = ∏

n≥1 exp f (n) xn

n!

= ∏

n≥1
 ∑

k≥0 f (n)k xkn

n!kk!
  .

We omit the details (Exercise 5).

LECTURE 5. FINITE FIELDS 65

For any arrangement A in K n, deﬁne r(A) = (−1)nχA(−1). Of course if K = R
this coincides with the deﬁnition of r(A) as the number of regions of A. We come
to the main result concering ESA’s.

Theorem 5.17. Let A = (A1, A2, . . . ) be an ESA. Then

∑

n≥0 χAn(t) xn

n! =
 ∑

n≥0(−1)nr(An) xn

n!
 
−t
 .

Example 5.13. For A = (B1, B2, . . . ) Theorem 5.17 asserts that

∑

n≥0 t(t − 1) · · · (t − n + 1) xn

n! =
 ∑

n≥0(−1)nn! xn

n!
 

−t
 ,

as immediately follows from the binomial theorem. On the other hand, if A =
(S1, S2, . . . ), then we obtain the much less obvious identity

∑

n≥0 t(t − n)n−1 xn

n! =
 ∑

n≥0(−1)n(n + 1)n−1 xn

n!
 

−t
 .

Proof of Theorem 5.17. By Whitney’s theorem (Theorem 2.4) we have for
any arrangement A in K n that

χA(t) = ∑

B⊆A
B central

(−1)#Btn−rank(B).

Let A = (A1, A2, . . . ), and let B ⊆ An for some n. Deﬁne π(B) ∈ Πn to have blocks
that are the vertex sets of the connected components of the graph G on [n] with
edges E(G) = {ij : ∃ xi − xj = c in B}.

Deﬁne
 ˜χAn(t) = ∑

B⊆A
B central
π(B)=[n]

(−1)#Btn−rk(B).

Then
 χAn(t) = ∑

π={B1,...,Bk}∈Πn
 ∑

B⊆A
B central
π(B)=π
 (−1)#Btn−rk(B)

= ∑

π={B1,...,Bk}∈Πn ˜χA#B1 (t) ˜χA#B2 (t) · · · ˜χA#Bk (t).

Thus by the exponential formula (34),

∑

n≥0 χAn(t) xn

n! = exp ∑

n≥1 ˜χAn(t) xn

n! .

66 , HYPERPLANE ARRANGEMENTS

But π(B) = [n] if and only if rk(B) = n − 1, so ˜χAn(t) = cnt for some cn ∈ Z. We
therefore get ∑

n≥0 χAn(t) xn

n! = exp t ∑

n≥1 cn xn

n!

=
 ∑

n≥0 bn xn

n!
 

t
 ,

where exp ∑n≥1 cn xn

n! = ∑n≥0 bn xn
n! . Put t = −1 to get

∑

n≥0(−1)nr(An) xn

n! =
 ∑

n≥0 bn xn

n!
 
−1
 ,

from which it follows that

∑

n≥0 χAn(t) xn

n! =
 ∑

n≥0(−1)nr(An) xn

n!
 
−t
 .
 □
For a generalization of Theorem 5.17, see Exercise 9.

5.4. The Catalan arrangement

Deﬁne the Catalan arrangement Cn in K n, where char(K) ̸= 2, by

QCn(x) = ∏

1≤i<j≤n(xi − xj )(xi − xj − 1)(xi − xj + 1).

Equivalently, the hyperplanes of Cn are given by

xi − xj = −1, 0, 1, 1 ≤ i < j ≤ n.

Thus Cn has 3(
n
2) hyperplanes, and rank(Cn) = n − 1.
Assume now that K = R. The symmetric group Sn acts on Rn by permuting
coordinates, i.e., w · (x1, . . . , xn) = (xw(1), . . . , xw(n)).
Here we are multiplying permutations left-to-right, e.g., (1, 2)(2, 3) = (1, 3, 2) (in
cycle form), so vw · α = v · (w · α). Both Bn and Cn are Sn-invariant, i.e., Sn
permutes the hyperplanes of these arrangements. Hence Sn also permutes their
regions, and each region xw(1) > xw(2) > · · · > xw(n) of Bn is divided “in the same
way” in Cn. In particular, if r0(Cn) denotes the number of regions of Cn contained
in some ﬁxed region of Bn, then r(Cn) = n!r0(Cn) . See Figure 3 for C3 in the
ambient space ker(x1 + x2 + x3), where the hyperplanes of B3 are drawn as solid
lines and the remaining hyperplanes as dashed lines. Each region of B3 contains
ﬁve regions of C3, so r(C3) = 6 · 5 = 30.
We can compute r(Cn) (or equivalently r0(Cn)) by a direct combinatorial ar-
gument. Let R0 denote the region x1 > x2 > · · · > xn of Bn. The regions of Cn
contained in R0 are determined by those i < j such that xi − xj < 1. We need only
specify the maximal intervals [i, j] such that xi − xj < 1, i.e., if a ≤ i < j ≤ b and
xa − xb < 1, then a = i and b = j. It is easy to see that any such speciﬁcation of
maximal intervals determines a region of Cn contained in R0. Thus r0(Cn) is equal

LECTURE 5. FINITE FIELDS 67

Figure 3. The Catalan arrangement C3 in ker(x1 + x2 + x3)

to the number of antichains A of strict intervals of [n], i.e., sets A of intervals [i, j],
where 1 ≤ i < j ≤ n, such that no interval in A is contained in another. (“Strict”
means that i = j is not allowed.) It is known (equivalent to [19, Exer. 6.19(bbb)])
that the number of such antichains is the Catalan number Cn = 1
n+1 (2n
n ). For
the sake of completeness we give a bijection between these antichains and a stan-
dard combinatorial structure counted by Catalan numbers, viz., lattice paths from
(0, 0) to (n, n) with steps (1, 0) and (0, 1), never rising above the line y = x ([19,
Exer. 6.19(h)]). Given an antichain A of intervals of [n], there is a unique lattice
path of the claimed type whose “outer corners” (a step (1, 0) followed by (0, 1))
consist of the points (j, i − 1) where [i, j] ∈ A, together with the points (i, i − 1)
where no interval in A contains i. Figure 4 illustrates this bijection for n = 8 and
A = {[1, 4], [3, 5], [7, 8]}.
We have therefore proved the following result. For a reﬁnement, see Exercise 10.

Proposition 5.14. The number of regions of the Catalan arrangement Cn is given
by r(Cn) = n!Cn. Each region of Bn contains Cn regions of Cn.

In fact, there is a simple formula for the characteristic polynomial χCn(t).

Theorem 5.18. We have

χCn(t) = t(t − n − 1)(t − n − 2)(t − n − 3) · · · (t − 2n + 1).

68 , HYPERPLANE ARRANGEMENTS

52

40
 65
 86

Figure 4. A bijection corresponding to A = {[1, 4], [3, 5], [7, 8]}

Proof. Clearly the sequence (C1, C2, . . . ) is an ESA, so by Theorem 5.17 we have

∑

n≥0 χCn(t) xn

n! =
 ∑

n≥0(−1)nn!Cn xn

n!
 
−t

=
 ∑

n≥0(−1)nCnxn

−t
 .

One method for expanding this series is to use the Lagrange inversion formula
[19, Thm. 5.4.2]. Let F (x) = a1x + a2x2 + · · · be a formal power series over K,
where char(K) = 0 and a1 ̸= 0. Then there exists a unique formal power series
F ⟨−1⟩ = a−1
1 x + · · · satisfying

F (F ⟨−1⟩(x)) = F ⟨−1⟩(F (x)) = x.

Let k, t ∈ Z. The Lagrange inversion formula states that

(37) t[xt]F ⟨−1⟩(x)k = k[xt−k] ( x

F (x)
 )t .

Let y = ∑
n≥0(−1)nCnxn+1. By a fundamental property of Catalan numbers,
y2 = −y + x. Hence y = (x + x2)⟨−1⟩. Substitute t − n for k and apply equation
(37) to y = F (x), so F ⟨−1⟩(x) = x + x2:

(38) t[xt](x + x2)t−n = (t − n)[xn] ( x
y
 )t .

The right-hand side of (38) is just

(t − n)[xn] ( y
x
 )−t = (t − n)χCn(t)
n! .

LECTURE 5. FINITE FIELDS 69

a b

c
 f
 d e

a c f

b d e

Figure 5. An example of an interval order

The left-hand side of (38) is given by

t[xt]xt−n(1 + x)t−n = t(t − n
n
 ) = t(t − n)(t − n − 1) · · · (t − 2n + 1)
n! .

It follows that

χCn(t) = t(t − n − 1)(t − n − 2)(t − n − 3) · · · (t − 2n + 1)

for all t ∈ Z. It then follows easily (e.g., using the fact that a polynomial in one
variable over a ﬁeld of characteristic 0 is determined by its values on Z) that this
equation holds when t is an indeterminate. □
Note. It is not diﬃcult to give an alternative proof of Theorem 5.18 based on
the ﬁnite ﬁeld method (Exercise 11).

5.5. Interval orders

The subject of interval orders has a long history (see [10][23]), but only recently
[20] was their connection with arrangements noticed. Let P = {I1, . . . , In} be a
ﬁnite set of closed intervals Ii = [ai, bi], where ai, bi ∈ R and ai < bi. Partially
order P by deﬁning Ii < Ij if bi < aj, i.e., Ii lies entirely to the left of Ij on the real
number line. A poset isomorphic to P is called an interval order. Figure 5 gives
an example of six intervals and the corresponding interval order. It is understood
that the real line lies below and parallel to the line segments labelled a, . . . , f , and
that the actual intervals are the projections of these line segments to R. If all the
intervals Ii have length one, then P is called a semiorder or unit interval order.
The following proposition collects some basic results on interval orders. We sim-
ply state them without proof. Only part (a) is needed in what follows (Lemma 5.6).

70 , HYPERPLANE ARRANGEMENTS

0  0  0 0 1 1

0 0 1
 0 1 1
 0 0 1

Figure 6. The semiorders with three elements

We use the notation i to denote an i-element chain and P +Q to denote the disjoint
union of the posets P and Q.

Proposition 5.15. (a) A ﬁnite poset is an interval order if and only if it has
no induced subposet isomorphic to 2 + 2.
(b) A ﬁnite poset is a semiorder if and only if it has no induced subposets
isomorphic to 2 + 2 or 3 + 1.
(c) A ﬁnite poset P is a semiorder if and only if its elements can be ordered as
I1, . . . , In so that the incidence matrix of P (i.e., the matrix M = (mij ),
where mij = 1 if Ii < Ij and mij = 0 otherwise) has the form shown
below. Moreover, all such semiorders are nonisomorphic.

0

1 n

n

1 1

In (c) above, the southwest boundary of the positions of the 1’s in M form a
lattice path which by suitable indexing goes from (0, 0) to (n, n) with steps (0, 1)
and (1, 0), never rising above y = x. Since the number of such lattice paths is
the Catalan number Cn, it follows that the number of nonisomorphic n-element
semiorders is Cn. Later (Proposition 5.17) we will give a proof based on properties
of a certain arrangement. Figure 6 illustrates Proposition 5.15(c) when n = 3. It
shows the matrices M , the corresponding set of unit intervals, and the associated
semiorder.
Consider now labelled interval orders, i.e., interval orders on a set S. For
instance, Figure 7 shows the ﬁve nonisomorphic interval orders (which for three
vertices concides with semiorders) with three vertices, and below them the number
of distinct labelings. (In general, the number of labelings of an n-element poset P

LECTURE 5. FINITE FIELDS 71

63361

Figure 7. The number of labelings of semiorders with three elements

Figure 8. The arrangement I(1,1,1) in the space ker(x1 + x2 + x3)

is n!/#Aut(P ), where Aut(P ) denotes the automorphism group of P .) It follows
that there are 19 labelled interval orders or labelled semiorders on a 3-element set.
Let ℓ1, . . . , ℓn > 0 and set η = (ℓ1, . . . , ℓn). Let Pη denote the set of all interval
orders P on [n] such that there exist a set I1, . . . , In of intervals corresponding to

P (with Ii corresponding to i ∈ P ) such that ℓ(Ii) = ℓi. In other words, i P
< j if
and only if Ii lies entirely to the left of Ij. For instance, it follows from Figure 7
that #P(1,1,1) = 19.
We now come to the connection with arrangements. Given η = (ℓ1, . . . , ℓn) as
above, deﬁne the arrangement Iη in Rn by letting its hyperplanes be given by

xi − xj = ℓi, i ̸= j.

(Note the condition i ̸= j, not i < j.) Thus Iη has rank n − 1 and n(n − 1)
hyperplanes (since ℓi > 0). Figure 8 shows the arrangement I(1,1,1) in the space
ker(x1 + x2 + x3).

Proposition 5.16. Let η ∈ Rn . Then r(Iη) = #Pη.

72 , HYPERPLANE ARRANGEMENTS

Proof. Let (x1, . . . , xn) belong to some region R of Iη. Deﬁne the interval Ii =
[xi − ℓi, xi]. The region R is determined by whether xi − xj < ℓi or xi − xj > ℓi.
Equivalently, Ii ̸> Ij or Ii > Ij in the ordering on intervals that deﬁnes interval
orders. Hence the number of possible interval orders corresponding to intervals
I1, . . . , In with ℓ(Ii) = ℓi is just r(Iη). □
Consider the case ℓ1 = · · · = ℓn = 1, so we are looking at the semiorder
arrangement xi − xj = 1 for i ̸= j. We abbreviate (1, 1, . . . , 1) as 1n and denote
this arrangement by I1n. By the proof of Proposition 5.16 the regions of I1n are in
a natural bijection with semiorders on [n].
Now note that Cn = I1n ∪ Bn, where Cn denotes the Catalan arrangement.
Fix a region R of Bn, say x1 < x2 < · · · < xn. Then the number of regions of
I1n that intersect R is the number of semiorders on [n] that correspond to (unit)
intervals I1, . . . , In with right endpoints x1 < x2 < · · · < xn. Another set I ′
1, . . . , I ′
n
of unit intervals I ′
i = [x′ − 1, x′ ] with x′ < x′ < · · · < x′ deﬁnes a diﬀerent
region from that deﬁned by I1, . . . , In if and only if the corresponding semiorders
are nonisomorphic. It follows that the number of nonisomorphic semiorders on [n]
is equal to the number of regions of I1n intersecting the region x1 < x2 < · · · < xn
of Bn. Since Cn = I1n ∪ Bn, there follows from Proposition 5.14 the following result
of Wine and Freunde [24].

Proposition 5.17. The number u(n) of nonisomorphic n-element semiorders is
given by
 u(n) = 1

n! r(Cn) = Cn.

Figure 9 shows the nonisomorphic 3-element semiorders corresponding to the
regions of Cn intersecting the region x1 < x2 < · · · < xn of Bn.
We now come to the problem of determining r(I1n ), the number of semiorders
on [n].

Theorem 5.19. Fix distinct real numbers a1, a2, . . . , am > 0. Let An be the ar-
rangement in Rn with hyperplanes

An : xi − xj = a1, . . . , am, i ̸= j,

and let A∗ = An ∪ Bn. Deﬁne

F (x) = ∑

n≥1 r(An) xn

n!

G(x) = ∑

n≥1 r(A∗ ) xn

n! .

Then F (x) = G(1 − e−x).

Proof. Let c(n, k) denote the number of permutations w of n objects with k cycles
(in the disjoint cycle decomposition of w). The integer c(n, k) is known as a signless
Stirling number of the ﬁrst kind and for ﬁxed k has the exponential generating
function ∑

n≥0 c(n, k) xn

n! = 1
k! (log(1 − x)−1)k .

For futher information, see e.g. [18, pp. 17–20][19, (5.25)].

LECTURE 5. FINITE FIELDS 73

x   = x1 2

x   = x2 3

2 1

2

3

1 2
3

1

2 3

1 2 3 1

3

Figure 9. The nonisomorphic 3-element semiorders as regions of C1n

We have

F (x) = G(1 − e−x) ⇔ G(x) = F (log(1 − x)−1)

= ∑

k≥1 r(Ak) 1
k! (log(1 − x)−1)k

= ∑

k≥1 r(Ak) ∑

n≥0 c(n, k) xn

n! .

It follows that we need to show that

(40) r(A∗ ) =
 n∑

k=1 c(n, k)r(Ak).

For simplicity we consider only the case m = 1 and a1 = 1, but the argument
is completely analogous in the general case. When m = 1 and a1 = 1 we have
r(A∗ ) = n!Cn, and r(An) is the number of semiorders on [n]. Choose w ∈ Sn with
k cycles in c(n, k) ways, and make these cycles the vertices of a semiorder P in r(Ak)
ways. Deﬁne a new poset ρ(P, w) as follows: if the cycle (c1, . . . , cj) is an element
of P , then replace it with an antichain with elements c1, . . . , cj. Given 1 ≤ c ≤ n,

74 , HYPERPLANE ARRANGEMENTS

let C(c) be the cycle of w containing c. Deﬁne c < d in ρ(P, w) if C(c) < C(d) in
P . We illustrate this deﬁnition with n = 8 and w = (1, 5, 2)(3)(6, 8)(4, 7):

(       )P,w (       )P,wQ = ρ

(1,5,2) (6,8) 1 5 2 6 8

ρ

(3) (4,7) 3 4 7

Given an unlabelled n-element semiorder Q, such as

we now show that there are exactly n! pairs (P, w) for which ρ(P, w) ∼ Q. Call a
pair of elements x, y ∈ Q autonomous if for all z ∈ Q we have

x < z ⇔ y < z, x > z ⇔ y > z.

Equivalently, the map τ : Q → Q transposing x, y and ﬁxing all other z ∈ Q is an
automorphism of Q. Clearly the relation of being autonomous is an equivalence
relation. Partition Q into its autonomous equivalence classes. Regard the elements
of Q as being distinguished, and choose a bijection (labeling) ϕ : Q → [n] (in n!
ways). Fix a linear ordering (independent of ϕ) of the elements in each equivalence
class. (The linear ordering of the elements in each equivalence classe in the diagram
below is left-to-right.)
 2 8

4 1

73 6

5

In each class, place a left parenthesis before each left-to-right maximum, and
place a right parenthesis before each left parenthesis and at the end. (This is the
bijection Sn → Sn, ˆw ↦→ w, in [18, p. 17].) Merge the elements c1, c2, . . . , cj
(appearing in that order) between each pair of parentheses into a single element
labelled with the cycle (c1, c2, . . . , cj).

LECTURE 5. FINITE FIELDS 75

(3) (7      ,    6) (2) (8)

(5) (4      ,    1)
 3 (7,6) (2) (8)

(4,1)(5)

ρ

We have thus obtained a poset P whose elements are labelled by the cycles of
a permutation w ∈ Sn, such that ρ(P, w) = Q. For each unlabelled Q, there are
exactly n! pairs (P, w) (where the poset P is labelled by the cycles of w ∈ Sn)
for which ρ(P, w) ∼ Q. Since by Proposition 5.17 there are Cn nonisomorphic
n-element semiorders, we get

n!Cn =
 n∑

k=1 c(n, k)r(Ak).
 □
Note. Theorem 5.19 can also be proved using Burnside’s lemma (also called
the Cauchy-Frobenius lemma) from group theory.
To test one’s understanding of the proof of Theorem 5.19, consider why it
doesn’t work for all posets. In other words, let f (n) denote the number of posets on
[n] and g(n) the number of nonisomorphic n-element posets. Set F (x) = ∑ f (n) xn

n!
and G(x) = ∑ g(n)xn. Why doesn’t the above argument show that G(x) = F (1 −
e−x)? Let Q = 2 + 2 (the unique obstruction to being an interval order, by
Proposition 5.15(a)). The autonomous classes have one element each. Consider the
two labelings ϕ : Q → [4] and the corresponding ρ−1:

ρ −1

ρ −1

1

2 4

3

4 2
 4

1

2 4

We obtain the same labelled posets in both cases, so the proof of Theorem 5.19
fails. The key property of interval orders that the proof of Theorem 5.19 uses
implicitly is the following.

Lemma 5.6. If σ : P → P is an automorphism of the interval order P and
σ(x) = σ(y), then x and y are autonomous.

Proof. Assume not. Then there exists an element s ∈ P satisfying s > x, s ̸> y (or
dually). Since σ(x) = y, there must exist t ∈ P satisfying t > y, t ̸> x. But then
{x, s, y, t} form an induced 2 + 2, so by Proposition 5.15(a) P is not an interval
order. □
Specializing m = 1 and a1 = 1 in Theorem 5.19 yields the following corollary,
due ﬁrst (in an equivalent form) to Chandon, Lemaire and Pouget [8].

76 , HYPERPLANE ARRANGEMENTS

Corollary 5.11. Let f (n) denote the number of semiorders on [n] (or n-element
labelled semiorders). Then ∑

n≥0 f (n) xn

n! = C(1 − e−x),

where
 C(x) = ∑

n≥0 Cnxn = 1 − √1 − 4x
2x .

5.6. Intervals with generic lengths

A particularly interesting class of interval orders are those corresponding to intervals
with speciﬁed generic lengths η = (ℓ1, . . . , ℓn). Intuitively, this means that the
intersection poset P (Iη) is as “large as possible.” One way to make this precise
is to say that η is generic if P (Iη) ∼ P (Iη′), where η′ = (ℓ′ , . . . , ℓ′ ) and the
ℓ′’s are linearly independent over Q. Thus if η is generic, then the intersection
poset L(Iη) does not depend on η, but rather only on n. In particular, r(Iη) does
not depend on η (always assuming η is generic). Hence by Proposition 5.16, the
number #Pη of labelled interval orders corresponding to intervals I1, . . . , In with
ℓ(Ii) = ℓi depends only on n. This fact is not at all obvious combinatorially, since
the interval orders themselves do depend on η. For instance, it is easy to see that
η = (1, 1.0001, 1.001, 1.01, 1.1) is generic and that no corresponding interval order
can be isomorphic to 4 + 1. On the other hand, η = (1, 10, 100, 1000, 10000) is also
generic, but this time there is a corresponding interval order isomorphic to 4 + 1.
(See Exercise 16.)
The preceding discussion raises the question of computing #Pn when η is
generic. We write Gn for the corresponding interval order xi − xj = ℓi, i ̸= j,
since the intersection poset depends only on n. The following result is a nice appli-
cation of arrangements to “pure” enumeration; no proof is known except the one
sketched here.

Theorem 5.20. Let

z = ∑

n≥0 r(Gn) xn

n! = 1 + x + 3 x2

2! + 19 x3

3! + 195 x4

4! + 2831 x5

5! + · · · .

Deﬁne a power series
y = 1 + x + 5 x2

2! + 46 x3

3! + 631 x4

4 + · · ·

by 1 = y(2 − exy). Equivalently,

y = 1 + ( 1
1 + x log 1 + 2x
1 + x
 )⟨−1⟩ .

Then z is the unique power series satisfying z′/z = y2, z(0) = 1.

Note. The condition z′/z = y2 can be rewritten as z = exp ∫ y2 dx.
Sketch of proof. Putting t = −1 in Theorem 2.4 gives

(41) r(Gn) = ∑

B⊆Gn
B central

(−1)#B−rk(B).

LECTURE 5. FINITE FIELDS 77

Given a central subarrangement B ⊆ Gn, deﬁne a digraph (directed graph) GB on
[n] by letting i → j be a (directed) edge if the hyperplane xi − xj = ℓi belongs to B.
One then shows that as an undirected graph GB is bipartite, i.e., the vertices can be
partitioned into two subsets U and V such that all edges connect a vertex in U to a
vertex in V . The pair (U, V ) is called a vertex bipartition of GB. Moreover, if B is
a block of GB (as deﬁned preceding Proposition 4.11), say with vertex bipartition
(UB, VB), then either all edges of B are directed from UB to VB, or all edges are
directed from VB to UB. It can also be seen that all such directed bipartite graphs
can arise in this way. It follows that equation (41) can be rewritten

(42) r(Gn) = (−1)n ∑

G (−1)e(G)+c(G)2b(G),

where G ranges over all (undirected) bipartite graphs on [n], e(G) denotes the
number of edges of G, and b(G) denotes the number of blocks of G.
Equation (42) reduces the problem of determining r(G) to a (rather diﬃcult)
problem in enumeration, whose solution may be found in [14, §6]. □

5.7. Other examples

There are two additional arrangements related to the braid arrangement that in-
volve nice enumerative combinatorics. We merely repeat the deﬁnitions here from
Lecture 1 and assemble some of their basic properties in Exercises 18–27.
The Linial arrangement in K n is given by the hyperplanes xi − xj = 1, 1 ≤ i <
j ≤ n. It consists of “half” of the semiorder arrangement I1n. Despite its similarity
to I1n, it is considerably more diﬃcult to obtain its characteristic polynomial and
other enumerative invariants. Finally the threshold arrangement in K n is given by
the hyperplanes xi + xj = 0, 1 ≤ i < j ≤ n. It is a subarrangement of the Coxeter
arrangements A(Bn) (=A(Cn)) and A(Dn).

78 , HYPERPLANE ARRANGEMENTS

Exercises
(1) [2] Verify equation (32), viz.,

χA(Dn)(t) = (t − 1)(t − 3) · · · (t − (2n − 3) · (t − n + 1).

(2) [2] Draw a picture of the projectivization of the Coxeter arrangement A(B3),
similar to Figure 1 of Lecture 1.
(3) (a) [2] An embroidered permutation of [n] consists of a permutation w of [n]
together with a collection E of ordered pairs (i, j) such that:
• 1 ≤ i < j ≤ n for all (i, j) ∈ E.
• If (i, j) and (h, k) are distinct elements of E, then it is false that
i ≤ h ≤ k ≤ j.
• If (i, j) ∈ E then w(i) < w(j).
For instance, the three embroidered permutations (w, E) of [2] are given
by (12, ∅), (12, {(1, 2)}), and (21, ∅). Give a bijective proof that the num-
ber r(Sn) of regions of the Shi arrangement Sn is equal to the number of
embroidered permutations of [n].
(b) [2+] A parking function of length n is a sequence (a1, . . . , an) ∈ Pn whose
increasing rearrangement b1 ≤ b2 ≤ · · · ≤ bn satisﬁes bi ≤ i. For instance,
the parking functions of length three are 11, 12, 21. Give a bijective proof
that the number of parking functions of length n is equal to the number of
embroidered permutations of [n].
(c) [3–] Give a combinatorial proof that the number of parking functions of
length n is equal to (n + 1)n−1.
(4) [2+] Show that if Sn denotes the Shi arrangement, then the cone cSn is not
supersolvable for n ≥ 3.
(5) [2] Show that if f : P → R and h : N → R are related by equation (35) (with
h(0) = 1), then equation (34) holds.
(6) (a) [2] Compute the characteristic polynomial of the arrangement B′ in Rn

with deﬁning polynomial

Q(x) = (x1 − xn − 1) ∏

1≤i<j≤n(xi − xj).

In other words, B′ consists of the braid arrangement together with the
hyperplane x1 − xn = 1.
(b) [5–] Is cB′ (the cone over B′ ) supersolvable?
(7) [2+] Let 1 ≤ k ≤ n. Find the characteristic polynomial of the arrangement Sn,k
in Rn deﬁned by
 xi − xj = 0 for 1 ≤ i < j ≤ n
xi − xj = 1 for 1 ≤ i < j ≤ k.

(8) [2+] Let 1 ≤ k ≤ n. Find the characteristic polynomial of the arrangement Cn,k
in Rn deﬁned by
 xi = 0 for 1 ≤ i ≤ n
xi ± xj = 0 for 1 ≤ i < j ≤ n
xi + xj = 1 for 1 ≤ i < j ≤ k. .

In particular, show that r(Cn,k) = 2n−kn!(2k
k ).
(9) (a) [2+] For n ≥ 1 let An be an arrangement in Rn such that every H ∈ An
is parallel to a hyperplane of the form xi = cxj, where c ∈ R. Just as in

LECTURE 5. FINITE FIELDS 79

the deﬁnition of an exponential sequence of arrangements, deﬁne for every
subset S of [n] the arrangement

AS = {H ∈ An : H is parallel to some xi = cxj, where i, j ∈ S}.

Suppose that for every such S we have LAS ∼ LAk , where k = #S. Let

F (x) = ∑

n≥0(−1)nr(An) xn

n!

G(x) = ∑

n≥0(−1)rk(An)b(An) xn

n! .

Show that

(43) ∑

n≥0 χAn(t) xn

n! = G(x)(t+1)/2

F (x)(t−1)/2 .

(b) [2] Simplify equation (43) when each An is a central arrangement. Make
sure that your simpliﬁcation is valid for the braid arrangement and the
coordinate hyperplane arrangement.
(10) [2+] Let R0(Cn) denote the set of regions of the Catalan arrangement Cn con-
tained in the regions x1 > x2 > · · · > xn of Bn. Let ˆR be the unique region
in R0(Cn) whose closure contains the origin. For R ∈ R0(Cn), let XR be the
set of hyperplanes H ∈ Cn such that ˆR and R lie on diﬀerent sides of H. Let
Wn = {XR : R ∈ R0(Cn)}, ordered by inclusion.
 a

b

c d

e

W3

a b
 c e

Let Pn be the poset of intervals [i, j], 1 ≤ i < j ≤ n, ordered by reverse
inclusion.

80 , HYPERPLANE ARRANGEMENTS

P3
 [1,3]

[2,3][1,2]
 [1,2] [2,3] [3,4]

[2,4][1,3]
 [1,4]
P4

Show that Wn ∼ J(Pn), the lattice of order ideals of Pn. (An order ideal of a
poset P is a subset I ⊆ P such that if x ∈ I and y ≤ x, then y ∈ I. Deﬁne J(P )
to be the set of order ideals of P , ordered by inclusion. See [18, Thm. 3.4.1].)
(11) [2] Use the ﬁnite ﬁeld method to prove that

χCn(t) = t(t − n − 1)(t − n − 2)(t − n − 3) · · · (t − 2n + 1),

where Cn denotes the Catalan arrangement.
(12) [2+] Let k ∈ P. Find the number of regions and characteristic polynomial of the
extended Catalan arrangement

Cn(k) : xi − xj = 0, ±1, ±2, . . . , ±k, for 1 ≤ i < j ≤ n.

Generalize Exercise 10 to the arrangements Cn(k).
(13) [3–] Let SB denote the arrangement

xi ± xj = 0, 1, 1 ≤ i < j ≤ n

2xi = 0, 1, 1 ≤ i ≤ n,

called the Shi arrangement of type B. Find the characteristic polynomial and
number of regions of SB. Is there a “nice” bijective proof of the formula for the
number of regions?
(14) [5–] Let 1 ≤ k ≤ n. Find the number of regions (or more generally the charac-
teristic polynomial) of the arrangement (in Rn)

xi − xj = { 1, 1 ≤ i ≤ k
2, k + 1 ≤ i ≤ n,

for all i ̸= j. Thus we are counting interval orders on [n] where the elements
1, 2, . . . , k correspond to intervals of length one, while k + 1, . . . , n correspond
to intervals of length two. Is it possible to count such interval orders up to
isomorphism (i.e., the unlabelled case)? What if the length 2 is replaced instead
by a generic length a?
(15) [2+] A double semiorder on [n] consists of two binary relations < and ≪ on [n]
that arise from a set x1, . . . , xn of real numbers as follows:

i < j if xi < xj − 1
i ≪ j if xi < xj − 2.

If we associate the interval Ii = [xi − 2, xi] with the point xi, then we are
specifying whether Ii lies to the left of the midpoint of Ij , entirely to the left of

LECTURE 5. FINITE FIELDS 81

Ij, or neither. It should be clear what is meant for two double semiorders to be
isomorphic.
(a) [2] Draw interval diagrams of the 12 nonisomorphic double semiorders on
{1, 2, 3}.
(b) [2] Let ρ2(n) denote the number of double semiorders on [n]. Find an
arrangement I(2) satisfying r(I(2)) = ρ2(n).
(c) [2+] Show that the number of nonisomorphic double semiorders on [n] is
given by 1

2n+1 (3n
n ).
(d) [2–] Let F (x) = ∑n≥0 1
2n+1 (3n
n )xn. Show that

∑

n≥0 ρ2(n) xn

n! = F (1 − e−x).

(e) [2] Generalize to “k-semiorders,” where ordinary semiorders (or unit interval
orders) correspond to k = 1 and double semiorders to k = 2.
(16) [1+] Show that intervals of lengths 1, 1.0001, 1.001, 1.01, 1.1 cannot form an in-
terval order isomorphic to 4 + 1, but that such an interval order can be formed
if the lengths are 1, 10, 100, 1000, 10000.
(17) [5–] What more can be said about interval orders with generic interval lengths?
For instance, consider the two cases: (a) interval lengths very near each other
(e.g., 1, 1.001, 1.01, 1.1), and (b) interval lengths superincreasing (e.g., 1, 10, 100,
1000). Are there ﬁnitely many obstructions to being such an interval order? Can
the number of unlabelled interval orders of each type be determined? (Perhaps
the numbers are the same, but this seems unlikely.)
(18) (a) [3] Let Ln denote the Linial arrangement, say in Rn. Show that

χLn(t) = t
2n
 n∑=1
 (n
k
)(t − k)n−1.

(b) [1+] Deduce from (a) that

χLn(t)

t = (−1)nχLn(−t + n)
−t + n .

(19) (a) [3–] An alternating tree on the vertex set [n] is a tree on [n] such that
every vertex is either less than all its neighbors or greater than all its neigh-
bors. Figure 10 shows the seven alternating trees on [4]. Deduce from
Exercise 18(a) that r(Ln) is equal to the number of alternating trees on
[n + 1].
(b) [5] Find a bijective proof of (a), i.e., give an explicit bijection between the
regions of Ln and the alternating trees on [n + 1].
(20) [3–] Let
 χLn(t) = antn − an−1tn−1 + · · · + (−1)n−1a1t.

Deduce from Exercise 18(a) that ai is the number of alternating trees on the
vertex set 0, 1, . . . , n such that vertex 0 has degree (number of adjacent vertices)
i.
(21) (a) [2+] Let P (t) ∈ C[t] have the property that every (complex) zero of P (t)
has real part a. Let z ∈ C satisfy |z| = 1. Show that every zero of the
polynomial P (t − 1) + zP (t) has real part a + 1
2 .

82 , HYPERPLANE ARRANGEMENTS

1 23 4 2 4 1 3

1 4 2 3 3 4 1 2

2 3 1 4 2

41

4
 32
 1

Figure 10. The seven alternating trees on the vertex set [4]

(b) [2+] Deduce from (a) and Exercise 18(a) that every zero of the polynomial
χLn(t)/t has real part n/2. This result is known as the “Riemann hypothesis
for the Linial arrangement.”
(22) (a) [2–] Compute limn→∞ b(Sn)/r(Sn), where Sn denotes the Shi arrangement.
(b) [3] Do the same for the Linial arrangement Ln.
(23) [2+] Let Ln denote the Linial arrangement in Rn. Fix an integer r ̸= 0, ±1, and
let Mn(r) be the arrangement in Rn deﬁned by xi = rxj , 1 ≤ i < j ≤ n, together
with the coordinate hyperplanes xi = 0. Find a relationship between χLn(t) and
χMn(r)(t) without explicitly computing these characteristic polynomials.
(24) (a) [3–] A threshold graph on [n] may be deﬁned recursively as follows: (i) the
empty graph ∅ is a threshold graph, (ii) if G is a threshold graph, then so is
the disjoint union of G and a single vertex, and (iii) if G is a threshold graph,
then so is the graph obtained by adding a new vertex v and connecting it
to every vertex of G. Let Tn denote the threshold arrangement. Show that
r(Tn) is the number of threshold graphs on [n].
(b) [2+] Deduce from (a) that
∑

n≥0 r(Tn) xn

n! = ex(1 − x)
2 − ex .

(c) [1+] Deduce from Exercise 9 that
∑

n≥0 χTn(t) xn

n! = (1 + x)(2ex − 1)(t−1)/2.

(25) [5–] Let χTn(t) = tn − an−1tn−1 + · · · + (−1)na0.
For instance,
 χT3 (t) = t3 − 3t2 + 3t − 1

χT4 (t) = t4 − 6t3 + 15t2 − 17t + 7

χT5 (t) = t5 − 10t4 + 45t3 − 105t2 + 120t − 51.

LECTURE 5. FINITE FIELDS 83

By Exercise 24(a), a0 + a1 + · · · + an−1 + 1 is the number of threshold graphs
on the vertex set [n]. Give a combinatorial interpretation of the numbers ai as
the number of threshold graphs with a certain property.
(26) (a) [1+] Find the number of regions of the “Linial threshold arrangement”

xi + xj = 1, 1 ≤ i < j ≤ n.

(b) [5–] Find the number of regions, or even the characteristic polynomial, of
the “Shi threshold arrangement”

xi + xj = 0, 1, 1 ≤ i < j ≤ n.

(27) [3–] Let An denote the “generic threshold arrangement” (in Rn) xi + xj = aij,
1 ≤ i < j ≤ n, where the aij ’s are generic. Let

T (x) = ∑

n≥1 nn−2 xn

n! ,

the generating function for labelled trees on n vertices. Let

R(x) = ∑

n≥1 nn−1 xn

n! ,

the generating function for rooted labelled trees on n vertices. Show that
∑

n≥0 r(An) xn

n! = eT (x)− 1
2 R(x) ( 1 + R(x)
1 − R(x)
 )1/4

= 1 + x + 2 x2

2! + 8 x3

3! + 54 x4

4! + 533 x5

5! + 6934 x6

6! + · · · .

(28) [2+] Let f (k, n, r) be the number of k×n (0, 1)-matrices A over the rationals such
that all rows of A are distinct, every row has at least one 1, and rank(A) = r.
Let gn(q) be the number of n-tuples (a1, . . . , an) ∈ Fn such that no nonempty
subset of the entries sums to 0 (in Fq). Show that

gn(q) = ∑

k,r
 (−1)k

k! f (k, n, r)qn−r.

(The case k = 0 is included, corresponding to the empty matrix, which has rank
0.)
 BIBLIOGRAPHY

1. C. A. Athanasiadis, Algebraic Combinatorics of Graph Spectra, Subspace Ar-
rangements and Tutte Polynomials, Ph.D. thesis, MIT, 1996.
2. C. A. Athanasiadis, Characteristic polynomials of subspace arrangements and
ﬁnite ﬁelds, Advances in Math. 122 (1996), 193–233.
3. H. Barcelo and E. Ihrig, Lattices of parabolic subgroups in connection with
hyperplane arrangements, J. Algebraic Combinatorics 9 (1999), 5–24.
4. A. Bj¨orner and F. Brenti, Combinatorics of Coxeter Groups, to appear.
5. A. Bj¨orner, M. Las Vergnas, B. Sturmfels, N. White, and G. Ziegler, Oriented
Matroids, second ed., Encyclopedia of Mathematics and Its Applications 46,
Cambridge University Press, Cambridge, 1999.
6. A. Blass and B. Sagan, Characteristic and Ehrhart polynomials, J. Algebraic
Combinatorics 7 (1998), 115–126.
7. N. Bourbaki, Groupes et alg`ebres de Lie, ´El´ements de Math´ematique, Fasc.
XXXIV, Hermann, Paris, 1968.
8. J. L. Chandon, J. Lemaire, and J. Pouget, D´enombrement des quasi-ordres sur
un ensemble ﬁni, Math. Inform. Sci. Humaines 62 (1978), 61–80, 83.
9. H. Crapo and G.-C. Rota, On the Foundations of Combinatorial Theory: Com-
binatorial Geometries, preliminary edition, MIT Press, Cambridge, MA, 1970.
10. P. C. Fishburn, Interval Orders and Interval Graphs, Wiley-Interscience, New
York, 1985.
11. C. Greene, On the M¨obius algebra of a partially ordered set, Advances in Math.
10 (1973), 177–187.
12. J. E. Humphreys, Reﬂection Groups and Coxeter Groups, Cambridge Univer-
sity Press, Cambridge, 1990.
13. P. Orlik and H. Terao, Arrangements of Hyperplanes, Springer-Verlag, Berlin,
1992.
14. A. Postnikov and R. Stanley, Deformations of Coxeter hyperplane arrange-
ments, J. Combinatorial Theory (A) 91 (2000), 544–597.
15. J.-Y. Shi, The Kazhdan-Lusztig cells in certain aﬃne Weyl groups, Lecture
Notes in Mathematics, vol. 1179, Springer-Verlag, Berlin, 1986.
16. R. Stanley, Modular elements of geometric lattices, Algebra Universalis 1
(1971), 214–217.
17. R. Stanley, Supersolvable lattices, Algebra Universalis 2 (1972), 197–217.

85

86 , HYPERPLANE ARRANGEMENTS

18. R. Stanley, Enumerative Combinatorics, vol. 1, Wadsworth and Brooks/Cole,
Paciﬁc Grove, CA, 1986; second printing, Cambridge University Press, Cam-
bridge, 1996.
19. R. Stanley, Enumerative Combinatorics, vol. 2, Cambridge University Press,
Cambridge, 1999
20. R. Stanley, Hyperplane arrangements, interval orders, and trees, Proc. Nat.
Acad. Sci. 93 (1996), 2620–2625.
21. H. Terao, Free arrangements of hyperplanes and unitary reﬂection groups,
Proc. Japan Acac., Ser. A 56 (1980), 389–392.
22. H. Terao, Generalized exponents of a free arrangement of hyperplanes and
Shepherd[sic]-Todd-Brieskorn formula, Invent. math. 63 (1981), 159–179.
23. W. T. Trotter, Combinatorics and Partially Ordered Sets, The Johns Hopkins
Univ. Press, Baltimore/London, 1992.
24. R. L. Wine and J. E. Freund, On the enumeration of decision patterns involving
n means, Ann. Math. Stat. 28, 256–259.
