<!-- source: https://arxiv.org/pdf/1905.03283 | converted from PDF -->

arXiv:1905.03283v3  [math.NT]  22 Aug 2021
ALGORITHMIC CLASSIFICATION OF
NONCORRELATED BINARY PATTERN SEQUENCES

JAKUB KONIECZNY

Abstract. The main subject of this paper are binary pattern sequences, that
is, sequences of the form (−1)#(n,A) where A is a set of strings of 0s and
1s, and #(n, A) denotes the total number of times patterns from A appear
in the binary expansion of n. A sequence is said to be noncorrelated if the
corresponding spectral measure is equal to the Lebesgue measure.
We show that it is possible to algorithmically verify if a given binary pat-
tern sequence is noncorrelated. As an application, we compute that there
are exactly 2272 noncorrelated binary pattern sequences of length ≤ 4. If we
restrict our attention to patterns that do not end with 0, we put forward a
suﬃcient condition for a pattern sequence to be noncorrelated. We conjecture
that this condition is also necessary, and verify this conjecture for lengths ≤ 5.

1. Introduction

Uniformity properties of sequences deﬁned in terms of digital expansions have
long been studied. Consider, for instance, the Thue–Morse sequence t(n) = (−1)
s2(n),
where s2(n) denotes the sum of binary digits of n, discussed at length by Allouche
and Shallit in the survey paper [AS99]. It was shown by Gelfond [Gel68] (see also
[MS98]) that t(n) is equidistributed in arithmetic progressions:

(1) lim
N →∞ |{0 ≤ n < N | t(An + B) = +1}| /N = 1/2

for all A ∈ N and B ∈ N0, and the rate of convergence can be made explicit.
Analogous results hold also for other bases, with mild additional assumptions to
account for the fact that sk(n) ≡ n mod k − 1. Mauduit and S´ark¨ozy [MS98] also
observed that the Thue–Morse sequence admits large self-correlations. Here, the
(self-)correlation coeﬃcients of a sequence a : N → C are deﬁned by

(2) γa(m) := lim
N →∞ 1
N
 N −1∑

n=0 a(n)a(n + m),

and a simple computation shows that γt(1) = −1/3 ̸= 0 (see Section 3 for details).
By the same token,

(3) γt(2ℓ) = −1/3 for all ℓ ∈ N0,

meaning in particular that γ(m) ̸→ 0 as m → ∞. On the other hand, the coeﬃcients
γt(m) tend to be rather small; in particular

(4) lim
N →∞ 1
N
 N −1∑

m=0 γt(m)
2 = 0,

2010 Mathematics Subject Classiﬁcation. Primary: 47B15; Secondary: 11B50.

1

2 J. KONIECZNY

which follows e.g. from results in [Coq76]. The spectral measure µa on R/Z associ-
ated to a sequence a : N → C is characterised by the identity ∫

R/Z exp(2πimt)dµa(t) =
γa(m), and (4) is equivalent to absolute continuity of µt.
Many other notions of uniformity have been investigated for the Thue–Morse
sequence. In an inﬂuential paper, Mauduit and Rivat showed that t(n) and its
analogues in diﬀerent bases are equidistributed along the primes [MR10]. Drmota,
Mauduit and Rivat [DMR19] showed that t(n2) is a normal sequence, meaning
that each ﬁnite sequence of ±1s appears with the expected frequency. Spiegel-
hofer [Spi18] proved that t(n) has level of distribution 1, which is a far-reaching
quantitative generalisation of (1) and can be used to show equdistribution along
Piatetski–Shapiro sequences ⌊nc⌋, 1 < c < 2 (see [FM96] for analogous, but some-
what weaker, results in diﬀerent bases). It was also shown by the author [Kon19]
that t(n) has small Gowers norms, meaning that it is uniform from the point of
view of higher order Fourier analysis.
Another oft-studied sequence carries the name of Rudin–Shapiro and is given by
r(n) = (−1)
#(11,n), where #(11, n) denotes the number of times the pattern 11 ap-
pears in the binary expansion of n, allowing overlaps. Similarly to the Thue–Morse
sequence, the Rudin–Shapiro sequence is equidistributed in arithmetic progressions
and along the primes [MR15], and has small Gowers norms [Kon19]. However, in
contrast to (3), the Rudin–Shapiro sequence is noncorrelated, by which we mean
that γr(m) = 0 for all m ≥ 1 or, equivalently, that the spectral measure µr is is
the Lebesgue measure. Intuitively, noncorrelated sequences are free of any sort of
periodic behaviour.
The Thue–Morse and the Rudin–Shapiro sequences are special cases of what we
call binary pattern sequences. In general, a binary pattern sequence takes the form

a(n) = aA(n) = (−1)
#(A,n),

where A is a ﬁnite set of patterns over the alphabet {0, 1} and #(A, n) denotes
the total number of appearances of patterns from A in the binary expansion of n
(see Section 2 for details). Pattern sequences were studied in a more general con-
text by Morton and Mourant [MM89, Mor90], Coquet, Kamae and Mend`es France
[CKMF77], and Boyd, Cook and Morton [BCM89]. Generalised Rudin–Shapiro
sequences and their correlation coeﬃcients were studied by Allouche and Liardet
[AL91]. Finally, Zheng, Peng and Kamae [ZPK18] studied correlation coeﬃcients
of binary pattern sequences, and obtained a complete classiﬁcation of noncorrelated
sequences corresponding to sets of patterns of length ≤ 3. Examples of sets A that
give rise to noncorrelated sequences include:

• {11} (then aA(n) = r(n) is the Rudin–Shapiro sequence);
• {11, 1} (then aA(n) = r(n)t(n)) and {10, 1} (then aA(n) = (−1)
nr(n));
• {101, 111}, or more generally {101, 111} ∪ B for a set B ⊆ {0, 1}2.

In this paper, we extend the result of [ZPK18] to patterns of length ≤ 4 and
put the ﬁndings in a wider context provided by the theory of automatic and reg-
ular sequences. Many of the ideas we use have their analogues and prototypes in
[ZPK18]; throughout the paper we give references to the relevant results therein.
Unfortunately, there does not appear to be a simple criterion that determines
if a given pattern sequence is noncorrelated (except for the partial information

NONCORRELATED PATTERN SEQUENCES 3

suggested by Conjecture 1.2 below). Due to practical limitations we only state a
counting result here, as opposed to a complete list.1

Theorem A. There are precisely 2272 noncorrelated binary pattern sequences cor-
responding to patterns of length ≤ 4.

As a key step towards obtaining the above result, we reduce the task of verifying
whether a given binary pattern sequence is noncorrelated to a ﬁnite computation,
which can then be automated. The time complexity of the resulting algorithm is
polynomial in 2ℓ, where ℓ denotes the length of patterns under consideration. Since
it takes approximately 2ℓ bits to specify a binary pattern sequence, this is optimal
up to improvements in the exponent.

Theorem B. There exists an algorithm which, given a ﬁnite set of patterns A ⊆
{0, 1}ℓ, performs 2O(ℓ) operations and decides if the corresponding pattern sequence
aA is noncorrelated.

While we keep the exposition fairly self-contained, we also wish to emphasize that
the above problem can be seen as a part of a larger theory. We note that binary
pattern sequences are 2-automatic (see Section 2 for the relevant deﬁnitions). A
crucial component of our reasoning is Theorem 3.5, which assets that the correlation
sequences coming from automatic sequences are regular. While this result will not
come as a surprise to the experts in the ﬁeld, to the best of our knowledge it does
not appear in print elsewhere. Its importance stems from the fact that a regular
sequence admits a simple recursive description, an hence many properties are easily
veriﬁed for such a sequence. In our particular application, we reduce the task of
determining if a pattern sequence is noncorrelated to the ostensibly simpler task of
determining if a 2-regular sequence is identically zero.
The problem of classifying noncorrelated pattern sequences becomes more tractable
if we impose additional assumptions on the set of patterns under consideration.
Let us call a binary pattern sequence a : N0 → {+1, −1} dilation-invariant if
a(2n) = a(n) for all n ∈ N0, or equivalently, if a = aA for a set A that con-
tains only patterns that begin and end with 1 (see Section 2.4 for details). In the
dilation-invariant case, we have a conjectural classiﬁcation, which we are able to
conﬁrm in one direction in full generality, and in the opposite direction for patterns
of length ≤ 5.

Theorem C. Let A be a set of patterns over the alphabet {0, 1}, all of which begin
and end with 1. Let ℓ be the length of the longest word in A and let a = aA be
the corresponding binary pattern sequence. If ℓ ≥ 2 and 1{0, 1}ℓ−21 ⊆ A then a is
noncorrelated. Conversely, if 2 ≤ ℓ ≤ 5 and a is noncorrelated then 1{0, 1}ℓ−21 ⊆
A.

Conjecture 1.1. Let A, ℓ and a be as in Theorem C. If a is noncorrelated then
ℓ ≥ 2 and 1{0, 1}ℓ−21 ⊆ A.

If A = 1{0, 1}ℓ−21 then the fact that aA is noncorrelated follows from [ZPK18].
More generally, Theorem 1.3 in [ZPK18] (see also [AL91]) provides a classiﬁcation
of all noncorrelated binary pattern sequences aA for sets of patterns of the form
A = w1{0, 1}ℓ1w2{0, 1}ℓ2 . . . ws{0, 1}ℓsws+1 where s ∈ N, wi are words over the

1The list, together with the code which can be used to produce it, is available from the author.

4 J. KONIECZNY

alphabet {0, 1} and ℓ1, ℓ2, . . . , ℓs ∈ N0. Conjecture 1.1 is consistent with said
classiﬁcation.
Returning to the general case, we notice that each binary pattern sequence
a : N0 → {+1, −1} can be written as the product of a periodic sequence h and
a dilation-invariant pattern sequence b (Lemma 2.9). The correlation coeﬃcients
of a and b are closely related (see also Remark 5.6), and in all cases that we were
able to check (i.e., ℓ ≤ 4), if a is noncorrelated then so is b. This motivates us to
put forward the following conjecture.

Conjecture 1.2. Let a : N0 → {+1, −1} be a noncorrelated binary pattern se-
quence. Then a is the product of a periodic sequence and an dilation-invariant
noncorrelated binary pattern sequence

Above we restricted our attention to base 2 for the sake of brevity. In the
remaining part of the paper, we work in arbitrary base k ≥ 2. In particular, the
natural base-k variant of Theorem B holds true. The same applies to the ﬁrst part
of Theorem C, except that it is less clear what the base-k variant should be and the
resulting statement is vacuous for many values of k (see Proposition 5.3). When it
comes to computations, we only consider base 2 since for larger bases the number of
distinct pattern sequences becomes so large that merely listing them all is already
infeasible even for modest pattern lengths.

Acknowledgements. While writing this paper, the author was supported by the
ERC grant ErgComNum 682150 at the Hebrew University of Jerusalem. During
the review process, the author was working within the framework of the LABEX
MILYON (ANR-10-LABX-0070) of Universit´e de Lyon, within the program ”In-
vestissements d’Avenir” (ANR-11-IDEX-0007) operated by the French National
Research Agency (ANR). The author also acknowledges support from the Founda-
tion for Polish Science (FNP).
The author wishes to express his gratitude to Boris Adamczewski, Jakub Byszewski,
Aihua Fan and Tamar Ziegler for helpful conversations and to the anonymous Ref-
eree for the careful reading of this paper and constrictive suggestions.

2. Background and definitions

Convention: Throughout the paper, k denotes the base and is considered to
be ﬁxed. In particular, all constructions and constants are allowed to depend on k
unless explicitly stated otherwise.

2.1. Pattern sequences. We let Σk = {0, 1, . . . , k − 1} denote the set of digits
in base k. For a set X, we let X ∗ denote the monoid consisting of words over the
alphabet X, equipped with the operation of concatenation and neutral element ǫ,
the empty word. For v ∈ X ∗, |v| denotes the length of v. For n ∈ N0, (n)k ∈ Σ∗
k
denotes the expansion of n in base k (without leading zeros). Conversely, for v ∈ Σ∗
k,
[v]k ∈ N0 denotes the integer encoded by v.
Let X be a set. We say that a word v ∈ X ∗ appears in another word w ∈ X ∗,
or that v is a factor of w, if there exist x, y ∈ X ∗ such that w = xvy. We call v
a preﬁx (resp. suﬃx) of w if we may take x = ǫ (resp. y = ǫ). We further deﬁne
#(v, w) to be the number of times v appears in w, that is, the number distinct of
pairs (x, y) ∈ X ∗ × X ∗ such that w = xvy. We note that this deﬁnition allows

NONCORRELATED PATTERN SEQUENCES 5

for overlaps, so for instance #(010, 01010) = 2. More generally, for a ﬁnite set
A ⊆ X ∗, we deﬁne #(A, w) = ∑
v∈A #(v, w).
Accordingly, for n ∈ N0 and v ∈ Σ∗
k \ {0}∗, #(n, v) denotes the number of times
that v appears in the base-k expansion of n padded with suﬃciently many leading
zeros, that is, #(v, n) = (v, 0|v|−1(n)k). The inclusion of the leading zeros in the
expansion of n ensures better behaviour of the map n ↦→ #(v, n); in particular, for
each n, m ∈ N0 and suﬃciently large α ∈ N0 we have #(v, kαm + n) = #(v, kαm) +
#(v, n). The assumption that v is not a string of zeros ensures that #(v, n) is
well-deﬁned, in the sense that for ﬁxed n, the sequence (v, 0α(n)k) (α ∈ N0) is
eventually constant.
We will call a set A ⊆ Σ∗
k admissible if A is ﬁnite and A ∩ {0}∗ = ∅, so that we
may deﬁne #(A, n) = ∑v∈A #(v, n). For any admissible set A, the corresponding
pattern sequence is deﬁned by (cf. [ZPK18, Deﬁnition 1.1])

(5) aA(n) = (−1)
#(A,n).

If additionally |u| ≤ ℓ for all u ∈ A then we say that a is a pattern sequence of
length ≤ ℓ, or equivalently we deﬁne the length of a as the least possible value of
maxu∈A |u| among all representations of a in the form (5), where A ⊆ Σ∗
k is an
admissible set. Note that one pattern sequence can have multiple representations
of the aforementioned form.
For two sets A, B, we let A⊕ B denote the symmetric diﬀerence (A\ B)∪(B \ A).

Lemma 2.1. The class of pattern sequences N0 → {+1, −1} is closed under mul-
tiplication.

Proof. It is enough to note that for any admissible sets A, B ⊆ Σ∗
k we have

aA · aB = aA⊕B. □

It will usually be convenient to impose further restrictions on the set of patterns
A. Depending on the context we require that either A has not leading zeros (in the
sense that that 0 is not a preﬁx of v for any v ∈ A) or that A has constant length
(in the sense that there is some ℓ ∈ N such that |v| = ℓ for all v ∈ A).

Lemma 2.2. Let ℓ ∈ N0 and let a : N0 → {+1, −1} be a pattern sequence of length
≤ ℓ. Then there exist admissible sets B, C ⊆ Σ∗
k such that B has no leading zeros,
C has constant length ℓ, and a = aB = aC . Moreover, B and C are uniquely
determined by a.

Proof. Pick any admissible set A ⊆ Σ∗
k with a = aA. Note that for each v ∈ Σ∗
k
and each n ∈ N0 we have

(6) #(v, n) =
 k−1∑

i=0 #(iv, n)

To construct B, begin with A and as long as A contains at least one word starting
with 0, say 0v, replace A with A = A ⊕ {iv | i ∈ Σk} ⊕ {v}. Because of (6), this
operation does not change the sequence aA. Since each iteration decreases the total
number of leading zeros in the patterns in A, after a ﬁnite number of steps this
procedure must terminate and the resulting set of patterns has no leading zeros.
To construct C, likewise, begin with A and as long as A contains at least one
word v with length |v| < ℓ, pick the shortest such word v and replace A with
A ⊕ {iv | i ∈ Σk} ⊕ {v}. Like before, this operation does not change the sequence

6 J. KONIECZNY

aA. Each iteration either decreases the number of words in A with least possible
length, or increases the length of the shortest word in A. At the same time, no
words of length larger than ℓ are introduced. Hence, after a ﬁnite number of steps
this procedure must terminate and the resulting set of patterns has constant length
equal to ℓ.
It remains to show uniqueness. Using Lemma 2.1, we may assume that A =
∅. For the sake of contradiction, suppose that one of B and C is non-empty.
Consider ﬁrst the case when B ̸= ∅ and let v be the shortest word in B. Then
1 = aB([v]k) = −1, since 0ℓv contains exactly one pattern from B, namely v.
Hence, we have reached a contradiction. Consider next the case when C ̸= ∅ and
choose the word 0mv ∈ C where m is largest possible. Then we again reach the
contradiction: 1 = aC ([v]k) = −1. □

Remark 2.3. We focus our attention on ±1-valued sequences for two basic reasons.
The ﬁrst one is practical: The noncorrelation phenomenon that we are interested in
relies on occurrence of certain arithmetic coincidences, which become less likely as
the number of possible values increases; accordingly, the computational part of the
problem becomes increasingly resource-intensive as sequences under consideration
become more complicated. The second reason is conceptual: For a ±1-valued
sequence a with mean Ma = 0, noncorrelation is tantamount to equidistribution of
the pairs a(n), a(n + m). More precisely, for each m ∈ N, if we additionally assume
that the limits mentioned above exist then γa(m) = 0 if and only if

lim
N →∞ |{n < N | a(n) = i, a(n + m) = i′}|
N = 1
4 for all i, i′ ∈ {+1, −1}.

The analogous characterisation is false without the assumption that a is allowed to
take more than 2 values.

2.2. Automatic sequences. In this section we brieﬂy discuss the basics of the
theory of automatic sequences; for extensive background see [AS03a]. For i ∈ Σk,
we deﬁne the operators Λi acting on sequences N0 → C by

(7) Λia(n) = a(kn + i).

The k-kernel of a sequence a : N0 → C consists of all sequences N0 → C that can
be obtained from a by repeated application of Λi’s, that is,

(8) Nk(a) = {n ↦→ a(kαn + r) | α, r ∈ N0, 0 ≤ r < kα} ⊆ CN0.

It will also be convenient to introduce the shift operator S acting on sequences
N0 → C by Sa(n) = a(n + 1). For future reference, we record how the introduced
operators interact.

Lemma 2.4. For each 0 ≤ i < k−1 we have ΛiS = Λi+1. Moreover, Λk−1S = SΛ1.

Proof. Direct computation. □

A sequence a is k-automatic (or just automatic, if k is clear from the context) if
and only if Nk(f ) is ﬁnite. Many equivalent deﬁnitions of automaticity are possible,
and we brieﬂy mention some of them to provide context. Details and terminology
can be found in [AS03a]. As the name suggests, a sequence is k-automatic if and
only if it is computed by a deterministic ﬁnite k-automaton with output. Any ﬁxed
point of a k-uniform morphism is k-automatic, and conversely any k-automatic
sequence can be obtained as a letter-to-letter coding of a ﬁxed point of a k-uniform

NONCORRELATED PATTERN SEQUENCES 7

morphism. When k is a prime and a is a sequence taking values in a ﬁnite ﬁeld F
of characteristic k, yet another criterion due to Christol shows that a is automatic
if and only if the associated formal power series is algebraic over F.
It is a well-known fact that the class of k-automatic complex-valued sequences is
closed under addition, multiplication, conjugation and restriction to subsequences,
that is, if a, b : N0 → C are k-automatic, then so are n ↦→ a(n)+b(n), n ↦→ a(n)·b(n),
n ↦→ a(n) and n ↦→ a(An + B) for any A ∈ N, B ∈ N0. More generally, if
a, b : N0 → C are k-automatic and h : C2 → C is arbitrary, then the sequence
n ↦→ h(a(n), b(n)) is k-automatic.
For a sequence a : N0 → C, we deﬁne the mean and the logarithmic mean:

(9) Ma := lim
N →∞ 1
N
 N −1∑

n=0 a(n), M
log
a := lim
N →∞ 1
log N
 N −1∑

n=0
 1
n + 1 a(n).

We note that Ma are not guaranteed to exist, even when the sequence a is automatic.
(Consider, for instance, the sequence deﬁned by a(0) = 0 and a(n) = (−1)
α if
kα ≤ n < kα+1, α ∈ N0.) On the other hand, we have the following positive result
for logarithmic means.

Theorem 2.5 ([AS03a, Thm. 8.4.8]). Let a : N0 → C be a k-automatic sequence.
Then M
log
a exists.

We also record the fact that that if a : N0 → C is a bounded sequence and Ma
exists then M
log
a also exists and M
log
a = Ma, see e.g. [AS03a, Prop. 8.4.4 (a)].
Pattern sequences are, unsurprisingly, automatic. In fact, we have the follow-
ing characterisation of pattern sequences in terms of their k-kernels (cf. [ZPK18,
Lemma 2.2]).

Lemma 2.6. Let a : N0 → {+1, −1} be a sequence with a(0) = +1 and ℓ ∈ N.
Then the following conditions are equivalent:
(i) There exists a set A ⊆ Σℓ
k \ {0ℓ} with a = aA.
(ii) For each b ∈ Nk(a), the sequence b/a has period kℓ−1.

Proof. (i) ⇒ (ii): Let i ∈ Σk and n ∈ N0. Then each factor of (n)k is also a factor
of (kn + i)k = (n)ki and conversely each factor of (kn + i)k that is not a suﬃx is a
factor of (n)k. More precisely, for each v ∈ Σ∗
k \ {0}∗ we have

#(v, kn + i) =
 {#(v, n) + 1 if v is a suﬃx of 0|v|−1(kn + i)k,
#(v, n) otherwise.

Consequently, Λia(n)/a(n) = −1 if the suﬃx of 0ℓ−1(kn + i)k of length ℓ belongs
to A and Λia(n)/a(n) = +1 otherwise. It follows that hi := Λia/a is kℓ−1-periodic.
Since for each i ∈ Σi, the operator Λi maps kℓ−1-periodic sequences to kℓ−2-periodic
sequences (or constant sequences, if ℓ = 1), it follows that all sequences in the k-
kernel of a take the form a · h where h is kℓ−1-periodic.
(ii) ⇒ (i): For each i ∈ Σk, let hi := Λia/a. Note that h0(0) = a(0)/a(0) = +1
and that the sequences hi take values in {+1, −1}. Conversely, given any k-tuple
of kℓ−1-periodic {+1, −1}-valued sequences h′
i (i ∈ Σk) with h′
0(0) = +1, we can
inductively construct a sequence a : N0 → {+1, −1} with a(0) = +1 and hi = h′
i
for all i ∈ Σk. Hence, the number of sequences that satisfy (ii) is
(2kℓ−1 )k−1 · 2kℓ−1−1 = 2kℓ−1.

8 J. KONIECZNY

On the other hand, the number of subsets of Σℓ
k \ {0ℓ} is also equal to 2kℓ−1, and
by the previously proven implication and Lemma 2.2, each of these choices gives
rise to a diﬀerent sequence satisfying (ii). It follows that each sequence satisfying
(ii) has a representation as in (i). □

2.3. Regular sequences. The class of k-regular sequences was introduced by Al-
louche and Shallit [AS92, AS03b] as a natural generalization of the class of k-
automatic sequences.
Let R be a ring contained in C. A sequence f : N0 → C is (R, k)-regular if Nk(f )
is contained in a ﬁnitely generated R-module. Note that if R′ ⊆ C is another ring
and R ⊆ R′ then any (R, k)-regular sequence is also (R′, k)-regular. In our context,
the choice of the ring R does not play a major role: For the sake of brevity, we
set R = Q throughout the paper and omit R from the notation. (Strictly speaking
we could have worked with R = Z[1/k], making some results marginally stronger.)
The fact that the ring under consideration is in fact a ﬁeld leads to a slightly more
succinct deﬁnition of regularity: A sequence f : N0 → C is k-regular if and only if
its k-kernel spans a ﬁnite dimensional vector space over Q: dim spanQ Nk(f ) < ∞.
The class of k-regular sequences enjoys closure properties analogous to k-automatic
sequences: If f, g : N0 → C are k-regular, then so are n ↦→ f (n) + g(n), n ↦→
f (n) + g(n), n ↦→ f (n), n ↦→ zf (n) (z ∈ C) and n ↦→ f (An + B) (A ∈ N, B ∈ N0).
In particular, k-regular sequences N0 → C form an involutive algebra over C (with
addition and multiplication deﬁned pointwise).
We will need a method to verify if a given regular sequence is identically zero.
The following lemma provides a simple criterion.

Lemma 2.7. Let f : N0 → C be k-regular and non-zero. Then there exists g ∈
Nk(f ) with g(0) ̸= 0.

Proof. For the sake of contradiction, suppose that g(0) = 0 for all g ∈ Nk(f ). We
show by induction on α that g(n) = 0 for all g ∈ Nk(f ) and 0 ≤ n < kα. If α = 0
then n = 0, so there is nothing to prove. If α > 0 and n < kα then n = kn′ +i where
i ∈ Σk and n′ < kα−1. Hence, g(n) = Λig(n′) = 0 by the inductive assumption. □

2.4. Invariant sequences. We will say that a sequence a : N0 → C is dilation-
invariant if a(kn) = a(n) for all n ∈ N0. The dilation-invariant pattern sequences
admit a simple description. Following the convention in Section 2.1, we will say
that a set A ⊆ Σ∗
k has no trailing zeros if 0 is not a suﬃx of any v ∈ A.

Lemma 2.8. Let a : N0 → {+1, −1} be a pattern sequence. Then a is dilation-
invariant if and only if there exists a set A ⊆ Σ∗
k that has no leading and no trailing
zeros and such that a = aA.

Proof. If A ⊆ Σ∗
k has no trailing zeros then #(v, n) = #(v, kn) for all v ∈ A and
n ∈ N0, so aA is dilation-invariant.
Conversely, suppose that a is dilation-invariant and let A ⊆ Σ∗
k be a set of
patterns without leading zeros such that a = aA, which exists by Lemma 2.2.
Suppose for the sake of contradiction that A contains a pattern ending with 0, say
u0 ∈ A for some u ∈ Σ∗
k, and let u be as short as possible. Since a is dilation-
invariant, we have

(10) a([u0]k) = a([u]k).

NONCORRELATED PATTERN SEQUENCES 9

On the other hand, each v ∈ A either ends in a non-zero digit (in which case
#(v, u0) = #(v, u)), or ends in 0 and is not a factor or u0 (in which case #(v, u0) =
#(v, u) = 0), or is equal to u0 (in which case #(v, u0) = 1 and #(v, u) = 0). As a
consequence,

(11) a([u0]k) = (−1)
#(A,u0) = (−1)
#(A,u)+1 = −a([u]k),

which contradicts (10) and ﬁnishes the argument. □

We also record the fact that every pattern sequence is the product of a dilation-
invariant sequence and a periodic sequence. As we will see (cf. Remark 5.6) the
introduction of the multiplicative factor aﬀects the correlation coeﬃcients in a rel-
atively simple way, which motivates our focus on dilation-invariant sequences.

Lemma 2.9. Let ℓ ∈ N0 and let a : N0 → {+1, −1} be a pattern sequence of length
≤ ℓ. Then there exist a unique dilation-invariant pattern sequence of length ≤ ℓ
such that a/b is kℓ−1-periodic.

Proof. By Lemma 2.2, we may assume that a = aA for a set A ⊆ Σ∗
k without
leading zeros. Reasoning along similar lines as in the proof of Lemma 2.2, we note
that for any word v, we have

k−1∑

i=0 #(vi, n) − #(v, n) =
 {1 if v is a suﬃx of n,
0 otherwise.

In particular, letting D(v) := {vi | i ∈ Σk} ∪ {v}, we see that the sequence aD(v)
is k|v|-periodic. We construct a sequence of sets A := A0, A1, . . . , At =: B, where
Aj+1 = Aj ⊕D(v) if Aj contains the word v0 for some v ∈ Σ∗
k and t is the ﬁrst index
such that no word in At ends with 0. This construction is guaranteed to terminate
because each step decreases the total length of words in Aj that end with 0. Letting
b := aB we observe that a/b is the product of kℓ−1-periodic sequences and hence
kℓ−1-periodic. □

3. Correlation coefficients

In this section we study correlation coeﬃcients of k-automatic sequences and
show that they are k-regular (Corollary 3.5). This allows us to reduce the task
of verifying if a given k-automatic sequence is noncorrelated to checking if a given
k-regular sequence is identically zero on N, which can be accomplished with the
help of Lemma 2.7.

3.1. Deﬁnitions. For two sequences a, b : N0 → C, we deﬁne the correlation coef-
ﬁcients:

(12) γa,b(m) := lim
N →∞ 1
N
 N −1∑

n=0 a(n)b(n + m),

if the limit exists (otherwise, γa,b(m) is considered undeﬁned). We are often inter-
ested in the case where a = b, when we write γa in place of γa,a. Unfortunately, the
limit deﬁning γa,b(m) is not guaranteed to converge even if a and b are automatic.
This motivates us to consider the logarithmic correlation coeﬃcients, deﬁned by

(13) γlog
a,b (m) := lim
N →∞ 1
log N
 N −1∑

n=0
 1
n + 1 a(n)b(n + m),

10 J. KONIECZNY

If a and b are automatic and m ∈ N0, then the sequence n ↦→ a(n)b(n + m) is
also automatic. Since Theorem 2.5 guarantees existence of logarithmic means of
automatic sequences, we have the following fact.

Corollary 3.1. Let a, b : N0 → C be k-automatic sequences. Then the coeﬃcients
γlog
a,b (m) are well-deﬁned for all m ∈ N0. Moreover, if the coeﬃcient γa,b(m) is

well-deﬁned for some m ∈ N0 then γa,b(m) = γlog
a,b (m).

3.2. Recurrence. Our next goal is to obtain a recursive description of the corre-
lation coeﬃcients discussed above. Recall that for a k-automatic sequence a, the
kernel Nk(a) is ﬁnite and closed under the operators Λi deﬁned in (7) for all i ∈ Σk.

Lemma 3.2. Let N be a ﬁnite set of sequences N0 → C, closed under the operators
Λi for all i ∈ Σk. Then for all a, b ∈ N it holds that

(14) γlog
a,b (m) = 1
k
 k−1∑

i=0 γlog
a′
i,b′
i (m′
i),

where a′
i, b′
i and m′
i are given by

(15) a′
i = Λia, b′
i = Λm+i mod kb, m′
i = ⌊ m + i
k
 ⌋ .

Proof. Rescaling if necessary, we assume that all sequences in N are 1-bounded
(that is, |a(n)| ≤ 1 for all a ∈ N and n ∈ N0). For each N > 0, splitting [N ] into
residue classes modulo k we obtain

N −1∑

n=0
 a(n)b(n + m)
n + 1 =
 k−1∑

i=0
 ⌊N/k⌋−1∑

n=0
 a(kn + i)b(kn + i + m)
kn + i + 1 + O ( 1
N
 ) .

= 1
k
 k−1∑

i=0
 ⌊N/k⌋−1∑

n=0
 a′
i(n)b′
i(n + m′
i)
n + 1 + O (1) ,

where a′
i, b′
i and m′
i are given by (15), and we use the estimate 1/ (kn + i + 1) =
1/k(n + 1)+O(1/(n+1)
2) together with the fact that ∑∞
n=0 1/(n+1)
2 is summable.
Dividing by log N and recalling that 1/ log(N/k) = 1/ log N + O(1/ log2 N ) we
obtain

1
log N
 N −1∑

n=0
 a(n)b(n + m)
n + 1 = 1
k
 k−1∑

i=0
 1
log ⌊N/k⌋
 ⌊N/k⌋−1∑

n=0
 a′
i(n)b′
i(n + m′
i)
n + 1 + O ( 1
log N
 ) .

Letting N → ∞, we obtain (14). □

While the coeﬃcients γlog
a,b (m) are better-behaved in general, our original moti-
vation concerns the coeﬃcients γa,b(m) (where additionally a = b). Fortunately,
existence of the latter is easy to ensure under mild additional assumptions.

Lemma 3.3. Let N be a ﬁnite set of sequences N0 → C, closed under the operators
Λi for all i ∈ Σk. Suppose that γa,b(0) exists for each a, b ∈ N . Then also γa,b(m)
exists for all a, b ∈ N and m ∈ N0 and, using the notation from (15), satisfy

(16) γa,b(m) = 1
k
 k−1∑

i=0 γa′
i,b′
i(m′
i),

NONCORRELATED PATTERN SEQUENCES 11

Proof. Rescaling if necessary, we may assume that all sequences in N are 1-bounded.
Generalizing the deﬁnition of γa,b(m) slightly, for x ≥ 1 let us put

(17) γa,b(m; x) = 1
⌊x⌋
 ⌊x⌋−1∑

n=0 a(n)b(n + m).

Then, following the same reasoning as in Lemma 3.2, we ﬁnd the recursive relation

(18) γa,b(m; x) = 1
k
 k−1∑

i=0 γa′
i,b′
i(m′
i; x/k) + O(1/x),

where a′
i, b′
i and m′
i are given by (15).
In particular, for m = 1 we obtain

(19) γa,b(1; x) = 1
k
 k−2∑

i=0 γa′
i,b′
i(0; x/k) + 1
k γa′
k−1,b′
k−1 (1; x/k) + O(1/x).

Iterating (19) t times, we conclude that there exist weights w(t)
a′,b′ ≥ 0 (a′, b′ ∈ N )

with ∑

a′,b′∈N w(t)
a′,b′ = 1 − 1/kt and sequences a(t), b(t) ∈ N such that

(20) γa,b(1; x) = ∑

a′,b′∈N w(t)
a′,b′γa′,b′(0; x/kt) + 1
kt γa(t),b(t) (1; x/kt) + O(kt/x).

Since γa′,b′ (0; y) → γa′,b′ (0) as y → ∞ for each a′, b′ ∈ N , letting x → ∞ in (20)
we conclude that there exists a number γ(t)
a,b(1) = ∑a′,b′∈N w(t)
a′,b′ γa′,b′ (0) such that

(21) lim sup
x→∞
 ∣
∣
∣γa,b(1; x) − γ(t)
a,b(1)
∣
∣
∣ = O(1/kt).

It follows that the sequence γ(t)
a,b(1) (t ∈ N) is Cauchy, and γa,b(1) is well-deﬁned:

(22) γa,b(1) = lim
x→∞ γa,b(1; x) = lim
t→∞ γ(t)
a,b(1).

We are now ready to prove by induction on m that the coeﬃcients γa,b(m) are
well-deﬁned for all m ∈ N0 and a, b ∈ N . The case m = 0 is included in the
assumptions, and we have dealt with m = 1 above. Suppose now that m ≥ 2. For
each i ∈ Σk, since ⌊x/k⌋ ≤ x/k < x for all x > 0, we have

(23) m′
i = ⌊ m + i
k
 ⌋ ≤ ⌊ m + k − 1
k
 ⌋ = ⌊ m − 1
k
 ⌋ + 1 < (m − 1) + 1 = m.

Hence, existence of γa,b(m) follows from (19) and the inductive assumption. Finally,
to obtain (16) it remains to pass to the limit x → ∞ in (18) (or use Lemma 3.2
combined with the remark after Theorem 2.5). □

3.3. Regularity. We are now ready to show that the logarithmic correlation se-
quences coming from k-automatic sequences are k-regular. In fact, bearing in mind
applications in Section 4 we record a slightly more precise statement. Recall that
for a sequence a, the sequence Sa is given by Sa(n) = a(n + 1). Similar ideas can
be seen in [AS03b, Thm. 6].

Proposition 3.4. Let N be a ﬁnite set of sequences N0 → C, closed under the op-
erators Λi for all i ∈ Σk. Let M = {
Seγlog
a,b ∣
∣
∣ a, b ∈ N , e ∈ {0, 1}}
. Then spanQ M
is closed under the operators Λi for all i ∈ Σk.

12 J. KONIECZNY

Proof. Pick any g = Seγlog
a,b ∈ M (a, b ∈ N , e ∈ {0, 1}) and j ∈ Σk. It follows from
Lemma 3.2 that

(24) Λjg(n) = γlog
a,b (kn + j + e) = 1
k
 k−1∑

i=0 γlog
a′
i,b′
i (n + e′
i)

where for each i ∈ Σk, a′
i, b′
i ∈ N and

e′
i = ⌊ j + i + e
k
 ⌋ ≤ ⌊ (k − 1) + (k − 1) + 1
k
 ⌋ = 1.

It remains to note that each of the functions of n appearing under the sum on the
right hand side of (24) belongs to M. □

Theorem 3.5. If a : N0 → C is k-automatic then the sequence γlog
a is k-regular
and dim spanQ Nk(γlog
a,a) ≤ 2 |Nk(a)|2.

4. Verifying noncorrelation

We now discuss the practical details of how one can check if a given pattern
sequence is noncorrelated. We begin by setting up the notation and adapting
the general results from previous sections to the situation at hand; this is done in
subsections 4.1 and 4.2. Then, in subsections 4.3 and 4.4 we discuss how the relevant
computations can be performed. Finally, in subsection 4.5 we discuss the complexity
of the resulting algorithm, which ﬁnishes the proof of Theorem B. Implementation
of this algorithm allows us to verify Theorem A by direct computation.

4.1. Setup. Throughout this section, A ⊆ Σℓ
k denotes an admissible set and a : N0 →
{+1, −1} denotes the corresponding pattern sequence:

a(n) = aA(n) = (−1)
#(A,n) (n ∈ N0).

We also introduce the sequence f : N0 → R given by

f := 1N · γa.

Our task amounts to verifying that f is well-deﬁned (i.e., that the limits deﬁning
γa(m) exist for all m ∈ N) and determining whether it is identically zero. The
existence question is easily accounted for (cf. [ZPK18, Section 3]).

Lemma 4.1. For each b, c ∈ Nk(a) and m ∈ N0, the coeﬃcient γb,c(m) exists.

Proof. By Lemma 2.6, all sequences in Nk(a) are products of a and kℓ−1-periodic se-
quences. Hence, there is a kℓ−1-periodic sequence h such that b(n)c(n) = a(n)
2h(n) =
h(n) for all n ∈ N0, and consequently

γb,c(0) = lim
N →∞ 1
N
 N −1∑

n=0 h(n) = 1
kℓ−1
 kℓ−1−1∑

n=0 h(n)

exists. Existence of γb,c(m) for m ∈ N now follows from Lemma 3.3. □

Recall that f = 1N · γlog
a is k-regular by Theorem 3.5. In principle, in order to
decide if f is identically zero, it is now enough to follow the arguments in Section
3 to describe the structure of the k-kernel of f and then apply Lemma 2.7. In
practice, we essentially follow this route, but we also take advantage of the fact
that f is a k-regular sequence of a rather speciﬁc form.

NONCORRELATED PATTERN SEQUENCES 13

4.2. Recursive relations. As a ﬁrst step towards describing the recursive rela-
tions that deﬁne f , we introduce a set that spans Nk(f ), in analogy to Proposition
3.4. It will be convenient to introduce the restricted averages

(25) γ(r)(m) := lim
N →∞ kℓ

log N
 N −1∑

n=0
 1
n + 1 a(n)a(n + m)1kℓN0+r(n).

Note that these averages are well-deﬁned thanks to Theorem 2.5. Additionally,
it follows from Lemma 2.6 and Lemma 4.1 that the logarithmic averages can be
replaced with unweighted averages:

(26) γ(r)(m) = lim
N →∞ kℓ

N
 N −1∑

n=0 a(n)a(n + m)1kℓN0+r(n).

As a direct consequence of the relevant deﬁnitions, we have

(27) f = 1N
kℓ ·
 kℓ−1∑

r=0 γ(r) = 1
kℓ
 kℓ
∑

q=1
 kℓ−1∑

r=0 1kℓN0+q · γ(r).

Proposition 4.2. Each sequence in Nk(f ) is a linear combination of the sequences
1kℓN0+q · Seγ(r), where e ∈ {0, 1}, 0 ≤ r < kℓ and 0 ≤ q ≤ kℓ. In particular,
dim spanQ Nk(f ) ≤ 2kℓ(kℓ + 1).

The proof of the above proposition will follow directly once we describe the
behaviour of the base sequences 1kℓN0+q · Seγ(r) under the operators Λi (i ∈ Σk).
To simplify this description, it will be convenient to introduce the auxiliary sequence
h : N0 → {+1, −1}, given by

(28) h(n) := a(n)/a(⌊n/k⌋).

The following basic fact is analogous to [ZPK18, Lemma 2.1].

Lemma 4.3. The sequence h given by (28) is kℓ-periodic.

Proof. Follows immediately from Lemma 2.6. □

Lemma 4.4. Let e ∈ {0, 1}, i ∈ Σk, 0 ≤ q ≤ kℓ and 0 ≤ r < kℓ. If i ̸= q mod k
then Λi1kℓN0+q = 0. If i = q mod k then

(29) Λi (
1kℓN0+q · Seγ(r)) = h(r)h(r + q + e)
k
 ∑

q′
 ∑

r′ 1kℓN0+q′ · Se
′γ(r′),

where the value of e and the ranges of the summations are given by

e′ := ⌊ i + e + (r mod k)
k
 ⌋ , q′ ∈ kℓ−1Σk + ⌊q/k⌋ , r′ ∈ kℓ−1Σk + ⌊r/k⌋ .

Proof. The case e = 0 follows by a standard adaptation of the proof of Lemma 3.2.
Then, the case e = 1 is derived using Lemma 2.4. □

14 J. KONIECZNY

4.3. Small shifts. Bearing in mind that we hope to apply Lemma 2.7, we need
to be able to compute the values Seγ(r)(0) = γ(r)(e) for e ∈ {0, 1} and 0 ≤ r ≤
kℓ. This can, in principle, be accomplished by straightforward adaptations of the
arguments in Lemma 3.3 and Lemma 4.1. Here, we discuss the practical details of
how the computations are performed. Recall that γ(r)(0) = 1, so we only need to
compute γ(r)(1).
For 0 ≤ r < kℓ, let ν = ν(r) denote the ﬁrst position where a digit distinct from
k − 1 appears in the base-k expansion (r)k; if r = kα − 1 for some α ≥ 0 then ν = α.
We consider r in nondecreasing order with respect to ν(r). We have three ranges
to consider: r = 0, 1 ≤ r < ℓ and r = ℓ.
If ν(r) = 0 then it follows from Lemma 4.4 that

(30) γ(r)(1) = h(r)h(r + 1)
k
 ∑

r′ γ(r′)(0) = h(r)h(r + 1);

here and elsewhere, the summation over r′ runs through r′ ∈ kℓ−1Σk + ⌊r/k⌋. Since
we can readily compute h(r) and h(r + 1), we can compute γ(r)(1).
If 1 ≤ ν(r) < ℓ then another application of Lemma 4.4 yields

(31) γ(r)(1) = h(r)h(r + 1)
k
 ∑

r′ γ(r′)(1).

For all r′ appearing in the above sum we have ν(r′) = ν(r) − 1, and hence γ(r′)(1)
has been previously computed. Hence, again, we can directly compute γ(r)(1).
Finally, if ν = ℓ (meaning that r = kℓ − 1) then (31) continues to hold, and
we have ν(r′) = ℓ − 1 for all summands on the right-hand-side except for the one
corresponding to r′ = r. Hence, we can compute γ(r) as

(32) γkℓ−1(1) = 1
kh(r)h(r + 1) − 1
 k−2∑

i=0 γkℓ−2(ki+1)−1(1).

4.4. Basis construction. Recall that our general strategy calls for a construction
of a spanning set of spanQ Nk(f ). For technical reasons, it appears to be slightly
more convenient and eﬃcient to instead work with the potentially larger space

M := spanQ {1kℓN0+q · g ∣
∣ g ∈ Nk(f ), 0 ≤ q ≤ kℓ} .

It remains true that f = 0 if and only if M = {0}, and that M is closed under Λi
for all i ∈ Σk. Additionally, M admits a decomposition

M =
 kℓ
⊕

q=0 Mq, Mq := ηq · spanQ Nk(f ),

where the sequences ηq are given by

η0 = 1{0}, ηq = 1kℓN0+q for 1 ≤ q ≤ kℓ.

By Lemma 2.7, to show that M = {0} it suﬃces to verify that g(0) = 0 for each
g ∈ M, which is trivially satisﬁed for g ∈ Mq for all 1 ≤ q ≤ kℓ.
We proceed to construct a list of sequences f1, f2, · · · ∈ M which spans M.
Additionally, we ensure that for each t ≥ 1, the sequence ft belongs to Mqt for

NONCORRELATED PATTERN SEQUENCES 15

some 0 ≤ qt ≤ kℓ and we keep track the value of qt. By Proposition 4.2, each ft
has a decomposition

(33) ft =
 kℓ−1∑

r=0
 1∑

e=0 w(t)
r,eηtSeγ(r),

for some coeﬃcients w(t)
r,e, which we also keep track of. While we cannot ensure that
f1, f2, . . . are linearly independent (in fact, we are primarily interested in the case
when f1 = f2 = · · · = 0), we will ensure that for each 1 ≤ q ≤ kℓ, the (multi-)set of
coeﬃcient vectors {w(t) ∣
∣ qt = q} ⊆ R2kℓ is linearly independent.
We start by setting for 1 ≤ t ≤ kℓ,

(34) ft = 1kℓN0+t ·
 kℓ
∑

r=0 γ(r), qt = t,

and accordingly w(t)
r,e = 1{0}(e) (0 ≤ r < kℓ, e ∈ {0, 1}).
Suppose next that at a certain stage we have constructed f1, f2, . . . , fv and that
for all 1 ≤ t ≤ u we have ensured that Λift ∈ spanQ{f1, f2, . . . , fv} for all i ∈ Σk.
(Initially, v = kℓ and u = 0.) If u = v then spanQ{f1, f2, . . . , fv} is a subset of M
that is closed under Λi (i ∈ Σk) and under multiplication by 1kℓN0+q (0 ≤ q ≤ kℓ),
hence spanQ{f1, f2, . . . , fv} = M and the construction is complete.
Let us next consider the case when u < v. Put q = qu+1, g = fu+1 and
w = w(u+1). Recall that the only value of i for which Λig could be non-zero is
i = q mod k. If q = 0 then g = g(0)1{0}. Hence, either g(0) ̸= 0, in which case
a is not noncorrelated and we are done; or g(0) = 0, in which case g = 0 and so
Λig = 0 as well. Suppose now that 1 ≤ q ≤ kℓ. Applying Lemma 4.4, we obtain a
representation of Λig in the form

(35) Λig = ∑

q′
 ∑

r′
 ∑

e′ w′
q′,r′,e′ 1kℓN0+q′ · Se
′γ(r′),

where the ranges of summation are given by 0 ≤ q′ ≤ kℓ, 0 ≤ r′ < kℓ and 0 ≤ e′ ≤ 1,
and the coeﬃcients w′ are given by explicit formulae coming from (29). Bearing in
mind that 1kℓN0 = 1kℓN + 1{0}, we ﬁnd the decomposition

(36) Λig = ∑

q′ g′
q′ , g′
q′ = ∑

r′
 ∑

e′ w′′
q′,r′,e′ ηq′ Se
′ γ(r′),

where the coeﬃcients w′′
q′,r′,e′ are given by:

w′′
q′,r′,e′ = w′
q′,r′,e′ if q′ ̸= kℓ, w′′
kℓ,r′,e′ = w′
kℓ,r′,e′ + w′
0,r′,e′.(37)

For each q′, we append g′
q′ to the list f1, f2, . . . , fv if (and only if)

(38) (
w′′
q′,r′,e′ )

r′,e′ ̸∈ spanQ
 {(w(t)
r,e)

r,e
 ∣
∣
∣
∣ 1 ≤ t ≤ v, qt = q′} .

If (38) holds then we also record g′
q′ ∈ Mq′ (that is, we append q′ to the list
q1, q2, . . . , qv) and that the decomposition of g′
q′ as the sum of basis sequences is
given by (36) (what is, we append w′′
q′ to the list w(1), w(2), . . . , w(v). Each time
a new sequence is added, v increases by 1 and after all q′ have been processed, u
increases by 1.

16 J. KONIECZNY

The linear independence condition (38) ensures that for each 1 ≤ q ≤ kℓ, there
are at most 2kℓ values of t with qt = q, and hence the construction needs to
terminate after a bounded number of steps. As the result, we either ﬁnd, for some
t ≥ 1, a sequence ft ∈ M with ft(0) ̸= 0 (in which case a is not noncorrelated)
or we construct a ﬁnite list of sequences f1, f2, . . . , fN ∈ M that spans M and
satisﬁes ft(0) = 0 for all 1 ≤ t ≤ N (in which case a is noncorrelated). In either
case, we are able to determine whether a is noncorrelated.

4.5. Complexity. We now provide quantitative estimates for the amount of com-
putational power needed to verify if the pattern sequence a is noncorrelated using
the method described above. Throughout, we treat k as ﬁxed, and hence are in-
terested in the regime ℓ → ∞. It will be convenient to introduce, for a function
F : N → R>0, the shorthand ̃O(F (ℓ)) to denote O(ℓO(1)F (ℓ)). Thus, for instance,
addition or multiplication of two integers of size O(kℓ) can be performed using ̃O(1)
operations.
At several points, we need to compute the values of a(n) where n = O(kℓ). For
a word w ∈ Σ∗
k with length |w| ≤ ℓ, computing #(n, w) directly from the deﬁnition
requires ̃O(1) operations. Since |A| ≤ kℓ, the values #(n, A) and a(n) can be
computed in time ̃O(kℓ) . Consequently, we can also compute h(n) in time ̃O(kℓ).
Following the steps in subsection 4.3, we compute γ(r)(1) for all 0 ≤ r < kℓ. It
takes ̃O(kℓ) operations to write the values of r (0 ≤ r < kℓ) in an order consistent
with ν(r). Note that each of the formulae (30), (31), (32) produces the correspond-
ing value of γ(r)(1) using ̃O(1) arithmetic operations on rational numbers. One
can also check by a simple inductive argument that all denominators and numer-
ators that appear in these computations are bounded by O(kℓ), and hence each
arithmetic operation takes only ̃O(1) basic operations. We also note that all the
denominators take the form (k ± 1)kα.
We next proceed to the computation of the sequences ft (t = 1, 2, 3, . . . ) in
subsection 4.4. Strictly speaking, we compute the sequence w(t), which uniquely
determine ft via (33), and the auxiliary sequence qt. For t ≤ kℓ, the explicit
formula (34) allows us to compute w(t) and qt with ̃O(k2ℓ) operations (note that
w(t) = (
w(t)
r,e)

r,e has k2ℓ entries, so this is the least number of operations possible).
Let us now consider the amount of computation required to compute ft for
t > kℓ. Consider any u, v, as in the iterative procedure in second half of subsection
4.4. We note that the application of Lemma 4.4 used to compute w′ in (35) requires
no more than ̃O(k3ℓ) arithmetic operations (for each of O(kℓ) summands in the
decomposition of g, we substitute a sum of size O(k2ℓ)). Once w′ is computed, it
only takes ̃O(k2ℓ) operations to compute w′′. Then, for each of O(kℓ) values of q′,
in order to verify if g′
q′ should be appended to the list f1, f2, . . . , we need to verify
if the corresponding vector of coeﬃcients belongs to a certain linear subspace of
R2kℓ, see (38). Keeping track of how much the complexity increases in each step
of the construction, we see that for each t > kℓ, the entries of w(t) are rational
numbers whose numerators are ̃O(k3t), and whose denominators are O(kt) and
divide (k2 − 1)kα for some integer α. Thus, in (38) we may scale all of the relevant
vectors by a factor of (k2−1)kO(u), leaving us with the task of verifying if an integer-
valued vector belongs to the span of other integer-valued vectors. The latter task is
well-known to have polynomial complexity (with respect to dimensions and lengths

NONCORRELATED PATTERN SEQUENCES 17

of representations of entries), see e.g. [BCS97, Chpt. 16]. Hence, for each q′ in
order to decide if g′
q′ should appended, we perform ̃O(kO(ℓ)) = kO(ℓ) operations.
Consequently, the number of operations needed to process the step corresponding
to the index u is kO(ℓ).
Because of the linear independence conditions discussed at the end of subsection
4.4, the total number of the sequences f1, f2, . . . we construct is at most 2k2ℓ+1. It
follows that in total, we perform at most kO(ℓ) operations.

5. Dilation-invariant sequences

We now turn to the classiﬁcation of dilation-invariant pattern sequences. Through-
out, let A ⊆ Σ∗
k be a set of patterns with no leading or trailing zeros, and let a = aA
be the corresponding pattern sequence. We also retain the notation from Section
4, speciﬁcally the coeﬃcients γr deﬁned in (25). We let ℓ = maxv∈A |v| denote the
length of a, and we assume that ℓ ≥ 2.
The following condition turns out to be closely connected to the question of
whether a is noncorrelated:

(†) ∣
∣A(ui0)
−1 ⊕ A(ui1)
−1∣
∣ = k
2 for each u ∈ Σℓ−2
k and i0, i1 ∈ Σk with i0 ̸= i1.

Above, using the standard notation from semigroup theory, for a word u ∈ Σ∗
k and
a set X ⊆ Σ∗
k, we let Xu−1 := {v ∈ Σ∗
k | vu ∈ X}.

Remark 5.1. The condition (†) can be stated in simpler terms when k = 2. Then,
necessarily, {i0, i1} = {0, 1} and since A has no trailing zeros, A0−1 = ∅. Hence,
(†) says that ∣
∣A(u1)
−1∣
∣ = 1 for all u ∈ Σℓ−2
k . Because all patterns in A have length
≤ ℓ, A(u1)
−1 ⊆ {0, 1}; and because A has no leading zeros, 0 ̸∈ A(u1)
−1. Thus,
(†) reduces to the statement that 1u1 ∈ A for all u ∈ Σℓ−2
k , that is, 1Σℓ−2
2 1 ⊆ A.
This is precisely the assumption that appears in Theorem C.

Remark 5.2. For general k ≥ 2, it is not a priori clear if there exists a set of
patterns A such that (†) holds. Fix u ∈ Σℓ−2
k and consider the matrix M =
(
M (u)
i,j )k−1
i,j=0 where M (u)
i,j = −1 if iuj ∈ A and M (u)
i,j = +1 otherwise. Then (†)
says that M TM = kI, where I denotes the identity matrix, meaning that M is a
Hadamard matrix. Additionally, M (u)
i,j = +1 if i = 0 or j = 0, meaning that M is
normalized. Conversely, given any normalized Hadamard matrix M ′, one can easily
reconstruct A so that M = M ′ for each choice of u ∈ Σℓ−2
k . Thus, it is possible
to satisfy the condition (†) if and only if there is at least one Hadamard matrix of
dimension k.
The question of existence of Hadamard matrices of a given dimension has long
been investigated. They are easily constructed when k is a power of 2 through a
tensor-power construction. More generally, given Hadamard matrices of dimensions
k and k′ one can construct a Hadamard matrix of dimension k · k′. It is conjectured
that Hadamard matrices exist for k = 1, 2 and all k divisible by 4. So far, this has
been conﬁrmed for k < 668. See e.g. [CD07, Chpt. V] for further discussion.

The main goal of this section is to prove a slightly more general variant of
Theorem C. The second part of this theorem asserts that if a is noncorrelated,
k = 2 and ℓ ≤ 5 then (†) holds. This is veriﬁed by exhaustive search
2, using the

2Code available from the author.

18 J. KONIECZNY

methods developed in Section 4. The remaining part of Theorem C follows from
the following result, whose proof will occupy the remainder of this section.

Proposition 5.3. Suppose that (†) holds. Then the sequence a is noncorrelated.

From this point onwards, assume that (†) holds. Proceeding along similar lines
as in Lemma 3.3 (or Section 4.3), we will compute γr(m) for small values of m ∈ N0
(0 ≤ r < kℓ). The following lemma is the main consequence of (†) that we use.

Lemma 5.4. Let u ∈ Σℓ−2
k and j0, j1 ∈ Σk, j0 ̸= j1. Then

(39)
 k−1∑

i=0 a ([iuj0]k) a ([iuj1]k) = 0.

Proof. Multiplying by a ([uj0]k) a ([uj1]k), we see that (39) is equivalent to

(40)
 k−1∑

i=0 a ([uj0]k) a ([uj1]k) a ([iuj0]k) a ([iuj1]k) = 0.

Each pattern v in A of length < ℓ and each i ∈ Σk, considering the diﬀerent
positions where v can appear, one can check that

#(v, uj0) + #(v, iuj1) = #(v, uj1) + #(v, iuj0).

Conversely, if v ∈ A and |v| = ℓ then

#(v, uj0) = #(v, uj1) = 0,

since |uj0| , |uj1| < ℓ, and for each i ∈ Σk

#(v, iuj0) + #(v, iuj1) =
 {
1 if v ∈ {iuj0, iuj1},
0 otherwise.

Substituting the above identities into the sum on the left-hand side of (39) and
applying (†) we conclude that

k−1∑

i=0 a ([iuj0]k) a ([iuj1]k) =
 k−1∑

i=0(−1)
#{iuj0,iuj1}∩A

= k − 2 ∣
∣A(uj0)
−1 ⊕ A(uj1)
−1∣
∣ = 0. □

Lemma 5.5. Let 0 ≤ r < kℓ and m ≥ 0. Put j = r mod k. Then

γr(m) =
 {a(r)a(r + m) if j + m < k and m ̸= 0,
0 otherwise.

Proof. Let us write m = km′ + i with m′ ≥ 0 and i ∈ Σk. Then by Lemma 4.4 (or,
equivalently, by Lemma 3.2) we have

(41) γr(m) = γr(km′ + i) = h(r)h(r + km′ + i)
k
 ∑

r′ γr′ (m′ + e′),

where as usual r′ ∈ kℓ−1Σk + ⌊r/k⌋ and e′ = ⌊(i + j)/k⌋ ∈ {0, 1}. We consider
several diﬀerent cases.
Case 0: m = 0. It follows directly from the deﬁnition of γr that

γr(0) = 1 = a(r)
2 = a(r)a(r + m).

NONCORRELATED PATTERN SEQUENCES 19

Case 1: m ̸= 0 and j + m < k. Applying (41) and noticing that i = m, m′ = 0,
and e′ = 0, we obtain

(42) γr(m) = h(r)h(r + m) = a(r)a(r + m),

where the second equality holds because ⌊r/k⌋ = ⌊(r + m)/k⌋.
In all of the remaining cases, we will show that γr(m) = 0. We start with the
simplest situation where e′ = 1.
Case 2: m = 1 and j + m ≥ k, meaning that j = k − 1. Let ν(r) denote the ﬁrst
position where a digit distinct from k − 1 appears in the expansion of r, allowing
ν(r) = α if r = kα − 1. By (41),

(43) γr(1) = ± 1
k
 ∑

r′ γr′(1).

If ν(r) = 1 then from the previously considered cases and Lemma 5.4 it follows that

γr(1) = ± 1
k
 ∑

r′ a(r′)a(r′ + 1) = 0.

If 1 < ν(r) < ℓ then ν(r′) = ν(r) − 1 for all r′ that enter the sum (43). Hence,
reasoning by induction on ν(r) we conclude that γr(1) = 0. Finally, if ν(r) = ℓ
then r = kℓ − 1, and ν(r′) = ℓ − 1 for all r′ that appear in the sum (43) except for
r′ = r. It follows that γkℓ−1(1) = ± 1
k γkℓ−1(1),

which is only possible if γkℓ−1(1) = 0.
Case 3: 2 ≤ m < k and j + m ≥ k. By (41) and Case 2,

(44) γr(m) = ± 1
k
 ∑

r′ γr′(1) = 0.

Case 4: k ≤ m < k2. By (41),

(45) γr(m) = ± 1
k
 ∑

r′ γr′(m′ + e′) = 0.

Let j′ := ⌊r/k⌋ mod r and i′ := m′ + e′. Note that r′ mod k = j′ for all r′ in the
sum in (45), where we are using the fact that ℓ ≥ 2. We have several subcases to
consider. If j′ + i′ < k then

γr(m) = ± 1
k
 ∑

r′ a(r′)a(r′ + i′) = 0

by Cases 0 and 1 and Lemma 5.4. If j′ + i′ ≥ k while i′ < k (i.e. m′ ̸= k − 1 or
e′ ̸= 1) then γr′(m′ + e′) = 0 for all r′ by Cases 2 and 3, and consequently also
γr(m) = 0. Finally, if j′ + i′ = k (i.e. m′ = k − 1 and e′ = 1) then

γr(m) = ± 1
k
 ∑

r′ γr′(k · 1 + 0) = 0

by the previously considered subcases.
Case 5: m ≥ k2. We reason by induction on m. By (41) and the inductive
assumption,

(46) γr(m) = ± 1
k
 ∑

r′ γr′(m′ + e′) = 0

20 J. KONIECZNY

since k ≤ m′ + e′ < m. □

Now that we have computed the values of the coeﬃcients γr(m), the remainder
of the argument is straightforward.

Proof of Proposition 5.3. We need to show that

γ(m) = 1
kℓ
 kℓ−1∑

r=0 γr(m) = 0

for all m ≥ 1. If m ≥ k there is nothing to prove since γr(m) = 0. Suppose
now that 1 ≤ m < k. We may write arbitrary 0 ≤ r < kℓ − 1 in the form
r = kℓ−1i + ks + j where i, j ∈ Σk and 0 ≤ s < kℓ−2. Then, γr(m) = 0 if j + m ≥ k
and γr(m) = a(r)a(r + m) otherwise. It follows that

γ(m) =
 k−m−1∑

j=0
 kℓ−1−1∑

s=0
 k−1∑

i=0 a (
kℓ−1i + ks + j) a (
kℓ−1i + ks + j + m) = 0,

where the inner-most sum vanishes by Lemma 5.4. □

Remark 5.6. Let a′ : N0 → {+1, −1} be a sequence such that a′/a is kℓ−1-periodic.
Then a′ is pattern by Lemma 2.2. Deﬁning γ′ and γ′
r in analogy to γ and γr, with
a′ in place of a, by a direct computation we show for all m ≥ 0 and 0 ≤ r < kℓ that

(47) γ′
r(m) = a′(r)a′(r + m)
a(r)a(r + m) γr(m) = ±γr(m).

It follows that γ′
r(m) = 0 for all m ≥ k. In particular, γ′(m) = 0 for all m ≥ k.
We check by exhaustive search that all noncorrelated binary pattern sequences
of length ≤ 4 can arise as a′ in the construction outlined above. It seems plausible
that the same holds for all lengths. If this is the case, and if Conjecture 1.1 holds
true, then the task of verifying if a given binary pattern sequence b′ is noncorre-
lated can be split into two independent steps: First, check if the dilation-invariant
sequence b obtained from b′ in Lemma 2.9 satisﬁes (†); if not then b′ is not noncor-
related
3. Second, check if the ± signs in (the analogue of) (47) align in a way that
ensures γb′(1) = 0. While the condition from the ﬁrst step is quite conceptual, it
appears that the second step relies mostly on arithmetic coincidence. This would
provide an intuitive explanation for why the results in the dilation-invariant case
are considerably more concise.
 References

[AL91] J.-P. Allouche and P. Liardet. Generalized Rudin-Shapiro sequences. Acta Arith.,
60(1):1–27, 1991.
[AS92] J.-P. Allouche and J. Shallit. The ring of k-regular sequences. Theoret. Comput. Sci.,
98(2):163–197, 1992.
[AS99] J.-P. Allouche and J. Shallit. The ubiquitous Prouhet-Thue-Morse sequence. In Se-
quences and their applications (Singapore, 1998), Springer Ser. Discrete Math. Theor.
Comput. Sci., pages 1–16. Springer, London, 1999.
[AS03a] J.-P. Allouche and J. Shallit. Automatic sequences. Cambridge University Press, Cam-
bridge, 2003. Theory, applications, generalizations.
[AS03b] J.-P. Allouche and J. Shallit. The ring of k-regular sequences. II. Theoret. Comput.
Sci., 307(1):3–29, 2003. Words.

3For the sake of simplicity, we work under the additional assumption that b and b′ have equal
lengths, which is not true in general.

NONCORRELATED PATTERN SEQUENCES 21

[BCM89] D. W. Boyd, J. Cook, and P. Morton. On sequences of ±1’s deﬁned by binary patterns.
Dissertationes Math. (Rozprawy Mat.), 283:64, 1989.
[BCS97] P. B¨urgisser, M. Clausen, and M. A. Shokrollahi. Algebraic complexity theory, vol-
ume 315 of Grundlehren der Mathematischen Wissenschaften [Fundamental Princi-
ples of Mathematical Sciences]. Springer-Verlag, Berlin, 1997. With the collaboration
of Thomas Lickteig.
[CD07] C. J. Colbourn and J. H. Dinitz, editors. Handbook of combinatorial designs. Discrete
Mathematics and its Applications (Boca Raton). Chapman & Hall/CRC, Boca Raton,
FL, second edition, 2007.
[CKMF77] J. Coquet, T. Kamae, and M. Mend`es France. Sur la mesure spectrale de certaines
suites arithm´etiques. Bull. Soc. Math. France, 105(4):369–384, 1977.
[Coq76] J. Coquet. Sur les fonctions q-multiplicatives pseudo-al´eatoires. C. R. Acad. Sci. Paris
S´er. A-B, 282(4):Ai, A175–A178, 1976.
[DMR19] M. Drmota, C. Mauduit, and J. Rivat. Normality along squares. J. Eur. Math. Soc.
(JEMS), 21(2):507–548, 2019.
[FM96] E. Fouvry and C. Mauduit. M´ethodes de crible et fonctions sommes des chiﬀres. Acta
Arith., 77(4):339–351, 1996.
[Gel68] A. O. Gel’fond. Sur les nombres qui ont des propri´et´es additives et multiplicatives
donn´ees. Acta Arith., 13:259–265, 1967/1968.
[Kon19] J. Konieczny. Gowers norms for the Thue-Morse and Rudin-Shapiro sequences. Ann.
Inst. Fourier (Grenoble), 69(4):1897–1913, 2019.
[MM89] P. Morton and W. J. Mourant. Paper folding, digit patterns and groups of arithmetic
fractals. Proc. London Math. Soc. (3), 59(2):253–293, 1989.
[Mor90] P. Morton. Connections between binary patterns and paperfolding. S´em. Th´eor. Nom-
bres Bordeaux (2), 2(1):1–12, 1990.
[MR10] C. Mauduit and J. Rivat. Sur un probl`eme de Gelfond: la somme des chiﬀres des
nombres premiers. Ann. of Math. (2), 171(3):1591–1646, 2010.
[MR15] C. Mauduit and J. Rivat. Prime numbers along Rudin-Shapiro sequences. J. Eur.
Math. Soc. (JEMS), 17(10):2595–2642, 2015.
[MS98] C. Mauduit and A. S´ark¨ozy. On ﬁnite pseudorandom binary sequences. II. The Cham-
pernowne, Rudin-Shapiro, and Thue-Morse sequences, a further construction. J. Num-
ber Theory, 73(2):256–276, 1998.
[Spi18] L. Spiegelhofer. The level of distribution of the Thue–Morse sequence. arXiv e-prints,
page arXiv:1803.01689, Mar 2018.
[ZPK18] Y. Zheng, L. Peng, and T. Kamae. Characterization of noncorrelated pattern sequences
and correlation dimensions. Discrete Contin. Dyn. Syst., 38(10):5085–5103, 2018.

(J. Konieczny) Camille Jordan Institute, Claude Bernard University Lyon 1, 43 Boule-
vard du 11 novembre 1918, 69622 Villeurbanne Cedex, France

Faculty of Mathematics and Computer Science, Jagiellonian University in Krak´ow,
 Lojasiewicza 6, 30-348 Krak´ow, Poland

Email address: jakub.konieczny@gmail.com
