<!-- source: https://dmtcs.episciences.org/450/pdf | converted from PDF -->

Discrete Mathematics and Theoretical Computer Science DMTCS vol. 11:1, 2009, 153–172

Diophantine Approximation, Ostrowski
Numeration and the Double-Base Number

Val´erie Berth´e
1 and Laurent Imbert
12

1 CNRS, LIRMM, Universit´e Montpellier 2, 161 rue Ada, 34390 Montpellier, France
2 CNRS, PIMS, Centre for Information Security and Cryptography, University of Calgary, 2500 University Drive NW,
Calgary, AB, T2N 1N4, Canada

received July 16, 2008, revised January 15, 2009, accepted March 6, 2009.

A partition of x > 0 of the form x = P

i 2
ai 3
bi with distinct parts is called a double-base expansion of x. Such a rep-
resentation can be obtained using a greedy approach, assuming one can efﬁciently compute the largest {2, 3}-integer,
i.e., a number of the form 2
a3
b, less than or equal to x. In order to solve this problem, we propose an algorithm
based on continued fractions in the vein of the Ostrowski number system, we prove its correctness and we analyse
its complexity. In a second part, we present some experimental results on the length of double-base expansions when
only a few iterations of our algorithm are performed.

Keywords: Double-base number system, Ostrowski numeration, diophantine approximation

1 Introduction

In this paper, we consider representations of integers in two coprime bases. More exactly, we analyze
decompositions of positive integers in the form

x =
 ℓ∑

i=1 2
ai3bi, (1)

with ai, bi ≥ 0 and (ai, bi) ̸= (aj, bj) if i ̸= j.
Apart from its practical interest in real life applications such as digital signal processing [13] and
cryptography [10, 14], this so-called double-base number system (DBNS) has many intriguing properties
and leads to interesting Diophantine approximation problems. We focus on bases 2 and 3 but most of the
results and algorithms presented in this paper remain valid for arbitrary bases.
Clearly, such a decomposition always exists, the binary expansion is a special case of (1). In fact,
this number system is even extremely redundant. For a given integer x > 0, the number f (x) of DBNS

1365–8050 c⃝ 2009 Discrete Mathematics and Theoretical Computer Science (DMTCS), Nancy, France

154 Val´erie Berth´e and Laurent Imbert

representations is given by (see [11] for more details):

f (x) =
 

1 if x = 1,
f (x − 1) + f (x/3) if x ≡ 0 (mod 3),
f (x − 1) otherwise.

It is not difﬁcult to see that the elements of this sequence go by triples and correspond to the number of
partitions of 3x into powers of 3, also called ternary partitions (see [3] and the sequence #A005704 from
the on-line encyclopedia of integer sequences), whose ﬁrst terms are:

1, 2, 3, 5, 7, 9, 12, 15, 18, 23, 28, 33, 40, 47, 54, 63, 72, 81, 93, 105, 117, . . .

For a given x > 0, ﬁnding an expansion of minimal length ℓ (i.e., it is not possible to write x with
ℓ − 1 or fewer terms) is believed to be a difﬁcult problem. Those representations of minimal length are
extremely sparse. For example, among its 783 representations, the integer 127 can be written as a sum of
exactly three terms in 6 different ways:

127 = 2
23
3 + 2
13
2 + 2
03
0 = 108 + 18 + 1

127 = 2
23
3 + 2
43
0 + 2
03
1 = 108 + 16 + 3

127 = 2
53
1 + 2
03
3 + 2
23
0 = 96 + 27 + 4

127 = 2
33
2 + 2
13
3 + 203
0 = 72 + 54 + 1

127 = 2
63
0 + 213
3 + 203
2 = 64 + 54 + 9

127 = 2
630 + 223
2 + 2
03
3 = 64 + 36 + 27

This observation suggests that 127 cannot be expressed with fewer than three terms. In fact, the smallest
integer requiring three summands is 23 (as pointed out in [27] by Tijdeman); the smallest integer requiring
four summands is 431. Similarly, the next smallest numbers requiring ﬁve, six and seven summands are
18431, 3448733, and 1441896119 (a 21-bit integer), respectively.
For large numbers, such as those used in cryptographic applications, ﬁnding a representation of minimal
length, in a reasonable amount of time, seems very hard. Fortunately, one can use a greedy approach (see
Algorithm 1) to ﬁnd a fairly sparse representation very quickly, based on the determination of the best
default approximation of x (i.e., the largest integer ≤ x) of the form z = 2
a3
b.

Algorithm 1 Greedy decomposition
Input : An integer x > 0
Output : The sequence of exponents (ai, bi)i>0 s.t. x = ∑ℓ=1 2ai3bi as in (1)
1: while x ̸= 0 do

2: Find the best default approximation of x of the form z = 2
a3
b

3: Print (a, b)
4: x := x − z

Although it sometimes fails in ﬁnding a minimal representation (the smallest example is 41: the mini-
mal representation is 32 + 9, whereas Algorithm 1 returns 41 = 36 + 4 + 1), it is very easy to implement.

Ostrowski numeration and DBNS 155

More importantly, it guarantees an expansion of sublinear length ℓ. Indeed, an important theorem from
Dimitrov [12] states that ℓ is in O(log x/ log log x). The proof is based on a result by Tijdeman [26],
which says that there exists an absolute constant C such that there is always a number of the form 2a3b in
the interval [
x − x/(log x)
C, x
]
. See [12] for a complete proof.
In this paper we investigate the problem of ﬁnding the best default approximation of x of the form
z = 2
a3b. This operation is clearly of crucial importance for Algorithm 1. We present an algorithm as
well as inhomogeneous approximation results in the vein of a number system from Ostrowski [20], which
uses the series of convergents of the continued fraction expansion of an irrational number.
We introduce the problem in Diophantine terms in Section 2 and recall basic facts on Ostrowski’s
numeration in Section 3. In Section 4, we describe our algorithm and prove its correctness. Moreover,
we show that for all x of bounded binary length, our algorithm terminates in O(log log x) iterations. The
natural extension to signed digits and some implementation considerations are discussed in Section 5. We
then conclude by presenting some numerical experiments in Section 6. The present paper is an extended
version of [7].

2 Problem and notationx ≥ 2 be a given positive integer. We want to ﬁnd two integers a, b ≥ 0 such that 2
a3
b ≤ x and
among the solutions to this problem, 2
a3
b is the largest possible value. In other words

2
a3
b = max {2
c3
d ≤ x : (c, d) ∈ N2} . (2)

Equivalently, one can solve the following Diophantine inequality in non-negative integers

a log 2 + b log 3 ≤ log x, (3)

with the constraint that no other integers c, d ≥ 0 give a better left approximation to log x; meaning that
if (a, b) is a maximal solution of (3), then for all integers c, d with (c, d) ̸= (a, b), we have

cα + d < aα + b ≤ log3 x, where α = log3 2.

In the following, {t} denotes the fractional part of t. Graphically, the solutions to cα + d ≤ log3 x are
the points (c, d) with non-negative integer coordinates located under the line of equation

v = −αu + log3 x.

These are the integer points in the gray area of Figure 1. Among those points, the best left approximationx we are looking for is the point (a, b), which has the smallest vertical distance to the line, that we
denote by δ(u) = {−αu + log3 x}, for u ≥ 0.
A naive approach consists in computing δ(u) for every integer 0 ≤ u ≤ log2 x and to keep the point
(u, v) which gives the smallest value. Since log3 x < log2 x, a little more efﬁcient solution is to exchange
the coordinate axis, i.e., to consider the line v′ = u′/α − log2 x, and to keep the closest point among
all integers 0 ≤ u′ ≤ log3 x (we perform here the change of coordinates system u′ = v, v′ = −u).
Let us note that in some cases, it may be interesting to compute the best right approximation, i.e., the
smallest integer of the form 2
a3
b greater than x. Observe that it can be easily obtained by symmetry, by
looking for the point (a
′, b
′) located under and with the smallest vertical distance to the line of equation
v′ = −αu
′ + α⌈log2 x⌉ + ⌈log3 x⌉ − log3(x) (the dashed line in Figure 1), and to apply the change of
coordinates system u = ⌈log2 x⌉ − u′, v = ⌈log3 x⌉ − v′.

156 Val´erie Berth´e and Laurent Imbert

u

v
 u′
 v′

(2, 4)
 (7, 1)

(2, 5)

Fig. 1: Graphical interpretation of the problem

Example 1 In Figure 1, we consider an example with x = 358. We have log2 x ≈ 8.48, log3 x ≈ 5.35.
The best left approximation is the point of coordinates (2, 4). Similarly the closest point below the dashed
line is the point (2, 5), which by symmetry gives the best right approximation: (9 − 2, 6 − 5) = (7, 1). We
easily verify that 2α + 4 ≈ 5.26 < log3 x < 7α + 1 ≈ 5.41.

The complexity of all those graphical approaches is O(log x). In the next sections, we give an algorithm
which solves the problem in O(log log x).

In the following, we deﬁne β = {log3 x}. We assume 0 < β < 1. Indeed, if β = 0, then we take a = 0
and b = log3 x ∈ N. Clearly, if (a, b) is a maximal solution of (3), then we have

⌊log3 x⌋ ≤ aα + b ≤ β + ⌊log3 x⌋,

with 0 ≤ a ≤ ⌊log2 x⌋ and 0 ≤ b ≤ ⌊log3 x⌋. Indeed, the pair (c, d) = (0, ⌊log3 x⌋) is a solution which
provides cα + d = ⌊log3 x⌋.
Let us brieﬂy describe the strategy followed in the present paper. We set k = a and l = ⌊log3 x⌋ − b.
We have 0 ≤ kα − l ≤ β.
We thus are looking for (k, l) ∈ N2 such that 0 ≤ kα − l ≤ β and

kα − l = max
(r,s)∈N2 {rα − s : 0 ≤ rα − s ≤ β, 0 ≤ r ≤ ⌊log2 x⌋, 0 ≤ s ≤ ⌊log3 x⌋} . (4)

We shall deﬁne two increasing sequences (kn)n≥0, (ln)n≥0 such that, for some j > 0, kj = k, lj = l
satisfy (4). We then set a = k and b = ⌊log3 x⌋ − l to get the solution of (2).

Ostrowski numeration and DBNS 157

We will consider this classical inhomogeneous approximation problem in Section 4, where the sequence
of inhomogeneous best approximations of β by points of the form N α will be explicitly given. For that
purpose, we ﬁrst introduce Ostrowski’s number system.

3 Ostrowski’s number system

In this section we introduce a number system due to Ostrowski [20]. Let us ﬁrst recall some basic facts
about continued fractions (see [17] for more details).
A simple continued fraction is an expression of the form

α = a0 + 1

a1 + 1

a2 + 1
a3 + · · ·

,

where a0 = ⌊α⌋ and a1, a2, . . . are integers ≥ 1. The sequence (an)n∈N of partial quotients can either be
ﬁnite or inﬁnite.
Every rational number α can be expressed as a ﬁnite simple continued fraction, denoted by α =
[a0, a1, . . . , an] in the more convenient compact notation. Similarly, every irrational number α can be
expressed uniquely as an inﬁnite simple continued fraction. We write α = [a0, a1, a2, . . . ]. For example,
the continued fraction decomposition of log 2/ log 3 = 0.630929753571 . . . is

log3 2 = [0, 1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, . . . ].

The rational number obtained by restricting the continued fraction of α to its ﬁrst n + 1 partial quotients

pn
qn = [a0, a1, a2, . . . , an]

is called the nth convergent of α. The integers pn, qn are easily computable; we have p−1 = 1, q−1 = 0,
p0 = a0, q0 = 1, and
 pn+1 = an+1 pn + pn−1
qn+1 = an+1 qn + qn−1.

It is well known that the sequences (pn)n≥0, (qn)n≥0 satisfy limn→∞ pn/qn = α and pn+1qn−pnqn+1 =
(−1)
n. Moreover, simple continued fractions provide the sequence of best rational approximations of an
irrational number.
Ostrowski’s number system [20] (see [2] for an introduction) is associated with the numeration scale
(qn)n≥0 of denominators of the convergents of the continued fraction expansion of an irrational number
0 < α < 1. The following proposition holds.

Proposition 1 Let 0 < α < 1 be an irrational number. Every integer N can be written uniquely in the
form
 N =
 m∑

k=1 bkqk−1,

where 0 ≤ b1 ≤ a1 − 1; 0 ≤ bk ≤ ak, for k ≥ 2 and bk = 0 if bk+1 = ak+1.

158 Val´erie Berth´e and Laurent Imbert

For example, for α = 1+√5
2 = [1, 1, 1, 1, . . . ], the sequence (qn)n≥0 corresponds to the Fibonacci
numbers [28]. The unicity condition bk = 0 if bk+1 = ak+1 means that we do not have two consecutive
ones in the corresponding Zeckendorf representation [29].
Ostrowski’s representation of integers can be extended to real numbers (see e.g. the survey [5]). The
base is given by the sequence (θn)n≥0, where θn = qnα − pn. Note that the sign of θn is equal to (−1)
n.

Proposition 2 Let 0 < α < 1 be an irrational number. Every real number −α ≤ β < 1 − α can be
written uniquely in the form
 β =
 +∞∑

k=1 bkθk−1,

where 0 ≤ b1 ≤ a1 − 1; 0 ≤ bk ≤ ak, for k ≥ 2; bk = 0 if bk+1 = ak+1, and bk ̸= ak for inﬁnitely many
odd integers.

Proposition 2 can be used to approximate β modulo 1 by numbers of the form N α, with N ∈ N.
Indeed, one veriﬁes that the integers
 Nn =
 n∑

k=1 bkqk−1

provides a series of arbitrarily good approximations to β on both sides, i.e., the fractional part of Nnα can
either be greater or smaller than β.
If we are only interested in the best left approximations to β, which is our case, we can express β in
base (|θn|)n≥0 (see Section 4 below for the exact deﬁnition of best left approximations). The following
proposition holds.

Proposition 3 Let 0 < α < 1 be an irrational number. Every real number 0 ≤ β < 1 can be written
uniquely in the form
 β =
 +∞∑

k=1 dk|θk−1|,

where 0 ≤ dk ≤ ak for k ≥ 1; dk+1 = 0 if dk = ak and dk ̸= ak for inﬁnitely many even and odd
integers.

In this case, the sequence of best left approximations is more difﬁcult to deﬁne due to the alternating
signs of θn. Indeed, the corresponding numeration system on integers is deﬁned with respect to the
numeration scale ((−1)
nqn)n≥0. Nevertheless, none of these expansions provides the sequence of best
left approximations (see Remark 3 below for more details). In the next sections, we present an algorithm
inspired by [22] and [6], we prove its correctness and analyse its complexity.

4 The sequence of inhomogeneous best approximations of β

From now on we assume α irrational, 0 < α < 1 and 0 < β ≤ 1. Inhomogeneous left approximations
of β are numbers of the form kα + l ≤ β, with k, l integers. Clearly, there exist inﬁnitely many such
approximations. We want to deﬁne two increasing sequences of integers (kn)n≥0 and (ln)n≥0, such that

0 < knα − ln < kn+1α − ln+1 < β,

Ostrowski numeration and DBNS 159

and, furthermore, ∀k < kn+1, k ̸= kn, and ∀l ∈ Z such that 0 ≤ kα − l ≤ β, we have

0 < kα − l < knα − ln < β.

For simplicity, we deﬁne fn = |θn| for all n. We have f−1 = 1, f0 = α, f1 = 1 − a1α, and for n ∈ N

fn−1 = an+1fn + fn+1. (5)

One has fn > 0 for all n, since α is irrational. Hence, the sequence (fn−1 + fn)n≥0 is strictly decreasing
and tends to zero. Since 0 < β ≤ 1, there exists a unique integer n ≥ 0 such that

fn + fn+1 < β ≤ fn−1 + fn. (6)

Before we give the algorithm that deﬁnes the series of inhomogeneous best left approximations of β, we
need to prove the following two lemmas.

Lemma 1 Let 0 < β ≤ 1 and (fn)n≥0 be deﬁned as above. There exists a unique integer n ≥ 0, a
unique integer c ≥ 1, and a unique e ∈ R such that

β = cfn + fn+1 + e, (7)

with 0 < e ≤ fn, and 1 ≤ c ≤ a1 − 1 if n = 0, 1 ≤ c ≤ an+1 if n ≥ 1.

Proof: If n ∈ N satisﬁes (7), then fn + fn+1 < β ≤ fn−1 + fn, and n is uniquely determined since
(fn + fn+1)n≥−1 is strictly decreasing. Now, let n ∈ N be the unique integer that satisﬁes fn + fn+1 <
β ≤ fn−1 + fn. If n ≥ 1, then fn + fn+1 < β ≤ an+1fn + fn+1 + fn by (5). If n = 0, then
f0 + f1 < β ≤ 1 = f−1 = (a1 − 1)f0 + f1 + f0. (Note that a1 ≥ 2 in this case.) ✷

Lemma 2 Let α irrational, 0 < α < 1. Let 0 < β ≤ 1 and (fn)n≥0 be deﬁned as above, and let n, c, e
be the unique numbers satisfying (7). We deﬁne k, l ∈ N by setting

(k, l) =
 {
(qn, pn) if n is even,
(−cqn + qn+1, −cpn + pn+1) if n is odd.

Then we have 0 < kα − l < β.

Proof: Let us prove that 0 < β − (kα − l) < β. Assume ﬁrst that n is even. In this case, qnα − pn = fn.
We have β − (kα − l) = β − fn, and thus 0 < β − (kα − l) < β. Now, if n is odd, qnα − pn = −fn
and thus β − (kα − l) = β + c(qnα − pn) − (qn+1α − pn+1) = β − cfn − fn+1 = e, and thus,
0 < β − (kα − l) ≤ fn < β. ✷

Algorithm 2 below computes the inﬁnite sequence (knα − ln)n≥1 of inhomogeneous best left approx-
imations to β.

160 Val´erie Berth´e and Laurent Imbert

Algorithm 2 Inhomogeneous best left approximations to β
Input : Two real numbers 0 < α < 1 and 0 < β ≤ 1, with α irrational
Output : The inﬁnite sequence (ki, li)i≥1 of best left approximations to β with 0 < kiα − li < β, ∀i
1: (k0, l0) := (0, 0)
2: while true do
3: Compute ni, ci, ei such that β − (kiα − li) = cifni + fni+1 + ei
4: if ni is even then

5: (ki+1, li+1) := (ki + qni, li + pni)
6: else
7: (ki+1, li+1) := (ki − ciqni + qni+1, li − cipni + pni+1)

This algorithm is inspired by [22]; similar ones can be found in [23, 24, 25]. Note that β−(ki+1α−li+1)
is equal to ei if ni is odd, and to (ci − 1)fni + fni+1 + ei, if ni is even. Hence, we may have ni+1 = ni.
This happens if and only if ni is even and ci > 1; it therefore happens (ci − 1) times before the sequence
(ni) keeps growing towards +∞. We thus have

β = ∑

ni even cifni + ∑

ni odd(cifni + fni+1). (8)

The following proposition proves the correctness of Algorithm 2.

Proposition 4 Let 0 < α < 1 and 0 < β ≤ 1 be given. We assume α irrational. The increasing
sequences of integers (ki)i≥0 and (li)i≥0 provided by Algorithm 2 satisfy

0 < kiα − li < ki+1α − li+1 < β, ∀i ≥ 0 (9)

and furthermore, for all i, for all k such that ki < k < ki+1, and for all l ∈ Z such that 0 ≤ kα − l < β,
then 0 ≤ kα − l < kiα − li < β. (10)

Proof: We ﬁrst prove (9). From Lemma 2, we know that, for all i, 0 < kiα − li < β. We consider two
cases:

1. If ni is even, then β > ki+1α − li+1 = kiα − li + qniα − pni = kiα − li + fni > kiα − li > 0.

2. If ni is odd, then β > ki+1α − li+1 = kiα − li − ci(qniα − pni) + qni+1α − pni+1 = kiα − li +
cifni + fni+1 > kiα − li > 0.

Let us now prove (10). Let us assume that ki < k < ki+1, and 0 ≤ kα − l < β. By rewriting β − (kα −
l), we get that 0 ≤ β −(kα−l) = β −(kiα−li)+(kiα−li −ki+1α+li+1)+(ki+1α−li+1 −kα+l) < β.
What we prove in the next two cases depending on the parity of ni, is that β − (kα − l) > β − (kiα − li).

1. Assume ﬁrst that ni is even. We have

β − (kα − l) = β − (kiα − li) − fni + (ki+1α − li+1 − kα + l).

Ostrowski numeration and DBNS 161

Thus, what remains to be proved is that (ki+1α − li+1 − kα + l) is greater than fni. Since |ki+1 −
k| < |ki+1 − ki| = qni, one has |ki+1α − li+1 − kα + l| > fni (we use the best approximation
property of continued fractions, see e.g. [8]). Next we show that (ki+1α − li+1 − kα + l) cannot
be negative by considering two cases. Note ﬁrst that, from (5) and line 3 of Algorithm 2, we haveβ − (kiα − li) − fni| ≤ fni−1.

(a) If ki+1 − k ̸= qni−1, then |(ki+1α − li+1 − kα + l)| > fni−1, and since 0 ≤ kα − l < β,
we have (ki+1α − li+1 − kα + l) > 0.

(b) If ki+1−k = qni−1, since ni−1 is odd, we have (ki+1α−li+1−kα+l) = (qni−1α−pni−1) =
−fni−1 < 0. And we get β − (kα − l) = β − (kiα − li) − fni − fni−1 ≤ 0, which contradicts
the hypothesis.

2. If we now assume that ni is odd, we have

β − (kα − l) = β − (kiα − li) − (cifni + fni+1) + (ki+1α − li+1 − kα + l).

Here, what remains to be proved is that (ki+1α − li+1 − kα + l) is greater than cifni + fni+1. Since
|ki+1 − k| < |ki+1 − ki| = qni+1 − ciqni, we have |ki+1α − li+1 − kα + l| > fni+1 + cifni. We
know from (7) and Algorithm 2, that |β − (kiα − li) − cifni − fni+1| ≤ fni. Hence (ki+1α −
li+1 − kα + l) > 0, which implies (ki+1α − li+1 − kα + l) > cifni + fni+1.

Thus, in both cases β − (kα − l) > β − (kiα − li), which concludes the proof. ✷

As stated in Section 2, we want to ﬁnd two integers a, b ≥ 0 such that

2
a3
b = max {2
c3
d : (c, d) ∈ N2, and 2
c3
d ≤ x
} .

Let (a, b) ∈ N2 be one of the solutions of the equivalent Diophantine inequality

a log 2 + b log 3 ≤ log x.

Let α = log3 2 (note that α is irrational and 0 < α < 1), and β = {log3 x}. Recall that we assume
0 < β < 1. We have aα + b ≤ β + ⌊log3 x⌋ with 0 ≤ a ≤ ⌊log2 x⌋ and 0 ≤ b ≤ ⌊log3 x⌋.
Now, we use a slightly modiﬁed version of Algorithm 2 (see Remark 4, below) to compute (k, l) ∈ N2

such that 0 ≤ kα − l ≤ β and

kα − l = max
(r,s)∈N2 {rα − s : 0 ≤ rα − s ≤ β, 0 ≤ r ≤ ⌊log2 x⌋, 0 ≤ s ≤ ⌊log3 x⌋} .

Proposition 5 Let x ≥ 2 be a ﬁxed positive integer. Let α = log3 2; note that α is irrational and
0 < α < 1. Let β = {log3 x}. We assume furthermore that β ̸= 0. Let (kn, ln)n∈N be the sequence
of inhomogeneous best left approximations of β. Let v be the uniquely deﬁned integer that satisﬁes kv ≤
⌊log2 x⌋ < kv+1. Then

kvα − lv = max
(r,s)∈N2 {rα − s : 0 ≤ rα − s ≤ β, 0 ≤ r ≤ ⌊log2 x⌋, 0 ≤ s ≤ ⌊log3⌋} .

162 Val´erie Berth´e and Laurent Imbert

Proof: From the proof of Proposition 4, we know that Algorithm 2 returns the inﬁnite sequence (ki, li)i≥0
of best left approximations to β = {log3 x}. In order to ﬁnd (k, l) as above, we only need to perform a
ﬁnite number of iterations. In fact, this number of iterations is given by the smallest integer v such that
⌊log2 x⌋ < kv, or equivalently, the smallest integer v such that ⌊log3 x⌋ < lv. We use this bound in our
complexity analysis (see proof of Proposition 6). ✷

Remark 1 As pointed out in the proof of Proposition 5, we only need to perform a ﬁnite number of
iterations of Algorithm 2. Remark that this number of iterations depends on the sequence of partial
quotients in the continued fraction expansion of α. For the same reason, we can also use a rational
approximation of α = log3 2, say pw/qw, given by the wth convergent. Note that the required precision
for the rational approximation of α depends on the binary length of the input x. This is why we state
our complexity result for integers x with bounded binary length. We analyse the required precision in
Remark 2.

Proposition 6 Let m > 0. For all x having at most m bits, the ﬁnite version of Algorithm 2 (see Remark 4,
above) terminates in O(log log x) iterations.

Proof: We use the notation of Algorithm 2. According to (8), we obtain

β = ∑

ni even cifni + ∑

ni odd(cifni + fni+1).

For x ≥ 2, let v(x) be the unique integer such that kv(x) ≤ ⌊log2 x⌋ < kv(x)+1. If ni is even, we
compute ki+1 = ki + qni and we have seen that this occurs ci − 1 times. If ni is odd, we compute
ki+1 = ki − ciqni + qni+1. We have

kv(x) = ∑

ni even ciqni + ∑

ni odd (−ciqni + qni+1) ,

and thus kv(x) = ∑

ni even ciqni + ∑

ni odd
 ((ani+1 − ci)qni + qni−1) .

Let w(x) = maxi{ni}. Since ani+1 − ci ≥ 0, for all ni ≥ 1, and ci ≥ 1, for all ni, we have

qw(x)−1 ≤ ∑

ni even qni + ∑

ni odd qni−1 ≤ kv(x) ≤ ⌊log2 x⌋ .

Moreover, we also know that the sequence (qi)i≥0 grows at least as fast as the sequence of Fibonacci
numbers given by the denominators of the continued fraction expansion of (1 + √5)/2 = [1, 1, 1, 1, . . . ]
(all the partial quotients are equal to 1). Therefore, from Binet’s formula (see [28]), we deduce that there
exists a constant C > 0 such that ∀x, w(x) < C log log x.

Consequently, there exists C ′ such that for all x having at most m bits, w(x) < C ′ log m. We now set A =
maxi=1... C ′ log m{ai}. For any m-bit integer x, the number of iterations s(x) satisﬁes s(x) ≤ Aw(x).
This concludes the proof. ✷

Ostrowski numeration and DBNS 163

Corollary 1 The greedy algorithm combined with Algorithm 2 is optimal.

Proof: Since the greedy algorithm produces decompositions with O(log x/ log log x) terms according
to [12], its overall asymptotic complexity is O(log x), i.e., it reaches the lower bound for a recoding
algorithm (all the bits/digits of x have to be scanned). ✷

Remark 2 Let us analyse the required precision for α in terms of the bitlength of x. From the proof of
Proposition 6, we have

kv = ∑

ni even ciqni + ∑

ni odd(ani+1 − ci)qni + qni−1 ≤ ⌊log2 x⌋

with ani+1 − ci ≥ 0 for all ni ≥ 1, and ci ≥ 1 for all ni. Therefore, if x is an m-bit integer, we only need
the denominators qi such that qi ≤ m for all i ≥ 1. Let w = max{i : qi ≤ m}. Table 1 gives some useful
numerical values for w.
Now, we need to know how many bits of precision µ are given by ˆα = pw
qw , the wth rational approxima-
tion of α. It is well known (see [17]) that for all n
∣α − pn

qn
 ∣ ≤ 1

qnqn+1 .

Therefore, if 1
qn+1qn > 2−µ, we obtain
 µ > log2 qn + log2 qn+1. (11)

From (11), we can e.g. deduce that

1.11022... × 10−16 ≈ 2
−53 < 1
q16q17 ≈ 6.87368... × 10−16,

which tells us that a double-precision binary ﬂoating-point approximation of α = log3 2 provides roughly
the same precision as the 16th convergent, and that it is ”good-enough” for numbers of size up to 17
millions bits!
 Size of x (in bits) w µ
3 to 7 4 6
8 to 18 5 9
19 to 64 6 12
65 to 83 7 14
84 to 484 8 18
484 to 1053 9 23

Tab. 1: Number w of partial quotients ai, and convergents pi/qi to be computed based on the size of input x. The
last column gives the number of bits of precision provided by pw/qw, the wth rational approximation of α.

164 Val´erie Berth´e and Laurent Imbert

Remark 3 We have seen that Algorithm 2 provides an expansion of β of the form

β = ∑

ni even cifni + ∑

ni odd(cifni + fni+1).

Let us stress the fact that sequences (ni)i≥0 and (ci)i≥0 cannot be directly derived from the sequences
of digits provided by Proposition 2 and 3 by performing ﬁnitely many operations. Note that these latter
sequences of digits can be generated in an effective way by maps deﬁned on the unit square as skew
products of the Gauss map, such as described in [15] and [16].

A numerical example

We want to ﬁnd the largest integer of the form 2
a3
b ≤ x = 23832098195. We have ⌊log3 x⌋ = 21,
β = {log3 x} ≈ 0.7495. The partial quotients and the convergents of the continued fraction expansion of
α = log3 2 ≃ 0.63093 are given in Table 2.

i ai pi qi fi = |qiα − pi|
0 0 0 1 0.63093
1 1 1 1 0.36907
2 1 1 2 0.26186
3 1 2 3 0.10721
4 2 5 8 0.04744
5 2 12 19 0.01234
6 3 41 65 0.01043

Tab. 2: Partial quotients and convergents of log3 2

Table 3 gives the ﬁrst inhomogeneous best left approximations to β.

i β − (kiα − li) ni ci ei ki+1 li+1 ki+1α − li+1
0 0.7495 1 1 0.1186 1 0 0.6309
1 0.1186 4 2 0.0114 9 5 0.6784
2 0.0712 4 1 0.0114 17 10 0.7258
3 0.0237 5 1 0.0009 63 39 0.7486

Tab. 3: Best left approximations of β ≃ 0.7495 with numbers of the form kα − l

The stop condition (see Remark 4) is reached for i = 3 because we get a negative ternary exponent
(21 − 39 = −18). We thus retain the third approximation (0.7258), which gives a = 17 and b =
21 − 10 = 11. In order to ﬁnd the DBNS representation of x, we then apply the same algorithm with the
value x − 2
173
11 = 613086611. For completeness, we give the DBNS representation of x provided by
the greedy decomposition: x = 2
173
11 + 2
73
14 + 273
8 + 2
23
8 + 293
0 + 223
1 + 203
1.

Ostrowski numeration and DBNS 165

5 Signed expansions

It is natural to consider signed expansions of the form

x = ∑ ±2
ai3
bi,

with ai, bi ≥ 0, (ai, bi) ̸= (aj, bj) if i ̸= j. The following proposition shows that it is not possible to
deﬁne a greedy algorithm based on a similar logarithm reduction approach, that is, by working with the
sequence of two-sided inhomogeneous best approximations of β. More precisely, Proposition 7 below
shows that it may give an erroneous solution inﬁnitely often; this happens only when the logarithm reduc-
tion approach returns a solution greater than log x whereas the best approximation of x is possibly less
than x.

Proposition 7 Let (Kn)n∈N be the increasing sequence of integers of the form 2
a3
b, with a, b ∈ N. For
any positive integer n, we deﬁne Nn as the number of positive integers x such that Kn ≤ x < Kn+1 with

1. x − Kn ≤ Kn+1 − x

2. log Kn+1 − log x < log x − log Kn.

The sequence (Nn)n∈N tends towards inﬁnity.

Proof: Condition (1) is equivalent to Kn ≤ x ≤ Kn+1 + Kn
2 , whereas condition (2) is equivalent to
log Kn + log Kn+1
2 < log x < log Kn+1, that is,

√KnKn+1 < x < Kn+1.

Hence Nn satiﬁes ∆n − 1 ≤ Nn ≤ ∆n + 1

with
 ∆n = Kn + Kn+1
2 − √KnKn+1.

For all n, we set δn = Kn+1
Kn . One has

∆n = ( δn + 1
2 − √δn
) Kn =
 (√δn − 1
)2

2 Kn = (δn − 1)
2

2 Kn 1
(√δn + 1)2 .

According to [26], there exist C, C ′ with C > 0, C ′ > 0 such that for all n

1
log KnC′ ≤ δn − 1 = Kn+1 − Kn
Kn ≤ 1
log KnC .

We thus deduce that limn→+∞ Nn = +∞. ✷

166 Val´erie Berth´e and Laurent Imbert

Nevertheless, we can apply the following strategy in the signed case. Let x ≥ 2 be a given positive
integer. We ﬁrst ﬁnd a, b ≥ 0 such that 2
a3
b ≤ x and among the solutions to this problem, 2a3
b is the
largest possible value: 2
a3
b = max {2
c3
d ≤ x : (c, d) ∈ N2} .

We similarly ﬁnd a
′, b
′ ≥ 0 such that 2
a
′3
b′ ≥ x and among the solutions to this problem, 2a
′3
b′ is the
smallest possible value:
 2
a
′3b′ = min {
2
c
′3
d
′ ≥ x : (c, d) ∈ N2} .

For this latter problem, we can either deal with an analogous algorithm providing the sequence of inho-
mogeneous best right approximations of β, or work with 1 −α and 1 −β, with the notation of the previous
sections. It then remains to compare x − 2a3
b and 2a
′3
b′ − x, and to take the smallest of both values.

6 An approximate greedy algorithm

The greedy algorithm is not optimal, in the sense that it does not necessarily produce a DBNS representa-
tion of minimal length. However, within this algorithm, we proved that ﬁnding the largest number of the2
a3
b less than equal to x is optimal in complexity. It seems then natural to investigate the potential
advantages of an approximate greedy algorithm, where we only perform a few iterations of Algorithm 2
to deﬁne a “good” integer of the form 2
a3b, although not the largest, less than or equal to x.
The greedy decomposition described in Algorithm 1 can easily be adapted to compute a DBNS expan-
sion of x, where only d iterations of Algorithm 2 are performed at each step to deﬁne the term z ≤ x. In
the following, we shall refer to d as the depth.
In order to visualize DBNS expansions, we use a two-dimensional array where the columns represent
the powers of 2 while the rows represent the powers of 3. A black square at position (i, j) indicates
that the term 2
i3
j is part of the DBNS decomposition. (The upper-left corner corresponds to the term
2
03
0 = 1.) Figure 2 shows the DBNS representations obtained for x = 23832098195 when the greedy
decomposition algorithm is applied at depth 1,2, and 3. (Note that depth 3 is equivalent to the complete
greedy decomposition.)
As expected, the length of the DBNS decomposition decreases as the depth increases; we get 12 terms
at depth 1; 8 terms at depth 2; and 7 terms at depth 3. We note also that the largest binary exponent (the
number of columns) is smaller for small depths. These results were to be expected. However, the follow-
ing questions seem difﬁcult to answer in the general case. By using a greedy decomposition algorithm at
a given depth d, how many summands are required to represent x compared to the solution provided by
the complete greedy approach? What decrease (resp. increase) can we expect on the largest binary (resp.
ternary) exponents? In order to answer those questions, we have implemented the algorithm at different
depths, for a thousand randomly chosen numbers of sizes ranging from 128 to 512 bits. The difference in
length between the full-greedy approach and the decomposition at ﬁxed depths is shown in Figures 3 to 5.
Our experiments are summarized in Table 4.
We ﬁrst note that, for all our tests (up to 512-bit integers), d = 5 is equivalent to the complete greedy
algorithm; which means that we perform 6 iterations of Algorithm 2 to get an approximation which
corresponds to a negative ternary exponent (the stop condition, cf. Remark 4). With the greedy algorithm
at ﬁxed depth d, it is possible that the stop condition occurs before we reach the desired depth, or would
occur at the (d + 1)th iteration. Only in those two cases, we get the optimal solution; i.e, the largest

Ostrowski numeration and DBNS 167

0 1 2

0
.

(a) depth 1
 0 1 2 3 4 . . .

0
.
 (b) depth 2
 0 1 2 3 4 . . .

0
.
 (c) depth 3

Fig. 2: DBNS decompositions of x = 23832098195 at depth 1,2,3

 0

 100

 200

 300

 400

 500

 600

 700

 800

 900

 1000
 -6 -4 -2  0  2  4  6  8  10  12  14frequency
distance to full-greedy

128-bit integers
 depth 2
depth 3
depth 4

Fig. 3: Distribution of the length difference of DBNS expansions obtained with the full-greedy and the approximate
algorithm at depths 2,3,4 for 128-bit numbers

168 Val´erie Berth´e and Laurent Imbert

 0

 50

 100

 150

 200

 250

 300

 350

 400

 450
 -5  0  5  10  15  20  25frequency
distance to full-greedy

256-bit integers
 depth 2
depth 3
depth 4

Fig. 4: Distribution of the length difference of DBNS expansions obtained with the full-greedy and the approximate
algorithm at depths 2,3,4 for 256-bit numbers

 0

 20

 40

 60

 80

 100

 120

 140

 160

 180

 200
 -5  0  5  10  15  20  25frequency
distance to full-greedy

512-bit integers
 depth 3
depth 4

Fig. 5: Distribution of the length difference of DBNS expansions obtained with the full-greedy and the approximate
algorithm at depths 3,4 for 512-bit numbers

Ostrowski numeration and DBNS 169

Size of x Approx # digits Avg. dist. to greedy at depth . . .
(in bits) with F-greedy d = 1 d = 2 d = 3 d = 4 d = 5
64 12 9.08 2.35 0.47 0 -
128 20 19.76 5.8 1.4 0.02 0
256 35 - 14.5 4.6 0.5 0
512 62 - - 12.14 2.2 0

Tab. 4: Average distance to the full-greedy solution at various depths. Note that depth 5 is equivalent to the full-
greedy algorithm in all our experiments
a3
b ≤ x. It is also interesting to note that at medium depth (d = 3 or 4), the length of the representations
can be very close to the full greedy ones, and in some cases even shorter.
For some applications, we might not need the DBNS decomposition given by the complete greedy
approach, but rather satisfy with an approximated one, with slightly more terms, especially if the time
required for the conversion is reduced. Another consequence of using the greedy decomposition at ﬁxed
depth is that the binary exponent is likely to be smaller at small depths than with the complete greedy
decomposition. It is clear that the ternary exponent increases at the same time, but clearly not as fast (the
ratio is α ≃ 0.63).

7 Discussions

The question of the generalization to more than two bases, such as 2
a3
b5
c is natural. Nevertheless, there
is no canonical generalization of Ostrowski numeration to higher dimensions. This is mainly due to the
fact that there is no canonical notion of multidimensional continued fractions. To remedy to the lack of
a satisfactory tool replacing continued fractions, several approaches are possible. One can consider e.g.
lattice reduction algorithms: let us quote the computation of the n-th Hamming number in [21] based on
results from [4]. Let us recall that Hamming numbers are numbers of the form 2a3
b5
c for a, b, c ∈ N,
and that they are called after Hamming who asked for an efﬁcient algorithm to generate in order the list
of these numbers. The problem was popularized by E. W. Dijkstra in [9].
Algorithm 2 relies on the so-called three-gap theorem (see [22] and also the survey [5]). In the same
vein, an algorithm is given in [18] which computes the points in Z
2 located at a distance smaller than
a given ε from a segment. This latter algorithm is based on the three-distance theorem, which can be
considered as a dual version of the three-gap theorem. As an application, an algorithm which produces
worst cases when trying to round the elementary functions in ﬂoating-point arithmetic is given in [19].
Instead of working with integer bases, one can also consider numeration in rational base (2/3). The
dynamical and arithmetical behaviour of such a numeration system differs drastically. Let us quote [1]
which considers connections to number theory and applications to the problem of the distribution of the
fractional part of the powers of rational numbers.

Acknowledgements

The authors would like to thank A. R´emondi`ere for many useful discussions concerning Proposition 7 and
the anonymous reviewers for their very careful reading.

170 Val´erie Berth´e and Laurent Imbert

References

[1] S. Akiyama, C. Frougny, and J. Sakarovitch. Powers of rationals modulo 1 and rational base number
systems. Isra¨el Journal of Mathematics, 168(1):53–91, 2008.

[2] J.-P. Allouche and J. Shallit. Automatic Sequences. Cambridge University Press, 2003.

[3] G. E. Andrews. Congruence properties of the m-ary partition function. Journal of Number Theory,
3(1):104–110, 1971.

[4] A. Barvinok and J. E. Pommersheim. An algorithmic theory of lattice points in polyhedra. In New
perspectives in algebraic combinatorics, volume 38 of MSRI Publications, pages 91–147. Cam-
bridge Univ. Press, 1999. Available at http://www.msri.org/publications/books/
Book38/contents.html.

[5] V. Berth´e. Autour du syst`eme de num´eration d’Ostrowski. Bulletin of the Belgian Mathematical
Society, 8:209–239, 2001.

[6] V. Berth´e, N. Chekhova, and S. Ferenczi. Covering numbers: Arithmetics and dynamics for rotations
and internal exchanges. Journal d’Analyse Math´ematique, 79:1–31, 1999.

[7] V. Berth´e and L. Imbert. On converting numbers to the double-base number system. In Advanced
Signal Processing Algorithms, Architecture and Implementations XIV, volume 5559 of Proceedings
of SPIE, pages 70–78. SPIE, 2004.

[8] J. W. S. Cassels. An Introduction to Diophantine Approximation. Cambridge University Press, 1957.

[9] E. W. Dijkstra. Hamming’s exercise in SASL. Originally a privately-circulated handwitten
note; available at http://www.cs.utexas.edu/users/EWD/ewd07xx/EWD792.PDF,
June 1981.

[10] V. Dimitrov, L. Imbert, and P. K. Mishra. Efﬁcient and secure elliptic curve point multiplication
using double-base chains. In Advances in Cryptology, ASIACRYPT’05, volume 3788 of Lecture
Notes in Computer Science, pages 59–78. Springer, 2005.

[11] V. Dimitrov, L. Imbert, and P. K. Mishra. The double-base number system and its application to
elliptic curve cryptography. Mathematics of Computation, 77(262):1075–1104, 2008.

[12] V. Dimitrov, G. A. Jullien, and W. C. Miller. An algorithm for modular exponentiation. Information
Processing Letters, 66(3):155–159, May 1998.

[13] V. Dimitrov, G. A. Jullien, and W. C. Miller. Theory and applications of the double-base number
system. IEEE Transactions on Computers, 48(10):1098–1106, Oct. 1999.

[14] C. Doche and L. Imbert. Extended double-base number system with applications to elliptic curve
cryptography. In Progress in Cryptology, INDOCRYPT’06, volume 4329 of Lecture Notes in Com-
puter Science, pages 335–348. Springer, 2006.

[15] S. Ito. Some skew product transformations associated with continued fractions and their invariant
measures. Tokyo Journal of Mathematics, 9:115–133, 1986.

Ostrowski numeration and DBNS 171

[16] S. Ito and H. Nakada. Approximations of real numbers by the sequence {nα} and their metrical
theory. Acta Mathematica Hungarica, 52(1-2):91–100, Mar. 1988.

[17] A. Y. Khinchin. Continued Fractions. Dover Publications, new edition, 1997.

[18] V. Lef`evre. An algorithm that computes a lower bound on the distance between a segment and
Z
2. Research report RR1997-18, Laboratoire de l´Informatique du Parall´elisme, Lyon, France, June
1997. Available at http://www.vinc17.org/research/publi.en.html.

[19] V. Lef`evre. New results on the distance between a segment and Z
2. application to exact rounding. In
Proceedings of the 17th IEEE Symposium on Computer Arithmetic, pages 68–75. IEEE Computer
Society Press, June 2005.

[20] V. A. Ostrowski. Bemerkungen zur theorie der diophantischen approximationen. Abh. Math. Semin.
Hamburg Univ, 1:77–98, 1922.

[21] M. Quercia. Calcul du n-´eme entier de Hamming, 1999. Available at http://pauillac.
inria.fr/˜quercia/.

[22] N. B. Slater. Gaps and steps for the sequence nθ mod 1. Mathematical Proceedings of the Cam-
bridge Philosophical Society, 63:1115–1123, 1967.

[23] V. T. S´os. On the theory of diophantine approximations. I. Acta Mathematica Hungarica, 8:461–472,
1957.

[24] V. T. S´os. On the theory of diophantine approximations. II. Acta Mathematica Hungarica, 9:229–
241, 1958.

[25] V. T. S´os. On a problem of Hartman about normal forms. Colloquium Mathematicum, 7:155–160,
1960.

[26] R. Tijdeman. On the maximal distance between integers composed of small primes. Compositio
Mathematica, 28:159–162, 1974.

[27] R. Tijdeman. Some applications of Diophantine approximation. In Surveys in Number Theory: Pa-
pers from the millennial conference on number theory (University of Illinois at Urbana-Champaign,, pages 261–284. A K Peters, 2003.

[28] N. N. Vorobiev. Fibonacci Numbers. Birkh¨auser, 2002.

[29] E. Zeckendorf. Repr´esentation des nombres naturels par une somme de nombres de Fibonacci ou de
nombres de Lucas. Fibonacci Quarterly, 10:179–182, 1972.

172 Val´erie Berth´e and Laurent Imbert
