<!-- source: https://arxiv.org/pdf/1710.11553 | converted from PDF -->

arXiv:1710.11553v2  [cs.FL]  2 Nov 2017
Sturmian numeration systems and decompositions to
palindromes

Anna E. Frid

Aix Marseille Univ, CNRS, Centrale Marseille, I2M, Marseille, France

Abstract

We extend classical Ostrowski numeration systems, closely related to Stur-
mian words, by allowing a wider range of coeﬃcients, so that possible repre-
sentations of a number n better reﬂect the structure of the associated char-
acteristic Sturmian word. In particular, this extended numeration system
helps to catch occurrences of palindromes in a characteristic Sturmian word
and thus to prove for Sturmian words the following conjecture stated in 2013
by Puzynina, Zamboni and the author: If a word is not periodic, then for
every Q > 0 it has a preﬁx which cannot be decomposed to a concatenation
of at most Q palindromes.

Keywords: numeration systems, Ostrowski numeration systems, Sturmian
words, palindromes, palindromic length
2000 MSC: 68R15

1. Introduction

Ostrowski numeration systems, ﬁrst introduced in 1921 [16], are closely
related to continued fractions. A classical example of an Ostrowski numer-
ation system is the Fibonacci (or Zeckendorf) numeration system, ﬁrst de-
scribed by Lekkerkerker in 1952 [14, 18], where a number is represented as
a sum of Fibonacci numbers, but not consecutive ones (since the sum of
two consecutive Fibonacci numbers is the next Fibonacci number). In some
studies, the idea is extended to allow consecutive Fibonacci numbers [2] and
the analogous freedom for the general Ostrowski representations [10]. In the

Email address: anna.e.frid@gmail.com (Anna E. Frid)

Preprint submitted to European Journal of Combinatorics November 27, 2024

last mentioned paper, this was made to better explore the link between Os-
trowski representations and Sturmian words which can also be constructed
with the use of a continued fraction and its directive sequence. For the link
between Ostrowski representations and Sturmian words, see also [5]; for a
modern deﬁnition of an Ostrowski numeration system, see [1]. For a general
introduction to Sturmian words, see [4].
In this paper, we extend the range of possible representations in an
Ostrowski-like numeration system even further to better reﬂect the struc-
ture of the related Sturmian word. In particular, this allow us to describe
occurrences of palindromes in a Sturmian word by representations of their
ends. Note that palindromes in Sturmian words have been extensively stud-
ied, and even their occurrences were completely described by Glen [13]. How-
ever, their relation to our numeration system catches some internal structure
and in particular, allows to prove for Sturmian words the 2013 conjecture by
Puzynina, Zamboni and the author [12] which can be formulated as follows.
The palindromic length of a ﬁnite word u is the minimal number Q of
palindromes P1, . . . , PQ such that u = P1 · · · PQ.

Conjecture 1. In every inﬁnite word which is not ultimately periodic, the
palindromic length of factors (version: of preﬁxes) is unbounded.

The conjecture was stated in 2013 by Puzynina, Zamboni and the author
[12] and was proved in the same paper for the case when the inﬁnite word
is k-power-free for some k; moreover, a generalisation of the original proof
works for a wider class of inﬁnite words covering in particular ﬁxed points
of morphisms. Recently, Saarela [17] proved the equivalence of two versions
of the conjecture: the palindromic length of factors is bounded if and only
if this is true for preﬁxes. Bucci and Richomme [6] managed to prove the
analogue of the conjecture for greedy palindromic lengths, but their result
does not help to do it for the original statement.
So, until now, Sturmian words remained the simplest class of words for
which the conjecture was not proved. As we know from a 1991 paper by
Mignosi [15], a Sturmian word is k-power-free for some k if and only if the
directive sequence of the respective continued fraction is bounded. The case
when it is unbounded does not fall into any class for which the conjecture has
been proved. Moreover, computational experiments by Bucci and Richomme
[6] showed that the minimal length of a Sturmian factor whose palindromic
length is n can grow surpisingly fast.
 2

In this paper we use a new technique related to extended Sturmian nu-
meration systems to prove Conjecture 1 for every Sturmian word with an
unbounded directive sequence. The word of a palindromic length greater
than a given Q is found explicitly as the preﬁx of the characteristic Stur-
mian word of length whose Ostrowski-like representation is of a given form.
Since every Sturmian word has the same set of factors as some characteristic
one, and due to the above-mentioned result by Saarela [17], this proves both
versions of the conjecture for all Sturmian words.
We believe that ﬁrst, our extension of the Ostrowski numeration system
can be useful for other related problems, and second, that the developed
technique can be generalized to prove Conjecture 1 for all inﬁnite words for
which it is not yet proved, even though the proof has to be much bulkier.
Moreover, new numeration systems themselves, as well as their link to palin-
dromes, make a beautiful object for further studies.
The paper is organized as follows. In the next section, after introducing
some basic notation, we deﬁne new Sturmian representations of non-negative
integers. In Section 3 we prove some properties of these representations and,
inevitably, of Sturmian words. The main result of this section is Corollary 2
stating that all valid representations of the same number can be obtained one
from another by a series of elementary transformations. Section 4 is devoted
to representations of ends of palindromes and establishes relations between
them (Theorem 2). At last, in Section 5, the described properties are used
to prove that the palindromic length of preﬁxes of characteristic Sturmian
words is unbounded.

2. Notation and Sturmian representations

We use the notation usual in combinatorics on words; the reader is re-
ferred, for example, to [4] for an introduction on it. Given a ﬁnite word
u, we denote its length by |u|. The power uk means just a concatenation
uk = u · · · u︸ ︷︷ ︸
k . Symbols of ﬁnite or inﬁnite words are denoted by u[i], so that

u = u[1]u[2] · · · . A factor w[i + 1]w[i + 2] · · · w[j] of a ﬁnite or inﬁnite word
w, or, more precisely, its occurrence starting from the position i + 1 of w,
is denoted by w(i..j]. In particular, for j > 0, w(0..j] is the preﬁx of w of
length j.
Sturmian words can be deﬁned in many diﬀerent ways discussed in detail
in [4]. What we use in this paper the classical construction related to a direc-

3

tive sequence (d0, d1, . . . , dn, . . .), where di ≥ 1. Given a directive sequence,
the standard sequence (sn) of words on the binary alphabet {a, b} is deﬁned
as follows: s−1 = b, s0 = a, sn+1 = sdn
n sn−1 for all n ≥ 0. (1)

The word sn is called also the standard word of order n.
Note that to get all possible standard words, we also need to allow d0 = 0,
but due to the symmetry between a and b, we can restrict ourselves to the
case of d1 > 0.
It is easy to see that starting from n = 0, each sn is a preﬁx of sn+1, and
the lengths of sn strictly grow, so that there exists a right inﬁnite word w =
limn→∞ sn. The word w is called a characteristic Sturmian word associated
with a sequence (di). A word is Sturmian if its set of factors coincides with
that of some characteristic Sturmian word. For a classical survey on Sturmian
words and in particular characteristic Sturmian words see, e. g., [4].
Note that the directive sequence (di) is closely related to the continuous
fraction expansion of the slope of the Sturmian word. However, continuous
fractions are not directly used in this paper. However, we will make use of
the coeﬃcients qn which are lengths of the words sn: by the deﬁnition of sn,
we have q−1 = q0 = 1, qn+1 = dnqn + qn−1 for all n ≥ 0.

In the Ostrowski numeration system [16, 1] associated with the sequence (di),
a non-negative integer N < qj+1 is represented as

N = ∑

0≤i≤n kiqi, (2)

where 0 ≤ ki ≤ di for i ≥ 0, and for i ≥ 1, if ki = di, then ki−1 = 0. Such
a representation of N is unique up to leading zeros (see Theorem 3.9.1 in
[1]). We use the notation N = kn · · · k1k0[o]. Note also that everywhere in
the text, we will not distinguish representations which diﬀer only by leading
zeros.
The following lemma is a well-known direct corollary of the deﬁnition
of characteristic Sturmian words and of the Ostrowski numeration system.
Further in this paper we will give a proof for a more general result, named
here as Corollary 1.

Lemma 1. Let w be the characteristic Sturmian word associated with the
directive sequence (di) and N = kn · · · k1k0[o] in the respective Ostrowski
numeration system. Then w(0..N] = skn
n skn−1
n−1 · · · sk1
1 sk0
0 .

4

Example 1. The directive sequence (1, 1, 1, . . .) corresponds to the famous
Fibonacci word deﬁned by its preﬁxes s0 = a, s1 = s0s−1 = ab, s2 = s1s0 =
aba, s3 = s2s1 = abaab, etc.:

w = abaababaabaababaababa · · · .

The lengths qi = |si| are Fibonacci numbers, and the respective numeration
system is the Fibonacci, or Zeckendorf, one: it corresponds to the greedy
decomposition of a number N to a sum of Fibonacci numbers Fn: here we
start from F0 = 1, F1 = 2. For example, 14 = 13 + 1 = F5 + F0, and thus
14 = 100001[o].

In several recent papers [10, 2], more general legal decompositions of the
same type have been considered. A decomposition N = ∑

0≤i≤n kiqi is called
legal if 0 ≤ ki ≤ di for i ≥ 0 (but the second restriction from the deﬁnition of
the Ostrowski representation is not imposed). A number can admit several
legal representations, including the Ostrowski one. A legal representation of
N is denoted by N = kn · · · k1k0 (without [o] at the end, reserved for the
Ostrowski version).
In this paper, we extend the deﬁnition of such a decomposition even more
by deﬁning general Sturmian representations of non-negative integers.

Deﬁnition 1. Given a directive sequence (di) and the respective sequence
(si) of standard words, |si| = qi, we call a decomposition N = ∑
0≤i≤n kiqi
valid if the preﬁx of length N of the characteristic Sturmian word w is equal
to skn
n skn−1
n−1 · · · sk1
1 sk0
0 . A valid representation of N is also denoted as N =
kn · · · k1k0. We are going to discuss why it is correct to have the same notation
for legal and valid representations.

Example 2. As we have seen in the previous example, in the Fibonacci
word, the Ostrowski representation of 14 is 14 = 100001[o]. We also have a
legal representation 14 = 11001 since 14 = F4 + F3 + F0 = 8 + 5 + 1. This
representation is also valid, since the preﬁx w(0..14] = abaababaabaaba of the
Fibonacci word is equal to s4s3s0: indeed, s0 = a, s3 = s2s1 = abaab, and
s4 = s3s2 = abaababa.
Now consider the representation 14 = 1300. It is valid since w(0..14] =
s3s3
2 = (abaab)(aba)3, but not legal since its digit b2 = 3 is greater than
d2 = 1.
 5

3. Properties of Sturmian words and valid representations

Throughout this section, we consider a ﬁxed directive sequence (di) and
the standard words si (and other notions) associated with it.
In particular, we need the following classical properties [9, 4]: for all
n ≥ 0, we have snsn−1 ̸= sn−1sn, but these two words coincide except for
the last two symbols: snsn−1 = cnxy and sn−1sn = cnyx, where if n is even,
x = a and y = b and if n is odd, x = b and y = a. The words cn as well as
all words cn,j = sj−1
n cn for j > 0, obtained by erasing two last symbols from
sj
nsn−1, are called central (Sturmian) words and are palindromes.
The following proposition can be found e. g. in [3].

Proposition 1. For all n ≥ 0, we have sdn
n sdn−1
n−1 · · · sd0
0 = cn+1.

Proposition 2. For all k0, . . . , kn such that ki ≤ di, the word skn
n skn−1
n−1 · · · sk0
0
is a preﬁx of cn+1.

Proof. For n = 0, the statement is obvious. To proceed by induction on n,
it is clearly suﬃcient to prove that if u is a preﬁx of cn, then skn
n u is a preﬁx
of cn+1. To see it, suppose ﬁrst that kn < dn. In this situation, we consider
cn as a preﬁx of snsn−1 and see that skn
n u is a preﬁx of skn+1
n sn−1 which is in
its turn a preﬁx of sn+1, which is a preﬁx of cn+1. Now suppose that kn = dn
and consider cn as a preﬁx of sn−1sn (obtained by erasing two last symbols).
We see that skn
n u = sdn
n u is a preﬁx of sdn
n sn−1sn = sn+1sn obtained by erasing
at least two last symbols, that is, it is a preﬁx of cn+1. □

The next corollary explains why we feel free to use the same notation for
legal and valid representations.

Corollary 1. Every legal representation of a number N in a Sturmian rep-
resentation system is valid.

Proof. Follows immediately from the deﬁnitions, the previous proposition
and the fact that for all n, the word cn+1 is by the construction a preﬁx of
the characteristic Sturmian word. □

In particular, Corollary 1 implies Lemma 1: the Ostrowski representation
is valid.
Here is yet another property of valid representations.

Proposition 3. Let kn · · · k0 be a valid representation of a number N. Then
k0 ≤ d0 + 1, k1 ≤ d1 + 1, and for all i ≥ 2, we have ki ≤ di + 2.

6

Proof. The restriction k0 ≤ d0+1 follows from the fact that by the construc-
tion, the maximal number of consecutive as in w is d0 + 1. The restrictions
k1 ≤ d1 + 1 and ki ≤ di + 2 for i ≥ 2 follow immediately from Lemma 3.4 of
[7] stating that the maximal power of si in w is 2 + di + (qn−1 − 2)/qn. □

Now let us deﬁne two basic transformations of valid representations. Con-
sider a representation r = kn · · · k0, where km = dm and km−1 > 0 for some
m ≥ 1, so, r = kn · · · km+1dmkm−1 · · · k0. To distinguish the representation
and the number N it denotes, we write N = r. The unbending transformation
ρm is deﬁned on such representations by

ρm(kn · · · km+1 · dm · km−1 · · · k0) = kn · · · (km+1 + 1) · 0 · (km−1 − 1) · · · k0.

(Here and below we sometimes put dots between digits for readability.) In
particular, for m = n, we have to add to the representation the new symbol
kn+1 = 1: ρn(dnkn−1 · · · k0) = 1 · 0 · (kn−1 − 1) · · · k0.
The inverse bending transformation βm = ρ
−1
m for m ≥ 1 is deﬁned on
representations with km+1 > 0, km = 0 by

βm(kn · · · km+1 · 0 · km−1 · · · k0) = kn · · · (km+1 − 1) · dm · (km−1 + 1) · · · k0.

Proposition 4. Consider a representation N = r such that ρm(r) (respec-
tively, βm(r)) is well-deﬁned for some m ≥ 1. If this representation is valid,
then N = ρm(r) (N = βm(r)) is also a valid representation of N.

Proof. Consider a valid representation r = kn · · · k0. The fact that ρm
is well-deﬁned means that km = dm and km−1 > 0. By the deﬁnition of a
valid representation, we have that the preﬁx of w of length n is equal to
skn
n · · · skm+1
m+1 sdm
m skm−1
m−1 · · · sk0
0 . But sdm
m sm−1 = sm+1, so, the same preﬁx is also
equal to skn
n · · · skm+1+1
m+1 skm−1−1
m−1 · · · sk0
0 . The proof for βm is symmetric. □

Example 3. Let us start from the representation 14 = 1300 in the Fibonacci
numeration system considered in Example 2. Here dm = 1 for all m. We
have 1300 ρ3
−→ 10200 β1
−→ 10111 ρ2
−→ 11001 ρ4
−→ 100001.

Due to the previous proposition, we obtain that 14 = 100001; in fact, this
is the Ostrowski representation. Note that we can also invert this series of
transformations:

100001 β4
−→ 11001 β2
−→ 10111 ρ1
−→ 10200 β3
−→ 1300.

7

We are going to prove that any valid representation can be transformed
to the Ostrowski one by a series of unbending and bending transformations.
To do it, we need two more propositions.

Proposition 5. Let us consider a sequence of coeﬃcients km, . . . , kn of length
l = n − m + 1 such that m ≥ 0, km < dm, and for each i greater than m, we
have ki ≤ di with ki = di implying ki−1 = 0. Then the word ul = skn
n · · · skm
m
is a preﬁx of w which is followed in w by the word smsm−1.

Proof. Let us proceed by induction on the length l of the sequence, l =
n − m + 1. If l = 0, the preﬁx u0 is empty, so, it is suﬃcient to notice that
w starts with sn+1sn. If l = 1, we have u1 = skn
n , where kn < dn, and use
the above observation for l = 0 and the fact that sn+1 = sdn
n sn−1. So, u1 is
followed in w either by snsn−1 (if kn = dn − 1) or by snsn (if kn < dn − 1),
but since sn starts with sn−1, this gives us what we need anyway.
Now suppose that l ≥ 2 and that the statement is proved for l − 1 and
l − 2 (that is, for m + 1 and m + 2). Let us prove it for l (and m). By the
assertion, we have km < dm.
If km+1 < dm+1, we use the statement for l − 1 to see that ul−1 is followed
by sm+1sm. When we add skm
m to ul−1 to get ul, we erase from sm+1sm =
sdm
m sm−1sm the preﬁx skm
m , and as above, we see that what remains starts
from smsm−1.
If km+1 = dm+1, we by the assertion have km+2 < dm+2 and km = 0. By
the induction hypothesis, ul−2 is followed by sm+2sm+1 = sdm+1
m+1 smsm+1. To
get ul, we add to ul−2 the word sdm+1
m+1 . In w, it is continued by smsm+1, and
since sm+1 starts with sm−1, the statement is proved. □

Proposition 6. Let kn · · · k0 be a valid representation of a number N. Sup-
pose that for some m ≥ 0, we have km+1 < dm+1, and for each i greater than
m + 1, we have ki ≤ di with ki = di implying ki−1 = 0. Then km ≤ dm + 1,
and the equality km = dm + 1 implies that m ≥ 2 and km−1 = 0.

Proof. As it was proved in the previous statement, the preﬁx skn
n · · · skm+1
m+1
of w is followed by sm+1sm. If m = 0, sm+1 = s1 = a
d0b, meaning that
km = k0 ≤ d0. If m = 1, s2s1 = (a
d0b)d1a
d0+1b, and we see that again,
km = k1 ≤ d1. If m ≥ 2, then sm+1sm = sdm
m sm−1sm. We know that sm−1sm
diﬀers from smsm−1 exactly by the last two symbols, whereas sm−1 is of length
at least 2 and sm−1 is a preﬁx of sm. So, sm+1sm starts with sdm+1
m but is not
equal to sdm+1
m sm−1, the word of the same length which is a preﬁx of sdm+2
m .

8

This means exactly that km ≤ dm + 1. Moreover, if km = dm + 1, the next
factor of w of length qm−1 is not equal to sm−1, which means that km−1 = 0.
□

Theorem 1. A representation of a number N is valid if and only if it can
be transformed to the Ostrowski representation of N by a series of unbending
and bending transformations.

Proof. The Ostrowski representation is valid due to Corollary 1, and since
unbending and bending transformations are inversible and preserve validity
due to Proposition 4, the “if” part follows.
Now let us consider a valid representation r0 = kn · · · k0 and get from it
the Ostrowski representation as follows. We look for the greatest m such
that either km = dm and km−1 > 0, or km > dm. Due to Proposition 6, the
second situation is possible only if km = dm + 1, m ≥ 2 and km−1 = 0.
So, if km = dm and km−1 > 0, we take r1 = ρm(r0), turning the symbols
km+1 · dm · km−1 into (km+1 + 1) · 0 · (km−1 − 1). If km = dm + 1, m ≥ 2 and
km−1 = 0, we take r1 = ρm(βm−1(r0)), turning km+1 · (dm + 1) · 0 · km−2 ﬁrst to
km+1·dm·dm−1·(km−2+1) and then to (km+1+1)·0·(dm−1−1)·(km−2+1). Note
that both transformations are possible since by our conditions, km+1 < dm+1,
and that due to Proposition 4, r1 is also a valid representation of N.
Now we repeat the same procedure and similarly get valid representations
r2, r3 and so on, every time transforming the leftmost fragment with km = dm
and km−1 > 0, or with km = dm + 1, as it is described above: so, either ri+1 =
ρm(ri), or ri+1 = ρm(βm−1(ri)). As soon as there are no such fragments, we
get the Ostrowski representation. It remains only to prove that the process
is always ﬁnite.
Indeed, each transformation of the type ri+1 = ρm(βm−1(ri)) decreases the
greatest position m of the digit km such that km > dm. And each transforma-
tion of the type ri+1 = ρm(ri) does not increase that position and decreases
the sum of digits in the representation. Thus the chain of transformations
cannot be inﬁnite, and the theorem is proved. □

Corollary 2. Every two valid representations of the same number can be ob-
tained from each other by a series of unbending and bending transformations.

Proof. The statement directly follows from Theorem 1 and the fact that
every transformation is inversible: the inverse of a bending transformation is
an unbending transformation and vice versa. □

9

Note that a complete study of valid representations is not within the goals
of this paper. Below we just give some their properties which will be useful
later.

Proposition 7. Consider a representation N = kn · · · k0 where km ≥ 2 and
km−1 ≥ 1 for some m ≥ 1. Then for any other representation N = bn′ · · · b0
obtained from it by a series of transformations βi and ρi for i < m, we have
bm ≥ km − 1.

Proof. Let us proceed by induction on m. If m = 1, the statement is
obvious since βi and ρi for i < 1 are not even deﬁned. If m = 2, we cannot
apply β1 since k1 > 0, and the use of ρ1 can only increase k2.
Suppose now that m > 2 and the statement is proved for m − 2. To
decrease km, we should ﬁrst reduce km−1 to zero. This is possible at least if
km−1 = 1 and km−2 = 0: then we have

· · · km10km−3 · · · βm−2
−−−→ · · · km0dm−2(km−3 + 1) · · ·

βm−1
−−−→ · · · (km − 1) · dm−1 · (dm−2 + 1) · (km−3 + 1) · · ·

(here again dots are added for the sake of readability). To decrease the
digit at position m further, we should ﬁrst turn dm−1 to zero, and to do
it, we should ﬁrst do the same with the digit at position m − 2. But the
situation at positions m − 2 and m − 3 falls into the induction step: we have
dm−2 +1 ≥ 2 and km−3 +1 ≥ 1. The use of ρm−1 and ρm−2 does not help since
can only invert the previously used transformations. So, further decrease of
the symbol number m is not possible, which was to be proved. □

Proposition 8. Let r = kn · · · k0 and bn · · · b0 be two valid representations
of the same number N (we may assume that their lengths are equal since it
is not prohibited to add zeros at the left). Suppose that for some m, where
0 ≤ m ≤ n, we have 4 ≤ km ≤ dm − 4. Then |bm − km| ≤ 3.

Proof. Due to Corollary 2, every representation of N can be obtained from
r by bending and unbending transformations. Since km is not equal to 0 nor
dm, we cannot apply ρm or βm until km is suﬃciently changed. So, we have a
restriction to use only transformations βi and ρi with i > m or i < m. These
two groups of transformations do not aﬀect each other except for the change
of the digit number m.
Suppose that we try to decrease km. For i > m, the only transformation
which can do it is ρm+1 (if km+1 = dm+1). For i < m, we can apply βm−1

10

if km−1 = 0. After applying these two transformations, in any order, the
fragment · · · km+2dm+1km0km−2 · · · is transformed into

· · · (km+2 + 1) · 0 · (km − 2) · dm−1 · (km−2 + 1) · · · .

We see that there is no mean to decrease the digit number m by transfor-
mations with i > m, since there is no mean to increase the digit number
m + 1 without increasing the digit number m if the digit number m + 2 is
non-zero. As for the transformations with i < m, we use Proposition 7 to
show that the maximal possible decrease in this situation is by one. Note
that the proposition can be applied since km − 2 ≥ 2 and dm−1 ≥ 1.
So, the total possible decrease of the digit number m is at most 3. The
proof for the increase is symmetric. □

Example 4. The change by 3 is indeed possible. Consider the directive
sequence with di = 1 for i = 0, . . . , 3, 5, and d4 > 4. Then

140000 ρ5
−→ 1030000 β3
−→ 1021100 β1
−→ 1021011 β2
−→ 1020121 β3
−→ 1011221.

We see that the digit number 4 was decreased from 4 to 1.

4. Palindromes and their representations

In this section, we investigate valid representations of palindromes which
occur in characteristic Sturmian words.
The main statement of the section which will be proved below is

Theorem 2. Let w be a characteristic Sturmian word corresponding to the
directive sequence (dn), and w(p1..p2] be a palindrome. Then there exists a
valid representation p1 = xn · · · x0 and a number m ≤ n such that xi ≤
di for all i < m and xn · · · xm+1ym · (dm−1 − xm−1) · · · (d0 − x0) is a valid
representation of p2 for some ym.

Example 5. Consider the palindrome w(12..13] = w[13] = b in the Fibonacci
word w = abaababaabaababaababaabaab · · · .

The Ostrowski representations of 12 = 10101[o] and 13 = 100000[o] are quite
diﬀerent. However, the representations 12 = 1201 and 13 = 1210 are also
valid and ﬁt the statement of the theorem for m = 1.

11

Note also that the pair of representations from Theorem 2 is not obliged to
be unique. For example, for the palindrome w(7..9] = aa, we have 7 = 1010
and 9 = 1012 = 1101. Both representations of 9 constitute a pair from
Theorem 2 with the representation of 7: for the ﬁrst one, m = 0, and for the
second one, m = 2.

To prove the theorem, we ﬁrst have to describe some properties of palin-
dromes in Sturmian words.
Let w be an inﬁnite word and its factor w(p1..p2] be a palindrome. If
w(p1 − 1..p2 + 1] is also a palindrome, it is called the palindromic extension
of w(p1..p2]. We can continue the process until either after p1 steps we get
a palindrome preﬁx w(0..p2 + p1] of w, or until w(p1 − d − 1..p2 + d + 1] is
not a palindrome for some d < p1. In both cases, we speak of the maximal
(palindromic) extension w(0..p2 + p1] or w(p1 − d..p2 + d] of the occurrence
w(p1..p2].
To prove the next proposition, we need to know that a factor u of an
inﬁnite words w over the alphabet {a, b} is called left special if au and bu
are both factors of w. Symmetrically, it is called right special if ua, ub are
factors of w. A word which is left and right special is called bispecial.
The set of factors of a Sturmian word is closed under reversal (see Propo-
sition 2.1.19 of [4]). It is also known (see Subsection 2.1.3 of [4]) that all
preﬁxes of characteristic Sturmian words are left special. This immediately
means that bispecial factors of a characteristic Sturmian word are exactly its
preﬁxes which are palindromes.

Proposition 9. For every occurrence of a palindrome to a characteristic
Sturmian word w, its maximal palindromic extension is bispecial.

Proof. If the maximal palindromic extension is a preﬁx of w, it is bispecial
as discussed above. If it is of the form w(p1 − d..p2 + d] with d < p1, where
w(p1..p2] is the initial palindrome, it means that its left and right extension
letters are diﬀerent: w[p1 − d] ̸= w[p2 + d + 1]. Since the set of factors of w
is closed under reversal, and w(p1 − d..p2 + d] is a palindrome, it means that
it is bispecial. □
Bispecial factors in a Sturmian word constructed with a given directive
sequence (which are also exactly preﬁxes of the characteristic word that are
palindromes) are completely described (see [9, 4]). They are are exactly
central words deﬁned above as follows: for each n ≥ 0, cn is the word obtained
from snsn−1 by erasing two last symbols, and for each j ≥ 0, the word cn,j

12

is deﬁned as cn,j = sj
ncn, so, cn,j is obtained by erasing two last symbols
from sj+1
n sn−1. In particular, cn = cn,0 for all n. Also, c0 is the empty word,
c0,j = a
j, c1 = a
d0 = c0,d0, c1,j = (a
d0b)ja
d0, c2 = c1,d1, and so on.
The following fact is a reformulation of results of [9, 3].

Proposition 10. The bispecial factors of a caracteristic Sturmian word w
are exactly words cn,j, where 0 ≤ j ≤ dn. All these words are palindromes
and each cn,j except for c0,0 which is empty and c1,0 = a
d0 = c0,d0 starts with
sn.

Remark 1. There is no doubt that the link between Sturmian palindromes
and central words has been known to specialists since many years. However,
it is diﬃcult to ﬁnd references with precisely needed statements. For example,
in [8], it was proved that every palindrome in a Sturmian word is a median
factor of a central word, but this statement concerned words and not their
occurrences. For a recent study of bispecial Sturmian words, the reader is
referred to [11].

Now we shall use the following information on occurrences of sn to w.
First of all, since w is built as the limit of the iterative construction (1),
for each n, the word w can be written as a product of blocks sn and sn−1.
Following [7], we call this decomposition the n-partition of w. We also use
Lemma 3.3 from the same paper by Damanik and Lenz which we reformulate
as follows.

Proposition 11 ([7]). Consider an occurrence sm = w(r..r + qm] of sm to
w, where m ≥ 0. Then w(0..r] consists of full blocks of the m-partition of w,
and their sequence is completely determined by the symbol w[r].

Proposition 12. Consider an occurrence sm = w(r..r + qm] of sm to w,
where m ≥ 0. Then w(0..r] = skn
n · · · skm
m
for some n ≥ m and appropriate ki ≥ 0.

Proof. If r = 0, the statement is obvious with n = m and km = 0.
For the general case, consider the partition of w(0..r] to blocks equal to sm
and sm−1 which exists due to Proposition 11. Suppose that it ends by k
occurrences of sm preceded by sm−1; we put km = k and use the fact that by
the construction, sm−1 appears in the m-partition only as the end of a block

13

sdm
m sm−1 = sm+1. So, we may pass to the m + 1-partition of w(0..r − kmqm]
and do as before: let this partition end by k occurrences of sm+1; we put
km+1 = k and pass to the m + 2-partition of the remaining preﬁx of w. After
a ﬁnite number of steps, we will see the empty preﬁx, which will terminate
the procedure. □

Proposition 13. Consider an occurrence w(p1..p2] of a palindrome to w
and its maximal palindromic extension w(p1 − d..p2 + d] = cm,j. Then w(p1 −
d..p1] = slm
m slm−1
m−1 · · · sl0
0 and w(p1 − d..p2] = sLm
m sdm−1−lm−1
m−1 · · · sd0−l0
0 for some
Lm ≥ lm and for some 0 ≤ li ≤ di for i = 0, . . . , m − 1.

Proof. First of all, cm,j is a preﬁx of w, and so do its preﬁxes w(p1 − d..p1]
and w(p1 − d..p2]. Let lm be the maximal power of sm such that w(p1 − d..p1]
starts with it: w(p1 − d..p1] = slm
m u. Note that lm ≤ j ≤ dm since d, the
distance before the beginning of the initial palindrome, is less than |cm,j|/2.
Here u is a preﬁx of sm and thus is can be represented as u = slm−1
m−1 · · · sl0
0 ,
where lm−1 · · · l0 is the Ostrowski representation of |u|. So, d = lmlm−1 · · · l0,
which is a legal (and valid) representation. It means that

d = lmqm + lm−1qm−1 + · · · + l0q0.

Due to Proposition 1, we know that cm = sdm−1
m−1 · · · sd0
0 . So, cm,j = sj
msdm−1
m−1 · · · sd0
0 ,
and in particular,
 |cm,j| = jqm + dm−1qm−1 + · · · + d0q0.

The length of w(p1 − d..p2] is |cm,j| − d. Since ln ≤ j and li ≤ di for i < m,
we can just subtract the two previous equalities to get

|w(p1 − d..p2]| = |cm,j| − d = (j − lm)qm + (dm − lm)qm−1 + · · · + (d0 − l0)q0.

So, |w(p1 − d..p2]| = (j − lm)(dm − lm) · · · (d0 − l0) is a legal representation.
Due to Corollary 1, this representation is also valid. Since w(p1 − d..p2] is a
preﬁx of w, this means exactly that

w(p1 − d..p2] = sj−lm
m sdm−1−lm−1
m−1 · · · sd0−l0
0 .

It remains to set Lm = j − lm. □

Proof of Theorem 2. Given a non-empty palindrome w(p1..p2], consider
its maximal palindromic extension w(p1 − d..p2 + d] = cm,j. The word cm,j

14

is not empty, so, the only case when it does not start with sm is c1,0 = a
d0.
In this case, we consider the same word a
d0 as c0,d0 with m = 0. So, we
may assume that cm,j starts with sm and use Proposition 12 to see that
w(0..p1 − d] = skn
n · · · skm
m for some n ≥ m and ki ≥ 0. We can also apply
Proposition 13 and see that w(p1 −d..p1] = slm
m slm−1
m−1 · · · sl0
0 and w(p1 −d..p2] =
sLm
m sdm−1−lm−1
m−1 · · · sd0−l0
0 . Taking the concatenation, we see that

w(0..p1] = skn
n · · · skm+lm
m slm−1
m−1 · · · sl0
0

and w(0..p2] = skn
n · · · skm+Lm
m sdm−1−lm−1
m−1 · · · sd0−l0
0 .

Setting xi = ki for i > m, xi = li for i < m, xm = km + lm and ym = km + Lm,
and using the deﬁnition of a valid representation, we get the statement of
Theorem 2. □

5. Decompositions to palindromes

In this section, we use the tools developed above to prove for Sturmian
words the conjecture on the decomposition to palindromes stated in [12].
Note that on k-power-free inﬁnite words, the conjecture was proved in the
same paper where is was stated. A Sturmian word is k-power-free for some
k if and only if the directive sequence (di) is bounded [15, 3]. So, it remains
to prove

Theorem 3. Consider a characteristic Sturmian word w with an unbounded
directive sequence (di). Then for all Q > 0 there exists a preﬁx of w which
cannot be decomposed to a concatenation of Q palindromes.

To prove the theorem, let us ﬁrst introduce another notion. Given a valid
representation r = xn · · · x0, let us denote by zm(r) the distance between xm
and 0 or dm: zm(r) = min(xm, |dm − xm|).

Note that the transformations ρm and βm can be applied only to representa-
tions r with zm(r) = 0, and do not change zm(r). Note also that Theorem 2
has the following immediate corollary.

Corollary 3. Let w(p1..p2] be a palindrome. Then there exist valid represen-
tations r1 of p1 and r2 of p2 such that zi(r1) = zi(r2) for all i except for one
value i = m.
 15

With this new notion, we state the following corollary of Proposition 8.

Proposition 14. Let r1 and r2 be two valid representations of the same
number N = r1 = r2. Then for all m, we have |zm(r1) − zm(r2)| ≤ 3.

Proof. Proposition 8 means that the statement is true for zm(r1) ≥ 4. Since
the nth symbol of r2 is bounded by dm + 2 by Proposition 3, Proposition 8
also implies that if zm(r1) = 0, we cannot have zm(r2) ≥ 4, completing the
proof. □

Proof of Theorem 3. Since (di) is unbounded, for any given Q > 0,
we can ﬁnd Q + 1 values m0, · · · , mQ such that dmi ≥ 6Q + 2 for each i.
Consider N = xn · · · x0, where xj = 3Q + 1 for n = mi, i = 0, . . . , Q, and
xj = 0 otherwise. This representation of N is legal and thus valid due to
Corollary 1.
Now suppose that the preﬁx w(0..N] can be represented as a concatena-
tion of at most Q palindromes, that is, there exists a sequence

0 = p0 ≤ p1 ≤ p2 · · · ≤ pQ = N

such that for each k = 0, . . . , Q − 1, the word w(pk..pk+1] is a palindrome.
Due to Corollary 3, for eack k = 0, . . . , Q − 1, there exist representations
rk,1 of pk and rk+1,2 of pk+1 such that zi(rk,1) and zi(rk+1,2) diﬀer at most for
one index which we denote by i = ik. Note also that 0 admits essentially
only one valid representation consisting of zeros (or empty, if we get rid of
leading zeros). For the sake of completeness, we denote the representation
xn · · · x0 of N by rQ,1.
Due to Proposition 14, for each digit m, we have |zm(rk,1) − zm(rk,2)| ≤ 3.
So, the representation N = rQ,1 = xn · · · x0, containing Q + 1 digits mi
equal to 3Q + 1, with the distance zmi(rQ,1) = 3Q + 1, is obtained from
the representation 0 = 0 · · · 0 by a series of Q steps. At each step, ﬁrst a
palindrome number k (here k = 0, . . . , Q − 1) may suﬃciently change exactly
one distance zik (r) when we pass from the rk,1 to rk+1,2. Then each distance
zi(r) changes at most by 3 when we pass from rk+1,2 to rk+1,1 (and pass from
k to k + 1).
We see that after Q steps of this kind, we can only have Q digits in the
representation such that the distance z for them is greater than 3Q. At the
same time, in the starting representation N = xn · · · x0 such digits are Q + 1.
A contradiction. □

16

Remark 2. The preﬁx of length N of a characteristic Sturmian word is a
factor of any Sturmian word of the same slope. So, due to the Saarela’s result
[17] stating the equivalence of the preﬁx and the factor versions of Conjecture
1, we have completed the proof of the conjecture for any Sturmian word.

6. Acknowledgement

I am deeply grateful to Srecko Brlek and all the organizers of WORDS
2017 whose kind invitation inspired me to return to the topic.

References

References

[1] J.-P. Allouche, J. Shallit. Automatic Sequences: Theory, Applications,
Generalizations. Cambridge University Press, 2003.

[2] J. Berstel. An exercise on Fibonacci representations. Theor. Inform.
Appl. 35 (2002) 491–498.

[3] J. Berstel. On the index of Sturmian words. In: J. Karhum¨aki, H. A.
Maurer, G. Paun, G. Rozenberg, Eds, Jewels are Forever, Contributions
on Theoretical Computer Science in Honor of Arto Salomaa. Springer,
1999. pp. 287–294.

[4] J. Berstel, P. S´e´ebold. Sturmian words. In: M. Lothaire, Algebraic com-
binatorics on words. Cambridge University Press, 2002. Chapter 2, pp.
45–110.

[5] V. Berth´e. Autour du syst`eme de num´eration d’Ostrowski. Bull. Belg.
Math. Soc. Simon Stevin 8 (2001) 209–239.

[6] M. Bucci, G. Richomme. Greedy palindromic lengths, arXiv:1606.05660,
2016.

[7] D. Damanik, D. Lenz. The index of Sturmian sequences. Europ. J. Com-
binatorics 23 (2002), 23–29.

[8] A. de Luca, A. De Luca. Palindromes in Sturmian words. Proc. DLT
2005, LNCS V. 3572, Springer (2005) 199–208.

17

[9] A. de Luca, F. Mignosi. Some combinatorial properties of Sturmian
words. Theoret. Comput. Sci. 136 (1994) 361–385.

[10] C. Epifanio, C. Frougny, A. Gabriele, F. Mignosi, J. Shallit. Sturmian
graphs and integer representations over numeration systems. Discrete
Appl. Math. 160 (2012) 536–547.

[11] G. Fici. On the Structure of Bispecial Sturmian Words. J. Comput. Syst.
Sci. 80 (2014), 711–719.

[12] A. Frid, S. Puzynina, L. Zamboni. On palindromic factorization of
words. Advances in Appl. Math. 50 (2013) 737–748.

[13] A. Glen. Occurrences of palindromes in characteristic Sturmian words.
Theoret. Comput. Sci. 352 (2006) 31–46.

[14] C. G. Lekkerkerker. Voorstelling van natuurlijke getallen door een som
van getallen van Fibonacci. Simon Stevin 29 (1952) 190–195.

[15] F. Mignosi. On the number of factors of Sturmian words. Theoret. Com-
put. Sci. 82 (1991) 71–84.

[16] A. Ostrowski. Bemerkungen zur Theorie der diophantischen Approxi-
mationen. Hamb. Abh. 1 (1921) 77–98.

[17] A. Saarela. Palindromic length in free monoids and free groups. Proc.
WORDS 2017, LNCS V. 10432, Springer (2017) 203–213.

[18] E. Zeckendorf. Repr´esentation des nombres naturels par une somme de
nombres de Fibonacci ou de nombres de Lucas. Bull. Soc. R. Sci. Li`ege
41 (1972) 179–182.
 18
