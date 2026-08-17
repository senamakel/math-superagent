<!-- source: https://www.irif.fr/~berthe/Articles/3d.pdf | converted from PDF -->

Three distance theorems and combinatorics on
words

Pascal Alessandri, Val´erie Berth´e

Abstract

The aim of this paper is to investigate the connection between some
generalizations of the three distance theorem and combinatorics on
words for sequences deﬁned as codings of irrational rotations on the
unit circle. We also give some new results concerning the frequencies
of factors for such sequences.

1 Introduction

For a given α in ]0, 1[, let us place the points {0}, {α}, {2α}, . . . , {nα}
on the unit circle (we mean here the circle of perimeter 1), where {x}
denotes as usual, the fractional part of x (i.e., if ⌊x⌋ denotes the largest
integer not exceeding x, {x} = x−⌊x⌋). These points partition the unit
circle into n + 1 intervals having at most three lengths, one being the
sum of the other two. This property is known as the three distance
theorem and can be seen as a geometric interpretation of good approx-
imation properties of the Farey partial convergents in the continued
fraction expansion of α.
The connection between this classical theorem in diophantine ap-
proximation and combinatorics on words is particularly apparent in
the following result, known as the three gap theorem, which is equiv-
alent to the three distance theorem and can be seen as its “dual”:
assume we are given α and β in the interval ]0, 1[, the gaps between
the successive n for which {αn} < β take at most three values, one
being the sum of the other two. It is indeed natural to introduce the
binary sequence with values 0 and 1, deﬁned as the coding of the orbit
of a point of the unit circle under the rotation by angle α with respect
to the intervals [0, β[, [β, 1[ (in particular, if β equals 1 − α or α, this
sequence is a Sturmian sequence): the lengths of strings consisting of
0’s and 1’s are thus directly connected with the three gaps. In fact, the
three distance and the three gap theorems have deep relations with the

1

measure-theoretic and topological properties of the dynamical systems
associated with codings of rotations.
The aim of this paper is to review the diﬀerent generalizations of the
three distance and three gap theorems and to emphasize the relation-
ships with combinatorics on words. This paper is organized as follows.
We recall in Section 2 basic deﬁnitions and properties concerning cod-
ings of rotations. We emphasize the connections between frequencies
of factors of given length for such sequences and the lengths of the
intervals obtained by partitioning the unit circle by a set of points in
arithmetical progression. We prove in particular that the three dis-
tance theorem is equivalent to the fact that the frequencies of factors
of given length of a Sturmian sequence take at most three values. Fur-
thermore, this last statement is easily proved by using the notion of
graph of words, which gives us a very simple combinatorial proof of the
three distance theorem. Section 3 is devoted to the study of the three
distance theorem. We introduce the three gap theorem in Section 4.
We will deduce from these two theorems in Section 5 the expression of
the recurrence function of a Sturmian sequence, due to Hedlund and
Morse [40]. Section 6 deals with generalizations of the three distance
and the three gap theorems. We give in Section 7 a direct proof of
a particular case of the two-dimensional version of the three distance
theorem (i.e., that there are at most 5 lengths when the unit circle is
partitioned by the points {iα} and {iα + β}, for 0 ≤ i ≤ n). In Sec-
tion 8, we give a proof of the 3d distance theorem, proved by Chung
and Graham [18, 37] (i.e., that there are at most 3d lengths when the
unit circle is partitioned by the points {kiα + γi}, for 0 ≤ i ≤ d and
0 ≤ ki ≤ ni).
In each case, we study the connection with frequencies of codings of
rotations. More precisely, we prove that the frequencies of a coding of
an irrational rotation with respect to a partition in two intervals take
ultimately at most 5 values and we deduce from the two-dimensional
version of the three distance theorem that the frequencies of a coding
of an irrational rotation with respect to a partition in d intervals of
the same length take ultimately at most d + 3 values; more generally,
we prove that the frequencies of a coding of an irrational rotation
with respect to a partition into d intervals (not necessarily of the same
length) take ultimately at most 3d values (this result corresponds to
the 3d distance theorem).

Let us ﬁrst review some of the many related results and applications
of the three distance theorem. We will focus on the theorem itself and
its diﬀerent proofs in Section 3.
As one of the ﬁrst applications the theorem of Hartman [33] (which
answers an earlier question of Steinhaus concerning the circular dis-

2

persion spectrum) has been proved in [53].

Theorem 1 Let 0 < α < 1 be an irrational number and let n be a pos-
itive integer. Let Hn (respectively hn) denote the maximal (respectively
the minimal) length of the n + 1 intervals obtained by partitioning the
unit circle by the points of the set {iα, 0 ≤ i ≤ n−1}. If the partial quo-
tients of the regular continued fraction expansion of α are unbounded,
then lim inf
n→+∞ n.hn = 0,

lim sup
n→+∞ n.hn = 1,

lim inf
n→+∞ n.Hn = 1,

lim sup
n→+∞ n.Hn = +∞.

In [21] Del´eglise studies the length L(h) of the smallest closed in-
terval I of the unit circle such that I, 2I, . . . , hI cover the circle. More
precisely, he shows the following result.

Theorem 2 Let I be a closed interval of minimal length L such that
I, 2I, . . . , hI cover the circle; we have, for h ≥ 3

L = { 3/(h(h + 2)), if h ≡ 0 or 1 mod 3,
3/(h(h + 2) − 2), if h ≡ 2 mod 3.

In particular, the function L(h) is equivalent to 3/h2 when h tends
towards inﬁnity.
In [7], Bessi and Nicolas apply the three distance theorem to 2-
highly composite numbers, i.e., if N2 denotes the set of integers having
only 2 and 3 as prime factors, an integer n in N2 is said to be a 2-highly
composite number if for any m in N2 such that m < n, then the number
of divisors of m is strictly less than n. They prove, in particular, that
there exists a constant c such that the number of 2-highly composite
numbers smaller than X is larger than c(log X)
4/3.
In [8] Boshernitzan extends the three distance theorem to the case
of interval exchange maps in his proof of Keane’s conjecture, which
states the unique ergodicity of Lebesgue almost all minimal interval
exchange maps. Let us recall brieﬂy the deﬁnition of an interval ex-
change map. Assume we are given λ = (λ1, . . . , λr) in the positive cone
in IR
r, i.e., λi > 0, for 1 ≤ i ≤ r; it deﬁnes a segment I = [0, ∑r
1 λk[
of IR composed of r intervals Ii = [
∑i
0 λk, ∑i+1
1 λk[, for 0 ≤ i ≤ r − 1
and by taking λ0 = 0. Let σ denote a permutation of {1, 2, . . . , r}.
The interval exchange map T associated with λ and σ is deﬁned as

3

the map from I to I which exchanges the intervals Ii according to the
permutation σ:

T (x) = x +
 

 ∑

j<σ(i) λσ−1(j) − ∑

j<i λi


 , for x ∈ Ii.

The n-fold iterate of T is also an interval exchange map of say r(n)
intervals I1, . . . , Ir(n). Boshernitzan proved the following.

Theorem 3 The number of intervals I1, . . . , Ir(n) of diﬀerent length
is not greater than 3(r − 1), for all n ≥ 1.

Let us note that a two interval exchange map is a rotation; hence when
r = 2, this theorem reduces to the three distance theorem.
As another ergodic application, we have the following. In [5] (see
also [12]) topological and measure-theoretic covering numbers (i.e., the
maximal measure of Rokhlin stacks having some prescribed regularity
properties) are computed ﬁrst for the symbolic dynamical systems as-
sociated to the rotation of argument α acting on the partition of the
circle by the point β and then to exchange of three intervals; in this
way, it is proved that every ergodic exchange of three intervals has sim-
ple spectrum, and a new class of exchanges of three intervals having
nondiscrete spectrum is built. Results for irrational rotations of the
torus TT2 can also be obtained, by replacing intervals by Vorono¨ı cells
(see [16]).
The connections between Beatty sequences and the three distance
and three gap theorems, and more precisely with the gaps in the in-
tersection of Beatty sequences, have been investigated by Fraenkel and
Holzman in [26]. We will discuss their results in Section 6.
J. Shallit introduces in [47] a measure of automaticity of a sequence.
This measure counts the number of states in a minimal deterministic
ﬁnite automaton which generates the preﬁx of size n of this sequence.
Let us recall that a sequence has a ﬁnite measure of automaticity if and
only if this sequence is a letter-to-letter projection of a ﬁxed point of a
constant length morphism of a free monoid. The author deduces in [47]
a measure of automaticity of Sturmian codings of rotations from the
three distance theorem, which are shown to have a high automaticity
measure, even when they are ﬁxed points of homomorphism.

Theorem 4 Let 0 < α < 1 be an irrational number with bounded par-
tial quotients. Let un = ⌊(n+1)α⌋−⌊nα⌋, for n ≥ 1. The automaticity
of the sequence (un)n≥1 has the same order of magnitude as n1/5.

Let us also note the following two applications of the three distance
theorem in theoretical computer science. The ﬁrst one deals with mul-
tiplicative hashing, as Fibonacci hashing, and is quoted in [34]. The

4

second one is due to Lef`evre and gives a fast algorithm for computing a
lower bound on the distance between a straight line and the points of a
regular grid. This algorithm is used to ﬁnd worst cases when trying to
round the elementary functions correctly in ﬂoating-point arithmetic
(see [36]).
Langevin studies in [35] the three distance theorem in connection
with a mathematical model of the ventricular parasystole. He proves
in particular the following generalization of the three distance theorem
to lattices.

Theorem 5 Let L be a lattice in IR
2. Let I be a bounded interval of IR
and let L(I) = {(x, y), x ∈ I} ∩ L. For any point M of L(I), let S(M )
denote the smallest point M ′ ̸= M of L(I) such that M is smaller
than M ′, in lexicographic order. Then there exists a basis (U, V ) of the
lattice L such that for any point M of L(I), the diﬀerence S(M ) − M
is either equal to U , V or U + V .

Let us note that this theorem has been generalized by Fried and V. T.
S´os to groups in [28].
Finally, Van Ravenstein studies in [43] the phenomenon of phyl-
lotaxis, i.e., the regular leaf arrangement, which is given by the Fi-
bonacci phyllotaxis for most plants (see also the work of Marzec and
Kappraﬀ in [38]). In [42] Van Ravenstein also applies the three distance
theorem to evaluate some values of the discrepancy of the sequence
(nα)n∈IN, for α irrational.

2 Codings of rotations

The aim of this section is to introduce some deﬁnitions concern-
ing sequences deﬁned as codings of irrational rotations on the unit
circle, and more precisely measure-theoretic and topological proper-
ties of sequences with values in a ﬁnite alphabet. For p ≥ 2, let
F = {β0 < β1 < . . . < βp−1} be a set of p consecutive points of
the unit circle (identiﬁed in all that follows with [0, 1[ or with the
unidimensional torus IR/ZZ) and let βp = β0. Let α be an irrational
number in ]0, 1[ and let us consider the positive orbit of a point x of
the unit circle under the rotation by angle α, i.e., the set of points
{{αn + x}, n ∈ IN}. We denote by IN the set of non-negative integers.
The coding of the orbit of x under the rotation by angle α with re-
spect to the partition {[β0, β1[, [β1, β2[, . . . , [βp−1, βp[} is the sequence
(un)n∈IN deﬁned on the ﬁnite alphabet Σ = {0, . . . , p − 1} as follows:

un = k ⇔ {x + nα} ∈ [βk, βk+1[, for 0 ≤ k ≤ p − 1.

5

A coding of the rotation R means the coding of the orbit of a point x
of the unit circle under the rotation R with respect to a ﬁnite partition
of the unit circle consisting of left-closed and right-open intervals.
For instance, consider the case F = {0, 1 − α}, i.e., P = {[0, 1 −
α[, [1 − α, 1[}, where α is an irrational number in ]0, 1[. We could also
choose to code the orbit of the rotation with respect to the following
partition: P ′ = {]0, 1 − α], ]1 − α, 1]}. As α is irrational, the two se-
quences obtained by coding with respect to P or to P ′ are ultimately
equal. Such sequences are called Sturmian sequences (such a coding is
called a Sturmian coding). Sturmian sequences have received consider-
able attention in the literature. We refer the reader to the impressive
bibliography of [9]. A recent account on the subject can also be found
in [6]. The most famous Sturmian sequence is the Fibonacci sequence
(α = τ − 1, x = α), where τ = (
√5 + 1)/2 denotes the golden ratio;
this sequence is the ﬁxed point of the following substitution

σ(1) = 10, σ(0) = 1.

Let us recall that a substitution deﬁned on the ﬁnite alphabet A is a
map from A to the set of words deﬁned on A, denoted by A
⋆, extended
to A
⋆ by concatenation, or in other words, a homomorphism of the free
monoid A
⋆.
The results stated for codings of rotations with respect to left-
closed and right-open intervals are obviously true for left-open and
right-closed partitions.

2.1 Complexity and frequencies of codings of rota-
tions

A factor of the inﬁnite sequence u is a ﬁnite block w of consecutive
letters of u, say w = un+1 · · · un+d; d is called the length of w, denoted
by |w|. Let p(n) denote the complexity function of the sequence u with
values in a ﬁnite alphabet: it counts the number of distinct factors of
given length of the sequence u. For more information on the subject,
we refer the reader to the survey [2].
With the above notation, consider a coding u of the orbit of a
point x under the rotation by angle α with respect to the partition
{[β0, β1[, [β1, β2[, . . . , [βp−1, βp[}. Let Ik = [βk, βk+1[ and let R denote
the rotation by angle α. A ﬁnite word w1 · · · wn deﬁned on the alphabet
Σ = {0, 1, . . . , p − 1} is a factor of the sequence u if and only if there
exists an integer k such that

{x + kα} ∈ I(w1, . . . , wn) =
 n−1⋂

j=0 R−j(Iwj+1 ).

6

As α is irrational, the sequence ({x + nα})n∈IN is dense in the unit
circle, which implies that w1w2 . . . wn is a factor of u if and only if
I(w1, . . . , wn) ̸= ∅. In particular, the set of factors of a coding does
not depend on the initial point x of this coding. Furthermore, the
connected components of these sets are bounded by the points

{k(1 − α) + βi}, for 0 ≤ k ≤ n − 1, 0 ≤ i ≤ p − 1.

Let us recall that the frequency f (B) of a factor B of a sequence is
the limit, if it exists, of the number of occurrences of this block in the
ﬁrst k terms of the sequence divided by k. Thus the frequency of the
factor w1 . . . wn exists and is equal to the density of the set

{k | {x + kα} ∈ I(w1, . . . , wn)},

which is equal to the length of I(w1, . . . , wn), by uniform distribution
of the sequence ({x + nα})n∈IN. These sets consist of ﬁnite unions of
intervals. More precisely, if for every k, βk+1 − βk ≤ sup(α, 1 − α),
then these sets are connected; if there exists K such that βK+1 −
βK > sup(α, 1 − α), then the sets are connected except for w1 . . . wn
of the form an
K (see [1]) (the notation an
K denotes the word of length
n obtained by successive concatenations of the letter aK). Let us
note that there exists at most one integer K satifying βK+1 − βK >
sup(α, 1 − α). We thus have the following lemma which links the three
distance theorem and related results to the frequencies of codings of
rotations.

Lemma 1 Let u be a coding of a rotation by irrational angle α on the
unit circle with respect to the partition

{[β0, β1[, [β1, β2[, . . . , [βp−1, βp[},

such that the lengths of the intervals of the partition are less than or
equal to sup(α, 1 − α). Then the frequencies of factors of length n of
the sequence u are equal to the lengths of the intervals bounded by the
points
 {k(1 − α) + βi}, for 0 ≤ k ≤ n − 1, 0 ≤ i ≤ p − 1.

In particular, if the partition is equal to {[0, 1 − α[, [1 − α, 1[}, i.e.,
if u is a Sturmian sequence, the intervals I(w1, . . . , wn) are exactly the
(n + 1) intervals bounded by the points

0, {(1 − α)}, . . . , {(n(1 − α)}.

Therefore there are exactly n+1 factors of length n and the complexity
of a Sturmian sequence satisﬁes p(n) = n+1, for every n. Furthermore,

7

the lengths of these intervals are equal to the frequencies of factors of
length n.
In fact, this complexity function characterizes Sturmian sequences.
Indeed, any sequence of complexity p(n) = n + 1, for every n, is a
Sturmian sequence, i.e., there exists α irrational in ]0, 1[ and x such
that this sequence is the coding of the orbit of x under the rotation
by angle α with respect either to the partition {[0, 1 − α[, [1 − α, 1[}
or {]0, 1 − α], ]1 − α, 1]} (see [40]) (the coding of the orbit of α is
called the characteristic sequence of α). Note that a sequence whose
complexity satisﬁes p(n) ≤ n, for some n, is ultimately periodic (see
[19] and [39]). Sturmian sequences thus have the minimal complexity
among sequences not ultimately periodic. Sturmian sequences are also
characterized by the following properties.

• Sturmian sequences are exactly the non-ultimately periodic bal-
anced sequences over a two-letter alphabet. A sequence is bal-
anced if the diﬀerence between the number of occurrences of a
letter in any two factors of the same length is bounded by one in
absolute value.

• Sturmian sequences are codings of trajectories of irrational initial
slope in a square billiard obtained by coding horizontal sides by
the letter 0 and vertical sides by the letter 1.

In the general case of a coding of an irrational rotation, the complexity
has the form p(n) = an + b, for n large enough (see Theorem 10 below
and [1], for the whole proof). The converse is not true: every sequence
of ultimately aﬃne complexity is not necessarily obtained as a coding of
rotation. Didier gives in [23] a characterization of codings of rotations.
See also [46], where Rote studies the case of sequences of complexity
p(n) = 2n, for every n. However, if the complexity of a sequence u has
the form p(n) = n + k, for n large enough, then u is the image of a
Sturmian sequence by a morphism, up to a preﬁx of ﬁnite length (see
for instance [22] or [1]).

2.2 The graph of words

The aim of this section is to introduce the Rauzy graph of words of
a sequence, in order to obtain results concerning the frequencies of
factors of this sequence. This follows an idea of Dekking who expressed
the block frequencies for the Fibonacci sequence, by using the graph of
words (see [20] and also [8]). Note that Boshernitzan also introduces
in [8] a graph for interval exchange maps (homeomorphic to the Rauzy
graph of words) in order to prove Theorem 3, which can be seen as a
result on frequencies.
 8

Let us note that precise knowledge of the frequencies of a sequence
with values in a ﬁnite alphabet A allows a precise description of the
measure associated with the dynamical system (O(u), T ): T denotes
here the one-sided shift which associates to a sequence (un)n∈IN the
sequence (un+1)n∈IN and O(u) is the orbit closure under the shift T
of the sequence u in AIN, equipped with the product of the discrete
topologies (it is easily seen that O(u) is the set of sequences of factors
belonging to the set of factors of u). Indeed, we deﬁne a probability
measure µ on the Borel sets of O(u) as follows: the measure µ is the
unique T -invariant measure deﬁned by assigning to each cylinder [w]
corresponding to the sequences of O(u) of preﬁx w, the frequency of
w, for any ﬁnite block w with letters from A. Let us note that a dy-
namical system obtained via a coding of irrational rotation is uniquely
ergodic, i.e., there exists a unique T -invariant probability measure on
this dynamical system, which is thus determined by the block frequen-
cies.
The Rauzy graph Γn of words of length n of a sequence with values
in a ﬁnite alphabet is an oriented graph (see, for instance, [41]), which is
a subgraph of the de Bruijn graph of words. Its vertices are the factors
of length n of the sequence and the edges are deﬁned as follows: there is
an edge from U to V if V follows U in the sequence, i.e., more precisely,
if there exists a word W and two letters x and y such that U = xW ,
V = W y and xW y is a factor of the sequence (such an edge is labelled
by xW y). Thus there are p(n + 1) edges and p(n) vertices, where p(n)
denotes the complexity function. A sequence is said to be recurrent
if every factor appears at least twice, or equivalently if every factor
appears an inﬁnite number of times in this sequence. For instance,
codings of rotations are recurrent. Note that the Rauzy graphs of words
of a sequence are always connected; furthermore, they are strongly
connected if and only if this sequence is recurrent.
If B is a factor, then a letter x such that Bx (respectively xB) is
also a factor is called right extension (respectively left extension). Let
U be a vertex of the graph. Denote by U + the number of edges of
Γn with origin U and U − the number of edges of Γn which end vertex
U . In other words, U + (respectively U −) counts the number of right
(respectively left) extensions of U . Note that

p(n + 1) − p(n) = ∑

U∈V (Γn)(U + − 1) = ∑

U∈V (Γn)(U − − 1),

where V (Γn) is the vertex set of Γn.
In this section we restrict ourselves to sequences with values in a
ﬁnite alphabet, for which the frequencies exist. Note that the function
which associates to an edge labelled by xW y the frequency of the

9

factor xW y is a ﬂow. Indeed, it satisﬁes Kirchhoﬀ’s current law: the
total current ﬂowing into each vertex is equal to the total current
leaving the vertex. This common value is equal to the frequency of the
word corresponding to this vertex. Let us see how to deduce, from the
topology of a graph of words, information on the number of frequencies
for factors of given length. We will use the following obvious result.

Lemma 2 Let U and V be two vertices joined by an edge such that
U + = 1 and V − = 1. Then the two factors U and V have the same
frequency.

A branch of the graph Γn is a maximal directed path of consecutive
vertices (U1, . . . , Um) (possibly m = 1), satisfying

U +
i = 1, for i < m, U −
i = 1, for i > 1.

Therefore, the vertices of a branch have the same frequency and the
number of frequencies of factors of given length is bounded by the
number of branches of the corresponding graph, as expressed below
(for a proof of this result due to Boshernitzan, see [8]).

Theorem 6 For a recurrent sequence of complexity function (p(n)),
the frequencies of factors of given length, say n, take at most 3(p(n +
1) − p(n)) values.

Remark In fact, on can prove the following: the frequencies of fac-
tors of length n take at most p(n + 1) − p(n) + rn + ln values, where rn
(respectively ln) denotes the number of factors having more than one
right (respectively left) extension.

We deduce from this theorem that if p(n + 1) − p(n) is uniformly
bounded with n, the frequencies of factors of given length take a ﬁnite
number of values. Indeed, using a theorem of Cassaigne quoted below
(see [10]), we can easily state the following corollary.

Theorem 7 If the complexity p(n) of a sequence with values in a ﬁnite
alphabet is sub-aﬃne then p(n + 1) − p(n) is bounded.

Corollary 1 If a sequence over a ﬁnite alphabet has a sub-aﬃne com-
plexity, then the frequencies of its factors of given length take a ﬁnite
number of values.

Examples of sequences with sub-aﬃne complexity function include the
ﬁxed point of a uniform substitution (i.e., of a substitution such that
the images of the letters have the same length), the coding of a rotation
or the coding of the orbit of a point under an interval exchange map
with respect to the intervals of the interval exchange map.

10

2.3 Frequencies of factors of Sturmian sequences

In particular, in the Sturmian case (p(n) = n + 1, for every integer n),
Theorem 6 implies the following result (see [3]).

Theorem 8 The frequencies of factors of given length of a Sturmian
sequence take at most three values.

Consider a Sturmian sequence of angle α. We have seen in Section 2.1
that the frequency of a factor w1 . . . wn of u is equal to the length of
the interval
 I(w1, . . . , wn) =
 n−1⋂

j=0 R−j(Iwj+1 ),

and that these sets I(w1, . . . , wn) are exactly the intervals bounded by
the points 0, {1 − α}, . . . , {n(1 − α)}.

We deduce from Theorem 8 that the lengths of the intervals
I(w1, . . . , wn), and thus the lengths of the intervals obtained by placing
the points 0, {1 − α}, . . . , {n(1 − α)} on the unit circle, take at most
three values. Hence Theorem 8 is equivalent to the three distance
theorem and provides a combinatorial proof of this result.

Remarks In fact this point of view, and more precisely the study
of the evolution of the graphs of words with respect to the length n of
the factors, allows us to give a proof of the most complete version of
the three distance theorem as given in [53] (for more details, the reader
is referred to [3]).

3 The three distance theorem

The three distance theorem was initially conjectured by Steinhaus, ﬁrst
proved V. T. S´os (see [53] and also [52]), and then by ´Swierczkowski
[56], Sur´anyi [55], Slater [51], Halton [31]. More recent proofs have also
been given by Van Ravenstein [44] and Langevin [35]. A survey of the
diﬀerent approaches used by these authors is to be found in [44, 51, 35].
In the literature this theorem is called the Steinhaus theorem, the three
length, three gap or the three step theorem. In order to avoid any
ambiguity, we will always call it the three distance theorem, reserving
the name three gap for the theorem introduced in the next section.

Three distance theorem Let 0 < α < 1 be an irrational number
and n a positive integer. The points {iα}, for 0 ≤ i ≤ n, partition the
unit circle into n + 1 intervals, the lengths of which take at most three
values, one being the sum of the other two.

11

More precisely, let ( pk
qk )k∈IN and (ck)k∈IN be the sequences of con-
vergents and partial quotients associated to α in its continued frac-
tion expansion (if α = [0, c1, c2, . . .], then pn
qn = [0, c1, . . . , cn]). Let
ηk = (−1)
k(qkα − pk). Let n be a positive integer. There exists a
unique expression for n of the form

n = mqk + qk−1 + r,

with 1 ≤ m ≤ ck+1 and 0 ≤ r < qk. Then, the circle is divided by the
points 0, {α}, {2α}, . . . , {nα} into n + 1 intervals which satisfy:

• n + 1 − qk of them have length ηk (which is the largest of the three
lengths),

• r + 1 have length ηk−1 − mηk,

• qk − (r + 1) have length ηk−1 − (m − 1)ηk.

Remarks

• One can reformulate this result in terms of n-Farey points. Let
us recall that an n-Farey point is a rational element p
q of [0, 1]
such that p ≥ 0, 1 ≤ q ≤ n and p, q are coprime (see [32] for
instance). Note that the two successive n-Farey points, say p
(1)

q(1)

and p
(2)

q(2) , satisfying p
(1)

q(1) < α < p
(2)

q(2) are pk
qk and mpk+pk−1
mqk+qk−1 , with
the above notation. The three distance theorem states that the
lengths of the intervals belong to the set

{p(2) − αq(2), αq(1) − p(1), α(q(1) − q(2)) + p(2) − p(1)}.

• As α is irrational, the three lengths are distinct. The third length
in the above theorem, which is the largest since it is the sum of
the two others, appears if and only if

n ̸= q(1) + q(2) − 1 = (m + 1)qk + qk−1 − 1.

Thus there are inﬁnitely many integers n for which there are only
two lengths. The other two lengths do always appear.

• The structure and the transformation rules for the partitioning in
two-length intervals are studied in details in [44]. Furthermore,
in [45] van Ravenstein, Winley and Tognetti prove the follow-
ing: for α having as sequence of partial quotients the constant
sequence aaaa · · ·, label by large and small the lengths of inter-
vals of the partition {iα}, for 0 ≤ i ≤ qn + qn−1 − 1, where qn
is the denominator of a reduced convergent of α (there are only
two lengths in this case); this binary ﬁnite sequence of lengths is

12

a preﬁx after a permutation of the characteristic sequence of α
(i.e., the Sturmian coding of the orbit of α). For a precise study
of the limit points of these ﬁnite binary sequences (coresponding
to the two-length case), see [48].

• In the two-length case, it is easily seen that the largest length
is less than or equal to twice the second one. In [14] (see also
[15, 16]) Chevallier extends this result to the two-dimensional
torus TT2, by studying the notion of best approximation.

• The point {(n + 1)α} belongs to an interval of largest length in
the partition of the unit circle by the points {iα}, for 0 ≤ i ≤ n.

• The three distance theorem is a geometric illustration of the prop-
erties of good approximation of the n-Farey points. Indeed, the
two intervals containing 0 are of distinct lengths and their lengths
are the two smallest. We thus have

αq(1) − p(1) = inf{kα, for 0 ≤ k ≤ n}

and p(2) − αq(2) = 1 − sup{kα, for 0 ≤ k ≤ n}.

• For a deeper study of the rational case, the reader is referred for
instance to [51].

4 The three gap theorem

The following theorem, called the three gap theorem, is in some sense
the dual of the three distance theorem. This theorem was ﬁrst proved
by Slater (see [49] and see also [50, 51]), in the early ﬁfties, whereas
the ﬁrst proofs of the three distance theorem date back to the late
ﬁfties. For other proofs of the three-gap theorem, see also [25], and
more recently, [58] and [35].
The formulation of the three gap theorem quoted below is due to
Slater. Following the notation of [51], let ki be the sequence of integers
k satisfying kα < β. Then any diﬀerence ki+1 − ki is called a gap.
Moreover, the frequency of a gap is deﬁned as its frequency in the
sequence of the successive gaps (ki+1 − ki)i∈IN.

Three gap theorem Let α be an irrational number in ]0, 1[ and
let β ∈ ]0, 1/2[. The gaps between the successive integers j such that
{αj} < β take at most three values, one being the sum of the other
two.
More precisely, let ( pk
qk )k∈IN and (ck)k∈IN be the sequences of the
convergents and partial quotients associated to α in its continued frac-
tion expansion. Let ηk = (−1)
k(qkα − pk). There exists a unique

13

expression for β of the form

β = mηk + ηk+1 + ψ,

with k ≥ 0, 0 < ψ ≤ ηk, and if k = 0, 1 ≤ m ≤ c1 − 1, otherwise,
1 ≤ m ≤ ck+1. Then, the gaps between two successive j such that
{jα} ∈ [0, β[ satisfy the following:

• the gap qk has frequency (m − 1)ηk + ηk+1 + ψ,

• the gap qk+1 − mqk has frequency ψ,

• the gap qk+1 − (m − 1)qk has frequency ηk − ψ.

Remarks

• Suppose that α is an irrational number. By density of the se-
quence ({nα})n∈IN, this theorem still holds when considering the
gaps between the successive integers k such that {αk} ∈ I, where
I denotes any interval of the unit circle of length β.

• Furthermore, the third gap, which is the largest, can have fre-
quency 0, when ηk = ψ, with the above notation. This means
that this gap does not appear at all, as a consequence of the
uniform distribution of the sequence ({nα})n∈IN in the circle.

• The other two gaps do always appear (inﬁnitely often, in fact,
because of their positive frequencies) and are shown to be equal
to the smallest positive integers l1 and l2 such that {l1α} < β
and {l2α} > 1 − β (see [51]).

• The study of the rational case proves the equivalence between
the three distance and the three gap theorems, as observed by
Slater [51] in the case of an open interval and by Langevin, for
any interval, in [35].

4.1 Connectedness index

Let u = (un)n∈IN be a coding of a rotation by irrational angle 0 < α < 1
with respect to the partition

P = {[β0, β1[, [β1, β2[, . . . , [βp−1, βp[}.

We have seen in Section 2.1 that the sets
I(w1, . . . , wn) = ⋂n−1
j=0 R−j(Iwj+1 ), where Ik = [βk, βk+1[, for 0 ≤ j ≤
p − 1, are connected except for w1 . . . wn of the form an
K, where K
denotes the index of the interval of P (if such an interval exists) of
length greater than sup(α, 1 − α).
Let us suppose that there exists an interval of P of length L greater
than 1 − α and index K, say. We deduce from the three gap theorem

14

that the set of integers n such that an
K is a factor of the sequence u is
bounded. More precisely, let us deﬁne n(1) as the largest integer n such
that an
K is a factor of the sequence u. We will call the integer n(1) the
index of connectedness of the sequence u. (If every interval of P has
length smaller than or equal to sup(α, 1 − α) then the connectedness
index of u is equal to 1.) The three gap theorem enables us to give an
exact expression for the connectedness index. Indeed n(1) + 1 is the
largest gap between the consecutive values of k for which 0 < {kα} <
1 − L. We thus have the following.

Theorem 9 Let u = (un)n∈IN be a coding of the rotation by irra-
tional angle α. Suppose that there exists an interval of P of length
L > sup(α, 1 − α). Let ( pk
qk )k∈IN and (ck)k∈IN be the sequences of con-
vergents and partial quotients associated to α in its continued fraction
expansion. Let ηk = (−1)
k(qkα − pk). Write

1 − L = mηk + ηk+1 + ψ,

with k ≥ 1, 0 < ψ ≤ ηk and 1 ≤ m ≤ ck+1. The connectedness index
n(1) of the sequence u satisﬁes

n(1) = qk+1 − (m − 1)qk − 1, if ψ ̸= ηk,

n(1) = qk+1 − mqk − 1, if ψ = ηk and m < ck+1,

n(1) = qk − 1, if ψ = ηk and m = ck+1.

4.2 Applications

Precise knowledge of the connectedness index is useful, as shown by
the following. Indeed Lemma 1 can be rephrased as follows.

Lemma 3 Let u be a coding of an irrational rotation on the unit cir-
cle with respect to the partition {[β0, β1[, [β1, β2[, . . . , [βp−1, βp[}. The
frequencies of factors of u of length n ≥ n(1), where n(1) denotes the
connectedness index, are equal to the lengths of the intervals bounded
by the points

{k(1 − α) + βi}, for 0 ≤ k ≤ n − 1, 0 ≤ i ≤ p − 1.

The complexity of a coding on p letters of an irrational rotation
ultimately has the form p(n) = an + b, where a ≤ p, and depends
on the algebraic relations between the angle and the lengths of the
intervals of the coding. More precisely, we have the following theorem
proved in [1].
 15

Theorem 10 Let u = (un)n∈IN be a coding of the irrational rotation
R of irrational angle α with respect to the partition

P = {[β0, β1[, [β1, β2[, . . . , [βp−1, βp[}.

Let (kn)n∈IN be the sequence deﬁned by

k0 = p = card(F ),

kn = card{βi ∈ F ; ∀k ∈ [1 . . . n], R−k(βi) /∈ F }.

Let a be the limit of this sequence, n(2) the smallest index such that
kn = a, and let
 b =
 n
(2)−1∑

i=0 (ki − a).

Let n(1) denote the connectedness index of u.
If n ≥ max(n(1), n(2)), then the complexity of the sequence u satis-
ﬁes p(n) = an + b.

Remarks

• Note that if 1, α, β1, . . . , βp are rationally independent, then
n(2) = 0, b = 0 and a = p.

• Theorem 10 answers the question of the existence of sequences
of ultimately aﬃne complexity (for more details, the reader is
referred to [1], see also the result of Cassaigne in [11]).

4.3 Beatty sequences

The connections between the three gap theorem and the Beatty se-
quences have been investigated by Fraenkel and Holzman in [26]. Let
us recall that a Beatty sequence is a sequence u(α, ρ) = (un)n∈IN of the
form un = ⌊αn + ρ⌋, where α and ρ are real numbers such that α ≥ 1.
The number α is called the modulus and ρ is called the residue or inter-
cept. For an impressive bibliography on the subject, we refer the reader
to [27] and [54]. Fraenkel and Holzman have noticed in [26] that the
three gap theorem answers the question of the gaps in the intersection
of a Beatty sequence and an arithmetical sequence (an + c)n∈IN, for
a a positive integer and c an integer. This result has been obtained
independently by Wolﬀ and Pitman in [58]. By intersection of the two

16

Beatty sequences s = (sn)n∈IN and t = (tn)n∈IN, we mean the strictly
increasing sequence u deﬁned as:

{un, n ∈ IN} = {u, ∃k, l ∈ IN such that u = sk = tl}.

Hence a gap in the intersection denotes the diﬀerence between two
distinct elements of the intersection.
Note that Beatty sequences and Sturmian sequences are related: let
u be a Beatty sequence of modulus α and residue ρ; the characteristic
sequence (vn)n∈IN of u deﬁned as

vn = 1 if and only if there exists m such that n = ⌊αm + ρ⌋

is the Sturmian sequence obtained as the coding of the orbit of −ρ/α
under the rotation by angle 1/α, with respect to the partition {]0, 1 −
1/α], ]1 − 1/α, 1]}. Indeed, if n = ⌊αm + ρ⌋, then ⌈1/α(n + 1) − ρ/α⌉ =
m + 1 = 1 + ⌈n/α − ρ/α⌉, and if ⌊αm + ρ⌋ < n < ⌊α(m + 1) + ρ⌋, then
⌈1/α(n + 1) − ρ/α⌉ = ⌈n/α − ρ/α⌉.

5 The recurrence function

Let us deduce now from the three distance and three gap theorems a
simple proof of the following result originally due to Morse and Hed-
lund concerning the recurrence function of a Sturmian sequence (see
[40]).
Recall that a sequence u is called minimal or uniformly recurrent
if every factor of u appears inﬁnitely often and with bounded gaps or,
equivalently, if for any integer n, there exists an integer m such that
every factor of u of length m contains every factor of u of length n.
Note that it is equivalent (see [30]) to the minimality of the dynamical
system (O(u), T ), i.e., the orbit of every element of O(u) is dense, or
equivalently every sequence in the orbit closure of u has the same set
of factors as u.
The recurrence function ϕ of a minimal sequence u is deﬁned by:

ϕ(n) = min{m ∈ IN such that ∀B ∈ Lm, ∀A ∈ Ln, A is a factor of B}

where Ln denotes the set of factors of u of length n, i.e., ϕ(n) is the size
of the smallest window that contains all factors of length n whatever
its position on the sequence.

Theorem 11 Let u be a Sturmian sequence with angle α. Let (qk)k∈IN
denote the sequence of denominators of the convergents of the continued
fraction expansion of α. The recurrence function ϕ of this sequence
satisﬁes for any non zero integer n:

ϕ(n) = n − 1 + qk + qk−1, where qk−1 ≤ n < qk.

17

Proof of Theorem 11 Let u ∈ {0, 1}IN be a Sturmian sequence.
There exist a real number x and an irrational number α in ]0, 1[ such
that un = 0 ⇔ {x+ nα} ∈ I0, with I0 = [0, α[ or I0 =]0, α] (see Section
2.1). Let I1 = [α, 1[ (respectively ]α, 1]) if I0 = [0, α[ (respectively
I0 =]0, α]). Let us denote by R the rotation of the circle by angle α.
Assume we are given a positive integer n. We have seen in Section 2.1
that the word w1w2 . . . wn deﬁned on {0, 1} appears in u if and only if

I(w1, . . . , wn) =
 n−1⋂

j=0 R−j(Iwj+1 ) ̸= ∅.

We deduce from this that every Sturmian sequence of angle α has the
same factors as u and thus belongs to the orbit closure of u. Conversely,
each sequence of the orbit closure of u is a Sturmian sequence of angle
α. Hence the closed orbit of any Sturmian sequence is equal to the set of
all Sturmian sequences of the same angle. This implies the minimality
of any Sturmian sequence and that Sturmian sequences of the same
angle have the same recurrence function; hence we can suppose here
that x = 0.
Theorem 11 can easily been deduced from the following two lem-
mata. We omit the proof of Lemma 5 which is straightforward.

Lemma 4 Let δn be the smallest length of the nonempty intervals
I(w1, . . . , wn), where w1, . . . , wn belong to {0, 1}. Let ln be the greatest
gap between the succesive integers k such that {kα} ∈ [0, δn[. We have

ϕ(n) = n − 1 + ln.

Lemma 5 Let (qk)k∈IN denote the sequence of denominators of the
convergents of the continued fraction expansion of α. Let k be an
integer such that qk−1 ≤ n < qk. Then we have

δn = ηk−1 and ln = qk + qk−1.

Proof of Lemma 4 A set of points is said to visit an interval if one
of these points belongs to this interval. By deﬁnition of ln, every set of
ln consecutive points of the sequence ({kα})k∈IN visits every interval of
length δn (see Remark 4). Therefore they visit every nonempty interval
of the form I(w1, . . . , wn), by deﬁnition of δn. Let B be a factor of u of
length n − 1 + ln; there exists an integer K such that B corresponds to
the n−1+ln consecutive points {Kα}, . . . , {(K +n−1+ln −1)α}. The
set of the ln ﬁrst points of this sequence of points visits every interval
of the form I(w1, . . . , wn), thus B contains every factor of u of length
n. This implies that ϕ(n) ≤ n − 1 + ln.

18

By deﬁnition of ln and by density of ({kα})k∈IN, there exists a
sequence of ln − 1 points of the sequence ({kα})k∈IN which do not visit
an interval of the form I(w1, . . . , wn) of length δn; therefore, there
exists a factor of u of length ln − 2 + n which does not contain the
factor w1 . . . wn. This shows that ϕ(n) ≥ n − 1 + ln. The lemma is
thus proved.

Remark Note that in the case of the Fibonacci sequence (α =
√
5−1
2 ), the recurrence function satisﬁes, for Fk−1 < n ≤ Fk,

ϕ(n) = n − 1 + Fk+1,

where (Fn)n∈IN denotes the Fibonacci sequence Fn+1 = Fn + Fn−1,
with F0 = 1 and F1 = 2.

This result is extended in [13] to the ﬁxed point of the substitution
σ introduced by Rauzy which generalizes the Fibonacci substitution
and deﬁned by σ(0) = 01, σ(1) = 02, σ(2) = 0.

Theorem 12 Let Tn denote the so-called Tribonacci sequence deﬁned
as follows: Tk+3 = Tk+2 + Tk+1 + Tk, with T0 = 0, T1 = 0, T1 = 1. The
recurrence function ϕ of the ﬁxed point beginning with 0 of the Rauzy
substitution satisﬁes for any positive integer n:

ϕ(n) = n − 1 + Tk+6, where
 k+1∑

0 Ti < n ≤
 k+2∑

0 Ti.

6 Higher dimensional generalisations

6.1 Two-dimensional generalisations and Beatty
sequences

Let us consider now some two-dimensional versions of the three dis-
tance and three gap theorems. Such generalisations were introduced by
Fraenkel and Holzman in [26] in order to give an upper bound for the
number of gaps in the intersection of two Beatty sequences. They ﬁrst
reduce this problem to a two-dimensional version of the three distance
theorem, conjectured by Simpson and Holzman and proved by Geelen
and Simpson (see [29]). Then they deduce from this theorem a bound
for the number of gaps in the intersection of two Beatty sequences,
when at least one of the moduli is rational.
Let us ﬁrst give the two-dimensional version of the three gap the-
orem introduced by Fraenkel and Holzman. We will use the same
notation as in [26]: for any pair of real numbers (x, y), {(x, y)} means

19

the equivalence class of (x, y) mod ZZ2, i.e., {(x, y)} belongs to the
torus TT2.

Theorem 13 Let α1, α2, β1, β2, µ1 and µ2 be real numbers in [0, 1[.
The gaps between the successive values of the integers n such that the
following points of the torus TT2

{(nα1, nα2)}

belong to the rectangle

R = {{(x, y)}; µ1 − β1 < x ≤ µ1, µ2 − β2 < y ≤ µ2}

take a ﬁnite number of values which depend only on α1, α2, β1 and β2.
Furthermore, if at least one of the two angles α1 and α2 is rational,
then the number of gaps is bounded by q + 3, where q is the minimum
of the denominators of α1 and α2 in lowest terms (the denominator of
an irrational number is considered as +∞).

Let us state now the two-dimensional version of the three distance
theorem proved in [29] by Geelen and Simpson.

Theorem 14 Assume we are given two real numbers α1, α2 and two
positive integers n1, n2. The set of points

{iα1 + jα2 + ρ, 0 ≤ i ≤ n1 − 1, 0 ≤ j ≤ n2 − 1}

partitions the unit circle into intervals having at most min{n1, n2} + 3
lengths.

Note that the bound min{n1, n2} + 3 is not the best possible when n1
or n2 = 1. Indeed, in this case, the statement reduces to the three
distance theorem. For a discussion on the achievability of the bound,
the reader is referred to [29].

Fraenkel and Holzman have proved in [26] that Theorems 13 and
14 together answer the question of the intersection of two Beatty se-
quences, when at least one modulus is rational. We deﬁne a gap in
the intersection of two Beatty sequences to be a diﬀerence between
two successive elements of the intersection, and an index-gap to be the
diﬀerence between the two corresponding indices in the same Beatty
sequence.

Theorem 15 Let (⌊nα1+ρ1⌋)n∈IN and (⌊nα2+ρ2⌋)n∈IN be two Beatty
sequences, with at least one of the two moduli α1 and α2 rational. Let q
denote the minimum of the denominators of α1 and α2 in lowest terms
(the denominator of an irrational number is considered as +∞). The
number of gaps and index-gaps in the intersection is bounded by q + 3,
if q ≥ 2, and bounded by 3 otherwise.

20

Fraenkel and Holzman show furthermore that this bound is achievable
and that the number of gaps can be made arbitrarily large, when at
least one of the moduli is rational.

6.2 Combinatorial applications

Now let us review some applications of Theorems 13 and 14. For
instance we can deduce the following result for the intersection of two
Sturmian sequences.

Theorem 16 Let s = (sn)n∈IN and t = (tn)n∈IN be two Sturmian
sequences. The number of gaps between the successive integers n such
that sn = tn is ﬁnite.

Proof Let s = (sn)n∈IN and t = (tn)n∈IN be two Sturmian sequences
of angles α and β, with corresponding partitions {I0, I1} and {J0, J1}.
The gaps between the integers n such that the points {(nα, nβ)} in TT2

belong to the rectangle I0×J0 (respectively I1×J1) take a ﬁnite number
of values, hence so do the gaps between the successive integers n such
that the points {(nα, nβ)} in TT2 belong to the set I0 × J0 ∪ I1 × J1.

We also deduce from Theorem 14 and Lemma 3 the following.

Theorem 17 Let u be a coding of the irrational rotation by angle
0 < α < 1 with respect to a partition into d intervals of length 1/d.
The frequencies of factors of u of length n ≥ sup{n(1), d} take at most
d + 3 values, where n(1) denotes the connectedness index.

Proof This result is a direct application of Lemma 3 and Theorem
14. Indeed, the intervals I(w1, . . . , wn) (corresponding to the factors
w1 . . . wn of length n) are bounded by the points {i(1 − α) + j/d, 0 ≤
i ≤ n − 1, 0 ≤ j ≤ d − 1}.

Vuillon has introduced in [57] two-dimensional generalisations of
Sturmian sequences obtained by considering the approximation of a
plane of irrational normal by square faces oriented along the three
coordinates planes. Theorem 14 can also be applied to give an upper
bound for the number of frequencies of blocks of a given size for such
double sequences (see [4]).
We will give in Section 7 a direct combinatorial proof of Theorem
14 in the particular case min{n1, n2} = 2, and give an interpretation
in terms of frequencies of binary codings: the frequencies of the factors
of given length of a coding of an irrational rotation with respect to a
partition in two intervals take ultimately at most 5 values.

21

6.3 The 3d distance theorem

Let us consider another generalisation of the three distance theorem,
known as the 3d distance theorem. This result, conjectured by Graham
(see [17] and [34]), was ﬁrst proved by Chung and Graham in [18] and
secondly by Liang who gave a very nice proof in [37]. Geelen and
Simpson remark in [29] that their proof uses ideas from Liang’s proof.

The 3d distance theorem Assume we are given 0 < α < 1 irra-
tional, γ1,. . ., γd real numbers and n1, . . . , nd positive integers. The
points {nα + γi}, for 0 ≤ n < ni and 1 ≤ i ≤ d, partition the unit
circle into at most n1 + · · · + nd intervals, having at most 3d diﬀerent
lengths.

We will give a combinatorial proof of this result in Section 8 and express
the coresponding result for frequencies of codings of rotations, i.e., that
the frequencies of the factors of given length of a coding of a rotation
by the unit circle under a partition in d intervals take ultimately at
most 3d values.

6.4 Other generalisations

Slater has studied in [50] the following generalisation of the three
gap theorem, which should be compared with Theorem 13: there is
a bounded number of gaps between the successive values of the in-
tegers n such that {n(η1, . . . , ηd)} ∈ C, where C is a closed convex
region on the d-dimensional torus and where 1, η1 . . . , ηd are rationally
independent. However, Fraenkel and Holzman prove Theorem 13 even
in the case where α1, α2 and 1 are rationally independent.
Chevallier studies in [16] a d-generalization of the three distance
theorem to TTd, where intervals are replaced by Vorono¨ı cells: the
number of Vorono¨ı cells (up to isometries) is shown to be connected to
the number of sides of a Vorono¨ı cell. The notion of continued fraction
expansion is generalized by properties of best approximation.
Finally, note the unsolved problems quoted in [29] concerning fur-
ther generalisations of the three distance theorem. For instance, an
upper bound for the number of distinct lengths in the partition of the
unit circle by the points k1α1 + k2α2 + · · · + kdαd, for ki ≤ ni − 1 and
1 ≤ i ≤ d is conjectured to be of the form cd + ∏d−1
i=1 ni, where cd is a
constant independent of n1, · · · , nd.

22

7 Frequencies of factors for binary codings
of rotations

We will prove in this section the following result, which corresponds to
the case min{n1, n2} = 2 in Theorem 14. The idea of using a reﬂection
of the unit circle can also be found in the original proof in [29].

Theorem 18 Let α be an irrational number in ]0, 1[, β ̸= 0 a real
number and n a non zero integer. The set of points {0}, {β}, {α},
{β + α}, . . . , {nα}, {β + nα} divides the circle into a ﬁnite number of
intervals, whose lengths take at most ﬁve values.

7.1 A combinatorial proof

We will prove Theorem 18 by introducing a coding of the rotation by
angle α with respect to the intervals of the unit circle bounded by the
points {0}, {β}, {α}, {β + α}, · · · , {nα}, {β + nα}.
Let α be an irrational number, β a non-zero real number and n an
integer. Let I1, · · · , Ip denote the intervals of the unit circle bounded by
the points {0}, {β}, {α}, {β+α}, · · · , {nα}, {β+nα}. Let u = (un)n∈IN
be the sequence deﬁned on the alphabet Σ = {a1, . . . , ap} as the coding
of the orbit of 0 under the rotation R of angle α under the partition
{I1, · · · , Ip}: un = ak ⇔ {nα} ∈ Ik.

The frequency of the letter ak in the sequence u is equal to the length
of the interval Ik, by uniform distribution of the sequence ({nα})n∈IN.
We must now prove that the frequencies of the letters of u take at
most ﬁve values Let us consider the graph Γ1 of words of u of length
1. There is one edge from ak to ak′ if Ik′ is the image of Ik by the
rotation R or if Ik′ contains {−α} or {−α + β}. Therefore the graph
Γ1 contains p vertices (one for each letter) and p + 2 edges: indeed,
every vertex has only one leaving edge, except the ones associated with
the intervals containing {−α} or {n − α + β}, which have two leaving
edges (if both of these points belong to the same interval Ik, then ak
has three leaving edges and all the other intervals have only one edge).
In other words, we have p(1) = p and p(2) = p + 2. As in the proof
of Theorem 6, this implies that there are at most 6 branches in Γ1:
indeed, each branch starts with a vertex with more than one entering
edge (this provides at most two branches) or just after a vertex with
at least two leaving edges (at most four branches are of this kind). We
deduce from this that the frequencies of the letters in u take at most
6 values. Let us prove that at least two branches of Γ1 have the same
frequency, which will complete the proof.

23

Let s denote the reﬂection of the circle deﬁned by s : x → {β +
nα − x}. This reﬂection leaves invariant the endpoints of the intervals
I1, · · · , Ip and thus induces a permutation σ of the interiors of the
intervals Ik, which can also be seen as a permutation of Σ. The length
of Ik is equal to the length of Iσ(k) = s(Ik). The frequency of the letter
ak is thus equal to the frequency of the letter σ(ak). Note that if aiaj is
a factor of u, then σ(aj)σ(ai) is also a factor. We deduce from this that
if there is an edge in Γ1 from ai to aj, then there is also an edge from
σ(aj) to σ(ai), or in other words, that Γ1 is invariant by the following
action of σ: the image of the vertex associated with the letter a is equal
to the vertex associated with σ(a) and the image of the edge a → b is
the edge σ(b) → σ(a), i.e., each letter is replaced by its image and the
direction of every edge is changed. Furthermore, the image of a branch
is a branch. Let us prove that at most four branches of the graph Γ1
are invariant by σ. Let B = U1 → U2 → . . . → Uq be an invariant
branch of the graph. We have B = σ(B) = σ(Uq) → . . . → σ(U1). We
thus get σ(Uk) = Uq+1−k.

• Suppose that there exists i such that Ui = σ(Ui). Therefore
the interval Ii must contain a ﬁxed point for s. Since there are
only two such ﬁxed points, at most two branches can satisfy this
property.

• Let us suppose that Ui ̸= σ(Ui) for each 1 ≤ i ≤ q. We thus
have q even and σ(Uq/2) = Uq/2+1. Let I (respectively I ′) be the
closure of the interval associated with Uq/2 (respectively Uq/2+1).
We thus get s(I) = I ′. Furthermore, I ′ is the image of I by the
rotation R, because of the edge Uq/2 → Uq/2 + 1. This implies
that I ′ contains a ﬁxed point of the symmetry s ◦ R−1, which has
at most two ﬁxed points. Hence, at most two branches are of this
kind.

We have proved that at most four basic paths can be their own image by
σ. Therefore, there exist among the six branches at least two diﬀerent
branches, say A and B, such that B = σ(A). Thus A and B have
the same frequency, which implies that there are at most ﬁve possible
frequencies for the letters of u.

7.2 Application to binary codings

A more natural coding of the rotation R would have been with re-
spect to the partition [0, β[, [β, 1[. The points {0}, {β}, {α}, {β +
α}, . . . , {nα}, {β + nα} are the endpoints of the sets I(w1, . . . , wn),
following the notation of Section 2. But these sets might not be con-
nected. Thus the frequencies of factors of length n are the sums of the

24

lengths of the connected components of the sets I(w1, . . . , wn). De-
spite this disandvantage, this coding allows us to deduce the following
result from Lemma 3.

Theorem 19 Let u be a coding of an irrational rotation with respect
to the partition into two intervals {[0, β[, [β, 1[}, where 0 < β < 1. Let
n(1) denote the connectedness index of u. The frequencies of factors of
given length n ≥ n(1) of u take at most 5 values. Furthermore, the set
of factors of u is stable by mirror image, i.e., if the word a1 · · · an is a
factor of the sequence u, then an · · · a1 is also a factor and furthermore,
both words have the same frequency.

Proof It remains to prove the part of this theorem concerning the
stability by mirror image. Assume we are given a ﬁxed positive integer
n. Let sn be the reﬂection of the circle deﬁned by sn : x → {β −
(n − 1)α − x}. We have sn(R−k(Ij )) = R(−n+1+k)(Ij ), for j = 0, 1,
following the previous notation. The image of I(w1, . . . , wn) by sn is
I(wn, · · · , w1); they thus have the same length, which gives the result.

Remark A study of the topology of the graph of words for a bi-
nary coding of an irrational rotation of complexity satisfying ultimately
p(n + 1) − p(n) = 2 can be found in [24] or in [46].

8 The 3d distance theorem

Following the idea of the above proof, let us give a combinatorial proof
of the 3d-distance theorem.

The 3d distance theorem Assume we are given 0 < α < 1 irra-
tional, γ1,. . ., γd real numbers and n1, . . . , nd positive integers. The
points {nα + γi}, for 0 ≤ n < ni and 1 ≤ i ≤ d, partition the unit
circle into at most n1 + · · · + nd intervals, having at most 3d diﬀerent
lengths.

Proof Let us consider a coding of the rotation by angle α under
the left-closed and right-open partition of the unit circle bounded by
all the points of the form {nα + γi}, for 0 ≤ n < ni and 1 ≤ i ≤ d;
let β0, . . . , βp−1 denote these consecutive points. The letter associated
with the interval Ik = [βk, βk+1[ has a unique right extension, except
when Ik contains points of the form {βi − α}. Suppose there are q ≥ 2
pints of this form; the associated letter has q +1 right extensions. Since
there are at most d points of this type, we obtain p(2) − p(1) ≤ d. We
deduce from Theorem 6 that there are at most 3d diﬀerent frequencies

25

for the letters of the coding, i.e., there are at most 3d diﬀerent lengths
for the intervals Ik.

Remark The start and ﬁnish intervals as introduced by Liang in
his proof in [37] correspond exactly to the beginning of the branches in
the graph of words. Indeed, Liang shows that any interval is associated
either with a start point {γi} (i.e., with one extension of a factor having
more than one right extension) or with a ﬁnish point {(ni − 1)α + γi}
(i.e., with a factor having more than one left extension). Counting
the ﬁnish and start points deﬁned in [37] (there are 3d such points) is
equivalent to counting the number of branches in the graph of words.

As in the remark of the previous section, we can consider a cod-
ing of the rotation by irrational angle 1 − α under the partition
{[γ1, γ2[, . . . , [γd, γ1[}. For such a coding, the 3d distance theorem can
be rephrased as follows.

Theorem 20 The frequencies of the factors of given length n ≥ n(1)

of a coding of a rotation by irrational angle under a partition in d
intervals take at most 3d values, where n(1) denotes the connectedness
index.

Acknowledgements We would like to thank Arnoux, Berstel,
Daud´e, Dumont, Liardet and Shallit for their bibliographic help. Fur-
thermore, we are greatly indebted to Allouche for his many useful
comments and to Ferenczi and Jenkinson who read carefully a previ-
ous version of this paper.

References

[1] P. ALESSANDRI Codages de rotations et basses complexit´es, Uni-
versit´e Aix-Marseille II, Th`ese, 1996.

[2] J.-P. ALLOUCHE Sur la complexit´e des suites inﬁnies, Bull. Belg.
Math. Soc. 1 (1994), 133–143.

[3] V. BERTH´E Fr´equences des facteurs des suites sturmiennes, The-
oret. Comput. Sci. 165 (1996), 295–309.

[4] V. BERTH´E, L. VUILLON Tilings and rotations, Pr´etirage 97-19,
Institut de Math´ematiques de Luminy.

[5] V. BERTH´E, N. CHEKHOVA, S. FERENCZI, Covering numbers:
arithmetics and dynamics for rotations and interval exchanges,
Pr´etirage 97-20, Institut de Math´ematiques de Luminy.

26

[6] J. BERSTEL Recent results in Sturmian words, Developments in
language theory II (Magedburg 1995), World Scientiﬁc (96), 13–
24.

[7] G. BESSI, J.-L. NICOLAS Nombres 2-hautement compos´es, J.
Math. Pures Appl. 56 (1977), 307–326.

[8] M. BOSHERNITZAN A condition for minimal interval exchange
maps to be uniquely ergodic, Duke Math. J. 52 (1985), 723–752.

[9] T. C. BROWN Descriptions of the characteristic sequence of an
irrational, Canad. Math. Bull 36 (1993), 15–21.

[10] J. CASSAIGNE Special factors of sequences with linear sub-
word complexity, Developments in language theory II (Magedburg
1995), World Scientiﬁc (96), 25–34.

[11] J. CASSAIGNE Complexit´e et facteurs sp´eciaux, Bull. Belg.
Math. Soc. 4 (1997), 67–88.

[12] N. CHEKHOVA Covering numbers of rotations, Theoret. Com-
put. Sci., to appear.

[13] N. CHEKHOVA, P. HUBERT, A. MESSAOUDI Propri´et´es com-
binatoires, ergodiques et arithm´etiques de la substitution de Tri-
bonacci, preprint.

[14] N. CHEVALLIER Distances dans la suite des multiples d’un point
du tore `a deux dimensions, Acta Arith. 74, 47–59.

[15] N. CHEVALLIER G´eom´etrie des suites de Kronecker,
Manuscripta Math. 94 (1997), 231–241.

[16] N. CHEVALLIER Meilleures approximations d’un ´el´ement du tore
TT2 et g´eom´etrie de la suite des multiples de cet ´el´ement, Acta
Arith. 78 (1996), 19–35.
[17] V. CHV ´ATAL, D. A. KLARNER, D. E. KNUTH Selected combi-
natorial research problems, Stanford CS report 292 (1972).

[18] F. R. K. CHUNG, R. L. GRAHAM On the set of distances de-
termined by the union of arithmetic progressions, Ars Combin. 1
(1976), 57–76.

[19] E. M. COVEN, G. A. HEDLUND Sequences with minimal block
growth, Math. Systems Theory 7 (1973), 138–153.

[20] F. M. DEKKING On the Prouhet-Thue-Morse measure, Acta Uni-
versitatis Carolinae, Mathematica et Physica, 33 (1992), 35–40.

[21] M. DEL´EGLISE Recouvrement optimal du cercle par les multiples
d’un intervalle, Acta Arith. 59 (1991), 21–35.

[22] G. DIDIER Caract´erisation des N -´ecritures et applications `a
l’´etude des suites de complexit´e ultimement n+cste, Theoret. Com-
put. Sci, to appear.
 27

[23] G. DIDIER Combinatoire des codages de rotations, Acta Arith.,
to appear.

[24] S. FERENCZI Les transformations de Chacon : combinatoire,
structure g´eom´etrique, lien avec les syst`emes de complexit´e 2n+1,
Bull. Soc. math. France 123 (1995), 271–292.

[25] K. FLOREK Une remarque sur la r´epartition des nombres nξ
(mod 1), Colloq. Math. Wroclaw 2 (1951), 323–324.

[26] A. S. FRAENKEL, R. HOLZMAN Gap problems for integer part
and fractional part sequences, J. Number Theory 50 (1995), 66–
86.

[27] A. S. FRAENKEL, M. MUSHKIN, U. TASSA Determination of
[nθ] by its sequence of diﬀerences, Canad. Math. Bull. 21 (1978),
441–446.

[28] E. FRIED, V. T. S ´OS A generalisation of the three-distance the-
orem for groups, Algebra Universalis 29 (1992), 136–149.

[29] A. S. GEELEN, R. J. SIMPSON A two dimensional Steinhaus
theorem, Australas. J. Combin. 8 (1993), 169–197.

[30] W. H. GOTSCHALK, G. HEDLUND Topological dynamics,
American Math Soc. Colloq., Public. 36 (1955).

[31] J. H. HALTON The distribution of the sequence {nξ} (n =
0, 1, 2, · · ·), Proc. Cambridge Philos. Soc. 61 (1965), 665–670.

[32] G. H. HARDY et E. M. WRIGHT An introduction to the theory
of numbers, Oxford Science Publications (1979).

[33] S. HARTMAN ¨Uber die Abst¨ande von Punkten nξ auf der Kreis-
peripherie, Ann. Soc. Polon. Math. 25 (1952), 110–114.

[34] D. E. KNUTH The art of computer programming, Vol. 3, Ex.
6.4.10, Addison Wesley, New York, 1973.

[35] M. LANGEVIN Stimulateur cardiaque et suites de Farey, Period.
Math. Hung. 23 (1991), 75–86.

[36] V. LEF`EVRE An algorithm that computes a lower bound on the
distance between a segment and ZZ2, Rapport de recherche LIP
18, 1997.

[37] F. M. LIANG A short proof of the 3d distance theorem, Discrete
Math. 28 (1979), 325–326.

[38] C. MARZEC, J. KAPPRAFF Properties of maximal spacing on
a circle related to phyllotaxis and to the golden mean, J. Theor.
Biol. 103 (1983), 201–226.

[39] M. MORSE, G. A. HEDLUND Symbolic dynamics, Amer. J.
Math. 60 (1938), 815–866.
 28

[40] M. MORSE, G. A. HEDLUND Symbolic dynamics II: Sturmian
trajectories, Amer. J. Math. 62 (1940), 1–42.

[41] G. RAUZY Suites `a termes dans un alphabet ﬁni, S´em. de Th´eorie
des Nombres de Bordeaux (1983), 25-01–25-16.

[42] T. van RAVENSTEIN On the discrepancy of the sequence formed
from multiples of an irrational number, Bull. Austral. Math. Soc.
31 (1985), 329–338.

[43] T. van RAVENSTEIN Optimal spacing of points on a circle, Fi-
bonacci Quart. 27 (1989), 18–24.

[44] T. van RAVENSTEIN The three gap theorem (Steinhaus conjec-
ture), J. Austral. Math. Soc. Ser. A 45 (1988), 360–370.

[45] T. van RAVENSTEIN, G. WINLEY, K. TOGNETTI Character-
istics and the three gap theorem, Fibonacci Quarterly 28 (1990),
204–214.

[46] G. ROTE Sequences with subword complexity 2n, J. Number The-
ory 46 (1994), 196–213.

[47] J. SHALLIT Automaticity IV: Sequences, sets, and diversity, J.
Th´eor. Nombres Bordeaux 8 (1996), 347–367.

[48] A. SIEGEL Th´eor`eme des trois longueurs et suites sturmiennes :
mots d’agencement des longueurs, preprint.

[49] N. B. SLATER The distribution of the integers N for which
{θN } < Φ, Proc. Cambridge Philos. Soc. 46 (1950), 525–534.

[50] N. B. SLATER Distribution problems and physical applications,
Compositio Math. 16 (1964), 176–183.

[51] N. B. SLATER Gaps and steps for the sequence nθ mod 1, Proc.
Cambridge Philos. Soc. 63 (1967), 1115–1123.

[52] V. T. S ´OS On the theory of diophantine approximations I, Acta
Math. Acad. Sci. Hungar. 8 (1957), 461–472.

[53] V. T. S ´OS On the distribution mod 1 of the sequence nα, Ann.
Univ. Sci. Budapest, E¨otv¨os Sect. Math. 1 (1958), 127–134.

[54] K. STOLARSKY Beatty sequences, continued frations, and cer-
tain shift operators, Canad. Math. Bull. 19 (1976), 473–482.

[55] J. SUR ´ANYI ¨Uber die Anordnung der Vielfachen einer reellen
Zahl mod 1, Ann. Univ. Sci. Budapest, E¨otv¨os Sect. Math. 1
(1958), 107–111.

[56] S. ´SWIERCZKOWSKI On successive settings of an arc on the
circumference of a circle, Fund. Math. 46 (1958), 187–189.

[57] L. VUILLON Contribution `a l’´etude des pavages et des surfaces
discr´etis´ees, Theoret. Comput. Sci., to appear.

29

[58] A. WOLFF, J. PITMAN Lattice points in strips, Tech. Rep., Uni-
versity of Adelaide, Australia, 1990.

30
