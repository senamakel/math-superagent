<!-- source: https://arxiv.org/pdf/2301.06095 | converted from PDF -->

arXiv:2301.06095v1  [math.NT]  15 Jan 2023
SUMS OF SINGULAR SERIES ALONG ARITHMETIC PROGRESSIONS
AND WITH SMOOTH WEIGHTS

VIVIAN KUPERBERG

Abstract. Sums of the singular series constants that appear in the Hardy–Littlewood k-
tuples conjectures have long been studied in connection to the distribution of primes. We
study constrained sums of singular series, where the sum is taken over sets whose elements
are speciﬁed modulo r or weighted by smooth functions. We show that the value of the
sum is governed by incidences modulo r of elements of the set in the case of arithmetic
progressions and by pairings of the smooth functions in the case of weights. These sums
shed light on sums of singular series in other formats.

1. Introduction

The Hardy–Littlewood k-tuples conjectures, and the constants known as singular series
that appear within them, have long been studied in connection to the distribution of primes.
These conjectures state that for any k-tuple H = {h1, . . . , hk} of distinct integers, the number
of k-tuples of primes of the form (n + h1, . . . , n + hk), with n ≤ x, is given by

(1) ∑

n≤x
 k∏

i=1 Λ(n + hi) = S(H)x + o(1)x,

where S(H) is the singular series

(2) S(H) = ∏

p prime
 1 − νH(p)/p
(1 − 1/p)k ,

and νH(p) denotes the number of distinct residue classes modulo p occupied by the elements
of H.
In [1], Gallagher showed that the Hardy–Littlewood conjectures imply that the distribution
of primes in intervals of size h = λ log x is Poissonian for ﬁxed λ, by showing that the singular
series is 1 on average. In particular, he showed that for any ﬁxed k,
∑

H⊂[1,h]
|H|=k
 S(H) ∼ ∑

H⊂[1,h]
|H|=k
 1.

In 2004, Montgomery and Soundararajan [7] used a more reﬁned estimate of sums of sin-
gular series to show that when h is in a larger regime, with h/ log x → ∞ but h = o(x), the
Hardy–Littlewood conjectures imply that the distribution of primes, counted with von Man-
goldt weights, becomes Gaussian with mean ∼ h and variance ∼ h log x
h, matching numerical
data. Instead of the singular series itself, they considered alternating sums of singular se-
ries, deﬁning S0(H) := ∑

J⊂H(−1)|H\J|S(J). These sums have the eﬀect of subtracting the

The author is supported by NSF GRFP grant DGE-1656518 as well as the NSF Mathematical Sciences
Research Program through the grant DMS-2202128, and would like to thank Kannan Soundararajan for
many helpful comments and discussions. 1

2 VIVIAN KUPERBERG

main term from the outset, making it easier to understand lower-order contributions. The
analogous Hardy–Littlewood conjecture says that

∑

n≤x
 k∏

i=1 (Λ(n + hi) − 1) = S0(H)x + o(x),

so that each term on the left-hand side has expectation 0.
Montgomery and Soundararajan [7] showed that for ﬁxed k,

(3) ∑

H⊂[1,h]
|H|=k
 S0(H) = µk(−h log h + A)k/2 + Ok(h
k/2−1/(7k)+ε),

where µk = 1 · 3 · · · (k − 1) if k is even, and 0 if k is odd, and A = 2 − γ0 − log 2π, with γ0
the Euler–Mascheroni constant. Their results depend crucially on work of Montgomery and
Vaughan [8] on the distribution of reduced residues mod q in short intervals.
Here we develop analogs of the work of Montgomery and Vaughan as well as that of Mont-
gomery and Soundararajan by studying sums of singular series with added conditions on the
set H. First, instead of summing over all subsets of [1, h], we restrict to sets whose elements
lie in arithmetic progressions. For a ﬁxed modulus r and congruence classes c1, . . . , ck mod
r, we study the sum

(4) Rk(h; r, c1, . . . , ck) := ∑

H={h1,...,hk}⊂[1,h]
|H|=k
hi≡ci mod r
 S0,r(H),

where S0,r(H) = ∑

J⊂H Sr(J)(−1)|H\J| and Sr(H) is the singular series of H away from r,
given by

(5) Sr(H) := ∏

p prime
p∤r
 1 − νH(p)/p
(1 − 1/p)k .

The study of these sums is of interest for two reasons. First, they appear in the work
of Lemke Oliver and Soundararajan in [5] on bias in the distribution of consecutive primes
in arithmetic progressions. Speciﬁcally, Lemke Oliver and Soundararajan conjecture that if
π(x; q, (a, b)) is deﬁned as the number of primes p ≤ x with p ≡ a mod q and pnext ≡ b mod q,
then
 π(x; q, (a, b)) ∼ 1
q
 ∫ x

2 α(y)ǫq(a,b) ( q
φ(q) log y
 )2 D(a, b; y)dy,

where α(y) : −1 − q
φ(q) log y , ǫq(a, b) is a constant deﬁned only in terms of q, a, and b, and

D(a, b; y) := ∑

h>0
h≡b−a mod q
 ∑

A⊂{0,h}
 ∑

T⊂[1,h−1]
(t+a,q)=1∀t∈T
(−1)|T|S0,q(A ∪ T) ( q
φ(q)α(y) log y
 )|T| α(y)hφ(q)/q.

They proceed to heuristically estimate D(a, b; y), and thus π(x; q, (a, b)), by estimating a
weighted version of R2(h; r, c1, c2). Our results generalize these arguments by estimating
Rk(h; r, c1, c2) for all k, which is necessary for understanding some of the error terms appear-
ing in Lemke Oliver and Soundararajan’s heuristic. Secondly, restricting sums of singular
series in this manner may shed light on other questions about sums of singular series. We

RESTRICTED SUMS OF SINGULAR SERIES 3

show in Theorem 1.2 that the asymptotics for (4) are governed by incidences among the
ci’s mod r. As discussed in [4], we do not yet know the asymptotic average size of sums of
S0(H) when |H| is odd. The results of these more reﬁned averages of singular series may
clarify where the main term should be coming from for sums of singular series with an odd
number of terms.
The sums over S0,r admit the expansion

∑

1≤h1,...,hk≤h
hi≡ci mod r ∀i
distinct
 S0,r({h1, . . . , hk}) = ∑

q1,...,qk
qi>1
(qi,r)=1
 µ(qi)
φ(qi)
 ∑

a1,...,ak
1≤ai≤qi
(ai,qi)=1∑i ai/qi∈Z
 ∑

1≤h1,...,hk≤h
hi≡ci mod rdistinct
 k∏

i=1 e (aihi
qi
 ) .

Following [7] and [8], we ﬁrst consider a related quantity, where the summands qi are re-
stricted to divide a secondary modulus q > 1 and the hi’s are not necessarily distinct, to
get

(6) Vk(q, h; r, c1, . . . , ck) := ∑

q1,...,qk
1<qi|q
(qi,r)=1
 µ(qi)
φ(qi)
 ∑

a1,...,ak
1≤ai≤qi
(ai,qi)=1∑i ai/qi∈Z
 k∏

i=1 Er,ci
 (aihi
qi
 ) ,

where for α ∈ R,

(7) Er,ci(α) := ∑

m≤h
m≡ci mod r
 e(mα).

In order to state our result, we will need to ﬁx some notation concerning perfect matchings
of [1, k]. For k ≥ 1, a perfect matching σ of [1, k] is a set σ = {(i, j)} of unordered pairs in
[1, k] so that each element is paired with exactly one other element, i.e. each i appears in
exactly one pair (i, j), and i ̸= j. Since each pair (i, j) ∈ σ is unordered, we will generally
choose to write the representative with i < j, so that σ{(i, j)} with i < j. Let Bk denote
the set of perfect matchings of [1, k], so that

(8) Bk := {
σ = {(i, j)} : ∀(i, j) ∈ σ, 1 ≤ i < j ≤ k
∀i ∈ [1, k], ∃!j ∈ [1, k] with (i, j) ∈ σ or (j, i) ∈ σ
 } .

Note that when k is odd, Bk = ∅. Moreover, for a set of integers {a1, . . . , ak}, we will denote
by B(a1, . . . , ak) the set of matchings of {a1, . . . , ak} into pairs, so that Bk = B([1, k]).
In Section 2, we prove the following result, which mirrors Theorem 1 of [7].

Theorem 1.1. Fix a modulus r ≥ 1, an integer k ≥ 1, and k congruence classes c1, . . . , ck
modulo r. Deﬁne Bk as in (8). Let q ≥ 1 be a squarefree integer with (r, q) = 1, and deﬁne
Vk(q, h; r, c1, . . . , ck) as in (6). For h ≥ 3,

Vk(q, h; r, c1, . . . , ck) = ∑

σ∈Bk
 ∏

(i,j)∈σ V2(q, h; r, ci, cj) + Or,k
 (
h
k/2−1/(7k) ( q
φ(q)
 )2k+k/2)
 .

In order to state our main result on the asymptotics of Rk(h; r, c1, . . . , ck), we deﬁne some
further notation. For 1 ≤ ℓ ≤ r, deﬁne

Cℓ := {i : ci ≡ ℓ mod r} .

4 VIVIAN KUPERBERG

Note that some of the sets Cℓ may be empty, and that ⋃r
ℓ=1 Cℓ = [1, k]. We will say that a
partition P = {S1, . . . , SM } of [1, k] reﬁnes {Cℓ}ℓ∈[1,k] if for each Sm ∈ P, there exists some
ℓ with Sm ⊂ Cℓ; note that ℓ is then unique. For such a partition, write P ≼ {Cℓ}ℓ∈[1,k] and
deﬁne c(Sm) to be the value ℓ with Sm ⊂ Cℓ.

Theorem 1.2. Fix a modulus r ≥ 1 and an integer k ≥ 1, as well as k congruence classes
c1, . . . , ck modulo r. Deﬁne Rk(h; r, c1, . . . , ck) by (4). Then for h ≥ 3,

Rk(h; r, c1, . . . , ck) = ∑

0≤j≤k/2
(−1)j ∑

P≼{Cℓ}ℓ∈[1,k]
P={S1,...,Sk−j}
|Sm|=2 ∀1≤m≤j
|Sm|=1 ∀j<m≤k−j
 



h
r
 ∑

d|Q
d>1
 µ(d)2

φ(d)
 





j

∑

σ∈B(j+1,...,k−j)
 ∏

(i1,i2)∈σ V2(Q, h; r, c(Si1), c(Si2)), +Or,k(h
k/2−1/(7k)+ε).(9)

In particular, if #̃B(c1, . . . , ck) is the number of ways to pair the ci’s such that every pair
has equal values, then

Rk(h; r, c1, . . . , ck) = #̃B(c1, . . . , ck) (
−hφ(r)
r log h + C0(r)h
)k/2 + Or,k(h
k/2(log h)k/2−1).

Remark. When all the ci’s are congruent mod r, then #̃B(c1, . . . , ck) = µk and this theorem
implies Theorem 2 of [7]. When the ci’s are not all congruent, the estimate depends crucially
on the precise arrangement of the ci’s. Nevertheless, while the value of the main term is
dependent on the ci’s, we always have the upper bound Rk(h; r, c1, . . . , ck) ≪r,k h
k/2(log h)k/2.

The framework of Theorems 1.1 and 1.2 also applies to sums of singular series weighted by
smooth functions. Let f1, . . . , fk : R)≥ 0 → C be functions with compact supports contained
in (0, ∞) and such that | ˆfi(ξ)| ≪ ξ−2, where the Fourier transform ˆf is deﬁned as

ˆf (ξ) := − ∫ ∞

∞ f (x)e
−2πixξdx.

For h ∈ N, we are interested in the quantity

(10) Rk(h; f1, . . . , fk) := ∑

h1,...,hk∈Z
distinct
 k∏

i=1 fi
 (hi
h
 ) S0({h1, . . . , hk}).

The size of Rk(h; f1, . . . , fk) as h → ∞ is similar in structure to the analogous result for
sums of singular series along arithmetic progressions: the main term is a sum over perfect
matchings of [1, k], and for each matching σ the contribution is determined by interactions
of fi and fj for each pair (i, j) ∈ σ.
We set some notation before stating our results. Deﬁne

(11) V (q, h; f1, . . . , fk) := ∑

1<q1,...,qk|q
 k∏

i=1
 µ(qi)
φ(qi)
 ∑

a1,...,ak
1≤ai≤qi
(ai,qi)=1∑i ai/qi∈Z
 Ef1,h
 ( a1
q1
 ) · · · Efk,h
 ( ak
qk
 ) ,

RESTRICTED SUMS OF SINGULAR SERIES 5

where for α ∈ R and f smooth, with compact support, and such that | ˆf (ξ)| = O(|ξ|−2),

(12) Ef,h(α) :=
 ∞∑

m=−∞ f ( m
h
 ) e(mα).

Since f is smooth, Ef,h(α) is a smoother indicator function of values of α that are close
to 0. In particular, by Poisson summation,

Ef,h(α) = h
 ∞∑

n=−∞ ˆf (h(n − α)).

By assumption, ˆf (ξ) = O(|ξ|−2). For any real number α, only one value of α − n will be in
the interval [−1/2, 1/2); let α denote this value, so that α is the representative of α mod 1
satisfying −1/2 ≤ α < 1/2. Then

(13) Ef,h(α) = h ˆf (−hα) + h
 ∞∑

n=1 O((hn)−2) = h ˆf (−hα) + O(h
−1).

The following results about Vk(q, h; f1, . . . , fk) hold, analogous to Theorem 1.1 and Lemma
3.2.

Theorem 1.3. Fix k ≥ 1 and k smooth functions f1, . . . , fk : R≥0 → C with compact
supports supp(fi) ⊂ (0, ∞) and such that | ˆfi(ξ)| = O(|ξ|−2) for all 1 ≤ i ≤ k. Deﬁne Bk
as in (8). Let q ≥ 1 be a squarefree integer, and deﬁne Vk(q, h; f1, . . . , fk) as in (11). For
h ≥ 3,

Vk(q, h; f1, . . . , fk) = ∑

σ∈Bk
 ∏

(i,j)∈σ V2(q, h; fi, fj) + Of1,...,fk
 (

h
k/2−1/(7k) ( q
φ(q)
)2k+k/2)
 .

Lemma 1.4. Fix h ≥ 1 and let f1, f2 : R≥0 → C be smooth functions with compact sup-
ports supp(fi) ⊂ (0, ∞) such that | ˆfi(ξ)| ≪ O(|ξ|−2). Deﬁne Q := ∏
p≤h2 p, and deﬁne
V2(q, h; f1, f2) via (11). Then

(14) V2(Q, h; f1, f2) = (− ˆf1(0) ˆf2(0) + {Mf }(2))h
2 − {Mf ′}(1)
2 h log h + Of1,f2(h),

where {Mf }(s) is the Mellin transform of f , deﬁned by

(15) {Mf }(s) := ∫ ∞

0 x
s−1f (x)dx.

Using precisely the same techniques as in the case of arithmetic progressions, an analog to
Theorem 1.2 also holds for the smooth functions setting, where the input to each summand
is clariﬁed by Lemma 1.4.

Theorem 1.5. Fix an integer k and smooth functions f1, . . . , fk : R≥0 → C with compact
support such that supp(fi) ⊂ (0, ∞) and such that | ˆfi(ξ)| = O(|ξ|−2) for each 1 ≤ i ≤ k.

6 VIVIAN KUPERBERG

Deﬁne Rk(h; f1, . . . , fk) via (10). Then for h ≥ 3,

Rk(h; f1, . . . , fk) = ∑

0≤j≤k/2
(−1)j ∑

P={S1,...,Sk−j}
|Sm|=2 ∀1≤m≤j
|Sm|=1 ∀j<m≤k−j
 



h ∑

d|Q
d>1
 µ(d)2

φ(d)
 





j

∑

σ∈B(j+1,...,k−j)
 ∏

(i1,i2)∈σ V2(Q, h; fSi1 , fSi2 ), +Or,k(h
k/2−1/(7k)+ε),(16)

where the sum is taken over partitions of [1, k] where each part has either 1 or 2 elements,
and for |Sm| = 1, fSm denotes fj where j ∈ Sm.

The proofs of Theorems 1.3 and 1.5 are identical to the proofs of Theorems 1.1 and 1.2,
so we omit them. However, Theorems 1.3 and 1.1, which provide asymptotics for Vk in
the cases of smooth weighting and arithmetic progressions, rely on lemmas about sums of
Ef,h(α). The results are fundamentally the same, but the ﬂavor of several of these lemmas
is somewhat diﬀerent in the smooth case, so we record them in Section 5. We also provide
the proof of Lemma 1.4, which is similar to the proof of Lemma 3.2.
The organization of this paper is as follows. In Section 2, we prove Theorem 1.1. In
Section 3, we compute certain sums of 2-term singular series which will then be used in the
proof of Theorem 1.2. In Section 4, we prove Theorem 1.2. Finally, in Section 5 we discuss
the smooth case.
 2. Proof of Theorem 1.1

The arguments in this section closely follow the arguments in the proof of Lemma 8 in [8]
and Theorem 1 in [7]. Here we outline the argument; where it diﬀers, we present detailed
explanations, but many steps are cited to [8] and [7].
The functions Er,ci(α), deﬁned in (7), are modular versions of sums E(α) := ∑

m≤h e(mα).
The sums E(α) are large if α is close to an integer and otherwise exhibit large amounts of
cancellation. Since Er,ci(α) is summed only over m in a set congruence class modulo r, it
will also take large values when α is close to a multiple of r. For any c, r, write

Er,c(α) = ∑

m≤h
 1
r
 r∑

n=1 e ((m − c)n
r
 ) e(mα)

= 1
r
 r∑

n=1 e(−cn/r) ∑

m≤h e(mα + mn/r),

so that
 |Er,c(α)| ≤ 1
r
 r∑

n=1 min {
h, 1
∥α + n/r∥
} .

Deﬁne

(17) Fr(α) := 1
r
 r∑

n=1 min {h, 1
∥α + n/r∥
 } ,

so that |Er,c(α)| ≤ Fr(α). We can then closely follow the analysis of Montgomery and
Vaughan in [8] and Montgomery and Soundararajan in [7]. In particular, Fr(α) can be

RESTRICTED SUMS OF SINGULAR SERIES 7

bounded, up to some dependence on r, by the same bounds as appear in Lemmas 4,5,6, and
7 of [8] and using the same arguments. We arrive at the following result.

Theorem 2.1. Fix r, k, q ≥ 1. Let S(q) denote the set of k-tuples (q1, . . . , qk) such that for
all i, qi|q, qi > 1, and the qi’s are not equal in pairs and otherwise distinct; that is to say,
there is no reordering permutation σ of the k indices with qσ(i) = qσ(i+k/2) for all 1 ≤ i ≤ k/2,
and no other equalities. Then

∑

(q1,...,qk)∈S(q)
 k∏

i=1
 µ(qi)2

φ(qi)
 ∑

a1,...,ak
1≤ai≤qi
(ai,qi)=1∑i ai/qi∈Z
 k∏

i=1 Fr
 ( ai
qi
 ) ≪r qh
k/2−1/7k ( φ(q)
q
 )k/2−2k .

Theorem 2.1 accounts for all terms in Vk(q, h; r, c1, . . . , ck) except for those terms where
the qi’s are equal in pairs and otherwise distinct. When k is odd, there are no such terms,
so assume that k is even. By the same argument as in [7], we can drop the assumption that
the pairs are distinct, so that the terms left to be estimated are given by

∑

σ∈Bk
 ∑

(qi)(i,j)∈Bk
1<qi|q
 ∏

(i,j)∈Bk
 µ(qi)2

φ(qi)2 ∑

(bi)(i,j)∈Bk
1≤bi≤qi∑i bi/qi∈Z
 ∏

(i,j)∈Bk Jr,ci,cj (bi, qi),

where for each i,
 Jr,ci,cj (bi, qi) := ∑

1≤ai≤qi
(ai,qi)=1
(bi−ai,qi)=1
 Er,ci
 ( ai
qi
 ) Er,cj
 ( bi − ai
qi
 ) .

Each term σ in our sum is identical up to changing labels, so without loss of generality
we will work with the term σ = {(i, k/2 + i) : 1 ≤ i ≤ k/2}, so that qi = qi+k/2 for all
1 ≤ i ≤ k/2. This term is given by

(18) ∑

q1,...,qk/2
1<qi|q
 k/2∏

i=1
 µ(qi)2

φ(qi)2 ∑

b1,...,bk/2
1≤bi≤qi∑
i bi/qi∈Z
 k/2∏

i=1 Jr,ci,ck/2+i(bi, qi).

Let J ⊂ [1, k/2] be the subset of i’s with 0 < bi < qi instead of bi = qi. For i ̸∈ J, we have

Ji,k/2+i(qi, qi) = ∑

1≤ai≤qi
(ai,qi)=1
 Er,ci
 (ai
qi
 ) Er,ck/2+i
 (
−ai
qi
 ) ,

which, when summed over 1 < qi|q with the weight µ(qi)2

φ(qi)2 , is equal to V2(q, h; r, ci, ck/2+i).
Thus, (18) is equal to

(19) ∑

J⊂[1,k/2]
 ∏

i̸∈J V2(q, h; r, ci, ck/2+i)WJ(q, h; r, (bi)i∈J),

8 VIVIAN KUPERBERG

where
 WJ(q, h; r, (bi)i∈J) := ∑

(qi)i∈J
1<qi|q
 ∏

i∈J
 µ(qi)2

φ(qi)2 ∑

(bi)i∈J
0<bi<qi∑
i∈J bi/qi∈Z
 ∏

i∈J Jci,ck/2+i(bi, qi).

The term J = ∅ gives the desired main term, so it remains to show that the terms with
J ̸= ∅ are smaller. By following the reasoning on page 11 of [7], we get that

WJ(q, h; r, (bi)i∈J) ≪r h
|J|/2 ( q
φ(q)
)2|J| ,

and that for any c1, c2 mod r,
 V2(q, h; r, c1, c2) ≪r h q
φ(q).

Applying these estimates to (19) completes the proof of Theorem 1.1.

3. Auxiliary lemmas: two-term computations

In order to prove Theorem 1.2, we will ultimately invoke Theorem 1.1, which will then
relate quantities involving k-term singular series to quantities involving 2-term singular series.
In this section, we state two lemmas which compute, respectively, sums of two-term singular
series in arithmetic progressions, and the quantity V2(Q, h; r, c1, c2) when Q is the product
of all primes below h
2, which will be applied in Section 4.
The following lemma is a computation of sums of two-term singular series to the modulus
q. Its proof is nearly identical to the proof of Proposition 2.1 in [5], so we omit it. Similar
quantities were previously studied in [2] and [6].

Lemma 3.1. Fix r, h ≥ 1, and let v mod r be any residue class. Deﬁne

S(r, v, h) := ∑

1≤m≤h
m≡v mod r
(h − m)Sr({0, m}).

Then when v = 0,

S(r, v, h) = h
2

2r − h
2 φ(r)
 

log h
r + log 2π + γ0 + ∑

p|r
 log p
p − 1


 + Or(h
1/2+ε),

where γ0 denotes the Euler–Mascheroni constant. Meanwhile, if v ̸= 0, then if d = (v, r),

S(r, v, h) = h
2

2r − h
2 φ(r)
r 1
φ(r/d)Λ(r/d)

+ h
φ(r/d)
 ∑

χ̸=χ0 mod r/d χ(v/d)L(0, χ)L(1, χ)Ar,χ + Or(h
1/2+ε),

with

(20) Ar,χ = ∏

p|r
 (
1 − χ(p)
p
 ) ∏

p∤r
 (1 − (1 − χ(p))2

(p − 1)2
 ) .

RESTRICTED SUMS OF SINGULAR SERIES 9

Lemma 3.2. Fix integers r, h ≥ 1 and two congruence classes c1, c2 mod r. Deﬁne

Q = ∏

p≤h2
p∤r
 p,

so that Q is the product of all primes below h
2 that do not divide r. Let V2(Q, h; r, c1, c2) be
deﬁned as in (6). Then if c1 ≡ c2 mod r,

V2(Q, h; r, c1, c1) = h
r
 ∑

d|Q
d>1
 µ(d)2

φ(d) − hφ(r)
r log h + C0(r)h + Or(h
1/2+ε),

where

(21) C0(r) = φ(r)
r
 

log r
2π − γ0 − ∑

p|r
 log p
p − 1
 

 ,

and γ0 is the Euler–Mascheroni constant. If c1 ̸≡ c2 mod r, deﬁne d = (c1 − c2, r), with
d < r. Then

V2(Q, h; r, c1, c2) = −h φ(r)
r2φ(r/d)Λ(r/d)

+ 2h
rφ(r/d)
 ∑

χ̸=χ0 mod r/d χ (c1 − c2
d
 ) L(0, χ)L(1, χ)Ar,χ + Or(h
1/2+ε),(22)

where Ar,χ is deﬁned in (20).

Proof. Begin by expanding

V2(Q, h; r, c1, c2) = −Er,c1(1)Er,c2(1) + ∑

q|Q
 µ(q)2

φ(q)2 ∑

1≤a≤q
(a,q)=1
 Er,c1
 (a
q
 ) Er,c2
 (
−a
q
 )

= −h
2

r2 + ∑

q|Q
 µ(q)2

φ(q)2 ∑

1≤a≤q
(a,q)=1
 ∑

m1,m2≤h
mi≡ci mod r
 e (
(m1 − m2) a
q
 ) .

Assume ﬁrst that c1 ≡ c2 mod r. Then

(23) V2(Q, h; r, c1, c1) = −h
2

r2 + ∑

q|Q
 µ(q)2

φ(q)2 ∑

1≤a≤q
(a,q)=1
 ∑

|m|≤h
r|m
 1
r (h − |m|)e (
ma
q
 ) .

Let cq(m) denote the Ramanujan sum ∑ 1≤a≤q
(a,q)=1 e (
m a
q )
. The expression (23) is then

V2(Q, h; r, c1, c1) = −h
2

r2 + 1
r
 ∑

q|Q
 µ(q)2

φ(q)2
 

hcq(0) + 2 ∑

1≤m≤h/r(h − rm)cq(rm)




= −h
2

r2 + h
r
 ∑

q|Q
 µ(q)2

φ(q)2 + 2
r
 ∑

1≤m≤h/r(h − rm) ∑

q|Q
 µ(q)2

φ(q)2 cq(rm).

10 VIVIAN KUPERBERG

The inside sum over q|Q is multiplicative and, since Q is the product of primes p ≤ h
2 not
dividing r, it is given by
∑

q|Q
 µ(q)2

φ(q)2 cq(rm) = ∏

p|m
p∤r
 (
1 + 1
p − 1
 ) ∏

p∤m
p∤r
 (
1 − 1
(p − 1)2
 ) + Or(h
−2) = Sr({0, m}) + Or(h
−2),

by the deﬁnition of Sr in (5).
Then

V2(Q, h; r, c1, c1) = −h
2

r2 + h
r
 ∑

q|Q
 µ(q)2

φ(q)2 + 2
r
 ∑

1≤m≤h/r(h − rm)Sr({0, m}) + Or(1),

which by Lemma 3.1 is equal to

−h
2

r2 + h
r
 ∑

q|Q
 µ(q)2

φ(q)2 + h
2

r2 − hφ(r)
r
 

log h
r + log 2π + γ0 + ∑

p|r
 log p
p − 1
 

 + Or(h
1/2+ε).

After a little rearranging this gives the desired result.
Now assume c1 ̸≡ c2 mod r. In this case,

V2(Q, h; r, c1, c2) = −h
2

r2 + ∑

q|Q
 µ(q)2

φ(q)2 ∑

1≤a≤q
(a,q)=1
 ∑

|m|≤h
m≡c1−c2 mod r
 1
r (h − |m|)e (
ma
q
 )

= −h
2

r2 + ∑

|m|≤h
m≡c1−c2 mod r
 1
r (h − |m|) ∑

q|Q
 µ(q)2

φ(q)2 cq(m)

= −h
2

r2 + ∑

|m|≤h
m≡c1−c2 mod r
 1
r (h − |m|)Sr({0, m}) + Or(1),

where if m ≡ c1 − c2 mod r, then m ̸= 0.
Applying Lemma 3.1 completes the proof. □

4. Proof of Theorem 1.2

Throughout this section, ﬁx r, k, h ≥ 1 and set Q = ∏
p≤y
p∤r p, where y = h
k+1.

Begin with the expansion

(24) Rk(h; r, c1, . . . , ck) = ∑

q1,...,qk
1<qi|Q
 k∏

i=1
 µ(qi)
φ(qi)
 ∑

a1,...,ak
1≤ai≤qi
(ai,qi)=1∑i ai/qi∈Z
 ∑

d1,...,dk
1≤di≤h
distinct
di≡ci mod r
 e
 ( k∑

i=1
 aidi
qi
 )
 + Or(1),

where the error term is due to our choice of Q. The expression on the right-hand side of
(24) is very close to Vk(Q, h; r, c1, . . . , ck), but in order to apply Theorem 1.1, we will need
to remove the distinctness condition on the di’s. As in the proof of Theorem 2 from [7],
removing this condition will be the bulk of our work.
This distinctness condition is heavily dependent on the congruence classes c1, . . . , ck; in
particular, if ci ̸≡ cj mod r, then di and dj never coincide and the distinctness condition is

RESTRICTED SUMS OF SINGULAR SERIES 11

immaterial. Our arguments follow those of [7] closely, but with additional bookkeeping in
order to account for the congruence classes c1, . . . , ck mod r.
For a given tuple (d1, . . . , dk) with 1 ≤ di ≤ h and di ≡ ci mod r for all i, put δij = 1 if
di = dj and δij = 0 otherwise. Then

r∏

ℓ=1
 ∏

i,j∈Cℓ
i<j
 (1 − δij) =
 {
1 if the di are distinct
0 otherwise.

When the left-hand side above is expanded, it is a linear combination of products of the
δ symbols. Let ∆ denote one such product, and let |∆| denote the number of δij in the
product. As in [7], deﬁne an equivalence relation on these δ-products by setting ∆1 ∼ ∆2 if
∆1 and ∆2 have the same value for all choices of di’s; for example, δ12δ23 ∼ δ12δ13 ∼ δ12δ23δ13.
Recall that a partition P = {S1, . . . , SM } of [1, k] reﬁnes {Cℓ}ℓ∈[1,k] if for each Sm ∈ P,
there exists some ℓ with Sm ⊂ Cℓ; note that ℓ is then unique. For such a partition, write
P ≼ {Cℓ}ℓ∈[1,k] and deﬁne c(Sm) to be the value ℓ with Sm ⊂ Cℓ. Given a partition P reﬁning
{Cℓ}ℓ∈[1,k], let
 ∆P =
 M∏

m=1
 ∏

i<j
i,j∈Sm
 δij.

Every equivalence class of δ-products contains a unique ∆P, where the condition that P
reﬁnes {Cℓ}ℓ∈[1,k] corresponds precisely to the fact that we are only considering δij when
ci ≡ cj mod r. Equivalence classes of δ-products are thus in bijection with partitions of [1, k]
that reﬁne {Cℓ}ℓ∈[1,k]. For a partition P, put

w(P) = ∑

∆∼∆P(−1)|∆|,

so that
 r∏

ℓ=1
 ∏

i,j∈Cℓ
i<j
 (1 − δij) = ∏

P≼{Cℓ}ℓ∈[1,k] w(P)∆P,

and the sum over ai’s in (24) is equal to

∑

P≼{Cℓ}ℓ∈[1,k]
P={S1,...,SM }
 w(P) ∑

a1,...,ak
1≤ai≤qi
(ai,qi)=1∑i ai/qi∈Z
 M∏

m=1 Er,c(Sm)
 ( ∑

i∈Sm
 ai
qi
 )
 .

12 VIVIAN KUPERBERG

By the same reasoning as in [7], the contribution to Rk(h; r, c1, . . . , ck) from terms where
|Sm| ≥ 3 for some m is Or(h
(k−1)/2+ε), so that

Rk(h; r, c1, . . . , ck) = ∑

P≼{Cℓ}ℓ∈[1,k]
P={S1,...,SM }
|Sm|≤2 ∀m
 w(P) ∑

q1,...,qk
1<qi|Q
 k∏

i=1
 µ(qi)
φ(qi)

· ∑

a1,...,ak
1≤ai≤qi
(ai,qi)=1∑i ai/qi∈Z
 M∏

m=1 Er,c(Sm)
 ( ∑

i∈Sm
 ai
qi
 )
 + Or,k(h
(k−1)/2+ε).(25)

Suppose that P consists of j doubleton sets S1, . . . , Sj and k −2j singleton sets Sj+1, . . . , Sk−j.
Note that the number of these partitions depends on the partition {Cℓ}, because of the
constraint that P ≼ {Cℓ}ℓ∈[1,k]. The term in Rk(h; r, c1, . . . , ck) corresponding to a ﬁxed such
partition P is

(26) (−1)j ∑

q1,...,qk
1<qi|Q
 k∏

i=1
 µ(qi)
φ(qi)
 ∑

a1,...,ak
1≤ai≤qi
(ai,qi)=1∑
i ai/qi∈Z
 j∏

m=1 Er,c(Sm)
 ( ∑

i∈Sm
 ai
qi
 ) k−j∏

m=j+1 Er,c(Sm)
 (aSm
qSm
 ) ,

where we are slightly abusing notation in the ﬁnal product by identifying the singletons Sm
with their unique element.
For 1 ≤ m ≤ j, deﬁne bm and sm by the relations

bm
sm = ∑

i∈Sm
 ai
qi mod 1, 1 ≤ bm ≤ sm, (bm, sm) = 1,

and deﬁne
 Hm
 ( b
s
 ) = Er,c(Sm)
 ( b
s
 ) ∑

d1,d2|Q
1<di
 µ(d1)µ(d2)
φ(d1)φ(d2)
 ∑

e1,e2
1≤ei≤di
(ei,di)=1
e1
d1 + e2
d2 = b
s mod 1
 1.

Then (26) is equal to

(27) ∑

s1,...,sj
si|Q
 ∑

b1,...,bj
1≤bi≤si
(bi,si)=1
 j∏

i=1 Hi
 ( bi
si
 ) ∑

qj+1,...,qk−j
1<qi|Q
 ∑

aj+1,...,ak−j
1≤ai≤qi
(ai,qi)=1∑i ai/qi+∑
i bi/si∈Z
 k−j∏

i=j+1
 µ(qi)
φ(qi) Er,c(Si)
 ( ai
qi
 ) .

Now separate the indices i with si = 1. To do so, let L = {i : si > 1}. We can again rewrite
(27) as

(28) ∑

L⊂[1,j] M(L) ∏

i̸∈L Hi(1),

RESTRICTED SUMS OF SINGULAR SERIES 13

where

M(L) = ∑

(si)i∈L
1<si|Q
 ∑

(bi)i∈L
1≤bi≤si
(bi,si)=1
 ∏

i∈L Hi
 ( bi
si
 ) ∑

qj+1,...,qk−j
1<qi|Q
 ∑

aj+1,...,ak−j
1≤ai≤qi
(ai,qi)=1∑i ai/qi+∑
i bi/si∈Z
 k−j∏

i=j+1
 µ(qi)
φ(qi) Er,c(Si)
 (ai
qi
 ) .

Note that M(∅) = V2k−j(Q, h; r, c(Sj+1), . . . , c(Sk−j)).
By precisely the same arguments as in [7], the contributions when |L| ≥ 1 can be absorbed
into the error term. Moreover,

Hi(1) = Er,c(Si)(1) ∑

d|Q
d>1
 µ(d)2

φ(d)

= (h
r + O(1)) ∑

d|Q
d>1
 µ(d)2

φ(d) .

Thus the expression (28) is equal to




h
r
 ∑

d|Q
d>1
 µ(d)2

φ(d)
 





j
 Vk−2j(Q, h; r, c(Sj+1), . . . , c(Sk−j)) + Or,k(h
(k−1)/2+ε).

Inserting this back into (25) yields

Rk(Q, h; r, c1, . . . , ck) = ∑

0≤j≤k/2
(−1)j

∑

P≼{Cℓ}ℓ∈[1,k]
P={S1,...,SM }
|Sm|≤2 ∀m
|P|=k−j
 



 h
r
 ∑

d|Q
d>1
 µ(d)2

φ(d)
 




j
 Vk−2j(Q, h; r, c(Sj+1), . . . , c(Sk−j)) + Or,k(h
(k−1)/2+ε).

We are ﬁnally prepared to appeal to Theorem 1.1. If k is odd, then so is k − 2j, so there
is no main term. Suppose that k is even. Recall that B(j + 1, . . . , k − j) denotes the set of
perfect matchings of the set {j + 1, . . . , k − j}. Then the main term is

∑

0≤j≤k/2
(−1)j ∑

P≼{Cℓ}ℓ∈[1,k]
P={S1,...,SM }
|Sm|≤2 ∀m
|P|=k−j
 



h
r
 ∑

d|Q
d>1
 µ(d)2

φ(d)
 





j ∑

σ∈B(j+1,...,k−j)
 ∏

(i1,i2)∈σ V2(Q, h; r, c(Si1), c(Si2)),(29)

which proves the ﬁrst claim in Theorem 1.2.
By Lemma 3.2, V2(Q, h; r, c(Si1), c(Si2)) = Or,k(h) unless c(Si1) = c(Si2). So, the largest
term comes from those σ with c(Si1) = c(Si2) for all (i1, i2) ∈ σ. Note that the error term is
then quite large; it is only smaller by a factor of (log h)−1.

14 VIVIAN KUPERBERG

If there exists some σ with c(Si1) = c(Si2) for all (i1, i2) ∈ σ, then it must be that |Cℓ|
is even for all ℓ. Moreover, each term in this sum corresponds to a perfect pairing of [1, k]
such that for each pair (i1, i2), ci1 = ci2; either two indices are paired by lying in the same
Sm, or by lying in the same element of σ. The choice of P then corresponds to choosing j of
these pairs. Note also that V2(Q, h; r, c, c) = V2(Q, h; r, c′, c′) + Or(h
1/2+ε) for any c, c′ mod r,
which allows us to simplify the main term in this case to get

#̃B(c1, . . . , ck) ∑

0≤j≤k/2
(−1)j(k/2
j
 ) 



h
r
 ∑

d|Q
d>1
 µ(d)2

φ(d)
 





j
 V2(Q, h; r, 0, 0)k/2−j,

where #̃B(c1, . . . , ck) is the number of ways to pair the ci’s such that every pair has equal
values. By the binomial theorem, this is

#̃B(c1, . . . , ck)
 



V2(Q, h; r, 0, 0) − h
r
 ∑

d|Q
d>1
 µ(d)2

φ(d)
 





k/2
 .

By Lemma 3.2, this is

#̃B(c1, . . . , ck) (
−hφ(r)
r log h + C0(r)h
)k/2 + Or,k(h
(k−1)/2+ε),

for C0(r) deﬁned in (21), which gives the result.

5. Weighting by smooth functions

We now consider sums of singular series weighted by smooth functions and the proofs of
Theorems 1.3 and 1.5. Theorem 1.3 follows arguments identical to those in the proof of
Theorem 1.1 as well as Theorem 1 of [7]. In particular, all estimates used in bounding E(α)
in the proof of Theorem 1 of [7] hold for the sums Efi,h(α) that we consider in the smooth
setting, and the remainder of the proof is identical.
Accordingly, for the proof of Theorem 1.3 we restrict our attention to relevant estimates
of the sums Efi,h(α), which is the only place where the proof diﬀers. These estimates, the
equivalents of Lemmas 4 and 6 from [8], are contained in Section 5.1.
Similarly for Theorem 1.5, the proof is identical to that of Theorem 1.2 presented in
Section 4, so we omit it. In Section 5.2, we prove Lemma 1.4, whose proof follows similar
lines as the proofs in Section 3.

5.1. Exponential sums weighted by smooth functions.

Lemma 5.1. Let m, h ≥ 1, let f1, f2 : R → R be a smooth functions with compact support
such that | ˆfi(ξ)| = O(|ξ|−2), and deﬁne Efi,h by (12). Then

(30) ∑

µ mod m
µ̸=0
 Ef1,h ( µ
m
 ) Ef2,h ( µ
m
) ≪f1,f2 mh
−2 min{m
3, h
3}.

RESTRICTED SUMS OF SINGULAR SERIES 15

Moreover, for any α ∈ R,

(31) ∑

µ mod m Ef1,h ( µ
m + α) Ef2,h ( µ
m + α) = h
2 ˆf (
− h
m (mα))2 + Of (mh
−2 min{m
3, h
3}).

Proof. Begin with the second statement. Expand via (13) to get
∑

µ mod mEf1,h ( µ
m + α) Ef2,h ( µ
m + α)

= h
2 ∑

µ mod m ˆf1(−h(µ/m + α)) ˆf2(−h(µ/m + α))

+ O(
mh
−2 + ∑

µ mod m ˆf1(−h(µ/m + α)) + ˆf2(−h(µ/m + α)))

= h
2 ∑

µ mod m ˆf1(−h(µ/m + α)) ˆf2(−h(µ/m + α)) + Of1,f2 (min{m, m
2h
−2}) .

Let µ0 be the value of µ such that ∣
∣
∣ µ
m + α∣
∣
∣ is minimized; then µ
m + α = mα/m. If m ≤ h,
then

h
2 ∑

µ mod m ˆf1(−h(µ/m + α)) ˆf2(−h(µ/m + α))

= h
2 ˆf1
 (
− h
m mα) ˆf2
 (
− h
m mα) + h
2 ∑

µ mod m
µ̸=µ0
 ˆf1(−h(µ/m + α)) ˆf2(−h(µ/m + α))

≪f1,f2 h
2 + O(m
4h
−2),

using the fact that | ˆfi(ξ)| = O(|ξ|−2). On the other hand, if m > h, then

h
2 ∑

µ mod m ˆf1(−h(µ/m + α)) ˆf2(−h(µ/m + α))

= h
2 ∑

µ mod m
|µ/m+α|≤m/h
 ˆf1(−h(µ/m + α)) ˆf2(−h(µ/m + α))

+ h
2 ∑

µ mod m
|µ/m+α|>m/h
 ˆf1(−h(µ/m + α)) ˆf2(−h(µ/m + α))

≪f1,f2 h
2 m
h ˆf (0)2 + h
2 m
h
≪f1,f2 mh,

as desired.
Equation (30) follows from the proof of (31) for α = 0 upon excluding the term m = 0. □

Remark. In the case of analogous exponential sums in the function ﬁeld case of polynomials
over Fq[t], as explored in [4], the sum analogous to ∑

µ mod m E ( µ
m + α)2 can be bounded
by the analog of mh whenever α is large, i.e. whenever α is a rational function of suﬃ-
ciently large degree (see Lemma 3.4 of [4]). The equivalent statement here would be that

16 VIVIAN KUPERBERG
∑

µ mod m E ( µ
m + α)2 is bounded by mh whenever α is far away from an integer. However,
this is not true: if m is even and α is very close to 1
2, say, then this sum will still have a
contribution of size h
2.
In the function ﬁeld case of [4], the simpliﬁed and stronger bounds correspondingly yield a
simpliﬁed proof of the analog of Theorem 1.3. The smooth weights fi make the exponential
sums here cleaner, but because the function ﬁeld-style bounds are not available for the sums
in Lemma 5.1, the simpliﬁed proof of the analog of Theorem 1.3 in the function ﬁeld case
also fails to apply.

The following lemma corresponds to Lemma 6 of Montgomery and Vaughan’s work.

Lemma 5.2. Let f1, f2 : R → R be smooth functions with compact support such that | ˆfi(ξ)| =
O(|ξ|−2), and deﬁne Efi,h by (12). Fix α1, α2 ∈ R. Then

(32) ∑

µ mod m Ef1,h ( µ
m + α1) Ef2,h ( µ
m + α2) ≪ (m + h)Ef1f2(α1 − α2) + O(m).

Proof. By Lemma 3 from [8],
∑

µ mod m
Ef1,h ( µ
m + α1) Ef2,h ( µ
m + α2)

= ∑

µ mod m h
2 ˆf1 (−h µ
m − hα1) ˆf2 (−h µ
m − hα2) + O(m)

≪ (m + h) ∫ ∞

−∞ ˆf1(−ht − hα1) ˆf2(−ht − hα2)h
2dt + O(m),

keeping in mind that fi(x) ≍ fi(y) whenever |x − y| ≤ 1/h. The integral is the convolution
of ˆf1 and ˆf2:

(m + h) ∫ ∞

−∞ ˆf1(−ht − hα1) ˆf2(−ht − hα2)h
2dt = (m + h)h ∫ ∞

−∞ ˆf1(u) ˆf2(u + hα1 − hα2)du

= (m + h)h ˆf1 ∗ ˆf2(hα2 − hα1)k

= (m + h)Ef1f2,h(α1 − α2) + O(m/h),

which yields the desired bound. □

Remark. The bound in Lemma 5.2 improves on the analogous lemma in [8] by a factor of
log h. However, the improvement in this lemma does not aﬀect the error term in Theorem
1.3.

5.2. Proof of Lemma 1.4.

Lemma 5.3. Fix h ≥ 1, and let f : R≥0 → C be a smooth function with compact support
supp(f ) ⊂ (0, ∞) and such that | ˆf (ξ)| ≪ O(|ξ|−2). Deﬁne

S(f, h) :=
 ∞∑

m=1 f (m
h
 ) S({0, m}).

Then

S(f, h) = {Mf }(2)h− {Mf ′}(1)
2 log h+ {Mf ′}(1)
2
 (γ0 − log 2π − {Mf ′′}
{Mf ′}(1)
 )+Of (h
−1/2+ε),

RESTRICTED SUMS OF SINGULAR SERIES 17

where γ0 denotes the Euler–Mascheroni constant and for a function g, {Mg}(s) is the Mellin
transform of g deﬁned in (15).

Proof. The proof proceeds almost entirely along the lines of Proposition 2.1 in [5], so we will
be brief. Deﬁne for Re(s) > 1
 F (s) := ∑

n≥1
 S({0, n})
ns ,

so that

(33) S(f, h) = 1
2πi
 ∫
(2) F (s)h
s{Mf }(s)ds.

As noted in [5] and [7], F (s) admits a meromorphic continuation to Re(s) > −1/2 via

F (s) = ζ(s)ζ(s + 1) ∏

p prime
 (
1 − 1 − 1/ps)2

(p − 1)2
 ) .

Since f is smooth and has compact support, {Mf }(s) is analytic in Re(s) > 0. It can be
extended meromorphically to the complex plane via the identity

{Mf } = −1
s {Mf ′},

which follows from integration by parts. Thus {Mf }(s) has simple poles at all nonpositive
integers and no other poles.
The result follows from moving the line of integration in (33) to Re(s) = −1/2 + ε and
recording the contributions from the simple pole at s = 1 and the double pole at s = 0. □

We are now ready to prove Lemma 1.4.

Proof. Begin by expanding

V2(Q, h; f1, f2)

= −Ef1,h(1)Ef2,h(1) + ∑

q|Q
 µ(q)2

φ(q)2 ∑

1≤a≤q
(a,q)=1
 Ef1,h
 (a
q
 ) Ef2,h
 (
−a
q
 )

= −h
2 ˆf1(0) ˆf2(0) + Of1,f2(1)

+ ∑

q|Q
 µ(q)2

φ(q)2 ∑

1≤a≤q
(a,q)=1
 ∞∑

m1,m2=1 f1 ( m1
h
 ) f2 (
−m2
h
 ) e (
(m1 − m2) a
q
 )

= −h
2 ˆf1(0) ˆf2(0) + Of1,f2(1) +
 ∞∑

m1,m2=1 f1 (m1
h
 ) f2 (
−m2
h
 ) ∑

q|Q
 µ(q)2

φ(q)2 cq(m1 − m − 2),

18 VIVIAN KUPERBERG

where cq(m) is a Ramanujan sum. Just as for the arithmetic progressions case, this simpliﬁes
to
 = −h
2 ˆf1(0) ˆf2(0) +
 ∞∑

m1,m2=1
m1̸=m2
 f1 (m1
h
 ) f2 (−m2
h
 ) S({0, m1 − m2})

+
 ∞∑

m=1 f1 (m
h
 ) f2 (
−m
h
 ) + Of1,f2(1),

since for any m ̸= 0, by our choice of Q,
∑

q|Q
 µ(q)2

φ(q)2 cq(m) = ∏

p|m
 (
1 + 1
p − 1
 ) ∏

p∤m
 (
1 − 1
(p − 1)2
 ) = S({0, m}) + O(h
−2).

The sum over m can be interpreted as a Riemann sum as h → ∞, yielding

∞∑

m=1 f1 ( m
h
 ) f2 (−m
h
 ) = h ∫ ∞

0 f1(x)f2(−x)dx + Of1,f2(1)

= h(f1 ∗ f2)(0) + Of1,f2(1).

Similarly, the sum over m1 and m2 can also be interpreted as a Riemann integral (and also
as the convolution of f1 and f2), yielding

∞∑

m1,m2=1
m1̸=m2
 f1 ( m1
h
 ) f2 (
−m2
h
 ) S({0, m1 − m2})

=
 ∞∑

m=1 S({0, m})
 ∞∑

n=1
 (
f1 (n
h
 ) f2
 (m − n
h
 ) + f1 ( n
h
 ) f2
 (−m − n
h
 ))

=
 ∞∑

m=1 S({0, m})h (
(f1 ∗ f2) (m
h
 )) + Of1,f2
 ( Ch∑

m=1 S({0, m})
)
 ,

where C is a constant large enough that f1(x) = f2(x) = 0 for any |x| ≥ C/2; note that C
depends only on f1 and f2. By the results of [1] and [7], the error term is Of1,f2(h). For the
inside sum, apply Lemma 5.3 with f = f1 ∗ f2 to get

∞∑

m1,m2=1
m1̸=m2
 f1 ( m1
h
 ) f2 (
−m2
h
 ) S({0, m1 − m2})

= {Mf }(2)h
2 − {Mf ′}(1)
2 h log h + Of1,f2(h),

which, after collecting terms, implies the result. □

References

1. P. X. Gallagher, On the distribution of primes in short intervals, Mathematika 23 (1976), no. 1, 4–9.
MR 409385
2. D. A. Goldston, Linnik’s theorem on Goldbach numbers in short intervals, Glasgow Math. J. 32 (1990),
no. 3, 285–297. MR 1073669

RESTRICTED SUMS OF SINGULAR SERIES 19

3. A. Granville and K. Soundararajan, Sieving and the Erd˝os-Kac theorem, Equidistribution in number
theory, an introduction, NATO Sci. Ser. II Math. Phys. Chem., vol. 237, Springer, Dordrecht, 2007,
pp. 15–27. MR 2290492
4. V. Kuperberg, Odd moments in the distribution of primes, arXiv:2109.03767, 2021.
5. R. J. Lemke Oliver and K. Soundararajan, Unexpected biases in the distribution of consecutive primes,
Proc. Natl. Acad. Sci. USA 113 (2016), no. 31, E4446–E4454. MR 3624386
6. H. L. Montgomery and K. Soundararajan, Beyond pair correlation, Paul Erd˝os and his mathematics, I
(Budapest, 1999), Bolyai Soc. Math. Stud., vol. 11, J´anos Bolyai Math. Soc., Budapest, 2002, pp. 507–514.
MR 1954710
7. , Primes in short intervals, Comm. Math. Phys. 252 (2004), no. 1-3, 589–617. MR 2104891
8. H. L. Montgomery and R. C. Vaughan, On the distribution of reduced residues, Ann. of Math. (2) 123
(1986), no. 2, 311–333. MR 835765
