> **Digest only — read this first.** This is a structural digest of the source: its outline, what it claims, and the statements it makes. The complete text is at `research/sources/helfgott-ternary-goldbach-conjecture-is-true-arxiv-1312.7748.full.md`; open that only when this file does not answer the question, because it is large. Replace this digest with a summary of what the source establishes and what it implies for this problem — under 1000 tokens, specific enough that nobody needs the full text, and wikilinking it so they can still reach it.

<!-- source: https://arxiv.org/pdf/1312.7748 | converted from PDF -->

## What it claims

Abstract. The ternary Goldbach conjecture, or three-primes problem, as-
serts that every odd integer n greater than 5 is the sum of three primes. The
present paper proves this conjecture.
Both the ternary Goldbach conjecture and the binary, or strong, Goldbach
conjecture had their origin in an exchange of letters between Euler and Gold-
bach in 1742. We will follow an approach based on the circle method, the
large sieve and exponential sums. Some ideas coming from Hardy, Littlewood
and Vinogradov are reinterpreted from a modern perspective. While all work
here has to be explicit, the focus is on qualitative gains.
The improved estimates on exponential sums are proven in the author’s
papers on major and minor arcs for Goldbach’s problem. One of the highlights
of the present paper is an optimized large sieve for primes. Its ideas get
reapplied to the circle method to give an improved estimate for the minor-arc
integral.
 Contents

1. Introduction 2
1.1. Results 2
1.2. History 3
1.3. Main ideas 5
1.4. Dependency diagram 7
1.5. Acknowledgments 8
2. Preliminaries 8
2.1. Notation 8
2.2.…

## Statements it makes

Corollary 1.1 (to Main Theorem). Every integer n > 1 is the sum of at most 4
primes.

Lemma 3.1. Let η : [0, ∞) → R be in L1 ∩ L∞. Let Sη(α, x) be as in (3.1) and
let M = Mδ0,r be as in (3.5). Let η◦ : [0, ∞) → R be thrice diﬀerentiable outside
ﬁnitely many points. Assume η(3)
◦ ∈ L1.
Assume r ≥ 182. Then
(3.26)∫

Proposition 3.2. Let x ≥ 1. Let η+, η∗ : [0, ∞) → R. Assume η+ ∈ C2, η′′
+ ∈ L2
and η+, η∗ ∈ L1 ∩ L2. Let η◦ : [0, ∞) → R be thrice diﬀerentiable outside ﬁnitely
many points. Assume η(3)
◦ ∈ L1 and |η+ − η◦|2 < ϵ0|η◦|2, where ϵ0 ≥ 0.

Lemma 4.1. Let V be a real vector space with an inner product ⟨·, ·⟩. Then, for
any v, w ∈ V with |w − v|2 ≤ |v|2/2,

Lemma 4.2. For any q ≥ 1 and any r ≥ max(3, q),
q
φ(q) < ϝ(r),

Lemma 4.3. Let gx(r) be as in (4.13) and h(x) as in (4.16). Then

Lemma 4.4. Let Rx,r be as in (4.13). Then t → Ret,r(r) is convex-up for
t ≥ 3 log 6r.

Proposition 4.5. Let x ≥ Kx0, x0 = 2.16 · 1020, K ≥ 1. Let Sη(α, x) be as
in (3.1). Let η∗ = η2 ∗M ϕ, where η2 is as in (4.10) and ϕ : [0, ∞) → [0, ∞) is
continuous and in L1.
Let 2α = a/q + δ/x, q ≤ Q, gcd(a, q) = 1, |δ/x| ≤ 1/qQ, where Q = (3/4)x2/3.
If q ≤ (x/K)1/3/6, then

Lemma 4.6. Let x > K · (6e)3, K > 1. Let η∗ = η2 ∗M ϕ, where η2 is as in
(4.10) and ϕ : [0, ∞) → [0, ∞) is continuous and in L1. Let gx,ϕ be as in (4.20).
Then gx,ϕ(r) is a decreasing function of r for r ≥ 175.

Lemma 4.7. Let x ≥ 1025. Let φ : [0, ∞) → [0, ∞) be continuous and in L1.
Let gx,φ(r) and h(x) be as in (4.20) and (4.16), respectively. Then

Proposition 5.1. Let {an}∞
n=1, an ∈ C, be supported on the primes. Assume
that {an} is in ℓ1 ∩ ℓ2 and that an = 0 for n ≤ √x. Let Q0 ≥ 1, δ0 ≥ 1 be such
that δ0Q2
0 ≤ x/2; set Q = √
x/2δ0 ≥ Q0. Let

Proposition 5.2. Let {an}∞
n=1, an ∈ C, be supported on the primes. Assume
that {an} is in ℓ1 ∩ ℓ2 and that an = 0 for n ≤ √x. Let Q0 ≥ 1, δ0 ≥ 1 be such
that δ0Q2
0 ≤ x/2; set Q = √
x/2δ0 ≥ Q0. Let M = Mδ0,Q0 be as in (3.5).
Let S(α) = ∑
n ane(αn) for α ∈ R/Z. Then

Lemma 5.3. Let m ≥ 1, q ≥ 1. Then

Lemma 5.4. Let Q0 ≥ 1, Q ≥ 182Q0. Let q ≤ Q0, s ≤ Q0/q, q an integer.
Then
 Gq(Q0/sq)
Gq(Q/sq) ≤ eγ log ( Q0
sq + log q) + 1.172

Lemma 5.4 will play a crucial role in reducing to a ﬁnite computation the
problem of bounding Gq(Q0/sq)/Gq(Q/sq). As we will now see, we can use
Lemma 5.4 to obtain a bound that is useful when sq is large compared to Q0
– precisely the case in which asymptotic estimates such as (5.12) are relatively
weak.

Lemma 5.5. Let Q0 ≥ 1, Q ≥ 200Q0. Let q ≤ Q0, s ≤ Q0/q. Let ρ =
(log Q0)/ log Q ≤ 2/3. Then, for any σ ≥ 1.312ρ,

Proposition 5.6. Let Q ≥ 20000Q0, Q0 ≥ Q0,min, where Q0,min = 105. Let
ρ = (log Q0)/ log Q. Assume ρ ≤ 0.6. Then, for every 1 ≤ q ≤ Q0 and every
s ∈ [1, Q0/q],

Corollary 5.7. Let {an}∞
n=1, an ∈ C, be supported on the primes. Assume that
{an} is in ℓ1 ∩ ℓ2 and that an = 0 for n ≤ √
x. Let Q0 ≥ 105, δ0 ≥ 1 be such that…

Corol…


*[further statements in the full text]*

*[digest of a 150058 character source; every section, statement, and proof in full at `research/sources/helfgott-ternary-goldbach-conjecture-is-true-arxiv-1312.7748.full.md`]*
