<!-- source: https://arxiv.org/pdf/1407.7000 | converted from PDF -->

arXiv:1407.7000v2  [math.LO]  8 Oct 2015
OSTROWSKI NUMERATION SYSTEMS, ADDITION AND FINITE
AUTOMATA

PHILIPP HIERONYMI AND ALONZA TERRY JR.

ABSTRACT. We present an elementary three pass algorithm for computing addition in
Ostrowski numerations systems. When a is quadratic, addition in the Ostrowski numera-
tion system based on a is recognizable by a ﬁnite automaton. We deduce that a subset of
X ⊆ Nn is deﬁnable in (N,+,Va), where Va is the function that maps a natural number x to
the smallest denominator of a convergent of a that appears in the Ostrowski representation
based on a of x with a non-zero coefﬁcient, if and only if the set of Ostrowski representa-
tions of elements of X is recognizable by a ﬁnite automaton. The decidability of the theory
of (N,+,Va) follows.
 1. INTRODUCTION

A continued fraction expansion [a0; a1, . . . , ak, . . . ] is an expression of the form

a0 + 1
a1 + 1
a2+ 1
a3+ 1
...

For a real number a, we say [a0; a1, . . . , ak, . . . ] is the continued fraction expansion of a if
a = [a0; a1, . . . , ak, · · · ] and a0 ∈ Z, ai ∈ N>0 for i > 0. Let a be a real number with continued
fraction expansion [a0; a1, . . . , ak, . . . ]. In this note we study a numeration system due to
Ostrowski [13] based on the continued fraction expansion of a. Set q−1 := 0 and q0 := 1,
and for k ≥ 0,

(1.1) qk+1 := ak+1 · qk + qk−1.

Then every natural number N can be written uniquely as

N = n
∑
k=0 bk+1qk,

where bk ∈ N such that b1 < a1, bk ≤ ak and, if bk = ak, bk−1 = 0. We say the word bn . . . b1
is the Ostrowski representation of N based on a, and we write ρa(N) for this word. For
more details on Ostrowski representations, see for example Allouche and Shallit [2, p.106]
or Rockett and Sz¨usz [14, Chapter II.4]. When a is the golden ratio φ := 1+√
5
2 , the con-
tinued fraction expansion of a is [1; 1, . . . ]. In this special case the sequence (qk)k∈N is the
sequence of Fibonacci numbers. Thus the Ostrowski representation based on the golden
ratio is precisely the better known Zeckendorf representation [17].

Date: October 15, 2018.
The ﬁrst author was partially supported by NSF grant DMS-1300402 and by UIUC Campus Research Board
award 13086. A version of this paper will appear in the Notre Dame Journal of Formal Logic.

1

2 P. HIERONYMI AND A. TERRY

In this paper, we will study the following question: given the continued fraction ex-
pansion of a and the Ostrowski representation of two natural numbers based on a, is there
an easy way to compute the Ostrowski representation of their sum? Ahlbach, Usatine,
Frougny and Pippenger [1] give an elegant algorithm to calculate the sum of two natural
numbers in Zeckendorf representations. In this paper we generalize their work and present
an elementary three pass algorithm for computing the sum of two natural numbers given
in Ostrowski representation. To be precise, we show that given the continued fraction ex-
pansion of a, addition of two n-digit numbers in Ostrowski representation based on a can
be computed by three linear passes over the input sequence and hence in time O(n). If a is
a quadratic number1, we establish that the graph of addition in the Ostrowski numeration
system based on a can be recognized by a ﬁnite automaton (see Theorem B for a precise
statement). When a is the golden ratio, this result is due to Frougny [8]2.

Ostrowski representations arose in number theory and have strong connections to the
combinatorics of words (see for example Berth´e [3]). However, our main motivation
for studying Ostrowski representations is their application to decidability and deﬁnabil-
ity questions in mathematical logic. The results in this paper (in particular Theorem B
below) play a crucial role in the work of the ﬁrst author [9] on expansions of the real ad-
ditive group. Here we will present the following application of our work on addition in
the Ostrowski numeration system to the study of expansions of Presburger Arithmetic (see
Theorem A).

Let a be quadratic. Since the continued fraction expansion of a is periodic, there is a
natural number c := maxk∈N ak. Let Σa = {0, . . . , c}. So ρa(N) is a Σa-word. Let Va : N → N
be the function that maps x ≥ 1 with Ostrowski representation bn . . . b1 to the least qk with
bk+1 ̸= 0, and 0 to 1.

Theorem A. Let a be quadratic. A set X ⊆ Nn is deﬁnable in (N, +,Va) if and only if X is
a-recognizable. Hence the theory of (N, +,Va) is decidable.

We say a set X ⊆ N is a-recognizable if 0∗ρa(X) is recognizable by a ﬁnite automaton,
where 0∗ρa(X) is the set of all Σa-words of the form 0 . . . 0ρa(N) for some N ∈ X. The
deﬁnition of a-recognizability for subsets of Nn is slightly more technical and we post-
pone it to Section 3. The decidability of the theory of (N, +,Va) follows immediately from
the ﬁrst part of the statement of Theorem A and Kleene's theor em (see Khoussainov and
Nerode [11, Theorem 2.7.2]) that the emptiness problem for ﬁnite automata is decidable.
Bruy`ere and Hansel [4, Theorem 16] establish Theorem A when a is the golden ratio. In
fact, they show that Theorem A holds for linear numeration systems whose characteristic
polynomial is the minimal polynomial of a Pisot number. A similar result for numeration
systems based on (pn)n∈N, where p > 1 is an integer, is due to B¨uchi [6] (for a full proof
see Bruy`ere, Hansel, Michaux and and Villemaire [5]). It is known by Shallit [15] and
Loraud [12, Theorem 7] that the set N is a-recognizable if and only if a is quadratic. So in
general the conclusion of Theorem A fails when a is not quadratic.

1A real number a is quadratic if it is a solution to a quadratic equation with rational coefﬁcients
2In private communication Frougny proved that whenever the continued fraction expansion of a has period
1, the stronger statement that addition in the Ostrowski numeration system associated with a can be obtained by
three linear passes, one left-to-right, one right-to-left and one left-to-right, where each of the passes deﬁnes a
ﬁnite sequential transducer.
 3

A few remarks about the proof of Theorem A are in order. The proof that every deﬁnable
set is a-recognizable, is rather straightforward, and we follow a similar argument from
Villemaire [16]. For the other direction, by Hodgson [10] it is enough to prove that N,
the graph of Va and the graph of + are a-recognizable. While it is easy to check the a-
recognizability of the graph of Va, we have to use our algorithm for addition in Ostrowski
numeration systems to show that the graph of + is a-recognizable. Thus most of the work
towards proving Theorem A goes into showing the following result.

Theorem B. Let a is a quadratic. Then {(x, y, z) ∈ N3 : x + y = z} is a-recognizable.

We end this introduction with a brief comment about possible applications of Theorem
B to the theory of Sturmian words
3. Let a be a real number in [0, 1]. We deﬁne

fa(n) := ⌊(n + 1)a⌋ − ⌊na⌋,

and we denote the inﬁnite {0, 1}-word fa(1) fa(2) . . . by f a. This word is called the Stur-
mian characteristic word with slope a. If a is a quadratic irrational, the set {n ∈ N :
fa(n) = 1} is a-recognizable (see [2, Theorem 9.1.15]). Du, Mousavi, Schaeffer and Shal-
lit [7] use this connection and Theorem B in the case of the golden ratio φ to prove results
about the Fibonacci word (that is the Sturmian characteristic word with slope φ − 1). Be-
cause of Theorem B the techniques in [7] can be applied to any characteristic Sturmian
word whose slope is a quadratic irrational.

Notation. We denote the set of natural numbers by {0, 1, 2, . . .} by N. Deﬁnable will
always mean deﬁnable without parameters. If Σ is a ﬁnite set, we denote the set of Σ-
words by Σ∗. If a ∈ Σ and X ⊆ Σ∗, we denote the set {a . . . aw : w ∈ X} of Σ-words by
a∗X. If x ∈ X m for some set X, we write xi for the i-th coordinate of x.

2. OSTROWSKI ADDITION

Fix a real number a with continued fraction expansion [a0; a1, . . . , ak, . . . ]. In this sec-
tion we present an algorithm to compute the Ostrowski representations based on a of the
sum of two natural numbers given in Ostrowski representation based on a. Since we will
only consider Ostrowski representation based on a, we will omit the reference to a. In the
special case that a is the golden ratio, our algorithm is exactly the one presented in [1].
Although it is not strictly necessary, the reader might ﬁnd it useful to read [1, Section 2]
ﬁrst.

Let M, N ∈ N and let xn . . . x1, yn . . . y1 be the Ostrowski representations of M and N. We
will describe an algorithm that given the continued fraction expansion of a calculates the
Ostrowski representation of M + N. Let s be the word sn+1sn . . . s1 given by

si := xi + yi,

for i = 1, . . . , n and sn+1 := 0. For ease of notation, we set m := n + 1.

The algorithm consists of three linear passes over s: one left-to-right, one right-to-left
and one left-to-right. These three passes will change the word s into a word that is the
Ostrowski representation of M + N. The ﬁrst pass converts s into a word whose digit at
position k is smaller or equal to ak. The idea how to achieve this, is as follows. We will
argue (see Lemma 2.4) that whenever the digit at position k is larger or equal to ak, then

3When preparing this paper, the authors were completely unaware of the connection between Sturmian words
and Ostrowski representations. We would like to thank the anonymous referee to point out this connection.

4 P. HIERONYMI AND A. TERRY

the preceding digit has to be less than ak+1. Using (2.1) we can then decrease the digit
at position k by ak, without increasing the one at position k + 1 above ak+1, and without
changing the value the word represents. The resulting word might not yet be an Ostrowski
representation of M + N, because the digit at position k may be ak and not followed by 0.
With the second and third pass we eliminate all such occurrences.

The ﬁrst step is an algorithm that makes a left-to-right pass over the sequence sm . . . s1
starting at m. That means that it starts with the most signiﬁcant digit, in this case sm, and
works its way down to the least signiﬁcant digit s1. The algorithm can best be described
in terms of a moving window of width four. At each step, we only consider the entries in
this window. After any possible changes are performed, the window moves one position
to the right. When the window reaches the last four digits, the changes are carried out as
usual. Afterwards, one ﬁnal operation is performed on the last three digits. The precise
algorithm is as follows. Given s = sm . . . s1, we will recursively deﬁne for every k ∈ N with
3 ≤ k ≤ m + 1, a word zk := zk,mzk,m−1 . . . zk,2zk,1.

Algorithm 1. Let k = m + 1. Then set

zm+1 := sm . . . s1.

Let k ∈ N with 4 ≤ k < m + 1. We now deﬁne zk = zk,mzk,m−1 . . . zk,2zk1:
• for i /∈ {k, k − 1, k − 2, k − 3}, we set zk,i = zk+1,i,
• the subword zk,kzk,k−1zk,k−2zk,k−3 is determined as follows:

(A1) if zk+1,k < ak, zk+1,k−1 > ak−1 and zk+1,k−2 = 0,

zk,kzk,k−1zk,k−2zk,k−3 = (zk+1,k + 1)(zk+1,k−1 − (ak−1 + 1))(ak−2 − 1)(zk+1,k−3 + 1)

(A2) if zk+1,k < ak, ak−1 ≤ zk+1,k−1 ≤ 2ak−1 and zk+1,k−2 > 0,

zk,kzk,k−1zk,k−2zk,k−3 = (zk+1,k + 1)(zk+1,k−1 − ak−1)(zk+1,k−2 − 1)(zk+1,k−3)

(A3) otherwise,

zk,kzk,k−1zk,k−2zk,k−3 = zk+1,kzk+1,k−1zk+1,k−2zk+1,k−3.

Let k = 3. We now deﬁne z3 = z3,m . . . z3,1:
• for i /∈ {1, 2, 3}, we set z3,l = z4,l,
• the subword z3,3z3,2z3,1 is determined as follows:

(B1) if z4,3 < a3, z4,2 > a2 and z4,1 = 0,

z3,3z3,2z3,1 = (z4,3 + 1)(z4,2 − (a2 + 1))(a1 − 1),

(B2) if z4,3 < a3, z4,2 ≥ a2 and a1 ≥ z4,1 > 0,

z3,3z3,2z3,1 = (z4,3 + 1)(z4,2 − a2)(z4,1 − 1),

(B3) if z4,3 < a3, z4,2 ≥ a2 and z4,1 > a1,

z3,3z3,2z3,1 = (z4,3 + 1)(z4,2 − a2 + 1)(z4,1 − a1 − 1),

(B4) if z4,2 < a2 and z4,1 ≥ a1,

z3,3z3,2z3,1 = z4,3(z4,2 + 1)(z4,1 − a1).
 5

(B5) otherwise, z3,3z3,2z3,1 = z4,3z4,2z4,1.

When we speak of the entry at position l after step k, we mean zk,l. When zk+1,l ̸= zk,l,
we say that at step k the entry in position l was changed. It follows immediately from the
algorithm that the only entries changed at step k, are in position k, k − 1, k − 2 or k − 3.

The goal of Algorithm 1 is to produce a word whose entry at position k is smaller or equal
to ak, and which represents the same value as s. The following two Propositions make this
statement precise.

Proposition 2.1. Algorithm 1 leaves the value represented unchanged. That is, for every
k ∈ N with 3 ≤ k ≤ m + 1 m
∑
i=0zk,i+1qi = m
∑
i=0 si+1qi.

Proof. It follows immediately from the recursive deﬁnition of the qi's (see ( 1.1)) that each
rule of Algorithm 1 leaves the value represented unchanged. Induction on k gives the
statement of the Proposition. □

Proposition 2.2. For k > 1, z3,k ≤ ak and z3,1 ≤ a1 − 1.

We will prove the following two lemmas ﬁrst.

Lemma 2.3. Let k ∈ N and k ≥ 3. Then
(i) If zk+1,k−1 = 2ak−1 + 1, then zk+1,k−2 = 0.
(ii) If zk+1,k−1 = 2ak−1, then zk+1,k−2 ≤ ak−2.

Proof. For (i), let zk+1,k−1 = 2ak−1 + 1. It follows immediately from the rules of the al-
gorithm that zk+2,k−1 = 2ak−1 + 1 and zm+1,k−1 = 2ak−1. So xk−1 and yk−1 are both equal
to ak−1. Hence xk−2 = 0, yk−2 = 0 and zm+1,k−2 = 0. The ﬁrst time that the entry in po-
sition k − 2 can be changed, is at step k + 1, when rule (A1) is applied. However, since
zk+2,k−1 = 2ak−1 + 1, rule (A1) was not applied at step k + 1. Thus zk+1,k−2 = zm+1,k−2 = 0.

For (ii), let zk+1,k−1 = 2ak−1. If xk−1 = yk−1 = ak−1, we argue as before to get zk+1,k−2 = 0.
Suppose that either xk−1 ̸= ak−1 or yk−1 ̸= ak−1. Because zk+1,k−1 = 2ak−1, we get that
xk−1 + yk−1 = 2ak−1 − 1, and that the entry in position k − 1 had to be increased by 1
at step k + 2. Hence either xk−1 = ak−1 or yk−1 = ak−1. By the deﬁnition of Ostrowski
representations, xk−2 + yk−2 ≤ ak−2. Thus zk+2,k−2 ≤ ak−2. Since the entry in position
k − 1 was increased by 1 at step k + 2, zk+2,k = ak − 1. Thus no change is made at step
k + 1. It follows that zk+1,k−2 = xk−2 + yk−2 ≤ ak−2. □

Lemma 2.4. Let k ∈ N and 3 ≤ k ≤ m.
(i)k If zk+1,k−1 > ak−1, then zk+1,k < ak.
(ii)k If zk+1,k−1 = ak−1 and zk+1,k−2 > 0, then zk+1,k < ak.

Proof. We prove the statements by induction on k. For k = m, both (i)m and (ii)m hold,
because zm+1,m = 0. For the induction step, suppose that (i)k+1 and (ii)k+1 hold. We need
to establish (i)k and (ii)k.

We ﬁrst show (i)k. Suppose zk+1,k−1 > ak−1. Towards a contradiction, assume that zk+1,k ≥
ak. Since zk+1,k−1 > ak−1 and the algorithm does not increase the entry in position k − 1
above ak−1 at step k + 1, we have zk+2,k−1 > ak−1. Because zk+1,k ≥ ak and the algorithm

6 P. HIERONYMI AND A. TERRY

either leaves the entry in position k at step k + 1 untouched or decreases it by ak or ak + 1,
we get that either zk+2,k = zk+1,k or zk+2,k ∈ {2ak, 2ak + 1}. We handle these cases sepa-
rately.

Suppose zk+2,k ∈ {2ak, 2ak + 1}. By (i)k+1, zk+2,k+1 < ak+1. It follows from Lemma 2.3
that, if zk+2,k = 2ak, then zk+2,k−1 ≤ ak−1, and if zk+2,k = 2ak + 1, then zk+2,k−1 = 0. Since
one of the ﬁrst two rules is applied at step k + 1, we have that zk+1,k−1 < ak−1. This con-
tradicts our assumption that zk+1,k−1 > ak−1.

Now, we suppose that zk+2,k = zk+1,k and zk+2,k = ak. Because zk+2,k−1 > ak−1, we get
zk+2,k+1 < ak+1 by (ii)k+1. Hence zk+1,k = zk+2,k − ak by rule (A2). This contradicts
zk+1,k = zk+2,k.

Finally, assume that zk+2,k = zk+1,k and zk+2,k > ak. By (i)k+1, zk+2,k+1 < ak+1. Since
zk+2,k−1 > ak−1, we have zk+2,k+1 < 2ak+1 by Lemma 2.3. Applying rule (A2) gives
zk+1,k = zk+2,k − ak. As before, this is a contradiction.

We now prove (ii)k. Let zk+1,k−1 = ak−1 and zk+1,k−2 > 0. Suppose towards a contradiction
that zk+1,k ≥ ak. Then zk+2,k ≥ ak, because the algorithm never increases the entry at
position k at step k + 1. Since zk+1,k−1 = ak−1, either zk+2,k−1 = ak−1 + 1 (in this case rule
(A2) was applied) or zk+2,k−1 = ak−1 (in this case rule (A3) was applied). In both cases,
zk+2,k+1 < ak+1 by (i)k+1 and (ii)k+1. Since zk+2,k−1 > 0, zk+2,k ≤ 2ak by Lemma 2.3(i).
Hence rule (A2) was applied at step k + 1, and zk+2,k−1 = ak−1 + 1. By Lemma 2.3(ii),
zk+2,k < 2ak. Thus zk+1,k = zk+2,k − ak < ak, a contradiction. □

Proof of Proposition 2.2. Suppose k ≥ 3. Because the entry at position k is not changed
after step k, it is enough to show that zk,k ≤ ak. We have to consider four different cases
depending on the value of zk+2,k.

First, consider the case that zk+2,k < ak. Since the algorithm does not increase the entry in
position k at step k + 1, zk+1,k < ak. Thus zk,k ≤ zk+1,k + 1 ≤ ak.

Suppose zk+2,k = ak and zk+2,k−1 > 0. By Lemma 2.4(ii), zk+2,k+1 < ak+1. By rule (A2),
zk+1,k = 0. Hence zk,k ≤ 1 ≤ ak.

Suppose zk+2,k = ak and zk+2,k−1 = 0. Then no change is made at step k + 1. Thus
zk+1,k = ak and zk+1,k−1 = 0. Since no change is made at step k as well, zk,k = ak.

Finally, consider zk+2,k > ak. By Lemma 2.4(i), zk+2,k+1 < ak+1 . Hence either rule (A1)
or rule (A2) is applied. We get that zk+1,k ≤ ak. If zk+1,k = ak, then zk,k = ak. If zk+1,k < ak,
then zk,k ≤ zk+1,k + 1 ≤ ak.

Now suppose that k < 3. We have to show that z3,k ≤ ak. We do so by considering several
different cases depending on the values of z4,2 and z4,1. By Lemma 2.4, if z4,2 > a2, or,
if z4,2 = a2 and z4,1 > 0, then z4,3 < a3. If z4,2 = a2 and z4,1 = 0, then no changes was made.

Suppose that z4,2 = 2a2 + 1. By Lemma 2.3, z4,1 = 0 . By rule (B1), z3,2 = a2, z3,1 = a1 − 1
and z3,3 = z4,3 + 1 ≤ a3.
 7

Now suppose that z4,2 = 2a2. We get z4,1 ≤ a1 from Lemma 2.3. Then either rule (B1)
or rule (B2) was applied. In both cases we get that z3,2 = a2, z3,1 = z4,1 − 1 ≤ a1 − 1 and
z3,3 = z4,3 + 1 ≤ a3.

Consider that a2 ≤ z4,2 < 2a2 and z4,1 > 0. Here either rule (B2) or rule (B3) was used.
Then z3,2 ≤ a2, z3,1 ≤ a1 − 1 and z3,3 = z4,3 + 1 ≤ a3.

The last case we have to consider is z4,2 < a2. Depending on whether z4,1 ≥ a1, we applied
either rule (B4) or rule (B5). Since z4,1 ≤ 2a1 − 1, we get z3,1 ≤ a1 − 1 and z3,2 ≤ z3,2 + 1 ≤
a2 in both cases. □

We will now describe the second step towards determining the Ostrowski representation
of M + N. This second algorithm will be a right-to-left pass over z3. Given the word
z3,mz3,m−1 . . . z3,2z3,1, we will recursively generate a word

wk = wk,m+1wk,m . . . wk,2wk,1
for each k ∈ N with k ∈ N with 2 ≤ k ≤ m + 1. At each step only elements in a moving
window of length 3 are changed. Because the algorithm moves right to left, we will start
by deﬁning w2, and then recursively deﬁne wk for k ≥ 2.

Algorithm 2. Let k = 2. Then set

w2 := 0z3,mz3,m−1 . . . z3,2z3,1.

Let k ∈ N with 2 < k ≤ m + 1. We now deﬁne wk = wk,m+1 . . . wk,1:
• for i /∈ {k, k − 1, k − 2}, we set wk,i := wk−1,i.
• if wk−1,k < ak, wk−1,k−1 = ak−1 and wk−1,k−2 > 0, set

wk,kwk,k−1wk,k−2 := (wk−1,k + 1)0(wk−1,k−2 − 1),

otherwise
 wk,kwk,k−1wk,k−2 := wk−1,kwk−1,k−1wk−1,k−2.

Again it follows immediately from Equation (1.1) that this algorithm leaves the value rep-
resented unchanged: m
∑
k=0 wm+1,k+1qk = m
∑
k=0 z3,k+1qk.

By Proposition 2.2 and the rules of Algorithm 2, wk,i ≤ ak for every k = 2, . . . , m + 1 and
i = 1, . . . , m + 2.

Lemma 2.5. There is no k ∈ N such that
• wm+1,k = ak
• wm+1,k−1 < ak−1,
• wm+1,k−2 = ak−2, and
• wm+1,k−3 > 0.

Proof. Towards a contradiction, suppose that there is such an k. We will ﬁrst show that
wk−2,k−3 > 0, wk−2,k−2 = ak−2 and wk−2,k−1 = ak−1.

Suppose that wk−2,k−3 = 0. Then the algorithm would not have made any changes at step
k − 2. Thus wk−1,k−3 = 0. Because the entry will not be changed later than step k − 1,
wm+1,k−3 = 0. However, this contradicts wm+1,k−3 > 0. Thus wk−2,k−3 > 0.

8 P. HIERONYMI AND A. TERRY

Suppose that wk−2,k−2 < ak−2. Then wk−1,k−2 = wk−2,k−2. This implies that wk,k−2 < ak−2
and wm+1,k−2 < ak. This a contradiction against our assumption wm+1,k−2 = ak−2. Hence
wk−2,k−2 = ak−2.

Now suppose that wk−2,k−1 < ak−1. Since wk−2,k−2 = ak−2 and wk−2,k−3 > 0, wk−1,k−2 = 0.
Thus wm+1,k−2 = 0, contradicting wm+1,k−2 = ak−2. So wk−2,k−1 = ak−1.

It follows that wk−1,k−1 = wk−2,k−1 = ak−1 and wk−1,k−2 = wk−1,k−2 = ak−2. We will now
argue that wk−1,k < ak.

Suppose towards a contradiction that wk−1,k = ak. Then wk,k = ak and wk,k−1 = ak−1. Since
wm+1,k−1 < ak−1, we have wk,k+1 < ak+1. Thus wk+1,k = 0. Hence wm+1,k = 0, a contra-
diction. So wk−1,k < ak.

We conclude that the entry at position k − 2 is changed at step k. Therefore, wk,k−2 =
wk−1,k−2 − 1 = ak−2 − 1. So wm+1,k−2 = ak−2 − 1. This contradicts our original assumption
wm+1,k−2 = ak−2. □

The third and ﬁnal step of our algorithm is a left-to-right pass over wm+1. The mov-
ing window is again of length 3 and we use the same rule as in step 2. Given the word
wm+1,m+1 . . . wm+1,1, we will recursively generate a word

vk := vk,m+2 . . . vk,1
for each k ∈ N with k ∈ N with 3 ≤ k ≤ m + 3. Because the algorithm moves left to right,
we will start by deﬁning wm+3 and then recursively deﬁne wk for k ≤ m + 3.

Algorithm 3. Let k = m + 3. Then set

vm+3 := 0wm+1,m+1 . . . wm+1,1.

Let k ∈ N with 3 ≤ k ≤ m + 2. We now deﬁne vk = vk,m+2 . . . vk,1:
• for i /∈ {k, k − 1, k − 2}, we set vk,i := vk+1,i,
• if vk+1,k < ak, vk+1,k−1 = ak−1 and vk+1,k−2 > 0, set

vk,kvk,k−1vk,k−2 := (vk+1,k + 1)0(vk+1,k−2 − 1),

otherwise vk,kvk,k−1vk,k−2 := vk+1,kvk+1,k−1vk+1,k−2.

As before Equation (1.1) implies that this algorithm leaves the value represented un-
changed: m
∑
k=0 wm+1,k+1qk = m
∑
k=0 v3,k+1qk.

Moveover, we have vk,i ≤ ak for every k = 3, ..., m + 3 and i = 1, . . . , m + 2. We will now
show v3 is indeed the Ostrowski representation of M + N. It is enough to prove the follow-
ing Proposition.

Proposition 2.6. Let l ≥ 3. Then there is no k ≥ l − 1 such that vl,k = ak and vl,k−1 > 0.

Before we give the proof of Proposition 2.6, we need one more Lemma.

Lemma 2.7. Let l ∈ {3, . . . , m + 3}. Then there is no k ∈ N such that
• vl,k = ak
• vl,k−1 < ak−1,
 9

• vl,k−2 = ak−2, and
• vl,k−3 > 0.

Proof. We prove the Lemma by induction on l. By Lemma 2.5, there is no such k for
m + 3. Suppose that the statement holds for l + 1. We want to show the statement for l.
Towards a contradiction, suppose that there is a k such that

(2.1) vl,k = ak, vl,k−1 < ak−1, vl,k−2 = ak−2 and vl,k−3 > 0.

By the induction hypothesis, it is enough to check that no change was made at step l; that
is vl,i = vl+1,i for i ∈ {k, ..., k − 3}. Since the algorithm only modiﬁes the entries at position
l, l + 1 or l + 2, we can assume that k ∈ {l − 2, . . . , l + 3}. We consider each case separately.

First, suppose k = l − 2. We get that vl,i = vl+1,i for i ∈ {k − 1, k − 2, k − 3}, because they
are not in the moving window at step l. The only possible change is at position k. Since
vl,l−2 < vl+1,l−2 by induction hypothesis, and vl,l−2 = al−2, we get vl,k = vl+1,k. So no
change is made.

Suppose that k = l − 1. If a change is made at step l, then vl,k = 0. But this contradicts
(2.1). Hence no change is made in this case.

Suppose that k = l. If a change is made at step l, then vl,k−2 = vl+1,k−2 − 1 < ak−2. As
before, this contradicts (2.1). Thus no change is made.

Suppose k = l + 1. If a change is made at step l, then vl,k−2 = 0 contradicting (2.1). So no
change is made in this case either.

Suppose k = l + 2. If a change is made at step l, then vl,k−3 = 0. This again contradicts
(2.1), and hence no change is made.

Finally suppose k = l + 3. By induction hypothesis, vl+1,k−3 = 0. Since vl,k−3 > 0, we have
vl+1,k−4 = ak−4 and vl+1,k−5 > 0. Then

vl+1,k−2 = ak−2, vl+1,k−3 = 0, vl+1,k−4 = ak−4 and vl+1,k−5 > 0.

This contradicts the induction hypothesis. □

Proof of Propositon 2.6. We prove this statement by induction on l. For l = m+3 the state-
ment holds trivially, because vm+3,m+2 = 0. Now suppose that the statement holds for l + 1,
but fails for l. Hence there is k ≥ l − 1 such that vl,k = ak and vl,k−1 > 0. Since vl+1,i = vl,i
for i > l, we have k ≤ l + 1. We now consider the three remaining cases k = l + 1, k = l
and k = l − 1 individually.

If k = l + 1, then vl+1,k = al+1,k. By the induction hypothesis, vl+1,k−1 = 0. But in order
for vl,k−1 > 0 to hold, we must have vl+1,k−2 = ak−2 and vl+1,k−3 > 0. This contradicts
Lemma 2.7.

If k = l, then either vl+1,k = ak or vl+1,k = ak − 1. Suppose that vl+1,k = ak − 1. Then
vl+1,k−1 = ak and vl+1,k−2 > 0. This implies vl,k−1 = 0, which contradicts vl,k−1 > 0. Sup-
pose that vl+1,k = ak. By induction hypothesis, vl+1,k−1 = 0. But then no change is made
at step l, and hence vl,k−1 = 0. A contradiction against vl,k−1 > 0.

10 P. HIERONYMI AND A. TERRY

If k = l − 1, then no change is made at step l, since vl,l−1 = al−1. Hence vl+1,l−1 = vl,l−1 =
al−1 and vl+1,l−2 = vl,l−2 > 0. Since no change was made at step l, we get that vl+1,l = al.
This contradicts the induction hypothesis. □

Corollary 2.8. The word v3,m+2 . . . v3,1 is the Ostrowski representation of M + N.

3. PROOF OF THEOREM A

In this section we will prove Theorem A. Let a be a quadratic irrational number. Let
[a0; a1, . . . , an, . . . ] be its continued fraction expansion. Since the continued fraction expan-
sion of a is periodic, it is of the form

[a0; a1, . . . , aξ−1, aξ , . . . , aν],

where ν − ξ is the length of the repeating block and the repeating block starts at ξ. We can
choose ξ and ν such that ξ > 4 and ν − ξ ≥ 3.4 Set µ := maxi ai. Set m := 2µ + 1. Set
Σa := {0, . . . , m}.

We ﬁrst remind the reader of the deﬁnitions of ﬁnite automata and recognizability. For
more details, we refer the reader to [11]. Let Σ be a ﬁnite set. We denote by Σ∗ the set of
words of ﬁnite length on Σ.

Deﬁnition 3.1. A nondeterministic ﬁnite automaton A over Σ is a quadruple (S, I, T, F),
where S is a ﬁnite non-empty set, called the set of states of A , I is a subset of S, called
the set of initial states, T ⊆ S × Σ × S is a non-empty set, called the transition table of A
and F is a subset of S, called the set of ﬁnal states of A . An automaton A = (S, I, T, F)
is deterministic if I contains exactly one element, and for every s ∈ S and w ∈ Σ∗ there
is exactly one s′ ∈ S such that (s, w, s′) ∈ T . We say that an automaton A on Σ accepts a
word w = wn . . . w1 ∈ Σ∗ if there is a sequence sn, . . . , s1, s0 ∈ S such that sn ∈ I, s0 ∈ F and
for i = 1, . . . , n, (si, wi, si−1) ∈ T . A subset L ⊆ Σ∗ is recognized by A if L is the set of
Σ-words that are accepted by A . We say that L ⊆ Σ∗ is recognizable if L is recognized by
some deterministic ﬁnite automaton.

It is well known (see [11, Theorem 2.3.3]) that a set is recognizable if it is recognized by
some nondeterministic ﬁnite automaton.

Let Σ be a set containing 0. Let z = (z1, . . . , zn) ∈ (Σ∗)n and let m be the maximal length of
z1, . . . , zn. We add to each zi the necessary number of 0's to get a word z′
i of length m. The
convolution
5 of z is deﬁned as the word z1 ∗ · · · ∗ zn ∈ (Σn)∗ whose i-th letter is the element
of Σn consisting of the i-th letters of z′
1, . . . , z′
n.

Deﬁnition 3.2. A subset X ⊂ (Σ∗)n is Σ-recognizable if the set

{z1 ∗ · · · ∗ zn : (z1, . . . , zn) ∈ X}

is Σn-recognizable.

We remind the reader that every natural number N can be written as N = ∑
n
k=0 bk+1qk,
where bk ∈ N such that b1 < a1, bk ≤ ak and, if bk = ak, bk−1 = 0, and that we denoted the
Σa-word bn . . . b1 by ρa(N).

4It might be the case that neither ξ nor ν are minimal, but this will be irrelevant here.
5Here we followed the presentation in [16]. For a general deﬁnition of convolution see [11].
 11

Deﬁnition 3.3. Let X ⊆ Nn. We say that X is a-recognizable if the set

{(0l1ρa(N1), . . . , 0lnρa(Nn)) : (N1, . . . , Nn) ∈ X, l1, . . . , ln ∈ N}

is Σa-recognizable.

In this section we will prove that a subset X ⊆ Nn is a-recognizable if and only if X is
deﬁnable in (N, +,Va).

Recognizability implies deﬁnability. We will ﬁrst show that whenever a set X ⊆ Nn is
a-recognizable, then X is deﬁnable in (N, +,Va). The proof here is an adjusted version of
the proofs in Villemaire [16] and [4].

First note that < is deﬁnable in (N, +,Va) and so is Va(N) = {qk : k ∈ N}. For convenience,
we write I for Va(N). We denote the successor function on I by sI.

Deﬁnition 3.4. For j ∈ {1, . . . , m}, let εj ⊆ I × N be the set of (x, y) ∈ I × N with

∃z ∈ N∃t ∈ N(z < x ∧ z + jx < sI(x) ∧Va(t) > x ∧Va(x + t) = x ∧ y = z + jx + t)

∨ ∃z ∈ N(z < x ∧ y < sI(x) ∧ y = z + jx).

Let ε0 ⊆ I × N be the set of (x, y) ∈ I × N with ⋀m
j=1 ¬εj(x, y).

This deﬁnition is inspired by [16, Lemma 2.3]. Obviously, εj is deﬁnable in (N, +,Va).
Because of the greediness of the Ostrowski representation, εj(x, y) holds iff x = qk for
some k ∈ N and the coefﬁcient of qk in the Ostrowski representation of y is j. We directly
get the following Lemma.

Lemma 3.5. Let l, n ∈ N and let ∑k bk+1qk be the Ostrowski representation of n. Then
bl+1 = j iff εj(ql, n).

Deﬁnition 3.6. Let Ie be the set of all y ∈ I with

∃z ∈ N ε1(1, z) ∧ ε1(y, z) ∧ ∀x ∈ I(
ε1(x, z) ↔ ¬ε1(sI(x), z)
),

and let Io be the set of all y ∈ I with

∃z ∈ N (¬ε1(1, z)) ∧ ε1(y, z) ∧ ∀x ∈ I(
ε1(x, z) ↔ ¬ε1(sI(x), z)
).

Obviously both Ie and Io are deﬁnable in (N, +,Va), I = Ie ∪ Io, and since q0 = 1,

Ie = {qk : k even } and Io = {qk : k odd }.

Deﬁnition 3.7. Let Ue ⊆ N be the set of all y ∈ N with

∀z ∈ Io ε0(z, y) ∧ ∀z ∈ Ie (ε0(z, y) ∨ ε1(z, y)),

and Uo ⊆ N be the set of all y ∈ N with

∀z ∈ Ie ε0(z, y) ∧ ∀z ∈ Io (ε0(z, y) ∨ ε1(z, y)).

Again it is easy to see that Ue and Uo are deﬁnable in (N, +,Va). We get the following
Lemma from Lemma 3.5.

Lemma 3.8. Let n ∈ N and let ∑k bk+1qk be the Ostrowski representation of n. Then
(i) n ∈ Ue if and only if for all even k bk+1 ≤ 1, and for all odd k bk+1 = 0,
(ii) n ∈ Uo if and only if for all odd k bk+1 ≤ 1, and for all even k bk+1 = 0.

Deﬁnition 3.9. Let ε ⊆ I × (Ue × Uo) be the set of all (x, (y1, y2)) with

(x ∈ Ie → ε1(x, y1)) ∧ (x ∈ Io → ε1(x, y2)).

12 P. HIERONYMI AND A. TERRY

Theorem 3.10. Let X ⊆ Nn be a-recognizable. Then X is deﬁnable in (N, +,Va).

Proof. Let X ⊆ Nn be a-recognizable by a ﬁnite automaton A = (S, I, T, F). Without loss
generality we can assume that the set of states S is {1, . . .,t} for some t ∈ N, and I = {1}.
Let ϕ be the formula deﬁning the following subset Z of Ut:

{(u1, . . . , ut ) ∈ Ut : ∀q ∈ I
 t⋀

i=1
 (
ε(q, ui) →
 t⋀

j=1, j̸=i¬ε(q, u j)
)
}.

So Z is the set of tuples (u1, . . . , ut) ∈ Ut such that for q ∈ I there is at most one i ∈ {1, . . . ,t}
such that ε(q, ui). Note that x ∈ X if there is a run s1 . . . sm of A on the word given by the
Ostrowski representation of the coordinates of x such that s1 = 1 and sm ∈ F. The idea now
is to code such a run as an element of Z. To be precise, a tuple (u1, . . . , ut ) ∈ Z will code
a run s1 . . . sm if for each qi ∈ I, si is the unique element k of {1, . . . ,t} such that ε(qi, uk).
Thus x = (x1, . . . , xn) ∈ X if and only if x satisﬁes the following formula in (N, +,Va):

∃u1, . . . , ut ∈ U ∃q ∈ I ϕ(u1, . . . , ut) ∧ ε(1, u1) ∧ ⋁

l∈F ε(q, ul)

∧ ⋀

(l,(ρ1,...,ρn),k)∈T ∀z ∈ I(
(z > q) →
 n⋀

i=1
 m⋀

j=1¬εj(z, xi)
)

∧
[(z ≤ q ∧ ε(z, ul) ∧
 n⋀

i=1ερi (z, xi)
) → ε(sI(z), uk)
].
 □

Deﬁnability implies recognizability. We will prove that if a subset X ⊆ Nn is deﬁnable
in (N, +,Va), then it is a-recognizable. By [10] it is sufﬁces to show that the set N and the
relations {(x, y) ∈ N2 : x = y}, {(x, y, z) ∈ N3 : x + y = z} and {(x, y) ∈ N2 : Va(x) = y}
are all a-recognizable. It is well known that N is a-recognizable (see for example [15,
Theorem 8]), and using that knowledge it is easy to check that {(x, y) ∈ N2 : x = y} and
{(x, y) ∈ N2 : Va(x) = y} are a-recognizable. We are now going to show that {(x, y, z) ∈
N3 : x + y = z} is a-recognizable.

By the work in the previous section, we have an algorithm to compute addition in Os-
trowski representation based on a. This algorithm consists of four steps, and we will
now show that each of the four steps can be recognized by a ﬁnite automaton. Given
two words z = zn . . . z1, z′ = z′
n . . . z′
1 ∈ ρa(N), the ﬁrst step is to compute the Σa-word
(zn + z′
n) . . . (z1 + z′
1), which we will denote by z + z′. It is straightforward to verify that
the set {z ∗ z′ ∗ (z + z′) : z, z′ ∈ ρa(N)} is recognizable by a ﬁnite automaton. For z, z′ ∈ Σ∗
a,
we will write z ⇝i z′ if Algorithm i produces z′ on input z. In the following, we will prove
that the set {z ∗ z
′ : z, z
′ ∈ Σ
∗
a, z ⇝i z
′} is recognizable by a ﬁnite automaton for i = 1, 2, 3.
From these results it is immediate that

{z ∗ z
′ ∗ z
′′ ∗ u0 ∗ u1 ∗ u2 : z, z
′, z
′′ ∈ ρa(N), u0, u1, u2 ∈ Σ
∗
a,

u0 = z + z
′, u0 ⇝1 u1 ⇝2 u2 ⇝3 z
′′}

is recognizable by a ﬁnite automaton. Since recognizability is preserved under projections
(see [11, Theorem 2.3.9]), {(x, y, z) ∈ N3 : x + y = z} is a-recognizable by Corollary 2.8.
Thus every set X ⊆ Nn deﬁnable in (N, +,Va) is a-recognizable.
 13

An automaton for Algorithm 1. We will now construct a non-deterministic automaton
A1 that recognizes the set {z ∗ z′ : z, z′ ∈ Σ∗
a, z ⇝1 z′}. Before giving the deﬁnition of
A1, we need to introduce some notation. Let A ⊆ N4
≤m × N4
≤m × N4
≤m be the set of tuples
(u, v, w) with

w =
 



 (v1 + 1, v2 − (u2 + 1), u3 − 1, v4 + 1), if v1 < u1, v2 > u2 and v3 = 0,
(v1 + 1, v2 − u2, v3 − 1, v4, if v1 < u1, u2 ≤ v2 ≤ 2u2 and v3 > 0,
(v1, v2, v3, v4), otherwise.

Let B ⊆ N3
≤m × N3
≤m × N3
≤m be the set of tuples (u, v, w) with

w =
 



 (v1 + 1, v2 − (u2 + 1), u3 − 1), v1 < u1, v2 > u2 and v3 = 0;
(v1 + 1, v2 − u2, v3 − 1), v1 < u1, v2 ≥ u2 and u1 ≥ v1 > 0,;
(v1 + 1, v2 − u2 + 1, v1 − u1 − 1), v1 < u1, v2 ≥ u2 and v1 > u1;
(v1, v2 + 1, v1 − u1), if v2 < u2 and v1 ≥ u1;
(v1, v2, v3), otherwise.

Note that A corresponds to the rules (A1),(A2) and (A3) of Algorithm 1, while B corre-
sponds to the rules (B1)-(B5) of Algorithm 1. The values of the variable u represent the
relevant part of the continued fraction, the values of the variable v are used to code the
entries in the moving window before any changes are carried out, and the values of the
variable w correspond to the entries in the moving window after the changes are carried
out. For i ∈ {4, . . . , ν} and l ∈ {0, 1},

P(i, l) :=
 



 (ai, ai−1, ai−2, aν), i = ξ + 2 and l = 1;
(ai, ai−1, aν, aν−1), i = ξ + 1 and l = 1;
(ai, aν, aν−1, aν−2), i = ξ and l = 1;
(ai, ai−1, ai−2, ai−3), otherwise.

We ﬁrst explain informally the construction of A1. Suppose we take z = zl . . . z1 ∈ Σ∗
a.
Now perform Algorithm 1 on z, and let the word z′ = z′
l . . . z′
1 be the output. In or-
der to carry out the operations at step k in Algorithm 1, we needed to know the val-
ues of ak, ak−1, ak−2, ak−3. Because of the periodicity of the continued fraction expan-
sion of a, there is i ≤ ν such ak = ai. Let l be 1 if k > ν and 0 otherwise. Then
P(i, l) = (ak, ak−1, ak−2, ak−3). Hence in order to reconstruct (ak, ak−1, ak−2, ak−3), it is
enough to save i and whether or not k ≤ ν. Moreover, to perform the operations at step k in
Algorithm 1, we also used the values of the last three entries in the moving window after
the changes in the previous step are carried out, but before the window moves to the right.
Let us denote the triple consisting of these entries by v = (v1, v2, v3) ∈ Σ3
a. So before the
operations at step k are performed, the values in the moving window are (v1, v2, v3, zk−3).
Note that at step k in the algorithm, we are reading in zk−3, and not zk. However, the value
of z′
k is determined at the same step. Indeed, at step k with k ≥ 4, the entries in the moving
window are changed as follows:

(v1, v2, v3, zk−3) ↦→ (z
′
k, v′
1, v′
2, v′
3),

for a certain triple (v′
1, v′
2, v′
3) ∈ Σ3
a with A(P(i, l), v1, v2, v3, zk−3, z′
k, v′
1, v′
2, v′
3). The values
in the moving window for step k − 1 will be (v′
1, v′
2, v′
3, zk−4). Because the value of z′
k is
only determined at step k, and thus at the same time z
′
k−3 is being read, we are required to
store the value of z′
k for three steps. In order to save this information when moving from
state to state, we introduce another triple (w1, w2, w3) ∈ Σ3
a. This triple will always contain
the last three digits of z′. That means that before step k, (w1, w2, w3) = (z′
k, z′
k−1, z′
k−2). We
now deﬁne the set of states of A1 as the set of quadruples (i, l, v, w), where i ≤ ν, l ∈ {0, 1},

14 P. HIERONYMI AND A. TERRY

v, w ∈ Σ3
a. The idea is that in each state of the automaton the pair (i, l) codes the relevant
part of the continued fraction expansion, v contains the entries of the moving window, and
w ∈ Σ3
a the values of z′
k that we needed to save. The automaton moves from one of these
states to another according to the rules described in Algorithm 1.

Here is the deﬁnition of the automaton A1 = (S1, I1, T1, F1).

1. The set S1 of states of A1 is

{(i, 1, v, w) : ξ ≤ i ≤ ν, v, w ∈ Σ
3
a}

∪ {(i, 0, v, w) : 3 ≤ i ≤ ν, v, w ∈ Σ
3
a},

2. the set I1 of initial states is

{(i, l, (0, 0, 0), (0, 0, 0)) ∈ S : i ≥ 4},

3. the transition table T1 contains the tuples (s, (x, y),t) ∈ S1 × Σ2
a × S1 that satisfy
w
′ = (w2, w3, y) and one of the following conditions:
a. i ̸= ξ, ( j, l′) = (i − 1, l), A(P(i, l), v, x, w1, v′),
b. i = ξ, l = 1, ( j, l′) = (ν, l), A(P(i, l), v, x, w1, v′),
c. i = ξ, l = 0, ( j, l′) = (i − 1, l), A(P(i, l), v, x, w1, v′)
d. i = 4, j = 3, A(P(4, l), v, x, w1, v′), B(a3, a2, a1, v′, w2, w3, y),
where s = (i, l, v, w), w = (w1, w2, w3) and t = ( j, k, v′, w′),
4. the set F1 of ﬁnal states is {(i, l, w, y) ∈ S1 : i = 3}.

We leave it to the reader to check the details that A indeed recognizes the set {z ∗ z′ :
z, z′ ∈ Σ∗
a, z ⇝1 z′}. The automata we constructed is non-deterministic, but as mentioned
above there is deterministic ﬁnite automaton that recognizes the same set.

Automata for Algorithm 2 and 3. We now describe the non-deterministic automata A2
and A3 recognizing the sets {z ∗ z′ : z, z′ ∈ Σ∗
a, z ⇝2 z′} and {z ∗ z′ : z, z′ ∈ Σ∗
a, z ⇝3 z′}.
Again, we have to ﬁx some notation ﬁrst. Let C ⊆ N3
≤m × N3
≤m × N3
≤m be the set of triples
(u, v, w) ∈ C such that

w = { (v1 + 1, 0, v3 − 1), if v1 < u1, v2 = u2 and v3 > 0;
(v1, v2, v3), otherwise.

The relation C represents the operation performed in both Algorithm 2 and 3. As for A
and B above, the values of the variable u correspond to the relevant part of the continued
fraction, while the values of the variables v and w represent the entries in the moving
window, before and after any changes are carried out. For i ∈ {3, . . . , ν} and l ∈ {0, 1},

Q(i, l) :=
 



 (ai, ai−1, aν), i = ξ + 1 and l = 1;
(ai, aν, aν−1), i = ξ and l = 1;
(ai, ai−1, ai−2), otherwise.

We start with an informal description of the automaton A2. Let z = zl . . . z1 ∈ Σ∗
a and
suppose that z′ = z′
l . . . z′
1 is the output of Algorithm 2 on input z. To perform the operations
at step k in Algorithm 2, we again need to know a certain part of the continued fraction
expansion of a; in this case (ak, ak−1, ak−2). As before it is enough to know the natural
numbers i ≤ ν with ak = ai, and whether k < ν. Set l to be 1 if k > ν and 0 otherwise. Then
Q(i, l) = (ak, ak−1, ak−2). When constructing A2, we have to be careful: the Algorithm 2
runs from the right to the left, but the automaton reads the input from the left to the right.

15

Let (v′
1, v′
2) ∈ Σ2
a be such that (zk, v′
1, v′
2) are the entries in the moving window before the
changes at step k are made. Then at step k, the entries change as follows:

(zk, v′
1, v′
2) ↦→ (v1, v2, z
′
k−2),

for some pair (v1, v2) ∈ Σ2
a with C(Q(i, l), zk, v′
1, v′
2, v1, v2, z′
k−2). So when the automaton
reads in (zk−2, z
′
k−2), the value of zk is used to determine z
′
k−2. Hence in contrast to A1,
the automaton A2 has to remember the value of zk, and not the value of z′
k. We deﬁne the
states of A2 to be tuples (i, l, v, w) ∈ {0, . . . , m} × {0, 1} × Σ2
a × Σ2
a. The pair v is again used
to save the entries of the moving window, and w is needed to remember the previously read
entries of z. The automaton moves from one of these states to another according to the
rules described in Algorithm 2. However, since the automaton reads the input backwards,
the automaton will go from a state (i, l, v, w) to a state (i′, l′, v′, w′) if Q(i, l) and Q(i′, l′)
are the correct parts of the continued fraction expansion of a and the algorithm transforms
(zk, v′
1, v′
2) to (v1, v2, z
′
k−2).

Here is the deﬁnition of the automaton A2 = (S2, I2, T2, F2).

1. The set S2 of states of A2 is

{(i, 1, v, w) : ξ ≤ i ≤ ν, v, w ∈ Σ
2
a}

∪ {(i, 0, v, w) : 2 ≤ i ≤ ξ, v, w ∈ Σ
2
a},

2. the set I2 of initial states is

{(i, l, (0, 0, 0), (0, 0, 0)) ∈ S : i ≥ 3},

3. the transition table T2 contains the tuples (s, (x, y),t) ∈ S2 × Σ2
a × S2 that satisfy
w
′ = (w2, x) and one of the following conditions:
a. i ̸= ξ, ( j, l′) = (i − 1, l),C(Q(i, l), w1, v′, v, y),
b. i = ξ, l = 1, ( j, l′) = (ν, l),C(Q(i, l), w1, v′, v, y),
c. i = ξ, l = 0, ( j, l′) = (i − 1, l),C(Q(i, l), w1, v′, v, y)
d. i = 3, j = 2, C(Q(i, 0), w, x, v, y),
where s = (i, l, v, w), w = (w1, w2) and t = ( j, k, v′, w′),
4. the set F2 of ﬁnal states is {(i, l, w, y) ∈ S2 : i = 3}.

As in the case of Algorithm 1, we leave it to the reader to verify that A2 recognizes the set
{z ∗ z′ : z, z′ ∈ Σ∗
a, z ⇝2 z′}. As before, while A2 is non-deterministic, there is a determin-
istic automata recognizing the same set as A2.

It is left to construct the automaton for Algorithm 3. The only difference between Al-
gorithm 2 and 3 is the direction in which the algorithm runs over the input. Hence the
only adjustment we need to make to A2, is to address the change in direction. Let A3 =
(S2, I2, T3, F2) be the automaton that has the same states as A2, but whose transition table
T3 contains the tuples (s, (x, y),t) ∈ S2 × Σ2
a × S2 that satisfy w′ = (w2, y) and one of the
following conditions:

a. i ̸= ξ, ( j, l′) = (i − 1, l),C(Q(i, l), v, x, w1, v′),
b. i = ξ, l = 1, ( j, l′) = (ν, l),C(Q(i, l), v, x, w1, v′),
c. i = ξ, l = 0, ( j, l′) = (i − 1, l),C(Q(i, l), v, x, w1, v′)
d. i = 3, j = 2, C(Q(i, 0), v, x, w, y),

where s = (i, l, v, w), w = (w1, w2) and t = ( j, k, v′, w′).

16 P. HIERONYMI AND A. TERRY

The set {z ∗ z′ : z, z′ ∈ Σ∗
a, z ⇝3 z′} is recognized by A3. So there is also a deterministic
automaton recognizes this set. This completes the proof of Theorem A.

REFERENCES

[1] Connor Ahlbach, Jeremy Usatine, Christiane Frougny, and Nicholas Pippenger. Efﬁ-
cient algorithms for Zeckendorf arithmetic. Fibonacci Quart., 51(3):249–255, 2013.
[2] Jean-Paul Allouche and Jeffrey Shallit. Automatic sequences. Cambridge University
Press, Cambridge, 2003. Theory, applications, generalizations.
[3] Val´erie Berth´e. Autour du syst`eme de num´eration d'O strowski. Bull. Belg. Math. Soc.
Simon Stevin, 8(2):209–239, 2001. Journ´ees Montoises d'Informatique Th´eorique
(Marne-la-Vall´ee, 2000).
[4] V´eronique Bruy`ere and Georges Hansel. Bertrand numeration systems and recog-
nizability. Theoret. Comput. Sci., 181(1):17–43, 1997. Latin American Theoretical
INformatics (Valpara´ıso, 1995).
[5] V´eronique Bruy`ere, Georges Hansel, Christian Michaux, and Roger Villemaire.
Logic and p-recognizable sets of integers. Bull. Belg. Math. Soc. Simon Stevin,
1(2):191–238, 1994. Journ´ees Montoises (Mons, 1992).
[6] J. Richard B¨uchi. Weak second-order arithmetic and ﬁnite automata. Z. Math. Logik
Grundlagen Math., 6:66–92, 1960.
[7] C. F. Du, H. Mousavi, L. Schaeffer, and J. Shallit. Decision algorithms for ﬁbonacci-
automatic words, with applications to pattern avoidance. ArXiv 1406.0670, 2014.
[8] Christiane Frougny. Representations of numbers and ﬁnite automata. Math. Systems
Theory, 25(1):37–60, 1992.
[9] Philipp Hieronymi. Expansions of the ordered additive group of real numbers by two
discrete subgroups. J. Symbolic Logic, to appear, arXiv:1407.7002, 2015.
[10] Bernard R. Hodgson. D´ecidabilit´e par automate ﬁni. Ann. Sci. Math. Qu´ebec,
7(1):39–57, 1983.
[11] Bakhadyr Khoussainov and Anil Nerode. Automata theory and its applications, vol-
ume 21 of Progress in Computer Science and Applied Logic. Birkh¨auser Boston, Inc.,
Boston, MA, 2001.
[12] Nathalie Loraud. β-shift, syst`emes de num´eration et automates. J. Th´eor. Nombres
Bordeaux, 7(2):473–498, 1995.
[13] Alexander Ostrowski. Bemerkungen zur Theorie der Diophantischen Approximatio-
nen. Abh. Math. Sem. Univ. Hamburg, 1(1):77–98, 1922.
[14] Andrew M. Rockett and Peter Sz¨usz. Continued fractions. World Scientiﬁc Publish-
ing Co., Inc., River Edge, NJ, 1992.
[15] Jeffrey Shallit. Numeration systems, linear recurrences, and regular sets. Inform. and
Comput., 113(2):331–347, 1994.
[16] Roger Villemaire. The theory of ⟨N, +,Vk,Vl⟩ is undecidable. Theoret. Comput. Sci.,
106(2):337–349, 1992.
[17] E. Zeckendorf. Repr´esentation des nombres naturels par une somme de nombres de
Fibonacci ou de nombres de Lucas. Bull. Soc. Roy. Sci. Li`ege, 41:179–182, 1972.
 17

DEPARTMENT OF MATHEMATICS, UNIVERSITY OF ILLINOIS AT URBANA-CHAMPAIGN, 1409 WEST
GREEN STREET, URBANA, IL 61801
E-mail address: phierony@illinois.edu
URL: http://www.math.uiuc.edu/~phierony

DEPARTMENT OF MATHEMATICS, UNIVERSITY OF ILLINOIS AT URBANA-CHAMPAIGN, 1409 WEST
GREEN STREET, URBANA, IL 61801
E-mail address: aterry@illinois.edu
