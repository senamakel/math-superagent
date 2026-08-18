<!-- source: https://arxiv.org/pdf/1807.11273 | converted from PDF -->

arXiv:1807.11273v3  [math.DS]  2 Feb 2019
Deducing Three Gap Theorem From
Rauzy-Veech Induction

Christian Weiß

February 5, 2019

Abstract
The Three Gap Theorem states that there are at most three dis-
tinct lengths of gaps if one places n points on a circle, at angles of
z, 2z, 3z, . . . nz from the starting point. The theorem was ﬁrst proven
in 1958 by Sós and many proofs have been found since then. In this
note we show how the Three Gap Theorem can easily be deduced by
using Rauzy-Veech induction.

Kronecker sequences are important examples of uniformly distributed
sequences. Given z ∈ R, a Kronecker sequence is of the form (zn)n≥0 =
({nz})n≥0 where {z} := z − ⌊z⌋ denotes the fractional part of z. Sometimes
their level of uniformity is even as great as possible since inﬁnitely many
Kronecker sequences belong to the classical examples of low-discrepancy se-
quences, see e.g. [DT97], Corollary 1.65. Another important property de-
scribing the uniformity of Kronecker sequences is the Three Gap Theorem,
going back to a famous conjecture of Steinhaus which was ﬁrst proved by
Sós in [Sos58]. Since the Three Gap Theorem is closely linked to continued
fraction expansion we shortly introduce some notation ﬁrst: every irrational
number z has a uniquely determined inﬁnite continued fraction expansion

z = a0 + 1/(a1 + 1/(a2 + . . .)) =: [a0; a1; a2; . . .],

where the ai are integers with a0 = ⌊z⌋ and ai ≥ 1 for all i ≥ 1. The sequence
of convergents (ri)i∈N of z is deﬁned by

ri = [a0; a1; . . . ; ai].

The convergents ri = pi/qi with gcd(pi, qi) = 1 can also be calculated directly
by the recurrence relation

p−2 = 0, p−1 = 1, pi = aipi−1 + pi−2, i ≥ 0
q−2 = 1, q−1 = 0, qi = aiqi−1 + qi−2, i ≥ 0. (1)

1

Now the Three Gap Theorem states the following.

Theorem 1 (Three Gap Theorem). Let z ∈ (0, 1) be irrational with con-
tinued fraction expansion z = [a0; a1; a2; . . .] and convergents rn = pn/qn.
Furthermore let N ∈ N with N ≥ 2 have Ostrowski representation1

N =
 m∑

j=0 bjqj

with integer coeﬃcients b0, b1, . . . , bm satisfying 0 ≤ bj ≤ aj+1 and minimal
m with qm + 1 ≤ N < qm+1 + qm. If z < 1
2, let K2l−1 = {q2l−1z} and
K2l = 1 − {q2lz} for l ∈ N0, and if z > 1
2, let K2l−1 = 1 − {q2l−1z} and
K2l = {q2lz}. Then the ﬁnite sequence ({nz})n=1,...,N −1 has at most three
diﬀerent lengths of gaps, namely

L1 = Km−1 − bmKm,
L2 = Km
L3 = L1 + L2.

The number of gaps of lengths L1, L2, L3 are

N1 = N − bmqm − qm−1,
N2 = N − qm,
N3 = qm − (N − bmqm − qm−1).

Later on, several further proofs of the claim have been found, see e.g.
[Lia79], [AB98], [MS17] and most recently [Tah17]. In this note we add
another proof to the list of proofs of Theorem 1: a Kronecker sequence cor-
responds to the rotation of the unit circle by the angle 2πz if we identify
[0, 1) with R/Z. The map x ↦→ x + z mod 1 is also the simplest exam-
ple of an interval exchange transformation. Indeed, it may be considered
an exchange of two subintervals of [0, 1), speciﬁcally A := [0, 1 − {z}) and
B := [1 − {z} , 1). Here we show that the Three Gap Theorem can easily be
deduced from the viewpoint of interval exchange transformations by using
Rauzy-Veech induction.

Interval Exchange Transformations. We only give a brief summary
here and refer the reader to [Via06], which is also our main source, for more

1Actually, this is a slightly amended version of the Ostrowski representation, since
usually it is assumed that 0 ≤ b0 < a1 and bj−1 = 0 if bj = aj+1 but not qm + 1 ≤ N <
qm+1 + qm.
 2

details. Let I ⊂ R be an interval of the form [0, λ∗) and let {Iα|α ∈ A}
be a ﬁnite partition of I into subintervals indexed by some ﬁnite alphabet
A. An interval exchange transformation is a map f : I → I which is
a translation on each subinterval Iα. It is determined by its combinatorial
data and its length data. The combinatorial data consists of two bijec-
tions π0, π1 : A → {1, . . . , n}, where n is the number of elements of A and
the length data are numbers (λα)α∈A =: λ with λα > 0 and λ∗ = ∑

α∈A λα.
The number λα is the length of the subinterval Iα and the pair π = (π0, π1)
describes the ordering of the subintervals before and after the map f is it-
erated. For A = {A, B} , π0(A) = π1(B) = 1 and π1(A) = π0(B) = 2 the
interval exchange transformation becomes the rotation of R/λ∗Z by λB.

Rauzy-Veech Induction. For an interval exchange transformation f given
by the data (π, λ), we deﬁne the type ǫ by

λπ−1
ǫ (n) > λπ−1
1−ǫ(n),

if the lengths of these two intervals do not coincide. Following the usual
terminology, we say that Iπ−1
ǫ (n) is the winner and Iπ−1
1−ǫ(n) is the loser. Let
J be the subinterval of I obtained by removing the loser, i.e.

J =
 {
I \ f (Iπ−1
1 (n)) if f has type 0

I \ Iπ−1
0 (n) if f has type 1.

The Rauzy-Veech induction R(f ) of f is its ﬁrst return map to the in-
terval J. It is again an interval exchange transformation consisting of n
subintervals. The corresponding data (π′, λ′) can be easily calculated, see
e.g. [Via06]. In this note, we restrict our attention to π0(A) = π1(B) = 1
and π1(A) = π0(B) = 2 because it is the only case of interest for the proof
of Theorem 1. The ﬁrst a − 1 steps of Rauzy-Veech induction for two inter-
vals are depicted in Figure 1, where A
k respectively Bk denotes the speciﬁc
interval appearing after step k.

As long as the two rightmost intervals λπ−1
ǫ (n), λπ−1
1−ǫ(n) have diﬀerent lengths

the construction can be iterated yielding a sequence R(j)(f ) = (π(j), λ(j)) of
interval exchange transformations. The type is well-deﬁned inﬁnitely times if
and only if the so-called Keane-condition which postulates that the orbits
of the singularities of f −1 by f are inﬁnite and distinct is satisﬁed, see e.g
[Yoc06].
 3

A B

B f (A)

A B1 f (A)

B1 f 2(A) f (A)

A Ba−1 . . . f 2(A) f (A)

Ba−1 f a(A) . . . f 2(A) f (A)
 A B

f (B) A

A
1 f −1(B) B

f (B) A
1 B

A
a−1f −a(B) . . . f −1(B) B

f (B) A
a−1 . . . f −1(B) B

Figure 1. First a steps of Rauzy-Veech induction, for type 0 (left) and type
1 (right)

Besides the Rauzy-Veech induction we need the accelerated Rauzy-Veech
induction, also known as Zorich-Rauzy-Veech induction: it means that
the Rauzy-Veech induction is applied as many times a ∈ N until the type
changes, compare again Figure 1. We denote the resulting map by ˆR and the
corresponding a by ai. In the case of two intervals, the accelerated Rauzy-
Veech induction is equivalent to the continued fraction algorithm and the
ai are equal to the coeﬃcients of the continued fraction expansion, see e.g.
[Via06], Chapter 9.

Proof of the Three Gap Theorem. Let N ∈ N be arbitrary and let us
assume that 1 > z > 1
2 since the case z < 1
2 works likewise. At ﬁrst, we prove
by induction that the m
th application of accelerated Rauzy-Veech yields a
partition of [0, 1) into qm long and qm−1 short intervals. Using the notation
therein, we can see from Figure 1 that the ﬁrst application of accelerated
Rauzy-Veech disjointly partitions

[0, 1) = f (A) ˙∪f 2(A) ˙∪ . . . ˙∪f a1(A) ˙∪Ba−1 (2)

into 1 = q0 short interval with length ˆl(1)
s and a1 = q1 long intervals with
length ˆl(1)
l . In the same manner, the m-th application of accelerated Rauzy-
Veech partitions the long interval (before m-th step) of length ˆl(m−1)
l into
am long intervals (after the m-th step) of length ˆl(m)
l = ˆl(m−1)
s and one short
interval of length ˆl(m)
s . Inductively it follows from (2), that applying f to one
distinguished long interval am · qm−1 + qm−2 = qm times (compare (1)) and to
one distinguished small interval qm−1 times yields again a disjoint partition
of [0, 1).

Hence, if N = qm+qm−1, then the set of left endpoints of the partition implied

4

by ˆRm, which consists of N = qm + qm−1 subintervals, only has two diﬀerent
gap lengths, i.e. N1 = 0, N2 = qm−1 and N3 = qm, as claimed. Similarly,
one step of the usual (not accelerated) Rauzy-Veech algorithm partitions the
long interval of length l(i)
l into one interval of length l(i)
l − l(i)
s and one of
length l(i)
s , compare again Figure 1. Note that ˆl(m) = l(
∑m
k=0 ak). This proves
the formulas for N1, N2, N3 in the case N = bmqm + qm−1 since applying the
usual Rauzy-Veech algorithm at this stage increases N by qm.

Moreover by applying (2) inductively, we see that the set of left endpoints
equals the ﬁnite Kronecker sequence ((n − 2)z)n=1,...,N as a set. This trans-
fers the results on the number of gaps to the Kronecker sequence for N =
bmqm +qm−1. Note that considering ((n−2)z)n=1,...,N instead of (nz)n=1,...,N −1
is no restriction because the variable shift just corresponds to a rotation of all
points of the sequence by a ﬁxed angle, namely −2z, which does not change
the number of gaps or their lengths.

If i Rauzy-Veech steps have been applied and N is increased by 1, the Kro-
necker sequence must approach the set of left endpoints implied by the next
Rauzy-Veech step R(i+1) as a set. In other words, one of the long intervals
is subdivided into one subinterval of length l(i)
s and one subinterval of length
lm := l(i)
l − l(i)
s by the additional point of the Kronecker sequence while the
other intervals remain undivided. In other words, as N increases by 1 also
N1 (number of medium length intervals) and N2 (number of short intervals)
increase by 1, while N3 (number of long intervals) decreases by 1 until there
is no interval of length l(i)
l left (and thus N1 drops to 0 again). This completes
the proof of the expressions for N1, N2 and N3 for all values of N.

The only part of the assertion which is missing are the formulas for L1, L2
and L3. Of course, the total length of all subintervals has to sum up to 1 and
we have already seen L3 = L1 + L2 because lm = l(i)
l − l(i)
s . Therefore, it suf-
ﬁces to only calculate one of the lengths. Another time we use induction to
show the formula for the shortest length L2. At the beginning there is 1 = q0
interval of short length ˆl(0)
s = L
(0)
2 = 1 − {q0z} and applying accelerated
Rauzy-Veech once yields

ˆl(1)
s = L
(1)
2 = 1 − a1(1 − {q0z}) = {q1z} .

5

Again by accelerated Rauzy-Veech, the m-th appearing short interval length
ˆl(m)
s = L
(m)
2 has to satisfy the equation

L
(m)
2 = L
(m−1)
3 − am · L
(m−1)
2
= Km−2 − amKm−1

=
 {(1 − {qm−2z}) − am {qm−1z} m is even
{qm−2z} − am(1 − {qm−1z}) m is odd

=
 {1 − {qmz} m is even
{qmz} m is odd

This ﬁnishes the proof because the length L2 does not change before one
accelerated Rauzy-Veech step is completed.

Acknowledgement. The author thanks two anonymous referees for their
very valuable comments.

References

[AB98] Alessandri P., Berthé V.: “Three Distance Theorems and Combina-
torics on Words”, Enseign. Math. 44, 103–132 (1998).

[DT97] Drmota, M., Tichy, R.: “Sequences, Discrepancies and Applications”,
Lecture Notes in Mathematics 1651, Springer, Berlin (1997).

[Lia79] Liang, F.: “A short proof of the 3d distance theorem”, Discrete Math-
ematics, 28 (3): 325–326 (1979).

[MS17] Marklof, J.: Strömbergsson A., “The Three Gap Theorem and the
Space of Lattices”, ArXiv: 1612.04906.

[Sos58] Sós, V.: “On the distribution mod 1 of the sequence nα”, Ann. Univ.
Sci. Budapest, Eötv¨ps Sect. Math., 1, 127–134 (1958).

[Tah17] Taha, D.: “The Three Gaps Theorem, Interval Exchange Transfor-
mations, and Zippered Rectangles”, ArXiv: 1708.04380.

[Via06] Viana, M.: “Ergodic Theory of Interval Exchange Maps”, Rev. Mat.
Complut 19(1), 7–100 (2006).

[Yoc06] Yoccoz, J.–C.: "Continued Fraction Algorithms for Interval Ex-
change Maps: an Introduction", in: Frontiers in number theory,
physics, and geometry I, 401–435, Springer (2006).

6

Christian Weiß, Hochschule Ruhr West, Duisburger Str.
100, D-45479 Mülheim an der Ruhr
E-mail address: christian.weiss@hs-ruhrwest.de

7
