<!-- source: https://matwbn.icm.edu.pl/ksiazki/aa/aa92/aa9229.pdf | converted from PDF -->

ACTA ARITHMETICA
XCII.2 (2000)
 Collatz cycles with few descents

by

T. Brox (Stuttgart)

1. Introduction. Let T : Z → Z be the function deﬁned by T (x) = x/2
if x is even, T (x) = (3x + 1)/2 if x is odd. T is known as the 3x + 1 function
(see [4], [7]). We are interested in the cycles of T , referred to as 3x + 1 cycles
(see [3]–[5]). The well known Finite Cycle Conjecture asserts that T has only
ﬁnitely many cycles. In this note we generalize a theorem due to R. Steiner
(see [4], [6]).
In order to state the result in a concise form, we consider instead of T a
slightly diﬀerent function T1 deﬁned by the unique decomposition

(1.1) 2k(x)T1(x) = 3x + 1 (x odd),

where k(x) ≥ 1 is the multiplicity of the prime factor 2 in the number 3x+1.
Note that T1 is only deﬁned for odd integers. For each odd argument the
iteration T k(x)(x) is equal to T1(x). An odd integer x is called descending if
k(x) ≥ 2.
In what follows, a cycle of T1 is called a Collatz cycle. By deﬁnition,
we can represent a Collatz cycle by a tuple Γ = (x1, . . . , xn) consisting of
distinct odd integers (n ≥ 1). By |Γ | we denote the number of elements in
Γ , i.e. the period of the Collatz cycle. Each Collatz cycle consists of the odd
elements in a 3x + 1 cycle, and conversely. If k denotes the sum of k(x) over
all elements of a Collatz cycle, then k is the period of the corresponding
3x + 1 cycle. Let δ(Γ ) be the number of descending elements in a Collatz
cycle Γ .

Theorem 1.1. The number of Collatz cycles satisfying δ(Γ ) < 2 log |Γ |
is ﬁnite.

We will prove Theorem 1.1 in the following sections. In Section 4 we
brieﬂy discuss the extension of Theorem 1.1 to 3x + d mapping (see [2]).
The theorem of R. Steiner states that the ﬁxed point 1 is the only positive

2000 Mathematics Subject Classiﬁcation: 11D61, 11Z05.

[181]

182 T. Brox

Collatz cycle with δ(Γ ) = 1. It is easy to deduce the following corollary of
Theorem 1.1, using Lemma 2.2 in Section 2.

Corollary 1.2. For each ﬁxed ν ≥ 1 the number of Collatz cycles with
δ(Γ ) ≤ ν is ﬁnite.

2. A divisibility problem. In this section we express the existence
problem of a Collatz cycle by an appropriate periodic sequence (see Sections
2, 5 of [3]). Given an odd integer x0, consider the iteration xm = T1(xm−1).
Let km = k(xm−1). Because of (1.1), we get

(2.1) 2kmxm = 3xm−1 + 1 (m ≥ 1),

where it is required that x1, x2, . . . are odd. Proceeding iteratively, we im-
mediately obtain

(2.2) 2
k1+...+kmxm = 3mx0 + ϕm−1(k1, . . . , km−1).

Here ϕ0 = 1 and

(2.3) ϕm(u1, . . . , um) =
 m∑

l=0 3m−l2u1+...+ul ((u1, . . . , um) ∈ R
m),

where u1 + . . . + ul is zero if l = 0. For further references see Section 2 of [3].
Assume now (x0, . . . , xn−1) is a Collatz cycle. By construction, ki ≥ 1
for 1 ≤ i ≤ n. Since xn = x0, (2.2) implies

M x0 = ϕn−1(k1, . . . , kn−1),

where

(2.4) M = 2k − 3n, k = k1 + . . . + kn.

Consider (x0, . . . , xn−1) and (k1, . . . , kn) as n-periodic sequences {xi}i∈Z,
{ki}i∈Z. Since we can take each xi as start value, we obtain

(2.5) M xi = ϕn−1(ki+1, . . . , ki+n−1) (i ∈ Z).

Hence M divides the right hand side of (2.5) for each i. Since the Collatz
cycle consists of distinct elements, n is the smallest period of {ki}, by (2.5).
Conversely, let {ki}i∈Z be any periodic sequence of positive integers. Let
n be the smallest period of {ki}. Deﬁne M and k by (2.4). Let

Fi = ϕn−1(ki+1, . . . , ki+n−1) (i ∈ Z).

Note that Fi does not depend on ki. Plainly {Fi} is n-periodic. Because of
(2.3) and periodicity, we get by a simple computation

(2.6) 2kiFi = 3Fi−1 + M (i ∈ Z).

Collatz cycles with few descents 183

Since each ki is positive, we conclude from (2.3) and (2.4) that

gcd(2 · 3, Fi) = 1 (i ∈ Z),(2.7) gcd(2 · 3, M ) = 1.(2.8)

Because of (2.6) and (2.7), ki and Fi are uniquely determined by Fi−1. If
Fl = Fm, then |m − l| is a period of {ki}. Hence F1, . . . , Fn are distinct. We
are now ready to prove the following lemmas (see also Section 5 of [3]).

Lemma 2.1. Let M = 2k − 3n. Then either M ∤ Fi (1 ≤ i ≤ n) or
M | Fi (1 ≤ i ≤ n). The latter case corresponds to a Collatz cycle (x1, . . . , xn),
where xi = Fi/M .

P r o o f. Assume that M | Fi for one i. Then (2.6)–(2.8) imply that for
all i, M | Fi and xi = Fi/M is odd. Dividing (2.6) by M , we arrive at
xi = T1(xi−1), since each xi is odd. Plainly x1, . . . , xn are distinct.

Lemma 2.2. If {ki} generates a Collatz cycle, then k = k1+. . .+kn ≤ 2n.
In particular , for each n ≥ 1, the number of Collatz cycles with |Γ | = n is
ﬁnite.

P r o o f. If {ki} generates a Collatz cycle, then xi = Fi/M , by Lemma
2.1. If we multiply (2.6) from i = 1 to i = n, a simple reduction yields

2k =
 n∏

i=1
(3 + 1/xi−1) ≤ 4n,

since |1/xi| ≤ 1. Hence k ≤ 2n.

Remark 2.3. By Lemma 2.1, since ki = 1 (i ∈ Z) has period 1, there
exists at most one Collatz cycle with δ(Γ ) = 0, and this Collatz cycle has
to be a ﬁxed point. In fact, −1 = 1/(2 − 3) is a non-descending ﬁxed point.

3. Algebraic reformulation. In order to prove Theorem 1.1, we re-
formulate the divisibility problem in a more convenient form. As before let
{ki}i∈Z be a periodic sequence of positive integers. Let n be the smallest
period of {ki}. Deﬁne

̃ϕn(u1, . . . , un) = 2u1ϕn−1(u2, . . . , un) − 2ϕn−1(u1, . . . , un−1)
((u1, . . . , un) ∈ R
n).

Because of (2.3), we obtain

(3.1) ̃ϕn(u1, . . . , un) = 2
 n−1∑

l=0 3n−(l+1)2u1+...+ul {2ul+1−1 − 1}.

For each i ∈ Z deﬁne ̃Fi = ̃ϕn(ki+1, . . . , ki+n).

184 T. Brox

Then (2.6) implies

(3.2) ̃Fi = 2ki+1 Fi+1 − 2Fi = Fi + M (i ∈ Z).

Let ν be the number of indices i such that 1 ≤ i ≤ n and ki ≥ 2.
We assume ν ≥ 1. Deﬁne strictly ascending numbers τ (1), . . . , τ (ν) by 1 ≤
τ (j) ≤ n and kτ (j) ≥ 2. Put τ (0) = τ (ν) − n. For 1 ≤ j ≤ ν let

hj = kτ (j) − 1, nj = τ (j) − τ (j − 1).

Consider (h1, . . . , hν), (n1, . . . , nν) as ν-periodic sequences {hi}i∈Z, {ni}i∈Z.
By construction, the two sequences consist of positive integers, and ν is the
smallest common period. Also by construction,

(3.3) n = n1 + . . . + nν, k = h + n,

where

(3.4) h = h1 + . . . + hν.

Given (t0, . . . , tν−1) ∈ R
ν and (u1, . . . , uν−1) ∈ R
ν−1, put

(3.5) ψ2ν−1(t0, u1, t1, u2, . . . , tν−1)

=
 ν−1∑

l=0 2t0+u1+...+tl−1+ul {2tl − 1}3ul+1+...+uν−1 ,

where the sum in the 2-exponent (3-exponent) is zero if l = 0 (l = ν − 1).
For each j ∈ Z deﬁne

(3.6) Hj = ψ2ν−1(hj, nj+1, hj+1, nj+2, . . . , hj+ν−1).

Thus Hj does not depend on nj. Note that Hj > 0 for each j ∈ Z. Note also
that {Hj} is ν-periodic. We assert

(3.7) ̃Fτ (j) = 2nj+1 Hj+1 (j ∈ Z).

By shift, it is enough to verify (3.7) for j = 0. Also by shift, we can assume
that τ (0) = 0. Then τ (j) equals n1 + . . . + nj (1 ≤ j ≤ ν). In (3.1) only
those terms can survive which are placed at l + 1 = τ (j). Hence

̃Fτ (0) = 2
 ν∑

j=1 3n−τ (j)2h1+...+hj−1+τ (j)−1{2hj − 1}.

In the last formula we take the 2-exponent n1 − 1 outside the sum. After
some rearrangement, the remaining sum is easily identiﬁed as H1.
Conversely, let {hj}j∈Z, {nj}j∈Z be any periodic sequences consisting of
positive integers. Let ν be the smallest common period of both sequences.
Deﬁne h, k, n by (3.3) and (3.4). Let Hj be given by (3.6). Up to shift, {ki}
is uniquely determined by both sequences, i.e. by {h0, n1, h1, n2, . . .}. Also
n is the smallest period of {ki}. Because of (2.8), (3.2) and (3.7), we can
reformulate Lemma 2.1.
 Collatz cycles with few descents 185

Lemma 3.1. Let M = 2k − 3n. Then either M ∤ Hj (1 ≤ j ≤ ν) or
M | Hj (1 ≤ j ≤ ν). The latter case corresponds to a Collatz cycle with
|Γ | = n and δ(Γ ) = ν.

4. Minimum of the H-sequence. In this section we prove Theorem
1.1 assuming the truth of Lemma 5.1, which will be stated and proved in
Section 5. Consider a pair {hj}j∈Z, {nj}j∈Z of periodic sequences consisting
of positive integers. Deﬁne ν, h, k, n as described in the preceding section.
By Lemma 3.1, since each Hj > 0, the two sequences cannot generate a
Collatz cycle if

(4.1) min
0≤j≤ν−1 Hj < |M | = |2k − 3n|.

To prove Theorem 1.1, it is enough, by Lemma 2.2 and Remark 2.3, to show
(4.1) holds for all suﬃciently large n, assuming that ν < 2 log n.
First we consider the left hand side of (4.1). Let θ = log2 3 and θ1 = θ−1.
Note that θ1 > 0. In order to estimate Hj, we replace the bracket inside (3.5)
by 2hj+l . Because of periodicity, an easy rearrangement yields

3−nHj <
 ν−1∑

l=0 2−nj +Sj,l (j ∈ Z),

where
 Sj,l =
 l∑

i=0(hj+i − θ1nj+i) (l ≥ 0).

As a functional of both sequences deﬁne

E = min
0≤j≤ν−1{−nj + max
0≤l≤ν−1 Sj,l}.

By an elementary estimation,

min
j 3−nHj < ν2E.

We claim that

(4.2) E ≤ max(0, ∆) − Aνn,

where Aν = θ1/(θν − 1), ∆ = h − θ1n = k − θn.
But (4.2) is a consequence of Lemma 5.1 below, applied with xj = θ1nj,
yj = hj, α = 1/θ1. Hence we obtain

min
j 3−nHj < ν2max(0,∆)−Aν n.

Let γ = 1 − 2 log θ = 0.0788 . . . If we assume that ν < 2 log n, then

(θν − 1)
−1n > θ−νn = n1−ν log θ/ log n > nγ,

186 T. Brox

and it follows that

(4.3) min
j 3−nHj < log n · 21+max(0,∆)−θ1n
γ .

We now consider the right hand side of (4.1). By elementary analysis we
get 3−n|M | = |2∆ − 1| ≥ min(|∆|, 1)2max(0,∆)−1.
Note that we have n ≥ 1 and k = h + n ≥ 2. By deﬁnition, |∆| < 1 if
k > θn − 1 and k < θn + 1, otherwise |∆| ≥ 1. A result of A. Baker and
N. Feldman (see Theorem 3.1 in [1]) implies the existence of an eﬀectively
computable constant C0 > 0 such that

|∆| > |k log 2 − n log 3| > {max(k, n)}−C0 (k ≥ 2, n ≥ 1).

Since θn + 1 > n, |∆| > {θn + 1}−C0,
and therefore

(4.4) 3−n|M | > {θn + 1}−C0 2max(0,∆)−1.

If n is large enough, the right side of (4.3) is smaller than the right side of
(4.4), which gives (4.1).

Remark 4.1. We brieﬂy sketch the extension of Theorem 1.1 to the 3x+d
mapping, where d is a positive integer prime to 2 and 3. Deﬁne T1 according
to (1.1), where the right hand side is replaced by 3x + d. Now k(x) is the
multiplicity of 2 in the number 3x+d. Deﬁne a Collatz cycle, descending and
δ(Γ ) as in Section 1. After an obvious modiﬁcation of (2.1), in (2.2) replace
ϕm−1 by dϕm−1. Note that the deﬁnition of ϕm is not aﬀected (m ≥ 0).
Hence multiply the right hand side of (2.5) with d. If (2.6) is multiplied with
d, it follows that Fi can be replaced by dFi in Lemma 2.1. Similarly to the
proof of Lemma 2.2, if {ki} generates a Collatz cycle, then

2k =
 n∏

i=1(3 + d/xi−1) ≤ (3 + d)
n.

Hence put k ≤ C1n in Lemma 2.2, where C1 = log2(3+d). In Lemma 3.1 put
dHj instead of Hj. Finally multiply the left hand side of (4.1) with d. The
additional factor d causes no harm for the conclusion that the inequality is
true if n is large enough and ν < 2 log n.

5. Upper value of E. Let there be given an integer ν ≥ 1 and real
numbers r > 0, s > 0. Let {xj}j∈Z, {yj}j∈Z be ν-periodic sequences of
non-negative real numbers such that

x1 + . . . + xν = r, y1 + . . . + yν = s.

Collatz cycles with few descents 187

For each j ∈ Z and l ≥ 0 deﬁne

Sj,l =
 l∑

i=0(yj+i − xj+i).

Lemma 5.1. For any real α > 0,

min
0≤j≤ν−1{−αxj + max
0≤l≤ν−1 Sj,l} ≤ max(0, s − r) − r/(βν − 1),

where β = 1 + 1/α.

P r o o f. (a) Reduction to the case r = s. If r ̸= s, put ̃yj = ryj/s. Then
̃s = r and

Sj,l =
 l∑

i=0(yj+i − ̃yj+i) +
 l∑

i=0(̃yj+i − xj+i) = s − r
s
 l∑

i=0 yj+i + ̃Sj,l.

Hence max
0≤l≤ν−1 Sj,l ≤ max(0, s − r) + max
0≤l≤ν−1 ̃Sj,l.

Thus we have to prove the assertion for the case r = s.
(b) Elimination of {yj}. We suppose r = s. Then {S0,l}l≥0 is ν-periodic.
By a simple shift, we can assume

S0,ν−1 = max
l≥0 S0,l = 0.

If 1 ≤ j ≤ ν − 1, then

max
0≤l≤ν−1 Sj,l =
 ν−1∑

i=j (yi − xi) =
 j−1∑

i=0(xi − yi) ≤
 j−1∑

i=0 xi.

Note that the last inequality is sharp if yj = 0 (0 ≤ j ≤ ν − 2) and yν−1 = r.
Now we have to estimate the minimum of

(5.1) −αx0, −αx1 + x0, −αx2 + x0 + x1, . . . , −αxν−1 + x0 + . . . + xν−2.

(c) Linear optimization. Consider x = (x0, . . . , xν−1) as a vector in R
ν.
Deﬁne linear functionals L0, . . . , Lν−1 according to (5.1). Let f (x) be the
minimum of L0x, . . . , Lν−1x. Let B be the aﬃne subspace x0+. . .+xν−1 = r.
We assert

(5.2) sup
x∈B f (x) = −r/(βν − 1).

In order to prove (5.2), consider the vector

b = r(β − 1)(βν − 1)
−1(β0, β1, . . . , βν−1).

Plainly b ∈ B. An easy computation shows

(5.3) L0b = L1b = . . . = Lν−1b.

188 T. Brox

Next, f (b) equals the right hand side of (5.2). Let U be the linear subspace
where the sum of coordinates equals zero. If x ∈ B, then x = b + u (u ∈ U ).
By (5.3),
 f (x) = f (b) + min
j Lju = f (b) + f (u) (x ∈ B).

We have to show f (u) ≤ 0. Assume the contrary, that is, each number
L0u, . . . , Lν−1u is positive. Since L0u > 0, we get u0 < 0. Since u0 < 0 and
L1u > 0, we get u1 < 0. Repeating the argument, each uj is negative, which
contradicts u ∈ U .

Acknowledgements. We thank the referee for useful hints and im-
provements.
 References

[1] A. B a k e r, Transcendental Number Theory, Cambridge Univ. Press, 1975.
[2] E. G. B e l a g a and M. M i g n o t t e, Embedding the 3x + 1 conjecture in a 3x + d
context, Experiment. Math. 7 (1998), 145–152.
[3] L. H a l b e i s e n and N. H u n g e r b ¨u h l e r, Optimal bounds for the length of rational
Collatz cycles, Acta Arith. 78 (1997), 227–239.
[4] J. C. L a g a r i a s, The 3x + 1 problem and its generalizations, Amer. Math. Monthly
92 (1985), 3–23.
[5] —, The set of rational cycles for the 3x + 1 problem, Acta Arith. 56 (1990), 33–53.
[6] R. P. S t e i n e r, A theorem on the Syracuse Problem, in: Proc. 7th Manitoba Conf.
on Numerical Mathematics, 1977, Winnipeg, 1978, 553–559.
[7] G. J. W i r s c h i n g, The Dynamical System Generated by the 3n+1 Function, Lecture
Notes in Math. 1681, Springer, Berlin, 1998.

Helblingstr. 21
D-70565 Stuttgart, Germany
E-mail: thomas.brox@daimlerchrysler.com

Received on 12.2.1999
and in revised form on 15.9.1999 (3554)
