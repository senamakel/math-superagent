<!-- source: https://arxiv.org/pdf/1404.4269 | converted from PDF -->

arXiv:1404.4269v1  [math.DS]  16 Apr 2014
Gap Sequence of Factors of Fibonacci Sequence
Huang Yuke
1,2 Wen Zhiying3,4

ABSTRACT

Let ω be a factor of Fibonacci sequence F∞ = x1x2 · · · , then it appears in the sequence inﬁnitely
many times. Let ωp be the p-th appearance of ω and νω,p be the gap between ωp and ωp+1.
In this paper, we discuss the structure of the gap sequence {νω,p}p≥1, we ﬁrst introduce the
singular kernel word sk(ω) for any factor ω of F∞ and give a decomposition of ω with respect to
sk(ω). Using the singular kernel and the decomposition, we prove the gap sequence {νω,p}p≥1
has exactly two diﬀerent elements {νω,1, νω,2} and determine the expressions of gaps completely,
then we prove that the gap sequence over the alphabet {νω,1, νω,2} is still a Fibonacci sequence.
Finally, we introduce the spectrum for studying some typical combinatorial, using the results
above, we determine completely the spectrums.

1. Introduction

Let A = {a, b} be a binary alphabet. Let A∗ be the set of ﬁnite words on A and AN be the
set of one-sided inﬁnite words. The elements of A∗ are called words or factors, which will be
denoted by ω. The neutral element of A∗ is called the empty word, which we denote by ε. For
a ﬁnite word ω = x1x2 · · · xn, the length of ω is equal to n and denoted by |ω|. We denote by
|ω|a (resp. |ω|b) the number of letters of a (resp. b) appearing in ω.
Factor property have been studied extensively, such as Lothaire[13, 14]. As a typical se-
quence over a binary alphabet, the Fibonacci sequence, having many remarkable properties,
appears in many aspects of mathematics and computer science, symbolic dynamics, theoretical
computer science etc., we refer to Allouche and Shallit[1]. Speciﬁcally, in combinatorial on
words, see Berstel[4, 5] for a survey.
As usual, let σ : A → A∗ be a morphism deﬁned by σ(a) = ab, σ(b) = a. As we know,
A∗ is the free monoid on A, so σ(ab) = σ(a)σ(b). We deﬁne the k-th iteration of σ by
σk(a) = σk−1(σ(a)), k ≥ 2 and we denote Fk = σk(a), by convention, we deﬁne σ0(a) = a and
σ0(b) = b. Then the Fibonacci sequence F∞ is deﬁned by

F∞ = lim
k→∞ Fk = abaababaabaababaababa · · · ,

for the details of the properties of the sequence, see[19].
Let fk be the k-th Fibonacci number, i.e., f−1 = 1, f0 = 1, f1 = 2, fk+1 = fk + fk−1 for
k ≥ 0. Obviously, |Fk| = fk.
For a ﬁnite word ω = x1x2 · · · xn, let 0 ≤ i ≤ n − 1, the word Ci(ω) := xi+1 · · · xnx1 · · · xi
is called the i-th conjugation of ω. If j ≥ n, 0 ≤ i ≤ n − 1 and i ≡ j(mod n), we deﬁne
Cj(ω) := Ci(ω).
Let τ = x1x2 · · · xm · · · be a sequence, for any i ≤ j, deﬁne τ [i, j] := xixi+1 · · · xj−1xj, the
factor of τ of length j − i + 1, starting from the i-th letter and ending to the j-th letter. By
convention, we note τ [i] := τ [i, i] = xi and τ [i, i − 1] := ε.
The notation ν ≺ ω means that the word ν is a factor of word ω.

1Department of Mathematical Sciences, Tsinghua University, Beijing, 100084, P. R. China.
2E-mail address: hyg03ster@163.com.
3Department of Mathematical Sciences, Tsinghua University, Beijing, 100084, P. R. China.
4E-mail address: wenzy@tsinghua.edu.cn(Corresponding author).

1

For each ﬁxed k ≥ 1, we always denote by α ∈ {a, b} the last letter of Fk. It’s easy to see
that when k is even then α = a and when k is odd then α = b. Since Fk+1 = FkFk−1, the last
letter of Fk and Fk+2j are coincident. Since F0 = a and F1 = ab, then last letter of Fk and
Fk+2j−1 are diﬀerent, which we denote by β ∈ {a, b}. That means α is the last letter of Fk+2j
and β is the last letter of Fk+2j−1, for each j = 1, 2, . . .. Throughout the paper, we always
suppose α and β are diﬀerent letter when they appear simultaneously.
Let ν = ν1ν2 · · · νn ∈ A∗, we denote by ν−1 := ν−1
n · · · ν−1
2 ν−1
1 , called the inverse word
of ν. Let ω = uν, then ω−1 = (uν)−1 = ν−1u−1. Furthermore, ων−1 = uνν−1 = u and
u−1ω = u−1uν = ν.
In 1994, Wen Zhi-Xiong and Wen Zhi-Ying[19] introduced two concepts called singular word
and singular decomposition. The singular word of order k, which we denote by sk = βFkα−1,
where ωα−1 = ω[1, |ω| − 1], i.e., delete the last letter of ω. Obviously, we must make sure the
last letter of ω is α before we use notation ωα−1 to express a factor.
The singular word will play an important role in this paper, for more details of singular
words and applications, see Cao and Wen[7], Tan and Wen[18], which generalized the singular
word to Sturmian sequences and Tribonacci sequence respectively. The singular word has some
applications in some aspects, such as Lyndon words[15, 16], palindromes[11], smooth words[6],
location of factors[8, 9], Pad´e approximation[12, 17], etc.

1.1 Some Deﬁnitions

Let ω be factor of F∞, we will introduce some deﬁnitions: factor sequence {ωp}p≥1, gap
word νω,p, gap sequence {νω,p}p≥1, and singular kernel sk(ω). Especially, when ω is sk, the
singular word of order k, the factor sequence {sk,p}p≥1, the gap word νsk,p and gap sequence
{νsk,p}p≥1.

Deﬁnition 1.1 (Factor sequence). Let ω be a factor of Fibonacci sequence, then it appears in
the sequence inﬁnitely many times, which we arrange by the sequence {ωp}p≥1, where ωp denote
the p-th appearance of ω. Especially, when ω = sk, the factor sequence is {sk,p}p≥1, where sk,p
is the p-th appearance of sk.

Remark. In this paper, we always use letter ”k” to express the ”order”, such as Fk = σk(a),
fk = |Fk|, sk = βFkα−1 etc, use letter ”p” to express ”the p-th appearance” of a word in
Fibonacci sequence, such as ωp, sk,p etc, use letter ”n” to express ”the length” of a factor, such
as |ω| = n.

Deﬁnition 1.2 (Gap). Let ωp = xi+1 · · · xi+n, ωp+1 = xj+1 · · · xj+n, the gap between ωp and
ωp+1, denoted by νω,p, is deﬁned by

νω,p =
 




ε when i + n = j, ωp and ωp+1 are adjacent;
xi+n+1 · · · xj when i + n < j, ωp and ωp+1 are separated;
(xj+1 · · · xi+n)−1 when i + n > j, ωp and ωp+1 are overlapped.

Especially, when ω = sk, the gap between sk,p and sk,p+1 denoted by νsk,p.
The set of gaps of factor ω is deﬁned as {νω,p| p ≥ 1}.

Remark. Intuitively when ωp and ωp+1 are overlapped, the overlapped part is the word
xj+1 · · · xi+n, we take its inverse word as the gap νω,p. By this way, it is clear to distinguish the
cases ”adjacent”, ”separated” and ”overlapped”.

Example. Let ω1 = aababaab, ω2 = baabaabab, then:

2

(1) νω1,1 = ε (adjacent) and νω1,2 = (aab)−1 (overlapped);
(2) νω2,1 = aaba (separated) and νω2,2 = b
−1 (overlapped).

Remark. A closed related concept of ”Gap” is ”Return Word” was introduced by F.Durand[10],
for characterizing a sequence over a ﬁnite alphabet to be substitutive, he proved that a sequence
is primitive substitutive if and only if the set of its return words is ﬁnite, which means, each
factor of this sequence has ﬁnite return words. In 2001, L.Vuillon[20] proved that an inﬁnite
word τ is a Sturmian sequence if and only if each non-empty factor ω ≺ τ has exactly two
distinct return words. Some other related researches(see also [2, 3]) were interested in the car-
dinality of the set of return words of ω and the consequent results, but didn’t concern about
the structures of the sequence derived by return words. Essentially gap words can be derived
from the return words which diﬀer from only one preﬁx ω, but since the terminology ”gap” will
be convenient and have some advantages for our discussions, we prefer adopt it.
In the present paper, we are interested in the structures of the gap words and the gap
sequence, i.e., we will determine the gap words for each factor ω (in general, the gaps associated
with ω are distinct for diﬀerent ω), and the structure of the sequence induced by the gap words,
we will prove that the sequence over a new alphabet is still a Fibonacci sequence. Moreover,
using the structure, we discuss some typical combinatoric properties of the factors.

Deﬁnition 1.3 (Gap sequence). Let νω,p be the gap between ωp and ωp+1, we call {νω,p}p≥1 the
gap sequence of the factor ω.

We will see below that the sequence νω,p consists of only two diﬀerent factors which we will
determine them explicitly, moreover the sequence is still a Fibonacci sequence over a binary
alphabet.

Now we are going to introduce ”singular kernel” (Deﬁnition 1.4) and give ”singular decom-
position” (Proposition 1.5) which will play an important role in our studies.

Deﬁnition 1.4 (Singular kernel). For each ω ≺ F∞, we denote the longest singular word sk in
ω by sk(ω), called the singular kernel of ω.

We also call ”singular kernel” as ”kernel” sometimes for short.

Example. sk(baabaa) = aabaa = s3, sk(aababa) = bab = s2.

Proposition 1.5 (Uniqueness of Singular Kernel and Singular Decomposition).
Assume that ω ≺ F∞ and ω ̸∈ {ε, ab, ba, aba}. Then
(1) ω has a unique singular kernel sk(ω), i.e., as a factor, sk(ω) appears in ω only once;
(2) ω has a unique singular decomposition by its singular as ω = µ1(ω) ∗ sk(ω) ∗ µ2(ω).

Proof. Notice that s−1 = b and s0 = a, so if ω ≺ F∞ with ω ̸= ε, ω contains a singular word.
When ω ̸∈ {ε, ab, ba, aba}, there is a singular word si ≺ ω with i ≥ 1. Since |sk| = fk, we
see that if i < j, i ̸= −1, j ̸= 0, |si| < |sj|. Thus, there is a singular word sk ≺ ω, such
that if sm ≺ ω is a singular words and m ̸= k, then |sm| < |sk|. By deﬁnition sk is a singular
kernel of ω. Suppose sk appears in ω twice, then by Proposition 1.7(2), either sksk+1sk or
sksk−1sk = sk+2 will be a factor of ω. In both cases, since |sk+1|, |sk+2| > |sk|, which contracts
the hypotheses of sk. So sk appears in ω only once, that is ω has a unique singular kernel sk.
From the discussion above, we get immediately the conclusion (2).

Remark. In this article, we only consider the factor which has a unique singular decomposition
by its singular kernel, i.e., ω ̸∈ {ε, ab, ba, aba}. When ω ∈ {ε, ab, ba, aba}, their gaps and gap
sequences are ready to determine.
 3

The decomposition of Proposition 1.5 will be essential in our research, we will determine
the decomposition for any factor, it is not evident to get the expressions of sk(ω), µ1(ω) and
µ2(ω) in general. To do this, let ω be a factor with |ω| = n, since we only know the length of
ω, we should ﬁrst determine all possible order of its singular kernel, secondly we should study
all possible factors neighbor to the kernel. By a carefully analysis, we can classify all factors of
F∞ into the following six set, called types. In each types, we have an explicit expression of the
decomposition.

Deﬁnition 1.6 (Types). The sets Ti,j, where i = 1, 2, j = 1, 2, 3 are deﬁned as follows:
T1.1:={ω ∈ F∞| |ω| = fk, sk(ω) = sk};
T1.2:={ω ∈ F∞| |ω| = fk, sk(ω) = sk−1};
T1.3:={ω ∈ F∞| |ω| = fk, sk(ω) = sk−2};
T2.1:={ω ∈ F∞| fk < |ω| < fk+1, sk(ω) = sk};
T2.2:={ω ∈ F∞| fk < |ω| < fk+1, sk(ω) = sk−1};
T2.3:={ω ∈ F∞| fk < |ω| < fk+1, sk(ω) = sk−2}.

In Lemma 4.1 we will prove these six types are pairwise disjoint and their union is all factors
of F∞ with length fk ≤ |ω| < fk+1.

1.2 Decompositions of F∞

Wen and Wen[19] gave two decompositions of F∞ as below, and the second one is called the
positively separate property of the singular words.

Proposition 1.7 (Wen and Wen[19]).

(1) F∞ =
 ∞∏

k=−1 sk = a︸︷︷︸
s−1 b︸︷︷︸
s0 aa︸︷︷︸
s1 bab︸︷︷︸
s2 aabaa︸ ︷︷ ︸
s3 babaabab︸ ︷︷ ︸
s4 aabaababaabaa︸ ︷︷ ︸
s5 ,

where sk = βFkα−1, the k-th singular word;

(2) F∞ =
 ( k−1∏

j=−1 sj
)
 sk,1νsk,1sk,2νsk,2 · · · sk,pνsk,p · · · , F or any k ≥ 0,

where the set of gaps {νsk,p, p ≥ 1} has only two elements sk+1 and sk−1. Furthermore, the gap
sequence {νsk,p}p≥1 is Fibonacci sequence over the alphabet {sk+1, sk−1}.

Example. In the decomposition 1.7(2), take s2 = bab. Then two distinct gaps of the word s2
are νs2,1 = s3 = aabaa and νs2,2 = s1 = aa.

F∞ =a|b|aa(bab) aabaa︸ ︷︷ ︸
A (bab) aa︸︷︷︸
B (bab) aabaa︸ ︷︷ ︸
A (bab) aabaa︸ ︷︷ ︸
A (bab) aa︸︷︷︸
B (bab) aabaa︸ ︷︷ ︸
A (bab)

aa︸︷︷︸
B (bab) aabaa︸ ︷︷ ︸
A (bab) aabaa︸ ︷︷ ︸
A (bab) aa︸︷︷︸
B (bab) aabaa︸ ︷︷ ︸
A (bab) aabaa︸ ︷︷ ︸
A (bab) aa︸︷︷︸
B · · · .

We see that the gap sequence {νs2,p}p≥1 = ABAABABAABAAB · · · is Fibonacci sequence
over the alphabet {A, B}.

The ﬁrst aim of this article is to extended the results for singular words to the general
words of the Fibonacci sequence, and discuss the structure of gap sequence {νω,p}p≥1. But
in the present case, we have no recurrence relation sk+2 = sksk−1sk only valid for singular
words. One of main ideas for overcoming the diﬃculty is to introduce the singular kernel and

4

establishes the relation among four diﬀerent sequences: {ωp}, {sk,p}, {νω,p} and {νsk,p}. We
also give the expressions of gaps between each ωp and ωp+1. Since diﬀerent factors has diﬀerent
gaps, we have no general expressions for them, by carefully observing, we are led to classify
some types of the factors by their characterization, and study respectively the gaps by these
types(see Deﬁnition 1.6).
The second aim of this article consists of studying some global combinatoric properties of
factors, that is, the property depends on the location of the factor. We will introduce the
spectrum {(ω, p)} of a property, that is, ω ≺ F∞, p ∈ N, s.t. ωp possess the property. The
spectrum {(ω, p)} describes two independent variables ω and p. Using the results above, we
determine completely the spectrum for some typical combinatoric properties.

1.3 Organization of the paper

The paper is organized as follows. In Section 2, we state the main results of the paper
and give some examples. Section 3 to Section 5 are devoted to the proofs of our main results.
In Section 6, we will deﬁne and determine the spectrums of some combinatorial properties of
factors.

2. Main Results And Examples

In this section, we state the main results of this paper and give some simple examples.
The main conclusions are Theorem 2.2 and 2.4 which characterize the structure of the gap
sequence: Theorem 2.2 show that there are exactly two distinct elements and they constitutes
still a Fibonacci sequence over a new alphabet; and Theorem 2.4, for any factor ω ∈ F∞, gives
explicitly the expressions for all gaps.

Proposition 1.5 (Uniqueness of Singular Kernel and Singular Decomposition).
Assume that ω ≺ F∞ and ω ̸∈ {ε, ab, ba, aba}. Then
(1) ω has a unique singular kernel sk(ω), i.e., as a factor, sk(ω) appears in ω only once;
(2) ω has a unique singular decomposition by its singular as ω = µ1(ω) ∗ sk(ω) ∗ µ2(ω).

Proposition 1.5 states a factor ω can be decomposed by its singular kernel, and two questions
arise naturally: (1) for any factor ω, determine explicitly its decomposition by singular kernel;
(2) the sequences {ωp}p≥0 and {sk,p}p≥0 describes the locations of these factors, what is the
relation between the singular kernel of sk(ωp) and the singular word sk,p? Theorem 2.3 answers
completely the ﬁrst question, and Theorem 2.1 answers the second question positively, it shows
that sk(ωp) = sk,p.

Theorem 2.1 (Decomposition of ωp and νω,p by sk(ω)).
Let ωp ≺ F∞ and sk(ωp) = sk. Both decompositions below are unique:
(1) ωp = µ1(ω) ∗ sk,p ∗ µ2(ω);
(2) νω,p = µ−1
2 (ω) ∗ νsk,p ∗ µ−1
1 (ω).

Using Theorem 2.1, we can prove Theorem 2.2. Furthermore, by Theorem 2.1, we know
the key to determine the expressions of gaps is to ﬁnd out the expressions of µ1, µ2 and sk(ω)
for each ω. Theorem 2.3 give us the expressions of them, where we divide the factors into six
types. The expressions of gaps are given in Theorem 2.4.

Theorem 2.2 (Gap and gap sequence).
(1) Any factor ω ≺ F∞ has exactly two distinct gaps νω,1 and νω,2;
(2) The gap sequence {νω,p}p≥1 is the Fibonacci sequence.

5

Remark. Theorem 2.2(1) has been proved by Vuillon[20], we will give another simple proof in
this case.

Example. The factor ω = abaa has exact two gaps νω,1 = b =: A, νω,2 = a
−1 =: B. Then the
sequence {νω,p}p≥1 = ABAABABA · · · is the Fibonacci sequence over the alphabet {A, B}.

F∞ =(abaa) b︸︷︷︸
A (aba (a)
︸︷︷︸
B baa) b︸︷︷︸
A (abaa) b︸︷︷︸
A (aba (a)
︸︷︷︸
B baa) b︸︷︷︸
A (aba (a)
︸︷︷︸
B baa) b︸︷︷︸
A

(abaa) b︸︷︷︸
A (aba (a)
︸︷︷︸
B baa) b︸︷︷︸
A (abaa) b︸︷︷︸
A (aba (a)
︸︷︷︸
B baa) · · ·

Given a factor ω, by Proposition 1.5, ω has a unique decomposition by its singular kernel
ω = µ1(ω)sk(ω)µ2(ω). For giving the explicitly expression of µ1(ω) and µ2(ω), we need to
divide all factors of F∞ in to six disjoined types T i, j(1 ≤ i ≤ 2, 1 ≤ j ≤ 3)(see Deﬁnition 1.6).

Theorem 2.3 (Decomposition of ω by sk(ω), more explicitly).

ω ∈ T1.1 ⇒ µ1(ω) = µ2(ω) = ε.

ω ∈ T1.2 ⇒
 {
µ1(ω) = sk−2[i − fk−1 + 2, fk−2],
µ2(ω) = sk−2[1, i − fk−1 + 1], fk−1 − 1 ≤ i ≤ fk − 1.

ω ∈ T1.3 ⇒
 {
µ1(ω) = sk−1[i + 2, fk−1],
µ2(ω) = sk−1[1, i + 1], 0 ≤ i ≤ fk−1 − 2.

ω ∈ T2.1 ⇒
 {
µ1(ω) = sk−1[fk−1 − i + 1, fk−1],
µ2(ω) = sk−1[1, n − fk − i], 0 ≤ i ≤ n − fk.

ω ∈ T2.2 ⇒
 {
µ1(ω) = sk[fk − i + 1, fk],
µ2(ω) = sk[1, n − fk−1 − i], 0 ≤ i ≤ n − fk−1.

ω ∈ T2.3 ⇒
 {
µ1(ω) = sk−1[fk+1 − n − i, fk−1],
µ2(ω) = sk−1[1, fk−1 − i − 1], 0 ≤ i ≤ fk+1 − n − 2.

Example.
(1) Take ω = babaabab, |ω| = 8, sk(ω) = babaabab = sk, so ω ∈T1.1, µ1 = µ2 = ε.
(2) Take ω = baabaaba, |ω| = 8, sk(ω) = aabaa = sk−1, so ω ∈T1.2, µ1 = s2[3, 3] = b and
µ2 = s2[1, 2] = ba. The position of ω in s4−2s4−1s4−2 is shown as bab|aabaa|bab.
(3) Take ω = baababaa, |ω| = 8, sk(ω) = bab = sk−2, so ω ∈T1.3, µ1 = s3[3, 5] = baa and
µ2 = s3[1, 2] = aa. The position of ω in a
−1s4−1s4−2s4−1a
−1 is shown as abaa|bab|aaba.
(4) Take ω = ababaabab, |ω| = 9, sk(ω) = babaabab = sk, so ω ∈T2.1, µ1 = s3[5, 5] = a and
µ2 = s3[1, 0] = ε. The position of ω in s4−1s4s4−1 is shown as aabaa|babaabab|aabaa.
(5) Take ω = abaabaaba, |ω| = 9, sk(ω) = aabaa = sk−1, so ω ∈T2.2, µ1 = s4[7, 8] = ab and
µ2 = s4[1, 2] = ba. The position of ω in s4s4−1s4 is shown as babaabab|aabaa|babaabab.
(6) Take ω = baababaab, |ω| = 9, sk(ω) = bab = sk−2, so ω ∈T2.3, µ1 = s3[3, 5] = baa and
µ2 = s3[1, 3] = aab. The position of ω in a
−1s4−1s4−2s4−1a
−1 is shown as abaa|bab|aaba.

6

Theorem 2.4 (Expressions of νω,1 and νω,2).

ω ∈ T1.1 ⇒
 {
νω,1 = sk+1, |νω,1| = fk+1 > 0,
νω,2 = sk−1, |νω,2| = fk−1 > 0.

ω ∈ T1.2 ⇒
 {
νω,1 = Ci−fk−1(Fk−1), |νω,1| = fk−1 > 0,
νω,2 = ε, |νω,2| = 0.

ω ∈ T1.3 ⇒
 {
νω,1 = ε, |νω,1| = 0,
ν−1
ω,2 = Ci(Fk−2), |νω,2| = −fk−2 < 0.

ω ∈ T2.1 ⇒
 {
νω,1 = sk+1[n − fk − i + 1, fk+1 − i], |νω,1| = fk+2 − n > 0,
νω,2 = sk−1[n − fk − i + 1, fk−1 − i], |νω,2| = fk+1 − n > 0.

ω ∈ T2.2 ⇒
 {
νω,1 = sk[n − fk−1 − i + 1, fk − i], |νω,1| = fk+1 − n > 0,
ν−1
ω,2 = Fk+1[fk − i, n − i − 1], |νω,2| = fk − n < 0.

ω ∈ T2.3 ⇒
 {
ν−1
ω,1 = sk−1[fk+1 − n − i, fk−1 − i − 1], |νω,1| = fk − n < 0,
ν−1
ω,2 = Fk[fk+1 − n − i − 1, fk − i − 2], |νω,2| = fk−1 − n < 0.

Example.
(1) Take ω = babaabab ∈T1.1, then n = 8, k = 4.

⇒
 {
νω,1 = s5 = aabaababaabaa, |νω,1| = f5 = 13 > 0,
νω,2 = s3 = aabaa, |νω,2| = f3 = 5 > 0.

(2) Take ω = baabaaba ∈T1.2, then n = 8, k = 4, i = 6.

⇒
 {
νω,1 = C1(F3) = baaba, |νω,1| = f3 = 5 > 0,
νω,2 = ε, |νω,2| = 0.

(3) Take ω = baababaa ∈T1.3, then n = 8, k = 4, i = 1.

⇒
 {
νω,1 = ε, |νω,1| = 0,
ν−1
ω,2 = C1(F2) = baa, |νω,2| = −f2 = −3 < 0.

(4) Take ω = ababaabab ∈T2.1, then n = 9, k = 4, i = 1.

⇒
 {
νω,1 = s5[1, 12] = aabaababaaba, |νω,1| = f6 − 9 = 12 > 0,
νω,2 = s3[1, 4] = aaba, |νω,2| = f5 − 9 = 4 > 0.

(5) Take ω = abaabaaba ∈T2.2, then n = 9, k = 4, i = 2.

⇒
 {
νω,1 = s4[3, 6] = baab, |νω,1| = f5 − 9 = 4 > 0,
ν−1
ω,2 = F5[6, 6] = a, |νω,2| = f4 − 9 = −1 < 0.

(6) Take ω = baababaab ∈T2.3, then n = 9, k = 4, i = 1.

⇒
 {
ν−1
ω,1 = s3[3, 3] = b, |νω,1| = f4 − 9 = −1 < 0,
ν−1
ω,2 = F4[2, 5] = baab, |νω,2| = f3 − 9 = −4 < 0.

3. Proofs of Theorem 2.1 and Theorem 2.2

7

In this section, we will prove Theorem 2.1 and Theorem 2.2.
Theorem 2.1 establishes the relations among four sequences below:
(1) Factor sequence {ωp}p≥1, ωp is the p-th appearance of ω;
(2) Factor sequence {sk,p}p≥1, sk is the singular kernel of ω;
(3) Gap sequence {νω,p}p≥1, νω,p is the gap between ωp and ωp+1;
(4) Gap sequence {νsk,p}p≥1, νsk,p is the gap between sk,p and sk,p+1.
As one of our main conclusion, Theorem 2.2 shows that there are exactly two distinct
elements and they constitutes still a Fibonacci sequence over a new alphabet.
We give some lemmas ﬁrst which are very useful in the studies.

Lemma 3.1. Let sk be the k-th singular word. Then:
(1) sk = βα−1sk−1sk−2 = sk−2sk−1α−1β;
(2) sk = sk−2sk−3sk−2.

Proof. (1) As we declared in Section 1, α is the last letter of Fk and Fk−2, β is the last letter
of Fk−1, β ̸= α. Since Fk = Fk−1Fk−2, we know βFkα−1 = βα−1αFk−1β−1βFk−2α−1. By the
deﬁnition of singular word, sk = βα−1sk−1sk−2, we thus get the ﬁrst equality in (1).
By induction, we can prove Fk = Fk−2Fk−1β−1α−1βα, so

βFkα−1 = βFk−2Fk−1β−1α−1βαα−1 = βFk−2α−1αFk−1β−1α−1β,

which yields that sk = sk−2sk−1α−1β, and concludes the second equality in (1).
(2) By (1), sk = βα−1sk−1sk−2 and sk−1 = αβ−1sk−2sk−3, so

sk = βα−1 ∗ αβ−1sk−2sk−3 ∗ sk−2 = sk−2sk−3sk−2.

Lemma 3.2. ∏k−1
j=−1 sj = α−1sk+1.

Proof. By induction. (1) When k = 0, ∏−1
j=−1 sj = s−1 = a and α−1s1 = a
−1aa = a, where α
is the last letter of Fk. When k = 1, ∏0
j=−1 sj = s−1s0 = ab and α−1s2 = b
−1bab = ab. The
proposition holds.
(2) Assume the conclusion holds for k − 1, ∏k−1
j=−1 sj = α−1sk+1, then:

k∏

j=−1 sj =
 ( k−1∏

j=−1 sj
)
 sk = α−1sk+1sk = α−1αFk+1β−1βFkα−1

=Fk+1Fkα−1 = Fk+2α−1 = β−1sk+2,

where α is the last letter of Fk, β is the last letter of Fk±1. Thus the conclusion holds for k,
and we prove the proposition.

Remark. As a simple corollary of Lemma 3.2, we have ∑k−1
j=−1 fj = fk+1 − 1.

Lemma 3.3. For any ω ﬁxed, let sk(ω) = sk, then sk(ωp) = sk,p, i.e., the singular kernel of
ωp is equal to sk,p by location.

Proof. We will prove the following claims:
Claim (1): For any p, there exists q, such that sk(ωp) = sk,q;
Claim (2): For any q, there exists p, such that sk(ωp) = sk,q;
Claim (3): If both sk,q1 and sk,q2 are singular kernel of ωp, then q1 = q2;
Claim (4): If both sk(ωp1) and sk(ωp2) are sk,q, then p1 = p2.

8

Since sk ≺ ω, Claim (1) is trivial. By Proposition 1.5, each ω has a unique decomposition
by its singular kernel, so both Claim (3) and (4) are true. It rest to prove Claim (2).
Proof of Claim (2).
Using the positively separate property of the singular word sk and Lemma 3.2, we get

F∞ = α−1sk+1sksk+1sksk−1sksk+1sksk+1sksk−1sk · · ·

So for any q, the singular words neighboring to sk,q have only ﬁve possible cases below. We use
’underline’ to emphasize the singular word sk,q we consider.
Case 1: · · · sksk+1sk,qsk−1sk · · ·
Case 2: · · · sksk+1sk,qsk+1sk · · ·
Case 3: · · · sksk−1sk,qsk+1sk · · ·
Case 4: · · · sksk−1sk,qsk−1sk · · ·
Case 5: when q = 1, α−1sk+1sk,1sk+1sk · · ·
We want to prove: there is a ωp such that ωp ≻ sk,q and sk(ωp) = sk,q in each case. Since
sk(ω) = sk, by Proposition 1.5, we only need to ﬁnd two constant words µ1 and µ2 such that
ω = µ1skµ2 in all cases.
In case 1, since sk(ω) = sk, ω must be factor of α−1sk+1sksk−1skβ−1, i.e., α−1sk+1sksk+1α−1

with kernel sk. Otherwise, ω contains sk+1 or sksk−1sk = sk+2, then sk(ω) = sk+1 or sk+2, which
contradict sk(ω) = sk. Similarly, in case 2, 3, 4, 5, ω must be the factor of α−1sk+1sksk+1α−1

with kernel sk too. So, in all cases, µ1 is the suﬃx of α−1sk+1 and µ2 is the preﬁx of sk+1α−1.
Both of them are constant words throughout the ﬁve cases.

By the proof of Lemma 3.3 and Proposition 1.5, we have the corollary below.

Corollary 3.4. Let sk be the singular word of order k, θk := α−1sk+1sksk+1α−1.
(1) sk(θk) = sk;
(2) If τ ≺ θk with sk(τ ) = sk, then τ appears in θk only once;
(3) Let ω be a factor with singular kernel sk, then ω ≺ θk, i.e.,

{ω ≺ F∞| sk(ω) = sk} = {ω ≺ F∞| ω ≺ θk, sk(ω) = sk}.

Theorem 2.1(Decomposition of ωp and νω,p by sk(ω)).
Let ωp ≺ F∞ and sk(ω) = sk. Both decompositions below are unique:
(1) ωp = µ1(ω) ∗ sk,p ∗ µ2(ω);
(2) νω,p = µ−1
2 (ω) ∗ νsk,p ∗ µ−1
1 (ω).

Proof. The proof of the proposition will be easy by the following diagram.
Fig. 3.1: The relation among {ωp}, {sk,p}, {νω,p} and {νsk,p}.

Theorem 2.2(Gap and gap sequence).
(1) Any factor ω ≺ F∞ has exactly two distinct gaps νω,1 and νω,2;
(2) The gap sequence {νω,p}p≥1 is the Fibonacci sequence.

Proof. (1) Since νω,p = µ−1
2 (ω) ∗ νsk,p ∗ µ−1
1 (ω) and {{νsk,p}p≥1} = {νsk,1, νsk,2}, so {{νω,p}p≥1} =
{µ−1
2 (ω) ∗ νsk,1 ∗ µ−1
1 (ω), µ−1
2 (ω) ∗ νsk,2 ∗ µ−1
1 (ω)} =: {νω,1, νω,2}. That means, any factor ω has
exactly two distinct gaps νω,1 and νω,2.
(2) Since νω,p = µ−1
2 (ω) ∗ νsk,p ∗ µ−1
1 (ω) and the gap sequence {νsk,p}p≥1 is the Fibonacci
sequence (see Proposition 1.7(2)), the gap sequence {νω,p}p≥1 = {µ−1
2 (ω) ∗ νsk,p ∗ µ−1
1 (ω)}p≥1 is
the Fibonacci sequence.
 9

4. Proof of Theorem 2.3

By Proposition 1.5, we know that each ω ≺ F∞ has a unique decomposition by its singular
kernel: ω = µ1(ω) ∗ sk(ω) ∗ µ2(ω). We are going to prove Theorem 2.3. which determines the
expressions of sk(ω), µ1(ω) and µ2(ω) for each ω. To solve this problem, we divide the factors
into six types in Deﬁnition 1.6. Lemma 4.1 give the relations among these six types, where the
notation ”⊔” means pairwise disjoint union.

Lemma 4.1. The six types are pairwise disjoint and their union is all factors of F∞, i.e.,
(1) {ω ∈ F∞| ∃ k, s.t. |ω| = fk} = T1.1 ⊔ T1.2 ⊔ T1.3;
(2) {ω ∈ F∞| ∃ k, s.t. fk < |ω| < fk+1} = T2.1 ⊔ T2.2 ⊔ T2.3.

Proof. (1) Since |sk(ω)| ≤ |ω|, sk(ω) can not be singular word sj with j > k. So sk(ω) can
only be sj with j ≤ k. On the other hand, assume sk(ω) = sk−3, then by Corollary 3.4(3),
ω ≺ β−1sk−2sk−3sk−2β−1 with kernel sk−3 . But

|β−1sk−2sk−3sk−2β−1| = 2 ∗ fk−2 + fk−3 − 2 = fk − 2 < fk = |ω|,

so sk(ω) can not be singular word sk−3. By an analogous argument, sk(ω) can not take singular
word sj for −1 ≤ j ≤ k − 4 too. That is, sk(ω) has only three possible cases: sk, sk−1, sk−2,
and by the deﬁnitions of T1.1, T1.2 and T1.3, we get

{ω ∈ F∞| |ω| = fk} = T1.1 ∪ T1.2 ∪ T1.3.

Furthermore by Proposition 1.5(1), ω has a unique singular kernel, so T1.1, T1.2 and T1.3 are
pairwise disjoint.
(2) Since |ω| < fk+1 and |sk(ω)| ≤ |ω|, sk(ω) can not be singular word sj for j > k. As well
as the discussion in the case (1), sk(ω) can not take singular word sj(−1 ≤ j ≤ k − 3), and
may take only three cases: sk, sk−1, sk−2. That is,

{ω ∈ F∞| |ω| = fk} = T2.1 ∪ T2.2 ∪ T2.3.

Moreover, from Proposition 1.5(1), ω has a unique singular word, so T2.1, T2.2 and T2.3 are
pairwise disjoint.

Theorem 2.3 (Decomposition of ω by sk(ω)).

ω ∈ T1.1 ⇒ µ1(ω) = µ2(ω) = ε.

ω ∈ T1.2 ⇒
 {
µ1(ω) = sk−2[i − fk−1 + 2, fk−2],
µ2(ω) = sk−2[1, i − fk−1 + 1], fk−1 − 1 ≤ i ≤ fk − 1.

ω ∈ T1.3 ⇒
 {
µ1(ω) = sk−1[i + 2, fk−1],
µ2(ω) = sk−1[1, i + 1], 0 ≤ i ≤ fk−1 − 2.

ω ∈ T2.1 ⇒
 {
µ1(ω) = sk−1[fk−1 − i + 1, fk−1],
µ2(ω) = sk−1[1, n − fk − i], 0 ≤ i ≤ n − fk.

ω ∈ T2.2 ⇒
 {
µ1(ω) = sk[fk − i + 1, fk],
µ2(ω) = sk[1, n − fk−1 − i], 0 ≤ i ≤ n − fk−1.

ω ∈ T2.3 ⇒
 {
µ1(ω) = sk−1[fk+1 − n − i, fk−1],
µ2(ω) = sk−1[1, fk−1 − i − 1], 0 ≤ i ≤ fk+1 − n − 2.

10

Proof. (1) If ω ∈T1.1, then |ω| = fk and sk(ω) = sk. Notice that |sk| = fk, we get |µ1| =
|µ2| = 0, i.e., µ1(ω) = µ2(ω) = ε. We have therefore in this case, ω = sk.
(2) If ω ∈T1.2, then |ω| = fk and sk(ω) = sk−1. By Corollary 3.4, ω ≺ β−1sksk−1skβ−1,
and by Lemma 3.1(2),

β−1sksk−1skβ−1 = β−1sk−2sk−3sk−2sk−1sk−2sk−3sk−2β−1.

Since |sk(ω)| = fk−1, |µ1| + |µ2| = fk − fk−1 = fk−2, which means µ1 is suﬃx of sk−2 and
µ2 is preﬁx of sk−2. So ω ≺ sk−2sk−1sk−2. We get therefore, µ1 = sk−2[i − fk−1 + 2, fk−2],
µ2 = sk−2[1, i − fk−1 + 1] and ω = sk−2[i − fk−1 + 2, fk−2]sk−1sk−2[1, i − fk−1 + 1], where
fk−1 − 1 ≤ i ≤ fk − 1.
(3) If ω ∈T1.3, then |ω| = fk and sk(ω) = sk−2. By corollary 3.4, ω ≺ α−1sk−1sk−2sk−1α−1.
In this case, µ1 = sk−1[i + 2, fk−1], µ2 = sk−1[1, i + 1] and ω = sk−1[i + 2, fk−1]sk−2sk−1[1, i + 1],
where 0 ≤ i ≤ fk−1 − 2.
(4) The conclusion for ω ∈T2.1 can be obtained by the same argument as in (2). The
conclusions for ω being in T2.2 or T2.3 can be obtained by the same argument as in (3).

Remark. By Theorem 2.3 and Corollary 3.4(2) the cardinality of each type are:
♯T1.1= 1, ♯T1.2= fk−2 + 1, ♯T1.3= fk−1 − 1;
♯T2.1= n − fk + 1, ♯T2.2= n − fk−1 + 1, ♯T2.3= fk+1 − n − 1.
Let ρ(n) is the complexity function of Fibonacci sequence which is deﬁned by the cardinality
of the set of the factors with length n, then above formulas give immediately the known result
ρ(n) = n + 1.

Corollary 4.2.
(1) ω ∈T1.2⇔ ω = Ci(Fk), where fk−1 − 1 ≤ i ≤ fk − 1.
(2) ω ∈T1.3⇔ ω = Ci(Fk), where 0 ≤ i ≤ fk−1 − 2.

Proof. (1) By Theorem 2.3, ω ∈ T1.2 ⇔ ω = sk−2[i − fk−1 + 2, fk−2]sk−1sk−2[1, i − fk−1 + 1].
By the deﬁnition of conjugate word,

ω = Ci−fk−1+1(sk−2sk−1) = Ci−fk−1+1(sk−2αα−1sk−1) = Ci(α−1sk−1sk−2α) = Ci(Fk),

where fk−1 − 1 ≤ i ≤ fk − 1.
(2) In this case, ω ∈ T1.3 ⇔ ω = sk−1[i + 2, fk−1]sk−2sk−1[1, i + 1], and

ω = sk−1[i + 2, fk−1]sk−2αα−1sk−1[1, i + 1] = Ci(sk−1[2, fk−1]sk−2sk−1[1, 1]) = Ci(Fk),

where 0 ≤ i ≤ fk−1 − 2.

5. Proof of Theorem 2.4

This section is devoted to the proof of Theorem 2.4 which gives explicitly the expressions
of all gaps for each factors ω. By Theorem 2.2, we only need to determine the expressions of
gaps νω,1 and νω,2.
Suppose |ω| = n with fk ≤ n < fk+1 for some k. We divide the proof of Theorem 2.4 into
six parts, i.e., Theorem 2.4(1) to Theorem 2.4(6) according to the six types in Theorem 2.3. By
Theorem 2.1, νω,p = µ−1
2 νsk(ω),pµ−1
1 and ν−1
ω,p = µ1ν−1
sk(ω),pµ2. By Proposition 1.7(2), νsk,1 = sk+1
and νsk,2 = sk−1.

Theorem 2.4(1)

ω ∈ T1.1 ⇒
 {
νω,1 = sk+1, |νω,1| = fk+1 > 0,
νω,2 = sk−1, |νω,2| = fk−1 > 0.

11

Proof. Since ω is in T1.1, ω = sk by Theorem 2.3. So νω,1 = sk+1 and νω,2 = sk−1.

Theorem 2.4(2)

ω ∈ T1.2 ⇒
 {
νω,1 = Ci−fk−1(Fk−1), |νω,1| = fk−1 > 0,
νω,2 = ε, |νω,2| = 0.

Proof. Let ω ∈T1.2, by Theorem 2.3,

ω = sk−2[i − fk−1 + 2, fk−2]sk−1sk−2[1, i − fk−1 + 1], fk−1 − 1 ≤ i ≤ fk − 1,

so µ1 = sk−2[i − fk−1 + 2, fk−2] and µ2 = sk−2[1, i − fk−1 + 1].
(1) Since νsk−1,1 = sk:

νω,1 = µ−1
2 νsk−1,1µ−1
1 = s−1
k−2[1, i − fk−1 + 1]sks−1
k−2[i − fk−1 + 2, fk−2]
=s−1
k−2[1, i − fk−1 + 1](sk−2sk−3sk−2)s−1
k−2[i − fk−1 + 2, fk−2]
=sk−2[i − fk−1 + 2, fk−2]sk−3sk−2[1, i − fk−1 + 1] = Ci−fk−1+1(sk−2sk−3) = Ci−fk−1(Fk−1),

which yields that νω,1 = Ci−fk−1(Fk−1), |νω,1| = fk−1 > 0.
(2) Since νsk−1,2 = sk−2:

νω,2 = µ−1
2 νsk−1,2µ−1
1 = s−1
k−2[1, i − fk−1 + 1]sk−2s−1
k−2[i − fk−1 + 2, fk−2] = ε,

so νω,2 = ε, |νω,2| = 0.

Example. Taking ω = baabaaba ∈T1.2, it appears in F∞ as:
F∞ = abaaba(baabaaba)baaba(baabaaba)(baabaaba)baaba(baabaaba)baaba(baabaaba) · · ·
Theorem 2.4 gives the expressions of gaps, where n = 8, k = 4, i = 6:
{
νω,1 = Ci−fk−1(Fk−1) = C1(F3) = baaba, |νω,1| = f3 = 5 > 0,
νω,2 = ε, |νω,2| = 0.

Theorem 2.4(3)

ω ∈ T1.3 ⇒
 {
νω,1 = ε, |νω,1| = 0,
ν−1
ω,2 = Ci(Fk−2), |νω,2| = −fk−2 < 0.

Proof. Since ω is in T1.3, by Theorem 2.3,

ω = sk−1[i + 2, fk−1]sk−2sk−1[1, i + 1],

where 0 ≤ i ≤ fk−1 − 2, µ1 = sk−1[i + 2, fk−1] and µ2 = sk−1[1, i + 1].
(1) Since νsk−2,1 = sk−1:

νω,1 = µ−1
2 νsk−2,1µ−1
1 = s−1
k−1[1, i + 1]sk−1s−1
k−1[i + 2, fk−1] = ε,

i.e., νω,1 = ε, |νω,1| = 0.
(2) Since νsk−2,1 = sk−3:

ν−1
ω,2 = µ1ν−1
sk−2,2µ2 = sk−1[i + 2, fk−1]s−1
k−3sk−1[1, i + 1].

We are going to determine the expression of ν−1
ω,2 which we divide into three diﬀerent cases.

12

(2.1) If sk−3 is the suﬃx of sk−1[i + 2, fk−1], then

|sk−1[i + 2, fk−1]| = fk−1 − i − 1 ≥ fk−3,

i.e., i ≤ fk−2 − 1.

ν−1
ω,2 = (sk−3sk−4sk−3)[i + 2, fk−1]s−1
k−3(sk−3sk−4sk−3)[1, i + 1]

=(sk−3sk−4)[i + 2, fk−1](sk−3sk−4)[1, i + 1] = Ci+1(sk−3sk−4) = Ci(Fk−2).

(2.2) If sk−3 is the preﬁx of sk−1[1, i + 1], then

|sk−1[1, i + 1]| = i + 1 ≥ fk−3,

i.e., i ≥ fk−3 − 1.

ν−1
ω,2 = (sk−3sk−4sk−3)[i + 2, fk−1]s−1
k−3(sk−3sk−4sk−3)[1, i + 1]

=(sk−4sk−3)[i − fk−3 + 2, fk−2](sk−4sk−3)[1, i − fk−3 + 1]
=Ci−fk−3+1(sk−4sk−3) = Ci(Fk−2).

(2.3) If sk−3 is neither the suﬃx of sk−1[i + 2, fk−1] nor the preﬁx of sk−1[1, i + 1], then
fk−2 − 1 < i < fk−3 − 1, we have thus fk−2 < fk−3, which is obviously not true. So the third
case does not exist.
According to (2.1)-(2.3), we have ν−1
ω,2 = Ci(Fk−2), |νω,2| = −fk−2 < 0.

Example.Taking ω = baababaa ∈T1.3, it appears in F∞ as:
F∞ = a(baababaa)(baaba(baa)babaa)(baababaa)(baaba(baa)babaa)(baaba(baa)babaa)(ba · · ·
where (baa) in (baaba(baa)babaa) shows a overlap between two successive ω.
Theorem 2.4 gives the expressions of gaps, where n = 8, k = 4, i = 1:
{
νω,1 = ε, |νω,1| = 0,
ν−1
ω,2 = Ci(Fk−2) = C1(F2) = baa, |νω,2| = −f2 = −3 < 0.

Theorem 2.4(4)

ω ∈ T2.1 ⇒
 {
νω,1 = sk+1[n − fk − i + 1, fk+1 − i], |νω,1| = fk+2 − n > 0,
νω,2 = sk−1[n − fk − i + 1, fk−1 − i], |νω,2| = fk+1 − n > 0.

Proof. Since ω is in T2.4, by Theorem 2.3,

ω = sk−1[fk−1 − i + 1, fk−1]sksk−1[1, n − fk − i],

where 0 ≤ i ≤ n − fk, µ1 = sk−1[fk−1 − i + 1, fk−1] and µ2 = sk−1[1, n − fk − i].
(1) Since νsk,1 = sk+1:

νω,1 = µ−1
2 νsk,1µ−1
1 = s−1
k−1[1, n − fk − i]sk+1s−1
k−1[fk−1 − i + 1, fk−1]
=s−1
k−1[1, n − fk − i]sk−1sk−2sk−1s−1
k−1[fk−1 − i + 1, fk−1]
=sk−1[n − fk − i + 1, fk−1]sk−2sk−1[1, fk−1 − i] = sk+1[n − fk − i + 1, fk+1 − i],

which yields νω,1 = sk+1[n − fk − i + 1, fk+1 − i], |νω,1| = fk+2 − n > 0.
(2) Since νsk,2 = sk−1:

νω,2 = µ−1
2 νsk,2µ−1
1 = s−1
k−1[1, n − fk − i]sk−1s−1
k−1[fk−1 − i + 1, fk−1]
=sk−1[n − fk − i + 1, fk−1 − i],

i.e., νω,2 = sk−1[n − fk − i + 1, fk−1 − i], |νω,2| = fk+1 − n > 0.

13

Example. Taking ω = ababaabab ∈T2.1, it appears in F∞ as:
F∞ = abaababaaba(ababaabab)aabaababaaba(ababaabab)aaba(ababaabab)aabaababaaba(· · ·
Theorem 2.4 gives the expressions of gaps, where n = 9, k = 4, i = 1:





νω,1 = sk+1[n − fk − i + 1, fk+1 − i] = s5[1, 12] = aabaababaaba,
|νω,1| = fk+2 − n = f6 − 9 = 12 > 0,
νω,2 = sk−1[n − fk − i + 1, fk−1 − i] = s3[1, 4] = aaba,
|νω,2| = fk+1 − n = f5 − 9 = 4 > 0.

Theorem 2.4(5)

ω ∈ T2.2 ⇒
 {
νω,1 = sk[n − fk−1 − i + 1, fk − i], |νω,1| = fk+1 − n > 0,
ν−1
ω,2 = Fk+1[fk − i, n − i − 1], |νω,2| = fk − n < 0.

Proof. Since ω is in T2.2, by Theorem 2.3,

ω = sk[fk − i + 1, fk]sk−1sk[1, n − fk−1 − i],

where 0 ≤ i ≤ n − fk−1, µ1 = sk[fk − i + 1, fk] and µ2 = sk[1, n − fk−1 − i].
(1) Since νsk−1,1 = sk:

νω,1 = µ−1
2 νsk−1,1µ−1
1 = s−1
k [1, n − fk−1 − i]sks−1
k [fk − i + 1, fk]
=sk[n − fk−1 − i + 1, fk − i],

i.e., νω,1 = sk[n − fk−1 − i + 1, fk − i], |νω,1| = fk+1 − n > 0.
(2) Since νsk−1,2 = sk−2:

ν−1
ω,2 = µ1ν−1
sk−1,2µ2 = sk[fk − i + 1, fk]s−1
k−2sk[1, n − fk−1 − i].

We are going to determine the expression of ν−1
ω,2, which we divide into three distinct cases.
(2.1) If sk−2 is the suﬃx of sk[fk − i + 1, fk], then

|sk[fk − i + 1, fk]| = i ≥ fk−2.

ν−1
ω,2 = (sk−2sk−3)[fk − i + 1, fk−1]sk[1, n − fk−1 − i]

=(αFk−2Fk−3β−1)[fk − i + 1, fk−1](βFkα−1)[1, n − fk−1 − i]
=Fk−1[fk − i, fk−1]Fk[1, n − fk−1 − i − 1] = (Fk−1Fk)[fk − i, n − i − 1]
=(Fk+1β−1α−1βα)[fk − i, n − i − 1] = Fk+1[fk − i, n − i − 1].

(2.2) If sk−2 is the preﬁx of sk[1, n − fk−1 − i], then

|sk[1, n − fk−1 − i]| = n − fk−1 − i ≥ fk−2,

i.e., i ≤ n − fk.

ν−1
ω,2 = sk[fk − i + 1, fk](sk−3sk−2)[1, n − fk − i]

=(βFkα−1)[fk − i + 1, fk](αFk−1β−1α−1β)[1, n − fk − i]
=Fk[fk − i, fk]Fk−1[1, n − fk − i − 1] = Fk+1[fk − i, n − i − 1].

14

(2.3) If sk−2 is neither the suﬃx of sk[fk − i + 1, fk], nor the preﬁx of sk[1, n − fk−1 − i], then
n − fk < i < fk−2, i.e., n − fk < fk−2, and |sk[fk − i + 1, fk]| < fk−2, |sk[1, n − fk−1 − i]| < fk−2.

ν−1
ω,2 = sk−2[fk−2 − i + 1, fk−2]s−1
k−2sk−2[1, n − fk−1 − i]

=sk−2[fk−2 − i + 1, fk−2]s−1
k−2[n − fk−1 − i + 1, fk−2] = sk−2[fk−2 − i + 1, n − fk−1 − i]
=(sk−2sk−3sk−2)[fk−2 + fk−1 − i + 1, n − fk−1 + fk−1 − i]
=sk−1[fk − i + 1, n − i] = Fk+1[fk − i, n − i − 1].

According to (2.1)-(2.3), we know ν−1
ω,2 = Fk+1[fk − i, n − i − 1], |νω,2| = fk − n < 0.

Example. Taking ω = baabaabab ∈T2.2, it appears in F∞ as:
F∞ = abaaba(baabaabab)aaba(baabaaba(b)aabaabab)aaba(baabaabab)aaba(baabaaba(b)a · · ·
where ”(b)” in ”baabaaba(b)aabaabab” shows a overlap.
Theorem 2.4 gives the expressions of gaps, where n = 9, k = 4, i = 1:





νω,1 = sk[n − fk−1 − i + 1, fk − i] = s4[4, 7] = aaba,
|νω,1| = fk+1 − n = 13 − 9 = 4 > 0,
ν−1
ω,2 = Fk+1[fk − i, n − i − 1] = F5[7, 7] = b,
|νω,2| = fk − n = f4 − 9 = −1 < 0.

Theorem 2.4(6)

ω ∈ T2.3 ⇒
 {
ν−1
ω,1 = sk−1[fk+1 − n − i, fk−1 − i − 1], |νω,1| = fk − n < 0,
ν−1
ω,2 = Fk[fk+1 − n − i − 1, fk − i − 2], |νω,2| = fk−1 − n < 0.

Proof. Since ω is in T2.3, by Theorem 2.3,

ω = sk−1[fk+1 − n − i, fk−1]sk−2sk−1[1, fk−1 − i − 1],

where 0 ≤ i ≤ fk+1 − n − 2, µ1 = sk−1[fk+1 − n − i, fk−1] and µ2 = sk−1[1, fk−1 − i − 1].
(1) Since νsk−2,1 = sk−1:

ν−1
ω,1 = µ1ν−1
sk−2,1µ2 = sk−1[fk+1 − n − i, fk−1]s−1
k−1sk−1[1, fk−1 − i − 1]

=sk−1[fk+1 − n − i, fk−1]s−1
k−1[fk−1 − i, fk−1] = sk−1[fk+1 − n − i, fk−1 − i − 1],

i.e., ν−1
ω,1 = sk−1[fk+1 − n − i, fk−1 − i − 1], |νω,1| = fk − n < 0.
(2) Since νsk−2,2 = sk−3:

ν−1
ω,2 = µ1ν−1
sk−2,2µ2 = sk−1[fk+1 − n − i, fk−1]s−1
k−3sk−1[1, fk−1 − i − 1].

We are going to determine the expression of ν−1
ω,2, which we divide into three distinct cases.
(2.1) If sk−3 is the suﬃx of sk−1[fk+1 − n − i, fk−1], then

|sk−1[fk+1 − n − i, fk−1]| = fk−1 − fk+1 + n + i + 1 ≥ fk−3,

i.e., i ≥ fk + fk−3 − n − 1.

ν−1
ω,2 = (sk−3sk−4)[fk+1 − n − i, fk−2]sk−1[1, fk−1 − i − 1]

=(βFk−3Fk−4α−1)[fk+1 − n − i, fk−2](αFk−1β−1)[1, fk−1 − i − 1]
=Fk−2[fk+1 − n − i − 1, fk−2]Fk−1[1, fk−1 − i − 1] = Fk[fk+1 − n − i − 1, fk − i − 2].

15

(2.2) If sk−3 is the preﬁx of sk−1[1, fk−1 − i − 1], then

|sk−1[1, fk−1 − i − 1]| = fk−1 − i − 1 ≥ fk−3,

i.e., i ≤ fk−2 − 1.

ν−1
ω,2 = sk−1[fk+1 − n − i, fk−1](sk−4sk−3)[1, fk−2 − i − 1]

=(αFk−1β−1)[fk+1 − n − i, fk−1](βFk−4Fk−3β−1)[1, fk−2 − i − 1]
=Fk−1[fk+1 − n − i, fk−1]Fk−2[1, fk−2 − i − 2] = Fk[fk+1 − n − i − 1, fk − i − 2],

the 3-rd equality holds because Fk−4Fk−3 = Fk−2α−1β−1αβ.
(2.3) If sk−3 is neither the suﬃx of sk−1[fk+1−n−i, fk−1], nor the preﬁx of sk−1[1, fk−1−i−1].
Then fk−2−1 < i < fk +fk−3−n−1, i.e., fk−2−1 < fk+fk−3−n−1, so n < fk+fk−3−fk−2 < fk,
which is obviously not true. So this case does not exist.
According to (2.1)-(2.3), we have ν−1
ω,2 = Fk[fk+1−n−i−1, fk −i−2], |νω,2| = fk−1−n < 0.

Example. Taking ω = baababaab ∈T2.3, it appears in F∞ as:
F∞ = a(baababaa(b)aaba(baab)abaa(b)aababaa(b)aaba(baab)abaa(b)aaba(baab)abaa(b)a · · ·
where ”(b)” in ”baababaa(b)aaba” and ”(baab)” in ”aaba(baab)abaa” show two diﬀerent overlaps.
Theorem 2.4 gives the expressions of gaps, where n = 9, k = 4, i = 1:





ν−1
ω,1 = sk−1[fk+1 − n − i, fk−1 − i − 1] = s3[3, 3] = b,
|νω,1| = fk − n = f4 − 9 = −1 < 0,
ν−1
ω,2 = Fk[fk+1 − n − i − 1, fk − i − 2] = F4[2, 5] = baab,
|νω,2| = fk−1 − n = f3 − 9 = −4 < 0.

6. Combinatorial Properties Of Factors

In this section, we will discuss some combinatorial properties of the factors of the Fibonacci
sequence. Let F∞ = x1x2 · · · xn · · · be the Fibonacci sequence and ω ≺ F∞ be a factor of F∞,
as usual let {ωp}p≥1 be the factor sequence where ωp is p-th appearance of ω. Notice that if we
consider the location of ωp ∈ F∞, then the factors ωp and ωq(p ̸= q) are distinct. In fact, ωp
should be regarded as two variables ω and p, ω is the factor and p indicates the location of ω.
Let P be a property, we say ω ∈ P if there exists an index p ∈ N such that ωp ∈ P. But in
this case, we do not know where is the location of ωp ∈ F∞, so we wish to determine the set
{(ω, p), ω ≺ F∞, p ∈ N| ωp ∈ P}.

Example. we consider P is ”property of square factor”, that is, if ω ∈ P, then there exists p
such that ωpωp+1 ∈ F∞. Let ω = ab ∈ F∞, then ω1 = F∞[1, 2], ω2 = F∞[4, 5], and we know
that ω1 ̸∈ P, ω2 ∈ P, ω ∈ P.

By the example, we are led naturally to study combinatorial properties of factor ω of the
following two types:

Local Question: Determine all factors ω ∈ F∞ such that ω ∈ P, i.e., there exists
p ∈ N such that ωp ∈ P.
Global Question: Determine all factors ω ∈ F∞ and all indices p such that ωp ∈ P.

More precisely, deﬁne the spectrum of P by

Λ(P) := Λ(P)(ω, p) := {(ω, p), ω ≺ F∞, p ∈ N| ωp ∈ P}.

16

By the deﬁnition above, the Global question is equivalent to determine the spectrum of the
property P.

Remark. By the deﬁnition above, the spectrum of the property P depends two independent
variables ω and p. For a given factor ω, the spectrum Λ(P) will give all indices p such that
ωp ∈ P; and for a given index p, the spectrum Λ(P) will give all factors ω such that ωp ∈ P.
The Local question is equivalent to determine the projection of the spectrum Λ(P) on factor
space.

We will study mainly some combinatorial properties such as ”adjacent property, separated
property and overlapped property of factors” for both questions. From our knowledge, all
previous studies on combinatorial over words concern with only local question, in fact, ”Global
Question” is much more diﬃcult than ”Local Question”.

Notation. For the convenience for the discussions below, we give some notations.
(1)Γa = {p ≺ N| F∞[p] = a}; (2)Γb = {p ≺ N| F∞[p] = b};
(3)Γaa = {p ≺ N| F∞[p] = a, F∞[p + 1] = a}; (4)Γab = {p ≺ N| F∞[p] = a, F∞[p + 1] = b}.
It is easy to see that Γa ⊔ Γb = N and Γaa ⊔ Γaa = Γa.

Remark. It is known that F∞[p] can be expressed explicitly by the following formula: F∞[p] =
a if [(p + 1)ξ] − [pξ] = 0, F∞[p] = b if [(p + 1)ξ] − [pξ] = 1, where ξ = 3−√5
2 . So the sets Γa and
Γb can be deﬁne easily.

Lemma 6.1. Let ω ∈ F∞, then νω,p = νω,1 ⇔ p ∈ Γa, νω,p = νω,2 ⇔ p ∈ Γb.

Proof. By Theorem 2.2, the gap sequence {νω,p}p≥1 is Fibonacci sequence, in which νω,1 and
νω,2 correspond with letter a and b respectively. Thus νω,p = νω,1 ⇔ F∞[p] = a and νω,p =
νω,2 ⇔ F∞[p] = b.

Deﬁnition 6.2 (Power Property). Let ω ∈ F∞. We say that ω ∈ Pi(i ≥ 1) if there exists p
such that ωp · · · ωp+i ≺ F∞.

Proposition 6.3 (Global property for Power Property).
(1) Λ(P1) = (T1.2, Γb) ⊔ (T1.3, Γa);
(2) Λ(P2) = (T1.3, Γaa);
(3) Λ(P2) \ Λ(P1) = (T1.2, Γb) ⊔ (T1.3, Γab);
(4) Λ(Pi) = ∅, i ≥ 3.

Proof. (1) The spectrum of P1 contains all ω and p such that ωp ∈ P1, i.e., ωpωp+1 ≺ F∞, which
is equal to νω,p = ε. By Theorem 2.2, there are two cases:
Case 1: νω,1 = ε and νω,p = νω,1. By Theorem 2.4, νω,1 = ε ⇔ ω ∈T1.3. By Lemma 6.1,
νω,p = νω,1 ⇔ p ∈ Γa.
Case 2: νω,2 = ε and νω,p = νω,1. By Theorem 2.4, νω,2 = ε ⇔ ω ∈T1.2. By Lemma 6.1,
νω,p = νω,2 ⇔ p ∈ Γb.
(2) The spectrum of P2 contains all ω and p such that ωpωp+1ωp+2 ≺ F∞. By Theorem 2.2
and Theorem 2.4, it is equivalent to νω,p = νω,p+1 = ε, i.e., νω,1 = ε and aa ≺ F∞ or νω,2 = ε
and bb ≺ F∞. Since aa ≺ F∞ and bb ̸≺ F∞, the spectrum of P2 contains ωp with ω ∈T1.3,
F∞[p] = a and F∞[p + 1] = a, i.e., (T1.3, Γaa).
(3) Since (1) and (2), by the minus of sets, Λ(P2) \ Λ(P1) = (T1.2, Γb) ⊔ (T1.3, Γab).
(4) The spectrum of P3 contains all ω and p such that ωpωp+1ωp+2ωp+3 ≺ F∞. By Theorem
2.2 and Theorem 2.4, it is equivalent to νω,p = νω,p+1 = νω,p+2 = ε, i.e., νω,1 = ε and aaa ≺ F∞
or νω,2 = ε and bbb ≺ F∞. Since aaa ̸≺ F∞ and bbb ̸≺ F∞, both of them are obviously not true.
So there is no 4-square word in F∞, i.e.Λ(P3) = ∅. Similarly, Λ(Pi) = ∅, i ≥ 3.

17

We have shown that the Local question is equivalent to determine the projection of the
spectrum Λ(P) on factor space. Thus we get the Local property for power property immediately
from Proposition 6.3, where only Corollary 6.3(3) is proved by the minus of sets.

Corollary 6.4 (Local property for Power Property).
(1) Λ(P1) = T1.2 ⊔ T1.3;
(2) Λ(P2) = T1.3;
(3) Λ(P2) \ Λ(P1) = T1.2;
(4) Λ(Pi) = ∅, i ≥ 3.

Remark. Corollary 6.4(1) means ”ω2 ≺ F∞ ⇔ ω ∈T1.2⊔T1.3”, i.e., ”ω2 ≺ F∞ ⇔ ω is a
conjugation of Fk”, which is equivalent to Theorem 3(1) to 3(3) in Wen and Wen[19]. Similarly,
Corollary 6.4(2) is equivalent to Theorem 3(4), Corollary 6.4(3) is equivalent to Theorem 3(5),
Corollary 6.4(4) is equivalent to Theorem 3(6) in Wen and Wen[19].

Deﬁnition 6.5 (Separated Properties). Let ω ∈ F∞. We say that ω ∈ Si (i = 1, 2, · · · ) if there
exists p and nonempty factors u1, · · · , ui−1 such that

ωpu1ωp+1u2 · · · ui−1ωp+i ∈ F∞.

If all i ∈ N, ω ∈ Si, we say that ω ∈ S∞.

Remark. By deﬁnition of νω,p, ω ∈ Si is equivalent to there exists p such that |νω,p|, |νω,p+1|,
· · · , |νω,p+i−1| are strictly positive.

Proposition 6.6 (Global property for separated Property).
(1) Λ(S1) = (T1.1 ⊔ T2.1, N) ⊔ (T1.2 ⊔ T2.2, Γa);
(2) Λ(S2) = (T1.1 ⊔ T2.1, N) ⊔ (T1.2 ⊔ T2.2, Γaa);
(3) Λ(S3) = (T1.1 ⊔ T2.1, N);
(4) Λ(S∞) = T1.1 ⊔ T2.1.

Proof. (1) ωp ∈ S1 means |νω,p| > 0. By Theorem 2.2 and Theorem 2.4, there are two cases:
Case 1: Both |νω,1| and |νω,2| are strictly positive. Then ω ∈T1.1⊔T2.1.
Case 2: |νω,1| > 0, |νω,2| ≤ 0 and νω,p = νω,1. Then ω ∈T1.2⊔T2.2. By Lemma 6.1,
νω,p = νω,1 ⇔ F∞[p] = a, i.e., p ∈ Γa.
(2) ωp ∈ S2 means both |νω,p| and |νω,p+1| are strictly positive. By Theorem 2.2 and Theorem
2.4, there are two cases:
Case 1: Both |νω,1| and |νω,2| are strictly positive. Then ω ∈T1.1⊔T2.1.
Case 2: |νω,1| > 0, |νω,2| ≤ 0 and νω,p = νω,p+1 = νω,1. Then ω ∈T1.2⊔T2.2. By Lemma 6.1,
νω,p = νω,p+1 = νω,1 ⇔ F∞[p] = F∞[p + 1] = a, i.e., p ∈ Γaa.
(3) ωp ∈ S3 means |νω,p|, |νω,p+1| and |νω,p+2| are all strictly positive. Since aaa, bbb ̸≺ F∞,
both νω,1 and νω,2 can not appear three times continually. So ωp ∈ S3 contains both |νω,1| and
|νω,2| are strictly positive. By Theorem 2.4, ω ∈T1.1⊔T2.1.
(4) When ω ∈T1.1⊔T2.1., both |νω,1| and |νω,2| are strictly positive, thus ∀p ∈ N, |νω,p| > 0,
i.e., ω ∈ S∞.

Corollary 6.7 (Local property for separated properties).
(1) Λ(S1) = T1.1 ⊔ T1.2 ⊔ T2.1 ⊔ T2.2;
(2) Λ(S2) = Λ(S1);
(3) Λ(S3) = T1.1 ⊔ T2.1;
(4) Λ(S∞) = Λ(S3).
 18

Remark. Corollary 6.7(4) determine the factor with separated property completely, which we
only know T1.1 (singular word) before, see[19].

Deﬁnition 6.8 (Overlapped Property). Let ω ∈ F∞. We say that ω ∈ Oi (i = 1, 2, · · · ) if
there exists p and nonempty factors u1, · · · , ui−1 such that:

ωpu−1
1 ωp+1u−1
2 · · · u−1
i−1ωp+i ∈ F∞.

If all i ∈ N, ω ∈ Oi, we say that ω ∈ O∞.

Remark. By deﬁnition of νω,p, ω ∈ Oi is equivalent to there exists p such that |νω,p|, |νω,p+1|,
· · · , |νω,p+i−1| are strictly negative.

Proposition 6.9 (Global property for overlapped Property).
(1) Λ(O1) = (T1.3 ⊔ T2.2, Γb) ⊔ (T2.3, N);
(2) Λ(O2) = (T2.3, N);
(3) Λ(O∞) = T2.3.

Proof. (1) ωp ∈ O1 means |νω,p| < 0. By Theorem 2.2 and Theorem 2.4, there are two cases:
Case 1: Both |νω,1| and |νω,2| are strictly negative. Then ω ∈T2.3.
Case 2: |νω,1| ≥ 0, |νω,2| < 0 and νω,p = νω,2. Then ω ∈T1.3⊔T2.2. By Lemma 6.1,
νω,p = νω,2 ⇔ F∞[p] = b, i.e., p ∈ Γb.
(2) ωp ∈ O2 means both |νω,p| and |νω,p+1| are strictly negative. Since bb ̸∈ F∞, the word
ωp ∈ (T1.3 ⊔ T2.2, Γb) doesn’t possess O2. When ω ∈T2.3, both |νω,1| and |νω,2| are strictly
negative. So for ∀p ∈ N, ωp ∈T2.3 possesses O2.
(3) By Theorem 2.4, when ω ∈T2.3, both |νω,1| and |νω,2| are strictly negative, thus ∀ p,
|νω,p| < 0, i.e., ω ∈ O∞.

Corollary 6.10 (Local property for overlapped property).
(1) Λ(O1) = T1.3 ⊔ T2.2 ⊔ T2.3;
(2) Λ(O2) = T2.3;
(3) Λ(O∞) = Λ(O2).

Remark. Corollary 6.10 contains Theorem 6 in Wen and Wen[19]. Moreover, we correct a small
mistake (Lemma 7) there: If ω ∈ O1, then the overlap of ω is unique. In fact, when ω ∈T2.3,
ν−1
ω,1 = sk−1[fk+1 −n−i, fk−1 −i−1], |νω,1| = fk −n < 0 and ν−1
ω,2 = Fk[fk+1 −n−i−1, fk −i−2],
|νω,2| = fk−1 − n < 0, which means the overlap of ω is not unique. For instance, let ω =
baababaab ∈T2.3, both baababaa(b)aababaab and baaba(baab)abaab are factors of F∞.

Acknowledgments

The research is supported by the Grant NSF No.61071066, No.11271223 and No.11371210.

References

[1] J.M.Allouche, J.Shallit, Automatic sequences: Theory, applications, generalizations.
Cambridge University Press, Cambridge, 2003.

[2] I.M.Ara´ujo, V.Bruy`ere, Words derivated from Sturmian words, Theor. Comput. Sci. 340
(2005) 204-219.
 19

[3] L.Balkov´a, E.Pelantov´a, W.Steiner, Sequences with constant number of return words,
Monatsh Math. 155 (2008) 251-263.

[4] J.Berstel, Recent results in Sturmian words, in J.Dassow, A.Salomaa (Eds.), Develop-
ments in Language Theory, World Scientiﬁc, Singapore, 1966, pp.13-24.

[5] J.Berstel, Mot de Fibonacci, S´eminaire d’informatique th´erique, L.I.T.P., Paris, Ann´ee
1980/1981, pp.57-78.

[6] V.Berthe, S.Brlek, P.Choquette, Smooth words over arbitrary alphabets, Theor. Comput.
Sci. 341 (2005) 293-310.

[7] W.-T.Cao, Z.-Y.Wen, Some properties of the factors of Sturmian sequences, Theor. Com-
put. Sci. 304 (2003) 365-385.

[8] W.-F.Chuan, H.-L.Ho, Locating factors of the inﬁnite Fibonacci word, Theor. Comput.
Sci. 349 (2005) 429-442.

[9] W.-F.Chuan, H.-L.Ho, Factors of characteristic words: Location and decompositions,
Theor. Comput. Sci. 411 (2010) 31-33.

[10] F.Durand, A characterization of substitutive sequences using return words, Discrete Math.
179 (1998) 89-101.

[11] A.Glen, Occurrences of palindromes in characteristic Sturmian words, Theor. Comput.
Sci. 352 (2006) 31-46.

[12] T.Kamae, J.I.Tamura, Z.-Y.Wen, Hankel determinants for the Fibonacci word and Pad´e
approximation, Acta Arithmetica. 89 (1999) 123-161.

[13] M.Lothaire, Combinatorics on words, in: Encyclopedia of Mathematics and its applica-
tions, Vol.17, Addison-Wesley, Reading, MA, 1983.

[14] M.Lothaire, Algebraic combinatorics on words, Cambridge Univ. Press, Cambridge, 2002.

[15] G.Melancon, Lyndon words and singular factors of sturmian words, Theor. Comput. Sci.
218 (1999) 41-59.

[16] K.Saari, Lyndon words and Fibonacci numbers, Journal of Combinatorial Theory Series
A. 121 (2014) 34-44.

[17] J.I.Tamura, Pad´e approximation for words generated by certain substitutions, and Hankel
determinants, Number Theory and its Applications. 2 (1999) 309-346.

[18] B.Tan, Z.-Y.Wen, Some properties of the Tribonacci sequence, European J. Combin. 28
(2007) 1703-1719.

[19] Z.-X.Wen, Z.-Y.Wen, Some properties of the singular words of the Fibonacci word, Eu-
ropean J. Combin. 15 (1994) 587-598.

[20] L.Vuillon, A characterization of Sturmian words by return words, European J. Combin.
22 (2001) 263-275.
 20
