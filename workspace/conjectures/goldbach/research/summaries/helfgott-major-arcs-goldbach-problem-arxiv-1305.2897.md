> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/helfgott-major-arcs-goldbach-problem-arxiv-1305.2897.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/1305.2897 | converted from PDF -->

## What it claims

Abstract. The ternary Goldbach conjecture states that every odd number
n ≥ 7 is the sum of three primes. The estimation of the Fourier series∑
p≤x e(αp) and related sums has been central to the study of the problem
since Hardy and Littlewood (1923).
Here we show how to estimate such Fourier series for α in the so-called
major arcs, i.e., for α close to a rational of small denominator. This is part of
the author’s proof of the ternary Goldbach conjecture.
In contrast to most previous work on the subject, we will rely on a ﬁnite
veriﬁcation of the Generalized Riemann Hypothesis up to a bounded conduc-
tor and bounded height, rather than on zero-free regions. We apply a rigorous
veriﬁcation due to D. Platt; the results we obtain are both rigorous and un-
conditional.
The main point of the paper will be the development of estimates on para-
bolic cylinder functions that make it possible to use smoothing functions based
on the Gaussian. The generality of our explicit formulas will allow us to work
with a wide variety of such functions.

Contents

1. Introduction 2
1.1. Results 3
1.2.…

2…

## Statements it makes

Theorem 1.1. Let x be a real number ≥ 108. Let χ be a primitive character
mod q, 1 ≤ q ≤ r, where r = 300000.
Then, for any δ ∈ R with |δ| ≤ 4r/q,

Theorem 1.2. Let η(t) = t2e−t2/2. Let x be a real number ≥ 108. Let χ be a
primitive character mod q, 1 ≤ q ≤ r, where r = 300000.
Then, for any δ ∈ R with |δ| ≤ 4r/q,

Corollary 1.3. Let η(t) = t2e−t2/2 ∗M η2(t), where η2 = η1 ∗M η1 and η1 =
2 · I[1/2,1]. Let x be a real number ≥ 108. Let χ be a primitive character mod q,
1 ≤ q ≤ r, where r = 300000.
Then, for any δ ∈ R with |δ| ≤ 4r/q,

Theorem 1.4. Let η(t) = η+(t) = hH (t)te−t2/2, where hH is as in (1.5) and
H = 200. Let x be a real number ≥ 1012. Let χ be a primitive character mod q,
where 1 ≤ q ≤ 150000 if q is odd, and 1 ≤ q ≤ 300000 if q is even.
Then, for any δ ∈ R with |δ| ≤ 600000 · gcd(q, 2)/q,

Proposition 1.5. Let η(t) = η+(t) = hH(t)te−t2/2, where hH is as in (1.5) and
H = 200. Let x be a real number ≥ 1012.
Then
∞∑

Theorem 3.1. Let fδ(t) = e−t2/2e(δt), δ ∈ R. Let Fδ be the Mellin transform of
fδ. Let s = σ + iτ , σ ≥ 0, τ ̸= 0. Let ℓ = −2πδ. Then, if sgn(δ) ̸= sgn(τ ),

Corollary 3.2. Let fδ(t) = e−t2/2e(δt), δ ∈ R. Let Fδ be the Mellin transform
of fδ. Let s = σ + iτ , where σ ∈ [0, 1] and |τ | ≥ max(100, 4π2|δ|). Then, for
0 ≤ k ≤ 2,

Lemma 3.3. Let E(ρ) and υ(ρ) be as in (3.2). Then

Lemma 4.1. Let η : R+
0 → R be in C 1. Let x ∈ R+, δ ∈ R. Let χ be a primitive
character mod q, q ≥ 1.
Write Gδ(s) for the Mellin transform of η(t)e(δt). Assume that η(t) and η′(t)
are in ℓ2 (with respect to the measure dt) and that η(t)tσ−1 and η′(t)tσ−1 are in
ℓ1 (again with respect to dt) for all σ in an open interval containing [1/2, 3/2].
Then

Lemma 4.1 leaves us with three tasks: bounding the sum of Gδ(ρ)xρ over all
non-trivial zeroes ρ with small imaginary part, bounding the sum of Gδ(ρ)xρ over
all non-trivial zeroes ρ with large imaginary part, and bounding L′(1, χ)/L(1, χ).
Let us start with the last task: while, in a narrow sense, it is optional – in
that, in most of our applications, we will have η(0) = 0, thus making the term
L′(1, χ)/L(1, χ) disappear – it is also very easy and can be dealt with quickly.
Since we will be using a ﬁnite GRH check in all later applications, we might
as well use it here.

Lemma 4.2. Let χ be a primitive character mod q, q > 1. Assume that all
non-trivial zeroes ρ = σ + it of L(s, χ) with |t| ≤ 5/8 satisfy ℜ(ρ) = 1/2. Then
∣
∣
∣
∣ L′(1, χ)
L(1, χ)
 ∣
∣
∣
∣ ≤ 5
2 log M (q) + c,

Lemma 4.3. Let f : R+ → C be piecewise C 1. Assume limt→∞ f (t)t log t = 0.
Let χ be a primitive character mod q, q ≥ 1; let ρ denote the non-trivial zeros
ρ of L(s, χ). Then, for any y ≥ 1,

Lemma 4.4. Let η : R+
0 → R be such that both η(t) and (log t)η(t) lie in L1 ∩ L2
and η(t)/
√t lies in L1 (with respect to dt). Let δ ∈ R. Let Gδ(s) be the Mellin
transform of η(t)e(δt).
Let χ be a primitive character mod q, q ≥ 1. Let T0 ≥ 1.…

Lemm…


*[further statements in the full text]*

*[digest of a 153395 character source; every section, statement, and proof in full at `research/sources/helfgott-major-arcs-goldbach-problem-arxiv-1305.2897.full.md`]*
