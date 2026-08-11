<!-- source: https://arxiv.org/pdf/1106.1995 | converted from PDF -->

arXiv:1106.1995v2  [math.CO]  12 Jan 2012
REFINED INVERSION STATISTICS ON PERMUTATIONS

JOSHUA SACK AND HENNING ´ULFARSSON

Abstract. We introduce and study new reﬁnements of inversion sta-
tistics for permutations, such as k-step inversions, (the number of in-
versions with ﬁxed position diﬀerences) and non-inversion sums (the
sum of the diﬀerences of positions of the non-inversions of a permuta-
tion). We also provide a distribution function for non-inversion sums,
a distribution function for k-step inversions that relates to the Euler-
ian polynomials, and special cases of distribution functions for other
statistics we introduce, such as (≤ k)-step inversions and (k1, k2)-step
inversions (that ﬁx the value separation as well as the position). We
connect our reﬁnements to other work, such as inversion tops that are
0 modulo a ﬁxed integer d, left boundary sums of paths, and marked
meshed patterns. Finally, we use non-inversion sums to show that for
every number n > 34, there is a permutation such that the dot product
of that permutation and the identity permutation (of the same length)
is n.
 Contents

1. Introduction 1
2. Non-inversion sums and the dot product of permutations 3
3. Zone-crossing vectors and the distribution of the non-inversion
sum 9
4. The distribution of k-, (k1, k2)-, and (≤ k)-step inversions 14
5. Future work and connections with other work 20
References 27

1. Introduction

The main object of study in this paper is the set of inversions in a permu-
tation.
1 An inversion in a permutation π, of rank n, is a pair (a, b) satisfying
1 ≤ a < b ≤ n and π(a) > π(b). All other pairs are called non-inversions.
We are particularly interested in permutation statistics related to inversions,
such as the number of inversions of a certain form. The study of permutation
statistics was largely initiated by the seminal MacMahon [6], but has seen

Date: Updated: October 29, 2018.
Sack was partly supported by grant no. 100048021 from the Icelandic Research Fund.
´Ulfarsson was supported by grant no. 090038011 from the Icelandic Research Fund.
1We provide basic deﬁnitions at the end of this introduction.

2 SACK AND ´ULFARSSON

explosive growth in recent decades. In Section 2 we introduce the concept of
the non-inversion sum of a permutation. This is the sum of the diﬀerences
b − a for all non-inversions (a, b) in the permutation. Before studying the
distribution of this statistic we connect these non-inversion sums to another
known statistic on permutations: the dot product with a ﬁxed vector. In
particular, the dot product of the permutation (treated as a vector) with
the identity permutation of the same length is equal to the non-inversion
sum of the permutation plus a function of the rank of the permutation; see
Theorem 2.5.
In Section 3, we deﬁne the distribution function for the non-inversion sum
and prove a recurrence relation for it in Theorem 3.8. We introduce the
concept of a zone-crossing vector, which appears in the recurrence relations.
This is a vector whose kth coordinate is the number of non-inversions (a, b)
such that a ≤ k < b. We relate these vectors to the non-inversion sums
and show that there is a bijective correspondence between permutations
and their zone-crossing vectors. We also prove a theorem showing that the
distribution of the coordinates of these vectors is related to the q-analog of
the binomial coeﬃcients; see Theorem 3.7.
In Section 4 we consider k-step inversions, which are inversions (a, b)
such that b − a = k, and show in Theorem 4.4 that the distribution of these
types of inversions is related to the Eulerian polynomials. We next consider
(k1, k2)-step inversions, which are inversions (a, b), such that b − a = k1 and
π(b) − π(a) = k2, and prove a special case of the distribution function; see
Proposition 4.6. We also consider inversions (a, b) such that b − a ≤ k and
prove recurrence relations for their distributions in some special cases; see
Proposition 4.8.
In Section 5, we consider some relationships between our work and the
work of others. In Section 5.1, we consider a k-step variant of a statistic that
counts inversions whose ﬁrst coordinate (called the inversion top) is 0 modulo
d. Inversion tops mod d have been studied by Kitaev and Remmel [4, 5] and
by Jansson [3]. We provide formulas for special cases of the distribution of
k-step inversions whose ﬁrst coordinate is 0 mod d.
In Section 5.2, we consider a k-step variant of the left boundary sums in
Dukes and Reifergerste [2]. Given a permutation π, the left boundary sum
of π (denoted lbsum(π)) gives the area to the left of the Dyck path of π.
Dukes and Reifergerste [2] show that lbsum(π) is also the sum of the number
of inversions and the number of certiﬁed non-inversions, where a certiﬁed
non-inversion is a non-inversion (a, b), with a position c, such that a < c < b
and πc ≥ πd whenever a < d < b. We consider a k-step variant of this
(denoted ipcnik(π)) that only counts k-step inversions and k-step certiﬁed
non-inversions, and provide special cases of the distribution functon. Finally
we show how many of the statistics we consider can be represented using
marked mesh patterns deﬁned by ´Ulfarsson in [7]
The connection found in Theorem 2.5 is used in Theorem 2.2 to show
that given any integer k greater than 34 there exists a permutation π such

REFINED INVERSION STATISTICS ON PERMUTATIONS 3

that the dot product of π with the identity permutation 12 · · · |π| equals
k. We also present an algorithm that, given k, produces the permutation
π; see Section 2.1. The total number of permutations which dotted with
the identity permutation gives k, is given by the sequence A135298
2 in the
Online Encyclopedia of Integer Sequences, and hence our theorem tells us
that this sequence is non-zero after k = 34.

Basic deﬁnitions. We deﬁne the set of positive integers to be P = {1, 2, 3, . . . }.
A permutation is a bijective function π : {1, . . . , n} → {1, . . . , n} for some n
in P. The number n is called the rank of the permutation. We often write
πk for π(k), and write a permutation as a list of its values π1π2 · · · πn. Let
Sn be the set of permutations of rank n.
We deﬁne the identity permutation 1n as the permutation π, such that
πk = k for 1 ≤ k ≤ n. We will write 1, omitting the subscript, if the rank is
clear from the context. Given a permutation π = π1π2 · · · πn, we deﬁne its
reverse as πr = πnπn−1 · · · π1, its complement as πc = (n + 1 − π1)(n + 1 −
π2) · · · (n + 1 − πn), and its inverse πi as the unique permutation such that
π ◦ πi = 1.

2. Non-inversion sums and the dot product of permutations

Deﬁnition 2.1. For a permutation π of rank n, the number

1 · π =
 n∑

i=1 iπ(i)

is called the cosine of the permutation.

Note that if we treat permutations as vectors then

1 · π = |1| · |π| cos(θ) = (1
2 + 2
2 + · · · + n2) cos(θ) = n(n + 1)(2n + 1)
6 cos(θ),

where θ is the angle between 1 and π. So 1 · π only depends on the cosine
of the angle between the identity and the permutation.
Most of this section will be leading to a proof of the following theorem:

Theorem 2.2. For a positive integer

k ̸∈ {2, 3, 6, 7, 8, 9, 12, 15, 16, 17, 18, 19, 31, 32, 33, 34},

there exists a permutation π such that 1 · π = k.

The total number of permutations π, such that 1 · π = k, is given by the
sequence A135298
3 in the Online Encyclopedia of Integer Sequences. Our
theorem tells us that this sequence is non-zero after k = 34. Furthermore,
we will provide an algorithm in Section 2.1 for constructing a permutation
π, such that 1 · π = k for k as in the theorem.

2http://oeis.org/A135298
3http://oeis.org/A135298

4 SACK AND ´ULFARSSON

To prove this theorem, we introduce the notion of the non-inversion sum.
We build this notion on that of a non-inversion. Given a permutation π
of rank n, an inversion is a pair (a, b), such that 1 ≤ a < b ≤ n and
π(a) > π(b), and a non-inversion is a pair (a, b), such that 1 ≤ a < b ≤ n
and π(a) < π(b). Denote the set of inversions of π by INV(π), and the set
of non-inversions by NINV(π).

Deﬁnition 2.3. Let π be a permutation.
(1) The number
 invsum(π) = ∑

(a,b)∈INV(π) (b − a) ,

is called the inversion sum of π.
(2) The number
 ninvsum(π) = ∑

(a,b)∈NINV(π) (b − a) ,

is called the non-inversion sum of π.

Observe that the values added up in the sums are diﬀerences of positions
(b − a) rather than of values (π(b) − π(a)). The following result shows that
had we deﬁned the sums in terms of diﬀerences of values we would have
resulted in the same function.

Proposition 2.4. For any permutation π

ninvsum(πi) = ninvsum(π),

or equivalently ∑

(a,b)∈NINV(π) (π(b) − π(a)) = ∑

(a,b)∈NINV(π) (b − a) .

A similar statement holds for the inversion sum.

Proof. We will prove the statement by induction on the rank of the permu-
tation. Let π be an arbitrary permutation and let π(n) = k. If k = 1 then
the result follows immediately by the induction hypotheses. Otherwise let
π(hj) = j for j = 1, . . . , k − 1. We depict in Figure 1 graphs of π and πi,
where the boxi,j represents the sets of pairs (a, πa) lying in the designated re-
gions of the graph on the left, or (a, πi
a) lying in the designated regions of the
graph on the right. For example, box2,j = {(a, πa) | hj < a, j < πa < k}.
Let τ be the permutation obtained from π by removing the last element
k = π(n) and reducing the letters of π that are larger than k by 1. Then,
by the induction hypothesis, ninvsum(τ ) = ninvsum(τ i). But

ninvsum(π) = ninvsum(τ ) +
 k−1∑

j=1 1 + | box1,j | + | box2,j | + | box3,j |,

REFINED INVERSION STATISTICS ON PERMUTATIONS 5

j
 hj

n

k
 n

box1,j

box2,j

box3,j

box4,j
 n
 j

hj
 k n

box1,jbox2,jbox3,j
 box4,j

Figure 1. The permutation π is shown on the left and πi is
shown on the right.

where for each j the sum of the box sizes is equal to one less than the
separation n − hj, and

ninvsum(πi) = ninvsum(τ i) +
 k−1∑

j=1 1 + | box1,j | + | box2,j | + | box4,j |,

where for each j the sum of the box sizes box2,j and box4,j is equal to one
less than the separation k − j and the size of box1,j represents the number
of former non-inversions whose separation has just increased by one.
To see that ∑k−1
j=1 | box3,j | is equal to ∑k−1
j=1 | box4,j | note that the following
are equivalent:
• (a, σ(a)) ∈ box4,π(b),
• (a, b) ∈ INV(π) with π(a) < k,
• (b, σ(b)) ∈ box3,π(a). □

It is straightforward to see that ninvsum(πr) = invsum(π) = ninvsum(πc).
Note that for any permutation π of rank n, the sum of the inversion sum
and the non-inversion sum is the (n − 1)th tetrahedral number (n+1
3 ):

invsum(π) + ninvsum(π) = ∑

1≤a<b≤n(b − a) (1)

= (n − 1)n(n + 1)
6 = (n + 1
3
 ),

so two permutations have the same inversion sum if and only if they have
the same non-inversion sum.
We now show that the cosine of the permutation is closely related to the
non-inversion sum of the permutation.

Theorem 2.5. For any permutation π,

1 · π = 1 · 1
c + ninvsum(π).

6 SACK AND ´ULFARSSON

Proof. Let ϕ be a function mapping a permutation π of rank n to a vector,
whose jth coordinate is the number of times the jth position of π is at the
end of a non-inversion minus the number of times the jth position is at the
beginning of a non-inversion, that is,

ϕ(π)j = ∑

(i,j)∈NINV(π) 1 − ∑

(j,k)∈NINV(π) 1.

The jth coordinate of ϕ(π) is then the coeﬃcient of j (treating j as a vari-
able) in the non-inversion sum formula, and hence the contribution of the
jth position of π to the non-inversion sum is j times this number. Thus
ninvsum(π) = 1 · ϕ(π).
We next see that the jth coordinate of ϕ(π) is ϕ(π)j = πj − 1c
j. The ﬁrst
coordinate is ϕ(π)1 = π1 − n = π1 − 1c
1, since in the formula for the non-
inversion sum, π1 will be subtracted once for every non-inversion, which is
guaranteed by a value greater than π1. For general j ≥ 1, if πj − πj+1 > 0,
then ϕ(πj+1) can be obtained from ϕ(πj) by subtracting the number of
values between πj+1 and πj, as given each such value πk, either k < j, in
which case (k, j) was counted positively toward ϕ(πj) but (k, j + 1) does not
count toward ϕ(πj+1), or j > j + 1, in which case (j, k) did not count toward
ϕ(πj), but (j + 1, k) counts negatively toward ϕ(πj+1). Thus we subtract
πj − πj+1 − 1. If πj − πj+1 < 0, then to obtain ϕ(πj) we add 1 for every value
between πj+1 and πj, and we add 2 in order to account for the non-inversion
(j, j + 1). Thus we add πj+1 − πj − 1 + 2. Either way, we obtain the formula:

ϕ(π)j+1 = ϕ(π)j + πj+1 − πj − 1.

By induction, let us assume that ϕ(π)j = πj − 1c
j. Thus

ϕ(π)j+1 = πj − 1
c
j + πj+1 − πj − 1 = πj+1 − 1
c
j − 1 = πj+1 − 1
c
j+1.

In conclusion:

ninvsum(π) = 1 · ϕ(π) = 1 · (π − 1
c) = 1 · π − 1 · 1
c,

whence our desired result of this theorem immediately follows. □

Note that for 1 ∈ Sn, 1 · 1c = (n+2
3 ), so equation 1 implies that the
equation in the theorem is equivalent to

1 · π = (n + 2
3
 ) + (n + 1
3
 ) − invsum(π),

which can be simpliﬁed to

1 · π = n(n + 1)(2n + 1)
6 − invsum(π).

Corollary 2.6. Given two permutations π, ρ ∈ Sn,

ninvsum(π ◦ ρ) = π · ρi − 1 · 1
c.

Proof. By a direct calculation,

ninvsum(π ◦ ρ) = 1 · (π ◦ ρ) − 1 · 1
c = π · ρi − 1 · 1
c. □

REFINED INVERSION STATISTICS ON PERMUTATIONS 7

Observe that since π · ρ = ρ · π, then ninvsum(π ◦ ρi) = ninvsum(ρ ◦ πi).
Then taking ρ = 1, we get ninvsum(π) = ninvsum(πi). This serves as an
alternative proof to Proposition 2.4.

Lemma 2.7. For n ≥ 6,
(n + 1
3
 ) + (n
3
) ≥ (n + 2
3
 ) − 1.

Proof. A straightforward calculation shows that for n ≥ 7, (
n+1
3 ) + (
n
3) >
(
n+2
3 ). For the case where n = 6, note that (7
3
) + (6
3
) = (8
3
) − 1. □

Lemma 2.8. For each value 0 ≤ k ≤ 10, there exists a permutation π ∈ S4,
such that ninvsum(π) = k.

Proof. Here is a permutation for each value of k: 4321, 3421, 3412, 4213,
4123, 2413, 3214, 1423, 2143, 1243, 1234. □

Lemma 2.9. For n ≥ 4 and each 0 ≤ k ≤ (n+1
3 )
, there is a permutation
π ∈ Sn, such that ninvsum(π) = k.

Proof. We show this by induction on n, where the base case (n = 4) is given
by Lemma 2.8. Assuming this holds for n − 1 (with n > 4), we consider
permutations π ∈ Sn, with πn = 1. The last entry does not contribute
anything to the non-inversion sum of the ﬁrst n − 1, which by the induction
hypothesis ranges through all the integers in the interval from 0 through(
n
3). Next, consider permutations π ∈ Sn, with π1 = 1. This ﬁrst entry is
guaranteed to contribute (n
2) to the non-inversion sum, while the rest can
be chosen to contribute any integer ranging from 0 through (n
3). Because
(
n+1
3 ) = (
n
3) + (n
2), and because (n
3) > (n
2) for n > 3, we have that we can
obtain every integer from 0 through (n+1
3 ). □

We are now ready to prove the main theorem of this section.

Proof of Theorem 2.2. Given k ≥ 35, let n be the largest integer, such that(n+2
3 ) ≤ k. Note that n ≥ 5. Let m = k − (n+2
3 ). For n ≥ 5, we have by
Lemma 2.7, (n+2
3 ) + (n+1
3 ) ≥ (n+3
3 ) − 1. Thus m ≤ (n+1
3 ), and hence by
Lemma 2.9, there is a permutation π ∈ Sn, with ninvsum π = m. Thus, by
Theorem 2.5,

1 · π = (n + 2
3
 ) + ninvsum(π) = (n + 2
3
 ) + m = k.

For the values of k less than 35, we ﬁrst consider in the following chart
for each n ≤ 5, the maximum and minimum values 1 · π can obtain, where

8 SACK AND ´ULFARSSON

π ∈ Sn. n (n+2
3 ) (n+2
3 ) + (n+1
3 )

1 1 1
2 4 5
3 10 14
4 20 30
5 35 55

By Lemma 2.9, we have permutations π such that the value 1 · π can hit
every value from 20 through 30. For the other values, we have the following
chart π 1 · π
1 1
21 4
12 5
321 10
312 11
132 13
123 14
 □

Note that an integer k ̸∈ {2, 3, 6, 7, 8, 9, 12, 15, 16, 17, 18, 19, 31, 32, 33, 34}
is even if and only if there is a permutation π such that 1 · π = k and the
number of odd integers in the odd positions of π is even.

2.1. Algorithm. We present an algorithm for ﬁnding a permutation π for a
given k ̸∈ {2, 3, 6, 7, 8, 9, 12, 15, 16, 17, 18, 19, 31, 32, 33, 34}, such that 1 · π =
k. We ﬁrst introduce three functions: η, r, and ν.
For k < 35 and k ̸∈ {2, 3, 6, 7, 8, 9, 12, 15, 16, 17, 18, 19, 31, 32, 33, 34}, let
η(k) be π such that 1 · π = k (this is guaranteed by Lemma 2.2 and is easy
to make explicit because of the bound on k).
Let k be such that we wish to ﬁnd π with 1 · π = k. In the proof of
Theorem 2.2, we chose the length n of the to-be-constructed π, such that(n+2
3 ) ≤ k. Since 6(
(n+2
3 ) − k) = n3 + 3n2 + 2n − 6k, we can determine from
k the desired n as the ﬂoor of the real cubic root of n3 + 3n2 + 2n − 6k,
which is the ﬂoor of
1
3
 3
√81k + 3
√(27k)2 − 3 + 1
3
 3
√81k − 3
√(27k)2 − 3 − 1. (2)

Let r be a function mapping a positive integer k to such a value n.
Let ν : {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10} → S4, be given by 0 ↦→ 4321, 1 ↦→
3421, 2 ↦→ 3412, 3 ↦→ 4213, 4 ↦→ 4123, 5 ↦→ 2413, 6 ↦→ 3214, 7 ↦→ 1423,
8 ↦→ 2143, 9 ↦→ 1243, 10 ↦→ 1234. This is from the proof of Lemma 2.8.
Assuming the functions η, r, and ν, we present an algorithm Main(k), see
Algorithm 1, that calls another function ζ, deﬁned below in Algorithm 2,
that inputs m, a value for the ninvsum, and n, the length of the permutation
to create.
 REFINED INVERSION STATISTICS ON PERMUTATIONS 9

Algorithm 1 Main(k)

if k < 35 then
output η(k)
else
n ← r(k).
m ← k − (n+2
3 ) (Note that m ≤ (
n+1
3 ).)
output ζ(m, n)
end if

Algorithm 2 ζ(m, n)

if n = 4 then
output ν(m)
else
if m ≤ (n
3) then
output ζ(m, n − 1) ⊖ 1
else
output 1 ⊕ ζ(m − (n
2), n − 1)
end if
end if

Here π ⊕ σ is the direct sum of the permutations π and σ and π ⊖ σ is
the skew sum. Because of Lemma 2.7 and the fact that n ≥ 5 for the ﬁrst
function call, we have that m ≤ (n+1
3 ) for that ﬁrst call. The reasoning
behind why the inductive hypothesis applies to Lemma 2.9 guarantees that
m ≤ (n+1
3 ) for every function call after the ﬁrst, even if n = 4. Also,
because of equation 2, it is clear that the running time of this algorithm is
proportional to k1/3.

3. Zone-crossing vectors and the distribution of the
non-inversion sum

We are interested in the function

Nn(x) = ∑

π∈Sn xninvsum(π)

which records the distribution of the non-inversion sum. Table 3 provides
some empirical data generated with the computer algebra system Sage
4,
where we factor the polynomials as much as possible. In the context of
Table 3, some of these polynomials factor into some reasonably small factors
and a very large factor.
One can observe that the degree of Nn(x) is always the (n − 1)th tetrahe-
dral number (
n+1
3 ). This is consistent with equation (1), where the maximum
non-inversion sum (n+1
3 ) can be obtained using the identity permutation 1.

4www.sagemath.org

10 SACK AND ´ULFARSSON

Table 1. The distribution function of ninvsum, Nn(x).

n Small factors of Nn(x) Big factor of Nn(x)

1 1 1

2 x + 1 1

3 1 x4 + 2x3 + 2x + 1

4 x2 + 1 x8 + 3x7 + x5 + 2x4 + x3 + 3x + 1

5 x2 − x + 1 x18 + 5x17 + 7x16 + 8x15 + 8x14 + 6x13 + 2x12 + 6x11 + 10x10

+14x9 + 10x8 + 6x7 + 2x6 + 6x5 + 8x4 + 8x3 + 7x2 + 5x + 1

6 (x + 1)(x2 − x + 1)2 x30 + 6x29 + 11x28 + 13x27 + 13x26 + 6x25 − x24 + 6x23 + 21x22

+30x21 + 19x20 + 3x19 − 7x18 + 14x17 + 27x16 + 36x15 + 27x14

14x13 − 7x12 + 3x11 + 19x10 + 30x9 + 21x8 + 6x7 − x6 + 6x5

+13x4 + 13x3 + 11x2 + 6x + 1

7 (x2 − x + 1)
 x54 + 7x53 + 16x52 + 23x51 + 36x50 + 39x49 + 38x48 + 45x47 + 62x46

+71x45 + 83x44 + 82x43 + 83x42 + 91x41 + 86x40 + 85x39 + 128x38

+149x37 + 144x36 + 129x35 + 132x34 + 101x33 + 137x32 + 166x31

+204x30 + 182x29 + 146x28 + 108x27 + 146x26 + 182x25 + 204x24

+166x23 + 137x22 + 101x21 + 132x20 + 129x19 + 144x18 + 149x17

+128x16 + 85x15 + 86x14 + 91x13 + 83x12 + 82x11 + 83x10 + 71x9

+62x8 + 45x7 + 38x6 + 39x5 + 36x4 + 23x3 + 16x2 + 7x + 1

8 (x4 + 1)(x2 − x + 1)
 x78 + 8x77 + 22x76 + 36x75 + 60x74 + 71x73 + 66x72 + 67x71 + 84x70

+94x69 + 133x68 + 150x67 + 171x66 + 182x65 + 164x64 + 135x63

+196x62 + 249x61 + 280x60 + 278x59 + 290x58 + 218x57 + 243x56

+270x55 + 375x54 + 456x53 + 432x52 + 326x51 + 322x50 + 329x49

+442x48 + 481x47 + 533x46 + 464x45 + 413x44 + 362x43 + 437x42

+489x41 + 520x40 + 462x39 + 520x38 + 489x37 + 437x36 + 362x35

+413x34 + 464x33 + 533x32 + 481x31 + 442x30 + 329x29 + 322x28

+326x27 + 432x26 + 456x25 + 375x24 + 270x23 + 243x22 + 218x21

+290x20 + 278x19 + 280x18 + 249x17 + 196x16 + 135x15 + 164x14

+182x13 + 171x12 + 150x11 + 133x10 + 94x9 + 84x8 + 67x7 + 66x6

+71x5 + 60x4 + 36x3 + 22x2 + 8x + 1

The primary aim of this section is to ﬁnd a recursive deﬁnition of the
distribution function for the non-inversion sum, that is, to deﬁne Nn+1(x)
in terms of Nn(x). Our formulation of the distribution function will involve
a new type of vector, the zone-crossing vector, whose coordinates count the
number of inversions or non-inversions (a, b) of a permutation, with a given
point between a and b.

Deﬁnition 3.1. Given a permutation π of rank n, we deﬁne
(1) its inversion zone-crossing vector, izcv(π) = (z1, z2, . . . , zn−1), where
zk is the number of inversions (a, b) ∈ INV(π), where a ≤ k < b, and
its augmented zone crossing vector aizcv(π) = (0, z1, z2, . . . , zn−1, 0).
(2) its non-inversion zone-crossing vector nzcv(π) = (z1, z2, . . . , zn−1),
where zk is the number of non-inversions (a, b) ∈ NINV(π), where
a ≤ k < b, and its augmented zone crossing vector anzcv(π) =
(0, z1, z2, . . . , zn−1, 0).

Example 3.2. Consider the permutation π = 314562. Then izcv(π) =
(2, 1, 2, 3, 4) and nzcv(π) = (3, 7, 7, 5, 1).

The following proposition states that a zone crossing vector uniquely de-
termines its permutation.

REFINED INVERSION STATISTICS ON PERMUTATIONS 11

Proposition 3.3. If v = (v0, v1, . . . , vn−1, vn) = aizcv(π), then πk = n −
(k − 1) − (vk − vk−1), for 1 ≤ k ≤ n. (Therefore, if ρ is a permutation, such
that aizcv(π) = aizcv(ρ), then π = ρ.)

Proof. Let ρ be a permutation, and let v be its zone-crossing vector. Let π
be constructed according to the statement of the proposition. We show that
π = ρ. First observe that ρ1 = n − v1, since this is the number of positions
to the right of the ﬁrst position that have a value greater than ρ1. Thus
ρ1 = π1. For a general k ≥ 1, note that if ρk = 1, then vk − vk−1 = n − k.
Thus 1 = ρk = n − (k − 1) − (vk − vk−1), just as is the case with πk. To
consider diﬀerent values of ρk, imagine incrementing its value by 1 as a result
of swapping ρk with the position with one larger value. If ρk is incremented
by 1, then vk − vk−1 is decremented by 1, for either the original value of ρk
is swapped with a value to the right, thus decrementing vk, or it is swapped
with a value to the left, thus incrementing vk−1. Thus all the values of ρk
can be obtained by the formula above, and hence ρ = π. □

Lemma 3.4. The sum of the coordinates of nzcv(π) equals ninvsum(π).

Proof. This follows from the fact that each non-inversion will contribute
to as many zone-crossing coordinates as is the separation distance of the
non-inversion. For example, a non-inversion from position 1 to position 3
has separation 2, which is the number of zone-crossing coordinates it will
contribute to. □

Proposition 3.5. For any π ∈ Sn,
(1) nzcv(π) + izcv(π) = (1 · n − 1, 2 · n − 2, . . . , n − 1 · 1),
(2) nzcv(πc) = izcv(π),
(3) nzcv(πr) = izcvr(π).

Proof. (1) To prove nzcv(π) + izcv(π) = (1 · n − 1, 2 · n − 2, . . . , n − 1 · 1),
we note that the jth coordinate of nzcv(π) + izcv(π) counts the total
number of pairs matching each coordinate in the ﬁrst j positions
with each coordinate in the last n − j positions. This is because
each such pair is a zone crossing inversion or non-inversion and is
hence counted in either izcv(π) or nzcv(π). This yields the vector
(1 · n − 1, 2 · n − 2, . . . , n − 1 · 1), giving us the desired formula.
(2) To prove nzcv(πc) = izcv(π), note that the complement operation
changes every inversion to a non-inversion, and every non-inversion
to an inversion.
(3) To prove nzcv(πr) = izcvr(π), note that every inversion in π between
positions j and j+k is a non-inversion in πr from positions n−j−k+1
to n − j + 1. This yields nzcvr(πr) = izcv, and reversing the vectors
on each side yields the desired equation. □

Lemma 3.6. Let π be a permutation of rank n with augmented zone-crossing
vector anzcv(π) = (a0, a1, a2, . . . , an−1, an). Let ρ be the permutation ob-
tained by inserting n + 1 into π in between position k and k + 1 (in the case

12 SACK AND ´ULFARSSON

where k = 0, the resulting permutation is 1 ⊖ π). Then for 0 ≤ k ≤ n,

anzcv(ρ) = (a0 + 0, a1 + 1, a2 + 2, . . . , (ak + k), ak, ak+1, . . . , an).

(Note that for k = 0, we have anzcv(ρ) = (0, 0, a1, a2, . . . , an−1, 0) and for
k = n we have anzcv(ρ) = (0, a1 + 1, a2 + 2, . . . , an−1 + n − 1, n, 0).)

Proof. For 0 ≤ j ≤ k the jth position of the zone-crossing vector (counting
from 0 in the augmented vector) is incremented by the number j of positions
in the left zone, as each forms a new non-inversion pair with the new position
k + 1 in the right zone. The jth position among the (k + 1)th position in
the new zone-crossing vector counts the number of non-inversions starting
among the ﬁrst j positions and ending among the n + 1 − j positions. As
the inserted position is now in the left zone and has the highest value, it
does not contribute to the zone-crossing count. Thus the jth position of
the new zone-crossing vector is the same as the (j − 1)th position of the
old zone-crossing vector (we decrement the position by one, as the position
counts the size of the left zone, which decreases by one when the inserted
position is removed). □

The preceding lemma can be used to give a recursive deﬁnition of the
zone-crossing vectors. We show how this is done when adding a value to
permutations of rank 2 to obtain permutations of rank 3. The set of (aug-
mented) non-inversion zone-crossing vectors for permutations of rank 2 are
(010) corresponding to the permutation 12 and (000) corresponding to 21.
Using Lemma 3.6, we determine the (augmented) non-inversion zone cross-
ing vectors for permutations of rank 3 in the following chart:

k = 0 k = 1 k = 2
(000) (0000) (0100) (0120)
(010) (0010) (0210) (0220)

The ﬁrst column gives the zone-crossing vectors for the permutations of
rank 2. The ﬁrst row gives the position k to the right of which we place
the highest value to obtain the new permutation. The remaining entries
correspond to the resulting zone-crossing vectors. We underline the value
ak in position k +1 of the zone-crossing vector. Notice that these correspond
to the positions k in the left column.
In summary, we see that these vectors do not range across all possibilities
between the lowest (0000) and the highest (0220), as we are missing (0110),
(0020) and (0200). We hope future work can yield a more direct characteri-
zation of the set of all possible zone-crossing vectors. Such a characterization
may reveal new patterns of a variety of permutation statistics. A variation
of such a characterization might, for example, capture sets of zone-crossing
vectors correspond to permutations avoiding a certain classical pattern of
rank 3, such as the patten 231. Since the number of permutations of rank
n that avoid a given classical pattern of rank 3 is the nth Catalan number,
such a set may oﬀer a new Catalan structure.

REFINED INVERSION STATISTICS ON PERMUTATIONS 13

The proof of the following theorem will make use of partitions of integers.
Given a positive integer, n, we write λ ⊣ n to indicate that λ is a partition of
n. We write ℓλ for the length of the partition λ. For example, λ = 3+3+2+1
is a partition of 9 of length 4.

Theorem 3.7. The number of permutations of rank n such that the kth

coordinate of the zone-crossing vector equals ℓ is

k!(n − k)![qℓ] [ n
k
 ]
q .

In other words ∑

π∈Sn qnzcv(π)k = k!(n − k)! [ n
k
 ]
q .

Proof. The number of partitions of ℓ into at most k parts, where each part

has size at most n − k, is given by [qℓ] [ n
k
 ]
q. Each part may correspond to

one of the ﬁrst k positions of a permutation, and the size of the part would
correspond to the number out of the n − k last positions that the selected
position is a non-inversion with. For each partition, we may rearrange the
ﬁrst k positions and rearrange the last n − k positions without aﬀecting
the kth coordinate of the zone-crossing vector. This gives us the remaining
k!(n − k)!. □

Theorem 3.8. For n ≥ 1, letting (
1
2) = 0, we have

Nn+1(q) =
 n∑

k=0 q(
k+1
2 ) ∑

π∈Sn qanzcvk(π)qninvsum(π)

= Nn(q) +
 n−1∑

k=1 q(
k+1
2 ) ∑

π∈Sn qnzcvk(π)qninvsum(π) + q(
n+1
2 )Nn(q).

Proof. We are interested in the result of extending a permutation π to a
permutation ρ by inserting n + 1 between the kth and (k + 1)th positions
of π (like in Lemma 3.6). We proceed by summing the functions restricted
to permutations with n + 1 in the (k + 1)th positions for each k. When
k = 0, the value n + 1 is inserted at the beginning of the permutation and
hence contributes nothing to the non-inversion sum. Thus we have the term
Nn(q). When k = n, the value n + 1 is in the last position, and hence
adds (the maximum) (n+1
2 ) to whatever non-inversion sum the permutation

originally had. Thus our last term will be q(
n+1
2 )Nn(q). For the other values
of k (1 ≤ k ≤ n − 1), what the insertion of the value n + 1 contributes to
the non-inversion sum depends on the original permutation. By Lemma 3.6,
the sum of the zone-crossing vector coordinates (equaling the non-inversion
sum) increases by (k+1
2 ) + nzcvk, which is why we multiply qninvsum(π) by

q(
k+1
2 )+nzcvk(π). □

14 SACK AND ´ULFARSSON

4. The distribution of k-, (k1, k2)-, and (≤ k)-step inversions

4.1. The distribution of k-step inversions.

Deﬁnition 4.1. A k-step inversion of a permutation π is an inversion
(a, b) ∈ INV(π), where b − a = k. Similarly a k-step non-inversion is a
non-inversion (a, b) ∈ NINV(π), such that b − a = k.

Let invk(π) be the number of k-step inversions in π, and let ninvk(π) be
the number of k-step non-inversions in π. Then inv(π) = ∑n−1
k=1 invk(π), and
similarly for ninvk(π). Deﬁne

Hn,k(x) = ∑

π∈Sn xinvk(π)

so I(n, k, i) def
= [xi]Hn,k(x) is the number of permutations in Sn with the
number of k-step inversions equaling the number i. It is known that Hn,1(x)
is the nth Eulerian polynomial, which we denote An(x)
5, since a 1-step
inversion is a descent.
In ﬁnding Hn,k(x) for arbitrary k, we will divide up the permutations into
k smaller permutations which can be interleaved to form the original. We
call these smaller permutations runs, and deﬁne them precisely as follows.

Deﬁnition 4.2. Given a permutation π of rank n and 1 ≤ k ≤ n, the ith

k-step run of π is the permutation ρ of rank j = ⌊(n − i)/k⌋ + 1, where
ρj = πk(j−1)+i.

Let λi = ⌊(n − i)/k⌋ + 1 be the length of the ith k-step permutation.
One can observe that if n ≥ k, then there are rem(n/k) many j, such
that λj = ⌊n/k⌋ + 1, and k − rem(n/k) many j, such that λj = ⌊n/k⌋.
Furthermore, ∑k
i=1 λi = n. The intuition for this can be seen in the following
example, where the runs partition the original permutation, and hence the
λi partition n.

Example 4.3. Consider the case n = 11, k = 4. Since n ≥ k, the total
number of 4-step runs is four. Of those, three are of length 3 (λ1, λ2, λ3 = 3).

1 2 3 4 5 6 7 8 9 10 11

The remaining one is of length 2 (λ4 = 2).

1 2 3 4 5 6 7 8 9 10 11

Note that k-step inversions only occur within the same k-step run, and
that a k-step inversion in the original permutation corresponds to a 1-step
inversion (a descent) in a run. We will see in the proof of the next theorem
how this leads to H11,4 = I(11, 4, 0)A3
3(x)A1
2(x), where I(11, 4, 0) will count

5The coeﬃcient [xk−1]An(x) is T (n, k) in the sequence http://oeis.org/A008292

REFINED INVERSION STATISTICS ON PERMUTATIONS 15

the ways of distributing the 11 values among the 4 runs, and the As will
correspond to the permutations of the s values within a run.

Theorem 4.4. For 1 ≤ k ≤ n let s = ⌊n/k⌋ + 1 and t = rem(n/k). Then

Hn,k(x) = I(n, k, 0)A
t
s(x)A
k−t
s−1(x),

where Aℓ(x) = Hℓ,1(x) is the ℓth Eulerian polynomial, and

I(n, k, 0) =
 k−1∏

j=1
 (n − ∑j−1
i=0 λi
λj
 ),

where the λ0 def
= 0 and for 1 ≤ j ≤ k − 1, λj is the length of the jth k-step
run.

Proof. Let us ﬁrst ﬁnd I(n, k, 0). Given a permutation π with no k-step
inversions, the order within each run must be increasing. Thus the entire
variation of such permutations is with how the n values are distributed
among the runs. If j − 1 runs have been ﬁlled, we must choose λj more out
of the remaining n − ∑j−1
i=0 λi. Thus we have

I(n, k, 0) =
 k−1∏

j=1
 (n − ∑j−1
i=0 λi
λj
 ).

Furthermore, the number of k-step inversions is invariant over how we dis-
tribute n among the runs. Thus I(n, k, 0) is a factor of the distribution
function. What the number of k-step inversions depends on is how the
numbers are arranged within each run. Note again that k-step inversions
only occur within the same k-step run, and that a k-step inversion in the
original permutation corresponds to a 1-step inversion (a descent) in a run.
In this way, the runs do not interact. Thus

I(n, k, i) = ∑

∑k
j=1 pj=i; 1≤pj <λj
 I(n, k, i)
 k∏

j=1[xpj ]Aλj (x).

Since there are t = rem(n/k) many j, such that λj = s = ⌊n/k⌋ + 1, and
k − rem(n/k) many j, such that λj = ⌊n/k⌋, we have that

Hn,k(x) = I(n, k, 0)A
t
s(x)A
k−t
s−1(x). □

If we had used ninvk instead of invk in the deﬁnition of the distribution
function Hn,k(x) then we would have obtained the same formula as in the
theorem above. Also, had we used the diﬀerence of values, rather than
positions, in the deﬁnitions of invk and ninvk, we would also have arrived at
the same formula, since the values-deﬁnition for π would have corresponded
to the positions-deﬁnition for πi. Table 2 includes experimental runs for the
distribution function Hn,k for n = 1, . . . , 9, and select k for high values of n.

16 SACK AND ´ULFARSSON

Table 2. The distribution function of ninvk, Hn,k(x).

n k Hn,k(x)

1 1 1

2 1 x + 1
2 2

3 1 x2 + 4x + 1
2 3(x + 1)
3 6

4
 1 (x + 1)(x2 + 10x + 1)

2 6(x + 1)2

3 12(x + 1)
4 24

5
 1 x4 + 26x3 + 66x2 + 26x + 1

2 10(x + 1)(x2 + 4x + 1)
3 30(x + 1)2

4 60(x + 1)
5 120

6
 1 (x + 1)(x4 + 56x3 + 246x2 + 56x + 1)

2 20(x2 + 4x + 1)2

3 90(x + 1)3

4 180(x + 1)2

5 360(x + 1)
6 720

7
 1 x6 + 120x5 + 1191x4 + 2416x3 + 1191x2 + 120x + 1

2 35(x + 1)(x2 + 4x + 1)(x2 + 10x + 1)
3 210(x + 1)2(x2 + 4x + 1)
4 630(x + 1)3

5 1260(x + 1)2

6 2520(x + 1)
7 5040

8
 1 (x + 1)(x6 + 246x5 + 4047x4 + 11572x3 + 4047x2 + 246x + 1)

2 70(x + 1)2(x2 + 10x + 1)2

3 560(x + 1)(x2 + 4x + 1)2

4 2520(x + 1)4

5 5040(x + 1)3

6 10080(x + 1)2

7 20160(x + 1)
8 40320

9
 1 x8 + 502x7 + 14608x6 + 88234x5 + 156190x4 + 88234x3 + 14608x2 + 502x + 1

2 126(x + 1)(x2 + 10x + 1)(x4 + 26x3 + 66x2 + 26x + 1)
3 1680(x2 + 4x + 1)3

4 7560(x + 1)3(x2 + 4x + 1)
.
.
. .
.
.

4.2. (k1, k2)-step inversions and non-inversions.

Deﬁnition 4.5. Given a permutation π, a (k1, k2)-step inversion is a pair
(a, b), such that 1 ≤ a < b ≤ n, satisfying b − a = k1 and π(b) − π(a) = k2.
Similarly, a (k1, k2)-step non-inversion is a pair (a, b), such that 1 ≤ a <
b ≤ n, satisfying b − a = k1 and π(a) − π(b) = k2.

Let inv(k1,k2)(π) be the number of (k1, k2)-step inversions in π. Then

inv(π) = ∑

1≤k1,k2≤n−1 inv(k1,k2)(π).

REFINED INVERSION STATISTICS ON PERMUTATIONS 17

Deﬁne
 Hn,(k1,k2)(x) = ∑

π∈Sn xinv(k1,k2)(π).

Proposition 4.6. Let n/2 < k1, k2 < n. Then the degree of Hn,(k1,k2)(x) is
ℓ = min(n − k1, n − k2), and its leading coeﬃcient equals

(n − 2ℓ)!ℓ!
(n − k1
ℓ
 )(n − k2
ℓ
 ).

Proof. Since k1 > n/2, there are n−k1 location pairs that a k1-step inversion
could be, since there are n − k1 many k-step runs of length two, with the
remainder of the runs of length 1. Similarly, since k2 > n/2, there are at
most n − k2-inversions with a value separation of k2, as the top value has to
be greater than k2. Thus ℓ = min(n − k1, n − k2) is the maximum number
of (k1, k2)-step inversions, and the degree of Hn,(k1,k2)(x) is ℓ.
For the leading coeﬃcient, we select (n−k1
ℓ ) positions pairs to place top
values among (n−k2
ℓ ). Then there are ℓ! ways to arrange the values among the
position pairs, and there are (n − 2ℓ)! ways to arrange the remaining values
among the remaining positions. Note that no new (k1, k2)-step inversions
can occur with the (n−2ℓ)! values and positions, since either all the available
position pairs have been ﬁlled (when ℓ = n−k1) or all the available top values
have been used (when ℓ = n − k2). □

This proof will be adapted in Section 5.1, for a similar result involving
k-step inversions with inversion tops divisible by d. For future work, we
would like a complete description of the polynomials Hn,(k1,k2)(x) as we had
for Hn,k(x), the distribution of k-step inversions. Table 3 contains some
experimental runs for Hn,(k1,k2)(x).

Table 3. The distribution function of inv(k1,k2), Hn,(k1,k2)(x).

n k1 k2 = 1 k2 = 2 k2 = 3 k2 = 4
1 1 1
2 1 x + 1 2
2 2 2
3 1 x2 + 2x + 3 2(x + 2) 6
2 2(x + 2) x + 5 6
3 6 6 6
4 1 x3 + 3x2 + 9x + 11 2(x2 + 4x + 7) 6(x + 3) 24
2 2(x2 + 4x + 7) 2(x2 + 2x + 9) 4(x + 5) 24
3 6(x + 3) 4(x + 5) 2(x + 11) 24
4 24 24 24 24
5 1 x4 + 4x3 + 18x2 + 44x + 53 2(x3 + 6x2 + 21x + 32) 6(x2 + 6x + 13) 24(x + 4)
2 2(x3 + 6x2 + 21x + 32) (x + 3)(x2 + 4x + 25) 4(x2 + 7x + 22) 6(3x + 17)
3 6(x2 + 6x + 13) 4(x2 + 7x + 22) 2(x2 + 10x + 49) 12(x + 9)
4 24(x + 4) 6(3x + 17) 12(x + 9) 6(x + 19)
5 120 120 120 120

18 SACK AND ´ULFARSSON

4.3. The distribution of (≤ k)-step inversions.

Deﬁnition 4.7. Let inv≤k(π) = ∑

k′≤k invk′(π).

Then, since n − 1 is the maximum separation, and a separation of one
corresponds to a descent, we get

inv(π) = inv≤n−1(π) and des(π) = inv≤1(π),

for any permutation of rank n. Deﬁne

Jn,≤k(x) = ∑

π∈Sn xinv≤k(π).

For the purpose of the next proposition we recall the falling factorial

(k)j = k(k − 1) · · · (k − (j − 1)),

and deﬁne a diﬀerential operator

∇k =
 k∑

j=0
 j + 1
(k)j
 dj

dxj .

Proposition 4.8. (1) If the maximum step-size is 1, we have

Jn,1(x) = An(x),

where An(x) is the nth Eulerian polynomial.
(2) If the maximum step-size is n − 2, we have

Jn,≤n−2(x) = Jn−1,≤n−3(x) ·
 

 d
dx
 

x
 n−2∑

j=0 xj


 + xn−2∇n−2(xn−2)



 .

(3) If the maximum step-size is n − 1, we have

Jn,≤n−1(x) = Jn−1,≤n−2(x) ·
 n−1∑

j=0 xj = [n]x!.

Proof. (1) This follows from the fact that a 1-step inversion is a descent.
(3) As noted above inv≤n−1(π) = inv(π) and therefore

Jn,≤n−1(x) = ∑

π∈Sn xinv(π)

= (1 + x)(1 + x + x2) · · · (1 + x + x2 + · · · + xn−1)

= [n]x!.

We also give an alternative proof: Let k = n − 1. For each value m
for the last position of a permutation σ, we have that inv≤k(σ) = n−
m + inv≤k(τ ), where τ is the permutation obtained by ﬂattening the
restriction of σ the domain to {1, . . . , n − 1}. Thus for each value m,
we multiply Jn−1,≤k−1(x) by xn−m to account for all permutations

REFINED INVERSION STATISTICS ON PERMUTATIONS 19

that end in m. We then add these products together for all values
of m so as to account for all permutations.
(2) Let k = n − 2. Here we imagine the eﬀect of the ﬁrst and the
last positions on the inversion count of the middle positions. For
each pair (mf , mℓ) of values that the ﬁrst and last positions can
assume, the contribution to the counts in Jn,≤k(x) will be the same
as their contribution of the counts in Jn,≤k+1(x) as long as mf < mℓ.
Otherwise (if mf > mℓ), the contribution to Jn,≤k(x) is one less than
it would be for Jn,≤k+1(x), since the ﬁrst and last positions form an
inversion not counted in the former, but counted in the latter.
By part (3) of this proposition, the last two factors of Jn,≤k+1(x)
are (1 + x2 + · · · + xk) and (1 + x2 + · · · + xk + kk+1), which when
multiplied together give us

1 + 2x + · · · + (k − 1)xk−2 + kxk−1 + (k + 1)xk (3)

+ (k + 1)xk+1 + · · · + 3x2k−1 + 2x2k + x2k+1

The coeﬃcient of each xj in (3) corresponds to the number of pairs
(mf , mℓ) that contribute j to the inversion count of the middle po-
sitions. The number of inversions a pair (mf , mℓ) contributes is
(mf − 1) from the ﬁrst position plus (n − mℓ) from the last position
minus possibly one for over counting in the case that mf > mℓ. So
the contribution of the pair to Jn,≤k+1(x) would be n + mf − mℓ − 1
if mf < mℓ or n + mf − mℓ − 2 if mf > mℓ. Note that if mf < mℓ,
then this number is at most n − 2 = k. Otherwise (if mf > mℓ)
this number is at least n − 1 = k + 1. Thus, up to j = k, all pairs
(mf , mℓ) are such that mf < mℓ, and hence the exact same pairs can
be used in the count for determining Jn,≤k. Starting with j = k + 1,
all pairs (mf , mℓ), are such that mf > mℓ, and there is an inversion
counted toward Jn,≤k+1(x) that is not counted toward Jn,k(x), and
hence these pairs will contribute to the case where j = k when con-
structing the formula for Jn,≤k(x). A similar argument shows that
this generalizes, so that when t ≥ 1, we have xk+t in (3) replaced by

20 SACK AND ´ULFARSSON

xk+t−1. Thus we obtain,

Jn,≤k(x) = Jn−1,≤k−1(x) · (1 + 2x + · · · + (k − 1)xk−2 + kxk−1

+ 2(k + 1)xk + kxk+1 + · · · + 2x2k−1 + x2k).

= Jn−1,≤k−1(x) ·
 

 k∑

j=0(j + 1) (xj + x2k−j)




= Jn−1,≤k−1(x) ·
 

 k∑

j=0(j + 1)xj +
 k∑

j=0(j + 1)x2k−j




= Jn−1,≤k−1(x) ·
 

 k∑

j=0(j + 1)xj + xk k∑

j=0(j + 1)xk−j




= Jn−1,≤k−1(x) ·
 

 d
dx
 

x
 k∑

j=0 xj


 + xk∇k(xk)



 . □

Table 4 includes experimental runs for the distribution function Jn,≤k(x)
for n = 1, . . . , 7. The degree of Jn+1,≤k(x) is given by k(2n−k+1)
2 since the
maximum of inv≤k is achieved by the reverse of the identity, and the number
of j-step inversions in this permutation is n + 1 − j. Summing this number
from 1 to k gives the claimed degree. We would like a more complete de-
scription of the distribution function of Jn,≤k(x), but we leave it for future
work.
 5. Future work and connections with other work

5.1. k-step inversion tops that are zero modulo d. Recall that given
an inversion (a, b) in a permutation, the letter a is called an inversion top.
Kitaev and Remmel [4, 5] considered inversions where the inversion top is
zero modulo d for a particular integer d. We adapt this deﬁnition to our
setting by deﬁning modinvd,k(π) to be the number of k-step inversions with
an inversion top that is zero modulo d. Let

Ln,d,k(x) = ∑

π∈Sn xmodinvd,k(π)

be the corresponding distribution function.

Proposition 5.1. The leading coeﬃcient of Ln,2,n−1(x) is
⌊ n
2
 ⌋2 (n − 2)!.

Thus Ln,2,n−1(x)
(n − 2)! = ⌊ n
2
 ⌋2 x + n(n − 1) − ⌊ n
2
 ⌋2 .

REFINED INVERSION STATISTICS ON PERMUTATIONS 21

Table 4. The distribution function of inv≤k, Jn,≤k(x).

n k Jn,≤k(x)

1 1 1

2 1 x + 1

3 1 x2 + 4x + 1

2 (x + 1)(x2 + x + 1)

4 1 (x + 1)(x2 + 10x + 1)

2 (x + 1)(x4 + 2x3 + 6x2 + 2x + 1)

3 (x + 1)(x2 + x + 1)(x3 + x2 + x + 1)

5
 1 x4 + 26x3 + 66x2 + 26x + 1

2 (x + 1)3(x4 + x3 + 11x2 + x + 1)

3 (x + 1)(x2 + x + 1)(x6 + 2x5 + 3x4 + 8x3 + 3x2 + 2x + 1)

4 (x + 1)(x2 + x + 1)(x3 + x2 + x + 1)(x4 + x3 + x2 + x + 1)

6
 1 (x + 1)(x4 + 56x3 + 246x2 + 56x + 1)

2 (x + 1)(x8 + 4x7 + 25x6 + 88x5 + 124x4 + 88x3 + 25x2 + 4x + 1)

3 (x + 1)2(x10 + 3x9 + 7x8 + 22x7 + 31x6 + 52x5 + 31x4 + 22x3 + 7x2 + 3x + 1)

4 (x + 1)(x2 + x + 1)(x3 + x2 + x + 1)(x8 + 2x7 + 3x6 + 4x5 + 10x4 + 4x3 + 3x2 + 2x + 1)

5 (x + 1)(x2 + x + 1)(x3 + x2 + x + 1)(x4 + x3 + x2 + x + 1)(x5 + x4 + x3 + x2 + x + 1)

7
 1 x6 + 120x5 + 1191x4 + 2416x3 + 1191x2 + 120x + 1

2 (x + 1)(x10 + 5x9 + 39x8 + 218x7 + 562x6 + 870x5 + 562x4 + 218x3 + 39x2 + 5x + 1)

3 (x + 1)(x2 + x + 1)(x12 + 4x11 + 10x10 + 38x9 + 79x8

+166x7 + 244x6 + 166x5 + 79x4 + 38x3 + 10x2 + 4x + 1)

4 (x + 1)4(x2 + x + 1)
(x12 + x11 + 4x10 + 4x9 + 21x8 + 43x6 + 21x4 + 4x3 + 4x2 + x + 1)

5 (x + 1)(x2 + x + 1)(x3 + x2 + x + 1)(x4 + x3 + x2 + x + 1)
(x10 + 2x9 + 3x8 + 4x7 + 5x6 + 12x5 + 5x4 + 4x3 + 3x2 + 2x + 1)

6 (x + 1)(x2 + x + 1)(x3 + x2 + x + 1)(x4 + x3 + x2 + x + 1)
(x5 + x4 + x3 + x2 + x + 1)(x6 + x5 + x4 + x3 + x2 + x + 1)

Proof. The formula for the leading coeﬃcient is proved as follows: In order
to have one (n − 1)-step inversion with an even inversion top, a permutation
must start with an even number and end in some smaller number. Thus we
get the formula
 (n − 2)!
 ⌊ n
2 ⌋∑

j=1(2j − 1).

Simpliﬁcation yields the claimed formula. □

We now generalize this proposition.

Proposition 5.2. Let n/2 < k < n and 1 < d ≤ n. The degree of Ln,d,k(x)
is ℓ = min(n − k, ⌊ n
d ⌋) and its leading coeﬃcient equals

(n − 2ℓ)!ℓ!
(n − k
ℓ
 ) ∑

1≤i1<i2<···<iℓ≤⌊ n
d ⌋
 ℓ∏

j=1
(dij − 2j + 1).

22 SACK AND ´ULFARSSON

Proof. Since k > n/2, there are n − k locations that an inversion top could
be, since there are n − k many k-step runs of length two, with the remain-
ing k many k-step runs being of length 1. There are ⌊ n
d ⌋ possible values
for inversion tops. Thus ℓ = min(n − k, ⌊ n
d ⌋) is the maximum number of
inversions possible with inversion tops modulo d. Hence ℓ is the degree of
Ln,d,k(x).
The sum selects the values of the inversion tops, the jth smallest inversion
top being dij . The jth factor of the product represents the remaining possible
values that could be the bottom of the inversion with top dij . The positions
of these inversions are chosen among the n−k possible locations pairs, which
is why we multiply by the binomial coeﬃcient. The sum had arranged the
tops in increasing order, and hence the coeﬃcient of ℓ! counts the ways
of rearranging the tops among their ℓ positions. The coeﬃcient of (n −
2ℓ)! counts the ways of assigning the remaining values to the remaining
positions. □

Table 5 contains some empirical data for the case d = 2.

Table 5. The distribution function of modinv2,k, Ln,2,k(x).

n k Ln,2,k(x)
1 1 1

2 1 y + 1
2 2

3 1 2(y + 2)
2 y + 5
3 6

4
 1 4(y2 + 4y + 1)
2 2(y + 1)(y + 5)
3 8(y + 2)
4 24

5
 1 12(y2 + 6y + 3)
2 6(y + 1)(y + 9)
3 2(y2 + 22y + 37)
4 24(y + 4)
5 120

6
 1 36(y + 1)(y2 + 8y + 1)
2 4(4y3 + 55y2 + 94y + 27)
3 6(y + 1)(y2 + 22y + 37)
4 4(y + 5)(13y + 17)
5 72(3y + 7)
6 720

7
 1 144(y3 + 12y2 + 18y + 4)
2 2(37y3 + 615y2 + 1359y + 509)
3 4(7y3 + 204y2 + 651y + 398)
4 6(y3 + 75y2 + 387y + 377)
5 12(13y2 + 154y + 253)
6 360(3y + 11)
7 5040

We would like a more complete description of the polynomial Ln,2,k(x),
but we leave it for future work.

5.2. Paths. Dukes and Reifergerste [2] showed that the left boundary sum
of π, written lbsum(π), is the number of inversions in π added to the num-
ber certiﬁed non-inversions. A certiﬁed non-inversion is an occurrence of

REFINED INVERSION STATISTICS ON PERMUTATIONS 23

the pattern 132 which is neither part of a 1432 nor a 1342 pattern. The
mesh patterns deﬁned by Br¨and´en and Claesson [1] can be used to give
an alternative deﬁnition: A certiﬁed non-inversions is an occurrence of the
mesh pattern
 .

In Dukes and Reifergerste [2], the left boundary vector of a permutation
π of rank n has as its jth coordinate the largest i < j, such that πi > πj.
The left boundary sum of a permutation π, denoted lbsum(π), is deﬁned as
the sum of the left boundary coordinates.
Variations of this may be as follows.
(1) Deﬁne the (≥k)-left boundary vector of a permutation π to be such
that its jth coordinate is the largest i ≤ j − k, such that πi > πj.
Deﬁne lbsum≥k(π) to be the the sum of this vector.
(2) Deﬁne the (≤k)-left boundary vector of a permutation π to be such
that its jth coordinate is i − max(0, j − k) + 1, where i is the largest,
such that max(0, j − k) ≤ i < j and either πi > πj or i = max(0, j −
k). Deﬁne lbsum≤k(π) to be the sum of this vector.
(3) Deﬁne the (=k)-left boundary vector to be such that coordinate j is
1 if aj−k > aj, and 0 otherwise. Deﬁne lbsum=k(π) to be the sum of
this vector.

Proposition 5.3. (1) Given a permutation π, lbsum≥k(π) is the num-
ber of (≥k)-step inversions, plus the number of non-inversions form-
ing the end-points of an occurrence of the pattern 132, but with at
least k steps from the 3 to the 2. (Such a non-inversion consists
of the endpoints of certiﬁed non-inversion within a permutation ob-
tained by removing the k − 1 positions to the left of the top of the
non-inversion, and isomorphically adjusting the values to ﬁt in the
new range.)
(2) Given a permutation π, lbsum≤k(π) is the number of (≤k)-step in-
versions plus the number of certiﬁed (≤k)-step non-inversions (a
certiﬁed non-inversions whose endpoints are at most k apart).
(3) Given a permutation π, lbsum=k(π) is the number of k-step inver-
sions of π.

Proof. The proof of these are adapted from [2].
(1) Let (a1, . . . , an) be the (≥k)-left boundary vector. Then aj = d is
the maximum value no less than k away from j, such that πd > πj.
Then every i ≤ d is such that either πi > πj or there is a position
c (we can always choose d), such that i < c ≤ j − k and πc > πj.
Since d is maximal, every (≥k)-step inversion with bottom j will be
counted among such i, and no (<k)-step inversion will qualify, since
d is already k-steps away. Furthermore, any (≥k)-step non-inversion

24 SACK AND ´ULFARSSON

(i, j) with i < d, such that there is a c (we can always pick d), such
that i < c ≤ j − k and πc > πj. Because d is maximal, any non-
inversion (i, j) that has a c, such that i < c ≤ j − k and πc > πj, is
a non-inversion, where i < d.
(2) The proof here is almost identical to the previous case, except we
restrict d to ranging from max(0, j −k) to j −1, and we only consider
i ≤ d, such that i ≥ j − k. This allows us to focus on (≤k)-step
inversions and certiﬁed (≤k)-step non-inversions, and is accounted
for by the fact that the aj is really d−max(0, j −k)+1. Furthermore,
since we are technically counting certiﬁed non-inversions, which are
triples rather than pairs, we select for the middle point the position
of maximum value. If we did not place this restriction, we could
over-count, with many possibilities for a middle, given one pair of
endpoints.
(3) The coordinates of the (=k)-left boundary vector with the value 1
are precisely the positions of the permutation that form the top of
a k-step non-inversion. Since a position can be the top of at most
one k-step non-inversion, the sum of the coordinates of the vector is
equal to the number of k-step non-inversions. □

We consider yet a forth way to generalize lbsum(π). For our purposes we
deﬁne a certiﬁed k-step non-inversion to be a certiﬁed non-inversion with
endpoints forming a k-step non-inversion. The generalization we focus on
from here is as follows. For a permutation π, let ipcnik(π) be the number of
k-step inversions in π added to the number of certiﬁed k-step non-inversions.
Let Kn,k(x) = ∑

π∈Sn xipcnik(π)

be the corresponding distribution function.
From the empirical data in Table 6 it seems that the constant term in
Kn,k(x) is always equal to k!. This is proven below.

Proposition 5.4. The constant term in Kn,k is k!. Furthermore, the per-
mutations π ∈ Sn, such that ipcnik(π) = 0, are precisely the permutations
that have the form σ(k + 1)(k + 2) · · · n, where σ ∈ Sk.

Proof. It is clear that any permutation of the form σ(k + 1)(k + 2) · · · n,
where σ is a permutation from Sk has ipcnik zero. Conversely, suppose that
ipcnik(π) = 0 and that π is of the form σλ where σ consists of the ﬁrst k
letters of π and λ consists of the remaining letters. Then the letters of λ
must be in increasing order; otherwise we let ℓ1 > ℓ2 be the ﬁrst two adjacent
letters in λ that are not in increasing order. Then if πℓ2−k < πℓ2, there is
an ℓ, such that the triple (ℓ2 − k, ℓ, ℓ2) is a certiﬁed k-step non-inversion,
and if πℓ2−k > πℓ2, the pair (ℓ2 − k, ℓ2) is an inversion. Now to ﬁnish the
proof we need to show that σ consists of the letters 1, . . . , k. First observe

REFINED INVERSION STATISTICS ON PERMUTATIONS 25

Table 6. The distribution function of ipcnik, Kn,k(x).

n k Kn,k(x)

1 1 1

2 1 x + 1
2 2
3 1 x2 + 4x + 1
2 2(2x + 1)
3 6
4 1 (x + 1)(x2 + 10x + 1)
2 2(x + 1)(5x + 1)
3 6(3x + 1)
4 24
5 1 x4 + 26x3 + 66x2 + 26x + 1

2 2(13x3 + 35x2 + 11x + 1)
3 6(11x2 + 8x + 1)
4 24(4x + 1)
5 120
6 1 (x + 1)(x4 + 56x3 + 246x2 + 56x + 1)

2 2(38x4 + 183x3 + 121x2 + 17x + 1)
3 6(x + 1)(46x2 + 13x + 1)
4 24(19x2 + 10x + 1)
5 120(5x + 1)
6 720
7 1 x6 + 120x5 + 1191x4 + 2416x3119x2 + 120x + 1

2 2(116x5 + 969x4 + 1100x3 + 310x2 + 24x + 1)
3 6(202x4 + 459x3 + 157x2 + 21x + 1)
4 24(103x3 + 89x2 + 17x + 1)
5 120(29x2 + 12x + 1)
6 720(6x + 1)
7 5040
8 1 (x + 1)(x6 + 246x5 + 4047x4 + 11572x3 + 4047x2 + 246x + 1)

2 2(382x6 + 5124x5 + 9517x4 + 4420x3 + 684x2 + 32x + 1)
3 6(986x5 + 3454x4 + 1925x3 + 325x2 + 29x + 1)
4 24(x + 1)(614x3 + 201x2 + 24x + 1)
5 120(190x3 + 125x2 + 20x + 1)
6 720(41x2 + 14x + 1)
7 5040(7x + 1)
8 40320

that the ﬁrst letter of λ is larger than any letter in σ. Since λ is increasing,
the remaining letters in λ are also larger than 1, . . . , k. This ﬁnishes the
proof. □

Corollary 5.5. The number of permutations π ∈ Sn with ipcnin−1(π) = 1
is (n − 1)(n − 1)!. Thus
 Kn,n−1(x)
(n − 1)! = (n − 1)x + 1.

Proof. As a consequence of Proposition 5.4, given π ∈ Sn, ipcnin−1(π) =
0 if and only if πn = n. Note that ipcnik(π) = 1 otherwise. There are
(n − 1)(n − 1)! permutation π, such that πn ̸= n. □

Proposition 5.6. The number of permutations π ∈ Sn, with ipcnin−2(π) =
2 is (n − 2)!(n2 − 3n + 1).

26 SACK AND ´ULFARSSON

Thus Kn,n−2(x)
(n − 2)! = (n2 − 3n + 1)x2 + 2(n − 1)x + 1.

Proof. In order to construct a permutation with ipcnin−2 equal to 2 we need
to choose four numbers to occupy the ﬁrst two positions and the last two
positions. The permutation constructed in this way will always have ipcnin−2
equal to 2 unless any of the following hold:
• n is in position 1 and n − 1 is in position n,
• n is in position n − 1, or
• n is in position n.
This shows that the number we are looking for is

(n − 4)!
(n(n − 1)(n − 2)(n − 3)(n − 4)

− (n − 2)(n − 3) − 2(n − 1)(n − 2)(n − 3)
).

When this is simpliﬁed, it gives the formula in the proposition. □

5.3. Marked mesh patterns. Marked mesh patterns were deﬁned by ´Ulfarsson
in [7, Deﬁnition 24]. In this subsection we show how these patterns relate to
the concepts introduced above. Figure 2 shows how k-step, (≤k)-step and
(k1, k2)-step inversions can be identiﬁed with patterns.

=k−1 ≤k−1 =k1−1

=k2−1

Figure 2. k-step, (≤k)-step and (k1, k2)-step inversions in
terms of patterns.

Using the representation of k-step inversions allows us to write the number
of inversions and the inversion sum of a permutation as a linear combination
of patterns; see Figure 3.

inv = ∑

k≥1
 



 =k−1 


 , invsum = ∑

k≥1 k ·
 



 =k−1 




Figure 3. Writing the inv and invsum as a linear combina-
tion of patterns.

It is only slightly harder to realize that the coordinates of the zone-crossing
vectors are given by patterns, for example, the kth coordinate of the inversion

REFINED INVERSION STATISTICS ON PERMUTATIONS 27

zone-crossing vector of a permutation π is the number of occurrences of the
pattern
 zk =

k−1≥
 ≤n−k−1
,

in π. A k-step inversion with an inversion top that is zero modulo d is an
occurrence of
 =k−1

=n−dℓ

for some ℓ ≥ 1.
Finally, a certiﬁed k-step non-inversion is an occurrence of the pattern

=k−2 .

5.4. Acknowledgements. We would like to thank Anders Claesson and
Einar Steingr´ımsson for their helpful comments.

References

1. Petter Br¨and´en and Anders Claesson, Mesh patterns and the expansion of permutation
statistics as sums of permutation patterns, in preparation.
2. Mark Dukes and Astrid Reifegerste, The area above the Dyck path of a permutation,
Adv. in Appl. Math. 45 (2010), no. 1, 15–23. MR 2628782
3. Fredrik Jansson, Variations on the excedance statistic in permutations, Master’s thesis,
Chalmers Tekniska H¨ogskola, 2006.
4. Sergey Kitaev and Jeﬀrey Remmel, Classifying descents according to equivalence mod
k, Electron. J. Combin. 13 (2006), no. 1, Research Paper 64, 39 pp. (electronic).
MR 2240770 (2007b:05007)
5. , Classifying descents according to parity, Ann. Comb. 11 (2007), no. 2, 173–193.
MR 2336014 (2008f:05008)
6. Percy A. MacMahon, Combinatory analysis. Vol. I, II (bound in one volume), Dover
Phoenix Editions, Dover Publications Inc., Mineola, NY, 2004, Reprint of An introduc-
tion to combinatory analysis (1920) and Combinatory analysis. Vol. I, II (1915, 1916).
MR 2417935 (2009e:05002)
7. Henning ´Ulfarsson, A uniﬁcation of permutation patterns related to Schubert varieties,
Pure Math. Appl. to appear (2011).

(Sack) Department of Mathematics and Statistics, California State Univer-
sity, Long Beach, USA

( ´Ulfarsson) School of Computer Science, Reykjavik University, Iceland
E-mail address: joshua.sack@gmail.com, henningu@ru.is
