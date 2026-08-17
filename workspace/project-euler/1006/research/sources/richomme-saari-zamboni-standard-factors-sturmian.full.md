<!-- source: https://www.numdam.org/item/ITA_2010__44_1_159_0.pdf | converted from PDF -->

RAIRO-Theor. Inf. Appl. 44 (2010) 159–174 Available online at:

DOI: 10.1051/ita/2010011 www.rairo-ita.org

STANDARD FACTORS OF STURMIAN WORDS ∗, ∗∗

Gw·ena¤el Richomme 1, 2, Kalle Saari 3

and Luca Q. Zamboni 4, 5

Abstract. Among the various ways to construct a characteristic
Sturmian word, one of the most used consists in deﬁning an inﬁnite
sequence of preﬁxes that are standard. Nevertheless in any character-
istic word c, some standard words occur that are not preﬁxes of c.We
characterize all standard words occurring in any characteristic word
(and so in any Sturmian word) using ﬁrstly morphisms, then standard
preﬁxes and ﬁnally palindromes.

Mathematics Subject Classiﬁcation. 68R15.

1. Introduction

Morse and Hedlund [25] begun the study of Sturmian words in 1940 to help
develop the theory of symbolic dynamical systems they initiated a couple of years
earlier [24]. Since then, and especially during the last two decades, Sturmian words
have been under intensive scrutiny, as indicated by the surveys [4,5,7]. A reason of

Keywords and phrases. Sturmian words, standard factors, morphisms, palindromes.

∗ The second author was supported by the Finnish Academy under grant 8206039.
∗∗ The third author is partially supported by grant no. 090038011 from the Icelandic Research
Fund.
1 Universit´edePicardie Jules Verne, LaboratoireMIS (Mod´elisation, Information, Syst`emes),
33 rue Saint Leu, 80039 Amiens Cedex 1, France; gwenael.richomme@u-picardie.fr
2 Universit´ePaul-Val´ery Montpellier 3, UFR 4, Dpt. MIAp, Route de Mende, 34199
Montpellier Cedex 5, gwenael.richomme@univ-montp3.fr
3 Department of Mathematics and Turku Centre for Computer Science, University of Turku,
20014 Turku, Finland; kasaar@utu.fi
4 Universit´ede Lyon, Universit´e Lyon 1, CNRS UMR 5208 Institut Camille Jordan, Bˆatiment
du Doyen Jean Braconnier, 43 bd. du 11 novembre 1918, 69622 Villeurbanne Cedex, France;
luca.zamboni@wanadoo.fr
5 Reykjavik University, School of Computer Science, Kringlan 1, 103 Reykjavik, Iceland;
lqz@ru.is

Article published by EDP Sciences c∗ EDP Sciences 2010

160 G. RICHOMME, K. SAARI AND L.Q. ZAMBONI

this passion comes from the various connections Sturmian words have with other
domains like for instance number theory [1,2], discrete geometry [8,20], crystallog-
raphy [10] or scheduling [3].
Another reason is the richness of combinatorial properties of Sturmian words
(see previous references) which concerns various aspects including, e.g., palin-
dromes, repetitions, unbordered or Lyndon words (see for instance [6,9,13,14,19,
22,23,26,27]). The problem considered in the current paper continues a theme of
characterizing those factors of a Sturmian word that belong to some interesting
class of ﬁnite words.
We consider standard words. These ﬁnite words can be used to deﬁne in a
constructive way some Sturmian words (see Sect. 2 for more details) building
arbitrarily long preﬁxes of so-called characteristic Sturmian words. Among these
inﬁnite words, the well-known Fibonacci word is maybe the one with a maximal
number of extremal properties [11]. In his Ph.D. thesis [28], the second author
observed that the Fibonacci word contains some factors that are standard but not
preﬁxes of it, and he asked for a characterization of the set of standard words
occurring as factors in the Fibonacci word.
Sections 3, 4 and 5 solve this problem in a much more general way since they
provide, for any Sturmian word, characterizations of its factors that are standard.
Section 3 uses existing links between standard words and Sturmian morphisms.
The proof is rather technical but the result allows to derive in a simple way a char-
acterization using standard words occurring in the construction of characteristic
words mentioned above (Sect. 4). Previous characterizations are illustrated using
the Fibonacci word as an example. This word is also used in Section 5 to show
how to relate standard factors of a Sturmian word to palindromes. This needs a
characterization based on directive sequences of standard words.

2. Standard and Sturmian words

We will follow the usual notation and terminology of combinatorics on words.
For further information about the concepts and results mentioned in this section,
we refer the reader to [12,21].
A word is a sequence, ﬁnite or inﬁnite, of symbols drawn from a ﬁnite alpha-
bet A;in this paper we set A = {0, 1}. The empty word is denoted by ε.The set
of all ﬁnite words over A is denoted by A
∗; the set of all nonempty words over A
is denoted by A
+. A ﬁnite word u is a factor of a word w if we can write w = xuy.
The length of a word u is denoted by ∣
∣u∣
∣, and the number of occurrences of a
letter a in u is denoted by ∣
∣u∣
∣a. For an integer k ≥ 2, a kth power is a word of the
form uk, that is, a word obtained concatenating k occurrences of a given word u
(we also denote u1 = u and u0 = ε).
A Sturmian word is an inﬁnite word with precisely n+1 factors for each length n.
Equivalently [21], Theorem 2.1.13 and Proposition 2.1.18 a Sturmian word is an
inﬁnite word whose factors coincide with those of a characteristic word, where
a characteristic word is an inﬁnite word cα, depending on an irrational α with

STANDARD FACTORS OF STURMIAN WORDS 161

0 <α < 1, such that cα(n)= ⌊α(n +1)⌋−⌊αn⌋

for all n ≥ 1. When proving a property of the factors of a Sturmian word, it often
suﬃces to prove it for a characteristic word.
A ﬁnite word s is called a standard word if there exist integers n ≥−1, d1 ≥ 0,
d2,d3,...,dn ≥ 1, and words s−1,s0,s1,... ,sn with s = sn such that

s−1 =1,s0 =0,sk = sdk
k−1sk−2 (k ≥ 1).

Also, if n ≥ 1, then (d1,d2,... ,dn) is called the directive sequence of the word
sn. Observe that the letter 1 has a directive sequence (0), but the letter 0 does
not have any. Therefore we agree that the directive sequence of 0 is the empty
sequence.
Two basic properties of standard words are that (1) they are primitive (that
is, not a power of a shorter word) and (2) all standard words of length at least 2
have a suﬃx in {01, 10}.
In this paper, we are interested in factors of an inﬁnite word that are standard
words; we call such a factor brieﬂy a standard factor.
Let us denote the simple continued fraction expansion of α by

α =[ 0; d1 +1,d2,d3,... ].

The sequence (d1,d2,d3,...) is called the directive sequence of cα. This terminol-
ogy is justiﬁed by the fact that cα can be obtained as a limit of those standard
words whose directive sequences are preﬁxes of the one of cα,thatis,

cα = lim
n→∞ sn.

Many properties of Sturmian words can be dealt with using morphisms. Let us
recall that a mapping h : A
∗ →A
∗ is called a morphism if it satisﬁes h(uv)=
h(u)h(v) for all u, v ∈A
∗. Observe that a morphism is uniquely determined by
how it maps letters.
The well-known Fibonacci word f is the characteristic word cα with α =(3 −√
5)/2, so that it has directive sequence (1, 1, 1,...). It is also the unique ﬁxed
point of the morphism
 ϕ : { 0 ↦→ 01
1 ↦→ 0.

Next we deﬁne the morphisms

L0 : { 0 ↦→ 0
1 ↦→ 01 L1 : { 0 ↦→ 10
1 ↦→ 1.

The following lemma is well-known; it has a straightforward proof in the spirit of
the proof of [7], Proposition 2.3.11, which we omit here.

162 G. RICHOMME, K. SAARI AND L.Q. ZAMBONI

Lemma 2.1. Aword w ∈{0, 1}∗ is standard if and only if there exists a morphism
f in the monoid generated by L0 and L1 such that either w = f (0) or w = f (1).

In addition to L0 and L1, we shall need a few other morphisms. For all integers
m ≥ 1, we deﬁne the morphisms

θm : { 0 ↦→ 0m−11
1 ↦→ 0m−110.

We also deﬁne the morphism E :0 ↦→ 1, 1 ↦→ 0, and denote (with (d1,d2,d3,...)
the directive sequence of cα)

hn = θd1+1 ◦ θd2 ◦ ... ◦ θdn (n ≥ 1).

Morphisms hn are handy because we have hn(0) = sn and hn(1) = snsn−1 for all
n ≥ 1 (see the proof of [7], Prop. 2.2.24). Furthermore, they satisfy

h2k = Ld1
0 ◦ Ld2
1 ◦ ... ◦ Ld2k−1
0 ◦ Ld2k
1 ◦ L0, and (2.1)

h2k+1 = Ld1
0 ◦ Ld2
1 ◦ ... ◦ Ld2k
1 ◦ Ld2k+1
0 ◦ L1 ◦ E. (2.2)

This follows from the two identities θm = Lm−1
0 ◦ E ◦ L0 and E ◦ L0 = L1 ◦ E.
For a ﬁnite word x, the shortest palindrome that has x as a preﬁx is denoted
by x
(+); this is called the (right) palindromic closure of x due to de Luca [15]. We
let Pal denote the operation of iterated palindromic closure deﬁned by

Pal(a1)= a1 and Pal(a1a2 ...an)= (
Pal(a1a2 ... an−1)an)(+),

where ai is a letter.
The characteristic word cα can be also represented as follows. Let us denote
0d11d20d3 ... = x1x2x3 ...,where xi ∈{0, 1}.Then

cα = lim
n→∞ Pal(x1 ... xn).

The sequence 0d11d20d3 ... is called the directive word of cα. Both directive words
and directive sequences will be used in this paper to represent a characteristic
word.
The following relation (see [16], Thm. 9) will be useful. If x and y are charac-
teristic words directed, respectively, by a1a2a3 ... and a2a3 ...,where ai ∈{0, 1},
then x = La1(y). (2.3)

3. Characterization via morphisms L0 and L1

Here we present a characterization of standard factors of a Sturmian word using
the morphisms L0 and L1. The proof can appear a bit laborious, but the result
enables us to derive two other characterizations in a relatively simple manner.

STANDARD FACTORS OF STURMIAN WORDS 163

First, however, we need to introduce an auxiliary notation. Let n1,n2,n3 ≥ 1
be integers. Then we let S(n1,n2,n3) denote the union of the following ﬁve sets
of words:
 { Li
0(0),Li
0(1),Li
0(10) | 0 ≤ i<n1 }
,
{ Ln1
0 (1i0) | 1 ≤ i ≤ n2 },
{ Ln1−1
0 (
(10)
i1) | 1 ≤ i ≤ n2 }
,
{ Ln1
0 (
1n2−10(1n20)
i1n20) | 1 ≤ i ≤ n3 },
{ Ln1
0 (
1i−101i0) | 1 ≤ i ≤ n2 }
.

Using Lemma 2.1, it is readily checked that all words in S(n1,n2,n3) are standard
(note that 1i0= Li
1(0), (10)
i1= L1 ◦ Li
0(1), 1n2−10(1n20)
i1n20= Ln2−1
1 ◦ L0 ◦
Li+1
1 (0) and 1i−101i0= Li−1
1 ◦ L0 ◦ L1(0)).
It is instructive to observe that each word in S(n1,n2,n3) is a factor of any
characteristic word whose directive sequence starts with 0n11n20n3 . This follows
from equation (2.3)when w belongs to one of the two ﬁrst sets of S(n1,n2,n3).
When w belongs to one of the three last sets of S(n1,n2,n3), we deduce the
previous observation from the following three facts where x denotes an arbitrary
non-ultimately-periodic inﬁnite word over {0, 1}:

-1n2+1 is a factor of Ln2
1 (x);
-1n2−10(1n20)
n31n2+1 is a factor of Ln2
1 ◦ Ln3
0 (x); and
-1n2−101n20 is a factor of Ln2
1 ◦ Ln3
0 (x).

Now we are ready for the main result of this section. In order to state it nicely,
we extend notation S by letting S(0,n2,n3)= ∅, the empty set, for all integers n2
and n3.

Theorem 3.1. Let α =[ 0 ; d1 +1,d2,...]. A ﬁnite standard word u is a factor
of cα if and only if there exists an integer k ≥ 0 such that one of the following
holds:

• There exists x ∈S(d2k+1,d2k+2,d2k+3) such that

u = Ld1
0 ◦ Ld2
1 ◦ ... ◦ Ld2k−1
0 ◦ Ld2k
1 (x).

• There exists x ∈S(d2k+2,d2k+3,d2k+4) such that

u = Ld1
0 ◦ Ld2
1 ◦ ... ◦ Ld2k−1
0 ◦ Ld2k
1 ◦ Ld2k+1
0 ◦ E(x).

Remark 3.2. By the deﬁnition of the continued fraction [ 0 ; d1 +1,d2,...], we
have d1 ≥ 0and dk ≥ 1for k ≥ 2. When d1 = 0, the ﬁrst item provides no
standard word for k =0.

164 G. RICHOMME, K. SAARI AND L.Q. ZAMBONI

We will divide the proof of Theorem 3.1 into several lemmas. But let us see
ﬁrst what it says in the case of the Fibonacci word:

Example 3.3. Recall that the directive sequence of the Fibonacci word f is
(1, 1,...). Since
 S(1, 1, 1) = {0, 1, 10, 010, 101, 0010, 0010010},

and since L0 ◦ L1 = ϕ
2 and L0 ◦ E = ϕ, it follows from Theorem 3.1 that the set
of standard factors of the Fibonacci word equals

{ ϕ
n(1),ϕ
n(10),ϕ
n(101),ϕ
n(0010010) | n ≥ 0 }
.

We will see other ways to characterize these standard factors in later examples.

Now we are ready to start proving Theorem 3.1.

Lemma 3.4. Let x, y be two inﬁnite words over {0, 1} such that x = L0(y).
Suppose that the letter 1 occurs in x.Then a word u is a standard factor of x if
and only if one of the following holds:

(1) u ∈{0, 1, 10};
(2) u = L0(v) with v a standard factor of y;
(3) u = L0(w0) with w ̸= ε,the word w0 standard, and w1 afactor of y;
(4) u = (10)
n1 with n ≥ 1 and 1n+1 afactor of y.

Proof. Using Lemma 2.1, it is veriﬁed that conditions (1)–(4) are suﬃcient, that
is, if u fulﬁlls one of these conditions then u is a standard factor of x.
Conversely, suppose ﬁrst that ∣
∣u∣
∣ ≤ 2. As a standard word, u is primitive,
and consequently u ∈{0, 1, 01, 10}.We see that u satisﬁes condition (1), unless
u =01= L0(1), in which case u satisﬁes condition (2).
Suppose now that ∣
∣u∣
∣ ≥ 3. Lemma 2.1 implies that either u = L0(v)or u =
L1(v) for some standard word v. Furthermore, the primitivity and length of u
imply that both letters 0 and 1 occur in v, and hence ∣
∣v∣
∣ < ∣
∣u∣
∣.We have two
possibilities to consider:
If u = L0(v), then u begins with 0. If v is a factor of y, then condition (2) is
satisﬁed, and therefore we may suppose that v is not a factor of y. It follows that
u also ends with 0. Now it is easy to see that v = w0for some word w ̸= ε such
that w1 is a factor of y. Hence condition (3) holds.
If u = L1(v), then the word 00 does not occur in u.Since u is a factor of x =
L0(y), the word 11 does not occur in u either. Consequently, we have u = (10)
n

or u = (10)
n1for some n ≥ 0. Since u is primitive and ∣
∣u∣
∣ ≥ 3, it follows that
u = (10)
n1and n ≥ 1. Since u is afactorof L0(y), we see that 1n+1 must be a
factor of y. Thus condition (4) holds. □

STANDARD FACTORS OF STURMIAN WORDS 165

Lemma 3.5. Let y be an inﬁnite word over {0, 1},and let k ≥ 1 be an integer.
Then a standard word u is a factor of Lk
0 ◦ L1(y) if and only if one of the following
conditions holds:
(1) u ∈ { Li
0(0),Li
0(1),Li
0(10) | 0 ≤ i< k }
;
(2) u = Lk
0(v) with v a standard factor of L1(y);
(3) u = Lk
0(w0) with w ̸= ε, w0 is standard, and w1 is a factor of L1(y);
(4) u = Lk−1
0 (
(10)
n1) with n ≥ 1 and 1n+1 is a factor of L1(y).

Proof. It is easy to see that conditions (1)–(4) are suﬃcient. We prove the necessity
of the conditions by induction on k.The case k = 1 follows immediately from
Lemma 3.4. So we may suppose that k ≥ 2. Using Lemma 3.4, wehavethe
following four cases to consider:
Case 1.If u ∈{0, 1, 10}, then condition (1) holds.
Case 2.We have u = L0(v), where v is a standard factor of Lk−1
0 (y). By the
induction assumption, one of the four conditions holds:
(1) v ∈ { Li
0(0),Li
0(1),Li
0(10) | 0 ≤ i< k − 1 }
;
(2) v = Lk−1
0 (v′)with v′ a standard factor of L1(y);
(3) v = Lk−1
0 (w0) with w ̸= ε, w0 standard, and w1 a factor of L1(y);
(4) v = Lk−2
0 (
(10)
n1) with n ≥ 1and 1n+1 afactorof L1(y).
Therefore one of conditions (1)–(4) holds.
Case 3.We have u = L0(w0) with w ̸= ε,the word w0 is a standard word,
and w1 a factor of Lk−1
0 (y). Since w0 is standard, the word w must endinthe
letter 1. Consequently, the word 11 is a factor of Lk−1
0 (y). But thisisnot possible
as k − 1 ≥ 1.
Case 4.We have u = (10)
n1with n ≥ 1and 1n+1 afactorof Lk−1
0 (y). Again,
since k − 1 ≥ 1, this case is not possible. The proof is complete. □

Lemma 3.6. If u is a standard word with u ∈{0, 1}+0, then there exists an
integer ℓ ≥ 1 such that either u =1ℓ0 or u ∈ 1ℓ−10{1ℓ−10, 1ℓ0}∗1ℓ0.

Proof. The claim is clearly true if ∣
∣u∣
∣ =2. If ∣
∣u∣
∣ ≥ 3, then Lemma 2.1 implies
that u = L0(v)or u = L1(v) for some standard word v with 2 ≤ ∣
∣v∣
∣ < ∣
∣u∣
∣.
Furthermore, also v satisﬁes v ∈{0, 1}+0, and therefore either v is of the form 1ℓ0
or it is in 1ℓ−10{1ℓ−10, 1ℓ0}∗1ℓ0for some ℓ ≥ 1. A straightforward computation
shows that u is of one of the attested forms. □

Lemma 3.7. Let y be aSturmianwordover {0, 1}. Suppose that w ̸= ε is a ﬁnite
word such that w0 is a standard word and w1 is a factor of y. Then either w =1ℓ

or w =1ℓ−10(1ℓ0)
i1ℓ,where ℓ ≥ 1 and i ≥ 0 are integers.

Proof. Since w ̸= ε and w0 is standard, the word w ends in the letter 1. Let
ℓ ≥ 1 denote the largest integer such that 1ℓ is a suﬃx of w.If w =1ℓ,we are
done, so we may suppose that this is not the case. Then by Lemma 3.6,wehave
w0 ∈ 1ℓ−10{1ℓ−10, 1ℓ0}∗1ℓ0.
Since the works of Morse and Hedlund [25] it is well-known that all Sturmian
words have the balance property, that is, for all factors u, v of the same length

166 G. RICHOMME, K. SAARI AND L.Q. ZAMBONI

of a Sturmian word, we have ∣
∣
∣
∣u∣
∣
0 − ∣
∣v∣
∣0∣
∣ ≤ 1. Hence, since w1 ends in 1ℓ+1,the
balance property of y implies that 01ℓ−10cannot occurin w.Consequently, we
have w0 ∈ 1ℓ−10{1ℓ0}∗1ℓ0, and the proof is complete. □

Using the previous result, we may rewrite Lemma 3.5 as follows.

Lemma 3.8. Let y be an inﬁnite word over {0, 1},and let k ≥ 1 be an integer.
Then a standard word u is a factor of Lk
0 ◦ L1(y) if and only if one of the following
conditions holds:

(1) u ∈ { Li
0(0),Li
0(1),Li
0(10) | 0 ≤ i< k }
;
(2) u = Lk
0(v) with v a standard factor of L1(y);
(3) u = Lk
0(1ℓ0) with ℓ ≥ 1 and 1ℓ+1 is a factor of L1(y);
(4) u = Lk
0(
1ℓ−10(1ℓ0)
i1ℓ0)
,where ℓ ≥ 1, i ≥ 0,and 1ℓ−10(1ℓ0)
i1ℓ+1 is a
factor of L1(y);
(5) u = Lk−1
0 (
(10)
n1) with n ≥ 1 and 1n+1 afactor of L1(y).

Proof. This statement is obtained by applying Lemma 3.7 to condition (3) of
Lemma 3.5, which then splits into conditions (3) and (4) of the current lemma.
Therefore we only need to make sure that conditions (3) and (4) are suﬃcient.
But this is immediately clear. □

Finally, before proving Theorem 3.1, we formulate the previous lemma into a
more suitable form:

Lemma 3.9. Let y be an inﬁnite word over {0, 1} such that 0 occurs in y.Let
d1,d2,d3 ≥ 1 be integers. A standard word u is a factor of Ld1
0 ◦ Ld2
1 ◦ Ld3
0 ◦ L1(y)
if and only if one of the following conditions holds:

(1) u ∈ { Li
0(0),Li
0(1),Li
0(10) | 0 ≤ i< d1 }
;
(2) u = Ld1
0 (v) with v a standard factor of Ld2
1 ◦ Ld3
0 ◦ L1(y);
(3) u ∈{Ld1
0 (1i0) | 1 ≤ i ≤ d2};
(4) u ∈{Ld1
0 (
1ℓ−10(1ℓ0)
i1ℓ0) | (i =0 and 1 ≤ ℓ ≤ d2) or (1 ≤ i ≤ d3 and ℓ =
d2)};
(5) u ∈{Ld1−1
0 (
(10)
i1) | 1 ≤ i ≤ d2}.

Proof. That conditions (1)–(3) and (5) are suﬃcient is a direct consequence of the
suﬃciency of corresponding conditions in Lemma 3.8. For condition (4), the same
holds since either 01 or 00 occurs in y and thus the word 1d2−10(1d20)
d31d2+1 is a
factor of Ld2
1 ◦ Ld3
0 ◦ L1(y).
Conversely, suppose u is a standard factor of Ld1
0 ◦ Ld2
1 ◦ Ld3
0 ◦ L1(y). In what
follows, we denote z = Ld2
1 ◦ Ld3
0 ◦ L1(y). Lemma 3.8 implies that one of the
following ﬁve cases holds:
Case 1. Condition (1) of Lemma 3.8 holds with k = d1. This is condition (1)
of the present lemma.
Case 2. Condition (2) in Lemma 3.8 holds, and we have u = Ld1
0 (v)with v a
standard factor of z.

STANDARD FACTORS OF STURMIAN WORDS 167

Case 3. Condition (3) in Lemma 3.8 holds, that is, we have

u = Ld1
0 (1ℓ0)

with ℓ ≥ 1and 1ℓ+1 is a factor of z. It is easy to see that 1d2+2 is not a factor
of z; therefore ℓ ≤ d2.
Case 4. Next we suppose that condition (4) in Lemma 3.8 holds. Then

u = Ld1
0 (
1ℓ−10(1ℓ0)
i1ℓ0)
,

where ℓ ≥ 1, i ≥ 0, and 1ℓ−10(1ℓ0)
i1ℓ+1 is a factor of z.Since the word 1d2+2 is
not a factor z,we have ℓ ≤ d2. We may thus assume that i ≥ 1.
Now the word 01ℓ0 is a factor of z.Since z, as any word of the form Ld2
1 (x),
can be factorized over {1d20, 1}, and since ℓ ≤ d2, it follows that ℓ = d2. To ﬁnish
proving this case, we only need to show that i ≤ d3. Indeed, otherwise the word

1d2−10(1d20)
d3+11d2+1

is afactorof z, and it follows that 0d3+2 is a factor of Ld3
0 ◦ L1(y), which is not
possible because 00 is not factor of L1(y).
Case 5. Finally, suppose that condition (5) in Lemma 3.8 holds, that is,

u = Ld1−1
0 (
(10)
n1)

with n ≥ 1and 1n+1 afactorof z.Since 1d2+2 is not a factor of z,we have
n ≤ d2. □

Now we are ready to ﬁnish proving Theorem 3.1.

ProofofTheorem 3.1. From Lemma 2.1, a ﬁnite word u is a standard factor of
cα if and only if E(u) is a standard factor of E(cα). When d1 =0, E(cα)is the
word cβ with β =1 − α =[0; d2 +1,d3,...](see [7], Cor. 2.2.20). Then since
E ◦ L0 = L1 ◦ E (and E ◦ L1 = L0 ◦ E), it is straightforward that if Theorem 3.1
holds for cβ then it holds for cα. So we may assume that d1 ≥ 1.
Suppose that

u = Ld1
0 ◦ Ld2
1 ◦ ... ◦ Ld2k−1
0 ◦ Ld2k
1 (x)with x ∈S(d2k+1,d2k+2,d2k+3).

As noted earlier, x is a standard factor of any characteristic word whose direc-
tive word starts with 0d2k+11d2k+20d2k+3 ... Consequently, by Equation (2.3)and
Lemma 2.1, u is a standard factor of cα. Analogous reasoning works also in the
case when

u = Ld1
0 ◦ Ld2
1 ◦ ... ◦ Ld2k−1
0 ◦ Ld2k
1 ◦ Ld2k+1
0 ◦ E(x)with x ∈S(d2k+2,d2k+3,d2k+4)

because then E(x) is a standard factor of any characteristic word whose directive
word starts with 1d2k+20d2k+31d2k+4 ...

168 G. RICHOMME, K. SAARI AND L.Q. ZAMBONI

Conversely, suppose that u is a standard factor of cα.By equation (2.3), cα =
Ld1
0 ◦ Ld2
1 ◦ Ld3
0 ◦ L1(y) for a word y. Consequently, since we are assuming that d1 ≥
1, Lemma 3.9 applies, and so u satisﬁes one of conditions (1)–(5) of Lemma 3.9.If
u satisﬁes condition (1), (3), (4), or (5), then u ∈S(d1,d2,d3), so we may assume
that condition (2) holds. Then u = Ld1
0 (u1), where u1 is a standard factor of the
characteristic word Ld2
1 ◦ Ld3
0 ◦ Ld4
1 ◦ ...
Denote u′
1 = E(u1). Then u = Ld1
0 ◦ E(u′
1), and u′
1 is a standard factor of the
characteristic word Ld2
0 ◦ Ld3
1 ◦ Ld4
0 ◦ ... Consequently, Lemma 3.9 applies, and so
either u′
1 ∈S(d2,d3,d4)or u′
1 = Ld2
0 (u2), where u2 is a standard factor of the
characteristic word Ld3
1 ◦ Ld4
0 ◦ Ld5
1 ◦ ... In the ﬁrst case, we have

u = Ld1
0 ◦ E(u′
1)and u′
1 ∈S(d2,d3,d4),

and the claim holds. In the second case, we denote u′
2 = E(u2), whence u′
2 is a
standard factor of the characteristic word Ld3
0 ◦ Ld4
1 ◦ Ld5
0 ◦ ... Again, Lemma 3.9
implies that either u′
2 ∈S(d3,d4,d5)or u′
2 = Ld3
0 (u3), where u3 is a standard
factor of the characteristic word Ld4
1 ◦ Ld5
0 ◦ Ld6
1 ◦ ... In the ﬁrst case, we have

u = Ld1
0 ◦ E ◦ Ld2
0 (u2)= Ld1
0 ◦ Ld2
1 (u′
2)and u′
2 ∈S(d3,d4,d5),

and the claim holds. In the second case, we continue the process.
Since di ≥ 1for i ≥ 2, the sequence of lengths of words u1,u2,u3,... is strictly
decreasing, and hence the procedure described above cannot continue forever.
When it stops, we arrive at the form given in the claim. □

4. Characterization via standard words

Here we reformulate Theorem 3.1 to a more constructive form.

Theorem 4.1. Let α =[ 0 ; d1 +1,d2,... ]. Then a ﬁnite standard word u is a
factor of cα if and only if there exists an integer k ≥ 0,or k ≥ 1 if d1 =0,
such that u belongs to one of the following sets (where the si’s correspond to those
deﬁned in Sect. 2):
 { sk,si
ksk−1,si
ksk−1sk | 0 ≤ i< dk+1 }
;
{ si−1
k+1sksi
k+1sk | 1 ≤ i ≤ dk+2 };
{ sdk+2−1
k+1 sksi+1
k+2 | 1 ≤ i ≤ dk+3 };
{ sdk+1−1
k sk−1si
k+1 | 1 ≤ i ≤ dk+2 }.

STANDARD FACTORS OF STURMIAN WORDS 169

Proof. We start with the following four identities; they follow immediately from
equations (2.1)and (2.2). For all k ≥ 0, we have

Ld1
0 ◦ Ld2
1 ◦ ... ◦ Ld2k−1
0 ◦ Ld2k
1 (0) = s2k, (4.1)

Ld1
0 ◦ Ld2
1 ◦ ... ◦ Ld2k−1
0 ◦ Ld2k
1 (1) = s2k−1, (4.2)

Ld1
0 ◦ Ld2
1 ◦ ... ◦ Ld2k−1
0 ◦ Ld2k
1 ◦ Ld2k+1
0 (0) = s2k, (4.3)

Ld1
0 ◦ Ld2
1 ◦ ... ◦ Ld2k−1
0 ◦ Ld2k
1 ◦ Ld2k+1
0 (1) = s2k+1. (4.4)

Next, if x ∈S(d2k+1,d2k+2,d2k+3), then x belongs to one of the following sets:

{ Li
0(0),Li
0(1),Li
0(10) | 0 ≤ i<d2k+1 } = { 0, 0i1, 0i10 | 0 ≤ i<d2k+1 }
;
{ Ld2k+1
0 (1i0) | 1 ≤ i ≤ d2k+2 };
{ Ld2k+1
0 (
1i−101i0) | 1 ≤ i ≤ d2k+2 };
{ Ld2k+1
0 (
1d2k+2−10(1d2k+20)
i1d2k+20) | 1 ≤ i ≤ d2k+3 } =
{ Ld2k+1
0 (
1d2k+2−10(
Ld2k+2
1 (0)
)i+1) | 1 ≤ i ≤ d2k+3 }
;
{ Ld2k+1−1
0 (
(10)
i1) | 1 ≤ i ≤ d2k+2 } =
{ 0d2k+1−11(
Ld2k+1
0 (1)
)i | 1 ≤ i ≤ d2k+2 }
.

Consequently, if

u = Ld1
0 ◦ Ld2
1 ◦ ... ◦ Ld2k−1
0 ◦ Ld2k
1 (x)with x ∈S(d2k+1,d2k+2,d2k+3),

the equations above imply that u is in one of the sets

{ s2k,si
2ks2k−1,si
2ks2k−1s2k | 0 ≤ i< d2k+1 }
,
{ si
2k+1s2k | 1 ≤ i ≤ d2k+2 }
,
{ si−1
2k+1s2ksi
2k+1s2k | 1 ≤ i ≤ d2k+2 }
.
{ sd2k+2−1
2k+1 s2ksi+1
2k+2 | 1 ≤ i ≤ d2k+3 },
{ sd2k+1−1
2k s2k−1si
2k+1 | 1 ≤ i ≤ d2k+2 }.

Similarly, if

u = Ld1
0 ◦ Ld2
1 ◦ ...◦ Ld2k−1
0 ◦ Ld2k
1 ◦ Ld2k+1
0 ◦ E(x)with x ∈S(d2k+2,d2k+3,d2k+4),

170 G. RICHOMME, K. SAARI AND L.Q. ZAMBONI

then it follows from the equations above that u is in one of the sets

{ s2k+1,si
2k+1s2k,si
2k+1s2ks2k+1 | 0 ≤ i< d2k+2 }
,
{ si
2k+2s2k+1 | 1 ≤ i ≤ d2k+3 }
,
{ si−1
2k+2s2k+1si
2k+2s2k+1 | 1 ≤ i ≤ d2k+3 }
,
{ sd2k+3−1
2k+2 s2k+1si+1
2k+3 | 1 ≤ i ≤ d2k+4 }
,
{ sd2k+2−1
2k+1 s2ksi
2k+2 | 1 ≤ i ≤ d2k+3 }
.

Applying Theorem 3.1, it follows that u is a standard factor of cα if and only if
there exists an integer k ≥ 0, or k ≥ 1if d1 = 0, such that u is in one of the
following sets
 { sk,si
ksk−1,si
ksk−1sk | 0 ≤ i< dk+1 }
,
{ si
k+1sk | 1 ≤ i ≤ dk+2 }
,
{ si−1
k+1sksi
k+1sk | 1 ≤ i ≤ dk+2 },
{ sdk+2−1
k+1 sksi+1
k+2 | 1 ≤ i ≤ dk+3 },
{ sdk+1−1
k sk−1si
k+1 | 1 ≤ i ≤ dk+2 }.

Now the formulation of the statement is obtained by observing that sets of the
form { si
k+1sk | 1 ≤ i ≤ dk+2 }

are included in the union of sets of the form

{ sk,si
ksk−1,si
ksk−1sk | 0 ≤ i< dk+1 }
.

This completes the proof. □

Example 4.2. Let us denote fn = ϕ
n(0) for n ≥ 0and f−1 = 1. Then the charac-
terization of the standard factors of the Fibonacci word f given by Theorem 4.1 is

{ fn−1,fn−1fn,fnfn+2fn+2,fn−1fn+1 | n ≥ 0 },

which is clearly the same set we obtained in Example 3.3.

5. Characterization via the directive sequence

In this section, we characterize the standard factors of a Sturmian word in terms
of their directive sequences, and show how this can be used for characterizing
standard factors in terms of palindromic closure.

STANDARD FACTORS OF STURMIAN WORDS 171

Theorem 5.1. Let α =[ 0 ; d1 +1,d2,... ]. A ﬁnite standard word u is a factor
of cα if and only if it has one of the following directive sequences, where k ≥ 0,or
k ≥ 1 if d1 =0:

1. empty sequence, (0), (0, 1);
2. (d1,d2,...,dk−1,dk,i), 1 ≤ i ≤ dk+1 +1;
3. (d1,d2,...,dk−1,dk,i, 1), 1 ≤ i ≤ dk+1 +1;
4. (d1,d2,...,dk−1,dk,dk+1,i, 1, 1), 1 ≤ i< dk+2;
5. (d1,d2,...,dk+1,dk+2 − 1, 1,i +1), 1 ≤ i ≤ dk+3 if dk+2 ̸=1;
6. (d1,d2,...,dk−1,dk,dk+1 +1,i +1), 1 ≤ i ≤ dk+3 if dk+2 =1;
7. (d1,d2,...,dk,dk+1 − 1, 1,i), 1 ≤ i ≤ dk+2 if dk+1 ̸=1;
8. (d1,d2,...,dk−1,dk +1,i), 1 ≤ i ≤ dk+2 if dk+1 =1
and k ̸=0;
9. (0, 1,i), 1 ≤ i ≤ d2 if d1 =1.

Remark 5.2. In the previous theorem, some items (e.g.,5 and 7) give the same
directive sequences for some instances of dk and i. Nevertheless, no set of directive
sequences corresponding to an item is included in another.

ProofofTheorem 5.1. Theorem 5.1 is a direct consequence of Theorem 4.1.Below
we show the correspondence between words occurring in Theorem 4.1 and their
directive sequences. More precisely, using the characterization of standard factors
of cα in Theorem 4.1, we show that each of the standard factors has a directive
sequence listed above. The converse can be seen with a similar construction.
By [form n] we indicate that the directive sequence is of the form of the nth
item in Theorem 5.1. Thus for each item, looking at all directive sequences on this
form for all k ≥ 0, one can verify the possible values for i.

• The directive sequence of the word sk is
{ (d1,...,dk)if k ̸= 0, [form 2][form 3 when dk =1 and k ≥ 2]
the empty sequence if k =0. [form 1]

• The directive sequence of the word si
ksk−1 for k ≥ 0and 0 ≤ i< dk+1 is
⎧
⎪⎪⎨

⎪⎪⎩
 (d1,... ,dk−1,dk,i)if i ̸= 0, [form 2] [form 3 when i =1 and k ≥ 1]
(d1,... ,dk−1)if i =0 and k ≥ 2, [form 2]
the empty sequence if i =0 and k =1, [form 1]
(0) if i =0 and k =0. [form 1]

• The directive sequence of the word si
ksk−1sk for k ≥ 0and 0 ≤ i< dk+1 is
⎧
⎨

⎩
 (d1,... ,dk−1,dk,i, 1) if i ̸= 0 (sequence (i, 1) when k =0), [form 3]
(d1,... ,dk−1,dk +1) if i =0 and k ̸=0, [form 2]
(0, 1) if i =0 and k =0. [form 1]

For the second case, note that sk−1sk = sdk+1
k−1 sk−2.

172 G. RICHOMME, K. SAARI AND L.Q. ZAMBONI

• Thedirectivesequenceof the word si−1
k+1sksi
k+1sk for k ≥ 0and 1 ≤ i ≤
dk+2 is
{ (d1,...,dk,dk+1,i − 1, 1, 1) if i ̸=1, [form 4]
(d1,...,dk,dk+1 +1, 1) if i =1. [form 3]

For the second case, note that sksk+1sk = sdk+1+1
k sk−1sk.
• The directive sequence of the word sdk+2−1
k+1 sksi+1
k+2 for k ≥ 0and 1 ≤ i ≤
dk+3 is
{ (d1,...,dk,dk+1,dk+2 − 1, 1,i +1) if dk+2 ̸=1, [form 5]
(d1,...,dk,dk+1 +1,i +1) if dk+2 =1. [form 6]

In the ﬁrst case we used sdk+2−1
k+1 sksi+1
k+2 =(sdk+2−1
k+1 sksk+1)
i+1sdk+2−1
k+1 sk;

the second case follows from sksi+1
k+2 = sk(sk+1sk)
i+1 =(sdk+1+1
k sk−1)
i+1sk.

• The directive sequence of the word sdk+1−1
k sk−1si
k+1 for k ≥ 0and 1 ≤ i ≤
dk+2 is
⎧
⎨

⎩
 (d1,... ,dk,dk+1 − 1, 1,i)if dk+1 ̸=1, [form 7]
(d1,... ,dk +1,i)if dk+1 =1, k ̸=0, [form 8]
(0, 1,i)if dk+1 =1, k =0. [form 9]. □

Next we will recall a result by de Luca connecting the directive sequence of a
standard word and palindromic closures ([15], p. 66).
Each word w over {0, 1} is uniquely determined by a ﬁnite sequence (h1,
h2,...,hn) of integers, where h1 ≥ 0, hi > 0for 1 <i< n and w =0h11h20h3 ...;
such a representation of w is called its integral representation.

Proposition 5.3 (de Luca). Let w ∈{0, 1}∗,and let (h1,h2,...,hn) be its integral
representation. The standard words Pal(w)01 and Pal(w)10 have the directive
sequences

(h1,...,hn, 1) and (h1,... ,hn +1)

if n is even, and

(h1,...,hn +1) and (h1,...,hn, 1)

if n is odd, respectively.

We have the following immediate corollary of the previous proposition.

Corollary 5.4. If s is a standardwordoflengthatleast 2 with directive sequence
(d1,... ,dn) then

s = Pal(0d11d2 ... 0dn−11dn−1)10, when n is even,
s = Pal(0d11d2 ... 1dn−10dn−1)01, when n is odd.

Now one can use Corollary 5.4 to present the standard factors of a Sturmian word
by using the directive sequences given in Theorem 5.1 and the palindromic closure

STANDARD FACTORS OF STURMIAN WORDS 173

operation. We did not do this since the statement of this result involves a lot of
cases (more than in Thm. 5.1) and so does not seem interesting.
However, the Fibonacci word is a special case, as shown in the next example.

Example 5.5. In this example we present a characterization of the standard
factors of the Fibonacci word that is essentially diﬀerent from the ones in Exam-
ples 3.3 and 4.2.
The directive sequence of the Fibonacci word is (1, 1, 1,...). Thus Theorem 5.1
says that the directive sequences of the standard factors of the Fibonacci word are
of the following form:

• empty sequence, (0), (0, 1),
• (1, 1,... , 1, 1),
• (1, 1,... , 1, 2), possibly with no preceding 1’s; that is (2), (1, 2), (1, 1, 2),...,
• (1, 1,... , 1, 2, 1), possibly with no preceding 1’s; that is (2, 1), (1, 2, 1),...,
• (1, 1,... , 1, 2, 2), possibly with no preceding 1’s; that is (2, 2), (1, 2, 2),...,
• (0, 1, 1).

Therefore, by Corollary 5.4, the standard factors of the Fibonacci word are

• 0, 1, 01, 10, 101;
• For each nonempty preﬁx u of (01)
∞,the words Pal(u)01 and Pal(u)10;
• For each nonempty preﬁx u of (01)
∞ of odd length, the words Pal(u0)10
and Pal(u01)10;
• For each nonempty preﬁx u of (01)
∞ of even length, the words Pal(u1)01
and Pal(u10)01.

To conclude let us mention that most of the previous characterizations can cer-
tainly be extended to the more general case of episturmian words [16,17]using
links between episturmian morphisms and directive sequences of these words de-
ﬁned over arbitrary alphabet (see, e.g.,[18]). Nevertheless the main problem
should be a combinatorial explosion.

References

[1] J.-P. Allouche and V. Berth´e, Words in number theory, edited by M. Lothaire. Applied
Combinatorics on Words, Cambridge University Press (2005) 520–574.
[2] J.-P. Allouche and J. Shallit, Automatic sequences. Cambridge University Press (2003).
[3] E. Altman, B. Gaujal and A. Hordijk, Balanced sequences and optimal routing. J. ACM 47
(2000) 752–775.
[4] P. Arnoux, Sturmian sequences,edited by P.Fogg. Substitutions in dynamics, arithmetics
and combinatorics, Lect. Notes Math. 1794 (2002) 143–198.
[5] J. Berstel, Sturmian and episturmian Words (a survey of some recent results), edited by
S. Bozapalidis and G. Rahonis. Conference on algebraic informatics (CAI’07), Lect. Notes
Comput. Sci. 4728 (2007) 23–47.
[6] J. Berstel and A. de Luca, Sturmian words. Lyndon words and trees. Theoret. Comput. Sci.
178 (1997) 171–203.
[7] J. Berstel and P. S´e´ebold, Sturmian words, edited by M. Lothaire. Algebraic combinatorics
on words, Cambridge University Press (2002) 45–110.

174 G. RICHOMME, K. SAARI AND L.Q. ZAMBONI

[8] J. Berstel, A. Lauve, C. Reutenauer and F. Saliola, Combinatorics on words: Christoﬀel
words and repetition in words. CRM Monograph Series, Vol. 27, CRM-AMS Montr´eal
(2008).
[9] V. Berth´e, C. Holton and L.Q. Zamboni, Initial powers of Sturmian sequences. Acta Inform.
122 (2006) 315–347.
[10] E. Bombieri and J.E. Taylor, Which distributions of matter diﬀract? An initial investigation.
J. Phys. 47 (1986) 19–28.
[11] J. Cassaigne, On extremal properties of the Fibonacci word. RAIRO-Theor. Inf. Appl. 42
(2008) 701–715.
[12] C. Choﬀrut and J. Karhum¨aki, Combinatorics of words, edited by G. Rozenberg and A.
Salomaa. Handbook of Formal Languages 1, Springer (1997).
[13] W.-f. Chuan, Unbordered factors of the characteristic sequences of irrational numbers. The-
oret. Comput. Sci. 205 (1998) 337–344.
[14] J.D. Currie and K. Saari, Least periods of factors of inﬁnite words. RAIRO-Theor. Inf.
Appl. 43 (2009) 165–178.
[15] A. de Luca, Sturmian words: structure, combinatorics, and their arithmetics. Theoret. Com-
put. Sci. 183 (1997) 45–82.
[16] X. Droubay, J. Justin and G. Pirillo, Episturmian words and some constructions of de Luca
and Rauzy. Theoret. Comput. Sci. 255 (2001) 539–553.
[17] A. Glen and J. Justin, Episturmian words: a survey. RAIRO-Theor. Inf. Appl. 43 (2009)
403–442.
[18] A. Glen, F. Lev´e and G. Richomme, Directive words of episturmian words: equivalence and
normalization. RAIRO-Theor. Inf. Appl. 43 (2009) 299–319.
[19] T. Harju and D. Nowotka, Minimal Duval Extensions. Int. J. Found. Comput. Sci. 15 (2004)
349–354.
[20] R. Klette and A. Rosenfeld, Digital straightness – a review. Discrete Appl. Math. 139 (2004)
197–230.
[21] M. Lothaire, Algebraic Combinatorics on Words. Cambridge University Press (2002).
[22] G. Melan¸con, Lyndon factorization of Sturmian words. Discrete Math. 210 (2000) 137–149.
[23] F. Mignosi and L.Q. Zamboni, A note on a conjecture of Duval and Sturmian words. RAIRO-
Theor. Inf. Appl. 36 (2002) 1–3.
[24] M. Morse and G.A. Hedlund, Symbolic dynamics. Amer. J. Math. 60 (1938) 815–866.
[25] M. Morse and G.A. Hedlund, Symbolic dynamics II: Sturmian trajectories. Amer.J.Math.
62 (1940) 1–42.
[26] G. Richomme, Conjugacy of morphisms and Lyndon decomposition of standard Sturmian
words. Theoret. Comput. Sci. 380 (2007) 393–400.
[27] K. Saari, Everywhere α-repetitive sequences and Sturmian words, in Proc. CSR 2007. Lect.
Notes Comput. Sci. 4649 (2007) 363–372.
[28] K. Saari, On the frequency and periodicity of inﬁnite words.Ph.D. Thesis,University of
Turku, TUCS Dissertations 97 (2008).
