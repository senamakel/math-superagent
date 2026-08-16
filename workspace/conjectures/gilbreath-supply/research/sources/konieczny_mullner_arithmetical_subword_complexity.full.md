<!-- source: https://arxiv.org/pdf/2309.03180 | converted from PDF -->

arXiv:2309.03180v2  [math.NT]  7 Feb 2024
ARITHMETICAL SUBWORD COMPLEXITY
OF AUTOMATIC SEQUENCES

JAKUB KONIECZNY AND CLEMENS M ¨ULLNER

Abstract. We fully classify automatic sequences a over a ﬁnite alphabet Ω
with the property that each word over Ω appears is a along an arithmetic
progression. Using the terminology introduced by Avgustinovich, Fon-Der-
Flaass and Frid, these are the automatic sequences with the maximal possible
arithmetical subword complexity. More generally, we obtain an asymptotic
formula for arithmetical (and even polynomial) subword complexity of a given
automatic sequence a.
 1. Introduction

Automatic sequences — that is, sequences computable by ﬁnite automata, see
[AS03] for background — have long been studied from the point of view of com-
binatorics on words. A notable property of these sequences is that their subword
complexity is linear. To be more precise, for a sequence a = (a(n))
∞
n=0 taking values
in some ﬁnite alphabet Ω we deﬁne the subword complexity pa(ℓ) to be the number
of length-ℓ subwords that appear in a:

(1) pa(ℓ) = # {x = (x(i))
ℓ−1
i=0 ∈ Ωℓ ∣
∣ (∃ n ≥ 0) (∀ 0 ≤ i < ℓ) a(n + i) = x(i)
} .

If a is automatic then we have pa(ℓ) = Oa(ℓ), or in other words there exists a
constant Ca such that pa(ℓ) ≤ Caℓ for all ℓ ≥ 1. In fact, in many cases the
subword complexity can be computed explicitly. As an example, we may consider
the Thue–Morse sequence t, given by

(2) t(n) = s2(n) mod 2,

where s2(n) denotes the sum of binary digits of n. The subword complexity of t is

(3) pt(n) =
 {
3 · 2k + 4(r − 1) if n = 2k + r with 1 ≤ r ≤ 2k−1,
4 · 2k + 2(r − 1) if n = 2k + r with 2k−1 < r ≤ 2k.

(This sequence appears as A005942 on OEIS [OEI23, A008277].)

Date: February 8, 2024.
2020 Mathematics Subject Classiﬁcation. Primary: 11B85, 68R15.
Key words and phrases. automatic sequence, arithmetical subword complexity, Gowers norm.
During the initial work on this paper, the ﬁrst-named author worked within the framework
of the LABEX MILYON (ANR-10-LABX-0070) of Universit´e de Lyon, within the program ”In-
vestissements d’Avenir” (ANR-11-IDEX-0007) operated by the French National Research Agency
(ANR). Currently, he works at the University of Oxford and is supported by UKRI Fellowship
EP/X033813/1. The second-named author is supported by the Austrian-French project “Arith-
metic Randomness” between FWF and ANR (grant numbers I4945-N and ANR-20-CE91-0006).
For the purpose of open access, the authors have applied a Creative Commons Attribution (CC
BY) licence to any Author Accepted Manuscript version arising.

1

2 J. KONIECZNY AND C. M ¨ULLNER

However, automatic sequences can often look much more complicated along
subsequences. For instance, the restriction of the Thue–Morse sequence to the
squares (t(n2))
∞
n=0 is normal [DMR19], meaning that for each ℓ ≥ 1, each subword
x ∈ {0, 1}ℓ occurs with frequency 1/2ℓ,

lim
N →∞ 1
N # {n < N | (∀ 0 ≤ i < ℓ) t(n + i) = x(i)} = 1/2ℓ.

This result was later generalized to block-additive functions modulo m by the second
named author [M¨ul18]. Moreover, a similar result applies to the restrictions of the
Thue–Morse sequence to Piatetski-Shapiro sequences (t(⌊nc⌋)
∞
n=0 for 1 < c < 3/2
[MS17]. These results are conjectured to hold for larger exponents as well. It follows
from [Kon19] that, for a ﬁxed value of ℓ and suﬃciently large N , the restriction
of the Thue–Morse sequence to a randomly chosen length-ℓ arithmetic progression
contained in [N ] = {0, 1, . . . , N − 1} behaves like a random sequence in the sense
that for each ℓ ≥ 1 there exists c(ℓ) > 0 such that for each x = (x(i))
ℓ−1
i=0 ∈ {0, 1}ℓ

we have

#
 


(n, m) ∈ N2
0
 ∣
∣
∣
∣
∣
∣
 n + im < N and
t(n + im) = x(i)
for all 0 ≤ i < ℓ
 


 = N 2

2ℓ+1(ℓ − 1) + O(N 2−c(ℓ))

In particular, the Thue–Morse sequence has the largest possible arithmetical
subword complexity — a concept introduced by Avgustinovich, Fon-Der-Flaass
and Frid [AFDFF03] as an analogue of the usual subword complexity, which we
will presently introduce. For a sequence a = (a(n))
∞
n=0 taking values in some
ﬁnite set Ω the arithmetical subword complexity pAP
a (ℓ) is deﬁned as the number
of length-ℓ subwords that appear in a along an arithmetic progression:

(4) pAP
a (ℓ) = # {
x ∈ Ωℓ ∣
∣ (∃ n ≥ 0, m ≥ 1) (∀ 0 ≤ i < ℓ) a(n + im) = x(i)
} .

This notion was further studied in [Fri03a, Fri03b, Fri06, ACF06, CF07]. We also
point out that other modiﬁcations of the notion of subword complexity that have
been studied include d-complexity [Iv´a87], pattern complexity [RS02] and maximal
pattern complexity [KZ02]. In fact, we will consider an even more far-reaching
generalisation, which we dub polynomial subword complexity, counting the number
of subwords which appear along polynomials of some degree d:

(5) p≤d
a (ℓ) = # {x ∈ Ωℓ ∣
∣
∣
∣ (∃ P (X) ∈ R[X]) P (N0) ⊆ N0, deg P ≤ d,
(∀ 0 ≤ i < ℓ) a(P (i)) = x(i)
 } .

We point out that, because the deﬁnition of pAP
a in (1) includes the requirement
that m ̸= 0, setting d = 1 in (5) we do not exactly recover pAP
a . Nonetheless, we
have pAP
a (ℓ) ≤ p≤1(ℓ) ≤ pAP
a (ℓ) + #Ω. Moreover, we have the chain of inequalities

pa(ℓ) ≤ pAP
a (ℓ) ≤ p≤1
a (ℓ) ≤ p≤2
a (ℓ) ≤ p≤3
a (ℓ) ≤ · · · ≤ #Ωℓ.

We will say that a sequence a taking values in a ﬁnite set Ω has maximal arithmetical
subword complexity if pAP
a (ℓ) = #Ωℓ for all ℓ ≥ 1.

As mentioned above, this property is enjoyed by the Thue–Morse sequence. More
examples can also be found in [AFDFF03] and [Fri03a].
At the opposite extreme, it is possible for an automatic sequence to have very
low arithmetical or polynomial subword complexity. As a basic example, if a is

ARITHMETICAL SUBWORD COMPLEXITY OF AUTOMATIC SEQUENCES 3

periodic with period q ≥ 1 then for each d ≥ 1 we have

p≤d
a (ℓ) ≤ qd+1,

which is a direct consequence of the fact that the sequence α0 + α1i + . . . αdid mod
q (i ∈ N0) is completely determined by its initial d + 1 terms. A less trivial
example concerns (forwards) synchronising sequences, that is, automatic sequences
a with the property that there exists a word w ∈ Σ∗
k such that for u, v ∈ Σ∗
k,
the value a([uwv]k) depends only on v (and hence is equal to a([wv]k). Here,
Σk = {0, 1, . . . , k − 1} denotes the set of base-k digits, Σ∗
k denotes the set of all
words over Σk, and [u]k for u ∈ Σ∗
k denotes the integer encoded by u. For such
sequences it was proved by Deshouillers, Drmota, Shubin, Spiegelhofer and the
second author in [DDM
+24],
 p≤d
a (ℓ) ≤ exp o(ℓ),(6)

which is in stark contrast to the behaviour of other automatic sequences such as the
Thue–Morse sequence. This was an important intermediate goal to being able to
study the subword complexity of synchronizing automatic sequences along ⌊nc⌋ or
more generally along Hardy sequences of polynomial growth, which was the main
motivation in [DDM
+24]. Finally, we mention backwards synchronising sequences,
that is, automatic sequences a with the property that there exists a word w ∈ Σ∗
k
such that for u, v ∈ Σ∗
k, the value a([uwv]k) depends only on u (and hence is equal
to a([uw]k). While arithmetical subword complexity of such sequences has not been
previously studied, in analogy with the results in [DDM
+24] it will not come as a
surprise that (6) holds also in this case.
Our goal is to obtain a description of the asymptotic behaviour of the arithmetic
(and polynomial) subword complexity for an arbitrary automatic sequence a. Mo-
tivated by the examples mentioned above, we introduce the family AP k consisting
of all sets P of the form

(7) P = {n ∈ N0
 ∣
∣
∣
∣ the base-k expansion of n begins with u, ends with v,
has length ≡ ℓ mod m, and n ≡ c mod q
 }

where u, v ∈ Σ∗
k, u does not begin with 0, 0 ≤ ℓ < m and 0 ≤ c < q are integers
with q coprime to k. We think of these sets as a generalisation of the notion of a
residue class, but additionally accounting for the behaviour of the base-k expansion.
We note that this notion is stable under change of base in the sense that if K is a
power of k then AP K ⊆ AP k and each set in AP k is a ﬁnite union of sets in AP K.
With this notion in place, we are ready to introduce the parameter which controls
the arithmetical subword complexity of an automatic sequence.

Deﬁnition 1.1. Let a = (a(n))
∞
n=0 be a k-automatic sequence taking values in
a ﬁnite set Ω. The eﬀective alphabet size of a is the largest integer r with the
property that there exists P ∈ AP k such that a takes at least r diﬀerent values on
each Q ∈ AP k with Q ⊆ P .

In fact, since in the deﬁnition above we can freely replace P with a smaller
element of AP k, if a is a k-automatic sequence with eﬀective alphabet size r then
there exists Θ ⊆ Ω with #Θ = r and P ∈ AP k such that for each Q ∈ AP k with
Q ⊆ P the set of values taken by a on Q is precisely Θ. Additionally, r is the
largest integer with this property.
The rationale behind the name “eﬀective alphabet size” is that, with notation
as in Deﬁnition 1.1, for each ε > 0 we can ﬁnd a partition N0 = P1 ∪ P2 ∪ · · · ∪

4 J. KONIECZNY AND C. M ¨ULLNER

PN ∪ Q1 ∪ Q2 ∪ · · · ∪ QM into elements of AP k such that a takes at most r distinct
values of each Pi (1 ≤ i ≤ N ) and d(Q1 ∪ Q2 ∪ · · · ∪ QM ) < ε. (We do not prove
this result since we do not rely on it, but it is not hard to obtain it using techniques
used in this paper.) Thus, up to a negligible error, one can think of a as the result
of “glueing together” sequences on alphabets of size r.

Example 1.2. (i) If a is periodic, forwards synchronising or backwards syn-
chronising, then r(a) = 1.
(ii) If a takes the form a(n) = F (b(n), c(n)) for k-automatic sequences b and c
and a map F , then r(a) ≤ r(b)r(c).
(iii) If r(a) = 1 then a is strongly structured in the sense of [BKM23], see Section
2.2 for further discussion.

We are now ready to state our main result.

Theorem A. Let a = (a(n))
∞
n=0 be a k-automatic sequence with eﬀective alphabet
size r (cf. Deﬁnition 1.1). Then for each d ∈ N we have

rℓ ≤ pAP
a (ℓ) ≤ p≤d
a (ℓ) ≤ rℓ exp (o(ℓ)) .

Remark 1.3. Using similar methods, one could obtain a more precise upper bound
of the form rℓ exp (O(ℓη)) for some η < 1; cf. Remark 4.7. For the sake of exposi-
tion, we prove a slightly weaker bound rℓ exp (o(ℓ)), which allows us to avoid some
technical computations.

As alluded to earlier, a particularly interesting case of Theorem A is when r(a) =
#Ω, meaning that the sequence a has maximal arithmetical subword complexity.

Corollary 1.4. Let a = (a(n))
∞
n=0 be a k-automatic sequence taking values in a
ﬁnite set Ω. Then a has maximal arithmetical subword complexity if and only if
there exists P ∈ AP k such that for each Q ∈ AP k with Q ⊆ P and each x ∈ Ω
there exists n ∈ Q with a(n) = x.

The criterion in Corollary 1.4 may come across as somewhat complicated. In the
case where the alphabet Ω has two elements, we have a simple suﬃcient condition.

Corollary 1.5. Let a = (a(n))
∞
n=0 be a k-automatic sequence taking values in
{0, 1} and suppose that there exists α ∈ (0, 1) such that for all A > B ≥ 0 we have

1
N
 N −1∑

n=0 a(An + B) → α as N → ∞.

Then a has maximal arithmetical subword complexity.

By the same token, if a instead takes values in a ﬁnite set Ω then for a to have
maximal arithmetical subword complexity it is enough that for each x ∈ Ω there
exists αx ∈ (0, 1) such that for all A > B ≥ 0 we have
1
N # {n < N | a(An + B) = x} → αx as N → ∞.

If the condition above is true, one might say that the sequence a is totally asymp-
totically equidistributed with respect to the measure on Ω given by (αx)x∈Ω.
Inspecting the proof of Theorem A we also notice that the conditions therein
guarantee not only maximal arithmetical subword complexity but also positive
frequency of all subwords.

ARITHMETICAL SUBWORD COMPLEXITY OF AUTOMATIC SEQUENCES 5

Corollary 1.6. Let a = (a(n))
∞
n=0 be a k-automatic sequence with maximal arith-
metical subword complexity, taking values in a ﬁnite set Ω. Then for each ℓ ≥ 1
and x ∈ Ωℓ we have

lim inf
N →∞ 1
N 2 # {
(n, m) ∈ N2
0
 ∣
∣
∣
∣ n + im < N and a(n + im) = x(i)
for all 0 ≤ i < ℓ
 } > 0.

Acknowledgements. The authors wish to thank Anna Frid for helpful comments
on arithmetical subword complexity, and to Boris Adamczewski for inspiring con-
versations.

Notation. We let N = {1, 2, . . . } denote the set of positive integers and put N0 =
N ∪ {0}. For N ∈ N we let [N ] = {0, 1, 2, . . . , N − 1} denote the length-N initial
interval of N0. We usually let k denote the base in which we work; thus k is an
integer with k ≥ 2. We let Σk = {0, 1, . . . , k −1} denote the set of base-k digits, and
Σ∗
k denote the set of words over Σk. For u ∈ Σk we let |u| denote the length of u.
For u ∈ Σk, [u]k ∈ N0 denotes the corresponding integer, and for n ∈ N0, (n)k ∈ Σ∗
k
denotes the base-k expansion of n without any leading zeros. In particular, (0)k = ǫ
is the empty word, and [(n)k]k = n for all n ∈ N0. We use standard asymptotic
notation, such as O(·) and ≫. This includes the notation f (n) = Θ(g(n)) for
f (n) = O(g(n)) and g(n) = O(f (n)).

2. Preliminaries

2.1. Automata. A deterministic k-automaton with output (or simply an automa-
ton if there is no risk of confusion) is a sextuple A = (S, s0, Σk, δ, Ω, τ ) where S is
a ﬁnite set of states, s0 ∈ S is the initial state, δ : S × Σk → S is the transition
function, Ω is the output set, and τ : S → Ω is the output function. We extend δ
to a map δ : S × Σ∗
k → S by declaring δ(s, uv) = δ(δ(s, u), v). The automaton A
computes the sequence aA given by a(n) = τ (δ(s0, (n)k)).
The automaton A is strongly connected if the underlying directed graph en-
joys this property, meaning that for each s, s′ ∈ S there exists u ∈ Σ∗
k such
that δ(s, u) = s′. The automaton A is primitive if it is strongly connected and
gcd ({|u| | u ∈ Σ∗
k, δ(s0, u) = s0}) = 1. A strongly connected component of A is a
maximal subset of states such that the corresponding directed graph is strongly
connected. A ﬁnal component is a strongly connected component from which no
other strongly connected component is reachable.
The automaton A is synchronising if there exists a state s1 ∈ S and a word
w ∈ Σ∗
k (sometimes called a synchronising word) such that δ(s, w) = s1 for all
s ∈ S. An automatic sequence is (forwards) synchronising if it is produced by
a synchronising automaton. Likewise, a sequence is backwards synchronising if it
is produced by a synchronising automaton reading input starting with the least
signiﬁcant digit. Alternative characterisations of these notions, already mentioned
in the introduction, are given in [BKM23, Lem. 3.2].
A set A ⊆ N0 is k-automatic if the corresponding indicator function 1A is auto-
matic. We let dlog(A) = limN →∞ 1/(log N ) ∑N −1
n=0 1A(n)/(n + 1) denote the loga-
rithmic density of a set A; the logarithmic density exists for all automatic sets.

2.2. Higher order Fourier analysis. Our argument hinges on a decomposition
constructed by J. Byszewski and the authors in [BKM23]. For a map f : [N ] → C

6 J. KONIECZNY AND C. M ¨ULLNER

and an integer d ≥ 1 we deﬁne the corresponding Gowers norm

∥f ∥U d[N ] =
 

E
n
 ∏

ω∈{0,1}d C|ω|f (n0 + ω1n1 + · · · + ωdnd)




1/2
d
 ,

where En denotes the average over all n = (n0, n1, . . . , ns) ∈ Z
d+1 such that n0 +
ω1n1 + · · · + ωdnd ∈ [N ] for all ω = (ω1, ω2, . . . , ωd) ∈ {0, 1}d, |ω| denotes the
number of indices i such that ωi = 1, and C denotes the complex conjugation.
For a comprehensive discussion on Gowers norms we refer to [Tao12]. A brief
introduction, adapted to the current application, can also be found in [BKM23, Sec.
2]. With this piece of notation in hand, we are ready to state the main result of
[BKM23]

Theorem 2.1. Let a = (a(n))
∞
n=0 be a complex-valued k-automatic sequence. Then
there exists a decomposition a = astr + auni where:
(i) auni is Gowers uniform in the sense that for each s ≥ 1 there exists c(s) > 0
such that ∥auni∥U s+1[N ] = O(N −c(s)) as N → ∞;
(ii) astr is structured in the sense that there exists an integer K that is a power
of k, a periodic sequence aper with period coprime to k, a K-automatic forwards
synchronising sequence afs, and a K-automatic backwards synchronising sequence
abs, taking values in some ﬁnite sets Ωper, Ωfs, Ωbs respectively, as well as a map
F : Ωper ×Ωfs ×Ωbs → C, such that astr(n) = F (astr(n), afs(n), abs(n)) for all n ≥ 0.

In general, the structured part astr of an automatic sequence can be somewhat
complicated. However, in [BKM23] we showed that astr = 0 almost everywhere
(i.e., # {n < N | astr(n) ̸= 0} /N → 0 as N → ∞) if and only if for all integers
A > B ≥ 0 we have
 1
N
 N −1∑

n=0 a(An + B) → 0 as N → ∞.

The following lemma elucidates the connection between the concept of eﬀective
alphabet size from Deﬁnition 1.1 and the structured part of an automatic sequence
in Theorem 2.1. Recall that the family AP k consists of sets of the form (7).

Lemma 2.2. Let A ⊆ N0 be a k-automatic set and let R ∈ AP k. Then the
following conditions are equivalent.
(i) There exists P ∈ AP k with P ⊆ R such that for each Q ∈ AP k with Q ⊆ P
we have A ∩ Q ̸= ∅.
(ii) There exists P ∈ AP k with P ⊆ R such that for each Q ∈ AP k with Q ⊆ P
we have dlog(A ∩ Q) > 0.
(iii) We have dlog(A ∩ R) > 0.
(iv ) There exists P ∈ AP k with P ⊆ R such that 1A,str is constant and strictly
positive on P .

Proof. Replacing A with A ∩ R, we may freely assume that R = N0. We will prove
implications (i) ⇒ (ii), (iii) ⇒ (iv) ⇒ (ii). Since the implications (ii) ⇒ (i) and (ii)
⇒ (iii) are immediate, this will ﬁnish the argument.
(i) ⇒ (ii): Let P be as in (i). For the sake of contradiction, suppose that for
some Q ∈ AP k we have dlog(A ∩ Q) = 0. Since the set A ∩ Q is automatic, it follows
that there exists a word w ∈ Σ∗
k which does not appear in the base-k expansion of

ARITHMETICAL SUBWORD COMPLEXITY OF AUTOMATIC SEQUENCES 7

any n ∈ A ∩ Q (see e.g. [BKM23, Lem. 3.1]). However, there exists Q′ ∈ AP k with
Q′ ⊆ Q such that w appears in the base-k expansion of all n ∈ Q′. It follows that
A ∩ Q′ = ∅, contradicting (i).
(iii) ⇒ (iv): For each ε > 0 there exists a partition

N0 = P1 ∪ P2 ∪ · · · ∪ PN ∪ E

where for each Pi ∈ AP k and 1A,str is constant on Pi for 1 ≤ i < N and dlog(E) < ε.
Picking ε = dlog(A), we see that there exists some cell P = Pi in the partition
above such that dlog(A ∩ P ) > 0 and 1A,str is constant on P and takes some value
α ∈ [0, 1]. It remains to show that α > 0. Because 1P is strongly structured
and hence asymptotically orthogonal to all Gowers uniform functions (cf. [BKM23,
Prop. 2.5]), we have

0 < dlog(A ∩ P ) = lim
N →∞ 1
log N
 N −1∑

n=0
 1P (n)1A(n)
n + 1

= lim
N →∞ 1
log N
 N −1∑

n=0
 α1P (n)
n + 1 + 1P (n)1A,uni(n)
n + 1 = αdlog(P ).

In particular, α = dlog(A ∩ P )/dlog(P ) > 0.
(iv) ⇒ (ii): Let P be as in (iv), and let α > 0 be the value that 1A,str takes
on P . For Q ∈ AP k with Q ⊆ P we have, by the same computation as above,
dlog(A ∩ Q) = αdlog(Q) > 0. □

We now have all the ingredients necessary to see that Corollary 1.5 follows from
Theorem A.

Proof of Corollary 1.5. It follows from the criterion for vanishing of the structured
part, mentioned earlier in this section, that astr is almost everywhere constant and
takes a value strictly between 0 and 1. Hence, bearing in mind that 1a−1(1) = a
and 1a−1(0) = 1 − a, we conclude from Lemma 2.2 that r(a) = 2, as needed. □

3. Lower bound

In this section, we prove the lower bound in Theorem A, that is, pAP
a (ℓ) ≥ rℓ.
This is a standard application of the tools of higher order Fourier analysis. A key
ingredient in the argument is the following variant of the generalised von Neumann
theorem, see e.g. [Tao12, Ex. 1.3.23] or [BKM23, Prop. 2.1]. Below, we call a map
f : X → C 1-bounded if ∥f ∥∞ := supx∈X |f (x)| ≤ 1.

Proposition 3.1. Fix ℓ ≥ 1. Let N ≥ 1 and let f0, f1, . . . , fℓ−1 : [N ] → C be
1-bounded maps. Then
∣
∣
∣
∣
∣
 N −1∑

n,m=0
 ℓ−1∏

i=0 fi(n + im)

∣
∣
∣
∣
∣ ≪ N 2 min
0≤i<ℓ ∥fi∥U ℓ−1[N ] .

(Above, the constant implicit in the ≪ notation is allowed to depend on ℓ.) As
an immediate corollary, we have the following counting lemma.

Lemma 3.2. Fix ℓ ≥ 1. Let N ≥ 1, ε > 0, let f0, f1, . . . , fℓ−1 : [N ] → C be
1-bounded and assume that for each 0 ≤ i < ℓ we have a decomposition fi =

8 J. KONIECZNY AND C. M ¨ULLNER

fi,str + fi,uni where fi,str : [N ] → C are 1-bounded and ∥fi,uni∥U ℓ−1[N ] ≤ ε. Then

N −1∑

n,m=0
 ℓ−1∏

i=0 fi(n + im) =
 N −1∑

n,m=0
 ℓ−1∏

i=0 fi,str(n + im) + O(εN 2).

We are now ready to approach the proof of the lower bound. Let a be a k-
automatic sequence with eﬀective alphabet size r, and ﬁx ℓ ∈ N. Pick P ∈ AP k such
that a takes at least r values on each Q ∈ AP k, Q ⊆ P . Note that each P ′ ∈ AP k
with P ′ ⊆ P also enjoys the property mentioned above. Replacing P with a some
P ′ ∈ AP k with P ′ ⊆ P , we can assume that a takes on P exactly r diﬀerent values
ω1, ω2, . . . , ωr. By Lemma 2.2 we can construct a sequence P1, P2, . . . , Pr ∈ AP k
with P ⊃ P1 ⊃ P2 ⊃ · · · ⊃ Pr such that for each 1 ≤ i ≤ r, the sequence 1a(ωi)−1,str
is constant on Pi and takes some strictly positive value αi.
Put Q := Pr, Θ := {ω1, ω2, . . . , ωr}, δ := min
1≤i≤r α
ℓ
i and let N be a large integer.

For x = (x(i))
ℓ−1
i=0 ∈ Θℓ, consider the set

S(x, N ) := {
(n, m) ∈ N2
0
 ∣
∣
∣
∣ n + im < N, n + im ∈ Q, and
a(n + im) = x(i) for all 0 ≤ i < ℓ
 } .

We will show that #S(x, N ) ≫ N 2, which for suﬃciently large N implies that
#S(x, N ) > N and consequently x appears in a along an arithmetic progression. It
will follow that pAP
a (ℓ) ≥ #Θℓ = rℓ, as needed. This estimate also yields Corollary
1.6.
If follows from Theorem 2.1 combined with e.g. [BKM23, Prop. 2.5] that there
is a positive constant c such that ∥
∥1Q1a−1(ω),uni∥
∥
U ℓ−1[N ] ≪ N −c for all ω ∈ Ω. It
follows from Lemma 3.2 that

#S(x, N ) =
 N −1∑

n,m=0
 ℓ−1∏

i=0
 (
1Q∩[N ]1a−1(x(i))) (n + im)

=
 N −1∑

n,m=0
 ℓ−1∏

i=0 1Q∩[N ](n + im)1a−1(x(i)),str(n + im) + O(N 2−c)

≥ δ · # {
(n, m) ∈ N2
0 ∣
∣ n + im ∈ Q ∩ [N ] for all 0 ≤ i < ℓ} + O(N 2−c)

≫ N 2.

Thus, the argument is complete.

4. Upper bound

In this section, we prove the upper bound in Theorem A. It will be convenient to
ﬁrst consider the special case where the sequence is primitive. A key idea behind
our argument is to construct an alterative description of the eﬀective alphabet size
r(a), which is stated as Proposition 4.5.

4.1. Primitive case. Let a be a primitive automatic sequence produced by an
automaton A = (S, s0, Σk, δ, Ω, τ ) which ignores the leading zeros (i.e., δ(s0, 0) =
s0).
We will need the notion of the height of a substitution (taken from [Que10]):
Let us consider a primitive substitution η : Λ → Λk with a ﬁxed point u ∈ Λ∞ (i.e.

ARITHMETICAL SUBWORD COMPLEXITY OF AUTOMATIC SEQUENCES 9

η(u) = u). The height measures in some sense how far u is from being a periodic
sequence. For every n ≥ 0 we put

Rn = {d ≥ 1 : u(n + d) = u(n)} and gn = gcd Rn.

Deﬁnition 4.1. The height of η, denoted by h = h(η), is the number

h = max {m ≥ 1 | gcd(m, k) = 1, m | g0} .

We list some standard properties of the height, which can be found in [Que10].

Proposition 4.2. (i) For each n ≥ 0 we have

h = max {m ≥ 1 | gcd(m, k) = 1, m | gn} .

(ii) If h = #Λ then u is periodic.
(iii) For each 0 ≤ j < h we consider the class

Cj = {u(n) : n ≡ j mod h}.

These classes form a partition of Λ. If we identify in u the letters in the same class
Cj, we thus obtain a periodic sequence, and h is the largest positive integer coprime
to k with this property.

Let t(n) = δ(s0, (n)k) denote the state reached by A upon reading n as input.
Note that the sequence t = (t(n))
∞
n=0 is produced by the same automaton as a,
with the output function replaced by the identity map. The sequence t is also the
ﬁxed point of the substitution S → S given by s ↦→ (δ(s, 0), δ(s, 1), . . . , δ(s, k − 1)).
With the sets Cj deﬁned as above, we let j(n) denote the unique index such that
t(n) ∈ Cj(n). We point out that the sequence j = (j(n))
∞
n=0 is periodic (in fact,
j(n) = n mod h). Replacing k (and hence also η) with a suitable power, we may
freely assume that k ≡ 1 mod h.
We will need the following technical lemma. A similar argument can be found
in [M¨ul17].

Lemma 4.3. Let q, m > 0 be integers, with q coprime to k. Then for each n ∈ hZ
and ℓ ∈ N there exists u ∈ Σ∗
k such that δ(s0, u) = s0, |u| ≡ ℓ mod m and [u]k ≡
n mod q.

Proof. We may assume that h | q. For s, s′ ∈ S and ℓ ∈ Z/mZ consider the set

W (s, s′; ℓ) = {[u]k mod q | δ(s, u) = s′, |u| ≡ ℓ mod m} ⊆ Z/qZ.

Since A is primitive, all sets W (s, s′; ℓ) are non-empty. The composition rule for δ
implies that

(8) W (s, s′; ℓ)kℓ′ + W (s′, s′′; ℓ′) ⊆ W (s, s′′; ℓ + ℓ′)

for all s, s′, s′′ ∈ S and ℓ, ℓ′ ∈ Z/mZ. Comparing the cardinalities of the sets in (8),
we see that the inclusion is in fact an equality:

(9) W (s, s′; ℓ)kℓ′ + W (s′, s′′; ℓ′) = W (s, s′′; ℓ + ℓ′).

Setting s = s′ = s′′ and ℓ = ℓ′ = 0 in (9), we see that W (s, s; 0) is a subgroup
H = mZ/qZ ⊆ Z/qZ, where m | q is independent of s. In general, W (s, s′; ℓ) =
H + w(s, s′; ℓ) is a coset of H (here, w(s, s′; ℓ) ∈ Z/qZ). Thus, (9) becomes

(10) w(s, s′; ℓ)kℓ′ + w(s′, s′′; ℓ′) ≡ w(s, s′′; ℓ + ℓ′) mod m.

10 J. KONIECZNY AND C. M ¨ULLNER

Recall that δ(s0, 0) = s0 and consequently 0 ∈ W (s0, s0, 1) and w(s0, s0, 1) ≡
0 mod m. By the same token, w(s0, s0, ℓ) ≡ 0 mod m for all ℓ. As a consequence,

{[u]k mod q | δ(s0, u) = s0} = ⋃

ℓ∈Z/mZ W (s0, s0; ℓ) = H.

It follows that H = hZ/qZ, and the argument is complete. □

The second ingredient which we will need comes from [M¨ul17]. Let c denote the
least possible cardinality of the set δ(S, w) = {δ(s, w) | s ∈ S} for w ∈ Σ∗
k, and
let M = {M0, M1, . . . , Mp−1} denote the family of all possible sets of the form
δ(S, w) with cardinality c. For n ≥ 0, let i(n) denote the unique index such that
δ(M0, (n)k) = Mi(n). Without loss of generality, we may assume that s0 ∈ M0,
which implies that t(n) ∈ Mi(n) for all n.
Finally, for 0 ≤ i < p and 0 ≤ j < h we let Si,j = Mi ∩ Cj. We point out that
for all n we have t(n) ∈ Si(n),j(n).

Example 4.4. Let us take k = 3 and consider the automaton A depicted by the
following diagram:
 αstart
 β
 γ

δǫ

0
 0
 0
 0,2

0,2

1

2 1
2
 1
2
 1

1

We compute the corresponding automatic sequence

α, ǫ, β, ǫ, δ, ǫ, β, γ, α, ǫ, δ, ǫ, δ, γ, α, . . .

which shows R0 = {8, 14, . . .} and g0 | 2, which implies h | 2. Moreover, considering
the sets C0 = {α, β, δ} and C1 = {γ, ǫ} one ﬁnds h = 2.
Moreover, we have c = 4 and M0 = {α, β, γ, ǫ} and M1 = {α, γ, δ, ǫ}. The sets
Si,j = Mi ∩ Cj are given by:

S0,0 = {α, β}, S0,1 = {γ, ǫ},

S1,0 = {α, δ}, S1,1 = {γ, ǫ}.

Proposition 4.5. With the same notation as above, we have

r(a) = max
i,j #{τ (s) : s ∈ Si,j}.

Proof. The inequality

(11) r(a) ≤ max
i,j #{τ (s) : s ∈ Si,j}

ARITHMETICAL SUBWORD COMPLEXITY OF AUTOMATIC SEQUENCES 11

is relatively simple. Indeed, since (i(n))n is synchronising and (j(n))n is periodic,
for each P ∈ AP k we can ﬁnd Q ∈ AP k with Q ⊆ P and 0 ≤ i < p and 0 ≤ j < h
such that i(n) = i and j(n) = j for all n ∈ Q. Hence, t(n) ∈ Si,j and a(n) ∈ {τ (s) :
s ∈ Si,j} for all n ∈ Q, which implies that r(a) ≤ #{τ (s) : s ∈ Si,j}, and (11)
follows.
It remains to prove the reverse inequality

(12) r(a) ≥ max
i,j #{τ (s) : s ∈ Si,j}.

Pick a minimal set Mi ∈ M and a residue j mod h (0 ≤ i < p, 0 ≤ j < h). There
exists P ∈ AP k such that for all n ∈ P we have i(n) = i and j(n) = j. We will
show that for each Q ∈ AP k with Q ⊆ P and each s ∈ Si,j there exists n ∈ Q such
that t(n) = s. Since i and j were arbitrary, once this is accomplished, (12) will
follow.
Replacing Q with a smaller set if needed, we can assume that Q takes the form

Q = {n ∈ N0 | n ≡ j′ mod q, (n)k ∈ uΣ∗
Kv}

for some K that is a power of k, u, v ∈ Σ∗
k and some 0 ≤ j′ < q with q coprime to
k. (Here and elsewhere, we identify ΣK with Σlogk K
k .) Without loss of generality
we may assume that h | q and thus j′ ≡ j mod h. Prolonging u if necessary,
we may freely assume that δ(s0, u) = s0. It follows from the minimality of Mi
and the fact that all states in S are reachable from s0 that there exists w ∈ Σ∗
k
such that δ(s0, wv) = s; indeed, otherwise δ(S, v) would be a proper subset of Mi.
By primitivity, we can assume that w ∈ Σ∗
K. Now, the deﬁnition of Cj implies
that [u]k + [w]k + [v]k ≡ j mod h. By Lemma 4.3, for each m ∈ Z we can ﬁnd
w′
m ∈ Σ∗
K of some length ℓ(m) divisible by logk K and such that δ(s0, w′
m) = s0,
[w′
m]k ≡ hm mod q and kℓ(m) ≡ 1 mod q. It remains to note that for all m we have
δ(s0, uw′
mwv) = s and there exists m such that [uw′
mwv]k ≡ j′ mod q. □

Proposition 4.6. Let a be a primitive automatic sequence. Then

p≤d
a (ℓ) ≤ rℓp≤d
(i,j)(ℓ) ≤ rℓ exp (o(ℓ)) .

Proof. We recall that from the construction of Si,j that for all n we have t(n) ∈
Si(n),j(n). In particular a(n) ∈ {τ (s) : s ∈ Si(n),j(n)}. This already shows the ﬁrst
inequality. For the second inequality we let h denote the height of a and have

p≤d
(i,j)(ℓ) ≤ p≤d
i (ℓ) · p≤d
j (ℓ) ≤ exp(o(ℓ)) · hd+1,

where the second inequality follows from Proposition 5.8 in [DDM
+24]. □

Remark 4.7. The upper bound in Proposition 5.8 in [DDM
+24] can be improved
by balancing the error terms more carefully. We switch for this remark to the
notation used in [DDM
+24] (i.e. ℓ is replaced by H). If we let λ grow with H and
ignore the estimates using ε, all the arguments can be kept essentially unchanged
and we ﬁnd the upper bound

p≤d
a (H) ≪ |Kerk(a)| · |A|kλ(d+1) · ( kλ

O(kλ(1−η))
) · |A|(H/kλ+1)kλ(1−η)

≪ |A|kλ(d+1) · (kλ)
O(kλ(1−η) ) · |A|(H/kλ+1)kλ(1−η)

12 J. KONIECZNY AND C. M ¨ULLNER

Choosing for example kλ = ⌊H 1/(d+2)⌋ leads to

p≤d
a (H) ≤ exp (
O (
H 1−η/(d+2))) .

4.2. General case. We now deal with sequences that are not necessarily primitive.
To begin with, we will need the following lemma.

Lemma 4.8. Let w ∈ Σ∗
k be a word, let P be a degree d polynomial such that
P (N0) ⊆ N0, and let ℓ ∈ N. Then there exists 0 < θ < 1, dependent only on |w|
and d, such that [0, ℓ) can be covered by ℓθ intervals, each of which either contains
exactly one integer point, or is contained in a set of the form P −1([mki, (m + 1)ki))
where m, i ∈ N0 and w is a subword of (m)k.

Proof. Let P (n) = α0 + α1n + . . . + αdnd and P1(n) = P (n) − α0. It follows from
Lemma 5.6 in [KM23] that

M := max
n∈[0,ℓ] |P1(n)| = Θ ( max
1≤j≤d ∣
∣ℓjαj∣
∣) .

Similarly we have

M ′ := max
n∈[0,ℓ] |P ′(n)| = Θ ( max
1≤j≤d
 ∣
∣jℓj−1αj∣
∣) = Θ(M/ℓ).

Moreover, for each δ > 0 we have

λ ({
x ∈ [0, ℓ] ∣
∣ |P ′(x)| < δd−1M ′}) ≪ δℓ.(13)

We note that (13) also holds for d = 1 as the left hand side equals 0.
Let ε > 0 be a small positive quantity, to be determined in the course of the
argument, and let
 I = {x ∈ [0, ℓ] ∣
∣ |P ′(x)| > εd−1M ′} .

We note that I is a union of at most d intervals and it follows from (13) that

λ([0, ℓ] \ I) ≪ εℓ.(14)

(In the case where d = 1 we have P ′(n) = M ′ = α1, whence (14) is trivially true
and I = [0, ℓ].)
Let R > 0 be a large real number, to be determined in the course of the argument,
and let K = ki be a power of K such that K ≤ M/R < kK. Recall that P ([0, ℓ])
is an interval of length at most 2M , and hence can be covered with O(R) intervals
of the form Jm := [mK, (m + 1)K). For each m, the set I ∩ P −1(Jm) is a union of
O(d) intervals. If the base-k expansion (m)k contains w as a subword then these
intervals satisfy the required conditions; we will call such intervals “good”.
We cover the remaining part of [0, ℓ) with singletons. Thus, it remains to estimate
the number of integers in [0, ℓ) not covered by “good” intervals. These integers fall
into two categories. Firstly, we have the elements of [0, ℓ) \ I, whose number can
be estimated by (13). Secondly, we have the “bad” intervals, corresponding to
the intervals Jm such that (m)k does not contain w. The number of such “bad”
values of m is O(R1−λ) for some λ > 0 (dependent only on k and |w|). Recall
that for each m the set I ∩ P −1(Jm) is a union of O(d) intervals, each of length
O(ℓ/ (
εd−1R) + 1). Thus, in total, the number of points and “bad” intervals we
obtain is, up to a constant, bounded by

εℓ + R1−λ · ℓ
εd−1R + R1−λ = ℓ · (
ε + 1/ (
εd−1Rλ)) + R1−λ.

ARITHMETICAL SUBWORD COMPLEXITY OF AUTOMATIC SEQUENCES 13

Optimising, we are lead to choose

R = ℓ d
d+λ , ε = R− λ
d = ℓ− λ
d+λ .

This ﬁnishes the argument, with θ = d
d+λ . □

We are now ready to prove Theorem A in full generality.

Proof of Theorem A, non-primitive case. Let A = (S, s0, Σk, δ, Ω, τ ) be an automa-
ton which computes a. Replacing k with a power, we may freely assume that
δ(s, 00) = δ(s, 0) for all s ∈ S. It follows directly from Deﬁnition 1.1 that

r = r(a) = max {r(a′) | a′ is computed by a ﬁnal component of A} .

Recall that we have already proved that for each sequence a′ computed by a ﬁnal
component of A, starting from a state s′
0 with δ(s′
0, 0) = s′
0, we have

pa′ (ℓ) ≤ r(a′)
ℓ exp(f (ℓ)) ≤ rℓ exp(f (ℓ)),

where f : N → R≥0 is some function with f (ℓ)/ℓ → 0 as ℓ → ∞. We may freely
assume that f is deﬁned on [0, ∞), f (0) = 0 and that f is concave.1 Let w be
a word such that δ(s, w) belongs to a ﬁnal component of A for each s ∈ S (cf.
[BKM23, Lem. 3.1]). Replacing w with w0 if necessary, we may further assume
that for each s ∈ S the state s′ := δ(s, w) belongs to a ﬁnal component and satisﬁes
δ(s′, 0) = s′.
Let ℓ be a large integer and let P be a degree d polynomial with P (N0) ⊆ N0. By
Lemma 4.8, we can partition [0, ℓ) into R ≪ ℓθ intervals I that either are singletons
or are contained in P −1([mki, (m + 1)ki)) for some m, i ∈ N0 such that w is a
subword of (m)k. In the latter case, for n ∈ I we have

a(P (n)) = a′(P ′(n))

for a sequence a′ computed by a strongly connected component of A, starting from
a state s′
0 with δ(s′
0, 0) = s′
0 and a polynomial P ′ with P ′(N0) ⊆ N0. (To be
more precise, we can ﬁnd integers m′, i′ ∈ N0 such that (m′)k ends with w and
[mki, (m + 1)ki) ⊆ [m′ki
′ , (m′ + 1)ki
′); thus replacing m, i with m′, i′ we may
freely assume that (m)k ends with w. Let s′
0 = δ(s0, (m)k), let a′ be the sequence
computed by A starting from the state s′
0, and let P ′(n) = P (n) − mki. Then
a(P (n)) = a′(P ′(n)) for n ∈ I. One remaining problem is that P ′ could take
negative values outside of I. To overcome it, we replace P ′(n) with P ′(n) + hkj,
where j is suﬃciently large that kj > (m + 1)ki and h > 0 is an integer such
that δ(s′
0, (h)k) = s′
0, which exists by strong connectivity.) Above, θ ∈ (0, 1) is a
constant which depends only on |w| and d. The number of partitions, as described
above, is ℓO(R). Fix one such partition. For each singleton {n} we have at most
#Ω possible values of a(P (n)). For each non-degenerate interval of length ℓi the
number of possible values taken by a(P (n)) is at most rℓi exp(f (ℓi)). Note that, by
concavity, we have ∑
i f (ℓi) ≤ Rf (ℓ/R), where the sum runs over all lengths ℓi of
non-degenerate intervals involved in the partition. In total, we obtain the estimate

pa(ℓ) ≤ ℓO(R) · #ΩR · rℓ · exp (Rf (ℓ/R))

= rℓ · exp (R(O(log(ℓ) + f (ℓ/R))) = rℓ · exp (o(ℓ)) .

1If f is not concave, consider the area A = {(x, y) | x ≥ 0, 0 ≤ y ≤ f (x)} below the graph of
f . The closure of the convex hull of A is the area below the graph of some concave g. Directly
from construction, g is concave and g ≥ f . It is routine to verify that g(ℓ)/ℓ → 0 as ℓ → ∞.

14 J. KONIECZNY AND C. M ¨ULLNER

(In the last transition, we used the fact that ℓ/R → ∞ and consequently also
Rf (ℓ/R)/ℓ → 0 as ℓ → ∞.) □

References

[ACF06] S. V. Avgustinovich, J. Cassaigne, and A. E. Frid. Sequences of low arithmetical
complexity. Theor. Inform. Appl., 40(4):569–582, 2006.
[AFDFF03] S. V. Avgustinovich, D. G. Fon-Der-Flaass, and A. E. Frid. Arithmetical complexity
of inﬁnite words. In Words, languages & combinatorics, III (Kyoto, 2000), pages
51–62. World Sci. Publ., River Edge, NJ, 2003.
[AS03] J.-P. Allouche and J. Shallit. Automatic sequences. Cambridge University Press, Cam-
bridge, 2003. Theory, applications, generalizations.
[BKM23] J. Byszewski, J. Konieczny, and C. M¨ullner. Gowers norms for automatic sequences.
Discrete Analysis, (4), 2023.
[CF07] J. Cassaigne and A. E. Frid. On the arithmetical complexity of Sturmian words.
Theoret. Comput. Sci., 380(3):304–316, 2007.
[DDM+24] J.-M. Deshouillers, M. Drmota, C. M¨ullner, A. Shubin, and L. Spiegelhofer. Syn-
chronizing automatic sequences along piatetski-shapiro sequences. Israel Journal of
Mathematics (to appear), 2024+. arXiv: 2211.01422.
[DMR19] M. Drmota, C. Mauduit, and J. Rivat. Normality along squares. J. Eur. Math. Soc.
(JEMS), 21(2):507–548, 2019.
[Fri03a] A. E. Frid. Arithmetical complexity of symmetric D0L words. Theoret. Comput. Sci.,
306(1-3):535–542, 2003.
[Fri03b] A. E. Frid. Sequences of linear arithmetical complexity. In Proceedings of WORDS’03,
volume 27 of TUCS Gen. Publ., pages 53–64. Turku Cent. Comput. Sci., Turku, 2003.
[Fri06] A. E. Frid. On possible growths of arithmetical complexity. Theor. Inform. Appl.,
40(3):443–458, 2006.
[Iv´a87] A. Iv´anyi. On the d-complexity of words. Ann. Univ. Sci. Budapest. Sect. Comput.,
8:69–90 (1988), 1987.
[KM23] J. Konieczny and C. M¨ullner. Bracket words along hardy ﬁeld sequences. February
2023.
[Kon19] J. Konieczny. Gowers norms for the Thue-Morse and Rudin-Shapiro sequences. Ann.
Inst. Fourier (Grenoble), 69(4):1897–1913, 2019.
[KZ02] T. Kamae and L. Zamboni. Sequence entropy and the maximal pattern complexity
of inﬁnite words. Ergodic Theory Dynam. Systems, 22(4):1191–1199, 2002.
[MS17] C. M¨ullner and L. Spiegelhofer. Normality of the Thue-Morse sequence along
Piatetski-Shapiro sequences, II. Israel J. Math., 220(2):691–738, 2017.
[M¨ul17] C. M¨ullner. Automatic sequences fulﬁll the Sarnak conjecture. Duke Math. J.,
166(17):3219–3290, 2017.
[M¨ul18] C. M¨ullner. The Rudin-Shapiro sequence and similar sequences are normal along
squares. Canadian Journal of Mathematics, 70(5):1096–1129, 2018.
[OEI23] OEIS Foundation Inc. The On-Line Encyclopedia of Integer Sequences, 2023. Pub-
lished electronically at http://oeis.org.
[Que10] M. Queﬀ´elec. Substitution dynamical systems. Spectral analysis, volume 1294 of Lect.
Notes Math. Dordrecht: Springer, 2nd ed. edition, 2010.
[RS02] A. Restivo and S. Salemi. Binary patterns in inﬁnite binary words. In Formal and
natural computing, volume 2300 of Lecture Notes in Comput. Sci., pages 107–116.
Springer, Berlin, 2002.
[Tao12] T. Tao. Higher order Fourier analysis, volume 142 of Graduate Studies in Mathe-
matics. American Mathematical Society, Providence, RI, 2012.

Universit´e Claude Bernard Lyon 1, CNRS UMR 5208, Institut Camille Jordan, F-
69622 Villeurbanne Cedex, France
Email address: jakub.konieczny@gmail.com

Institut f¨ur Diskrete Mathematik und Geometrie TU Wien, Wiedner Hauptstr. 8-10,
1040 Wien, Austria
Email address: clemens.muellner@tuwien.ac.at
