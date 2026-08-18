<!-- source: https://arxiv.org/pdf/2212.10069 | converted from PDF -->

arXiv:2212.10069v2  [math.CO]  21 Dec 2022
N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE
AND DIGITAL SEQUENCES

YANXI LI AND WEN WU∗

Abstract. In this paper, we introduce a variation of the factor complexity, called the N -
factor complexity, which allows us to characterize the complexity of sequences on an inﬁnite
alphabet. We evaluate precisely the N -factor complexity for the inﬁnite Fibonacci sequence f
given by Zhang, Wen and Wu [Electron. J. Comb., 24 (2017)]. The N -factor complexity of a
class of digit sequences, whose nth term is deﬁned to be the number of occurrences of a given
block in the base-k representation of n, is also discussed.

1. Introduction

The factor complexity of inﬁnite sequences on a ﬁnite alphabet was well studied in recent
decades. For an inﬁnite sequence a = a(0)a(1)a(2)a(3) . . . , its factor complexity Pa(n) counts
the number of distinct subwords a(i)a(i + 1) . . . a(i + n − 1) (i ≥ 0) where n ≥ 1 is an integer.
It measures the complexity or randomness of an inﬁnite sequence. It is well known that an
ultimately periodic sequence has a bounded factor complexity (see Morse and Hedlund [9]).
Among the non-periodic sequences, the Sturmian sequences have the smallest factor complexity
(see Morse and Hedlund [10]). For any morphic sequence a on a ﬁnite alphabet, one has Pa(n) =
O(n2) (see Allouche and Shallit [2]). For the study of sequences with linear factor complexity,
see for example Rote [13], Tan et al [14], Cassaigne et al [5, 6] and Cassaigne [4], etc. In
addition to factor complexity, many other variations of complexity were also proposed to depict
the characteristics of a sequence, such as permutation complexity (see Makarov [8], Widmer [15]),
Abelian complexity (see Richomme et al [11, 12]), maximal pattern complexity (see Kamae et al
[7]), palindrome complexity (see Allouche et al [1] and Bal´aˇzi et al [3]), etc.
The above complexities are proposed for inﬁnite sequences on a ﬁnite alphabet. While for the
sequences on an inﬁnite alphabet, such as the sequence of all prime numbers, the sequence of
Fibonacci numbers, κ-regular sequences, morphic sequences on an inﬁnite alphabet, the factor
complexity may be inﬁnite as well. The factor complexity fail to tell their diﬀerences in the
sense of complexity. In this paper, we introduce a variation of the factor complexity, called the
N -factor complexity, which allows us to characterize the complexity of the sequences on inﬁnite
alphabets.

1.1. N -factor complexity. First recall the deﬁnition of factor complexity. Let Σ ⊂ N be an
alphabet and a = a(0)a(1)a(2)a(3) . . . be an inﬁnite sequence (or inﬁnite word) on Σ. For n ≥ 1,
denote by a[i, i + n − 1] := a(i)a(i + 1) . . . a(i + n − 1), which is called a factor (or subword)
of a. Deﬁne Fa(n) = {a[i, i + n − 1] : i ≥ 0} as the set of all factors of a of length n. Let
Fa = ∪n≥0Fa(n) be the set of factors of a.

2020 Mathematics Subject Classiﬁcation. 68R15 and 11B85.
Key words and phrases. N -factor complexity; iniﬁnite Fibonacci sequence; digital sequences.
∗Wen Wu is the corresponding author.
 1

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 2

Deﬁnition 1.1 (Factor complexity). Let a ∈ Σ∞ be an inﬁnite sequence on a ﬁnite alphabet
Σ ⊂ N. The factor complexity Pa(n) of a is deﬁned to be ♯Fa(n), i.e. the number of distinct
factors (of length n) of a.

For N ≥ 1, deﬁne Fa(n, N ) as the set of factors of length n (of a) that are composed by
alphabets in ΣN = {0, 1, . . . , N − 1}. Namely,

Fa(n, N ) = Fa(n) ∩ Σn
N +1 = {a[i, i + n − 1] : i ≥ 0, and a(j) ≤ N for all i ≤ j ≤ i + n − 1}
.

Deﬁnition 1.2 (N -factor complexity). Let a ∈ Σ∞ where Σ ⊂ N is an (inﬁnite) alphabet. For
any integer N ≥ 1, the N -factor complexity of a is deﬁned to be

Pa(n, N ) = ♯Fa(n, N ).

Remark 1.3. Since Pa(n, N ) ≤ ♯Σn
N = N n, the N -factor complexity, which depends on both n
and N , is ﬁnite. Noting that Fa(n, N − 1) ⊂ Fa(n, N ), the function Pa(n, N ) is non-decreasing
with respect to N .

In the following, we focus on the N -factor complexity of the inﬁnite Fibonacci sequence f
introduced in [16] and a class of digital sequences sw = (s(n))n≥0 where s(n) is deﬁned in terms
of the number of occurrences of a given block w ∈ Σ∗
k in the base-k representation of n.

1.2. N -factor complexity of the inﬁnite Fibonacci sequence. The classic Fibonacci se-
quence is the ﬁxed point of the Fibonacci morphism σ deﬁned by 0 ↦→ 01, 1 ↦→ 0. Zhang et al [16]
extended the Fibonacci morphsim to the inﬁnite alphabet N. They introduced the morphism

τ :
 {(2i) ↦→ (2i)(2i + 1),
(2i + 1) ↦→ (2i + 2), for all i ∈ N (1.1)

and deﬁned the inﬁnite Fibonacci sequence f as the ﬁxed point of τ . Namely, f = τ ∞(0) and

f = 0 1 2 2 3 2 3 4 2 3 4 4 5 . . .

It is easy to see that Pf (n) = ∞ for any n ≥ 1.
Our ﬁrst result fully characterizes the N -factor complexity of the inﬁnite Fibonacci sequence
f . Let (Fk)k≥0 be the Fibonacci numbers deﬁned by

F0 = F1 = 1 and Fk = Fk−1 + Fk−2 for all k ≥ 2. (1.2)

Write φ(n) = max{k : Fk < n}. Below, we give the explicit expression of Pf (n, N ) for all N ≥ 0
and n ≥ 1.

Theorem 1.4. For all N ≥ 0 and n ≥ 1,

Pf (n, N ) =
 



0, if 0 ≤ N ≤ φ(n) − 2,
FN +2 − n, if N = φ(n) − 1 or φ(n),
C2N 2 + C1N + C0 if N ≥ φ(n) + 1 and N + φ(n) is even,
C2N 2 + C1N + C′
0 if N ≥ φ(n) + 1 and N + φ(n) is odd,

where C2 = n−1
4 , C1 = 1
2 (Fφ(n)+2 − (n − 1)φ(n)), C0 = (1 − 1
2 φ(n))Fφ(n)+2 + n−1
4 φ(n)
2 − n and
C′
0 = Fφ(n)+1 + 1
2 (1 − φ(n))Fφ(n)+2 + n−1
4 φ(n)
2 + 1−5n
4 .

Remark 1.5. For a ﬁxed N , when n is large enough, one see that Pf (n, N ) always decreases to
0 since 0 ≤ N ≤ φ(n) − 2 holds for any n ≥ FN +2. On the other hand, for any ﬁxed n ≥ 2, since
C1 > 0 and C2 > 0 for n ≥ 2, we have lim
N →∞ Pf (n, N ) = ∞. Nevertheless, we obtain that

lim
N →∞ Pf (n, N )
N 2 = n − 1
4 .

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 3

1.3. N -factor complexity of digital sequences. Let k ≥ 2 be an integer. For any m ∈ N
with kℓ−1 ≤ m < kℓ for some integer ℓ ≥ 1, one has m = ∑ℓ−1
i=0 mikℓ−1−i where mi ∈ Σk =
{0, 1, . . . , k − 1} for all i. The base-k representation of m is

(m)k := m0m1 . . . mℓ−1.

Deﬁnition 1.6 (Digitial sequences). Fix w = w0w1 . . . wq−1 ∈ Σq
k. For any m ∈ N, let sk,w(m)
be the number of occurrences of w in the base-k representation of m, i.e.,

sk,w(m) := ♯
{
0 ≤ i < |(m)k| − q : mimi+1 . . . mi+q−1 = w}

where (m)k = m0m1 . . . mℓ−1. We call sk,w = (sk,w(m))m≥0 a (k, w)-digital sequence.

Example 1.7. When k = 2, we have

m 0 1 2 3 4 5 6 7 8 . . .

(m)2 0 1 10 11 100 101 110 111 1000 . . .

s2,1(m) 0 1 1 2 1 2 2 3 1 . . .

s2,11(m) 0 0 0 1 0 0 1 2 0 . . .

We remark that sk,w is an unbounded κ-regular sequence (see [2] for more information on
κ-regular sequences). In particular, the sequences s2,1 (mod 2) and s2,11 (mod 2) are the well-
known Thue-Morse sequence and the Rudin-Shapiro sequence on the alphabet {0, 1}, respectively.
When k and w are clear for the context, we simply write s(m) := sk,w(m) and s := sk,w.
Our second result describes the N -factor complexity of the digital sequences. For all x ∈ R,
the notion ⌈x⌉ refers to the smallest integer that is larger or equal to x.

Theorem 1.8. Let n ≥ 1 and M = ⌈logk(n)⌉ + 2. For all N ≥ M ,

Ps(n, N ) =
 {d0N + d1, if w /∈ {0}∗ ∪ {k − 1}∗,
d3N 2 + d4N + d5, if w ∈ {0}∗ ∪ {k − 1}∗,

where d0 = Ps(n, M ) − Ps(n, M − 1), d1 = Ps(n, M ) − d0M , d3 = (n − 1)/2, d4 = d0 + (1 −
2M )(n − 1)/2 and d5 = Ps(n, M ) + (M 2 − M )(n − 1)/2.

Remark 1.9. The value of Ps(n, N ) depends on the initial values Ps(n, M ) and Ps(n, M − 1),
both of which vary with diﬀerent k, w and n. In particular, we see that when w ∈ {0}∗ ∪{k −1}∗,

lim
N →∞ Ps(n, N )
N 2 = n − 1
2 (1.3)

and when w /∈ {0}∗ ∪ {k − 1}∗,
 lim
N →∞ Ps(n, N )
N = d0 (1.4)

where d0 depends on k, w and n. These limits (1.3) and (1.4) could serve as a complexity for the
(unbounded) integer sequence sk.w. However, for w /∈ {0}∗ ∪ {k − 1}∗, it is quite challenging to
determine d0 precisely. Furthermore, in Proposition 4.20, we show that d0 is invariant while we
replace w by its conjugate.

The paper is organized as follows. In Section 2, we recall certain operations on words and give
a list of notations that are used in the paper. In Section 3, we discuss the N -factor complexity of
the inﬁnite Fibonacci sequence and prove Theorem 1.4. In Section 4, we study some combinatorial
properties of the digital sequences and prove Theorem 1.8.

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 4

2. Notations

In this section, we introduce notations that are used in the paper. We also provide a table of
notation; see Table 1.
Finite or inﬁnite words. Let A be an alphabet whose elements are called letters. A (ﬁnite)
word of length n on the alphabet A is a list of n letters w0w1 . . . wn−1 where wi ∈ A for all i.
Finite words are denoted by underlined characters w, u, v, etc. The length of a ﬁnite word w
is written as |w|. The empty word is denoted by ε. Let A
n be the set of all words of length
n on the alphabet A. Then A
∗ = ∪n≥0A
n is the set of all ﬁnite words on A where A
0 = {ε}.
For x = x0x1 . . . xi, y = y0y1 . . . yj ∈ A
∗, their concatenation, denoted by xy, is the word
x0x1 . . . xiy0y1 . . . yj. For all integer q ≥ 1, let x
q = x . . . x be the qth concatenation of x. For
u = u0u1 . . . uh ∈ A
∗, write
 u[i, j] = uiui+1 . . . uj

where 0 ≤ i ≤ j ≤ h. In addition, we deﬁne u[i, j] = ε for all j > h. For x, y ∈ A
∗, if x = y[i, j]
for some 0 ≤ i ≤ j ≤ |y| − 1, then x is a subword (or factor ) of y and we write x ≺ y. In
particular, if i = 0 (resp. j = |y| − 1), then we call x a preﬁx (resp. suﬃx ) of y, denoted by x ⊳ y
(resp. x ⊲ y). The number of occurrences of x in y is deﬁned as

|y|x = ♯{0 ≤ i ≤ |y| − 1 : y[i, i + |x| − 1] = x}.

The inﬁnite words (or sequences) on A are denoted by bold characters, such as a, s, c, etc. We
write a = (a(n))n≥0 = a(0)a(1)a(2) · · · where a(n) is the nth term of a. The set of all inﬁnite
words on A is A
∞. Similarly, we write a[i, j] = a(i)a(i + 1) . . . a(j) for 0 ≤ i ≤ j.

Base-k representation. For all integer k ≥ 1, let Σk = {0, 1, . . . , k − 1}. For all m ∈ N
with kℓ−1 ≤ m < kℓ for some integer ℓ ≥ 1, we have m = ∑ℓ−1
i=0 mikℓ−1+i where mi ∈ Σk for all
i = 0, 1, . . . , ℓ − 1 and m0 ̸= 0. The base-k representation of m is deﬁne as

(m)k = m0m1 . . . mℓ−1 ∈ Σ∗
k.

Conversely, for any u = u0u1 . . . uh ∈ Σ∗
k, the base-k realization of u is deﬁned as

[u]k =
 h∑

i=0 uikh−i.

It is possible that ([u]k)k ̸= u since u0 is not necessarily zero.

Sets of factors. Let Σ ⊂ N be an (inﬁnite) set of nonnegative integers. Let a ∈ Σ∞

be an inﬁnite sequence. Recall that for all n ≥ 1 and N ≥ 1, Fa(n) is the set of all factors
(of length n) of a and Fa(n, N ) = Fa(n) ∩ Σn
N +1. Since Fa(n − 1) ⊂ Fa(n), we see that
Fa(n, N − 1) ⊂ Fa(n, N ). In the study of N -factor complexity, we need the to count the factors
in which the letter N occurs. For this purpose, we deﬁne

F (1)
a (n, N ) := Fa(n, N )\Fa(n, N − 1).

The ﬁrst and second order diﬀerence of Pa(n, N ) on the variable N are denoted by

P (1)
a (n, N ) := Pa(n, N ) − Pa(n, N − 1) (N ≥ 2), (2.1)

P (2)
a (n, N ) := P (1)
a (n, N ) − P (1)
a (n, N − 1) (N ≥ 3). (2.2)

Then P (1)
a (n, N ) = ♯F (1)
a (n, N ).

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 5

N, N≥1 Non-negative integers; positive integers.
⌈n⌉, ⌊n⌋ The smallest integer but not smaller than n; the largest integer but not larger
than n.
ΣN A ﬁnite alphabet consisting of 0, 1, . . . , N − 1.
Σ∗ The set of words of arbitrary length composed by the elements in Σ.
Σn The set of words of length n composed by the elements in Σ.
w An underlined character represents a word w = w0w1 . . . w|w|−1.
a A bold character represents a sequence a = a(0)a(1) . . . .
w[i, j], a[i, j] The segment wiwi+1 . . . wj; the segment a(i)a(i + 1) . . . a(j).
ε The empty word.
wq A word composed by q consecutive w’s.
( · )k The base-k representation of a non-negative integer.
[ · ]k The base-k realization of a word in Σ∗
k, e.g. [w0 . . . wq−1]k = ∑q−1
i=0 wikq−1−i.
| · | The length of a word.
| · |w The number of occurrence of w in a word.
x ≺ y (or y) x occurs in the word y (or the sequence y).
x ⊳ y, x ⊲ y x is a preﬁx of y; x is a suﬃx of y.
Fi The ith Fibonacci number.
φ(n) The maximal index of the Fibonacci numbers that are smaller than n.
u ± 1 The word (u0 ± 1)(u1 ± 1) . . . (u|u|−1 ± 1)
Fa(n, N ) The set of factors of length n (of a) that are composed by alphabets in ΣN +1.
F (1)
a (n, N ) The set diﬀerence of Fa(n, N ) and Fa(n, N − 1).
Pa(n, N ) The number of elements in Fa(n, N ).
P (1)
a (n, N ) The ﬁrst order diﬀerence of Pa(n, N ) on the variable N .
P (2)
a (n, N ) The second order diﬀerence of Pa(n, N ) on the variable N .
Table 1. List of notations

3. Infinite Fibonacci Sequence

Let τ be the morphism on N deﬁned in (1.1). Its ﬁxed point f = τ ∞(0) is the inﬁnite Fibonacci
sequence. In this section, we give the explicit expression of the N -factor complexity Pf (n, N ) of
the inﬁnite Fibonacci sequence f . Recall that Fi is the ith Fibonacci number given in (1.2).
Using the deﬁnition of τ , we have the following lemma.

Lemma 3.1. Suppose p, q ≥ 0 and q is even. Let u = τ p(q). Then |u| = Fp+1. Further, u0 = q,
uFp+1−1 = p + q, and q + 1 ≤ ui ≤ p + q − 1 for 1 ≤ i ≤ Fp+1 − 2.

The next result shows that all factors of f in Ff (n, N ) can be found in the preﬁx (of f ) of
length FN +2, which reduces our work in calculating Pf (n, N ).

Lemma 3.2. If N ≥ 1 and n ≥ 1, then Ff (n, N ) = Fτ N +1(0)(n, N ).

Proof. It is enough to show that Fτ N +1(0)(n, N ) = Fτ N +i(0)(n, N ) for all i ≥ 2. We prove by
induction on i. Let q ≥ 0 be an even number. Since τ p+1(q) = τ p(q) τ p−1(q + 2), then

Fτ p−1(q+2)(n, p + q) ⊂ Fτ p+1(q)(n, p + q). (3.1)

By Lemma 3.1, we know p + q + 1 ⊲ τ p+1(q), which implies

Fτ p+1(q)τ p−1(q+2)(n, p + q) = Fτ p+1(q)(n, p + q) ∪ Fτ p−1(q+2)(n, p + q).

Combining with (3.1), we have

Fτ p+1(q)τ p−1(q+2)(n, p + q) = Fτ p+1(q)(n, p + q).

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 6

Repeating the above procedure, it follows that

Fτ p+1(q)(n, p + q) = Fτ p+1(q)τ p−1(q+2)···τ p−2k+1(q+2k)(n, p + q) (3.2)

for all 0 ≤ k ≤ ⌊p/2⌋. Note that

τ N +2(0) =
 {
τ N +1(0)τ N −1(2)τ N −3(4) · · · τ 3(N − 2)τ 1(N )τ 0(N + 2), if N is even,
τ N +1(0)τ N −1(2)τ N −3(4) · · · τ 2(N − 1)τ 1(N + 1), if N is odd.

Since τ 0(N + 2) = τ 1(N + 1) = N + 2, the equation (3.2) yields that

Fτ N +1(0)(n, N ) = Fτ N +2(0)(n, N ). (3.3)

Now suppose Fτ N +1(0)(n, N ) = Fτ N +k(0)(n, N ) for some k ≥ 2. It follows from (3.3) that
Fτ N +k(0)(n, N + k − 1) = Fτ N +k+1(0)(n, N + k − 1). Since N + k − 1 > N , by the deﬁnition of
Ff (n, N ), we have Fτ N +k(0)(n, N ) = Fτ N +k+1(0)(n, N ).

As a result, Ff (n, N ) = Fτ N +1(0)(n, N ). □

Recall that φ(n) = max{k : Fk < n}. In Proposition 3.3, we determine Pf (1, N ) for all N ≥ 0
and Pf (n, N ) for N < φ(n) when n ≥ 2. The explicit expressions of P (1)
f (n, N ) for all N ≥ φ(n)
are given in Proposition 3.4.

Proposition 3.3. If n = 1, then Pf (1, N ) = N + 1 for all N ≥ 0. If n ≥ 2, we have

Pf (n, N ) =
 {0, if 0 ≤ N ≤ φ(n) − 2,
FN +2 − n, if N = φ(n) − 1.

Proof. For every N ≥ 0, we have N ≺ τ N (0) ≺ f . So

Pf (1, N ) = N + 1.

Suppose n ≥ 2. If N ≤ φ(n) − 2, then n > FN +2 = |τ N +1(0)|. It follows from Lemma 3.2 that

Pf (n, N ) = 0.

In the case N = φ(n) − 1, we see that FN +1 < n ≤ FN +2. Note that N = 0 implies n = 2. Since
|f |0 = 1, we have Pf (2, 0) = 0 = F2 − 2. If N ≥ 1, then

τ N +1(0) = τ N (0) τ N −1(2),

where |τ N (0)| = FN +1 and |τ N −1(2)| = FN . Combining with Lemma 3.1, we see that

τ N +1(0)[i − n + 1, i] ∈ Fτ N +1(0)(n, N )

whenever n − 1 ≤ i < FN +2 − 1. Moreover, since FN +1 < n ≤ FN +2, the (FN +1 − 1)-th term
of τ N +1(0) (which is the ﬁrst letter ‘N ’ in the sequence f ) must be contained in the subword
τ N +1(0)[i − n + 1, i]. It follows from Lemma 3.1 that τ N +1(0)[0, n − 1], . . . , τ N +1(0)[FN +2 − n −
1, FN +2 − 2] are all diﬀerent. Hence, by Lemma 3.2,

Pf (n, N ) = Pτ N +1(0)(n, N ) = FN +2 − n. □

Proposition 3.4. For all n ≥ 2,

P (1)
f (n, N ) =
 



FN , if N = φ(n),
Fφ(n)+1 + (n − 1)(N − φ(n) − 1)/2, if N ≥ φ(n) + 1 and N + φ(n) is odd,
Fφ(n) + (n − 1)(N − φ(n))/2, if N ≥ φ(n) + 1 and N + φ(n) is even.

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 7

τ N (0) τ N −2(2) · · · τ N −2j0 (2j0 ) τ N −2j0−2(2j0 + 2) · · · τ 3(N − 3) τ 1(N − 1) τ 0(N + 1)

FN +1 FN −1 · · · FN −2j0+1 FN −2j0−1 · · · F4 F2 F1

Table 2. Decomposition of τ N +1(0) when N is odd.

Proof. If N = φ(n), noting that τ N +1(0) = τ N (0) τ N −1(2), then

τ N +1(0)[i − n + 1, i] ∈ F (1)
τ N +1(0)(n, N ) if and only if FN +1 − 1 ≤ i < FN +2 − 1.

So P (1)
f (n, N ) = FN . Now suppose N ≥ φ(n) + 1, and namely Fφ(n) < n ≤ Fφ(n)+1 ≤ FN .
Case 1: N is odd. In this case τ N +1(0) has the following decomposition

τ N +1(0) =
 



⌊N/2⌋∏

j=0 τ N −2j(2j)



 τ 0(N + 1) = τ N (0) · · · τ 1(N − 1)τ 0(N + 1) (3.4)

where ∏ refers the concatenation between word (see also Table 2) and τ 0(N + 1) = N + 1. For
all 0 ≤ j ≤ ⌊N/2⌋, we see that |τ N −2j (2j)| = FN −2j+1, |τ N −2j (2j)|N = 1 and N ⊲ τ N −2j(2j).
There exists 0 ≤ j0 ≤ ⌊N/2⌋ such that

N − 2j0 =
 {φ(n), if φ(n) is odd;
φ(n) + 1, if φ(n) is even.

For all FN +2 − FN −2j0 − 1 ≤ i ≤ FN +2 − 2, since Fφ(n) < n ≤ Fφ(n)+1, we have N ≺
f [i − n + 1, i]. Remark that f (FN +2 − 2) is the last term of τ 1(N − 1) in the decomposition (3.4),
and f (FN +2 − FN −2j0 − 1) is the last term of τ N −2j0 (2j0) in the decomposition (3.4). Further,
the term f (i − n + 1) is always in the segment τ N −2j0 (2j0) since n ≤ Fφ(n)+1 ≤ FN −2j0+1. So
we have found FN −2j0 diﬀerent factors in F (1)
τ N +1(0)(n, N ).
For all i < FN +2 − FN −2j0 − 1, since n ≤ Fφ(n)+1, we have ∣
∣f [i − n + 1, i]∣
∣
N ≤ 1. If f (i) = N ,
then f [i − n + 1, i] ⊲ τ N −2j (2j) for some 0 ≤ j < j0. However,

τ N −2j(2j) = τ N −2j−1(2j)τ N −2j−2(2j + 2) · · · τ N −2j0 (2j0).

Thus, in fact, if f (i) = N , then f [i − n + 1, i] ⊲ τ N −2j0 (2j0) and

f [i − n + 1, i] = f [FN +2 − FN −2j0 − n, FN +2 − FN −2j0 − 1].

If f (i − k) = N where 1 ≤ k ≤ n − 1, then f (i − k + 1) ⊳ τ N −2j(2j) for some 1 ≤ j ≤ j0. Hence,
f (i − k + 1) can take j0 diﬀerent values, namely, 2, 4, . . . , 2j0. As i and k vary, we have (n − 1)j0
new factors in F (1)
τ N +1(0)(n, N ) when i < FN +2 − FN −2j0 − 1. In summary,

P (1)
f (n, N ) = FN −2j0 + (n − 1)j0.

Case 2: N is even. In this case τ N +1(0) has the following decomposition

τ N +1(0) =
 


N/2∏

j=0 τ N −2j (2j)



 τ 0(N + 1) = τ N (0) · · · τ 0(N )τ 0(N + 1).

There exists 0 ≤ j1 ≤ N/2 such that

N − 2j1 =
 {φ(n), if φ(n) is even;
φ(n) + 1, if φ(n) is odd.

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 8

A similar discussion as in Case 1 yields that P (1)
f (n, N ) = FN −2j1 + (n − 1)j1. □

From Proposition 3.4, we obtain the second order diﬀerence of the N -factor complexity
Pf (n, N ).

Corollary 3.5. If n ≥ 3 and N ≥ φ(n) + 1, then the following holds:

P (2)
f (n, N ) =
 {(n − 1) − Fφ(n)−1, if N + φ(n) is even,
Fφ(n)−1, if N + φ(n) is odd.

Now we are able to prove our ﬁrst main result (Theorem 1.4).

Proof of Theorem 1.4. The result follows from Proposition 3.3 and Proposition 3.4. □

4. N -factor complexity of the digital sequences

In this section, we study the N -factor complexity of the digital sequence sk,w deﬁned in
Deﬁnition 1.6. The main result in this section is the following.

Theorem 4.1. Let n ≥ 1 be an integer and w ∈ Σ∗
k\{ε}. For all N ≥ ⌈logk(n)⌉ + 2,

P (2)
s (n, N ) =
 {n − 1, if w ∈ {0}∗ ∪ {k − 1}∗,
0, if w /∈ {0}∗ ∪ {k − 1}∗.

The proof of Theorem 4.1 are separated into the following three cases. We deal with the case
(k, w) = (2, 1) in Proposition 4.3 (see Section 4.1). The second case (k, w) ̸= (2, 1) and w = 0q

or (k − 1)
q is given in Proposition 4.14 (see Section 4.2.1). The last case (k, w) ̸= (2, 1) and
w /∈ {0}∗ ∪ {k − 1}∗ is discussed in Proposition 4.18 (see Section 4.2.2).
In Section 4.3, we compare the N -factor complexities of sk,w and sk,conj(w) where w /∈ {0}∗ ∪
{k − 1}∗. Hereafter, for u ∈ N∗, we write

u ± 1 := (u0 ± 1)(u1 ± 1) . . . (u|u|−1 ± 1).

For simplicity, we write s := sk,w. One can ﬁnd the proper values of k and w from the context.

4.1. The case (k, w) = (2, 1). In this case, s = s2,1 = (s(m))m≥0. We observer that

s(m) = 0 ⇐⇒ m = 0, and s(m) = 1 ⇐⇒ m is a power of 2.

Further, for all N > log2(n), we have 0 ̸≺ u for every u ∈ F (1)
s (n, N ). In fact, if 0 ≺ u, then
u = s[0, n − 1] and s(m) = N for some 1 ≤ m ≤ n − 1. However, s(m) = N implies m ≥ 2N − 1
and log2(n) ≥ log2(m + 1) ≥ N which is impossible.
A relation between factors in F (1)
s (n, N ) and F (1)
s (n, N + 1) is given below.

Proposition 4.2. Let k = 2, w = 1 and n ≥ 1. Suppose that u ∈ Nn
≥1. For all N ≥ ⌈logk(n)⌉+2,

we have u ∈ F (1)
s (n, N ) if and only if u + 1 ∈ F (1)
s (n, N + 1).

Proof. ‘⇒’ Suppose that u ∈ F (1)
s (n, N ) and u = s[m, m+n−1] for some m ≥ 0. Let m′ = m+2p

where p ≥ |(m + n)k|. Then for all 0 ≤ i ≤ n − 1,

s(m′ + i) = |(m′ + i)k|1 = 1 + |(m + i)k|1 = 1 + s(m + i).

Therefore, u + 1 = s[m′, m′ + n − 1] ∈ F (1)
s (n, N + 1).
‘⇐’ Suppose that u+1 = s[m, m+n−1] ∈ F (1)
s (n, N +1). We claim that |(m+i)k| = |(m)k| =: ℓ
for all 0 ≤ i ≤ n − 1. Otherwise, there exists a j ≤ n − 1 such that m + j = 10ℓ which contradicts
to the fact that s(m + j) ≥ 2. Let m′ = m − 2ℓ−1. We have s(m′ + i) = s(m + i) − 1 for all
0 ≤ i ≤ n − 1. Therefore, u = s[m′, m′ + n − 1] ∈ F (1)
s (n, N ). □

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 9

Recall that in Section 2 we have deﬁned that

P (2)
s (n, N ) = P (1)
s (n, N ) − P (1)
s (n, N − 1)

= ♯F (1)
s (n, N ) − ♯F (1)
s (n, N − 1).

Since for any u ∈ F (1)
s (n, N ) with N > log2(n), we have 0 ̸≺ u. By Proposition 4.2, there is a one-
to-one correspondence between elements in F (1)
s (n, N − 1) and elements in {u ∈ F (1)
s (n, N ) : 1 ̸≺
u}. Thus P (2)
s (n, N ) = ♯{u ∈ F (1)
s (n, N ) : 1 ≺ u} =: ♯G. (4.1)

To estimate P (2)
s (n, N ), we only need to ﬁnd all factors of s that contain both 1 and N .

Proposition 4.3. Let k = 2, w = 1 and n ≥ 1. For all N ≥ ⌈logk(n)⌉ + 2, we have

P (2)
s (n, N ) = n − 1.

Proof. When n = 1, it is easy to see that Ps(1, N ) = N + 1 and P (2)
s (1, N ) = 0. Now we assume
that n ≥ 2. Recall that s(m) = 1 if and only if m = 2ℓ for some ℓ ≥ 1. Let

Gp = {s[h, h + n − 1] ∈ F (1)
s (n, N ) : 2p−1 ≤ h < 2p, 1 ≺ s[h, h + n − 1]}.

Then according to (4.1), we have G = ∪p≥1Gp. Observe that for p ≥ 1,

s(2p−1) s(2p−1 + 1) · · · s(2p − 2) s(2p − 1) s(2p)

= 1 ∈ {2, 3, . . . , p − 1} = p = 1

We have Gp = ∅ for 1 ≤ p ≤ N − 1. When p = N , since n ≤ 2N −2 < 2p−1, we have

s(2N −1) · · · s(2N − 1) s(2N ) . . . s(2N + 2N −1 − 1)

= 1 ∈ {2, 3, . . . , N − 1} = N = 1 ∈ {2, 3, . . . , N − 1} = N

Consequently, GN = {s[h, h + n − 1] : 2N − n + 1 ≤ h ≤ 2N − 1}

and ♯GN = n − 1. When p > N ,

s(2p−1) · · · s(2p−1 + 2N −1 − 1) · · · s(2p − 1) s(2p)

= 1 ∈ {2, 3, . . . , N − 1} = N ≥ 2 > N = 1

For all 2p−1 ≤ j < 2p, in order that 1 ≺ s[h, h + n − 1], we need h = 2p−1 or h + n − 1 ≥ 2p.
If h = 2p−1, then it follows from n ≤ kN −2 that N ̸≺ s[h, h + n − 1]. If h + n − 1 ≥ 2p, then
N < p = s(2p − 1) ≺ s[h, h + n − 1]. We conclude that Gp = ∅ for p > N . Therefore, G = GN
and P (2)
s (n, N ) = n − 1. □

4.2. The case (k, w) ̸= (2, 1). We ﬁrst give a relation between factors in F (1)
s (n, N ) and
F (1)
s (n, N + 1) as in Proposition 4.2.

Proposition 4.4. Suppose (k, w) ̸= (2, 1). Let n ≥ 1 and u ∈ Nn. Then for all N ≥ ⌈logk n⌉+1,
u ∈ F (1)
s (n, N ) if and only if u + 1 ∈ F (1)
s (n, N + 1).

Proof. The proof is lengthy. We separate it into two parts. The ‘only if’ part is proved in Lemma
4.5. The ‘if’ part is proved in Lemma 4.7. □

Lemma 4.5. Suppose that (k, w) ̸= (2, 1). Let n ≥ 1 and u ∈ Nn. Then for all N ≥ ⌈logk n⌉+ 1,
we have u + 1 ∈ F (1)
s (n, N + 1) if u ∈ F (1)
s (n, N ).

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 10

Proof. Since u ∈ F (1)
s (n, N ), we have u = s(m)s(m + 1) · · · s(m + n − 1) for some m ≥ 0.
Let |(m)k| = ℓ. We can assume that ℓ ≥ N . (In fact, when (k, w) ̸= (2, 1), we can ﬁnd
arbitrarily long word v ∈ Σ∗
k with v0 ̸= 0 and |v (m)k|w = 0. Write t = [
v (m)k]

k. We have
u = s(t)s(t + 1) · · · s(t + n − 1) and |(t)k| ≥ N .) Then

n ≤ kN −1 ≤ kℓ−1 ≤ m < kℓ and m + n − 1 ≤ kℓ + kℓ−1.

We conclude that |(m + n − 1)k| − |(m)k| = 0 or 1.

To show u + 1 ∈ F (1)
s (n, N + 1), we only need to ﬁnd m′ such that for all 0 ≤ i ≤ n − 1,

s(m′ + i) = s(m + i) + 1. (4.2)

In the following, for 0 ≤ i ≤ n − 1, whenever m + i ≥ kℓ, we write

(m + i)k = 1ω(i)

where ω(i) ∈ Σℓ
k.

• Case 1: w = 0. Set m′ = kℓ+2 + (k − 1)kℓ + m, namely (m′)k = 10(k − 1)(m)k. If
m + n − 1 < kℓ, then for all 0 ≤ i ≤ n − 1, (m′ + i)k = 10(k − 1)(m + i)k. Thus (4.2)
holds. If m + n − 1 ≥ kℓ, then for all 0 ≤ i ≤ n − 1,

(m′ + i)k =
 {
10(k − 1)(m + i)k, if m + i < kℓ,
110 ω(i), if m + i ≥ kℓ,

which implies that (4.2) holds.
• Case 2: w = 0q where q ≥ 2. If m + n − 1 < kℓ, then let m′ = kℓ+q + m, namely
(m′)k = 10q(m)k. We see that for all 0 ≤ i ≤ n − 1, (m′ + i)k = 10q(m + i)k and
|(m′ + i)k|0q = |10q(m + i)k|0q = 1 + |(m + i)k|0q since m ≥ kℓ−1. Thus (4.2) holds. If
m + n − 1 ≥ kℓ, then we choose m′ = kℓ+q+2 + kℓ+1 + m, namely (m′)k = 10q10(m)k.
For 0 ≤ i ≤ n − 1,

(m′ + i)k =
 {10q10(m + i)k, if m + i < kℓ,
10q11 ω(i), if m + i ≥ kℓ,

which implies that (4.2) holds.
• Case 3: w0 ̸= 0. Let m′ be the integer with (m′)k = w 0q(m)k, where q = |w|. Then for
all 0 ≤ i ≤ n − 1,

(m′ + i)k =
 {w 0q (m + i)k, if m + i < kℓ,
w 0q−1(m + i)k, if m + i ≥ kℓ.

Since |w| = q and w0 ̸= 0, we have for all 0 ≤ i ≤ n − 1,

|(m′ + i)k|w =
 {|w 0q (m + i)k|w = |w 0q|w + |(m + i)k|w, if m + i < kℓ,
|w 0q−1(m + i)k|w = |w 0q−1|w + |(m + i)k|w, if m + i ≥ kℓ,

= 1 + |(m + i)k|w.

Consequently, (4.2) holds.
• Case 4: w0 = 0 and w ̸= 0q. When k ≥ 3, let m′ be the integer with (m′) = 1 w 1q (m)k.
For all 0 ≤ i ≤ n − 1,

(m′ + i)k =
 {1 w 1q (m + i)k, if m + i < kℓ,
1 w 1q−12 ω(i), if m + i ≥ kℓ, (4.3)

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 11

where (m + i)k = 1 ω(i) for kℓ − m ≤ i ≤ n − 1. Note that when m + i ≥ kℓ,

|ω(i)|w = |2 ω(i)|w = |1 ω(i)|w = |(m + i)k|w.

It follows from (4.3) that for all 0 ≤ i ≤ n − 1,

|(m′ + i)k|w = |1 w 1q−1|w + |(m + i)k|w = 1 + |(m + i)k|w.

We conclude that m′ satisﬁes (4.2). In the following, we deal with the sub-case k = 2.

w = 0w1 · · · wq−1 (m′)k (m′ + i)k

if m + i < kℓ if m + i ≥ kℓ

w1 = 0 1 w 1q0 (m)k 1 w 1q0 (m + i)k 1 w 1q1 ω(i)

w1 = 1, wq−1 = 1
(w = 01q−1) 101q−201q−1(m)k 101q−201q−1(m + i)k 101q−10q−1 ω(i)

w1 = 1, wq−1 = 1
(w ̸= 01q−1) 1w 0q1q (m)k 1w 0q1q (m + i)k 1w 0q−110q ω(i)

w1 = 1, wq−1 = 0 1w1q01q(m)k 1w1q01q(m + i)k 1w1q10q ω(i)

Table 3. k = 2 and w = 0w1 · · · wq−1.

When k = 2, the integer m′ are chosen according to the diﬀerent forms of the word
w; see Table 3. We remark that 1 ⊳ (m)k when k = 2. Then one can see from Table 3
that for every w = 0w1 · · · wq−1, |(m′ + i)k|w = 1 + |(m + i)k|w for all 0 ≤ i ≤ n − 1.
Thus (4.2) holds. □

To prove the ‘if’ part of Proposition 4.4, we need the following auxillary result.

Lemma 4.6. Suppose that (k, w) ̸= (2, 1). Let m and n be positive integers. Let x be the longest
common preﬁx of (m)k, (m + 1)k, . . . , (m + n − 1)k. If w ≺ x, then there exists m′ such that

s[m′, m′ + n − 1] = s[m, m + n − 1] − 1. (4.4)

Proof. Recall that w = w0w1 . . . wq−1 ∈ Σq
k. Assume x = x0x1 . . . xp and for i = 0, 1, . . . , n − 1,
write (m + i)k = x u
(i), where u
(i) ∈ Σ∗
k. The condition implies implicitly that
[u
(0)]
k + (n − 1) ≤ k|u
(0)| − 1. (4.5)

Let j0 = min{0 ≤ j ≤ p − q : x[j, j + q − 1] = w}.

Then xj0 = w0. When k > 2, we can choose x
′
j0 ∈ Σk such that x
′
j0 ̸= 0 and x
′
j0 ̸= w0. (This is
feasible when k > 2, and the restriction x
′
j0 ̸= 0 ensures that the result holds for j0 = 0.) Let

x
′ = x
′
j0 xj0+1 . . . xp

and m′ = [x′u(0)]k. By (4.5), we have (m′ + i)k = x
′u(i). It follows that for all 0 ≤ i ≤ n − 1,

s(m′ + i) = s(m + i) − 1.

In the following, we suppose that k = 2.
• In this case, if w0 = 0, then we choose x
′ = 1xj0+1 . . . xp. Consequently, m′ = [x′u
(0)]k
satisﬁes (4.4).

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 12

• If w0 = 1, then by out assumption, |w| ≥ 2. If |x|1 = 1, then for all i = 0, 1, . . . , n − 1,
|x u(i)|w = |x|w + |u
(i)|w = 1 + |u(i)|w. It follows that m′ = [
u(i)]
k satisﬁes (4.4). If
|x|1 ≥ 2, then let j1 = min{j0 + 1 ≤ j ≤ p : xj = 1} be the index of second 1 in x. Let
x
′ = xj1 xj1+1 . . . xp. We have m′ = [
x′u(0)]

k satisﬁes (4.4). We are done. □

Now we prove the ‘if’ part of Proposition 4.4.

Lemma 4.7. Suppose that (k, w) ̸= (2, 1). Let n ≥ 1 and u ∈ Nn. Then for all N ≥ ⌈logk n⌉+ 1,
we have u ∈ F (1)
s (n, N ) if u + 1 ∈ F (1)
s (n, N + 1).

Proof. If u + 1 ∈ F (1)
s (n, N + 1), then there exists an m such that

u + 1 = s(m)s(m + 1) · · · s(m + n − 1)

and 1 ≤ s(m + i) ≤ N + 1 for all 0 ≤ i ≤ n − 1. Namely, |(m + i)k|w ≥ 1 for all 0 ≤ i ≤ n − 1.
Moreover, we can assume that ℓ = |(m)k| ≥ N . Consequently, n ≤ kN −1 ≤ kℓ−1 ≤ m < kℓ.
If m + n − 1 ≥ kℓ, then there exists 0 ≤ a ≤ n − 1 such that m + a = kℓ and m + a − 1 = kℓ − 1.
That is (m + a)k = 10ℓ and (m + a − 1)k = (k − 1)
ℓ. Noting that |(m + a)k|w ≥ 1 and
|(m + a − 1)k|w ≥ 1, we have k = 2 and w = 1 which is out of the scope of the result.
In the following, we assume that m + n − 1 < kℓ. Let x be the longest common preﬁx of (m)k,
(m + 1)k, . . . , (m + n − 1)k. (It is possible that x = ε.) Now, if we can show that w ≺ x, then
the result follows from Lemma 4.6.
Let p = ℓ − |x| − 1. Then there exists 1 ≤ a ≤ n − 1 such that
{(m + a − 1)k = x b (k − 1)
p,

(m + a)k = x (b + 1) 0p, (4.6)

where b ∈ Σk−1. In fact, if such a does not exist, then (m)k, (m + 1)k, . . . , (m + n − 1)k
diﬀer only in the last digit, which implies w ≺ x. Further, if w ̸≺ x, noting that p ≥ N and
0 ≤ a ≤ n − 1 ≤ kN −1 − 1 ≤ kp−1 − 1, the number b that satisﬁes (4.6) is unique and so is a.
Recall that F (1)
s (n, N + 1) = Fs(n, N + 1)\Fs(n, N ). Then u + 1 ∈ F (1)
s (n, N + 1) implies that

s(m + t) = |(m + t)k|w = N + 1 (4.7)

for some 0 ≤ t ≤ n − 1. There are two sub-cases: t ≥ a and t ≤ a − 1.
• Case 1: t ≥ a. For a ≤ i ≤ n − 1, write α
(i) = (i − a)k. By (4.6) and the uniqueness of
b, we have (m + i)k = x (b + 1) 0p−|α
(i)|α
(i), (4.8)
where |α
(i)| ≤ N − 1 since i − a < n ≤ kN −1.
– If w ̸= 0q, then for some a ≤ t ≤ n − 1 satisfying (4.7), it holds that
∣
∣x (b + 1) 0p−|α
(t)|∣
∣w ≤ |x|w + 1. (4.9)

Further, since |α
(t)| ≤ N − 1, we have

|(m + t)k|w = ∣
∣x (b + 1) 0p−|α
(t)| α
(t)∣
∣w ≤ ∣
∣x (b + 1) 0p−|α
(t)|∣
∣w + N − 1. (4.10)

Combining (4.7), (4.9) and (4.10), it follows that |x|w ≥ 1.
– If w = 0q, then by (4.6) and (4.8), we have

|(m + a)k|0q ≥ |(m + t)k|0q = N + 1

which implies |(m + a)k|0q = N + 1. If 0q ≺ x, then we are done. If 0q ̸≺ x, then
N + 1 = |(m + a)k|0q = |x (b + 1) 0p|0q = |0p|0q . So, p = q + N and for a ≤ i ≤ n − 1,

p − |α
(i)| = q + N − |α(i)| ≥ q + 1.

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 13

Combing the facts that 1 ≤ |(m + a − 1)k|0q = |x b (k − 1)
p|0q and 0q ̸≺ x, we have
b = 0 and |x b|0q = 1. Now (4.6) yields that

(m + a − 1)k = x 0 (k − 1)
q+1 (k − 1)
N −1,

(m + a)k = x 1 0q+1 0N −1.

Since i ≤ n − 1 < kN −1, we have

(m + i)k =
 {x 0 (k − 1)
q+1 β(i), if 0 ≤ i ≤ a − 1,
x 1 0q+1 β(i), if a ≤ i ≤ n − 1, (4.11)

where β(i) ∈ ΣN −1
k . Now let m′ be the integer such that

(m′)k = (k − 1)
q β(0).

Then
 (m′ + i)k =
 {(k − 1)
q β(i), if 0 ≤ i ≤ a − 1,
1 0q β(i), if a ≤ i ≤ n − 1. (4.12)

Combing (4.11) and (4.12), we have

|(m + i)k|0q =
 {|x 0|0q + |β(i)|0q = |(m′ + i)k|0q + 1, if 0 ≤ i ≤ a − 1,
∣
∣0q+1 β(i)∣
∣
0q = |(m′ + i)k|0q + 1, if a ≤ i ≤ n − 1.

• Case 2: t ≤ a − 1. By the uniqueness of b, for 0 ≤ i ≤ a − 1 we have

(m + i)k = x b (k − 1)
p−|γ(i)|γ(i), (4.13)

where (k − 1) ̸⊳ γ(i), and thus |γ(i)| ≤ N − 1 since i < n ≤ kN −1.
– If w ̸= (k − 1)
q, then for some 0 ≤ t ≤ a − 1 satisfying (4.7), it holds that
∣
∣x b (k − 1)
p−|γ(t)|∣
∣
w ≤ |x|w + 1. (4.14)

Further, since |γ(t)| ≤ N − 1, we have

|(m + t)k|w = ∣
∣x b (k − 1)
p−|γ(t)| γ(t)∣
∣w ≤ ∣
∣x b (k − 1)
p−|γ(t)|∣
∣w + N − 1. (4.15)

Combining (4.7), (4.14) and (4.15), it follows that |x|w ≥ 1.
– If w = (k − 1)
q, then by (4.6) and (4.13), we have

|(m + a − 1)k|(k−1)q ≥ |(m + t)k|(k−1)q = N + 1

which implies |(m + a − 1)k|(k−1)q = N + 1. If (k − 1)
q ≺ x, then we are done. If
(k−1)
q ̸≺ x, then N +1 = |(m+a−1)k|(k−1)q = |x b (k−1)
p|(k−1)q = |(k−1)
p|(k−1)q .
So, p = q + N and for a ≤ i ≤ n − 1,

p − |γ(i)| = q + N − |γ(i)| ≥ q + 1.

Combing the facts that 1 ≤ |(m + a)k|(k−1)q = |x (b + 1) 0p|(k−1)q and (k − 1)
q ̸≺ x,
we have b = k − 2 and |x (b + 1)|(k−1)q = 1. Now (4.6) yields that

(m + a − 1)k = x (k − 2) (k − 1)
q+1 (k − 1)
N −1,

(m + a)k = x (k − 1) 0q+1 0N −1.

Since i ≤ n − 1 < kN −1, we have

(m + i)k =
 {x (k − 2) (k − 1)
q+1 β(i), if 0 ≤ i ≤ a − 1,
x (k − 1) 0q+1 β(i), if a ≤ i ≤ n − 1, (4.16)

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 14

where β(i) ∈ ΣN −1
k . Now let m′ be the integer such that

(m′)k = (k − 1)
q β(0).

Then
 (m′ + i)k =
 {(k − 1)
q β(i), if 0 ≤ i ≤ a − 1,
1 0q β(i), if a ≤ i ≤ n − 1. (4.17)

Combing (4.16) and (4.17), since (k, w) ̸= (2, 1), then the extra 1 in 1 0q β(i) has no
eﬀect on the value of |(m′ + i)k|(k−1)q . Hence,

|(m + i)k|(k−1)q =
 {∣
∣(k − 1)
q+1 β(i)∣
∣(k−1)q , if 0 ≤ i ≤ a − 1,

|x (k − 1)|(k−1)q + |β(i)|(k−1)q , if a ≤ i ≤ n − 1,

=
 {|(m′ + i)k|(k−1)q + 1, if 0 ≤ i ≤ a − 1,
|(m′ + i)k|(k−1)q + 1, if a ≤ i ≤ n − 1. □

4.2.1. The case (k, w) ̸= (2, 1) and w = 0q or (k − 1)
q. In this case, we can easily obtain Ps(1, N )
by ﬁnding integers m such that s(m) = |(m)k|w = i for any 1 ≤ i ≤ N . For example, we could
choose (m)k = 10q+i−1 or (k − 1)
q+i−1. Since s(0) = 0, then

Ps(1, N ) = N + 1. (4.18)

In the following we assume that n ≥ 2. As deﬁned in Section 2,

P (2)
s (n, N ) = P (1)
s (n, N ) − P (1)
s (n, N − 1) = ♯F (1)
s (n, N ) − ♯F (1)
s (n, N − 1).

By Proposition 4.4, we have

P (2)
s (n, N ) = ♯{u ∈ F (1)
s (n, N ) : 0 ≺ u} =: ♯G.

Namely, in order to calculate P (2)
s (n, N ), we shall ﬁnd all u ∈ Fs(n, N ) with 0 ≺ u and N ≺ u.
Note that there are inﬁnitely many m with s(m) = 0 and s(m + 1) ≥ 1. For instance, if
w = 0q (q ≥ 1), we have s(kℓ − 1) = 0 and s(kℓ) ≥ 1 for all ℓ ≥ q. Let

N = {m ≥ 0 : s(m) = 0, s(m + 1) ≥ 1}

and write its elements in ascending order, i.e. m1 < m2 < m3 < · · · .
We ﬁrst discuss the case w = 0q.

Lemma 4.8. Let w = 0q, N ≥ 0 and n ≤ kN −2. For all m > 0 satisfying s(m + 1) ≥ N , we
have s(m + i) > 0 for all 1 ≤ i ≤ n.

Proof. Suppose s(m + 1) = N and write (m + 1)k = x w z, where |x w|w = 1 (i.e. ﬁnd the
leftmost w in (m + 1)k). Suppose |z| = λ. Since |x w z|0q = N , we see that |z|0 ≥ N − 1 and
thus [x w z]k ≤ [x w (k − 1)
λ−N +1 0N −1]k. As a result, for 1 ≤ i ≤ n we have

[x w z]k ≤ m + i ≤ m + n ≤ m + kN −2 = [x w z]k + [1 0N −2]k ≤ [x w (k − 1)
λ−N +1 1 0N −2]k,

which implies x w ⊳ (m + i)k and s(m + i) > 0. On the other hand, if s(m + 1) = N ′ > N , then
n ≤ kN ′−2. For the same reason, we have s(m + i) > 0 for 1 ≤ i ≤ n. □

Lemma 4.9. If w = 0q, then for all mi + 2 ≤ m ≤ mi+1, we have s(mi + 1) > s(m).

Proof. Since s(mi) = 0 and s(mi + 1) ≥ 1, we have

(mi)k = (k − 1)
p, (mi + 1)k = 10p

or (mi)k = x b (k − 1)
p, (mi + 1)k = x (b + 1) 0p

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 15

where p ≥ q, b ∈ Σk−1, x ∈ Σ∗
k and 0q ̸≺ x b. Let t = [1 0p]k. Then

(mi + t)k = 1 (k − 1)
p or x (b + 1) (k − 1)
p.

Note that |(mi + 1)k|0q > |(m)k|0q for all mi + 2 ≤ m ≤ mi + t. Moreover, since 0q ̸≺ x b,
then 0q ̸≺ x (b + 1) and s(mi + t) = 0. Combining with the fact that s(mi + t + 1) > 0,
we have mi + t ∈ N and thus mi+1 ≤ mi + t, which implies s(mi + 1) > s(m) holds for all
mi + 2 ≤ m ≤ mi+1. □

Proposition 4.10. Let n ≥ 2 and w = 0q (q ≥ 1). Then for all N ≥ ⌈logk(n)⌉ + 2, we have
P (2)
s (n, N ) = n − 1.

Proof. Recall that P (2)
s (n, N ) = ♯G. For i ≥ 1, deﬁne

Gi = {s[h − n + 1, h] : mi < h ≤ mi+1, h − n + 1 ≥ 0, s[h − n + 1, h] ∈ G},

and write G0 = {s[h − n + 1, h] : h ≤ m1, h − n + 1 ≥ 0, s[h − n + 1, h] ∈ G}.

Then G = ∪i≥0Gi. By the deﬁnition of N , it follows that s(m) = 0 for 0 ≤ m ≤ m1 and hence
G0 ⊂ {0n}. However, combining with the deﬁnition of G, we see that 0n /∈ G and namely G0 = ∅.
Therefore, all we have to do is to ﬁnd the elements in ∪i≥1Gi.

. . . s(mi) s(mi + 1) s(mi + 2) . . . s(mi+1 − 1) s(mi+1) s(mi+1 + 1) . . .

0 ≥ 1 ∈ {0, 1, . . . , s(mi + 1) − 1} 0 ≥ 1

• Case 1: s(mi + 1) < N . If mi + 1 ≤ h ≤ min{mi + n − 1, mi+1}, then h − n + 1 ≤ mi.
Then Lemma 4.8 yields s(j) < N for h − n + 1 ≤ j ≤ mi, and Lemma 4.9 yields s(j) < N
for mi + 1 ≤ j ≤ h. Thus s[h − n + 1, h] /∈ Gi. Moreover, if mi + n ≤ h ≤ mi+1, the same
result can be obtained directly by Lemma 4.9. As a result, Gi = ∅.
• Case 2: s(mi + 1) > N . Since s(mi+1) = 0, it follows from Lemma 4.8 that mi + n ≤
mi+1. If mi+1 ≤ h ≤ mi+n, then s(mi+1) ≺ s[h−n+1, h], which implies s[h−n+1, h] /∈
Gi. Now consider mi + n + 1 ≤ h ≤ mi+1. If there does not exists 0 ≺ s[h − n + 1, h],
then s[h − n + 1, h] /∈ Gi. Otherwise, if there is an h′ with h − n + 1 ≤ h′ ≤ h such that
s(h′) = 0, then by the deﬁnition of mi we have s(j) = 0 for all h′ ≤ j ≤ h. However,
Lemma 4.8 implies that s(j) < N for all h − n + 1 ≤ j ≤ h′. Hence, we obtain that
Gi = ∅.
• Case 3: s(mi + 1) = N . Similarly, we have mi + n ≤ mi+1. Combining Lemma 4.9 and
Lemma 4.8, {
N ̸≺ s[h − n + 1, h], if mi + n + 1 ≤ h ≤ mi+1,
0 ̸≺ s[h − n + 1, h], if h = mi + n.

If mi + 1 ≤ h ≤ mi + n − 1, then




s(m) < N, if h − n + 1 ≤ m ≤ mi − 1,
s(m) = 0, if m = mi,
s(m) = N, if m = mi + 1,
s(m) < N, if mi + 2 ≤ m ≤ h.

Therefore, s[h − n + 1, h] ∈ Gi. Since N is unique in s[h − n + 1, h], then diﬀerent h must
yield diﬀerent subword, which implies ♯Gi = n − 1 (Note that s(mi + 1) = N ensures
mi + 1 ≥ kN −1 and thus h − n + 1 ≥ mi − kN −2 + 2 > 0).

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 16

Next, for any i and i′ with ♯Gi = ♯Gi′ = n − 1, we shall show that Gi = Gi′ . From the above
discussion, we see that
 (mi)k = (k − 1)
q+N −1 or x b (k − 1)
q+N −1,

(mi′ )k = (k − 1)
q+N −1 or y b′ (k − 1)
q+N −1,

where x, y ∈ Σ∗
k, b, b′ ∈ Σk−1, 0q ̸≺ xb and 0q ̸≺ yb′. Then s(mi ± j) = s(mi′ ± j) for all
0 ≤ j ≤ n − 1. This means s[mi + j − n + 1, mi + j] = s[mi′ + j − n + 1, mi′ + j] for all
1 ≤ j ≤ n − 1. Therefore, Gi = Gi′ . Finally, we conclude that G = Gi for some i ≥ 0 with Gi ̸= ∅
and ♯G = n − 1. □

Now we consider the case w = (k − 1)
q. There are also inﬁnitely many m with s(m) ≥ 1 and
s(m + 1) = 0. Deﬁne N ′ = {m ≥ 0 : s(m) ≥ 1, s(m + 1) = 0}
and write its elements in ascending order, i.e. m1 < m2 < m3 < · · · .

Lemma 4.11. Let w = (k − 1)
q, N ≥ 0 and n ≤ kN −2. For all m > 0 satisfying s(m) ≥ N , we
have s(m − i) > 0 for 0 ≤ i ≤ n − 1.

Proof. Suppose s(m) = N and write (m)k = x w z, where |x w|w = 1 (i.e. ﬁnd the leftmost
w in (m)k). Suppose |z| = λ. Since |x w z|(k−1)q = N , we see that |z|k−1 ≥ N − 1 and thus
[x w z]k ≥ [x w 0λ−N +1 (k − 1)
N −1]k. As a result, for 0 ≤ i ≤ n − 1 we have

[x w z]k ≥ m−i ≥ m−n+1 ≥ m−kN −2 = [x w z]k −[1 0N −2]k ≥ [x w 0λ−N +1 (k−2) (k−1)
N −2]k,

which implies x w ⊳ (m − i)k and s(m − i) > 0. Moreover, if s(m) = N ′ > N , it also holds that
n ≤ kN ′−2. Then for the same reason, we have s(m − i) > 0 for 0 ≤ i ≤ n − 1. □

Lemma 4.12. If w = (k − 1)
q, then for all mi−1 + 1 ≤ m ≤ mi − 1, we have s(mi) > s(m).

Proof. Since s(mi) ≥ 1 and s(mi + 1) = 0, we have

(mi)k = (k − 1)
p, (mi + 1)k = 10p

or (mi)k = x b (k − 1)
p, (mi + 1)k = x (b + 1) 0p

where p ≥ q, b ∈ Σk−1, x ∈ Σ∗
k and (k − 1)
q ̸≺ x (b + 1). If (mi)k = (k − 1)
p, it is clear that
|(mi)k|(k−1)q > |(m)k|(k−1)q holds for all 0 ≤ m ≤ mi − 1, and the desired result follows.
In the other case, let t = [(k − 1)
p]k. Then (mi − t)k = x b 0p. Note that |(mi)k|(k−1)q >
|(m)k|(k−1)q for all mi − t ≤ m ≤ mi − 1. Moreover, since (k − 1)
q ̸≺ x (b + 1), then (k − 1)
q ̸≺ x b
and s(mi − t) = 0. Combining with the fact that s(mi − t − 1) > 0, we have mi − t − 1 ∈ N ′ and
thus mi−1 ≥ mi − t − 1, which implies s(mi) > s(m) holds for all mi−1 + 1 ≤ m ≤ mi − 1. □

Proposition 4.13. Let n ≥ 2, w = (k − 1)
q (q ≥ 1) and (k, w) ̸= (2, 1). Then for all N ≥
⌈logk(n)⌉ + 2, we have P (2)
s (n, N ) = n − 1.

Proof. Let G′
i = {s[h, h + n − 1] : mi−1 < h ≤ mi, s[h, h + n − 1] ∈ G}
for i ≥ 1, and G′
0 = {s[h, h + n − 1] : 0 ≤ h ≤ m1, s[h, h + n − 1] ∈ G}.
Hence, G = ∪i≥0G′
i. By the deﬁnition of N ′, we have s(h) = 0 for 0 ≤ h ≤ m1. Combining with
Lemma 4.11, however, we see that N ̸≺ s[h, h + n − 1] and thus s[h, h + n − 1] /∈ G′
0. Therefore,
all we have to do is to ﬁnd the elements in ∪i≥1G′
i.

. . . s(mi−1) s(mi−1 + 1) s(mi−1 + 2) . . . s(mi − 1) s(mi) s(mi + 1) . . .

≥ 1 0 ∈ {0, 1, . . . , s(mi) − 1} ≥ 1 0

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 17

• Case 1: s(mi) < N . If max{mi − n + 2, mi−1 + 1} ≤ h ≤ mi, then h + n − 1 ≥ mi + 1.
Then Lemma 4.11 yields s(j) < N for mi + 1 ≤ j ≤ h + n − 1, and Lemma 4.12 yields
s(j) < N for h ≤ j ≤ mi. Thus s[h, h+n−1] /∈ G′
i. Moreover, if mi−1+1 ≤ h ≤ mi−n+1,
the same result can be obtained directly by Lemma 4.12. As a result, G′
i = ∅.
• Case 2: s(mi) > N . Since s(mi−1 + 1) = 0, it follows from Lemma 4.11 that mi−1 + 1 ≤
mi −n. If mi −n+1 ≤ h ≤ mi, then s(mi) ≺ s[h, h+n−1], which implies s[h, h+n−1] /∈
G′
i. Now consider mi−1 + 1 ≤ h ≤ mi − n. If there does not exists 0 ≺ s[h, h + n − 1],
then s[h, h + n − 1] /∈ G′
i. Otherwise, if there is an h′ with h ≤ h′ ≤ h + n − 1 such that
s(h′) = 0, then by the deﬁnition of mi, we have s(j) = 0 for all h ≤ j ≤ h′. However,
Lemma 4.11 implies that s(j) < N for all h′ ≤ j ≤ h + n − 1. Hence, we obtain that
G′
i = ∅.
• Case 3: s(mi) = N . Similarly, we have mi−1 + 1 ≤ mi − n. Combining Lemma 4.12
and Lemma 4.11,
{
N ̸≺ s[h, h + n − 1], if mi−1 + 1 ≤ h ≤ mi − n − 1,
0 ̸≺ s[h, h + n − 1], if h = mi − n.

If mi − n + 1 ≤ h ≤ mi, then




s(m) < N, if h ≤ m ≤ mi − 1,
s(m) = N, if m = mi,
s(m) = 0, if m = mi + 1,
s(m) < N, if mi + 2 ≤ m ≤ h + n − 1.

Therefore, s[h, h + n − 1] ∈ G′
i. Since N is unique in s[h, h + n − 1], then diﬀerent h must
yield diﬀerent subword, which implies ♯G′
i = n − 1.
Next, for any i and i′ with ♯G′
i = ♯G′
i′ = n − 1, we shall show that G′
i = G′
i′ . From the above
discussion, we see that
 (mi)k = (k − 1)
q+N −1 or x b (k − 1)
q+N −1,

(mi′ )k = (k − 1)
q+N −1 or y b′ (k − 1)
q+N −1,

where x, y ∈ Σ∗
k, b, b′ ∈ Σk−1, 0q ̸≺ xb and 0q ̸≺ yb′. Then s(mi ± j) = s(mi′ ± j) for all
0 ≤ j ≤ n − 1. This means s[mi + j − n + 1, mi + j] = s[mi′ + j − n + 1, mi′ + j] for all
1 ≤ j ≤ n − 1. Therefore, G′
i = G′
i′ . Finally, we conclude that G = G′
i for some i ≥ 0 with G′
i ̸= ∅
and ♯G = n − 1. □

We summarize the cases w = 0q and (k − 1)
q in the following result.

Proposition 4.14. Let n ≥ 1 and w ∈ Σ∗
k\{ε}. If w ∈ {0}∗ ∪ {k − 1}∗ and (k, w) ̸= (2, 1), then
for all N ≥ ⌈logk(n)⌉ + 2, we have P (2)
s (n, N ) = n − 1.

Proof. If n = 1, as mentioned in (4.18) at the beginning of section 4.2.1, we see that Ps(1, N ) =
N + 1. Thus P (1)
s (1, N ) = 1 and P (2)
s (1, N ) = 0. Combining with Proposition 4.10 and Proposi-
tion 4.13, we are done. □

4.2.2. The case (k, w) ̸= (2, 1) and w /∈ {0}∗ ∪ {k − 1}∗. In this case, we ﬁrst prove a balance
property (Lemma 4.15) for s which indicates that the diﬀerence sequence of s taking values in
{0, ±1}. Then by using this balance property, we show that P (1)
s (n, N ) does not depend on N ;
see Proposition 4.18. Consequently, we give the precise value of P (2)
s (n, N ) in Theorem 4.1.

Lemma 4.15. Let w ∈ Σ∗
k\{ε}. If w /∈ {0}∗ ∪{k −1}∗, then for all m ≥ 0, |s(m)−s(m+1)| ≤ 1.

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 18

Proof. If m = kℓ − 1 for some integer ℓ ≥ 0, then (m)k = (k − 1)
ℓ and (m + 1)k = 10ℓ. We have
s(m) = |(m)k|w = 0 and s(m + 1) = |(m + 1)k|w ≤ 1. The result follows.
If m ̸= kℓ − 1 for all ℓ ≥ 0, then we have

(m)k = x b (k − 1)
p, (m + 1)k = x (b + 1) 0p

where x ∈ Σ∗
k, p ≥ 0 and b ∈ Σk−1. When p = 0, it is easy to see that |s(m) − s(m + 1)| ≤ 1.
When p ≥ 1, since w /∈ {0}∗ ∪ {k − 1}∗, we have

|x|w ≤ s(m) ≤ |x|w + 1 and |x|w ≤ s(m + 1) ≤ |x|w + 1.

If s(m) = |x|w + 1, then b (k − 1)
t ⊲ w for some t ≥ 0, which implies s(m + 1) = |x|w. If
s(m + 1) = |x|w + 1, then (b + 1) 0r ⊲ w for some r ≥ 0, which implies s(m) = |x|w. In either
case, we have |s(m) − s(m + 1)| ≤ 1. □

Remark 4.16. When w ∈ {0}∗ ∪ {k − 1}∗, Lemma 4.15 does not hold. In fact, when w =
0j (j ≥ 1), we have s(kj+ℓ) − s(kj+ℓ − 1) = ℓ for all ℓ ≥ 1; when w = (k − 1)
j, we have
s(kj+ℓ − 1) − s(kj+ℓ) = ℓ for all ℓ ≥ 1.

Before calculating P (1)
s (n, N ), we give an auxillary lemma.

Lemma 4.17. Let α ∈ Σ∗
k\{ε}, w ∈ Σ∗
k\{ε} and w /∈ {0}∗ ∪{k −1}∗. Suppose that |α|w = r > 0.
Write α = x w z with |x w|w = 1. Then |z|0 ≤ |z| − r + 1 and |z|k−1 ≤ |z| − r + 1.

Proof. Write α = α0α1 . . . αℓ−1 and A = {0 ≤ i ≤ ℓ − 1 : αi > 0}
. For any w = w0w1 . . . wq−1 /∈
{0}∗, there exists j ≥ 0 such that wj > 0. Hence α[t, t + q − 1] = w only if t + j ∈ A. As a result,

r = |α|w ≤ |x w|w + |z|wj ≤ 1 + |z| − |z|0.

Therefore, |z|0 ≤ |z| − r + 1. Similarly, for w /∈ {k − 1}∗, we have |z|k−1 ≤ |z| − r + 1 as well. □

Proposition 4.18. Fix n ≥ 1 and w ∈ Σ∗
k\{ε}. If w /∈ {0}∗ ∪ {k − 1}∗, then for all N ≥
⌈logk(n)⌉ + 2, we have P (1)
s (n, N ) = P (1)
s (n, ⌈logk(n)⌉ + 1) ≥ 1.

Proof. Recall that P (1)
s (n, N ) = ♯F (1)
s (n, N ). For every u ∈ F (1)
s (n, N ), we have N ≺ u and
u = s(m)s(m + 1) · · · s(m + n − 1) for some m ≥ 0. Suppose s(m + t) = N where 0 ≤ t ≤ n − 1.
Write (m + t)k = x w z such that |x w|w = 1. It follows from Lemma 4.17 that |z|0 ≤ |z| − N + 1
and |z|k−1 ≤ |z| − N + 1. Then

[x w 0|z|−N +1 1N −1]k ≤ m + t ≤ [x w (k − 1)
|z|−N +1 (k − 2)
N −1]k.

Since 0 ≤ t ≤ n − 1 and 1 ≤ n ≤ N k−2, for 0 ≤ i ≤ n − 1 we have

[x w 0|z|]k ≤ m + i ≤ [x w (k − 1)
|z|]k,

which implies x w ≺ (m + i)k and namely s(m + i) ≥ 1. Then applying Proposition 4.4, we
obtain that for all N ≥ ⌈logk(n)⌉ + 2,

P (1)
s (n, N ) = P (1)
s (n, N − 1).

Thus P (1)
s (n, N ) = P (1)
s (n, ⌈logk(n)⌉ + 1).
Finally, letting m′ = [(w)
N ]k, we see that s(m′) = |(m′)k|w ≥ N . Note that n ≤ kN −1 and
s(j) < N for j = 0, 1, · · · , n. By Lemma 4.15, there exists n ≤ t ≤ m′ such that s(t) = N and
s(j) < N for all j < t. Thus s[t − n + 1, t] ∈ F (1)
s (n, N ) and P (1)
s (n, N ) ≥ 1. □

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 19

Proof of Theorem 1.8 and 4.1.

Proof of Theorem 4.1. The result follows from Proposition 4.3, Proposition 4.14 and Proposition
4.18. □

Proof of Theorem 1.8. Combing the deﬁnitions (2.1), (2.2) and Theorem 4.1, the result holds.
□

4.3. Duality of F (1)
sk,w (n, N ). Let u = u0u1 · · · ul−1 ∈ Σl
k. The conjugate of u is deﬁned as

conj(u) = (k − 1 − u0)(k − 1 − u1) · · · (k − 1 − ul−1).

We call F (1)
sk,conj(w) (n, N ) the dual of F (1)
sk,w (n, N ). We show that for w /∈ {0}∗ ∪ {k − 1}∗,

F (1)
sk,conj(w) (n, N ) = {mirr(u) : u ∈ F (1)
sk,w (n, N )}

where N ≥ ⌈log2(n)⌉ + 2 and mirr(u) = ul−1ul−2 · · · u0 is the mirror of u; see Proposition 4.20.
This implies that for all w /∈ {0}∗ ∪ {k − 1}∗ and N ≥ ⌈log2(n)⌉ + 2,

P (1)
sk,conj(w)(n, N ) = P (1)
sk,w (n, N ).

Lemma 4.19. Let u, v ∈ Σl
k, a ∈ Σ∗
k. Then [u]k − [v]k = [a conj(v)]k − [a conj(u)]k.

Proof. Let u = u0u1 · · · ul. Note that

[a conj(u)]k = [a]kkl +
 l−1∑

i=0(k − 1 − ui)kl−1−i = [a]kkl + (k − 1)(kl − 1) − [u]k.

So [u]k − [v]k = ∑l−1
i=0 ki(ul−1−i − vl−1−i) = [a conj(v)]k − [a conj(u)]k. □

Proposition 4.20. Suppose n ≥ 1 and N ≥ ⌈logk(n)⌉ + 2. Let u ∈ Σn
N +1, w ∈ Σq
k and

w /∈ {0}∗ ∪ {k − 1}∗. Then u ∈ F (1)
sk,w (n, N ) if and only if mirr(u) ∈ F (1)
sk,conj(w)(n, N ).

Proof. Let u ∈ F (1)
sk,w (n, N ) and write u = sk,w(m) · · · sk,w(m + n − 1). Then there exists
0 ≤ i ≤ n − 1 such that |(m + i)k|w = N . Since w /∈ {0}∗ ∪ {k − 1}∗, letting ℓ = |(m + i)k|, it
follows that |(m + i)k|0 ≤ ℓ − N and |(m + i)k|k−1 ≤ ℓ − N.

Hence, [1 0ℓ−N 1N −1]k ≤ m + i ≤ [(k − 1)
ℓ−N (k − 2)
N ]k.

Noting that n ≤ kN −2, for any 0 ≤ j ≤ n − 1 we have

[1 0ℓ−1]k ≤ m + i − n + 1 ≤ m + j ≤ m + i + n − 1 ≤ [(k − 1)
ℓ],

which implies |(m + j)k| = ℓ. (4.19)

In order to show mirr(u) ∈ F (1)
sk,conj(w) (n, N ), we shall ﬁnd an m′ such that for all 0 ≤ j ≤ n− 1,

|(m′ + j)k|conj(w) = |(m + n − 1 − j)k|w.

Let w = w0w1 · · · wq−1. If k ≥ 3, we can select a ∈ Σk such that a ̸= 0 and a ̸= k − 1 − w0. If
k = 2, then we choose
 a =
 



1, if conj(w0) = 0,
11, if conj(w0w1) = 10,
10, if conj(w0w1) = 11.

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 20

Letting (m′)k = a conj (
(m + n − 1)k)
, it follows from (4.19) that for all 0 ≤ j ≤ n − 1,
|(m + n − 1 − j)k| = ℓ and ∣
∣ conj (
(m + n − 1 − j)k)∣
∣ = ℓ. By Lemma 4.19,
[
a conj (
(m + n − 1 − j)k)]

k − m′ = [a conj (
(m + n − 1 − j)k)]
k − [a conj (
(m + n − 1)k)]

k
= [(m + n − 1)k]k − [(m + n − 1 − j)k]k = j

which implies that (m′ + j)k = a conj (
(m + n − 1 − j)k)
. Therefore,

|(m′ + j)k|conj(w) = ∣
∣a conj (
(m + n − 1 − j)k)∣
∣conj(w)
= ∣
∣ conj (
(m + n − 1 − j)k)∣
∣conj(w)
= ∣
∣(m + n − 1 − j)k∣
∣
w.

Thus mirr(u) = sk,w(m′) · · · sk,w(m′ + n − 1) ∈ F (1)
sk,conj(w) (n, N ).
Noting that conj(conj(u)) = u and mirr(mirr(w)) = w, the proof is completed. □

Remark 4.21. Given w /∈ {0}∗ ∪ {k − 1}∗, as shown in Theorem 1.8, we have P (1)
sk,w (n, N ) =
d0(k, w, n) for any N ≥ ⌈logk(n)⌉ + 2.

Acknowledgement

This work was supported by Guangdong Basic and Applied Basic Research Foundation (No.
2021A1515010056) and Guangzhou Science and Technology program (No. 202102020294).

References

[1] J.-P. Allouche, M. Baake, J. Cassaigne, D. Damanik, Palindrome complexity, Theoret. Comput. Sci., 292
(2003) 9-31.
[2] J.-P. Allouche, J. Shallit, Automatic Sequences Theory, Applications, Generalizations, Cambridge University
Press, 2003.
[3] P. Bal´aˇzi, Z. Mas´akov´a, E. Pelantov´a, Factor versus palindromic complexity of uniformly recurrent inﬁnite
words, Theoret. Comput. Sci., 380 (2007) 266-275.
[4] J. Cassaigne, Double sequences with complexity mn + 1, J. Autom. Lang. Comb., 4 (1999) 153-170.
[5] J. Cassaigne, S. Labb´e, J. Leroy, A set of sequences of complexity 2n + 1, in: Brlek, S., Dolce, F., Reutenauer,
C., Vandomme, ´E. (eds) Combinatorics on Words. WORDS 2017. Lecture Notes in Computer Science, vol
10432. Springer.
[6] J. Cassaigne, S. Labb´e, J. Leroy, Almost everywhere balanced sequences of complexity 2n+1, Mosc. J. Comb.
Number Theory, 11 (2022) 287-333.
[7] T. Kamae, H. Rao, Y.-M. Xue, Maximal pattern complexity of two-dimensional words, Theoret. Comput.
Sci., 359 (2006) 15-27.
[8] M. A. Makarov, On the permutations generated by the Sturmain words. Sib. Math. J., 50 (2009) 674-680.
[9] M. Morse, G. A. Hedlund, Symbolic dynamics, Amer. J. Math. 60 (1938) 815-866.
[10] M. Morse, G. A. Hedlund, Symbolic dynamics II. Sturmian trajectories, Amer. J. Math. 62 (1940) 1-42.
[11] G. Richomme, K. Saari, L. Q. Zamboni, Balance and abelian complexity of the Tribonacci word, Adv. Appl.
Math., 45 (2010) 212-231.
[12] G. Richomme, K. Saari, L. Q. Zamboni, Abelian complexity of minimal subshifts, J. London Math. Soc., 83
(2011) 79-95.
[13] G. Rote, Sequences with subword complexity 2n, J. Number Theory, 46 (1994) 196-213.
[14] B. Tan, Z.-X. Wen, Y. Zhang, On the triplex substitution combinatorial properties, Comptes Rendus Math.,
346 (2008) 813-818.
[15] S. Widmer, Permutation complexity of the Thue-Morse word, Adv. Appl. Math., 47 (2011) 309-329.
[16] J.-M. Zhang, Z.-X. Wen, W. Wu, Some properties of the Fibonacci sequence on an inﬁnite alphabet, Electron.
J. Comb., 24 (2017) 2-52.

N -FACTOR COMPLEXITY OF THE INFINITE FIBONACCI SEQUENCE AND DIGITAL SEQUENCES 21

(Y.-X. Li) School of Mathematics, South China University of Technology, Guangzhou 510640, China
Email address: ma lyx@mail.scut.edu.cn

(W. Wu) School of Mathematics, South China University of Technology, Guangzhou 510640, China
Email address, corresponding author: wuwen@scut.edu.cn
