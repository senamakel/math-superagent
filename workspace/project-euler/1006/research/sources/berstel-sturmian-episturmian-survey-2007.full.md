<!-- source: https://ligm.univ-eiffel.fr/~berstel/Articles/2007SturmianThessalonique.pdf | converted from PDF -->

Sturmian and Episturmian Words

(A Survey of Some Recent Results)

Jean Berstel

Institut Gaspard Monge, Universit´e Paris-Est, Marne-la-Vall´ee, France

Abstract. This survey paper contains a description of some recent re-
sults concerning Sturmian and episturmian words, with particular em-
phasis on central words. We list fourteen characterizations of central
words. We give the characterizations of Sturmian and episturmian words
by lexicographic ordering, we show how the Burrows-Wheeler transform
behaves on Sturmian words. We mention results on balanced episturmian
words. We give a description of the compact suﬃx automaton of central
Sturmian words.

1 Introduction

Sturmian words are combinatorial objects that are quite remarkable by the num-
ber of diﬀerent characterizations they have, formulated in terms coming from
diﬀerent mathematical frameworks.
Sturmian words have a geometric description as digitized straight lines. Com-
puter representation of lines has been an active subject of research, although
early theory of Sturmian words remained unnoticed in the patter recognition
community. The paper by [1] is a review of recognition of straight lines with
respect to interaction with other disciplines. The natural generalization would
be here to digitized planes, and as counter part to Sturmian bisequences.
Sturmian words have an arithmetic description, as rotations on the torus, a
combinatorial description, as aperiodic words that are balanced, a description
from the point of view of dynamical systems, as aperiodic words of minimal factor
(subword) complexity, and so on. Many of these descriptions are known since
the years 1940 and the fundamental paper [2], and a new widely disseminated
research on these words has been started about thirty years ago.
In all these cases, the description given is a characterization, that is the con-
dition stated fully describes the set of Sturmian words. Other, less known char-
acterizations of this kind have been given. For instance, Sturmian words are
characterized by the number of their return words, or by their palindromic com-
plexity, that is the number of palindromic factors they have.
Theoretical computer scientists have contributed the point of view of eﬀective
computation. These have been studied and developed for the class of charac-
teristic Sturmian words, where amazing computational descriptions have been
provided. The special class of characteristic Sturmian words has itself some char-
acterizations of several kinds.

S. Bozapalidis and G. Rahonis (Eds.): CAI 2007, LNCS 4728, pp. 23–47, 2007.
c⃝ Springer-Verlag Berlin Heidelberg 2007

24 J. Berstel

The richness of the theory of Sturmian words, as the meeting point of tools
from diﬀerent mathematical descriptions, and as extremal point of various fam-
ilies of inﬁnite words, has of course led to tentatives of generalizations to other
situations, especially with the objective to capture the essence of what makes
the Sturmian words so special.
One of the limitation of Sturmian words is that they are over a binary alpha-
bet. Among the extensions to larger alphabet, the so called episturmian words
have appeared to be best suited family by the number of properties of Sturmian
words they share.
Another extension is to two dimensions, that is to what are discretized or dig-
ital planes. This is quite interesting from the applications to pattern recognition,
and is an ongoing research topic.
Another generalization is to trees. This is just at its beginnings (see [3]).
Another extension is obtained when the reversal operator is replaced by an
arbitrary involutory automorphism of the free monoid, see [4].

2 Sturmian and Episturmian Words

Before starting, we give some notational conventions. Given a nonempty word
w,we denote by w− the word without its last letter. If w has at least two letters,
then we write w= instead of w−−. Thus, for instance abaab= = aba.
Given a ﬁnite or inﬁnite word w, the set of letters that occur in w is denoted
by Alph(w). If w is inﬁnite, Ult(w) denotes the set of letters that occur inﬁnitely
many often in w.
Finally, we denote by w(k) the letter at position k (k ≥ 0) in the word w.

2.1 Complexity

Let w be an inﬁnite word on some alphabet A.Wedenoteby F (w)the set of
(ﬁnite) factors of w,and by Fn(w)= F (w) ∩ A
n the set of factors of length n of
w.The complexity function cw of w is deﬁned by

cw(n)= Card(Fn(w))

This complexity is also called subword or factor or block complexity.The (right)
degree degw(x) of a ﬁnite word x in w is the number of letters a such that xa is
afactorof w: degw(x)=Card{a ∈ A | xa ∈ F (w)}

Similarly, the left degree of w is the number of a ∈ A with ax ∈ F (w). Clearly,
degw(x) ≥ 1 for each factor x of w.Also, degw(xy) ≤ degw(y) for all x, y. Clearly

cw(n +1) = ∑

x∈Fn(w)
deg(x) .

Afactor x is right special (left special) if its degree (left degree) is strictly greater
than 1. Any suﬃx of a right special factor is again right special. Observe that

Sturmian and Episturmian Words 25

cw(n +1) − cw(n)= ∑

x∈Sn(w)
deg(x) − 1 . (1)

where Sn(w) is the set of right special factors of length n. An inﬁnite word w is
episturmian if the set F (w) is closed under reversal, and if, for every n ≥ 1there
exists at most one right special factor of length n.Itis aperiodic episturmian if it
is episturmian and aperiodic, that is not eventually periodic. This is equivalent
to require that there is exactly one right special factor of each length. The word
w is strict episturmian if w is aperiodic episturmian and if all its right special
factors have the same degree. If this degree is k, then it follows from (1) that for
n ≥ 1 cw(n)= kn +1 .

Below, we will give a more detailed description the Tribonacci word which is a
strict episturmian word. The theory of episturmian words and morphisms has
been developed in three basic papers [5,6,7] by Justin and Pirillo, the ﬁrst with
Droubay, see also [8].
Recall that an inﬁnite word w is recurrent if each factor of w occurs inﬁnitely
many often in w, and it is uniformly recurrent if each factor occurs inﬁnitely
many often with bounded gaps between consecutive occurrences. In other terms,
w is uniformly recurrent if, for every n,there exists N such that each factor of
w of length N contains all factors of w of length n,in symbols Fn(w)= Fn(u)
for all u ∈ FN (w). Any episturmian word is uniformly recurrent.
Strict episturmian words are also called Arnoux-Rauzy words or AR-words.
They were introduced and studied in [9], mainly in the case of three letters.
Strict episturmian words over two letters are exactly the Sturmian words. These
are aperiodic words of minimal block complexity in view of the well-known.

Theorem 1. [2,10] An inﬁnite word w is eventually periodic if and only if there
exists an integer n ≥ 1 such that cw(n) ≤ n.

2.2 Other Complexity Functions

Several other measures of complexity of inﬁnite words have been deﬁned and
compared to the block complexity.
The palindrome complexity function pw of an inﬁnite word w associates to
each integer n ≥ 0 the number of distinct palindromes of length n in w.
A general exposition of palindrome complexity together with new results is
given in [11]. In particular, it is shown in this paper that if w is an aperiodic
inﬁnite word, then
 pw(n) < 16
n cw(n + ⌊ n
4
 ⌋) .

Thus in particular if cw(n)= O(n)then w has bounded palindromic complex-
ity. This holds for Sturmian and episturmian words, for automatic words, and
for words that are ﬁxed points of primitive morphisms. For uniformly recurrent

26 J. Berstel

words, there is a more precise formula given in [12]. They prove that, provided
the set of factors F (w) is closed under reversal,

pw(n)+ pw(n +1) ≤ 2+ cw(n +1) − cw(n) .

This is sharp for Sturmian words: these are characterized by the fact that
pw(n)= 1 if n is even and pw(n)= 2 if n is odd [13], and also for AR-words over
r> 2 letters: these words have palindrome complexity pw(n)=1 if n is even
and pw(n)= r if n is odd [14].
Another complexity function is arithmetical complexity introduced in [15].
Given an inﬁnite word w = w(0)w(1) ··· ,the arithmetical complexity function
aw associates to n ≥ 0 the number of distinct words of the

w(k)w(k + d)w(k +2d) ··· w(k +(n − 1)d)

for k ≥ 0, d ≥ 1. The arithmetical complexity of a Sturmian word depends only
on its slope (see below), since two Sturmian words have the same set of factors
if and only if they have same slope. So, it is convenient to write aα instead of
aw for a Sturmian word of slope α.

Theorem 2. [16] For any Sturmian word of slope α, one has

aα(n) ≤ h(n)

where
 h(n)= 2 + (
n +1
3
 ) +2
 n−1∑

i=1 (n − i)φ(i) .

Here φ is Euler’s totient function. In fact, the authors give the exact expression
for the arithmetical complexity of Sturmian words for 1/3 <α < 1/2(note
that exchanging the two letters in a Sturmian words replaces the slope α by
1 − α without changing the complexity, so the result holds also for 1/2 <α <
2/3). Denote by (rk) the decreasing sequence of rational numbers given by rk =
k/(3k − 1), for k ≥ 2. Thus r2 =2/3, r3 =3/8.

Theorem 3. [16] For any irrational α with 1/3 <α < 1/2, one has

aα(n)=
 {h(n) − 8 if n is odd
h(n) − 9 otherwise

for n ≥ 3k,where k is such that rk−1 >α >rk.

For other results concerning arithmetical complexity, see [17].
A more general measure is the maximal pattern complexity. A window τ of
size k is a sequence 0 = τ0 <τ1 < ··· <τk−1 of integers. The τ -pattern at
position n in w is the word

w(n + τ0)w(n + τ1) ··· w(n + τk−1) .

Sturmian and Episturmian Words 27

Denote by Fτ (w)the set of τ -pattern occurring in w.The τ -complexity of w is
the number cw(τ )=Card Fτ (w), and the maximal pattern complexity is

c∗
w(k)= sup
|τ |=k cw(τ ) ,

where |τ | denotes the size of τ . There is an analogue of Theorem 1 for the
maximal pattern complexity:

Theorem 4. [18] An inﬁnite word w is eventually periodic if and only if c∗
w(k) <
2k for some k ≥ 1.

Words with maximal pattern complexity 2k have been called pattern Sturmian
words and are studied in [18]. Sturmian words are special cases of pattern Stur-
mian words. Generalizations are given in [19,20].
There is a variation of block complexity considered by [21,22]. Instead of
counting the number of factors of given length in an inﬁnite word, they count
the number of factors of this length that occur inﬁnitely many often in the word.
If the word is uniformly recurrent, the complexities are the same. For skew words,
as deﬁned later, they are diﬀerent.

2.3 Palindromic Closure

The right palindromic closure of a word w is the shortest palindrome which has
w as a preﬁx. It is denoted by w(+). For instance, the right palindromic closure
of 01011 is 0010110100. It is easy to prove that

w(+) = uv˜u,

where v is the longest palindrome suﬃx of w. In the example, the longest palin-
drome suﬃx of w = 001011 is 11, and therefore w(+) = 0010 11 0100. The notion
was introduced and used by de Luca [23,24] for the analysis of ﬁnite Sturmian
words.
Given a ﬁnite word d,the right iterated palindrome produced by d is the word
P (d) deﬁned as follows. P (ε)= ε and for a word d and a letter a,

P (da)= (P (d)a)
(+) . (2)

For example, for the word abbaab one gets successively

dP (d)
aa
ab aba
abb ababa
abba ababaababa
abbaa ababaababaababa
abbaab ababaababaabababaababaababa

28 J. Berstel

The word d is the directive word of P (d). A right iterated palindrome is a right
iterated palindrome w produced by some word d.If d is over at most two letters,
then the word w is binary.
If d is an inﬁnite word, the right iterated palindrome produced by d is the
inﬁnite word which has as preﬁxes all right iterated palindromes produced by
the ﬁnite preﬁxes of d. This makes sense because P (x)is a preﬁx of P (xy)for
all words x, y.
If a does not occur in d, then (2) gives simply P (da)= P (d)aP (d)˜. There is
another way to compute (2) when the letter a occurs in d.Let pa be the longest
preﬁx of d ending with the letter a, and deﬁne the word s by P (pa)= P (p)s.
Then P (da)= P (d)s. In our example, for db = abbaab, one has p = ab and
s = baababaababa. This computation rule is given in [25].

2.4 Justin’s Formula

Justin’s formula gives a useful relation between standard words and central words
generated by iterated right palindromic closure. Let A be an alphabet and let
ψ : A
∗ → End(A
∗) be the morphism that maps a letter a to the morphism ψa
deﬁned, for b ∈ A,by
 ψa(b)=
 {ab if b ̸= a ,

a otherwise.

For instance, if a, b, c are letters, then

ψa(bac)= abaac .

Composition is deﬁned for words u, v by

ψuv = ψu ◦ ψv ,

that is ψuv(w)= ψu(ψv(w)) .

For instance, ψabc(a)= ψab(ca)= ψa(bcba)= abacaba .

Aword of the form ψu(a)for some word u and some letter a is an epistan-
dard word. The morphisms ψu are pure epistandard morphisms. In the binary
case, these morphisms are called pure Sturmian morphisms, and the words they
produce are indeed the standard words. Justin’s formula establishes a relation
between the morphism ψ and right palindromic closure P .

Proposition 5. (Justin’s Formula) The following holds for any words u, v:

P (uv)= ψu(P (v))P (u) . (3)

As an example, let u = ab, v = ac.Then P (u)= aba, P (v)= aca, ψu(P (v)) =
ψa(ψb(aca)) = ψa(babcba)= abaabacaba,whereas P (abac)= ((abaa)
(+)c)
(+) =
abaabac
(+) = abaabacabaaba, so indeed P (abac)= ψab(aca)aba.

Sturmian and Episturmian Words 29

The formula admits several interesting special cases. First, when u is a letter,
then (3) becomes P (av)= ψa(P (v))a.

This shows that P (av) is obtained from P (v) by simply inserting the letter a
before each letter of P (v) which is not an a, and then adding a ﬁnal a.For
instance, since P (ba)= bab,one gets P (aba)= abaaba.Observe that P (av)is
also obtained from P (v) by inserting the letter a after each non-a letter.
Another special case arises when v is just a letter. Then (3) becomes

P (ua)= ψu(a)P (u) . (4)

This shows a way to compute the right palindrome closure P (ua)by preﬁxing
P (u) the standard word ψu(a). Recall that by deﬁnition P (ua)= P (u)a˜y,where
P (u)a = yz with z a maximal suﬃx of P (u)a which is a palindrome. Since P (u)
and P (ua) both are palindromes, one has P (ua)= yaP (u)and so ψu(a)= ya.
As an example, consider the computation of P (acbc). By (4), it suﬃces to
compute ψacb(c)= acabac and P (acb)= acabaca to get the word

P (acbc)= acabacacabaca .

Finally, iteration of (4) gives, for a word u = a1a2 ··· an the formula

P (a1a2 ··· an)= ψa1a2···an−1(an)ψa1a2···an−2(an−1) ··· ψa1a2 (a3)ψa1 (a2)a1 .

For instance
 P (acbc)= ψacb(c)ψac(b)ψa(c)a = acabac · acab · ac · a.

As an illustration of the uses of the formula, we prove the following observation.

Remark 6. A standard episturmian word w has the form ψu(v), where u is a
ﬁnite word and v is a strict standard episturmian word.

Proof. Let d be the inﬁnite word such that w = P (d). Let d
′ be a suﬃx of d such
that Ult(d
′) = Alph(d
′), and let d = ud
′. By Justin’s formula, w = ψu(P (d
′)),
and by construction P (d
′) is strict.

Another remark concerns eventually periodic standard episturmian words. If w
is such a word, then it is purely periodic. Indeed, by Theorem 3 in [5], one
has w = P (vaω)for some word v and some letter a, and consequently w =
ψv(P (aω)) = ψv(aω)= (ψv(a))
ω.

Example 7. The Tribonacci word is a generalization of the Fibonacci word. Fi-
nite Tribonacci words are the words tn deﬁned over three letters a, b, c by

t−1 = c, t0 = a, t1 = ab, tn = tn−1tn−2tn−3 (n ≥ 2) .

30 J. Berstel

Thus t2 = abac
t3 = abacaba
t4 = abacabaabacab
t5 = abacabaabacababacabaabac

The inﬁnite Tribonacci word t is the limit of the words tn. An equivalent deﬁni-
tion of the tn is through the morphism

ψ : a ↦→ ab, b ↦→ ac, c ↦→ a.

Indeed, it is easy to check that tn = ψn(a)for n ≥ 0. Finally, one has also

t = P ((abc)
ω)

showing that t is a strict standard episturmian word. Indeed, denote by δn the
preﬁx of length n of (abc)
ω and set un = P (δn). Then it can be shown that
un = tn−1un−1 for n ≥ 1. Thus t = lim un.Also

un = tn−1tn−2 ··· t0 .

This formula has been extended to more general words in [26]. For other proper-
ties of the Tribonacci word, see [27,28] and the chapter by Allouche and Berth´e
in [29].

3Sturmian Words

Sturmian words have particular properties related to their geometric interpreta-
tion. This holds especially for ﬁnite Sturmian words.

3.1 Mechanical Words

Sturmian words have a geometric interpretation as cutting sequences of straight
lines (this word comes from [30]) and therefore are closely related to digitization
and pattern recognition. An equivalent formulation is through mechanical words
(as they are called in [2]) or as rotation words (this is the name given for instance
in [31]).
Consider a straight line in the plane. At each intersection point with the
integer grid, write the letter a if the line intersects grid vertically, and write
the letter b otherwise, see Figure 1. This is the deﬁnition of Sturmian words as
cutting sequences. By a “shear”, that is the mapping (x, y) ↦→ (x + y, y), one
gets the deﬁnition as “mechanical words”. These are inﬁnite words deﬁned, for
reals 0 <α < 1and 0 ≤ ρ ≤ 1, by

sα,ρ(n)=
 {
a if ⌊(n +1)α + ρ⌋ = ⌊nα + ρ⌋,
b otherwise.

s′
α,ρ(n)=
 {
a if ⌈(n +1)α + ρ⌉ = ⌈nα + ρ⌉,
b otherwise.

Sturmian and Episturmian Words 31

ba ab a ba a b a ab ba

Fig. 1. A Sturmian word deﬁned as a cutting sequence by intersection or by adjacent
squares, and the upper and the lower mechanical word

for n ≥ 0. The word sα,ρ (s′
α,ρ) is called the lower (upper) mechanical word with
slope α and intercept ρ.
 ba aba b a a ba aba

Fig. 2. “Shear” of the cutting sequence

There is an equivalent deﬁnition by rotation. Consider indeed the torus T =
R/Z of reals modulo 1, and partition T

Ia =[0, 1 − α),Ib =[1 − α, 1),I ′
a =(0, 1 − α],I ′
b =(1 − α, 1] ,

and let Rα : T → T be the rotation of angle α.Then

sα,ρ(n)=
 {a if Rn
α(ρ) ∈ Ia,
b otherwise. ,s′
α,ρ(n)=
 {a if Rn
α(ρ) ∈ I ′
a,
b otherwise.

This is why mechanical words are also called rotation words. They are rational
words when α is rational, and irrational words when α is irrational. It is known
[2] that irrational mechanical words are exactly Sturmian words. It is also known
that two Sturmian words with the same slope have the same set of factors. When
ρ = α, one has sα,ρ = s′
α,ρ. This word is called the characteristic word of slope
α, and is denoted by cα. For a systematic exposition, see [32] and [33].

4 Finite Sturmian Words

In this section, all words are binary over the alphabet A = {a, b}.
A ﬁnite word is Sturmian if it is a factor of some inﬁnite Sturmian word.
Among ﬁnite Sturmian words, particular classes are the standard words, the
central words, and the Christoﬀel words.

32 J. Berstel

  
    
   
    
   

Fig. 3. The central word corresponding to the point (8, 5) is x = abaababaaba.The
upper and lower Christoﬀel words are bxa = babaababaabaa and axb = aabaababaabab.
Two standard words are associated with them, namely xab = abaababaabaab and
xba = abaababaababa.

The mechanical words sα,ρ and s′
α,ρ are purely periodic when α is rational.
Moreover, if α = p/(p + q)for p⊥q,then sα,0 = wω and s′
α,0 = w′ω where w and
w′ are precisely the lower and upper Christoﬀel words deﬁned by p and q.It is
easily checked that for 0 ≤ n<p + q,
⌊(n +1) p
q
 ⌋ = ⌊
n p
q
 ⌋ ⇐⇒ np mod p + q< (n +1)p mod p + q.

So the lower Christoﬀel word is obtained simply by considering consecutive values
in the sequence np mod p + q.For p =5 and q = 8, one gets the sequence

0 a
→ 5 a
→ 10 b
→ 2 a
→ 7 a
→ 12 b
→ 4 a
→ 9 b
→ 1 a
→ 6 a
→ 11 b
→ 3 a
→ 8 b
→ 0

This is the construction as given by Christoﬀel in [34]. Another equivalent deﬁ-
nition is by directive sequences and will be given below.
A ﬁnite word w is balanced if, for each pair of factors x, y of w of equal length,∣
∣
∣|x|a −|y|a∣
∣
∣ ≤ 1 for the letter a.Here |x|a denotes the number of occurrences of
a in x.

4.1 Standard and Central Words

A directive sequence d =(d0,d1,...,dk) is a sequence of integers with d0 ≥ 0
and di > 0for i ≥ 1. The standard word produced by d is the word S(d)= sk+1,
where s−1 = b, s0 = a, sn+1 = sdn
n sn−1 ,n ≥ 0 .

Example 8. For d =(3, 1, 2, 1), one gets s1 = a3b, s2 = a3ba, s3 = a3ba4ba4b,
S(d)= s4 = a3ba4ba4ba3ba.
The standard word produced by the empty sequence is a, the standard word
produced by (0) is b.

If k ≥ 0, the sequences d =(d0,d1,...,dk, 1) and d
′ =(d0,d1,...,dk+1) produce
the same word up to the last two letters which are interchanged, because

S(d)= sdk
k sk−1sk ,S(d
′)= sdk
k sksk−1 ,

Sturmian and Episturmian Words 33

and sk−1sk and sksk−1 are easily seen to be the same up to the last two letters,
by induction.
A central word is a standard word without its two last letters: a word x is
central if and only if x = s= for some standard word s.
A upper (lower) Christoﬀel word is a word of the form bxa (axb)for some
central word x.
The relation between the mechanical deﬁnition and the description by the
directive sequence is through the continued fraction expansion of the slope. Let
again p and q be positive integers with p⊥q. The rational number q/p has two
expansions into continued fractions, say

[d0,d1,... ,dk, 1] = [d0,d1,...,dk +1] .

These are the directive sequences for the two standard words with q letters a
and p letters b. For example, if q =5 and p =8, then q/p =[1, 1, 1, 1, 1] =
[1, 1, 1, 2]. Also, for the word s4 = a3ba4ba4ba3ba produced by the directive
sequence d =(3, 1, 2, 1) given above, one has q/p =[3, 1, 2, 1] with p = |s4|a =4
and q = |s4|b = 15.

Proposition 9. Let x be a word. Then the following are equivalent

1. x is a central word;
2. xab is a standard word;
3. xba is a standard word;
4. bxa is an upper Christoﬀel word;
5. axb is a lower Christoﬀel word.

As a consequence, every characterization of central words translates automat-
ically into a characterization of standard words and of Christoﬀel words. In
particular, we may speak about the central word produced by a directive se-
quence, and as mentioned above, the sequences d =(d0,d1,... ,dk, 1) and d
′ =
(d0,d1,...,dk + 1) produce the same central word.

4.2 Characterizations of Central Words

Proposition 10. [35] Aword x is central if and only if the words axb and bxa
are conjugate.

Proposition 11. [36] A word is central if and only if it is a palindrome preﬁx
of a characteristic Sturmian word.

Proposition 12. [23] A word is central if and only if it is a binary right iterated
palindrome.

Proposition 13. [36] Aword w is central if and only if wab or wba is a standard
Sturmian word.

Proposition 14. [36] Aword w is central if and only if it is a palindrome and
wab (or wba)isa productof two palindromes.

34 J. Berstel

Proposition 15. [37] Aword w is a conjugate of a standard Sturmian word if
and only if it is primitive and all its conjugates are balanced.

Proposition 16. [37] Aword w is a conjugate of a standard Sturmian word if
and only if the circular word w has k +1 factors of length k for 0 ≤ k< |w|,and
this holds if and only if w is primitive and has |w|− 1 factors of length |w|− 2.

Proposition 17. [36] Aword w is central if and only if the words awa, awb,
bwa, bwb are balanced.

In fact, a weaker condition is suﬃcient.

Proposition 18. [36] Aword w is central if and only if the words awb and bwa
are balanced.

Proposition 19. [23,38] Aword w is central if and only if it is a palindrome
and the words wa and wb are balanced.

Denote by πw the minimal period of w. Then one has

Proposition 20. [38] Aword w is central if and only if it is a power of a letter
or it is a palindrome and its preﬁx of length πw − 2 is a right special factor of w.

Example 21. Consider the word w = baaabaaab has minimal period 4. Its preﬁx
of length 2 is ba which is not a right special factor of w. So, according to Proposi-
tion 20, this word is not central. The conclusion follows also from Proposition 19,
since wb = baaabaaabb is not balanced.

The next proposition is actually a consequence of a result of [23].

Proposition 22. [39] Aword w is central if it is a power of a single letter or it
satisﬁes the equation w = w1abw2 = w2baw1 with w1,w2 ∈ a, b
∗. Moreover, in
this latter case w1 and w2 are central words, p = |w1| +2 and q = |w2| +2 are
co-prime periods of w and min p, q is the minimal period of w.

Proposition 23. [36] Aword w is central if and only if there exist integers p⊥q
with |w| = p + q − 2 such that w has periods p, q.

There is a duality between periods and number of letters in central words as
already described in [23] and in [40]. Further results are in [24]. This duality has
been developed recently in [41].

Proposition 24. [40] Aword w is central if and only if the word awb is a
balanced Lyndon word.

A Sturmian palindrome is a ﬁnite Sturmian word which is a palindrome. Every
central word is a Sturmian palindrome but the converse is false. For instance,
baab is a Sturmian palindrome (it is a factor of the inﬁnite Fibonacci word
f = abaab ··· ) but is it not central in view of Proposition 18 since bbaaba is not
balanced. The following characterization holds.

Sturmian and Episturmian Words 35

Theorem 25. [37,23,5,38] A word is a Sturmian palindrome if and only if it is
a median factor of a central word.

There are much more Sturmian palindromes than central words. The number of
central words of length n is φ(n + 2) since a central word of length n is described
by two positive integers p⊥q with p + q = n + 2. On the contrary, one has

Theorem 26. [38] Denote by h(n) the number of Sturmian palindromes of
length n.Then

h(2n)= 1 +
 n∑

i=1 φ(2i) ,h(2n +1) = 1+
 n∑

i=1 φ(2i +1) .

4.3 Directive Word and Directive Sequence

Given a directive sequence d =(d0,d1,...), the word S(d) produced by d is a
standard word if d is ﬁnite, a characteristic word if d is inﬁnite. Deﬁne a directive
word δ by δ = ad0bd1ad2 ··· cdn,where c = a if n is even, and c = b otherwise.
The relation between directive words and directive sequences in the binary case
is the following.

Proposition 27. Let d and δ be as above. Then S(d)= ψδ(¯c) where ¯c is the
opposite letter of c and moreover S(d)
= = P (δ).

5 Balance

Let ℓ ≥ 1 be an integer. A set X of words over an alphabet A is ℓ-balanced if, for
each x, y in X of equal length, ∣
∣
∣|x|a −|y|a∣
∣
∣ ≤ ℓ for all letters a.Here |x|a denotes
the number of occurrences of a in x.Aword is ℓ-balanced if the set of its factors
is balanced. Binary balanced words are precisely 1-balanced words. A word w is
strongly balanced if w is primitive and w2 is balanced. A word w such that w2

is balanced, without being necessarily primitive is called cyclically balanced in
[42]. Thus a word is cyclically balanced if it is a power of some strongly balanced
word. For instance, abba is balanced but is not strongly balanced because the
square abbaabba contains both factors aa and bb.The word ababab is cyclically
balanced. A ﬁnite Sturmian word is a word which is a factor of some (inﬁnite)
Sturmian word.

Proposition 28. A ﬁnite binary word is balanced if and only if it is a ﬁnite
Sturmian word.

Proposition 29. [43,42,44] A ﬁnite binary word is strongly balanced if and only
if it is a conjugate of some standard Sturmian word.

For inﬁnite words, we recall the following characterization of Sturmian words.

Proposition 30. A binary inﬁnite word is Sturmian if and only if it is balanced
and aperiodic.

36 J. Berstel

It is easy to ﬁnd balanced eventually periodic words, such as abω. These are not
Sturmian. We discuss this in the next section.
In fact, Sturmian words share a stronger balance property. Denote by |x|u the
number of distinct occurrences of the word u as a factor in the word x,counting
also overlaps. For instance, |abbabaab|ba =2 and |abaababa|aba = 3. Then, one
has

Theorem 31. [45] A binary inﬁnite word w is Sturmian if and only if for each
word u, ∣
∣
∣|x|u −|y|u∣
∣
∣ ≤|u|

for each pair of factors x, y of the same length of w,

A characterization of episturmian words by a balance property like Proposi-
tion 30 does not exist. It is known that the Tribonacci word t is 2-balanced.
However, when applying a well chosen pure epistandard morphism, it does not
remain 2-balanced. For instance, the word μ(t)with μ = ψaabbac,contains the
factors baabaaabaabaabaaabaab and aacaabaabaaabaabaacaa of length 21. In-
deed, the ﬁrst is a factor of μ(bab) and the second is a factor of μ(aca). The
number of b in these factors are 7 and 4, so their balance is 3. It has been proved
by [46] that there exist AR-sequences which not ℓ-balanced for any ℓ.
There is a closed formula for the number of ﬁnite balanced words, that is of
factors of Sturmian words.

Proposition 32. The number of balanced binary words of length n is

1+
 n∑

i=1(n +1 − i)φ(i)

where φ is the Euler’s totient function.

The ﬁrst proof of this formula is perhaps [47]. Other proofs are in [48,36,23,49,50].
Related results also appear in [51,52]. An exact formula for the number gℓ(n)
of ℓ-balance words of length n seems not to be known. It was shown already in
[47] that it is exponential for ℓ ≥ 2 (whereas usual number theory shows that
g1(n)= N 3/π2 + O(n2)) and more exactly that

gℓ(n)= Θ(ℓ +1
⌊ℓ/2⌋

)n/(ℓ+1)

which gives g2(n)= Θ(3n/3). Heinis provided independently in [53] a lower
bound, and Tarannikov [54] shows that

gℓ(n)= Θ(n2(2 cos π
ℓ +2 )
n)

which is better for ℓ ≥ 3.
On the other hand, the number of factors of length n of strict episturmian
words (or equivalently of Arnoux-Rauzy words) has been considered. A bispecial
factor is a word that is both a left and a right special factor of the same Arnoux-
Rauzy word.
 Sturmian and Episturmian Words 37

Proposition 33. [55] The number of factors of length n of strict episturmian
words over a k-letter alphabet is

k +(n − 1)k(k − 1) + (k − 1)
2 n−2∑

i=1 (n − i − 1)b(i)

where b(m) is the number of bispecial factors of length m of Arnoux-Rauzy words.

The number of bispecial factors is evaluated, in [55], in terms of a generalized
Euclidean algorithm.
We already mentioned that episturmian words are not balanced in general. In
fact, almost the opposite is true: episturmian words are never balanced, except
in simple cases. More precisely, the following holds.

Theorem 34. [56] Let x be a standard episturmian word over the alphabet A =
{1, 2,... ,k} with k ≥ 3.Then x is balanced if and only if its directive word δ can
be written in one of the following forms, up to a permutation of the alphabet.

1. 123 ··· k1ω

2. 1n23 ··· (k − 1)kω for some n ≥ 1
3. 12 ··· ℓ1(ℓ +1) ··· (k − 1)kω for some 1 ≤ ℓ<k.

For k = 5, an example of the last case is 121345ω with ℓ = 2. All episturmian
words of the theorem are eventually periodic.

6 Lexicographic Ordering

Every (total) order on an alphabet A deﬁnes a lexicographic order on (right)
inﬁnite words. Given an inﬁnite word x, wedenoteby min(x)and by max(x)the
minimal and the maximal word, for the lexicographic order, of the orbit of x.This
is simply deﬁned by the condition that, for each integer n, the preﬁx of length
n of min(x)(of max(x)) is the smallest (largest) word in Fn(x). For Sturmian
words, it is easily seen that sα,ρ <sα,ρ′ if and only if ρ<ρ′ (recall that α is
irrational). Thus for the ordering a< b, one gets that min(sα,ρ)= sα,0 = acα and
max(sα,ρ)= bcα,where cα denotes the characteristic word with slope α.Asan
example, consider the Fibonacci word f = abaababaabaab ··· .Then min(f )= af
and max(f )= bf .
The comparison of words for the lexicographic order is well suited for the
study of balanced inﬁnite words, and can be extended to the case of more than
two letters. It will be convenient to use the following old terminology from [2].
A Sturmian trajectory is an inﬁnite binary word whose (ﬁnite) factors are ﬁ-
nite Sturmian words. Thus, Sturmian trajectories are precisely balanced binary
words.
Similarly, we call episturmian trajectory an inﬁnite word whose ﬁnite factors
are ﬁnite episturmian words. Episturmian trajectories are called episturmian
words in the wide sense in [57].
It is known since [2] that Sturmian trajectories can be partitioned into three
classes:

38 J. Berstel

1. aperiodic words: these are exactly all Sturmian words or equivalently all
irrational mechanical words;
2. (purely) periodic words : these are the rational mechanical words; they are
of the form wω,where w is a conjugate of some standard word;
3. eventually periodic but not purely periodic words. These are called skew
words. They are not mechanical words. It has been shown that they are
those suﬃxes of the words of the form μ(anbaω), for some pure standard
Sturmian morphism μ and some integer n ≥ 0 which are not suﬃxes of
μ(aω).

The three classes of Sturmian trajectories can be grouped together in three
manners. First, group (1) is compose of aperiodic words whereas groups (2)+ (3)
are eventually periodic words. Next, words in (1) + (2) are uniformly recurrent,
whereas words of type (3) are not recurrent. Finally, words of type (1) + (3) are
precisely the words called ﬁne by Pirillo in [58] and that we will describe in a
moment. First we give the following characterization.

Theorem 35. A binary inﬁnite word x over {a, b} with a<b is a Sturmian
trajectory if and only if there is an inﬁnite y such that ay ≤ min(x) and
max(x) ≤ by.

This is a corollary of the next theorem, and appears also, under a diﬀerent guise,
in [59]. We denote by min(A) the smallest letter in the alphabet A for the given
order.

Theorem 36. [57] An inﬁnite word x over A is an episturmian trajectory if
and only if there exists an inﬁnite word y such that min(A)y ≤ min(x) for every
order over A.

Episturmian trajectories are either episturmian words or belong to the family
of so-called episkew words. These are exactly the episturmian trajectories which
are not recurrent. It is quite interesting to note that the characterization of skew
Sturmian trajectories carries over, with some complications, to episkew words.
This is done in [60], see also [57].

Proposition 37. An inﬁnite word x with A =Alph(x) is episkew if and only
if there is a letter a, a standard episturmian word y on B = A \{a}, a ﬁnite
preﬁx p of y and a pure epistandard morphism μ such that zx = μ(˜pay) for some
proper preﬁx z of μ(˜pa).

If, in the proposition, the word y is strict, then the word x itself is called strict
episkew. Observe also that in the Sturmian case the word ˜pay indeed reduces to
aword of the form apbaω.
In the case of characteristic words or of epistandard words, one has stronger
conditions.

Theorem 38. [61] A binary word x over A = {a, b} with a< b is a character-
istic Sturmian word if and only if ax =min(x) and max(x)= bx.

Sturmian and Episturmian Words 39

A result similar to Theorem 38 holds for strict episturmian (or Arnoux-Rauzy)
words.

Proposition 39. [6] An inﬁnite word x over some alphabet A is a strict epis-
tandard word if and only if min(A)x =min(x) for any order on A.

This is related to the following.

Proposition 40. [61] An inﬁnite word x over some alphabet A is an epistandard
word if and only if min(A)x ≤ min(x) for any order on A.

Let x be an inﬁnite word and let A =Alph(x). The word x is ﬁne if there exists
an inﬁnite word y such that min(x)=min(A)y holds for any lexicographic order.
As announced, we have the following.

Proposition 41. [58] A binary word is ﬁne if and only if it is a Sturmian word
or a skew Sturmian word.

Thus, the Sturmian trajectories which are not ﬁne are precisely the rational
mechanical words. This has been extended to episturmian trajectories.

Proposition 42. [60] Aword x is ﬁne if and only if it is a strict epistandard
word or a strict skew episturmian word.

7 Burrows-Wheeler Transformation

The Burrows-Wheeler transformation, introduced in [62], is a reversible trans-
formation that produces a permutation BWT(w) of an input sequence w.It
appears that the transform is easier to compress than the original sequence be-
cause there is some clustering eﬀect in the transformed word. BWT is used in the
BZIP2 data compression algorithm. The Burrows-Wheeler transformation has a
strong relation to a transformation called the Gessel-Reutenauer transform, in-
troduced in [63]. This connection has been described in [64]. As has been shown
in [65] the Burrows-Wheeler transformation takes a very particular form when
applied to standard Sturmian words. Recent results are given in the forthcoming
paper [66].
The Burrows-Wheeler transformation takes as input a word w, and produces
as output a permutation BWT(w), obtained as follows. Let M (w)be the matrix
composed of all conjugates of w, ordered lexicographically. Then BWT(w)is the
last column of M (w).

Example 43. For the input word w = abraca, the matrix is

M (w)=
 ⎡

⎢
⎢
⎢
⎢
⎢
⎢
⎣

aa b r a c
ab r a c a
ac a a b r
br a c a a
ca ab r a
ra c a a b
⎤

⎥
⎥
⎥
⎥
⎥
⎥
⎦

and the output is the last column, that is BWT(w)= caraab.

40 J. Berstel

Clearly, two words u and v are conjugate if and only if M (u)= M (v). In par-
ticular, BWT(u)= BWT(v). In order to make the transformation injective, the
position of the input word in the matrix is added to the transform. If u = vm

for some integer m and BWT(v)= a0a1 ··· an−1,the BWT(u)= am
0 am
1 ··· am
n−1.
In fact, the matrix M (u) has every row repeated m times and every column
duplicated m times.
The Burrows-Wheeler Transform is reversible: given x = BWT(w)and an
index i, it is possible to recover w. To do this, one ﬁrst recovers the ﬁrst column
of M (w) by ordering lexicographically the letters of the word BWT(w). Next,
one deﬁnes a permutation τ on the set {0,... ,n − 1} that maps a position in
the ﬁrst column of M (w) to the corresponding position in x. This permutation
gives the word w, when started in the position i.

Example 44. Consider x = caraab, and let us compute w such that BWT(w)=
x.The matrix M (w) has the form

M (w)=
 ⎡

⎢
⎢
⎢
⎢
⎢
⎢
⎣

a ·· ·· c
a ·· ·· a
a ·· ·· r
b ·· ·· a
c ·· ·· a
r ·· ·· b
⎤

⎥
⎥
⎥
⎥
⎥
⎥
⎦

The correspondence τ is

τ = (
0 1234 5
1 3450 2
) = (
13 540
)

Thus 13 5240
w = ab r a ca

The main observation concerning the relation with Sturmian words is the fol-
lowing remarkable theorem. Recall that a binary word is strongly balanced if
and only if it is a conjugate of a standard Sturmian word.

Theorem 45. [66] Aword w over {a, b},with a< b is the power of a strongly
balanced word if and only if its Burrows-Wheeler Transform is of the form bqap.
Moreover, in the matrix M (w), each row is obtained from the preceding by re-
placing a factor ab by a factor ba, and all columns also are conjugates.

Example 46. Consider the strongly balanced word abaabab. The matrix is

M (abaabab)=
 ⎡

⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎣

a a babab
aba a bab
aba b a a b
aba b aba
ba a b aba
ba ba aba
ba baba a

⎤

⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎦
 (5)

Sturmian and Episturmian Words 41

Observe that the ﬁrst (last) row is the lower (upper) Christoﬀel word, and these
rows are composed of the central word bordered by a, b and b, a respectively.

The matrix M (w) deﬁned for the Burrows-Wheeler transform has also been
considered in [43] in the process of giving characterizations of strongly balanced
binary words. Denote by P (w) the matrix of partial sums of M (w)where P (w)i,j
is deﬁned to be the number of b in the preﬁx of length j of the ith row in M (w).
For instance, the matrix in (5) has the matrix of partial sums.

P (abaabab)=
 ⎡

⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎢
⎣

001 1223
011 1223
011 2223
011 2233
111 2233
112 2233
112 2333

⎤

⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎥
⎦

They prove the following

Theorem 47. [43] Aword w over {a, b},with a< b is the power of a strongly
balanced word if and only if every column in the matrix of partial sum is increas-
ing when read from top to bottom.

Let us mention brieﬂy the connection of the Burrows-Wheeler and the Gessel-
Reutenauer transformation [63]. The Burrows-Wheeler transformation is the in-
verse of the Gessel-Reutenauer transformation. Deﬁne the standardization asso-
ciated to a word w = a1 ··· an over an ordered alphabet A as the permutation
σ given by
 σ(i) <σ(j)iﬀ ai <aj or (ai = aj and i< j)

Example 48. Consider the word ccbbbcacaaabba. After a lexicographic sort, the
symbols a are at positions 1–5, symbols b at positions 6–10. The symbols c
appear in position 11 to 14. This gives the permutation.
⎛

⎝ 1 2 3 4 5 6 7 8 9 10 11 12 13 14
c c bbb c a c a a a b b a
11 12 678131 14 2 3 4 9 10 5
 ⎞

⎠

After cycle decomposition, one gets

(1 11 4 7)
ca b a (2 12 9)
cba (3 6 13 10)
bc b a (5 8 14)
bca

The result is (caba)(cba)(bcba)(bca)

Theorem 49. [63] The standardization σ induces a bijection between all words
over A and the family of multisets of conjugacy classes of primitive words
over A.

42 J. Berstel

Deﬁne a new order on ﬁnite order on words by

u ≼ v if and only if uω <vω or (uω = vω and |u|≤ |v|)

For example, aba ≺ ab because abaaba ··· < ababab ··· . Recovering the word w
from its decomposition S into conjugacy classes is done as follows: One sorts the
conjugates of words in S by ≺. Then the word w is the sequence of last letters
in this table.

Example 50. Consider the set S = {caba, bcba, bca, cba}. The conjugates of all
words in S are ordered with respect to the new order ≺. This gives the sequence
(abac,abc,abcb, acab,acb,babc, baca,bac,bca,bcba, caba,cab,cbab, cba). The word
composed of the last letters of the words in this sequence is ccbbbcacaaabba.

Conversely, to get the decomposition S from w, one sorts the word w alphabet-
ically, then computes the letter-correspondence permutation and then outputs
the permutation in cycle form, and computes the multiset.

Example 51. Starting with ccbbbcacaaabba, one gets the table
⎛

⎜
⎜
⎝
a a a a a b b b bb cccc
1 2 3 4 5 6 7 8 9 101112 1314
7 9 10 11 14 3 4 5 12 13 1 2 6 8
c c bbb c a c a a a bb a
 ⎞

⎟
⎟
⎠

In cycle form, one gets

(1 7 4 11)
aba c (2 9 12)
abc (3 10 13 6)
ab c b (5 14 8)
acb

The output is the set S = {caba, bca, bcba, cba}.

8 Sturmian Graphs

Given a standard or a central Sturmian word it appears interesting to consider,
in this special case, some well known constructs, such as the (compacted) suﬃx
tree or the suﬃx automaton (also called DAWG for directed acyclic word graph).
A compacted version of the minimal suﬃx automaton has been considered by
[67] for the Fibonacci word and by [68] for arbitrary central words.
The CDWAG (compact directed acyclic word graph) G(w)of a word w is the
minimal automaton recognizing the set of suﬃxes of w, after removing non-ﬁnal
states with out-degree 1.
The terminology DWAG stems from [69]. See also [70].

Example 52. For w = abaababaaba, the automaton G(w) (all states are ﬁnal) is
given in Figure 4.

Any CDAWG is homogeneous, that is all edges leading to a state have the
same label. For the description of the method of construction, we use u[d]to

Sturmian and Episturmian Words 43

a ba aba baaba

ba
 aba
 baaba

Fig. 4. The automaton G(abaababaaba)

denote the reversal of the standard word with directive sequence d.Thus u[21] =
abaa because the standard word produced by (2, 1) is aaba.We write c[d]for the
central word produced by the directive sequence d.Weuse theidentity

c[d0d1 ··· dn1] = u[ε]
d0u[d0]
d1u[d0d1]
d2 ··· u[d0d1 ··· dn−1]
dn .

The CDAWG of a central word c with directive sequence d is constructed by
induction. The method goes as follows. Set d = d
′δ1.

1. if δ ̸= 1, repeat the last edge of the graph of d
′(δ − 1)1.
2. otherwise (that is d ends with 11), set d = d
′′δ′11, take the graph of d
′1, add
anew state and 1 + δ′ edges to this state. The common label of these fresh
edges is u[d
′′].

Example 53. In order to compute the graph of 12311, we start with d = 11,
c[11] = a, and the graph
a

Then, using the second rule with d = 111, c[111] = a|ba,weget

a ba

Now the ﬁrst rule is applied for d = 121, c[121] = a|ba|ba.This gives

a ba ba

For d = 1211 and c[1211] = a|ba|ba|ababa, the second rule gives

a ba ba ababa

For d = 1221, and setting z = ababa,one gets c[1221] = a|ba|ba|z|z and the
graph is
a ba ba z z

For d = 1231, one has c[1231] = a|ba|ba|z|z|z and

a ba ba z z z

44 J. Berstel

Finally, for d = 12311, one gets c[12311] = a|ba|ba|z|z|z|t with t = bazzz and
the graph

a ba ba z z z t

The length of the central word c deﬁned by d =(d0,d1,... ,dk)is |ℓk|− 2,
where ℓn = |sn|− 2and ℓ−1 = ℓ0 =1, ℓn+1 = dnℓn + ℓn−1.Let H(c)be the
graph obtained from the G(c) by replacing each label by its length. Then H(c)
counts from 0 to |c| in the following sense: each integer h with 0 ≤ h ≤|c| is the
sumofthe weightsofexactly one pathin H(c) starting at the initial state. In

a ba ba ababa 1 2 2 5

Fig. 5. The CDAWG for 1211 and the corresponding counting graph

other words, the set of weights in H(c) is complete and unambiguous base for
representing integer up to |c|, provided the representation is a path in the graph.
For example, the graph on the right of Figure 5 counts up to 10.

Problem 54. What is the minimal size of a graph with out-degree at most 2
counting from 0 to n?

If the size of the labels increase exponentially, like for the Fibonacci word, then
thesizeis O(log n). It is conjectured that the bound O(log n) always holds. This
is related to the following number-theoretic conjecture (see [68] for details).

Conjecture 55 (Zaremba). There exists an integer K such that for all positive
m,there exists some i⊥m, i< m such that all partial quotients in the continued
fraction expansions of i/m are bounded by K.

Acknowledgments

I thank Amy Glen, Aldo de Luca for their helpful comments, and Alessandro De
Luca for sending me several preprints.

References

1. Klette, R., Rosenfeld, A.: Digital straightness—a review. Discrete Appl. Math. 139,
197–230 (2004)
2. Morse, M., Hedlund, G.A.: Symbolic dynamics II. Sturmian trajectories. Amer. J.
Math. 62, 1–42 (1940)
 Sturmian and Episturmian Words 45

3. Berstel, J., Boasson, L., Carton, O., Fagnot, I.: A ﬁrst investigation of Sturmian
trees. In: Thomas, W., Weil, P. (eds.) STACS 2007. LNCS, vol. 4393, pp. 73–84.
Springer, Heidelberg (2007)
4. de Luca, A., De Luca, A.: Pseudopalindrome closure operators in free monoids.
Theoret. Comput. Sci. 362(1-3), 282–300 (2006)
5. Droubay, X., Justin, J., Pirillo, G.: Epi-Sturmian words and some constructions of
de Luca and Rauzy. Theoret. Comput. Sci. 255(1-2), 539–553 (2001)
6. Justin, J., Pirillo, G.: On a characteristic property of Arnoux-Rauzy sequences.
Theor. Inform. Appl. 36(4), 385–388 (2002)
7. Justin, J., Pirillo, G.: Episturmian words and episturmian morphisms. Theoret.
Comput. Sci. 276(1-2), 281–313 (2002)
8. Justin, J.: Episturmian words and morphisms (results and conjectures). In: Crapo,
H., Senato, D. (eds.) Algebraic Combinatorics and Computer Science, pp. 533–539.
Springer, Heidelberg (2001)
9. Arnoux, P., Rauzy, G.: Repr´esentation g´eom´etriquedesuitesdecomplexit´e2n +1.
Bull. Soc. Math. France 119, 199–215 (1991)
10. Coven, E.M., Hedlund, G.A.: Sequences with minimal block growth. Math. Systems
Theory 7, 138–153 (1973)
11. Allouche, J.P., Baake, M., Cassaigne, J., Damanik, D.: Palindrome complexity.
Theoret. Comput. Sci. 292(1), 9–31 (2003)
12. Bal´aˇzi, P., Mas´akov´a, Z., Pelantov´a, E.: Factor versus palindromic complexity of
uniformly recurrent inﬁnite words. Theoret. Comput. Sci. 380, 266–275 (2007)
13. Droubay, X., Pirillo, G.: Palindromes and Sturmian words. Theoret. Comput.
Sci. 223(1-2), 73–85 (1999)
14. Damanik, D., Zamboni, L.Q.: Combinatorial properties of Arnoux-Rauzy subshifts
and applications to Schr¨odinger operators. Rev. Math. Phys. 15(7), 745–763 (2003)
15. Avgustinovich, S.V., Fon-Der-Flaas, D.G., Frid, A.E.: Arithmetical complexity of
inﬁnite words. In: Words, Languages and Combinatorics. Proc. 3rd Conf. Words,
Languages and Combinatorics, Kyoto, March 2000, vol. III, pp. 51–62. World Sci-
entiﬁc, Singapore (2003)
16. Cassaigne, J., Frid, A.E.: On the arithmetical complexity of Sturmian words. The-
oret. Comput. Sci. 380, 304–316 (2007)
17. Avgustinovich, S.V., Cassaigne, J., Frid, A.E.: Sequences of low arithmetical com-
plexity. Theor. Inform. Appl. 40(4), 569–582 (2006)
18. Kamae, T., Zamboni, L.Q.: Maximal pattern complexity for discrete systems. Er-
godic Theory Dynam. Systems 22(4), 1201–1214 (2002)
19. Kamae, T., Rao, H., Tan, B., Xue, Y.M.: Language structure of pattern Sturmian
words. Discrete Math. 306(15), 1651–1668 (2006)
20. Kamae, T., Rao, H.: Maximal pattern complexity of words over l letters. European
J. Combin. 27(1), 125–137 (2006)
21. Nakashima, I., Tamura, J.I., Yasutomi, S.I.: Modiﬁed complexity and ∗-Sturmian
word. Proc. Japan Acad. Ser. A Math. Sci. 75(3), 26–28 (1999)
22. Nakashima, I., Tamura, J.I., Yasutomi, S.I.: ∗-Sturmian words and complexity. J.
Theor. Nombres Bordeaux 15(3), 767–804 (2003)
23. de Luca, A.: Sturmian words: structure, combinatorics, and their arithmetics. The-
oret. Comput. Sci. 183(1), 45–82 (1997)
24. de Luca, A.: Combinatorics of standard Sturmian words. In: Mycielski, J., Rozen-
berg, G., Salomaa, A. (eds.) Structures in Logic and Computer Science. LNCS,
vol. 1261, pp. 249–267. Springer, Heidelberg (1997)
25. Risley, R., Zamboni, L.Q.: A generalization of Sturmian sequences: combinatorial
structure and transcendence. Acta Arith. 95, 167–184 (2000)

46 J. Berstel

26. Glen, A.: Powers in a class of ⊣-strict standard episturmian words. Theoret. Com-
put. Sci. 380, 330–354 (2007)
27. Tan, B., Wen, Z.Y.: Some properties of the Tribonacci sequence. European J.
Combin. (2007)
28. Chekhova, N., Hubert, P., Messaoudi, A.: Propri´et´es combinatoires, ergodiques et
arithm´etiques de la substitution de Tribonacci. J. Theor. Nombres Bordeaux 13(2),
371–394 (2001)
29. Lothaire, M.: Applied Combinatorics on Words. Encyclopedia of Mathematics and
its Applications, vol. 105. Cambridge University Press, Cambridge (2005)
30. Series, C.: The geometry of Markoﬀ numbers. Math. Intelligencer 7(3), 20–29 (1985)
31. Berth´e, V., Ei, H., Ito, S., Rao, H.: Invertible substitutions and Sturmian words:
an application to Rauzy fractals. Theor. Inform. Appl. (to appear, 2007)
32. Lothaire, M.: Algebraic Combinatorics on Words. Encyclopedia of Mathematics
and its Applications, vol. 90. Cambridge University Press, Cambridge (2002)
33. Pytheas Fogg, N.: Substitutions in dynamics, arithmetics and combinatorics. In:
Berth´e, V., Ferenczi, S., Mauduit, C., Siegel, A. (eds.) Lecture Notes in Mathe-
matics, vol. 1794, Springer, Heidelberg (2002)
34. Christoﬀel, E.B.: Observatio arithmetica. Annali di Mathematica 6, 145–152 (1875)
35. Pirillo, G.: A curious characteristic property of standard Sturmian words. In:
Crapo, H., Senato, D. (eds.) Algebraic Combinatorics and Computer Science. A
tribute to Gian-Carlo Rota., pp. 541–546. Springer, Heidelberg (2001)
36. de Luca, A., Mignosi, F.: Some combinatorial properties of Sturmian words. The-
oret. Comput. Sci. 136(2), 361–385 (1994)
37. Borel, J.P., Reutenauer, C.: Palindromic factors of billiard words. Theoret. Com-
put. Sci. 340(2), 334–348 (2005)
38. de Luca, A., De Luca, A.: Combinatorial properties of Sturmian palindromes. In-
ternat. J. Found. Comput. Sci. 17(3), 557–573 (2006)
39. Carpi, A., de Luca, A.: Codes of central Sturmian words. Theoret. Comput.
Sci. 340(2), 220–239 (2005)
40. Berstel, J., de Luca, A.: Sturmian words, Lyndon words and trees. Theoret. Com-
put. Sci. 178(1-2), 171–203 (1997)
41. Berth´e, V., de Luca, A., Reutenauer, C.: On an involution of Christoﬀel words and
Sturmian morphisms. In: European J. Combinatorics (in press, 2007)
42. Chuan, W.F.: Moments of conjugacy classes of binary words. Theoret. Comput.
Sci. 310(1-3), 273–285 (2004)
43. Jenkinson, O., Zamboni, L.Q.: Characterisations of balanced words via orderings.
Theoret. Comput. Sci. 310(1-3), 247–271 (2004)
44. de Luca, A., De Luca, A.: Some characterizations of ﬁnite Sturmian words. Theoret.
Comput. Sci. 356(1-2), 118–125 (2006)
45. Fagnot, I., Vuillon, L.: Generalized balances in Sturmian words. Discrete Appl.
Math. 121(1-3), 83–101 (2002)
46. Cassaigne, J., Ferenczi, S., Zamboni, L.Q.: Imbalances in Arnoux-Rauzy sequences.
Ann. Inst. Fourier (Grenoble) 50(4), 1265–1276 (2000)
47. Lipatov, E.P.: A classiﬁcation of binary collections and properties of homogeneity
classes. Problemy Kibernet 39, 67–84 (1982)
48. Mignosi, F.: On the number of factors of Sturmian words. Theoret. Comput.
Sci. 82(1), 71–84 (1991)
49. Berstel, J., Pocchiola, M.: A geometric proof of the enumeration formula for Stur-
mian words. Internat. J. Algebra Comput. 3(3), 349–355 (1993)

Sturmian and Episturmian Words 47

50. Berstel, J., Pocchiola, M.: Random generation of ﬁnite Sturmian words. In: Pro-
ceedings of the 5th Conference on Formal Power Series and Algebraic Combina-
torics (Florence, 1993), vol. 153, pp. 29–39 (1996)
51. Berenstein, C.A., Lavine, D.: On the number of digital straight line segments. IEEE
Trans. Pattern Anal. Mach. Intell. 10(6), 880–887 (1988)
52. Koplowitz, J., Lindenbaum, M., Bruckstein, A.M.: The number of digital straight
lines on an n × n grid. IEEE Transactions on Information Theory 36(1), 192–197
(1990)
53. Heinis, A.: On low-complexity bi-inﬁnite words and their factors. J. Theor. Nom-
bres Bordeaux 13(2), 421–442 (2001)
54. Tarannikov, Y.: On the bounds for the number of ℓ-balanced words. Technical
report, Mech. & Math. Department, Moscow State University (2007)
55. Mignosi, F., Zamboni, L.Q.: On the number of Arnoux-Rauzy words. Boolean
Calculus of Diﬀerences 101(2), 121–129 (2002)
56. Paquin, G., Vuillon, L.: A characterization of balanced episturmian sequences.
Electronic J. Combinatorics 14(1) R33, pages 12 (2007)
57. Glen, A., Justin, J., Pirillo, G.: Characterizations of ﬁnite and inﬁnite episturmian
words via lexicographic orderings. European Journal of Combinatorics (2007)
58. Pirillo, G.: Morse and Hedlund’s skew Sturmian words revisited. Annals Combi-
natorics (to appear, 2007)
59. Gan, S.: Sturmian sequences and the lexicographic world. Proc. Amer. Math.
Soc. 129, electronic, 1445–1451 (2001)
60. Glen, A.: A characterization of ﬁne words over a ﬁnite alphabet. Theoret. Comput.
Sci. CANT conference, Liege, Belgium, May 8-19, 2007, 8–19 (to appear, 2007)
61. Pirillo, G.: Inequalities characterizing standard Sturmian and episturmian words.
Theoret. Comput. Sci. 341, 276–292 (2005)
62. Burrows, M., Wheeler, D.J.: A block sorting data compression algorithm. Technical
report, Digital System Research Center (1994)
63. Gessel, I., Reutenauer, C.: Counting permutations with given cycle structure and
descent set. J. Comb. Theory A 64, 189–215 (1993)
64. Crochemore, M., D´esarm´enien, J., Perrin, D.: A note on the Burrows-Wheeler
transformation. Theoret. Comput. Sci. 332, 567–572 (2005)
65. Mantaci, S., Restivo, A., Sciortino, M.: Burrows Wheeler transform and Sturmian
words. Inform. Proc. Letters 86, 241–246 (2003)
66. Mantaci, S., Restivo, A., Rosone, G., Sciortino, M.: An extension of the Burrows
Wheeler transform. Theoret. Comput. Sci. (2007)
67. Rytter, W.: The structure of subword graphs and suﬃx trees of Fibonacci words.
Theoret. Comput. Sci. 363(2), 211–223 (2006)
68. Epifanio, C., Mignosi, F., Shallit, J., Venturini, I.: On Sturmian graphs. Discrete
Appl. Math 155, 1014–1030 (2007)
69. Blumer, A., Blumer, J.A., Haussler, D., Ehrenfeucht, A., Chen, M.T., Seiferas,
J.I.: The smallest automaton recognizing the subwords of a text. Theoret. Com-
put. Sci. 40(1), 31–55 (1985) (Special issue: Eleventh international colloquium on
automata, languages and programming, Antwerp, (1984)
70. Crochemore, M., Rytter, W.: Jewels of stringology. World Scientiﬁc Publishing Co.
Inc, River Edge, NJ (2003)
