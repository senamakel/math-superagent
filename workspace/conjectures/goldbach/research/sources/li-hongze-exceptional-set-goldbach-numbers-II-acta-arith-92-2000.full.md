<!-- source: http://matwbn.icm.edu.pl/ksiazki/aa/aa92/aa9217.pdf | converted from PDF -->

ACTA ARITHMETICA
XCII.1 (2000)

The exceptional set of Goldbach numbers (II)

by

Hongze Li (Jinan)

1. Introduction. A positive number which is a sum of two odd primes
is called a Goldbach number . Let E(x) denote the number of even numbers
not exceeding x which cannot be written as a sum of two odd primes. Then
the Goldbach conjecture is equivalent to proving that

E(x) = 2 for every x ≥ 4.

E(x) is usually called the exceptional set of Goldbach numbers. In [8]
H. L. Montgomery and R. C. Vaughan proved that E(x) = O(x
1−∆) for
some positive constant ∆ > 0. In [3] Chen and Pan proved that one can
take ∆ > 0.01. In [6], we proved that E(x) = O(x
0.921). In this paper we
prove the following result.

Theorem. For suﬃciently large x,

E(x) = O(x0.914).

Throughout this paper, ε always denotes a suﬃciently small positive
number that may be diﬀerent at each occurrence. A is assumed to be suﬃ-
ciently large, A < Y , and D = Y 1+ε.

2. Some lemmas. Let A < q ≤ Y and χq be a non-principal character
mod q. Write α = 1 − λ/log D, and assume

(2.1) α ≤ σ ≤ 1, |t| ≤ D/q.

Let χ (mod q) and χ0 (mod q) be a character and a principal character
mod q, and L = log D.

1991 Mathematics Subject Classiﬁcation: 11P32, 11P55.
This work was supported by the National Natural Science Foundation of China (Grant
no 19671051).
 [71]

72 H. Z. Li

Lemma 1. Let χ be a non-principal character modulo q, and let φ = 3/8.
Then for any ε > 0 there exists a δ = δ(ε) > 0 such that

−ℜ L′

L (s, χ) ≤ − ∑

|1+it−ϱ|≤δ ℜ 1
s − ϱ + ( φ
2 + ε)
H

uniformly for
 1 + 1
H log H ≤ σ ≤ 1 + log H
H ,

providing that q is suﬃciently large; here H = log q(|t| + 2).

This is Lemma 2.4 of [5].

Lemma 2. Suppose Y is suﬃciently large. Then no function L(s, χ) with
χ primitive modulo q ≤ Y , except for a possible exceptional one only, has a
zero in the region
 σ ≥ 1 − 0.239
log Y , q(|t| + 1) ≤ Y 1+ε.

If the exceptional function exists, say L(s, ̃χ), then ̃χ must be a real primitive
character modulo ̃q ≤ Y , and L(s, ̃χ) has a real simple zero ̃β satisfying

1 − 0.239
log Y ≤ ̃β ≤ 1 − c
̃q10−8 .

This is Lemma 2.3 of [6].

For a real number a, let a
∗ = aL−1, and let ϱj = 1−λ∗
j +iγ∗
j , j = 1, 2, . . . ,
denote the non-trivial zeros of L(s, χ) in (2.1), with λj in increasing order.

Lemma 3. Suppose χ is a real non-principal character mod q ≤ Y , and
ϱ1 is real. Then λ2 > 0.8.

P r o o f. Apply Lemma 3.2 of [5].

When χ
2 = χ0 and ϱ1 is complex, or χ
3 = χ0, we follow Lemma 9.1 of
[4]. Let a, k, ε be positive constants, and let φ = 3/8, P (x) = x + x
2 + 2
3 x
3.
Then
(
k2 + 1
2
 ){P ( a + λ1
a
 ) − P ( a + λ1
a + λ2
 )} − 2kP (1) + (a + λ1)(ψ + ε) ≥ 0,

where
 ψ = φ
2
 (
k2 + 3k + 3
2
 )
,

providing that

k0(a + λ1)−3 + (a + λ2)−3 ≥ a
−3 with k0 = min (
k + 3
4k , 4k).

Taking a = 2.4, k = 0.88, we see that if λ1 ≤ 0.618, then λ2 > 0.618.

Exceptional set of Goldbach numbers 73

Now suppose χ does not have order 2 or 3. Let

(2.2) L−1 ∑

k ak (a + 0.239)
k

(k − 1)!
 ∞∑

n=1 Λ(n) ℜ
( χ(n)
ns
 )( log n
L
 )k−1 = Σ(s, χ).

Again we follow Lemma 9.1 of [4] with a, k, ε, φ and P (x) as above. Then
(
k2 + 1
2
 ){
P ( a + 0.239
a
 ) − P ( a + 0.239
a + λ2
 )}

−2kP ( a + 0.239
a + λ1
 ) + (a + 0.239)(ψ + ε) ≥ 0.

Taking a = 2.21, k = 0.89, we see that if λ1 ≤ 0.575, then λ2 > 0.575.
Now we consider λ3. Our starting point is the inequality

(2.3)
 3∏

j=1
(1 + ℜ(χ(n)n−iγ∗
j )) ≥ 0.

Let P (x) = ∑ akx
k = x + x
2 + 2
3 x
3 and

(2.4) L−1 ∑

k ak ak

(k − 1)!
 ∞∑

n=1 Λ(n) ℜ( χ(n)
ns
 )( log n
L
 )k−1 = Σ(s, χ).

Then

(2.5) Σ(σ, χ0) +
 3∑

j=1 Σ(σ + iγ∗
j , χ) + 1
2
 ∑

2 + 1
4
 ∑

3 ≥ 0,

with ∑
2 = ∑

1≤j<k≤3{Σ(σ + iγ∗
j + iγ∗
k, χ2) + Σ(σ + iγ∗
j − iγ∗
k, χ0)}

and ∑
3 = Σ(σ + iγ∗
1 + iγ∗
2 + iγ∗
3 , χ
3) + Σ(σ + iγ∗
1 + iγ∗
2 − iγ∗
3 , χ)

+ Σ(σ + iγ∗
1 − iγ∗
2 + iγ∗
3 , χ) + Σ(σ + iγ∗
1 − iγ∗
2 − iγ∗
3 , ̃χ).

Let s = σ + it, σ = 1 + aL−1. We now observe that

ℜ
(
P ( a
(s − ϱ)L
 )) ≥ 0

for all zeros ϱ, since ℜP (1/z) ≥ 0 for ℜz ≥ 1. Moreover, if |1 + it − ϱ| ≥ δ,
then
 ℜ(
P ( a
(s − ϱ)L
 )) = O(L−1).

Here we follow Lemma 8.3 of [4]. Thus

Σ(σ, χ0) ≤ P (1) + ε,

74 H. Z. Li

∑

1≤j<k≤3 Σ(σ + iγ∗
j − iγ∗
k, χ0) ≤ ∑

1≤j<k≤3 ℜ{
P ( a
a + i(γj − γk)
 )} + ε,

Σ(σ + iγ∗
1 , χ) ≤ − P ( a
a + λ1
 ) − ℜ
{
P ( a
a + λ2 + i(γ1 − γ2)
 )}

− ℜ
{
P ( a
a + λ3 + i(γ1 − γ3)
 )} + a
( φ
2 + ε)
,

Σ(σ + iγ∗
2 , χ) ≤ −P ( a
a + λ2
 ) − ℜ{
P ( a
a + λ3 + i(γ2 − γ3)
 )} + a
( φ
2 + ε)
,

Σ(σ + iγ∗
3 , χ) ≤ −P ( a
a + λ3
 ) + a
( φ
2 + ε
),

∑

1≤j<k≤3 Σ(σ + iγ∗
j − iγ∗
k, χ2) ≤ a( 3
2 φ + ε
)
,

Σ(σ + iγ∗
1 + iγ∗
2 − iγ∗
3 , χ) ≤ − ℜ{
P ( a
a + λ1 + i(γ2 − γ3)
 )}

− ℜ
{
P ( a
a + λ2 + i(γ1 − γ3)
 )} + a
( φ
2 +ε
),

Σ(σ + iγ∗
1 − iγ∗
2 + iγ∗
3 , χ) ≤ −ℜ{
P ( a
a + λ3 + i(γ1 − γ2)
 )} + a
( φ
2 + ε
),

Σ(σ + iγ∗
1 + iγ∗
2 + iγ∗
3 , χ
3) ≤ a(φ/2 + ε),
Σ(σ + iγ∗
1 − iγ∗
2 − iγ∗
3 , ̃χ) ≤ a(φ/2 + ε).

Hence

P (1) − P ( a
a + λ1
 ) − P ( a
a + λ2
 ) − P ( a
a + λ3
 ) + a
( 11
4 φ + ε)

+ 1
2 ℜ
{
P ( a
a + i(γ1 − γ2)
 ) − 2P ( a
a + λ2 + i(γ1 − γ2)
 )

− 1
2 P ( a
a + λ3 + i(γ1 − γ2)
 )}

+ 1
2 ℜ
{
P ( a
a + i(γ1 − γ3)
 ) − 2P ( a
a + λ3 + i(γ1 − γ3)
 )

− 1
2 P ( a
a + λ2 + i(γ1 − γ3)
 )}

+ 1
2 ℜ
{
P ( a
a + i(γ2 − γ3)
 ) − 2P ( a
a + λ3 + i(γ2 − γ3)
 )

− 1
2 P ( a
a + λ1 + i(γ2 − γ3)
 )} ≥ 0.

Exceptional set of Goldbach numbers 75

Providing that a
−3 ≤ 5
2 (a + λ3)
−3

we have

P (1) − P ( a
a + λ1
 ) − P ( a
a + λ2
 ) − P ( a
a + λ3
 ) + a
( 11
4 φ + ε) ≥ 0.

Taking a = 2, we have λ3 ≥ 0.68.

Lemma 4. Suppose χ is a non-principal character mod q ≤ Y , and
ϱ1, ϱ2, ϱ3 are the zeros of L(s, χ). Then

λ2 > 0.575, λ3 > 0.618.

Lemma 5. Suppose χ ̸= χ0 is a character mod q ≤ Y . Let n0, n1, n2
denote the numbers of zeros of L(s, χ) in the rectangles

R0 : 1 − L−1 ≤ σ ≤ 1, |t − t0| ≤ 5.8L−1,

R1 : 1 − 5L−1 ≤ σ ≤ 1, |t − t1| ≤ 23.4L−1,

R2 : 1 − λ+L−1 ≤ σ ≤ 1, |t − t2| ≤ 23.4L−1,

where t0, t1, t2 are real numbers satisfying |ti| ≤ T , and 5 < λ+ ≤ log log L.
Then n0 ≤ 3, n1 ≤ 10, n2 ≤ 0.2292(λ+ + 42.9).
P r o o f. It is well known that

− ζ ′

ζ (σ) − ℜ L′

L (s, χ) ≥ 0;

here σ = ℜs.
(i) We consider the rectangle R0. Let s = σ + it0, σ = 1 + 8.4L−1, and
denote by ϱ = 1−λ∗ +iγ the zero of L(s, χ) in R0, hence 0 ≤ λ ≤ 1, |γ −t0| ≤
5.8L−1, and

−ℜ 1
s − ϱ = −L 8.4 + λ
(8.4 + λ)2 + ((γ − t0)L)2 ≤ −L 9.4
9.42 + 5.82 .

By Lemma 1,
 −ℜ L′

L (s, χ) ≤ − ∑

|1+it0−ϱ|≤δ ℜ 1
s − ϱ + 0.18751L.

If |1 + it0 − ϱ| > δ then ℜ 1
s−ϱ = O(1). So

−ℜ L′

L (s, χ) ≤ L(
0.18751 − 9.4n0
9.42 + 5.82
 )
.

Since − ζ′

ζ (σ) ≤ 1
σ−1 + A, where A is an absolute constant, we have

9.4n0
9.42 + 5.82 ≤ 1
8.4 + 0.18752, n0 ≤ 3.

76 H. Z. Li

(ii) The rectangles R1 and R2 are treated as R0 in (i) but with σ =
1 + 24L−1. Thus n1 ≤ 10, n2 ≤ 0.2292(λ+ + 42.9).

3. The zero density estimate of the Dirichlet L-function near
the line σ = 1. Let A < q ≤ Y and χq be a non-principal character mod q.
Write α = 1 − λ/log D, and assume

(3.1) α ≤ σ ≤ 1, |t| ≤ D/q.

Let Sjq = {χq : L(s, χq) has only j zeros in the region (3.1)}. Suppose
A < q0 ≤ Y and deﬁne

N ∗
1 (α, Y ) = N ∗
1 (λ, Y ) = ∑

A<q≤Y
[q,q0]≤Dε(q,q0)
 ∑

j≥1
 ∑∗

χ∈Sjq j,(3.2)
 N ∗(α, Y ) = N ∗(λ, Y ) = ∑

A<q≤Y
 ∑

j≥1
 ∑∗

χ∈Sjq j,(3.3)

where ∑∗ indicates that the sum is over primitive characters. In this section
we will prove the following lemma which improves Lemma 2.1 of [6].

Lemma 6. Suppose A < q0 ≤ Y and 0 < λ ≤ ε log D. Then

N ∗
1 (α, Y ) = N ∗
1 (λ, Y ) ≤
 



 4.356C1(λ)e4.064λ, 0.517 < λ ≤ 0.575,
8.46C2(λ)e4.12λ, 0.575 < λ ≤ 0.618,
14.3C3(λ)e4.5λ, 0.618 < λ ≤ 1,
104.1C4(λ)e3.42λ, 1 < λ ≤ 5,
268.6e2.16λ, 5 < λ ≤ ε log D,

N ∗(α, Y ) = N ∗(λ, Y ) ≤
 



 3.632C5(λ)e5.2λ, 0.334 < λ ≤ 0.517,
4.338C6(λ)e4.82λ, 0.517 < λ ≤ 0.575,
10.42C7(λ)e4.5λ, 0.575 < λ ≤ 0.618,
14.91C8(λ)e5.2λ, 0.618 < λ ≤ 1,
104.8C9(λ)e4.16λ, 1 < λ ≤ 5,
279.7e2.9λ, 5 < λ ≤ ε log D,

where
 C1(λ) = λ−1(
1 − e
−4.064λ e2.808λ − e1.76λ

1.048λ
 )
,

C2(λ) = λ−1(
1 − e
−4.12λ e2.855λ − e1.78λ

1.075λ
 )
,

C3(λ) = λ−1(
1 − e
−4.5λ e3.198λ − e2.013λ

1.185λ
 )
,

C4(λ) = λ−1(
1 − e
−3.42λ e2.358λ − e1.64λ

0.718λ
 )
,

Exceptional set of Goldbach numbers 77

C5(λ) = λ−1(
1 − e
−5.2λ e3.866λ − e2.668λ

1.198λ
 )
,

C6(λ) = λ−1(
1 − e
−4.82λ e3.565λ − e2.51λ

1.055λ
 )
,

C7(λ) = λ−1(
1 − e
−4.5λ e3.32λ − e2.36λ

0.96λ
 )
,

C8(λ) = λ−1(
1 − e
−5.2λ e3.928λ − e2.7312λ

1.1968λ
 )
,

C9(λ) = λ−1(
1 − e
−4.16λ e3.104λ − e2.38λ

0.724λ
 )
.

P r o o f. We use the method of Section 3 of [7]. For 1 ≤ j ≤ 4, let hj
denote positive constants which satisfy

(3.4) h1 < h2 < h3, h2 + h4 + 3/8 < h3, 2h4 + 3/8 < h1

when we consider N ∗
1 (α, Y ), and

(3.5) h1 < h2 < h3, h2 + h4 + 3/8 < h3, 2h4 + 3/4 < h1

when we consider N ∗(α, Y ).
Let

(3.6) zj := Dhj , α := 1 − λL−1, λ ≤ εL.

For positive δ1, δ3, let

κ(s) := s−2{(e−(1−δ1)(log z1)s − e
−(log z1)s)δ3(log z3)(3.7) − (e
−(log z3)s − e−(1+δ3)(log z3)s)δ1(log z1)}.

For a zero ϱ0 ∈ D, let

(3.8) M (ϱ0) := ∑

ϱ(χ) |κ(ϱ(χ) + ϱ0 − 2α)|,

where the sum is over the zeros of L(s, χ) in (3.1). Then if 2h4 + 3/8 <
(1 − δ1)h1, then as in (3.17) of [7] we have

N ∗
1 (α, Y ) ≤ (1 + δ)maxϱ0 M (ϱ0)
2(1 − α)(h2 − h1)δ1δ3h1h3h4L4(3.9)
 × (
D2h3(1−α) − (2α − 1)(D2h2(1−α) − D2h1(1−α))
2(1 − α)(h2 − h1)L
 )

≤ (1 + δ)maxϱ0 M (ϱ0)
2λ(h2 − h1)δ1δ3h1h3h4L3
 (
e2h3λ − e
2h2λ − e2h1λ

2λ(h2 − h1)
 ).

78 H. Z. Li

If 2h4 + 3/4 < (1 − δ1)h1, then as in (3.17) of [7] we have

N ∗(α, Y ) ≤ (1 + δ)maxϱ0 M (ϱ0)
2(1 − α)(h2 − h1)δ1δ3h1h3h4L4(3.10)
 × (
D2h3(1−α) − (2α − 1)(D2h2(1−α) − D2h1(1−α))
2(1 − α)(h2 − h1)L
 )

≤ (1 + δ)maxϱ0 M (ϱ0)
2λ(h2 − h1)δ1δ3h1h3h4L3
 (
e2h3λ − e
2h2λ − e2h1λ

2λ(h2 − h1)
 ).

(i) If 5 < λ ≤ εL, let ∆ = 23.4L−1. As in [7], by Lemma 5 we have

M (ϱ0) ≤ 0.2292(λ + 42.9)L
3(1/2)

× {(δ1h1(2δ3 + δ2
3)h2
3 − δ3h3(2δ1 − δ2
1)h2
1)

+ (π/23.4)
2(δ1h1 + δ3h3)}.

Choose h1 = 0.58, h2 = 0.669, h3 = 1.08, h4 = 0.0353, δ1h1 = δ3h3 =
π/23.4. By (3.9) we have
 N ∗
1 (α, Y ) ≤ 268.6e2.16λ.

Choose h1 = 0.95, h2 = 1.042, h3 = 1.45, h4 = 0.0328, δ1h1 = δ3h3 =
π/23.4. By (3.10) we have
N ∗(α, Y ) ≤ 279.7e
2.9λ.

(ii) If 1 < λ ≤ 5, then as in [7], by Lemma 5 (n1 ≤ 10) we have

M (ϱ0) ≤ (10/2)L3

× {(δ1h1(2δ3 + δ2
3)h2
3 − δ3h3(2δ1 − δ2
1)h2
1)

+ (π/23.4)
2(δ1h1 + δ3h3)}.

Choose h1 = 0.82, h2 = 1.179, h3 = 1.71, h4 = 0.155, δ1h1 = δ3h3 = π/23.4.
By (3.9) we have
 N ∗
1 (α, Y ) ≤ 104.1C4(λ)e3.42λ.

Choose h1 = 1.19, h2 = 1.552, h3 = 2.08, h4 = 0.1528, δ1h1 = δ3h3 =
π/23.4. By (3.10) we have

N ∗(α, Y ) ≤ 104.8C9(λ)e4.16λ.

(iii) If 0.618 < λ ≤ 1, then as in [7], by Lemma 5 we have
( 1
a − 1
a + 1 − 2(a + 1)
(a + 1)2 + 5.82 + 0.1876)

× max { a + 1
5.82 + 1
a + 1 , a + 0.618
5.82 + 1
a + 0.618
 } ≤ 0.014621.

Exceptional set of Goldbach numbers 79

For a = 6.3,

M (ϱ0) ≤ {1.5(δ1h1(2δ3 + δ2
3)h2
3 − δ3h3(2δ1 − δ2
1)h2
1)

+ 2 · 0.014621 · (δ1h1 + δ3h3)}L3.

Choose h1 = 1.0065, h2 = 1.599, h3 = 2.25, h4 = 0.2759, δ1 = 0.079,
δ3 = 0.094. By (3.9) we have

N ∗
1 (α, Y ) ≤ 14.3C3(λ)e4.5λ.

Choose h1 = 1.3656, h2 = 1.964, h3 = 2.6, h4 = 0.26, δ1 = 0.07, δ3 = 0.094.
By (3.10) we have N ∗(α, Y ) ≤ 14.91C8(λ)e5.2λ.
(iv) If 0.575 < λ ≤ 0.618, then by Lemma 4 there are at most two zeros
satisfying ϱ = 1 − β/L − iγ/L, β < 0.618. Then, as in (v) of [7], when (3.4)
holds we have

N ∗
1 (α, Y ) ≤ (1 + δ) ̃M
2(1 − α)(h2 − h1)h4L2(3.11)
 × (
D2h3(1−α) − (2α − 1)(D2h2(1−α) − D2h1(1−α))
2(1 − α)(h2 − h1)L
 )

≤ (1 + δ) ̃M
2λ(h2 − h1)h4L
 (
e2h3λ − e
2h2λ − e2h1λ

2λ(h2 − h1)
 ).

Similarly, when (3.5) holds we have

(3.12) N ∗(α, Y ) ≤ (1 + δ) ̃M
2λ(h2 − h1)h4L
 (
e2h3λ − e2h2λ − e2h1λ

2λ(h2 − h1)
 )

where
 ̃M := max
χ mod q
q≤Y max
1≤j≤2 1
j
 log z3\

log z1
 ∣
∣
∣
 j∑

l=1 e−(ϱ(l,χ)−α)x∣
∣
∣2 dx.

We have log z3\

log z1 |e−(ϱ(χ)−α)x|2 dx ≤ (h3 − h1)L,

1
2
 log z3\

log z1
 ∣
∣
∣
 2∑

l=1 e−(ϱ(l,χ)−α)x∣
∣
∣2 dx ≤ 2(h3 − h1)L.

Choose h1 = 0.89, h2 = 1.4275, h3 = 2.06, h4 = 0.2574. By (3.11) we have

N ∗
1 (α, Y ) ≤ 8.46C2(λ)e4.12λ.

Choose h1 = 1.18, h2 = 1.66, h3 = 2.25, h4 = 0.214. By (3.12) we have

N ∗(α, Y ) ≤ 10.42C7(λ)e4.5λ.

80 H. Z. Li

(v) If 0.517 < λ ≤ 0.575, then by Lemma 4 there is at most one zero
satisfying ϱ = 1 − β/L − iγ/L, β < 0.575. Then, as in (v) of [7], when (3.4)
holds we have

N ∗
1 (α, Y ) ≤ (1 + δ)(h3 − h1)
2(1 − α)(h2 − h1)h4L
(3.13)
 × (
D2h3(1−α) − (2α − 1)(D2h2(1−α) − D2h1(1−α))
2(1 − α)(h2 − h1)L
 )

≤ (1 + δ)(h3 − h1)
2λ(h2 − h1)h4
 (
e2h3λ − e2h2λ − e
2h1λ

2λ(h2 − h1)
 )
.

When (3.5) holds we have

(3.14) N ∗(α, Y ) ≤ (1 + δ)(h3 − h1)
2λ(h2 − h1)h4
 (
e
2h3λ − e
2h2λ − e2h1λ

2λ(h2 − h1)
 ).

Choose h1 = 0.88, h2 = 1.404, h3 = 2.032, h4 = 0.2524. By (3.13) we have

N ∗
1 (α, Y ) ≤ 4.356C1(λ)e4.064λ.

Choose h1 = 1.255, h2 = 1.7825, h3 = 2.41, h4 = 0.2524. By (3.14) we have

N ∗(α, Y ) ≤ 4.338C6(λ)e4.82λ.

(vi) If 0.334 < λ ≤ 0.517, then as above, when (3.5) holds we have

(3.15) N ∗(α, Y ) ≤ (1 + δ)(h3 − h1)
2λ(h2 − h1)h4
 (
e
2h3λ − e
2h2λ − e2h1λ

2λ(h2 − h1)
 ).

Choose h1 = 1.334, h2 = 1.933, h3 = 2.6, h4 = 0.291. By (3.15) we have

N ∗(α, Y ) ≤ 3.632C5(λ)e5.2λ.

If q1, q2 ≤ Y , we consider the zeros of L(s, χq1) and L(s, χq2) for non-
principal characters χq1 and χq2. If ϱ1 = β1 + iγ1 = 1 − λ1/log Y + iγ1
is a zero of L(s, χq1) satisfying q1(|γ1| + 1) ≤ Y 1+ε and ϱ2 = β2 + iγ2 =
1 − λ2/log Y + iγ2 is a zero of L(s, χq2) satisfying q2(|γ2| + 1) ≤ Y 1+ε, then
we have the lower bounds for λ2 given in Table 1. If [q1, q2] ≤ Y ε(q1, q2),
then we have the lower bounds for λ2 given in Table 2.

Table 1. The lower bounds for λ2

λ1 λ2
0.24 0.444
0.26 0.418
0.28 0.393
0.30 0.37
0.32 0.349
0.334 0.334
 Table 2. The lower bounds for λ2

λ1 λ2 λ1 λ2
0.22 1.189 0.38 0.745
0.24 1.116 0.40 0.706
0.26 1.050 0.42 0.669
0.28 0.989 0.44 0.634
0.30 0.933 0.46 0.601
0.32 0.881 0.48 0.570
0.34 0.832 0.50 0.541
0.36 0.787 0.517 0.517

Exceptional set of Goldbach numbers 81

In each table, following the convention of [6], the entries indicate that
if λ1 does not exceed the ﬁrst entry, then λ2 is no smaller than the second
entry.

4. The circle method. Suppose x is a suﬃciently large positive number,
and Y = x
λ where λ = 0.0862. Let

S(α) = ∑

Y <p≤x log p e(αp), D(n) = D(n; x, Y ) = ∑

n=p1+p2
Y <p1,p2≤x
 log p1 log p2.

Then

(4.1) D(n) =
 1\

0 S2(α)e(−αn) dα.

Trivially, D(n) = 0 if n ≤ 2Y or n > 2x, and n is a Goldbach number if
D(n) > 0.
Let Q = x
1−λ, τ = Q
−1 and

E1 = ⋃

1≤q≤Y
 ⋃

1≤a≤q
(a,q)=1
 I(a, q), E2 = (−τ, 1 − τ ] \ E1

where
 I(a, q) = [ a
q − 1
qQ , a
q + 1
qQ
 ].

Then
 D(n) =
 1−τ\

−τ S2(α)e(−αn) dα(4.2)
 = \

E1 S2(α)e(−αn) dα + \

E2 S2(α)e(−αn) dα

= D1(n) + D2(n).

Lemma 7. Let M (x) denote the number of integers n ∈ [(1 − ε)x, x] for
which
 |D2(n)| > 0.5x
1−10−5λ.

Then
 M (x) ≪ x
1−(1−10−4)λ.

P r o o f. Apply Lemma 8 of [3].

Now we consider the integral on the major arcs. For α ∈ I(a, q) ⊂ E1, we
write α = a/q +θ, (a, q) = 1, q ≤ Y , |θ| ≤ 1/(qQ). Moreover, suppose that ̃q,
̃χ and ̃β are the possible modulus, primitive character and zero respectively,

82 H. Z. Li

with ̃q ≤ Y . Let
 T (θ) = ∑

Y <m≤x e(mθ),(4.3)
 ̃T (θ) = − ∑

Y <m≤x m ̃β−1e(mθ),(4.4)
 ̂S(θ, χ) = ∑

Y <p≤x χ(p) log p e(pθ),(4.5)

χ being a character modulo q, q ≤ Y , and

(4.6)
 



 ̂S(θ, χ0
q) = T (θ) + W (θ, χ0
q),

̂S(θ, χ0
q ̃χ) = ̃T (θ) + W (θ, χ0
q ̃χ) if ̃q | q,

̂S(θ, χq) = W (θ, χq) otherwise.

Then if the exceptional character exists we have

(4.7) D1(n) = ∑

q≤Y
 ∑

a≤q
(a,q)=1
 a/q+1/(qQ)\

a/q−1/(qQ) S2(α)e(−αn) dα =
 6∑

j=1 D1j(n).

Otherwise we have

(4.8) D1(n) =
 3∑

j=1 D1j(n).

For the deﬁnitions of D1j(n), see [3]. By the method of [8] one has

D11(n) = nC(n) + O(x1+εY −1),(4.9)
 D14(n) = ̃C(n)̃I(n) + O((n, ̃q)x
1+εY −1),(4.10)

where
 C(n) =
 ∞∑

q=1
 µ
2(q)
φ2(q) Cq(−n) = n
φ(n)
 ∏

p∤n
 (1 − 1
(p − 1)2
 )
,(4.11)
 ̃C(n) =
 ∞∑

q=1
̃q|q
 τ 2(χ
0
q ̃χ)
φ2(q) Cq(−n) = ̃χ(−1)µ
( ̃q
(̃q, n)
 ) ∏

p|̃q
p∤n
 ( 1
p − 2
 )
C(n),(4.12)
 ̃I(n) = ∑

Y <m≤n−Y (m(n − m)) ̃β−1 ≤ x
(1−ε)( ̃β−1)n ̃β,(4.13)

with
 τ (χ) =
 q∑

h=1 χ(h)e( h
q
 )
, Cq(m) = ∑

h≤q
(h,q)=1
 e( mh
q
 )
.

Exceptional set of Goldbach numbers 83

Let

(4.14) W (χd) = ( 1/(dQ)\

−1/(dQ) |W (θ, χd)|2 dθ)1/2.

Then by (20) of [3] one has

(4.15) D12(n) ≤ n
φ(n)
 {
8x
1/2W (log10 x) + O( x1/2W (Y )
log6 x
 )}
,

where

(4.16) W (Y ) = ∑

d≤Y
 ∑∗

χd W (χd),

the ∗ denoting that the sum is over primitive characters χd. We have

(4.17) D15(n) ≪ ̃χ2(n) ̃q
φ2(̃q) · n
φ(n) x.

From ∏
p≥5(1 + 1/(p − 1)
2) ≤ 1.132, by the method of [1], we have

D16(n) ≤ 4.1594 n
φ(n) x
1/2W (Y, ̃q) + n
φ(n) W (Y )x
(1−ε)/2,(4.18)
 D13(n) ≤ 2.0797 n
φ(n) W (Y )W ′(Y ),(4.19)

where
 W (Y, ̃q) = ∑

d≤Y
[d,̃q]≤xε(d,̃q)
 ∑∗

χd W (χd),(4.20)
 W ′(Y ) = max ∑

d≤Y
[d1,d]≤xε(d1,d)
 ∑∗

χd W (χd).(4.21)

Here the max is over A < d1 ≤ Y .

5. The estimation of W ′(Y ), W (Y ) and W (Y, ̃q). By Section III of [2]
we have

W (χd) ≤ (1 + 2 · 10−5)x1/2 ∑′

β≥1/4
|γχd |≤Y 1+εd
−1
 x
(1−ε)(β−1)(5.1)
 + O(x1/2−ε ∑′

β≥1/4
|γχd |≤Y 1.01d
−1
 x
β−1)

+ O(x1/2−0.01λ ∑′

β≥1/4
|γχd |≤Y 2.01
 x
β−1) + O(x
1/2−1.01λ+εd−1),

84 H. Z. Li

where ∑′ indicates that the sum does not contain the exceptional zero ̃β.
By the same methods as in [1] we have

(5.2)
 ∑

d≤Y
[d1,d]≤Y ε(d1,d)
 ∑∗

χd
 ∑′

β≥1/4
|γχd |≤Y 2.01
 x
β−1 ≪ x
0.7ε,

∑

d≤Y
 ∑∗

χd
 ∑′

β≥1/4
|γχd |≤Y 2.01
 x
β−1 ≪ x
0.7ε.

Let

(5.3)
 I1 = ∑

d≤Y
[d1,d]≤Y ε(d1,d)
 ∑∗

χd
 ∑′

β≥1/4
|γχd |≤Y 1+εd−1
 x
(1−ε)(β−1),

I2 = ∑

d≤Y
 ∑∗

χd
 ∑′

β≥1/4
|γχd |≤Y 1+εd
−1
 x
(1−ε)(β−1).

Suppose ϱχd = βχd + iγχd , |γχd | ≤ Y 1+εd−1, is a zero of L(s, χd). Let
L = (1 + ε) log Y .

1) If 1 − 0.24/L ≤ βχd ≤ 1 − 0.239/L, then by Lemma 6 and Tables 1
and 2 we have

I1 ≤ 2e−0.239/(λ+ε) + 1
λ + ε
 ∞\

1.116 e−(1−ε)t/(λ+ε)N ∗
1 (t, Y ) dt ≤ 0.136,

I2 ≤ 2e−0.239/(λ+ε) + 1
λ + ε
 ∞\

0.444 e−(1−ε)t/(λ+ε)N ∗(t, Y ) dt ≤ 1.009.

2) If 1 − 0.26/L ≤ βχd ≤ 1 − 0.24/L, we have I1 ≤ 0.143, I2 ≤ 1.098.
3) If 1 − 0.28/L ≤ βχd ≤ 1 − 0.26/L, we have I1 ≤ 0.129, I2 ≤ 1.177.
4) If 1 − 0.30/L ≤ βχd ≤ 1 − 0.28/L, we have I1 ≤ 0.118, I2 ≤ 1.271.
5) If 1 − 0.32/L ≤ βχd ≤ 1 − 0.30/L, we have I1 ≤ 0.114, I2 ≤ 1.377.
6) If 1 − 0.34/L ≤ βχd ≤ 1 − 0.32/L, we have I1 ≤ 0.118, I2 ≤ 1.464.
7) If 1 − 0.36/L ≤ βχd ≤ 1 − 0.34/L, we have I1 ≤ 0.131, I2 ≤ 1.374.
8) If 1 − 0.38/L ≤ βχd ≤ 1 − 0.36/L, we have I1 ≤ 0.153, I2 ≤ 1.249.
9) If 1 − 0.40/L ≤ βχd ≤ 1 − 0.38/L, we have I1 ≤ 0.185, I2 ≤ 1.141.
10) If 1 − 0.42/L ≤ βχd ≤ 1 − 0.40/L, we have I1 ≤ 0.229, I2 ≤ 1.047.
11) If 1 − 0.44/L ≤ βχd ≤ 1 − 0.42/L, we have I1 ≤ 0.287, I2 ≤ 0.967.
12) If 1 − 0.46/L ≤ βχd ≤ 1 − 0.44/L, we have I1 ≤ 0.337, I2 ≤ 0.897.
13) If 1 − 0.48/L ≤ βχd ≤ 1 − 0.46/L, we have I1 ≤ 0.372, I2 ≤ 0.835.
14) If 1 − 0.50/L ≤ βχd ≤ 1 − 0.48/L, we have I1 ≤ 0.395, I2 ≤ 0.784.
15) If 1 − 0.517/L ≤ βχd ≤ 1 − 0.50/L, we have I1 ≤ 0.420, I2 ≤ 0.738.
16) If 1 − 0.517/L ≥ βχd , we have I1 ≤ 0.414, I2 ≤ 0.704.

Exceptional set of Goldbach numbers 85

Hence in all cases we have

(5.4) I1I2 ≤ 0.311.

Lemma 8. Let χ1 be a real non-principal character mod q, β1 = 1 − δ1 a
real zero of L(s, χ1), χ a character mod q, and ϱ = β + iγ = 1 − δ + iγ a zero
of L(s, χ) with δ < 1/6, β ≤ β1. Suppose that D = q(|γ| + 1) is suﬃciently
large, that is, D ≥ D0(ε). Then

δ1 ≥ (2/3 − ε)(1 − 6δ)D−(3/2+ε)δ/(1−6δ)/log D.

This is Theorem 2 of [9].

Lemma 9. If the exceptional primitive real character ̃χ (mod ̃q) exists,
and the unique exceptional zero ̃β of L(s, ̃χ) satisﬁes ̃δ(λ + ε) log x ≤ 0.239
where ̃δ = 1 − ̃β, let χq be a primitive character mod q, and ϱ = β + iγ =
1 − δ + iγ a zero of L(s, χq) with 0 < δ < ε. Suppose that D1 = [q, ̃q](|γ| + 1)
is suﬃciently large, that is, D1 ≥ D1(ε). Then

̃δ ≥ (2/3 − ε)(1 − 6δ)D−(3/2+ε)δ/(1−6δ)
1 /log D1.

P r o o f. This follows by Lemma 8 and the method of Lemma 15 of [1].

By (26) of [1] we have

(5.5) W ((log x)
10) ≤ 10−10x
1/2.

By (5.1)–(5.4) and deﬁnitions of W (Y ) and W ′(Y ) we have

(5.6) W (Y )W ′(Y ) ≤ 0.311x.

Now we suppose that the exceptional primitive real character ̃χ (mod ̃q)
exists, and the unique exceptional real zero ̃β of L(s, ̃χ) satisﬁes
̃δ(λ + ε) log x ≤ 0.239 where ̃δ = 1 − ̃β. In this case, as above we have

(5.7) W (Y, ̃q) ≤ W ′(Y ) ≤ 0.0107x
1/2, W (Y ) ≤ 0.884x1/2.

Hence we have

(5.8) W (Y )W ′(Y ) ≤ 0.0095x.

We suppose, as we may, that ̃q ≤ Y , q ≤ Y , [q, ̃q] ≤ x
ε(q, ̃q) and |γ| ≤
Y 1+εq−1, and then we may take D1 = x
λ+2ε in Lemma 9. Therefore if
̃δ(λ + ε) log x ≤ 0.005 and δ ≤ ε, then we have

(5.9) δ ≥ 3.26
λ log x .

If ̃δ(λ + ε) log x ≥ 0.005, ̃δ ≥ (2/3 − ε)(D1.501ε
1 log D1)−1, δ ≤ ε, then as
above, by Lemma 9 one has

(5.10) δ ≥ − log(1.501̃δ log D1)
1.501 log D1 .

86 H. Z. Li

By Lemma 6 we have

(5.11) ∑

d≤Y
[d1,d]≤Y ε(d1,d)
 ∑∗

χd
 ∑′

β≥1/4
|γχd |≤Y 1.01d
−1
 x
(1−ε)(β−1)

≤ 1
λ + ε
 ∞\

−(log(1.501̃δ log D1))/1.501 e−(1−ε)t/(λ+ε)N ∗
1 (t, Y ) dt + O(x−ε)

≤ 10−8(̃δ log x) + O(x
−ε).

Hence
(5.12) W ′(Y ) ≤ 10−8(̃δ log x)x1/2 + O(x
1/2−ε).

Similarly we have

(5.13) W ((log x)
10), W (Y, ̃q) ≤ 10−8(̃δ log x)x
1/2 + O(x1/2−ε).

If x
−λ/105 ≤ ̃δ ≤ (2/3 − ε)(D1.501ε
1 log D1)−1, then as above, by Lemma 9
one has
(5.14) W ((log x)
10), W (Y, ̃q), W ′(Y ) ≤ ε(̃δ log x)x
1/2 + O(x
1/2−0.01).

6. Proof of the Theorem. First of all, we suppose that there is no
exceptional character. When (1 − ε)x ≤ n ≤ x, by (4.8), (4.9), (4.15) and
(4.19) we have

D1(n) ≥ nC(n) − n
φ(n)
 {
8x1/2W ((log x)
10)

+ 2.0797W (Y )W ′(Y ) + O( x
1/2W (Y )
(log x)6
 )} + O(x
1−λ+ε).

Since λ = 0.0862, ∏
p≥3(1 − 1/(p − 1)2) ≥ 0.6601, by (5.5) and (5.6) it
follows that

D1(n) ≥ nx
φ(n)
 { ∏

p≥3
 (1 − 1
(p − 1)2
 ) − 2.0797 · 0.311 − 10−9} ≥ 0.01x,

which proves the assertion.
Now we suppose the exceptional character occurs, and (1 − ε)x ≤ n ≤ x.
By Section 4 we have
D1(n) ≥ nC(n) + ̃I(n) ̃C(n)(6.1)
 − n
φ(n) {8x1/2W ((log x)
10) + 2.0797W (Y )W ′(Y )

+ 4.1594W (Y, ̃q) + W (Y )x
(1−ε)/2}

+ O( x1/2W (Y )
(log x)6
 ) + O(̃χ2(n) ̃q
φ2(̃q) · n
φ(n) x)

+ O(x
1−λ+ε(n, ̃q)).

Exceptional set of Goldbach numbers 87

1) When (n, ̃q) = 1 or (n, ̃q) ≤ x
(1−10−4)λ and ∏
p|̃q, p∤n(p − 2) ≥ 1/ε we
follow the argument of [1]. Thus by (5.7) and (5.8) we have

(6.2) D1(n) ≥ n
φ(n)
 {
x ∏

p≥3
 (1 − 1
(p − 1)2
 ) − 2.0797W (Y )W ′(Y ) − 10−8x

− 4.1594W (Y, ̃q)x
1/2} ≥ 0.59x.

2) When (n, ̃q) > x(1−10−4)λ we have

(6.3) ∑

n≤x

(n,̃q)>x(1−10−4 )λ
 1 ≤ x1−(1−10−4)λ+ε.

3) When 1 < (n, ̃q) ≤ x
(1−10−4)λ and ∏
p|̃q, p∤n(p − 2) ≤ 1/ε, we no-
tice that ̃χ(n) = 0, and from Lemma 5.1 of [8] we have µ(̃q/(4, ̃q)) = 0
hence 16 ∤ ̃q, p2 ∤ ̃q (p ≥ 3). Since ∏
p|̃q, p∤n(p − 2) ≤ 1/ε, there exists ̃q ≤

16(n, ̃q)/ε2 ≤ x
(1−10−4)λ+ε. By (4.12) and (4.13) we have

(6.4) nC(n) − |̃I(n) ̃C(n)| ≥ (n − x
(1−ε)( ̃β−1)n ̃β)C(n).

When 1 − 0.239
(λ+ε) log x ≤ ̃β ≤ 1 − 0.005
(λ+ε) log x , we have

x
(1−ε)( ̃β−1)n ̃β ≤ 0.8905n.

By (5.7) and (5.8) we have

(6.5) D1(n) ≥ nx
φ(n)
 {
0.1095 ∏

p≥3
 (
1 − 1
(p − 1)2
 ) − 2.0797 · 0.0095

−10−8 − 4.1594 · 0.0107} ≥ 0.007x.

When 1 − 0.005
(λ+ε) log x ≤ ̃β ≤ 1 − ( 2
3 − ε
) x−1.501ελ
λ log x , as in (48) of [1] we have

nC(n) − |̃I(n) ̃C(n)| ≥ 0.62 ̃δnx log n
φ(n) .

By (5.12) and (5.13) we have

D1(n) ≥ ̃δnx log n
φ(n) {0.62 − 2.0797 · 10−7 − (8 + 4.1594) · 10−8}(6.6)
 ≥ 0.6x
1−ε.

When ̃β ≥ 1 − ( 2
3 − ε
) x−1.501ελ
λ log x , by ̃q ≤ x
λ and Lemma 2 we have

x
−10−5λ ≤ ̃δ ≤ ( 2
3 − ε
) x
−1.501ελ

λ log x ,

88 H. Z. Li

and by (5.14) we have

(6.7) D1(n) ≥ ̃δnx log n
φ(n) {0.62 − 20ε} ≥ 0.6x
1−10−5λ.

By (6.1)–(6.7) and Lemma 7 the assertion follows.

References

[1] J. R. C h e n, The exceptional set of Goldbach numbers (II ), Sci. Sinica 26 (1983),
714–731.
[2] J. R. C h e n and J. M. L i u, The exceptional set of Goldbach numbers (III ), Chinese
Quart. J. Math. 4 (1989), 1–15.
[3] J. R. C h e n and C. D. P a n, The exceptional set of Goldbach numbers, Sci. Sinica 23
(1980), 416–430.
[4] D. R. H e a t h - B r o w n, Zero-free regions for Dirichlet L-functions, and the least
prime in an arithmetic progression, Proc. London Math. Soc. (3) 64 (1992), 265–338.
[5] H. Z. L i, Zero-free regions for Dirichlet L-functions, Quart. J. Math. Oxford Ser. (2)
50 (1999), 13–23.
[6] —, The exceptional set of Goldbach numbers, ibid. 50 (1999).
[7] J. Y. L i u, M. C. L i u and T. Z. W a n g, The number of powers of 2 in a representation
of large even integers (II ), Sci. China Ser. A 41 (1998), 1255–1271.
[8] H. L. M o n t g o m e r y and R. C. V a u g h a n, The exceptional set in Goldbach’s prob-
lem, Acta Arith. 27 (1975), 353–370.
[9] W. W a n g, On zero distribution of Dirichlet’s L-functions, J. Shandong Univ. 21
(1986), 1–13 (in Chinese).

Department of Mathematics
Shandong University
Jinan Shandong
P.R. China
E-mail: lihz@sdu.edu.cn
 Received on 13.11.1998 (3508)
