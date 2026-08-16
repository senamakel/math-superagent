<!-- source: https://arxiv.org/pdf/2005.00530 | converted from PDF -->

arXiv:2005.00530v3  [math.CO]  11 Jan 2022
A RANDOM ANALOGUE OF GILBREATH’S CONJECTURE

ZACHARY CHASE

Abstract. A well-known conjecture of Gilbreath, and independently Proth from
the 1800s, states that if a0,n = pn denotes the nth prime number and ai,n =
|ai−1,n − ai−1,n+1| for i, n ≥ 1, then ai,1 = 1 for all i ≥ 1. It has been postulated
repeatedly that the property of having ai,1 = 1 for i large enough should hold for
any choice of initial (a0,n)n≥1 provided that the gaps a0,n+1 − a0,n are not too
large and are suﬃciently random. We prove (a precise form of) this postulate.

1. Introduction

Given any sequence of non-negative integers (an)n≥1, we can form the sequence of
non-negative integers (|an − an+1|)n≥1. Start with the primes as the initial sequence
and iterate this consecutive diﬀerencing procedure. Gilbreath’s conjecture is that
the ﬁrst term in every sequence, starting with the ﬁrst iteration, is a 1. Precisely,
if a0,n = pn for n ≥ 1 and ai,n = |ai−1,n − ai−1,n+1| for i, n ≥ 1, then ai,1 = 1 for all
i ≥ 1. Below are the ﬁrst few terms of the ﬁrst few iterations.

2 3 5 7 11 13 17
1 2 2 4 2 4
1 0 2 2 2
1 2 0 0
1 2 0
1 2
1

Proth [6] discussed Gilbreath’s conjecture in 1878, before Gilbreath independently
made the conjecture. Many sources claim Proth asserted he had a proof of the
conjecture, and that his proof was wrong. However, we believe this claim is baseless.
See Section 7 for more details. Odlyzko [3] veriﬁed Gilbreath’s conjecture for 1 ≤
i ≤ π(1013) ≈ 3.34 × 1011. One is led to wonder how special the primes are in
Gilbreath’s conjecture and whether any sequence beginning with 2 followed by an
increasing sequence of odd numbers with small and “random” gaps between them
will have ﬁrst term 1 from some iteration onwards.

Date: May 1, 2020.
The author is partially supported by Ben Green’s Simons Investigator Grant 376201 and grate-
fully acknowledges the support of the Simons Foundation.

1

Odlyzko, at the end of Section 2 of [3], speculates that such a random sequence
indeed will have ﬁrst term 1 from some iteration onwards. Additionally, Problem 68
of [2] asks what gap or density properties of an initial sequence suﬃces to ensure the
conclusion of Gilbreath’s conjecture. Despite Gilbreath’s conjecture being around
for over a decade and several additional sources postulating that the conjecture
should hold for initial sequences with small and random gaps, as of date, nothing has
actually been proven along these lines, nor about Gilbreath’s conjecture speciﬁcally.

In this paper, we initiate a rigorous study of Gilbreath’s conjecture by proving a
random analogue of it.

Theorem 1. Let f : N → N be an increasing function with f (M) ≤ 1
100 log log M
log log log M
for M large and f (M) ≥ 2 for all M ≥ 1. Let a1, a2, . . . be a random inﬁnite
sequence formed as follows. Let a1 = 2, a2 = 3, and for n ≥ 2, an+1 = an + 2un,
where un is drawn uniformly at random from {0, 1, . . . , f (n) − 1}, independent of
the other ui’s. Then, with probability 1, there is some M0 so that for all M ≥ M0,
after M iterations of consecutive diﬀerencing, the ﬁrst term of the sequence is a 1.

Computations suggest that Gilbreath’s conjecture holds because 0s and 2s form to
the right of the leading 1 early on. We prove Theorem 1 by showing that our random
initial sequence indeed has that property almost surely. Since the ﬁrst iteration is
1, 2u2, 2u3, . . . , if we ignore the leading 1 and divide by 2, what we wish to show is
encapsulated by the following theorem, which is the heart of the paper.

Theorem 2. For M large, for any C with 2 ≤ C ≤ 1
100 log log M
log log log M , if we form an
initial sequence of length M by choosing numbers from {0, . . . , C − 1} independently
and uniformly at random, then, with probability at least 1 − e
−e 20√log M , after e 5√log M

iterations of consecutive diﬀerencing, everything is a 0 or 1.

The randomness in Theorem 2 is certainly necessary. For example, if the initial
sequence consists of only 0s and 3s, then after any number of iterations, everything
is still a 0 or 3. However, there are more exotic examples of initial sequences
2 0 6 0 2 2 6 5 0 0 6 1 3 2 2 3 0 6 0 5
2 6 6 2 0 4 1 5 0 6 5 2 1 0 1 3 6 6 5
4 0 4 2 4 3 4 5 6 1 3 1 1 1 2 3 0 1
4 4 2 2 1 1 1 1 5 2 2 0 0 1 1 3 1
0 2 0 1 0 0 0 4 3 0 2 0 1 0 2 2
2 2 1 1 0 0 4 1 3 2 2 1 1 2 0
0 1 0 1 0 4 3 2 1 0 1 0 1 2
1 1 1 1 4 1 1 1 1 1 1 1 1
0 0 0 3 3 0 0 0 0 0 0 0
for which all future iterations have only 0s and 3s (say). These exotic examples
1

suggest that we are far away from a proof of Gilbreath’s conjecture.

1To clarify, in the setting in which the primes are the initial sequence, the analogous situation
to having only 0s and 3s is having only 0s and 6s past the ﬁrst index, making the ﬁrst index very
likely to repeatedly change from 1 to 5 (see Lemma 3.5), thereby violating Gilbreath’s conjecture.
2

2. A General Bootstrapping Argument

In this section, we prove a result about random walks on regular directed graphs
that will be of use to proving Theorem 2.

Deﬁnition 2.1. A directed graph is regular if there is a positive integer d such that
each vertex has in-degree and out-degree equal to d. We allow our graphs to have
self-loops (but no multiple edges). For our discussion, a simple random walk on a
regular directed graph of degree d is formed by choosing a starting point uniformly
at random, and then walking along the directed edges, with each out-edge chosen
with probability 1/d, independent of the previous steps.

Proposition 2.2. Let G = (V, E) be a regular directed graph. Suppose V is red-
blue colored such that the probability a simple random walk on G of length L consists
entirely of red vertices is at least c. Then the probability a simple random walk on
G of length ⌊(1 + 1
10c2)L⌋ consists entirely of red vertices is at least 1
10 c2.

Proof. Let X1, X2, . . . denote the steps of a simple random walk. Deﬁne functions
w1, . . . , wL on V by wj(v) := Pr(X1, . . . , XL all red|Xj = v). Note (by, e.g., induc-
tion on the number of steps) the regularity assumption implies

wj(v) = |V | Pr(X1, . . . , XL all red, Xj = v).

Thus, for any j, letting wj(V ) := ∑

v∈V wj(v),

we have by assumption

wj(V ) = ∑

v |V | Pr(X1, . . . , XL all red, Xj = v)

= |V | Pr(X1, . . . , XL all red)

≥ c|V |.

Let K = ⌈ 3
c2 ⌉, and let k1, . . . , kK be kj := ⌊ j
K L⌋. By Cauchy-Schwarz,
(∑

v
 ∑

j wkj (v)
)2 ≤
 [
∑

v 12]
 ·
 


∑

v
 (∑

j wkj (v)
)2

(1)
 = |V |
 [
∑

j
 ∑

v wkj (v)2 + 2 ∑

j<j′
 ∑

v wkj (v)wkj′ (v)
]
 .

Note, since ||wj||∞ ≤ 1, we have
∑

j
 ∑

v wkj (v)2 ≤ ∑

j
 ∑

v wkj (v) = ∑

j |V | Pr(X1, . . . , XL all red) ≤ K|V |;

also, ∑

v
 ∑

j wkj (v) = ∑

j wkj (V ) ≥ Kc|V |.

3

So (1) implies
 K 2c2|V |2 ≤ |V |
 [

K|V | + 2 ∑

j<j′
 ∑

v wkj (v)wkj′ (v)
]
 ,

and thus, since K 2c2|V | − K|V | is increasing in K for K ≥ 3/c2,
6
c2 |V | ≤ 2 ∑

j<j′
 ∑

v wkj (v)wkj′ (v).

By the pigeonhole principle, there are j < j′ with
∑

v wkj (v)wkj′ (v) ≥ 1
K 2 3
c2 |V |.

Usingkj (v) ≤ Pr(Xkj +1, . . . , XL all red|Xkj = v) = Pr(Xkj′ +1, . . . , XL+kj′ −kj all red|Xkj′ = v),

which is true merely due to translation invariance of the random walk, and

wkj′ (v) ≤ Pr(X1, . . . , Xkj′ all red|Xkj′ = v),

we obtain
1

K 2 3
c2 |V | ≤ ∑

v Pr(X1, . . . , Xkj′ all red|Xkj′ = v) Pr(Xkj′ +1, . . . , XL+kj′ −kj all red|Xkj′ = v)

= |V | ∑

v Pr(X1, . . . , Xkj′ all red, Xkj′ = v) Pr(Xkj′ +1, . . . , XL+kj′ −kj all red|Xkj′ = v)

= |V | ∑

v Pr(X1, . . . , XL+kj′ −kj all red, Xkj′ = v)

= |V | Pr(X1, . . . , XL+kj′ −kj all red),

yielding
 Pr(X1, . . . , XL+kj′ −kj all red) ≥ 1
K 2 3
c2 .

Note K ≤ 3
c2 + 1 ≤ 4
c2 , so 1
K 2 3
c2 ≥ 3
16 c2 ≥ 1
10c2. Since the proposition is trivial if
L < 10/c2, we may assume L ≥ 10/c2 to obtain kj′ −kj ≥ L
K −1 ≥ c2
4 L−1 ≥ c2
10L. □

Remark. It is natural to think that Proposition 2.2 can be extended, in some form,
to arbitrary length increases. However, such an extension is not possible in general
(note that iterating Proposition 2.2 results in only a summable geometric series of
length increases). For example, consider V = {1, . . . , n}, E = {(1 ↦→ 2), . . . , (n−1 ↦→
n), (n ↦→ 1)} with the vertices {1, . . . , 1
10 n} colored red and the rest blue. Then with
L = 1
20n and c = 1
20 , it holds that a simple random walk on G of length L will hit
only red vertices with probability at least c. However, of course no simple (random)
walk on G of length 5L = 1
2n will hit only red vertices.

Examples of such “bad” colorings also exist on the graph we apply Proposition
2.2 to, namely a Debrujin graph. We don’t think these colorings are actually the
ones we need to address in our proof of Theorem 2, but we couldn’t prove that.

4

3. A Lower Bound for Ending with 0

We begin by exploiting the main property of the “dynamical system” of taking
consecutive diﬀerences: the supremum never increases. In fact, we use that it quickly
decreases provided there is no trivial obstruction to it doing so (Lemma 3.2).

Deﬁnition 3.1. We say non-negative integers a1, . . . , ai come from ̃a1, . . . , ̃ai+1 if
|̃aj − ̃aj+1| = aj for each 1 ≤ j ≤ i. Given a1, . . . , ai and a subset E ⊆ Z, an E-block
is a contiguous set of terms aj1+1, . . . , aj′
1 such that aj ∈ E for each j1 + 1 ≤ j ≤ j′
1;
the length of the block is j′
1 − j1.

Lemma 3.2. Let a1, . . . , ai be non-negative integers with d := maxj aj. Let L denote
the length of the longest {0, d}-block containing at least one d. If L ≤ i − 1, then,
after L iterations of consecutive diﬀerencing, the largest number is at most d − 1.

Proof. We induct on L. For L = 1, the result is clear. Assume L ≥ 2 and the result
is true for all L
′ < L. It is easy to see that, since d is the maximum, any {0, d}-block
containing a d after an iteration would have had to have come from a {0, d}-block
of greater length containing a d, so the longest {0, d}-block containing a d after one
iteration is at most L − 1, say L
′. By induction, after L
′ more iterations, the largest
number is at most d −1. It follows that after L (total) iterations, the largest number
is at most d − 1. □

So, to prove Theorem 2, “all” we need to do is argue that long {0, d}-blocks
are unlikely to exist. In this next lemma, we observe that any large {0, d}-block
essentially must have come from a block with no 0s.

Lemma 3.3. Suppose that after i iterations, there is a dZ-block of length L. Then
either there was a dZ-block of length L + i in the initial sequence, or there is some
i
′, 0 ≤ i
′ ≤ i − 1, such that after i
′ iterations, there is a block of length L + i − i
′

with no 0s.

Proof. We prove by induction on i the statement for all L. For i = 0, the result is
tautological. Take i ≥ 1, and suppose the result holds for i − 1. The dZ-block of
length L had to come from either a dZ-block of length L + 1 or a block of length
L + 1 with no 0s (since everything will have the same residue modulo d), so we are
done by the induction hypothesis. □

Another nice property of the consecutive diﬀerencing operation is that it “com-
mutes” with reducing mod 2. This allows for a decently explicit formula for the
parity of a term after a given number of iterations, merely in terms of the parities
of the initial terms.

Deﬁnition 3.4. For non-negative integers a1, a2, deﬁne f1(a1, a2) = |a1 − a2|, and for
any i ≥ 2 and non-negative a1, . . . , ai+1, deﬁne fi(a1, . . . , ai+1) = |fi−1(a1, . . . , ai) −
fi−1(a2, . . . , ai+1)|. We say a1, . . . , ai+1 ultimately iterate to fi(a1, . . . , ai+1).

Lemma 3.5. For any i ≥ 1, there is a subset Ji ⊆ [i + 1] containing 1 and i + 1 so
that for any non-negative integers a1, . . . , ai+1, fi(a1, . . . , ai+1) ≡ ∑

j∈Ji aj mod 2.
5

Proof. We induct on i. For i = 1, the result follows from |a1 − a2| ≡ a1 + a2 mod 2.
Assume i ≥ 2 and the result is true for i − 1. Note that fi(a1, . . . , ai+1) ≡
|fi−1(a1, . . . , ai) − fi−1(a2, . . . , ai+1)| ≡ fi−1(a1, . . . , ai) + fi−1(a2, . . . , ai+1) ≡∑

j∈Ji−1 aj + ∑

j∈Ji−1 aj+1 ≡ ∑

j∈Ji−1△(Ji−1+1) aj mod 2. By induction, Ji−1 contains
1 and i, and so Ji := Ji−1△(Ji−1 + 1) contains 1 and i + 1, as desired. □

We take a moment to note some useful corollaries of Lemma 3.5 which tells us
that the parity of what a1, . . . , ai+1 ultimately iterate to depends linearly on each
of the parities of a1 and ai+1. For example, let a1, . . . , ai+1 be drawn independently,
uniformly at random from {0, . . . , C − 1}. Then, the probability a1, . . . , ai+1 ulti-
mately iterate to an even integer is between 1
3 and 2
3. And the probability that, for
j = i/2 say, all of fj(at, . . . , at+j) are even, for t = 1, . . . , i/2, is exponentially small
in i/2.

Let [C]0 = {0, . . . , C − 1}.

The following proposition shows that 0s are not too rare, which will be useful
in conjuction with Lemma 3.3. Before the proof, we introduce some notation (for
a given C and i). Deﬁne i0 = i and ij+1 = ⌊ ij
100C2 ⌋ for 0 ≤ j ≤ C − 3. For
1 ≤ j ≤ C − 2, let Ej denote the event that after i − ij−1 iterations there’s a
{0, C − j}-block of length (at least) ij−1 − ij. For example, E1 is the event that after
0 iterations, there’s a {0, C − 1}-block of length i − i1, and E2 is the event that after
i − i1 iterations, there’s a {0, C − 2}-block of length i1 − i2.

Proposition 3.6. For any C ≥ 2 and any i ≥ (200C 2)2C, if a1, . . . , ai are chosen
independently and uniformly at random from {0, . . . , C − 1}, then the probability
they ultimately iterate to 0 is at least 1
200C2 .

Proof. Fix C ≥ 2 and i ≥ (200C 2)2C. If C = 2, then Lemma 3.5 gives the result,
so assume C ≥ 3. We may suppose that the desired probability is at most 0.01.
Let B0 denote all i-tuples in [C]i
0 that ultimately iterate to something 0 mod 2; we
say “conditional probability” when speaking of the conditional probability that B0
induces. Then, by Lemma 3.5, the conditional probability of ultimately iterating to
0 is at most 0.03, and so the conditional probability of not having only 0s and 1s
after some iteration is at least 0.97.

Therefore, with conditional probability at least 0.97, some Ej occurs. Indeed,
otherwise, repeated use of Lemma 3.2 shows that after i−iC−2 iterations, everything
is a 0 or a 1: after i − i1 iterations, there are no more (C − 1)s and thus no (C − 1)s
ever again; after i − i2 iterations, there are no more (C − 2)s and thus no (C − 2)s
ever again, etc..

Therefore, by the pigeonhole principle, there is some j, 1 ≤ j ≤ C − 2, such
that Ej occurs with conditional probability at least 0.97
C−2. Clearly j cannot be 1,
since we have the uniform distribution after 0 iterations. Also, j must be such that
C − j is odd, since by Lemma 3.5, the probability of having 2ij evens in a row is

6

at most ( 2
3)2ij ≤ ( 2
3)2(200C2)C (since, as is easy to verify, ij ≥ iC−2 ≥ (200C 2)C for
each j). Since after i − ij−1 iterations, there are only ij−1 indices, a block of length
ij−1 − ij must contain the block [ij + 1, ij−1 − ij] (see ﬁgure 1). So, with conditional
probability at least 0.97
C−2, all indices ij + ∆, for 1 ≤ ∆ ≤ ij−1 − 2ij, will be a 0 or
C − j.

Let a1, . . . , ai be the initial sequence, and note that, after i − ij−1 iterations, none
of the indices ij +∆ depend on a1 or ai (only the ﬁrst and last indices do). Therefore,
by Lemma 3.5, with (unconditional) probability at least 0.30
C−2, all ij + ∆ will be 0 or
C − j. Now, note that after i := i − ij−1 iterations, the integer at any index r is
equal to fi(ar, ar+1, . . . , ar+i).

0 ij ij−1 − ij ij−1 i − ij−1

i − (ij−1 − ij)
i − ij i

0 ij ij−1 − ij ij−1

Figure 1: Indicates which initial indices (in [i]) a particular index after i iterations depends on.

Deﬁne a (regular) directed graph on [C]
i
0 by (x1, . . . , xi) → (x2, . . . , xi, y) for
any x1, . . . , xi, y ∈ [C]0. Color a tuple (x1, . . . , xi) ∈ [C]i
0 “red” if and only if it
ultimately iterates to 0 or C − j. The fact that, with probability at least 0.30
C−2, all
fi(ar, ar+1, . . . , ar+i), for ij + 1 ≤ r ≤ (1 − ǫj)ǫ1 . . . ǫj−1i, are 0 or C − j corresponds
exactly to: with probability at least 0.30
C−2, a simple random walk in [C]i
0 of length
L := ij−1 − 2ij consists entirely of red vertices.

Hence, by Proposition 2.2, with probability at least 1
20C2 a simple random walk of
length
2 (1+ 1
20C2 )L consists entirely of red vertices. Now, (1+ 1
20C2 )L ≥ (1+ 1
40C2 )ij−1
since it is equivalent to 1
40C2 ij−1 ≥ (2 + 1
10C2 )ij, which is true since ij ≤ ij−1
100C2 . We
have thus shown that, if a1, . . . , a(1+ 1
40C2 )ij−1+i are chosen independently and uni-

formly at random from [C]0, then with probability at least 1
20C2 , all fi(ar, . . . , ar+i)
for 1 ≤ r ≤ (1 + 1
40C2 )ij−1 are either 0 or C − j.

We’re nearly done, as (fi(ar, . . . , ar+i))1≤r≤L′ is the whole sequence after i iter-
ations; since C − j is odd, we just need to additionally ensure that the ultimate
iterate is even. Speciﬁcally, we argue as follows.

2To be light on notation, we suppress ceiling and ﬂoor functions in the rest of this section.
7

We now deduce that, for L
′ := ij−1, if a1, . . . , ai are chosen independently and
uniformly at random from [C]0, then with probability at least 1
160C2 , they ulti-
mately iterate to something 0 mod 2 and each fi(ar, . . . , ar+i), for 1 ≤ r ≤ L
′,
are either 0 or C − j. Let δ = 1
40C2 . By Lemma 3.5, the proportion of walks
(X1, . . . , X(1+δ)L′) in [C]i
0 of length (1 + δ)L
′ that have at most δL′
4 values of j ∈ [δL
′]
with
3 (Xj+1, Xj+2, . . . , Xj+L′) ∈ B0 is at most4 δL′
4 ( δL′

δL′/4
)2−δL′ ≤ 1
40C2 . Therefore,
since the proportion of walks (X1, . . . , X(1+δ)L′) with X1, . . . , X(1+δ)L′ all red is at
least 1
20C2 , if we let A denote the walks (X1, . . . , X(1+δ)L′) such that X1, . . . , X(1+δ)L′
are all red and such that there are at least δL′
4 values of j with (Xj+1, Xj+2, . . . , Xj+L′) ∈
B0, then the density of A is at least 1
40C2 . So on one hand,

∑

(X1,...,X(1+δ)L′ )∈A
 δL′
∑

j=1 1(Xj+1,...,Xj+L′ )∈B0 ≥ δL
′

4 1
40C 2 C iC (1+δ)L′−1,

while on another hand,

∑

(X1,...,X(1+δ)L′ )∈A
 δL′
∑

j=1 1(Xj+1,...,Xj+L′ )∈B0 =
 δL′
∑

j=1
 ∑

(Xj+1,...,Xj+L′ )∈B0
 ∑

X1,...,Xj,Xj+L′+1,...,X(1+δ)L′
(X1,...,X(1+δ)L′ )∈A
 1

≤
 δL′
∑

j=1
 ∑

(Xj+1,...,Xj+L′ )∈B0 C δL′1Xj+1,...,Xj+L′ all red

= δL
′C δL′ ∑

(X1,...,XL′ )∈B0 1X1,...,XL′ all red.

We deduce that ∑

(X1,...,XL′ )∈B0 1Xl,...,XL′ all red ≥ 1
160C 2 C iC L′−1,

which is what we wanted to deduce. □

Corollary 3.7. For any C ≥ 2 and any i ≥ 1, if a1, . . . , ai are chosen independently
and uniformly at random from {0, . . . , C − 1}, then the probability they ultimately
iterate to 0 is at least ( 1
C )(200C2)2C .

Proof. For i ≥ (200C 2)2C, Proposition 3.6 yields a lower bound of 1
200C2 , and for
1 ≤ i < (200C 2)2C, we use the trivial lower bound coming from aj = 0 for all j. □

3Here we have abused notation, by associating the i-tuple that Xj+1, . . . , Xj+L′ form with
(Xj+1, . . . , Xj+L′).
4The inequality following this footnote follows from the well known (
n
k) ≤ ( en
k )
k, giving

δL′
4 ( δL′

δL′/4
)
2−δL′ ≤ δL′
4 ( eδL′
δL′/4 )
δL′/42−δL′ < δL′
4 (0.91)
δL′. Note δL′ ≥ 1
40C 2 (200C2)
C .

8

4. Finishing the Proof of Theorem 2

We now ﬁnish the proof of Theorem 2, copied below for the reader’s convenience.

Theorem 2. For M large, for any C with 2 ≤ C ≤ 1
100 log log M
log log log M , if we form an
initial sequence of length M by choosing numbers from {0, . . . , C − 1} independently
and uniformly at random, then, with probability at least 1 − e
−e 20√log M , after e 5√log M

iterations of consecutive diﬀerencing, everything is a 0 or 1.

Fix M large and C in the range [3, 1
100 log log M
log log log M ] (the case C = 2 is trivial). Let
E1 denote
5 the event that after 0 iterations, there is a {0, C − 1}-block of length
R := e 10√log M . Let E2 be the event that after 2R iterations, there is a {0, C −2}-block
of length R2. Let E3 be the event that after 2R2 iterations, there is a {0, C − 3}-
block of length R3. In general, for 2 ≤ j ≤ C − 2, Ej is the event that after 2Rj−1

iterations, there is a {0, C − j}-block of length Rj. Since 2Rj−1 ≥ 2Rj−2 + Rj−1 for
3 ≤ j ≤ C − 1, we see that, as before, by Lemma 3.2, if no Ej occurs, then after
2RC−2 iterations, everything is a 0 or a 1. Note that 2RC−2 ≤ e 5√log M , so it suﬃces
to show that the probability that some Ej occurs is at most e
−e 20√log M . By the union
bound, it suﬃces to show Pr(Ej) ≤ e
−e 13√log M , say, for each 1 ≤ j ≤ C − 2.

Clearly, Pr(E1) ≤ M( 2
3 )R ≤ e
−e 13√log M , so ﬁx some j with 2 ≤ j ≤ C − 2. By
Lemma 3.3, if Ej occurs, either there is a (C − j)Z-block of length Rj in the initial
sequence or there is a block of length Rj in the ﬁrst 2Rj−1−1 iterations containing no
0s. Once again, the ﬁrst option holds with probability at most M( 2
3)Rj ≤ 1
2 e
−e 13√log M ,
so by the union bound, it suﬃces to show that for each 0 ≤ i ≤ 2Rj−1 − 1, the
probability that there is a block of length L := Rj = e
j 10√log M without 0s after i
iterations is at most e
−e 12√log M , say.

So ﬁx some i ∈ [0, 2Rj−1 − 1]. Let b1, . . . , bM −i denote the sequence after i itera-
tions. Let’s ﬁrst focus on the block b1, . . . , bL. Say the initial sequence is a1, . . . , aM .
Note that bk(i+1)+1 = fi(ak(i+1)+1, . . . , a(k+1)(i+1)) for 0 ≤ k ≤ 1
2R − 1. Since
( 1
2R − 1)(i + 1) + 1 ≤ 1
2R(i + 1) ≤ L and the sets {ak(i+1)+1, . . . , a(k+1)(i+1)} are dis-
joint as k ranges, by independence the probability that b1, . . . , bL are all nonzero is at

most (1 − ( 1
C )(200C2)2C )R/2 by Corollary 3.7. Using the standard 1 −x ≤ e
−x, we see

that (1 − ( 1
C )(200C2)2C )R/2 ≤ exp (
− R
2 ( 1
C )(200C2)2C ) ≤ exp (
− R
2 e
−(log C)e5C log C ) ≤

exp (
− R
2 e
−(log log log M )e 1
19 log log M ) ≤ exp (
− R
2 e
− 15√
log M ) ≤ exp (−e 11√log M ). There-
fore, by the union bound, the probability that there is some block of length L after
i iterations containing no 0s is at most Me
−e 11√log M ≤ e
−e 12√log M . The proof is thus
complete. □

5To be light on notation, we suppress ceiling and ﬂoor functions in this section.

9

5. Proof of Theorem 1

In this section we deduce Theorem 1 from Theorem 2. We start with a lemma.

Lemma 5.1. Take M large. Let f : [M] → {2, 3, . . . , ⌊ 1
100 log log M
log log log M ⌋} be an increas-
ing function. Form a random initial sequence b1, . . . , bM by choosing bm uniformly
at random from {0, 1, . . . , f (n) − 1}, independently of the other bi’s. Then, with
probability at least 1 − e
− 1
20 log2 M , after 3 M
log
2 M iterations of consecutive diﬀerencing,
everything is a 0 or 1.

Before proving Lemma 5.1, let’s prove Theorem 1 assuming it.

Proof of Theorem 1. Let AM denote the event that after M iterations, the ﬁrst term
is not a 1. We wish to show that, with probability 1, only ﬁnitely many AM ’s occur.
By Borel-Cantelli, it suﬃces to show that for all M large, the probability of AM
occurring is at most e
− 1
30 log2 M . Note that AM is equivalent to a1, . . . , aM +1 not
ultimately iterating to 1. For M large enough, by Lemma 5.1, with probability at
least 1−e
− 1
20 log2 M , after 3 M
log2 M iterations of consecutive diﬀerencing beginning with
initial sequence u2, . . . , uM , everything is a 0 or 1. Therefore, with probability at
least 1−e
− 1
20 log2 M , after 3 M
log2 M iterations of consecutive diﬀerencing beginning with
initial sequence 2u2, . . . , 2uM , everything is a 0 or 2. It follows that with probability
at least 1−e
− 1
20 log2 M , after 1+3 M
log2 M iterations of consecutive diﬀerencing beginning
with initial sequence a1, . . . , aM +1, the obtained sequence starts oﬀ with an odd
number at most 1
100 log log M
log log log M followed by only 0s and 2s. By Lemma 3.5, with

probability at least 1 − e
− 1
10 log2 M , the second term of the sequence is congruent
to 2 mod 4 at least 1
3 log2 M times out of the log2 M iterations following the (1 +
3 M
log2 M )th iteration. Therefore, with probability at least 1 − e
− 1
20 log2 M − e
− 1
10 log2 M ≥

1 − e
− 1
30 log2 M , starting with a1, . . . , aM +1, after 1 + 3 M
log2 M + log2 M iterations, the
ﬁrst term will be a 1, and therefore will remain a 1 all the way until the ﬁnal (i.e.,
M th) iteration, since everything else is a 0 or 2. □

Deﬁnition 5.2. Let a1, . . . , aM +1 be non-negative integers. We say that an index
i ∈ [M + 1] inﬂuenced the index j ∈ [M + 1 − t] after t iterations if 0 ≤ i − j ≤ t.
Recall that ft(aj, . . . , aj+t) is the value at index j after t iterations.

We ﬁnish by proving Lemma 5.1. The idea of the proof is as follows. By Theorem
2, the blocks on which f is constant will become all 0s and 1s after not too many
iterations. Although there are some indices that were inﬂuenced by indices where
f took diﬀerent values, these indices are contained in not too many not too large
intervals, so we can let all the 0s and 1s drop the values at these “bad indices” with
a few extra iterations.

We start by proving a lemma that allows us to isolate these “bad indices”. For an
interval I ⊆ N, let L(I) and R(I) denote its left and right endpoints, respectively.
10

Lemma 5.3. Suppose M is large, and let CM be a positive integer with CM ≤
log log M. Let I1, . . . , Ir ⊆ [M] be disjoint intervals with r ≤ CM and |It| ≤
CM e 5√log M for each t. Then there are pairwise disjoint intervals J1, . . . , Js ⊆ [M],
each containing some It, such that the following two hold.
• For all t, 1 ≤ t ≤ r, there is some m with It ⊆ Jm.
• For any m, 1 ≤ m ≤ s, if we let Bm denote the smallest interval con-
taining all of the It’s in Jm, then we have that either L(Bm) − L(Jm) ≥
(log2 M)CM |Bm| or R(Jm) − R(Bm) ≥ (log2 M)CM |Bm|, with both being true
if Jm contains neither 1 nor M.

Proof. For a subset A of [r], let BA denote the smallest interval containing ∪t∈AIt,
and let J(A) denote the smallest interval containing ∪t∈AIt such that either L(BA)−
L(J(A)) ≥ (log2 M)CM |BA| or R(J(A))−R(BA) ≥ (log2 M)CM |BA|, with both being
true if J(A) contains neither 1 nor M; if no such interval exists, we let J(A) = ∅. Let
C0 = {J({t}) : 1 ≤ t ≤ r}. For i ≥ 0, if Ci contains two intervals J(A1), J(A2) that
intersect, we deﬁne Ci+1 to be the same as Ci, except we replace J(A1) and J(A2)
with J(A1 ∪ A2) (Ci+1 thus could depend on the choice of intersecting intervals).
Say C0, . . . , Ck−1 are the deﬁned collections. It is clear that k ≤ r and that if each
element of Ck−1 is non-empty, then the elements of Ck−1 satisfy the conditions of
Lemma 5.3. The largest diameter of an interval in C0 is at most (2(log2 M)CM +
1)CM e 5√
log M ≤ 3(log2 M)CM CM e 5√
log M . If J(A1) and J(A2) each have diameter at
most D and intersect, then the diameter of J(A1 ∪ A2) is at most (2(log2 M)CM +
1)(2D) ≤ 6(log2 M)CM D. Therefore, each interval in any Ci−1 has diameter at most
6i−1(log2 M)(i−1)CM 3(log2 M)CM CM e 5√log M ≤ 6r(log2 M)rCM CM e 5√log M ≤ e 4√log M .
To ﬁnish the proof, it just remains to note that J(A) ̸= ∅ if the diameter of ∪t∈AIt
is at most e 4√log M . □

Proof of Lemma 5.1. Do e 5√log M iterations of consecutive diﬀerencing. For 2 ≤ C ≤
1
100 log log M
log log log M =: CM , we say that an index j is C-pure if f took the value C at

all indices in the initial sequence that inﬂuenced j (after e 5√log M iterations). Let I
denote the indices that are not C-pure for any C. Write I = ⊔
r
t=1It as a disjoint
union of intervals with r minimal. Clearly r ≤ CM . Also, crudely, |It| ≤ CM e 5√log M

for each t.

Let J1, . . . , Js be the intervals guaranteed
6 by Lemma 5.3, and let B1, . . . , Bs be
as in Lemma 5.3. For any C, by
7 Theorem 2 applied to the (interval of) C-pure
indices, the probability that all C-pure indices are 0 or 1 is at least 1 − e
−e 20√log M ,

6We are applying Lemma 5.3 with M − e 5√log M instead of M , but all bounds are essentially the
same.
7As stated, Theorem 2 only applies to initial sequences of length M . However, given any shorter
initial sequence, we can independently add elements uniformly chosen from {0, . . . , C −1} to obtain
a sequence of length M , then do e 5√log M iterations, and then truncate the sequence to keep only
indices inﬂuenced by the original initial sequence.
11

and therefore the probability that all indices that are C-pure for some C are 0 or 1
is at least 1 − CM e
−e 20√log M ≥ 1 − e
− 21√log M . In particular, with probability at least
1 − e
− 21√log M , all indices in ∪
s
m=1(Jm \ Bm) are 0 or 1; we from here on condition on
this being the case. For 1 ≤ m ≤ s and 1 ≤ j ≤ CM − 1, let J j
m denote the interval
(of length |Jm| − 2(log2 M)j|Bm|) whose indices after 2(log2 M)j|Bm| iterations past
the e 5√log M th are inﬂuenced by indices only in Jm, and let Bj
m denote the interval (of
length |Bm|+2(log2 M)j|Bm|) whose indices after 2(log2 M)j|Bm| iterations past the
e 5√log M th are inﬂuenced by at least one index in Bm. Note that Lemma 5.3 implies
Bj
m ⊆ J j
m for each 1 ≤ j ≤ CM − 1 (since 2(log2 M)CM −1|Bm| ≤ (log2 M)CM |Bm|).

For 1 ≤ m ≤ s, let E0
m denote the event that there is a {0, CM }-block in Jm
of length (log2 M)|Bm| containing a CM . For 1 ≤ m ≤ s and 1 ≤ j ≤ CM − 2,
let Ej
m denote the event that, after 2(log2 M)j|Bm| iterations (past the e 5√log M th),
there is a {0, CM − j}-block in J j
m of length (log2 M)j+1|Bm| containing a CM − j.
Fix m with 1 ≤ m ≤ s. As in the proofs of Proposition 3.6 and Theorem 2, since
2(log2 M)i+1|Bm| ≥ (log2 M)i+1|Bm|+2(log2 M)i|Bm|, if none of E0
m, E1
m, . . . , ECM −2
m
occur, then after 2(log2 M)CM −1 iterations, the largest number in J CM −1
m is a 1.

Note that any CM ’s in Jm lie in Bm, so by Lemma 3.5, the probability that
E0
m occurs is at most 2( 1
2) 1
2 log2 M , since either to the left or to the right of Bm
must be 1
2 log2 M consecutive 0s. Similarly, the length of the longest {0, CM − j}-
block in J j
m is at most the whole of Bj
m and 0s surrounding it, so the probability
Ej
m occurs is at most 2( 1
2) 1
4 log2 M . Therefore, the probability that at least one of
E0
m, . . . , ECM −2
m occurs is at most 2( 1
2) 1
2 log2 M + (CM − 2)2( 1
2) 1
4 log2 M ≤ e
− 1
10 log2 M .
Since BCM −1
m ⊆ J CM −1
m , if none of E0
m, . . . , ECm−2
m occur, then the elements of (the
growing) Bm became 0 and 1 quickly enough to not aﬀect anything outside of (the
shrinking) Jm. In particular, if none of E0
m, . . . , ECM −2
m occur for any m (i.e. for each
m, none occur), then
8 after 2(log2 M)CM −1 max1≤m≤s |Bm| ≤ 2 M
log2 M iterations past

the e 5√log M th, everything is a 0 or 1. Since the probability at least one Ej
m (over all
j, m) occurs is at most se
− 1
10 log2 M ≤ e
− 1
20 log2 M , Lemma 5.1 is established. □

6. Additional Mathematical Remarks

The proof of Theorem 2 can be relatively easily adapted to handle any distribution
(not just the uniform distribution) on {0, . . . , C −1} that gives not too large, positive
weight to each of 0, . . . , C − 1 (one should create duplicate vertices in [C]
i
0 so that
the obtained simple random walk models this diﬀerent probability distribution).

In Theorem 2 we did not try to optimize e
−e 20√log M nor e 5√log M . A proof allowing
C to go all the way up to log2 M, or even a power of M, would be interesting. We
expect that, in reality, the highest C can go is M, in that if C = o(M), then with

8It is clear from Lemma 5.3 that |Bm| ≤ M
(log2 M)CM for each m.

12

probability 1 − o(1), after M
2 iterations, everything is a 0 or 1, while if C = ω(M),
with probability o(1), after M
2 iterations, everything is a 0 or 1.

7. A Historical Remark

Various sources (websites, blog posts, etc.) have claimed that Proth believed he
had proven Gilbreath’s conjecture, and that his proof turned out to be wrong.

Not only do we currently have no evidence for this claim, the apparent source of
this claim has retracted it.

The claim seemed plausible, for Proth did publish a paper [6] on (what later
became known as) Gilbreath’s conjecture and did, admittedly confusingly, call it a
“theorem”. However, a reading through the paper shows he did not seriously claim
a proof. Indeed, Hugh Williams who made the claim about Proth without reference
[7, p. 123], said “On rereading his actual paper ... I can ﬁnd no support for my
assertion. ... My apologies for seeming to have started a myth” [8].

We also take this time to correct another historical error, which actually is com-
posed of two suberrors. The ﬁrst suberror is that many sources incorrectly cited
[5] when referring to Proth’s discussion of Gilbreath’s conjecture, referring to the
correct title “Th´eor`emes sur les nombres premiers” but citing Comp. Rend. Acad.
Sci. Paris, 85 (1877) instead of Comp. Rend. Acad. Sci. Paris, 87 (1877). The
former actually corresponds to a completely unrelated paper of Pepin [4]. The sec-
ond suberror is that, the intended reference, [5], didn’t even discuss Gilbreath’s
conjecture! We were only able to ﬁnd Proth discussing Gilbreath’s conjecture in [6].

We refer the reader to [1] for more information surrounding all of this.

8. Acknowledgments

I would like to thank my advisor, Ben Green, for suggesting this problem to me
and Daniel Korandi for helpful feedback on the introduction. I would also like to
thank Juan Arias de Reyna for bringing to attention the dubious nature of the
claim discussed in Section 7, and Hugh Williams for kindly responding to emails
and helping resolve the situation.
 References

[1] J. Arias-de-Reyna, Gilbreath’s conjecture, blog post available at
https://institucional.us.es/blogimus/en/2020/07/gilbreaths-conjecture/
[2] H. L. Montgomery, Ten lectures on the interface between analytic number theory and harmonic
analysis, CBMS No. 84, Amer. Math. Soc, Providence, 1994.
[3] A. M. Odlyzko, “Iterated absolute values of diﬀerences of consecutive primes”, Math. Comp.,
61 (1993) 373-380.
[4] F. Pepin, “Sur la formule 22
n + 1”, Comp. Rend. Acad. Sci. Paris, 85 (1877), 329-331.

13

[5] F. Proth, “Th´eor`emes sur les nombres premiers”, Comp. Rend. Acad. Sci. Paris, 87 (1877)
329-331.
[6] F. Proth, “Sur la s´erie des nombres premiers”, Nouvelle Correspondance Math´ematique, 4
(1878) 236-240.
[7] H. C. Williams, Edouard Lucas and Primality Testing, Canad. Math. Soc. Ser. Monogr. Adv.
Texts, Wiley, (1998).
[8] H. C. Williams, Email correspondence (2020).

Mathematical Institute, Andrew Wiles Building, Radcliffe Observatory Quar-
ter, Woodstock Road, Oxford OX2 6GG, UK
Email address: zachary.chase@maths.ox.ac.uk

14
