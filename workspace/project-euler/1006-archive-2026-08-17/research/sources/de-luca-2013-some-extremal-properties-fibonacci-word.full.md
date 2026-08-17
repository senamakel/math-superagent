<!-- source: https://arxiv.org/pdf/1209.3927 | converted from PDF -->

arXiv:1209.3927v1  [cs.DM]  18 Sep 2012
Some extremal properties of the Fibonacci word

Aldo de Luca

Dipartimento di Matematica e Applicazioni “R. Caccioppoli”

Universit`a degli Studi di Napoli Federico II

Via Cintia, Monte S. Angelo, I-80126 Napoli, Italy

June 20, 2018

Abstract

We prove that the Fibonacci word f satisﬁes among all character-
istic Sturmian words, three interesting extremal properties. The ﬁrst
concerns the length and the second the minimal period of its palin-
dromic preﬁxes. Each of these two properties characterizes f up to
a renaming of its letters. A third property concerns the number of
occurrences of the letter b in its palindromic preﬁxes. It characterizes
uniquely f among all characteristic Sturmian words having the preﬁx
abaa.

Keywords. Fibonacci word, Sturmian words, Characteristic words,
Central words, Standard words, Christoﬀel words, Continuants

1 Introduction

Words are ﬁnite or inﬁnite sequences of elements, called letters, taken from
a ﬁnite set called alphabet. In the combinatorics of inﬁnite words the Fi-
bonacci word is very famous since it satisﬁes a great number of beautiful
properties which are of a paramount interest both from the theoretical and
the applicative point of view.
As is well known, the Fibonacci word f can be deﬁned in several diﬀerent
ways. For instance, f is the ﬁxed point ϕω(a) of the Fibonacci morphism
ϕ : {a, b}∗ → {a, b}∗ deﬁned by ϕ(a) = ab and ϕ(b) = a. The name
Fibonacci given to f is due to the fact that f is the limit sequence of the
inﬁnite sequence (fn)n≥−1 of ﬁnite words recursively deﬁned as

f−1 = b, f0 = a, and fn+1 = fnfn−1 for n ≥ 0.

For any n ≥ −1 one has |fn| = Fn where (Fn)n≥−1 is the Fibonacci numerical
sequence:
 F−1 = F0 = 1 and Fn+1 = Fn + Fn−1 for n ≥ 0.

1

The Fibonacci word is a paradigmatic example of Sturmian word. As
is well known, Sturmian words are inﬁnite words over a binary alphabet
of great interest in combinatorics on words for the many applications in
Algebra, Number theory, Physics, and Computer Science.
Several diﬀerent but equivalent deﬁnitions of Sturmian words exist (see,
for instance, [23, Chap. 2]). A Sturmian word can be deﬁned in a purely
combinatorial way as an inﬁnite sequence of letters such that for any integer
n ≥ 0, the number of its distinct factors of length n is n+1. This is equivalent
to say that an inﬁnite word is Sturmian if and only if it is aperiodic and for
any n it has the minimal possible of distinct factors of length n.
A geometrical deﬁnition is the following: a Sturmian word is an inﬁnite
word associated to the sequence of the cuts (cutting sequence) in a squared-
lattice made by a semi-line having a slope which is an irrational number. A
horizontal cut is denoted by the letter b, a vertical cut by a and a cut with a
corner by ab or ba. Sturmian words represented by a semi-line starting from
the origin are usually called characteristic, or standard. For any Sturmian
word there exists a characteristic Sturmian word having the same set of
factors. The Fibonacci word is the characteristic Sturmian word having a
slope equal to the golden ratio g = √5−1
2 .
In many cases, the Fibonacci word f satisﬁes among all inﬁnite words
of a given class, some extremal properties in the sense that some quantity is
maximal or minimal for f (see, for instance [5, 6, 9, 25], and the overview [7]).
A special case of great interest is when the class of inﬁnite words is formed
by all characteristic Sturmian words and the extremal property is satisﬁed
only by the Fibonacci word f and by E(f ), where E is the automorphism of
{a, b}∗ interchanging the letter a with the letter b. In this way one obtains
a characterization of f , up to a renaming of the letters, inside the class of
characteristic Sturmian words.
Some of these latter extremal properties are strictly related to a simple
construction of characteristic Sturmian words, due to the author [10]. It
is based on an operator deﬁnable in any free monoid A∗ and called right-
palindromic closure, which associates to each word w ∈ A∗ the shortest
palindrome of A∗ having w as a preﬁx. Any given word v ∈ A∗ can suitably
‘direct’ subsequent iterations of the preceding operator according to the
sequence of letters in v as follows: at each step, one concatenates the next
letter of v to the right of the already constructed palindrome and then takes
the right palindromic closure. Thus starting with any directive word v one
generates a palindrome ψ(v). The map ψ, called palindromization map, is
injective; the word v is called the directive word of ψ(v).
Since for any u, v ∈ A∗, ψ(uv) has ψ(u) as a preﬁx, one can extend the
map ψ to right inﬁnite words x ∈ Aω producing an inﬁnite word ψ(x). It
has been proved in [10] that in the case of a binary alphabet A = {a, b}
if each letter of A occurs inﬁnitely often in x, then one can generate all

2

characteristic Sturmian words1. Moreover, ψ(A∗) coincides with the set of
the palindromic preﬁxes of all characteristic Sturmian words. These words
can be also deﬁned in a purely combinatorial way by an extremal property
closely related to Fine and Wilf’s periodicity theorem [17]; they are usually
c! alled also central words since they play a central role in Sturmian words
theory. In Section 3 some remarkable structural properties of central words
relating them to ﬁnite standard words and to Christoﬀel words are brieﬂy
presented.
A central word is of order n if its directive word is of length n. In [6]
we proved that the Fibonacci word f = ψ((ab)ω) is the only characteristic
Sturmian word, up to a renaming of the letters, whose palindromic preﬁxes
w of any order are harmonic, that is the minimal period π(w) of w satisﬁes
the condition π2(w) ≡ ±1 (mod |w| + 2).
The main results of the paper are three theorems (cf. Theorems 4.4, 4.7,
and 4.11), somehow related to each other, showing the following extremal
properties of f . Theorem 4.4 states that a characteristic Sturmian word s
has the palindromic preﬁxes of any order of maximal length if and only if
s = f or s = E(f ), where E is the automorphism of {a, b}∗ interchanging the
letter a with b. Similarly, Theorem 4.7 states that, up to a renaming of the
letters, the Fibonacci word is the only characteristic Sturmian word whose
palindromic preﬁxes of any order have a maximum value of the minimal
period. Theorem 4.11 shows that a characteristic Sturmian word beginning
with the letter a has the palindromic preﬁxes of any order with the maximal
number of occurrences of the letter b if and only if s = f or s has the directive
word (ab2)(ab)ω. Hence, this extremal property characterizes uniquely f
among all characteristic Sturmian words having the preﬁx abaa.
The proof of these theorems is given in Section 4 by using techniques of
combinatorics on words and three extremal properties of central words which
are preﬁxes of the Fibonacci word concerning their length (cf. Theorem 4.1),
their minimal period (cf. Theorem 4.5), and the number of occurrences of
the letter b (cf. Theorem 4.9).
In Section 5 we consider the arithmetization of Sturmian words theory
obtained by representing the directive words of central words, as well as of
characteristic Sturmian words, by sequences of integers (integral represen-
tations). In this setting continued fractions and continuants associated to
these numerical sequences play a relevant role. We show that Theorem 4.1
is equivalent to a property of continuants (cf. Theorem 5.4) and a direct
proof of this latter result is also given. Moreover, we show that also Theo-
rem 4.5 can be derived from Theorem 5.4 by using a suitable expression of

1The palindromization map ψ has been extended to inﬁnite words over an arbitrary
alphabet A by X. Droubay, J. Justin, and G. Pirillo in [16], where the family of standard
episturmian words over A has been introduced. Some further extensions and generaliza-
tions of ψ are in [12, 13]. An extension of ψ to free group F2 was given by C. Reutenauer
in [20].
 3

the minimal periods of central words in terms of continuants.

2 Preliminaries

2.1 Notation and preliminary deﬁnitions

In the following A will denote a binary alphabet A = {a, b} and A∗ the
free monoid generated by A. The elements a and b of A are usually called
letters and those of A∗ words. We suppose that A is totally ordered by
setting a < b. The identity element of A∗ is called empty word and denoted
by ε. We set A+ = A∗ \ {ε}.
A word w ∈ A+ can be written uniquely as a sequence of letters w =
w1w2 · · · wn, with wi ∈ A, 1 ≤ i ≤ n, n > 0. The integer n is called the
length of w and denoted |w|. The length of ε is taken equal to 0. For any
w ∈ A∗ and x ∈ A, |w|x denotes the number of occurrences of the letter x
in w. For any w ∈ A∗, alph w will denote the set of all distinct letters of A
occurring in w.
We consider the map η : A∗ → Q ∪ {∞} deﬁned by

η(ε) = 1 and η(w) = |w|b
|w|a for w ̸= ε.

If |w|a = 0 and w ̸= ε, we assume η(w) = |w|b
0 = ∞. For any w ∈ A∗, η(w)
is called the slope of w.
Let w ∈ A∗. The word u is a factor of w if there exist words r and s
such that w = rus. A factor u of w is called proper if u ̸= w. If w = us,
for some word s (resp., w = ru, for some word r), then u is called a preﬁx
(resp., a suﬃx ) of w.
Let p be a positive integer. A word w = w1 · · · wn, wi ∈ A, 1 ≤ i ≤ n,
has period p if the following condition is satisﬁed: for any integers i and j
such that 1 ≤ i, j ≤ n,

if i ≡ j (mod p), then wi = wj.

Let us observe that if a word w has a period p, then any non-empty factor
of w has also the period p. We shall denote by π(w) the minimal period of
w. Conventionally, we set π(ε) = 1.
We recall the following important periodicity theorem due to Fine and
Wilf [17]: If a word w has two periods p and q and |w| ≥ p + q − gcd(p, q),
then w admits the period gcd(p, q).
Let w = w1 · · · wn, wi ∈ A, 1 ≤ i ≤ n. The reversal, or mirror image, of
w is the word w∼ = wn · · · w1. One deﬁnes also ε∼ = ε. A word is called
palindrome if it is equal to its reversal. We shall denote by PAL the set of
all palindromes on the alphabet A.
 4

A right-inﬁnite word x, or simply inﬁnite word, over the alphabet A is
just an inﬁnite sequence of letters:

x = x1x2 · · · xn · · · where xi ∈ A, for all i ≥ 1 .

For any integer n ≥ 0, x[n] will denote the preﬁx x1x2 · · · xn of x of length n.
A factor of x is either the empty word or any sequence xi · · · xj with i ≤ j.
The set of all inﬁnite words over A is denoted by Aω.
For all deﬁnitions and notation concerning words not explicitly given in
the paper, the reader is referred to the book of M. Lothaire [22]; for Sturmian
words see [23, Chap. 2].

2.2 The palindromization map

We introduce in A∗ the operator (+) : A∗ → PAL which maps any word
w ∈ A∗ into the palindrome w(+) deﬁned as the shortest palindrome having
the preﬁx w (cf. [10]). We call w(+) the right palindromic closure of w. If
Q is the longest palindromic suﬃx of w = uQ, then one has

w(+) = uQu
∼ .

Let us now deﬁne the map
 ψ : A∗ → PAL,

called right iterated palindromic closure, or simply palindromization map, as
follows: ψ(ε) = ε and for all v ∈ A∗, x ∈ A,

ψ(vx) = (ψ(v)x)
(+) .

Example 2.1. Let v = ab2a. One has ψ(a) = a, ψ(ab) = (ab)(+) = aba,
ψ(ab2) = ababa, and ψ(v) = (ababaa)(+) = ababaababa.

The following proposition summarizes some noteworthy properties of the
palindromization map (cf., for instance [10, 16]):

Proposition 2.2. The palindromization map ψ satisﬁes the following prop-
erties:

P1. The palindromization map is injective.

P2. If u is a preﬁx of v, then ψ(u) is a palindromic preﬁx (and suﬃx) of
ψ(v).

P3. If p is a preﬁx of ψ(v), then p(+) is a preﬁx of ψ(v).

P4. Every palindromic preﬁx of ψ(v) is of the form ψ(u) for some preﬁx u
of v.
 5

P5. The palindromization map ψ commute with the automorphism E of
A∗ deﬁned by E(a) = b and E(b) = a, i.e., ψ ◦ E = E ◦ ψ.

P6. For every v ∈ A∗, |ψ(v)| = |ψ(v∼)|.

For any w ∈ ψ(A∗) the unique word v such that ψ(v) = w is called the
directive word of w. The directive word v of w = ψ(v) can be read from
w just by taking the subsequence of w formed by all letters immediately
following all proper palindromic preﬁxes of w.
For any x ∈ A let µx denote the injective endomorphism of A∗

µx : A∗ → A∗

deﬁned by µx(x) = x, µx(y) = xy, for y ∈ A \ {x}. (1)

If v = x1x2 · · · xn, with xi ∈ A, i = 1, . . . , n, then we set:

µv = µx1 ◦ · · · ◦ µxn;

moreover, if v = ε, µε= id.
The following interesting theorem, proved by J. Justin [19] in the case of
an arbitrary alphabet, relates the palindromization map to morphisms µv.

Theorem 2.3. For all v, u ∈ A∗,

ψ(vu) = µv(ψ(u))ψ(v).

In particular, if x ∈ A, one has:

ψ(xu) = µx(ψ(u))x and ψ(vx) = µv(x)ψ(v).

Example 2.4. Let v = ab2a. One has (see Example 2.1) ψ(v) = ababaababa
and ψ(av) = µa(ψ(v))a = aabaabaaabaabaa.

One can extend ψ to Aω as follows: let x ∈ Aω be an inﬁnite word

x = x1x2 · · · xn · · · , xi ∈ A, i ≥ 1.

Since by property P2 of Proposition 2.2 for all n, ψ(x[n]) is a proper preﬁx
of ψ(x[n+1]), we can deﬁne the inﬁnite word ψ(x) as:

ψ(x) = lim
n→∞ ψ(x[n]).

The extended map ψ : Aω → Aω is injective. The word x is called the
directive word of ψ(x). It has been proved in [10] that the word ψ(x) is a
characteristic Sturmian word if and only if both the letters a and b occur
inﬁnitely often in the directive word x. From property P4 of Proposition 2.2
one easily derives that ψ(A∗) is equal to the set of the palindromic preﬁxes
of all characteristic Sturmian words.

Example 2.5. Let A = {a, b}. If x = (ab)ω, then the characteristic Stur-
mian word ψ((ab)ω) having the directive word x is the Fibonacci word

f = abaababaabaababaababaabaa · · ·

6

3 Central, standard, and Christoﬀel words

In this section we consider three noteworthy classes of ﬁnite words called
central, standard, and Christoﬀel words which are closely interrelated and
are very important in the combinatorics of Sturmian words as they satisfy
remarkable structural properties and, moreover, can be regarded as a ﬁnite
counterpart of Sturmian sequences.
A word w is called central if w has two periods p and q such that
gcd(p, q) = 1 and |w| = p + q − 2. Thus a word is central if it is a power
of a single letter or is a word of maximal length for which the theorem of
Fine and Wilf does not apply. The set of central words, usually denoted by
PER, was introduced in [14] where its main properties were studied. It has
been proved that PER is equal to the set of the palindromic preﬁxes of all
characteristic Sturmian words, i.e.,

PER = ψ(A∗).

The term central was given by J. Berstel and P. S´e´ebold in [23, Chap. 2] to
emphasize the central role that these words play in Sturmian words theory.
We say that a central word w is of order n if its directive word has length
n. As proved in [14] the number of central words of order n is φ(n + 2)
where φ is the totient Euler function. The following remarkable structural
characterization of central words holds [10, 6]:

Proposition 3.1. A word w is central if and only if w is a power of a single
letter of A or it satisﬁes the equation:

w = w1abw2 = w2baw1

with w1, w2 ∈ A∗. Moreover, in this latter case, w1 and w2 are uniquely
determined central words, p = |w1| + 2 and q = |w2| + 2 are coprime periods
of w, and min{p, q} is the minimal period of w.

Another important family of ﬁnite words, strictly related to central
words, is the class of ﬁnite standard words. In fact, characteristic Sturmian
words can be equivalently deﬁned in the following way. Let c1, . . . , cn, . . . be
any sequence of integers such that c1 ≥ 0 and ci > 0 for i > 1. We deﬁne,
inductively, the sequence of words (sn)n≥−1, where

s−1 = b, s0 = a, and sn = scn
n−1sn−2 for n ≥ 1 .

Since for any n ≥ 0, sn is a proper preﬁx of sn+1, the sequence (sn)n≥−1
converges to a limit s which is a characteristic Sturmian word (cf. [23]).
Any characteristic Sturmian word is obtained in this way. The sequence
(c1, c2, . . . , cn, . . .) is called the directive numerical sequence of s. The Fi-
bonacci word is obtained when ci = 1 for i ≥ 1.

7

We shall denote by Stand the set of all the words sn, n ≥ −1 of any
sequence (sn)n≥−1. Any word of Stand is called ﬁnite standard word, or
simply standard word.
The following remarkable relation existing between standard and central
words, has been proved in [14]:

Stand = A ∪ PER{ab, ba}.

More precisely, the following holds (see, for instance [11, Propositions 4.9
and 4.10]):

Proposition 3.2. Any standard word diﬀerent from a single letter can be
uniquely expressed as µv(xy) with {x, y} = {a, b} and v ∈ A∗. Moreover,
one has: µv(xy) = ψ(v)xy.

Let us set for any v ∈ A∗ and x ∈ A, px(v) = |µv(x)|. From Justin’s
formula one derives (see, for instance, [15]) that px(v) is the minimal pe-
riod of ψ(vx) and then a period of ψ(v). Moreover, px(v) = π(ψ(v)x),
gcd(px(v), py(v)) = 1,
 π(ψ(v)) = min{px(v), py(v)}, (2)

and from Proposition 3.2,

|ψ(v)| = px(v) + py(v) − 2.

Let us now recall the important notion of Christoﬀel word [8] (see also [2,
3]). Let p and q be positive relatively prime integers such that n = p + q.
The Christoﬀel word w of slope p
q is deﬁned as w = x1 · · · xn with

xi = { a if ip mod n > (i − 1)p mod n
b if ip mod n < (i − 1)p mod n

for i = 1, . . . , n where k mod n denotes the remainder of the Euclidean
division of k by n. The term slope given to the irreducible fraction p
q is
due to the fact that, as one easily derives from the deﬁnition, p = |w|b and
q = |w|a. The words a and b are also Christoﬀel words with a respective
slope 0
1 and 1
0 . The Christoﬀel words of slope p
q with p and q positive integers
are called proper Christoﬀel words.
Let us denote by CH the class of Christoﬀel words. The following im-
portant result, proved in [1], shows a basic relation existing between central
and Christoﬀel words: CH = a PER b ∪ A.

Hence, there exists a simple bijection of the set of central words onto the set
of proper Christoﬀel words. Any proper Christoﬀel word w can be uniquely
represented as aψ(v)b for a suitable v ∈ A∗.

8

Let <lex denote the lexicographic order of A∗ and let Lynd be the set of
Lyndon words [22] of A∗ and St be the set of (ﬁnite) factors of all Sturmian
words. The following theorem summarizes some results on Christoﬀel words
proved in [4, 1, 3, 15].

Theorem 3.3. Let w = aψ(v)b with v ∈ A∗ be a proper Christoﬀel word.
Then the following hold:

1. CH = St ∩ Lynd, i.e., CH equals the set of all factors of Sturmian
words which are Lyndon words.

2. There exist and are unique two Christoﬀel words w1 and w2 such that
w = w1w2. Moreover, w1 <lex w2, and (w1, w2) is the standard fac-
torization of w in Lyndon words.

3. If w has the slope η(w) = p
q , then |w1| = p′, |w2| = q′, where p′

and q′ are the respective multiplicative inverse of p and q (mod |w|).
Moreover, p′ = pa(v), q′ = pb(v) and p = pa(v∼), q = pb(v∼).

Example 3.4. The Christoﬀel word having slope 5
12 is

w = aaabaabaaabaabaab = aub,

where u = aabaabaaabaabaa = ψ(a2b2a) is the central word of length 15
having the two coprime periods 7 = pa(v) and 10 = pb(v) with v = a2b2a.
The word w can be uniquely factorized as w = w1w2, where w1 and w2 are
the Lyndon words w1 = aaabaab and w2 = aaabaabaab. One has w1 <lex w2
with |w1| = 7 = pa(v) and |w2| = 10 = pb(v). Moreover, w2 is the proper
suﬃx of w of maximal length which is a Lyndon word. Finally, ψ(v∼) =
ψ(ab2a2) = ababaababaababa, pa(v∼) = 5 = |w|b, pb(v∼) = 12 = |w|a and
|w|bpa(v) = 5.7 = 35 ≡ |w|apb(v) = 12.10 = 120 ≡ 1 mod 17.

4 The Fibonacci word

The Fibonacci word f is without doubt the most famous characteristic Stur-
mian word. As is well known it can be constructed in several diﬀerents ways.
As we have seen is Section 2.2, f can be generated by the palindromization
map ψ from the directive word x = (ab)ω, i.e., f = ψ(x). In the following
we set for any n ≥ 0 v(n) = x1 · · · xn = x[n],

so that v(0) = ε, v(1) = a,

v(n) = (ab) n
2 if n is even, and v(n) = (ab)
⌊ n
2 ⌋a if n is odd.

9

Theorem 4.1. Let n ≥ 0. For any v ∈ An one has:

|ψ(v)| ≤ |ψ(v(n))|,

where the equality holds if and only if

v = v(n) or v = E(v(n)).

Proof. The proof is by induction on the length n of v. The result is trivially
true for n ≤ 1. For n = 2 the result is also true since |ψ(aa)| = |ψ(bb)| = 2,
whereas |ψ(ab)| = |ψ(ba)| = 3. Let us then suppose that the result is
achieved up to the length n ≥ 2 and prove it for the length n + 1.
We can write v(n+1) = v(n)z with z = a if n is even and z = b, otherwise.
By Justin’s formula (cf. Theorem 2.3) one has:

ψ(v(n+1)) = ψ(v(n)z) = µv(n)(z)ψ(v(n)). (3)

From the deﬁnition v(n) = v(n−1) ¯z having set ¯z = E(z). Thus, since by (1)
µ¯z(z) = ¯zz, from Proposition 3.2 one has

µv(n)(z) = (µv(n−1) ◦ µ¯z)(z) = µv(n−1) (¯zz) = ψ(v(n−1))¯zz

and replacing in (3), one derives:

ψ(v(n+1)) = ψ(v(n−1))¯zzψ(v(n)). (4)

Let v ∈ An+1 and write v = uy with u ∈ An and y ∈ A. One has by Justin’s
formula: ψ(v) = ψ(uy) = µu(y)ψ(u). (5)

If v ∈ y∗, i.e., v = yn+1, then ψ(v) = yn+1. In this case we are done
since for n ≥ 1, |ψ(v)| = n + 1 < |ψ(v(n+1))| (cf. Lemma 4.2). Let us then
suppose that card(alph v) = 2. We can write u = u′ ¯yζ with ζ ∈ y∗ and
u′ ∈ A∗. From (5) and Proposition 3.2 one has, since µζ(y) = y,

ψ(v) = µu′ ¯y(y)ψ(u) = (µu′ ◦ µ¯y)(y)ψ(u) = µu′(¯yy)ψ(u) = ψ(u′)¯yyψ(u).

From (4) and the preceding equation it follows:

|ψ(v(n+1))| − |ψ(v)| = (|ψ(v(n))| − |ψ(u)|) + (|ψ(v(n−1))| − |ψ(u′)|). (6)

Setting k = |u′| ≤ n − 1 one has |ψ(v(n−1))| ≥ |ψ(v(k))|, so that

|ψ(v(n+1))| − |ψ(v)| ≥ (|ψ(v(n))| − |ψ(u)|) + (|ψ(v(k))| − |ψ(u′)|).

By induction, |ψ(v(n))| ≥ |ψ(u)| and |ψ(v(k))| ≥ |ψ(u′)| that implies

|ψ(v(n+1))| ≥ |ψ(v)|,

10

which proves the ﬁrst part of theorem.
If v = v(n+1) or v = E(v(n+1)), then |ψ(v)| = |ψ(v(n+1))|. Indeed,
one has only to observe that in view of property P5 of Proposition 2.2,
ψ(E(v(n+1))) = E(ψ(v(n+1))), so that |ψ(E(v(n+1)))| = |ψ(v(n+1))|.
Conversely, let us suppose that |ψ(v)| = |ψ(v(n+1))|. From (6) one de-
rives: |ψ(v(n))| = |ψ(u)| and |ψ(v(n−1))| = |ψ(u′)|. (7)

From equation (7)2 one obtains k = |u′| = n − 1. Indeed, if k < n − 1 one
would have: |ψ(v(n−1))| > |ψ(v(k))| ≥ |ψ(u′)|, a contradiction. Hence, from
(7)2 one has u = u′ ¯y and v = uy = u′ ¯yy.
By induction (7) is satisﬁed if and only if

a) u = v(n) or b) u = E(v(n))

and c) u
′ = v(n−1) or d) u′ = E(v(n−1)).

Since u′ is a non-empty preﬁx of u, condition a) & d), as well as b) & c), is a
contradiction. Indeed, u′ would begin with the letter a and with the letter
b. Thus (7) is satisﬁed if and only if

u = v(n) and u′ = v(n−1)

or u = E(v(n)) and u′ = E(v(n−1)).

In the ﬁrst case one has:

v(n+1) = v(n)z = uz = v(n−1) ¯zz.

Moreover, u = u′ ¯y = v(n−1) ¯y, so that

v(n+1) = uz = v(n−1) ¯yz.

Hence, y = z and v = uy = uz = v(n+1).

In the second case one has:

v = uy = u
′ ¯yy = E(v(n−1))¯yy = E(v(n))y.

Thus E(v(n)) = E(v(n−1))¯y = E(v(n−1)y), so that v(n) = v(n−1)y. Since
v(n+1) = v(n)z, one derives: v(n+1) = v(n−1)yz. This implies z = ¯y and

v = E(v(n))y = E(v(n+1)),

which concludes our proof.
 11

Lemma 4.2. Let (Fn)n≥−1 be the Fibonacci numerical sequence. For all
n ≥ 0 one has: |ψ(v(n))| = Fn+1 − 2.

Proof. The result is trivial for n ≤ 1. Indeed, for n = 0 one has |ψ(ε)| = 0
and F1 = 2. For n = 1, |ψ(a)| = 1 and F2 = 3. Suppose by induction the
result true up to n and prove it for n + 1. By (4) one has:

|ψ(v(n+1))| = |ψ(v(n−1))| + |ψ(v(n))| + 2.

Since by induction |ψ(v(n−1))| = Fn − 2 and |ψ(v(n))| = Fn+1 − 2, the result
follows.

Corollary 4.3. Let n ≥ 0. For any v ∈ An one has:

|ψ(v)| ≤ Fn+1 − 2,

where the equality holds if and only if

v = v(n) or v = E(v(n)).

Proof. Immediate from Theorem 4.1 and Lemma 4.2.

Let us recall (cf., Section 3) that a palindromic preﬁx of a characteristic
Sturmian word is of order n if its directive word is of length n. From
Theorem 4.1 the following extremal property of the Fibonacci word holds:

Theorem 4.4. A characteristic Sturmian word s has the palindromic pre-
ﬁxes of any order of maximal length if and only if s = f or s = E(f ).

Proof. Let s = ψ(y), with y = y1 · · · yn · · · , yi ∈ A, i ≥ 1, be any character-
istic Sturmian word. By Theorem 4.1 for any n ≥ 0,

|ψ(y1 · · · yn)| ≤ |ψ(v(n))| = |ψ(E(v(n)))|,

where v(n) and E(v(n)) are respectively the preﬁxes of (ab)ω and of (ba)ω

of length n. Since ψ(v(n)) and E(ψ(v(n))) are respectively the palindromic
preﬁxes of order n of f and of E(f ), the ‘if part’ of theorem follows.
Let now s = ψ(y) be any characteristic Sturmian word such that for any
n and v ∈ An, |ψ(y1 · · · yn)| ≥ |ψ(v)|. In particular, one has |ψ(y1 · · · yn)| ≥
|ψ(v(n))|. By Theorem 4.1 it follows that for any n ≥ 0

|ψ(y1 · · · yn)| = |ψ(v(n))|.

Moreover, the equality occurs if and only if y1 · · · yn = v(n) or y1 · · · yn =
E(v(n)). Since for n > 0, v(n) begins with the letter a and E(v(n)) begins
with the letter b, it follows that either for any n ≥ 0, y1 · · · yn = v(n) or for
any n ≥ 0, y1 · · · yn = E(v(n)), i.e., s = f or s = E(f ), which concludes the
proof.
 12

Let us introduce in A∗ the operator c deﬁned as: c(ε) = ε, c(x) = x for
any x ∈ A, and for v = uxy with u ∈ A∗, x, y ∈ A, c(v) = c(uxy) = uyx.
Thus the operator c acting on words v of length ≥ 2 changes the suﬃx xy
of v of length 2 in yx. Note that if x ̸= y, then c(uxy) = u¯x¯y. For instance,
c(abbaba) = abbaab. It is ready veriﬁed that the operator c commutes with
E, i.e., c ◦ E = E ◦ c.
The following theorem concerns the minimal periods of the central words
having a directive word of any length.

Theorem 4.5. For any n ≥ 0 and v ∈ An,

π(ψ(v)) ≤ π(ψ(v(n))) = Fn−1,

where the maximum is reached if and only if v is one of the following words:

v(n), E(v(n)), c(v(n)), and E(c(v(n))).

Proof. The result is trivial for n = 0. We ﬁrst prove that for any n ≥ 0
π(ψ(v(n+1))) = Fn. Indeed, setting v(n+1) = v(n)z with z ∈ A one has, in
view of (4),

ψ(v(n+1)) = ψ(v(n−1))¯zzψ(v(n)) = ψ(v(n))z¯zψ(v(n−1)).

From Proposition 3.1 and Lemma 4.2, one has:

π(ψ(v(n+1))) = min{|ψ(v(n−1))| + 2, |ψ(v(n))|) + 2} = |ψ(v(n−1))| + 2 = Fn.

We prove now that for any v ∈ An+1, π(ψ(v)) ≤ π(ψ(v(n+1))) = Fn.
Indeed, we can write v = uy with u ∈ An and y ∈ A. If u = yn, then
v = yn+1 and ψ(yn+1) = yn+1 that implies π(yn+1) = 1 ≤ Fn. Let us then
suppose card(alph v) = 2. As we have seen in the proof of Theorem 4.1, we
can write u = u′ ¯yζ with ζ ∈ y∗ and u′ ∈ A∗ having:

ψ(v) = ψ(u′)¯yyψ(u).

From Proposition 3.1, as |ψ(u′)| < |ψ(u)|, one has

π(ψ(v)) = |ψ(u′)| + 2. (8)

By Theorem 4.1 and Lemma 4.2, |ψ(u′)| ≤ |ψ(v(|u′|))| = F|u′|+1 − 2. Since
|u′| ≤ n − 1 it follows |ψ(u′)| ≤ Fn − 2. Hence, from (8) one obtains that for
all v ∈ An+1, π(ψ(v)) ≤ Fn = π(ψ(v(n+1))), and the ﬁrst part of theorem is
proved.
As regards the second part, the result is trivial for n ≤ 1. We shall sup-
pose n > 1 and prove that for v ∈ An+1, n ≥ 1, the maximal value of π(ψ(v))
is reached if and only if v is one of the following words v(n+1), E(v(n+1)),
c(v(n+1)), and E(c(v(n+1))).
 13

For what concerns the ‘if part’ of the statement we have proved above
that π(ψ(v(n+1))) = π(E(ψ(v(n+1)))) = π(ψ(E(v(n+1)))) = Fn. Let us now
prove that π(ψ(v(n+1))) = π(ψ(c(v(n+1)))).

Since v(n+1) = v(n)z = v(n−1) ¯zz, one has c(v(n+1)) = v(n−1)z¯z. From
Justin’s formula one derives:

ψ(c(v(n+1))) = ψ(v(n−1)z¯z) = µv(n−1) (z¯z)ψ(v(n−1)z).

By Proposition 3.2, µv(n−1)(z¯z) = ψ(v(n−1))z¯z, so that

ψ(c(v(n+1))) = ψ(v(n−1))z¯zψ(v(n−1)z).

From Proposition 3.1 and Lemma 4.2, π(ψ(c(v(n+1)))) = |ψ(v(n−1))| + 2 =
Fn = π(ψ(v(n+1))).
Let us now prove the ‘only if part’. We suppose that v ∈ An+1 is such
that π(ψ(v)) = π(ψ(v(n+1))) = Fn. This implies by (8),

|ψ(u′)| = Fn − 2 and |u′| = n − 1.

By Theorem 4.1 this can occur if and only if

u
′ = v(n−1) or u′ = E(v(n−1)).

Let us recall that v(n+1) = v(n−1) ¯zz and v = u′ ¯yy. Suppose ﬁrst u′ =
v(n−1). If y = z, we have v = v(n−1) ¯zz = v(n+1). If y = ¯z, then one
has v = v(n−1)z¯z = c(v(n+1)). In the case u′ = E(v(n−1)) one has v =
E(v(n−1))¯yy. If y = ¯z, then v = E(v(n−1) ¯zz) = E(v(n+1)). If y = z, then
v = E(v(n−1)z¯z) = E(c(v(n+1))), which concludes the proof.

Example 4.6. For n = 4 the maximum value of the minimal period of
central words of order 4 is 5 = F3. It is reached with the directive words
abab, abba, baba, and baab. The corresponding central words are respec-
tively, ψ(abab) = abaababaaba, ψ(abba) = ababaababa, E(ψ(abab)), and
E(ψ(abba)).

Theorem 4.7. The minimal periods of the palindromic preﬁxes of any order
of a characteristic Sturmian word s are maximal if and only if s = f or
s = E(f ).

Proof. The proof follows the same lines of that of Theorem 4.4. Let s = ψ(y),
with y = y1 · · · yn · · · , yi ∈ A, i ≥ 1, be any characteristic Sturmian word.
By Theorem 4.5, for any n ≥ 0,

π(ψ(y1 · · · yn)) ≤ π(ψ(v(n))) = π(ψ(E(v(n)))),

14

where v(n) and E(v(n)) are respectively the preﬁxes of (ab)ω and of (ba)ω

of length n. Since ψ(v(n)) and E(ψ(v(n))) are respectively the palindromic
preﬁxes of order n of f and E(f ), the ‘if part’ of theorem follows.
Let now s = ψ(y) be any characteristic Sturmian word such that for
any n and v ∈ An, π(ψ(y1 · · · yn)) ≥ π(ψ(v)). In particular, one has
π(ψ(y1 · · · yn)) ≥ π(ψ(v(n))). By Theorem 4.5 it follows that for any n ≥ 0

π(ψ(y1 · · · yn)) = π(ψ(v(n))), (9)

where the equality occurs if and only if for any n, y1 · · · yn is one of the fol-
lowing words v(n), E(v(n)), c(v(n)), and E(c(v(n))). We can suppose, without
loss of generality, that y1 = a, i.e., y ∈ aAω. In this case equality (9) implies
that for each n

either y1 · · · yn = v(n) or y1 · · · yn = c(v(n)).

Let us prove that the preceding equation implies that for all n ≥ 0 one has
y1 · · · yn = v(n). This is trivial for n ≤ 1. For n = 2, one has that y1y2 =
v(2) = ab or y1y2 = ba. However, this second case cannot occur since y1 = a.
Thus y1y2 = v(2). Let us now prove by induction that if y1 · · · yn = v(n) with
n ≥ 2, then y1 · · · yn+1 = v(n+1). Indeed, suppose by contradiction that
y1 · · · yn−1ynyn+1 = c(v(n+1)). This would imply v(n+1) = y1 · · · yn−1 ¯yn ¯yn+1,
so that v(n) = y1 · · · yn−1 ¯yn which is absurd. Thus y = (ab)ω and s = f .
If y ∈ bAω, one proves in a perfect similar way that y = (ba)ω, i.e.,
s = E(f ) and this concludes the proof.

The following lemma relates the composition, i.e., the number of letters
a and b, of a proper Christoﬀel word aψ(v)b to the minimal period of ψ(v∼).

Lemma 4.8. For any proper Christoﬀel word w = aψ(v)b,

π(ψ(v∼)) = min{|w|a, |w|b}.

In particular, if v ∈ aA∗, then

π(ψ(v∼)) = |ψ(v)|b + 1.

Proof. In view of (2) and statement 3. of Theorem 3.3, one has

π(ψ(v∼)) = min{pa(v∼), pb(v∼)} = min{|w|a, |w|b}.

If v ∈ aA∗, then |w|b < |w|a. Hence, in such a case

π(ψ(v∼)) = |w|b = |ψ(v)|b + 1.

Let us denote by d the operator in A∗ deﬁned as: d(ε) = ε, d(x) = x for
any x ∈ A, and for v = xyu with u ∈ A∗, x, y ∈ A, d(v) = d(xyu) = yxu.
Thus the operator d acting on words v of length ≥ 2 changes the preﬁx xy
of v of length 2 in yx. As it is readily veriﬁed the operator d is related to c
as follows: for any v ∈ A∗, d(v) = (c(v∼))∼. Moreover, d commute with E.

15

Theorem 4.9. For any n ≥ 0 and v ∈ aA∗ of length n

|ψ(v)|b ≤ |ψ(v(n))|b = Fn−1 − 1,

where the equality holds if and only if v = v(n) or v = E(d(v(n))).

Proof. By Lemma 4.8 one has:

|ψ(v)|b = π(ψ(v∼)) − 1 and |ψ(v(n))|b = π(ψ((v(n))
∼)) − 1.

By Theorem 4.5, π(ψ(v∼)) ≤ π(ψ(v(n))) = Fn−1.

Moreover, since (v(n))∼ is equal to v(n) if n is odd and is equal to E(v(n)) if
n is even, by Theorem 4.5 one has

π(ψ((v(n))
∼)) = π(ψ(v(n))).

Hence, |ψ(v)|b = π(ψ(v∼)) − 1 ≤ Fn−1 − 1 = |ψ(v(n))|b

and the ﬁrst part of the theorem is proved.
Now |ψ(v)|b = |ψ(v(n))|b if and only if

π(ψ(v∼)) = π(ψ(v(n))).

By Theorem 4.5 this occurs if and only if v∼ is one of the following words:
v(n), E(v(n)), c(v(n)), and E(c(v(n))). We have to consider two cases:

Case 1. n is even. The word v(n) terminates with the letter b, so that, as v
begins with the letter a, v∼ cannot be equal to v(n). Similarly, v∼ cannot
be equal to E(c(v(n))). Indeed, c(v(n)) terminates with the letter a and
E(c(v(n))) with the letter b. This would imply that, v will begin with the
letter b which is a contradiction.
Now, as one easily veriﬁes, v∼ = E(v(n)) if and only if v = v(n). More-
over, v∼ = c(v(n)) if and only if v = E(d(v(n))).

Case 2. n is odd. The word v(n) is a palindrome beginning and terminating
with the letter a. Thus E(v(n)) is also a palindrome terminating with the
letter b. Thus, as v begins with the letter a, v∼ cannot be equal to E(v(n)).
Similarly, the word c(v(n)) terminates with the letter b, so that v∼ cannot
be equal to c(v(n)).
Trivially, as v(n) is a palindrome, v∼ = v(n) if and only if v = v(n).
Finally, it is ready veriﬁed that v∼ = E(c(v(n))) if and only if v = E(d(v(n))).

Hence, in conclusion the maximal value of |ψ(v)|b is reached if and only
if v = v(n) or v = E(d(v(n))).
 16

Example 4.10. For n = 5 the central words of aA∗ with a maximal number
of b have the directive words v(5) = ababa and E(d(v(5))) = abbab. One has
ψ(ababa) = abaababaabaababaaba, ψ(abbab) = ababaabababaababa, and the
number of b is 7 = F5 − 1.

Theorem 4.11. The only characteristic Sturmian words beginning with the
letter a whose palindromic preﬁxes of any order have the maximal number
of occurrences of the letter b are the Fibonacci word f = ψ((ab)ω and the
word g = ψ(ab2(ab)ω).

Proof. Let s = ψ(y) be any characteristic Sturmian word such that y =
y1y2 · · · yn · · · , with y1 = a and yi ∈ A for i > 1. Let us suppose that for
any n ≥ 1, |ψ(y1y2 · · · yn)|b = |ψ(x1x2 · · · xn)|b

where x1x2 · · · xn = v(n) is the preﬁx of length n of the word (ab)ω. Setting
v = y1y2 · · · yn, from Theorem 4.9 the preceding equality can occur if and
only if v = v(n) or v = E(d(v(n))), that is

v = x1x2x3 · · · xn or v = x1x2x2x3 · · · xn−1.

For any n > 2, if y1y2 · · · yn = v(n), then y1y2 · · · ynyn+1 ̸= E(d(v(n+1))) so
that y1y2 · · · ynyn+1 = v(n+1). Similarly, if y1y2 · · · yn = E(d(v(n))), then
y1y2 · · · ynyn+1 ̸= v(n+1) so that y1y2 · · · ynyn+1 = E(d(v(n+1))).
Thus if y1y2y3 = v(3) = aba, then y = (ab)ω and s = ψ((ab)ω) = f .
If, on the contrary, y1y2y3 = E(d(v(3))) = abb, then y = ab2(ab)ω and
s = ψ(ab2(ab)ω).

From the preceding theorem one derives the following extremal property
of Fibonacci word.

Corollary 4.12. Fibonacci word is the unique characteristic Sturmian word
s whose directive word begins with aba, or equivalently s begins with abaa,
such that its palindromic preﬁxes of any order have the maximal number of
occurrences of the letter b.

5 Arithmetization

In this section we shall give an interpretation of the extremal properties
satisﬁed by the palindromic preﬁxes of f and E(f ) shown in the preceding
section, in terms of continued fractions and more precisely of continuants.
Any word v ∈ A∗ can be uniquely represented as:

v = bα0a
α1bα2 · · · a
αm−1 bαm,

where m is an even integer, αi > 0, i = 1, . . . , m − 1, and α0 ≥ 0, αm ≥ 0.
We call the list (α0, α1, . . . , αn), where n = m if αm > 0 and n = m − 1
otherwise, the integral representation of the word v.

17

We can identify the word v with its integral representation and write
v ≡ (α0, α1, . . . , αn). One has:
 |v| =
 n∑

i=0 |αi|.

For instance, the words v1 = b2aba2 and v2 = a3bab2 have the integral
representations v1 ≡ (2, 1, 1, 2) and v2 ≡ (0, 3, 1, 1, 2).
If v ∈ Aω is the directive word of the characteristic word ψ(v), then v
can be uniquely represented by

v = bα0aα1b
α2 · · · ,

with α0 ≥ 0 and αi > 0, i > 0. The inﬁnite sequence (α0, α1, α2, · · · , αn, · · · )
is called the integral representation of v. It has been proved in [10] that
if α0 = 0 then (α1, α2, · · · , αn, · · · ) coincides with the directive numerical
sequence of the characteristic word ψ(v). If α0 > 0, then the directive
numerical sequence of ψ(v) is (0, α0, α1, . . . , αn, . . .).
The following important theorem holds (cf.[1, 2]):

Theorem 5.1. Let w = aub be a proper Christoﬀel word with u = ψ(v) and
(α0, α1, . . . , αn), n ≥ 0, be the integral representation of v. Then the slope
η(w) of w is given by the continued fraction

[α0; α1, . . . , αn−1, αn + 1].

We remark that in the case n = 0 the preceding formula becomes [α0 +1],
or, equivalently, [α0; 1].

Example 5.2. Let v = a2b2a. One has w = a3ba2ba3ba2ba2b and η(w) =
[0; 2, 2, 2]= 5
12 . If v = ba2b, then w = abababbababb and η(w) = [1; 2, 2]= 7
5 . If
v = b3, then w = ab4 and η(w) = 4
1 = [4] = [3; 1].

Let [a0; a1, . . . , an] be a continued fraction. As is well known (see, for in-
stance, [21]), for any 0 ≤ k ≤ n, the k-order convergent Ck = [a0; a1, . . . , ak]
is given by the ratio Ak
Bk , where (Ak)k≥−1, (Bk)k≥−1 is a bisequence deﬁned
by A−1 = 1, A0 = a0, B−1 = 0, B0 = 1

and Ak+1 = ak+1Ak + Ak−1, Bk+1 = ak+1Bk + Bk−1,

for 0 ≤ k ≤ n − 1. For any k ≥ 0 the fraction Ak
Bk is irreducible.
Let us now set for any k ≥ −1,

Pk = Ak + Bk.

18

One has that P−1 = 1, P0 = a0 + 1, and

Pk+1 = ak+1Pk + Pk−1, for k ≥ 0. (10)

The value of Pn for n ≥ 0 can be expressed in terms of continuants (cf. [18])
(called cumulants in [24]). Let a0, a1, . . . , an, . . . be any sequence of numbers.
The n-th continuant K[a0, . . . , an] is deﬁned recursively as: K[ ] = 1,
K[a0] = a0, and for n ≥ 1,

K[a0, a1, . . . , an] = anK[a0, a1, . . . , an−1] + K[a0, a1, . . . , an−2]. (11)

As it is ready veriﬁed for any n ≥ 0, K[a0, a1, . . . , an] is a multivariate
polynomial in the variables a0, a1, . . . , an which is obtained by starting with
the product a0a1 · · · an and then striking out adjacent pairs akak+1 in all
possible ways. For instance, K[a0, a1, a2, a3, a4] = a0a1a2a3a4 + a2a3a4 +
a0a3a4 + a0a1a4 + a0a1a2 + a0 + a2 + a4.
We recall (cf. [18, 24]) that for every n ≥ 0,

K[a0, . . . , an] = K[an, . . . , a0], (12)

i.e., a continuant does not change its value by reversing the order of its
elements; moreover, one has K[1n] = Fn−1, where we have denoted by 1n

the sequence of length n, (1, 1, . . . , 1). A further property that we shall use
in the following, is:

K[a0, . . . , an, 1] = K[a0, . . . , an−1, an + 1]. (13)

There exists a strong relation between continued fractions and continuants.
More precisely the following holds. Let [a0; a1, . . . , an] be any continued
fraction. Then
 [a0; a1, . . . , an] = K[a0, a1, . . . , an]
K[a1, . . . , an] (14)

Indeed, as is ready veriﬁed, K[a0, a1, . . . , an] = An and K[a1, . . . , an] = Bn.
From (10) and (11), or using the preceding properties of continuants, one
derives that if [a0; a1, . . . , an] is a continued fraction, then for any n ≥ 0,

Pn = An + Bn = K[a0 + 1, a1, . . . , an]. (15)

The following holds:

Theorem 5.3. Let w = aub be a proper Christoﬀel word with u = ψ(v) and
(α0, α1, . . . , αn), n ≥ 0, be the integral representation of v. Then

|w| = K[α0 + 1, α1, . . . , αn−1, αn + 1].

We remark that for n = 0 the preceding formula becomes K[α0 + 1, 1] =
K[α0 + 2].
 19

Proof. By Theorem 5.1, the slope |w|b
|w|a of w is given by the continued fraction

[α0; α1, . . . , αn−1, αn + 1]. Since the n-th order convergent C ′
n = A′
n
B′
n = |w|b
|w|a
and gcd(|w|a, |w|b) = 1, one has P ′
n = A′
n + B′
n = |w|b + |w|a = |w|. Then
the result follows from (15).

Theorem 4.1 and Corollary 4.3 can be restated equivalently in terms of
continuants as follows:

Theorem 5.4. Let n ≥ 0 and α0, α1, . . . , αm be any sequence of integers
such that
 α0 ≥ 0, αi > 0, i = 1, . . . , m, and
 m∑

i=0 αi = n.

Then

K[α0 + 1, α1, . . . , αm−1, αm + 1] ≤ K[1
n, 2] = K[2, 1
n] = Fn+1, (16)

where the equality occurs if and only if m = n and α0 = 0, α1 = α2 = · · · =
αn = 1 or m = n − 1 and α0 = α1 = α2 = · · · = αn−1 = 1.

Proof. Let v be any word of An having the integral representation v ≡
(α0, α1, . . . , αm) such that n = ∑m
i=0 αi. By Theorem 4.1 and Corollary 4.3
one has |ψ(v)| ≤ |ψ(v(n))| = Fn+1 − 2,

so that |aψ(v)b| ≤ Fn+1. Thus, by Theorem 5.3 one derives

|aψ(v)b| = K[α0 + 1, α1, . . . , αm−1, αm + 1] ≤ Fn+1 = K[1
n, 2] = K[2, 1
n].

By Corollary 4.3 the equality occurs if and only if v = v(n) or v = E(v(n)).
In the ﬁrst case m = n and α0 = 0, α1 = α2 = · · · = αn = 1. In the second
case m = n − 1, and α0 = α1 = α2 = · · · = αn−1 = 1. Hence, the theorem
is proved.

Let us observe that the preceding theorem implies the validity of The-
orem 4.1 and Corollary 4.3. Indeed, let v be any word over A having the
integral representation v ≡ (α0, α1, . . . , αm) and length n = ∑m
i=0 αi. From
(16) and Theorem 5.3 one derives |ψ(v)| ≤ |ψ(v(n))| = Fn+1 − 2, where the
equality holds if and only if v = v(n) or v = E(v(n)).
We shall give now a direct proof of Theorem 5.4 without using combi-
natorics on words. We need the following lemma on Fibonacci numbers.

Lemma 5.5. Let n ≥ 1. For any integer x such that 0 < x ≤ n, one has:

xFn−x + Fn−x+1 ≤ Fn+1,

where the equality holds if and only if x = 1.

20

Proof. The proof is by induction on the value of x ≤ n. For x = 1 one has
Fn−1 + Fn = Fn+1. For x = 2 ≤ n one has 2Fn−2 + Fn−1 = Fn−2 + Fn−2 +
Fn−1 = Fn−2 + Fn < Fn−1 + Fn = Fn+1. Suppose the statement true up to
1 < x − 1 < n and prove it for x. One has by using the inductive hypothesis,

xFn−x + Fn−x+1 = (x − 1)Fn−x + Fn−x + Fn−x+1 = (x − 1)Fn−x + Fn−x+2

< (x − 1)Fn−x+1 + Fn−x+2 < Fn+1.

(Second proof of Theorem 5.4). The proof is by induction on the integer n.
The result is trivial if n ≤ 1. Let us suppose the result true for all integers
less than n > 1 and prove it for n. Let α0, α1, . . . , αm be any sequence of
integers such that α0 ≥ 0, αi > 0, i = 1, . . . , m, and ∑m
i=0 αi = n. From
the deﬁnition of continuant one has:

K[α0 + 1, α1, . . . , αm−1, αm + 1] = (αm + 1)K[α0 + 1, α1, . . . , αm−1]

+K[α0 + 1, α1, . . . , αm−2].

By induction one derives:

K[α0 + 1, α1, . . . , αm−1] ≤ Fn−αm. (17)

Indeed, if αm−1 > 1 one has

K[α0 + 1, α1, . . . , αm−1] = K[α0 + 1, α1, . . . , αm−2, (αm−1 − 1) + 1].

Since, ∑m−2
i=0 αi+(αm−1−1) = n−αm−1, equation (17) follows by induction.
If αm−1 = 1, by (13), one has

K[α0 + 1, α1, . . . , αm−2, 1] = K[α0 + 1, α1, . . . , αm−2 + 1].

Since ∑m−2
i=0 αi = n − αm − 1, equation (17) follows again by induction. In
a similar way one derives by induction

K[α0 + 1, α1, . . . , αm−2] ≤ Fn−αm−αm−1 . (18)

Thus, since αm−1 ≥ 1, one has:

K[α0 + 1, α1, . . . , αm−1, αm + 1] ≤ (αm + 1)Fn−αm + Fn−αm−αm−1

= αmFn−αm + Fn−αm + Fn−αm−αm−1 ≤ αmFn−αm + Fn−αm+1,

where in the last inequality the equality sign occurs if and only if αm−1 = 1.
By Lemma 5.5, αmFn−αm + Fn−αm+1 ≤ Fn+1, where the equality holds if
and only if αm = 1. Thus in any case

K[α0 + 1, α1, . . . , αm−1, αm + 1] ≤ Fn+1.

21

The equality can occur in the preceding equation if and only if αm = αm−1 =
1 and, moreover, in view of (17) and (18),

K[α0 + 1, α1, . . . , αm−2 + 1] = Fn−1 and K[α0 + 1, α1, . . . , αm−2] = Fn−2.

Since ∑m−2
i=0 αi = n−2, by induction the ﬁrst of the two preceding equations
is satisﬁed if and only if α0 = 0, m = n, and α1 = · · · = αn−2 = 1 or α0 = 1,
m = n − 1, and α1 = · · · = αn−3 = 1. In the ﬁrst case αm−1 = αn−1 = αn =
αm = 1, and in the second case, αm−1 = αn−2 = αm = αn−1 = 1. Since
for the previous values of α’s the second equation is certainly satisﬁed, the
result follows. □

Proposition 5.6. Let v ∈ A∗ be a word having the integral representation
v = (α0, α1, . . . , αn). Then

π(ψ(v)) = K[α0 + 1, α1, . . . , αn−1].

Proof. It has been proved in [10] (see also [1, 6]) that if v has the integral
representation v = (α0, α1, . . . , αn), then

[0; αn, αn−1, . . . , α1, α0 + 1] = π(ψ(v))
q ,

where π(ψ(v)) is the minimal period of ψ(v) and q is the period of ψ(v) such
that gcd(q, π(ψ(v))) = 1 and |ψ(v)| = π(ψ(v)) + q − 2. By (14) one has:

[0; αn, αn−1, . . . , α1, α0 + 1] = K[0, αn, . . . , α1, α0 + 1]
K[αn, . . . , α1, α0 + 1] .

Since the preceding fraction is irreducible, by (12) and (11) one derives:

π(ψ(v)) = K[0, αn, . . . , α1, α0 + 1] = K[α0 + 1, α1, . . . , αn−1, αn, 0]

= K[α0 + 1, α1, . . . , αn−1],

which concludes the proof.

By the preceding proposition and the extremal property of continuants
expressed by Theorem 5.4, we can give a diﬀerent proof of Theorem 4.5.
Indeed, the following proposition holds:

Proposition 5.7. Let n ≥ 0 and α0, α1, . . . , αm be any sequence of integers
such that
 α0 ≥ 0, αi > 0, i = 1, . . . , m, and
 m∑

i=0 αi = n.

One has that K[α0 + 1, α1, . . . , αm−1] ≤ Fn−1. (19)

22

The equality is reached if and only if one of the following conditions is sat-
isﬁed:

1) α0 = 0, m = n, and α1 = α2 = · · · = αn−1 = αn = 1,
2) α0 = 0, m = n − 1, and αi = 1 for 1 ≤ i ≤ n − 3, αn−2 = 2, αn−1 = 1,
3) α0 = 1, m = n − 1, and α1 = α2 = · · · = αn−1 = 1,
4) α0 = 1, m = n − 2, and αi = 1 for 1 ≤ i ≤ n − 4, αn−3 = 2, αn−2 = 1.

Proof. We have to consider two cases. If αm−1 = 1, since

K[α0 + 1, α1, . . . , αm−2, 1] = K[α0 + 1, α1, . . . , αm−2 + 1],

one has K[α0 + 1, α1, . . . , αm−2 + 1] ≤ Fn−αm ≤ Fn−1. (20)

Indeed, since ∑m−2
i=0 αi = n − 1 − αm, the preceding formula follows from
Theorem 5.4. If αm−1 > 1, one derives:

K[α0 + 1, α1, . . . , αm−2, (αm−1 − 1) + 1] ≤ Fn−αm ≤ Fn−1. (21)

Indeed, since ∑m−2
i=0 αi + αm−1 − 1 = n − 1 − αm, the previous inequality
follows again from Theorem 5.4. Thus in any case (19) is satisﬁed.
The maximal value of K[α0 + 1, α1, . . . , αm−1] is then Fn−1. It is reached
if and only if one of the conditions 1), 2), 3), and 4) is satisﬁed. The suf-
ﬁciency of the preceding conditions is readily veriﬁed. Let us prove the
necessity.
Indeed, necessarily αm = 1. Moreover, by Theorem 5.4, if K[α0 +
1, α1, . . . , αm−1] = Fn−1, then α0 = 0 or α0 = 1. We consider only the
case α0 = 0; the case α0 = 1 is similarly dealt with.
If αm−1 = 1, in view of (20), one derives by Theorem 5.4, that m = n
and α1 = α2 = · · · = αn−2 = 1. Since αm−1 = αn−1 = αm = αn = 1,
condition 1) is satisﬁed.
If αm−1 > 1, in view of (21), one derives by Theorem 5.4, that m = n − 1
and α1 = α2 = · · · = αm−2 = αm−1−1 = 1. Thus αm−1 = αn−2 = 2. Hence,
since αm = αn−1 = 1, condition 2) is satisﬁed.

By Propositions 5.6 and 5.7, one easily derives Theorem 4.5 of the pre-
vious section.

References

[1] J. Berstel, A. de Luca, Sturmian words, Lyndon words and trees, The-
oret. Comput. Sci. 178 (1997) 171–203

[2] J. Berstel, A. Lauve, C. Reutenauer, F.V. Saliola, Combinatorics on
Words, Christoﬀel Words and Repetitions in Words, CRM Monograph
series, vol. 27, American Mathematical Society, (Providence, RI, 2009)

23

[3] V. Berth´e, A. de Luca, C. Reutenauer, On an involution of Christoﬀel
words and Sturmian morphisms, European J. Combin. 29 (2008) 535–
553

[4] J.-P. Borel, F. Laubie, Quelques mots sur la droite projective r´eelle,
Journal de Th´eorie des Nombres de Bordeaux 5 (1993) 23–52

[5] A. Carpi, A. de Luca, Special factors, Periodicity, and an Application
to Sturmian words, Acta Informatica 36 (2000) 983–1006

[6] A. Carpi, A. de Luca, Harmonic and gold Sturmian words, European
J. Combin. 25 (2004) 685–705

[7] J. Cassaigne, On extremal properties of the Fibonacci word, Theor.
Inform. Appl. 42 (2008) 701–715

[8] E.B. Christoﬀel, Observatio arithmetica, Annali di Matematica Pura e
Applicata 6 (1875) 148–152

[9] A. de Luca, A combinatorial property of the Fibonacci words, Infor-
mation Processing Letters 12 (1981) 193–195

[10] A. de Luca, Sturmian words: Structure, Combinatorics, and their
Arithmetics, Theoret. Comput. Sci. 183 (1997) 45–82

[11] A. de Luca, A standard correspondence on epicentral words, European
J. Combin. 33 (2012) 1514–1536

[12] A. de Luca, A. De Luca, Pseudopalindrome closure operators in free
monoids, Theoret. Comput. Sci. 362 (2006) 282–300

[13] A. de Luca, A. De Luca, A generalized palindromization map in free
monoids, Theoret. Comput. Sci. (2012), doi:10.1016/j.tcs.2012.01.029

[14] A. de Luca, F. Mignosi, Some combinatorial properties of Sturmian
words, Theoret. Comput. Sci. 136 (1994) 361–385

[15] A. de Luca, L. Q. Zamboni, Involutions of epicentral words, European
J. Combin. 31 (2010) 867–886

[16] X. Droubay, J. Justin, G. Pirillo, Episturmian words and some con-
structions of de Luca and Rauzy, Theoret. Comput. Sci. 255 (2001)
539–553

[17] N. J. Fine, H.S. Wilf, Uniqueness theorem for periodic functions, Proc.
Amer. Math. Soc. 16 (1965) 109–114

[18] R.L. Graham, D.E. Knuth, O. Patashnik, Concrete Mathematics, 2-nd
edition, Addison-Wesley (Reading Mass., 1994)

24

[19] J. Justin, Episturmian morphisms and a Galois theorem on continued
fractions, Theor. Inform. Appl. 39 (2005) 207–215

[20] C. Kassel, C. Reutenauer, A palindromization map for the free group,
Theoret. Comput. Sci. 409 (2008) 461–470

[21] A. Ya. Khinchin, Continued fractions, The University of Chicago Press,
(Chicago Ill., 1964)

[22] M. Lothaire, Combinatorics on Words, Addison-Wesley (Reading, MA,
1983)

[23] M. Lothaire, Algebraic Combinatorics on Words, Encyclopedia of
Mathematics and its Applications, vol. 90, Cambridge University Press
(Cambridge, 2002)

[24] E. Lucas, Th´eorie des nombres, Gauthier-Villars (Paris, 1891)

[25] F. Mignosi, A. Restivo, S. Salemi, Periodicity and golden ratio, Theoret.
Comput. Sci. 204 (1998) 199–204

25
