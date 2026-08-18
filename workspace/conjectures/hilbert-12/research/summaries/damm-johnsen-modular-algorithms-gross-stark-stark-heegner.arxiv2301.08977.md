> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/damm-johnsen-modular-algorithms-gross-stark-stark-heegner.arxiv2301.08977.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/2301.08977 | converted from PDF -->

## What it claims

In recent work, Darmon, Pozzi and Vonk explicitly construct a modular form whose spectral
coeﬃcients are p-adic logarithms of Gross–Stark units and Stark–Heegner points. Here we
describe how this construction gives rise to a practical algorithm for explicitly computing these
logarithms to speciﬁed precision, and how to recover the exact values of the Gross–Stark units
and Stark–Heegner points from them.
Key tools are overconvergent modular forms, reduction theory of quadratic forms and Newton
polygons. As an application, we tabulate Brumer–Stark units in narrow Hilbert class ﬁelds of real
quadratic ﬁelds with discriminants up to 10000, for primes less than 20, as well as Stark–Heegner
points on elliptic curves.

Contents

1 Introduction 1

2 The modular algorithm 4
2.1 Notation . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 4
2.2 Gross-Stark units and Stark–Heegner points . . . . . . . . . . . . . . . . . . . . . . . 4
2.3 Diagonal restriction derivatives . . . . . . . . . . . . . . . . . . . . . . . . . . . . . . 5
2.4 Improvements using…

3…

## Statements it makes

Theorem 1.1. The form G ∈ M2(Γ0(p)) is non-zero if F = Q(
√D) has no unit of negative norm,
and satisﬁes

Proposition 2.1 ([DPV21b, Prop. 4.6]). The diagonal restriction derivative is an overconvergent
modular form of weight 2 and tame level 1

Theorem 2.2. Set F = Q(
√D) and let p be a prime inert in F . Assume conjecture 3.19 in [DV20,
§3], and write eord(∂f +
ψ ) = λ0E(p)
2 + ∑

Proposition 2.3 ([Cox11, Ex. 7.21]). There is a bijection between ideals of Q(
√D) and indeﬁnite
quadratic forms of discriminant D, given by

Proposition 2.4. Let F = Q(
√D) be a real quadratic ﬁeld and A ∈ Cl
+ a ﬁxed class with associated
reduced quadratic form Q0. Then there is a bijection between

Algorithm 1: Compute set the M (n, A) of nearly reduced forms
Input:

Corollary 2.6. Fix an indeﬁnite quadratic form Q corresponding to a class A ∈ Cl
+ . The series

Algorithm 2: Algorithm for computing logp uA

Proposition 3.1 ([Lem00, Prop. 2.19]). Let F = Q(
√D), and let D = D1 · · · Dt be a factorisation
of D into prime discriminants, meaning ±Di is a prime power with sign chosen so that if Di is odd,
then Di ≡ 1 mod 4. Then the genus ﬁeld of F equals Q(
√D1, . . . , √Dt).

Corollary 3.2. We have #µ(H) > 2 if and only if either of the following holds:

Theorem 3.3 (Meyer). Fix a class A ∈ Cl
+, and let γA ∈ SL2(Z) be the associated matrix. Then

Corollary 3.4. Let uA be a Gross–Stark unit attached to a narrow ideal class A. Then

Algorithm 4: Compute ordP ϵA using Meyer’s formula

Lemma 3.5. Let ϵ be a Brumer–Stark unit in OH [1/p]×, and let P (T ) = ∑d
i=0 aiT i = ad ∏σ∈G(T −
σ(ϵ)) be its minimal polynomial. Then

Lemma 3.6. Let v0 . . . , vd/2−1 be the P-valuations of the conjugates of ϵ which are positive, ordered
so that v0 ≥ v1 ≥ . . . ≥ vd/2−1 ≥ 0, and vd/2 = 0. Then for any i = 0, . . . , d/2 we have ordp(ai) ≥
∑d/2−i
j=0 vd/2−j. In particular, ordp(ad) = ordp(a0) = ∑d/2
j=1 vj.

Algorithm 5: Find the minimal polynomial of ϵA from p-adic approximation of logp ϵA
Input:

Lemma 3.8. Let F be a number ﬁeld, H/F a Galois extension containing all e-th roots of unity,
and α ∈ H ×. Deﬁne χcyc : G ..= Gal(H/F ) → (Z/eZ)× by ζ χcyc(σ) = σ(ζ) for any ζ ∈ µe(H). Then
K ..= H( e√
α)/F is a central extension if and only if for all σ ∈ G there exists some β ∈ H × such
that σ(α) = αχcyc(σ)βe.

Algorithm 6: Find Stark–Heegner point Pψ,f from λf
Input:

*[digest of a 58630 character source; every section, statement, and proof in full at `research/sources/damm-johnsen-modular-algorithms-gross-stark-stark-heegner.arxiv2301.08977.full.md`]*
