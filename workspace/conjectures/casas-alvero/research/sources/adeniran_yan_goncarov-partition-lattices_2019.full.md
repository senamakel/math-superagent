<!-- source: https://arxiv.org/pdf/1907.07814 | converted from PDF -->

arXiv:1907.07814v1  [math.CO]  17 Jul 2019
Gonˇcarov Polynomials in Partition Lattices

and Exponential Families

Dedicated to Joseph Kung

Ayomikun Adeniran∗ and Catherine Yan†

Department of Mathematics, Texas A&M University, College Station, TX 77843

Abstract

Classical Gonˇcarov polynomials arose in numerical analysis as a basis for the solutions of
the Gonˇcarov interpolation problem. These polynomials provide a natural algebraic tool in the
enumerative theory of parking functions. By replacing the diﬀerentiation operator with a delta
operator and using the theory of ﬁnite operator calculus, Lorentz, Tringali and Yan introduced
the sequence of generalized Gonˇcarov polynomials associated to a pair (∆, Z) of a delta operator
∆ and an interpolation grid Z. Generalized Gonˇcarov polynomials share many nice algebraic
properties and have a connection with the theories of binomial enumeration and order statistics.
In this paper we give a complete combinatorial interpretation for any sequence of generalized
Gonˇcarov polynomials. First we show that they can be realized as weight enumerators in par-
tition lattices. Then we give a more concrete realization in exponential families and show that
these polynomials enumerate various enriched structures of vector parking functions.

Keywords: Gonˇcarov polynomials, partition lattices, exponential family
AMS Classiﬁcation: 05A10, 05A15, 05A18, 06A07

1 Introduction

The classical Gonˇcarov interpolation problem in numerical analysis was introduced by Gonˇcarov
[2, 3] and Whittaker[17]. It asks for a polynomial f (x) of degree n such that the ith derivative of
f (x) at a given point ai has value bi for i = 0, 1, 2, ..., n. The solution is obtained by taking linear
combinations of the (classical) Gonˇcarov polynomials, or the Abel-Gonˇcarov polynomials, which
have been studied extensively by analysts; see e.g. [2, 10, 1, 4]. Gonˇcarov polynomials also play
a crucial role in Combinatorics due to their close relations to parking functions. A (classical)

∗Corresponding author: ayoijeng@math.tamu.edu
†cyan@math.tamu.edu
 1

parking function is a sequence (a1, a2, ..., an) of positive integers such that for every i = 1, 2, ..., n,
there are at least i terms that are less than or equal to i. For example, the sequences (1, 2, 3, 4)
and (2, 1, 4, 1) are both parking functions while (2, 2, 3, 4) is not. The set of parking functions
stays in the center of enumerative combinatorics, with many generalizations and connections
to other research areas, such as hashing and linear probing in computer science, graph theory,
interpolation theory, diagonal harmonics, representation theory, and cellular automaton. See
the comprehensive survey [19] for more on the combinatorial theory of parking functions.
The connection between Gonˇcarov polynomials and combinatorics was ﬁrst found by Joseph
Kung, who in a short note [8] of 1981 proved that classical Gonˇcarov polynomials give the
probability distribution of the order statistics of n independent uniform random variables, and
its diﬀerence analog describes the order statistics of discrete, injective functions. These results
were further developed in [9] to an explicit correspondence between classical Gonˇcarov polyno-
mials and vector parking functions. Inspired by the rich theory on delta operators and ﬁnite
operator calculus, which is a uniﬁed theory on linear operators analogous to the diﬀerentiation
operator D and special polynomials, Lorentz, Tringali, and the second author of the present
paper introduced the generalized Gonˇcarov polynomials [11] as a basis for the solutions to the
Gonˇcarov interpolation problem with respect to a delta operator. Many algebraic and analytic
properties of classical Gonˇcarov polynomials have been extended to the generalized version.
A natural question is to ﬁnd the combinatorial interpretations for the generalized Gonˇcarov
polynomials. To answer this question we need to understand the combinatorial signiﬁcance of
delta operators. In the third paper of the seminal series On the Foundations of Combinatorial
Theory III, Mullin and Rota [12] developed the basic theory of delta operators and their asso-
ciated sequence of polynomials. Such sequences of polynomials are of binomial type and occur
in many combinatorial problems when objects can be pieced together out of small, connected
objects. Mullin and Rota’s work provides a realization of binomial sequences in combinatorial
problems. However, this realization is only valid for binomial sequences whose coeﬃcients are
non-negative integers, and so excludes many basic counting polynomials, for example, the falling
factorial x(n) = x(x − 1)⋯(x − n + 1). Mullin and Rota hint at a generalization of their theory
to incorporate such cases. Using the language of partitions, partition types and partition cat-
egories, Ray [14] proved that every polynomial sequence of binomial type can be realized as a
weighted enumerator in partition lattices.
In this paper we give a complete combinatorial interpretation of the generalized Gonˇcarov
polynomials, ﬁrst in Ray’s partition lattices and then in a more concrete model, the exponential
families, as described by Wilf [18]. Basically, to any polynomial sequence of binomial type and
any given interpolation grid Z there is an associated sequence of Gonˇcarov polynomials. While
the sequence of binomial type can be realized as weighted enumerators in partition lattices or in
an exponential family, the associated Gonˇcarov polynomials count those structures which also
encode vector parking functions. In other words, the generalized Gonˇcarov polynomials charac-
terize structures in a binomial enumeration problem that are subject to certain order-statistic
constraints. Our results cover the initial attempt in [11] which provides a combinatorial inter-
pretation for some families of generalized Gonˇcarov polynomials in a structure called reluctant
functions.
The rest of the paper is organized as follows. In Section 2, we recall the basic theory

2

of delta operators and binomial enumeration, as well as the concepts of generalized Gonˇcarov
polynomials and vector parking functions. In Section 3, we describe the realization of generalized
Gonˇcarov polynomials in partition lattices and weight functions. Then, in Section 4, we study a
more concrete realization of Gonˇcarov polynomials as type-enumerator in exponential families.
We end the paper in Section 5 with a few closing remarks.

2 Background

2.1 Delta Operators and Binomial Enumeration

We recall the basic theory of delta operators and their associated sequence of basic polynomials
as developed by Rota, Kahaner, and Odlyzko [15]. Let K be a ﬁeld of characteristic zero and
K[x] the vector space of all polynomials in the variable x over K. For each a ∈ K, let Ea
denote the shift operator K[x] → K[x] ∶ f (x) ↦ f (x + a). A linear operator s ∶ K[x] → K[x] is
called shift-invariant if sEa = Eas for all a ∈ K, where the multiplication is the composition of
operators.

Deﬁnition 1. A delta operator ∆ is a shift-invariant operator satisfying ∆(x) = a for some
nonzero constant a.

Deﬁnition 2. Let ∆ be a delta operator. A polynomial sequence {pn(x)}n≥0 is called the
sequence of basic polynomials, or the associated basic sequence of ∆ if
(i) p0(x) = 1;
(ii) Degree of pn(x) is n and pn(0) = 0 for each n ≥ 1;
(iii) ∆(pn(x)) = npn−1(x).

Every delta operator has a unique sequence of basic polynomials, which is a sequence of
binomial type (or binomial sequence) that satisﬁes

pn(u + v) = Q
i≥0 ‹n
i •pi(u)pn−i(v), (1)

for all n ≥ 0. Conversely, every polynomial sequence of binomial type is the associated basic
sequence of some delta operator.
Let s be a shift-invariant operator, and ∆ a delta operator. Then s can be expanded uniquely
as a formal power series of ∆. If s = Q
k≥0
 ak
k! ∆
k,

we say that f (t) = ∑k≥0 ak
k! tk is the ∆-indicator of s. In fact, the correspondence

f (t) = Q
k≥0
 ak
k! tk ←→ Q
k≥0
 ak
k! ∆
k

is an isomorphism from the ring K[[t]] of formal power series in t onto the ring of shift-invariant
operators. Under this isomorphism, a shift-invariant operator is invertible if and only if its ∆-
indicator f (t) satisﬁes f (0) ≠ 0, and it is a delta operator if and only if f (0) = 0 and f ′(0) ≠ 0,
i.e., f (t) has a compositional inverse g(t) satisfying f (g(t)) = g(f (t)) = t.

3

Another important result is the generating function for the sequence of basic polynomials
{pn(x)}n≥0 associated to a delta operator ∆. Let f (t) be the D-indicator of ∆, where D = d~dx
is the diﬀerentiation operator. Let g(t) be the compositional inverse of f (t). Then,

Q
n≥0 pn(x) tn

n! = exp (xg(t)) . (2)

The operator Λ = g(D) is called the conjugate delta operator of ∆, and {pn(x)}n≥0 is the
conjugate sequence of Λ. It is easy to see that if pn(x) = ∑
k≥1 pn,kx
k, then g(t) = ∑
k≥1 pk,1 t
k

k! .

Polynomial sequences of binomial type are closely related to the theory of binomial enumer-
ation. Consider the following model. Assume B is a family of discrete structures. For a ﬁnite
set E, let Π(E) be the poset of all partitions π of E, ordered by reﬁnement, and write SπS for the
number of blocks of π. Deﬁne a k-assembly of B-structures on E as a partition π of the set E
into SπS = k blocks such that each block of π is endowed with a B-structure. Let Bk(E) denote
the set of all such k-assemblies. For example, when B is a set of rooted trees, a k-assembly of
B-structures on E is a forest of k rooted trees with vertex set E. We can also take B to be other
structures, such as permutations, complete graphs, posets, etc. Assume that the cardinality of
Bk(E) depends only on the cardinality of E, but not its content. In other words, there is a
bijection between Bk(E) and Bk([n]) where [n] = {1, 2, ..., n} and SES = n.

Deﬁnition 3. Let
 bn,k = ⎧⎪⎪
⎨
⎪⎪⎩
 SBk([n])S, if k ≤ n
0, if k > n,

where b0,0 = 1 and bn,0 = 0 for n ≥ 1.

Theorem 1 ([12]). Assume b1,1 ≠ 0. If bn(x) = ∑
n
k=1 bn,kx
k is the enumerator for assemblies of
B-structures on [n], then (bn(x))n≥0 is a sequence of polynomials of binomial type.

Theorem 1 provides a realization of binomial sequences in combinatorial problems. If we
think of x as a positive integer such that SXS = x for some set X, then we can interpret bn(x) as
the number of assemblies of B-structures on [n], where each block carries a label from X. From
this viewpoint, it is easy to see that (bn(x))n≥0 is of binomial type.
This realization is only valid for binomial sequences whose coeﬃcients are non-negative
integers, and so excludes many polynomial sequences naturally appearing in combinatorics, for
example, the falling factorials x(n). Mullin and Rota expanded their construction slightly by
considering the monomorphic classes, in which diﬀerent blocks receive diﬀerent labels from X,
and hence the counting polynomial becomes ˜bn(x) = ∑
n
k=1 bn,kx(k). Ray [14] extended Mullin-
Rota’s theory and developed the concept of partition categories, and he proved that any binomial
sequence can be realized as a weight enumerator in partition lattices. We will use Ray’s model
in Section 3.

2.2 Generalized Gonˇcarov Polynomials and Vector Parking Functions

Let Z = (zi)i≥0 be a ﬁxed sequence with values in K, where K is the scalar ﬁeld. For our
purpose, it suﬃces to take K to be Q, R, or C. We call Z the interpolation grid and zi ∈ Z the

4

i-th interpolation node. Let T = (tn(x; ∆, Z))n≥0 be the unique sequence of polynomials that
satisﬁes εzi∆
i(tn(x; ∆, Z)) = n!δi,n, (3)

where εzi is evaluation at zi.

Deﬁnition 4. The polynomial sequence T = (tn(x; ∆, Z))n≥0 determined by (3) is called the
sequence of generalized Gonˇcarov polynomials associated with the pair (∆, Z) and tn(x; ∆, Z)
is the n-th generalized Gonˇcarov polynomial relative to the same pair.

This sequence T has a number of interesting algebraic properties. One of them is a recurrence
formula described as follows: Let tn(x) = tn(x; ∆, Z) and {pn(x)}n≥0 be the basic sequence
associated to ∆. Then
 pn(x) = n
Q
i=0 ‹
n
i • pn−i(zi) ti(x). (4)

We remark that by deﬁnition, to compute the generalized Gonˇcarov polynomials given the
basic sequence, one would ﬁnd the conjugate operator Λ via (2), compute ∆ by solving for the
compositional inverse of the D-indicator of Λ, and then ﬁnd the n-th polynomial tn(x) of the
sequence by using (3). The computation required in this process can be quite involved. However,
(4) gives a recursive formula which can be used as an alternative deﬁnition for tn(x), which is
much more convenient in combinatorial problems. For other algebraic properties of generalized
Gonˇcarov polynomials, see [11].
Classical Gonˇcarov polynomials have a combinatorial interpretation in enumeration. Let ⃗u =
(ui)i≥1 be a sequence of non-decreasing positive integers. A (vector) ⃗u-parking function of length
n is a sequence (x1, ..., xn) of positive integers whose order statistics, i.e., the nondecreasing
rearrangement (x(1), x(2), ..., x(n)), satisfy the inequalities x(i) ≤ ui for all i = 1, . . . , n. Vector
parking functions can be described via a parking process of n cars trying to park along a line
of x ≥ n parking spots. Cars enter one by one in order, and before parking, each driver has a
preferred parking spot. Each driver goes to her preferred spot directly and parks in the ﬁrst
spot available from there, if there exists one. A ⃗u-parking function is a sequence of drivers’
preferences such that at least i cars prefer to park in the ﬁrst ui spots, for all i = 1, . . . , n. When
ui = i, we recover the classical parking functions, which were originally introduced by Konheim
and Weiss [7] and are the preference sequences such that x = n and every driver can ﬁnd some
spot to park. In general, the n-th Gonˇcarov polynomials associated to the pair (D, −Z) counts
the number of ⃗z-parking functions of length n, where ⃗z = (z0, z1, . . . , zn−1) is the initial segment
of the grid Z; see [9].
A concrete realization of tn(x; ∆, Z) for some other delta operators ∆ is found in a combina-
torial object called reluctant functions whose underlying structure are families of labeled trees.
In [11], it is proved for some properly deﬁned ∆ and Z, tn(x; ∆, Z) enumerates the number of
reluctant functions in a certain binomial class B whose label sequences are ⃗z-parking functions.
The object of the present paper is to extend this result and prove that for any delta operator, the
generalized Gonˇcarov polynomials (up to a scaling) have a realization as a weighted enumerator
in partition lattices and in any exponential family.

5

3 Gonˇcarov Polynomials in Partition Lattices

In this section we give a generic, or universal realization of generalized Gonˇcarov polynomials in
weighted enumeration over partition lattices. Our result is built on Ray’s solution of the real-
ization problem for arbitrary sequences of binomial types in the context of partition categories.
Here, we will simplify his notation and present his construction in terms of incidence algebra
of partially ordered sets, which was the language originally used by combinatorialists, e.g., see
Joni and Rota [6].
For any ﬁnite set S, let Π(S) denote the set of all partitions of S, and write Πn for Π([n]).
Elements of Π(S) are partially ordered by reﬁnement: that is, deﬁne π ≤ σ if every block of
π is contained in a block of σ. In particular, Π(E) has a unique maximal element ˆ1 that has
only one block and a unique minimal element ˆ0 for which every block is a singleton. Let SπS be
the number of blocks of π and Π(π) be the partitions of the set that consists of blocks of π,
When π ≤ σ, the induced partition σ~π is the partition σ viewed as an element of Π(π). Deﬁne
the class of (π, σ) as the sequence λ = (λ1, λ2, ...) of non-negative integers such that λi is the
number of blocks of size i in the partition σ~π, for 1 ≤ i ≤ SπS. It follows that

Q
i≥1 iλi = SπS and Q
i≥1 λi = SσS.

Example 1. Let E = [8], π = {1}, {2}, {345}, {67}, {8}, σ = {1345}, {2}, {678} ∈ Π8. Then,
σ~π = {(1), (345)}, {(2)}, {(67), (8)} ∈ Π(π). The class of (π, σ) is λ = (1, 2, 0, 0, ...), where we
have ∑i≥1 iλi = SπS = 5 and ∑i≥1 λi = SσS = 3.

We recall the basic notation in incidence algebra. Let P be a ﬁnite poset and A a commutative
ring with unity. Denote by Int(P ) the set of all intervals of P , i.e., the set {(x, y) ∶ x ≤ y}. The
incidence algebra I(P, A) of P over A is the A-algebra of all functions

f ∶ Int(P ) → A,

where multiplication is deﬁned via the convolution

f g(x, y) = Q
x≤z≤y f (x, z)g(z, y).

The algebra I(P, A) is associative with identity δ, where

δ(x, y) = ⎧⎪⎪
⎨
⎪⎪⎩
 1, if x = y,
0, if x ≠ y.

An element f ∈ I(P, A) is invertible under the multiplication if and only if f (x, x) is invertible
in A for every x ∈ P .
In this paper we are concerned with the case P = Πn, the partition lattice of [n], and
A = K[w2, w3, . . .], where w2, w3, ... are independent variables. In addition, we set w1 = 1.

Deﬁnition 5. Assume π ≤ σ in Πn and the class of (π, σ) is λ = (λ1, λ2, . . .). Deﬁne the zeta-type
function w(π, σ) ∈ I(Πn, A) by letting

w(π, σ) = wλ1
1 wλ2
2 . . . wλSπS
SπS . (5)

6

Note that w(π, π) = 1 for all π. Hence w is invertible. The inverse of w is called the
M¨obius-type function and denoted by µw. Explicitly, µw(π, π) = 1 and for π < σ,

µw(π, σ) = − Q
π≤τ <σ µw(π, τ )w(τ, σ).

When all wi = 1, the zeta-type function and the M¨obius-type function become the zeta function
and the M¨obius function of Πn respectively.

Example 2. Consider the lattice Π3. Then for all π < σ, w(π, σ) = w2 except that w(ˆ0, ˆ1) = w3.
Consequently, µw(π, σ) = −w2 if π < σ except that µw(ˆ0, ˆ1) = 3w2
2 − w3.

Deﬁne the zeta-type enumerator {an(x; w)}n≥0 and M¨obius-type enumerator {bn(x; w)}n≥0
as follows. Let a0(x; w) = b0(x; w) = 1 and for n ≥ 1,

an(x; w) = Q
π∈Πn w(ˆ0, π) x
SπS, (6)

bn(x; w) = Q
π∈Πn µw(ˆ0, π) x
SπS. (7)

Theorem 2 ([14]). 1. The polynomial sequences {an(x; w)}n≥0 and {bn(x; w)}n≥0 are of bi-
nomial type.
2. Let Λ be the delta operator whose D-indicator is given by g(t) = t + ∑i≥2 witi~i!. Then
{an(x; w)}n≥0 is the conjugate sequence of Λ and {bn(x; w)}n≥0 is the basic sequence of Λ.

For n = 0, 1, . . . , 4, the polynomials an(w, x) and bn(w, x) are

a0(x; w) = 1,

a1(x; w) = x,

a2(x; w) = x
2 + w2x,

a3(x; w) = x
3 + 3w2x
2 + w3x,

a4(x; w) = x
4 + 6w2x
3 + (4w3 + 3w2
2)x
2 + w4x,

and
 b0(x; w) = 1,

b1(x; w) = x,

b2(x; w) = x
2 − w2x,

b3(x; w) = x
3 − 3w2x
2 + (3w2
2 − w3)x,

b4(x; w) = x
4 − 6w2x
3 + (15w2
2 − 4w3)x
2 + (10w2w3 − w4 − 15w3
2)x.

The linear coeﬃcient in bn(w; x) is µw
n = µw(ˆ0, ˆ1) in Πn. Assume ∆ is the conjugate delta
operator of Λ. Then {an(x; w)}n≥0 is the basic sequence of ∆ and {bn(x; w)}n≥0 is the conjugate
sequence of ∆. The operator ∆ can be written as ∆ = ∑n≥1 µw
n Dn~n!. Since w1 = 1, each µw
n
is a polynomial of w2, w3, . . . . If we take w1 to be a variable, µw
n would be a polynomial in
w−1
1 , w2, w3, . . . .
The condition w1 = 1 is equivalent to the equation a1(x; w) = x. Since the weight vari-
ables w2, w3, . . . can take arbitrary values, Theorem 2 implies that any polynomial sequence

7

{pn(x)}n≥0 of binomial type with p1(x) = x can be realized as the zeta-type weight enumerator
or the M¨obius-type weight enumerator over partition lattices. Note that for any scalar k ≠ 0,
if a sequence {pn(x)}n≥0 is the basic sequence of ∆ and the conjugate sequence of Λ, then
{pn~kn}n≥0 is the basic sequence of k∆ and the conjugate sequence of g(D~k) where g(t) is the
D-indicator of Λ. Hence Theorem 2 covers all polynomial sequences of binomial type up to a
scaling.
In the problem of counting assemblies of B-structures outlined in Section 2.1, the enumerator

∑k bn,kx
k in Theorem 1 is a specialization of the polynomial an(x; w), where wn is the number
of B-structures on a block of size n. For example, when B is the set of rooted trees, wn = nn−1

and hence an(x; w) = x(x + n)
n−1, the n-th Abel polynomial.
Our objective is to ﬁt the generalized Gonˇcarov polynomials into this model and present
a combinatorial interpretation in terms of weight-enumeration in partition lattices. Following
the notation of Theorem 2, let ∆ be the conjugate delta operator of Λ. Given an interpolation
grid Z, we denote by tn(x; w, Z) the n-th generalized Gonˇcarov polynomial relative to the pair
(∆, Z). We use this notation to emphasize the role of the zeta-type function w(π, σ).
To get a formula for the polynomial tn(x; w, Z), we use the recurrence (4) in Section 2.2.
Since an(x; w) is the basic sequence of ∆, {tn(x; w, Z)}n≥0 is the unique sequence of polynomials
that satisﬁes the recurrence

an(x; w) = n
Q
i=0 ‹n
i •an−i(zi; w) ti(x; w, Z). (8)

In other words,
 tn(x; w, Z) = an(x; w) − n−1
Q
i=0 ‹n
i •an−i(zi; w) ti(x; w, Z). (9)

In particular, t0(x; w, Z) = 1 and t1(x; w, Z) = a1(x; w)−a1(z0; w) = x−z0. Here we again assume
w1 = 1 and hence a1(x; w) = x. Since if ∆ is changed to k∆, the corresponding tn(x; w, Z) just
changes to tn(x; w, Z)~kn, again we cover all the cases up to a scaling.
Assume x is a positive integer and X = {1, 2, . . . , x}. Then an(x; w) is the zeta-type weight
enumerator of all the block-labeled partitions, where each block of the partition carries a label
from X. In symbols,
 an(x; w) = Q
π∈Πn w(ˆ0, π) ⋅ S{f ∶ Block(π) → X}S,

where Block(π) is the set of blocks of π. For a partition π with a block-labeling f , we record
the labeling by the list fπ = (x1, x2, . . . , xn), where xi = f (Bj) whenever i is in the block Bj of
π. Let ⃗z = (z0, z1, ⋯, zn−1) be the initial segment of the grid Z. Furthermore, assume that
z0 ≤ z1⋯ ≤ zn−1 are positive integers with zn−1 < x.
Deﬁne the set PF π(Z) as the set of all block-labelings of π that are also ⃗z-parking functions,
i.e.,
 PF π(Z) = {f ∶ Block(π) → X S fπ is a ⃗z-parking function}. (10)

More precisely, PF π(Z) is the set of block-labelings of π such that the order statistics of
fπ = (x1, x2, . . . , xn) satisﬁes x(i) ≤ zi−1 for i = 1, . . . , n. Let P Fπ(Z) be the cardinality of
PF π(Z).
 8

Our main result of this section is the following theorem.

Theorem 3. Assume tn(x; w, Z) is the n-th generalized Gonˇcarov polynomial deﬁned by (8)
with a positive increasing integer sequence Z = (z0, z1, ...). Let x be an integer larger than zn−1.
Then, tn(0; ω, −Z) = tn(x; ω, x − Z) = Q
π∈Πn w(ˆ0, π) ⋅ P Fπ(Z), (11)

where x − Z = (x − z0, x − z1, x − z2, . . . ) and −Z = (−z0, −z1, −z2, . . . ).

The ﬁrst equality follows from [11, Prop.3.5] that was proved by verifying the deﬁning equa-
tion (3), and the second equality follows from the recurrence (8) and Lemma 4 proved next.
Note that all three parts of (11) are polynomials of z0, z1, . . . , zn−1, hence (11) is a polynomial
identity.

Lemma 4. For every n ≥ 0, it holds that

an(x; w) = n
Q
i=0 ‹n
i •an−i(x − zi; w) Q
π∈Πi w(ˆ0, π) ⋅ P Fπ(Z) (12)

Proof. Again we assume that x and zi are positive integers and z0 < z1 < ⋯ < zn−1 < x. For a
ﬁnite set E and P , let S(E, P ) be the set of pairs (π, f ) where π is a partition of the set E and
f is a function from Block(π) to P . Then the left-hand side of (12) counts the set S([n], X)
by the zeta-type weight function w(ˆ0, π). Note that if π has blocks B1, B2, . . . , Bk, then

w(ˆ0, π) = k
M
j=1 wSBj S.

For a pair (π, f ) ∈ S([n], X) with fπ = (x1, x2, . . . , xn), let inc(fπ) = (x(1), x(2), . . . , x(n)) be
the non-decreasing rearrangement of the terms of fπ. Set

i(f ) = max{k ∶ x(j) ≤ zj−1 ∀j ≤ k}.

Thus, the maximality of i = i(f ) means that

x(1) ≤ z0, x(2) ≤ z1, ... , x(i) ≤ zi−1

and zi < x(i+1) ≤ x(i+2) ≤ ⋯ ≤ x(n) ≤ x.

In the case that x(j) > zj−1 for all j, we have i(f ) = 0.
Assume (xr1, ..., xri ) is the subsequence of fπ from which the non-decreasing sequence
(x(1), x(2), ..., x(i)) is obtained. Let R1 = {r1, r2, . . . , ri} ⊆ [n]. Then it is easy to see that
R1 must be a union of some blocks of π, while R2 = [n] ∖ R1 is the union of the remaining blocks
of π. Let π1 be the restriction of π on R1 and π2 the restriction of π on R2. Thus π is a disjoint
union of π1 and π2. Furthermore, let fi be the restriction of f on Ri. Then f1 is a map from
the blocks of π1 to {1, . . . , zi} that is also a ⃗z-parking function, and f2 is a map from blocks of
π2 to the set X ∖ [zi] = {zi + 1, . . . , x}.
Let S P (E, X) be the subset of S(E, X) such that for each pair (π, f ), the sequence fπ is
a ⃗z-parking function. Then the above argument deﬁnes a decomposition of (π, f ) ∈ S([n], X)

9

into pairs (π1, f1) ∈ S P (R1, X) and (π2, f2) ∈ S(R2, X ∖ [zi]). Conversely, any pairs of (π1, f1)
and (π2, f2) described above can be reassembled into a partition π of [n] with labels in X. In
other words, the set S([n], X) can be written as a disjoint union of Cartesian products as

S([n], X) = #
i;R1⊆[n]∶SR1S=i S P (R1, X) × S(R2, X ∖ [zi]). (13)

In addition, if π is the disjoint union of π1 and π2, then

w(ˆ0, π) = w(ˆ0, π1)w(ˆ0, π2).

Putting the above results together, we have

an(x; w) = Q
(π,f )∈S([n],X) w(ˆ0, π)

= n
Q
i=0 Q
R1∶SR1S=i
 ⎛

⎝ Q
(π1,f1)∈S p(R1,X) w(ˆ0, π1) ⋅ Q
(π2,f2)∈S(R2,X∖[zi]) w(ˆ0, π2)
⎞

⎠

= n
Q
i=0 ‹n
i •an−i(x − zi; w) Q
(π1,f1)∈S p(R1,X) w(ˆ0, π1)

= n
Q
i=0 ‹n
i •an−i(x − zi; w) Q
π∈Πi w(ˆ0, π)P Fπ(Z).

The last equation follows from the deﬁnition of P Fπ(Z).

Example 3. From the recurrence (8) we get

t2(x; w, Z) = x
2 + (w2 − 2z1)x + (2z0z1 − z2
0 − w2z0).

Hence t2(0; w, −Z) = 2z0z1 − z2
0 + w2z0. On the other hand, there are two partitions in Π2. For
π = {12}, clearly w(ˆ0, {12}) = w2 and P F{12}(Z) = z0. For π = {1}{2}, w(ˆ0, π) = 1 and P Fπ(Z)
is the number of pairs of positive integers (x, y) such that min(x, y) ≤ z0 and max(x, y) ≤ z1. It
is easy to check that there are 2z0z1 − z2
0 such pairs.

Since {an(x; w)} gives a generic form of the sequence of polynomials of binomial type,
{tn(x; w, Z)} is the generic form of the generalized Gonˇcarov polynomials. In particular, from
Theorem 3 we see that when w2 = w3 = ⋯ = 0, tn(0; w, −Z) gives the number of ⃗z-parking
functions of length n.

4 Gonˇcarov Polynomials in Exponential Families

In this section, we explore a more concrete realization of generalized Gonˇcarov polynomials in
exponential families, which are picturesque models that deal with counting structures that are
built out of connected pieces and can be applied to many combinatorial problems.

4.1 Exponential Families

Exponential families are combinatorial models based on the partition lattices where the enu-
meration are captured by the exponential generating functions. The description of exponential

10

families and their relation to the incidence algebra of Πn can be found in standard textbooks,
e.g., [16, Section 5.1]. Here we adopt Wilf’s description of exponential families [18] in the context
of ‘playing cards’ and ‘hands’.
Suppose that there is given an abstract set P of ‘pictures’, which typically are the connected
structures. A card C(S, p) is a pair consisting of a ﬁnite label set S of positive integers and a
picture p ∈ P . The weight of C is SSS. If S = [n], the card is called standard. A hand H is a
set of cards whose label sets form a partition of [n] for some n. The weight of a hand is the
sum of the weights of the cards in the hand. The n-th deck Dn is the set of all standard cards
of weights n. We require that Dn is always ﬁnite. An exponential family F is the collection of
decks D1, D2, . . . .
In an exponential family, let di = SDiS and hn,k be the number of hands H of weight n that
consist of k cards. Let h0(x) = 1 and for n ≥ 1,

hn(x) = n
Q
k=1 hn,kx
k. (14)

Then the main counting theorem, the exponential formula, states that these polynomials satisfy
the generating relation:
 exD(t) = Q
n≥0 hn(x) tn

n! , (15)

where D(t) = ∑k≥1 dktk~k!. In other words, if d1 = h1,1 ≠ 0, {hn(x)}n≥0 is a sequence of binomial
type that is conjugate to the delta operator ∑k≥1 dkDk~k!.

Example 4. Set Partitions: Here, a card is a label set [n] with a ‘picture’ of n dots. Each
deck Dn consists of the single card of weight n, and a hand is just a partition of the set [n].
Thus, hn,k is the number of partitions of the set [n] into k classes, which is S(n, k), the Stirling
number of the second kind.

Example 5. Permutations and their Cycles: Each card is a cyclic permutation on a label set
S. The deck Dn consists of all distinct cyclic permutations on [n] so dn = (n − 1)! and a hand
is a permutation of [n] consisting of k cycles. Thus, hn,k is the number of permutations on [n]
that have k cycles, that is, the signless Stirling number of the ﬁrst kind c(n, k).

Note that we can interpret x
k in hn(x) as the number of maps from the set of cards in a
hand to the set X = {1, . . . , x} for some positive integer x. Hence hn(x) counts the number of
hands of weight n in which each card is labeled by an element of X. This set-up gives a natural
combinatorial interpretation for binomial polynomial sequences whose coeﬃcients are positive
integers.
In Foundation III [12] Mullin and Rota introduced a structure called reluctant functions,
which can be used to give a combinatorial interpretation for some generalized Gonˇcarov poly-
nomials; see [11]. We remark that reluctant functions is a special case of exponential families,
in which the ‘pictures’ are certain sets of trees. We will show that by taking the type enumera-
tor an exponential family actually provides a combinatorial model for all generalized Gonˇcarov
polynomials.
 11

4.2 Type Enumerator in Exponential Families

In a given exponential family F , we have seen that

hn(x) = n
Q
k=1 hn,kx
k = Q
H S{f ∶ cards in H → X}S (16)

where H ranges over all hands of weight n. For a hand H consisting of cards C1, C2, . . . , Ck of
weights t1, t2, . . . , tk, deﬁne the type of H as

type(H) = yt1 yt2⋯ytk ,

where y1, y2, . . . , are free variables.
Let hn(x; y) = Q
H∶ weight n type(H)S{f ∶ cards in H → X}S. (17)

Then we have the following form of the exponential formula.

Proposition 5. The sequence of type enumerators {hn(x; y)}n≥0, viewed as a polynomial in x,
is a sequence of polynomials of binomial type satisfying the equation

Q
n≥0 hn(x; y) tn

n! = exp Œx Q
k≥1 dkyk tk

k! ‘ . (18)

Proof. We compare the formula of hn(x; y) with that of hn(x). Note for n ≥ 1, hn(x) can be
computed by hn(x) = Q
k≥1 Q
H={C1,...,Ck} dt1 dt2 ⋯dtk x
k, (19)

where {C1, ⋯, Ck} is a hand of weight n and ti is the weight of card Ci, while

hn(x; y) = Q
k≥1 Q
H={C1,...,Ck} dt1 dt2 ⋯dtk yt1yt2⋯ytk x
k. (20)

The exponential formula for hn(x) then implies Proposition 5.

Remark. Comparing to the generic form an(x; w) in the previous section, we see that hn(x; y)
corresponds to the case where the variables in the zeta-type function are determined by wn =
dnyn. As far as d1 ≠ 0, we can obtain arbitrary polynomial sequences of binomial type by taking
suitable values for the yi-variables.

4.3 Sequence of Generalized Goncarov Polynomials

Let Z = (zi)i≥0 be an interpolation grid. For the binomial sequence {hn(x; y)}n≥0 deﬁned in an
exponential family F , we can consider the associated generalized Gonˇcarov polynomials given
by (4) with pn(x) replaced by hn(x; y). Denote this Gonˇcarov polynomial by tn(x; y, F , Z) to
emphasize that it has variables yi and is deﬁned in F . Explicitly, tn(x; y, F , Z) is obtained by
the recurrence
 tn(x; y, F , Z) = hn(x; y) − n−1
Q
i=0 ‹n
i •hn−i(zi; y)ti(x; y, F , Z). (21)

12

Suppose X = {1, 2, ..., x} and assume that z0 ≤ z1 ≤ ⋯ ≤ zn−1 are integers in X. Let
⃗z = (z0, z1, . . . , zn−1). For a hand H = {C1, C2, . . . , Ck} of weight n with a function f from
{C1, C2, . . . , Ck} to X, denote by fH the list (x1, x2, . . . , xn), where xi = f (Cj) if i is in the label
set of Cj. Let
 PF H (Z) = {f ∶ {C1, C2, . . . , Ck} → X S fH is a ⃗z-parking function},

and P FH (Z) the cardinality of PF H (Z). Then we have the following analog of Theorem 3.

Theorem 6. For n ≥ 0,

tn(0; y, F , −Z) = tn(x; y, F , x − Z) = Q
H∶ of weight n type(H) ⋅ P FH (Z). (22)

Here by convention, the third term of (22) equals 1 when n = 0.

Theorem 6 follows from (21) and the following recurrence relation

hn(x; y) = n
Q
i=0 ‹n
i •hn−i(x − zi; y) Q
H∶ of weight i type(H) ⋅ P FH (Z), (23)

whose proof is similar to that of Lemma 4. In an exponential family F , let A(S, X) be the set
of pairs (H, f ) such that H is a hand whose label sets form a partition of S and f is a function
from the cards in H to X. Then the basic ingredients of the proof are that
(1) type(H) is a multiplicative function only depending on the weights of cards in H, and
(2) The set A([n], X) can be decomposed into a disjoint union of Cartesian products of the
form AP (R, X) × A([n] ∖ R, X ∖ [zi]),

where AP (R, X) = {(H, f ) ∈ A(R, X) ∶ fH is a ⃗z-parking function}, and the disjoint union
is taken over all the subsets R of [n].
We skip the details of the proof of Eq. (23).
We illustrate the above results and some connections to combinatorics in the exponential
families given in Examples 4 and 5. There are many other exponential families in which the type
enumerator and associated Gonˇcarov polynomials have interesting combinatorial signiﬁcance.
1. Let F1 be the exponential family of set partitions described in Example 4. In this family,

di = 1 for all i and hn(x) = n
∑
k=0 S(n, k)x
k. In the type enumerator, if we substitute y1 = 1

and yi = wi for i ≥ 2, then hn(x; y) is exactly the same as the generic sequence an(x; w)
in (6), and consequently tn(x; y, F1, Z) is the same as the generic Gonˇcarov polynomial
tn(x; w, Z) deﬁned by (9). In particular, if all yi = 1, tn(0; y, F1, −Z) gives a formula for
the number of ⃗z-parking functions with the additional structure that cars arrive in disjoint
groups, and drivers in the same group always prefer the same parking spot.
When yi = 1 and zi = 1 + i for all i, the ﬁrst few terms of the Gonˇcarov polynomials

13

tn(x) = tn(x; y, F1, −Z) are

t0(x) = 1

t1(x) = x + 1

t2(x) = x
2 + 5x + 4

t3(x) = x
3 + 12x
2 + 40x + 29

t4(x) = x
4 + 22x
3 + 163x
2 + 453x + 311

In particular, for x = 0 we get the sequence 1, 1, 4, 29, 311, .... This is sequence A030019 in
the On-Line Encyclopedia of Integer Sequences (OEIS) [13], where it is interpreted as the
number of labeled spanning trees in the complete hypergraph on n vertices (all hyper-edges
having cardinality 2 or greater). It would be interesting to ﬁnd a direct bijection between
the hyper-trees and the parking-function interpretation.
2. Let F2 be the exponential family of the permutations and their cycles, as described in

Example 5. Here dn = (n − 1)! and hn(x) = n
∑
k=0 c(n, k)x
k = x
(n), where the c(n, k) is the

signless Stirling numbers of the ﬁrst kind and x
(n) is the rising factorial x(x+1)⋯(x+n−1).
When y1 = 1, the Gonˇcarov polynomial tn(x; y, F2, Z) can be obtained from the generic
form tn(x; w, Z) by replacing wn with (n − 1)!yn for n ≥ 2. When all yi = 1, i.e. y = 1,
tn(0; 1, F2, −Z) gives a formula for the number of ⃗z-parking functions with the addition
requirement that cars are formed in disjoint cycles, and drivers in the same cycle prefer
the same parking spot.
In addition, when y = 1, and Z is the arithmetic progression zi = a + bi, the Goncarov
polynomial is tn(x; 1, F2; −Z) = (x + a)(x + a + nb + 1)
(n−1). (24)

Another combinatorial interpretation of tn(0; 1, F2, −Z) is given in [11, Section 6.7], where
it shows that tn(0; 1, F , −Z) is n! times the number of lattice paths from (0, 0) to (x−1, n)
with strict right boundary Z. For example, when zi = a + bi for some positive integers a
and b, 1
n! tn(0; 1, F2, −Z) is the number of lattice paths from (0, 0) to (x − 1, n) which stay
strictly to the left of the points (a + ib, i) for i = 0, 1, . . . , n. In particular for a = 1 and
b = k, it counts the number of labeled lattice paths from the origin to (kn, n) that never
pass below the line x = yk. In that case (24) gives 1
1+kn ‰(k+1)n
n Ž, the n-th k-Fuss-Catalan
number.

Remark. We can also consider the injective functions in the deﬁnition of hn(x) and hn(x; y) in
(16) and (17), where the term x
k is replaced by the lower factorial x(k) = x(x − 1)⋯(x − k + 1). In
other words, cards of a hand are labeled by X with the additional property that diﬀerent cards
get diﬀerent labels. Some examples are given in [11, Section 6] and called monomorphic classes.
A result analogous to Theorem 6 still holds for the momomorphic classes of an exponential
family.

As a ﬁnal result we point out an explicit formula to compute the constant coeﬃcient of the
generalized Gonˇcarov polynomial whenever we know the basic sequence {pn(x)}n≥0. It is proved
in [11] and only depends on the recurrence (4) and the fact that pn(0) = 0 for n > 0. The proof

14

does not need an explicit formula for the delta operator ∆ and hence the result is easier to use
when we need to compute the value of tn(0; y, F , −Z) in a given exponential family.
Let {pn(x)}n≥0 be a sequence of binomial type and Z = (z0, z1, . . . ) be a given grid. Assume
{tn(0; −Z)}n≥0 is deﬁned by the recurrence relation

tn(0; −Z) = − n−1
Q
i=0 ‹n
i •pn−i(−zi)ti(0),

for n ≥ 1 and t0(0; −Z) = 1. Then for n ≥ 1, tn(0; −Z) can be expressed as a summation over
ordered partitions.
Given a ﬁnite set S with n elements, an ordered partition of S is an ordered list (B1, ..., Bk)
of disjoint nonempty subsets of S such that B1 ∪ ⋯ ∪ Bk = S. If ρ = (B1, ..., Bk) is an ordered
partition of S, then we set SρS = k. For each i = 1, 2, ..., k, we let bi = bi(ρ) = SBiS, and si ∶= si(ρ) ∶=

∑
i
j=1 bj. In particular, set s0(p) = 0. Let Rn be the set of all ordered partitions of the set [n].

Theorem 7 ([11]). For n ≥ 1,

tn(0; −Z) = Q
ρ∈Rn(−1)
SρS k−1
M
i=0 pbi+1(−zsi)

= Q
ρ∈Rn(−1)
SρSpb1 (−z0), ⋯ pbk (−zsk−1). (25)

The following list is the formulas for the ﬁrst several Gonˇcarov polynomials.

t0(0; −Z) = 1

t1(0; −Z) = −p1(−z0)

t2(0; −Z) = 2p1(−z0)p1(−z1) − p2(−z0)

t3(0; −Z) = −p3(−z0) + 3p2(−z0)p1(−z2) + 3p1(−z0)p2(−z1) − 6p1(−z0)p1(−z1)p1(−z2).

4.4 Degenerate Cases

In an exponential family, the polynomial hn(x) or hn(x; y) may not always have degree n, e.g.,
when d1 = h1,1 = 0. We say that such polynomial sequences and the corresponding exponential
families are degenerate. For a degenerate sequence of polynomials, there is no delta operator
for which the sequence is the basic or the conjugate sequence. Nevertheless, the exponential
formulas (15) and (18) are still true. Hence the sequences {hn(x)}n≥0 and {hn(x; y)}n≥0 still
satisfy the binomial-type identity (1).
Without a delta operator, we cannot deﬁne the generalized Gonˇcarov interpolation problems.
However, we can still introduce the generalized Gonˇcarov polynomials via the recurrence (4).
Furthermore, we will prove in Theorem 8 that the shift invariance of Gonˇcarov polynomials
can also be derived from (4). Therefore, Theorems 6 and 7 still hold true for the degenerate
exponential families since all the proofs follow from the binomial-type identity (1) and the
recurrence (4).

Theorem 8. Assume {pn(x)}n≥0 is a polynomial sequence of binomial type with p0(x) = 1, but
the degree of an(x) is not necessary n. Let tn(x; Z) be deﬁned by the recurrence relation

tn(x; Z) = pn(x) − n−1
Q
i=0 ‹n
i •pn−i(zi)ti(x; Z). (26)

15

For any scalar η and the interpolation grid Z = {z0, z1, z2, . . . ), let Z + η be the sequence (z0 +
η, z1 + η, z2 + η, ⋯). Then we have
 tn(x + η; Z + η) = tn(x; Z) (27)

for all n ≥ 0.

Proof. We prove Theorem 8 by induction on n. The initial case n = 0 is trivial since t0(x; Z) = 1
for all x and any grid Z. Assume Eq. (27) is true for all indices less than n. We compute
tn(x + η; Z + η). By deﬁnition

tn(x + η; Z + η) = pn(x + η) − n−1
Q
i=0 ‹n
i •pn−i(zi + η)ti(x + η; Z + η). (28)

By the inductive hypothesis ti(x + η; Z + η) = ti(x; Z) for i < n and the binomial identity of
pn(x), the right-hand side of (28) can be written as

n
Q
k=0 ‹n
k•pk(x)pn−k(η) − n−1
Q
i=0 ‹n
i • ⎛
⎝

n−i
Q
j=0 ‹
n − i
j •pn−i−j (zi)pj(η)
⎞
⎠ ti(x; Z)

= n
Q
k=0 ‹n
k•pk(x)pn−k(η) − Q

i+j≤n
except (i,j)=(n,0) ‹
n
i •‹
n − i
j •pj(η)pn−i−j(zi)ti(x; Z) (29)

Since ‹n
i •‹n − i
j • = n!
i!j!(n − i − j)! = ‹n
j •‹n − j
i •,

then (29) can be expressed as

n
Q
k=0 ‹n
k•pk(x)pn−k(η) − Q

i+j≤n
except (i,j)=(n,0) ‹n
j •‹
n − j
i •pj(η)pn−i−j (zi)ti(x; Z)

= n
Q
k=0 ‹n
k•pk(x)pn−k(η) − n
Q
j=1 ‹n
j •pj(η)
 n−j
Q
i=0 ‹
n − j
i •pn−i−j (zi)ti(x; Z)

− n−1
Q
i=0 ‹n
i •pn−i(zi)ti(x; Z). (30)

The last summation in (30) corresponds to the terms with j = 0. Note that

n−j
Q
i=0 ‹n − j
i •pn−i−j (zi)ti(x; Z) = pn−j(x).

Hence For. (30) is equal to

n
Q
k=0 ‹n
k•pk(x)pn−k(η) − n
Q
j=1 ‹n
j •pj(η)pn−j(x) − n−1
Q
i=0 ‹
n
i •pn−i(zi)ti(x; Z)

= pn(x) − n−1
Q
i=0 ‹n
i •pn−i(zi)ti(x; Z)

= tn(x; Z).

This ﬁnishes the proof.
 16

The next example shows a degenerate exponential family.

Example 6. 2-Regular simple graphs. In this exponential family a card is an undirected cycle
on a label set [m] (where m ≥ 3). The deck Dn consists of all undirected circular arrangements
of n letters so dn = 1
2 (n − 1)! for n ≥ 3 and d1 = d2 = 0. A hand is then a undirected simple graph
on the vertex set [n], which is 2-regular, that is, every vertex has degree 2. Thus, hn,k is the
number of undirected 2-regular simple graphs on n vertices consisting of k cycles. Denote by
F3 this exponential family.
For F3, the type enumerators are h0(x, y) = 1, h1(x; y) = h2(x; y) = 0, h3(x; y) = y3x,
h4(x; y) = 2y4x, h5(x, y) = 12y5x, and h6(x; y) = 60y6x + 10y2
3x
2, etc. Although the degree of
hn(x; y) is not n, the exponential formula still holds:

n
Q
k=0 hn(x; y) tk

k! = exp Œx Q
k≥3 yk tk

2k ‘ .

We compute by the recurrence (21) that

t0(x; y, F3, Z) = 1

t1(x; y, F3, Z) = t2(x; y, F3, Z) = 0

t3(x; y, F3, Z) = y3(x − z0),

t4(x; y, F3, Z) = 3y3(x − z0),

t5(x; y, F3, Z) = 12y5(x − z0),

t6(x; y, F3, Z) = 10y2
3x
2 + 60y6x − 20y2
3z3x − 60y6z0 − 10y2
3z2
0 + 20y2
3z0z3.

The equation tn(0; y, F3, −Z) = Q
H∶ of weight n type(H) ⋅ P FH (Z)

is still true. For example, for n = 6, t6(0; y, F3, −Z) = 60y6z0 + 20y2
3z0z3 − 10y2
3z2
0. The term
60y6z0 comes from the 5!~2 = 60 6-cycles, and the terms 10y2
3(2z0z3 − z2
0) comes from the 10
hands each with two 3-cycles.

5 Closing Remarks

In this paper we present the combinatorial interpretation of an arbitrary sequence of Gonˇcarov
polynomials associated with a polynomial sequence of binomial type. There are many other
combinatorial problems that provide a formal framework of coalgebras, bialgebras, or Hopf
algebras [6]. In those problems the counting sequences satisfy an identity that is analogous to
the binomial-type identity (1), with the binomial coeﬃcients ‰
n
i Ž replaced by some other section
coeﬃcients. For example, the theory of binomial enumeration proposed by Mullin and Rota [12]
was generalized to an abstract context and applied to dissecting schemes by Henle [5]. It would
be an interesting project to investigate the role of generalized Gonˇcarov polynomials in these
other dissecting schemes and discrete structures. As suggested by Henle, this research may lead
to connections to rook polynomials, order invariants of posets, Tutte invariants of combinatorial
geometries, cycle indices and symmetric functions, and many others.

17

References

[1] J. L. Frank and J. K. Shaw, Abel-Goncarov polynomial expansions, J. Approx. Theory 10
(1974), No. 1, 6-22.
[2] V. L. Gonˇcarov, Recherches sur les d´eriv´ees successives des fonctions analytiques. Etude
des valeurs que les d´eriv´ees prennent dans une suite de domaines, Bull. Acad. Sc. Leningrad
(1930), 73-104.
[3] V. L. Gonˇcarov, The Theory of Interpolation and Approximation of Functions, Gostekhiz-
dat: Moscow, 1954.
[4] F. Haslinger, Abel-Goncarov polynomial expansions in spaces of holomorphic functions, J.
Lond. Math. Soc. (2) 21 (1980), No. 3, 487-495.
[5] M. Henle, Binomial enumeration on dissects, Trans. Amer. Math. Soc. 202 (1975), 1-39.
[6] S.A. Joni and G.-C. Rota, Coalgebras and bialgebras in Combinatorics, Umbral calculus and
Hopf algebras (Norman, Okla., 1978), Contemp. Math., 6, Amer. Math. Soc., Providence,
R.I., 1982, 1–47.
[7] A. G. Konheim and B. Weiss, An occupancy discipline and applications, SIAM J. Appl.
Math. 14 (1966), No. 6, 1266-1274.
[8] J.P.S. Kung, A probabilistic interpretation of the Gonˇcarov and related polynomials, J.
Math. Anal. Appl. 79 (1981), 349–351.
[9] J. P. S. Kung and C. Yan, Goncarov polynomials and parking functions, J. Combin. Theory
Ser. A 102 (2003), No. 1, 16-37.
[10] N. Levinson, The Gontcharoﬀ polynomials, Duke Math. J. 11 (1944), No. 4, 729-733.
[11] R. Lorentz, S. Tringali, C. Yan, Generalized Goncarov polynomials, S. Butler et al. (Eds.),
Connections in Discrete Mathematics: A Celebration of the Work of Ron Graham, Cam-
bridge University Press, Cambridge, 2018, 56–85.
[12] R. Mullin, G.-C. Rota, On the foundations of combinatorial theory. III. Theory of bino-
mial enumeration. 1970 Graph Theory and its Applications (Proc. Advanced Sem., Math.
Research Center, Univ. of Wisconsin, Madison, Wis., 1969) pp. 167-213 Academic Press,
New York.
[13] The On-Line Encyclopedia of Integer Sequences, https://oeis.org.
[14] N. Ray, Umbral calculus, binomial enumeration and chromatic polynomials, Trans. Amer.
Math. Soc. 309 (1988), No. 1, 191-213.
[15] G.-C. Rota, D. Kahaner, and A. Odlyzko, On the foundations of combinatorial theory. VII.
Finite operator calculus, J. Math. Anal. Appl. 42 (1973), No. 3, 684-760.
[16] R. P. Stanley, Enumerative combinatorics. Vol. 2. Cambridge Studies in Advanced Mathe-
matics, 62. Cambridge University Press, Cambridge, 1999.
[17] J. M. Whittaker, Interpolatory function theory, Cambridge Tracts in Math. and Math.
Physics 33, Cambridge University Press: Cambridge, 1935.
[18] H. S. Wilf, generatingfunctionology. Third edition. A K Peters, Ltd., Wellesley, MA, 2006.
[19] C. Yan, Parking Functions, M. B´ona (ed.), Handbook of Enumerative Combinatorics, Dis-
crete Math. Appl., CRC Press Boca Raton, FL, 2015, 835–893.

18
