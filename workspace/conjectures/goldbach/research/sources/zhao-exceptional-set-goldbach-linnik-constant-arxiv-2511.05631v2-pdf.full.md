<!-- source: https://arxiv.org/pdf/2511.05631v2 | converted from PDF -->

THE EXCEPTIONAL SET OF GOLDBACH PROBLEM AND
LINNIK’S CONSTANT

GENHENG ZHAO

Abstract. Let E(X) denote the number of even integers below X which

are not a sum of two primes. We prove the bound E(X) = O(X 7
10 ), where
the implicit constant is ineffective. The method applied here also leads to
P (q) = O(q5), where P (q) denotes the least prime, if it exists, in any arithmetic
progression modulo q.
 1. Introduction

The famous Goldbach conjecture asserts that every even integer m ≥ 6 is a sum
of two odd primes. Though the original conjecture is still unsolved today, there
have appeared various approximations which are available by current methods.
One typical example is to bound the number of possible exceptions.
Let E(X) denote the size of exceptional set, which consists of even integers
m ≤ X which are not a sum of two odd primes. In the 1920s, under the generalized
Riemann hypothesis, Hardy-Littlewood [2] used their newly invented circle method
to show the bound
 E(X) = Oε(X 1/2+ε), ∀ ε > 0. (1.1)

The later breakthrough of Vinogradov [1] in the 1930s was able to reach the un-
conditional bound
 E(X) = OA(X(log X)−A), ∀A > 0. (1.2)

Bounds of such type are often related to Siegel-Walfisz theorem, which gives the
uniform distribution of primes p ≤ X among congruence classes with moduli q ≤
(log X)A, ∀A > 0. When q gets larger, such uniformity will inevitably be broken
by the possibly existing Siegel zero of some L-function. Hence for better bounds
of E(X), the effect of Siegel zero must be taken into account. This was done by
Vaughan in 1972, allowing him to replace Siegel-Walfisz theorem by Page’s theorem
to obtain
 E(X) = O(Xe
−c
√log X ). (1.3)

Soon after this improvement, in 1975 Montgomery-Vaughan [3] showed that

E(X) = O(X 1−δ) (1.4)

1arXiv:2511.05631v2  [math.NT]  23 Jan 2026
2 GENHENG ZHAO

holds with some δ > 0. Their method can be seen as a generalization of Linnik’s
method [4] showing
 P (q) = O(qL) (1.5)

holds with some L < ∞, where P (q) denotes the least prime in any arithmetical
progression {a, q + a, 2q + a, · · · } with 1 ≤ a ≤ q and (a, q) = 1.
Linnik’s method relies on three intricate principles on the distribution of zeroes
of L-functions near the line σ = 1, including a zero-free region with at most one
exception, a log-free zero density estimate and a quantified version of Deuring-
Heilbronn phenomenon. Roughly speaking, these three principles together serve as
a substitute for the zero free region

σ ≥ 1 − c
log(qT ) , |t| ≤ T (1.6)

based on which the bound (1.5) would be quite clear. Obviously, the admissible
values of δ and L are closely related to the constants appeared in these principles.
For such a result concerning L, see [15, Corollary 18.8].
The first admissible value of δ was obtained by J. R. Chen and J. M. Liu [5],
where they showed δ = 0.05. They [6] also showed that L = 13.5 is admissible. In
1991, Heath-Brown [11] developed the currently sharpest tool to obtain zero free
regions of L-functions, giving the improvement L = 5.5. This was further improved
to L = 5.2 by Xylouris [9] in 2009, which is still best up to date. On the other
hand, by exploiting Heath-Brown’s idea, the admissible value of δ was improved to
δ = 0.086 by H. Z. Li [7], δ = 0.121 by W. C. Lu [8] and finally δ = 0.28 by Pintz
[13], which seems to match the result L = 5.2.
In this paper, with a refinement of Pintz’s method, we verify that δ = 0.3 is
admissible. In other words, we have the following.

Theorem 1.1. E(X) = O(X 7
10 ), where the implicit constant is ineffective.

In light of Pintz’s reduction [13, Section 2], we only need to consider the contri-
bution of zeroes of L-functions for a single moduli q, in a highly restricted area

σ ∈ [1 − H(log q)−1, 1], |t| ≤ H, (1.7)

where H is a fixed positive constant. We may denote the multi-set of these zeroes
by Z(χ, H), Z(K, H) the union of Z(χ, H) for all χ ∈ K and always write

ϱ = β + iγ, 1 − ϱ = λ + iµ
log q . (1.8)

It remains to show the following result.

Theorem 1.2. Let q, H ≥ 1 and c0 > 0. Let {Ki}i≥1 be pairwise disjoint sets of
characters module q. For i ≥ 1, let Zi = Z(Ki, H) and suppose

max
(χ,χ′)∈K2
i cond(χχ
′) ≤ c−1
0 , min
ϱ∈Zi λ ≥ c0. (1.9)

THE EXCEPTIONAL SET OF GOLDBACH PROBLEM AND LINNIK’S CONSTANT 3

Then for q ≥ q(H, c0) we have

∑

i≥1
 

 ∑

ϱ∈Zi e− 10
3 λ




2
 ≤ 1 − c1, (1.10)

where c1 > 0 depends only on c0.

In [13], Pintz showed (1.10) with 25/7 in place of 10/3. Hence we have reduced
the value by 5/21 = 0.2380 · · · . We can deduce from the original argument the
estimate (1.10) with 1.277 in place of 1 − c1. The small saving 0.277 consists of two
parts: a refined estimate of sums of the type
∑

ϱ∈Z e− 10
3 max{λ,Λ} (1.11)

which contributes 0.114 and an estimate of sums of the type
∑

ϱ∈Zi(e
− 10
3 λ − e− 10
3 Λ) (1.12)

which contributes 0.163.
We shall mention that the refined argument here has also uncovered the potential
of Pintz’s method to improve some other results such as Linnik’s constant. Let
Z(q, H) the union of all Z(χ, H) with χ modulo q.

Theorem 1.3. Let q, H ≥ 1, c0 > 0. Assume that

min
ϱ∈Z(q,H) λ ≥ c0. (1.13)

Then for q ≥ q(H, c0) we have ∑

ϱ∈Z(q,H) e−5λ ≤ 1 − c1, (1.14)

where c1 > 0 depends only on c0.

Since it is much simpler than Theorem 1.2, we are not going to provide details
for its proof. Recall the standard notation

π(X; q, a) = ∑

p≤X
p≡a(mod q)
 1. (1.15)

Theorem 1.3 combined with the argument in [10] gives the following result.

Theorem 1.4. Let 1 ≤ a ≤ q and (a, q) = 1. Let X = qϑ with ϑ ≥ 5 being fixed.
Then we have for any ε > 0 that

0 < π(X; q, a) ≤ (2 + ε)X
ϕ(q) log X , q ≥ q(ε). (1.16)

4 GENHENG ZHAO

This clearly shows L = 5 is addmissible. The improvement from L = 5.2 to
L = 5 is essentially due to Pintz’s generalization of Heath-Brown’s new zero density
estimate, which counts all zeroes of L(s, χ) rather than the number of L(s, χ) which
has at least a zero in the area

σ ∈ [1 − Λ(log q)−1, 1], |t| ≤ H, (1.17)

with Λ ≤ 1.6. This fully avoids the use of the function (2.1) which is less optimal
than the function (2.4), in Heath-Brown’s method.
The remaining parts of this paper are arranged as follows. In Section 2 we will
introduce some preliminary results for the estimates of certain sums over zeroes in
Section 3. Finally we prove Theorem 1.2 in Section 4.

2. Preliminary results

Let H ≥ 1 and z0, t0 ∈ [0, 2H]. We now introduce several special functions used
in [11], including
 f1(t) = 1t∈[0,t0] sinh(z0(t0 − t)) (2.1)

and its Laplace transform

F1(z) = ∫ ∞

0 f1(t)e−tudt = 1
2
 ( e
z0t0

z0 + z + e−z0t0

z0 − z − 2z0e−zt0

z2
0 − z2
 ) . (2.2)

Note first that f1(t) and F1(z) vary in a compact set depending merely on H.
Moreover, the function F1(z) obeys the property that for Re(z) ≥ 0,

Re(F1(z)) ≥ z0
2 ez0t0 |F2(z0 + z)|, (2.3)

where
 F2(z) = ( 1 − e−t0z

z
 )2 . (2.4)

We will use this relation to treat

max
ϱ∈Z(χ,H)
 ∑

ϱ′∈Z(χ,H) |F2(λ + λ′ − i(µ − µ
′))| (2.5)

for some χ modulo q. Note that
 |F1(z)| ≪ 1
1 + |z| (2.6)

and by a zero density estimate of Jutila [14, Theorem 2], when q ≥ q(H),

#Z(χ, H) = O(e
3H ), (2.7)

Let ϕ = 1/3 be fixed. Then [11, Lemma 5.2] and [11, Lemma 5.3] easily lead to the
following estimate.

THE EXCEPTIONAL SET OF GOLDBACH PROBLEM AND LINNIK’S CONSTANT 5

Lemma 2.1. Let H ≥ 1, ε > 0 and suppose s = σ + it satisfy

|σ − 1| ≤ H
log q , |t| ≤ 2H. (2.8)

Let χ be a non-principal character modulo q. If χ is non-principal, then for q ≥
q(H, ε) we have

∑

ϱ∈Z(χ,H) Re F1((s − ϱ) log q) ≤ F1((σ − 1) log q) + ϕ
2 f1(0) + ε, (2.9)

Proof. Since χ is non-principal and f1 vary in a compact set depending only on H,
by [11, Lemma 5.2] there exists δ = δ(H, ε) such that

∑

|1+it−ϱ |≤δ Re F1((s − ϱ) log q) ≤ −K1(s, χ) + ϕ
2 f1(0) + ε, (2.10)

where
 K1(s, χ) = 1
log q
 ∑

n≥1 Λ(n) Re ( χ(n)
ns
 ) f1
 ( log n
log q
 ) . (2.11)

We now remove those zeroes with β < 1 − H(log q)−1 in (2.10). This can be done
since σ ≥ 1 − H(log q)
−1 and hence by (2.3), Re F1((s − ϱ)) ≥ 0. Then, we can add
those zeroes in Z(χ, H) with |1 + it − ϱ | ≥ δ into the reduced sum, since by (2.7)
their total number is O(e
3H ) and by (2.6) each contributes O(δ−1(log q)−1). Thus
we obtain ∑

ϱ∈Z(χ,H) Re F1((s − ϱ) log q) ≤ −K1(s, χ) + ϕ
2 f1(0) + 2 ε, (2.12)

provided q ≥ q(H, ε). Meanwhile, by [11, Lemma 5.3] we have

−K1(s, χ) ≤ K1(σ, χ0
q) ≤ F1((σ − 1) log q) + ε . (2.13)

Now the conclusion is clear if we change the value of ε. □

We now obtain a bound of (2.5).

Lemma 2.2. Let H ≥ 1 and ε > 0. Let χ be a non-principal character modulo q.
Assume that each zero ϱ ∈ Z(χ, H) satisfies λ ≥ λ0 ≥ 0. Then for q ≥ q(H, ε), we
have
 max
ϱ∈Z(χ,H)
 ∑

ϱ′∈Z(χ,H) |F2(λ + λ′ − i(µ − µ
′))| ≤ B(t0, λ, λ0) + ε, (2.14)

where

B(t0, λ, λ0) = ϕ
2
 ( 1 − e−2(λ+λ0)t0

λ + λ0
 ) + 1 − e−λt0

λ(λ + λ0) + e−2(λ+λ0)t0 − e−λt0

(λ + λ0)(λ + 2λ0) . (2.15)

6 GENHENG ZHAO

Proof. Fix ϱ ∈ Z(χ, H). We then set z0 = λ + λ0 and (1 − s0) log q = λ0 + iµ,
which leads to
∑

ϱ′∈Z(χ,H) |F2(λ + λ′ − i(µ − µ
′))| ≤ 2
z0 e−z0t0 ∑

ϱ′∈Z(χ,H) Re F1(λ′ − λ0 − i(µ − µ
′)).

(2.16)

By (2.9), for q ≥ q(H, ε) we have
∑

ϱ′∈Z(χ,H) Re F1(λ′ − λ0 − i(µ − µ
′))

= ∑

ϱ′∈Z(χ,H) Re F1((s0 − ϱ′) log q)

≤f1(0) + F1(−λ0) + 2 ε

= ϕ
2
 ( ez0t0 − e−z0t0

2
 ) + 1
2
 ( ez0t0

z0 − λ0 + e−z0t0

z0 + λ0 − 2z0e2λ0t0

z2
0 − λ2
0
 ) + 2 ε,
 (2.17)

which immediately leads to (2.14) from (2.16). □

We need the following elementary property of B(t0, λ, λ0).

Lemma 2.3. Suppose λ, Λ, t0, λ0 ≥ 0, then we have

e− max{Λ−λ,0}t0B(t0, λ, λ0) ≤ B(t0, Λ, λ0). (2.18)

Proof. It suffices to show B(t0, λ, λ0) is decreasing while e
λt0B(t0, λ, λ0) is increas-
ing, with λ. When λ0 = 0, we see

B(t0, λ, 0) = ϕ
2
 ( 1 − e−2λt0

λ
 ) + ( 1 − e−λt0

λ
 )2 (2.19)

clearly obeys this property. Hence we may assume λ0 > 0. Meanwhile, since

ϕ
2
 ( 1 − e−2(λ+λ0)t0

λ + λ0
 ) (2.20)

satisfies this property, it remains to consider

g(λ) = 1 − e−λt0

λ(λ + λ0) + e−2(λ+λ0)t0 − e−λt0

(λ + λ0)(λ + 2λ0) . (2.21)

Notice that by Laplace inversion, we have

g(λ) = 1
λ0
 ∫ 2t0

0
 (e−2λ0 max{t−t0,0} − e−λ0t) e−λtdt (2.22)

and hence
 eλt0g(λ) = 1
λ0
 ∫ t0

0 (1 − e−λ0(t0−t))(eλt + e−(λ+2λ0)t)dt. (2.23)

From this we derive that

g′(λ) = − 1
λ0
 ∫ 2t0

0
 (e−2λ0 max{t−t0,0} − e−λ0t) te
−λtdt ≤ 0 (2.24)

THE EXCEPTIONAL SET OF GOLDBACH PROBLEM AND LINNIK’S CONSTANT 7

and
 (e
·t0 g)
′(λ) = 1
λ0
 ∫ t0

0 (1 − e−λ0(t0−t))t(eλt − e−(λ+2λ0)t)dt ≥ 0, (2.25)

as desired. □

The final task of this section is to label the zeroes. In what follows we will keep
the notations consistent with that in Theorem 1.2. For convenience we label ϱ ∈ Zi
by
 λi,1 ≤ λi,2 ≤ · · · , (2.26)

and {Zi}i≥1 by
 λ1,1 ≤ λ2,1 ≤ · · · . (2.27)

For i ≥ 1, let
 Si = ∑

j≥1 e− 10
3 λi,j . (2.28)

It now remains to show ∑

i≥1 S2
i ≤ 1 − c1. (2.29)

For each Λ ≤ H, let N (Λ) denote the number of zeroes ϱ = β + iγ of
∏

χ(mod q) L(s, χ), (2.30)

in the region
 β ≥ 1 − Λ
log q , |γ| ≤ H. (2.31)

The classical zero free region for L-functions implies that N (Λ) ≤ 1 holds for some
Λ > 0. Meanwhile, if N (Λ) = 1 does hold for some very small value of Λ, then
N (Λ) ≤ 1 will be expected to hold for some considerably large value of Λ, due
to the Deuring-Heilbronn phenomenon. Explicit versions of this phenomenon have
already been established in [11] and [9], and they are still applicable in our setting
if q ≥ q(H, c0), which we henceforth assume,
We end up this section with the following Lemma, according to which our final
argument will be separated into several cases.

Lemma 2.4. Let q be sufficiently large.

(1) If λ1,1 ≤ 0.01, then N (5.68) ≤ 1.
(2) If λ1,1 ≤ 0.10, then N (3.08) ≤ 1.
(3) If λ1,1 ≤ 0.30, then N (1.58) ≤ 1.
(4) If λ1,1 ≤ 0.40, then N (1.29) ≤ 1.
(5) If λ1,1 ≤ 0.60, then N (0.92) ≤ 2.
(6) If λ1,1 ≤ 0.62, then either N (0.85) ≤ 1 or N (0.91) ≤ 2.
(7) If λ1,1 ≤ 0.64, then N (0.85) ≤ 2.
(8) If λ1,1 ≤ 0.68, then N (0.74) ≤ 2.

8 GENHENG ZHAO

Despite the value of λ1,1, we have always N (1.09 log λ−1
1,1) ≤ 1, N (0.702) ≤ 2, and
λi,1 ≥ 0.857 for i ≥ 5.

Proof. Values of Λ for which N (Λ) ≤ 1 are taken from Table 2,3,4,5,7 of [11] and
N (Λ) ≤ 2 are taken from Tabellen 2,3,7 of [9]. The range λ ≤ 1.09 log λ−1
1,1 is a
simple consequence of [11, Lemma 8.8]. The result λi,1 ≥ 0.857 for i ≥ 5 is [11,
Theorem 3]. □

3. Weighted sums over zeroes

In this section we confine our attention to the sum

S = ∑

j≥1 e− 10
3 λj , (3.1)

with max{c0, λ0} ≤ λ1 ≤ λ2 ≤ · · · ≤ H. The underlying set K here may be a union
of several Ki or simply a single one. Let

M = M (K) = max
(χ,χ′)∈K2 cond(χχ
′). (3.2)

Clearly, M = O(1) if K = Ki, i ≥ 1. This would be an advantage when estimating
the value of S, as we can see below.

Lemma 3.1. Let x, y, z, ε, Λ > 0 be given and

k =
 



2(ϕ + 3x + y + z), M = O(1),

2(2ϕ + 3x + y + z), otherwise. (3.3)

Then for q ≥ q(k, ε) we have
∑

j≥1 e
−k max{λj ,Λ} ≤ (1 + ε)C(x, y, z, Λ, λ0), (3.4)

where

C(x, y, z, Λ, λ0) = 1
xz
 ( 1
2 + ϕ + x
y
 ) √
B (ϕ + x + y, Λ, λ0) B(z, Λ, λ0). (3.5)

Proof. Let w(ϱ) = w(λ) be a positive-valued function to be determined later. When
q is sufficiently large, all character can be assumed to be non-principal, since Rie-
mann zeta function has no zeroes in (1.7). By following the argument of [13, Page
19-25], with a slight change on the notations of parameters, it is easy to show that
for q ≥ q(k, ε),


 ∑

ϱ∈Z(K,H) w(ϱ)





2
 ≤ 1 + ε
xz
 ( 1
2 + ϕ + x
y
 )

∑

χ∈K
 ∑

ϱ∈Z(χ,H)
 ∑

ϱ′∈Z(χ,H) w(ϱ)w(ϱ
′)e
k λ+λ′

2 √
(G1G2)(λ + λ′ − i(µ − µ′))

, (3.6)

THE EXCEPTIONAL SET OF GOLDBACH PROBLEM AND LINNIK’S CONSTANT 9

where G1 is defined by F2 using t0 = t1 := x + y + ϕ and G2 using t0 = t2 := z.
Now by the basic inequality 2ab ≤ a2 + b2 and Cauchy-Schwartz inequality, for any
w0(ϱ) > 0 and w(ϱ) = e
−kλw0(ϱ) we derive from (2.14) that
∑

χ∈K
 ∑

ϱ∈Z(χ,H)
 ∑

ϱ′∈Z(χ,H) w(ϱ)w(ϱ
′)e
k λ+λ′

2 √(G1G2)(λ + λ′ − i(µ − µ′))

≤ ∑

χ∈K
 ∑

ϱ∈Z(χ,H) w(ϱ)
2ekλ ∑

ϱ′∈Z(χ,H)
 √(G1G2)(λ + λ′ − i(µ − µ′))

= ∑

χ∈K
 ∑

ϱ∈Z(χ,H) w(ϱ)w0(ϱ) ∑

ϱ′∈Z(χ,H)
 √(G1G2)(λ + λ′ − i(µ − µ′))

≤ max
ϱ w0(ϱ)√B(t1, λ, λ0)B(t2, λ, λ0) ∑

ϱ∈Z(K,H) w(ϱ).
 (3.7)

This means
∑

ϱ∈Z(K,H) w(ϱ) ≤ 1 + ε
xz
 ( 1
2 + ϕ + x
y
 ) max
ϱ w0(ϱ)
√B(t1, λ, λ0)B(t2, λ, λ0). (3.8)

Let w0(ϱ) = e
− (t1+t2) max{Λ−λ,0}
2 . By Lemma 2.3, we have

w0(ϱ)√
B(t1, λ, λ0)B(t2, λ, λ0) ≤ √B(t1, Λ, λ0)B(t2, Λ, λ0) (3.9)

This implies ∑

ϱ∈Z(K,H) w(ϱ) ≤ (1 + ε)C(x, y, z, Λ, λ0). (3.10)

Note that when λ ≤ Λ,
 w(ϱ) = e
−kλ− t1 +t2
2 max{Λ−λ,0}

≥ min{e
− t1+t2
2 Λ, e
−kλ}

≥ min{e
−2(3x+y+z+ϕ), e
−kλ}

≥ e
−kΛ
 (3.11)

which concludes the proof. □

From this result it is easy to derive estimates for N (Λ) (in this section N (Λ) is
restricted to the set K), that is,

N (Λ) ≤ C(x, y, z, Λ, λ0)ekΛ. (3.12)

For example, by λ0 = 1/2, x = 1/12, y = 1/4 and z = 1/6 we have

N (Λ) ≤ 19.62e 8
3 Λ, Λ ≥ 1.311. (3.13)

This improves the corresponding result of [13], where the coefficient is 22.281. To
make full use of this estimate, for any Λ ∈ [c0, H] we separate S into two parts,
that is, T = T (Λ) = ∑

j≥1 e− 10
3 max{λj ,Λ}, R = R(Λ) = S − T (Λ). (3.14)

10 GENHENG ZHAO

Then for q ≥ q(k, ε) and k ∈ [0, 10/3], we have by Lemma 3.1 that

T (Λ) ≤ (1 + ε)e
−( 10
3 −k)ΛC(x, y, z, Λ, λ0). (3.15)

Choosing optimal parameters for each given Λ and λ0 will give desired bounds of
T (Λ) in the general case. When M = O(1), T (Λ) can be estimated by a more
efficient way. In this case we will only apply (3.15) with λ0 = 0 and Λ ≥ 5.2 to
obtain the following result.

Corollary 3.2. Let q be sufficiently large and M = O(1). For Λ ≥ 5.2, we have

T (Λ) ≤ 100e−2.22Λ ≤ 0.001. (3.16)

Proof. Since C(x, y, z, Λ, 0) decreases as Λ increases, it follows that for Λ ≥ 5.2,

T (Λ) ≤ (1 + ε)e
−( 10
3 −k)ΛC(x, y, z, 5.2, 0). (3.17)

When q is sufficiently large, the choice

x = 0.029, y = 0.083, z = 0.052 (3.18)

gives
 C(x, y, z, 5.2, 0) ≤ 99.728 · · · , 10
3 − k = 2.226 · · · , (3.19)

which immediately implies (3.16). Meanwhile, we see

T (5.2) ≤ 100e−2.22·5.2 = 0.00096 · · · . (3.20)

□

When M = O(1) and Λ ≤ 5.2, the above estimate shows that the terms for
which λj ≥ 5.2 in T (Λ) are negligible. As for the terms λj ∈ [Λ, 5.2], we can bound
them by the new zero density estimate of Heath-Brown, which is generalized to our
setting by Pintz.
Let G(z) be the Laplace transform of

g(u) = 1
30 (2 − u)3(4 + 6u + u
2), u ∈ [0, 2], (3.21)

that is,
 G(z) = ∫ 2

0 g(u)e
−uzdu. (3.22)

For x > 0, let fx(u) := x · g(ux) whose Laplace transform is denoted by Fx(z) =
G(z/x). Define for j ≥ 1,

ψj = Fx(λj − λ0)
Fx(−λ0) , ψ = Fx(Λ − λ0)
Fx(−λ0) , ξ = ϕ
2 fx(0)
Fx(−λ0) , ∆ = ψ − ξ.

Let D = D(Λ) = ∑

j≥1
λj ≤Λ

(ψj − ψ). (3.23)

The following two basic inequalities based on these quantities are essentially estab-
lished in [13].

THE EXCEPTIONAL SET OF GOLDBACH PROBLEM AND LINNIK’S CONSTANT 11

Lemma 3.3. With the notations above and any ε > 0, we have for q ≥ q(ε) that

(∆2 − ξ − ε)N + 2∆D ≤ 1 − ξ (3.24)

provided x ≥ 4λ0/5 and ∆ ≥ √ξ + ε. When M = O(1), we have instead

(∆2 − ε)N + 2∆D ≤ 1 (3.25)

provided x ≥ 4λ0/5 and ∆ ≥ √ε.

Proof. The inequality (3.24) is exactly [13, Equation (8.3)]. The inequality (3.25)
can be derived in a similar way from [13, Equation (7.29)]. □

We first utilize this to continue the estimate of T (Λ) provided M = O(1). Note
that by (3.25) we have
 N ≤ 1
∆2 − ε , (3.26)

which is exactly [13, Theorem I]. Let Λ = Λ0 ≤ Λ1 ≤ · · · ≤ Λ200 = 5.2 be equally
distributed. For each Λi, we apply (3.26) to obtain a Ni with x = xi being chosen
optimally. Recall that T (5.2) ≤ 0.001, it follows

T (Λ) ≤ e− 10
3 Λ0N0 +
 200∑

i=1(Ni − Ni−1)e
− 10
3 Λi−1 + 0.001. (3.27)

Until now we have introduced all methods estimating T (Λ). As for the estimate
of
 R(Λ) = ∑

j≥1
λj ≤Λ

(e
− 10
3 λj − e− 10
3 Λ), (3.28)

we will basically follow the treatment of [13] to relate it to the sum

D(Λ) = ∑

j≥1
λj ≤Λ

(ψj − ψ). (3.29)

In the sequel we will always assume that N (Λ) ≥ 3, otherwise bounds from trivial
methods would be better. Meanwhile, we will preassign the values of λ1, λ2, and a
lower bound λ3 ≥ λ
∗. Hence λ0 = λ1 and we can write

R(Λ) =
 2∑

j=1(e− 10
3 λj − e− 10
3 Λ) + ∑

j≥3
λj ≤Λ

(e
− 10
3 λj − e− 10
3 Λ). (3.30)

Since the function eau − 1
ebu − 1 , (b ≥ a), (3.31)

decreases as u increases, when x ≥ 3/5 we see that

ψj − ψ
eK(Λ−λj ) − 1 = 1
Fx(−λ0)
 ∫ 2/x

0 Fx(u)e
−u(Λ−λ0) eu(Λ−λj ) − 1

e 10
3 (Λ−λj ) − 1 du (3.32)

12 GENHENG ZHAO

increases as λj increases. Hence by our labelling of λj,

∑

j≥3
λj ≤Λ

(e
− 10
3 λj − e− 10
3 Λ) ≤ e− 10
3 λ
∗ − e− 10
3 Λ

ψ∗ − ψ
 ∑

j≥3
λj ≤Λ

(ψj − ψ), (3.33)

where
 ψ∗ = Fx(λ∗ − λ0)
Fx(−λ0) . (3.34)

Recall that by Lemma 3.3 we have

N (∆2 − ξ − ε) + 2∆D ≤ 1 − ξ. (3.35)

To make full use of this inequality, for any given λ0 we will choose Λ to be as large
as possible such that there exists x ≥ max{4λ0/5, 3/5} for which ∆2 > ξ. Hence
∆2 ≈ ξ and with minor loss we obtain

D ≤ 1 − ξ
2∆ , (3.36)

which is exactly [13, Theorem J]. The desired pairs of λ0 and Λ in our argument
are 



λ0 = 0.60, Λ = 1.348,

λ0 = 0.62, Λ = 1.355,

λ0 = 0.64, Λ = 1.363,

λ0 = 0.66, Λ = 1.370,

λ0 = 0.68, Λ = 1.378,

λ0 = 0.92, Λ = 1.467.
 (3.37)

Gathering these inequalities, we finally arrive at

R(Λ) ≤
 2∑

j=1(e− 10
3 λj − e− 10
3 Λ) + e− 10
3 λ∗ − e− 10
3 Λ

ψ∗ − ψ
 

 1 − ξ
2∆ −
 2∑

j=1(ψj − ψ)


 , (3.38)

provided x ≥ max{4λ0/5, 3/5}, ∆ > √ξ and q sufficiently large. Since we require
x ≥ 3/5, by [13, Theorem K] the above bound is still valid when λ1 and λ2 get
larger than the preassigned values.
The next refinement comes when estimating R(Λ) for M = O(1). Recall in this
case we have
 (∆
2 − ε)N + 2∆D ≤ 1. (3.39)

If we argue as before, it would follow

D ≤ 1
2∆ , (3.40)

which is actually worse than (3.36) since we lose a −ξ in the numerator. The key
observation is that, by our setting of Λ, we have ∆2 ≈ ξ and thus an additional

THE EXCEPTIONAL SET OF GOLDBACH PROBLEM AND LINNIK’S CONSTANT 13

assumption N ≥ N ∗ + 1 will imply, approximately, a better bound

D ≤ 1 − (N ∗ + 1)ξ
2∆ . (3.41)

The empirical choice of N ∗ will be 3 or 4. In this way, we have either N ≤ N ∗

which means

R(Λ) ≤
 2∑

j=1(e
− 10
3 λj − e− 10
3 Λ) + (N ∗ − 2)(e− 10
3 λ
∗ − e− 10
3 Λ) (3.42)

or

R(Λ) ≤
 2∑

j=1(e
− 10
3 λj −e
− 10
3 Λ)+ e− 10
3 λ
∗ − e− 10
3 Λ

ψ∗ − ψ
 

 1 − (N ∗ + 1)∆2

2∆ −
 2∑

j=1(ψj − ψ)


 .

(3.43)
Also, this bound is still valid for larger λ1 and λ2. Now we have introduced all
methods estimating R(Λ).
It remains to apply these estimates to prove Theorem 1.2.

4. Proof of theorem 1.2

We now roughly distinguish the following five cases

• λ1,1 ∈ [c0, 0.01]
• λ1,1 ∈ [0.01, 0.40]
• λ1,1 ∈ [0.40, 0.60]
• λ1,1 ∈ [0.60, 0.62]
• λ1,1 ∈ [0.62, H]

In different cases, we will choose different values of Λ to separate Si = Ti + Ri to
apply those estimates.
The case λ1,1 ∈ [c0, 0.01]: In this case we let Λ = max{5.68, 1.09 log λ
−1
1,1}.
Hence by Lemma 2.4 we have N (Λ) ≤ 1, which means

Ri =
 


e− 10
3 λ1,1 − e− 10
3 Λ, i = 1,

0, i ≥ 2. (4.1)

It follows that ∑

i≥1 S2
i ≤ e
−2· 10
3 ·λ1,1 + 2T1 + ∑

i≥1 T 2
i

≤ e
− 20
3 λ1,1 + max
i≥1 Ti
 

2 + ∑

i≥1 Ti


 . (4.2)

Since Λ ≥ 5.2, by Corollary 3.2 we have

max
i≥1 Ti ≤ 100e
−2.22Λ. (4.3)

14 GENHENG ZHAO

Meanwhile using (3.15) with λ0 = 0 and Λ = 5.68 we see
∑

i≥1 Ti ≤ 0.02. (4.4)

Thus ∑

i≥1 S2
i ≤ e
− 20
3 λ1,1 + 202e−2.22Λ. (4.5)

The critical value λ1,1 = e
− 5.68
1.09 gives the bound 0.965. Noticing that the right hand
side is strictly convex if λ1,1 ≤ e− 5.68
1.09 and decreasing if λ1,1 ≥ e− 5.68
1.09 , we conclude
that there exists c1 > 0 depending only on c0 such that
∑

i≥1 S2
i ≤ 1 − c1 (4.6)

as desired.
The case λ1,1 ∈ [0.01, 0.40]: We now further distinguish three cases: λ1,1 ∈
[0.01, 0.10], λ1,1 ∈ [0.10, 0.30] and λ1,1 ∈ [0.30, 0.40]. However, they will be treated
in a similar manner. Since our method takes its advantages when λ0 is large, it
suffices to treat the special case λ1,1 ∈ [0.30, 0.40].
Now by Lemma 2.4 we have N (1.29) = 1. Hence we may let Λ = 1.29 to obtain
∑

i≥1 S2
i ≤ (e
− 10
3 ·0.3 + T1)
2 + ∑

i≥2 T 2
i . (4.7)

Using (3.15) and (3.12), with λ0 = 0.30 for i = 1 and λ0 = 1.29 for i ≥ 2, we see

Ti ≤
 



0.1231, i = 1,

0.0971, i ≥ 2,
 ∑

i≥2 Ti ≤ 6.85, (4.8)

which means∑

i≥ S2
i ≤ (0.3679 + 0.1231)2 + 0.0971 · 6.85 = 0.9062 · · · . (4.9)

The case λ1,1 ∈ [0.40, 0.60]: From now on estimates of R(Λ) will get involved.
By Lemma 2.4, we have N (0.92) ≤ 2. So there exists i0 ≥ 1 such that λi,1 ≥ 0.92
holds for i > i0. Hence we may first consider
∑

i>i0 S2
i . (4.10)

Let Λ = 1.467, then we have
∑

i>i0 S2
i = ∑

i>i0(Ti + Ri)
2

= ∑

i>i0 R2
i + ∑

i≥i0 Ti (2Ri + Ti) . (4.11)

Using (3.15) and (3.12), with λ0 = 0.92 and Λ = 1.467, we see

max
i>i0 Ti ≤ 0.0704, ∑

i>i0 Ti ≤ 6.33. (4.12)

THE EXCEPTIONAL SET OF GOLDBACH PROBLEM AND LINNIK’S CONSTANT 15

Meanwhile, using (3.42), (3.43) and (3.41) with λ1 = λ2 = λ∗ = 0.92 and N ∗ = 4,
we have
 max
i>i0 Ri ≤ 0.157, ∑

i>i0 Ri ≤ 0.457. (4.13)

Hence ∑

i>i0 S2
i ≤ 0.157 · 0.557 + 0.0704 · (2 · 0.457 + 6.33) = 0.5817 · · · . (4.14)

On the other hand, for i ≤ i0 we always have the bound

Ti ≤ 0.0808 (4.15)

from (3.15) with λ0 = 0.40 and Λ = 1.467. But for Ri, the case i0 = 2 gives
λ1 = 0.40 and λ2 = λ
∗ = 0.92. So by (3.42) and (3.43) with N ∗ = 4 we have

R1, R2 ≤ 0.374, (4.16)

and hence ∑

i≤i0 S2
i ≤ 2(0.374 + 0.0808)2 = 0.4136 · · · . (4.17)

The case i0 = 1 gives λ1 = λ2 = 0.40 and λ∗ = 0.92, which means

R1 ≤ 0.556 (4.18)

and thus ∑

i≤i0 S2
i ≤ (0.556 + 0.0808)2 = 0.4055 · · · . (4.19)

In conclusion, we have ∑

i≥1 S2
i ≤ 0.995 · · · . (4.20)

The case λ1,1 ∈ [0.60, H]: We further distinguish four cases: λ1,1 ∈ [0.60, 0.62],
λ1,1 ∈ [0.62, 0.64], λ1,1 ∈ [0.64, 0.68] and λ1,1 ∈ [0.68, H].
When λ1,1 ∈ [0.60, 0.62], let Λ = 1.348. By Lemma 2.4, in this case we have
either N (0.85) ≤ 1 or N (0.91) ≤ 2. When N (0.91) ≤ 2, using (3.15) and (3.12)
with λ0 = 0.60 and Λ = 1.348 we have

max
i≥1 Ti ≤ 0.101, ∑

i≥1 Ti ≤ 7.63. (4.21)

And using (3.15) with λ0 = 0.91 we have

max
i≥3 Ti ≤ 0.0927. (4.22)

Meanwhile, using (3.42), (3.43) and (3.41) with λ1 = λ2 = 0.60, λ∗ = 0.91 and
N ∗ = 3, we obtain
 max
i≥1 Ri ≤ 0.300, ∑

i≥1 Ri ≤ 0.581. (4.23)

16 GENHENG ZHAO

Hence ∑

i≥1 S2
i = ∑

i≥1 R2
i + ∑

i≥1 Ti(2Ri + Ti)

≤0.3 · 0.581 + 0.0927 · (2 · 0.581 + 7.63)

+ 2 · (0.1001 − 0.0927)(2 · 0.3 + 0.1001)

=0.9996 · · · .
 (4.24)

The case N (0.85) ≤ 1 is a simple analogue to this. We can repeat this argument
for λ1,1 ∈ [0.62, 0.64]. But when λ1,1 ∈ [0.64, 0.66], λ1,1 ∈ [0.66, 0.68] and λ1,1 ∈
[0.68, H], we may use the fact
 max
i≥5 Ti (4.25)

has better estimate due to Lemma 2.4.
In all cases, we have shown that
∑

i≥1 S2
i ≤ 1 − c1 (4.26)

for some c1 > 0 depending only on c0, which completes the proof of Theorem 1.2.

References

[1] I. M. Vinogradov, Representation of an odd number as a sum of three prime numbers, Doklady
Akad. Nauk SSSR 15 (1937), 291–294 (Russian).
[2] G. H. Hardy, J. E. Littlewood, Some problems of ‘Partitito Numerorum’, V: A further contri-
bution to the study of Goldbach’s problem, Proc. London Math. Soc. (2) 22 (1924), 46–56.
[3] H. L. Montgomery, R. C. Vaughan, The exceptional set in Goldbach’s problem. Collection of
articles in memory of Juri˘i Vladimiroviˇc Linnik, Acta Arith. 27 (1975), 353–370.

[4] Linnik Yu. V., On the least prime in an arithmetic progression I. The basic theorem, Rec.
Math. (Mat. Sbornik) N.S. 15(57) (1944) 139-178.
[5] J. R. Chen, J. M. Liu, The exceptional set of Goldbach numbers III, Chinese Quart. J. Math.
4 (1989), 1–15.
[6] J. R. Chen, J. M. Liu, On the least prime in an arithmetical progression (III), (IV), Science
in China Ser. A 32 (1989) 654–673, 792–807.
[7] H. Z. Li, The exceptional set of Goldbach numbers II, Acta Arith. 92 (2000), no. 1, 71–88.

[8] W. C. Lu, Exceptional set of Goldbach number, J. Number Theory 130 (2010), no. 10,
2359–2392.
[9] Xylouris, T., ¨Uber die Linniksche Konstante, Diplomarbeit, Universit¨at Bonn, 2009, arXiv:
0906.2749v1
[10] J. A. Maynard, On the Brun-Titchmarsh theorem, Acta Arith. 157 (2013), no. 3, 249–296
[11] D. R. Heath-Brown, Zero-free regions for Dirichlet L-functions, and the least prime in an
arithmetic progression, Proc. London Math. Soc. (3) 64 (1992), no. 2, 265–338.

[12] J. Pintz, A new explicit formula in the additive theory of primes with applications I. The
explicit formula for the Goldbach problem and the generalized twin prime problem, Acta
Arith. 210 (2023), 53–94
[13] J. Pintz. A new explicit formula in the additive theory of primes with applications II. The
exceptional set in Goldbach’s problem, arXiv:1804.09084v2
[14] M. Jutila, On Linnik’s constant, Math. Scand. 41 (1975), 45–62.

THE EXCEPTIONAL SET OF GOLDBACH PROBLEM AND LINNIK’S CONSTANT 17

[15] H. Iwaniec and E. Kowalski, Analytic number theory, American Mathematical Society Col-
loquium Publications, 53, Amer. Math. Soc., Providence, RI, 2004

Email address: zhaogenheng@amss.ac.cn
