<!-- source: https://arxiv.org/pdf/1206.4001 | converted from PDF -->

Ramsey Theory, Integer Partitions and a New Proof of the

Erd˝os-Szekeres Theorem

Guy Moshkovitz
∗ Asaf Shapira†

Abstract

Let H be a k-uniform hypergraph whose vertices are the integers 1, . . . , N . We say that H
contains a monotone path of length n if there are x1 < x2 < · · · < xn+k−1 so that H contains
all n edges of the form {xi, xi+1, . . . , xi+k−1}. Let Nk(q, n) be the smallest integer N so that
every q-coloring of the edges of the complete k-uniform hypergraph on N vertices contains a
monochromatic monotone path of length n. While the study of Nk(q, n) for speciﬁc values of k
and q goes back (implicitly) to the seminal 1935 paper of Erd˝os and Szekeres, the problem of
bounding Nk(q, n) for arbitrary k and q was studied by Fox, Pach, Sudakov and Suk.
Our main contribution here is a novel approach for bounding the Ramsey-type numbers
Nk(q, n), based on establishing a surprisingly tight connection between them and the enumer-
ative problem of counting high-dimensional integer partitions. Some of the concrete results we
obtain using this approach are the following:

• We show that for every ﬁxed q we have N3(q, n) = 2
Θ(nq−1), thus resolving an open problem
raised by Fox et al.

• We show that for every k ≥ 3, Nk(2, n) = 2·
·2(2−o(1))n where the height of the tower is
k − 2, thus resolving an open problem raised by Eli´aˇs and Matouˇsek.

• We give a new pigeonhole proof of the Erd˝os-Szekeres Theorem on cups-vs-caps, similar to
Seidenberg’s proof of the Erd˝os-Szekeres Lemma on increasing/decreasing subsequences.

1 Introduction

1.1 Some historical background

It would not be an exaggeration to state that modern Extremal Combinatorics, and Ramsey Theory
in particular, stemmed from the seminal 1935 paper of Erd˝os and Szekeres [9]. Besides establishing

2010 Mathematics Subject Classiﬁcation: 05D10, 05A17, 05C65
∗School of Mathematics, Tel-Aviv University, Tel-Aviv, Israel 69978. Email: guymosko@tau.ac.il. Supported in
part by ISF grant 224/11.
†School of Mathematics, Tel-Aviv University, Tel-Aviv, Israel 69978, and Schools of Mathematics and Computer
Science, Georgia Institute of Technology, Atlanta, GA 30332. Email: asafico@tau.ac.il. Supported in part by NSF
Grant DMS-0901355, ISF Grant 224/11 and a Marie-Curie CIG Grant 303320.

1arXiv:1206.4001v1  [math.CO]  18 Jun 2012
explicit bounds for graph and hypergraph Ramsey numbers, they also proved two of the most well-
known results in Combinatorics, which have become known as the Erd˝os-Szekeres Lemma (ESL)
and the Erd˝os-Szekeres Theorem (EST). Let f (a, b) be the smallest integer so that every sequence
of f (a, b) distinct real numbers contains either an increasing sequence of length a or a decreasing
sequence of length b. Then ESL states that

f (n, n) ≤ (n − 1)
2 + 1 .

Let g(a, b) be the smallest integer so that every set of g(a, b) points in the plane in general position,
all with distinct x-coordinates, contains either a points p1, . . . , pa with increasing x-coordinate so
that the slopes of the segments (p1, p2), (p2, p3) . . . , (pa−1, pa) are increasing, or b such points so
that the slopes of these segments are decreasing. Then EST states that

g(n, n) ≤ (
2n − 4
n − 2
 ) + 1 . (1)

We note that EST implies that for any integer n there is an integer N (n) so that every set of
N (n) points in general position in the plane contains n points in convex position. Speciﬁcally, it
shows that N (n) ≤ (2n−4
n−2 ) + 1. The fact that N (n) is ﬁnite was later labelled the “Happy Ending
Theorem”.
The original proof in [9] of ESL was based on establishing the recurrence relation f (n+1, n+1) ≤
f (n, n) + 2n − 1. By now, there are several proofs of ESL. In fact, Steele [27] has collected 7 of
these proofs, and dubbed the following pigeonhole-type proof by Seidenberg [23] as “the slickest
and most systematic”. Assign to each real number x in the sequence two labels x+, x− where we
take x+ to be the length of the longest increasing sequence ending at x, and x− to be the length
of the longest decreasing sequence ending at x. Now, it is easy to see that for every pair of reals
x, y in the sequence we have (x+, x−) ̸= (y+, y−). Hence, if there is neither an increasing nor a
decreasing sequence of length n then there can be no more than (n − 1)2 numbers in the sequence.
The same idea shows that f (a, b) ≤ (a − 1)(b − 1) + 1, and it is easy to see that this bound is tight.
The original proof in [9] of EST was based on establishing the recurrence relation g(a+1, b+1) ≤
g(a, b + 1) + g(a + 1, b) − 1. To the best of our knowledge, this is the only known proof of this
classic result.1 As part of our investigation here we will establish a new pigeonhole-type proof of
EST, similar in spirit to Seidenberg’s proof [23] of ESL we sketched in the previous paragraph. We
have to admit that we did not set out to try and ﬁnd a new proof of EST. Our goal was actually to
bound Ramsey numbers of certain generalizations of EST, and the new proof is just a byproduct.

1.2 High-dimensional integer partitions

The notion of integer partitions is without doubt the most well-studied notion in discrete mathe-
matics, and goes back (at least) to Euler. We will be very brief here and just deﬁne the notions

1We stress that here we are referring to bounding g(a, b). The bound on N (n) has been slightly improved (see [20]
for a survey). Interestingly, all improvements rely on clever applications of g(a, b).

2

1 2 3 4 5 6 7

1

2

3

4

5

6

7
 (a) A line partition and the
lattice path along its bound-
ary.
 (b) A plane partition. Note that the
stacks are “ﬂushed into the corner”.

Figure 1: Partitions

that are relevant to the results of this paper (see [2] for more background on this subject). A
decreasing sequence of nonnegative integers a1 ≥ a2 ≥ . . . will be called a line partition. One
can visualize a line partition as a 2-dimensional sequence of stacks of height ai each (essentially,
a Young diagram, see Figure 1a). A matrix A of nonnegative integers so that Ai,j ≥ Ai+1,j and
Ai,j ≥ Ai,j+1 for all possible i, j will be called a plane partition. One can visualize a plane partition
in 3-dimensions as a plane consisting of stacks, where at location (i, j) we have a stack of height
Ai,j (see Figure 1b). The notion of a plane partition was introduced by MacMahon in 1897 [16] as
a 2-dimensional analogue of integer partitions2 and has been extensively studied ever since. More
generally, one deﬁnes a d-dimensional partition as a d-dimensional (hyper)matrix A of nonnegative
integers so that the matrix is decreasing in each line, that is, Ai1,...,it,...,id ≥ Ai1,...,it+1,...,id for every
possible i1, . . . , id and 1 ≤ t ≤ d.
Let Pd(n) be the number of n × · · · × n d-dimensional partitions with entries from {0, 1, . . . , n}.
Note that when d = 1 (that is, line partitions n ≥ a1 ≥ . . . ≥ an ≥ 0) we can think of such an
integer partition as a lattice path in Z2 starting at (0, n) and ending at (n, 0) where in each step
the path moves either down or to the right (see Figure 1a). It is thus clear that

P1(n) = (2n
n
 ) . (2)

Computing P2(n) appears to be much harder. Luckily, a celebrated result of MacMahon [17] states
that
 P2(n) = ∏

1≤i,j,k≤n
 i + j + k − 1
i + j + k − 2 . (3)

2Recall that if n = a1 + . . . + ak then the standard way to write this partition is as a decreasing sequence
a1 ≥ a2 ≥ . . ., that is, what we call here a line partition.
 3

We refer the reader to [25] for more background and references on the rich history and current
research on plane partitions. We also recommend Chapter 5 of [1] for an ingenious proof of (3)
using the Lindstr¨om-Gessel-Viennot Lemma.
Unfortunately, there is no known closed formula for Pd(n) even for d = 3 (see, e.g., [3]). The
same is true even for the more well-studied variant of the problem, which considers the number of
partitions with a given sum of entries; in fact, even establishing a generating function for three-
dimensional partitions, usually referred to as solid partitions, is an outstanding open problem in
enumerative combinatorics which goes back to MacMahon. See [21] and [25] for some background on
this open problem. However, observe that each line in a d-dimensional partition is a line partition.
Since a d-dimensional partition is composed of nd−1 line partitions, we can derive from (2) the
crude bound
 Pd(n) ≤ (2n
n
 )nd−1 ≤ 22nd . (4)

1.3 Erd˝os-Szekeres generalized

One cannot but suspect that there is some abstract combinatorial phenomenon behind ESL and
EST. Indeed, ESL is a special case of Dilworth’s Theorem [7] (or actually, its dual, which is due to
Mirsky [19]). As to EST, Chv´atal and Koml´os [5] obtained a combinatorial lemma generalizing it
in terms of paths in edge weighted tournaments. Very recently, Fox, Pach, Sudakov and Suk [10]
suggested the following elegant framework for studying such problems, which nicely puts both ESL
and EST under a single roof.
Let Kk
N denote the complete k-uniform hypergraph on a set of N vertices, that is, the collection
of subsets of size k of the N vertices. For our purposes here it will be useful to think of the vertices
as being ordered and thus name them 1, . . . , N . For a sequence of vertices x1 < x2 < · · · < xn+k−1
we say that the edges
 {x1, . . . , xk}, {x2, . . . , xk+1}, . . . , {xn, . . . , xn+k−1}

form a monotone path, and we refer to the number of edges as its length (so the path above is
of length n).3 Note that henceforth, whenever we will be talking about an edge {x, y, z} we will
implicitly assume that x < y < z.
Let Nk(q, n) be the smallest integer N so that every coloring of the edges of Kk
N using q
colors contains a monochromatic monotone path of length n. Recalling ESL, it is easy to see that
f (n + 1, n + 1) ≤ N2(2, n) (notice N2(q, n) measures length with respect to edges), and that the
proof of ESL we sketched earlier implies N2(q, n) ≤ nq + 1. It is also easy to see that

g(n + 2, n + 2) ≤ N3(2, n) , (5)

3We note that Fox et al. [10] measured the length of a path using the number of vertices. As it turns out, in our
proofs it will be much more natural to use the number of edges as the measure of length.

4

and that one can prove N3(2, n) ≤ (2n
n ) + 1 by applying the recursive argument (mentioned above)
that was used by Erd˝os and Szekeres [9] to prove EST (1). Hence, one can prove both ESL and
EST in the framework of studying Nk(q, n).
The question of bounding N3(q, n) for q ≥ 3 was raised by Fox et al. [10], motivated (partially)
by certain geometric generalizations of EST (see [10] for the exact details). One of their main
results was that 2
(n/q)q−1 ≤ N3(q, n) ≤ nnq−1 . (6)

The main problem they left open was whether the correct exponent log2 N3(q, n) is of order nq−1.

1.4 Our results

Our main result in this paper establishes a surprisingly close connection between the problem
of bounding the Ramsey numbers N3(q, n) deﬁned above, and the problem of enumerating high-
dimensional integer partitions we discussed in the previous subsection.

Theorem 1. For every q ≥ 2 and n ≥ 2 we have

N3(q, n) = Pq−1(n) + 1 .

Recall that by (4) we have Pq−1(n) ≤ 22nq−1. Hence, Theorem 1 resolves the problem of Fox et
al. [10] mentioned above by establishing that for every ﬁxed q we have N3(q, n) = 2Θ(nq−1). Also,
we get via MacMahon’s formula (3) an exact bound for N3(3, n), and from the long history of
unsuccessful attempts to precisely compute P3(n) we learn that it is probably hopeless to compute
N3(4, n) exactly. In fact, as we shall see later on in the paper, Theorem 1 also implies that it is
unlikely to expect a closed formula even for N3(q, 2), namely the case of the two-edge path! (see
Section 4)
Notice that Theorem 1, together with the observations we have made in (2) and (5), implies
EST (1). We note that our initial approach for resolving the problem raised in [10] was to adapt the
recursive approach of Erd˝os and Szekeres for proving EST (1) (as sketched in the previous section)
to the general setting of q ≥ 3. It appears that this approach cannot be generalized, mainly because
attempts to come up with a recursion for Pq−1(n) have failed. So in some sense, our new proof of
EST came out of the need to ﬁnd a proof that can be generalized to more than 2 colors.
To prove the upper bound in Theorem 1 we will use a pigeonhole type argument, similar to
Seidenberg’s proof [23] of ESL which we sketched above. To this end we will map every vertex of
the hypergraph to a (q − 1)-dimensional partition and argue that this mapping must be injective.
To prove the lower bound, we will show a surprising way by which one can think of (q − 1)-
dimensional partitions as vertices of a hypergraph, and then use certain relations between these
partitions/vertices in order to deﬁne an explicit q-coloring of the complete 3-uniform hypergraph
without long monochromatic monotone paths.
 5

Note that the bounds on N3(q, n) we get from Theorem 1 by combining (4) and the lower
bound in (6) are 2(n/q)q−1 ≤ N3(q, n) ≤ 22nq−1. It is thus natural to ask if one can use the precise
description of N3(q, n) of Theorem 1 in order to tighten the dependence on q in the exponent of
N3(q, n). To this end we ﬁrst prove the following.

Theorem 2. For every d ≥ 1 and n ≥ 1 we have

Pd(n) ≥ 2 2
3 nd/√d+1 .

Observe that from the above (and Theorem 1) we immediately get an exponential improvement
over the lower bound of Fox et al. [10] (stated in (6)) in terms of the dependence of N3(q, n) on q.
The following corollary thus summarizes our bounds for N3(q, n).

Corollary 1. For every q ≥ 2 and n ≥ 2 we have

2 2
3 nq−1/
√q ≤ N3(q, n) ≤ 22nq−1 .

As we discuss in the concluding remarks, it seems reasonable to conjecture that the lower bound
gives the correct exponent, and that N3(q, n) = 2Θ(nq−1/
√q).

1.5 Higher uniformity

Given the characterization of N3(q, n) in terms of enumerating integer partitions, it is natural to
ask if a similar characterization can be proved for Nk(q, n) for arbitrary k ≥ 3. As we show in
Section 3 the answer is positive, but since the objects involved in this characterization are (slightly)
complicated to deﬁne, we refrain from stating the results in this section and refer the reader to the
statement of Theorem 5 in Section 3. Let us instead describe some immediate corollaries of this
characterization.
Let tk(x) be a tower of exponents of height k −1 with x at the top. So t1(x) = x and t3(x) = 22x.
Since we know that N3(q, n) ≤ 2O(nq−1), it seems natural to suspect that Nk(q, n) ≤ tk−1(O(nq−1)).
Indeed, Fox et al. [10] show how to convert a bound of the form N3(q, n) ≤ 2cnq−1 (which we
obtain in Theorem 1) into the more general bound Nk(q, n) ≤ tk−1(c′nq−1) (where c, c′ are absolute
constants). Here, we apply the main idea behind the proof of Theorem 1 to give a very short and
direct proof of the following bound, improving the one from [10], which relates Nk(q, n) to N3(q, n).

Theorem 3. For every k ≥ 3, q ≥ 2, and n ≥ 2 we have

Nk(q, n) ≤ tk−2(N3(q, n)) .

This implies, by the upper bound in Corollary 1, that Nk(q, n) ≤ tk−1(2nq−1) for k ≥ 3, as
desired. We note that using our enumerative characterization of Nk(q, n) we can actually get a
better upper bound than the one stated above; see the discussion in Section 4.

6

While we can prove Theorem 3 directly, and without using our characterization for Nk(q, n),
it appears that to prove a matching lower bound does require this enumerative characterization.
Speciﬁcally, we have the following.

Theorem 4. There is an absolute constant n0, so that for every k ≥ 3, q ≥ 2 and n ≥ n0, we have

Nk(q, n) ≥ tk−2(N3(q, n)/3nq) .

The above result improves upon a lower bound of [10], but more importantly, matches (up to
lower order terms) the upper bound of Theorem 3. One application of the above tight bounds is
the following. Eli´aˇs and Matouˇsek [8] have recently introduced another framework for studying
generalizations of both ESL and EST in terms of the kth derivative of the function passing through
a set of points. Motivated by the relation between their framework and the one introduced in [10],
they asked if for every k ≥ 3 one has Nk(2, n) = tk−1(Θ(n)). By combining Theorems 3, Theorem 4,
and our bounds on N3(q, n) in Corollary 1, we in particular get the following sharp (and positive)
answer.

Corollary 2. For every k ≥ 3 we have

Nk(2, n) = tk−1((2 − o(1))n) ,

where the o(1) term goes to 0 as n → ∞.

In fact, we may deduce the following, summarizing our bounds for general q.

Corollary 3. For every k ≥ 3, q ≥ 2, and suﬃciently large n we have

tk−1(nq−1/2
√q) ≤ Nk(q, n) ≤ tk−1(2nq−1) .

Organization: The rest of the paper is organized as follows. In Section 2 we mainly focus on
3-uniform hypergraphs. We ﬁrst give a new proof of EST by showing that N3(2, n) ≤ P1(n) + 1.
We will then move on to prove the more general bound N3(q, n) ≤ Pq−1(n) + 1. The proof of the
general bound will turn out to be almost identical to the proof of the case q = 2. Next we will
prove the lower bound of Theorem 1, thus completing the characterization of N3(q, n). Since the
proof of Theorem 3 (giving an upper bound on our Ramsey number for k-uniform hypergraphs) is
so similar to the proof of Theorem 1, we will also give this proof in Section 2. We will end Section 2
with the proof of Theorem 2.
In Section 3 we consider k-uniform hypergraphs. We will start with proving a theorem analogous
to Theorem 1, giving a characterization of Nk(q, n) in terms of enumerating higher-order variants of
Pq−1(n). We will then show how one can derive the lower bound in Theorem 4 from this character-
ization. In Section 4 we give some concluding remarks and open problems; among other things, we
discuss how the problem of estimating the Ramsey-type numbers N3(q, k), or equivalently, estimat-
ing the number of d-dimensional integer partitions Pd(n), naturally leads to a problem of estimating
the number of independent sets in graphs, a well-studied problem in enumerative combinatorics.

7

2 New Bounds for 3-Uniform Hypergraphs

We write [n] for {1, . . . , n}. For x, y ∈ [n]d we denote x ≼ y when xi ≤ yi for all 1 ≤ i ≤ d. A set
S ⊆ [n]d is a down-set if s ∈ S implies x ∈ S for all x ≼ s. We will frequently use the following
simple observation stating that any down-set can be viewed as a d − 1-dimensional partition. This
is best explained by Figures 1a and 1b, but we include the formal proof for completeness.

Observation 2.1. The number of down-sets S ⊆ [n]d is Pd−1(n).

Proof. We injectively map every down-set S ⊆ [n]d to a (d − 1)-dimensional integer partition as
follows. For every 1 ≤ i1, . . . , id−1 ≤ n let Ai1,...,id−1 = max{s : (i1, . . . , id−1, s) ∈ S} (where by
convention, maximum over an empty set is 0). Then clearly 0 ≤ Ai1,...,id−1 ≤ n and, since S is a
down-set, it easily follows that Ai1,...,it,...,id−1 ≥ Ai1,...,it+1,...,id−1 for every possible 1 ≤ t ≤ d − 1. In
other words, the (hyper)matrix A is a (d − 1)-dimensional n × · · · × n partition with entries from
{0, 1, . . . , n}. Furthermore, one can easily verify that this deﬁnes a bijection.

2.1 A new proof of the Erd˝os-Szekeres Theorem

Proof. Fix a black/white coloring of the edges of K3
N that has no monochromatic monotone path
of length n. We need to show that N ≤ P1(n). For every pair of vertices u < v denote C(uv) :=
(1 + nb, 1 + nw) where nb is the length (i.e., number of edges) of the longest black monotone path
ending with {u, v}, and nw is deﬁned in a similar way only with respect to white monotone paths.
Notice that C(uv) ∈ [n]2. Deﬁne

D(v) = {x ∈ [n]
2 : x ≼ C(uv) for some u < v} ,

and note that D(v) is (by deﬁnition) a down-set in [n]2. It thus follows from Observation 2.1 (and
the pigeonhole principle) that it is enough to show that D(u) ̸= D(v) for every pair of vertices.
So suppose to the contrary that u < v and D(u) = D(v). By deﬁnition, C(uv) ∈ D(v), and thus
C(uv) ∈ D(u). Hence, (again, by deﬁnition) there is a vertex t < u such that C(uv) ≼ C(tu).
However, if the edge {t, u, v} is colored black then we can extend the longest black monotone path
ending at {t, u} to a longer one ending at {u, v}, and similarly if {t, u, v} is colored white. In either
case we have C(uv) ̸≼ C(tu)—a contradiction.

2.2 Proof of Theorem 1

We begin by generalizing our proof of EST to any number of colors. In fact, the two proofs are
nearly identical, and so we will be concise here.

Lemma 2.2. N3(q, n) ≤ Pq−1(n) + 1.
 8

Proof. Fix a q-coloring of the edges of K3
N that has no monochromatic monotone path of length
n. We need to show that N ≤ Pq−1(n). For every pair of vertices u < v denote C(uv) :=
(1 + n1, . . . , 1 + nq) where ni is the length of the longest color-i monotone path ending with {u, v}.
Notice that C(u, v) ∈ [n]q. Deﬁne D(v) = {x ∈ [n]q : x ≼ C(uv) for some u < v}. Since D(v) is
a down-set in [n]q, it follows from Observation 2.1 that it suﬃces to show that D(u) ̸= D(v) for
every pair of vertices. So suppose to the contrary that u < v and D(u) = D(v). By deﬁnition,
C(uv) ∈ D(v), and thus C(uv) ∈ D(u). Hence, (again, by deﬁnition) there is a vertex t < u such
that C(uv) ≼ C(tu). However, the longest monochromatic monotone path ending at {t, u} that
has the same color as the edge {t, u, v} can be extended to a longer one ending at {u, v}, implying
C(uv) ̸≼ C(tu)—a contradiction.

We now turn to prove the lower bound of Theorem 1, namely, that N3(q, n) > Pq−1(n). We
ﬁrst focus on the case of q = 2 colors, which would simplify the notation we need. Recall that
in our proof of EST we assigned to each vertex a down-set, or equivalently, a line partition. It
therefore seems natural to do a similar thing here, and so in order to deﬁne a 2-coloring of the
edges of the complete 3-uniform hypergraph, we identify each vertex with a distinct line partition.
Of course, we now need to deﬁne a total order on the vertex set, so we order the line partitions (i.e.,
vertices) lexicographically. To be more precise: for two line partitions A ̸= B, A = (a1, . . . , an), B =
(b1, . . . , bn), denote δ(A, B) the smallest i for which ai ̸= bi; then A is lexicographically smaller
than B, denoted A ⋖ B, if aδ(A,B) < bδ(A,B).4

Our proof will follow by deﬁning a certain coloring and showing that, roughly, if we look at
the δ-value of consecutive line partitions in a monochromatic monotone path, it is either strictly
increasing, or else the δth element of the line partitions along the path is strictly increasing. Since
this clearly cannot go on for long, any monochromatic monotone path would have to be short.

Lemma 2.3. N3(2, n) > P1(n).

Proof. Put N = P1(n), and identify each vertex of K3
N with a distinct line partition of length n
with entries from {0, 1, . . . , n}, where the diﬀerent line partition are ordered lexicographically. We
need to color the edges so that there is no monochromatic monotone path of length n. Given an
edge whose vertices are (identiﬁed with) the three line partitions A ⋖ B ⋖ C, we color it black if
δ(B, C) > δ(A, B), and otherwise white.
We claim that the following holds for any monochromatic monotone path on ℓ + 2 vertices
(i.e., of length ℓ): denoting B ⋖ C its last two vertices, if all edges of the path are black then
δ(B, C) > ℓ, and if all edges of the path are white then Cδ(B,C) > ℓ. This would imply that there
is no monochromatic monotone path of length n, as required.
We prove our claim by induction on ℓ, noting that for the base case ℓ = 0 both conditions
trivially hold. Consider a path of length ℓ ≥ 1, whose last three vertices are A ⋖ B ⋖ C, and denote

4So for example, (5, 4, 3, 2, 1) ⋖ (5, 5, 3, 0, 0).
 9

δ = δ(B, C), δ′ = δ(A, B). By the deﬁnition of our coloring, if the path is black then δ > δ′ ≥ ℓ.
Otherwise, δ ≤ δ′ and so Cδ > Bδ ≥ Bδ′ ≥ ℓ, which holds since B ⋖C, and since B is decreasing.

To generalize the above lower bound to any number of colors, we ﬁrst need to deﬁne a total
ordering on partitions of any given dimension. For two d-dimensional partitions A ̸= B, denote
δ(A, B) the lexicographically smallest (i1, . . . , id) ∈ [n]d such that Ai1,...,id ̸= Bi1,...,id. We consider
A to be smaller than B, denoted A ⋖ B, if Aδ(A,B) < Bδ(A,B).5

Lemma 2.4. N3(q, n) > Pq−1(n).

Proof. Put d = q − 1, N = Pd(n), and identify each vertex of K3
N with a distinct n × · · · × n
d-dimensional partition with entries from {0, 1, . . . , n}. Further, order the vertex set using the
above deﬁned ⋖. We need to color the edges with the colors {1, 2, . . . , d + 1} so that there is no
monochromatic monotone path of length n. For every three d-dimensional partition A ⋖ B ⋖ C, if
there is an 1 ≤ i ≤ d satisfying (δ(B, C))i > (δ(A, B))i we color {A, B, C} by i (if there are several
such i we choose one arbitrarily); if there is no such i, we color the edge by d + 1.
We claim that the following holds for any monochromatic monotone path on ℓ + 2 vertices
(i.e., of length ℓ): denoting B ⋖ C its last two vertices and denoting δ(B, C) = (δ1, . . . , δd), if all
edges of the path are colored by 1 ≤ i ≤ d then δi > ℓ, and if all edges of the path are colored
by d + 1 then Cδ1,...,δd > ℓ. This would imply that there is no monochromatic monotone path
of length n. We prove our claim by induction on ℓ, noting that for the base case ℓ = 0 both
conditions trivially hold. Consider a path of length ℓ ≥ 1 whose last three vertices are A ⋖ B ⋖ C,
and denote (δ1, . . . , δd) = δ(B, C), (δ′
1, . . . , δ′
d) = δ(A, B). By the deﬁnition of our coloring, if
the path is colored by 1 ≤ i ≤ d then δi > δ′
i ≥ ℓ; otherwise, (δ1, . . . , δd) ≼ (δ′
1, . . . , δ′
d) and so
Cδ1,...,δd > Bδ1,...,δd ≥ Bδ′
1,...,δ′
d ≥ ℓ, which holds since B ⋖ C, and since B is decreasing in each line.
This completes the proof.

Proof of Theorem 1. It follows immediately from Lemma 2.2 and Lemma 2.4 that N3(q, n) =
Pq−1(n) + 1.

Let us brieﬂy mention the implications of the above arguments to a natural extension of N3(q, n).
Let N3(q, n1, . . . , nq) be the smallest integer N so that every coloring of the edges of K3
N using q
colors contains a color-i monotone path of length ni, in at least one of the colors 1 ≤ i ≤ q. One
can modify both the upper and lower bound proofs above in a straightforward manner to show that
N3(q, n1, . . . , nq) = Pq−1(n1, . . . , nq) + 1, where Pd(n1, . . . , nd, n) is the number of d-dimensional
n1 × · · · × nd (hyper)matrices with entries from {0, 1, . . . , n} that decrease in each line. One can
easily generalize the argument proving (2) to show P1(a, b) = (a+b
a ), which implies the known result
N3(2, a, b) = (a+b
a ) + 1. As for the next case, MacMahon [17] proved a result which is in fact more

5Notice this is the lexicographic ordering if we were to ”ﬂatten” the d-dimensional partitions into line partitions.
Thus, ⋖ is clearly a total order (it is transitive, and for every A ̸= B either A ⋖ B or else B ⋖ A).

10

general than the one stated in (3), namely, P2(a, b, c) = ∏a
i=1 ∏b
j=1 ∏c
k=1 i+j+k−1
i+j+k−2 , which gives an
exact bound for N3(3, a, b, c).

2.3 Proof of Theorem 3

It will be more convenient to prove the following stronger bound for every k ≥ 4:

Nk(q, n) ≤ Nk−2(N3(q, n) − 1, 2) . (7)

Proof. Fix a q-coloring of the edges of Kk
N that has no monochromatic monotone path of length n.
We need to show that N < Nk−2(N3(q, n) − 1, 2). For any k − 1 vertices x1 < · · · < xk−1 denote
C(x1, . . . , xk−1) := (1 + n1, . . . , 1 + nq) where ni is the length of the longest color-i monotone
path ending with {x1, . . . , xk−1}, and notice that C(x1, . . . , xk−1) ∈ [n]q. For any k − 2 vertices
x2 < · · · < xk−1 we deﬁne

D(x2, . . . , xk−1) = {y ∈ [n]q : y ≼ C(x1, x2, . . . , xk−1) for some x1 < x2} ,

which is of course a down-set in [n]q.
Now, we deﬁne a coloring of the complete (k − 2)-uniform hypergraph Kk−2
N (on the same
vertex set) by letting the color of an edge {x1, . . . , xk−2} be D(x1, . . . , xk−2). We claim that
there is no monochromatic monotone path of length 2 in our coloring of Kk−2
N . Indeed, sup-
pose for contradiction that {x1, . . . , xk−2} and {x2, . . . , xk−1} receive the same color, that is,
D(x1, . . . , xk−2) = D(x2, . . . , xk−1). By deﬁnition, C(x1, . . . , xk−1) ∈ D(x2, . . . , xk−1), and so
by our assumption, C(x1, . . . , xk−1) ∈ D(x1, . . . , xk−2). Hence, (again, by deﬁnition) there is a
vertex x < x1 such that C(x1, . . . , xk−1) ≼ C(x, x1, . . . , xk−2). However, in the (given) coloring
of Kk
N , the longest monochromatic monotone path ending at {x, x1, . . . , xk−2} that has the same
color as the edge {x, x1, . . . , xk−1} can be extended to a longer one ending at {x1, . . . , xk−1}, so
C(x1, . . . , xk−1) ̸≼ C(x, x1, . . . , xk−2)—a contradiction.
We conclude that in our coloring of Kk−2
N there is no monochromatic monotone path of two
edges. Therefore it must be the case that N < Nk−2(c, 2) where c is the number of colors we used.
Since each D(x1, . . . , xk−2) is a down-set in [n]q, Observation 2.1 implies c ≤ Pq−1(n), and since
Theorem 1 tells us that Pq−1(n) = N3(q, n) − 1 the proof is complete.

Having completed the proof of (7), let us prove that it implies the (weaker) bound Nk(q, n) ≤
tk−2(N3(q, n)) stated in Theorem 3. We proceed by induction on k, noting that when k = 3 there
is nothing to prove, and that the case k = 4 follows from (7) and the fact that N2(q, 2) ≤ 2q + 1
(see the discussion preceding (5)). For the induction step, assuming k ≥ 5, we have from (7)
that Nk(q, n) ≤ Nk−2(q′, 2), where q′ = N3(q, n), and by the induction hypothesis, Nk−2(q′, 2) ≤

11

tk−4(N3(q′, 2)). Applying the upper bound in Corollary 1 we deduce that

Nk(q, n) ≤ tk−4(N3(q′, 2))

≤ tk−3(2 · 2
q′−1)

= tk−2(q′)

= tk−2(N3(q, n)) ,

as needed.

2.4 An improved lower bound for Pd(n)

Recall that by Observation 2.1, Pd−1(n) is the number of down-sets in [n]d. Here it will be convenient
to use the notion dual to that of a down-set. A set A ⊆ [n]d is an antichain if a ∈ A implies x /∈ A
for all x ≼ a. In this section (and later on as well) it will be useful to refer to the following simple
observation.

Observation 2.5. The number of antichains A ⊆ [n]d is Pd−1(n).

Proof. Observe that retaining only the ≺-maximal elements of a down-set yields a unique antichain.
Moreover, every antichain can clearly be obtained from a down-set in this manner. Hence down-sets
are in bijection with antichains, and from Observation 2.1 we deduce that the number of antichains
in [n]d is exactly Pd−1(n).

We will use the antichain characterization of Observation 2.5 in order to prove a lower bound on
Pd(n). First, we need a simple lemma. For any d ≤ k ≤ dn let Sn(k, d) be the number of solutions
to the equation x1 + · · · + xd = k with xi ∈ [n] for every 1 ≤ i ≤ d. Notice that S2(k, d) are simply
the binomial coeﬃcients (speciﬁcally, S2(k, d) = ( d
k−d
)). The numbers Sn(k, d) (which were already
studied by Euler) satisfy many of the properties of binomial coeﬃcients, e.g., symmetry about the
middle Sn(k, d) = Sn(dn − k, d). In particular, it is known that maxk Sn(k, d) =: Md,n is achieved
at the middle, that is, at k = d(n + 1)/2 (this already follows from the work of de Bruijn et al. [4]).
We remark that it can be shown (using a version of the central limit theorem, see [18]) that when
d tends to inﬁnity,
 Md,n =
 √ 6
π(n2 − 1)d · nd(1 + od(1)) ( ≈
 √ 6
π · nd−1
√
d
 ) .

However, we will need to estimate Md,n for any d, and so we prove the following easy lower bound.

Lemma 2.6. For every d ≥ 1 and n ≥ 1 we have

Md,n = max
k Sn(k, d) ≥ 2
3 · nd−1
√d .

12

Proof. Let x1, . . . , xd be randomly (independently and uniformly) chosen from [n], and set X = x1+
· · ·+xd. Notice that the expectation of X is µ := d(n+1)/2, and its variance is σ2 := d(n2 −1)/12 ≤
dn2/12. By Chebyschev’s Inequality, for λ > 0 to be chosen later, Pr (|X − µ| ≥ λσ) ≤ λ−2. Put
α = 1 − λ−2. Since Pr(X = k) = Sn(k, d)/nd, we have

⌊µ+λσ⌋∑

k=⌈µ−λσ⌉ Sn(k, d) ≥ αn
d .

Using the pigeonhole principle, we can bound from below the largest Sn(k, d) in the range above,
which is Md,n, by αnd

2λσ ≥
 √3α
λ · nd−1
√d .

Choosing λ = √3 so as to maximize α/λ yields the desired bound.

We now use Lemma 2.6 above to deduce a lower bound on Pd−1(n).

Proof of Theorem 2. We show that Pd−1(n) ≥ 2
Md,n , (8)

which, by Lemma 2.6, would complete the proof. For x = (x1, . . . , xd) ∈ [n]d write |x| = ∑d
i=1 xi,
and note that Sn(k, d) is the number of x satisfying |x| = k. Let d ≤ k ≤ dn, and let A ⊆ [n]d

be a set whose every member a satisﬁes |a| = k. Then A is an antichain since every x ≼ a, where
a ∈ A and x ̸= a, must satisfy |x| < |a| = k, implying that x /∈ A. It follows that the number of
antichains in [n]d is at least 2Sn(k,d). Taking k so as to maximize Sn(k, d) shows that the number
of antichains in [n]d is at least 2Md,n. Observation 2.5 now proves (8), as needed.

3 General Hypergraphs

Our goal in this section is to give an enumerative characterization of Nk(q, n) analogous to the one
we have previously obtained for N3(q, n) in Theorem 1. We will show that just as the numbers
N3(q, n) are closely related to high-dimensional integer partitions, the numbers Nk(q, n) are closely
related to what can naturally be thought of as higher-order analogues of partitions. For simplicity
of presentation, we will focus on higher-order line partitions, which we would use to characterize
Nk(2, n). The characterization for Nk(q, n) is obtained by exactly the same arguments.
To state our characterization we will need to restate Observation 2.1 in a language that will
be somewhat easier to generalize. So for what follows, let us set P 2[n] = [n]2, and let P 3[n]
denote the family of line partitions as deﬁned in Section 1 (so ∣
∣P 3[n]
∣
∣ = P1(n)). Recall that by
Observation 2.1, line partitions are in bijection with down-sets in [n]2; put in other words, every
line partition F ∈ P 3[n] is a subset of P 2[n] with the property that if x ∈ F then so is every x′ ≼ x.
Now, to make the above easier to generalize, we think of any x = (x1, x2) ∈ [n]2 as a multiset (with

13

Figure 2: A line partition contained in another.

xi − 1 being the multiplicity of the ith element). Accordingly, we henceforth use the notation x′ ⊆ x
instead of x′ ≼ x.6

We deﬁne P 4[n] in a similar manner, so that the members of P 4[n] are down-sets in P 3[n]; that
is, each F ∈ P 4[n] is a collection of line partitions (i.e., elements of P 3[n]) with the property that
if a line partition L belongs to F then so do all line partitions L′ ⊆ L. Note that the way we have
redeﬁned line partitions in the previous paragraph allows us to talk about one line partition being
a subset of another. For the sake of clarity the reader can check Figure 2 which depicts inclusion
of two line partitions; furthermore, see Section 4 for a detailed discussion about P 4[n].
In general, we inductively deﬁne P k[n], whose members are the down-sets in P k−1[n], as follows.

Deﬁnition 3.1. Let P 2[n] = [n]2 and suppose we have already deﬁned P k−1[n]. A set F ⊆ P k−1[n]
is in P k[n] if S ∈ F implies S′ ∈ F for any S′ ⊆ S.

We denote the cardinality of P k[n] by ρk(n). In what follows, we will sometimes refer to the
members of P k[n] as line partitions of order k. We obviously have ρk(n) ≤ 2ρk−1(n) for any k ≥ 3,
and in particular, ρ4(n) ≤ 2(2n
n ) ≤ 222n. Summarizing, we have

ρ2(n) = n2, ρ3(n) = (
2n
n
 )
, ρk(n) ≤ tk−1(2n)

for any k ≥ 3. Our characterization of Nk(2, n) is thus the following.

Theorem 5. For every k ≥ 2 and n ≥ 2 we have

Nk(2, n) = ρk(n) + 1 .

Note that Theorem 5 subsumes both ESL and EST (as well as our main result in Theorem 1
when q = 2; see (10) at the end of this section for arbitrary q). The proof of Theorem 5 follows
immediately from Lemmas 3.2 and 3.4 stated below.

6For consistency, one can instead think of x as a (standard) set, say by using the “unary representation”: Letting
A, B be two disjoint ordered sets of cardinality n, we may represent x as the subset of A ∪ B consisting of the ﬁrst
x1 members of A and the ﬁrst x2 members of B.
 14

Lemma 3.2. Nk(2, n) ≤ ρk(n) + 1.

Proof. Fix a 2-coloring of the edges of Kk
N that has no monochromatic monotone path of length
n. We need to show that N ≤ ρk(n). We begin with some deﬁnitions. For every k − 1 vertices
x1 < · · · < xk−1 denote D(x1, . . . , xk−1) := (1+nb, 1+nw) where nb is the length of the longest black
monotone path ending with {x1, . . . , xk−1}, and nw is deﬁned in a similar way only with respect to
white monotone paths. Notice that D(x1, . . . , xk−1) ∈ P 2[n]. For any r ∈ {k − 2, k − 1, . . . , 1} and
any r vertices xk−r < · · · < xk−1 we recursively deﬁne

D(xk−r, . . . , xk−1) = {S ∈ P k−r[n] : S ⊆ D(x, xk−r, . . . , xk−1) for some x < xk−r} .

Since for r = k − 1 we have D(xk−r, . . . , xk−1) ∈ P 2[n], from Deﬁnition 3.1 we immediately have
that D(xk−r, . . . , xk−1) ∈ P k−r+1[n]. In particular, it holds that D(v) ∈ P k[n]. Hence to complete
the proof it suﬃces to show that D(u) ̸= D(v) for every pair of vertices.
We ﬁrst prove that for any 2 ≤ r ≤ k − 1 and any r vertices xk−r < · · · < xk−1,

D(x, xk−1) ⊆ D(xk−r, x) ⇒ ∃x < xk−r s.t. D(xk−r, x, xk−1) ⊆ D(x, xk−r, x) , (9)

where x is short for xk−r+1, . . . , xk−2. By deﬁnition, D(xk−r, x, xk−1) ∈ D(x, xk−1). Therefore, the
assumption that D(x, xk−1) ⊆ D(xk−r, x) implies D(xk−r, x, xk−1) ∈ D(xk−r, x). Hence, (again,
by deﬁnition) there is some vertex x < xk−r such that D(xk−r, x, xk−1) ⊆ D(x, xk−r, x), as desired.
By iteratively applying (9) we deduce the following. Suppose there are two vertices u < v such
that D(u) = D(v). Note that the case r = 2 of (9) is satisﬁed, namely, D(v) ⊆ D(u), where we
put xk−1 = v, xk−2 = u. Therefore, the conclusion in (9) for the case r = k − 1 must hold as well.
That is, there are k vertices x0 < · · · < xk−3 < u < v such that D(x1, . . . , u, v) ⊆ D(x0, . . . , u)
(∈ [n]2). However, the longest monochromatic monotone path ending at {x0, . . . , u} that has the
same color as the edge {x0, . . . , u, v} can be extended to a longer one ending at {x1, . . . , u, v},
implying D(x1, . . . , u, v) ̸⊆ D(x0, . . . , u)—a contradiction. This completes the proof.

Before giving the lower bound on Nk(2, n) matching our upper bound, we ﬁrst give a short proof
for the case of graphs, that is, for the fact that N2(2, n) ≥ n2 + 1, which would be suggestive of
the generalization we plan to make. In other words, we give a black/white coloring of the complete
graph on n2 vertices that has no monochromatic monotone path of length n. First, identify each
of the n2 vertices with a distinct pair of integers (x, y) ∈ [n]2, and order the pairs (i.e., vertices)
lexicographically. For an edge whose vertices are identiﬁed with the pairs (x1, y1) and (x2, y2),
where (x1, y1) is lexicographically smaller than (x2, y2), color it black if x1 < x2; otherwise, color
it white if y1 < y2. Crucially, observe that the lexicographic ordering ensures that every edge is
indeed colored by either black or white. Under this coloring, it is clear that any monochromatic
monotone path is of length at most n − 1, or equivalently, has at most n vertices, simply because
the pairs along the path are strictly increasing either in the ﬁrst or in the second coordinate.

15

Let us give the necessary deﬁnitions we will need in order to prove the lower bound on Nk(2, n)
stated in Lemma 3.4 below. We begin by extending the lexicographic ordering of pairs of nonneg-
ative integers (which are line partitions of order 2) to partitions of arbitrary order. Assuming we
have already deﬁned lexicographic ordering for line partitions of order k − 1, we say that an order-k
line partition F is lexicographically smaller than an order-k line partition F ′, denoted F ⋖F ′, if the
lexicographically ﬁrst element on which they diﬀer (that is, the lexicographically ﬁrst member of
the symmetric diﬀerence F△F ′) is in F ′.7 (This ordering in fact coincides with the one preceding
the proof of Lemma 2.3 that we used for the k = 3 case.)
Furthermore, when two order-k line partition F, F ′ satisfy F ⊉ F ′ we denote δ(F, F ′) the
lexicographically ﬁrst element that F ′ contains and F does not (that is, the lexicographically ﬁrst
member of F ′ \ F).8 Note that δ(F, F ′) is a line partition of order k − 1; that is, if F, F ′ ∈ P k[n]
then δ(F, F ′) ∈ P k−1[n].

Claim 3.3. For any sequence of order-k line partitions F1 ⊉ F2 ⊉ · · · ⊉ Ft we have δ(F1, F2) ⊉
δ(F2, F3) ⊉ · · · ⊉ δ(Ft−1, Ft).

Proof. It suﬃces to show that for any three order-k line partitions F1 ⊉ F2 ⊉ F3 we have
δ(F1, F2) ⊉ δ(F2, F3). By deﬁnition, δ(F1, F2) ∈ F2 and δ(F2, F3) /∈ F2. Since F2 is closed
under taking subsets, it cannot be the case that δ(F2, F3) ⊆ δ(F1, F2).

Lemma 3.4. Nk(2, n) > ρk(n).

Proof. Put N = ρk(n), and identify the vertex set of Kk
N with P k[n], ordered lexicographically.
We need to color the edges so that there is no monochromatic monotone path of length n. Let
e = {F1, . . . , Fk} be an edge, and note that since the Fi’s are lexicographically ordered F1 ⋖· · ·⋖Fk
it follows that F1 ̸⊇ · · · ̸⊇ Fk. By Claim 3.3 we have δ(F1, F2) ⊉ · · · ⊉ δ(Fk−1, Fk), and observe
that we may apply Claim 3.3 again, this time on the sequence of δ’s, which is a sequence of k − 1
line partitions of order k − 1. By applying Claim 3.3 i times in a similar fashion we obtain a
sequence of k − i line partitions in P k−i[n]. In particular, after i = k − 2 applications we obtain
two pairs (x1, y1) =: δ∗(F1, . . . , Fk−1) and (x2, y2) =: δ∗(F2, . . . , Fk) that belong to P 2[n] (= [n]2)
and satisfy (x1, y1) ̸⊇ (x2, y2). We color the edge e black if x1 < x2; otherwise, we necessarily have
y1 < y2, and we color e white.
Observe that a monochromatic monotone path of length ℓ determines a sequence of ℓ + 1 pairs
from [n]2 (namely, if the path is on the vertices F1 ⋖ · · · ⋖ Fℓ+k−1 then it determines the ℓ + 1 pairs
δ∗(F1, . . . , Fk−1), δ∗(F2, . . . , Fk), . . . , δ∗(Fℓ+1, . . . , Fℓ+k−1)). Moreover, these pairs strictly increase
either in the ﬁrst or in the second coordinate. We deduce that ℓ + 1 ≤ n, completing the proof.

7The reader may ﬁnd it useful here to think of an order-k line partition as a 0/1-vector indexed by order-
(k − 1) line partitions that are ordered lexicographically. Now, F is lexicographically smaller than F ′ precisely when
0 = FS < F ′
S = 1 where S is the ﬁrst index in which the two vectors diﬀer.
8In the vector terminology mentioned earlier, δ(F, F ′) is the ﬁrst index S such that 0 = FS < F ′
S = 1.

16

Having completed the proof of Theorem 5 we ﬁnally mention that all the above can be extended
in a straightforward manner to any number q > 2 of colors, so as to determine Nk(q, n). Setting
P 2
d [n] = [n]d, we deﬁne P k
d [n] so that its members are the down-sets in P k−1
d [n], similarly to what
we did before. Denoting ρk,d(n) = ∣
∣P k
d [n]
∣
∣, we of course have ρ3,d(n) = Pd−1(n), and since for any
k ≥ 3, ρk,d(n) ≤ 2ρk−1,d(n), we have ρk,d(n) ≤ tk−2(Pd−1(n)). By following the proofs in this section
essentially line by line, and replacing [n]2 with [n]q, one obtains the characterization

Nk(q, n) = ρk,q(n) + 1 . (10)

We now use the above characterization to deduce a recursive lower bound on Nk(q, n).

Lemma 3.5. For every k ≥ 4, q ≥ 2, and n ≥ 2 we have

Nk(q, n) ≥ 2Nk−1(q,n)/Nk−2(q,n) .

Proof. We show that for every k ≥ 4, d ≥ 2, and n ≥ 2, we have ρk,d(n) ≥ 2(ρk−1,d(n)+1)/(ρk−2,d(n)+1),
from which the proof immediately follows using (10). Put U = ρk−2,d(n). Let Li be the number of
sets A ∈ P k−1
d [n] of cardinality i, for some 0 ≤ i ≤ U . Observe that any collection of such sets A,
together with all A′ ⊆ A, determines a distinct down-set; indeed, any such down-set has a unique
set of maximal elements. It therefore follows that ρk,d(n) ≥ 2Li. Now, take i so as to maximize Li.
Since ρk−1,d(n) = ∑U
j=0 Lj, we have Li ≥ ρk−1,d(n)/(U + 1), and in fact, this inequality is clearly
strict. The desired inequality now follows.

We will show that Theorem 4 follows by iteratively applying Lemma 3.5. First, we need a
simple lemma concerning diﬀerences of towers. We henceforth write log() for log2().

Lemma 3.6. For any k ≥ 2 and positive reals a ≥ b + 1, a ≥ 3, we have tk(a) − tk(b) ≥
tk(a − 2−(k−2)).

Proof. We proceed by induction on k. For the base case k = 2 we have 2a − 2b ≥ 2a − 2a−1 = 2a−1,
as needed. Now, observe that it follows from the standard estimate 1 − p ≥ e−2p, applicable for
any 0 ≤ p ≤ 1
2 , that for every pair of positive reals x ≥ 2y we have x − y = x(1 − y/x) ≥ xe−2y/x.
So for every x ≥ 2y > 0 we have

log(x − y) ≥ log x − 2 log(e)y/x ≥ log x − 3y/x . (11)

Denote by log(i)() the i ≥ 1 times iterated log() (so, e.g., log(2)(x) = log log(x)). For the induction
step, which is equivalent to log(k−1)(tk(a) − tk(b)) ≥ a − 2−(k−2), we have

log(k−1)(tk(a) − tk(b)) = log log(k−2)(tk−1(2
a) − tk−1(2
b))

≥ log(2
a − 2−(k−3))

≥ a − 3 · 2−(k−3)/2
a

≥ a − 1
2 · 2−(k−3) ,

17

where the ﬁrst inequality follows from the induction hypothesis, the second inequality from (11),
and the third inequality from the assumption that a ≥ 3. The proof follows.

Proof of Theorem 4. The case k = 4 follows immediately from Theorem 4 and the fact that
N2(q, n) ≤ nq + 1 (see the discussion preceding (5)). We prove by induction on k ≥ 5 that
Nk(q, n) ≥ tk−2( N3(q,n)
2nq − ∑k−6
i=0 2−i), from which the result clearly follows. We assume throughout
the proof that n is larger than some absolute constant (i.e., independent of q, k). For the base case
k = 5 we get
 log N5(q, n) ≥ N4(q, n)/N3(q, n)

≥ 2N3(q,n)/(nq+1)/N3(q, n)

≥ 2N3(q,n)/2nq ,

where the ﬁrst and second inequalities rely on Lemma 3.5, and the last inequality is due to the fact
that log2 N3(q, n) = on(N3(q, n)/nq) (12)

uniformly for all n larger than some absolute constant (i.e., independently of q; this easily follows
from the bounds in Corollary 1). For the induction step, assuming k ≥ 6, we have

log Nk(q, n) ≥ Nk−1(q, n)/Nk−2(q, n)

≥ Nk−1(q, n)/tk−4(N3(q, n))

≥ 2tk−4( N3(q,n)
2nq −∑k−7
i=0 2−i)−tk−4(log N3(q,n))

≥ 2tk−4( N3(q,n)
2nq −∑k−7
i=0 2−i−2−(k−6))

= tk−3( N3(q, n)
2nq −
 k−6∑

i=0 2−i) ,

where the ﬁrst inequality follows from Lemma 3.5, the second inequality from the upper bound
Nk(q, n) ≤ tk−2(N3(q, n)) in Theorem 3, the third inequality from the induction hypothesis, and
the fourth inequality from Lemma 3.6 using the fact that k − 4 ≥ 2, as well as (12). This completes
the proof.

4 Concluding Remarks and Open Problems

An exact bound for the two-edge path?: Combining Theorem 1 together with Observa-
tion 2.5 we see that N3(q, n) is determined by the number of antichains in [n]q. In particular,
N3(q, 2) − 1 is the number of antichains in [2]q, where [2]q is the Boolean poset over [q], that is, the
poset of the subsets—ordered by inclusion—of a q-element ground set. These numbers are called
Dedekind numbers, ﬁrst introduced by Dedekind in [6], and despite much research they have no
known (reasonable) closed formula. Hence, we do not expect a closed formula even for N3(q, 2)
(i.e., the case of two-edge paths), which is the simplest non-trivial case (for any given q).

18

The exact exponent of N3(q, n): While Dedekind numbers do not have a closed formula,

Kleitman [13] has shown that the number of antichains in [2]d is at most 2(1+o(1))( d
d/2). Note that

2( d
d/2) is a trivial lower bound since any family of subsets of [d], all of the same cardinality d/2, is
an antichain. So Kleitman’s result can be phrased as saying that the size of the largest antichain in
[2]d essentially determines also the number of antichains. It is known that the poset [n]d (equipped
with the partial order ≼) satisﬁes the so-called “Sperner property”, which means here that the
largest antichain in [n]d is also the “middle layer”. As noted in Subsection 2.4, the middle layer
is of size (1 + od(1))
√
6/dπ · nd−1 for d, n ≫ 1, so Pd−1(n) is (at least) exponentially larger than
this.9 Now, recall that our best upper bound on Pd−1(n) is (roughly) 22nd−1, so the two exponents
are oﬀ by a √d factor.
As the problem of estimating the number of antichains in [n]d seems like a natural extension
of the classical problem of estimating the Dedekind numbers (which is the number of antichains in
[2]d), the following question seems especially natural—does the phenomenon in Dedekind’s problem
hold in this case as well? In other words, is the number of antichains in [n]d of order 2cnd−1/
√d? One
might even be bolder and ask if the exact constant in the exponent is √
6/π (as the one in the size of
the largest antichain). Such a bound would immediately imply that N3(q, n) = 2
(1+o(1))nq−1/
√πq/6

with the o(1) term going to 0 as q → ∞.
We note that by now there are several proofs [12, 14, 15, 22] of Kleitmen’s result10 but as of now
we are not able to apply any of them in order to prove that the number of antichains in [n]d is of
order 2O(nd−1/
√d). It is worth mentioning here that an antichain in the poset [n]d is nothing but an
independent set in the graph whose vertex set is [n]d and with an edge between any two x, y ∈ [n]d

satisfying x ≼ y or y ≼ x (this is the corresponding comparability graph). So it seems that the
next step towards a complete solution of the Ramsey-type problem considered in this paper is yet
another classical enumerative problem, namely, that of counting independent sets.

Tighter bounds for N4(2, n): While we know that N3(2, n) = (2n
n )+1, it seems hard to determine
even the asymptotics of Nk(2, n) for k > 3. Let us explain why this is the case by focusing on k = 4.
Recall that by Corollary 2 we know that N4(2, n) = 22(2−o(1))n. However, as for the logarithm of
N4(2, n), what we know by Theorem 3 and Lemma 3.5 is only that (roughly)
(2n
n
 )/n
2 ≤ log2 N4(2, n) ≤ (
2n
n
 ) .

Actually, the enumerative characterization in Theorem 5 tells us more. Deﬁne a poset on the set of
line partitions P 3[n] by letting P ≼ P ′ whenever P is below P ′ (as in Figure 2). This poset is known
in the literature as (the restricted) Young’s lattice L(n, n) (see, e.g., [26], Section 3.1.2), and from

9So we also note that the constant 2/3 in Theorem 2 can be improved to √
6/π when d is large.
10We remark that earlier works, such as the one by Hansel [11], proved the weaker result that the number of
antichains in [2]n is at most C( n
n/2) for some absolute constant C. Observe, however, that proving a similar result in our
setting, that is, that the number of antichains in [n] is at most C nd−1/
√d will suﬃce to prove that Pd(n) ≤ 2O(nd−1/
√d).

19

Theorem 5 it follows that N4(2, n) − 1 is exactly equal to the number of antichains in L(n, n) (as it
clearly equals the number of down-sets there). A well-known result in enumerative combinatorics
states that this poset has the Sperner property (this was ﬁrst shown by Stanley in [24]), implying
that the largest antichain in it is obtained by taking every line partition such that the area below
it is 1
2 n2. However, the number M (n) of these line partitions is, as far as we know, not well
understood, even asymptotically. It therefore seems that determining N4(2, n) is hard; even if
L(n, n) is a “nice” poset, in the sense that the same phenomenon in Dedekind’s problem holds and
the number of antichains in L(n, n) is 2Θ(M (n)), it seems that in order to determine N4(2, n) one
must ﬁrst know M (n).
Let us mention here that a lower bound for M (n) is not too hard to obtain. Indeed, letting X
be the area below a random member of L(n, n), one can show that the variance of X is O(n3). By
Chebyschev’s Inequality, the area below most members of L(n, n) deviates from 1
2 n2 by O(n3/2), and
so M (n) ≥ Ω(|L(n, n)| /n3/2) (which improves on the “naive” bound M (n) ≥ |L(n, n)| /(n2 + 1)).
Note that this implies that log2 N4(2, n) ≥ Ω((2n
n )/n3/2), as N4(2, n) ≥ 2M (n) similarly to the proof
of Theorem 2. It seems reasonable to believe that M (n), and respectively log2 N4(2, n), are not
much larger than the aforementioned lower bounds.

Transitive colorings: As in the rest of the paper, let us assume that the vertices of the complete
hypergraphs Kk
N are the integers 1, . . . , N . We say that a q-coloring of the edges of Kk
N is transitive
if the following condition holds; for every (k + 1)-tuple of vertices x1 < x2, . . . < xk+1, if the two
edges {x1, . . . , xk}, {x2, . . . , xk+1} received color i, then so did the other k − 1 edges consisting
of k of the vertices x1, . . . , xk+1. Let N ′
k(q, n) be the variant of Nk(q, n) restricted to transitive
colorings. The problem of bounding N ′
k(q, n) was raised by Eli´aˇs and Matouˇsek [8]. We clearly
have N ′
k(q, n) ≤ Nk(q, n) so the main question is whether N ′
k(q, n) is a tower of height k − 1 as is
Nk(q, n). It is not hard to see that the coloring showing that N2(q, n) > nq is transitive, implying
that N ′
2(q, n) = N2(q, n). One can also check that the colori ng we use in the proof of Lemma 2.4
is transitive, implying that N ′
3(q, n) = N3(q, n). One is thus tempted to ask if N ′
k(q, n) = Nk(q, n)?
As it turns out, the coloring we use to prove Lemma 3.4 is not transitive. So the question of
deciding if N ′
k(q, n) = Nk(q, n) remains an interesting open problem. It might very well be possible
to deﬁne a variant of our coloring that will be transitive and give comparable bounds.

A better exponent for Pd(n): It is not hard to see that one can derive from (3) the bound
N3(3, n) = (27/16)3/2·n2(1−o(1)) = 2(c−o(1))n2, where c = 3
2 (3 log2 3 − 4) ≈ 1.1323. This of course
means that the bound in (4) can be improved to Pd(n) ≤ 2(c−o(1))nd (for d ≥ 2), implying similar
improvements of the constants involved in the results stated in Subsections 1.3 and 1.5 (for q ≥ 3).
This can also be used to show that Nk(3, n) = tk−1((c − o(1))n).

Acknowledgment: We are extremely grateful to Benny Sudakov for suggesting to us some of the
problems studied in this paper.
 20

References

[1] M. Aigner. A Course in Enumeration. Springer, 2007. 1.2

[2] G. Andrews and K. Ericson. Integer Partitions. Cambridge University Press, 2004. 1.2

[3] G. D. Bailey. Coherence and Enumeration of Tilings of 3-Zonotopes. Discrete & Computational
Geometry, 22(1):119–147, 1999. 1.2

[4] N. G. de Bruijn, Ca. van Ebbenhorst Tengbergen, and D. Kruyswijk. On the set of divisors
of a number. Nieuw Arch. Wiskunde, 23:191–193, 1951. 2.4

[5] V. Chv´atal and J. Koml´os. Some combinatorial theorems on monotonicity. Canad. Math.
Bull., 14:151–157, 1971. 1.3

[6] R. Dedekind. ¨Uber zerlegungen von zahlen durch ihre gr¨ossten gemeinsamen teiler. Festschrift
Hoch. Braunschweig u. ges. Werke, II:103–148, 1897. 4

[7] R. P. Dilworth. A decomposition theorem for partially ordered sets. Ann. of Math., 51:161-166,
1950. 1.3

[8] M. Eli´aˇs and J. Matouˇsek. Higher-order Erd˝os–Szekeres theorems. ArXiv e-prints, November
2011. 1.5, 4

[9] P. Erd˝os and G. Szekeres. A combinatorial problem in geometry. Compositio Math., 2:463–470,
1935. 1.1, 1.1, 1.3

[10] J. Fox, J. Pach, B. Sudakov, and A. Suk. Erd˝os-Szekeres-type theorems for monotone paths
and convex bodies. Proc. London Math. Soc., 2012. 1.3, 3, 1.3, 1.4, 1.4, 1.5, 1.5

[11] G. Hansel,. Sur le nombre des fonctions bool´eennes monotones de n variables. C. R. Acad.
Sci. Paris S´er. A-B, 262:A1088–A1090, 1966. 10

[12] J. Kahn. Entropy, independent sets and antichains: a new approach to Dedekind’s problem.
Proc. Amer. Math. Soc., 130(2):371–378, 2002. 4

[13] D. Kleitman. On Dedekind’s problem: the number of monotone Boolean functions. Proc.
Amer. Math. Soc., 21(3):677–682, 1969. 4

[14] D. Kleitman and G. Markowsky. On Dedekind’s problem: the number of isotone Boolean
functions. II. Trans. Amer. Math. Soc., 213:373–390, 1975. 4

[15] A. D. Korshunov. The number of monotone Boolean functions. Problemy Kibernet., 38:5–108,
272, 1981. 4
 21

[16] P A. MacMahon. Memoir on the theory of the partitions of numbers—Part I. Philos. Trans.,
187:619–673, 1897; Collected papers, Vol. I (ed. G. E. Andrews; MIT Press, Cambridge, MA,
1978) 1026–1080. 1.2

[17] P A. MacMahon. Combinatory analysis. Two volumes (bound as one). Chelsea Publishing
Co., New York, 1960. 1.2, 2.2

[18] L. Mattner and B. Roos. Maximal probabilities of convolution powers of discrete uniform
distributions. Statistics & Probability Letters, 78(17):2992 – 2996, 2008. 2.4

[19] L. Mirsky. A dual of Dilworth’s decomposition theorem. American Math. Month., 78:876-877,
1971. 1.3

[20] W. Morris and V. Soltan. The Erd˝os-Szekeres problem on points in convex position—a survey.
Bull. Amer. Math. Soc. (N.S.), 37(4):437–458 (electronic), 2000. 1

[21] V. Mustonen and R. Rajesh. Numerical estimation of the asymptotic behaviour of solid parti-
tions of an integer. Journal of Physics A: Mathematical and General, 36(24):6651–6659, 2003.
1.2

[22] N. Pippenger. Entropy and enumeration of Boolean functions. IEEE Trans. Inform. Theory,
45(6):2096–2100, 1999. 4

[23] A. Seidenberg. A simple proof of a theorem of Erd˝os and Szekeres. J. London Math. Soc.,
34:352, 1959. 1.1, 1.4

[24] R. P. Stanley. Weyl groups, the hard Lefschetz theorem, and the Sperner property. SIAM J.
Algebraic Discrete Methods, 1(2):168–184, 1980. 4

[25] R. P. Stanley. Plane partitions: past, present, and future. In Combinatorial Mathematics:
Proceedings of the Third International Conference (New York, 1985), volume 555 of Ann. New
York Acad. Sci., pages 397–401. New York Acad. Sci., New York, 1989. 1.2

[26] R. P. Stanley. Some applications of algebra to combinatorics. Discrete Appl. Math., 34:241–277,
1991. 4

[27] J. M. Steele. Variations on the monotone subsequence theme of Erd˝os and Szekeres. In
Discrete Probability and Algorithms, volume 72 of The IMA Volumes in Mathematics and Its
Applications, pages 111–131. Springer-Verlag, 1995. 1.1

22
