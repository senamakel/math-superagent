<!-- source: https://www.irif.fr/~berthe/Articles/chili.pdf | converted from PDF -->

SEQUENCES OF LOW COMPLEXITY:
AUTOMATIC AND STURMIAN
SEQUENCES

Val´erie BERTH´E
Institut de Math´ematiques de Luminy
CNRS-UPR 9016
Case 907, 163 avenue de Luminy
F-13288 Marseille Cedex 9
France

Contents

1 Introduction 35

2 Complexity Function 36
2.1 Deﬁnition . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 36
2.2 Frequencies and Measure-Theoretic Entropy . . . . . . . . . . 38
2.3 Variational Principle . . . . . . . . . . . . . . . . . . . . . . . 40

3 Symbolic Dynamical Systems 40

4 The Graph of Words 43
4.1 The Line Graph . . . . . . . . . . . . . . . . . . . . . . . . . . 45
4.2 Graph and Frequencies . . . . . . . . . . . . . . . . . . . . . . 46

5 Special factors 48

6 Sturmian sequences 49
6.1 A Particular Coding of Rotations . . . . . . . . . . . . . . . . 50
6.2 Frequencies of Factors of Sturmian Sequences . . . . . . . . . 52

35

7 Automatic Sequences 53
7.1 Automata and Transcendence . . . . . . . . . . . . . . . . . . 54
7.2 Applications . . . . . . . . . . . . . . . . . . . . . . . . . . . . 56
7.3 The Multidimensional Case . . . . . . . . . . . . . . . . . . . 58
7.4 Application to Diagonals . . . . . . . . . . . . . . . . . . . . . 59
7.5 Transcendence of the Bracket Series . . . . . . . . . . . . . . . 61
7.6 Complexity and Frequencies . . . . . . . . . . . . . . . . . . . 63

8 Conclusion 65
8.1 Automaticity and Sturmian sequences . . . . . . . . . . . . . . 65
8.2 Sub-aﬃne Complexity . . . . . . . . . . . . . . . . . . . . . . 66

Abstract

The complexity function is a classical measure of disorder for se-
quences with values in a ﬁnite alphabet: this function counts the
number of factors of given length. We introduce here two charac-
teristic families of sequences of low complexity function: automatic
sequences and Sturmian sequences. We discuss their topological and
measure-theoretic properties, by introducing some classical tools in
combinatorics on words and in the study of symbolic dynamical sys-
tems.

1 Introduction

The aim of this course is to introduce two characteristic families of sequences
of low “complexity”: automatic sequences and Sturmian sequences (complex-
ity is deﬁned here as the combinatorial function which counts the number of
factors of given length of a sequence over a ﬁnite alphabet). These sequences
not only occur in many mathematical ﬁelds but also in various domains as
theoretical computer science, biology, physics, cristallography...
We ﬁrst deﬁne some classical tools in combinatorics on words and in the
study of symbolic dynamical systems: the complexity function and frequen-
cies of factors in connection with the notions of topological and measure-
theoretic entropy (Sections 2 and 3), the graphs of words (Section 4), special
and bispecial factors (Section 5). Then we study Sturmian sequences in Sec-
tion 6: these sequences are deﬁned as the sequences of minimal complexity
among non-ultimately periodic sequences. This combinatorial deﬁnition has

36

the particularity of being equivalent to the following simple geometrical rep-
resentation: a Sturmian sequence codes the orbit of a point of the unit circle
under a rotation by irrational angle α with respect to a partition of the unit
circle into two intervals of lengths α and 1 − α. Sturmian sequences have
thus remarkable combinatorial and arithmetical properties. Then we intro-
duce automatic sequences in Section 7: an automatic sequence is deﬁned as
the image by a letter-to-letter projection of a ﬁxed point of a substitution
of constant length or equivalently as a ﬁnite-state function of the represen-
tation of the index in a given basis. We emphasize on the connections with
transcendence of formal power series with coeﬃcients in a ﬁnite ﬁeld. In
particular, we will try to answer the following question: how to recognize if
a sequence is automatic or not? We conclude this course by discussing the
connections between sequences with a linear growth order for the complexity
function, and substitutions.

2 Complexity Function

2.1 Deﬁnition

Let us introduce a combinatorial measure of disorder for sequences over a
ﬁnite alphabet: this notion is called (symbolic) complexity. For more infor-
mation on the subject, we refer the reader to the surveys [8, 43] and to the
course [59].
In all that follows we restrict ourselves to sequences over a ﬁnite alpha-
bet indexed by the set N of non-negative integers. A factor of the inﬁnite
sequence u = (un)n∈N is a ﬁnite block w of consecutive letters of u, say
w = un+1 · · · un+l; l is called the length of w, denoted by |w|. Let p(n) de-
note the complexity function of sequence u with values in a ﬁnite alphabet:
it counts the number of distinct factors of length n of the sequence u. The
complexity function is obviously non-decreasing and for any integer n, one
has 1 ≤ p(n) ≤ dn, where d denotes the cardinality of the alphabet.
This function can be considered to measure the predictability of a se-
quence. The ﬁrst diﬀerence of the complexity function counts the number of
possible extensions in the sequence of factors of given length. We call right
extension (respectively left extension) of a factor w a letter x such that wx
(respectively xw) is a factor of the sequence. Let w+ (respectively w−) de-
note the number of right (respectively left) extensions of w. (One may have

37

w− = 0 but always w+ ≥ 1.) We have

p(n + 1) = ∑

|w|=n w+ = ∑

|w|=n w−,

and thus p(n + 1) − p(n) = ∑

|w|=n
(w+ − 1) = ∑

|w|=n
(w− − 1).

Exercise 2.1 (see [31, 54]) Prove that a sequence is ultimately periodic (i.e.,
periodic from a certain index on) if and only if its complexity function satisﬁes

∃n, p(n) ≤ n ⇐⇒ ∃C, ∀n p(n) ≤ C.

What happens in the case of a sequence deﬁned over Z ?

The complexity function is a measure of disorder connected to the topological
entropy: the topological entropy [1] is deﬁned as the exponential growth rate
of the complexity as the length increases

Htop(u) = lim
n→+∞ logd(p(n))
n .

It is easy to check that this limit exists because of the subadditivity of the
function n ↦→ log(p(n)). Note that the word entropy is used here as a measure
of randomness or disorder. For a survey on the connections between entropy
and sequences, see [13].
The study of the complexity is mainly concerned with the following three
questions.

• How to compute the complexity of a sequence?

• Which functions can be obtained as the complexity function of some
sequence?

• Can one deduce from the complexity a geometrical representation of
sequences?

We will see how to answer the ﬁrst question by introducing special and
bispecial factors, in some particular cases of substitutive sequences (Section
5). The second question is still very much in progress and far from being
solved (in particular in the case of positive entropy): for a survey on the

38

question, see [24, 43]. Although the complexity function is in general not
suﬃcient to describe a sequence, we will see in Section 6 that much can be
said on the geometrical properties in the case of lowest complexity, i.e., in
the case of Sturmian sequences: these sequences are deﬁned to have exactly
n + 1 factors of length n, for any integer n. By Exercise 2.1 a sequence with
complexity satisfying p(n) ≤ n for some n is ultimately periodic. Sturmian
sequences have thus the minimal complexity among all sequences that are
not ultimately periodic.

Exercise 2.2 Deduce from Exercise 2.1 that every preﬁx of a Sturmian se-
quence appears at least two times in the sequence. Deduce that the factors
of every Sturmian sequence appear inﬁnitely often (such a sequence is called
recurrent).

2.2 Frequencies and Measure-Theoretic Entropy

The purpose of this section is to introduce a more “precise” (in a sense that
we will see in Section 2.3) measure of disorder of sequences, connected with
frequencies of factors. The frequency f (B) of a factor B of a sequence (called
density in Host’s course) is deﬁned as the limit, if it exists, of the number of
occurrences of this block in the ﬁrst k terms of the sequence divided by k.

Exercise 2.3 Construct a sequence for which the frequencies of letters do
not exist.

Let us ﬁrst introduce the block entropies for sequences with values in a ﬁnite
alphabet in order to deﬁne the notion of measure-theoretic entropy. These
sequences of block entropies were ﬁrst introduced by Shannon in information
theory, to measure the entropy of the English language (see [65]).
Let u be a sequence with values in the alphabet A = {1, · · · , d}. We
suppose that all the block frequencies exist for u. Let

P (x|x1 · · · xn) = f (x1 · · · xnx)
f (x1 · · · xn) ,

where x1 · · · xn is a block of non-zero frequency and x a letter. Intuitively
P (x|x1 · · · xn) is the conditional probability that the letter x follows the block
x1 · · · xn in the sequence u. We are going to associate with the sequence u
two sequences of block entropies (Hn)n∈N and (Vn)n∈N.

39

For all n ≥ 1, let Vn = ∑L(f (x1 · · · xn)),

where the sum is over all the factors of length n and L(x) = −x logd(x), for
all x ̸= 0 and L(0) = 0. We put V0 = 0.
For all n ≥ 1, let
 Hn = ∑′ f (x1 · · · xn)H(x1 · · · xn), (1)

where the sum is over all the blocks of length n of non-zero frequency and

H(x1 · · · xn) = ∑

x∈A L(P (x/x1 · · · xn)).

We put H0 = V1. The sequence (Hn)n∈N measures in some way the properties
of predictability of the initial sequence u.

Exercise 2.4 Prove that: ∀n ∈ N, Hn = Vn+1 − Vn. (This classical property
in information theory is called the chain-rule.)

Thus, (Hn)n∈N is the discrete derivative of (Vn)n∈N. Note that (Vn)n∈N is a
non-decreasing sequence, since Hn ≥ 0 for all n.
It can be shown that (Hn)n∈N is a monotonic non-increasing sequence of n
(see, for instance [16]). The intuitive meaning of this is that the uncertainty
about the choice of the next symbol decreases when the number of known
preceding symbols increases. From the non-increasing behaviour of the pos-
itive sequence (Hn)n∈N, we deduce the existence of the limit lim
n→+∞ Hn. We

have: ∀n, Hn = Vn+1 − Vn and
 n−1∑

k=0 Hk = Vn. By taking Ces`aro means, we

obtain: lim
n→+∞ Hn = lim
n→+∞ Vn
n .

This limit is called the measure-theoretic entropy of the sequence u, it is the
limit of the entropy per symbol of the choice of a block of length n, when n
tends to inﬁnity.
 40

2.3 Variational Principle

What is the relation between the sequences (Hn)n∈N and (Vn)n∈N? We have:

∀n, nHn ≤
 n−1∑

k=0 Hk = Vn = ∑L(P (x1 · · · xn)).

By concavity of the function L we get: ∀n ≥ 1, Vn ≤ logd p(n). Hence the
following proposition:

Proposition 2.5 We have Hn ≤ logd(p(n))
n , for all n ≥ 1.

We hence get:

lim
n→+∞ Hn = lim
n→+∞ Vn
n = H(u) ≤ Htop(u) = lim
n→+∞ logd(p(n))
n .

This inequality is a particular case of a basic relationship between topological
entropy and measure-theoretic entropy called the variational principle (for a
proof see [53]).

The two limits lim
n→+∞ Hn and lim
n→+∞ logd(p(n))
n are distinct in general and

the notion of measure-theoretic entropy for a sequence is more precise. But
the sequences we are mostly dealing with here are deterministic, i.e., se-
quences with zero entropy. Therefore neither the metrical nor the topological
entropy can distinguish between these sequences.

3 Symbolic Dynamical Systems

Recall some basic notions on symbolic dynamical systems. For a detailed
introduction to the subject, see [57]. Let A denote a ﬁnite alphabet; here we
work with the space AN, whereas in Host’s course it is AZ.
Endow the set AN of all sequences with values in the ﬁnite set A with the
product of discrete topologies on A. This set is thus a compact space. The
topology deﬁned on AN is equivalent to the topology deﬁned by the following
metrics: for x, y ∈ AN

d(x, y) = (1 + inf{k ≥ 0; xk ̸= yk})−1.

41

Two sequences are thus close to each other if their ﬁrst terms coincide. The
cylinder [w], where w = w1 . . . wn belongs to An, is the set of sequences of
the form
 [w] = {x ∈ AN| x0 = w1, x1 = w2, . . . , xn−1 = wn}.

Cylinders are closed and open sets and span the topology.
The space AN is complete as a metric compact space. Let us deduce from
this the existence of ﬁxed points of substitutions. A substitution deﬁned
on the ﬁnite alphabet A is a map from A to the set of words deﬁned on
A, denoted by A∗, extended to A∗ by concatenation, or in other words, a
homomorphism of the free monoid A∗ (see also [49] for a precise study of
substitution dynamical systems).

Exercise 3.1 Let σ be a substitution and a be a letter such that σ(a) begins
by a and |σ(a)| ≥ 2. Prove that there exists a unique sequence beginning with
a satisfying σ(u) = u. This sequence is called a ﬁxed point of the substitution.

For instance, the Fibonacci sequence is deﬁned as the ﬁxed point begin-
ning with 1 of the following substitution

σ(1) = 10, σ(0) = 1.

Let T denote the following map deﬁned on AN, called the one-sided shift:

T ((un)n∈N) = (un+1)n∈N.

The map T is uniformly continuous, onto but not necessarily one-to-one on
AN.

Exercise 3.2 Recall that a sequence is said to be recurrent if every factor
appears at least two times, or equivalently if every factor appears an inﬁnite
number of times in this sequence.
Prove that a sequence u is recurrent if and only if there exists a strictly
increasing sequence (nk)k∈N such that

u = lim
k→+∞ T nku.

Let u be a sequence with values in A. Deﬁne O(u) as the positive orbit
closure of the sequence u under the action of the shift T , i.e., the closure of
the set O(u) = {T n(u), n ≥ 0}. The set O(u) is a compact metric space,
and thus complete. It is also T -invariant: T (O(u)) ⊂ O(u). In other words
T may be considered as acting on O(u).

42

Exercise 3.3 1. Prove that

O(u) = {x ∈ AN, L(x) ⊂ L(u)},

where L(x) denotes the set of factors of the sequence x.

2. Prove that u is recurrent if and only if T is onto on O(u).

Let X be a non-empty compact metric space and T be a continuous map
from X to X. The system (X, T ) is called a topological dynamical system.
For instance, (O(u), T ) is a topological dynamical system. A topological
dynamical system is called minimal if every closed T -invariant set E is either
equal to the full set X or to the empty set.

Exercise 3.4 • Prove that (X, T ) is minimal if and only if X = O(x),
for every element x of X.

• A sequence is said to be uniformly recurrent if every factor appears
inﬁnitely often and with bounded gaps (or, equivalently, if for every
integer n, there exists an integer m such that every factor of u of
length m contains every factor of length n). Prove that a sequence u
is uniformly recurrent if and only if (O(u), T ) is minimal. (If w is a
factor of u, write O(u) = ⋃

n∈N T −n[w],

and conclude by a compactness argument.)

The following special case of the Daniell-Kolmogorov consistency theo-
rem (see for instance [73]) establishes the existence of a certain probability
measure on (O(u), T ). A Borel probability measure µ deﬁned on (O(u), T )
is called T -invariant if µ(T −1(B)) = µ(B), for any Borel set B.

Theorem 3.5 Let u be a sequence on A = {1, . . . , d}. Consider a family of
maps (pn)n≥1, where pn is a map from An to R, such that

• for any word w in An, pn(w) ≥ 0,

•
 d∑

i=1 p1(i) = 1,
 43

• for any word w = w1 . . . wn in An, pn(w) =
 d∑

i=1 pn+1(w1 . . . wni).

Then there exists a unique probability measure µ on AN deﬁned on the cylin-
ders by µ([w1 . . . wn]) = pn(w1 . . . wn).
Furthermore, if for any n and for any word w = w1 . . . wn in An,

pn(w) =
 d∑

i=1 pn+1(iw1 . . . wn),

then this measure is T -invariant.

In particular, if all frequencies exist, then there exists a unique T -invariant
probability measure which assigns to each cylinder the frequency of the corre-
sponding factor. Moreover suppose the symbolic dynamical system (O(u), T )
uniquely ergodic, i.e., there exists a unique T -invariant probability measure µ
on this dynamical system. Thus a precise knowledge of the frequencies allows
a complete description of the measure µ. For instance, a symbolic dynamical
system obtained via the ﬁxed point of a primitive substitution [49, 57], or
via a Sturmian sequence is uniquely ergodic.

4 The Graph of Words

The Rauzy graph Γn of words of length n of a sequence on a ﬁnite alphabet
A (of cardinality d) is an oriented graph (see, for instance, [58]), which is
a subgraph of the de Bruijn graph of words
1 (see [32]). Its vertices are the
factors of length n of the sequence and the edges are deﬁned as follows: there
is an edge from U to V if V follows U in the sequence, i.e., if there exists a
word W and two letters x and y such that U = xW , V = W y and xW y is
a factor of the sequence. There are p(n + 1) edges and p(n) vertices, where
p(n) denotes the complexity function.

Exercise 4.1 Prove that the graphs of words of a sequence are always con-
nected. Prove the following equivalence (see [61]):

1The de Bruijn graph of words corresponds to the graph of words of a sequence of
maximal complexity (∀n, p(n) = d
n) and was introduced by de Bruijn in order to construct
circular ﬁnite sequences of length d
n with values in {0, 1, . . . , d − 1} such that every factor
of length n appears once and only once: such a sequence corresponds to a Hamiltonian
closed path in de Bruijn graph.
 44

• the sequence u is recurrent,

• every factor of u appears at least twice,

• the graphs of words are strongly connected.

Let U be a vertex of the graph. Denote by U + the number of edges of Γn
with origin U and by U − the number of edges of Γn with end vertex U. In
other words, U + (respectively U −) counts the number of right (respectively
left) extensions of U. Recall that

p(n + 1) = ∑

|U |=n U + = ∑

|U |=n U −,

and thus p(n + 1) − p(n) = ∑

|U |=n
(U + − 1) = ∑

|U |=n
(U − − 1).

Exercise 4.2 Recall that a Sturmian sequence is deﬁned as a sequence of
complexity function p(n) = n + 1, for every positive integer n, and that it is
recurrent (Exercise 2.2).

• For any positive integer n, prove that there exists a unique factor of
length n having two right (respectively left) extensions: such a factor is
called a right (respectively left) special factor (or also expansive factor)
and is denoted from now on by Rn (respectively Ln).

• Prove that the graph of words Γn of a Sturmian sequence has the two
following possible forms.

• Deduce from the morphology of the graph of words Γn that every Stur-
mian sequence is uniformly recurrent. One can ﬁrst prove that every
factor of a Sturmian sequence is a subfactor of a factor of the form Rn
and then deduce from the morphology of the graph Γn that Rn appears
with bounded gaps.
 45

✬ ✩✛

✫ ✪

✲

✛

Ln Rn Ln = Rn

✛

✛

✤

✣
 ✜

✢

✤

✣
 ✜

✢

Exercise 4.3 • Prove that if the sequence u is uniformly recurrent and
non-constant, then the graph Γn has no edge of the form U → U, for
n large enough.

• Suppose that the sequence u is uniformly recurrent. Prove that if the
graph of words Γn+1 is Hamiltonian (i.e., there exists a closed oriented
path passing exactly once through every vertex), then the graph Γn is
Eulerian (there exists a closed path passing exactly once through every
edge) and that U + = U −, for every vertex of Γn. Is the converse true?

4.1 The Line Graph

The line graph D(Γn) of the graph of words Γn is deﬁned as follows: its
vertices are the edges of Γn (i.e., the factors of length n + 1); given two
vertices u and v in D(Γn), there is an edge from u to v if the enpoint of the
edge labelled u in Γn is the origin of the edge labelled v. It is easily seen
that the edges of the line graph correspond to words of length n + 2 such
that their preﬁx and their suﬃx of length n + 1 are factors of the sequence
u. The line graph of Γn is thus a subgraph of Γn+1.

Exercise 4.4 Study the evolution of the graph of words from Γn to Γn+1 for
a Sturmian sequence by using the line graph. (Distinguish between the two
possible forms of the graph).

Remark 4.5 In [61] Rote uses the graph of words and the line graph for
the study of sequences of complexity p(n) = 2n, for every n (see also [41]).
The study of the evolution of the graph of words for any Sturmian sequence
is a very powerful method and contains all the information concerning the
sequence: Arnoux and Rauzy have thus proved that every Sturmian sequence
is generated by the composition of two substitutions (see [11]); one can also

46

study the frequencies of factors of given length (see Section 8.2 and [14]) or
covering numbers for rotations (see [15, 26]).

4.2 Graph and Frequencies

Let us see how to deduce from the morphology of the graphs of words results
concerning the frequencies of factors. This follows an idea of Dekking who
expressed the block frequencies for the Fibonacci sequence, by using the
graph of words (see [34]).
In this section we restrict ourselves to sequences for which the frequencies
exist. Observe that the function which associates to an edge labelled by xW y
the frequency of the factor xW y is a ﬂow. Indeed, it satisﬁes Kirchhoﬀ’s
current law: the total current ﬂowing into each vertex is equal to the total
current leaving the vertex. This common value is equal to the frequency of
the word corresponding to this vertex.

Lemma 4.6 Let U and V be two vertices linked by an edge such that U + = 1
and V − = 1. Then the two factors U and V have the same frequency.

Proof. Write U = xW and V = W y, where x and y are letters. As U + = 1,
U has a unique right extension y. Similarly, V has a unique left extension
x. Thus f (U) = f (Uy) = f (xW y) = f (xV ) = f (V ), where f denotes the
frequency.
A branch of the graph Γn is a longest sequence of maximal length (U1, . . . , Um)
of connected edges of Γn, possibly empty, satisfying

U +
i = 1, for i < m, U −
i = 1, for i > 1.

Therefore, the edges of a branch have the same frequency and the number of
frequencies of factors of given length is bounded by the number of branches
of the corresponding graph, as expressed below (see [18]).

Theorem 4.7 For a recurrent sequence of complexity function p(n), the fre-
quencies of factors of given length, say n, take at most 3(p(n + 1) − p(n))
values.

Proof. Let V1 denote the set of factors of length n having more than one
extension. In other words V1 is the subset of vertices of the graph Γn deﬁned
as follows: U ∈ V1 if and only if U + ≥ 2. The cardinality of V1 satisﬁes

card(V1) = ∑

|U |=n, U +≥2 1 ≤ ∑

|U |=n
(U + − 1) = p(n + 1) − p(n).

47

Let V2 denote the subset of vertices of the graph Γn deﬁned as follows: U ∈ V2
if and only if U + = 1 and if V denotes the unique vertex such that there is
an edge from U to V in Γn, then V − ≥ 2. In other words, U belongs to V2
if and only if U = xW , where x is a letter and where the factor W of the
sequence u has a unique right extension but at least two left extensions. The
cardinality of V2 satisﬁes:

card(V2) ≤ ∑

V −≥2 V − = ∑

V −≥2
(V − − 1) + ∑

V −≥2 1 ≤ 2(p(n + 1) − p(n)).

Thus there are at most 3(p(n + 1) − p(n)) factors in V1 ∪ V2.
Let U be a factor of length n belonging neither to V1 nor to V2: U + = 1
and the unique word V such that there is an edge from U to V in Γn satisﬁes
V − = 1. The two factors U and V thus have the same frequency. Now
consider the path of the graph beginning at U and consisting of vertices
which do not belong to V1 nor to V2. The last vertex of this path belongs to
either V1 or to V2, and has the same frequency as U.

Remark 4.8 In fact we have proved that the frequencies of factors of length
n take at most p(n + 1) − p(n) + rn + ln values, where rn (respectively ln)
denotes the number of factors having more than one right (respectively left)
extension.

We deduce from this result that if p(n + 1) − p(n) is uniformly bounded
with n, the frequencies of factors of given length take a ﬁnite number of
values. Indeed, using a theorem of Cassaigne quoted below (see [23]), we can
easily state the following corollary.

Theorem 4.9 If the complexity p(n) of a sequence on a ﬁnite alphabet is
sub-aﬃne, i.e., ∃(a, b), ∀n, p(n) ≤ an + b,

then p(n + 1) − p(n) is bounded.

Corollary 4.10 If a sequence has a sub-aﬃne complexity then the frequen-
cies of its factors of given length take a ﬁnite number of values.

We will see in Section 7.6 (Theorem 7.26) that ﬁxed points of uniform substi-
tutions (i.e., substitutions such that the images of the letters have the same
length) or ﬁxed point of primitive substitutions have sub-aﬃne complexities.

48

In particular, in the Sturmian case (∀n, p(n) = n + 1), Theorem 4.7 implies
that the frequencies of factors of given length of a Sturmian sequence take
at most three values. We will come back to this in Section 6.2.
Note that Theorem 4.9 above does not hold anymore for the second-
diﬀerence of the complexity p(n + 2) + p(n) − 2p(n + 1) in the case of a
sub-quadratic complexity (see the counterexample in [42]).

5 Special factors

The aim of this section is to introduce the notions of special and bispecial
factors in order to evaluate the second-diﬀerence of the complexity, which is
often easier to compute than the complexity itself. Indeed, in the case of a
low complexity, the number of special factors and bispecial factors, which is
low, is quite easy to evaluate. For a more detailed exposition, see [24].
Let u be a sequence with values in a two-letter alphabet A. Let w+

(respectively w−) denote the number of right (respectively left) extensions of
w. Recall that

p(n + 1) − p(n) = ∑

|w|=n
(w+ − 1) = ∑

|w|=n
(w− − 1).

A factor is said to be a left special factor (respectively right special factor)
if it has more than one left (respectively right) extension. We use the notation
of [24], in which the case of a bigger-sized alphabet is also considered. A
factor is said to be bispecial if it is both a right and a left special factor.
More precisely, we distinguish three cases according to the cardinality c(w)
of L(u)∪AwA, where L(u) denotes the set of factors of the sequence u and w
is a bispecial factor, the operation considered here being the concatenation.
We have obviously 2 ≤ c(w) ≤ 4.

• If c(w) = 2, then w is called a weak bispecial factor,

• if c(w) = 3, then w is called an ordinary bispecial factor,

• if c(w) = 4, then w is called a strict bispecial factor.

Exercise 5.1 Let bw(n) (respectively bs(n)) denote the number of weak (re-
spectively strict) bispecial factors of the sequence u of size n. Prove that the
second-diﬀerence of the complexity is given by

p(n + 2) + p(n) − 2p(n + 1) = s(n + 1) − s(n) = bs(n) − bw(n),

49

where s(n) = p(n + 1) − p(n).

Exercise 5.2 Consider the Fibonacci sequence. Prove that every factor w
can be uniquely written as follows: w = r1σ(x)r2, where x is a factor, r1 ∈
{ε, 0}, and r2 = 1 if the last letter of w is 1, and r2 = 0, otherwise. Prove by
induction that the bispecial factors of the Fibonacci sequence are all ordinary.
Deduce that this sequence is Sturmian.

Exercise 5.3 Let u be the Thue-Morse sequence deﬁned as the ﬁxed point
beginning by 0 of the following substitution: σ(0) = 01 and σ(1) = 10. We
will compute the complexity function of the Thue-Morse sequence in two
ways.

1. Prove that every factor w can be written as follows: w = r1σ(x)r2,
where x is a factor and ri ∈ {ε, a, b}. If |w| ≥ 5, then this decomposition
is unique.

2. Prove that p(2n) = p(n) + p(n + 1) and that p(2n + 1) = 2p(n + 1), for
n ≥ 1. Give an expression for the complexity function (see for instance
[20]).

3. Find by induction the expressions of bs(n), bo(n) and bw(n) by studying
the small length cases. Deduce an expression for the complexity.

6 Sturmian sequences

Sturmian sequences have received considerable attention in the literature.
We refer the reader to the impressive bibliography of [21]. A recent account
on the subject can also be found in [12].

6.1 A Particular Coding of Rotations

We introduce a large family of Sturmian sequences obtained by coding the
orbit of a point of the unit circle under an irrational rotation.
Let {x} denote as usual the fractional part of x (i.e., if ⌊x⌋ denotes the
largest integer not exceeding x, then {x} = x − ⌊x⌋). Let α be an irrational
number in ]0, 1[ and consider the rotation Rα of angle α deﬁned on the unit
circle (identiﬁed with [0, 1[ or with the unidimensional torus R/Z): we have
Rα(x) = x + α (mod 1). The positive orbit of a point x of the unit circle

50

under the rotation by angle α is the set of points {{αn + x}, n ≥ 0}. We
code the information concerning the orbit of x by a binary sequence. The
coding of the orbit of x under the rotation by angle α with respect to the
partition P = {[0, 1 − α[, [1 − α, 1[} is the sequence u = (un)n∈N deﬁned on
the alphabet {0, 1} as follows:

un = 1 ⇔ {x + nα} ∈ [0, 1 − α[.

We could also choose to code the orbit of the rotation with respect to the
partition P ′ = {]0, 1 − α], ]1 − α, 1]}. As α is irrational, the two sequences
obtained by coding with respect to P or to P ′ are ultimately equal. The
results stated below on codings with respect to P are obviously true for P ′.
Let I0 = [0, 1 − α[ and I1 = [1 − α, 1[. A ﬁnite word w1 · · · wn deﬁned on
the alphabet {0, 1} is a factor of the sequence u if and only if there exists an
integer k such that

{x + kα} ∈ I(w1, . . . , wn) =
 n−1⋂

j=0 R−j(Iwj+1).

As α is irrational, the sequence ({x+nα})n∈N is dense in the unit circle, which
implies that w1w2 . . . wn is a factor of u if and only if I(w1, . . . , wn) ̸= ∅. In
particular, the set of factors does not depend on the initial point x of this
coding. Furthermore, one can check that the sets I(w1, . . . , wn) are connected
and are bounded by the points {k(1 − α)}, for 0 ≤ k ≤ n − 1. There are n + 1
such intervals (α is irrational) and thus n+1 factors of length n: the sequence
u is therefore Sturmian.

Remark 6.1 In the general case of a coding of an irrational rotation with
respect to a partition of the unit circle in l intervals, the complexity has the
form p(n) = an + b, for n large enough (see [2]). Conversely, every sequence
of ultimately aﬃne complexity is not necessarily obtained as a coding of
rotation. See for instance [61], where Rote studies the case of sequences of
complexity p(n) = 2n, for every n. However, if the complexity of a sequence
u has the form p(n) = n + k, for n large enough, then u is the image of a
Sturmian sequence by a morphism, up to a preﬁx of ﬁnite length (see for
instance [2, 25, 36]).

Exercise 6.2 Let u be a coding of the rotation by angle α deﬁned as above.
Prove that the orbit closure O(u) is the set of sequences obtained by coding

51

every point of the unit circle with respect to the partition P or P ′ under the
rotation by angle α. (Use the fact that the set of factors of a coding depends
neither on the initial point x nor on the choice of the partition but only on
the angle of the rotation). Deduce the minimality of (O(u), T ).

Now a natural question is whether all Sturmian sequences are obtained
by coding a rotation as deﬁned above. The answer is yes and is due to Morse
and Hedlund (see [55]): this shows that in this case of low disorder, one can
give a geometrical description of sequences deﬁned up to their complexity
function. When the complexity grows, this becomes much more diﬃcult
(see for instance [11] for a geometrical representation of a particular class of
sequences of complexity 2n + 1).

Theorem 6.3 (Hedlund and Morse) A sequence u is Sturmian if and
only if there exists an irrational α in ]0, 1[ and x on the unit circle such
that u is the coding of the orbit of x under the rotation by angle α with
respect to one of the partitions {[0, 1 − α[, [1 − α, 1[} or {]0, 1 − α], ]1 − α, 1]}.

Sturmian sequences are also characterized by the following properties.

• Sturmian sequences are exactly the non-ultimately periodic balanced
sequences over a two-letter alphabet. A sequence is balanced if the
diﬀerence between the number of occurrences of a letter in any two
factors of the same length is bounded by one in absolute value.

• Sturmian sequences are codings of trajectories of irrational initial slope
in a square billiard obtained by coding horizontal sides by the letter 0
and vertical sides by the letter 1.

• One can also consider Sturmian sequences as approximations of a line
of irrational slope in the upper half-plane.

The last three properties can be easily deduced from the representation by a
rotation: they are just geometrical reformulations; the ﬁrst characterization
of Sturmian sequences in terms of the balance property is much more diﬃcult
to establish and is an important step in the proof of Theorem 6.3.

52

6.2 Frequencies of Factors of Sturmian Sequences

We now consider properties of frequencies of factors of Sturmian sequences.
The frequency of the factor w1 . . . wn exists and is equal to the density of
the set {k | {x + kα} ∈ I(w1, . . . , wn)},

which is equal to the length of I(w1, . . . , wn), by uniform distribution of the
sequence ({x + nα})n∈N. The lengths of these intervals are equal to the
frequencies of factors of length n.
But we deduce from Theorem 4.7 the following result.

Theorem 6.4 The frequencies of factors of given length of a Sturmian se-
quence take at most three values.

Theorem 6.4 implies that the lengths of the intervals I(w1, . . . , wn), and
thus the lengths of the intervals obtained by placing the points 0, {1 −
α}, . . . , {n(1−α)} on the unit circle, take at most three values. We thus have
proved the following classical result in Diophantine approximation, called the
three-distance theorem (see the survey [3]). In fact, this point of view and
more precisely, the study of the evolution of the graphs of words with respect
to the length n of the factors, allows us to give a proof of the most complete
version of the three distance theorem, i.e., to express the exact number of
factors having each of the three frequencies and the frequencies themselves
(for more details, the reader is referred to [14]).
The three distance theorem was initially conjectured by Steinhaus and
proved by V. T. S´os (see [67, 68, 69, 70]).

Theorem 6.5 Let 0 < α < 1 be an irrational number and n a positive
integer. The points {iα}, for 0 ≤ i ≤ n, partition the unit circle into n + 1
intervals, the lengths of which take at most three values, one being the sum
of the other two.
More precisely, let ( pk
qk )k∈N and (ck)k∈N be the sequences of the convergents
and partial quotients associated to α in its continued fraction expansion (if
α = [0, c1, c2, . . .], then pn
qn = [0, c1, . . . , cn]). Let ηk = (−1)
k(qkα − pk). Let n
be a positive integer. There exists a unique expression for n of the form

n = mqk + qk−1 + r,

with 1 ≤ m ≤ ck+1 and 0 ≤ r < qk. Then, the circle is divided by the points
0, {α}, {2α}, . . . , {nα} into n + 1 intervals which satisfy:

53

• n + 1 − qk of them have length ηk (which is the largest of the three
lengths),

• r + 1 have length ηk−1 − mηk,

• qk − (r + 1) have length ηk−1 − (m − 1)ηk.

7 Automatic Sequences

The aim of this section is to introduce automatic sequences and to study
them in connection with properties of algebraicity of formal power series
over a ﬁnite ﬁeld.
Let k be an integer greater than or equal to 2. Recall the deﬁnition of a
ﬁnite complete deterministic k-automaton (also called 2-tape automaton or
transducer). For more details, see the courses of Frougny, see [30] or see the
surveys [5, 9]. A k-automaton is represented by a directed graph deﬁned by:

• a ﬁnite set of states S = {i = a1, a2, · · · , ad}, one of these states i is
called the initial state;

• k transition maps (or “edges”) from the set of states S into itself,
denoted by 0, 1, · · · , k − 1;

• a set Y and a map ϕ from S into a set Y , called output function or exit
map.

A sequence (u(n))n∈N with values in Y is called k-automatic (it is also
called a k-uniform tag sequence or a k-recognizable sequence) if it is generated
by a k-automaton as follows: let ω(n) be the base k expansion of the integer n;
starting form the initial state one feeds the automaton the sequence ω(n), the
digits being read in growing order of powers; after doing this the automaton
is in the state a(n) (the automaton is said to be fed in reverse reading.) Then
put u(n) = ϕ(af ). One can similarly give another deﬁnition of k-automaticity
by reading the digits in the reverse order, i.e., by starting with the most
signiﬁcant digit, but these two notions are easily seen to be equivalent. (The
automaton is said to be fed in direct reading.)

54

7.1 Automata and Transcendence

Let Fq be the ﬁnite ﬁeld with q elements, and let p denote its characteristic.
We thus have p prime and q = ps, where s is a nonzero natural integer. The
ﬁeld Fq((1/X)) of Laurent formal power series with coeﬃcients in Fq is the
ﬁeld of formal power series series of the form

u(−d)X d + · · · + u(0) + u(1)X −1 + · · · ,

where the coeﬃcients u(i) belong to Fq. Similarly, we denote by Fq((X)) the
ﬁeld of formal power series of the form

u(−d)X −d + · · · + u(0) + u(1)X + · · ·

A formal power series F is called algebraic over Fq(X) if there exists a non-
trivial polynomial P with coeﬃcients in Fq(X) such that P (F ) = 0. In the
converse case, F is called transcendental over Fq(X).
The following theorem due to Christol, Kamae, Mend`es France and Rauzy
(see [27, 28] and also [5]) gives a necessary and suﬃcient condition of alge-
braicity for a formal power series with coeﬃcients in a ﬁnite ﬁeld.

Theorem 7.1 (Christol, Kamae, Mend`es France and Rauzy)
Let u = (u(n))n∈N be a sequence with values in Fq. The following condi-
tions are equivalent:

1. the formal power series ∑

n≥0 u(n)X n is algebraic over the ﬁeld Fq(X),

2. the q-kernel Nq(u) of the sequence u is ﬁnite, where Nq(u) is the set of
subsequences of the sequence (u(n))n∈N deﬁned by

Nq(u) = {(u(qkn + r))n∈N; k ≥ 0; 0 ≤ r ≤ qk − 1},

3. the sequence u is q-automatic,

4. the sequence u is the image by a letter-to-letter projection of a ﬁxed
point of a substitution of constant length.

The last equivalence is due to Cobham (see [30]) and the equivalence between
2 and 3 dates back to Eilenberg in [39].

55

Remark 7.2 • The same theorem holds by considering a series ∑ u(n)X −n

in Fq((1/X)) with the same deﬁnition for the q-kernel. Indeed, ∑ u(n)X −n

is transcendental over Fq(X) if and only if ∑ u(n)X n is transcendental
over Fq(X).

• The proof of the equivalence between 2 and 3, and between 2 and 4, is
constructive.

• The equivalences between 2, 3 and 4 is true for any sequence taking its
values in a set of cardinality q, where q is not necessarily a power of a
prime.

• The notion of p-automaticity can also be expressed as follows in terms
of ﬁrst-order logic: a sequence is generated by a p-substitution if and
only if it is p-deﬁnable (it can be deﬁned in the theory (N, +, Vp), where
Vp is the function “valuation” that associates to x the highest power of
p that divides x (or 1 if x = 0)). For more details, the reader is referred
to the survey [22].

• Durand has extended in [37] this characterization of automatic se-
quences to the case of uniformly recurrent sequences generated by sub-
stitutions of non-constant length, by introducing the notion of return
words.

Exercise 7.3 1. Show that a sequence is p-automatic if and only if it is
pk-automatic for any non-zero power of the prime p.

2. Consider the Thue-Mose sequence (S2(n))n∈N deﬁned over F2, where
S2(n) is the sum modulo 2 of the coeﬃcients of the digits in the base 2
expansion of the integer n. Build a 2-automaton generating the Thue-
Morse sequence.

3. Build a d-automaton generating the characteristic sequence of the set
of powers of a ﬁxed positive integer d.

4. Build a d-automaton generating the characteristic sequence of the set
of integers divisible by d.

5. Build a 2-automaton generating the characteristic sequence of the set
of integers of base 2-expansion of the form 1
n0m1, for n, m > 0 and
n + m odd.
 56

6. Prove that the characteristic sequence of the set of integers of base
2-expansion of the form 1n0n+11, for n > 0, is not 2-automatic.

7.2 Applications

In this section we give some applications of Theorem 7.1. The ﬁrst two are
easy consequences of the theorem.

• Let ∑ u(n)X n be an algebraic formal power series. Let a and b be two
natural integers. The series ∑

n≥0 u(an + b)X n is algebraic.

• Let p ≥ 2 be an integer. Let Sp(n) be the sum modulo p of the digits
of n in base p. The series ∑

n≥0 Sp(n)X n is algebraic.

Remark 7.4 The series ∑
n≥0 Sp(n
2)X n is transcendental. More precisely,
let R be a polynomial with coeﬃcients in Q such that R(N) ⊂ N. The formal
power series ∑

n≥0 Sp(R(n))X n is algebraic over Fp if and only if the degree
of R is less than or equal to 1 (see [4]).

The Hadamard product of two series ∑ u(n)X n and ∑ v(n)X n is de-

ﬁned as the series ∑ u(n)v(n)X n. By considering the the notion of q-kernel,
we easily deduce the following.

Theorem 7.5 The Hadamard product of two algebraic formal power series
with coeﬃcients in a ﬁnite ﬁeld is algebraic.

Note that the following theorem, due to Cobbham [29], produces more
examples of transcendental series. We will not give here the proof of this
theorem, which is rather diﬃcult.

Theorem 7.6 Let u be a sequence which is both k-automatic and k′-automatic.
If k and k′ are multiplicatively independent (i.e., if log(k)
log(k′) is irrational), then
the sequence u is ultimately periodic.

We deduce from this theorem the following result of transcendence, which
answers, in the case of formal power series with values in a ﬁnite ﬁeld, an
analogous question attributed to Mahler and still open: given (u(n))n∈N a
binary sequence such that the series ∑ u(n)2−n and ∑ u(n)3−n are algebraic
over Q, is this sequence ultimately periodic?

57

Theorem 7.7 Let (u(n))n∈N be a binary sequence such that ∑ u(n)X n con-
sidered as an element of F2((X)) and ∑ u(n)X n considered as an element of
F3((X)) are algebraic. Then, this sequence is ultimately periodic, i.e., both
series are rational.

Another application of Cobham’s Theorem is the following (see for in-
stance [7]).

Theorem 7.8 Let r be an integer greater than or equal to 2. The series
+∞∑

k=0 X rk is algebraic over Fq(X) if and only if r is a power of p.

Proof. Write +∞∑

k=0 X rk = ∑

n≥1 u(n)X n,

where u = (u(n))n∈N is the characteristic sequence of the set of powers of r.

The series
 +∞∑

k=0 X rk is algebraic over Fq(X) if and only if the sequence u is p-

automatic. But it is easily seen that the sequence u is r-automatic (Exercise

7.3) and not ultimately periodic. Hence the series
 +∞∑

k=0 X rk is algebraic over

Fq(X) if and only if r is a power of p.

Remark 7.9 The formal power series ∑ u(n)X n belongs to Fq(X) if and
only if the sequence (u(n))n∈N is ultimately periodic. Note that in the real
case we just have the following implication: if the sequence (u(n))n∈N is
ultimately periodic, then the series ∑ u(n)X n belongs to Q(X). The rational
series ∑ nX n shows that the converse is not true.

It is natural to consider the connections between transcendence in the real
case and in positive characteristic. Indeed, a formal power series is algebraic
in positive characteristic if the sequence of its coeﬃcients has some kind of
order, whereas irrational algebraic real numbers cannot have a too regular
expansion. Loxton and van der Poorten [51] have conjectured the following
(this conjecture is often quoted as a theorem, but there seems to be a gap in
the proof).
 58

Conjecture 7.10 If the sequence of the coeﬃcients in the base q-expansion
of a real number is automatic, then this number is either rational or tran-
scendental.

This conjecture illustrates, like Cobhams’s Theorem, the fact that transcen-
dence deeply depends on the frame in which it is considered.

7.3 The Multidimensional Case

The Christol, Kamae, Mend`es France and Rauzy theorem can be generalized
to the multidimensional case. In particular, Salon has generalized this theo-
rem to the case of a formal power series with a ﬁnite number of indeterminates
and with coordinates in a ﬁnite ﬁeld, say ∑

ni≥0 u(n1, n2, · · · , nd)X n1
1 · · · X nd
d
(see for instance [62] and [63]). The generalization of the q-kernel is given in
this case by:

Nq(u(n1, n2, · · · , nd)) = {u(qkn1 + r1, qkn2 + r2, · · · , qknd + rd),

k ≥ 0, 0 ≤ ni ≤ qk − 1, for i = 1 to d}.

Recall that a formal power series F = ∑

ni≥0 u(n1, n2, · · · , nd)X n1
1 · · · X nd
d
is said to be algebraic over Fq(X1, X2, · · · , Xd) if there exists a nontrivial
polynomial P with coeﬃcients in Fq(X1, X2, · · · , Xd) such that P (F ) = 0.
The notions of automaton and substitution can also be generalized in two
dimensions. A two-dimensional substitution of constant length l associates
to each letter a square array of letters of size (l, l). A two-dimensional k-
automaton is deﬁned similarly as a one-dimensional k-automaton but in this
case the edges are labelled by pairs of integers in [0, k − 1]
2. A sequence
(u(m, n))(m,n)∈Z2 is generated by the automaton A by reading simultaneously
the digits of the base k expansions of m and n, the shortest expansion being
completed with leading zeroes to get two strings of symbols of the length of
the longest expansion (without leading zeroes).
We thus have the following theorem due to Salon (see [62] and [63]).

Theorem 7.11 The series ∑ u(n1, n2, · · · , nd)X n1
1 · · · X nd
d is algebraic over
Fq(X1, X2, · · · , Xd) if and only if the q-kernel of the sequence u is ﬁnite.

The following results are easy applications of this theorem.

• Let u be an algebraic formal power series. The double formal power
series ∑ u(m + n)X mY n is algebraic.

59

• Let ∑ u(m, n)X mY n be algebraic. Let a, b, c, d be four integers. The
series ∑ u(am + b, cn + d)X mY n is algebraic.

Exercise 7.12 Consider the substitution σ : {0, 1} → {0, 1} ×{0, 1} deﬁned
by
 σ(0) = 00
00 ,

σ(1) = 11
10 .

Prove that the double-sequence ﬁxed point of this substitution generated by
the successive images of 1 is equal to Pascal’s triangle reduced modulo 2.
Find the substitution generating Pascal’s triangle modulo a prime p.

Remark 7.13 The double-sequence corresponding to Pascal’s triangle mod-
ulo an integer d is automatic if and only if d is a power of a prime (see [10]).

7.4 Application to Diagonals

Another interesting consequence of this generalization to the multidimen-
sional case is given by the following results. The diagonal of a double formal
power series ∑ u(m, n)X mY n is deﬁned as the series ∑ u(n, n)X n.

Theorem 7.14 The diagonal of an algebraic formal power series with coef-
ﬁcients in a ﬁnite ﬁeld is algebraic.

Proof. Consider either the notion of q-kernel or the one-dimensional sub-
stitution deﬁned by associating to each letter the “diagonal” of the square
array of letters associated by the initial substitution.
Theorem 7.14 was ﬁrst proved by Furstenberg in [46] and can be compared
to the following theorem, also due to Furstenberg.

Theorem 7.15 A series with coeﬃcients in a ﬁnite ﬁeld is algebraic if and
only if there exists a rational double formal power series such that the initial
series is the diagonal of this double series.

Observe that this result still holds on C when considering two-indeterminate
series but is false for series involving more indeterminates. For a survey on
the subject, the reader is referred to [6].

60

Exercise 7.16 1. Conisder the Thue-Morse sequence (S2(n))n∈N. Prove
that the series ∑ S2(n)X n is the diagonal of the rational function in
F2(X, Y ) deﬁned by Y (1 + Y (1 + XY ) + X(1 + XY )−2)−1.

2. Let (u(n))n∈N be a sequence with values in the ﬁnite set X. Prove that
if ∑ u(n)X n is algebraic, then, for any x ∈ X, ∑

v(n)=x X n is algebraic.

3. Let (v(n))n∈N be the characteristic sequence of the set of powers of the
prime p. Prove that the series ∑ v(n)X n is the diagonal of the rational
fraction of Fp(X, Y ) deﬁned by X/(1 − (X p−1 + Y )).

4. Let (w(n))n∈N be the characteristic sequence of the set of integers of
base 2-expansion of the form 1n0m1, for n, m > 0 and n + m odd.
Let (x(n))n∈N be the characteristic sequence of the set of integers
of base 2-expansion of the form 1
n0n+11, for n > 0. Let (y(n))n∈N
be the characteristic sequence of the set of squares. Prove that the
Hadamard product of the series ∑

n≥0 w(n)X n and ∑

n≥0 y(n)X n is
equal to ∑

n≥0 x(n)X n. Deduce from Exercice 7.3 that the sequence
(y(n))n∈N is not 2-automatic (see [60] and the survey [71]).

Remark 7.17 Christol, Kamae, Mend`es France and Rauzy’s theorem can
also be extended to a general ﬁeld of positive characteristic, which is not
necessarily ﬁnite. Such a generalization is due to Sharif and Woodcock (see
[66]) and Harase (see [48]). The results on the Hadamard poduct and on
the diagonal still hold in this context. We can deduce namely the following
corollary proved ﬁrst by Deligne in [35].

Corollary 7.18 The Hadamard product of two algebraic formal power series
with coeﬃcients in a ﬁeld of positive characteristic is algebraic. The diagonal
of an algebraic formal power series with coeﬃcients in a ﬁeld of positive
characteristic is algebraic.

Remark 7.19 Fresnel, Koskas and de Mathan have also generalized eﬀec-
tively Christol, Kamae, Mend`es France and Rauzy’s Theorem to the case of
an inﬁnite ground ﬁeld [44].
 61

7.5 Transcendence of the Bracket Series

The purpose of this section is to prove the following result, which gives us an
example of application of the Christol, Kamae, Mend`es France and Rauzy
theorem. This result was ﬁrst proved by Wade in [72]; the proof below is due
to Allouche (see [7] and also [52]).

Theorem 7.20 The series
 +∞∑

k=1
 1
[k] is transcendental over Fq(X).

This proof makes use of the following consequence of the Christol, Kamae,
Mend`es France and Rauzy theorem.

Proposition 7.21 Let (u(n))n∈N be a sequence with values in Fq. If the
series ∑

n≥0 u(n)X −n is algebraic over Fq(X), then the sequence (u(qn −
1))n∈N is ultimately periodic.

Proof. Suppose that the series ∑

n≥0 unX −n is algebraic; the sequence u =
(u(n))n∈N is thus q-automatic. Let A denote a ﬁnite q-automaton which
generates the sequence u. The subsequence (u(qn − 1))n∈N is obtained by
reading in the automaton A strings of ones. As the number of states of
A is ﬁnite, a suﬃciently long string of ones meets twice the same state.
The sequence of states met is thus ultimately periodic, which implies that
(u(qn − 1))n∈N is also ultimately periodic.

Remark 7.22 Let UT nV denote, for any natural integer n, the integer of
base-q expansion UT nV , where U, T, V are words deﬁned over {0, 1, · · · , q −
1}. We can similarly prove that if the series ∑

n≥0 unX −n is algebraic, then
the sequence (u(UT nV ))n∈N is ultimately periodic. This result corresponds
to the classical pumping lemma in automata theory.

Exercise 7.23 Give another proof of Proposition 7.21, by using the notion
of q-kernel.
 62

Proof. Let us prove Theorem 7.20. We have:

∑

k≥1
 1
[k] = ∑

k≥1
 1
(X qk − X) = ∑

k≥1
 1
X qk(1 − ( 1
X )qk−1)

= ∑

k≥1
 1
X qk ∑

j≥0 ( 1
X )j(qk−1) = 1
X
 ∑

k≥1, j≥0
( 1
X )(j+1)(qk−1)

= 1
X
 ∑

k≥1, j≥1
 1
X j(qk−1) = 1
X
 ∑

n≥1 a(n)X −n,

where a(n) is the number (modulo the characteristic p) of decompositions of
the integer n as n = j(qk − 1), with k ≥ 1 and j ≥ 1, i.e.,

a(n) = ∑

k≥1, (qk−1)|n 1.

Clearly the series ∑

k≥1
 1
[k] is transcendental over Fq(X) if and only if the

series X ∑

k≥1 1
[k] is transcendental. Suppose that the series ∑

n≥1 a(n)X −n is
algebraic over Fq(X). This implies that the sequence (a(n))n∈N is q-automatic
and in particular that the subsequence a((qn − 1))n∈N is ultimately periodic.
This assertion leads to a contradiction.
Indeed, it is easily seen that qk − 1 divides qn − 1 if and only if k divides
n. We thus have
 a(qn − 1) = ∑

k≥1, (qk−1)|(qn−1) 1 = ∑

k≥1, k|n 1.

The subsequence a((qn − 1))n∈N is supposed to be ultimately periodic. Thus
there exist n0 ≥ 1 and T ≥ 1 such that:

∀n ≥ n0, ∑

k≥1, k|n 1 = ∑

k≥1, k|n+T 1 mod p.

This implies

∀n ≥ n0, ∀µ ∈ N, ∑

k≥1, k|n 1 = ∑

k≥1, k|n(1+µT ) 1 mod p.

63

By the primes in arithmetic progression theorem, there exists a prime number
ω > n0 and such that ω = 1 + µT for some integer µ. Then for n = ω
∑

k≥1, k|ω 1 = ∑

k≥1, k|ω2 1 mod p,

i.e., 2 = 3 mod p,

which is the desired contradiction.

Exercise 7.24 Let us give another proof of this result which does not involve
the primes in arithmetic progression theorem. This very nice proof is due to
Mend`es France and Yao ([52]).

1. Prove that for any positive integers u, v, w, the number qw − 1 divides
qu(qv − 2) + 1 if and only if w divides the greatest common divisor of
u and v.

2. Deﬁne the sequence au = (a(qun + 1))n∈N, for a ﬁxed positive integer
u. Let u, v be two distinct positive integers. Let h be the smallest
integer such that h divides u and h does not divide v. Prove that
au(qh − 2) − av(qh − 2) ≡ 1.

3. Deduce from this the transcendence of ∑

n≥1 a(n)X −n.

4. Prove similarly the following theorem [52].

Theorem 7.25 Let (nk)k∈N be a sequence of elements of Fq which is not
ultimately equal to zero. The formal power series ∑

k≥1 nk
[k] is transcendental
over Fq(X).

7.6 Complexity and Frequencies

Recall that automatic sequences (and more generally substitutive sequences)
have a strong underlying structure with respect to the complexity, as ex-
pressed by the following properties.

Theorem 7.26 1. The complexity of a ﬁxed point of a primitive substi-
tution [57] or of a ﬁxed point of a substitution of constant length [30]
satisﬁes ∀n, p(n) ≤ Cn.

64

2. The complexity of a substitution ﬁxed point satisﬁes [40, 56]

∀n, p(n) ≤ Cn
2.

This disproves the automaticity of a high complexity sequence. Note that
automatic sequences have rather similar complexity functions but very dis-
similar spectral properties (see for instance [57]).
Let us review some results on the frequencies of factors of a ﬁxed point of
a substitution of constant length. For general results in the case of primitive
substitutions, see [49, 57]. Recall in particular that for such sequences the
frequencies exist and are strictly positive.
The following equirepartition result holds for frequencies of factors of
primitive substitutions of constant length (see [35]).

Theorem 7.27 Let σ be a primitive substitution of constant length. There
exist C2 > C1 > 0 such that
 C1 ≤ nf (w) ≤ C2,

for all n ≥ 1 and all factors w of length n.

One proves the following result by applying the properties of stochastic
matrices to the n-th power of the matrix of the substitution divided by ln,
where l denotes the length of the substitution (see [30, 49, 57]).

Theorem 7.28 If the frequencies of the factors of an automatic sequence
exist, they are rational. Furthermore, if the corresponding substitution is
primitive, then the frequencies exist.

In particular, a Sturmian sequence cannot be automatic.
Cobham gives more precise results for automatic sequences with a letter
of 0 frequency [30]. In particular we have the following result which can be
considered as a criterion for testing the automaticity.

Theorem 7.29 Let u be an automatic sequence and let a be a letter which
occurs in u inﬁnitely often with 0 frequency. Then the gaps beween successive
occurrences of a in u satisfy

lim supn→+∞ αn+1
αn > 1,

where αn denotes the index of the n-th occurrence of a in the sequence u

65

Exercise 7.30 Apply Theorem 7.29 to the characteristic sequence of the set
of squares (see also Exercise 7.16).

Remark 7.31 Yao produces in [74] non-automaticity criteria motivated by
a transcendence criterion due to de Mathan (see [33]). Note that Koskas
gives a proof using automata of this last criterion in [50].

8 Conclusion

Let us conclude this lecture by discussing the connections between Sturmian
sequences and automatic sequences (Section 8.1), and more generally between
sequences of sub-aﬃne complexity and substitutions (Section 8.2).

8.1 Automaticity and Sturmian sequences

Shallit introduces in [64] a measure of automaticity of a sequence u over a
ﬁnite alphabet: the k-automaticity of u, A
k
u(n), is deﬁned as the smallest
possible number of states in any deterministic ﬁnite automaton which gen-
erates the preﬁx of size n of this sequence. (By Christol, Kamae, Mend`es
France and Rauzy’s theorem a sequence has a ﬁnite measure of automaticity
if and only if this sequence is automatic.) This measure tells quantitatively
how “close” a sequence is to being k-automatic.

Remark 8.1 The automaton is fed with the digits i, starting from the least
signiﬁcant digit: there are languages of low automaticity whose mirror image
has high automaticity (see [47]).

A sequence can fail to be k-automatic if all the sequences in the k-kernel
are distinct. A sequence is said to be maximally diverse if the subsequences
{(u(kn + r))n∈N : k ≥ 1, 0 ≤ r ≤ k − 1} are all distinct. Shallit proves
in [64] that Sturmian sequences are maximally diverse, which shows that
they are very far from being automatic, even when they are ﬁxed points of
substitution. More precisely, he deduces from the three distance theorem a
measure of automaticity for some Sturmian sequences [64].

Theorem 8.2 Let 0 < α < 1 be an irrational number with bounded partial
quotients. Let un = ⌊(n + 1)α⌋ − ⌊nα⌋, for n ≥ 1. The automaticity of the
sequence (un)n≥1 has the same order of magnitude as n
1/5.

66

8.2 Sub-aﬃne Complexity

Numerous combinatorial, ergodic or arithmetical properties hold in the case
of a sub-aﬃne complexity function. Consider a dynamical system generated
by a minimal sequence with sub-aﬃne complexity. Ferenczi proves in [42]
the absence of strong mixing. Boshernitzan produces in [17, 19] an explicit
upper bound for the number of ergodic measures. He proves furthermore
that the following conditions imply the unique ergodicity [17, 19]:

lim inf
n→+∞ p(n)
n < 2, or lim sup
n→+∞ p(n)
n < 3.

Furthermore Ferenczi deduces from Theorem 4.9 the following result [42]:
a symbolic dynamical system generated by a minimal sequence of sub-aﬃne
complexity is generated by a ﬁnite number of substitutions (such a system
is called S-adic following Vershik’s terminology). One thus explicitely knows
S-adic expansions of Sturmian sequences or of Arnoux-Rauzy sequences [11].
The reciprocal of this result is false. Consider indeed a substitution of
quadratic complexity: it thus provides a counter-example.
The question of ﬁnding a characterization of sequences of sub-aﬃne com-
plexity in terms of S-adic expansions remains open. Note that Durand gives
in [38] a suﬃcient (but not necessary) condition for a S-adic sequence to have
sub-aﬃne complexity.

References

[1] R. L. Adler, A. G. Konheim, M. H. Mcandrew, Topological Entropy,
Trans. Amer. Math. Soc. 114, pp. 309–319 (1965).

[2] P. Alessandri, Codages de Rotations et Basses Complexit´es, Universit´e
Aix-Marseille II, Th`ese (1996).

[3] P. Alessandri, V. Berth´e, Three Distance Theorems and Combinatorics
on Words, Enseig. Math. 44, pp. 103–132 (1998).

[4] J.-P. Allouche, Somme des Chiﬀres et Transcendence, Bull. Soc. math.
France 110, pp. 279–285 (1982).

[5] J.-P. Allouche, Automates Finis en Th´eorie des Nombres, Expo. Math.,
5, pp. 239–266 (1987).
 67

[6] J.-P. Allouche, Note sur un Article de Sharif et Woodcock, S´eminaire de
th´eorie des Nombres de Bordeaux, S´erie II, 1, pp. 631–633 (1989).

[7] J.-P. Allouche, Sur la Transcendance de la S´erie Formelle Π, S´eminaire
de Th´eorie des Nombres de Bordeaux 2, pp. 103-117 (1990).

[8] J.-P. Allouche, Sur la Complexit´e des Suites Inﬁnies, Bull. Belg. Math.
Soc. 1, pp. 133–143 (1994).

[9] J.-P. Allouche, M. Mend`es France, Automata and Automatic Sequences,
Actes de l’´Ecole de Physique Th´eorique des Houches: “Beyond qua-
sicrystals”, Les ´Editions de Physique, Springer, pp. 293–367 (1995).

[10] J.-P. Allouche, F. von Haeseler, H.-O. Peitgen, G. Skordev, Linear Cellu-
lar Automata, Finite Automata and Pascal’s Triangle, Discrete Applied
Mathematics 66, pp. 1–22 (1996).

[11] P. Arnoux, G. Rauzy, Repr´esentation G´eom´etrique de Suites de Com-
plexit´e 2n + 1, Bull. Soc. Math. France 199, pp. 199–215 (1991).

[12] J. Berstel, Recent Results in Sturmian Words, Developments in Lan-
guage Theory II (DLT’95) (Dassow, Rozenberg, Salomaa eds) World
Scientiﬁc, pp. 13–24 (1996).

[13] V. Berth´e, Entropy in Deterministic and Random Systems, Actes de
l’´Ecole de Physique Th´eorique des Houches: “Beyond quasicrystals”,
Les ´Editions de Physique, Springer, pp. 441–463 (1995).

[14] V. Berth´e, Fr´equences des Facteurs des Suites Sturmiennes, Theoret.
Comput. Sci. 165, pp. 295–309 (1996).

[15] V. Berth´e, N. Chekhova, S. Ferenczi, Covering Numbers: Arithmetics
and Dynamics for Rotations and Interval Exchanges, J. Anal. Math., to
appear.

[16] P. Billingsley, Ergodic Theory and Information, John Wiley and Sons,
New York (1965).

[17] M. Boshernitzan, A Unique Ergodicity of Minimal Symbolic Flows with
Linear Block Growth, J. Anal. Math. 44, pp. 77–96 (1984).

68

[18] M. Boshernitzan, A Condition for Minimal Interval Exchange Maps to
be Uniquely Ergodic, Duke Math. J. 52, pp. 723–752 (1985).

[19] M. Boshernitzan, A condition for unique ergodicity of minimal symbolic
ﬂows, Ergodic Theory Dynam. Sys. 12, pp. 425–428 (1992).

[20] S. Brlek, Enumeration of Factors in the Thue-Morse Word, Discr. Appl.
Math. 24, pp. 83–96 (1989).

[21] T. C. Brown, Descriptions of the Characteristic Sequence of an Irra-
tional, Canad. Math. Bull 36, pp. 15–21 (1993).

[22] V. Bruy`ere, G. Hansel, C. Michaux, Logic and p-Recognizable Sets of
Integers, Bull. Belg. Math. Soc. 1, pp. 191–238 (1994).

[23] J. Cassaigne, Special Factors of Sequences with Linear Subword Com-
plexity, Developments in Language Theory II (DLT’95) (Dassow, Rozen-
berg, Salomaa eds) World Scientiﬁc, pp. 25–34 (1996).

[24] J. Cassaigne, Complexit´e et Facteurs Sp´eciaux, Bull. Belg. Math. Soc.
4, pp. 67–88 (1997).

[25] J. Cassaigne, Sequences with Grouped Factors, Developments in Lan-
guage Theory III (DLT’97), Publications of the Aristotle University of
Thessaloniki, pp. 211–222 (1998).

[26] N. Chekhova, Covering Numbers of Rotations, Theoret. Comput. Sci.,
to appear.

[27] G. Christol, Ensembles presque P´eriodiques k-Reconnaissables, Theoret.
Comp. Sci. 9, pp. 141–145 (1979).

[28] G. Christol, T. Kamae, M. Mend`es France, G. Rauzy, Suites Alg´ebriques,
Automates et Substitutions, Bull. Soc. Math. France 108, pp. 401-419
(1980).

[29] A. Cobham, On the Base Dependence of Sets of Numbers Recognisable
by Finite Automata, Math. Systems Theory 3, pp. 186–192 (1969).

[30] A. Cobham, Uniform Tag Sequences, Math. Systems Theory 6, pp. 164–
192 (1972).
 69

[31] E. M. Coven, G. A. Hedlund, Sequences with Minimal Block Growth,
Math. Systems Theory 7, pp. 138–153 (1973).

[32] N. G. de Bruijn, A Combinatorial Problem, Rominklijke Netherland
Academic Van Wetenschepen Proc. 49 Part. 20, pp. 758–764 (1946).

[33] B. de Mathan, Irrationality Measures and Transcendence in Positive
Characteristic, J. Number Theory 54, pp. 93–112 (1995).

[34] F. M. Dekking, On the Prouhet-Thue-Morse Measure, Acta Universitatis
Carolinae, Mathematica et Physica 33, pp. 35–40 (1992).

[35] P. Deligne, Int´egration sur un Cycle ´Evanescent, Invent. Math. 76,
pp. 129–143 (1984).

[36] G. Didier, Caract´erisation des N- ´Ecritures et Applications `a l’ ´Etude des
Suites de Complexit´e Ultimement n + cste, Theoret. Comput. Sci. 215,
pp. 31–49 (1999).

[37] F. Durand, A Characterization of Substitutive Sequences using Return
Words, Discrete Math. 179, pp. 89–101 (1998).

[38] F. Durand, Linearly Recurrent Subshifts, Ergod. Theory Dynam. Sys.,
to appear.

[39] S. Eilenberg, Automata, Languages, and Machines, Vol. A Academic
Press (1974).

[40] A. Ehrenfeucht, K. P. Lee, G. Rozenberg, Subwords of various classes
of deterministic developmental languages without intercations, Theoret.
Comput. Sci. 1 (1975), 59–75.

[41] S. Ferenczi, Les Transformations de Chacon : Combinatoire, Structure
G´eom´etrique, Lien avec les Syst`emes de Complexit´e 2n + 1, Bull. Soc.
math. France 123, pp. 271–292 (1995).

[42] S. Ferenczi, Rank and Symbolic Complexity, Erg. Theory Dynam. Sys.
16, pp. 663–682 (1996).

[43] S. Ferenczi, Complexity of Sequences and Dynamical Systems, Discrete
Math., to appear.
 70

[44] J. Fresnel, M. Koskas, B. de Mathan, Automata and Transcendence in
Positive Characteristic, J. Number Theory, to appear.

[45] C. Frougny, Number Representation and Finite Automata, this volume.

[46] H. Furstenberg, Algebraic Functions over Finite Fields, J. Algebra 7,
pp. 271–277 (1967).

[47] I. Glaister, J. Shallit, Automaticity III: Polynomial Automaticity and
Context-Free Languages (extended abstract), Mathematical foundations
of Computer Science 1996 (Cracow), Lecture Notes in Comput. Sci.
1113, pp. 382–393 (1996).

[48] T. Harase, Algebraic Elements in Formal Power Series Rings, Israel J.
Math. 63, pp. 281–288 (1988).

[49] B. Host, Substitutions and Bratelli Diagrams, this volume.

[50] M. Koskas, Complexit´e de Suites, Fonctions de Carlitz, University of
Bordeaux I, Thesis (1995).

[51] J. H. Loxton, A. J. van der Poorten, Arithmetic Properties of Automata:
Regular Sequences, J. Reine Angew. Math. 392, pp. 57–69 (1988).

[52] M. Mend`es France, J. Y. Yao, Transcendence and the Carlitz-Goss
Gamma Function, J. Number Theory 63, pp. 396–402 (1997).

[53] M. Misiurewicz, A short proof of the variational principle for a Z
n
+ action
on a compact space, Int. Conf. Dyn. Systems in Math. Physics, Soci´et´e
Math´ematique de France, Ast´erisque 40, pp. 147–158 (1976).

[54] M. Morse, G. A. Hedlund, Symbolic Dynamics, Amer. J. Math. 60,
pp. 815–866 (1938).

[55] M. Morse, G. A. Hedlund, Symbolic Dynamics II: Sturmian Trajectories,
Amer. J. Math. 62, pp. 1–42 (1940).

[56] J.-J. Pansiot, Complexit´e des facteurs des mots inﬁnis engendr´es par
morphismes it´er´es, Lecture Notes in Comput. Sci. 172, pp. 380–389
(1984).
 71

[57] M. Queﬀ´elec, Substitution Dynamical Systems. Spectral Analysis, Lec-
ture Notes in Math. 1294, Springer-Verlag (1987).

[58] G. Rauzy, Suites `a Termes dans un Alphabet Fini, S´em. de Th´eorie des
Nombres de Bordeaux, 25-01–25-16 (1983).

[59] G. Rauzy, Low Complexity and Geometry, Dynamics of Complex Inter-
acting Systems (Santiago, 1994), 147–177, Nonlinear Phenom. Complex
Systems, 2, Kluwer Acad. Publ., Dordrecht (1996).

[60] R. Ritchie, Finite automata and the set of squares, J. Assoc. Comput.
Mach. 10, pp. 528–531 (1963).

[61] G. Rote, Sequences with Subword Complexity 2n, J. Number Theory 46,
pp. 196–213 (1994).

[62] O. Salon, Suites Automatiques `a Multi-indices et Alg´ebricit´e, C. R. Acad.
Sci. Paris, S´erie I 305, pp. 501–504 (1987).

[63] O. Salon, Suites Automatiques `a Multi-indices, S´eminaire de Th´eorie des
Nombres, Expos´e 4, 1986-1987.

[64] J. Shallit, Automaticity IV: Sequences, Sets, and Diversity, J. Th´eor.
Nombres Bordeaux 8, pp. 347–367 (1996).

[65] C. E. Shannon, A Mathematical Theory of Communication, Bell System
Tech. J. 27, pp. 379–423, 623–656 (1948).

[66] H. Sharif, C. F. Woodcock, Algebraic Functions over a Field of Positive
Characteristic and Hadamard Products, J. Lond. Math. Soc. 37, pp. 395–
403 (1988).

[67] V. T. S´os, On the Theory of Diophantine Approximations I, Acta Math.
Acad. Sci. Hungar. 8, pp. 461–472 (1957).

[68] V. T. S´os, On the Distribution mod 1 of the Sequence nα, Ann. Univ.
Sci. Budapest, E¨otv¨os Sect. Math. 1, pp. 127–134 (1958).

[69] J. Sur´anyi, ¨Uber die Anordnung der Vielfachen einer reellen Zahl mod
1, Ann. Univ. Sci. Budapest, E¨otv¨os Sect. Math. 1, pp. 107–111 (1958).

72

[70] S. ´Swierczkowski, On Successive Settings of an Arc on the Circumference
of a Circle, Fundamenta Math. 46, pp. 187–189 (1958).

[71] D. S. Thakur, Automata and Transcendence, Contemporary Mathemat-
ics, 210, pp. 387–399 (1998).

[72] L. J. Wade, Certain Quantities Transcendental over GF (pn, x), Duke
Math. J. 8, pp. 701-720 (1941).

[73] P. Walters, An Introduction to Ergodic Theory, Graduate Texts in Math-
ematics 79.

[74] J.-y. Yao, Crit`eres de non-automaticit´e et leurs applications, Acta Arith.
80 (1997), 237–248.
 73
