<!-- source: https://arxiv.org/pdf/1811.11073 | converted from PDF -->

arXiv:1811.11073v3  [math.NT]  11 Jun 2021
AN IMPROVEMENT ON FURSTENBERG’S INTERSECTION PROBLEM

HAN YU

ABSTRACT. In this paper, we study a problem posed by Furstenberg on intersections between ×2, ×3
invariant sets. We present here a direct geometrical counting argument to revisit a theorem of Wu and
Shmerkin. This argument can be used to obtain further improvements. For example, we show that if
A2, A3 ⊂ [0, 1] are closed and ×2, ×3 invariant respectively, assuming that dim A2 + dim A3 < 1 then
A2 ∩ (uA3 + v) is sparse (deﬁned in this paper) and has box dimension zero uniformly with respect to
the real parameters u, v such that u and u
−1 are both bounded away from 0.

1. INTRODUCTION AND MOTIVATION

1.1. Furstenberg’s intersection problem. Furstenberg ( [F70]) posed a series of fundamental ques-
tions on the transversality of dynamical systems. A central heuristic of those problems is that ×2, ×3
should be two very different actions. Towards this direction, we have the following conjecture.

Conjecture 1.1 (The strong Furstenberg’s intersection problem). Let A2, A3 be closed ×2, ×3 invariant
sets respectively and such that dimH A2 + dimH A3 < 1. Then the intersection A2 ∩ A3 contains only rational
numbers.

Here dimH is the Hausdorff dimension, and it will be discussed in Section 3.5. The original form
of the above conjecture states that for any irrational number a, its ×2 mod 1 orbit closure and ×3
mod 1 orbit closure have total Hausdorff dimension at least 1. In this direction, an earlier result of
Furstenberg in [F67] states that the ×2, ×3 mod 1 orbit, i.e.

{2
k3
ma mod 1}k,m≥1

is dense in [0, 1]. As we mentioned above, Furstenberg posed a series of deep conjectures of this kind.
Conjecture 1.1 is perhaps the strongest among all of them. Some weaker conjectures are recently
resolved, and we now introduce them. In [F70], Furstenberg introduced the notion of CP-chains and
showed that if dimH A2 + dimH A3 < 0.5, then dimH A2 ∩ A3 = 0. One of the ﬁrst breakthroughs of
Conjecture 1.1 is the following result which appeared in [HS12]. This result settled an earlier sumset
conjecture of Furstenberg.

Theorem 1.2 (Hochman-Shmerkin). Let A2, A3 be closed ×2, ×3 invariant sets respectively. For all real
numbers u, v such that uv ̸= 0 we have the following result

dimH(uA2 + vA3) = max{1, dimH A2 + dimH A3}.

2010 Mathematics Subject Classiﬁcation. Primary: 11K55, 28A50, 28A80, 28D05, 37C45.
Key words and phrases. dynamical system, binary-ternary independence, discrepancy.

1

2 HAN YU

Intuitively speaking, the above result says that the projections of A2 × A3 along non-trivial di-
rections (i.e. not horizontal nor vertical) all attain the largest possible dimension. This somehow
indicates that the ﬁbres (i.e. intersections with lines orthogonal with the projecting direction) should
not be large. A precise form of the intersection result was proved in [S16] and [W19] independently
which improves Furstenberg’s original result. The following result settled an earlier intersection
conjecture of Furstenberg.

Theorem 1.3 (Shmerkin, Wu). Let A2, A3 be closed ×2, ×3 invariant sets respectively. For all real numbers
u, v such that u ̸= 0 we have the following result

dimB(A2 ∩ (uA3 + v)) ≤ min{0, dimH A2 + dimH A3 − 1}.

Here dimB is the upper box dimension and it will be discussed in Section 3.5. The above theorem
is a signiﬁcant step towards Conjecture 1.1. Notice that when dimH A2 + dimH A3 < 1 then we
have dimBA2 ∩ A3 = 0. This indicates that A2 ∩ A3 is small which strongly supports Conjecture 1.1.
From here, one might be curious about whether anything can be obtained beyond dimension zero.
Indeed, this is one of the main focus of this paper. There are other recent results around Furstenberg’s
intersection problem. See [Al20], [Au20], [BY18], [Y20] for further details.
We will show a stronger version of Furstenberg’s intersection result. In the statement, we en-
counter the notions of the Hausdorff dimension (dimH), the Assouad dimension (dimA), densities
and sparseness and invariant sets. They are deﬁned and discussed in details in Sections 3.5, 3.7, 4.2
and Section 3.6. For concreteness, the results we list here are about ×2, ×3 mod 1 invariant sets.
They still hold if we replace 2, 3 by p, q respectively such that log p/ log q /∈ Q. The bound O(N 27s)
below needs to be changed to O(N C(p,q)s) with constants C(p, q) depending on p, q.
We shall see that being sparse implies having zero dimension. The advantage of considering
sparseness is that it provides us with more quantitative understanding of the size of sets. For ex-
ample, instead of considering an individual intersection, one can consider all intersections at once
and the box-counting numbers can be controlled in a uniform way. We ﬁrst introduce the following
notion of spareness which provides us with a quantitative view of the ’topological smallness’ of a
compact subset of a line.

Deﬁnition 1.4. Let A ⊂ R be a compact set. We see that A is (super) sparse near 0 if

W (A) = {k ∈ N : A ∩ ([2
−k−1, 2
−k] ∪ [−2
−k, −2
−k−1]) ̸= ∅}

has upper (Banach) density 0. We call W (A) the sparse index of A near 0. More generally given any a ∈ A,
we deﬁne the sparse index of A near a by W (A, a) = W (A − a) and we say that A is (super) sparse near a if
and only if A − a is (super) sparse near 0. In general when l ⊂ R2 is contained in a line not parallel with the
Y -coordinate axis, we deﬁne W (A, a) as

W (A, a) = W (πY (A), πY (a)).

Now we state the main results of this paper.

Theorem 1.5. Let A2, A3 be closed ×2, ×3 invariant sets respectively and dimH A2 + dimH A3 = s < 1/2.
Then let l = lu,v = A2 ∩ (uA3 + v), u ̸= 0 be an intersection. The distance set |l − l| is supersparse near 0.
Moreover, we have the following bound which is uniform with respect to k ∈ N,

#(W (|l − l|) ∩ [k + 1, k + N ]) = O(N 27s).

AN IMPROVEMENT ON FURSTENBERG’S INTERSECTION PROBLEM 3

Theorem 1.6. Let A2, A3 be closed ×2, ×3 invariant sets respectively and dimH A2 + dimH A3 < 1. Then
let lu,v = A2 ∩ (uA3 + v), u ̸= 0 be an intersection. For all a ∈ lu,v, lu,v is super sparse near a. Moreover, for
each γ > 0, the following bound is uniform with respect to |u| ∈ (γ, γ−1), a ∈ lu,v, k ∈ N,

#(W (lu,v, a) ∩ [k + 1, k + N ]) = o(N ).

See Section 3.7 for the meaning of densities. A direct consequence of the above theorems is the
following corollary on a uniform version of box dimension estimate. This follows by applying The-
orem 1.6, Proposition 4.2 and the discussions below Proposition 4.2. We remark that this uniform
box dimension estimate is very useful in some problems concerning numbers with restricted digits,
see [BY18].

Corollary 1.7 (A uniform estimate for the upper box dimension). Let A2, A3 be closed ×2, ×3 invariant
sets respectively and dimH A2 + dimH A3 < 1. For each pair of real numbers u, v with u ̸= 0, let lu,v =
A2 ∩ (uA3 + v), u ̸= 0 be the intersection. Let γ > 0 be ﬁxed. For each ǫ > 0 there is an integer Nǫ such that
whenever |u| ∈ (γ, γ−1), v ∈ R N (lu,v, 2
−N ) ≤ 2
ǫN

for all N ≥ Nǫ.

A key tool for proving the above results is the notion of sparseness. This is where we make use of
the notation W (.)( see Section 4.2). Our notion of sparseness is a very natural indicator which says
that a set is small. We think this topic might be interesting on its own and we will give a detailed
treatment of the notion of sparseness. In Section 4.2 we will prove some relations between sparseness
and fractal dimensions. In particular, we show that being sparse implies having zero dimension but
the converse is in general not true. In particular, we have the following results as consequences:
• By Proposition 4.3: If dimH A2 + dimH A3 = s < 1/27 then Hg(lu,v) = 0 for the gauge function
g(x) = exp(−(− log x)27s).
• By Proposition 4.2: If dimH A2 + dimH A3 < 1 then dimA lu,v = 0.
In other words, lu,v is actually far away from having positive dimension if dimH A2 + dimH A3 is
small. The above weaker consequences already revisit partially the results (see Theorem 1.3 above)
of [S16] and [W19] on Furstenberg’s intersection conjecture. We note here that one can modify Wu’s
and Shmerkin’s methods to show that dimA lu,v = 0 as well.

1.2. Wu’s ergodic sampling theorem. A key step for Wu’s approach of Furstenberg’s intersection
problem is an ergodic sampling theorem proved as [W19, Theorem 6.1]. The precise statement is
rather technical and we will give a detailed discussion in Section 7. Here we only provide some
heuristics. Let S = {xn}n≥1 be a sequence of numbers in [0, 1], and we want to sample this sequence
by taking a subsequence S′ = {xnk }k≥1. Suppose that S equidistributes in [0, 1], and taking a random
subsequence S′ in a Bernoulli manner (by tossing a coin for each xn and decide whether or not put
it into S′) will almost surely keep the equidistribution property. Now, instead of randomly (in a
Bernoulli manner) choosing the subsequence S′, we can choose it according to some returning time
with respect to an auxiliary dynamical system (Y, T ) given y ∈ Y and A ⊂ Y :

nk = the integer i such that T i(y) ∈ A for the k-th time.

If (Y, T ) is a ‘complicated’ system, then we expect that some randomness can be extract and the
subsequence S′ will be still nicely distributed. [W19, Theorem 6.1] provides a precise result when

4 HAN YU

S is an irrational rotation orbit and (Y, T ) is a dynamical system with positive entropy. We will
provide a generalization of this result, see Theorem 7.8. Essentially, our result allows us to take S
to be a subsequence rather than the whole irrational rotation orbit. Although not straightforwardly,
we remark that one can actually modify Wu’s proof in [W19] for proving Theorem 7.8. We decide to
include a full detailed proof for this theorem in Section 7. There are other results in this direction,
see [Au20] and [Yu19].
 2. STRUCTURE OF THIS PAPER

In Section 3, we brieﬂy recall some basic terminology from dynamical systems, notions of dimen-
sions and densities of integer sequences. In Section 4, we introduce notions of sparseness and their
connections with fractal dimensions. We point out the importance of Section 4.3, the dipole direction
structure will be useful later. In Section 5, we prove some target hitting estimates using discrepancy
theory and use it in Section 6 for proving Theorem 1.5. We present in Section 7 a version of Sinai’s fac-
tor theorem which is closely related to but different than the version which appeared in [W19, Section
6]. Then ﬁnally in Section 8 we proof Theorem 1.6.

3. NOTATION

3.1. Filtrations, atoms and entropy. Let X be a set with σ-algebra X . A ﬁltration of σ-algebras is a
sequence Fn ⊂ X , n ≥ 1 such that F1 ⊂ F2 ⊂ · · · ⊂ X .

Given a measurable map S : X → X and a ﬁnite measurable partition A of X, we denote S−nA to
be the following ﬁnite collection of sets (notice that S might not be invertible)

{S−n(A) : A ∈ A}.

Then we use ∨n−1
i=0 S−iA to denote the σ-algebra generated by S−iA, i ∈ [0, n − 1]. An atom in
∨n−1
i=0 S−iA is a set A that can be written as
 A = ⋂

i Ci

where for each i ∈ {0, . . . , n − 1}, Ci ∈ S−iA. In other words, an atom in ∨n−1
i=0 S−iA can be also
described as follows. Given a sequence {Ai}n
i=0 ∈ An+1, we deﬁne the following set (which can be
empty) {x ∈ X : x ∈ A0, S(x) ∈ A1, . . . , Sn(x) ∈ An}.

The above set is an atom and all atoms have the above form. In this sense ∨n−1
i=0 S−iA is generated by
a ﬁnite partition An−1 of X which is ﬁner than A. Let µ be a probability measure. Then we deﬁne the
entropy of µ with respect to a ﬁnite partition A as follows

H(µ, A) = − ∑

A∈A µ(A) log µ(A).

We deﬁne the entropy of S as follows

h(S, µ) = lim
n→∞ 1
n H(µ, An−1),

AN IMPROVEMENT ON FURSTENBERG’S INTERSECTION PROBLEM 5

where A is a partition such that ∨∞
i=1S−iA = X . Here we implicitly used Sinai’s entropy theorem,
see [PY98, Lemma 8.8].

3.2. Dynamical systems and factors. A measurable dynamical system is denoted as (X, X , S, µ)
where X is a set with σ-algebra X and measure µ and a measurable map S : X → X. In case when
X is clear in context (for example Borel σ-algebra in Borel spaces) then we do not explicitly write it
down. Given two dynamical systems (X, X , S, µ), (X1, X1, S1, µ1), a measurable map f : X → X1
is called a factorization map and (X1, X1, S1, µ1) is called a factor of (X, X , S, µ) if µ1 = f µ and
f ◦ S = S1 ◦ f.

3.3. Dynamics on product sets and components. Let (X, S, µ) be a measurable dynamical system
with X = X1 × X2. Denote the projection function π1 : X → X1. Then the X1 component of the
measure µ is the projected measure π1µ. Let A be a collection of subsets of X. The X1 component
of A is π1A. In the case when S is a product or skew-product of maps, namely, for (x1, x2) ∈ X,
S(x1, x2) = (S1(x1), S2(x1, x2)), then (X1, S1, π1µ) is a factor of (X, S, µ) and π1µ is S1-invariant if µ
is S-invariant. We call (X1, S1, π1µ) the X1 component of (X, S, µ).

3.4. Equidistribution. Let X = {xn}n≥1 be a sequence in [0, 1]. We say that X equidistributes in [0, 1]
if for each interval [a, b] ⊂ [0, 1] we have the following result,

lim
N →∞ 1
N
 N∑

n=11[a,b](xn) = b − a = λ([a, b]),

where λ is the Lebesgue measure on [0, 1].

3.5. Dimensions. We will encounter (and have encountered) in this paper various notions of fractal
dimensions. We brieﬂy introduce the deﬁnitions. For more details on the Hausdorff and box dimen-
sions, see [F05, Chapters 2,3] and [M99, Chapters 4,5]. For the Assouad dimension, see [F14]. We
shall use N (F, r) for the minimal covering number of a set F in Rn with cubes of side length r > 0.

3.5.1. Hausdorff dimension. Let g : [0, 1) → [0, ∞) be a continuous function such that g(0) = 0. Then
for all δ > 0 we deﬁne the following quantity

Hg
δ (F ) = inf
 { ∞∑

i=1 g(diam(Ui)) : ⋃

i Ui ⊃ F, diam(Ui) < δ
}
 .

The g-Hausdorff measure of F is
 Hg(F ) = lim
δ→0 Hg
δ(F ).

When g(x) = xs then Hg = Hs is the s-Hausdorff measure and Hausdorff dimension of F is

dimH F = inf{s ≥ 0 : Hs(F ) = 0} = sup{s ≥ 0 : Hs(F ) = ∞}.

6 HAN YU

3.5.2. Box dimensions. The upper box dimension of a bounded set F is

dimBF = lim sup
r→0
 (− log N (F, r)
log r
 ) .

Similarly the lower box dimension of F is

dimBF = lim inf
r→0
 (− log N (F, r)
log r
 ) .

If the limsup and liminf are equal we call this value the box dimension of F and we denote it as
dimB F.

3.5.3. Assouad and modiﬁed Assouad dimensions. The Assouad dimension of F is

dimA F = inf
 {

s ≥ 0 : (∃ C > 0) (∀R > 0) (∀r ∈ (0, R)) (∀x ∈ F )

N (B(x, R) ∩ F, r) ≤ C (R
r
 )s }

,

where B(x, R) denotes the closed ball of centre x and radius R.
The modiﬁed Assouad dimension of F is

dimmA F = inf {sup
i∈N{dimA Fi} : F ⊂ ∪iFi
} .

In particularly any countable set has modiﬁed Assouad dimension 0 and it is easy to see that

dimmA F ≤ dimA F.

3.6. ×p mod 1 invariant sets. In this paper, given an integer p ≥ 2, we use Ap to denote an arbitrary
closed ×p mod 1 invariant subset of [0, 1]. This is to say, for all a ∈ Ap, {pa} ∈ Ap, where {x} is the
fractional part of x. We say that Ap is strictly invariant if a ∈ Ap ⇐⇒ {pa} ∈ Ap. For each closed
×p mod 1 invariant set Ap, it is known ( [F08, Theorem 5.1]) that dimH Ap = dimBAp. In particular
for any integers p, q ≥ 2, dimH Ap × Aq = dimBAp × Aq.

3.7. Densities of integer sequences. We also work with various notions of densities of integer se-
quences. We recall two notions of density for integer sequences.

Deﬁnition 3.1. The upper natural density of W is deﬁned as

d(W ) = lim sup
n→∞ #{W ∩ [1, n]}
n .

Similarly, we deﬁne the lower natural density by replacing the above lim sup with lim inf and write it as d(W ).
If these two numbers coincide we call it the natural density of W and write it as d(W ).

Deﬁnition 3.2. The upper Banach density of W is deﬁned as

dB(W ) = lim sup
k,M →∞
 1
k (#{W ∩ [M, M + k − 1]}).

AN IMPROVEMENT ON FURSTENBERG’S INTERSECTION PROBLEM 7

3.8. The big O and small o notations. Let f, g : N → [0, ∞) be two functions. We write

f = O(g)

if there exists positive number C > 0 such that

f (k) ≤ Cg(k)

for all k ∈ N. Similarly we write f = o(g)

if for any ǫ > 0 there exists N ∈ N such that for all k ≥ N we have

f (k) ≤ ǫg(k).

In some occasions there is another parameter set S and we have functions f, g : N × S → [0, ∞). For
each c ∈ S we write f = Oc(g), oc(g) to indicate that the above tendencies depend on the choice of c.
We say that f = O(g), o(g) uniformly for c ∈ S if the above tendencies do not depend on the choice
of c.

3.9. Weak convergence of measures and the Portmanteau theorem. In Section 8, we need the notion
of weak * convergence of measures and the Portmanteau theorem. Let µk, k ≥ 1 be a sequence of
probability measures on a Borel space X. We say that µk → µ in weak * sense (or weakly) if for all
bounded continuous functions f : X → R

lim
k→∞
 ∫

X f dµk = ∫

X f dµ.

The following version of the Portmanteau theorem is taken from [K06, Theorem 13.16] and [Su14,
Theorem 1.3].

Theorem 3.3 (Portmanteau theorem). Let µk, k ≥ 1 be a sequence in P(X) (the space of Borel probability
measures supported on X) where X is a Borel space. Let µ ∈ P(X). The following statements are equivalent:
1 : µk → µ weakly;
2 : lim supk µk(K) ≤ µ(K) for all closed subsets K of X;
3 : limk→∞ ∫
X f dµk = ∫

X f dµ for bounded and µ-almost everywhere continuous real valued functions
f on X.

There are a lot of other equivalent statements for the Portmanteau theorem, for more details,
see [Su14] and the references therein. One particular use of the above result is related to invari-
ant measures of almost continuous dynamical systems. More precisely, let X be a compact metric
space. Let T : X → X be a map (not necessary continuous). For each integer n ≥ 1, let xn ∈ X
be arbitrarily chosen and let µn = (n + 1)−1 ∑n
i=0 δT i(xn) be a sequence of probability measures on
X. Let µ be a weak * limit point of this sequence. In the case when T is continuous, we know that
µ is T -invariant. This is the content of Kryloff-Bogoliouboff theorem. We can extend this result if
T is only assumed to be µ-almost everywhere continuous. In fact, for any f ∈ C(X), we have the
following result for a sequence of integers {ik}k≥1 such that ik → ∞,
∫

X f (x)dµ(x) = lim
k→∞
 ∫
X f (x)dµik (x).

8 HAN YU

Now we want to consider the same for the function f ◦ T. It is continuous at where T is continuous.
Then we see that f ◦T is µ-almost everywhere continuous. We have the following result (by Theorem
3.3(3)), ∫
X f (T (x))dµ(x) = lim
k→∞
 ∫
X f (T (x))dµik (x) = lim
k→∞ 1
ik + 1
 ik∑

i=0 f (T (T i(xik ))).

The last term is equal to

lim
k→∞ 1
ik + 1
 ( ik∑

i=0 f (T i(xik )) + f (T ik+1(xik )) − f (xik )

)

which is the same as (recall that f is bounded)

lim
k→∞ 1
ik + 1
 ik∑

i=0 f ((T i(xik )) = ∫

X f (x)dµ(x).

This shows that µ is T -invariant. In general, it is not simple to show that T is µ-almost everywhere
continuous. There are some special cases when this is possible to be checked, see for example [W19,
Section 5.2].
 4. SPARSENESS AND DIPOLES

In this section, we introduce our key tools for approaching Furstenberg’s intersection problem.
The ideas behind the deﬁnitions are very natural and straightforward, however, we are not able to
ﬁnd any direct references. We decide to give a detailed treatment which will be more than what we
need for Furstenberg’s intersection problem.

4.1. Doubling measures. Later we shall use some facts about doubling measures. Here we are in-
terested in doubling measures supported on compact subsets of R. We have the following result. The
proofs can be found in [VK], [L98, Theorem 6.10] and [KRS12].

Theorem 4.1. Let A ⊂ R be a compact set. Then there is a doubling probability measure supported on A.
Namely, there is a measure µ ∈ P(A) and there exists an absolute constant (called the doubling constant for
R) D ≥ 1 such that for all a ∈ A and r > 0,

0 < µ(B(x, 2r)) ≤ Dµ(B(x, r)) < ∞.

According to [L98, Section 6.13], the constant D for R can be chosen to be 2 × 3 × 4 × 95.

4.2. Sparseness. We call the notion of spareness (Deﬁnition 1.4).

Deﬁnition. Let A ⊂ R be a compact set. We see that A is (super) sparse near 0 if

W (A) = {k ∈ N : A ∩ ([2
−k−1, 2
−k] ∪ [−2
−k, −2
−k−1]) ̸= ∅}

has upper (Banach) density 0. We call W (A) the sparse index of A near 0. More generally given any a ∈ A,
we deﬁne the sparse index of A near a by W (A, a) = W (A − a) and we say that A is (super) sparse near a if
and only if A − a is (super) sparse near 0. In general when l ⊂ R2 is contained in a line not parallel with the
Y -coordinate axis, we deﬁne W (A, a) as

W (A, a) = W (πY (A), πY (a)).

AN IMPROVEMENT ON FURSTENBERG’S INTERSECTION PROBLEM 9

It is easy to see that (super) sparseness is insensitive with respect to scaling. That is to say, if
W (A, a) has upper natural density 0, then for each real number c ̸= 0, W (cA, ca) also has natural
density 0. A similar result holds for upper Banach density as well.
Given any set A ⊂ R, we denote |A − A| as its distance set. Intuitively, if |A − A| is sparse near
0 then A cannot be too large. A less restrictive notion is uniform sparseness. That is to say, for each
δ > 0, there is an integer Nδ such that #W (A, a) ∩ [1, . . . , N ] ≤ δN for all a ∈ A, N ≥ Nδ. Similar
notion of uniform super sparseness can be formulated as well. In particular, if |A − A| is (super)
sparse then A is uniformly sparse.

Proposition 4.2. We have the following results.

• 1: Given any uniformly sparse set A ⊂ R, we have dimBA = 0.
• 2: If A is uniformly super sparse then dimA A = 0.
• 3: Let A ⊂ [0, 1] be a compact set such that for all a ∈ A, A is super sparse near a then

dimmA A = 0.

• 4: The converses of the above are in general not true. On the other hand, if A is ﬁnite then it is
uniformly super sparse.

Proof. The proofs for (1) and (2),(3) are very similar and we only write the proof for (1). First observe
that the last conclusion of (4) is trivial. We now illustrate the ﬁrst part of (4). Let A0 be the set
{0} ∪ {2−k}k≥0 ⊂ [0, 1]. We see that dimBA0 = 0 but we can see that A0 is not sparse near 0 and
therefore it is not uniformly sparse. Now we consider (1). Let A ∈ [0, 1] be a uniformly sparse set.
Then we see that the following set has 0 upper natural density uniformly across a ∈ A,

W (A, a) = {k ∈ N : |A − A| ∩ [2
−k−1, 2
−k] ̸= ∅}.

Since A is compact we assume that it is contained in [0, 1]. To bound the upper box dimension of A
we shall use Theorem 4.1 and ﬁnd a doubling (with doubling constant D > 0) probability measure
supported on A. Let a ∈ A be arbitrarily chosen and for any integer n ≥ 0 we can ﬁnd a nested
sequence of intervals a ∈ B(a, 2−n) ⊂ · · · ⊂ B(a, 1). Since we assumed that A ⊂ [0, 1] therefore we
see that µ(B(a, 1)) = 1. Now we make use of the uniform sparseness of |A − A|. It is clear that if
A ∩ B(a, 2−j) \ B(a, 2−j−1) ̸= ∅ then j ∈ W (A, a). This means that A ∩ B(a, 2−j ) = A ∩ B(a, 2−j−1) if
j /∈ W (A, a). Then we write

µ(B(a, 2
−n)) = µ(B(a, 1))
 n−1∏

j=0
 µ(B(a, 2−j−1))
µ(B(a, 2−j)) .

If j /∈ W (A, a) then A ∩ B(a, 2−j) \ B(a, 2−j−1) = ∅ therefore we see that,

µ(B(a, 2−j−1))
µ(B(a, 2−j)) = 1,

otherwise if j ∈ W (A, a) we can still write

µ(B(a, 2−j−1))
µ(B(a, 2−j )) ≥ D−1.

10 HAN YU

Since W (A, a) has natural density 0 uniformly across a ∈ A, we see that for all ǫ > 0 there exist a Nǫ
such that for all a ∈ A, N ≥ Nǫ we have

#W (A, a) ∩ [1, N ] ≤ ǫN.

Then we see that for all N ≥ Nǫ µ(B(a, 2
−N )) ≥ D−ǫN .
We can cover A with disjoint intervals of length 2−N −1 and denote the collection of such intervals as
NN +1, then for any I ∈ NN +1 there is a a ∈ I∩A such that I ⊂ B(a, 2−N ) and therefore µ(I) ≥ D−ǫ(N ).
Since µ is a probability measure we see that

#NN +1 ≤ DǫN .

This implies that dimBA ≤ ǫ log D/ log 2. and because ǫ can be arbitrarily chosen we see that dimBA =
0. This ﬁnishes the proof of (1). The proofs of (2), (3) are similar and we omit the details. □

Since the doubling constant D can be chosen independently with respect to A we see that with the
uniform sparseness assumption, for each ǫ > 0 there is an integer Nǫ such that

N (A, 2
−n) ≤ Dǫn

for all n ≥ Nǫ. Therefore, if we have a collection of compact sets {Ai}i∈I of [0, 1] and we assume
uniform sparseness uniformly across i ∈ I then for each ǫ > 0 there is an integer Nǫ and for all
n ≥ Nǫ, i ∈ I we have N (Ai, 2
−n) ≤ Dǫn.
In general, if we can control W (A, a) individually for all a ∈ A then it is possible to say something
about the Hausdorff measure of A with respect to a certain gauge function.

Proposition 4.3. Let A ⊂ [0, 1] be a compact set. Let f : [0, ∞) → [0, ∞) be such that for all a ∈ A,

#W (A, a) ∩ [1, N ] = oa(f (N )) as N → ∞.

We write a gauge function as g(x) = exp(−f (1 − log x/ log 2)) for x ∈ (0, 1). Then we have Hg(A) < ∞.

Proof. Since A is compact we can ﬁnd a doubling probability measure with doubling constant D on
it, see Theorem 4.1. Let c > 0 be an arbitrarily chosen constant. Then for each a ∈ A, because of
the sparseness of A around a with a similar argument as in the proof of Lemma 4.2 we see that there
exists an integer Na such that whenever N ≥ Na we have

µ(B(a, 2
−N )) ≥ D−f (N )/c.

Since A is compact we see that there is a ﬁnite collection of intervals of form Ia = B(a, Na) that covers
A. By Besicovitch’s covering lemma( [M99, Chapter 2, Section 7]) we see that there exists an absolute
constant C > 0 and for a ﬁnite subset A′ of A such that
∑

a∈A′ D−f (Na)/c ≤ ∑

a∈A′ µ(Ia) ≤ C.

Now we choose c = max{log D, 1}. Notice that f (Na) = f (− log 2−Na/ log 2) and 2−Na+1 is the length
of Dka(a). Let ra be the length of Ia, we see that for an absolute constant C > 0,
∑

a∈A′ exp(−f (1 − log ra/ log 2)) ≤ C.

AN IMPROVEMENT ON FURSTENBERG’S INTERSECTION PROBLEM 11

It is clear that we can bound maxa∈A′ ra to be arbitrarily small. This implies that Hg(A) < ∞. □

In particular if f (N ) = o(N ) then we see that dimH A = 0. If f (N ) = o(N σ) for σ ∈ (0, 1) then we
can choose g(x) = exp(−(− log x)σ).

4.3. Dipole set. Let C > 1. Then there is a constant c > 0 such that the following holds for all small
enough δ > 0 :
Let A ⊂ R2 be a compact subset. Let E ⊂ [0, 2π] be a δ-separated set of directions. Suppose that
for each e ∈ E we can ﬁnd xe, ye ∈ A such that

|ye − xe| ∈ [C −1, C]

and ye − xe points towards the direction e. Then we have N (A, δ) ≥ c
√#E.
To see this, we only need to cover A with disjoint δ-cubes. As long as δ is small enough, there is a
number c′ > 0 so that if there is a δ-cube containing M points of form xe then the corresponding ye
are all at least c′δ-separated from each other. Therefore we have N (A, δ) ≥ c′M/2. On the other hand
if non of the δ-cubes contain more than M many points of form xe then N (A, δ) ≥ #E/M. Then we
see that for all integer M ,
 N (A, δ) ≥ max {
c
′M/2, #E/M } ≥ √c′/2√#E.

Deﬁnition 4.4. Let A ⊂ R2 be a compact subset, the dipole direction set of A is deﬁned as follows,

DD(A) = { x − y
|x − y| : |x − y| ∈ [1/6, 1.5], x, y ∈ A
} .

It is easy to see that when A is compact DD(A) is also compact. We have shown the following
lemma.

Lemma 4.5. For all compact subset A ⊂ R2, we have the following result

dimBA ≥ 0.5dimBDD(A).

5. IRRATIONAL ROTATIONS, DISCREPANCY AND TARGET HITTING

Let α ∈ (0, 1) be an irrational number. Consider the rotation system Rα : [0, 1] → [0, 1] deﬁned as
follows, Rα(x) = x + α mod 1.

Then for any compact subset A ⊂ [0, 1], by Birkhoff’s ergodic theorem( [PY98, Theorem 10.6]) we see
that for Lebesgue almost all x ∈ [0, 1],

lim
N →∞ 1
N
 N −1∑

n=01A(Rn
α(x)) = λ(A),

where λ is the Lebesgue measure on [0, 1]. This implies that when A is small we expect that n ≥
0, Rn
α(x) ∈ A happens not so often. It is known that the circle rotation system with irrational α is
uniquely ergodic therefore it is expected that Rn
α(0) ∈ A happens not so often.

12 HAN YU

Lemma 5.1. Let A ⊂ [0, 1] be a compact set and for any irrational number α ∈ (0, 1) we construct the
following sequence, W = {k ∈ N : Rk
α(0) = {kα} ∈ A}.

Then the upper Banach density of W is at most λ(A).

Proof. For any ǫ > 0, we can cover A with intervals A ⊂ ⋃i∈I Ii such that I is a ﬁnite set and
∑

i∈I λ(Ii) ≤ λ(A) + ǫ.

Then we can approximate each1Ii with a continuous function fi : [0, 1] → [0, 1] such that fi(x) = 1
for x ∈ Ii and fi(x) = 0 for x /∈ (1 + ǫ)Ii, where (1 + ǫ)Ii is the interval with the same centre as Ii
but its length is equal to (1 + ǫ) times that of Ii. Then because of the unique ergodicity we see that for
each i ∈ I and x ∈ [0, 1),
 lim
N →∞ 1
N
 N −1∑

i=0 fi(Ri
α(x)) = ∫ fidλ.

Furthermore the above limit holds uniformly across x ∈ [0, 1). Therefore for each i ∈ I there is a
number Ni which does not depend on x such that for each N ≥ Ni and x ∈ [0, 1),

1
N
 N −1∑

i=0 fi(Ri
α(x)) ≤ (1 + ǫ) ∫ fidλ ≤ (1 + ǫ)
2λ(Ii).

Now let Nǫ = maxi∈I Ni (this is where we use the ﬁniteness of I) and we see that for any integers
a, M such that M ≥ Nǫ we see that

W ∩ [a + 1, a + M ] ⊂ {k ∈ [a + 1, a + M ] : {kα} ∈ A} ⊂ ⋃

i∈I{k ∈ [a + 1, a + M ] : {kα} ∈ Ii}.

Since M ≥ Nǫ for each i ∈ I we see that

#{k ∈ [a + 1, a + M ] : {kα} ∈ Ii} ≤
 M −1∑

k=0 fi(Ri
α(Ra
α(0))) ≤ (1 + ǫ)
2λ(Ii)M.

This implies that
 #W ∩ [a + 1, a + M ] ≤ ∑

i∈I (1 + ǫ)
2λ(Ii)M ≤ (1 + ǫ)
2(λ(A) + ǫ)M.

Since ǫ > 0 and M > Nǫ can be chosen arbitrarily we see that the upper Banach density of W is at
most λ(A). □

It is natural to consider what happens when A is small in dimension. For this purpose we need to
consider error terms in ergodic limits. We will be most interested in the cases when α = log p/ log q
and α /∈ Q. It was proved in [B15] that there are numbers C(α), c(α) > 0 such that for all integers
n, m ≥ 1 ∣
∣
∣α − m
n
 ∣
∣
∣ ≥ c(α) 1
nC(α) . (1)

AN IMPROVEMENT ON FURSTENBERG’S INTERSECTION PROBLEM 13

The best known example in this kind is when α = log 2/ log 3 and in this case, see [R85, proposition
and formula (6)(7) on page 160] the above inequality can be written as
∣
∣
∣α − m
n
 ∣
∣
∣ ≥ 0.00000000000001 1
n14.3 .

Since for any two different integers i1, i2 we have

|{i1α} − {i2α}| = |i1α − i2α − M1 + M2|,

where M1 = ⌊i1α⌋, M2 = ⌊i2α⌋. We see that

|i1α − i2α − M1 + M2| = |i1 − i2| ∣
∣
∣
∣α − M1 − M2
i1 − i2
 ∣
∣
∣
∣ .

As we can assume that i1 > i2, the inequality (1) implies that

|{i1α} − {i2α}| = |i1 − i2| ∣
∣
∣
∣α − M1 − M2
i1 − i2
 ∣
∣
∣
∣ ≥ c(α) 1

i
C(α)−1
1 . (GAP)

This is the key point of the inequality (1) that we shall use.

Lemma 5.2. Let A ⊂ [0, 1] be a set with dimBA = s < 1, then for any irrational number of form α =
log p/ log q with two integers p, q > 0, we have the following inequality holds for all ǫ ∈ (0, 1 − s),

N −1∑

n=01A(Rn
α(0)) = Oα,ǫ(N C(α)(s+ǫ)),

where C(α) > 0 is a constant depends only on α.

Remark 5.3. This lemma applies better in the case when s is small. For example if α = log 2/ log 3 then when
s < 1/14 we have the following polynomial bound,

N −1∑

n=01A(Rn
α(0)) = O(N 0.95).

Proof. Let N be a large integer and we consider the following sequence

SN (α) = {{iα}}i∈[0,N ].

Then it is clear that elements in SN (α) never coincide because α is an irrational number. Then by
inequality (GAP) we see that there exist positive numbers c(α), C(α) > 0 such that for any x, y ∈
SN (α) with x ̸= y,
 |x − y| ≥ c(α)N −C(α)+1.

Now we choose rN = N −C(α)+1 and cover A with kN = N (A, rN ) many disjoint rN -intervals. We
denote again the union of those rN -intervals as ArN . Then we see that

N −1∑

n=01ArN (Rn
α(0)) = Oα(kN ).

14 HAN YU

This is because each rN -interval we use to cover A contains at most Oα(1) many points in SN (α).
Then because of the dimension requirement of A we see that for any ǫ > 0,

kN = Oǫ(r−s−ǫ
N ).

Therefore we see that for a constant C ′(α) we have

N −1∑

n=01ArN (Rn
α(0)) = Oα,ǫ(N C′(α)(s+ǫ)).

This proves the result. □

6. SMALL SETS, DIPOLE CONFIGURATIONS

In this section we study A2 ∩ (uA3 + v) when dimH A2 + dimH A3 < 1/2. Furstenberg studied this
intersection in [F70], in particular, he showed that dimH A2 ∩ (uA3 + v) = 0 for all u ̸= 0. In this
section, we provide a more straightforward argument and a stronger result.

Proof of Theorem 1.5. We consider the product set K = A3 × A2. Then l is, up to rescaling, the same as
lK = l′ ∩ K with l′ = {y = ux + v}. For convenience we require that u > 1 but we note that the cases
for other u ̸= 0 are similar. Now we want to show that |lK − lK | is super sparse near 0. We denote
WK = W (|lK − lK |) and we want to show that WK has zero upper Banach density. Now for each
k ∈ WK we can ﬁnd xk, yk ∈ lK such that

|yk − xk| ∈ [2
−k−1, 2
−k].

Without loss of generality we shall assume that the vector yk − xk has positive Y -component. Now
let α = log 2/ log 3 and we can construct the map T = R2 × [0, 1] → R2 × [0, 1],

T ((t1, t2), t) =
 {
((t1, 2t2), Rα(t)), if t + α ≤ 1

((3t1, 2t2), Rα(t)), if t + α > 1

Now let x, y ∈ R2 be two different points such that the line segment xy is not parallel to the coordinate
axis. Then we can ﬁnd the following sequence of pairs of points in R2,

((xn, tn) = T n(x, 0), (yn, tn) = T n(y, 0))n≥0.

Now construct the following sequences,

(θ1,n, θ2,n) = yn − xn
|xn − yn| ∈ S1, θn(x, y) = log ( θ2,n
θ1,n
 ) .

Then we see that θ0(x, y) = log ( θ2,0
θ1,0
 ) and in general for each integer n ≥ 1,

θn(x, y) = log 3{n log 2/ log 3} + θ0.

Now we apply the above map T for k times with initial pair xk, yk and end up with the pair

((x, tk) = T k(xk, 0), (y, tk) = T k(yk, 0)).

AN IMPROVEMENT ON FURSTENBERG’S INTERSECTION PROBLEM 15

Then we see that θk(xk, yk) = log 3{k log 2/ log 3} + θ0(xk, yk) ∈ (log u, log u + log 3). We want to
estimate the distance |x − y|, the Y -component of yk − xk lies in [2−k−1/
√2, 2−k]. Therefore we see
that the Y -component of y − x lies in [0.5/
√2, 1] thus we see that

|y − x| ∈ [1/6, 1.5].

We still have to perform the mod 1 operation on each coordinate component of x and y. Denote the
following doubled set of K

˜K = K ∪ (K + (0, 1)) ∪ (K + (1, 0)) ∪ (K + (1, 1)),

then because |y − x| ∈ [1/6, 1.5], we can ﬁnd ˜y, ˜x ∈ ˜K such that

˜y − ˜x = y − x.

For each k ∈ WK we have seen that there is a pair of points x, y ∈ ˜K with |x − y| ∈ [1/6, 1.5] such that
the direction vector y − x has slope u3
{k log 2/ log 3}.

We denote the map e : [0, 1] → S1 such that e(t) is the direction vector in S1 ⊂ R2 with slope u3t. It is
easy to see that this map is smooth; therefore it is bi-Lipschitz. Then we see that

e ({k log 2/ log 3}k∈WK ) ⊂ DD(K).

However the dipole direction set DD(K) has upper box dimension at most 2s < 1 and therefore
its Lebesgue measure is 0. By Lemma 5.1 WK must have upper Banach density 0. For the sec-
ond conclusion, let N be a large integer and a be an arbitrarily chosen integer. We notice that
{k log 2/ log 3}k∈[a,a+N ]∩WK consists rN -separated points for rN = N −13.3, see Lemma 5.2. Let ǫ > 0
be a small number then for all large enough N we see that

#WK ∩ [a, a + N ] ≤ ( 1
rN
 )2s+ǫ .

If we choose ǫ to be small enough we see that

#WK ∩ [a, a + N ] = O(N 27s).
 □

7. SINAI’S FACTOR THEOREM: CASINO WITH CLOCKS

In this section we introduce Sinai’s factor theorem and prove Theorem 7.8. The main technicalities
here are similar to that in [W19, Section 6] and our Theorem 7.8 can be seen as a generalization
of [W19, Theorem 6.1].
To have a intuitive idea in mind, consider a sequence of i.i.d random variables {Xn}n≥1 with values
in {0, 1} For any irrational number α we consider the sequence {XnRn
α(0)}n≥1. Intuitively, imagine a
casino with a clock (which is unrealistic) with only one ﬁnger rotating with irrational angular speed
( +α mod 1 system). Whenever a gambler throws a coin with head up then he will check the clock.
Then a sample path of the above random sequence would be a series of time a gambler observed.
The results in this section can be intuitively stated as follows. For each gambler, almost surely, the
time series he observed equidistributes in [0, 1], that is, the time series he observed does not depend

16 HAN YU

on whether he is winning or losing. We shall discuss various different aspects towards the above
intuition.

7.1. Bernoulli system. Let Λ be a ﬁnite set of symbols and let Ω = ΛN be the space of one sided
inﬁnite sequences over Λ. We deﬁne S to be the shift operator, namely, for ω = ω1ω2 · · · ∈ Ω,

S(ω) = ω2ω3 . . . .

Then we take a σ-algebra on Ω generated by cylinder subsets. A cylinder subset Z ⊂ Ω is such that
Z = ∏i∈N Zi and Zi = Λ for all but ﬁnitely many integers i ∈ N. We construct a probability measure
µ on Ω by giving a probability measure µΛ = {pλ}λ∈Λ on Λ and set µ = µN
Λ. We require here that
pλ ̸= 0 for all λ ∈ Λ. Then this system is weak-mixing and has entropy h(S, µ) = ∑λ∈Λ −pλ log pλ.
We call this system a Bernoulli system. We can also introduce a metric topology on Ω by deﬁning
d(ω, ω′) = #Λ− min{i∈N:ωi̸=ω′
i}. This turns Ω into a compact and totally disconnected space. For ω ∈ Ω
and r ∈ (0, 1), we use B(ω, r) to denote the r-ball around ω with radius r with respect to the metric d
constructed above.

7.2. Sinai’s factor theorem.

Theorem 7.1 (Sinai’s factor theorem). Let (X, S, µ) be an ergodic dynamical system. Then any Bernoulli
system (Ω, SB, ν) with h(SB, ν) ≤ h(S, µ) is a factor of (X, S, µ).

Let Ber = (Ω, S, µ) be a Bernoulli system on Ω = ΛN. Let α ∈ (0, 1) be an irrational number.
Heuristically, the dynamical system T looks like a stochastic process with a sequence of i.i.d random
variables. For any B ⊂ Ω with µ(B) > 0 and ω ∈ Ω the following set

K(ω, B) = {k ∈ N : Sk(ω) ∈ B}

can be realized as randomly constructed by choosing each k ∈ N independently with probability
µ(B). Then for any subset K ′ ⊂ N the chance that K(ω, B) ∩ K ′ = ∅ is (1 − µ(B))#K ′ and it is small
when #K ′ is large unless µ(B) = 0 which we assumed not to be the case.

Deﬁnition 7.2. Let (X, S, µ) be a dynamical system and let B ⊂ X be a subset. Then we can construct the
following sequence
 K(x, B) = {k ∈ N : Sk(x) ∈ B},

and the following set for α ∈ [0, 1),
 AK(x,B)(α) = {Rk
α(0)}k∈K(x,B).

Lemma 7.3. Consider the Bernoulli system (Ω, S, µ). Let {Bi}i∈I be a ﬁnite pairwise disjoint family of
measurable subsets of Ω. Suppose that ∑i∈I µ(Bi) ≥ 1 − δ for a δ ∈ (0, 1). Then there exists a set Ω′ ⊂ Ω
with full µ-measure such that for each ω ∈ Ω and any integer sequence K of lower natural density ρ larger
than δ, there exists an i = i(ω, K) ∈ I such that

AK(ω,Bi)∩K

has Lebesgue measure at least ρ − δ.

AN IMPROVEMENT ON FURSTENBERG’S INTERSECTION PROBLEM 17

Proof. For each i ∈ I, K(ω, Bi) can be essentially viewed as a random sequence of integers obtained
by deciding to choose each integer independently with probability µ(Bi). It is helpful to have this
intuition in mind for what follows. We see that for almost all ω ∈ Ω, by the ergodicity of Bernoulli
systems, d(K(ω, Bi)) = µ(Bi),
and the sequence of real numbers {Rk
α(0)}k∈K(ω,Bi) equidistributes in [0, 1] (we re-enumerate K(ω, Bi)
with N). This can be seen by considering the dynamical system (Ω × [0, 1], S × Rα, µ × λ) (λ is the
Lebesgue measure) which is ergodic because it is the product of a weakly mixing and a uniquely
ergodic system, see also [W19, Lemma 6.5]. Since I is a ﬁnite family, we see that for almost all ω ∈ Ω,
for each i ∈ I the above results hold. We denote this full measure set as Ω′. We see that for each
ω ∈ Ω′
 d(∪i∈I K(ω, Bi)) ≥ 1 − δ.
Now let K be an arbitrarily chosen sequence with lower natural density ρ > δ, then we see that
K ∩ (∪i∈I K(ω, Bi)) has lower natural density at least ρ − δ > 0. We denote for each i ∈ I, Ki =
K ∩ K(ω, Bi) and ρi = d(Ki). Then we see that
∑

i∈I ρi ≥ ρ − δ.

Now if ρi < (ρ − δ)µ(Bi) for all i ∈ I we see that

(ρ − δ) ∑

i∈I µ(Bi) > ∑

i∈I ρi ≥ ρ − δ.

This implies that ∑i∈I µ(Bi) > 1 and it is impossible. So we see that there exists an i ∈ I such that
ρi ≥ (ρ − δ)µ(Bi). Now we denote ǫ = ρ − δ. For this i we see that K(ω, Bi) \ Ki has lower natural
density at most µ(Bi) − ρi ≤ (1 − ǫ)µ(Bi).
Now by the equidistribution property we see that for any interval I ⊂ [0, 1],

K ′′ = {k ∈ K(ω, Bi) : Rk
α(0) ∈ I}

has natural density µ(Bi)|I| and therefore if |I|µ(Bi) > (1 − ǫ)µ(Bi) then K ′′ has natural density
strictly larger than (1−ǫ)µ(Bi). Therefore Ki∩K ′′ cannot be empty and thus we have I ∩AK(ω,Bi)∩K ̸=
∅. This argument works for ﬁnite unions of intervals as well. For any ﬁnite collection of intervals with
disjoint interiors Ij, j ∈ J with total length ∑j∈J |Ij| > 1 − ǫ we see that


 ⋃

j∈J Ij


 ∩ AK(ω,Bi)∩K ̸= ∅.

Then we see that Ac
K(ω,Bi)∩K is open and has Lebesgue measure at most 1 − ǫ. This is because for any
open set O ⊂ [0, 1], there exist a countable family Lm, m ≥ 1 of intervals with disjoint interior such
that ∑m |Lm| = λ(O), where λ is the Lebesgue measure, see [SS05, Theorem 1.3]. Then for any η > 0
we can ﬁnd a ﬁnite collection of those intervals with total length at least λ(O) − η. We can apply this
argument for Ac
K(ω,Bi)∩K and for arbitrary small η > 0. As a result we see that λ(AK∩K(ω,Bi)) ≥ ǫ as
required. □

18 HAN YU

Theorem 7.4. Let (X, S, µ) be an ergodic dynamical system with h(S, µ) > 0. We can ﬁnd a Bernoulli factor
Ber = (Ω, SB, ν) of (X, S, µ) with h(SB, ν) = h(T, µ) > 0. Denote f : X → Ω to be the factorization map.
For a δ > 0, let Bi, i ∈ I be a ﬁnite disjoint collection of measurable subsets in Ω with ∑i∈I ν(Bi) ≥ 1 − δ.
Then for µ almost all x ∈ X, for any integer sequence K with lower natural density ρ > δ there exist an i ∈ I
such that AK∩Hi(x)(α) has Lebesgue measure at least ρ − δ,

where Hi(x) = {k ∈ N : Sk(x) ∈ f −1(Bi)}.

Proof. We can ﬁnd a Bernoulli factor Ber = (Ω, SB, ν) of (X, S, µ) with h(SB, ν) = h(S, µ) > 0. The a
straightforward application of Theorem 7.4 gives us the result. □

When Ber is a factor of (X, S, µ) with the same entropy, then intuitively all the complicities are
carried by Ber and therefore the ﬁbres of f should not be too complicated with respect to the map S.
The following result expresses this intuition in a clear way. The following result is known as Rohlin’s
disintegration theorem, and we adopt the version in [S12].

Deﬁnition 7.5. Let f : X → Y be a measurable map between two measurable spaces and let µ be a measure on
X with projection µY = f µ on Y . We call a collection of measures {µy}y∈Y a system of conditional measures
if the following properties hold,
1 : For all y ∈ Y , µy is a measure supported on f −1(y) and for µY almost all y ∈ Y , µy is a probability
measure.
2 : We have the law of measure disintegration. For all Borel set B ⊂ X, we have

µ(B) = ∫ µy(B)dµY (y).

If X, Y are also metric spaces (f need not to be continuous) we require further that the following holds for µY
almost all y ∈ Y .
3 : µy = limr→0 µf −1(B(y,r)), where the limit is in the weak* sense and µf −1(B(y,r)) is the conditional
measure of µ on f −1(B(y, r)), namely, for any Borel set B ⊂ X with positive µ measure,

µf −1(B(y,r))(B) = µ(B ∩ f −1(B(y, r)))
µ(B) .

Theorem 7.6. Let f : X → Y be a measurable map between two metric spaces with corresponding Borel
σ-algebra. Then there exists a system of conditional measures.

Then we have the following result due to [W19, Lemma 6.4] which is a direct consequence of the
conditional Shannon-McMillan-Breiman theorem, Egorov’s theorem and the Portmanteau theorem.

Theorem 7.7 (Wu). Let (X, S, µ) be an ergodic dynamical system with X being a Borel space. Let A be a ﬁnite
partition of X such that ∨∞
i=0S−iA generates the sigma-algebra of X. For each x ∈ X not on the boundaries
of sets in ∨n
i=1S−iA, for each n ∈ N we denote An(x) the unique atom A of ∨n
i=0S−iA such that x ∈ A.
If µ does not give positive measures to boundaries of S−iA for all i ∈ N and h(S, µ) > 0 then there exist
a Bernoulli factor (Ω, SB, ν) with measurable factorization map f : X → Ω and for each δ > 0 there exist a
Xδ ⊂ X and a constant Cδ with the following properties,
1 :µ(Xδ) > 1 − δ.
2 :For all x ∈ Xδ and n ≥ 1, µf (x)(An(x)) ≥ Cδ2−nδ and µf (x) is a probability measure.

AN IMPROVEMENT ON FURSTENBERG’S INTERSECTION PROBLEM 19

3 :For all integers n ≥ 1, there exists a measurable set Bn
δ ⊂ Ω with ν(Bn
δ ) ≥ 1−δ and a r = r(δ, n) > 0
such that for all ω ∈ Bn
δ and all atoms An we have

µ(f −1(B(ω, r)) ∩ An)
µ(f −1(B(ω, r))) ≥ (1 − δ)µω(An).

The following result is a generalization of [W19, Theorem 6.1].

Theorem 7.8. We adopt the conditions in Theorem 7.7. In addition we let ǫ > 0 be arbitrarily chosen in (0, 1)
and α be an arbitrary irrational number in (0, 1). For each δ ∈ (0, 1), there is a constant cδ > 0 and X ′
δ with
full µ measure such that the following statement holds:
For all n ≥ 1, all x ∈ X ′
δ and all K ⊂ N with lower natural density at least ρ > 2δ + ǫ, there
is a collection Mn = Mn(x, K) of at most cδ2nδ atoms of ∨n
i=0S−iA with the following properties.
Denote the union of elements in Mn as Mn. We construct the following sequence

K ′(x) = {k ∈ N : Sk(x) ∈ Mn}.

Then the following set has Lebesgue measure at least ǫ

AK∩K ′(x)(α) = {Rk
α(0) : k ∈ K ∩ K ′(x)}.

Proof. We use Theorem 7.7 to ﬁnd a set Xδ with µ(Xδ) > 1 − δ. Then for each integer n ≥ 1 we can
ﬁnd Bn
δ with ν(Bn
δ ) ≥ 1 − δ and r = r(δ, n) > 0. Without loss of generality we shall assume that
r = d−k where d is the number of digits of the Bernoulli system and k is an integer. For each ω ∈ Bn
δ
we have µ(f −1(B(ω, r)) ∩ An)
µ(f −1(B(ω, r))) ≥ (1 − δ)µω(An).

Now because of the topology we chose for Ω, we see that B(ω, r) consists of all sequences in Ω with
the same ﬁrst k digits as ω. In particular if ω′ ∈ B(ω, r) then B(ω′, r) = B(ω, r). This property reﬂects
the fact that Ω is an ultrametric space. Notice that for any Bernoulli system (Ω, SB, ν), any ball of
positive radius has positive ν measure. In particular µ(f −1(B(ω, r))) > 0 and by properties (2) and
(3) in Theorem 7.7, for each ω′ ∈ Bn
δ ∩ B(ω, r) we have

µ(f −1(B(ω, r)) ∩ An)
µ(f −1(B(ω, r))) = µ(f −1(B(ω′, r)) ∩ An)
µ(f −1(B(ω′, r))) ≥ (1 − δ)µω′(An) ≥ (1 − δ)Cδ2
−nδ

whenever An = An(x) for some x ∈ Xδ ∩ f −1(ω′). Now it is possible to see that for all x in the set
Xδ ∩ f −1(B(ω, r) ∩ Bn
δ ) we have

µ(f −1(B(ω, r)) ∩ An(x))
µ(f −1(B(ω, r))) ≥ (1 − δ)Cδ2
−nδ.

On the other hand we clearly have ∑

atoms An
 µ(f −1(B(ω, r)) ∩ An)
µ(f −1(B(ω, r))) = 1.

Since µ is not supported on boundaries of any atom we see that Xδ ∩ f −1(B(ω, r) ∩ Bn
δ ) can intersect
at most 2nδ

(1 − δ)Cδ

20 HAN YU

many atoms of ∨n
i=0S−iA since different atoms can intersect only on boundaries. Now let Y (ω) =
Xδ ∩ f −1(B(ω, r) ∩ Bn
δ ). Since there are only ﬁnitely many r balls in Ω we see that as ω varies
in Bn
δ there are ﬁnitely many different sets of form Y (ω). Denote the collection of these sets as
{Y1, . . . , YN (n)} where N (n) is an integer. For each i ∈ I = {1, . . . , N (n)}, let Ω(i) ⊂ Bn
δ be the
set of form B(ω, r) ∩ Bn
δ such that Yi = Xδ ∩ f −1(Ω(i)). We notice here that the union of all Yi is a
rather large subset of X, more precisely we have the following result,

µ
 (⋃

i∈I Yi
)
 = µ (
Xδ ∩ f −1(Bn
δ )
) ≥ 1 − 2δ.

For each i ∈ I we write the collection of atoms intersecting Yi as Mn(i) and write their union as
Mn(i). Then we saw that
 #Mn(i) ≤ 2nδ

(1 − δ)Cδ .

Now we consider the following sequence for x ∈ X,

K(x) = {k ∈ N : Sk(x) ∈ Xδ}

by the ergodic theorem we see that for µ almost all x ∈ X, K(x) has natural density at least 1 − δ. For
each i ∈ I and x ∈ X we construct the following set

K ′
i(x) = {k ∈ N : Sk(x) ∈ Mn(i)}

and we see that
 K(x) ∩ K ′
i(x) = {k ∈ N : Sk(x) ∈ Mn(i) ∩ Xδ}

⊃ {k ∈ N : Sk(x) ∈ Yi}

= {k ∈ N : Sk(x) ∈ f −1(Ω(i)) ∩ Xδ}
= K(x) ∩ K(f (x), Ω(i)).

By Lemma 7.3 and Theorem 7.4 we see that for µ almost all x ∈ X and any sequence K with lower
natural density at least 2δ + ǫ there exists an i ∈ I such that

AK∩K(x)∩K(f (x),Ω(i))
has Lebesgue measure at least ǫ. This is because K ∩ K(x) has lower natural density at least δ + ǫ
for µ almost all x ∈ X and ∑i∈I ν(Ω(i)) = µ(Bn
δ ) ≥ 1 − δ. This theorem follows since the above
argument holds for all n ≥ 1 and we can ﬁnd a full measure set X ′
δ ⊂ X which satisﬁes all our
requirements. □

8. LARGE SETS, BERNOULLI FACTORS

We now deal with the case when dimH A2 + dimH A3 ∈ (1/2, 1).

Proof of Theorem 1.6. For the moment let A ⊂ R2 be an arbitrary compact set. We deﬁne the following
function gA : R2 × [0, 1] → {0, 1}. For (a, t) ∈ R2 × [0, 1], we assign the value

gA(a, t) = 1 if and only if ([a + 0.5vt, a + vt] ∪ [a − 0.5vt, a − vt]) ∩ A ̸= ∅,

where we use [x, y] with x, y ∈ R2 for the line segment from x to y and vt is the vector with slope 3t

whose Y -projection has length 1. To see that gA is measurable it is enough to see that {g(a, t) = 0} is

AN IMPROVEMENT ON FURSTENBERG’S INTERSECTION PROBLEM 21

Borel measurable. Let (a, t) ∈ R2 × [0, 1] be such that ([a + 0.5vt, a + vt] ∪ [a − 0.5vt, a − vt]) ∩ A = ∅.
Since A is compact, for each η ∈ [0, 5, 1] ∪ [−1, −0.5] we see that a + ηvt /∈ A and therefore there
exists positive number r(η) > 0 such that B(a + ηvt, r(η)) ∩ A = ∅. We know that the segment
([a + 0.5vt, a + vt] ∪ [a − 0.5vt, a − vt]) is compact, therefore there exist positive number r > 0 such
that ([a + 0.5vt, a + vt] ∪ [a − 0.5vt, a − vt])r ∩ A = ∅, where ([a + 0.5vt, a + vt] ∪ [a − 0.5vt, a − vt])r is
the r-neighbourhood of [a + 0.5vt, a + vt] ∪ [a − 0.5vt, a − vt]. Then it is easy to see that there exist two
positive numbers r(a), r(t) such that for each (a′, t′) ∈ R2 × [0, 1] with |a′ − a| < r(a) and |t′ − t| < r(t)
we have ([a + 0.5vt′ , a + vt′] ∪ [a − 0.5vt′ , a − vt′]) ∩ A = ∅.

This shows that {gA(a, t) = 0} is in fact an open set and therefore gA is measurable.
Now let A = (A3 × A2) ∪ (A3 × A2 + (0, ±1)) ∪ (A3 × A2 + (±1, 0)) ∪ (A3 × A2 + (±1, ±1)) (there
are in total 9 translated copies of A3 × A2) and α = log 2/ log 3. In what follows we omit the subscript
A in gA.
Suppose the uniform sparseness condition does not hold. We shall restrict to the special case when
u ∈ [1, 3) and the general case follows similarly. We see that there is a positive number ρ, a sequence
{lk}k≥1 of lines with slope {uk}k≥1 ⊂ [1, 3), a sequence {ak}k≥1 ⊂ A3×A2 of points with ak ∈ lk, k ≥ 1
and sequences of integers Nk, nk with Nk → ∞ such that

1
Nk #W (lk, ak) ∩ [nk + 1, nk + Nk] ≥ ρ > 0.

For convenience, we have written W (lk, ak) for W (lk ∩ A, ak). Since we are always considering the
intersection, it is possible to drop the ∩A without causing confusions. Denote tk = log uk/ log 3 ∈
[0, 1). Now we deﬁne a dynamical system (U, S, µ) according to this initial choice of ak, lk. First we
set U = [0, 1]2 × [0, 1]. Let a = (x, y) ∈ A3 × A2 and θ ∈ [0, 1)

S(a, θ) = (T ((x, y), θ), Rα(θ)),

T ((x, y), θ) =
 {
(x, 2y mod 1), if θ + α ≤ 1

(3x mod 1, 2y mod 1), if θ + α > 1.

We notice that for any a ∈ A and any t ∈ [0, 1] the orbit of (a, t) always lies in (A3 ×A2)×[0, 1]. Having
deﬁned the dynamics we now construct a measure. Denote xk = (ak, tk). For each k we construct the
following measure in P(U ).
 µk = 1
Nk
 nk+Nk∑

i=nk+1 δSi(xk).

Then by taking a sub-sequence if necessary we assume that

µk → µ

weakly in P(U ). This measure µ is not necessarily S-invariant because it might give positive measure
on the discontinuities of S. If we identify [0, 1]2 with R2/Z2 = T2 then S is discontinuous precisely
at points (a′, t′) with t′ = 1 − α. This is where we are about to choose a different multiplication map
for the [0, 1]2 component. However it is easy to see that the projection of µ onto the [0, 1] component
is precisely the Lebesgue measure because α /∈ Q and Rα is uniquely ergodic. Thus S is µ-a.e.

22 HAN YU

continuous and therefore µ is S-invariant (see Theorem 3.3, statement 3). Now we take a µ-typical
x ∈ U . Suppose that x = (a′, t′), we want to estimate the following average,

lim
N →∞ 1
N
 N −1∑

i=0 g(Si(a′, t′)).

Thus for µ.a.e (a′, t′) we denote µa′,t′ to be the ergodic component of (a′, t′) and we see that,

lim
N →∞ 1
N
 N −1∑

i=0 g(Si(a′, t′)) = ∫ g(a, t)µa′ ,t′(a, t).

Suppose σ(a′, t′) is the ergodic disintegration measure of µ against the S-invariant σ-algebra we see
that ∫ ∫ g(a, t)µa′,t′(a, t)σ(a
′, t′) = ∫ g(a, t)µ(a, t)

≥ lim sup
k→∞
 1
Nk
 nk+Nk∑

i=nk+1 g(Si(xk))

≥ lim sup
k→∞
 1
Nk #W (lk, ak) ∩ [nk + 1, nk + Nk] ≥ ρ > 0.

In the second step, we have used the fact that {g(a, t) = 1} is a closed set and we also used the
Portmanteau theorem ( Theorem 3.3, statement 2). For the third step we used the fact that A3 is ×3
mod 1 invariant and A2 is ×2 mod 1 invariant. We would get equality in the third step if the sets
A2, A3 would be strictly invariant under the maps ×2, ×3 respectively. Intuitively we transferred the
upper Banach density in our initial data to the upper natural density almost surely along the orbit
average. For this reason, for each (a, t) ∈ U we denote W ′(a, t) to be the following sequence,

W ′(a, t) = {k ∈ N : g(Sk(a, t)) = 1}.

We see that there is an ergodic component µa′,t′ such that
∫ g(a, t)µa′,t′(a, t) ≥ ρ.

Consider now the dynamical system (U, S, µa′,t′), it is ergodic by construction with the property that
for µa′,t′ almost all (a′′, t′′) ∈ U
 lim
N →∞ 1
N
 N −1∑

i=0 g(Si(a
′′, t′′)) ≥ ρ.

In order to apply Theorem 7.8 we need to address some issues. We divide the rest of proof into three
subsections.
 AN IMPROVEMENT ON FURSTENBERG’S INTERSECTION PROBLEM 23

8.1. Partitions and boundaries. First we take an initial partition A of [0, 1]2 × [0, 1] by taking

Ai,j × Ck,

where we deﬁne for (i, j) ∈ {0, 1, 2} × {0, 1} the following partition B of [0, 1]2

Ai,j = [ i
3 , i + 1
3
 ] × [ j
2 , j + 1
2
 ] ,

and a partition C of [0, 1] as C1 = [1−α, 1], C2 = [0, 1−α). We see that ∨∞
i=0S−iA generates the Borel σ-
algebra of [0, 1]2 × S1 and therefore h(S, µa′,t′) = h(S, µa′,t′, A). Our ﬁrst issue is that µa′,t′ could give
positive measure on boundaries of {S−iA}i≥0. We see that the [0, 1] component of µa′,t′ is +α mod 1
invariant and thus it is the Lebesgue measure. If µa′,t′ does give positive measure on boundaries of
{S−iA}i≥0 then its [0, 1]2 component gives positive measure on boundaries of the [0, 1]2 component
of {S−iA}i≥0, which are rectangles with edges that project to either dyadic rational numbers on Y -
axis or triadic rational numbers on X-axis. In this case the Y -component of µa′,t′ is then supported on
ﬁnitely many rational numbers since it is ×2 mod 1 invariant and we can focus on the X-component.
For the other case, the projection on X-axis does not deﬁne a dynamical system. In this case it can
be seen that the [0, 1]2 component of µa′,t′ supports on ﬁnitely many horizontal lines with rational X-
coordinates. Suppose the former case and the later case can be treated in a similar way. We consider
the following dynamical system (A3 × [0, 1], SX , µX
a′,t′).
Here SX is deﬁned as follows, SX(x, θ) = (TX (x, θ), Rα(θ)),

TX (x, θ) = {x, if θ + α ≤ 1

3x mod 1, if θ + α > 1,

and µX
a′,t′ is the corresponding projected measure. If µX
a′,t′ still supports on boundaries we see that the
[0, 1]2 component of µa′,t′ supports on ﬁnitely many rational points and this case the result is obvious.
Therefore we can assume that at least one of the X or Y coordinate projections of µa′,t′ does not
support on boundaries and we then perform the following entropy arguments for either (U, S, µa′,t′)
or one of its projections. We only illustrate the argument for (U, S, µa′,t′) and the arguments for its
projections are similar.

8.2. Zero entropy. We now consider the case when h(S, µa′,t′) = 0. In this case for each integer n ≥ 1,
the atoms of ∨n
i=0S−iA are of form B × C where B ⊂ [0, 1]2 is a rectangle with dimension 3−n′ × 2n

where n′ satisﬁes 2−n ≤ 3−n′ ≤ 3 × 2−n (so the rectangle is almost a square) and C is one of the atoms
of ∨n
i=0R−i
α C. The number of atoms in ∨n
i=0R−i
α C is at most 2n and for each C the number of different
atoms B × C is between 22n/3 and 3 × 22n. Now if the entropy 1
n H(µa′,t′, ∨n
i=0S−iA) is smaller than a
given small number ǫ for all large enough n then there exist δ(ǫ) = O(ǫ) such that O(2δn) many atoms
in ∨n
i=0S−iA support at least 1 − δ portion of µa′,t′ measure.
To see this, let V be a ﬁnite set of points of cardinality greater than 2n and for each v ∈ V we give
a probability pv ∈ (0, 1) such that ∑v∈V pv = 1. If the entropy, namely − ∑v∈V pv log pv < nǫ′ for a
number ǫ′ > 0, then for another number δ′ > 0 we deﬁne the following subset

Vδ′ = {v ∈ V : pv ≥ 2
−nδ′}.

24 HAN YU

Then it is easy to see that
∑

v∈V pv(− log pv) = ∑

v∈Vδ′ pv(− log pv) + ∑

v /∈Vδ′ pv(− log pv) < nǫ′.

If v /∈ Vδ′ then − log pv > nδ′ log 2 and therefore

nǫ′ > ∑

v /∈Vδ′ pv(− log pv) > ∑

v /∈Vδ′ nδ′pv log 2.

Then we see that ∑

v∈Vδ′ pv = 1 − ∑

v /∈Vδ′ pv > 1 − 1
log 2 ǫ′

δ′ .

On the other hand because ∑v∈V pv = 1 we see that

#Vδ′ ≤ 2
nδ′ .

Then we choose δ′ = √ǫ′ and we see that at least 1 − δ′/ log 2 portion of the measure pv, v ∈ V is
supported in a collection of less than 2nδ′ many points in V .
Now we apply the above result to our dynamical system (U, S, µa′,t′) and denote the collection of
those O(2δn) atoms in ∨n
i=0S−iA as Mn and their union as Mn. We can choose an ǫ > 0 such that
δ = δ(ǫ) < ρ. Now because µa′,t′ is an ergodic component of a′, t′ we see that by the ergodic theorem,
for µa′,t′.a.e (a′′, t′′) ∈ U,
 {k ∈ N : Sk(a′′, t′′) ∈ Mn}

has natural density at least 1 − δ. Since 1 − δ + ρ > 1 we see that

K = {k ∈ N : Sk(a′′, t′′) ∈ Mn} ∩ W ′(a
′′, t′′)

has natural density at least ρ − δ. For each k ∈ K we see that Sk(a′′, t′′) ∈ Mn and g(Sk(a′′, t′′)) = 1.
Denote a′′
k, t′′
k to be the [0, 1]2 and [0, 1] components of Sk(a′′, t′′) respectively. Then we can ﬁnd a point
b′′
k ∈ A such that |πY (a′′
k − b′′
k)| ∈ [0.5, 1] and the line segment [a′′
k, b′′
k] has slope 3t′′
k . This implies that
|a′′
k − b′′
k| ∈ [0.5, √2] ⊂ [1/6, 1.5].
As Mn is a collection of at most O(2δn) many atoms in ∨n
i=0S−iA, the [0, 1]2 component of Mn
consist at most O(2δn) many almost squares, notices that they are not necessary disjoint. We denote
the [0, 1]2 component of Mn as Qn and we see that for each k ∈ K, there exist a Q ∈ Qn such that
a′′
k ∈ Q. It is also easy to see that t′′
k = Rk
α(t′′). Let t∗ be a limit point of {t′′
k}k∈K. Since Qn is a ﬁnite
collection of closed sets we see that ⋃Q∈Qn Q s a closed set. Assume that limj→∞ t′′
kj = t∗ for a
subsequence {kj }j∈N of K. Then {a′′
kj }j∈N has a limit point a∗ in ⋃Q∈Qn Q. Since A3, A2 are compact
we see that this limit point is contained in A3 × A2 as well. Moreover since A is also compact we see
that we can assume the sequence {bkj }j∈N converges to a limit point b∗ in A and |b∗ − a∗| ∈ [1/6, 1.5]
and the line segment [a∗, b∗] has slope 3t∗ . We have seen that AK = {Rk
α(t′′) : k ∈ K} has Lebesgue
measure at least ρ − δ, see Lemma 5.1. Recall the smooth map e : [0, 1] → S1 constructed in the
proof of Theorem 1.5. Then it is easy to see that there exists constant c > 0 such that we can ﬁnd
a set E of directions with Lebesgue measure at least c(ρ − δ) such that for each e′ ∈ E there is a

AN IMPROVEMENT ON FURSTENBERG’S INTERSECTION PROBLEM 25

point xe′ ∈ A3 × A2 and Q ∈ Qn such that xe′ ∈ Q. Moreover there exists ye′ ∈ A with distance
|xe′ − ye′| ∈ [1/6, 1.5] and ye′ − xe′
|ye′ − xe′| = e
′.

We notice that A and A3 × A2 have the same Hausdorff dimension. For all large enough integers n,
we can ﬁnd at least 0.5c(ρ − δ)2n many 2−n-separated directions in E and we denote this collection
of direction as En. By the pigeonhole principle we see that there exists Q ∈ Qn such that it contains
O(2−δn(0.5c(ρ − δ)2n)) many points of form {xe′}e′∈En. Then the corresponding points ye′ are all at
least 0.5/2n-separated. As this holds for all large enough n we see that this implies that dimBA ≥ 1−δ
but we constructed δ = O(ǫ) therefore by letting ǫ be small enough we obtain a contradiction because
we assumed that dimH A3 × A2 = dimBA3 × A2 < 1.

8.3. Positive entropy. Now ﬁnally we can assume that (U, S, µa′,t′) has positive entropy, that is,
h(S, µa′,t′) > 0. We saw that for µa′,t′ almost all x = (a′′, t′′) ∈ U , W ′(a′′, t′′) has lower natural density
at least ρ. Now we want to apply Theorem 7.8. Let δ > 0 be such that ρ > 2δ. Then exists a constant
cδ > 0 and for each n ≥ 1 there exist a set Uδ ⊂ U with full µa′,t′ measure such that for each x ∈ Uδ,
there is a collection Mn of at most cδ2δn atoms in ∨n
i=0S−iA with union Mn such that

AW ′(a′′,t′′)∩{k∈N:Sk(x)∈Mn}
has Lebesgue measure at least ρ − 2δ. Then the rest of the argument is the same as that of the zero
entropy case. □

9. FURTHER REMARKS AND PROBLEMS

9.1. Casinos with multidimensional clocks. In this paper we only considered problems related to
intersections between two invariant sets. One reason is that in Theorem 7.8 we coupled a Bernoulli
system with an irrational rotation on the unit circle. There is no problem if we replace the irrational
rotation with an irrational torus rotation. Let Tk be the unit torus. We view it as [0, 1]k. Suppose that
α1, . . . , αk are irrational numbers which are linearly independent over the ﬁeld of rational numbers.
Then the action (x1, . . . , xk) → (x1 + α1 mod 1, . . . , xk + αk mod 1)
is an irrational torus rotation. Like its one dimensional brother, irrational torus rotations are uniquely
ergodic with the Lebesgue measure. One can also study discrepancy estimates, see [DT97]. All
results in Section 7 can be generalized in this way. Let p1, . . . , pk be k ≥ 2 integers such that
1, log p1/ log p2, . . . , log p1/ log pk are linearly independent over the ﬁeld of rational numbers. We can
consider l ∩ Ap1 × · · · × Apk with a line l in Rk which is not parallel with the coordinate axis. We also
assume that l is not contained in any subspaces generated by coordinate axis, otherwise we can drop
some of Ap1, . . . , Apk . To see how to obtain a torus rotation, let (x1, . . . , xk, θ2, . . . , θk) ∈ [0, 1]2k−1,
we deﬁne the following map (which can be viewed as a higher dimensional version of the map T
deﬁned in the proof of Theorem 1.6)

T (x1, . . . , xk, θ2, . . . , θk) = (y1, . . . , yk, {θ2 + log p2/ log p1}, . . . , {θk + log pk/ log p1})

where y1, . . . , yk are determined as follows
 y1 = {p1x1}

26 HAN YU

and for each i ∈ {2, . . . , k},
 yi =
 {xi if θi − log p1 > 0
{pixi} else.

Now we allow the direction vector of l range inside Sk−1 whose coordinate components are contained
in (δ, 1 − δ) where δ > 0 can be arbitrarily chosen. Then if l ∩ Ap1 × · · · × Apk is large (in terms of
sparseness which can be deﬁned similarly for lines in Rk), by using the torus rotation with vector
(log p1/ log p2, . . . , log p1/ log pk) we see that Ap1 × · · · × Apk would have dimension at least k − 1, the
dimension of Sk−1. Therefore we can upgrade Theorem 1.6 for intersections among more than two
sets. As the main technical steps are the same for all k ≥ 2, we only illustrated the proof for k = 2 in
which case we have a better visualization. To be precise, we state the following higher dimensional
version of Corollary 1.7.

Corollary 9.1. Let k ≥ 2 be an integer. Let Ap1, . . . , Apk be k closed invariant subsets of [0, 1] with respect
to ×p1 mod 1, ×p2 mod 1 . . . respectively. Assume that log p1/ log pi for i ∈ {2, . . . , k} are irrational
numbers which are linearly independent over the ﬁeld of rational numbers. Suppose that ∑k
i=1 dimH Api <
k − 1 then for each 2k-tuple u1, . . . , uk, v1, . . . , vk of non-zero real numbers we have

dimB ∩k
i=1 (uiApi + vi) = 0.

Moreover, let δ > 0 be an arbitrarily chosen positive number and suppose that δ < |ui| < δ−1 for each
i ∈ {1, . . . , k}. Then for each ǫ > 0, there is an integer Nǫ > 0 such that

N (∩k
i=1(uiApi + vi), 2
−N ) ≤ N ǫ

for all N ≥ Nǫ. The choice of Nǫ does not depend on ui, vi.

There is one important point to note. For k ≥ 3, it is surprisingly not an easy task to produce even
one example of integers p1, . . . , pk to satisfy the condition that

1, log p1
log p2 , . . . , log p1
log pk (*)

are Q-linearly independent. Problems of this kind are related to the study of algebraic relations
among logarithms of algebraic numbers. We now show that a conjecture of Schanuel (see below)
implies the above Q-linear independence as long as p1, . . . , pk are multiplicatively independent, i.e.,

1, log p2
log p1 , . . . , log pk
log p1
are Q-linearly independent, for example, p1 = 2, p2 = 3, p3 = 5.
Let Pk(x1, . . . , xk) be the symmetric polynomial of degree (1, . . . , 1) (there are k − 1 many ones).
For example, we have P3(x1, x2, x3) = x1x2 + x1x3 + x2x3.

For the above Q-linear independence of (*) we would need that (log p1, . . . , log pk) does not solve the
polynomial equation Pk(n1x1, . . . , nkxk) = 0.

unless n1, . . . , nk = 0. We recall a conjecture of Schanuel,see [A71].

AN IMPROVEMENT ON FURSTENBERG’S INTERSECTION PROBLEM 27

Conjecture 9.2 (Schanuel’s conjecture). Let z1, . . . , zk be k ≥ 1 many Q-linearly independent complex
numbers. Then the transcendence degree of (z1, . . . , zk, ez1, . . . , ezk ) is at least k.

We replace zi = log pi in the above conjecture. As a result the conjecture says that

(log p1, . . . , log pk, p1, . . . , pk)

has transcendence degree at least k. As p1, . . . , pk are already integers, this implies that (log p1, . . . , log pk)
transcendence degree k, i.e. log p1, . . . , log pk are algebraically independent. Thus

Pk(n1 log p1, . . . , nk log pk) = 0

implies that n1, . . . , nk = 0.
 10. ACKNOWLEDGEMENT

HY was ﬁnancially supported by the University of St Andrews. HY was also ﬁnancially supported
by the University of Cambridge and the Corpus Christi College, Cambridge. HY has received fund-
ing from the European Research Council (ERC) under the European Union’s Horizon 2020 research
and innovation programme (grant agreement No. 803711). HY thanks the anonymous referees for
help comments.
 REFERENCES

[Al20] A. Algom, Slicing theorems and rigidity phenomena for self afﬁne carpets, Proc. London Math. Soc., 121, (2020),
312-353.
[Au20] T. Austin, A new dynamical proof of the Shmerkin–Wu theorem, arxiv:2009.01292, (2020).
[A71] J. Ax, On Schanuel’s Conjectures, Annals of Mathematics(2), 93(2), (1971).
[B15] Y. Bugeaud, Effective irrationality measures for quotients of logarithms of rational numbers, Hardy-Ramanujan
Journal, 38, (2015), 45-48.
[BY18] S. Burrell, H. Yu, Digit expansions of numbers in different bases, arxiv:1905.00832 , (2019)
[DT97] M. Drmota and R. Tichy, Sequences, Discrepancies and Applications, Lecture Notes in Mathematics, Springer-
Verlag Berlin Heidelberg,(1997).
[EW11] M. Einsiedler and T. Ward. Ergodic theory: with a view towards number theory, Graduate Texts in Mathematics,
Springer-Verlag London, (2011).
[F05] K. Falconer, Fractal geometry: Mathematical foundations and applications, second edition, John Wiley and Sons,
Ltd, (2005).
[F14] J. Fraser, Assouad type dimensions and homogeneity of fractals, Transactions of the American Mathematical Soci-
ety, 366,(2014), 6687–6733.
[F67] H. Furstenberg, Disjointness in Ergodic Theory, Minimal Sets, and a Problem in Diophantine Approximation, Math-
ematical systems theory, 1(1),(1967), 1-49.
[F70] H. Furstenberg, Intersections of Cantor sets and transversality of semigroups, Problems in Analysis, Princeton
University Press,(1970), 41-59.
[F08] H. Furstenberg, Ergodic fractal measures and dimension conservation, Ergodic Theory Dynamical Systems,
28,(2008), 405–422.
[HS12] M. Hochman and P. Shmerkin, Local entropy averages and projections of fractal measures, Annals of Mathematics,
175,(2012), 1001-1059.
[K06] A. Klenke, Probability Theory: A Comprehensive Course,Springer-Verlag London, (2006).
[KRS12] A. Käenmäki, T. Rajala, and V. Suomala, Existence of doubling measures via generalised nested cubes, Proceedings
of the American Mathematical Society 140(9),(2012), 3275-281.
[L98] J. Luukkainen, Assouad dimension:antifractal metrization, porous sets, and homogeneous measures, Journal of the
Korean Mathematical Society, 35,(1998), 23-76.

28 HAN YU

[MT10] J. Mackay and J. Tyson. Conformal dimension. Theory and application, University Lecture Series, 54, American
Mathematical Society, Providence, RI, (2010).
[M99] P. Mattila, Geometry of sets and measures in Euclidean spaces: Fractals and rectiﬁability, Cambridge Studies in
Advanced Mathematics, Cambridge University Press, (1999).
[PY98] M. Pollicott and M. Yuri, Dynamical systems and ergodic theory, London Mathematical Society Student Texts,
Cambridge University Press, (1998).
[R85] G. Rhin, Approximants de Padé et mesures effectives d’irrationalité, Séminaire de Théorie des Nombres, Paris
(1985–86), 155-164.
[S16] P. Shmerkin, On Furstenberg’s intersection conjecture, self-similar measures, and the L
q norms of convolutions,
preprint, arxiv:1609.07802, (2016).
[S12] D. Simmons, Conditional measures and conditional expectation; Rohlin’s disintegration theorem, Discrete and con-
tinuous dynamical systems, 32(7), (2012), 2565-2582.
[SS05] E. Stein and R. Shakarchi, Real analysis: Measure theory, integration and Hilbert spaces,Princeton University
Press, (2005).
[Su14] R-F. Sun, URL: http://www.math.nus.edu.sg/~matsr/ProbI/Lecture5.pdf, (2014).
[VK] A. Vol’berg and S. Konyagin, On measures with the doubling condition, Izv.Akad.Nauk SSSR Ser. Mat.,
51(3),(1987),666-675.
[W19] M. Wu, A proof of Furstenberg’s conjecture on the intersections of ×p and ×q-invariant sets, Annals of Mathematics,
189(3), (2019), 707–751.
[Y20] H. Yu, Additive properties of numbers with restricted digits, arxiv: 2004.05926, (2020).
[Yu19] H. Yu, Bernoulli decomposition and arithmetical independence between sequences, Ergodic Theory and Dynamical
Systems, 1-11. doi:10.1017/etds.2019.117.

HAN YU, DEPARTMENT OF PURE MATHEMATICS AND MATHEMATICAL STATISTICS, UNIVERSITY OF CAMBRIDGE, CB3
0WB, UK
Email address: hy351@maths.cam.ac.uk
