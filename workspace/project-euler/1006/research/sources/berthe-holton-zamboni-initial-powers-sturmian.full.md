<!-- source: https://www.irif.fr/~berthe/Articles/sturm15.pdf | converted from PDF -->

INITIAL POWERS OF STURMIAN SEQUENCES

VAL´ERIE BERTH´E, CHARLES HOLTON, AND LUCA Q. ZAMBONI

Abstract. We investigate powers of preﬁxes in Sturmian sequences. We obtain an explicit
formula for ice(ω), the initial critical exponent of a Sturmian sequence ω, deﬁned as the
supremum of all real numbers p > 0 for which there exist arbitrary long preﬁxes of ω of the
form up, in terms of its S-adic representation. This formula is based on Ostrowski’s numer-
ation system. We characterize those irrational slopes α of which there exists a Sturmian
sequence ω beginning in only ﬁnitely many words of the form u2+ε for every ﬁxed ε > 0,
that is for which ice(ω) = 2. In the process we recover the known results for the index (or
critical exponent) of a Sturmian sequence.

1. Introduction.

There are a number of recent papers on powers of words occurring in Sturmian sequences
(see for instance [1, 2, 3, 8, 9, 19, 18, 29, 34, 40, 43]). Quantities of interest include the
supremum of powers of factors of a sequence (the index or critical exponent of the sequence),
and the limit superior of powers of longer and longer factors of the sequence. It is well-known
that these numbers are ﬁnite if and only if the partial quotients of the continued fraction
expansion of the slope of the Sturmian sequence are bounded (see [33]). An explicit formula
for the index of a Sturmian sequence was given by Vandeth (see Theorem 16 in [43]) in terms
of the partial quotients of its slope.
This paper deals with powers of factors occurring at the beginning of Sturmian sequences,
which we call initial powers. The work is motivated in part by a simple observation about the
Fibonacci Sturmian shift, the shift space of all Sturmian sequences of slope 2
1+√5 . This space
is inﬁnite, minimal and uniquely ergodic; one might expect preﬁx powers to be somewhat
uniform. Yet its characteristic sequence begins in no 3+√5
2 ≈ 2.62 power at all, while every
sequence outside the shift orbit of the characteristic sequence begins in arbitrarily long words
repeated 3 or more times. This example leads us to deﬁne the initial critical exponent of
a sequence ω over a ﬁnite alphabet, denoted ice(ω), as the supremum of all real numbers
p > 0 for which there exist arbitrarily long preﬁxes u of ω such that up is also a preﬁx of
ω. We obtain an explicit formula for the initial critical exponent of a Sturmian sequence, in
terms of a particular S-adic expansion. For characteristic Sturmian sequences, our formula
for ice has probably been known since [36], though Hedlund and Morse did not address this
question speciﬁcally. One can also obtain the formula for ice of a characteristic sequence
using Cassaigne’s formula for the recurrence quotient in [14]. See also [9, 45].
Every Sturmian sequence ω on the alphabet {0, 1} admits a unique S-adic representation
as an inﬁnite composition of the form

ω = T c1 ◦ τ a1
0 ◦ T c2 ◦ τ a2
1 ◦ T c3 ◦ τ a3
0 ◦ T c4 ◦ τ a4
1 ◦ · · · ,

1991 Mathematics Subject Classiﬁcation. Primary 37B10; Secondary 37A25,11J70,68R15.
The second author was partially supported by NSF grant DMS-0091946.
The third author was partially supported by NSF grant INT-9726708.
1

2 V. BERTH´E, C. HOLTON, AND L.Q. ZAMBONI

where T denotes the one-sided shift map, τ0 and τ1 are the morphisms on {0, 1}∗ deﬁned by

τ0(0) = 0 τ1(0) = 10,

τ0(1) = 01 τ1(1) = 1,
ak ≥ ck ≥ 0 for all k, ak ≥ 1 for k ≥ 2, and if ck = ak then ck−1 = 0. The sequence (ak)k≥1
turns out to be the sequence of partial quotients of the slope (deﬁned as the density of the
symbol 1), while (ck)k≥1 is the sequence of digits in the arithmetic Ostrowski expansion of
the intercept of the Sturmian sequence (see for instance [20, 21, 30, 31, 28, 37, 41, 42] and
the references in [10]). From this point of view, the characteristic (or standard) Sturmian
sequence of a particular slope is the one having ck = 0 for all k. This expansion of ω is
just one of many possible expansions as an inﬁnite composition of morphisms (see work of
Arnoux [39], Arnoux-Fisher [4], Arnoux-Ferenczi-Hubert [6]). In each case these expansions
are intimately linked to the Ostrowski numeration system.
In [3] it is shown that each Sturmian sequence begins in inﬁnitely many squares (see
also [19]), and hence ice(ω) ≥ 2 for all Sturmian sequences ω. We show that the value 2
is attainable, and give the following characterization of those slopes for which there is a
Sturmian sequence with initial critical exponent equal to 2 :

Theorem 1.1. Let α = [0; a1, a2, a3, . . . ] be an irrational number and let Xα be the set of all
Sturmian sequences of slope α. Then there is a Sturmian sequence ω ∈ Xα with ice(ω) = 2
if and only if for each pair of positive integers (s, t) with s > 1 there are only ﬁnitely many
indices k for which (ak, ak+1) = (s, t) or (ak, ak+1, ak+2) = (1, 1, t).

We also show how to explicitly construct a Sturmian sequence ω ∈ Xα with ice(ω) = 2 in
case one exists.
Write ind∗(ω) for the limit superior of powers of longer and longer words appearing in a
sequence ω. We prove the following relation between ice and ind∗ for characteristic Sturmian
sequences:

Theorem 1.2. Let ω be the characteristic Sturmian sequence of slope α. Then

ind∗(α) = 1 + ice(ω).

The paper is organized as follows. After ﬁrst recalling some basic facts on Sturmian
sequences and on ice, we introduce in Section 2 two S-adic representations of Sturmian se-
quences (additive and multiplicative versions) based on Ostrowski’s numeration system, and
conclude the section with a characterization of primitive substitutive Sturmian sequences.
We derive an explicit formula for the ice of a Sturmian sequence in Section 3. We study
general properties of ice in Section 4; special attention is given to the Fibonacci shift in
Section 4.4. We end with a proof of Theorem 1.1 in Section 5.

2. Preliminaries.

2.1. Deﬁnitions and notation. Throughout the paper, α denotes an irrational number in
(0, 1). Consider two two-interval exchange transformations, Rα : [−α, 1 − α) → [−α, 1 − α)
and ˜Rα : (−α, 1 − α] → (−α, 1 − α], deﬁned by

Rα(z) =
 {
z + α if z ∈ [−α, 1 − 2α)
z + α − 1 if z ∈ [1 − 2α, 1 − α)

INITIAL POWERS OF STURMIAN SEQUENCES 3

and
 ˜Rα(z) =
 {
z + α if z ∈ (−α, 1 − 2α]
z + α − 1 if z ∈ (1 − 2α, 1 − α].

Both can be considered as rotations of angle 2πα, since these are conjugate, after identiﬁ-
cation of points −α and 1 − α, to a circle rotation. A Sturmian sequence ω ∈ {0, 1}N of
slope α is simply the forward itinerary (with respect to the natural partition) of a point
x ∈ [−α, 1 − α] (called the intercept of ω) under the action of one of these transformations,
i.e., either ∀k ∈ N (ωk = 0 ⇐⇒ Rk
α(x) ∈ [−α, 1 − 2α))
or ∀k ∈ N (ωk = 0 ⇐⇒ ˜Rk
α(x) ∈ (−α, 1 − 2α]).
It is clear from this interpretation that the slope of a Sturmian sequence is the density of
the symbol 1.
Notation. In all that follows, the coding of the orbit of the point y with respect to the
partition (I, J) under the action of the two-interval exchange E means the sequence υ ∈
{0, 1}
N deﬁned by ∀k ∈ N (υk = 0 ⇐⇒ Ek(y) ∈ I).
A factor of a sequence ω is a ﬁnite subsequence of the form ω[i, j) := ωiωi+1 . . . ωj−1, i.e.,
a ﬁnite word that appears in ω. The complexity function p : N → N for a sequence ω is given
by p(n) = the number of distinct factors of ω of length n.
Sturmian sequences are exactly those one-sided inﬁnite sequences with complexity p(n) =
n + 1 for every n (see [36, 15]). Write Xα for the set of all Sturmian sequences of slope α,
and denote by T the shift map on sequences, i.e., (T (ω))i = ωi+1. Then Xα is a compact, T -
invariant subset of {0, 1}
N and the restriction of T to Xα (we shall abuse notation and call it T
also) gives us an inﬁnite, minimal, uniquely ergodic (one-sided) shift space. Recall that a map
on a topological space is minimal if the only closed non-empty invariant subset is the whole
space, and is uniquely ergodic if there exists a unique invariant Borel probability measure
on the space. The characteristic sequence of slope α is the unique left-special sequence in
Xα, i.e., the sequence having more than one T -preimage in Xα; this is the sequence with
intercept 0 (it is the same for Rα and ˜Rα) and its two shift preimages code respectively the
orbits of −α under Rα and 1 − α under ˜Rα. For more details on Sturmian sequences, see
[32, 39].
We shall use in Section 2.3 and 2.4 the notion of induction of a rotation. The induced
transformation of the rotation Rα (or similarly of ˜Rα) on a subinterval I of [−α, 1 − α] is
deﬁned as follows. For x ∈ I, we call the ﬁrst return time of x in I and denote by nI(x) the
smallest integer m > 0 such that Rm
α (x) ∈ I (m is ﬁnite since α is irrational). The induced
transformation of Rα on I is the map x ↦→ RnI (x)
α (x) on I.
A sequence is called recurrent if each of its factors appears inﬁnitely many times, and
uniformly recurrent if each of its factor appears with bounded gaps. If a shift space is
minimal, then any of its sequences is uniformly recurrent, and any shift space generated by
a uniformly recurrent sequence, as the closure of the orbit of this sequence under the action
of the shift, is minimal. A shift space (X, T ) is said to be linearly recurrent if there exists a
constant K such that, for each n ∈ N, every factor of length n of a sequence of X appears

4 V. BERTH´E, C. HOLTON, AND L.Q. ZAMBONI

in every factor of length nK. If a shift space (X, T ) is linearly recurrent, then it is minimal,
and it has sublinear complexity, that is, there exists C > 0 such that, for all n ∈ N, there
are at most Cn diﬀerent factors of length n in sequences of X. For more details on these
notions, see for instance [39] and [23].
If i ∈ {0, 1} we denote by ¯ı the other symbol in {0, 1}. Thus ¯ı = 1 − i, τi(i) = i, and
τi(¯ı) = i¯ı. Throughout the paper we write θ for the golden mean, (1 + √5)/2. We use Greek
letters ω and υ for inﬁnite sequences, and Roman letters u, v, w for ﬁnite words. The length
of a word w over the alphabet {0, 1} is denoted by |w|. We write N for the set of nonnegative
integers (0 ∈ N) and N∗ for the set of positive integers.

2.2. Initial critical exponent. Positive integer powers of a ﬁnite word w are deﬁned by

w1 = w and wn = wn−1w for n > 1.

We deﬁne w0 to be the empty word, i.e., the unique word of length 0, and for arbitrary
p ≥ 0, the pth power of w is given by
 wp = w⌊p⌋u

where u is the preﬁx of w of length ⌈(p − ⌊p⌋) |w|⌉ . Thus, wp has length ⌈p|w|⌉. A word is
called primitive if it is not an integer power of some shorter word. The power of a word w
in a sequence ω is the largest p (possibly ∞) so that wp is a factor of ω. The preﬁx power
of a word w in a sequence ω is the largest p (possibly ∞) so that wp is a preﬁx of ω. We
deﬁne the initial critical exponent of ω, denoted by ice(ω), as the limit superior of the preﬁx
powers of the words ω[0, n) in ω. We similarly deﬁne ind∗(ω) for a sequence ω as the limit
superior as n tends to ∞ of the largest powers of the factors of length n appearing in ω. For
a minimal shift space X, we write ind∗(X) for the common value of ind∗ on sequences of X.
Let us prove some properties of ice and ind∗ .

Proposition 2.1. Let (X, T ) be a (one-sided) shift space. Then

(1) For any ω ∈ X one has ice(ω) ≤ ice(T ω), and if the inequality is strict then T ω is
the shift image of at least two diﬀerent members of X, i.e., ω is a left-special element
of X.
(2) If (X, T ) is minimal then maxω∈X ice(ω) = ind
∗(X).
(3) If X is inﬁnite and minimal then some ω ∈ X has ice(ω) ≤ 1 + θ = (3 + √5)/2.
(4) If (X, T ) is minimal with sublinear complexity then ice is shift invariant oﬀ of the
union of a ﬁnite set of orbits; hence ice is almost everywhere constant with respect to
any ergodic Borel measure.
(5) If (X, T ) is linearly recurrent then ice is almost everywhere equal to ind∗(X) with
respect to any ﬁnite invariant Borel measure.

Proof. Let ω ∈ X. If w is a preﬁx of ω with preﬁx power p then the ﬁrst right conjugate of w,
i.e., the word v obtained from w by moving the ﬁrst letter to the end, is a preﬁx of T ω with
preﬁx power p − 1
|w| . The inequality in (1) follows by taking limits as |w| tends to inﬁnity.
Now suppose the inequality in (1) is strict. Then ice(T ω) > 1. Let vk be an increasing
sequence of preﬁxes of T ω whose corresponding preﬁx powers qk converge to ice(T ω). Let a
be the ﬁrst letter of ω and let b be a common last letter for inﬁnitely many of the vk. By
passing to a subsequence we may assume that qk > 1 and vk ends in b for all k. Note that

INITIAL POWERS OF STURMIAN SEQUENCES 5

a ̸= b, since otherwise, for all k, the ﬁrst left conjugate of vk is a preﬁx of ω with preﬁx
power qk + 1
|vk| and we obtain a contradiction:

lim
k→∞ qk + 1
|vk| ≤ ice(ω) < ice(T ω) = lim
k→∞ qk.

For each k, T ω begins in vkvqk−1
k and ω begins in avqk
k , hence avqk−1
k and bvqk−1
k are both
factors of sequences of X. But |vqk−1
k | → ∞ and each vqk−1
k is a preﬁx of T ω, hence aT ω and
bT ω both belong to X.
To prove (2) we need the following:
(2
′) For every p ∈ (0, ind∗(X)), every word which appears in sequences of X is a preﬁx of
some word whose pth power appears in sequences of X.
Proof of (2
′). By minimality, if w appears in sequences of X then it appears in bounded
gaps, i.e., there exists N = N (w) such that for all ω in X, at least one of ω, T ω, . . . , T N (w)−1ω
begins in w. Choose η > 0 such that p + η < ind
∗(X), and let v be a word of length at least
N/η such that vp+η appears in sequences of X. Then one of the ﬁrst N − 1 right conjugates
of v has w as a preﬁx and appears to power p in sequences of X.
Proof of (2). By (2
′) we can ﬁnd a sequence wk of words which appear in sequences of X,
such that, for each k, wpk
k is a preﬁx of wk+1, where pk ≥ 1 and pk → ind∗(X) and |wk| → ∞
as k → ∞. There is a unique ω ∈ X having each wk as a preﬁx, and the construction
guarantees ice(ω) ≥ ind
∗(X). We always have ice ≤ ind
∗(X), of course.
Part (3) follows from [35].
To prove (4), we use Cassaigne’s result from [13]: The ﬁrst diﬀerence of the complexity
function is bounded if complexity is sublinear. Let C > 0 be an upper bound for the ﬁrst
diﬀerence of the complexity. By minimality, every word w in X of length n has at least
one left extension, that is, a word aw occurring in X for some letter a; hence there can be
no more than C words of length n which have two or more left extensions and the set of
sequences ω in X that have more than one shift preimage has at most C elements.
Assertion (5) holds trivially if X consists of a single periodic orbit, so let us assume that X
is an inﬁnite set. Then (X, T ) is minimal and has sublinear complexity, and ind
∗(X) < ∞.
Let µ be a (nonzero) ﬁnite invariant Borel measure for (X, T ). Suppose, for a contradiction,
that µ{ω ∈ X : ice(ω) < ind
∗(X)} > 0. For some ε > 0 we must have µ{ω ∈ X : ice(ω) <
ind
∗(X) − ε} > 0. Fix such an ε, and set E = {ω ∈ X : ice(ω) < ind
∗(X) − ε}. Let ν be
the Borel probability measure deﬁned by ν(B) = µ(E∩B)
µE . As in the proof of part (4), ice is
invariant oﬀ a ﬁnite set of orbits. Thus, µ(T −1E \ E) = 0, and ν is an invariant measure.
Choose a subsequence (nk)k≥0 of the positive integers such that the sequence of maximal
powers pk of words of length nk converges to ind∗(X). Linear recurrence implies that the pk
are bounded and the ν-measure of the set of sequences beginning in a word of length nk to
power at least pk − ε is bounded away from 0 (see for instance [23]). But then we must have
ν{ω ∈ X : ice(ω) ≥ ind
∗(X) − ε} > 0, a contradiction. □

The focus of this paper is on the values of ice on the set Xα of all Sturmian sequences of
some ﬁxed irrational slope α. It follows from known results (see for instance [43]) that

ind
∗(α) := ind
∗(Xα) = 2 + lim sup
k→∞ [ak; ak−1, . . . , a1],

where [ak; ak−1, . . . , a1] denotes the continued fraction of ak, ak−1, · · · , a1. This implies in
particular that any Sturmian sequence contains cubes (see also [9]) and that a Sturmian

6 V. BERTH´E, C. HOLTON, AND L.Q. ZAMBONI

sequence has ﬁnite index if and only if its slope has bounded partial quotients (this last
result is in [34]). See [14] for a study of the topological structure of the set of values taken
by the index. Recall that Xα is uniquely ergodic.

Lemma 2.2. The almost everywhere value of ice on Xα is ind
∗(α).

Proof. Suppose ﬁrst that ind
∗(α) = ∞. Let p > 2 and N ≥ 3. There is a primitive word u
of length at least N and a power p′ ≥ N p + 1 such that up′ appears in Xα and the exponent
p′ is maximal for words having the same length as u.
We claim that up′−1 is left special, i.e., both 0up′−1 and 1up′−1 appear in Xα. To see this,
let a be the last letter of u. Since aup′ is the same as the ﬁrst left conjugate of u to power
p′ + 1
|u| , maximality of p′ implies that this word does not appear in Xα. One of the symbols
b ∈ {0, 1} is such that bup′ appears in Xα, and we have just shown that b ̸= a. Thus aup′−1

and bup′−1 both appear in Xα, the former as a suﬃx of up′ and the latter as a preﬁx of bup′.
A return word to a factor h in a sequence ω is a factor ω[i, j), where h occurs in ω starting
at the ith and jth places and nowhere between. Sturmian sequences have the following
properties (see for instance [44]):
- there is exactly one left special factor of each length;
- every factor has exactly two return words;
- the sum of the lengths of the return words to a factor v is at least |v| + 1; and
- the length of a return word to a left special factor v is bounded above by |v| + 1.
We know that u is a return word for up′−1 because u is primitive and p′ > 3. The other
return word to up′−1 must be a preﬁx of up′−10 or up′−11 of length at least (p′ − 2)|u| + 1.
This implies that the set of points of Xα beginning in a suﬃx of up′−1 of length at least
(p′ − 1)|u|/N has measure at least
⌈ (N −1)(p′−1)|u|
N ⌉

(p′ − 2)|u| + 1 ≥ N − 1
N

and such points begin in a word of length |u| to power p. The result follows easily from this.
In case ind
∗(α) < ∞, the partial quotients of α are bounded and Xα is linearly recurrent
following [23]. Part (5) of Proposition 2.1 applies directly. □

Using this lemma and the formula for ind∗(α) above, we see that the a.e. value of ice on
Xα is greater than 4 unless the partial quotients ak are eventually 1. Lebesgue almost every
slope α ∈ (0, 1) has unbounded partial quotients, and thus, for Lebesgue a.e. α, ice is a.e.
inﬁnite on Xα.

2.3. An additive S-adic representation. Let ω ∈ {0, 1}
N be a Sturmian sequence of
slope α. Exactly one of the words ii (i ∈ {0, 1}) is a factor of ω and there is a unique
sequence ω′ such that ω = T b(τi(ω′)), where b = 0 if ω begins in i and b = 1 otherwise.
The map ω ↦→ ω′ on Xα is really just induction on the longer of the two intervals in the
associated two-interval exchange. Speciﬁcally, suppose ω codes the orbit of a point x; if x is
in the longer interval then ω′ codes the orbit of x in the induced interval exchange, and if x
is in the other (shorter) interval then ω′ codes the orbit of the preimage of x (which is in the
longer interval) in the induced interval exchange. With this interpretation it is clear that ω′

is also Sturmian. Thus we may iterate this “desubstitution” process to obtain our additive
S-adic expansion:
 INITIAL POWERS OF STURMIAN SEQUENCES 7

Proposition 2.3. Let ω be a Sturmian sequence. There exist a sequence of Sturmian se-
quences (ω(n))n≥1 and two sequences (bn)n≥1, (in)n≥1 with values in {0, 1} such that
(1) ω = T b1 ◦ τi1 ◦ · · · ◦ T bn ◦ τin(ω(n)) for each n,
(2) (in) is not eventually constant,
(3) if in = in+1 and bn+1 = 0 then bn = 0,
(4) if in ̸= in+1 then bn and bn+1 are not both 1.

Proof. The induction process described above gives us the three sequences satisfying assertion
(1). If (in)n≥1 were eventually constant, say in = i for all n ≥ N, then ω would contain
arbitrary powers of τi1 ◦ · · · ◦ τiN (i), which is impossible since ω is Sturmian.
Assertions (3) and (4) are easily deduced from the facts that ω(n)
0 is the ﬁrst letter of
T bn+1 ◦ τin+1, i.e.,
 ω(n)
0 =
 {
in+1 if bn+1 = 0,
¯ın+1 if bn+1 = 1,

and bn = 1 =⇒ ω(n)
0 = ¯ın. □

It is helpful to think of T b1 ◦τi1 ◦· · ·◦T bn ◦τin as a composition of “inﬂations” (the τim) and
“cuts” (the T bm) where the amount cut after applying τim to ω(m) is less than the inﬂated
image of the ﬁrst letter of ω(m), i.e., bm < |τim(ω(m)
0 )|. Extending this notion of T as the map
which cuts oﬀ the ﬁrst letter of a sequence, we shall abuse notation slightly and write T w for
the suﬃx of a word w obtained by deleting the ﬁrst letter. Let us note that, by deﬁnition,∣
∣
∣T b1 ◦ τi1 ◦ · · · ◦ T bn ◦ τin (ω(n)
0 )∣
∣
∣ ≥ 1 for all n, hence

T b1 ◦ τi1 ◦ · · · ◦ T bn ◦ τin (ω(n)) = T b1 ◦ τi1 ◦ · · · ◦ T bn ◦ τin (ω(n)
0 ) ⋆ τi1 ◦ · · · ◦ τin
 ((ω(n)
k )
k≥1
) ,

where, for clarity, we have written ⋆ for concatenation. It is possible that
∣
∣
∣T b1 ◦ τi1 ◦ · · · ◦ T bn ◦ τin (ω(n)
0 )∣
∣
∣ = 1 for all n.

This happens, for example, when in = bn = n mod 2 for all n.
The following useful lemma can be proved by straightforward induction.

Lemma 2.4. If υ and υ′ are sequences in {0, 1} beginning in diﬀerent letters and τ is any
composition of the τi then the longest common preﬁx of τ (υ) and τ (υ′) has length |τ (01)| − 2.

We next show that what we have is indeed an additive S-adic expansion in the sense of
[23, 25]. The important thing is that the sequences (in)n≥1 and (bn)n≥1 entirely determine
ω – we do not need to keep track of the ω(n).

Proposition 2.5. Every pair of sequences (in)n≥1, (bn)n≥1 with values in {0, 1} satisfying
(2)–(4) of Proposition 2.3 is the additive S-adic expansion of a unique Sturmian sequence.

Proof. Suppose (in), (bn) satisfy (2)–(4) of Proposition 2.3. If υ, υ′ ∈ {0, 1}N then it follows
from Lemma 2.4 and the previous remarks on cuts and inﬂations that T b1 ◦τi1 ◦· · ·◦T bn ◦τin(υ)
and T b1 ◦τi1 ◦· · ·◦T bn ◦τin(υ′) have a common preﬁx of length at least |τi1 ◦τi2 ◦· · ·◦τin(in)|−1,
which tends to inﬁnity as n tends to inﬁnity. Thus ∩
∞
n=1T b1 ◦ τi1 ◦ · · · ◦ T bn ◦ τin({0, 1}N)

8 V. BERTH´E, C. HOLTON, AND L.Q. ZAMBONI

consists of a single point, ω. We claim that ω is Sturmian. Indeed, if υ is any Sturmian
sequence then ω = lim
n→∞ T b1 ◦ τi1 ◦ · · · ◦ T bn ◦ τin(υ).

The morphisms τ0 and τ1 are Sturmian (i.e., they take Sturmian sequences to Sturmian
sequences, see [32]) and the complexity of a limit is less than or equal to the limit of the
complexities, hence ω has complexity p(n) ≤ n + 1 and is therefore either Sturmian or
eventually periodic. It follows from the fact that (in)n≥1 is not eventually constant that ω is
not eventually periodic, so p(n) ≥ n + 1 and ω is Sturmian. One checks by induction that ω
has (in)n≥1, (bn)n≥1 as its S-adic expansion. □

Such an expansion will be called the additive Ostrowski S-adic expansion associated with
the sequence ω. We will see below that Ostrowski expansions in the sense of [37] appear in
a natural way when one considers a multiplicative version of these expansions.

2.4. A multiplicative S-adic expansion. A more compact version of the additive S-adic
representation is desirable. As a sequence in {0, 1} we can write

i1i2 . . . = 0
a11
a20
a31
a4 . . .

with ai ≥ 1 for i ≥ 2. Let sk = ∑k
j=1 aj and ck = ∑sk
n=sk−1+1 bn. For all n ≥ 1 we have
0 ≤ cn ≤ an and if cn+1 = an+1 then cn = 0. We also have

b1b2 . . . = 0
a1−c11
c10
a2−c21
c2 . . . ,

and for k > 0

ω = τ a1−c1
0 ◦ (T ◦ τ0)
c1 ◦ τ a2−c2
1 ◦ (T ◦ τ1)
c2 ◦ · · · ◦ τ ak−ck
k−1 mod 2 ◦ (T ◦ τk−1 mod 2)
ck(ω(sk)).

To avoid cumbersome notation we shall henceforth write τn for τn mod 2. We can further
simplify to obtain
 ω = T c1τ a1
0 ◦ T c2τ a2
1 ◦ T c3τ a3
0 ◦ · · · ◦ T ckτ ak
k−1(ω(sk)).

Let α = [0; a1 + 1, a2, a3, . . . ]. Set
 p0 = 0 q0 = 1
p1 = 1 q1 = a1 + 1

and for k ≥ 2,
 pk = akpk−1 + pk−2 qk = akqk−1 + qk−2.

Set δ−1 = 1 − α, and for k ≥ 0 put δk = |qkα − pk| = (−1)
k(qkα − pk). One has

∀k ∈ N, δk−1 = ak+1δk + δk+1.

The continued fraction convergents of α are the rational numbers pk/qk, which, as the name
suggests, converge to α. The convergents are, in a sense, the best possible rational approxi-
mations to α. The following lemma can be proved by straightforward induction.

INITIAL POWERS OF STURMIAN SEQUENCES 9

Lemma 2.6. Write |w|j for the number of occurrences of the letter j in word w. Then for
i ∈ {0, 1}

(|τ a1
0 ◦ · · · ◦ τ ak
k−1(i)|0, |τ a1
0 ◦ · · · ◦ τ ak
k−1(i)|1) =
 {
(qk − pk, pk) i = k mod 2
(qk−1 − pk−1, pk−1) i ̸= k mod 2.

It follows that the slope of ω is equal to lim pk/qk = α. This means that the ak and hence
also the sequence (in)n≥1 are determined by the slope of ω. Translating the condition on
the sequences (in)n≥1 and (bn)n≥1 to a condition on the ck, we have shown how Sturmian
sequences of slope α = [0; a1 + 1, a2, . . . ] are in one-to-one correspondence with sequences
(ck)k≥1 such that 0 ≤ ck ≤ ak and if ck+1 = ak+1 then ck = 0.

Proposition 2.7. Let α = [0; a1 + 1, a2, a3, . . . ]. Let ω be a Sturmian sequence which codes
the orbit of the point x under the action of Rα or ˜Rα. There exists a sequence of integers
(cn)n∈N where

(1) ∀n,
 {
0 ≤ cn ≤ an,
cn+1 = an+1 ⇒ cn = 0,

and a sequence of Sturmian sequences (υ(k)) such that

(2) ∀k, ω = T c1τ a1
0 ◦ T c2τ a2
1 ◦ T c3τ a3
0 ◦ · · · ◦ T ckτ ak
k−1(υ(k)),

and
 x =
 ∞∑

k=1 ck(−1)
k−1δk−1 =
 ∞∑

k=1 ck(qk−1α − pk−1).

Proof. Let us suppose that ω codes the orbit of x in [−α, 1 − α) under the rotation Rα with
respect to the partition ([−α, 1 − 2α), [1 − 2α, 1 − α)) (the ˜Rα case is similar). We deﬁne
two-interval exchanges E(n) for n ≥ 0 as follows:
If n is even then E(n) : [−δn, δn−1) → [−δn, δn−1) is given by

E(n)(z) =
 {
z + δn if z ∈ [−δn, −δn + δn−1)
z − δn−1 if z ∈ [−δn + δn−1, δn−1) .

If n is odd then E(n) : [−δn−1, δn) → [−δn−1, δn) is given by

E(n)(z) =
 {
z + δn−1 if z ∈ [−δn−1, −δn−1 + δn)
z − δn if z ∈ [−δn−1 + δn, δn) .

Note that E(0) equals Rα. We also deﬁne inductively a sequence of points (x(n))n≥0 where

x(n) ∈
 {
[−δn, δn−1) if n is even
[−δn−1, δn) if n is odd ,

and a sequence of nonnegative integers (cn)n≥1 by setting x(0) = x, and for n > 0 :
If n is even then
 cn+1 =
 {
0 if x(n) ∈ [−δn, δn+1)⌊ x(n)−δn+1
δn
 ⌋ + 1 if x(n) ∈ [δn+1, δn−1)

10 V. BERTH´E, C. HOLTON, AND L.Q. ZAMBONI

and
 x(n+1) = x(n) − cn+1δn.

If n is odd then
 cn+1 =
 {
0 if x(n) ∈ [−δn+1, δn)⌈
− x(n)+δn+1
δn
 ⌉ if x(n) ∈ [−δn−1, −δn+1)

and
 x(n+1) = x(n) + cn+1δn.

Let us check that the admissibility condition (1) holds. We have easily that ck ≤ ak for all
k ≥ 1. If c2k+1 ̸= 0 then x(2k+1) ∈ [δ2k+1 − δ2k, δ2k+1), and thus c2k+2 ̸= a2k+2. If c2k+2 ̸= 0
then x(2k+2) ∈ [−δ2k+2, −δ2k+2 + δ2k+1), and thus c2k+3 ̸= a2k+3.
Furthermore, for all n ∈ N we have x = x(n) + ∑n−1
k=0 ck+1(−1)
kδk and thus

x =
 ∞∑

k=0 ck+1(−1)
kδk.

We claim that if n is even then E(n+1) is the induced transformation of E(n) on the interval
[−δn, δn+1). Let us check this. If z ∈ [−δn, −δn + δn+1) then

E(n)(z) = z + δn ∈ [0, δn+1)

and thus the induced transformation agrees with E(n+1) on [−δn, −δn + δn+1). If z ∈ [−δn +
δn+1, δn+1) then (E(n))k (z) = z + kδn ≥ δn+1 for 1 ≤ k ≤ an+1

and (E(n))an+1+1 = z + (an+1)δn − δn−1 = z − δn+1 ∈ [−δn, 0),

as desired. One similarly checks that for n odd, E(n+1) is the induced transformation on the
interval [−δn+1, δn) of the map E(n).
For n ≥ 1 we let υ(n) be the Sturmian sequence coding the orbit of x(n) in the two-interval
exchange E(n) with respect to the partition ([−δn, −δn + δn−1), [−δn + δn−1, δn−1)) if n is
even, and to the partition ([−δn−1, −δn−1 + δn), [−δn−1 + δn, δn)) if n is odd. It follows that
υ(n) = T cn+1τ an+1
n+1 (υ(n+1)) holds for every n. □

Remarks. Such an expansion will be called the (multiplicative) Ostrowski S-adic expansion
associated with the sequence ω. More generally, an expansion of the form

x =
 ∞∑

k=0 ck+1(qkα − pk),

where the sequence of integer digits (ck)k≥1 satisﬁes the admissibility condition (1) is called
an Ostrowski expansion following [37] (see also [10, 20, 21, 30, 31, 28, 37, 41, 42]). Note that
the characteristic sequence of slope α corresponds to intercept x = 0, having all ck equal to
0.
 INITIAL POWERS OF STURMIAN SEQUENCES 11

2.5. The Ostrowski odometer. Let α = [0; a1 + 1, a2, . . . ] and set

Kα = {(ck)k≥1| ∀k ≥ 1 (ck ∈ N, 0 ≤ ck ≤ ak) and (ck+1 = ak+1 ⇒ ck = 0)}.

It is easy to see that

Kα = {(ck)k≥1| ∀k ≥ 1, ck ∈ N, c1q0 + · · · + ckqk−1 ≤ qk − 1}.

Let c = (ck)k≥1 ∈ Kα, set

D(c) = {k ≥ 1| c1q0 + · · · + ckqk−1 = qk+1 − 1},

and put m(c) = sup D(c) if D(c) is nonempty, and m(c) = −1 otherwise. Note that m(c) =
+∞ if and only if c is of the form

a10a30 . . . or 0a20a4 . . . ,

and if m(c) > 0 then

c =
 {
a10a30 . . . am(c)−10cm(c)+1cm(c)+2 . . . if m(c) is even
0a20a4 . . . 0am(c)−10cm(c)+1cm(c)+2 . . . if m(c) is odd.

Following [26], one can deﬁne on the compact set Kα (endowed with the product of the
discrete topologies on the ﬁnite sets {0 ≤ d ≤ ak}) the addition σ by 1,

σ(c) =
 {
0
m(c)+1(cm(c)+1 + 1)cm(c)+2 . . . if m(c) < ∞,
0
∞ otherwise.

The map σ is called the Ostrowski α-odometer. The map σ : Kα → Kα is onto and
continuous, and (Kα, σ) is minimal (for more details, see [26, 7]).

Proposition 2.8. The dynamical systems (Kα, σ) and (Xα, T ) are topologically conjugate.

Proof. The sets Xα and Kα are in one-to-one correspondence via the map Ψ : Xα → Kα,
ω ↦→ (ck)k≥1, where (ck)k≥1 is the Ostrowski S-adic expansion of Proposition 2.7.
Suppose ω ∈ Xα and Ψ(ω) = c does not have a tail in common with a10a30 . . . or
0a20a4 . . . . Put m = max D(c) and let υ(k) be as in Proposition 2.7. Then cm+1 < am+1 and

T (ω) = T (T c1τ a1
0 ◦ · · · ◦ T cmτ am
m−1 (υ(m)))

= τ a1
0 ◦ · · · ◦ τ am
m−1 (T υ(m))

= τ a1
0 ◦ · · · ◦ τ am
m−1 ◦ T cm+1+1τ am+1
m (υ(m+1)) ,

whence Ψ(T ω) = σ(Ψ(ω)). This holds for a dense set of ω ∈ Xα. □

2.6. A characterization of primitive substitutive Sturmian sequences. Let A be a
ﬁnite alphabet and denote by A∗ the free monoid generated by A with concatenation as
the multiplication, i.e, A∗ is the set of ﬁnite words over the alphabet A. A substitution
is a morphism of the free monoid A∗ taking each element of A to a nonempty word. A
substitution τ is primitive if there exists an integer k such that for all letters a, b in the
alphabet A, a is a factor of τ k(b). A sequence u is primitive substitutive if there exist a
primitive substitution τ over an alphabet B and a letter-to-letter morphism ϕ : B → A
such that u = ϕ(v), where v = τ (v) ∈ BN is ﬁxed by τ . We shall characterize primitive
substitutive Sturmian sequences in this section. For characterizations of Sturmian sequences
that are ﬁxed points of substitutions, see [16, 38, 46]. Let us recall a fact about Ostrowski’s
numeration (see for instance [28]):

12 V. BERTH´E, C. HOLTON, AND L.Q. ZAMBONI

Theorem 2.9. Let
 x =
 ∞∑

k=1 ck+1(qkα − pk),

where the sequence (ck)k≥1 satisﬁes the admissibility conditions (1). Suppose α is quadratic.
Then (ck)k≥1 is eventually periodic if and only if x ∈ Q(α).

Let ω be a uniformly recurrent sequence, and let h be a factor of ω. Recall that a return
word to h is a factor ω[i, j), where h occurs in ω starting at the ith and jth places and
nowhere between. Let Ah be the set of return words to h in ω. A sequence υ with the same
set of factors as ω and having h as a preﬁx can be recoded over the alphabet Ah. Indeed
we can naturally write the sequence υ as a concatenation of return words to h and this
decomposition is unique. We enumerate the elements of the set Ah of return words to h in
the order of their ﬁrst appearance in the sequence ω, turning this set into a new alphabet.
We then can recode the sequence υ over this new alphabet. The recoded sequence, called a
derived sequence of υ, is denoted by Dh(υ). One can also associate a derived sequence with
a sequence υ not having h as a preﬁx as follows. Let p be a preﬁx of a return word in Ah
such that the sequence pυ starts with h and has the same set of factors as ω. We will also
call a derived sequence the sequence over Ah obtained by coding the sequence pυ. We will
use the following result [22, 27, 24]:

Theorem 2.10. A uniformly recurrent sequence is primitive substitutive if and only if the
set of derived sequences (up to the alphabet) over all its factors is ﬁnite.

Note that an expansion of the form

ω = τ a1−c1
0 ◦ (T ◦ τ0)
c1 ◦ τ a2−c2
1 ◦ (T ◦ τ1)
c2 ◦ · · · ◦ τ ak−ck
k−1 ◦ (T ◦ τk−1)
ck(ω(sk)).

can explicitly be written as a standard S-adic expansion, that is, as a limit of the composition
of a ﬁnite number of substitutions following [25, 23], by introducing the morphisms τ ′
i for
i ∈ {0, 1} deﬁned by τ ′
i (i) = i and τ ′
i (j) = ji, for j ̸= i. Indeed we have

ω = τ a1−c1
0 ◦ (τ ′
0)
c1 ◦ τ a2−c2
1 ◦ (τ ′
1)
c2 ◦ · · · ◦ τ ak−ck
k−1 ◦ (τ ′
k−1)
ck(ω(sk)).

Proposition 2.11. A Sturmian sequence ω of slope α which codes the orbit of x is primitive
substitutive if and only if α is a quadratic irrational and x ∈ Q(α).

Proof. If α is quadratic and x ∈ Q(α), then (ak)k≥1 and (ck)k≥1 are eventually periodic. The
standard S-adic expansion above (using the τi and τ ′
i ) is eventually periodic, and ω is seen
to be primitive substitutive.
Conversely, suppose ω is primitive substitutive. We will use the notation of Proposition 2.7.
The sequences υ(k) are derived sequences. More precisely, if k mod 2 denotes the letter in
{0, 1} with value k mod 2, then

υ(k+1) = D(k mod 2)ak+1 ((k mod 2)
ck+1υ(k)),

where (k mod 2)
ck+1υ(k) denotes the sequence made of the word (k mod 2)
ck+1 concatenated
with the sequence υ(k). Indeed, (k mod 2)
ck+11 and (k mod 2)
ck+1+11 are exactly the two
return words of (k mod 2)
ck+1 in ω, the second one corresponding to the interval of induction.
The derived sequence of a derived sequence is again a derived sequence (up to the alphabet).
Hence following Theorem 2.10, there are two sequences υ(k) and υ(ℓ) which are equal, hence
(ak)k≥1 and (ck)k≥1 are eventually periodic. □

INITIAL POWERS OF STURMIAN SEQUENCES 13

3. Calculating initial powers.

The paradigm for our study is that large initial powers of ω come from large initial powers
of the ω(n). Before giving a more precise statement let us prove a simpler fact. Let ω be a
Sturmian sequence and let in, bn, ω(n) be deﬁned as in the previous section. Recall that a
word is primitive if it is not an integer power of a shorter word.

Lemma 3.1. If ω begins in a word wr where r > 1, |w| > 2, and w is primitive then there is
a preﬁx w(1) of ω(1) such that w is a cyclic permutation of τi1(w(1)). Furthermore, |w(1)| ≥ 2
and w(1) is primitive.

Proof. If b1 = 0 then ω0 = ω|w| = i1. The only place that i1 occurs in the image of a letter
under τi1 is as the ﬁrst letter. Thus the longest word of the form τi1(ω(1)
0 )τi1(ω(1)
1 ) . . . τi1(ω(1)
j )
which is a preﬁx of w must in fact be w, so that w(1) = ω(1)[0, j] does the job.
In the case b1 = 1, we have τi1(ω(1)) = i1ω, and ω0 = ω|w| = ¯ı1. Since no sequence in
the image of τi1 can have ¯ı1¯ı1 as a factor, it must be that ω|w|−1 = i1. The same argument
used in the ﬁrst case produces a preﬁx w(1) of ω(1) for which τi1(w(1)) = i1w[0, |w| − 2], and
i1w[0, |w| − 2] is a cyclic permutation of w.
Now |τi1(u)| ≤ 2|u| for any word u, and |τi1(w(1))| = |w| > 2, so we must have |w(1)| ≥ 2,
and if w(1) were an integer power of some shorter word then w would be also, contrary to
the hypothesis. □

We are now prepared to prove an important fact about initial powers. Let us recall that
for all k > 0, sk = ∑k
j=1 aj, and

ω = τ a1−c1
0 ◦ (T ◦ τ0)
c1 ◦ τ a2−c2
1 ◦ (T ◦ τ1)
c2 ◦ · · · ◦ τ ak−ck
k−1 ◦ (T ◦ τk−1)
ck(ω(sk))

= T c1τ a1
0 ◦ T c2τ a2
1 ◦ T c3τ a3
0 ◦ · · · ◦ T ckτ ak
k−1(ω(sk)).

Proposition 3.2. Suppose ω begins in a word w to power r ≥ 2, where |w| ≥ 2, and w
is primitive. Then there is a nonnegative integer m such that w is a cyclic permutation of
τi1 ◦ · · · ◦ τim(01), and ω(m) begins in 01 or 10 to power > ⌊r⌋ − 1. Furthermore, m is one of
the numbers sk − 1 or sk − ck − 1. If r ≥ 3 then m is one of the numbers sk − 1.

Proof. Let w(1) be the preﬁx of ω(1) given by Lemma 3.1. If |w(1)| > 2 and the preﬁx power
of w(1) in ω(1) is > 1 then we can apply the lemma again to get a preﬁx w(2) of ω(2). Continue
in this way as long as possible, at the nth step obtaining a preﬁx w(n) of ω(n) for which
τin(w(n)) is a cyclic permutation of w(n−1), stopping after m steps when either |w(m)| = 2 or
the preﬁx power r′ of w(m) in ω(m) is 1. We shall show that r′ > 1 and |w(m)| = 2, from which
it follows that w(m) is 01 or 10 since w(m) is primitive, and hence w is a cyclic permutation
of τi1 ◦ · · · ◦ τim(01).
Write (w(m))
∞ for the inﬁnite periodic word w(m)w(m)w(m) . . . . The longest common preﬁx
shared by (w(m))
∞ and ω(m) is (w(m))
r′, so by Lemma 2.4 the longest common preﬁx of

τi1 ◦ · · · ◦ τim((w(m))
∞)

and τi1 ◦ · · · ◦ τim(ω(m))
has length

|τi1 ◦ · · · ◦ τim((w(m))
r′)| + |τi1 ◦ · · · ◦ τim(01)| − 2 < |τi1 ◦ · · · ◦ τim((w(m))
r′+1)|,

14 V. BERTH´E, C. HOLTON, AND L.Q. ZAMBONI

since w(m) must contain both a 0 and a 1, by primitivity of w(m) and |w(m)| > 1 in view of
Lemma 3.1.
On the other hand, T b1 ◦ τi1 ◦ · · · ◦ T bm ◦ τim((w(m))
∞)

and T b1 ◦ τi1 ◦ · · · ◦ T bm ◦ τim(ω(m))

have wr as their longest common preﬁx and thus

τi1 ◦ · · · ◦ τim((w(m))
∞)

and τi1 ◦ · · · ◦ τim(ω(m))

have a common preﬁx of length ≥ r|w|. Putting these inequalities together we have

|τi1 ◦ · · · ◦ τim((w(m))
r′+1)| > r|τi1 ◦ · · · ◦ τim(w(m))|

from which we may deduce that ⌊r′⌋ ≥ ⌊r⌋ − 1 and if r or r′ is an integer then r′ > r − 1.
Thus r′ > 1 and hence |w(m)| = 2 as claimed. This shows that ω(m) begins in 01 or 10 to
power r′ > ⌊r⌋ − 1.
Let us now examine m more closely. We know that ω(m) begins in 010 or 101; indeed
w(m) = 01 or 10 and r′ > 1. By symmetry we need only to consider the former possibility.
Case 1: im+1 = 0. Since ω(m) begins in 01, then bm+1 = 0 and ω(m+1) must begin in 1.
If im+2 = 0 then this means bm+2 = 1, i.e., m is one of the numbers sk − ck − 1, where
0 < ck < ak. Otherwise im+2 = 1 and m is one of the sk − 1.
Case 2: im+1 = 1. Then bm+1 = 1 and ω(m+1) begins in 00, which means im+2 = 0, and hence
m is one of the sk − 1.
From the ﬁrst case we see that if m is one of the numbers sk − ck − 1 (0 < ck < ak) then
ω(m) = τ0 ◦ T ◦ τ0(ω(m+2)) and ω(m+2) begins in 1, and thus in 10 since 11 does not occur as a
factor in ω(m+2) (one has im+2 = 0), which is enough to guarantee that ω(m) begins in 0100,
i.e., r′ = 3/2. This cannot happen if r ≥ 3, since ⌊r′⌋ ≥ ⌊r⌋ − 1. □

Now that we know where preﬁx powers r ≥ 2 in ω come from we can compute them exactly.

Proposition 3.3. Let w and r be as in Proposition 3.2 and let m, ω(m), and w(m) be as in
its proof. Assume that r is the largest power of w which is a preﬁx of ω. Then

r =
 



1ak+2=ck+2 +
 Pk+1
j=1 (aj −cj )qj−1
qk if m = sk − 1

1 +
 Pk
j=1(aj −cj )qj−1
qk−ckqk−1 if m = sk − ck − 1 with 0 < ck < ak

where 1ak+2=ck+2 is 1 if ak+2 = ck+2 and 0 otherwise.
Conversely, for each k, ω begins in a cyclic permutation of τ a1
0 ◦ τ a2
1 ◦ · · · ◦ τ ak
k−1(01) with

preﬁx power 1ak+2=ck+2 +
 Pk+1
j=1 (aj −cj )qj−1
qk and for each k such that 0 < ck < ak, ω begins in a

cyclic permutation of the word τ a1
0 ◦τ a2
1 ◦· · ·◦τ ak−ck−1
k−1 (01) with preﬁx power 1+
 Pk
j=1(aj −cj )qj−1
qk−ckqk−1 .

Before proving the proposition let us state a lemma closely related to Lemma 2.6 to be
used in the calculation. It is proved easily by induction.

INITIAL POWERS OF STURMIAN SEQUENCES 15

Lemma 3.4. Let k > 0 and set i = k mod 2. Then

∣
∣τ a1
0 ◦ τ a2
1 ◦ · · · ◦ τ ak
k−1(i¯ı)
∣
∣ = qk + qk−1 = 2 +
 k∑

j=1 ajqj−1,

∣
∣τ a1
0 ◦ τ a2
1 ◦ · · · ◦ τ ak
k−1(i)
∣
∣ = qk,

∣
∣T c1 ◦ τ a1
0 ◦ · · · ◦ T ck ◦ τ ak
k−1(i)
∣
∣ = qk −
 k∑

j=1 cjqj−1,

∣
∣T c1 ◦ τ a1
0 ◦ · · · ◦ T ck ◦ τ ak
k−1(i¯ı)
∣
∣ = 2 +
 k∑

j=1 (aj − cj)qj−1.

Proof of Proposition 3.3. First suppose m = sk − 1. Set i = k mod 2. The sequence ω(sk)

begins in i1ak+2=ck+2 +ak+1−ck+1¯ı. Indeed, ω(sk) = T ck+1 ◦ τ ak+1
i ω(sk+1); if ak+2 ̸= ck+2, then
ω(sk+1) begins in ¯ı and ω(sk) begins in iak+1−ck+1¯ı; if ak+2 = ck+2, ω(sk+1) begins in i¯ı and since
ck+1 = 0, ω(sk) begins in i1+ak+1¯ı. The longest common preﬁx of

ω = T c1 ◦ τ a1
0 ◦ · · · ◦ T ck ◦ τ ak
k−1(ω(sk))

and T c1 ◦ τ a1
0 ◦ · · · ◦ T ck ◦ τ ak
k−1(i∞)

has the following length from Lemma 2.4:
∣
∣T c1 ◦ τ a1
0 ◦ · · · ◦ T ck ◦ τ ak
k−1(i1ak+2=ck+2 +ak+1−ck+1)
∣
∣ + ∣
∣τ a1
0 ◦ τ a2
1 ◦ · · · ◦ τ ak
k−1(i¯ı)
∣
∣ − 2

= (1ak+2=ck+2 + ak+1 − ck+1 − 1
) ∣
∣τ a1
0 ◦ τ a2
1 ◦ · · · ◦ τ ak
k−1(i)
∣
∣

+ |T c1 ◦ τ a1
0 ◦ · · · ◦ T ck ◦ τ ak
k−1(i)| + ∣
∣τ a1
0 ◦ · · · ◦ τ ak
k−1(i¯ı)
∣
∣ − 2

= (1ak+2=ck+2 + ak+1 − ck+1)
) ∣
∣τ a1
0 ◦ τ a2
1 ◦ · · · ◦ τ ak
k−1(i)
∣
∣

+ ∣
∣T c1 ◦ τ a1
0 ◦ · · · ◦ T ck ◦ τ ak
k−1(i¯ı)
∣
∣ − 2

=
 k∑

j=1 (aj − cj)qj−1 + (1ak+2=ck+2 + ak+1 − ck+1)qk

=
 k+1∑

j=1 (aj − cj)qj−1 + qk(1ak+2=ck+2).

Thus ω begins in a cyclic permutation of τ a1
0 ◦ τ a2
1 ◦ · · · ◦ τ ak
k−1(i) to power
∑k+1
j=1 (aj − cj)qj−1 + qk1ak+2=ck+2∣
∣τ a1
0 ◦ τ a2
1 ◦ · · · ◦ τ ak
k−1(i)
∣
∣ = 1ak+2=ck+2 +
 ∑k+1
j=1 (aj − cj)qj−1
qk .

Since τk−1(i) = ¯ıi, this power is exactly the value of r.
Next we consider the case m = sk − ck − 1 with 0 < ck < ak. Again, set i = k mod 2. From

ω = τ a1−c1
0 ◦ (T ◦ τ0)
c1 ◦ τ a2−c2
1 ◦ (T ◦ τ1)
c2 ◦ · · · ◦ τ ak−ck
k−1 ◦ (T ◦ τk−1)
ck(ω(sk)),

it is easy to see that ω(sk−ck) begins in i¯ı. Indeed, since ck ̸= 0, then ck+1 ̸= ak+1, and ω(sk)

begins in i, which gives ω(sk−ck) = (T ◦ τk−1)
ck(ω(sk)) begins in i, and then in i¯ı, since ii does

16 V. BERTH´E, C. HOLTON, AND L.Q. ZAMBONI

not occur in ω(sk−ck). We thus deduce that the longest common preﬁx of

ω = T c1 ◦ τ a1
0 ◦ · · · ◦ T ck−1 ◦ τ ak−1
k−2 ◦ τ ak−ck
k−1 (ω(sk−ck))

and T c1 ◦ τ a1
0 ◦ · · · ◦ T ck−1 ◦ τ ak−1
k−2 ◦ τ ak−ck
k−1 (i∞)
has length
∣
∣T c1 ◦ τ a1
0 ◦ · · · ◦ T ck−1 ◦ τ ak−1
k−2 ◦ τ ak−ck
k−1 (i)
∣
∣

+ ∣
∣τ a1
0 ◦ τ a2
1 ◦ · · · ◦ τ ak−1
k−2 ◦ τ ak−ck
k−1 (i¯ı)
∣
∣ − 2

= ∣
∣T c1 ◦ τ a1
0 ◦ · · · ◦ T ck−1 ◦ τ ak−1
k−2 (¯ı
ak−cki)
∣
∣ + ∣
∣τ a1
0 ◦ τ a2
1 ◦ · · · ◦ τ ak−1
k−2 (¯ı)
∣
∣

+ ∣
∣τ a1
0 ◦ τ a2
1 ◦ · · · ◦ τ ak−1
k−2 ◦ τ ak−ck
k−1 (i)
∣
∣ − 2

= ∣
∣T c1 ◦ τ a1
0 ◦ · · · ◦ T ck−1 ◦ τ ak−1
k−2 (i¯ı)
∣
∣ + (ak − ck) ∣
∣τ a1
0 ◦ τ a2
1 ◦ · · · ◦ τ ak−1
k−2 (¯ı)
∣
∣

+ ∣
∣τ a1
0 ◦ τ a2
1 ◦ · · · ◦ τ ak−1
k−2 ◦ τ ak−ck
k−1 (i)
∣
∣ − 2

=
 k−1∑

j=1 (aj − cj)qj−1 + (ak − ck)qk−1 + ∣
∣τ a1
0 ◦ τ a2
1 ◦ · · · ◦ τ ak−1
k−2 ◦ τ ak−ck
k−1 (i)
∣
∣

=
 k∑

j=1 (aj − cj)qj−1 + ∣
∣τ a1
0 ◦ τ a2
1 ◦ · · · ◦ τ ak−1
k−2 ◦ τ ak−ck
k−1 (i)
∣
∣ .

We also have ∣
∣τ a1
0 ◦ τ a2
1 ◦ · · · ◦ τ ak−1
k−2 ◦ τ ak−ck
k−1 (i)
∣
∣ = qk − ckqk−1
and thus ω begins in a cyclic permutation of τ a1
0 ◦ τ a2
1 ◦ · · · ◦ τ ak−1
k−2 ◦ τ ak−ck
k−1 (i) to power

1 +
 ∑k
j=1(aj − cj)qj−1
qk − ckqk−1 .

As in the ﬁrst case, this is exactly the value of r.
To prove the “conversely” part of the proposition, simply note that the formulas for the
lengths above do not depend on r or m at all. □

Corollary 3.5.

ice(ω) = lim sup
k→∞ max
 (∑k+1
j=1 (aj − cj)qj−1
qk , 1 +
 ∑k
j=1(aj − cj)qj−1
qk − ckqk−1
 )
 .

Proof. Set x(k) = 1ak+2=ck+2 +
 Pk+1
j=1 (aj −cj )qj−1
qk and y(k) = 1 +
 Pk
j=1(aj −cj )qj−1
qk−ckqk−1 . One has from
Proposition 3.3, ice(ω) = max(lim sup
k→∞ x(k), lim sup
k→∞, 0<ck<ak y(k)).

Observe that
• If ck = ak then y(k) = x(k − 2). Thus, if ck+2 = ak+2 then x(k) = y(k + 2).
• If ck = 0 and ck+1 = ak+1 then y(k) < y(k + 1) = x(k − 1).
• If ck = 0 and ck+1 < ak+1 then y(k) ≤ x(k).
The conclusion follows from these observations. □

INITIAL POWERS OF STURMIAN SEQUENCES 17

4. ice for some special Sturmian sequences.

4.1. Notation. In all that follows,

x(k) = 1ak+2=ck+2 +
 ∑k+1
j=1 (aj − cj)qj−1
qk ,

x′(k) =
 ∑k+1
j=1 (aj − cj)qj−1
qk ,

y(k) = 1 +
 ∑k
j=1(aj − cj)qj−1
qk − ckqk−1 .

One has ice(ω) = lim sup
k→∞ max(x(k), y(k)) = lim sup
k→∞ max(x′(k), y(k)).

4.2. Characteristic sequence. Recall that the characteristic sequence ω of slope α is the
sequence obtained by setting all of the cj equal to 0. We prove now Theorem 1.2 that we
recall below.

Theorem 1.2 Let ω be the characteristic Sturmian sequence of slope α. Then

ind
∗(α) = 1 + ice(ω).

Proof. We can easily compute ice(ω) for such sequences from Corollary 3.5:

ice(ω) = lim sup
k→∞ max
 (∑k+1
j=1 ajqj−1
qk , 1 +
 ∑k
j=1 ajqj−1
qk
 )

= lim sup
k→∞
 ∑k+1
j=1 ajqj−1
qk

= lim sup
k→∞
 qk+1 + qk − 2
qk

= lim sup
k→∞ 1 + qk+1
qk
= 1 + lim sup
k→∞ [ak+1; ak, . . . , a1]

= ind∗(α) − 1.
 □

This quantity is ﬁnite if and only if the ak are bounded. One has ice(ω) ≤ 3 if and only
if all but ﬁnitely many of the ak are equal to 1, in which case α ∈ Q(θ) and ice(ω) = 1 + θ.
We can recover the shift invariance of ice oﬀ the orbit of ω as follows. Let ω(−α) be the
Sturmian sequence of slope α coding the orbit of −α under under Rα, and let ω(1 − α) be
the Sturmian sequence of slope α coding the orbit of 1 − α under ˜Rα. These sequences are
the two shift preimages of the characteristic sequence ω, i.e.,

ω(−α) = 0ω and ω(1 − α) = 1ω.

18 V. BERTH´E, C. HOLTON, AND L.Q. ZAMBONI

Since σ(0a20a4 . . . ) = σ(a10a30 . . . ) = 0000 · · · = Ψ(ω), it follows from Proposition 2.8 that

Ψ(ω(−α)) = 0a20a4 . . . and Ψ(ω(1 − α)) = a10a30 . . . .

Corollary 3.5 shows that for c ∈ Kα, ice(Ψ
−1(c)) depends only on the tail of c, which is
by deﬁnition the same as that of σ(c) unless c ∈ {a10a30 . . . , 0a20a4 . . . }. Thus ice = ice ◦T
on Xα \ {ω(−α), ω(1 − α)}.
By Corollary 3.5, one checks that for ω(−α), x′(2k) ≥ x′(2k + 1) and y(2k) ≥ y(2k + 1)
for all k, and

lim supk→∞ max(x′(2k), y(2k)) = = lim supk→∞ max(
 P2k+1
j=1,odd aj qj−1
q2k , 1 +
 P2k
j=1,odd aj qj−1
q2k−2 ) =
= lim supk→∞ max( q2k+1
q2k , 1 + q2k−1
q2k−2 ),

hence ice(ω(−α)) = lim sup
k→∞ max(a2k+1 + q2k−1
q2k , 1 + a2k−1 + q2k−3
q2k−2 ),

and similarly
 ice(ω(1 − α)) = lim sup
k→∞ max(a2k+2 + q2k
q2k+1 , 1 + a2k + q2k−2
q2k−1 ).

This implies ice(ω(−α)) ≤ ice(ω) and ice(ω(1 − α)) ≤ ice(ω). One may have equality as in
the Fibonacci case (α = θ = [1; 1, 1, . . . ]), as well as a strict inequality as, for instance, for
α = [0; 3, 1, 3, 1, . . . ].

4.3. The “keep one” sequence. The aim of this section is to prove that there exists a
Sturmian sequence of slope α with very little repetition at the beginning, even if α has
unbounded partial quotients (and thus Xα has arbitrarily large powers in its language).

Proposition 4.1. For every irrational slope α there exists a Sturmian sequence ω ∈ Xα
such that ice(ω) ≤ 1 + θ.

Proof. This is a special case of (3) of Proposition 2.1, but we ﬁnd it interesting to speciﬁcally
give the S-adic expansion of such a point ω. Set ck = ak − 1 for all k and let ω ∈ Xα be the
corresponding Sturmian sequence. We claim that ice(ω) ≤ θ + 1. By Corollary 3.5,

ice(ω) = lim sup
k→∞ max
 (∑k+1
j=1 qj−1
qk , 1 +
 ∑k
j=1 qj−1
qk−1 + qk−2
 )

= lim sup
k→∞ max
 (

1 +
 ∑k
j=1 qj−1
qk , 1 +
 ∑k
j=1 qj−1
qk−1 + qk−2
 )

= 1 + lim sup
k→∞
 ∑k
j=1 qj−1
qk−1 + qk−2 .

Our next lemma completes the proof. □

Lemma 4.2. The continued fraction convergents qj satisfy
∑k
j=1 qj−1
qk−1 + qk−2 < θ.

INITIAL POWERS OF STURMIAN SEQUENCES 19

Proof. Our proof is far from elegant and requires consideration of several cases. Let fn be
the Fibonacci sequence f0 = 0, f1 = 1 and fn+1 = fn + fn−1. Also, set a′
1 = a1 + 1 and
a′
n = an for n ≥ 2.
If all of the a′
j, j = 1, . . . , k − 1, are equal to 1 then qj = fj+1 for 0 ≤ j ≤ k and
∑k
j=1 qj−1
qk−1 + qk−2 = fk+2 − 1
fk+1 < θ,

since fk+2/fk+1 is one of the continued fraction convergents for θ.
Otherwise we let ℓ ∈ {1, 2, . . . , k − 2} be the greatest index for which a′
ℓ ̸= 1, or we set
ℓ = 1 if a′
1 = · · · = a′
k−2 = 1 (and thus a′
k−1 > 1). We have

qr = fr−ℓ+1qℓ + fr−ℓqℓ−1 for ℓ ≤ r ≤ k − 2,

and from the recursive deﬁnitions,

Pk
j=1 qj−1
qk−1 + qk−2 = (fk−ℓ+2 − 1)qℓ + (fk−ℓ+1 − 1)qℓ−1 + (a′
k−1 − 1)qk−2 + Pℓ
j=1 qj−1
fk−ℓ+1qℓ + fk−ℓqℓ−1 + (a′
k−1 − 1)qk−2

= (fk−ℓ+2 − 1 + (a′
k−1 − 1)fk−ℓ−1)qℓ + (fk−ℓ+1 + (a′
k−1 − 1)fk−ℓ−2)qℓ−1 + Pℓ−1
j=1 qj−1
(fk−ℓ+1 + (a′
k−1 − 1)fk−ℓ−1)qℓ + (fk−ℓ + (a′
k−1 − 1)fk−ℓ−2)qℓ−1

= (fk−ℓ+2 + (a′
k−1 − 1)fk−ℓ−1)qℓ + (fk−ℓ+1 − a′
ℓ + (a′
k−1 − 1)fk−ℓ−2)qℓ−1 + Pℓ−2
j=1 qj−1
(fk−ℓ+1 + (a′
k−1 − 1)fk−ℓ−1)qℓ + (fk−ℓ + (a′
k−1 − 1)fk−ℓ−2)qℓ−1

≤ (fk−ℓ+2 + (a′
k−1 − 1)fk−ℓ−1)qℓ + (fk−ℓ+1 − (a′
ℓ − 1) + (a′
k−1 − 1)fk−ℓ−2)qℓ−1
(fk−ℓ+1 + (a′
k−1 − 1)fk−ℓ−1)qℓ + (fk−ℓ + (a′
k−1 − 1)fk−ℓ−2)qℓ−1 ,

since q0 +· · ·+qℓ−3 < qℓ−1. We shall use the fact that a+b
c+d is between a
c and b
d for any positive
real numbers a, b, c, d.
If a′
k−1 > 1 then, since fn+1+m
fn+m < θ for any positive integers m, n,

fk−ℓ+2 + (a
′
k−1 − 1)fk−ℓ−1
fk−ℓ+1 + (a
′
k−1 − 1)fk−ℓ−1 < θ

and fk−ℓ+1 − (a′
ℓ − 1) + (a′
k−1 − 1)fk−ℓ−2
fk−ℓ + (a′
k−1 − 1)fk−ℓ−2 < θ,

and the desired inequality follows.
We are left to consider the possibility that a′
k−1 = 1 and a′
ℓ > 1. The inequality above
simpliﬁes to ∑k
j=1 qj−1
qk−1 + qk−2 ≤ fk−ℓ+2qℓ + (fk−ℓ+1 − (a
′
ℓ − 1))qℓ−1
fk−ℓ+1qℓ + fk−ℓqℓ−1 .

If k − ℓ is even then fk−ℓ+2
fk−ℓ+1 < θ and fk−ℓ+1−(a′
ℓ−1)
fk−ℓ ≤ fk−ℓ+1−1
fk−ℓ < θ, and the desired inequality

follows. In case k−ℓ is odd, we have k−ℓ ≥ 3 and fk−ℓ+1
fk−ℓ < θ. Since (a′
ℓ−1)qℓ−1 > a′
ℓ−1
a′
ℓ+1 qℓ ≥ 1
3 qℓ,
we have ∑k
j=1 qj−1
qk−1 + qk−2 ≤ (fk−ℓ+2 − 1
3 )qℓ + fk−ℓ+1qℓ−1
fk−ℓ+1qℓ + fk−ℓqℓ−1

and the observation that fn− 1
3
fn−1 < θ for n ≥ 5 completes the proof. □

20 V. BERTH´E, C. HOLTON, AND L.Q. ZAMBONI

Remarks. By Proposition 3.3, all preﬁx powers r ≥ 2 in the “keep one” Sturmian sequence
of slope α are of the form

1 +
 ∑k
j=1 qj−1
qk or 1 +
 ∑k
j=1 qj−1
qk−1 + qk−2 .

We have qk ≥ qk−1 +qk−2 for k ≥ 2 and thus, by Lemma 4.2, the Sturmian sequence obtained
this way begins in no 1 + θ power at all. It is easy to see from the proof of Lemma 4.2 that

lim supk→∞ 1 +
 Pk
j=1 qj−1
qk−1+qk−2 ≤ 1 + θ with equality if and only if (ak)k≥1 has arbitrarily long
strings of consecutive ones. Thus, ice(“keep one”) ≤ 1 + θ. One can show that equality holds
in this last expression if and only if every sequence of slope α has ice ≥ 1 + θ.

4.4. The Fibonacci case. We prove some characteristic properties of the Fibonacci Stur-
mian shift X 1
θ = Xθ−1, which we henceforth denote by Xθ. Let us recall that according to
the results of Section 4.2, the function ice is shift invariant on Xθ, and ice(ω) = 1 + θ if ω
belongs to the Z-orbit of the characteristic sequence. The ﬁrst statement of the following
proposition also occurs in [9].

Proposition 4.3. Every ω in the Fibonacci shift Xθ begins in arbitrarily large cubes except
those ω in the shift orbit of the characteristic sequence. Furthermore, suppose ω ∈ Xθ is
not in the shift orbit of the characteristic sequence. Then ice(ω) = 2 + θ if and only if the
Ostrowski expansion (ck)k≥1 of ω contains arbitrarily long strings of consecutive 0s.

Proof. Here we have a1 = 0 and aj = 1 for all j ≥ 2. Observe that for ω ∈ Xθ,

ice(ω) = lim sup
k→∞ y(k).

Indeed, this is an immediate consequence of the following:
• if ak+1 = ck+1 = 1, then ck = 0, and y(k) = x′(k) + 1;
• if ck+1 = ck = 0, then y(k) = x′(k);
• if ck+1 = 0 and ck = 1, then ck−1 = 0, and y(k) = 1 + x′(k − 2).
Let ω be a Sturmian sequence of slope θ, with Ostrowski expansion (ck)k≥1, not belonging
to the shift orbit of the characteristic sequence. That is, (ck)k≥1 ends with neither 0101010 · · ·
nor 00000 · · · .
The pattern 001 must appear inﬁnitely often in the sequence (ck)k≥1. Consider an integer
k for which (ck−2, ck−1, ck) = (0, 0, 1). We have

y(k) = 1 + qk−2 + qk−3 + ∑k−3
j=2 (1 − cj)qj−1
qk−2 .

One easily proves by induction that for any positive integer ℓ,

ℓ∑

j=2 (1 − cj)qj−1 ≥ qℓ−1 − 1,

with equality if and only if cℓ−i ≡ ℓ − i + 1 mod 2, for j = 0, 1, . . . , ℓ − 1. Thus, if k is large
enough that (cj)
k−3
j=1 contains two consecutive 0s, the preﬁx of ω of length qk−2 has preﬁx
power
 y(k) ≥ 2 + qk−3 + qk−4
qk−2 = 3.

INITIAL POWERS OF STURMIAN SEQUENCES 21

Consider now an arbitrary index k. If ck = 0 then

y(k) = 1 +
 ∑k−1
j=2 (1 − cj)qj−1
qk

≤ 1 +
 ∑k−1
j=2 qj−1
qk

= 1 + qk+1 − 2
qk
< 1 + θ,

and if ck = 1 then
 y(k) = 2 +
 ∑k−2
j=2 (1 − cj)qj−1
qk−2

= 2 + qk−1 − ∑k−2
j=2 cjqj−1
qk−2 .

Since qk−1
qk−2 → θ as k → ∞, we see that ice(ω) = 2+θ if and only if (ck)k≥1 contains arbitrarily
long strings of consecutive 0s and inﬁnitely many 1s. □

5. Smallest prefix powers.

Now we turn our attention to minimizing ice over Xα and proving Theorem 1.1, which we
recall below.

Theorem 1.1 Let α = [0; a1, a2, a3, . . . ] be an irrational number and Xα be the set of all
Sturmian sequences of slope α. Then there is a Sturmian sequence ω ∈ Xα with ice(ω) = 2
if and only if for each pair of positive integers (s, t) with s > 1 there are only ﬁnitely many
k for which (ak, ak+1) = (s, t) or (ak, ak+1, ak+2) = (1, 1, t).

We deduce from this theorem that if min(ice(Xα)) = 2 then α has unbounded partial
quotients and only ﬁnitely many strings of more than than two consecutive 1s in its sequence
of partial quotients (ak)k≥1. The set of α with this property has measure zero, since every
ﬁnite sequence of positive integers appears inﬁnitely many times in the sequence of partial
quotients of almost every real number (see for instance [11]). In particular, no Sturmian shift
with a quadratic slope can contain a sequence of ice equal to 2, and by Proposition 2.11,
there are no substitutive Sturmian sequences ω with ice(ω) = 2.

5.1. Some ﬁrst restrictions. Given the partial quotients ak of α we must choose the ck
(satisfying the admissibility condition (1)) so as to minimize the lim sup in Corollary 3.5. A
couple of observations will help narrow the playing ﬁeld:
• If ak − ck > 2 for inﬁnitely many k then ice(ω) ≥ 3. Indeed if ak − ck ≥ 3, then
x′(k − 1) ≥ (ak−ck)qk−1
qk−1 ≥ 3.
• Given a sequence (ck) we can deﬁne a new sequence c′
k by setting

c′
k =
 {
ck if ak = ck or ak+1 = ck+1
ak − 1 otherwise.

22 V. BERTH´E, C. HOLTON, AND L.Q. ZAMBONI

The sequence c′
k also satisﬁes the admissibility condition (1) and determines a Stur-
mian sequence of slope α, and the only quantities in the formula of Corollary 3.5
which are increased by substituting the c′
k for the ck are the ones of the form

y(k) = 1 +
 Pk
j=1(aj −cj )qj−1
qk−ckqk−1 where k is an index for which c′
k ̸= ck, in which case
c′
k = ak − 1 > ck and

1 +
 ∑k
j=1(aj − c′
j)qj−1
qk − c′
kqk−1 = 1 +
 ∑k
j=1(aj − c′
j)qj−1
qk−1 + qk−2

< 1 +
 ∑k
j=1(aj − c′
j)qj−1
qk−1

≤
 ∑k
j=1(aj − cj)qj−1
qk−1
so that ice of the new sequence is no greater than that of the given sequence.
Consequently, in our quest to minimize ice over Xα we need only consider sequences where
for each k
• ck ∈ {0, ak − 1, ak},
• if ck = 0 or if ck+1 = ak+1, then ak = 1.

5.2. Special slopes. We describe those slopes α for which Xα has a sequence with ice
equal to 2. First we rule out some of the noncontenders. As before, α = [0; a1 + 1, a2, a3, . . . ],

x(k) = 1ak+2=ck+2 +
 Pk+1
j=1 (aj −cj )qj−1
qk , x′(k) =
 Pk+1
j=1 (aj −cj )qj−1
qk and y(k) = 1 +
 Pk
j=1(aj −cj )qj−1
qk−ckqk−1 .

Proposition 5.1. If (s, t) is a pair of integers with s > 1 such that (ak, ak+1) = (s, t) for
inﬁnitely many k then every ω ∈ Xα has ice(ω) ≥ 2 + 1
2(s+1)(t+1)+1 .

Proof. From the results of the previous section, we can restrict ourselves to sequences (ck)k≥1
which satisfy: for all k, if ck = 0 then ak = 1. Fix now an index k for which ak > 1 (and
hence ck ≥ 1). There are three cases to consider:
C1: ck+2 = ak+2. Then ck+1 = 0. We have

y(k + 2) = 1 +
 ∑k+1
j=1 (aj − cj)qj−1
qk

≥ 1 + ak+1 + ak−1qk−2
qk

≥ 1 + ak+1 + 1
2ak + 1.

C2: ck+2 ≤ ak+2 − 2. We have

x(k + 1) ≥ ak+2 − ck+2 +
 ∑k+1
j=1 (aj − cj)qj−1
qk+1

≥ ak+2 − ck+2 + akqk−1
qk+1

≥ ak+2 − ck+2 + 1
2ak+1 + 1.

INITIAL POWERS OF STURMIAN SEQUENCES 23

C3: ck+2 = ak+2 − 1. Using the fact that ck+1 < ak+1, which follows here from the
hypothesis that ak > 1, we have

y(k + 2) = 1 + qk+1 + ∑k+1
j=1 (aj − cj)qj−1
qk+1 + qk

≥ 1 + qk+1 + qk + ∑k
j=1(aj − cj)qj−1
qk+1 + qk

≥ 2 + ak−1qk−2
qk+1 + qk

≥ 2 + 1
2(ak + 1)(ak+1 + 1) + 1.

In every case, one of x(k + 1), y(k + 1) and y(k + 2) is at least 2 + 1
2(ak+1)(ak+1+1)+1 . The result
follows from this fact and Proposition 3.3. □

Proposition 5.2. If t is an integer such that (ak, ak+1, ak+2) = (1, 1, t) for inﬁnitely many
k then every ω ∈ Xα has ice(ω) ≥ 2 + 1
8t+1 .

Proof. Fix an index k for which ak = ak+1 = 1, and set t = ak+2. We can save ourselves
some labor by noting that in our proof of Proposition 5.1 the assumption ak > 1 was used
only in the third of the three cases, to deduce that ck+1 < ak+1; in the ﬁrst two cases
the same estimates are valid and we see that one of x(k + 1) and y(k + 2) is at least
2 + 1/9 ≥ 2 + 1/(8ak+2 + 1) = 2 + 1/(8t + 1).
In the case that ck+1 = ak+1 we must have ck+2 < ak+2; if we replace k with k+1 in our proof
of Proposition 5.1, we ﬁnd that one of x(k +2) and y(k +3) is at least 2+1/(4(ak+2 +1)+1) ≥
2 + 1/(8ak+2 + 1) = 2 + 1/(8t + 1). □

5.3. Proof of Theorem 1.1. Finally, we can prove the main theorem.

Proof of Theorem 1.1. One direction follows from the preceding propositions. Let us prove
the converse. Let α be as in the statement of the theorem,that is, for each pair of positive
integers (s, t) with s > 1 there are only ﬁnitely many indices k for which

(3) (ak, ak+1) = (s, t) or (ak, ak+1, ak+2) = (1, 1, t).

We shall deﬁne the sequence (ck)k≥1 and check that the Sturmian sequence it represents
has ice equal to 2. Since ice does not depend on the ﬁrst values of ck, we will deﬁne the ck for
k large enough such that the pattern 111 no longer appears in ak, ak+1, . . . . We just require
that the ﬁrst values of (ck)k≥1 satisfy the admissibility condition (1). Here it is:

ck =
 




ak − 1 if ak > 1, ak−1 > 1,
ak − 1 if ak > 1, ak−1 = ak−2 = 1,
ak if ak > 1, ak−1 = 1, ak−2 > 1,
0 if ak = 1 and ak−1 > 1
ak if ak = 1 and ak−1 = 1.

We verify the admissibility condition: If ck = ak then either ak > 1, ak−1 = 1 and ak−2 > 1
or ak = 1, ak−1 = 1 and thus ak−2 > 1; in both cases we have ck−1 = 0.

24 V. BERTH´E, C. HOLTON, AND L.Q. ZAMBONI

Note that ak − ck ∈ {0, 1} for all k ≥ 1, hence x′(k) ≤ y(k) for every k ≥ 1. Assume that
ice(ω) > 2. Then there exists ε > 0 such that y(k) ≥ 2 + ε holds for inﬁnitely many integers
k; among those k, one of the following four possibilities holds for inﬁnitely many of them:
A: ak > 1 and ck = ak − 1;
B: ak > 1 and ck = ak;
C: ak = ak−1 = 1;
D: ak = 1 and ak−1 > 1.

Case A: Suppose ak > 1 and ck = ak − 1. Then either ak−1 > 1 or ak−1 = ak−2 = 1. We thus
get
 2 + ε ≤ y(k) ≤ 1 +
 ∑k
j=1(aj − cj)qj−1
qk−1 + qk−2 ,

therefore
 (1 + ε)(qk−1 + qk−2) ≤
 k∑

j=1 qj−1 ≤ qk−1 + qk−2 + qk−3 +
 k−3∑

j=1 qj−1.

Since k−3∑

j=1 qj−1 ≤
 k−3∑

j=1 ajqj−1 ≤ qk−3 + qk−4,

we have ε(qk−1 + qk−2) ≤ 2qk−3 + qk−4,
hence ε(ak−1qk−2 + ak−2qk−3) ≤ 3qk−3 ≤ 3qk−2.
In particular, ε(ak−1qk−2) ≤ 3qk−2 and ε(ak−2qk−3) ≤ 3qk−3 hold for inﬁnitely many k,
therefore there exists a pair of integers (s, t) such that (ak−2, ak−1) = (s, t) for inﬁnitely
many k. It follows from our assumption (3) on α that s = 1. There are two cases to consider:
• s = t = 1, and thus for inﬁnitely many k,

(4) ak > 1, ak−1 = ak−2 = 1, ck = ak − 1, ck−1 = ak−1,

ak−3 > 1, ck−2 = 0, ck−3 ≥ ak−3 − 1,
and
 2 + ε ≤ y(k) ≤ 1 + qk−1 + qk−3 + qk−4 + ∑k−4
j=1 (aj − cj)qj−1
qk−1 + qk−2

= 1 + qk−1 + qk−2 + ∑k−4
j=1 (aj − cj)qj−1
qk−1 + qk−2 ,

and thus ε(qk−1 + qk−2) ≤ 2qk−4.
As

qk−1 + qk−2 = qk−2 + qk−3 + qk−3 + qk−4 = 3qk−3 + 2qk−4 ≥ (3ak−3 + 2)qk−4,

we see that ε(3ak−3 + 2)qk−4 ≤ 2qk−4.

INITIAL POWERS OF STURMIAN SEQUENCES 25

Since this inequality holds for inﬁnitely many k, there exists an integer s′ > 1 such
that ak−3 = s′, and ak−2 = t = 1 (by (4)) for inﬁnitely many k, a contradiction with
(3).
• s = 1 and t > 1. We thus have ak > 1, ak−1 = t > 1, ak−2 = 1, and ck = ak − 1. One
can assume ak−3 > 1, by assumption (3) on α (the pattern 11t appears only ﬁnitely
many times). Hence ck−1 = ak−1 and ck−2 = 0. We thus obtain by arguing as in case
s = t = 1, ε((t + 2)ak−3 + (t + 1))qk−4 ≤ 2qk−4.
Since this inequality holds for inﬁnitely many k, there exists an integer t
′ such that
ak−3 = t
′, ak−2 = 1 and ak−1 = t for inﬁnitely many k, a contradiction with (3).

Case B: Suppose ak > 1, ck = ak. Then ak−1 = 1, ak−2 > 1 and ck−1 = 0. We have

2 + ε ≤ y(k) = 1 + qk−2 + ∑k−2
j=1 (aj − cj)qj−1
qk−2 = 2 +
 ∑k−2
j=1 (aj − cj)qj−1
qk−2 ,

hence
 εqk−2 ≤ qk−3 +
 k−3∑

j=1 (aj − cj)qj−1 ≤ 3qk−3,

and εak−2qk−3 ≤ 3qk−3.
Since this inequality holds for inﬁnitely many k, there exists an integer s > 1 such that
ak−1 = 1 and ak−2 = s for inﬁnitely many k, a contradiction with (3).
Case C: Suppose ak = ak−1 = 1. Then, by hypothesis, ak−2 > 1, ck = 1 and ck−1 = 0. We
have
 2 + ε ≤ y(k) = 1 + qk−2 + qk−3 + ∑k−3
j=1 (aj − cj)qj−1
qk−2 ,

that is, εqk−2 ≤ 3qk−3,
and εak−2qk−3 ≤ 3qk−3.
Since this inequality holds for inﬁnitely many k, there once again exists an integer s > 1
such that for ak−1 = 1 and ak−2 = s for inﬁnitely many k, contrary to hypothesis (3).
Case D: Suppose ak = 1 and ak−1 > 1. Then ck = 0. One has

2 + ε ≤ y(k) ≤ 1 + qk−1 + qk−2 + ∑k−2
j=1 (aj − cj)qj−1
qk = 1 + qk + ∑k−2
j=1 (aj − cj)qj−1
qk ,

hence εqk ≤ qk−2 + qk−3,
and ε(ak−1 + 1)qk−2 ≤ ε(qk−1 + qk−2) ≤ 2qk−2.
These inequalities hold for inﬁnitely many k. It follows that for some s > 1 we have ak = 1
and ak−1 = s for inﬁnitely many k, a contradiction with (3). □

Acknowledgements. We would like to thank Boris Adamczewski, Jean-Paul Allouche,
Fabien Durand and Alain R´emondi`ere for many stimulating discussions.

26 V. BERTH´E, C. HOLTON, AND L.Q. ZAMBONI

References

[1] B. ADAMCZEWSKI, R´ep´etitions dans les codages de rotations, Adv. Appl. Math. 34 (2005), 1–29.
[2] B. ADAMCZEWSKI, Y. BUGEAUD, Transcendental continued fractions, preprint 2005.
[3] J.-P. ALLOUCHE, J. P. DAVISON, M. QUEFF´ELEC, L. Q. ZAMBONI, Transcendence of Sturmian
or morphic continued fractions, J. Number Theory 91 (2001), 39–66.
[4] P. ARNOUX, A.M. FISCHER, The scenery ﬂow for geometric structures on the torus: the linear setting,
Chin. Ann. of Math. 22B (2001), 1–44.
[5] P. ARNOUX, G. RAUZY, Repr´esentation g´eom´etrique de suites de complexit´e 2n + 1, Bull. Soc. Math.
France 119 (1991), 199–215.
[6] P. ARNOUX, S. FERENCZI, P. HUBERT, Trajectories of rotations, Acta. Arith. 87 (1999), 209–217.
[7] G. BARAT, P. LIARDET, Dynamical systems originated in the Ostrowski alpha-expansion, Publ. Math.
Debrecen, to appear.
[8] J. BERSTEL, Recent results in Sturmian words, in Developments in Language Theory, (Eds. J. Dassow,
A. Salomaa), World Scientiﬁc, Singapore (1996), 13–24.
[9] J. BERSTEL, On the index of Sturmian words, Jewels are Forever, Springer, Berlin (1999), 287–294.
[10] V. BERTH´E, Autour du syst`eme de num´eration d’Ostrowski, Bull. Belg. Math. Soc. Simon Stevin 8
(2001), 209–239.
[11] P. BILLINGSLEY, Ergodic theory and information, John Wiley & Sons Inc., New York, 1965.
[12] W.-T. CAO, Z.-Y. WEN, Some properties of the factors of Sturmian sequences, Theoret. Comput. Sci.
304 (2003), 365–385.
[13] J. CASSAIGNE, Special factors of sequences with linear subword complexity, Developments in Language
Theory II (DLT’95), Magdeburg (Allemagne), World Scientiﬁc (1996), 25–34.
[14] J. CASSAIGNE, Limit values of the recurrence quotient in Sturmian sequences, Theoret. Comput.
Science 218 (1999), 3–12.
[15] E. M. COVEN, G. A. HEDLUND, Sequences with minimal block growth, Math. Systems Theory 7
(1973), 138–153.
[16] D. CRISP, W. MORAN, A. POLLINGTON, P. SHIUE, Substitution invariant cutting sequences, J.
Th´eorie des Nombres de Bordeaux 5 (1993), 123–137.
[17] D. DAMANIK, D. LENZ, Uniform spectral properties of one-dimensional quasicrystals, I. Absence of
eigenvalues, Comm. Math. Phys. 207 (1999), 687–696.
[18] D. DAMANIK, D. LENZ, The index of Sturmian sequences, Europ. J. Combinatorics 23 (2002), 23–29.
[19] D. DAMANIK, R. KILLIP, D. LENZ, Uniform spectral properties of one-dimensional quasicrystals, III.
α-continuity, Comm. Math. Phys. 212 (2000), 191–204.
[20] I. R. DESCOMBES, Sur la r´epartition des sommets d’une ligne polygonale r´eguli`ere non ferm´ee, Ann.
Sci. ´Ecole Norm. Sup. 75 (1956), 284–355.
[21] Y. DUPAIN, V. T. S ´OS, On the one-sided boundedness of the discrepancy-function of the sequence nα,
Acta Arith. 27 (1980), 363–374.
[22] F. DURAND, A characterization of substitutive sequences using return words, Discrete Math. 179
(1998), 89–101.
[23] F. DURAND, Linearly recurrent subshifts have a ﬁnite number of non-periodic subshift factors, Ergodic
Theory Dynam. Systems 20 (2000), 1061–1078.
[24] F. DURAND, Combinatorial and Dynamical study of substitutions around the Theorem of Cobham,
Dynamics and Randomness, Nonlinear Phenomena and Complex Systems, Kluwer Acad. Pub (2002),
53–94.
[25] S. FERENCZI, Rank and symbolic complexity, Ergodic Theory Dynam. Systems 16 (1996), 663–682.
[26] P.J. GRABNER, P. LIARDET, R. TICHY, Odometers and systems of numeration, Acta Arith. 70
(1995), 103–123.
[27] C. HOLTON, L. Q. ZAMBONI, Descendants of primitive substitutions, Theory Comput. Systems 32
(1999), 133–157.
[28] S. ITO, H. NAKADA, Approximations of real numbers by the sequence nα and their metrical theory,
Acta Math. Hung. 52 (1988), 91–100.

INITIAL POWERS OF STURMIAN SEQUENCES 27

[29] J. JUSTIN, G. PIRILLO, Fractional powers in Sturmian words, Theoret. Comput. Science 223 (2001),
363–376.
[30] J. LESCA, Sur la r´epartition modulo 1 des suites nα, S´eminaire Delange-Pisot-Poitou (1966-67), Th´eorie
des Nombres, Fasc. 1, Exp. 15, 7 pp.
[31] J. LESCA, Sur la r´epartition modulo 1 de la suite nα, Acta Arith. 20 (1972), 345–352.
[32] M. LOTHAIRE, Algebraic combinatorics on words, Cambridge University Press 2002.
[33] F. MIGNOSI, Inﬁnite words with linear subword complexity, Theoret. Comput. Science 65 (1989),
221–242.
[34] F. MIGNOSI, G. PIRILLO, Repetitions in the Fibonacci inﬁnite word, RAIRO Inform. Theor. Appl.
26 (1992), 199–204.
[35] F. MIGNOSI, A. RESTIVO, S. SALEMI, Periodicity and the golden ratio, Theoret. Comput. Sci.
204(1988), 153–167.
[36] M. MORSE, G. A. HEDLUND, Symbolic dynamics II: Sturmian trajectories, Amer. J. Math. 62 (1940),
1–42.
[37] A. OSTROWSKI, Bemerkungen zur Theorie der Diophantischen Approximationen, I, II, Abh. Math.
Sem. Hamburg I (1922), 77–98 and 250–251.
[38] B. PARVAIX, Substitution invariant Sturmian bisequences, J. Th´eorie des Nombres de Bordeaux 11
(1999), 201–210.
[39] N. PYTHEAS FOGG, Substitutions in Dynamics, Arithmetics and Combinatorics, (Eds. V. Berth´e, C.
Mauduit, A. Siegel), Lecture Note in Mathematics 1794, Springer Verlag (2002).
[40] R. RISLEY, L.Q. ZAMBONI, A generalization of Sturmian sequences; combinatorial structure and
transcendence, Acta Arith. 95 (2000), 167–184.
[41] V. T. S ´OS, On the distribution mod 1 of the sequence nα, Ann. Univ. Sci. Budapest, E¨otv¨os Sect.
Math. 1 (1958), 127–134.
[42] M. STEWART, Irregularities of uniform distribution, Acta Math. Acad. Sci. Hung. 37 (1981), 185–221.
[43] D. VANDETH, Sturmian words and words with a critical exponent, Theoret. Comput. Science 242
(2000), 283–300.
[44] L. VUILLON, A characterization of Sturmian words by return words, European J. Combin. 22 (2001),
263–275.
[45] Z.-X. WEN, Z.-Y. WEN, Some properties of the singular words of the Fibonacci word, Europ. J. Combin.
15 (1994), 1–12.
[46] S.-i. YASUTOMI, Sturmian sequences which are invariant under some substitutions, Number theory
and its applications, (Eds. K. Gyory, S. Kanemitsu), Kluwer (1999), 347–373.

LIRMM, 161 rue Ada, F-34392 Montpellier cedex 5, France
E-mail address: berthe@lirmm.fr

Department of Mathematics, University of Texas, Austin TX 78712-0257, US
E-mail address: cholton@math.utexas.edu

Department of Mathematics, University of North Texas, Denton, TX 76203-5116, US
E-mail address: luca@unt.edu
