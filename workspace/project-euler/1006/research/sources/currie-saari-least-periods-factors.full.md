<!-- source: https://www.numdam.org/item/ITA_2009__43_1_165_0.pdf | converted from PDF -->

RAIRO-Theor. Inf. Appl. 43 (2009) 165–178 Available online at:

DOI: 10.1051/ita:2008006 www.rairo-ita.org

LEAST PERIODS OF FACTORS OF INFINITE WORDS ∗, ∗∗

James D. Currie 1 and Kalle Saari 2

Abstract. We show that any positive integer is the least period of a
factor of the Thue-Morse word. We also characterize the set of least
periods of factors of a Sturmian word. In particular, the corresponding
set for the Fibonacci word is the set of Fibonacci numbers. As a by-
product of our results, we give several new proofs and tightenings of
well-known properties of Sturmian words.

Mathematics Subject Classiﬁcation. 68R15.

1. Introduction

The combinatorial study of inﬁnite words often entails considering periods of
factors. For example, showing that an inﬁnite word has a bounded critical expo-
nent requires showing, perhaps implicitly, that the ratio between a factor and its
least period is bounded. Therefore it seems natural to study directly the set of
least periods of factors of an inﬁnite word; we call this set the period set of an
inﬁnite word. To our knowledge, this is a novel area of inquiry into the periodicity
of ﬁnite and inﬁnite words [11], Chapter 8.
This paper initiates the study of the period set of inﬁnite words. It is easy to
see that the period set of an inﬁnite word is ﬁnite if and only if the word is purely
periodic. Therefore inﬁnite aperiodic words give rise to inﬁnite period sets, and
it is natural to ask what kind of restrictions period sets have to obey. It is plain
that the period set of an aperiodic inﬁnite word must include periods 1, 2, and 3.
But already 4 is avoidable, as is witnessed by the Fibonacci word, see Corollary 4.

Keywords and phrases. Periodicity, Fibonacci word, Thue-Morse word, Sturmian word.

∗ Work of the ﬁrst author supported by a Discovery Grant from NSERC.
∗∗ Work of the second author supported by the Finnish Academy under grant 8206039.

1 Department of Mathematics & Statistics, University of Winnipeg, Winnipeg, R3B2E9,
Canada
2 Department of Mathematics and Turku Centre for Computer Science, University of Turku,
Turku, Finland; kasaar@utu.fi

Article published by EDP Sciences c∗ EDP Sciences 2008

166 J.D. CURRIE AND K. SAARI

In this paper we will characterize the period sets of the Thue-Morse word and of
all Sturmian words. These much studied words have applications and connections
to several ﬁelds, such as algebra, number theory, ergodic theory, crystallography,
computer graphics, and text algorithms; see [1]and [11], Chapter 2 and the refer-
ences therein. The characterizations of the period sets show that the gaps in the
period set of the Fibonacci word grow exponentially, while the gaps in the period
set of the Thue-Morse word have the lowest possible growth an aperiodic inﬁnite
word can have. As a by-product of our work, we give new proofs, tightenings, and
generalizations of some known properties of Sturmian words.
An outline of this paper is as follows: in Section 2, we set the terminology used
in the paper, and mention some basic results. In Section 3, we show that any
positive integer is the least period of some factor of the Thue-Morse word. In
Section 4, we characterize the set of least periods of a Sturmian word. Finally,
in Section 5, we give four applications of our results, including a tightening of a
result by de Luca and De Luca [7] and a characterization of the least periods of
standard words.
 2. Preliminaries

In this section we brieﬂy deﬁne the terminology used in this work. For a state-
ment without a citation in this section, we refer to [4,10,11].
We will be dealing with words over the alphabet {0, 1}. The set of all such
words, including the empty word, is denoted by {0, 1}∗.
Let w = a1a2 ··· an be a word with ai ∈{0, 1} and n ≥ 1. The length of w is
the integer n, and is denoted by |w|. We denote the number of occurrences of a
letter a ∈{0, 1} in w by |w|a.
A factor of w is a word of the form u = aiai+1 ··· ak with 1 ≤ i ≤ k ≤ n.It is
a preﬁx if i =1 and a suﬃx if k = n. In each case, we add the attribute proper if
w ̸= u.
Let 0 ≤ i< |w|.The word ai+1ai+2ai+3 ··· ana1a2 ··· ai is called a conjugate
of w, and is denoted by σi(w).
We write w∗ = a1a2 ··· an−1 and ∼w = a2a3 ··· an.The reverse of w is the
word anan−1 ··· a1, and we denote it by wR.We denote by w the word obtained
from w by exchanging 0’s and 1’s; it is called the complement of w.
A period of the word w is an integer p ≥ 1 such that, for all i =1, 2,... ,n − p,
we have ai = ai+p.The word w is said to be a rational power of the word
u = a1a2 ··· ap,and u is called a word period of w.If no period p divides the
length of w,then w is termed primitive. Primitivity of a word implies that all
conjugates of the word are distinct.
In this work, we are interested in the least period of a word w, which we denote
by p(w). The word w is called unbordered if p(w)= |w|. Finally, the preﬁx of w
of length p(w) is called the fractional root of w.
Let the words in {0, 1}∗ be ordered by the lexicographic order induced by the
relation 0 < 1. If w is a primitive word, then its least conjugate with respect to

LEAST PERIODS OF FACTORS OF INFINITE WORDS 167

the lexicographic order is called a Lyndon word.If |w| > 1, we get a diﬀerent
Lyndon word by using the lexicographic order induced by the relation 1 < 0. One
of the basic properties of a Lyndon word is that it is unbordered.
Let x be an inﬁnite word, that is, a mapping from the nonnegative integers to
a ﬁnite alphabet. The notion of a factor is extended naturally to inﬁnite words
with the agreement that a factor is always a ﬁnite word. The set of ﬁnite factors
of x is denoted by F (x). We call the set of least periods of all factors of x the
period set of x.
A morphism is a mapping h : {0, 1}∗ →{0, 1}∗ with the property that h(uv)=
h(u)h(v) for every u, v ∈{0, 1}∗. The domain of h extends to inﬁnite words such
that if x = a1a2 ··· an ··· , then h(x)= h(a1)h(a2) ··· h(an) ···
The Thue-Morse word, denoted by t, is the inﬁnite word starting with the letter 0
that is a ﬁxed point of the morphism μ : {0, 1}∗ →{0, 1}∗ determined by μ :0 ↦→
01, 1 ↦→ 10. If u is afactorof t,thenso are u and uR. The Thue-Morse word is
overlap-free, which means that t does not have a factor of the form uua,where u
is a nonempty word and a is the ﬁrst letter of u.
A Sturmian word is an inﬁnite word x over {0, 1} such that, for every integer
n ≥ 1, the word x has precisely n + 1 diﬀerent factors of length n. The frequency
of letters 0and 1in x exists; the frequency of 1 is called the slope of x,and we
denote it by θ.The slope θ is an irrational number, and therefore it has an inﬁnite
continued fraction expansion

θ =[ 0,d1 +1,d2,d3,... ], (1)

where d1 ≥ 0and dn ≥ 1for n ≥ 2.
Next we deﬁne words sn corresponding to the expansion (1) as follows:

s−1 =1,s0 =0,sn = sdn
n−1sn−2 (n ≥ 1).

Words that can be recursively deﬁned as above are called standard. All standard
words are primitive. Furthermore, consecutive standard words sn−1 and sn are
near-commutative in the following sense: if n ≥ 1, then there exists a word pn
such that snsn−1 = pna¯a and sn−1sn = pn¯aa, (2)
where a ∈{0, 1}. Therefore, for n ≥ 2, we have

sns∗∗
n−1 = sn−1s∗∗
n. (3)

Let us denote qn = |sn| for all n ≥−1.
The standard words corresponding to the slope θ are related to x in the following
way. Since sn is a preﬁx of sn+1 for all n ≥ 1, there is a unique inﬁnite word,
which we denote by c, such that sn is a preﬁx of c for all n ≥ 1. The word c is
called the characteristic word with slope θ. The sets of ﬁnite factors of x and c
coincide, that is, we have F (c)= F (x).

168 J.D. CURRIE AND K. SAARI

Since x has n + 1 factors of length n, it follows that there exist precisely one
factor u of length n such that both 0u and 1u are factors of x. Such a factor is
called left special. A factor of x is left special if and only if it is a preﬁx of c.
The set of factors of x is closed under reversal, that is to say, if u ∈ F (x), then
also uR ∈ F (x).
Now we will adopt a notation from [13]. For each integer n ≥ 1, there exists a
unique representation

n = d1 + d2 + ··· + di−1 + j, 1 ≤ j ≤ di.

With this representation, we denote

tn = sj
i−1si−2. (4)

It is also useful to denote t−1 =1 and t0 =0. Observe that td1+···+dn = sn for all
n ≥ 1.
The following result by Berstel [2] is one of the key observations we need in
characterizing the period set of a Sturmian word.

Theorem 1 (Berstel). For n ≥ 2, the longest preﬁx of c that is a rational power
of the word sn is sdn+1+1
n s∗∗
n−1.

3. Periods of factors of the Thue-Morse word

In this section we will show that every positive integer is the least period of
some factor of the Thue-Morse word. To do that, we need some auxiliary results.
Recall that μ denotes the morphism given by μ :0 ↦→ 01, 1 ↦→ 10.

Lemma 1. Let u be a factor of the Thue-Morse word t.Then u does not have
any odd period p such that p< |u|− 3.

Proof. Suppose that u has an odd period p with p< |u|− 3. We may suppose that
p ≥ 3 because t does not contain 000 or 111. Then |u|≥ 7. Let v be the preﬁx of
u of (odd) length p +4.
Observe that, since v is a factor of t,also vR and v are factors of t. Therefore,
without loss of generality, replacing v by its reversal or complement or both if
necessary, write v = μ(w)a = v0v1v2 ··· vp+3,where vi, a ∈{0, 1},and v0 =0.
Since v has period p, we ﬁnd that vp = v0 =0, so that vp−1vp = 10. Similarly,
vp+1 = v1 =1, so that vp+1vp+2 = 10. Thus v2 = vp+2 = 0, whence v2v3 = 01.
This implies that vp+3 = v3 =1, and v contains the overlap vp−1vpvp+1vp+2vp+3 =
10101, which is impossible because t is overlap-free. □

Recall that we denote by ∼u, u∗ and ∼u∗ the words obtained from u by deleting
respectively the ﬁrst letter, the last letter, or the ﬁrst and last letters.

Lemma 2. Let u = μ(w),some w ∈{0, 1}+.Let v =∼u∗. Suppose that v has an
even period 2r< |v|.Then w has period r.

LEAST PERIODS OF FACTORS OF INFINITE WORDS 169

Proof. Write w = w0w1w2 ··· ws−1ws and v = v0v1v2 ··· v2s−1,so that r< s.We
see that v = w0w1w1w2w2 ··· ws−1ws−1ws.
Since v has period 2r,wehave wi = v2i = v2i+2r = wi+r whenever 0 ≤ 2i +2r ≤
|v|− 2, that is, 0 ≤ i ≤ s − 1 − r. Therefore,

wi = wi+r for all 0 ≤ i ≤ s − 1 − r.

Similarly, since v has period 2r,we have wi = v2i−1 = v2i−1+2r = wi+r whenever
0 ≤ 2i − 1+2r ≤|v|− 1, that is, 1 ≤ i ≤ s − r. In total,

wi = wi+r for all 0 ≤ i ≤ s − r. □

The claim in the lemma above does not hold if we allow |v| =2r. Indeed, if
w = 01, then v = 11. Even though 2 is plainly a period of v,the word w certainly
does not have period 1.

Corollary 1. Let u = μ(w),some w ∈{0, 1}+.Let v be obtained from u by
possibly deleting ﬁrst or last or both letters; that is, let v be one of u, u∗, ∼u, ∼u∗.
Then v has period 2r< |u|− 2 if and only if w has period r.

Proof. Suppose that v has period 2r.Then ∼u∗ is a factor of v and has period 2r,
so that, by Lemma 2, w has period r.
If w has period r,then μ(w)has period 2r since |μ(0)| = |μ(1)| = 2. It follows
that the factor v of μ(w)has period 2r. □

Lemma 3. Let r ≥ 4 be a positive integer. Then the following statements hold:
(i) if r ≡ 4(mod 6),then t has a factor u of the form u =00y11 with |u| = r
and p(u)= r;
(ii) if r ≡ 0, 2, 3,or 5(mod 6),then t has a factor u of the form u =00y101
with |u| = r and p(u)= r;
(iii) if r ≡ 0, 1,or 3(mod 6),then t has a factor u of the form u =00y010
with |u| = r +1 and p(u)= r.

Proof. We prove this by induction. The item (i) with r = 4 is witnessed by the
factor 0011. The item (ii) with r =5, 6, 8, or 9 is witnessed by factors

00101, 001101, 00101101, and 001100101.

The item (iii) with r =6, 7, 9 is witnessed by factors

0011010, 00110010, and 0011010010.

Let us now assume that r ≥ 10, and that the lemma is satisﬁed for all smaller
values of r.

Case 1. r ≡ 0 (mod 6). First, let s = r/2. Then either s ≡ 0, or 3 (mod 6), and
s<r. By the minimality of r and the item (iii), there is a factor w of t of the form

170 J.D. CURRIE AND K. SAARI

00z010 having length s +1 and least period s.Let u =∼μ(wR). Then u is a factor
of t,itis oflength r + 1, and it has the form u =00y010, where y = 110μ(zR)1.
Evidently, u has period r. Corollary 1 implies that u has no even period shorter
than r =2s.Writing u = u0u1u2 ··· ur,wesee that u0 ̸= ur−1, u2 ̸= ur, u3 ̸= ur,
showing that u does not have period r − 1, r − 2, or r − 3. By Lemma 1, u can have
no odd period, and therefore the least period of u is r, witnessing the item (iii).
Next, let v =∼μ(wR)
∗.Then v is of length r, and thus has period r.Further-
more, v =∼μ(101zR11)
∗ has the form 00y101, where y = 110μ(zR). It has no even
period shorter than r =2s by Corollary 1.Writing v = v0v1v2 ··· vr−1,we see
that v0 ̸= vr−1, v1 ̸= vr−1, v0 ̸= vr−3, showing that v does not have period r − 1,
r − 2, or r − 3. By Lemma 1, v can have no odd period. Thus the least period of
v is r, witnessing the item (ii).

Case 2. r ≡ 3 (mod 6). First, let s =(r +3)/2. Then either s ≡ 0, or 3 (mod 6),
and s<r.Thus there is a factor w of t of the form 00z101 having length s and
least period s.Let u =∼μ(wR)
∗.Then u is a factor of t,it is of length r +1, and
it is of the form u =00y010, where y = 110μ(zR).
Evidently, the word u has period r. Corollary 1 implies that it has no even
period strictly shorter than |u| = r +1 = 2s − 2. Writing u = u0u1u2 ··· ur,we see
that u0 ̸= ur−1, u1 ̸= ur−1, u3 ̸= ur, showing that u does not have period r − 1,
r − 2, or r − 3. By Lemma 1, u can have no odd period less than r.Thus the least
period of u is r, witnessing the item (iii).
Next, let s =(r +1)/2. Then either s ≡ 2, or 5 (mod 6). There is a factor
v of t of the form 00z101 having length s and least period s.Let u =∼μ(vR).
Then u is a factor of t,it is of length r, and it has the form u =00y101, where
y = 110μ(zR)0.
Evidently, the word u has period |u| = r. Corollary 1 implies that it has no
even period strictly shorter than r +1 = 2s.Writing u = u0u1u2 ...ur−1,we see
that u0 ̸= ur−1, u1 ̸= ur−1, u0 ̸= ur−3, showing that u does not have period r − 1,
r − 2, or r − 3. By Lemma 1, u can have no odd period less than r.Thus the least
period of u is r, witnessing the item (ii).

Case 3. r ≡ 1(mod 6). Let s =(r +3)/2. Then either s ≡ 2, or 5 (mod 6),
and s<r.Thus there is a factor v of t of the form 00z101 having length s and
least period s.Let u =∼μ(vR)
∗. As in the previous case, u is a factor of t,it is
of length r + 1, has the form u =00y010, and its least period equals r = |u|− 1,
witnessing the item (iii).

Case 4. r ≡ 4(mod 6). Let s = r/2. Then either s ≡ 2, or 5 (mod 6). There
is a factor v of t of the form 00z101 having length s and least period s.The
word v =00z101 must be obtained by deleting the ﬁrst and possibly last letter
of some word μ(t), where t is some factor of t.Let u denote a word of the form
u = 1001x101 that is obtained from μ(t) by possibly deleting the last letter.
Next we will show that u has no evenperiodless than s. To derive a contra-
diction, suppose that u has period 2k< s. Then by Corollary 1,the word t has
period k. But then, again by Corollary 1,the word v has a period 2k< s,a
contradiction.
 LEAST PERIODS OF FACTORS OF INFINITE WORDS 171

Writing u = u0u1 ··· us,we see that u1 ̸= us, u2 ̸= us, u1 ̸= us−2,so that u
does not have period s − 1, s − 2, or s − 3. Therefore u has no odd period less
than s, and it follows that its least period is s.
We now let w =∼μ(u)
∗ =00y11, where y = 10110μ(x)100. Then w is of
length r. The same argument used before shows that w hasno evenperiodless
than r.Writing w = w0w1 ··· wr−1,we see that w0 ̸= wr−1, w0 ̸= wr−2, w1 ̸=
wr−2,and so w has no odd period less than r either. Therefore the least period
of w is r, witnessing the item (i), as desired.

Case 5. r ≡ 2(mod 6). Let s = r/2. Then we have two possibilities.
If s ≡ 1 (mod 6), then t has a factor w =00z010 of length s + 1, minimum
period s.Let v =∼μ(wR)
∗.Then v has form 00y101 with length r and least
period r, as can be seen as above.
If s ≡ 4 (mod 6), then t has a factor of the form 00z11 having length s and
least period s. It follows that u = 100z11 is a factor of t having length s +1 and
its least period is s.Let w =∼μ(u)
∗.Then w =00y101, where y = 101μ(z). As
in previous cases, the word w is of length r, and its least period is r, witnessing
the item (ii).

Case 6. r ≡ 5(mod 6). Let s =(r +1)/2. Then either s ≡ 0, or 3 (mod 6),
and s< r. Therefore, t has a factor of the form v =00z101 having length s
and least period s. It follows that u =∼μ(vR) has the form u =00y101 where
y = 110μ(zR)0. As in previous cases, u is of the length r,and theleast period of
u is r, witnessing the item (ii). □

Remark 1. The previous lemma shows that the Thue-Morse word has an unbor-
dered factor for each length r ̸≡ 1 (mod 6). It is readily veriﬁed that all factors
of length 7 are bordered. Since the factors of length 1 are trivially unbordered,
it is natural to ask, for which lengths r ≡ 1 (mod 6) are all factors of length r
bordered. This question remains open.

We are ready for the main theorem of this section.

Theorem 2. For each integer n ≥ 1, the Thue-Morse word has a factor of least
period n.

Proof. The least periods 1,2,3 are displayed by factors 0, 01, and 001. For integers
n ≥ 4, appropriate factors exist according to Lemma 3. □

4. Periods of factors of Sturmian words

In this section we will characterize the period sets of all Sturmian words, and
by doing so, we obtain a few older results on Sturmian words as a by-product in
the next section.
Let x be a Sturmian word with slope θ. Denote the continuedfractionexpansion
of θ by θ =[ 0,d1 +1,d2,d3,... ]. (5)

172 J.D. CURRIE AND K. SAARI

Let (sn)n≥−1 be the corresponding sequence of standard words, and let (tm)m≥−1
denote the corresponding auxiliary words deﬁned in (4). Further, let c denote the
characteristic sequence with slope θ.Observe that d1 ≥ 0and dn ≥ 1 for all n ≥ 2.
Since the period set of a sequence does not depend on the naming of letters, we
may assume that c begins with 0. Therefore, we assume in the rest of this section
that d1 ≥ 1.

Lemma 4. For n ≥ 0,the word s2
n is a factor of x.For m ≥ d1,the word t2
m is
afactor of x.

Proof. The word sdn+2
n+1 snsn+1 is a preﬁx of sn+3, and therefore a factor of x.Since
n ≥ 0(and d1 ≥ 1), the word sn is a preﬁx of sn+1.Consequently, s2
n is a factor
of x.
If m = d1,then t2
m = s2
1 occurs in x. So, we may suppose that m>d1.Then
we have tm = si
nsn−1 for some integers n ≥ 1and 1 ≤ i ≤ dn+1.Since s2
n+1 occurs
in x, we see that the word si
nsn−1sdn+1
n sn−1 occurs in x.Since n ≥ 1, the word
sn−1 is a preﬁx of sn, and hence it follows that the square of the word tm = si
nsn−1
occurs in x. □

Corollary 2. For m ≥−1, all conjugates of tm are factors of x.

Proof. The claim is trivial if m equals −1or0. When1 ≤ m< d1,the claim is
witnessed by s2
1 =0d110d11. When m ≥ d1,the word t2
m occurs in x,and so the
claim obviously holds then as well. □

The words tm clearly are standard, and hence primitive. Therefore all the
conjugates of tm are distinct. Since all conjugates of tm are factors of x,and x
has |tm| + 1 factors of length |tm|, it follows that x has precisely one factor of
length |tm| that is not a conjugate of tm. We call this factor the singular factor
of x corresponding to tm1. With this deﬁnition, t−1 = 1 is the singular factor
corresponding to t0 = 0, and vice versa. We give the other singular factors in the
next lemma.

Lemma 5. Let m ≥ 1,and let a denote the last letter of tm = si
nsn−1.The
singular factor corresponding to tm equals at
∗
m, and it is bordered with period qn.

Proof. First, observe that n ≥ 0and 1 ≤ i ≤ dn+1. It is clear that sn+2sn+1 is a
preﬁx of c, and hence a factor of x.Since

sn+2sn+1 = sdn+2
n+1 sdn+1+1
n sn−1, (6)

we see that the word si+1
n sn−1 is a factor of x.
First, suppose that n = 0. Then the word 0i+1 occurs in x, and it clearly is the
singular factor corresponding to si
nsn−1 =0i1. The claim holds for 0i+1.

1Singular factors for Sturmian words seem to have been introduced by Cao and Wen [3], but
only in cases that correspond to the words sn.

LEAST PERIODS OF FACTORS OF INFINITE WORDS 173

Next, suppose that n =1. Then

si+1
1 s0 =0d11(
0d11)i0,

and hence the word 1(
0d11)i occurs in x, and it clearly is the singular factor
corresponding to si
1s0, satisfying the claim.
Finally, suppose that n ≥ 2. Let us denote sn = s∗∗
nab and sn−1 = s∗∗
n−1ba,where
ab ∈{01, 10}.Equation (6) shows that the word w = bsi
ns∗∗
n−1b is a factor of x.
Also, w is not a conjugate of si
nsn−1 because |w|b = |si
nsn−1|b + 1. Hence w is the
corresponding singular factor of tm.Since b = a,wehave w = at
∗
m.Furthermore,
the word w is bordered with period qn because

w = bsi
ns∗∗
n−1b = (
bs∗∗
na)ibs∗∗
n−1b,

and bs∗∗
n−1b is a preﬁx of bs∗∗
na. □

Lemma 6. Let n ≥ 0 and i ≥ 1.Denote wj = σj(si
nsn−1).Then wj has a period

{ qn if 0 ≤ j ≤ qn − 2;

(i − 1)qn + qn−1 if qn ≤ j ≤ iqn + qn−1 − 2.

Furthermore, wj is unbordered if and only if j = qn − 1 or j = iqn + qn−1 − 1,and
then wj is a Lyndon word.

Proof. The claim is readily veriﬁed for n = 0, so we may assume that n ≥ 1.
First, suppose that 0 ≤ j ≤ qn−2. Then wj is a factor of the word z = si
nsn−1s∗∗
n.
If n =1, then z clearly has a period qn.If n ≥ 2, then Equation (3) implies
z = si+1
n s∗∗
n−1, and we see that z has a period qn. Therefore also wj has a period qn.
Next, suppose that kqn ≤ j< (k +1)qn,where 1 ≤ k ≤ i − 1. This implies that
i ≥ 2. Then wj is a factor of the word

z = si−k
n sn−1sk
ns∗
n.

We claim that z is a preﬁx of the word (si−k
n sn−1sk−1
n )3. Indeed, if n =1,
verifying this is a straightforward computation. And if n ≥ 2, the claim follows by
an application of Equation (3). Hence z, and consequently also wj,has a period
(i − 1)qn + qn−1.
Finally, suppose that iqn ≤ j ≤ iqn + qn−1 − 2. This implies n ≥ 2. Then
the word wj is a factor of z = sn−1si
ns∗∗
n−1.By Equation (3), we can write
z = sn−1si−1
n sn−1s∗∗
n, and hence z,and also wj,have a period (i − 1)qn + qn−1.
Since si
nsn−1 is a primitive word over a two-letter alphabet, it has at least
two conjugates that are Lyndon words, and therefore unbordered. We have seen
that wj is bordered in all other cases except possibly when j = qn − 1and j =
iqn + qn−1 − 1, so that the last claim of the lemma holds. □

174 J.D. CURRIE AND K. SAARI

Lemma 7. Aword w is an unbordered factor of x if and only if w = t−1, w = t0,
or w is one of the two Lyndon words that are conjugates of tm for some m ≥ 1.

Proof. According to Lemmas 5 and 6, the claim holds if |w| = |tm| for some
m ≥−1. Hence we may suppose that |w| ̸= |tm| for all m ≥−1. We will show
that w is bordered.
First, observe that we have |w| > |td1 | = d1 + 1 because |ti| = i +1 for i =
0, 1,... ,d1. Furthermore, there exists an integer n ≥ 1 such that either

qn < |w| <qn + qn−1 or iqn + qn−1 < |w| < (i +1)qn + qn−1

for some 1 ≤ i< dn+1. It follows that w is a proper preﬁx of some factor of x of
length iqn + qn−1 with 1 ≤ i ≤ dn+1 such that

|w| > max{ qn, (i − 1)qn + qn−1 }. (7)

Denote this factor by z.Then z is either a conjugate of si
nsn−1, or the singular
factor corresponding to si
nsn−1.If z is the singular factor, then w is bordered
because z has a period qn and |w| >qn. Hence we may suppose that z is a
conjugate of tm = si
nsn−1.
If z is bordered, then according to Lemma 6, z has a period qn or a period
(i − 1)qn + qn−1.In either case, z has a period strictly less than |w|,and so w is
bordered.
If z is unbordered, Lemma 6 implies that either

z = σ−1(si
nsn−1)or z = σqn−1(si
nsn−1). (8)

Now we have two possibilities regarding as to whether n =1 or n ≥ 2.
Suppose ﬁrst that n = 1. Then either z =0(0d11)
i or z =(10d1)
i0. In the
ﬁrst case, the inequality in (7) implies that w =0(0d1)
i−10j for some j ≥ 1, so
that w is bordered. Similarly, in the second case we have w =(10d1)
i−110j,where
1 ≤ j ≤ d1.If i =1, the word w is a conjugate of tj, a contradiction. Therefore,
i ≥ 2, and w is bordered.
Suppose then that n ≥ 2. Now, the word w is a factor of either

σ−2(si
nsn−1)or σqn−2(si
nsn−1). (9)

Since we have already proved that w is bordered if w is a factor of a bordered word
of length iqn + qn−1, we only have to show that both words in (9) are bordered.
To do that, we only have to show that they are distinct from the words in (8).
There are four cases to consider; one of them is

σ−2(si
nsn−1)= σqn−1(si
nsn−1). (10)

Since si
nsn−1 is primitive, we get iqn + qn−1 − 2= qn − 1, which implies that n ≤ 1,
a contradiction. The remaining three cases are proved similarly; we omit details
here. □

LEAST PERIODS OF FACTORS OF INFINITE WORDS 175

The next result by de Luca and De Luca appears in the proof of [7], Theorem 10.
The original proof was obtained with a clever use of Duval extensions and a result
of Mignosi and Zamboni [12]. Here we give a diﬀerent, more constructive, albeit
longer, proof.

Lemma 8 (de Luca, De Luca). The least period of a factor w of x equals the
length of a longest unbordered factor of w.

Proof. Let u denote a longest unbordered factor of w. The claim clearly holds if
u is a letter, so we may assume that |u|≥ 2. Clearly, p(w) ≥|u|. To show that w
has a period |u|, it suﬃces to show that all factors of length |u| of w are conjugates
of u.
To do that, suppose, contrary to what we want to show, that w has a factor z
of length |u| that is not a conjugate of u. Since the reversal of w is also a factor of
x, wemay,possiblybyreplacing w by wR, assume that u occurs on the left of z
in w.Let v denote a preﬁx of w such that z is a suﬃx of v and u is a factor of v.
Since u is unbordered and |u|≥ 2, Lemma 7 implies that u is a conjugate of
tm = si
nsn−1 for some n ≥ 0and 1 ≤ i ≤ dn+1. Therefore, z is the singular factor
corresponding to si
nsn−1. Hence, if a denotes the last letter of sn−1, then it follows
from Lemma 5 that z = asi
ns∗
n−1.
Next, denote p = snsn+1 = sdn+1+1
n sn−1. Observe that, as a suﬃx of sn+2sn+1,
the word ap is a factor of x.
Let us denote the longest common suﬃx of ap and va by y.Since za is a suﬃx
of both p and va,it is a suﬃx of y, as well. By Lemma 6,the word

ap∗ = σ−1(sdn+1+1
n sn−1)

is unbordered. Since |ap∗| = |sdn+1+1
n sn−1| > |u|, it then follows that y is a proper
suﬃx of ap because otherwise ap∗ is a factor of w, contradicting the maximality
of |u|.
Since p, and hence also y,has a period qn,the word u cannot be a factor of y
because u is unbordered and |u| = iqn + qn−1.Consequently, y is also a proper
suﬃx of va. This implies that y is a left special factor of x, and as such, a preﬁx
of c.In particular, sn is a preﬁx of y. Now the primitivity of sn and the fact
that y is a suﬃx of p = sdn+1+1
n sn−1 imply that we have y = sj
nsn−1 for some
i +1 ≤ j ≤ dn+1 + 1 (for the left inequality, note that |y| > |u| = |si
nsn−1|.
We can rule out the possibility that j = dn+1 + 1 because the word sdn+1+1
n sn−1
is not a preﬁx of c. Indeed, this is straightforward to verify for n =0 and n =1,
and Theorem 1 handles the case when n ≥ 2.
Now, we see that ay is a suﬃx of p.Since y is a proper suﬃx of va,the
maximality of y implies that ay is a factor of va. Therefore ay∗ is a factor of v,and
hence of w.But ay∗ = asj
ns∗
n−1 is unbordered by Lemma 6,and |ay∗|≥ |za| > |u|,
contradicting the maximality of u. The proof is complete. □

The next result is the strongest result in this section, and it gives our desired
formula for the period set of x as a corollary.

176 J.D. CURRIE AND K. SAARI

Theorem 3. The fractional root of a factor of x is a conjugate of tm for some
m ≥−1.

Proof. Let w be a factor of x.If w is unbordered, then according to Lemma 7,
it is a conjugate of some tm,where m ≥−1. If w is bordered, Lemmas 8 and 7
imply that p(w)= |tm| for some m ≥ 0. Consequently, the fractional root of w
is either a conjugate of tm, or the singular factor at
∗
m,where a is the last letter
of tm. In the ﬁrst case the claim holds, so may suppose that at
∗
m is the fractional
root of w.
Since p(w) < |w|, it follows that t∗
ma is a factor of x. By the deﬁnition of
a singular factor, no other conjugates of at
∗
m except at
∗
m itself are factors of x.
Therefore, at
∗
m = t∗
ma. This implies that the fractional root of w is actually the
letter a, and the claim follows. □

Theorem 3 implies the following characterization of the period set of x.

Corollary 3. The period set of x is the set

{|tm| : m ≥−1 } = {1}∪ { iqn + qn−1 : n ≥ 0,i =1,... ,dn+1}.

The famous Fibonacci word is the characteristic sequence with slope 1/φ,where
φ =(1 + √
5)/2 denotes the golden ratio. As a special case of Corollary 3,we
obtain the next result, which was ﬁrst proved in [14].

Corollary 4. The least period of a factor of the Fibonacci word is a Fibonacci
number.
 5. Applications

In this section we give four applications of our results in the previous section.
The ﬁrst application by Harju and Nowotka [9] is a direct corollary of Lemma 7.

Corollary 5. Unbordered words that are factors of Sturmian words are Lyndon
words.

The next characterization of ﬁnite Sturmian words is by de Luca and De Luca [7],
Theorem 10.

Corollary 6. A ﬁnite word is a factor of a Sturmian word if and only if its
fractional root is a conjugate of a standard word.

Proof. Let a ﬁnite word w be a factor of a Sturmian word, say a factor of x using
the notation from the last section. Then by Theorem 3 the fractional root of w is
a conjugate of tm for some m ≥−1, and tm is a standard word.
Conversely, suppose w = uτ ,where u is a conjugate of a standard word, say sn,
and τ ≥ 1 is rational. Then w is a factor of sa+2
n ,where a = ⌊τ ⌋, which clearly is
a preﬁx of a characteristic word. □

LEAST PERIODS OF FACTORS OF INFINITE WORDS 177

Our last two corollaries below use a well-known theorem by Fine and Wilf [8],
which states that if two words x
n and ym have a common preﬁx of length |x| +
|y|− gcd(|x|, |y|), then both of them have a period gcd(|x|, |y|).
Here is one more application of Theorem 3, see also Damanik and Lenz [6].

Corollary 7. If a square uu is a factor of x and u is primitive, then u is a
conjugate of tm for some m ≥ 0.

Proof. Let v denote the fractional root of uu,which by Theorem 3 is a conjugate
of tm for some m ≥−1. The word 11 does not occur in x,so that m ≥ 0. Then
uu = vτ for some rational τ ≥ 2, and we have |u| + |v|≤ |uu|.By the theorem of
Fine and Wilf, uu has a period gcd(|u|, |v|). Since v is the fractional root of uu,
this implies that |v| =gcd(|u|, |v|), and hence |v| divides |u|.Since u is primitive,
it follows that u = v. □

Cummings et al. [5] gave two proofs showing that, for n ≥ 2, the least period
of the ﬁnite Fibonacci word fn is fn−12. As our last result of this chapter, we
generalize the result of Cummings et al. to standard words. Let us use the notation
from the previous section, that is, sn is a standard word and sn = sdn
n−1sn−2.

Corollary 8. If n ≥ 2, then the least period of sn equals qn−1.

Proof. Since sn = sdn
n−1sn−2 and sn−2 is a preﬁx of sn−1,we see that qn−1 is a
period of sn. Hence we only need to show that qn−1 is the least period. To do
that, suppose the contrary: we have p(sn) <qn−1.
First, suppose that dn ≥ 2. Since sn has periods qn−1 and p(sn), and

qn−1 + p(sn) < 2qn−1 <qn,

it follows from the theorem of Fine and Wilf that p(sn) is a proper divisor of qn−1.
Since sn−1 is a preﬁx of sn, this implies that sn−1 is not primitive, a contradiction.
Second, suppose that dn =1. If p(sn) ≤ qn−2, we derive a contradiction as
above. Therefore we may assume that p(sn) >qn−2.Now, Theorem 3 implies that
p(sn)= iqn−2 + qn−3 with 1 ≤ i< dn−1. Then the word si
n−2sn−3sn−2 is a preﬁx
of sn. But since sn−1 = sdn−1
n−2 sn−3 is also a preﬁx of sn,we obtain sn−3sn−2 =
sn−2sn−3, which is absurd by Equation (2). This contradiction completes the
proof. □

Acknowledgements. The second author is grateful to Alessandro De Luca for pointing
out the result stated in Lemma 8. A sincere thank you also to Gw·ena¤el Richomme
for pointing out a deﬁciency in the ﬁrst version of Lemma 2 and also for other useful
comments that helped to clarify the presentation. Finally, thank you to the referees for
their remarks.

2To be precise, Cummings et al. showed that the longest border of fn is fn−2, but these two
claims are equivalent.

178 J.D. CURRIE AND K. SAARI

References

[1] J.-P. Allouche and J. Shallit, The ubiquitous Prouhet-Thue-Morse sequence, in Sequences
and Their Applications: Proceedings of SETA’98. Springer Series in Discrete Mathemat-
ics and Theoretical Computer Science, C. Ding, T. Helleseth and H. Niederreiter, Eds.,
Springer-Verlag, London (1999) 1–16.
[2] J. Berstel, On the index of Sturmian words.In Jewels are forever. Springer, Berlin (1999)
287–294.
[3] W.-T. Cao and Z.-Y. Wen, Some properties of the factors of Sturmian sequences. Theor.
Comput. Sci. 304 (2003) 365–385.
[4] C. Choﬀrut and J. Karhum¨aki, Combinatorics on words. In A. Salomaa and G. Rozenberg,
Eds., Handbook of Formal Languages, volume 1. Springer, Berlin (1997) 329–438.
[5] L.J. Cummings, D.W. Moore and J. Karhum¨aki, Borders of Fibonacci strings. J. Comb.
Math. Comb. Comput. 20 (1996) 81–87.
[6] D. Damanik and D. Lenz, Powers in Sturmian sequences. Eur. J. Combin. 24 (2003) 377–
390.
[7] A. de Luca and A. De Luca, Some characterizations of ﬁnite Sturmian words. Theor. Com-
put. Sci. 356 (2006) 118–125.
[8] N.J. Fine and H.S. Wilf, Uniqueness theorems for periodic functions. Proc. Amer. Math.
Soc. 16 (1965) 109–114.
[9] T. Harju and D. Nowotka, Minimal Duval extensions. Int. J. Found. Comput. Sci. 15 (2004)
349–354.
[10] M. Lothaire, Combinatorics on Words. Cambridge University Press, Cambridge (1997).
[11] M. Lothaire, Algebraic Combinatorics on Words, Encyclopedia of Mathematics and its Ap-
plications,Vol. 90. Cambridge University Press, Cambridge (2002).
[12] F. Mignosi and L.Q. Zamboni, A note on a conjecture of Duval and Sturmian words. RAIRO-
Theor. Inf. Appl. 36 (2002) 1–3.
[13] M. Mohammad-Noori and J.D. Currie, Dejean’s conjecture and Sturmian words. Eur. J.
Combin. 28 (2007) 876–890.
[14] K. Saari, Periods of factors of the Fibonacci word.in Proceedings of the Sixth International
Conference on Words (WORDS’07). Institut de Math´ematiques de Luminy (2007) 273–279.

Communicated by J. Karhum¨aki.
Received November 28, 2007. Accepted February 6, 2008.
