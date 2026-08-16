<!-- source: https://arxiv.org/pdf/1106.0369 | converted from PDF -->

arXiv:1106.0369v1  [math.CO]  2 Jun 2011Minimum density of union-closed families

Igor Balla

November 12, 2018

Abstract

Let F be a ﬁnite union-closed family of sets whose largest set con-
tains n elements. In [6], W´ojcik deﬁned the density of F to be the
ratio of the average set size of F to n and conjectured that the mini-
mum density over all union-closed families whose largest set contains n
elements is (1 + o(1)) log2 n/(2n) as n → ∞. We use a result of Reimer
[3] to show that the density of F is always at least log2 n/(2n), verify-
ing W´ojcik’s conjecture. As a corollary we show that for n ≥ 16, some
element must appear in at least √
(log2 n)/n(|F |/2) sets of F .

1 Preliminaries and Notations

Given a family of sets F , we say F is union-closed if for all A, B ∈ F ,
A ∪ B ∈ F . In what follows, a union-closed family will always be taken to
mean a ﬁnite union-closed family of ﬁnite sets. Let N = {1, 2, 3, . . .} be the
set of natural numbers. We denote the cardinality of a ﬁnite set A by |A| :=∑x∈A 1 and denote the union of a family of sets F by ⋃ F := ⋃A∈F A.
Given sets A, B, the set diﬀerence A \ B := {x ∈ A|x /∈ B}.
Let F be a union-closed family and let n = | ⋃ F |. To avoid trivial cases,
in this paper we only consider F with n ≥ 1. Deﬁne Fa = {S ∈ F |a ∈ S}
for all a ∈ ⋃ F . We deﬁne the density of F by

D(F ) := 1
n|F |
 ∑

A∈F |A| = 1
n|F |
 ∑

a∈
⋃ F |Fa|

and denote the minimum density over all union-closed families F with
| ⋃ F | = n by sn := min {D(F )|F union-closed, | ⋃ F | = n} for all n ∈ N.

1

2 Some Previous Conjectures and Results

Interest in studying the structure of union-closed families ﬁrst arose because
of the following conjecture due to Frankl in 1979.

Conjecture 1 (Frankl). For all union-closed families F , there exists an
a ∈ ⋃ F such that |Fa| ≥ |F |/2.

Although much research has been done on union-closed families, we still
seem to be far from being able to prove Conjecture 1. Roberts [4] showed
that Conjecture 1 holds when |F | ≤ 40 and Boˇsnjak and Markovi´c [1]
showed that it holds when | ⋃ F | ≤ 11. Additionally, Sarvate and Renaud,
Poonen [5, 2] and others have shown that Conjecture 1 holds if there exists
an S ∈ F with |S| = 1, 2. In order to generalize this idea, W´ojcik [6] deﬁned
the notions of density and minimum density as stated above and proved the
following theorem.

Theorem 1 (W´ojcik [6]). Let F be a union-closed family and let S ∈ F
with |S| = k. Then ∑

a∈S |Fa| ≥ ksk|F |.

One can easily verify that s1, s2 = 1/2, so Theorem 1 shows that Conjec-
ture 1 holds if there exists S ∈ F with |S| = 1, 2. Unfortunately, s3 = 4/9
and W´ojcik showed in [6] that for any ǫ > 0, k ∈ N, one can ﬁnd a union-
closed family F with S ∈ F , |S| = k such that |Fa| < (sk + ǫ)|F | for
all a ∈ S. Thus having a 3-set in a union-closed family F is not enough
to guarantee that one of its elements satisﬁes Conjecture 1. In any case,
it is an interesting question to be able to determine sk in general. W´ojcik
conjectured that

Conjecture 2 (W´ojcik [6]). For all n ∈ N, a union-closed family F with
| ⋃ F | = n which attains the minimum density sn is of the form F :=
{A|A ⊆ {1, 2, . . . , k}} ∪ {{1, 2, . . . , n}} where k = ⌊log2 n⌋ or ⌈log2 n⌉.

He veriﬁed this claim for n ≤ 10, and noted that as a consequence we
would have sn = (1 + o(1)) log2 n
2n as n → ∞. W´ojcik claimed, without
providing the proof, that Conjecture 1 implies this asymptotic result. In
Corollary 1, we verify this asympotic result, giving more evidence towards
the truth of Conjectures 1 and 2. In order to do so, we use a theorem proven
by Reimer in [3] bounding the average set size of a union-closed family.

2

Theorem 2 (Reimer [3]). For all union-closed families F ,

1
|F |
 ∑

A∈F |A| ≥ 1
2 log2 |F |.

3 Main Results

The main goal of this paper to show that for all union-closed families F
with | ⋃ F | = n, D(F ) ≥ log2 n/(2n). In the case where |F | ≥ n, Theorem
2 gives us the desired result. In the other case |F | < n, we will need Lemma
2.

Lemma 1. Let F be a union-closed family, let A ∈ F be a minimal non-
empty set and let G := F \ {A}. If there exist a, b ∈ ⋃ G such that Ga = Gb
but Fa ̸= Fb then a ∈ B for all non-empty B ∈ F or b ∈ B for all
non-empty B ∈ F .

Proof. If both a, b ∈ A or both a, b /∈ A then Fa = Fb. Otherwise without
loss of generality we have a ∈ A and b /∈ A. Now suppose there exists a
non-empty B ∈ G such that a /∈ B. Then B /∈ Ga = Gb, so b /∈ B and thus
b /∈ A ∪ B. A ∪ B ̸= A by minimality of A, and so A ∪ B ∈ G since F is
union-closed. But a ∈ A ⊆ A ∪ B, contradicting Ga = Gb.

Lemma 2. For all union-closed family F with | ⋃ F | ≥ 2 and |F | <
| ⋃ F |, there exist distinct a, b ∈ ⋃ F such that Fa = Fb.

Proof. We induct on |F |. For |F | = 1, F = {
⋃ F }, so we can choose
any a, b ∈ ⋃ F to satisfy Fa = Fb. Now let F be a union-closed family
with |F | = m ≥ 2 and | ⋃ F | = n such that m < n. Let A ∈ F be
a minimal non-empty set and let G := F \ {A}. If A = ⋃ F then we
must have F = {A, ∅}, so we can choose any a, b ∈ A to satisfy Fa = Fb.
Otherwise we have | ⋃ G | = | ⋃ F | = n. No 2 sets of G can have union A
by minimality of A, so G is union-closed because F is. Since |G | = m − 1,
we can apply the induction hypothesis to G to obtain distinct a, b ∈ ⋃ G
such that Ga = Gb. If Fa = Fb then we are done. Otherwise we can
apply Lemma 1 and without loss of generality have a ∈ B for all non-empty
B ∈ F . Now deﬁne G ′ := {B \ {a}|B ∈ G }, so that |G ′| ≤ |G | = m − 1
and | ⋃ G ′| = | ⋃ G \ {a}| = n − 1. G ′ is union-closed because G is, so we
can apply the induction hypothesis to G ′ to obtain distinct c, d ∈ ⋃ G ′ such
that G ′
c = G ′
d. Thus Gc = Gd. If Fc = Fd then we are done. Otherwise
again applying Lemma 1, without loss of generality we have c ∈ B for all
non-empty B ∈ F . So then Fa = Fc, and the claim holds by induction.

3

Note that for any n ∈ N, the family F := {{1, 2, . . . k}|k ∈ {1, 2, . . . , n}}
is union-closed with |F | = n = | ⋃ F | such that Fa ̸= Fb for all distinct
a, b ∈ ⋃ F . Thus Lemma 2 is in some sense best possible.

Theorem 3. For all n ∈ N,
 sn ≥ log2 n
2n .

Proof. We proceed by induction. For n = 1, trivially s1 ≥ 0 = log2 n/(2n).
Now suppose sn ≥ log2 n/(2n) for some n ∈ N and let F be a union-closed
family with | ⋃ F | = n + 1. If |F | ≥ n + 1 then by Theorem 2,

D(F ) = 1
(n + 1)|F |
 ∑

A∈F |A| ≥ log2 |F |
2(n + 1) ≥ log2 (n + 1)
2(n + 1) .

Otherwise |F | ≤ n, so we can apply Lemma 2 to obtain distinct a, b ∈ ⋃ F
such that Fa = Fb. Thus we can deﬁne G := {A \ {a}|A ∈ F }, so that
|G | = |F | and G is union-closed since F is. Now | ⋃ G | = | ⋃ F \ {a}| = n,
so we can apply the induction hypothesis to obtain
∑

x∈
⋃ F \{a} |Fx| = ∑

x∈
⋃ G |Gx| = nD(G )|G | ≥ nsn|G | ≥ 1
2 |F | log2 n.

Using the limit deﬁnition of e we see that
( n + 1
n
 )|F | ≤ (1 + 1
n
 )n ≤ e ≤ 4.

Thus
 |F |(log2 (n + 1) − log2 n) = log
 (( n + 1
n
 )|F |)
 ≤ log2 4 = 2.

Finally observing that |Fa| ≥ 1, we obtain
∑

x∈
⋃ F |Fx| = |Fa| + ∑

x∈
⋃ F \{a} |Fx| ≥ 1 + 1
2 |F | log2 n ≥ 1
2 |F | log2 (n + 1).

Thus D(F ) ≥ log2 (n + 1)/(2(n + 1)) and the claim holds by induction.

With repeated application of Lemma 2, it can be proven that either
1
|F | ∑A∈F |A| ≥ n(n − 1)/2 or there exist α, β ∈ ⋃ F distinct, such that
Fα = Fβ. This may be combined with Theorem 2, to yield a better lower
bound on sn using the same techniques as in Theorem 3. Work is currently
being done along these lines to verify Conjecture 2.

4

Corollary 1.
 sn = (1 + o(1)) log2 n
2n .

as n → ∞.

Proof. Let n ∈ N and let k := ⌈log2 n⌉. Deﬁne F := {A|A ⊆ {1, . . . , k}} ∪
{{1, 2, . . . , n}}. Observe that F is union-closed with | ⋃ F | = n. Thus we
have
 sn ≤ D(F ) = k2k−1 + n
n(2k + 1) = (1 + o(1)) log2 n
2n

as n → ∞. On the other hand, sn ≥ log2 n/(2n) by Theorem 3.

Corollary 2. Let n ∈ N with n ≥ 16 and let F be a union-closed family
with | ⋃ F | = n. Then there exists an a ∈ ⋃ F such that

|Fa| ≥ 1
2
 √ log2 n
n |F |.

Proof. Let S ∈ F be a non-empty set with minimum |S| and let k = |S|.
Deﬁne G := F \ {∅, ⋃ F } so that ∑
A∈G |A| ≥ k(|F | − 2), and thus

max
a∈
⋃ F |Fa| ≥ 1
n
 ∑

a∈
⋃ F |Fa| = 1
n
 ∑

A∈F |A| = 1 + 1
n
 ∑

A∈G |A| ≥ 1 + k
n (|F | − 2).

If k > n/2, then

max
a∈
⋃ F |Fa| ≥ 1 + k
n (|F | − 2) > |F |
2 ≥ 1
2
 √ log2 n
n |F |

so we are done. Otherwise k ≤ n/2 and so we obtain

max
a∈
⋃ F |Fa| ≥ 1 + k
n (|F | − 2) ≥ 2k + (|F | − 2)k
n = k
n |F |. (1)

Additionally, we can apply Theorem 1 to obtain

max
a∈
⋃ F |Fa| ≥ max
a∈S |Fa| ≥ 1
k
 ∑

a∈S |Fa| ≥ sk|F |.

If k ≤ 2, then we observe that sk = 1/2 so we are done. Otherwise k ≥ 3.
By Theorem 3 we have

max
a∈
⋃ F |Fa| ≥ sk|F | ≥ log2 k
2k |F |. (2)

5

Consider the function f : [4, ∞) → [16, ∞) deﬁned by f (x) := 2x2/ log2 x for
all x ∈ [4, ∞). Since f increasing and f (4) = 16, we can deﬁne the inverse
function g : [16, ∞) → [4, ∞) of f . We have

g(n)
n = g(n)
f (g(n)) = log2 g(n)
2g(n) .

Thus g(n) = √n log2 √g(n) and since g(n) ≥ 4,

g(n)
n =
 √n log2 √g(n)

n =
 √ log2 g(n)
2n =
 √
√
√
√ log2 √n log2 √g(n)

2n

=
 √ log2 n + log2 (log2 √g(n))
4n ≥ 1
2
 √ log2 n
n .

Now suppose for sake of contradiction that maxa∈
⋃ F |Fa| < (g(n)/n)|F |.
Then by (1), g(n) > k. But by (2) we also have

log2 g(n)
2g(n) = g(n)
n > max
a∈
⋃ F |Fa| ≥ log2 k
2k .

Since log2 x/(2x) is decreasing for x > e and g(n) ≥ 4 > e, k ≥ 3 > e, it
follows that g(n) < k, a contradiction. Thus

max
a∈
⋃ F |Fa| ≥ g(n)
n |F | ≥ 1
2
 √ log2 n
n |F |.

Corollary 2 clearly does not give a sharp lower bound and with some
work the technique used in the proof can be extended to prove a slightly
better bound. In this paper we decided against spoiling the neatness of the
result by doing so. In any case, the above technique is not powerful enough
to prove Conjecture 1, since the minimum density sn < 1/2 for n ≥ 3.

References

[1] Boˇsnjak, I., Markovi´c, P. The 11-element case of Frankl’s conjecture.
Electron. J. Comb., 15(1), 2008.

[2] Poonen, Bjorn. Union-closed families. J. Comb. Theory Ser. A,
59(2):253–268, 1992.
 6

[3] Reimer, David. An average set size theorem. Comb. Probab. Comput.,
12(1):89–93, 2003.

[4] Roberts, I. Tech. Rep. No. 2/92. School Math. Stat., Curtin Univ. Tech.,
Perth, 1992.

[5] Sarvate, D. G., Renaud, J.-C. On the union-closed sets conjecture. Ars
Combin., 27:149–153, 1989.

[6] W´ojcik, Piotr. Density of union-closed families. Discrete Math., 105(1-
3):259–267, 1992.
 7
