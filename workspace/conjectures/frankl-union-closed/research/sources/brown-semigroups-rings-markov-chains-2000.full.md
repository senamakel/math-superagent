<!-- source: https://arxiv.org/pdf/math/0006145 | converted from PDF -->

arXiv:math/0006145v1  [math.PR]  20 Jun 2000
SEMIGROUPS, RINGS, AND MARKOV CHAINS

KENNETH S. BROWN

Abstract. We analyze random walks on a class of semigroups called “left-
regular bands”. These walks include the hyperplane chamber walks of Bidi-
gare, Hanlon, and Rockmore. Using methods of ring theory, we show that the
transition matrices are diagonalizable and we calculate the eigenvalues and
multiplicities. The methods lead to explicit formulas for the projections onto
the eigenspaces. As examples of these semigroup walks, we construct a random
walk on the maximal chains of any distributive lattice, as well as two random
walks associated with any matroid. The examples include a q-analogue of the
Tsetlin library. The multiplicities of the eigenvalues in the matroid walks are
“generalized derangement numbers”, which may be of independent interest.

1. Introduction

There are many tools available for the study of random walks on ﬁnite groups,
an important one being representation theory [15]. For ﬁnite semigroups, on the
other hand, there is no representation theory comparable to that for groups. And,
although there is some general theory of random walks [22, 17], much less is known
for semigroups than for groups. We consider here a special class of ﬁnite semi-
groups whose irreducible representations can be worked out explcitly (they are
all 1-dimensional), and we use this information to analyze the random walks. In
particular, we calculate the eigenvalues, which turn out to be real.
The semigroups we treat are called “left-regular bands” in the semigroup lit-
erature. There are many interesting examples of them, including the hyperplane
chamber walks introduced by Bidigare, Hanlon, and Rockmore [6], as well as several
new examples. Our approach via representation theory provides a clear conceptual
explanation for some of the remarkable features of the hyperplane chamber walks
proved in [6, 11].

1.1. Random walks on left-regular bands. A left-regular band, or LRB, is a
semigroup S that satisﬁes the identities

x
2 = x and xyx = xy(D)

for all x, y ∈ S. We call (D) the “deletion property”, because it admits the following
restatement: Whenever we have a product x1x2 · · · xn in S, we can delete any factor
that has occurred earlier without changing the value of the product. Information
about LRBs can be found in [20, 26, 27]. Early references to the identity xyx = xy
are [24, 29].
Our LRBs will always be ﬁnite and, for simplicity, will usually have an identity.
The second assumption involves no loss of generality, since we can always adjoin an
identity to S and property (D) still holds. And even the ﬁrst assumption involves
very little loss of generality, since (D) implies that S is ﬁnite if it is ﬁnitely generated.

Date: September 20, 1999.
 1

2 KENNETH S. BROWN

To run a random walk on S, start with a probability distribution {wx}x∈S on S.
A step in the walk then goes from s to xs, where x ∈ S is chosen with probability wx.
Thus there is a transition from s to t with probability

P (s, t) = ∑

xs=t wx.(1)

As we will see in the examples below, it is natural to consider a slight variant of
this walk, in which we conﬁne ourselves to elements of a left ideal I ⊆ S, i.e., a
nonempty subset that is closed under left-multiplication by arbitrary elements of S.
If the walk starts in I then it stays there, so we have a Markov chain on I with
transition matrix given by (1) for s, t ∈ I.
The next three subsections give examples of LRBs and the associated random
walks.

1.2. Example: Hyperplane face semigroups. These are the motivating exam-
ples that led to the present paper. Brieﬂy, a ﬁnite set of aﬃne hyperplanes in a real
vector space V divides V into regions called chambers. These are polyhedral sets,
which have faces. The totality F of all the faces is a poset under the face relation.
Less obviously, F admits a product, making it a LRB. See Appendix A for details.
Assume for simplicity that the arrangement is central (i.e., that the hyperplanes
have a nonempty intersection); in this case F has an identity.
The set C of chambers is an ideal, so we can run a random walk on it. A step in
the walk goes from a chamber C to the chamber F C, where F is chosen according
to some probability distribution {wF }F ∈F . Examples in [5, 6, 7, 11, 14] show that
these hyperplane chamber walks include a wide variety of interesting processes.
The references also explain a geometric interpretation of the step from C to F C:
Namely, F C is the chamber closest to C having F as a face.
Surprisingly, the eigenvalues of the transition matrix turn out to be real. In
fact, they are certain partial sums of the weights wF . To say which partial sums
occur, we need the intersection lattice L, consisting of all subspaces X ⊆ V that
are intersections of some of the given hyperplanes; we order L by inclusion. The
result, then, is that there is an eigenvalue λX = ∑
F ⊆X wF for each X ∈ L, with
multiplicity mX = |µ(X, V )|, where µ is the M¨obius function of L. This was proved
by Bidigare, Hanlon, and Rockmore [6]. A diﬀerent proof is given by Brown and
Diaconis [11], who show further that the transition matrix is diagonalizable.

1.3. Example: The free LRB. The free LRB with identity on n generators,
denoted Fn, may be constructed as follows: The elements of Fn are sequences
x = (x1, . . . , xl) of distinct elements of the set [n] = {1, . . . , n}, 0 ≤ l ≤ n. We
multiply two such sequences by

(x1, . . . , xl)(y1, . . . , ym) = (x1, . . . , xl, y1, . . . , ym)̂,

where the hat means “delete any element that has occurred earlier”. For example,

(2 1)(3 5 4 1 6) = (2 1 3 5 4 6).

One can think of the elements of Fn as reduced words on an alphabet of n letters,
where “reduced” means that the word cannot be shortened by applying (D).
The ideal I on which we will run our random walk is the set of reduced words
of length n; these can be identiﬁed with permutations. If the weights wx are
concentrated on the n generators, then the resulting random walk can be pictured
as follows: Think of (x1, . . . , xn) as the set of labels on a deck of n cards. Then

SEMIGROUPS, RINGS, AND MARKOV CHAINS 3

a step in the walk consists of removing the card labeled i with probability wi and
replacing it on top. This is the well-studied Tsetlin library, or weighted random-
to-top shuﬄe, which arises in the study of dynamic list-management in computer
science. See Fill [18] and the references cited there.
The eigenvalues were ﬁrst found by Phatarfod [28]; see also [5, 6, 11, 18] for other
proofs.
The result is that there is one eigenvalue λX = ∑
i∈X wi for each subset X ⊆ [n],
with multiplicity equal to the derangement number dn−|X|. Here dk is the number
of ﬁxed-point-free permutations of k elements. (Note that d1 = 0, so λX does not
actually occur as an eigenvalue if |X| = n − 1.)

1.4. Example: A q-analogue. Let V be the n-dimensional vector space Fn
q ,
where Fq is the ﬁeld with q-elements. Let Fn,q be the set of ordered linearly
independent sets (x1, . . . , xl) in V ; two such are multiplied by

(x1, . . . , xl)(y1, . . . , ym) = (x1, . . . , xl, y1, . . . , ym)̂,

where the hat means “delete any vector that is linearly dependent on the earlier
vectors”. Alternatively, we can think of the elements of Fn,q as n-rowed matrices
over Fq with independent columns; we multiply two such matrices by juxtaposing
them and then deleting the columns that are linearly dependent on earlier columns.
A natural ideal to use is the set of ordered bases of V or, equivalently, the set
of invertible matrices. If we now assign weights wv summing to 1 to the nonzero
vectors v ∈ V (i.e., to the sequences x as above of length 1), we get a Markov chain
on invertible matrices that can be described as follows: Given an invertible matrix,
pick a nonzero vector v with probability wv and adjoin it as a new ﬁrst column;
delete the unique column that is linearly dependent on the earlier ones.
This chain does not seem to have been considered before. We will see, as a
consequence of our main theorem, that its transition matrix is diagonalizable, with
an eigenvalue
 λX = ∑

v∈X wv

for each subspace X ⊆ V . The multiplicity mX of this eigenvalue is the number of
elements of GLn(Fq) with X as ﬁxed subspace, i.e., the number of elements that
ﬁx X pointwise and act as a derangement on the set-theoretic complement V − X.
This Markov chain is, in some sense, a q-analogue of the Tsetlin library. We will
construct in Section 5 a quotient ¯Fn,q of Fn,q, for which the random walk is more
deserving of the name “q-analogue of the Tsetlin library”.

1.5. The main result. If S is any ﬁnite LRB with identity, one can construct an
associated lattice L, along with a “support map” supp : S ։ L. For the hyperplane
face semigroup, L is the intersection lattice, the support of a face being its aﬃne
span. For S = Fn, L is the lattice of subsets of [n], and the support of a word
(x1, . . . , xl) is the underlying set {x1, . . . , xl} of letters. And for S = Fn,q, L is the
lattice of subspaces of Fn
q , the support of (x1, . . . , xl) being the subspace spanned
by {x1, . . . , xl}. The ideal on which we run our random walk is the set C of all
c ∈ S with supp c = ˆ1, where ˆ1 is the largest element of L. Borrowing terminology
from the hyperplane example, we call the elements of C chambers. Our main result,
illustrated by the examples above, can be stated roughly as follows:

4 KENNETH S. BROWN

Main theorem (Informal statement). The transition matrix of the walk on cham-
bers is diagonalizable, with one eigenvalue

λX = ∑

supp y≤X wy

for each X ∈ L. The multiplicity mX of this eigenvalue depends on combinatorial
data derived from S and L.

Unfortunately, the formula for mX is somewhat technical. See Theorem 1 in
Section 3 for the precise statement.

1.6. Stationary distribution and convergence rate. For the hyperplane cham-
ber walk, Brown and Diaconis [11] describe the stationary distribution and estimate
the rate of convergence to stationarity. These results and their proofs apply with-
out change to the present setup. For completeness, we state the results here. Note
ﬁrst that we can run, along with our walk on the chambers, a random walk on S
starting at the identity; after m steps it is at xm · · · x2x1, where x1, x2, . . . are i.i.d.
with distribution {wx}. If S is generated by {x ∈ S : wx ̸= 0}, then this walk is
eventually in C with probability 1. Let T be the ﬁrst time m that xm · · · x2x1 ∈ C.

Theorem 0. Let S be a ﬁnite LRB with identity, and let L be the associated
lattice. Let {wx} be a probability distribution on S such that S is generated by
{x ∈ S : wx ̸= 0}. Then the random walk on the ideal C of chambers has a unique
stationary distribution π; it is the distribution of the inﬁnite product c = x1x2 · · · ,
where x1, x2, . . . are i.i.d. with distribution {wx}. The total variation distance from
stationarity after m steps for the walk started at any chamber c0 satisﬁes

∥P m
c0 − π∥ ≤ Pr{T > m} ≤ ∑

H λ
m
H ,

where H ranges over the maximal elements (co-atoms) of L.

The fact that the inﬁnite product converges (i.e., that the partial sums are even-
tually constant) is an immediate consequence of property (D). See [11, Section 3]
for other descriptions of π, involving sampling without replacement, that can be
obtained by making systematic use of (D).

1.7. Organization of the paper. We begin by restarting the theory of LRBs in
Section 2, adopting a deﬁnition slightly diﬀerent from (but equivalent to) the one
in Section 1.1. This allows us to get more quickly to the main ideas of the paper
without getting bogged down in semigroup theory. We can then give in Section 3
the precise statement of our main theorem, with the multiplicities mX spelled out.
We also give some easy examples in that section.
Sections 4, 5, and 6 contain more elaborate examples. Readers who wish to
proceed to the proof of the main theorem may skip ahead to Section 7. In Section 4
we consider a convex, open, polyhedral subset U ⊂ Rn, divided into chambers
by hyperplanes that cut across it. There is a random walk on these chambers,
generalizing the walk of Section 1.2. From a technical point of view, this is a fairly
trivial generalization; but it leads to new examples, including a random walk on the
maximal chains of any ﬁnite distributive lattice. An amusing special case of this is
the “kids walk”. Section 5 treats the q-analogue of the Tsetlin library mentioned
above. The multiplicities mX for this walk are the q-derangement numbers studied
by Wachs [36]. And Section 6 gives a matroid generalization of the Tsetlin library,

SEMIGROUPS, RINGS, AND MARKOV CHAINS 5

including both the Tsetlin library and its q-analogue. Applying the theory to
graphical matroids, we obtain a random walk on the edge-ordered spanning trees
of a graph, as well as a random walk that has a (speculative) connection with
phylogenetic trees.
In Section 7 we begin the proof of the main theorem. We ﬁnd the radical and
semisimple quotient of the semigroup algebra RS using ideas of Bidigare [5], and
from this we can read oﬀ the irreducible representations of S. The eigenvalue
formulas follow easily, but not the diagonalizability of the transition matrix.
Diagonalizability is deduced in Section 8 from a more precise result, asserting
that the subalgebra R[w] ⊆ RS generated by w = ∑x∈S wxx is split semisimple
(isomorphic to a direct product of copies of R). We use here a criterion that deserves
to be better known, involving the poles of the generating function for the powers
of w. As a byproduct of the proof, we obtain an explicit (though complicated)
formula for the primitive idempotents in R[w], and hence for the projections onto
the eigenspaces of P . Our methods are inspired by the work of Fill [18] on the
Tsetlin library, and some of our formulas may be essentially the same as unpublished
results of his. Finally, we specialize in Section 9 to the hyperplane face semigroup of
a reﬂection arrangement, and we give connections with Solomon’s descent algebra.
Here again we make crucial use of results of Bidigare [5].
There are three appendices that provide supplementary material. Appendix A
summarizes the facts about hyperplane arrangements that we use. This appendix
is not logically necessary, but it is cited in many examples and it provides the
motivation for several deﬁnitions that would otherwise seem quite strange. Appen-
dix B lays the foundations for the theory of LRBs; in particular, it is here that we
reconcile the deﬁnition given in Section 1.1 with the one in Section 2. Finally, in
Appendix C we discuss a generalization of the derangement numbers. These arise
naturally in connection with the matroid examples of Section 6.

Acknowledgments. This paper grew out of my joint work with Persi Diaco-
nis [11]. It is a pleasure to thank him for many conversations and probing questions,
from which I have beneﬁted enormously. I am also grateful to Swapneel Mahajan,
Richard Stanley, and Michelle Wachs for helping me with Appendix C. John Howie
provided helpful pointers to the semigroup literature. Finally, I would like to ac-
knowledge that, as is already evident, this paper owes a great debt to the work of
Bidigare [5].

Convention. For simplicity, all semigroups are assumed to be ﬁnite and to have
an identity, unless the contrary is stated explicitly.

2. Left-regular bands

Let S be a semigroup (ﬁnite, with identity). It is convenient to redeﬁne “LRB”
so that the lattice L, whose existence was asserted in Section 1.5, is built into
the deﬁnition. The interested reader can refer to Appendix B for a proof that
the present deﬁnition is equivalent to the one in Section 1.1, as well as for other
characterizations of LRBs.

2.1. Deﬁnition. We say that S is a LRB if there are a lattice L and a surjection
supp : S ։ L satisfying
 supp xy = supp x ∨ supp y(2)

6 KENNETH S. BROWN

and
 xy = x if supp y ≤ supp x.(3)

Here ∨ denotes the join operation (least upper bound) in L. It follows from these
axioms that every x ∈ S is idempotent (x
2 = x) and that S satisﬁes the identity

xyx = xy(4)

for all x, y ∈ S. Thus S has the deletion property (D) stated in Section 1.1.
The motivation for (2) and (3) comes from the theory of hyperplane arrangements
(Appendix A); this theory, then, provides a huge supply of examples, one of which
is discussed in detail in Section 2.3. Further examples have been given in Sections
1.3 and 1.4, and many more will be given in Sections 4, 5, and 6,

2.2. Partial order. If S is a LRB, we can deﬁne a partial order on S by setting

x ≤ y ⇐⇒ xy = y.(5)

(For motivation, see equation (33) in Appendix A.) This relation is reﬂexive because
every element of S is idempotent. And it is transitive because if xy = y and yz = z,
then xz = x(yz) = (xy)z = yz = z. To check antisymmetry, suppose x ≤ y and
y ≤ x. Then xy = y and yx = x, hence x = yx = (xy)x = xy = y, where the
second-to-last equality uses (4); so S is indeed a poset.
Note that left multiplication by x is a projection (idempotent operator) mapping
S onto S≥x = {y ∈ S : y ≥ x}. The latter is a LRB in its own right, the associated
lattice being the interval [X, ˆ1] in L, where X = supp x and ˆ1 is the largest element
of L. Note also that S≥x depends only on X, up to isomorphism. Indeed, if we
also have supp x
′ = X, then the projections (left multiplications) deﬁned by x and
x
′ give mutually inverse semigroup isomorphisms between S≥x and S≥x′; this is a
straightforward consequence of the axioms. We may therefore write S≥X instead
of S≥x. Thus
 S≥X ∼= {y ∈ S : y ≥ x}

for any ﬁxed x with supp x = X. Note that the random walk studied in this paper
is deﬁned in terms of the projection operators restricted to chambers, mapping C
onto C≥x. For the hyperplane face semigroup these projections have a geometric
meaning that we mentioned in Section 1.2.
Finally, we remark that there is also a LRB

S≤X = {y ∈ S : supp y ≤ X},

whose associated lattice is the interval [ˆ0, X], where ˆ0 is the smallest element of L.

2.3. Example: The semigroup of ordered partitions. One of the standard
examples of a hyperplane arrangement is the braid arrangement, which is discussed
in detail in [5, 6, 7, 11]; see also Section A.5 of the present paper. Its face semi-
group B is easy to describe combinatorially, without reference to hyperplane ar-
rangements: The elements of B are ordered partitions B = (B1, . . . , Bl) of the set
[n] = {1, 2, . . . , n}. Thus the Bi are nonempty sets that partition [n], and their order
matters. We multiply two ordered partitions by taking intersections and ordering
them lexicographically; more precisely, if B = (B1, . . . , Bl) and C = (C1, . . . , Cm),
then
 BC = (B1 ∩ C1, . . . , B1 ∩ Cm, . . . , Bl ∩ C1, . . . , Bl ∩ Cm)̂,

SEMIGROUPS, RINGS, AND MARKOV CHAINS 7

where the hat means “delete empty intersections”. This product makes B a LRB,
with the 1-block ordered partition as identity. The associated lattice L is the lattice
of unordered set partitions Π, with Π ≤ Π
′ if Π
′ is a reﬁnement of Π. Thus the
smallest element ˆ0 of L is the 1-block partition, and the largest element ˆ1 is the
partition into singletons. The support map B ։ L forgets the ordering of the
blocks.
The partial order on B is also given by reﬁnement, taking account of the block
ordering. Thus B ≤ C if and only if C consists of an ordered partition of B1
followed by an ordered partition of B2, and so on. The chambers are the ordered
partitions into singletons, so they correspond to the permutations of [n].
It is useful to have a second description of B. Ordered partitions (B1, . . . , Bl)
of [n] are in 1–1 correspondence with chains of subsets ∅ = E0 < E1 < · · · < El =
[n], the correspondence being given by Bi = Ei − Ei−1. So we may identify B
with the set of such chains. The product is then described as follows: Given a
chain E as above and a second chain F : ∅ = F0 < F1 < · · · < Fm = [n], their
product EF is obtained by using F to reﬁne E. More precisely, consider the sets
Gij = (Ei−1 ∪ Fj ) ∩ Ei = Ei−1 ∪ (Fj ∩ Ei). For each i = 1, 2, . . . , l we have

Ei−1 = Gi0 ⊆ Gi1 ⊆ · · · ⊆ Gim = Ei.

Deleting repetitions gives a chain from Ei−1 to Ei, and combining these for all i
gives the desired reﬁnement EF of E.
This construction is used in one of the standard proofs of the Jordan–H¨older
theorem.
 3. Statement of the main theorem

We are now in a position to complete the statement of our main result by spelling
out the multiplicities mX mentioned in Section 1.5. Let S be a LRB with lattice
of supports L. For each X ∈ L let cX be the number of chambers in S≥X , i.e.,
the number of chambers c ∈ C such that c ≥ x, where x is any ﬁxed element of S
having support X. Our main theorem is:

Theorem 1. Let S be a ﬁnite LRB with identity, let {wx} be a probability distri-
bution on S, and let P be the transition matrix of the random walk on chambers:

P (c, d) = ∑

xc=d wx(6)

for c, d ∈ C. Then P is diagonalizable. It has an eigenvalue

λX = ∑

supp y≤X wy

for each X ∈ L, with multiplicity mX , where
∑

Y ≥X mY = cX(7)

for each X ∈ L. Equivalently,

mX = ∑

Y ≥X µ(X, Y )cY ,(8)

where µ is the M¨obius function of the lattice L.

8 KENNETH S. BROWN

Note that mX depends only on the semigroup S≥X . With this in mind, there is
an easy way to remember the formula (7). It says that for the random walk gener-
ated by any set of weights on S≥X , the sum of the multiplicities of the eigenvalues
is equal to the number of chambers.
Here are a few easy examples. More complicated examples will be discussed in
Sections 4, 5, and 6.

Example 1. Consider the chamber walk associated with a central hyperplane ar-
rangement in a vector space V . We have cX = ∑
Y ≥X |µ(Y, V )| by Zaslavsky [39].
Comparing this with (7), we conclude that mX = |µ(X, V )|. Thus Theorem 1
gives the results cited in Section 1.2. The same results remain valid for noncen-
tral arrangements. This was already shown in [11] by diﬀerent methods. To see
how it follows from Theorem 1, one argues exactly as in the central case, with one
complication: The face semigroup F need not have an identity, and the poset L
of supports of the faces is only a semilattice (it has least upper bounds but not
necessarily greatest lower bounds). Before applying the theorem, one has to adjoin
an identity to F to get a LRB ˆF with identity, and one has to adjoin a smallest
element ˆ0 to L to get a lattice ˆL. The theorem would seem, then, to give an extra
eigenvalue λˆ0 = 0. But Zaslavsky [39] showed that cˆ0, the total number of cham-
bers, is ∑
Y ∈L|µ(Y, V )|. One can now deduce from (7) that mˆ0 = 0 and hence that
λˆ0 does not really occur as an eigenvalue.

Example 2. Let S = Fn. As we stated in Section 1.3, mX is the derangement
number dn−|X| for any X ⊆ [n]. To deduce this from Theorem 1, we need only
observe that ∑

Y ⊇X dn−|Y | = cX(9)

for each X ⊆ [n]. Indeed, one can check that cX = (n − |X|)!, which is the number
of permutations of [n] that ﬁx X pointwise; and the left-hand-side of (9) counts
these according to their ﬁxed-point sets.

Example 3. Let S = Fn,q. We claimed in Section 1.4 that mX for a subspace
X ⊆ Fn
q is the number of elements of GLn(Fq) with X as ﬁxed subspace. To see
this, note that cX is the number of ways to extend a given ordered basis of X to
an ordered basis of Fn
q . This is also the number of elements of GLn(Fq) that ﬁx X
pointwise, and the claim now follows from (7) exactly as in Example 2.

4. Examples: Convex sets, distributive lattices, and the kids walk

The examples in this section were ﬁrst treated in unpublished joint work with
Persi Diaconis, using the techniques of [11] rather than semigroup methods.
Let U ⊂ Rn be a nonempty set that is a ﬁnite intersection of open halfspaces. A
ﬁnite set of hyperplanes cutting across U divides U into regions. We are interested
in a random walk on these regions driven by a set of weights on their faces. A
convenient way to set this up is to combine the hyperplanes deﬁning U with the
hyperplanes cutting across U ; this yields a hyperplane arrangement A, and the
regions into which U is cut form a subset D of the set C of chambers of A. Section 4.1
spells out this point of view in more detail. We then construct and analyze a
random walk on D in Section 4.2. We show in Section 4.3 how the theory yields a

SEMIGROUPS, RINGS, AND MARKOV CHAINS 9

random walk on the maximal chains of a distributive lattice, and we illustrate this
in Section 4.4 by discussing the “kids walk”.

4.1. Convex sets of chambers. Let A = {Hi}i∈I be a hyperplane arrangement
in a real vector space V , let F be its face semigroup, and let C be the ideal of
chambers. We do not assume that A is central, so F need not have an identity.
Let D ⊆ C be a convex set of chambers, as deﬁned in Section A.7. Thus there is a
subset J ⊆ I and a set of signs σi ∈ {+, −} (i ∈ J) such that

D = {C ∈ C : σi(C) = σi for all i ∈ J}.

We may assume that each σi = +. The open set U referred to above is then⋂

i∈J H +
i .
As a simple example, consider the braid arrangement in R4 (Section A.5). The
region U deﬁned by x1 > x2 and x3 > x4 contains six chambers, corresponding to
the permutations 1234, 1324, 1342, 3124, 3142, 3412. As explained in Section A.6,
it is possible to represent the arrangement by means of a picture on the 2-sphere.
In this picture (Figure 7 in Section A.6) U corresponds to one of the open lunes
determined by the great circles 1-2 and 3-4. Figure 1 gives a better view of this
lune.
 1234 1324 3142 3412

1-4

3-4

1-2
 2-31-3 2-4

3124

Figure 1. A convex subset of the braid arrangement.

4.2. A walk on the chambers. Let G be the set of faces of the chambers D ∈ D;
equivalently,
 G = {G ∈ F : σi(G) ≥ 0 for all i ∈ J}.

(To see that the right side is contained in the left, suppose σi(G) ≥ 0 for all i ∈ J.
Choose an arbitrary D ∈ D. Then we have G ≤ GD ∈ D, hence G ∈ G.) Then G
is a subsemigroup of F , hence a LRB (possibly without identity) in its own right.
Its set of chambers is D. Thus we can run a random walk on D driven by a set of
weights on G. To describe the eigenvalues, we need some further notation.
Let G0 = {G ∈ G : σi(G) = +}. In other words, G0 is the set of faces that
are contained in our open set U = ⋂
i∈J H +
i . Let L be the intersection semilattice
of A, let M ⊆ L be the set of supports of the faces in G, and let M0 ⊆ M be the
set of supports of the faces in G0. Equivalently, M0 consists of the X ∈ L that
intersect U . In our braid arrangement example, where we identify F with the set

10 KENNETH S. BROWN

of cells in the spherical representation of the arrangement, G0 consists of the cells
in the interior of the lune: one vertex, six edges, and six chambers. The bigger
semigroup G contains, in addition, the six vertices and six edges on the boundary
of the lune, as well as the empty cell (which is the identity of G). The poset M0 is
shown in Figure 2.
 ✚
✚
✚
✚
✚
✚
✚✚❩
❩
❩
❩
❩
❩
❩❩

✁
✁
✁
✁
✁✁
 ❆❆
❆❆
❆❆

❆❆
❆❆
❆❆
 ✁
✁
✁
✁
✁✁

H14
 V

H13 H24 H23

H13 ∩ H24

Figure 2. The poset M0.

Note that if X ∈ M0 and X ≤ Y ∈ L, then Y ∈ M0; this implies that we get
the same value for the M¨obius number µ(X, V ) for X ∈ M0 no matter which of
the posets M0, M, L we work in. We can now state:

Theorem 2. Let A be a hyperplane arrangement and let G, D, and M0 be as
above. For any probability distribution {wG}G∈G on G, the transition matrix of the
random walk on D is diagonalizable. It has an eigenvalue

λX = ∑

G∈G
G⊆X
 wG

for each X ∈ M0, with multiplicity |µ(X, V )|.

Proof. We argue as in our discussion of the walk on C in Example 1 of Section 3.
Assume ﬁrst that A is central, so that G has an identity. The lattice associated
with G is M, so Theorem 1 gives us an eigenvalue λX as above for each X ∈ M,
with multiplicities mX characterized by
∑

Y ∈M
Y ⊇X
 mY = cX(10)

for each X ∈ M, where cX is the number of chambers in GX . We wish to show
that mX = |µ(X, V )| for X ∈ M0 and that mX = 0 for X /∈ M0. This will follow
from (10) if we show ∑

Y ∈M0
Y ⊇X
 |µ(Y, V )| = cX(11)

for each X ∈ M.
Now Zaslavsky [40] counted the number of regions obtained when an open convex
set is cut by hyperplanes (see his Theorem 3.2 and the comments at the bottom of
p. 275). His result, in our notation, is

|D| = ∑

Y ∈M0|µ(Y, V )|.(12)
 SEMIGROUPS, RINGS, AND MARKOV CHAINS 11

This is the case X = ˆ0 of (11). Equation (11) for arbitrary X can be obtained by
applying (12) with A replaced by the set of hyperplanes H ∈ A that contain X.
Theorem 2 is now proved if A is central.
The noncentral case is treated by adjoining an identity to G, as in Example 1
of Section 3. The essential point is that (12) still holds, and this implies that the
“extra” eigenvalue λˆ0 = 0 has multiplicity 0.

To illustrate the theorem, we return to the convex set in Figure 1, with M0 as
in Figure 2. We have µ(X, V ) = ±1 for each X ∈ M0, so each contributes an
eigenvalue of multiplicity 1. Suppose, for example, that we take uniform weights
wG = 1/7 on the seven vertices in Figure 1. Then Theorem 2 gives the following
eigenvalues:
 X λX
V 1

H13, H24 3/7
H14, H23 2/7

H13 ∩ H24 1/7

The transition matrix P in this case is 1/7 of the following matrix:

1234 1324 1342 3124 3142 3412
1234 3 1 1 1 0 1
1324 1 3 1 1 0 1
1342 1 1 3 0 1 1
3124 1 1 0 3 1 1
3142 1 0 1 1 3 1
3412 1 0 1 1 1 3

4.3. Distributive lattices. If L is a ﬁnite distributive lattice, there is a LRB S
whose elements are chains ˆ0 = x0 < x1 < · · · < xl = ˆ1. To construct the product
of two such chains, we use the second factor to reﬁne the ﬁrst, exactly as in the
discussion at the end of Section 2.3, where we treated the Boolean lattice of subsets
of [n]. A simple way to verify that S is indeed a LRB is to appeal to the well-
known fact that L can be embedded as a sublattice of a Boolean lattice. Moreover,
Abels [1, Proposition 2.5] has described a way of constructing an embedding which
makes the set of chambers in S (i.e., the maximal chains in L) correspond to a
convex set of chambers in the braid arrangement. His embedding depends on a
choice of a “fundamental” maximal chain, which then corresponds to the identity
permutation. We can therefore use the results of Section 4.2 to analyze a random
walk on the maximal chains of L, driven by weights on arbitrary chains.
As an example of a distributive lattice, consider the product {0, 1, . . . , p} ×
{0, 1, . . . , q} of a chain of length p by a chain of length q. The case p = q = 2
is shown in Figure 3(a). The maximal chains are the lattice paths from (0, 0)
to (p, q), as in Figure 3(b). Each maximal chain has length p + q, and there are(
p+q
p ) of them; indeed, a lattice path can be identiﬁed with a binary vector of length
p + q containing exactly p ones. (Think of 1 as “right” and 0 as “up”.)
One interesting random walk on these lattice paths is obtained by assigning
uniform weights to the (p + 1)(q + 1) − 2 chains of the form ˆ0 < x < ˆ1. A step
in the walk consists of choosing x ∈ L − {ˆ0, ˆ1} at random and then modifying the

12 KENNETH S. BROWN

(a) (b)

Figure 3. (a) A distributive lattice. (b) A maximal chain.

given path minimally to make it pass through x. See Figure 4 for an illustration;
here x = (2, 1).
 Figure 4. A step in the walk on lattice paths.

In case p = q = 2, the method of Abels cited above leads to an embedding of
L = {0, 1, 2} × {0, 1, 2} into the Boolean lattice of rank 4. One such embedding is
shown in Figure 5; it is obtained by taking the fundamental maximal chain in L to
be the lattice path that goes up the left side and then across the top. (Note: An
expression like 134 in Figure 5 denotes the set {1, 3, 4}.) The six maximal chains
correspond to the six permutations shown in Figure 1, and the walk on lattice paths
is the same as the walk discussed at the end of Section 4.2.

12 123 1234
| | |
1 13 134
| | |
∅ 3 34

Figure 5. Embedding in the Boolean lattice.

One can treat general p, q in a similar way, but it would take us too far aﬁeld to
give further details. One can also obtain results on the stationary distribution and
convergence rate via Theorem 0 (Section 1.6).

4.4. The kids walk. This is a walk on the p-subsets of a (p + q)-set, represented
as binary vectors of length p + q containing p ones. Think of the zeroes as empty
spaces and the ones as spaces occupied by kids. At each step a kid and an empty
space are independently chosen at random. The kid then moves toward the empty
space, pushing any other kids he encounters until the space is occupied. Here is an
example with p = 3 and q = 4. The initial conﬁguration is

↓ ↓
0 1 1 0 0 1 0

with the two chosen positions indicated by arrows. The ﬁnal conﬁguration is

0 0 0 1 1 1 0

SEMIGROUPS, RINGS, AND MARKOV CHAINS 13

The kids walk is the same as the walk on lattice paths described in Section 4.3,
except that the latter has holding; namely, the chosen lattice point x is on the
current path with probability α = (p+ q − 1)/(pq + p+ q − 1), in which case the walk
stays at the current path. Thus if P is the transition matrix for the walk on lattice
paths and P1 is the transition matrix for the kids walk, we have P = αI +(1−α)P1,
so that P1 = (P − αI)/(1 − α). It follows that P1 is diagonalizable with eigenvalues
(λ − α)/(1 − α), where λ ranges over the eigenvalues of P . If p = q = 2, for
example, we have α = 3/7, and the result at the end of Section 4.2 gives eigenvalues
1, 0, 0, −1/4, −1/4, −1/2 for the kids walk.

5. Example: A q-analogue of the Tsetlin library

The random walk in this section is based on a quotient ¯Fn,q of the semigroup Fn,q
(Section 1.4). For motivation, we begin by deﬁning a quotient ¯Fn of Fn, and we
explain how it is related to the Tsetlin library. The q-analogue is then given in
Section 5.2.

5.1. A quotient of Fn. The references cited in Section 2.3 show how the random
walk associated with the semigroup B of ordered partitions captures many shuﬄing
schemes. In particular, to obtain the Tsetlin library one puts weight wi > 0 on the 2-
block ordered partition (i, [n]−i) and weight 0 on all other ordered partitions, where∑n
i=1 wi = 1. From the point of view of the present paper, however, the semigroup
B is much too big for the study of the Tsetlin library; one should replace B by the
subsemigroup (with identity) generated by the n two-block ordered partitions to
which we have assigned weights. This subsemigroup, which we denote by ¯Fn, is
easily described: It consists of the ordered partitions (B1, . . . , Bl) such that each
block Bi is a singleton except possibly Bl. Alternatively, it consists of the chains
∅ = E0 < E1 < · · · < El = [n] with |Ei| = i for 0 ≤ i < l.
The freeness of Fn implies that ¯Fn is a quotient of Fn. Explicitly we have
a surjection Fn ։ ¯Fn sending the sequence (x1, . . . , xl) to the following ordered
partition B: If l < n, then B has l + 1 blocks, with Bi = {xi} if i ≤ l and
Bl+1 = [n]− {x1, . . . , xl}; if l = n, then B is the partition into singletons Bi = {xi},
1 ≤ i ≤ n. In terms of chains of subsets, B corresponds to the chain E with
Ei = {x1, . . . , xi} for 1 ≤ i ≤ l and, if l < n, El+1 = [n].
The lattice of supports of ¯Fn can be identiﬁed with the set of subsets X ⊆ [n]
such that |X| ̸= n − 1, the support of B being the union of the singleton blocks.
Note that the quotient map Fn ։ ¯Fn is almost 1–1; the only identiﬁcations are that
each (n − 1)-tuple (x1, . . . , xn−1) in Fn gets identiﬁed with its (unique) extension
to an n-tuple in Fn.

Remark. The semigroups Fn and ¯Fn have the same set of chambers, and we have
seen that either one can be used to generate the Tsetlin library. But ¯Fn is more
eﬃcient for this purpose, in the following two senses: (a) When we use Fn, Theo-
rem 1 gives extraneous eigenvalues λX with |X| = n − 1, which then turn out not to
occur because mX = 0. (b) The estimate of convergence rate given in Theorem 0
is sharper if we use ¯Fn than if we use Fn, because the maximal elements of the
support lattice have size n − 2 instead of n − 1.

5.2. q-analogue. Let V be the vector space Fn
q , where Fq is the ﬁeld with q ele-
ments. As a q-analogue of ¯Fn we propose the following semigroup ¯Fn,q: An element
of ¯Fn,q is a chain of subspaces 0 = X0 < X1 < · · · < Xl = V with dim Xi = i for

14 KENNETH S. BROWN

i < l. Thus the chain cannot be reﬁned except possibly at the last step, between
Xl−1 and V . Given two such chains X = (X0, . . . , Xl) and Y = (Y0, . . . , Ym), we
construct the product XY by using Y to reﬁne X. More precisely, the product is
obtained by forming the chain

0 = X0 < · · · < Xl−1 ≤ Xl−1 + Y1 ≤ Xl−1 + Y2 ≤ · · · ≤ Xl−1 + Ym = V

and deleting repetitions.
The simplest way to verify that this product is associative is to exhibit ¯Fn,q as
a quotient of the semigroup Fn,q of ordered independent sets. Namely, we can map
Fn,q onto ¯Fn,q by sending (x1, . . . , xl) to the chain with Xi equal to the span of
{x1, . . . , xi} for 0 ≤ i ≤ l and, if l < n, Xl+1 = V . This gives a product-preserving
surjection Fn,q ։ ¯Fn,q, so our product on ¯Fn,q is indeed associative.
It is easy to check that ¯Fn,q is a LRB whose associated lattice is the set of
subspaces of V of dimension diﬀerent from n − 1. The support map is given by

supp(X0, . . . , Xl) =
 {Xl−1 if l < n
V if l = n.

Note that the join of two such subspaces X, Y in this lattice is their vector space
sum X + Y unless the latter has dimension n − 1, in which case the join is V .
The chambers in ¯Fn,q are the maximal chains 0 = X0 < X1 < · · · < Xn = V .
To construct a random walk analogous to the Tsetlin library, put weight wℓ > 0
on the chain 0 < ℓ < V for each subspace ℓ of dimension 1, and put weight 0 on
all other elements of ¯Fn,q, where ∑
ℓ wℓ = 1. This yields a walk on maximal chains
that goes as follows: Given a maximal chain

0 < X1 < · · · < Xn−1 < V,

pick a line ℓ with probability wℓ, and form a new maximal chain

0 < ℓ ≤ ℓ + X1 ≤ · · · ≤ ℓ + Xn−1 ≤ V ;

exactly one of the inequalities is an equality, and we delete the repetition. One can
also view this walk as taking place on the maximal ﬂags in the projective space
Pn−1(Fq), driven by weights on the points. If n = 3, for example, this is a walk on
the incident point-line pairs in the projective plane.
According to Theorem 1 the transition matrix of this walk is diagonalizable, with
an eigenvalue
 λX = ∑

ℓ⊆X wℓ

for each subspace X with dim X ̸= n − 1; the multiplicities mX are characterized
by ∑

Y ⊇X mY = cX ,

where cX is the number of maximal chains in the interval [X, V ] in L. It follows
that mX is the q-derangement number dn−dim X (q) of Wachs [36]; see Example 2
in Section C.2. This is why we view the present walk as the “right” q-analogue of
the Tsetlin library, rather than the walk based on Fn,q.
The stationary distribution π of this walk is a probability measure on the set of
maximal chains. One can deduce from Theorem 0 the following description of π:
Sample from the set of lines ℓ according to the weights wℓ to get a line l1. Remove

SEMIGROUPS, RINGS, AND MARKOV CHAINS 15

ℓ1 and sample again to get ℓ2. Remove all the lines contained in ℓ1 + ℓ2 and choose
ℓ3. Continuing in this way, we obtain a maximal chain

0 < ℓ1 < ℓ1 + ℓ2 < · · · < ℓ1 + ℓ2 + · · · + ℓn−1 < V

after n − 1 steps. This chain is distributed according to π.

Remark. This q-analogue of the Tsetlin library was ﬁrst studied in joint work with
Persi Diaconis [unpublished], in which we extended the hyperplane chamber walks
to walks on the chambers of a building. And the ﬁrst proof that the multipli-
cities were given by the q-derangement numbers was arrived at with the help of
Richard Stanley. In fact, the original calculation of the multiplicities, which was
quite diﬀerent from the one given in this paper, led to formulas similar to those
of Proposition 10 (Section C.1), and it was not immediately obvious that these
formulas gave the q-derangement numbers.

6. Examples: Random walks associated with matroids

Matroids were introduced by Whitney [38], as an abstraction of the linear inde-
pendence properties of the columns of a matrix. We describe in this section two
natural LRBs S, ¯S that can be associated with a matroid, hence two random walks.
These generalize the pairs Fn, ¯Fn and Fn,q, ¯Fn,q discussed in Section 5.
We begin by reviewing matroid concepts in Section 6.1. We then construct
the semigroups and the associated walks in Section 6.2. Our discussion is brief
because the theory follows quite closely the two special cases already treated. In
Section 6.3 we consider a third case, graphical matroids. This leads to two random
walks associated with a graph. In an eﬀort to understand one of these examples
intuitively, we give an interpretation of it in terms of phylogenetic trees.

6.1. Review of matroids. The book by Welsh [37] is a good reference for this
subsection. A matroid M consists of a ﬁnite set E and a collection of subsets
of E, called independent sets, subject to axioms modeled on the notion of linear
independence in vector spaces. A maximal independent set is called a basis, and
all such have the same cardinality n, called the rank of M . More generally one can
deﬁne rank(A) for any subset A ⊆ E as the rank of any maximal independent set
in A. Any such maximal independent set is called a basis for A. We say that x
depends on A if rank(A ∪ x) = rank(A); otherwise, rank(A ∪ x) = rank(A) + 1. Any
set A has a closure σ(A), obtained by adjoining every x that depends on A, and
A is said to be closed, or a ﬂat, if σ(A) = A. The set L of ﬂats is a lattice under
inclusion. One can think of L as an analogue of the lattice of subspaces of a vector
space, and σ(A) plays the role of the span of a set of vectors.
In addition to the motivating example, in which E is a set of vectors, there are
two other canonical examples: The ﬁrst is the free matroid of rank n; the set E is
{1, 2, . . . , n}, and all subsets are independent. The second is the graphical matroid
associated with a ﬁnite graph G; here E is the set of edges of G, and a subset is
independent if it contains no cycles.

6.2. Semigroups associated with a matroid. Let M be a matroid of rank
n with underlying set E. We construct two LRBs S, ¯S. The elements of S are
ordered independent sets, i.e., l-tuples x = (x1, . . . , xl) of distinct elements of E

16 KENNETH S. BROWN

whose underlying set {x1, . . . , xl} is independent. We set supp x = σ({x1, . . . , xl}).
The product is deﬁned by

(x1, . . . , xl)(y1, . . . , ym) = (x1, . . . , xl, y1, . . . , ym)̂,

where the hat means “delete any element that depends on the earlier elements”. It
is easy to check that we obtain in this way a LRB S whose associated lattice is the
lattice of ﬂats L.
The chambers of S are the ordered bases of M . To construct a random walk
analogous to the Tsetlin library, put weight wx > 0 on the 1-tuple (x) and weight
0 on the l-tuples with l ̸= 1, where ∑x wx = 1. (Note: Not all x ∈ E occur here,
since M might contain loops, i.e., elements x such that the singleton {x} is not
independent.) This yields a walk on ordered bases that goes as follows: Given an
ordered basis (x1, . . . , xn), pick a nonloop x ∈ E with probability wx, and make it
the new ﬁrst basis element; delete the (unique) xi that depends on {x, x1, . . . , xi−1}.
According to Theorem 1, the transition matrix of this walk is diagonalizable,
with an eigenvalue
 λX = ∑

x∈X wx

for each ﬂat X; the multiplicities mX are characterized by
∑

Y ≥X mY = cX(13)

for each X ∈ L. Here cX is the number of ways of completing any ﬁxed basis
of X to a basis of M . The stationary distribution π of this chain is a probability
measure on the set of ordered bases. One can deduce from Theorem 0 the following
description of π: Sample from E (according to the weights wx) to get a nonloop x1.
Remove x1 and everything dependent on it and sample again to get x2. Remove
the closure of {x1, x2}, choose x3, and so on. After n steps we have an ordered
basis (x1, . . . , xn) whose distribution is π.
The second semigroup, ¯S, consists of chains of ﬂats ˆ0 = X0 < X1 < · · · < Xl = ˆ1
with rank(Xi) = i for i < l. Given two such chains X = (X0, . . . , Xl) and Y =
(Y0, . . . , Ym), their product XY is obtained by forming the chain

ˆ0 = X0 < · · · < Xl−1 ≤ Xl−1 ∨ Y1 ≤ · · · ≤ Xl−1 ∨ Ym = ˆ1

and deleting repetitions. Here ∨ denotes the join operation in the lattice of ﬂats,
i.e., X ∨ Y = σ(X ∪ Y ). One can verify, exactly as in Section 5.2, that ¯S is a LRB
whose associated lattice ¯L is the set of ﬂats of rank diﬀerent from n − 1.
The chambers in ¯S are the maximal chains ˆ0 = X0 < X1 < · · · < Xn = ˆ1. To
construct a random walk analogous to the Tsetlin library, put weight wℓ > 0 on
the chain ˆ0 < ℓ < ˆ1 for each ﬂat ℓ of rank 1, where ∑ℓ wℓ = 1. This yields a walk
on maximal chains that goes as follows: Given a maximal chain

ˆ0 < X1 < · · · < Xn−1 < ˆ1,

pick a ﬂat ℓ of rank 1 with probability wℓ, and form a new maximal chain

ˆ0 < ℓ ≤ ℓ ∨ X1 ≤ · · · ≤ ℓ ∨ Xn−1 ≤ ˆ1;

exactly one of the inequalities is an equality, and we delete the repetition.

SEMIGROUPS, RINGS, AND MARKOV CHAINS 17

According to Theorem 1, the transition matrix of this walk is diagonalizable,
with an eigenvalue
 λX = ∑

ℓ≤X wℓ

for each ﬂat X with rank(X) ̸= n − 1; the multiplicities mX are characterized by
∑

Y ≥X mY = cX(14)

where now cX is the number of maximal chains in the interval [X, ˆ1] in L.
Recall that the multiplicities of the eigenvalues for the Tsetlin library and its
q-analogue are the derangement numbers and their q-analogues. Motivated by this,
we show in Appendix C how to associate a “generalized derangement number”
d(L) to every ﬁnite lattice L. It will follow quickly from the deﬁnition that the
multiplicities in (14) are given by

mX = d (
[X, ˆ1]) ;(15)

see equation (41) and the discussion following it.
The stationary distribution π of this chain is a probability measure on the set of
maximal chains. One can deduce from Theorem 0 the following description of π:
Sample from the set of “lines” (rank 1 ﬂats) according to the weights wℓ to get a
line l1. Remove ℓ1 and sample again to get ℓ2. Remove all the lines contained in
ℓ1 ∨ ℓ2 and choose ℓ3, and so on. After n − 1 steps we have a maximal chain

ˆ0 < ℓ1 < ℓ1 ∨ ℓ2 < · · · < ℓ1 ∨ ℓ2 ∨ · · · ∨ ℓn−1 < ˆ1,

which is distributed according to π.

6.3. Random walks associated with graphs. One of Whitney’s main motiva-
tions in developing the theory of matroids was the connection with graph theory.
As we mentioned in Section 6.1, every ﬁnite graph G gives rise to a matroid whose
underlying set E is the set of edges of G, with a set of edges being independent
if it contains no cycles. Equivalently, the independent sets correspond to forests
F ⊆ G, where we make the convention that a forest contains every vertex of G.
We brieﬂy describe here our two random walks, as specialized to the matroid of G.
Much remains to be understood about these examples.
For simplicity, all of our graphs are assumed simple (no loops or multiple edges).
The lattice of ﬂats L = L(G) of the graphical matroid can then be described as
follows. An element of L is speciﬁed by a partition Π of the vertex set V of G
such that each block induces a connected subgraph. The ordering on L is given by
reﬁnement, but with the opposite convention from the one used in Section 2.3: In
L(G), Π ≤ Π
′ if Π is a reﬁnement of Π
′. Thus going up in the lattice corresponds to
merging blocks. Associated with each Π ∈ L is the contraction ¯G = G/Π, obtained
by collapsing each block to a point and making the resulting graph simple. (Delete
loops and replace multiple edges by a single edge.) Equivalently, G/Π is the simple
graph with one vertex for each block, two blocks B, B′ being adjacent if, in G,
some vertex in B is adjacent to some vertex in B′. Because of this interpretation
of partitions, L(G) is often called the lattice of contractions of G. The smallest
element ˆ0 is the partition into singletons (so ¯G = G), and the largest element ˆ1 is
the partition into connected components (so ¯G is the discrete graph with one vertex

18 KENNETH S. BROWN

for each connected component of G). From the collapsing point of view, going up
in the lattice L(G) corresponds to doing further collapsing.
Consider now the two semigroups S, ¯S associated with the graphical matroid.
An element of S can be identiﬁed with an edge-ordered forest F ⊆ G, i.e., a forest
together with a linear ordering of its edges. The support of F is the partition of V
given by the connected components of F . In particular, the chambers of S are the
edge-ordered spanning forests of G (spanning trees if G is connected). The random
walk on these chambers goes as follows: Given a spanning forest with ordered edges
e1, . . . , en, pick an edge e with probability we and make it the new ﬁrst edge; delete
the ﬁrst ei such that {e, e1, . . . , ei} contains a cycle.
We leave it to interested reader to spell out what the general results in Section 6.2
say about this example. One interesting question arises: Running this random walk,
say with uniform weights, gives a way of choosing an edge-ordered spanning forest
with distribution π; what is the distribution of the spanning forest obtained by
forgetting the ordering?
We turn next to the random walk on maximal ﬂags, based on the semigroup ¯S.
A maximal ﬂag in L(G) is gotten by collapsing an edge of G to get a (simple)
graph G1, then collapsing an edge of G1 to get G2, and so on, until we reach a
discrete graph Gn. The number n of collapses is the number of edges in a span-
ning forest of G, i.e., the number of vertices of G minus the number of connected
components. Note that an edge-ordered spanning forest determines a collapsing se-
quence (maximal ﬂag), but this correspondence is not 1–1. Diﬀerent edge-ordered
spanning forests can give the same maximal ﬂag, just as diﬀerent ordered bases of
a vector space can determine the same maximal ﬂag of subspaces.
We close this section by giving an interpretation of these maximal ﬂags and the
corresponding random walk in terms of phylogenetic trees. Think of the vertices
of G as species that exist today. We join two species by an edge if we think they
might have had a direct common ancestor. Thus humans and chimpanzees are
probably adjacent, but not humans and frogs. Assume, for simplicity, that G is
connected, so that all species ultimately evolved from one common ancestor. To
run the random walk, we are given weights on the edges. These can be thought
of as indicating the strength of our belief that two species have a direct common
ancestor; alternatively, they might indicate how recently we think they diverged
from that ancestor.
Recall that a maximal ﬂag in L(G) consists of a sequence of edge collapses

G = G0 ։ G1 ։ · · · ։ Gn = point.

We can think of this as representing a feasible reconstruction of the phylogenetic
tree describing the evolution from the original common ancestor to the present-day
situation, in reverse chronological order. Thus the ﬁrst edge collapsed corresponds
to the two species that most recently split oﬀ from a direct common ancestor. The
collapsed graph G1 then represents the situation before that split. The edge of G1
that is collapsed to form G2 corresponds to the next-most-recent split, and so on.
The random walk proceeds as follows: Given a collapsing sequence as above, pick
a random edge e of G according to the weights. Make a new collapsing sequence
in which e is collapsed ﬁrst, but after that the collapses mimic those of the original
sequence. In other words, we revise our view of the evolutionary history by declaring
that two particular species were the most recent to split from a common direct
ancestor.
 SEMIGROUPS, RINGS, AND MARKOV CHAINS 19

A pick from the stationary distribution of this walk can, as usual, be obtained
by sampling without replacement. In the present situation this amounts to the
following: Pick an edge of G according to the weights and collapse it to get G1.
Use the collapsing map G ։ G1 to put weights on the edges of G1; thus the weight
on an edge of G1 is the sum of weights of the edges of G that map to that edge.
Note that the weights on G1 do not sum to 1, because at least one edge of G with
positive weight gets collapsed to a point in G1; so we must rescale them. Now
repeat the process: Choose an edge of G1 according to the weights and collapse it
to get G2. Continue in this way until a maximal collapsing sequence is obtained.

Remark. See Aldous [2] for a detailed analysis of this walk in the case of uniform
weights.

7. Irreducible representations and computation of eigenvalues

We now begin the proof of Theorem 1, starting with the description of the
eigenvalues. Throughout this section S denotes a LRB (ﬁnite, with identity), and
supp : S ։ L is the associated support map. Assume that we are given a proba-
bility distribution {wx} on S and that P is the transition matrix of the random
walk on chambers. We begin by recalling in Section 7.1 the algebraic interpre-
tation of P in terms of the semigroup algebra of S. In Section 7.2 we compute
the radical and semisimple quotient of the semigroup algebra. This was done by
Bidigare [5] for hyperplane face semigroups, and the proof in general is identical.
We include the proof for the convenience of the reader, since the thesis [5] is not
readily available. From this result we can read oﬀ the irreducible representations
of S, and the eigenvalue formula stated in Theorem 1 follows at once; we explain
this in Section 7.3.

7.1. Algebraic formulation. It is well-known to probabilists that the transition
matrix of a random walk on a semigroup can be interpreted as the matrix of a con-
volution operator. (This is perhaps best known for groups, but the result remains
valid for semigroups.) We wish to recast this result in ring-theoretic language.
Consider the vector space RS of formal linear combinations ∑x∈S axx of elements
of S, with ax ∈ R. The product on S extends to a bilinear product on RS, making
the latter a ring (the semigroup ring of S over R). Thus
(∑

x∈S axx

) (∑

x∈S bxx

)
 = ∑

x∈S cxx,

where
 cx = ∑

yz=x aybz.

On the level of coeﬃcients, this is the familiar convolution product.
A probability distribution {wx}x∈S can be encoded in the element

w = ∑

x∈S wxx

of RS, and I claim that the transition matrix P of the random walk determined
by {wx} is simply the matrix of the operator “left multiplication by w”. More

20 KENNETH S. BROWN

precisely, we have for any a = ∑
s ass in RS

wa = ∑

x wxx ∑

s ass = ∑

t
 


 ∑

x,s
xs=t
 wxas



 t

= ∑

t
 (∑

s asP (s, t)

)
 t,

where the last equality follows from (1). Thus left multiplication by w acting on RS
corresponds to right multiplication by P acting on row vectors (as)s∈S. Similarly,
if we run the walk on an ideal C ⊆ S, then the transition matrix is the matrix of
left multiplication by w on RC, which is an ideal in the ring RS.
In principle, then, the analysis of the random walk has been reduced to ring
theory. Here is a familiar example in which this point of view can be exploited
(using C instead of R). Suppose that S is a ﬁnite abelian group G, and let ˆG
be its group of characters χ : G → C∗. Then the Fourier transform gives a ring
isomorphism
 CG ∼=
−→ C ˆG.

Here C ˆG is the ring of functions ˆG → C (with functions multiplied pointwise), and
the Fourier transform of a = ∑x axx is the function ˆa given by ˆa(χ) = ∑x axχ(x);
see [30, Section 6.2]. In particular, left multiplication by our element w acting on CG
is transformed to multiplication by ˆw acting on C ˆG. This operator is diagonal with
respect to the standard basis of C ˆG, and one concludes that the eigenvalues of the
transition matrix P are simply the numbers ˆw(χ). Moreover, the Fourier inversion
formula gives an explicit diagonalization of multiplication by w and hence of P .

7.2. Structure and representations of the semigroup algebra. We now re-
turn to the case of a LRB S. Our study of the semigroup algebra makes no use of
the fact that the scalars are real numbers or that {wx} is a probability distribution.
We therefore work in the semigroup algebra kS of S over an arbitrary ﬁeld k.
The axiom (2) for LRBs says that the support map S ։ L is a semigroup
homomorphism, where L is viewed as a semigroup under the join operation, X, Y ↦→
X ∨ Y . Extending to linear combinations, we obtain a k-algebra surjection

supp : kS ։ kL.

Now Solomon [31] showed that the semigroup algebra kL is isomorphic to a product
of copies of k; see also [19] and [34, Section 3.9]. Explicitly, if kL denotes the ring
of functions from L to k, then there is an algebra isomorphism

φ : kL ∼=
−→ kL

such that φ(X) for X ∈ L is the function 1Y ≥X , whose value at Y is 1 if Y ≥ X and
0 otherwise. (Note that φ preserves products because 1Y ≥X 1Y ≥X ′ = 1Y ≥X∨X ′.)
Composing φ with the support map, we obtain a map ψ : kS ։ kL, which plays the
role of the Fourier transform. It is not an isomorphism but, as we will see shortly,
its kernel is nilpotent; this turns out to be enough to let us compute eigenvalues.
Before proceeding to the analysis of the kernel, we record for future reference an
explicit formula for φ
−1. Let {δX }X∈L be the standard basis of kL; thus δX (Y ) =

SEMIGROUPS, RINGS, AND MARKOV CHAINS 21

1Y =X . Then φ is given by φ(X) = ∑Y ≥X δY ; hence X = ∑Y ≥X φ
−1(δY ), and
M¨obius inversion gives φ
−1(δX ) = eX , where

eX = ∑

Y ≥X µ(X, Y )Y.(16)

The elements eX therefore give a basis of kL consisting of pairwise orthogonal
idempotents, i.e., e2
X = eX and eXeY = 0 for X ̸= Y . In the standard terminology
of ring theory, they are the primitive idempotents of kL.
Consider now the kernel J of supp : kS ։ kL. It consists of linear combinations
of elements of S such that if we lump the terms according to supports, the coeﬃ-
cient sum of each lump is zero. Thus J = ∑X∈L JX , where JX consists of linear
combinations ∑supp x=X axx with ∑
x ax = 0. Suppose we compute a product ab
with a = ∑ axx ∈ JX and b = ∑ byy ∈ JY . If Y ≤ X, we get 0, because our
axiom (3) (Section 2.1) implies that xb = 0 for each x with supp x = X. If Y ≰ X,
on the other hand, then ab ∈ JX∨Y , and X ∨ Y > X.
Next, suppose we compute a product abc · · · of several factors, coming from JX ,
JY , JZ , . . . . By what we have just shown, we either get 0 or we get an increasing
chain X < X ∨ Y < X ∨ Y ∨ Z < · · · . Since L is ﬁnite, we must in fact get 0 if
there are enough factors. Thus the ideal J is nilpotent. Summarizing, we have:

Theorem 3 (Bidigare). There is an algebra surjection ψ : kS ։ kL whose kernel
J is nilpotent. The X-component of ψ is the homomorphism χX : kS → k given by

χX (y) = 1supp y≤X

for y ∈ S.

One can express the ﬁrst sentence of Theorem 3 by saying that J is the radical
of the ring kS and that kL is the semisimple quotient. Standard ring theory now
implies:

Corollary. Every irreducible representation of kS is 1-dimensional. There is one
such for each X ∈ L, given by the character χX .

We give the proof, for the convenience of readers not familiar with the concepts
of radical and semisimple quotient.

Proof. Let V be an irreducible kS-module. Then JV is a submodule of V , so it is
either V or 0. (Here JV is the set of ﬁnite sums ∑i aivi with ai ∈ J and vi ∈ V .)
It cannot be V , because then we would have J mV = V for all m, contradicting
the fact that J is nilpotent and V ̸= 0. So JV = 0, and the action of kS on V
factors through the quotient kL. Now consider the action on V of the standard
basis vectors δX of kL. Each δX V is a submodule (because kL is commutative),
so it is either V or 0. There cannot be more than one X with δX V = V because
δX δY = 0 for X ̸= Y . Since ∑
X δX = 1, it follows that exactly one δX is nonzero
on V , and it acts as the identity. Hence every a ∈ kS acts on V as multiplication
by the scalar χX (a), and irreducibility now implies that V is 1-dimensional.

For any ﬁnite-dimensional kS-module V , we can take a composition series

0 = V0 < V1 < · · · < Vn = V

and apply the corollary to each factor Vi/Vi−1. It follows that there are Xi ∈ L,
i = 1, . . . , n, such that the elements a ∈ kS are simultaneously triangularizable

22 KENNETH S. BROWN

on V , with diagonal entries χX1 (a), . . . , χXn (a). In particular, we can read oﬀ the
eigenvalues of a acting on V as soon as we know, for each X ∈ L, how many times
χX occurs as a composition factor.

7.3. The eigenvalues of P . We can now prove the formula for the eigenvalues of
our transition matrix P stated in Theorem 1, in somewhat greater generality:

Theorem 4. Let S be a ﬁnite LRB with identity, let k be a ﬁeld, and let w =∑
x∈S wxx be an arbitrary element of kS. Let P be deﬁned by equation (6). Then
P has an eigenvalue
 λX = ∑

supp y≤X wy

for each X ∈ L, with multiplicity mX , where
∑

Y ≥X mY = cX(17)

for each X ∈ L.

Proof. Recall from Section 7.1 that the eigenvalues of P are the same as the eigen-
values of w acting by left multiplication on the ideal kC ⊆ kS. For each X ∈ L, let
m′
X be the number of composition factors of kC given by the character χX . Then
the discussion at the end of Section 7.2 shows that P has eigenvalues χX (w) with
multiplicity m′
X . Now

χX (w) = ∑

y∈S wy1supp y≤X = ∑

supp y≤X wy = λX ,

so the proof will be complete if we show that ∑
Y ≥X m′
Y = cX for all X ∈ L.
Consider an arbitrary x ∈ S. It acts on kC as an idempotent operator, projecting
kC onto the linear span of the chambers in S≥x. The rank r of this projection is
therefore the number cX deﬁned in Section 3, where X = supp x. On the other
hand, the rank of a projection is the multiplicity of 1 as an eigenvalue, so

r = ∑

Y ∈L
χY (x)=1
 m′
Y = ∑

Y ≥X m′
Y .

Equating the two expressions for r gives ∑
Y ≥X m′
Y = cX , as required.

We turn now to the proof that P is diagonalizable when k = R and w is a
probability distribution.
 8. Semisimplicity

Let R[w] ⊆ RS be the subalgebra (with identity) generated by w = ∑

x∈S wxx,
where wx ≥ 0 and ∑x wx = 1. We will show that R[w] is semisimple; more precisely,
it is isomorphic to a direct product of copies of R. This implies that the action of w
is diagonalizable in every RS-module; in particular, it implies that the transition
matrix P of our walk on chambers is diagonalizable, as asserted in Theorem 1.
In order to show the idea of the proof in its simplest form, we begin by giving
in Section 8.1 a criterion (probably known) for the diagonalizability of a matrix A,
involving the poles of the generating function for the powers of A. In Section 8.2
we essentially repeat the proof, but in a more abstract setting; the result is a
criterion for semisimplicity of an algebra generated by a single element a, involving

SEMIGROUPS, RINGS, AND MARKOV CHAINS 23

the generating function for the powers of a. Then in Section 8.3 we compute the
powers of our element w ∈ R[w] ⊆ RS, and we deduce a formula for the generating
function. The criterion of Section 8.2 is visibly satisﬁed, and we get the desired
semisimplicity result in Section 8.4. As a byproduct of the proof we obtain formulas
for the primitive idempotents of R[w], which we state in Section 8.5. As a simple
example, we write out the formulas for the Tsetlin library with uniform weights in
Section 8.6. In a very technical Section 8.7 we attempt to organize the formulas in
a sensible way. Finally, we return to the Tsetlin library in Section 8.8, this time
with arbitrary weights, to illustrate the results of Section 8.7.

8.1. Diagonalizability. Let Mn(C) be the ring of n × n matrices over C, and let
A ∈ Mn(C). [With minor changes we could work over an arbitrary ﬁeld instead
of C.] Consider the generating function

f (t) = ∑

m≥0 A
mtm = 1
I − tA ,

where I is the identity matrix and the fraction is to be interpreted as (I − tA)
−1.
The series converges for small t ∈ C and represents a holomorphic function with
values in Mn(C). It is initially deﬁned in a neighborhood of 0, but we will see in
Proposition 1 that f is a rational function, i.e., that each of the n2 matrix entries
is a rational function in the usual sense. Let

g(z) = (1/z)f (1/z) = 1
zI − A ,

initially deﬁned for z in a neighborhood of ∞.

Proposition 1. The function g is rational, with poles precisely at the eigenvalues
of A. The matrix A is diagonalizable if and only if the poles of g are all simple. In
this case g has a partial fractions decomposition of the form

g(z) = ∑

i
 Ei
z − λi ,

where the λi are the distinct eigenvalues of A and Ei is the projection onto the
λi-eigenspace.

“Projection” here refers to the decomposition of Cn into eigenspaces.

Proof. Consider the Jordan decomposition A = ∑
i(λiEi + Bi); here the Ei are
pairwise orthogonal idempotents summing to I, the Bi are nilpotent, and Bi =
BiEi = EiBi. If A is diagonalizable, then each Bi = 0 and we have

g(z) = 1
zI − A = ∑

i
 1
z − λi Ei,

as required. If A is not diagonalizable, then for some eigenvalue λi we have Bi ̸= 0.
Since g(z) can be computed in each Jordan block separately, we may assume that

24 KENNETH S. BROWN

A = λI + B, where Br = 0 but Br−1 ̸= 0 for some r > 1. Then

g(z) = 1
zI − A

= 1
(z − λ)I − B

= 1
z − λ · 1
I − (z − λ)−1B

=
 r−1∑

j=0
 Bj

(z − λ)j+1 .

Thus g(z) is rational and has a pole of order r > 1 at z = λ.

8.2. A semisimplicity criterion. The ring-theoretic version of what we have just
done goes as follows. Let k be a ﬁeld and R a ﬁnite-dimensional commutative k-
algebra (with identity). For simplicity, we will pretend that k is a subﬁeld of C, so
that we can speak of convergent power series; to deal with a general ﬁeld k, one
needs to work with formal power series. In our application we will have k = R.
Assume that R is generated by a single element a. Thus R ∼= k[x]/(p) for some
polynomial p, with a corresponding to x mod p. We give here a criterion for R to
be split semisimple, i.e., isomorphic to kI , a product of copies of k indexed by a
(ﬁnite) set I. Giving such an isomorphism is equivalent to giving a basis (ei)i∈I
for R consisting of pairwise orthogonal idempotents. The ei are then characterized
as the primitive idempotents of R, i.e., the nonzero idempotents that cannot be
decomposed as sums of pairwise orthogonal nonzero idempotents.
Consider the generating function

f (t) =
 ∞∑

m=0 amtm = 1
1 − at ,

where the fraction is to be interpreted as (1R − at)
−1. It will follow from the proof
of Proposition 2 that the series has a positive radius of convergence and that f is
a rational function with values in A; this means that if we express f (t) in terms of
a basis for A, then each component is a rational function in the usual sense. Let

g(z) = (1/z)f (1/z) = 1
z − a ;

here we identify k with the ring of scalar multiples of the identity 1R, so that z − a
means z1R − a.

Proposition 2. The k-algebra R is split semisimple if and only if g(z) has the
form
 g(z) = ∑

i∈I
 ei
z − λi ,(18)

where the λi are distinct elements of k and the ei are nonzero elements of R. In
this case the ei are the primitive idempotents of R, and the generator a of R is
equal to ∑i∈I λiei.

Proof. Suppose A is split semisimple with primitive idempotents (ei)i∈I , and write
a = ∑i λiei. Then am = ∑
i λ
m
i ei, f (t) = ∑
i(1 − λit)
−1ei, and the expression (18)
for g(z) = (1/z)f (1/z) follows at once.

SEMIGROUPS, RINGS, AND MARKOV CHAINS 25

Conversely, suppose A is not split semisimple. Assume ﬁrst that the minimal
polynomial p of a splits into linear factors in k[x], say p(x) = ∏i∈I (x − λi)
ri, where
the λi are distinct. By the Chinese remainder theorem,

A ∼= ∏

i∈I k[x]/(x − λi)
ri ,(19)

and the assumption that A is not split semisimple implies that some ri > 1.
Since g(z) can be computed componentwise with respect to the decomposi-
tion (19) of A, we may assume that there is only one factor, i.e., that A =
k[x]/(x − λ)
r for some λ, where r > 1. Then a = λ + b, where br = 0 but
br−1 ̸= 0; hence
 g(z) = 1
z − a

= 1
(z − λ) − b

= 1
z − λ · 1
1 − (z − λ)−1b

=
 r−1∑

j=0
 bj

(z − λ)j+1 .

Thus g(z) has a pole of order r > 1 at z = λ and hence does not have the form (18).
If p does not split into linear factors, extend scalars to a splitting ﬁeld k′ of p
and apply the results above to A
′ = k′ ⊗k A ∼= k′[x]/(p). Then g(z), viewed now
as a function k′ → A
′, has poles at the roots of p, at least one of which is not in k.
Once again, g(z) does not have the form (18).

8.3. A formula for wm. Let S be a LRB and let w = ∑
x∈S wxx, where {wx}
is a probability distribution on S. From now on we identify w with {wx} and
simply say that w is a probability distribution. We wish to apply Proposition 2 to
R = R[w] ⊆ RS. To this end we need a formula for wm. As an aid to the intuition,
we use probabilistic language in deriving this formula. The interested reader can
recast the discussion in purely algebraic language, where it is valid with R replaced
by an arbitrary ﬁeld k and w by an arbitrary element of the semigroup algebra kS.
Our methods in this section are inspired by the paper of Fill [18].
By a reduced word we mean an l-tuple x = (x1, . . . , xl), xi ∈ S, such that
for each i = 1, . . . , l we have supp xi ≰ supp(x1 · · · xi−1). Equivalently, if we set
Xi = supp(x1 · · · xi), then we get a strictly increasing chain
ˆ0 = X0 < X1 < · · · < Xl
in L. We say that x is a reduced decomposition of the element ¯x = x1x2 · · · xl ∈ S.
The intuitive meaning of this is that there is no obvious way to shorten the expres-
sion x1x2 · · · xl by using the axiom (3) to delete factors. If an m-tuple (x1, . . . , xm)
is not necessarily reduced, there is a reduced word (x1, . . . , xm)̂, obtained by delet-
ing any xi such that supp xi ≤ supp(x1 · · · xi−1).

Remark. It might seem more natural to require the “letters” xi in a reduced word
to be in some given generating set S1 ⊆ S. In practice, one is typically interested
in S1 = {x ∈ S : wx ̸= 0}. Our convention of allowing arbitrary xi is harmless,
however, since only those words whose letters are in S1 make a nonzero contribution
to the formula (20) that we are going to derive.

26 KENNETH S. BROWN

We need some notation in order to state the formula. Let x = (x1, . . . , xl) be a
reduced word of length l = l(x), with associated chain

ˆ0 = X0 < X1 < · · · < Xl.

Let λ0, λ1, . . . , λl be the corresponding eigenvalues λXi as in Theorem 1, and,
for n ≥ 0, let Hn(x) = hn(λ0, . . . , λl), where hn is the complete homogeneous
symmetric function of degree n (sum of all monomials of degree n). Let wx =
wx1wx2 · · · wxl .

Proposition 3. Let S be a ﬁnite LRB with identity and let w ∈ RS be a probability
distribution. For any m ≥ 0,

wm = ∑

x Hm−l(x)(x)wx ¯x,(20)

where x ranges over the reduced words of length l(x) ≤ m.

Proof. Let y1, y2, · · · , ym be independent picks from the probability measure w.
We will get a formula for wm by computing the distribution of the reduced word
(y1, . . . , ym)̂; for we have

wm = ∑

l(x)≤m Pr{(y1, . . . , ym)̂= x}¯x.(21)

Given a reduced word x = (x1, . . . , xl) with associated chain (X0, . . . , Xl), we
compute the probability in (21) as follows. Let Si = S≤Xi = {x ∈ S : supp x ≤ Xi},
and let λi = λXi . In order to have (y1, . . . , ym)̂= x, the m-tuple (y1, . . . , ym) must
consist of i0 elements of S0, then x1, then i1 elements of S1, then x2, and so on,
ending with il elements of Sl, where i0, . . . , il ≥ 0 and i0 + · · · + il = m − l.
The probability of this, for ﬁxed i0, . . . , il, is λ
i0
0 wx1 λ
i1
1 wx2 λ
i2
2 · · · wxlλ
il
l . Summing
over all possible (i0, . . . , il), we see that the probability in question is Hm−l(x)wx,
whence (20).

Formula (20) can be rewritten in terms of the function g(z) of Section 8.2. Given
a reduced word x as above, set

gx(z) =
 l∏

i=0
 1
(z − λi) .

Corollary. Let g(z) = (1/z)f (1/z), where f (t) = ∑

m≥0 wmtm. Then

g(z) = ∑

x gx(z)wx ¯x,(22)

where x ranges over all reduced words.

Proof. Fix a reduced word x of length l, and let λ0, . . . , λl be as above. Then
∑

m≥l Hm−l(x)tm = tl ∑

m≥0 hm(λ0, . . . , λl)tm

= tl l∏

i=0
 1
1 − λit .

Setting t = 1/z and multiplying by 1/z, we obtain gx(z); (22) now follows from (20).

SEMIGROUPS, RINGS, AND MARKOV CHAINS 27

8.4. Proof of semisimplicity. Call an element X ∈ L feasible for w if X =
supp(x1 · · · xm) with wxi ̸= 0 for i = 1, . . . , m or, equivalently, if X is the join of
elements supp x with wx ̸= 0. Let Lw be the set of feasible elements of L. In
applying formulas (20) and (22), we need only consider reduced words x whose
associated chain is in Lw, since otherwise wx = 0. The eigenvalues λ0, . . . , λl are
then all distinct; in fact, we have λ0 < λ1 < · · · < λl. So we obtain an expression
of the form (18) for g(z) by splitting each gx(z) into partial fractions. We have
therefore proved the ﬁrst part of the following theorem:

Theorem 5. Let S be a ﬁnite LRB with identity and let w ∈ RS be a probability
distribution. Then the subalgebra R[w] is split semisimple. Consequently, the action
of w on any RS-module is diagonalizable.

The second assertion is an easy consequence of the ﬁrst. Indeed, if we write
w = ∑i λiei, where the ei are the primitive idempotents of R[w], then any RS-
module V decomposes as V = ⊕
i eiV , with w acting as multiplication by λi on eiV .
Theorem 1 is now completely proved.

Remark. Everything we have done remains valid with R replaced by an arbitrary
ﬁeld k and w by an arbitrary element of kS, with one proviso. Namely, it is no
longer automatic that the eigenvalues λ0, . . . , λl are distinct. In order to guarantee
this, we need to assume that w satisﬁes the following condition: Whenever X < Y
in Lw, one has λX ̸= λY . Under this assumption, then, k[w] is split semisimple.

8.5. Primitive idempotents, ﬁrst version. It is easy to determine the primitive
idempotents of R[w] (or k[w], under the hypotheses of the remark above) by using
Proposition 2 and formula (22). We assume, without loss of generality, that S is
generated by {x ∈ S : wx ̸= 0}; this implies that Lw = L.
Suppose ﬁrst that w is generic, by which we mean that λX ̸= λY for X ̸= Y in L.
(Thus we are excluding those probability measures that lie on the union of a certain
ﬁnite collection of hyperplanes in RS.) Then the homomorphism ψ : RS ։ RL of
Theorem 3 (Section 7.2) maps R[w] onto RL; in fact, ψ(w) = ∑X∈L λX δX , and it is
easy to check that RL is generated as an algebra by any element whose components
are all distinct. Since R[w] is known to be semisimple and ker ψ is nilpotent, it
follows that ψ maps R[w] isomorphically onto RL. Hence R[w] has one primitive
idempotent eX for each X ∈ L, and

w = ∑

X∈L λX eX .(23)

To compute eX , we have to multiply the right side of (22) by z − λX and then set
z = λX .
Let x be a reduced word as in Section 8.3, and suppose its associated chain
passes through X, say X = Xi. Then the residue of gx(z) at z = λX is

RX,x = (−1)
l−i

(λX − λ0) · · · (λX − λi−1)(λi+1 − λX ) · · · (λl − λX ) .

Hence
 eX = ∑

x RX,xwx ¯x,(24)

where x ranges over all reduced words whose chain passes through X.

28 KENNETH S. BROWN

If w is not generic, then this formula still makes sense, but one has to sum the
eX having a common value of λX in order to get the primitive idempotents of R[w];
the eX themselves may not lie in R[w]. Notice, however, that the eX still form
an orthogonal family of idempotents in RS summing to 1, and the decomposition
of w given in (23) is still valid. To see this, note that these assertions can be
formulated as polynomial equations in the variables wx; since the equations are
valid generically, they must hold as algebraic identities.
Summarizing, we have:

Theorem 6. Let S be a ﬁnite LRB with identity and let w be a probability dis-
tribution on S. Assume that S is generated, as a semigroup with identity, by
{x ∈ S : wx ̸= 0}. Then (24) deﬁnes an orthogonal family of idempotents eX ,
X ∈ L, such that (23) holds. If w is generic, then the eX are the primitive idem-
potents of R[w]. In general, the decomposition of w as a linear combination of
primitive idempotents of R[w] is obtained by grouping the terms in (23) according
to the value of λX .

8.6. Example: The Tsetlin library with uniform weights. Let S = Fn,
with uniform weights wi = 1/n on the elements (i) of length 1. For each x =
(x1, . . . , xl) ∈ S, the only reduced decomposition x of x with wx ̸= 0 is the obvious
one, x = ((x1), . . . , (xl)). The associated chain is given by Xi = {x1, . . . , xi} for
0 ≤ i ≤ l. If X = Xi, then the contribution of x to eX is

RX,xwxx = (−1)
l−i x
i!(l − i)! .(25)

To get eX , then, we have to sum over all x having some ordering of X as an initial
segment. The eigenvalue corresponding to X is λX = i/n. We conclude that R[w]
has n + 1 primitive idempotents e0, e1, . . . , en, where ei = ∑
|X|=i eX ; hence ei is
obtained by summing the right-hand side of (25) over all x of length l ≥ i. If
σl ∈ RS is the sum of all x ∈ S of length l, the result is

ei =
 n∑

l=i (−1)
l−i σl
i!(l − i)! =
 n∑

l=i (−1)
l−i(l
i
) σl
l! .

The decomposition of w is
 w = 1
n
 n∑

i=0 iei.

Recall that the Tsetlin library can also be obtained by using a quotient ¯S = ¯Fn
of Fn (Section 2.3). For any a ∈ RS, let ¯a be its image in R ¯S. Then the probability
distribution on ¯S that gives the Tsetlin library with uniform weights is ¯w. One
can check that the quotient map S ։ ¯S induces a surjection R[w] ։ R[ ¯w] with
1-dimensional kernel, spanned by en−1. Thus R[ ¯w] has n primitive idempotents
¯e0, . . . , ¯en−2, ¯en, with
 ¯ei =
 n∑

l=i (−1)
l−i(l
i
) ¯σl
l! .(26)

This equation is also valid for i = n−1, in which case its content is that ¯en−1 = 0, as
stated above; this follows from the fact that ¯σn−1 = ¯σn. Formula (26) is essentially
the same as a formula of Diaconis–Fill–Pitman [16, (4.5)], except that these authors

SEMIGROUPS, RINGS, AND MARKOV CHAINS 29

work with operators on RC and interpret the answer in terms of Solomon’s descent
algebra. We will explain this in more detail in Section 9.7.

Remark. We could equally well have treated general weights, but instead we will
do that in Section 8.8, as an illustration of a diﬀerent version of the formula for eX.

8.7. Primitive idempotents, second version. In this quite technical subsec-
tion we attempt to make sense out of formula (24) for the primitive idempotents.
Our goal, motivated by equation (16) for the primitive idempotents in RL, is to
write (24) in the form
 eX = ∑

Y ≥X νX,Y ,(27)

where νX,Y is a certain signed measure on CY = {y ∈ S : supp y = Y }. Comparing
this with (16), we see that νX,Y necessarily has total mass µ(X, Y ). As usual, νX,Y
is identiﬁed with a linear combination of the elements of CY , hence it is an element
of RS and (27) makes sense. The deﬁnition of νX,Y is complicated. We begin with
the case X = ˆ0, which is slightly simpler.
Fix Y ∈ L and consider an arbitrary chain X from ˆ0 to Y ,
ˆ0 = X0 < X1 < · · · < Xl = Y,

of length l = l(X) ≥ 0. We associate to X a defective probability measure ρX on
CY , as follows. Given y ∈ CY , consider all reduced decompositions (y1, . . . , yl) of
y whose associated chain is X. For each such decomposition, set wi = wyi and
λi = λXi and form the product
w1
λ1 − λ0
 w2
λ2 − λ0 · · · wl
λl − λ0 .

Then ρX(y) is the sum of all these products. This has a probabilistic interpretation:
Pick elements yi ∈ S≤Xi − {id} independently, according to the weights wy, where
i = 1, . . . , l. If supp(y1 · · · yi) = Xi for each i, form the product y1 · · · yl. This
deﬁnes a defective random variable with values in CY , and ρX is its distribution. (A
defective random variable is one that is deﬁned with probability ≤ 1; its distribution
is a positive measure having total mass ≤ 1.) The signed measure νˆ0,Y is now
obtained by taking an alternating sum:

νˆ0,Y = ∑

X (−1)
l(X)ρX,

where X ranges over all chains from ˆ0 to Y .
For general X, consider chains X from X to Y :

X = X0 < X1 < · · · < Xl = Y.

We ﬁrst deﬁne a defective probability measure ρx,X on CY , depending on a choice of
x ∈ CX . Pick y1, . . . , yl independently, with yi ∈ S≤Xi − S≤X. If supp(xy1 · · · yi) =
Xi for each i, form the product xy1 · · · yl. This gives a defective random variable
with values in CY , and ρx,X is its distribution. We now set

νx,Y = ∑

X (−1)
l(X)ρx,X ,(28)

where X ranges over all chains from X to Y . We can also describe νx,Y as the
measure obtained by applying the procedure of the previous paragraph to S≥x,
using the probability measure obtained from w via the projection S ։ S≥x.

30 KENNETH S. BROWN

We now deﬁne the desired νX,Y by averaging over x ∈ CX :

νX,Y = ∑

x∈CX πX (x)νx,Y ,(29)

where πX is the stationary distribution of the random walk on CX driven by the
weights wy, y ∈ S≤X (scaled to give a probability distribution). This completes the
formula for eX . We leave it to the interested reader to verify that (27) is indeed a
reformulation of (24); the starting point is to group the terms in (24) according to
the chain X associated with x.

Remark. The idempotent eˆ1 is the stationary distribution π of our random walk.
The decomposition of w can therefore be written as

w = π + ∑

X<ˆ1 λX eX ,

so that
 wm = π + ∑

X<ˆ1 λ
m
X eX .

In theory, this should make it possible to give precise estimates for

∥P m
c − π∥ = 1
2
 ∥
∥
∥ ∑

X<ˆ1 λ
m
X eX c∥
∥
∥
1.

In practice, however, the presence of signs makes this very tricky.

8.8. Example: The Tsetlin library. We return to S = Fn and the Tsetlin
library, but now with generic weights w1, . . . , wn. Since the associated lattice L is
the Boolean lattice of subsets of [n], we get 2n primitive idempotents eX in R[w], and
w = ∑
X⊆[n] λX eX , with λX = ∑
x∈X wx. Working through the deﬁnition of the
signed measure νX,Y for X ⊆ Y , one ﬁnds that it is (−1)
|Y −X| times the distribution
of the following random ordering of Y : Sample without replacement from X, getting
an ordering (x1, . . . , xi) of X, where i = |X|; sample without replacement from
Y − X, getting an ordering (y1, . . . , yj) of Y − X, where j = |Y − X|; now form
(x1, x2, . . . , xi, yj, . . . , y2, y1). Note the reversal of the ordering of the y’s; thus we
are building a random ordering of Y by accumulating elements of X from left to
right and elements of Y − X from right to left.
This gives a very explicit formula for the primitive idempotent

eX = ∑

Y ⊇X νX,Y .

This and the related formula
 wm = ∑

X⊆[n] λ
m
X eX ,

are essentially the formulas of Fill [18], except that he works with operators on RC
instead of with elements of RS. To get his formulas, right multiply the formulas
above by a permutation σ (chamber of S) and pick out the τ -component. This gives
(σ, τ )-entries of matrices. One can check that eX annihilates RC if |X| = n − 1, so
the spectral decomposition of left multiplication by w on RC only involves 2n − n
idempotents, as in Fill’s paper. This would have arisen more naturally if we had
used ¯Fn instead of Fn.

SEMIGROUPS, RINGS, AND MARKOV CHAINS 31

The reader who has come this far might ﬁnd it a useful exercise to rederive the
formulas for the uniform case (Section 8.6) from those above.

9. Reflection arrangements and Solomon’s descent algebra

The work of Bayer–Diaconis [3] and Diaconis–Fill–Pitman [16] relates certain
card-shuﬄing random walks on the symmetric group Sn to subalgebras of Solomon’s
descent algebra [32]. We show here how this surprising connection arises naturally
from semigroup considerations. We work with an arbitrary ﬁnite Coxeter group W
and its associated hyperplane face semigroup Σ (the Coxeter complex of W ). But
we will try to explain everything in concrete terms for the case W = Sn, in an eﬀort
to make the discussion accessible to readers unfamiliar with Coxeter groups.
Our treatment can be viewed as an elaboration of Tits’s appendix to Solomon’s
paper, with further ideas borrowed from Bidigare’s thesis [5]. In particular, we
use (and include a proof of) Bidigare’s theorem that Solomon’s descent algebra is
anti-isomorphic to the W -invariant part of the semigroup algebra of Σ.
In this section the probability measure driving our random walk on the chambers
of Σ is denoted by p instead of w, so that we can reserve the letter w for a typical
element of W .

9.1. Finite reﬂection groups. We begin with a very quick review of the basic
facts that we need about ﬁnite Coxeter groups and their associated simplicial com-
plexes Σ. Details can be found in many places, such as [10, 21, 23, 35]. A ﬁnite
reﬂection group on a real inner-product space V is a ﬁnite group of orthogonal
transformations of V generated by reﬂections sH with respect to hyperplanes H
through the origin. The set of hyperplanes H such that sH ∈ W is the reﬂection
arrangement associated with W . Its hyperplane face semigroup Σ can be identi-
ﬁed with the set of simplices of a simplicial complex, called the Coxeter complex
of W . Geometrically, this complex is gotten by cutting the unit sphere in V by
the hyperplanes H, as in Section A.6. (As explained there, one might have to ﬁrst
pass to a quotient of V .) The action of W on V induces an action of W on Σ, and
this action is simply-transitive on the chambers. Thus the set C of chambers can
be identiﬁed with W , once a “fundamental chamber” C is chosen.
The canonical example is W = Sn, acting on Rn by permuting the coordinates.
The arrangement in this case is the braid arrangement (Section A.5). The Coxeter
complex Σ can be identiﬁed with the following abstract simplicial complex: The
vertices are the proper nonempty subsets X ⊂ [n] = {1, . . . , n}, and the simplices
are the chains of such subsets. The Sn-action is induced by the action of Sn on [n].
The product on Σ was discussed in Section 2.3, where Σ was identiﬁed with the
semigroup B of ordered partitions. The chambers of Σ correspond to permutations
w of [n], with w corresponding to the chamber

{w(1)} < {w(1), w(2)} < · · · < {w(1), w(2), . . . , w(n − 1)}.

This is the same as the identiﬁcation of C with Sn that results from choosing

{1} < {1, 2} < · · · < {1, 2, . . . , n − 1}

as fundamental chamber.

32 KENNETH S. BROWN

9.2. Types of simplices. The number r of vertices of a chamber of Σ is called the
rank of Σ (and of W ); thus the dimension of Σ as a simplicial complex is r − 1. It is
known that one can color the vertices of Σ with r colors in such a way that vertices
connected by an edge have distinct colors. The color of a vertex is also called its
label, or its type, and we denote by I the set of all types. We can also deﬁne type(F )
for any F ∈ Σ; it is the subset of I consisting of the types of the vertices of F .
For example, every chamber has type I, while the empty simplex has type ∅. The
action of W is type-preserving; moreover, two simplices are in the same W -orbit if
and only if they have the same type. In our canonical example with W = Sn, the
rank is n − 1, the set of types is I = {1, . . . , n − 1}, and type(X) = |X| for any
vertex X (proper nonempty subset of [n]).
The labeling allows us to reﬁne the adjacency relation on chambers deﬁned in
Section A.7: If C, C′ are distinct adjacent chambers and F is their common face of
codimension 1, then type(F ) = I − i for some i ∈ I, and we say that C and C′ are i-
adjacent. In the canonical example, two distinct chambers X1 < X2 < · · · < Xn−1
and X ′
1 < X ′
2 < · · · < X ′
n−1 are i-adjacent if and only if Xj = X ′
j for j ̸= i. If we
identify chambers with permutations as above, then w and w′ are i-adjacent if and
only if the n-tuple (w′(1), w′(2), . . . , w′(n)) is obtained from (w(1), w(2), . . . , w(n))
by interchanging w(i) and w(i + 1). For example, the chambers labeled 2134 and
2314 in Figure 7 (Section A.6) are 2-adjacent.

9.3. Descent sets. Given two chambers C, C′, we deﬁne the descent set of C′ with
respect to C, denoted des(C, C′), to be the set of i ∈ I such that there is a minimal
gallery
 C = C0, C1, . . . , Cl = C′

ending with an i-adjacency between Cl−1 and Cl. (See section A.7 for the deﬁnition
and basic facts concerning minimal galleries.) Equivalently, we have i ∈ des(C, C′)
if and only if C and C′ are on opposite sides of the hyperplane supp F , where F
is the face of C′ of type I − i. Or, if C′′ is the chamber i-adjacent to C′, then
i ∈ des(C, C′) if and only if d(C, C′) = d(C, C′′) + 1.
If we have chosen a fundamental chamber C, then we write des(C′) instead of
des(C, C′), and we call it the descent set of C′. And if C′ corresponds to w ∈ W ,
i.e., if C′ = wC, then we also speak of des(w), the descent set of w. The terminology
is motivated by the canonical example, where the descent set of a permutation w is
{i : w(i) > w(i + 1)}; it is a subset of {1, 2, . . . , n − 1}. For example, the descent set
of 2431 is {2, 3}; this is consistent with the fact that there are two minimal galleries
from 1234 to 2431 in Figure 7, one ending with a 2-adjacency and the other with a
3-adjacency.
Descent sets can be characterized in terms of the semigroup structure on Σ:

Proposition 4. Given chambers C, C′ and a face F ≤ C′, we have F C = C′ if
and only if des(C, C′) ⊆ type(F ). Thus des(C, C′) is the type of the smallest face
F ≤ C′ such that F C = C′.

Proof. Suppose F C = C′. Given i ∈ des(C, C′), let G be the face of C′ of type I − i
and let H = supp G; see Figure 6. We know that C and C′ are on opposite sides
of H, so F must be strictly on the C′-side of H, hence F ≰ G and i ∈ type(F ).
This proves des(C, C′) ⊆ type(F ).
Conversely, suppose des(C, C′) ⊆ type(F ). To show F C = C′, it suﬃces to show
that F C and C′ are on the same side of every hyperplane H = supp G, where G

SEMIGROUPS, RINGS, AND MARKOV CHAINS 33

s

 
 
 
 
  
❅
❅
❅
❅
❅❅ 
 
 
 
  
❅
❅
❅
❅
❅❅
 C ′G i

H

Figure 6.

is a codimension 1 face of C′; see [10, Section I.4B]. This is automatic if C and C′

are on the same side of H, so assume they are not. Writing type(G) = I − i, we
then have i ∈ des(C, C′), hence i ∈ type(F ). Then F ≰ G, so F is strictly on the
C′-side of H and therefore F C is on the C′-side of H.

9.4. Descent counts and the h-vector. In this subsection we ﬁx a fundamental
chamber C, so that every chamber C′ has a well-deﬁned descent set des(C′). For
J ⊆ I, let β(J) be the number of chambers with descent set J. This number is
independent of the choice of C, since the group of type-preserving automorphisms
of Σ is transitive on the chambers. It can also be described as the number of
w ∈ W with descent set J. We will show that the vector (β(J))J⊆I coincides with
the “h-vector” deﬁned below; the deﬁnition is modeled on that of the ﬂag h-vector
for graded posets (see Section C.3).
First we deﬁne the f -vector of Σ by setting fJ (Σ) equal to the number of sim-
plices of type J. The h-vector is then obtained by writing

fJ (Σ) = ∑

K⊆J hK(Σ),(30)

or, equivalently,
 hJ (Σ) = ∑

K⊆J(−1)
|J−K|fK(Σ).(31)

Proposition 5. Let Σ be the Coxeter complex of a ﬁnite reﬂection group, and let
I be the set of types of vertices. Then for any J ⊆ I,

β(J) = hJ (Σ).

Proof. Let ΣJ be the set of simplices of type J. There is a 1–1 map ΣJ → C, given
by F ↦→ F C, where C is the fundamental chamber. It is 1–1 because we can recover
F from F C as the face of type J. Its image, according to Proposition 4, is the set
of chambers with descent set contained in J. Hence

fJ (Σ) = ∑

K⊆J β(K).

The proposition now follows from (30).

34 KENNETH S. BROWN

Remark. Everything in this and the previous subsection generalizes from ﬁnite
Coxeter complexes to ﬁnite buildings.

9.5. The ring of invariants in the semigroup algebra. Fix a commutative
ring k and consider the semigroup algebra kΣ. This has a natural W -action, and
the W -invariants form a k-algebra A = (kΣ)
W . As a k-module, A is free with
one basis element for each W -orbit in Σ, that basis element being the sum of the
simplices in the orbit. Since orbits correspond to types of simplices, we get a basis
vector
 σJ = ∑

F ∈ΣJ F

for each J ⊆ I, where, as in the proof of Proposition 5, ΣJ is the set of simplices
of type J. The product of two basis vectors is given by

σJ σK = ∑

L αJKLσL,

where αJKL is the number of ways of writing a given simplex of type L as a product
F G, where type(F ) = J and type(G) = K. This number is 0 unless J ⊆ L.
There is a second natural basis (τJ )J⊆I for A, obtained by writing

σJ = ∑

K⊆J τK ,

or, equivalently,
 τJ = ∑

K⊆J(−1)
|J−K|σK.

This change of basis is motivated by the study of the h-vector above, and also by
considerations in Solomon’s paper [32].

9.6. Solomon’s descent algebra. Bidigare [5] proved that A is anti-isomorphic
to Solomon’s descent algebra, which is a certain subalgebra of the group algebra
kW . We give here a geometric version of his proof.
Recall that the k-module kC spanned by the chambers is an ideal in kΣ. In
particular, it is a module over the subring A ⊆ kΣ, and the action of A on kC
commutes with the action of W ; we therefore obtain a homomorphism

A → EndW (kC),

the latter being the ring of kW -endomorphisms of kC.
We now choose a fundamental chamber C ∈ C and use it to identify C with W ,
the correspondence being wC ↔ w. This is compatible with left W -actions, so
EndW (kC) gets identiﬁed with the ring of operators on kW that commute with the
left action of kW . But any such operator T is given by right multiplication by an
element of kW , that element being T (id). So we obtain, ﬁnally, a product-reversing
map (i.e., an anti-homomorphism)
 φ : A → kW.

Chasing through the deﬁnitions, one sees that φ is characterized by

φ(a)C = aC(32)
 SEMIGROUPS, RINGS, AND MARKOV CHAINS 35

for a ∈ A. Here C is the fundamental chamber, the product on the left is given by
the action of W on C, and the product on the right takes place in the semigroup
algebra kΣ.
Recall now that the choice of fundamental chamber determines a special set of
generators S for W (the “simple reﬂections”, or “Coxeter generators”), consisting
of the reﬂections with respect to the supports of the codimension 1 faces of C.
Using this set of generators, Solomon [32] deﬁned a subalgebra of kW , which has
come to be known as the descent algebra.

Theorem 7 (Bidigare). Let W be a ﬁnite reﬂection group with Coxeter complex Σ,
and let A be the invariant subalgebra (kΣ)
W of the semigroup algebra kΣ, where k
is an arbitrary commutative ring. Then A is anti-isomorphic to Solomon’s descent
algebra.

Proof. Let (σJ ) and (τJ ) be the k-bases of A introduced in Section 9.5. We have

σJ C = ∑

F ∈ΣJ F C.

As we noted in the proof of Proposition 5, the chambers F C that occur in the sum
are those with descent set contained in J. Under our bijection between C and W ,
a given chamber F C corresponds to the element w ∈ W such that F C = wC. So
we can write
 σJ C = ∑

w∈UJ wC,

where UJ = {w ∈ W : des(w) ⊆ J}. Our characterization (32) of φ therefore yields

φ(σJ ) = uJ := ∑

w∈UJ w.

Let ZJ = {w ∈ W : des(w) = J} and let zJ = ∑w∈ZJ w. Then uJ = ∑K⊆J zK, so
∑

K⊆J φ(τK ) = ∑

K⊆J zK

for all J, hence φ(τJ ) = zJ . Since the zJ are clearly linearly independent, it follows
that φ is injective and hence gives an anti-isomorphism of A onto a subalgebra
of kW .
It remains to show that φ(A) is the descent algebra. For each i ∈ I, let si be the
reﬂection with respect to the face of C of type I − i. Then our set of generators
of W is S = {si : i ∈ I}. Moreover, for any J ⊆ I the stabilizer of the face of C of
type J is the subgroup WI−J generated by {si : i ∈ I − J}; for example, the face of
type I −i has stabilizer of order 2, generated by si. Finally, our deﬁnition of descent
sets has the following translation: i ∈ des(w) if and only if ℓ(wsi) < ℓ(w), where
ℓ is the length function on W with respect to the generating set S. Using these
remarks, the reader can easily check that our basis vector uJ for φ(A) coincides
with Solomon’s xT , where T = {si : i ∈ I − J} ⊆ S. Hence φ(A) is equal to the
descent algebra.

Remark. There has been interest recently in giving explicit formulas for orthogonal
families of idempotents in the descent algebra that lift the primitive idempotents
of the algebra mod its radical. See, for example, Bergeron et al [4] and earlier
references cited there. The results of the present paper provide further formulas of

36 KENNETH S. BROWN

this type; it suﬃces to take a generic element p = ∑F ∈Σ pF F ∈ (kΣ)
W , ﬁnd the
primitive idempotents in k[w] by the results of Section 8, and apply φ.

9.7. The descent algebra and random walks. Assume, for the moment, that
we have not chosen a fundamental chamber. Given a W -invariant probability dis-
tribution p = ∑
F ∈Σ pF F , we get a W -invariant random walk on C with transition
matrix
 P (C, D) = ∑

F C=D pF

for C, D ∈ C. (“W -invariant” means P (wC, wD) = P (C, D) for C, D ∈ C, w ∈ W .)
If we now choose a fundamental chamber C and identify C with W , we get a left-
invariant Markov chain on W whose transition matrix satisﬁes

P (id, w) = µw := ∑

F C=wC pF .

Left invariance implies that this is a right random walk on the group W : At each
step, we choose w with probability µw and right-multiply by w. Note that the
deﬁnition of the probability distribution {µw} on W can be written as µC = pC,
where µ = ∑w∈W µww ∈ RW ; as in (32), the product on the left is given by
the action of W and the product on the right is in RΣ. Hence (32) implies that
µ = φ(p). We have therefore proved:

Theorem 8. Let W be a ﬁnite reﬂection group with Coxeter complex Σ, and let
p be a W -invariant probability distribution on Σ. Choose a fundamental chamber
and use it to identify C with W . Then the hyperplane chamber walk on C driven
by p corresponds to the right random walk on W driven by µ, where µ ∈ RW is the
image of p under the isomorphism of Theorem 7 between (RΣ)
W and the descent
subalgebra of RW . Consequently, the algebra R[µ] ⊆ RW generated by µ is a split
semisimple commutative subalgebra of the descent algebra.

Suppose, for example, that p is uniform on simplices of type J for some ﬁxed J.
Then the proof of Theorem 7 shows that µ = φ(p) is uniform on the w ∈ W
with des(w) ⊆ J. This explains some of the observations in [3, 16]. Returning
to our canonical example with W = Sn, let J = {1}; thus p is uniform on the
vertices of type 1, i.e., the singleton subsets of [n]. The corresponding hyperplane
chamber walk is the Tsetlin library with uniform weights. Viewing this as a walk
on the permutation group Sn, it is the right random walk driven by the uniform
distribution µ on the permutations w with des(w) ⊆ {1}. There are n such, with
(w(1), . . . , w(n)) = (i, 1, 2, . . . , i − 1, i + 1, . . . , n), i = 1, . . . , n.
Continuing with this example, we can use formula (26) (Section 8.6) to get
formulas for the primitive idempotents in R[µ]. In fact, the probability distribu-
tion ¯w ∈ R ¯S of Section 8.6 is the same as what we are now calling p. (Recall from
Section 5.1 that ¯S ⊂ Σ, so this assertion makes sense.) And the element ¯σl of
Section 8.6 is the same as the element σ{1,...,l} ∈ (RΣ)
W if l < n, while ¯σn = ¯σn−1.

Combining the isomorphism R[ ¯w] = R[p] ∼=
−→ R[µ] with equation (26), we now
obtain the following result: Deﬁne vl ∈ RW for 0 ≤ l ≤ n by

vl = ∑

des(w)⊆{1,...,l} w if l < n,

SEMIGROUPS, RINGS, AND MARKOV CHAINS 37

and
 vn = vn−1.

Let
 Ei =
 n∑

l=i (−1)
l−i(l
i

) vl
l! .

Then E0, . . . , En−2, En, are the primitive idempotents in R[µ]. These formulas are
the same as those of [16, Theorem 4.2].

Appendix A. The hyperplane face semigroup

More details concerning the material reviewed here can be found in [6, 7, 9, 10,
11, 25, 41]. Throughout this section A = {Hi}i∈I denotes a ﬁnite set of aﬃne
hyperplanes in V = Rn. Let H +
i and H −
i be the two open halfspaces determined
by Hi; the choice of which one to call H +
i is arbitrary but ﬁxed.

A.1. Faces and chambers. The hyperplanes Hi induce a partition of V into
convex sets called faces (or relatively open faces). These are the nonempty sets
F ⊆ V of the form
 F = ⋂

i∈I H σi
i ,

where σi ∈ {+, −, 0} and H 0
i = Hi. Equivalently, if we choose for each i an aﬃne
function fi : V → R such that Hi is deﬁned by fi = 0, then a face is a nonempty
set deﬁned by equalities and inequalities of the form fi > 0, fi < 0, or fi = 0, one
for each i ∈ I. The sequence σ = (σi)i∈I that encodes the deﬁnition of F is called
the sign sequence of F and is denoted σ(F ).
The faces such that σi ̸= 0 for all i are called chambers. They are convex open
sets that partition the complement V −⋃
i∈I Hi. In general, a face F is open relative
to its support, which is deﬁned to be the aﬃne subspace

supp F = ⋂

σi(F )=0 Hi.

Since F is open in supp F , we can also describe supp F as the aﬃne span of F .

A.2. The face relation. The face poset of A is the set F of faces, ordered as
follows: F ≤ G if for each i ∈ I either σi(F ) = 0 or σi(F ) = σi(G). In other words,
the description of F by linear equalities and inequalities is obtained from that of G
by changing zero or more inequalities to equalities.

A.3. Product. The set F of faces is also a semigroup. Given F, G ∈ F , their
product F G is the face with sign sequence

σi(F G) =
 {σi(F ) if σi(F ) ̸= 0
σi(G) if σi(F ) = 0.

This has a geometric interpretation: If we move on a straight line from a point of F
toward a point of G, then F G is the face we are in after moving a small positive
distance. Notice that the face relation can be described in terms of the product:
One has
 F ≤ G ⇐⇒ F G = G.(33)

38 KENNETH S. BROWN

A.4. The semilattice of ﬂats. A second poset associated with the arrangement
A is the semilattice of ﬂats, also called the intersection semilattice, which we denote
by L. It consists of all nonempty aﬃne subspaces X ⊆ V of the form X = ⋂
H∈A′ H,
where A
′ ⊆ A is an arbitrary subset (possibly empty). We order L by inclusion.
[Warning: Many authors order L by reverse inclusion.] Notice that any two el-
ements X, Y have a least upper bound X ∨ Y in L, which is the intersection of
all hyperplanes H ∈ A containing both X and Y ; hence L is an upper semilattice
(poset with least upper bounds). It is a lattice if the arrangement A is central, i.e.,
if ⋂
H∈A H ̸= ∅. Indeed, this intersection is then the smallest element of L, and a
ﬁnite upper semilattice with a smallest element is a lattice [34, Section 3.3]. The
support map gives a surjection
 supp : F ։ L,

which preserves order and also behaves nicely with respect to the semigroup struc-
ture. Namely, we have
 supp(F G) = supp F ∨ supp G(34)

and
 F G = F ⇐⇒ supp G ≤ supp F.(35)

A.5. Example: The braid arrangement. The braid arrangement in Rn consists
of the (
n
2) hyperplanes Hij deﬁned by xi = xj, where 1 ≤ i < j ≤ n. Each
chamber is determined by an ordering of the coordinates, so it corresponds to a
permutation. When n = 4, for example, one of the 24 chambers is the region
deﬁned by x2 > x3 > x1 > x4, corresponding to the permutation 2314. The faces
of a chamber C are obtained by changing to equalities some of the inequalities
deﬁning C. For example, the chamber x2 > x3 > x1 > x4 has a face given by
x2 > x3 > x1 = x4, which is also a face of the chamber x2 > x3 > x4 > x1.
It is useful to encode the system of equalities and inequalities deﬁning a face F by
an ordered partition (B1, . . . , Bk) of [n] = {1, . . . , n}. Here B1, . . . , Bk are disjoint
nonempty sets whose union is [n], and their order counts. For example, the face
x2 > x3 > x1 = x4 corresponds to the 3-block ordered partition ({2}, {3}, {1, 4}),
and the face x2 > x1 = x3 = x4 corresponds to the 2-block ordered partition
({2}, {1, 3, 4}).
Thus the face semigroup of the braid arrangement can be viewed as the set B of
ordered partitions, with a product that one can easily work out. We have recorded
this product in Section 2.3, where one can also ﬁnd a description of the face relation,
the intersection lattice, and the support map. See also Section 9.1, where the braid
arrangement appears as the canonical example of a reﬂection arrangement.

A.6. Spherical representation. Suppose now that A is a central arrangement,
i.e., that the hyperplanes have a nonempty intersection. We may assume that this
intersection contains the origin. Suppose further that ⋂
i∈I Hi = {0}, in which case
A is said to be essential. (There is no loss of generality in making this assump-
tion; for if it fails, then we can replace V by the quotient space V / ⋂i Hi.) The
hyperplanes then induce a cell-decomposition of the unit sphere, the cells being
the intersections with the sphere of the faces F ∈ F . Thus F , as a poset, can be
identiﬁed with the poset of cells of a regular cell-complex Σ, homeomorphic to a
sphere. Note that the face F = {0}, which is the identity of the semigroup F , is not

SEMIGROUPS, RINGS, AND MARKOV CHAINS 39

visible in the spherical picture; it corresponds to the empty cell. The cell-complex
Σ plays a crucial role in [11], to which we refer for more details.
The braid arrangement provides a simple example. It is not essential, because
the hyperplanes Hij intersect in the line L deﬁned by x1 = · · · = xn. We can
therefore view the braid arrangement as an arrangement in the (n − 1)-dimensional
quotient space Rn/L. When n = 4, we obtain an arrangement of six planes in R3,
whose spherical picture is shown in Figure 7. The plane corresponding to Hij cuts

  
  
  

    
   
  
  
 2
 3
1

2413 2431
 2341

23142134

2143

1243 1234

1324 3124

3214
 3412

3421

3142
13421432

1423
 3241
 1-2

2-4

2-3
 3-4

1-4
 1-3

Figure 7. The braid arrangement when n = 4.

the sphere in the great circle labeled i-j. Each chamber of the arrangement is a
simplicial cone, which intersects the sphere in a triangle labeled with the associated
permutation. Figure 7 has been reproduced from [7], where one can ﬁnd further
discussion and more examples.

A.7. Galleries and convex sets. We return to an arbitrary arrangement A. Two
chambers C, C′ ∈ C are said to be adjacent if they have a common codimension 1
face. A gallery is a sequence of chambers C0, C1, . . . , Cl such that Cj−1 and Cj
are adjacent for each j = 1, 2, . . . , l. Given C, C′ ∈ C, the minimal length l of
a gallery from C to C′ is the distance between C and C′, denoted d(C, C′); and
any gallery from C to C′ of minimal length d(C, C′) is called a minimal gallery.
The distance d(C, C′) can also be characterized as the number of hyperplanes in A
separating C from C′; in fact, every minimal gallery from C to C′ crosses each of
these hyperplanes exactly once (see [10, Section I.4E]).
Let D ⊆ C be a nonempty set of chambers. We say that D is convex if it satisﬁes
the equivalent conditions of the following result:

Proposition 6. The following conditions on a nonempty set D ⊆ C are equivalent:

(i) For any C, C′ ∈ D, every minimal gallery from C to C′ is contained in D.
(ii) D is the set of chambers in an intersection of some of the halfspaces deter-
mined by A.

40 KENNETH S. BROWN

In terms of sign sequences, condition (ii) says that there is a subset J ⊆ I and
a set of signs σi ∈ {+, −}, i ∈ J, such that

D = {C ∈ C : σi(C) = σi for all i ∈ J}.

Proposition 6, which is stated as in exercise in [10, Section I.4E], is essentially
due to Tits [35, Theorem 2.19]. See also [9, Proposition 4.2.6] for a proof in the
context of oriented matroids. For the convenience of the reader, here is the latter
proof specialized to hyperplane arrangements:

Proof. A minimal gallery from C to C′ crosses only the hyperplanes that separate
C from C′. This shows that (ii) implies (i). For the converse, it suﬃces to show
that if (i) holds and C is a chamber not in D, then there is a hyperplane H ∈ A
separating C from D. Choose a gallery D, C1, C2, . . . , Cl = C of minimal length,
starting in D and ending at C. By minimality, we have C1 /∈ D. Let H be the
(unique) hyperplane in A separating D from C1. Then H also separates D from C.
For any D′ ∈ D, we have d(D, D′) = d(C1, D′) ± 1, where the sign depends on
which H-halfspace contains D′. The sign cannot be +, because then we could
construct a minimal gallery from D to D′ passing through C1, contradicting (i). So
d(D, D′) = d(C1, D′) − 1, which means that D and D′ are on the same side of H.
Thus H separates D from C, as required.

Appendix B. Left-regular bands: Foundations

In this appendix S is an arbitrary semigroup, not necessarily ﬁnite, not neces-
sarily having an identity. Motivated by the theory of hyperplane face semigroups,
we wish to isolate the conditions on S under which we can deﬁne analogues of the
face relation, chambers, the semilattice of ﬂats, etc.

B.1. Partial order. Given x, y ∈ S, we set x ≤ y if xy = y. This relation is
transitive for any semigroup (see the ﬁrst paragraph of Section 2.2). It is reﬂexive if
and only if every element of S is idempotent, in which case S is called an idempotent
semigroup or a band. Antisymmetry, however, imposes a much stronger condition
on S:

Proposition 7. The relation deﬁned above is a partial order if and only if S is an
idempotent semigroup satisfying
 xyx = xy(36)

for all x, y ∈ S.

In other words, the relation makes S a poset if and only if S is a LRB as deﬁned
in Section 1.1.

Proof. For the “if” part see the beginning of Section 2.2. To prove the converse,
we may assume that S is an idempotent semigroup for which the relation is an-
tisymmetric, and we must prove (36). Note that (xy)(xyx) = (xy)
2x = xyx, so
xy ≤ xyx. On the other hand, (xyx)(xy) = xyxy = (xy)
2 = xy, so xyx ≤ xy.
Thus antisymmetry implies that xyx = xy, as required.

SEMIGROUPS, RINGS, AND MARKOV CHAINS 41

B.2. The associated semilattice. We now show how to construct, for any idem-
potent semigroup satisfying (36), an analogue of the intersection semilattice of a
hyperplane arrangement. In particular, this shows that the deﬁnition of LRB given
in Section 1 is equivalent to the one given in Section 2 and used throughout this
paper.

Proposition 8. Let S be an idempotent semigroup satisfying (36). Then there is
a semilattice L that admits an order-preserving surjection supp : S ։ L such that

supp xy = supp x ∨ supp y(37)

for all x, y ∈ S and
 xy = x ⇐⇒ supp y ≤ supp x.(38)

Proof. The construction of L is forced on us by (38): Deﬁne a relation ≼ on S
by y ≼ x ⇐⇒ xy = x. This is transitive and reﬂexive, but not necessarily
antisymmetric. We therefore obtain a poset L by identifying x and y if x ≼ y
and y ≼ x. If we denote by supp : S ։ L the quotient map, then (38) holds by
deﬁnition. To see that supp is order-preserving, suppose that x ≤ y, i.e., xy = y.
Multiplying on the right by x and using (36), we conclude that xy = yx; hence
yx = y and x ≼ y, i.e., supp x ≤ supp y. It remains to show that supp xy is the
least upper bound of supp x and supp y in L. It is an upper bound because the
equations xyx = xy and xyy = xy show that xy ≽ x and xy ≽ y. And it is the
least upper bound, because if z ≽ x and z ≽ y, then zx = z and zy = z, whence
z(xy) = (zx)y = zy = z, so that z ≽ xy.

If S has an identity e, then L has a smallest element ˆ0 = supp e. If, in addition,
L is ﬁnite, then it is is a lattice [34, Section 3.3].

B.3. Chambers. We close this appendix by giving several characterizations of the
chambers. Let S be a LRB whose semilattice L has a largest element ˆ1. This is
automatic if S is ﬁnite. As in Section 1.1, we call an element c ∈ S a chamber if
supp c = ˆ1.

Proposition 9. The following conditions on an element c ∈ S are equivalent:

(i) c is a chamber.
(ii) cx = c for all x ∈ S.
(iii) c is maximal in the poset S.

Proof. We have supp c = ˆ1 ⇐⇒ supp c ≥ supp x for all x ∈ S. In view of (38),
this holds if and only if cx = x, so (i) and (ii) are equivalent. If (ii) holds then c
is maximal, because c ≤ x =⇒ cx = x =⇒ c = x. For the converse, note that
c ≤ cx for all x, c ∈ S; so if c is maximal then (ii) holds.

The set C of chambers is a 2-sided ideal in S. Indeed, (ii) shows that it is a right
ideal, and it is a left ideal because if supp c = ˆ1 then supp xc = ˆ1 by (37). One can
check that C is the kernel of the semigroup S, i.e., the (unique) minimal 2-sided
ideal.

42 KENNETH S. BROWN

Appendix C. Generalized derangement numbers

In this appendix we associate to any ﬁnite poset L with ˆ0, ˆ1 a derangement
number d(L) ≥ 0. If L is the Boolean lattice of rank n, then d(L) is the ordinary
derangement number dn (number of ﬁxed-point-free permutations of an n-set). If
L is the lattice of subspaces of an n-dimensional vector space over Fq, then d(L) is
the q-analogue of dn studied by Wachs [36]. If L is the lattice of contractions of a
graph, then d(L) is some (new) graph invariant.
We are mainly interested in the case where L is a geometric lattice, i.e., the
lattice of ﬂats of a matroid. In this case, the derangement numbers of the intervals
[X, ˆ1] give the multiplicities of the eigenvalues for the random walk on the maximal
chains of L constructed in Section 6.2. But since the derangement numbers may
be of independent interest, we will keep this appendix logically independent of the
theory of random walks; the latter will be mentioned only for motivation.

C.1. Deﬁnition. Let L be a ﬁnite poset with smallest element ˆ0 and largest ele-
ment ˆ1. We associate to L an integer d(L), called the derangement number of L.
It is deﬁned inductively by the equation
∑

X∈L d([X, ˆ1]) = f (L),(39)

where f (L) is the number of maximal chains in L. If L = 0 (the one-element poset,
with ˆ0 = ˆ1), this gives d(L) = 1. Otherwise, it gives a recurrence that can be solved
for d(L) = d([ˆ0, ˆ1]); thus
 d(L) = f (L) − ∑

X>ˆ0 d([X, ˆ1]).(40)

Note that d(L) = 0 if L is the two-element poset {ˆ0, ˆ1}. More generally, d(L) = 0
if L has exactly one atom, where an atom is a minimal element of L − ˆ0. Indeed,
let X0 be the atom and let L0 = [X0, ˆ1]. Then f (L) = f (L0), so (40) becomes

d(L) = f (L0) − ∑

X∈L0 d([X, ˆ1]),

and the right side is 0 by (39) applied to L0.
If we apply the deﬁnition (39) to each interval [Y, ˆ1], we get

f ([Y, ˆ1]) = ∑

X≥Y d([X, ˆ1]).(41)

In case L is a geometric lattice, this system of equations for the numbers d([X, ˆ1])
is the same as the system of equations (14) in Section 6.2 for the multiplicities mX ;
this proves our assertion that d([X, ˆ1]) = mX . And this interpretation of d([X, ˆ1])
also provides an easy way to remember the deﬁnition (39), which says that the sum
of the multiplicities equals the size of the state space for the random walk.
We can solve (41) by M¨obius inversion to get

d([Y, ˆ1]) = ∑

X≥Y µ(Y, X)f ([X, ˆ1]).

Setting Y = ˆ0, we get an explicit formula for d(L):

d(L) = ∑

X∈L µ(ˆ0, X)f ([X, ˆ1]).(42)
 SEMIGROUPS, RINGS, AND MARKOV CHAINS 43

It is useful to have a slight variant of this:

d(L) = µ(ˆ0, ˆ1) + ∑

X∈M d([ˆ0, X]),(43)

where M is the set of maximal elements of L − ˆ1. This is proved by writing

f ([X, ˆ1]) = ∑

Y ∈M
Y ≥X
 f ([X, Y ])

for X < ˆ1, and then rearranging the sum in (42).
It is not clear from what we have done so far that d(L) ≥ 0, though we know this
is true if L is geometric, since it is the multiplicity mˆ0. An independent proof of
this, valid for any L, is obtained by giving yet another recursive formula for d(L),
which involves no signs.

Proposition 10. If L = 0 then d(L) = 1. Otherwise,

d(L) = ∑

X<ˆ1
(c(X) − 1)d([ˆ0, X]),(44)

where c(X) is the number of covers of X.

(Recall that Y covers X, written X ⋖ Y , if X < Y and there is no Z with
X < Z < Y .)

Corollary. d(L) ≥ 0, with equality if and only if L has exactly one atom.

Proof of the corollary. The inequality is immediate by induction on the size of L.
We have already observed that equality holds if L has exactly one atom. If L has
no atoms, then L = 0 and d(L) = 1 > 0. If L has more than one atom, then
consideration of the term X = ˆ0 in (44) shows that d(L) > 0.

Proof of Proposition 10. Let us temporarily take the statement of the proposition
as a new deﬁnition of d(L). It then suﬃces to show that, with this deﬁnition,
equation (39) holds. We may assume that L ̸= 0 and that (39) holds for smaller
posets. Then
∑

X∈L d([X, ˆ1]) = 1 + ∑

X<ˆ1 d([X, ˆ1])

= 1 + ∑

X<ˆ1
 ∑

X≤Y <ˆ1
(c(Y ) − 1)d([X, Y ]) by (44)

= 1 + ∑

Y <ˆ1
(c(Y ) − 1) ∑

X≤Y d([X, Y ])

= 1 + ∑

Y <ˆ1
(c(Y ) − 1)f ([ˆ0, Y ]) by induction

= 1 + ∑

Y ∈L
(c(Y ) − 1)f ([ˆ0, Y ]) + f (L).

So we are done if we can show 1 + ∑Y ∈L(c(Y ) − 1)f ([ˆ0, Y ]) = 0, i.e.,

1 + ∑

Y ∈L c(Y )f ([ˆ0, Y ]) = ∑

Y ∈L f ([ˆ0, Y ]).

44 KENNETH S. BROWN

The sum on the right counts all chains ˆ0 = X0 ⋖ X1 ⋖ · · · ⋖ Xm in L, where m ≥ 0.
The sum on the left counts all such chains of length m > 0. Adding 1 counts the
chain of length 0, so the equation holds.

C.2. Examples.

Example 1 (Ordinary derangement numbers). Let L be the Boolean lattice of sub-
sets of an n-set. Writing d(L) = dn, the recurrence (39) becomes

n∑

i=0
 (
n
i
 )
di = n!,

which is a standard recurrence for the ordinary derangement numbers. (It is ob-
tained by counting permutations according to the number of elements they move.)
Formulas (42) and (43) are the well-known results

dn =
 n∑

i=0(−1)
i(
n
i
 )
(n − i)! = n!
 n∑

i=0
 (−1)
i

i!

and
 dn = ndn−1 + (−1)
n;(45)

see [34, Section 2.2]. Finally, Proposition 10 reads

d0 = 1

dn =
 n−1∑

i=0
 (n
i
 )
(n − i − 1)di (n > 0),

which may be new.

Example 2 (q-analogue). Let L be the lattice of subspaces of an n-dimensional
vector space over Fq. Writing d(L) = dn [= dn(q)], the recurrence (39) becomes

n∑

i=0
 [n
i
 ]di = [n]!,

which characterizes the q-derangement numbers of Wachs [36, p. 277]. Here [n
i ]

and [n]! are the q-analogues of (
n
i ) and n!, respectively. The inverted form of this
as in (42) is
 dn =
 n∑

i=0(−1)
i[n
i
 ][n − i]!q(i
2) = [n]!
 n∑

i=0
 (−1)
i

[i]! q(i
2);

see [36, Theorem 4]. Finally, Proposition 10 reads

d0 = 1

dn =
 n−1∑

i=0
 [
n
i
 ]([n − i] − 1)di (n > 0),

where [n − i] is the q-analogue of n − i.

SEMIGROUPS, RINGS, AND MARKOV CHAINS 45

Example 3 (A graph invariant). Let L = L(G) be the lattice of contractions of
a simple ﬁnite graph G, as discussed in Section 6.3. Set f (G) = f (L(G)) and
d(G) = d(L(G)). Thus f (G) is the number of collapsing sequences of G and d(G)
is some new invariant of G, deﬁned by
∑

¯G d( ¯G) = f (G),

where the sum is taken over all collapsings ¯G = G/Π. The inverted form is

d(G) = ∑

Π∈L(G) µ(ˆ0, Π)f (G/Π).

The numbers µ(ˆ0, Π) that occur here are familiar from Rota’s formula for the chro-
matic polynomial of G [34, Chapter 3, Exercise 44]: One has

χG(x) = ∑

Π∈L(G) µ(ˆ0, Π)x
|Π|.

Finally, Proposition 10 gives

d(G) = 1 if G is discrete

d(G) = ∑

Π<ˆ1
(e(G/Π) − 1)d(GΠ) otherwise,

where e( ) denotes the number of edges of a graph and GΠ ⊂ G is the union of the
subgraphs induced by the blocks of Π.

C.3. Connection with the ﬂag h-vector. The result of this subsection (Propo-
sition 11) is due to Richard Stanley and is included with his permission.
The ordinary derangement number dn has the following interpretation, due to
D´esarm´enien [12] (see also [13] and further references cited there): Call a per-
mutation π ∈ Sn a desarrangement if the maximal initial descending sequence
π(1) > π(2) > · · · > π(l) has even length l; then dn is the number of desarrange-
ments. D´esarm´enien gave a bijective proof of this assertion and used it to give a
combinatorial proof of the recurrence (45). One can also reverse the process and
deduce D´esarm´enien’s result from (45), by induction on n.
The result can be phrased in terms of descent sets. Recall that π is said to have a
descent at i if π(i) > π(i + 1), where 1 ≤ i ≤ n − 1. For J ⊆ [n − 1] = {1, . . . , n − 1},
let β(J) be the number of permutations in Sn with descent set J. Let J be the
family of sets J such that the ﬁrst integer l ≥ 1 not in J is even. Then D´esarm´enien’s
interpretation of dn is
 dn = ∑

J⊆[n−1]
J∈J
 β(J).(46)

We wish to generalize this. The role of the descent numbers β(J) is played by the
components of the ﬂag h-vector. We brieﬂy recall the deﬁnition of the latter; for
more information, see [33, Section III.4], [34, Sections 3.12 and 3.8], or [8].
Let L be a graded poset with ˆ0, ˆ1; thus all maximal chains have the same length
n, called the rank of L. For J ⊆ [n − 1], let fJ (L) be the number of ﬂags in L of
type J, where the type of a ﬂag X1 < X2 < · · · < Xl is the set {rank Xi}1≤i≤l.

46 KENNETH S. BROWN

These numbers are the components of the ﬂag f -vector of L. The ﬂag h-vector is
deﬁned by
 hJ (L) = ∑

K⊆J(−1)
|J−K|fK(L),(47)

or, equivalently,
 fJ (L) = ∑

K⊆J hK(L).(48)

Up to sign, hJ (L) is the reduced Euler characteristic of the rank-selected subposet
LJ of L. More precisely,
 hJ (L) = (−1)
|J|−1 ˜χ(LJ ).(49)

If the order complex of LJ is homotopy equivalent to a wedge of (|J| − 1)-spheres,
then hJ (L) is the number of spheres.
For the Boolean lattice, one can see from (48) that hJ (L) is equal to the descent
number β(J). This is also a special case of Proposition 5 (Section 9.4). The main
result of this subsection, generalizing (46), is the following proposition.

Proposition 11 (Stanley, private communication). Let L be a graded poset with
ˆ0, ˆ1, and let n be its rank. Then

d(L) = ∑

J⊆[n−1]
J∈J
 hJ (L).(50)

Proof. Let d
′(L) denote the right-hand side of (50) if L ̸= 0, and let d
′(0) = 1. It
suﬃces to show that d
′ satisﬁes the recurrence (43), i.e.,

d
′(L) = µL(ˆ0, ˆ1) + ∑

X∈M d
′([ˆ0, X]),(51)

where M is the set of elements of L of rank n − 1. We may assume n ≥ 2. Group
the terms on the right-hand side of (50) in pairs, where J ⊆ [n − 2] is paired
with J+ = J ∪ {n − 1}. This leaves one term unpaired: If n is even, we have
[n − 1] = [n − 2]+ ∈ J but [n − 2] /∈ J , while the reverse is true if n is odd. In both
cases we obtain

d
′(L) = (−1)
nh[n−1](L) + ∑

J⊆[n−2]
J∈J
 (
hJ (L) + hJ+(L)
) .(52)

Two simple observations now complete the proof of (51). The ﬁrst is that

(−1)
nh[n−1](L) = µL(ˆ0, ˆ1)

by (49) with J = [n − 1]. The second observation is that

hJ (L) + hJ+(L) = ∑

X∈M hJ ([ˆ0, X])

for J ⊆ [n − 2]. This is proved by expanding both terms on the left-hand side
by (47), noting that many terms cancel, and applying the following fact to the
remaining terms:
 fK+ (L) = ∑

X∈M fK([ˆ0, X])

for K ⊆ [n − 2].
 SEMIGROUPS, RINGS, AND MARKOV CHAINS 47

Michelle Wachs [private communication] has pointed out that Proposition 11
implies the following result about q-derangement numbers, due to D´esarm´enien
and Wachs [13, Section 7]:

Corollary. The q-derangement number dn(q) satisﬁes

dn(q) = ∑

π∈En qinv(π),

where En is the set of desarrangements in Sn and inv(π) is the number of inversions
of π.

Proof. Take L to be the subspace lattice of Fn
q , so that d(L) = dn(q). It is known
[34, Theorem 3.12.3] that
 hJ (L) = ∑

π∈Sn
des(π)=J
 qinv(π).

The corollary now follows at once from the proposition.

C.4. More on the ﬂag h-vector. Going back to the random walk on maximal
chains for motivation, recall that there is an eigenvalue λX for each X ∈ L (where
L is the lattice of ﬂats of a matroid), with multiplicity mX = d([X, ˆ1]). We have
just seen that this multiplicity is a sum of certain components of the ﬂag h-vector
when X = ˆ0. Is the same true of the other multiplicities? This is a reasonable
question since ∑

X∈L mX = f (L) = ∑

J⊆[n−1] hJ (L).

One might naively hope to lump the terms on the right-hand-side in such a way
that each lump accounts for one mX . This does not seem to be the case; but what
is true is that if we lump together all the mX with X of a given rank, then their
sum is equal to the sum of the hJ for certain sets J. This was observed by Swapneel
Mahajan [private communication]. It is of interest for the random walk in case L
has the property that all ﬂats of a given rank contain the same number of rank 1
ﬂats. If, further, we take uniform weights on the rank 1 ﬂats, then we get one
eigenvalue for each possible rank r, 0 ≤ r ≤ n = rank(L), the multiplicity being

Dn−r(L) := ∑

rank(X)=r d([X, ˆ1]).

(The subscript n − r is a reminder that each interval [X, ˆ1] on the right has rank
n − r.) Mahajan’s result, then, is that Dn−r(L) is a sum of certain values of the
ﬂag h-vector. This is valid for every graded poset with ˆ0, ˆ1. When r = 0 it reduces
to Stanley’s result from the previous section.
To state the result precisely, we associate to every set J ⊆ [n − 1] a number
γ = γ(J), 0 ≤ γ ≤ n, as follows. Arrange the elements of J in order, and consider
the initial run of consecutive integers; this has the form i, i + 1, . . . , i + l − 1, where
l is the length of the run. We allow the case J = ∅, in which case we set l = 0 and
i = n. Then γ is deﬁned by
γ(J) =
 {i if l is even
i − 1 if l is odd.

48 KENNETH S. BROWN

The result, then, is:

Proposition 12 (Mahajan, private communication). If L is a graded poset with
ˆ0, ˆ1 and n = rank(L), then
 Dn−r(L) = ∑

γ(J)=r hJ (L).

We omit the proof. The starting point is to apply Proposition 11 to each of the
posets [X, ˆ1].
For our random walk, the proposition says that the total multiplicity of the
eigenvalues contributed by the X ∈ L of rank r is given by the components of the
ﬂag h-vector with γ(J) = r.
Here are some special cases.
• r = 0: We have γ(J) = 0 if and only if the initial run in J is 1, . . . , l with l
odd, so the ﬁrst omitted integer is even, as in Proposition 11.
• r = n − 1: There is no J with γ(J) = n − 1, so D1(L) = 0. This is consistent
with the fact that d = 0 for posets of rank 1.
• r = n: The only J with γ(J) = n is J = ∅, so D0(L) = h∅(L) = 1. This is
consistent with the fact that d = 1 for the trivial poset.

References

[1] Herbert Abels, The geometry of the chamber system of a semimodular lattice, Order 8 (1991),
no. 2, 143–158.
[2] David Aldous, The Moran process as a Markov chain on leaf-labeled trees, preprint, 1999.
[3] Dave Bayer and Persi Diaconis, Trailing the dovetail shuﬄe to its lair, Ann. Appl. Probab.
2 (1992), no. 2, 294–313.
[4] Fran¸cois Bergeron, Nantel Bergeron, Robert B. Howlett, and Donald E. Taylor, A decompo-
sition of the descent algebra of a ﬁnite Coxeter group, J. Algebraic Combin. 1 (1992), no. 1,
23–44.
[5] T. Patrick Bidigare, Hyperplane arrangement face algebras and their associated Markov
chains, Ph.D. thesis, University of Michigan, 1997.
[6] T. Patrick Bidigare, Phil Hanlon, and Daniel N. Rockmore, A combinatorial description of
the spectrum for the Tsetlin library and its generalization to hyperplane arrangements, Duke
Math. J. 99 (1999), no. 1, 135–174.
[7] Louis J. Billera, Kenneth S. Brown, and Persi Diaconis, Random walks and plane arrange-
ments in three dimensions, Amer. Math. Monthly 106 (1999), no. 6, 502–524.
[8] Louis J. Billera and Niandong Liu, Noncommutative enumeration in graded posets, J. Alge-
braic Combin., to appear.
[9] Anders Bj¨orner, Michel Las Vergnas, Bernd Sturmfels, Neil White, and G¨unter M. Ziegler,
Oriented matroids, Encyclopedia of Mathematics and its Applications, vol. 46, Cambridge
University Press, Cambridge, 1993.
[10] Kenneth S. Brown, Buildings, Springer-Verlag, New York, 1989.
[11] Kenneth S. Brown and Persi Diaconis, Random walks and hyperplane arrangements, Ann.
Probab. 26 (1998), no. 4, 1813–1854.
[12] Jacques D´esarm´enien, Une autre interpr´etation du nombre de d´erangements, S´em. Lothar.
Combin. 8 (1983), Art. B08b, 6 pp. (electronic).
[13] Jacques D´esarm´enien and Michelle L. Wachs, Descent classes of permutations with a given
number of ﬁxed points, J. Combin. Theory Ser. A 64 (1993), no. 2, 311–328.
[14] Persi Diaconis, From shuﬄing cards to walking around the building: An introduction to mod-
ern Markov chain theory, Proceedings of the 1998 International Congress of Mathematicians,
to appear.
[15] , Group representations in probability and statistics, Institute of Mathematical Statis-
tics Lecture Notes—Monograph Series, vol. 11, Institute of Mathematical Statistics, Hayward,
CA, 1988.
 SEMIGROUPS, RINGS, AND MARKOV CHAINS 49

[16] Persi Diaconis, James Allen Fill, and Jim Pitman, Analysis of top to random shuﬄes, Com-
bin. Probab. Comput. 1 (1992), no. 2, 135–155.
[17] Persi Diaconis and David Freedman, Iterated random functions, SIAM Rev. 41 (1999), no. 1,
45–76 (electronic).
[18] James Allen Fill, An exact formula for the move-to-front rule for self-organizing lists, J.
Theoret. Probab. 9 (1996), no. 1, 113–160.
[19] Curtis Greene, On the M¨obius algebra of a partially ordered set, Advances in Math. 10 (1973),
177–187.
[20] Pierre Antoine Grillet, Semigroups. an introduction to the structure theory, Monographs and
Textbooks in Pure and Applied Mathematics, vol. 193, Marcel Dekker Inc., New York, 1995.
[21] Larry C. Grove and Clark T. Benson, Finite reﬂection groups, second ed., Graduate Texts
in Mathematics, vol. 99, Springer-Verlag, New York, 1985.
[22] G¨oran H¨ogn¨as and Arunava Mukherjea, Probability measures on semigroups, Plenum Press,
New York, 1995, Convolution products, random walks, and random matrices.
[23] James E. Humphreys, Reﬂection groups and Coxeter groups, Cambridge Studies in Advanced
Mathematics, vol. 29, Cambridge University Press, Cambridge, 1990.
[24] Fritz Klein-Barmen, ¨Uber eine weitere Verallgemeinerung des Verbandsbegriﬀes, Math. Z.
46 (1940), 472–480.
[25] Peter Orlik and Hiroaki Terao, Arrangements of hyperplanes, Grundlehren der Mathematis-
chen Wissenschaften, vol. 300, Springer-Verlag, Berlin, 1992.
[26] Mario Petrich, A construction and a classiﬁcation of bands, Math. Nachr. 48 (1971), 263–274.
[27] , Lectures in semigroups, John Wiley & Sons, London-New York-Sydney, 1977.
[28] Ravindra M. Phatarfod, On the matrix occurring in a linear search problem, J. Appl. Probab.
28 (1991), no. 2, 336–346.
[29] Maurice-Paul Sch¨utzenberger, Sur certains treillis gauches, C. R. Acad. Sci. Paris 224 (1947),
776–778.
[30] Jean-Pierre Serre, Linear representations of ﬁnite groups, Springer-Verlag, New York, 1977,
Translated from the second French edition by Leonard L. Scott, Graduate Texts in Mathe-
matics, Vol. 42.
[31] Louis Solomon, The Burnside algebra of a ﬁnite group, J. Combinatorial Theory 2 (1967),
603–615.
[32] , A Mackey formula in the group ring of a Coxeter group, J. Algebra 41 (1976), no. 2,
255–264.
[33] Richard P. Stanley, Combinatorics and commutative algebra, second ed., Progress in Math-
ematics, vol. 41, Birkh¨auser Boston Inc., Boston, MA, 1996.
[34] , Enumerative combinatorics. Vol. 1, Cambridge Studies in Advanced Mathematics,
vol. 49, Cambridge University Press, Cambridge, 1997, with a foreword by Gian-Carlo Rota,
corrected reprint of the 1986 original.
[35] Jacques Tits, Buildings of spherical type and ﬁnite BN-pairs, Springer-Verlag, Berlin, 1974,
Lecture Notes in Mathematics, Vol. 386.
[36] Michelle L. Wachs, On q-derangement numbers, Proc. Amer. Math. Soc. 106 (1989), no. 1,
273–278.
[37] Dominic J. A. Welsh, Matroid theory, Academic Press [Harcourt Brace Jovanovich Publish-
ers], London, 1976, L. M. S. Monographs, No. 8.
[38] Hassler Whitney, On the abstract properties of linear dependence, Amer. J. Math. (1935),
509–533, Collected Papers, vol. I, 147–171.
[39] Thomas Zaslavsky, Facing up to arrangements: face-count formulas for partitions of space
by hyperplanes, Mem. Amer. Math. Soc. 1 (1975), no. 154, vii+102 pp.
[40] , A combinatorial analysis of topological dissections, Advances in Math. 25 (1977),
no. 3, 267–285.
[41] G¨unter M. Ziegler, Lectures on polytopes, Graduate Texts in Mathematics, vol. 152, Springer-
Verlag, New York, 1995.

Department of Mathematics, Cornell University, Ithaca, NY 14853
E-mail address: kbrown@math.cornell.edu
