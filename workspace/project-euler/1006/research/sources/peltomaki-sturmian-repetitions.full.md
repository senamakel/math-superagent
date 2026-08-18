<!-- source: https://arxiv.org/pdf/1411.5474 | converted from PDF -->

arXiv:1411.5474v2  [cs.DM]  26 May 2015
Characterization of repetitions in Sturmian words:
A new proof

Jarkko Peltomäki

jspelt@utu.ﬁ

Turku Centre for Computer Science TUCS, 20520 Turku, Finland
University of Turku, Department of Mathematics and Statistics, 20014 Turku, Finland

Abstract
We present a new, dynamical way to study powers (that is, repetitions) in Sturmian words
based on results from Diophantine approximation theory. As a result, we provide an alternative
and shorter proof of a result by Damanik and Lenz characterizing powers in Sturmian words
[Powers in Sturmian sequences, Eur. J. Combin. 24 (2003), 377–390]. Further, as a consequence,
we obtain a previously known formula for the fractional index of a Sturmian word based on
the continued fraction expansion of its slope.

Keywords: sturmian word, standard word, power, combinatorics on words, continued fraction

1 Introduction

In 2003 Damanik and Lenz [6] completely described factors of length n of a Sturmian word which
occur as pth powers for every n ≥ 0 and p ≥ 1. Damanik and Lenz prove a series of results
concerning how factors of a Sturmian word align to the corresponding (ﬁnite) standard words.
By a careful analysis of the alignment, they obtain the complete description of powers thanks
to known results on powers of standard words. Our method is based on the dynamical view
of Sturmian words as codings of irrational rotations. Translating word-combinatorial concepts
into corresponding dynamical concepts allows us to apply powerful results from Diophantine
approximation theory (such as the Three Distance Theorem) providing a more geometric proof
of the result of Damanik and Lenz. Our methods allow us to avoid tricky alignment arguments
making the proof in our opinion easier to follow. Furthermore, the results allow us to infer a
formula for the fractional index of a Sturmian word based on the continued fraction expansion
of its slope. This formula and its proof appeared in an earlier paper by Damanik and Lenz [5]
and was also established purely combinatorially using alignment arguments. The formula was
independently obtained with different methods by Carpi and de Luca [3] and Justin and Pirillo
[7]. For partial results and works related to powers in Sturmian words see e.g. the papers of
Mignosi [11], Berstel [2], Vandeth [13], and Justin and Pirillo [7].
The paper is organized as follows: in Section 2 we brieﬂy recall results concerning contin-
ued fractions and rational approximations and prove the purely number-theoretic and important
Proposition 2.2 for later use in Section 4. In Section 3 we state needed facts about Sturmian words
with appropriate references. Section 4 contains the main results and their proofs.

c⃝ 2015, Elsevier. Licensed under the Creative Commons Attribution-NonCommercial-NoDerivatives 4.0 International.

1

2 Continued Fractions and Rational Approximations

Every irrational real number α has a unique inﬁnite continued fraction expansion

α = [a0; a1, a2, a3, . . .] = a0 + 1

a1 + 1

a2 + 1
a3 + · · ·
 (1)

with a0 ∈ Z and ak ∈ N for all k ≥ 1. The numbers ai are called the partial quotients of α. Good
references on continued fractions are the books of Khinchin [8] and Cassels [4]. We focus here
only on irrational numbers, but we note that with small tweaks much of what follows also holds
for rational numbers, which have ﬁnite continued fraction expansions.
The convergents ck = pk
qk of α are deﬁned by the recurrences

p0 = a0, p1 = a1a0 + 1, pk = ak pk−1 + pk−2, k ≥ 2,
q0 = 1, q1 = a1, qk = akqk−1 + qk−2, k ≥ 2.

The sequence (ck)k≥0 converges to α. Moreover, the even convergents are less than α and form
an increasing sequence and, on the other hand, the odd convergents are greater than α and form
a decreasing sequence.
If k ≥ 2 and ak > 1, then between the convergents ck−2 and ck there are semiconvergents (called
intermediate fractions in Khinchin’s book [8]) which are of the form

pk,l
qk,l = l pk−1 + pk−2
lqk−1 + qk−2

with 1 ≤ l < ak. When the semiconvergents (if any) between ck−2 and ck are ordered by the size
of their denominators, the obtained sequence is increasing if k is even and decreasing if k is odd.
Note that we make a clear distinction between convergents and semiconvergents, i.e., conver-
gents are not a speciﬁc subtype of semiconvergents.
For the rest of this paper we make the convention that α refers to an irrational number with a
continued fraction expansion as in (1) having convergents pk
qk and semiconvergents pk,l
qk,l as above.
A rational number a
b is a best approximation of the real number α if for every fraction c
d such
that c
d ̸= a
b and d ≤ b it holds that
 |bα − a| < |dα − c| .

In other words, any other multiple of α with a coefﬁcient at most b is further away from the near-
est integer than is bα. The next proposition shows that the best approximations of an irrational
number are connected to its convergents (for a proof see Theorems 16 and 17 of [8]).

Proposition 2.1. The best rational approximations of an irrational number are exactly its convergents.

We identify the unit interval [0, 1) with the unit circle T. Let α ∈ (0, 1) be irrational. The map

R : [0, 1) → [0, 1), x ↦→ {x + α},

where {x} stands for the fractional part of the number x, deﬁnes a rotation on T. The circle
partitions into the intervals (0, 1
2 ) and ( 1
2 , 1). Points in the same interval of the partition are said
to be on the same side of 0, and points in different intervals are said to be on the opposite sides of
0. (We are not interested in the location of the point 1
2 .) The points {qkα} and {qk−1α} are always
on the opposite sides of 0. The points {qk,lα} with 0 < l ≤ ak always lie between the points
{qk−2α} and {qkα}; see (3).
We measure the shortest distance to 0 on T by setting

∥x∥ = min{{x}, 1 − {x}}.

2

We have the following facts for k ≥ 2 and for all l such that 0 < l ≤ ak:

∥qk,l α∥ = (−1)k(qk,lα − pk,l), (2)
∥qk,l α∥ = ∥qk,l−1α∥ − ∥qk−1α∥. (3)

We can now interpret Proposition 2.1 as

min
0<n<qk ∥nα∥ = ∥qk−1α∥, for k ≥ 1. (4)

Note that rotating preserves distances; a fact we will often use without explicit mention. In par-
ticular, the distance between the points {nα} and {mα} is ∥|n − m|α∥. Thus by (4) the minimum
distance between the distinct points {nα} and {mα} with 0 ≤ n, m < qk is at least ∥qk−1α∥. The
formula (4) tells what is the point closest to 0 among the points {nα} for 1 ≤ n ≤ qk − 1. We are
also interested to know the point closest to 0 on the side opposite to {qk−1α}. The next result is
very important and concerns this.

Proposition 2.2. Let α be an irrational number. Let n be an integer such that 0 < n < qk,l with k ≥ 2
and 0 < l ≤ ak. If ∥nα∥ < ∥qk,l−1α∥, then n = mqk−1 for some integer m such that 1 ≤ m ≤
min{l, ak − l + 1}.

Proof. Suppose that ∥nα∥ < ∥qk,l−1α∥, and assume for a contradiction that the point {nα} is on
the same side of 0 as {qk−2α}. Since n < qk,l, we conclude that n ̸= qk,r for r ≥ l. By (3) and our
assumption that ∥nα∥ < ∥qk,l−1∥, we see that n ̸= qk,r with 0 ≤ r ≤ l − 1. As ∥nα∥ > ∥qkα∥ by
(4), we infer that the point {nα} must lie between the points {qk,l′ α} and {qk,l′+1α} for some l′

such that 0 ≤ l′ < ak. The distance between the points {nα} and {qk,l′ } is less than ∥qk−1α∥. By
(4), it must be that qk,l′ ≥ qk; a contradiction.
Suppose for a contradiction that n is not a multiple of qk−1. Then the point {nα} lies between
the points {tqk−1α} and {(t + 1)qk−1α} for some t such that 0 < t < ⌊1/∥qk−1α∥⌋. As {nα} is on
the same side of 0 as the point {qk−1α}, it follows that ∥nα∥ > ∥tqk−1α∥ and ∥tqk−1α∥ = t∥qk−1α∥.
The distance between the points {nα} and {tqk−1α} is less than ∥qk−1α∥, so by (4) it must be that
tqk−1 ≥ qk = akqk−1 + qk−2. Thus necessarily t > ak. Using (3) we see that the distance between
the points {qkα} and {qk−2α} is ak∥qk−1α∥. Since ∥qkα∥ < ∥qk−1α∥, we infer that

∥qk,l−1α∥ ≤ ∥qk−2α∥ = ak∥qk−1α∥ + ∥qkα∥ < (ak + 1)∥qk−1α∥. (5)

Therefore by our assumption,

(ak + 1)∥qk−1α∥ > ∥qk,l−1α∥ > ∥nα∥ > t∥qk−1α∥,

so ak ≥ t; a contradiction. We have thus concluded that n = mqk−1 for some m ≥ 1.
Let us now analyze the upper bound on m. First of all, mqk−1 < qk,l exactly when m ≤ l ≤ ak.
It follows that ∥mqk−1α∥ = m∥qk−1α∥. By (3)

m∥qk−1α∥ < ∥qk,l−1α∥ = (ak − (l − 1))∥qk−1α∥ + ∥qkα∥,

so m ≤ ak − l + 1. We conclude that m ≤ min{l, ak − l + 1}.

The inequalities (3) and (5) imply that ak∥qk−1α∥ < ∥qk−2α∥ < (ak + 1)∥qk−1α∥. We derive
the following useful fact:
 ak = ⌊ ∥qk−2α∥
∥qk−1α∥
 ⌋ . (6)

We need the famous Three Distance Theorem (see e.g. [1] and the references therein).

Theorem 2.3 (The Three Distance Theorem). Let α be an irrational number, and let n > a1 be a positive
integer uniquely expressed in the form n = lqk−1 + qk−2 + r with k ≥ 2, 0 < l ≤ ak, and 0 ≤ r < qk−1.
The points 0, {α}, {2α}, . . . , {nα} partition the circle T into n + 1 intervals. There are exactly

3

• n + 1 − qk−1 intervals of length ∥qk−1α∥,

• r + 1 intervals of length ∥qk,l α∥, and

• qk−1 − (r + 1) intervals of length ∥qk,l−1α∥.

By (3) the intervals of the last type (if they exist) are the longest, and their length is the sum of
the two other length types.

3 Word Combinatorics and Sturmian Words

We mention here only few key concepts from combinatorics on words; good background refer-
ences are Lothaire’s books [9, 10].
A word is primitive if it is not a non-trivial power of some word. A word w is primitive if and
only if it occurs exactly twice in w2. The cyclic shift operator C is deﬁned by C(a1 · · · an−1an) =
ana1 · · · an−1 where the ai are letters. A word u is conjugate to v if Ci(v) = u for some i such
that 0 ≤ i < |v|. The reversal of the word w = a1 · · · an−1an where the ai are letters is the word
̃w = anan−1 · · · a1.
Sturmian words are a well-known class of inﬁnite, aperiodic binary words over {0, 1} with
minimal factor complexity. They are deﬁned as the (right-)inﬁnite words having n + 1 factors
of length n for every n ≥ 0. For our purposes it is more convenient to view Sturmian words
equivalently as the inﬁnite words obtained as codings of orbits of points in an irrational circle
rotation with two intervals [12, 10]. Let us make this more precise. The frequency α of letter 1
(called the slope) in a Sturmian words exists, and it is irrational. Divide the circle T into two
intervals I0 and I1 deﬁned by the points 0 and 1 − α, and deﬁne the coding function ν by setting
ν(x) = 0 if x ∈ I0 and ν(x) = 1 if x ∈ I1. The coding of the orbit of a point x is the inﬁnite
word sx,α obtained by setting its nth, n ≥ 0, letter to equal ν(Rn(x)) where R is the rotation by
angle α. This word is Sturmian with slope α, and conversely every Sturmian word with slope
α is obtained this way. To make the deﬁnition proper, we need to deﬁne how ν behaves in the
endpoints 0 and 1 − α. We have two options: either take I0 = [0, 1 − α) and I1 = [1 − α, 1) or
I0 = (0, 1 − α] and I1 = (1 − α, 1]. The difference is seen in the codings of the orbits of the special
points {−nα}, and both options are needed to be able to obtain every Sturmian word of slope α as
a coding of a rotation. However, in this paper we are not concerned about this choice. We make
the convention that I(x, y) with x, y ̸= 0 is either of the half-open intervals of T separated by the
points x and y (taken modulo 1 if necessary) not containing the point 0 as an interior point. The
interval I(x, 0) = I(0, x) is either of the half-open intervals separated by the points 0 and x having
smallest length (the case x = 1
2 is not important in this paper). Since the sequence ({nα})n≥0 is
dense in [0, 1)—as is well-known—every Sturmian word of slope α has the same language (that
is, the set of factors); this language is denoted by L(α). Thus to study repetitions, it is sufﬁcient
to analyze L(α). The fractional index indQ(w) of a nonempty factor w ∈ L(α) is deﬁned as

indQ(w) = sup{k ∈ Q : wk ∈ L(α)}

where the fractional power wk is the word (uv)nu with w = uv and k = n + |u|
|w| . The index ind(w)
of a nonempty factor w is deﬁned similarly by letting k take only integral values. The index of a
factor in L(α) is always ﬁnite. The fractional index of a Sturmian word with slope α is deﬁned to be

sup{indQ(w) : w ∈ L(α)}.

This quantity can be inﬁnite.
For every factor w = a0a1 · · · an−1 of length n there exists a unique subinterval [w] of T such
that sx,α begins with w if and only if x ∈ [w]. Clearly

[w] = Ia0 ∩ R−1(Ia1) ∩ . . . ∩ R−(n−1)(Ian−1).

4

We denote the length of the interval [w] by |[w]|. The points 0, {−α}, {−2α}, . . . , {−nα} partition
the circle into n + 1 intervals, which have one-to-one correspondence with the words of L(α) of
length n. Among these intervals the interval containing the point {−(n + 1)α} corresponds to
the right special factor of length n. A factor w is right special if both w0, w1 ∈ L(α). Similarly a
factor is left special if both 0w, 1w ∈ L(α). In a Sturmian word there exists a unique right special
and a unique left special factor of length n for all n ≥ 0. The language L(α) is mirror-invariant,
that is, for every w ∈ L(α) also ̃w ∈ L(α). It follows that the right special factor of length n is the
reversal of the left special factor of length n.
Given the continued fraction expansion of an irrational α ∈ (0, 1), we deﬁne the correspond-
ing standard sequence (sk)k≥0 of words by

s−1 = 1, s0 = 0, s1 = sa1−1
0 s−1, sk = sak
k−1sk−2, k ≥ 2.

As sk is a preﬁx of sk+1 for k ≥ 1, the sequence (sk) converges to a unique inﬁnite word cα
called the inﬁnite standard Sturmian word of slope α, and it equals sα,α. Inspired by the notion of
semiconvergents, we deﬁne semistandard words for k ≥ 2 by

sk,l = sl
k−1sk−2

with 1 ≤ l < ak. Clearly |sk| = qk and |sk,l| = qk,l. Every preﬁx of cα is left special, so in
particular, standard and semistandard words are left special. Every standard or semistandard
word is primitive [10, Proposition 2.2.3]. An important property of standard words is that the
words sk and sk−1 almost commute; namely sksk−1 = wab and sk−1sk = wba for some word w
and distinct letters a and b. For more information about standard words see Chapter 2 of [10]
and Berstel’s paper [2]. Here we see that the only difference between the words cα and cα where
α = [0; 1, a2, a3, . . .] and α = [0; a2 + 1, a3, . . .] is that the roles of the letters 0 and 1 are reversed.
Thus for the study of powers, we may assume without loss of generality that a1 ≥ 2.
For the rest of this paper we make the convention that the partial quotients of an irrational α
satisfy a0 = 0 and a1 ≥ 2, that is, 0 < α < 1
2 . Moreover, the words sk and sk,l refer to the standard
or semistandard words of slope α.

4 The Main Results

This section presents a complete description of powers occurring in a Sturmian word with slope
α. As a side-product, in Theorem 4.3 we obtain a description of conjugacy classes of length qk,l.
Finally, as an easy consequence of the established results, we obtain a formula for the fractional
index of a Sturmian word (Theorem 4.7).
The following important proposition shows the usefulness of Proposition 2.2 in the study of
Sturmian words and plays a role similar to Theorem 1 of [6].

Proposition 4.1. If w2 ∈ L(α) with w primitive, then |w| = qk for some k ≥ 0 or |w| = qk,l for some
k ≥ 2 with 0 < l < ak.

Proof. Let n = |w|. If n < q1 = a1, then the factors of length n are readily seen to be 0n and
the conjugates of 0n−11. Since the minimum number of letters 0 between two occurrences of
letter 1 in L(α) is a1 − 1 and the maximum number is a1, the only way w2 can be a factor is
that w = 0 = s0. Suppose then that n ≥ q1 and [w] = I(−iα, −jα) with 0 ≤ i, j ≤ n. We
may assume without loss of generality that w is right special, so {−(n + 1)α} ∈ [w]. Further,
since [w2] = [w] ∩ R−n([w]) ̸= ∅, then necessarily (depending on n) either [w2] = I(−iα, −(j +
n)α) or [w2] = I(−jα, −(i + n)α). We assume that [w2] = I(−iα, −(j + n)α); the other case is
symmetric. We wish to prove that the points {−(n + 1)α and {−(j + n)α} are actually the same
point. This is equivalent to saying that j = 1. Assume on the contrary that j ̸= 1. Let a be the
ﬁrst letter of w and b be a letter such that b ̸= a. Note that [w2] ⊂ [wa]. Now as w is right special,
[wa] = I(−jα, −(n + 1)α) and [wb] = I(−(n + 1)α, −iα). Let x ∈ [w2] and y ∈ [wa] \ [w2], and

5

let u be the longest common preﬁx of sx,α and sy,α. Since [w2] ̸= [wa], we have that |u| < 2|w|.
Moreover, u is right special, so w is a sufﬁx of u. However, w2 is a preﬁx of sx,α implying that u
is a preﬁx of w2. Thus w2 contains at least three occurrences of w contradicting the primitivity of
w. From this contradiction we conclude that j = 1. There are no points {−mα} in the interval
I(−(j + n)α, −jα) = I(−(n + 1)α, −α) with m ≤ n. Therefore the point {−nα} is the closest point
to 0 from either side. If q1 ≤ n < q2,1, then it must be that n = q1. Otherwise let k ≥ 2 be such
that qk,l ≤ n < qk,l+1 with 0 < l ≤ ak. By Proposition 2.2 either n = qk−1 or n = qk,l proving the
claim.

Indeed, for each length given in the statement of the previous proposition, there exists a factor
occurring as a square.

Lemma 4.2. We have that s2
0, s2
1 ∈ L(α) and s2
k,l ∈ L(α) for all k ≥ 2 and l such that 0 < l ≤ ak.

Proof. As s2
0 = 02 and s2
1 = (0a1−11)2, clearly s2
0, s2
1 ∈ L(α). Since the words sk+1sk and sksk+1
differ only by their last two letters, it follows that s2
k is a preﬁx of sk+1sk if k ≥ 2. As sk is a preﬁx
of sk+1 when k ≥ 0, the word sk,l = sl
k−1sk−2 is both a preﬁx and a sufﬁx of sk = sak
k−1sk−2 for all
k ≥ 2 and l such that 0 < l ≤ ak. Thus s2
k contains s2
k,l. The claim follows.

As was seen in the proof of Proposition 4.1, the index of a factor w of length n depends only
on the maximum r ≥ 0 such that R−tn(x) ∈ [w] for 0 ≤ t ≤ r where x is either of the endpoints of
[w]. That is, the index of a factor depends only on the length of its interval but not on its position.
To put it more precisely, if w is a factor of length n, then

ind(w) = γ + ⌊ |[w]|
∥|w|α∥
 ⌋ (7)

where γ is 1 if |[w]| ̸= ∥|w|α∥ and 0 otherwise. Next we will carefully characterize the lengths of
the intervals of factors of length qk,l. After this it is easy to conclude the main results.

Theorem 4.3. Let n = qk,l with k ≥ 2 and 0 < l ≤ ak. Then Ci(̃sk,l) ∈ L(α) for 0 ≤ i ≤ n − 1.
The intervals of the ﬁrst qk−1 − 1 conjugates of ̃sk,l have length ∥qk,l−1α∥, and the intervals of the latter
n + 1 − qk−1 conjugates have length ∥qk−1α∥. The interval of the remaining factor has length ∥qk,lα∥.

Proof. The geometric ideas of this proof are illustrated in the example following this proof. The
intervals of the factors of length n are called in this proof level n intervals. With the same effort we
prove here more than what is claimed above; we give the exact positions of the intervals of the
conjugates of ̃sk,l on the circle.
By Proposition 2.2 the interval J = I(−qk,l−1α, 0) has exactly one point {−tα} with 0 < t ≤ n
as an interior point; namely the point {−nα}. That is, the point {−nα} split the level n − 1
interval J into the level n intervals K = I(−qk,l−1α, −nα) and L = I(−nα, 0). Observe that
∥qk,l−1α∥ = |J| = |K| + |L| = ∥qk−1α∥ + ∥qk,l α∥. The Three Distance Theorem tells that level n
intervals have lengths ∥qk,l−1α∥, ∥qk,lα∥, and ∥qk−1α∥. In particular, interval L is the unique level
n interval of length ∥qk,l α∥. Let i be the smallest positive integer such that the interval R−i(J)
is not any interval of level n. The interval R−i(J) must be a union of two level n intervals: one
having length |K| and the other having length |L|. This is true as by (3) it can be deduced that |J|
is never a multiple of |K|; further, |K| is never a multiple of |L|. Since the interval of length ∥qk,l α∥
is unique, we conclude that the other interval in the union is L. As α is irrational, R−i(J) ̸= J, so
it must be that R−i(J) = M ∪ L where M = I(−qk−1α, 0). Therefore R−i maps the endpoint 0 of
L to the endpoint {−qk−1α} of M, so i = qk−1. As k > 1, also i > 1. We have shown that the level
n intervals R−1(J), R−2(J), . . . , R−(i−1)(J) have length |J| = ∥qk−1,lα∥. By the Three Distance
Theorem the remaining n + 1 − qk−1 intervals excluding L have length ∥qk−1α∥.
What remains is to analyze the connection between rotation and conjugation. Let u and v
be factors of length n such that [u] = M and [v] = L. Since the intervals M and L are on the
opposite sides of 0, we have that u = au′ and v = bv′ for distinct letters a and b. Let x ∈ M and

6
 0

−α
 {−nα}

v = 00100

00101

s = 01001

01010
 ̃s = 10010
 10100

J = R([ ̃s ]) R−1([s])

1
 1
 2

2
 2

3

Figure 1: An example of the geometric ideas in the proof of Theorem 4.3.

y ∈ L. Since i > 1, the interval R−(i−1)(J) = R(M ∪ L) is the interval of some factor w of length
n. Therefore the Sturmian words sx+α,α and sy+α,α both have w as a preﬁx. Thus sx,α begins with
aw and sy,α begins with bw. Hence w must be left special, that is, w = sk,l. We will show next that
v is not conjugate to sk,l. Note that k − 1 is odd if and only if {−qk−1α} ∈ I0. Hence the ﬁrst letter
of v is 0 if and only if k − 1 is odd. On the other hand, the last letter of sk,l is 0 if and only if k − 1
is even. Thus we conclude that the ﬁrst letter of v is distinct from the last letter of sk,l. However,
as the sufﬁx of v of length n − 1 is a preﬁx of sk,l, we see that there are more letters b in v than
there are in sk,l, so v and sk,l cannot be conjugate.
Let then z be the factor of length n such that [z] = R−1(J). Since {−nα} ∈ J, it must be that
{−(n + 1)α} ∈ R−1(J) = [z]. Thus z is right special, that is, z = ̃sk,l. By Lemma 4.2 s2
k,l ∈ L(α).
Thus every conjugate of sk,l is a factor. Further, by the mirror-invariance of L(α), we see that sk,l
and ̃sk,l are conjugates. Moreover, every conjugate of ̃sk,l is extended to the left by its last letter.
Suppose that λ ̸= v is a factor of length n such that R−1([λ]) is the interval of some factor µ of
length n. As R−1([sk,l]) does not satisfy this condition, it follows that λ ̸= sk,l, so λ extends to the
left uniquely. We will prove that C(λ) = µ. Write λ = λ′c for some letter c. Then obviously µ =
dλ′ for some letter d. By deﬁnition µ must be followed by the letter c, that is, µc = dλ′c = dλ ∈
L(α). We have that d = c because λ is uniquely extended to the left by its last letter. Therefore
we conclude that C(λ) = µ. In this way we see that the factors of length n having the intervals
R−1(J), R−2(J), . . . , R−(i−1)(J) correspond (in order) to the factors ̃sk,l, C(̃sk,l), . . . , Cqk−1−2(̃sk,l) =
sk,l. We saw above that v is not conjugate to sk,l, so it must be that C(sk,l) = u. Thus the factors
of length n having the intervals [u] = L, R−1(L), R−2(L), . . . , R−(n−qk−1)(L) correspond (in order)
to the factors u, C(u), C2(u), . . . , Cn−qk−1(u). As u = C(sk,l) = Cqk−1−1(̃sk,l), we have a complete
description of the positions of the intervals of conjugates of ̃sk,l using the backward orbit of J
under R.

Example 4.4. Let α = [0; 2, 1] = 1
2 (√
3 − 1) (that is, the continued fraction expansion of α has
period 2, 1). Consider the semiconvergent p3,1
q3,1 = 1+1
3+2 = 2
5 of α and factors of length n = 5. The
factors of length n are 00100, 00101, 01001, 01010, 10010, and 10100. Their intervals are depicted
in Figure 1. There are intervals of type 1, 2, and 3 depending on their length. Intervals of type
1 have length ∥2α∥, intervals of type 2 have length ∥3α∥, and the interval of type 3 has length
∥2α∥ − ∥3α∥ = ∥5α∥. As in the proof of Theorem 4.3, the point {−nα} has split the type 1
interval J = I(0, −2α) into intervals of type 2 and 3. The interval R−1(J) corresponds to the right
special factor ̃s = ̃s3,1. The arrows in the ﬁgure indicate how conjugation acts on ̃s. The backward
orbit of J corresponds to conjugates of ̃s of type 1 until the interval of the left special factor s
is encountered. As seen in the proof of Theorem 4.3, the interval R−1([s]) no longer coincides

7

with any interval of length n. Here R−1([s]) = L ∪ M = I(0, −nα) ∪ I(0, −3α) just as the proof
requires. The factor having interval L is here seen to be not conjugate to ̃s as it should be by the
proof. The interval M must then correspond to the conjugate of s. As in the proof, the rest of
the conjugates of ̃s are obtained by rotating M backwards. The intervals obtained this way are of
type 2.

We are now ready to prove the main result. The result was originally proven by Damanik and
Lenz [6]. We present it here phrased in a different way.

Theorem 4.5. Consider indices of factors of length n > 0 in L(α), and let k ≥ 2.

(i) If n < q1, then the index of the conjugates of 0n−11 is 1, and the index of the remaining factor 0n is
⌊a1/n⌋.

(ii) If n = q1, then the index of the conjugates of ̃s1 is a2 + 1, and the index of the remaining factor 0a1
is 1.

(iii) If n = qk, then the index of any of the ﬁrst qk−1 − 1 conjugates of ̃sk is ak+1 + 2, the index of any of
the remaining n + 1 − qk−1 conjugates is ak+1 + 1, and the index of the remaining factor is 1.

(iv) If n = qk,l with 0 < l < ak, then the index of the ﬁrst qk−1 − 1 conjugates of ̃sk,l is 2, and the index
of the remaining factors is 1.

(v) If n = mq1 with 1 < m < a2 + 1, then the index of any of the ﬁrst q1 conjugates of ̃s m
1 is
⌊(a2 + 1)/m⌋, and the index of any remaining factor is 1.

(vi) If n = mqk with 1 < m < ak+1 + 2, then the index of any of the ﬁrst qk−1 − 1 conjugates of ̃s m
k is
⌊(ak+1 + 2)/m⌋, the index of any of the next qk + 1 − qk−1 conjugates is ⌊(ak+1 + 1)/m⌋, and
the index of any remaining factor is 1.

(vii) If n does not fall into any of the above cases, then the index of every factor of length n is 1.

Proof. First of all, observe that all the cases (i)–(vii) are mutually exclusive. Consider the cases (i)
and (ii). The factors of length n ≤ q1 are readily seen to be 0n and the conjugates of 0n−11. As the
index of 0 is a1, the index of the factor 0n is ⌊a1/n⌋. The intervals of the conjugates of 0n−11 have
length α. If n = 1, then the index of the factor 0n−11 = 1 is 1. If n > 1, the number 1 + ⌊α/∥nα∥⌋
equals 1 unless n = q1 when it equals a2 + 1 by (6). The claims of (i) and (ii) follow from (7).
Consider next a factor w of length n = qk,l for some k ≥ 2 and l such that 0 < l ≤ ak. By
Theorem 4.3, the intervals of the ﬁrst qk−1 − 1 conjugates of ̃sk,l have length ∥qk,l−1α∥. Using (7)
and (3) we see that their index equals to

1 + ⌊ ∥qk,l−1α∥
∥qk,l α∥
 ⌋ = 1 + ⌊ ∥qk,lα∥ + ∥qk−1α∥
∥qk,l α∥
 ⌋ = 2 + ⌊ ∥qk−1α∥
∥qk,lα∥
 ⌋ .

If l ̸= ak, then by (4) ∥qk,lα∥ > ∥qk−1α∥, so the index is 2. If l = ak, then by (6), the index equals
to 2 + ak+1. This proves the ﬁrst claims in (iii) and (iv). The latter cases are analogous, so (iii) and
(iv) are proved.
Proposition 4.1 shows that the factors not covered by the cases (i)–(iv) having index higher
than 1 must be nonprimitive. By (i) and (iv) they must have length mqk for some k ≥ 1, meaning
that we are in either of the cases (v) or (vi). It is a straightforward application of (ii) and (iii) to
deduce (v) and (vi). The theorem is proved.

In particular, every Sturmian word contains inﬁnitely many cubes, but fourth powers are
avoidable. The theorem implies the following weaker version which is still useful (compare to
[5, Lemma 3.6]):

Corollary 4.6. Let w ∈ L(α) be primitive. If w2 ∈ L(α), then w is conjugate to sk for some k ≥ 0 or to
sk,l with k ≥ 2 and 0 < l < ak. If w3 ∈ L(α), then either w = 0 and a1 > 2 or w is conjugate to some sk
with k ≥ 1.
 8

We obtain the result of [5], [3], and [7] on the fractional index of Sturmian words as a direct
consequence of the results so far:

Theorem 4.7. The fractional index of a Sturmian word with slope α is

max
 {
a1, 2 + sup
k≥2 {ak + (qk−1 − 2)/qk}
}
 .

Proof. The largest fractional power of a factor with length less than q1 is clearly 0a1. Therefore by
Theorem 4.5 it is sufﬁcient to analyze the largest fractional power of a (primitive) factor of length
qk for k ≥ 1. By Theorem 4.5 the index ak+1 + 2 of the ﬁrst qk−1 − 1 conjugates of ̃sk dominates
the index of the rest of the factors of length qk. The fractional part of the fractional index of a
factor w is determined by the shortest extension of w to a right special factor. Note that from the
proof of Theorem 4.3 it is evident that Cqk−1−2(̃sk) = sk. Thus among the ﬁrst qk−1 − 1 conjugates
of ̃sk, the factor sk has longest extension to a right special factor, and the length of the extension
is qk−1 − 2. Thus the fractional index of sk is ak+1 + 2 + (qk−1 − 2)/qk. The claim follows.

In particular, this theorem says that that a Sturmian word has bounded fractional index if
and only if the partial quotients of its slope are bounded. This is a result of Mignosi [11]. An
alternative proof was given by Berstel [2].

5 Acknowledgments

The author was supported by University of Turku Graduate School UTUGS Matti programme.
We thank Markus Whiteland, Tero Harju, and Luca Zamboni for giving fruitful feedback on
the draft version of this paper.

References

[1] P. Alessandri and V. Berthé. Three distance theorems and combinatorics on words. Enseign. Math. 44
(1998), 103–132.

[2] J. Berstel. On the index of Sturmian words. In: Jewels Are Forever. Springer-Verlag, 1999, pp. 287–294.

[3] A. Carpi and A. de Luca. Special factors, periodicity, and an application to Sturmian words. Acta Inf.
36 (2000), 983–1006. DOI: 10.1007/PL00013299.

[4] J. W. S. Cassels. An Introduction to Diophantine Approximation. Cambridge Tracts in Mathematics and
Mathematical Physics 45. Cambridge University Press, 1957.

[5] D. Damanik and D. Lenz. The index of Sturmian sequences. Eur. J. Combin. 23 (2002), 23–29. DOI:
10.1006/eujc.2000.0496.

[6] D. Damanik and D. Lenz. Powers in Sturmian sequences. Eur. J. Combin. 24 (2003), 377–390. DOI:
10.1016/S0195-6698(03)00026-X.

[7] J. Justin and G. Pirillo. Fractional powers in Sturmian words. Theoret. Comput. Sci. 255 (2001), 363–376.

DOI: 10.1016/S0304-3975(99)90294-3.

[8] A. Y. Khinchin. Continued Fractions. Dover Publications, Mineola, New York, 1997.

[9] M. Lothaire. Combinatorics on Words. Encyclopedia of Mathematics and Its Applications 17. Addison-
Wesley, 1983.

[10] M. Lothaire. Algebraic Combinatorics on Words. Encyclopedia of Mathematics and Its Applications 90.
Cambridge University Press, 2002.

[11] F. Mignosi. Inﬁnite words with linear subword complexity. Theoret. Comput. Sci. 65 (1989), 221–242.

DOI: 10.1016/0304-3975(89)90046-7.

[12] N. Pytheas Fogg. Substitutions in Dynamics, Arithmetics and Combinatorics. Lecture Notes in Mathemat-
ics 1794. Springer, 2002. DOI: 10.1007/b13861.

[13] D. Vandeth. Sturmian words and words with a critical exponent. Theoret. Comput. Sci. 242 (2000), 283–
300. DOI: 10.1016/S0304-3975(98)00227-8.
 9
