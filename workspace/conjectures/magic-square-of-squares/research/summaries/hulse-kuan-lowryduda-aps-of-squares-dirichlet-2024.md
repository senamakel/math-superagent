> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/hulse-kuan-lowryduda-aps-of-squares-dirichlet-2024.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2007.14324 | converted from PDF -->

## What it claims

Abstract. We study a Dirichlet series in two variables which counts
primitive three-term arithmetic progressions of squares. We show that
this multiple Dirichlet series has meromorphic continuation to C2 and
use Tauberian methods to obtain counts for arithmetic progressions of
squares and rational points on x2 + y2 = 2.

1. Introduction

In this paper, we produce estimates for the number of primitive three-
term arithmetic progressions of integer squares, {a2, b2, c2} with c2 − b2 =
b2−a2, whose terms are constrained to lie in certain regions. As no nontrivial
arithmetic progression of integer squares has more than three terms — stated
by Fermat and proved by Euler (among others) — we refer to three-term
arithmetic progressions more succinctly as just arithmetic progressions, or
APs. (See [Dic13, Vol II, Ch. XIV] for a description of the early history of
this problem).
To study primitive APs of squares, we study the multiple Dirichlet series

D(s, w) := ∑

m,h≥1
(m,h)=1
 r1(h)r1(m)r1(2m − h)
mshw ,

where rℓ(n) denotes the number of ways to represent n as a sum of ℓ squares.
Thus…

2…

## Statements it makes

Theorem (Theorem 7.1). Fix δ ∈ [0, 1]. For any ǫ > 0, the number of
primitive APs of squares {a2, b2, c2} with b2 ≤ X and (a/b)2 ≤ δ is

Theorem (Theorem 8.1). For any ǫ > 0, the number of primitive APs of
squares {a2, b2, c2} with c2 ≤ X is
√2
π2 log(1 + √2)X 1
2 + Oǫ(
X 3
8 +ǫ)
.

Theorem (Theorem 8.3). Suppose that Y ≤ X. For any ǫ > 0, the number
of primitive APs of squares {a2, b2, c2} for which a2 ≤ Y and b2 ≤ X is

Theorem (Theorem 8.4). For any ǫ > 0, the number of primitive APs of
squares {a2, b2, c2} for which ab ≤ X is

Proposition 3.1. The function V (z) lies in L2(Γ0(8)\H; χ).

Lemma 3.2. The Fourier expansion of E(z, s; χ) is

Proposition 3.3. For h ≥ 1 and Re s ≫ 1, we have that

Theorem 4.1. For h ≥ 1 and Re s ≫ 1, we have that

Lemma 4.2. We have that ⟨V, Ea(·, s; χ)⟩ = 0 for the cusps 0 and ∞.

Lemma 4.3. For h ≥ 1 and Re s ≫ 1,

Lemma 4.4. We have ⟨V, µj⟩ ̸= 0 if and only if µj = ⟨fm, fm⟩−1/2fm for
some m ∈ N as in (4.3), in which case

Theorem 5.1. The double Dirichlet series D(s, w) has meromorphic con-
tinuation to C2. For Re s and Re w suﬃciently large, we have

Theorem 7.1. Fix δ ∈ [0, 1]. Then for any ǫ > 0, the number of primitive
APs of squares {h, m, 2m − h} with m ≤ X and (h/m) ≤ δ is

Lemma 7.2. Fix ǫ > 0 and a meromorphic function F (w) satisfying F (w) ≪
| Im w|−ǫ on Re w = σw. Deﬁne H(z) = 1
2πi ∫
(σw) F (w) zw
w dw. Then H(z) is
meromorphic and for z ≥ 0, we have

Lemma 7.3. With the notation as above, we have that

Proposition 7.4. For any ﬁxed ǫ > 0 and δ ∈ [0, 1], we have

Lemma 7.5. On the lines Re z = x ∈ (0, 1
2 ) and Re s = 1
2 + ǫ, we have
∑

Proposition 7.6. For any ǫ > 0 and δ ∈ [0, 1], we have

Theorem 8.1. The number of primitive APs of squares with largest term
at most X is
 1
8 T (X) =
 √
2
π2 log(1 + √2)X 1
2 + Oǫ(X 3
8 +ǫ)

Theorem 8.3. Suppose that Y ≤ X. Then, for any ǫ > 0, the number of
primitive APs of squares {h, m, 2m − h} with h ≤ Y and m ≤ X is

Theorem 8.4. For any ǫ > 0, the number of primitive APs of squares
{h, m, 2m − h} with hm ≤ X is

*[digest of a 64397 character source; every section, statement, and proof in full at `research/sources/hulse-kuan-lowryduda-aps-of-squares-dirichlet-2024.full.md`]*
