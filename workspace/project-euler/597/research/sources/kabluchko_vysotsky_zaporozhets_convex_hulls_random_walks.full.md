<!-- source: https://arxiv.org/pdf/1612.00249 | converted from PDF -->

arXiv:1612.00249v3  [math.PR]  21 Aug 2017
CONVEX HULLS OF RANDOM WALKS: EXPECTED NUMBER OF
FACES AND FACE PROBABILITIES

ZAKHAR KABLUCHKO, VLADISLAV VYSOTSKY, AND DMITRY ZAPOROZHETS

Abstract. Consider a sequence of partial sums Si = ξ1 + · · · + ξi, 1 ≤ i ≤ n, starting at
S0 = 0, whose increments ξ1, . . . , ξn are random vectors in Rd, d ≤ n. We are interested
in the properties of the convex hull Cn := Conv(S0, S1, . . . , Sn). Assuming that the tuple
(ξ1, . . . , ξn) is exchangeable and a certain general position condition holds, we prove that
the expected number of k-dimensional faces of Cn is given by the formula

E[fk(Cn)] = 2 · k!
n!
 ∞∑

l=0
 [ n + 1
d − 2l
]{d − 2l
k + 1
 }
,

for all 0 ≤ k ≤ d − 1, where [ n
m] and { n
m} are Stirling numbers of the ﬁrst and second kind,
respectively.
Further, we compute explicitly the probability that for given indices 0 ≤ i1 < · · · < ik+1 ≤
n, the points Si1 , . . . , Sik+1 form a k-dimensional face of Conv(S0, S1, . . . , Sn). This is done
in two diﬀerent settings: for random walks with symmetrically exchangeable increments
and for random bridges with exchangeable increments. These results generalize the classical
one-dimensional discrete arcsine law for the position of the maximum due to E. Sparre
Andersen. All our formulae are distribution-free, that is do not depend on the distribution
of the increments ξk’s.
The main ingredient in the proof is the computation of the probability that the origin is
absorbed by a joint convex hull of several random walks and bridges whose increments are
invariant with respect to the action of direct product of ﬁnitely many reﬂection groups of
types An−1 and Bn. This probability, in turn, is related to the number of Weyl chambers of
a product-type reﬂection group that are intersected by a linear subspace in general position.

2010 Mathematics Subject Classiﬁcation. Primary: 52A22, 60D05, 60G50; secondary: 60G09, 52C35,
20F55, 52B11, 60G70.
Key words and phrases. Convex hull, random walk, random walk bridge, absorption probability,
distribution-free probability, exchangeability, hyperplane arrangement, Whitney’s formula, Zaslavsky’s theo-
rem, characteristic polynomial, Weyl chamber, ﬁnite reﬂection group, convex cone, Wendel’s formula, random
polytope, average number of faces, average number of vertices, discrete arcsine law.
This paper was written when V.V. was aﬃliated to Imperial College London, where his work was supported
by People Programme (Marie Curie Actions) of the European Union’s Seventh Framework Programme
(FP7/2007-2013) under REA grant agreement n
◦[628803]. His work is also supported in part by Grant 16-
01-00367 by RFBR. The work of D.Z. is supported in parts by Grant 16-01-00367 by RFBR, the Program of
Fundamental Researches of Russian Academy of Sciences “Modern Problems of Fundamental Mathematics”,
and by Project SFB 1283 of Bielefeld University. 1

2 ZAKHAR KABLUCHKO, VLADISLAV VYSOTSKY, AND DMITRY ZAPOROZHETS

1. Statement of main results

1.1. Introduction. Let ξ1, . . . , ξn be (possibly dependent) random d-dimensional vectors
with partial sums Si = ξ1 + · · · + ξi, 1 ≤ i ≤ n, S0 = 0.
The sequence S0, S1, . . . , Sn will be referred to as random walk or, if the additional boundary
condition Sn = 0 is imposed, a random bridge.
In the one-dimensional case d = 1, Sparre Andersen [23, 24, 25] derived remarkable
formulae for several functionals of the random walk S0, S1, . . . , Sn including the number of
positive terms and the position of the maximum. More speciﬁcally, assuming that the joint
distribution of the increments (ξ1, . . . , ξn) is invariant under arbitrary permutations and sign
changes and that P[Si = 0] = 0 for all 1 ≤ i ≤ n, Sparre Andersen proved in [25, Theorem C]
the following discrete arcsine law for the position of the maximum:

P [max{S0, . . . , Sn} = Si] = 1
22n
 (2i
i
 )(
2n − 2i
n − i
 ), i = 0, . . . , n. (1)

By the symmetry, the same holds for the position of the minimum. Surprisingly, the above
formula is distribution-free, that is its right-hand side does not depend on the distribution
of (ξ1, . . . , ξn) provided the symmetric exchangeability and the general position assumptions
mentioned above are satisﬁed. Another unexpected consequence of this formula is that the
maximum is more likely to be attained at i = 0 or i = n rather than at i ≈ n/2, as one
could na¨ıvely guess. A discussion of the arcsine laws can be found in Feller’s book [6, Vol II,
Section XII.8].
Let us now turn to the general d-dimensional case and ask ourselves what could be an
appropriate multidimensional generalization of (1). Of course, the maximum and the mini-
mum are not well deﬁned for multidimensional random walks, but instead we can consider
vertices (and, more generally, faces) of the convex hull

Cn := Conv(S0, S1, . . . , Sn) = {α0S0 + · · · + αnSn : α0, . . . , αn ≥ 0, α0 + · · · + αn = 1}.

Clearly, Cn is a random polytope in Rd whose vertices belong to the collection {S0, S1, . . . , Sn}.
In the one-dimensional case, Cn has two vertices, the maximum and the minimum, but in
higher dimensions the question on the number of vertices (or, more generally, faces) and
their positions becomes non-trivial. The main results of the present paper can be summa-
rized as follows. Under the appropriate exchangeability and general position assumptions on
the random walk or bridge, we compute
(a) the expected number of k-dimensional faces of Cn, for all 0 ≤ k ≤ d − 1, and
(b) the probability that the simplex Conv(Si1, . . . , Sik+1) is a k-dimensional face of the
convex hull Cn, for a given collection of indices 0 ≤ i1 < · · · < ik+1 ≤ n.
All formulae turn out to be distribution-free. The probabilities in (b), referred to as
face probabilities, will be interpreted below in terms of the so-called absorption probabilities,
that is the probabilities that a joint convex hull of several random walks and random bridges
contains the origin. In our recent work [13], we showed that in the case of just one random
walk or bridge, the absorption probability can be computed in a purely geometric way by
counting the number of Weyl chambers of a certain reﬂection group that are intersected

CONVEX HULLS OF RANDOM WALKS 3

by a linear subspace in general position. Moreover, we showed in [13] that random walks
correspond to Weyl chambers of type Bn, whereas random bridges correspond to type An−1
chambers. In the present paper, we extend the results of [13] to joint convex hulls of several
random walks and bridges. We shall show that the corresponding absorption probabilities
can be interpreted in terms of Weyl chambers of product type. Our main formula for the
absorption probabilities will be stated in Theorem 2.1, below.
We shall argue below that (b) can be viewed as a generalization of the discrete arcsine
law to higher dimensions. Let us mention that there is another discrete arcsine law, also due
to Sparre Andersen [25, Theorem C], for the number of positive terms in a random walk. A
multidimensional generalization of this result is considered in our separate paper [12].
Convex hulls of random walks and their applications to Brownian motions and L´evy
processes were much studied; see, e.g., [2, 3, 5, 14, 15, 16, 17, 22, 26, 29, 30]. These
papers concentrate mostly on functionals like the volume and the perimeter, which are
not distribution-free. Face probabilities for faces of maximal dimension were computed by
Barndorﬀ-Nielsen and Baxter [2] and Vysotsky and Zaporozhets [29]. We shall recover the
corresponding formula as a special case of our results, but our methods are diﬀerent from
that of [2, 29]. Reviews of the literature on random convex hulls and random polytopes can
be found in [9, 16, 21].

1.2. Expected number of k-faces. Recall that Cn = Conv(S0, . . . , Sn) denotes the convex
hull of a d-dimensional random walk (Si)n
i=0 with increments ξ1, . . . , ξn. The increments are
random vectors which may be dependent. Our ﬁrst result is a formula for the expected
number of k-dimensional faces of Cn. To state it, we need to impose the following assumptions
on the joint distribution of the increments.
(Ex) Exchangeability: For every permutation σ of the set {1, . . . , n}, we have the distri-
butional equality (ξσ(1), . . . , ξσ(n)) d
= (ξ1, . . . , ξn).
(GP) General position: For every 1 ≤ i1 < · · · < id ≤ n, the probability that the vectors
Si1, . . . , Sid are linearly dependent is 0.

Example 1.1. Conditions (Ex) and (GP) are satisﬁed if ξ1, . . . , ξn are independent iden-
tically distributed, and for every hyperplane H0 ⊂ Rd passing through the origin we have
P[Si ∈ H0] = 0, for all 1 ≤ i ≤ n. The proof of (GP) can be found in [13, Proposition 2.5],
while the proof of (Ex) is trivial. The assumption P[Si ∈ H0] = 0, 1 ≤ i ≤ n, in turn follows
(for i.i.d. increments) if we assume that P[ξ1 ∈ H] = 0 for every aﬃne hyperplane H ⊂ Rd;
this is again shown in the proof of [13, Proposition 2.5]. To clarify, the proposition addition-
ally assumes (although does not state explicitly in the published version) that ξ1 d
= −ξ1, but
this is not required for the implications mentioned above.

Denote by Fk(C), where 0 ≤ k ≤ d−1, the set of all k-dimensional faces (or just k-faces,
in short) of a convex polytope C. Let fk(C) be the number of k-faces of C:

fk(C) := #Fk(C).

Note that under assumption (GP), all faces of Cn are simplices with probability 1; see
Remark 1.5, below for a proof.

4 ZAKHAR KABLUCHKO, VLADISLAV VYSOTSKY, AND DMITRY ZAPOROZHETS

Theorem 1.2. Let (Si)n
i=0 be a random walk in Rd, n ≥ d, whose increments ξ1, . . . , ξn
satisfy conditions (Ex) and (GP). Then, for all 0 ≤ k ≤ d − 1,

E[fk(Cn)] = 2 · k!
n!
 ∞∑

l=0
 [ n + 1
d − 2l
]{d − 2l
k + 1
 }
. (2)

The right-hand side contains the (signless) Stirling numbers of the ﬁrst kind [ n
m
] and the
Stirling numbers of the second kind { n
m}
, where m, n ∈ N and 1 ≤ m ≤ n, which are deﬁned
as the number of permutations of an n-element set with exactly m cycles and the number
of partitions of an n-element set into m non-empty subsets, respectively. The exponential
generating functions of the Stirling numbers are given by

∞∑

n=m
 [ n
m

] t
n

n! = 1
m!
 (log 1
1 − t
)m ,
 ∞∑

n=m
 { n
m

} t
n

n! = 1
m! (e
t − 1)m. (3)

For these and other properties of Stirling numbers, we refer to [7, Chapters 6 and 7]. For
n ∈ N, m ∈ Z\{1, . . . , n} and n /∈ N we use the convention [ n
m] = { n
m
} = 0, so that the sum
in (2) contains only ﬁnitely many non-vanishing terms. The Stirling numbers of the ﬁrst
kind can also be deﬁned as the coeﬃcients of the rising factorial

t
(n) := t(t + 1)(t + 2) . . . (t + n − 1) =
 n∑

j=0
 [n
j
 ]
t
j. (4)

Remark 1.3. Let us mention some special cases of Theorem 1.2. For faces of maximal
dimension (where k = d − 1 and only the term with l = 0 is present) and vertices (where
k = 0), formula (2) simpliﬁes to

E [fd−1(Cn)] = 2(d − 1)!
n!
 [
n + 1
d
 ], E [f0(Cn)] = 2
n!
 ∞∑

l=0
 [ n + 1
d − 2l
],

where we used the identities {
d
d
} = 1 and {
d−2l
1 } = 1 (for d − 2l ≥ 1). For example, in
dimension d = 2, both the expected number of edges and the expected number of vertices
of the random polygon Cn are equal to 2Hn := 2 (
1 + 1
2 + · · · + 1
n ) since [
n+1
2 ] = n!Hn. This
result was known [3, 29]. In dimension d = 1 we recover the trivial formula E [f0(Cn)] = 2,
which accounts the two vertices being the maximum and the minimum of the random walk,
since [n+1
1 ] = n!.

Remark 1.4. Using the ﬁxed k asymptotic formula for Stirling numbers of the ﬁrst kind,
see [11, page 160] (or [32] for much more precise asymptotics), namely

1
(n − 1)!
 [
n
k
] ∼ (log n)k−1

(k − 1)! , n → ∞, k ﬁxed, (5)

we obtain
 E [fk(Cn)] ∼ 2 · k!
(d − 1)!
 { d
k + 1

}(log n)d−1, n → ∞, k, d ﬁxed. (6)

CONVEX HULLS OF RANDOM WALKS 5

Here, an ∼ bn means that limn→∞ an/bn = 1. Interestingly, the same asymptotics (up to a
constant factor) holds for the expected number of k-faces of the convex hull of n i.i.d. points
uniformly distributed in a d-dimensional convex polytope; see [20].

Remark 1.5. Under assumptions (Ex) and (GP), each face g ∈ Fk(Cn) of the polytope Cn
is, with probability 1, a k-dimensional simplex of the form

g = Conv(Sj1(g), . . . , Sjk+1(g))

for some indices 0 ≤ j1(g) < · · · < jk+1(g) ≤ n. It suﬃces to prove this for k = d − 1 because
all faces of a simplex are simplices. For all 0 ≤ i1 < · · · < id+1 ≤ n we have

P[Si1, . . . , Sid+1 are contained in a common hyperplane]

= P[Si2 − Si1, Si3 − Si1, . . . , Sid+1 − Si1 are linearly dependent]

= P[Si2−i1, Si3−i1, . . . , Sid+1−i1 are linearly dependent]
= 0

by assumptions (Ex) and (GP). It follows that, with probability 1, every (d − 1)-dimensional
face of Cn contains at most d vertices and, consequently, is a simplex.

1.3. Face probabilities for symmetric random walks. In the next theorem we compute
the probability that a given collection of points of the random walk forms a face of the convex
polytope Cn. To state it, we need an assumption which, in addition to exchangeability,
requires invariance with respect to sign changes:
(±Ex) Symmetric exchangeability: For every permutation σ of the set {1, . . . , n} and every
ε1, . . . , εn ∈ {−1, +1}, there is the distributional equality

(ξ1, . . . , ξn) d
= (ε1ξσ(1), . . . , εnξσ(n)).

Random walks satisfying (±Ex) will be frequently referred to as symmetric. For exam-
ple, (±Ex) is satisﬁed if ξ1, . . . , ξn are i.i.d. random vectors in Rd with centrally symmetric
distribution (meaning that ξ1 has the same distribution as −ξ1).

Theorem 1.6. Let (Si)n
i=0 be a random walk in Rd whose increments ξ1, . . . , ξn satisfy as-
sumptions (±Ex) and (GP). Fix some 0 ≤ k ≤ d − 1 and let 0 ≤ i1 < · · · < ik+1 ≤ n be any
indices. Then,

P[Conv(Si1, . . . , Sik+1) ∈ Fk(Cn)] = 2(P (n)
i1,...,ik+1(d − k − 1) + P (n)
i1,...,ik+1(d − k − 3) + . . . )

2i1+n−ik+1i1!(i2 − i1)! . . . (ik+1 − ik)!(n − ik+1)! ,

where the P (n)
i1,...,ik+1(j)’s are the coeﬃcients of the polynomial

(t + 1)(t + 3) . . . (t + 2i1 − 1) × (t + 1)(t + 3) . . . (t + 2(n − ik+1) − 1)

×
 k∏

l=1((t + 1)(t + 2) . . . (t + il+1 − il − 1)) =
 n−k∑

j=0 P (n)
i1,...,ik+1(j)t
j.

For j < 0 or j > n − k we use the convention P (n)
i1,...,ik+1(j) := 0.

6 ZAKHAR KABLUCHKO, VLADISLAV VYSOTSKY, AND DMITRY ZAPOROZHETS

Remark 1.7. Take some 0 ≤ i ≤ n. For the probability that Si is a vertex of the convex hull
Cn, we obtain, by taking k = 0 in Theorem 1.6,

P[Si ∈ F0(Cn)] = P (n)
i (d − 1) + P (n)
i (d − 3) + . . .
2n−1i!(n − i)! , (7)

where the P (n)
i (j)’s are the coeﬃcients of the polynomial

(t + 1)(t + 3) . . . (t + 2i − 1) × (t + 1)(t + 3) . . . (t + 2(n − i) − 1) =
 n∑

j=0 P (n)
i (j)t
j. (8)

In the one-dimensional case d = 1, the convex hull is the interval

Cn = [ min
i=0,...,n Si, max
i=0,...,n Si
] ,

so (by symmetry of the increments) the probability that Si is a vertex of Cn is just twice the
probability that Si is the maximum. Therefore, (7) and (8) yield

P[max{S0, . . . , Sn} = Si] = 1
22n
 (
2i
i
 )(
2n − 2i
n − i
 ) = (2i − 1)!!(2n − 2i − 1)!!
(2i)!!(2n − 2i)!! , (9)

for all i = 0, . . . , n, which recovers the discrete arcsine law for the position of the maximum
due to Sparre Andersen [25, Theorem C], see also [6, Vol II, Section XII.8]. Thus, we can
view Theorem 1.6 as a multidimensional generalization of the discrete arcsine law.

Remark 1.8. For faces of maximal possible dimension k = d−1, Theorem 1.6 (with only non-
zero term P (n)
i1,...,id(0) in the numerator) recovers a formula of Vysotsky and Zaporozhets [29]:

P[Conv(Si1, . . . , Sid) ∈ Fd−1(Cn)] = 2 (2i1 − 1)!!
(2i1)!! (2n − 2id − 1)!!
(2n − 2id)!!
 d−1∏

j=1
 1
ij+1 − ij .

Remark 1.9. The coeﬃcients P (n)
i1,...,ik+1(j) admit the following probabilistic interpretation.
Consider the random variables

Kn :=1A1 +1A2 + · · · +1An, Ln :=1A2 +1A4 + · · · +1A2n, n ∈ N,

where A1, A2, . . . are independent events with P[Am] = 1/m, m ∈ N. The generating
functions of Kn and Ln are given by

Et
Kn = t(t + 1) . . . (t + n − 1)
n! , Et
Ln = (t + 1)(t + 3) . . . (t + 2n − 1)
2nn! .

It is well known that the number of cycles of a uniform random permutation on n
elements has the same distribution as Kn. This can be deduced from the connection between
random uniform permutations and the Chinese restaurant process; see [19, Section 3.1]. To
give a similar interpretation of Ln, consider the group of signed permutations of the set
{1, . . . , n}. Any such permutation can be written in the form

Σ = ( 1 2 . . . n
ε1σ(1) ε2σ(2) . . . εnσ(n)
) ,

CONVEX HULLS OF RANDOM WALKS 7

where σ is a permutation on {1, . . . , n} and ε1, . . . , εn ∈ {−1, +1}. The permutation σ can
be decomposed into cycles. We call a cycle w1 → w2 → · · · → wr → w1 of σ an even cycle
of the signed permutation Σ if εw1 . . . εwr = +1, i.e. if making a full turn along the cycle
does not change the sign. Clearly, for a uniformly chosen random signed permutation, any
cycle is even with probability 1/2, independently of all other cycles. This implies that the
number of even cycles has the same distribution as Ln. The symmetric group and the group
of signed permutations, acting on Rn as the reﬂection groups An−1 and Bn, will play a major
role in our proofs.
Let us now return to Theorem 1.6. Let L
(0)
i1 , K (1)
i2−i1, . . . , K (k)
ik+1−ik, L
(k+1)
n−ik+1 be indepen-
dent random variables with the same distributions as Li1, Ki2−i1, . . . , Kik+1−ik, Ln−ik+1, re-
spectively. Then Theorem 1.6 states that

P[Conv(Si1, . . . , Sik+1) ∈ Fk(Cn)] = 2
 ∞∑

l=0 P[L
(0)
i1 +K (1)
i2−i1 +· · ·+K (k)
ik+1−ik +L
(k+1)
n−ik+1 = d−2l−1].

Thus, the faces probabilities are similar to the distribution functions of the total number of
cycles in a set of independent random permutations of the appropriate types.

Example 1.10. In a sharp contrast with Theorem 1.2, the assumption of symmetric ex-
changeability is essential in Theorem 1.6. To see this, consider i.i.d. standard normal random
vectors η1, . . . , ηn in Rd and deﬁne

ξ1(t) := 1 + tη1, . . . , ξn(t) := 1 + tηn, t > 0.

Clearly, the random vectors ξ1(t), . . . , ξn(t) satisfy assumptions (Ex) and (GP) for all t > 0.
On the other hand, the corresponding random walk Si(t) := ξ1(t) + · · · + ξi(t), 1 ≤ i ≤ n,
starting at S0(t) := 0 satisﬁes

p(t) := P[S0(t) is a vertex of Conv(S0(t), . . . , Sn(t))] = P[0 /∈ Conv(S1(t), . . . , Sn(t))],

which converges to 1 as t → 0 because1{0∈Conv(S1(t),...,Sn(t))} → 0 a.s. as t → 0. It follows
that p(t) cannot be given by (7) for suﬃciently small t. The reason is the lack of central
symmetry of the distribution of increments.

1.4. Face probabilities for random bridges. Random bridges are essentially random
walks required to return to the origin after n steps. Formally, let ξ1, . . . , ξn be (in general,
dependent) random vectors in Rd with partial sums Si = ξ1 + · · · + ξi, 1 ≤ i ≤ n, and S0 = 0.
We impose the following assumptions on the increments ξ1, . . . , ξn:
(Br) Bridge property: Sn = ξ1 + · · · + ξn = 0 a.s.
(Ex) Exchangeability: For every permutation σ of the set {1, . . . , n}, we have the distri-
butional equality
 (ξσ(1), . . . , ξσ(n)) d
= (ξ1, . . . , ξn).

(GP
′) General position: For every 1 ≤ i1 < · · · < id ≤ n − 1, the probability that the
vectors Si1, . . . , Sid are linearly dependent, is 0.
The bridge starts and terminates at the origin: S0 = Sn = 0 a.s. Let us stress that, unlike in
the case of random walks, we don’t need any central symmetry assumption on the increments.

8 ZAKHAR KABLUCHKO, VLADISLAV VYSOTSKY, AND DMITRY ZAPOROZHETS

As above, we denote by Cn = Conv(S0, . . . , Sn) the convex hull of S0, . . . , Sn and by Fk(Cn)
the set of its k-faces, where 0 ≤ k ≤ d − 1.

Theorem 1.11. Let (Si)n
i=0 be a random bridge in Rd whose increments ξ1, . . . , ξn satisfy the
above assumptions (Br), (Ex), (GP
′). Fix some 0 ≤ k ≤ d−1 and let 0 ≤ i1 < · · · < ik+1 < n
be any indices. Then,

P[Conv(Si1, . . . , Sik+1) ∈ Fk(Cn)] = 2(Q
(n)
i1,...,ik+1(d − k − 1) + Q
(n)
i1,...,ik+1(d − k − 3) + . . . )

(i2 − i1)! . . . (ik+1 − ik)!(n − ik+1 + i1)! ,

where the Q
(n)
i1,...,ik+1(j)’s are the coeﬃcients of the polynomial

k+1∏

l=1((t + 1)(t + 2) . . . (t + il+1 − il − 1)) =
 n−k−1∑

j=0 Q
(n)
i1,...,ik+1(j)t
j,

and we put ik+2 = n+i1. For j < 0 and j > n−k−1 we use the convention Q
(n)
i1,...,ik+1(j) := 0.

Remark 1.12. For faces of maximal dimension k = d − 1 the above formula simpliﬁes to

P[Conv(Si1, . . . , Sid) ∈ Fd−1(Cn)] = 2
(i2 − i1) . . . (id − id−1)(n − id + i1) ,

which recovers a result obtained in [29].

Remark 1.13. At the other extreme case, taking k = 0 in Theorem 1.11 yields the following
formula for the probability that Si, where 0 ≤ i < n, is a vertex of the convex hull Cn:

P[Si ∈ F0(Cn)] = 2
n!
 ([n
d
] + [ n
d − 2
] + . . . ) . (10)

Note that the result does not depend on i which becomes quite straightforward if one notices
the cyclic exchangeability: (ξ1, . . . , ξn) has the same distribution as (ξi+1, . . . , ξn, ξ1, . . . , ξi−1)
for all i = 0, . . . , n − 1. Since [n
1] = (n − 1)!, in the one-dimensional case d = 1 formula (10)
reduces to the classical result of Sparre Andersen [24, Corollary 2] stating that

P[max{S0, . . . , Sn} = Si] = 1
n , i = 0, . . . , n − 1.

1.5. Shift averages of face probabilities for general random walks. Connection
to random bridges. Finally, let us again turn to random walks. As was argued in Ex-
ample 1.10, face probabilities for non-symmetric exchangeable random walks do not enjoy
distribution freeness. On the other hand, the next theorem states that certain shift averages
of face probabilities are distribution-free.

Theorem 1.14. Let (Si)n
i=0 be a random walk in Rd whose increments ξ1, . . . , ξn satisfy
conditions (Ex) and (GP) but do not need to satisfy (±Ex). Then, for all 0 ≤ k ≤ d − 1 and

CONVEX HULLS OF RANDOM WALKS 9

for all indices 1 ≤ l1 < · · · < lk ≤ n,

1
n + 1 − lk
 n−lk∑

i=0 P[Conv(Si, Si+l1, . . . , Si+lk) ∈ Fk(Cn)]

= 1
n + 1
 n∑

i=0 P[Conv(Si, Si+l1, . . . , Si+lk) ∈ Fk(Cn)]

= 2(Q
(n+1)
0,l1,...,lk(d − k − 1) + Q
(n+1)
0,l1,...,lk(d − k − 3) + . . . )
l1!(l2 − l1)! . . . (lk − lk−1)!(n + 1 − lk)! ,

where in the second line we put Si+lj = S(i+lj )−(n+1) if i + lj ≥ n + 1.

According to Theorem 1.11, the last expression is exactly the face probability of a
random bridge of length n + 1. This is due to a direct relation between convex hulls of
random walks and random bridges, which is the essence of our proofs of Theorem 1.2 and
Theorem 1.14 (given below in Sections 5 and 6, respectively). The main idea, explored in
Section 5.3, is to construct a random bridge from a non-symmetric random walk S0, . . . , Sn by
adding the extra increment ξn+1 = −Sn and reshuﬄing the total n + 1 increments randomly
to enforce the exchangeability. For faces of maximal dimension k = d − 1, a diﬀerent proof
of Theorem 1.14 (without the middle term) was given by Vysotsky and Zaporozhets [29].

2. Absorption probability for the joint convex hull

2.1. Connection to absorption probabilities. Let us describe the idea of our proofs of
Theorems 1.6 an 1.11. For concreteness, consider a symmetric random walk (Si)n
i=0 in the
three-dimensional space R3. Given some 0 ≤ i1 < i2 ≤ n, we consider the probability that
the segment [Si1, Si2] is an edge of the polytope Cn = Conv(S0, . . . , Sn). Denote by l the line
passing through the points Si1 and Si2, and let h be any two-dimensional plane orthogonal
to the line l. The intersection point of l and h is denoted by P0.
Consider the orthogonal projection of the random walk S0, . . . , Sn on the plane h. Since
the projection of the points Si1 and Si2 is P0 (which we from now on view as the “origin”
of the plane h), we can split the projected random walk path into three components: the
“walk” from the projection of S0 to P0 (which shall be time-reversed and sign-changed to
be “starting” at P0), the “bridge” from P0 to P0, and the “walk” from P0 to the projection
of Sn. The basic geometric observation underlying our proof of Theorems 1.6 and 1.11 is
as follows: [Si1, Si2] is an edge of the convex hull Cn if and only if the point P0 is a vertex
of the joint convex hull of these three projected paths. Thus, we need to compute the so-
called non-absorption probability, that is the probability that the interior of the joint convex
hull of several random walks and bridges starting at the origin does not contain the origin.
Problems of this type for just one random walk or random bridge were considered in our
recent work [13].

2.2. Absorption probability for joint convex hulls. Consider a collection of s random
walks and r random bridges in Rd whose increments have a joint distribution invariant under
the following transformations: we are allowed to perform any signed permutation of the

10 ZAKHAR KABLUCHKO, VLADISLAV VYSOTSKY, AND DMITRY ZAPOROZHETS

increments inside any random walk, and any permutation of increments inside any random
bridge. The next theorem provides a distribution-free formula for the probability that the
joint convex hull of such random walks and bridges absorbs the origin. A particular case of
this theorem was stated without proof in [13, Theorem 2.7]. Before stating the theorem, we
introduce necessary notation and assumptions.
Denote by Sym(n)the symmetric group on a set of n elements. Fix s, r ∈ N0 := N ∪ {0}
that do not vanish simultaneously, n1, . . . , ns ∈ N, m1, . . . , mr ∈ N\{1}, and consider d-
dimensional random vectors

ξ(1)
1 , . . . , ξ(1)
n1 , . . . , ξ(s)
1 , . . . , ξ(s)
ns , η(1)
1 , . . . , η(1)
m1, . . . , η(r)
1 , . . . , η(r)
mr (11)

such that η(j)
1 + · · · + η(j)
mj = 0 a.s. for every 1 ≤ j ≤ r. Assume that for all permutations
σ(1) ∈ Sym(n1), . . . , σ(s) ∈ Sym(ns), θ(1) ∈ Sym(m1), . . . , θ(r) ∈ Sym(mr) and all signs
ε(1)
1 , . . . , ε(1)
n1 , . . . , ε(s)
1 , . . . , ε(s)
ns ∈ {−1, +1}, we have the distributional equality
(
ξ(1)
1 , . . . , ξ(1)
n1 , . . . , ξ(s)
1 , . . . , ξ(s)
ns , η(1)
1 , . . . , η(1)
m1, . . . , η(r)
1 , . . . , η(r)
mr )

d
= (
ε(1)
1 ξ(1)
σ1(1), . . . , ε(1)
n1 ξ(1)
σ1(n1), . . . , ε(s)
1 ξ(s)
σs(1), . . . , ε(s)
ns ξ(s)
σs(ns),

η(1)
θ1(1), . . . , η(1)
θ1(m1), . . . , η(r)
θr(1), . . . , η(r)
θr(mr )) . (12)

Consider the collection of s random walks (S(1)
l )n1
l=1, . . . , (S(s)
l )ns
l=1 and r random bridges
(R(1)
l )m1
l=1, . . . , (R(r)
l )mr
l=1 deﬁned by

S(i)
l = ξ(i)
1 + · · · + ξ(i)
l , 1 ≤ i ≤ s, 1 ≤ l ≤ ni,

R(j)
l = η(j)
1 + · · · + η(j)
l , 1 ≤ j ≤ r, 1 ≤ l ≤ mj.

Write H for the joint convex hull of these walks and bridges, that is

H = Conv (S(1)
1 , . . . , S(1)
n1 , . . . , S(s)
1 , . . . , S(s)
ns , R(1)
1 , . . . , R(1)
m1−1, . . . , R(r)
1 , . . . , R(r)
mr−1) .
(13)

Theorem 2.1. Assume that (12) holds and that any d random vectors from the list on the
right-hand side of (13) are linearly independent with probability 1. Then

P[0 ∈ H] = 2(P (d + 1) + P (d + 3) + . . . )
2n1n1! . . . 2nsns!m1! . . . mr! , (14)

where the P (j)’s (which also depend on s, r, n1, . . . , ns, m1, . . . , mr) are the coeﬃcients of the
polynomial

s∏

i=1((t + 1)(t + 3) . . . (t + 2ni − 1)) ×
 r∏

l=1((t + 1)(t + 2) . . . (t + ml − 1)) =
 ∞∑

j=0 P (j)t
j. (15)

Remark 2.2. Theorem 2.1 computes the so-called absorption probability. The non-absorption
probability is given by
 P[0 /∈ H] = 2(P (d − 1) + P (d − 3) + . . . )
2n1n1! . . . 2nsns!m1! . . . mr! , (16)

CONVEX HULLS OF RANDOM WALKS 11

with the usual convention P (j) := 0 for j < 0. To see the equivalence of (14) and (16) note
that ∞∑

j=0 P (j) = 2n1n1! . . . 2nsns!m1! . . . mr!,
 ∞∑

j=0 (−1)jP (j) = 0,

obtained by taking t = +1 and t = −1 in (15).

Remark 2.3. We can include the joint starting point 0 to the joint convex hull and consider
H0 := Conv(H, 0). Then, under the general position assumption of Theorem 2.1, we have

P[0 /∈ H] = P[0 ∈ F0(H0)].

Remark 2.4. Without the general position condition, it holds that

P[0 ∈ Int H] ≤ 2(P (d + 1) + P (d + 3) + . . . )
2n1n1! . . . 2nsns!m1! . . . mr! ≤ P[0 ∈ H],

where Int H is the interior of H. We omit the proof of these inequalities because it is
analogous to the proof of Proposition 2.10 in [13].

3. Proof of Theorem 2.1

3.1. Symmetry groups and Weyl chambers. In our recent work [13] we showed that
absorption probabilities for random walks with symmetrically distributed increments (re-
spectively, random bridges) can be interpreted geometrically using Weyl chambers of type
Bn (respectively, An−1). We shall extend these ideas by showing that Theorem 2.1 con-
cerning the convex hull of several walks and bridges can be interpreted in terms of Weyl
chambers corresponding to the direct product of several reﬂection groups. The possibility of
extension to direct products was mentioned without proof in Theorem 2.7 of [13]. We start
by recalling some relevant deﬁnitions.
The reﬂection group of type Bn is the symmetry group of the regular cube [−1, 1]n (or
of its dual, the regular crosspolytope). The elements of this group act on Rn by permuting
the coordinates in arbitrary way and multiplying any number of coordinates by −1. The
number of elements of this group is 2nn!. We shall not distinguish between an abstract group
and its action because this convenient for our purposes.
The reﬂection group of type An−1 is the symmetric group Sym(n) which acts on Rn by
permuting the coordinates. The number of elements of this group is n!. The action of this
group leaves the following hyperplane invariant:

Ln = {(x1, . . . , xn) ∈ Rn : x1 + · · · + xn = 0},

which explains why the subscript n − 1 rather than n appears in the standard notation An−1.
Note that the group An−1 is the symmetry group of the regular simplex with n vertices
(deﬁned as the convex hull of the standard basis in Rn).
The fundamental Weyl chambers of type An−1 and Bn are the following convex cones in
Rn:
 C(An−1) := {(x1, . . . , xn) ∈ Rn : x1 < x2 < · · · < xn},

C(Bn) := {(x1, . . . , xn) ∈ Rn : 0 < x1 < x2 < · · · < xn}.

12 ZAKHAR KABLUCHKO, VLADISLAV VYSOTSKY, AND DMITRY ZAPOROZHETS

Observe that C(An−1) is a fundamental domain for the reﬂection group An−1. This means
that the cones of the form gC(An−1), g ∈ An−1, are pairwise disjoint and the union of their
closures constitutes Rn. The cones gC(An−1) or their closures will be referred to as Weyl
chambers of type An−1. Similarly, the cone C(Bn) is a fundamental domain for the reﬂection
group Bn, and the closures of the cones gC(Bn), g ∈ Bn, are called Weyl chambers of type
Bn. Note that there are n! Weyl chambers of type An−1 and 2nn! Weyl chambers of type
Bn. In the sequel, a fundamental role will be played by the following reﬂection group of direct
product type: G := Bn1 × · · · × Bns × Am1−1 × · · · × Amr−1.
This group acts on Rn1 × · · · × Rns × Rm1 × · · · × Rmr ≡ Rn, where

n = n1 + · · · + ns + m1 + · · · + mr,

in the following natural way. Let e
(i)
1 , . . . , e
(i)
ni be the standard basis of Rni (for all 1 ≤ i ≤ s)
and let f (j)
1 , . . . , f (j)
mj be the standard basis of Rmj (for all 1 ≤ j ≤ r). Then the elements of
G can be represented as tuples of the form

g = (gσ(1),ε(1), . . . , gσ(s),ε(s), hθ(1), . . . , hθ(r)), (17)

where: σ(i) ∈ Sym(ni), θ(j) ∈ Sym(mj) are permutations; ε(i) := (ε(i)
1 , . . . , ε(i)
ni ) ∈ {−1, +1}ni
are signs; each gσ(i),ε(i) is the orthogonal transformation of Rni deﬁned by

gσ(i),ε(i)(e
(i)
k ) = ε(i)
k e
(i)
σ(i)(k), k = 1, . . . , ni; (18)

and each hθ(j) is the orthogonal transformation of Rmj deﬁned by

hθ(j)(f (j)
l ) = f (j)
θ(j)(l), l = 1, . . . , mj. (19)

The total number of elements in the group G is 2n1n1! . . . 2nsns!m1! . . . mr!.

3.2. Absorption probability and subspaces intersecting Weyl chambers. Consider
the (open) Weyl chambers

C (i)
B := C(Bni) = {(x
(i)
1 , . . . , x
(i)
ni ) ∈ Rni : 0 < x
(i)
1 < · · · < x
(i)
ni } ⊂ Rni,

C (j)
A := C(Amj −1) = {(y(j)
1 , . . . , y(j)
mj ) ∈ Rmj : y(j)
1 < · · · < y(j)
mj } ⊂ Rmj

and their direct product

C := C (1)
B × · · · × C (s)
B × C (1)
A × · · · × C (r)
A ⊂ Rn1 × · · · × Rns × Rm1 × · · · × Rmr ≡ Rn.

Let ¯C denote the closure of C. Note that C is a fundamental domain for the action of G on
Rn. The closed convex cones g ¯C, where g ∈ G, are called Weyl chambers (of product type).
Let L
(j) be the hyperplane invariant under the action of the group Amj −1:

L
(j) = {(y1, . . . , ymj ) ∈ Rmj : y1 + · · · + ymj = 0}, 1 ≤ j ≤ r, (20)

and consider the linear subspace

L := Rn1 × · · · × Rns × L
(1) × · · · × L
(r) ⊂ Rn.

CONVEX HULLS OF RANDOM WALKS 13

Note that the action of G leaves L invariant. Let A be a d × n-matrix with the columns

ξ(1)
1 , . . . , ξ(1)
n1 , . . . , ξ(s)
1 , . . . , ξ(s)
ns , η(1)
1 , . . . , η(1)
m1, . . . , η(r)
1 , . . . , η(r)
mr . (21)

We can view A : Rn → Rd as a linear operator mapping the standard basis of Rn, namely

e
(1)
1 , . . . , e
(1)
n1 , . . . , e
(s)
1 , . . . , e
(s)
ns , f (1)
1 , . . . , f (1)
m1 , . . . , f (r)
1 , . . . , f (r)
mr , (22)

to the vectors listed in (21), respectively. The next lemma states that the absorption prob-
ability equals the probability that the random linear subspace (Ker A) ∩ L intersects any
given Weyl chamber g ¯C in a non-trivial way.

Lemma 3.1. Under the assumptions of Theorem 2.1, for every g ∈ G,

P[0 ∈ Conv(S(1)
1 , . . . , S(1)
n1 , . . . , S(s)
1 , . . . , S(s)
ns , R(1)
1 , . . . , R(1)
m1−1, . . . , R(r)
1 , . . . , R(r)
mr−1)]

= P[(Ker A) ∩ L ∩ (g ¯C) ̸= {0}].

Proof. We are interested in the probability of the event

E := {(Ker A) ∩ L ∩ (g ¯C) ̸= {0}} = {Ker(Ag) ∩ L ∩ ¯C ̸= {0}}.

Recall that g : Rn → Rn is a linear operator given by (17), (18), (19). The columns of the
matrix Ag are
 ε(1)
1 ξ(1)
σ(1)(1), . . . , ε(1)
n1 ξ(1)
σ(1)(n1), . . . , ε(s)
1 ξ(s)
σ(s)(1), . . . , ε(s)
ns ξ(s)
σ(s)(ns),

η(1)
θ(1)(1), . . . , η(1)
θ(1)(n1), . . . , η(r)
θ(r)(1), . . . , η(r)
θ(r)(mr ),

as one can easily check by computing the action of Ag on the standard basis of Rn; see (22).
So, we can write the event E in the form

E = {∃(x
(1), . . . , x
(s), y(1), . . . , y(r)) ∈ ( ¯C (1)
B × · · · × ¯C (s)
B × ¯C (1)
A × · · · × ¯C (r)
A ) ∩ (L\{0}) :

s∑

i=1
 (
ε(i)
1 ξ(i)
σ(i)(1)x
(i)
1 + · · · + ε(i)
ni ξ(i)
σ(i)(ni)x
(i)
ni ) +
 r∑

j=1
 (η(j)
θ(j)(1)y(j)
1 + · · · + η(j)
θ(j)(mj )y(j)
mj ) = 0}
. (23)

For every 1 ≤ i ≤ s, there is a bijective correspondence between x
(i) = (x
(i)
1 , . . . , x
(i)
ni ) ∈
¯C (i)
B and ˜x
(i) = (˜x
(i)
1 , . . . , ˜x
(i)
ni ) ∈ Rni
≥0 given by

x
(i)
1 = ˜x
(i)
1 , x
(i)
2 = ˜x
(i)
1 + ˜x
(i)
2 , . . . , x
(i)
ni = ˜x
(i)
1 + · · · + ˜x
(i)
ni .

Similarly, there is a bijective correspondence between y(j) = (y(i)
1 , . . . , y(j)
mj ) ∈ ¯C (j)
A ∩ L
(j) and
˜y(j) = (˜y(j)
1 , . . . , ˜y(j)
mj−1) ∈ Rmj −1
≥0 given by

˜y(j)
1 = y(j)
2 − y(j)
1 , . . . , ˜y(j)
mj−1 = y(j)
mj − y(j)
mj −1,

or, equivalently,

y(j)
1 = ˜y(j)
0 , y(j)
2 = ˜y(j)
0 + ˜y(j)
1 , . . . , y(j)
mj = ˜y(j)
0 + ˜y(j)
1 + · · · + ˜y(j)
mj−1,

14 ZAKHAR KABLUCHKO, VLADISLAV VYSOTSKY, AND DMITRY ZAPOROZHETS

where ˜y(j)
0 ∈ R is chosen such that the condition y(j)
1 + · · · + y(j)
mj = 0 holds. Thus, we have

E = {∃(˜x
(1), . . . , ˜x
(s), ˜y(1), . . . , ˜y(r)) ∈ (Rn1
≥0 × · · · × Rns
≥0 × Rm1−1
≥0 × · · · × Rmr−1
≥0 )\{0} :

s∑

i=1
 ni∑

k=1 ˜x
(i)
k (ε(i)
k ξ(i)
σ(i)(k) + · · · + ε(i)
ni ξ(i)
σ(i)(ni)) +
 r∑

j=1
 mj −1∑

l=1 ˜y(j)
l (
η(j)
θ(j)(l+1) + · · · + η(j)
θ(j)(mj )) = 0}

modulo null sets, where we omitted the terms

˜y(j)
0 (
η(j)
θ(j)(1) + · · · + η(j)
θ(j)(mj )) = ˜y(j)
0 (
η(j)
1 + · · · + η(j)
mj ) = 0 a.s., 1 ≤ j ≤ r,

which vanish by the bridge condition (11). The invariance assumption (12) implies the
distributional equality
(
{ε(i)
k ξ(i)
σ(i)(k) + · · · + ε(i)
ni ξ(i)
σ(i)(ni)}
 i=1,...,s
k=1,...,ni, {
η(j)
θ(j)(l+1) + · · · + η(j)
θ(j)(mj )}
 j=1,...,r
l=1,...,mj−1
)

d
=
 ({S(i)
ni−k+1}
 i=1,...,s
k=1,...,ni, {
R(j)
mj −l}
 j=1,...,r
l=1,...,mj −1
)
 . (24)

Therefore,

P[E] = P[
∃(˜x
(1), . . . , ˜x
(s), ˜y(1), . . . , ˜y(r)) ∈ (Rn1
≥0 × · · · × Rns
≥0 × Rm1−1
≥0 × · · · × Rmr−1
≥0 )\{0} :

s∑

i=1
 (˜x
(i)
1 S(i)
ni + ˜x
(i)
2 S(i)
ni−1 + · · · + ˜x
(i)
ni S(i)
1 )

+
 r∑

j=1
 (˜y(j)
1 R(j)
mj −1 + ˜y(j)
2 R(j)
mj −2 + · · · + ˜y(j)
mj −1R(j)
1 ) = 0]
.

The term on the right-hand side is the probability that the joint convex hull of the walks
S(i)
k , 1 ≤ k ≤ ni, 1 ≤ i ≤ s, and the bridges R(j)
l , 1 ≤ l ≤ mj − 1, 1 ≤ j ≤ r, contains 0.
This proves the lemma. □

3.3. Hyperplane arrangements. Now we need some results from the theory of hyperplane
arrangements [18, 28]. A linear hyperplane arrangement (or simply “arrangement”) A is
a ﬁnite set of distinct hyperplanes in Rn that pass through the origin. The rank of an
arrangement A is the codimension of the intersection of all hyperplanes in the arrangement:

rank(A) = n − dim
 ( ⋂

H∈A H
)
 .

Equivalently, the rank is the dimension of the space spanned by the normals to the hyper-
planes in A. The characteristic polynomial χA(t) of the arrangement A is deﬁned by

χA(t) = ∑

B⊂A
(−1)#Bt
n−rank(B), (25)

CONVEX HULLS OF RANDOM WALKS 15

where #B denotes the number of elements in the set B, and rank(∅) = 0 under convention
that the intersection over the empty set of hyperplanes is Rn. The original deﬁnition of the
characteristic polynomial uses the notions of the intersection poset of A and the M¨obius
function on it; see [28, Section 1.3]. The equivalence of both deﬁnitions was proved by
Whitney; see, e.g., [18, Lemma 2.3.8] or [28, Theorem 2.4].
Denote by R(A) the ﬁnite set of open connected components (“regions” or “chambers”)
of the complement Rn \ ∪H∈AH of the hyperplanes. The following fundamental result due to
Zaslavsky [33] (see also [28, Theorem 2.5]) expresses the number of regions of the arrangement
A in terms of its characteristic polynomial:

#R(A) = (−1)nχA(−1). (26)

The lattice L(A) generated by an arrangement A in Rn consists of all linear subspaces
that can be represented as intersections of some of the hyperplanes from A, that is

L(A) =
 { ⋂

H∈B H : B ⊂ A
}
 .

By deﬁnition, Rn ∈ L(A), corresponding to the empty intersection over B = ∅. Let Mn−d
be a linear subspace in Rn of codimension d ≤ n − 1. We say that Mn−d is in general position
with respect to A if for all K ∈ L(A),

dim(Mn−d ∩ K) =
 {
dim K − d, if dim K ≥ d,
0, if dim K ≤ d. (27)

The next theorem provides a formula for the number of regions in R(A) intersected by a
linear subspace in general position. We refer to [13, Theorem 3.3 and Lemma 3.5] for its
proof.

Theorem 3.2. Let Mn−d be a linear subspace in Rn of codimension d that is in general
position w.r.t. to a linear hyperplane arrangement A. Let

χA(t) =
 n∑

k=0(−1)n−kakt
k (28)

be the characteristic polynomial of A. Then, the number of regions in R(A) intersected by
Mn−d is given by

#{R ∈ R(A) : R ∩ Mn−d ̸= ∅} = #{R ∈ R(A) : R ∩ Mn−d ̸= {0}}

= 2(ad+1 + ad+3 + . . . ),

where we put ak = 0 for k /∈ {0, . . . , n}.

Let us consider a special case: the reﬂection arrangements in Rn of types An−1 and Bn.
These arrangements consist of the hyperplanes

A(An−1) : {xi = xj}, 1 ≤ i < j ≤ n, (29)

A(Bn) : {xi = xj}, {xi = −xj}, {xk = 0}, 1 ≤ i < j ≤ n, 1 ≤ k ≤ n, (30)

16 ZAKHAR KABLUCHKO, VLADISLAV VYSOTSKY, AND DMITRY ZAPOROZHETS

where (x1, . . . , xn) are the coordinates on Rn. It is easily seen that the regions in R(A(An−1))
and R(A(Bn)) are precisely the interiors of the Weyl chambers of type An−1 and Bn.
The characteristic polynomials of the reﬂection arrangements (see Section 5.1 and Corol-
lary 2.2 in [28]) are given by

χA(An−1)(t) = t(t − 1) . . . (t − (n − 1)) =
 n∑

k=1(−1)n−k[
n
k
]
t
k, (31)

χA(Bn)(t) = (t − 1)(t − 3) . . . (t − (2n − 1)) =
 n∑

k=0(−1)n−kB(n, k)t
k, (32)

where [n
k] (the Stirling numbers of the ﬁrst kind) and B(n, k) (their B-analogues) have the
following generating functions:

t(t + 1) . . . (t + n − 1) =
 n∑

k=1
 [n
k
]
t
k, (t + 1)(t + 3) . . . (t + 2n − 1) =
 n∑

k=0 B(n, k)t
k.

3.4. Proof of Theorem 2.1. We are now ready to complete the proof of Theorem 2.1.
Applying Lemma 3.1 to all g ∈ G and taking the arithmetic mean, we obtain

P[0 ∈ H] = 1
#G
 ∑

g∈G P[(Ker A) ∩ L ∩ (g ¯C) ̸= {0}] = EN
#G , (33)

where the random variable N := ∑

g∈G1{(Ker A)∩L∩(g ¯C)̸={0}} (34)

counts the number of Weyl chambers of the form g ¯C, g ∈ G, intersected by the random
linear subspace (Ker A) ∩ L in a nontrivial way.
Given arbitrary arrangements A1, . . . , AM in Rq1, . . . , RqM , deﬁne their direct product as
the following arrangement in Rq ≡ Rq1+···+qM :

A1 × · · · × AM =

{H × Rq−q1}H∈A1 ⋃ {Rq1 × H × Rq−q1−q2}H∈A2 ⋃ . . . ⋃ {Rq−qM × H}H∈AM .

Consider the reﬂection arrangement A of type Bn1 × · · · × Bns × Am1−1 × · · · × Amr−1, that
is A = A(Bn1) × · · · × A(Bns) × A(Am1−1) × · · · × A(Amr−1).
The characteristic polynomial of a direct product of arrangements is the product of the
individual characteristic polynomials (Lemma 2.50 on p. 43 in [18]), hence

(−1)nχA(−t) =
 s∏

i=1((t + 1)(t + 3) . . . (t + 2ni − 1)) ×
 r∏

j=1(t(t + 1) . . . (t + mj − 1))

=
 n+r∑

k=r P (k − r)t
k,

CONVEX HULLS OF RANDOM WALKS 17

where we used the notation P (k) from (15). Now observe that N is the number of regions
in R(A) intersected by (Ker A) ∩ L.

Lemma 3.3. If the general position assumption imposed in Theorem 2.1 holds, then with
probability 1, the random linear subspace (Ker A) ∩ L has codimension d + r in Rn and is in
general position w.r.t. A.

Postponing the proof of the lemma for a moment, we apply Theorem 3.2 to obtain that

N = 2(P (d + 1) + P (d + 3) + . . . ) a.s.

Combining this equation with (33) completes the proof of Theorem 2.1. □

Proof of Lemma 3.3. In the case of just one random walk or random bridge, we proved the
lemma in [13, Section 6.2]. The proof in the direct product case is similar and we sketch only
the main ideas. Consider a linear subspace K from the lattice generated by the arrangement
A. That is, K can be represented as an intersection of some hyperplanes from A and,
consequently, K = K1 × · · · × Ks × K ′
1 × · · · × K ′
r (35)
for some Ki ∈ L(A(Bni)), 1 ≤ i ≤ s, and K ′
j ∈ L(A(Amj −1)), 1 ≤ j ≤ r. Our aim is to
prove that
 dim(K ∩ L ∩ Ker A) a.s.
=
 {
dim K − d − r, if dim K ≥ d + r,
0, if dim K ≤ d + r. (36)

Note in passing that taking K = Rn would yield codim(L ∩ Ker A) = d + r a.s.
In fact, it suﬃces to prove that

dim(K ∩ Ker A) a.s.
=
 {
dim K − d, if dim K ≥ d + r,
r, if dim K ≤ d + r. (37)

To see that (37) implies (36), let us show that K ∩ Ker A contains the r-dimensional linear
subspace L
⊥ with probability 1. Indeed, for every 1 ≤ j ≤ r we have

A(f (j)
1 + · · · + f (j)
mj ) = η(j)
1 + · · · + η(j)
mj = 0 a.s.

by deﬁnition of A and the bridge property, whence L
⊥ ⊂ Ker A. To see that L
⊥ ⊂ K, recall
that by deﬁnition of the arrangement of type Amj −1, see (29), the vector f (j)
1 + · · · + f (j)
mj be-
longs to all hyperplanes from A(Amj−1) and hence, to all linear subspaces from L(A(Amj −1)).
Next we are going to write down an explicit system of equations deﬁning K. Recall that
(x
(i)
1 , . . . , x
(i)
ni ) are coordinates on Rni, while (y(j)
1 , . . . , y(j)
mj ) are coordinates on Rmj . Let us
ﬁrst look at the lattice generated by the hyperplane arrangement A(Amj −1); see (29) for its
deﬁnition. Any linear subspace belonging to this lattice is given by a system of equations
of the following type. Decompose the variables y(j)
1 , . . . , y(j)
mj into some number, say q(j), of
non-empty groups, and then require the variables inside the same group to be equal to each
other. Linear subspaces belonging to the lattice generated by the hyperplane arrangement
A(Bni−1), see (30) for its deﬁnition, can be described as follows. Decompose the variables
x
(i)
1 , . . . , x
(i)
ni into some number, say p(i) + 1 of groups (all groups being non-empty except

18 ZAKHAR KABLUCHKO, VLADISLAV VYSOTSKY, AND DMITRY ZAPOROZHETS

possibly the last one). Require the variables in the last group to be 0. For each group except
the last one, multiply each variable in the group by either +1 or −1, and require the resulting
signed variables to be equal to each other.
Taking all the equations described above together, we obtain a system of equations
deﬁning K. However, since the distribution of the linear subspace (Ker A) ∩ L is invariant
w.r.t. the action of G, after transforming everything by a suitable g ∈ G, we can assume
without loss of generality that K is given by the following simpliﬁed system of equations.
For every 1 ≤ i ≤ s, we have the equations

γ1(i) := x
(i)
1 = · · · = x
(i)
u1(i),

γ2(i) := x
(i)
u1(i)+1 = · · · = x
(i)
u2(i),

. . . ,

γp(i)(i) := x
(i)
up(i)−1(i)+1 = · · · = x
(i)
up(i)(i),

x
(i)
up(i)(i)+1 = · · · = x
(i)
ni = 0,

with some 0 =: u0(i) < u1(i) < · · · < up(i)(i) ≤ ni, and for every 1 ≤ j ≤ r, we have the
equations
 δ1(j) := y(j)
1 = · · · = y(j)
v1(j),

δ2(j) := y(j)
v1(j)+1 = · · · = y(j)
v2(j),

. . . ,

δq(j)(j) := y(j)
vq(j)−1(j)+1 = · · · = y(j)
mj ,

with some 0 =: v0(j) < v1(j) < · · · < vq(j)(j) := mj. We use the variables γ1(i), . . . , γp(i)(i)
(1 ≤ i ≤ s) and δ1(j), . . . , δq(j)(j) (1 ≤ j ≤ r) as coordinates on K. Note that

dim K =
 s∑

i=1 p(i) +
 r∑

j=1 q(j). (38)

The linear subspace Ker A is the given by the equation

s∑

i=1
 ni∑

l=1 x
(i)
l ξ(i)
l +
 r∑

j=1
 mj∑

l=1 y(j)
l η(j)
l = 0. (39)

Inside K, the linear subspace K ∩ Ker A is given by the equation

s∑

i=1
 (γ1(i)S(i)
u1(i) + γ2(i)(S(i)
u2(i) − S(i)
u1(i)) + · · · + γp(i)(i)(S(i)
up(i)(i) − S(i)
up(i)−1(i)))

+
 r∑

j=1
 (δ1(j)R(j)
v1(j) + δ2(j)(R(j)
v2(j) − R(j)
v1(j)) + · · · + δq(j)(j)(0 − R(j)
vq(j)−1(j))) a.s.
= 0. (40)

Recall that the random walks and bridges take values in Rd, so that, eﬀectively, (39) and (40)
are systems of d equations each.

CONVEX HULLS OF RANDOM WALKS 19

Let dim K ≥ d + r. Then, by the general position assumption from Theorem 2.1, the
collection of random vectors

S(i)
u1(i), S(i)
u2(i), . . . , S(i)
up(i)(i), (1 ≤ i ≤ s), R(j)
v1(j), R(j)
v2(j), . . . , R(j)
vq(j)−1(j) (1 ≤ j ≤ r)

spans linearly the whole Rd with probability 1 since the total number of the vectors is at
least d; see (38). It follows that the system of d equations in (40) has full rank a.s., hence the
dimension of the set of its solutions is dim K − d a.s., thus proving the ﬁrst case of (37). Let
now dim K ≤ d + r. Then, we can ﬁnd a linear subspace K ′ ⊃ K such that dim K ′ = d + r
and K ′ ∈ L(A). Applying the above to K ′, we obtain dim(K ′ ∩ L ∩ Ker A) = 0 a.s., hence
dim(K ∩ L ∩ Ker A) = 0 a.s., thus proving the second case in (37). □

4. Proof of Theorems 1.6 and 1.11

Proof of Theorem 1.6. Given k + 1 vectors x1, . . . , xk+1 ∈ Rd denote by aﬀ(x1, . . . , xk+1) =
x1 + lin(0, x2 − x1, . . . , xk+1 − x1) their aﬃne hull and by

aﬀ ⊥(x1, . . . , xk+1) = (aﬀ(x1, . . . , xk+1) − x1)⊥

the orthogonal complement of aﬀ(x1, . . . , xk+1), which is a linear subspace.
Let ·|M denote the orthogonal projection on M := aﬀ⊥(Si1, . . . , Sik+1). Note that
dim M = d − k a.s. because

(Si2 − Si1, . . . , Sik+1 − Si1) d
= (Si2−i1, . . . , Sik+1−i1)

by (±Ex) (in fact, condition (Ex) suﬃces) and the random vectors on the right-hand side
are a.s. linearly independent by (GP). Projecting the path S0, . . . , Sn on M gives a random
walk terminating at P0 := Si1|M = · · · = Sik+1|M (viewed as the origin of M), k random
bridges that start and terminate at P0, and a random walk starting at P0. The ﬁrst walk
shall be time-reversed and sign-changed to start from P0. The increments of the random
walks are given by

ξ(1)
1 = −ξi1|M, ξ(1)
2 = −ξi1−1|M, . . . , ξ(1)
i1 = −ξ1|M,

ξ(2)
1 = ξik+1+1|M, ξ(2)
2 = ξik+1+2|M, . . . , ξ(2)
n−ik+1 = ξn|M,

while the increments of the random bridges are given by

η(j)
1 = ξij+1|M, . . . , η(j)
ij+1−ij = ξij+1|M, j = 1, . . . k.

We shall apply Theorem 2.1 to these s = 2 random walks and r = k random bridges in M
with M ∼= Rd−k a.s. It is easy to see that their increments listed above satisfy the invariance
assumption (12) of Theorem 2.1, namely, permuting the increments within the walks/bridges
and changing the signs of the increments in both random walks does not change the joint
distribution of the increments. In fact, such transformations of the unprojected increments of
the original random walk S1, . . . , Sn do not change the joint distribution of these increments
and, importantly, do not change M.
Denote by H0 the joint convex hull of the above random walks and bridges: H0 := Cn|M.
The key observation is as follows:

Conv(Si1, . . . , Sik+1) is a k-face of Cn if and only if P0 is a vertex of H0 (41)

20 ZAKHAR KABLUCHKO, VLADISLAV VYSOTSKY, AND DMITRY ZAPOROZHETS

on the set of full probability described by the general position assumption (GP). This is
evident since, by deﬁnition, the faces of a convex polytope are obtained by intersecting the
polytope with its supporting hyperplanes.
Postponing the veriﬁcation of the general position assumption for a moment, we apply
Theorem 2.1, see also Remark 2.3 and (16), to obtain that

P[P0 ∈ F0(H0)] = 2(P (n)
i1,...,ik+1(d − k − 1) + P (n)
i1,...,ik+1(d − k − 3) + . . . )

2i1+n−ik+1i1!(i2 − i1)! . . . (ik+1 − ik)!(n − ik+1)!

with the generating function for the P (n)
i1,...,ik+1(j)’s deﬁned in Theorem 1.6.
To complete the proof of Theorem 1.6 we need to verify the general position assumption
of Theorem 2.1. Let T1, . . . , Td−k be any d − k random vectors from the list

Si1−1 − Si1, Si1−2 − Si1, . . . , S1 − Si1 (ﬁrst walk, unprojected and time-reversed),

Si1+1 − Si1, Si1+2 − Si1, . . . , Si2−1 − Si1 (ﬁrst bridge, unprojected),
. . . ,

Sik+1 − Sik , Sik+2 − Sik , . . . , Sik+1−1 − Sik (k-th bridge, unprojected),

Sik+1+1 − Sik+1, Sik+1+2 − Sik+1, . . . , Sn − Sik+1 (second walk, unprojected).

We need to show that T1|M, . . . , Td−k|M are linearly independent with probability 1. Since
the orthogonal complement of h is spanned by Si2 − Si1, . . . , Sik+1 − Sik , it suﬃces to check
that the random vectors
 T1, . . . , Td−k, Si2 − Si1, . . . , Sik+1 − Sik (42)

are linearly independent with probability 1. But it is easy to see that their linear hull
coincides with the linear hull of

Sj1 − Sj0, Sj2 − Sj1, . . . , Sjd − Sjd−1

for some collection of indices 0 ≤ j0 < j1 < · · · < jd ≤ n containing the set {i1, . . . , ik+1}. By
assumptions (±Ex) and (GP), this linear hull has maximal possible dimension d a.s. This
proves the a.s. linear independence of the random vectors in (42). □

Proof of Theorem 1.11. The main idea is the same as in the previous proof. Consider the
linear subspace M := aﬀ ⊥(Si1, . . . , Sik+1) and note that dim M = d − k a.s. by the same
argument as in the previous proof. Projecting the closed path S0, . . . , Sn on M, we obtain
k + 1 random bridges in M (with M ∼= Rd−k a.s.) starting and terminating at P0 := Si1|M =
· · · = Sik+1|M. The random bridge number j + 1 ∈ {2, . . . , k + 1} is the projection of the
path Sij , Sij +1, . . . , Sij+1 and has increments

η(j+1)
1 = ξij+1|M, η(j+1)
2 = ξij+2|M, . . . , η(j+1)
ij+1−ij = ξij+1|M, j = 1, . . . , k,

while the ﬁrst random bridge is the projection of the path Sik+1, . . . , Sn−1, 0, S1, . . . , Si1 and
its increments are

η(1)
1 = ξik+1+1|M, . . . , η(1)
n−ik+1 = ξn|M, η(1)
n−ik+1+1 = ξ1|M, . . . , η(1)
n−ik+1+i1 = ξi1|M.

CONVEX HULLS OF RANDOM WALKS 21

Again, we observe that the invariance condition (12) of Theorem 2.1 is satisﬁed for these
r = k + 1 random bridges (and s = 0 random walks) because the joint distribution of the
increments is invariant with respect to arbitrary permutations of the increments within the
bridges. The general position assumption of Theorem 2.1 will be veriﬁed below. Observe
that with probability one, Conv(Si1, . . . , Sik+1) is a k-face of Cn if and only if P0 is a vertex
of the joint convex hull H0 := Cn|M of the above bridges; see (41). Hence, Theorem 2.1 (see
also Remark 2.3 and (16)), yields

P[P0 ∈ F0(H0)] = 2(Q
(n)
i1,...,ik+1(d − k − 1) + Q
(n)
i1,...,ik+1(d − k − 3) + . . . )

(i2 − i1)! . . . (ik+1 − ik)!(n − ik+1 + i1)!

with the generating function for the Q
(n)
i1,...,ik+1(j)’s deﬁned in Theorem 1.11.
To verify the general position assumption of Theorem 2.1, let T1, . . . , Td−k be any d − k
vectors from the list

Sik+1+1 − Sik+1, Sik+1+2 − Sik+1, . . . , Sn−1 − Sik+1, 0 − Sik+1, S1 − Sik+1, . . . , Si1−1 − Sik+1,
Si1+1 − Si1, Si1+2 − Si1, . . . , Si2−1 − Si1,
. . . ,
Sik+1 − Sik, Sik+2 − Sik, . . . , Sik+1−1 − Sik.

Our aim is to prove that T1|M, . . . , Td−k|M are linearly independent with probability 1. The
orthogonal complement of h is spanned by Si2 − Si1, . . . , Sik+1 − Sik, hence our task reduces
to showing that the vectors

T1, . . . , Td−k, Si2 − Si1, . . . , Sik+1 − Sik (43)

are linearly independent with probability 1. But their linear hull coincides with the linear
hull of
 Sj1 − Sj0, Sj2 − Sj1, . . . , Sjd − Sjd−1

for a suitable collection of indices i1 =: j0 < j1 < · · · < jd < n + j0 containing the
set {i1, . . . , ik+1} (with the convention Sn+j = Sj for j ≥ 0). By assumptions (Ex) and
(GP
′), this linear hull has maximal possible dimension d a.s. This proves the a.s. linear
independence of the random vectors in (43). □

5. Expected number of faces of a random walk

5.1. Method of proof. In the following we shall sketch the main steps in the proof of
Theorem 1.2. As a direct corollary of Theorem 1.6, we obtain a formula for the expected
number of k-dimensional faces of Cn under assumptions (±Ex) and (GP):

E[fk(Cn)] = 2 ∑

0≤i1<···<ik+1≤n
 P (n)
i1,...,ik+1(d − k − 1) + Pi1,...,ik+1(d − k − 3) + . . .

2i1+n−ik+1i1!(i2 − i1)! . . . (ik+1 − ik)!(n − ik+1)! , (44)

22 ZAKHAR KABLUCHKO, VLADISLAV VYSOTSKY, AND DMITRY ZAPOROZHETS

for all 0 ≤ k ≤ d − 1. Similarly, it follows from Theorem 1.11 that for random bridges
satisfying (Br), (Ex), (GP
′), we have

E [fk(Cn)] = 2 ∑

0≤i1<···<ik+1<n
 Q
(n)
i1,...,ik+1(d − k − 1) + Q
(n)
i1,...,ik+1(d − k − 3) + . . .

(i2 − i1)! . . . (ik+1 − ik)!(n − ik+1 + i1)! . (45)

In particular, the expected number of faces is distribution-free both for walks under (±Ex),
(GP), and for bridges under (Br), (Ex), (GP
′).
In Section 5.2 we shall evaluate the sum on the right-hand side of (44), thus proving
Theorem 1.2 for symmetric random walks satisfying (±Ex) and (GP). In order to remove the
unnecessary symmetry assumption, we shall prove in Section 5.3 that the expected number of
k-faces of any random walk of length n satisfying assumptions (Ex), (GP) is the same as for
any random bridge of length n + 1 satisfying assumptions (Br), (Ex), (GP
′) with n replaced
by n + 1. In particular, the expected number of k-faces of a random walk is distribution-free
provided (Ex) and (GP) hold. This will show that assumption (±Ex) is indeed unnecessary
and can be relaxed to (Ex).

5.2. Proof of Theorem 1.2 in the symmetric case. Let us prove that under assumptions
(±Ex) and (GP),
 E[fk(Cn)] = 2 · k!
n!
 ∞∑

l=0
 [ n + 1
d − 2l
]{d − 2l
k + 1
 }
. (46)

Recall from (4) that t
(j) = t(t + 1) . . . (t + j − 1) denotes the rising factorial. Let
[t
N ]f (t) = 1
N !f (N )(0) be the coeﬃcient of t
N in the Taylor expansion of a function f around
0. For m ∈ N0 = N ∪ {0} deﬁne

Rn,k(m)

:= [t
m] ∑

j0,...,jk+1
 ( (t + 1)(t + 3) . . . (t + 2j0 − 1)
2j0j0! (t + 1)(t + 3) . . . (t + 2jk+1 − 1)
2jk+1jk+1! t
(j1)

tj1! . . . t
(jk)

tjk!
 ) ,

where the sum is taken over all j0, jk+1 ∈ N0 and j1, . . . , jk ∈ N such that j0 + · · · + jk+1 = n.
With this notation, Theorem 1.6 (see also (44)) implies that

E[fk(Cn)] = 2
 ∞∑

l=0 Rn,k(d − k − 2l − 1).

Thus, to prove (46), it suﬃces to show that

Rn,k(m) = k!
n!
 {m + k + 1
k + 1
 }[ n + 1
m + k + 1
]. (47)

Expanding the product yields

Rn,k(m) = [t
m][x
n]
 



( ∞∑

j=0
 (t + 1)(t + 3) . . . (t + 2j − 1)
2jj! x
j)2 ( ∞∑

j=1
 t
(j)

tj! x
j)k

 .

CONVEX HULLS OF RANDOM WALKS 23

Using the binomial series (for t > 0)

∞∑

j=1
 t
(j)

tj! x
j = (1 − x)−t − 1
t ,
 ∞∑

j=0
 (t + 1)(t + 3) . . . (t + 2j − 1)
2jj! x
j = (1 − x)− 1
2 (t+1),

we obtain

Rn,k(m) = [t
m][x
n]
 (
(1 − x)−t−1 ((1 − x)−t − 1
t
 )k)
 = [x
n][t
m]
 (

e
−a(t+1) ( e
−at − 1
t
 )k)
 ,

where we introduced the notation a = a(x) = log(1 − x).
Consider the term

e
−a(t+1) (e
−at − 1
t
 )k = te
−a (e
−at − 1
t
 )k+1 + e
−a (e
−at − 1
t
 )k .

As a consequence of the second equality in (3), we have
(e
−at − 1
t
 )k =
 ∞∑

m=0(−a)m+k k!
(m + k)!
 {m + k
k
 }t
m.

Using this formula twice, we obtain

[t
m]e
−a(t+1) (e
−at − 1
t
 )k = (−a)m+k 1
(m + k)! e
−a ({m + k
k + 1
 }(k + 1)! + {m + k
k
 }k!
)

= (−a)m+k k!
(m + k)! e
−a{m + k + 1
k + 1
 },

where the last line follows from the relation
{m + k
k + 1
 }
(k + 1) + {m + k
k
 } = {
m + k + 1
k + 1
 }.

Now recall that a = log(1 − x) and use the ﬁrst generating function in (3) to get

[x
n]((−a)m+ke
−a) = [x
n] (− log(1 − x))m+k

(1 − x)

= 1
m + k + 1 [x
n] d
dx(− log(1 − x))m+k+1

= n + 1
m + k + 1 [x
n+1](− log(1 − x))m+k+1

= (m + k)!
n!
 [ n + 1
m + k + 1

].

Taking everything together, we obtain (47), thus completing the proof.

24 ZAKHAR KABLUCHKO, VLADISLAV VYSOTSKY, AND DMITRY ZAPOROZHETS

5.3. Relation between random walks and random bridges. The next result completes
the proof of Theorem 1.2.

Theorem 5.1. Let (Si)n
i=0 be a random walk in Rd whose increments (ξ1, . . . , ξn) satisfy
conditions (Ex) and (GP). Further, let (S′
i)n+1
i=0 be a random bridge of length n + 1 satisfying
conditions (Br), (Ex) and (GP′) with n replaced by n + 1 (in particular, S′
0 = S′
n+1 = 0).
Write Cn = Conv(S0, . . . , Sn) and C ′
n+1 = Conv(S′
0, . . . , S′
n+1) for the corresponding convex
hulls. Then, for all 0 ≤ k ≤ d − 1,

E[fk(Cn)] = E[fk(C ′
n+1)]. (48)

Proof. From (45) we know that E[fk(C ′
n+1)] does not depend on the choice of the particular
bridge (S′
i)n+1
i=0 . Hence, it suﬃces to prove (48) for any random bridge of our choice. This
bridge will be constructed as follows. Start with a random walk (Si)n
i=0 satisfying (Ex) and
(GP), and consider the closed path S0, S1, . . . , Sn, 0. Although this path returns to Sn+1 := 0
at step n + 1, its increments are not exchangeable because the last increment ξn+1 := −Sn
and, say, ξ1 have diﬀerent distributions. In order to enforce the exchangeability, we shall
consider a random permutation of the increments of this closed path. More precisely, our
construction goes as follows.
For any permutation σ from the symmetric group Sym(n + 1), consider the random
sequence (Sσ
i )n+1
i=0 starting at Sσ
0 := 0 and deﬁned by

Sσ
i := ξσ(1) + · · · + ξσ(i), 1 ≤ i ≤ n + 1.

Clearly, each sequence terminates at Sσ
n+1 = ξ1 + · · · + ξn + ξn+1 = 0. Denote by C σ
n+1 :=
Conv(Sσ
0 , Sσ
1 , . . . , Sσ
n+1) its convex hull. Consider a random permutation ς that is uniformly
distributed on the symmetric group Sym(n+ 1) and independent of the random walk (Si)n
i=0.
It is clear that (Sς
i )n+1
i=0 satisﬁes conditions (Br) and (Ex) with n replaced by n + 1. To
verify (GP
′) (with n + 1 as well), by (Ex) it suﬃces to show that for any p ∈ {1, . . . , d} and
1 ≤ l1 < . . . < lp ≤ lp+1 < . . . < ld < n and also for p = 0 and any 0 ≤ l1 < . . . < ld < n, the
random vectors Sl1, . . . , Slp, Slp+1 − Sn, . . . , Sld − Sn
are linearly independent with probability 1. Equivalently, the increments

Sl1, Sl2 − Sl1, . . . , Slp − Slp−1, Sn − Sld, Sld − Sld−1, . . . , Slp+2 − Slp+1

are a.s. linearly independent. Since these increments are taken over disjoint time intervals,
their linear independence follows from assumptions (Ex) and (GP) imposed on (Si)n
i=0, as in
the proof of Remark 1.5. This veriﬁes (GP
′) (with n + 1) for (Sς
i )n+1
i=0 .
By the distribution freeness of the expected number of k-faces under (Br), (Ex), and
(GP
′) (see(45)), it remains to prove that

E[fk(Cn)] = E[fk(C ς
n+1)]. (49)

We have
 E[fk(C ς
n+1)] = 1
(n + 1)!
 ∑

σ∈Sym(n+1) E[fk(Conv(Sσ
1 , . . . , Sσ
n+1))]. (50)

CONVEX HULLS OF RANDOM WALKS 25

Fix a permutation σ ∈ Sym(n + 1) and let r ∈ {1, . . . , n + 1} be such that σ(r) = n + 1.
Then

Conv(Sσ
1 , Sσ
2 , . . . , Sσ
n+1) = Conv(Sσ
r , . . . , Sσ
n+1, Sσ
1 , . . . , Sσ
r−1)

= Sσ
r + Conv(0, Sσ
r+1 − Sσ
r , . . . , Sσ
n+1 − Sσ
r , Sσ
n+1 − Sσ
r + Sσ
1 , . . . , Sσ
n+1 − Sσ
r + Sσ
r−1),

where in the second equality we used that Sσ
n+1 = 0. Since shifts do not change the number
of faces, we arrive at

fk(Conv(Sσ
1 , Sσ
2 , . . . , Sσ
n+1))

= fk(Conv(0, Sσ
r+1 − Sσ
r , . . . , Sσ
n+1 − Sσ
r , Sσ
n+1 − Sσ
r + Sσ
1 , . . . , Sσ
n+1 − Sσ
r + Sσ
r−1)). (51)

It follows from σ(r) = n + 1 and condition (Ex) that

(ξσ(r+1), . . . , ξσ(n+1), ξσ(1), . . . , ξσ(r−1)) d
= (ξ1, . . . , ξn),

which implies, by taking partial sums at both sides, that

(0, Sσ
r+1 − Sσ
r , . . . , Sσ
n+1 − Sσ
r , Sσ
n+1 − Sσ
r + Sσ
1 , . . . , Sσ
n+1 − Sσ
r + Sσ
r−1) d
= (0, S1, . . . , Sn). (52)

Combining (51) and (52), we obtain that for every deterministic σ ∈ Sym(n + 1),

E[fk(Conv(Sσ
1 , Sσ
2 , . . . , Sσ
n+1))] = E[fk(Cn)].

Inserting this into (50) yields (49), and the theorem follows. □

6. Proof of Theorem 1.14

The following two propositions combined with Theorem 1.11 yield Theorem 1.14. Their
proofs use the same ideas of reshuﬄing of increments as in the proof of Theorem 5.1.

Proposition 6.1. With the same notation and assumptions as in Theorem 5.1, for all indices
1 ≤ l1 < · · · < lk ≤ n,

1
n + 1
 n∑

i=0 P[Conv(Si, Si+l1, . . . , Si+lk) ∈ Fk(Cn)] = P[Conv(0, S′
l1, . . . , S′
lk) ∈ Fk(C ′
n+1)],

where we put Si+lj = S(i+lj )−(n+1) if i + lj ≥ n + 1.

Proof. The increments ξ1, . . . , ξn of the random walk (Si)n
i=0 satisfy (Ex) and (GP). Repeat-
ing the proof of Theorem 5.1, we deﬁne ξn+1 := −Sn and reshuﬄe the increments ξ1, . . . , ξn+1
according to a random uniformly distributed permutation ς ∈ Sym(n + 1) independent of
(Si)n
i=0. Since (Sς
i )n+1
i=0 is a random bridge satisfying (Br), (Ex), and (GP
′) (with n replaced
by n + 1), by Theorem 1.11 and the deﬁnition of (Sς
i )n+1
i=0 , we have

P[Conv(0, S′
l1, . . . , S′
lk) ∈ Fk(C ′
n+1)]

= 1
(n + 1)!
 ∑

σ∈Sym(n+1) P[Conv(Sσ
0 , Sσ
l1, . . . , Sσ
lk) ∈ Fk(Conv(Sσ
0 , Sσ
1 , . . . , Sσ
n+1))]. (53)

26 ZAKHAR KABLUCHKO, VLADISLAV VYSOTSKY, AND DMITRY ZAPOROZHETS

Fix a permutation σ ∈ Sym(n + 1) and let r ∈ {1, . . . , n + 1} be such that σ(r) = n + 1.
Since the shift by Sσ
r does not change the structure of the convex hull, we have

P[Conv(Sσ
0 , Sσ
l1, . . . , Sσ
lk) ∈ Fk(Conv(Sσ
0 , Sσ
1 , . . . , Sσ
n+1))]

= P[Conv(Sσ
0 − Sσ
r , Sσ
l1 − Sσ
r , . . . , Sσ
lk − Sσ
r ) ∈ Fk(Conv(Sσ
0 − Sσ
r , Sσ
1 − Sσ
r , . . . , Sσ
n − Sσ
r ))].
(54)

Recall that from (52) and Sσ
n+1 = 0,

(Sσ
r − Sσ
r , Sσ
r+1 − Sσ
r , . . . , Sσ
n+1 − Sσ
r , Sσ
1 − Sσ
r , . . . , Sσ
r−1 − Sσ
r ) d
= (0, S1, . . . , Sn). (55)

Note that Sσ
l − Sσ
r on the left-hand side corresponds to Sl−r on the right-hand side if we
agree to understand all indices modulo n + 1. Applying (55) to the right-hand side of (54)
and using the fact that {Sl}n
l=0 = {Sl−r}n
l=0, we arrive at

P[Conv(Sσ
0 , Sσ
l1, . . . , Sσ
lk) ∈ Fk(Conv(Sσ
0 , Sσ
1 , . . . , Sσ
n+1))]

= P[Conv(S−r, Sl1−r, . . . , Slk−r) ∈ Fk(Conv(S0, S1, . . . , Sn))].

Taking the sum over all σ ∈ Sym(n + 1) and observing that for any ﬁxed r ∈ {1, . . . , n + 1}
there are n! permutations σ for which σ(r) = n + 1, we arrive at

RHS of (53) = n!
(n + 1)!
 n+1∑

r=1 P[Conv(S−r, Sl1−r, . . . , Slk−r) ∈ Fk(Conv(S0, S1, . . . , Sn))].

Substituting i = n+1−r and recalling that the indices are considered modulo n+1 completes
the proof. □

Proposition 6.2. With the same notation and assumptions as in Theorem 5.1, for all indices
1 ≤ l1 < · · · < lk ≤ n,

1
n − lk + 1
 n−lk∑

i=0 P[Conv(Si, Si+l1, . . . , Si+lk) ∈ Fk(Cn)] = P[Conv(0, S′
l1, . . . , S′
lk) ∈ Fk(C ′
n+1)].

(56)

Proof. The main idea is to combine the proof of Theorem 1.11 with the method of reshuﬄing
from the proof of Theorem 5.1. From Theorem 1.11 we know that the face probability on
the right-hand side of (56) is distribution-free under (Br), (Ex), and (GP
′). Hence, it suﬃces
to prove (56) for a bridge of our choice.
The increments ξ1, . . . , ξn of the random walk (Si)n
i=0 satisfy (Ex) and (GP). Similarly
to the proof of Theorem 5.1, we deﬁne ξn+1 := −Sn and reshuﬄe the increments ξ1, . . . , ξn+1
according to a random permutation ς ∈ Sym(n + 1) given by

ς = (1, . . . , lk, lk + ς ′(1), . . . , lk + ς ′(n − lk + 1)),

where ς ′ ∈ Sym(n − lk + 1) is a uniformly distributed random permutation independent of
(Si)n
i=0.
 CONVEX HULLS OF RANDOM WALKS 27

Let ρ be the random variable deﬁned by ς ′(ρ) = n − lk + 1. Clearly, ρ is distributed
uniformly on {1, . . . , n − lk + 1}. Consider the random permutation τ ∈ Sym(n + 1)

τ := (lk + ς ′(ρ + 1), . . . , lk + ς ′(n − lk + 1), 1, . . . , lk, lk + ς ′(1), . . . , lk + ς ′(ρ − 1), n + 1)

obtained by a cyclic shift of ς, that is τ (n − lk − ρ + 1 + i) = ς(i) for 1 ≤ i ≤ n + 1 if we
agree to understand all indices modulo n + 1. Then

(Sς
i )n
i=0 = −Sτ
n−lk−ρ+1 + (Sτ
n−lk−ρ+1, Sτ
n−lk−ρ+2, . . . , Sτ
n, 0, Sτ
1 , . . . , Sτ
n−lk−ρ),

implying, by the equality

{Sτ
n−lk−ρ+1, Sτ
n−lk−ρ+2, . . . , Sτ
n, 0, Sτ
1 , . . . , Sτ
n−lk−ρ} = {Si}n
i=0
and the fact that shifts do not change the structure of the convex hull, the equality of the
events
{
Conv(0, Sς
l1, . . . , Sς
lk) ∈ Fk(C ς
n+1)}

= {
Conv(Sτ
n−lk−ρ+1, Sτ
(n−lk−ρ+1)+l1, . . . , Sτ
(n−lk−ρ+1)+lk ) ∈ Fk(Cn)}
.

Finally, we pass to probabilities and condition on ρ in the right-hand side. Using the dis-
tributional identity Law((Si)n
i=0) = Law((Sτ
i )n
i=0|ρ = ρ0) for all ρ0 ∈ {1, . . . , n − lk + 1},
which holds since the random walk (Si)n
i=0 satisﬁes (Ex) and the increments of (Sτ
i )n
i=0 do
not include ξn+1, we arrive at

P[Conv(0, Sς
l1, . . . , Sς
lk) ∈ Fk(C ς
n+1)] = 1
n − lk + 1
 n−lk∑

i=0 P[Conv(Si, Si+l1, . . . , Si+lk) ∈ Fk(Cn)].

(57)
It remains to compute the left-hand side to prove the proposition. We cannot apply
Theorem 1.11 directly since (Sς
i )n+1
i=0 does not have exchangeable increments: ξς(n+1) and, say,
ξ1 clearly have diﬀerent distributions. However, the argument of the proof of Theorem 1.11
applies directly, and we repeat it below.
Consider the linear hull M := lin
⊥(Sς
0, Sς
l1, . . . , Sς
lk) and note that dim M = d − k a.s.
Projecting the path Sς
0 , . . . , Sς
n+1 on M, we obtain k + 1 random bridges that start and
terminate at 0 ∈ M. The increments of the bridges are given by

η(j)
1 = ξlj−1+1|M, . . . , η(j)
lj −lj−1 = ξlj |M, j = 1, . . . k,

where l0 := 0, and
 η(k+1)
1 = ξlk+ς′(1)|M, . . . , η(k+1)
n−lk+1 = ξlk+ς′(n−lk+1)|M.

Let H ς
0 := C ς
n+1|M denote the convex hull of these k + 1 random bridges in M ∼= Rd−k a.s.
Then P[Conv(0, Sς
l1, . . . , Sς
lk) ∈ Fk(C ς
n+1)] = P[0 ∈ F0(H ς
0 )]. (58)
It is easy to see that the invariance condition (12) of Theorem 2.1 is satisﬁed for these
r = k + 1 random bridges (and s = 0 random walks). The argument uses the same ideas as
in the proofs of Theorems 1.6 and 1.11. The general position assumption of Theorem 2.1 is
veriﬁed in the same manner as in the proof of Theorem 1.11 supplemented by the respective
argument from the proof of Theorem 5.1.

28 ZAKHAR KABLUCHKO, VLADISLAV VYSOTSKY, AND DMITRY ZAPOROZHETS

Now (56) follows by combining (57) with (58) and applying Theorem 2.1 (see also
Remark 2.3 and (16)) to H ς
0 exactly as in the proof of Theorem 1.11. □

7. Further remarks and conjectures

7.1. Results not requiring the general position assumption. Let (Si)n
i=0 and (S′
i)n
i=0
be two random walks with increments (ξ1, . . . , ξn) and (ξ′
1, . . . , ξ′
n), respectively, such that
(ξ1, . . . , ξn) satisﬁes (±Ex) and (GP), while (ξ′
1, . . . , ξ′
n) satisﬁes (±Ex) only. Denote the
corresponding convex hulls by Cn := Conv(S0, . . . , Sn) and C ′
n := Conv(S′
0, . . . , S′
n). All
faces of Cn are simplices a.s., see Remark 1.5, but this is in general not true for C ′
n. The
face probabilities of C ′
n are not distribution-free, but it can be shown that

P[Conv(S′
i1, . . . , S′
ik+1) ∈ Fk(C ′
n)] ≤ P[Conv(Si1, . . . , Sik+1) ∈ Fk(Cn)]

≤ P[Conv(S′
i1, . . . , S′
ik+1) ⊂ F ′ for some F ′ ∈ Fk(C ′
n)], (59)

where the distribution-free probability in the middle was calculated in Theorem 1.6. To
prove this, one argues in the same way as in the proof of Theorem 1.6, but uses Remark 2.4
instead of Theorem 2.1. Similar inequalities hold for bridges violating the general position
assumption.
From (59) it is possible to deduce that under assumption (Ex), one has

E[f −
k (C ′
n)] ≤ 2 · k!
n!
 ∞∑

l=0
 [ n + 1
d − 2l
]{d − 2l
k + 1
 } ≤ E[f +
k (C ′
n)],

where f −
k (C ′
n) is the number of simplicial k-faces of C ′
n, while f +
k (C ′
n) is the number of
collections of indices 1 ≤ i1 < · · · < ik+1 ≤ n such that Conv(Si1, . . . , Sik+1) is contained in
some k-face F ′ of C ′
n.

7.2. Expected total number of faces. Assuming (Ex) and (GP), let us compute the
expected number of faces of Cn in all dimensions together. We need the numbers ̂cN (which
appeared in [27]) deﬁned by

̂cN =
 N∑

k=1(k − 1)!
{
N
k
 } = N![t
N ] log ( 1
2 − et
 ) = (N − 1)![t
N −1] ( e
t

2 − et
 ) . (60)

From Theorem 1.2 and (5) we obtain the formula

E
 [ d−1∑

k=0 fk(Cn)
]
 = 2
n!
 ∞∑

l=0
 [ n + 1
d − 2l
]
̂cd−2l ∼ 2̂cd
(d − 1)! (log n)d−1,

where the asymptotics is for n → ∞ and ﬁxed d ∈ N. The numbers ̂cN are similar to the
ordered Bell numbers ON which count the number of weak orderings on a set of N elements
and are given by
 ON =
 N∑

k=0 k!{N
k
 } = 1
2
 ∞∑

i=0
 i
N

2i .

CONVEX HULLS OF RANDOM WALKS 29

7.3. Open questions. It is natural to ask for the limit distribution of the (appropriately
normalized) number of k-faces of Cn. For convex hulls of i.i.d. Gaussian samples, variance
asymptotics for the face numbers were established recently by Calka and Yukich [4] (also see
earlier works [1, 8, 10] for limit theorems as LLN and CLT), but the i.i.d. model may behave
very diﬀerently from the convex hulls of random walks studied in the present paper. Exam-
ple 1.10 shows that the absorption probability is not distribution-free for (non-symmetric)
random walks satisfying (Ex) and (GP). It is likely that among such random walks the
absorption probability attains its maximum value for random walks satisfying (±Ex). A
similar result for convex hulls of i.i.d. samples was proved by Wagner and Welzl [31].
It also remains open to compute the expected number of faces and the face probabilities
for the simple random walk on the lattice Z
d, even for d = 2.

Acknowledgments

We would like to thank the referee for his/her stimulating comments and suggestions.

References

[1] I. Barany and V. Vu. Central limit theorems for Gaussian polytopes. Ann. Probab., 35:1593–1621, 2007.
[2] O. Barndorﬀ-Nielsen and G. Baxter. Combinatorial lemmas in higher dimensions. Trans. Amer. Math.
Soc., 108:313–325, 1963.
[3] G. Baxter. A combinatorial lemma for complex numbers. Ann. Math. Statist., 32:901–904, 1961.
[4] P. Calka and J. E. Yukich. Variance asymptotics and scaling limits for Gaussian polytopes. Probab.
Theory Relat. Fields, 163(1-2):259–301, 2015.
[5] R. Eldan. Extremal points of high-dimensional random walks and mixing times of a Brownian motion
on the sphere. Ann. Inst. H. Poincar´e Sec. B, 50:95–110, 2014.
[6] W. Feller. An Introduction to Probability Theory and its Applications, volume 2. Wiley, New York, 1966.
[7] R. L. Graham, D. E. Knuth, and O. Patashnik. Concrete mathematics: A foundation for computer
science. Amsterdam: Addison-Wesley Publishing Group, second edition, 1994.
[8] I. Hueter. Limit theorems for the convex hull of random points in higher dimensions. Trans. Amer.
Math. Soc., 351:4337–4363, 1999.
[9] D. Hug. Random polytopes. In Stochastic geometry, spatial statistics and random ﬁelds, pages 205–238.
Springer, Heidelberg, 2013.
[10] D. Hug and M. Reitzner. Gaussian polytopes: variances and limit theorems. Adv. in Appl. Probab.,
37(2):297–320, 2005.
[11] C. Jordan. Calculus of ﬁnite diﬀerences. 3rd ed. New York: Chelsea Publishing Company, 1965.
[12] Z. Kabluchko, V. Vysotsky, and D. Zaporozhets. A multidimensional analogue of the arcsine law for the
number of positive terms in a random walk. Preprint, 2016. Available at arXiv:1610.02861.
[13] Z. Kabluchko, V. Vysotsky, and D. Zaporozhets. Convex hulls of random walks, hyperplane arrange-
ments, and Weyl chambers. Geom. Funct. Anal., 27:880–918, 2017.
[14] Z. Kabluchko and D. Zaporozhets. Intrinsic volumes of Sobolev balls with applications to Brownian
convex hulls. Trans. Amer. Math. Soc., 368:8873–8899, 2016.
[15] J. Kampf, G. Last, and I. Molchanov. On the convex hull of symmetric stable processes. Proc. Amer.
Math. Soc., 140(7):2527–2535, 2012.
[16] S. N. Majumdar, A. Comtet, and J. Randon-Furling. Random convex hulls and extreme value statistics.
J. Stat. Phys., 138(6):955–1009, 2010.
[17] I. Molchanov and F. Wespi. Convex hulls of L´evy processes. Elect. Comm. Probab., 21:paper no. 69,
2016.

30 ZAKHAR KABLUCHKO, VLADISLAV VYSOTSKY, AND DMITRY ZAPOROZHETS

[18] P. Orlik and H. Terao. Arrangements of hyperplanes. Probability and its Applications. Springer-Verlag,
Berlin, 1992.
[19] J. Pitman. Combinatorial stochastic processes. Ecole d’Et´e de Probabilit´es de Saint-Flour XXXII – 2002.
Berlin: Springer, 2006.
[20] M. Reitzner. The combinatorial structure of random polytopes. Adv. Math., 191(1):178–208, 2005.
[21] R. Schneider. Recent results on random polytopes. Boll. Unione Mat. Ital. (9), 1(1):17–39, 2008.
[22] T. L. Snyder and J. M. Steele. Convex hulls of random walks. Proc. Amer. Math. Soc., 117:1165–1173,
1993.
[23] E. Sparre Andersen. On sums of symmetrically dependent random variables. Scand. Aktuarietidskr.,
36:123–138, 1953.
[24] E. Sparre Andersen. On the ﬂuctuations of sums of random variables I. Math. Scand., 1:263–285, 1953.
[25] E. Sparre Andersen. On the ﬂuctuations of sums of random variables. II. Math. Scand., 2:195–223, 1954.
[26] F. Spitzer and H. Widom. The circumference of a convex polygon. Proc. Amer. Math. Soc., 12:506–509,
1961.
[27] R. Sprugnoli. Riordan arrays and combinatorial sums. Discrete Math., 132(1-3):267–290, 1994.
[28] R. Stanley. An introduction to hyperplane arrangements. In Geometric combinatorics, pages 389–496.
Amer. Math. Soc., Providence, RI, 2007.
[29] V. Vysotsky and D. Zaporozhets. Convex hulls of multidimensional random walks. Trans. Amer. Math.
Soc., 2017. Published on-line.
[30] A. R. Wade and Ch. Xu. Convex hulls of random walks and their scaling limits. Stochastic Process.
Appl., 125(11):4300–4320, 2015.
[31] U. Wagner and E. Welzl. A continuous analogue of the upper bound theorem. Discrete Comput. Geom.,
26(2):205–219, 2001. ACM Symposium on Computational Geometry (Hong Kong, 2000).
[32] H. S. Wilf. The asymptotic behavior of the Stirling numbers of the ﬁrst kind. J. Comb. Theory, Ser. A,
64(2):344–349, 1993.
[33] T. Zaslavsky. Facing up to arrangements: face-count formulas for partitions of space by hyperplanes.
American Mathematical Society, 1975.

Zakhar Kabluchko: Institut f¨ur Mathematische Stochastik, Westf¨alische Wilhelms-
Universit¨at M¨unster, Orl´eans–Ring 10, 48149 M¨unster, Germany
E-mail address: zakhar.kabluchko@uni-muenster.de

Vladislav Vysotsky, University of Sussex, Pevensey 2 Building, Falmer Campus, Brighton
BN1 9QH, United Kingdom and St. Petersburg Department of Steklov Mathematical Insti-
tute, Fontanka 27, 191011 St. Petersburg, Russia
E-mail address: v.vysotskiy@sussex.ac.uk, vysotsky@pdmi.ras.ru

Dmitry Zaporozhets, St. Petersburg Department of Steklov Mathematical Institute,
Fontanka 27, 191011 St. Petersburg, Russia
E-mail address: zap1979@gmail.com
