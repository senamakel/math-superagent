<!-- source: https://hal.science/hal-01827511/document | converted from PDF -->

HAL Id: hal-01827511

https://hal.science/hal-01827511v1

Preprint submitted on 2 Jul 2018

HAL is a multi-disciplinary open access archive
for the deposit and dissemination of scientific re-
search documents, whether they are published or not.
The documents may come from teaching and research
institutions in France or abroad, or from public or pri-
vate research centers.
 L’archive ouverte pluridisciplinaire HAL, est des-
tinée au dépôt et à la diffusion de documents scien-
tifiques de niveau recherche, publiés ou non, émanant
des établissements d’enseignement et de recherche
français ou étrangers, des laboratoires publics ou
privés.

HAL Authorization

Formal Intercept of Sturmian words

Caïus Wojcik

To cite this version:

Caïus Wojcik. Formal Intercept of Sturmian words. 2018. ⟨hal-01827511⟩arXiv:1803.02073v1  [math.CO]  6 Mar 2018Formal intercepts of Sturmian words

Caïus Wojcik

Abstract
We introduce the concept of formal intercept of Sturmian words, de-
ﬁned as an inﬁnite sequence of integers written in Ostrowski expansion.
We ﬁrst recall the combinatorial proofs of basics properties of sturmian
words. Then, we study the Rauzy graphs and repetition functions of Stur-
mian words. In the last part, we deﬁne the formal intercept associated to
a sturmian word.

Sturmian words are deﬁned as the inﬁnite words having lowest unbounded
complexity. They enjoy rich combinatorial structures, that are sometimes diﬃ-
cult to quantify. However, unlike most of other dynamical systems, in the case
of sturmian words one can hope to ﬁnd some explicit combinatorial formulas.
In order to describe the combinatorial properties of Sturmian words, we give
here a combinatorial description of the second parameter in the caracterisation
of sturmian words. The ﬁrst parameter, well-known, is the slope, which is an
irrational number in ]0, 1[, whose continued fraction expansion describes the set
of factors of a sturmian word. The second parameter, the intercept, has been
deﬁned dynamicaly in the litterature, but its combinatorial implications in the
structure of sturmian words were not well understood in the author’s view.
In this paper, which is the ﬁrst of two about formal intercepts, we deﬁne
the formal intercept of a given Sturmian word, and show that there is a natural
bijection between Sturmian words of a given slope, and the formal intercepts
associated to this slope. Since we insist on the combinatorial properties of such
parameters, and for sake of completeness, we start from the bottom about Stur-
mian words, and give entierely combinatorial proofs of their basic properties.
The paper is organized as follows. In the ﬁrst section, we recall the proofs
of basic properties of sturmian words. In the second part of the paper, we give
a description of the factor graph and some links with the repetition function of
Sturmian words. In the last part, we deﬁne the formal intercept of Sturmian
word.

1 Basic properties

In this section we give combinatorial proofs of the main properties about stur-
mian words. All these come from the classical book [1], rewritten in a concise

1

manner.

1.1 The Morse-Hedlund theorem

Let A be a ﬁnite set, the alphabet. A ﬁnite ord over A is an element of the
union ∪nA
n, and if u ∈ A
n, we set |u| = n and call it its length. For a letter
a ∈ A we note |u|a the number of occurrences of the letter a in u.
An inﬁnite word x = x1x2x3 . . . is an element of A
N. A factor of x is a ﬁnite
word occurring in x. For such an inﬁnite word, we note Pn(x) = x1x2 . . . xn
its preﬁx of length n, and we note T (x) = x2x3x4 . . . the shifted of x, which
consists of the inﬁnite word x deprived of its ﬁrst letter. A suﬃx of x is an
element of the form T k(x) for some k ≥ 1.

Deﬁnition 1. Let x = x1x2x3 . . . be an inﬁnite word. For n ≥ 1, set

p(x, n) = Card{xixi+1 . . . xi+n−1 | i ≥ 1}

and call p(x, ·) the complexity function of x.

Theorem 1 (Morse-Hendlund). Let x be an inﬁnite word over A. Then x is
ultimately periodic if and only if there exists n ≥ 1 such that p(x, n) ≤ n.

Proof. The condition is clearly necessary, since a ultimately periodic word has
bounded complexity function. For the converse, from the increasing of the
complexity function and the pigeonhole principle, there exists n ∈ N∗ such that
p(x, n) = p(x, n + 1). That means that every factor u of x can be only uniquely
extend on the right. Let u be a factor of x having two occurrences in x. The
two corresponding suﬃxes of x are uniquely determined by u, and hence are
equal, showing that x is ultimately periodic.

This theorem can be reformulated as follows : if x is a non-ultimately peri-
odic word, then p(x, n) ≥ n + 1 for all n ≥ 1.

Deﬁnition 2. An inﬁnite word is said to be Sturmian if

∀n ≥ 1, p(x, n) = n + 1.

Notice that a Sturmian word x is a word over a 2-letter alphabet, since
p(x, 1) = 2, so we assume from now on that A = {0, 1}. Also, notice that since
T (x) is non-ultimately periodic, T (x) and x share the same set of factors.
For all n ≥ 1, there exists a unique factor Ln of x of length n such that
both 0Ln and 1Ln are factor of x, called the left special factor of x of length
n. Similarly, deﬁne the right special factor Rn of x as the unique factor of x of
length n such that both Rn0 and Rn1 are factors of x.

1.2 Slopes and balanced words

Deﬁnition 3. A word over A = {0, 1} is said to be balanced if for all pair of
factors u, v with |u| = |v| we have
 2

||u|1 − |v|1| ≤ 1.

Lemma 1. A word x is balanced if and only if for all palindrome w, 0w0 and
1w1 are not both factors of x.

Proof. Note that the direct implication holds for any word w. For the converse,
we take u and v of minimal length such that ||u|1 − |v|1| > 1, and we show that
{u, v} = {0w0, 1w1} for some palindrome w.
The minimality hypothesis implies that u and v start with diﬀerent letters,
and let w be the longest common preﬁx of u∗ and v∗, where the star denotes a
word deprived of its ﬁrst letter. Write

u = awcu′ and v = bwdv′

with a, b, c, d ∈ {0, 1} and a ̸= b. Since the couple (u′, v′) cannot satisfy the
balanced property by minimality, we must have c = a and d = b. From this the
words u′ and v′ must be empty, 0w0 and 1w1 factors of x.
In order to show that w is a palindrome, let t be the longest common preﬁx
of w and ˜w where the tilda denotes the reversal of a word and assume by
contradiction that t ̸= w. Let a be the letter following t in w and ¯a the opposite
letter. If a = 0 then 0t0 is a preﬁx of 0w0 and 1˜t1 is a suﬃx of 1w1, contradicting
the minimality hypothesis. If a = 1 then writing 0w0 = 0t1u′ and 1w1 = v′0˜t1
oﬀers a pair u′, v′ contradicting the minimality hypothesis.

Theorem 2. 1) An inﬁnite balanced word satisﬁes ∀n ∈ N∗, p(x, n) ≤ n + 1.

2) An inﬁnite word over A = {0, 1} is Sturmian if and only if he is balanced
and non-ultimately periodic.

Proof. 1) Let x be a balanced word and suppose that there is n ∈ N∗ such that
p(x, n + 1) ≥ p(x, n) + 2. Then x has two distincts left special factors y and z,
and let w be their longest common preﬁx. Then both 0w0 and 1w1 are factors
of x, in contradiction with the balanced hypothesis.
2) A non-ultimately periodic word satisfy ∀n ∈ N∗, p(x, n) ≥ n + 1 by the
Morse & Hedlund theorem. Combined with 1), we get the suﬃcient condition.
For the converse, we have to show that a Sturmian word x is necessarily
balanced. Arguing by contradiction and using the Lemma, we assume that
there is a palindrome w such that both 0w0 and 1w1 are factors of x. The word
w is a right special factor of x, and one of the words 0w or 1w is a right special
factor, and we assume without loss of generality that 0w is a right special factor.
By the unicity of right special factors of a given length for Sturmian words, 1w
is not a right special factor. So the three words 0w0, 1w1 and 0w1 are factors
of x although 1w0 is not.
Let u = 1w1v be a factor of x with the preﬁx 1w1 and |v| = |w|. We show
that the right special factor of x of length |w| + 1, namely 0w, is not a factor of
u. Suppose this is the case and write the word u as :

u = 1w1v = λ0wµ

3

and let t be the word such that u = λ0t1v. The word t is both a preﬁx and a
suﬃx of w, and we also see that t1 is a preﬁx of w and that 0t is a suﬃx of w.
But since w is a palindrome, the (|t| + 1)
th letter of w is both a 0 and a 1, and
that’s a contradiction.
We’ve just shown that no factor of u = 1w1v of length n = |w| + 1 is a
right special factor. Since there is at most n such factors, and |u| = 2n, there
is a factor ν of length n in u that occurs twice. Let’s show that this implies
that x is ultimately periodic, hence proving the theorem. Let’s note y the suﬃx
of x beginning at the ﬁrst occurrence of ν, and z the suﬃx of x beginning at
its second occurrence. The two inﬁnite words y and z share the same preﬁx of
length n, but since this preﬁx is not a right special factor, its following letter in
y and z is uniquely determined, so that y and z share the same preﬁx of length
n + 1. And the letter following this preﬁx is also uniquely determined since the
preceeding word of length n appears in u and so is not a right special factor.
This argument goes on and on, so that we must have y = z. There are two
suﬃxes of the inﬁnite word x, taken at diﬀerent starting point, that are equal.
This shows that x is ultimately periodic.

The following proposition is an extension of the balanced property.

Proposition 1. A word x is balanced if and only if for all factors u, v of x we
have ∣
∣
∣
∣ |u|1
|u| − |v|1
|v|
 ∣
∣
∣
∣ < 1
|u| + 1
|v| .

Proof. The suﬃcient condition is clear by taking two words of the same length.
Conversely, we show the result by induction on max |u|, |v|. If |u| = |v| then
the result follows directly from the balanced property. If |u| > |v|, write u = st
with |s| = |v|. From the balanced property on the one hand, and the induction
hypothesis on the other, we have :
∣
∣
∣
∣ |s|1
|s| − |v|1
|v|
 ∣
∣
∣
∣ ≤ 1
|v|

∣
∣
∣
∣ |t|1
|t| − |v|1
|v|
 ∣
∣
∣
∣ < 1
|t| + 1
|v|

we also have by simple calculation :

|u|1
|u| − |v|1
|v| = |s|
|u|
 ( |s|1
|s| − |v|1
|v|
 ) + |t|
|u|
 ( |t|1
|t| − |v|1
|v|
 )

so that ∣
∣
∣
∣ |u|1
|u| − |v|1
|v|
 ∣
∣
∣
∣ < |s|
|u| × 1
|v| + |t|
|u|
 ( 1
|t| + 1
|v|
 ) = 1
|u| + 1
|v|

wich ends the proof.
 4

This proposition shows that the family of numbers (|u|1/|u|) behave like a
Cauchy sequence when u runs through the factors of a balanced word x. Hence
we can deﬁne :

Deﬁnition 4. Let x be a balanced word. We deﬁne the slople α of x as the
number
 lim
|u|→+∞ |u|1
|u|

where the limit is taken over the factors of x.

By using this deﬁnition in the second caracterisation of balanced word, we
get the speed relation : ∣
∣
∣
∣ |u|1
|u| − α
∣
∣
∣
∣ ≤ 1
|u|

for every factor u of a balanced word of slope α.
If a word is ultimately periodic, then its slope is a rational number. The
following theorem shows that the converse is true for balanced word.

Theorem 3. 1) A balanced word is Sturmian if and only if its slope is irra-
tional.

2) Two balanced words of diﬀerent slope only share a ﬁnite number of factors.

3) Two Sturmian words of same slope have same set of factors.

Proof. 1) Suppose that α = p/q is the slope of a Sturmian word x, with p, q
integers. Assume ﬁrst that for every factor u of x such that |u| = q we have
|u|1 = p. If w is any factor of x of length q + 1, then by assumption, the preﬁx
and suﬃx of length q have the same number of 1’s, so that w must begin and
end with the same letter, showing that x is ultimately periodic. Suppose now
that there is an inﬁnity of factors u of x such that |u| = q and |u| ̸= p. By the
balanced property and without loss of generality we can assume |u|1 = p + 1 for
an inﬁnity of such factors. Let u and v be two non-crossing such factors and
w = uzv a factor of x. From the relations :
∣
∣
∣
∣|w|1 − p
q |w|∣
∣
∣
∣ = ∣
∣
∣
∣2 + |z|1 − p
q |z|∣
∣
∣
∣ ≤ 1 and ∣
∣
∣
∣|z|1 − p
q |z|
∣
∣
∣
∣ ≤ 1

we get
 |z|1 − p
q = −1

then ∣
∣
∣
∣ |u|1
|u| − |z|1
|z|
 ∣
∣
∣
∣ = ∣
∣
∣
∣ |u|1
|u| − p
q − ( |z|1
|z| − p
q
 )∣
∣
∣
∣ = ∣
∣
∣
∣ 1
q + 1
|z|
 ∣
∣
∣
∣ = 1
|u| + 1
|z|

5

contradicting the strict inequality in the second caracterisation of balanced
words.
2) The speed relation implies that for two distincts slopes α and β, a ﬁnite
word that is too long cannot be a common factor of two balanced words of slope
α and β.
3) We ﬁrst show that two Sturmian words have same set of left special
factors. Let x and y be two Sturmian words of slope α. Write Ln(x) and Ln(y)
for the left special factor of length n ≥ 1 of x and y respectively. From the strict
inequality ∣
∣
∣
∣ |u|1
|u| − α
∣
∣
∣
∣ < 1
|u|

satisﬁed by the 2-letters factors

0L1(x), 1L1(x), 0L1(y), 0L1(y),

we see that 2α must lie in the two open balls of radius 1 and center |L1(x)|1 and
|L1(x)|1 + 1, determining uniquely the number |L1(x)|1 which has to be equal to
|L1(y)|1. Since they are both letters, we have |L1(x)|1 = |L1(y)|1. Recall that
two left special factors of a Sturmian word are preﬁx of one another, so that
we can prove the result by induction : suppose that Ln−1(x) = Ln−1(y), and
by the same argument we have |Ln(x)|1 = |Ln(y)|1 and so Ln(x) = Ln(y). Let
cα = lim Ln(x) = lim Ln(y), then cα is a balanced word that is not ultimately
periodic since its slope is irrationnal, so cα is a Sturmian word, and by the
cardinality of the sets of factors involved, we see that x, y and cα share the
same set of factors.

Deﬁnition 5. For all Sturmian word of slope α, the sequence (Ln) of its left
special factors deﬁnes a Sturmian word :

cα = lim Ln

which depends only on the slope α, noted cα and called the caracteristic Sturmian
word of slope α.

Proposition 2. Let (Ln) and (Rn) be the sequences of left special factors and
right special factors respectively of a Sturmian word. Then :

1) The Sturmian word x is caracteristic if and only if both 0x and 1x are Stur-
mian.

2) cα = lim ̃Rn

3) ∀n ∈ N∗, Rn = ̃Ln

4) The set of factors of a Sturmian word is stable under reversal,

5) For all Sturmian word x, at least one of the words 0x and 1x is Sturmian

6

Proof. 1) If both 0x and 1x are Sturmian, then all the preﬁxes of x are left
special, so x = lim Ln = cα.
2) Since the right special factors are suﬃxes of one another, the word c =
lim ̃Rn is well-deﬁned, balanced and of irrational slope, so it is Sturmian. Be-
sides, both 0c and 1c are Sturmian, so that c = cα by 1).
3) Obvious since cα = lim Ln = lim ̃Rn.
4) Obvious from 3) and the fact that a Sturmian word and the caracteristic
word of same slope share the same set of factors.
5) It is clear if x is caracteristic. Let u be a preﬁx of x that is not left
special. Then by 4) there is a unique letter a ∈ {0, 1} such that au is a factor
of x, and this letter does not depend on u. The word ax is then balanced and
non-ultimately periodic, so it is Sturmian.

1.3 Caracteristic words and continued fractions

Recall that every irrational number α ∈]0, 1[ can be written uniquely in the
form
 α = [0; a1, a2, . . .] = 1

a1 + 1

a2 + 1
a3 + . . .

with ai ∈ N∗ for i ≥ 1. The coeﬃcient (ai) are called the partial quotient of α.
We deﬁne the positive integers pn and qn as the irreducible quotient

pn
qn = [0; a1, . . . , an]

and we set q−1 = 0 and q0 = 1. We call the sequence (qn) the sequence of
continuant of α. We have the induction relation

qn+1 = an+1qn + qn−1

for n ≥ 0. Notice that for all n ≥ 0, qn+1 and qn are relatively prime (the
induction steps are the steps of Euclide’s algorithm).

Theorem 4. Let α = [0; a1, a2, . . .] be an irrational number in ]0, 1[. Deﬁne the
sequence of words :
 s−1 = 1, s0 = 0, s1 = sa1−1
0 s−1,

sn+1 = san+1
n sn−1

for all n ≥ 1. Then :
 cα = lim sn.

Proof. Deﬁne the two morphisms
 7

E : 0 ↦−→ 1
1 ↦−→ 0 and G : 0 ↦−→ 0
1 ↦−→ 01
,

they are injective, in the sense that if x and y are two inﬁnite words such that
G(x) = G(y), then x = y, and the same for E. We obviously have that x is
sturmian if and only if E(x) is sturmian. Let’s show now that x is Sturmian if
and only if G(x) is Sturmian.
Suppose that G(x) is unbalanced : there exists a palindrome w such that
both 0w0 and 1w1 are factors of G(x). In view of G there must exist a word z
such that w = 0z0, moreover 01w1 = 010z01 is a factor of G(x). There must
be a word y such that 0z = G(y) and 01w1 = G(1y1) so that 1y1 is a factor
of x by injectivity of G. On the other hand 0w0 = 00z00 = G(0y0) is a factor
of G(x) and so 1y1 is a factor of x. Both 0y0 and 1y1 are factors of x so x is
unbalanced. This shows that if x is Sturmian then G(x) is balanced, and it is
not hard to see that its slope is irrational, so G(x) is Sturmian.
Conversely, if G(x) is Sturmian, then x is Sturmian. Indeed, suppose that x
is unbalanced, namely let w be a palindrome such that both 0w0 and 1w1 are
factors of x. Then both 0G(w)0 and 01G(w)01 are factors of G(x). In view of
G, 0G(w)00 is a preﬁx of G(0w0a) for any letter a, so that both 0G(w)00 and
1G(w)01 are factors of G(x), showing at once that G(x) is unbalanced. It is
clear from the slopes that if G(x) is not ultimately periodic, then x is also not
ultimately periodic.
Let m be the greatest m ≥ 1 such that 0m1 is a factor of cα. Suppose m ≥ 2,
by the balanced property, the words 10k1 for k = 0 . . . m − 2 cannot be factors
of cα, and we see that 10m−11 must be a factor of cα for otherwise cα would be
ultimately periodic. If m = 1, then we easily see that 11 must be a factor of cα.
So the word 0m−11 is left special and hence a preﬁx of cα. All this sums up to
the fact that cα can be factorised in an inﬁnite concatenation of the two words
0m−11 and 0m−110 for some m ≥ 1.
We deﬁne the morphisms, for m, n ≥ 1 :

θm = G
m−1 ◦ E ◦ G and hn = θa1 ◦ θa2 ◦ · · · ◦ θan .

Since θm(0) = 0m−11 and θm(1) = 0m−110, we have seen that cα factorises as
cα = θm(x) for some x, that must be Sturmian. For m ≥ 1, we have θm(0cα) =
0m−11θm(cα) and θm(1cα) = 0m−110θm(cα) so that θm(cα) is caracteristic and,
according to the slopes, we have

θm(cα) = c 1
m+α .

so that for all n ≥ 1 we have :

hn(c[0;an+1,an+2,...]) = cα.

Moreover, we have hn(0) = sn and hn(1) = snsn−1 as it is easily checked by
induction on n ≥ 1. This shows that sn is a preﬁx of cα for all n ≥ 1, proving
the theorem.
 8

1.4 Standard and central words

Deﬁnition 6. The subset of (A
∗)
2 of standard pairs is recursively deﬁned by
the rules :

• (0, 1) is a standard pair,

• if (u, v) is a standard pair, then (vu, v) and (u, uv) are standard pairs.

We recall the notation x
− for a word x deprived of its last letter. If x is
empty, then we set x
− to be the empty word.

Proposition 3. Let (u, v) be a standard pair.

1) (uv)
−− = (vu)
−−,

2) if |u| ≥ 2, u ends with 10. If |v| ≥ 2, u ends with 01

3) u−− and v−− are palindromes.

4) We have |u||v|1 − |u|1|v| = 1.

The proofs of proposition 3 are straightforward inductions.

Deﬁnition 7. A word is said to be standard if it is a coponent of a central pair.

Proposition 4. 1. If u is standard, then u−− is palindromic.

2. A standard word is primitive (that is, not a non-trivial power of a word).

3. The words (sn) in theorem 4 are standard. The suﬃx of length 2 of sn is
tn, where tn = 10 if n is even, and tn = 01 if n is odd, for n ≥ 2.

Proof. 1) The fact that u−− is palindromic is trivial from proposition 3.
2)The word u is primitive since by proposition 3−4), |u| and |u|1 are coprime.
3) We see by the deﬁnition of the sequence (sn) that (s2n, s2n−1) and (s2n, s2n+1)
are standard pairs for all n ≥ 0. The remaining part of the assertion is clear by
proposition 3.

Deﬁnition 8. We deﬁne the set of central words by one of the following equiv-
alent deﬁnitions :

(i) a word w is central if and only if there exists a standard word u such that
w = u−−,

(ii) the set of central words is inductively deﬁned as follows :

• powers of a letter are central words

• if p and q are central, and p01q is a palindrome, then p01q is central

(iii) a word w is central if and only if it is a power of a letter, or a palindrome
of the form p01q with p, q palindromes,

9

(iv) a word is central if and only if it is a preﬁx palindrome of a caracteristic
word.

The decomposition w = p01q with p, q palindrome of a central word that is not
a power of a letter is then unique.

Proof. (ii)-central ⇔ (iii)-central : It is clear from the deﬁnition (ii) that (ii)-
central words are palindromes, so that (ii)-central ⇒ (iii)-central. For the
converse, it is suﬃcient to show that if w = p01q is a palindrome with p and
q palindrome is (iii)-central, then p and q are (iii)-central. We cannot have
|p| = |q| since w is a palindrome, and we can assume that |p| ≤ |q| − 1. If
|p| = |q| − 1 then q = p0 = 0p and p, q are powers of letters. If |p| = |q| − 2 then
q = p01u and since w = p01˜u10p is a palindrome, u is a palindrome and q is
(iii)-central. By continuing this argument with q in the place of w, we see that
there exists a unique N ≥ 1 such that q = (p01)
N t with |t| ≤ |p| − 1, so that
p01t is (iii)-central with |t| ≤ |p| − 1, and in this situation we have seen that p
is (iii)-central.
(ii)-central ⇒ (i)-central : The case of powers of letters being obvious, we
show by induction on |w| that if w = p01q with p, q and w (ii)-central, then
(q10, p01) is a standard pair. We can assume |p| ≤ |q| without loss of generality.
If |p| = |q| − 1, then p0 = q = 0p = 0|q| and (0|q|10, 0|q|1) is a standard pair.
If |p| ≤ |q| − 2, then q = p01u for some palindrome u. Since q is (ii)-central,
it is (iii)-central and from the preceeding proof we know that u is (iii)-central,
and so u is (ii)-central. By the induction hypothesis, (u10, p01) is a standard
pair, and so is (p01u10, p01) = (q10, p01). Since (q10, p01) is a standard pair,
(p01q10, p01) is also and w = (p01q10)
−− is (i)-central.
(i)-central ⇒ (iii)-central : Let w = u−− with (u, v) a standard pair. Write
u = w01 = yx for a standard pair (x, y), x = q10 and y = p01, with p and q
palindromes. Then w = p01q and w is (iii)-central.
(i)-central ⇒ (iv)-central : We know that a (i)-central word is a palindrome.
Let Γ : (u, v) ∈ (A
∗)
2 ↦→ (u, uv) ∈ (A
∗)
2 and ∆ : (u, v) ∈ (A
∗)
2 ↦→ (vu, v) ∈
(A
∗)
2. Let w = u−− with (u, v) = Γak ◦ ∆
ak−1 ◦ · · · ◦ ∆
a2 ◦ Γa1−1(0, 1), with
ai ∈ N∗ for i = 1 . . . k. Then w = s−−
k for any caracteristic word having slope
whose partial quotients begins with a1, a2, . . . , ak, with the sequence (sn) deﬁned
as in theorem 4, so that w is (iv)-central. The case where w = v−− with (u, v)
standard is similar.
(iv)-central ⇒ (iii)-central : In view of the preceeding proof, any (iv)-central
word is a preﬁx of a (i)-central word, and so a preﬁx of a (iii)-central word.
Let w be a palindrome preﬁx of a palindrome p01q with p and q palindromes.
We may assume |p| ≤ |q| and by induction on |p01q| we may assume |w| > |q|
since otherwise w is a preﬁx of the (iii)-central word q. If |w| = |q| + 1 then
w = q1 = 1q and w is a power of a letter. If |w| ≥ |q| + 2 then write w = q10t,
and since w is a preﬁx of q10p, t is a preﬁx of p, and so is also a preﬁx of q. The
word t is a suﬃx and a preﬁx of the palindromic word w, and so is palindromic,
and w = q10t with q and t palindromes, as required.
Unicity of decomposition : Let w = p01q = s01t = u−− be a central word,
with p, q, s and t palindrome and u10 standard, and assume that |s| > |p|. We

10

cannot have |s| = |p| + 1, so write s = p01λ and see that q = λ01t so that
u = w10 = q10p10 = λ01t10p10 = t10s10 = t10p01λ10, and the two words
λ01 and t10p10 commute. The primitive word u is a product of two non-empty
commuting words, hence a contradiction.

2 Repetition function and Rauzy graphs of Stur-
mian words

We recall the following notations. The dynamical map T is the shift, which
removes the ﬁrst letter of an inﬁnite word. For any word x and integer n ≥ 1,
we note Pn(x) the preﬁx of length n of x.

2.1 Deﬁnitions

In [8] a new complexity function is introduced, also called the repetition func-
tion. We deﬁne here a similar function and still call it the repetition function,
since the two are linked by a simple formula. Namely, if r0(x, n) is Bugeaud
and Kim’s repetition function, then we have r0(x, n) = n + r(x, n).

Deﬁnition 9 (Repetition function). Let x be an inﬁnite word over a ﬁnite
alphabet A. We deﬁne, for an integer m > 0 :

r(x, m) = max{k ∈ N | Pm(x), Pm(T (x)), . . . , Pm(T k−1(x)) are all distincts }.

The function r(x, ·) is called the repetition function of x.

Proposition 5. Let x be an inﬁnite word.

• ∀m > 0, r(x, m) ≤ p(x, m).

• if x is Sturmian we have ∀m > 0, r(x, m) ≤ m + 1

Deﬁnition 10 (Rauzy graph). Let x be an inﬁnite word over an alphabet A.
For every integer m > 0, we deﬁne the factor graph, or Rauzy graph, of x of
degree m as the directed graph having :

• vertexes as the factors of x of length m

• an arrow s → t if and only if there exists a factor r of x of length m + 1
such that s is a preﬁx of r and t a suﬃx of r.

Given a path s1 → s2 → . . . → sk in this graph, we set k − 1 to be its length.
The path deﬁned by x in Gm is the inﬁnite path

Pm(x) → Pm(T (x)) → . . . → Pm(T k(x)) → . . ..

11

For a Sturmian word x and m > 0, Gm has m + 1 vertexes. The vertex Lm
has in-degree 2 and the vertex Rm has out-degree 2 (notice that they may be
equal). Every vertex that is neither Lm nor Rm has in-degree 1 and out-degree
1. Therefore, Gm is the fusion of two cycles, sharing a common path. The
following proposition explains how to read the repetition function on the factor
graph of x. A Hamiltonian path in a directed graph is a path that does not
visit a vertex more that twice.

Proposition 6. Let x be a Sturmian word, m > 0 and Gm its Rauzy graph of
degree m. Then r(x, m) is the length of the longest Hamiltonian ﬁnite path

Pm(x) → Pm(T (x)) → . . . → Pm(T k−1(x)).

in the inﬁnite path deﬁned by x.

2.2 Repetition function of caracteristic words

Theorem 5. Let x be a Sturmian word and m ≥ 2. The following statements
are equivalents :

i) r(x, m) = m + 1

ii) r(x, m) ̸= r(x, m − 1)

Proof. The implication (i) ⇒ (i) is clear since r(x, m−1) ≤ m. For the converse,
let Am and Bm be the two distinct vertexes of Gm such that

Rm → Am and Rm → Bm.

Consider the path

Pm−1(x) → Pm−1(T (x)) → . . . → Pm−1(T r(x,m−1)(x)).

in Gm−1. There exists a unique integer 0 ≤ j < r(x, m−1) such that Pm−1(T r(x,m−1)(x)) =
Pm−1(T j(x)). In Gm, we cannot have Pm(T r(x,m−1)(x)) = Pm(T j(x)) because
this would imply r(x, m) = r(x, m − 1), which by assumption is not the case.
We then have Pm(T r(x,m−1)(x)) ̸= Pm(T j(x)) and these two words diﬀer only
by their last letters. This shows that

{Am, Bm} = {Pm(T r(x,m−1)(x)), Pm(T j(x))}

so that the path

Pm(x) → Pm(T (x)) → . . . → Pm(T r(x,m)−1(x)).

passes on the two vertexes Am and Bm. This path is the longest Hamiltonian
path that starts at Pm(x) in the path deﬁned by x, so we can see that it must
pass by all the m + 1 vertexes of Gm. This shows that r(x, m) = m + 1.

Lemma 2. Let cα be a caracteristic Sturmian word. Then we have

Pm(T r(cα,m)(cα)) = Pm(cα) = Lm

12

for all m > 0.

Proof. The second equality comes from the deﬁnition of cα. Let 0 ≤ j <
r(cα, m) be the only integer such that Pm(T r(cα,m)(cα)) = Pm(T j(cα)) and
assume j ̸= 0. Then Pm(T r(cα,m)−1(x)) ̸= Pm(T j−1(cα)) and these two words
diﬀer only by their ﬁrst letters. This shows that Pm(T j(cα)) is left special, so
that j = 0 and this is a contradiction.

We deﬁne r(z, m) for a ﬁnite word z and m > 0, provided z admits a factor
of length m that occurs at least twice, as r(x, m) for any inﬁnite word x such
that z is a preﬁx of x.

Lemma 3. Let z = p01q be a central word with |p| ≤ |q|. Then

r(z, |p| + 1) = |p| + 2.

Proof. Let cα be a caracteristic word having z as a preﬁx. Then by the pre-
ceeding lemma we have P|p|+1(T r(z,|p|+1)(cα)) = p0
We prove the result by induction on |z|. Since |z| is palindromic we cannot
have |p| = |q| and if |p| = |q| − 1 then q = p0 = 0p so z = 0|p|+110|p|+1 and the
result is clear. Assume that |p| ≤ |q| − 2 and write q = p01u, u is palindromic
since z = q10p = p01u10p is palindromic so that q = p01u is the decomposition
of q as a central word.
If |p| ≤ |u| then we are done by induction. Assume that |u| ≤ |p| so that
r(z, |u| + 1) = r(q, |u| + 1) = |u| + 2 by induction. Since r(z, |u| + 1) ≤ r(z, |p|) ≤
|u| + 2 we have r(z, |p|) = |u| + 2. But z = u10p10p so that u10p0 is not a preﬁx
of z and we must have r(z, |p| + 1) > r(z, |u| + 1) = |u| + 2 = r(z, |p|), and hence
(z, |p| + 1) ̸= r(z, |p|). By theorem 5, we have r(z, |p| + 1) = |p| + 2.

Corollary 1. Let cα be the caracteristic Sturmian word of slope α, and let (qn)
be the sequence of continuant of α. Then for all n ≥ 0 we have

r(cα) = qn for all qn − 1 ≤ m ≤ qn+1 − 2. (m ̸= 0)

Proof. Let (sn) be the sequence associated to α deﬁned as in theorem 4, so that
cα = lim sn. It is easily checked that |sn| = qn for n ≥ 0. We have

cα = lim sn+2 = lim sn+1sn = lim sn+1s−−
n = lim s−−
n tns−−
n+1

where tn = 10 if n ≥ 2 is even and tn = 01 if n ≥ 2 is odd. The words s−−
n tns−−
n+1
are the central preﬁxes of cα and we have r(cα, |s−−
n | + 1) = |s−−
n | + 2 = |sn|
and since r(cα, |s−−
n+1|) ≤ |sn|, we have

r(cα, m) = |sn| = qn

for n ≥ 2 and qn − 1 ≤ m ≤ qn+1 − 2.
If a1 ≥ 3, then it is easily checked that the formula still holds for 1 ≤ m ≤
q2 − 2. If a1 = 2, or a1 = 1 and a2 ≥ 2, then the formulas hold but the set
of integer m such that 1 ≤ m ≤ q1 − 2 is empty. If a1 = 1 and a2 = 2 then
the formulas hold, but the sets of integers m such that 1 ≤ m ≤ q1 − 2 or
q1 − 1 ≤ m ≤ q2 − 2 are empty.
 13

2.3 Rauzy graph of Sturmian words

Let x be a Sturmian word of slope α whose sequence of continuant is (qn).

Notations :

• In the remaining part of the article, we make the abuse of notation of
noting [a, b] the integer interval of integers m such that a ≤ m ≤ b.

• We deﬁne the integer intervals In, for n ≥ 0,

In = [qn − 1, qn+1 − 2]

I 0
n = [qn − 1, qn + qn−1 − 2]

and for 1 ≤ l ≤ an+1 − 1,

I l
n = [lqn + qn−1 − 1, (l + 1)qn + qn−1 − 2].

If a1 = 1 or a1 = 2 then I0 is empty. If a1 = 1 and a2 = 1, then both I0
and I1 are empty.

• An Eulerian path in a directed graph is a path that does not pass twice
on the same arrow. A cycle in a directed graph is an Eulerian path s1 →
s2 → . . . → sk such that s1 = sk and we set k to be its length.

We recall the notation u∗ for a ﬁnite word u, denoting the suﬃx of length
|u| − 1 of u, which is u deprived of its ﬁrst letter.

Proposition 7. Let m ∈ I l
n for n ≥ 0 and 1 ≤ l ≤ an+1 − 1, then :

1. one of the two cycles of Gm is of length qn. It is called the referent cycle.

2. the other cycle is of length lqn + qn−1.

3. The arrow Rm → R∗
mt−
n−1 belongs to the referent cycle, and the arrow
Rm → R∗
mt−
n belongs to the non-referent cycle. These two arrows do not
belong to the same cycle.

Proof. 1) Since two inﬁnite words sharing the same set of factors also share the
same Rauzy graphs, we can reduce to the case x = cα. Since r(cα, m) = qn by
Corollary 2, by deﬁnition of the repetition function the path

Pm(cα) → Pm(T (cα)) → . . . → Pm(T r(cα,m)(cα))

deﬁnes a cycle of length qn.
2) The common part of the two cycles is the shortest path that starts at the
vertex Lm and ends at the vertex Rm. The ﬁnite word w deﬁned by this path
is left and right special, so it is the shortest central word of length |w| ≥ m, and
this length is equal to (l + 1)qn + qn−1 − 2 and has (l + 1)qn + qn−1 − 1 vertexes.
The path so deﬁned is of length (l + 1)qn + qn−1 − 2 − m. Since the sum of the
length of the two cycles equals the sum of the number of vertexes of Gm and
the number of vertexes in the common part, we get that the other cycle is of
length µ where
 14

qn + µ = m + 1 + (l + 1)qn + qn−1 − 1 − m

so that µ = lqn + qn−1.
Since qn and lqn + qn−1 are coprime, the referent cycle is well-determined
by its length.
3) The common path Lm → . . . → Rm corresponds to the central word of
length (l + 1)qn + qn−1 − 2, namely sl+1
n s−−
n−1. The referent cycle is the cycle

Pm(cα) → Pm(T (cα)) → . . . → Pm(T r(cα,m)(cα))

so we only have to see that sl+1
n s−
n−1 is a preﬁx of cα since sn−1 ends with
tn−1. But this is obvious, sn−1 is a preﬁx of sn, and sn+1 = san+1
n sn−1, so
that indeed the arrow Rm → R∗
mt−
n−1 belongs to the referent cycle. The fact
that Rm → R∗
mt−
n belongs to the non-referent cycle comes from the fact that
sl+1
n s−−
n−1tn is not a preﬁx of cα. It is obvious that the two arrows leaving the
right special factor Rm cannot be on the same cycle.

Deﬁnition 11. • We say x turns around a cycle of length k in Gm when
r(x, m) = k and the path Pm(x) → Pm(T (x)) → . . . → Pm(T k(x)) shares
the same arrow as this cycle.

• We say x turns d times around a cycle of length k if for all i = 0 . . . d − 1,
T ik(x) turns around this cycle.

For a Sturmian word x, since the two cycles of its Rauzy graph Gm have
diﬀerent length, x turns around a cycle of length k if and only if r(x, m) = k.

Theorem 6. For m ∈ I l
n, the caracteristic word cα turns around the referent
cycle an+1 − l times, and no more.

Proof. We ﬁrst consider the case where l = 0. Then the central word s−−
n is a
strict preﬁx of Lm and Lm is a strict preﬁx of the central word s−−
n tns−−
n−1. The
word z = sn+1s−−
n = san+1+1
n s−−
n−1 is central and so we have

r(z, m) = qn = r(T qn (z), m) = . . . = r(T (an+1−1)qn (cα), m),

showing that cα turns at least an+1 times around the referent cycle.
Since sn+1sn is a preﬁx of cα, sn+1sn = ztn = san+1+1
n s−−
n−1tn is a preﬁx of
cα and sns−−
n−1tn is a preﬁx of T an+1qn (cα) and from this we easily see that the
word T an+1qn (cα) passes by the arrow Rm → R∗
mt−
n before passing by the arrow
Rm → R∗
mt−
n−1. This shows that cα does not turn an+1 + 1 times around the
referent cycle.
The case l > 0 is similar.

Lemma 4. Let x be a Sturmian word of slope α, and let m > 0. Then x does
not turn twice around the non-referent cycle.

15

Proof. Since the set of factors of a Sturmian word is stable under reversal, we
see that if s → t is an arrow of Gm, then ˜t → ˜s is an arrow of Gm. Since the
two cycles of Gm are of diﬀerent length, we can derive from the fact that only
one of the two arrows
Rm → R∗
mt−
n−1 and Rm → R∗
mt−
n

belongs to the referent cycle the fact that only one of the two arrows

0L−
m → Lm and 1L−
m → Lm

belongs to the referent cycle. The two words 0cα and 1cα are Sturmian, and so
there is a unique word u of length qn such that ucα is Sturmian and turns around
the referent cycle. Since cα always turns at least once around the referent cycle,
ucα turns twice around the referent cycle.
If there is a Sturmian word x that turns twice around the non-referent cycle,
wee see from the preceeding argument that the central word w deﬁned by the
common part of Gm is such that the four word 0w0, 1w0, 0w1 and 1w1 are
factors of x. But this contradicts the balanced property of Sturmian words.

3 Formal Intercepts of Sturmian words

We still consider a slope α with continuants (qn).

Proposition 8. Let N =
 k−1∑

i=0 bi+1qi with bi ≥ 0 for all i ≥ 2 and n ≥ 1. Then

the following statements are equivalent :

i) ∀l = 1 . . . k,
 l−1∑

i=0 bi+1qi < ql

ii) We have :

• 0 ≤ b1 ≤ a1 − 1

• ∀i ≥ 1, 0 ≤ bi ≤ ai
• ∀i ≥ 1, bi+1 = ai+1 ⇒ bi = 0

Proof. i) ⇒ ii) : Since q1 = a1, the ﬁrst line of ii) is easily checked. Let j ≥ 1,

then if bj > aj we have bjqj−1 ∑j−1
i=0 bi+1qi < qj = ajqj−1 + qj−2 ≤ (aj + 1)qj−1
which is absurd. If bj+1 = aj+1 then from ∑j
i=0 bi+1qi < qj+1 = aj+1qj + qj−1
we get ∑j−1
i=0 bi+1qi < qj−1 which clearly implies bj = 0.
ii) ⇒ i) : The result is clear for l = 1 and we prove the result by induction

on l. Assume ∑l−1
i=0 bi+1qi < ql. If bl+1 < al+1 then ∑l
i=0 bi+1qi < ql + bl+1ql ≤
al+1ql < ql+1. If bl+1 = al+1 then by assumption bl = 0 so that ∑l−1
i=0 bi+1qi <
ql−1 and ∑l
i=0 bi+1qi < ql−1 + al+1ql = ql+1.

16

For a sequence (bi)i≥1, we call the conditions of Proposition 8 as the Os-
trowski conditions.

Proposition 9. Every integer N ∈ [0, qn[ can be written uniquely in the form

N =
 n−1∑

i=0 bi+1qi

where the integers (bi) satisfy the Ostrowski conditions.

Proof. We proceed by induction on N . Write N = bnqn−1 + c with c ∈ [0, qn−1[.
By induction, c can be written uniquely in the form c = ∑n−2
i=0 bi+1qi where the
coeﬃcient (bi)
n−1
i=1 satisfy the Ostrowski conditions. It is obvious that bn ≤ an.
If bn = an, then we must have c < qn−2 and by induction on the unicity we
must have bn−1 = 0 so that the sequence (bi) indeed satisfy the Ostrowski
conditions.

Deﬁnition 12. We deﬁne the set :

Iα =
 {
 (kn)n>0 ∈ ∏

n>0
[0, qn[
 ∣
∣
∣
∣
∣ ∀n ≥ 0, kn = kn+1[mod qn]
}

of formal intercepts of the slope α.

Remark 1. In view of proposition 8 and 9, if ρ = (ρn)n≥0 is a formal intercept,
there is a unique sequence of integers (bi)i≥1, satisfying the Ostrowski conditions,
such that
 ρn =
 n−1∑

i=0 bi+1qi

for all n ≥ 0. In this case, we directly write :

ρ =
 +∞∑

i=0 bi+1qi.

Remark 2. For n > 0, we deﬁne :

Ψn+1
n : [0, qn+1[ ↦−→ [0, qn[
k ↦−→ k [mod qn]

and for integers m ≥ n > 0 :

Ψm
n = Ψn+1
n ◦ Ψn+2
n+1 ◦ · · · ◦ Ψm
m−1 : [0, qm[ → [0, qn[

then
 Iα = lim
←−[0, qn[=
 {
 (kn)n>0 ∈ ∏

n>0
[0, qn[
 ∣
∣
∣
∣
∣ n ≤ m ⇒ Ψm
n (km) = kn
}

17

may be viewed as the projective limit of the sets [0, qn[ endowed with the functions
Ψm
n .

Proposition 10. Let ρ = ∑
i≥0 bi+1qi be a formal intercept of the slope α, and
n ≥ 1. Let λn = qn+1 + qn − ρn+1 − 2, then

1. The words T ρn (cα) and T ρn+1(cα) share the same preﬁx of length λn.

2. If bn+1 ̸= 0, then λn is the length of the longest common preﬁx of T ρn(cα)
and T ρn+1(cα),

3. the increasing sequence (λn)n≥1 is unbounded.

Proof. 1) Let m = qn − 1 ∈ I 0
n. By theorem 6, the word T bn+1qn (cα) turns
an+1 − bn+1 times around the referent cycle, and then turns around the non-
referent cycle. This shows that the words

T bn+1qn (cα) and cα

share the same preﬁx of length

m + (an+1 − bn+1)qn + r

where r is the length of the common part of the two cycles of Gm. Since
m = qn − 1, every vertex of the non-referent cycle belongs to the referent cycle.
This implies that r = qn−1 − 1, and the two words T bn+1qn (cα) and cα share the
same preﬁx of length m+(an+1−bn+1)qn+r = qn−1+(an+1−bn+1)qn+qn−1−1.
This shows that the two words

T ρn (T bn+1qn (cα)) = T ρn+1(cα) and T ρn (cα)

share the same preﬁx of length qn + (an+1 − bn+1)qn + qn−1 − 2 − ρn = qn+1 +
qn − ρn+1 − 2 = λn.
2) If bn+1 ̸= 0 then the longest common preﬁx of the words T bn+1qn (cα) and
cα has length qn − 1 + (an+1 − bn+1)qn + qn−1 − 1. So that the length of the
longest common preﬁx of T ρn+1(cα) and T ρn (cα) indeed equals λn.
3) We have λn+1 − λn = qn+2 + qn+1 − qn+1 − qn − (ρn+2 − ρn+1) = (an+2 −
bn+2)qn+1 ≥ 0 so that the sequence (λn) is increasing. Since ρn+1 < qn+1, we
get :
 λn ≥ qn − 1

and this shows that λn → +∞ when n → +∞.

Remark 3. Notice that in the case where ρn+1 = qn+1 − 1 then λn = qn − 1
and the lower bound for (λn) found in the proof of 3) is optimal. However, the
sequence (qn − 1)n≥1 does not deﬁnes a formal intercept.

Deﬁnition 13. Let ρ be a formal intercept of the slope α. We deﬁne the Stur-
mian word T ρ(cα) of slope α and formal intercept ρ as the word

T ρ(cα) = lim T ρn (cα)

18

having the same preﬁx of length qn − 1 as T ρn (cα) for all n ≥ 1.

Proposition 11. Let ρ be a formal intercept of the slope α ans n ≥ 1. Then
the length of the longest common preﬁx of the words

T ρ(cα) and T ρn(cα)

equals λN , where N is the smallest integer N ≥ n such that bN +1 ̸= 0. If no
such N exists, then they are equal.

Proof. This is clear, since ρn = ρk for all n ≤ k ≤ N if such a N exists, and
ρn = ρk for all n ≤ k in the second case.

Proposition 12. Let x be a Sturmian word of slope α. Then there exist a
unique formal intercept ρ of the slope α such that x = T ρ(cα).

Proof. We consider the sequence, deﬁned for n ≥ 0 as :

ρn = min{k ≥ 0 | x and T k(cα) share the same preﬁx of length qn − 1}

and show that ρ = (ρn)n≥1 is a formal intercept. Let n ≥ 1 and m = qn −1 ∈ I 0
n.
Since the referent cycle is of length qn = m + 1, every vertex of Gm is in the
referent cycle. This shows that 0 ≤ ρn < qn. Since T ρn+1(cα), T ρn (cα) and x
share the same preﬁx of length qn − 1, the paths they deﬁne start at the same
vertex.
Write ρn+1 = bqn + c with c < qn. Since ρn+1 = bqn + c < qn+1 = an+1qn +
qn−1, we have b ≤ an+1 and if b = an+1 then c < qn−1. Since the caracteristic
word cα turns an+1 times around the referent cycle, if b < an+1 then T ρn+1(cα)
and T c(cα) start at the same vertex, and hence share the same preﬁx of length
qn − 1. Since the referent cycle is of length qn, and that ρn < qn we must have
c = ρn. In the case where b = an+1, then c < qn−1 so that T ρn+1(cα) starts in
the common part of the two cycles of Gm, T ρn+1(cα) and T c(cα) start at the
same vertex, which is on the referent cycle, and we again must have ρn = c.
Thus ρn = ρn+1 [mod qn] and we are done.
For unicity, notice that since for m = qn − 1 the referent cycle is of length
qn, there must be only one k < qn such that T k(cα) and T ρ(cα) share the same
preﬁx of length qn − 1, and since ρn is such a k, every formal intercept γ such
that x = T γ(cα) must satisfy γn = ρn.

Example : One can compute easily that the inﬁnite words 0cα and 1cα have
respective formal intercepts ∑i≥0 a2i+2q2i+1 and (a1 − 1) + ∑i≥1 a2i+1q2i.
Remark : In a future paper we will investigate more properties of formal
intercepts.

References

[1] M. Lothaire, Algebraic Combinatorics on words, (2000) ISBN :
9781107326019
 19

[2] J.-P. Allouche, J. O. Shallit, Automatic Sequences : Theory, Appli-
cations, Generalizations, (2002) ISBN : 9780521823326

[3] D. E. Knuth, Fibonacci multiplication, Appl. Math. Lett., 1 (1988), pp.
57-60

[4] P. Arnoux, Some remarks about Fibonacci multiplication, Appl. Math.
Lett., 2 (1989), pp. 319-320

[5] V. Berthé, Autour du système d’énumération d’Ostrowski, Bull. Belg.
Math. Soc. 8 (2001), pp. 209-238

[6] V. Berthé, Fréquences des facteurs des suites sturmiennes, Theoretical
Computer Science, Volume 165, Issue 2, 1996, pp. 295-309, ISSN 0304-
3975, https://doi.org/10.1016/0304-3975(95)00224-3.

[7] V. Berthé, C Holton, Luca Q. Zamboni, Initial powers of Stur-
mian sequences, Acta Arithmetica, Instytut Matematyczny PAN, 2006, 122,
pp.315-347. lirmm-00123046

[8] Y. Bugeaud, D. H. Kim, A new complexity function, repetitions in stur-
mian words, arXiv:1510.00279 [math.NT]

[9] M. Mayero, The Three Gap Theorem, arXiv:cs/0609124 [cs.LO]

[10] A. Siegel, Théoréme des trois longueurs et suites sturmiennes : mots
d’agencement des longueurs, ACTA ARITHMETICA XCVII.3 (2001)

[11] L. Ramshaw, On the discrepancy of the sequence formed by the multi-
ples of an irrational number, Journal of Number Theory, Volume 13, Is-
sue 2, 1981, pp. 138-175, ISSN 0022-314X, https://doi.org/10.1016/0022-
314X(81)90002-0.
 20
