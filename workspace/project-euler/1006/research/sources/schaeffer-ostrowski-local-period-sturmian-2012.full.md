<!-- source: https://arxiv.org/pdf/1210.2343 | converted from PDF -->

arXiv:1210.2343v1  [cs.FL]  8 Oct 2012
Ostrowski Numeration and the Local Period of Sturmian
Words

Luke Schaeffer

School of Computer Science
University of Waterloo
Waterloo, ON N2L 3G1 Canada
l3schaef@cs.uwaterloo.ca

October 11, 2018

Abstract

We show that the local period at position n in a characteristic Sturmian word can be given
in terms of the Ostrowski representation for n + 1.

1 Introduction

We consider characteristic Sturmian words, which are inﬁnite words over {0, 1} such that the ith
character is ⌊α(i + 1)⌋ − ⌊αi⌋ − ⌊α⌋

for some irrational α. We give an alternate deﬁnition later better suited to our purposes. Let fw(n)
denote the number of factors of length n in w, also known as the subword complexity of O(n). It is
well-known that fw(n) = n+1 when w is a Sturmian word. On the other hand, the Coven-Hedlund
theorem [4] states that fw(n) is either bounded or fw(n) ≥ n + 1 for all n. In this sense, Sturmian
words are extremal with respect to subword complexity.

In a recent paper [3], Restivo and Mignosi show that characteristic Sturmian words are also ex-
tremal with respect to local period, which we deﬁne shortly as part of Deﬁnition 2. Let pw(n)
denote the local period of a word w at position n. The critical factorization theorem states that
either pw(n) is bounded or pw(n) ≥ n + 1 for inﬁnitely many n. Restivo and Mignosi show that
when w is a characteristic Sturmian word, pw(n) is at most n + 1 and pw(n) = n + 1 inﬁnitely
often. Hence, characteristic Sturmian words also have extremal local periods.

1

n 0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20
pF (n) 1 2 3 1 5 2 2 8 1 3 3 1 13 2 2 5 1 5 2 2 21

Table 1: The local period function for the Fibonacci word.

Unlike subword complexity, the local period function pw(n) is erratic. Consider Table 1, which
gives the local period at points in F , the Fibonacci word. Although there are patterns in the table
(for example, each pF (n) is a Fibonacci number), it is not obvious how pF (n) is related to n in
general. Shallit [1] showed that pF (n) is easily computed from the Zeckendorf representation
of n + 1, and conjectured that for a general characteristic Sturmian word w, pw(n) is a simple
function of the corresponding Ostrowski representation for n+1. In this paper, we conﬁrm Shallit's
conjecture by describing pw(n) in terms of the Ostrowski representation for n + 1.

2 Notation

Let Σ := {0, 1} for the rest of this paper. We write w[n] to denote the nth letter of a word w (ﬁnite
or inﬁnite), and w[i..j] for the factor w[i]w[i + 1] · · · w[j − 1]w[j]. We use the convention that the
ﬁrst character in w is w[0]. Let |w| denote the length of a ﬁnite word w.

2.1 Repetition words

Deﬁnition 1. Let w be an inﬁnite word over a ﬁnite alphabet Σ. A repetition word in w at position
i is a non-empty factor w[i..j] such that either w[i..j] is a preﬁx of w[0..i − 1] or w[0..i − 1] is a
preﬁx of w[i..j].

If the inﬁnite word w is recurrent (i.e., every factor in w occurs more than once in w) then every
factor occurs inﬁnitely many times. In particular, for every i the preﬁx w[0..i−1] occurs in w[i..∞],
so there exists a repetition word at every position in a recurrent word.

Deﬁnition 2. Let w be an inﬁnite recurrent word over a ﬁnite alphabet Σ. Let rw(i) denote the
shortest repetition word in w at position i. The length of the shortest repetition word, denoted by
pw(i) := |rw(i)|, is called the local period in w at position i.

We note that Sturmian words are recurrent, so pw(i) and rw(i) exist at every position for a charac-
teristic Sturmian word w. We omit further discussion of the existence of pw(i) and rw(i).

For example, consider the Fibonacci word F shown in Figure 1. The factors F [5..6] = 01,
F [5..9] = 01001 and F [5..17] = 0100100101001 are examples of repetition words in the Fi-
bonacci word at position 5. The shortest repetition word at position 5 is rF (5) = F [5..6] = 01 and
therefore the local period at position 5 is pF (5) = 2.

2

F = 0 1 0 0 1 0 1 0 0 1 0 0 1 0 1 0 0 1 0 1 0 . . .

0 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20

10 0 1

10010 0 1 0 0 1

1001010010010 0 1 0 0 1 0 0 1 0 1 0 0 1

Figure 1: The Fibonacci word F and some repetition words at position 5

3 Characteristic Sturmian Words and the Ostrowski Repre-
sentation

We deﬁne characteristic Sturmian words and the Ostrowski representation based on directive se-
quences of integers, deﬁned below. For every directive sequence there is a corresponding charac-
teristic Sturmian word. Similarly, for each directive sequence there is an Ostrowski representation
associating nonnegative integers with strings.

Deﬁnition 3. A directive sequence α = {ai}∞
i=0 is a sequence of nonnegative integers, where
ai > 0 for all i > 0.

Directive sequences are in some sense inﬁnite words over the natural numbers, so we use the same
indexing/factor notation. The notation α[i] indicates the ith term, ai. We will frequently separate a
directive sequence α into the ﬁrst term, α[0], and the rest of the sequence, α[1..∞].

Note that our deﬁnitions for characteristic Sturmian words and Ostrowski representations deviate
slightly from the deﬁnitions given in our references, [2] and [5]. Speciﬁcally, there are two main
differences between our deﬁnition and [2]:

1. We start indexing the directive sequence at zero instead of one.

2. The ﬁrst term is interpreted differently. For example, if the ﬁrst term in the sequence a then
our characteristic Sturmian word begins with 0a1, whereas the characteristic Sturmian word
in [2] begins with 0a−11.

In other words, we are describing the same mathematical objects, but label them with slightly
different directive sequences. Any result that does not explicitly reference the terms of the directive
sequence will be true for either set of deﬁnitions. This includes our main result, Theorem 13.

3.1 Characteristic Sturmian Words

Consider the following collection of morphisms.

3

Deﬁnition 4. For each k ≥ 0, we deﬁne a morphism ϕk : Σ
∗ → Σ
∗ such that

ϕk(0) = 0k1
ϕk(1) = 0

for all k ≥ 0.

Given a directive sequence, we use this collection of morphisms to construct a sequence of words.

Deﬁnition 5. Let α be a directive sequence. We deﬁne a sequence of ﬁnite words {Xi}∞
i=0 over Σ
where
 Xn = (ϕα[0] ◦ · · · ◦ ϕα[n−1])(0).

We call {Xi}∞
i=0 the standard sequence, and we say Xi is the ith characteristic block.

Sometimes the characteristic blocks are deﬁned recursively as follows.

Proposition 6. Let α be a directive sequence and let {Xi}∞
i=0 be the corresponding directive se-
quence. Then
 Xn =
 




0, if n = 0;
0α[0]1, if n = 1;
X α[n−1]
n−1 Xn−2, if n ≥ 2.

Proof. See Theorem 9.1.8 in [2]. Note that due to a difference in deﬁnitions, the authors number
the directive sequence starting from one instead of zero, and they treat the ﬁrst term differently
(i.e., they deﬁne X1 as 0a1−11 instead of 0α[0]1).

It follows from the proposition that Xn−1 is a preﬁx of Xn for each n ≥ 2, and therefore the limit
limn→∞ Xn exists. We deﬁne cα, the characteristic Sturmian word corresponding to the directive
sequence α, to be this limit. cα := lim
n→∞ Xn.

Then Xn is a preﬁx of cα for each n ≥ 2.

There is a simple relationship between cα, α[0] and cα[1..∞], given in the following proposition.

Proposition 7. Let α be a directive sequence, and let β := α[1..∞]. Then

cα = ϕα[0] (cβ)

Proof. (Sketch) We factor ϕα[0] out of each Xi and then out of the limit.

cα = lim
n→∞
(ϕα[0] ◦ · · · ◦ ϕα[n−1])(0) = ϕα[0] ( lim
n→∞
(ϕα[1] ◦ · · · ◦ ϕα[n−1])(0)) = ϕα[0] (cβ) .

Alternatively, see Theorem 9.1.8 in [2] for a similar result.

4

Notice that if α[0] = 0 then cα and cβ are the same inﬁnite word up to permutation of the alphabet,
since ϕ0 swaps 0 and 1. Permuting the alphabet does not affect the local period or repetition words,
so henceforth we assume that the ﬁrst term of any directive sequence is positive (and therefore all
terms are positive). Consequently, all characteristic Sturmian words we consider will start with 0
and avoid the factor 11.

Let us give an example of a characteristic Sturmian word. Consider the directive sequence α
beginning 1, 3, 2, 2. Then we can compute the ﬁrst ﬁve terms of the standard sequence

X0 = 0
X1 = 01
X2 = 0101010
X3 = 0101010010101001
X4 = 010101001010100101010100101010010101010.

We know X4 is a preﬁx of cα, so we can deduce the ﬁrst |X4| = 39 characters of cα. Thus,

cα = 010101001010100101010100101010010101010 · · ·

By Proposition 7, cα is equal to ϕ1(cα[1..∞]).

cα = 01 01 01 0 01 01 01 0 01 01 01 01 0 01 01 01 0 01 01 01 01 0 · · ·
= ϕ1(0001000100001000100001 · · · ).

3.2 Ostrowski representation

For each directive sequence α, there is a corresponding characteristic Sturmian word cα. For
each characteristic Sturmian word there is a numeration system, the Ostrowski representation,
which is closely related to the standard sequence. For example, if the directive sequence is α =
1, 1, 1, . . . then cα is F , the Fibonacci word. The Ostrowski representation for α = 1, 1, 1, . . . is
the Zeckendorf representation, where we write an integer as a sum of Fibonacci numbers. See
chapter three in [2] for a description of these numeration systems, but note that their deﬁnition of
Ostrowski representation differs from our deﬁnition.

Deﬁnition 8. Let α be a directive sequence, and let {Xi}∞
i=0 be the corresponding standard se-
quence. Deﬁne an integer sequence {qi}∞
i=0 where qi = |Xi| for all i ≥ 0. Let n ≥ 0 be an integer.
An α-Ostrowski representation (or simply Ostrowski representation when α is understood) for n
is a sequence of non-negative integers {di}∞
i=0 such that

1. Only ﬁnitely many di are nonzero.

2. n = ∑

i diqi

3. 0 ≤ di ≤ α[i] for all i ≥ 0.
 5

4. If di = α[i] then di−1 = 0 for all i ≥ 1.

Note that by Proposition 6, we can also generate {qi}∞
i=0 directly from α using the following
recurrence
 qn =
 



1, if n = 0;
α[0] + 1, if n = 1;
qn−1α[n − 1] + qn−2, if n ≥ 2.

It is well-known that for any given directive sequence, there is a unique Ostrowski representation,
which we denote ORα(n), for every non-negative integer [2]. Also note that formally ORα(n)
is an inﬁnite sequence {di}∞
i=0, but we often write the terms up to the last nonzero term, e.g.,
dkdk−1 · · · d1d0, with the understanding that di = 0 for i > k. This is analogous to decimal
representation of integers, where we write the least signiﬁcant digit last and omit leading zeros.

Theorem 9. Let α be a directive sequence. Let n ≥ 0 be an integer, and let dkdk−1 · · · d1d0 be an
Ostrowski representation for n. Then

w := X dk
k X dk−1
k−1 · · · X d1
1 X d0
0

is a proper preﬁx of Xk+1, and therefore w is a preﬁx of cα. Since |w| = ∑

i dk |Xi| = n, it follows
that w = cα[0..n − 1].

Proof. This is essentially Theorem 9.1.13 in [2].

The following technical lemma relates Ostrowski representations for α and α[1..∞], in much the
same way that Proposition 7 relates cα to cα[1..∞].

Lemma 10. Let α be a directive sequence and deﬁne β := α[1..∞]. Let n ≥ 0 be an integer
with Ostrowski representation ORα(n) = dk · · · d0. Then there exists an integer m ≥ 0 such that
ORβ(m) = dk · · · d1 and
 cα[0..n − 1] = ϕα[0](cβ[0..m − 1])0d0.

Furthermore, if d0 > 0 then cβ[m] = 0.

Proof. We leave it to the reader to show that if dk · · · d0 is an α-Ostrowski representation then
dk · · · d1 is a β-Ostrowski representation, and conversely, if dk · · · d1 is a β-Ostrowski representa-
tion then dk · · · d10 is an α-Ostrowski representation. Theorem 9 proves that

cα[0..n − 1] = X dk
k X dk−1
k−1 · · · X d1
1 X d0
0 = cβ[0..m − 1]0d0.

Finally, suppose that d0 > 0 and cβ[m] = 1 for a contradiction. We consider the integer n − d0 + 1
and its Ostrowski representations. On the one hand, dk · · · d11 is a valid Ostrowski representation
and d0 − 1 less than n. On the other hand,

cα[0..n − d0] = ϕα[0](cβ[0..m − 1])0 = ϕα[0](cβ[0..m]),

6

so ORβ(m + 1) followed by 0 is another Ostrowski representation for n − d0 + 1. This contradicts
the uniqueness of Ostrowski representations.

Let us continue our earlier example, where we had a directive sequence α beginning 1, 3, 2, 2. We
can compute the ﬁrst ﬁve terms of {qi}∞
i=0.

q0 = |X0| = 1
q1 = |X1| = 2
q2 = |X2| = 7
q3 = |X3| = 16
q4 = |X4| = 39.

In Table 2, we show Ostrowski representations for some small integers. By Theorem 9, we should

n ORα(n) n ORα(n) n ORα(n) n ORα(n)
0 0 15 201 30 1200 45 10030
1 1 16 1000 31 1201 46 10100
2 10 17 1001 32 2000 47 10101
3 11 18 1010 33 2001 48 10110
4 20 19 1011 34 2010 49 10111
5 21 20 1020 35 2011 50 10120
6 30 21 1021 36 2020 51 10121
7 100 22 1030 37 2021 52 10130
8 101 23 1100 38 2030 53 10200
9 110 24 1101 39 10000 54 10201
10 111 25 1110 40 10001 55 11000
11 120 26 1111 41 10010 56 11001
12 121 27 1120 42 10011 57 11010
13 130 28 1121 43 10020 58 11011
14 200 29 1130 44 10021 59 11020

Table 2: Ostrowski representations where α = 1, 3, 2, 2, · · ·

be able to decompose cα[0..20] as X3X 2
1 X0 since ORα(21) = 1021.

cα[0..20] = 010101001010100101010
= (0101010010101001)(01)20
= X3X 2
1 X0.

4 Local periods in characteristic Sturmian words

Let α be a directive sequence. Let pα(n) := pcα(n) and rα(n) := rcα(n) be notation for the local
period and shortest repetition word for characteristic Sturmian words. In this section we discuss

7

how pα(n) and rα(n) are related to ORα(n + 1).

Deﬁnition 11. Let x, y be words in Σ
∗. Then x is a conjugate of y if there exist words u, v ∈ Σ
∗

such that x = uv and y = vu.

Lemma 12. Let α be a directive sequence, let β := α[1..∞] and k := α[0]. Suppose we have
integers m, n ≥ 0 such that cα[0..n] = ϕk(cβ[0..m]). Then

(i) If u is a repetition word in cβ at position m then there exists a repetition word v in cα at
position n such that ϕk(u) is a conjugate of v.

(ii) If v is a repetition word in cα at position n then there exists a repetition word u in cβ at
position m such that ϕk(u) is a conjugate of v.

In particular, rα(n) is a conjugate of ϕk(rβ(m)) when cα[0..n] = ϕk(cβ[0..m]).

Proof. We divide into two cases based on whether cβ[m] is 0 or 1. The situation when cβ[m] = 0 is
shown in Figure 2, and cβ[m] = 1 is shown in Figure 3. These ﬁgures, along with the more detailed
diagrams in Figures 4 and 5 later in the proof, indicate how ϕk maps blocks in cβ to blocks in cα.

cβ = 0 . . .

cα = 0k1 . . .

cβ[0..m]

cα[0..n]

Figure 2: Simple diagram for cβ[m] = 0
 cβ = 0 1 . . .

cα = 0k1 0 . . .

cβ[0..m]

cα[0..n]

Figure 3: Simple diagram for cβ[m] = 1

Case cβ[m] = 0:
Clearly cα[0..n] ends with 0k1 = ϕk(0) since cβ[m] = 0. This gives us Figure 2.

(i) Let u be a repetition word in cβ at position m. If cβ[0..m − 1] is a sufﬁx of u then
certainly cα[0..n − 1] = ϕk(cβ[0..m − 1]) is a sufﬁx of ϕk(u).
Suppose that u is a sufﬁx of cβ[0..m − 1]. Since cβ[m] = 0 we know u begins with 0
and write u = 0u′. Since u′ is a preﬁx of cβ[m + 1..∞], we see that v′ := ϕk(u′) is a
preﬁx of cα[n + 1..∞]. The preﬁx u′ in cβ[m + 1..∞] is followed by 00, 01 or 10. Since
ϕk(00), ϕk(01) and ϕk(10) all start with at least k zeros, we deduce that v′ (as it occurs
at the beginning of cα[n + 1..∞]) is followed by k zeros. Thus, v := 1v′0k is a preﬁx
of cα[n..∞]. From the other occurrence of u (as a sufﬁx of cβ[0..m − 1]) we deduce
that 1v′0k is also a sufﬁx of cα[0..n − 1]. We conclude that v is a repetition word in
cα at position, and note that v = 1v′0k is a conjugate of 0k1v′ = ϕk(0u′) = ϕk(u), as
required.
 8

cβ = 0 u′ 0 u′ ? . . .

cα = 0k 1 v′ 0k 1 v′ 0k . . .

v v

u u

Figure 4: Detailed diagram for cβ[m] = 0

(ii) Let v be a repetition word in cα at position n. The 1 at position n is preceded by k
zeros. Hence, cα[0..n − 1] ends in 0k, so v ends in 0k. Clearly v begins with 1, let v′ be
such that v = 1v′0k. We do not know whether the trailing 0k is the beginning of ϕk(0)
or ϕk(10), but in either case v′ is ϕk(u′) for u′ a factor of cβ.
If cα[0..n − 1] is a proper sufﬁx of v then cα[0..n − k − 1] is a sufﬁx of v′. Then
cβ[0..m − 1] is a sufﬁx of u′, and hence u := 0u′ is a repetition word in cβ at position
m such that v is a conjugate of ϕk(u).
Otherwise, v is a sufﬁx of cα[0..n − 1]. The trailing 0k in this occurrence of v is in the
image of cβ[m] = 0. The remaining 1v′ must be preceded by 0k, and then 0k1v′ is the
image of 0u′, which occurs as a sufﬁx of cβ[0..m − 1]. Now we have the situation in
Figure 4. It follows that u := 0u′ is a repetition word, and v = 1v′0k is a conjugate of
ϕk(u) = 0k1v′.

Case cβ[m] = 1:
The characteristic Sturmian words we consider start with 0, so m ̸= 0. Since cβ does not
contain the factor 11, we know cβ[m − 1] = 0. Therefore cα[0..n] ends in ϕk(01) = 0k10,
as shown in Figure 3.

cβ = 1 u′ 0 1 u′ 0 . . .

cα = 0 v′ 0k1 0 v′ 0k1 . . .

v v

u u

Figure 5: Detailed diagram for cβ[m] = 1

(i) Suppose u is a repetition word in cβ at position m, and let v := ϕk(u). We know that
ϕk(cβ[0..m − 1]) = cα[0..n − 1] and ϕk(cβ[m..∞]) = cα[n..∞]. Thus,

• v is a preﬁx of cα[n..∞] if u is a preﬁx of cβ[m..∞]
• v is a sufﬁx of cα[0..n − 1] if u is a sufﬁx of cβ[0..m − 1]
• cα[0..n − 1] is a sufﬁx of v if cβ[0..m − 1] is a sufﬁx of u.

9

It follows that v is a repetition word in cα at position n.

(ii) Suppose v is a repetition word in cα at position n. We know v starts with 0 since
cα[n] = 0, and v ends with 1 since cα[n − 1] = 1, therefore v = 0v′0k1 for some v′.
Then v′ = ϕk(u′) for some u′, and we deﬁne u := 1u′0 so that

ϕk(u) = ϕk(1u′0) = 0v′0k1 = v.

It is also clear that

• u is a preﬁx of cβ[m..∞]
• u is a sufﬁx of cβ[0..m − 1] if v is a sufﬁx of cα[0..n − 1]
• cβ[0..m − 1] is a sufﬁx of u if cα[0..n − 1] is a sufﬁx of v,

so we conclude that u is a repetition word in cβ at position m.

Theorem 13. Let α be a directive sequence and let β := α[1..∞]. Let n ≥ 0 be a nonnegative
integer. Let t be the number of trailing zeros in ORα(n + 1). Then rα(n) is a conjugate of Xt,
except when all of the following conditions are met:

• The last nonzero digit in ORα(n + 1) is 1.

• ORα(n + 1) contains at least two nonzero digits.

• The last two nonzero digits of ORα(n + 1) are separated by an even number of zeros.

When ORα(n + 1) meets these conditions, then rα(n) is a conjugate of Xt+1 .

Proof. Let dk · · · d0 = ORα(n + 1) be the Ostrowski representation of n + 1. Let t be the number
of trailing zeros in ORα(n + 1). We use induction on t to prove that rα(n) is a conjugate of Xt, or
under the conditions described above, a conjugate of Xt+1.

Base case t = 0: Since n + 1 > 0, we have d0 > 0. By Theorem 9, we have

cα[0..n] = X dk
k · · · X d0
0 .

If d0 ≥ 2 then we are done since cα[0..n] ends in 00. Hence cα[n − 1] = cα[n] = 0 and
rα(n) = 0 = X0 is the shortest repetition word at position n. Let us assume without loss of
generality that d0 = 1.

According to the induction hypothesis, the second last nonzero digit in ORα(n + 1) becomes
relevant when the last nonzero digit is 1. If d0 is the only nonzero digit, then n = 0 and
rα(0) is clearly cα[0] = 0. Otherwise, pick ℓ > 0 minimal such that dℓ ̸= 0. That is, let dℓ be
the second last nonzero digit. Note that by Theorem 9, the word cα[0..n − 1] ends in Xℓ.

10

If ℓ is even then Xℓ ends in 0 (by a simple induction), so cα[n − 1] = 0 and it follows that
rα(n) = 0. When ℓ is odd, the word Xℓ ends in X1 and X1 ends in 1. It follows that

cα[0..n − 1] = ϕα[0](cβ[0..m − 1])

for some m ≥ 0. We claim that cβ[m] = 0, since otherwise

ϕα[0](cβ[0..m]) = cα[0..n]

so Lemma 10 states that ORα(n + 1) ends in 0, contradicting d0 = 1. Then cα[n..∞] begins
with ϕα[0](cα[m]) = X1, so rα(n) = X1.

Inductive step t > 0: We note that removing (or adding) trailing zeros from ORα(n + 1) does
not change whether it satisﬁes all three conditions in the theorem. We will assume that
ORα(n + 1) does not meet the conditions, since the proof is nearly identical if it does meet
the conditions.

Let {Xi}∞
i=0 and {Yi}∞
i=0 be standard sequences corresponding to the directive sequences α
and β respectively. Lemma 10 states that cα[0..n] = ϕα[0](cβ[0..m]) where m ≥ 0 is such
that ORβ(m + 1) = dk · · · d1.

Note that dk · · · d1 has t − 1 trailing zeros, so rβ(m) is a conjugate of Yt−1 by induction. By
Lemma 12, rα(n) is a conjugate of ϕα[0](Yt−1) = Xt, completing the proof.

Let us continue our example with a directive sequence α starting with 1, 3, 2, 2. Recall that

cα = 01010 10010 10100 10101 01001 01010 01010 1010 · · ·

Consider the shortest repetition words at positions 23 through 26. These positions happen to give
illustrative examples of the theorem.

rα(23) = 0 X0 = 0 ORα(24) = 1101
rα(24) = 1010100 X2 = 0101010 ORα(25) = 1110
rα(25) = 01 X1 = 01 ORα(26) = 1111
rα(26) = 10 X1 = 01 ORα(27) = 1120

When n = 23, there are no trailing zeros in ORα(24) = 1101 and we have an odd number of zeros
between the last two nonzero digits. Hence, rα(23) is a conjugate of X0 = 0. Compare this to
n = 25, where ORα(26) = 1111 also has no trailing zeros, but the last two ones are adjacent, so
rα(25) is a conjugate of X1. We are in a similar situation for n = 24, but with an trailing zero
so rα(24) is a conjugate of X2. Finally, consider n = 26 where the last two nonzero digits are
adjacent and we have a trailing zero, like n = 24, but the last nonzero digit is not a one. It follows
that rα(26) is a conjugate of X1. Although rα(25) and rα(26) are both conjugates of X1, they are
not the same.
 11

5 Open Problems and Further Work

It would be interesting to generalize the result to two-sided Sturmian words, with an appropriate
deﬁnition for local period in two-sided words. We might deﬁne a repetition word in w ∈ ωΣ
ω

at position n as a word that is simultaneously a preﬁx of w[n..∞] and a sufﬁx of w[−∞..n − 1].
Note that if we extend a characteristic Sturmian word cα to a two-sided word w, the local period at
position n in w may not be the same as the local period at position n in cα.

Our main result is about the local period and the shortest repetition word, but Lemma 12 applies to
all repetition words at a speciﬁc position. Is it possible to extend our result to all repetition words,
not just the shortest repetition word? Patterns in the lengths of repetition words for the Fibonacci
word suggest that it is possible, but we do not have a speciﬁc conjecture.

References

[1] J. Shallit (Personal communication).

[2] J.-P. Allouche, J. Shallit, Automatic Sequences, Cambridge Univ. Press (2003).

[3] F. Mignosi, A. Restivo, Characteristic Sturmian words are extremal for the Critical Factoriza-
tion Theorem, Theoret. Comput. Sci. 454 (2012), 199–205.

[4] E. Coven, G. Hedlund, Sequences with minimal block growth, Math. Systems Theory 7 (1973)
138–153.

[5] J. Berstel and P. S´e´ebold, Sturmian words, in M. Lothaire, ed., Algebraic Combinatorics on
Words, Encyc. of Math. and its Appl., Vol. 90, Cambridge Univ. Press (2002) 45–110.

12
