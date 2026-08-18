> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/tao-every-odd-integer-sum-of-at-most-five-primes-arxiv-1201.6656.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/1201.6656 | converted from PDF -->

## What it claims

Abstract. We prove that every odd number N greater than 1 can be expressed as
the sum of at most ﬁve primes, improving the result of Ramar´e that every even natural
number can be expressed as the sum of at most six primes. We follow the circle method
of Hardy-Littlewood and Vinogradov, together with Vaughan’s identity; our additional
techniques, which may be of interest for other Goldbach-type problems, include the use
of smoothed exponential sums and optimisation of the Vaughan identity parameters to
save or reduce some logarithmic losses, the use of multiple scales following some ideas
of Bourgain, and the use of Montgomery’s uncertainty principle and the large sieve
to improve the L2 estimates on major arcs. Our argument relies on some previous
numerical work, namely the veriﬁcation of Richstein of the even Goldbach conjecture
up to 4 × 1014, and the veriﬁcation of van de Lune and (independently) of Wedeniwski
of the Riemann hypothesis up to height 3.29 × 109.

1. Introduction

Two of most well-known conjectures in additive number theory are the even and odd
Goldbach conjectures,…

## Statements it makes

Conjecture 1.1 (Even Goldbach conjecture). Every even natural number x can be
expressed as the sum of at most two primes.

Conjecture 1.2 (Odd Goldbach conjecture). Every odd number x larger than 1 can be
expressed as the sum of at most three primes.

Theorem 1.3 (Exponential sum estimate). Let x ⩾ 1020 be a real number, and let
4α = a
q + β for some natural number 100 ⩽ q ⩽ x/100 with (a, q) = 1 and some
β ∈ [−1/q2, 1/q2]. Let q0 be a natural number, such that all prime factors of q0 do not
exceed √x. Then

Theorem 1.4. Every odd number x larger than 1 can be expressed as the sum of at
most ﬁve primes.

Theorem 1.5 (Numerical veriﬁcation of Riemann hypothesis). Let T0 := 3.29 × 109.
Then all the zeroes of the Riemann zeta function ζ in the strip {s : 0 < ℜ(s) < 1; 0 ⩽
ℑ(s) ⩽ T0} lie on the line ℜ(s) = 1/2. Furthermore, there are at most 1010 zeroes in
this strip.

Theorem 1.6 (Numerical veriﬁcation of even Goldbach conjecture). Let N0 := 4×1014.
Then every even number between 4 and N0 is the sum of two primes.

Lemma 3.1. Let α ∈ R/Z, and let F : R → C be a smooth, compactly supported
function. Then we have the bounds
∑

Corollary 3.2. With the same hypotheses as Lemma 3.1, we have

Lemma 3.3. Let F : R → C be a smooth, compactly supported function. Then one has
∣
∣
∣
∣
∫

Lemma 3.4 (Vinogradov-type lemma). Let α = a
q + β for some β = O∗(1/q2). Then
for any x < y, A, B > 0, and θ ∈ R/Z, we have
∑

Corollary 3.5 (Restricting to odd integers). Let 2α = a
q + β for some β = O∗(1/q2).
Then for any x < y, A, B > 0, and θ ∈ R/Z, we have
∑

Lemma 3.6 (Large sieve inequality). Let ξ1, . . . , ξR ∈ R/Z be such that ∥ξi −ξj∥R/Z ⩾ δ
for all 1 ⩽ i < j ⩽ R and some δ > 0. Let I = [N1, N2] be an interval of length
|I| = N2 − N1 ⩾ 1. Then we have

Corollary 3.7 (Special case of large sieve inequality). Let I, J ⊂ R be intervals of
length at least 1, and let α ∈ R/Z. Then one has

Corollary 3.8 (Restricting to odd numbers). Let I, J ⊂ R be intervals of length at
least 2, and let α ∈ R/Z. Then one has

Corollary 3.9 (Subdivision). Let I, J ⊂ R be intervals of length at least 2, and let
α ∈ R/Z. Let M ⩾ 1. Then one has

Lemma 4.1. We have

Lemma 4.2. If η is smooth, then one has

Lemma 4.3. We have

Lemma 4.4 (Montgomery’s uncertainty principle). For any q0 dividing q, we have

Lemma 4.5 (Global L
2 estimate). We have
∫

Lemma 4.6 (Local L
2 estimate). Let Q, R ⩾ 1, and let Σ ⊂ R/Z be the set

Corollary 4.7. If 0 < r < 1/2 and √
1/2r♯|q, one has
∫
∥α∥R/Z⩽r |Sη,q(x, α)|2 dα ⩽ 2

Proposition 4.8. Let η be smooth and 0 ⩽ r ⩽ 1/2. Then
∫
∥α∥R/Z⩽r |Sη,q(x, α)|2 dα ⩾ (Sη2,q(x, 0) − 1
π2rx∥η′η′ + ηη′′∥L1(R)Sη,q(x, 0))2
+
∥η∥2
L2(R)x + ∥ηη′∥L1(R) .

Corollary 4.9. Let η be smooth and supported on [c, 1] for some c > 0, and suppose
that 1
2x ⩽ r ⩽ 1/2 and q = √x♯. We normalise ∥η∥L2(R) = 1. Assume furthermore that

Proposition 4.10 (Mesoscopic L
2 estimate). Suppose that…


*[further statements in the full text]*

*[digest of a 84593 character source; every section, statement, and proof in full at `research/sources/tao-every-odd-integer-sum-of-at-most-five-primes-arxiv-1201.6656.full.md`]*
