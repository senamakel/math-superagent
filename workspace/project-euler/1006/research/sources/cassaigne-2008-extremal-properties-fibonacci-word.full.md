<!-- source: https://www.numdam.org/item/10.1051/ita:2008003.pdf | converted from PDF -->

RAIRO-Theor. Inf. Appl. 42 (2008) 701–715 Available online at:

DOI: 10.1051/ita:2008003 www.rairo-ita.org

ON EXTREMAL PROPERTIES
OF THE FIBONACCI WORD

Julien Cassaigne 1

Abstract. We survey several quantitative problems on inﬁnite words
related to repetitions, recurrence, and palindromes, for which the
Fibonacci word often exhibits extremal behaviour.

Mathematics Subject Classiﬁcation. 68R15.

1. Introduction

The Fibonacci inﬁnite word,

f = abaababaabaababaababaabaababaabaababaababaabaababaababa . . .

is certainly one of the most often cited examples in the combinatorial theory of
inﬁnite words. It is the archetype of a Sturmian word, and also the ﬁxed point of
a very simple substitution, the Fibonacci substitution ϕ : a ↦→ ab, b ↦→ a.
In many situations, the Fibonacci word happens to have the “best possible”
properties, in the sense that some quantity is maximal or minimal for this word.
In this paper, we present several such situations, and also a few where the Fibonacci
word happens not to be optimal. We consider three diﬀerent classes of problems:
ﬁrst, problems related to repetition of words; then, problems related to the notion
of recurrence; ﬁnally, problems involving palindromes.
Throughout the paper, A is an arbitrary ﬁnite alphabet, and B = {a, b} is the
binary alphabet. The Fibonacci word is the unique inﬁnite word in BN ﬁxed by
the substitution ϕ on B deﬁned above.
We denote by (Fn) the classical sequence of Fibonacci numbers,with F0 =0,
F1 =1 and Fn+1 = Fn + Fn−1, so that the length of the n-th iterate of the
Fibonacci substitution is |ϕ
n(a)| = Fn+2.The golden ratio is denoted Φ = 1+√5
2 .

Keywords and phrases. Fibonacci word, repetitions, recurrence function, palindromes.

1 Institut de math´ematiques de Luminy, case 907, 163 avenue de Luminy, 13288 Marseille
Cedex 9, France; cassaigne@iml.univ-mrs.fr

Article published by EDP Sciences c⃝ EDP Sciences 2008

702 J. CASSAIGNE

Given an inﬁnite word u ∈ A
N, Ln(u) denotes the language of factors of length n
of u (i.e., ﬁnite words of length n that occur as a block of consecutive letters of u)
and L(u) the language of all factors of u.
Let α ∈ [0, 1] \ Q.A word u ∈ BN is called a Sturmian word of slope α when
there exists β ∈ R such that one of the following holds:
(i) for all n ∈ N, un = a if and only if ⌊αn + β⌋ = ⌊α(n +1)+ β⌋;
(ii) for all n ∈ N, un = a if and only if ⌈αn + β⌉ = ⌈α(n +1)+ β⌉.
The letter b occurs then in u with frequency α. The Fibonacci word is a Sturmian
word of slope 2 − Φ. (There are many alternative deﬁnitions for Sturmian words,
see [18], Chap. 2.)
 2. Repetitions

2.1. Index

Let u = u0u1u2 ... ∈ A
N be an inﬁnite word.
The exponent e(w)of a word w ∈ A
∗ is the maximum of |w|/|z| over all words
z ∈ A
+ such that w is a preﬁx of zω.Equivalently, e(w)= |w|/(|w|− |x|), where
x is the maximal border of w, i.e., the longest word that is both a proper preﬁx
and a proper suﬃx of w.If e(w) > 1, then w is called a repetition of exponent
e(w)and of period z.
The index (or critical exponent )of u is the supremum of exponents of repetitions
that occur in u:
 ind(u)= sup{e(w): w ∈ L(u)}∈ (1, +∞].

Periodic words, among others, have inﬁnite index, and it is not diﬃcult to con-
struct words with arbitrarily big but ﬁnite index. On the other hand, on a given
alphabet there is a lowest possible index, and ﬁnding that index is a problem
known as Dejean’s conjecture [14]. Currently, it is solved for alphabets of size
k ≤ 14 [12,24,25] as well as for alphabets of size k ≥ 33 [6]; for the remaining
cases, it is conjectured to be equal to k/(k − 1).
On a binary alphabet, the lowest possible index is 2, as is well known since
the work of Thue [28], and the standard example of a word with index 2 is the
Prouhet-Thue-Morse word (see Sect. 6 for more on this word).
Here, the Fibonacci word is far from optimal since ind(f )=Φ + 2 ≃ 3.618 [19].
For instance, the cube (aba)
3 occurs in f at position 5.
However, it is optimal among Sturmian words. A general formula for the index
of a Sturmian word was given independently by Carpi and de Luca [7]and by
Damanik and Lenz [13](seealso [3]):

Theorem 2.1. If u is a Sturmian word of slope α =[0; a1,a2,a3,...],then

ind(u)= sup
n≥0
 (
2+ an+1 + qn−1 − 2
qn
 ) ,

ON EXTREMAL PROPERTIES OF THE FIBONACCI WORD 703

where qn is the denominator of [0; a1,a2,a3,...,an] and satisﬁes q−1 =0, q0 =1,
qn+1 = an+1qn + qn−1.

From this theorem, we ﬁrst recover the fact that ind(f )= Φ + 2, since f has
slope 2 − Φ=[0; 2, 1, 1,...] We also deduce that this is the smallest possible
index for Sturmian words. Indeed, if the partial quotients are eventually 1, then
ind(u) ≥ lim
n→∞(3 + qn−1/qn) = Φ + 2; otherwise, choosing n such that qn−1 ≥ 2

and an+1 ≥ 2, we ﬁnd that ind(u) ≥ 4.
However, the Fibonacci word and its subshift (i.e., Sturmian words that share
the same slope) are not the only Sturmian words that achieve the lowest possible
index. Those were classiﬁed by Carpi and de Luca [7]:

Theorem 2.2. Let u be Sturmian word. Then ind(u)=Φ + 2 if and only if the
slope of u is one of the six numbers

3−Φ
5 =[0; 3, 1, 1, 1,...] ≃ .276 Φ+2
5 =[0; 1, 2, 1, 1, 1,...] ≃ .724
2 − Φ= [0; 2, 1, 1,...] ≃ .382 Φ − 1=[0; 1, 1, 1,...] ≃ .618
Φ+3
11 =[0; 2, 2, 1, 1, 1,...] ≃ .420 8−Φ
11 =[0; 1, 1, 2, 1, 1, 1,...] ≃ .580.

Then u is in the subshift generated respectively by h1(f ), f , h2(f ), E(h1(f )), E(f ),
or E(h2(f )),where h1(a)= aab, h1(b)= a, h2(a)= ababa, h2(b)= ab, E(a)= b,
E(b)= a.

Sturmian words of slope Φ+4
19 and 15−Φ
19 have index 11
3 > Φ+ 2. All other
Sturmian words have index at least 4.

2.2. Long repetitions

If we consider only arbitrarily long repetitions, we deﬁne the asymptotic index :

ind
∗(u) = lim
n→∞ sup{e(w): w ∈ L(u)and |w|≥ n}∈ [1, +∞].

Obviously, ind∗(u) ≤ ind(u).
The asymptotic index for Sturmian words was computed by Vandeth [29](ac-
tually, the theorem is stated there only for Sturmian words that are ﬁxed points
of substitutions, but it remains valid in general).

Theorem 2.3. If u is a Sturmian word of slope α =[0; a1,a2,a3,...],then

ind∗(u) = 2 + lim sup
n→∞ [an; an−1,an−2,...,a1] ∈ [1, +∞].

With ind∗(f ) = Φ+2, the Fibonacci word is again optimal among Sturmian words,
as well as σ(f ) for any Sturmian morphism σ.
We may wonder if the Prouhet-Thue-Morse word t is still optimal among all
binary inﬁnite words. As any binary ﬁxed point, t has arbitrarily long squares,
therefore ind
∗(t)= ind(t) = 2. There exist binary words without long squares
[16], but a word without long squares may still have asymptotic index 2. Actually,
we found that asymptotic index 1 is achievable, and this is obviously optimal.

704 J. CASSAIGNE

Theorem 2.4. There exists a binary inﬁnite word u such that ind
∗(u)=1.

Proof. Deﬁne v ∈{0, 1,... , 7}N with:

{ v2n =2n mod 8
v2k+1n+2k−1 =2⌊n/2k⌋ +1 mod 8

and let u = σ(v), where σ(i)= a8−ibi+1:

v = 012141610321436105214561072147610123416103234361052345610 ...;

u = aaaaaaaabaaaaaaabbaaaaaabbbaaaaaaabbaaaabbbbbaaaaaaabbaab . . .

Then ind
∗(u)=ind
∗(v)= 1.
Indeed, if w = xyx ∈ L(v)and k = ⌊log2 |x|⌋,then |xy|≥ 22k+1 ≥ 1
2 (|x| +1)
2

by Lemma 2.5 below. Therefore e(w)=1 + O(1/√
|w|), and ind∗(v)= 1. By
Lemma 2.6 below, ind
∗(u)= 1 too. □

Lemma 2.5. Let v be deﬁned as in Theorem 2.4, k ∈ N,and x ∈ L(v) such that
2k ≤|x| < 2k+1. Then there exists i ∈ Z such that all occurrences of x in v are at
position i +22k+1n for some n ∈ Z.

Proof. It is suﬃcient to consider the case when |x| =2k. The proof is by induction
on k.
If k =0, then x is a single digit and one can take i = x. Indeed, by construction,
even digits x ∈{0, 2, 4, 6} occur only at even positions in v, whereas odd digits
x ∈{1, 3, 5, 7} occur only at odd positions.
Assume that the property holds for a given k, and consider the word x =
x0x1 ...x2k+1−1 ∈ L(v)with |x| =2k+1. By the induction hypothesis, there exists
i ∈ Z such that all occurrences of the preﬁx of length 2k of x in v are at position
i +22k+1n for some n ∈ Z. In particular, this applies to occurrences of x.Let
j =2k − 1 − i mod 2k+1 and m =(i + j − 2k +1)/2k+1.If x occurs in v at position
i +22k+1n,then xj occurs at position i +22k+1n + j =2k − 1+2k+1(2kn + m). By
the deﬁnition of v we then have xj =2(n + ⌊m/2k⌋) + 1 mod 8. Therefore n is
determined modulo 4. Let i′ = i +22k(xj − 1 − 2⌊m/2k⌋). Then all occurrences
of x in v are at position i′ +22k+3n′ for some n′ ∈ Z. □

Lemma 2.6. Let A = {c1,c2,...,cd} be any ﬁnite alphabet, and deﬁne the sub-
stitution σ from A
∗ to B∗ by σ(ci)= ad+1−ibi for all ci ∈ A.Then σ preserves
ind
∗, i.e., if v is any inﬁnite word in A
N and u = σ(v),then ind
∗(u)= ind
∗(v).

Proof. It is clear that e(σ(w)) ≥ e(w) for all w ∈ L(v), therefore ind∗(u) ≥ ind
∗(v)
(this holds for any uniform substitution).
Conversely, observe that ba does not occur in σ(A), but always occurs when
two such image words are concatenated. Let w′ ∈ L(u), x
′ be its maximal border,
and z′ the corresponding period, so that w′ = z′x
′. Then either |x
′|≤ d +1 or
x
′ contains ba. In the former case e(w′)= |w′|/(|w′|− |x
′|)=1 + O(1/|w′|). In
the latter case one can write x
′ = sσ(x)p and z′s = sσ(z), with |p|≤ d, |s|≤ d,

ON EXTREMAL PROPERTIES OF THE FIBONACCI WORD 705

and w = zx ∈ L(v), z being a period of w.We have |z′| =(d +1)|z| and
|w′|≤ (d +1)|w| +2d, hence e(w′)= |w′|/|z′|≤ (|w| +2)/|z|≤ e(w)(1 + O(1/|w|)).
Therefore ind∗(u) ≤ ind∗(v). □

2.3. Initial repetitions

Let us now restrict to initial repetitions, i.e., repetitions that occur as preﬁxes.
The initial critical exponent of u is the supremum of exponents of repetitions that
are preﬁxes of u:
 ice(u)= sup{e(w): w preﬁx of u}∈ [1, +∞].

If only long repetitions are considered, we get the asymptotic initial critical exponent:

ice∗(u) = lim
n→∞ sup{e(w): w preﬁx of u and |w|≥ n}∈ [1, +∞].

Among all inﬁnite words, ice(abω)= ice∗(abω) = 1 is trivially optimal.
One has ice(f )= ice∗(f ) = Φ + 1, so we may expect f to be optimal among
Sturmian words.
Every Sturmian word u has inﬁnitely many square preﬁxes [2] hence ice(u) ≥
ice∗(u) ≥ 2. Berth´e et al. [4] constructed a class of Sturmian words such that
ice∗(u)= 2 (see Th. 1.1 of [4]). One such word is:

Proposition 2.7. Let α = ∞∑

n=1 fn2−n be the real number whose binary expansion

is the Fibonacci word, where the letters are assigned the values a =1 and b =0:
α = .1011010110110 ...2 ≃ .710. Then the continued fraction expansion of α is
α =[0; 20, 21, 21, 22, 23, 25, 28, 213, 221, 234,...], where exponents are the Fibonacci
numbers, and there is a Sturmian word u of slope α such that ice∗(u)= 2.

Proof. We only need to compute the continued fraction expansion of α,as the last
statement follows from [4].
Let an =2Fn−1 be the desired partial quotients; then the continued fraction is
equal to lim
n→∞ pn/qn where p−1 =1, p0 =0, q−1 =0, q0 =1, pn+1 = an+1pn+pn−1,

qn+1 = an+1qn + qn−1. We prove by induction that qn =2Fn+1 − 1: indeed, if
qn =2Fn+1 − 1and qn−1 =2Fn − 1, then

qn+1 =2Fn(2Fn+1 − 1) + 2Fn − 1= 2Fn+2 − 1.

Also by induction, we prove that pn = Fn+1∑

i=1 fi2Fn+1−i is the integer whose binary

expansion is the preﬁx of length Fn+1 of f , i.e., ϕ
n−1(a). Indeed, the relation
pn+1 =2Fn pn + pn−1 amounts to concatenating the binary expansions of pn and
pn−1,and we know that ϕ
n(a)= ϕ
n−1(a)ϕ
n−2(a). Finally,

lim
n→∞ pn
qn =
 ∞∑

i=1 fi2−i = α. □

706 J. CASSAIGNE

2.4. Initial repetitions in a subshift

The index of an inﬁnite word depends only on its language of factors; conse-
quently, all elements of a minimal subshift have the same index since they all have
the same language of factors. On the other hand, the initial critical exponent and
its asymptotic counterpart are dependent on the particular inﬁnite word that is
considered, so it is interesting to study how they vary within a given subshift.
Let I(u) be the inﬁmum of ice∗(v)where v is in the subshift generated by u.

Theorem 2.8. The Fibonacci word is maximal for I among all non periodic words.

Proof. Obviously, I(u) is inﬁnite when u is periodic, so periodic words should be
excluded. Mignosi et al. [20]proved that I(u) ≤ Φ + 1 for any non periodic u.
Berth´e et al. [4]proved thatif u is in the Fibonacci subshift, and is not in
the shift orbit of f , then it begins in arbitrarily long cubes: ice
∗(u) ≥ 3(see
Prop. 4.3 of [4]). Therefore the minimum is attained in the shift orbit of f ,where
ice∗(u)= ice∗(f )=Φ + 1. Hence I(f )= Φ + 1. □

3. Recurrence

The recurrence function of an inﬁnite word u was introduced by Morse and
Hedlund [22]. It is deﬁned by

R(n)= inf{N ∈ N : ∀w ∈ LN (u),Ln(w)= Ln(u)}∈ N ∪{+∞}

and the recurrence quotient of u by

ρ∗(u) = lim sup
n→∞ R(n)
n ∈ [1, +∞].

The recurrence quotient of Sturmian words can be easily computed from the con-
tinued fraction expansion of their slope [10]:

Theorem 3.1. If u is a Sturmian word of slope α =[0; a1,a2,a3,...],then

ρ∗(u) = 2 + lim sup
n→∞ [an; an−1,an−2,... ,a1].

Consequently, as was already known by Morse and Hedlund [23], the Fibonacci
word has ρ∗(f ) = Φ + 2 and this is the lowest possible value for a Sturmian word,
for as soon as an is not eventually 1, ρ∗(u) ≥ 3+ √
2.
Actually, f seems to be also optimal among non-periodic words, as conjectured
by Rauzy [27].

3.1. Recurrence quotient and asymptotic index

We observe that a bound on the asymptotic index can be derived from the
recurrence quotient.

ON EXTREMAL PROPERTIES OF THE FIBONACCI WORD 707

Proposition 3.2. For any inﬁnite word u, ind
∗(u) ≥ 1+ 1
ρ∗(u)−1 .

Proof. If ρ∗(u)=+∞, the inequality obviously holds as ind∗(u) ≥ 1.
Assume now that ρ∗(u) is ﬁnite, so R(n) is ﬁnite too. Let xn be the preﬁx of
length n of u,and zn be the shortest preﬁx of u such that znxn is alsoapreﬁx
of u (in other words, |zn| is the position of the second occurrence of xn in u).
Observe that the word obtained by removing the ﬁrst and last letters in znxn does
not contain xn, hence |zn| + n − 2 <R(n). Then obviously

ind
∗(u) ≥ ice∗(u) = lim sup
n→∞ n
|zn| +1

and
 ρ∗(u) = lim sup
n→∞ R(n)
n ≥ lim inf
n→∞ R(n)
n ≥ lim inf
n→∞ |zn|
n +1

and the result follows from

lim sup
n→∞ n
|zn| = ( lim inf
n→∞ |zn|
n
 )−1. □

In particular, when ind
∗(u)=1, then ρ∗(u) has to be inﬁnite. Apart from this
case, and the periodic case where ind∗(u)=+∞ and ρ∗(u) = 1, equality cannot
hold, as a consequence of the result of [11]that R(n)/n cannot converge to a ﬁnite
limit when u is not periodic.

Open problem 1. What is the inﬁmum of (ind
∗(u) − 1)(ρ∗(u) − 1) over all
words u for which both ind
∗(u)and ρ∗(u) are ﬁnite?

The above inequality may suggest that ind
∗ and ρ∗ vary somehow in opposite
directions. However, this is not at all the case for Sturmian words:

Theorem 3.3. If u is a Sturmian word, then ρ∗(u)=ind
∗(u).

Proof. Just observe that Theorems 2.1 and 3.1 contain exactly the same formula.
If u is a Sturmian word of slope α =[0; a1,a2,a3,...], then

ind
∗(u) = 2 + lim sup
n→∞ [an; an−1,an−2,... ,a1]

and
 ρ∗(u) = 2 + lim sup
n→∞ [an; an−1,an−2,... ,a1]. □

Open problem 2. How can this equality be explained? Does it characterize
Sturmian words? (Compare, for instance, with the Prouhet-Thue-Morse word
which has ind
∗(t)=2 and ρ∗(t) = 10, see Prop. 6.1.)

708 J. CASSAIGNE

3.2. First occurrence

We now consider preﬁxes. Analogously to the recurrence function, we deﬁne

R′(n)= inf{N ∈ N : Ln(u0 ... uN −1)= Ln(u)}

and
 ρ′∗(u) = lim sup
n→∞ R′(n)
n ∈ [1, +∞].

Note that R′(n) − n + 1 is the maximal position where a factor of length n occurs
for the ﬁrst time.
When u is eventually periodic, obviously ρ′∗(u) = 1. Surprisingly, the lowest
possible value for ρ′∗ among non eventually periodic words is not attained by the
Fibonacci word, for which ρ′∗(f ) = Φ + 1, but by another Sturmian word [9]:

Theorem 3.4. Let u be the ﬁxed point of a ↦→ abaababa, b ↦→ aba:

u = abaababaabaabaababaabaababaabaabaababaabaabaababaabaababaabaaba . . .

u is a non-standard Sturmian word, with slope 5−√
10
5 .Then

ρ′∗(u)= 29 − 2√
10
9 ≃ 2.519 < 2.618 ≃ Φ+1,

and this is optimal.
 4. Palindromes

4.1. Palindrome densities

A palindrome is a ﬁnite word w which is equal to its mirror image ˜w.The
only inﬁnite word all factors of which are palindromes is the constant word aω;
other eventually periodic words may have a positive proportion of palindromes
(for instance, one third of the factors of (aab)
ω of each length are palindromes),
or no palindromes after a certain length (like (aababb)
ω).
Assume now that u is non eventually periodic. Let fac(n)bethe subword
complexity of u (i.e., the number of its factors of length n,fac(n)=#Ln(u)),
and pal(n) its palindrome complexity (i.e., the number of palindromes of length n
that are factors of u). As pal(n) is usually much smaller than fac(n), instead of a
proportion it is more interesting to consider the lower palindrome density

π(u) = lim inf
n→∞ n pal(n)
fac(n)

ON EXTREMAL PROPERTIES OF THE FIBONACCI WORD 709

and the total lower palindrome density

¯π(u) = lim inf
n→∞
 n n−1∑

k=0 pal(k)

n−1∑

k=0 fac(k) ·

For Sturmian words, π(u)=1 and ¯π(u) = 3, as follows from the characterization
of Sturmian words using palindromes by Droubay and Pirillo [15]. Compare with
the Prouhet-Thue-Morse word t: as pal(5) = 0, the function pal(n) vanishes for
odd n and π(t) = 0; but there are inﬁnitely many palindromes of even length and
one can compute that ¯π(t)=20/19, see Proposition 6.3.

Open problem 3. Does there exist a non eventually periodic inﬁnite word u
such that π(u) > 1or ¯π(u) > 3?

Note that, on the other hand, the upper palindrome density lim sup
n→∞
 n pal(n)
fac(n) can

be inﬁnite, as shown in [1], Remark 9.

4.2. Palindromic prefixes

Let n0 =0, n1 =1, n2, . . . be the lengths, in increasing order, of palindromes
that are preﬁxes of u. Deﬁne then the palindromic preﬁx gap by

δ(u) = lim sup
i→∞
 ni+1
ni

with the convention δ(u)=+∞ if u has ﬁnitely many palindromic preﬁxes.
If u is periodic with palindromic period, δ(u) = 1. For the Fibonacci word, ni =
Fi+3 − 2 hence δ(u) = Φ. For any other inﬁnite word, δ(u) ≥ 1+ √
2/2 > Φ[17].

4.3. First occurrence of a palindrome

We conclude with one last open problem.
Let u be a non eventually periodic word containing palindromes of each length.
Let p1(n) be the starting position of the ﬁrst occurrence of a palindrome of length n
in u, and deﬁne the ﬁrst palindrome occurrence rate by

ψ(u) = lim sup
n→∞ p1(n)
n ·

The Fibonacci word has ψ(f )= Φ.

Open problem 4. What is the minimal value of ψ for non eventually periodic
words, and for which word is it attained (if it is)?

710 J. CASSAIGNE

5. Summary

Index ind(u)
Among all words: inﬁmum 1 (not attained), maximum +∞.
Among binary words: minimum ind(t)=2, maximum +∞.
Among Sturmian words: minimum ind(f )=Φ + 2, maximum +∞ (with gaps, e.g.
(Φ + 2, 11/3)).

Asymptotic index ind
∗(u)
Among all words, or binary words: minimum 1 (see Th. 2.4), maximum +∞.
Among Sturmian words: minimum ind
∗(f )=Φ + 2, maximum +∞.

Initial critical exponent ice(u)
Among all words: minimum ice(abω) = 1, maximum ice(aω)= +∞. (ice(f )=
Φ + 1)).

Asymptotic initial critical exponent ice∗(u)
Among Sturmian words: minimum 2 (see Prop. 2.7), maximum +∞.

Minimal asymptotic initial critical exponent in a subshift I(u)
Among all words: minimum I(abω)= 1, maximum I(aω)= +∞.
Among non (purely) periodic words: minimum I(abω)= 1, maximum I(f )= Φ+1.
Among Sturmian words: minimum 2 (see Prop. 2.7), maximum I(f )=Φ + 1.

Recurrence quotient ρ∗(u)
Among Sturmian words: minimum ρ∗(f )= Φ + 2, maximum +∞ (with gaps, e.g.
(Φ + 2, 3+ √
2)).

First occurrence quotient ρ′∗(u)
Among all words: minimum ρ′∗(aω)= 1, maximum +∞.
Among non eventually periodic words: minimum 29−2
√
10
9 (see Th. 3.4), maximum
+∞ (ρ′∗(f )=Φ + 1).

Lower palindrome density π(u)
Among non eventually periodic words: minimum 0, maximum unknown.
Among Sturmian words: constant 1.

Total lower palindrome density ¯π(u)
Among non eventually periodic words: minimum 0, maximum unknown.
Among Sturmian words: constant 3.

Palindromic preﬁx gap δ(u)
Among all words: minimum 1, maximum +∞.
Among non periodic words: minimum δ(f )=Φ, maximum +∞ (with gaps, e.g.
(Φ, 1+ √
2/2)).

First palindrome occurrence rate ψ(u)
Among non eventually periodic words: minimum unknown, maximum +∞
(ψ(f )=Φ).
 ON EXTREMAL PROPERTIES OF THE FIBONACCI WORD 711

6. Appendix on the Prouhet-Thue-Morse word

A few properties of the Prouhet-Thue-Morse word that have been used here do
not seem to be published elsewhere. For the sake of completeness, we include a
sketch of their proof.
The Prouhet-Thue-Morse word

t = abbabaabbaababbabaababbaabbabaabbaababbaabbabaababbabaabbaab . . .

is the only ﬁxed point beginning with a of the substitution θ : a ↦→ ab, b ↦→ ba.It
was ﬁrst deﬁned by Thue [28], who proved that it is overlap-free, hence of index 2.
It was later rediscovered by Morse [21], and was already implicit in the work of
Prouhet [26].
The subword complexity of t was computed by Brlek [5] and satisﬁes the formula

fac(n)=
 ⎧
⎪⎪⎪⎪⎨

⎪⎪⎪⎪⎩
 1if n =0
2if n =1
4if n =2
4n − 2.2k − 4if 2.2k <n ≤ 3.2k

2n +4.2k − 2if 3.2k <n ≤ 4.2k

for every k ∈ N. A nice way to obtain this formula is to use special factors and
bispecial factors,see [8].
The recurrence function of t can be computed in a similar way, using singular
factors,see [10]. A singular factor of an inﬁnite word u ∈ A
N is either a letter
or a factor w = xvy ∈ L(u) such that x
′vy and xvy′ are also factors of u,where
x, x
′,y,y′ ∈ A, x ̸= x
′,and y ̸= y′.Then v is a bispecial factor, so the set of
singular factors S can be easily deduced from that of bispecial factors. For each
w ∈ S, consider the set r(w)of return words of w (a return word of w in u is a
word z such that zw is a factor of u, w is a preﬁx of zw,and w is not an inner
factor of zw)and the return time of w, α(w)= max{|z| : z ∈ r(w)}.Then R(n)is
given for all n ≥ 1 by the formula

R(n)= n − 1+max{α(w): w ∈ S and |w|≤ n}

so that ρ∗(u) = 1 + lim sup
w∈S
 ℓ(w)
|w| .

Proposition 6.1. The recurrence function of t is given by

R(n)=
 ⎧
⎪⎪⎨

⎪⎪⎩
 0 if n =0
3 if n =1
9 if n =2
n − 1+9.2⌊log2(n−2)⌋ if n ≥ 3

and its recurrence quotient is ρ∗(t)= 10.

712 J. CASSAIGNE

Proof. The set of singular factors of t is:

S = {a, b, aa, ab, ba, bb, aba, bab}∪ {xθk(z)y : x, y, z ∈ B and k ≥ 1}.

The return words of small singular factors are listed below, up to symmetries
(mirror w ↦→ ˜w and alphabet permutation w ↦→ E(w)):

r(a)= {a, ab, abb};

r(ab)= {ab, aba, abb, abba};
r(aa)= {aabb, aababb, aabbab, aababbab};

r(aba)= {aba, ababb, abaabba, ababbaabb};
r(aabb)= {aabbab, aabbaababb, aabbabaababbab, aabbaababbabaababb};

r(abaa)= {abaababb, abaabbaababb, abaababbaabb, abaabbaababbaabb};
r(abab)= {ababbaba, ababbaabbaba, ababbabaabba, ababbaabbabaabba}.

The return words of other singular factors are obtained recursively, using the
following lemma: if x, y, z ∈ B and k ≥ 2, then

r(xθk(z)y)= E(x)
−1θ (r (
E(x)θk−1(z)y)) E(x)

(recall that E(a)= b and E(b)= a,so that θ(E(x)) = E(x)x). As a consequence,
α(xθk(z)y)= 2α(E(x)θk−1(z)y), and we get α(xθk(z)y)=2kc with c =9 (if k is
odd and x = z ̸= y,or if k is even and x = y ̸= z)or c = 8 (otherwise). We deduce
that R(n)= n − 1+9.2k for 2k +2 ≤ n< 2k+1 + 2, for all k ∈ N. As a direct
consequence, ρ∗(t) = 10. □

Palindromes in t can be described recursively. It is easier to simultaneously
describe antipalindromes, i.e.,words w such that ˜w = E(w). Let ap(n)denote
the number of antipalindromes of length n in t. Let also PAL denote the set of
all palindromes in t and AP the set of all antipalindromes in t.If w is a word
of length at least 2, let γ(w) be the word obtained by deleting the ﬁrst and last
letter in w.

Lemma 6.2. The sets PAL and AP satisfy

PAL = {a, b, aba, bab}∪ θ(AP) ∪ γ(θ(AP))

AP = θ(PAL) ∪ γ(θ(PAL))

ON EXTREMAL PROPERTIES OF THE FIBONACCI WORD 713

and the functions pal(n) and ap(n) satisfy

pal(4n)= ap(2n)
pal(4n +2) = ap(2n +2)

pal(1) = 2
pal(3) = 2

pal(2n +1) = 0 (if n ≥ 2)
ap(0) = 1

ap(2) = 2
ap(2n)= pal(n)+pal(n +1) (if n ≥ 2)

ap(2n +1) = 0

for all n ∈ N (except when otherwise noted). They are given by

pal(n)=
 ⎧
⎪⎪⎪⎪⎨

⎪⎪⎪⎪⎩
 1 if n =0
2 if 1 ≤ n ≤ 4
0 if n ≥ 5 and n is odd
2 if 3.4k <n ≤ 4k+1 and n is even
4 if 4k+1 <n ≤ 3.4k+1 and n is even

ap(n)=
 ⎧
⎪⎪⎪⎪⎨

⎪⎪⎪⎪⎩
 0 if n is odd
1 if n =0
2 if n =2
4 if 2.4k <n ≤ 6.4k and n is even
2 if 6.4k <n ≤ 2.4k+1 and n is even
for all k ∈ N.

Proof. Observe ﬁrst that ̃θ(w)= E(θ(˜w)). As a consequence, θ(PAL) ⊆ AP and
θ(AP) ⊆ PAL. It is also clear that PAL and AP are stable under γ.This proves
inclusions in one direction.
To prove the reverse inclusions, consider ﬁrst palindromes of odd length. It is
easy to check that among the four palindromes of length 3, only two occur in t,
and that none of the eight palindromes of length 5 occurs in t; therefore no longer
palindrome of odd length occurs in t. Obviously there are no antipalindromes of
odd length.
Consider now factors of even length. A factor w of t of even length is always
either of the form θ(w′) (if it occurs at an even position) or γ(θ(w′)) (if it occurs
at an odd position). If w is a palindrome, then w′ is an antipalindrome, and if w is
an antipalindrome, then w′ is a palindrome. This proves the language equalities.
To get the recurrence relations, one has to pay attention to the fact that the
language equalities may be ambiguous; for instance, ab is both in θ(PAL) and
γ(θ(PAL)). One checks that θ(A
∗) ∩ γ(θ(A
∗)) = {ab}∗ ∪{ba}∗, and consequently
θ(L(t))∩γ(θ(L(t))) = {ε, ab, ba} so ambiguity aﬀects only words of length up to 2.
The last formulas are easily deduced from the recurrence relations. □

714 J. CASSAIGNE

Proposition 6.3. The total lower palindrome density of the Prouhet-Thue-Morse
word is ¯π(t)= 20/19.

Proof. Recall that ¯π(t) = lim inf
n→∞ g(n)

where
 g(n)= n n−1∑

k=0 pal(k)

n−1∑

k=0 fac(k) ·

From the formulas for pal(n)and fac(n), a long but elementary computation pro-
duces a formula for g(n), with eight diﬀerent cases. For instance, if n is odd and
4.4k <n ≤ 6.4k, one has

g(n)= n(6n +1 − 4.4k)
6n2 − 12.4kn +28.42k − 18n +18.4k +23 ·

One ﬁnds that lim inf
n→∞ g(n) = lim
k→∞ g(4k +1) = 20
19 and lim sup
n→∞ g(n)= 39+√1554
66 . □

References

[1] J.-P. Allouche, M. Baake, J. Cassaigne and D. Damanik, Palindrome complexity. Theoret.
Comput. Sci. 292 (2003) 9–31.
[2] J.-P. Allouche, J.L. Davison, M. Queﬀ´elec and L.Q. Zamboni, Transcendence of Sturmian
or morphic continued fractions. J. Number Theory 91 (2001) 39–66.
[3] J. Berstel, On the index of Sturmian words, in Jewels are Forever. Springer, Berlin (1999)
287–294.
[4] V. Berth´e, C. Holton and L.Q. Zamboni, Initial powers of Sturmian sequences. Acta Arith.
122 (2006) 315–347.
[5] S. Brlek, Enumeration of factors in the Thue-Morse word. Discrete Appl. Math. 24 (1989)
83–96.
[6] A. Carpi, On Dejean’s conjecture over large alphabets. Theoret. Comput. Sci. 385 (2007)
137–151.
[7] A. Carpi and A. de Luca, Special factors, periodicity, an application to Sturmian words.
Acta Inform. 36 (2000) 983–1006.
[8] J. Cassaigne, Complexit´eet facteurs sp´eciaux. Bull. Belg. Math. Soc. Simon Stevin 4 (1997)
67–88.
[9] J. Cassaigne, On a conjecture of J. Shallit, in Automata, languages and programming
(ICALP 1997), Springer, Berlin. Lect. Notes Comput. Sci. 1256 (1997) 693–704.
[10] J. Cassaigne, Limit values of the recurrence quotient of Sturmian sequences. Theoret.
Comput. Sci. 218 (1999) 3–12.
[11] J. Cassaigne and N. Chekhova, Fonctions de r´ecurrence des suites d’Arnoux-Rauzy et
r´eponse `a une question de Morse et Hedlund. Ann. Inst. Fourier (Grenoble) 56 (2006)
2249–2270.
[12] J.D. Currie and M. Mohammad-Noori, Dejean’s conjecture and Sturmian words. Eur. J.
Combin. 28 (2007) 876–890. Also in Morteza Mohammad-Noori, PhD. thesis, Universit´e
Paris-Sud (2005).

ON EXTREMAL PROPERTIES OF THE FIBONACCI WORD 715

[13] D. Damanik and D. Lenz, The index of Sturmian sequences. Eur. J. Combin. 23 (2002)
23–29.
[14] F. Dejean, Sur un th´eor`eme de Thue. J. Comb. Theory A 13 (1972) 90–99.
[15] X. Droubay and G. Pirillo, Palindromes and Sturmian words. Theoret. Comput. Sci. 223
(1999) 73–85.
[16] R.C. Entringer, D.E. Jackson and J.A. Schatz, On nonrepetitive sequences. J. Comb. Theory
A 16 (1974) 159–164.
[17] S. Fischler, Palindromic preﬁxes and episturmian words. J. Comb. Theory A 113 (2006)
1281–1304.
[18] M. Lothaire, Algebraic combinatorics on words, Encyclopedia of Mathematics and its
Applications 90. Cambridge University Press, Cambridge (2002).
[19] F. Mignosi and G. Pirillo, Repetitions in the Fibonacci inﬁnite word. RAIRO-Theor. Inf.
Appl. 26 (1992) 199–204.
[20] F. Mignosi, A. Restivo and S. Salemi, Periodicity and the golden ratio. Theoret. Comput.
Sci. 204 (1998) 153–167.
[21] M. Morse, Recurrent geodesics on a surface of negative curvature. Trans. Amer. Math. Soc.
22 (1921) 84–100.
[22] M. Morse and G.A. Hedlund, Symbolic dynamics. Amer. J. Math. 60 (1938) 815–866.
[23] M. Morse and G.A. Hedlund, Symbolic dynamics II. Sturmian trajectories. Amer.J.Math.
62 (1940) 1–42.
[24] J. Moulin-Ollagnier, Proof of Dejean’s conjecture for alphabets with 5, 6, 7, 8, 9, 10 and 11
letters. Theoret. Comput. Sci. 95 (1992) 187–205.
[25] J.-J. Pansiot, `A propos d’une conjecture de F. Dejean sur les r´ep´etitions dans les mots.
Discrete Appl. Math. 7 (1984) 297–311.
[26] ´E. Prouhet, M´emoire sur quelques relations entre les puissances des nombres. C. R. Acad.
Sci. Paris S·er. I 33 (1851) 225.
[27] G. Rauzy, Suites `a termesdansun alphabet ﬁni, in Seminaire de th·eorie des nombres
1982–1983, Univ. Bordeaux I, 1983. Expos´e 25.
[28] A. Thue, ¨Uber unendliche Zeichenreihen. Norske Vid. Selsk. Skr., I. Mat. Nat. Kl.,
Christiana 7 (1906) 1–22.
[29] D. Vandeth, Sturmian words and words with a critical exponent. Theoret. Comput. Sci. 242
(2000) 283–300.

Received April 8, 2007. Accepted November 22, 2007.
